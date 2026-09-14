# WuKong Education

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 14 / 24 → ⭐ **High Priority** — earned on arithmetic, no override needed
**Industry:** E-Learning & EdTech (live 1-on-1 / small-group tutoring) · **HQ:** Contested — Mountain View, CA claimed; operational centre of gravity Auckland, NZ; billing entity Hong Kong · **Researched:** 2026-09-14 · **First email sent:** —
**Motion:** In-house — but a *shallow* in-house layer. See Section 3B.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** WuKong Education (悟空教育 / WuKong Chinese) sells live online Chinese, maths and English classes to overseas-Chinese families in the US, Canada, Australia, New Zealand, Singapore and a long tail of other markets. The model is sales-led: a free trial is booked on the site, an academic advisor calls, and the advisor closes a **prepaid class-credit package of roughly $349–$2,039 USD** — not a subscription. Payment is taken on a **self-built, self-hosted checkout at `pay.wukongsch.com`** whose client bundle contains their entire acquirer routing table in plaintext.

**SimilarWeb (supplied 2026-09-14):** `wukongsch.com`, Jun–Aug 2026, all traffic, **"Include all country domains" ON**, 60 countries. Full table in [`accounts/traffic/wukong-education.md`](../accounts/traffic/wukong-education.md).

**Largest market is the US at 43.89% — no market reaches 60%, and 16 countries carry >1% share.** ⚠️ **No total-visits figure was captured**, so country shares are solid but absolute monthly visits per market cannot be stated and are not stated anywhere in this report.

⚠️ **Engagement splits the country list into two different populations, and that split matters more than the ranking.** Ten markets behave like prospective buyers (2:00+ dwell, 2.7+ pages/visit): US, New Zealand, China, Australia, Canada, Germany, France, Brazil, Singapore, Netherlands. Nine behave like SEO-blog traffic (<1:00 dwell, <2 pages/visit): India (00:11), Sweden (00:08), Malaysia (00:18), Indonesia (00:19), Turkey (00:22), Philippines (00:32), Nigeria (00:44), Vietnam (00:49), Thailand (00:50). **India's 2.99% is not 2.99% of buyers.**

### Top 5 markets
Real SimilarWeb ranking (Jun–Aug 2026). The company's own ordering in its Play listing — "US, Canada, Australia, New Zealand, Singapore" — turns out to be **almost right but misses the UK**, which outranks New Zealand.

| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇺🇸 United States | **43.89%** ↑26.69% | The **only** market with a full method set: cards + PayPal force-unhidden, UnionPay, Venmo, Cash App Pay, Klarna, Atome, Alipay, WeChat Pay, AlipayHK, bank transfer, Easy Payment Plan | ACH / bank debit as a named rail | ⚠️ Smart Learner International Corporation (CA #5287146) — `[UNVERIFIED — search summary only]` |
| 2 | 🇨🇦 Canada | **5.13%** ↓13.90% | `CA` is in the buyer-country enum but **CAD is absent from the currency map** → falls through to `DEFAULT: []` | **Interac**; CAD presentment entirely. Their 2nd-largest market has **no method list at all** | ❌ None found |
| 3 | 🇦🇺 Australia | **4.07%** ↓4.31% | AUD supported: WeChat Pay, Alipay, AlipayHK, **Bank Transfer (tagged "Recommend")**, Credit/Debit Card (`hide:!0`), Klarna, Atome | **PayTo, BPAY, Afterpay, Zip** — all absent from an enumerated catalogue | ❌ None found |
| 4 | 🇬🇧 United Kingdom | **3.61%** ↑25.76% · **72.14% bounce, worst on the list** | **GBP is absent from the currency map** → `DEFAULT: []`. The only European rail in the entire catalogue is iDEAL, hard-scoped to NL/EUR. | GBP presentment; any UK rail whatsoever | ❌ None found; no Companies House record surfaced |
| 5 | 🇸🇬 Singapore | **3.17%** ↑14.05% | `SG` is in the buyer-country enum. A `PAY_NOW` entry exists but carries **no country/currency scoping** (unlike iDEAL). **SGD is absent from the currency map.** | **PayNow presentment in SGD**, GrabPay, NETS | ❌ SG entity appears **struck off** `[UNVERIFIED]` |

**Then:** 🇮🇳 India 2.99% *(00:11 dwell — SEO traffic, not buyers)* · 🇨🇳 China 2.60% **↓93.53%** *(highest-engagement market after the US and NZ; CNY is a first-class checkout currency)* · 🇳🇿 New Zealand 2.30% ↓31.57% *(only confirmed local entity)* · 🇮🇩 Indonesia 1.66% · 🇩🇪 Germany 1.59% · 🇵🇭 Philippines 1.56% · 🇸🇪 Sweden 1.53% · 🇲🇾 Malaysia 1.37% · 🇫🇷 France 1.24% · 🇧🇷 Brazil 1.09% · 🇳🇱 Netherlands 1.04% · 🇹🇷 Turkey 1.01% ↑194.06%

> **The single most damning line in the whole account:** iDEAL is hard-scoped and shipped for the **Netherlands, their 16th market at 1.04%** — while **Canada (#2, 5.13%), the UK (#4, 3.61%) and Singapore (#5, 3.17%) have no presentment currency at all.** Somebody built a rail for 1% of traffic and left 12% on an empty method list.

### Legal entities
- **WUKONG International (Hong Kong) Limited** (Hong Kong) — named in the Klarna **US** store-directory slug for a live merchant page that links out to `wukongsch.com`. *Entity name is from Klarna's merchant slug, not from an HK Companies Registry record.* **This is the billing entity facing US families.**
- **LAN GLOBAL LIMITED** (New Zealand) — NZ Company No. 6120872 / NZBN 9429043350629, inc. 29 Sep 2016. Named as **Google Play developer of record** with contact `it.account@wukongsch.com`, L3 49 Parkway Drive, Rosedale, Auckland 0632. Developer link **directly fetched**; registration numbers `[UNVERIFIED — search summary only]`.
- **Smart Learner International Corporation** (USA) — CA SoS #5287146, filed 11 Oct 2022, 340 E Middlefield Rd, Mountain View CA 94043. `[UNVERIFIED — search summary only]`; **medium-low confidence that it is the billing entity.**
- **SMART LEARNER INTERNATIONAL PTE. LTD.** (Singapore) — UEN 202129493C, inc. 24 Aug 2021, **status: struck off**. `[UNVERIFIED — search summary only]`; name-match to the US entity is suggestive, not proven.
- ❌ **No entity found** in Canada, Australia, the UK, Hong Kong (registry) or mainland China.

### Known PSPs
- **Citcon** — `[Source Code]` literal `paymentMethod:"CITCON"` (US buyers: Alipay, WeChat, UnionPay, PayPal, Cash App, Venmo)
- **Airwallex** — `[Source Code]` literal `method:"AIRWALLEX"`, routes `/aw/card`, `/aw/aw-add-params` (all non-US)
- **Latipay** — `[Source Code]` literal `paymentMethod:"LATIPAY"` (rest-of-world Alipay / WeChat / UnionPay)
- **PingPong** — `[Source Code]` `paymentMethod:"PINGPONG", standardPaymentMethod:"KLARNA"`
- **Stripe** — `[Source Code]` dedicated `/stripe` route, separate from `/aw/card` → **two card acquirers wired in parallel**
- **Klarna** — `[Source Code]` + `[Provider Page]` SDK `x.klarnacdn.net/kp/lib/v1/api.js` loaded on the gateway; live Klarna US merchant page
- **Atome** — `[Source Code]` `atomeAvailableCurrency` SSR prop
- **Manual bank transfer** — `/bankTransfer?countryCode=` route, tagged **`"Recommend"` in every currency**

### Orchestration status
**In-house orchestration layer — but a shallow one.** WuKong built and hosts its own checkout (`pay.wukongsch.com`, Next.js, footer "Supported by WuKong") holding the method catalogue, currency eligibility, BNPL gating and the acquirer-selection logic. **No third-party orchestrator SDK, iframe, domain or token appears anywhere in the bundle** — no Juspay, Primer, Gr4vy, Spreedly, IXOPAY, Adyen or Yuno string in any chunk (verified independently: 0 hits each).

The routing is a hardcoded ternary inside a React `useCallback`, verbatim from `1306-d238e146e95b80e3.js`:

```js
"billingInfomation"===e && "US"===n?.cascader?.country?.code
  || "billingInfomation"!==e && "US"===h
  ? "citcon" : "aw"
```

Buyer in the US → Citcon. Everyone else → Airwallex. No fallback, no retry, no cascade. Note the typo `billingInfomation` — hand-rolled, not a vendor SDK.

### Buying signals
- 🔧 **They already made the build-vs-buy decision once, badly.** Five acquirers, two card acquirers, country-hardcoded routing with no failover. The maintenance surface is growing and the routing logic is not. — [pay.wukongsch.com bundle](https://pay.wukongsch.com/_next/static/chunks/1306-d238e146e95b80e3.js)
- 🚩 **Cards are hidden by default outside the US** (`hide:!0`, force-unhidden only when `"US"===c`) and carry a `"(May Charge 3%)"` surcharge label, while **manual bank transfer is the only method tagged `"Recommend"` in all four currencies**. That is an admission in their own code that their card economics or auth rates outside the US do not work. — [index bundle](https://pay.wukongsch.com/_next/static/chunks/pages/index-091bbfd821769875.js)
- 🏦 **`jpmorgan-digitalsig-uat.wukongedu.net` and `jpmorgan-transport-uat.wukongedu.net`** exist in Certificate Transparency logs — a J.P. Morgan connectivity integration in a UAT environment. `[INFERENCE, not confirmed]` this is bank host-to-host / treasury connectivity work, i.e. they are actively building payment plumbing right now. — [crt.sh](https://crt.sh/?q=%25.wukongedu.net)
- 💬 **Moderate, consistent refund and FX friction** — an undisclosed 3% processing fee on refunds, a Canadian customer who wired in USD, was told to pay in CAD, paid twice and was still awaiting the refund. Their checkout literally disclaims the final amount: *"Currency conversions may affect the actual amount. Please refer to third-party payment platforms for the actual payment amount."* — [Trustpilot](https://ca.trustpilot.com/review/wukongsch.com?page=2) `[UNVERIFIED — search summary]` + [pay.wukongsch.com](https://pay.wukongsch.com/) (fetched)
- 📈 **Frost & Sullivan No.1 globally by cumulative paying users** (Feb 2026) — a *paying-user* metric, i.e. the billing base is the headline number they market on. — [PR Newswire](https://www.prnewswire.com/news-releases/wukong-chinese-ranked-no1-globally-based-on-cumulative-paying-users-according-to-frost--sullivan-302687368.html)

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Wukong Education` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

**Before drafting, read these three constraints:**
1. **Never open with "you have no orchestration layer."** They built one. The opening is that the layer they built has no cascade and no failover, and that they are paying for it in hidden cards and manual bank transfers.
2. **Do not pitch network tokens, dunning, retries on renewals, or mandate handling.** There is no recurring billing — grep for `subscription|recurring|autoRenew|saveCard|storedCard|cardToken|tokeniz|mandate` across all three bundles returns **zero hits**. The lever is **single-shot authorisation on a $349–$2,039 cross-border card transaction**, where a decline is a lost enrolment, not a retryable renewal. That is a stronger story, not a weaker one.
3. **The buyer is not an APAC consumer.** The payer is a Chinese-diaspora parent in Los Angeles, Toronto, Sydney or Singapore, paying a Hong Kong entity. Cross-border corridor economics, not local-rail coverage in India or Indonesia.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 14 / 24
| Signal | Points | Status |
|--------|--------|--------|
| Orchestration status | **+1** | ✅ **In-house layer confirmed** by direct source-code evidence. Scored +1 per the matrix. Worth noting the matrix's +1 assumes a mature in-house platform; this is a hardcoded ternary with no cascade, which makes the sale closer to greenfield than the score implies. |
| 3+ countries | **+3** | ✅ **Cleanly met.** **16 countries carry >1% traffic share** (SimilarWeb, supplied). Independently corroborated by the checkout code, which enumerates five buyer countries (`US, AU, CA, SG, NZ`) and four billing currencies. |
| Multiple PSPs | **+3** | ✅ **Five acquirers plus a manual rail**, every one a literal string in the checkout bundle: Citcon, Airwallex, Latipay, PingPong, Stripe. Independently re-verified — token counts in `1306-d238e146e95b80e3.js`: CITCON ×8, LATIPAY ×3, STRIPE ×2, AIRWALLEX ×1, PINGPONG ×1, KLARNA ×2. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Australia — now a genuine top-3 traffic market at 4.07%**, no caveat needed. AUD is a supported billing currency, yet **PayTo, BPAY, Afterpay and Zip are all absent** from a complete enumerated method catalogue — a sourced absence. Singapore (#5, 3.17%) compounds it: PayNow unscoped, SGD absent, entity struck off, and SG acquiring is regulatorily gated on local presence. Canada (#2, 5.13%) is worse still but sits outside APAC. |
| Recent expansion | **0** ⬜ | No new market launch found in the last 12 months. The 2026 Australian business-simulation programme is market *programming*, not market entry. GSV 150 and Frost & Sullivan are recognition. |
| Payment issues reported | **+2** | ✅ **Moderate.** Verbatim 1★ App Store reviews fetched directly (credit-transfer promise refused; package lock-in with no cancellation; classes withdrawn after full payment). Trustpilot's 3% refund fee and the USD/CAD double-charge are `[UNVERIFIED — search summary only]` but the 3% figure **matches the `remind:"(May Charge 3%)"` string in their own code**, which is strong mutual corroboration. Agent verdict: 6 of 109 iOS reviews payment-related (~5.5%) — recurring, not dominant. |
| Funding >$10M | **0** ❌ | Series B ~$10M reported, but dated **2022 or 2023** depending on aggregator — outside the 12-month window either way. The reported cap table (Marcy Venture Partners, Bobby Wagner, Daniel Wu) looks contaminated by a different "Wukong" and **should not be used in outreach**. |
| High traffic outside home | **+2** | ✅ **Met.** Largest market (US) is **43.89%** — comfortably under the 60% threshold, and the remaining 56% is spread across 59 countries with 15 more above 1%. SimilarWeb, supplied 2026-09-14. |
| Competitor using orchestration | **0** ❌ | Searched across LingoAce, AmazingTalker, LingoBus, PandaTree, Outschool, Preply, italki, 51Talk. **Zero** appear on Primer, Gr4vy, Spreedly, Corefy or Yuno. 51Talk's PayerMax is a cross-border PSP, not an orchestrator. |
| Payment job postings | **0** ❌ | No payments, treasury or billing-ops roles surfaced on `wukongsch.zhiye.com`, Liepin, BOSS直聘 or general search. Teaching roles only. |

**Tier:** **14 / 24 → ⭐ High Priority (14+)**. Earned on the arithmetic — **no analyst override applied**.
**No public payment RFP found** — no RFP override needed either.

> #### Note on the tier — the override was withdrawn
>
> This report first scored **12 / 24 → 🟢 Medium** with an upward analyst override, because three signals were unscoreable for want of a traffic split rather than for want of evidence, and the predicted ceiling on a proper pull was "14–15 / 24".
>
> Prateek supplied the SimilarWeb pull on 2026-09-14 (`wukongsch.com`, Jun–Aug 2026, all country domains ON). It landed at the bottom of that predicted range: **"high traffic outside home" converts to +2** (US 43.89%, under the 60% threshold), **"3+ countries" is now cleanly met** (16 countries >1%), and **the Australia rail gap is a genuine top-3 traffic market**, not the company's self-ordering. Total **14 / 24 → ⭐ High Priority on the arithmetic**. The override is withdrawn as no longer necessary.
>
> **The one caveat survives, and it is the important one: volume is still unconfirmed.** The `~$100M est.` on the TAL is supported by **no public source whatsoever** — neither confirmed nor refuted — and the supplied SimilarWeb view carried **no total-visits figure**, so we have shares without a denominator. At a $349–$2,039 ticket the business case is entirely a function of transaction count. **Establishing annual card volume is the first job of the first call.**
>
> **Second caveat, new from the traffic data: do not size this off raw traffic share.** Nine of the top twenty markets — India, Sweden, Malaysia, Indonesia, Turkey, Philippines, Nigeria, Vietnam, Thailand — sit under one minute of dwell and under two pages per visit. That is SEO-blog traffic, not enrolment intent. The commercially real footprint is roughly **US, Canada, Australia, UK, Singapore, China, New Zealand, Germany, France, Netherlands, Brazil**.

### Source Notes
- ✅ **Re-verified by me directly, not taken from an agent:** the `citcon`/`aw` routing ternary; the `hide:!0` flags on `AW_CARD` and `PAYPAL`; the `tag:"Recommend"` on Bank Transfer; the `remind:"(May Charge 3%)"` card label; the `"AW_CARD"!==a.key&&"PAYPAL"!==a.key||(a.hide=!1)` unhide function and its `"US"===c` call-site guard; the currency map containing **only** USD / AUD / NZD / CNY plus `DEFAULT:[]`; zero hits for Adyen, Juspay, Primer, Gr4vy, Spreedly and Yuno.
- ✅ **`wukongedu.net` and `wukongsch.com` are the same property** — `wukongedu.net/robots.txt` declares `Host: https://www.wukongsch.com/` and lists only `wukongsch.com` sitemaps. Primary source, fetched.
- ✅ **Certificate Transparency** (crt.sh, 188 unique names on `wukongedu.net` + 23 on `wukongsch.com`) confirms `pay`, `pay-dev`, `pay-test`, `s-payment.dev`, `s-payment.test`, `booking`, `student`, `cp-gateway`, `s-subscription.test`, `s-mall.test`, and the two `jpmorgan-*-uat` hosts.
- ⚠️ **Correction to an agent finding:** the Klarna **AU** merchant page (`/au/store/7032fca8-.../WuKong-Education/`) **302s to the Klarna AU store directory root** — it does not resolve to a merchant page. The claim of "two separate Klarna merchant entities" does **not** hold. Only the **US** page (`WUKONG-International-(Hong-Kong)-Limited`) is live and links out to `wukongsch.com`.
- ⚠️ **Correction to an agent finding:** the "Hong Kong" strings inside the Klarna US page HTML are generic locale UI entries (`FAB.Country.HK`), not entity metadata. The HK entity name rests on **Klarna's merchant URL slug alone**. Treat as strong but single-source.
- ⚠️ Trustpilot could not be fetched — **403 / AWS WAF** on both `www.` and `au.` mirrors. Its ~943–1,000 reviews across ~44 pages are the largest unread evidence pool in this report.
- ⚠️ `wukongsch.com` and `www.wukongedu.net` are behind a **Vercel Security Checkpoint (HTTP 429)** that persists with browser UA, referer and Accept-Language. `/terms/`, `/policy/` and `/faq/` were never read, and `/terms/` has **no Wayback snapshot**. Static assets (`robots.txt`) and the `pay.` subdomain are outside the checkpoint.
- ⚠️ All pricing figures ($349 / 12 sessions, $1,349 / 60 sessions, $349–$2,039 range, $2,800+ annual) are `[UNVERIFIED — search summary only]`.
- ❌ **Do not use the Series B cap table in outreach.** Internally contradictory across aggregators and probably a different company.
- ❌ **Do not cite "40 million global families."** It appears on a WuKong property and is not credible; their own other pages say 300,000 / 400,000 / "nearly one million".

### Success Case Alternatives
- **NetEase Games** — the closest structural match Yuno has in APAC: a Greater-China-origin company collecting from a globally distributed consumer base in multiple currencies, where approval rate on cross-border card is the primary lever. ⚠️ *Prateek has not yet supplied verified NetEase/Garena result figures — do not quote numbers until he does.*
- **Garena** — SEA-centric; weaker fit here, since WuKong's payers are in North America and ANZ, not SEA.
- ⚠️ **Gap:** the case library carries no cross-border education or high-ticket prepaid-package reference. The honest framing on a first call is corridor economics, not a same-vertical logo.

---

## Executive Summary

WuKong Education sells live online Chinese, maths and English tuition to overseas-Chinese families — **43.89% of traffic from the US and 56% spread across 59 other countries, 16 of them above 1% share** (SimilarWeb, supplied 2026-09-14) — billing **$349–$2,039 prepaid class-credit packages** through consultant-issued payment links rather than a self-serve cart. The decisive finding is that WuKong **built its own checkout and its own acquirer routing** at `pay.wukongsch.com`, fanning five acquirers — Citcon, Airwallex, Latipay, PingPong and Stripe — out of a normalised internal `paymentMethod` enum, with the routing decision itself being a hardcoded ternary on buyer country and **no fallback, retry or cascade anywhere in the bundle**. The sharpest single observation is that **credit and debit cards ship `hide:!0` and are force-unhidden only for US traffic**, carrying a `"(May Charge 3%)"` surcharge label, while **manual bank transfer is the only method tagged `"Recommend"` in all four supported currencies** — a merchant steering payers off cards and onto wire transfer on a two-thousand-dollar ticket. Their currency map holds exactly four entries — USD, AUD, NZD, CNY — so **Canada (#2), the UK (#4) and Singapore (#5), together 11.9% of traffic, fall through to an empty method list**, while the one scoped local rail they did build, iDEAL, serves the Netherlands at #16. The motion is **in-house**, but a shallow one: there is no platform to defend, and the opportunity is single-shot authorisation rate and acquirer failover on high-value cross-border card transactions where a decline costs an entire enrolment.

---

### Section 1: Website Traffic Analysis by Country

**Data source: resolution path 1 — pasted SimilarWeb data supplied by Prateek.** `wukongsch.com`, **Jun 2026 – Aug 2026**, all traffic, **"Include all country domains" ON**, 60 countries listed. Cited throughout as "SimilarWeb (supplied 2026-09-14)". Full table saved at [`accounts/traffic/wukong-education.md`](../accounts/traffic/wukong-education.md).

✅ **Correct domain, single pull.** `wukongedu.net` was deliberately **not** pulled separately — its `robots.txt` declares `Host: https://www.wukongsch.com/`, so it is the same property and a second pull would double-count.

⚠️ **No total-visits figure was captured in the supplied view.** Shares are reliable; **absolute monthly visits per country cannot be computed and are not stated anywhere in this report.** The only absolute figure that exists in any source is a 14-month-old search summary (~317.6K/mo, Jul 2024, `[ESTIMATE, not confirmed]`) and it must **not** be multiplied against these shares.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | 🇺🇸 United States | **43.89%** | Not available | ↑ 26.69% — growing | SimilarWeb (supplied 2026-09-14) |
| 2 | 🇨🇦 Canada | **5.13%** | Not available | ↓ 13.90% — declining | same |
| 3 | 🇦🇺 Australia | **4.07%** | Not available | ↓ 4.31% — stable/soft | same |
| 4 | 🇬🇧 United Kingdom | **3.61%** | Not available | ↑ 25.76% — growing | same |
| 5 | 🇸🇬 Singapore | **3.17%** | Not available | ↑ 14.05% — growing | same |
| 6 | 🇮🇳 India | 2.99% | Not available | ↑ 0.69% — flat | same |
| 7 | 🇨🇳 China | 2.60% | Not available | **↓ 93.53% — collapsed** | same |
| 8 | 🇳🇿 New Zealand | 2.30% | Not available | ↓ 31.57% — declining | same |
| 9 | 🇮🇩 Indonesia | 1.66% | Not available | ↑ 3.15% — flat | same |
| 10 | 🇩🇪 Germany | 1.59% | Not available | ↑ 0.78% — flat | same |
| 11 | 🇵🇭 Philippines | 1.56% | Not available | ↑ 43.10% — growing | same |
| 12 | 🇸🇪 Sweden | 1.53% | Not available | ↓ 22.13% — declining | same |
| 13 | 🇲🇾 Malaysia | 1.37% | Not available | ↓ 32.53% — declining | same |
| 14 | 🇫🇷 France | 1.24% | Not available | ↓ 33.09% — declining | same |
| 15 | 🇧🇷 Brazil | 1.09% | Not available | ↑ 45.27% — growing | same |
| 16 | 🇳🇱 Netherlands | 1.04% | Not available | ↓ 17.38% — declining | same |
| 17 | 🇹🇷 Turkey | 1.01% | Not available | **↑ 194.06% — fastest growth** | same |
| 18 | 🇻🇳 Vietnam | 0.96% | Not available | ↓ 2.64% — flat | same |
| 19 | 🇹🇭 Thailand | 0.95% | Not available | ↓ 10.51% — declining | same |
| 20 | 🇳🇬 Nigeria | 0.95% | Not available | ↓ 11.64% — declining | same |

Ranks 21–60 not captured; the top 20 account for **~80.7%** of traffic.

**High-priority markets (>5% share):** United States (43.89%), Canada (5.13%).

**Markets with no confirmed local entity, cross-referenced against Section 2 — this is nearly all of them:** 🇨🇦 Canada (#2), 🇦🇺 Australia (#3), 🇬🇧 United Kingdom (#4), 🇸🇬 Singapore (#5 — entity struck off), 🇮🇳 India (#6), 🇨🇳 China (#7), 🇮🇩 Indonesia (#9), 🇩🇪 Germany (#10), 🇵🇭 Philippines (#11). **The only confirmed local entity in the entire top 20 is New Zealand at #8 (2.30%)**, and the entity that actually bills (Hong Kong) does not appear in the top 20 at all.

> ⚠️ **Read the engagement columns before using any of these shares as buyer volume.** The list contains two different populations:
>
> - **Buyer-like (2:00+ dwell, 2.7+ pages/visit):** US (02:46 / 4.68), New Zealand (02:50 / 4.85), China (02:36 / 4.72), Australia (02:12 / 4.20), Canada (01:51 / 4.06), Germany (02:03 / 3.61), France (02:09 / 3.54), Brazil (03:18 / 2.95), Singapore (01:59 / 2.76), Netherlands (02:07 / 2.73).
> - **SEO-blog-like (<1:00 dwell, <2 pages/visit):** India (00:11 / 1.82), Sweden (00:08 / 1.35), Malaysia (00:18 / 1.81), Indonesia (00:19 / 1.37), Turkey (00:22 / 1.57), Philippines (00:32 / 1.61), Nigeria (00:44 / 1.76), Vietnam (00:49 / 1.88), Thailand (00:50 / 1.87).
>
> WuKong runs a large content/blog operation (`/blog/sitemap_index.xml`, `/cms/sitemap_index.xml` in robots.txt), which is the obvious explanation. **India's 2.99% is not 2.99% of buyers**, and nor is most of the SEA share. `[INFERENCE, not confirmed]` as to cause — the dwell and pages-per-visit figures themselves are measured data.

**Two movements worth a question on a call, neither of which should be asserted as fact:**
- **China −93.53%**, the largest swing in the table by an order of magnitude, and the only market with no country rank shown — yet still the third-highest engagement on the list (02:36 / 4.72) and a first-class CNY checkout currency. A drop that steep is either a real access event or a measurement artefact. **Do not assert a cause.**
- **UK 72.14% bounce**, by far the worst in the top 20, on a market growing 25.76% — and GBP is absent from the checkout currency map entirely. Correlation, not proven causation, but a very pointed one.

**Domains resolved:**

| Domain | Status | Finding |
|---|---|---|
| `wukongsch.com` / `www.` | **429 Vercel Security Checkpoint** | Primary global property. Unfetchable with browser UA, referer and Accept-Language headers. Static assets (`robots.txt`) still serve. |
| `wukongedu.net` (apex) | 200 earlier in the run; **404 on `/en` at re-check** | Chinese-language brochure. **`robots.txt` declares `Host: https://www.wukongsch.com/`** — same property, canonical host is `wukongsch.com`. Not a separate traffic property. |
| `www.wukongedu.net` | **429 Vercel Security Checkpoint** | Same block. |
| `pay.wukongsch.com` | **200 — "WuKong Payment Gateway"** | **Not behind the checkpoint.** The single most valuable asset in this run. |
| `pay.wukongedu.net` | **200 — byte-identical to `pay.wukongsch.com`** | Same deployment, two hostnames. |
| `student.wukongsch.com` | 200 — "WuKong Learning Center" | Post-purchase portal. |
| `booking.wukongsch.com` | CONNECT 502 | Exists in CT logs; unreachable from here. |
| `cp-gateway.wukongsch.com` | **TLS certificate expired** | Exists; expired cert. |
| `en.wukongsch.com` | 404 — **"ConnectYourDomain Error \| Wix.com"** | Abandoned Wix property, DNS still pointed. |
| `wukong.com` | 200 — 小悟空 AI assistant | ❌ **Different company. Never cite.** |
| `wukongacademy.com`, `wukongedu.com` | Do not resolve | — |

**Certificate Transparency inventory** — [crt.sh `%.wukongedu.net`](https://crt.sh/?q=%25.wukongedu.net) (188 unique names) and [crt.sh `%.wukongsch.com`](https://crt.sh/?q=%25.wukongsch.com) (23 names). Payment- and commerce-relevant hosts:

`pay.wukongsch.com` · `pay.wukongedu.net` · `pay-dev.wukongedu.net` · `pay-test.wukongedu.net` · `s-payment.dev.wukongedu.net` · `s-payment.test.wukongedu.net` · `booking.wukongsch.com` · `student.wukongsch.com` · `cp-gateway.wukongsch.com` · `cp-gateway-test.wukongedu.net` · `s-subscription.test.wukongedu.net` · `s-mall.test.wukongedu.net` · `s-wechat.test.wukongedu.net` · **`jpmorgan-digitalsig-uat.wukongedu.net`** · **`jpmorgan-transport-uat.wukongedu.net`**

> The two `jpmorgan-*-uat` hostnames are a **fact** from a public CT log. `[INFERENCE, not confirmed]` — "digitalsig" and "transport" are the naming pattern of J.P. Morgan host-to-host connectivity (signed file transport for treasury/payment files). If that reading is right, WuKong has been building direct bank connectivity in a UAT environment. Worth raising as a question on a call, **not** as an assertion in an email.
>
> `s-subscription.test` is also worth a note: a subscription *service* exists in their test estate even though **no subscription logic ships in the live checkout bundle**. Possible roadmap signal. `[INFERENCE, not confirmed]`.

---

### Section 2: Legal Entities & Local Presence

**Headquarters: contested, and worth understanding before a call.**
- **Mountain View, CA** — the company's own PR says "Silicon Valley"; 340 E Middlefield Rd matches the CA entity address. [PR Newswire](https://www.prnewswire.com/news-releases/wukong-education-named-to-the-2025-gsv-150-for-leading-the-way-in-education-technology-302338883.html)
- **Auckland, NZ** — Glassdoor location page (Candida Building 4, L3, 61 Constellation Dr, Rosedale 0630); Tracxn lists Auckland as base; Google Play gives a *second* Rosedale address (L3, 49 Parkway Drive, 0632). **Two different Rosedale addresses, unexplained.**
- **Hong Kong** — the billing entity for US buyers, plus hiring presence on hk.jobsdb.com.

`[INFERENCE, not confirmed]` "Silicon Valley HQ" reads as positioning for a US parent audience; the operational and legal centre of gravity looks like **Auckland for corporate and Hong Kong for money**.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| 🇭🇰 Hong Kong | **WUKONG International (Hong Kong) Limited** | Not found | [Klarna US merchant page](https://www.klarna.com/us/store/cb7b6231-09fb-4c35-af44-f1f1c9f2eaaa/WUKONG-International-(Hong-Kong)-Limited/pay-with-klarna/) — live, HTTP 200, links to `wukongsch.com`. Name from the merchant slug. |
| 🇳🇿 New Zealand | **LAN GLOBAL LIMITED** | NZ Co. 6120872 · NZBN 9429043350629 · inc. 29 Sep 2016 | [Google Play](https://play.google.com/store/apps/details?id=com.wukongacademy.studentportal) (fetched; developer email `it.account@wukongsch.com`); reg. numbers via [companyhub.nz](https://www.companyhub.nz/companyDetails.cfm?nzbn=9429043350629) `[UNVERIFIED]` |
| 🇺🇸 USA | **Smart Learner International Corporation** | CA SoS #5287146 · filed 11 Oct 2022 | [bizprofile.net](https://www.bizprofile.net/ca/mountain-view/smart-learner-international-corporation) `[UNVERIFIED]`; brand link via [virtualvocations](https://www.virtualvocations.com/company/remote-jobs-at-smart-learner-international-corporation-wukong-education-54402.html) |
| 🇸🇬 Singapore | **SMART LEARNER INTERNATIONAL PTE. LTD.** — **struck off** | UEN 202129493C · inc. 24 Aug 2021 | [sgpbusiness.com](https://www.sgpbusiness.com/company/Smart-Learner-International-Pte-Ltd) `[UNVERIFIED]` |
| 🇨🇦 Canada | Not found | — | — |
| 🇦🇺 Australia | Not found | — | No ASIC record surfaced |
| 🇬🇧 UK | Not found | — | No Companies House record surfaced, despite a live UK Trustpilot locale |
| 🇨🇳 China | Not found | — | Despite CNY being a first-class checkout currency |

**Cross-Border Gap Analysis:**

| Country | Traffic rank / share | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|---------------------|-------------------|---------------------------|---------------------|
| 🇺🇸 USA | **#1 · 43.89%** | ⚠️ Unverified | No | **High** — a Hong Kong entity is billing US families. Every US card transaction is cross-border, on the market that is 44% of all traffic. |
| 🇨🇦 Canada | **#2 · 5.13%** | ❌ No | No | **High** — and no CAD in the currency map at all, so their second-largest market has no presentment currency. |
| 🇦🇺 Australia | **#3 · 4.07%** | ❌ No | No | **High** — AUD supported, but no Australian rail and no entity. |
| 🇬🇧 UK | **#4 · 3.61%** | ❌ No | No | **High** — GBP absent from the currency map; worst bounce rate in the top 20 (72.14%). |
| 🇸🇬 Singapore | **#5 · 3.17%** | ❌ Struck off | **Yes** — SG acquiring generally requires local presence | **High** — the one market in the top 5 where the gap is regulatory, not merely a cost question. |
| 🇮🇳 India | #6 · 2.99% | ❌ No | **Yes** — domestic acquiring requires local presence | **High** — but note the 00:11 dwell; treat as SEO traffic, not buyers. |
| 🇨🇳 China | #7 · 2.60% *(↓93.53%)* | ❌ No | **Yes** — mainland domestic acquiring is gated behind local licensing | **High** — despite CNY being a first-class checkout currency. |
| 🇳🇿 New Zealand | #8 · 2.30% | ✅ LAN GLOBAL LIMITED | No | **Medium** — the only confirmed entity in the top 20; whether it is the *billing* entity is unknown. |
| 🇮🇩 Indonesia | #9 · 1.66% | ❌ No | **Yes** — local presence required for domestic acquiring | **High** — but 00:19 dwell; SEO cohort. |
| 🇩🇪 Germany | #10 · 1.59% | ❌ No | No | **High** — buyer-like engagement (02:03 / 3.61) with **no EUR in the currency map**. |
| 🇭🇰 Hong Kong | Not in top 20 | ✅ (billing entity) | No | **Low** — the entity that bills is in the one market that barely appears in the traffic. |

> *Warning: Potential cross-border operation in the United States, Canada, Australia, the United Kingdom and Singapore — ranks #1 through #5, together roughly **60% of all traffic**. No confirmed local billing entity in any of them. Transactions are likely processed cross-border, with higher scheme costs, lower approval rates and FX exposure.*

This is not speculative here — **the merchant says so themselves on their own payment page**: *"Currency conversions may affect the actual amount. Please refer to third-party payment platforms for the actual payment amount."* A merchant that controlled presentment currency would not need that disclaimer.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| **US buyers** — Alipay, WeChat Pay, UnionPay, PayPal, Cash App, Venmo | **Citcon** | `[Source Code]` literal `paymentMethod:"CITCON"` ×8 | [1306 chunk](https://pay.wukongsch.com/_next/static/chunks/1306-d238e146e95b80e3.js) |
| **All non-US** — cards, AlipayHK, WeChat HK, PayNow, DANA, GCash, KakaoPay, TrueMoney, Touch'n Go, iDEAL, Sofort, Giropay | **Airwallex** | `[Source Code]` literal `method:"AIRWALLEX"`; routes `/aw/card`, `/aw/aw-add-params` | same |
| **Rest-of-world** Alipay / WeChat / UnionPay (non-US, non-HK) | **Latipay** | `[Source Code]` `paymentMethod:"LATIPAY"` with `method:"wechat"` / `"alipay"` / `"upi_upop"` | same |
| Klarna instalments ("Easy Payment Plan") | **PingPong** | `[Source Code]` `paymentMethod:"PINGPONG", standardPaymentMethod:"KLARNA"` | same |
| Card — second, parallel route | **Stripe** | `[Source Code]` `case"STRIPE": Y("/stripe"...)`; `/stripe` is a distinct route from `/aw/card`, and is prefetched | same + [index chunk](https://pay.wukongsch.com/_next/static/chunks/pages/index-091bbfd821769875.js) |
| BNPL scheme, US/AU/NZ/CN | **Klarna** | `[Source Code]` SDK `x.klarnacdn.net/kp/lib/v1/api.js` in page head + `[Provider Page]` live merchant listing | [pay.wukongsch.com](https://pay.wukongsch.com/) · [Klarna US](https://www.klarna.com/us/store/cb7b6231-09fb-4c35-af44-f1f1c9f2eaaa/WUKONG-International-(Hong-Kong)-Limited/pay-with-klarna/) |
| BNPL scheme (SEA/HK) | **Atome** | `[Source Code]` `atomeAvailableCurrency` SSR prop + `{title:"Atome",key:"ATOME"}` | [pay.wukongsch.com](https://pay.wukongsch.com/) |
| All markets | **Manual bank transfer** | `[Source Code]` `/bankTransfer?countryCode=` route, tagged `"Recommend"` | index chunk |

**Two card acquirers wired in parallel** (`/stripe` and `/aw/card`) is itself a finding. Whether Stripe is primary, legacy or near-dead is unknown — the route exists, the volume share does not.

**False positives ruled out** (recorded because the integrity mandate requires it):
- `wukongedu.net` "omise" ×5 → all from `bg_promise_app.png` and CSS classes `promise-inner/-box/-bg`. **Not Omise.**
- `pay.wukongsch.com` "eway" → substring of `<title>WuKong Payment Gat**eway**</title>`. **Not eWAY.**
- `4426` chunk "omise.resolve" → `Promise.resolve`. **Not Omise.**
- `1306` chunk "zipCode" ×4 → billing-address field. **Not Zip/Quadpay.**
- `dLocale` → substring of a locale variable. **Not dLocal.**
- `wukong.com` → 小悟空, a Chinese AI-assistant product. **Different company, discarded.**
- "Black Myth: Wukong" (the video game) → discarded from all search results.

#### 3B. Payment Orchestrator

**Classification: In-house orchestration layer.** `[Source Code]`, [pay.wukongsch.com](https://pay.wukongsch.com/) and its chunks.

WuKong hosts its own checkout, which owns the method catalogue, the country/currency eligibility rules, the BNPL availability gating (`klarnaAvailableCurrency`, `atomeAvailableCurrency`) and the acquirer-selection logic. Five acquirers plus a manual rail fan out from a normalised internal `paymentMethod` enum. **No third-party orchestrator SDK, iframe, domain or token appears anywhere in any bundle** — independently verified, zero hits for Adyen, Juspay, Primer, Gr4vy, Spreedly and Yuno.

> *Confirmed in-house. Do not argue "you need orchestration" — they have a routing layer and will say so. Argue **reach and failover**: their routing is a two-branch ternary on buyer country with no cascade, no retry and no second acquirer to fall to when the first declines.*

The whole "orchestration layer" is this, verbatim:

```js
j=(0,d.useCallback)((function(e,n){
  return "billingInfomation"===e && "US"===n?.cascader?.country?.code
      || "billingInfomation"!==e && "US"===h
      ? "citcon" : "aw"
}),[h])
```

And the method dispatch it feeds, abridged:

```js
case"WECHAT":   paymentMethod:"LATIPAY", method:"wechat"
case"ALIPAY":   paymentMethod:"LATIPAY", method:"alipay"
case"UNION_PAY":"citcon"===j(e,o) ? paymentMethod:"CITCON", payMethod:UPOP, countryName:"US"
                                  : paymentMethod:"LATIPAY", method:"upi_upop"
case"PAYPAL":   paymentMethod:"CITCON", payMethod:PAYPAL, countryName:"US"
case"CASH_APP": case"VENMO": paymentMethod:"CITCON"
case"INSTALLMENT": paymentMethod:"PINGPONG", standardPaymentMethod:"KLARNA"
case"STRIPE":   Y("/stripe"...)
case"AW_CARD":  Y("/aw/card"...)
case"DANA": case"GCASH": case"KAKAO": case"TRUEMONEY": case"TNG":
case"SOFORT": case"GIROPAY": case"IDEAL": → AIRWALLEX
case"PAY_NOW":  currency: SGD → AIRWALLEX
```

> **MANUAL:** book a free trial, let an advisor issue a real order link, and open `pay.wukongsch.com?orderId=…` with DevTools. That is the only way to see which methods actually *render* per country — everything above is the code's routing table, not an observed checkout.

---

### Section 4: Alternative & Local Payment Methods

The gateway bundle contains a **complete, enumerated method catalogue**, so absence from it is a **sourced absence**, not an assumption. One caveat: Apple Pay and Google Pay could still surface inside a hosted Airwallex or Stripe card component without appearing as named methods — treat those two as "not offered as a top-level choice" rather than definitively unavailable.

**Master catalogue, verbatim:**

```js
{title:"WeChat Pay",        key:"AW_WECHAT",   paramsKey:"wechatpay"}
{title:"Alipay",            key:"AW_ALIPAY",   paramsKey:"alipaycn"}
{title:"AlipayHK",          key:"ALIPAY_HK",   paramsKey:"alipayhk", listTips:"For Hong Kong residents only"}
{title:"Bank Transfer",     key:"BankTransfer", tag:"Recommend"}
{title:"Credit/Debit Card", key:"AW_CARD", hide:!0,
   listTips:"Some banks may charge overseas transaction fees...", remind:"(May Charge 3%)"}
{title:"Union Pay",         key:"UNION_PAY"}
{title:"Easy Payment Plan", key:"INSTALLMENT"}
{title:"PayPal",            key:"PAYPAL", hide:!0,
   listTips:"PayPal may charge extra transaction fees, actual amount may differ.", remind:"(Extra fees may apply)"}
{title:"Venmo",             key:"VENMO"}
{title:"Cash App Pay",      key:"CASH_APP"}
{title:"Pay Now",           key:"PAY_NOW",  paramsKey:"pay_now"}
{title:"iDEAL",             key:"IDEAL", country:["NL"], currencys:{NL:["EUR"]}, paramsKey:"ideal"}
{title:"Klarna", key:"KLARNA"}   // server-gated on klarnaAvailableCurrency
{title:"Atome",  key:"ATOME"}    // server-gated on atomeAvailableCurrency
```

**Per-currency "Recommended payment methods" map — verified directly:**

| Currency | Recommended list, in order |
|---|---|
| **USD** | WeChat Pay, Alipay, AlipayHK, **Bank Transfer ("Recommend")**, Klarna, PayPal, Atome, Credit/Debit Card |
| **AUD** | WeChat Pay, Alipay, AlipayHK, **Bank Transfer ("Recommend")**, Credit/Debit Card, Klarna, Atome |
| **NZD** | WeChat Pay, Alipay, AlipayHK, **Bank Transfer ("Recommend")**, UnionPay, Credit/Debit Card, Klarna, Atome |
| **CNY** | WeChat Pay, Alipay, AlipayHK, **Bank Transfer ("Recommend")**, Credit/Debit Card, Klarna, Atome |
| **DEFAULT** | **`[]` — empty** |

Verified: the currency map contains **only** `USD:[`, `AUD:[`, `NZD:[`, `CNY:[` and `DEFAULT:[]`. **CAD, SGD, GBP, HKD, EUR, MYR and JPY all fall through to an empty list.**

The US unhide function and its guard, verified verbatim:

```js
// call site
v = "US"===c ? ie(v, I?.money?.currency) : v
// inside ie
["KLARNA","ATOME"].includes(a.key) || ("AW_CARD"!==a.key && "PAYPAL"!==a.key || (a.hide=!1), n.push(a))
```

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| All | Credit/Debit Card (`AW_CARD`) | Cards | **Active but `hide:!0`** — force-unhidden only for US traffic; labelled `(May Charge 3%)` | index chunk |
| All | Bank Transfer (`/bankTransfer`) | Bank transfer / A2A | **Active — the only method tagged `"Recommend"`, in every currency** | index chunk |
| All | Alipay (`alipaycn`) | Digital wallet | Active | index chunk |
| All | WeChat Pay (`wechatpay`) | Digital wallet | Active | index chunk |
| 🇭🇰 Hong Kong | AlipayHK | Digital wallet | Active — "For Hong Kong residents only" | index chunk |
| US / NZD | UnionPay | Cards | Active | index chunk |
| US, AU, NZ, CN | PayPal | Digital wallet | **Active but `hide:!0`** outside US | index chunk |
| 🇺🇸 US only | Venmo | Digital wallet | Active | index chunk |
| 🇺🇸 US only | Cash App Pay | Digital wallet | Active | index chunk |
| US, AU, NZ, CN | Klarna | BNPL | Active, server-gated by currency | gateway page + Klarna merchant page |
| US, AU, NZ, CN | Atome | BNPL | Active, server-gated | gateway page |
| All | "Easy Payment Plan" (`INSTALLMENT`) | BNPL/Instalments | Active, via PingPong→Klarna | 1306 chunk |
| 🇳🇱 Netherlands | iDEAL | Bank redirect | Active — hard-scoped `country:["NL"], currencys:{NL:["EUR"]}` | index chunk |
| 🇸🇬 Singapore (likely) | "Pay Now" | Bank transfer / A2A | Active in catalogue, **but no country/currency scoping** unlike iDEAL, and **SGD is absent from the currency map** | index chunk |
| 🇨🇦 Canada | **Interac** | Bank / debit | ❌ **Not found** — and CAD has no currency-map entry | index chunk |
| 🇦🇺 Australia | **PayTo, BPAY, Afterpay, Zip** | Bank / BNPL | ❌ **Not found** | index chunk |
| 🇲🇾 Malaysia | FPX, Touch 'n Go, GrabPay | Bank / wallet | ❌ **Not found** | index chunk |
| All | **Apple Pay, Google Pay** | Digital wallet | ❌ Not found as named methods (could exist inside a hosted card field) | index chunk |
| All | Affirm, Afterpay | BNPL | ❌ Not found | index chunk |
| 🇮🇳 India (#6, 2.99%) | UPI, netbanking, RuPay, EMI | Local | ❌ **Not found** | index chunk |
| 🇮🇩 Indonesia (#9, 1.66%) | QRIS, GoPay, OVO, DANA | Local | ❌ **Not in the rendered catalogue** — **but `case"DANA"` routes to Airwallex in the dispatch switch.** Plumbing without a front end. | 1306 + index chunks |
| 🇵🇭 Philippines (#11, 1.56%) | GCash, Maya | Local | ❌ **Not in the rendered catalogue** — **but `case"GCASH"` routes to Airwallex.** | 1306 + index chunks |
| 🇲🇾 Malaysia (#13, 1.37%) | FPX, Touch 'n Go, GrabPay | Local | ❌ **Not in the rendered catalogue** — **but `case"TNG"` routes to Airwallex.** | 1306 + index chunks |
| 🇹🇭 Thailand (#19, 0.95%) | PromptPay, TrueMoney | Local | ❌ **Not in the rendered catalogue** — **but `case"TRUEMONEY"` routes to Airwallex.** | 1306 + index chunks |
| 🇻🇳 Vietnam (#18, 0.96%) | MoMo, ZaloPay, VNPay | Local | ❌ Not found | index chunk |
| 🇰🇷 Korea / 🇯🇵 Japan | KakaoPay, Toss, PayPay, konbini | Local | ❌ **Not in the rendered catalogue** — **but `case"KAKAO"` routes to Airwallex.** Neither market appears in the top 20 traffic. | 1306 + index chunks |
| 🇩🇪🇫🇷 Germany / France | SEPA, Sofort, Cartes Bancaires | Local | ❌ Not found — **and EUR is absent from the currency map.** `case"SOFORT"` and `case"GIROPAY"` route to Airwallex but are not in the catalogue. | 1306 + index chunks |
| 🇬🇧 UK | GBP presentment, any UK rail | — | ❌ **Not found. GBP is absent from the currency map entirely.** | index chunk |

> *Warning: In **Canada (#2, 5.13%)**, Interac is the dominant domestic rail and CAD is not even a supported presentment currency — a CAD-denominated order falls through to `DEFAULT: []`, an empty method list. There is a public Trustpilot complaint of a Canadian customer double-paying over exactly this USD/CAD mismatch.*
>
> *Warning: In **Australia (#3, 4.07%)**, PayTo and BPAY are established domestic rails and Afterpay/Zip are the dominant local BNPL brands, yet none appears in WuKong's enumerated method catalogue — BNPL for AUD is Klarna and Atome only.*
>
> *Warning: In the **UK (#4, 3.61%, growing 25.76%)**, GBP is absent from the currency map entirely. A UK parent gets an empty recommended list. The UK also carries the worst bounce rate in the top 20 at **72.14%** — correlation, not proven causation, but pointed.*
>
> *Warning: In **Singapore (#5, 3.17%)**, PayNow is the dominant domestic A2A rail. A `PAY_NOW` entry exists but SGD is absent from the currency map, so a Singapore parent is billed in a foreign currency on a rail that may not even be scoped to them. Singapore is also the one top-5 market where local acquiring is **regulatorily gated** on local presence — and their SG entity appears struck off.*
>
> *Warning: **Germany (#10, 1.59%), France (#14, 1.24%) and the Netherlands (#16, 1.04%)** are all in the buyer-like engagement cohort. EUR is absent from the currency map. The single European rail in the entire catalogue is **iDEAL, hard-scoped to NL/EUR** — built for the 16th-largest market while the 2nd, 4th and 5th have no presentment currency at all.*

**Alipay / WeChat Pay — confirmed, and prioritised above cards.** All three Chinese rails (Alipay mainland, WeChat Pay, AlipayHK) sit **first in every single currency's recommended list — above cards, above PayPal, above bank transfer**. A family in Los Angeles or Sydney is being offered a mainland Chinese wallet as the default. This confirms the diaspora hypothesis, and it is also why **Citcon** (a US-based Alipay/WeChat/UnionPay cross-border specialist) is the US acquirer.

**Currency:** the gateway ships a currency picker (`supportCurrencys`, `selectCurrencyVisble`, `onCurrencyConfirm`), so the payer can switch currency at checkout. **CNY is a first-class checkout currency.**

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| **Cross-border payment failure + double payment + refund pending** — wired in USD, told to pay in CAD, paid a second time by card, *"Now I am still waiting for the refund of the..."* | Trustpilot CA | Isolated but the most diagnostic single item | Undated | [ca.trustpilot.com](https://ca.trustpilot.com/review/wukongsch.com?page=2) `[UNVERIFIED — search summary only]` |
| **Undisclosed 3% processing fee deducted from refunds** — *"charge a 3% processing fee that I was unaware of and did not care to make it right in any way"* | Trustpilot | **Moderate** — multiple independent reviewers | Undated | [trustpilot.com](https://www.trustpilot.com/review/wukongsch.com?page=6) `[UNVERIFIED — search summary only]` — **but corroborated by `remind:"(May Charge 3%)"` in their own code** |
| **Refund charged a fee / refund friction** on a $1,199 6-month programme | Trustpilot | Moderate | Undated | [trustpilot.com](https://www.trustpilot.com/review/wukongsch.com?page=6) `[UNVERIFIED]` |
| **Refund delay on a $699 prepaid package** — *"who knows take how long can get my money back"* | Trustpilot AU | Isolated | Undated | [au.trustpilot.com](https://au.trustpilot.com/review/wukongsch.com?page=3) `[UNVERIFIED]` |
| **Unused class credits — transfer promise refused**, title *"promise flexibility NOT honored"* — verbatim: *"I was told that if I cannot use all of them, I can transfer the credit to Chinese class or English class, or to a sibling. However when I truly needed that, I was told they don't allow it. I was also asked to provide screenshots and show who made that promise."* | iOS App Store (US), 1★ | Isolated | Recent | [apps.apple.com/us/app/id1574837622](https://apps.apple.com/us/app/id1574837622) — **fetched, verbatim** |
| **Prepaid package lock-in, no cancellation** — *"you can't even cancel it or get your money back when you lose interest… if I cancel too last second it still takes my money"* | iOS App Store (US), 1★ | Isolated | Recent | same — **fetched, verbatim** |
| **Paid classes withdrawn / more money demanded** — *"the owner or worker kept asking for more money, even though the classes were already fully paid for. Then she took away my daughter's classes."* | iOS App Store (US), 1★ | Isolated | Recent | same — **fetched, verbatim** |
| **Refund conditions not disclosed at sign-up**; *"Despite 'unconditional refund' claims, actually getting money back involves administrative hurdles"* | Third-party review aggregation | Moderate | 2026 | [joshuawwy.com](https://joshuawwy.com/c/2026/a/wukong-review) `[UNVERIFIED]` |

**Honest frequency assessment:** 109 unique iOS reviews were read across the US/GB/AU/CA/SG storefronts; 6 matched payment keywords (~5.5%), of which 4 are genuine payment/refund findings. The other ~95% are product complaints — teacher turnover, app glitches, curriculum — and are excluded. **Verdict: MODERATE, not high.** Trustpilot carries ~943–1,000+ reviews across ~44 pages which could not be read (403 / AWS WAF), so the payment share *there* is unknown.

**No evidence of chargebacks or card disputes was found.** The *conditions* for them are well documented above; do not claim chargeback volume.
**No auto-renewal disputes** — consistent with there being no recurring billing.

> *Pattern: refund friction + FX mismatch + an undisclosed 3% card surcharge, on a merchant whose own checkout disclaims the final charged amount, points to a merchant collecting cross-border in a presentment currency it does not control. That is local acquiring and multi-currency presentment, not a refunds-policy problem.*

**Does the "unconditional refund" promise hold?** The Chinese site carries 「**退款承诺：对课程不满意，随时可提出退款要求**」 ("Refund commitment: if dissatisfied with the course, you may request a refund at any time"), and English materials claim *"Risk-free, unconditional refunds."* Evidence contradicts it on three consistent points: **a 3% fee is deducted** (an "unconditional" refund that returns 97% is a payment-operations gap); **unused credits are not freely transferable or cancellable**; **refunds are slow when granted**. Counter-evidence exists — one third-party review states dissatisfied customers do get unused credits refunded, and the Trustpilot aggregate sits at 4.5/5 across ~943 reviews. The realistic reading: **a promise honoured with friction, fees and delay**, not one refused.

**The BNPL wrinkle:** Klarna on a $349–$2,039 prepaid education package means the refund clock and the Klarna repayment clock run separately. A parent refunded at 97% while still repaying Klarna is a live failure mode.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | **Feb 2026** | Ranked **No.1 globally** among online Chinese-education platforms in non-native-Chinese regions **by cumulative paying users** (Frost & Sullivan Market Position Statement, research completed Jan 2026, as of 31 Dec 2025). Scope excludes mainland China, HK, Macau, Taiwan. Vendor-commissioned. | Market position — payment-adjacent | [PR Newswire](https://www.prnewswire.com/news-releases/wukong-chinese-ranked-no1-globally-based-on-cumulative-paying-users-according-to-frost--sullivan-302687368.html) |
| 2 | **2026** | International Business Simulation debuts in **Australia**; four teams qualify for global finals in Shanghai. Active AU market programming, **not** market entry. | Market activity (AU) | [PR Newswire APAC](https://www.prnewswire.com/apac/news-releases/international-business-simulation-debuts-in-australia-four-teams-qualify-for-global-finals-in-shanghai-302772317.html) |
| 3 | **2025** | 9th anniversary: "over 400,000 families", "118 countries and regions", teachers 3,000 → 4,500 | Scale (self-reported) | [PR Newswire](https://www.prnewswire.com/news-releases/from-one-online-classroom-to-400-000-families-wukong-education-marks-its-9th-anniversary-with-a-growing-global-vision-302593777.html) |
| 4 | **Dec 2024 / 2025 list** | Named to the **GSV 150**, selected on revenue scale, growth, user reach, geographic diversification and margin profile. No numbers disclosed. | Recognition | [PR Newswire](https://www.prnewswire.com/news-releases/wukong-education-named-to-the-2025-gsv-150-for-leading-the-way-in-education-technology-302338883.html) |
| 5 | **Jun 2023 or Dec 2022 — contested** | **Series B**, ~$10M reported, investors listed as Bessemer Venture Partners, Marcy Venture Partners, Daniel Wu Neh-Tsu, Bobby Wagner. **Dating inconsistent across Crunchbase and CB Insights; the cap table looks contaminated by a different "Wukong".** | Funding | [Crunchbase](https://www.crunchbase.com/organization/wukong-education) · [CB Insights](https://www.cbinsights.com/company/wukong-education) — ❌ **do not use in outreach** |

⚠️ **Conflicting self-reported scale claims across WuKong's own properties:** "300,000 families" (zh/aboutus) vs "400,000 families" (9th-anniversary PR) vs "nearly one million families" (Feb 2026 PR) vs "more than 40 million global families". **The 40M figure is not credible and must never be cited.**

**No public payment-related RFP found.**
**No payment-related job postings found** — recruitment properties (`wukongsch.zhiye.com`, Liepin, BOSS直聘) surface teaching roles only.
**Licence applications:** none found in any APAC market.

---

### Section 7: Payment-Specific News

**No payment press release, PSP partnership announcement, provider removal or billing-model change was found in any public source.** Not a single item across thepaypers, finextra, pymnts, techinasia, e27 or the company newsroom.

What exists instead is directly observable infrastructure, already documented in Sections 3 and 4:

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | Observed 2026-09-14 | WuKong runs its **own branded hosted payment gateway** at `pay.wukongsch.com`, separate from the WAF-blocked main site, rendering "Recommended" and "Other" payment-method groups | Confirms a self-built method-routing layer, not a single-PSP checkout | [pay.wukongsch.com](https://pay.wukongsch.com/) |
| 2 | Observed 2026-09-14 | **Klarna is live**, confirmed two ways: SDK in the page head, and a live Klarna US merchant page naming **WUKONG International (Hong Kong) Limited** | Confirms the HK billing entity and BNPL on a high-ticket prepaid package | [Klarna US](https://www.klarna.com/us/store/cb7b6231-09fb-4c35-af44-f1f1c9f2eaaa/WUKONG-International-(Hong-Kong)-Limited/pay-with-klarna/) |
| 3 | Observed 2026-09-14 | `jpmorgan-digitalsig-uat` and `jpmorgan-transport-uat` subdomains in Certificate Transparency | `[INFERENCE]` bank host-to-host connectivity being built in UAT | [crt.sh](https://crt.sh/?q=%25.wukongedu.net) |

> **No provider removals identified.**

---

### Section 8: Checkout Experience Audit

**Partially accessible.** `pay.wukongsch.com` returns HTTP 200 and its full client bundle was read, but the page is **order-bound** — without a valid `orderId` it returns `"orderApiErr":"Must have orderId"` with an empty `orderInfo`, so the method list never renders. Everything below is either (a) directly observed in the served HTML/JS, or (b) read out of the routing code and **labelled as such**. `wukongsch.com` itself is behind a Vercel checkpoint and was never rendered.

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | **Custom-built, self-hosted, order-link based.** Next.js app, build `vRXbbt0epgQN1gRRSqdio`, footer "Supported by WuKong" | Fair | Not a cart. An advisor issues a payment link per order. |
| Guest checkout | N/A — the order link *is* the identity. `userId` is passed in the route query. | Good | No account creation friction at pay time |
| Steps to complete payment | Advisor call → order link issued → select method → redirect to acquirer → `/result` | Fair | The human step before payment is the bottleneck, not the page |
| Card input experience | **Redirect to `/aw/card` or `/stripe`** — no card fields on the WuKong page itself | Good | Keeps PCI scope down; costs conversion |
| Payment methods visible | Two groups, "Recommended payment methods" and "Other payment methods" — both render empty without a valid order | Not assessable live | Catalogue read from code, Section 4 |
| Location-based method display | **Yes, on two axes at once** — order *currency* selects the recommended list, buyer *IP/billing country* triggers the US-only unhide and the Citcon/Airwallex acquirer choice | Fair | Adaptive, but the adaptation is hardcoded and only really built out for the US |
| Instalment / EMI options | Klarna, Atome and an "Easy Payment Plan" (PingPong→Klarna). Server-gated on `klarnaAvailableCurrency` / `atomeAvailableCurrency` | Good | Appropriate for a $349–$2,039 ticket |
| 3DS implementation | **Not detected — and not detectable** without an order token. Card entry is redirected to the acquirer, so 3DS would be the acquirer's. | Unknown | **Do not claim either way** |
| PCI indicator | Card capture is redirected out to Airwallex or Stripe, not self-hosted fields | Good | `[INFERENCE, not confirmed]` → likely SAQ A |
| Mobile responsiveness | `viewport` locked with `minimum-scale=1, maximum-scale=1` (pinch-zoom disabled); layout capped at `max-width:699px` | Fair | Built mobile-first; zoom-lock is an accessibility negative |
| Multi-currency / local pricing | Currency picker present (`supportCurrencys`, `onCurrencyConfirm`). **Only USD, AUD, NZD, CNY have method lists.** Packages published in USD. | **Poor** | CAD, SGD, GBP, HKD, EUR, MYR fall to an empty list |
| Saved payment methods | **None.** Zero hits for `saveCard`, `storedCard`, `cardToken`, `tokeniz` across all three bundles | Poor | Every repurchase is a fresh full-friction payment |
| Error message clarity | Generic: *"The selected country does not support this payment method. Please reselect."* Expiry overlay: *"Order expired / Please contact the consultant to re-initiate the order payment"* | Fair | An expired link sends the parent back to a human |

**Verbatim from the page (fetched):**
- *"Currency conversions may affect the actual amount. Please refer to third-party payment platforms for the actual payment amount."*
- *"By clicking the Pay button means that you have read and agreed to our Terms of Service."*
- Card: *"Some banks may charge overseas transaction fees, please confirm with your issuing bank for details."* + `remind:"(May Charge 3%)"`
- PayPal / Venmo: *"PayPal may charge extra transaction fees, actual amount may differ."* + `remind:"(Extra fees may apply)"`

**Also present in the checkout:** flash-sale (秒杀) pricing with a countdown and *"Only {n} items left, Price after restoration {currency} {value}"*, an order-expiry countdown, and a `paymentMethod:"ZERO"` short-circuit for zero-value orders (free trials run through the same order system).

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **Not found** | No attestation, SAQ level or compliance page located |
| Card data handling | **`[INFERENCE, not confirmed]` — likely SAQ A** | Card entry is routed out to `/stripe` and `/aw/card`, i.e. redirect/hosted capture at Airwallex or Stripe; no card input fields exist on `pay.wukongsch.com` itself |
| Recommended Yuno integration | **SDK** (drop-in / hosted fields) | Consistent with their current redirect model and keeps scope unchanged. A back-to-back API integration would expand their PCI scope and should not be led with. |

*No direct PCI compliance documentation found publicly for WuKong Education.* The privacy policy at `https://www.wukongsch.com/policy/` is the most likely place a processor or PCI statement is named, and it **could not be fetched** — Vercel checkpoint, no Wayback snapshot. **This is the highest-value unread document in the account.**

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: They hide their own card option outside the US and tell parents to wire money instead.**
> **Evidence:** Section 3A/4 — `{title:"Credit/Debit Card",key:"AW_CARD",hide:!0,remind:"(May Charge 3%)"}`, force-unhidden only inside `ie()` which is called only when `"US"===c`; meanwhile `{title:"Bank Transfer",key:"BankTransfer",tag:"Recommend"}` in **all four** currency lists. ([index chunk](https://pay.wukongsch.com/_next/static/chunks/pages/index-091bbfd821769875.js)) + Section 5 — a Canadian parent who wired in USD, was told to pay in CAD, paid twice, and was still awaiting a refund ([Trustpilot CA](https://ca.trustpilot.com/review/wukongsch.com?page=2)).
> **Pain Point:** **56% of their traffic is outside the US** (SimilarWeb supplied 2026-09-14; US is 43.89%), and every one of those visitors sees a checkout with the card option hidden. On a $349–$2,039 enrolment, pushing a parent from a two-tap card payment to a manual bank transfer is a conversion event, not a cost optimisation. Wires arrive days later, in the wrong currency, unreconciled, and land on a human to chase. A merchant only does this when cross-border card economics — decline rates, interchange, FX — have stopped working.
> **Yuno Value Proposition:** Local acquiring in the US, Canada, Australia and Singapore turns those cross-border card attempts into domestic ones, which is where the approval-rate and interchange gap actually lives. The goal is to make the card option good enough to un-hide.
> **Best Success Case:** NetEase Games — Greater-China-origin merchant collecting from a globally distributed consumer base, approval rate as the primary lever. ⚠️ *Do not quote figures until Prateek supplies verified results.*
> **Outreach Angle:** "Your checkout ships credit card with `hide: true` everywhere except the US, and bank transfer as the only method tagged 'Recommend'. That's a decision someone made because the card numbers outside the US weren't working."
> **Suggested Subject Line:** Why is card hidden by default on pay.wukongsch.com?

> **Insight #2: Five acquirers, no cascade. A decline is just a decline.**
> **Evidence:** Section 3B — the entire acquirer selection is `"US"===h ? "citcon" : "aw"` inside a `useCallback`, with Latipay, PingPong and Stripe reached through a `switch` on method, and **no fallback, retry or second-attempt logic anywhere in the bundle**. Section 3A — two card acquirers (`/stripe`, `/aw/card`) are wired in parallel but nothing routes between them.
> **Pain Point:** They already carry the cost of five acquirer relationships — five contracts, five reconciliation formats, five sets of settlement timing — and get none of the benefit, because a declined transaction dies where it falls. On a single-shot $1,349 package purchase, a soft decline is a lost enrolment. And they can't retry, because there's no stored card either (zero hits for `saveCard`/`cardToken`).
> **Yuno Value Proposition:** They've already paid the integration tax for multi-acquirer. Orchestration is what converts that sunk cost into recovered revenue — cascade the decline to the second acquirer, retry on a different route, and stop maintaining routing logic in a React component.
> **Best Success Case:** NetEase Games.
> **Outreach Angle:** "You've integrated Citcon, Airwallex, Latipay, PingPong and Stripe. The routing between them is a one-line ternary on buyer country, and there's no cascade — so when Citcon declines a US card, nothing catches it."
> **Suggested Subject Line:** Five acquirers, one ternary

> **Insight #3: They built a payment rail for their 16th market and left their 2nd, 4th and 5th on an empty method list.**
> **Evidence:** Section 1 — SimilarWeb (supplied 2026-09-14): Canada **#2 at 5.13%**, UK **#4 at 3.61%**, Singapore **#5 at 3.17%** — together **11.9% of all traffic**. Section 4 — the recommended-methods map contains **only** `USD`, `AUD`, `NZD`, `CNY` and `DEFAULT:[]`, so **CAD, GBP and SGD all fall through to an empty list**; meanwhile the single European rail in the entire catalogue is **iDEAL, hard-scoped `country:["NL"], currencys:{NL:["EUR"]}`** — the Netherlands, **#16 at 1.04%**. Section 5 — a Canadian parent double-paid over exactly this USD/CAD mismatch.
> **Pain Point:** Someone had the appetite and the engineering time to ship a scoped local rail for one percent of traffic, and their second-largest market still can't be billed in its own currency. That is not a strategy, it's what happens when every market is a separate hand-built project competing for the same queue. Every Canadian, British and Singaporean parent is paying a foreign-currency cross-border card charge — with the UK carrying the worst bounce rate in the top 20 at 72.14%.
> **Yuno Value Proposition:** Local presentment currency and local rails across all three at once — Interac in Canada, GBP acquiring in the UK, PayNow in SGD in Singapore — configured rather than built, and without WuKong incorporating in each market.
> **Best Success Case:** Cross-border corridor framing; no same-vertical case exists in the library (see Success Case Alternatives).
> **Outreach Angle:** "You shipped iDEAL for the Netherlands, which is about 1% of your traffic. Canada is 5%, the UK is 3.6% and Singapore is 3.2% — and CAD, GBP and SGD aren't in your currency map at all."
> **Suggested Subject Line:** iDEAL for the Netherlands, nothing for Canada

> **Insight #4: A Hong Kong entity is billing American families, and the checkout says so.**
> **Evidence:** Section 2 — the Klarna US merchant of record is **WUKONG International (Hong Kong) Limited**; no confirmed billing entity in the US, Canada or Australia. Section 8 — the payment page carries the verbatim disclaimer *"Currency conversions may affect the actual amount. Please refer to third-party payment platforms for the actual payment amount."*
> **Pain Point:** A merchant that controlled presentment currency would not need to disclaim the final amount to the cardholder. That disclaimer is an admission of cross-border card processing: higher scheme fees, cross-border assessments, FX spread the merchant doesn't capture, and materially lower issuer approval rates on a large-ticket foreign transaction from an unfamiliar merchant descriptor.
> **Yuno Value Proposition:** Local acquiring against a US descriptor for US parents, AUD acquiring for Australian ones — removing both the cross-border fee stack and the foreign-transaction decline pattern, without WuKong changing its corporate structure.
> **Best Success Case:** NetEase Games.
> **Outreach Angle:** "Your own payment page tells parents you can't tell them what they'll actually be charged. That's what cross-border presentment looks like from the cardholder's side."
> **Suggested Subject Line:** "Currency conversions may affect the actual amount"

> **Insight #5: The SEA rails are already wired to Airwallex and surfaced to nobody — and SEA is real traffic.**
> **Evidence:** Section 3B — the dispatch switch handles `case"DANA": case"GCASH": case"KAKAO": case"TRUEMONEY": case"TNG":` by routing to `/aw/aw-add-params` with `method:"AIRWALLEX"`. Section 4 — **none of those five methods appears in the rendered method catalogue.** Section 1 — Indonesia **#9 (1.66%)**, Philippines **#11 (1.56%)**, Malaysia **#13 (1.37%)**, Thailand **#19 (0.95%)**: **~5.5% of traffic sitting on markets whose local rails they have already integrated and never exposed.**
> **Pain Point:** Someone built this and it stalled. ⚠️ **Be careful how hard you push it** — all four of those markets sit in the thin-engagement cohort (00:18–00:50 dwell, 1.37–1.87 pages/visit), so this is very likely blog traffic rather than enrolment demand today. The honest read is that the rails were built for an expansion that didn't convert, not that there is 5.5% of revenue going uncollected. That makes it a **discovery question about why it stalled**, which is more useful than a claim.
> **Yuno Value Proposition:** The reason single-PSP APM expansion stalls is that each market needs its own method set, currency, compliance posture and front end, and the merchant maintains all of it. Orchestration makes the market a configuration change rather than a project — which is exactly the difference between a rail that ships and a rail that sits in a switch statement.
> **Best Success Case:** Garena, for SEA rail coverage specifically — though note the payer base here is diaspora, not SEA-resident.
> **Outreach Angle:** *Use on a call, not in an email* — "you've got GCash, DANA, KakaoPay and TrueMoney wired through Airwallex but not surfaced in the method list. What happened to that expansion?"
> **Suggested Subject Line:** *(call question, not an email)*

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. "Your checkout ships `Credit/Debit Card` with `hide: true` and `(May Charge 3%)`, force-unhidden only for US buyers, while Bank Transfer is the only method tagged 'Recommend' in all four of your currencies — that's a decision someone made because the card economics outside the US stopped working."
2. "You've integrated Citcon, Airwallex, Latipay, PingPong and Stripe, and the routing between them is a single ternary on buyer country with no cascade — so a declined $1,349 enrolment has nowhere to go."
3. "You shipped iDEAL for the Netherlands, which is about 1% of your traffic — meanwhile Canada is 5%, the UK 3.6% and Singapore 3.2%, and CAD, GBP and SGD aren't in your currency map at all."

**Cold call openers (conversational, one sentence each):**
1. "I read your payment gateway's front-end code — specifically the bit where card is hidden by default everywhere except the US. Can I ask what drove that?"
2. "You're running five acquirers. What happens today when Citcon declines a US card at two thousand dollars — does anything catch it, or does the parent just get a failure screen?"
3. "Your payment page tells parents that currency conversion may change what they actually get charged. How much of your support load is that one sentence?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| **LingoAce** | lingoace.com | 🇸🇬 Singapore | ~1,300–4,000 staff (sources conflict); $180M raised, $105M Series C (Sequoia India, Owl, Shunwei); 580k+ learners | US, SG, SEA, global diaspora | **No PSP named publicly.** Methods confirmed: Visa/MC/Amex/**UnionPay**, WeChat Pay, Alipay, bank transfer, **PayNow/PayLah/NETS**, **Atome** (APAC BNPL), **Affirm** (US BNPL) | [payment agreement](https://www.lingoace.com/lingoace-payment-agreement-foundation-1v1/) (fetched, 149,495 bytes) · [CB Insights](https://www.cbinsights.com/research/lingoace-series-c-funding/) |
| **AmazingTalker** | en.amazingtalker.com | 🇹🇼 Taiwan | Not established | TW, HK, JP, KR, global | PayPal + Visa/MC/Amex. Processor not named. | [help centre](https://amazingtalker.elevio.help/en/articles/223-how-can-i-pay-for-amazingtalker) `[UNVERIFIED]` |
| **LingoBus** (VIPKid) | lingobus.com | 🇨🇳 China | Not established | Overseas Chinese families | Nothing found | [comparison](https://www.mamababymandarin.com/lingoace-or-lingo-bus-online-chinese-classes/) |
| **PandaTree** | pandatree.com | 🇺🇸 USA | Small | US | Nothing found | [via LingoAce](https://www.lingoace.com/guides/compare/wukong-education-vs-pandatree-which-online-chinese-class-is-best-in-2026/) |
| **Outschool** | outschool.com | 🇺🇸 USA | Large | US | Nothing found | [via LingoAce](https://www.lingoace.com/guides/compare/wukong-education-outschool/) |

❌ **Not verified, do not use without checking:** iTutorGroup, Talkbean, HSK Academy, Panda Chinese, eChineseLearning, Chinese Buddy, GoEast Mandarin, Superprof, Cambly.

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| **51Talk** (NYSE: COE) | 51talk.com | Online language tutoring | Global incl. MENA, SEA | **The single best public disclosure of this payment shape.** Its FY2024 20-F names **Airwallex, Stripe, Checkout.com, 2C2P, PayerMax, Tabby and Tamara** — seven processors run side by side — and lists rising interchange, fraud exposure across heterogeneous methods, and counterparty risk ("could not guarantee that all such platforms will timely and fully transfer collected payments") **as risk factors**. That is a merchant describing orchestration's problem statement in a regulatory filing. ⚠️ *Inverse model — 51Talk sells English to learners outside China. And the processor list came from consistent search summaries of the filing; the SEC document itself was not fetched.* | [SEC 20-F FY2024](https://www.sec.gov/Archives/edgar/data/1659494/000141057825000918/coe-20241231x20f.htm) |
| **Preply** | preply.com | Tutoring marketplace | Global | **Braintree, PayPal, Stripe** + payouts via Wise/Payoneer/PayPal/Skrill — three processors, four payout rails | [help centre](https://help.preply.com/en/articles/4182730-accepted-payment-methods-on-preply) `[UNVERIFIED]` |
| **italki** | italki.com | Tutoring marketplace | Global | Card, **PayPal, Skrill, Apple Pay, UnionPay, Alipay**; WeChat only on italki.cn — same diaspora wallet pattern as WuKong | [help centre](https://support.italki.com/hc/en-us/articles/217489907) `[UNVERIFIED]` |

**The cohort pattern, and why it matters for this pitch:** every comparable is running **self-assembled per-market PSP stacks, not orchestration**. LingoAce splits policy *by jurisdiction* with a different BNPL per region (Atome in APAC, Affirm in US) alongside SG domestic rails and China wallets — different BNPL vendors per region almost always means different acquiring behind them. **UnionPay + Alipay/WeChat Pay are near-universal** across the cohort, confirming that the diaspora parent often still holds a mainland instrument. Nobody has consolidated. WuKong is not behind its peers — **none of them has solved this**, which means the orchestration conversation is a category-first conversation in this vertical, not a catch-up one.

#### 11C. Companies Recently Adopting Payment Orchestration

*No public case studies found of direct competitors adopting payment orchestration.* Searches across LingoAce, AmazingTalker, LingoBus, PandaTree, Outschool, Preply, italki and 51Talk returned **zero** references on Primer, Gr4vy, Spreedly, Corefy or Yuno. 51Talk's PayerMax is a cross-border PSP/aggregator, not an orchestrator — seven processors run in parallel is the *pre*-orchestration state.

**Consequence for the ICP score:** the "competitor using orchestration" signal scores 0, and **there is no competitive-urgency angle available**. Do not manufacture one.

#### 11D. Prospect Scoring

Not run — Agent 5's budget went to establishing the cohort's payment stacks, which was the higher-value question. Scoring the competitors properly needs a dedicated pass.

#### Top Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | **LingoAce** | Direct competitor | SG, US, SEA | Not scored | **Genuine find** | Jurisdiction-split payment policy, region-swapped BNPL (Atome APAC / Affirm US), SG domestic rails, $180M raised, **Singapore HQ = squarely in territory** | ❌ **Not on the TAL — add it** |
| 2 | **AmazingTalker** | Direct competitor | TW, HK, JP, KR | Not scored | Medium | Taiwan HQ, multi-market North Asia footprint, processor unknown | ❌ Not on the TAL |
| 3 | **51Talk** | Peer | SEA, MENA, global | Not scored | Medium | Seven processors named in an SEC filing, with the pain written up as a risk factor | ❌ Not on the TAL — *but check territory: MENA exposure may put part of it with EMEA* |

> **LingoAce is the strongest genuine find in this run.** Singapore-HQ'd, in territory, $180M raised, and running a per-jurisdiction payment policy with different BNPL vendors per region — the exact profile orchestration is built for. It is not on `accounts/apac-tal.csv`.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | **Not found.** The `~$100M est.` on the TAL is supported by **no public source** — neither confirmed nor refuted | TAL row is a lead, not a fact |
| GMV / Gross Transaction Volume | Not found | — |
| Average Transaction Value (USD) | **$349–$2,039 per package**, ~$20–30/lesson; $349 = 12 sessions, $1,349 = 60 sessions; one independent parent review cites "$2,800+ for a year" | [company blog](https://www.wukongsch.com/blog/complete-guide-to-wukong-chinese-post-28985/) · [myengineeringbuddy](https://www.myengineeringbuddy.com/blog/wukong-tutoring-reviews-alternatives-pricing-offerings/) · [joshuawwy](https://joshuawwy.com/c/2026/a/wukong-review) — **all `[UNVERIFIED — search summary only]`** |
| Est. Annual Transactions | `[ESTIMATE, not confirmed]` **~40,000–100,000 package purchases/yr** *if* the $100M line is real | Our arithmetic: $100M ÷ $1,000–$2,500 average package. **A derivation from an unverified input — a discovery question, not a number.** The supplied SimilarWeb view carried no total-visits figure, so there is no denominator to cross-check it against either. |
| Active Customers / Users | Self-reported and mutually inconsistent: "300,000 families" / "400,000 families" / "nearly one million families" (cumulative, not active). 50K+ Android installs. 4,500 teachers. | [9th-anniversary PR](https://www.prnewswire.com/news-releases/from-one-online-classroom-to-400-000-families-wukong-education-marks-its-9th-anniversary-with-a-growing-global-vision-302593777.html) · [Frost & Sullivan PR](https://www.prnewswire.com/news-releases/wukong-chinese-ranked-no1-globally-based-on-cumulative-paying-users-according-to-frost--sullivan-302687368.html) · Google Play (fetched) |
| Primary Currency | **USD.** Also live: AUD, NZD, CNY. **Not live: CAD, SGD, GBP, HKD, EUR, MYR, JPY** | Checkout currency map, verified directly |
| Top 3 Markets by Revenue | **Not found.** Best available proxy is traffic: **US 43.89%, Canada 5.13%, Australia 4.07%**, then UK 3.61% and Singapore 3.17%. ⚠️ Traffic is not revenue, and nine of the top 20 markets are thin-engagement SEO traffic — see the engagement split in Section 1 before using any share as volume. | SimilarWeb (supplied 2026-09-14) |
| **Billing channel split (web vs app store)** | **Web/pay-link dominant. `[INFERENCE, not confirmed]` — but well supported.** The sale is advisor-led and closed on a consultant-issued `pay.wukongsch.com` link; the apps are a learning portal (`com.wukongacademy.studentportal`), and **no IAP product tiers or store-billing evidence surfaced**. Contrast YuppTV, where Apple IAP was found live with fetched price tiers. | [Google Play](https://play.google.com/store/apps/details?id=com.wukongacademy.studentportal) · [pay.wukongsch.com](https://pay.wukongsch.com/) |

> **This account does not fail the app-store test.** The revenue that matters runs through a web pay link WuKong controls end to end, which is exactly the volume orchestration can touch. **No downward override on app-store grounds.**

---

### Overall Research Confidence

**High on infrastructure, Medium on the commercials.**

**Very strong (higher confidence than any account in the pipeline so far):** the PSP stack, the orchestration classification, the method catalogue, the currency map and the country gating. All of it comes from **primary source code** on a live, fetchable host, independently re-fetched and re-grepped by me rather than taken on an agent's word. The `hide:!0` flags, the `"Recommend"` tag on bank transfer, the `(May Charge 3%)` label, the `citcon`/`aw` ternary and the four-entry currency map were each verified a second time. There is no ambiguity in Sections 3, 4 and 8.

**Now strong: the country profile.** Traffic was **supplied by Prateek as a SimilarWeb pull** (`wukongsch.com`, Jun–Aug 2026, all country domains ON, 60 countries) — resolution path 1, the primary source under the method. Shares, trends and engagement metrics are all first-party from that pull. This converted three previously unscoreable ICP signals and raised the tier from 🟢 12/24-with-override to a clean ⭐ 14/24.

**Still weak: entities, financials, and absolute volume.**
- **The supplied view carried no total-visits figure**, so we have country shares without a denominator. Absolute per-market visits are not stated anywhere in this report and must not be back-computed from the stale ~317.6K/mo search-summary estimate.
- **The billing entity per market is not established.** `/terms/` and `/policy/` sit behind a Vercel checkpoint and `/terms/` has no Wayback snapshot. Only the Klarna slug tells us a Hong Kong entity bills US families, and that is single-source.
- **Revenue is entirely unconfirmed.** The `~$100M est.` on the TAL should be treated as a hypothesis.
- **Trustpilot's ~943–1,000 reviews were never read** (403 / AWS WAF). The complaint picture rests on 109 directly-read iOS reviews plus search snippets.

**Not downgraded for environment.** Network access was Full and `curl` worked throughout; the blocks were the target's own Vercel checkpoint and AWS WAF, not an egress policy. The residual Medium rating is driven entirely by unsourced revenue and the unread terms/privacy pages — both closable by hand, see below.

---

### Manual Research Recommendations

> ✅ **CLOSED — Traffic split.** Supplied by Prateek 2026-09-14 and saved to [`accounts/traffic/wukong-education.md`](../accounts/traffic/wukong-education.md). Correct domain, all country domains ON, no double-count. It landed at the bottom of the predicted 14–15/24 range and took the account to ⭐ on arithmetic. **One thing it did not carry: a total-visits figure** — worth re-capturing from the same SimilarWeb view if a business case needs absolute numbers.

> **Area:** The privacy policy and terms of service.
> **Why it matters:** APAC merchants name their processor in the privacy policy far more often than anywhere else, and the terms would settle which entity bills which market — the single biggest gap in this report.
> **Suggested manual action:** Open `https://www.wukongsch.com/policy/` and `https://www.wukongsch.com/terms/` in a normal browser (the Vercel checkpoint passes a real browser, it only blocks automated fetches). Grep for entity names, "processor", "payment", and any PCI statement.

> **Area:** A live checkout, rendered.
> **Why it matters:** Everything in Section 4 is the routing table, not an observed method list. Which methods actually render for a Canadian or Singaporean parent is the difference between a sharp email and a wrong one.
> **Suggested manual action:** Book a free trial, let an advisor issue a real order link, then open it with DevTools — ideally twice, once on a US IP and once on an AU or SG IP. Capture the rendered method list and the network calls. This would also confirm 3DS.

> **Area:** Annual card volume.
> **Why it matters:** We now have country *shares* but no *denominator* — the supplied SimilarWeb view carried no total-visits figure, and revenue is unsourced. At a $349–$2,039 ticket the business case is entirely a function of transaction count.
> **Suggested manual action:** Ask directly on the first call. Frame it as sizing the approval-rate uplift, not as qualification.

> **Area:** The `jpmorgan-*-uat` subdomains.
> **Why it matters:** If it is bank host-to-host connectivity in test, there is an active payments/treasury workstream and an internal owner for it right now.
> **Suggested manual action:** Ask on a call — "are you building direct bank connectivity?" Do **not** put the subdomain names in an email; reading someone's CT logs back to them lands badly even though the data is public.

> **Area:** LingoAce.
> **Why it matters:** Singapore-HQ'd, in territory, $180M raised, per-jurisdiction payment policy, and **not on the TAL**.
> **Suggested manual action:** Add to `accounts/apac-tal.csv` and queue a research run. Its checkout sits behind `student.lingoace.com` login, so it will need the same trial-and-DevTools approach.

---

### Appendix: All Source URLs

**Supplied by Prateek**
- SimilarWeb, `wukongsch.com`, Jun–Aug 2026, all traffic, "Include all country domains" ON, 60 countries (screenshot, 2026-09-14) → saved at `accounts/traffic/wukong-education.md`

**Primary — fetched directly and verified by me**
- https://pay.wukongsch.com/
- https://pay.wukongsch.com/_next/static/chunks/1306-d238e146e95b80e3.js
- https://pay.wukongsch.com/_next/static/chunks/pages/index-091bbfd821769875.js
- https://pay.wukongsch.com/_next/static/chunks/4426-300d526150b40c9e.js
- https://pay.wukongedu.net/ (byte-identical to the above)
- https://www.wukongsch.com/robots.txt
- https://www.wukongedu.net/robots.txt (declares `Host: https://www.wukongsch.com/`)
- https://student.wukongsch.com/
- https://crt.sh/?q=%25.wukongsch.com
- https://crt.sh/?q=%25.wukongedu.net
- https://www.klarna.com/us/store/cb7b6231-09fb-4c35-af44-f1f1c9f2eaaa/WUKONG-International-(Hong-Kong)-Limited/pay-with-klarna/
- https://www.klarna.com/au/store/7032fca8-aa22-4700-bd38-9d78de66bcf8/WuKong-Education/pay-with-klarna/ — **302s to the store directory; does not resolve**
- https://play.google.com/store/apps/details?id=com.wukongacademy.studentportal
- https://apps.apple.com/us/app/id1574837622
- https://www.lingoace.com/lingoace-payment-agreement-foundation-1v1/
- https://www.lingoace.com/pricing/

**Company statements / PR**
- https://www.prnewswire.com/news-releases/wukong-chinese-ranked-no1-globally-based-on-cumulative-paying-users-according-to-frost--sullivan-302687368.html
- https://www.prnewswire.com/news-releases/from-one-online-classroom-to-400-000-families-wukong-education-marks-its-9th-anniversary-with-a-growing-global-vision-302593777.html
- https://www.prnewswire.com/news-releases/wukong-education-named-to-the-2025-gsv-150-for-leading-the-way-in-education-technology-302338883.html
- https://www.prnewswire.com/apac/news-releases/international-business-simulation-debuts-in-australia-four-teams-qualify-for-global-finals-in-shanghai-302772317.html
- https://www.wukongsch.com/zh/aboutus/
- https://www.wukongsch.com/blog/complete-guide-to-wukong-chinese-post-28985/

**Entity / financial — `[UNVERIFIED — search summary only]`**
- https://www.companyhub.nz/companyDetails.cfm?nzbn=9429043350629
- https://www.bizdb.co.nz/company/9429043350629/
- https://www.bizprofile.net/ca/mountain-view/smart-learner-international-corporation
- https://www.sgpbusiness.com/company/Smart-Learner-International-Pte-Ltd
- https://recordowl.com/company/smart-learner-international-pte-ltd
- https://www.crunchbase.com/organization/wukong-education — ❌ funding data contaminated, do not use
- https://www.cbinsights.com/company/wukong-education — ❌ same
- https://pitchbook.com/profiles/company/518434-57

**Complaints — `[UNVERIFIED — search summary only]`, Trustpilot 403/WAF**
- https://www.trustpilot.com/review/wukongsch.com
- https://ca.trustpilot.com/review/wukongsch.com?page=2
- https://au.trustpilot.com/review/wukongsch.com?page=3
- https://joshuawwy.com/c/2026/a/wukong-review
- https://www.myengineeringbuddy.com/blog/wukong-tutoring-reviews-alternatives-pricing-offerings/

**Competitors**
- https://www.sec.gov/Archives/edgar/data/1659494/000141057825000918/coe-20241231x20f.htm — ⚠️ not fetched; processor list is from consistent search summaries
- https://www.cbinsights.com/research/lingoace-series-c-funding/
- https://amazingtalker.elevio.help/en/articles/223-how-can-i-pay-for-amazingtalker
- https://help.preply.com/en/articles/4182730-accepted-payment-methods-on-preply
- https://support.italki.com/hc/en-us/articles/217489907
- https://www.mamababymandarin.com/lingoace-or-lingo-bus-online-chinese-classes/

**Unreachable**
- https://www.wukongsch.com/ — 429 Vercel Security Checkpoint
- https://www.wukongsch.com/policy/ — 429
- https://www.wukongsch.com/terms/ — 429; **no Wayback snapshot**
- https://www.wukongsch.com/faq/ — 429
- https://booking.wukongsch.com/ — CONNECT 502
- https://cp-gateway.wukongsch.com/ — TLS certificate expired
- https://en.amazingtalker.com/payment — HTTP 202, bot challenge, 0 bytes

**❌ Discarded as different companies:** `wukong.com` (小悟空 AI assistant) · "Black Myth: Wukong" (video game)

</details>
