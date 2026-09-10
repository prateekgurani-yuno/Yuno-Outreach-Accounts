---
name: prepare_batch
description: Process a batch of companies from 1-to-outreach/ — for each, run /research, score ICP, then either reject (move to not-icp/) or run /full-outreach. Auto-replaces rejects from the queue. Rebuilds README.md and writes a batch log.
argument-hint: [N] [company-name-1] [company-name-2] ...
allowed-tools: Read, Edit, Write, Glob, Bash, SlashCommand
---

# /prepare_batch

```
1-to-outreach/{name}.md  →  /research {name}  →  2-ready-to-outreach/{name}.md (with ICP score)
                                                       ↓
                                  ICP < 8  →  not-icp/{name}.md (rejected)
                                  ICP ≥ 8  →  /full-outreach {name}  →  ready
```

All paths are relative to the repository root.

---

## Step 1 — Parse arguments

`$ARGUMENTS` tokenizes on whitespace.

- **Numeric tokens** → target batch count (take the largest if several).
- **Non-numeric tokens** → explicit company names, each matching (after normalization) a
  file in `1-to-outreach/`.

**Resolution:**
- Count only (`/prepare_batch 5`): auto-pick 5 from `1-to-outreach/` by **queue priority**
  — P1 stubs first, then P2, then P3, then unprioritized; within a tier, oldest `Added`
  date first. (The stub header carries a `**Priority:**` field.)
- Names only (`/prepare_batch YuppTV "Great Learning"`): count = number of names.
- Both: explicit names first, then auto-pick the remainder.
- Count > available stubs: process all available and warn at the end.

**Normalization:** lowercase · non-alphanumeric → hyphen · collapse hyphens · trim.
So `"YuppTV"` → `yupptv.md`, `"Air New Zealand"` → `air-new-zealand.md`.

If an explicit name doesn't match any file, stop and ask Prateek. Do not start the batch.

---

## Step 2 — Pre-flight

- Confirm `1-to-outreach/` has at least 1 stub.
- Record the start time as `YYYY-MM-DD-HH-MM` for the batch log filename.
- Note the starting queue count.
- **Confirm traffic data availability.** For each company in the batch, check whether
  SimilarWeb data has been supplied (in conversation or `accounts/traffic/{name}.md`). List
  any company with no data before starting — research still runs, but the country profile
  will be estimate-grade and two ICP signals will be unverifiable. Let Prateek decide
  whether to proceed or supply the data first.

---

## Step 3 — Per-company loop

### 3a. Read the stub
Read `1-to-outreach/{normalized-name}.md`. Extract the freeform content under `## Notes` —
manual context Prateek captured — and the header fields (Industry, HQ, Priority, Website).

### 3b. Run research
Invoke `/research {Original Company Name}` with the notes injected as additional context.

### 3c. Parse the ICP score
Read the saved file, find `**ICP Score:** {N} / 24 → {tier}`, extract `N`.

### 3d. Branch on score

**If N < 8, or an analyst override rejects the account:**

1. Append inside the Section 3 `<details>` block, just before its closing `</details>`:

   ```markdown
   ## Rejection Rationale

   {1–2 sentences citing the specific missing signals, or the override reasoning.}
   ```

2. Update the status header to `**Status:** 🔴 Not ICP — score {N}/24`
   (or `— analyst override` where the override, not the score, drove it).

3. Move and clean up:
   ```bash
   git mv 2-ready-to-outreach/{normalized-name}.md not-icp/{normalized-name}.md
   git rm 1-to-outreach/{normalized-name}.md
   git commit -m "reject: {Original Company Name} — ICP {N}/24 below threshold"
   ```

4. **Pull a replacement** — the next stub by queue priority, excluding anything already in
   this batch and the scaffolding files. If the queue is exhausted, continue without one.

**If N ≥ 8:**

1. Invoke `/full-outreach {Original Company Name}`.
2. Clean up the stub:
   ```bash
   git rm 1-to-outreach/{normalized-name}.md
   git commit -m "prep: {Original Company Name} → ready"
   ```

### 3e. Track results
Company name, normalized filename, ICP score, motion, outcome (`ready` / `not-icp`),
whether it was a replacement pull, and whether traffic data was supplied or estimated.

---

## Step 4 — End of batch

### 4a. Rebuild the dashboard
Invoke `/pipeline_update`. It does not commit — this skill commits the README change.

### 4b. Write the batch log

Write `batches/{YYYY-MM-DD-HH-MM}.md`:

```markdown
# Batch — {YYYY-MM-DD HH:MM}

**Target count:** {N requested}
**Processed:** {actual}
**Ready:** {M}
**Not ICP:** {K}
**Replacements pulled:** {R}
**Time taken:** {approx minutes}

## Companies processed

| Company | ICP | Motion | Traffic data | Outcome | Replacement? |
|---------|-----|--------|--------------|---------|--------------|
| {Name} | {N}/24 | {greenfield/displacement/in-house} | supplied / estimated | ✅ ready / 🔴 not-icp | — / yes |

## Key research flags (read before outreach)

{Anything that contradicts the stub premise, could not be verified, or changes the angle.
This section is the point of the log — be specific and blunt.}

## Queue status after batch

- `1-to-outreach/` count: {N remaining}
{Warning line if < 20:}
> ⚠️ Below minimum of 20. Top up before next batch.
```

### 4c. Final commit
```bash
git add README.md batches/{YYYY-MM-DD-HH-MM}.md
git commit -m "batch: {YYYY-MM-DD} — {M} ready, {K} not-icp"
```

Push only when Prateek has confirmed the remote is private and asked for a push.

---

## Step 5 — Final report

Summarize in chat, ≤ 8 lines: timestamp, companies and outcomes, ICP range, replacements,
queue warning if under 20, and any account where the research contradicted the stub.

---

## Hard rules

- **Never** invoke `/full-outreach` on a rejected company.
- **Never** auto-pick `_README.md` or `_template.md`.
- **Never** push to a public remote.
- **Always** check the stub exists before invoking `/research` (a missing stub is fatal, not
  a skip).
- **Always** write the batch log, even for a partial or failed batch.
- **Always** surface research findings that contradict the stub's premise. A stub note is
  Prateek's hypothesis, not a fact — the EMEA pack has a worked case where a stub's central
  premise was four years out of date.

## Edge cases

- **`/research` fails:** record it, leave the stub in place, continue. Do not delete the stub.
- **`/full-outreach` fails:** file stays in `2-ready-to-outreach/` at 🟡. Note it and surface
  it so Prateek can re-run manually.
- **Score line missing or unparseable:** treat as a research failure, log, continue.
- **Duplicate names:** dedupe silently.
- **Name already in `2-ready-to-outreach/` or `3-outreached/`:** stop and ask.
- **Company is a PSP or existing Yuno customer:** the Phase 0 gate in `/research` catches
  this — record as `not-icp` with the gate reason, do not run outreach.
