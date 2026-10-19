# Linktree

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 20 / 29 computed → **analyst override DOWN to 🟢 Medium** (16 adjusted; see breakdown)
**Industry:** Creator SaaS: link-in-bio subscriptions (Starter/Pro/Premium) plus creator commerce ("Earn") · **HQ:** Melbourne, Australia (Linktree Pty Ltd, ABN 68 608 721 562) · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** 🛠️ **In-house.** Linktree's own billing code routes subscriptions across **Stripe (two accounts: AU and US), Braintree (PayPal) and a dLocal gateway**, all sitting behind **Chargebee**. **Never tell them they need orchestration.** Argue reach (the markets the layer doesn't cover) and the opportunity cost of building each one.

---

> ## ⭐ THE FINDING — they localised the price for Indonesia and India, but not the payment method
>
> Verified first-hand in Linktree's production billing bundle (`assets.production.linktr.ee/mfe-billing/`, chunk `static/js/async/537.118901.js`):
>
> ```js
> f = { Braintree:"braintree", Dlocal:"dlocal", Stripe:"stripe" }            // gateway enum
> x = e => e ? "USD"===e.toUpperCase() ? "US" : "AU" : null                  // Stripe account picked by currency
> v = { AUD, BRL, CAD, COP, EUR, GBP, IDR, INR, MXN, MYR, USD }              // 11 billing currencies
> paymentSourceGateway:"braintree"  // PayPal path
> paymentSourceGateway:"stripe"     // card / Apple Pay / Google Pay / Link
> "pixLabel":"Pix Automático"       // Brazil's recurring Pix rail
> ```
>
> - **Billing UI:** translated into Bahasa Indonesia, Malay, Hindi, Portuguese and others. The Indonesian copy reads: *"Kami akan menahan sementara sejumlah kecil dana di kartumu…"* ("we will temporarily hold a small amount on your card").
> - **Payment methods in the bundle:** `card`, `link`, `apple_pay`, `google_pay`, `paypal`, `pix`. **No QRIS, GoPay, OVO, DANA, ShopeePay, virtual account, UPI, FPX or GrabPay** (grep verified; the only "dana" hit is the Indonesian word for "funds" in the card-hold notice).
> - **Where each currency goes:** USD goes to the US Stripe account. **Every other currency, IDR and INR included, goes to the AU Stripe account.** That an Indonesian card billed in IDR is then acquired cross-border out of Australia is `[INFERENCE, not confirmed]`, but it follows directly from the routing line.
> - **The asymmetry:** Brazil got a local recurring rail (Pix Automático). Indonesia, Linktree's **#2 traffic market at 13.81%**, got local currency and local-language copy on top of a card form. India (3.35%) got the same treatment.
> - **Linktree admits the cost itself:** its failed-payment help article lists *"online or international purchases blocked"* as a cause of failed payments ([help](https://linktr.ee/help/en/articles/5434082-why-payment-failed)).
> - **They are actively hiring for this:** "Senior Software Engineer, Growth (**Payment Localization**)" — integrate *"third-party payment service providers"* and *"various payment methods and gateways"* ([Built In](https://www.builtinchicago.org/job/senior-software-engineer-growth-payment-localization/8879102); listing now closed).

> ## ⚠️ Read the traffic before using it
> - **Source:** SimilarWeb Sales Intelligence, supplied by Prateek 2026-10-19 (`accounts/traffic/linktree.md`). It covers Jul–Sep 2026, linktr.ee only, **desktop + mobile web only (no app traffic)**, and shows the top 10 countries only, as shares.
> - **Per-country visit counts below are derived** (share × 203.3M avg monthly visits), not SimilarWeb figures.
> - **Visitors are not payers.** Most linktr.ee visits are people clicking a creator's link page. A market's share of visits says where creators' *audiences* are, not where Linktree's *paying subscribers* are. Two ICP signals (3+ countries, traffic outside home) rest on this split. The override below discounts them for exactly this reason.
> - **Some subscriptions bypass Linktree's PSPs entirely:** some Pro plans are bought in the mobile app (Apple/Google billing), and creator commerce settles on creators' own Stripe accounts.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Linktree is a Melbourne-founded link-in-bio platform with "70M+ Linkers" ([about](https://linktr.ee/s/about)).
- **How it makes money:** tiered subscriptions (Starter US$8 / Pro US$15 / Premium US$35 per month, cheaper billed annually) plus a plan-based take rate on creator sales of digital products, courses and Bookings ([pricing](https://linktr.ee/s/pricing)).
- **Who bills:** Linktree Pty Ltd (Australia) is the contracting and billing entity for subscribers worldwide ([terms](https://linktr.ee/s/terms)).

**SimilarWeb total visits (last full month):** ~203.3 million average per month, Jul–Sep 2026 (609.9M over the 3 months) — **supplied** (SimilarWeb Sales Intelligence, linktr.ee only, web only).

### Top 5 markets
| Rank | Country | Traffic | Accepted methods (web subscriptions) | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇺🇸 United States | 26.63% | Card, PayPal, Apple Pay, Google Pay | None material flagged | ✅ Linktree, Inc. |
| 2 | 🇮🇩 **Indonesia** | **13.81%** | Card, PayPal, Apple Pay, Google Pay. IDR is a billing currency in code | **QRIS, GoPay / OVO / DANA / ShopeePay, virtual account** — absent from code and help docs | ❌ none found (whether the regulator gates domestic acquiring is unverified) |
| 3 | 🇧🇷 Brazil *(out of APAC territory)* | 12.25% | Card, PayPal, Apple/Google Pay. **Pix Automático in code** (whether it is live is unverified) | Boleto | ❌ none found |
| 4 | 🇬🇧 United Kingdom | 4.81% | Card, PayPal, Apple Pay, Google Pay | None material flagged | ✅ Linktree International UK Ltd (15882736) |
| 5 | 🇮🇳 **India** | **3.35%** | Card, PayPal, Apple Pay, Google Pay. INR is a billing currency in code | **UPI / UPI Autopay, RuPay, netbanking** — absent from code and help docs | ❌ none found |

### Legal entities
- **Linktree Pty Ltd** (Australia) — ABN 68 608 721 562 / ACN 608 721 562. Contracting and billing entity ([ABR](https://abr.business.gov.au/ABN/View?abn=68608721562), [terms](https://linktr.ee/s/terms))
- **Linktree International Holdings Pty Ltd** (Australia) — ABN 87 650 946 580 ([privacy notice](https://linktr.ee/s/privacy))
- **Linktree Group Holdings Pty Ltd** (Australia) — ABN 54 663 360 049. Probably the holding company (unverified)
- **Linktree, Inc.** (USA) — state and number not found ([privacy notice](https://linktr.ee/s/privacy))
- **Linktree International UK Limited** (UK) — Co. No. 15882736, incorporated 2024-08-07 ([Companies House](https://find-and-update.company-information.service.gov.uk/company/15882736))

### Known PSPs
- **Chargebee** — subscription billing engine `[Source Code]` (global, web)
- **Stripe** — two merchant accounts, AU (all non-USD currencies) and US (USD). Cards, Apple Pay, Google Pay, Link, SetupIntents with 3DS `[Source Code]`. Also **Stripe Connect** (Standard + Express) for creator commerce `[Developer Docs]` `[Source Code]`
- **Braintree** — PayPal on subscriptions `[Source Code]` (global)
- **dLocal** — gateway enum value in billing code `[Source Code]`. Probably Brazil / Pix `[INFERENCE, not confirmed]`
- **PayPal, Square** — named as current "Payment Providers" in the privacy notice (effective 2026-07-05). Their creator-commerce flows look legacy `[Terms/Privacy Policy]`
- **Apple App Store / Google Play** — in-app subscription billing; Linktree "is unable to process refunds" on these ([terms](https://linktr.ee/s/terms))

### Orchestration status
**In-house orchestration layer.**
- **What the code does:** Linktree's own GraphQL billing layer sets `paymentSourceGateway` per method (Braintree for PayPal, Stripe for everything else) and picks the Stripe account (AU or US) by currency. A third gateway, dLocal, is wired in, all on top of Chargebee `[Source Code]`.
- **What it doesn't show:** no third-party orchestrator was found (Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails and Yuno all searched). There is also no evidence of approval- or cost-based routing, or of failover between PSPs. The routing is **static**, by method and currency.

### Buying signals
- 💼 **Payment Localization hire:** "Senior Software Engineer, Growth (Payment Localization)" — integrate third-party PSPs, payment methods and gateways ([Built In](https://www.builtinchicago.org/job/senior-software-engineer-growth-payment-localization/8879102); closed). Also open: "Senior Software Engineer, Earn" — subscriptions, checkout, payouts, "payment provider contracts", payment recovery ([Built In](https://www.builtinboston.com/job/senior-software-engineer-earn/11452448))
- 🚀 **Local billing already built:** 11 billing currencies including IDR, INR and MYR, plus Pix Automático (`mfe-billing` source; launch date unknown)
- 🤝 **Acquisition:** Fingertip (Melbourne) acquired 2025-11-13; its co-founder Olly Hoffman is ex-Klarna ([SmartCompany](https://www.smartcompany.com.au/startupsmart/linktree-acquires-leibovich-brothers-backed-fingertip-to-shut-it-down/))
- 🚀 **Earn launch:** monetisation suite launched 2025-04-23, with native digital products and a single creator wallet ([TechCrunch](https://techcrunch.com/2025/04/23/linktree-rolls-out-a-suite-of-monetization-features-for-creators/))

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Linktree` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 20 / 29 computed → 16 adjusted → 🟢 Medium (override)
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5 ⚠️** | **⚠️ NOT FOUND — ASSUMED ~150,000–300,000 web billing events/month.** `[ASSUMPTION — not researched.]` Linktree has never disclosed paying subscribers, revenue or GMV; in 2022 it declined to give its paid share ([TechCrunch](https://techcrunch.com/?p=2284606)). **Basis:** Sacra *estimates* 2024 revenue at US$55.5M ([Sacra](https://sacra.com/c/linktree/)). That is a third-party estimate, not a sourced figure, so anything derived from it is still an assumption. US$55.5M ÷ an assumed ~US$10 blended monthly price ≈ ~460K paying subscribers. Then remove (a) annual-plan subscribers, who are billed once a year, and (b) app-store subscribers, who are billed by Apple/Google. Both shares are unknown. **Billing unit counted:** one Chargebee renewal or charge on the web. **Excluded:** creator-commerce sales, which settle on creators' own Stripe Connect accounts and are not Linktree's merchant volume. Even at the low end the figure clears 100K, so the rejection rule cannot fire. **Confirm on the first call.** |
| Orchestration status | +1 | ✅ **In-house layer** — gateway selection by method and currency across Stripe AU, Stripe US, Braintree and dLocal on Chargebee `[Source Code]` |
| 3+ countries | +3 | ✅ 10 countries above 1% traffic share (supplied SimilarWeb). 3 confirmed entity countries (AU, US, UK) |
| Multiple PSPs | +3 | ✅ Stripe + Braintree confirmed in production code. dLocal wired as a gateway (live use unverified) |
| Local rail or licensing gap in a top-3 market | +3 | ✅ **Indonesia (#2, 13.81%)**: QRIS, e-wallets and virtual account are absent from the billing code and from help docs ([help](https://linktr.ee/help/en/articles/5434083-upgrade-linktree-plan)), even though IDR is a supported billing currency. QRIS hit 13.66B transactions and 59M users in 2025 ([Marketing-Interactive, Bank Indonesia figures](https://www.marketing-interactive.com/bi-unveils-cross-border-expansion-and-merchant-growth-plans-for-qris)) |
| Recent expansion | 0 | ⬜ The Fingertip acquisition (Nov 2025) and the Bento migration (Feb 2026) are consolidation, not new markets. Localised currencies exist, but their launch date is unknown |
| Payment issues reported | +2 | ✅ Moderate. Trustpilot billing complaints (charged after cancelling, double charge with 2 cards on file, refunds refused after 72h), 2025–2026 ([Trustpilot](https://www.trustpilot.com/review/linktr.ee?page=9)). **Caveat:** these are about billing policy, not declines |
| Funding >$10M | 0 | ❌ Last round 2022-03 (US$110M at US$1.3B) ([TechCrunch](https://techcrunch.com/?p=2284606)). Nothing in the last 12 months |
| High traffic outside home | +2 | ✅ Australia is not in the top 10 at all |
| Competitor using orchestration | 0 | ⬜ No direct competitor confirmed on an orchestrator. Canva (peer) states a multi-gateway routing plan ([Stripe](https://stripe.com/cn/customers/canva)). Not an orchestrator adoption |
| Payment job postings | +1 | ✅ Payment Localization, Payments, and Earn engineering roles (Section 6) |

**Computed: 20 / 29 → ⭐ High Priority. Tier after analyst override: 🟢 Medium (16 adjusted).**

**Analyst override — DOWN to 🟢 Medium.** Reasoning:
1. **Double-counting one fact.** "3+ countries" and "high traffic outside home" both fire on the same *visitor* split, and visitors are mostly creators' audiences, not payers (−2).
2. **The payment-issues signal is policy-driven.** The complaints are about refund windows and renewal surprise, not declines or rail failures, so orchestration doesn't fix them (−2).
3. **The +5 volume band is assumed, not sourced.** It rests on a third-party revenue estimate.
4. **In-house motion is the hardest sale.** They built a routing layer and are hiring to extend it.

**What would push it back to ⭐:**
- the share of paying subscribers in Indonesia and India, and
- the web-vs-app-store billing split.

If Indonesia is a top-5 *paying* market, the IDR-priced-but-card-only gap is a ⭐ story.

### Source Notes
- ✅ **Production billing code** (gateway enum, currency routing, 11 currencies, Pix Automático, Bahasa Indonesia card-hold copy): verified first-hand by grep of the `mfe-billing` bundle, 2026-10-19
- ✅ **Billing entity:** Linktree Pty Ltd ([terms](https://linktr.ee/s/terms))
- ✅ **Payment providers:** "Stripe; PayPal; and Square" ([privacy](https://linktr.ee/s/privacy))
- ✅ **Web payment methods:** card, PayPal, Google Pay, Apple Pay. In-app purchases are billed by the app store ([help](https://linktr.ee/help/en/articles/5434083-upgrade-linktree-plan))
- ✅ **Earn (creator selling) countries:** in APAC only AU, HK, JP, NZ, SG; **excludes ID, IN, BR, MX, AR** ([help](https://linktr.ee/help/en/articles/11126119-earn-feature-requirements-limits), verified by curl)
- ✅ **India outage:** Linktree was inaccessible in India for several days in Aug 2025 ([TechCrunch](https://techcrunch.com/2025/08/18/linktree-goes-dark-in-india-and-the-company-isnt-sure-why/))
- ⚠️ **dLocal → Pix mapping:** inferred, not seen as an explicit mapping in code
- ⚠️ **Cross-border acquiring of IDR/INR via Stripe AU:** inferred from the routing line
- ⚠️ **Local-currency web pricing:** the pricing page served USD to our (US) egress IP. Whether ID/IN visitors see IDR/INR on the web is untested. iOS in-app prices *are* shown in IDR, INR and BRL ([App Store ID](https://apps.apple.com/id/app/linktree-link-in-bio-creator/id1593515263))
- ⚠️ **Revenue:** US$55.5M (2024) is a Sacra estimate, not disclosed by Linktree

### Success Case Alternatives
- **inDrive** — Tier 2, the **reach** case: "10 new countries in under 8 months." That fits an in-house team that has localised one market's rails (Brazil/Pix) and is hiring to do the rest one by one. Pattern match only; LATAM-centred results, so say so. [y.uno](https://y.uno/en/success-stories/indrive)
- **Livelo** — Tier 2, the decline-cascade case (+5% approval, 50% of failed transactions recovered by routing to a secondary acquirer). Fits **renewal recovery**: Linktree runs 2 Stripe accounts + Braintree with no evidence of failover between them. LATAM results; say so. [y.uno](https://y.uno/en/success-stories/livelo)
- **Whop / Hotmart** — **nameable only, no metrics.** Both are on Yuno's site-wide customer list and both are creator-commerce platforms, the closest vertical match in the library. Use them as a relevance signal; they cannot carry an E4.
- **Garena** — nameable only. SEA consumer billing on local rails; a relevance signal for the Indonesia angle.
- No Tier 1 (creator SaaS with quantified results) exists in the library.

---

## Executive Summary

Linktree is an Australian-HQ'd creator platform that bills a global, mostly low-ticket subscription base from **Linktree Pty Ltd** and takes a cut of creator sales through Stripe Connect.

- **The stack:** it has quietly built its own routing layer over Chargebee. Gateway is picked by payment method (Braintree for PayPal, Stripe for the rest) and the Stripe account by currency (US for USD, AU for everything else), with dLocal wired in. Billing is localised into 11 currencies, including IDR and INR.
- **The gap:** the payment methods didn't follow the currencies. Indonesia, the #2 traffic market, gets IDR pricing and Bahasa copy on a card-only form with no QRIS, e-wallets or virtual account. India gets INR with no UPI.
- **The motion is in-house.** The opening is the cost of building every remaining market themselves, which their own "Payment Localization" hiring shows they are doing, rather than the case for orchestration.

---

## Section 1: Website Traffic Analysis by Country

**Data source:** Path 1 — **pasted SimilarWeb data**, "SimilarWeb (supplied 2026-10-19)", Sales Intelligence view, `accounts/traffic/linktree.md`.
- **Period and domain:** Jul–Sep 2026, linktr.ee only. `linktree.com` and `www.linktree.com` both 301 to `https://linktr.ee/`, so no other domain carries separate traffic (verified by curl).
- **Global rank:** not captured.
- **Device split:** Desktop 32.14% / Mobile Web 67.86%.
- **Trend:** not supplied.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | 🇺🇸 United States | 26.63% | ~54.1M `[DERIVED from supplied share, not a SimilarWeb figure]` | N/A | SimilarWeb (supplied 2026-10-19) |
| 2 | 🇮🇩 **Indonesia** | **13.81%** | ~28.1M `[DERIVED]` | N/A | same |
| 3 | 🇧🇷 Brazil | 12.25% | ~24.9M `[DERIVED]` | N/A | same |
| 4 | 🇬🇧 United Kingdom | 4.81% | ~9.8M `[DERIVED]` | N/A | same |
| 5 | 🇮🇳 **India** | 3.35% | ~6.8M `[DERIVED]` | N/A | same |
| 6 | 🇨🇦 Canada | 2.74% | ~5.6M `[DERIVED]` | N/A | same |
| 7 | 🇲🇽 Mexico | 2.26% | ~4.6M `[DERIVED]` | N/A | same |
| 8 | 🇦🇷 Argentina | 2.12% | ~4.3M `[DERIVED]` | N/A | same |
| 9 | 🇫🇷 France | 2.03% | ~4.1M `[DERIVED]` | N/A | same |
| 10 | 🇩🇪 Germany | 1.95% | ~4.0M `[DERIVED]` | N/A | same |

Top 10 = 71.95%. The remaining 28.05% is unlisted, so Australia, the HQ market, sits below 1.95%.

- **High priority (>5%):** US, Indonesia, Brazil.
- **Top-10 markets with no local entity:** Indonesia, Brazil, India, Canada, Mexico, Argentina, France, Germany (see Section 2).
- **APAC-relevant markets in the top 10:** Indonesia and India only. Brazil, Mexico and Argentina are LATAM; Yuno is strong there, but they are not this territory's markets.

**Caveats from the supplied file (verbatim intent):**
1. Sales Intelligence view: top-10 shares only. Visit counts above are derived.
2. Single domain, so no aggregation was needed.
3. **Mobile app traffic is not included.**
4. **linktr.ee visits are mostly visitors clicking creator links, not paying users.** Some Pro subscriptions are bought in-app (app-store billing), and creator commerce flows through creators' own Stripe / PayPal / Square accounts.

---

## Section 2: Legal Entities & Local Presence

**Headquarters:** Collingwood, Melbourne VIC 3066, Australia.
- **Incorporated:** Linktree Pty Ltd, 2015-10-13 ([ABR](https://abr.business.gov.au/ABN/View?abn=68608721562)).
- **Offices:** Melbourne (HQ), Los Angeles (Culver City), San Francisco and London. The about page lists exactly four offices and no Sydney ([about](https://linktr.ee/s/about)).

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Australia | **Linktree Pty Ltd** — contracting and billing entity. Registered business names "Linktree" and "Plann" | ABN 68 608 721 562 / ACN 608 721 562 | https://abr.business.gov.au/ABN/View?abn=68608721562 ; https://linktr.ee/s/terms |
| Australia | Linktree International Holdings Pty Ltd | ABN 87 650 946 580 | https://abr.business.gov.au/Search/ResultsActive?SearchText=linktree ; https://linktr.ee/s/privacy |
| Australia | Linktree Group Holdings Pty Ltd (likely the holding company, unverified) | ABN 54 663 360 049 | https://abr.business.gov.au/Search/ResultsActive?SearchText=linktree |
| USA | Linktree, Inc. | Not found | https://linktr.ee/s/privacy |
| UK | Linktree International UK Limited | 15882736 (inc. 2024-08-07) | https://find-and-update.company-information.service.gov.uk/company/15882736 |
| EU | No entity. GDPR representative only (Instant EU GDPR Representative Ltd, Dublin) | — | https://linktr.ee/s/privacy |

⚠️ **Do not confuse with "LINKTREE LIMITED" (UK, 02101938).** That is a 1987 building-development company and is unrelated.

**Contracting terms** ([terms](https://linktr.ee/s/terms), effective 2026-07-05):
- "we/us" = Linktree Pty Ltd, Plann and group companies; Victorian law governs.
- Subscriptions are billed in advance, monthly or annually, and auto-renew.
- **App-store purchases cannot be refunded by Linktree.**
- For creator commerce, the creator is **Seller of Record** on a processor "designated by us, for example Stripe."

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| United States | ✅ #1 | ✅ Linktree, Inc. | N/A | Low — USD routes to the **US Stripe account** `[Source Code]` |
| Indonesia | ✅ #2 | ❌ None found | Unverified — rules not sourced in this run | **High** — IDR routes to the **AU Stripe account** `[Source Code]`, so this is likely cross-border `[INFERENCE]` |
| Brazil | ✅ #3 | ❌ None found | Not assessed (out of territory) | Medium — dLocal gateway present, which may localise BR `[INFERENCE]` |
| United Kingdom | ✅ #4 | ✅ UK Ltd | N/A | GBP routes to the AU Stripe account `[Source Code]` |
| India | ✅ #5 | ❌ None found | Unverified — rules not sourced in this run | **High** — INR routes to the AU Stripe account `[Source Code]` |
| Canada / France / Germany | ✅ #6, #9, #10 | ❌ | N/A | CAD/EUR route to the AU Stripe account |
| Mexico / Argentina | ✅ #7, #8 | ❌ | Not assessed (out of territory) | MXN routes to the AU Stripe account. No ARS currency |

> *"Warning: Potential cross-border operation in **Indonesia**. No local entity found. Transactions are likely processed cross-border, with higher scheme costs, lower approval rates and FX exposure."* Supporting it: the code sends every non-USD currency to the AU Stripe account, and Linktree's own help article lists *"online or international purchases blocked"* as a failure cause ([help](https://linktr.ee/help/en/articles/5434082-why-payment-failed)).

> *"Warning: Potential cross-border operation in **India**. No local entity found."* Same evidence. India also had a multi-day access outage in Aug 2025 ([TechCrunch](https://techcrunch.com/2025/08/18/linktree-goes-dark-in-india-and-the-company-isnt-sure-why/)).

> **Regulatory gate:** Indonesia and India are flagged in the APAC reference as markets where domestic acquiring is effectively gated behind local presence. **This was not verified with a current source in this run, so it is not asserted.** Verify before using.

> **MANUAL:** Check the receipt and statement descriptor on an IDR-billed Linktree subscription. That shows which Stripe entity acquires it and whether the charge is cross-border.

---

## Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Global (web subs) | **Chargebee** — subscription billing engine (`GetChargebeeInvoices`, `chargebeeSubscription`) | [Source Code] | `https://assets.production.linktr.ee/mfe-billing/` (bundle, fetched 2026-10-19) |
| USD | **Stripe (US account)** — cards, Apple Pay, Google Pay, Link; SetupIntent + `confirmCardSetup` 3DS | [Source Code] | same bundle (`STRIPE_US_PUBLISHABLE_KEY`, `"USD"===e.toUpperCase()?"US":"AU"`) |
| All non-USD (AUD, BRL, CAD, COP, EUR, GBP, IDR, INR, MXN, MYR) | **Stripe (AU account)** | [Source Code] | same bundle (`STRIPE_AU_PUBLISHABLE_KEY`) |
| Global | **Braintree** — the PayPal path (`paymentSourceGateway:"braintree"`); braintree-web modules bundled | [Source Code] | same bundle |
| Probably Brazil | **dLocal** — gateway enum `Dlocal:"dlocal"` alongside Pix Automático labels. Live use unverified | [Source Code] | same bundle, chunk `537.118901.js` |
| Global (app) | **Apple App Store / Google Play** in-app billing | [Terms/Privacy Policy] / Help | https://linktr.ee/help/en/articles/5434083-upgrade-linktree-plan ; https://linktr.ee/s/terms |
| ~40 Earn countries | **Stripe Connect** — Standard accounts (sell products, tips) and Express (affiliate/Shops commission payouts) | [Developer Docs] / [Source Code] | https://linktr.ee/help/en/articles/10518645-guide-to-selling-digital-products-on-linktree ; https://linktr.ee/help/en/articles/11410206-understanding-transaction-and-processing-fees-on-linktree |
| Global | **Stripe, PayPal, Square** — "The Payment Providers we currently work with" | [Terms/Privacy Policy] | https://linktr.ee/s/privacy |
| 200+ countries (2021, legacy) | **PayPal** — Commerce Links / Support Me | [Press Release] | https://techcrunch.com/2021/08/24/linktree-partners-with-paypal-to-allow-users-globally-to-accept-direct-payments/ |
| AU, CA, UK, US (legacy) | **Square** — "Support Me" tips | [Provider Case Study] | https://squareup.com/help/gb/article/7430 |

**Regional PSPs:** no Linktree link found to Xendit, Midtrans or DOKU (Indonesia), Razorpay, PayU or Cashfree (India), or EBANX (Brazil). The bundle contains no such integration.

**Status of the PayPal/Square creator flows:** they look legacy. None of the 182 current help-centre articles covers them, and the current commerce bundle has no PayPal or Square connect flow `[INFERENCE]`.

#### 3B. Payment Orchestrator

**Classification: In-house orchestration layer.** Evidence type: [Source Code].
- Linktree's GraphQL billing layer (`graph.linktr.ee`) selects the gateway per payment method (Braintree for PayPal; Stripe for cards and wallets).
- It selects the Stripe merchant account per currency (US for USD, AU for everything else).
- It carries dLocal as a third gateway.
- Chargebee is the subscription system of record.
- Orchestrator searches found nothing: Juspay, "payment orchestration", Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno. BuiltWith returned 404 for linktr.ee.
- The TAL `Payment Orchestrator` column is empty.

**What the layer is not:** there is no evidence of dynamic routing on approval rate or cost, of retries across gateways, or of failover between the two Stripe accounts and Braintree. It is static routing by method and currency.

> **Implication:** argue reach and opportunity cost, never "you need orchestration."
> - Every new local rail is currently a new gateway integration into Linktree's own GraphQL layer and Chargebee. Brazil (Pix via dLocal) shows the cost: one market, one new gateway.

> **MANUAL:** Start an upgrade from an Indonesian and an Indian IP, with DevTools open. Confirm which currency is shown, whether any local method appears, and which Stripe account's `pk_live` key initialises.

**Competitive note:** Stripe Orchestration is in private preview and routes to Adyen, Braintree and Worldpay ([Stripe docs](https://docs.stripe.com/payments/orchestration/feature-support)). Linktree is a Stripe-heavy merchant already running Braintree, so it is an obvious target for that pitch.

---

## Section 4: Alternative & Local Payment Methods

**Two flows, kept separate:**
- **(a) Linktree's own subscriptions** — where Yuno can play.
- **(b) Creator commerce on creators' Stripe Connect accounts** — a platform flow.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| Global (a) | Credit/debit card | Cards | Active in checkout (per docs + code) | https://linktr.ee/help/en/articles/5434083-upgrade-linktree-plan |
| Global (a) | PayPal (via Braintree) | Digital wallet | Active in checkout | same + code |
| Global (a) | Apple Pay / Google Pay (via Stripe) | Digital wallet | Active in checkout | same + code |
| Global (a) | Stripe Link (card + bank) | Digital wallet / A2A | Mentioned in code (`linkCard`, `linkBank`) | `mfe-billing` bundle |
| Global (a) | iOS in-app purchase / Google Play Billing | App store | Active | https://linktr.ee/help/en/articles/5434083-upgrade-linktree-plan ; https://apps.apple.com/us/app/linktree-link-in-bio-creator/id1593515263 |
| Brazil (a) | **Pix Automático** | Direct debit / mandate (A2A) | Mentioned in code (UI label + icon). Live status unverified | `mfe-billing` bundle |
| Brazil (a) | Boleto | Cash/voucher | Not found | — |
| **Indonesia (a)** | **QRIS** | A2A / QR | **Not found** (code + docs) | — |
| **Indonesia (a)** | GoPay / OVO / DANA / ShopeePay | Digital wallet | **Not found** | — |
| **Indonesia (a)** | Virtual account / bank transfer | Bank transfer | **Not found** | — |
| **Indonesia (a)** | Alfamart / Indomaret | Cash/voucher | **Not found** | — |
| **India (a)** | **UPI / UPI Autopay** | A2A / mandate | **Not found** | — |
| **India (a)** | RuPay, netbanking | Cards / bank | **Not found** | — |
| Malaysia (a) *(MYR is a billing currency)* | FPX / DuitNow / Touch 'n Go | Bank / wallet | Not found | — |
| Mexico (a) | OXXO / SPEI | Cash / A2A | Not found | — |
| UK/EU (a) | SEPA DD / Pay by Bank | Bank debit | Not found | — |
| ID, IN, BR, MX, AR (b) | Any paid creator selling | — | **Not available — country not supported for Earn** | https://linktr.ee/help/en/articles/11126119-earn-feature-requirements-limits |
| ~40 Earn countries (b) | Stripe Checkout (buyer methods not itemised) | PSP-hosted | Mentioned in docs | https://linktr.ee/help/en/articles/10518645-guide-to-selling-digital-products-on-linktree |

> *"Warning: In **Indonesia**, **QRIS** is widely used but not currently supported by Linktree."*
> - QRIS reached 13.66 billion transactions, 59 million users and 42 million merchants in 2025 ([Marketing-Interactive, reporting Bank Indonesia](https://www.marketing-interactive.com/bi-unveils-cross-border-expansion-and-merchant-growth-plans-for-qris)).
> - Linktree bills in IDR and shows Bahasa Indonesia billing copy, but the copy tells the user it will hold funds *on their card*.

> *"Warning: In **India**, **UPI** is widely used but not currently supported by Linktree."*
> - UPI processed 24.51 billion transactions in August 2026 ([StartupTalky, reporting NPCI](https://startuptalky.com/india-upi-transactions-august-2026-record-volume/); secondary report, not fetched from NPCI).
> - INR is a supported billing currency, and there is a Hindi billing UI.

**Local currency, app vs web:**
- **iOS in-app prices are localised:** Indonesia Starter Rp 39ribu, Pro Rp 125–149ribu; India Starter ₹249, Pro ₹650–899; Brazil Starter R$14,90 ([App Store ID](https://apps.apple.com/id/app/linktree-link-in-bio-creator/id1593515263), [IN](https://apps.apple.com/in/app/linktree-link-in-bio-creator/id1593515263), [BR](https://apps.apple.com/br/app/linktree-link-in-bio-creator/id1593515263)).
- `[INFERENCE, not confirmed]`: in Indonesia and India, the one confirmed path to a local-feeling price and a familiar wallet experience runs through Apple/Google and their store commission. A web checkout with QRIS/UPI is the lever that pulls those subscribers back to web billing.

**Recurring rails:**
- No UPI Autopay.
- Pix Automático is present in code.
- Indonesia recurring is card-only.

> **MANUAL:** Using a VPN, check web pricing and checkout methods from Indonesia, India and Malaysia.

---

## Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Charged after cancelling / deleting account | Trustpilot (GB) | Moderate (recurring theme) | 2025–2026 | https://www.trustpilot.com/review/linktr.ee?page=9 |
| Duplicate charge (two cards on file) | Trustpilot (GB) | Isolated | 2026-02-19 | https://www.trustpilot.com/review/linktr.ee?page=9 |
| Refund refused ("too late", 72-hour window) | Trustpilot (GB + snippets AU/UK/CA) | Moderate | 2025–2026-09 | https://www.trustpilot.com/review/linktr.ee ; https://au.trustpilot.com/review/linktr.ee?page=10 (snippet only) |
| Renewal after introductory benefit ended (likely the Bento migration) | Trustpilot (DE) | Isolated | 2026-02-04 | https://www.trustpilot.com/review/linktr.ee?page=9 |
| Stripe connection trouble (resolved) | Trustpilot (US) | Isolated | 2026-09-28 | https://www.trustpilot.com/review/linktr.ee |
| Card-decline / failed-payment complaints | — | **None found** | — | — |
| Creator payout complaints (Stripe holds) | — | None found | — | — |

**Context:**
- Trustpilot TrustScore is 4.0 from 7,161 reviews ([Trustpilot](https://www.trustpilot.com/review/linktr.ee)).
- Reddit and App Store / Play reviews were not reached in this run.

**The most useful payment-failure evidence comes from Linktree itself, not from complaints.** Its failed-payment article lists:
- online or international purchases blocked,
- mismatched billing details,
- expired card,
- insufficient funds.

Its fix is "change to a different card or PayPal account" ([help](https://linktr.ee/help/en/articles/5434082-why-payment-failed)). It also places a $1 card pre-authorisation hold ([help](https://linktr.ee/help/en/articles/10597023-1-charge-after-subscribing)).

> *Pattern: the Trustpilot complaints are about cancellation and refund policy, not payment infrastructure, so they are weak Yuno evidence.* The infrastructure signal is the help article: Linktree tells failed payers to *switch card*, not to *switch rail*. For a card-only IDR/INR checkout acquired from Australia, that is a recovery path with nothing local behind it.

---

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | ~2026-01 (closed by 2026-07) | **"Senior Software Engineer, Growth (Payment Localization)"** (SF/LA, US$190–215k). Integrate third-party PSPs and "various payment methods and gateways"; PCI DSS; fraud | Payment Infrastructure Hiring | https://www.builtinchicago.org/job/senior-software-engineer-growth-payment-localization/8879102 |
| 2 | 2026-10 (reposted) | "Senior Software Engineer, Earn" — subscriptions, checkout, entitlements, reconciliation, payouts, "payment provider contracts", payment recovery | Payment Infrastructure Hiring | https://www.builtinboston.com/job/senior-software-engineer-earn/11452448 |
| 3 | 2026-02-13 | Bento shut down; users migrated to Linktree | M&A | https://alternativeto.net/news/2025/12/bento-to-shut-down-in-2026-as-linktree-takes-over-and-offers-migration-path/ |
| 4 | 2025-11-13 | Acquired Fingertip (Melbourne); co-founders Olly Hoffman (ex-Klarna) and Matthew Blode joined | M&A | https://www.smartcompany.com.au/startupsmart/linktree-acquires-leibovich-brothers-backed-fingertip-to-shut-it-down/ |
| 5 | 2025-04-23 | "Earn" suite: native digital products, courses, US Shops, sponsored links, a single creator wallet. Plan-based take rate | Market Expansion (product) | https://techcrunch.com/2025/04/23/linktree-rolls-out-a-suite-of-monetization-features-for-creators/ |

**Other roles and leadership:**
- Earlier payment roles: "Staff Product Manager, Payments" (~2024-12) ([Airtree jobs](https://jobs.airtree.vc/companies/linktree-2/jobs/43493734-staff-product-manager-payments)); "Senior Software Engineer, Growth (Payments)" ([Built In London](https://builtinlondon.uk/job/senior-software-engineer-growth-payments/11465744)).
- Leadership: CEO Alex Zaccaria; CPO Jiaona Zhang (from Jan 2024, [iTWire](https://itwire.com/it-people-news/people-moves/linktree-appoints-new-cpo,-two-technologists-to-lead-machine-learning,-ai-and-personalisation)); CTO Zak Islam (ex-Atlassian, [Mumbrella](https://mumbrella.com.au/linktree-taps-atlassian-for-new-cto-706479)). No CFO found.
- *"No public payment-related RFP found."*

---

## Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 2025-04-23 | Earn suite. Digital products sold natively, replacing the SendOwl partnership; Stripe is the processor | Creator commerce consolidated on Stripe | https://techcrunch.com/2025/04/23/linktree-rolls-out-a-suite-of-monetization-features-for-creators/ |
| 2 | 2025-08-18 | Linktree inaccessible in India for several days; cause unclear | India market risk | https://techcrunch.com/2025/08/18/linktree-goes-dark-in-india-and-the-company-isnt-sure-why/ |
| 3 | 2023-12-14 | Acquired Koji to bring commerce/monetisation tools in-house; Koji shut down 2024-01-31 | Commerce built in-house | https://www.tubefilter.com/2023/12/14/linktree-link-in-bio-acquires-koji/ |
| 4 | 2022 | Payment Lock paywall and "Buy Me a Gift" tipping powered by PayPal and Square | Legacy multi-PSP creator flows | https://thepaypers.com/payments-general/linktree-introduces-3-new-monetisation-features--1260118 |
| 5 | 2021-08-24 | PayPal partnership: creators in 200+ countries accept PayPal and card payments | Legacy | https://techcrunch.com/2021/08/24/linktree-partners-with-paypal-to-allow-users-globally-to-accept-direct-payments/ |

> **Possible REMOVAL:** PayPal and Square creator-payment flows (Commerce Links, Payment Lock, Support Me) no longer appear in the current help centre or commerce code. **No sunset announcement found.** `[INFERENCE, not confirmed]`.

---

## Section 8: Checkout Experience Audit

*"Full checkout flow not accessible. Findings limited to publicly observable elements."* The checkout sits behind login (Descope OIDC). Findings below come from the pricing page, help docs and the billing bundle.

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | Embedded micro-frontend (`mfe-billing`) over Chargebee; Stripe Elements / SetupIntents + Braintree | Good | Custom-built |
| Guest checkout | N/A — account required (SaaS) | N/A | |
| Steps to complete payment | Not observable | — | Free trial CTA defaults to annual Pro (`freeTrial=true&tier=paid2&frequency=annual`) |
| Card input experience | PSP-hosted fields (Stripe Elements; Braintree hosted-fields bundled) | Good | `[Source Code]` |
| Payment methods visible | Card, PayPal, Apple Pay, Google Pay (+ Link; Pix in code) | Fair | No local APMs in Asia |
| Location-based method display | Pix shown for Brazil, per code. Nothing for ID/IN/MY | **Poor for APAC** | |
| Instalment / EMI options | None found | N/A | Low ticket — not material |
| 3DS implementation | `confirmCardSetup` "stripe_3ds" stage; Braintree three-d-secure module | Good | 3DS2 via Stripe `[INFERENCE]` |
| PCI indicator | PSP iframes / hosted fields | Good | |
| Mobile responsiveness | Not tested | — | 67.86% of web traffic is mobile web |
| Multi-currency / local pricing | 11 billing currencies in code. Pricing page served USD to a US IP | Fair | Web localisation per geo untested |
| Saved payment methods | SetupIntent future-payment vaulting; Braintree vault-manager | Good | |
| Error message clarity | Localised error strings (e.g. "Gagal menghubungi gateway pembayaran") | Fair | Failure guidance is "use a different card" |

---

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found. The privacy notice says only that its Payment Providers adhere to PCI-DSS | https://linktr.ee/s/privacy |
| Card data handling | Not found | — |
| Recommended Yuno integration | SDK (keeps the PSP-hosted field pattern) | — |

`[INFERENCE, not confirmed]`: card capture runs through Stripe Elements and Braintree hosted fields, with credentials vaulted at the PSPs. Linktree's PCI scope is therefore likely reduced (SAQ-A-type), with Stripe and Braintree handling card data. A side effect is that **tokens are split across three vaults** (Stripe AU, Stripe US, Braintree) plus the app stores. No network-token evidence was found.

---

## Section 10: Strategic Insights & Outreach Angles

> **Insight #1: Priced in rupiah, paid by card — the Indonesia gap**
> **Evidence:**
> - S1: Indonesia is the #2 market at 13.81%.
> - S4: IDR is a billing currency and the billing UI has Bahasa copy, but QRIS, e-wallets and VA are all absent. QRIS did 13.66B transactions in 2025 ([source](https://www.marketing-interactive.com/bi-unveils-cross-border-expansion-and-merchant-growth-plans-for-qris)).
> - S2/S3: no Indonesian entity, and IDR routes to the AU Stripe account (`mfe-billing` bundle).
>
> **Pain Point:**
> - Indonesian creators who want to pay on the web need a card that accepts an international charge. Linktree's own help article names "international purchases blocked" as a failure cause.
> - The alternative is the App Store, where Linktree loses the refund relationship and the margin.
>
> **Yuno Value Proposition:** QRIS, VA and wallets through local acquiring, behind one integration, without Linktree building and maintaining another gateway in its GraphQL layer.
> **Best Success Case:** inDrive (reach, LATAM results) for speed; Garena as a nameable SEA consumer-billing reference.
> **Outreach Angle:** "Your billing speaks Bahasa and quotes rupiah, then asks for a card. In Indonesia that's the minority rail."
> **Suggested Subject Line:** "Rupiah pricing, card-only checkout"

> **Insight #2: You already did this for Brazil — Indonesia and India didn't get the same treatment**
> **Evidence:**
> - S3/S4: dLocal gateway and Pix Automático in code. For Asia, the only methods are card, PayPal and Apple/Google Pay.
> - S6: the Payment Localization engineering req.
>
> **Pain Point:** each local recurring rail has been a bespoke gateway integration. At one market per project, the APAC list (ID, IN, MY are already priced) is a multi-quarter roadmap for a small growth team.
> **Yuno Value Proposition:** the reach argument. Add QRIS, UPI and FPX as configuration, not as new gateways.
> **Best Success Case:** inDrive — 10 new countries in under 8 months.
> **Outreach Angle:** "Pix Automático tells me you've already decided local recurring rails are worth building. Curious what the plan is for IDR and INR."
> **Suggested Subject Line:** "After Pix Automático — QRIS and UPI?"

> **Insight #3: Three gateway accounts, static routing, no failover on renewals**
> **Evidence:**
> - S3B: currency-based Stripe US/AU split plus Braintree, with no dynamic routing or retry across them.
> - S5: failed-payment guidance tells users to change card.
> - S1/S2: most non-USD volume goes through one AU acquiring account.
>
> **Pain Point:** a soft-declined renewal on the AU account has nowhere else to go. Recovery depends on the subscriber acting, which is involuntary churn on a low-ticket book.
> **Yuno Value Proposition:** smart routing and cascade retry across the acquirers Linktree already holds, plus local acquirers in issuer geographies.
> **Best Success Case:** Livelo — 50% of failed transactions recovered by routing to a secondary acquirer (LATAM; say so).
> **Outreach Angle:** "When a renewal declines on your AU Stripe account, does it ever get a second try anywhere else, or does it go straight to 'update your card'?"
> **Suggested Subject Line:** "Second attempt on declined renewals"

> **Insight #4: A third of the audience can't sell on Linktree**
> **Evidence:**
> - S4: Earn is unavailable in ID, IN, BR, MX and AR.
> - S1: those five markets are ~33.8% of traffic.
> - S3: creator commerce is Stripe Connect only.
>
> **Pain Point:** the monetisation suite, the strategic bet since the Apr 2025 launch, is closed to Linktree's biggest emerging-market creator bases.
> **Yuno Value Proposition:** `[INFERENCE — validate on call]` broader PSP and local-rail coverage could be part of opening Earn to those markets. Marketplace and payout mechanics need scoping; do not promise them.
> **Best Success Case:** Whop and Hotmart — nameable creator-commerce Yuno customers. **No metrics.**
> **Outreach Angle:** "Indonesia, Brazil and India are a third of your traffic and none of them can sell through Earn. Is that a payments constraint or a policy one?"
> **Suggested Subject Line:** "Earn in Indonesia"

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. Your billing flow quotes rupiah and talks to Indonesian creators in Bahasa, then holds funds on a card. In a market that ran 13.66B QRIS transactions last year, that's the minority path.
2. You built Pix Automático for Brazil. IDR, INR and MYR are already in your billing currencies without a single local method behind them.
3. Indonesia, Brazil and India are ~30% of linktr.ee traffic and none of them are on the Earn country list.

**Cold call openers (conversational, one sentence each):**
1. "Saw you're hiring for payment localization. Is Indonesia on that list, given it's your second-biggest market?"
2. "Quick one: when an Indonesian card declines on a renewal, does Linktree have anywhere to send it other than back to the subscriber?"
3. "You've got Stripe in two regions, Braintree and dLocal behind Chargebee. Who owns adding the next rail, and how long does one take?"

---

## Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| Beacons | beacons.ai | USA (San Francisco) | ~$52M raised (CB Insights) | US, global creators | Stripe + PayPal payouts | https://help.beacons.ai/en/articles/4700481 ; https://www.cbinsights.com/investor/beacons |
| Stan (Stan Store) | stan.store | USA (sources conflict: NY / LA) | ~$40M ARR claimed (company-linked PR) | US | Stripe Connect + PayPal (third-party blog only) | https://cartmango.com/stan-store-pricing/ |
| Lynk.id | lynk.id | Indonesia (Jakarta) | No funding found | Indonesia | Gateway not identified. Offers e-money, QRIS, VA, Indomaret | https://ghost.bitscale.ai/lynkid |
| Lnk.Bio | lnk.bio | Not found | Not found | Not found | Stripe Connect + PayPal | https://o-mega.ai/tools/lnk-bio |
| Bio Sites (Squarespace) | biosites.com | USA | Not found | US | Stripe or PayPal connect | https://blog.biosites.com/blog/easily-accept-payments-online-connect-stripe-or-paypal-to-your-bio-site |

**Telling contrast:** Lynk.id, the Indonesian local competitor, offers QRIS, VA and Indomaret ([source](https://ghost.bitscale.ai/lynkid)), which Linktree does not.

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Canva | canva.com | Creator / design SaaS (AU) | Global, 40 localised markets | Stripe "benchmark partner"; India e-mandate recurring; Korea domestic acquiring via KakaoPay/Naver Pay; plans multi-gateway routing | https://stripe.com/cn/customers/canva |
| Patreon | patreon.com | Creator memberships | 200+ countries | Adyen, started as backup processor; routing gave +1.89% auth | https://www.adyen.com/knowledge-hub/how-patreon-powers-payments-for-fans |
| Kajabi | kajabi.com | Creator courses | Global | Kajabi Payments on Stripe, region-limited | https://stripe.com/nz/customers/kajabi |
| Hotmart | hotmart.com | Creator digital products (BR) | LATAM | Pix Automático via EBANX (+32pp retention). Also a Yuno customer (nameable) | https://business.ebanx.com/en/press-room/press-releases/hotmart-sees-a-32-percentage-point-boost-in-retention-after-launching-recurring-payments-with-pix-via-ebanx |
| Trakteer | trakteer.id | Creator support (ID) | Indonesia | E-wallet-first, avoids cards | https://en.dailysocial.id/post/creator-monetization-platform-tracter |
| Saweria | saweria.co | Creator donations (ID; IDN Media) | Indonesia | Payouts via DANA, GoPay, OVO, LinkAja, QRIS | https://wikipedia.com/wiki/Saweria |

#### 11C. Companies Recently Adopting Payment Orchestration

*"No public case studies found of direct competitors adopting payment orchestration."*

**Adjacent:**
- Patreon's multi-route Adyen setup (single PSP).
- Canva's stated multi-gateway routing plan (no orchestrator named).
- Stripe Orchestration private preview — a competitive threat.

#### 11D. Prospect Scoring

Only Canva has enough verified signals to score meaningfully.

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| Canva — Monthly tx count | — | ⬜ Not researched | — |
| Canva — Multiple PSPs | +3 | ✅ Stripe + KakaoPay/Naver Pay (Korea) | https://stripe.com/cn/customers/canva |
| Canva — 3+ countries | +3 | ✅ 40 localised markets | same |
| Canva — Local rail gap | 0 | ⬜ Not researched | — |
| Canva — Orchestration | 0 | ⬜ Multi-gateway routing *planned*, vendor unknown | same |

*Partial: 6 known points, not comparable to a full score.*

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Canva | Peer (AU) | Global / APAC | Partial (6+) | Run `/research` | Multi-gateway routing plan, India/Korea localisation | ✅ Yes |
| 2 | Envato | Peer (AU) | Global | Not scored | Run `/research` | AU creator marketplace | ✅ Yes (P1) |
| 3 | Culture Amp | AU SaaS | Global | Not scored | Lower | AU subscription SaaS | ✅ Yes |
| 4 | Lynk.id | Direct competitor (ID) | Indonesia | Not scored | Low (size unknown) | Local rails already live | ❌ No — likely too small |
| 5 | Saweria (IDN Media) | Peer (ID) | Indonesia | Not scored | Low | Wallet-first creator payments | ❌ No |

US/LATAM competitors (Beacons, Stan, Patreon, Kajabi, Hotmart) are out of territory and excluded. **No strong in-territory prospect missing from the TAL was found.**

---

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | ~$55.5M (2024) `[ESTIMATE, not confirmed]`. TAL says "~$100M ARR est." (unsourced lead) | https://sacra.com/c/linktree/ (third-party estimate; not disclosed by Linktree) |
| GMV / Gross Transaction Volume | Not disclosed. Creator commerce settles on creators' Stripe accounts | — |
| Average Transaction Value (USD) | List prices: Starter $8 / Pro $15 / Premium $35 monthly; $6 / $12 / $30 per month billed annually | https://linktr.ee/s/pricing |
| Est. Annual Transactions | Not computable from sourced inputs | — |
| **Monthly transaction count** | **⚠️ NOT FOUND — ASSUMED ~150,000–300,000 web billing events/month. [ASSUMPTION — not researched.]** Basis: Sacra's estimated $55.5M ÷ an assumed ~$10 blended price ≈ ~460K paying subscribers, less annual-plan and app-store subscribers (shares unknown). Billing unit: one Chargebee web charge. Excludes creator-commerce sales and app-store billing | See ICP breakdown |
| Active Customers / Users | "70M+ Linkers"; 70K profiles/day; 1.3B monthly profile views | https://linktr.ee/s/about |
| Primary Currency | USD (US Stripe account); 10 other billing currencies on the AU account | `mfe-billing` bundle |
| Top 3 Markets by Revenue | Not disclosed | — |
| Billing channel split (web vs app store) | **Not disclosed.** Both channels confirmed: web (Chargebee / Stripe / Braintree) and Apple/Google in-app purchase | https://linktr.ee/help/en/articles/5434083-upgrade-linktree-plan |
| Funding | $110M at $1.3B valuation (2022-03), Index + Coatue. ~$166–176M total. Nothing since | https://techcrunch.com/?p=2284606 ; https://sacra.com/c/linktree/ |
| Creator take rate | 12% Free / 9% Starter & Pro / 0% Premium, per the pricing-page plan table. Contradicted by the Pro card ("0% fees") — treat as unsettled | https://linktr.ee/s/pricing |

**App-store check (subscription reference §4):**
- Linktree is **web-significant, not app-store-dominated, as far as can be seen**: the web checkout is the primary upgrade path in the help centre and the pricing page.
- The split is unknown, so this is the #2 discovery question.

---

## Overall Research Confidence

**Medium-High.**

**Strong:**
- **Payment stack:** first-hand production source code, cross-checked against help docs, terms and the privacy notice.
- **Entities:** ABR and Companies House.
- **Earn country restrictions:** primary help article.

**Limited:**
- **Traffic** was **supplied** (SimilarWeb Sales Intelligence). It is visitor traffic on one web domain, top-10 shares only, with **no app traffic and no link to paying users**. The country profile therefore says where creators' audiences are, not where subscription revenue is.
- **Volume and revenue:** undisclosed. The monthly transaction count is assumed.
- **Checkout:** behind login, so not walked.
- **Local web pricing:** not tested from APAC IPs.
- **Complaints:** Reddit and app-store reviews not reached.
- **Regulatory gates** (Indonesia, India acquiring): not sourced in this run, so not asserted.

---

## Manual Research Recommendations

> **Area:** Monthly transaction count / paying subscribers (mandatory)
> **Why it matters:** the only signal that can reject the account; the +5 is currently assumed.
> **Suggested manual action:** ask on the first call for the number of paying subscribers, the monthly/annual mix and the web/app split. Check LinkedIn for finance or analytics staff who may quote ARR.

> **Area:** Indonesia and India share of *paying* subscribers
> **Why it matters:** the whole lead insight rests on Indonesia being a payer market, not just an audience market.
> **Suggested manual action:** ask directly. As a proxy, check whether linktr.ee/s/pricing shows IDR from an Indonesian VPN.

> **Area:** Checkout walk-through from ID / IN / MY
> **Why it matters:** confirms the card-only claim at the point of sale and shows which Stripe account initialises.
> **Suggested manual action:** create a free account behind an Indonesian VPN, start a Pro upgrade, record the methods shown and the `pk_live` key in network requests.

> **Area:** Indonesia / India acquiring regulation
> **Why it matters:** escalates "cross-border inefficiency" to "regulatory gate" if it holds.
> **Suggested manual action:** source current Bank Indonesia PJP and RBI rules before any email cites them.

> **Area:** Payments ownership
> **Why it matters:** in-house motion — the buyer is whoever owns the Payment Localization roadmap.
> **Suggested manual action:** on LinkedIn, find the Growth/Payments engineering manager and the PM who hired the Payment Localization role (SF/LA); also try Olly Hoffman (ex-Klarna, via Fingertip).

---

## Appendix: All Source URLs

**Section 1:** `accounts/traffic/linktree.md` (SimilarWeb, supplied 2026-10-19)

**Section 2:**
- https://abr.business.gov.au/ABN/View?abn=68608721562
- https://abr.business.gov.au/Search/ResultsActive?SearchText=linktree
- https://find-and-update.company-information.service.gov.uk/company/15882736
- https://linktr.ee/s/terms
- https://linktr.ee/s/privacy
- https://linktr.ee/s/about

**Section 3:**
- `https://assets.production.linktr.ee/mfe-billing/` (chunk `static/js/async/537.118901.js`)
- https://linktr.ee/help/en/articles/5434083-upgrade-linktree-plan
- https://linktr.ee/help/en/articles/10518645-guide-to-selling-digital-products-on-linktree
- https://linktr.ee/help/en/articles/11410206-understanding-transaction-and-processing-fees-on-linktree
- https://techcrunch.com/2021/08/24/linktree-partners-with-paypal-to-allow-users-globally-to-accept-direct-payments/
- https://squareup.com/help/gb/article/7430
- https://docs.stripe.com/payments/orchestration/feature-support

**Section 4:**
- https://linktr.ee/help/en/articles/11126119-earn-feature-requirements-limits
- https://linktr.ee/help/en/articles/5434080-how-do-i-change-or-remove-my-payment-method
- https://apps.apple.com/id/app/linktree-link-in-bio-creator/id1593515263
- https://apps.apple.com/in/app/linktree-link-in-bio-creator/id1593515263
- https://apps.apple.com/br/app/linktree-link-in-bio-creator/id1593515263
- https://apps.apple.com/us/app/linktree-link-in-bio-creator/id1593515263
- https://www.marketing-interactive.com/bi-unveils-cross-border-expansion-and-merchant-growth-plans-for-qris
- https://startuptalky.com/india-upi-transactions-august-2026-record-volume/

**Section 5:**
- https://www.trustpilot.com/review/linktr.ee
- https://www.trustpilot.com/review/linktr.ee?page=9
- https://au.trustpilot.com/review/linktr.ee?page=10
- https://linktr.ee/help/en/articles/5434082-why-payment-failed
- https://linktr.ee/help/en/articles/10597023-1-charge-after-subscribing

**Section 6:**
- https://www.builtinchicago.org/job/senior-software-engineer-growth-payment-localization/8879102
- https://www.builtinboston.com/job/senior-software-engineer-earn/11452448
- https://jobs.airtree.vc/companies/linktree-2/jobs/43493734-staff-product-manager-payments
- https://builtinlondon.uk/job/senior-software-engineer-growth-payments/11465744
- https://alternativeto.net/news/2025/12/bento-to-shut-down-in-2026-as-linktree-takes-over-and-offers-migration-path/
- https://www.smartcompany.com.au/startupsmart/linktree-acquires-leibovich-brothers-backed-fingertip-to-shut-it-down/
- https://techcrunch.com/2025/04/23/linktree-rolls-out-a-suite-of-monetization-features-for-creators/
- https://itwire.com/it-people-news/people-moves/linktree-appoints-new-cpo,-two-technologists-to-lead-machine-learning,-ai-and-personalisation
- https://mumbrella.com.au/linktree-taps-atlassian-for-new-cto-706479

**Section 7:**
- https://techcrunch.com/2025/08/18/linktree-goes-dark-in-india-and-the-company-isnt-sure-why/
- https://www.tubefilter.com/2023/12/14/linktree-link-in-bio-acquires-koji/
- https://thepaypers.com/payments-general/linktree-introduces-3-new-monetisation-features--1260118

**Section 8:** https://linktr.ee/s/pricing

**Section 9:** https://linktr.ee/s/privacy

**Section 11:**
- https://help.beacons.ai/en/articles/4700481
- https://www.cbinsights.com/investor/beacons
- https://cartmango.com/stan-store-pricing/
- https://ghost.bitscale.ai/lynkid
- https://o-mega.ai/tools/lnk-bio
- https://blog.biosites.com/blog/easily-accept-payments-online-connect-stripe-or-paypal-to-your-bio-site
- https://stripe.com/cn/customers/canva
- https://www.adyen.com/knowledge-hub/how-patreon-powers-payments-for-fans
- https://stripe.com/nz/customers/kajabi
- https://business.ebanx.com/en/press-room/press-releases/hotmart-sees-a-32-percentage-point-boost-in-retention-after-launching-recurring-payments-with-pix-via-ebanx
- https://en.dailysocial.id/post/creator-monetization-platform-tracter
- https://wikipedia.com/wiki/Saweria

**Section 12:**
- https://sacra.com/c/linktree/
- https://techcrunch.com/?p=2284606

</details>
