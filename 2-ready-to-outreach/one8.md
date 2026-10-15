# One8

**Status:** 🟡 Research complete — **partial run, see the scoring note** · outreach not yet generated
**ICP Score:** 7 / 29 → 🔴 **Low — but PROVISIONAL: 13 of the 29 points could not be assessed.** Read the scoring note before acting on this.
**Industry:** Performance sportswear — footwear, apparel and gear, D2C on Shopify · **HQ:** **Agilitas Brands Private Limited**, WeWork Roshni Arcade, EPIP Zone, Marathahalli, Bengaluru 560037, India · **Researched:** 2026-10-15 · **First email sent:** —
**Motion:** **IN-HOUSE** — they built a client-side geo-router. Verified verbatim from their live theme, not inferred.

---

> ## 🎯 THE HOOK — they ship to 50 countries and price every one of them in rupees
>
> Verified by me from `https://one8.com/meta.json` (HTTP 200, 507 B, against a clean **0-byte 404** control on a nonsense `.json` path):
>
> - **`ships_to_countries` = 50** — AE, AT, AU, BD, BE, BG, BH, CA, CY, CZ, DE, DK, EE, EG, ES, FI, GB, GR, HK, HR, HU, ID, IE, IN, IT, JP, KW, LK, LT, LU, LV, MY, NG, NL, NP, NZ, OM, PH, PL, PT, QA, RO, SA, SE, SG, SI, SK, TH, US, ZA
> - **13 of those are APAC territory** — AU, BD, HK, ID, IN, JP, LK, MY, NP, NZ, PH, SG, TH
> - **`currency` = INR**, `country` = IN, `shopify_pay_enabled_card_brands` = **`[]`**, `offers_shop_pay_installments` = **false**
>
> And on the live checkout, **every payment method carries `availablePresentmentCurrencies: ["INR"]`.**
>
> **A shopper in Singapore, Sydney or Tokyo is quoted in rupees and acquired through an Indian acquirer.** That is the
> cross-border approval-rate and local-method gap in its textbook form — and it is their own configuration, not an inference.

> ## 🔀 THE MOTION — they already built a payment router. It is CSS.
>
> Verbatim from the live theme on `one8.com`, including their own comments:
>
> ```js
> const getCountry = await fetch("/browsing_context_suggestions.json");
> const res = response?.detected_values?.country_name;
> switch(res){
>   case "India":
>     //Enter Selector to disable Shopify and Third Part Button
>     css = ".shopifycheckoutbtn{display:none !important;}";
>     break;
>   default:
>     //Enter Gokwik Selector | Dont change it if it is same.
>     css = ".gokwik-checkout{ display : none !important;} #gokwik-buy-now{ display : none !important;} .shopifycheckoutbtn{display:block !important;}";
>     break;
> }
> ```
>
> **India → GoKwik checkout, Shopify button hidden. Everyone else → GoKwik hidden, native Shopify checkout.**
>
> This is geography-keyed **button hiding**, not transaction routing. There is no retry, no cascade, no failover, and one
> acquirer per path. It breaks if JS is slow, if the country guess is wrong, or if a VPN is in play. **The vendor's own
> placeholder comment — *"Dont change it if it is same"* — is still in production.**
>
> **This is the warmest possible opening short of a live RFP:** the conversation is *"you already route — route properly"*,
> not *"you should consider routing."* ⛔ But the motion is **in-house**: respect the build, anchor on opportunity cost
> and reach, and **never say they need orchestration.**

> ## ⚠️ SCORING NOTE — read before quoting 7/29 to anyone
>
> **This was a deliberately reduced run.** After establishing first-hand that the store is ~4.5 months old and INR-only, I
> cut three of the five agents (complaints, competitors, news/jobs) rather than spend them before knowing whether there was
> volume to orchestrate. **No SimilarWeb data was supplied and none exists third-party.**
>
> **Consequence: 13 of the 29 points are unassessed, not failed.**
> - **8 points** cannot be evaluated without traffic data — 3+ countries (3), local rail gap in a top-3 market (3), traffic
>   outside home (2). With no traffic, there are no "top-3 markets" to test against.
> - **5 points** were not researched — payment complaints (2), competitor orchestration (2), payment job postings (1).
>
> **The account scored 7 of the ~16 points that could actually be assessed.** The 🔴 is arithmetic, not a verdict.
> Supplying a SimilarWeb pull would be the single highest-value action and could plausibly move this to 🟢.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** One8 is Virat Kohli's sportswear brand. **Kohli sold the brand to Agilitas Sports in December 2025**, invested
₹40 cr alongside, and is now positioned as co-founder rather than endorser. **The PUMA licensing arrangement has ended.**
One8 relaunched as an independent Agilitas-owned performance brand in June/July 2026, and `one8.com` is the new D2C channel
stood up for that relaunch.

