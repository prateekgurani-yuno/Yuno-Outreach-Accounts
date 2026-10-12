# RedteaGO

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 17 / 29 → ⭐ **High Priority** — ⚠️ **boundary score. Strip the two weakest rows and it is 13 🟢. Read the ICP table before pitching.**
**Industry:** Telecommunications — consumer travel eSIM / prepaid mobile data (brand of the Redtea Mobile Group) · **HQ:** contracting entity **Hong Kong** (eSIM Access Limited, Central); app-store seller **Singapore** (Redtea Mobile Pte. Ltd.); group copyright holder **Shenzhen** (深圳杰睿联科技有限公司) · **Researched:** 2026-10-11 · **First email sent:** —
**Motion:** 🛑 **IN-HOUSE — they built the multi-PSP abstraction themselves.** Server-returned payment-method list, numeric `payMethod` enum, per-vendor redirect routes, one unified execute/confirm/status API across four acquiring paths. **Never say they need orchestration.**

---

> ## ⭐ THE CENTRAL QUESTION — SETTLED: the China traffic is a Chinese-language app-handoff funnel with a confirmed locale-redirect hop. **There is NO WeChat or Alipay Mini Program.**
>
> The supplied SimilarWeb row — **China 74.32%, 6-second visits, 1.53 pages, 81.59% bounce** — was right to be flagged. Here is what is actually there, in order of evidential strength.
>
> ### 1. ✅ CONFIRMED and reproducible: the storefront 302-redirects every Chinese-language browser
> `esim.redteago.com/` returns **HTTP 302 → `/zh-CN`** with `set-cookie: i18n_redirected=zh-CN` for any browser sending `Accept-Language: zh-CN`. Verified twice from this session — once with a zh-CN Android UA, once with a WeChat in-app UA (`MicroMessenger/8.0.49`). An English-language browser gets a plain `200` and `i18n_redirected=en`, no redirect.
> > ⚠️ **CORRECTED BY THE ORCHESTRATOR, 2026-10-12 — the redirect is real but it does NOT explain the supplied traffic data.**
> >
> > The 302 is confirmed. I reproduced it myself: `esim.redteago.com` returns `200` to `Accept-Language: en-US` and **`302` with `location: /zh-CN`** to `Accept-Language: zh-CN`.
> >
> > **But SimilarWeb measured `redteago.com`, not `esim.redteago.com`, and `redteago.com` does NOT redirect.** I tested both headers against the measured property: **English `200`, Chinese `200`, no `Location` header either way.** The locale hop happens on a host that was never in the dataset, so it cannot be the mechanical cause of the 1.53 pages per visit in the supplied table.
> >
> > **What DOES survive on the measured property is the app hand-off.** `redteago.com` carries an `apple-itunes-app` Smart App Banner plus `apps.apple.com` and `play.google.com` links, and **sells nothing at all** — 149 `wp-content` hits, zero for `stripe`, `checkout`, `cart` or `buy now`. A visitor lands on a brochure page, taps into an app store, and the session ends. **That genuinely produces ~1.5 pages and a 6-second visit, and it is the explanation that fits the data we actually have.**
> >
> > 🚩 **Keep both facts, and keep them apart.** The locale 302 is a real finding about the storefront and belongs in a checkout conversation. It is **not** the explanation for the traffic table, and presenting it as one would be a causal claim about data it does not touch.
>
> ### 2. ✅ CONFIRMED: the funnel's purpose is to hand the visitor to an app — and in China it has to be an APK
> - `redteago.com` carries an **Apple Smart App Banner** (`apple-itunes-app` meta) — an OS-level app-install prompt on iOS Safari.
> - Both the marketing site and the storefront link to **`apps.apple.com/.../id1492864476`**, **`play.google.com/.../com.redteamobile.redteago`** and — the tell — **`www.pgyer.com/RedteaGOeSIM`**.
> - **Pgyer (蒲公英) is a Chinese third-party APK distribution host.** It serves a direct **RedteaGO APK, v2.5.3 (build 3), 20.5 MB, published 2025-06-20**. They publish an APK channel *because Google Play is unavailable in mainland China.*
> > 🔑 **Google Play is not reachable in mainland China, so the "100K+ downloads" on the Play listing systematically excludes RedteaGO's single largest audience.** Any sizing built on that number is wrong by construction.
> >
> > 🚩 **And the China-accessible Android build is stale: Pgyer is on 2.5.3 (Jun 2025) while Google Play is on 2.5.17.** Fourteen versions of drift on the channel serving 74% of the traffic.
>
> ### 3. ✅ CONFIRMED: the Chinese audience is real and deliberately served — this is not an accident of measurement
> | Evidence | Detail |
> |---|---|
> | Full Chinese localisation | `hreflang` set is `en, de, es, ja, tr, zh-CN, zh-HK` — **two Chinese locales out of seven.** UI locale map: `{"zh-CN":"中文(简体)","zh-HK":"中文(繁体)"}` |
> | CJK byte density | **~19,000 CJK bytes** on `/zh-CN` vs **7** on `/` (raw-byte count, `\xe5`–`\xe7`). Fully translated, not machine-stubbed |
> | Chinese-language Terms of Service | §4.1 translated verbatim, naming 支付宝 / 微信支付 |
> | Chinese email providers wired into signup | `mail.qq.com`, `mail.163.com`, `mail.126.com` shortcuts in the client bundle |
> | Chinese support stack | Udesk widget on **`redteamobile.udesk.cn`** — a `.cn` domain under the `redteamobile` tenant |
> | CNY display currency | `supportCurrency.CNY` present with a hard-coded rate |
> | Group structure | **Redtea Mobile Group**, formed 28 Jan 2026, operates as **Redtea Mobile Global + Redtea Mobile China**, described as *"the first chapter of the Group's 'local for local' setup"* |
>
> ### 4. 🛑 RULED OUT as far as it can be: **no WeChat Mini Program, no Alipay Mini Program**
> Searched for explicitly, as instructed, five ways:
> - `小程序` (mini program) → **0 occurrences** in the en storefront, the zh-CN storefront, the marketing site, or any of 13 JS bundles.
> - `weixin://`, `alipays://`, `intent://` deep links → **0**.
> - `wechat` / `weixin` as a *platform* reference (not a payment method) → **0**.
> - A WeChat in-app UA gets the ordinary web storefront with the same locale 302 — **no Mini Program hand-off, no JSSDK, no `wx.config`**.
> - Chinese-language web search for a RedteaGO 微信小程序 returned nothing. [UNVERIFIED — search summary only, page not fetched]
> > **Conclusion: no Mini Program surface found.** Absence cannot be proven absolutely from outside, but every available first-party probe is negative. **This is NOT a hidden second payment surface. The reframing the brief anticipated does not happen.**
>
> ### 5. ⚠️ NOT excluded — be honest about these in the call
> - **Crawler/bot traffic.** Cannot be measured from here. A 6-second/81.59% profile is also what bot traffic looks like, and nothing rules it out.
> - **A CN-side block or interstitial.** `redteago.com` and `esim.redteago.com` both return `200` from this session with no geo-interstitial — **but this session is not on a Chinese IP.** A GFW-side degradation would be invisible to me and would independently explain a 6-second session. **Untestable without a mainland vantage point. Put it on the discovery call.**
>
> ### 🎯 The reading to take into outreach
> **This is not four accounts. It is one account whose largest market is a Chinese-language audience being funnelled into an app through a measurement-hostile redirect, and whose money nonetheless leaves China as a USD cross-border charge.** The country rank corroborates the volume — **China #11,055 and Hong Kong #31,529 are far stronger ranks than the US at #293,759** — so the audience is real even though the sessions read shallow.

---

> ## ⭐ THE PAYMENT FINDING — four acquiring paths, one home-built abstraction, and every cent settled in USD
>
> **Their own Terms of Service (English and Chinese, last updated 6 May 2026) name the processors:**
> > *"RedteaGO supports payment methods including credit cards, Alipay, WeChat Pay, and PayPal. **All transactions are settled in US dollars (USD).** Payment transactions are processed and secured by platforms such as **Stripe, PayPal, WeChat Pay, and Alipay.**"*
>
> **And their production code names a fourth and fifth:**
> ```
> /v1/payment/nuvei/options      → NUVEI  (country → local-method picker)
> /v1/get/payparam/adyen-pay     → ADYEN  (payparam fetch)
> js.stripe.com/v3 + stripe.elements() + stripe.confirmCardPayment()   → STRIPE
> paypalPay()                    → PAYPAL
> ```
> Plus seven locale-specific **`/nuvei-jump`** redirect routes registered in the production router, and `authResult=AUTHORISED` in the success-URL template — **Adyen's HPP result vocabulary.**
>
> ### 🔑 Nuvei is doing the APM breadth, and the UI admits it
> `/v1/payment/nuvei/options` returns a **country → payment-methods** structure (`areaName`, `areaCode`, `paymentMethods[].paymentName/.paymentCode`), rendered as a two-step *"select country, then select method"* picker. When `payMethod === 14`, the client attaches `areaCode` + `paymentCode` and redirects through `/nuvei-jump`.
> > **They bought their local-rail coverage from Nuvei rather than integrating rails directly — and they bolted it on as a separate, redirect-based "id 14" branch beside their own card flow.** That is the seam.
>
> ### 🔑 The abstraction is theirs, which sets the motion
> One unified API spans all four paths: `/v1.1/query/payments` (server returns the available method list) → `/v1.1/setup/payment` → `/v1.1/execute/payment` → `/v1.1/payOrder/confirm` → `/v1.1/query/payment-status`. The client routes on a **server-supplied numeric `payMethod` enum**, and a `samePagePayment: [5, 6]` constant classifies which methods render in-page versus redirect.
> **Resolved from the code: `6` = card via Stripe Elements · `5` = RedteaGO Credit wallet balance · `14` = Nuvei local method.** The rest of the enum is server-side and not enumerable from the client.
> > **They have hand-rolled the multi-PSP abstraction Yuno sells. Motion is IN-HOUSE. Do not pitch orchestration as a concept — pitch reach and opportunity cost.**
>
> ### 🎯 THE HOOK — they localise the price tag and the language, and then charge everyone in dollars
> A constant literally named **`supportCurrency`** carries **13 display currencies with hard-coded FX multipliers**, off `baseCurrency: "USD"`:
> ```
> USD 1 · GBP .74 · JPY 147.57 · THB 32.41 · TRY 40.84 · KRW 1385 · HKD 7.79
> SGD 1.29 · RUB 80.4 · INR 87.46 · CAD 1.38 · CNY 7.13 · EUR .86
> ```
> ⚠️ **This is NOT the Flexiroam country-metadata trap** — the key is named `supportCurrency`, it sits in the payment/pricing state store, and every entry carries an FX `value`. It is a display-conversion table, and it is load-bearing.
>
> **But their Terms say settlement is USD, in both languages.** So:
> > **A Chinese customer is shown ¥, a Korean customer ₩, an Indian customer ₹ — and all three are billed a cross-border USD charge.** Local price tag, foreign card charge. The customer eats the issuer FX spread and the cross-border fee, and RedteaGO eats the cross-border decline rate on top. **That asymmetry is their own code contradicting their own currency menu, and it is the single best opener on this account.**
>
> 🚩 **And the rates are hard-coded client-side constants.** They are stale the moment FX moves, until someone redeploys the bundle.

---

> ## 🛑 THE STUB AND THE TAL — what held and what did not
>
> | Source says | Finding | Verdict |
> |---|---|---|
> | HQ Hong Kong | ✅ **The contracting entity is Hong Kong** — *"eSIM Access Limited ... located at ROOM B 16/F EUBANK PLAZA 9 CHIU LUNG STREET CENTRAL HK"* | **HELD** — in territory |
> | "Consumer brand of eSIM technology firm Redtea Mobile" | ✅ Directionally right, but the entity is **not** Redtea Mobile. See below | **REFINED** |
> | "Sold app-first" | ✅ Confirmed — Smart App Banner, three app channels, 100K+ Play installs | **HELD** |
> | "Prepaid data plans" | ✅ Confirmed — Terms cover *"all prepaid services"*; **zero** recurring/mandate/saved-card tokens anywhere | **HELD** |
> | **"~$30M est. revenue"** | 🛑 **NOT VERIFIED AND NOT VERIFIABLE.** No revenue figure is published for RedteaGO, eSIM Access Limited or Redtea Mobile anywhere I could reach. CB Insights lists revenue as not disclosed. A third-party aggregator estimate of $37.5m surfaced in a search summary but also places HQ in Singapore while CB Insights places it in Shenzhen — **the source is unreliable and I am not carrying it forward** | **UNVERIFIED — do not quote $30M** |
>
> ### ⚠️ The entity question the brief asked me to settle: **which entity takes the consumer's money?**
> **It depends on the channel, and that is itself the finding.**
>
> | Channel | Entity that contracts / collects | Source |
> |---|---|---|
> | **Web (`esim.redteago.com`)** | **eSIM Access Limited**, d/b/a RedteaGO, Hong Kong | Terms of Service + Privacy Policy, first-party |
> | **iOS app** | **REDTEA MOBILE PTE. LTD.** (Singapore) | Apple App Store seller field |
> | **Android app** | **REDTEA MOBILE PTE. LTD.** (Singapore) | Google Play developer field |
> | Group copyright holder | **深圳杰睿联科技有限公司** (Shenzhen) | `redteamobile.com` footer |
>
> 🔑 **The consumer-facing brand's billing entity is the group's B2B wholesale entity.** `esimaccess.com` — linked from RedteaGO's own homepage — describes eSIM Access as *"an overseas SaaS platform"* and a **B2B eSIM aggregator** that lets *"reseller partners to access the full offering of roaming data plans from Redtea Mobile."* Redtea Mobile's own site lists **"For Consumers: RedteaGO"** and **"For Travel Partners: eSIMAccess"** as separate product lines in the same portfolio. **So one Hong Kong entity, eSIM Access Limited, is simultaneously the B2B wholesale platform and the consumer contracting party — while the app stores bill through a Singapore entity.**
>
> ✅ **Phase 0 verdict holds and is reinforced: this is a telecom merchant that ACCEPTS payments. The B2B arm sells eSIM/connectivity infrastructure, not payment infrastructure. IN ICP. No Partnerships hand-off.**
>
> ⚠️ **One live confusion to avoid.** Redtea Mobile uses the word **"orchestration"** for its own product — *"end-to-end orchestration of eSIM profiles, devices, and connectivity across complex, multi-operator environments."* **If Prateek writes "orchestration" cold, they will read it as eSIM orchestration and assume he has not understood the company.** Lead with routing, acquiring, approval rates and settlement currency — never the bare word.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** RedteaGO is the consumer travel-eSIM brand of the Redtea Mobile Group, selling prepaid mobile-data plans for 180–200+ countries through `esim.redteago.com` and iOS/Android apps. Plans are one-off prepaid purchases at very low ticket — destination entry prices run **$0.10–$8.80** — topped up through a **RedteaGO Credit** stored-value wallet. The web storefront contracts through **eSIM Access Limited (Hong Kong)**, which is also the group's B2B eSIM wholesale platform; the app stores bill through **Redtea Mobile Pte. Ltd. (Singapore)**.

