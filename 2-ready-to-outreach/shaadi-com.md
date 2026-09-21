# Shaadi.com

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 16 / 29 → 🟢 **Medium** — one point below ⭐, and an upward override was considered and declined. See the breakdown.
**Industry:** Matrimonial matchmaking — prepaid membership subscriptions · **HQ:** Mumbai, India — **People Interactive (India) Private Limited**, CIN U72900MH2000PTC124485 · **Researched:** 2026-09-21 · **First email sent:** —
**Motion:** ⚠️ **DISPLACEMENT — Juspay confirmed.** Never open with "you have no orchestration layer." Open on coverage and reach.

---

> ## 🎯 THE HOOK — they went to the CCI, the NCLAT and the Supreme Court to keep control of their own payment routing
>
> **Verified first-hand** in MediaNama, 1 March 2024. Shaadi.com was **delisted from the Google Play Store** over the Play billing policy, alongside Matrimony.com, Info Edge and TrulyMadly. **Anupam Mittal, quoted by name:**
>
> > *"In a blatant violation of the CCI order, Google has delisted some of the most well-known apps in India without any fore-warning… The govt needs to intervene now and direct CCI to ensure Google is in compliance with their order and immediately restore all apps that were delisted **including Shaadi.com**."*
>
> — https://www.medianama.com/2024/03/223-google-removes-apps-indian-companies/
>
> **Shaadi.com was an original complainant that triggered the CCI's investigation into Play billing**, and was a named appellant at the NCLAT in May 2024. The relief sought included stopping Google from *"levying any fee if a transaction is processed inside an app through third-party billing systems."*
>
> **No other account in this pipeline has publicly and expensively litigated for control of its own payment routing.** You do not have to sell the premise of orchestration to this company. They have already paid lawyers to defend it.
>
> ### And they won the architecture they were fighting for — verified by me today
>
> | Platform | In-app purchase billing? | Evidence |
> |---|---|---|
> | **iOS** | **YES — Apple IAP** | App Store declares *"In-App Purchases: Yes — 3 Month Gold Membership **$109.99**"* (US storefront) |
> | **Android** | **NO — zero Play billing products** | `play.google.com/store/apps/details?id=com.shaadi.android` contains **0 occurrences** of "In-app purchases". My own grep |
>
> **1 crore+ Android installs are funnelled out of the app to Shaadi's own web checkout, on Shaadi's own payment stack, with Google earning nothing.** That is the revenue orchestration can actually reach, and it exists *because* they fought for it.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Shaadi.com is India's best-known matrimonial matchmaking platform, operated by People Interactive (India) Pvt Ltd (Mumbai, incorporated 2000). It sells prepaid 3/6/12-month membership packages to Indians domestically and across the diaspora, from a **single global `.com` property** — there is no regional storefront estate.

**SimilarWeb traffic:** supplied by Prateek 2026-09-21, `shaadi.com` incl. all country domains, 69 countries. ⚠️ **Shares only — no absolute visit count was supplied**, so monthly transactions cannot be derived from traffic. Full data: `accounts/traffic/shaadi-com.md`.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|---|---|---|---|---|---|
| 1 | 🇮🇳 India | **73.04%** ▲3.13% | Debit card, credit card, netbanking, **UPI**, Paytm; offline cash/cheque at ICICI & SBI branches | ❌ RuPay and Amex not named · ❌ PhonePe/GPay/Amazon Pay not offered as wallets (only as UPI intent targets) | ✅ **People Interactive (India) Pvt Ltd** |
| 2 | 🇺🇸 United States | **15.04%** ▲5.71% | Cards via **Checkout.com**; **PayPal by redirect** | ❌ **No PayPal/Apple Pay/Google Pay on the documented web list** · ❌ ACH · ❌ BNPL | ❌ **None** |
| 3 | 🇨🇦 Canada | **3.83%** ▲**77.59%** | Same as US | ❌ Interac · ❌ local wallet | ❌ **None** |
| 4 | 🇬🇧 United Kingdom | 1.72% ▼22.69% | Same as US | ❌ Faster Payments · ❌ local wallet | ❌ **None** — *registry-confirmed*, see Section 2 |
| 5 | 🇦🇪 UAE | 1.50% ▼34.04% | Legacy offline only: Aramex Memo Express, UAE Exchange cash | ❌ mada/STC Pay · ❌ Tabby/Tamara · ❌ local cards | ❌ **None** |

⚠️ **The Gulf rows (UAE, Saudi, Qatar) are EMEA territory.** Shaadi is India-HQ'd so the *account* is APAC per `CLAUDE.md`; the Gulf traffic is corridor evidence, not an EMEA claim.

### Legal entities
- **People Interactive (India) Private Limited** (India) — CIN **U72900MH2000PTC124485**, RoC-Mumbai reg. 124485, incorporated **25-02-2000**, Active. Registered office: Film Centre Building, 68 Tardeo Road, Mumbai 400034.
- **No entity found in any other market.** US, Canada, UK, UAE, Australia, Singapore: none. The UK is **registry-confirmed** (Companies House searched directly, 20 results each for "shaadi" and "people interactive", none connected to this group). The others are "not found across four independent official sources", which is weaker — OpenCorporates 403'd and ACRA/UAE registries were unreachable.

