# Sogni AI

**Status:** 🔴 Not ICP — **under 40,000 monthly transactions (volume gate)**
**ICP Score:** Not scored — the volume gate fires regardless of every other signal
**Industry:** Creative AI — image, video, music and language generation on a decentralized GPU network ("Supernet") · **HQ:** **we&robot PTE LTD**, 60 Paya Lebar Road, Paya Lebar Square #07-54, **Singapore 409051** · **Researched:** 2026-10-07 · **First email sent:** —
**Motion:** N/A — rejected before outreach
**⏰ REVISIT: Q2 2027.** See the rejection rationale — this is a timing call, not a quality call.

---

## Rejection Rationale

**Derived monthly transaction count is ~8,500–15,600 against a 40,000/month gate.** The derivation rests on **two SOURCED inputs** and is a hard *ceiling*, not an estimate — so per the ICP rules it legitimately fires the gate.

```
Oct 2026 net subscription revenue   $136,797.21   SOURCED — Sogni's own public API, verified first-hand
Cheapest monthly plan                    $20.00   SOURCED — sogni.ai/pricing, verified first-hand
                                     ----------
MAX possible subscription charges         6,840 / month
  grossed up ~12% (revenue is already net of fees/taxes)
                                        ~ 7,661 / month
Spark top-ups: $597,772 lifetime card-paid ÷ ~15 months = ~$39,851/month
  at ASSUMED $50 avg top-up →   797 / month
  at ASSUMED $15 avg top-up → 2,657 / month
  at ASSUMED  $5 avg top-up → 7,970 / month
                                     ----------
TOTAL                            ~8,458 – 15,631 / month   vs gate of 40,000
```

**Why this is a sound derivation and not an assumption:** dividing revenue by the *cheapest* plan gives the **maximum possible** number of subscription charges. Every subscriber on Unlimited Pro ($50/mo), or on any annual plan (one charge covering twelve months of recognised revenue), pushes the real count **lower**. The only assumed input is average Spark top-up size, and **even the most generous assumption ($5) leaves the total at ~16k — under half the gate.**

⚠️ **One unresolved conflict, which does not change the verdict.** A second method — lifetime billing events ÷ elapsed months — gives a different answer: 21,170 signups + 37,827 renewals = 58,997 events ÷ ~3.2 months ≈ **18,400/month**. That is 2.7× Method A and I cannot reconcile them. Candidate explanations: `subscriptionRenewal` may count period rollovers rather than captures (crypto plans "never auto-renew" yet still roll); regional App Store prices may sit below $20; `subscriptionSignup` may predate the paid launch. **Both methods land below 40,000, so the conclusion is robust to the conflict.**

### ⏰ Why this is a REVISIT, not a kill

**The paid business is three months old and grew 9.2× in a single month.** Their own API, verified:

| Month | Net subscription revenue | Status |
|---|---|---|
| 2026-07 | **$521.51** | `finalized: true` |
| 2026-08 | **$13,860.23** | estimated |
| 2026-09 | **$126,859.66** | estimated — **9.2× MoM** |
| 2026-10 | **$136,797.21** | estimated, 7 days elapsed |
| 2026-11 | $9,161.50 | forward-booked |

**MRR ≈ $137k → ~$1.64M ARR run-rate, from a standing start in July 2026.** At even a fraction of that trajectory they cross 40,000 transactions/month within **2–4 quarters**. Traffic agrees: sixteen of seventeen visible markets are growing, most triple-digit.

**Recommended action: dated nurture, revisit Q2 2027.** Re-run the same two API endpoints then — they are public and unauthenticated, so re-qualifying costs one minute.

---

## ⭐ Why this account is worth keeping warm — the research is the value

### 1. They publish their own payment telemetry, unauthenticated

**This is the most unusual finding in the repo.** `sogni.ai/leaderboard` and `/capacity` call public endpoints that expose production billing data. I verified both first-hand on 2026-10-07:

