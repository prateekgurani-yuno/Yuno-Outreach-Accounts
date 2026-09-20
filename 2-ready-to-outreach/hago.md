# HAGO

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 19 / 29 → ⭐ **High Priority** — earned on arithmetic, no override applied
**Industry:** Casual game + voice-chat social app · **HQ:** **HAGO SINGAPORE PTE. LTD.**, UEN 201815430H, 30 Pasir Panjang Road #15-31A, Mapletree Business City, Singapore 117440 · parent **JOYY Inc. (NASDAQ: YY)** · **Researched:** 2026-09-20 · **First email sent:** —
**Motion:** **In-house orchestration**, and an unusually developed one. They built a group-wide pay-center. Never pitch "you need orchestration." Anchor on **maintenance burden, PSP sprawl and reach**.

---

> ## 🚨 READ THIS FIRST — the "Yuno" trap
>
> **JOYY operates a social app literally called Yuno.** Verified first-hand in the production pay-center bundle: `e.YUNO="yuno"`, `[APP_NAME.YUNO]:/yym-yuno-and(\d+\.\d+\.\d+)/`, `[APP_NAME.YUNO]:/^(.+\.)?(yunoliveapp\.com|yocolive\.com)$/`, and `.yunoliveapp.com` in the cookie-domain allowlist.
>
> **My own grep of that bundle returns 57 hits for "yuno". Every single one is JOYY's app `com.joyy.yuno`. None of them is us.**
>
> Anyone who greps a JOYY codebase and reports "Yuno is already integrated" will be wrong in a way that is very hard to walk back on a call. **Flag this before it reaches a deal review.**

---

> ## 🎯 THE HOOK — JOYY's own audited filing describes a multi-PSP recharge stack
>
> **Verified first-hand** by downloading JOYY's FY2025 Form 20-F from SEC EDGAR (CIK 1530238) and grepping the full text:
>
> > *"We have a **recharge system** for users to purchase our virtual currency. **Users can recharge via various online payment platforms provided by third parties.** Virtual currency is non-refundable and without expiry."*
>
> That is JOYY, under auditor review, describing exactly the shape of an orchestration buyer. It is a better opener than anything inferred.
>
> ### And the dated, audited trigger sitting next to it
>
> From the same filing: *"Bigo Live was temporarily removed from the Google Play Store and the iOS App Store in December 2024… reinstated on the Google Play Store in December 2024 and on the iOS App Store in early January 2025."*
>
> **JOYY has a named, dated, audited instance of losing store distribution.** That is the strongest possible internal argument for off-store billing, and it comes from their own paperwork — not from us.
>
> ### The companion observation — Indonesia has eleven rails and not one of them is QRIS
>
> **My own counts from the production pay-center bundle** (`pay.ihago.net/a/pay-center/assets/index-CylAhR5R.js`, 236KB, fetched 2026-09-20):
>
> | Indonesia rail | Occurrences |
> |---|---|
> | Alfamart | 10 · OVO 7 · LinkAja 4 · Indomaret 3 · GoPay 2 · plus DANA, bank VAs, four carriers |
> | **QRIS** | **0** |
> | **ShopeePay** | **0** |
>
> Indonesia is the **one market HAGO gives a dedicated payment backend** (`yjd-turnover.ihago.net`). It has Alfamart and Indomaret cash, five wallets, four carrier rails, four bank virtual accounts — **and no QRIS**, the rail Bank Indonesia made the national QR standard. ⚠️ **Frame it as a question, not an accusation** — the channel list may be server-driven rather than client-enumerated, and I could not test live availability (see §3).

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

### ✅ GATE 1 — Phase 0 on the JOYY payments question: **CLEARS**, with one thing to carry

This gate had a real chance of firing — VNGGames was rejected this week because its SEC filing disclosed it operated a payment gateway. **I downloaded JOYY's FY2025 20-F myself and ran the same test:**

| Term | Hits in the FY2025 20-F |
|---|---|
| "payment gateway" | **0** |
| "digital wallet" | **0** |
| "e-wallet" | **0** |
| "payment license" / "payment licence" | **0** |
| "intermediary payment" | **0** |

JOYY is the **payer**, not the operator: *"we sell almost all of our products and services to our users through **third-party online payment systems**… **We do not have control over the security measures of our third-party online payment vendors**"* and *"**our third-party payment processors** may from time to time experience cash flow difficulties."*