**SimilarWeb total visits (last full month):** 🛑 **NOT AVAILABLE.** The supplied dataset is **shares only — the total visit count is not shown.** Period Jul–Sep 2026, scope `redteago.com`, 34 countries, "include all country domains" **OFF**. Source: SimilarWeb (supplied 2026-10-11).
⚠️ **This is a hard limit on this account.** With no denominator, no absolute volume, no transaction count and no revenue can be derived from traffic. Said plainly rather than papered over.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇨🇳 China | **74.32%** ⚠️ *engagement-suspect; see the headline* | **Alipay ✅, WeChat Pay ✅** (Terms §4.1, EN + zh-CN) · UnionPay brand mark on the pay page · cards via Stripe · PayPal | **Domestic RMB settlement** — all transactions settle in USD by their own Terms, so this is cross-border collection, not a domestic rail gap | ❌ No consumer-contracting entity in mainland China. *Redtea Mobile China* exists as a group **operating organisation** (28 Jan 2026) but is described as smartphones / connected vehicles / industrial IoT, not consumer eSIM retail. ⚠️ **Whether mainland domestic acquiring is licence-gated could NOT be established from a current primary source — claim omitted, see Section 2** |
| 2 | 🇺🇸 United States | 6.30% | Cards (Stripe Elements), Apple Pay, PayPal | Nothing material — cards and wallets are the US rails | ❌ None found |
| 3 | 🇦🇺 Australia | 2.17% ▼26.56% | Cards, Apple Pay, PayPal | **PayTo, BPAY, Afterpay, Zip — all 0 occurrences** across storefront, Terms and 13 JS bundles. ⚠️ Absence is sourced first-party; **the rails' domestic prominence is NOT sourced**, so this is not scored | ❌ None found |
| 4 | 🇩🇪 Germany | 1.89% | Cards, Apple Pay, PayPal | SEPA direct debit, Klarna, giropay — not found. *(Out of APAC territory)* | ❌ None found |
| 5 | 🇮🇳 India | 1.78% ▲**474.90%** | Cards, Apple Pay, PayPal · **INR display currency present** | **UPI, RuPay, netbanking, EMI — all absent.** `upi` returned 8 raw hits, **all spurious** (`TopupIdx`). **No Hindi UI locale** despite being the fastest-growing market | ❌ None found |

### Legal entities
- **eSIM Access Limited** (Hong Kong) — d/b/a RedteaGO; registered office ROOM B, 16/F, Eubank Plaza, 9 Chiu Lung Street, Central, HK. **Registration number: not found** (no reachable HK Companies Registry record)
- **Redtea Mobile Pte. Ltd.** (Singapore) — Apple/Google app-store seller; address given on the Trustpilot profile as 29 Media Circle #02-14/15 Alice@MediaPolis, 138565. **UEN: not found**
- **深圳杰睿联科技有限公司** (Shenzhen, China) — copyright holder in the `redteamobile.com` footer. **Registration number: not found**
- **Redtea Mobile Group** — holding structure announced 28 Jan 2026, comprising *Redtea Mobile Global* and *Redtea Mobile China*. **No legal entity names disclosed in the release**

### Known PSPs
- **Stripe** — `[Source Code]` + `[Terms/Privacy Policy]`. `js.stripe.com/v3`, `stripe.elements()`, `stripe.confirmCardPayment()` on the pay page; a **live publishable key** sits in the production config (🔒 vendor named, value deliberately not transcribed). Named in the Terms in both languages. Card rail, global
- **Nuvei** — `[Source Code]`. `/v1/payment/nuvei/options` (country → local-method picker) + seven locale `/nuvei-jump` redirect routes + `payMethod === 14` branch. **Alternative/local payment methods, global.** ⚠️ Not named in the Terms — code-only, but unambiguous
- **Adyen** — `[Source Code]`. `/v1/get/payparam/adyen-pay`, corroborated by `authResult=AUTHORISED` in the success-URL template (Adyen HPP vocabulary). ⚠️ **Single endpoint. Live status not established** — it may be a secondary or legacy path
- **PayPal** — `[Source Code]` + `[Terms/Privacy Policy]`. `paypalPay()` on the top-up page; named in the Terms in both languages
- **Alipay** and **WeChat Pay** — named as *processing platforms* in Terms §4.1 (both languages). ⚠️ **No separate SDK or endpoint found; the acquiring route to them is not established** — Stripe and Nuvei both offer them as cross-border methods, and the USD settlement clause is consistent with either
- ❌ **NOT FOUND** anywhere: Airwallex · Braintree · Checkout.com · Worldpay · Razorpay · PayU · Cashfree · 2C2P · Xendit · Midtrans · iPay88 · Omise · GMO · KOMOJU · Toss · eWAY · Windcave · Payssion · PingPong · LianLian · Oceanpayment · AsiaBill · Cybersource

### Orchestration status
**In-house orchestration layer.** `[Source Code]` — one unified API (`/v1.1/query/payments` → `/v1.1/setup/payment` → `/v1.1/execute/payment` → `/v1.1/payOrder/confirm` → `/v1.1/query/payment-status`) spanning four acquiring paths, a server-supplied numeric `payMethod` enum the client routes on, a `samePagePayment: [5,6]` in-page-vs-redirect classifier, and per-vendor redirect routes. **No third-party orchestrator: Juspay, Spreedly, Primer, Gr4vy, Payrails, Corefy, CellPoint, APEXX and Yuno all return 0 occurrences across every fetched asset.** ⚠️ Whether the layer does *routing* — retry, failover, cascading — is server-side and **could not be established.** It may be a method-selection shim rather than a router.

