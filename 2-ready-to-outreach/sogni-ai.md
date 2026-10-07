# Sogni AI

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 13 / 29 → 🟢 **Medium** — ⚠️ **scored under an explicit volume-gate exception granted by Prateek**
**Industry:** Creative AI — image, video, music and language generation on a decentralized GPU network ("Supernet") · **HQ:** **we&robot PTE LTD**, 60 Paya Lebar Road, Paya Lebar Square #07-54, **Singapore 409051** · **Researched:** 2026-10-07 · **First email sent:** —
**Motion:** 🛑 **IN-HOUSE — but only half of one.** They built a five-rail reconciliation and entitlement layer and **no routing layer at all**. No orchestrator incumbent to displace.

---

> ## 🛑 THE VOLUME EXCEPTION — read this first
>
> **This account does not clear the 40,000/month transaction gate, and is in the pipeline because Prateek explicitly granted an exception on 2026-10-07** (*"take this company as exception in terms of txn. count"*). The arithmetic is unchanged and is recorded here so nobody mistakes the exception for a passing score.
>
> ```
> Oct 2026 net subscription revenue   $136,797.21   SOURCED — Sogni's own public API, verified first-hand
> Cheapest monthly plan                    $20.00   SOURCED — sogni.ai/pricing, verified first-hand
>                                      ----------
> MAX possible subscription charges         6,840 / month
>   grossed up ~12% (revenue is already net of fees/taxes)      ~ 7,661 / month
> Spark top-ups: $597,772 lifetime card-paid ÷ ~15 months = ~$39,851/month
>   at ASSUMED $50 / $15 / $5 avg top-up →  797 / 2,657 / 7,970 per month
>                                      ----------
> TOTAL                            ~8,458 – 15,631 / month     vs gate of 40,000
> ```
>
> **Dividing revenue by the *cheapest* plan gives the maximum possible number of subscription charges** — every subscriber on Unlimited Pro ($50/mo) or on any annual plan pushes the real count lower. The only assumed input is average Spark top-up size, and even the most generous assumption leaves the total under half the gate.
>
> ⚠️ **A second method disagrees by 2.7× and I could not reconcile it:** 21,170 signups + 37,827 renewals = 58,997 lifetime billing events ÷ ~3.2 months ≈ **18,400/month**. Candidate causes: `subscriptionRenewal` may count period rollovers rather than captures; regional App Store prices may sit below $20; `subscriptionSignup` may predate the paid launch. **Both methods land below 40,000.**
>
> ### Why the exception is defensible on its own merits
> **The paid business is three months old and grew 9.2× in a single month.** Their own API:
>
> | Month | Net subscription revenue | Status |
> |---|---|---|
> | 2026-07 | **$521.51** | `finalized: true` |
> | 2026-08 | **$13,860.23** | estimated |
> | 2026-09 | **$126,859.66** | estimated — **9.2× MoM** |
> | 2026-10 | **$136,797.21** | estimated, 7 days elapsed |
>
> **MRR ≈ $137k → ~$1.64M ARR run-rate from a standing start in July 2026.** At even a fraction of that trajectory they cross 40,000 transactions/month within **2–4 quarters**. Sixteen of seventeen visible traffic markets are growing, most triple-digit.
>
> **🔑 Re-qualification is free and takes one minute** — both endpoints below are public and unauthenticated. Re-read them before any meeting to get a current number.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Creative AI platform — image, video, music and language generation across 200+ models — running on a decentralized GPU network ("Supernet") where community operators earn **51% of net subscription revenue**. Singapore-incorporated, ~10–14 staff, founded by two ex-CoinMarketCap executives. Monetises through **Sogni Unlimited** ($20/mo or $199/yr; Pro $50/mo or $498/yr) plus **Spark**, a prepaid credit currency, and an OpenAI-compatible developer API.