⚠️ **One caveat to carry into the account plan — real, but not HAGO.** JOYY's e-commerce SaaS arm **Shopline** embeds merchant payment processing: *"integrating enterprise-grade storefront management, **localized and cross-border payment processing (Shopline Payments)**"*, and restricted cash includes *"fixed deposits pledged for **payment processing operations**"* (US$21.6M). **That is a separately-segmented sibling business. HAGO buys payment processing; it does not sell it.** If anyone asks "doesn't JOYY do payments?", the honest answer is: *Shopline Payments exists, HAGO is a different segment, and no payment licence is disclosed in either 20-F.* Put it in the account notes rather than letting it surface cold in a review.

### ✅ GATE 2 — Territory: **In scope. Genuinely Singapore.**

| Evidence | What it shows |
|---|---|
| **Google Play developer block** | HAGO SINGAPORE PTE. LTD., 30 Pasir Panjang Road #15-31A, Mapletree Business City, Singapore 117440 |
| **Apple seller-of-record** (iTunes lookup, trackId 1400667917) | `sellerName` = **HAGO Singapore PTE. LTD**, `sellerUrl` = ihago.net |
| **HAGO's own site bundle** | `CompanyName:"HAGO SINGAPORE PTE.LTD"` · `Headquarters:"65 CHULIA STREET #38-06 OCBC CENTRE SINGAPORE"` · `FounadedTime:"Founded: May 2018"` |
| **Singapore register** | UEN 201815430H, incorporated 07 May 2018, **Live**, principal activity *development of computer games* |

