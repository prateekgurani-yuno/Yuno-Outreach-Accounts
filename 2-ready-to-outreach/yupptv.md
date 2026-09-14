# YuppTV

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 15 / 24 → ⭐ High Priority *(conditional — see analyst note)*
**Industry:** OTT / Video streaming (South Asian diaspora) · **HQ:** Alpharetta, Georgia, USA (engineering centre Hyderabad, India) · **Researched:** 2026-09-14 · **First email sent:** —
**Motion:** Displacement — Juspay confirmed in production code

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** YuppTV streams South Asian live TV, film and cricket to the diaspora across 100+ countries, sold as auto-renewing subscriptions. It contracts through exactly two entities — **YuppTV USA Inc.** (Georgia) and **YuppTV India Private Limited** — and runs web checkout on **two Indian-domiciled gateways, Juspay and Razorpay**, while roughly 45% of its traffic sits outside India. A second business line, Yupp Video Services, white-labels its stack (including subscription billing) to other OTT platforms.

**SimilarWeb total visits (last full month):** Not shown in the supplied view — shares and country ranks only. Source: SimilarWeb (supplied 2026-09-10), Jun–Aug 2026, `yupptv.com`, all-country-domains OFF. Verified independently that no other YuppTV domain resolves (`yupptv.in`, `yupptv.tv` both dead), so the single-domain view is complete.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | India | 55.26% | Visa, Mastercard, Amex, **RuPay, UPI, GPay, PhonePe, Paytm** — from the checkout's own method assets | None confirmed missing | ✅ YuppTV India Pvt Ltd (CIN U72200TG2007PTC054335) |
| 2 | United States | 8.59% | Cards. PayPal claimed by a 2020 user-generated page only — **unverified** | No PayPal in the checkout asset set | ✅ YuppTV USA Inc. (Alpharetta, GA) |
| 3 | Pakistan | 4.73% | Not determinable — checkout is client-rendered | JazzCash / Easypaisa — **no evidence either way** | ❌ no entity found |
| 4 | UAE | 3.76% | **Etisalat (e&) direct carrier billing** — co-branded DCB landing page + `etisalat.yupptv.com`; du distribution partnership | Local card rails not determinable | ❌ no entity found |
| 5 | Bangladesh | 3.07% | Not determinable | bKash / Nagad / Rocket — **no evidence either way** | ❌ no entity found |

**10 of the top 12 markets — 30.1% of traffic — have no confirmed local entity.** Those subscribers contract with a Georgia company under Georgia law.

### Legal entities
- **YuppTV USA Inc.** (USA, Georgia) — contracting party, data controller, App Store seller of record. 11175 Cicero Dr, Suite #100, Alpharetta, GA 30022
- **YuppTV India Private Limited** (India) — CIN U72200TG2007PTC054335, Hyderabad
- YuppTV Digital India Private Limited (India) — CIN U22300TG2019PTC137791. Appears in registries but in none of YuppTV's own legal documents
- UK: **GDPR Article 27 representative only** — a compliance appointment at a London address, not a subsidiary
- No Singapore, UAE, Australian, Canadian, German, Dutch, Malaysian, Pakistani or Bangladeshi entity found in any registry

### Known PSPs
- **Juspay** — `[Source Code]` dedicated Next.js route `/buy/juspay/[...index]`, `gateway:"juspay"`, `juspay_order_id` persisted client-side
- **Razorpay** — `[Source Code]` dedicated routes `/buy/razorpay/[...index]` and `/buy/razorpay-paymentStatus`, `gateway:"razorpay"`
- Both dispatched by a merchant-controlled `gateway` parameter against `prod-api.yupptv.com/payment/api/v1/order/checkout`
- **No international PSP of any kind** appears in the production build manifest

### Orchestration status
**Juspay confirmed — displacement motion.** A first-class production checkout route with an `externalTransactionToken` redirect pattern. There is also a thin merchant-side gateway-dispatch switch above it running Razorpay as a parallel rail, so routing is not fully delegated. Zero evidence of any global orchestrator (Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno). **Not a Yuno customer** — zero matches across all production assets and search.