- **`https://api.sogni.ai/v1/analytics/lifetime`** — HTTP 200, 12,758 bytes. Called with **no `keys` parameter it returns all 350 counters**; their own leaderboard requests only three.
- **`https://api.sogni.ai/v1/leaderboard/subscription-workers?month=YYYY-MM`** — HTTP 200, returns `totalNetSubscriptionRevenueUsd`, `workerSharePct: 51`, `finalized`, `revenueBasis`.

**Anyone can read their MRR, churn and dunning performance. No login. That is worth knowing on its own, and it makes re-qualification trivial.**

### 2. Their own numbers show a measurable dunning problem

Verified from the lifetime feed:

| Counter | Value |
|---|---|
| `subscriptionSignup` | **21,170** |
| `subscriptionRenewal` | **37,827** |
| `subscriptionTrialStart` | 15,972 |
| `subscriptionCancellation` | **17,335** |
| **`subscriptionPastDue`** | **2,204** |
| **`subscriptionRecovered`** | **643** |
| `subscriptionChargeback` | 31 |
| `subscriptionRefund` | 162 |

- **Dunning recovery is 643 / 2,204 = 29%.** Roughly **1,561 subscriptions lost to failed payments** out of 21,170 signups — **7.4% leakage.** `[DERIVED]`
- **Chargeback rate 31 / 58,997 = 0.05%** — low. Where the card rail works, it works well.
- Net active subscriptions ≈ 21,170 − 17,335 = **~3,835**, implying **ARPU ≈ $35.66/month** against a $20 entry price. `[DERIVED, crude — cancellation timing lags]`

**A 29% recovery rate is the single best hook for the revisit conversation, and it is their own number.**

### 3. The $498 authorization hold on a free trial

From their pricing page, verbatim: *"Web/Stripe trials require your authorization for a **temporary card hold equal to the selected plan's payment amount, including the full annual amount for annual billing**."* Confirmed in the checkout code:

```js
const f = n==="annual" ? t.annualPriceFormatted : t.monthlyPriceFormatted;
["I authorize the temporary ", f, " card hold and understand that Sogni will not collect it."]
```

| Plan | Cadence | Auth hold on a **3-day free trial** |
|---|---|---|
| Unlimited | Monthly | $20 |
| Unlimited | Annual | **$199** |
| Unlimited Pro | Monthly | $50 |
| Unlimited Pro | Annual | **$498** |

**And a decline kills the trial outright.** From `docs.sogni.ai/pricing/cancellation-and-refund-policy/`, verified verbatim:

> *"**If the issuer declines the authorization, the trial may be ended automatically** before any subscription payment is taken. Trial eligibility remains available so the customer can **retry with another eligible card**."*

**No retry cascade, no fallback rail, no step-down to a smaller hold, no local method. The entire documented remedy is "try another card."**

⚠️ **Their two properties disagree on this.** `docs.sogni.ai` (policy v2026-09-18) says a hold *"for **up to** the first subscription payment"* and that *"Sogni **releases the authorization immediately** without capturing the funds."* The marketing page says the full amount. **Both are live. Quote the docs version to be safe.** The policy has been rewritten **four times in about two months** (2026-08-05 → superseded 2026-08-26 → header 2026-09-18 → footer claiming 2026-10-06, contradicting its own header) — **billing terms churning that fast means the billing stack is being actively reworked.**

### 4. They built the hard half of orchestration and skipped the half that recovers revenue

Provider enum, verbatim from `dashboard.sogni.ai/assets/main-BH-30axC.js` (2,828,912 bytes):

```js
{stripe:"Stripe", apple:"App Store", google:"Google Play", manual:"Sogni", crypto:"Crypto (USDC)"}
```

