---
name: mark_outreached
description: Mark a prepared company as outreached. Updates status + first-email-sent date, moves it from 2-ready-to-outreach/ to 3-outreached/, rebuilds README, commits.
argument-hint: <company-name>
allowed-tools: Read, Edit, Glob, Bash, SlashCommand
---

# /mark_outreached

Call this when the first email of a sequence has gone out via Gong.

## Step 1 — Resolve the file

Normalize `$ARGUMENTS` (lowercase · non-alphanumeric → hyphen · collapse · trim) and look
for `2-ready-to-outreach/{normalized-name}.md`. If no exact match, Glob `*{normalized-name}*`
in that folder. Multiple matches: list and ask.

If not found: tell Prateek it isn't in `2-ready-to-outreach/` — it may already be in
`3-outreached/`, or still in `1-to-outreach/` awaiting a batch run.

## Step 2 — Update the header

- `**Status:** 🟢 Ready to outreach — sequence drafted` → `**Status:** 🔵 Outreached — sequence active`
- Replace `**First email sent:** —` with today's date (`YYYY-MM-DD`).

Preserve every other header field and all three `<details>` sections.

## Step 3 — Move

```bash
git mv 2-ready-to-outreach/{normalized-name}.md 3-outreached/{normalized-name}.md
```

## Step 4 — Rebuild README

Invoke `/pipeline_update`. It does not commit.

## Step 5 — Commit

```bash
git add README.md 3-outreached/{normalized-name}.md
git commit -m "sent: {Original Company Name} — moved to outreached"
```

## Step 6 — Confirm

`{Company Name} marked as outreached on {YYYY-MM-DD} — moved to 3-outreached/.`

## Hard rules

- **Never** modify the file body — only the two header lines change.
- **Never** stamp the date if `**First email sent:**` already carries one. Stop and ask.
- **Never** move a file whose status isn't 🟢. If 🟡 or 🔴, stop and flag.