### Buying signals
- 🚀 [TATA IPL 2026 streaming rights](https://blog.yupptv.com/2026/03/yupptv-bags-tata-ipl-2026-streaming-rights.html) (Mar 2026) — Continental Europe, Malaysia, Hong Kong, Japan, SE Asia. **New billing territories for a payment stack built on two Indian gateways.**
- 🚀 [Asia Cup 2025 digital rights](https://www.prnewswire.com/news-releases/yupptv-secures-digital-telecast-rights-for-asia-cup-2025-302554070.html) (Sep 2025) — 60+ countries
- 🤝 [Yupp Video Services powers Chaupal's platform](https://www.prnewswire.com/news-releases/yupp-video-services-powers-chaupals-full-scale-technology-upgrade-strengthening-platform-reliability-performance-and-user-experience-across-25-devices-302637692.html) (Dec 2025) and [launches Heartland+ with subscription services](https://www.prnewswire.com/news-releases/yupp-video-services-partners-with-get-after-it-media-to-launch-heartland-302656422.html) (Jan 2026) — they sell billing infrastructure to other OTTs
- ⚠️ Multi-year, multi-platform complaint pattern on **unauthorised renewals, absent self-serve cancellation and withheld refunds**, with users routing to issuer chargebacks
- ❌ **No funding since 2016.** No current IPO filing or process despite historical reports — do not use either as a trigger

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach YuppTV` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 15 / 24
| Signal | Points | Status |
|--------|--------|--------|
| Orchestration status | +3 | ✅ **Juspay confirmed** in production source code → displacement, not greenfield. Not +4: this is not a greenfield stack |
| 3+ countries | +3 | ✅ 10 markets above 1% traffic share; 2 confirmed legal entities |
| Multiple PSPs | +3 | ✅ Juspay **and** Razorpay, two independently built checkout routes, source code |
| Local rail or licensing gap in a top-3 market | 0 | ❌ India (55%) carries UPI, RuPay, Paytm, PhonePe, GPay in its own checkout assets. US and Pakistan are top-3 but neither is a regulatorily gated acquiring market. **Scored honestly at zero rather than stretched** |
| Recent expansion | +2 | ✅ IPL 2026 rights across Continental Europe, Malaysia, HK, Japan, SE Asia (Mar 2026); Asia Cup 2025 across 60+ countries |
| Payment issues reported | +2 | ✅ Moderate, persistent, verbatim-sourced across App Store 2022–2023, corroborated (unverified) on Trustpilot and BBB |
| Funding >$10M | 0 | ❌ Last institutional round Series B $50M, October 2016 |
| High traffic outside home | +2 | ✅ India 55.26%, below the 60% threshold |
| Competitor using orchestration | 0 | ❌ None confirmed. The apparent ZEE5–Juspay hit is a syndicated press release ZEE5 *published*, not a merchant relationship — see 11C |
| Payment job postings | +1 → 0 | ❌ None found |

**Tier:** ⭐ High Priority (15) — **conditional.**

> ### Analyst note — read before working this account
>
> The arithmetic says ⭐, and the payment-infrastructure findings genuinely support it. Two things temper it, and both should be resolved before sequence effort is spent:
>
> **1. An unquantified share of billing sits outside orchestration's reach.** Confirmed live and promoted by YuppTV itself: Apple IAP (with fetched price tiers, including device-activation fees), Google Play, Amazon Appstore, Roku (bills to the Roku account), and **six telco billing relationships** — Etisalat and du (UAE), unifi (Malaysia), BSNL and Vi (India), Ooredoo (Qatar, white-label app). Orchestration cannot touch any of it. The web-vs-store-vs-telco split is **not quantified in any public source**.
>
> **This is not the Replika case.** There, IAP dominance was established and the account was rejected. Here the direct-billed book is demonstrably real: two production checkout routes exist, and the cancellation-friction complaints *cannot* be describing the Apple path, since Apple subscribers self-cancel in Settings. One complainant explicitly routes their remedy through an **issuer chargeback**, which only happens in a direct merchant-of-record relationship. So web billing is real — its *share* is the open question.
>
> **2. This is not a growth account.** Traffic is falling in most markets (India −34%, US −45%, Bangladesh −57% YoY). The Indian entity's revenue fell 19% to ₹41.3 Cr in FY25. No funding since 2016. Absolute transaction volume may be smaller than a 15/24 implies.
>
> **Gate:** establish the channel split on the first call before investing in the full sequence. If IAP and telco dominate, this drops to 🟢 Medium or below.

### Source Notes
- ✅ Juspay and Razorpay — production build manifest and payment route chunks, fetched 2026-09-14
- ✅ Two contracting entities and Georgia governing law — verbatim from `/help/terms-and-conditions`
- ✅ Apple IAP tiers — fetched from the App Store listing
- ✅ Complaint verbatims — dated, attributable App Store reviews
- ⚠️ **Revenue ₹41.3 Cr FY25 is the Indian entity's standalone MCA figure, not global.** ≈US$4.7M is implausible for a 12-country subscription business with a $50M round behind it. The US entity files nothing public. Use as a floor on one entity, never as company size
- ⚠️ Trustpilot and BBB complaint specifics (the $35 charge, the £139 charge, partial refunds) — **403 blocked, summary only. Do not quote these figures**
- ⚠️ PayPal acceptance — a single 2020 user-generated page. **Do not assert**
- ⚠️ Etisalat co-branded pages surfaced but not fetched. Verify before citing
- ⚠️ No PSP is named in any press release, case study or job posting. Source code is the sole channel for the Juspay and Razorpay findings — strong, but single-channel
- ❌ No evidence either way on UPI in non-India markets, or on any local rail in Pakistan, Bangladesh, Saudi, Netherlands, Germany, Australia

### Success Case Alternatives
- **Shahid (MBC Group)** — the closest public analogue found: Arabic content billed across 14+ MENA markets plus US/Europe diaspora, cross-border collection solved through a single-API aggregator spanning local carrier-billing rails. Same payment shape as YuppTV. Not a Yuno case — use conversationally, never as Yuno proof
- **NetEase Games / Garena** — Yuno's APAC gaming references. **No verified results on file for either, and no public confirmation of the Garena relationship.** Relevance signalling only, never quantified proof
- **Open English** — Tier 2 pattern match: multi-country recurring subscriptions. Different vertical; say so if used
- **inDrive** — Tier 2: multi-country scale via orchestration. LATAM results; never imply they came from Asia

---

## Executive Summary

YuppTV sells auto-renewing South Asian streaming subscriptions to a diaspora audience spread across 100+ countries, contracting through just two entities — one in Georgia, USA and one in Hyderabad, India. Its web checkout runs on **Juspay and Razorpay, both Indian-domiciled**, dispatched by a merchant-controlled gateway switch, while **roughly 45% of its traffic originates outside India** and 10 of its top 12 markets have no local entity. The motion is **displacement, not greenfield**: they already believe in orchestration, so the opening is international reach beyond an India-built stack, not the case for orchestration itself. The account's main qualification is that an unquantified share of billing runs through Apple, Google, Roku and six telco partners, which orchestration cannot address.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** SimilarWeb supplied by Prateek 2026-09-10 (screenshot transcription), period Jun–Aug 2026, domain `yupptv.com`, "Include all country domains" OFF. Independently verified that `yupptv.in` and `yupptv.tv` do not resolve, so no other domain exists to merge. Total visit volume was not shown in the supplied view.

| Rank | Country | Traffic Share | Est. Monthly Visits | Trend | Country rank | Source |
|------|---------|---------------|---------------------|-------|--------------|--------|
| 1 | India | 55.26% | Not shown | ↓ −34.30% | #5,540 | SimilarWeb (supplied) |
| 2 | United States | 8.59% | Not shown | ↓ −45.13% | #63,828 | SimilarWeb (supplied) |
| 3 | Pakistan | 4.73% | Not shown | ↓ −33.18% | #6,082 | SimilarWeb (supplied) |
| 4 | United Arab Emirates | 3.76% | Not shown | ↓ −31.17% | #5,160 | SimilarWeb (supplied) |
| 5 | Bangladesh | 3.07% | Not shown | ↓ −56.56% | #12,447 | SimilarWeb (supplied) |
| 6 | United Kingdom | 1.88% | Not shown | ↑ +45.50% | #39,542 | SimilarWeb (supplied) |
| 7 | Australia | 1.46% | Not shown | ↑ +0.11% | #21,820 | SimilarWeb (supplied) |
| 8 | Saudi Arabia | 1.37% | Not shown | ↓ −19.55% | #14,815 | SimilarWeb (supplied) |
| 9 | Canada | 1.34% | Not shown | ↓ −21.01% | #45,310 | SimilarWeb (supplied) |
| 10 | Germany | 1.24% | Not shown | ↓ −7.74% | #59,161 | SimilarWeb (supplied) |
| 11 | Netherlands | 0.97% | Not shown | ↓ −2.01% | #35,884 | SimilarWeb (supplied) |
| 12 | Malaysia | 0.71% | Not shown | ↓ −4.97% | #20,023 | SimilarWeb (supplied) |

**High priority (>5% share):** India, United States.

**Engagement anomaly worth noting:** US visit duration is **8:22** against India's **2:31**, with 5.30 pages per visit against 3.42. The US audience is far smaller but materially more engaged — a paying-subscriber signature rather than a browsing one. US revenue share is therefore likely well above its 8.59% traffic share. `[INFERENCE, not confirmed]`

**Trend caution:** traffic is declining in 10 of 12 markets. The UK (+45.50%) is the exception. Do not build an outreach hook on decline — it reads as an insult in a cold email.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Alpharetta, Georgia, USA (11175 Cicero Dr, Suite #100). Engineering centre in Hyderabad, India. Founded 2006 by Uday Reddy, who remains Founder & CEO.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| USA (Georgia) | YuppTV USA Inc. | GA control no. 0669640 `[UNVERIFIED — search summary only]` | https://www.yupptv.com/help/terms-and-conditions · https://www.yupptv.com/help/privacy-terms |
| USA (West Virginia, foreign reg.) | YUPPTV USA, INC. | 358447 `[UNVERIFIED — search summary only]` | https://opencorporates.com/companies/us_wv/358447 |
| India | YUPPTV INDIA PRIVATE LIMITED | CIN U72200TG2007PTC054335 | https://www.yupptv.com/help/terms-and-conditions · https://www.zaubacorp.com/YUPPTV-INDIA-PRIVATE-LIMITED-U72200TG2007PTC054335 |
| India | YUPPTV DIGITAL INDIA PRIVATE LIMITED | CIN U22300TG2019PTC137791 | https://www.zaubacorp.com/YUPPTV-DIGITAL-INDIA-PRIVATE-LIMITED-U22300TG2019PTC137791 |
| UK | **None.** GDPR Art. 27 representative only — 344-354 Gray's Inn Road, London WC1X 8BP | n/a | https://www.yupptv.com/help/privacy-terms |

**The two decisive quotes, verbatim from YuppTV's own T&Cs:**

> "This Agreement sets out the terms and conditions for a User… intending to subscribe, avail or access or receiving services and/or equipment of **YuppTV India Private Limited/ YuppTV USA Inc.**"

> "**YuppTV shall mean YuppTV USA Inc. and/or YuppTV India Private Limited.**"

> "This Agreement is governed by the laws of the **United States and the federal state of Georgia** and is subject to the exclusive jurisdiction of the courts at Georgia."

**Cross-Border Gap Analysis:**

| Country | In Top 12 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| India | ✅ 55.26% | ✅ YuppTV India Pvt Ltd | ✅ Yes — India gates domestic acquiring behind local presence | Low — the entity clears the gate |
| United States | ✅ 8.59% | ✅ YuppTV USA Inc. | No | Low |
| Pakistan | ✅ 4.73% | ❌ | No | **High** |
| UAE | ✅ 3.76% | ❌ | No | **High** |
| Bangladesh | ✅ 3.07% | ❌ | No | **High** |
| United Kingdom | ✅ 1.88% | ❌ (representative only) | No | **High** |
| Australia | ✅ 1.46% | ❌ | No | **High** |
| Saudi Arabia | ✅ 1.37% | ❌ | No | **High** |
| Canada | ✅ 1.34% | ❌ | No | **High** |
| Germany | ✅ 1.24% | ❌ | No | **High** |
| Netherlands | ✅ 0.97% | ❌ | No | **High** |
| Malaysia | ✅ 0.71% | ❌ | No | **High** |

> *"Warning: 10 of the top 12 markets — 30.1% of total traffic — have no confirmed local entity. Those subscriptions are contracted with YuppTV USA Inc. under Georgia law and are almost certainly acquired cross-border out of the US. Every non-USD market in that list is a foreign-issued card hitting a US acquirer."*

**On the regulatory gate:** of the markets where domestic acquiring is effectively gated behind local presence (India, Indonesia, China, Vietnam, South Korea), **only India is material for YuppTV — and it holds the entity**. The gate does not bind elsewhere in its footprint.

**Contradiction to resolve on a call:** the T&Cs name YuppTV India Pvt Ltd as a contracting party, yet governing law for the whole agreement is Georgia, with no India carve-out found. Which entity actually invoices an Indian subscriber is not determinable from public documents. `[INFERENCE, not confirmed]`

> **MANUAL:** Confirm which entity appears on an Indian subscriber's card statement, and whether the US entity holds a separate merchant account.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Not geo-scoped in client code | **Juspay** | `[Source Code]` | https://www.yupptv.com/_next/static/chunks/pages/buy/juspay/%5B...index%5D-6d6c11bf7e3f0562.js |
| Not geo-scoped in client code | **Razorpay** | `[Source Code]` | https://www.yupptv.com/_next/static/chunks/pages/buy/razorpay/%5B...index%5D-175d0d89a5e67f00.js |
| UAE | Etisalat (e&) direct carrier billing | `[Third-Party Report]` | https://pt6.etisalat.ae/dcb-digital/landindex?id=7&type=132gff&txnid=y&banner=etisalat&lang=en |
| UAE | du (EITC) distribution partnership | `[Press Release]` | https://www.du.ae/about/media-centre/newsdetail/du-launches-strategic-partnership-with-yupptv |
| Malaysia | unifi / TM direct carrier billing | `[Third-Party Report]` | https://unifi.com.my/sites/default/files/html/plus-box/doc/FAQ-YuppTV-ver4a_14June2021.pdf |
| India | BSNL bundle (YuppTV Scope) | `[Third-Party Report]` | https://telecomtalk.info/bsnl-yupptv-scope-subscription-costs-rs-199-per-month-after-introductory-offer/345284/ |
| India | Vi (Vodafone Idea) bundle | `[Third-Party Report]` | https://www.myvi.in/blog/get-yupptv-subscription |
| Qatar | Ooredoo white-label app | `[Third-Party Report]` | https://play.google.com/store/apps/details?id=com.yupptv.ooredooapp |
| Global (iOS/tvOS) | Apple In-App Purchase | `[Third-Party Report]` | https://apps.apple.com/us/app/yupptv-live-tv-movies/id665805393 |
| Global (Roku) | Roku billing | `[Third-Party Report]` | https://support.roku.com/article/36296801163799 · https://www.yupptv.com/Devices/Roku |

**Primary evidence, verbatim from the production build:**

```
"/buy/juspay/[...index]"
"/buy/razorpay/[...index]"
"/buy/razorpay-paymentStatus"
"/buy/payment-failure"  "/buy/payment-status"  "/buy/payment-success"
```

```js
proceedToPayWithJstpay = e => { let o=e[1], t={ gateway:"juspay", packages:e[0].toString(),
  externalTransactionToken:o, sharePersonalInfoWithCP:"true" };
```

```js
proceedToPayWithRazorpay = (e,a) => { let t={ gateway:"razorpay", packages:e[0].toString(),
  userConsent:"true", method:a, sharePersonalInfoWithCP:"true" };
  s({ url:"https://prod-api.yupptv.com/payment/api/v1/order/checkout", apiData:t })
```

**Checkout method assets (shared module across both gateway chunks):**
`visa` · `mastercard` · `amex` · `rupay` · `upi` · `gpay` · `phonepe` · `paytm`

India-domestic rails plus global card schemes. **No PayPal, no Mada, no bKash, no iDEAL, no local rail for any non-India market.**

**Negative check** — combined grep across homepage, build manifest, all payment route chunks and the privacy policy for `stripe|paypal|adyen|braintree|checkout.com|worldpay|2c2p|telr|payfort|nuvei|worldline|recurly|chargebee|cleeng|spreedly|primer|gr4vy|payrails|y.uno`: **0 matches.**

#### 3B. Payment Orchestrator

**Regional orchestrator — Juspay confirmed.** Evidence: a first-class production checkout route posting `gateway:"juspay"` with an `externalTransactionToken` and persisting `juspay_order_id`. Juspay self-describes as an orchestration layer above multiple gateways and publicly documents Razorpay as a connected gateway.

> *"Confirmed orchestration-aware. The opening is coverage and international reach, not the case for orchestration itself."*

**Nuance:** YuppTV also maintains its own gateway-dispatch switch — `prod-api.yupptv.com/payment/api/v1/order/checkout` accepts `gateway` as a merchant-controlled parameter with at least `juspay` and `razorpay` as siblings. So routing is not fully delegated: Juspay handles part of the traffic, a hand-rolled merchant-side switch decides which rail a transaction enters, and Razorpay runs as a parallel direct rail. Whether that switch is geo-aware is **not observable** — grep for `countryCode|currency|geo|region|INR|USD` across the payment chunks returned zero matches, so the decision lives server-side.

**Caveat:** what sits *behind* Juspay is invisible client-side. Juspay could be fanning out to international acquirers. Absence of evidence is not proof of absence.

> **MANUAL:** Walk checkout with DevTools from an India IP and a UAE IP. Compare which `gateway` value the API returns. This single test answers the central question of the account.

---

### Section 4: Alternative & Local Payment Methods

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| India | UPI, GPay, PhonePe, Paytm | Bank rail / Wallet | **Active in checkout** (method assets) | Juspay/Razorpay route chunks |
| India | RuPay, Visa, Mastercard, Amex | Cards | **Active in checkout** | Juspay/Razorpay route chunks |
| India | UPI Autopay (recurring) | Bank rail | **Not found** | — |
| India | Netbanking | Bank transfer | Mentioned in docs (category only) | https://www.yupptv.com/help/privacy-terms |
| India | BSNL / Vi telco bundles | Carrier billing | **Active** | telecomtalk.info · myvi.in |
| UAE | Etisalat DCB | Carrier billing | **Active** (co-branded DCB path) | pt6.etisalat.ae |
| Malaysia | unifi DCB, myunifi app, TMpoint, POS Malaysia, online banking | Carrier / Cash / Bank | Mentioned in operator FAQ | unifi.com.my FAQ PDF |
| Global (iOS/tvOS) | Apple IAP | App-store billing | **Active — tiers fetched** | apps.apple.com |
| Global (Android) | Google Play billing | App-store billing | Listings exist; tiers unverified | play.google.com |
| Global (Roku) | Roku account billing | App-store billing | **Active** | support.roku.com |
| US | PayPal | Wallet | **Not confirmed** — 2020 user-generated page only | https://yupptv.knoji.com/questions/yupp-tv-paypal/ |
| Pakistan | JazzCash / Easypaisa | Wallet | **Not found** | — |
| Bangladesh | bKash / Nagad / Rocket | Wallet | **Not found** | — |
| Saudi Arabia | Mada / STC Pay / Tabby / Tamara | Cards / Wallet / BNPL | **Not found** | — |
| Netherlands | iDEAL | Bank transfer | **Not found** | — |
| Germany | SEPA / Klarna | Bank transfer / BNPL | **Not found** | — |
| Australia | PayTo / BPAY | Bank rail | **Not found** | — |
| Global | Apple Pay / Google Pay (web) | Wallet | **Not found** | — |

**No accepted-payment-methods list is published anywhere.** No help-centre article, FAQ or checkout page enumerating methods is publicly indexed or fetchable; the checkout is client-rendered and login-gated.

**Consequence, and it matters:** every "Not found" above is genuinely unknown, **not** a confirmed gap. Nobody may write *"YuppTV doesn't accept bKash"* — that is unverified. The only sourced method set is the India-centric asset bundle above.

The privacy policy's only payment language, verbatim:

> "YuppTV will be using **third party payment gateway providers** to process and facilitate the payment of your subscription fee… Please note that YuppTV does not directly collect any financial information such as credit card or debit card or **net banking** details from you."

> **MANUAL:** VPN checkout walkthrough from India, UAE and the US. This is the only way to close the gap.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Unauthorised auto-renewal + refund refusal + forced chargeback | iOS App Store | Moderate, recurring | Jul 2023 | https://justuseapp.com/en/app/665805393/yupptv-live-tv-movies/reviews |
| Recurring debit without consent, no working support channel | iOS App Store | Moderate | Jan 2023 | ibid. |
| No self-service cancellation; hard refund cut-off | iOS App Store | Moderate, recurring | Dec 2022 | ibid. |
| Locked annual term, no refund option | iOS App Store | Isolated | Oct 2022 | ibid. |
| Cancellation friction | iOS App Store | Moderate | Nov 2022 | ibid. |
| Charges after cancellation, partial refunds withheld | Trustpilot / BBB | **Unverified — 403 blocked** | Various | Not readable |

**Verbatim, the most commercially significant:**

> "They did renew and charged from my credit card without my knowledge. They didn't give money back… **There is no way to cancel the subscription.** They are looting money from cards and not giving it back… **Onlyway to get your money back is to dispute through credit card's bank.**" — VG18011987, 2023-07-04

> "…addressing a issue regarding **automatic deductions from my CC without my consent** and despite multiple assurances haven't got a reply or a callback." — Vaishsays, 2023-01-29

> "**if you want to cancel the subscription you have to go through customer support… Why isn't there an option online??** If you miss cancelling by even one day they won't refund you back!" — Palanki, 2022-12-28

**The channel diagnosis — this is the most useful inference in the report.** Apple IAP subscribers can self-cancel in Settings. So complaints saying *"there is no way to cancel"* and *"you have to go through customer support"* **cannot be describing the Apple path**. They describe YuppTV's own web card-on-file billing. The 2023-07-04 reviewer routes the remedy through an **issuer chargeback**, which only exists in a direct merchant-of-record relationship.

> *"Pattern of forced-support cancellation and withheld refunds on the direct-billed path suggests a chargeback-cost problem, not merely an NPS problem. Chargeback ratios feed acquirer risk scoring, which feeds approval rates."*

**Honest frequency assessment:** **moderate and persistent, not systemic-by-proof.** Of ~21 App Store reviews readable verbatim, roughly 6 concern payment or billing. The dominant complaint theme by volume is advertising load and mid-term channel removals — product issues, out of scope, and deliberately not counted here. No App Store review after January 2024 was readable, so the 2025–26 picture is unverified.

**No verified FX or currency-mismatch complaint was found.** Do not claim one.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | Mar 2026 | TATA IPL 2026 streaming rights — Continental Europe, Malaysia, Hong Kong, Japan, SE Asia | Market Expansion | https://blog.yupptv.com/2026/03/yupptv-bags-tata-ipl-2026-streaming-rights.html |
| 2 | Jan 2026 | Yupp Video Services + Get After It Media launch **Heartland+**, incl. ad stack and subscription services | B2B platform / Partnership | https://www.prnewswire.com/news-releases/yupp-video-services-partners-with-get-after-it-media-to-launch-heartland-302656422.html |
| 3 | Dec 2025 | Yupp Video Services powers Chaupal's technology upgrade across 25+ devices | B2B platform / Partnership | https://www.prnewswire.com/news-releases/yupp-video-services-powers-chaupals-full-scale-technology-upgrade-strengthening-platform-reliability-performance-and-user-experience-across-25-devices-302637692.html |
| 4 | Sep 2025 | Asia Cup 2025 digital telecast rights — 60+ countries | Market Expansion | https://www.prnewswire.com/news-releases/yupptv-secures-digital-telecast-rights-for-asia-cup-2025-302554070.html |
| 5 | FY25 | Indian-entity revenue ₹41.3 Cr, down 19% from ₹51.0 Cr FY24 | Financial | https://inc42.com/company/yupptv/financials/ |

**No public payment-related RFP found.**
**No payment, billing or finance job postings found.** No Head of Payments or Head of Finance appointment.
**No funding since the October 2016 Series B ($50M, Emerald Media).** Total raised reported as $67.7M `[UNVERIFIED]`; a separate aggregator gives $58M — sources conflict, do not cite unqualified.
**No current IPO filing or process.** Historical IPO reports exist; nothing live in 2025 or 2026. Do not use as a trigger.

**Business-model signal:** the two most recent corporate items are both **Yupp Video Services** deals. YuppTV sells its stack — including subscription billing — to other OTT platforms as a white-label B2B product. Any payments conversation touches both their own D2C book and a product they resell.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | Jan 2026 | Heartland+ packages "ad units **and subscription-based services**" | Yupp Video Services resells subscription billing — implies an owned billing layer | https://www.prnewswire.com/news-releases/yupp-video-services-partners-with-get-after-it-media-to-launch-heartland-302656422.html |
| 2 | Undated (live) | T&Cs require "a valid **credit card** for payment of all monies due"; auto-renewal; country-differentiated rates | Confirms card-on-file merchant-of-record recurring billing | https://www.yupptv.com/help/terms-and-conditions |

**No PSP partnership announcement, provider removal, pricing-model change, or web↔app-store billing migration was found in any source.** None is being manufactured to fill this section.

---

### Section 8: Checkout Experience Audit

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | **Unknown** | — | Client-rendered. Route structure suggests a redirect pattern (`externalTransactionToken`), but not observed |
| Guest checkout | **Not determinable** | — | `/signup` route exists; purchase-before-account not observable |
| Card input experience | **Unknown** | — | No card form in delivered HTML |
| Payment methods visible | Visa, MC, Amex, RuPay, UPI, GPay, PhonePe, Paytm | — | From checkout asset module, not a rendered page |
| Location-based method display | **Not observable** | — | Zero `countryCode`/`currency`/`geo` keys in payment chunks; decision is server-side |
| Instalment / EMI options | **Not found** | — | No EMI asset or route |
| 3DS implementation | **Not detected** | — | No 3DS indicator in source |
| PCI indicator | No card-vault or payment iframe script on public pages | — | Consistent with hosted/redirect model |
| Multi-currency / local pricing | T&Cs state rates differ by country; USD activation fees confirmed | — | Not observable in HTML |
| Mobile responsiveness | Viewport meta present; separate `m.yupptv.com` property | — | Rendering not verified |
| App-store linkage | `apple-itunes-app: app-id=665805393` and `google-play-app` meta in page head | — | App-first distribution confirmed at the web layer |
| Third-party scripts | JW Player, mux.js, GTM-KHGQ2D, gtag G-06SYNBB45M, **Google Ads AW-1007853834** | — | Purchase-conversion tracking present |

*"Full checkout flow not accessible. Findings limited to publicly observable elements."* The site is a Next.js SPA (build ID `x9RG7ENCJOWrqzhasQoOf`); `/allpackages` delivers exactly one server-rendered string — the page title. **Checkout type is not being inferred.**

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **No public information found** | — |
| Card data handling | Merchant disclaims holding card data entirely | https://www.yupptv.com/help/privacy-terms |
| Recommended Yuno integration | SDK (consistent with a hosted/redirect model) | — |

> "YuppTV does not directly collect any financial information such as credit card or debit card or net banking details from you… **YuppTV never receives your financial and payment information from these payment gateways.**"

> `[INFERENCE, not confirmed]: Based on the stated redirect/hosted-checkout model and the externalTransactionToken pattern observed in code, PCI scope is likely reduced with the gateways handling card data. No attestation, AOC or compliance statement exists publicly.`

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: Two Indian gateways carrying a 45%-international subscriber book**
> **Evidence:** §3A — Juspay and Razorpay confirmed in production code, no international PSP anywhere in the build manifest. §1/§2 — 10 of 12 top markets (30.1% of traffic) have no local entity and contract with a Georgia company.
> **Pain Point:** Foreign-issued cards from the UK, Australia, Canada, Germany, the Netherlands, Pakistan, Bangladesh and the Gulf being presented to Indian-domiciled acquiring. Domestic issuers decline foreign-acquired transactions at materially higher rates than locally-acquired ones, and there is no observable geo-routing in the client to suggest otherwise.
> **Yuno Value Proposition:** Route each transaction to a local acquirer in the cardholder's geography, on top of the existing stack — Juspay and Razorpay stay where they are strongest.
> **Best Success Case:** Shahid/MBC conversationally (same diaspora billing shape); inDrive as a Tier 2 Yuno pattern match on multi-country acquiring, explicitly labelled as LATAM.
> **Outreach Angle:** Your checkout runs Juspay and Razorpay, and roughly 45% of your traffic sits outside India.
> **Suggested Subject Line:** Two Indian gateways, 45% international traffic
>
> **Insight #2: New territories bought, old rails underneath**
> **Evidence:** §6 — IPL 2026 rights across Continental Europe, Malaysia, Hong Kong, Japan and SE Asia (Mar 2026), Asia Cup 2025 across 60+ countries. §3A — the confirmed payment stack is two Indian gateways.
> **Pain Point:** Cricket rights are bought per-tournament and monetised in a fixed window. Peak-load signup in markets where the acquiring path was not designed for local cards is exactly where approval-rate leakage costs the most, and there is no second attempt at a tournament.
> **Yuno Value Proposition:** Add local acquiring and failover per market through one integration, ahead of the next rights window rather than during it.
> **Best Success Case:** Wingo (airlines — high-ticket, peak-demand routing), labelled as a pattern match.
> **Outreach Angle:** IPL 2026 put you live in Japan, Hong Kong and Continental Europe; the checkout behind it is still two Indian gateways.
> **Suggested Subject Line:** IPL 2026 markets, India-built checkout
>
> **Insight #3: Cancellation friction converting into chargebacks**
> **Evidence:** §5 — dated, verbatim complaints across 2022–2023 describing no self-serve cancellation, renewals during the friction window, refunds withheld, and remedy sought through issuer chargeback. §2 — T&Cs state charges are "non-refundable" with no refunds for partial periods.
> **Pain Point:** Every forced chargeback is the fee plus the disputed amount plus a ratio that feeds acquirer risk scoring — which feeds approval rates on the same cross-border volume as Insight #1. The two problems compound.
> **Yuno Value Proposition:** Dunning and retry logic that recovers the renewal before it becomes a dispute, and unified visibility of failed renewals across providers instead of per-gateway dashboards.
> **Best Success Case:** Livelo (failed-transaction recovery), labelled as a pattern match.
> **Outreach Angle:** Your App Store reviews from 2022 and 2023 have subscribers saying the only way to get a refund was to dispute with their bank.
> **Suggested Subject Line:** Renewals ending as chargebacks
> **Caution:** this angle is sharp and could read as an attack. Use the diplomatic clause, and only in Phase 2 or later.

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks:**
1. Your checkout ships two gateways, Juspay and Razorpay, and both are India-domiciled — while roughly 45% of your traffic comes from outside India.
2. IPL 2026 took you live across Continental Europe, Malaysia, Hong Kong and Japan, on a payment stack built for the Indian market.
3. Ten of your top twelve markets have no local entity, so those subscribers are contracting with a Georgia company and paying on a foreign-acquired card.

**Cold call openers:**
1. I was looking at how your checkout dispatches between Juspay and Razorpay, and I got curious about what happens to a card issued in the UK or Australia.
2. You picked up IPL rights for Japan, Hong Kong and Continental Europe this year — did the payment side get revisited when that landed?
3. Roughly a third of your traffic is in markets where you don't hold an entity. I'd be curious whether approval rates there look different from India.

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------------|------------------------|--------|
| ZEE5 / ZEE5 Global | zee5.com | India | India, US, UK, UAE, Gulf, AU, CA | **Not found** — international tier reported credit-card-only | https://helpcenter.zee5.com/portal/en/kb/articles/how-can-i-pay-for-a-zee5-premium-subscription |
| SonyLIV | sonyliv.com | India | India + diaspora | **Gateway not found.** Site strings confirm Paytm wallet + UPI as consumer methods | https://www.sonyliv.com/ (grepped) |
| JioHotstar | jiohotstar.com | India | India + international tiers | **Not found** | https://www.jio.com/jcms/airfiber/ott/hotstar/ |
| Sun NXT | sunnxt.com | India | India, BD, US, CA, EU, SG, MY, LK, AU, NZ, ME, TH | **Not found.** Distributed via Singtel carrier bundle in SG | https://www.singtel.com/personal/products-services/lifestyle-services/cast/sun-nxt |
| aha | aha.video | India | India + NRI (Telugu/Tamil) | **Not found** | — |
| Hoichoi | hoichoi.tv | India | India, BD, US, SEA, ME | **Gateway not found.** Methods: cards, UPI (GPay, PhonePe), location-dependent | https://support.hoichoi.tv/support/solutions/articles/35000132504-what-are-the-different-payment-methods- |
| Chaupal | chaupal.com | India | India + Punjabi/Haryanvi diaspora | **Not found.** Note: Chaupal is a Yupp Video Services *customer* | https://www.chaupal.com/ |

**Method note:** ZEE5 and Hoichoi both return 403 to automated fetching. On SPA-based OTT sites the payment SDK loads only on the authenticated checkout route, so homepage HTML is a weak signal. Confirming competitor stacks requires a real browser session on the subscribe flow.

#### 11B. Industry Peers — same payment shape

| Company | Website | Why Similar (Payment Context) | Source |
|---------|---------|-------------------------------|--------|
| Shahid / Shahid VIP (MBC) | shahid.mbc.net | Arabic content billed across 14+ MENA markets plus US/EU diaspora; solved cross-border collection via a single-API aggregator spanning local carrier-billing rails. **Closest public analogue to YuppTV's problem** | https://www.tpaymobile.com/wp-content/uploads/2024/11/CASE-STUDY_SHAHID-new-version_20241015_single.pdf |
| VMX (ex-Vivamax) | — | Filipino content, large OFW diaspora billed from abroad | https://en.wikipedia.org/wiki/VMX_(streaming_service) |
| Viu (PCCW) | viu.com | Asian content across many SEA markets, distinct local methods each, heavy telco bundling | https://en.wikipedia.org/wiki/Viu_(streaming_service) |
| LycaTV | — | Built for Filipino and African diaspora on Lyca's existing SIM/credit billing rails `[UNVERIFIED]` | https://www.viaccess-orca.com/blog/how-to-succeed-using-ott-tv-services-to-reach-diaspora-populations |

#### 11C. Companies Recently Adopting Payment Orchestration

*"No public case studies found of direct competitors adopting payment orchestration."*

> ⚠️ **Do not recycle this false positive.** A URL exists at
> `zee5.com/articles/juspay-hypercheckout-give-your-customers-an-enhanced-payment-experience-boost-your-conversion`.
> **ZEE5 is the publisher of that article, not its subject.** It is an ANI-syndicated press release dated 19 Oct 2023, republished identically on ThePrint, ANI News and Lokmat Times. It is **not** evidence that ZEE5 uses Juspay. Asserting that in outreach would be a fabricated competitive claim.

Juspay's own public material names Amazon, Ola, Vodafone and Jio. No OTT merchant is publicly named.

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Sun NXT | Direct competitor | India, BD, US, CA, EU, SEA, ME, ANZ | Not scored | — | 12+ market diaspora footprint, Singtel carrier bundle | To check |
| 2 | Hoichoi | Direct competitor | India, BD, US, SEA, ME | Not scored | — | 100+ countries, location-dependent methods | To check |
| 3 | ZEE5 Global | Direct competitor | India, US, UK, Gulf, AU, CA | Not scored | — | International tier reported credit-card-only | To check |
| 4 | aha | Direct competitor | India + NRI | Not scored | — | Regional-language diaspora billing | To check |
| 5 | Shahid (MBC) | Industry peer | MENA + diaspora | Not scored | — | Same cross-border diaspora billing shape | Out of APAC territory |
| 6 | VMX | Industry peer | Philippines + OFW diaspora | Not scored | — | 17M+ users, diaspora billing | To check |

Scores are deliberately blank — none of these was researched to the evidentiary standard this report requires, and a guessed score is worse than none.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | **No consolidated global figure exists publicly** | US entity files nothing |
| Revenue (India entity only) | ₹41.3 Cr FY25, down 19% from ₹51.0 Cr FY24 ≈ US$4.7M | https://inc42.com/company/yupptv/financials/ — **a floor on one entity, not company size** |
| Net loss (India entity) | ₹2.0 Cr FY25; ₹6.9 Cr FY24 | ibid. |
| GMV / Transaction Volume | Not found | — |
| Average Transaction Value | Partial: YuppFlix IAP $3.99–$6.99; Basic+Cricket $12.99; international ~$79.99/yr `[UNVERIFIED]`; India entry ₹49/mo `[UNVERIFIED]` | apps.apple.com · secondary sources |
| Est. Annual Transactions | **Not calculable** — no subscriber count and no reliable revenue base | — |
| Active Customers / Users | Not found. "13 million mobile downloads" is an undated company download metric, **not subscribers** | https://www.yupptv.com/help/about |
| Primary Currency | USD for activation fees (confirmed); INR for India plans; T&Cs say rates "vary from country to country" | https://www.yupptv.com/help/terms-and-conditions |
| Total funding | $67.7M across 4 rounds `[UNVERIFIED]`; conflicting $58M figure. Last round Series B $50M, Oct 2016, Emerald Media | https://www.crunchbase.com/organization/yupptv |
| Billing channel split (web vs app store vs telco) | **Not quantified anywhere. The single most decision-relevant unknown** | — |

**Fee stack beyond the subscription price, verbatim from T&Cs:** account activation ~$10, non-refundable, **charged every year on renewal**; device activation ~$10 one-time; concurrent-device ~$20 plus $2.99/month. **Discrepancy:** Apple's live IAP tiers list device activations at $1.99–$2.99, not ~$10. Unreconciled — a question for a call, not an assertion in an email.

*"No public revenue/GMV data found at group level. Business case sizing will require a discovery call."*

---

### Overall Research Confidence

**Medium-High.**

**Strong coverage:** the payment stack (§3) is the best-evidenced section — Juspay and Razorpay come from YuppTV's own shipped production code, which is primary evidence of the highest quality available without a merchant conversation. Legal entities (§2) are quoted verbatim from the company's own T&Cs. Corporate developments (§6) are dated and press-released.

**Weak coverage:** payment methods outside India (§4) — the checkout is client-rendered and login-gated, so no accepted-methods list could be obtained and no rail gap could be confirmed in any market. Complaints (§5) rest on App Store reviews that stop at January 2024, with Trustpilot and BBB both 403-blocked. Competitor stacks (§11A) are entirely unresolved.

**Traffic data was SUPPLIED** by Prateek from SimilarWeb (Jun–Aug 2026), not API-sourced or estimated, and was independently corroborated as complete since no other YuppTV domain resolves. Country shares are reliable; absolute visit volumes were not in the supplied view.

**The decisive unknown is the billing-channel split.** Everything in §10 assumes a materially sized direct-billed book. That assumption is well supported (two production checkout routes; complaint patterns that can only describe direct billing) but unquantified.

---

### Manual Research Recommendations

> **Area:** Which gateway serves which geography (§3B)
> **Why it matters:** The entire pitch rests on Indian gateways carrying international cards. If Juspay already fans out to international acquirers server-side, Insight #1 collapses.
> **Suggested manual action:** Open `/allpackages` with DevTools from an India IP and again from a UAE or UK IP. Watch the `POST prod-api.yupptv.com/payment/api/v1/order/checkout` response and compare the `gateway` value and the rendered method set. This single test is worth more than another full research run.

> **Area:** Billing-channel split — web vs Apple/Google/Roku vs telco (§12)
> **Why it matters:** Determines whether the account is worth a full sequence. Orchestration addresses only the web-checkout share.
> **Suggested manual action:** Ask directly on the first call. Frame it as scoping, not qualification: *"how much of your subscriber book bills through your own checkout versus the stores and the operator bundles?"*

> **Area:** Which entity invoices which subscriber (§2)
> **Why it matters:** The T&Cs name both entities and apply Georgia law throughout, with no India carve-out. Merchant of record determines acquiring geography.
> **Suggested manual action:** Subscribe from an Indian card and a non-Indian card, and read the descriptor on each statement.

> **Area:** Non-India payment methods (§4)
> **Why it matters:** Not a single rail gap outside India could be confirmed, so no coverage claim can be made in outreach.
> **Suggested manual action:** VPN checkout walkthrough from UAE, US and UK. Record the method set each market is shown.

> **Area:** Competitor payment stacks (§11A)
> **Why it matters:** The competitive-urgency angle is unavailable without one confirmed competitor stack.
> **Suggested manual action:** A real browser session on ZEE5 and Hoichoi subscribe flows — both bot-block automated fetching, and homepage HTML does not load the payment SDK.

---

### Appendix: All Source URLs

**Company primary sources**
- https://www.yupptv.com/help/terms-and-conditions
- https://www.yupptv.com/help/privacy-terms
- https://www.yupptv.com/help/about
- https://www.yupptv.com/_next/static/x9RG7ENCJOWrqzhasQoOf/_buildManifest.js
- https://www.yupptv.com/_next/static/chunks/pages/buy/juspay/%5B...index%5D-6d6c11bf7e3f0562.js
- https://www.yupptv.com/_next/static/chunks/pages/buy/razorpay/%5B...index%5D-175d0d89a5e67f00.js
- https://www.yupptv.com/Devices/Roku · https://blog.yupptv.com/2026/03/yupptv-bags-tata-ipl-2026-streaming-rights.html

**Registries & financials**
- https://www.zaubacorp.com/YUPPTV-INDIA-PRIVATE-LIMITED-U72200TG2007PTC054335
- https://www.zaubacorp.com/YUPPTV-DIGITAL-INDIA-PRIVATE-LIMITED-U22300TG2019PTC137791
- https://opencorporates.com/companies/us_wv/358447 · https://inc42.com/company/yupptv/financials/
- https://www.crunchbase.com/organization/yupptv · https://en.wikipedia.org/wiki/YuppTV

**Distribution & billing channels**
- https://apps.apple.com/us/app/yupptv-live-tv-movies/id665805393 · https://support.roku.com/article/36296801163799
- https://pt6.etisalat.ae/dcb-digital/landindex?id=7&type=132gff&txnid=y&banner=etisalat&lang=en
- https://www.du.ae/about/media-centre/newsdetail/du-launches-strategic-partnership-with-yupptv
- https://unifi.com.my/sites/default/files/html/plus-box/doc/FAQ-YuppTV-ver4a_14June2021.pdf
- https://telecomtalk.info/bsnl-yupptv-scope-subscription-costs-rs-199-per-month-after-introductory-offer/345284/
- https://www.myvi.in/blog/get-yupptv-subscription · https://play.google.com/store/apps/details?id=com.yupptv.ooredooapp

**Corporate developments**
- https://www.prnewswire.com/news-releases/yupptv-secures-digital-telecast-rights-for-asia-cup-2025-302554070.html
- https://www.prnewswire.com/news-releases/yupp-video-services-partners-with-get-after-it-media-to-launch-heartland-302656422.html
- https://www.prnewswire.com/news-releases/yupp-video-services-powers-chaupals-full-scale-technology-upgrade-strengthening-platform-reliability-performance-and-user-experience-across-25-devices-302637692.html

**Complaints**
- https://justuseapp.com/en/app/665805393/yupptv-live-tv-movies/reviews
- https://www.trustpilot.com/review/www.yupptv.com *(403 — unread)*
- https://www.bbb.org/us/ga/alpharetta/profile/cable-internet-and-radio/yupptv-usa-inc-0443-27306026/complaints *(403 — unread)*

**Competitors**
- https://helpcenter.zee5.com/portal/en/kb/articles/how-can-i-pay-for-a-zee5-premium-subscription
- https://support.hoichoi.tv/support/solutions/articles/35000132504-what-are-the-different-payment-methods-
- https://www.singtel.com/personal/products-services/lifestyle-services/cast/sun-nxt
- https://www.tpaymobile.com/wp-content/uploads/2024/11/CASE-STUDY_SHAHID-new-version_20241015_single.pdf
- https://juspay.io/in/products

</details>
