# TRAC (Astra)

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 11 / 29 → 🟢 **Medium**
**Industry:** Vehicle rental & mobility — corporate fleet leasing, retail self-drive, chauffeur, bus, motorcycle, airport transfer, attractions · **HQ:** **PT Serasi Autoraya ("SERA")**, Indonesia — **99.9999% owned by PT Astra International Tbk** (IDX: ASII). TRAC is a brand, not a legal entity · **Researched:** 2026-10-06 · **First email sent:** —
**Motion:** ✅ **GREENFIELD — a single PSP (Xendit), hard-wired, no orchestration, no failover, no routing layer.**

---

> ## ⛔ MY OWN BRIEF'S HYPOTHESIS WAS WRONG — and the correction is the account
>
> I briefed the research on the premise that TRAC is an invoiced B2B fleet-leasing business with a brochure site and nothing to orchestrate. **That is disproved.** The reason it looked right is a structural fact that matters for the whole account: **the marketing site and the transacting site are two different properties.**
>
> **I verified both myself:**
>
> | Property | Role | My fetch |
> |---|---|---|
> | `www.trac.astra.co.id/reservasi` | **Brochure / lead-gen only** | HTTP 200, **343,666 bytes**, and `payment` = **0**, `bayar` = **0**, `pembayaran` = **0**, `xendit` = **0** |
> | **`tractogo.trac.astra.co.id/car-rental`** | **The real checkout** | HTTP 200, **29,820 bytes**, `noindex, nofollow` |
>
> That zero on a 343KB page is a **genuine** zero, not a wrong-file artefact — the same control on the FAQ page returns 48 `bayar` / 36 `pembayaran`, and on the TRACtoGo payment bundle **231** `payment`. The full Next.js route manifest was fetched (`_buildManifest.js`, 6,677 bytes, **78 routes**) and **contains no checkout, payment, cart or order route anywhere.** `/checkout`, `/pembayaran`, `/payment`, `/pesan`, `/booking`, `/cart`, `/order`, `/sewa` all return **404**.
>
> **🔑 Consequence for sizing: the supplied SimilarWeb figure of 183,693 visits/mo for `trac.astra.co.id` almost certainly does NOT measure the transacting property.** `tractogo.*` is a sub-subdomain, explicitly `noindex, nofollow`, and every "Pesan"/"Book" CTA on the marketing site points at it (`href="https://tractogo.trac.astra.co.id/car-rental"`, 4× in the homepage HTML). **Any volume model built off 183,693 understates the business.** `[INFERENCE, not confirmed]` that SimilarWeb excludes it.

---

> ## ⭐ THE FINDING — Xendit, loaded blocking, as the only third-party host on the checkout
>
> **I verified this myself.** `https://tractogo.trac.astra.co.id/car-rental` carries **three** occurrences of `https://js.xendit.co/cards-session.min.js` in its `<head>`, including a `preload` and a `beforeInteractive` strategy:
>
> ```html
> <link rel="preload" href="https://js.xendit.co/cards-session.min.js" as="script"/>
> <script>(self.__next_s=self.__next_s||[]).push(["https://js.xendit.co/cards-session.min.js",{...}])</script>
> ["$","$L12",null,{"nonce":"","strategy":"beforeInteractive","type":"text/javascript",
>  "src":"https://js.xendit.co/cards-session.min.js"}]
> ```
>
> **`js.xendit.co` is the ONLY third-party host on the page besides Google Tag Manager.** `beforeInteractive` + `preload` means a **hard, blocking, first-party dependency on the checkout's critical path** — not a tag-manager afterthought.
>
> And the payment bundle (`chunks/8578-0af686b3b524b367.js`, HTTP 200, **4,320,135 bytes**, control: **231** `payment` / 30 `bayar` / 20 `pembayaran` / 10 `xendit`) carries a second Xendit SDK **with bespoke error handling**:
> ```
> 'https://js.xendit.co/v1/xendit.min.js'   'xendit-script'
> 'Xendit\x20script\x20failed\x20to\x20load'      'XENDIT_UAS'   ← 3DS / auth service
> 'payment':{'paymentMethodId':…,'tokenId':…,'cvv':…}
> 'PaymentMethod':{…,'CC_Tokenization':…}      'modal-checkout-cc'
> ```
> **Direct card acceptance with Xendit tokenisation. One PSP. No abstraction layer, no second PSP, no router.** Zero hits for Adyen, Stripe, Checkout.com, 2C2P, Midtrans, Primer, Spreedly, IXOPAY, Gr4vy or Juspay.
>
> **`'Xendit script failed to load'` is a hard-coded single point of failure on the checkout's critical path, and they wrote the error message themselves.**

