# Moonshot AI (月之暗面) / Kimi

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 22 / 29 → ⭐ **High Priority**
**Industry:** Frontier LLM — consumer subscription + developer API · **HQ:** Beijing, China · international billing from **Singapore** · **Researched:** 2026-09-30 · **First email sent:** —
**Motion:** **In-house.** Not inferred — I decoded their payment service definition out of the production bundle.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Moonshot AI is one of China's frontier LLM labs, behind the **Kimi** assistant and the Kimi API platform. It sells a consumer/business membership (web, iOS, Android) and a prepaid developer API. It filed a **confidential A1 with HKEX** in the week of 2026-09-03 at roughly **US$50bn pre-money**.

> ## 🎯 THE HOOK — Apple prices in rupees. Their own checkout prices in dollars.
>
> Apple App Store, per storefront, live:
>
> | Market | iOS membership (localised) | Their own web checkout |
> |---|---|---|
> | 🇮🇳 India | **₹1,999 / ₹3,999 / ₹9,900 / ₹19,900** | **USD** |
> | 🇰🇷 Korea | **₩25,000 / ₩33,000 / ₩55,000** | **USD** |
> | 🇹🇼 Taiwan | **NT$590 / NT$1,290** | **USD** |
> | 🇺🇸 US | $19 / $39 / $99 / $199 | USD |
>
> The web codebase has exactly **two currency predicates — `isCNYPlan()` and `isUSDPlan()`** — and the API plan config is a hardcoded `isOverseas ? USDConfig : CNYConfig` pair, not a conversion. Local-currency pricing reaches their customers **only through `getLocalePlan()` reading a `goods` array from Apple StoreKit and Play Billing.**
>
> **They are renting local pricing from Apple and Google at 15–30%, on the one path they don't own, while the path they do own stays in dollars.** Both halves are theirs, both are verifiable, and neither is disputable.

> ## 💥 THE SECOND HOOK — they coded 19 currencies and shipped one
>
> Their own price formatter, `formatPriceCurrency()`, already codes symbols for **19
> currencies — USD, EUR, GBP, JPY, CNY, HKD, SGD, AUD, CAD, CHF, KRW, TWD, THB, MYR, INR,
> NZD, AED, BRL, PHP.** Twelve are APAC.
>
> I then called their **live, unauthenticated catalogue API** —
> `POST www.kimi.com/apiv2/kimi.gateway.order.v1.GoodsService/ListGoods` — and every plan on
> every channel came back **`"currency":"USD"`, `"useRegion":"REGION_OVERSEA"`**.
>
> **The rails are built. The pricing isn't localised.** That is not a gap they need convincing
> about — it is a half-finished job somebody already started.

> ## ⚙️ AND A THIRD — three acquirers, split by customer type, gated server-side
>
> Probing that same API channel by channel (verified by me, 2026-09-30):
>
> | Channel passed | Paid plans returned |
> |---|---|
> | **STRIPE** (1) | **all 9** |
> | **PAYERMAX** (7) | **all 9** |
> | **APPLE** (4) | **all 9** |
> | AIRWALLEX (2) | **free tier only** |
> | ALIPAY (6) / WECHAT (3) | free tier only |
>
> So **consumer international web → Stripe (and PayerMax is catalogue-enabled)**, while
> **Airwallex is the B2B / business rail** — corroborated by a real invoice on their own forum:
> a **USD 1,200 Kimi Business purchase, invoice INV-F80DGT8T-0001, seller NOVASCENT PRIVATE
> LIMITED, captured via Airwallex**. Consumer refunds in the same forum are on **Stripe**.

**SimilarWeb total visits:** shares only, no visit count supplied. ⚠️ **And the supplied dataset is the wrong property** — see the scope warning below and `accounts/traffic/moonshot-ai.md`.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇺🇸 US | 12.71% ▼47.71% | Web → Airwallex (USD) · iOS/Play IAP | — | ❌ none |
| 2 | 🇮🇳 **India** | **7.77% ▲11.53%** — the only large market growing | Web → Airwallex (USD) · **iOS IAP in ₹** | **UPI ❌🔒 · UPI Autopay ❌ · RuPay ❌ · netbanking ❌ · EMI ❌** | ❌🔒 none — RBI PA regime gates domestic acquiring |
| 3 | 🇰🇷 Korea | 3.97% ▼35.19% — longest sessions in the table (2m48s) | Web → Airwallex (USD) · **iOS IAP in ₩** | **KakaoPay ❌ · Naver Pay ❌ · Toss ❌ · local card PG ❌ · instalments ❌** | ❌🔒 none — domestic acquiring effectively needs a Korean entity |
| 4 | 🇬🇧 UK | 3.68% ▲4.15% | Web → Airwallex (USD) | — | ❌ none |
| 5 | 🇵🇰 Pakistan | 3.38% ▼48.72% | Web → Airwallex (USD) | **JazzCash ❌ · Easypaisa ❌ · Raast ❌** | ❌ none |

*(then 🇧🇷 Brazil 3.18% — **Pix ❌**, LATAM · 🇩🇪 3.17% · 🇨🇳 **China 3.06%** ▼56.83% · 🇮🇩 Indonesia 2.88% — **QRIS ❌** · 🇧🇩 2.61% — **bKash ❌** · 🇹🇼 2.12% — **iOS IAP in NT$** · 🇻🇳 1.78% — **MoMo ❌** · 🇦🇺 1.78% · 🇸🇬 1.76%)*

**~97% of traffic sits in markets with no local entity.** Only China and Singapore are covered.

### Legal entities
- **NOVASCENT PRIVATE LIMITED** (Singapore) — **UEN 202326494K**, inc. 2023-07-06, LIVE. **International billing entity** for Kimi consumer (ToS v2, eff. 2026-08-13). Singapore law, **SIAC arbitration, liability capped at USD 100**
- **MOONSHOT AI PTE. LTD.** (Singapore) — named in the **API/developer ToS** (upd. 2026-07-30). ⚠️ Likely the former name of 202326494K, **not registry-confirmed**
- **北京月之暗面科技股份有限公司** (PRC, **joint-stock**) — China API top-up counterparty, agreement eff. **2026-08-31**
- **北京月之暗面科技有限公司** (PRC, LLC) — fapiao-issuing entity, 技术服务费 at **6%**
- **Moonshot AI HK Limited** — CR 75375676 · **Moonshot AI Ltd** (Cayman) — Reg. 399981, the red-chip parent being unwound for the listing

### Known PSPs — by surface, not in aggregate
| Surface | Provider | Evidence |
|---|---|---|
| **Intl consumer membership (web)** | **Stripe** — returns all 9 paid plans from the live catalogue API; consumer refund threads on their forum are Stripe | `[Source Code]` + live API, verified by me |
| **Intl business/enterprise (web)** | **Airwallex** — the `isOverseas ? AIRWALLEX : ALIPAY` ternary sits behind `checkAgreement("business")`; a real USD 1,200 Business invoice was captured on Airwallex | `[Source Code]` + `[Third-Party Report]` forum invoice |
| Intl consumer (catalogue-enabled) | **PayerMax** — returns all 9 paid plans, but **no observed transaction** | `[Source Code]` live API |
| **International API top-up** | **Stripe** — Hosted Checkout, no method picker of their own | `[Source Code]` 48 Stripe refs, 0 Alipay/WeChat refs in the intl pay page |
| China membership (web) | **Alipay**; **WeChat Pay** on the gift-card/pay-token checkout | `[Source Code]` `subscribe(PaymentChannel.WECHAT)` / `.ALIPAY` |
| China API top-up | **Alipay** (iframe) · **WeChat Pay** (QR) · **corporate bank transfer** (dedicated account, 1–5 working days) | `[Source Code]` + `[Developer Docs]` |
| Both app surfaces | **Apple IAP** · **Google Play Billing** — deep StoreKit 2 server integration | `[Source Code]` + `[Checkout]` store listings |

### Orchestration status
**In-house orchestration layer — HIGH confidence.** They run **`growth.pay.v1.PayService`**, a channel-agnostic payment service with ~25 RPCs, decoded by me from a protobuf `FileDescriptorProto` embedded in their production bundle. Every RPC takes `payment_channel` as a parameter. Zero third-party orchestrator anywhere across a 16 MB sweep.

