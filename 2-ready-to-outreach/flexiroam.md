# Flexiroam

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 16 / 29 → 🟢 **Medium** — ⚠️ **but see the volume warning. This is an analyst-override candidate.**
**Industry:** Telecommunications — travel eSIM / MVNO, brand-partner entitlements, enterprise IoT connectivity · **HQ:** operationally **Malaysia** (Petaling Jaya); legally domiciled Australia (**ASX: FRX**, ABN 27 143 777 397) · **Researched:** 2026-10-06 · **First email sent:** —
**Motion:** 🛑 **IN-HOUSE — they hand-rolled the multi-PSP abstraction Yuno sells.** Server-side vendor selection across Airwallex and Stripe, with per-attempt retry and decline telemetry. **Never say they need orchestration.**

---

> ## 🛑 READ THIS FIRST — the account fails on volume, which is the top ICP criterion
>
> **FY26 audited revenue is A$10,172,890, DOWN 25% from A$13,576,602.** And the segment that payment orchestration actually addresses is smaller still:
>
> | | FY26 | FY25 |
> |---|---|---|
> | Recurring (brand-partner entitlement + contracted B2B) | **56%** ≈ A$5.70m | 39% |
> | **Transactional (= consumer travel checkout)** | **44% ≈ A$4.47m** | 61% |
>
> **The addressable consumer checkout is roughly A$4.5m (~US$3.0m) per year — and it is being deliberately shrunk.** Two reasons, both stated in the Directors' Report:
> 1. *"the Group withdrew from consumer acquisition channels that were not generating positive unit economics"*
> 2. *"the Middle East conflict weighed on airfares, consumer confidence and discretionary international travel"*
>
> And the outlook: *"The Group expects softness in discretionary consumer travel demand to **persist in the near term**."*
>
> **The structural problem: everything Flexiroam is GROWING does not touch a consumer checkout at all.** Brand-partner revenue is *"paid for making the entitlement available rather than for the volume of data consumed"* — an invoiced B2B subscription to Mastercard issuers, Generali, Tune Protect and Dragonpass. B2B Solutions is contracted monthly data-pool subscriptions to Etihad, DIALOG and Paydibs. **Neither generates checkout volume for Flexiroam to orchestrate.**
>
> ### Volume gate — the arithmetic, and why the gate does NOT formally fire
> ```
> Transactional consumer revenue FY26 (SOURCED, audited)   A$4,470,000  ≈ US$2,950,000
> ÷ ASSUMED average travel-eSIM plan price:
>     at US$5   →  590,000 txns/yr  →  49,200/month   ✅ clears
>     at US$10  →  295,000 txns/yr  →  24,600/month   ❌ fails
>     at US$20  →  147,500 txns/yr  →  12,300/month   ❌ fails
> ```
> **The average plan price is ASSUMED — no ARPU, plan-price, subscriber, activation or transaction figure is disclosed in any filing.** Per the rule, **only a SOURCED or soundly-derived sub-40k figure may reject an account, and an assumption never can.** So the gate does **not** formally fire — but the honest read is that this account is **below or barely at the minimum, on a shrinking base.**
>
> **🔑 Recommendation: do not build outreach on this until Prateek decides. Scored 16/29 on the matrix, but the matrix has no row for "the addressable segment is being deliberately wound down." This is an analyst-override call and it is his to make, not mine.**

---

