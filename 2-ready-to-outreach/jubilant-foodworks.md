# Jubilant FoodWorks

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 18 / 29 → ⭐ **High Priority**
**Industry:** Quick-service restaurants / food delivery — Domino's Pizza master franchisee (India, Sri Lanka, Bangladesh), Popeyes (India), Hong's Kitchen (India), Domino's + COFFY in Türkiye/Azerbaijan/Georgia via DP Eurasia · **HQ:** Noida, Uttar Pradesh, India — Jubilant FoodWorks Limited, **CIN L74899UP1995PLC043677**, NSE: JUBLFOOD / BSE: 533155 · **Researched:** 2026-10-05 · **First email sent:** —
**Motion:** 🛑 **IN-HOUSE — they built it, and it is called `unifiedpayment`.** First-party proof: the Java class `com.jubl.food.unifiedpayment.entity.TokenDetails` is leaked into their shipped production bundle, alongside a client ID `unifiedpayments-prod-pwa` and a self-hosted PCI redaction service at `/data-security-sentinel/ve1/inbound/redact/unified-payments-cards-input-route`. Independently corroborated: CIO.inc reports JFL is **"transitioning from legacy outsourced systems to proprietary solutions"** with a **250-member** in-house tech team (article prose, not a quoted executive). **NEVER say they need orchestration.** Anchor on reach, reconciliation and opportunity cost.

---

