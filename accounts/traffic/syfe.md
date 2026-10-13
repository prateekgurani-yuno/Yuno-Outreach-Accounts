# Syfe — SimilarWeb traffic

**Source:** SimilarWeb, supplied by Prateek 2026-10-13 (screenshot).
**Period:** Jul 2026 – Sep 2026 · All traffic · "Include all country domains" ON
**Domains:** `syfe.com` — **single domain, no "+N domains" shown** · **Countries: 48**

| # | Country | Share | Change | Audience | Rank | Duration | Pages | Bounce |
|---|---------|-------|--------|----------|------|----------|-------|--------|
| 1 | **Singapore** | **53.37%** | **↑86.93%** | 56.65% | #3,055 | 00:01:21 | 2.85 | 66.32% |
| 2 | Hong Kong | 6.96% | ↓25.88% | 8.45% | #18,005 | 00:01:03 | 2.31 | 31.90% |
| 3 | United States | 4.94% | ↑14.06% | 4.36% | #598,064 | 00:02:23 | 2.88 | 54.82% |
| 4 | Australia | 2.79% | ↑20.44% | 2.48% | #147,844 | 00:00:18 | 1.55 | 37.02% |
| 5 | India | 2.67% | ↓2.90% | 2.62% | #287,673 | 00:00:21 | 1.63 | 54.17% |
| 6 | Canada | 2.42% | ↑28.47% | 2.09% | #196,806 | 00:00:32 | 1.48 | 42.51% |
| 7 | Malaysia | 1.67% | ↓45.34% | 1.45% | #58,960 | 00:01:49 | 2.47 | 43.71% |
| 8 | Republic of Korea | 1.57% | ↑53.96% | 1.40% | #138,936 | **00:00:08** | 1.30 | 32.50% |
| 9 | Indonesia | 1.55% | ↑19.80% | 1.42% | #152,738 | 00:00:28 | 1.73 | 33.32% |
| 10 | Taiwan | 1.52% | ↑73.38% | 1.33% | #64,090 | 00:00:32 | 1.58 | 46.72% |

---

## ⚠️ Analyst notes

**1. Singapore 53.37% — below 60%, so the *"high traffic outside home"* row fires**, but only
just, and it is **rising fast (↑86.93%)**. If that trend continued the row would stop firing.
Note the direction in the report.

**2. 🛑 READ THE STASHAWAY FILE FIRST. This is the same segment, and the prior is strong.**
`2-ready-to-outreach/stashaway.md` (researched 2026-10-13) found StashAway accepts **no cards in
any market**, funds entirely by bank rail, and was **overridden DOWN to 🔴 Low**. That run also
established — from Syfe's own published material — that **Syfe funds identically: eGIRO, PayNow,
FAST and wire, with no cards and no orchestrator.** Prateek has asked for the full method anyway,
so **run it properly and try hard to falsify that prior** rather than confirm it. **Finding cards
in any Syfe flow would overturn a segment-wide conclusion and is the single most valuable
possible outcome of this run.**

**3. ⚠️ Engagement is LOW, exactly as expected for a wealth manager** — Singapore 00:01:21 /
2.85 pages / 66.32% bounce. The marketing site is a thin front door; all real activity is inside
the **logged-in app**, which SimilarWeb cannot see. **These visits are a weak proxy for deposit
volume. Do NOT derive a transaction count from them.**
**Korea at 00:00:08 / 1.30 pages** and **Australia at 00:00:18 / 1.55** are too thin to treat as
real markets despite their growth percentages.

**4. ⛔ MY ORIGINAL NOTE 4 WAS WRONG ON TWO COUNTS. CORRECTED 2026-10-13, both verified by me.**

~~Originally: "The only markets with credible depth are Singapore, Hong Kong and the US. HK is
↓25.88% and Malaysia ↓45.34% — both notable declines in markets Syfe actually operates in."~~

- ⛔ **Malaysia is NOT a Syfe market at all.** `www.syfe.com/my` and `/en-my` each return exactly
  **132,265 bytes — byte-identical to my nonsense-path control** (`/zzz-not-real-7781`). They are
  soft-404s. Syfe's own About page lists **Singapore | Hong Kong | Australia**. So the
  **↓45.34% is content traffic, not a business signal**, and must not be read as a market in
  decline. *(Note `/sg` is also a soft-404 at the same byte count — Singapore content sits at the
  root — so path probing cannot establish markets on this site.)*
- ⛔ **Australia's 2.79% / 00:00:18 / 1.55 pages is a MEASUREMENT ARTEFACT, not a thin market.**
  **`www.syfe.com/au` 301s to `https://www.selfwealth.com.au/`** (834,492 b), a **separate
  registrable domain that is absent from this single-domain dataset**. Selfwealth is Syfe's
  **second-largest client base (130,000+ AU investors, acquired May 2025)** and — critically —
  **the only part of the group with a live card flow**. The supplied table therefore
  **systematically understates Australia** and cannot see the commercially most relevant surface.

**The corrected read:** the markets with credible depth are **Singapore, Hong Kong, Australia
(via selfwealth.com.au, invisible here) and the US.**

**5. Single domain — hypothesis DISCONFIRMED (2026-10-13).** `syfe.com` is indeed one domain with
locale sub-paths, but **three entities and three regulators sit behind it**: SYFE PTE. LTD. (MAS
CMS100837), Syfe Hong Kong Limited (SFC CE BRQ741) and Syfe Australia Pty Ltd (CAR of Sanlam,
AFSL 337927). **Structurally this is the same per-market arrangement as StashAway's five ccTLDs,
just presented differently** — so the "single domain implies a single entity" reading was wrong.
And it is not even strictly single-domain: `selfwealth.com.au` is a second registrable domain
outside this dataset (see note 4).

**6. Billing unit, same as StashAway:** one **client deposit/top-up = one transaction**. The
management fee is deducted from assets, not collected over a rail. Confirm whether Syfe runs
**recurring deposits** (standing instruction / eGIRO / DDA / autopay) — that is the only
plausible high-frequency rail in this model.
