# 1-to-outreach

Queue of APAC accounts awaiting research and outreach prep.
Minimum target: 20 active stubs.

Stubs are generated from `accounts/apac-tal.csv` by `scripts/make_stubs.py`, or created by
hand from `_template.md`.

Processing order is by `**Priority:**` (P1 → P2 → P3 → unprioritized), then oldest `Added`
date within a tier.

To run a batch:
- `/prepare_batch 3` — auto-pick 3 by queue priority
- `/prepare_batch YuppTV "Great Learning" "Air New Zealand"` — process these specific stubs
- `/prepare_batch 5 YuppTV` — YuppTV plus 4 auto-picked

Add anything you already know to the `## Notes` block before running. A known PSP, a payment
hire, an expansion announcement or a contact name is worth ten web searches — and it gets
injected into the research run as context.