---

> ## 🎯 THE HOOK — recurring renewals on contracted fleet revenue, with no visible retry logic
>
> This is the sharpest and most quantifiable conversation on the account. From the same bundle:
> ```
> TRAC_TD_SUBSCRIBE_CHECKOUT          TRAC_TD_SUBSCRIBE_ORDER
> ORDER_RESUBSCRIBE_LONGTERM          ORDER_RESUBSCRIBE_PAYMENT_LONGTERM   ← recurring renewal endpoint
> TRAC_ORDER_END_SUBSCRIPTION         TRAC_ORDER_END_SUBSCRIPTION_REASONS
> TRAC_ORDER_DETAIL_LONGTERM          TRAC_TD_RESCHEDULE_LONG_TERM
> carRentalLongterm / isLongterm / resubscribe / setSubscribtion / endSubscription
> ```
> **`ORDER_RESUBSCRIBE_PAYMENT_LONGTERM` is a recurring-payment renewal endpoint on long-term rental.** Card-on-file lifecycle, retry/dunning and involuntary churn are live concerns, and **no retry, dunning or account-updater logic is visible anywhere.** Involuntary churn on *contracted fleet revenue* is a far better number to argue about than one-off retail bookings.
>
> **Second hook — "Pick Up Now" turned authorisation latency into a product problem.** Launched 2026 (reported 16 July 2026 and 23 September 2026): instant/on-demand rental and airport transfer with **no day-before reservation.** Confirmed live in code — the homepage banner reads *"✨ Baru! Pick up now. Pesan mobil kini lebih cepat dan praktis"* linking to the checkout, with `Pick_SD_CarDetail_PilihMetodePembayaran` / `Pick_WD_...` analytics events. **Instant booking means instant payment confirmation. Auth latency and success rate stop being a finance metric and become a customer-experience metric.**
>
> **Third hook — two routing constraints a single-PSP integration cannot express:**
> - **AstraPay is a subsidised related-party method.** SERA ran a co-marketing promo (10% cashback + up to Rp50,000 Astra Poin on TRAC rentals paid with AstraPay, **16 May – 31 Dec 2025**), and AstraPay is operated by **PT Astra Digital Arta**, part of Astra Financial. **TRAC has a strategic reason to steer volume to a group wallet regardless of cost or conversion** — exactly the kind of routing rule an orchestrator expresses cleanly.
> - **A bank super-app embedded channel nobody has written about.** The live bundle carries `MandiriSukhaAuthWrapper`, `AUTH_REQUEST_KYC_MANDIRI_SUKHA`, `mandiriSukhaUser`, `mandiriSukha` — **TRAC is distributing rentals inside Bank Mandiri's Livin' Sukha lifestyle app with SSO.** No press release found; this is a **code-only finding**, which makes it a strong, non-obvious opener.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Astra's vehicle-rental and mobility arm, founded 1986 with "five cars for rent." Now **35,000 vehicles** across "more than 20 large cities", Sumatra to Papua. Operates a genuinely multi-product transactional platform: **car (self-drive and with-driver), bus, motorcycle, airport transfer, attractions/tourism tickets, and long-term subscription rental** — each with its own confirmed checkout and payment-method selector.

**SimilarWeb:** 183,693 visits (Aug 2026), +38.71% MoM, **50.13% desktop** (highest in the batch, consistent with B2B booking), Indonesia 83.32%, **Singapore 15.06%**. ⚠️ **But see above — this measures the brochure, not the checkout.**

