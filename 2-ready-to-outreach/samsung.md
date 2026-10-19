# Samsung

**Status:** ⛔ **HOLD — Samsung appears to be an existing Yuno customer.** Research complete; do not start outreach until the account owner has been identified in CRM.
**ICP Score:** 19 / 29 → ⭐ High Priority **on arithmetic**. **ANALYST OVERRIDE: tier set to ⛔ Hold (existing customer, route internally).** The reasoning is in the ICP breakdown.
**Industry:** Consumer electronics: smartphones, TVs, appliances, sold D2C through samsung.com country stores and the Samsung Shop app · **HQ:** Suwon, South Korea (Samsung Electronics Co., Ltd.) · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **Expansion inside an existing customer, not a cold motion.** In APAC, no third-party orchestrator was found. Samsung picks a local PSP per subsidiary: Midtrans in Indonesia (confirmed on Samsung's own FAQ) and KG Inicis in Korea (named in the samsung.com/sec privacy policy). The India PSP is not identified. The APAC stack would be greenfield, but Yuno already holds a Samsung logo, so the play is a cross-sell from whichever Samsung entity is live today.

---

> ## ⛔ READ FIRST: Samsung is on Yuno's own customer logo wall
>
> On 2026-10-19 I fetched [y.uno/en/success-stories](https://y.uno/en/success-stories). Its page data contains `"trustedBy":{"label":"Trusted by leading retail and ecommerce brands","logos":["Samsung","McDonald's","Tesla","Reserva","Rappi","Whop"]}`. The site-wide list reads *"TRUSTED BY GLOBAL TEAMS: McDonald's, Samsung, Uber, Carrefour, Ant Group, NetEase…"*. The same site-wide list was recorded on 2026-09-15 in `3-outreached/air-new-zealand.md`.
>
> **This trips the Phase 0 gate "existing Yuno customer: stop and flag".** I didn't catch it until the research was already running, so the full report is below. It is useful for an expansion conversation, but it is **not** a cold prospect.
>
> **What is not known:** which Samsung entity, which market, or which product uses Yuno. No case study, press release or metric exists. Given Yuno's footprint it is *probably* a LATAM subsidiary `[INFERENCE, not confirmed]`. Brazil (9.53%) is samsung.com's #2 traffic market. A Samsung Electronics **Mexico** "Payments Gateway Specialist" job ad describes local PSP and acquirer management `[UNVERIFIED — search summary only]` ([overseasjobs](https://www.overseasjobs.com/job/details/37250222/payments-gateway-specialist)).
>
> **Next step:** find the Samsung account owner in CRM and ask which entity is live and whether an APAC expansion intro is welcome. Outreach to Samsung India, Korea, Indonesia or Thailand should be a warm internal referral ("your colleagues in X already run on Yuno"), only once the owner signs off.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Samsung Electronics makes and sells smartphones (Galaxy), TVs, appliances and semiconductors. Group revenue was KRW 333.6T in FY2025 `[UNVERIFIED — search summary only]` ([Khan](https://www.khan.co.kr/en/article/202601290845007)). Samsung runs D2C online stores on samsung.com country paths and in the Samsung Shop app across most APAC markets. Each store is run by the local subsidiary, and some use a partner retailer as the legal seller. The payment-relevant business is the D2C store, not the chip business.

**SimilarWeb total visits (last full month):** ≈810.8M/month average, samsung.com, Jul–Sep 2026 (2.432B over 3 months). Source: SimilarWeb (supplied 2026-10-19). **Caveats from the supplied file:**
1. The Sales Intelligence view gives top-10 shares only, with no per-country visits.
2. It excludes app traffic.
3. 94.92% of visits are mobile web, which includes support and product-info traffic from device owners. **Web visits are not a proxy for D2C orders.**
4. The country split is used only as a market-mix signal and never to size payments.

### Top 5 markets
Ranked by the supplied samsung.com share. India is #1 overall and Korea is #5. Indonesia (#8, 2.12%) and Thailand (#9, 2.11%) complete the APAC picture and appear in the table below.

| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇮🇳 **India** | 29.06% | Debit/credit cards, EMI (credit card), net banking, "Wallet Payment", Cash on Delivery, Samsung Finance+ cardless loans (DMI, TVS Credit, Cholamandalam) | **UPI not named** on Samsung's payment FAQ (absence from checkout not proven). RuPay, UPI Autopay, BNPL not named | ✅ Samsung India Electronics Pvt. Ltd. (CIN U31900DL1995PTC071387). The ToS frames the store as an intermediary; seller of record unconfirmed |
| 2 | 🇧🇷 Brazil *(out of territory)* | 9.53% | Not assessed | Not assessed | Not researched. Possible Yuno-live market `[INFERENCE]` |
| 3 | 🇺🇸 United States *(out of territory)* | 9.45% | Not assessed | Not assessed | Not researched |
| 4 | 🇮🇹 Italy *(out of territory)* | 8.11% | Not assessed | Not assessed | Not researched |
| 5 | 🇰🇷 **Korea** (HQ) | 6.90% | Credit cards with interest-free instalments (up to 12 months; partial up to 24), Naver Pay, "나눠서 결제" split payment | KakaoPay, Toss, PAYCO not found on the fetched page (the FAQ is JS-rendered, so this is not proof of absence) | ✅ Samsung Electronics Co., Ltd. (HQ) |

### APAC markets (where the pitch actually is)
| Market | Traffic | Methods confirmed on Samsung's own pages | PSP | Seller / entity |
|---|---|---|---|---|
| 🇮🇳 India | 29.06% | Cards, EMI, net banking, wallets, COD, Finance+ | **Not identified** (storefront is SAP Hybris) | Samsung India Electronics Pvt. Ltd. operates the store; seller unconfirmed |
| 🇰🇷 Korea | 6.90% | Cards + interest-free instalments, Naver Pay | **KG Inicis** `[Terms/Privacy Policy]` | Samsung Electronics Co., Ltd.; 삼성전자판매 / 리빙프라자 handle order processing |
| 🇮🇩 Indonesia | 2.12% | Cards, 0% instalments up to 36 months, bank transfer, e-wallet, SPayLater, Kredivo, Indodana, Home Credit | **Midtrans** `[Checkout / FAQ]` | **Seller: PT. Global Distribusi Pusaka** (partner retailer). Payment "collected by Samsung Electronics Indonesia" |
| 🇹🇭 Thailand | 2.11% | **Thai-issued cards only**, 0% instalments, Krungsri First Choice, QR Payment, PromptPay, mobile banking, Rabbit LINE Pay, Google Pay, ShopeePay, TrueMoney | Not identified | Thai Samsung Electronics Co., Ltd. `[UNVERIFIED]`; seller unconfirmed |
| 🇸🇬 Singapore | Not in top 10 | Visa/MC/Amex, bank instalments, CIMB PayLater, Atome, GrabPay, Grab PayLater, ShopeePay, Shopee PayLater, PayNow | Not identified | Samsung Electronics Singapore Pte Ltd `[UNVERIFIED]` |
| 🇯🇵 Japan | Not in top 10 | Not researched | Not identified | Samsung Electronics Japan Co., Ltd. Samsung Shop app launched 2026-07-07 |

### Legal entities
- **Samsung Electronics Co., Ltd.** (Korea): global HQ and the Korean store operator.
- **Samsung India Electronics Pvt. Ltd.** (India): CIN **U31900DL1995PTC071387**, registered office 6th Floor, DLF Centre, Sansad Marg, New Delhi. Fetched from the samsung.com/in footer.
- **Samsung Electronics Indonesia** (Indonesia): store operator and payment collector. **PT. Global Distribusi Pusaka** is the seller (shop T&Cs, fetched).
- **Samsung Electronics Australia Pty Ltd** (Australia): ABN 63 002 915 648 (footer, fetched).
- **Samsung Electronics Japan Co., Ltd.** (Japan): runs the Samsung Shop app (newsroom, fetched).
- Thai Samsung Electronics Co., Ltd.; Samsung Electronics Singapore Pte Ltd; Samsung Electronics Philippines Corporation; Samsung Vina (SAVINA, Vietnam); Samsung SDS Malaysia Sdn Bhd as possible Malaysia store operator. All `[UNVERIFIED — search summary only]`.

### Known PSPs
- **Midtrans** (GoTo): `[Checkout / FAQ]`, **Indonesia**. *"Kami menerima berbagai metode pembayaran melalui Midtrans (Gateway Pembayaran Online)"* ([samsung.com/id FAQ](https://www.samsung.com/id/shop-faq/payment-and-financing/what-payment-methods-are-available-on-samsung-online-store/), fetched).
- **KG Inicis**: `[Terms/Privacy Policy]`, **Korea**. "㈜이니시스: 상품 구매에 필요한 신용카드, 현금결제 등의 결제정보 전송" (Inicis transmits card and cash payment data for product purchases) ([samsung.com/sec privacy policy](https://www.samsung.com/sec/info/privacy/01/rc/), fetched). ⚠️ The clause sits in a third-party-provision block carrying a 2013-09-01 effective-date label. It is on the current policy page, but it may be legacy text.
- **India: not identified.** The homepage source shows SAP Hybris (`hybrisApiJson`) and no PSP signatures. Searches tying Samsung India's store to Razorpay, PayU, Juspay, BillDesk or CCAvenue returned nothing. Pine Labs and Paytm deals with Samsung were **offline in-store EMI**, not the samsung.com/in gateway.

### Orchestration status
**None detected in APAC: local PSP integrations per subsidiary.** No Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX or Payrails link was found. There is a twist: **Yuno itself appears to be live somewhere in Samsung** (see READ FIRST). Samsung also runs its own in-house billing for Galaxy Store and TV apps (Samsung Checkout), but that is a separate product from the D2C stores.

### Buying signals
- 🚀 **Samsung Shop app launched in Japan on 2026-07-07**, with a first-purchase campaign ([Samsung Newsroom JP](https://news.samsung.com/jp/launches-official-samsung-shop-app-in-japan), fetched). This is a new D2C channel, not a new market.
- 🤝 **Samsung India is building its own payment rails.** It is the "first OEM" to put UPI onboarding into device setup. Its Samsung Wallet "will soon support" online use of tokenised cards "across a wide set of key merchants" (2025-10-30, [Samsung Newsroom India](https://news.samsung.com/in/samsung-india-introduces-breakthrough-features-to-samsung-wallet-redefining-digital-payments-and-upi-onboarding), fetched). Payments are a strategic topic inside Samsung India.
- 💼 Payment hiring was seen only outside territory (Mexico Payments Gateway Specialist `[UNVERIFIED]`). No APAC payments postings were found.
- 🤝 **Competitive:** OnePlus, a direct India competitor, runs on Juspay payment orchestration with PSP routing ([Juspay customer story](https://juspay.io/customer-stories/oneplus), fetched).

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated, and **do not generate it** until the Samsung account owner has cleared an APAC approach. Samsung appears to be an existing Yuno customer (see the HOLD note above). Once cleared, run `/full-outreach Samsung` with the warm-referral framing.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 19 / 29 (arithmetic) → override to ⛔ Hold
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | +5 | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. [ASSUMPTION — not researched.]** Basis: no D2C order count or online GMV is published for any APAC Samsung store. Samsung India's FY25 revenue was ₹1,11,183 cr ([Business Standard](https://www.business-standard.com/companies/news/samsung-fy25-revenue-from-operations-rises-over-11-to-1-11-trillion-125111900332_1.html) `[UNVERIFIED — search summary only]`), but the online share is unknown. In 2020 the company targeted 10% of India business through its online store ([Daily Excelsior](https://www.dailyexcelsior.com/?p=1005690), `[UNVERIFIED]`, dated). Even 1% of FY25 India revenue through samsung.com/in at a ₹30,000 average ticket would be ~31,000 orders/month. At the 2020 target of 10% it would be ~310,000/month. Korea's Samsung Store reportedly out-sold Lotte Himart domestically in 2023 ([KED Global](https://www.kedglobal.com/newsView/ked202304180016), `[UNVERIFIED]`). The online-share inputs are not sourced, so this stays an assumption, and the 40k gate cannot fire on it. **Billing unit:** D2C device and accessory orders on samsung.com stores. Galaxy Store / IAP billing is excluded. |
| Orchestration status | +4 | ✅ None detected in APAC. Midtrans (ID) and Inicis (KR) are direct integrations; India is unknown. ⚠️ Yuno appears to be live elsewhere in Samsung. That isn't a competing orchestrator, but it makes "greenfield" misleading for the group |
| 3+ countries | +3 | ✅ All 10 supplied countries are above 1% share. Entities confirmed in KR, IN, ID, AU and JP |
| Multiple PSPs | +3 | ✅ Midtrans (Indonesia, own FAQ) + KG Inicis (Korea, own privacy policy). Caveat: the Inicis clause carries a 2013 label |
| Local rail or licensing gap in a top-3 market | 0 | ⬜ **India:** UPI is not named on Samsung's payment FAQ, but the FAQ also says "Wallet Payment" generically, and absence from a FAQ doesn't prove absence from checkout. **Korea:** KakaoPay and Toss were not seen, but the FAQ is JS-rendered. **No sourced absence → 0.** A live checkout on samsung.com/in would settle it |
| Recent expansion | 0 | ❌ The Japan Samsung Shop app (2026-07-07) is a new channel in an existing market, not a new market |
| Payment issues reported | 0 | ⬜ The "money deducted, no order created" and slow-refund pattern recurs on Samsung's own India community forum (2020–2024), and there are isolated Voxya complaints in 2026. All of it comes from search summaries; the forum blocked fetching (403). Not scored |
| Funding >$10M | 0 | ❌ Public company; no funding rounds |
| High traffic outside home | +2 | ✅ Korea is 6.90% of samsung.com traffic; India alone is 29.06% |
| Competitor using orchestration | +2 | ✅ OnePlus on Juspay payment orchestration ([Juspay](https://juspay.io/customer-stories/oneplus), fetched). Xiaomi on Juspay via Hyperswitch case study `[UNVERIFIED — page returned 403]` |
| Payment job postings | 0 | ⬜ Only a Mexico role (out of territory, search summary) |

**Tier on arithmetic:** 19 → ⭐ High Priority. No public payment RFP found.

**ANALYST OVERRIDE → ⛔ Hold (existing customer).** Three reasons:
1. **Phase 0 gate.** Samsung is on y.uno's "Trusted by leading retail and ecommerce brands" logos and the site-wide customer list (fetched 2026-10-19). Cold outreach to a logo customer risks the existing relationship and contradicts Yuno's own marketing. The account belongs to whoever owns that relationship.
2. **The score leans on one assumption.** +5 of the 19 points come from an assumed transaction count. Without it the score is 14, which is 🟢 Medium.
3. **Decentralised buying.** PSP choice is made per subsidiary (Midtrans in ID, Inicis in KR, the Mexico job ad). In Indonesia the legal seller is a third-party retailer, and India's ToS frames the store as an intermediary. Any APAC deal is a country-by-country sale with a different contracting party each time. That fits a warm referral from an existing Samsung entity much better than a cold top-down pitch.

**If the account owner clears it**, this becomes a strong expansion lead. The best entry points are India (29% of traffic, PSP unknown, OnePlus already orchestrated) and Thailand (domestic cards only).

### Source Notes
- ✅ Samsung on Yuno logo walls: y.uno/en/success-stories, fetched and grepped by me on 2026-10-19.
- ✅ India CIN and registered office: samsung.com/in footer, fetched.
- ✅ India payment methods (cards, EMI, net banking, wallet, COD): samsung.com/in shop-faq, fetched and grepped.
- ✅ Indonesia Midtrans; seller PT. Global Distribusi Pusaka; payments collected by Samsung Electronics Indonesia: samsung.com/id FAQ and T&Cs, fetched and grepped by me.
- ✅ Korea Inicis: samsung.com/sec privacy policy, fetched and grepped by me. ⚠️ The block carries a 2013 effective-date label.
- ✅ Thailand "Credit / Debit Card issued in Thailand only", PromptPay and QR Payment: samsung.com/th FAQ, fetched and grepped by me.
- ✅ Singapore methods (incl. PayNow, GrabPay, Atome): samsung.com/sg FAQ, fetched by me.
- ✅ Korea interest-free instalments and Naver Pay: samsung.com/sec card-benefit page, fetched by Agent 3.
- ✅ Japan Samsung Shop app 2026-07-07; Samsung India Wallet UPI onboarding and tokenised-card plans 2025-10-30; OnePlus on Juspay orchestration: all fetched by me.
- ✅ Australia ABN 63 002 915 648: footer, fetched.
- ⚠️ Samsung FY2025, Q2 2026 and Q3 2026 guidance figures; Samsung India FY25/FY26 results: search summaries only.
- ⚠️ India complaint threads (Samsung Community, Voxya): search summaries only; the forum returned 403.
- ⚠️ Mexico Payments Gateway Specialist job, UK PCI statement, Malaysia SDS operator, Thai/SG/PH/VN entities: search summaries only.
- ⚠️ `accounts/apac-tal.csv` row for Samsung: PSP and orchestrator columns blank. Nothing to verify.

### Success Case Alternatives
- **Samsung itself (internal reference).** The strongest possible proof point is a live Samsung entity on Yuno. Get the details, and permission to reference them, from the account owner. **Never cite it externally without that.**
- **McDonald's / Rappi / Carrefour** (same y.uno retail and global customer lists). These are retail logo references only; no metric is published. Weak profile match: none is a consumer-electronics D2C brand.

---

## Executive Summary

Samsung Electronics sells devices D2C through samsung.com country stores and the Samsung Shop app. India is samsung.com's #1 traffic market (29.06%) and Korea is #5. In APAC the payment stack is **decentralised per subsidiary with no orchestrator found**: Midtrans in Indonesia, KG Inicis in Korea, an unidentified gateway behind India's SAP Hybris storefront, and a Thailand store that only takes Thai-issued cards. The decisive finding is that **Samsung appears on Yuno's own customer logo wall**, which trips the existing-customer gate. The motion is an internal-referral expansion into APAC subsidiaries, not cold outreach, and only once the account owner clears it.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** Path 1, pasted SimilarWeb data: `accounts/traffic/samsung.md`, SimilarWeb Sales Intelligence (supplied 2026-10-19), samsung.com only, Jul–Sep 2026, desktop + mobile web.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | 🇮🇳 India **(high priority, APAC)** | 29.06% | ~235.6M `[DERIVED from supplied share, not a SimilarWeb figure]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | Brazil *(out of territory)* | 9.53% | ~77.3M `[DERIVED]` | Not supplied | same |
| 3 | United States *(out of territory)* | 9.45% | ~76.6M `[DERIVED]` | Not supplied | same |
| 4 | Italy *(out of territory)* | 8.11% | ~65.8M `[DERIVED]` | Not supplied | same |
| 5 | 🇰🇷 Korea **(high priority, APAC, HQ)** | 6.90% | ~55.9M `[DERIVED]` | Not supplied | same |
| 6 | Germany *(out of territory)* | 4.01% | ~32.5M `[DERIVED]` | Not supplied | same |
| 7 | France *(out of territory)* | 3.27% | ~26.5M `[DERIVED]` | Not supplied | same |
| 8 | 🇮🇩 Indonesia (APAC) | 2.12% | ~17.2M `[DERIVED]` | Not supplied | same |
| 9 | 🇹🇭 Thailand (APAC) | 2.11% | ~17.1M `[DERIVED]` | Not supplied | same |
| 10 | Russia *(out of territory)* | 1.76% | ~14.3M `[DERIVED]` | Not supplied | same |

Derived visits = share × 810.8M average monthly visits. The top 10 cover 76.32%; the remaining 23.68% is unlisted.

**Caveats (from the supplied file, applied throughout):**
- Shares only; per-country visits are derived as above.
- A single global domain with country paths, so there are no regional domains to merge.
- App traffic is excluded. Galaxy Store, Samsung Wallet and Samsung Members activity happens on the device.
- 94.92% mobile web, much of it support and product-info traffic from existing owners. Not a proxy for D2C orders.

No top-10 APAC market lacks an entity (see Section 2). The entity question in APAC is about *who the seller is*, not whether Samsung is present.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Suwon, South Korea (Samsung Electronics Co., Ltd.).

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| India | Samsung India Electronics Pvt. Ltd. (store operator) | CIN U31900DL1995PTC071387 | [samsung.com/in](https://www.samsung.com/in/) footer, fetched |
| Indonesia | Samsung Electronics Indonesia (operator, payment collector); **PT. Global Distribusi Pusaka (seller)** | Not found | [samsung.com/id T&Cs](https://www.samsung.com/id/shop-faq/service-and-warranty/what-is-samsung-online-stores-terms-and-conditions/), fetched |
| Korea | Samsung Electronics Co., Ltd.; 삼성전자판매(주) / 리빙프라자(주) (order processing) | Not found | [samsung.com/sec privacy](https://www.samsung.com/sec/info/privacy/01/rc/), fetched |
| Australia | Samsung Electronics Australia Pty Ltd | ABN 63 002 915 648 | [samsung.com/au](https://www.samsung.com/au/) footer, fetched |
| Japan | サムスン電子ジャパン株式会社 (Samsung Electronics Japan Co., Ltd.) | Not found | [Samsung Newsroom JP](https://news.samsung.com/jp/launches-official-samsung-shop-app-in-japan), fetched |
| Thailand | Thai Samsung Electronics Co., Ltd. | Not found | [news.samsung.com/th](https://news.samsung.com/th/president-mr-sunghwan-kim) `[UNVERIFIED — search summary only]` |
| Singapore | Samsung Electronics Singapore Pte Ltd | Not found | [samsung.com/sg offers](https://www.samsung.com/sg/business/offers/) `[UNVERIFIED]` |
| Malaysia | Samsung SDS Malaysia Sdn Bhd (reported store operator/seller) | Not found | [samsung.com/my T&Cs](https://www.samsung.com/my/shop-faq/service-and-warranty/what-are-the-terms-and-conditions/) `[UNVERIFIED]` |
| Philippines | Samsung Electronics Philippines Corporation | Not found | [samsung.com/ph T&Cs](https://www.samsung.com/ph/info/online-shop-tnc) `[UNVERIFIED]` |
| Vietnam | Samsung Vina Electronics (SAVINA) | Not found | [pricing policy PDF](https://images.samsung.com/is/content/samsung/assets/vn/shop-faq/samsung-account/chinh-sach-ve-gia.pdf) `[UNVERIFIED]` |

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| India | ✅ #1 | ✅ | Not researched (moot: entity present) | Low |
| Korea | ✅ #5 | ✅ HQ | Not researched (moot) | Low |
| Indonesia | ✅ #8 | ✅ (seller is a third-party retailer) | Not researched (moot) | Low |
| Thailand | ✅ #9 | ✅ `[UNVERIFIED]` | Not researched (moot) | Low for domestic. **Foreign-issued cards are refused outright** ("Credit / Debit Card issued in Thailand only", [samsung.com/th FAQ](https://www.samsung.com/th/shop-faq/payment-and-financing/accepted-payment-methods/), fetched) |

No cross-border warning applies: Samsung is local everywhere it sells. **The structural finding is the seller model.** In Indonesia the legal seller is a partner retailer while Samsung collects payment. India's eStore ToS reportedly frames samsung.com/in as an intermediary under the IT Rules (`[UNVERIFIED — search summary only]`, [shop-terms-of-use](https://www.samsung.com/in/shop-terms-of-use/)). Who signs the PSP contract may therefore differ from the brand entity.

> **MANUAL:** Read the India shop T&Cs in full to confirm the seller of record and the payment-collection clause.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Indonesia | **Midtrans** | `[Checkout]` (shop FAQ) | https://www.samsung.com/id/shop-faq/payment-and-financing/what-payment-methods-are-available-on-samsung-online-store/ |
| Korea | **KG Inicis** (㈜이니시스) | `[Terms/Privacy Policy]` | https://www.samsung.com/sec/info/privacy/01/rc/ |
| Korea | KG Inicis / KG Financial as sub-processors for Samsung Welstory promotions (not checkout) | `[Terms/Privacy Policy]` | same |
| India | Not identified. Storefront is SAP Hybris | `[Source Code]` (homepage) | https://www.samsung.com/in/ |
| India | Samsung Finance+ lenders: DMI Finance, TVS Credit, Cholamandalam Finance (lenders, not PSPs) | `[Checkout]` (microsite) | https://www.samsung.com/in/microsite/finance-plus/ |
| Thailand | Not identified. Krungsri First Choice instalments shown (a lender, not confirmed as PSP) | `[Checkout]` (FAQ) | https://www.samsung.com/th/shop-faq/payment-and-financing/accepted-payment-methods/ |
| Global (EU/UK/AU likely) | BuiltWith detects Afterpay, Klarna, PayPal and card brands only, with no acquirer | `[Tech Profiler]` | https://builtwith.com/samsung.com |

**Not to be confused with Samsung's own store stack:**
- Pine Labs (2020 EMI festival) and Paytm (2022) partnered with Samsung's **offline stores**.
- Pine Labs, Ezetap and Mswipe terminals accept **Samsung Pay**, the wallet.

None of these processes samsung.com/in.

#### 3B. Payment Orchestrator

**Classification: None detected (APAC).** No public evidence was found of a third-party orchestration platform on any APAC Samsung store. Each subsidiary appears to integrate a local PSP directly (Midtrans in ID, Inicis in KR). That limits routing optimisation, failover and multi-acquirer strategies across the region. A Samsung Mexico job ad for a Payments Gateway Specialist who negotiates with banks and PSPs points the same way: PSPs are managed per subsidiary (`[UNVERIFIED — search summary only]`, [overseasjobs](https://www.overseasjobs.com/job/details/37250222/payments-gateway-specialist)).

**Group-level caveat:** Yuno appears on Samsung's logo list ([y.uno/en/success-stories](https://y.uno/en/success-stories), fetched), so some Samsung entity likely already runs on Yuno. Samsung also operates in-house billing for Galaxy Store / TV apps ("Samsung Checkout"), separate from the D2C stores (`[UNVERIFIED — search summary only]`).

> **MANUAL:** Run a test checkout on samsung.com/in with DevTools open and note the gateway domain and merchant name on the payment page. This is the single most important open question.

---

### Section 4: Alternative & Local Payment Methods

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| India | Debit/credit cards | Cards | Mentioned in docs | [IN FAQ](https://www.samsung.com/in/shop-faq/payment-and-financing/how-do-i-pay-for-my-order/) |
| India | Net banking | Bank transfer / A2A | Mentioned in docs | same |
| India | "Wallet Payment" (wallets not named) | Digital wallet | Mentioned in docs | same |
| India | Credit-card EMI | BNPL/Instalments | Mentioned in docs | [IN finance FAQ](https://www.samsung.com/in/shop-faq/payment-and-financing/what-are-various-finance-programs-available-on-samsung-com/) |
| India | Samsung Finance+ (DMI, TVS Credit, Cholamandalam) | BNPL/Instalments | Mentioned in docs | [Finance+](https://www.samsung.com/in/microsite/finance-plus/) |
| India | Cash on Delivery (major cities) | Cash/voucher | Mentioned in docs | [IN FAQ](https://www.samsung.com/in/shop-faq/payment-and-financing/how-do-i-pay-for-my-order/) |
| India | UPI | Bank transfer / A2A | Not found on Samsung's payment FAQ; unknown at checkout | — |
| India | RuPay, UPI Autopay, named BNPL | Various | Not found | — |
| Korea | Credit cards, interest-free instalments (up to 12 months; partial up to 24) | Cards / Instalments | Mentioned in docs | [SEC card benefits](https://www.samsung.com/sec/eventList/creditcard_benefit) |
| Korea | Naver Pay | Digital wallet | Mentioned in docs | same |
| Korea | "나눠서 결제" split payment | Instalments | Mentioned in docs (privacy policy) | [SEC privacy](https://www.samsung.com/sec/info/privacy/01/rc/) |
| Korea | KakaoPay, Toss, PAYCO | Digital wallet | Unknown (FAQ JS-rendered) | — |
| Indonesia | Credit cards, 0% instalments up to 36 months | Cards / Instalments | Mentioned in docs | [ID bank promo](https://www.samsung.com/id/offer/bank-promo-and-installment/) |
| Indonesia | Bank transfer, "e-wallet" (unnamed) | A2A / Wallet | Mentioned in docs | same |
| Indonesia | SPayLater, Kredivo, Indodana, Home Credit | BNPL | Mentioned in docs | [ID FAQ](https://www.samsung.com/id/shop-faq/payment-and-financing/what-payment-methods-are-available-on-samsung-online-store/) |
| Indonesia | QRIS, virtual account, GoPay, OVO, DANA by name | A2A / Wallet | Not found by name (likely via Midtrans `[INFERENCE, not confirmed]`) | — |
| Thailand | Thai-issued credit/debit cards only | Cards | Mentioned in docs | [TH FAQ](https://www.samsung.com/th/shop-faq/payment-and-financing/accepted-payment-methods/) |
| Thailand | 0% instalments (3–10 months); Krungsri First Choice 24–60 months | Instalments | Mentioned in docs | same |
| Thailand | QR Payment, PromptPay, Mobile Banking | A2A | Mentioned in docs | same |
| Thailand | Rabbit LINE Pay, Google Pay, ShopeePay, TrueMoney | Digital wallet | Mentioned in docs | same |
| Singapore | Cards, PayNow, GrabPay, ShopeePay, Atome, Grab/Shopee PayLater, CIMB PayLater | Mixed | Mentioned in docs | [SG FAQ](https://www.samsung.com/sg/shop-faq/payment-and-financing/what-online-payment-methods-do-you-accept/) |

**Assessment:** The confirmed method sets are broad and locally tailored. Indonesia, Thailand and Singapore have strong instalment and wallet coverage. **There is no sourced "missing dominant rail" warning for any top market.** India's UPI is the only plausible gap, and it is probably present at checkout but simply unnamed in the FAQ. Do not lead with "you don't take UPI": it is likely wrong, and Samsung India runs its own UPI onboarding in Samsung Wallet.

> **MANUAL:** Check the samsung.com/in checkout payment page for UPI (collect / intent / QR) and RuPay, and the samsung.com/id checkout for QRIS and VA.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Checkout errors: money debited, no order created, no order ID | Samsung Community (India Online Store board) | Moderate, recurring | 2020–Jan 2024 | [thread 1](https://r2.community.samsung.com/t5/Samsung-Online-Store/Payment-have-been-deducted-but-order-has-not-processed/td-p/15366109), [thread 2](https://r2.community.samsung.com/t5/Samsung-Online-Store/Money-deducted-yet-no-confirmation-nor-cancellation/td-p/4875454) `[UNVERIFIED — search summary only; forum returned 403]` |
| Slow refunds (17 to 35+ days) | Samsung Community (India) | Moderate | 2020–2025 | [thread](https://r2.community.samsung.com/t5/Samsung-Online-Store/Refund-not-received-after-35-days/m-p/12276999/highlight/true) `[UNVERIFIED]` |
| EMI charge higher than expected | Voxya | Isolated | May 2026 | [Voxya](https://voxya.com/consumer-complaints/merchant-charged-extra-amount/266976) `[UNVERIFIED]` |
| Cancellation charge deducted from refund | Voxya | Isolated | Mar 2026 | [Voxya](https://voxya.com/consumer-complaints/product-not-delivered-got-damaged-at-delivery-office-cancellation-amount-charged/260840) `[UNVERIFIED]` |
| Samsung Wallet UPI payment debited but not posted / slow refund | Voxya, Samsung Community | Isolated | 2025–Feb 2026 | [Voxya](https://voxya.com/consumer-complaints/loan-emi-payment-not-updated/260001) `[UNVERIFIED]` |

"Debited, no order" is a recurring India pattern on Samsung's own forum. That suggests weak gateway-to-order reconciliation and single-gateway exposure, which an orchestration layer with webhook reconciliation and failover addresses `[INFERENCE, not confirmed]`. The dated threads are mostly before 2025, and none were fetched, so **this is not scored and should not be quoted in outreach**. No Reddit, Trustpilot or app-store hits were found.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 2026-10-08 | Q3 2026 earnings guidance: sales ~KRW 195T, operating profit ~KRW 107.4T | Tech / financial | [Samsung Newsroom](https://news.samsung.com/global/samsung-electronics-announces-earnings-guidance-for-third-quarter-2026) `[UNVERIFIED — search summary only]` |
| 2 | 2026-07-07 | Samsung Shop app launched in Japan | Market Expansion (channel) | [Samsung Newsroom JP](https://news.samsung.com/jp/launches-official-samsung-shop-app-in-japan), fetched |
| 3 | 2026-07-30 | Q2 2026: MX/Networks revenue KRW 33.2T, operating loss KRW 0.7T on component costs | Tech / financial | [Korea Times](https://www.koreatimes.co.kr/business/companies/20260730/samsung-electronics-posts-q2-profit-of-62-bil-up-nearly-20-fold) `[UNVERIFIED]` |
| 4 | 2025-10-30 | Samsung India Wallet: UPI onboarding in device setup; tokenised-card online checkout "soon" across key merchants | Tech / payments | [Samsung Newsroom IN](https://news.samsung.com/in/samsung-india-introduces-breakthrough-features-to-samsung-wallet-redefining-digital-payments-and-upi-onboarding), fetched |
| 5 | 2025-02 | Galaxy S25 sold through BigBasket quick-commerce in India (after the Blinkit S24 tie-up in 2024) | Market Expansion (channel) | [FoneArena](https://www.fonearena.com/blog/414939/samsung-galaxy-s24-10-minute-delivery-blinkit.html/amp) `[UNVERIFIED]` |

No public payment-related RFP found. No APAC payment-infrastructure job postings found; the only payments role surfaced is in Mexico. No payment licence applications found.

A mobile division running at an operating loss on component costs (Q2 2026, unverified) is a plausible cost-of-acceptance lever `[INFERENCE]`.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 2025-10-30 | Samsung India: "first OEM" to put UPI onboarding into device setup; FOREX cards (WSFx) and AU Bank on Tap & Pay; online tokenised-card checkout coming | Samsung India treats payments as a product line, so expect a sophisticated buyer | [Samsung Newsroom IN](https://news.samsung.com/in/samsung-india-introduces-breakthrough-features-to-samsung-wallet-redefining-digital-payments-and-upi-onboarding), fetched |
| 2 | 2026-08 | 30-month no-cost EMI for new Galaxy foldables in India via DMI, TVS Credit, IDFC FIRST, Poonawalla (lender list differs from the Finance+ microsite) | Instalment-heavy checkout | [IANS](https://ianslive.in/samsung-introduces-30-month-no-cost-emi-plans-for-new-galaxy-foldables-in-india--20260803175805) `[UNVERIFIED]` |
| 3 | 2022-08 | Paytm × Samsung stores: postpaid and EMI (offline) | Background only; not the online stack | [Business Today](https://businesstoday.in/latest/corporate/story/paytm-partners-with-samsung-stores-offers-no-cost-emi-options-344750-2022-08-16) `[UNVERIFIED]` |

No provider removals found.

---

### Section 8: Checkout Experience Audit

Full checkout flow not accessible: the samsung.com/in checkout renders client-side and no test order was placed. Findings are limited to publicly observable elements.

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | SAP Hybris storefront (India); gateway page not observed | N/A | `hybrisApiJson` in page source |
| Guest checkout | Korea policy has a separate "비회원 구매" (non-member purchase) consent → guest checkout exists in KR | Good (KR) | India not observed |
| Steps to complete payment | Not observed | N/A | |
| Card input experience | Not observed | N/A | |
| Payment methods visible | Broad per-market sets (Section 4) | Good | |
| Location-based method display | Separate country stores with local methods | Good | |
| Instalment / EMI options | Present in IN, KR, ID, TH, SG; EMI calculator popup on IN | Good | |
| 3DS implementation | Not detected | N/A | |
| PCI indicator | Not observed | N/A | |
| Mobile responsiveness | 94.92% of traffic is mobile web; Samsung Shop app exists | Not assessed | |
| Multi-currency / local pricing | Local currency per country store; **Thailand refuses foreign-issued cards** | Fair (TH) | |
| Saved payment methods | Account menu with orders/addresses; saved cards not observed | N/A | |
| Error message clarity | Complaints describe no order ID after failed payment (unverified) | N/A | |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found for APAC. The UK shop FAQ self-states PCI DSS compliance | [UK FAQ](https://www.samsung.com/uk/shop-faq/payment-and-financing/is-shopping-on-samsung-com-or-samsung-shop-app-secure/) `[UNVERIFIED — search summary only]` |
| Card data handling | Not found | — |
| Recommended Yuno integration | Not assessable until the existing Samsung–Yuno integration pattern is known. Mirror whatever the live entity uses | Internal |

No direct PCI compliance documentation found publicly for Samsung's APAC stores.

---

### Section 10: Strategic Insights & Outreach Angles

> All angles assume the account owner clears an APAC approach. Until then they are **internal briefing material only**.

> **Insight #1: The best reference for Samsung India is another part of Samsung**
> **Evidence:** S3B: Samsung is on y.uno's customer logos ([y.uno](https://y.uno/en/success-stories)), and no orchestrator was found on any APAC store. S1: India is 29.06% of samsung.com traffic, more than the next three markets combined.
> **Pain Point:** The largest web market runs on an unidentified, apparently direct gateway setup, while some other Samsung entity already runs on Yuno.
> **Yuno Value Proposition:** Extend an existing, procured, security-reviewed Yuno relationship to India: multi-PSP routing, failover and reconciliation without a new vendor onboarding.
> **Best Success Case:** The live Samsung entity, once the account owner shares which one. Never cite it externally without permission.
> **Outreach Angle:** Warm intro via the account owner: "Your colleagues in [entity] already route payments through Yuno; India is a third of samsung.com's traffic."
> **Suggested Subject Line:** "Samsung [entity] → Samsung India: same payments layer?"

> **Insight #2: One brand, a different PSP per country**
> **Evidence:** S3A: Midtrans (ID, own FAQ) and KG Inicis (KR, own privacy policy); India unknown; Mexico job ad managing local PSPs (unverified). S2: Indonesia's legal seller is a third-party retailer, while Samsung collects payment.
> **Pain Point:** Every subsidiary negotiates, integrates and reconciles its own gateway. There is no regional routing, no shared token vault and no single view of approval rates.
> **Yuno Value Proposition:** One integration across subsidiaries, keeping each local PSP (Midtrans, Inicis) while adding routing, failover and unified reporting.
> **Best Success Case:** The live Samsung entity (internal).
> **Outreach Angle:** "Samsung Indonesia runs on Midtrans and Samsung Korea on Inicis. Who sees approval rates across both?"
> **Suggested Subject Line:** "Midtrans in Jakarta, Inicis in Seoul"

> **Insight #3: OnePlus has already orchestrated the India smartphone checkout**
> **Evidence:** S11C: OnePlus on Juspay orchestration with "intelligent PSP routing" across "regional PSPs and APMs" during launches and flash sales ([Juspay](https://juspay.io/customer-stories/oneplus), fetched). S1: India is Samsung's #1 web market. S5: a recurring "debited, no order" pattern on Samsung India's own forum (unverified).
> **Pain Point:** Launch-day spikes (Galaxy foldables, S-series pre-orders) are when a single-gateway checkout fails, and the competitor has engineered for it.
> **Yuno Value Proposition:** Routing and failover across Indian PSPs, plus reconciliation so that debited-but-unconfirmed payments are caught.
> **Best Success Case:** The live Samsung entity (internal).
> **Outreach Angle:** "OnePlus routes launch-day traffic across several Indian PSPs. What happens on samsung.com/in when one gateway slows during a Fold launch?"
> **Suggested Subject Line:** "Launch day on samsung.com/in"

> **Insight #4: Thailand turns away every foreign card**
> **Evidence:** S4: *"Credit / Debit Card issued in Thailand only"* ([TH FAQ](https://www.samsung.com/th/shop-faq/payment-and-financing/accepted-payment-methods/), fetched). S1: Thailand is 2.11% of traffic (~17.1M visits/month derived).
> **Pain Point:** Expats and visitors with non-Thai cards cannot buy, likely a deliberate fraud or acquiring-scope choice `[INFERENCE]`.
> **Yuno Value Proposition:** Add a cross-border-capable acquirer for foreign BINs, with fraud rules, without touching the domestic PSP.
> **Best Success Case:** Not chosen; no published Yuno case matches.
> **Outreach Angle:** Secondary, low volume. Use only as a supporting point.
> **Suggested Subject Line:** "Foreign cards on samsung.com/th"

---

### Quick Hits: Ready-to-Use Sales Ammunition

*Internal use only until the account owner clears an approach.*

**Email hooks (one sentence each):**
1. Samsung Indonesia's store takes payment through Midtrans and Samsung Korea's through KG Inicis, two separate gateways with no shared routing between them.
2. OnePlus already runs Juspay orchestration with PSP routing across India; samsung.com/in is a third of Samsung's global web traffic.
3. samsung.com/th accepts only Thai-issued cards.

**Cold call openers (conversational, one sentence each):**
1. "Your colleagues in [entity] already use Yuno — would India want the same routing layer?"
2. "Who at Samsung India owns gateway performance on launch days?"
3. "Do your Indonesia and Korea teams ever compare approval rates across Midtrans and Inicis?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| OnePlus | oneplus.com | China | Not found | India, global | **Juspay** (orchestration, Hyper Checkout) | [Juspay](https://juspay.io/customer-stories/oneplus), fetched |
| Xiaomi | mi.com | China | Not found | India, SEA | **Juspay/Hyperswitch** `[UNVERIFIED — 403]` | [Hyperswitch](https://hyperswitch.io/case-studies/xiaomi) |
| realme | realme.com | China | Not found | India | Juspay per TAL (unsourced) | `accounts/apac-tal.csv` |
| Oppo | oppo.com | China | Not found | India, SEA | Not found | — |
| Vivo | vivo.com | China | Not found | India, SEA | Not found | — |
| LG Electronics | lg.com | South Korea | Not found | KR, JP, SG, IN | Stripe (Japan) `[UNVERIFIED]` | [Stripe](https://stripe.com/en-sk/customers/lg-electronics) |
| Apple | apple.com | US | Not found | IN, JP, KR, AU | Not found for apple.com/in | — |
| Lenovo / Motorola | lenovo.com | China/HK | Not found | Global, India | In-house payment platform (Lenovo); PayU (Motorola India) `[UNVERIFIED]` | [Lenovo](https://basd.lenovo.com/en/ProductandServices/ValueChain/Sales/unifiepay.html) |

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Croma | croma.com | Electronics retail | India | High-ticket electronics + EMI; Juspay per TAL (unsourced) | `apac-tal.csv` |
| Vijay Sales | vijaysales.com | Electronics retail | India | Same; Juspay per TAL (unsourced) | `apac-tal.csv` |
| Dyson | dyson.com | Premium appliances D2C | IN, JP, KR, AU | Per-market PSPs (NHN KCP, JACCS, Afterpay); no orchestrator | `2-ready-to-outreach/dyson.md` |
| JB Hi-Fi | jbhifi.com.au | Electronics retail | AU, NZ | Electronics + BNPL | `apac-tal.csv` (no PSP data) |
| Harvey Norman | harveynorman.com.au | Electronics/appliances | AU, NZ, SG, MY | Multi-market electronics | `apac-tal.csv` (no PSP data) |
| COURTS | courts.com.sg | Electronics retail | SG, MY | Instalment-heavy | `apac-tal.csv` (no PSP data) |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| OnePlus | Juspay | Not dated | Smartphones | https://juspay.io/customer-stories/oneplus |
| Xiaomi | Juspay (Hyperswitch) | Not dated | Smartphones | https://hyperswitch.io/case-studies/xiaomi `[UNVERIFIED — 403]` |

#### 11D. Prospect Scoring

Peers were not scored in full: the agents gathered PSP and orchestrator evidence only, which is too thin for the 29-point matrix. Partial signals:

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| OnePlus: orchestration status | +3 | ✅ Regional orchestrator (Juspay), so a displacement motion | Juspay customer story |
| Xiaomi: orchestration status | +3 | ⬜ Juspay/Hyperswitch, unverified | Hyperswitch (403) |
| Dyson: orchestration status | +4 | ✅ None detected (per existing report) | dyson.md |
| LG Electronics: multiple PSPs | 0 | ⬜ Stripe JP unverified | Stripe |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | OnePlus | Competitor | India | Not scored | 🟢 | Confirmed Juspay orchestration → displacement | ✅ |
| 2 | Xiaomi | Competitor | India, SEA | Not scored | 🟢 | Juspay (unverified) | ✅ |
| 3 | LG Electronics | Competitor | KR, JP, SG, IN | Not scored | 🟢 | Korean peer, Stripe in JP (unverified) | ✅ |
| 4 | Oppo | Competitor | India, SEA | Not scored | — | No stack data | ✅ |
| 5 | Vivo | Competitor | India, SEA | Not scored | — | No stack data | ✅ |
| 6 | Lenovo | Competitor | Global | Not scored | — | In-house payments platform (unverified) | ✅ |
| 7 | Croma | Peer | India | Not scored | — | Juspay per TAL | ✅ |
| 8 | Harvey Norman | Peer | AU, NZ, SG, MY | Not scored | — | Multi-market | ✅ |
| 9 | **Apple** | Competitor | IN, JP, KR, AU | Not scored | — | Large APAC D2C stores | ❌ **Not on TAL** |
| 10 | **Motorola India** | Competitor | India | Not scored | — | PayU on VTEX store (unverified) | ❌ **Not on TAL** |

**Not on the TAL:** Apple (a huge D2C store, but likely an in-house stack and a hard sell), Motorola India, Nothing, Reliance Digital and Sony Electronics. Motorola India and Reliance Digital are the realistic adds.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | Group FY2025 KRW 333.6T; Samsung India FY25 ₹1,11,183 cr | [Khan](https://www.khan.co.kr/en/article/202601290845007), [Business Standard](https://www.business-standard.com/companies/news/samsung-fy25-revenue-from-operations-rises-over-11-to-1-11-trillion-125111900332_1.html) `[UNVERIFIED — search summary only]` |
| GMV / Gross Transaction Volume | No D2C GMV found for any APAC market | — |
| Average Transaction Value (USD) | Not found | — |
| Est. Annual Transactions | Not computable: no sourced D2C revenue or ATV | — |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. [ASSUMPTION — not researched.]** Basis: India store at any plausible online share (1–10% of ₹1.11 lakh cr) and a ₹30,000 assumed ticket gives ~31k–310k orders/month; plus Korea, ID, TH, SG and others. The gate cannot fire on an assumption. **Billing unit:** D2C device and accessory orders | See ICP breakdown |
| Active Customers / Users | Not found | — |
| Primary Currency | Local per store (INR, KRW, IDR, THB…) | Country store pages |
| Top 3 Markets by Revenue | Not found (traffic: India, Brazil, US) | — |
| Billing channel split (web vs app store) | D2C stores are web + Samsung Shop app, billed by Samsung, not IAP. Galaxy Store purchases go through Samsung's own billing and are out of scope | Supplied traffic file caveat 4 |

No public D2C revenue or GMV data found. Business case sizing will require a discovery call, or the existing account owner.

---

### Overall Research Confidence

**Medium.**
- **Traffic:** supplied by Prateek (SimilarWeb Sales Intelligence, 2026-10-19), with shares only and app traffic excluded. All its caveats are applied.
- **Strong:** Indonesia (PSP, seller and payment collector, all fetched), Thailand and Singapore methods (fetched), the Korea PSP (fetched, with a dating caveat), and the Yuno logo finding (fetched).
- **Weak:** the India PSP, which is unknown and the single most important gap. Also weak: India's UPI status, every transaction-volume figure, and the complaints, all of which come from search summaries.
- **Not done:** the checkout audit, beyond observable elements.

---

### Manual Research Recommendations

> **Area:** Existing Yuno relationship
> **Why it matters:** It decides whether this account can be worked at all, and by whom.
> **Suggested manual action:** Look up Samsung in CRM / ask in the Yuno sales channel: which entity, which markets, who owns it, is APAC expansion welcome.

> **Area:** Monthly transaction count
> **Why it matters:** The +5 is assumed. Without it the score drops to 14 (🟢).
> **Suggested manual action:** Ask the account owner for transaction volumes on the live Samsung entity; for India, look for D2C order volume in Samsung India RoC filings or trade press.

> **Area:** India PSP and UPI
> **Why it matters:** India is 29% of traffic and the lead market for any APAC pitch.
> **Suggested manual action:** Place a test checkout on samsung.com/in up to the payment page. Record the gateway domain and merchant name, and whether UPI and RuPay appear.

> **Area:** Korea Inicis currency
> **Why it matters:** The clause carries a 2013 label.
> **Suggested manual action:** Test checkout on samsung.com/sec; confirm the PG on the payment window.

---

### Appendix: All Source URLs

**Yuno / gate**
- https://y.uno/en/success-stories

**Traffic**
- `accounts/traffic/samsung.md` (SimilarWeb, supplied 2026-10-19)

**Section 2**
- https://www.samsung.com/in/
- https://www.samsung.com/in/shop-terms-of-use/
- https://www.samsung.com/id/shop-faq/service-and-warranty/what-is-samsung-online-stores-terms-and-conditions/
- https://www.samsung.com/sec/info/privacy/01/rc/
- https://www.samsung.com/au/
- https://news.samsung.com/jp/launches-official-samsung-shop-app-in-japan
- https://news.samsung.com/th/president-mr-sunghwan-kim
- https://www.samsung.com/sg/business/offers/
- https://www.samsung.com/my/shop-faq/service-and-warranty/what-are-the-terms-and-conditions/
- https://www.samsung.com/ph/info/online-shop-tnc
- https://images.samsung.com/is/content/samsung/assets/vn/shop-faq/samsung-account/chinh-sach-ve-gia.pdf

**Section 3**
- https://www.samsung.com/id/shop-faq/payment-and-financing/what-payment-methods-are-available-on-samsung-online-store/
- https://builtwith.com/samsung.com
- https://www.overseasjobs.com/job/details/37250222/payments-gateway-specialist

**Section 4**
- https://www.samsung.com/in/shop-faq/payment-and-financing/how-do-i-pay-for-my-order/
- https://www.samsung.com/in/shop-faq/payment-and-financing/what-are-various-finance-programs-available-on-samsung-com/
- https://www.samsung.com/in/microsite/finance-plus/
- https://www.samsung.com/sec/eventList/creditcard_benefit
- https://www.samsung.com/id/offer/bank-promo-and-installment/
- https://www.samsung.com/th/shop-faq/payment-and-financing/accepted-payment-methods/
- https://www.samsung.com/sg/shop-faq/payment-and-financing/what-online-payment-methods-do-you-accept/

**Section 5**
- https://r2.community.samsung.com/t5/Samsung-Online-Store/Payment-have-been-deducted-but-order-has-not-processed/td-p/15366109
- https://r2.community.samsung.com/t5/Samsung-Online-Store/Money-deducted-yet-no-confirmation-nor-cancellation/td-p/4875454
- https://r2.community.samsung.com/t5/Samsung-Online-Store/Refund-not-received-after-35-days/m-p/12276999/highlight/true
- https://voxya.com/consumer-complaints/merchant-charged-extra-amount/266976
- https://voxya.com/consumer-complaints/product-not-delivered-got-damaged-at-delivery-office-cancellation-amount-charged/260840
- https://voxya.com/consumer-complaints/loan-emi-payment-not-updated/260001

**Sections 6–7**
- https://news.samsung.com/global/samsung-electronics-announces-earnings-guidance-for-third-quarter-2026
- https://www.koreatimes.co.kr/business/companies/20260730/samsung-electronics-posts-q2-profit-of-62-bil-up-nearly-20-fold
- https://news.samsung.com/in/samsung-india-introduces-breakthrough-features-to-samsung-wallet-redefining-digital-payments-and-upi-onboarding
- https://www.fonearena.com/blog/414939/samsung-galaxy-s24-10-minute-delivery-blinkit.html/amp
- https://ianslive.in/samsung-introduces-30-month-no-cost-emi-plans-for-new-galaxy-foldables-in-india--20260803175805
- https://businesstoday.in/latest/corporate/story/paytm-partners-with-samsung-stores-offers-no-cost-emi-options-344750-2022-08-16

**Section 9**
- https://www.samsung.com/uk/shop-faq/payment-and-financing/is-shopping-on-samsung-com-or-samsung-shop-app-secure/

**Section 11**
- https://juspay.io/customer-stories/oneplus
- https://hyperswitch.io/case-studies/xiaomi
- https://stripe.com/en-sk/customers/lg-electronics
- https://basd.lenovo.com/en/ProductandServices/ValueChain/Sales/unifiepay.html

**Section 12**
- https://www.khan.co.kr/en/article/202601290845007
- https://www.business-standard.com/companies/news/samsung-fy25-revenue-from-operations-rises-over-11-to-1-11-trillion-125111900332_1.html
- https://www.dailyexcelsior.com/?p=1005690
- https://www.kedglobal.com/newsView/ked202304180016

</details>