### Buying signals
- 💰 **Confidential A1 filed with HKEX**, week of 2026-09-03, **~US$50bn pre-money**; company said *"no comment on the market report"* ⚠️ press-sourced, no public filing exists
- 🏗️ **Onshore joint-stock conversion visible in a live contract** — the China top-up agreement effective **2026-08-31** names 股份**有**限公司, the form required for a HK listing
- 🔀 **A PSP migration looks to be in progress** — new overseas subscriptions default to Stripe on the API platform while Airwallex is retained only for downgrades on existing Airwallex subscriptions
- 💳 **Kimi AI Card** — ABC × American Express co-brand, launched **2026-07-10**, ¥580/¥880 annual fees. ⚠️ **Card issuing, not acquiring** — warm opener, not a PSP relationship
- ⚠️ **Live US export-control allegation** — White House OSTP director alleged GB300 access; Treasury Secretary said Entity List designation is *"on the table"*. **No formal action taken.** See §3

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Moonshot AI`.*

⚠️ **Read before drafting.**

1. **Lead with the Apple-vs-web currency asymmetry.** ₹1,999 in the App Store, dollars on their own checkout. It is an asymmetry inside their own stack, both halves sourced, and it names the 15–30% they are paying to rent what they could own.
2. **Second: one ternary for thirteen markets.** `isOverseas ? AIRWALLEX : ALIPAY`. Quote it.
3. **Motion is IN-HOUSE. Never say "you need orchestration."** They built `growth.pay.v1.PayService` with unified subscription lifecycle, invoicing, cross-channel reconciliation and a retry counter. The frame is reach and the cost of maintaining it, never the case for the abstraction.
4. **Do NOT reuse the Kling dunning angle.** `past_payment_attempt_count` exists — they track retries.
5. **PayerMax is catalogue-enabled but unproven.** It returns all 9 paid plans from the live API, yet appears in no *client* selection path and **no PayerMax transaction was ever observed** (Airwallex and Stripe both appear on real invoices). Say "wired but unproven", never "live".
6. **Do NOT claim they don't accept UPI.** Airwallex renders its method set dashboard-side, invisibly. Say *"nothing in your web stack references a single APAC local rail, and your checkout can only price in USD or CNY"* — which is sourced.
7. **Never state the export-control allegations as fact.** They are allegations by named officials; the company has not been designated.
8. **Correct surface mapping — get this right or a reply will correct you:** consumer international web → **Stripe**; business/enterprise → **Airwallex** (a real USD 1,200 Business invoice, seller NOVASCENT, was captured on Airwallex); China → Alipay/WeChat; apps → Apple/Google IAP. **PayerMax: catalogue-enabled, unproven.**
9. **Consumer signups are throttled.** Kimi suspended new C-end subscriptions on 2026-07-19 over compute, and the gate is still returning `REASON_SUBSCRIPTION_NEED_APPLY`. Pitch **revenue per existing payer and B2B**, not acquisition.
10. **The best discovery question:** *"a USD 1,200 Business purchase on your own forum was captured on Airwallex and never provisioned, with no reply for a week — is entitlement delivery something you're actively working on?"* Or, softer: *is Airwallex the B2B rail by design, or is it a migration in progress?*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 22 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ⚠️ **NOT FOUND — ASSUMED ~150,000/month. [ASSUMPTION — not researched.]** Basis: Kimi app MAU reported at 10–15m in 2026 by third-party trackers (**tracker not named in any source I could attribute**), against any plausible paid-conversion rate, plus prepaid API top-ups from a self-serve funnel starting at $1. **No company-issued paying-subscriber, API-customer, DAU or revenue figure exists.** Per the disclosure rule an assumption never rejects — the band is scored, the row is ⚠️, and "confirm monthly transaction count" is top of Manual Research. **Billing unit counted: membership charges + prepaid API top-ups.** App-store IAP may not appear in their own transaction count at all |
| Orchestration status | **+1** | ✅ **In-house layer confirmed** from their own service definition (§3B). Correctly the hardest sell |
| 3+ countries | **+3** | ✅ 13 non-China markets above 1% traffic share |
| Multiple PSPs | **+3** | ✅ **Airwallex** (intl membership) + **Stripe** (intl API) + **Alipay** + **WeChat Pay** + Apple + Google, each code-confirmed on a named surface |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **India (#2) has no UPI anywhere in the stack**, and no Indian entity. Absence established by an exhaustive sweep of **353 assets (16 MB) + 90 chunks** with zero word-boundary hits, **and** independently by the currency predicates: a checkout that can only price in **USD or CNY** cannot present UPI in INR. Prominence sourced: **UPI ≈85% of India's digital payments FY2025-26** ([PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2257087&reg=3&lang=2), [NPCI](https://www.npci.org.in/product/upi/product-statistics)). Korea (#3) is the same picture |
| Recent expansion | **0** | ⬜ Kimi K3 / K2.7 are **product** launches, not market entry. No new-market launch found |
| Payment issues | **+2** | ✅ **HIGH.** **22 distinct payment threads on Moonshot's own forum** (forum.moonshot.ai), 2025-11 → 2026-09: 13 refund threads, 4 duplicate/unauthorised-charge-after-cancellation, 4 top-up-captured-but-not-credited, 1 payment-captured-entitlement-never-provisioned. **Trustpilot 1.6/5 across 39 reviews**, 7 payment-relevant |
| Funding >$10M | **+2** | ✅ Multiple rounds through 2026 culminating in a pre-IPO G round at **~US$50bn pre-money** ⚠️ amounts press-sourced |
| High traffic outside home | **+2** | ✅ **China is 8th at 3.06%.** There is no home market in the data at all |
| Competitor using orchestration | **0** | ❌ **Confirmed absent.** DeepSeek runs PayPal + cards; BytePlus runs cards + PayPal only with zero local APMs in SG/MY/ID; Z.ai and MiniMax are single-PSP Stripe. **No orchestrator anywhere in the cohort** |
| Payment job postings | **+1** | ✅ **A live req that reads like our own pitch deck.** `Agentic Commerce Engineer`, Beijing, created 2025-08-29, **updated 2026-09-18, status open** — recovered by decrypting their MokaHR job feed. Plus a dedicated `客户投诉处理专家（政府绿色通道方向）` req for membership **refund disputes and regulator escalation** (updated 2026-09-07) |

**Tier:** ⭐ **High Priority (17+)** → **22/29**

> **No analyst override applied, but two things bound the number.**
> **(1) The app-store trap is live and material.** Apple IAP is where localised pricing happens, with a deep StoreKit 2 server integration (receipt verification, discount JWS signing, Consumption Request API). If IAP dominates consumer revenue, the orchestrable share is smaller than it looks — **but the API platform and the web membership are both non-IAP by construction, and the API funnel is entirely web.** Ask for the split.
> **(2) All five agents have now reported.** 22/29 is the settled score.

### Source Notes
- ✅ **`PaymentChannel` enum and `growth.pay.v1.PayService`** — I decoded the protobuf descriptor myself from `kimi.utils-DGHI4XwS.js` (78,892 b, 404-body check passed)
- ✅ **The region ternary, and the 0 hits for STRIPE/PAYERMAX in that chunk** — pulled and grepped by me
- ✅ **Invoice console intl 404 / China 200** — both checked by me
- ✅ **Domain resolution** — curl, by me
- ✅ **Export-control screen** — BIS Entity List, OFAC SDN, OFAC Consolidated, all with passing controls, by me
- ⛔ **A correction to my own finding:** I first reported *"Airwallex provisioned in production on both developer platforms."* **Over-stated.** On `platform.kimi.ai` the string appears **once**, as a dereferenced env var next to an unset companion; `js.airwallex.com` appears **zero** times; `stripe` appears **172** times. **On the developer platforms Airwallex is dead config.** Airwallex's real, code-selected use is the **membership** app. *Methodology rule banked: an env var is not an integration.*
- ⛔ **A second correction:** I first said *"three card acquirers running in parallel."* **Wrong.** Three sit in the `overseas` **array**; the membership app selects **one**. Stripe's confirmed use is the API platform; **PayerMax is selected nowhere.**
- ⚠️ Entities, funding, IPO, users, app-store prices, complaint data — agent-reported, not re-fetched by me
- ⚠️ **No company-issued revenue, ARR, MAU or paying-subscriber figure exists.** A ">$1B ARR" figure circulates; it is press-reported and unverified. **Do not put it in an email**

### Success Case Alternatives
- **A global consumer-subscription business with a large India base billed cross-border in USD** — matched on the FX/approval-rate mechanics, not the vertical
- ⚠️ **Do not use the "Netflix +40% APAC via orchestration" claim** recorded elsewhere in this repo — it traces to a payments-vendor marketing page with no primary source

---

## Executive Summary

Moonshot AI is a Beijing frontier-LLM lab selling the **Kimi** assistant and a developer API, with international billing run from a **Singapore** entity and a **confidential HKEX A1** filed in September 2026 at roughly US$50bn pre-money. The decisive payment finding is a single line in their own pricing component — `isOverseas ? AIRWALLEX : ALIPAY` — which routes **thirteen non-China markets through one acquirer with no per-market logic of any kind**, on a checkout whose only two currency predicates are `isCNYPlan()` and `isUSDPlan()`. Meanwhile **Apple sells the same membership in ₹1,999, ₩25,000 and NT$590**, so the company is renting localised pricing from the app stores at 15–30% on the path it does not own while the path it does own stays in dollars. The motion is **in-house**: they have built `growth.pay.v1.PayService`, a genuine channel abstraction with unified subscription lifecycle, invoicing, cross-channel reconciliation and a retry counter — so the sale is reach and opportunity cost, never the case for orchestration itself.

---

## Section 1: Website Traffic Analysis by Country

**Data source: SimilarWeb, supplied by Prateek 2026-09-30** (Jun–Aug 2026, `moonshot.ai`, 117 countries, shares only).

> ## 🛑 The supplied dataset measures the wrong property. Resolved by me by curl.
> ```
> moonshot.ai          → www.moonshot.ai        corporate site — does NOT fold into kimi
> kimi.moonshot.cn     → 301 → www.kimi.com     China consumer product moved onto kimi.com
> platform.moonshot.ai → 301 → platform.kimi.ai international developer platform
> platform.moonshot.cn → 301 → platform.kimi.com China developer platform
> ```
> With country-domains **OFF**, the table below is the **marketing site** and excludes `kimi.com`
> and both platform hosts — every payment surface. Engagement corroborates independently:
> **00:00:22–00:02:48 visits, 1.49–2.30 pages/visit, bounce to 75.03%.**
>
> **Consequence:** the country profile is directionally useful for *where interest is*, and I
> have used it that way. It **cannot** size the business. Full table, arithmetic and analyst
> notes: **`accounts/traffic/moonshot-ai.md`**.

| Rank | Country | Share | Trend | Source |
|---|---|---|---|---|
| 1 | 🇺🇸 United States | **12.71%** | ▼ 47.71% | SimilarWeb (supplied 2026-09-30) |
| 2 | 🇮🇳 **India** | **7.77%** | **▲ 11.53%** | same |
| 3 | 🇰🇷 Korea | **3.97%** | ▼ 35.19% | same |
| 4 | 🇬🇧 UK | 3.68% | ▲ 4.15% | same |
| 5 | 🇵🇰 Pakistan | 3.38% | ▼ 48.72% | same |
| 6 | 🇧🇷 Brazil | 3.18% | ▼ 17.48% | same |
| 7 | 🇩🇪 Germany | 3.17% | ▼ 18.04% | same |
| 8 | 🇨🇳 China | 3.06% | ▼ **56.83%** | same |
| 9 | 🇮🇩 Indonesia | 2.88% | ▼ 35.42% | same |
| 10 | 🇧🇩 Bangladesh | 2.61% | ▼ 17.68% | same |

*(11–18: Canada 2.23 · Italy 2.14 · Taiwan 2.12 ▲17.18 · Spain 1.97 ▲25.82 · France 1.82 · Vietnam 1.78 ▼63.51 · Australia 1.78 · Singapore 1.76)*

**High priority (>5%): US, India.** **APAC across visible rows = 25.32%**, a floor. Visible top 18 = 56.99% of total; **43.01% unshown**.

⚠️ **Thirteen of eighteen rows are falling steeply.** Do not read that as the business shrinking — it is at least as consistent with migration onto `kimi.com`, which the `kimi.moonshot.cn` redirect shows happening. `[INFERENCE, not confirmed]`

---

## Section 2: Legal Entities & Local Presence

**Headquarters:** Beijing, China. International contracting from **Singapore**.

| Country | Entity | Registration # | Role | Source |
|---|---|---|---|---|
| 🇸🇬 SG | **NOVASCENT PRIVATE LIMITED** | **UEN 202326494K**, inc. 2023-07-06, LIVE. 91 Bencoolen St #12-003 | **Intl billing entity, Kimi consumer.** SIAC arbitration, **liability cap USD 100** | kimi.ai ToS v2 (eff. 2026-08-13) |
| 🇸🇬 SG | **MOONSHOT AI PTE. LTD.** | ⚠️ likely former name of 202326494K — **not registry-confirmed** | Contracting entity in the **API/developer ToS** (upd. 2026-07-30) | platform.kimi.ai/docs/agreement/modeluse |
| 🇨🇳 PRC | 北京月之暗面科技**股份**有限公司 | not found | China API top-up counterparty, eff. **2026-08-31** | platform.kimi.com/docs/agreement/payment |
| 🇨🇳 PRC | 北京月之暗面科技有限公司 | not found | **Fapiao issuer**, 技术服务费, **6%** | platform.kimi.*/docs/guide/account-and-payments |
| 🇭🇰 HK | Moonshot AI HK Limited | CR **75375676**, LEI 984500897UEF0399DE53 | No billing role found | GLEIF |
| 🇰🇾 KY | Moonshot AI Ltd | Reg. **399981**, LEI 9845005D09BD6A4U1D27 | Red-chip parent, being unwound | GLEIF |

**Cross-Border Gap Analysis**

| Country | Top 10? | Local entity? | Domestic acquiring gated? | Cross-border risk |
|---|---|---|---|---|
| 🇺🇸 US | #1 | ❌ | No | Moderate — contracts via Singapore, disputes to SIAC |
| 🇮🇳 **India** | **#2** | ❌ | ✅ **Yes** — RBI Payment Aggregator regime | **HIGH** |
| 🇰🇷 Korea | #3 | ❌ | ✅ **Yes** — domestic card acquiring effectively needs a Korean entity | **HIGH** |
| 🇮🇩 Indonesia | #9 | ❌ | ⚠️ BI PJP licensing — verify | **HIGH** |
| 🇨🇳 China | #8 | ✅ ×2 | ✅ heavily licensed | N/A |
| 🇸🇬 Singapore | #18 | ✅ Novascent | No | Low |

> **Warning: potential cross-border operation in India.** India is their #2 market, the **only large market growing**, and there is no Indian entity. Transactions run cross-border against a Singapore entity — higher scheme cost, lower approval on domestically-issued cards, FX on top.

> **Regulatory gate: India and Korea.** Both effectively require local presence or a licensed local partner for domestic acquiring. ⚠️ **Verify the current RBI PA and Korean PG rules against a live source before citing either.**

⚠️ **Two live discrepancies, both from primary documents — good discovery questions.**
1. **Consumer terms contract with Novascent; developer terms still name Moonshot AI Pte. Ltd.** Stale document, or two entities? **Unresolved**, and it decides *who bills API customers*.
2. **The PRC entity changed form** 有限公司 → **股份有限公司** in a contract effective 2026-08-31 — the onshore joint-stock conversion required for a HK listing, visible in a live contract and independently corroborating the red-chip unwind reporting.

---

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers — four surfaces, four different answers

| Surface | Provider | Evidence Type | Source |
|---|---|---|---|
| **Intl membership (web)** | **Airwallex** — single channel, `createPayIntent` → `redirectUrl` | `[Source Code]` | `statics.kimi.ai/kimi-web-seo/assets/Pricing-Wdoe70Yp.js` |
| Intl membership | **Airwallex** — named **first** in their own invoice FAQ: *"Invoices are automatically sent to the email address registered with your payment provider (**Airwallex**, Stripe, Apple, or Google)."* | `[Terms/Privacy Policy]` | `.../en-US-DPuVS8An.js` |
| **Intl API top-up** | **Stripe Hosted Checkout** — *"You will be redirected to Stripe's secure checkout page"*, *"Secure Payment by Stripe"*, *"View on Stripe"*; full `stripe.pay.*` namespace (79 keys) incl. `autoRecharge.*` | `[Source Code]` | `platform.kimi.ai/_next/static/chunks/5291-*.js` |
| China membership | **Alipay** (region ternary) | `[Source Code]` | `statics.moonshot.cn/.../Pricing-CTi6ML3A.js` |
| China membership | **WeChat Pay** + Alipay on gift-card/pay-token checkout | `[Source Code]` | `.../Checkout-Bq3o8JbC.js` |
| China (app SDK) | **WeChat Pay** — *"Third-Party Entity: **Tenpay Payment Technology Co., Ltd.** (财付通)"*, personal info incl. *"order amount, transaction number"* | `[Terms/Privacy Policy]` | `kimi-img.moonshot.cn/.../sdk_sharing_list_v2_en.md` |
| China (app SDK) | **Alipay** — *"Third-Party Entity: Alipay Payment Technology Co., Ltd."* | `[Terms/Privacy Policy]` | same |
| China API top-up | Alipay iframe · WeChat QR · **corporate bank transfer** (dedicated account, 1–5 working days) | `[Source Code]`+`[Developer Docs]` | `platform.kimi.com/console/pay` chunk |
| iOS | **Apple IAP** — deep StoreKit 2 server integration | `[Source Code]`+`[Checkout]` | proto + `apps.apple.com/*/app/id6474233312` |
| Android | **Google Play Billing** | `[Source Code]`+`[Checkout]` | `play.google.com/store/apps/details?id=com.moonshot.kimichat` |
| — | **PayerMax** | ⚠️ **enum value 7 only. Referenced by NO selection, checkout or pricing code.** Not live | `[Source Code]` |
| — | UnionPay | ⚠️ label-map only, `avatar:""`, `/unionpay.png` 404s, absent from every picker. **Deprecated/legacy** | `[Source Code]` |

### 3B. Payment Orchestrator

**IN-HOUSE ORCHESTRATION LAYER — HIGH confidence.** Decoded by me from a protobuf `FileDescriptorProto` in `kimi.utils-DGHI4XwS.js`:

```
growth.pay.v1.PaymentChannel:
  UNSPECIFIED=0 · STRIPE=1 · AIRWALLEX=2 · WECHAT=3 · APPLE=4 · GOOGLE_PLAY=5 · ALIPAY=6 · PAYERMAX=7
```

**`growth.pay.v1.PayService` — ~25 RPCs, every one taking `payment_channel`:**

| Area | RPCs / fields |
|---|---|
| Payment | `CreatePayment` (returns `client_secret` + `out_payment_intent_id`) · `GetPaymentStatus` · `CreatePaymentCheckout` (returns `checkout_id`, `checkout_url`, `wechat_passthrough_params`) |
| Subscription lifecycle | `CreateSubscriptionCheckout` · `VoidSubscriptionCheckout` · `Cancel` · `Resume` · `Terminate` · `TerminateUserSubscriptions` · `Downgrade` · `AddSubscriptionCoupon` · `GetSubscription` · `next_billing_time` · `total_billing_cycles` · `trial_period_days` |
| Invoicing & refunds | `Invoice` · `InvoiceStatus` · `InvoiceEvent` (CREATED/FINALIZED/VOIDED/PAID/PRE_PAID/BILLING_TERMINATED/REFUND/CANCELED/RESUME) · `RefundInvoice` · `ManualRefundEvent` · `refund_amount_cents` |
| **Dunning** | **`past_payment_attempt_count`** |
| **Cross-channel reconciliation** | **`GetExternalTransactions`** · **`GetInnerTransactions`** · **`GetChannelTransactionByInvoiceNumber`** |
| Apple IAP | `VerifyReceipts` · `VerifyReceiptProductID` · `CreateSubscriptionByReceipt` · `GetSubscriptionByReceipt` · `BindApplePurchaseUUID` · `SendAppleConsumptionInfo` · `CreateAppleSubscriptionDiscountSignature` · `CreateAppleSubscriptionDiscountJWS` |
| Scenarios | `PayScenario{GIFT_CARD, ENTERPRISE_MEMBERSHIP, ENTERPRISE_SEAT, BOOSTER, SUBSCRIPTION, BUSINESS_BOOSTER, ENTERPRISE_SSO}` · `AppCategory{KIMI_C, KIMI_B}` |

A second BFF layer `kimi.gateway.order.v1.PayService` (`CreatePayIntent`, `CreatePayIntentByPaymentToken`) fronts it for web.

**Routing, verbatim** (`subscription-Cmx3G86j.js`):
```js
var channels = { cn:[ALIPAY,WECHAT], overseas:[STRIPE,AIRWALLEX,PAYERMAX],
                 ios:[APPLE], google:[GOOGLE_PLAY], android:[ALIPAY,WECHAT] };
// recommendedPaymentChannel from useMembershipPlans()  ← backend can override per plan
```

**No third-party orchestrator.** Swept 353 kimi-web-seo assets (16 MB) + 90 Next.js chunks + 4 HTML surfaces for Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno, IXOPAY, Corefy, Rebilly, Nuvei, Zooz — **zero real hits** (see §FP for the near-misses, including a base64 blob containing "yuno").

> **What this means for the sale.** They have already built the abstraction. This is **displacement of an internal build**, not filling a gap. The value story is **local APMs, routing intelligence and recovery** — and the fact that `overseas` resolves to one branch for thirteen markets.

> **MANUAL:** Walk the membership checkout from an Indian and an Indonesian IP with DevTools open. Airwallex renders its method set dashboard-side and it is the one thing source-mining cannot reach.

---

## Section 4: Alternative & Local Payment Methods

| Market | Surface | Method | Category | Status | Source |
|---|---|---|---|---|---|
| All 13 non-China | Membership web | **Airwallex** (whatever it renders) | Cards + unknown | **Active in checkout** | region ternary |
| All non-China | Membership web | **Pricing currency: USD only** | — | **Active** — only two branches exist, CNY and USD | `isCNYPlan()`/`isUSDPlan()` |
| All non-China | API top-up | **Stripe Hosted Checkout**; **auto-recharge on saved card** (threshold, amount, monthly cap, failure-pause) | Cards; card-on-file CIT→MIT | **Active in checkout** | intl pay chunk |
| 🇮🇳 India | iOS | **Apple IAP in ₹** — ₹1,999 / ₹3,999 / ₹9,900 / ₹19,900 | App-store IAP | **Active** | `apps.apple.com/in/app/id6474233312` |
| 🇰🇷 Korea | iOS | **Apple IAP in ₩** — ₩25,000 / ₩33,000 / ₩55,000 | App-store IAP | **Active** | `apps.apple.com/kr/...` |
| 🇹🇼 Taiwan | iOS | **Apple IAP in NT$** — NT$590 / NT$1,290 | App-store IAP | **Active** | `apps.apple.com/tw/...` |
| 🇺🇸 US | iOS | Apple IAP — $19 / $39 / $99 / $199 | App-store IAP | **Active** | `apps.apple.com/us/...` |
| All non-China | Android | Google Play IAP, $0.59–$3,863.99/item | App-store IAP | **Active** | Play listing |
| All non-China | Membership web | Gift cards (`PAY_SCENARIO_GIFT_CARD`) | Cash/voucher | **Active in checkout** | `index-CSFKQLS8.js` |
| 🇨🇳 China | Membership / API | Alipay · WeChat Pay · corporate bank transfer · **VAT fapiao** (ordinary `02` / special `01`, USCC field, 6%) | Wallet / A2A / invoicing | **Active in checkout** | CN chunks + docs |
| **Every APAC local rail** | **all surfaces** | UPI · UPI Autopay · RuPay · netbanking · Paytm · PhonePe · EMI · KakaoPay · Naver Pay · Toss · JKOPay · LINE Pay · TW ATM/VA · TW convenience-store cash · instalments · QRIS · GoPay · OVO · DANA · ShopeePay · VA · MoMo · ZaloPay · VNPay/VietQR · PayNow · GrabPay · JazzCash · Easypaisa · bKash · Nagad · PayTo · BPAY · Afterpay · Zip · konbini · Pix · boleto | — | ❌ **NOT FOUND** — zero word-boundary hits across every bundle, doc and page on all four surfaces | exhaustive negative sweep |

### Dominant rails missing from markets where Moonshot is live

| Market | Missing rail | Cited prominence |
|---|---|---|
| **🇮🇳 India 7.77%** | **UPI** + UPI Autopay, RuPay, netbanking, EMI | **UPI ≈85% of India's digital payments FY2025-26**; ~24,161.69 crore txns/yr ([PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2257087&reg=3&lang=2) · [NPCI](https://www.npci.org.in/product/upi/product-statistics)) |
| **🇰🇷 Korea 3.97%** | KakaoPay / Naver Pay / Toss, local card PG, instalments | Three-wallet market; KakaoPay 40m+ registered, Toss 19.1m MAU; wallet share of txn value 27% (2023) → 42% by 2027 ([Statista](https://www.statista.com/statistics/1061986/south-korea-most-commonly-used-mobile-payment-providers/) · [KOMOJU](https://en.komoju.com/blog/general-advice/korea-mobile-payment-trends/)) |
| **🇮🇩 Indonesia 2.88%** | **QRIS**, virtual account, GoPay/OVO/DANA/ShopeePay | **QRIS 15.51bn txns in 2025, +148.54% YoY**, ~43m merchants ([Katadata/BI](https://databoks.katadata.co.id/en/finance/statistics/6a2631bbc1a3f/the-number-of-qris-users-increased-74-in-the-q4-2025)) |
| **🇻🇳 Vietnam 1.78%** | MoMo, ZaloPay, VNPay/VietQR | MoMo 68% wallet share (31m+ users); SBV: 57.31m e-wallets activated ([VIR](https://vir.com.vn/e-wallet-players-look-to-take-hold-of-market-gaps-113427.html)) |
| **🇹🇼 Taiwan 2.12%** | ATM/VA, convenience-store cash, card instalments | Cards 39% of TW e-commerce, wallets 34%, **convenience-store cash 15%** ([Antom](https://www.antom.com/guides/markets/taiwan)) |
| **🇵🇰 Pakistan 3.38%** | JazzCash, Easypaisa, Raast | Raast 48m users / ~2bn txns by 2025; Easypaisa 55m+ users, 2.7bn txns ≈9% of GDP |
| **🇧🇩 Bangladesh 2.61%** | bKash, Nagad | bKash 60m+ customers; national MFS base >200m registered ([PaymentBrief](https://paymentbrief.com/markets/bangladesh/)) |
| 🇧🇷 Brazil 3.18% *(LATAM)* | Pix, boleto, instalments | **Pix 42% of Brazilian e-commerce vs cards 41%** (2025) ⚠️ EBANX-authored source, flagged |

> ⚠️ **METHODOLOGY — the most important caveat in this file.** Moonshot passes **one** `AIRWALLEX` channel and redirects. **The method set Airwallex renders is dashboard configuration and is invisible externally.** The same applies to Stripe on the API platform.
>
> **Do NOT claim Kimi does not accept UPI.** What IS sourced: (a) nothing in their entire shipped web stack references a single APAC local rail, across an exhaustive 16 MB sweep; (b) **the checkout can only price in USD or CNY**; (c) Apple IAP *is* localised while the web is not. Those three are defensible. "No UPI" is not.

---

## Section 5: Payment Issues & Customer Complaints

**Their own support forum is the richest source on this account.** 22 distinct payment threads enumerated via the Discourse search API on `forum.moonshot.ai`; 10 read in full.

| Issue Type | Platform | Frequency | Date Range | Source |
|---|---|---|---|---|
| **Refund requests unanswered or auto-denied** | forum.moonshot.ai | **HIGH — 13 threads** | 2026-04-16 → 2026-09-17 | t/355, t/371, t/401, t/432, t/499, t/512, t/522, t/556, t/567, t/568, t/575, t/600, t/610 |
| **Billing / metering disputes** (quota consumption, double-billing idle VMs) | forum.moonshot.ai | **HIGH — 9 threads** | 2025-11-08 → 2026-09-28 | t/111, t/384, t/413, t/458, t/486, t/531, t/559, t/572, t/614 |
| **Duplicate / unauthorised charges after cancellation** | forum.moonshot.ai | **HIGH — 4 threads** | 2026-03-15 → 2026-09-08 | t/305, t/353, t/456, t/589 |
| **Top-up captured but balance not credited** (reconciliation failure) | forum.moonshot.ai | Moderate — 4 threads | 2026-07-28 → 2026-08-22 | t/498, t/535, t/538, t/554 |
| **Payment captured, entitlement never provisioned** (B2B) | forum.moonshot.ai | Isolated but severe | 2026-09-02 | t/579 |
| Repeat charge attempts after cancellation | Trustpilot (Peru) | — | 2026-09-07 | [Trustpilot](https://www.trustpilot.com/review/www.kimi.com) |
| Refund refused, API unusable from purchase | Trustpilot (**Vietnam**) | — | 2026-08-19 | same |
| *"cannot cancel subscription"* | Trustpilot (Ireland) | — | 2026-06-29 | same |
| **Paid subscription not offered in the Indonesian App Store storefront** | App Store **ID** | Isolated, but a clean APAC availability gap | 2025-10-27 | Apple customer-reviews RSS, id 6474233312 |
| Indian **+91 mobile OTP never delivered**, paid account inaccessible 7+ days | forum.moonshot.ai | Isolated | 2026-08-27 | t/571 |

**Trustpilot aggregate: 1.6 / 5 across 39 reviews.** 7 of 39 payment-relevant — moderate in count, **high as a proportion** of a small, very negative base.

### The three artefacts that matter

**t/579 (2026-09-02) — the best single artefact on this account.**
> *"On 29 Aug 2026 I purchased Kimi Business (2 seats, **USD 1,200**)… Payment was confirmed the same day via **Airwallex** (invoice **INV-F80DGT8T-0001**, seller **NOVASCENT PRIVATE LIMITED**). Since then: my account still shows the free plan… I have emailed membership@moonshot.cn twice on 29 Aug and membership@moonshot.ai on 30 Aug with **no response**."*

A captured payment with no entitlement delivered, on Airwallex, at USD 1,200, from an APAC buyer, **with zero staff reply**. That is a webhook/provisioning break between the acquirer and their own `PayService`.

**t/456 (2026-07-03, with a staff reply) — they explain the defect themselves.**
Trial expired 06-29 05:36; *"the system automatically generated a new pending renewal bill"*; user cancelled at 06-29 **06:07**; staff: *"Because the new billing cycle had already begun and the new bill was generated **half an hour prior**, the system applied your cancellation to the subsequent billing cycle, rather than the pending bill."* The card was then retried **three times** for $19 and the subscription had to be **cancelled manually by a human**.
→ **A 31-minute race condition between cancellation and bill generation, with in-house dunning retries that have no cancellation interlock.**

**t/554 (2026-08-22) — cross-channel ledger mismatch.**
A USD 30 top-up (invoice WN3ZPWLI-0001) showed *"Successful"* on the top-up page while Billing Overview showed `Total Recharge: USD 0.00000`. Resolved 14 days later: the balance had landed **on a different org id**.

> **Pattern — and it maps directly onto §3B.** Every one of these is a symptom of the in-house layer: `past_payment_attempt_count` firing after a cancellation it didn't interlock against; `GetChannelTransactionByInvoiceNumber` failing to tie a channel transaction to the right ledger; `ManualRefundEvent` existing because refunds need a human. **They built the abstraction and are now carrying its operational cost.** That is the honest, specific version of the orchestration argument for this account.

⚠️ **黑猫投诉 volume: not established.** The platform was never reached and **no complaint count there should be cited.** The only evidence it matters is indirect — their own complaint-handler job req names 黑猫投诉 as a monitoring target.

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | **wk of 2026-09-03** | **Confidential A1 filed with HKEX**, ~US$50bn pre-money. Company: *"no comment on the market report"*. ⚠️ HK01 + unnamed sources; the company **publicly denied** an August filing report | Funding / IPO | TechNode 2026-09-03 |
| 2 | **2026-08-31** | **China top-up agreement takes effect naming 北京月之暗面科技股份有限公司** — the joint-stock form required for a HK listing, visible in a live contract | Corporate restructuring | platform.kimi.com/docs/agreement/payment |
| 3 | 2026-07-22 | **White House OSTP director Michael Kratsios alleges** large-scale distillation and GB300 server access incl. via Thailand. **Treasury Secretary Bessent:** *"sanctions and Entity List designations will be on the table"* | Regulatory risk | TechCrunch 2026-07-22 |
| 4 | **2026-07-10** | **Kimi AI Card** — Agricultural Bank of China × American Express co-brand, ¥580/¥880 annual fees | Partnership (**issuing**) | kimi.com/aicard · 21世纪经济报道 · 界面新闻 |
| 5 | 2026-05 / 2026-06 | API platform changelog: *"Added automatic balance top-up"* (May) and *"custom top-up amounts"* (Jun) — maps 1:1 onto the `stripe.pay.autoRecharge.*` and `stripe.pay.custom*` namespaces | Payment infrastructure | platform.kimi.ai/docs/platform-changelog |

**Public payment RFP:** **No public payment-related RFP found.**

### ⭐ Payment job postings — FOUND, live, and one of them is our pitch in their words

Recovered by decrypting Moonshot's live MokaHR job feed (`app.mokahr.com/api/outer/ats-apply/website/jobs/v2`, AES-CBC with the page's own key/IV). **106 open roles** — Beijing 66, Shanghai 17, Shenzhen 8, Chengdu 2, **US 2, Singapore 2**, other 33. Three are payment-relevant.

**1. `Agentic Commerce Engineer`** — Beijing, full-time, created 2025-08-29, **updated 2026-09-18, status `open`**. Verbatim from the JD:
> 「商业化平台 - 抽象定价、订阅、计费与权益，让新产品、新套餐和商业实验更快上线」
> *Commercialization platform: abstract pricing, subscription, billing and entitlements…*
>
> 「**可靠的交易体验 - 打通国内外支付、续费与权益交付，改善成功率与成本；用监控、对账与补偿保障长期运行**」
> ***Reliable transaction experience: connect domestic and overseas payments, renewals and entitlement delivery; improve SUCCESS RATE and COST; safeguard long-term operation with monitoring, RECONCILIATION and COMPENSATION.***

**That is Yuno's value proposition, written by the prospect, in their own words.** Multi-market connectivity, authorisation-rate optimisation, cost reduction, reconciliation. They are hiring to build in-house exactly what we sell — which is both the strongest buying signal on this account and the clearest statement of why the motion is *in-house* and not greenfield.

**2. `客户投诉处理专家（政府绿色通道方向）`** — Customer Complaint Specialist, Government Green-Channel. Beijing, created 2026-03-21, **updated 2026-09-07, `open`**. Handles 「Kimi商业化会员订阅相关的**退费纠纷**」 (membership **refund disputes**), builds monitoring across Weibo, Xiaohongshu and **黑猫投诉**, identifies pain points in 「**计费流程**」 (billing flows), and needs familiarity with 消费者权益保护法, the Beijing **12345** hotline and **SAMR** workflows.
→ **They have budgeted dedicated headcount for subscription refund disputes and regulator escalation.** That quantifies §5.

**3. `国际化合规`** (Internationalization Compliance) — Beijing, **created 2026-09-22, the newest req on the board**. Global regulatory tracking, ISO 27001/42001, SOC 2, direct dialogue with overseas regulators, overseas complaints and deletion requests; bonus for **Japanese and Korean**. Active international build-out.

### ⚠️ And one more development that changes the timing

**2026-07-19 — Kimi suspended all new C-end subscriptions** after the K3 launch, citing a compute shortage: 「暂停 C 端新用户订阅」. It also announced it would **split Kimi main entitlements from Kimi Code entitlements** — a live re-plumbing of the product and entitlement catalogue.

I confirmed the gate is **still in place**: the live catalogue API returns `"transitionSummary":{"reason":"**REASON_SUBSCRIPTION_NEED_APPLY**"}`, and the Plus plan's `createTime` is **`2026-07-19T14:24:16Z`** — the catalogue was rebuilt that very day.
→ Consumer acquisition is throttled by compute, so **revenue per existing payer and B2B are where the pressure is** — which is exactly where their payment problems are worst (§5). ([ithome](https://www.ithome.com/0/978/808.htm))

---

## Section 7: Payment-Specific News

| # | Date | Headline | Relevance | Source |
|---|---|---|---|---|
| 1 | 2026-07-10 | Kimi AI Card launches with ABC and American Express | Sophistication + warm opener. **Issuing, not acquiring** | kimi.com/aicard |
| 2 | 2026-08-31 | China recharge agreement v2026-08-31: *"您可以选择我们认可的第三方支付渠道（如支付宝和微信）"*, **no refunds on unconsumed balance** | Current contractual position in China | platform.kimi.com/docs/agreement/payment |
| 3 | 2026-08-13 | Consumer ToS/Privacy v2 — contracting party becomes **NOVASCENT PRIVATE LIMITED** | The international billing entity, named | kimi.ai ToS v2 |
| 4 | 2026-05 → 2026-06 | Auto-recharge, then custom top-up amounts, added to the API platform | They are actively building billing features | platform changelog |
| 5 | 2026-03-08 | 36Kr: *"Kimi 1月个人用户支付订单数环比增长8280%，2月环比再涨123.8%"*, attributed only to *"据Stripe数据"* | Corroborates a Stripe relationship. ⚠️ **No named Stripe report exists — treat the ranking as unverified** | [36Kr](https://36kr.com/newsflashes/3714143264059528) |

**No provider removals found.**

---

## Section 8: Checkout Experience Audit

Never authenticated, so no rendered checkout was observed. Findings are from shipped code, published docs and store listings.

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | **Hosted redirect throughout** — `createPayIntent`→`redirectUrl` (membership), `checkout_url` (API) | Fair | No embedded card form anywhere |
| Guest checkout | Account required (region tied to account) | Fair | — |
| Card input | **No PAN field in any bundle.** No `js.stripe.com`, no Stripe Elements | Good | Scope stays at the PSP |
| Methods visible | One channel per region; no picker of Moonshot's own on the intl paths | **Poor** | The PSP's page does the choosing |
| **Location-based display** | **One ternary — `isOverseas ? AIRWALLEX : ALIPAY`.** No per-market logic exists | **Poor** | This is the finding |
| Instalments / EMI | **None evidenced** in India, Korea, Taiwan | Poor | — |
| 3DS | **Not established** | Unknown | ⚠️ Both acquirers do 3DS server-side. **Do not claim they lack it** |
| PCI indicator | Hosted redirect + card-on-file at PSP | Good | See §9 |
| **Multi-currency** | **USD or CNY. Two branches, no others.** API plan config is a hardcoded `isOverseas ? USDConfig : CNYConfig` pair | **Poor** | CNY: ¥1.30/¥6.50/¥27.00/MTok · USD: $0.95/$4.00/$0.16/MTok |
| Saved payment methods | Yes on the API platform — auto-recharge with threshold, amount, monthly cap, failure-pause | Good | `triggerSource: auto/manual` |
| **Invoicing** | **China `/console/invoice` → HTTP 200**, full VAT fapiao. **International `/console/invoice` → HTTP 404**, while the English doc promises invoices at a 9% rate | **Poor — verified by me** | A real, quotable operational gap |
| Error/dunning | `past_payment_attempt_count` on the Invoice model; `autoRecharge.failureNoticeTitle`, `previousFailureTitle` | Fair | **Server-side dunning exists** — do not pitch its absence |

⚠️ **The English billing FAQ is an unlocalised translation of the Chinese original** — it claims international top-ups "support WeChat Pay and Alipay QR code payments" and names a PRC entity at a 6% Chinese tax rate, while the live international pay page is **Stripe end-to-end**. **Trust the code, not that page.**

---

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|---|---|---|
| PCI DSS Level | **No direct PCI compliance documentation found publicly for Moonshot AI.** No claim, attestation, SAQ level or AOC in any ToS, privacy policy, recharge agreement or SDK disclosure | — |
| Card data handling | `[INFERENCE, not confirmed]` **SAQ A / minimal scope** | See below |
| Recommended Yuno integration | **SDK** — preserves the reduced scope they already have | — |

`[INFERENCE, not confirmed]`: every flow observed is hosted-redirect or store-billed, with card-on-file held at the PSP. **No `js.stripe.com`, no Stripe Elements, no PAN field in any bundle.** Consistent with SAQ A. `CreatePayment` returning `client_secret` means embedded-intent capability exists server-side but is unused client-side. **Do not assert a PCI level in outreach.**

⚠️ FP caught: *"PCI ID of the graphics card hardware device"* in the SDK disclosure is a **PCI bus** ID — device fingerprinting, nothing to do with PCI DSS.

---

## Section 10: Strategic Insights & Outreach Angles

> **Insight #1: They coded nineteen currencies and shipped one**
> **Evidence:** §8 — their own `formatPriceCurrency()` codes **19 currencies including INR, KRW, TWD, SGD, THB, MYR, PHP, HKD, JPY, AUD, NZD** + §12 — every plan on every channel of their **live catalogue API** returns `"currency":"USD"` + §4 — Apple IAP *is* localised (**₹1,999, ₩25,000, NT$590**) while the web is not.
> **Pain Point:** Somebody built the multi-currency plumbing and it was never switched on. So the only path where an Indian customer sees rupees is the App Store — the path that takes 15–30% and owns the relationship. On the path they own, the same customer gets a USD charge, a cross-border authorisation against a foreign issuer, and a decline rate nobody is measuring by market.
> **Yuno Value Proposition:** Local-currency presentment and local acquiring on the owned channel, so it stops being the worse one. The formatter already knows the symbols.
> **Best Success Case:** A global consumer-subscription business with a large India base billed cross-border in USD — matched on mechanics, not vertical.
> **Outreach Angle:** *"Your price formatter already codes nineteen currencies — rupees, won, Taiwan dollars, Singapore dollars. Your live catalogue returns USD on every single plan. Apple sells Kimi in India for ₹1,999; your own checkout doesn't."*
> **Suggested Subject Line:** 19 currencies coded, 1 shipped

> **Insight #1b: Your own job ad is the business case**
> **Evidence:** §6 — a live `Agentic Commerce Engineer` req (updated 2026-09-18) asking for 「打通国内外支付、续费与权益交付，**改善成功率与成本**；用监控、**对账**与补偿保障长期运行」 + §5 — 22 payment threads on their own forum, including a USD 1,200 B2B payment captured on Airwallex with **no entitlement delivered and no staff reply**, and a 31-minute cancel/bill race condition that retried a card three times.
> **Pain Point:** They have already written down that they need better authorisation rates, lower cost and working reconciliation across domestic and overseas payments. Their support forum is the evidence that they don't have it yet. They are recruiting for a problem we have already solved.
> **Yuno Value Proposition:** The thing the req describes, without the hiring cycle — and without the second req they have open for refund disputes and regulator escalation.
> **Best Success Case:** Match on "already multi-acquirer, already building in-house, drowning in reconciliation".
> **Outreach Angle:** ⚠️ **Handle carefully — quoting someone's job ad can read as surveillance.** Use the *substance*, not the citation: *"Improving success rate and cost across domestic and overseas payments, with reconciliation that holds up — is that a 2027 project for you, or already underway?"*
> **Suggested Subject Line:** Success rate and reconciliation, across both books

> **Insight #2: Thirteen markets, one branch**
> **Evidence:** §3A — `paymentChannel = isOverseas.value ? PaymentChannel.AIRWALLEX : PaymentChannel.ALIPAY`, with `STRIPE` and `PAYERMAX` referenced **zero** times in that chunk + §1 — 13 non-China markets above 1% traffic, India the only large one growing.
> **Pain Point:** Every non-China market shares one acquirer, one currency and one method set. India, Korea, Indonesia and Pakistan are treated identically to Germany. There is no mechanism in the code to do anything market-specific, so improving any single market means a code change, not a config change.
> **Yuno Value Proposition:** Per-market routing and method sets behind the abstraction they already built — config, not a release.
> **Best Success Case:** Match on "already multi-PSP, wants per-market routing".
> **Outreach Angle:** *"There's one line in your pricing component that decides how the entire world outside China pays. I'm curious whether that was a deliberate simplification or just the thing nobody's got to yet."*
> **Suggested Subject Line:** One ternary for thirteen markets

> **Insight #3: The slot for local rails exists, and it's empty**
> **Evidence:** §3A — `PAYMENT_CHANNEL_PAYERMAX = 7`, the **highest enum value and therefore newest**, present in the `overseas` array and the label map but **referenced by no selection, checkout or pricing code** + §3B — `growth.pay.v1.PayService` already takes `payment_channel` on every RPC.
> **Pain Point:** Somebody added an emerging-markets acquirer to the enum and it never reached the checkout. The abstraction is ready; the integrations aren't. Each one is a hand-built channel in their own service.
> **Yuno Value Proposition:** One integration behind the abstraction they already have, instead of PayerMax-then-the-next-one-then-the-next.
> **Best Success Case:** n/a — this is an architecture argument.
> **Outreach Angle:** *"PayerMax is in your payment-channel enum but nothing selects it. Did that stall, or is it waiting on something?"* — a genuine question, and they will know the answer.
> **Suggested Subject Line:** ⚠️ Keep this one in the body. Naming their enum in a subject line reads as surveillance.

> **Insight #4: A US acquirer is a concentration risk they can name internally**
> **Evidence:** §6 — a sitting Treasury Secretary said **Entity List designation is "on the table"** for Chinese AI firms, with Moonshot specifically alleged by the White House OSTP director to have breached chip controls + §3A — **Stripe (a US acquirer) is the sole processor on their international API funnel**.
> **Pain Point:** If designation ever happened, the API revenue line loses its only processor overnight. This is not a hypothetical they need convincing of — they have already added Airwallex and put PayerMax in the enum.
> **Yuno Value Proposition:** Acquirer redundancy and instant failover that is not dependent on any single jurisdiction's posture.
> **Outreach Angle:** ⚠️ **Handle with care and never state the allegations as fact.** Frame as resilience: *"single-acquirer dependency on any one jurisdiction"*. Let them supply the context.
> **Suggested Subject Line:** ⚠️ Do not put this in a subject line at all.

### Quick Hits

**Email hooks**
1. Your App Store listing prices Kimi in rupees, won and Taiwan dollars. Your own checkout prices it in US dollars.
2. One ternary — `isOverseas ? AIRWALLEX : ALIPAY` — decides how thirteen markets pay.
3. PayerMax sits in your payment-channel enum and nothing in the codebase selects it.

**Cold call openers**
1. *"I had a look at how Kimi handles payments outside China — it's a single branch to one acquirer. Was that deliberate, or just where it's got to?"*
2. *"Apple sells your membership in rupees. Does the web path in India convert anywhere near the app?"*
3. *"Your China invoice console works and the international one returns a 404. Is overseas invoicing still being built?"*

---

## Section 11: Similar Companies & Prospecting Pipeline

### 11A. Direct Competitors — Chinese frontier LLMs
| Company | Website | HQ | Overlap markets | Known PSP/Orchestrator | Source |
|---|---|---|---|---|---|
| **Z.ai / Zhipu** | z.ai | Beijing | Global | **Stripe + PayPal, USD-only, in-house motion** | `2-ready-to-outreach/z-ai.md` — 🔴 **BLOCKED, BIS Entity List** |
| **MiniMax** | hailuoai.video | Shanghai | Global | **Stripe, USD-only, in-house** | `2-ready-to-outreach/minimax-io.md`, 23/29 ⭐ |
| DeepSeek | deepseek.com | Hangzhou | Global | ⬜ not established | — |
| Alibaba Qwen · ByteDance Doubao · Baidu Ernie · StepFun · 01.AI | — | China | China + global | ⬜ not established | — |

⚠️ **The competitor agent had not reported when this file was written** — 11B, 11C and 11D are thin for that reason.

**Prior repo finding that matters:** Z.ai and MiniMax both run **Stripe, USD-only, no APAC local rails internationally**. The Chinese LLM cohort is **not** China-rails-only abroad — they all have the same gap. **Moonshot having Airwallex makes it the outlier in the cohort, not the laggard.**

### 11C. Companies Recently Adopting Payment Orchestration
**"No public case studies found of direct competitors adopting payment orchestration."** Prior repo research checked Gr4vy, Spreedly and Primer customer lists directly — no AI or LLM company on any of them.

### 11D. Top Prospect Pipeline
| Rank | Company | Type | Score | In TAL? |
|---|---|---|---|---|
| 1 | **Moonshot AI / Kimi** | Target | **22/29 ⭐** | ❌ **new — add at P1** *(already recommended at P1 in `z-ai.md` line 629)* |
| 2 | MiniMax | Peer | 23/29 ⭐ | ✅ own file |
| 3 | Z.ai | Peer | 23/29 ⭐ | ✅ own file — 🔴 compliance hold |
| 4 | DeepSeek | Peer | ⬜ | ❌ — `z-ai.md` recommended **P2 on reachability, not fit** |

---

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|---|---|---|
| Annual Revenue / ARR | ⚠️ **No company-issued figure exists.** A ">$1B ARR" figure circulates (Aug 2026) and ~$100m→$300m ARR growth is press-reported — **all unverified. Do not use in an email** | press only |
| GMV | N/A — subscription + prepaid API | — |
| **Consumer pricing (iOS, localised)** | **US** $19/$39/$99/$199 · **India** ₹1,999/₹3,999/₹9,900/₹19,900 · **Korea** ₩25,000/₩33,000/₩55,000 · **Taiwan** NT$590/NT$1,290 | Apple storefronts, per country |
| **Web pricing** | **USD only** internationally; CNY in China. Two currency branches exist in the codebase | ✅ verified by me |
| API pricing | **Intl (USD):** k3 $3.00 in / $15.00 out / $0.30 cached per 1M tok; k2.7-code $0.19 hit / $0.95 miss / $4.00 out. **China (CNY):** ¥1.30 / ¥6.50 / ¥27.00 / ¥1.10 per MTok | ✅ hardcoded `USDConfig` / `CNYConfig`, read by me |
| Prepaid tier ladder | **USD $1 → $3,000** intl · **¥0 → ¥20,000** China. Min $1 to start | platform docs |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ~150,000/month. [ASSUMPTION — not researched.]** Basis: reported app MAU 10–15m (third-party, **tracker unattributable**) at any plausible paid conversion, plus API top-ups. **Billing unit: membership charges + prepaid top-ups.** App-store IAP may not appear in their own count | Band ≥100,000 → +5, row marked ⚠️ |
| Active users | ⚠️ **No absolute count from any source.** Growth rates only (paid users +170% MoM to 2025-12-31; individual paid orders +8,280% MoM in January) — **unusable for sizing without a base** | press |
| Primary Currency | **USD** internationally, **CNY** in China | ✅ verified |
| Top 3 markets by traffic | US 12.71% · India 7.77% · Korea 3.97% ⚠️ *of the corporate site* | supplied SimilarWeb |
| **Billing channel split (web vs app store)** | ⚠️ **NOT DISCLOSED — and it is the biggest hole in the business case.** Apple IAP is where localised pricing happens and the StoreKit integration is deep. The API funnel is web by construction | — |

---

## Overall Research Confidence

**HIGH on the payment stack and routing. MEDIUM on entities and corporate. LOW on traffic, users and revenue.**

- **Payment stack — HIGH.** The protobuf service definition, the `PaymentChannel` enum, the region ternary, the routing map, the currency predicates and the invoice-console asymmetry were all pulled and read by me from live production assets with 404-body checks. Two independent agents reached the same conclusions from different bundle hashes (cn vs oversea builds).
- **Traffic — LOW, and structurally so.** **Supplied, but for the wrong property.** `moonshot.ai` is the corporate site; `kimi.com` and both platform hosts are excluded. I have used the country split only directionally and marked every dependent claim accordingly. **This is the single most valuable thing to re-supply.**
- **Entities — MEDIUM.** Primary documents, but the Novascent/Moonshot AI Pte. Ltd. relationship is inference and no PRC USCC was found.
- **Users and revenue — LOW.** No company-issued figure of any kind exists. Everything circulating is press-reported growth rates without bases.
- **Complaints and competitors — INCOMPLETE.** One agent had not reported.

---

## Manual Research Recommendations

> **Area:** Confirm the monthly transaction count
> **Why it matters:** It is the only ICP signal that can reject an account, and it is currently an **assumption**. Everything else in this file is stronger than this row.
> **Suggested action:** Ask in discovery. No public figure exists.

> **Area:** Re-supply SimilarWeb for `kimi.com` with "include all country domains" ON
> **Why it matters:** The current dataset is the marketing site. The country profile drives the APM analysis and two ICP signals, and right now it describes where people *read about* Kimi, not where they pay.
> **Suggested action:** Two minutes in SimilarWeb. Highest-value single action on this account.

> **Area:** What Airwallex actually renders in India and Indonesia
> **Why it matters:** It is the difference between "nothing in your stack references a local rail" (defensible) and "you don't support UPI" (correctable in one line by the prospect). This repo has already shipped that mistake once on another account.
> **Suggested action:** VPN to India and Indonesia, open the membership checkout, screenshot the method list. **Do this before the first email.**

> **Area:** Is Airwallex still taking new overseas volume?
> **Why it matters:** The code defaults new overseas API subs to Stripe and keeps Airwallex for downgrades on existing subscriptions. If a migration is underway, the timing is unusually good.
> **Suggested action:** Ask it directly — it is the best opening question on this account.

> **Area:** The web vs app-store billing split
> **Why it matters:** Apple IAP is where localised pricing lives. If IAP dominates consumer revenue, the orchestrable share is smaller than the headline.
> **Suggested action:** Ask in discovery.

> **Area:** Export-control status before contracting
> **Why it matters:** Not on any list today, but a sitting Treasury Secretary named Entity List designation as on the table. It is a watch item for legal, not a blocker for outreach.
> **Suggested action:** Flag to Yuno compliance **before contracting**, not before emailing.

---

## Appendix: All Source URLs

**Payment stack (source code, all fetched):** `statics.kimi.ai/kimi-web-seo/assets/kimi.utils-DGHI4XwS.js` · `.../Pricing-Wdoe70Yp.js` · `.../subscription-Cmx3G86j.js` · `.../en-US-DPuVS8An.js` · `statics.moonshot.cn/kimi-web-seo/assets/kimi.utils-DvtesH0I.js` · `.../Pricing-CTi6ML3A.js` · `.../Checkout-Bq3o8JbC.js` · `platform.kimi.ai/_next/static/chunks/5291-8800918ab632513d.js` · `platform.kimi.com/_next/static/chunks/9867-007fa5375112b804.js`

**Their own documents:** [kimi.ai ToS v2](https://www.kimi.ai/user/agreement/modelUse?version=v2) · [platform.kimi.ai developer ToS](https://platform.kimi.ai/docs/agreement/modeluse) · [China recharge agreement](https://platform.kimi.com/docs/agreement/payment) · [intl billing FAQ](https://platform.kimi.ai/docs/guide/account-and-payments) · [SDK sharing list](https://kimi-img.moonshot.cn/prod-chat-kimi/kimi/sdk_sharing_list_v2_en.md) · [platform changelog](https://platform.kimi.ai/docs/platform-changelog) · [kimi.com/aicard](https://www.kimi.com/aicard)

**Stores:** [iOS id6474233312](https://apps.apple.com/us/app/id6474233312) (US/IN/KR/TW/SG/AU storefronts) · [Google Play](https://play.google.com/store/apps/details?id=com.moonshot.kimichat)

**Rail prominence:** [PIB — UPI](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2257087&reg=3&lang=2) · [NPCI](https://www.npci.org.in/product/upi/product-statistics) · [Statista — Korea](https://www.statista.com/statistics/1061986/south-korea-most-commonly-used-mobile-payment-providers/) · [KOMOJU — Korea](https://en.komoju.com/blog/general-advice/korea-mobile-payment-trends/) · [Katadata/BI — QRIS](https://databoks.katadata.co.id/en/finance/statistics/6a2631bbc1a3f/the-number-of-qris-users-increased-74-in-the-q4-2025) · [VIR — Vietnam](https://vir.com.vn/e-wallet-players-look-to-take-hold-of-market-gaps-113427.html) · [Antom — Taiwan](https://www.antom.com/guides/markets/taiwan) · [PaymentBrief — Bangladesh](https://paymentbrief.com/markets/bangladesh/)

**Corporate / compliance:** [36Kr — Stripe data](https://36kr.com/newsflashes/3714143264059528) · [21世纪经济报道 — Kimi AI Card](https://m.21jingji.com/article/20260710/herald/b378a98708940e9b5ff48aa4046dd468.html) · [界面新闻](https://www.jiemian.com/article/14743063.html) · TechCrunch 2026-07-22 (export-control allegations) · TechNode 2026-09-03 (HKEX A1)

**Traffic:** `accounts/traffic/moonshot-ai.md` (SimilarWeb, supplied 2026-09-30)

</details>
