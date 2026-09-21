# Shaadi.com — SimilarWeb traffic

**Supplied by Prateek:** 2026-09-21 · **Scope:** `shaadi.com` with **"Include all country domains"** ON
**Countries in dataset:** 69 · **Total visits figure:** NOT shown in the supplied view — shares only.

| # | Country | Traffic share | Change | Audience share | Country rank | Visit duration | Pages/visit | Bounce |
|---|---------|---------------|--------|----------------|--------------|----------------|-------------|--------|
| 1 | 🇮🇳 India | **73.04%** | ▲ 3.13% | 79.54% | #692 | 04:53 | 9.45 | 39.42% |
| 2 | 🇺🇸 United States | **15.04%** | ▲ 5.71% | 8.06% | #6,447 | 06:56 | 11.04 | 20.09% |
| 3 | 🇨🇦 Canada | **3.83%** | ▲ **77.59%** | 3.01% | #2,299 | 06:52 | 14.25 | 19.77% |
| 4 | 🇬🇧 United Kingdom | 1.72% | ▼ 22.69% | 1.96% | #9,568 | 05:15 | 6.91 | 34.17% |
| 5 | 🇦🇪 UAE | 1.50% | ▼ 34.04% | 1.48% | #2,220 | 03:50 | 5.88 | 42.19% |
| 6 | 🇦🇺 Australia | 1.03% | ▼ 24.91% | 0.71% | #7,477 | 06:28 | 10.83 | 34.50% |
| 7 | 🇸🇦 Saudi Arabia | 0.63% | ▲ **73.53%** | 0.90% | #2,428 | 03:16 | 12.61 | 62.81% |
| 8 | 🇩🇪 Germany | 0.53% | ▼ 0.45% | 0.61% | #25,499 | 05:13 | 8.66 | 23.30% |
| 9 | 🇶🇦 Qatar | 0.39% | ▲ **106.06%** | 0.23% | #203 | 13:54 | 34.42 | 16.70% |
| 10 | 🇫🇮 Finland | 0.35% | ▼ 0.08% | 0.08% | #4,232 | 21:03 | 20.67 | 3.71% |
| 11 | 🇳🇿 New Zealand | 0.32% | ▲ 31.98% | 0.39% | #3,925 | 02:19 | 6.28 | 36.67% |

## Analyst notes

- **Home market is 73.04%** — above the 60% threshold, so the ICP "high traffic outside home" row scores **0**.
- **The non-home 27% is a diaspora corridor, not a market portfolio.** US + Canada + UK + Australia + NZ = **21.94%**; Gulf (UAE + Saudi + Qatar) = **2.52%**. This is the outbound-cross-border pattern described in `apac-payments.md` §3.
- **Canada is the growth story** — ▲77.59%, on the highest pages/visit of the top five (14.25).
- **Gulf is split in direction:** Saudi ▲73.53% and Qatar ▲106.06% against UAE ▼34.04%.
- ⚠️ **Territory note:** UAE, Saudi and Qatar are EMEA territory. Shaadi is India-HQ'd so the *account* is in APAC scope per `CLAUDE.md`; the Gulf traffic is evidence of corridor breadth, not an EMEA claim.
- ⚠️ **No absolute visit count was supplied**, so monthly transactions cannot be derived from traffic. Any volume figure must come from revenue ÷ ATV instead, and be labelled accordingly.
- Qatar's 34.42 pages/visit and 13:54 duration, and Finland's 21:03 / 20.67, are extreme outliers on tiny shares — small-sample artefacts, not signals. Do not build anything on them.

## Domain resolution (checked by me, 2026-09-21)

The SimilarWeb view aggregated "all country domains" — so I resolved what that set actually contains.
**There are no meaningful regional ccTLD properties. `shaadi.com` is effectively the whole estate.**

| Domain | Result |
|---|---|
| `shaadi.com` | ✅ **200** — the live property |
| `shaadi.com.au` | 200 but a near-empty placeholder page, not a Shaadi storefront |
| `shaadi.ae` | 200, empty — not a Shaadi storefront |
| `shaadi.us` | 200, empty — not a Shaadi storefront |
| `shaadi.ca` | ❌ Parked at a **domain auction** (whc.ca) — not owned by Shaadi |
| `shaadi.co.uk` · `shaadi.in` · `shaadi.sg` · `us.shaadi.com` · `uk.shaadi.com` | ❌ Do not resolve |

**Consequence:** the diaspora markets are served from the single `.com` property, not from local storefronts.
That matters — it means US, Canadian, British, Australian and Gulf members are transacting against whatever
entity and acquirer sit behind `shaadi.com`, which is the central question of this research.

**Sibling group properties** found on the homepage (separate estates, payment stack unknown):
`sangam.com` · `shaadilive.com` · `astrochat.com` · `jainshaadi.in` · `muslimshaadi.in` · `marwarishaadi.in`
· `buddhistshaadi.in` · `shaadicentre.in` · corporate: `people-group.com`, `careers.peopleinteractive.in`.
