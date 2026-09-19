# KKday

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 22 / 29 → ⭐ **High Priority** — second-highest in the repo
**Industry:** Travel-experiences marketplace (tours, activities, attraction tickets) · **HQ:** Taipei, **Taiwan** · **Researched:** 2026-09-19 · **First email sent:** —
**Motion:** ⚠️ **DISPLACEMENT** — **Juspay is confirmed incumbent, from Juspay's own website.** Read Section 2 before drafting a single line.

---

> ## ⛔ THEY ALREADY BOUGHT ORCHESTRATION — AND IT STOPPED AT HONG KONG
>
> **✅ Verified by me directly on Juspay's own site**, stated twice on the same page:
> > *"The platform powers payments for Singapore Airlines, IndiGo, SpiceJet, and Air India alongside global travel platforms including Agoda, MakeMyTrip, Etraveli Group, **KKday**, Tiket.com, and Wego."*
> > *"Travel platform customers include Agoda, MakeMyTrip, Etraveli Group, **KKday**, Tiket.com, and Wego."*
>
> **Corroborated inside KKday's own code:** the bundle carries `payment_pmch_name_JUSPAY_CREDIT_CARD_HKD`, plus `BookingForm_JuspayCreditCardMonthPlaceholder`, `...YearPlaceholder` and `...CVC` — **Juspay is rendering KKday's card-entry fields**, which is a hosted-fields SDK integration, not a passthrough.
>
> 📌 **And it is deployed on exactly ONE channel out of roughly 400: Hong Kong cards.** Taiwan still goes direct to TapPay, Japan direct to GMO, Korea direct to KCP/Toss/iamport, Malaysia direct to 2C2P, Vietnam direct to OnePay, and the long tail direct to **three separate Stripe entities and four Adyen entities.**
>
> **The opening is therefore not "you should orchestrate." It is: "you already decided to, and it stopped at Hong Kong."** Either it did not expand, or it could not.
>
> ⛔ **NEVER NAME JUSPAY IN OUTREACH.** It is on the never-name list and the displacement rule forbids naming the incumbent. Use the knowledge to avoid saying anything that implies they lack a routing layer.

---

