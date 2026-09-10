# APAC Outreach Pipeline — Setup & Usage

A Claude Code–driven system for low-volume, high-personalization enterprise outreach across
APAC. Feed it a company name; it researches the payment stack, scores it against a 24-point
APAC ICP matrix, drafts a 12-touch outreach sequence, and tracks the prospect through the
pipeline — all as version-controlled Markdown.

Adapted from the EMEA pipeline, with the payments logic rebuilt for this territory.

---

## ⚠️ This repository must stay private

It holds the full APAC target account list (1,215 accounts with revenue estimates),
competitive intelligence including confirmed orchestrator relationships, prospect research,
and stakeholder notes. Confirm `Settings → General → Danger Zone → visibility = Private`
before pushing anything.

---

## 1. How the pipeline works

```
1-to-outreach/          2-ready-to-outreach/        3-outreached/
(queue)          ──►    (researched + drafted)  ──► (sequence sent)
                   │
                   └──► not-icp/  (rejected, with rationale)
```

| Stage | Folder | Contents |
|-------|--------|----------|
| **1. Queue** | `1-to-outreach/` | Stubs — company, domain, priority, prior context. Generated from the TAL or copied from `_template.md`. |
| **2. Ready** | `2-ready-to-outreach/` | Full payment-intel report + ICP score + drafted 12-touch sequence. Copy-paste ready. |
| **3. Outreached** | `3-outreached/` | Sequence started, first-send date stamped. |
| **Rejected** | `not-icp/` | Below threshold or overridden, with rationale. |

`README.md` is an **auto-generated dashboard** — never edit by hand; `/pipeline_update`
rebuilds it. Batch runs are logged in `batches/`.

## 2. The skills

Invoked as slash commands with this repo as the working directory.

| Command | What it does |
|---------|--------------|
| `/research <company>` | Five-agent payment-intelligence run. Scores against the 24-point APAC ICP matrix. Saves to `2-ready-to-outreach/{name}.md`. |
| `/full-outreach <company>` | Drafts the 12-touch sequence — 5 emails + 4 LinkedIn + 3 manual touches across 23 days — into the company file's Section 2. |
| `/prepare_batch [N] [names...]` | Takes N companies from the queue, researches each, then rejects (<8) or drafts outreach (≥8). Auto-tops-up from the queue. Writes a batch log. |
| `/mark_outreached <company>` | Moves to `3-outreached/`, stamps the send date. |
| `/mark_not_icp <company> [\| reason]` | Rejects from anywhere in the pipeline with a dated rationale. |
| `/pipeline_update` | Regenerates the `README.md` dashboard. Does not commit. |

Reference files the skills read:
- `.claude/reference/apac-payments.md` — market rails, regulatory gates, cross-border
  framing, the Juspay displacement motion. Read by `/research` on every run.
- `.claude/reference/subscription-payments.md` — recurring billing, APAC mandate rules, and
  the app-store trap. Read when the prospect has a recurring model.
- `.claude/reference/email-samples.md` — voice anchor for `/full-outreach`. **Currently a
  placeholder.**

## 3. Day-to-day flow

1. Top up the queue: `python3 scripts/make_stubs.py --priority P1`
2. Paste SimilarWeb data into `accounts/traffic/{name}.md` for the companies you're about to
   run (see that folder's README for the format).
3. `/prepare_batch 3`
4. Review the drafted files. **Check the Source Notes block** — anything ⚠️ unverified must
   be rewritten or cut before sending.
5. Send emails via Gong, LinkedIn via Chief.
6. `/mark_outreached <company>` as each sequence starts.

## 4. What changed from the EMEA pipeline

| Area | EMEA | APAC |
|---|---|---|
| **ICP matrix** | Public RFP +3 | Removed from the matrix — rare in this territory. Now an **override**: a confirmed public payment RFP escalates to ⭐ High Priority regardless of score. |
| | — | **Local rail / licensing gap +3** added. The strongest and most common orchestration trigger here. |
| | No orchestrator +4 (binary) | **Graded**: greenfield +4 · regional orchestrator such as Juspay +3 (displacement) · in-house or global-competitor incumbent +1. |
| **Cross-border framing** | Heavy IFR caveat — intra-EEA carries no interchange premium | No regional cap regime exists in APAC. Cross-border is argued **per corridor**, leading with approval rate, then FX, then regulatory gating. |
| **Entity gaps** | A cost inefficiency | Often a **regulatory blocker** — India, Indonesia, China, Vietnam and Korea gate domestic acquiring behind local presence or a licensed partner. |
| **Rails** | Card-first, APMs as conversion upside | Account-to-account and wallet rails are the default in several of the largest markets. Instalments/EMI are a conversion rail, not a convenience. |
| **Motion** | Mostly greenfield | A large part of the Indian market is already orchestration-aware via Juspay. `/full-outreach` carries a motion override so a displacement account is never opened with "you have no orchestration layer." |
| **Recurring** | Standard card-on-file logic | India e-mandate rules and UPI Autopay break naive retry logic. The strongest recurring hook in the territory. |
| **Qualification** | Implicit | Explicit **Phase 0 gate** in `/research` — PSP, existing customer, no online volume, out of territory. |
| **Paths** | Hardcoded `~/yuno-outreach` | Repo-relative. Open Claude Code at the repo root. |
| **Push** | Auto-push on every skill | Skills commit but **do not push**. |
| **Missing file** | `subscription-industry-reference.md` referenced but absent | Written, as `.claude/reference/subscription-payments.md`. |
| **Setup vs dashboard** | Both were `README.md` — the dashboard overwrote the guide | Split: `SETUP.md` is this guide, `README.md` is the generated dashboard. |

## 5. Known gaps

- **`.claude/reference/email-samples.md` is a placeholder.** Until it holds real samples,
  `/full-outreach` produces structurally correct but generically voiced copy.
- **Identity placeholders.** `full-outreach.md` carries `{{TODO}}` for the sending address
  and calendar link. The calendar link appears in five touches.
- **No SimilarWeb MCP** in the current environment. Traffic data must be supplied per
  company, or research falls back to web-search estimates.
- **The success case library is LATAM-weighted.** Tier 1 matches for APAC prospects are
  thin. `/full-outreach` searches y.uno before defaulting and is forbidden from implying a
  LATAM case's numbers came from Asia. Internal APAC references would fix this.

## 6. Data

- `accounts/apac-tal.csv` — the target account list (1,215 accounts). Every column is an
  unverified starting hypothesis; `/research` confirms with a source or drops it.
- `accounts/traffic/` — supplied SimilarWeb data, one file per company.
- `scripts/make_stubs.py` — generates queue stubs from the TAL. Safe to re-run; never
  overwrites an existing stub or recreates one already processed.