**SimilarWeb total visits: NO DATA.** None supplied, and no third-party estimate exists for `one8.com`. **The country
profile is unverified**, which suppresses three ICP rows.

### Markets
**No traffic data**, so no ranked market table can be produced honestly. What *is* established: **sells into 50 countries,
prices all of them in INR, holds one legal entity (India).**

### Legal entities
- **Agilitas Brands Private Limited** — CIN `U32300KA2024PTC191432`, incorporated **29 Jul 2024**, ROC Bangalore.
  **Paid-up capital ₹5,00,000 (~USD 5,600). No financials filed.** Named as site owner in their own privacy policy.
- Parent: **Agilitas Sports Private Limited**, CIN `U32300KA2023PTC170821`.
- ⚠️ **Which entity holds the gateway MID is unresolved** — a ₹5-lakh vehicle is an odd merchant of record.
- **No entity outside India.**

### Known payment stack
- **Razorpay** — ✅ CONFIRMED on the live checkout, two gateway entries: `"Cards Onsite by 1Razorpay"` and
  `"Razorpay Secure (UPI, Card, Int'l Card, Apple Pay)"` `[Checkout]`
- **GoKwik** (KwikPass + KwikCheckout) — ✅ CONFIRMED live, `environment:"production"`, India path only `[Source Code]`
- **Snapmint** — ✅ CONFIRMED, white-labelled as **"one8 Pay Later"**, no-cost EMI `[Source Code]`
- **Shopify Payments — NOT in use** (`shopify_pay_enabled_card_brands: []`)

### Orchestration status
**In-house client-side geo-router** over GoKwik (India) and Razorpay (rest of world). Rests on **presence** — the code is
quoted above. **No commercial orchestrator**: Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails and Yuno all
return zero across control, cart, product page and live checkout.

### Buying signals
- 💰 **₹225 cr (US$23.51M) raised 3 Jun 2026** — ₹200 cr follow-on from **Nexus Venture Partners**, ₹25 cr from
  **Rainmatter (Zerodha)**; Anushka Sharma participated. Stated use: manufacturing, retail, **brand building**.
- 🚀 **Brand relaunched Jun/Jul 2026** after the Agilitas acquisition; drops via **Myntra** (180 SKUs, 18 Aug 2026),
  **District/Zomato**, **Blinkit** (1,000 pairs, Bengaluru, 8–9 Oct 2026).
- 🌏 **US, UK, Australia and Canada named as early growth markets**; distribution partnerships reportedly being finalised
  in UK, South Africa and US.