### Known PSPs
**Routed behind Juspay** *(agent-sourced from the v10.64.0 Android APK's Juspay merchant config; I verified the Juspay namespace itself but not this routing table)*:
- **PayU** — dominant rail; cards, UPI, UPI QR, eMandate card + netbanking, TPV
- **BillDesk** — sole netbanking gateway inside Juspay
- **Paytm (PAYTM_V2)** — cards, UPI, UPI QR, UPI eMandate
- **Razorpay** — cards, **Amex exclusively**
- **Yes Bank (YES_BIZ)** — UPI, UPI QR, UPI autopay
- **LazyPay** — wallet/BNPL

**Integrated directly, outside Juspay** *(same source)*:
- **Checkout.com** — full Components/Flow SDK + Risk SDK; international cards, Google Pay, card vaulting. **Shipped late Apr / early May 2026.**
- **Paytm** — All-in-One SDK, direct
- **BillDesk** — direct, separate enum from the Juspay path
- **PayPal** — redirect only, no SDK bundled
- **Google Play Billing** — present in the APK despite no Play IAP products declared

❌ **Explicitly NOT in the stack:** Adyen *(3 raw hits were `alreadyEncoded` / `isCallAlreadyEnded` — a caught false positive)*, Stripe, Braintree, Worldpay, Cashfree, CCAvenue, Easebuzz, Pine Labs, Amazon Pay.

### Orchestration status
**⚠️ Regional orchestrator — JUSPAY CONFIRMED. Displacement motion.**

**Verified first-hand on Juspay's own CDN, 2026-09-21, with a control test:**

| URL | Result |
|---|---|
| `assets.juspay.in/hyper/bundles/in.juspay.merchants/shaadi/android/release/manifest.json` | **200** |
| `.../shaadi/web/release/manifest.json` | **200** |
| `.../shaadi/ios/release/manifest.json` | **200** |
| `.../notarealmerchantxyz123/android/release/manifest.json` | **403 AccessDenied** |

The control is what makes it conclusive — a fabricated merchant is refused, `shaadi` is served. Each manifest carries a merchant-specific `sdk_config.json`; I pulled it and it contains live UPI intent URIs: `upi://pay`, `phonepe://pay`, `paytmmp://pay`, `tez://upi/pay` (Google Pay), `credpay://upi/pay` (CRED Pay). Modules include `in.juspay.ec` (Express Checkout), `hyperpay`, `hyperupi`, `inappupi`, `upiintent`, `godel` (bank ACS automation), `dotp` (in-app OTP).

**Provisioned on Android, iOS AND web — the whole checkout surface.**

🚩 **The nuance that makes the pitch, not the obstacle:** Shaadi also hand-built a **second selector above Juspay**. The app's per-method gateway enums route to `CHECKOUT`, `PAYTM` and `BILL_DESK` as well as `JUSPAY`, server-driven via `api/pages/payment-gateway-config`. **Juspay orchestrates the India rail; an in-house layer reaches Checkout.com, Paytm and BillDesk outside it.** Two partial orchestration layers doing half a job each.

❌ **Not a Yuno customer** — zero occurrences of Yuno/y.uno in the APK dex strings. No Phase 0 stop.

### Buying signals
- 📋 **The Play billing litigation** — CCI complainant, NCLAT appellant May 2024, Supreme Court listing Nov 2025. Public, dated, and directly about payment routing control. https://www.medianama.com/2024/05/223-nclat-admits-appeal-kuku-fm-shaadi-com-google-play-store-billing-policy/
- 🔧 **The PSP mix changed materially in seven months** — Razorpay **dropped** from UPI, **Yes Bank added**, **PayU added** to cards, and a full **Checkout.com SDK shipped Apr/May 2026**. Someone owns a payments roadmap and is spending on it right now.
- 💰 **IPO exploration** — Bloomberg, 20 Nov 2025: early talks with bankers, **no advisers appointed, no DRHP filed.** Pre-IPO companies clean up their payment stack. https://www.storyboard18.com/brand-marketing/shaadi-com-in-early-talks-for-ipo-evaluates-timing-valuation-report-84509.htm
- 🤝 **One orchestration decision covers the whole group** — malayaleeshaadi.com and bengalishaadi.com serve a **byte-identical payments FAQ** on the same codebase, asking *"How can I purchase a Shaadi.com Premium Membership?"* Community sites are one platform, one checkout. Good for deal size.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Shaadi.com`.*

⚠️ **Read before drafting.**

1. **This is a DISPLACEMENT sequence.** Juspay is confirmed on Android, iOS and web. Per `/full-outreach` §6a and `apac-payments.md` §4: **never write "you have no orchestration layer"** and **never name the incumbent.** Open on coverage and reach.
2. **Lead with the two-layer problem, not the absence of a layer.** Juspay routes India across six gateways with failover; a hand-rolled selector reaches Checkout.com, Paytm and BillDesk outside it; ~22% of traffic (US/CA/UK/AU) gets one acquirer plus a PayPal redirect. That asymmetry is internal, factual and undisputable.
3. **The mandate-cancellation cluster is the strongest customer-pain evidence** (Section 5) and it is recent, sustained and multi-market. Use it.
4. **Do NOT claim a cross-border decline pattern.** Exactly one review supports it. It is a hypothesis for the call, not an observation for an email.
5. **Do NOT quote `shaadi.com/info/customer-relations/faq/payments`** — it names Bank of Punjab (merged 2005) and Bank of Rajasthan (merged 2010). It is ~15 years stale. Use the support-portal article instead.
6. **Do NOT quote a revenue or transaction figure.** Newest credible revenue is FY23 and today is Sept 2026; the transaction count is an assumption.
7. **Do NOT say Adyen, Stripe, Alipay, WeChat Pay, Amazon Pay or Simpl** — all were caught as false positives.
8. **EMI is contradicted by their own help centre** — one article says it exists on Diamond Plus/Platinum Plus, another says it exists only on VIP Shaadi. Don't assert it.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 16 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+2** | ⚠️ **NOT FOUND — ASSUMED ~43,000/month. [ASSUMPTION — not researched.]** Basis: FY23 revenue ~₹310 Cr ÷ an **assumed** ₹6,000 blended package price ÷ 12. The revenue input is itself derived (see Section 12); the package price has no public source. **Per the matrix rule, an assumption never rejects an account** — scored at the 40,000–49,999 band it implies and marked ⚠️. **Top manual action: confirm this number.** |
| Orchestration status | **+3** | ⚠️ **Juspay CONFIRMED — displacement.** Verified by me on Juspay's CDN with a 403 control test, across Android, iOS and web. Already orchestration-aware, so a shorter education cycle — but +3, not the +4 a greenfield account earns |
| 3+ countries | **+3** | ✅ Six markets above 1% traffic: India 73.04%, US 15.04%, Canada 3.83%, UK 1.72%, UAE 1.50%, Australia 1.03% |
| Multiple PSPs | **+3** | ✅ **Nine named** — PayU, BillDesk, Paytm, Razorpay, Yes Bank, LazyPay behind Juspay; Checkout.com, PayPal, Paytm direct |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Analyst reading, stated as such.** The US is 15.04% of traffic and the merchant's own enumerated online list is five **India** rails. No PayPal, Apple Pay or Google Pay on the documented web checkout. ⚠️ The matrix's named-rail list (UPI/QRIS/PayNow/FPX…) is APAC-oriented, so this is not a literal match — knock it to 0 if you disagree, which makes the account 13/29 |
| Recent expansion | **0** | ⬜ No new market launch found. The PSP churn and the Checkout.com build are recorded as buying signals instead — they are not market expansion |
| Payment issues reported | **+2** | ✅ **High and sustained.** The auto-renewal/e-mandate cluster runs 2023 → Aug 2026 across India, UAE, Canada, UK and US. Plus the merchant's own declined-but-deducted article and a self-documented 12-hour payment-notification lag |
| Funding >$10M | **0** | ❌ No round, secondary or M&A in 24 months. Last M&A was Frivil, Dec 2016; WestBridge invested ₹166 Cr in **2006** |
| High traffic outside home | **0** | ❌ India is **73.04%**, above the 60% threshold |
| Competitor using orchestration | **0** | ❌ **An explicit blank, not a miss.** No Indian matrimonial platform is publicly on any orchestrator. Juspay's and Hyperswitch's case-study walls were fetched and contain no matrimony or dating merchant |
| Payment job postings | **0** | ❌ Nine roles open Sept 2026 (iOS, data, PHP+Node, Node, Android, 2× APM, design, FDE) — **zero payments/billing roles**, no PSP named |
| **TOTAL** | **16** | 🟢 **Medium** |

**Tier:** 🟢 Medium (10–16).

**Upward override considered and DECLINED — reasoning in full.** The Play-billing litigation is the strongest single qualification signal in this pipeline, and there is no row in the matrix that scores "the prospect has publicly and expensively litigated for control of its own payment routing." That argues for ⭐. I declined it because **the one row that would justify the promotion is the one row nobody can source**: monthly volume is assumed, sits within ~10% of the rejection floor, and iOS IAP removes an unknown slice of it. Promoting a marginal-volume account on a qualitative signal would be score inflation, and this file already carries one analyst reading (the rail-gap row). **If volume confirms above 40,000/month on a call, this becomes ⭐ immediately and the litigation signal is the reason.**

**Phase 0:** PASSES on all five gates. Matrimonial platform, not a PSP. Not a Yuno customer (zero dex hits). Real online payment volume. India-HQ'd, in territory. Volume not *confirmed* under 40,000, so the gate does not fire.

### Source Notes

**✅ Verified first-hand by me (2026-09-21):**
- **Juspay merchant namespace** on `assets.juspay.in` — 200 on Android, iOS and web; **403 AccessDenied on a fabricated control merchant**; merchant `sdk_config.json` pulled and read, containing the five UPI intent URIs.
- **MCA MGT-7 annual returns**, read in the filed PDFs People Group publishes itself: FY21 turnover ₹2,347,079,083 / net worth −₹970,678,518; FY22 ₹2,601,684,499.2 / −₹1,106,015,005.02; FY23 **₹30,983,068,656** / −₹1,284,269,390.13. Fiscal-year mapping confirmed from the period dates in each filing.
- **The live payments support article** — *"We accept payment through all major banks in India. You can use any of the below options for online payments: 1. Debit Card 2. Credit Card 3. Netbanking 4. UPI 5. Paytm"* — https://support.shaadi.com/support/solutions/articles/48000755733-i-want-to-buy-a-membership-how-can-i-pay-
- **The declined-but-deducted article** — *"please mail your bank statement reflecting the payment deduction with us at help@shaadi.com"* — https://support.shaadi.com/support/solutions/articles/48000755563-i-need-help-as-my-payment-is-declined-but-the-amount-is-deducted
- **The MediaNama delisting article and the Mittal quote**, both verbatim.
- **The platform split** — Apple declares IAP (`In-App Purchases: Yes — 3 Month Gold Membership $109.99`, US); Google Play `com.shaadi.android` contains **0 occurrences** of "In-app purchases".
- **Apple seller of record = "People Interactive (I) Pvt. Ltd."** in **all six** storefronts checked (IN, US, GB, CA, AU, AE) via the iTunes lookup API.
- **The entity** — People Interactive (India) Private Limited named in both `shaadi.com/info/terms` and `/info/privacy`.
- **PCI posture** — *"payment instrument details processed through our payment gateway partners. We do not store full card numbers on our own systems."* **Plural.**
- **Domain estate** — `shaadi.co.uk`/`.in`/`.sg` do not resolve; `shaadi.ca` is parked at a domain auction; `.com.au`/`.ae`/`.us` are empty placeholders. **`shaadi.com` is the whole property.**
- **No CSP header on `www.shaadi.com`.**
- **The TAL audit** — 250 of 344 India-HQ rows (72.7%) carry "Juspay"; 263 of 1,215 rows overall; only **38 rows have any Payment Gateway value.**

**⚠️ Agent-sourced, NOT re-verified by me:**
- The entire **PSP routing table** (PayU/BillDesk/Paytm/Razorpay/Yes Bank/LazyPay) and the **Checkout.com SDK findings** — extracted from the v10.64.0 APK. Well-evidenced with class counts and live endpoints, but I did not decompile the APK myself.
- The **Feb→Sep 2026 PSP diff** and the Checkout.com ship date (narrowed to v10.45.0 absent / v10.48.1 present).
- The **complaint corpus** — 5,488 Play reviews, 353 ConsumerComplaints entries, ~1,100 App Store reviews.
- **UK Companies House** negative result.
- The **89 eMandate payment methods** and `auto_renew_opt_out_dialog` in the APK.

**❌ Contradictions I could not resolve — both recorded, neither picked:**
1. **Recurring vs prepaid.** The Terms contain **zero** hits for auto-renew, recurring, mandate, standing instruction or tokenisation, and there is no cancellation article — which reads as prepaid. But the APK carries **89 eMandate methods**, `AutoRenewalDetails` and an auto-renew opt-out dialog, **and the complaint corpus is dominated by users saying auto-renewal fired without consent.** The weight of evidence says **recurring is real and the Terms are stale** — but I could not confirm it from outside, and the earlier "prepaid, no recurring" reading in this session was wrong.
2. **EMI.** Support article 48001159010 says *"Currently, we don't have an EMI option for our membership plans… only for VIP Shaadi"*; article 48001158986 says *"you have an EMI option for our Diamond Plus & Platinum Plus membership"*. The app ships a full EMI rail (`EMIPayment$GatewayForEmi = [JUSPAY]`, `EmiPlansActivity`).
3. **Activation latency.** The stale FAQ says *"within 12 hours"* and *"sometimes it takes upto 12 hours for the payment notification to reach us"*; the current help centre says *"activated instantly"*.

### Success Case Alternatives
- **A diaspora-billing subscription business** — the profile match is the outbound corridor (India-acquired, US/CA/UK/Gulf cardholders), not the matrimonial vertical.
- ⚠️ **Do not reach for a matrimonial or dating case.** None exists: no Indian matrimonial platform is publicly on any orchestrator, confirmed against Juspay's and Hyperswitch's own case-study walls.

---

## Section 1: Website Traffic Analysis by Country

**Data source:** **Pasted SimilarWeb data, supplied by Prateek 2026-09-21** (resolution path 1 — the primary source). Scope: `shaadi.com` with "Include all country domains" ON, 69 countries. **No absolute visit count was supplied** — shares only.

| Rank | Country | Traffic Share | Change | Country rank | Visit duration | Pages/visit | Bounce |
|---|---|---|---|---|---|---|---|
| 1 | 🇮🇳 India | **73.04%** | ▲ 3.13% | #692 | 04:53 | 9.45 | 39.42% |
| 2 | 🇺🇸 United States | **15.04%** | ▲ 5.71% | #6,447 | 06:56 | 11.04 | 20.09% |
| 3 | 🇨🇦 Canada | **3.83%** | ▲ **77.59%** | #2,299 | 06:52 | 14.25 | 19.77% |
| 4 | 🇬🇧 United Kingdom | 1.72% | ▼ 22.69% | #9,568 | 05:15 | 6.91 | 34.17% |
| 5 | 🇦🇪 UAE | 1.50% | ▼ 34.04% | #2,220 | 03:50 | 5.88 | 42.19% |
| 6 | 🇦🇺 Australia | 1.03% | ▼ 24.91% | #7,477 | 06:28 | 10.83 | 34.50% |
| 7 | 🇸🇦 Saudi Arabia | 0.63% | ▲ **73.53%** | #2,428 | 03:16 | 12.61 | 62.81% |
| 8 | 🇩🇪 Germany | 0.53% | ▼ 0.45% | #25,499 | 05:13 | 8.66 | 23.30% |
| 9 | 🇶🇦 Qatar | 0.39% | ▲ **106.06%** | #203 | 13:54 | 34.42 | 16.70% |
| 10 | 🇫🇮 Finland | 0.35% | ▼ 0.08% | #4,232 | 21:03 | 20.67 | 3.71% |
| 11 | 🇳🇿 New Zealand | 0.32% | ▲ 31.98% | #3,925 | 02:19 | 6.28 | 36.67% |

**High priority (>5% share):** India, United States.

**The shape that matters: this is one diaspora corridor, not a market portfolio.** US + Canada + UK + Australia + NZ = **21.94%**; Gulf = **2.52%**. Per `apac-payments.md` §3 this is the *outbound* cross-border pattern — an APAC business billing its diaspora on a stack chosen for the home market.

⚠️ Qatar's 34.42 pages/visit and Finland's 21:03 duration are small-sample artefacts on sub-0.4% shares. **Do not build anything on them.**

**Domain resolution (checked by me):** no regional ccTLD estate exists. `shaadi.co.uk`, `shaadi.in`, `shaadi.sg` do not resolve; `shaadi.ca` is parked at a **domain auction** (whc.ca); `shaadi.com.au`, `shaadi.ae`, `shaadi.us` are near-empty placeholders. **Every diaspora market transacts against the single `.com`.**

---

## Section 2: Legal Entities & Local Presence

**Headquarters:** Mumbai, India. Incorporated **25 February 2000**.

| Country | Entity Name | Registration # | Source |
|---|---|---|---|
| India | **People Interactive (India) Private Limited** | **CIN U72900MH2000PTC124485** (RoC-Mumbai 124485) | https://www.indiafilings.com/search/people-interactive-(india)-private-limited-cin-U72900MH2000PTC124485 ; reconciled against the MGT-7 filings at https://people-group.com/ |
| United States | Not found | — | Web search, Apple seller-of-record, official contact pages |
| Canada | Not found | — | same |
| **United Kingdom** | **Not found — registry-confirmed** | — | https://find-and-update.company-information.service.gov.uk/search/companies?q=shaadi and `?q=people+interactive` — 20 results each, none connected to this group |
| UAE / Australia / Singapore | Not found | — | Free-zone registries and ACRA not reachable from this environment |

**Capital:** authorised ₹13.35 Cr; paid-up ₹12.62 Cr (30,580,779 equity + 95,651,495 preference @ ₹1). IndiaFilings and the MGT-7 reconcile exactly.
**Directors:** Anupam Mittal (DIN 00233657, 13,409,092 shares), Anand Murarilal Mittal (DIN 00375242, 6,703,545), Shobitha Annie Mani (DIN 07911078, WestBridge nominee). CS: Varsha Rohra.
**Ownership:** WestBridge Capital 44.38% / Anupam Mittal 30.26% / Anand Mittal 13.13% / others 12.23% `[UNVERIFIED — Wikipedia citing Inc42]`.
⚠️ **MGT-7 Section III declares 3 related companies but the name/CIN rows are blank in the published PDFs.** Recovering them needs a paid MCA pull.

### Cross-Border Gap Analysis

| Country | Top-10 traffic? | Local entity? | Domestic acquiring gated? | Cross-border risk |
|---|---|---|---|---|
| India | ✅ #1 (73.04%) | ✅ Yes | n/a — home market | None |
| **United States** | ✅ #2 (15.04%) | ❌ **No** | No regulatory gate | **HIGH** — cross-border acquiring, FX, issuer decline exposure |
| **Canada** | ✅ #3 (3.83%) | ❌ **No** | No | **HIGH** |
| **United Kingdom** | ✅ #4 (1.72%) | ❌ **No — registry-confirmed** | No | **HIGH** |
| UAE / Saudi / Qatar | ✅ (2.52% combined) | ❌ No | Verify per market | HIGH — and EMEA territory |
| Australia / NZ | ✅ (1.35%) | ❌ No | No | HIGH |

> **Warning: confirmed cross-border operation in the United States, Canada, the United Kingdom, Australia and the Gulf. No local entity exists in any of them.** Four independent primary sources agree: the Terms are a **single global contract** with the Indian entity under **exclusive Mumbai jurisdiction**; **Apple's seller of record is "People Interactive (I) Pvt. Ltd." in all six storefronts I checked**; the only address on any official page is Mumbai, and the grievance page's "USA/Canada" tabs are **empty**; the footer "USA/Canada/UK/Singapore/Australia/UAE" links are NRI *landing pages*, not country sites.

**No regulatory acquiring gate applies** — the diaspora markets are all open-acquiring jurisdictions. This is a **cost, FX and approval-rate** story, not a licensing one. Do not escalate the language.

---

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Region | PSP/Acquirer | Evidence Type | Source |
|---|---|---|---|
| India | **PayU** — cards, UPI, UPI QR, eMandate, TPV | `[Source Code]` Juspay merchant routing config in APK v10.64.0 | apkcombo → `com.shaadi.android` 10.64.0 |
| India | **BillDesk** — all netbanking inside Juspay; also a direct enum | `[Source Code]` same + `GatewayForNetBanking = [BILL_DESK, JUSPAY]` | same |
| India | **Paytm (PAYTM_V2)** — cards, UPI, UPI QR, UPI eMandate; also direct All-in-One SDK | `[Source Code]` same | same |
| India | **Razorpay** — cards, **Amex exclusively** | `[Source Code]` same | same |
| India | **Yes Bank (YES_BIZ)** — UPI, UPI QR, UPI autopay | `[Source Code]` same | same |
| India | **LazyPay** — wallet/BNPL | `[Source Code]` same | same |
| International | **Checkout.com** — cards + Google Pay + vaulting; `api.checkout.com/tokens`, `card-acquisition-gateway.checkout.com` | `[Source Code]` 490 `com.checkout.components.*` classes | same |
| Diaspora | **PayPal** — redirect only, no SDK bundled | `[Source Code]` sole URL `https://www.paypal.com` | same |
| iOS | **Apple IAP** | `[Checkout]` App Store listing, verified by me | https://apps.apple.com/us/app/shaadi-com-matrimony-app/id480093204 |

⚠️ **Every row in this table except the Apple one is agent-sourced from the APK and was not re-verified by me.**

**PCI:** `[Terms/Privacy Policy]` *"payment instrument details processed through our payment gateway partners. We do not store full card numbers on our own systems."*

### 3B. Payment Orchestrator

> **Regional orchestrator confirmed — JUSPAY. Displacement motion.**
> *"Confirmed orchestration-aware. The opening is coverage and international reach, not the case for orchestration itself."*

Evidence and control test in the Quick Look. **Provisioned on Android, iOS and web.** Present in every APK build checked from v10.37.0 (13 Feb 2026) to v10.64.0 (17–18 Sep 2026) with an identical `"clientId": "shaadi"` — **a live relationship at least 7 months old, not a stale logo.**

⚠️ **Zero public celebration of it.** Shaadi is absent from Juspay's customer-story wall and from all trade press. **You cannot write "as you've publicly shared."**

**Second layer, in-house:** per-method gateway enums (`CardPayment$GatewayForCard = [CHECKOUT, JUSPAY, PAYTM]`, `GatewayForNetBanking = [BILL_DESK, JUSPAY]`, `GatewayForUpiIntent = [JUSPAY, PAYTM]`) resolved server-side.

---

## Section 4: Alternative & Local Payment Methods

| Country | Method | Category | Status | Source |
|---|---|---|---|---|
| 🇮🇳 India | **UPI** | Bank A2A | **Active in checkout** | support article 48000755733 |
| 🇮🇳 India | UPI intent: PhonePe, Paytm, Google Pay, CRED Pay | Bank A2A | **Active** — verified by me in Juspay `sdk_config.json` | assets.juspay.in |
| 🇮🇳 India | **UPI Autopay / eMandate** | Recurring A2A | **Active** (APK: 89 eMandate methods via PayU/Paytm/Yes Bank) — ⚠️ contradicted by the Terms | APK v10.64.0 |
| 🇮🇳 India | Paytm wallet | Wallet | **Active in checkout** | support article |
| 🇮🇳 India | Netbanking | Bank transfer | **Active in checkout** | support article |
| 🇮🇳 India | Cards (Visa/MC; Amex via Razorpay) | Cards | **Active** | support article + APK |
| 🇮🇳 India | Cash/cheque at ICICI or SBI branch | Cash | **Active** — account numbers published | support article |
| 🇮🇳 India | **RuPay** | Cards | **Not found** | Never named on any property |
| 🇮🇳 India | **EMI** | Instalments | **Contradicted** — see Source Notes | support articles 48001159010 / 48001158986 |
| 🇺🇸🇨🇦🇬🇧🇦🇺 | Cards via Checkout.com | Cards | **Active** | APK |
| 🇺🇸🇨🇦🇬🇧🇦🇺 | PayPal | Wallet | **Active — redirect** (APK) but **absent from the documented method list** | APK vs support article |
| 🇺🇸🇨🇦🇬🇧🇦🇺 | **Apple Pay / Google Pay (web)** | Wallet | **Not found** on the documented web list | support article |
| 🇺🇸 | **ACH** · 🇨🇦 **Interac** · 🇬🇧 **Faster Payments** · 🇦🇺 **PayTo/BPAY** | Bank A2A | **Not found** | — |
| 🇺🇸🇨🇦🇬🇧🇦🇺 | **BNPL** | BNPL | **Not found** | — |
| 🇦🇪 | Aramex Memo Express, UAE Exchange cash | Cash | **Deprecated** — legacy FAQ only; UAE Exchange collapsed with Finablr ~2020 | stale FAQ |
| 🇦🇪🇸🇦 | **mada / STC Pay / Tabby / Tamara** | Local | **Not found** | — |

> **Warning: in the United States — 15.04% of traffic and the #2 market — the merchant's own enumerated online method list is five India rails.** The only international rails that exist are a card acquirer and a PayPal redirect, and neither appears in the customer-facing documentation.

---

## Section 5: Payment Issues & Customer Complaints

**The split is the point, and it is measured, not estimated.** Across 5,488 Play reviews, 353 ConsumerComplaints entries and ~1,100 App Store reviews: **roughly 1 in 100 complaints is a payment-rail failure.** The other ~99% are refunds, fake profiles, romance fraud and VIP mis-selling — commercially irrelevant. **Anyone pitching Shaadi on raw complaint volume will be caught.**

| Issue Type | Platform | Frequency | Date Range | Source |
|---|---|---|---|---|
| **Auto-renewal / e-mandate fired without consent; cancellation does not stick** | Play + App Store (IN, UAE, CA, UK, US) | **HIGH and sustained** | 2022 → **Aug 2026** | Play listing; apps.apple.com AE/CA/GB/US |
| UPI captured, membership not credited; merchant says "failed", bank statement says success | Web/UPI | Isolated but explicit | Feb–Mar 2022 | https://www.consumercomplaints.in/people-group-people-interactive-india-b100319 |
| Triple charge on a US-issued card, issuer identified it as duplicate authorisation | iOS (US) | Isolated | **24 Mar 2026** | apps.apple.com/us |
| **Merchant's own standing article for money captured on a declined transaction** | Web | Standing policy | current | support article 48000755563 |
| Self-documented **12-hour payment-notification lag** | Web | Standing policy | current (stale FAQ) | shaadi.com FAQ |

**Representative mandate complaints, verbatim:** *"I got to know that auto mandate is automatically activated"* (13 Jul 2026) · *"They save your UPI I'd to automatically renew your subscription… There's a hidden option where you can disable auto subscription but it'll automatically enables again"* (20 Feb 2025) · *"Even if you cancel auto renewal, it gets enabled automatically"* (23 Jan 2025) · UAE: *"they confirm i don't want to renew my subscription but the renewed without acknowledge me"* (5 Jul 2025) · Canada: *"they sent me different steps for different platforms but nothing of them worked"* (17 Jan 2026).

> *"Pattern of mandate-cancellation failure across five countries suggests mandate lifecycle is handled per-PSP with no unified view — precisely what a routing layer with consolidated mandate management consolidates."*

⚠️ **Cross-border declines: NOT a pattern.** Exactly one supporting review (18 Apr 2023: *"my bank don't do international transaction. This has stopped me from connecting with members"*) plus the March 2026 US triple charge. **Zero** currency-conversion complaints, **zero** complaints about being charged in INR. **Frame as a hypothesis, never as an observation.**

**Not reachable:** Reddit (403), Trustpilot (403), X/Twitter.

---

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | **1 Mar 2024** | **Delisted from Google Play over billing policy**; Mittal quoted by name | Payment Platform Dispute | https://www.medianama.com/2024/03/223-google-removes-apps-indian-companies/ |
| 2 | **10 May 2024** | **NCLAT admits Shaadi.com's appeal** against CCI's refusal of interim relief on Play billing | Litigation | https://www.medianama.com/2024/05/223-nclat-admits-appeal-kuku-fm-shaadi-com-google-play-store-billing-policy/ |
| 3 | **Apr/May 2026** | **Checkout.com Components SDK shipped** — absent v10.45.0 (9 Apr), present v10.48.1 (4 May) | Payment Infrastructure | APK diff `[agent-sourced]` |
| 4 | **Feb→Sep 2026** | **PSP mix changed** — Razorpay dropped from UPI, Yes Bank added, PayU added to cards | Payment Infrastructure | APK diff `[agent-sourced]` |
| 5 | **20 Nov 2025** | **IPO exploration** — early bank talks, no advisers, **no DRHP** | Funding | https://www.storyboard18.com/brand-marketing/shaadi-com-in-early-talks-for-ipo-evaluates-timing-valuation-report-84509.htm |

**Public payment RFP:** *No public payment-related RFP found.*
**Payment job postings:** *None.* Nine roles open Sept 2026, **zero** in payments/billing, no PSP named.
**Payment-adjacent licences:** *No public information found* — no RBI PA, PPI or PA-CB activity traceable.

---

## Section 7: Payment-Specific News

| # | Date | Headline | Relevance | Source |
|---|---|---|---|---|
| 1 | 1 Mar 2024 | Google removes Shaadi.com and peers from Play over billing | **The strongest buying signal on the account** | medianama.com |
| 2 | 10 May 2024 | NCLAT admits Kuku FM / Shaadi.com appeal | Shaadi litigating for routing control | medianama.com |
| 3 | 28 Mar 2025 | NCLAT upholds CCI's core findings against Google | Ongoing | `[UNVERIFIED — search summary only]` |
| 4 | Nov 2025 | Google/CCI/ADIF appeals admitted by Supreme Court | Ongoing | `[UNVERIFIED — search summary only]` |
| 5 | 20 Nov 2025 | Shaadi.com in early IPO talks | Pre-IPO stack cleanup | storyboard18.com |

> **REMOVAL / ARCHITECTURE CHANGE:** Shaadi.com's Android app carried **no Google Play billing products** as of 2026-09-21 (verified by me: 0 occurrences of "In-app purchases"), while iOS declares Apple IAP. `[INFERENCE, not confirmed]` they resolved the 2024 delisting via Google's consumption-only option — Android buyers are pushed to Shaadi's own web checkout.

---

## Section 8: Checkout Experience Audit

**Full live checkout flow not accessible.** `www.shaadi.com/payment` 302s to `/registration/user/login?go=…` (verified by me). Findings limited to publicly observable elements.

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | Own-hosted, multi-step, server-rendered legacy app **separate from the Next.js marketing site** | Fair | Historic chain `/payment/index` → `/payment/responseorder/my-cart` → `/payment/thankyou/…`; `pay.shaadi.com` is an AWS API Gateway |
| Guest checkout | **No — forced login** | Poor | Confirmed by the live 302 |
| Card input | Tokenized — Checkout.com client-side (`api.checkout.com/tokens`) or inside Juspay HyperSDK | Good | |
| Methods visible | Five: debit, credit, netbanking, UPI, Paytm | Fair for India, **Poor for 27% of traffic** | |
| Location-based method display | **No evidence.** Geo cookie `i2c=US\|USA` is set, but documented methods are India-only | Poor | |
| Instalment / EMI | **Contradicted** across two help articles; app ships an EMI rail | Poor | |
| 3DS | **Not detected.** Security FAQ mentions only "SSL and 128 Bit Encryption". Juspay `dotp` + `godel` modules imply native OTP/ACS handling | Unknown | Absence of evidence |
| PCI indicator | PSP tokenization, no card storage | Good | |
| Saved payment methods | Present — Checkout.com `rememberme`; complaints reference stored cards and stored UPI IDs | Fair | |
| Error message clarity | Poor — declined-but-deducted resolved by **emailing a bank statement** | Poor | |

⚠️ **CSP methodology note.** `www.shaadi.com`, `my.shaadi.com`, `api.shaadi.com` return **no `Content-Security-Policy` at all** — so **no `form-action` directive exists and header absence proves nothing** about which PSPs are in the redirect path. Every PSP claim rests on compiled binaries or Juspay's CDN, never on headers.

---

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|---|---|---|
| PCI DSS Level | **Not found** — zero PCI/DSS hits in the privacy policy, terms, payments FAQ, support portal or the entire v10.64.0 APK string set | — |
| Card data handling | *"payment instrument details processed through our payment gateway partners. We do not store full card numbers on our own systems."* | https://www.shaadi.com/info/privacy |
| Recommended Yuno integration | **SDK** — consistent with existing tokenized-PSP architecture | — |

*No direct PCI compliance documentation found publicly for Shaadi.com.*
`[INFERENCE, not confirmed]`: card data is tokenized client-side by Checkout.com or captured inside Juspay's HyperSDK webview, so PCI scope is plausibly SAQ-A / SAQ-A-EP rather than full Level 1. **Do not state as fact.**

---

## Section 10: Strategic Insights & Outreach Angles

> **Insight #1: They litigated for routing control, then built the architecture — and the international half is unfinished**
> **Evidence:** S6/S7 — CCI complainant, NCLAT appellant, Mittal quoted 1 Mar 2024 + S3A — Juspay routes India across six gateways while the US corridor gets one acquirer and a PayPal redirect.
> **Pain Point:** They spent years and legal fees establishing that they should control their own payment routing. They then built that control for India and left 22% of traffic on a thin international rail.
> **Yuno Value Proposition:** Extends the control they already fought for into the markets where they do not yet have it — global PSP and rail breadth beyond the home region, one integration.
> **Best Success Case:** A diaspora-billing subscription business — match on corridor, not vertical.
> **Outreach Angle:** They have already won the argument internally. The question is reach, not principle.
> **Suggested Subject Line:** *Six gateways for India, one for the US*

> **Insight #2: Mandate cancellation fails in five countries**
> **Evidence:** S5 — a sustained 2022→Aug 2026 complaint cluster across IN, UAE, CA, UK, US + S3A — 89 eMandate methods split across PayU, Paytm and Yes Bank.
> **Pain Point:** Mandates registered per-PSP with no unified lifecycle view. Users report opt-out re-enabling itself; the merchant's own Terms do not even document auto-renewal.
> **Yuno Value Proposition:** Consolidated mandate management and a unified view of failed and cancelled mandates across providers, instead of three PSP dashboards.
> **Best Success Case:** A subscription business with multi-PSP recurring.
> **Outreach Angle:** Their own reviews, in five countries, say the same thing — and it is a payments-architecture symptom, not a support one.
> **Suggested Subject Line:** *Auto-renew opt-out across three PSPs*

> **Insight #3: Money captured, membership not delivered — resolved by emailing a bank statement**
> **Evidence:** S5 — standing support article 48000755563 + the stale FAQ's *"sometimes it takes upto 12 hours for the payment notification to reach us"*, against the current help centre's *"activated instantly"*.
> **Pain Point:** An asynchronous, un-reconciled webhook path. The remedy of record is a human reading a customer's bank statement.
> **Yuno Value Proposition:** Unified webhook handling and reconciliation across providers, so capture-without-fulfilment is detected rather than reported by the customer.
> **Best Success Case:** Any merchant with multi-PSP reconciliation load.
> **Outreach Angle:** Quote their own article. It is the clearest statement of the problem anyone could write.
> **Suggested Subject Line:** *"Mail your bank statement to help@"*

> **Insight #4: The Android web funnel is the growing, addressable half**
> **Evidence:** S7 — Play listing declares no IAP (verified by me) while Apple declares IAP at $109.99 + S1 — 1 Cr+ Android installs.
> **Pain Point:** The half of the business they control runs on a login-walled legacy checkout with five India rails; the half Apple controls is taxed.
> **Yuno Value Proposition:** Every improvement to the web rail compounds, because that is the channel they chose and defended.
> **Best Success Case:** A consumer subscription business growing web checkout to escape store fees.
> **Outreach Angle:** The channel they won in court is the one running on the oldest infrastructure.
> **Suggested Subject Line:** *The checkout Android users land on*

### Quick Hits

**Email hooks:**
1. *"Your Android app has no Play billing products and your iOS app does — so the web checkout is carrying the half of the business you actually control."*
2. *"Your help centre resolves a captured-but-declined payment by asking the customer to email a bank statement."*
3. *"Six gateways route India. The US is 15% of your traffic and gets a card acquirer and a PayPal redirect."*

**Cold call openers:**
1. *"You took Google to the CCI over who controls your billing — I'm curious whether the international side ever got the same attention."*
2. *"I noticed auto-renew cancellation complaints from India, the UAE, Canada and the UK saying the same thing — is mandate handling split across providers?"*
3. *"You added a card acquirer and swapped a UPI gateway this year — is there a payments roadmap I should be talking to?"*

---

## Section 11: Similar Companies & Prospecting Pipeline

### 11A. Direct Competitors

| Company | Website | HQ | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---|---|---|---|---|---|---|
| **Matrimony.com** (BSE/NSE: MATRIMONY) | matrimony.com | Chennai | **₹460.0 Cr FY26**, 9.63 lakh paid subs, ATV ₹5,032 | India + NRI (8 countries) | **Plural unnamed "gateway partners"**, PayPal accepted, Apple SoR on iOS. **No PSP or orchestrator named in the 276-page AR** | https://img.matrimony.com/Matrimony_AR_web_8_40_pm_cef01a26b2.pdf |
| **Jeevansathi** (Info Edge, NSE: NAUKRI) | jeevansathi.com | Noida | ₹138.3 Cr FY26 revenue, +25.9% | India | **Untestable** — Akamai 403 on every path | https://www.infoedge.in/pdfs/Report_filings/InfoEdge_Annual_Report_2026.pdf |
| **Aisle** (Info Edge, 100%) | aisle.co | Bengaluru | ₹39 Cr FY26 billings, +30% | India | Not found | same |
| **TrulyMadly** | trulymadly.com | Delhi | Not public | India | **PayU + HDFC** (own privacy policy) + **live Paytm CheckoutJS**. **Zero Juspay footprint** | https://trulymadly.com/privacy |
| **Betterhalf.ai** | betterhalf.ai | Bengaluru | $11.01M raised | India | ⚠️ **Web funnel retired** — domain 302s to Play Store, `/pricing` 410 Gone | https://www.crunchbase.com/organization/betterhalf |
| **Muzz** | muzz.com | **London** | 21M+ members | Global Muslim diaspora | **Stripe** + Apple Pay + Google Pay + app stores | https://muzz.com/terms |
| **Dil Mil** | dilmil.co | **San Francisco** | ~1M+ users | US/CA/UK diaspora | Google Pay config found but **`enabled: false`, `environment: TEST`** — do not cite | dilmil.co bundle |

### 11B. Industry Peers
Indian consumer-subscription businesses billing a diaspora tail from an India-acquired stack — the shared payment pattern is **outbound cross-border recurring on a home-market stack**, not the matrimonial vertical.

### 11C. Companies Recently Adopting Payment Orchestration

*No public case studies found of direct competitors adopting payment orchestration.* Juspay's and Hyperswitch's own case-study walls were fetched and grepped: **no matrimony or dating merchant appears on either.** Adjacent only: Juspay open-sourced Hyperswitch (Mar 2025); Hyperswitch × Recurly subscription-billing partnership (Jul 2026).

**This is a blank, not a hit. It must not be written up as competitive urgency.**

### 11D. Prospect Scoring & Top Pipeline

| Rank | Company | Type | Key Markets | Priority | Top Signal | In TAL? |
|---|---|---|---|---|---|---|
| 1 | **Matrimony.com** | Direct | India + NRI ×8 | **P1** | **Listed. Discloses "Collection charges" ₹6.55 Cr (~1.42% of revenue) AND a payment-gateway receivable that rose 39% while revenue was flat. ~12% of revenue earned in foreign currency** | ❌ **MISSING — biggest gap** |
| 2 | **Jeevansathi** | Direct | India | P1–P2 | ₹138 Cr, +26%, listed parent | ❌ **MISSING** |
| 3 | TrulyMadly | Direct | India | P3 (on list) | Multi-PSP, no orchestrator — **TAL's "Juspay" tag refuted by its own privacy policy** | ✅ row 113 |
| — | Betterhalf | Direct | India | **Hold** | Verify shutdown / app-only first | ❌ |
| — | Dil Mil · Muzz | Diaspora | US/UK | **Not APAC** | US and UK HQ — route to AMER/EMEA | ❌ |

> 🎯 **Genuine prospecting find: Matrimony.com is not on the target list.** Listed, in territory (Chennai), ₹460 Cr, and it **publicly discloses payment-cost and settlement-float lines that Shaadi never will**. Recommend adding at P1.

---

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|---|---|---|
| Annual Revenue | **FY21 ₹234.71 Cr · FY22 ₹260.17 Cr** (filed) · **FY23 ₹3,098.31 Cr as filed** | **SOURCED** — MCA MGT-7, read by me in the PDFs at people-group.com |
| ⚠️ FY23 anomaly | **₹3,098.31 Cr is an 11.9× jump with no corporate event.** ÷10 gives ₹309.83 Cr (+19.1% YoY), consistent with Tracxn's ₹100–500 Cr band | **The filed figure is sourced; the ÷10 correction is an `[INFERENCE, not confirmed]`.** Both recorded; neither is safe to quote |
| Net worth | FY21 −₹97.07 Cr · FY22 −₹110.60 Cr · FY23 −₹128.43 Cr | SOURCED — MGT-7. **Structural**, from redeemable preference capital, not distress |
| Profit/loss | FY22 loss ≈ ₹13.53 Cr · FY23 loss ≈ ₹17.83 Cr | **DERIVED** from net-worth deltas (paid-up capital unchanged). FY22 matches Inc42's ₹13.5 Cr exactly, validating the method |
| Average Transaction Value | ₹5,200–₹6,900 (India, Apple IAP tiers); $109.99–$189.99 (US) | Apple storefronts |
| **Monthly transaction count** | **⚠️ NOT FOUND — ASSUMED ~43,000/month. [ASSUMPTION — not researched.]** Basis: ~₹310 Cr ÷ ₹6,000 blended package ÷ 12. **Sensitivity: ₹4,000 → 64,600 · ₹8,000 → 32,300.** On the hard-sourced FY22 ₹260 Cr: ₹6,000 → 36,100 | **Neither input is fully sourced** — the revenue is derived and the package price has no source. Per the disclosure rule this is an **assumption and must never trigger rejection** |
| **Billing unit** | **One transaction per prepaid 3/6/12-month package**, not per month. A 12-month Platinum member = 1 transaction/year | Plan taxonomy, shaadi.com |
| Active users | *"3.5 crore (35 million) people all over the world"* — cumulative registered, **page visibly stale** | https://www.shaadi.com/info/introduction/about-us |
| Primary currency | INR. Apple prices in local currency per storefront; **web checkout currency NOT ESTABLISHED** | |
| Top markets by revenue | **Not disclosed** | |
| **Billing channel split (web vs app store)** | **NOT ESTABLISHED — the largest single unknown.** iOS is Apple-billed; Android carries no Play billing products; web is live and promoted. The proportions are unknown | |

*No public revenue/GMV data found for FY2024–FY2026. Business case sizing requires a discovery call.*

---

### Overall Research Confidence

**MEDIUM-HIGH on architecture, LOW on financials and volume.**

**Traffic data was SUPPLIED by Prateek** (SimilarWeb, 2026-09-21) — the strongest of the three resolution paths — but as **shares only with no absolute visit count**, so it cannot drive a volume derivation.

**Strong coverage:** the orchestration verdict (verified by me with a control test), the entity and cross-border position (four independent primary sources), the litigation history (verified verbatim), the platform split (verified by me on both stores), filed financials to FY23 (read in the filings).

**Weak coverage:** the PSP routing table and Checkout.com findings are agent-sourced from an APK I did not decompile. Financials stop at FY23 — **three years stale**. The web checkout was never observable (login-gated, no Wayback for much of the run). Volume is an assumption. Reddit, Trustpilot and X were all 403.

**One conclusion in this session was reversed.** An early read of "greenfield" was wrong: I had correctly established that the TAL's Juspay column is a bulk default (72.7% of India rows), then over-generalised from the column's unreliability to this row. Juspay is real and proven. **A bulk default can still be accidentally correct — the column being untrustworthy is a reason to verify, not a reason to disbelieve.**

---

### Manual Research Recommendations

> **Area:** Monthly transaction count — **the only row that can reject this account**
> **Why it matters:** The estimate straddles the 40,000 floor and both inputs are soft. It also gates the tier: confirm >40,000 and the litigation signal justifies promoting this to ⭐.
> **Suggested manual action:** Ask on the call — paid subscriber count and average package price. Two numbers settle it.

> **Area:** Web checkout currency and method set for diaspora users
> **Why it matters:** Whether a US member is billed in USD or INR determines whether the pitch is FX and approval rate, or approval rate alone. Insight #1 depends on it.
> **Suggested manual action:** Register a free account from a US IP and walk to the payment page. Every logged-out avenue is exhausted.

> **Area:** Whether auto-renewal is live on web, or only in-app
> **Why it matters:** It decides whether the mandate angle (Insight #2) is the lead or a secondary.
> **Suggested manual action:** Same logged-in session — check for an auto-renew toggle at checkout.

> **Area:** Add **Matrimony.com** to the target list at P1
> **Why it matters:** Listed competitor, in territory, ₹460 Cr, and discloses payment-cost lines no private peer will.
> **Suggested manual action:** Create the stub; the FY2025-26 annual report is the research starting point.

> **Area:** The TAL's Payment Orchestrator column
> **Why it matters:** 250 of 344 India rows say "Juspay" as a bulk default. It was right here and wrong for TrulyMadly. **It is not evidence in either direction and should not be trusted without verification on any account.**
> **Suggested manual action:** Treat every "Juspay" cell as a hypothesis. Juspay's CDN namespace check is a fast, reliable test — see Section 3B.

---

### Appendix: All Source URLs

**Traffic:** SimilarWeb supplied 2026-09-21 → `accounts/traffic/shaadi-com.md`
**Entity/financial:** https://www.indiafilings.com/search/people-interactive-(india)-private-limited-cin-U72900MH2000PTC124485 · https://people-group.com/docs/PIIPL-MGT-7-annual-return-1.pdf · `-2.pdf` · `-3.pdf` · https://find-and-update.company-information.service.gov.uk/search/companies?q=shaadi
**Orchestrator:** https://assets.juspay.in/hyper/bundles/in.juspay.merchants/shaadi/android/release/manifest.json · `/web/release/` · `/ios/release/` · `/android/release/sdk_config.json` · https://juspay.io/customer-stories
**Methods/support:** https://support.shaadi.com/support/solutions/articles/48000755733-i-want-to-buy-a-membership-how-can-i-pay- · `/48000755563-…` · `/48001159010-…` · `/48001158986-…` · https://www.shaadi.com/info/customer-relations/faq/payments · https://www.shaadi.com/info/terms · https://www.shaadi.com/info/privacy
**Apps:** https://apps.apple.com/us/app/shaadi-com-matrimony-app/id480093204 · `/in/` · https://play.google.com/store/apps/details?id=com.shaadi.android
**News/litigation:** https://www.medianama.com/2024/03/223-google-removes-apps-indian-companies/ · https://www.medianama.com/2024/05/223-nclat-admits-appeal-kuku-fm-shaadi-com-google-play-store-billing-policy/ · https://www.storyboard18.com/brand-marketing/shaadi-com-in-early-talks-for-ipo-evaluates-timing-valuation-report-84509.htm
**Complaints:** https://www.consumercomplaints.in/people-group-people-interactive-india-b100319
**Competitors:** https://img.matrimony.com/Matrimony_AR_web_8_40_pm_cef01a26b2.pdf · https://www.infoedge.in/pdfs/Report_filings/InfoEdge_Annual_Report_2026.pdf · https://trulymadly.com/privacy · https://muzz.com/terms

</details>