> ## ⛔ THE STUB WAS WRONG ON ALL THREE COUNTS
>
> | Stub says | Truth | Source |
> |---|---|---|
> | HQ Australia | **Operationally MALAYSIA** (Petaling Jaya, Selangor). The Perth address is **c/o Boardwise Corporate Pty Ltd** — a corporate-services provider, not an operating office | FY26 Annual Report, Note 25 |
> | Operating countries MY/AU | Sells in **190+ countries / 600+ carrier partners.** MY/AU/HK is just the *entity* footprint | FY26 results pres. p3 |
> | Revenue ~$15M | **A$10.17m audited, DOWN 25%** | FY26 Appendix 4E |
>
> The Group states it is *"domiciled in Australia"* only because *"the majority of the Company's shareholder base is Australian."* Founder/CEO Jefrey Ong and CFO Grant Wong are Malaysia-based. **Treat Malaysia as the centre of gravity** — consistent with the supplied traffic showing Malaysia as the top market.
>
> **And the traffic premise was right to flag:** Malaysia 21.53%, Mexico 13.90%, US 13.19%, France 9.88%, Canada 9.12%, Kazakhstan 7.44%, **Australia only 6.35%.** The company itself concedes it cannot localise its revenue — FY26 AR revenue note: *"Due to the nature of sales and users of data roaming plans, the Group is **unable to practically and reliably determine the geographical location** relating to the sales."*
>
> **🔑 So the supplied SimilarWeb country mix is the ONLY geographic read available on this account, and it is better evidence than anything Flexiroam files.**
>
> ⚠️ **Also: Flexiroam X / X-ONE is dead.** The microchip-sticker product was **discontinued 1 July 2024** with users migrated to eSIM. **No reference to "Flexiroam X" or "X-ONE" appears anywhere in the FY26 Annual Report or results presentation.** The current platform is branded **flexiroam.ai** (WhatsApp-based AI eSIM agent, commercial launch 17–22 December 2025, 70+ languages).

---

> ## ⭐ THE FINDING — they built the routing layer themselves, and the Terms haven't caught up
>
> From the production Next.js bundles, the backend returns a `payment_intent` carrying `{vendor_name, public_key, client_secret, currency, auto_capture}` and **the client routes on it**:
> ```js
> r = ej.vendor_name ?? "AirWallex";  i = r.trim().toLowerCase();
> payment: { provider: n ? "native" : "airwallex"===i ? "airwallex" : "stripe",
>            isSetup: ej.client_secret.includes("seti_"), autoCapture: !!ej.auto_capture }
> if (!n && "stripe"!==s && "airwallex"!==s) { fail("key_error_payment_failed"); return }
> ```
> **Telemetry confirms it is deliberate, not accidental:** `payment_provider`, `provider_confirm`, `pre_payment`, `decline_code`, `error_stage`, `flow_version`, `attemptId`, `retry` — **all instrumented per attempt.** The server supplies the publishable key per transaction; **no `pk_live_*` appears anywhere in the client bundles.** Backing microservices: `prod-clientservices`, `prod-enduserservices`, `prod-planservices`, **`prod-vendorservices`**`.flexiroam.com`.
>
> **They have hand-rolled exactly the multi-PSP abstraction Yuno sells: two acquirers, server-side vendor selection, per-attempt retry and decline telemetry.**
>
> **🎯 And here is the usable discrepancy.** Their **Terms (clause 5.5, updated 1 September 2026)** say, verbatim:
> > *"We use **Stripe** as our electronic payment gateway. Stripe is an online credit card processor that uses technology to protect your transaction details. Your full credit card details are received and processed by Stripe, **not by us**."*
>
> **But the code defaults to Airwallex in two separate paths** (`vendor_name: C.vendor_name ?? "AirWallex"` and `r = ej.vendor_name ?? "AirWallex"`). **The Terms name Stripe as THE gateway while the code defaults to Airwallex — suggesting Airwallex was added later and the Terms were never updated. That is a recent, possibly still-settling migration, and it is excellent opener material.**
>
> ⚠️ **No external press confirms the Airwallex relationship at all.** It rests entirely on first-party code — which is strong, but single-source.

---

