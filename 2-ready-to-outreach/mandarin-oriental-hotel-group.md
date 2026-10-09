# Mandarin Oriental Hotel Group

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 17 / 29 → 🟢 **Medium** *(computed 17 = ⭐; analyst override applied downward — see breakdown)*
**Industry:** Ultra-luxury hotel management, branded residences and villa rentals · **HQ:** Mandarin Oriental Hotel Group Limited, 8th Floor, One Island East, Taikoo Place, 18 Westlands Road, Quarry Bay, Hong Kong · parent Mandarin Oriental International Limited (Bermuda), 100%-owned by Jardine Strategic Limited since 19 Jan 2026 · **Researched:** 2026-10-09 · **First email sent:** —
**Motion:** 🛠️ **IN-HOUSE — Mandarin Oriental owns its own card vault (Very Good Security) and a per-property payment-method matrix it built itself.** Never tell them they need orchestration. Anchor on the fact that the central tier they built captures cards but does not settle them.

---

> ## ⭐ THE FINDING — the central stack captures a card guarantee. It does not settle the money. And the settlement capability they built is switched OFF at all 48 properties.
>
> I pulled `https://www.mandarinoriental.com/en` and its application bundle `https://www.mandarinoriental.com/corporate/main.js?v=2.42.0-beta.1-30` myself on 2026-10-09 (both HTTP 200; 1,392,974 and 3,334,390 bytes). The homepage embeds a production configuration object for **48 properties**. For **every single one of the 48**, verbatim:
>
> ```
> "enablePlanetPaymentForBooking": false,
> "enablePlanetPaymentForFanClub": false,
> "enablePlanetPaymentWithAuthorize": false,
> "enablePlanetPaymentWithoutAuthorize": false,
> "redirectPaymentMethodsForRoomBooking": []
> ```
>
> The bundle shows what those flags gate. There are **two mutually exclusive card paths**, and the switch is per property:
>
> ```js
> isUsingVgs: function(){ return "" !== this.vgsBaseUrl },
> enablePlanetPayment: function(){ return !this.isBookingEditMode && ((this.isFanClubBooking
>     ? selectedHotel?.enablePlanetPaymentForFanClub
>     : selectedHotel?.enablePlanetPaymentForBooking) && "" !== this.planetPaymentScript) },
> isPaymentFormInvalid: function(){ return !this.isDirectBill &&
>     (this.enablePlanetPayment ? !this.planetPaymentValidationStatus : this.isVgsFormInvalid) }
> ```
>
> **Path A — Planet Payment / Datatrans Secure Fields.** A complete, built, production-grade acceptance path: `initializeTransaction`, `skipAuthorize`, `datatransCode`, `datatransTrxId`, `secureFields.submit({expm, expy, "3D": threeDSecureData})`, a full EMV 3DS2 cardholder-data object, redirect-APM handling, orphan-reservation cleanup, and seven localised Planet error strings. **Disabled at all 48 properties.**
>
> **Path B — Mandarin Oriental's own Very Good Security vault.** This is what actually runs today. The bundle carries a Vue component literally named **`VgsForm`**, loads `https://js.verygoodvault.com` / `js3.verygoodvault.com`, calls `VGSCollect.create(vaultId, environment)`, logs `tokenizedData:`, and throws `"Error: VGS not implemented!"` if the vault is missing. The **live** vault config is in the bundle in clear:
>
> ```js
> { name: "production", vaultId: "***(vault id redacted)", environment: "live",
>   endpoint: "vgs-live.sitecore.moweb-acc.com" }
> ```
>
> Corroborated by the response headers on `www.mandarinoriental.com`, which allow the `vgs-client` request header and CORS origins `*.verygoodvault.com` and `*.verygoodproxy.com`.
>
> **And the per-property booking terms in the same config say exactly what happens to that card.** Verbatim, from Mandarin Oriental's own `restrictionPolicy` strings:
>
> | Property | Market | Own words |
> |---|---|---|
> | **Tokyo** | Japan (7.28%, #2) | *"A credit card is required at time of booking; **no charges will be made until check-out**."* |
> | **Hong Kong (Mandarin Oriental)** | HK (4.93%) | *"A credit card **for guarantee** is required at time of booking."* |
> | **Taipei** | Taiwan (3.69%) | *"A credit card is required at the time of booking."* |
> | **Jakarta** | Indonesia (3.64%) | *"A credit card is required at time of booking; **no charges will be made until check-out**."* |
> | **Singapore** | SG | *"A credit card is required at time of booking; **no charges will be made until check-out**."* |
> | **Shanghai / Sanya / Guangzhou / Macau / Beijing-Wangfujing** | Greater China | same — *"no charges will be made until check-out"* |
> | **Shenzhen** | China | *"Deposit by cash or credit card will be required **upon check in**."* |
>
> **THE ANSWER TO THE SETTLEMENT QUESTION: the card settles PER PROPERTY, at check-out, not centrally at booking.** `mandarinoriental.com` tokenises the card into Mandarin Oriental's own VGS vault, hands it to the SynXis CRS as a **guarantee on the reservation**, and the money is taken later at the property through the property's own hotel system. The bundle confirms the property-system handoff: the localisation key `modifyUseOperaHmsMessage` reads *"Please contact the hotel directly for any modifications or cancellations."* — an **Oracle OPERA HMS** code path where the central site cannot even modify the booking, let alone bill it.
>
> **This is the fact that decides the account, and it cuts both ways.** There IS a central tier, and Mandarin Oriental built and owns it. But it is an **authorisation and custody tier, not a settlement tier**. The orchestratable central card volume today is a small fraction of what 1.265M monthly visits implies, and the acquirer sits with the property owner in each country.
>
> ⚠️ **What this does NOT establish, and I will not claim:** the acquirer. **No acquirer for any Mandarin Oriental property is disclosed anywhere I could reach.** Zero evidence for Adyen, Worldpay, Cybersource, Braintree, Checkout.com, Global Payments, Elavon, Shift4 or any local APAC acquirer against this merchant. Datatrans/Planet is the *built* gateway and is **off**; the property-level acquirers behind OPERA are **not established**. Treat the acquirer as a discovery question, not a research failure.

---

> ## 🎯 THE HOOK — the four prepay properties, and what they are missing
>
> The guarantee-only model is not universal. Four properties in the same config **do take money at booking**, in their own words:
>
> - **Beijing – Qianmen:** *"**Full prepayment is required at time of booking.**"*
> - **Kuala Lumpur:** *"**Full payment is required.** No refunds or amendments permitted. … If payment is unsuccessful within 48 hours of making the reservation, the hotel reserves the right to cancel the reservation."*
> - **Bangkok:** *"State Rooms & Suites: 1 night deposit required."*
> - **Lucerne:** *"All reservations must be guaranteed with deposit at time of booking."*
>
> Those four need a real settled transaction. And for those four, `redirectPaymentMethodsForRoomBooking` is **`[]`** — same as everywhere else. **A Beijing property that demands full prepayment at booking, with no Alipay, no WeChat Pay and no UnionPay enabled on the checkout.** The capability is in the code: the bundle carries Datatrans method codes `"ALP"`, `"APL"`, `"PAY"`, `"VIS"`, `"ECA"`, `"AMX"`, `"DIS"` and a card-brand map including `unionpay:"UP"`, `chinaUPe:"CU"`, `japCB:"JC"`. It is written, and it is switched off.
>
> That is not a hypothetical rail gap. It is Mandarin Oriental's own configuration, on both sides of the sentence, with a 48-hour kill clause on a failed payment in Kuala Lumpur.
>
> Pair it with the second hook, which is narrower and impossible to argue with:
>
> **The gift-card store takes cards only, in four currencies, and none of them is the yen.** `giftcards.mandarinoriental.com` is a live **Stripe** merchant (details below). Its footer shows exactly three payment marks — **Amex, Visa, Mastercard** — and its currency selector offers exactly **EUR, GBP, HKD, SGD**. No JPY, no TWD, no IDR, not even USD. Japan is Mandarin Oriental's second-largest traffic market at 7.28% and the United States its largest at 18.63%.

---

> ## ✅ Orchestrator audit — 2026-10-09. **Headline verified exactly. Two redactions. One correction to my own brief.**
>
> ### 🔒 Redactions
> This file carried **Mandarin Oriental's live Stripe publishable key**, their **Stripe Connect
> account id**, and their **VGS vault id** verbatim. All three are redacted. A `pk_live_` key is
> browser-visible by design, but **this repository has a public remote** and copying a third party's
> live payment identifiers into a public document gains us nothing. The findings do not depend on the
> values: *Stripe is live on the gift-card store* and *MO runs its own VGS vault* are both established
> by the vendor names and the `vgs-live` endpoint, which are recorded.
>
> ### The headline, re-verified by me — and it is exact
>
> I fetched `mandarinoriental.com` myself, HTML-decoded the embedded property config, and counted
> every flag:
>
> | Flag | Count | Values |
> |---|---|---|
> | `enablePlanetPaymentForBooking` | **48** | **`false` × 48** |
> | `enablePlanetPaymentForFanClub` | **48** | **`false` × 48** |
> | `enablePlanetPaymentWithAuthorize` | **48** | **`false` × 48** |
> | `enablePlanetPaymentWithoutAuthorize` | **48** | **`false` × 48** |
> | `redirectPaymentMethodsForRoomBooking` | **48** | **`[]` — one distinct value** |
>
> **192 gateway flags across 48 properties, every single one false, and not one payment method enabled
> anywhere.** The complete Planet/Datatrans path exists in the bundle and is switched off everywhere.
> `main.js?v=2.42.0-beta.1-30` confirmed at `/corporate/main.js`.
>
> ### 🚩 NEW ENVIRONMENT TRAP — add to the repo's list
>
> **The config is HTML-entity-encoded in the page source.** The keys appear as
> `&quot;enablePlanetPaymentForBooking&quot;:false`, **double-encoded**. My first grep for
> `enablePlanetPaymentForBooking":false` returned **0** and I nearly recorded the headline as
> unreproducible. A grep for the bare key returned 48. **`html.unescape()` twice, then match.**
> This is the same silent-failure family as `grep -P` returning 0, CloudFront Brotli, and FWD's
> client-rendered `__NEXT_DATA__`.
>
> 🚩 Also logged: **`planet` returns 199 hits and 192 of them are these flags** — but on a hotel site
> "planet" is equally likely to be sustainability copy, so the raw count means nothing without
> context. Check before reporting.
>
> ### ⚠️ A correction to MY OWN brief, not the agent's work
>
> **I told the research agent that "Mandarin Oriental International Limited is listed (Singapore/London
> — verify which and the ticker)." That was wrong, and the agent caught it.** MOIL **was** listed
> (primary LSE, secondary SGX `M04` and BSX) but **Jardine Strategic took it private for ~US$4.2bn** —
> scheme sanctioned 16 Jan 2026, completed 19 Jan 2026, **listings cancelled on all three exchanges on
> 20 Jan 2026**. **FY2024 is the last complete public financial picture.** Credit to the agent for
> checking the instruction instead of following it.
>
> ### What I did NOT re-verify
> The per-property terms quotes, the ~25-entity Jardine chain, the gift-card Techsembly stack, and the
> residences finding all stand as the agent sourced them.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Mandarin Oriental is an ultra-luxury hotel **management** company — asset-light by design, not a hotel owner at scale. As at the 2025 full-year release it operated **45 hotels, 15 branded residences and 36 Exceptional Homes across 28 countries and territories**, while **owning or part-owning only 12 hotels**. Its parent, Mandarin Oriental International Limited (MOIL, Bermuda), was taken private by Jardine Strategic Limited on **19 January 2026** and delisted from London, Singapore and Bermuda. Hotel operations are managed from Hong Kong by Mandarin Oriental Hotel Group Limited.

**SimilarWeb total visits (last full month):** **1.265M** (`mandarinoriental.com`, Sep 2026, ▲1.16% MoM; desktop 36.24% / mobile web 63.76%) — **source: supplied by Prateek**, SimilarWeb PRO (supplied 2026-10-09). Single domain, no corporate/booking split. Not re-researched.

### ⚠️ Read the money before the traffic
| Metric | Value | What it is | Source |
|---|---|---|---|
| **Combined total revenue of hotels under management (FY24)** | **US$2,127.7m** (+13%) | **NOT MOIL's revenue.** Turnover of subsidiary hotels **plus 100% of revenue from associate, JV and managed hotels** — i.e. mostly third-party owners' money | MOIL FY24 RNS |
| **MOIL reported revenue (FY24)** | **US$525.8m** (−6% from US$558.1m) | What MOIL actually books | MOIL FY24 RNS |
| Underlying EBITDA (FY24) | US$172.0m (−3%) | | MOIL FY24 RNS |
| Underlying profit attributable to shareholders (FY24) | US$74.7m (−8%) | | MOIL FY24 RNS |
| **Loss attributable to shareholders (FY24)** | **US$(78.6)m** | After a US$171.0m investment-property revaluation loss on One Causeway Bay | MOIL FY24 RNS |

**The target list's "~$2B (FY24)" is the combined managed-hotel figure, not Mandarin Oriental's revenue.** It overstates the contracting entity's size by roughly **4×**. Source: [MOIL 2024 Preliminary Announcement of Results, RNS 5036Z, 5 March 2025](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf).

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇺🇸 United States | 18.63% | Cards via VGS capture (guarantee only, per-property terms) | Everything else — `redirectPaymentMethodsForRoomBooking: []` at Boston & New York | ✅ Mandarin Oriental Management (USA) Inc.; Residences at Mandarin Oriental Management (Fifth Avenue) LLC |
| 2 | 🇯🇵 **Japan** | **7.28%** | Cards via VGS capture; Tokyo terms = *"no charges will be made until check-out"* | **konbini, PayPay, LINE Pay, Rakuten Pay, carrier billing, Paidy, domestic instalments — none enabled** (`[]` for Tokyo, id 558); no JPY on the gift-card store | ⚠️ **Japan is listed as a territory in the privacy policy but NO local management entity is named for it**, unlike 22 other markets |
| 3 | 🇧🇷 Brazil | 6.04% | Cards via VGS capture | **Pix and domestic instalments not enabled** (`[]`; no Brazilian property in the 48-property config at all) | ❌ No Brazilian entity named; no Brazilian property — this is pure inbound demand |
| 4 | 🇦🇪 United Arab Emirates | 5.77% | Cards via VGS capture; Dubai & Abu Dhabi terms = credit-card guarantee | n/a | ✅ Mandarin Oriental Dubai (BVI) Limited; Mandarin Oriental Abu Dhabi (BVI) Limited — **⚠️ EMEA territory, not APAC. Excluded from the pitch.** |
| 5 | 🇬🇧 United Kingdom | 5.01% | Cards via VGS capture | Open Banking / Pay by Bank not enabled | ✅ Mandarin Oriental Hyde Park Limited; Mandarin Oriental (UK) Limited; Mandarin Oriental Residences Management (UK) Limited |

**APAC markets further down the table:** 🇭🇰 Hong Kong 4.93% (⚠️ home market, **FPS and Octopus not enabled**), 🇹🇼 Taiwan 3.69% (**JKOPay, LINE Pay, ATM/virtual account, convenience-store cash, domestic instalments — none enabled**), 🇮🇩 Indonesia 3.64% (**QRIS and virtual account not enabled**). APAC visible total **19.54%**.

> **Note the shape.** Nothing above 18.63%, and the home market is sixth at 4.93%. There is **no single market to anchor a rail-gap argument on.** The honest framing is corridor breadth, not one missing rail.

### Legal entities
Per the Mandarin Oriental privacy policy (effective **10 April 2026**), `https://www.mandarinoriental.com/en/privacy-policy`, which names the local management entity per market:

- **Mandarin Oriental International Limited** (Bermuda) — parent holdco; **delisted 19–20 Jan 2026**; 100% Jardine Strategic Limited
- **Jardine Strategic Limited** (Bermuda) — parent company of the Group
- **Jardine Matheson Holdings Limited** (Bermuda) — ultimate holding company
- **Mandarin Oriental Hotel Group Limited** (Hong Kong) — the management company and Hong Kong data controller; *"the activities of the Group's hotels are managed from Hong Kong"*
- Mandarin Oriental (Shanghai) Hotel Management Company Limited (**China**)
- **P.T. MO Management Indonesia** (Indonesia)
- **MOHG Management (Singapore) Pte Limited** (Malaysia **and** Singapore — one entity for two markets)
- **Mandarin Oriental Services Limited** + Taiwan Mandarin Oriental Residences Management Maintenance Company Limited (**Taiwan**)
- **Mandarin Oriental (Thailand) Limited** (Thailand)
- Mandarin Oriental Residences Management (Macau) Limited (**Macau**)
- Mandarin Oriental Abu Dhabi (BVI) Limited · Mandarin Oriental Dubai (BVI) Limited · Mandarin Oriental Hotel Management (BVI) Limited (Italy)
- Mandarin Oriental Austria GmbH · Mandarin Oriental (Chile) SpA · Mandarin Oriental Prague S.R.O. · MOHG Hotel (Paris) SARL · Mandarin Oriental Munich GmbH · Mandarin Oriental (UK) Limited (also Greece) · Mandarin Oriental Holdings B.V. (Netherlands) · Mandarin Oriental Spain SL · Mandarin Oriental Residences Spain SL · Mandarin Oriental (Switzerland) SA · Société pour l'Exploitation de Mandarin Oriental (Genève) SA · MO Management SARL (Morocco) · Mandarin Oriental Otelcilik Limited Şirketi + MO Rezidans Hizmetleri Limited Sirketi (Turkey) · Mandarin Oriental Hyde Park Limited · Mandarin Oriental Residences Management (UK) Limited · Mandarin Oriental Management (USA) Inc. · Residences at Mandarin Oriental Management (Fifth Avenue) LLC

**Registration numbers: not found.** No registry filing was retrieved for any of these entities in this run.

### Known PSPs
- **Very Good Security (VGS)** — `[Source Code]` live vault `***(vault id redacted)`, environment `live`, reverse proxy `vgs-live.sitecore.moweb-acc.com`, `VgsForm` component, `vgs-client` header allowed. **This is the live card-capture and tokenisation tier for room booking, all markets.**
- **Datatrans (part of the Planet group)** — `[Source Code]` + `[Checkout]` `pay.datatrans.com` and `pay.sandbox.datatrans.com` explicitly allowlisted in the live CSP `default-src` and `script-src`; `datatransCode`, `datatransTrxId`, `secureFields.submit()` in the bundle. **Integrated but disabled at all 48 properties.**
- **Stripe** — `[Source Code]` **LIVE** publishable key `pk_live_**********(redacted)` and Stripe Connect standard account `acct_**********(redacted)`, statement descriptor suffix `"Mandarin Oriental"`, on `giftcards.mandarinoriental.com` via the **Techsembly** SaaS storefront. Gift cards and shop only.
- **SevenRooms** — `[Source Code]` dining reservations at Tokyo and Hong Kong run off-domain on `www.sevenrooms.com` with MO venue slugs (`motyokshiki`, `motyosense`, `mandarinbar`, `mandaringrillbarmohkg`). A separate payment surface for dining deposits.
- **Givex** — `[Source Code]` `givex_multi_currency: false` in the gift-card store config. Stored-value platform, present, multi-currency off.
- **Adyen** — `[Source Code]` `adyenOriginKey: ""` on the Techsembly gift-card store. The platform supports Adyen; **it is empty for Mandarin Oriental.** This is a negative, not a finding of use.
- **Acquirers: NOT ESTABLISHED.** No acquirer is named for any property, central or local. A deliberate blank.

### Orchestration status
**In-house orchestration layer.** No third-party orchestrator was found anywhere — zero evidence of Juspay, Spreedly, Primer, Gr4vy, CellPoint Digital, APEXX, Payrails or Yuno across the live CSP, response headers, the 3.3MB application bundle, the gift-card store config, the SynXis booking-engine CSP, or any press or filing. What Mandarin Oriental has instead is **its own merchant-side tier**: a VGS vault it controls, a per-property enable matrix for a second gateway, a per-property `redirectPaymentMethodsForRoomBooking` array, and a `skipAuthorize` flag per method. That is routing and method-selection logic the merchant built. **Treat this as in-house, not greenfield. Do not tell them they need orchestration — they built a version of it.** (`[Source Code]`, `main.js?v=2.42.0-beta.1-30`, fetched 2026-10-09.)