### Buying signals
- 🏢 **Redtea Mobile Group formed 28 Jan 2026**, split into *Redtea Mobile Global* and *Redtea Mobile China* on a stated *"local for local"* model, with a new group C-suite (Group CEO Hui Jin; Group CFO **Rico Zhong**; Group COO Qinghua Peng; Group CMO Xiaodong Guo; Global CEO Rob Varty; Global CTO Edwin Haver) — [redteamobile.com/news/post21](https://redteamobile.com/news/post21/)
- 🚀 **India +474.90% in one quarter with the best engagement in the whole table** (11.92% bounce, 4.83 pages) — and **no UPI, no RuPay, no Hindi locale.** SimilarWeb (supplied 2026-10-11)
- 💱 **13 display currencies against USD-only settlement**, FX rates hard-coded client-side — a self-inflicted cross-border cost they can see in their own dashboard
- 🤝 **Nuvei carrying local-method breadth as a bolted-on redirect branch** while cards run in-page through Stripe — two-tier checkout, two-tier conversion
- ⚠️ **Trustpilot has suppressed their score** *"due to a breach of our guidelines"* (74 reviews, 35% one-star) — reputational pressure on refund handling
- 🛑 **NO funding signal.** Latest round is **Series B, 7 July 2022**; $10M total across 4 rounds (CB Insights). **Do not pitch a funding trigger.**
- 🛑 **NO job-posting signal.** No payment-related — or any — openings found.
- 🛑 **NO public payment RFP found.**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach RedteaGO` to draft the 12-touch sequence, or call this from `/prepare_batch`.*

> **Three constraints to carry into the sequence when it is written:**
> 1. **Motion is IN-HOUSE.** They built the abstraction. Per `/full-outreach` Step 6a, respect the build decision — anchor on reach, coverage and opportunity cost. Never imply they lack orchestration.
> 2. **Never use the bare word "orchestration."** Redtea Mobile sells "eSIM orchestration." It will read as a category error. Say routing, acquiring, approval rate, settlement currency.
> 3. **The opener is the currency asymmetry**, not China. Thirteen display currencies, USD-only settlement, in their own Terms and their own code. It is verifiable, specific, and they cannot dispute it.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 17 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+2 / 5** | ⚠️ **NOT FOUND — ASSUMED ~40,000–50,000/month. `[ASSUMPTION — not researched]`** Scored at the conservative **40,000–49,999 (+2)** band. **Basis:** no transaction, order, subscriber, activation, ARPU or revenue figure is published by RedteaGO, eSIM Access Limited or Redtea Mobile; the supplied SimilarWeb dataset gives **shares only with no total**; and both derivation paths fail — revenue is unverified and average ticket is unknown. The only sourced volume proxies are **Google Play 100K+ lifetime installs** and **893 Apple ratings / 1.24K Play reviews**, and the Play figure **excludes mainland China entirely because Google Play is unavailable there** — i.e. it omits 74% of the audience by construction. **Billing unit counted: one prepaid data-plan purchase, plus RedteaGO Credit wallet top-ups as a second unit.** 🛑 **Per the disclosure rule, an ASSUMED figure cannot trigger the under-40,000 rejection, and it does not. This is the #1 item for the discovery call.** |
| Orchestration status | **+1** | ✅ **In-house layer confirmed.** Unified execute/confirm/status API across Stripe, Nuvei, Adyen and PayPal; server-supplied `payMethod` enum; `samePagePayment` classifier; per-vendor redirect routes. No third-party orchestrator (9 vendors searched, all 0). Hardest-sell motion, lowest score — correctly |
| 3+ countries | **+3** | ✅ **Verified twice over.** Seven countries at >1% traffic share (SimilarWeb, supplied 2026-10-11) **and** three confirmed entity jurisdictions — HK (Terms), SG (app-store seller), Shenzhen (group footer) |
| Multiple PSPs | **+3** | ✅ **Four acquiring paths with first-party evidence.** Stripe (code + Terms), Nuvei (code), Adyen (code), PayPal (code + Terms) |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **Deliberate zero — do not inflate this row.** Top-3 markets are China (74.32%), US (6.30%), Australia (2.17%). **China's dominant rails are actually PRESENT** — Alipay and WeChat Pay are both named in their own Terms, and UnionPay carries a brand mark on the pay page — so there is no rail gap in the #1 market. **Australia's PayTo/BPAY/Afterpay/Zip absence IS sourced first-party (0 occurrences), but I could not source those rails' domestic prominence**, and the RBA page I checked publishes only spreadsheet links, no figures. **And no current primary source was found for a mainland-China domestic-acquiring licence gate, so that leg is unavailable too.** The India UPI gap is real and well-evidenced but India is #5 at 1.78%, outside top-3. **Uncertain = 0** |
| Recent expansion | **+2** | ⚠️ **Awarded, and it is one of the two weakest rows.** **Redtea Mobile Group** formed **28 Jan 2026** (inside 12 months), standing up **Redtea Mobile China** as a distinct operating organisation on a *"local for local"* model and stating an intent to extend into *"additional strategic markets over time"* — [source](https://redteamobile.com/news/post21/). **Caveat stated plainly: the release names NO new market, and the restructure is group-level and B2B-weighted, not a RedteaGO consumer market launch.** |
| Payment issues | **+2** | ⚠️ **Awarded, and it is the other weakest row.** Moderate-frequency **refund** disputes across Trustpilot 2025–2026 with dated instances, and Trustpilot has **suppressed the score outright** *"due to a breach of our guidelines"* (74 reviews, 35% one-star). **Caveat stated plainly: there are ZERO card-decline, checkout-failure or payment-processing complaints.** The pattern is refund handling and eSIM connectivity — service quality, not payment infrastructure |
| Funding >$10M | **0** | ❌ **Not met.** Latest round **Series B, 7 July 2022**; $10M total raised across 4 rounds (CB Insights). Nothing in the last 12 months |
| High traffic outside home | **+2** | ✅ **Met under both readings of the China row, which is why it is safe.** Home market is **Hong Kong** (the contracting entity's jurisdiction) at **1.68%** — far below the 60% threshold. ⚠️ **Disclosed ambiguity:** if one instead treated mainland China as "home" on the strength of the Shenzhen copyright holder, home would be 74.32% and this row would fail. I use Hong Kong because the **consumer-contracting entity** is Hong Kong per their own Terms, and the TAL agrees |
| Competitor using orchestration | **+2** | ✅ **The strongest verified row in the table.** **Airalo — the category leader — runs Primer, a global payment orchestrator.** 23 distinct `validations.primer.*` i18n keys in Airalo's own bundle, alongside 45 `validations.stripe.*` keys, a `paypal_enabled` feature flag and a live Stripe publishable key in config. See Section 11C for the full key list and the false-positive rebuttal |
| Payment job postings | **0** | ⬜ No payment-related openings found — in fact no openings found at all |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **⭐ High Priority (17)**

> ### ⚠️ Read the tier with this caveat attached
> **17 is the first point of the ⭐ band, and it rests on two rows I have flagged as weak** — *Recent expansion* (+2, a group restructure naming no new market) and *Payment issues* (+2, refund complaints with no payment-processing component). **Remove both and the account is 13 → 🟢 Medium.**
>
> **No analyst override is applied, and here is the reasoning rather than a verdict.** The override criteria do not cleanly fire: revenue is not app-store dominated (checked and cleared, below), there is no double-counting, and no market is regulatorily closed to Yuno on any evidence I could source. But *"absolute volume too small"* **cannot be assessed at all** — there is no denominator in the supplied traffic data and no published volume figure anywhere. **So the honest statement is conditional: if discovery returns under 50,000 transactions/month, this account is a 🟢 Medium, and if it returns under 40,000 it is not an ICP at all.** Treat 17 as a strong Medium / weak High until that one number exists.

### ✅ The app-store trap — checked, and the answer is split
**Orchestration CAN reach the web channel, and probably the iOS app. Google Play is the open question.**
1. **Apple: NO In-App Purchase enumeration.** The listing for `id1492864476` has a Price row and an App Privacy section but **zero occurrences of "In-App Purchases" or "Offers In-App Purchases."** Apple always enumerates IAP items when present — the same test that cleared Flexiroam.
2. **Google Play: "In-App Purchases" IS declared** — the label appears beside the content rating on `com.redteamobile.redteago`.
3. **Web: unambiguously card/APM-billed** through Stripe Elements, Nuvei, PayPal and Adyen. No StoreKit, Play Billing or RevenueCat tokens anywhere in the bundles.
> ⚠️ **That Apple-vs-Google discrepancy is real and I am not resolving it by assumption.** Prepaid mobile data is a real-world service, which is the category commonly exempt from app-store billing — and the opposite case the brief flagged. **The honest read:** the web channel and the iOS app are reachable by orchestration; the Android IAP declaration needs one question on the call. **Not a `not-icp` failure mode on this evidence** — but do not assert 100% card billing either.

### ✅ The subscription trap — checked, and cleared outright
**This is NOT a subscription business, and `.claude/reference/subscription-payments.md` does not apply.** Across the storefront, both locale renderings, five page HTMLs and 13 JS bundles: `setup_intent` **0** · `seti_` **0** · `subscription` **0** · `recurring` **0** · `auto-renew`/`autoRenew` **0** · `mandate` **0** · `saveCard`/`savedCard`/`cardOnFile` **0** · `tokeniz*` **0**.
Corroborated first-party: Terms cover *"all **prepaid** services"*; the zh-CN Terms state the contract *"automatically terminates when the purchased eSIM plan's validity expires"*; the Apple listing says *"No contracts or long-term commitments."*
**Billing units are therefore: (a) a one-off prepaid plan purchase, and (b) a RedteaGO Credit wallet top-up.** There IS a top-up/recharge flow (`/topup`, `/v1.1/data/create/topup-order`, `/v1.1/execute/topup/payment`) — but it is a **manual** prepaid reload, not an auto-renewing mandate. **High-frequency, low-ticket, bought at the moment of travel — exactly as the brief predicted.**

### Source Notes
- ✅ **Contracting entity, address, Terms date, payment-method list and USD settlement** — first-party Terms of Service and Privacy Policy, English and Chinese, last updated 6 May 2026
- ✅ **Stripe, Nuvei, Adyen, PayPal, the unified payment API, the `payMethod` enum, `supportCurrency`, the 1/10,000 USD minor unit** — first-party production code (storefront HTML + 13 `_nuxt` bundles, fetched 2026-10-11 into a clean directory)
- ✅ **The zh-CN 302 locale redirect** — reproduced twice in this session with two different user agents
- ✅ **Pgyer APK channel, version and date** — `www.pgyer.com/RedteaGOeSIM`, fetched and read
- ✅ **App-store sellers, install band, ratings, IAP status** — Apple and Google Play listings, fetched
- ✅ **Airalo's Primer + Stripe stack** — Airalo's own i18n table, 23 + 45 distinct namespaced keys
- ✅ **Group structure and executives** — company press release, 28 Jan 2026
- ⚠️ **Revenue: no figure. The TAL's ~$30M is unverified and I am not carrying it.**
- ⚠️ **Monthly transaction count: ASSUMED.** No denominator exists in the supplied traffic data
- ⚠️ **Adyen live status unconfirmed** — one endpoint, no second evidence type
- ⚠️ **The acquiring route to Alipay and WeChat Pay is not established** — named as platforms in the Terms, no SDK or endpoint found
- 🛑 **Mainland-China acquiring licensing: claim OMITTED.** The only source I could reach (IBA e-payment guide, published 1 March 2023) predates the 2024 non-bank payment regulations, describes requirements for *payment companies* seeking PRC market entry, and **explicitly does not address foreign merchants collecting from Chinese consumers.** `law.asia` returned 403. **Per the integrity rules I am stating no regulatory requirement.** What IS established is first-party and sufficient: **all transactions settle in USD**, which means cross-border collection either way
- 🛑 **No CSP headers on either host.** `redteago.com` and `esim.redteago.com` return no `content-security-policy`, `frame-ancestors`, `connect-src` or `form-action`. The `frame-ancestors` asset-map trick was checked and yields nothing here
- 🛑 **Signed-API enumeration not completed.** `/v1.1/query/payments` and `/v1/payment/nuvei/options` require a body-derived request signature; reconstructing it was **blocked by this environment's safety classifier and not retried.** **The authoritative server-side payment-method list and the full Nuvei country→method matrix are therefore NOT in this report.** This is the largest single gap in Section 4

### Success Case Alternatives
- **Low-ticket, high-frequency travel/connectivity merchant with USD-only settlement across a dozen display currencies** — the closest profile match. The business case is approval rate on cross-border authorisations plus FX leakage, not MDR.
- ⚠️ **No Yuno customer is named here.** Per the Yuno customer rule, only publicly referenceable customers may be cited and no number may be attached to one without published metrics. **Prateek should select the reference case from the internal list; I am not inventing one.**

---

## Executive Summary

RedteaGO is the consumer travel-eSIM brand of the Redtea Mobile Group, selling one-off prepaid mobile-data plans for 180–200+ destinations through a Hong Kong contracting entity (**eSIM Access Limited**) on the web and a Singapore entity (**Redtea Mobile Pte. Ltd.**) in the app stores. The central payment finding is a **home-built abstraction over four acquiring paths — Stripe for cards in-page, Nuvei for local methods by redirect, PayPal, and an Adyen endpoint — with a server-supplied payment-method enum the client routes on, and every transaction settled in USD against a thirteen-currency display table whose FX rates are hard-coded in the client bundle.** The orchestration opportunity is therefore not the concept but the reach: a 74%-Chinese audience and a 475%-growing Indian one are both being charged cross-border in dollars, with no UPI, no domestic settlement, and no local acquiring anywhere. **Motion: in-house** — they built the layer, so the argument is coverage, approval rate and opportunity cost, never the case for orchestration itself.

---

## Section 1: Website Traffic Analysis by Country

**Data source:** Path 1 — **pasted SimilarWeb data supplied by Prateek**, `accounts/traffic/redteago.md`. Used verbatim, **not re-researched**. Cite as "SimilarWeb (supplied 2026-10-11)". Period Jul–Sep 2026, scope `redteago.com`, 34 countries in dataset, **"include all country domains" toggle OFF**.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | 🇨🇳 China **high priority** | **74.32%** | **Not derivable — total not supplied** | ▲ 16.03% · rank #11,055 · **00:06 / 1.53pp / 81.59% bounce** | SimilarWeb (supplied 2026-10-11) |
| 2 | 🇺🇸 United States **high priority** | 6.30% | Not derivable | ▲ 17.38% · rank #293,759 · 05:08 / 5.82pp / 36.08% | SimilarWeb (supplied 2026-10-11) |
| 3 | 🇦🇺 Australia | 2.17% | Not derivable | ▼ **26.56%** — the only shrinking market · rank #192,046 · 01:23 / 1.95pp / 31.83% | SimilarWeb (supplied 2026-10-11) |
| 4 | 🇩🇪 Germany | 1.89% | Not derivable | ▲ 36.68% · rank #123,842 · **10:16 / 5.57pp** / 46.88% | SimilarWeb (supplied 2026-10-11) |
| 5 | 🇮🇳 India | 1.78% | Not derivable | ▲ **474.90%** · rank #164,636 · 01:24 / 4.83pp / **11.92% — lowest bounce in the table** | SimilarWeb (supplied 2026-10-11) |
| 6 | 🇭🇰 Hong Kong *(home)* | 1.68% | Not derivable | ▲ 30.91% · **rank #31,529** · 03:04 / 4.69pp / 25.32% | SimilarWeb (supplied 2026-10-11) |
| 7 | 🇨🇦 Canada | 1.56% | Not derivable | ▲ 38.25% · rank #364,761 · 00:41 / 2.82pp / 28.09% | SimilarWeb (supplied 2026-10-11) |

**APAC visible total: 79.95%. APAC excluding the China row: 5.63%.**

**🛑 No absolute visit figure exists in this dataset.** Shares only. No monthly visits, no transactions and no revenue can be derived from it. Stated rather than estimated.

**Domain variants.** The toggle being off matters less than feared: **`redteago.com` is a WordPress.com-hosted marketing site** (`host-header: WordPress.com`, `x-hacker: ... join.a8c.com` — Automattic) and **all commerce lives on the separate subdomain `esim.redteago.com`**, a Nuxt application. No country-code domain was found (no `.cn`, `.com.hk`, `.in`, `.com.au`). ⚠️ **But because the storefront is a subdomain, it may be measured separately by SimilarWeb — so the supplied table may describe the brochure site rather than the shop.** A genuine limitation, and it compounds the missing total. Other group properties found: `partner.redteago.com` (partner/affiliate portal), `static.redteago.com` (assets), `esimaccess.com` (B2B), `redteamobile.com` (corporate), plus `esim.redteatest.com` / `affiliate.redteatest.com` (non-production).

**Markets with no local entity:** all seven. See Section 2.

---

## Section 2: Legal Entities & Local Presence

**Headquarters:** Ambiguous by design, and the ambiguity is a finding. The **consumer web contracting entity is Hong Kong**: *"These Terms of Service apply to all prepaid services and related offerings provided by eSIM Access Limited (hereinafter "RedteaGO"), located at ROOM B 16/F EUBANK PLAZA 9 CHIU LUNG STREET CENTRAL HK."* Redtea Mobile was **founded 2015** (CB Insights).

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| 🇭🇰 Hong Kong | **eSIM Access Limited** (d/b/a RedteaGO) — web contracting + billing entity | **Not found** | [esim.redteago.com/agreement](https://esim.redteago.com/agreement) · [esim.redteago.com/privacy-policy](https://esim.redteago.com/privacy-policy) |
| 🇸🇬 Singapore | **REDTEA MOBILE PTE. LTD.** — Apple & Google app-store seller | **Not found** | [apps.apple.com/us/app/redteago/id1492864476](https://apps.apple.com/us/app/redteago/id1492864476) · [play.google.com/store/apps/details?id=com.redteamobile.redteago](https://play.google.com/store/apps/details?id=com.redteamobile.redteago) |
| 🇨🇳 China (Shenzhen) | **深圳杰睿联科技有限公司** — group copyright holder | **Not found** | [redteamobile.com/news/post21](https://redteamobile.com/news/post21/) (page footer) |
| — | **Redtea Mobile Group** / Redtea Mobile Global / Redtea Mobile China — operating organisations, 28 Jan 2026 | **No entity names disclosed** | [redteamobile.com/news/post21](https://redteamobile.com/news/post21/) |

⚠️ **No registration number could be obtained for any entity.** No reachable Hong Kong Companies Registry or ACRA BizFile record was found. A search surfaced an unrelated **"eSIM Now Limited" (HK BRN 81039529, incorporated 14 Aug 2026)** — **this is a different company and must NOT be used.**
⚠️ **Conflicting HQ attributions on the record, all flagged:** Terms → Hong Kong · app stores and the Trustpilot profile (29 Media Circle, Alice@MediaPolis, 138565) → Singapore · CB Insights → Shenzhen · affiliate review sites → Singapore. **Hong Kong is the one that governs the consumer payment contract, so it is the one that matters for acquiring.**

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| 🇨🇳 China | ✅ #1, 74.32% | ❌ No consumer entity. A group *operating organisation* (Redtea Mobile China) and a Shenzhen copyright holder exist; neither is shown to contract with consumers | ⚠️ **NOT ESTABLISHED — claim omitted, no current primary source found** | 🔴 **CONFIRMED CROSS-BORDER, first-party.** Terms (EN + zh-CN): *"All transactions are settled in US dollars (USD)"* |
| 🇺🇸 United States | ✅ #2, 6.30% | ❌ None found | ❌ No | 🟠 USD-settled, so no FX leg; cross-border acquiring from an HK/SG entity |
| 🇦🇺 Australia | ✅ #3, 2.17% | ❌ None found | ❌ No | 🟠 AUD not even offered as a display currency |
| 🇩🇪 Germany | ✅ #4, 1.89% | ❌ None found | ❌ No | 🟠 EUR displayed, USD charged |
| 🇮🇳 India | ✅ #5, 1.78% ▲475% | ❌ None found | ⚠️ **NOT ESTABLISHED — not sourced, claim omitted** | 🔴 INR displayed, USD charged, **no UPI** |
| 🇭🇰 Hong Kong | ✅ #6, 1.68% | ✅ **eSIM Access Limited** | ❌ No | 🟢 Home jurisdiction — but HKD displayed and USD charged, so even home customers are billed cross-currency |
| 🇨🇦 Canada | ✅ #7, 1.56% | ❌ None found | ❌ No | 🟠 CAD displayed, USD charged |

> *"Warning: Potential cross-border operation in China, the United States, Australia, Germany and India. No local entity found in any of them. Transactions are processed cross-border, with higher scheme costs, lower approval rates and FX exposure."*
>
> **And on this account it is not a "likely" — it is stated by the merchant.** Their own Terms, in both English and Chinese, say every transaction settles in USD. **Even Hong Kong customers, in the one jurisdiction where an entity exists, are shown HK$ and charged US$.**

> **MANUAL:** Verify eSIM Access Limited in the Hong Kong Companies Registry e-Services and Redtea Mobile Pte. Ltd. in ACRA BizFile. Neither was reachable in this environment, and no registration number is in this report.

---

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Global — cards, in-page | **Stripe** | `[Source Code]` + `[Terms/Privacy Policy]` — `https://js.stripe.com/v3`, `name:"stripe-js"`, `stripe.elements()`, `stripe.confirmCardPayment(...)`, `pay-with-stripe-wrap` CSS class, `payMethod: 6`; a **live publishable key** in the production config object (🔒 **value deliberately omitted — vendor named, host cited**) | [esim.redteago.com/_nuxt/pages/topay.1a026be.js](https://esim.redteago.com/_nuxt/pages/topay.1a026be.js) · [esim.redteago.com/_nuxt/app.c8dae81.js](https://esim.redteago.com/_nuxt/app.c8dae81.js) · [esim.redteago.com/agreement](https://esim.redteago.com/agreement) |
| Global — local/alternative methods, redirect | **Nuvei** | `[Source Code]` — `queryNuveiPaymentAPI()` → `POST /v1/payment/nuvei/options`; returns `areaName` / `areaCode` / `paymentMethods[].paymentName` / `.paymentCode`; **seven locale `/nuvei-jump` routes** registered in the production router (`en`, `de`, `es`, `ja`, `tr`, `zh-CN`, `zh-HK`); `payMethod === 14` attaches `areaCode` + `paymentCode` | [esim.redteago.com/_nuxt/app.c8dae81.js](https://esim.redteago.com/_nuxt/app.c8dae81.js) · [esim.redteago.com/_nuxt/pages/topup.1b0f774.js](https://esim.redteago.com/_nuxt/pages/topup.1b0f774.js) · [esim.redteago.com/_nuxt/4.42d059a.js](https://esim.redteago.com/_nuxt/4.42d059a.js) |
| Not determined | **Adyen** | `[Source Code]` — `POST /v1/get/payparam/adyen-pay`, corroborated by `successUrl: "...?authResult=AUTHORISED&orderId=..."` (Adyen HPP result vocabulary). ⚠️ **Single endpoint, one evidence type. Live status NOT established** | [esim.redteago.com/_nuxt/app.c8dae81.js](https://esim.redteago.com/_nuxt/app.c8dae81.js) |
| Global — wallet, redirect | **PayPal** | `[Source Code]` + `[Terms/Privacy Policy]` — `paypalPay: function(e)` on the top-up page; named in Terms §2 and §4.1 in both languages | [esim.redteago.com/_nuxt/pages/topup.1b0f774.js](https://esim.redteago.com/_nuxt/pages/topup.1b0f774.js) · [esim.redteago.com/agreement](https://esim.redteago.com/agreement) |
| Greater China | **Alipay** · **WeChat Pay** — named as *processing platforms* | `[Terms/Privacy Policy]` — §4.1 EN: *"processed and secured by platforms such as Stripe, PayPal, WeChat Pay, and Alipay"*; zh-CN: *"支付交易由 Stripe、PayPal、微信支付 和 支付宝 等平台处理并提供安全保障"*. ⚠️ **No SDK, endpoint or deep link found. The acquiring ROUTE is NOT established** — Stripe and Nuvei each offer both as cross-border methods, and USD settlement is consistent with either | [esim.redteago.com/agreement](https://esim.redteago.com/agreement) · [esim.redteago.com/zh-CN/agreement](https://esim.redteago.com/zh-CN/agreement) |
| — | Airwallex · Braintree · Checkout.com · Worldpay · Cybersource · Razorpay · PayU · Cashfree · CCAvenue · Paytm · 2C2P · Xendit · Midtrans · Doku · iPay88 · Omise · GMO · SB Payment · Veritrans · KOMOJU · Toss · NICEPAY · eWAY · Pin Payments · Windcave · Tyro · Payssion · PingPong · LianLian · Oceanpayment · AsiaBill | ❌ **NOT FOUND** — searched the storefront, both locale renderings, five page HTMLs, 13 JS bundles, the Terms and the Privacy Policy | — |

**The in-house payment API, in full** (all first-party, `app.c8dae81.js`):
`/v1.1/query/payments` (server returns the available `payMethods[]`) · `/v1.1/setup/payment` · `/v1.1/execute/payment` · `/v1.1/payOrder/confirm` · `/v1.1/payOrder/payment-status` · `/v1.1/query/payment-status` · `/v1.1/data/create/topup-order` · `/v1.1/execute/topup/payment` · `/v1/query/topup/payment-status` · `/v1/refund/order` · `/v1/query/credit-plan` · `/v3/query/orders`. Backend service codename **`nobel`** (error prefix `RT_NOBEL_ERROR_*`, SSR base `http://nobel:8080`). Requests carry `meta.currentTime`, `meta.requestId` and a body-derived `signature` header.

**Resolved `payMethod` enum** (from `samePagePayment: [5, 6]` and the branch logic): **`6` = card via Stripe Elements (in-page)** · **`5` = RedteaGO Credit wallet balance (in-page)** · **`14` = Nuvei local method (redirect via `/nuvei-jump`)** · PayPal = redirect, id not resolvable client-side. **The remainder of the enum is server-side and was not obtained.**

### ⚠️ False positives ruled out — every one of these would have shipped as a finding
- **`omise` — 135 raw hits across the bundles, ALL spurious.** `Promise.all`, `new Promise`, `Promise.resolve`, `Promise.reject`. **Omise is NOT present.** (Flexiroam's trap, fired again exactly as predicted.)
- **`upi` — 8 raw hits, ALL spurious.** Every one is `selectedTopupIdx` / `topupIdx`. **No UPI. Not even a trace.**
- **`primer` — 0 hits on RedteaGO.** The Supprimer/primera trap did not fire here. ⚠️ **But it fired on a competitor and I checked it properly — see Section 11C.**
- **`payme` — 3 raw hits, ALL spurious.** `samePagePayment`, `Payment`, `paymentFailed`. **PayMe (HK) is NOT supported.**
- **`unionpay` — 2 hits, and they are an IMAGE ASSET ONLY**: `img/unionPay.7d69333.png` with `alt: "unionPay.png"` on the pay page, beside `visa`, `masterCard`, `express` and `jcb`. **This is UnionPay accepted as a card brand, NOT UnionPay as a separate rail and NOT evidence of domestic Chinese acquiring.** Stated precisely because the difference is the whole account.
- ⭐ **THE BIG ONE — and it resolves the OPPOSITE way to Flexiroam, so read the reasoning.** The 13 currency codes here are **NOT** a generic country-metadata table. The Flexiroam trap was `{name:"Malaysia",phone:[60],capital:"Kuala Lumpur",currency:["MYR"],languages:["ms"]}` — a country encyclopaedia. **This is a constant literally named `supportCurrency`, sitting in the storefront's payment/pricing state store beside `baseCurrency` and `currentCurrency`, where every entry carries a symbol AND an FX multiplier** (`CNY:{name:"CNY",currency:"¥",value:7.13}`). **That is a display-conversion table in a payment context and it is legitimate evidence.** ⚠️ **It is evidence of DISPLAY currency support only — settlement is USD per the Terms. Do not upgrade it to multi-currency settlement.**
- **Alipay / WeChat Pay in editorial copy — DO NOT CITE AS CHECKOUT SUPPORT.** The `travel-in-china` guide page says *"Most restaurants, shops, taxis, and tourist attractions accept Alipay or WeChat Pay"* — that is **travel advice about China for tourists**, not RedteaGO's checkout. The genuine evidence is Terms §4.1, which is a payment context. **Two different things on the same site; only one counts.**
- **`crypto` — 5 hits, FAQ TEXT ONLY, and it contradicts the Terms.** FAQ #2013 lists *"Apple Pay, PayPal, Bank Card, Alipay, **Crypto** and RedteaGo Credit"* (zh-CN: *"加密货币"*). **But crypto appears nowhere in the Terms' payment list, and no crypto PSP token exists anywhere** — `coinbase`, `binance`, `coingate`, `nowpayments`, `cryptomus`, `bitpay`, `triple-a`, `opennode`, `usdt` all **0**. **Crypto is advertised but the provider is NOT established. Flag as a discrepancy, do not assert it.**
- **`stripe` as a Tailwind class** — checked; no `bg-stripe-gradient-*` noise here. All 22 hits in the checkout chunks are genuine Stripe.js.

### 3B. Payment Orchestrator

**Classification: IN-HOUSE ORCHESTRATION LAYER.** Evidence type `[Source Code]`, sources as listed in 3A.

The merchant built the abstraction: a **server-returned payment-method list**, a **numeric `payMethod` enum the client routes on**, a **`samePagePayment` constant classifying in-page versus redirect methods**, **per-vendor redirect routes** registered across all seven locales, and **one unified setup → execute → confirm → status API spanning four acquiring paths**. That is a payment abstraction layer, not four bolt-on integrations.

**No third-party orchestrator.** Juspay, Spreedly, Primer, Gr4vy, Payrails, Corefy, CellPoint, APEXX and Yuno all return **0 occurrences** across the storefront, both locale renderings and all 13 bundles. The `apac-tal.csv` `Payment Orchestrator` column is empty for RedteaGO and nothing contradicts that.

> *"Confirmed in-house. The opening is reach and opportunity cost, not the case for orchestration itself — they have already made it, and made it twice over, since they also bought APM breadth from Nuvei rather than integrating rails directly."*

⚠️ **One honest limit on this classification.** Whether the layer performs actual **routing** — retry, failover, cascading, decline-code-driven re-attempts — is decided **server-side and is invisible from the client.** No per-attempt telemetry, `decline_code`, `retry` or `attemptId` instrumentation appears in the bundles (unlike Flexiroam, where it did). **It may be a method-selection shim rather than a router.** If it is a shim, the in-house objection is far weaker than it looks, and that is worth finding out early.

> **MANUAL:** Walk checkout with DevTools from a CN, IN and AU IP. Watch the `/v1.1/query/payments` response — it is the authoritative method list and it is almost certainly geo-conditional. Then watch which host the `/v1.1/execute/payment` call hands off to per method.

---

## Section 4: Alternative & Local Payment Methods

**Authoritative first-party list — Terms of Service §2 and §4.1, last updated 6 May 2026, identical in English and Chinese:**
> *"Payment services are supported by **Apple Pay, Stripe, PayPal, WeChat Pay,** and **Alipay**."*
> *"RedteaGO supports payment methods including **credit cards, Alipay, WeChat Pay, and PayPal.** All transactions are settled in US dollars (USD)."*

**Second first-party list — FAQ #2013** (differs, and the difference is itself a finding):
> *"We support multiple payment methods, including **Apple Pay, PayPal, Bank Card, Alipay, Crypto** and **RedteaGo Credit**."*

> 🚩 **The two lists do not agree. The Terms name WeChat Pay and omit crypto; the FAQ names crypto and omits WeChat Pay.** Neither is dated later than the other in a way I can resolve. **Both are quoted here; neither is presented as settled.**

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| Global | **Credit/debit cards** (Visa, Mastercard, Amex, JCB, UnionPay brand marks) | Cards | ✅ **Active in checkout** — Stripe Elements, `payMethod: 6` | [topay.1a026be.js](https://esim.redteago.com/_nuxt/pages/topay.1a026be.js) · [esim.redteago.com/topay](https://esim.redteago.com/topay) |
| Global | **Apple Pay** | Digital wallet | ✅ **Active in checkout** — full i18n string set: `applePay`, `applePayNotSupported`, `applePayError`, `applePayCardAdded`, `applePayNoCard`, `applePaySetupFailed` | [esim.redteago.com/](https://esim.redteago.com/) · [agreement](https://esim.redteago.com/agreement) |
| Global | **PayPal** | Digital wallet | ✅ **Active in checkout** — `paypalPay()` | [topup.1b0f774.js](https://esim.redteago.com/_nuxt/pages/topup.1b0f774.js) |
| Global | **RedteaGO Credit** (stored value) | Digital wallet / stored value | ✅ **Active in checkout** — `payMethod: 5`, `/credit`, `/balance`, `/topup`, `/v1/query/credit-plan`. Terms §4.4: *"virtual currency held in the registered user's account wallet"*, **non-refundable and non-exchangeable** | [esim.redteago.com/credit](https://esim.redteago.com/credit) · [agreement](https://esim.redteago.com/agreement) |
| 🇨🇳 China / Global | **Alipay** | Digital wallet | ✅ **Mentioned in Terms AND FAQ** — ⚠️ acquiring route not established, settles USD | [agreement](https://esim.redteago.com/agreement) · [zh-CN/agreement](https://esim.redteago.com/zh-CN/agreement) |
| 🇨🇳 China / Global | **WeChat Pay** | Digital wallet | ⚠️ **Mentioned in Terms, ABSENT from the FAQ list.** Discrepancy flagged, not resolved | [agreement](https://esim.redteago.com/agreement) · [zh-CN/agreement](https://esim.redteago.com/zh-CN/agreement) |
| 🇨🇳 China | **UnionPay** | Cards | ⚠️ **Brand mark only** (`img/unionPay.png` on the pay page beside Visa/MC/Amex/JCB). Accepted as a **card scheme**, not as a separate rail, and **not** evidence of domestic Chinese acquiring | [esim.redteago.com/topay](https://esim.redteago.com/topay) |
| Global | **Cryptocurrency** | Crypto | ⚠️ **Mentioned in FAQ only.** No provider token anywhere (9 vendors searched, all 0); absent from the Terms. **Provider NOT established** | [esim.redteago.com/](https://esim.redteago.com/) |
| Many | **Nuvei local payment methods** (country → method picker) | Mixed — bank transfer / wallet / cash, per country | ✅ **Active in checkout, but the method list could NOT be enumerated.** `payMethod === 14`, `/nuvei-jump` redirect. **The country→method matrix lives behind the signed `/v1/payment/nuvei/options` endpoint, and reconstructing the request signature was blocked in this environment.** 🛑 **This is the single largest gap in Section 4 — some of the "missing" rails below may in fact be present through Nuvei** | [app.c8dae81.js](https://esim.redteago.com/_nuxt/app.c8dae81.js) · [4.42d059a.js](https://esim.redteago.com/_nuxt/4.42d059a.js) |
| 🇮🇳 India (1.78%, ▲475%) | **UPI** · RuPay · netbanking · Paytm/PhonePe · **EMI / no-cost EMI** | A2A / cards / wallet / instalments | ❌ **NOT FOUND** — `upi` 8 hits, all `TopupIdx`; `rupay`, `netbanking`, `emi`, `paytm`, `phonepe` all 0. INR is a **display** currency only. **No Hindi UI locale exists** | grep over all fetched assets |
| 🇦🇺 Australia (2.17%) | **PayTo** · **BPAY** · Afterpay · Zip | Mandate / bill pay / BNPL | ❌ **NOT FOUND** — 0 occurrences each. AUD is **not even offered** as a display currency | grep over all fetched assets |
| 🇭🇰 Hong Kong (1.68%, home) | **FPS** · **Octopus** · **PayMe** · AlipayHK | A2A / stored value / wallet | ❌ **NOT FOUND** — `fps` 0, `octopus` 0, `payme` 3 hits all spurious. HKD is a **display** currency only | grep over all fetched assets |
| 🇯🇵 Japan *(zh/ja locale exists; <1% traffic)* | konbini · PayPay · LINE Pay · Paidy · instalments | Cash / wallet / BNPL | ❌ **NOT FOUND** — `konbini` 0, `paypay` 0, `linepay` 0, `paidy` 0. **A full Japanese UI locale and JPY display currency exist, with no Japanese rail** | grep over all fetched assets |
| 🇰🇷 Korea *(KRW display currency)* | KakaoPay · Naver Pay · Toss · domestic instalments | Wallet / instalments | ❌ **NOT FOUND** — all 0. **KRW is offered as a display currency with no Korean rail and no Korean UI locale** | grep over all fetched assets |
| 🇹🇭 Thailand *(THB display currency)* | PromptPay · TrueMoney | A2A / wallet | ❌ **NOT FOUND** — all 0 | grep over all fetched assets |
| 🇸🇬 Singapore *(SGD display currency)* | PayNow · GrabPay | A2A / wallet | ❌ **NOT FOUND** — all 0 | grep over all fetched assets |
| Global | **Google Pay** | Digital wallet | ❌ **NOT FOUND** — `googlepay` / `google pay` 0 occurrences, and absent from both first-party lists. **Notable on an Android-distributed app** | grep over all fetched assets |
| Global | Instalments / BNPL (Klarna, Afterpay, Zip, Atome) · carrier billing · konbini/OTC cash | BNPL / carrier / cash | ❌ **NOT FOUND** — and genuinely unexpected on a $0.10–$8.80 ticket. **No instalment hook on this account; do not reach for one** | grep over all fetched assets |

> *"Warning: In India — the fastest-growing market in the table at ▲474.90%, with the lowest bounce rate (11.92%) and 4.83 pages per visit — UPI is absent from RedteaGO's checkout, INR appears only as a display currency, and there is no Hindi interface."* ⚠️ **A source for UPI's domestic prominence in India was NOT obtained** (the NPCI statistics page returned no figures). **The absence is sourced first-party; the "widely used" half of the claim is not, so it is not scored and must not be asserted with a number in outreach.**

> 🎯 **The pattern across this whole table, and the thing to actually sell on:** they ship **seven UI languages** and **thirteen display currencies** — and **exactly four payment rails plus a stored-value wallet, every one settling in USD.** JPY, KRW, THB, SGD, INR, HKD and CNY all have a price tag and **not one has a local rail.** **They localised the shop window and left the till in dollars.**

> **MANUAL:** Use a VPN to walk checkout from China, India and Australia and capture the `/v1.1/query/payments` and `/v1/payment/nuvei/options` responses. **That single step closes the biggest gap in this report** and would confirm or kill several of the ❌ rows above.

---

## Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| **Slow / refused / partial refunds** | Trustpilot | **Moderate** — multiple dated instances in a 74-review base | Nov 2025 – Aug 2026 | [trustpilot.com/review/redteago.com](https://www.trustpilot.com/review/redteago.com) |
| Refund refused despite evidence supplied | Trustpilot (1★, 3 Aug 2026) | Isolated | Aug 2026 | same |
| Partial refund only — *"they didnt even refund me the full amount"* | Trustpilot (1★, 2 May 2026) | Isolated | May 2026 | same |
| Service disconnected without notice, refund issued | Trustpilot (4★, 12 Mar 2026) | Isolated | Mar 2026 | same |
| *"Scammers stole my money and deleted my contact information"* — company replied it *"will actively processing a refund"*, no timeline | Trustpilot (1★, 25 Jan 2026) | Isolated | Jan 2026 | same |
| **Score suppressed by the platform** — Trustpilot states the rating is *"unavailable due to a breach of our guidelines"* | Trustpilot | **Standing condition** | As at 2026-10-11 | same |
| eSIM fails to connect / wrong-region eSIM (**not a payment issue — listed so it is not miscounted as one**) | Trustpilot | High | 2025–2026 | same |

**Trustpilot distribution as at 2026-10-11:** 74 reviews — 5★ 50% · 4★ 8% · 3★ 4% · 2★ 3% · **1★ 35%.** Score withheld by the platform.
**App-store ratings:** Apple US **4.5 / 893 ratings**; Google Play **3.7 / 1.24K reviews, 100K+ downloads**. **The 0.8-star gap between iOS and Android is itself worth noting** given that Android is the China-facing channel and the China-facing Android build is 14 versions stale.

> **The honest pattern, and I am not dressing it up:** *"The complaint record on RedteaGO is about refund handling and eSIM connectivity, not payment processing. There are **ZERO** reports of card declines, checkout errors, failed authorisations or currency-conversion disputes anywhere I looked."* **Do not build outreach on a declines narrative — there is no evidence for one.** The orchestration-relevant read is narrower and more defensible: **refund operations across four acquiring paths, each with its own refund API and timeline, is exactly the kind of fragmentation that produces "we are processing it" with no date attached.** That is a credible hypothesis, and it should be put as one.

⚠️ Reddit, X and market-local forums returned nothing usable for RedteaGO specifically.

---

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | **28 Jan 2026** | **Redtea Mobile Group formed**, operating as **Redtea Mobile Global** + **Redtea Mobile China** on a stated *"local for local"* model. Group CEO **Hui Jin**, Group CFO **Rico Zhong**, Group COO **Qinghua Peng**, Group CMO **Xiaodong Guo**; Global CEO **Rob Varty**, Global CTO **Edwin Haver**. Intends to extend into *"additional strategic markets over time"* — **none named** | Market Expansion / Leadership Change | [redteamobile.com/news/post21](https://redteamobile.com/news/post21/) |
| 2 | **Jul 2026** | Group CEO **Dr Hui Jin** presented on eSIM revenue for operators — GSMA-hosted material | Tech / Conference Signal | [gsma.com ... Dr-Hui-Jin-Redtea-Mobile.pdf](https://www.gsma.com/solutions-and-impact/technologies/esim/wp-content/uploads/2026/07/Dr-Hui-Jin-Redtea-Mobile.pdf) |
| 3 | **2025** | **AfricaCom 2025** — 50+ operator sessions. ⚠️ B2B/carrier, no consumer or payment component | Tech / Conference Signal | [redteamobile.com/news/post20](https://redteamobile.com/news/post20/) |
| 4 | **6 May 2026** | **Terms of Service updated**, naming the current payment-method and processor list. Cookie policy effective **29 Dec 2025** | Payment Platform (documentation) | [esim.redteago.com/agreement](https://esim.redteago.com/agreement) |
| 5 | **7 Jul 2022** | **Series B** — latest round. $10M total raised across 4 rounds; investors include China Merchants Securities Capital, Qualcomm Ventures, Yueke Xintai, Shengming Enterprise Management Consulting, WiWide | Funding | [cbinsights.com/company/redtea-mobile/financials](https://www.cbinsights.com/company/redtea-mobile/financials) |

**🛑 No public payment-related RFP found.**
**🛑 No payment-related job postings found** — and no job postings of any kind for Redtea Mobile, RedteaGO or eSIM Access were located. Checked JobStreet SG and general search; nothing. **No hiring signal.**
**🛑 No M&A found. No payment licence application found in any market.**
**🛑 No funding in the last 12 months.** The latest round is over four years old. **Do not pitch a funding trigger.**

---

## Section 7: Payment-Specific News

**No payment-specific trade press was found for RedteaGO, eSIM Access Limited or Redtea Mobile.** Searches across thepaypers.com, finextra.com, pymnts.com, techinasia.com, e27.co and entrackr.com returned no items linking the company to any payment provider, partnership, migration or removal.

What exists instead, and it is first-party rather than press:

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 6 May 2026 | Terms of Service §4.1 names the processor set — *"Stripe, PayPal, WeChat Pay, and Alipay"* — and states **USD-only settlement** | **The single most load-bearing payment document on this account** | [esim.redteago.com/agreement](https://esim.redteago.com/agreement) |
| 2 | As at 2026-10-11 | Production code adds **Nuvei** (`/v1/payment/nuvei/options`, `/nuvei-jump`) and **Adyen** (`/v1/get/payparam/adyen-pay`) — **neither appears in the Terms** | ⭐ **The Terms are behind the code.** Two acquiring paths are live in production and undocumented publicly — the same tell Flexiroam showed, and the same opener | [app.c8dae81.js](https://esim.redteago.com/_nuxt/app.c8dae81.js) |
| 3 | As at 2026-10-11 | FAQ advertises **cryptocurrency**; the Terms do not, and no crypto provider token exists anywhere | Unresolved internal contradiction — ask, do not assert | [esim.redteago.com/](https://esim.redteago.com/) |

**🛑 No provider REMOVAL found.** No evidence that any processor was discontinued.

---

## Section 8: Checkout Experience Audit

Conducted by fetching the live storefront and its production bundles. **A full authenticated purchase was not completed** — no card was entered and no order placed.

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | **Custom-built, embedded** — Nuxt SPA on `esim.redteago.com`, dedicated `/topay` page | Good | Not hosted; the merchant owns the page |
| Guest checkout | **❌ Account required.** Terms §2.2: registration requires a nickname and email; `/login`, `/signup`, `/forgotPwd`, `/resetpwd`, `/changepwd` routes; FAQ: *"register with your email address on the RedteaGO app or website and purchase"* | **Poor** | ⭐ **A forced account on a $0.54–$8.80 impulse purchase bought at an airport is a conversion tax.** One of the clearest findings in this audit |
| Steps to complete payment | Select destination → select plan → `/topay` → method → pay. In-page for cards and Credit; **a full redirect for PayPal, Nuvei and Adyen** | Fair | Two-tier experience by method |
| Card input experience | **Tokenized Stripe Elements iframe** — `stripe.elements()`, `confirmCardPayment()`. Card data never touches their origin | **Good** | Implies deliberately reduced PCI scope |
| Payment methods visible | Cards (Visa/MC/Amex/JCB/UnionPay marks), Apple Pay, PayPal, RedteaGO Credit, Nuvei local methods | Fair | **Four rails and a wallet, against 13 display currencies** |
| Location-based method display | ⚠️ **Partially.** Locale is geo/language-adaptive (302 to `/zh-CN` on `Accept-Language`), and the Nuvei method list is country-keyed — **but the authoritative list is server-side and could not be retrieved, so true geo-adaptation of METHODS is NOT confirmed** | Unknown | The one dimension that most needs a VPN walk |
| Instalment / EMI options | **❌ None found.** No EMI in India, no Japanese/Taiwanese instalments, no BNPL | N/A | **Appropriate at this ticket size — do not pitch instalments** |
| 3DS implementation | ⚠️ **Not detected client-side.** `3ds`, `three_d`, `threeDS`, `challenge` all 0 — **expected**, since Stripe's `confirmCardPayment` handles 3DS internally and the other three paths redirect | Unknown | Not a finding either way |
| PCI indicator | **PSP iframe** (Stripe Elements) + redirect flows. No self-hosted card fields found | **Good** | See Section 9 |
| Mobile responsiveness | Tailwind utility classes throughout; **Vant** mobile component library (`van-index-bar`) in the Nuvei picker; dedicated mobile app-download assets | Good | Genuinely mobile-built, as an app-first merchant should be |
| Multi-currency / local pricing | ⭐ **13 display currencies with hard-coded client-side FX off a USD base — and USD-only settlement.** `baseCurrency: "USD"`, `currentCurrency: "USD"`. Prices stored in a **1/10,000 USD minor unit** (`(e/1e4).toFixed(2)`) | **Poor — and this is the hook** | Local price tag, foreign-currency charge, stale rates until redeploy |
| Saved payment methods | **❌ None.** `saveCard`, `savedCard`, `cardOnFile`, `setup_intent`, `seti_`, `tokeniz*` all **0** | **Poor** | ⭐ **On a repeat-purchase travel product with a stored-value wallet, there is no card vaulting at all.** Every trip is a fresh card entry. Strong, specific, verifiable |
| Error message clarity | Generic: `applePayError: "Apple Pay payment failed"`, `"Payment processing failed, please try again"`, `key_error_payment_failed`-style strings. **No decline-code mapping found** | **Poor** | ⚠️ **Contrast directly with Airalo, which maps 45 distinct Stripe decline codes and 23 Primer errors to specific user-facing messages.** RedteaGO tells the customer "try again." **That is a measurable competitive gap in recovered revenue** |

**Security headers:** 🛑 **No CSP on either host.** `redteago.com` and `esim.redteago.com` return no `content-security-policy`, `frame-ancestors`, `connect-src`, `script-src` or `form-action`. The `frame-ancestors` storefront-enumeration technique was checked and yields nothing here. `redteago.com` does carry `strict-transport-security: max-age=31536000`.

---

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **Not found.** No PCI statement, AOC, trust page or compliance claim on `redteago.com`, `esim.redteago.com`, in the Terms, or in the Privacy Policy. The token `pci` returns **0** across every fetched asset | — |
| Card data handling | **Likely SAQ A / SAQ A-EP equivalent.** Card entry is a tokenized **Stripe Elements** iframe (`stripe.elements()`, `confirmCardPayment()`); PayPal, Nuvei and Adyen are all **redirect** flows; **no self-hosted card fields and no `saveCard`/vaulting tokens exist anywhere.** No `form-action` CSP directive to check, but no card-posting endpoint on their own origin was found either | [topay.1a026be.js](https://esim.redteago.com/_nuxt/pages/topay.1a026be.js) |
| Recommended Yuno integration | **SDK** (hosted fields / drop-in), to preserve the reduced scope they already have. A back-to-back API integration would expand their PCI footprint and is the wrong opening ask | — |

*"No direct PCI compliance documentation found publicly for RedteaGO."*

> `[INFERENCE, not confirmed]`: Based on confirmed use of Stripe's tokenized Elements checkout plus redirect flows for all three other acquiring paths, the company's PCI scope is likely reduced, with Stripe and the redirect providers handling card data.

⚠️ **The Privacy Policy is thin on payments.** It names **no payment processor at all** — the processor list lives only in the Terms of Service. Worth knowing before quoting a privacy policy at them.
🔒 **Credential note.** Live and test **publishable** keys for a named vendor were found in the production client bundle. **Vendor named, host cited, values deliberately not transcribed into this report.** Publishable keys are designed to be public, so this is not a disclosure — but per repo policy no key value is written here.

---

## Section 10: Strategic Insights & Outreach Angles

> **Insight #1: Thirteen currencies on the shelf, one currency at the till**
> **Evidence:** **Section 4 / Section 8** — `supportCurrency` carries 13 display currencies with hard-coded FX multipliers off `baseCurrency: "USD"` ([store state, esim.redteago.com](https://esim.redteago.com/)) + **Section 2 / Section 3** — their own Terms of Service in both English and Chinese: *"All transactions are settled in US dollars (USD)"* ([agreement](https://esim.redteago.com/agreement)) + **Section 1** — only 1.68% of traffic is in the one jurisdiction where an entity exists.
> **Pain Point:** A Chinese, Korean, Indian, Thai or Japanese customer is shown a price in their own currency and then charged a cross-border USD authorisation. They absorb the issuer FX spread and the foreign-transaction fee; RedteaGO absorbs the cross-border decline rate and the scheme cross-border fee. On a $0.54–$8.80 impulse ticket, a 3–5 percentage-point approval difference is a larger number than the margin. And because the FX rates are **client-side constants**, the displayed price silently drifts from the charged amount until someone redeploys the bundle.
> **Yuno Value Proposition:** Local acquiring and local-currency settlement per corridor behind the abstraction they already built, so the price the customer sees is the price their issuer sees — routed to a domestic acquirer where one exists, cross-border only where it must be.
> **Best Success Case:** A low-ticket, high-frequency travel or connectivity merchant that moved from single-currency cross-border collection to per-corridor local acquiring. ⚠️ **Prateek to select the named reference from the internal list — I am not attaching a customer name or a metric I cannot source.**
> **Outreach Angle:** "You price in thirteen currencies and settle in one. Your own terms say USD; your own storefront quotes ¥, ₩ and ₹. Worth knowing what that costs you on approval rates in China and India specifically."
> **Suggested Subject Line:** "¥ on the page, $ on the statement"

> **Insight #2: You built the layer, then bought the rails — and bolted them on sideways**
> **Evidence:** **Section 3B** — a genuine in-house abstraction: server-returned `payMethods[]`, a numeric `payMethod` enum, `samePagePayment: [5,6]`, one unified setup→execute→confirm→status API across four acquiring paths + **Section 3A / Section 4** — but local-method breadth is **Nuvei's**, reached through a `payMethod === 14` branch and a `/nuvei-jump` **redirect**, while cards run **in-page** through Stripe Elements.
> **Pain Point:** Two-tier checkout by rail. A card customer stays on the page; anyone using a local method leaves the site, and redirect flows convert worse than in-page ones — in the markets where local methods are the *default* rail rather than the alternative. They did the hard engineering (the abstraction) and then accepted the easy integration (a redirect) on exactly the paths that matter most outside the US.
> **Yuno Value Proposition:** Keep their abstraction and their enum. Replace the redirect branch with in-page local methods through one integration, so the Indonesian, Thai or Indian customer never leaves `/topay` — and so adding a rail is a config change rather than a new jump route in seven locales.
> **Best Success Case:** A merchant that already had an internal payment abstraction and used orchestration to widen rail coverage without rebuilding it. ⚠️ Prateek to select the named reference.
> **Outreach Angle:** "You wrote your own payment layer and then sent every local method out to a redirect page while cards stay in-page. The engineering was the hard part and you've already done it."
> **Suggested Subject Line:** "payMethod 14 is the one costing you"

> **Insight #3: Airalo maps 45 decline codes. You say 'please try again.'**
> **Evidence:** **Section 11C** — Airalo's own i18n table carries **23 `validations.primer.*` keys and 45 `validations.stripe.*` keys**, mapping specific declines (`insufficient-funds`, `call-issuer`, `card-velocity-exceeded`, `authentication-required`, `three-ds-auth-failed`) to specific user-facing messages ([airalo.com app shell](https://www.airalo.com/terms)) + **Section 8** — RedteaGO's entire error vocabulary is generic: *"Payment processing failed, please try again"*, with **no decline-code mapping found anywhere** + **Section 3B** — and no per-attempt retry or decline telemetry in their bundles either.
> **Pain Point:** Every soft decline on RedteaGO's checkout is an abandoned $3 sale with no recovery path and no diagnosis. The category leader has built a recovery funnel; RedteaGO has an alert box. Worse, without decline telemetry they cannot see the size of the problem — which is why it has stayed unsolved.
> **Yuno Value Proposition:** Normalised decline codes across all four acquiring paths, retry and failover logic driven by the decline reason, and per-attempt visibility — the layer they would otherwise have to build a fifth time.
> **Best Success Case:** A low-ticket merchant where recovered soft declines, not MDR, carried the business case. ⚠️ Prateek to select the named reference.
> **Outreach Angle:** "Your biggest competitor translates forty-five distinct card declines into forty-five distinct messages. Your checkout says 'please try again.' That difference is recovered revenue on a three-dollar ticket."
> **Suggested Subject Line:** "45 decline codes vs 'please try again'"

> **Insight #4: No card vaulting on a repeat-purchase product that also runs a wallet**
> **Evidence:** **Section 8** — `saveCard`, `savedCard`, `cardOnFile`, `setup_intent`, `seti_` and `tokeniz*` all return **0** across the storefront and all 13 bundles + **Section 4** — yet they operate **RedteaGO Credit**, a stored-value wallet with its own top-up and recharge flows (`/topup`, `/v1.1/data/create/topup-order`) + **Section 8** — and checkout **forces account registration** on every purchase.
> **Pain Point:** They make the customer create an account, and then make them re-enter card details every single time. The wallet exists precisely because repeat purchase is the model — a traveller buys a plan per trip and tops up mid-trip — but the one thing that makes repeat purchase frictionless is missing. The account requirement captures the cost of registration without capturing the benefit.
> **Yuno Value Proposition:** Network tokenisation and vaulting across the acquiring paths they already run, so a returning traveller and a mid-trip top-up are one tap — with the token portable across providers rather than locked to one.
> **Best Success Case:** A repeat-purchase, low-ticket merchant that added vaulting and lifted returning-customer conversion. ⚠️ Prateek to select the named reference.
> **Outreach Angle:** "You require an account, you run a prepaid wallet, and you don't store a card. The second purchase is as much work as the first."
> **Suggested Subject Line:** "The second purchase shouldn't be as hard as the first"

---

## Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. "Your storefront quotes thirteen currencies and your terms of service settle every one of them in dollars — worth knowing what that does to approval rates in your two biggest growth markets."
2. "Your own code sends every local payment method out to a redirect page while cards stay in-page, which is backwards in the markets where local methods are the default rail."
3. "Airalo's checkout maps forty-five distinct card declines to forty-five distinct messages; yours says 'please try again' — on a three-dollar ticket that gap is pure recovered revenue."

**Cold call openers (conversational, one sentence each):**
1. "I was looking at your checkout — you've clearly built your own payment layer, which is why I'm not calling to sell you the idea of one; I'm calling about the thirteen display currencies sitting on top of USD-only settlement."
2. "Quick one: India is your fastest-growing market by a mile and there's no UPI on the checkout and no Hindi on the site — is that a roadmap thing or a provider thing?"
3. "You run a prepaid credit wallet and require an account to buy, but you don't store a card — was that a deliberate PCI call or just not got to yet?"

---

## Section 11: Similar Companies & Prospecting Pipeline

### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| **Airalo** | airalo.com | 🇸🇬 Singapore | Category leader | Global — all of RedteaGO's | ⭐ **PRIMER (orchestrator) + STRIPE + PayPal** — confirmed, first-party code | [airalo.com/terms app shell](https://www.airalo.com/terms) |
| **Flexiroam** | flexiroam.com | 🇲🇾 Malaysia (ops) / 🇦🇺 Australia (domicile, ASX:FRX) | A$10.17m FY26 revenue | Global, 190+ countries | **STRIPE + AIRWALLEX**, routed by an **in-house** vendor-selection layer. Terms clause 5.5: card data *"received and processed by Stripe, not by us"* → reduced PCI scope | `2-ready-to-outreach/flexiroam.md` (this repo, 16/29) |
| **Holafly** | esim.holafly.com | 🇪🇸 Spain | Large | Global, overlaps US/EU/APAC | **Not established** — homepage client-rendered, terms page carries no processor token | fetched 2026-10-11, no hits |
| **Nomad** | nomadesim.com | 🇸🇬 Singapore | Mid | Global, strong APAC | **Not established** | fetched 2026-10-11, no hits |
| **Saily** (Nord Security) | saily.com | 🇱🇹 Lithuania | Mid, well-capitalised | Global | **Not established** | fetched 2026-10-11, no hits |
| **Ubigi** (Transatel / NTT) | ubigi.com | 🇫🇷 France (NTT-owned) | Large, carrier-backed | Global, strong Japan | **Not established** | fetched 2026-10-11, no hits |
| **eSIM Access** ⚠️ | esimaccess.com | 🇭🇰 Hong Kong | — | — | 🛑 **NOT A COMPETITOR — it is RedteaGO's OWN contracting entity and the group's B2B arm.** Listed here only so it is never mistaken for one | [esimaccess.com/docs/why-choose-esim-access](https://esimaccess.com/docs/why-choose-esim-access/) |

⚠️ **Holafly, Nomad, Saily and Ubigi are "not established", not "none."** Their homepages are client-rendered and their terms pages carry no processor reference; their stacks would need a checkout walk. **Do not infer a greenfield competitor set from four blanks.**

### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Airalo | airalo.com | Travel eSIM | Global | Same ticket size, same impulse-at-travel moment, same stored-value wallet pattern (**Airmoney** ≈ RedteaGO Credit) | [airalo.com/terms app shell](https://www.airalo.com/terms) |
| Flexiroam | flexiroam.com | Travel eSIM / MVNO | Global, MY/AU/HK entities | **The closest structural twin in this repo** — in-house multi-PSP layer, USD-only pricing, many UI locales, no local rails | `2-ready-to-outreach/flexiroam.md` |
| Holafly | esim.holafly.com | Travel eSIM | Global | Same category, EU-weighted; unlimited-plan positioning | fetched 2026-10-11 |
| Nomad | nomadesim.com | Travel eSIM | Global, SG-HQ | APAC-HQ'd peer, in territory | fetched 2026-10-11 |
| Saily | saily.com | Travel eSIM | Global | Consumer-security parent, strong card-only funnel | fetched 2026-10-11 |
| Ubigi | ubigi.com | Travel eSIM / connected car | Global, JP strong | Carrier-owned; the Japan rails question (konbini, PayPay) applies to both | fetched 2026-10-11 |
| **China Mobile International / CMLink** | — | Carrier eSIM | China, global diaspora | ⚠️ **Named in RedteaGO's own Apple listing** as a coverage source: *"Based on CMI's global partners, operators around the world as service providers on CMLink eSIM."* **A supplier/partner, not a competitor** — but it is a real China relationship worth understanding | [apps.apple.com/.../id1492864476](https://apps.apple.com/us/app/redteago/id1492864476) |

### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| **Airalo** | ⭐ **PRIMER** | Date not established — present as at 2026-10-11 | Travel eSIM | [www.airalo.com/terms](https://www.airalo.com/terms) |

> ### ⭐ This is the most valuable single fact in the report, so here is the evidence in full
> Airalo's own i18n message table contains **23 distinct keys in a `validations.primer.*` namespace**:
> ```
> validations.primer.card-form-unexpected-field   .card-number-error
> validations.primer.client-session-update-error   .default-error
> validations.primer.duplicate-payment-method     .idempotency-key-exists
> validations.primer.initialization-error          .invalid-argument
> validations.primer.invalid-flow                  .missing-email
> validations.primer.missing-name                  .payment-creation-disabled
> validations.primer.payment-failed                .payment-method-not-compatible
> validations.primer.payment-method-not-provided   .payment-method-not-setup
> validations.primer.server-error                  .three-ds-auth-failed
> validations.primer.tokenization-error            .validation-error
> validations.primer.vault-delete                  .vault-fetch
> validations.primer.vault-validation
> ```
> Alongside **45 distinct `validations.stripe.*` keys** (the full Stripe decline-code taxonomy), a **`paypal_enabled`** feature flag, a **live Stripe publishable key** in the runtime config (🔒 value not transcribed), Datadog RUM, and `airmoney` (Airalo's stored-value wallet).
>
> 🚩 **And I checked the Flexiroam trap before reporting this.** Flexiroam's 16 `primer` hits were all French `Supprimer` and Spanish `primera`/`primeros` in i18n strings. **These are categorically different:** a structured `validations.primer.*` namespace whose members are **Primer's own API error taxonomy** — `client-session-update-error`, `idempotency-key-exists`, `vault-fetch`/`vault-delete`/`vault-validation`, `payment-method-not-compatible`, `invalid-flow`. **No natural-language word produces twenty-three dot-delimited keys that match an orchestrator's error contract. This is Primer.**
>
> ⚠️ **Source honesty:** the URL `https://www.airalo.com/terms` returned **HTTP 404**, but served Airalo's full 108KB Nuxt application shell with the global runtime config and i18n table embedded. `www.airalo.com/` itself returns **403** to this session (bot protection). **The content is unambiguously Airalo's own, served from Airalo's origin — but the status code was 404 and that is stated rather than hidden.**
>
> 🎯 **Why it matters here:** RedteaGO's largest competitor runs a **global payment orchestrator with full decline-code mapping and card vaulting**, while RedteaGO runs a **home-built shim with generic error strings and no vaulting.** That is competitive urgency with a specific, checkable shape — and it is the one ICP row on this account that needs no caveat.

### 11D. Prospect Scoring

Applied to the two competitors where real evidence exists. **Only verified signals; every uncertain row is 0.**

**Airalo**

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| Monthly transaction count | 0 | ⬜ Not researched | — |
| Orchestration status | **+1** | ✅ **Global orchestrator (Primer) incumbent** — competitive motion, hardest sell | [airalo.com/terms app shell](https://www.airalo.com/terms) |
| 3+ countries | **+3** | ✅ Global travel eSIM, SG-HQ | same |
| Multiple PSPs | **+3** | ✅ Stripe + PayPal behind Primer | same |
| Local rail gap in top-3 market | 0 | ⬜ Traffic profile not researched | — |
| Recent expansion | 0 | ⬜ Not researched | — |
| Payment issues | 0 | ⬜ Not researched | — |
| Funding >$10M | 0 | ⬜ Not researched | — |
| High traffic outside home | 0 | ⬜ Traffic not researched | — |
| Competitor on orchestration | 0 | ⬜ Not researched | — |
| Payment job postings | 0 | ⬜ Not researched | — |
| **TOTAL** | **7 / 29** | 🔴 **Low on evidence gathered — NOT a verdict.** Eight rows are deliberate zeros because Airalo was researched only as a competitor data point. **A dedicated run would score far higher. Do not treat 7 as Airalo's score.** | |

**Flexiroam** — already scored **16 / 29 🟢 Medium** in this repo (`2-ready-to-outreach/flexiroam.md`). Not rescored here.

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | **Airalo** | Direct competitor | Global, SG-HQ | 7/29 *(8 rows unresearched)* | ⭐ **Worth a dedicated run** | **Primer + Stripe confirmed — orchestration-aware, so the sale is reach, not education** | ✅ **CHECKED BY THE ORCHESTRATOR 2026-10-12 — Airalo IS on `apac-tal.csv`** (Esims & Connectivity). Not a missing account. **But its `Payment Orchestrator` column is EMPTY while this run found Primer — fix the column and the motion** |
| 2 | Flexiroam | Direct competitor | Global, MY ops | 16/29 | 🟢 Medium | In-house Stripe+Airwallex layer; ⚠️ **but the addressable consumer checkout is ~US$3m and shrinking by stated strategy** | ✅ **Already researched in this repo** |
| 3 | Nomad | Direct competitor | Global, SG-HQ | Not scored | 🟢 **Worth a look** | APAC-HQ'd, in territory, stack unknown | Not checked |
| 4 | Holafly | Direct competitor | Global, ES-HQ | Not scored | 🟡 Lower | **Spain-HQ'd — out of territory on HQ**; in scope only if it sells into APAC at scale | Not checked |
| 5 | Saily | Direct competitor | Global, LT-HQ | Not scored | 🟡 Lower | **Lithuania-HQ'd — out of territory on HQ** | Not checked |
| 6 | Ubigi / Transatel | Direct competitor | Global, FR-HQ (NTT) | Not scored | 🟡 Lower | **France-HQ'd — out of territory on HQ**; NTT ownership makes the Japan rails question interesting | Not checked |

⚠️ The research run did not cross-check these against `accounts/apac-tal.csv` and flagged it rather than guessing. **The orchestrator checked on 2026-10-12. Results:**

| Competitor | On the TAL? | Action |
|---|---|---|
| **Airalo** | ✅ **YES** — Esims & Connectivity | 🚩 **`Payment Orchestrator` column is EMPTY, but this run found Primer.** An empty column reads as greenfield and would send someone in with the wrong motion entirely. **Fix the column to Primer and the motion to Competitive.** |
| **GlocalMe (Uroaming)** | ✅ **YES** — Esims & Connectivity, HQ China | Already a target |
| **Alosim** | ✅ **YES** — Esims & Connectivity | Already a target |
| **Flexiroam** | ✅ **YES** — already researched at 16/29 | Stripe + Airwallex confirmed |
| Holafly · Nomad · Saily · Ubigi | ❌ not checked | Still open |

🔑 **So the by-product of this run is not a new account — it is a wrong column on an existing one.** Airalo is the category leader, Singapore-HQ'd and in territory, and the TAL currently implies it has no orchestrator. **That is the most valuable correction here.**

---

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | 🛑 **NOT FOUND.** The TAL's **~$30M is UNVERIFIED and should not be quoted.** No figure is published for RedteaGO, eSIM Access Limited or Redtea Mobile. CB Insights shows revenue as not disclosed. A third-party aggregator estimate of ~$37.5m surfaced in a search summary but **also contradicts CB Insights on HQ country and is not carried forward** | [cbinsights.com/company/redtea-mobile/financials](https://www.cbinsights.com/company/redtea-mobile/financials) |
| GMV / Gross Transaction Volume | **NOT FOUND** | — |
| Average Transaction Value (USD) | 🛑 **NOT FOUND.** What IS sourced is the **price range**: destination entry ("floor") prices run **$0.10 – $8.80**, decoded from first-party data (prices held in a **1/10,000 USD minor unit**, confirmed by the formatter `(e/1e4).toFixed(2)`). Google Play description: *"Data plan price from $0.54."* Real purchases visible in reviews: **$2.38** (1GB/30d) and **$68**. ⚠️ **Floor prices are not an AOV. The actual average ticket is unknown** | [esim.redteago.com/](https://esim.redteago.com/) · [topup.1b0f774.js](https://esim.redteago.com/_nuxt/pages/topup.1b0f774.js) · [play.google.com/.../com.redteamobile.redteago](https://play.google.com/store/apps/details?id=com.redteamobile.redteago) · [trustpilot.com/review/redteago.com](https://www.trustpilot.com/review/redteago.com) |
| Est. Annual Transactions | 🛑 **NOT DERIVABLE.** Both inputs are missing: revenue is unverified and ATV is unknown. **Per the disclosure rule, arithmetic on an unsourced input produces an assumption, not a derivation — so none is offered** | — |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ~40,000–50,000/month. `[ASSUMPTION — not researched.]`** **Billing unit counted: one prepaid eSIM data-plan purchase, plus RedteaGO Credit wallet top-ups as a second, separate unit.** **Basis:** no transaction, order, activation, subscriber or ARPU figure is published anywhere; the supplied SimilarWeb dataset is **shares only with no total**, so no visits-to-orders path exists either; and the only sourced volume proxies are **Google Play 100K+ lifetime installs** and **893 Apple ratings / 1.24K Play reviews** — the Play figure being structurally blind to mainland China, which is 74.32% of their traffic, **because Google Play is unavailable there** (which is precisely why they publish a Pgyer APK). Scored at the conservative **+2** band. 🛑 **An ASSUMED figure cannot and does not trigger the under-40,000 rejection. The true number could be materially higher or lower. This is the #1 discovery question on this account** | See the ICP breakdown and Manual Research Recommendations |
| Active Customers / Users | **Google Play 100K+ lifetime downloads** (Android, excludes mainland China) · **893 Apple US ratings** · **1.24K Play reviews** · **74 Trustpilot reviews.** No company-published user figure found | [play.google.com](https://play.google.com/store/apps/details?id=com.redteamobile.redteago) · [apps.apple.com](https://apps.apple.com/us/app/redteago/id1492864476) · [trustpilot.com](https://www.trustpilot.com/review/redteago.com) |
| Primary Currency | ✅ **USD — settlement AND base.** *"All transactions are settled in US dollars (USD)"* (Terms §4.1, EN + zh-CN); `baseCurrency: "USD"`, `currentCurrency: "USD"` in the storefront state. **13 DISPLAY currencies: USD, GBP, JPY, THB, TRY, KRW, HKD, SGD, RUB, INR, CAD, CNY, EUR** — with hard-coded client-side FX multipliers | [agreement](https://esim.redteago.com/agreement) · [esim.redteago.com/](https://esim.redteago.com/) |
| Top 3 Markets by Revenue | 🛑 **NOT FOUND.** No geographic revenue split published. **By TRAFFIC the top three are China 74.32%, US 6.30%, Australia 2.17%** — but the China row's engagement profile means traffic share is a poor revenue proxy here, and that caveat must travel with the number | SimilarWeb (supplied 2026-10-11) |
| Billing channel split (web vs app store) | 🛑 **NOT FOUND, and it matters.** **Web is card/APM-billed** (Stripe, Nuvei, PayPal, Adyen — confirmed). **Apple shows NO In-App Purchase enumeration** (the Flexiroam test, passed). **Google Play DOES declare "In-App Purchases"** — unresolved contradiction. No StoreKit, Play Billing or RevenueCat tokens in any bundle. ⚠️ **The web/app volume split is unknown on an explicitly app-first merchant, so the orchestration-addressable share of revenue is unknown.** Discovery question #2 | [apps.apple.com](https://apps.apple.com/us/app/redteago/id1492864476) · [play.google.com](https://play.google.com/store/apps/details?id=com.redteamobile.redteago) |

*"No public revenue/GMV data found. Business case sizing will require a discovery call."* Every figure above that is an estimate is labelled; nothing is presented as measured that is not.

---

## Overall Research Confidence

**MEDIUM-HIGH on the payment stack and the China mechanism. ZERO on volume and revenue.**

⚠️ **Method deviation, disclosed as instructed.** **There is no Agent/Task tool in this environment.** Phase 2's Agents 2–5 could not be spawned in parallel. **All four workstreams were run sequentially by a single analyst under the same per-agent budgets** (PSP/orchestrator/PCI; APMs; complaints/news/checkout; competitors). The practical effect is positive rather than negative here: a single analyst carried the first-party code findings across all four workstreams, which is how the Nuvei↔`payMethod 14`↔`/nuvei-jump` chain and the `supportCurrency`↔USD-settlement contradiction were connected at all. **Confidence is not downgraded for the deviation itself.**

**Traffic data provenance, stated explicitly because it drives the APM analysis and two ICP rows:** **SUPPLIED by Prateek** (`accounts/traffic/redteago.md`, SimilarWeb, Jul–Sep 2026), used verbatim and **not re-researched**. 🛑 **Two structural limits in it:** (1) **shares only — no total visit count**, so nothing absolute can be derived; (2) **"include all country domains" was OFF** and, more importantly, **all commerce lives on the `esim.redteago.com` subdomain while the measured property is `redteago.com`**, a WordPress.com marketing site. **The supplied table may therefore describe the brochure site rather than the shop.**

**Strong coverage:**
- ✅ **Payment stack** — four acquiring paths with first-party code evidence, the full in-house payment API surface, the resolved `payMethod` enum, the `supportCurrency` table, the minor-unit encoding. Fetched into a **clean empty directory** to avoid stale-asset contamination; `--compressed` used on every request; all greps run with `LC_ALL=C` and `-a` against **raw source**, never extracted text.
- ✅ **The China question** — the locale 302 reproduced twice with two user agents; the Pgyer APK channel fetched and dated; the Mini Program question probed five ways and answered negative; CJK byte density measured by raw byte class as instructed.
- ✅ **Entities and the billing question** — the contracting entity, its address and the Terms date come from the first-party Terms and Privacy Policy; the app-store sellers from the listings themselves.
- ✅ **False-positive control** — seven traps caught and documented, including a 135-hit `omise` (all `Promise`) and an 8-hit `upi` (all `TopupIdx`), plus the `supportCurrency` judgement reasoned out explicitly in both directions rather than assumed.
- ✅ **Competitive intelligence** — Airalo's Primer+Stripe stack from Airalo's own i18n table, with the Flexiroam `primer` trap explicitly checked and rebutted.

**Limited or absent:**
- 🛑 **Volume and revenue: nothing.** No transaction count, no revenue, no GMV, no ATV, no user count, no visit total. The monthly transaction figure is **ASSUMED** and labelled as such everywhere it appears.
- 🛑 **The server-side payment-method list was not obtained.** `/v1.1/query/payments` and `/v1/payment/nuvei/options` require a body-derived request signature; reconstructing it was **blocked by this environment's safety classifier and not retried.** **Several ❌ rows in Section 4 could flip if that list were read.** This is the largest single gap in the report and it is an environment limit, not an analysis gap.
- 🛑 **Mainland-China acquiring licensing: claim deliberately omitted.** The only reachable source (IBA, published 1 March 2023) predates the 2024 non-bank payment regulations and explicitly does not address foreign merchants collecting from Chinese consumers; `law.asia` returned 403. **Per the integrity rules, no regulatory requirement is asserted.** The first-party USD-settlement evidence carries the cross-border point without it.
- ⚠️ **No registration number for any entity.** Neither the HK Companies Registry nor ACRA BizFile was reachable.
- ⚠️ **Adyen's live status rests on one endpoint and one evidence type.**
- ⚠️ **The acquiring route to Alipay and WeChat Pay is not established** — named as platforms, no SDK or endpoint found.
- ⚠️ **Three competitors' stacks are "not established", not absent** — client-rendered homepages, no checkout walk performed.
- ⚠️ **No CSP on either host**, so the `frame-ancestors` asset-map technique yielded nothing.
- ⚠️ **Several Trustpilot and news items rest on search summaries.** Where a page was not fetched, the claim is marked `[UNVERIFIED — search summary only, page not fetched]`. The Trustpilot distribution, the CB Insights funding record, the group press release and the eSIM Access positioning **were** fetched and read.

---

## Manual Research Recommendations

> **Area:** 🔴 **Monthly transaction count and web-vs-app revenue split** — Section 12, and the top ICP row
> **Why it matters:** It is the only signal that can reject the account, and it is **ASSUMED**. The supplied traffic data has no total, no revenue figure exists, and the Play install count is structurally blind to 74% of their audience. **Everything else in this report is moot if the real figure is under 40,000.**
> **Suggested manual action:** Ask directly on the first call: monthly paid orders, split web versus iOS versus Android, and whether Credit top-ups are counted separately. Frame it as sizing, not qualification.

> **Area:** 🔴 **The server-side payment-method list** — Section 4's biggest gap
> **Why it matters:** `/v1.1/query/payments` and `/v1/payment/nuvei/options` hold the authoritative method set and the Nuvei country→method matrix. **Several rails I have marked ❌ NOT FOUND may in fact be live through Nuvei's redirect branch.** Getting a rail wrong in outreach on this account would be fatal to the thread.
> **Suggested manual action:** Walk checkout in a browser with DevTools open from CN, IN and AU VPN exits and read the two JSON responses. Fifteen minutes, and it closes the gap properly — which this environment could not.

> **Area:** 🟠 **Whether the in-house layer actually routes** — Section 3B
> **Why it matters:** If it retries, fails over and cascades, the in-house objection is strong and the sale is reach only. **If it is just a method-selection shim with no retry logic and no decline telemetry — which is what the absence of any retry/decline instrumentation in the bundles suggests — the objection is far weaker than it appears** and the Airalo decline-mapping comparison becomes the lead argument.
> **Suggested manual action:** One question: "when a card declines, does your layer re-attempt on a different provider, or does the customer see the error?" The answer picks the motion.

> **Area:** 🟠 **The Google Play In-App Purchase declaration** — Section 12
> **Why it matters:** Apple shows no IAP; Google declares it. If a meaningful share of Android revenue runs through Play Billing, that share is untouchable by orchestration — and Android is the China-facing channel.
> **Suggested manual action:** Ask what the Android app charges through. Also worth raising that **the Pgyer APK serving their largest market is 14 versions behind Google Play (2.5.3 vs 2.5.17)** — it is a genuinely useful observation that has nothing to do with payments and proves the homework.

> **Area:** 🟠 **Whether mainland China sees a degraded or blocked site** — the one China hypothesis not excluded
> **Why it matters:** It is the remaining alternative explanation for the 6-second session, and it cannot be tested without a mainland vantage point. If the site is partly blocked, the 74.32% is a different number than it looks.
> **Suggested manual action:** Ask, or test from a mainland exit node. Phrase it as curiosity about their China experience — it is a question they will enjoy answering.

> **Area:** 🟡 **Entity registration numbers and the Airalo TAL check**
> **Why it matters:** No registration number was obtainable for any of the four entities, and **Airalo — the category leader, Singapore-HQ'd, confirmed on Primer — may not be on the target account list at all.**
> **Suggested manual action:** HK Companies Registry e-Services for eSIM Access Limited; ACRA BizFile for Redtea Mobile Pte. Ltd.; and grep `accounts/apac-tal.csv` for Airalo before anything else — **if it is absent, that is the most valuable by-product of this run.**

---

## Appendix: All Source URLs

**First-party — RedteaGO / eSIM Access (fetched 2026-10-11 into a clean directory)**
- https://redteago.com/ — marketing site (WordPress.com-hosted; `apple-itunes-app` Smart App Banner; app + Pgyer links)
- https://esim.redteago.com/ — storefront; `supportCurrency`, `baseCurrency: "USD"`, locale set, FAQ #2013
- https://esim.redteago.com/zh-CN — Chinese storefront; ~19,000 CJK bytes; zh-CN Terms
- https://esim.redteago.com/agreement — **Terms of Service, last updated 6 May 2026**; eSIM Access Limited + HK address; §4.1 processors and USD settlement
- https://esim.redteago.com/zh-CN/agreement — Chinese Terms; 支付宝 / 微信支付 / USD settlement
- https://esim.redteago.com/privacy-policy — Privacy Policy; *"eSIM Access Limited doing business as RedteaGO"*; cookie policy effective 2025-12-29
- https://esim.redteago.com/topay — pay page; Visa / Mastercard / Amex / JCB / **UnionPay** brand marks
- https://esim.redteago.com/topup · /credit · /refund-policy · /about-redteaGO
- https://esim.redteago.com/_nuxt/app.c8dae81.js — **`/v1/payment/nuvei/options`, `/v1/get/payparam/adyen-pay`**, the full payment API surface, Stripe keys (🔒 not transcribed), `nobel` backend, QQ/163/126 mail hosts, `redteamobile.udesk.cn`
- https://esim.redteago.com/_nuxt/pages/topay.1a026be.js — **Stripe Elements, `confirmCardPayment`, `payMethod: 6`**
- https://esim.redteago.com/_nuxt/pages/topup.1b0f774.js — **`paypalPay()`, `payMethod === 14`, `queryNuveiPaymentAPI`, the `/1e4` price formatter**
- https://esim.redteago.com/_nuxt/4.42d059a.js — the **Nuvei country→method picker** component
- https://esim.redteago.com/_nuxt/runtime.8105155.js — route/chunk map including `pages/nuvei-jump`
- https://esim.redteago.com/_nuxt/{commons.app,defaultVendors.app,pages/index,pages/credit,1.4953552,3.3bce599}.js — searched for all vendor tokens
- https://www.pgyer.com/RedteaGOeSIM — **RedteaGO APK, v2.5.3 (build 3), 20.5 MB, published 2025-06-20**

**Corporate / group**
- https://redteamobile.com/news/post21/ — **Redtea Mobile Group, 28 Jan 2026**; Global + China; executives; Shenzhen copyright holder
- https://redteamobile.com/news/post20/ — AfricaCom 2025
- https://www.redteamobile.com/redtea-go-consumer/ — product portfolio: "For Consumers: RedteaGO" · "For Travel Partners: eSIMAccess"
- https://esimaccess.com/docs/why-choose-esim-access/ — eSIM Access as a **B2B aggregator** sourcing plans from Redtea Mobile
- https://www.gsma.com/solutions-and-impact/technologies/esim/wp-content/uploads/2026/07/Dr-Hui-Jin-Redtea-Mobile.pdf — Group CEO, Jul 2026
- https://www.cbinsights.com/company/redtea-mobile/financials — **$10M total, 4 rounds, Series B 7 Jul 2022**; revenue not disclosed

**App stores**
- https://apps.apple.com/us/app/redteago/id1492864476 — seller **REDTEA MOBILE PTE. LTD.**; 4.5 / 893 ratings; **no IAP enumeration**; CMI/CMLink coverage note
- https://play.google.com/store/apps/details?id=com.redteamobile.redteago — developer **REDTEA MOBILE PTE. LTD.**; **100K+ downloads**; 3.7 / 1.24K reviews; **"In-App Purchases" declared**; v2.5.17; *"price from $0.54"*

**Complaints**
- https://www.trustpilot.com/review/redteago.com — 74 reviews; 5★50/4★8/3★4/2★3/**1★35**; **score withheld** *"due to a breach of our guidelines"*; Singapore address; dated refund complaints

**Competitors**
- https://www.airalo.com/terms — ⭐ **23 `validations.primer.*` keys + 45 `validations.stripe.*` keys + `paypal_enabled` + live Stripe key (🔒 not transcribed) + `airmoney`.** ⚠️ HTTP **404** status, full Airalo Nuxt app shell served
- https://esim.holafly.com/ · https://esim.holafly.com/terms-and-conditions/ — no processor token
- https://www.nomadesim.com/ · /pages/terms-of-service — no processor token
- https://saily.com/ — no processor token
- https://www.ubigi.com/ — no processor token
- `2-ready-to-outreach/flexiroam.md` (this repo) — **Stripe + Airwallex, in-house routing layer**, 16/29

**Regulatory — checked and NOT used**
- https://www.ibanet.org/e-payment-guide-regulatory-landscape-in-China — published **1 March 2023**; predates the 2024 non-bank payment regulations; **explicitly does not address foreign merchants collecting from Chinese consumers.** 🛑 **No regulatory claim is made in this report on the strength of it**
- https://law.asia/new-rule-third-party-payments/ — **HTTP 403**, not readable
- https://www.rba.gov.au/payments-and-infrastructure/resources/payments-data.html — publishes spreadsheet links only, **no figures**; therefore no Australian rail-prominence claim is made
- https://www.npci.org.in/what-we-do/upi/product-statistics — returned no figures; therefore **no UPI volume claim is made**

</details>
