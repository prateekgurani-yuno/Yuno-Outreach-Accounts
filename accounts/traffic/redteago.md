# RedteaGO — SimilarWeb traffic

**Supplied by Prateek:** 2026-10-11 (screenshot) · **Period:** Jul 2026 – Sep 2026 · **Scope:** `redteago.com` · **All traffic**
⚠️ **"Include all country domains" toggle is OFF** — regional variants, if any exist, are excluded.
**Countries in dataset:** 34 · **Total visits: NOT shown** — shares only.

| # | Country | Traffic share | Change | Audience share | Country rank | Visit duration | Pages/visit | Bounce rate |
|---|---------|---------------|--------|----------------|--------------|----------------|-------------|-------------|
| 1 | 🇨🇳 **China** | **74.32%** | ▲ 16.03% | **75.25%** | **#11,055** | **00:06** | **1.53** | **81.59%** |
| 2 | 🇺🇸 United States | 6.30% | ▲ 17.38% | 6.75% | #293,759 | **05:08** | **5.82** | 36.08% |
| 3 | 🇦🇺 **Australia** | 2.17% | ▼ 26.56% | 2.06% | #192,046 | 01:23 | 1.95 | 31.83% |
| 4 | 🇩🇪 Germany | 1.89% | ▲ 36.68% | 1.89% | #123,842 | **10:16** | **5.57** | 46.88% |
| 5 | 🇮🇳 **India** | 1.78% | ▲ **474.90%** | 1.15% | #164,636 | 01:24 | 4.83 | **11.92%** |
| 6 | 🇭🇰 **Hong Kong** (home) | 1.68% | ▲ 30.91% | 2.00% | **#31,529** | 03:04 | 4.69 | 25.32% |
| 7 | 🇨🇦 Canada | 1.56% | ▲ 38.25% | 1.49% | #364,761 | 00:41 | 2.82 | 28.09% |

## 🛑 UPDATE 2026-10-12 — THIS TABLE MEASURES A SITE THAT SELLS NOTHING

**`redteago.com` is a WordPress marketing site. The shop is `esim.redteago.com`, and it is not in this dataset.** Verified first-hand:

| | `redteago.com` (measured) | `esim.redteago.com` (the shop) |
|---|---|---|
| `wp-content` hits | **149** | — |
| `stripe` · `checkout` · `cart` · `buy now` | **0 · 0 · 0 · 0** | stripe ✅ · paypal ✅ · checkout ✅ |
| `supportCurrency` | 0 | ✅ present |

🔑 **So every share in the table below describes brochure traffic, not buyers.** Same failure mode as the SpinX pull in the October batch. **Re-pull SimilarWeb on `esim.redteago.com`** — it is the single highest-value missing input on this account.

### What this means for the 6-second China row

The research run proposed a clean mechanical cause: a forced locale redirect. **It is real but it does not apply here.** `esim.redteago.com` does return **`302 → /zh-CN`** to a `zh-CN` browser while serving `200` to English. **But the measured property does not redirect at all** — I tested both: `redteago.com` returns **`200` to English and `200` to Chinese, with no `Location` header**.

**The explanation that does survive is the app hand-off.** `redteago.com` carries an `apple-itunes-app` Smart App Banner plus App Store and Play links, and sells nothing. Land, tap into an app store, session over. **That produces ~1.5 pages and a 6-second visit exactly as observed.**

⚠️ **Still not excluded:** crawler traffic, and a mainland block or interstitial — this session is not on a Chinese IP, so neither can be tested from here.

---

## 🛑 The China row does not behave like the others. Read this before using it.

**China is 74.32% of traffic on a 6-second visit, 1.53 pages and an 81.59% bounce rate.**
Set that against the markets below it:

| | China | United States | Germany | Hong Kong | India |
|---|---|---|---|---|---|
| Visit duration | **00:06** | 05:08 | **10:16** | 03:04 | 01:24 |
| Pages / visit | **1.53** | 5.82 | 5.57 | 4.69 | 4.83 |
| Bounce rate | **81.59%** | 36.08% | 46.88% | 25.32% | **11.92%** |

**Six seconds and one and a half pages is not someone buying a data plan.** Every other market in
the table shows genuine shopping behaviour — the US at five minutes and nearly six pages, Germany
at over ten minutes, India bouncing at just 11.92%.

⚠️ **Do NOT treat 74.32% as the commercial centre of this business without establishing what it
is.** Candidate explanations, none of them verified: crawler and bot traffic; an app-download
redirect where the real session continues in the app; a domain-level block or interstitial inside
mainland China; or genuine but very shallow interest. **These are four very different accounts.**
🔑 **This is the single most important thing to resolve before sizing RedteaGO.**

**Note the country-rank column cuts the other way:** China sits at **#11,055** and Hong Kong at
**#31,529**, both far stronger than the US at #293,759 — so the Chinese audience is real in volume
even if the sessions are shallow.

## APAC arithmetic

| | |
|---|---|
| 🇨🇳 China | **74.32%** ⚠️ *engagement-suspect* |
| 🇦🇺 Australia | 2.17% |
| 🇮🇳 India | 1.78% |
| 🇭🇰 Hong Kong (home) | 1.68% |
| **APAC visible total** | **79.95%** |
| **APAC excluding the China row** | **5.63%** |

🔑 **The two readings are radically different.** Taken at face value this is an overwhelmingly
Chinese business and the **"high traffic outside home" ICP row depends entirely on whether China
counts** — Hong Kong, the registered home market, is only 1.68%, so on a literal reading the row
is comfortably met. **But if the China traffic is not transacting, the real commercial mix is US,
Germany, Australia, India, Hong Kong and Canada — a dispersed, genuinely international book.**

🚩 **India is up 474.90% with the lowest bounce rate in the table (11.92%) and 4.83 pages per
visit.** Small at 1.78%, but that is the strongest engagement signal here and it is growing
fastest. Worth watching regardless of what China turns out to be.

🚩 **Australia is the only market shrinking** (▼26.56%).

---

⚠️ **Territory note.** APAC here is CLAUDE.md's definition: everything east of Dubai. Germany,
the US and Canada are excluded from the totals above. **Hong Kong is the registered home market**
per the target account list, which makes this comfortably in territory regardless of how the
China row resolves.

⚠️ **The country-domains toggle is OFF**, so any regional variant is excluded and the split may be
incomplete. **Identify whether RedteaGO runs country domains or an app-first funnel before relying
on this table.**

*Transcribed from the supplied screenshot. Not re-researched. Figures not independently verified
against SimilarWeb.*