Rail-specific ingress collapsing into a rail-agnostic surface — verified in the bundle:
```
/v1/iap/stripe/{subscribe,purchase,products,auto-top-up}   /v1/iap/google/{products,validate}
/v1/crypto-pay/intent                                       /v1/crypto-pay/intent/active
/v1/subscriptions/{status,plans,billing,change-plan,cancel,activate-paid,trial-eligibility,usage}
/v1/subscriptions/worker/{payout-wallet,earnings,earnings/participation}
```

Plus their own Spark ledger reconciling card, store and chain funding into one currency, and hand-built dunning UI (*"Auto top-up paused"*, *"Stripe could not accept the last automatic charge"*, error codes `ENROLMENT_PENDING:191`, `CARD_REQUIRED:192`).

**Classification: in-house reconciliation and entitlement layer — NOT a routing layer.** No second acquirer, no retry cascade, no failover, no BIN or geo routing anywhere. `app-main.js` has 61 `stripe` hits and **zero** hits for any other card acquirer. **No orchestrator incumbent to displace.** They proved the appetite and the engineering; what's missing is exactly the revenue-recovery half.

### 5. USD-only, zero local rails, across 29% APAC traffic

**Currency census, verified in `dash.js`: `"USD"` 4, `"usd"` 7 — and ZERO INR, IDR, EUR, GBP, AUD, PHP, VND, THB, MYR, BRL, EGP.** Formatters hardcoded `en-US`. No currency switcher, no geo-pricing.

Their own FAQ: *"Apple and Google show **localized** subscription prices that may differ from the **advertised US $20/month web price**."* — **the app stores localize price; their own web checkout does not.** And the two are walled off: *"Website checkout cannot spend Play credits, even if Google Pay is available."*

**Across eight APAC markets making up 29.10% of traffic — India, Indonesia, Malaysia, Philippines, Vietnam, Thailand, Australia, Pakistan — the local-rail count is ZERO.** Basis: three large fetched pages plus the complete **210-URL `docs.sogni.ai` sitemap**, whose entire `/pricing/` branch is `apple-subscription-refunds`, `cancel-unlimited-subscription`, `cancellation-and-refund-policy`, `fair-use-queue`, `google-play-subscriptions`, `pay-with-crypto`, `unlimited-plan-details`. **Four rails, no fifth.**

### 6. India is a toggle they have not flipped — resolved definitively

India is **15.32% of traffic, their #2 market, highest audience share in the table at 19.99%**. No UPI, no UPI Autopay, no netbanking, no RuPay, no EMI, no INR price.

**I fetched Stripe's own docs (`docs.stripe.com/payments/upi.md`, HTTP 200) to settle whether they even could:**
- *"UPI supports both one-time payments and **recurring payments through e-mandates (also known as UPI AutoPay)**."*
- Presentment currency **INR**; **Recurring payments: Yes**; available to **Subscriptions**, Invoicing and Payment Links.
- *"Recurring payments are limited to a maximum of **15,000 INR**."* — a $20/mo ticket (~₹1,780) sits comfortably inside.
- **Business locations: both `SG` and `US` are on Stripe's eligible list.** ✅

**So whichever way their Stripe account is domiciled, UPI with AutoPay is available to them and is a Dashboard toggle. This is a pure execution gap, not a structural blocker.** That is a clean, evidenced observation for the revisit.

⚠️ **The RBI e-mandate specifics could NOT be sourced** — `support.stripe.com/questions/rbi-e-mandate-regulations-faqs` served a JavaScript shell. **Do not cite e-mandate rules, thresholds or deadlines from memory in any future outreach.** Pull a current primary source first.

### 7. The 51% formula — payment costs are indexed to supply-side payouts

From their July 2026 launch release: *"participating GPU operators accrue **51% of net subscription revenue — calculated after payment fees, taxes and refunds**."* **Confirmed in their own API: `workerSharePct: 51`.** October's operator pool is **$69,766.58**.

**Every basis point of MDR, every failed retry and every refund directly reduces what GPU operators earn**, which affects supply-side retention on the network they depend on. That turns cost-of-payments into a supply-network argument. **It is also a growing monthly cross-border mass-payout obligation in USD — a second payments problem alongside inbound acceptance.**

