---
name: pipeline_update
description: Scan all pipeline folders and rebuild README.md with current state. Does NOT commit — the caller handles git.
argument-hint: (no arguments)
allowed-tools: Read, Write, Glob, Bash
---

# /pipeline_update

Rebuild `README.md` to reflect current pipeline state. Called by `/prepare_batch`,
`/mark_outreached` and `/mark_not_icp`; can be run manually after hand edits.

**This skill does NOT commit or push.**

---

## Step 1 — Scan the four folders

List `.md` files (excluding `_README.md`, `_template.md`, `.gitkeep`) in `1-to-outreach/`,
`2-ready-to-outreach/`, `3-outreached/`, `not-icp/`.

### 1-to-outreach/ (stub format)
```
# {Company Name}

**Website:** {domain} · **Industry:** {industry} · **HQ:** {country}
**Priority:** {P1/P2/P3} · **Added:** {YYYY-MM-DD}

## Notes
...
```

### Other folders (full template format)
```
# {Company Name}

**Status:** {emoji + label}
**ICP Score:** {N} / 24 → {tier}
**Industry:** {industry} · **HQ:** {country} · **Researched:** {date} · **First email sent:** {date or —}
**Motion:** {greenfield / displacement / in-house / competitive}
```

**Parsing rules:** missing or unparseable field → `—`. Split header lines on ` · `. A
malformed file is logged as `{filename} (parse error)` in a footnote; it never fails the run.

---

## Step 2 — Assemble

Capture the current timestamp as `YYYY-MM-DD HH:MM`. Write:

````markdown
# APAC Outreach Pipeline

*Last updated: {YYYY-MM-DD HH:MM}*

> Internal target-account data. This repository must remain **private**.
> Setup and usage: [SETUP.md](SETUP.md)

## 📋 To Outreach ({N})

{If N < 20:}
> ⚠️ Below minimum of 20. Top up before next batch.

| Company | Industry | HQ | Priority | Added |
|---------|----------|----|----------|-------|
| [{Name}](1-to-outreach/{filename}) | {Industry} | {HQ} | {P1} | {Added} |
{sorted by Priority (P1 → P3 → none), then Added ascending}

## 🟢 Ready to Outreach ({N})

*Sequences drafted. Copy from each company file and send via Gong / Chief.*

| Company | Industry | ICP | Motion | Researched |
|---------|----------|-----|--------|------------|
| [{Name}](2-ready-to-outreach/{filename}) | {Industry} | {N}/24 | {motion} | {date} |
{sorted by ICP descending}

## 🔵 Outreached ({N})

| Company | Industry | ICP | First Sent |
|---------|----------|-----|------------|
| [{Name}](3-outreached/{filename}) | {Industry} | {N}/24 | {date} |
{sorted by First Sent descending, limit 30}

{If truncated:}
> *+ {N - 30} more in [3-outreached/](3-outreached/)*

## 🔴 Not ICP ({N})

See [not-icp/](not-icp/) for rejection rationale.
````

**Rendering details:**
- Link each company name to its file with a relative markdown link.
- Counts exclude scaffolding files.
- A section with 0 rows renders as an empty table with just the header — never omit a section.
- Queue warning only in To Outreach, only when count < 20.
- Truncation footnote only when Outreached > 30.

---

## Step 3 — Save

Overwrite `README.md`. Do not stage, commit or push.

## Step 4 — Confirm

One line: `README.md rebuilt — 46 to-outreach · 3 ready · 0 outreached · 0 not-icp.`
Echo the queue warning in the summary if it fired.

## Hard rules

- **Never** commit, push or stage.
- **Never** modify any file other than `README.md`.
- **Never** skip a section.
- **Always** include the `*Last updated: ...*` line and the private-repo notice.
