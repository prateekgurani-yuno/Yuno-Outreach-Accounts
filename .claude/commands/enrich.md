---
name: enrich
description: Find work emails for people from a Sales Navigator list (screenshot, pasted text, or CSV) through Yuno's Freckle email waterfall, and save them as a CSV. Use when the user types /enrich or asks to find emails for Sales Navigator leads.
argument-hint: <screenshots, pasted list, or CSV path>
allowed-tools: Read, Write, Bash, WebSearch
---

# /enrich

Turns a Sales Navigator list into a CSV of work emails. Freckle tries LeadMagic, then Findymail, and checks every hit with ZeroBounce.

## 0. Check the token

Run `python3 enrich/enrich.py --check` first. If it fails, relay its message and stop:
- no token → the user sets `FRECKLE_API_KEY` in the environment settings and starts a new session;
- HTTP 401/403 → the token is wrong or revoked; ask Hernán for a new one;
- could not reach the API → `next-api.freckle.io` must be allowed in the environment's network access.

## 1. Read the list

The user gives one of:
- screenshots of a Sales Navigator lead list or account people page,
- pasted text copied from Sales Navigator,
- a CSV.

Extract one row per person: `name`, `title`, `company`. Read every screenshot fully; do not stop at the first one.

Clean names before lookup:
- Drop suffixes and decorations: degrees (MBA, PhD, CPA), pronouns, emojis, text in brackets after the name.
- If a name is written in Japanese, Korean or Chinese script, write it in Latin letters, given name first (田中 太郎 → Taro Tanaka; 김민준 → Minjun Kim), and keep the original in a `name_original` column.
- If the list already shows a Latin name, keep it as shown.

## 2. Confirm the company domain

Freckle needs the company's email domain, and a wrong domain returns wrong or no emails.
- For each distinct company, propose the domain its employees use for email (the corporate site, not a product or regional marketing site). Use web search if unsure.
- Show the user a short table `company → domain` and ask them to confirm or correct it. Never run on a domain the user has not confirmed.

## 3. Confirm and run

Save the rows to `enrich/runs/<company-or-list>-<YYYY-MM-DD>.csv` (relative to the repository root) with the header `name,title,company,domain` (plus `name_original` when used). Create the folder if needed.

Tell the user how many people will be looked up (each lookup spends Freckle credits) and wait for a yes. Then run:

```
python3 enrich/enrich.py "<input.csv>"
```

It prints one line per person and writes `<input>-emails.csv` next to the input. A run takes up to a few minutes; wait for it in the foreground with a 10-minute command timeout.

## 4. Report

Reply with:
- the counts line the script printed (valid / found but not valid / not found),
- a table of the people with valid emails,
- the path of the output CSV.

`email_valid = no` with an email means ZeroBounce could not confirm it: usable with care, not safe for a cadence. If most rows fail with `http_401` or `http_403`, the token is wrong or revoked: tell the user to ask Hernán for a new one and update `FRECKLE_API_KEY`.

Cloud sessions are ephemeral: the output CSV is lost when the container is reclaimed unless it is committed or downloaded. Ask the user which they want.