**SimilarWeb (supplied 2026-10-07, Jul–Sep 2026, country-domains toggle OFF, 82 countries):** US 27.75% ▲144.75% · **India 15.32% ▲107.81%** · Egypt 5.65% **▲1,223%** · Indonesia 3.62% · UK 3.60% · Canada 3.14% · Brazil 3.04% ▲544.66% · **Australia 2.47%** · Germany 2.34% · Italy 2.17% · **Malaysia 2.08% ▲749%** · Philippines 1.58% ▼20.24% · Iraq 1.53% ▲848% · **Vietnam 1.49%** · Mexico 1.40% · **Thailand 1.34% ▲720%** · **Pakistan 1.20%**. Full table in `accounts/traffic/sogni-ai.md`.

**🔑 APAC is 29.10% of visible traffic and exceeds the US (27.75%).** Eight of seventeen visible markets are in territory.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|---|---|---|---|---|---|
| 1 | 🇺🇸 United States | 27.75% | Card (Stripe), Apple Pay, Google Pay, USDC/USDT | **PayPal · ACH · BNPL** (Affirm/Afterpay/Klarna) | ❌ none — SG entity |
| 2 | 🇮🇳 **India** | **15.32%** | Card only (USD, cross-border) | **UPI · UPI Autopay · netbanking · RuPay · EMI · INR pricing** | ❌ none |
| 3 | 🇪🇬 **Egypt** | **5.65%** | Card only (USD, cross-border) | **Fawry · Meeza · ValU · mobile wallets · EGP pricing** ❌🔒 **Stripe offers NONE of these** | ❌ none |
| 4 | 🇮🇩 Indonesia | 3.62% | Card only (USD) | **QRIS · virtual account · GoPay/OVO/DANA · OTC cash · IDR** | ❌ none |
| 5 | 🇬🇧 United Kingdom | 3.60% | Card, Apple Pay, Google Pay | **GBP pricing · BNPL** | ❌ none |

### Legal entities
- **we&robot PTE LTD** (Singapore) — 60 Paya Lebar Road, Paya Lebar Square #07-54, Singapore 409051. ⚠️ **ACRA/BizFile UEN not found.** No US, HK or Indian entity found.

### Known PSPs
- **Stripe** — `[Source Code]` + `[Terms]`. **The only card acquirer.** Hosted Checkout redirect, Billing Portal, SetupIntent for auto-top-up
- **Apple App Store / Google Play** — platform rails, **not Sogni's**
- **Self-built crypto rail** — USDC on Base/Etherlink/Ethereum, USDT on Ethereum. **No crypto PSP** — not Coinbase Commerce, not thirdweb
- **"manual"** — a human-granted entitlement path, almost certainly the enterprise/comp route

### Orchestration status
🟡 **In-house reconciliation layer, NO routing layer.** Five rails normalised behind one provider enum and one Spark ledger, with a rail-agnostic subscription API — but **no second acquirer, no retry cascade, no failover, no BIN or geo routing anywhere.** **No orchestrator incumbent to displace.**