> ## 🎯 THE HOOK — two products, two completely separate payment stacks
>
> Their **WalletRoam** pay-as-you-go product tops up through a **different storefront entirely**: `walletroam.com/pages/top-up-credits` → **Shopify**.
> ```js
> Shopify.shop = "xnamue-08.myshopify.com"   "shopId":96884916542
> shopify-digital-wallet   Shopify.PaymentButton.init()
> "countryCode":"HK"   Shopify.currency = {"active":"USD","rate":"1.0"}
> ```
> **Two checkouts, two stacks, one company** — the eSIM plans on Next.js + Airwallex/Stripe, and WalletRoam credits on Shopify with a **Hong Kong** merchant locale. WalletRoam top-ups even settle via an **emailed redemption code** rather than direct wallet credit.
>
> **And the second asymmetry: they localise language but not currency or payment rails.** Every price renders in **USD** (sampled `flexiroam.com/en-us/shop/esim-singapore`: `USD 0.79 … USD 1.93`); code shows `currency: getCookie("Currency") ?? "USD"` and the payment intent `currency ?? "USD"`; WalletRoam's Shopify store is `active:"USD", rate:"1.0"`.
>
> Yet they ship UI locales for **`ms`, `kk`, `ru`, `pt-br`, `es`, `th`, `vi`, `ja`, `ko`, `zh-cn`, `ar-sa`** — Malay, Kazakh, Russian, Brazilian Portuguese, Spanish, Thai, Vietnamese, Japanese, Korean, Chinese and Arabic.
>
> **They translated the storefront into eleven languages for markets where no single one exceeds 22% of traffic, and gave every one of them a USD card form.** That is an asymmetry inside their own stack, and the strongest kind of observation.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Travel eSIM and connectivity provider, ASX-listed since June 2015, actively trading (~A$0.023–0.025, market cap **~A$35–38m**, ~1.517bn shares; 52-week range A$0.004–0.028, up ~260% over 12 months). **Three channels, two reported segments:**
1. **Consumer travel (D2C)** — eSIMs via flexiroam.com, the app, and a WhatsApp AI agent → *Travel Connectivity*
2. **Brand partner (B2B2C)** — data embedded as a benefit inside banks, insurers and loyalty programmes; **the partner funds the entitlement** → *Travel Connectivity*
3. **Enterprise (B2B)** — multi-network SIM/eSIM for payment terminals, aircraft, IoT → *B2B Solutions*

**SimilarWeb total visits:** 134,190 (Aug 2026) — supplied by Prateek. Malaysia 21.53%, Mexico 13.90%, US 13.19%, France 9.88%, Canada 9.12%, Kazakhstan 7.44%, **Australia 6.35%.**

### ✅ The app-store trap — checked and cleared
**IAP does NOT dominate. Orchestration CAN reach this revenue.** Three independent lines:
1. **The Apple App Store listing has NO "In-App Purchases" section** (`apps.apple.com/app/id1084265472`, seller: Flexiroam Sdn Bhd). **Apple always enumerates IAP items when present.**
2. **Current help-centre article, updated 2026-08-26:** *"You can pay via: - Credit or Debit Card - ApplePay"*
3. **Source code:** the payment intent is built with `isNativePayment:!1` as the default.

⚠️ **Residual risk, and be honest about it in outreach:** there IS a third provider branch called `native`, taken only inside the app's WebView:
```js
n = window.isInWebView ?? !!window.ReactNativeWebView;
let d = n ? "native" : "stripe"===s ? "stripe" : "airwallex"===s ? "airwallex" : "unknown";
```
**What that native layer uses (StoreKit vs a native Airwallex/Stripe SDK) could NOT be determined.** No `RevenueCat`/`StoreKit`/`Play Billing` tokens appear in the bundles, which argues against StoreKit. **The Google Play listing could not be verified — the guessed package id returned 404. This is the one question to ask on a call, not assert.**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

> **🛑 NOT YET GENERATED — and it should not be until Prateek rules on the volume question.** See the warning at the top: the addressable consumer checkout is ~US$3m/yr and is being deliberately wound down as stated strategy.
>
> If it proceeds: **motion is IN-HOUSE.** Per `/full-outreach` Step 6a, respect the build decision and anchor on reach and opportunity cost. **Also note: there is no funding trigger** — no equity raised and no new debt drawn in FY26, by design and loudly advertised. **Do not pitch on one.**

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