> ## 🎯 THE HOOK — a Taiwanese platform whose Taiwanese customers get charged a foreign transaction fee
>
> **✅ Verified verbatim by me** on Money101 (Taiwan's main card-comparison site), table dated **資料更新：2026年8月**:
>
> > 「※**部分KKday交易可能由境外機構收單，持卡人仍可能被收取國外交易服務費。**」
> > *"Some KKday transactions may be acquired by **offshore institutions**; cardholders may still be charged a **foreign transaction service fee**."*
>
> And in the same article:
> > 「**即使KKday訂單以新台幣計價**，如果發卡銀行將交易認定為跨境交易，**仍可能收取約1.5%的國外交易服務費**；若交易由**台灣收單且以新台幣結算**，則不一定會產生海外交易手續費。」
>
> **A mainstream Taiwanese finance site has to warn Taiwanese cardholders, in August 2026, that a TWD-priced booking on a Taiwanese platform may be acquired offshore and carry ~1.5%.**
>
> ### And the mechanism is visible in KKday's own channel IDs
> `SG_STRIPE_CREDIT_CARD_TWD` · `JP_STRIPE_CREDIT_CARD_TWD` · `SG_STRIPE_CREDIT_CARD_3D_OTHER_TWD` · `STRIPE_CREDIT_CARD_NTW_3D_TWD`
>
> **A TWD transaction routable through the Singapore or Japan Stripe entity instead of TapPay's Taiwan acquiring.** That is approval rate *and* customer trust, both measurable, and it is their own naming convention saying it.
>
> 📌 **The same complaint is seven years old.** A 2019 PTT thread records a user billed NT$3,163 against a NT$3,116 booking and refunded only NT$3,116 — short by the fee — with the card company explaining 「**對方公司在香港**」, *the counterparty entity is in Hong Kong*.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Taiwan's largest travel-experiences marketplace — 350,000+ products across 92 countries, ~US$200M raised, 900+ staff. A two-sided business: money in from travellers in 18 currencies, money out to thousands of local suppliers by international wire.

**SimilarWeb total visits:** **Not obtained.** No data supplied, and `www.kkday.com` is **fully behind Cloudflare Bot Management** (403 `cf-mitigated: challenge` to curl *and* WebFetch, every path including `/robots.txt`). Country profile unverified; **no split invented.**

### 🗝️ How this account was cracked, and it is a technique worth reusing
The site is unreachable — but **KKday's entire internal payment-channel routing table is embedded in the i18n string table of its Nuxt bundle**, recoverable from a Wayback capture. **Roughly 400 channel identifiers**, each following the convention:

`{PLATFORM}_{ACQUIRING_ENTITY}_{PSP}_{METHOD}_{CURRENCY}`

multiplied across `APP_`, `IOS_`, `ANDROID_`, `EC_`, `APP_CLIP_`, `B2D_`, `FINEDAY_`, `JKO_MINI_` and `MINI_` platform variants. **That is affirmative architectural evidence of the whole stack, from a site nobody could log into.**

### Known PSPs — roughly 16 providers across 7+ acquiring entities
| Provider | Role |
|---|---|
| **Stripe** | The workhorse — **three separate entities (JP, SG, MY)** plus an unprefixed one. Cards, Apple/Google Pay, Alipay, GrabPay across ~17 currencies |
| **Adyen** | `AU_`, `HK_`, `MY_`, `SG_`, `KR_ADYEN_KCP_` — cards, GrabPay, WeChat Pay, MoMo, UnionPay |
| **TapPay** (TW) | Taiwan card acquiring, Apple Pay, 國民旅遊卡. **Note `TW_TAPPAY_DYNAMIC_3D` — dynamic 3DS step-up built in-house** |
| **2C2P** | HK card instalments; the whole Malaysia stack (FPX, Touch 'n Go, Boost, Atome, GrabPay) |
| **GMO PG** (JP) · **NHN KCP** (KR) · **Toss Payments** (KR) · **iamport/PortOne** (KR, PAYCO only) | Domestic acquiring |
| **Juspay** | ⚠️ **Orchestrator — HKD cards only** |
| **PayDollar/AsiaPay** (HK Octopus) · **OnePay** (VN) · **VNPAY** (B2D only) · **PayPal** (HK only) | Regional |
| **Citibank direct** (+ Macau, Vietnam, **Citi Pay with Points**) · **Fubon direct** · **Taishin via Leadbest** | **Bank-direct acquiring** |
| **Ant International / Alipay+** | GCash PH — label reads *"GCash (Alipay+™ Partner)"* |
| **DataDome** | Bot/fraud defence, first-party subdomain |

❌ **Sourced absence across the full 400-key catalogue:** NewebPay 藍新 · ECPay 綠界 · O'Pay · ESUN · CTBC · Checkout.com · Worldpay · Braintree · Cybersource · Omise · Razorpay · Xendit · Midtrans · Airwallex · PayerMax · dLocal.

⚠️ **Calibration:** a channel ID proves the integration was **built**, not that it is **live today**. Some are certainly legacy. Checkout is Cloudflare-blocked so live availability is unverifiable.

### 🇮🇳 INDIA IS DISPLAY-ONLY — the sharpest gap, and it is Prateek's market
- **INR is in the currency switcher.** It was **added between Jan 2024 and Sep 2026** — KKday's own help article listed 17 currencies in Jan 2024, the identical set minus INR; the live switcher now has 18.
- **`/en-in` and `/hi` storefronts both exist.**
- **There is not one Indian payment channel in the entire catalogue.** No UPI, no Indian card acquirer, no netbanking, nothing.

📌 **An Indian traveller sees ₹ pricing and is then routed to a Singapore or Japan Stripe entity on a foreign card.** They built the storefront and the currency and never built the rails.

### 🇮🇩 Indonesia is the same shape
**Two storefronts (`/id` and `/en-id`), IDR pricing, and card-only acceptance.** ❌ No QRIS, GoPay, OVO, DANA, ShopeePay or virtual account. In a market where QRIS and VA are how people actually pay, that is a conversion floor.

### 🇹🇼 The Taiwan contrast with EVA Air — and KKday's own hole
**Direct answer to the calibration question: the contrast is real and stark.** KKday carries the deep Taiwanese set EVA Air lacks entirely — **LINE Pay, JKOPAY 街口, Pi Wallet, PXPay Plus, and 國民旅遊卡** (the Civil Servant Travel Card, about as Taiwan-specific as a rail gets). **A Taiwanese consumer marketplace behaves like one; the flag carrier does not.**

**But KKday's Taiwan set has its own sourced hole:** ❌ no 超商代收, no 虛擬帳號/ATM 轉帳, no 信用卡分期, no Taiwan Pay. And the asymmetry is telling — **they built instalments for Hong Kong and ATM/bank transfer for Vietnam. Just not for their home market.**

### 💸 The supplier payout leg — the under-defended flank
- **Portal:** `scm.kkday.com` (供應商登入), plus `b2d.kkday.com` and `kkpartners.kkday.com`.
- **Rail: cross-border SWIFT wire.** Onboarding collects bank account name/number/**type** (`普通`/`当座`/`储蓄`), **bank code**, **branch code**, beneficiary bank, and **`merchant_register_swift_code`**.
- **FX burden sits on the supplier**, verbatim: *"Verify the provided bank account's ability to receive the selected currency."* Each supplier nominates a settlement currency and must hold an account that can receive it.
- ❌ **No supplier wallet, balance, netting or on-demand withdrawal** — grepped for `payout|settle|remit|withdraw|balance|wallet`, nothing. **Every supplier payment is a discrete cross-border wire with its own correspondent fee and FX spread.**
- **Scale: 5,000+ rezio suppliers + 3,000+ Marketplace merchants across 56 nationalities.**

### 🔴 Three restructurings in eighteen months — the cost-to-serve trigger
- **Early 2025:** 38 voluntary redundancies
- **June 2025:** **~15% of headcount (~135–140 people)**, explicitly targeting **IT, customer service and operations**. Reason given: 「跨境旅遊的報復性紅利逐漸消失」 — the revenge-travel dividend fading
- **August 2026:** a **third** restructuring — 「一年半內已三度重整」

> 📌 **They cut IT, CS and operations by 15%, then cut again — while hand-maintaining 400 channel rows and thousands of monthly SWIFT wires. Cost-to-serve and engineering relief is a far more credible opening than approval-rate uplift.**

### Buying signals
- 💰 **~US$70M raised Dec 2024** (Cool Japan Fund, Taiwan National Development Fund, Chang Hwa Bank VC, Darwin Venture), cumulative ~US$200M, **earmarked for APAC M&A**
- 📉 **Three restructurings in 18 months**
- 🏦 **IPO in preparation, no timetable** — and evaluating **Tokyo** as well as Taiwan, via the TSE Asia Startup Hub
- 🆚 **Klook — their direct competitor — consolidated on Adyen** with **direct acquiring in Hong Kong** and *"speedy local currency settlements and a boost in authorization rates"* as the stated benefit
- 🔴 **`help.kkday.com` is DOWN right now** — ✅ I verified **HTTP 530** myself. Their entire public help centre, including every payment and refund article, is unreachable today.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach KKday` to draft the 12-touch sequence.*

**Seven instructions — this is a displacement motion and the rules are strict:**
1. ⛔ **NEVER imply they lack orchestration.** Juspay is live. One careless sentence ends the thread.
2. ⛔ **NEVER name Juspay, or any competitor.** The displacement rule forbids naming the incumbent.
3. **Open on the offshore-acquiring-on-domestic-currency observation.** It is third-party sourced, dated August 2026, about their home market, and it costs their own customers 1.5%.
4. **India is the second observation and it is Prateek's territory** — INR in the switcher, two storefronts, zero Indian rails.
5. **The cost-to-serve angle beats the approval-rate angle here.** Three restructurings aimed at IT, CS and ops, against 400 hand-maintained channel rows.
6. **The payout leg is the under-defended flank** — thousands of SWIFT wires, supplier-nominated currencies, no wallet, no netting. Most orchestration pitches ignore payouts.
7. **The Klook comparison is available but handle it carefully** — Adyen's own release states the authorisation-rate benefit. **Name what Klook did; never imply Klook is a Yuno customer.**

**Never claim:** that KKday is on TapPay's public reference list (**I checked — "kkday" appears zero times** on that page), the T+25 supplier payout cycle (SSO-gated, unverified), the Trustpilot "G12 gateway error" (unverified), or any GMV figure — **none is published.**

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 22 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ⚠️ **Awarded on scale — no GMV figure is published anywhere.** What is verified: **350,000+ products, 92 countries, ~US$200M raised, 900+ employees, 8,000+ suppliers**, and KKday's own statement of **record monthly GMV in Aug 2024**. **The gate cannot fire — no sourced sub-40k figure exists** — and a marketplace at this scale clears 100k/month comfortably. **But this is scale inference, not a number.** |
| Orchestration status | **+3** | ⚠️ **Regional orchestrator incumbent — Juspay, confirmed from Juspay's own site AND from KKday's own bundle.** Per the matrix that is the **+3 displacement band**. **Deployed on one channel out of ~400.** |
| 3+ countries | **+3** | ✅ **24 locales, 18 currencies, 92 countries** — extracted from their own `hreflang` alternates and currency-switcher object. |
| Multiple PSPs | **+2** | ✅ **The best-evidenced PSP row in this repo by a distance** — roughly 16 providers across 7+ acquiring entities, all from their own channel catalogue. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Sourced absence from a 400-key catalogue.** **India: INR priced, two storefronts, zero Indian channels. Indonesia: two storefronts, IDR priced, card-only.** Plus the home-market hole — no 超商代收, ATM, instalments or Taiwan Pay in Taiwan, while both instalments (HK) and ATM (VN) exist elsewhere in the same catalogue. |
| Recent expansion | **0** | ⬜ **Not awarded.** The Dec 2024 raise is earmarked for APAC M&A and the Jalan/Tabelog supply partnerships are real, but **no verified new market entry** — and **three restructurings in 18 months point the other way.** |
| Payment issues reported | **+2** | ✅ **Verified by me.** The Money101 warning dated Aug 2026; a Google Play review reporting **five separate authorisations succeeding at the issuer while KKday's front end reported failure** — an auth/capture state-reconciliation break across a multi-PSP stack, the most expensive failure mode in a hand-rolled router; and **`help.kkday.com` returning HTTP 530 today**. |
| Funding >$10M | **+2** | ✅ **~US$70M announced 5 Dec 2024**, taking cumulative raised to ~US$200M. Investors include **Cool Japan Fund** and Taiwan's **National Development Fund**. ⚠️ Round labelling conflicts between sources (Series C vs D); **valuation explicitly undisclosed.** |
| High traffic outside home | **0** | ⬜ No traffic data. |
| Competitor using orchestration | **+2** | ✅ **Klook — KKday's direct competitor — selected Adyen as its APAC payments partner**, per Adyen's own press release, covering HK, SG, PH, ID, MY including Dragonpay OTC cash, with **direct acquiring in Hong Kong** and *"a boost in authorization rates"* as the stated benefit. |
| Payment job postings | **0** | ⬜ Not found. |

**Tier: 22 / 29 → ⭐ High Priority.** No override applied. **Second-highest score in the repo, behind ANA's 23.**

### Source Notes
- ✅ **Juspay's customer claim was verified by me** on Juspay's own page, appearing twice. **Also useful competitive intel from the same page: Juspay names Singapore Airlines, IndiGo, SpiceJet, Air India and LATAM as airline customers, and states it is pre-integrated with Amadeus, Sabre and Navitaire.**
- ✅ **The Money101 offshore-acquiring warning and the 1.5% passage were verified verbatim by me**, including the 資料更新：2026年8月 date stamp, and that **JKOPAY is a live checkout option**.
- ✅ **`help.kkday.com` HTTP 530 verified by me** on 2026-09-19.
- ⚠️ **The 400-channel catalogue, the currency/locale lists, the supplier onboarding fields and the payout analysis are all agent-sourced** from Wayback captures of the Nuxt bundle. **Not re-extracted by me** — but the technique is reproducible and the evidence is machine-readable.
- 🚩 **A claim the agent correctly refused to let stand:** a search summary asserted KKday is a named TapPay reference customer. **The agent fetched that page and found "kkday" appears zero times.** ✅ TapPay is confirmed anyway — by KKday's own `TW_TAPPAY_*` channel IDs, which is stronger evidence.
- 🚩 **A second correction the agent made against a search summary:** a summary claimed KKday had completed Taiwan domestic acquiring agreements so the 1.5% fee no longer applies. **That is contradicted by the Money101 page actually fetched**, which is more recent and explicitly hedges. **Rejected.**
- ⚠️ **`kakao`, `naver` and `wechat` also appear in the bundle as SOCIAL LOGIN providers.** Do not misread them as payment methods — another entry for the false-positive list.
- ❌ **Privacy policy and T&Cs unreachable** — 403 to every method, and **zero Wayback snapshots for the entire `/static/` prefix**. The usual Taiwanese "金流服務商 named in the privacy policy" route was closed.
- ❌ **GMV, revenue, take rate, valuation: none published.**
- ❌ **Supplier payout cycle is SSO-gated** behind a Google sign-in wall. The reported T+25 monthly cycle and a currency-matching constraint are **unverified**.

### Manual Research Recommendations
> **1. Ask the discovery question directly: what share of TWD volume is acquired in Taiwan versus offshore?** Evidence says partial, but the split is not establishable from outside. **This is the single best opening question for a call.**
> **2. Get behind Cloudflare to the live checkout** and confirm which of the ~400 channels are actually enabled, and in what order.
> **3. Establish whether the Juspay deployment is growing or stalled.** It determines whether this is a displacement or an expansion conversation.
> **4. Verify the supplier payout cycle** — someone with a supplier login could settle it in a minute.

---

## Executive Summary

KKday is Taiwan's largest travel-experiences marketplace — 350,000+ products, 92 countries, ~US$200M raised, 8,000+ suppliers — and at **22/29 it is the second-highest-scoring account in this repo**. It is also **not a greenfield account: Juspay is confirmed incumbent from Juspay's own website and from KKday's own code**, which means the displacement rules apply and the incumbent must never be named. What makes it interesting is that the orchestration they already bought **is deployed on exactly one channel out of roughly four hundred** — Hong Kong cards — while Taiwan still goes direct to TapPay, Japan to GMO, Korea to KCP and Toss, Malaysia to 2C2P, and the long tail to three separate Stripe entities and four Adyen entities. That entire routing table was recovered from the i18n string table of their own JavaScript bundle, because the site itself is behind Cloudflare and unreachable. The sharpest hook is that **a mainstream Taiwanese finance site still warns, in August 2026, that a TWD-priced booking on this Taiwanese platform may be acquired offshore and carry a ~1.5% foreign transaction fee** — and KKday's own channel names show exactly how, with TWD transactions routable through Singapore and Japan Stripe entities rather than Taiwan acquiring. Behind that sit two markets that are **display-only**: India has INR pricing, an `/en-in` and a `/hi` storefront, and **not one Indian payment channel**; Indonesia has two storefronts and card-only acceptance in a QRIS market. And the under-defended flank is the payout leg — **thousands of monthly cross-border SWIFT wires to suppliers across 56 nationalities, in supplier-nominated currencies, with no wallet, no netting and no withdrawal layer** — operated by a team that has been through **three restructurings in eighteen months**, the largest of which explicitly targeted IT, customer service and operations.

</details>