### Buying signals
- 🏦 **Taken private and delisted.** Jardine Strategic acquired the 11.96% it did not own; total value ~**US$4.2bn**; US$2.75 cash + US$0.60 special dividend = US$3.35/share; announced **17 Oct 2025**, completed **19 Jan 2026** by Bermuda scheme of arrangement; listings cancelled on **London, Singapore and Bermuda** on 20 Jan 2026. ([Slaughter and May](https://www.slaughterandmay.com/recent-work/mandarin-oriental-transaction-committee-on-the-recommended-cash-acquisition-by-jardine-updated/), [Conyers](https://www.conyers.com/publications/view/mandarin-oriental-international-limited-privatisation-and-delisting/), [cancellation RNS](https://www.investegate.co.uk/announcement/rns/jardine-matheson-holdings-ltd-singapore-reg---jar/cancellation-of-the-listings-of-mandarin-oriental/9369226)) **A 100%-owned subsidiary with no public shareholders and a stated doubling target is the window for infrastructure decisions.**
- 🚀 **Stated intent to more than double the portfolio by 2033**, with **30+ signed hotel and branded-residence projects to open over the next six years**. ([MOIL FY24 RNS](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf), [FY25 release](https://press.mandarinoriental.com/annual-results-2025/?lang=eng))
- 🚀 **New APAC markets landing now:** Mandarin Oriental Makati, Manila opens **late 2026** (275 rooms, five F&B concepts, with Ayala Land) — the brand's return to the Philippines after 2014. Hangzhou **Spring 2027**, Cortina **2027**, Suzhou in pipeline. ([Ayala Land](https://ayalaland.com/news/ayala-land-and-mandarin-oriental-officials-visit-new-mandarin-oriental-site-on-the-road-to-opening-in-2026), [TTG Asia](https://www.ttgasia.com/2024/04/29/new-mandarin-oriental-to-open-in-philippines-makati-city-in-2026/), MO site navigation)
- 💼 **"Investing in capability now to achieve long-term targets and sustain accelerated growth"** — a FY24 results headline bullet, in their own words. ([MOIL FY24 RNS](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf))
- 🤝 **Asset-light pivot is live:** Paris property sold for US$382m (2024), Miami disposed and Munich agreed for sale (H1 2025) with long-term management agreements retained. **Every disposal moves a folio from "our acquirer" to "the owner's acquirer."** ([MOIL FY24 RNS](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf), [H1 2025](https://sg.finance.yahoo.com/news/mandarin-oriental-reports-higher-underlying-035816370.html))

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Mandarin Oriental Hotel Group` to draft the 12-touch sequence, or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 17 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+3** | ⚠️ **NOT FOUND — ASSUMED ~90,000 folios/month group-wide. `[ASSUMPTION — not researched.]`** See the mandatory disclosure below. **Billing unit: guest folios at property level** — not room nights, not guests, not visits. An assumed figure **cannot** fire the under-40,000 rejection, and it has not. |
| Orchestration status | **+1** | ✅ **In-house orchestration layer confirmed.** Merchant-owned VGS vault (`vaultId: ***(vault id redacted)`, `environment: live`), per-property gateway enable matrix, per-property redirect-method array, per-method `skipAuthorize`. No third-party orchestrator anywhere. `[Source Code]` `main.js?v=2.42.0-beta.1-30`. **+1, not +4** — this is not greenfield. |
| 3+ countries | **+3** | ✅ **Verified, double-sourced.** Ten countries above 1% traffic share (SimilarWeb supplied 2026-10-09) **and** 25+ named local management entities across 23 markets (privacy policy, eff. 10 Apr 2026). |
| Multiple PSPs | **+3** | ✅ **Verified, 2+ with first-hand evidence.** Stripe **live** on `giftcards.mandarinoriental.com` (`pk_live_…`, `acct_**********(redacted)`); VGS **live** vault on `mandarinoriental.com`; Datatrans/Planet integrated. Three distinct providers, three distinct surfaces. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Absence sourced first-hand from the merchant's own production config.** `redirectPaymentMethodsForRoomBooking: []` for **Tokyo (id 558)** — Japan is the #2 traffic market at 7.28%. Zero konbini, PayPay, LINE Pay, Rakuten Pay, Paidy, carrier billing or domestic instalments enabled. Reinforced by the gift-card store offering no JPY. ⚠️ **Caveat stated honestly: I sourced the ABSENCE, which is what this row tests. I did not source a primary citation for those rails' share of Japanese e-commerce in this run** — so the warning language in Section 4 is deliberately restrained. |
| Recent expansion | **+2** | ✅ **Verified, within 12 months.** FY2025 release (16 Mar 2026): two hotels opened, three rebrandings, five new destinations, now 45 hotels / 15 residences / 36 Exceptional Homes in 28 countries, 30+ signed projects over six years. Manila Makati opening late 2026. |
| Payment issues reported | **0** | ❌ **Not met.** No payment-related complaints found on Reddit, Trustpilot, app stores or X. A searched-and-found-nothing zero, not an unexamined one. (The bundle does contain `cancelOrphanReservation` and `cancelReservationOnFailedRedirect` — engineering evidence that failed redirect payments orphan reservations — but that is code, not a customer complaint, and I am not scoring it.) |
| Funding >$10M | **0** | ⬜ **Deliberately not awarded.** There IS a US$4.2bn capital event in the window — the Jardine Strategic take-private completed 19 Jan 2026 — but **a buyout is not a funding round into the business.** No capital was raised by Mandarin Oriental. Scoring this would be inflating the row. It is carried as the #1 buying signal instead. |
| High traffic outside home | **+2** | ✅ **Verified.** Home market Hong Kong is **4.93%** of traffic — sixth place, and 55 points below the 60% threshold. |
| Competitor using orchestration | **0** | ⬜ **Not established.** I probed eight luxury peers' live sites directly. **Aman (4 refs) and Banyan Tree (9 refs) both run the same SynXis booking engine as Mandarin Oriental.** No orchestrator at any. Peninsula, Four Seasons and Capella returned HTTP 403 to my fetches, so those three are **unexamined, not clean** — a weak negative, stated as such. |
| Payment job postings | **0** | ❌ **Not met.** No Mandarin Oriental payments, e-commerce or payment-engineering role found. |

**Tier:** computed **17/29 → ⭐ High Priority (17+)**.

> **🔻 ANALYST OVERRIDE APPLIED — downgraded to 🟢 Medium. Reasoning in full:**
>
> 1. **The matrix is double-counting a thin base.** "3+ countries" (+3) and "high traffic outside home" (+2) both fire off the same single SimilarWeb country table — five points from one artefact. "Multiple PSPs" (+3) fires substantially off a **gift-card microsite**, which is a marketing line, not the core business.
> 2. **The absolute central settlement volume may be close to zero.** This is the decisive point. The brand.com flow captures a card **guarantee**, not a charge, at 44 of 48 properties in Mandarin Oriental's own words. Settlement happens at the property, at check-out, through Oracle OPERA and the owner's acquirer. There is no confirmed central settlement volume for Yuno to orchestrate, and only four properties in the entire portfolio take money at booking.
> 3. **The contracting entity is a quarter of the size the target list implies.** MOIL books **US$525.8m**, not US$2.1bn. ~75% of guest spend across the estate belongs to third-party hotel owners and never crosses MOIL's P&L — so even the owner-side volume is not Mandarin Oriental's to contract for.
> 4. **The buyer may not be reachable through this account at all.** If the acquiring relationship sits with each owner's operating company, the central commercial team at MOHG Hong Kong cannot sign for it.
>
> 17 sits exactly on the ⭐ boundary. On this evidence it does not deserve the benefit of that boundary. **🟢 Medium, worth a call, with the settlement question as the only thing that call needs to answer.** It converts to ⭐ the moment someone confirms that MOHG is turning Planet Payment on, or that central prepay is expanding beyond four properties.
>
> **No public payment RFP was found, so no RFP override applies.**

### Monthly transaction count — mandatory disclosure

⚠️ **NOT FOUND — ASSUMED ~90,000 guest folios/month group-wide. `[ASSUMPTION — not researched.]`**

**Case: ASSUMED.** Mandarin Oriental publishes **no** booking count, folio count, room-night count or transaction count. I checked the FY2024 preliminary results RNS in full, the FY2025 results release, and the H1 2025 release. None discloses a volume metric. Nor could I soundly derive one: MOIL publishes RevPAR (FY24: Asia **US$242**, America **US$434**) but not the room inventory and occupancy inputs needed to convert that into folios, so any derivation would rest on an unsourced key count — which the rules correctly call an assumption no matter how careful the arithmetic.

**Basis for the assumption, shown so it can be attacked:** 45 hotels (sourced, FY25 release) × an assumed ~250 keys per ultra-luxury property (**unsourced** — anchored loosely on Manila Makati's 275 rooms, which IS sourced) ≈ 11,250 keys; × an assumed ~67% occupancy ÷ an assumed ~2.5-night average stay ≈ ~3,000 folios/day ≈ **~90,000 folios/month**. **Three of those four inputs are my assumptions.**

**State the billing unit, and then read it carefully.** The honest unit for a hotel group is the **guest folio** — one settled bill per stay — not room nights and not guests. But for this merchant the unit has to be narrowed twice more before it means anything to Yuno:

1. **Only ~12 of 45 hotels are MOIL-owned.** The remaining ~33 are managed for third-party owners, whose operating companies are the merchant of record.
2. **`mandarinoriental.com` is one channel among GDS, OTA, travel agent, corporate and telephone.** Only a fraction of folios originate there.
3. **And a brand.com booking is not a transaction at all at 44 of 48 properties** — it is a card guarantee. The money moves later, at the property.

**Therefore: the group-wide folio count comfortably clears 40,000, but the count of transactions settled through any stack Yuno could orchestrate is NOT ESTABLISHED and may today be close to zero.** I am scoring the band the assumption implies (**+3**, 50,000–99,999) and marking the row ⚠️. **Confirm the real settled-transaction count** is the #1 item in Manual Research Recommendations.

### Source Notes
- ✅ Per-property payment config for all 48 properties, all flags `false`, all redirect-method arrays empty — first-hand, `https://www.mandarinoriental.com/en`, HTTP 200, 1,392,974 bytes, fetched 2026-10-09 00:15 UTC. **Asset re-fetched this run; nothing reused from any prior scratchpad.**
- ✅ VGS live vault, Datatrans Secure Fields, Planet Payment gating logic, 3DS2 data object — first-hand, `https://www.mandarinoriental.com/corporate/main.js?v=2.42.0-beta.1-30`, HTTP 200, 3,334,390 bytes, fetched 2026-10-09 00:19 UTC.
- ✅ Live Stripe key and Connect account on the gift-card store — first-hand, `https://giftcards.mandarinoriental.com/egift-card-031505`, HTTP 200.
- ✅ MOIL FY24 financials, entity chain, Owned-Hotels count, residences-as-branding-fees, geographic revenue split — [MOIL 2024 Preliminary Announcement of Results, RNS 5036Z, 5 Mar 2025](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf).
- ✅ Take-private and delisting — [Slaughter and May](https://www.slaughterandmay.com/recent-work/mandarin-oriental-transaction-committee-on-the-recommended-cash-acquisition-by-jardine-updated/) (adviser to the MOIL Transaction Committee) and [Conyers](https://www.conyers.com/publications/view/mandarin-oriental-international-limited-privatisation-and-delisting/) (Bermuda counsel).
- ✅ 25+ local management entities per market — [MO privacy policy, eff. 10 April 2026](https://www.mandarinoriental.com/en/privacy-policy).
- ⚠️ **FY2025 full financial statements were NOT obtained.** MOIL delisted in Jan 2026, and the [16 Mar 2026 results release](https://press.mandarinoriental.com/annual-results-2025/?lang=eng) publishes RevPAR (+10% like-for-like) and portfolio counts but **no revenue, EBITDA or profit line.** FY2024 is the last fully public set of figures. Expect no further audited public disclosure.
- ⚠️ **The FY2025 release contradicts itself on portfolio size:** body text says **45 hotels / 15 branded residences / 36 Exceptional Homes / 28 countries**; the boilerplate on the same page says **47 / 16 / 43 / 30**. **Both presented; discrepancy flagged; neither silently chosen.** I use the body figures above and label them as such.
- ⚠️ Japan's EMV 3DS requirement is sourced only to **vendor and industry secondary pages** ([Adyen knowledge hub](https://www.adyen.com/knowledge-hub/post-3ds-mandate-in-japan.md), [Merchant Risk Council](https://merchantriskcouncil.org/learning/resource-center/member-news/blog/2025/mrc-japan-credit-association-emv-3ds-mandate), [Stripe](https://stripe.com/resources/more/3d-secure-mandatory-for-ecommerce-in-japan)), which **disagree on whether METI or the Japan Credit Association issued it.** No primary METI or JCA document was retrieved. **Do not cite this in outreach without pulling the primary text.**
- ⚠️ `*.cdn-apple.com` appears in the SynXis booking-engine CSP. That is **consistent with** Apple Pay but is **not proof** — it could equally be Apple Maps. Not claimed as a payment method.
- ⚠️ `enablePlanetPaymentAuthorization` and `isRatePolicyFound` appear at **rate** level as well as property level, so a specific rate could in principle behave differently from its property default. I only observed the property-level defaults, which are uniformly `false`. **An orchestrator-rendered or rate-level method list could still differ from what the bundle shows** — the per-property array being empty is strong evidence, not absolute proof, for every rate.
- ❌ **No acquirer named, anywhere, for any property.** A deliberate zero. The previous report in this repo that scored a 0 rather than guess an acquirer set the right precedent and I have followed it.
- 🪤 **Substring traps caught this run, recorded for the next analyst:** `infor` returned 54 hits on the MO homepage — **every one was "information"**, not Infor the PMS vendor. `opera` returned 2 — one was "Operational hours", the other the genuine `modifyUseOperaHmsMessage`. On Rosewood's site `stripe` matched **`Stripe-Lounge-Pant-Hero`** and `striped` — a product name, not Stripe. `pix` in MO's bundle matched only tracking-pixel code, never the Brazilian rail. On Shangri-La, `wechat` matched only `wechatPopup*` social-share keys, not WeChat Pay. Context was checked on every hit reported above.

### Success Case Alternatives
- **Qatar Airways** — the closest profile match available and the one I would lead with. High-ticket, multi-currency, genuinely global corridor mix with no dominant single market, and an APAC-plus-EMEA footprint that mirrors Mandarin Oriental's traffic shape. Publicly referenceable on Yuno's own site. **No published metrics exist for this relationship — never attach a number to it.**
- **Copa Airlines** / **Avianca** — secondary travel references, same caution: nameable, **no published figures**.
- **NetEase Games** / **Garena** — nameable but a poor profile match here (small-ticket, high-frequency, APM-led). Do not use for a luxury hotel group.
- ❌ **No Yuno hotel or hospitality case study was found.** I looked. The honest position in a first call is that Yuno's referenceable travel proof is in airlines, not hotels, and that the hotel-settlement architecture question is one Yuno would be learning alongside them. Saying so is more credible than reaching for a hospitality name that does not exist.

---

## Executive Summary

Mandarin Oriental is an ultra-luxury hotel **management** company, not a hotel owner at scale: 45 hotels under management but only 12 owned or part-owned, with revenue of **US$525.8m** at the contracting entity against **US$2,127.7m** of combined revenue across the hotels it manages. Its parent was taken private by Jardine Strategic for ~US$4.2bn and **delisted from London, Singapore and Bermuda on 20 January 2026**. The key payment finding, taken first-hand from its live production configuration, is that `mandarinoriental.com` **captures a card guarantee and tokenises it into Mandarin Oriental's own Very Good Security vault, then settles nothing** — the money is taken at the property at check-out through Oracle OPERA, and the central settlement capability the company built (Planet Payment / Datatrans) is **switched off at all 48 properties**, with the redirect-payment-method array **empty at all 48**. The orchestration motion is therefore **in-house**: they built a merchant-side vault and a per-property method matrix, and the opening is not "you need orchestration" but "the tier you built captures cards it cannot settle, and the four properties that do take money at booking have no local rail enabled." The single sharpest concrete gap is **Beijing – Qianmen, which demands full prepayment at booking with no Alipay, WeChat Pay or UnionPay enabled.**

---

## Section 1: Website Traffic Analysis by Country

**Data source:** **Path 1 — pasted SimilarWeb data supplied by Prateek.** `accounts/traffic/mandarin-oriental-hotel-group.md`, SimilarWeb PRO, Worldwide, All traffic, period Sep 2026, captured 2026-10-09 05:15 IST. Used verbatim. **Not re-researched.** This is a **top-10 cut**, so the APAC total below is a visible floor, not a complete one.

**Total visits:** **1.265M** · **MoM:** ▲1.16% · **Desktop** 36.24% · **Mobile web** 63.76% · **Domains:** 1 (`mandarinoriental.com`), no corporate/booking split.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | 🇺🇸 United States | **18.63%** 🔺high priority | ~235,700 | — | SimilarWeb (supplied 2026-10-09) |
| 2 | 🇯🇵 **Japan** | **7.28%** 🔺high priority ✅APAC | ~92,100 | — | SimilarWeb (supplied 2026-10-09) |
| 3 | 🇧🇷 Brazil | **6.04%** 🔺high priority | ~76,400 | — | SimilarWeb (supplied 2026-10-09) |
| 4 | 🇦🇪 United Arab Emirates | **5.77%** 🔺high priority ⚠️EMEA | ~73,000 | — | SimilarWeb (supplied 2026-10-09) |
| 5 | 🇬🇧 United Kingdom | **5.01%** 🔺high priority | ~63,400 | — | SimilarWeb (supplied 2026-10-09) |
| 6 | 🇭🇰 **Hong Kong** | 4.93% ✅APAC (home) | ~62,400 | — | SimilarWeb (supplied 2026-10-09) |
| 7 | 🇫🇷 France | 4.03% | ~51,000 | — | SimilarWeb (supplied 2026-10-09) |
| 8 | 🇹🇼 **Taiwan** | 3.69% ✅APAC | ~46,700 | — | SimilarWeb (supplied 2026-10-09) |
| 9 | 🇮🇩 **Indonesia** | 3.64% ✅APAC | ~46,000 | — | SimilarWeb (supplied 2026-10-09) |
| 10 | 🇮🇹 Italy | 3.39% | ~42,900 | — | SimilarWeb (supplied 2026-10-09) |

**APAC visible total: 19.54%** across 4 of the top 10 (Japan, Hong Kong, Taiwan, Indonesia) ≈ **~247,200 visits/month**.
**Top 10 total: 62.41%.** The remaining 37.59% is unlisted long tail.

**Per-country trend: not available.** The supplied sheet gives a domain-level MoM only (▲1.16%). No per-country trend is claimed.

**Shape of the table — this matters more than any single row.** Nothing above 18.63%; the home market sits **sixth at 4.93%**; **no market above 19%**. Mandarin Oriental is the only hotel group in this batch growing on a single domain, and it is genuinely global rather than concentrated. **There is no single market on which to anchor a rail-gap argument.** The defensible framing is **corridor breadth** — a guest base spread across North America, Japan, Brazil, the Gulf, Western Europe, Greater China and Southeast Asia, every one of them hitting a card-guarantee form and then being billed by a different property in a different country.

**Cross-border observation:** **Brazil is 6.04% of traffic and Mandarin Oriental has no Brazilian property** — it does not appear anywhere in the 48-property configuration. Brazilian traffic is therefore pure outbound-demand research, converting into stays in the US, Europe and Asia. Pix and Brazilian domestic instalments are **not enabled** on the checkout — though see Section 4 for why that is architecturally inevitable under a guarantee-only model rather than an oversight. **⚠️ Checked both ways per the recorded trap: `pix` in the bundle matched only tracking-pixel code, never the Brazilian rail.**

**Markets with no local entity (cross-reference Section 2):** 🇧🇷 Brazil (no entity, no property), 🇯🇵 **Japan (property and traffic, but no local management entity named in the privacy policy)**.

---

## Section 2: Legal Entities & Local Presence

**Headquarters:** Hotel operations are managed from **Hong Kong** — *"The activities of the Group's hotels are managed from Hong Kong"* (MOIL FY24 RNS). Registered address of the management company and data controller: **Mandarin Oriental Hotel Group Limited, 8th Floor, One Island East, Taikoo Place, 18 Westlands Road, Quarry Bay, Hong Kong**, phone +852 2895 9288 (MO privacy policy, eff. 10 Apr 2026). The parent, **Mandarin Oriental International Limited**, is **incorporated in Bermuda**. Founded: the group traces to Hong Kong, 1963 — *"Mandarin Oriental was established 1963 in Hong Kong"* `[UNVERIFIED — search summary only, page not fetched]`.

### Ownership chain — and which entity actually contracts

| Level | Entity | Jurisdiction | Role | Source |
|---|---|---|---|---|
| 1 | **Jardine Matheson Holdings Limited (JMH)** | Bermuda | *"the ultimate holding company of the Group"* | [MOIL FY24 RNS, note 15](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf) |
| 2 | **Jardine Strategic Limited (JSL)** | Bermuda | *"The parent company of the Group is Jardine Strategic Limited"*; held 79.45% of MOIL in Apr 2021 → **100% since 19 Jan 2026** | [MOIL FY24 RNS, note 15](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf); [SGX MOIL0416, 16 Apr 2021](https://links.sgx.com/1.0.0/corporate-announcements/5ES6E1GAXEGYO3PR/661332_MOIL0416.pdf); [Slaughter and May](https://www.slaughterandmay.com/recent-work/mandarin-oriental-transaction-committee-on-the-recommended-cash-acquisition-by-jardine-updated/) |
| 3 | **Mandarin Oriental International Limited (MOIL)** | Bermuda | Holdco. **Delisted** LSE/SGX/BSX 20 Jan 2026. Consolidates 12 Owned Hotels + the Management Business. **FY24 revenue US$525.8m.** | [MOIL FY24 RNS](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf); [Conyers](https://www.conyers.com/publications/view/mandarin-oriental-international-limited-privatisation-and-delisting/) |
| 4 | **🎯 Mandarin Oriental Hotel Group Limited (MOHG)** | **Hong Kong** | **The management company. Data controller. Named in the gift-card store's own copyright line: `"copyRightsText":"2022 © Mandarin Oriental Hotel Group Limited"`. Operations managed from here.** | [MO privacy policy](https://www.mandarinoriental.com/en/privacy-policy); `giftcards.mandarinoriental.com` config, fetched 2026-10-09 |
| 5 | ~25 local management entities | 23 markets | Per-market data controllers / management companies | [MO privacy policy](https://www.mandarinoriental.com/en/privacy-policy) |
| 6 | **Third-party hotel owners' operating companies** | Per property | **The merchant of record for a room charge at the ~33 managed (non-owned) hotels.** E.g. MO Jakarta's owning company was sold **96.9% to P.T. Astra Land Indonesia** in June 2023. | [MOIL FY24 RNS, note 15](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf) |

> **🔑 WHICH ENTITY CONTRACTS FOR PAYMENTS — the answer, and its limit.**
>
> **For the central brand.com tier: Mandarin Oriental Hotel Group Limited (Hong Kong).** It is the entity that manages hotel operations, the entity named as data controller for the booking data, and the entity whose name sits in the copyright line of the one storefront where a card is actually charged today. That is where the VGS vault contract, the Planet Payment contract and any Yuno contract would sit.
>
> **For the money itself: not MOHG, and usually not MOIL either.** MOIL books US$525.8m while the hotels it manages turn over US$2,127.7m — the definition in its own filing is *"turnover of the Group's subsidiary hotels in addition to **100% of revenue from associate, joint venture and managed hotels**."* Roughly three-quarters of guest spend across the estate belongs to third-party owners. **At the ~33 managed hotels, the merchant of record for a room charge is the owner's operating company, and the acquiring relationship is almost certainly theirs.** At the 12 Owned Hotels — Tokyo and Singapore among them — it is a MOIL subsidiary.
>
> **Do not attribute the US$2.1bn to the hotel operator, and do not attribute the US$525.8m to the brand.** They are different entities' money.

### Per-market management entities (APAC and top-traffic markets)
| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| **Hong Kong S.A.R.** | **Mandarin Oriental Hotel Group Limited** | Not found | [MO privacy policy](https://www.mandarinoriental.com/en/privacy-policy) |
| **China** | Mandarin Oriental (Shanghai) Hotel Management Company Limited | Not found | same |
| **Macau S.A.R.** | Mandarin Oriental Residences Management (Macau) Limited | Not found | same |
| **Taiwan** | Mandarin Oriental Services Limited; Taiwan Mandarin Oriental Residences Management Maintenance Company Limited | Not found | same |
| **Japan** | ⚠️ **NONE NAMED.** Japan is listed among the territories where MO operates, but no local management entity is given for it, unlike 22 other markets. | — | same |
| **Indonesia** | P.T. MO Management Indonesia | Not found | same |
| **Singapore** | MOHG Management (Singapore) Pte Limited | Not found | same |
| **Malaysia** | MOHG Management (Singapore) Pte Limited — **the Singapore entity covers Malaysia too** | Not found | same |
| **Thailand** | Mandarin Oriental (Thailand) Limited | Not found | same |
| Philippines | Not found — Manila property opens late 2026 | — | — |
| United States | Mandarin Oriental Management (USA) Inc.; Residences at Mandarin Oriental Management (Fifth Avenue) LLC | Not found | same |
| United Kingdom | Mandarin Oriental Hyde Park Limited; Mandarin Oriental (UK) Limited; Mandarin Oriental Residences Management (UK) Limited | Not found | same |
| United Arab Emirates | Mandarin Oriental Abu Dhabi (BVI) Limited; Mandarin Oriental Dubai (BVI) Limited | Not found | same |
| Brazil | ⚠️ **NONE — no entity and no property** | — | — |

Remaining entities (Austria, Chile, Czech Republic, France, Germany, Greece, Italy, Morocco, Netherlands, Spain, Switzerland, Turkey) are listed in Section 1 Quick Look. **No registration number was obtained for any entity in this run.**

### Cross-Border Gap Analysis
| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| 🇺🇸 United States | ✅ #1 (18.63%) | ✅ Yes (2) | Not researched | Low |
| 🇯🇵 **Japan** | ✅ #2 (7.28%) | ⚠️ **Not named in the privacy policy** — though MO Tokyo is an Owned Hotel, so a Japanese entity almost certainly exists | **Not sourced this run** | **Moderate — see warning** |
| 🇧🇷 Brazil | ✅ #3 (6.04%) | ❌ **No** — no entity, no property | Not researched | **High — pure cross-border inbound demand** |
| 🇦🇪 UAE | ✅ #4 (5.77%) | ✅ Yes (2, BVI-incorporated) | Not researched | ⚠️ **EMEA — out of territory, excluded** |
| 🇬🇧 United Kingdom | ✅ #5 (5.01%) | ✅ Yes (3) | Not researched | Low |
| 🇭🇰 Hong Kong | ✅ #6 (4.93%) | ✅ Yes — the HQ | Not researched | Low |
| 🇫🇷 France | ✅ #7 (4.03%) | ✅ Yes | Not researched | Low |
| 🇹🇼 Taiwan | ✅ #8 (3.69%) | ✅ Yes (2) | Not researched | Low |
| 🇮🇩 Indonesia | ✅ #9 (3.64%) | ✅ Yes | Not researched | Low on entity; **owner is P.T. Astra Land Indonesia since 2023** |
| 🇮🇹 Italy | ✅ #10 (3.39%) | ✅ Yes (3, incl. BVI) | Not researched | Low |

> *"Warning: Potential cross-border operation in **Brazil**. No local entity and no property found. Brazilian guests (6.04% of traffic, Mandarin Oriental's third-largest market) are researching stays that will be billed by a property in another country entirely, through that property's acquirer — with higher scheme costs, lower approval rates and FX exposure on every leg."*

> *"Warning: **Japan** is Mandarin Oriental's second-largest traffic market at 7.28% and hosts an Owned Hotel, yet the privacy policy — which names a local management entity for 22 other markets — names none for Japan. This is a documentation gap, not proof that no Japanese entity exists."*

**⚠️ On regulatory acquiring gates: I did not source a single one in this run, and I am not asserting any.** The APAC reference flags India, Indonesia, China, Vietnam and South Korea as markets where domestic acquiring is commonly gated behind local presence — but that file is a checklist, not a source, and I found no current primary document for any of them. **No regulatory gate is claimed for Mandarin Oriental in any market.** The gating question is listed in Manual Research Recommendations.

> **MANUAL:** Verify entity details against the Hong Kong Companies Registry (for Mandarin Oriental Hotel Group Limited), ACRA/BizFile (MOHG Management (Singapore) Pte Limited) and the Japan hojin-bangou registry (for the unnamed Japanese entity). None was retrieved here.

---

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| **All markets — room booking, LIVE** | **Very Good Security (VGS)** — merchant-owned card vault and tokenisation. Live config in the bundle: `{name:"production", vaultId:"***(vault id redacted)", environment:"live", endpoint:"vgs-live.sitecore.moweb-acc.com"}`. Component `VgsForm`; loads `js.verygoodvault.com` / `js3.verygoodvault.com`; `VGSCollect.create()`; logs `tokenizedData:`; error string `"Error: VGS not implemented!"`. Response headers allow the `vgs-client` header and CORS origins `*.verygoodvault.com`, `*.verygoodproxy.com`. | `[Source Code]` `[Checkout]` | `https://www.mandarinoriental.com/corporate/main.js?v=2.42.0-beta.1-30` · `https://www.mandarinoriental.com/en` |
| **All markets — room booking, BUILT BUT DISABLED** | **Datatrans / Planet Payment** — `pay.datatrans.com` and `pay.sandbox.datatrans.com` explicitly allowlisted in the live CSP `default-src` **and** `script-src`. Bundle contains `datatransCode`, `datatransTrxId`, `clearDatatransTrxIdFromUrl()`, `secureFields.submit({expm, expy, "3D": threeDSecureData})`, `initializeTransaction`, `skipAuthorize`, `PlanetPaymentSecureFields`, and seven localised Planet error strings. **`enablePlanetPaymentForBooking: false` at all 48 properties.** | `[Source Code]` `[Checkout]` | same two URLs |
| **Gift cards & shop — LIVE** | **Stripe** — publishable key `pk_live_**********(redacted)`, Connect standard account `acct_**********(redacted)`, `stripe_statement_descriptor_suffix: "Mandarin Oriental"`, `checkoutFlow: "v2"`. Platform: **Techsembly** (`cdn-saas.techsembly.com`, `static.techsembly.com`, `saas-storefront-an.techsembly.com`). Operations contact `mohg-giftcards@avenhospitality.com` (**Aven Hospitality**). Store config `start_date: 2026-06-05`, `min_purchase: 500`, `maxCartTransaction: 10000`. | `[Source Code]` | `https://giftcards.mandarinoriental.com/egift-card-031505` |
| Gift cards | **Givex** — `givex_multi_currency: false`. Stored-value platform present on the Techsembly store, multi-currency disabled. | `[Source Code]` | same |
| Gift cards | **Adyen — PRESENT IN THE PLATFORM, NOT CONFIGURED FOR MANDARIN ORIENTAL.** `"adyenOriginKey": ""`. **This is a negative. Mandarin Oriental does not use Adyen on this store.** | `[Source Code]` | same |
| Gift cards | **PayPal — NOT CONFIGURED.** `"payPalId": null`. | `[Source Code]` | same |
| **Dining — separate surface** | **SevenRooms** — dining reservations run off-domain with MO venue slugs: `sevenrooms.com/reservations/motyokshiki/mo-com`, `/motyosense/`, `/motyosignature/`, `/motyoorientallounge/`, `/motyotapasmolecularbar/`, `/motyoventaglio/`, `/motyopizzabaron38/`, `/mandarinbar/`, `/explore/mandaringrillbarmohkg/reservations`. 491 references on the Tokyo dining page alone. Any dining deposit or prepaid experience settles through SevenRooms' own payment integration, **not** MO's. | `[Source Code]` | `https://www.mandarinoriental.com/en/tokyo/nihonbashi/dine` · `https://www.mandarinoriental.com/en/hong-kong/victoria-harbour/dine/mandarin-grill-and-bar` |
| **Property level — settlement** | **Oracle OPERA HMS** — localisation key `modifyUseOperaHmsMessage`: *"Please contact the hotel directly for any modifications or cancellations."* 29 `opera` references in the bundle. **This is where the money is actually taken.** | `[Source Code]` | `https://www.mandarinoriental.com/corporate/main.js?v=2.42.0-beta.1-30` |
| **Property level — acquirer** | ❌ **NOT ESTABLISHED.** No acquirer is named for any of the 48 properties, in any market, in any source I could reach. | — | — |
| **Spa** | **SpaSoft** (Springer-Miller) — spa reservation links are detected in the bundle by `e.target.includes("spasoft")`. The bundle also carries a dedicated `pp_spa_redirect_timestamp` session key, i.e. **a Planet Payment redirect flow specifically for spa** — gated on the same per-property flags, and therefore off. | `[Source Code]` | same |
| **CRS / booking engine** | **Sabre Hospitality / SynXis**, chain code **507**. `https://be.synxis.com/signin?chain=507` is linked from the MO homepage as the Modify/Cancel destination; 116 `synxis` references in the bundle. The SynXis host's own CSP names `*.synxis.com`, `*.sabrehospitality.com`, `*.asc.sabre.com`, `*.synxis-gcp.com`. | `[Source Code]` `[Checkout]` | `https://be.synxis.com/?chain=507` · `https://www.mandarinoriental.com/en` |
| **3DS in the booking engine** | **Modirum** — `*.modirum.com` is allowlisted in the SynXis booking-engine CSP (`script-src`, `default-src`, `child-src`, `worker-src`). Modirum is a 3-D Secure provider. ⚠️ **This is the SynXis platform's CSP for chain 507, not proof that Mandarin Oriental has enabled 3DS on any specific flow.** | `[Checkout]` | `https://be.synxis.com/?chain=507` |
| Distribution | **DerbySoft** — `linkcenterus.derbysoftsec.com` in the MO site CSP; `*.derbysoftca.com` in the SynXis CSP. | `[Checkout]` | both |
| Ancillary fintech | **Hopper Technology Solutions** — `fintech-portal.hts.hopper.com` and `fintech-portal.hts.staging.hopper.com` allowlisted in the SynXis booking-engine CSP. ⚠️ Platform-level; **not evidence Mandarin Oriental has enabled any Hopper fintech product.** | `[Checkout]` | `https://be.synxis.com/?chain=507` |

**Historical context, for completeness and clearly dated:** SynXis has supplied Mandarin Oriental's booking engine since 2000 and the group moved its portfolio to the SynXis RedX distribution management system in April 2009, with Property Connect linking RedX to the **Springer-Miller** property management system. ([Hotel Online, Apr 2009](https://www.hotel-online.com/News/PR2009_2nd/Apr09_SynXisMandarin.html), [Hospitality Upgrade](https://new.hospitalityupgrade.com/news/synxis-to-provide-redx-distribution-management-system-for-mandarin-oriental-hotel-group)) **This is 17 years old and I am not relying on it** — the current SynXis relationship is established first-hand from the live `chain=507` booking-engine host and 116 bundle references, and the current property system evidence points to **Oracle OPERA**, not Springer-Miller, for the PMS. Springer-Miller's **SpaSoft** does still appear in the live bundle.

**On Datatrans and Planet:** Datatrans AG was acquired by **Advent International and Eurazeo**, Planet's majority owners, and combined with Planet alongside Proximis, protel Hotelsoftware and Hoist Group in **March 2022**. Datatrans now trades as "Datatrans from Planet." ([Datatrans' own announcement](https://datatrans.ch/en/know-how/news/detail/datatrans-enters-next-development-phase-new-owners), [datatrans.weareplanet.com](https://datatrans.weareplanet.com/), [Businesswire, 2 Mar 2022](https://www.businesswire.com/news/home/20220302005050/fr), [Wikipedia: Planet (company)](https://en.wikipedia.org/wiki/Planet_(company))) **This is why `enablePlanetPayment*` flags and `pay.datatrans.com` are the same integration.**

### 3B. Payment Orchestrator

**Classification: IN-HOUSE ORCHESTRATION LAYER.**

Evidence type: `[Source Code]` + `[Checkout]`. Sources: `https://www.mandarinoriental.com/corporate/main.js?v=2.42.0-beta.1-30` and `https://www.mandarinoriental.com/en`, both fetched 2026-10-09.

**No third-party orchestrator was found.** Zero references to Juspay, Spreedly, Primer, Gr4vy, CellPoint Digital, APEXX, Payrails, Zooz or Yuno across the live CSP header, the response headers, the 3,334,390-byte application bundle, the gift-card store configuration, the SynXis booking-engine CSP, or any filing or press release.

But **"no orchestrator" is not the same as "greenfield," and this is not greenfield.** What Mandarin Oriental has built, in its own code, is a merchant-side control layer:

1. **A card vault it owns.** VGS, live, vault `***(vault id redacted)`, with a reverse proxy on MO's own infrastructure (`vgs-live.sitecore.moweb-acc.com`). Card data is tokenised into **Mandarin Oriental's** vault, not a PSP's. That is deliberate processor-independence.
2. **A per-property gateway enable matrix.** Four independent boolean flags per property (`ForBooking`, `ForFanClub`, `WithAuthorize`, `WithoutAuthorize`) controlling whether the second gateway runs at all, and in which mode.
3. **A per-property payment-method array.** `redirectPaymentMethodsForRoomBooking`, each entry carrying a `datatransCode`, a `type` (`"redirect"`), and a `skipAuthorize` flag.
4. **Method-level business logic.** `paymentMethodsConfig` filters Alipay out when a rate policy is present: `n.filter(e => e.datatransCode !== "ALP")`. And `planetPaymentAmount` switches between `null` (authorise only), `0` and the full cart total depending on `enablePlanetPaymentWithAuthorize`, `WithoutAuthorize` and `isRatePolicyFound`.
5. **Two mutually exclusive card paths selected at runtime**, with validation routed to whichever is active.

> *"Confirmed in-house. Mandarin Oriental built its own vault, its own per-property gateway switch and its own per-property method matrix. **The Phase 1 observation must not be 'you have no orchestration layer' — that is factually wrong and will burn the thread.** The argument is that the layer they built is wired to a gateway that is switched off at every property, so it captures cards it cannot settle, and the method matrix they built is empty everywhere."*

**On the hardest version of this sell:** an in-house layer is the toughest motion in the matrix, and it is the right one here. Do not argue that they need orchestration. Argue reach and opportunity cost: they have already paid the engineering bill for processor-independence and then not spent the coverage. Every one of the 48 `redirectPaymentMethodsForRoomBooking` arrays is empty, and the Planet path has sat dark long enough for the group to ship 45 hotels across 28 countries without ever switching it on at one of them.

> **MANUAL:** Walk through checkout with DevTools on a **Beijing – Qianmen** rate (full prepayment required — the one flow where money must move) and on a **Kuala Lumpur** rate (full payment, 48-hour cancellation on failure). Those are the two places where the live settlement path, and therefore the real acquirer, should be visible on the wire. A Tokyo or Hong Kong rate will only show the VGS guarantee form.

---

## Section 4: Alternative & Local Payment Methods

**This section has an unusually strong source: Mandarin Oriental's own production configuration states, per property, which redirect payment methods are enabled. For all 48 properties the answer is `[]` — none.**

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| **Global** | Visa, Mastercard, Amex, Discover, UnionPay, JCB (brand detection) | Cards | **Active in checkout** — card-brand map in `VgsForm`: `{amex:"AX", visa:"VI", mastercard:"MC", unionpay:"UP", chinaUPe:"CU", japCB:"JC", dinersclub:"DN", discover:"DS", maestro:"SW"}`. ⚠️ Brand *detection* in the capture form; this is **not** evidence that UnionPay or JCB are accepted for settlement. | `main.js?v=2.42.0-beta.1-30` |
| **Global** | Apple Pay (`APL`), PayPal (`PAY`), Alipay (`ALP`) | Digital wallet | **Capability present in code, NOT enabled at any property.** Codes appear in the Datatrans integration; `redirectPaymentMethodsForRoomBooking: []` at all 48. Alipay is additionally filtered out when a rate policy exists. | `main.js?v=2.42.0-beta.1-30`, homepage config |
| 🇯🇵 **Japan (7.28%, #2)** | konbini · PayPay · LINE Pay · Rakuten Pay · Paidy · carrier billing · domestic instalments / bonus payment | Cash/voucher · Wallet · BNPL · Carrier · Instalments | ❌ **Not found — none enabled.** `redirectPaymentMethodsForRoomBooking: []` for Tokyo (id 558). No JPY on the gift-card store. | homepage config, `giftcards.mandarinoriental.com` |
| 🇯🇵 Japan | 3DS2 on the brand.com booking card capture | — | ❌ **Not present on the live path.** 3DS2 data collection (`threeDSecureData` with cardholder name, email and phone mapping) exists **only inside the Planet/Datatrans path**, which is disabled for Tokyo. The live VGS path performs no authentication. ⚠️ **See the important caveat below before treating this as a compliance gap.** | `main.js?v=2.42.0-beta.1-30` |
| 🇭🇰 **Hong Kong (4.93%)** | FPS · Octopus · AlipayHK · WeChat Pay HK | A2A · Wallet | ❌ **Not found — none enabled.** `[]` for both HK properties (id 514, 556). | homepage config |
| 🇹🇼 **Taiwan (3.69%)** | JKOPay · LINE Pay · ATM / virtual-account transfer · convenience-store cash · domestic instalments | Wallet · Bank transfer · Cash · Instalments | ❌ **Not found — none enabled.** `[]` for Taipei (id 59555). | homepage config |
| 🇮🇩 **Indonesia (3.64%)** | **QRIS** · virtual account · GoPay · OVO · DANA · ShopeePay · Alfamart/Indomaret | Wallet · Bank transfer · Cash | ❌ **Not found — none enabled.** `[]` for Jakarta (id 528). ⚠️ `dana` in Indonesian means "funds" — checked; no false positive either way. | homepage config |
| 🇨🇳 **China (6 properties)** | **Alipay · WeChat Pay · UnionPay** | Wallet · Cards | ❌ **Not found — none enabled** at Beijing-Qianmen (2264), Beijing-Wangfujing (2265), Guangzhou (56732), Sanya (648), Shanghai (58160), Shenzhen (36052). **Beijing-Qianmen requires full prepayment at booking.** | homepage config |
| 🇸🇬 Singapore | PayNow · GrabPay | A2A · Wallet | ❌ **Not found — none enabled.** `[]` for Singapore (id 509). *(SGD **is** offered on the gift-card store.)* | homepage config |
| 🇲🇾 Malaysia | **FPX** · DuitNow · Touch 'n Go · Boost · GrabPay | Bank transfer · Wallet | ❌ **Not found — none enabled** at Kuala Lumpur (516) or Desaru Coast (95612). **Kuala Lumpur requires full payment at booking with a 48-hour cancellation on failure.** | homepage config |
| 🇹🇭 Thailand | **PromptPay** · TrueMoney · instalment plans | A2A · Wallet · Instalments | ❌ **Not found — none enabled.** `[]` for Bangkok (510). **Bangkok State Rooms & Suites require a one-night deposit.** | homepage config |
| 🇵🇭 Philippines | **GCash** · Maya · InstaPay/PESONet · OTC cash | Wallet · A2A · Cash | ❌ **Not found — none enabled.** `[]` for Manila (98703), opening late 2026. | homepage config |
| 🇧🇷 Brazil (6.04%, #3) | **Pix** · domestic card instalments (*parcelado*) | A2A · Instalments | ❌ **Not found — none enabled**, and no Brazilian property exists. ⚠️ `pix` in the bundle matched only tracking-pixel code — checked both ways. | homepage config |
| 🇺🇸 United States (18.63%) | Apple Pay · Google Pay · PayPal · BNPL | Wallet · BNPL | ❌ **Not found — none enabled.** `[]` for Boston (21547) and New York (532). | homepage config |
| **Gift cards / shop** | **Amex, Visa, Mastercard — and nothing else** | Cards | **Active in checkout.** Exactly three payment marks in the store footer. Currencies: **EUR, GBP, HKD, SGD only** — no JPY, TWD, IDR, CNY or USD. | `giftcards.mandarinoriental.com/egift-card-031505` |
| **Corporate** | **MO Direct Bill** | Invoice | **Active** — `isDirectBill` where every cart line has `guaranteeCode === "MO Direct Bill"`; no card form shown. | `main.js?v=2.42.0-beta.1-30` |

> **Warning: in Indonesia, QRIS is the national interoperable QR standard and is not enabled by Mandarin Oriental.** Bank Indonesia figures reported in January 2026 put 2025 QRIS volume at **15.51 billion transactions** (+148.54% YoY) worth **Rp1,420.66 trillion** (+115.27%), with ~**60 million users** and ~**43 million merchants**. ([Kontan, Jan 2026](https://keuangan.kontan.co.id/news/bi-mencatat-nilai-transaksi-qris-capai-rp-16448-triliun-pada-januari-2026), [Databoks Q3 2025](https://databoks.katadata.co.id/en/finance/statistics/6944c027919cc/the-number-of-qris-users-increased-in-q3-2025)) ⚠️ These are news outlets quoting Bank Indonesia, **not bi.go.id directly** — I could not reach the primary BI statistics publication.

> **Warning: in China, Alipay, WeChat Pay and UnionPay are the consumer rails and cards in the Western sense are marginal — and Mandarin Oriental has six Chinese properties, one of which requires full prepayment at booking, with none of those three rails enabled.** ⚠️ **I did not source a current primary citation for Chinese wallet share in this run and am not quoting a number for it.**

> **⚠️ The honest framing, and you should use it rather than the warnings above.** The absence of every local rail at every property is **not an oversight — it is a direct consequence of the guarantee-only architecture.** You cannot take a card guarantee on a QRIS QR code, a PromptPay transfer or an Alipay redirect; those rails settle immediately or not at all. So long as brand.com's job is to hold a card against a reservation and let the property bill it at check-out, **no local rail can be enabled, anywhere, by construction.** That is a far stronger and more defensible observation than "you are missing QRIS," and it points at the real decision: the four prepay properties, and any expansion of prepaid rates, cannot be served by the guarantee model at all.

> **⚠️ On Japan's EMV 3DS requirement — read before using it.** Secondary vendor and industry sources describe a requirement for e-commerce credit-card transactions in Japan to implement EMV 3-D Secure by end-March 2025, with sources disagreeing on whether it was issued by **METI** or the **Japan Credit Association**, and listing exemptions that include **MOTO and merchant-initiated transactions**. ([Adyen](https://www.adyen.com/knowledge-hub/post-3ds-mandate-in-japan.md), [Merchant Risk Council](https://merchantriskcouncil.org/learning/resource-center/member-news/blog/2025/mrc-japan-credit-association-emv-3ds-mandate), [Stripe](https://stripe.com/resources/more/3d-secure-mandatory-for-ecommerce-in-japan)) **I retrieved no primary METI or JCA text, and I am not asserting that Mandarin Oriental is non-compliant.** Indeed the guarantee-only model is a plausible reason 3DS is absent from the Tokyo brand.com flow: if no e-commerce charge occurs at booking and the card is billed later at the property, the transaction may fall outside the mandate's scope. **Do not raise this in outreach without pulling the primary guideline text.** It is a discovery question, not an attack line.

> **MANUAL:** Use a VPN to verify the live checkout method list per country for **Japan, Hong Kong and Taiwan**, and separately for **Beijing – Qianmen** and **Kuala Lumpur** where prepayment is required. Note the recorded trap: an orchestrator-rendered method list can be injected client-side from the vendor's own dashboard, so an empty array in the merchant's bundle is strong but not absolute proof for every rate.

---

## Section 5: Payment Issues & Customer Complaints

**No payment-related complaints found on Reddit, X, Trustpilot, or app store reviews.**

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| — | — | — | — | No public information found. |

Searches covered Reddit, Trustpilot and general web for declined cards, duplicate charges, refund delays and deposit disputes against Mandarin Oriental and the Fans of M.O. programme. **Nothing specific to Mandarin Oriental surfaced.** Searches did return exactly these complaint patterns against other hotel groups (Atlantis The Palm, IHG, Swissôtel, Strahan Tourist Park) — which is worth noting only as evidence that the search would have found such complaints had they existed. ICP row scored **0**.

**One engineering observation, offered as code and not as a complaint.** The live bundle contains dedicated recovery logic for failed redirect payments:

```js
cancelReservationOnFailedRedirect: function(){
  var e=this.$route.query, t=e.paymentError, n=e.paymentCancelled;
  (t||n) && this.cancelOrphanReservation(this.getRedirectConfirmationNumbers()) }
```

plus `is3DSRedirectRecovery`, `checkIfIs3DSRedirect()`, a 30-minute `pp_spa_redirect_timestamp` expiry window, and `planetPaymentTransactionExpiredError` → *"Error: The payment form has expired. Please reenter your card information."* **Somebody built orphan-reservation cleanup, which means orphaned reservations after failed redirect payments were a real enough problem to engineer against.** That is a credible discovery question for a call. It is not a customer complaint and I have not scored it.

---

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | **19–20 Jan 2026** | **Jardine Strategic Limited completed the acquisition of the 11.96% of MOIL it did not own, by Bermuda scheme of arrangement sanctioned 16 Jan 2026. Total value ~US$4.2bn (US$2.75 cash + US$0.60 special dividend = US$3.35/share). Listings cancelled on the London Stock Exchange, SGX and BSX. MOIL is now a 100%-owned private subsidiary of Jardine Matheson.** Announced 17 Oct 2025; scheme document published 14 Nov 2025. | **M&A / Privatisation** | [Slaughter and May](https://www.slaughterandmay.com/recent-work/mandarin-oriental-transaction-committee-on-the-recommended-cash-acquisition-by-jardine-updated/) · [Conyers](https://www.conyers.com/publications/view/mandarin-oriental-international-limited-privatisation-and-delisting/) · [Cancellation RNS](https://www.investegate.co.uk/announcement/rns/jardine-matheson-holdings-ltd-singapore-reg---jar/cancellation-of-the-listings-of-mandarin-oriental/9369226) · [BSX](https://www.bsx.com/company_details.php?CompanyID=132) |
| 2 | **16 Mar 2026** | **FY2025 results: RevPAR +10% like-for-like, market share +3 percentage points. Portfolio 45 hotels / 15 branded residences / 36 Exceptional Homes across 28 countries** (⚠️ same page's boilerplate says 47 / 16 / 43 / 30 — **discrepancy flagged, both reported**). Two hotels opened, three rebrandings, five new destinations. **30+ signed hotel and branded-residence projects to open over the next six years.** 100% of the network GSTC-certified. **No revenue, EBITDA or profit figures published** — the first results release since delisting. | Market Expansion | [press.mandarinoriental.com/annual-results-2025](https://press.mandarinoriental.com/annual-results-2025/?lang=eng) · [Hospitality Net](https://www.hospitalitynet.org/news/4131468/mandarin-oriental-reports-strong-business-performance-for-2025) |
| 3 | **Late 2026 (imminent)** | **Mandarin Oriental Makati, Manila opens — 275 rooms and suites, a spa and wellness floor, five dining and bar concepts, event spaces.** Developed with Ayala Land. The brand's return to the Philippines, where it operated 1976–2014. ⚠️ 2024 coverage gave 276 rooms; 2026 coverage gives 275 — **minor discrepancy flagged.** | Market Expansion | [Ayala Land](https://ayalaland.com/news/ayala-land-and-mandarin-oriental-officials-visit-new-mandarin-oriental-site-on-the-road-to-opening-in-2026) · [TTG Asia](https://www.ttgasia.com/2024/04/29/new-mandarin-oriental-to-open-in-philippines-makati-city-in-2026/) · [Journal des Palaces](https://journaldespalaces.com/en/pressrelease-78578-philippines-hotel-opening-mandarin-oriental-announces-its-return-to-manila.html) |
| 4 | **H1 2025 (7 Aug 2025)** | Interim results: combined total revenue **US$1,088m** (+11%), hotel management fee income **US$41m** (+14%), consolidated revenue **US$248m** (−1%, on the Paris disposal), EBITDA **US$61m** (+4%), underlying profit attributable to shareholders **US$24m** (+6%), interim dividend US¢1.50. Portfolio reached **44 hotels** after the Lutetia rebrand and management takeovers in Amsterdam, Venice and **Desaru Coast, Malaysia**. **Miami disposal completed and Munich agreed for sale, with long-term management agreements retained.** Group RevPAR **US$430** (+11%); Asia +11%, EMEA +11%, America +6%. | Funding / Asset-light | [Yahoo Finance SG](https://sg.finance.yahoo.com/news/mandarin-oriental-reports-higher-underlying-035816370.html) · [Investing.com](https://www.investing.com/news/company-news/mandarin-oriental-reports-strong-management-business-growth-in-h1-2025-93CH-4155000) |
| 5 | **5 Mar 2025** | FY2024 results: combined total revenue **US$2,127.7m** (+13%), hotel management fees +15%, revenue **US$525.8m** (−6%), underlying profit after tax **US$75m** (−8%, *"due to lower one-off residences branding fees"*), **loss attributable to shareholders US$(78.6)m**. **41 hotels under management, with a target to more than double by 2033.** Eight new management contracts. Paris disposed for **US$382m**. **Headline bullet: *"Investing in capability now to achieve long-term targets and sustain accelerated growth."*** Chairman: **Ben Keswick**. | Market Expansion / Leadership | [MOIL FY24 RNS 5036Z](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf) · [press.mandarinoriental.com](https://press.mandarinoriental.com/?p=12035) |

**Also noted, dated and sourced:**
- **Nov 2024** — acquired 100% of **Mandarin Oriental Exceptional Homes** from **Stay One Degree Limited** (an associate company) for US$5.6m (US$4.7m cash + US$0.9m contingent). The portfolio was 26 properties at FY24 and 36 at FY25. **The privacy policy states Mandarin Oriental *"acts as booking agent and does not own, operate or manage the homes."*** ([MOIL FY24 RNS, note 15](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf), [MO privacy policy](https://www.mandarinoriental.com/en/privacy-policy))
- **June 2023** — sold **96.9%** of the owning company of **Mandarin Oriental, Jakarta** to **P.T. Astra Land Indonesia**, itself a JMH subsidiary. Indonesia is 3.64% of traffic; **the Jakarta hotel's revenue is no longer MOIL's.** ([MOIL FY24 RNS, note 15](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf))
- **Pipeline from MO's own site navigation:** Hangzhou (Spring 2027), Cortina (2027), Suzhou, Manila-Makati (Nov 2026), Venice, Puerto Rico.
- **~5 June 2026** — the Techsembly gift-card store config carries `"start_date":"2026-06-05T09:00:00-07:00"`, i.e. **the Stripe-backed gift-card storefront was configured or relaunched around June 2026.** The most recent payment-infrastructure change I can date. `[Source Code]`

**No public payment-related RFP found.** No RFP override applies.

**No payment-related job postings found.** Searches for Mandarin Oriental payments, e-commerce, payment-engineering and payment-infrastructure roles returned nothing from the company. A [Fourth workforce-management case study for MOHG](https://au.fourth.com/case-study/mandarin-oriental-hotel-group) exists but concerns labour and inventory, not payments. ICP row scored **0**.

---

## Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | ~5 Jun 2026 | **Stripe-backed gift-card storefront configured on Techsembly** (`start_date: 2026-06-05`), cards only, EUR/GBP/HKD/SGD, Givex stored value present, Adyen and PayPal left unconfigured | A second live PSP relationship, dated, on a surface where money actually moves | `giftcards.mandarinoriental.com/egift-card-031505` `[Source Code]` |
| 2 | Current (observed 2026-10-09) | **Planet Payment / Datatrans integration complete and disabled at all 48 properties**; `redirectPaymentMethodsForRoomBooking: []` at all 48 | The single most important payment fact on the account | `https://www.mandarinoriental.com/en` `[Source Code]` |
| 3 | Current (observed 2026-10-09) | **Mandarin Oriental runs its own live Very Good Security vault** (`***(vault id redacted)`) with a reverse proxy on its own infrastructure | Merchant owns the card vault — processor-independent by design | `main.js?v=2.42.0-beta.1-30` `[Source Code]` |
| 4 | Mar 2022 | Datatrans AG combined into the Planet group under Advent International and Eurazeo, alongside Proximis, protel Hotelsoftware and Hoist Group | Explains why the `enablePlanetPayment*` flags and `pay.datatrans.com` are one integration | [Datatrans](https://datatrans.ch/en/know-how/news/detail/datatrans-enters-next-development-phase-new-owners) · [Businesswire](https://www.businesswire.com/news/home/20220302005050/fr) |
| 5 | Apr 2009 | Mandarin Oriental moved its portfolio to SynXis RedX distribution management; SynXis had supplied its booking engine since 2000 | Historic root of the current Sabre/SynXis chain-507 relationship. **17 years old — context only, not relied upon** | [Hotel Online](https://www.hotel-online.com/News/PR2009_2nd/Apr09_SynXisMandarin.html) |

**No provider removals found.** No press, filing or source reports Mandarin Oriental discontinuing any payment provider or method.

> ⚠️ **However, note a de facto non-adoption that reads like a removal and is worth a question:** a complete Planet Payment / Datatrans acceptance path — 3DS2, authorise and no-authorise modes, redirect APMs, orphan cleanup, seven localised error strings, a dedicated spa redirect flow — exists in production code and is enabled at **zero of 48 properties**. Either it was switched off, or it was built and never switched on. **Both are good questions and I cannot tell which from outside.** `[Source Code]`

---

## Section 8: Checkout Experience Audit

**Fetching worked in this environment.** WebFetch returned real HTTP responses (a genuine 404 on one guessed URL, 200s elsewhere) and Bash `curl` returned 200s with full headers on every target. **Section 8 is completed from live first-hand observation of the publicly reachable layers.** What I could **not** do is complete a booking — the card step sits behind a live availability session with real rates, and nobody can reach it without transacting. Every row below says which layer it came from.

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | **Custom-built**, embedded. A Vue application on `www.mandarinoriental.com` (Sitecore CMS, `moweb-acc.com` / `managedcloud.sitecore.com`), with card fields rendered as **VGS-hosted iframes** inside MO's own form. Modify/Cancel is handed off to the **SynXis** booking engine at `be.synxis.com/signin?chain=507`. Checkout API: `/api/v1/booking/check-out`; edit mode: `/api/v1/booking/ModifyReservation`. | **Good** | Merchant controls the UI; the vault holds the PAN. `[Source Code]` |
| Guest checkout | **Yes.** `isFanClubBooking` is a separate branch with its own `enablePlanetPaymentForFanClub` flag, so loyalty is optional, not required. | **Good** | `[Source Code]` |
| Steps to complete payment | **Four or five labelled steps**, from the localisation dictionary: `guestInformation: "1. Guest Information"` → `paymentInformation: "2. Payment Information"` → `additionalInformation: "3. Additional Information"` → `termsAndContitionsInformation: "4. Terms and Conditions"`. The Fans of M.O. variant inserts a step: `fcpaymentInformation: "3. Payment Information"` … `fctermsAndContitionsInformation: "5. Terms And Conditions"`. | **Fair** | Five steps for a logged-in member is long for a luxury flow. `[Source Code]` |
| Card input experience | **Tokenised iframe.** Four VGS-hosted fields — `cardHolder`, `cardNumber`, `cardExpirationDate`, `cardCvc` — inside a component named `VgsForm`, posting to Mandarin Oriental's own live vault. When Planet is enabled instead, the fields come from `PlanetPaymentSecureFields` (Datatrans Secure Fields) and the error string becomes *"Missing card data from payment provider."* | **Good** | Two separate iframe providers for the same field set. `[Source Code]` |
| Payment methods visible | **Cards only.** `redirectPaymentMethodsForRoomBooking: []` at all 48 properties, plus **MO Direct Bill** for corporate (no card form at all). | **Poor** | `[Source Code]` |
| Location-based method display | **No geo-adaptation of methods — because there are no alternative methods to adapt.** The method list is driven by `selectedHotel.redirectPaymentMethodsForRoomBooking`, i.e. by the **property's** country, not the guest's. A Japanese guest booking New York sees New York's configuration. Both are `[]`. | **Poor** | Architecturally property-keyed, not guest-keyed. `[Source Code]` |
| Instalment / EMI options | ❌ **None, anywhere.** No instalment, EMI, bonus-payment or BNPL code path in the bundle. **Expected and absent in Japan (7.28%) and Taiwan (3.69%)**, both markets where high-ticket luxury commonly converts on instalments, and in Brazil (6.04%). | **Poor** | `[Source Code]` |
| 3DS implementation | **EMV 3DS2 — in the Planet path only, which is disabled everywhere.** `threeDSecureData` builds `{cardholder:{cardholderName, email}}` plus a phone map (`MOBILEPHONE`/`HOMEPHONE`/`BUSINESSPHONE`) and submits as `{expm, expy, "3D": threeDSecureData}` — a 3DS2 cardholder-data payload. `is3DSRedirectRecovery` handles the challenge return. **On the live VGS path: no authentication at all.** Separately, `*.modirum.com` (a 3DS provider) is allowlisted in the SynXis booking engine's CSP. | **Fair** | 3DS2 is built but dark on brand.com; the CRS has its own 3DS layer. `[Source Code]` `[Checkout]` |
| PCI indicator | **PSP/vault iframe, not self-hosted card fields.** Card data never enters MO's DOM — VGS iframes capture it. | **Good** | See Section 9. `[Source Code]` |
| Mobile responsiveness | **Mobile web is 63.76% of traffic** (SimilarWeb, supplied). The page declares a responsive viewport and the booking app is a single Vue codebase. **Not tested on a device** — I observed markup, not rendering. | **Not assessed** | Honest gap. `[Checkout]` |
| Multi-currency / local pricing | **Yes, per property.** Each property config carries `currency` and `currencyCn`; the UI has `findYourCurrency` / `selectCurrency` / `getDisplayPrice({withIsoCode, isoAfter})`. The gift-card store offers **EUR, GBP, HKD, SGD only**. | **Fair** | Room booking is multi-currency; the shop is not, and omits JPY. `[Source Code]` |
| Saved payment methods | **Yes, with a dedicated management component.** `ModifyReservationCardManagement` takes `vgs-endpoint`, `is-using-vgs`, `enable-planet-payment`, `cart-id`, `property-currency`, `return-url`, `hotel-code`, `planet-payment-amount` and `disable-add-new-card`; the UI shows `modifyCardEnd: "Card ending in"`. Stored credentials live in **Mandarin Oriental's VGS vault**. | **Good** | Merchant-owned stored credentials — unusual and strategically significant. `[Source Code]` |
| Error message clarity | **Specific and well-localised for the dark path, generic for the live one.** Seven distinct Planet strings including *"Error: The payment form has expired. Please reenter your card information"*, *"Payment not authenticated"*, *"Payment Server Unavailable"*. The VGS path has `paymentErrorMessage` / `paymentCancelledMessage` and little else. | **Fair** | The better messaging is on the disabled path. `[Source Code]` |
| **Guarantee vs settlement** | 🔑 **The defining row. At 44 of 48 properties the checkout takes a card guarantee and charges nothing** — Mandarin Oriental's own words, per property. Four properties take money at booking: Beijing-Qianmen (full prepayment), Kuala Lumpur (full payment, 48h kill clause), Bangkok (suite deposit), Lucerne (deposit). | **This is the finding** | `[Source Code]` |

**Separate surfaces audited:**
- **`giftcards.mandarinoriental.com`** (Techsembly, nginx + Phusion Passenger) — **live Stripe**, cards only (Amex/Visa/MC), four currencies, `checkoutFlow: "v2"`, reCAPTCHA, `min_purchase: 500`, `maxCartTransaction: 10000`, 10% bonus-card promotion, per-property storefronts including "MOLZN App Storefront" (Lucerne). Merchant of record per its own copyright line: **Mandarin Oriental Hotel Group Limited**.
- **`na.shopmo.com` / `shopmo.com`** (ASP.NET, AWS ALB, LiveChat) — the Mandarin Oriental Shop. **No payment vendor identifiable from the public pages**; `/checkout` returns 404 without a session. **`www.shopmo.cn` 301s to `na.shopmo.com/index.aspx?referrer=cn`** — **Chinese shoppers are served from a US-hosted storefront, not a China-resident one.** The `.cn` domain is not a separate property.
- **`be.synxis.com/?chain=507`** — the SynXis booking engine. CSP allowlists `*.sabrehospitality.com`, `*.asc.sabre.com`, `*.synxis-gcp.com`, **`*.modirum.com`** (3DS), `*.derbysoftca.com`, `fintech-portal.hts.hopper.com`, `icm.aexp-static.com` (Amex), `*.cdn-apple.com`, `*.triptease.io`, `*.thehotelsnetwork.com`, `*.dynatrace.com`, `*.datadoghq.com`. ⚠️ **Platform-level CSP for chain 507 — it shows what the booking engine may load, not what Mandarin Oriental has enabled.**
- **Dining** — off-domain on **SevenRooms**. **Spa** — **SpaSoft** links plus a dedicated (dark) Planet redirect path.
- **`/en/residences`** — **no payment functionality whatsoever.** See Section 10, Insight #4.

**On CSP as a discovery tool, for the record:** the main site's CSP has **no `form-action` and no `connect-src` directive**, and its `default-src` begins with a bare `https:` wildcard, so neither can be used to localise where card data posts. What the CSP *does* give is a deliberate, specific allowlist of `pay.datatrans.com`, `pay.sandbox.datatrans.com`, `*.stripe.com` and `js.verygoodvault.com` alongside `*.verygoodproxy.com` in the CORS origins and `vgs-client` in the allowed headers. **That allowlist, not the directive structure, is what identified the stack.**

---

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **Not found.** No PCI level, AOC, SAQ type or attestation is published by Mandarin Oriental anywhere I could reach. The only `pci` string on the site is `BOOMR_config.PageParams.pci` — a **Boomerang/mPulse RUM configuration flag, not a compliance statement.** ⚠️ Trap logged. | `https://www.mandarinoriental.com/en` |
| Card data handling | **VGS-hosted iframe fields → Mandarin Oriental's own live vault** (`vaultId: ***(vault id redacted)`, `environment: live`), with a reverse proxy at `vgs-live.sitecore.moweb-acc.com`. Alternative path: **Datatrans Secure Fields** iframes (disabled). Card data does not enter MO's own DOM in either path. | `main.js?v=2.42.0-beta.1-30` |
| Recommended Yuno integration | **SDK**, not back-to-back API — and with an explicit caveat. Mandarin Oriental has already invested in a **merchant-owned vault** as its abstraction layer. Any Yuno proposal that requires surrendering vault custody will meet architectural resistance. The viable shape is Yuno **downstream of the existing VGS vault**, consuming VGS aliases and routing them, rather than replacing the capture tier. **This is an inference from the architecture, not a tested integration pattern.** | — |

> `[INFERENCE, not confirmed]`: Based on confirmed use of VGS-hosted tokenising iframes, with card data captured in a vendor-hosted field and aliased before it reaches Mandarin Oriental's application, the merchant's PCI scope is **likely reduced** — plausibly in the SAQ A / SAQ A-EP region for the brand.com booking flow. **No compliance level is stated anywhere and I am not asserting one.** Note the complication that a merchant-operated VGS vault, unlike a PSP-hosted one, may keep the merchant in scope for the vault itself — **this is exactly the kind of question a payments owner will want to discuss, and it is a good reason for a call.**

**No direct PCI compliance documentation found publicly for Mandarin Oriental.**

---

## Section 10: Strategic Insights & Outreach Angles

> ### **Insight #1: The central tier captures cards it cannot settle**
> **Evidence:** **Section 3A + Section 8 + Section 2.** The homepage config sets `enablePlanetPaymentForBooking: false` at all 48 properties while the bundle carries a complete Planet/Datatrans acceptance path (`https://www.mandarinoriental.com/en`, `https://www.mandarinoriental.com/corporate/main.js?v=2.42.0-beta.1-30`); the per-property `restrictionPolicy` strings say *"no charges will be made until check-out"* at Tokyo, Singapore, Jakarta, Shanghai, Sanya, Guangzhou, Macau and Beijing-Wangfujing, and *"a credit card **for guarantee**"* at Hong Kong; `modifyUseOperaHmsMessage` routes modifications to the property's Oracle OPERA system; and MOIL's own FY24 filing shows US$525.8m of revenue against US$2,127.7m across the managed estate ([RNS 5036Z](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf)).
> **Pain Point:** Mandarin Oriental has paid the engineering bill for a central payment tier — vault, 3DS2, redirect APMs, per-property method matrix, orphan-reservation cleanup — and gets none of the commercial return, because at 44 of 48 properties the tier holds a card and the property takes the money. Every basis point of approval rate, every FX spread, every acquiring fee on the group's guest spend is decided property by property, by 33 different owners' acquirers, with no central visibility and no group negotiating leverage. The group can see what it sold but not what it cost to collect.
> **Yuno Value Proposition:** Orchestration is the wrong opening and would be rejected. The right one is **turning the tier they already built into a settling tier without re-platforming it.** Yuno sits downstream of the existing VGS vault, consumes the aliases Mandarin Oriental already owns, and gives one routing and reporting surface across however many acquirers the 48 properties use — so prepaid and deposit rates can be switched on per property without a new integration per market, and the group can finally see acceptance economics across the estate.
> **Best Success Case:** **Qatar Airways** — high-ticket, multi-currency, genuinely global corridor mix with no dominant market, APAC and EMEA together. Publicly referenceable on Yuno's own site. **No published metrics exist; never attach a number.**
> **Outreach Angle:** Your booking flow tokenises the card into your own VGS vault and then, at 44 of your 48 properties, charges nothing — the money moves at the property, at check-out. You built a central payment tier and use it as a filing cabinet.
> **Suggested Subject Line:** The vault is yours. The settlement isn't.

> ### **Insight #2: Beijing demands full prepayment with no Chinese rail enabled**
> **Evidence:** **Section 4 + Section 1 + Section 3B.** Beijing – Qianmen (property id 2264): *"**Full prepayment is required at time of booking.**"* Kuala Lumpur (id 516): *"**Full payment is required.** … If payment is unsuccessful within 48 hours of making the reservation, the hotel reserves the right to cancel the reservation."* For both, and for all six Chinese properties, `redirectPaymentMethodsForRoomBooking: []`. The capability exists in the same bundle — Datatrans code `"ALP"` (and a card map containing `unionpay:"UP"`, `chinaUPe:"CU"`) — and is switched off, with Alipay additionally filtered out when a rate policy applies: `n.filter(e => e.datatransCode !== "ALP")`. Mandarin Oriental opened Beijing – Qianmen in 2024 and reports *"strong domestic demand in China"* with the property *"commanding strong rate leadership"* ([MOIL FY24 RNS](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf)).
> **Pain Point:** This is the one place in the portfolio where the guarantee model cannot hide the gap. A Chinese domestic guest, on a Chinese property, on a rate that **requires money to move at booking**, is offered a card form and nothing else — in a market where Alipay, WeChat Pay and UnionPay are the consumer rails. Kuala Lumpur is worse in one respect: a failed payment does not just lose the sale, it arms a 48-hour clock that cancels a confirmed reservation at an ultra-luxury property. Both are silent, uninstrumented abandonment on the highest-value inventory the group sells.
> **Yuno Value Proposition:** This is the narrowest possible wedge and the easiest to prove: enable the local rails on the four properties that already require prepayment, measure conversion against the card-only baseline, and let that number decide whether prepaid rates expand. No re-platforming, no group mandate, four properties.
> **Best Success Case:** **Qatar Airways** — the nearest profile on high-ticket cross-border conversion. **No published metrics; do not invent one.**
> **Outreach Angle:** Beijing – Qianmen asks for full prepayment at the time of booking, and the only way to pay is a card. Alipay's integration code is already in your bundle — `datatransCode: "ALP"` — switched off at every property you run.
> **Suggested Subject Line:** Full prepayment in Beijing, card-only at checkout

> ### **Insight #3: The asset-light pivot moves folios out of your own acquiring, one disposal at a time**
> **Evidence:** **Section 6 + Section 2 + Section 12.** MOIL sold its Paris property for US$382m in 2024, completed the Miami disposal and agreed the sale of Munich in H1 2025, **retaining long-term management agreements in each case** ([FY24 RNS](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf), [H1 2025](https://sg.finance.yahoo.com/news/mandarin-oriental-reports-higher-underlying-035816370.html)); it sold 96.9% of MO Jakarta's owning company to P.T. Astra Land Indonesia in 2023; it now owns or part-owns **12 of 45 hotels**; and the target is to **more than double the portfolio by 2033** with **30+ signed projects in six years** ([FY25 release](https://press.mandarinoriental.com/annual-results-2025/?lang=eng)) — all of them management contracts, not acquisitions.
> **Pain Point:** Every disposal and every new management contract moves a property's folios from a MOIL subsidiary's acquiring relationship to a third-party owner's. The group is deliberately shrinking the share of guest spend it controls at the merchant-of-record level while doubling the number of properties whose brand.com bookings it is responsible for converting. By 2033 the central tier could be originating demand for ninety-odd properties and settling at a dozen. **The commercial consequence is concrete: brand.com conversion becomes the group's main lever on managed-hotel revenue, because management fees are a percentage of a top line the group no longer collects.**
> **Yuno Value Proposition:** A central routing and acceptance layer is the only thing that scales across a portfolio the group manages but does not own — one integration that each new management contract inherits on day one, rather than a per-owner acquiring negotiation per opening. This is the argument that matters to the Management Business, and it is about fee revenue, not cost.
> **Best Success Case:** **Qatar Airways** (multi-market acceptance under one routing layer). **No published metrics.**
> **Outreach Angle:** You own 12 of 45 hotels and plan to more than double the portfolio by 2033 — almost entirely through management contracts. Each new one inherits whatever acquiring the owner already has, and your management fee is a percentage of a top line you do not collect.
> **Suggested Subject Line:** 12 of 45 owned, doubling by 2033

> ### **Insight #4: Branded residences are not a payment flow at all — drop the hypothesis**
> **Evidence:** **Section 3A + Section 12 + Section 6.** `https://www.mandarinoriental.com/en/residences` (fetched 2026-10-09, HTTP 200) contains **zero** payment functionality: no price, no deposit, no reservation fee, no card field — only *"Contact Us"* and *"Submit Enquiry."* MOIL's own filing books residences income as **one-off branding fees** under "Hotel & Residences branding and management" (US$95.3m segment revenue FY24, including hotel management fees), and attributes the 8% fall in FY24 underlying profit to *"lower one-off residences branding fees"* and *"reduced one-off branding fees from the sale of branded residences"* ([RNS 5036Z](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf)).
> **Pain Point:** There isn't one — and saying so is the value. **The target list flags branded residences as a high-ticket payment flow. It is not.** Mandarin Oriental earns a **branding fee from the developer**; the residence itself is a real-estate conveyance between buyer and developer, handled by lawyers and escrow. A seven-figure deposit is not a card transaction and never touches a PSP. Walking into a first call with a residences-deposit theory would be immediately and visibly wrong to anyone on the other side.
> **Yuno Value Proposition:** **None here. Do not pitch it.** The one adjacent flow worth a single question is **residences owner service charges** — Mandarin Oriental Residences Management entities exist in the UK, Macau, Spain, Taiwan and Turkey, and those plausibly bill recurring charges to owners. `[INFERENCE, not confirmed — no public evidence of any payment stack for this.]` Ask; do not assert.
> **Best Success Case:** n/a.
> **Outreach Angle:** Do not use one. This insight exists so Prateek does not use the wrong one.
> **Suggested Subject Line:** n/a — do not raise residences as a payment flow.

> ### **Insight #5: Three live payment stacks, three different owners, no common surface**
> **Evidence:** **Section 3A + Section 8.** Room booking runs on Mandarin Oriental's own **VGS** vault with **Datatrans/Planet** dark (`www.mandarinoriental.com`). Gift cards and shop run on **live Stripe** via the **Techsembly** SaaS platform as a Connect standard account (`acct_**********(redacted)`), operated by **Aven Hospitality** (`mohg-giftcards@avenhospitality.com`), in EUR/GBP/HKD/SGD, cards only. Dining runs off-domain on **SevenRooms**. Spa has a separate (dark) Planet redirect path and **SpaSoft** links. Settlement for rooms happens property-side in **Oracle OPERA**. All first-hand, fetched 2026-10-09.
> **Pain Point:** Four guest-facing payment surfaces under one brand, with four different providers, four different reconciliation paths and no shared view of a guest's spend. The gift-card store omits JPY while Japan is the group's second-largest market and the US its largest; it offers no wallet at all; and it carries an unconfigured Adyen key and a null PayPal ID, meaning somebody evaluated both and stopped. Nobody in the group can answer "what did this guest pay us, across rooms, dining, spa and gift cards, and what did it cost us to accept" without manual work across four vendors.
> **Yuno Value Proposition:** One acceptance and reporting layer across the non-room surfaces is a smaller, faster, lower-politics first project than touching room settlement — and it is the one place where Mandarin Oriental is already the merchant of record (Mandarin Oriental Hotel Group Limited, per the gift-card store's own copyright line) and therefore can actually sign.
> **Best Success Case:** **Qatar Airways** — multi-surface, multi-currency travel acceptance. **No published metrics.**
> **Outreach Angle:** Your gift-card store sells in euros, pounds, Hong Kong dollars and Singapore dollars. Japan is 7.28% of your web traffic and the US 18.63%. Neither currency is on the list.
> **Suggested Subject Line:** Four currencies on the gift-card store, and no yen

---

## Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. Your booking flow tokenises the guest's card into your own Very Good Security vault, and then at 44 of your 48 properties charges nothing — your own terms say *"no charges will be made until check-out."*
2. Beijing – Qianmen requires full prepayment at the time of booking, and the only way a guest can pay is a card — Alipay's integration code is already in your bundle, switched off at every property you run.
3. Your gift-card store sells in EUR, GBP, HKD and SGD, while Japan is 7.28% of your web traffic and the United States 18.63%.
4. You own 12 of 45 hotels and intend to more than double the portfolio by 2033, almost entirely through management contracts — each one inheriting whoever the owner already acquires with.
5. Kuala Lumpur cancels a confirmed reservation if payment fails within 48 hours, and card is the only method on the page.

**Cold call openers (conversational, one sentence each):**
1. "I spent some time in your booking flow this week — am I right that the card you take on mandarinoriental.com is a guarantee, and the actual charge happens at the property on check-out?"
2. "You've got a complete Planet Payment integration sitting in your production bundle that looks like it's switched off at every property — was that a deliberate call, or has it just not had a reason to go live yet?"
3. "Beijing – Qianmen is the only one of your China properties asking for full prepayment at booking — how's that converting against a card-only checkout?"
4. "As you move to management contracts rather than ownership, who ends up owning the acquiring relationship for a new property — you or the owner?"
5. "Your gift-card store runs on a completely different provider from your room bookings — is anyone looking at those two together yet?"

---

## Section 11: Similar Companies & Prospecting Pipeline

### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| **The Peninsula Hotels** (HSH) | peninsula.com | Hong Kong | Not researched | HK, Tokyo, Shanghai, Beijing, Bangkok, Manila | ⬜ **Unexamined — HTTP 403 to my fetch.** A weak negative, not a clean one. | Live fetch 2026-10-09 |
| **Rosewood Hotel Group** | rosewoodhotels.com | Hong Kong | Not researched | HK, Bangkok, Phnom Penh, Beijing, Tokyo | ❌ None found on the public pages. ⚠️ `stripe` matched **`Stripe-Lounge-Pant-Hero`** and `striped` — **product names, not Stripe.** Trap logged. | Live fetch 2026-10-09 |
| **Langham Hospitality Group** | langhamhotels.com | Hong Kong | Not researched | HK, Shanghai, Tokyo, Sydney, Jakarta | ❌ None found on the public pages. | Live fetch 2026-10-09 |
| **Shangri-La Group** | shangri-la.com | Hong Kong | Not researched | Across APAC | ❌ None found. Only WeChat **social** links (`wechatPopup*`) — **not WeChat Pay.** Context checked. | Live fetch 2026-10-09 |
| **Aman Resorts** | aman.com | Switzerland / Asia | Not researched | Japan, China, Indonesia, Thailand, Bhutan | ✅ **SynXis (Sabre) booking engine — same CRS as Mandarin Oriental.** No orchestrator found. | Live fetch 2026-10-09 |
| **Banyan Tree Holdings** | banyantree.com | Singapore | Not researched | Thailand, China, Indonesia, Vietnam, Korea | ✅ **SynXis (Sabre) booking engine — same CRS as Mandarin Oriental.** No orchestrator found. | Live fetch 2026-10-09 |
| **Four Seasons** | fourseasons.com | Canada | Not researched | Across APAC | ⬜ **Unexamined — HTTP 403 to my fetch.** | Live fetch 2026-10-09 |
| **Capella Hotel Group** | capellahotels.com | Singapore | Not researched | Singapore, Bangkok, Hanoi, Sanya, Sydney | ⬜ **Unexamined — HTTP 403 to my fetch.** | Live fetch 2026-10-09 |

### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| **The Oberoi Group** | oberoihotels.com | Luxury hotels | India, Indonesia, UAE | **Mandarin Oriental's own alliance partner** — the "O&MO Alliance" appears in MO's site navigation and `oberoihotels.com` is linked from MO property pages. Same guarantee-vs-prepay question, plus an Indian domestic stack (UPI, EMI, RBI e-mandate). | MO site nav + live fetch 2026-10-09 |
| **Six Senses Hotels Resorts Spas** | sixsenses.com | Luxury resorts | Thailand, Vietnam, Maldives, Singapore | Resort model skews to prepaid and deposit-bearing rates, so the rail question bites harder than at a city hotel | TAL |
| **Minor Hotels** | minorhotels.com | Hotels (Anantara, Avani) | Thailand, Australia, Maldives, China | Thai-HQ'd multi-brand operator — PromptPay and Thai instalments directly relevant | TAL |
| **Marina Bay Sands** | marinabaysands.com | Integrated resort | Singapore | Very high ATV, multi-outlet (hotel, retail, F&B, gaming), PayNow and Chinese wallets for inbound | TAL |
| **Dusit International** | dusit.com | Hotels | Thailand, Philippines, Vietnam, China | Thai-HQ'd, APAC-concentrated, same CRS-era architecture | TAL |
| **Indian Hotels Company (Taj)** | tajhotels.com | Luxury hotels | India, SEA, UK, UAE | **The clearest instalment and UPI story in the vertical**, plus RBI e-mandate exposure on advance-purchase rates | TAL |
| **Jin Jiang International** | jinjiang.com | Hotels | China, global | Chinese-domestic rails are the entire question | TAL |
| **H World Group** | hworld.com | Hotels | China, global | Chinese-domestic rails, very high transaction frequency at the budget end | TAL |

### 11C. Companies Recently Adopting Payment Orchestration

**No public case studies found of direct competitors adopting payment orchestration.**

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| — | — | — | — | No public information found. |

I probed eight luxury hotel groups' live sites and searched for orchestration adoption in the vertical. **Not one luxury hotel group was found using any orchestrator.** Three of the eight (Peninsula, Four Seasons, Capella) returned HTTP 403 and are **unexamined rather than clean**. The one orchestrator relationship named anywhere near this vertical was "Radisson," on a third-party AI-generated comparison page (rfp.wiki) which describes no deployment — **`[UNVERIFIED — search summary only, page not fetched]`, and I would not repeat it.** ICP row scored **0**.

**The genuinely usable competitive intelligence from this pass is different and better:** **Mandarin Oriental, Aman and Banyan Tree all run the same SynXis (Sabre Hospitality) booking engine.** Whatever Mandarin Oriental concludes about layering payments on top of SynXis is directly transferable to two other accounts, and vice versa.

### 11D. Prospect Scoring

Scored against the same 29-point matrix. **Only verified signals. Every row below is thin because these are drive-by observations from this run, not research runs of their own** — none has had a traffic pull, an entity check or a financial check.

| Company | Signal | Points | Status | Evidence Source |
|---|---|---|---|---|
| **Aman Resorts** | Same SynXis CRS as MO; luxury, high-ATV, APAC-heavy (Japan, China, Indonesia, Thailand, Bhutan) | — | ⬜ Not scored — insufficient verified signals | Live fetch 2026-10-09; TAL |
| **Banyan Tree** | Same SynXis CRS as MO; Singapore HQ; Thailand/China/Indonesia/Vietnam/Korea | — | ⬜ Not scored — insufficient verified signals | Live fetch 2026-10-09; TAL |
| **The Oberoi Group** | MO's own alliance partner; India + Indonesia; TAL carries ~$350M (FY25) **unverified** | — | ⬜ Not scored — insufficient verified signals | MO site nav; TAL |
| **The Peninsula Hotels** | HK HQ, APAC-concentrated, closest structural analogue to MO | — | ⬜ Not scored — site returned 403 | Live fetch 2026-10-09; TAL |
| **Rosewood / Langham / Shangri-La** | HK HQ, APAC-concentrated | — | ⬜ Not scored — no PSP or orchestrator found | Live fetch 2026-10-09; TAL |

**I am deliberately not producing scores for these.** A 29-point score built on one homepage fetch would be a fabricated number wearing a table, and the matrix explicitly says uncertain = 0. They are ranked below on signal strength only.

### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | **The Peninsula Hotels** | Direct competitor | HK, Tokyo, Shanghai, Beijing, Bangkok, Manila | Not scored | 🟢 Research next | Closest structural analogue to MO — HK-HQ'd ultra-luxury, APAC-concentrated; the settlement question will have the same shape | ✅ Yes (`1-to-outreach/the-peninsula-hotels.md`) |
| 2 | **Aman Resorts** | Direct competitor | Japan, China, Indonesia, Thailand, Bhutan | Not scored | 🟢 Research next | **Same SynXis booking engine as MO** — findings transfer directly | ✅ Yes |
| 3 | **Banyan Tree Holdings** | Direct competitor | Thailand, China, Indonesia, Vietnam, Korea | Not scored | 🟢 Research next | **Same SynXis booking engine as MO**; Singapore HQ, resort model skews prepaid | ✅ Yes |
| 4 | **Indian Hotels Company (Taj)** | Industry peer | India, SEA, UK, UAE | Not scored | 🟢 | Strongest UPI + EMI + RBI e-mandate story in the vertical | ✅ Yes |
| 5 | **Rosewood Hotel Group** | Direct competitor | HK, Bangkok, Phnom Penh, Beijing, Tokyo | Not scored | 🟢 | HK-HQ'd ultra-luxury; no PSP found on public pages | ✅ Yes (`1-to-outreach/rosewood-hotel-group.md`) |
| 6 | **Langham Hospitality Group** | Direct competitor | HK, Shanghai, Tokyo, Sydney, Jakarta | Not scored | 🟢 | HK-HQ'd; already queued; same per-property settlement question | ✅ Yes (`1-to-outreach/langham-hospitality-group.md`) |
| 7 | **The Oberoi Group** | Industry peer | India, Indonesia, UAE | Not scored | 🟢 | **MO's own O&MO Alliance partner** — a warm structural reference | ✅ Yes |
| 8 | **Minor Hotels** | Industry peer | Thailand, Australia, Maldives, China | Not scored | 🟡 | Thai-HQ'd multi-brand; PromptPay and Thai instalments | ✅ Yes |
| 9 | **Six Senses Hotels Resorts Spas** | Industry peer | Thailand, Vietnam, Maldives, Singapore | Not scored | 🟡 | Resort model = prepaid and deposit-bearing rates | ✅ Yes |
| 10 | **Marina Bay Sands** | Industry peer | Singapore | Not scored | 🟡 | Very high ATV, multi-outlet, PayNow + Chinese inbound wallets | ✅ Yes |

**Genuine finds not on the target list: Four Seasons** (Canada-HQ'd, but extensive APAC estate — an APAC-operating company with an out-of-territory HQ, so check the territory rule before adding) and **Capella Hotel Group** (**Singapore-HQ'd, squarely in territory, ultra-luxury, Singapore/Bangkok/Hanoi/Sanya/Sydney — and absent from a 1,220-row list that already contains 26 hospitality accounts**). Capella is the real omission and worth adding.

**Also flagged: a classification error in the target list.** `Shangri-La` is filed under **"Travel & Online Agencies (OTAs)"**, not "Hospitality & Lodging." It is a Hong Kong-HQ'd hotel group and will be missed by any industry filter on that list.

---

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| **Annual Revenue (USD) — the contracting entity** | **US$525.8m (FY2024)**, down 6% from US$558.1m (FY2023). By business activity: hotel ownership **453.6**, hotel & residences branding and management **95.3**, less intra-segment **(23.1)**. By geography: **Asia 232.2 (44.2%)**, EMEA 245.3 (46.7%), America 48.3 (9.2%). | ✅ Audited — [MOIL FY24 RNS 5036Z, 5 Mar 2025](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf) |
| **Combined total revenue of hotels under management** | **US$2,127.7m (FY2024)**, +13% from US$1,890.2m. H1 2025: **US$1,088m**, +11%. **NOT the contracting entity's revenue** — defined in the filing as *"turnover of the Group's subsidiary hotels in addition to 100% of revenue from associate, joint venture and managed hotels."* | ✅ Audited — same; H1 via [Yahoo Finance SG](https://sg.finance.yahoo.com/news/mandarin-oriental-reports-higher-underlying-035816370.html) |
| **⚠️ The target list's figure** | **"~$2B (FY24)" is the combined managed-hotel figure, attributed to the wrong entity.** It overstates MOIL by ~4× and MOHG (the Hong Kong management company) by far more. | **Corrected against the primary filing** |
| GMV / Gross Transaction Volume | **Not disclosed.** The closest public proxy is the US$2,127.7m combined figure, but most of that is third-party owners' revenue collected by their own merchant entities. | — |
| **Average Transaction Value (USD)** | **Not disclosed.** Proxies only: **RevPAR** FY24 Asia **US$242**, America **US$434**; group RevPAR H1 2025 **US$430** (+11%). FY25 RevPAR +10% like-for-like. **RevPAR is revenue per available room per night — it is NOT a transaction value.** A folio spans multiple nights plus F&B, spa and incidentals, so true ATV is materially higher and unknown. | ✅ RevPAR sourced; ATV **not found** |
| Est. Annual Transactions | **Not calculable from sourced inputs.** Converting RevPAR to folios needs room inventory and occupancy, neither of which MOIL publishes usably. **Any figure here would be an assumption dressed as a calculation.** | **Deliberately blank** |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ~90,000 guest folios/month group-wide. `[ASSUMPTION — not researched.]`** **Billing unit: guest folios** (one settled bill per stay) — not room nights, not guests, not web visits. Basis: 45 hotels (sourced) × ~250 keys (**assumed**; Manila Makati's 275 is the only sourced key count) × ~67% occupancy (**assumed**) ÷ ~2.5-night stay (**assumed**) ≈ ~3,000 folios/day. **Three of four inputs are assumptions.** 🔑 **And the number that matters to Yuno is smaller and unknown:** only ~12 of 45 hotels are MOIL-owned, brand.com is one channel among GDS/OTA/agent/corporate/phone, and **at 44 of 48 properties a brand.com booking produces a card guarantee rather than a settled transaction.** The count of transactions settled through any stack Yuno could orchestrate is **NOT ESTABLISHED and may today be near zero.** Scored at the band the assumption implies (**+3**); **an assumed figure cannot and did not fire the under-40,000 rejection.** | **ASSUMED — see the full disclosure in the ICP breakdown** |
| Active Customers / Users | **Not disclosed.** The Fans of M.O. recognition programme exists with tiers visible in the bundle (`FM`, `PE`, `FS`, `FE`, `FE+`, `PER`, `FR`, `FER`, `FER+` — the `FER`/`FR` tiers route to a **residences** dashboard). **No member count published.** | `main.js?v=2.42.0-beta.1-30`; count not found |
| **Primary Currency** | **USD for reporting.** Operationally multi-currency: each of the 48 properties carries its own `currency` / `currencyCn` in config, and the booking UI exposes a currency selector. The gift-card store is restricted to **EUR, GBP, HKD, SGD**. | ✅ MOIL FY24 RNS (USD reporting); homepage config and gift-card store `[Source Code]` |
| **Top 3 Markets by Revenue** | **By MOIL geographic segment (FY24): EMEA US$245.3m, Asia US$232.2m, America US$48.3m.** **By web traffic (Sep 2026): US 18.63%, Japan 7.28%, Brazil 6.04%.** ⚠️ **These two orderings disagree sharply, and the disagreement is the point** — MOIL's revenue follows the 12 hotels it *owns* (heavily European), while demand follows the brand globally. **Both presented; neither reconciled.** | ✅ MOIL FY24 RNS; SimilarWeb (supplied 2026-10-09) |
| **Billing channel split (web vs app store)** | **Not applicable, and verified as such.** Hotel room bookings and folios are not in-app-purchase goods and do not route through Apple or Google billing. No subscription product and no IAP code path was found in the bundle. **The app-store override does not apply to this account.** | Assessed against `main.js?v=2.42.0-beta.1-30` |
| **Branded residences — the flow** | 🔑 **NOT a payment flow.** `/en/residences` has **zero** payment functionality — no price, no deposit, no reservation fee, no card field; only "Contact Us" and "Submit Enquiry." MOIL books residences income as **one-off branding fees** (FY24 underlying profit fell 8% *"due to lower one-off residences branding fees"*). The purchase itself is a real-estate conveyance between buyer and developer. **15 branded residences at FY25.** Residences *management* entities exist in the UK, Macau, Spain, Taiwan and Turkey, which plausibly bill owner service charges — `[INFERENCE, not confirmed; no public evidence of a payment stack]`. | ✅ [MO residences page](https://www.mandarinoriental.com/en/residences) fetched 2026-10-09; [MOIL FY24 RNS](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf) |
| **Other revenue lines, and whose stack they run on** | **Dining:** off-domain on **SevenRooms** (MO venue slugs at Tokyo and HK) — deposits settle through SevenRooms' integration, not MO's. **Spa:** **SpaSoft** links plus a dedicated (dark) Planet redirect path (`pp_spa_redirect_timestamp`). **Gift cards & shop:** **live Stripe** via **Techsembly**, operated by **Aven Hospitality**, cards only, 4 currencies. **Exceptional Homes (36 villas):** MO *"acts as booking agent and does not own, operate or manage the homes"* — payment flow not established. **Outlets:** the privacy policy discloses sharing with *"organisations which own, manage or operate the spas, restaurants, health clubs, and other outlets at our properties"* — i.e. **outlets can be third-party operators and therefore separate merchants of record.** | ✅ Live fetches 2026-10-09; [MO privacy policy](https://www.mandarinoriental.com/en/privacy-policy) |
| Net debt / balance sheet | Net debt fell from US$225m (31 Dec 2023) to **US$94m** (31 Dec 2024); gearing 2% of adjusted shareholders' funds. NAV/share US$2.25; adjusted NAV/share US$3.50. Capital commitments US$192.3m. **Take-private priced at US$3.35/share total.** | ✅ [MOIL FY24 RNS](https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf); [Slaughter and May](https://www.slaughterandmay.com/recent-work/mandarin-oriental-transaction-committee-on-the-recommended-cash-acquisition-by-jardine-updated/) |
| **⚠️ Forward disclosure** | **MOIL delisted 19–20 Jan 2026. The FY2025 release (16 Mar 2026) published RevPAR and portfolio counts but NO revenue, EBITDA or profit line — the first results release since going private. FY2024 is the last complete public financial picture, and there will be no further audited public filings.** Any business case built after FY2024 will depend on figures the company chooses to volunteer, or on Jardine Matheson's consolidated disclosures. | ✅ [FY25 release](https://press.mandarinoriental.com/annual-results-2025/?lang=eng); [Conyers](https://www.conyers.com/publications/view/mandarin-oriental-international-limited-privatisation-and-delisting/) |

---

## Overall Research Confidence

**HIGH on architecture and entity structure. MEDIUM on commercials. LOW on transaction volume and acquirers.**

**No downgrade for environment.** Both WebFetch and Bash `curl` worked throughout: WebFetch returned genuine HTTP responses (including a real 404 on one guessed URL, which proved reachability rather than blocking), and `curl` returned HTTP 200 with full headers on every target including the 3.3MB application bundle, two PDFs and eight competitor sites. **Section 8 is completed from first-hand observation, not marked inaccessible.**

**Traffic data was SUPPLIED, not API-sourced and not estimated.** `accounts/traffic/mandarin-oriental-hotel-group.md`, SimilarWeb PRO, Sep 2026, supplied by Prateek 2026-10-09, used verbatim and not re-researched — as instructed. It is a **top-10 country cut**, so the 19.54% APAC figure is a visible floor. The country profile drives the APM analysis and two ICP rows, and it is the strongest input in the report.

**What was strong:**
- **Sections 3, 4 and 8** are unusually well evidenced. The payment stack was read directly out of Mandarin Oriental's own live production configuration and application bundle — 48 per-property payment configs, a live VGS vault ID, a live Stripe key, two mutually exclusive card code paths and the per-property booking terms in the company's own words. This is `[Source Code]`-grade evidence throughout, not inference.
- **Sections 2, 6, 7 and 12** rest on MOIL's **audited FY2024 preliminary results filed through a UK Regulatory Information Service** and retrieved from the Bermuda Stock Exchange, plus the privacy policy effective 10 April 2026 naming ~25 legal entities, plus the take-private confirmed by the law firms on both sides of it.
- The settlement question — the one that decides the account — is **answered from the merchant's own words, per property**, not inferred.

**What was limited, and why:**
- **Acquirers: nothing.** Not one acquirer for any of 48 properties, central or local. This is the single biggest gap and it is structural, not a search failure: property-level acquiring through Oracle OPERA leaves no public footprint. I scored it as nothing rather than naming a plausible guess.
- **Transaction volume: assumed.** No booking, folio or transaction count is published anywhere, and the inputs needed to derive one are not public. Three of four inputs in my assumption are mine.
- **Complaints: nothing found.** Searched and empty. A real zero, not an unexamined one.
- **FY2025 financials: not obtainable.** The company went private in January 2026 and stopped publishing revenue and profit.
- **Competitor stacks: three of eight sites returned HTTP 403** (Peninsula, Four Seasons, Capella) and are unexamined rather than clean.
- **Regulatory sourcing: deliberately thin.** I cite **no** APAC regulatory rule as fact. Japan's 3DS requirement is carried only on vendor secondary pages that disagree on its issuer; no primary METI or JCA text was retrieved; QRIS figures come from news outlets quoting Bank Indonesia rather than bi.go.id. **No acquiring gate is asserted for any market.**
- **Parallel sub-agents: not available.** No Agent or Task tool exists in this environment, so Phase 2's four parallel agents were executed sequentially by me, with independent tool calls batched where they had no dependencies. Coverage follows the method's search and fetch allocation; concurrency does not. **This did not reduce evidence quality — the decisive findings came from direct fetches rather than searches — but it is a deviation from the method and is recorded as one.**

---

## Manual Research Recommendations

> **Area:** **Monthly transaction count, and specifically the count of *settled* transactions.** The ICP figure is `[ASSUMPTION — not researched]`.
> **Why it matters:** It is the only signal that can reject an account on its own, and for this merchant the unit is genuinely ambiguous — group-wide folios comfortably clear 40,000, but transactions settled through any central stack may be near zero. The business case cannot be sized without it.
> **Suggested manual action:** Ask directly on the first call: *"How many card transactions a month go through mandarinoriental.com and actually settle, as opposed to sitting as a guarantee?"* Then ask the same for the gift-card store, which is the one surface where MOHG is definitely the merchant of record.

> **Area:** **WHO OWNS THE ACQUIRING RELATIONSHIP — the question that decides whether this account is real.**
> **Why it matters:** If each property's acquirer belongs to that property's owner, there is no central contract for Yuno to win and the buyer is not at MOHG Hong Kong at all. If MOHG negotiates group acquiring that properties draw on, there is.
> **Suggested manual action:** One question: *"When a guest is charged at check-out in Tokyo, whose merchant account does that money land in — yours, or the hotel owner's?"* Follow with the same for a managed property such as Jakarta (owned by P.T. Astra Land Indonesia since 2023).

> **Area:** **Why Planet Payment is switched off at all 48 properties.**
> **Why it matters:** The whole motion turns on this. Built-and-never-launched is an opportunity; switched-off-after-a-bad-experience is an objection to handle; deliberately-off-because-settlement-is-property-side means the central stack is doing exactly what it was designed to do and Yuno's entry point is elsewhere entirely.
> **Suggested manual action:** Ask it as a genuine question, because it is one: *"You've got a complete Planet integration in production that looks disabled everywhere — was that deliberate?"*

> **Area:** **Checkout verification on the four prepayment properties.**
> **Why it matters:** Beijing-Qianmen, Kuala Lumpur, Bangkok suites and Lucerne are the only four flows where money must move at booking. They are the only places the live settlement path — and therefore the real acquirer — is observable from outside.
> **Suggested manual action:** With a VPN, walk a **Beijing – Qianmen** rate and a **Kuala Lumpur** rate to the card step with DevTools open. Watch for `pay.datatrans.com` traffic versus `vgs-live.sitecore.moweb-acc.com`, and capture whatever acquirer or 3DS endpoint appears. Note the recorded trap: a client-side-rendered method list can come from a vendor dashboard, so confirm on the wire rather than in the bundle.

> **Area:** **Japan — the unnamed legal entity, and the 3DS question.**
> **Why it matters:** Japan is 7.28% of traffic, hosts an Owned Hotel, and is the one market the privacy policy lists without naming a local management entity. Separately, the 3DS position needs the primary rule text before anyone mentions it.
> **Suggested manual action:** Search the Japanese corporate-number (hojin bangou) registry for the Mandarin Oriental Tokyo operating entity. Separately, pull the **primary METI / Japan Credit Association Credit Card Security Guidelines text** and establish whether a card taken as a guarantee at booking and charged at the property falls inside or outside its scope. **Do not raise 3DS with Mandarin Oriental until that is settled.**

> **Area:** **Regulatory acquiring gates — none sourced in this run.**
> **Why it matters:** The "local rail or licensing gap" argument would be considerably stronger with a sourced gate in Japan, Indonesia or China, and considerably weaker if there is none. I asserted none in either direction.
> **Suggested manual action:** Pull current primary sources for Bank Indonesia PJP licensing categories and the Chinese cross-border collection regime, and establish whether Mandarin Oriental's per-property settlement model sidesteps them entirely — which, if settlement is domestic and property-side, it probably does. **That answer may close the rail argument rather than open it, and it is better to know.**

> **Area:** **The gift-card store as a beachhead.**
> **Why it matters:** It is the one surface where Mandarin Oriental Hotel Group Limited is demonstrably the merchant of record, where a live PSP relationship already exists (Stripe via Techsembly), and where the gaps are embarrassing and cheap to fix: cards only, no wallets, four currencies, no JPY despite Japan being the #2 market.
> **Suggested manual action:** Check whether the Techsembly contract permits a different gateway — the config's empty `adyenOriginKey` suggests the platform supports alternatives. If it does, this is a small, fast, low-politics first project with a named contracting entity.

> **Area:** **Residences owner service charges — the only residences flow worth a question.**
> **Why it matters:** Residences are not a payment flow (confirmed), but Mandarin Oriental Residences Management entities in the UK, Macau, Spain, Taiwan and Turkey plausibly bill recurring charges to owners across multiple currencies. `[INFERENCE, not confirmed.]`
> **Suggested manual action:** Ask once, neutrally: *"Do the residences management entities collect owner service charges, and if so how?"* **Do not assert that they do.**

---

## Appendix: All Source URLs

**First-hand fetches, all performed 2026-10-09 (HTTP status and byte count recorded; every asset re-fetched this run, nothing reused from any prior scratchpad):**
- `https://www.mandarinoriental.com/en` — 200, 1,392,974 bytes (CSP header; 48-property payment config; per-property booking terms; SynXis link; external hosts)
- `https://www.mandarinoriental.com/corporate/main.js?v=2.42.0-beta.1-30` — 200, 3,334,390 bytes (VGS vault config, Datatrans/Planet integration, 3DS2 payload, card-brand map, OPERA key, SpaSoft, orphan-reservation logic)
- `https://www.mandarinoriental.com/en/privacy-policy` — 200 (effective 10 April 2026; ~25 local management entities; Exceptional Homes booking-agent disclosure; third-party outlet operators)
- `https://www.mandarinoriental.com/en/residences` — 200 (no payment functionality)
- `https://giftcards.mandarinoriental.com/egift-card-031505` — 200 (live Stripe key and Connect account, Techsembly, Givex, empty Adyen key, null PayPal, currencies, payment marks)
- `https://na.shopmo.com/` — 200 · `https://shopmo.com/` — 200 · `https://www.shopmo.cn/` — 200, **301s to `na.shopmo.com/index.aspx?referrer=cn`** · `https://na.shopmo.com/checkout` — 404
- `https://be.synxis.com/?chain=507` — 200 (Sabre Hospitality CSP: Modirum, DerbySoft, Hopper, Amex, Apple CDN)
- `https://www.mandarinoriental.com/en/tokyo/nihonbashi/dine` — 200 (SevenRooms, 491 refs) · `.../en/hong-kong/victoria-harbour/dine/mandarin-grill-and-bar` — 200 · `.../en/tokyo/nihonbashi/wellness` — 200
- Competitor probes: `peninsula.com` 403 · `rosewoodhotels.com` 200 · `shangri-la.com` 200 · `langhamhotels.com` 200 · `fourseasons.com` 403 · `aman.com` 200 (SynXis) · `capellahotels.com` 403 · `banyantree.com` 200 (SynXis)

**Filings and regulatory announcements:**
- https://www.bsx.com/CompanyDocuments/132/2025-03-05%20-%20MOIL0305.pdf — **MOIL 2024 Preliminary Announcement of Results, RNS 5036Z, 5 March 2025** (the primary financial source for this report)
- https://links.sgx.com/1.0.0/corporate-announcements/5ES6E1GAXEGYO3PR/661332_MOIL0416.pdf — MOIL notification of major interest in shares, 16 April 2021 (JSL 79.45%)
- https://www.bsx.com/company_details.php?CompanyID=132 — Bermuda Stock Exchange, MOIL
- https://www.investegate.co.uk/announcement/rns/jardine-matheson-holdings-ltd-singapore-reg---jar/cancellation-of-the-listings-of-mandarin-oriental/9369226 — Cancellation of the Listings of Mandarin Oriental
- https://www.conyers.com/publications/view/mandarin-oriental-international-limited-privatisation-and-delisting/ — Conyers (Bermuda counsel), privatisation and delisting
- https://www.slaughterandmay.com/recent-work/mandarin-oriental-transaction-committee-on-the-recommended-cash-acquisition-by-jardine-updated/ — Slaughter and May (adviser to the MOIL Transaction Committee)

**Company press and results:**
- https://press.mandarinoriental.com/annual-results-2025/?lang=eng — FY2025 results release, 16 March 2026
- https://press.mandarinoriental.com/?p=12035 — FY2024 preliminary results
- https://www.hospitalitynet.org/news/4131468/mandarin-oriental-reports-strong-business-performance-for-2025
- https://sg.finance.yahoo.com/news/mandarin-oriental-reports-higher-underlying-035816370.html — H1 2025
- https://www.investing.com/news/company-news/mandarin-oriental-reports-strong-management-business-growth-in-h1-2025-93CH-4155000
- https://www.traveldailynews.com/hospitality/mandarin-oriental-announced-combined-total-revenue-up-to-us2-1bn-for-2024/
- https://stockanalysis.com/quote/sgx/M04/revenue/ — MOIL (SGX:M04) revenue history

**Expansion:**
- https://ayalaland.com/news/ayala-land-and-mandarin-oriental-officials-visit-new-mandarin-oriental-site-on-the-road-to-opening-in-2026
- https://www.ttgasia.com/2024/04/29/new-mandarin-oriental-to-open-in-philippines-makati-city-in-2026/
- https://journaldespalaces.com/en/pressrelease-78578-philippines-hotel-opening-mandarin-oriental-announces-its-return-to-manila.html

**Vendors:**
- https://datatrans.ch/en/know-how/news/detail/datatrans-enters-next-development-phase-new-owners — Datatrans / Advent / Eurazeo
- https://datatrans.weareplanet.com/ — "Datatrans from Planet"
- https://www.businesswire.com/news/home/20220302005050/fr — Planet combination with Proximis, Datatrans, protel, Hoist
- https://en.wikipedia.org/wiki/Planet_(company)
- https://www.hotel-online.com/News/PR2009_2nd/Apr09_SynXisMandarin.html — SynXis RedX for MOHG, April 2009 (historic, 17 years old)
- https://new.hospitalityupgrade.com/news/synxis-to-provide-redx-distribution-management-system-for-mandarin-oriental-hotel-group
- https://au.fourth.com/case-study/mandarin-oriental-hotel-group — Fourth workforce management (not payments)

**Market and regulatory context (secondary — flagged as such in text, cited for nothing as fact):**
- https://www.adyen.com/knowledge-hub/post-3ds-mandate-in-japan.md · https://merchantriskcouncil.org/learning/resource-center/member-news/blog/2025/mrc-japan-credit-association-emv-3ds-mandate · https://stripe.com/resources/more/3d-secure-mandatory-for-ecommerce-in-japan — Japan EMV 3DS requirement (sources disagree on issuer; no primary text retrieved)
- https://keuangan.kontan.co.id/news/bi-mencatat-nilai-transaksi-qris-capai-rp-16448-triliun-pada-januari-2026 · https://databoks.katadata.co.id/en/finance/statistics/6944c027919cc/the-number-of-qris-users-increased-in-q3-2025 — QRIS volume (news quoting Bank Indonesia; bi.go.id not reached)

**Internal:**
- `accounts/traffic/mandarin-oriental-hotel-group.md` — SimilarWeb PRO, Sep 2026, supplied by Prateek 2026-10-09
- `accounts/apac-tal.csv` — target account list (1,220 rows); Mandarin Oriental row's "~$2B (FY24)" **corrected** against the primary filing
- `1-to-outreach/mandarin-oriental-hotel-group.md` — stub; each hypothesis verified or dropped in this report
- `.claude/reference/apac-payments.md` — checklist, **cited as a source for nothing**

</details>