⚠️ **Honest counter-evidence, reported not hidden:** the Play developer contact is a **mainland China mobile (+86)**; the pay-center is served off Alibaba Cloud (`server: Tengine`); analytics go to `hiido.com` (YY's in-house stack); the bundle references `efox-pay-test.yy.com` and carries untranslated Simplified-Chinese dev strings (`Xendit_BankTransferSub_BNI_Tip:"点击查看详情"`). **Verdict: a China-origin company with a genuine Singapore operating and billing entity** — the same pattern the gate warns about, resolving the right way. Same shape as HoYoverse/Cognosphere.

⚠️ **On the Middle East worry:** JOYY discloses no regional revenue at the HAGO level, so **I cannot say whether revenue is APAC- or MENA-weighted and will not claim it.** What is evidenced is that the *payment infrastructure* is APAC-weighted: Indonesia and South Asia each get a **dedicated regional backend**, MENA shares one with Africa and Turkey; APAC runs 10+ providers and 60+ methods, MENA runs **two** providers (Tap Payments, Centili) and ~6 methods.

### ✅ GATE 3 — App-store trap: **ESCAPED, on positive evidence**

**Verified first-hand in the pay-center bundle:**

```js
buyChannels:["Google+Balance"]   // com.yy.hiyo, Android
channelPkgs:[{channelPkgName:"huawei"},{channelPkgName:"xiaomi"},{channelPkgName:"aptoide"}]
DUAL_MODE_THIRD_CHANNELS=[{channel:"Airwallex+Balance", env:[{pack:"com.yy.hiyo", platform:"android"}]}]
```

Three things fall out, and they are the core finding:

1. **`Google+Balance` and `Apple+Balance` are just two entries in the same channel list** as Xendit, Coda, dLocal and Airwallex. HAGO treats IAP as **one rail among ~25**, selected by the same router.
2. **`Airwallex+Balance` is explicitly scoped to `pack:"com.yy.hiyo", platform:"android"`** — i.e. enabled specifically for the HAGO Android app. That is the most direct evidence that HAGO runs alternative billing against a global PSP **today**.
3. **HAGO ships non-Play Android builds** — `huawei`, `xiaomi`, `aptoide`. Those have no Google Play billing obligation at all and route 100% to third-party rails.

**Plus an off-store wholesale rail:** `ihago.net/a/recharge-of-agent/` returns HTTP 200, titled *"Diamonds Recharge"*, with a full tiered-distributor console (`Add Agent`, `TransferAgent`, `addedSecondaryAgent`, `ApproveRecharge`, `Cumulative Diamonds Sold`, `IsBigRechargeCustomer`). `[Agent-sourced.]` **And a third-party reseller:** Codashop Indonesia sells HAGO diamonds through GoPay, DANA, OVO, LinkAja, bank transfer, Kredivo, DOKU Wallet and four carriers.

⚠️ **NOT ESTABLISHED: the IAP-vs-alternative split.** No disclosure exists, the channel API is request-signed, and no public dataset splits it. **This is the right first question on a call, not an assertion in an email.**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach HAGO`.*

⚠️ **Read before drafting.**

1. **Lead with the QRIS gap in Indonesia**, framed as a question, against their own eleven other Indonesian rails. Internal asymmetry, both halves theirs.
2. **The Bigo store-takedown line is the strongest supporting argument** — it is audited, dated and theirs. It argues for off-store billing better than we can.
3. **Motion is in-house and the layer is genuinely good.** They built a multi-tenant pay-center serving ~25 JOYY apps. The wedge is **maintenance burden and PSP sprawl**, never "you have no orchestrator."
4. **Never claim a regional revenue split.** It is not disclosed. Payment topology is a proxy and must be labelled as one.
5. **Do not quote the 4.62% payment-handling ratio as proof of anything** (see §3).
6. **The consumer-pain signal is thin — do not inflate it.** One refund complaint and two disbursement complaints across 150 Indonesian Play reviews. Build on architecture, not frustration.
7. **Mind the Yuno-app trap** if anything technical gets shared internally.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 19 / 29

| Signal | Points | Status |
|---|---|---|
| Monthly transaction count | **+5** | ✅ **DERIVED** — even the deliberately harsh case clears the floor (~55,000/month addressable). See below |
| Orchestration status | **+1** | **In-house layer**, stated affirmatively on positive evidence — the bundle *contains* the orchestration layer |
| 3+ countries | **+3** | ✅ **Seven regional backends across ~150 country codes**, verified by me in the routing config |
| Multiple PSPs | **+3** | ✅ **~25 confirmed** from the production bundle |
| Local rail gap in a top market | **+3** | ✅ **QRIS and ShopeePay both zero in Indonesia**, their one dedicated-backend market; **JazzCash, Easypaisa, bKash, Nagad all zero** despite `-PK-` and `-BD-` being routed |
| Recent expansion | **0** | ⬜ Not established — no dated new-market launch found |
| Payment issues reported | **+2** | ✅ Dated Play reviews: a Google Play refund awaiting publisher approval; **two airtime-disbursement failures** — HAGO runs a payout rail that fails |
| Funding >$10M | **0** | ❌ NASDAQ-listed parent |
| High traffic outside home | **+2** | ✅ Singapore entity, revenue across Indonesia, MENA and LatAm |
| Competitor using orchestration | **0** | ⬜ Not established |
| Payment job postings | **0** | ⬜ Not established |
| **TOTAL** | **19** | ⭐ **High Priority** |

### The routing config — verified first-hand

From `pay.ihago.net/a/pay-center/assets/index-CylAhR5R.js`, verbatim (my own fetch, 2026-09-20):

```js
"pay.ihago.net":{regions:[
 {externalHost:"mm-turnover.ihago.net",  countrys:"-IN--NP--PK--BD--LK-"},
 {externalHost:"yjd-turnover.ihago.net", countrys:"-ID-"},
 {externalHost:"db-turnover.ihago.net",  countrys:"-AE--EG--ET--IQ--SA--KW--BH--YE--SY--NG--OM--QA--TR--…"},
 {externalHost:"gg-turnover.ihago.net",  countrys:"-US--AR--CO--PE--MX--EC--CL--BO--UY--PH--CA--…--AU--NZ--GB--…"},
 {externalHost:"sbl-turnover.ihago.net", countrys:"-BR--PT-"},
 {externalHost:"jlp-turnover.ihago.net", countrys:"-MY--SG--TH--VN--JP--KR--MM--KH--…--TW-"},
 {externalHost:"msk-turnover.ihago.net", countrys:"-RU--UA--AZ--KZ--…"}],
 project:{revenueAppId:"1802", uidKey:"hagouid"}, …
```

**Indonesia and South Asia each get their own backend. MENA shares one with Africa and Turkey.** That is deliberate APAC infrastructure.

### PSPs — ~25, all from the production bundle (my own counts)

| Provider | Key occurrences | Coverage |
|---|---|---|
| **Xendit** | 53 | Indonesia — DANA, OVO, LinkAja, Alfamart, BNI/BRI/Mandiri/Permata VAs |
| **Centili** | 52 | MENA carrier billing — Etisalat, Mobily, STC, Zain, Vodafone, Orange |
| **Mol / Razer Merchant Services** | 37 | SEA — FPX, GCash, TrueMoney, LINE Pay, PH banks, TH banks, 15 Turkish banks |
| **Coda Payments** | 34 | SEA + India — DANA, GoPay, GCash, PayMaya, Alfamart, Indomaret, carriers, DOKU Wallet, Paytm |
| **ShareitPay** | 36 | India/PH — UPI, Paytm, PhonePe/Mobikwik, netbanking, GCash, Coins.ph, DragonPay |
| **EBANX** | 36 | LatAm — OXXO, Baloto, PagoEfectivo, RapiPago, PSE, SPEI, webpay |
| **dLocal** | 30 | LatAm — cards, Boleto, Pix |
| **Nganluong** | 25 | Vietnam — carrier cards, ATM, netbanking |
| **Xsolla** | 20 | Russia/CIS — qiwi, yandex, vkPay, webMoney, Sberbank |
| **V5pay** 18 · **Tikipay** 12 · **Upay** 12 · **Airwallex** 11 · **Checkout.com** 10 · **Oceanpay** 10 · **Tap Payments** 7 · **Huifu** 7 · **Paymentwall** 6 · **PayPal** 5 · **Catappult** 5 · **Dokypay** 4 · **Antom/Alipay+** 2 · **Stripe** 2 · **Pagsmile** 2 · **Momo** 1 · **Payoneer** 1 · **EZeeLink** 1 · **CrossPay** 1 | | |

**Orchestrators — my own grep, all ZERO:** Juspay · Spreedly · Primer · Gr4vy · CellPoint · APEXX · Payrails · IXOPAY. *(Yuno's 57 hits are JOYY's own app — see the banner.)*
**Also zero:** Midtrans · PayerMax · 2C2P · Adyen · Worldpay · UnionPay.

⚠️ **False positives caught:** `Coda_Pay_DOKUWallet` is **DOKU sold as a wallet through Coda, not DOKU as an acquirer** — exactly the trap the methodology warns about. `tap:81` in the agent-portal bundle is RxJS `.tap()`, not Tap Payments. Every `dana` hit was checked individually and all resolve to real DANA channel keys, none from Indonesian `pengembalian dana` copy.

### Orchestration: IN-HOUSE — affirmatively, not by absence

The bundle **contains** the orchestration layer. Positive evidence:

1. A named, versioned, actively-maintained routing product at `/a/pay-center/` (`last-modified` five days before this report).
2. A **provider-agnostic channel model** — every method is a `{payChannel, payMethod, subChannel}` triple normalised through `getChannelName()` and keyed per country: `(f=[r,a,i,o].filter(h=>h)).join("+")+"_"+(country||"ALL")`. That is a routing table.
3. **Per-PSP SDK adapters behind one dispatcher** — `handleSDK({...})` branching on `isDlocalDirect`, `isAnTom`, `isAirwallexBalance`, `isAirwallexCard`, `isPaypalSPB`, `isHuifuDirectwarys`, `isCentili`, `CrossPay_Gate_UPI`.
4. **Its own tokenisation/vault UI** — `SDK_checkout_StoredCards`, `SaveCard`, `/comm/getQuickPaymentAccountList`, `/comm/deleteQuickPaymentAccounts`.
5. **Its own risk layer** — `riskControlTh`, `filterThParamChannel`, `filterLevelLaterChannelModeChannel`.
6. **Multi-tenant across ~25 JOYY apps** — one config object routes `pay.ihago.net`, `pay.olaparty.com`, `pay.moschat.com`, `pay.bolohi.net`, `pay.yunoliveapp.com`, `pay.lumoschat.com`, `pay.ludoisle.com`, `pay.tilive.net`, `pay.dera.chat`, `pay.loversnovel.com` and more.
7. **Own backend on EOL infrastructure** — `/charge_currency/chargeWithData`, `/charge_currency/query_channel_data`, served from **Apache Tomcat 7.0.82**, EOL since March 2021. `[Agent-sourced.]`

**Commercial read:** hardest to displace and highest value at once. Rip-and-replace, not bolt-on — but the prize is not HAGO's line, it is **a group-wide pay-center serving ~25 apps across ~150 countries with ~25 PSPs on an end-of-life stack**. HAGO is the door, not the room.

### Payment methods — the gaps worth naming

| Market | Present | **Absent (my own counts, all zero)** |
|---|---|---|
| **🇮🇩 Indonesia** *(dedicated backend)* | DANA · OVO · LinkAja · GoPay · GrabPay · BNI/BRI/Mandiri/Permata VA · **Alfamart · Indomaret** · DOKU Wallet (via Coda) · carriers Telkomsel/XL/Indosat/Tri · cards | ❌ **QRIS** ❌ **ShopeePay** |
| **🇵🇭 Philippines** | GCash · Maya · Coins.ph · DragonPay · 7-Eleven · SM · Robinsons · Bayad Center · BDO/BPI/Metrobank/RCBC/UnionBank · Globe · Smart/Sun | — |
| **🇻🇳 Vietnam** | MoMo · Viettel/Vinaphone/MobiFone/FPT/Zing cards · ATM/internet banking | ❌ ZaloPay ❌ VNPay |
| **🇮🇳 India / South Asia** *(dedicated backend)* | UPI · Paytm · PhonePe/Mobikwik · netbanking · OTC banks/ATMs · FreeCharge | ❌ **JazzCash, Easypaisa (PK)** ❌ **bKash, Nagad (BD)** — despite both being routed |
| **🇹🇭🇲🇾 SEA** | TrueMoney (wallet/cash card/agent) · Rabbit LINE Pay · mPAY · SCB/KBank/KTB/Krungsri/BBL · AIS/DTAC/Truemove/CAT · FPX · Celcom/Digi · Razer Gold | ❌ **PromptPay** ❌ **PayNow** |
| **🇰🇷🇹🇼🇯🇵** | — | ❌ **KakaoPay, Toss, MyCard, konbini** — all zero despite `-KR--TW--JP-` being routed |
| **Gulf/MENA** | mada · KNET · BENEFIT · Fawry · 6 carriers | *(out-of-territory markers)* |

⚠️ **This is the build-time catalogue, not live availability.** `POST yjd-turnover.ihago.net/charge_currency/query_channel_data` is **request-signed** (returns `Required String parameter 'sign' is not present`), so per-country live enablement could not be enumerated. Some catalogued channels may be dark; some live channels may be server-driven and absent from the client enum. **Say "I could not find" rather than "you do not have."**

### Financials — group only, HAGO not disclosed

| Metric | FY2025 |
|---|---|
| JOYY total net revenues | US$2,124.2M (2024: US$2,237.8M) |
| Live streaming | US$1,529.7M · Advertising US$442.7M (20.8%) |
| Group MAU | **272.1 million** (Q4 2025) |
| Paying users | 3.6M — **explicitly for Bigo Live, Likee and imo. HAGO is excluded.** |
| **"All other" segment live-streaming revenue** | **US$83,230k** (2024: US$88,430k) — *HAGO's ceiling, shared with other audio platforms* |
| "All other" total revenue / operating loss | US$277,137k / **US$(151,942)k** |
| Mainland China share of group revenue | 9.8% |

**JOYY on HAGO, verbatim:** *"Launched in 2018, Hago has a presence mainly in **Southeast Asia, the Middle East and South America**. Hago currently monetizes its user base mainly through virtual tips for live streaming."*

**Ownership confirmed:** JOYY divested Huya (2020) and completed the **sale of YY Live to Baidu on 2025-02-25**. HAGO was in neither disposal and is named as a current JOYY platform throughout the FY2025 filing.

**Scale (store-reported, not audited):** Google Play **299,309,592 lifetime installs**, 4.1★ from 6,382,102 ratings. Apple ID-storefront rating count **3,010** — **iOS is a rounding error; this is an Android-dominant app**, which matters because Android is where alternative billing is viable.

⚠️ **The tempting number that must NOT be used.** FY2025 Note 21 gives **"Payment handling costs" of US$98,164k on US$2,124,248k net revenue = 4.62%** (2024: US$120,292k; 2023: US$137,989k). 4.62% is far below a 15–30% store commission — **but it is equally consistent with store commissions being netted out of revenue and excluded from that line, and the filing does not say which.** `[INFERENCE, not confirmed.]` **Do not use it as proof of anything.** What it *does* support, directionally, is that someone at JOYY is actively working payment costs down — a 29% decline over two years against a 7.7% revenue decline.

### Volume — DERIVED, six of nine inputs assumed

| # | Input | Value | Status |
|---|---|---|---|
| 1 | "All other" live-streaming revenue FY2025 | US$83,230k | **SOURCED** — 20-F Note 33 |
| 2 | HAGO's share of that line | 60% | **ASSUMED** (range 40–80%) |
| 3 | Average ticket | US$3.00 | **ASSUMED** — anchored on sourced ladders: Codashop ID Rp1,932–Rp1,079,189; Play ID "Rp 3.300 - Rp 5.032.500 per item" |
| 4 | Non-store addressable share | 30–60% | **ASSUMED** — justified by ~25 PSPs, a dedicated ID backend, the agent network, three non-Play Android channels, and Airwallex scoped to the HAGO package. **Not measured** |

| Scenario | HAGO share | Ticket | Non-store | **Addressable txns/mo** |
|---|---|---|---|---|
| **Harsh** | 40% | US$10 | 20% | **~55,000** |
| **Base** | 60% | US$3 | 45% | **~625,000** |
| **Generous** | 80% | US$2 | 60% | **~1,665,000** |

**Even the deliberately harsh case clears the 40,000 floor.** Sanity check: group live-streaming US$1,529.7M ÷ 3.6M paying users ≈ US$425/yr ≈ US$35/month, i.e. ~12 purchases per paying user per month at a US$3 ticket — plausible for a gifting-driven social app. HAGO's US$83.2M line is 5.4% of group live streaming. The figures hang together.

⚠️ **Do not quote group volume as HAGO volume.** If the 4.62% ratio is representative, group payment volume is on the order of US$2B/yr — but that is ~25 apps, not HAGO.

### Complaints — thin, and labelled as thin

Method: 150 Indonesian Google Play reviews via the Play batchexecute endpoint, plus App Store RSS for ID/PH/US/IN. `[Agent-sourced.]`

- **2026-07-30, 1★ (ID):** *"Aku beli diamond di hago… **ingin ku refund aja lalu aku mengajukan refund lewat google play**… **tapi smpe skarang blom di setujui sama hago** ini udah 2 hari"* — a Google Play refund awaiting publisher approval after two days. **Confirms Play IAP is genuinely in use and that refunds carry a publisher-approval step.**
- **2026-09-14, 3★ (ID):** *"udah **reedem pulsa di uang phon tpi blum masuk di nomerku**"* — redeemed airtime never arrived. **HAGO runs a payout/disbursement rail in Indonesia and it fails.** Disbursement failure is a distinct, separately-sellable problem.
- **2026-09-11, 3★ (ID):** *"kita topup kristal tapi gak ngaruh sama sekali sm VIP… harus topup diamond melulu"* — confirms **two separate virtual currencies (Kristal and Diamond)** with separate top-up flows, matching the agent portal's two consoles.

**Honest negative:** across 150 Indonesian Play reviews and 118 App Store reviews, the dominant theme is **game fairness and ad load, not payment failure.** One refund complaint and two disbursement complaints is thin. **Label it as weak in any outreach; do not inflate it.**

**A standing public help article on failed top-ups: INCONCLUSIVE, not negative.** `help.ihago.net` does not resolve; `/a/help/`, `/a/pay-help/`, `/a/recharge-help/` all 404. HAGO's own review replies route users to an **in-app** Help Center, unreachable without the app.

### Methodology notes

- ⚠️ **CSP is the no-evidence case.** `pay.ihago.net` returns **no `Content-Security-Policy` header at all** — verified by me. No `form-action`, no allowlist, so absence of a PSP host proves nothing in either direction. **Every PSP conclusion rests on the production bundle**, which is stronger anyway.
- **The channel API is request-signed**, so live per-country availability is unobtainable without a session.
- **The pay-center is primarily an in-app H5 webview** — it reads `hagouid` from `window.nativeApp.userToken()`. The standalone web surfaces are the **agent portal** and **Codashop**.

### What could NOT be established

1. **The IAP-vs-alternative split.** No disclosure, signed API, no public dataset. **First question on a call.**
2. **HAGO-level revenue, MAU, DAU, paying users or ARPU.** The 3.6M paying-user figure explicitly excludes HAGO.
3. **HAGO's revenue split by region** — payment topology used as a proxy and labelled as one. **The "APAC or MENA account?" question is not settled by revenue.**
4. **Live per-country channel availability.**
5. **Whether QRIS or ShopeePay are live in Indonesia but server-driven.** Zero bundle hits and absent from Codashop — a strong, specific, verifiable talking point **framed as a question**.
6. **Whether "payment handling costs" include Apple/Google commission.** Unresolvable from the filing.
7. **A public help article on failed top-ups** — in-app only.
8. **Payment hiring, PSP press releases, payment licences** — searched, nothing found. Absence of evidence only.
9. **Pakistan and Bangladesh rails** — routed but no method enums. Genuine unknown.

### Overall research confidence — **HIGH on architecture, NIL on HAGO-level financials**
The Phase 0 grep, the region routing config, the ~25 PSP enums, the Airwallex package scoping, the non-Play Android channels, the QRIS/ShopeePay zeros and the Yuno-app trap were all read by me in the live 20-F and the live production bundle today. What does not exist is any HAGO-level financial disclosure at all.

</details>