## Section 1: Entities — only three, and two the stub implied do not exist

Per the audited **Consolidated Entity Disclosure Statement** at 30 June 2026:

| Entity | Incorporation | Ownership | Registration |
|---|---|---|---|
| **FlexiRoam Limited** (parent, ASX: FRX) | Australia | — | **ABN 27 143 777 397 / ACN 143 777 397** |
| **FlexiRoam Sdn Bhd** | **Malaysia** | 100% | Not disclosed in filings |
| **FlexiRoam Asia Limited** | **Hong Kong** | 100% | Not disclosed in filings |
| ~~Super Bonus Profit Sdn Bhd~~ | Malaysia | **struck off in FY26** | — |

**🛑 There is NO Singapore entity and NO US entity.** This can be stated affirmatively — the CEDS is exhaustive. **The stub's implied footprint does not exist.**

⚠️ **A search summary surfaced "Flexiroam Malaysia Company SSM No 670869-A." It could NOT be tied to FlexiRoam Sdn Bhd and the format looks pre-2016. DO NOT USE IT.**

**Other corporate detail:** Auditor **Horizon Nexus (Qld) Audit Pty Ltd** (Brisbane), unmodified opinion. Banker **National Australia Bank.** Registry Automic. Directors: Jefrey Ong, Wee Keat Chan, Nicholas Ong. Top holders: Citicorp Nominees 37.61%, Mr Thian Choy Ong 10.20%, HSBC Custody Nominees 8.51%.

## Section 2: Financials — a real turnaround on a thin base

| Metric (A$) | FY26 | FY25 | FY24 |
|---|---|---|---|
| Revenue | **10,172,890** | 13,576,602 | — |
| Profit/(loss) after tax | **+658,206** | (1,997,795) | (1.5m) |
| Net operating cash flow | **+2,712,503** | (3,084,467) | — |
| Cash at 30 Jun | **3,543,063** | 1,609,012 | 0.5m |
| Net current assets | **+434,921** | (1,312,511) | (5,356,946) |
| Net assets | 4.1m | 2.5m | (0.5m) |
| Underlying EBITDA (non-IFRS, unaudited) | 2.4m | 0.6m | 1.2m |

**Segment revenue FY26:** Travel Connectivity **9,023,366** (−26%, 88.7%) · B2B Solutions **1,149,524** (−18%, 11.3%).

**The profit came from a cost reset, not growth:** network & platform expenses **−42%** (A$7.26m→A$4.18m), marketing **−63%** (A$1.65m→A$0.60m), employee benefits −30%, D&A −80%.

### Distress assessment: NOT currently distressed — but it was 12 months ago, and it remains thin
**Resolved:** FY26 AR Note 3 (Going Concern): *"The material uncertainty disclosed in the prior year **no longer exists.** The Directors have concluded that the Group is able to pay its debts as and when they fall due."* **FY25 carried a going-concern material uncertainty; FY26 does not.** First statutory NPAT since the 2015 listing; first full year of positive operating cash flow; first positive year-end net current assets since 2017. **No equity raised and no new debt drawn in FY26** — the cash build was self-funded.

**Still thin:** A$3.54m cash against a ~A$35–38m market cap — **one bad half erases the buffer.** Severe recent dilution: the **6 Feb 2025** entitlement offer raised A$3,658,775 by issuing **731,754,813 shares at A$0.005** — roughly doubling the register at half a cent. **The founder is a creditor:** the Group's *only* borrowing at 30 June 2026 is an **unsecured A$0.75m CEO loan at 12% p.a.**, carried at A$0.9m with accrued interest. Revenue still falling 25%, and **management gives no revenue or earnings guidance.**

⚠️ **Get this number right:** several secondary sources and the 31 Jul 2026 Appendix 4C quote FY26 revenue ~A$9.9m and NPAT ~A$0.4m. **Those are the UNAUDITED quarterly figures.** The 4E explains the gap: ~A$0.3m of additional brand-partnership revenue was recognised on finalisation. **Cite the audited A$10.17m / A$0.66m.**