### Transaction volume — DERIVED, straddles the gate, arithmetic shown
**Approach A — fleet bottom-up (most defensible):**
```
Total fleet (SOURCED, undated marketing page)        35,000 vehicles
Under contract Q3 2025 (SOURCED, Astra release)      26,500  ← long-term corporate
Short-term/retail available (DERIVED)              =  8,500  ⚠️ fragile: subtracts an
                                                              undated figure from a dated one
× ASSUMED 65% utilisation ÷ ASSUMED 3-day avg rental
  → 30 × 0.65 ÷ 3 = 6.5 bookings per unit per month
8,500 × 6.5                                        ≈ 55,000 retail bookings/month
Conservative variant (5,000 units, 55%, 4-day)     ≈ 20,600/month
```
**Approach B — corporate:** 3,000+ corporate customers × ASSUMED 1 invoice/month ≈ **3,000 invoiced transactions/month.** These are TOP/bank-transfer, **not** online card/wallet — they do **not** count toward the gate, but they do count toward an invoice-collection use case.

**Approach C — app sanity check:** Play Store **500K+ downloads, 2,669 ratings, 4.84 stars** (verified in raw HTML: `"ratingValue":"4.838709831237793","ratingCount":"2669"`). ASSUMED ratings ≈ 0.2% of lifetime transacting users → ~1.3M lifetime bookings over ~7 years → **~15,000/month average, trending higher now.**

**Not counted in any of the above:** bus rental, airport transfer, motorcycle rental, attractions tickets, and long-term subscription renewals — **five additional confirmed transacting product lines.**

**🎯 Gate ruling: NOT FAILED.** The derived range **~20,600–55,000/month for car retail alone straddles 40,000**, and the low end rests entirely on ASSUMED utilisation and duration. **Per the rule, an assumption can never reject.** There is **no SOURCED transaction count in either direction.** Proceed.

### ⚠️ The revenue split could NOT be established — the central quantitative gap
Astra does not break out SERA revenue at all. TRAC segments itself as **long-term = >1 year = corporate** vs **short-term = <1 year = individual**. What is known: car rental was **66% of SERA revenue in FY2019**; SERA total revenue **Rp5.3 trillion in FY2022** (+10.9%) `[UNVERIFIED — search summary]`. **TRAC's own scale is roughly Rp3.5 trillion `[DERIVED — mixes a 2019 ratio with a 2022 total; order-of-magnitude only]`.**

**🛑 Astra group revenue of Rp243.6 trillion (9M to 30 Sep 2025) is NOT TRAC's revenue. Do not conflate them.**

**The crucial structural point: the invoiced-B2B side does not remove the consumer side — it sits alongside it in the same codebase.** Corporate customers are not off-platform; they self-serve with cost centres and approval chains and are *then* invoiced.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

> **Not yet generated.** Run `/full-outreach TRAC` to compose the 12-touch sequence into this section.
>
> **Motion is GREENFIELD.** Observations may note the absence of a routing or failover layer.
>
> **🛑 Four angles to AVOID, each because the research closed them off:**
> 1. **Deposit / pre-authorisation holds** — none exist. Established three ways (Section 6).
> 2. **Customer payment complaints** — none found, and the app sits at **4.84 stars**. A "your customers are complaining" angle will not land.
> 3. **Cross-border approval rates** — this is domestic IDR.
> 4. **"Add more local methods"** — **Xendit already aggregates 38+ Indonesian methods.** This angle is pre-empted and claiming it would expose a lack of homework.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

## Section 1: Entities

- **Operating entity: PT Serasi Autoraya ("SERA").** TRAC (full brand *"TRAC – Astra Rent a Car"*) is a **brand, not a legal entity.** Confirmed on `trac.astra.co.id/en/about/profile`.
- **Ownership: 99.9999% owned by PT Astra International Tbk** (IDX: ASII). Brand became "TRAC-Astra Rent a Car" on **5 October 2001.** `[UNVERIFIED — search summary]`
- **Astra reporting segment:** SERA sits under Astra's **Infrastructure and Logistics** segment, described in the Q3 2025 release as *"the Group's transportation and logistics solutions business."*
- **SERA's three business lines:** (1) **Transportation Solutions** — TRAC; (2) **Pre-owned car sales** — mobil88 and IBID Balai Lelang Serasi; (3) **Logistics** — SELOG.
- **Merchant of record for a retail rental: PT Serasi Autoraya** `[INFERENCE, not confirmed]`. No separate payment-entity disclosure was found, and the T&C page (`/syarat-ketentuan-customer`, HTTP 200, 110,823 bytes) **was not parsed.**
- **🛑 Singapore entity: NOT FOUND.** Searched specifically. SERA's disclosed structure is entirely Indonesian. **There is no evidence of a genuine Singapore operation.**
- **Infrastructure:** Microsoft Azure — Azure Blob Storage (`omnispace.blob.core.windows.net`, 349 references; `tracomni.blob.core.windows.net`, 8) + **Azure API Management** (`Ocp-Apim-Subscription-Key`). Next.js front ends, **Datadog RUM** (`'DATADOG RUM: Syncing User (TD/Cookie)'`), GTM-KPDXT6BP.
- ⚠️ Incidental: **`dev.trac.astra.co.id` is publicly indexed** — a dev environment exposed to search engines. Minor hygiene note.