- 🏪 **Sportsyard** retail: first Bengaluru store profitable in 2 months, 10 more planned this FY.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach One8` to draft the 12-touch sequence.*

⚠️ **Four constraints before drafting:**
- **Motion is IN-HOUSE.** They built a router. Anchor on opportunity cost and reach — never "you need orchestration."
- **Do not assume GMV.** The store is ~4.5 months old and volume is genuinely unknown. Lead with the **cross-border
  architecture** and the brand's international ceiling, not with assumed scale.
- **Myntra, Blinkit and District volume is NOT theirs** — those platforms are merchant of record. Only `one8.com` is
  orchestratable.
- **COD is unresolved on the India path** — do not assert its presence or absence.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 7 / 29 (13 points unassessed)

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **2** | ⚠️ **NOT FOUND — no sourced or derivable figure exists.** See disclosure below. Assumption-driven, so it **cannot reject**; scored at the lowest non-reject band. |
| Orchestration status | **1** | ✅ **In-house** — client-side geo-router verified verbatim from live theme; GoKwik + Razorpay beneath it |
| 3+ countries | **0** | ⬜ **UNASSESSABLE.** Rule requires 3+ countries at >1% *traffic share* or 3+ *legal entities*. No traffic data exists; only one entity. **Ships to 50 countries, which is commercially the whole story but meets neither leg of this row as written.** |
| Multiple PSPs | **0** | ⬜ **One confirmed PSP (Razorpay).** The two gateway entries are one provider. GoKwik is a checkout platform whose underlying acquirer is **unobserved**. Would move to 3 if the India path reveals a second acquirer. |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **UNASSESSABLE** — no traffic data, so no top-3 markets to test. The INR-only-across-50-countries finding is a *cross-border* gap, not this row. |
| Recent expansion | **2** | ✅ Brand relaunch Jun/Jul 2026; Myntra, District and Blinkit drops; four named export markets |
| Payment issues | **0** | ⬜ **NOT RESEARCHED** — complaints agent cut. This is a gap, not a negative finding. |
| Funding >$10M | **2** | ✅ **₹225 cr / US$23.51M, 3 Jun 2026**, Nexus + Rainmatter. Into parent Agilitas Sports, explicitly for brand building, with One8 as the flagship relaunch. |
| High traffic outside home | **0** | ⬜ **UNASSESSABLE** — no traffic data |
| Competitor using orchestration | **0** | ⬜ **NOT RESEARCHED** — competitor agent cut |
| Payment job postings | **0** | ⬜ **NOT RESEARCHED** |

**Tier: 🔴 Low on the arithmetic — provisional.** No analyst override applied in either direction: overriding up would
inflate an account whose volume is genuinely unknown, and overriding down would double-count the same uncertainty.
**The correct action is to complete the run, not to re-tier it.**

### Monthly transaction count — MANDATORY DISCLOSURE

⚠️ **NOT FOUND. No sourced figure, and no sound derivation is possible.** `[ASSUMPTION — not researched to a number.]`

Everything searched: MCA/registry financials for the operating entity, Agilitas group revenue, published order or unit
counts, launch-press scale claims, funding-round metrics, Myntra and Blinkit drop outcomes. **Agilitas Brands Pvt Ltd has
filed no financials at all** — incorporated Jul 2024, FY2024-25 was its first year, and the registry shows financials "NA".

**Directional indicators, all qualitative — none is a measurement:**
- Store ~4.5 months old; 250 products; median basket **₹3,299**.
- Agilitas **group** revenue ~₹1,400 cr FY26, of which ~₹1,350 cr is the **Mochiko Shoes** contract-manufacturing arm —
  leaving ~₹50 cr derived for all brands and retail combined. **One8's FY26 contribution is ₹0 by construction** (it
  debuted in FY27).
- Company guidance: **e-commerce is 25–30% of overall business — and that figure bundles marketplaces *with* D2C.**
  `one8.com`'s own checkout is a subset of a subset.
- The flagship Blinkit drop was **1,000 pairs**. The full 180-SKU collection was pushed through **Myntra**, not held on own site.
- A drop-based "access commerce" model (Shopify **Locksmith** access-gating is live) concentrates demand into short
  windows rather than producing steady monthly order flow.

⛔ **Two viral figures rejected as evidence:** "1.5 lakh pairs / ₹138 cr day one" (single promotional source; its ₹9,230
price point contradicts the actual catalogue range of ₹999–13,999) and "3.4 lakh pairs in 48 hours" (a Snapchat topic
page). **Neither has a primary source. Do not carry them.**

**Billing unit counted: individual D2C orders on `one8.com`.** Marketplace orders are excluded because One8 is not
merchant of record there.

### Source Notes
- ✅ **50 ship-to countries, INR-only** — `meta.json`, verified by me against a 0-byte 404 control
- ✅ **The geo-router** — quoted verbatim from the live theme
- ✅ **Razorpay** — from the live Shopify checkout `paymentGateways` object
- ✅ **GoKwik + Snapmint live** — named hosts and SDK init in page source
- ✅ **Operating entity** — from their own privacy policy, verbatim
- ✅ **PUMA relationship ended; brand sold to Agilitas Dec 2025** — Outlook Business, fetched
- ⚠️ **CIN rests on one aggregator**, not verified against mca.gov.in
- ⚠️ **COD unresolved** on the India path
- ⚠️ **No traffic data of any kind**

---

## Section 1: Website Traffic Analysis by Country

**Data source: NONE.** No SimilarWeb data was supplied, and both permitted searches for a third-party estimate returned
nothing for `one8.com`. **No country split is presented, because inventing one is worse than having none.**

⚠️ Searches surfaced confusable domains — `one88.social`, `one88.casino`, `o8.business`. **All unrelated. Do not let
these contaminate any future pull.**

**What stands in place of traffic, and is better evidenced:** `meta.json` gives **50 ship-to countries** with **13 in APAC
territory**, all priced in INR. That establishes market *reach* but says nothing about market *mix*.

**Consequence, stated plainly: three ICP rows (worth 8 points) cannot be evaluated, and the APM gap analysis cannot be
anchored to top-3 markets.** A SimilarWeb pull is the single highest-value missing input.

## Section 2: Legal Entities & Local Presence

**Headquarters:** Bengaluru, India.

| Country | Entity | Reg # | Source |
|---|---|---|---|
| 🇮🇳 India | **Agilitas Brands Private Limited** — named site owner | `U32300KA2024PTC191432` | one8.com privacy policy (fetched, verbatim) + registry aggregator |
| 🇮🇳 India | **Agilitas Sports Private Limited** — funded parent | `U32300KA2023PTC170821` | registry aggregator `[UNVERIFIED]` |
| 🇮🇳 India | *Truepalate Hospitality Pvt Ltd* — operates One8 Commune | not found | restaurantindia.in `[UNVERIFIED]` |

Verbatim from their own privacy policy:
> *"The owner of this website, **Agilitas Brands Private Limited** is a company registered under the Companies Act, 2013,
> having its registered office at WeWork, Roshni Arcade, EPIP Zone, Marathahalli Mn Rd, Marathahalli Colony, Bangalore
> North, Bangalore- 560037, Karnataka, India, hereinafter referred to as 'one8' or 'the Company'."*

**Cross-Border Gap Analysis**

| | Finding |
|---|---|
| Legal entities outside India | **ZERO** |
| Markets sold into | **50**, incl. 13 APAC |
| Presentment currency | **INR only, everywhere** |

> **Warning: cross-border operation across 49 of 50 markets.** Every non-Indian order is priced in rupees and acquired
> through an Indian acquirer — higher scheme costs, lower issuer approval, and FX borne by the shopper. **This is their
> own `meta.json` and checkout configuration, not an inference.**

⚠️ **Deliberately NOT asserted:** whether any of those 50 markets regulatorily gates domestic acquiring behind local
presence. Not sourced, so not claimed.

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Market | Provider | Role | Evidence | Source |
|---|---|---|---|---|
| Rest of world (49) | **Razorpay** | `"Cards Onsite by 1Razorpay"` — Visa, MC, Amex, Diners, Maestro, **RuPay** | `[Checkout]` | live `/checkouts/cn/<token>` |
| Rest of world (49) | **Razorpay** | `"Razorpay Secure (UPI, Card, Int'l Card, Apple Pay)"` — offsite redirect | `[Checkout]` | same |
| 🇮🇳 India | **GoKwik** (KwikPass + KwikCheckout) | Checkout platform, `environment:"production"` | `[Source Code]` | `pdp.gokwik.co`, `gkx.gokwik.co`, `api.gokwik.co` |
| 🇮🇳 India + global | **Snapmint** — *"one8 Pay Later"* | BNPL / no-cost EMI | `[Source Code]` | `static.snapmint.in` |
| — | **Shopify Payments** | **NOT in use** | `[Source Code]` | `shopify_pay_enabled_card_brands: []` |

**Snapmint terms, verbatim from config:** 3-month plan — 25% down payment, **₹199–₹100,000**, `no_cost_emi: true`;
6-month plan — 25% down, **₹5,000–₹500,000**, `no_cost_emi: true`. Branded `brand_name: 'one8 Pay Later'`.
**Commercially important: the 6-month floor of ₹5,000 sits above the ₹3,299 median basket**, so most orders qualify only
for the 3-month plan.

**Only four payment-related third-party hosts exist across the entire storefront** — three GoKwik, one Snapmint.
No Razorpay host on the storefront, consistent with it loading only at checkout.

### 3B. Payment Orchestrator

**Classification: In-house (client-side geo-router), over a regional checkout platform (GoKwik) and a single PSP (Razorpay).**
Rests on **presence** — the routing code is quoted at the top of this file.

> *"Confirmed orchestration-aware."* They have already concluded they need routing and built it. The gap is that it routes
> **buttons by geography**, not **transactions by performance**: no retry, no cascade, no failover, one acquirer per path.

**No commercial orchestrator detected** — Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno: zero across
control, cart, product page and live checkout. That leg rests on **absence**, though with full checkout access the absence
is better evidenced here than on most accounts.

## Section 4: Alternative & Local Payment Methods

| Method | Status | Evidence |
|---|---|---|
| **UPI** | ✅ **CONFIRMED** | `"upi"` in Razorpay Secure `paymentBrands`; gateway name `"Razorpay Secure (UPI, …)"` |
| Cards — Visa, MC, Amex, Diners, Maestro | ✅ CONFIRMED | onsite brands array |
| **RuPay** | ✅ CONFIRMED | `"RUPAY"` onsite, `"rupay"` offsite |
| Net banking | ✅ CONFIRMED | `"netbanking"` in offsite brands |
| Wallets — Paytm, Amazon Pay, Mobikwik, Freecharge, PayZapp, Airtel Money, Ola Money | ⚠️ **Declared, not confirmed-enabled** | present in the Razorpay app's declared brand list, which is **not** the same as being toggled on in the merchant's dashboard |
| **No-cost EMI — Snapmint** | ✅ CONFIRMED, configured | see 3A |
| Apple Pay | ⚠️ In the gateway **name** only | no separate wallet entry observed |
| **COD (cash on delivery)** | ❌ **NOT FOUND on observable surfaces — but UNRESOLVED for India** | see below |
| PhonePe · Simpl · LazyPay | ❌ NOT FOUND | zero hits |
| UPI Autopay / subscriptions | ❌ NOT FOUND | one-time apparel purchase only |

> ### ⚠️ COD is the highest-value open question on this account
> `cash[ _-]?on[ _-]?delivery` returns **0** on the control, cart, product page and decoded live checkout. The only two
> methods on that checkout are the two Razorpay ones.
> **But India traffic never reaches the checkout we could observe** — it is routed to GoKwik, whose Shopify app is
> literally named **"Kwik COD & Checkout"** and is marketed on COD blocking, COD fees, partial COD, prepaid discounts and
> RTO reduction. **COD's presence is NOT being inferred from a product name.** For an Indian D2C apparel brand this
> changes the entire payment conversation, and it needs India-egress observation to answer.

**Local-currency pricing: NONE.** `availablePresentmentCurrencies: ["INR"]` on every method, across all 50 markets.

## Section 5: Payment Issues & Customer Complaints

**NOT RESEARCHED.** The complaints agent was cut from this run. **This is an explicit gap, not a finding of "no
complaints."** Do not read the blank as a clean bill of health.

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | **9 Dec 2025** | **Kohli SELLS One8 to Agilitas Sports**, invests ₹40 cr, signs exclusivity barring other sportswear endorsements. *"Kohli's long-running Puma contract has expired."* | M&A | Outlook Business (fetched) |
| 2 | **3 Jun 2026** | **₹225 cr / US$23.51M** — Nexus Venture Partners ₹200 cr + Rainmatter ₹25 cr; Anushka Sharma participated | Funding | Apparel Resources (fetched) |
| 3 | **21 Jun / 3 Jul 2026** | One8 unveiled and formally debuts as an independent Agilitas brand; Kohli as **co-founder**; US/UK/AU/CA named early growth markets; >1.6M Instagram | Market Expansion | Entrepreneur India (fetched) |
| 4 | **18 Aug 2026** | **Myntra** 18-hour, 180-SKU drop — on Myntra **and** one8.com | Market Expansion | Tribune India |
| 5 | **8–9 Oct 2026** | **Blinkit** quick-commerce drop, **1,000 pairs**, Bengaluru | Market Expansion | mediainfoline `[UNVERIFIED]` |

**No public payment RFP found.** **No payment job postings researched** — agent cut.

**Notable:** Agilitas founder **Abhishek Ganguly is the former Managing Director of PUMA India**, and Agilitas's own
Sportsyard retail format **still stocks PUMA** alongside Nike, Adidas and others. They retail PUMA while competing with it.

## Section 7: Payment-Specific News

**No payment-specific news found.** The vendor stack was established from live assets rather than announcements — there
are no public Razorpay, GoKwik or Snapmint announcements naming One8.

## Section 8: Checkout Experience Audit

| Dimension | Finding | Quality |
|---|---|---|
| Checkout type | **Two surfaces.** Rest of world: Shopify-hosted (`/checkouts/cn/<token>`, `powered-by: Shopify`). India: **GoKwik**, unobserved. | Fair |
| Card input | Shopify app gateway, `"checkoutHostedFields": null` — One8 never touches card data on the observed path | Good |
| Payment methods visible | Two Razorpay methods on the observed path | Fair |
| Location-based display | ✅ **Yes — but via client-side CSS button-hiding**, keyed to a Shopify geolocation guess | **Poor** |
| Instalments | Snapmint "one8 Pay Later", 3mo and 6mo no-cost EMI | Good |
| Multi-currency | ❌ **INR only across 50 markets** | **Poor** |
| 3DS | Not observed | — |
| Identity | GoKwik **KwikPass** phone/OTP login accelerator (India) | — |
| Access gating | Shopify **Locksmith** present — consistent with the ticketed-drop model | — |

**The India checkout could not be walked** — their geo-router serves it only to India-detected traffic, and our egress
resolves as United States.

## Section 9: PCI DSS Compliance

**No published PCI attestation found for One8.**

> `[INFERENCE, not confirmed]`: the observed checkout **is** Shopify-hosted with card entry via a Shopify app gateway and
> `checkoutHostedFields: null`, so PCI scope most likely sits with Shopify and Razorpay, leaving One8 at SAQ-A / SAQ-A-EP.
> **The GoKwik India path is a separate checkout surface and its PCI posture is unknown** — a merchant running two distinct
> checkout surfaces plausibly has two different scope answers.

## Section 10: Strategic Insights & Outreach Angles

> ### Insight #1 — Fifty countries, one currency, one acquirer.
> **Evidence:** S2 (`ships_to_countries` = 50, zero entities outside India) + S3/S4 (`availablePresentmentCurrencies:
> ["INR"]` on every method; Razorpay sole PSP on that path).
> **Pain:** every non-Indian shopper is quoted in rupees and acquired cross-border into India — depressed issuer approval,
> scheme cross-border fees, and FX friction visible to the customer at the worst moment.
> **Yuno value:** local presentment and local acquiring per market through one integration, without an entity per market.
> **Outreach angle:** they ship to Singapore, Australia and Japan and price all three in rupees.
> **Subject:** `Rupee pricing in 13 Asian markets`

> ### Insight #2 — They already wrote a payment router. In CSS.
> **Evidence:** S3B (the verbatim `switch(res){case "India":…}` geo-router, with the vendor's placeholder comment still in
> production) + S3A (GoKwik on one path, Razorpay on the other, no cascade).
> **Pain:** routing by `display:none` fails open — slow JS, a wrong country guess or a VPN puts the shopper on the wrong
> checkout entirely. And it routes by geography only: no retry, no failover, no second acquirer anywhere.
> **Yuno value:** server-side routing with real failover, replacing a client-side guess.
> **Outreach angle:** quote their own comment back, gently. They've already decided they need routing.
> **Subject:** `Your checkout router runs on display:none`

> ### Insight #3 — Two checkouts, two different payment estates.
> **Evidence:** S8 (Shopify-hosted for 49 markets, GoKwik for India) + S9 (PCI scope differs across the two surfaces).
> **Pain:** two checkouts means two method sets, two reconciliations, two PCI answers and two vendor relationships — for
> one brand at ~4.5 months old. That divergence compounds with every market they add.
> **Yuno value:** one integration spanning both, so adding a market is configuration, not a second stack.
> **Subject:** `Two checkouts, one brand`

### Quick Hits

**Email hooks:**
1. Your store ships to 50 countries and quotes every one of them in rupees.
2. Your checkout router is a `switch` on country name that hides buttons with `display:none` — the vendor's placeholder comment is still in it.
3. Thirteen of your ship-to markets are in Asia-Pacific, and all thirteen settle through an Indian acquirer.

**Cold call openers:**
1. "You ship to Singapore, Australia and Japan — are those priced in rupees deliberately, or is that a Shopify Markets default?"
2. "You route India to one checkout and everyone else to another. What happens when the country detection gets it wrong?"
3. "You've got Snapmint branded as one8 Pay Later, but the six-month plan starts at ₹5,000 and your median basket is ₹3,299 — how's that converting?"

## Section 11: Similar Companies & Prospecting Pipeline

**NOT RESEARCHED** — the competitor agent was cut from this run. No competitor payment stacks were gathered and no
orchestration-adoption evidence was sought.

**Adjacent find worth noting:** **Agilitas Sports** is itself a larger entity than One8 — ~₹1,400 cr group revenue FY26,
guiding ₹1,800–1,900 cr, with the **Mochiko Shoes** manufacturing arm, the **Sportsyard** multi-brand retail chain, and
₹225 cr freshly raised. **Agilitas is not on the TAL.** If the One8 D2C volume proves too small, **the parent may be the
better-sized account** — Sportsyard retail alone is planning 10 new stores this FY.

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|---|---|---|
| Annual revenue (one8.com) | **No public information found** | Agilitas Brands has filed no financials |
| Parent group revenue | ~**₹1,400 cr** FY26; guidance ₹1,800–1,900 cr | company statements `[UNVERIFIED — summary only]` |
| GMV / GTV | **No public information found** | — |
| Average transaction value | **Median variant price ₹3,299** (range ₹999–13,999) | **my own pull** of `/products.json` — 250 products, 1,409 variants |
| **Monthly transaction count** | ⚠️ **NOT FOUND — no sourced or derivable figure** | See the mandatory disclosure above. **Billing unit: individual D2C orders on one8.com.** |
| Catalogue | 250 products / 1,409 variants, all published **Jun–Oct 2026** | my own pull |
| Primary currency | **INR, and only INR, across 50 markets** | `meta.json` + live checkout |
| Channels where One8 is merchant of record | **`one8.com` only.** Myntra, Blinkit and District are merchant of record on their own platforms | agent findings + Tribune India |
| Billing channel split | N/A — D2C e-commerce, not app-store billing | — |

## Overall Research Confidence

**MEDIUM-LOW, and the cause is twofold.**

1. **No traffic data of any kind** — none supplied, none third-party. Three ICP rows unevaluable and no market mix.
2. **A deliberately reduced run** — three of five agents cut after the store's age and single-currency setup emerged.

**Where confidence is genuinely HIGH:** the payment stack. Razorpay, GoKwik, Snapmint, the geo-router, the 50-country
ship-to list and the INR-only presentment were all read off live first-party assets with controls, and I verified the two
decisive ones personally. **This is better checkout evidence than most accounts in this repo** — we reached the live
Shopify checkout object.

**Where it is LOW:** volume, the India checkout, COD, complaints, competitors, hiring.

## Manual Research Recommendations

> **Area: SimilarWeb traffic.** **Why:** unlocks 8 ICP points and the entire market-mix analysis; the account is currently
> under-scored for want of it. **Action:** pull `one8.com` with all-country-domains ON. ⚠️ Beware `one88.social` /
> `one88.casino` — unrelated.

> **Area: The India checkout.** **Why:** that is where effectively all their volume goes, and we have never seen it.
> **Action:** load `one8.com` from an India IP and walk the GoKwik checkout — method set, COD terms, COD fees, prepaid
> discounts, and which PSP sits behind GoKwik.

> **Area: COD.** **Why:** for an Indian D2C apparel brand it reshapes the whole payment conversation (RTO risk, prepaid
> conversion). **Action:** downstream of the above.

> **Area: Monthly order volume.** **Why:** the only signal that can reject, currently unknown in both directions.
> **Action:** ask in discovery. No public source exists.

> **Area: Agilitas Sports as a separate account.** **Why:** ~₹1,400 cr group, ₹225 cr raised, Sportsyard retail scaling,
> **not on the TAL**. **Action:** consider stubbing it into `1-to-outreach/`.

</details>