⚠️ **Related-party note worth knowing:** the Group transacted with **Circlepay Technologies Pty Ltd t/a PayPilot**, of which **CFO Grant Wong is a director** — A$25,310 capitalised software development + A$16,130 hosting in FY26. **The CFO has a payments-product side interest.**

## Section 3: PSPs

| PSP | Status | Evidence |
|---|---|---|
| **Airwallex** | ✅ **CONFIRMED — appears to be PRIMARY** | Hosts in bundles: `checkout.airwallex.com`, `static.airwallex.com`, `o11y.airwallex.com/airtracker/{logs,metrics}`. SDK element registry bundled: `hpp, dropIn, card, cardNumber, cardExpiry, cardCvc, applePayButton, googlePayButton, krCardNumber, krCardIdentifier…`. **Default vendor in two separate code paths** |
| **Stripe** | ✅ **CONFIRMED, two evidence types** | `https://js.stripe.com/v3`, `@stripe/react-stripe-js` (`name:"stripe-js"`), `EmbeddedCheckoutProviderContext`, `paymentRequestButton`, `paymentMethodMessaging` — **plus Terms clause 5.5 naming Stripe explicitly** |
| **Shopify** (platform, not PSP) | ✅ CONFIRMED | WalletRoam storefront, HK merchant locale |
| Adyen · Braintree · **PayPal as a live method** · Razorpay · 2C2P · iPay88 · MOLPay/Razer · senangPay · eGHL · Billplz · Xendit · Midtrans · Checkout.com · Worldpay · Cybersource | ❌ **NOT FOUND** | searched code, help centre, legal and press |

### ⚠️ False positives ruled out — both would have been reported as hits
- **`omise` — 453 raw hits, ALL spurious:** `Promise`, `new Promise`, `compromise`, `pes_promise`.
- **`primer` — 16 hits, ALL spurious:** French **`"Supprimer"`** (delete) and Spanish **`"primera"`/`"primeros"`** in i18n strings. **Primer is NOT present.**
- `stripe` also appears in Tailwind classes (`bg-stripe-gradient-*`) — but the `js.stripe.com` / `react-stripe-js` hits are genuine and corroborated by the Terms.
- **`meses` (6 hits)** is Spanish/Portuguese for *months* in plan-validity copy (*"dentro de 3 meses"*) — **NOT `meses sin intereses`. No instalment evidence.**
- **Currency codes MYR/MXN/KZT/BRL/SGD** come from a **generic country-metadata table** (`{name:"Malaysia",phone:[60],capital:"Kuala Lumpur",currency:["MYR"],languages:["ms"]}`) — **NOT a supported-currency list. Do not cite as multi-currency support.**

**BuiltWith refused the domain:** *"We cannot lookup results on this domain sorry."*

## Section 4: Payment methods — the entire list is two items

**Authoritative first-party list (help centre, updated 2026-08-26): Credit/Debit Card + Apple Pay. That is all.** Corroborated by querying their Zendesk help-centre API per method: `fpx: 0`, `duitnow: 0`, `alipay: 0`, `paypal: 0`, `currency: 0`.