> ## ⛔ READ THIS BEFORE YOU SEND ANYTHING — a live commercial blocker
>
> **Razorpay and Cashfree have both publicly stepped back from supporting third-party payment-orchestration and routing platforms — as a category, not just one vendor.** Verified by direct fetch of [Entrackr, 20 Jan 2025](https://entrackr.com/news/after-phonepe-razorpay-and-cashfree-suspend-direct-integrations-with-juspay-8638638):
>
> - Razorpay: **"pause all integrations through third-party routing platforms"**
> - Cashfree: **"transition away from integrations via third-party routers and orchestrators. By offering direct integration, we can accelerate the delivery of features and provide superior support and merchant experience"**
> - The fetched article states the scope is **all** third-party orchestration/routing platforms, not exclusively one vendor. PhonePe moved first, in Dec 2024.
>
> **Why this lands on this specific account: Razorpay is one of Jubilant's seven gateways** — I pulled `RAZORPAY` out of their own gateway enum, and their token fixture carries `"gateway":"RAZORPAY"` with a Razorpay-format `token_` value.
>
> **So before Prateek writes a word: confirm with Yuno Solutions/Partnerships whether Yuno can currently route Razorpay volume in India.** If it cannot, the honest pitch covers their PayU / BillDesk / Paytm / PayHere / SSLCommerz legs and leaves Razorpay direct — which is still a real pitch, but it is a *different* pitch, and a payments engineer at Jubilant will know this news. Walking into it unprepared loses the room.
>
> A secondary, **unverified** report (search summary, page not fetched) gives Razorpay an effective date of **30 April 2025** and says Pine Labs will continue working with orchestrators. Do not quote either without verification. Sources: [Inc42](https://inc42.com/buzz/razorpay-cashfree-to-discontinue-partnership-with-juspay/), [Business Standard](https://www.business-standard.com/industry/news/payment-aggregators-call-for-break-from-juspay-s-third-party-routing-125033000575_1.html).

---

> ## 🎯 THE HOOK — the payment succeeds, the order is never created, and it happens on every rail they accept
>
> Four dated complaints from **one page** of Domino's India's complaint backlog on [consumercomplaints.in](https://www.consumercomplaints.in/dominos-pizza-b100147) (fetched, HTTP 200; page shows **6,604 complaints, 727 resolved / 5,877 unresolved**):
>
> | Date | Rail | Amount | Complaint title (verbatim) |
> |---|---|---|---|
> | **31 Jul 2026** | BHIM UPI — HDFC UPI **RuPay credit card** | ₹414.28 **×2** | "Payment deducted **twice** but orders not placed and not showing in Order History" |
> | **27 Jan 2026** | PhonePe | ₹865.20 | "Payment successful in phonepay to dominos but failed to place order" |
> | **27 Dec 2025** | Paytm | ₹461 | "Payment successful but order not created in Domino's pizza app" |
> | **23 May 2025** | Paytm | ₹217 **×2** | "Charges **debited twice** for single order, no customer support" |
>
> ### Why this is the whole pitch
> **The symptom is identical across four different rails — UPI, UPI-on-RuPay-credit, PhonePe and Paytm.** A fault that reproduces on every rail is not a PSP fault. It sits in the merchant's own payment-success-to-order-creation handoff — the callback/reconciliation leg. **That is the exact failure class a routing layer owns as a product concern rather than as bespoke code.**
>
> Two of the four are **double debits**, which is the signature of a retry against a transaction the merchant has not reconciled — an idempotency gap.
>
> ### The same symptom appears in Sri Lanka
> A TripAdvisor review of **Domino's Nugegoda, Colombo** — unambiguously Jubilant's Sri Lanka estate — is titled **"They deduct you money and then say the order was failed!!"** ([source](https://www.tripadvisor.in/ShowUserReviews-g3181345-d8002456-r940870440-Domino_s_Pizza-Nugegoda_Western_Province.html); title from the search result, body not fetched). Same wording, different country, different acquiring setup — consistent with a shared layer.
>
> ### And they have automated the apology rather than closed the gap
> Q4 FY26: Jubilant launched a **GenAI chatbot on the Domino's app** that handles complaints and **issues coupons autonomously** — the investor deck shows it granting a **₹150 coupon "as a service gesture" with no human in the loop**. ([medianama, Jun 2026](https://www.medianama.com/2026/06/223-jubilant-foodworks-q4fy26-genai-chatbot-delivery-growth/) — `[UNVERIFIED — search summary only]`.)
>
> **Handle this one carefully.** It is a genuinely sharp observation and it is also the single easiest way to insult a team that is proud of its build. Never frame it as "you're papering over a bug." The usable framing is cost: goodwill coupons are a per-incident payout, and the incident rate is set by the reconciliation leg.

---

> ## ⭐ THE SECOND HOOK — their saved-card tokens are bound to the gateway that created them
>
> Their production bundle ships a **fixture record from their own card vault** (a test record — `userId:"CUST_001"`, `status:"INACTIVE"` — **not live cardholder data**):
>
> ```json
> {"userId":"CUST_001","tokenId":"spt_LrS23jKtrgQQef","tenant":"oms_merchant_id_1",
>  "gateway":"RAZORPAY","methodCode":"CC","cardSuffix":"5366",
>  "panUniqueId":"V0010014621237165919303334037","status":"INACTIVE",
>  "network":"Visa","issuer":"HDFC",
>  "additionalInfo":{"cardToken":"token_Lx2yg0zNjflOgU"},
>  "_class":"com.jubl.food.unifiedpayment.entity.TokenDetails"}
> ```
>
> **`"gateway"` is a field on the token.** So a card tokenized at Razorpay is a Razorpay token; it is not chargeable through PayU or BillDesk. **Their routing freedom therefore stops at the returning customer** — the moment they want to route a repeat buyer to a better-performing acquirer, that customer loses their saved card and re-enters it.
>
> This is the cleanest, least insulting technical argument available on this account. It is not "your build is wrong" — it is a structural property of a gateway-scoped vault, and the fix (network tokens / a gateway-agnostic vault) is a capability, not a criticism. They implement the RBI card-on-file shape correctly: `panUniqueId`, `cardSuffix`, `network`, `issuer`, no raw PAN.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** India's largest QSR operator by store count (~3,636 at FY26 end). Master franchisee for **Domino's Pizza in India, Sri Lanka and Bangladesh** — renewed in Mar/Apr 2026 for **15 years with a further 10-year option** — plus **Popeyes** and **Hong's Kitchen** in India, and **Domino's + COFFY** across Türkiye, Azerbaijan and Georgia through its controlling stake in DP Eurasia N.V. FY26 consolidated revenue **₹9,512.51 crore (~US$987m)**, +17.4% YoY. **Exiting Dunkin' India** when that pact ends 31 Dec 2026.

**SimilarWeb total visits (last full month):** `dominos.co.in` **~3 million/month** — ⚠️ `[ESTIMATE, not confirmed]`, web-search sourced, **not supplied**. **Do not use web traffic to size this account.** It is app-first: **55% of orders come from its own apps** ([CIO.inc, 1 Apr 2025](https://www.cio.inc/from-pizza-to-ai-how-jfl-baking-tech-into-every-bite-a-27889), fetched), **17.1m own-app MAU** and **5.7m monthly transacting users**. Three million web visits understates the real transaction count by more than an order of magnitude.

### Top markets
Ranked by **operations and payment-stack scope**, not web traffic — web traffic is the wrong metric here and is 93.96% India in any case.

| Rank | Country | Traffic / scale | Accepted methods (status) | Missing / absent | Local entity |
|------|---------|-----------------|---------------------------|------------------|--------------|
| 1 | 🇮🇳 **India** | 93.96% of web traffic; 2,455 Domino's stores; Q3FY26 revenue +11.8% | **LIVE-VERIFIED** — UPI QR, cards (CC/DC), e-voucher, netbanking (~45 banks), COD, "other wallets", in-app stored value. UPI apps incl. PhonePe + Amazon UPI; Paytm & Amazon Pay wallets | **Meal/benefit cards (Pluxee/Sodexo) — no code path.** No EMI/instalment code path (verified absent; low-ticket, so not a real gap) | ✅ Jubilant FoodWorks Ltd, CIN L74899UP1995PLC043677 |
| 2 | 🇧🇩 **Bangladesh** | Q3FY26 revenue **+26.6%** | **CODE-INFERRED** — bKash, Rocket (`DBBL_MB`), AB Bank Direct, upay, iPay, netbanking (Islami, City Touch, Bank Asia, Mutual Trust), FastCash/QCash cards. Gateway: SSLCommerz | **Nagad — no code path** (#2 MFS, 28.2m active users). ⚠️ See the Nagad caveat below before using this | ✅ Jubilant FoodWorks Bangladesh Ltd + Jubilant Golden Harvest Ltd |
| 3 | 🇱🇰 **Sri Lanka** | Q3FY26 revenue **+65.9%** — fastest-growing market in the group | **CODE-INFERRED** — generic `CARD` + `OTHERS` only. "We Accept" row: Visa, Mastercard, Amex, Discover, Diners, **Genie**, **FriMi**. Gateway: PayHere | **No card-on-file / tokenization service** (India-only). **In-app wallet explicitly blocked** (`IS_WALLET_BLOCKED: true`) | ✅ Jubilant FoodWorks Lanka (Pvt) Ltd |
| 4 | 🇹🇷 Türkiye + 🇦🇿 🇬🇪 | COFFY 194 stores; Domino's TR ~690 | **Separate estate.** First-party: **Masterpass** (Mastercard) for card-on-file, direct card entry, **Domino's Cüzdan** wallet, meal vouchers, cash | No acquirer/PSP named publicly | ✅ via DP Eurasia N.V. (Netherlands) + Jubilant FoodWorks Netherlands B.V. |

⚠️ **Türkiye, Azerbaijan and Georgia are EMEA, not Prateek's territory.** The account is in scope because Jubilant is India-HQ'd. Use the Türkiye estate as *evidence of multi-stack complexity*, never as a market being sold into.

### Legal entities
- **Jubilant FoodWorks Limited** (India) — CIN **L74899UP1995PLC043677**, inc. 16 Mar 1995, RoC-Kanpur, Plot 1A Sector 16-A Noida 201301
- **Jubilant FoodWorks Lanka (Private) Limited** (Sri Lanka) — reg. no. not found
- **Jubilant FoodWorks Bangladesh Limited** + **Jubilant Golden Harvest Limited** (Bangladesh) — reg. nos. not found
- **Jubilant FoodWorks Netherlands B.V.** (Netherlands) — the DP Eurasia acquisition vehicle
- **DP Eurasia N.V.** (Netherlands; ops Türkiye/Azerbaijan/Georgia) — taken private, formerly LSE: DPEU
- **Jubilant FoodWorks International Luxembourg** — ⚠️ medium confidence, single secondary source (Nov 2022)
- **Fides Food Systems Coöperatief U.A.** (Netherlands) — **merged into Jubilant FoodWorks Netherlands B.V. 2 Mar 2022; no longer live**
- **Nepal** — board approved a subsidiary Nov 2022; **name never found, launch never confirmed**

### Known PSPs — seven gateways, from their own code
Extracted by me from `m.dominos.co.in/jfl-discovery-payment/public/dist/default/js/payment.js` (HTTP 200, 1,825,175 bytes):

```js
xf = {PAYU:"PAYU", PAYTM_PG:"PAYTM_PG", BILLDESK:"BILLDESK", PAYTM_WALLET:"PAYTM_WALLET",
      GLOBALPAY:"GLOBALPAY", SSLCOMMERZ:"SSLCOMMERZ", RAZORPAY:"RAZORPAY"}
```
- **PayU** — `[Source Code]` · India · `payuPayload` hand-built, lowercased key duplication, `ccnum` injected
- **Paytm PG** — `[Source Code]` · India · dedicated `/payment-verify-service/ve3|ve4/orders/pg/paytm/submit`
- **BillDesk** — `[Source Code]` · India · returns `initiateHtml`, rendered in an HTML modal
- **Razorpay** — `[Source Code]` · India · `RAZOR_SALT_ID`; token fixture shows `"gateway":"RAZORPAY"`
- **Paytm Wallet** — `[Source Code]` · India · link/verify/balance/redeem endpoints
- **SSLCommerz** — `[Source Code]` · **Bangladesh**
- **PayHere** — `[Source Code]` · **Sri Lanka** · `PAYHERE_SDK:"pg_sdk_hash"` + a whole Vuex module (`Payhere/initiatePayment`, `Payhere/initiatePaymentStatusPoll`, `Payhere/updatePayloadForPayhere_pg`)
- **`GLOBALPAY`** — ⚠️ **NOT IDENTIFIED.** Handed off via `postFormData(globalpayUrl, globalpayPayload)`. No public source links Jubilant to any "GlobalPay"/Global Payments product. Global Payments Inc. does hold India and Sri Lanka entities, but Sri Lankan bank IPGs run on MPGS/CyberSource. **Treat as unknown. Do not name it in outreach.**

### Orchestration status
**🛑 In-house orchestration layer — confirmed from first-party artefacts, not inferred.**

| Evidence | Detail |
|---|---|
| Leaked backend class | `com.jubl.food.unifiedpayment.entity.TokenDetails` — their own Java package, MongoDB extended JSON |
| Service client ID | `sentinelClientId: "unifiedpayments-prod-pwa"` |
| API response envelope | `unifiedPaymentResponse.nextActions` — their API tells the client what to do next |
| Dispatch | A hand-written `switch` over `xf.*`: `case xf.BILLDESK → initiateHtml` / `case xf.GLOBALPAY → postFormData(globalpayUrl…)` / `case xf.SSLCOMMERZ → …`. **Every gateway is a bespoke `case`.** |
| Their own named service | `/jfl-payment-aggregator/ve1/payment/transaction-status` |
| Self-hosted PCI redaction | `/data-security-sentinel/ve1/inbound/redact/unified-payments-cards-input-route` — "Sentinel" is theirs; no vendor product of that name exists in Indian payments |
| Corroborated publicly | CIO: **"transitioning from legacy outsourced systems to proprietary solutions"**, **250-member** product/UX/tech/data-science team, **"over 100 independent microservices"** ([CIO.inc](https://www.cio.inc/from-pizza-to-ai-how-jfl-baking-tech-into-every-bite-a-27889), fetched 2026-10-05) |

**No vendor publicly claims them.** Juspay, Razorpay Optimizer, PayU Switch, Cashfree, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails and Yuno were all checked — zero case studies, zero logo-wall appearances. Consistent with in-house.

### Buying signals
- 💼 ⭐ **CIO seat vacant.** Narottam Sharma resigned effective **18 Sep 2026** "to take up an external opportunity"; **no successor announced**. ([IndianRetailer](https://www.indianretailer.com/news/narottam-sharma-steps-down-jubilant-foodworks-cio), [BW People](https://www.bwpeople.in/article/jubilant-foodworks-cio-narottam-sharma-to-exit-company-in-september-616072)) — `[UNVERIFIED — two independent search summaries, neither fetched]`. **~2.5 weeks old. Re-verify before using.**
- 🤝 ⭐ **Domino's master franchise renewed Mar/Apr 2026 for 15 years + a 10-year option**, covering exactly India, Sri Lanka and Bangladesh. A long-dated commitment to the three markets that share the one payment codebase — the cleanest possible reason to invest in payment infrastructure now. ([Business Standard](https://www.business-standard.com/companies/news/jubilant-foodworks-renews-dominos-franchise-for-15-years-126040101142_1.html)) `[UNVERIFIED — search summary only]`
- 🚀 **+351 net new stores in FY26** (3,316 → ~3,636); Popeyes targeting ~250 stores in 3–4 years from 73
- 📉 **Exiting Dunkin' India** — pact ends **31 Dec 2026**. **Do not mention Dunkin' in outreach.** ([BusinessWorld](https://www.businessworld.in/article/jubilant-foodworks-to-exit-dunkin-india-partnership-as-pact-ends-in-2026-599993)) `[UNVERIFIED]`
- 🏗️ **Competitive urgency:** Devyani International and Sapphire Foods announced a **US$934m all-share merger** (~2 Jan 2026) creating a **3,002-store** KFC/Pizza Hut/Costa/Taco Bell group — roughly closing the store-count gap with Jubilant, and forcing a two-stack payment integration across India/Sri Lanka/Maldives/Thailand/Nepal/Nigeria. ([CNBC](https://www.cnbc.com/2026/01/02/devyani-sapphire-merger-yum-brands-india-kfc-pizza-hut-taco-bell-dominos.html)) `[UNVERIFIED — search summary only]`
- 📋 **No public payment RFP found.** Stated explicitly.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Jubilant FoodWorks` to draft the 12-touch sequence, or call this from `/prepare_batch`.*

**Mandatory constraints for whoever drafts this — read before writing a word:**
1. **Resolve the Razorpay/Cashfree orchestrator question first** (see the blocker box at the top). It changes what Yuno can credibly offer in India.
2. **Motion is IN-HOUSE.** They are publicly proud of the build. Never imply they need orchestration, never imply the build was a mistake. Anchor on reach, reconciliation and opportunity cost.
3. **Never name Juspay** or any other Yuno competitor in the sequence, even though this file names them as intelligence.
4. **No booking link.** Every CTA is a plain time proposal.
5. **Target the CTO or CPO, not a payments title — no payments owner exists.** Pawan Kumar (EVP & CTO, since ~31 Mar 2020); Vaneet Singla (EVP & Chief Product Officer, since ~16 Jun 2021). The CIO seat is empty.
6. **Do not pitch:** EMI/instalments in India (₹-hundreds tickets — absence is correct); Sri Lankan wallets (≤1% of SL online payment); BNPL (Simpl reportedly halted by RBI Sep 2025); RuPay-credit-on-UPI (not a merchant-side integration); UPI Autopay / e-mandate (**no recurring product exists**); Dunkin' India (exiting); Türkiye/Azerbaijan/Georgia as target markets (EMEA).
7. **Lead India on meal cards, Sri Lanka on card-on-file, Bangladesh on rail overhead.** Not on Nagad.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 18 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED (floor): ≥ 5,700,000 / month.** Input: **5.7 million monthly transacting users (MTU), Q3 FY26, +21% YoY** — disclosed on the earnings call, reported by [medianama](https://www.medianama.com/2026/02/223-jubilant-foodworks-dominos-app-ad-platform-q3fy26-earnings-call/). A monthly transacting user transacts ≥1× per month by definition, so monthly transactions ≥ MTU. **Band ≥100,000 → +5.** Billing unit counted: a food order on Jubilant's own app/web. Consistency check: ₹1,801.5cr India Q3 revenue ÷ 3 ÷ 5.7m = ₹1,053/order, far above any plausible Domino's ticket — so the true count materially exceeds the floor. **AOV is not disclosed**, so no point estimate is given. |
| Orchestration status | **+1** | ✅ **In-house layer confirmed** (`com.jubl.food.unifiedpayment`, `unifiedPaymentResponse`, `jfl-payment-aggregator`, `data-security-sentinel`) + public corroboration from the CIO. Scores +1, not +4 — this is the hardest sell in the matrix. |
| 3+ countries | **+3** | ✅ One payment codebase serves **India, Sri Lanka, Bangladesh** (`{IN:"india", LK:"sriLanka", BG:"bangladesh"}`); group operates **six markets**; **5+ legal entities confirmed**. |
| Multiple PSPs | **+3** | ✅ **Seven gateways** in their own enum + PayHere as an eighth handoff path. Verified from source code. |
| Local rail / licensing gap in a top-3 market | **0** | ⬜ **Taking zero deliberately, and the reasoning is the value.** India's coverage is genuinely comprehensive — UPI (4 app paths), ~45 netbanking banks, cards incl. RuPay, two wallets, COD. Bangladesh carries bKash *and* Rocket *and* 4 banks. Sri Lanka's thin config is **market-rational**: COD is **52%** of SL online retail payment and rising, cards 35% and falling, **e-wallets ≤1%** ([Daily Mirror / APIDM–Kelaniya Digital Outlook SL 2025](https://www.dailymirror.lk/print/business-news/Sri-Lankan-online-shoppers-stick-to-cash-on-delivery-amid-digital-payment-hesitation/273-307888)). No local entity is missing in any top market. **The meal-card gap is real but is not a "dominant local rail" and this row should not be stretched to fit it** — it is argued in Section 10 instead. |
| Recent expansion | **+2** | ✅ **+351 net stores in FY26**; Popeyes 73 → ~250 target; 15-year Domino's renewal across IN/LK/BD (Mar/Apr 2026). |
| Payment issues | **+2** | ✅ **Confirmed pattern, moderate-to-high frequency.** "Payment succeeded, order not created" across **four different rails**, dated **23 May 2025 → 31 Jul 2026**, two of them **double debits**; **5,877 unresolved** of 6,604 complaints on the brand page. Same symptom independently visible in Sri Lanka. |
| Funding >$10M | **0** | ❌ Listed company (NSE/BSE). No funding round — not applicable. |
| High traffic outside home | **0** | ❌ India is **93.96%** of web traffic. Home market far above the 60% threshold. |
| Competitor using orchestration | **+2** | ✅ with a recorded limit. **McDonald's** is a named payment-orchestration customer of an Indian orchestrator, with dynamic real-time PSP routing (vendor case study, fetched). **Burger King** appears on the same vendor's India logo wall. ⚠️ **Neither names a country or operating entity** — so this does **not** establish that Westlife Foodworld or Restaurant Brands Asia is the contracting party, and outreach must not say so. Separately, **Swiggy** — an aggregator channel Jubilant sells through — is confirmed on orchestration with a named finance executive on the record. |
| Payment job postings | **0** | ❌ **No open payments role found**, and no "Head of Payments" title exists anywhere in the company. The only matching posting was a **closed** Senior Software Engineer role (Noida, Java/Microservices/Spring/Hibernate) — which does corroborate the `com.jubl.food…` Java stack, but a closed req is not a hiring signal. |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **⭐ High Priority (18)**

**No RFP override** — no public payment RFP found.

**No analyst override applied.** Three were considered and rejected:
- *App-store revenue* — not applicable. This is food delivery; there is no Apple/Google IAP leg. Revenue runs through their own checkout and through aggregators.
- *Absolute volume too small* — the opposite. This is one of the highest-volume merchants in the repo.
- *Double counting* — "3+ countries" and "multiple PSPs" fire on **independent** facts here: the country split comes from the country-constants module, the seven gateways from the gateway enum. Not the same underlying fact.

⚠️ **One genuine downward pressure that is NOT an override but must be priced into any business case:** **Jubilant sells through Swiggy and Zomato, and for those orders the aggregator collects the payment — it never touches Jubilant's stack.** The addressable base is own-app + own-web only (plus in-store POS on a separate rail, likely non-addressable). The best current figure is **55% of orders from their own apps** (CIO.inc, Apr 2025). Older figures of ~68% own-app are from **2019–2021**, span COVID, and are stale — **do not use them.** Any sizing that takes total revenue as the orchestration-addressable base is wrong.

### Source Notes

**✅ Verified first-hand by me (fetched, parsed, controls run)**
- `payment.js` is **byte-identical across all three countries** — `md5 43acb80254b091185f8311b251342947`, 1,825,175 bytes, served from `m.dominos.co.in`, `m.dominoslk.com` and `m.dominos.com.bd`. One codebase, three tenants.
- Gateway enum, payment-method enum, payment-action enum, the per-gateway dispatch `switch`, the `unifiedPaymentResponse` envelope, the leaked `com.jubl.food.unifiedpayment.entity.TokenDetails` class and its full token fixture.
- **India's enabled method set is LIVE-VERIFIED** from server-rendered `module-data` on `m.dominos.co.in/jfl-discovery-payment/en/dt/payment` (HTTP 200, `<title>Payment</title>`), sort order 17–23: `QRCODE_UPI_WALLET`, `CASHCRD` (=`OTHER_WALLETS`), `CC`, `DC`, `EVOUCHER`, `NB` (3 visible), `CASH`.
- Per-country config diff: tenant keys `D6M9I3N2O1S3` / `…SL` / `…BD`; `sentinelClientId` **India only**; `IS_WALLET_BLOCKED` **true in Sri Lanka only**; Paytm/GPay mini-app keys **India only**.
- Seven payment-domain microservices of their own — `payment-service`, `payment-verify-service`, `saved-card-service`, `unified-payment`, `jfl-payment-aggregator`, `data-security-sentinel`, `wallet-service` — with **ve1–ve6 all in flight simultaneously** (179 ve1 / 76 ve2 / 79 ve3 / 42 ve4 / 5 ve5 / 1 ve6 references).
- **Their payment API is properly secured.** `/payment-service/ve1|ve2/options/default` returned **401 Unauthorized / 403 AccessDenied** on all three country hosts. I stopped there and made no attempt to obtain credentials.
- **Pluxee's own help centre** names its online acceptance as **Swiggy, Zomato, BigBasket, Zepto, JioMart, Blinkit** and displays **Pizza Hut, Costa, Pop Tates, Theobroma, Spencer's** as example brands. **Domino's appears nowhere on the page.**
- **Razorpay/Cashfree orchestrator policy** — Entrackr, 20 Jan 2025, fetched; scope is all third-party orchestrators.
- **CIO.inc article** (1 Apr 2025, author Sandhya Michu) — 250-member team, "legacy outsourced → proprietary", 100+ microservices, 55% D2C orders, Pawan Kumar CTO, Vaneet Singla CPO.
- Five separate digital estates: Domino's IN/LK/BD (`jfl-discovery-*`), **Hong's Kitchen on the same codebase but its own API host** `hongs-prod.hongskitchen.in`, **Popeyes India on a different platform entirely** `api.popeyes.in`, and **Türkiye on `cdn.dpeurasia.com`** with no overlap.

**⚠️ Unverified, or verified only via search summary — do not harden these**
- The ~3m/month SimilarWeb figure and the 93.96% India split — search-sourced estimate, **not supplied**.
- CIO vacancy (18 Sep 2026); 15-year franchise renewal; Dunkin' exit; Devyani–Sapphire merger; GenAI coupon bot; Nagad's share decimals; LankaQR's zero-MDR change.
- **PCI DSS:** Jubilant's FY2019-20 annual report reportedly names ISO 27001, NIST and PCI-DSS as frameworks it follows. **The PDF returned HTTP 403 and was never read.** Treat as unconfirmed.
- The Sri Lanka and Bangladesh **enabled** method sets are **CODE-INFERRED from the shared bundle, not live-verified.** The bundle holds the superset; what is switched on per country sits behind the authenticated API. **Say "no Nagad code path exists in the bundle that serves Bangladesh" — never "Bangladesh doesn't support Nagad."**

**❌ Could not establish**
- **Who `GLOBALPAY` is.** The top open question. Needs a live checkout redirect host or a direct ask.
- Whether a **Nepal** entity was ever incorporated. Popeyes has launched in **none** of Nepal, Bhutan or Bangladesh despite holding rights since Mar 2021.
- PSP for **Popeyes India**; acquirer behind **Domino's Türkiye** / COFFY (Masterpass is confirmed as the card-on-file layer, but not the underlying acquirer).
- **AOV** — not disclosed. Current own-channel vs aggregator split beyond the 55% D2C figure.
- Any **India-attributable payment outage**. Every "Domino's down" artefact found was **Domino's Pizza Inc (US)** and was quarantined, not used.

**Corrections made during this run**
- **FriMi is Nations Trust Bank, not NDB.** I had it wrong in my own research brief.
- The 100,000-outlet / 1,700-city Pluxee figure was cited to a page that **does not carry those numbers** — I fetched it and checked. That figure is not used here.
- `dt` vs `pwa` in the route path is a **surface/order-type prefix, not a different build.** The payment bundle is byte-identical by MD5 and `staticPaymentBaseUrl` is the same string in all three countries.
- **Rocket and Islami Bank ARE present** — as `DBBL_MB` and `IBBL_NB`. My first keyword pass missed them because they are coded by bank abbreviation.

**False positives caught before they reached this file**
`cred` → `credit`/`credential` (CRED not present) · **`slice` → `sliceBalance`, a loyalty *pizza-slice* counter** (slice BNPL not present) · `axis` → `skewFromAxis`/`skewAxis` (Axis Bank not present) · `simpl` → `intersectsImpl` in Lottie bezier code, and independently `SimplyCheese__720x700_FullSizeCard.jpg` in the Sri Lanka bundle (Simpl BNPL not present) · `emi` → `emit`/`emitted` (**zero** true EMI hits, whole-word verified) · `param` on the Türkiye site → `params` (Param the Turkish PSP not present) · `boc` → `isComboCart` (Bank of Ceylon not present) · `tap` → `.tap(` event handlers.

### Success Case Alternatives
- **Tier 1 — a high-volume food-delivery or QSR merchant with multi-country local rails.** The profile match is order frequency and low ticket value, where a fraction of a point of auth rate is a large absolute number. Use whichever Yuno QSR/delivery reference is publicly citable **with published metrics**. ⚠️ **Do not attach a number to any Yuno customer without a published figure.**
- **Tier 2 — same payment pattern: a merchant running one in-house routing layer across several countries and many PSPs**, where the argument was reconciliation and reach rather than "you need orchestration." This is the closer analogue for an in-house motion than any vertical match.
- **Tier 3 — credibility default.** Lead with multi-market rail breadth rather than a named case.

---

## Section 1: Website Traffic Analysis by Country

**Data source:** resolution path 3 — **WebSearch fallback. No SimilarWeb data was supplied and no SimilarWeb MCP tool is configured in this environment.** Everything here is `[ESTIMATE, not confirmed]`.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | 🇮🇳 India | **93.96%** | ~2.82m | Growing (+14.06% MoM) | [SimilarWeb](https://www.similarweb.com/website/dominos.co.in/) `[ESTIMATE]` |
| 2 | 🇺🇸 United States | 3.14% | ~94k | — | same |
| 3 | 🇬🇧 United Kingdom | 0.39% | ~12k | — | same |
| 4 | 🇦🇺 Australia | 0.20% | ~6k | — | same |
| 5 | 🇫🇷 France | 0.17% | ~5k | — | same |

`dominos.co.in` — global rank **#13,355** (prior quarter #16,243), India rank **#1,221**, category rank **#4** in Food & Drink > Restaurants and Delivery (India). Bounce 27.42%, 7.47 pages/visit, ~3m56s duration. A cross-check on the same provider's competitors page ranked it **#5** in that category as of Mar 2026 and gave swiggy.com ~16m visits vs pizzahut.co.in ~419k. The provider's own page is internally inconsistent about whether "3 million" is monthly or a 3-month total.

**⚠️ This table is close to useless for sizing this account, and must not be used that way.**
- **55% of orders come from Jubilant's own apps** (CIO.inc, fetched) — app traffic is invisible to SimilarWeb.
- **17.1m own-app MAU** (Q4 FY26), **17.0m** (Q3 FY26), **5.7m monthly transacting users** (Q3 FY26).
- **~70% of Domino's orders via the own app** (Q3 FY26 investor presentation, via [investywise](https://www.investywise.com/jubilant-foodworks-investor-presentation-for-q3fy26-results/)) `[UNVERIFIED — secondary summary of a primary deck; the deck host 403s]`.
- **Online sales ≈ 87% of delivery sales** — JFL's long-standing disclosed metric; **the 87% value could not be pinned to a specific quarter.**
- No traffic data at all was obtainable for `dominos.com.tr`, `coffy.com.tr`, `popeyes.in`, `hongskitchen.in`, `m.dominoslk.com` or `m.dominos.com.bd`.

**No traffic file was created in `accounts/traffic/`.** That directory is reserved for data Prateek supplies, and `/research` treats anything there as a **primary** source. Writing a search-derived estimate into it would launder an estimate into a primary citation on the next run. **If Prateek wants this upgraded, supply SimilarWeb for `dominos.co.in` — but note that for this merchant the app metrics above are the more honest volume signal either way.**

## Section 2: Legal Entities & Local Presence

**Headquarters:** Noida, Uttar Pradesh, India. Jubilant FoodWorks Limited, incorporated **16 March 1995**, RoC-Kanpur. Registered office Plot No. 1A, Sector 16-A, Noida 201301. Authorised capital ₹800,000,000; paid-up ₹659,845,200.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| 🇮🇳 India | Jubilant FoodWorks Limited | **L74899UP1995PLC043677** | [Zauba](https://www.zaubacorp.com/JUBILANT-FOODWORKS-LIMITED-L74899UP1995PLC043677), [Tofler](https://www.tofler.in/jubilant-foodworks-limited/company/L74899UP1995PLC043677), [ClearTax](https://cleartax.in/f/company/jubilant-foodworks-limited/L74899UP1995PLC043677/) |
| 🇱🇰 Sri Lanka | Jubilant FoodWorks Lanka (Private) Limited | Not found | [Wikipedia](https://en.wikipedia.org/wiki/Jubilant_FoodWorks) |
| 🇧🇩 Bangladesh | Jubilant FoodWorks Bangladesh Limited | Not found | JFL subsidiary lists `[UNVERIFIED]` |
| 🇧🇩 Bangladesh | Jubilant Golden Harvest Limited | Not found | [Wikipedia](https://en.wikipedia.org/wiki/Jubilant_FoodWorks) |
| 🇳🇱 Netherlands | Jubilant FoodWorks Netherlands B.V. | Not found (no KvK) | [MarketScreener](https://www.marketscreener.com/quote/stock/DP-EURASIA-N-V-36190721/news/Jubilant-Foodworks-Netherlands-B-V-completed-the-acquisition-of-51-16-stake-in-DP-Eurasia-N-V-LS-45857638/) |
| 🇳🇱 Netherlands | DP Eurasia N.V. (ops 🇹🇷 🇦🇿 🇬🇪) | Not found | [Investegate](https://www.investegate.co.uk/announcement/rns/dp-eurasia-n-v-di---dpeu/recommended-increased-and-final-cash-offer/7991350) |
| 🇱🇺 Luxembourg | "Jubilant FoodWorks International Luxembourg" | Not found | [BusinessWorld, Nov 2022](https://www.businessworld.in/article/Jubilant-Foodworks-To-Float-Subsidiary-For-Domino-s-Pizza-Biz-In-Nepal-/23-11-2022-455088/) ⚠️ **medium confidence, single secondary source** |
| 🇳🇱 Netherlands | Fides Food Systems Coöperatief U.A. | Not found | **MERGED into JFL Netherlands B.V. 2 Mar 2022 — no longer live** |
| 🇳🇵 Nepal | — | **Not found** | Board approved Nov 2022; **name and launch never confirmed** |

**Ownership chain evidenced:** India → Luxembourg (step-down, medium confidence) → Netherlands B.V. → DP Eurasia N.V. → Türkiye/Azerbaijan/Georgia. **No Singapore or Mauritius holding entity found.**

⚠️ **DP Eurasia stake percentage is genuinely contradictory across sources** — 32.81% (Feb 2021) → 39.79% (Nov 2021) → 41.32% (Mar 2022) → reported variously as "completed acquisition of 51.16%", an offer for "the remaining 51.16%", an offer for "the remaining 45.33%", and a raise to **94.28% in Jan 2024** — then delisted at 110p/share with stated intent to convert to a Dutch B.V. and reach 100%. One source still lists 49.04%, which is stale. **Do not quote a percentage.** The defensible statement: *JFL took DP Eurasia private and controls it.*

**Cross-Border Gap Analysis**

| Country | In Top Markets? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-----------------|-------------------|---------------------------|---------------------|
| 🇮🇳 India | ✅ #1 | ✅ Yes | Yes — but entity present, and a domestic gateway set is in place | **None** — fully domestic |
| 🇧🇩 Bangladesh | ✅ | ✅ Two entities | Likely — local MFS/bank rails require local presence; entity present | **None evident** — SSLCommerz is a domestic gateway |
| 🇱🇰 Sri Lanka | ✅ | ✅ Yes | Entity present; PayHere is a domestic gateway | **None evident** |
| 🇹🇷 🇦🇿 🇬🇪 | Out of territory | ✅ via DP Eurasia | — | EMEA — not assessed |
| 🇳🇵 Nepal | Rights held, **no operations found** | ❌ **Not found** | Would need local presence | **N/A — nothing to acquire yet** |

**Notably, there is no cross-border acquiring gap on this account.** Every operating market has a local entity and a domestic gateway. This is the opposite of the usual APAC pattern, and it means **the standard cross-border approval-rate pitch does not apply here.** Say so internally rather than reaching for it — the argument on this account is reconciliation, routing freedom and estate fragmentation.

> **MANUAL:** Verify the Nepal subsidiary via an MCA/ROC lookup or the FY26 annual-report subsidiary schedule.

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| 🇮🇳 India | **PayU** | `[Source Code]` | `m.dominos.co.in/jfl-discovery-payment/public/dist/default/js/payment.js` |
| 🇮🇳 India | **Paytm PG** | `[Source Code]` | same |
| 🇮🇳 India | **BillDesk** | `[Source Code]` | same |
| 🇮🇳 India | **Razorpay** | `[Source Code]` | same (`RAZOR_SALT_ID`, `"gateway":"RAZORPAY"`) |
| 🇮🇳 India | **Paytm Wallet** | `[Source Code]` | same |
| 🇧🇩 Bangladesh | **SSLCommerz** | `[Source Code]` | same |
| 🇱🇰 Sri Lanka | **PayHere** | `[Source Code]` | same (`PAYHERE_SDK`, `Payhere/*` store module) |
| ❓ Unknown | **`GLOBALPAY`** | `[Source Code]` — **provider NOT IDENTIFIED** | same |
| 🇹🇷 Türkiye | **Masterpass** (Mastercard) — card-on-file layer | `[Checkout]` | [dominos.com.tr/kurumsal/online-odeme](https://www.dominos.com.tr/kurumsal/online-odeme) |
| 🇮🇳 India (in-store) | Own Android POS, **"Elate"**, built in-house | `[Press]` | [CIO.inc](https://www.cio.inc/from-pizza-to-ai-how-jfl-baking-tech-into-every-bite-a-27889) |

**Card tokenization:** their own vault, via `/saved-card-service/ve4/card(s)`, with `/data-security-sentinel/ve1/inbound/redact/unified-payments-cards-input-route` doing field redaction and an RSA `sentinelPubKey` for client-side encryption. Token records carry `panUniqueId`, `cardSuffix`, `network`, `issuer` and **`gateway`** — the RBI card-on-file-compliant shape (no raw PAN), but **gateway-scoped**. Saved-card UX includes **CVV re-entry** (`savedCardCvv`, 36 refs) and a delete flow. BIN lookup is their own: `/cart-service/ve2/cart/$cartId/bin/$cardInitialDigits`.

### 3B. Payment Orchestrator

**Classification: 🛑 IN-HOUSE ORCHESTRATION LAYER.** Evidence table is in Section 1 above. Summary of the decisive artefacts:

```
com.jubl.food.unifiedpayment.entity.TokenDetails     ← their own Java class, in shipped JS
sentinelClientId: "unifiedpayments-prod-pwa"          ← their own service client
unifiedPaymentResponse.nextActions                    ← their API drives the client
/jfl-payment-aggregator/ve1/payment/transaction-status
/data-security-sentinel/ve1/inbound/redact/unified-payments-cards-input-route
UNIFIED_PAYMENT: "UNIFIED_PAYMENT_ACTION"
```

> *"The merchant has built its own payment orchestration layer. Every gateway is integrated as a bespoke branch in a hand-written dispatch, each with its own handoff shape — `initiateHtml` for one, `postFormData(globalpayUrl, globalpayPayload)` for another, an SDK hash for a third. This is the hardest motion in the matrix: never argue that they need orchestration. Argue reach, reconciliation and the engineering cost of the next gateway."*

**"Sentinel" is theirs, not a vendor.** No third-party product of that name exists in Indian payment tokenization or card encryption. The near-homonym **"Centinel"** (CardinalCommerce 3-D Secure MPI, `centinelapi.cardinalcommerce.com`) is a different spelling and different function — a spelling trap, not the answer. Their own URL path `/data-security-sentinel/…/unified-payments-cards-input-route` settles it internally.

**No external vendor claims them.** Checked: Juspay, Razorpay Optimizer, PayU Switch, Cashfree, Zecpay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno. Zero hits.

**PCI scope:** `[INFERENCE, not confirmed]` — given a self-hosted redaction proxy and an RSA client-encryption key, card data very likely enters **their** environment rather than a PSP iframe, which implies a **wider** PCI scope than a hosted-field merchant. That makes PCI-scope reduction a legitimate secondary angle. **Not verified** — treat as a discovery question, not a claim.

> **MANUAL:** Walk a real cart to the payment step on each of `m.dominos.co.in`, `m.dominoslk.com` and `m.dominos.com.bd` with DevTools open. That is the only way to get the live per-country method list and to see which host `globalpayUrl` resolves to.

## Section 4: Alternative & Local Payment Methods

| Country | Method | Category | Status | Source |
|---|---|---|---|---|
| 🇮🇳 India | UPI — QR | Bank transfer / A2A | **Active in checkout** (`QRCODE_UPI_WALLET`, sort 17) | `[Checkout]` server-rendered `module-data` |
| 🇮🇳 India | UPI — intent (PhonePe, Amazon UPI, generic) | A2A | **Active in code** (`PHONEPE_UPI_WALLET`, `AMAZON_UPI_WALLET`, `UPI_WALLET`) | `[Source Code]` |
| 🇮🇳 India | Credit / debit cards — Visa, Mastercard, Amex, Maestro, RuPay, Diners | Cards | **Active in checkout** (`CC`, `DC`, sort 19–20) | `[Checkout]` |
| 🇮🇳 India | Netbanking — ~45 banks (SBI, HDFC, ICICI, Axis, Kotak, IDFC, PNB, Canara, BOI, BOM, UCO, UBI, CBI, …) | Bank transfer | **Active in checkout** (`NB`, sort 22, 3 visible) | `[Checkout]` + `[Source Code]` |
| 🇮🇳 India | Paytm Wallet | Digital wallet | **Active in code** | `[Source Code]` |
| 🇮🇳 India | Amazon Pay wallet | Digital wallet | **Active in code** (`AMZPAY_WALLET`) | `[Source Code]` |
| 🇮🇳 India | Stored value — internally `PIGGYBANK` | Prepaid / closed-loop | **Active** (`IS_WALLET_BLOCKED: false`) | `[Source Code]` |
| 🇮🇳 India | E-voucher / gift card | Cash/voucher | **Active in checkout** (`EVOUCHER`, sort 21) | `[Checkout]` + [gift-vouchers page](https://www.dominos.co.in/gift-vouchers) |
| 🇮🇳 India | Cash on delivery | Cash | **Active in checkout** (`CASH`, sort 23) | `[Checkout]` |
| 🇮🇳 India | **Meal / benefit cards (Pluxee, Sodexo, Zeta, Ticket Restaurant)** | Prepaid benefit | **❌ NOT FOUND — no code path in the bundle** | `[Source Code]` absence |
| 🇮🇳 India | EMI / instalments | BNPL/Instalments | **❌ Not found — zero whole-word hits.** *Correctly absent: ticket values are ₹-hundreds.* | `[Source Code]` absence |
| 🇧🇩 Bangladesh | bKash | Mobile financial service | **In code** (`BKASH_MB`, dedicated `bKashModule` component) | `[Source Code]` |
| 🇧🇩 Bangladesh | Rocket (Dutch-Bangla) | MFS | **In code** (`DBBL_MB`) | `[Source Code]` |
| 🇧🇩 Bangladesh | AB Bank Direct | MFS | **In code** (`ABDIRECT_MB`) | `[Source Code]` |
| 🇧🇩 Bangladesh | upay · iPay | Digital wallet | **In code** (`UPAY_WALLET`, `IPAY_WALLET`) | `[Source Code]` |
| 🇧🇩 Bangladesh | Netbanking — Islami Bank, City Touch, Bank Asia, Mutual Trust | Bank transfer | **In code** (`IBBL_NB`, `CITYTOUCH_NB`, `BANKASIA_NB`, `MTBL_NB`) | `[Source Code]` |
| 🇧🇩 Bangladesh | FastCash · QCash cards | Cards | **In code** | `[Source Code]` |
| 🇧🇩 Bangladesh | **Nagad** | MFS | **❌ No code path in the bundle.** ⚠️ Read the caveat below | `[Source Code]` absence |
| 🇱🇰 Sri Lanka | Cards — Visa, Mastercard, Amex, Discover, Diners | Cards | **In code** (`CARDS_SL` = `CARD`) | `[Source Code]` |
| 🇱🇰 Sri Lanka | Genie (Dialog Axiata) · FriMi (**Nations Trust Bank**) | Digital wallet | **In code** — `jfi-bankicon-genie`, `jfi-bankicon-frimi` in the "We Accept" row | `[Source Code]` |
| 🇱🇰 Sri Lanka | **Card-on-file / saved cards** | Cards | **❌ No tokenization service configured** — `sentinelClientId` is India-only | `[Source Code]` absence |
| 🇱🇰 Sri Lanka | In-app stored value | Prepaid | **❌ Explicitly blocked** — `IS_WALLET_BLOCKED: true` | `[Source Code]` |
| 🇱🇰 Sri Lanka | LankaQR · eZ Cash · mCash | A2A / wallet | **❌ No code path.** *Likely rational — see below* | `[Source Code]` absence |
| 🇹🇷 Türkiye | Masterpass · direct card · Domino's Cüzdan · meal voucher · cash | Mixed | **Active in checkout** | `[Checkout]` [online-odeme](https://www.dominos.com.tr/kurumsal/online-odeme) |

### The three absences, honestly rated

**1. 🇮🇳 Meal/benefit cards — the strongest, and it is a revenue-leakage argument.**
**Pluxee's own help centre** names its **online** acceptance as Swiggy, Zomato, BigBasket, Zepto, JioMart and Blinkit, and displays **Pizza Hut** among example brands. **Domino's is named nowhere on that page** (fetched by me, 2026-10-05). So a corporate employee holding a meal-card balance can buy a pizza **through Zomato or Swiggy** — on which Jubilant pays aggregator commission — but there is no meal-card path in Domino's own app. **Captive, employer-funded food spend is being routed to the channel that costs Jubilant the most.**
⚠️ **Frame strictly as online/app absence.** Meal cards ride RuPay/Visa prepaid rails, so they very likely work on in-store POS. Claiming "Domino's doesn't take Pluxee" would be wrong and would lose the room. Zeta and Ticket Restaurant/Edenred positions were **not researched**.

**2. 🇱🇰 Sri Lanka card-on-file — strong, and it is an in-stack asymmetry.**
Not a rails gap — a **capability gap in the fastest-growing market in the group.** Sri Lanka grew **+65.9% YoY** in Q3 FY26 against India standalone's +11.8%, and runs the byte-identical payment bundle with the tokenization service unconfigured and the wallet switched off. With cards at **35%** of Sri Lankan online retail payment, no saved-card path means every repeat buyer re-enters a PAN.

**3. 🇧🇩 Nagad — demote to a probing question. Do not lead with it.**
Nagad is a real **#2**: **28.2m active users** vs bKash's 42.0m, and a Q1 2025 record of **Tk 111,355 crore** in transactions, +21% YoY ([The Daily Star, 16 Jul 2026](https://www.thedailystar.net/business/news/tk-6000cr-moves-daily-not-every-wallet-winning-4220811)).
**But the same article states Nagad "expanded rapidly despite never obtaining a full licence from Bangladesh Bank," and it is run by a Bangladesh Bank-appointed administrator** — upheld by the Appellate Division in June 2025. A payments lead can close this in one line: *"Nagad has never held a full licence and is under central-bank administration; we chose not to integrate it."* **Lead Bangladesh on the overhead of maintaining ~11 local rails through a hand-written dispatch, not on one missing wallet.**

**And one angle to drop outright: Sri Lankan wallets.** **E-wallets are ≤1% of Sri Lankan online retail payment; COD is 52% and rising; cards 35% and falling** ([Daily Mirror / APIDM–Kelaniya](https://www.dailymirror.lk/print/business-news/Sri-Lankan-online-shoppers-stick-to-cash-on-delivery-amid-digital-payment-hesitation/273-307888)). The thin Sri Lankan method list is pointed at where the money actually is. Pitching missing wallets there would be wrong on the market data.

⚠️ A **possible** cost angle, unverified: Sri Lanka's National QR Payment Adoption Programme reportedly **removed MDR entirely on LankaQR transactions up to Rs 5,000, effective 6 April 2026** — comfortably above a Domino's LK ticket. **Verify the CBSL circular before using.** No e-commerce/CNP **mandate** was found (absence of evidence, not evidence of absence).

> **MANUAL:** VPN into each of the three markets and walk a cart to the payment step. The enabled list comes from the authenticated API, not the bundle.

## Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| **Payment succeeded, order never created** — ₹414.28 **debited twice**, BHIM UPI via HDFC UPI RuPay credit card | consumercomplaints.in | — | **31 Jul 2026** | [link](https://www.consumercomplaints.in/dominos-pizza-payment-deducted-twice-but-orders-not-placed-and-not-showing-in-order-history-c3543705) |
| **Payment succeeded, order never created** — ₹865.20, PhonePe | consumercomplaints.in | — | **27 Jan 2026** | [link](https://www.consumercomplaints.in/dominos-pizza-dominos-pizza-payment-successful-in-phonepay-to-dominos-but-failed-to-place-order-n-dominos-application-need-refund-c3539039) |
| **Payment succeeded, order never created** — ₹461, Paytm | consumercomplaints.in | — | **27 Dec 2025** | [link](https://www.consumercomplaints.in/dominos-pizza-payment-successful-but-order-not-created-in-dominos-pizza-app-in-outlet-461-rs-has-been-deducted-c3538320) |
| **Double debit** — ₹217 ×2 for one order, Paytm | consumercomplaints.in | — | **23 May 2025** | [link](https://www.consumercomplaints.in/dominos-pizza-charges-debited-twice-for-single-order-no-customer-support-c3529299) |
| Brand-level backlog: **6,604 complaints, 727 resolved, 5,877 unresolved** (~11% resolution) | consumercomplaints.in | **High** | page 1 spans 27 Oct 2025 → 14 Sep 2026 | [brand page](https://www.consumercomplaints.in/dominos-pizza-b100147) (fetched, HTTP 200) |
| **Same symptom, Sri Lanka** — "They deduct you money and then say the order was failed!!" (Domino's Nugegoda, Colombo) | TripAdvisor | Isolated (1 review) | undated | [link](https://www.tripadvisor.in/ShowUserReviews-g3181345-d8002456-r940870440-Domino_s_Pizza-Nugegoda_Western_Province.html) — title from search result, body not fetched |
| Low ratings, top issue tags **delivery / refund / cancellation** — 766 reviews, avg **1.4/5** | PissedConsumer (India subdomain) | Moderate | — | [link](https://dominos-pizza-india.pissedconsumer.com/review.html) `[UNVERIFIED — search summary only]` |
| Stated refund SLA **7 working days**, reportedly breached | X / consumercomplaints.in | — | policy tweet 2018 | [link](https://x.com/dominos_india/status/1017641188524941318) — policy only, not current evidence |

> **Pattern — and it is the core of this account.** The identical symptom recurs across **BHIM UPI, UPI-on-RuPay-credit, PhonePe and Paytm** over **14 months**, with two double debits. **A fault that reproduces on every rail is not a PSP fault.** It is the merchant's own payment-success-to-order-creation handoff — callback consumption, reconciliation and idempotency. The double debits specifically indicate a retry against an unreconciled transaction.
>
> **The Yuno mapping is unusually direct:** an orchestration layer owns webhook/callback consumption, transaction-status reconciliation and idempotent retry as product behaviour, instead of each of seven gateways' callbacks being handled in bespoke merchant code. Their own `/jfl-payment-aggregator/ve1/payment/transaction-status` and `/payment-service/ve1/orders/$transactionId/otp` endpoints are exactly the surface where this is being carried by hand.

**Not found / explicitly negative:**
- **Popeyes India and Dunkin' India — no pattern found.** Searches returned almost entirely Popeyes US (BBB Atlanta) and Dunkin' US. Read as under-reported, **not** as clean.
- **Bangladesh — nothing found.** No pattern claimed.
- **Google Play review extraction failed.** The fetch returned truncated content with no reviews. **Nothing is reported from it.** The documented similar-apps-carousel trap therefore never arose. An aggregator blog titled "Domino's App Deals Not Working: 462 Reviews (2026)" was found and **deliberately not used** — no market attribution, almost certainly mixes Domino's US.
- ⚠️ **Quarantined, not used:** every `updownradar` / "Is Domino's app down?" artefact for Apr–Aug 2026 reports outages timed in **Eastern Time** against `dominos.com` — that is **Domino's Pizza Inc (US)**. Trustpilot returned `dominos.co.uk`. MoneySavingExpert returned UK. **None of this is Jubilant.** Listed here so nobody downstream reuses it.
- **No India-attributable payment outage was confirmed.** Treat as unknown, not absent.

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | **18 Sep 2026** | ⭐ **CIO Narottam Sharma resigned**, "to take up an external opportunity." **No successor announced.** | Leadership Change | [IndianRetailer](https://www.indianretailer.com/news/narottam-sharma-steps-down-jubilant-foodworks-cio) · [BW People](https://www.bwpeople.in/article/jubilant-foodworks-cio-narottam-sharma-to-exit-company-in-september-616072) `[UNVERIFIED]` |
| 2 | **~31 Mar / 1 Apr 2026** | ⭐ **Domino's master franchise renewed: 15 years + 10-year option**, India / Sri Lanka / Bangladesh | Franchise Renewal | [Business Standard](https://www.business-standard.com/companies/news/jubilant-foodworks-renews-dominos-franchise-for-15-years-126040101142_1.html) `[UNVERIFIED]` |
| 3 | **2026** | **Exiting Dunkin' India** — pact ends **31 Dec 2026**, not being renewed | Brand Exit | [BusinessWorld](https://www.businessworld.in/article/jubilant-foodworks-to-exit-dunkin-india-partnership-as-pact-ends-in-2026-599993) `[UNVERIFIED]` |
| 4 | **Jun 2026** (Q4 FY26) | **GenAI chatbot** on the Domino's app handling complaints and **issuing coupons autonomously** (₹150 shown); plus **Location AI** and a **Popeyes 2.0 app** | Tech / Product | [medianama](https://www.medianama.com/2026/06/223-jubilant-foodworks-q4fy26-genai-chatbot-delivery-growth/) `[UNVERIFIED]` |
| 5 | **Feb 2026** (Q3 FY26) | Domino's app turned into an **ad platform** — post-order placements sold to 10+ brands incl. Apple, Toyota, Airtel, Amazon Fresh; target ~1% of company revenue | Monetisation | [medianama](https://www.medianama.com/2026/02/223-jubilant-foodworks-dominos-app-ad-platform-q3fy26-earnings-call/) `[UNVERIFIED]` |
| 6 | **1 Apr 2025** | **In-house tech build made explicit** — 250-member team, "legacy outsourced → proprietary solutions", 100+ microservices, own Android POS **Elate**, 55% D2C orders | Tech Strategy | [CIO.inc](https://www.cio.inc/from-pizza-to-ai-how-jfl-baking-tech-into-every-bite-a-27889) **fetched** |
| 7 | **Jan 2024** | DP Eurasia stake raised to **94.28%** (from 49.04%) for ₹11.99bn, then delisted | M&A | [IIFL](https://www.indiainfoline.com/blog/jubilant-foodworks-dp-eurasia-acquisition-leveraging-the-india-playbook) `[UNVERIFIED]` |
| 8 | **24 Mar 2021 → today** | Popeyes rights cover **India, Bangladesh, Nepal, Bhutan** — **only India has opened.** Nepal/Bhutan/Bangladesh rights held, unexercised for 5+ years | Expansion (dormant) | [Business Standard](https://www.business-standard.com/article/companies/jubilant-foodworks-to-bring-popeyes-to-india-bangladesh-nepal-bhutan-121032500395_1.html) · [Popeyes](https://news.popeyes.com/blog-posts/popeyes-r-announces-agreement-to-open-restaurants-across-india-bangladesh-nepal-and-bhutan) |

**Public payment RFP:** **No public payment-related RFP or tender found.** Nothing on GeM, nothing on their site, nothing in press.

**Payment job postings:** **None open.** No "Head of Payments" title exists. The nearest match was a **closed** Senior Software Engineer req (Noida/Greater Noida, 3–7 yrs, **Java / Microservices / Spring / Hibernate**) — consistent with the `com.jubl.food…` class, but a closed req scores nothing. Reported stack from third-party technographics `[UNVERIFIED]`: Java, microservices, NoSQL, **Aerospike**, RabbitMQ, Amazon EKS, AWS Lambda.

**Licence applications:** **None found.** No RBI Payment Aggregator, no PPI authorisation, nothing in Bangladesh or Sri Lanka. **This negative is well-supported:** their gift-card product is unambiguously **closed-loop** — issued by Jubilant FoodWorks Ltd, redeemable only "at all participating Domino's Restaurants in India," physical card ₹500–₹49,999 reloadable, e-voucher ₹100–₹3,000 single-use, **with no mention of RBI, PPI, a bank partner or escrow** ([gift-vouchers page](https://www.dominos.co.in/gift-vouchers)). A closed-system PPI redeemable only at the issuer's own outlets sits outside PPI authorisation. ⚠️ RBI has a **draft Master Direction on PPIs, 2026** in flight that could change the treatment of gift cards and vouchers — worth monitoring.
*Not relevant: their C2FO supply-chain early-payment programme ([jfl.c2fo.com](https://jfl.c2fo.com/)) is vendor financing / accounts-payable, not consumer payments.*

## Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | **20 Jan 2025** | ⛔ **Razorpay and Cashfree step back from third-party payment orchestration and routing platforms as a category.** Razorpay: "pause all integrations through third-party routing platforms." | **Direct blocker — Razorpay is one of Jubilant's seven gateways.** See the box at the top of this file. | [Entrackr](https://entrackr.com/news/after-phonepe-razorpay-and-cashfree-suspend-direct-integrations-with-juspay-8638638) **fetched** |
| 2 | **Dec 2024** | PhonePe severed ties with third-party routing first | Same theme — the Indian PSP posture toward orchestrators is hardening | [Inc42](https://inc42.com/buzz/razorpay-cashfree-to-discontinue-partnership-with-juspay/) `[UNVERIFIED]` |
| 3 | **~Mar 2025** | Indian payment aggregators publicly called for a break from third-party routing | Context for how a Yuno pitch will be received in India | [Business Standard](https://www.business-standard.com/industry/news/payment-aggregators-call-for-break-from-juspay-s-third-party-routing-125033000575_1.html) `[UNVERIFIED]` |
| 4 | **Jun 2026** | GenAI chatbot issuing refund coupons autonomously on the Domino's app | The cost of the Section 5 failure pattern, automated | [medianama](https://www.medianama.com/2026/06/223-jubilant-foodworks-q4fy26-genai-chatbot-delivery-growth/) `[UNVERIFIED]` |
| 5 | **May 2011** | Domino's India trialled card-on-delivery powered by **PayMate** | 15 years stale — colour only, do not use | [Business Standard](https://www.business-standard.com/amp/article/press-releases/no-cash-no-problem-domino-8217s-now-accepts-credit-card-for-delivery-111050500126_1.html) |

**No PSP addition or removal announced in the last 24 months.** Four search angles returned nothing: no Razorpay / PayU / Juspay / Cashfree / BillDesk / CCAvenue announcement tied to Jubilant exists in public press. **Jubilant does not publicise its payment stack at all** — which is exactly why the code was the only way to get it, and why this file is worth more than a press sweep.

**No provider REMOVAL found.**

## Section 8: Checkout Experience Audit

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | **Custom-built, self-hosted.** Micro-frontend `jfl-discovery-payment`, served from the merchant's own domain in all three countries | Good | No third-party hosted-checkout domain anywhere in the bootstrap |
| Payment front-end sharing | **`payment.js` byte-identical across IN/LK/BD** — md5 `43acb80254b091185f8311b251342947`, 1,825,175 bytes | — | One codebase; three separate backends (`api.dominos.co.in`, `apis.dominoslk.com`, `api.dominos.com.bd`) |
| Guest checkout | **Unresolved — do NOT claim it exists.** Config shows `homeGuestMenuCategory:"menu-v2"`, `shouldHideCompleteLoginFlow:"true"`, `shouldLoginFlowSkip:"true"` on all three sites, and `loginPgUrl:"/postorder-ui/login"` suggests login sits around/after order placement | — | A guest **menu** is not guest **checkout**. Whether phone/OTP is mandatory before payment could not be determined |
| Steps cart → payment | **Not determinable** without driving the SPA | — | |
| Card input experience | Own fields, client-side RSA encryption via `sentinelPubKey`, redaction proxy at `/data-security-sentinel/…` | Fair | Implies card data enters their environment — wider PCI scope than hosted fields |
| Payment methods visible | **India live-verified** (7 top-level groups, sort 17–23). **LK/BD code-inferred only** | — | Nested items (which UPI app, which bank) load from the authenticated API |
| Location-based method display | **Yes — by country, confirmed.** Tenant key, currency, wallet availability and tokenization service all vary by country | Good | India `D6M9I3N2O1S3`; SL `…SL`; BD `…BD` |
| Instalment / EMI | **None. Zero whole-word hits.** Correct for a ₹-hundreds ticket | Good | Contrast: the Türkiye estate sits in a market where **taksit** is embedded in checkout behaviour |
| 3DS implementation | **Not detected in the client bundle** | — | Almost certainly handled gateway-side on redirect; not a finding either way |
| PCI indicator | Self-hosted card fields + own redaction service, **not** a PSP iframe | — | FY2019-20 annual report reportedly names ISO 27001, NIST, PCI-DSS — **PDF 403, unread** |
| Mobile responsiveness | Mobile-first by construction — `m.` subdomains are the primary ordering surface | Good | App-first merchant; 55% of orders from own apps |
| Multi-currency | Per-country: INR `₹` / LKR `Rs.` / BD `৳`. ⚠️ Live BD config serves `CURRENCY_CODE: "Tk"` where the bundle module says `BDT`; their internal country key for Bangladesh is **`BG`**, not ISO `BD` | Fair | Internal-naming choices rather than proven bugs — but worth knowing, and they prove the research is real |
| Saved payment methods | **India only.** `savedCardCvv` (36 refs), delete-card flow, `/saved-card-service/ve4/cards`, plus `/payment-service/veN/payment/options/lastSuccessful` and `/payment-service/ve5/recommendedOptions` | Good in India, **absent in LK/BD** | The clearest in-stack asymmetry on this account |
| Error message clarity | `internalServerError: "Something Went Wrong. Please Try Again."` | **Poor** | A generic string on the payment path — and Section 5 shows what sits behind it |

**Extra observations from the bundle, worth recording:**
- **Mini-app surfaces, India only:** distinct client builds and distinct analytics streams for **Paytm Mini-App** (`PAYTM_CLIENT_TYPE: "web app-paytm"`) and **Google Pay** (`GPAY_CLIENT_TYPE: "web app-gpay"`), with `miniAppExitError` strings. So India has **at least three order-entry surfaces** on top of the app and web.
- **API version sprawl:** ve1–ve6 all referenced in one shipped bundle (179 / 76 / 79 / 42 / 5 / 1).
- **Their API is properly secured** — 401/403 on every unauthenticated payment endpoint across all three hosts.
- A hardcoded `pwa.jfl@gmail.com` appears in the production bundle. **Noted, not weaponised** — it has no place in outreach.

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **Not found.** No level published | — |
| Framework claim | FY2019-20 annual report reportedly names **ISO 27001, NIST and PCI-DSS** as frameworks followed | [JFL AR FY2019-20](https://www.jubilantfoodworks.com/Uploads/Files/140akmfile-JFLAnnualReportFY2019-20.pdf) — ⚠️ **HTTP 403, never read.** `[UNVERIFIED — search summary only]` |
| Card data handling | **Likely full PCI scope, not SAQ A.** Own card fields + own RSA client-side encryption + own redaction proxy + own token vault | `[Source Code]` |
| RBI card-on-file tokenization | **No public statement found.** Their token shape is the compliant one — `panUniqueId`, `cardSuffix`, `network`, `issuer`, gateway/network token, **no raw PAN** | `[Source Code]` |
| Recommended Yuno integration | **Back-to-back API** — they already own the card-capture surface and will not want to give it up. An SDK/hosted-fields path is the secondary pitch, as PCI-scope reduction |

**No direct PCI compliance documentation was read for Jubilant FoodWorks.** The framework claim rests on a search summary of a PDF that returned 403.

## Section 10: Strategic Insights & Outreach Angles

> ### Insight #1: The failure crosses every rail, so it is not a gateway problem
> **Evidence:** Section 5 — the same "payment succeeded, order never created" symptom on **BHIM UPI, UPI-on-RuPay-credit, PhonePe and Paytm**, dated 23 May 2025 → 31 Jul 2026, two double debits, 5,877 unresolved complaints + Section 3B — a hand-written per-gateway dispatch with seven bespoke `case` branches and their own `/jfl-payment-aggregator/ve1/payment/transaction-status`.
> **Pain Point:** Every gateway's callback, status-poll and retry semantics is handled in merchant code. Seven gateways means seven reconciliation contracts to get right, and the complaint record says at least one is not holding. Each failure is a lost order **plus** a refund cycle **plus** (now) an automated goodwill coupon.
> **Yuno Value Proposition:** Callback consumption, transaction-status reconciliation and idempotent retry become platform behaviour rather than per-gateway code. One status contract instead of seven.
> **Best Success Case:** Tier 2 — a merchant running an in-house layer across many PSPs where the win was reconciliation, not "you need orchestration."
> **Outreach Angle:** The observation is that the symptom is identical on four different rails — which rules out any one provider. Ask it as a question; never assert their architecture is broken.
> **Suggested Subject Line:** "Same failure on four rails"

> ### Insight #2: Saved cards stop at the gateway that created them
> **Evidence:** Section 3A — the token fixture carries `"gateway":"RAZORPAY"` as a field on the token + Section 3B — four Indian gateways live in parallel (PayU, Paytm PG, BillDesk, Razorpay).
> **Pain Point:** Routing freedom and card-on-file are in direct conflict. Any attempt to route a returning customer to a better-performing acquirer costs that customer their saved card — so in practice the repeat buyer is pinned to whichever gateway tokenized them first. The four-gateway investment cannot be used where it would pay most: the highest-intent, highest-frequency customers.
> **Yuno Value Proposition:** A gateway-agnostic vault and network tokens decouple the stored credential from the processor, so routing decisions and saved-card UX stop trading off against each other.
> **Best Success Case:** Tier 2.
> **Outreach Angle:** Their own token record names the gateway. That is a structural property, not a mistake — and it is the cleanest thing to open on with a team that built the vault themselves.
> **Suggested Subject Line:** "Your saved cards are gateway-bound"

> ### Insight #3: The fastest-growing market runs the thinnest configuration
> **Evidence:** Section 8 — `payment.js` is byte-identical across IN/LK/BD (md5 verified), yet `sentinelClientId` is India-only and `IS_WALLET_BLOCKED` is true only in Sri Lanka + Agent-1 financials — Q3 FY26 revenue growth **Sri Lanka +65.9%**, Bangladesh +26.6%, India standalone +11.8%.
> **Pain Point:** The same code ships everywhere, but the payment *capability* was configured for India. Sri Lanka has no card-on-file in a market where cards are 35% of online retail payment, and no stored value at all. The market compounding fastest is the one running on the least.
> **Yuno Value Proposition:** Capability parity across markets from one integration — tokenization, stored credentials and local rails configured per market without a per-market build.
> **Best Success Case:** Tier 2.
> **Outreach Angle:** This is an asymmetry **inside their own stack** — the strongest kind, because they cannot dispute either half. And it is not criticism: the India-first sequencing was rational, the growth numbers just moved.
> **Suggested Subject Line:** "Sri Lanka +65.9% on the thinnest config"

> ### Insight #4: Employer-funded food spend is routed to the aggregator
> **Evidence:** Section 4 — no meal/benefit-card code path in the bundle + Pluxee's own help centre naming **Swiggy and Zomato** as online acceptance and displaying **Pizza Hut**, with **Domino's absent** (fetched by me) + Section 1 — only ~55% of orders are own-channel, so aggregator commission is a live cost line.
> **Pain Point:** A corporate employee with a meal-card balance **can** buy a Domino's pizza — through Zomato or Swiggy, on which Jubilant pays commission. The same customer cannot pay that way in Domino's own app. This is not a coverage gap; it is own-channel revenue being pushed to the most expensive channel by a missing payment method.
> **Yuno Value Proposition:** Add the benefit-card rail to the owned checkout through the existing integration rather than a new per-provider build.
> **Best Success Case:** Tier 1 if a QSR/delivery reference with published metrics exists; Tier 3 otherwise.
> **Outreach Angle:** Strongest commercial argument in the file because it converts a payment gap into a channel-mix cost. ⚠️ Must be framed as **online/app** absence only — POS almost certainly accepts these cards on the prepaid rails.
> **Suggested Subject Line:** "Meal cards work on Zomato, not your app"

> ### Insight #5: Five estates, seven gateways, no payments owner — and the CIO seat is empty
> **Evidence:** My own probing — five separate digital estates (Domino's IN/LK/BD on `jfl-discovery-*`; **Hong's Kitchen on the same codebase but `hongs-prod.hongskitchen.in`**; **Popeyes India on `api.popeyes.in`, a different platform**; **Türkiye on `cdn.dpeurasia.com`** with Masterpass for card-on-file) + Section 6 — **CIO resigned 18 Sep 2026, no successor**, no Head of Payments title, and a **15-year Domino's renewal** across exactly the three markets sharing one codebase.
> **Pain Point:** The marginal cost of the next gateway, the next brand and the next market is paid in engineering time against a 250-person team that also owns the app, the POS, Location AI and an ad platform. Seven gateways, ve1–ve6 in flight, and three per-country backends is the accumulated form of that cost.
> **Yuno Value Proposition:** One integration spanning brands and markets; new gateways and rails become configuration. **Additive — it sits above what they built.**
> **Best Success Case:** Tier 2.
> **Outreach Angle:** The 15-year renewal is the legitimate reason to raise infrastructure now. **Respect the build** — the argument is opportunity cost, never that the build was wrong.
> **Suggested Subject Line:** "Seven gateways, five estates, one team"

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks**
1. The same "payment taken, order never created" complaint shows up on BHIM UPI, UPI-on-RuPay-credit, PhonePe and Paytm between May 2025 and July 2026 — four different rails, one symptom, which points past any single provider.
2. Your saved-card records carry the gateway as a field on the token, so routing a returning customer to a different acquirer costs them their saved card.
3. Sri Lanka grew 65.9% last quarter against India's 11.8%, and runs the identical payment bundle with no card-on-file service configured.
4. A Pluxee meal-card holder can buy a Domino's pizza through Zomato but not in the Domino's app — and Pizza Hut is on Pluxee's own brand page.

**Cold call openers**
1. "I went through your payment flow across India, Sri Lanka and Bangladesh — it's the same build in all three, but the card-on-file service is only switched on in India. Was that deliberate sequencing?"
2. "Quick one — when you route a repeat customer to a different gateway, do they keep their saved card?"
3. "You've renewed Domino's for fifteen years across three markets, the CIO seat is open, and payments sits across seven gateways. Who owns that roadmap right now?"

## Section 11: Similar Companies & Prospecting Pipeline

### 11A. Direct Competitors

| Company | Website | HQ | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|----|-----------|-----------------|------------------------|--------|
| **Devyani International** (DEVYANI) | devyani-intl.com | India | 2,039 stores; ₹5,611.5 Cr | India, Nepal, Thailand, Nigeria | **Not found** | [scanx](https://scanx.trade/stock-market-news/companies/devyani-international-annual-report-fy-2025-26-revenue-at-56-115-million-merger-with-sapphire-foods-announced/46374246) |
| **Sapphire Foods India** (SAPPHIRE) | sapphirefoods.in | India | ~909 stores; ₹2,919.1 Cr | India, **Sri Lanka**, Maldives | **Not found** | [indmoney](https://www.indmoney.com/blog/stocks/sapphire-foods-devyani-merger) |
| **Westlife Foodworld** (WESTLIFE) | westlife.co.in | India | 438 stores; ₹2,491 Cr | India (W/S only) | ⚠️ **"McDonald's" is a named Juspay orchestration customer — market/entity NOT stated** | [Juspay](https://juspay.io/customer-stories/mcdonalds) **fetched** |
| **Restaurant Brands Asia** (RBA) | rbasia.in | India | ~₹2,800 Cr annualised (my arithmetic) | India, Indonesia | ⚠️ **"Burger King" on Juspay's India logo wall — entity NOT stated** | [Juspay](https://juspay.io/in) **fetched** |
| **Rebel Foods** | rebelfoods.com | India | 450+ kitchens; ₹1,951.6 Cr FY26 | India, MENA, Indonesia, UK | **Not found** | [inc42](https://inc42.com/features/rebel-foods-in-2025-cloud-kitchen-giant-simmers-down-before-ipo-push/) |
| **Barbeque Nation** | barbequenation.com | India | ~200 outlets; ₹1,220 Cr | India + intl | **Not found** | [Wikipedia](https://en.wikipedia.org/wiki/Barbeque_Nation) |
| **Wow! Momo** | wowmomo.in | India | 850+ outlets | India | **Razorpay POS** — 600+ devices, **in-store not online** | [Razorpay](https://razorpay.com/blog/wow-momo-and-razorpay/) `[UNVERIFIED]` |

### 11B. Industry Peers / Channels

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| **Swiggy** | swiggy.com | Food aggregator | India | **Confirmed on orchestration** with real-time PSP routing; named exec quote. **Jubilant's own sales channel** | [Juspay](https://juspay.io/customer-stories/swiggy) **fetched** |
| **Zomato / Eternal** | zomato.com | Food aggregator | India | Jubilant's other channel. **No orchestration evidence found** | — |
| **PickMe Food** | pickme.lk | Food delivery | Sri Lanka | 4,000+ merchants; COD with merchant-set caps — the SL channel benchmark | [pickme.lk](https://pickme.lk/services/food/) |
| **Pizza Hut India** | pizzahut.co.in | QSR — direct pizza rival | India, Sri Lanka | **On Pluxee's brand display where Domino's is absent** | [Pluxee](https://www.pluxee.in/helpcenter/consumer/where-can-i-use-pluxee-card/) **fetched** |
| **Yemeksepeti** | yemeksepeti.com | Food aggregator | Türkiye | 79.1% brand awareness; carries Domino's TR | [Wikipedia](https://en.wikipedia.org/wiki/Yemeksepeti) `[UNVERIFIED]` |

### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| **Swiggy** | Juspay (Express Checkout — orchestration + real-time PSP routing) | not dated | Food aggregator | [link](https://juspay.io/customer-stories/swiggy) **fetched** |
| **McDonald's** ⚠️ market/entity unstated | Juspay (Payment Orchestration, dynamic real-time PSP routing) | not dated | QSR | [link](https://juspay.io/customer-stories/mcdonalds) **fetched** |
| **Burger King** ⚠️ market/entity unstated | Juspay (logo wall only) | not dated | QSR | [link](https://juspay.io/in) **fetched** |

**⚠️ Attribution limit, stated plainly:** the ideal finding — *"Indian QSR peer X is live on orchestrator Y per X's own disclosure"* — **was not achieved.** Neither Juspay case study names a country, an operating entity, a single PSP, or any quantified metric; both are entirely qualitative (verified by direct fetch). **Outreach must not state that Westlife Foodworld or Restaurant Brands Asia uses an orchestrator.** The defensible version is brand-level and curiosity-framed.

**Notable absence:** Domino's, Jubilant, KFC, Pizza Hut, Devyani, Sapphire, Westlife, Zomato, Rebel Foods, Wow! Momo, Barbeque Nation and Subway are all **absent** from that vendor's India logo wall. Absence from one vendor's marketing is **not** proof of anything — a discovery probe, not a fact.

**No Indian QSR payment-orchestration vertical case study exists in public, from any vendor.** Searched explicitly.

### 11D. Prospect Scoring — top finds

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| **Devyani International + Sapphire Foods (merging)** | **Est. 17–20 ⭐** | 3,002 stores, ₹7,826.5 Cr pro-forma FY25, India + **Sri Lanka** + Maldives + Thailand + Nepal + Nigeria. **A US$934m merger forces consolidation of two payment stacks across six countries** — regulatory approval 12–15 months, integration 15–18 months. Devyani explicitly cites unifying "**technology**". No PSP evidence found for either = likely greenfield or direct-integration. **This is the single best new prospect surfaced by this run.** | [CNBC](https://www.cnbc.com/2026/01/02/devyani-sapphire-merger-yum-brands-india-kfc-pizza-hut-taco-bell-dominos.html), [scanx](https://scanx.trade/stock-market-news/companies/devyani-international-annual-report-fy-2025-26-revenue-at-56-115-million-merger-with-sapphire-foods-announced/46374246) |
| **Rebel Foods** | Est. 12–15 🟢 | ₹1,951.6 Cr FY26, 450+ kitchens, **India + MENA + Indonesia + UK**, IPO-track. Genuinely multi-region, no PSP evidence found | [inc42](https://inc42.com/features/rebel-foods-in-2025-cloud-kitchen-giant-simmers-down-before-ipo-push/) |
| **Restaurant Brands Asia** | Est. 10–13 🟢 | **India + Indonesia** — a genuine two-country APAC footprint, i.e. QRIS exposure. Burger King on a logo wall, entity unconfirmed | [upstox](https://upstox.com/news/market-news/stocks/devyani-international-westlife-foodworld-qsr-stocks-zoom-up-to-10-6-what-you-need-to-know/article-179901/) |
| **Westlife Foodworld** | Est. 8–11 🟢/🔴 | India-only (west/south), 438 stores. **Single-market = structurally weak for orchestration.** Possibly already on an orchestrator | [Wikipedia](https://en.wikipedia.org/wiki/Westlife_Foodworld) |
| **PickMe (Sri Lanka)** | Not scored | SL super-app, 4,000+ food merchants. **Not on the TAL.** Worth a stub on its own merits | [pickme.lk](https://pickme.lk/services/food/) |

#### Top Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | **Devyani International** | Direct competitor | IN, NP, TH, NG | Est. 17–20 | **⭐ P1** | $934m merger → two payment stacks, six countries | ❌ **NOT on TAL — genuine find** |
| 2 | **Sapphire Foods India** | Direct competitor | IN, **LK**, MV | Est. 17–20 | **⭐ P1** | Same merger; Sri Lanka overlap with Jubilant | ❌ **NOT on TAL — genuine find** |
| 3 | **Rebel Foods** | Industry peer | IN, MENA, ID, UK | Est. 12–15 | 🟢 P2 | Four-region cloud kitchens, IPO-track | ❌ **NOT on TAL** |
| 4 | **Restaurant Brands Asia** | Direct competitor | IN, ID | Est. 10–13 | 🟢 P2 | Indonesia = QRIS/VA exposure | ❌ **NOT on TAL** |
| 5 | **PickMe** | Regional channel | LK | Not scored | 🟢 P3 | Sri Lankan super-app, 4,000+ merchants | ❌ **NOT on TAL** |
| 6 | **Westlife Foodworld** | Direct competitor | IN only | Est. 8–11 | 🔴 P3 | Single market; may already be orchestrated | ❌ **NOT on TAL** |
| — | **Domino's Pizza Malaysia** | Different franchisee | MY | — | P1 (existing) | Already a stub in `1-to-outreach/` — **a separate company (Dommal Food Services), not Jubilant.** Do not merge the two files | ✅ On TAL |

**⚠️ Jubilant FoodWorks itself is NOT on `accounts/apac-tal.csv`.** The only related row is **Domino's Pizza Malaysia** — a different master franchisee entirely. Both Jubilant and the five finds above should be added.

**No PSP/ICP conflict:** none of the companies above is a PSP or payment-infrastructure business. Juspay, Razorpay, Cashfree, PayU, SSLCommerz and PayHere appear here only as vendors or competitors, correctly — nothing routes to Partnerships.

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | **~US$986.8m** — ₹9,512.51 crore consolidated revenue from operations, FY26 (ended 31 Mar 2026), **+17.37% YoY** | FX USD/INR **96.4006** at 2026-10-05 00:02 UTC ([open.er-api.com](https://open.er-api.com/v6/latest/USD)). [kotakneo](https://www.kotakneo.com/financial-results/jubilant-foodworks-share-price-q4fy2025-26-results/), [univest](https://univest.in/blogs/jubilant-foodworks-q4-fy26-results) |
| ⚠️ Revenue conflict | ₹9,512.51 cr vs **₹9,544 cr** — almost certainly revenue-from-operations vs total income. **Unresolved** | [Wikipedia](https://en.wikipedia.org/wiki/Jubilant_FoodWorks) |
| Most recent quarter | **₹2,499.46 cr** (~US$259.3m) Q4 FY26, +19.3% YoY; PAT ₹79.79 cr; EBITDA ₹484.9 cr, margin 19.4% | [upstox](https://upstox.com/news/market-news/earnings/jubilant-foodworks-q4-results-net-profit-soars-66-yo-y-to-80-crore-revenue-up-19-dividend-recommended/article-194032/) |
| Group system sales | **₹28,020 mn** Q3 FY26, +16.3% YoY | [investywise](https://www.investywise.com/jubilant-foodworks-investor-presentation-for-q3fy26-results/) |
| GMV / GTV | **Not separately disclosed.** System sales above is the closest analogue | — |
| **Average Transaction Value** | **❌ NOT DISCLOSED.** Directionally, average bill values have **moderated** — free-delivery threshold cut to ₹99, targeted cashbacks, packaging charges zeroed in some markets | [Yahoo Finance](https://sg.finance.yahoo.com/news/indias-jubilant-foodworks-posts-higher-103350913.html), [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-jubilant-foodworks-q1-2026-sees-mixed-growth-popeyes-shines-93CH-4857777) |
| Est. Annual Transactions | **≥68.4 million** (5.7m MTU × 12, floor) | Derived — see below |
| **Monthly transaction count** | **✅ DERIVED (floor): ≥ 5,700,000 / month.** Input: **5.7m monthly transacting users, Q3 FY26, +21% YoY**, disclosed on the earnings call. A monthly transacting user transacts ≥1× per month, so monthly transactions ≥ MTU. **Band ≥100,000 → +5.** **Billing unit: a food order on Jubilant's own app/web.** Consistency check: ₹1,801.5cr ÷ 3 months ÷ 5.7m = ₹1,053/order, well above any plausible Domino's ticket — so the real figure materially exceeds this floor. **No point estimate is given because AOV is not disclosed.** ⚠️ **This counts own-channel only by construction — aggregator orders never touch Jubilant's stack.** | [medianama Q3FY26](https://www.medianama.com/2026/02/223-jubilant-foodworks-dominos-app-ad-platform-q3fy26-earnings-call/) |
| Active Customers / Users | **17.1m own-app MAU** (Q4 FY26, +25% YoY); **17.0m** (Q3 FY26); **5.7m MTU** (Q3 FY26); loyalty **13.6m (FY23) → 23.1m (FY24) → 33.7m (FY25) → >40m (Q2 FY26)** | [medianama Q4FY26](https://www.medianama.com/2026/06/223-jubilant-foodworks-q4fy26-genai-chatbot-delivery-growth/); loyalty series `[UNVERIFIED]` |
| Primary Currency | **INR** · also LKR, BDT, TRY | `[Source Code]` |
| Top 3 Markets by Revenue | **India** (standalone ₹1,801.5 cr Q3 FY26, +11.8%), **Türkiye** (+15.0%), then **Bangladesh** (+26.6%) and **Sri Lanka** (+65.9%) by growth | [investywise](https://www.investywise.com/jubilant-foodworks-investor-presentation-for-q3fy26-results/) |
| Stores | **~3,636** at FY26 end (+351 net in FY26). ⚠️ A conflicting **3,663** also appears. Safest hard number: **3,594 at Q3 FY26** | [kotakneo](https://www.kotakneo.com/financial-results/jubilant-foodworks-share-price-q4fy2025-26-results/), [freepressjournal](https://www.freepressjournal.in/business/jubilant-foodworks-q3-fy26-revenue-rises-134-to-2439-crore-store-count-at-3594) |
| Channel mix | **Delivery 76.1%** of sales (Q4 FY26); online ≈ **87% of delivery sales** (quarter unpinned); **own app ≈70% of Domino's orders** (Q3 FY26) / **55% of orders from own apps** (Apr 2025, fetched) | [storyboard18](https://www.storyboard18.com/amp/brand-marketing/jubilant-foodworks-q4-profit-jumps-67-percent-on-dominos-value-strategy-ws-l-98724.htm), [CIO.inc](https://www.cio.inc/from-pizza-to-ai-how-jfl-baking-tech-into-every-bite-a-27889) |
| **Billing channel split (web vs app store)** | **Not applicable — and this is a positive.** Food delivery has **no Apple/Google IAP leg**. Revenue runs through Jubilant's own checkout and through Swiggy/Zomato. **The app-store trap does not apply to this account.** | — |
| ⚠️ **Addressable-base warning** | **Aggregator orders never touch Jubilant's payment stack.** Addressable = own app + own web only. Best current anchor: **55% of orders from own apps**. **Do not use the 2019–2021 ~68% figures** — stale, COVID-inflated, likely optimistic | [Agent 5 analysis]; [Quartz](https://qz.com/india/2191903/even-dominos-thinks-zomato-and-swiggys-commissions-are-too-high) |

### Overall Research Confidence

**HIGH on the payment stack — the highest in this repo to date. MEDIUM on traffic and financials. LOW on anything resting on Jubilant's own documents.**

- **Payment stack, architecture and method sets: HIGH, and first-party.** I decompiled the production payment bundle myself, verified it is byte-identical across three countries by MD5, extracted the gateway enum, the method enum, the per-gateway dispatch, the microservice inventory, the API-version spread and a leaked backend class name with a full token schema. India's enabled method set is live-verified from server-rendered markup. This did not depend on a vendor announcement, and there are none.
- **Traffic: LOW. Downgraded one level, and the cause is stated.** **No SimilarWeb data was supplied** and no SimilarWeb MCP tool exists in this environment, so the country profile is a web-search estimate. Mitigating this considerably: web traffic is the **wrong metric** for an app-first merchant, and the app metrics (17.1m MAU, 5.7m MTU, 55–70% own-app orders) are sourced from earnings-call reporting and carry the volume argument on their own.
- **Financials: MEDIUM.** Revenue, store count, channel mix and growth-by-market all have sources, but **every JFL primary document sits on `jubilantfoodworks.com`, which returns HTTP 403 to automated fetches.** Not one primary JFL document was read. Three internal conflicts remain unresolved (FY26 revenue, FY26 store count, DP Eurasia stake).
- **Market context for the rail gaps: HIGH, and it killed three of my own hypotheses.** The Sri Lankan wallet angle, the BNPL angle and the e-mandate angle were all retired on sourced market data rather than carried forward because they sounded good.
- **Complaints: HIGH for India** (fetched brand page, four dated items, cross-rail pattern). **LOW for Sri Lanka** (one review title). **None for Bangladesh.**
- **Competitive: MEDIUM, with an explicit attribution ceiling.** Two QSR brands are on an orchestrator per the vendor's own fetched case studies, but neither names a market or entity, so the India read is inference.
- **Section 8 was completed**, unlike runs where egress blocking prevents it — but the live per-country **enabled** method lists remain out of reach behind a properly secured API.

### Manual Research Recommendations

> **Area:** ⛔ **Whether Yuno can route Razorpay volume in India**
> **Why it matters:** It is the difference between a seven-gateway pitch and a six-gateway pitch, and a payments engineer at Jubilant will know the Razorpay policy. This is the only item that should block sending.
> **Suggested manual action:** Ask Yuno Solutions/Partnerships directly, and get the current position on Cashfree and PhonePe too.

> **Area:** The identity of `GLOBALPAY`
> **Why it matters:** It is one of seven gateways and the only unknown one. It may be the cross-border or foreign-card route, which would change the cross-border read on this account.
> **Suggested manual action:** Walk a real cart to the payment step with DevTools open and watch where `globalpayUrl` posts; or inspect the TLS certificate on that host. Alternatively, ask them — it is a fair discovery question.

> **Area:** Confirm the CIO vacancy is still open
> **Why it matters:** It is the freshest timing signal in the file and it is ~2.5 weeks old, resting on two unfetched search summaries. If a successor has been named, the angle changes from "who owns this" to "new owner with a mandate."
> **Suggested manual action:** Check BSE/NSE announcements for Jubilant FoodWorks since 18 Sep 2026, and LinkedIn.

> **Area:** Live per-country enabled payment-method lists
> **Why it matters:** The Sri Lanka and Bangladesh findings are **code-inferred**. The bundle holds the superset; what is switched on sits behind an authenticated API that correctly returned 401/403.
> **Suggested manual action:** VPN into India, Sri Lanka and Bangladesh and walk a cart to the payment step on each `m.` domain. This is the single highest-value manual step and it also closes the Nagad question properly.

> **Area:** Confirm monthly transaction count and AOV directly
> **Why it matters:** The volume figure is a **floor** derived from MTU, not a measurement, and AOV is not disclosed anywhere. The business case needs the real own-channel order count.
> **Suggested manual action:** Pull the Q3/Q4 FY26 investor presentations **via BSE** rather than the company site — `bseindia.com/xml-data/corpfiling/AttachLive/...` serves PDFs where `jubilantfoodworks.com` 403s. Ask for order count and AOV on a discovery call.

> **Area:** The Nepal entity, and Popeyes' unexercised territories
> **Why it matters:** Popeyes has held rights to Nepal, Bhutan and Bangladesh since March 2021 and opened in **none** of them. A dormant-but-incorporated Nepal entity is exactly the detail that makes an opener land, and unexercised multi-country rights are a forward expansion signal.
> **Suggested manual action:** MCA/ROC lookup, plus the FY26 annual-report subsidiary schedule via BSE.

> **Area:** The PCI-DSS claim
> **Why it matters:** Section 9 rests on a search summary of a PDF that returned 403. PCI-scope reduction is a secondary pitch and should not be built on an unread sentence.
> **Suggested manual action:** Retrieve the annual report via BSE and read the IT-controls section.

> **Area:** Add to `accounts/apac-tal.csv`
> **Why it matters:** **Jubilant FoodWorks is not on the TAL at all**, and neither are the five prospects this run surfaced.
> **Suggested manual action:** Add **Jubilant FoodWorks**, **Devyani International**, **Sapphire Foods India**, **Rebel Foods**, **Restaurant Brands Asia** and **PickMe**. Devyani and Sapphire are P1 on the merger trigger.

### Appendix: All Source URLs

**Primary artefacts I fetched and parsed myself**
- `https://m.dominos.co.in/` · `https://m.dominoslk.com/` · `https://m.dominos.com.bd/` (all HTTP 200)
- `https://m.dominos.co.in/jfl-discovery-payment/en/dt/payment` (HTTP 200, `<title>Payment</title>`)
- `https://m.dominos.co.in/jfl-discovery-payment/public/dist/default/js/payment.js` (HTTP 200, 1,825,175 b, md5 `43acb80254b091185f8311b251342947`) — identical on the LK and BD hosts
- `https://m.dominos.co.in/jfl-discovery-ui/public/dist/default/js/app.js` (HTTP 200, 1,889,201 b)
- `https://www.dominos.co.in/` · `https://hongskitchen.in/` · `https://www.popeyes.in/` · `https://www.dominos.com.tr/` (all HTTP 200)
- `https://api.dominos.co.in|apis.dominoslk.com|api.dominos.com.bd/payment-service/ve1|ve2/options/default` → **401/403, correctly secured**
- `https://www.jubilantfoodworks.com/` · `https://pizzaonline.dominos.co.in/` → **HTTP 403, bot protection**

**Pages fetched via WebFetch**
- https://entrackr.com/news/after-phonepe-razorpay-and-cashfree-suspend-direct-integrations-with-juspay-8638638
- https://www.pluxee.in/helpcenter/consumer/where-can-i-use-pluxee-card/
- https://www.cio.inc/from-pizza-to-ai-how-jfl-baking-tech-into-every-bite-a-27889
- https://www.consumercomplaints.in/dominos-pizza-b100147
- https://juspay.io/customer-stories/mcdonalds · https://juspay.io/customer-stories/swiggy · https://juspay.io/in
- https://www.dominos.com.tr/kurumsal/online-odeme · https://www.dominos.co.in/gift-vouchers
- https://www.thedailystar.net/business/news/tk-6000cr-moves-daily-not-every-wallet-winning-4220811
- https://www.dailymirror.lk/print/business-news/Sri-Lankan-online-shoppers-stick-to-cash-on-delivery-amid-digital-payment-hesitation/273-307888

**Entities & financials:** zaubacorp.com · tofler.in · cleartax.in · kotakneo.com · univest.in · upstox.com · business-standard.com · freepressjournal.in · storyboard18.com · investywise.com · restaurantindia.in · marketscreener.com · investegate.co.uk · businessworld.in · open.er-api.com
**Complaints:** consumercomplaints.in (brand page + 4 complaints) · tripadvisor.in · dominos-pizza-india.pissedconsumer.com · x.com/dominos_india
**Corporate/news:** medianama.com (Q3FY26, Q4FY26) · indianretailer.com · bwpeople.in · cio.inc · cnbc.com · forbes.com · finshots.in · scanx.trade · indmoney.com · inc42.com · indiainfoline.com · news.popeyes.com
**Market context:** thedailystar.net · dailymirror.lk · tbsnews.net · dhakatribune.com · pickme.lk · pluxee.in · nationstrust.com · ft.lk · cbsl.gov.lk · docs.ebanx.com
**Orchestration landscape:** entrackr.com · inc42.com · business-standard.com · theheadandtale.com · juspay.io
**Technographics (low confidence):** appsruntheworld.com · rocketreach.co · instahyre.com · similarweb.com

</details>