---

## Company facts for the revisit

**Entity:** **we&robot PTE LTD**, Singapore 409051 — first-hand from `sogni.ai/terms` (which serves the privacy policy; `/privacy` 404s). Data-protection contact **Cecilia Tan**. ⚠️ **ACRA/BizFile UEN not found.**

**Founders:** **Mauvis Ledford** (Co-founder & CEO, ex-CTO of CoinMarketCap), **Mark Ledford** (Co-founder & CTO, his brother, ex-CIO of CoinMarketCap), **Alejandro Ramos** (Co-founder & CPO). CEO is Singapore-resident. Conceived 2022; mainnet live **2 July 2025**; ~10–14 staff.

**✅ Territory: in APAC.** Singapore-incorporated, Singapore-registered, CEO resident in Singapore, SEA accelerator (Fortify Labs, run by TZ APAC), NTU Singapore workshops. ⚠️ Founders are US-origin and the team is distributed — if challenged, the defensible line is the entity and the CEO's residence.

**Funding — sources conflict, report both:**
- CEO interview: **$2M pre-seed Jan 2025**, then **$1.5M seed led by the Tezos Foundation**, *"total funding $3.5 million."*
- Crypto wire release: **$2M–$2.14M announced 11 Mar 2025**, co-led by **Comma3 Ventures** and **Republic Ventures**, with Nosana, Contango Digital, Oyster, ARC, DEXT Force, Formless, Gecko.
- ⚠️ A **$25M pre-seed valuation** appears on **one promotional page only — do not use it.**

**Scale (lifetime, verified from their API 2026-10-07):** 306,659 registered accounts · **172,813,492 completed render jobs** · 1,215 unique GPU worker addresses · 25.3M projects · 23.8M video seconds · **140,514 banned accounts (46% of all signups)** — so treat "306k users" as registrations, not actives. Dec 2025 → Oct 2026: users 84k → 307k (3.65×), jobs 148M → 172.8M (+17%). **Accounts are growing far faster than usage.**

**Plans:** Free $0 · **Unlimited $20/mo or $199/yr** · **Unlimited Pro $50/mo or $498/yr** · Spark packs $1.99–$105.99 (rate improves $0.0080 → $0.0053/Spark; 1 Spark ≈ $0.005 of GPU inference).

**Partner models (vendor-routed, excluded from community workers):** OpenAI **GPT Image 2** · ByteDance **Seedance 2.0 / 2.0 Fast / 2.5** · MiniMax **H3 / FastH3 Turbo**. Lifetime vendor cash cost **`vendorCostUSDArtist` = $166,211**.

**GPU supply partners:** **Nosana.network** holds 9 of the top 10 subscription-worker payout slots (and was an investor in the March 2025 round); **Akash** holds another.

**Token — strictly separate from revenue and equity:** $SOGNI, TGE July 2025, on Kraken/Gate.io/MEXC, 10B max supply, **market cap ~$1.3M–$2.7M** (aggregators disagree on circulating supply). ⚠️ **A micro-cap token. Not revenue, not funding. Never mix it with the figures above.** $SOGNI and WXTZ are **not** accepted on the stablecoin payment path — that rail is USDC/USDT only; SOGNI/WXTZ convert to Spark via a separate swap at `swap.sogni.ai`.

---

## Things a future run must NOT get wrong