### Buying signals
- 🚀 **Paid subscriptions launched July 2026 and grew 9.2× in one month** — the single best timing signal
- 💼 **Billing terms rewritten four times in ~two months** — the billing stack is actively being reworked
- 📋 **Zero payments or billing hires** at ~10–14 staff, running four billing channels across two crypto flows
- 🤝 **Ambassador Program paying USDC for bringing paying subscribers** — "coming this season", per their own leaderboard
- 💰 **SOGNI buybacks funded by revenue** and a staker revenue-share "in the works" — monetisation is board-level

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Sogni AI` to draft the 12-touch sequence.*

> **Motion is IN-HOUSE — but read Section 3 before drafting.** They built a five-rail reconciliation layer and deliberately chose Stripe-hosted checkout. **Respect the build decision.** The gap is not that they lack payment engineering — it is that they built the half that reconciles and skipped the half that recovers revenue. Anchor on **routing, retries and local rails**, never on "you need orchestration."
>
> ⚠️ **Do NOT claim their users are complaining.** Reddit, Trustpilot, Discord and X are genuinely empty of Sogni payment complaints. **The pain here is documented by Sogni itself** — use their own numbers and their own policy language.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 13 / 29

| Signal | Points | Status |
|---|---|---|
| **Monthly transaction count** | **0** | 🛑 **DERIVED: ~8,458–15,631/month — BELOW the 40,000 gate.** $136,797.21 Oct net subscription revenue **[SOURCED, their own API, verified]** ÷ $20 cheapest plan **[SOURCED, verified]** = 6,840 charges/month ceiling, plus 797–7,970 Spark top-ups on an ASSUMED average size. **Does not reach even the 40,000–49,999 band, so it scores 0.** **The gate is waived by Prateek's explicit exception, not met.** |
| Orchestration status | **1** | 🟡 **In-house layer.** Five rails normalised (`{stripe, apple, google, manual, crypto}`), rail-agnostic `/v1/subscriptions/*`, own Spark ledger, own dunning UI and error taxonomy. ⚠️ **But it is reconciliation and entitlement, NOT routing** — no second acquirer, no retry cascade, no failover. **That makes it a far easier in-house sell than most**, but the row still scores 1 |
| 3+ countries | **3** | ✅ 82 countries in the traffic data; sells globally from one Singapore entity |
| Multiple PSPs | **0** | ⬜ **Deliberate zero — and it is the pitch.** There is exactly **ONE card acquirer (Stripe)**. Apple and Google are platform rails they neither control nor price; the crypto rail is self-built. `app-main.js` has 61 `stripe` hits and **zero** for any other acquirer. **Single-acquirer concentration is the argument, not a scoring row** |
| Local rail or licensing gap in a top-3 market | **3** | ✅ **India (#2, 15.32%): zero UPI, UPI Autopay, netbanking, RuPay, EMI or INR pricing. Egypt (#3, 5.65%): zero local methods — and Stripe's catalog contains NONE for Egypt at any currency** (grepped `fawry\|meeza\|zaincash\|qi card\|egypt\|iraq` → 0 matches) |
| Recent expansion | **2** | ✅ **Sogni Intelligence** (OpenAI-compatible API) introduced March 2026 · **Unlimited launched July 2026** · Windows and Android worker support shipped · video generation live (23.8M seconds) |
| Payment issues reported | **2** | ✅ **From their own API: 2,204 past-due vs 643 recovered = 29% dunning recovery, ~1,561 subscriptions lost to failed payments (7.4% leakage).** Plus their own policy: an issuer decline on the trial hold *"may end the trial automatically"* |
| Funding >$10M | **0** | ⬜ **~$3.5M total** across a pre-seed and a Tezos-Foundation-led seed. Well below the threshold |
| High traffic outside home | **2** | ✅ **Singapore does not appear in the top 17 markets at all.** US 27.75%, India 15.32% — home-market share is effectively nil |
| Competitor using orchestration | **0** | ⬜ **No AI image/video platform found using any orchestrator.** The category is genuinely unclaimed |
| Payment job postings | **0** | ⬜ **None found — no careers page, no LinkedIn postings, no payments role of any kind** at ~10–14 staff |

**Tier:** 🟢 **Medium (10–16)**

### 🛑 Analyst note on the score
**13/29 is an honest reflection of a small, young, single-acquirer business — and it understates the opportunity.** Three of the four zeros are *the argument rather than its absence*: a single PSP, no competitor on orchestration, and no payments hire all describe a company that has outgrown its payment setup and has nobody internally to fix it. **The matrix has no row for "grew 9.2× in a month" or "publishes its own dunning failure rate."**

**Equally, the exception must not be forgotten.** At ~8.5k–15.6k transactions/month this is roughly a third of the minimum. **If the volume exception is ever withdrawn, this account rejects immediately.** Re-read the two public endpoints before any meeting.

### Source Notes
- ✅ **Verified first-hand by me:** `api.sogni.ai/v1/analytics/lifetime` (HTTP 200, **350 counters**, returns everything when called with no `keys` parameter) · the full `subscription-workers` monthly revenue series with `workerSharePct: 51` · `api.sogni.ai/v1/iap/stripe/products` (**7 live Stripe Price objects, all `usd`, all `tax_behavior: unspecified`, all `livemode: true`**) · the provider enum in `dashboard.sogni.ai/assets/main-BH-30axC.js` (2.83 MB) · the USD-only currency census · the decline-ends-trial and failure-to-deliver-Spark quotes · the trial-hold wording and its contradiction between properties · `docs.stripe.com/payments/upi.md` confirming SG **and** US eligibility and the 15,000 INR recurring cap
- ⚠️ **Could not verify:** ACRA UEN · which funding account is correct · the 2.7× conflict between the two transaction-count methods · Spark top-up *count* (not exposed in any of the 350 counters) · whether Oct's $136,797 is actual or projected (`finalized: false`) · payment-method split by rail · the live authenticated checkout from a non-US IP · Apple IAP implementation · **RBI e-mandate specifics — the authoritative page served a JS shell, so do not cite e-mandate rules from memory**

### Success Case Alternatives
- **A consumer subscription business that added local rails and recovered involuntary churn** — closest profile match. ⚠️ **Only cite a Yuno customer with a published metric** (standing rule).
- ❌ **Do NOT cite competitor case studies here** — no AI image/video platform uses an orchestrator, so there is no category proof point to point at.

---

## The findings

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

### 5. Their live Stripe catalog is public too — USD-only, tax disabled

**A second unauthenticated endpoint exposes their real Stripe Price objects.** `https://api.sogni.ai/v1/iap/stripe/products` — HTTP 200, 3,667 bytes, verified first-hand:

| nickname | currency | amount | type | tax_behavior | livemode |
|---|---|---|---|---|---|
| Premium Spark Points • 20K | **usd** | 10599 | one_time | **unspecified** | true |
| Premium Spark Points • 10K | **usd** | 5599 | one_time | **unspecified** | true |
| Premium Spark Points • 4.5K | **usd** | 2699 | one_time | **unspecified** | true |
| Premium Spark Points • 2K | **usd** | 1299 | one_time | **unspecified** | true |
| Premium Spark Points • 1K | **usd** | 699 | one_time | **unspecified** | true |
| Premium Spark Points • 550 | **usd** | 399 | one_time | **unspecified** | true |
| Premium Spark Points • 250 | **usd** | 199 | one_time | **unspecified** | true |

**Distinct currencies across all 7 live prices: `{usd}`. Distinct `tax_behavior`: `{unspecified}`. `currency_options` absent.**

In Stripe a price must be `inclusive` or `exclusive` for Stripe Tax to compute on it — **`unspecified` is incompatible with Stripe Tax calculating on these prices.** ⚠️ Caveat: `automatic_tax` is set at the Checkout Session level, which needs authentication to inspect, so this is strong evidence but not categorical. Likewise `currency_options` is only returned when explicitly expanded, so its absence is suggestive, not conclusive.

**🔑 And their own docs contradict this.** Verbatim from `docs.sogni.ai/pricing/unlimited-plan-details/`:
> *"Stripe (web checkout): The prices above are the Stripe list prices billed in USD. **Taxes and local currency conversion are applied by Stripe at checkout according to your billing address.**"*

**That does not survive contact with the catalog** — USD-only prices, tax not configured, and a client renderer hardcoded to USD:
```js
c = e => Number(e||0).toLocaleString("en-US",{style:"currency",currency:"USD",minimumFractionDigits:2})
```
**This reads as an assumption that Stripe localizes by default. It does not.** The adjacent sentence shows they know the difference — *"Subscription plans purchased through the App Store or Play Store are **priced by the platform in local currency**."* Localization exists only on Apple's and Google's rails.

⚠️ **Note:** the 7 public prices are the one-time Spark packs only. **The subscription prices ($20/$199/$50/$498) are NOT in this endpoint** — those are confirmed from page copy and the hardcoded USD formatter, not from a price object.

### 5b. 🔑 Even the FREE tier is card-gated

> *"Collecting and spending free Spark **requires a verified payment method** on accounts created in the Sogni web app."*
> *"**Until a valid card is on file, free generations and free reward claims are paused.**"*
> *"Free monthly Spark 400 — **Needs a verified payment method**."*

Their stated reason: *"free Spark was being farmed at scale by throwaway accounts… while we fight bots and fraudulent signups"* — consistent with **140,514 banned accounts, 46% of all signups.**

**Carve-out:** *"Premium Spark, SOGNI token, and Unlimited rendering are never gated by this"* — **so a crypto purchase bypasses the card gate entirely. Crypto is the only no-card path into the product.**

**This moves the payment problem from conversion to acquisition.** A user in Cairo or Jakarta without an international-enabled card cannot use the free tier at all — which fits the Egypt/Iraq pattern below: enormous engagement, no obvious way to pay.

### 5c. Stripe's own matrix locks them out structurally

From `docs.stripe.com/payments/payment-methods/payment-method-support`, local methods are **currency-locked and business-location-locked**:

| Method | Currency required | Stripe business location |
|---|---|---|
| Pix / Boleto | **BRL** | BR (Pix invite-only), US |
| OXXO | **MXN** | MX |
| SEPA Direct Debit · iDEAL · Bancontact | **EUR** | EU, AU, CA, HK, JP, MX, NZ, **SG**, US |
| Klarna · Affirm · Afterpay | incl. USD | **no SG** |
| PayPal | incl. USD | EU/CH/GB only — **no SG, no US** |
| ACH Direct Debit | USD | EU/UK/CH + US — **no SG** |
| Cards · Apple Pay · Google Pay · Link | most | most, incl. SG |

**Two independent locks.** (1) **Currency:** a USD-only catalog mechanically excludes Pix, Boleto, OXXO, SEPA DD, iDEAL and Bancontact — Stripe requires BRL/MXN/EUR prices. (2) **Entity:** if their Stripe account is Singapore-domiciled (inferred from we&robot PTE LTD, **not confirmed**), then Klarna, Affirm, Afterpay, PayPal, ACH, Pix, Boleto and OXXO are **unavailable to them on Stripe at any currency.**

**→ So "no BNPL" is not a configuration choice — on a Singapore Stripe entity that lever is closed. For a $199–$498 annual ticket that is an orchestration argument, not a settings argument.**

⚠️ **This is the one thing most worth confirming at revisit:** if they actually hold a **US** Stripe entity, Klarna/Affirm/Afterpay/ACH/Pix become enablable and this argument weakens considerably.

**🔑 And Stripe has nothing at all for their #3 market.** Grepping Stripe's full support page for `fawry|meeza|valu|vodafone cash|zaincash|fastpay|qi card|instapay|egypt|iraq` returns **0 matches.** **Sogni could not enable a single Egyptian or Iraqi local method on Stripe even if they priced in EGP/IQD.** Reaching Egypt requires a PSP Stripe does not provide.

### 5d. Egypt and Iraq — the most engaged markets with the least viable checkout

Egypt is **#3 at 5.65%, ▲1,223% QoQ, with a 26:38 average session — the deepest engagement in their entire table.** Iraq: 1.53%, ▲848%, 24:03 sessions. **These are not bounce-and-leave markets.**

Their options in Cairo or Baghdad are exactly three: an international-enabled card, Apple/Google store billing, or crypto.

⚠️ **All market context below is `[UNVERIFIED — search summaries, several from payment vendors with a commercial interest, several undated]`. Do not quote any figure without fetching the source.** Egypt: card penetration reported ~3%; cards under a third of online purchases; COD 40–45%; **Meeza — a domestic-only scheme that generally cannot complete a USD cross-border subscription — now reported as more than half of all cards issued.** Published (undated) EG Bank monthly international caps: **Classic $500, Titanium $1,000, Platinum $2,000**, plus a 3% FX markup.

**🔑 The mechanical collision, if those caps are right: a $498 annual Pro authorization hold consumes ~100% of a Classic cardholder's entire monthly international allowance; the $199 hold consumes ~40%.** For most Egyptian cardholders the annual plan is not a hard sell — it is arithmetically impossible.

**And crypto — the one rail that works there — has no trial:** *"Crypto plans are prepaid one-time purchases: they never auto-renew, there is nothing to cancel, and **there is no free trial**."* **Egypt and Iraq get the worst of both: no local rail, a card gate on the free tier, and no trial on the only rail available to them.**

### 5e. No tax configuration anywhere

| Question | Finding |
|---|---|
| "VAT" mentioned? | **Zero occurrences** across 9 fetched pages incl. ToS and Privacy |
| "GST" / "sales tax"? | **Zero** |
| "merchant of record"? | **Zero** |
| Tax-inclusive or exclusive? | **Never stated.** All live prices `tax_behavior: unspecified` |
| What the ToS says | Tax pushed to the customer: *"**You are responsible for accurate billing details and applicable taxes**"* (§5, v2026-08-26) |

A **Singapore** entity selling USD-priced digital subscriptions to German, Italian and UK consumers (**8.11% of traffic**), with no VAT registration referenced anywhere and prices not configured for tax calculation. ⚠️ **This is not a finding of non-compliance** — they may hold an unpublished OSS registration, and the Session-level tax config was not visible. But it is the textbook trigger for a merchant-of-record or tax layer, and a credible non-salesy opening with finance rather than growth at revisit.

### 6. USD-only, zero local rails, across 29% APAC traffic

**Currency census, verified in `dash.js`: `"USD"` 4, `"usd"` 7 — and ZERO INR, IDR, EUR, GBP, AUD, PHP, VND, THB, MYR, BRL, EGP.** Formatters hardcoded `en-US`. No currency switcher, no geo-pricing.

Their own FAQ: *"Apple and Google show **localized** subscription prices that may differ from the **advertised US $20/month web price**."* — **the app stores localize price; their own web checkout does not.** And the two are walled off: *"Website checkout cannot spend Play credits, even if Google Pay is available."*

**Across eight APAC markets making up 29.10% of traffic — India, Indonesia, Malaysia, Philippines, Vietnam, Thailand, Australia, Pakistan — the local-rail count is ZERO.** Basis: three large fetched pages plus the complete **210-URL `docs.sogni.ai` sitemap**, whose entire `/pricing/` branch is `apple-subscription-refunds`, `cancel-unlimited-subscription`, `cancellation-and-refund-policy`, `fair-use-queue`, `google-play-subscriptions`, `pay-with-crypto`, `unlimited-plan-details`. **Four rails, no fifth.**

### 7. India is a toggle they have not flipped — resolved definitively

India is **15.32% of traffic, their #2 market, highest audience share in the table at 19.99%**. No UPI, no UPI Autopay, no netbanking, no RuPay, no EMI, no INR price.

**I fetched Stripe's own docs (`docs.stripe.com/payments/upi.md`, HTTP 200) to settle whether they even could:**
- *"UPI supports both one-time payments and **recurring payments through e-mandates (also known as UPI AutoPay)**."*
- Presentment currency **INR**; **Recurring payments: Yes**; available to **Subscriptions**, Invoicing and Payment Links.
- *"Recurring payments are limited to a maximum of **15,000 INR**."* — a $20/mo ticket (~₹1,780) sits comfortably inside.
- **Business locations: both `SG` and `US` are on Stripe's eligible list.** ✅

**So whichever way their Stripe account is domiciled, UPI with AutoPay is available to them and is a Dashboard toggle. This is a pure execution gap, not a structural blocker.** That is a clean, evidenced observation for the revisit.

⚠️ **The RBI e-mandate specifics could NOT be sourced** — `support.stripe.com/questions/rbi-e-mandate-regulations-faqs` served a JavaScript shell. **Do not cite e-mandate rules, thresholds or deadlines from memory in any future outreach.** Pull a current primary source first.

### 8. The 51% formula — payment costs are indexed to supply-side payouts

From their July 2026 launch release: *"participating GPU operators accrue **51% of net subscription revenue — calculated after payment fees, taxes and refunds**."* **Confirmed in their own API: `workerSharePct: 51`.** October's operator pool is **$69,766.58**.

**Every basis point of MDR, every failed retry and every refund directly reduces what GPU operators earn**, which affects supply-side retention on the network they depend on. That turns cost-of-payments into a supply-network argument. **It is also a growing monthly cross-border mass-payout obligation in USD — a second payments problem alongside inbound acceptance.**

---

## Company facts

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

*Researched 2026-10-07. Volume gate overridden by Prateek on 2026-10-07 — see the ICP breakdown.*


</details>
