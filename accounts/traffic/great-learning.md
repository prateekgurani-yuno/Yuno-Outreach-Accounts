# Great Learning — SimilarWeb

**Pulled:** 2026-09-10 (supplied by Prateek, screenshot transcription)
**Period:** Jun 2026 – Aug 2026 · All traffic
**Domain:** greatlearning.in
**"Include all country domains": OFF.** Countries listed: 14.
**Total visits:** not shown. India country rank #95,988.

> ## ⚠️ DO NOT USE THIS DATA WITHOUT RE-PULLING FIRST
>
> This pull is almost certainly the wrong property, and the numbers behave like noise.
> See the analyst notes below. `/research` must not build a country profile, an APM gap
> analysis, or an ICP score on this table.

| # | Country | Traffic Share % | Change | Audience Share % | Country rank | Visit duration | Pages/Visit | Bounce |
|---|---------|-----------------|--------|------------------|--------------|----------------|-------------|--------|
| 1 | India | 59.79% | +215.64% | 57.58% | #95,988 | 00:01:03 | 1.69 | 47.50% |
| 2 | Pakistan | 19.08% | −100.00% | 25.46% | — | — | 1.00 | 98.21% |
| 3 | United States | 8.73% | +60.47% | 6.81% | #2,206,425 | 00:00:16 | 1.25 | 59.79% |
| 4 | Canada | 4.29% | −27.00% | 3.67% | — | 00:00:04 | 1.19 | 66.41% |
| 5 | Ethiopia | 1.98% | −100.00% | 1.51% | — | — | 1.04 | 43.85% |
| 6 | South Africa | 1.71% | −100.00% | 1.39% | — | — | 1.93 | 2.21% |
| 7 | Indonesia | 1.38% | −100.00% | 1.02% | — | 00:00:16 | 1.50 | 35.90% |
| 8 | Nigeria | 1.04% | — | 0.87% | — | — | 1.00 | 100% |
| 9 | Australia | 0.71% | −100.00% | 0.47% | — | 00:00:14 | 1.29 | 33.78% |
| 10 | France | 0.40% | −100.00% | 0.30% | — | — | 1.00 | 50.22% |
| 11 | Kenya | 0.38% | — | 0.33% | — | — | 1.02 | 39.81% |
| 12 | Egypt | 0.26% | — | 0.39% | — | — | 1.00 | 100% |

## Analyst notes — why this is being rejected as an input

1. **Wrong domain.** The target account list gives Great Learning's website as
   `mygreatlearning.com`. This pull is `greatlearning.in`. Those are different properties,
   and the main learner-facing platform is the former.
2. **The ranks say the same thing.** India country rank #95,988 for a company that sells
   high-ticket programmes to Indian learners at scale is not plausible for a primary domain.
   The US rank of #2,206,425 is effectively no traffic at all. Compare YuppTV's India rank of
   #5,540 in the same pull format.
3. **The engagement metrics read as junk traffic, not learners.** Pakistan at 19% of traffic
   with 98.21% bounce and exactly 1.00 pages per visit. Nigeria and Egypt at 100% bounce and
   1.00 pages. South Africa at 2.21% bounce. These are bot, redirect or parked-domain
   signatures, not people evaluating a ₹1L+ programme.
4. **Seven markets show a change of exactly −100.00%.** That is a measurement artefact on a
   tiny base, not seven simultaneous collapses.
5. **The 60% threshold is at stake.** India reads 59.79%, which would award the "high traffic
   outside home market" ICP signal by two-hundredths of a percent — on data this unreliable,
   on the wrong domain. That single point of noise would move the account's tier.

## What to re-pull
- `mygreatlearning.com` as the primary domain
- **"Include all country domains" toggled ON**, so any `.in` / regional properties merge in
- If both domains carry real traffic, both views are useful — the split between them is
  itself a finding about where Indian versus international learners transact