- ❌ **`renderUSDCompleteArtist` = $2,491,394 is GPU-time value delivered, NOT revenue.** Do not quote it as revenue.
- ❌ **The 585,000 Etherlink transactions are blockchain transactions, NOT payment transactions.** Do not feed them into the volume gate.
- ❌ **SOGNI token market cap is not revenue and not funding.**
- ❌ **"306,649 users" is registrations.** 46% of signups are banned accounts.
- ❌ **Don't claim users are complaining.** Reddit, Trustpilot, Discord and X are genuinely empty of Sogni payment complaints — the only hits were Apple App Store reviews about app crashes, which are Apple's rail. **The pain here is documented by Sogni, not reported by users.**
- ❌ **Don't cite RBI e-mandate rules from memory.** The authoritative page was unreachable.
- ❌ **Google Play Balance is not APAC local coverage** — it is Google's storefront, priced and collected by Google, and explicitly unavailable on web checkout.
- ❌ **Don't attribute Caplight's own "$16M Series A led by BlackRock" to Sogni** — that headline belongs to Caplight.
- ⚠️ **Substring traps that fired during this research and were correctly discarded:** `upi` → **"occ*upi*es"** · `emi` → **"Pr*emi*um"** (all 18 hits) · `currenc` → **"con*currenc*y"** (all 14) · `pix` → **"Pixal3D"** and `sogni-meta-pixel.js` · `omise` → `Promise.allSettled` · `eps` → "st*eps*" · `boost` → "Monthly Boost" reward · `payu` → **`cryptoPayUrl`** · `dlocal` → `readLocalFiles` · `paddle` → a demo prompt about *"the crocodile paddles frantically"* · `coinbase` → RainbowKit wallet connector, **not Coinbase Commerce** · `thirdweb` → a Sepolia testnet RPC URL.

---

## Competitive intelligence worth keeping

- **Civitai** — a competitor Sogni names on its own `/civitai-alternative` page — **was cut off by Visa and Mastercard on 23 May 2025** over content policy and fell back to **crypto-only via NowPayments**. `[UNVERIFIED — search summary]` **For any generative-AI merchant with NSFW-capable models, single-acquirer concentration is a live, dated, category-specific threat.** Sogni runs uncensored models and already has a crypto rail.
- **Leonardo.AI** (also named on `/leonardo-ai-alternative`, acquired by Canva July 2024) ran **four PSPs — Braintree, PayPal, Stripe and Paddle** — and hired a dedicated **"Technical Project Manager – Payments Platform and Billing"** to coordinate them. **Sogni runs four billing channels with no payments hire at all.**
- **No AI image/video platform was found using any payment orchestrator.** The category is unclaimed.
- **No competitor serves UPI either.** Runway, Kling and Midjourney are all card-only in India; Civitai is crypto-only. Canva (Leonardo's parent) does take UPI but has not extended it to Leonardo. **India is open ground in this category, not a race Sogni is losing.**

---

## Research Confidence

**HIGH — unusually so.** This account had better primary evidence than almost anything in the repo, because the merchant publishes its own telemetry.

- ✅ **Verified first-hand by me:** `api.sogni.ai/v1/analytics/lifetime` (HTTP 200, 350 counters) · the full `subscription-workers` monthly revenue series with `workerSharePct: 51` · the provider enum in `dashboard.sogni.ai/assets/main-BH-30axC.js` (2.83 MB) · the USD-only currency census · the decline-ends-trial and failure-to-deliver-Spark quotes in the refund policy · the trial-hold wording on the pricing page and its contradiction with the docs · plan tiers and the $41-vs-$50 correction · `docs.stripe.com/payments/upi.md` confirming SG and US eligibility and the 15,000 INR recurring cap.
- ⚠️ **Could not verify:** ACRA UEN · which funding account is correct · the 2.7× conflict between the two transaction-count methods · Spark top-up *count* (not exposed in any of the 350 counters) · whether October's $136,797 is actual or projected (`finalized: false`, 7 days elapsed) · payment-method split by rail (no per-rail counters exist) · the live authenticated checkout from a non-US IP · Apple IAP implementation (lives in the native app, not decompiled) · RBI e-mandate specifics.

*Marked not-ICP: 2026-10-07 — volume gate, ~8.5k–15.6k vs 40k. **Revisit Q2 2027** by re-reading the two public API endpoints above.*
