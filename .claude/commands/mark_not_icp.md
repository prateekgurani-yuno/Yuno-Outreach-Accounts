---
name: mark_not_icp
description: Manually reject a company from anywhere in the pipeline. Appends a Rejection Rationale, sets status 🔴, moves to not-icp/, rebuilds README, commits.
argument-hint: <company-name> [| reason]
allowed-tools: Read, Edit, Glob, Bash, SlashCommand
---

# /mark_not_icp

Manual override for when an account doesn't fit — vertical mismatch, hard objection,
app-store-dominated revenue, out of territory, already a Yuno customer. Distinct from
`/prepare_batch`'s automatic threshold rejection.

## Step 1 — Parse

`$ARGUMENTS` splits on `|`: **Segment 1** company name (required), **Segment 2** reason
(optional, defaults to `"Manual review"`). Normalize the name.

## Step 2 — Locate

Search in order: `1-to-outreach/`, `2-ready-to-outreach/`, `3-outreached/`. Fall back to
Glob `*{normalized-name}*` in each. Multiple matches: list and ask. Not found anywhere: say
so — it may already be in `not-icp/`.

Record the source folder and full path.

## Step 3 — Update

### 3a. Append the rationale

```markdown


---

## Rejection Rationale

{reason, or "Manual review"}

*Marked: {YYYY-MM-DD}*
```

From `1-to-outreach/` (stub, no collapsibles): append at the end.
From the other folders: append **after the last `</details>`** so it stays visible.

### 3b. Update the status header

Where a `**Status:**` line exists, replace it with `**Status:** 🔴 Not ICP`.
Stub files have no status line — the move is the signal.

## Step 4 — Move

```bash
git mv {source-folder}/{normalized-name}.md not-icp/{normalized-name}.md
```

## Step 5 — Rebuild README

Invoke `/pipeline_update`.

## Step 6 — Commit

```bash
git add README.md not-icp/{normalized-name}.md
git commit -m "reject: {Original Company Name} — manual"
```

## Step 7 — Confirm

`{Company Name} marked as Not ICP (reason: {reason}) — moved from {source-folder}/ to not-icp/.`

## Hard rules

- **Never** overwrite an existing `## Rejection Rationale`. Append a second dated one beneath.
- **Never** modify the body sections — the rejection is additive.
- **Always** date-stamp so the rejection is traceable.
