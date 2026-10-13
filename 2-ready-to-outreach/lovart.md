# Lovart

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 21 / 29 → ⭐ **High Priority**
**Industry:** AI design agent — consumer/prosumer subscription + credits (Free / Starter / Basic / Pro / Ultimate / Team) · **HQ:** China (Google Cloud's own customer page: *"Location: China"*) · **Billing entity:** Resonate International INC (Delaware, USA) · **Researched:** 2026-10-13 · **First email sent:** —
**Motion:** **In-house orchestration layer** — a self-written `resolvePayway()` router across **three acquirers** (Stripe, Antom, Waffo) plus a fourth China-domestic path
**Motion detail:** Decompiled from their own production bundle. Routing is decided in **browser JavaScript off browser language and IANA timezone** — not off BIN, not off performance. Do **not** pitch "you need orchestration": they built one. Pitch **what their router cannot reach** — the rails and the decision quality.

---

> ### ⚠️ Four things to read before anything else
>
> **1. ⭐⭐ THE CHINA QUESTION IS ANSWERED, AND THE ANSWER IS THE PITCH.** China is the #1 market at **19.68%**. Lovart monetises it — but **cross-border and in USD**, not domestically. Their own Chinese-language page says *"Starter 起 **$15/月** … **支持支付宝**"* (Starter from **US$15/month** … **Alipay supported**) — a **dollar** price and **Alipay only**. In their production code, **WeChat Pay is hard-coded off** (`isSupportWxpay` is `useMemo(()=>!1,[])`), and **UnionPay appears nowhere** in 4.1 MB of shipped JavaScript. The China-domestic rails — Alipay **and** WeChat Pay JSAPI, priced in **¥**, with an Alipay periodic-deduction mandate — exist, but on a **different product** (`xingliu.art`, 星流) under a **different legal entity** (上海哩布哩布科技有限公司, ICP 沪ICP备2025147903号-6). **Their largest market is served by the sibling product, and on lovart.ai it is served cross-border in dollars with one wallet.**
>
> **2. ⭐ THE APP-STORE TRAP DOES NOT FIRE — AND THIS IS LOAD-BEARING.** Per `subscription-payments.md` §4 this check can invalidate a consumer-subscription account. It does not here. **No official Lovart app exists** in the US, Singapore, Japan, Hong Kong, Brazil **or China** App Store (searched via the iTunes API; the only "Lovart" results are third-party squatters under other sellers' bundleIds) and **none on Google Play** (five candidate package IDs → 404; a Play search for "lovart" returns no Lovart-published app). `PaymentMethod.APPLE` and `PaymentMethod.GOOGLE` exist as **enum members only — zero call sites** in the whole bundle, and there is no StoreKit, RevenueCat or restore-purchase code. **Billing is web, end to end. The orchestratable share is ~100% of revenue**, which is better than the comparable Manus AI account.
>
> **3. IDENTITY AND TERRITORY, SETTLED WITH SOURCES — AND NOT THE WAY THE STUB GUESSED.** Lovart and LiblibAI are **not two unrelated companies and not one company either**: they are **two products of one group**. First-party proof, from Lovart's own shipped code: the HTTP client class is literally **`LiblibAxiosBase`**, the test-environment CDN is **`liblibai-web-static.liblib.cloud`**, image hosts are `liblibai-online.liblib.cloud` / `images-wm.liblib.cloud`, there is a complete **`XingliuMigration`** flow (`xlToken`, `libLoginPayload`, `confirmXingliuMigration`, `PromotionKind.XlMigratedDiscount`, "迁移专享价"), and `xingliu.art` ships Lovart's own CSS design tokens (`--mantine-color-lovart-green-*`). Parent is **Evoken** (formerly Qidian Xingyu Technology), **Beijing-based**, per Yicai Global 2026-06-18. **In territory.** ⚠️ But the contracting entity in the Terms is **Resonate International INC, Dover, Delaware** — if your org assigns accounts by billing entity rather than HQ, AMER could contest this. Flag it before you build the sequence.
>
> **4. 🚩 NO EXPANSION NARRATIVE, AND DON'T WRITE ONE.** Eight of eleven top markets are contracting (US ↓26.69%, Pakistan ↓32.61%, Morocco ↓25.97%, HK ↓19.24%); only Brazil and India grew. Their own **changelog's most recent entry is 2026-05-06** and the **newsroom's is 2025-10-13** — five and twelve months stale. Never tell them their traffic is falling. It does set the angle: **conversion, approval rate and recovered revenue — not scale.**

---

---

> ## 🔍 ANALYST AUDIT — Prateek, 2026-10-13
>
> **Score and motion stand: 21/29 ⭐, In-house orchestration.** I re-decompiled the bundle independently and **the router is confirmed verbatim.** This is the best technical evidence in the pipeline.
>
> ### ✅ THE SPINE, VERIFIED CHARACTER-FOR-CHARACTER
> From Lovart's own current production chunks, fetched by me:
> ```
> "resolvePayway",0,function(e,r){ return t.isCN ? a.Payway.CN_ALIPAY
>                                       : i(e,r) ? a.Payway.ANTOM_NEW
>                                       : o(e,r) ? a.Payway.WAFFO
>                                                : a.Payway.STRIPE }
> ```
> And the decisive constant: **`t.s(["config",0,k,"isCN",0,!1],82033)`** — `!1` is minified `false`. **The `CN_ALIPAY` branch ships and can never execute on `lovart.ai`.** Chinese-language visitors fall through to **`ANTOM_NEW`**. Counts in the payment chunks: `resolvePayway` 2 · `CN_ALIPAY` 11 · `ANTOM_NEW` 11 · `WAFFO` 11 · `checkIsCn` 8 · `payway` 69 · `antom` 21 · `stripe` 15 · `alipay` 16.
> Also confirmed from their own code: `cnAlipayJsapiInfo:"/api/www/pay/alipay/jsapi/info"`, `cnPayOrder:"/api/www/pay/order"` and `PaywayAlipay:"payway-option-alipay"` — the China-domestic endpoints are referenced exactly as reported.
>
> ### ⚠️ A METHODOLOGICAL NOTE WORTH KEEPING — I nearly produced a false negative on this account
> My first pass fetched **all 50 chunks referenced from the homepage (3.77 MB)** and returned **ZERO** for `resolvePayway`, `CN_ALIPAY`, `ANTOM_NEW`, `WAFFO`, `checkIsCn`, `stripe` and `waffo` — against passing controls (`lovart` 349, `useState` 171). The run's cited chunk path also now **404s**, which made the finding look unreproducible.
> **It was a wrong-asset zero.** The payment router loads only on the **`/pricing` route**; just **4 chunks (236 KB)** are unique to it, and every token is in those four. **A 3.77 MB zero against the wrong asset is still a zero against the wrong asset.** The lesson for this repo: **on a route-split app, fetch the chunks of the route that does the thing you are looking for** — the homepage bundle is not the app. Content-hashed chunk paths also rotate, so a 404 on a previously-cited chunk means "redeployed", not "wrong".
>
> ### ⭐ Why the China finding is the pitch, in one line
> **They monetise their #1 market cross-border in USD on a single wallet, while their own group runs licensed domestic WeChat and Alipay rails for that same market on a sibling product under a Chinese entity.** That is an asymmetry inside their own group, evidenced on both sides from first-party code — the strongest move available, and it is an architecture decision rather than a licensing wall, which is why it is reachable in a conversation.
>
> ### 🚩 Which rows carry the tier — and the one real failure mode
> **The ⭐ rests on one ASSUMED row.** Monthly transaction count **+5** is `[ASSUMPTION — not researched]`: revenue is sourced (~US$80M ARR) but **ATV is not**, so it is an assumption, not a derivation. **Strike it entirely → 16/29 🟢 Medium.** But note the run's own sensitivity: **any awarded band keeps ⭐** (+3 → 19, +2 → 18); only treating it as unknown loses the tier. An assumption can never fire the under-40k reject, and rejection would need an average charge above ~US$167, which is not reachable here.
> The **sourced core is 16/29** without it. Rows correctly **not** inflated: recent expansion 0, competitor-using-orchestration 0 (Canva did domestic acquiring on Stripe, which is not orchestration), payment job postings 0.
>
> ### ⚠️ Two things to carry into any conversation
> 1. **Ant Group is an existing shareholder** in the US$300M round, and **Antom is Ant International's product.** Treat the China acquirer as **sponsored**: go around it, not at it. **Lead with Brazil/Pix and India/UPI, not China**, until Prateek has asked how the Antom relationship came about. That single answer decides the sequence.
> 2. 🛑 **The export-control screen is PARTIAL and is NOT a clearance.** BIS Federal Register only, **English names only — the Chinese entity names were never screened**. OFAC SDN, DoD 1260H and the Denied Persons List were not checked. With Tencent and Ant Group on the cap table, **this goes to Yuno legal before outreach**, not after.
>
> ### ⚠️ Territory has a real counter-argument
> HQ is China (in territory), but **the Terms name `Resonate International INC`, Dover Delaware, California law, San Francisco venue.** If Yuno assigns by billing entity rather than HQ, **AMER can contest this account.** Settle it before investing in a sequence.
>
> ### ✔️ Safety
> No credential value in the file. No booking link. No Yuno-competitor name anywhere. Structure 3/3. ICP re-added independently: **5+1+3+3+3+0+2+2+2+0+0 = 21 across 11 rows.** ✅

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Lovart is a web-based **AI design agent** — you describe a brief in natural language and it plans and executes a multi-step design job (images, video, brand kits, posters, packaging) on a canvas you can talk to ("ChatCanvas"). It is sold as a recurring subscription with a monthly **credit** allowance (Free / Starter / Basic / Pro / Ultimate) plus purchasable **credit top-ups** and a seat-based **Team plan**. Launched publicly **2025-07-28** off an 800,000-person waitlist; **"more than 5 million users"** per Google Cloud's own customer page. It is the **overseas sibling of 星流 (Xingliu)**, the Chinese-market version, both built by **LiblibAI's parent group, Evoken** (Beijing).

**SimilarWeb total visits (last full month):** **Not found.** The supplied extract (SimilarWeb, supplied by Prateek 2026-10-13, Jul–Sep 2026, "All traffic", "Include all country domains" ON) gives country **shares**, change, audience share and engagement, but **no absolute visit counts**. No visit total is asserted anywhere in this report.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | **China** | **19.68%** (↓7.71%) | **Alipay** (cross-border, via **Antom** / Ant International) + cards via Stripe — **priced in USD** on their own Chinese page | **WeChat Pay — hard-coded off** in their bundle (`isSupportWxpay` returns `!1`; the QR prompt string "请使用微信/支付宝扫码支付" is unreachable) · **UnionPay — zero occurrences** in 4.1 MB JS · **CNY pricing** (the `¥` symbol exists only behind the `isCN` build flag, which is `false` on lovart.ai) · **Alipay periodic-deduction mandate** (exists only on `xingliu.art`) | ❌ none for `lovart.ai` — the Chinese entity (上海哩布哩布科技有限公司) contracts for **`xingliu.art`**, not for Lovart |
| 2 | United States | 13.20% (↓26.69%) | Cards via Stripe (USD) | **PayPal** — zero occurrences · Apple Pay / Google Pay — enum members with **zero call sites** | ❌ none (Delaware registered-agent address only) |
| 3 | **Brazil** | **6.58%** (**↑5.99%** — one of only two growing markets) | Cards via Stripe, **USD-priced** | **Pix** — zero occurrences across 4.1 MB JS **and** every page fetched (and Pix was **54.7% of all Brazilian transactions** in H2 2025, Banco Central data) · **boleto** · **cartão parcelado** (instalments) | ❌ none found |
| 4 | Hong Kong | 5.76% (↓19.24%) | Routed to **Antom** (any `zh` / `zh-TW` browser language or `Asia/Shanghai` timezone), USD-priced | **FPS**, **Octopus**, **AlipayHK**, **WeChat Pay HK** — none present | ❌ none found |
| 5 | **India** | **5.66%** (**↑10.72%**) — **audience share 9.11%, far above traffic share** | Cards via Stripe, USD-priced | **UPI** — zero genuine occurrences (all 73 `upi` hits are `classGroupId` / `grouping` / `occupied`) · **UPI Autopay** · netbanking · RuPay · EMI / no-cost EMI | ❌ none found |

Markets 6–11: **Taiwan 4.34%** — `zh-TW` is explicitly routed to Antom; no JKOPay / LINE Pay / ATM transfer · **Singapore 3.32%** — no PayNow; routed to Antom if the browser is Chinese-language, else Stripe · **Japan 3.03%** — ⚠️ **the one market that may already be served**: a dedicated acquirer, **Waffo**, is selected whenever currency is `JPY`, language is `ja` **or** timezone contains `Asia/Tokyo`, and Waffo publishes Japanese local methods (konbini, PayPay, Pay-easy). **But team/seat orders have no Japan branch at all** and fall through to Stripe · **Egypt 2.80%** — no Fawry · **Pakistan 2.19%** — no JazzCash / Easypaisa · **Morocco 1.83%** — no local method.

> **Entity cells are marked ❌, not ❌🔒.** `apac-payments.md` flags China and India as markets gating domestic acquiring behind local presence, but **that file is a checklist, not a source, and no live regulatory source for a China or India acquiring licence requirement was verified in this run.** What *is* evidenced is stronger and citable: **a licensed China-domestic path demonstrably exists inside this group and demonstrably sits on the other product under the other entity.**

### Legal entities
- **Resonate International INC** (Delaware, USA) — **the contracting and billing entity for `lovart.ai`**, named identically in both the Terms of Use (updated **2026-07-09**) and the Privacy Policy (updated **2025-07-23**): *"The Services are offered by Resonate International INC … registered address at 8The Green, Suite B, in the City of Dover County of Kent Zip Code 19901, State of Delaware."* Governing law **California**; exclusive venue **San Francisco County**. ⚠️ `8 The Green, Suite B, Dover DE 19901` is a well-known **registered-agent address**, not an operating office. **Not confirmed on any registry** — Delaware's entity search is a CAPTCHA-gated ASP.NET form and was not reachable in this environment.
- **上海哩布哩布科技有限公司** (Shanghai Liblib Technology Co., Ltd.), 上海市徐汇区丰谷路315弄24号1-3层 — named in the footer of **`xingliu.art`**'s own production bundle, with ICP filing **沪ICP备2025147903号-6**. This is the **China-domestic operating entity for 星流 (Xingliu)**, Lovart's Chinese sibling. It is **not** named anywhere on `lovart.ai`.
- **Evoken** (formerly **Qidian Xingyu Technology**), **Beijing** — the group parent, per Yicai Global 2026-06-18. ⚠️ **Discrepancy, stated rather than smoothed over:** the parent is reported as Beijing-based while the ICP-filed operating entity is Shanghai-registered. Both can be true; neither was confirmed on a Chinese registry (`beian.miit.gov.cn` unreachable, `tianyancha.com` returned HTTP 419, `qcc.com` returned a login wall).
- **No entity found in any of the eleven top-traffic markets** for `lovart.ai`.

### Known PSPs
- **Stripe** — the **global default** and the fall-through for every market with no special rule. Two distinct accounts/rails are modelled: `Payway.STRIPE = 1` **and** `Payway.STRIPE_TWO = 2`; `STRIPE_TWO` is what the user gets when they click the "card or other payment" button in the payway modal. `[Source Code]` — `js/2cfihdcovcy8y.js`. ⚠️ **No `pk_live` key, no `js.stripe.com`, no `checkout.stripe.com` in the marketing bundle** — the flow is a **server-minted redirect**, so there is no key to find here (and none is recorded in this file).
- **Antom** (Ant International's merchant acquiring brand) — `Payway.ANTOM = 0` and `Payway.ANTOM_NEW = 3`. Selected for **every Chinese-language or `Asia/Shanghai`-timezone visitor**. Presented to the user as the **Alipay** button (`testId:"payway-option-alipay"`, outline colour `#1677FF`, i18n key `commercial_aliPay` → 支付宝). The return handler strips **`resultStatus`** from the URL — Antom/Alipay's own redirect parameter. `[Source Code]` + the merchant's own Chinese page saying **支持支付宝**.
- **Waffo** (`waffo.com`, *"The global payments and monetization platform for digital businesses"*, 480+ methods / 173 markets, offers **Merchant of Record**) — `Payway.WAFFO = 4`. Selected **only** for the Japan branch: `checkIsJp(currency, lang) = currency === "JPY" || lang === "ja" || timezone.includes("Asia/Tokyo")`. `[Source Code]`.
- **China-domestic Alipay** — `Payway.CN_ALIPAY = 5`, driven by `/api/www/pay/alipay/jsapi/info`, `/api/www/pay/order` and an `openCnQrPay` QR modal. **Dead code on `lovart.ai`** (the build flag is literally exported as `isCN: !1`). **Live on `xingliu.art`**, where the sibling bundle also carries **`/api/www/pay/wx/jsapi/info`** (WeChat Pay JSAPI), prices in **元**, and the renewal copy *"次月按X元/月自动续费，可在支付宝内取消订阅"* — an **Alipay periodic-deduction mandate**.
- **Apple / Google** — `PaymentMethod.APPLE` and `PaymentMethod.GOOGLE` exist in the enum and are **never referenced anywhere else**. **No shipped app found in any storefront checked.** Do not treat these as live channels.

### Orchestration status
**In-house orchestration layer — built, shipped, and decompiled.** The whole router is one exported function:

```
resolvePayway(currency, lang) =
    isCN                        ? Payway.CN_ALIPAY   // build flag, false on lovart.ai
  : checkIsCn(currency, lang)   ? Payway.ANTOM_NEW
  : checkIsJp(currency, lang)   ? Payway.WAFFO
  :                               Payway.STRIPE
```
with `checkIsCn = currency !== "JPY" && (lang ∈ {zh, zh-TW} || timezone.includes("Asia/Shanghai"))`.

Three live acquirers, a fourth path behind a build flag, and **a routing decision taken client-side from `Intl.DateTimeFormat().resolvedOptions().timeZone` and the UI language string.** There is no BIN-level routing, no performance-based routing, no cross-acquirer failover; the renewal is **pinned** to whatever took the first charge (`lastPaymentMethod` is read back and reused). Per the matrix this scores **+1, not +4** — they are not greenfield, and saying otherwise burns the thread.
Evidence: `js/2cfihdcovcy8y.js` (`Payway`/`PaymentMethod`/`PaywayMap` enums, `resolvePayway`, `checkIsCn`, `checkIsJp`, the payway modal), `js/0-hdccp5_46x3.js` (team-order payway), `js/1mx604a0-etun.js` (`isCN: false`), `js/0w95so0zkp1fq.js` + `js/1ascpfhw4u352.js` (CN Alipay JSAPI endpoints) — all fetched from `https://web-static3.lovart.ai/lovart_prd/static/_next/static/chunks/`.

### Buying signals
- 💰 **US$300M Series B+ at >US$2B valuation, announced 2026-06-18 — four months before this report.** Jointly led by **Granite Asia**, **Tencent** and **Shunwei Capital**; existing investors **Ant Group** and HSG also participated. Group ARR US$300M as of May 2026. ([Yicai Global, 2026-06-18](https://www.yicaiglobal.com/news/liblibai-parent-evoken-valued-at-over-usd2-billion-after-new-funding-round))
- 🤝 **⭐ Ant Group is an investor in the parent, and Antom is the China acquirer.** That is almost certainly not a coincidence, and it is the single most important thing to know before you open the China conversation: **the Antom relationship is probably sponsored, so do not go at it.** The opening is everything Antom is *not* being used for — the eight non-China, non-Japan markets in the top eleven.
- 🚀 **Lovart hit ~US$80M annualised revenue five months after launch** — the fastest-monetising product in the group. ([36Kr](https://eu.36kr.com/en/p/3899540157236869) · [Dealroom summary](https://dealroom.co/news/142733-liblib-ai-hits-2b-valuation-with-300m-series-b-extension-as-arr-reaches/))
- 🔁 **They are mid-migration right now.** A complete `XingliuMigration` flow ships in production — OAuth-style handoff from Xingliu, `confirmXingliuMigration({xlToken})`, status polling, and an `XlMigratedDiscount` promotion with the badge "迁移专享价" (migration-exclusive price). **A company moving a paying user base between two billing stacks is in a re-platforming window.**
- 📉 **Billing operations are visibly under strain.** Trustpilot **1.5 / 5 across 80 reviews, 84% one-star**, and the complaint pattern is overwhelmingly **billing**: charges continuing after cancellation, no self-service downgrade, stalled refunds. Most recent: **2026-10-12, one day before this report.**
- 📋 **No public payment RFP found.** **No payment-related job posting found** — `/careers` and `/jobs` both 404 on their own domain and nothing surfaced in search.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Lovart` to draft the 12-touch sequence, or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 21 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. `[ASSUMPTION — not researched.]`** See the mandatory disclosure block below. **An assumption never fires the under-40,000 rejection**, and here the rejection is not arithmetically reachable. |
| Orchestration status | **+1** | ✅ **In-house orchestration layer confirmed** — `resolvePayway()` routing across Stripe / Antom / Waffo, decompiled from their own bundle. **Not greenfield.** Per the matrix an in-house layer scores +1. |
| 3+ countries | **+3** | ✅ **Verified** — eleven countries above 1% traffic share (SimilarWeb supplied 2026-10-13), 118 countries in total. |
| Multiple PSPs | **+3** | ✅ **Verified** — three acquirers with first-party source-code evidence (Stripe incl. a second Stripe rail, Antom, Waffo), plus a fourth China-domestic path. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Verified twice over.** **Brazil (#3, 6.58%, growing): Pix absent** — zero genuine occurrences across 4.1 MB of JS and every page fetched (all 50 `pix` hits are `devicePixelRatio` / `subpixel-antialiased` / `screen_width_pixels`), against **54.7% of all Brazilian transactions** on Banco Central data, H2 2025. **China (#1, 19.68%): WeChat Pay hard-coded off** (`isSupportWxpay → !1`) and **UnionPay absent**. Both absences are sourced in the merchant's own production code, not assumed. |
| Recent expansion | **0** | ⬜ **Uncertain — deliberately not awarded.** No sourced new-market launch in the last 12 months for Lovart. Eight of eleven markets contracting; changelog silent since 2026-05-06; newsroom silent since 2025-10-13. The group's LibTV launch (Mar 2026) is a *sibling product*, not Lovart market expansion. |
| Payment issues | **+2** | ✅ **Verified, high frequency** — Trustpilot 1.5/5, 80 reviews, 84% one-star, billing-specific complaints dated 2025-11-08 → 2026-10-12. |
| Funding >$10M | **+2** | ✅ **Verified** — US$300M Series B+ at >US$2B, announced 2026-06-18 (Yicai Global), four months inside the window. ⚠️ **The round is the parent's (Evoken), not Lovart-the-product's**; Lovart is a product line, not a separately funded company. Awarded on the group. |
| High traffic outside home | **+2** | ✅ **Verified decisively** — home market (China) is **19.68%**, far under 60%; the listed top eleven total only **68.39%**, so roughly a third of traffic is outside them entirely. |
| Competitor using orchestration | **0** | ⬜ **Uncertain — not awarded, and I am not going to stretch it.** No competitor was confirmed adopting a **third-party orchestrator**. What *was* found is adjacent and useful but does not satisfy the row: **Canva** moved to **domestic acquiring with local wallets in Korea on Stripe** (Stripe's own case study), and `accounts/apac-tal.csv` records **Kuaishou/Kling** as "In-house Routing (CONFIRMED)" with five acquirers — ⚠️ internal TAL, not re-verified in this run. Both are Section 10 ammunition, not points. |
| Payment job postings | **0** | ❌ **Not met** — `/careers` and `/jobs` both 404 on `lovart.ai`; nothing in search. |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **⭐ High Priority (21/29)**
**No public payment RFP was confirmed, so no RFP override applies. No analyst override applied** — and the one that could have, the app-store override, was tested hard and **does not apply** (no shipped app in any storefront checked; `PaymentMethod.APPLE`/`GOOGLE` have zero call sites; no IAP SDK). On the contrary, the web-only billing channel makes the orchestratable share of revenue unusually **high**.

> ### ⚠️ WHICH ROWS CARRY THE TIER — read this before quoting 21/29
> **The ⭐ rests on one assumed row.** Strike the **monthly-transaction-count +5** (the only row that is not sourced) and the score is **16/29 → 🟢 Medium**. Every other awarded row is verified, so:
> - **+5 → ⬜ 0: 16/29 🟢 Medium.** This is the one failure mode.
> - **+5 → +3** (50k–99,999 band): 19/29 — **still ⭐**.
> - **+5 → +2** (40k–49,999 band): 18/29 — **still ⭐**.
>
> So **any awarded band keeps the tier; only treating the row as unknown loses it.** The **sourced** core of the score is **16/29**: multiple PSPs (+3), 3+ countries (+3), local rail gap (+3), payment issues (+2), funding (+2), traffic outside home (+2), in-house orchestration (+1). **Confirming the transaction count is discovery question #1.**

### Monthly transaction count — mandatory disclosure

**⚠️ NOT FOUND — ASSUMED ≥100,000/month. `[ASSUMPTION — not researched.]`**

**Billing unit being counted:** one **charge event** = one subscription period (monthly **or** annual) **or** one credit top-up **or** one Off-Peak Image Pack **or** one seat-based Team purchase. This matters here: **annual plans bill once per twelve months** while delivering credits monthly (their own FAQ: *"Credits for annual subscriptions are distributed on a monthly basis"*), so an annual-heavy mix **depresses** the charge count well below the subscriber count; **credit top-ups raise it**. There is **no** app-store or carrier channel to sit outside the count.

- **Sourced input:** **~US$80M annualised revenue for Lovart**, reached five months after launch — 36Kr, carried in [Dealroom's summary](https://dealroom.co/news/142733-liblib-ai-hits-2b-valuation-with-300m-series-b-extension-as-arr-reaches/) and [36Kr directly](https://eu.36kr.com/en/p/3899540157236869). That is **~US$6.67M of billing per month**.
- **Unsourced input: average transaction value.** No ATV, order count, subscriber count or paid-conversion rate is published anywhere I could find. **Because one input is unsourced, this is an assumption and not a derivation**, per the method's rule 2.
- **Sensitivity, anchored on their own published entry price of US$15/month** (lovart.ai's own Chinese pricing page): at a $15 average charge → **~444,000/month** · at $19 → ~351,000 · at $32 → ~208,000 · at $90 → ~74,000 · at $199 → ~33,500.
- **The under-40,000 rejection would require an average charge above roughly US$167**, which is irreconcilable with a free tier, a sourced US$15 entry tier, mid tiers reported at $19/$32, and à-la-carte credit packs. **The rejection is not arithmetically reachable.** The ≥100,000 band holds for any average charge below ~US$67.
- **Corroborating order of magnitude (not used in the arithmetic):** **"more than 5 million users"** — Google Cloud's own customer page. A 2% paid-monthly conversion would alone put charges at ~100,000/month. That too is an assumption; it is noted only because it points the same way.
- **One real caveat for the business case:** the US$80M figure is **~5 months post-launch (so roughly Dec 2025)** and traffic has since contracted in eight of eleven top markets. The current run-rate may be higher (the CEO told Google Cloud revenue "has grown by 10x" since adopting Nano Banana) or lower. **Nothing here is a measurement.**

**Action:** "confirm monthly charge count, and the monthly-vs-annual plan mix" is item #1 in Manual Research Recommendations.

### Source Notes
- ✅ **Three live acquirers plus a fourth China path, with the router itself** — `Payway`/`PaymentMethod`/`PaywayMap` enums and `resolvePayway` decoded out of `js/2cfihdcovcy8y.js`, fetched from `web-static3.lovart.ai`. 58 chunks, 4.1 MB, all 58 downloaded successfully and grepped.
- ✅ **WeChat Pay hard-coded off on lovart.ai** — `isSupportWxpay` is `(0,t.useMemo)(()=>!1,[])`, and the conditional QR string `"请使用微信/支付宝扫码支付"` is therefore unreachable, falling through to `"请扫码完成支付"`.
- ✅ **`isCN` is exported as `false`** in the lovart.ai build — `t.s(["config",0,k,"isCN",0,!1],82033)` in `js/1mx604a0-etun.js`. So the CNY/`¥` path and `CN_ALIPAY` are dead code *in this build* and live in the sibling build.
- ✅ **The China-domestic property, its entity and its ICP filing** — `上海哩布哩布科技有限公司 (上海市徐汇区丰谷路315弄24号1-3层)` and `沪ICP备2025147903号-6`, read out of `xingliu.art`'s own production bundle (30 of 37 chunks on the first pass, remainder retried; 7.8 MB total). Same bundle carries `/api/www/pay/wx/jsapi/info`, `/api/www/pay/alipay/jsapi/info`, `commercial_aliPay: "支付宝"`, 元 pricing and the Alipay auto-renew mandate copy.
- ✅ **The Lovart ↔ LiblibAI link is first-party, not a search summary** — `LiblibAxiosBase` / `LiblibAxiosError` as the HTTP client, `liblibai-web-static.liblib.cloud` as the test CDN, `liblibai-online.liblib.cloud` / `images-wm.liblib.cloud` as image hosts, `xla-persist.xingliu.art`, the full `XingliuMigration` flow with `libLoginPayload`, and `--mantine-color-lovart-*` design tokens shipping on `xingliu.art`.
- ✅ **US$15/month Starter and "支持支付宝"** — the merchant's own page, `https://www.lovart.ai/zh/topics/zh-pricing-cn`.
- ✅ **Billing entity Resonate International INC (Delaware), California law, San Francisco venue** — Terms of Use (2026-07-09) and Privacy Policy (2025-07-23), both on `lovart.ai`, read after stripping tags and double-unescaping entities.
- ✅ **Credit allowances per tier** — Starter 2,000 / Basic 3,500 / Pro 11,000 / Ultimate 27,000 monthly credits; top-ups valid 366 days from 2026-06-30 — merchant's own Subscribe FAQ (updated 2026-06-30).
- ✅ **Pix = 54.7% of all Brazilian transactions, H2 2025, 42.9bn operations vs cards 30.4%** — Banco Central data, reported [2026-04-08](https://www.band.com.br/economia/noticias/pix-lidera-pagamentos-no-brasil-com-547-das-transacoes-diz-banco-central-202604081055).
- ✅ **RBI e-mandate AFA rule, fetched live from rbi.org.in** — RBI/2022-23/73, CO.DPSS.POLC.No.S-518/02.14.003/2022-23, **16 June 2022**: AFA on the first e-mandate transaction on cards/PPIs/UPI; AFA waived for subsequent transactions **up to ₹15,000** (raised from ₹5,000).
- ✅ **Canva's Korean domestic acquiring** — Stripe's own customer story: *"Canva partnered with Stripe to implement domestic acquiring to support local cards and local mobile wallets"*; *"Since going live in 2024, Canva has increased their payment reach by over 9.5 million users"*; Authorization Boost + Adaptive Acceptance *"helped increase Canva's payment success rates by 2.1% and saved over 1.5% in network costs"*; localised experiences across *"top 40 markets"*.
- ✅ **BIS Entity List screen negative with a passing positive control** — see the compliance note in Section 6.
- ✅ **No app in any storefront checked** — iTunes Search API across **us, cn, sg, jp, hk, br** (controls passed: `canva` returned results in **cn**, and Gemini/Grok returned in us/sg/jp/hk/br); Google Play 404 on five candidate package IDs with a passing control (`com.canva.editor` → 200) and a Play search returning 20 apps, none Lovart-published.
- ⚠️ **No registry confirmation for any entity.** Delaware's search is CAPTCHA-gated; **ACRA BizFile+ is a client-rendered SPA and returned no results in HTML** (so the mandated Singapore check was *attempted and failed*, not skipped — and no Singapore entity is claimed anywhere by the company); OpenCorporates requires an API token; `beian.miit.gov.cn` was unreachable; `tianyancha.com` returned HTTP 419; `npci.org.in` returned HTTP 403.
- ⚠️ **"Melvin Chen, CEO and Founder, Lovart" (Google Cloud) and "Chen Mian, founder of LiblibAI" (press) are plausibly the same person. Not verified. Do not assert it.**
- ⚠️ **Tier prices above Starter are third-party only and conflicting** — one guide dated 2026-09-24 lists Starter $19 / Basic $32 / Pro $90 / Ultimate $199 monthly, and *itself warns* that Lovart-branded pages show conflicting plan names and numbers. **The credit allowances in that guide match the merchant's own FAQ exactly**, which corroborates the tier structure but not the prices. `[ESTIMATE, not confirmed]`.
- ⚠️ **Whether additional methods are enabled server-side cannot be seen from outside.** Both Antom and Stripe render enabled methods on their own domains after a server-minted redirect. Every rail finding here rests on (a) the merchant's own client code and published pages and (b) the two buttons their payway modal actually renders — never on a guess.
- ⚠️ **China market-share sourcing is weak and I am flagging it rather than dressing it up.** The best figure found for Alipay + WeChat Pay's combined share is **92% of the mainland market, on CB Insights data for end-2017**, via Digital Transactions (2018-08-13) — **eight years stale**. A Tencent Q1 2026 Weixin/WeChat MAU of ~1.432bn surfaced only in secondary aggregators: `[UNVERIFIED — search summary only, page not fetched]`. **The China *absence* is first-party and solid; the China *prominence* stat is not. Use the absence.**
- ⚠️ **Trustpilot reviews are unverified individual accounts.** They evidence a *complaint pattern*, not confirmed company behaviour. **Never cite their Trustpilot score to them.**
- ⚠️ **`Payway.WPS = 11` appears in the `xingliu.art` enum and nowhere on lovart.ai. Not identified.** Possibly a WPS Office distribution channel. Flagged, not guessed at.
- ⚠️ **Internal-TAL competitor stacks (Kuaishou, z.ai, MiniMax, Kling, Moonshot) were not re-verified in this run** and are labelled as such wherever used.
- 🔒 **Credential hygiene:** the production config contains a bot-protection site key and a device-fingerprint public key. **`[live keys present — values deliberately not recorded]`.** No `pk_live` or any other secret exists in this file.

### Success Case Alternatives
- **No Yuno public case study was verified in this research run, so none is named.** Naming a customer, or attaching a number to one, would breach the repo's referenceability rule. **Required profile for the right reference:** a **global digital-subscription-plus-credits business that already runs more than one acquirer**, where Yuno replaced *self-written, locale-based routing* with BIN- and performance-based routing and added LATAM + South Asian local rails, with a measured approval-rate or recovered-revenue outcome on **renewals**. The second-best shape: a merchant whose **Brazilian** revenue was card-only and who added **Pix**. Pull the matching named reference from Yuno's current published customer list before the sequence is written.

---

## Executive Summary

Lovart is the overseas AI-design-agent product of **Evoken** (Beijing), the group behind **LiblibAI** — a subscription-plus-credits business serving **118 countries** with **more than 5 million users**, which reached **~US$80M annualised revenue five months after its July 2025 launch** and whose parent raised **US$300M at a >US$2B valuation in June 2026** with **Ant Group** among the existing investors. The payment finding is unusual and better than a greenfield story: **they have already built an orchestration layer, and it is a thirty-line client-side function.** `resolvePayway()` picks **Antom** for anyone whose browser language is Chinese or whose timezone is `Asia/Shanghai`, **Waffo** for anyone on `JPY`/`ja`/`Asia/Tokyo`, and **Stripe** for the entire rest of the world — decided in JavaScript from `Intl.DateTimeFormat()`, never from a BIN, a decline code or an acquirer's performance, with the renewal pinned to whichever rail took the first charge. The consequence is a map of hard gaps: **their #1 market (China, 19.68%) is billed cross-border in US dollars on Alipay alone, with WeChat Pay hard-coded `false` in their own bundle and UnionPay absent entirely** — while the group's *licensed* domestic Alipay-and-WeChat rails, priced in ¥ with a proper auto-renew mandate, sit on the sibling product `xingliu.art` under a different Shanghai entity; and **Brazil (#3 and growing) has no Pix** against 54.7% of all Brazilian transactions, **India (#5, with an audience share of 9.11% against a traffic share of 5.66%) has no UPI and no UPI Autopay**, and Egypt, Pakistan, Morocco, Taiwan, Hong Kong and Singapore have no local rail at all. Billing is **100% web** — no App Store or Play app exists in any storefront checked — so unusually little of this revenue is out of reach. **Motion: in-house orchestration layer**, opened by a live user migration between two billing stacks and a Trustpilot billing-complaint pattern running to the day before this report.

---

## Section 1: Website Traffic Analysis by Country

**Data source:** **Path 1 — pasted SimilarWeb data supplied by Prateek.** `accounts/traffic/lovart.md`, cited throughout as *SimilarWeb (supplied 2026-10-13)*, period **Jul–Sep 2026**, "All traffic", "Include all country domains" ON, **single domain `lovart.ai`**, **118 countries**. Used **verbatim** and **not re-researched**. No SimilarWeb API or search-estimate path was used.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | **China** 🔺high priority | **19.68%** | Not found | ↓ 7.71% — declining | SimilarWeb (supplied 2026-10-13) |
| 2 | **United States** 🔺high priority | **13.20%** | Not found | ↓ 26.69% — declining steeply | SimilarWeb (supplied 2026-10-13) |
| 3 | **Brazil** 🔺high priority | **6.58%** | Not found | **↑ 5.99% — growing** | SimilarWeb (supplied 2026-10-13) |
| 4 | **Hong Kong** 🔺high priority | **5.76%** | Not found | ↓ 19.24% — declining | SimilarWeb (supplied 2026-10-13) |
| 5 | **India** 🔺high priority | **5.66%** | Not found | **↑ 10.72% — growing** | SimilarWeb (supplied 2026-10-13) |
| 6 | Taiwan | 4.34% | Not found | ↓ 3.05% — broadly flat | SimilarWeb (supplied 2026-10-13) |
| 7 | Singapore | 3.32% | Not found | ↓ 19.51% — declining | SimilarWeb (supplied 2026-10-13) |
| 8 | Japan | 3.03% | Not found | ↓ 15.28% — declining | SimilarWeb (supplied 2026-10-13) |
| 9 | Egypt | 2.80% | Not found | ↓ 4.30% — declining | SimilarWeb (supplied 2026-10-13) |
| 10 | Pakistan | 2.19% | Not found | ↓ 32.61% — declining steeply | SimilarWeb (supplied 2026-10-13) |
| 11 | Morocco | 1.83% | Not found | ↓ 25.97% — declining | SimilarWeb (supplied 2026-10-13) |

**Engagement (supplied, and it is strong — this is a real user base, not bounce traffic):** China 00:03:07 / 2.28 pages / 48.43% bounce · US 00:04:42 / 3.28 / 29.45% · Brazil 00:04:07 / 5.60 / 32.08% · HK 00:03:21 / 4.67 / 41.04% · **India 00:08:41 / 8.59 / 29.96%** · Taiwan 00:03:42 / 3.05 / 37.21% · Singapore 00:02:49 / 2.97 / 20.67% · **Japan 00:12:10 / 14.48 / 20.01% — exceptional** · Egypt 00:04:19 / 4.31 / 35.35% · Pakistan 00:09:46 / 4.94 / 41.63% · **Morocco 00:06:17 / 8.26 / 33.16%**.

**Three things the table says that the shares alone do not:**
1. **The top eleven are only 68.39% of traffic.** Roughly a third sits in the other 107 countries. "High traffic outside home" fires on any reading.
2. **India's audience share (9.11%) is 1.6× its traffic share (5.66%)** — many *distinct* users rather than a few heavy ones, and it is one of only two growing markets. For a payments conversation India is therefore under-weighted by the traffic column, not over-weighted.
3. **Japan at 00:12:10 and 14.48 pages/visit is the deepest engagement in the table** — and Japan is the only market for which they bought a **dedicated acquirer**. Those two facts are almost certainly connected, and they establish that this company *does* act on market-level payment evidence when it sees it.

**Domain check, done rather than assumed:** `lovart.ai` **301s to `www.lovart.ai`** (confirmed, `%{url_effective}`); `lovart.com` is an unrelated **parked lander** (114 bytes, `window.location.href="/lander"`) and is **not** a Lovart property; `lovart.vip` and `lovart.cloud` appear in the bundle only as **pre-production and test** environments (`www-pre.lovart.vip`, `www-test.lovart.vip`) and `www.lovart.vip` does not resolve. **`lovart.cn` could not be reached** — the egress proxy returned `CONNECT tunnel failed, response 502`, which is a **proxy failure, not a NXDOMAIN**, so **nothing is concluded about it**. The real second property is **`xingliu.art`**, which is a different brand, not a country domain, and would not appear under "include all country domains". **No traffic figure for `xingliu.art` was obtained and none is asserted.**

Top-10 markets with **no** confirmed local entity: **all eleven.**

---

## Section 2: Legal Entities & Local Presence

**Headquarters:** **China** — stated as *"Location: China"* on Google Cloud's own Lovart customer page. The group parent, **Evoken** (formerly **Qidian Xingyu Technology**), is reported as **Beijing-based** (Yicai Global, 2026-06-18). Lovart launched publicly **2025-07-28**. ⚠️ Several third-party directories list Lovart in **San Francisco** or **Dover, Delaware**; those are self-reported or auto-generated listings and are consistent with the Delaware billing entity and a US-facing go-to-market, not with an operating HQ.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| United States (Delaware) | **Resonate International INC** — the contracting and billing entity for `lovart.ai`; registered address 8 The Green, Suite B, Dover, Kent County, DE 19901 | Not found — Delaware entity search not reachable | [Terms of Use](https://www.lovart.ai/statement/terms-of-use) (2026-07-09) and [Privacy Policy](https://www.lovart.ai/statement/privacy-policy) (2025-07-23), identical wording in both |
| China (Shanghai) | **上海哩布哩布科技有限公司** (Shanghai Liblib Technology Co., Ltd.), 上海市徐汇区丰谷路315弄24号1-3层 — operator of **`xingliu.art`** (星流), Lovart's China sibling | **ICP 沪ICP备2025147903号-6** | Footer strings in `xingliu.art`'s own production bundle, `xla-web-static.xingliu.art/xingliu_prd/static/_next/static/chunks/` |
| China (Beijing) | **Evoken** (formerly Qidian Xingyu Technology) — group parent | Not found | [Yicai Global, 2026-06-18](https://www.yicaiglobal.com/news/liblibai-parent-evoken-valued-at-over-usd2-billion-after-new-funding-round) |
| Singapore | **None claimed and none found.** ACRA BizFile+ is a client-rendered SPA and returned no result in HTML; the company claims no Singapore entity anywhere | N/A | Attempted, failed — see Source Notes |

**Governing law and venue:** State of **California**; all disputes *"brought exclusively in the state or federal courts located in San Francisco County, California"*; jury trial and class actions waived (Terms §12).

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| China | ✅ #1 (19.68%) | ❌ for `lovart.ai` — ✅ **but for the sibling product, under a different entity** | ⚠️ `apac-payments.md` says yes; **no live regulatory source verified in this run**. What *is* evidenced: a licensed domestic path exists in this group and is not wired to Lovart | 🔴 **Highest in the account.** Alipay cross-border via Antom, **USD-priced**, WeChat Pay off in code, UnionPay absent |
| United States | ✅ #2 (13.20%) | ⚠️ Delaware registered-agent address only; no operating entity evidenced | ❌ No | 🟡 Cards acquired by Stripe; no PayPal, no wallets |
| Brazil | ✅ #3 (6.58%, **growing**) | ❌ | ❌ No, but **Pix and boleto are domestic-only instruments** | 🔴 **USD cards only into a market where Pix is 54.7% of all transactions** |
| Hong Kong | ✅ #4 (5.76%) | ❌ | ❌ No | 🟠 Routed to Antom on language/timezone; **no FPS, Octopus, AlipayHK or WeChat Pay HK** |
| India | ✅ #5 (5.66%, **growing**, audience share 9.11%) | ❌ | ⚠️ Checklist says yes; **not sourced live** | 🔴 **No UPI, no UPI Autopay**, USD-priced, and recurring card debits fall under the RBI e-mandate AFA regime |
| Taiwan | ✅ #6 (4.34%) | ❌ | ❌ No | 🟠 `zh-TW` explicitly routed to Antom; no JKOPay / LINE Pay / ATM transfer |
| Singapore | ✅ #7 (3.32%) | ❌ | ❌ No | 🟡 No PayNow |
| Japan | ✅ #8 (3.03%) | ❌ | ❌ No | 🟢 **Lowest risk** — a dedicated local-methods acquirer is already wired in. ⚠️ **except team/seat orders, which have no Japan branch** |
| Egypt | ✅ #9 (2.80%) | ❌ | ❌ No | 🔴 No Fawry; USD cards into a low-card-penetration market |
| Pakistan | ✅ #10 (2.19%) | ❌ | ❌ No | 🔴 No JazzCash / Easypaisa |
| Morocco | ✅ #11 (1.83%) | ❌ | ❌ No | 🔴 No local method |

> *"Warning: Potential cross-border operation in China, the United States, Brazil, Hong Kong and India. No local entity found for `lovart.ai` in any of them. Transactions are likely processed cross-border, with higher scheme costs, lower approval rates and FX exposure."*

> **The China wording has to be more precise than the standard warning, because the standard warning is wrong here.** This is **not** a company that cannot reach China's domestic rails. It is a group that **has** reached them — licensed, under a Shanghai entity with an ICP filing, with Alipay *and* WeChat Pay JSAPI and a proper auto-renew mandate — and then **wired them to the other product**, leaving `lovart.ai`'s 19.68% of traffic on a cross-border, USD-denominated, Alipay-only path with WeChat Pay switched off in code. **That is an architecture decision, not a licensing wall, which is exactly why it is reachable in a conversation.**

> **MANUAL:** Verify Resonate International INC on the Delaware Division of Corporations entity search (CAPTCHA-gated, needs a human) and 上海哩布哩布科技有限公司 on a Chinese registry. Both were attempted and blocked here.

---

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| **Global default** (every market with no special rule — US, Brazil, India, Egypt, Pakistan, Morocco, Singapore, and non-Chinese-language HK/TW) | **Stripe** — modelled as **two rails**, `Payway.STRIPE = 1` and `Payway.STRIPE_TWO = 2`; `STRIPE_TWO` is what the "card or other payment" button resolves to | `[Source Code]` | `https://web-static3.lovart.ai/lovart_prd/static/_next/static/chunks/2cfihdcovcy8y.js` |
| **Greater China + any Chinese-language or `Asia/Shanghai` visitor** (China, HK, TW, Chinese-language SG) | **Antom** (Ant International) — `Payway.ANTOM = 0`, `Payway.ANTOM_NEW = 3`; surfaced to the user as the **Alipay** button (`payway-option-alipay`, `#1677FF`, `commercial_aliPay` → 支付宝); the redirect return strips Antom's **`resultStatus`** parameter | `[Source Code]` | same chunk; i18n `commercial_aliPay` confirmed in the `xingliu.art` bundle |
| **China (consumer-facing, published)** | **Alipay accepted** — *"Starter 起 $15/月含商业授权。**支持支付宝**。"* | `[Terms/Published page]` | `https://www.lovart.ai/zh/topics/zh-pricing-cn` |
| **Japan** (`currency === "JPY"` **or** `lang === "ja"` **or** timezone contains `Asia/Tokyo`) | **Waffo** — `Payway.WAFFO = 4`. Waffo describes itself as *"The global payments and monetization platform for digital businesses"*, **480+ payment methods across 173 markets**, with a **Merchant-of-Record** option, and its own material names **konbini, PayPay and Pay-easy** for Japan | `[Source Code]` + `[Provider site]` | same chunk · `https://waffo.com/` |
| **China domestic (sibling product `xingliu.art`)** | **Alipay JSAPI** (`/api/www/pay/alipay/jsapi/info`) **and WeChat Pay JSAPI** (`/api/www/pay/wx/jsapi/info`), QR flow, **¥ pricing**, Alipay **periodic-deduction** auto-renew (*"次月按X元/月自动续费，可在支付宝内取消订阅"*) | `[Source Code]` | `https://xla-web-static.xingliu.art/xingliu_prd/static/_next/static/chunks/` |
| — | **Apple IAP / Google Play Billing** — `PaymentMethod.APPLE` and `PaymentMethod.GOOGLE` exist in the enum with **zero call sites**; no shipped app found in any storefront checked; no StoreKit / RevenueCat / restore-purchase code | `[Source Code]` + `[App-store listing search]` | See the app-store check in Section 8 |

**Infrastructure, as context for who you are talking to:** static assets are served from **Alibaba Cloud OSS** (`web-static3.lovart.ai` returns Alibaba OSS `NoSuchKey` XML with an `api.alibabacloud.com` troubleshooting link; the env config names `ossRegion: "oss-us-east-1"` for production and `oss-cn-beijing` for test), fronted by **Cloudflare** (`server: cloudflare`, Turnstile bot protection), with an **Alibaba Cloud WAF/SLB cookie** (`acw_tc`) set on the apex. The production API at `api.lovart.ai` returns **Chinese-language error strings** (`"服务异常"` / `"服务异常，请稍后重试"`) to unauthenticated callers, against a control path that returns a correctly-shaped English Spring Boot 404. **The CMS is Sanity** (the only CSP header is `frame-ancestors 'self' https://*.sanity.io …`). Model vendors in the changelog include **Google Nano Banana / Nano Banana Pro / Veo 3 / Gemini**, **GPT Image 2.0**, **Luma uni-1**, **Seedance 2.0** — and an **OpenClaw** integration exposing Lovart inside **Feishu**, Slack and Discord.

### 3B. Payment Orchestrator

**Classification: IN-HOUSE ORCHESTRATION LAYER.** Evidence type `[Source Code]`, from the merchant's own production bundle.

The full router, decoded:

```js
// js/2cfihdcovcy8y.js — module 524227
function checkIsCnTimezone(){ return Intl.DateTimeFormat().resolvedOptions().timeZone.includes("Asia/Shanghai") }
function checkIsCn(currency, lang){ return currency !== "JPY" && (["zh","zh-TW"].includes(lang) || checkIsCnTimezone()) }
function checkIsJp(currency, lang){ return currency === "JPY" || ["ja"].includes(lang)
                                    || Intl.DateTimeFormat().resolvedOptions().timeZone.includes("Asia/Tokyo") }
resolvePayway(currency, lang) = isCN ? Payway.CN_ALIPAY
                              : checkIsCn(currency, lang) ? Payway.ANTOM_NEW
                              : checkIsJp(currency, lang) ? Payway.WAFFO
                              : Payway.STRIPE
// js/1mx604a0-etun.js — module 82033:  t.s(["config",0,k,"isCN",0,!1],82033)
Payway        = { 0:"ANTOM", 1:"STRIPE", 2:"STRIPE_TWO", 3:"ANTOM_NEW", 4:"WAFFO", 5:"CN_ALIPAY" }
PaymentMethod = { ANTOM, STRIPE, ANTOM_NEW, WAFFO, APPLE, GOOGLE, CN_ALIPAY }
PaywayMap     = { 0:"ANTOM", 1:"STRIPE", 2:"STRIPE", 3:"ANTOM_NEW", 4:"WAFFO", 5:"CN_ALIPAY" }
```

> *"Confirmed orchestration-aware — they built the layer themselves. The opening is not the case for orchestration. It is the three things their own router cannot do: it cannot route on a BIN, it cannot route on performance, and it cannot fail a declined renewal over to a second acquirer."*

**What the router is, concretely:**
- **Three live acquirers**, selected by **browser language string and IANA timezone**. A Chinese cardholder travelling with an English browser and a European timezone gets **Stripe**; an English-speaking expat in Shanghai gets **Antom**. The signal is the device locale, not the instrument.
- **No BIN-level routing, no performance-based routing, no retry ladder, no cross-acquirer failover.** `dunning`, `gracePeriod`, `network token`, `accountUpdater`, `autoRenew`, `chargeback` all return **zero** across 4.1 MB. Every apparent `3ds` hit is `THREE_D_MODEL_GENERATION`; every apparent `declin` hit is an agent-UI reject button.
- **Renewals are pinned to the first-charge rail.** `lastPaymentMethod` is read back and the payway forced to match it (`r?.lastPaymentMethod === PaymentMethod.ANTOM_NEW ? Payway.ANTOM_NEW : …`). If that rail declines, there is no second attempt anywhere else.
- **Failure handling is one modal.** `commercial_paymentFailed`, with telemetry carrying `pay_way` and `error_code: u.status` — an **order status code, not a scheme decline code**. There is a `commercial.payment.timeout` event. There is no decline taxonomy to act on.
- **The CN path is dead code here and alive next door.** `isCN` is exported as `false`, so `CN_ALIPAY`, the `¥` symbol, the Chinese paywall component, the hard-coded Chinese paywall strings (`"本月积分已用完"`, `"领取迁移用户限时折扣，机不可失"`) and the Alipay QR modal all ship to every visitor and never execute.
- **Both of their non-Stripe vendors are themselves aggregation layers, scoped to one region each.** Antom publicly markets *payment routing* across 300+ methods and 200+ countries; Waffo markets 480+ methods across 173 markets plus Merchant of Record. **They have already bought the "one integration, many rails" idea twice — and confined each purchase to a single market.** That, not orchestration-as-a-concept, is the conversation.

> **MANUAL:** Walk the paid flow with DevTools from a UK/US locale, then with `--lang=zh-TW`, then with TZ=Asia/Tokyo, and capture the three different redirect hosts. That is a 10-minute demo of their own router's behaviour and the single most persuasive artefact available for this account.

---

## Section 4: Alternative & Local Payment Methods

Checked against `.claude/reference/apac-payments.md` §2 for every country above 1% traffic share. **Absence was established by grepping 4.1 MB of their own production JavaScript plus every page fetched, with the known false-positive traps checked in both directions** (`pix` → all `devicePixelRatio`/`subpixel`/`screen_width_pixels`; `upi` → all `classGroupId`/`grouping`/`occupied`; `omise` → `Promise`; `stripe` hits in the sibling bundle partly Mantine `stripes-animation` CSS). **Font Awesome is not bundled** on this site, so vendor greps here are not poisoned by `fab` icon definitions — but every hit was still read in context.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| **China** | **Alipay** (cross-border, Antom) | Digital wallet | **Active in checkout** | Payway modal + *"支持支付宝"* on their own zh page |
| **China** | **WeChat Pay** | Digital wallet | **Not found — explicitly disabled.** `isSupportWxpay` is `useMemo(()=>!1,[])`; the string `"请使用微信/支付宝扫码支付"` is therefore unreachable | `[Source Code]` |
| **China** | **UnionPay** | Cards | **Not found** — zero occurrences of `unionpay` / `银联` | `[Source Code]` |
| **China** | **CNY pricing** | — | **Not found on `lovart.ai`** — `¥` exists only behind `isCN`, which is `false`; the Chinese-language page quotes **$15** | `[Source Code]` + their own page |
| **China (sibling `xingliu.art`)** | Alipay JSAPI + **WeChat Pay JSAPI**, ¥ pricing, Alipay periodic-deduction mandate | Wallet / mandate | **Active** — but on the other product, under the other entity | `[Source Code]` |
| **Hong Kong** | FPS · Octopus · AlipayHK · WeChat Pay HK | A2A / wallet | **Not found** (Chinese-language HK visitors reach cross-border Alipay via Antom) | `[Source Code]` |
| **Taiwan** | JKOPay · LINE Pay · ATM / virtual-account transfer · convenience-store cash · domestic instalments | Wallet / transfer / cash | **Not found** (`zh-TW` is routed to Antom) | `[Source Code]` |
| **India** | **UPI** | A2A | **Not found** | `[Source Code]` |
| **India** | **UPI Autopay** | Mandate | **Not found** | `[Source Code]` |
| **India** | netbanking · RuPay · EMI / no-cost EMI | A2A / cards / instalments | **Not found** | `[Source Code]` |
| **Brazil** | **Pix** | A2A | **Not found** — and Pix was **54.7% of all Brazilian transactions** (42.9bn operations) in H2 2025 on Banco Central data, versus 30.4% for all cards combined | `[Source Code]` + [Band / Banco Central, 2026-04-08](https://www.band.com.br/economia/noticias/pix-lidera-pagamentos-no-brasil-com-547-das-transacoes-diz-banco-central-202604081055) |
| **Brazil** | **boleto** · **cartão parcelado** | Cash/voucher · instalments | **Not found** | `[Source Code]` |
| **Japan** | konbini · PayPay · Pay-easy | Cash / wallet | **Likely served via Waffo — not independently confirmed in Lovart's checkout.** Waffo's own material names these for Japan, and Lovart routes all JPY/`ja`/Tokyo traffic to Waffo. ⚠️ **Team/seat orders have no Japan branch and fall through to Stripe** | `[Source Code]` + `[Provider site]` |
| **Japan** | carrier billing · instalment / bonus payment | Carrier / instalments | **Not found** | `[Source Code]` |
| **Singapore** | PayNow · GrabPay | A2A / wallet | **Not found** | `[Source Code]` |
| **Egypt** | **Fawry** | Cash/voucher | **Not found** | `[Source Code]` |
| **Pakistan** | **JazzCash · Easypaisa** | Wallet | **Not found** | `[Source Code]` |
| **Morocco** | local cards / cash | Cards / cash | **Not found** | `[Source Code]` |
| **Global** | PayPal | Wallet | **Not found** — zero occurrences | `[Source Code]` |
| **Global** | Apple Pay · Google Pay | Wallet | **Not found as live methods** — enum members with zero call sites | `[Source Code]` |
| **Global** | BNPL / instalments | BNPL | **Not found** | `[Source Code]` |

> *"Warning: In Brazil, Pix is used for 54.7% of all transactions (Banco Central, H2 2025) but is not currently supported by Lovart — and Brazil is one of only two Lovart markets that grew over Jul–Sep 2026."*

> *"Warning: In China, Lovart's largest market at 19.68% of traffic, WeChat Pay is explicitly disabled in Lovart's own production code and UnionPay is absent entirely; the only Chinese wallet offered is Alipay, cross-border, against a US-dollar price."*

> ⚠️ **On China rail prominence specifically:** the best share figure located is **92% combined for Alipay + WeChat Pay, on CB Insights data for end-2017** (Digital Transactions, 2018-08-13) — **too stale to put in an email**, and no current PBOC figure was reachable. **Argue the absence, which is first-party and current, not the market share, which is not.**

> **MANUAL:** VPN into Shanghai, São Paulo and Mumbai and walk the paid flow for real. Confirming that a São Paulo visitor is offered no Pix, and a Shanghai visitor no WeChat Pay, converts the strongest two claims in this report from "read in their JavaScript" to "seen in their checkout".

---

## Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| **Charges continuing after cancellation** | Trustpilot | **High** — the dominant theme | 2025-11-08 → **2026-10-12** | [uk.trustpilot.com/review/www.lovart.ai](https://uk.trustpilot.com/review/www.lovart.ai) |
| **No self-service downgrade path** ("does not allow downgrading through its own website"; charged for a plan not chosen) | Trustpilot | Moderate | 2025-12-24 | same |
| **Slow / unanswered refunds** — one reviewer reports paying ~$192 with no credits consumed, no response for days, and **escalating the dispute to Alipay** | Trustpilot (via search summary) | Moderate | 2025-09 | same ⚠️ `[UNVERIFIED — search summary only, page not fetched]` for this specific review |
| **Credits consumed on failed or unusable output** | Trustpilot | Moderate | 2025–2026 | same |
| **Credits still deducted with "unlimited" enabled** | Trustpilot | Isolated | 2026 | same |
| Reddit / X / PissedConsumer | — | **Not found at volume** — one 1-star PissedConsumer entry surfaced; no Reddit thread found | — | — |

**Aggregate:** **TrustScore 1.5 / 5 across 80 reviews, 84% one-star** (fetched 2026-10-13).

> *"Pattern of post-cancellation charges and stalled refunds, running from Nov 2025 to the day before this report, maps directly onto what the code shows: subscription management is thin (the only subscription endpoints are `/member/subscribe/list` and `/member/subscribe/cancel`, with no downgrade path), refunds are a manual email process to `support@lovart.ai` governed by a 7-day/no-credits-consumed rule, and there is no decline-code handling anywhere in the client. This is payment-operations strain, not evidence of a routing failure — and that distinction matters, because the orchestration pitch here is approval rate and rail coverage, while the complaints are about the subscription-lifecycle surface. Use the complaints to establish that billing is an active internal pain, never as the headline."*

⚠️ **Never cite their Trustpilot score to them.** Trustpilot reviews are unverified individual accounts and evidence a complaint *pattern* only.
⚠️ **One complaint is a genuine finding in disguise:** a customer escalating to **Alipay** independently corroborates Alipay as a live pay-in rail — and tells you that when a Chinese-market dispute goes wrong, it goes to the wallet, not to Lovart.

---

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | **2026-06-18** | **Parent Evoken (formerly Qidian Xingyu Technology), Beijing, raises US$300M Series B+ at >US$2B valuation.** Jointly led by **Granite Asia**, **Tencent** and **Shunwei Capital**; existing investors **Ant Group** and **HSG** participated. Group ARR US$300M as of May 2026 | Funding | [Yicai Global](https://www.yicaiglobal.com/news/liblibai-parent-evoken-valued-at-over-usd2-billion-after-new-funding-round) |
| 2 | **2026-06-30** | **Top-up credits stop being perpetual** — credits bought on or after this date expire **366 days** from purchase; earlier purchases grandfathered. A deliberate change to the deferred-revenue model | Pricing / billing policy | [Subscribe FAQ](https://www.lovart.ai/statement/lovart-subscribe-faq) |
| 3 | **2026-07-09** | **Terms of Use re-issued** naming **Resonate International INC** (Delaware) as the offering entity, California law, San Francisco venue | Corporate / legal | [Terms of Use](https://www.lovart.ai/statement/terms-of-use) |
| 4 | **2026-05-06** (most recent entry) | **Changelog goes quiet.** Last shipped item is Luma uni-1; before it GPT Image 2.0 (2026-04-21), one-click custom fonts (2026-04-12), OpenClaw integration into Feishu/Slack/Discord (2026-04-09), Seedance 2.0 (2026-04-09), user-created Skills (2026-04-08). **Nothing published in five months** | Tech / product signal | [Changelog](https://www.lovart.ai/changelog) |
| 5 | **2025-07-28** | **Public launch out of beta**, ending an **800,000-person waitlist**; reached **~US$80M annualised revenue five months later**; **"more than 5 million users"** today | Market launch | [Newsroom](https://www.lovart.ai/news) · [36Kr](https://eu.36kr.com/en/p/3899540157236869) · [Google Cloud](https://cloud.google.com/customers/lovart) |

**No public payment-related RFP found.** **No payment-related job posting found** — `/careers` and `/jobs` both return 404 against a passing nonsense-path control, and nothing surfaced in search. **No payment licence application found** in any market.

**🛡️ Export-control / sanctions pre-check — negative, with a passing control.** Given the z.ai precedent in this repo and the Manus AI run's BIS screen, I checked the **US BIS Entity List corpus directly** rather than from memory, via the Federal Register API filtered to Bureau of Industry and Security documents:

- `"Lovart"` → **0** · `"Liblib"` → **0** · `"LibLib"` → **0** · `"Eanyo"` → **0** · `"Evoken"` → **0** · `"Resonate International"` → **0** · `"Xingliu"` → **0**
- **Control: `"Zhipu"` → count 1**, returning *Addition of Entities to and Revision of Entry on the Entity List*, published **2025-01-16** — the known listing. **The control passes, so the zeros are meaningful and not an artefact of a broken query.**

⚠️ **Scope limit, stated so nobody over-reads it: this covers BIS Federal Register documents only, and it searched the English-language names above — not the Chinese entity name 上海哩布哩布科技有限公司, not 言语智能 / Qidian Xingyu, and not any romanisation variant.** **OFAC SDN/Consolidated, DoD 1260H, the BIS Denied Persons List and eCFR Supplement No. 4 to 15 CFR Part 744 were NOT checked in this run.** 🛑 **THIS IS NOT A COMPLIANCE CLEARANCE. A partial screen is not a clearance.** Escalate to Yuno legal before any commercial commitment, and note two live facts that make this more than box-ticking: **Tencent and Ant Group are shareholders of the parent**, and the group's China operating entity holds a PRC ICP filing.

---

## Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | **2026-06-18** | Ant Group named as an **existing shareholder** in the parent's US$300M round | **The highest-relevance payment fact in the account.** Their China acquirer is Ant International's Antom. Treat the Antom relationship as sponsored and go around it, not at it | [Yicai Global](https://www.yicaiglobal.com/news/liblibai-parent-evoken-valued-at-over-usd2-billion-after-new-funding-round) |
| 2 | **2026-06-30** | Top-up credit expiry introduced (366 days) | They are actively re-engineering monetisation mechanics — a billing-roadmap signal | [Subscribe FAQ](https://www.lovart.ai/statement/lovart-subscribe-faq) |
| 3 | **Live now** (no announcement found) | **Xingliu → Lovart user migration is shipping in production**, with `xlToken` handoff, status polling and an `XlMigratedDiscount` promotion ("迁移专享价") | **Two billing stacks, one user base in motion. This is the re-platforming window** | `[Source Code]` `js/0julhcua7ovyd.js` |
| 4 | **2026-04-09** | OpenClaw integration puts Lovart inside **Feishu**, Slack and Discord | Distribution moving into chat surfaces — more entry points, same single checkout | [Changelog](https://www.lovart.ai/changelog) |
| 5 | — | **No PSP partnership, provider-removal, orchestration or payment-RFP announcement found anywhere** | The entire stack picture in this report is from code and published pages, not press. There is no public narrative to contradict — or to lean on | — |

**No provider removal found.** *"No public payment-related RFP found."*

---

## Section 8: Checkout Experience Audit

Partially accessible: the paywall and payway-selection components, the full router and the order API surface were read **from their own production bundle**, but the authenticated purchase flow itself was not walked (and `/api/www/member/packages` returns `{"code":0,"data":[]}` without a token — the endpoint is real, since a nonsense sibling path returns a correctly-shaped Spring Boot 404, but it is gated).

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | **Hosted redirect**, per acquirer. Order is minted server-side (`/api/www/lovart/teams/purchase`, `/api/www/member/purchase`) and the browser is sent to the acquirer; result polled via `/api/www/order/payResult` and `/api/www/lovart/member/queryTradeOrder` | Fair | No embedded card fields anywhere. No `js.stripe.com`, no Stripe Elements, no `client_secret` |
| Guest checkout | **No.** Account required — email, Google OAuth, or (CN build) phone + SMS or WeChat QR | Fair | Normal for a credits product |
| Steps to complete payment | Paywall → SKU select → **(Chinese-language users only) payway modal with exactly two options** → acquirer redirect → return with `resultStatus` → poll | Fair | **Only Chinese-language users see a method choice at all.** Everyone else is sent straight to one rail with no choice |
| Card input experience | **Redirect to acquirer-hosted page.** Card data never touches Lovart's DOM | Good | Keeps PCI scope minimal |
| Payment methods visible | **Two buttons, and only for the China path:** `commercial_aliPay` (支付宝 → Antom) and `commercial_cardOrOtherPayment` (→ `STRIPE_TWO`) | **Poor** | Two options in the world's most method-diverse market, and no choice at all in the other nine |
| Location-based method display | **Yes, but by the wrong signal.** Routing is on `navigator` language + `Intl` timezone, never on the instrument or the issuer | **Poor** | A Chinese cardholder on an English browser abroad gets Stripe; an English speaker in Shanghai gets Antom |
| Instalment / EMI options | **None found** in any market — no EMI (India), no 卡分期, no Japanese bonus payment, no BNPL | **Poor** | Pro and Ultimate annual plans are high-ticket for consumer AI |
| 3DS implementation | **Not detected in Lovart's own code** — every `3ds`/`three_d` hit is `THREE_D_MODEL_GENERATION`. 3DS is the acquirer's to handle on its hosted page | N/A | Consistent with full redirect |
| PCI indicator | Acquirer-hosted pages only; no self-hosted card fields | Good | See Section 9 |
| Mobile responsiveness | Responsive marketing and paywall; **mobile web is the only mobile channel** — "tasks can run simultaneously on up to 2 desktop Web, 1 mobile Web" | Fair | No native app exists |
| Multi-currency / local pricing | **USD everywhere except Japan.** The client's only currency-specific logic is `"JPY"`; `"USD"` is the hard-coded fallback (`currencyPrice?.description?.currency \|\| "USD"`) and `¥` appears only behind the dead `isCN` flag. **No BRL, INR, HKD, TWD, SGD, EGP, PKR, MAD anywhere in 4.1 MB.** Their own Chinese-language page quotes **$15** | **Poor** | Seven of the top eleven markets are billed in a foreign currency. ⚠️ The SKU's currency is server-supplied, so this is strong evidence, not proof, that only USD/JPY/CNY exist |
| Saved payment methods | **`lastPaymentMethod` is persisted and the renewal is forced onto that same rail** | **Poor** | No failover. A declined renewal has nowhere to go |
| Error message clarity | One generic `commercial_paymentFailed` modal; telemetry carries `pay_way` and an **order status code**, not a scheme decline code; a separate `commercial.payment.timeout` event exists | **Poor** | **Nothing in the client can distinguish "insufficient funds" from "issuer blocked a foreign transaction" — so nothing can react to it** |

**⭐ App-store billing channel — checked explicitly, because this check can invalidate the account (`subscription-payments.md` §4):**
- **Apple:** iTunes Search API, `term=lovart`, `entity=software`, storefronts **us / cn / sg / jp / hk / br**. **No Lovart-published app in any of them.** The only "Lovart"-named results are third-party apps under other sellers' bundleIds — `com.ConvertEase19head.app` (Ignite Classes LLC), `com.teoili.genart` (Teodora Ilie), `com.yzsm.lovartapp` (Shenzhen Yunzhuo Digital Technology Co., Ltd.). **No `hasInAppPurchases` flag is attributed to Lovart, because Lovart has no bundleId to attribute one to.** Direct `lookup?bundleId=` on five plausible IDs → `resultCount: 0`. Controls passed (`canva` returns results in **cn**; Gemini/Grok return in the others). **tw and in returned HTTP 403 and were not checked.**
- **Google Play:** five candidate package IDs → **404**, against a passing control (`com.canva.editor` → 200). A Play **search** for "lovart" returns 20 apps, **none Lovart-published** (the closest is `com.pkm.media.cfish`, labelled "Lovart AI App Advisor" — a third party).
- **In code:** `PaymentMethod.APPLE` and `PaymentMethod.GOOGLE` have **zero call sites**; `restorePurchase`, `storekit`, `revenuecat`, `in-app`, `appstore`, `playstore` all return **zero** (the five `iap` hits are `ariaPlaceholder`, `ariaPosInSet`, `ariaPressed`, `sendEventsViaPost`).
- **Conclusion: the app-store override does not apply. Billing is web-only, so essentially all of this revenue is orchestratable** — the opposite of the EMEA `not-icp` failure mode. ⚠️ Their Terms §6.2–6.3 *do* describe purchasing and cancelling "through your Apple ID, Google account or other account" — that is forward-looking boilerplate for an app they have not shipped, and it is the one thing that could change this verdict later.

**Billing mechanics, from their own FAQ (useful for the call, and all merchant-published):** Free + **Starter 2,000 / Basic 3,500 / Pro 11,000 / Ultimate 27,000** monthly credits; monthly and annual cycles plus a Chinese "连续包月" continuous-monthly SKU; **annual plans release credits monthly and do not roll over**; **top-up credits expire 366 days from purchase** (new as of 2026-06-30); an "Off-Peak Image Pack" that is **final and non-refundable**; time-of-day credit multipliers (0.5× at 07:00–12:00 PDT, 1.4× at 00:00–02:00 PDT); **refunds only within 7 days and only if no credits were consumed**, by email, *"issued using the same payment method you used to make the purchase"*, replied to within 24 business hours and paid within 10 business days; upgrades by paying the price difference, with the explicit carve-out that **if you want to change payment method you must buy the new plan first and email support to reconcile the old one**. SKU internals: `packageLevel` 30 = Starter, 2 = Basic, 3 = Pro, 50 = Ultimate; prices held in **minor units** (`/100`); `firstMonthPrice` supports first-period promo pricing. **Team plan** is seat-based with invitations, seat caps, `purchasePower` top-ups, **invoice generation** (`/api/www/lovart/invoice/createAndGetUrl`) and a sales **contact form** — so there is a B2B motion alongside the consumer one.

---

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **No public PCI documentation found for Lovart.** | — |
| Card data handling | **Acquirer-hosted redirect for every rail.** No card fields, no PSP JS SDK, no `client_secret` anywhere in 4.1 MB. The Privacy Policy states: *"we use third-party payment processors to handle your payment transactions… We do not store your full payment card details, but we may retain transaction confirmation or records required for compliance and accounting purposes."* **Note the plural — "processors" — which the code confirms.** | [Privacy Policy](https://www.lovart.ai/statement/privacy-policy) + `[Source Code]` |
| Recommended Yuno integration | **SDK / hosted-fields**, to preserve the current minimal scope. A back-to-back API integration would expand their PCI footprint and is not the right opening. | — |

> `[INFERENCE, not confirmed]`: Based on confirmed full-redirect checkout with no card fields in their own DOM, Lovart's PCI scope is likely **SAQ A**, with each acquirer handling card data. **No compliance level is stated anywhere publicly and none is asserted here.**

---

## Section 10: Strategic Insights & Outreach Angles

> **Insight #1: Their largest market is billed cross-border, in dollars, on one wallet — while their own group runs licensed domestic rails for it next door.**
> **Evidence:** **S1** — China is #1 at 19.68% of traffic (SimilarWeb supplied 2026-10-13). **S3/S4** — on `lovart.ai`, Chinese-language visitors are routed to **Antom** cross-border; **WeChat Pay is `isSupportWxpay → !1`**, hard-coded off; **UnionPay has zero occurrences**; the only Chinese price they publish is **`$15/月`** (`https://www.lovart.ai/zh/topics/zh-pricing-cn`). **S2** — the group's domestic Alipay **and** WeChat Pay JSAPI rails, ¥ pricing and Alipay periodic-deduction mandate are live on **`xingliu.art`** under **上海哩布哩布科技有限公司 (沪ICP备2025147903号-6)**.
> **Pain Point:** One fifth of their traffic hits a checkout with two buttons, a foreign-currency price their customer's bank will convert and surcharge, and the country's second wallet switched off in code. Every Chinese user who prefers WeChat Pay, holds a UnionPay card, or balks at a dollar charge is a conversion they never see — and the fix exists inside their own company but is wired to a different product with a different entity and a migration flow in between.
> **Yuno Value Proposition:** One integration that presents the full local method set per market and routes on the instrument rather than the browser locale — so a Chinese-language user abroad and an English-language user in Shanghai are each routed on what they are actually paying with. Local currency presentment stops the issuer-side FX surprise that drives both abandonment and chargebacks.
> **Best Success Case:** See Success Case Alternatives — a global subscription-plus-credits merchant already running more than one acquirer, where locale-based routing was replaced with instrument- and performance-based routing. **No Yuno case is named until the published reference is confirmed.**
> **Outreach Angle:** Their Chinese-language pricing page offers Alipay against a dollar price, and the 支付宝/卡 choice is the only method choice anywhere in the product — worth asking what share of Chinese attempts never reach a second try.
> **Suggested Subject Line:** Two buttons for 19.68% of your traffic

> **Insight #2: They already built the routing layer. It routes on timezone.**
> **Evidence:** **S3B** — `resolvePayway(currency, lang)` selects Antom / Waffo / Stripe from `["zh","zh-TW"].includes(lang)`, `lang === "ja"` and `Intl.DateTimeFormat().resolvedOptions().timeZone.includes("Asia/Shanghai" | "Asia/Tokyo")`, decompiled from `js/2cfihdcovcy8y.js`. **S8** — `lastPaymentMethod` pins the renewal to the first-charge rail; `dunning`, `gracePeriod`, `network token`, `accountUpdater` are all **zero**; the only failure signal is an order status code in a generic modal.
> **Pain Point:** They own three acquiring relationships and cannot use them as alternatives to each other. A renewal that declines on Antom cannot retry on Stripe. A Japanese card that would approve domestically through Waffo goes to Stripe if it arrives from a team-seat order, because the team path has no Japan branch at all. The routing signal — device locale — is the one input that tells you least about whether a payment will approve.
> **Yuno Value Proposition:** Keep every acquirer they have; replace the `if/else` with routing on BIN, issuer geography and live acquirer performance, plus cross-acquirer failover and decline-code-aware retries on renewals, and network tokens / account updater once rather than per provider.
> **Best Success Case:** Same profile as #1 — the point of the reference is multi-acquirer *already in place*, badly used.
> **Outreach Angle:** Their own paywall picks the acquirer from the browser's timezone string — which means a card issued in Shanghai and presented from Singapore is treated as a Singapore card.
> **Suggested Subject Line:** Your payway router reads `Intl.DateTimeFormat()`

> **Insight #3: Brazil is one of only two markets still growing, and it has no Pix.**
> **Evidence:** **S1** — Brazil #3 at 6.58%, **↑5.99%**, 5.60 pages/visit, 32.08% bounce. **S4** — **zero** genuine `pix` occurrences across 4.1 MB of their JS and every page fetched (all 50 hits are `devicePixelRatio`, `subpixel-antialiased`, `screen_width_pixels`), **no boleto**, **no cartão parcelado**, and Brazilian visitors fall through `resolvePayway` to **Stripe in USD**. Against that: **Pix was 54.7% of all Brazilian transactions in H2 2025 — 42.9bn operations versus 30.4% for all cards combined** (Banco Central data, 2026-04-08).
> **Pain Point:** Their third-largest and fastest-growing market is served card-only in a foreign currency, in a country where the majority rail is instant account-to-account and where instalments are how consumers buy anything above an impulse price. Growing demand into the narrowest possible acceptance is the most expensive version of this problem.
> **Yuno Value Proposition:** Pix and boleto as part of the same integration, with BRL presentment and local acquiring for the card share, and `cartão parcelado` for the Pro and Ultimate annual tiers.
> **Best Success Case:** The second-best shape in Success Case Alternatives — a merchant whose Brazilian revenue was card-only and who added Pix. **Name only a confirmed published reference.**
> **Outreach Angle:** Brazil is one of only two markets where their engagement is rising, and it is the market where the acceptance gap is widest and most quantifiable.
> **Suggested Subject Line:** Brazil is growing for you — in dollars, without Pix

> **Insight #4: Prateek's home market is their highest-intent audience and their least-served checkout.**
> **Evidence:** **S1** — India #5 at 5.66% traffic but **9.11% audience share** (1.6×, i.e. many distinct users), **↑10.72%**, **00:08:41** average session, **8.59 pages/visit**. **S4** — **no UPI, no UPI Autopay, no netbanking, no RuPay, no EMI**, USD-priced. **S8** — subscriptions auto-renew on a card-on-file with no decline-code handling and no retry ladder, against the **RBI e-mandate framework** (RBI/2022-23/73, 16 June 2022, fetched live): AFA required on the first e-mandate transaction on cards/PPIs/UPI, waived for subsequent transactions **only up to ₹15,000**.
> **Pain Point:** A growing base of deeply-engaged Indian users is offered one instrument — a foreign-currency card charge — in a market where account-to-account is the default. And the renewal mechanics are the hard part: `[INFERENCE]` the annual tiers, and the top monthly tier, convert to amounts at or above the ₹15,000 AFA-exempt ceiling at any plausible exchange rate, so those debits require authentication every time. "Store the card and retry monthly" does not survive contact with this regime, and there is no retry logic in their client at all.
> **Yuno Value Proposition:** UPI for the one-off purchase, **UPI Autopay** as the local recurring rail, e-mandate-compliant card recurring with pre-debit notification and AFA handling where required, INR presentment, and no-cost EMI for the annual tiers.
> **Best Success Case:** A global subscription merchant that added India recurring under the e-mandate regime. **Name only a confirmed published reference.**
> **Outreach Angle:** India is their second-fastest-growing market and the one where users go deepest (8.6 pages a session) — and the only way to pay is a dollar card charge.
> **Suggested Subject Line:** 8.6 pages a session in India, one way to pay

> **Insight #5: The design incumbent they are attacking already did the local-acquiring work — publicly.**
> **Evidence:** **S11** — **Canva**, the APAC-HQ'd design incumbent and Lovart's most direct large competitor, *"partnered with Stripe to implement domestic acquiring to support local cards and local mobile wallets"* in **South Korea** and *"since going live in 2024… increased their payment reach by over 9.5 million users"*, running Authorization Boost (network tokens + account updater) and Adaptive Acceptance, which *"helped increase Canva's payment success rates by 2.1% and saved over 1.5% in network costs"* across its *"top 40 markets"* (Stripe's own customer story). **S3B** — Lovart serves **118 countries** with locale-based routing across three acquirers, no network tokens, no account updater and no retry logic. **S6** — and they have **US$300M of fresh capital** and ARR growing at the group level.
> **Pain Point:** The incumbent treats payment reach as a growth channel with published numbers against it. Lovart treats it as an `if/else`. At 118 countries and 5 million users, the gap between those two postures is a revenue line, and it widens every month the changelog stays quiet.
> **Yuno Value Proposition:** The same mechanisms — local acquiring, network tokens, account updater, intelligent retries — delivered across *all* their acquirers at once rather than one PSP's estate, which is the only version that works for a stack that is already three-vendor.
> **Best Success Case:** Same profile as #1.
> **Outreach Angle:** The category incumbent published what domestic acquiring in one Asian market was worth to them in users; Lovart runs 118 countries on three acquirers chosen by browser timezone.
> **Suggested Subject Line:** What Canva published about one market's rails

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. Your Chinese-language pricing page quotes **$15/month** and offers 支付宝 — so your largest market, at nearly a fifth of your traffic, is paying a dollar price on a single wallet.
2. Your paywall picks which acquirer to use from the browser's language and `Intl` timezone, which means a card issued in Shanghai and presented from Singapore gets routed as a Singapore card.
3. Brazil is one of only two markets where your engagement is **up** — and it is the one market where the dominant rail carried **54.7% of all national transactions** last half and does not appear in your checkout at all.

**Cold call openers (conversational, one sentence each):**
1. "I read your paywall code before I called — you've got three acquirers wired up and the choice between them is made off the browser's timezone. I wanted to ask what happens when the first one declines."
2. "You've got an 8-and-a-half minute average session in India and about one and a half times the distinct-user share you'd expect from the traffic — and the only way those users can pay you is a dollar card charge. Is that a decision or just where the roadmap landed?"
3. "Your own Chinese site says Alipay is supported, and your code has WeChat Pay switched off with a hard-coded false. I'm curious whether that was a conscious call or something nobody's had time to revisit."

---

## Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| **星流 / Xingliu Agent** | xingliu.art | China (Shanghai) | Sibling product, same group | China | **China-domestic Alipay + WeChat Pay JSAPI, ANTOM-default + Stripe fallback, `Payway.WPS=11` (unidentified)** | `[Source Code]`, this run |
| **Canva** | canva.com | Australia | ~$3–4B ARR (internal TAL, not re-verified) | Global incl. all APAC | **Stripe, with domestic acquiring + local wallets in Korea, Authorization Boost, Adaptive Acceptance** | [Stripe customer story](https://stripe.com/gb/customers/canva) |
| **Freepik** | freepik.com | Spain | Not found | Global | **Not found** — the only result was an unrelated no-code automation template | TAL row exists, PSP column empty |
| **Kling AI** (Kuaishou) | kling.ai | Singapore / China | ~$500M ARR (Mar 2026) | Global incl. India #1 | **Stripe (web), PayPal, Apple/Google Pay — "None detected, greenfield", ICP 23/29** | ⚠️ `accounts/apac-tal.csv`, not re-verified |
| **MiniMax** (稀宇科技) | minimax.io | China | $116.6M (H1 2026) | Global | **Stripe primary + Airwallex — in-house (build-flag routing)** | ⚠️ `accounts/apac-tal.csv`, not re-verified |
| **Vidu** (生数科技) | vidu.com | China | Not found | Global | **Not found** | TAL row exists, PSP column empty |
| **Picsart** | picsart.com | United States | Not found | Global | **Not found** | Searched, nothing relevant |
| **Recraft / Ideogram / Krea / Gamma** | — | US / global | Not found | Global | **Not found** | Not researched beyond name-level |

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| **Manus AI** | manus.im | AI agent, subscription + credits | Brazil, US, India, Japan | **The closest structural twin in this repo**: China-origin, global fragmented traffic, subscription + credits — but **single-PSP Stripe, greenfield, ICP 23/29, and app-store channels live**. Lovart is the *more mature stack with the weaker routing* | `2-ready-to-outreach/manus-ai.md` |
| **Moonshot AI (Kimi)** | moonshot.ai | LLM assistant, subscription | Global | **In-house `growth.pay.v1.PayService`, 7 channels, own dunning counter — ICP 22/29.** The nearest precedent for an in-house-layer sale in this repo | ⚠️ `accounts/apac-tal.csv`, not re-verified |
| **z.ai (Zhipu AI)** | z.ai | LLM, subscription | Global | In-house, 2 rails (Stripe + PayPal), ICP 23/29 — 🛑 **BIS Entity List compliance hold** | ⚠️ `accounts/apac-tal.csv`, not re-verified |
| **Kuaishou (Kwai)** | kuaishou.com | Short video + AI creative | China, Brazil, SEA | **Five acquirers in parallel (dLocal, EBANX, Liquido, PayerMax, Checkout.com), in-house routing CONFIRMED, ICP 17/29.** The best "a China-origin creative platform at scale ends up with five acquirers and a router" comparison | ⚠️ `accounts/apac-tal.csv`, not re-verified |
| **InVideo AI** | invideo.io | AI video, subscription | India-HQ, global | $30–70M est.; India-HQ AI creative tool, same prosumer subscription shape | TAL row |
| **Murf AI** | murf.ai | AI voice, subscription | India-HQ, global | ~$30M est.; same shape | TAL row |

#### 11C. Companies Recently Adopting Payment Orchestration

> *"No public case studies found of direct competitors adopting a third-party payment orchestration platform."*

What **was** found, and why it does not satisfy the +2 row:

| Company | What they actually did | Date | Vertical | Source URL |
|---------|----------------------|------|----------|------------|
| **Canva** | **Domestic acquiring + local mobile wallets in South Korea, on Stripe**, plus network tokens / account updater / AI retries — *not* a third-party orchestrator | Live since **2024** | Design SaaS | [stripe.com/gb/customers/canva](https://stripe.com/gb/customers/canva) |
| **Kuaishou / Kling** | **In-house routing across five acquirers** — built, not bought | Per internal note, researched 2026-09-29 | Short video / AI creative | ⚠️ `accounts/apac-tal.csv`, not re-verified |
| **Moonshot AI, MiniMax, z.ai** | **In-house layers** — built, not bought | 2026 | AI assistants | ⚠️ `accounts/apac-tal.csv`, not re-verified |

**The honest read, and it is itself a selling point:** every comparable company in this vertical that outgrew one PSP **built its own router**, exactly as Lovart did. Nobody in the set bought orchestration. So the competitive-urgency argument is *not* "your rivals adopted an orchestrator" — it is **"everyone in your category hand-rolls this, and the one that invested in real rails instead published what it was worth in users."** That is a stronger and more defensible line than the matrix row would have been.

#### 11D. Prospect Scoring

Applied to the peers above, **verified signals only**. Most rows are ⬜ because these companies were not researched in this run; TAL-sourced scores are carried with their provenance and **not** re-verified.

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| **星流 / Xingliu — monthly transaction count** | ⬜ | Uncertain — no revenue split published for the China product | — |
| **星流 / Xingliu — orchestration status** | **+1** | ✅ In-house: ANTOM-default + Stripe fallback + `WPS` channel, same shared codebase | `[Source Code]`, this run |
| **星流 / Xingliu — local rail gap** | **0** | ❌ **Not met — and that is the point.** Alipay *and* WeChat Pay JSAPI, ¥ pricing, Alipay mandate. **China-domestic rails are already correct here** | `[Source Code]`, this run |
| **星流 / Xingliu — 3+ countries** | **0** | ❌ Not met — China-only property | `[Source Code]`, this run |
| **星流 / Xingliu — funding >$10M** | **+2** | ✅ Same parent round, 2026-06-18 | Yicai Global |
| **Canva — multiple PSPs** | ⬜ | Uncertain — only Stripe evidenced | Stripe case study |
| **Canva — 3+ countries** | **+3** | ✅ "top 40 markets" | Stripe case study |
| **Canva — local rail gap** | **0** | ❌ Not met — they closed theirs in 2024 | Stripe case study |
| **Freepik / Vidu / Picsart / Recraft / Ideogram / Krea / Gamma** | ⬜ | **Uncertain across every row** — not researched | — |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | **Lovart** | Subject | China, US, Brazil, HK, India | **21/29** | ⭐ | In-house locale-based router across 3 acquirers; China in USD on one wallet; **web-only billing** | ❌ **NO — genuine new find** |
| 2 | **星流 / Xingliu (LiblibAI)** | Sibling product, same group | China | ⬜ insufficient | 🟢 **Investigate as one group account, not two** | China-domestic Alipay + WeChat Pay already correct; `WPS` channel unidentified; **same parent, same round, same codebase** | ❌ **NO — genuine new find** |
| 3 | **Evoken / LiblibAI (parent)** | Parent group | China + global | ⬜ insufficient | 🟢 | **US$300M at >US$2B, Jun 2026; group ARR US$300M; three product lines on one shared payment codebase.** The real buying centre may be here, not at Lovart | ❌ **NO — genuine new find** |
| 4 | **Picsart** | Direct competitor | US, global | ⬜ | 🟢 | Large consumer creative subscription; stack unknown | ❌ NO |
| 5 | **Freepik** | Direct competitor | Global | ⬜ | 🟢 | Stack unknown; TAL row exists but PSP column empty | ✅ yes (unresearched) |
| 6 | **Vidu (生数科技)** | Direct competitor | China, global | ⬜ | 🟢 | China-origin AI creative; stack unknown | ✅ yes (unresearched) |
| 7 | **Recraft** | Direct competitor | Global | ⬜ | 🟢 | AI design tool, subscription + credits | ❌ NO |
| 8 | **Ideogram** | Direct competitor | Global | ⬜ | 🟢 | AI image, subscription + credits | ❌ NO |
| 9 | **Krea** | Direct competitor | Global | ⬜ | 🟢 | AI creative, subscription + credits | ❌ NO |
| 10 | **Gamma** | Adjacent (AI decks) | Global | ⬜ | 🟢 | Same prosumer subscription + credits shape | ❌ NO |

> ### ⭐ Section 11 call-out — genuine new finds
> **I confirmed Prateek's check: `accounts/apac-tal.csv` (1,219 rows) contains no row for Lovart, Liblib, Xingliu or Evoken** — `grep -i -c "lovart\|liblib"` returns **0** against a passing control (`canva` → 1). **Lovart at 21/29 ⭐ is a genuine new find and should be added to the TAL.**
> **Three further genuine finds flow from it, and the third may matter more than the first:** **星流 / Xingliu** (the China-domestic sibling, same codebase, correct China rails, `WPS` channel unexplained), and **Evoken / LiblibAI**, the **parent**, which holds the US$300M round, US$300M group ARR and **three products — LiblibAI, Lovart/Xingliu and LibTV — demonstrably sharing one payment codebase.** If the payment decision is made at group level, the account is Evoken and Lovart is the wedge. **Also absent from the TAL:** Manus AI, Picsart, Recraft, Ideogram, Krea, Gamma, Figma, Adobe, Leonardo, PhotoRoom.

---

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | **~US$80M annualised for Lovart**, reached ~5 months after the 2025-07-28 launch (so roughly Dec 2025). Group (Evoken) **ARR US$300M as of May 2026** | [36Kr](https://eu.36kr.com/en/p/3899540157236869) · [Dealroom](https://dealroom.co/news/142733-liblib-ai-hits-2b-valuation-with-300m-series-b-extension-as-arr-reaches/) · [Yicai Global](https://www.yicaiglobal.com/news/liblibai-parent-evoken-valued-at-over-usd2-billion-after-new-funding-round) |
| GMV / Gross Transaction Volume | **Not found.** For a first-party subscription business, revenue ≈ processed volume | — |
| Average Transaction Value (USD) | **Not found.** Sourced anchor: **Starter from US$15/month** (merchant's own zh pricing page). Third-party and conflicting: Starter $19 / Basic $32 / Pro $90 / Ultimate $199 monthly `[ESTIMATE, not confirmed]` | lovart.ai/zh/topics/zh-pricing-cn · third-party guide 2026-09-24 |
| Est. Annual Transactions | **~1.2M–5.3M charge events/year**, from US$80M ÷ an average charge of $15–$67 | Calculated — **and an assumption, because ATV is unsourced** |
| **Monthly transaction count** | **⚠️ NOT FOUND — ASSUMED ≥100,000/month. `[ASSUMPTION — not researched.]` Billing unit = one charge event: a monthly or annual subscription period, a credit top-up, an Off-Peak Image Pack, or a seat purchase.** US$80M ÷ 12 = ~US$6.67M/month; at a $15 average charge → ~444,000, at $90 → ~74,000, at $199 → ~33,500. **The under-40,000 rejection would need an average charge above ~US$167 and is not arithmetically reachable.** See the full disclosure block in the ICP breakdown | **ASSUMED** — one sourced input (revenue), one unsourced (ATV) |
| Active Customers / Users | **"more than 5 million users around the world"** — registered, not paying | [Google Cloud customer page](https://cloud.google.com/customers/lovart) |
| Primary Currency | **USD.** The client's only currency-specific branch is `"JPY"`; `"USD"` is the hard-coded fallback; `¥` exists only behind the dead `isCN` flag. **No BRL, INR, HKD, TWD, SGD, EGP, PKR or MAD anywhere in 4.1 MB** | `[Source Code]` |
| Top 3 Markets by Revenue | **Not found.** By *traffic*: China 19.68%, US 13.20%, Brazil 6.58%. **Do not present traffic share as revenue share** — USD-only pricing in low-card-penetration markets means revenue is almost certainly skewed harder toward the US than traffic is | SimilarWeb (supplied 2026-10-13) |
| Billing channel split (web vs app store) | **⭐ Effectively 100% web.** No Lovart-published app in the US, CN, SG, JP, HK or BR App Store (controls passing) and none on Google Play; `PaymentMethod.APPLE`/`GOOGLE` have zero call sites; no IAP SDK of any kind. **tw and in App Store storefronts returned HTTP 403 and were not checked** | `[App-store listing search]` + `[Source Code]` |
| Deferred-revenue note | Annual plans bill once per 12 months while releasing credits monthly; **top-up credits bought on/after 2026-06-30 expire after 366 days**. Both facts move charge frequency and recognised revenue in opposite directions and should be asked about on the call | [Subscribe FAQ](https://www.lovart.ai/statement/lovart-subscribe-faq) |

---

### Overall Research Confidence

**High** — with two named exceptions.

**Very strong coverage.** The payment stack (S3), the full routing logic (S3B), the rail gaps (S4), the currency and billing-unit picture (S8/S12), the China answer, the corporate relationship to LiblibAI, the China operating entity and its ICP filing, the billing entity and governing law, and the app-store question all rest on **first-party evidence**: the merchant's own Terms and Privacy Policy, their own Subscribe FAQ, their own published Chinese pricing page, **4.1 MB of their own production JavaScript across all 58 chunks**, **7.8 MB of the sibling product's bundle**, their own API responses, and App Store / Google Play listing data. Almost nothing load-bearing depends on a press release or a search synthesis. Every route finding was checked against a deliberate nonsense control (`/zzz-control-not-real-7742`, which 404s within ~20 bytes of the other soft-404s and distinguishes real pages from the SPA shell); the app-store zeros carry passing positive controls in both stores; the BIS screen carries a passing positive control; and every known false-positive token (`pix`, `upi`, `omise`, `stripe`, `3ds`, `declin`, `iap`) was read in context in both directions rather than counted.

**Traffic data was supplied, not estimated** — SimilarWeb, pasted by Prateek 2026-10-13, used verbatim, Jul–Sep 2026, single domain, 118 countries. The country profile that drives the APM analysis and two ICP rows is therefore as good as this repo gets. **No absolute visit count exists in the extract and none is asserted.**

**Exception 1 — the transaction count is an assumption, and it carries the tier.** One sourced input, one unsourced. Strike it and 21/29 ⭐ becomes 16/29 🟢. Every other awarded row is verified.
**Exception 2 — no entity is registry-confirmed.** Delaware (CAPTCHA), ACRA BizFile+ (client-rendered SPA, returned nothing in HTML), OpenCorporates (token required), `beian.miit.gov.cn` (unreachable), `tianyancha.com` (HTTP 419), `qcc.com` (login wall). The entity names and the ICP number come from the companies' own published text, which is good evidence but not a registry.

**Smaller limits, stated plainly:** the authenticated purchase flow was never walked, so the two payway buttons are what their code renders rather than what a logged-in buyer sees; the SKU catalogue API is token-gated, so tier prices above the merchant's own $15 Starter figure are third-party and conflicting; the China rail-prominence statistic is eight years old; `Payway.WPS=11` is unidentified; and `lovart.cn` could not be reached because of a proxy failure, so nothing is concluded about it.

---

### Manual Research Recommendations

> **Area:** **Monthly charge count and the monthly-vs-annual plan mix.** (S12, and the +5 ICP row)
> **Why it matters:** It is the only unsourced row in the score and it is the row that makes this ⭐ rather than 🟢. It is also the business-case denominator — and annual plans bill 1/12th as often as monthly ones, so the mix changes the number by an order of magnitude.
> **Suggested manual action:** Ask on the first call: monthly charge events, the monthly/annual split, and what share of revenue is credit top-ups versus subscriptions. Their Trustpilot replies show an active `support@lovart.ai`; the Team-plan sales contact form is another route in.

> **Area:** **Walk the checkout from three locales, with DevTools open.** (S4, S8)
> **Why it matters:** The two strongest claims in this report — no Pix for Brazil, no WeChat Pay for China — are read out of their JavaScript. Seeing them in a live checkout converts them from analysis into an artefact you can put in front of a buyer. It also settles whether additional methods are enabled server-side on the Antom or Stripe hosted page, which cannot be seen from outside.
> **Suggested manual action:** VPN to Shanghai, São Paulo and Mumbai; also run `--lang=zh-TW` and `TZ=Asia/Tokyo` from one location to demonstrate that the router responds to locale rather than to geography. Capture the three redirect hosts.

> **Area:** **Who owns the payment decision — Lovart, or Evoken/LiblibAI at group level.** (S2, S11)
> **Why it matters:** Three products share one payment codebase, one parent holds the US$300M round, and the China rails sit under a Shanghai entity while Lovart contracts from Delaware. Pitching the Lovart product team when the decision sits with a group platform team would waste the cycle — and the group account is a bigger prize than the product.
> **Suggested manual action:** Map the engineering and finance org on LinkedIn across Lovart, LiblibAI and Evoken; look specifically for a shared payments or growth-infrastructure team. Then decide whether the wedge is Lovart or the parent.

> **Area:** **The Ant Group / Antom relationship.** (S6, S7)
> **Why it matters:** Ant Group is an existing shareholder of the parent and Antom is the China acquirer. If that is a sponsored relationship, the China rails may be commercially untouchable — in which case the entire pitch has to be built on the **eight non-China, non-Japan markets** in the top eleven, which is still a strong account but a different conversation.
> **Suggested manual action:** Ask directly and early how the Antom relationship came about, before building a China-led sequence. Keep the Brazil/India/Egypt/Pakistan/Morocco gap as the primary angle until you know.

> **Area:** **Compliance screening beyond BIS, and under the Chinese entity names.** (S6)
> **Why it matters:** The z.ai precedent in this repo shows how late a compliance blocker can surface. The screen here is **BIS Federal Register only** and only under English names — OFAC, DoD 1260H, the Denied Persons List and eCFR Supp. No. 4 were not checked, and 上海哩布哩布科技有限公司 / Qidian Xingyu were not screened at all. **Tencent and Ant Group are shareholders.**
> **Suggested manual action:** Route to Yuno legal for a full screen under both the English and Chinese entity names before any commercial commitment. **State internally that a partial screen is not a clearance.**

> **Area:** **Registry confirmation of Resonate International INC and the Shanghai entity.** (S2)
> **Why it matters:** The billing entity decides the acquiring path, the contracting party and — awkwardly — possibly the territory assignment. A Delaware Inc. with California law could put AMER's hand up.
> **Suggested manual action:** Run the Delaware Division of Corporations entity search by hand (CAPTCHA-gated) and 上海哩布哩布科技有限公司 on a Chinese registry. Then confirm internally that a China-HQ'd group billing from Delaware is Prateek's account.

> **Area:** **Tier prices above Starter, and whether any market gets local pricing.** (S12)
> **Why it matters:** The business case needs an ATV. Only the $15 Starter is merchant-sourced; everything above it is third-party and conflicting, and the SKU API is token-gated.
> **Suggested manual action:** Create a free account and read the paywall from a logged-in session in two locales. That also reveals whether the server ever returns a currency other than USD, JPY or CNY — which is the one thing the client code cannot settle.

---

### Appendix: All Source URLs

**Merchant's own properties (first-party)**
- `https://lovart.ai/` → 301 → `https://www.lovart.ai/`
- `https://www.lovart.ai/pricing` · `/zh/pricing` · `/ja/pricing` · `/pt/pricing`
- `https://www.lovart.ai/zh/topics/zh-pricing-cn` — **"Starter 起 $15/月含商业授权。支持支付宝。"**
- `https://www.lovart.ai/zh/topics/zh-pricing-compare` · `/zh/topics/zh-pain-collaboration-blocked`
- `https://www.lovart.ai/statement/terms-of-use` (2026-07-09) · `https://www.lovart.ai/statement/privacy-policy` (2025-07-23)
- `https://www.lovart.ai/statement/lovart-subscribe-faq` (2026-06-30)
- `https://www.lovart.ai/news` · `https://www.lovart.ai/changelog` · `https://www.lovart.ai/docs`
- `https://web-static3.lovart.ai/lovart_prd/static/_next/static/chunks/` — 58 chunks, 4.1 MB. Key files: `2cfihdcovcy8y.js` (Payway/PaymentMethod enums, `resolvePayway`, `checkIsCn`, `checkIsJp`, payway modal, `isSupportWxpay`), `1mx604a0-etun.js` (env config, `isCN: !1`, CN pay endpoints), `0-hdccp5_46x3.js` (team-order payway, CN paywall strings), `0julhcua7ovyd.js` (Xingliu migration), `0w95so0zkp1fq.js` (CN Alipay QR), `1ascpfhw4u352.js` (`LiblibAxiosBase`, Weixin login endpoints), `0tm2nwzq3y78i.js` (payway testIds, CN phone/WeChat login), `0e67yclpulsst.js` (API map)
- `https://www.lovart.ai/api/www/member/packages` — real endpoint, token-gated; nonsense sibling path returns a correctly-shaped 404 (control)
- `https://www.xingliu.art/` — **星流 - 新一代设计Agent**; `https://xla-web-static.xingliu.art/xingliu_prd/static/_next/static/chunks/` — 37 chunks, 7.8 MB: Shanghai entity + ICP filing, `/api/www/pay/wx/jsapi/info`, `/api/www/pay/alipay/jsapi/info`, 元 pricing, Alipay mandate copy, `Payway.WPS=11`
- `https://www.lovart.ai/zzz-control-not-real-7742` — **nonsense control**, 404 at 7,109 bytes

**Company, funding and HQ**
- `https://cloud.google.com/customers/lovart` — *"Location: China"*, *"more than 5 million users"*, CEO and Founder **Melvin Chen**, launched July 2025, "revenue has grown by 10x"
- `https://www.yicaiglobal.com/news/liblibai-parent-evoken-valued-at-over-usd2-billion-after-new-funding-round` — 2026-06-18, Evoken (formerly Qidian Xingyu Technology), Beijing, US$300M Series B+, Granite Asia / Tencent / Shunwei, **Ant Group** and HSG participating, >US$2B, ARR US$300M as of May
- `https://eu.36kr.com/en/p/3899540157236869` — Eanyo Tech owns LiblibAI, StarFlow/Lovart, LibTV; Chen Mian, ex-ByteDance; Lovart US$80M annualised 5 months post-launch
- `https://dealroom.co/news/142733-liblib-ai-hits-2b-valuation-with-300m-series-b-extension-as-arr-reaches/` — corroborates the round and Lovart's US$80M

**Payment vendors**
- `https://waffo.com/` — *"The global payments and monetization platform for digital businesses"*, 480+ methods / 173 markets, Merchant of Record
- Antom / Ant International background: `https://www.businesswire.com/news/home/20250903092575/en/Ant-Internationals-Antom-Debuts-Agentic-Payment-Solution-Pioneering-APM-Checkout-Solution-and-Trusted-AI-for-Secure-Transactions` — 300+ methods, 200+ countries, markets payment routing
- `https://stripe.com/gb/customers/canva` — Canva Korean domestic acquiring, 9.5M users of added reach since 2024, +2.1% success rate, >1.5% network-cost saving, top 40 markets

**Rails and regulation (fetched live, not from memory)**
- `https://www.band.com.br/economia/noticias/pix-lidera-pagamentos-no-brasil-com-547-das-transacoes-diz-banco-central-202604081055` — Banco Central data: Pix 54.7% of all transactions, 42.9bn operations, H2 2025; cards 30.4%
- `https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12341` — RBI/2022-23/73, CO.DPSS.POLC.No.S-518/02.14.003/2022-23, 16 June 2022, e-mandate AFA, ₹15,000 limit
- `https://www.digitaltransactions.net/commanding-92-of-the-home-market-its-no-wonder-chinese-mobile-giants-are-looking-abroad/` — ⚠️ Alipay+WeChat Pay 92% combined, **CB Insights data for end-2017**, article 2018-08-13. **Stale; flagged, not relied on**

**Complaints**
- `https://uk.trustpilot.com/review/www.lovart.ai` — TrustScore 1.5/5, 80 reviews, 84% one-star, billing complaints 2025-11-08 → 2026-10-12. (`trustpilot.com` and all regional mirrors return HTTP 403 to direct curl)

**Compliance screening**
- `https://www.federalregister.gov/api/v1/documents.json?conditions[agencies][]=industry-and-security-bureau&conditions[term]="<name>"` — Lovart / Liblib / LibLib / Eanyo / Evoken / Resonate International / Xingliu → **count 0** each; `"Zhipu"` → **count 1** (*Addition of Entities to and Revision of Entry on the Entity List*, 2025-01-16) — **positive control, passes**

**App-store checks**
- `https://itunes.apple.com/search?term=lovart&entity=software&country={us,cn,sg,jp,hk,br}` — no Lovart-published app; controls passed (`term=canva` in **cn**). **tw, in → HTTP 403, not checked**
- `https://itunes.apple.com/lookup?bundleId={ai.lovart.app, com.lovart.app, art.lovart.app, com.liblib.lovart, ai.lovart.lovart}` — `resultCount: 0` for all five
- `https://play.google.com/store/apps/details?id={ai.lovart.app, com.lovart.app, art.lovart.lovart, com.liblib.lovart, com.lovart.android}` — 404 for all five; control `com.canva.editor` → 200; `https://play.google.com/store/search?q=lovart&c=apps` → 20 apps, none Lovart-published

**Internal (lead data, not verified facts)**
- `accounts/apac-tal.csv` — **no row for Lovart, Liblib, Xingliu or Evoken** (control: `canva` → 1). Competitor stack notes for Kuaishou, Kling AI, MiniMax, Moonshot AI, z.ai carried from this file and **not re-verified in this run**
- `accounts/traffic/lovart.md` — SimilarWeb, supplied 2026-10-13
- `2-ready-to-outreach/manus-ai.md` — structural twin; method and Font-Awesome / vendor-grep trap list reused

**Blocked or unreachable in this environment (add to the standing list)**
`trustpilot.com` + all regional mirrors (403 to curl; readable via WebFetch) · `npci.org.in` (403, Akamai) · `beian.miit.gov.cn` (no connection) · `tianyancha.com` (419) · `qcc.com` (login wall) · `api.opencorporates.com` (token required) · `bizfile.gov.sg` (client-rendered SPA, no results in HTML) · `icis.corp.delaware.gov` (CAPTCHA-gated POST form) · `lovart.cn` (**proxy `CONNECT tunnel failed, response 502` — a proxy failure, not a DNS result; nothing concluded**)

</details>
