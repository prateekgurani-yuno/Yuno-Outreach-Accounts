# SEA Gamer Mall (SEAGM)

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 22 / 29 → ⭐ **High Priority** — earned on arithmetic, no override applied
**Industry:** Digital-goods marketplace — game top-ups, gift cards, credits · **HQ:** Sitiawan, Perak, Malaysia — **SEA Gamer Mall Sdn Bhd** (reg. 201201016057 / 1001568K, inc. 2012-05-14) · **Researched:** 2026-09-20 · **First email sent:** —
**Motion:** **Greenfield.** Seven named PSPs, 39 billing currencies, ~90 rails, and no routing layer of any kind — not third-party, not in-house.

---

> ## 🎯 THE HOOK — Vietnam has exactly one way to pay, and it is a foreign card
>
> **I enumerated SEAGM's entire "Online Payment" help-centre section myself on 2026-09-20 — all 89 articles across 8 paginated pages** (https://help.seagm.com/hc/en/sections/26-Online-Payment). Article count by billing currency:
>
> | Currency | Articles |
> |---|---|
> | USD | 13 |
> | KRW | 9 |
> | **IDR** | **8** |
> | **PHP** | **7** |
> | EUR | 5 |
> | **MYR** | 4 |
> | JPY | 4 |
> | **SGD** | 3 |
> | MNT (Mongolia) | 3 |
> | HKD | 2 · AUD 2 · CNY 1 |
> | **🇻🇳 VND** | **1** |
>
> That one Vietnamese article is `537-How-to-make-payment-using-Credit-Debit-Card-[VND]`. **I opened it.** Step 3, verbatim: *"You will be directed to the **Airwallex** payment page. Enter your name, email and card details."*
>
> **SEAGM bills in Vietnamese dong, runs `en-vn` and `vi-vn` locales, and offers Vietnamese buyers a card form on a foreign acquirer.** No MoMo. No ZaloPay. No VNPay. Indonesia — the neighbouring market, same vertical, same buyer — gets eight rails including QRIS, GoPay, DANA, LinkAja, ShopeePay and three bank VAs.
>
> **That is the asymmetry, and both halves are their own documentation.** A digital-goods merchant selling to Vietnamese gamers through a card-only checkout is leaving the majority of that market at the cart.
>
> ⚠️ **One honesty note on the enumeration.** The section listing is *not* a complete census — I probed six article IDs the research agent had found (PromptPay `1078`, Thai mobile banking `1326`, Touch 'n Go `1490`, DuitNow QR `1283`, ShopeePay MY `1424`, Maybank QRPay `1157`) and **all six resolve to live articles that do not appear in either section listing.** So unlisted articles exist. The Vietnam finding rests on the section enumeration *plus* a separate keyword search that returned nothing for MoMo, ZaloPay or VNPay — strong, but not airtight. **Frame it as a question, not an accusation:** *"the only VND payment option I could find documented is a card form — is MoMo live and just undocumented?"*

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

### ✅ GATE 1 — Phase 0: PASSES, and the wallet question is closed

**Merchant, not a PSP.** Self-described: *"SEAGM.com is a digital goods platform that **retails** gaming products and services to individuals and businesses"* (https://corp.seagm.com/platform).

**"SEAGM Balance" is store credit, not e-money.** *"a prepaid account denominated in the local currency, allows SEAGM users to top up and make purchases **on our platform**"* — no currency conversion, expires after 2 years' inactivity, withdrawal only back to the original payment method at SEAGM's discretion (help article `124`). Closed-loop. **Does not route to Partnerships.** No evidence of any payment or e-money licence in any jurisdiction; *no public information found*.

⚠️ **One nuance to expect on a call, not a blocker.** The corporate site pitches content partners with *"One Platform, Global Coverage — A single integration unlocks global & local alternative payment methods"* and *"250+ Global Payment Channels"*. That is a **distribution/reseller** pitch — SEAGM is merchant of record for the publisher's goods — not third-party processing. But they will frame their own payment breadth as an asset they sell.

### ✅ GATE 2 — App-store trap: **ESCAPED**, and this one is provable

**Verified first-hand in the page source of https://pay.seagm.com/ on 2026-09-20:**

```js
window.ReactNativeWebView.postMessage(...)   // 2 occurrences
seagm://                                      // 4 occurrences
```

**SEAGM's mobile app loads their own web payment centre in a React Native webview and deep-links back via `seagm://`.** It does not use IAP. **Orchestration reaches app revenue as well as web revenue here** — which is the opposite of the failure mode `subscription-payments.md` §4 warns about, and the reason this account outranks most of the gaming batch.

### Also verified first-hand on the same host — the fraud stack

```js
"for"+"ter"+".co"+"m"           // deliberately string-split to evade blockers
var siteId = "f7e93b5be549";
ftr__startScriptLoad / ftr__ncd / ftr__altd / ftr__snp_cwc   // 31 ftr__ occurrences
cdn9.forter.com / cdn3.forter.com
```

**Forter is deployed — on the payment host only.** I grepped `www.seagm.com` separately: zero `ftr__`, zero Forter fragments. Corroborated by their own copy: *"You will be required to verify your identity when your payment is **flagged by our fraud solution system**"* (article `1054`).

### The markets — 39 billing currencies, 17 of them APAC

Country/currency selector at https://www.seagm.com/language_currency. APAC options verbatim: `AUD · BND · CNY · HKD · IDR · JPY · MOP · MYR · NZD · PKR · PHP · SGD · KRW · NTD · THB · USD · VND`. Plus 22 non-APAC currencies.

**Notable absences: no INR** (despite `en-in`/`hi-in` locales existing) **and no KHR** — Cambodia is served but billed in **USD**, with every Cambodian method article tagged `[USD]`.

**Architecture note, and it is the pitch in one line:** payment availability is driven by **selected currency, not detected country**. SEAGM's own article `5528`: *"If the platform does not support the selected currency, **no payment method will be shown**. To resolve this, switch to a supported currency."* Per-method currency-gating is hand-written into the help copy — *"The Dana [IDR] payment method is ONLY supported under the Indonesian Rupiah"* (`737`), *"Touch N Go Payment is only limited to Malaysian users under the MYR Currency"* (`1490`), *"The MOLPay PayNow [SGD] payment method is ONLY supported under the Singapore Dollar"* (`736`). **That per-method rule-writing is precisely what a routing layer absorbs.**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach SEA Gamer Mall`.*

⚠️ **Read before drafting.**

1. **Lead with the Vietnam gap** — but phrase it as a question, per the enumeration caveat above. Pair it with Indonesia's eight rails as the internal contrast.
2. **The second observation is the manual KYC** (§3) — it is verified, it is extreme, and it is visible in their Trustpilot tail.
3. **Motion is greenfield**, so noting the absence of routing is fair. The sharper frame is what the absence costs: per-method currency rules maintained by hand in help articles.
4. **Do not quote a revenue figure.** Private company, no audited financials. The aggregator numbers in §3 are unverified and must not be used.
5. **Do not quote individual Trustpilot review text beyond what is recorded in §3** — those five are the ones I have on a fetched page.
6. **Ask for `seagm.com/pay`** — their privacy policy promises a list of payment-channel partners at that URL and **the URL is dead**. It is the highest-value missing artefact and a natural discovery question.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 22 / 29

| Signal | Points | Status |
|---|---|---|
| Monthly transaction count | **+5** | ✅ **DERIVED from two sourced milestones** — ~83,000 orders/month averaged 2013–2016, before a 7.9× growth in registered users. See below |
| Orchestration status | **+4** | ✅ **Greenfield** — zero genuine hits across 60+ payment articles, Terms of Sale, Privacy Policy, homepage source, corporate site and `pay.seagm.com` |
| 3+ countries | **+3** | ✅ **17 APAC billing currencies**, ~22 locales, offices in MY/TH/CN/SG |
| Multiple PSPs | **+3** | ✅ **Seven named by SEAGM itself** — Stripe, MOLPay, Airwallex, PayPal, Paysafecard, Skrill, Atome |
| Local rail gap in a top market | **+3** | ✅ **Vietnam is card-only**, on a foreign acquirer, against Indonesia's eight rails |
| Recent expansion | **0** | ⬜ Not established — the PayPal and Atome campaigns are promotional, not expansion |
| Payment issues reported | **+2** | ✅ **Trustpilot 4.0/5 across 7,916 reviews with a 10% one-star tail (~790 reviews)**, plus their own standing decline FAQs (`1226`, `1368`, `1339`, `5528`) |
| Funding >$10M | **0** | ❌ Private, self-funded from retained earnings `[UNVERIFIED]` |
| High traffic outside home | **+2** | ✅ Malaysia HQ; sells across 160+ countries in 39 currencies |
| Competitor using orchestration | **0** | ⬜ Not established |
| Payment job postings | **0** | ⬜ Not established |
| **TOTAL** | **22** | ⭐ **High Priority** |

### Volume — DERIVED from sourced milestones

**Inputs, both from the milestones timeline at https://corp.seagm.com/:**
- 2013 milestone: *"More than 1 million completed orders"*
- 2016 milestone: *"More than 4 million orders have been completed since inception"*

**(4,000,000 − 1,000,000) ÷ 36 months = ~83,333 orders/month**, averaged across 2013–2016.

**Cross-check (partly ASSUMED):** 215,000 monthly active users today; at an **assumed** 1 order per MAU per month, ~215,000/month.

**Verdict: comfortably above the 40k floor on the sourced-and-derived figure alone**, and that run rate is a decade old — registered users have gone from 1M (2017 milestone) to 7.9M. **This account is not rejected on volume.**

### Self-reported scale — with its own contradictions flagged

From https://corp.seagm.com/ and /about: 125M yearly pageviews · 8M yearly unique visitors · 7.9M registered users · **215,000 MAU** (homepage) / 2.5M annual active users (about page) · 250+ payment channels · 10,000+ products · 650+ mobile operators · 160+ countries.

⚠️ **Their marketing numbers are not internally consistent** — the same corporate homepage elsewhere claims *"Reach our 11 Million + and growing active users"*, and quotes both "250+" and "100+" payment channels on one page. The live currency selector shows **39** currencies against a claimed "51 Local Currencies". **Use 215K MAU / 7.9M registered / 39 currencies; treat the rest as marketing.**

### PSP identification — seven named in SEAGM's own copy

| PSP | Evidence | Scope |
|---|---|---|
| **Stripe** | Article `1438`, **fetched and read by me**: *"Stripe is a payment gateway that accepts the majority of Credit / Debit Cards with a total of 135 currencies… without adding operational complexity."* Also `1439`, `1447` | Global card acquiring |
| **MOLPay** (Razer Merchant Services) | Article `736`, **read by me**: *"How to make payment via MOLPay using PayNow QR [SGD]"* — and *"To proceed with a refund on MOLPay PayNow payment, a **0.50 SGD will be charged per transaction**."* Also `165` (Maybank2u MY) | MY + SG local rails |
| **Airwallex** | Article `737` (DANA, IDR) — **and, found by me, article `537`: Vietnam card payments also route to Airwallex** (*"You will be directed to the Airwallex payment page"*). The research agent had Airwallex on Indonesia only | **Indonesia AND Vietnam** |
| **PayPal** | `1222`, `1226`, `1554`; active co-marketing *"SEAGM x PayPal 7.5% OFF Bonus Campaign"* | Global |
| **Paysafecard** | `1148` | Global |
| **Skrill** | `4844` | Global |
| **Atome** | `1051`; homepage banner *"Enjoy Exclusive SG61 Savings on SEAGM with Atome!"* | BNPL, SG |
| **Forter** | Obfuscated snippet on `pay.seagm.com`, siteId `f7e93b5be549` — **verified by me** | Fraud, payment host only |

**Explicitly searched and NOT FOUND:** iPay88, 2C2P, Xendit, Midtrans, Omise/Opn, GHL/eGHL, Coda Payments, Xsolla, PayerMax, Adyen, Worldpay, dLocal, Checkout.com.

⚠️ **False positives caught and discarded** (context printed before rejecting): **"Razer" appears 23× on the homepage — all of it Razer Gold, a gift card SEAGM *sells*, not Razer as acquirer.** "iPay88" hits were fuzzy matches on Cambodia's **Pi Pay**. "Opn", "Coda", "GHL", "Primer", "dLocal" and "Xendit" all returned unrelated game-redemption articles — **the help-centre search is fuzzy and generates heavy noise.**

**The Terms of Sale and Privacy Policy name no processor.** The policy does give a structural tell: *"All payment data is stored by the respective **payment channel partners**. You may find our list of payment channel partners here: seagm.com/pay"* — **and that URL is dead**, returning the homepage byte-for-byte. Plural "partners" is SEAGM's own confirmation of a multi-acquirer setup.

### Payment methods per market

Every line is a live SEAGM help article; base `https://help.seagm.com/hc/en/articles/`.

| Market | Present | **Absent** |
|---|---|---|
| **🇲🇾 Malaysia [MYR]** | FPX `1328` · DuitNow Transfer `1282` · DuitNow QR `1283` · Touch 'n Go `1490` · Boost `1327` · ShopeePay `1424` · Maybank2u `166` · **Maybank2u via MOLPay** `165` · Maybank QRPay `1157` · Visa/MC `1329` · Razer cash @ 7-Eleven `1531` | ❌ GrabPay MY · ❌ CIMB Clicks |
| **🇮🇩 Indonesia [IDR]** | QRIS `1013` · GoPay `983` · **DANA via Airwallex** `737` · ShopeePay `1009` · LinkAja `1010` · BRI VA `982` · BNI `341` · Mandiri `342` | ❌ OVO · ❌ Alfamart · ❌ Indomaret |
| **🇵🇭 Philippines [PHP]** | GCash `1008` · Maya `1007` · GrabPay `1006` · QR Ph `208` · BPI transfer `1011` · BPI online `735` · ECPay `5168` · Cebuana Lhuillier `5165` · LBC `5166` · M Lhuillier `5167` | ❌ 7-Eleven PH |
| **🇸🇬 Singapore [SGD]** | PayNow `424` · **PayNow QR via MOLPay** `736` · GrabPay `4763` · AXS Kiosk `1324` · SingPost SAM `5164` | — |
| **🇹🇭 Thailand [THB]** | PromptPay `1078` *(offline-payment section)* · Thai mobile banking `1326` | ❌ TrueMoney Wallet *(TrueMoney appears only as a **product** SEAGM sells, `776`)* · ❌ Rabbit LINE Pay |
| **🇻🇳 Vietnam [VND]** | **Credit/debit card only `537`, routed to Airwallex** | ❌ **MoMo · ZaloPay · VNPay** |
| **🇰🇭 Cambodia [USD]** | Acleda Bank `1303` · Acleda XPay `6000` · AMK Bank `1304` · AMK Online Card `6032` · Chip Mong `1305` · **Bakong KHQR** `1301` · Pi Pay `1064`/`1299` · eMoney `1302`/`6030` | ❌ Billed in **USD, not KHR** |
| **Rest of APAC** | HK: AlipayHK `738` · Greater China: Alipay `889` · JP: FamiPay `1216`, **Lawson konbini** `1215` · KR: Naver Pay `4765`, Payco `1240`, Happy Money `1231`, Culture Voucher `1233`/`4766`, Book Voucher `1234`, Teencash `1235`, Eggmoney `1236` · AU: **NPP/PayID** `1038` · MN: MonPay `1156`, Unitel DCB `5144`, Toki `5145` | ❌ KakaoPay · ❌ Toss · ❌ JKOPay · ❌ WeChat Pay |
| **Global** | PayPal `1222` · Paysafecard `1148` · Skrill `4844` · Atome `1051` · Apple Pay `361` · Google Pay `362` · Cryptocurrency `1352` · Cards [USD] `437` | — |

### Fraud posture — heavy, manual, and costing conversion

**Manual document KYC on card payments.** Article `1553`, **fetched and read by me**: *"A buyer who paid using a credit/debit card is required to do a one-time identity verification when requested by our team. **Failure to adhere to this requirement will result in SEA Gamer Mall rejecting the payment made, and the payment will be refunded.**"* Required: a selfie holding passport/ID with a handwritten 【SEAGM+DATE】 note; a card receipt or bank statement under 3 months old; **a photograph of the credit card** showing first four and last four digits, name and expiry. Driving licences not accepted. During review *"all of your purchased orders will be placed on hold."*

**Chargeback-abuse controls.** Article `1517`: *"Our **Risk Management Team** does regular checks and will suspend members… Our system is also equipped with a **machine learning algorithmic identity management system**."* Suspension triggers include *"Sharing of Payment accounts or credit cards with another member"* and *"Submitting fraudulent disputes for delivered orders."* And: *"Our support will also **temporarily suspend the account whenever a user submitted a dispute or claim**."*

**They absorb chargeback liability for their content partners.** Corporate site, verbatim: *"**Guaranteed No Chargeback & On-time Settlement** — Every transaction made via our site is guaranteed with all payment methods including Cards Payments."*

**Cross-border declines named in their own copy.** Article `1438` blames failures on *"Some debit/credit cards have restrictions on **cross-border usage**"* and tells customers to phone their issuer.

**Other stated friction:** refunds take *"up to thirty (30) days"* (Terms of Sale §7); balance disputes must be raised within 7 days and SEAGM's decision is *"final and binding"*.

**Pitch read:** a merchant that has answered card-fraud pressure with **manual document review and account suspension** rather than acquirer diversification and routing. They are eating dispute risk on behalf of publishers while paying for it in conversion and in one-star reviews.

### Complaints

**Trustpilot — SOURCED** (https://www.trustpilot.com/review/seagm.com, fetched 2026-09-20): **4.0 / 5 across 7,916 reviews.** 5★ 83% · 4★ 4% · 3★ 2% · 2★ 1% · **1★ 10%** (~790 reviews — high for a repeat-purchase digital-goods merchant).

Verbatim, from that page:
- *"My account had been suspended way too many times for the stupidest reasons, and it's so difficult for it to be unsuspended."* (Sept 10, 2026)
- *"I had to provide my ID (for Security Purposes, which I fully understand), but Support (with Live Chat) was SUPER fast"* (Aug 19, 2026)
- *"I bought 2 cards and both were stolen. I contacted support and they asked me to wait 5 days. Even though the listing says it's Instant delivery."* (Sept 14, 2026)
- *"the code they gave me is invalid. I contacted customer support for assistance, but I still hadn't received any response."* (Sept 16, 2026)

⚠️ `[UNVERIFIED — search summary only]` Summaries additionally described money deducted on failed transactions with 30-day refund waits, crypto payments refunded as store credit rather than cash, and customers not told upfront that card photographs would be required. Directionally consistent with the KYC policy verified at `1553`, **but do not quote them.**

**No Reddit threads located** — searches returned SEAGM's own help articles. **No public information found** for app-store review analysis.

### 💥 Corrections to the target list

The TAL records: *"PayPal, PaySafeCard, Acleda XPay, Chip Mong Bank; cards, online banking, e-wallets, cryptocurrency."*

- ✅ All four named items confirmed, visible as payment-logo `alt` attributes in the storefront footer.
- ❌ **Category error:** Acleda XPay and Chip Mong Bank are **Cambodian bank rails**, not gateways. The TAL lists them in the "Payment Gateway" column.
- ❌ **The actual processors are missing entirely** — **Stripe**, **MOLPay/Razer**, **Airwallex**. Those three are the commercially relevant incumbents.
- ❌ Also missing: Skrill, Atome, Apple Pay, Google Pay, the entire Korean voucher stack, and **Forter**.
- ⚠️ **The stub's app-store-trap warning does not apply** — the mobile app routes through `pay.seagm.com` in a React Native webview, not IAP.

**Net effect: the TAL understated this account materially.**

### Methodology notes

- ⚠️ **CSP is worthless here.** `www.seagm.com` returns only `frame-ancestors` — no `connect-src`, no `frame-src`, **no `form-action`**. `pay.seagm.com` returns **no CSP at all**. Per the standing lesson, that means CSP evidences nothing about redirect flows, and these flows *are* redirect-based (*"allow the payment gateway to re-direct you back to our website"*). **The entire PSP list rests on SEAGM's own named documentation, not on header inference.**
- **The help-centre search is client-side** — `help.seagm.com/hc/en/search?keyword=X` returns no server-rendered results, so keyword absence there is weak evidence. The section enumeration is stronger but not a complete census (see the hook caveat).
- **Per-market checkouts could not be rendered live.** Fetching `/en-my/`, `/id-id/`, `/en-ph/`, `/en-th/`, `/en-sg/`, `/en-vn/` from this egress returns an **identical USD footer** for all six. Routing is currency-keyed, not geo-keyed, and the currency cannot be forced without a session.

### What could NOT be established

1. **Which PSP processes which rail beyond the four named.** The acquirer behind FPX, DuitNow, Touch 'n Go, Boost, QRIS, GoPay, GCash, Maya, PromptPay, PayNow-direct, all eight Cambodian rails and the Korean voucher stack is **not disclosed anywhere public.**
2. **Whether Stripe is the primary card acquirer**, and whether cards are multi-acquirer routed.
3. **The `seagm.com/pay` payment-partner list** promised by the privacy policy — URL dead. **The single highest-value missing artefact; ask for it on a call.**
4. **Any audited revenue, GMV or processed-volume figure.** None exists. `[UNVERIFIED — search summary only]` aggregators surfaced "+16.94% net sales 2024" and "$13.2M annual revenue 2026" — **not fetched, not usable.** Same status for the Vincent Tan / Cyberventures investor colour.
5. **Current order volume** — derived from 2013/2016 milestones only.
6. **Approval rates, decline rates, chargeback ratio, MDR.** No public data.
7. **Any payment or e-money licence.** No public information found.
8. **Payment/finance decision-makers.** Not researched in this pass.

### Overall research confidence — **HIGH on architecture, NIL on financials**
The Forter deployment, the React Native webview finding, the 89-article enumeration, the Vietnam card-only routing to Airwallex, the Stripe/MOLPay article wording and the KYC policy were all fetched and read by me today. Trustpilot was fetched. What does not exist is any financial disclosure whatsoever — this is a private Malaysian company and **no revenue figure should appear in any outreach.**

</details>