| Market | Rail | Status |
|---|---|---|
| 🇲🇾 **Malaysia (21.53%, #1)** | **FPX** | ❌ **NOT FOUND** — 0 code refs, 0 help articles |
| | **DuitNow** | ❌ **NOT FOUND** — 0 code refs, 0 help articles |
| | Touch 'n Go, Boost, GrabPay, ShopeePay | ❌ NOT FOUND |
| 🇲🇽 Mexico (13.90%) | OXXO, SPEI, CoDi, **meses sin intereses** | ❌ NOT FOUND |
| 🇧🇷 Brazil (2.00%) | **Pix**, boleto | ❌ NOT FOUND |
| 🇰🇿 Kazakhstan (7.44%) | **Kaspi.kz** | ❌ NOT FOUND |
| 🇸🇬 Singapore (2.12%) | PayNow | ❌ NOT FOUND |
| 🇦🇺 Australia (6.35%) | PayTo | ❌ NOT FOUND |
| Global | **Cards (Visa/MC/AMEX)** | ✅ **CONFIRMED** |
| Global | **Apple Pay** | ✅ **CONFIRMED** |
| Global | Google Pay | ⚠️ **NOT CONFIRMED** — `googlePayButton` exists only as an *Airwallex SDK element type*, i.e. vendor capability, **not proof Flexiroam enabled it.** Absent from the help-centre list |
| Global | PayPal | ⚠️ **NOT CURRENT.** 0 help articles, 0 code refs. Only a historical joint *marketing* campaign (30% off via PayPal) — **undated, treat as legacy** |
| Greater China | Alipay | 🛑 **UNVERIFIED — DO NOT USE.** A search snippet attributed *"in-app purchases available via Mastercard, Visa, AMEX & Alipay"* to a Flexiroam page, but no live first-party source was reachable, there are **0 help-centre articles for alipay and 0 code refs**, and it is **contradicted by the current help article** |

## Section 5: Orchestrator classification — IN-HOUSE

**Not "none detected" — there is a real routing layer; it is just theirs.** See The Finding for the code. **Third-party orchestrators NOT FOUND:** no Juspay, Spreedly, Primer (false positive ruled out), Gr4vy, Yuno or Corefy. The orchestration search returned only generic vendor-comparison pages with **zero Flexiroam linkage.**

## Section 6: PCI DSS — no published position

- **No PCI DSS statement, AOC or compliance page** on flexiroam.com or in the help centre.
- Nearest thing is **Terms 5.5**: card data is *"received and processed by Stripe, not by us"* → implies **deliberately reduced PCI scope** (hosted-fields / SAQ-A style). The Airwallex path is consistent (hosted elements + `client_secret`).
- ⚠️ **The Privacy Policy names NO payment processor at all and contains ZERO instances of the word "payment"** — it is an Australian-style APP policy focused on recruitment and general data.

## Section 7: Buying signals — an unusually dense 12 months, and three counterparties are payments companies

| Date | Counterparty | What |
|---|---|---|
| Dec 2025 | **Generali Insurance Malaysia Berhad** | Travel-insurance vertical entry, deployed within days of the flexiroam.ai launch |
| **8 Jan 2026** | **DIALOG Group Berhad** via DIV Services Sdn Bhd (Bursa-listed) | Multi-network connectivity for the **mPOS terminals behind Malaysia's MyKasih cashless welfare platform**, expected to serve ~8.1m SARA recipients in 2026. Min. annual commitment ~A$60,000. **LIVE** |
| **18 Mar 2026** | **Paydibs Sdn Bhd** | Connectivity embedded in the **Paydibs NEO all-in-one payment terminal.** Two-year, auto-renewing. **LIVE** |
| 11 May 2026 | **Tune Protect Group Berhad** (Bursa: TUNEPRO, AirAsia's travel insurer) | Data on every eligible Preset policy |
| **14 Jul 2026** | **Unnamed global telecommunications company** | Non-binding MoU for the AI eSIM platform. **Definitive agreement targeted within 90 days of 14 Jul — i.e. ~12 October 2026.** ⚠️ **This is live right now and is the sharpest near-term hook — but see the caveat below** |
| **24 Jul 2026** | **Unnamed established Australian payments group** | Multi-network SIM/eSIM for **payment terminals across Australia.** Commenced 23 Jul 2026, three-year initial term. Management planning-case ARR **A$0.32–0.44m at 31 Dec 2027** (not guidance) |
| **4 Aug 2026** | **Etihad Airways** | Two-year **master agreement** — staff connectivity, aircraft operational data, pilot iPad connectivity, 125+ countries. **No minimum data pools, devices or aggregate contract value.** LIVE |
| **4 Sep 2026** | **Dragonpass** | Two-year; loyalty programme of an unnamed **top-three global hotel group by room count.** First campaign pending |
| Ongoing | **Mastercard** | Embedded data benefit across **418 banks, 1,270 card programmes, 78 countries** at 30 Jun 2026 |

⚠️ **ICP note:** Flexiroam *sells connectivity TO* payment-infrastructure companies (Paydibs, DIALOG/MyKasih, an unnamed Australian payments group). **That is a customer relationship, not a PSP identity. Flexiroam is an MVNO/eSIM provider — in scope, no Partnerships hand-off.** Do not misread it. **But it does make Flexiroam a potential channel INTO payments players, which may be more valuable than the account itself.**

**Leadership:** Founder **Jefrey Ong** returned as Interim CEO **7 December 2024**, confirmed CEO and Executive Director **1 August 2025** — the company frames FY26 as *"21 months from the founder's return."* **CFO Grant Wong appointed 1 October 2025** — **a new CFO 12 months in is the most orthodox commercial entry point, and he signed off the cost reset.**

**🛑 Job postings: NO active openings found at all**, let alone payments roles. Wellfound shows no jobs; Maukerja shows 0 vacancies for Flexiroam Malaysia. Consistent with a company that cut employee benefits 30% and marketing 63%. **No hiring signal.**
**🛑 Public payment RFP: NONE. No M&A** — the only structural change is Super Bonus Profit Sdn Bhd being struck off.

**Disclosed metrics are channel reach, not volume:** 418 banks / 1,270 card programmes / 78 countries · 600+ carrier partners, 190+ countries · 31% fewer human-handled support tickets Jan 2026 vs Nov 2025 · *"over 15,000 users"* on the AI eSIM agent — ⚠️ **`[UNVERIFIED]`, appeared only in a search summary, NOT in any audited filing.**

**Other third parties on site:** Cloudflare Turnstile, MoEngage, Zendesk, Trustpilot, GTM.
**Mastercard co-brand is a distribution channel, not a payment method:** `mastercard.flexiroam.com`, a dedicated `flow:"mastercard_order"` with `redemptionPath:"payment"`, `MastercardEligibilityButton`, `mastercard_journey_id`, `mc-benefit-*` SKUs. A parallel **Westpac** programme exists, plus **Bank AlJazira** and **Latitude 28° Degrees**. **Card-issuer-led acquisition means issuer-side BIN concentration — relevant to approval-rate conversations.**

## Section 8: ICP Score — 16 / 29 → 🟢 Medium

| Signal | Max | Score | Evidence |
|---|---|---|---|
| Transaction volume | 5 | **2** | **A$4.47m/yr addressable consumer checkout (~US$3.0m), DELIBERATELY SHRINKING.** Derived 12,300–49,200 txns/month depending on an ASSUMED plan price — straddles and mostly fails the gate |
| Orchestration posture | 4 | **1** | **In-house** — server-side vendor selection across Airwallex and Stripe with per-attempt retry/decline telemetry |
| Operates 3+ countries | 3 | **3** | **190+ countries, 600+ carrier partners** |
| Multiple PSPs in parallel | 3 | **3** | **Airwallex + Stripe live simultaneously, PLUS a third stack (Shopify) for WalletRoam** |
| Local rail gap in a top market | 3 | **3** | **Cards + Apple Pay only, USD-only pricing, across 11 UI locales.** FPX and DuitNow absent in the #1 market; OXXO/SPEI absent in #2; Pix, Kaspi.kz, PayNow, PayTo all absent |
| Recent market expansion | 2 | **2** | Nine partnerships in 12 months; the ~12 Oct 2026 telco definitive agreement is live now |
| Known payment issues | 2 | **0** | ⬜ **Deliberate zero.** Complaints were not researched and none surfaced |
| Recent funding | 2 | **0** | ⬜ **No raise in FY26, by design and loudly advertised. DO NOT pitch a funding trigger** |
| Traffic outside home market | 2 | **2** | **Extreme dispersion** — no market above 21.53%; Malaysia 21.53%, Mexico 13.90%, US 13.19%, France 9.88%, Canada 9.12%, Kazakhstan 7.44%, **and no legal entity outside AU/MY/HK** |
| Competitor on orchestration | 2 | **0** | ⬜ Not researched |
| Payment job postings | 1 | **0** | ⬜ **Zero job openings of any kind found** |
| **TOTAL** | **29** | **16** | 🟢 **Medium** |

**Four deliberate zeros and a volume score of 2 out of 5.** **The 16 is honest on the matrix and misleading as a verdict** — the rows that score well (multi-PSP, rail gaps, country dispersion) all describe real complexity on a base too small to monetise, and the row that matters most scores 2. **Treat as analyst-override candidate.**

## Section 9: Do NOT Say

- ❌ **"HQ Australia"** — it is operationally Malaysia; Perth is a corporate-services address.
- ❌ **"~$15M revenue"** — it is **A$10.17m, down 25%.**
- ❌ **The unaudited A$9.9m / A$0.4m figures.** Cite the audited A$10.17m / A$0.66m.
- ❌ **Flexiroam X or X-ONE** — discontinued 1 July 2024, absent from FY26 filings.
- ❌ **A Singapore or US entity.** Neither exists.
- ❌ **"SSM No 670869-A."** Could not be tied to the entity.
- ❌ **Alipay** — unverified, contradicted by their own current help article.
- ❌ **PayPal as a live method** — legacy marketing only.
- ❌ **Google Pay as enabled** — only an Airwallex SDK element type.
- ❌ **Primer** — all 16 hits were `"Supprimer"` and `"primera"`.
- ❌ **Omise** — all 453 hits were `Promise`/`compromise`.
- ❌ **Instalments / `meses sin intereses`** — `meses` is just "months" in plan-validity copy.
- ❌ **Multi-currency support** from the MYR/MXN/KZT/BRL codes — that is a generic country-metadata table.
- ❌ **A funding trigger.** No raise in FY26.
- ❌ **"over 15,000 users"** on the AI agent — not in any audited filing.
- ❌ **Treating Paydibs/DIALOG as Flexiroam's processors.** They are Flexiroam's *customers*.
- ❌ **Any claim about the in-app `native` provider.** Unresolved — ask.

## Section 10: Research Confidence

**Overall: HIGH on financials and the payment stack. ZERO on volume.**

- ✅ **Primary audited sources:** FY26 Annual Report + Appendix 4E (ASX 28 Aug 2026, 83pp) and the FY26 Full Year Results Presentation (Board-authorised 5 Sep 2026, 27pp), both downloaded and text-extracted locally. All financials, segment data, the going-concern note, the CEDS entity list and the CEO loan come from these.
- ✅ **First-party code:** 5.6MB of Next.js bundles across 36 chunks, plus the WalletRoam Shopify storefront and the Terms.
- ✅ **Rigorous false-positive control** — five distinct traps caught, including a 453-hit `omise` and a 16-hit `primer` that were entirely spurious.
- ⚠️ **Blocked:** BuiltWith refused the domain.
- ⚠️ **Unresolved:** the D2C-vs-brand-partner split inside the A$9.0m Travel segment (not disclosed; the 56/44 recurring/transactional split is the closest proxy) · **the geographic revenue split — which the company states in its audited revenue note it CANNOT determine** · subscriber, activation, transaction, ARPU and plan-price figures (none disclosed anywhere) · **what the in-app `native` provider actually is — the only thing that could still undercut the orchestration case** · Google Play IAP status (guessed package id 404'd) · the Airwallex↔Stripe routing split by market/currency/BIN (server-side, invisible) · the supported currency list · acquiring geography, MDR, approval and decline rates, chargebacks, PCI level · **whether the ~12 Oct 2026 telco definitive agreement landed — the 90-day target expires within days of this report and no announcement was found as at 6 Oct 2026. The single most time-sensitive item; re-check before any outreach** · whether Alipay was ever live (the one unresolved contradiction in the record).

</details>