## Section 2: 🛑 There is NO shared Astra group payment layer

This was the highest-value question in the brief and the answer is clear.

| Property | Finding |
|---|---|
| **`www.seva.id`** (Astra's car marketplace) | HTTP 200, 233,421 bytes. **48 `payment` hits — but every one is a car-loan instalment calculator field** (`"installment":3080000`, `"totalFirstPayment":30610000`, `"totalBayar":215410000`, `"insuranceRate":13.29`). **Zero** Xendit/Midtrans/AstraPay/QRIS. **Seva is a marketplace and financing lead-gen tool with NO payment acceptance.** Different Next.js build fingerprint from TRAC |
| `www.ibid.astra.co.id` | First probe 200 (3,328 B, redirect); body fetch returned **curl 52, empty reply.** Not retried |
| `www.mobil88.astra.co.id` | **Redirects to `olx.co.id/olxmobbi/`** — folded into **OLXmobbi.** Corroborated by Astra's Q3 2025 release: *"OLXmobbi, the Group's used car business, booked a 24% increase in used car sales to 23,900 units"* |

**Each Astra property runs its own stack. The buying centre is TRAC/SERA, not Astra group IT.** Good news for a direct approach — but see the AstraPay caveat below.

## Section 3: AstraPay — a captive METHOD, not a captive PLATFORM

This is the nuance the brief asked to chase, and the answer matters.

1. `'AstrapaySignature'` is present in the live payment bundle — an API request-signing field, i.e. a **real integration, not a logo.**
2. First-party TRAC content lists **"Astra Pay"** as one of six e-wallets at checkout.
3. **Live commercial co-marketing:** SERA's newsroom published *"Kolaborasi dengan AstraPay, Rental Mobil TRAC Cashback Rp50,000"* (June 2025) — 10% cashback + Astra Poin up to Rp50,000, **16 May – 31 Dec 2025.** ⚠️ **The SERA page returned HTTP 404 on fetch** (moved/removed); not retried. `[UNVERIFIED — search summary only]`
4. AstraPay runs further TRAC promos (`astrapay.com/promo/tracmaret`). `[UNVERIFIED]`
5. AstraPay is operated by **PT Astra Digital Arta**, part of Astra Financial; e-wallet launched 2020, public launch Sept 2021. `[UNVERIFIED]`
6. **AstraPay is a standard e-wallet channel within Xendit's own catalogue**, alongside GoPay, OVO, DANA, ShopeePay, LinkAja and Jenius Pay.

**`[INFERENCE, not confirmed]`: AstraPay is most likely reached THROUGH Xendit, not via a separate Astra-internal payment platform.** The `AstrapaySignature` string hints there *may* additionally be a direct signed API integration — obfuscation blocked resolution. **🔑 This is the single highest-value discovery-call question.**

## Section 4: Rail table

| Rail | Status | Source |
|---|---|---|
| **Credit card (CNP)** | ✅ CONFIRMED | FAQ *"kartu kredit"*; `CC_Tokenization`/`tokenId`/`cvv`/`modal-checkout-cc` |
| **Credit-card instalments (cicilan)** | ✅ CONFIRMED | TRAC blog — **3–12 months** depending on bank |
| **Bank VA — Mandiri, BNI, BCA, Permata** | ✅ CONFIRMED | TRAC blog, verbatim: *"Mandiri, BNI, BCA, serta Permata"*; `MsBankId`/`MsBankName`/`PAYMENT_INSTRUCTION` |
| VA — **BRI**, CIMB | ❌ **NOT FOUND** | absent from the published list |
| **QRIS** | ✅ CONFIRMED | **Dedicated webpack modules per product line:** `CarRentalPaymentQRIS`, `BusRentalPaymentQRIS`, `BusRentalPaymentQRISSettlement`, `payment.howToPayQRIS.`, `media/QRIS.a4206371.png` + Indonesian scan-to-pay instructions |
| **GoPay · OVO · DANA · ShopeePay · LinkAja · AstraPay** | ✅ CONFIRMED | TRAC blog, verbatim: *"Gopay, OVO, DANA, Shopee Pay, Link Aja, hingga Astra Pay"* |
| **Manual bank transfer** | ✅ CONFIRMED | FAQ, for foreign customers |
| **Invoice / term billing (TOP)** | ✅ CONFIRMED | FAQ: *"pembayaran dengan sistem TOP… wajib melengkapi dokumen legalitas perusahaan dan membuat kontrak korporat"*; `TRAC_TD_PAYMENT_INVOICE`/`_LIST`/`_STATUS` |
| **Recurring / subscription billing** | ✅ CONFIRMED | `ORDER_RESUBSCRIBE_PAYMENT_LONGTERM`, `TRAC_TD_SUBSCRIBE_CHECKOUT` |
| **BNPL** (Kredivo/Akulaku/Indodana/Atome) | ❌ NOT FOUND | 0 bundle hits, absent from published lists |
| **Retail OTC cash** (Alfamart/Indomaret) | ❌ NOT FOUND | 0 hits |
| Corporate card acceptance | ❌ NOT FOUND | corporate volume goes to TOP invoicing instead |
| Debit / GPN local cards | ❌ NOT FOUND | not separately named |

**Analytics events prove every product line has its own payment-method selector and pay step:**
```
Car_SD_CarDetail_PilihMetodePembayaran / Car_SD_CarDetail_Bayar      (SD = self-drive)
Car_WD_CarDetail_PilihMetodePembayaran / Car_WD_CarDetail_Bayar      (WD = with driver)
Pick_SD_CarDetail_PilihMetodePembayaran / Pick_WD_...                (Pick Up Now)
Bus_PilihMetodePembayaran / Bus_Bayar
Airport_CarDetail_PilihMetodePembayaran / Airport_CarDetail_Bayar
Attractions_PilihMetodePembayaran / Attractions_Bayar / Attractions_Attractions_SuksesOrderBayar
```

### ⚠️ Substring false positives — every one ruled out with context. The brief's warning was warranted.
| Token | Hits | Verdict |
|---|---|---|
| **`dana`** | 2 | **FALSE POSITIVE** — ordinary Indonesian for "funds": `'Estimasi\x20pengembalian\x20dana'` (refund estimate), `'Tapi\x20tenang,\x20dana\x20anda\x20belum\x20terpotong.'` **Not DANA the wallet *in this bundle*** — the wallet is confirmed from the TRAC blog instead |
| **`doku`** | 3 | **FALSE POSITIVE** — all `Dokumen`: `'Nomor\x20Dokumen'`, `'Nama\x20di\x20Dokumen'`, `'Pilih\x20Jenis\x20Dokumen'`. **Not DOKU** |
| **`bca`** | **77** | **FALSE POSITIVE** — base64 and obfuscated identifiers only (`_0x12bca1`, `_0x17bca8`, UUID `'bca7ae51-6503-…'`). **No BCA branding** |
| **`bri`** | 18 | **FALSE POSITIVE** — base64 noise + **`'BRIO'` (Honda Brio, a car model)** |
| `bni` · `cimb` | 8 · 1 | **FALSE POSITIVE** — base64 noise |
| **`ovo`** | 6 | **FALSE POSITIVE** — base64 noise. (OVO confirmed from the blog, not the bundle) |
| **`mandiri`** | 5 | **NOT a payment rail — but a real separate finding:** the **Livin' Sukha** embedded channel. See The Hook |
| `authoriz` | 37 | Ordinary auth code. **No pre-auth hold** |
| midtrans, adyen, stripe, paypal, 2c2p, nicepay, faspay, espay, duitku, veritrans, tripay, finpay, ipaymu, kredivo, akulaku, indodana, atome, gopay, shopeepay, linkaja, permata, alfamart, indomaret, cicilan, installment, deposit, jaminan, preauth, va_number | **0** | **Genuinely absent from this bundle** |

## Section 5: B2B and subscription modules — both inside the consumer web app

**The most commercially interesting block in the research.** Corporate self-serve with enterprise controls:
```
CAR_LIST_B2B   RESERVASI_B2B   CITY_POOLS_LIST_B2B   PASSENGER_B2B   PROFILE_PRODUCTS_B2B
COST_CENTER_B2B                      ← cost-centre allocation
TRAC_ORDER_B2B_APPROVAL_HISTORY      ← multi-step approval workflow
USER_B2B_LOGIN_SECURE_V2   USER_B2B_CHECK_ELIGIBILITY_LOGIN   USER_B2B_OTP_VERIFICATION   SLA_B2B
TRAC_TD_PAYMENT_INVOICE / _LIST / _STATUS
```
Corroborated by product news: the latest TRACtoGo release added **"dual account functionality allowing users to activate personal and business accounts within one application."**

## Section 6: 🛑 No deposit, no pre-authorisation hold — a clean negative, established three ways

1. **Zero** occurrences of `deposit`, `jaminan`, `preauth`, `pre-auth` or `hold` as payment concepts in the 4.3MB bundle.
2. A verified Google Play review states verbatim: *"it so easy to use after you've completed all the documents they are asking for. just choose the city, date, time, and payment completion. **no deposit needed** and you will get confirmation straight away."*
3. **TRAC substitutes document-based risk control for a financial hold** — KTP + NPWP for Indonesians, passport for foreigners, SIM A licence verification, selfie/OCR: `ImagePassport`, `encryptedPassport`, `KYC_OTA_OCR_SUBMIT_WNA`, `OCR_EXTRACT`, `capture-driving-license-webcam-modal`, `kyc.verifSim.wrong`, `ExpiredSIM`.

Instead of deposits the bundle shows `downpayments` and `IsPaymentUpfront`/`setPaymentScheme` — **partial/upfront payment schemes, not auth holds.** A full refund flow exists (`ORDER_CHECK_CANCEL_REFUND`, `REFUND_INFORMATION`, `cancelRefund`).

**The pre-auth/deposit angle is DEAD for this account. Do not lead with it.**

## Section 7: The Singapore 15.06%

**What CAN be established — a purpose-built foreign-national onboarding and payment flow.** Strings from the bundle:
```
AUTH_REQUEST_KYC_WNA          (WNA = Warga Negara Asing = foreign national)
KYC_OTA_OCR_SUBMIT_WNA        IsForeign / IsForeigner
PassportNumber / NoPassport / ImagePassport / encryptedPassport
kyc.verifPassport.btnSend     kyc.verifSimInt.confirmSubtitle   (international driving permit)
```
Plus the FAQ verbatim: *"Anda hanya perlu mendaftar akun di aplikasi TRACtoGo secara online dan menyediakan dokumen paspor. **Pembayaran dapat dilakukan dengan cara transfer, menggunakan kartu k[redit]**"*

**Inbound foreign demand is a designed-for, instrumented segment — not an accident.** Singapore is the largest source of inbound business and leisure travel to Jakarta/Batam/Bali, so a genuine Singaporean customer segment is the leading explanation. `[INFERENCE, not confirmed]` that it specifically accounts for 15.06%.

**Second candidate — infrastructure artefact.** TRAC runs on **Azure**, and Azure's "Southeast Asia" region is physically **Singapore**. ⚠️ **I'd caution against this as the main explanation — SimilarWeb measures end-user geography, not server location.**

**Third candidate — OTA aggregator referral.** TRAC-Astra is listed as a supplier on `qeeq.com/suppliers/trac-astra` and `holidaycars.com`. `[UNVERIFIED]`

## Section 8: Financials — every figure dated

| Figure | Value | Date |
|---|---|---|
| **Astra group net revenue** | **Rp243.608 trillion** | 9M to 30 Sep 2025 (fetched) |
| Astra group net income (excl. FV adj.) | Rp24.674 trillion | 9M to 30 Sep 2025 |
| **SERA vehicles under contract** | **26,500 units** ("relatively stable") | **Q3 2025** |
| OLXmobbi used-car sales | 23,900 units, +24% | 9M 2025 |
| **TRAC total fleet** | **35,000 vehicles** | ⚠️ **undated** marketing page |
| SERA revenue | Rp5.3 trillion (+10.9%) | FY2022 `[UNVERIFIED]` |
| Car rental share of SERA revenue | **66%** | FY2019 `[UNVERIFIED]` |
| TRAC corporate customers | **3,000+** | 2020 `[UNVERIFIED]` |

⚠️ **SERA publishes its own annual reports** at `sera.astra.co.id/uploads/contents/` (2015–2020, 2022 PDFs located). **The FY2022 report is the best route to the corporate/retail revenue split and it was NOT opened — this is the top follow-up on the account.**

## Section 9: Buying signals

**Strong — active product velocity on the transacting app:**
1. **🔑 "Pick Up Now" launched 2026** — instant rental and airport transfer, no day-before reservation. Reported 16 Jul 2026 and 23 Sep 2026; confirmed live in code. **The sharpest timing hook.**
2. **TRACtoGo major release** — redesigned UI, **dual personal + business accounts in one app**, emergency button. 2025. `[UNVERIFIED]`
3. **AstraPay × TRAC commercial collaboration**, 16 May – 31 Dec 2025. `[UNVERIFIED — SERA page 404'd]`
4. **🔑 Bank Mandiri Livin' Sukha embedded channel** — code-only finding, no press release. **New channel = new payment context.**
5. **Attractions / tourism-ticket product line** in the checkout — diversification beyond vehicles into ticketed travel commerce, a different payment risk profile.
6. **Astranauts 2026** — Astra group digital-transformation competition. Group digital agenda is live. `[UNVERIFIED]`

**Weak / not established:**
- ⚠️ **EV fleet: only a 2021 item found.** **No 2025–2026 TRAC EV fleet investment.** Astra group EV activity sits with Astra Otoparts and Asuransi Astra — **do not attribute to TRAC.**
- **No payment-related job postings. No leadership changes at SERA or Astra Digital. No announced ride-hailing partnership.**

## Section 10: Complaints — materially fewer than expected, and that IS the finding

- **Google Play (`com.trac.tractogo`): 4.84 stars** (`"ratingValue":"4.838709831237793"`), **2,669 ratings**, **500K+ downloads.** Verified in raw HTML. **A 4.84 average across 2,669 ratings is unusually high for an Indonesian transactional app and is evidence AGAINST systemic payment failure.**
- **Positive payment signal**, verbatim: *"just choose the city, date, time, and payment completion. no deposit needed and you will get confirmation straight away."*
- **Non-payment complaint:** a user in **Medan** found all local stock marked limited, was bounced to WhatsApp and back, and could not complete a reservation. **An inventory/availability failure, not a payment failure** — but it is a conversion loss, and it shows WhatsApp is the fallback when the digital flow breaks. `[UNVERIFIED]`

**NOT FOUND, searched explicitly:** failed payments, double charges, VA payments not credited, refund delays, deposit-return disputes — across Play reviews, Kaskus, mediakonsumen.com and Twitter/X.

**🛑 Read carefully: absence of complaints is weak evidence of a healthy stack but STRONG evidence that a "your customers are complaining" angle will not land. Do not use one.**

## Section 11: ICP Score — 11 / 29 → 🟢 Medium

| Signal | Max | Score | Evidence |
|---|---|---|---|
| Transaction volume | 5 | **3** | **~20,600–55,000/month DERIVED for car retail alone**, straddling the gate, plus five un-quantified additional product lines. No SOURCED count exists |
| Orchestration posture | 4 | **4** | **Greenfield — one PSP (Xendit), hard-wired `beforeInteractive`, no router, no failover.** Verified first-hand |
| Operates 3+ countries | 3 | **0** | ⬜ **Deliberate zero.** Indonesia only. **No Singapore entity, searched specifically** |
| Multiple PSPs in parallel | 3 | **0** | ⬜ **Deliberate zero.** Exactly **one** PSP |
| Local rail gap in a top market | 3 | **0** | ⬜ **Deliberate zero, and it cost 3 points.** Coverage via Xendit is genuinely good — 6 wallets, 4 bank VAs, QRIS, 3–12mo instalments. BNPL and OTC cash are absent, **but Xendit already aggregates 38+ methods, so "add local rails" is pre-empted.** Scoring this row would contradict my own research |
| Recent market expansion | 2 | **2** | **Pick Up Now (2026)** · attractions line · Mandiri Livin' Sukha channel · dual B2B/B2C accounts |
| Known payment issues | 2 | **0** | ⬜ **Deliberate zero.** **None found, and the app sits at 4.84 stars** |
| Recent funding | 2 | **0** | ⬜ Astra subsidiary. No raise |
| Traffic outside home market | 2 | **2** | **Singapore 15.06%**, corroborated by a purpose-built foreign-national KYC and payment flow (`AUTH_REQUEST_KYC_WNA`, passport capture, international licence verification) |
| Competitor on orchestration | 2 | **0** | ⬜ Not found |
| Payment job postings | 1 | **0** | ⬜ None found |
| **TOTAL** | **29** | **11** | 🟢 **Medium** |

**Six deliberate zeros.** 11/29 is the lowest score in the batch that still clears the ≥10 threshold, and it is honest: a single-market, single-PSP account with good rail coverage and no complaint evidence. **The matrix undersells it slightly** — the recurring-renewal exposure on contracted fleet revenue and the two related-party routing constraints have no row, and they are the real conversation.

## Section 12: Do NOT Say

- ❌ **That TRAC is an invoiced B2B business with a brochure site.** My own brief said this and it is wrong.
- ❌ **Astra group revenue (Rp243.6tn) as TRAC's.**
- ❌ **Any transaction count as sourced.** The range is derived on assumed utilisation and duration.
- ❌ **Deposit or pre-authorisation holds.** None exist — established three ways.
- ❌ **Customer payment complaints.** None found; 4.84 stars.
- ❌ **Cross-border approval rates.** Domestic IDR.
- ❌ **"Add more local payment methods."** Xendit aggregates 38+. This would expose a lack of homework.
- ❌ **A Singapore entity or operation.** Not found.
- ❌ **DANA, DOKU, BCA, BRI, BNI, CIMB or OVO from bundle greps.** Every one was a false positive — `dana`="funds", `doku`="Dokumen", `bri`="BRIO" the Honda model, the rest base64 noise. (DANA and OVO *are* real rails, confirmed from TRAC's own blog instead.)
- ❌ **A shared Astra group payment layer.** There isn't one — Seva has no payment acceptance at all.
- ❌ **That AstraPay is a separate Astra-internal payment platform.** It is most likely a Xendit channel. **Ask.**
- ❌ **TRAC EV fleet investment in 2025–2026.** Only a 2021 item exists; group EV activity belongs to other Astra companies.
- ❌ **`astrafi.com` / "Astra" the US fintech.** A completely different company that surfaced in searches.

## Section 13: Research Confidence

**Overall: HIGH on the payment architecture. MEDIUM on scale. LOW on the revenue split.**

- ✅ **Verified first-hand by me:** `tractogo.trac.astra.co.id/car-rental` (HTTP 200, 29,820 bytes, `noindex, nofollow`), **three** `js.xendit.co/cards-session.min.js` references with `beforeInteractive`, and the genuine zero on `www.trac.astra.co.id/reservasi` (HTTP 200, 343,666 bytes, `payment`/`bayar`/`pembayaran`/`xendit` all 0).
- ✅ **Fetched by the research pass:** the 4,320,135-byte payment bundle with control counts, the 78-route `_buildManifest.js`, 16 path probes, the FAQ (408,300 B), the Play Store raw HTML, `seva.id`, and Astra's Q3 2025 press release.
- ✅ **Exemplary false-positive discipline** — 9 distinct substring traps caught and documented, including a 77-hit `bca` that was entirely base64 noise and a `bri` that was the Honda Brio.
- ⚠️ **Blocked / not done:** SERA's FY2022 annual report PDF (**the top follow-up**) · `ibid.astra.co.id` body (curl 52, empty reply) · the SERA AstraPay press release (404) · the T&C page was fetched but **not parsed** · the live `CONFIG_PAYMENT_METHOD` API was **not called** (no credentials, and correctly not attempted).
- ⚠️ **Unresolved:** the corporate/retail revenue split · any sourced transaction count or GMV · **whether AstraPay is reached via Xendit or a direct signed API** (highest-value call question) · the live rendered method list (`bank_name`/`logo` are null in the bundle, fetched at runtime) · whether a second PSP exists server-side · whether SimilarWeb covers `tractogo.*` · the Singapore 15% quantitatively · merchant of record in a legal document.

</details>
