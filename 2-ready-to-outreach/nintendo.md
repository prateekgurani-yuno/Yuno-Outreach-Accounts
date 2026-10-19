# Nintendo

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 22 / 29 → ⭐ High Priority *(no formal override, but read the "Reality check" in the ICP breakdown: an enterprise account with an in-house payment platform, so expect a long cycle)*
**Industry:** Gaming. Console maker and publisher, running its own first-party digital store (Nintendo eShop) and web shop (Nintendo Store) · **HQ:** Kyoto, Japan. Nintendo Co., Ltd. (任天堂株式会社), 11-1 Hokotate-cho, Kamitoba, Minami-ku · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **In-house.** Nintendo runs its own payment platform (internal services `SHOGUN` / `KANAT` / `WHARF` in its production code), with Adyen as the confirmed card PSP and PayPal, Alipay+ (KakaoPay) and Paidy integrated directly. Never pitch "you need orchestration." Pitch the cost of adding each country's rails one integration at a time, and what that cost has left uncovered on the console eShop across APAC.

---

> ## 🎯 THE HOOK: Nintendo's own job ad describes the problem, and its own support pages show the gap
>
> **Nintendo Systems (the Nintendo × DeNA JV) is hiring a server engineer for the Nintendo Store and eShop payment platform.** The listing was last updated 2026-06-09 ([herp.careers](https://herp.careers/careers/companies/nscareer/jobs/6fWhZUEJvoag), fetched). Verbatim:
> *「グローバルにサービス展開するNintendo Storeおよびニンテンドーeショップでは、各国の事情に応じた決済手段の提供が不可欠です。…社外サービスとの連携や各国のリーガル要件への対応など決済ドメインに固有な特性があります。」*
> ("For the globally deployed Nintendo Store and eShop, offering payment methods suited to each country's circumstances is essential … the payments domain has its own characteristics, such as integration with external services and handling each country's legal requirements.")
>
> **And this is what that platform currently offers on the console eShop in APAC.** Each row is Nintendo's own support page, fetched 2026-10-19:
>
> | Market | Console eShop top-up methods: Nintendo's complete list | Absent |
> |---|---|---|
> | 🇯🇵 Japan | 「次の3つの方法」 ("the following 3 methods"): credit card, prepaid card/number, PayPal | PayPay, konbini payment, carrier billing (d払い/au/SoftBank), Rakuten Pay |
> | 🇰🇷 Korea | KakaoPay **"(Alipay+ Partner)"** and prepaid. The card and PayPal text is commented out in the page source | Naver Pay, Toss, any direct domestic card |
> | 🇭🇰 Hong Kong | 信用卡 (credit card), 預付卡 (prepaid card) | AlipayHK, Octopus, FPS, PayPal |
> | 🇹🇼 Taiwan | 信用卡 (credit card) only | JKOPay, LINE Pay, convenience-store payment |
>
> **The timing signal:** on 2026-08-07 Nintendo added Paidy, Apple Pay and Google Pay to the Japan **web** Nintendo Store. The same notice says they **cannot be used in the console eShop**, for Nintendo Switch Online plans or for pre-orders ([nintendo.com/jp](https://www.nintendo.com/jp/topics/article/ab5aebd2-e3b0-4918-a5b8-2a881f8cf24a), fetched). The platform is adding rails now, but one channel at a time, and none have reached the console, which carries the digital revenue.
>
> **Who to frame it around:** Nintendo Co., Ltd. in Kyoto is the seller of record for eShop content in Japan, Korea, Hong Kong, Taiwan and the new Singapore/Malaysia/Thailand eShops (Nintendo Account agreements, §2). APAC payments for every market except ANZ are decided in Kyoto.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Nintendo designs the Switch / Switch 2 consoles and publishes Mario, Zelda and Pokémon titles. It sells digital content through its **own** eShop (console and web) and physical goods through the Nintendo Store. FY3/2026 net sales were ¥2,313.1bn, of which **¥407.6bn was digital sales** ([IR](https://www.nintendo.co.jp/ir/pdf/2026/260508e.pdf)). Japan is 23.1% of sales and 76.9% comes from outside Japan.

**SimilarWeb total visits (last full month):** ≈70.0M/month on average across nintendo.com and nintendo.co.jp (68.56M + 1.433M, Jul–Sep 2026 average). Source: SimilarWeb (supplied 2026-10-19). **App-heavy caveat:** this counts web traffic only. Console eShop purchases, mobile apps and retail are not in it, so web traffic is a market-mix signal and says nothing about payment volume.

### Top 5 markets
Ranked by supplied web traffic. Only Japan is in territory; the APAC markets follow below.

| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇺🇸 United States *(out of territory)* | 30.0% | Card, PayPal (18+), prepaid eShop card | Not assessed: out of territory | ✅ Nintendo of America Inc. |
| 2 | 🇯🇵 **Japan** | 23.3% | eShop: card, prepaid, PayPal. Web Store also has Paidy, Apple Pay, Google Pay (since 2026-08-07) | **PayPay, konbini payment, carrier billing on the console eShop**; foreign-issued cards blocked since 2025-03-25 | ✅ Nintendo Co., Ltd. (seller of record) |
| 3 | 🇨🇦 Canada *(out of territory)* | 4.4% | Card, PayPal, prepaid | Not assessed | ✅ Nintendo of Canada Ltd. |
| 4 | 🇬🇧 UK *(out of territory)* | 4.3% | Store: cards, PayPal, Apple Pay, Google Pay | Not assessed | ⚠️ Covered by Nintendo of Europe SE (DE); UK entity not confirmed |
| 5 | 🇩🇪 Germany *(out of territory)* | 4.3% | Card (Adyen), PayPal | Not assessed | ✅ Nintendo of Europe SE |

### APAC markets (where the pitch actually is)
| Market | Traffic | Console eShop methods | Missing methods | Entity / seller of record |
|---|---|---|---|---|
| 🇰🇷 Korea | 1.8% | KakaoPay (Alipay+ Partner), prepaid | Naver Pay, Toss, direct domestic cards | ⚠️ Nintendo of Korea exists, but the **seller is Nintendo Co., Ltd. (Japan)** |
| 🇦🇺 Australia / NZ | ≥0.02% (only in nintendo.co.jp's top 10) | Card (same-country issuer), PayPal, eShop card. Physical Store is VISA/MC only | Afterpay/Zip, PayTo, Apple/Google Pay | ✅ Nintendo Australia Pty Ltd (ACN 060 566 083) is the seller |
| 🇭🇰 Hong Kong | Not in top 10 | Credit card, prepaid | AlipayHK, Octopus, FPS, PayPal | ⚠️ Nintendo (HK) Ltd exists; seller is NCL (Japan) |
| 🇹🇼 Taiwan | Not in top 10 | Credit card only | JKOPay, LINE Pay, convenience store | ⚠️ Nintendo of Taiwan exists; seller is NCL (Japan) |
| 🇸🇬🇲🇾🇹🇭 SG / MY / TH | Not in top 10 | eShop launched 2025-11-18; **methods not found** (support pages return 403) | Unknown, not proven absent | ⚠️ Nintendo Singapore Pte. Ltd. (est. 2025-09-26); seller is NCL (Japan) |
| 🇮🇩 Indonesia | 0.9% of .co.jp (≥0.02% combined) | No local eShop found | — | ❌ No entity |

### Legal entities
- Nintendo Co., Ltd. (Japan). Corporate number 1130001011420 `[UNVERIFIED — search summary only]`
- Nintendo Sales Co., Ltd. (Japan, domestic sales)
- Nintendo of Korea Co., Ltd. (Korea)
- Nintendo (Hong Kong) Limited (Hong Kong)
- Nintendo of Taiwan Co., Ltd. (Taiwan)
- Nintendo Australia Pty Limited (Australia). ACN 060 566 083
- Nintendo Singapore Pte. Ltd. (Singapore). Est. 2025-09-26, capital SGD 8M
- Nintendo Thailand Co., Ltd. (Thailand). Est. ~2025-11-17 `[UNVERIFIED — search summary only]`
- Nintendo of America Inc., Nintendo of Canada Ltd., Nintendo of Europe SE (out of territory)

### Known PSPs
- **Adyen**: `[Source Code]`, from error codes `EXTERNAL_ERROR_ADYEN_PSP_*` in the global ec.nintendo.com bundle. Also `[Terms/Privacy Policy]`: the EU Nintendo Store names Adyen RevenueProtect. Confirmed for Europe; the region split elsewhere is not proven.
- **PayPal**: `[Source Code]` + `[Terms/Privacy Policy]`, stored billing agreement (global, incl. JP/AU/Americas)
- **Alipay+ → KakaoPay**: `[Checkout docs]`, Nintendo KR support page (Korea)
- **Paidy**: `[Press Release]` (Japan, web Store only, since 2026-08-07)
- **Apple Pay / Google Pay**: `[Press Release]` + `[Source Code]` (JP web Store, US/EU Store)
- No Japanese gateway (GMO-PG, SBPS, Veritrans, KOMOJU) found. **The Japan card acquirer is unknown.**

### Orchestration status
**In-house orchestration layer.** The ec.nintendo.com production bundle maps errors from Nintendo's own backend services: `SHOGUN` (catalogue and purchasing), `KANAT` (card payment, e.g. `kanat.error.vcspas_card_declined`), `WHARF` (payment-method and token handling, e.g. `payment_country_restricted`), `ZENITH` (prepaid) and `BATTERA` (balance). External PSPs are called underneath. Nintendo Systems is hiring for exactly this platform. No Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails or Yuno found. Note it is an **abstraction layer with one card PSP visible, not a multi-acquirer router**: no evidence of routing between acquirers.

### Buying signals
- 🚀 **Southeast Asia eShop and Switch Online launched in Singapore, Malaysia and Thailand on 2025-11-18**; the Philippines is "being worked on" ([nintendo.com/sg](https://www.nintendo.com/sg/news/article/tngPVu8X1gJcAMRvRJR7M)). Nintendo Singapore was set up on 2025-09-26 for "accelerating business in Southeast Asia" ([release](https://www.nintendo.co.jp/corporate/release/en/2025/250930.html)).
- 💼 **Nintendo Systems is hiring a payment-platform server engineer** for the Store and eShop; listing updated 2026-06-09 ([herp.careers](https://herp.careers/careers/companies/nscareer/jobs/6fWhZUEJvoag)). Nintendo of America posted "Manager, Payments" (Payments & Fraud, Redmond) on 2026-05-07, covering authorization rates and payment cost and coordinating with NCL `[UNVERIFIED — job page now returns 500]`.
- 🤝 **New rails in Japan on 2026-08-07**: Paidy, Apple Pay and Google Pay on the web Nintendo Store, Nintendo's first pay-later offering ([Nintendo JP](https://www.nintendo.com/jp/topics/article/ab5aebd2-e3b0-4918-a5b8-2a881f8cf24a), [paymentnavi](https://paymentnavi.com/paymentnews/177233.html)).
- 📋 **Japan fraud lockdown**: since 2025-03-25 the JP eShop and Store refuse overseas-issued cards and PayPal accounts "to prevent fraudulent use" ([Nintendo Life](https://www.nintendolife.com/news/2025/01/japans-switch-eshop-will-soon-no-longer-accept-overseas-payment-methods), [inside-games](https://www.inside-games.jp/article/2025/01/30/163843.html)). A blunt geo-block rather than risk-based routing.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Nintendo` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 22 / 29
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | +5 | ✅ DERIVED (floor): **≥340,000/month at an absurd ceiling; realistically millions.** FY3/2026 digital sales ¥407.6bn ÷ 12 = ¥34.0bn/month ([IR](https://www.nintendo.co.jp/ir/pdf/2026/260508e.pdf)). Even if every transaction averaged ¥100,000, about 20× a full-price game (Mario Kart World is $79.99 on the [US eShop](https://www.nintendo.com/us/store/products/mario-kart-world-switch-2/)), that is still ~340,000/month. The ceiling is a bound I chose, not a sourced ATV, but no plausible average ticket brings the count anywhere near 40,000. Billing unit: eShop purchases and balance top-ups. Third-party digital sales are booked net, so ¥407.6bn **understates** gross consumer spend. The 40k gate cannot fire. |
| Orchestration status | +1 | ✅ In-house layer (`SHOGUN`/`KANAT`/`WHARF` in the production bundle, plus Nintendo Systems' payment-platform hiring) |
| 3+ countries | +3 | ✅ 10 countries above 1% web traffic; 11+ legal entities |
| Multiple PSPs | +3 | ✅ Adyen, PayPal, Alipay+ (KakaoPay), Paidy, each with evidence |
| Local rail or licensing gap in a top-3 market | +3 | ✅ Japan (#2 market): Nintendo's own page lists exactly three console eShop top-up methods (card, prepaid, PayPal). PayPay, konbini payment and carrier billing are absent ([support.nintendo.com/jp](https://support.nintendo.com/jp/switch/eshop/purchase.html)). |
| Recent expansion | +2 | ✅ SG/MY/TH eShop and NSO launch on 2025-11-18 (within 12 months); Nintendo Thailand est. ~2025-11 |
| Payment issues reported | 0 | ⬜ Complaints are recurring but mostly US/UK and isolated. I read one forum thread in full ([Nintendo Life forum](https://www.nintendolife.com/forums/help/unable_to_make_payments), 2023: four cards from three banks plus PayPal all failing with 2813-2470; Nintendo's advice was to use eShop cards). Nothing APAC-specific found. Not enough for "moderate". |
| Funding >$10M | 0 | ❌ Listed company, no funding rounds |
| High traffic outside home | +2 | ✅ Japan is 23.3% of combined web traffic; 76.9% of sales come from outside Japan |
| Competitor using orchestration | +2 | ✅ NetEase Games is Yuno's named gaming customer ([y.uno gaming](https://y.uno/en/industries/gaming.md), fetched). Com2uS uses PortOne (repo file `2-ready-to-outreach/com2us.md`). |
| Payment job postings | +1 | ✅ Nintendo Systems payment-platform engineer (fetched, updated 2026-06-09) |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **⭐ High Priority (22)**
No public payment RFP found.

**Analyst override check: none applied, but here is the reality check.**
- *App-store trap: does NOT apply, and the traffic file's caveat needs a correction.* The supplied traffic note says most digital purchases happen "in the mobile apps and on the console eShop." The console eShop is **Nintendo's own store**: Nintendo is the merchant of record and bills through its own platform, not Apple or Google. Mobile IAP sits inside a much smaller line (IP-related income ¥73.5bn, which also includes film and licensing) next to digital sales of ¥407.6bn. So the account is web-and-console billed, which is orchestration-addressable. The caveat that web *traffic* understates *transactions* is correct.
- *Why not override down:* volume is enormous, and the rail gaps are on Nintendo's own pages, not inferred.
- *Why it will still be hard:* (1) there is a built in-house payment platform with a dedicated JV engineering team; (2) Adyen is very likely a strategic, multi-region relationship; (3) Nintendo is famously conservative, and decisions sit in Kyoto; (4) some gaps are console-UX choices, not PSP limitations: Korea already uses a QR-link flow for KakaoPay, so the console can support wallets. Treat as a multi-quarter enterprise play. Do not forecast it.
- *Double-counting:* "Multiple PSPs" and "3+ countries" are independent here: the PSPs are distinct integrations, not one regional split.

### Source Notes
- ✅ Adyen strings `EXTERNAL_ERROR_ADYEN_PSP_APL_ERROR` / `_INTERNAL_ERROR` are present in the ec.nintendo.com Next.js chunks (grep re-run by me, 2026-10-19)
- ✅ Adyen RevenueProtect is named verbatim in the EU Nintendo Store privacy policy (fetched)
- ✅ Japan has three eShop top-up methods; the Aug-2026 additions are excluded from the console eShop; Korea uses KakaoPay (Alipay+ Partner); HK and TW are card/prepaid only. All re-fetched by me from Nintendo support pages.
- ✅ Japan foreign-card block effective 2025-03-25 (Nintendo Life and inside-games, fetched)
- ✅ Nintendo Systems payment-platform job text (fetched)
- ⚠️ The Korea card/PayPal sections are commented out in the page HTML. I read this as disabled; confirm on a live console.
- ⚠️ Seller-of-record findings come from Nintendo Account agreements at accounts.nintendo.com/term/eula/{CC}, which the research agent pulled. The SG page is JavaScript-rendered and my own curl got an empty shell, so I have not re-verified it myself.
- ⚠️ NOA "Manager, Payments" listing: careers.nintendo.com/jobs/4140793009 now returns HTTP 500, so it rests on a search summary.
- ⚠️ Switch 2 life-to-date of 23.68M comes from the Q1 FY3/27 explanatory material via the research agent; not re-read by me.
- ⚠️ The words `fpx` and `jcb` match in the ec.nintendo.com bundle, but only inside base64 blobs. They are false positives and are not evidence of FPX or JCB.

### Success Case Alternatives
- **NetEase Games (Yuno customer)**: the only named Yuno gaming case. It is a large Asian game company serving "dozens of markets" with wallets, cash top-ups, gift cards and BNPL ([y.uno](https://y.uno/en/industries/gaming.md)). It matches the multi-market, wallet-heavy problem. It is a weaker match on the console-platform model; Nintendo is the store, not a publisher on one.

---

## Executive Summary

Nintendo is a ¥2.3tn-revenue Japanese console and game company that bills ¥407.6bn a year of digital sales through **its own** eShop. Nintendo Co., Ltd. in Kyoto is the seller of record for Japan, Korea, Hong Kong, Taiwan and the new Southeast Asian eShops. Its stack is an **in-house payment platform** (internal services visible in production code) calling Adyen for cards, plus direct PayPal, Alipay+ (KakaoPay in Korea) and, since August 2026, Paidy, Apple Pay and Google Pay on the Japan web store only. The gap is concrete and documented by Nintendo itself: the console eShop in Japan takes three methods, Korea one wallet, Hong Kong and Taiwan cards only, and the platform team's own job ad says per-country payment methods are "essential." Motion: **in-house**. Argue the opportunity cost and speed of reaching local rails across APAC through one integration, not the concept of orchestration.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** Supplied SimilarWeb (Sales Intelligence view), pulled 2026-10-19, period Jul–Sep 2026, file `accounts/traffic/nintendo.md`. Only the top 10 countries per domain were supplied. Per-country visits below are **[DERIVED from supplied share, not a SimilarWeb figure]**: share × domain average monthly visits, summed across domains, with shares recalculated on the combined 69.99M.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | United States | 30.01% | 21.0M | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | **Japan** ⭐ | 23.25% | 16.3M | Not supplied | " |
| 3 | Canada | 4.41% | 3.09M | Not supplied | " |
| 4 | United Kingdom | 4.31% | 3.02M | Not supplied | " |
| 5 | Germany | 4.28% | 2.99M | Not supplied | " |
| 6 | France | ≥3.71% | ≥2.60M | Not supplied | " (top 10 of .com only) |
| 7 | Mexico | 3.31% | 2.31M | Not supplied | " |
| 8 | Spain | 2.71% | 1.90M | Not supplied | " |
| 9 | Brazil | ≥2.17% | ≥1.52M | Not supplied | " (top 10 of .com only) |
| 10 | **South Korea** | 1.84% | 1.29M | Not supplied | " |
| — | Australia | ≥0.02% | ≥14k | — | top 10 of .co.jp only; its nintendo.com share is unknown but <1.84% |
| — | Indonesia | ≥0.02% | ≥13k | — | top 10 of .co.jp only |

- Combined: **69.99M visits/month**. nintendo.com is 75.6% mobile web, and regional paths (/us, /au, /sg, /jp) sit under nintendo.com. Regional domains such as nintendo.co.kr and nintendo.com.hk were not supplied.
- **High priority (>5%) in territory: Japan only.** All other >1% markets except Korea are outside APAC.
- **App-heavy caveat (from the traffic file):** console eShop, mobile app and retail activity are not captured. Do not size payments from this.
- Every top-10 market has a Nintendo entity except France, Spain, Mexico and Brazil, which are served by NoE/NoA. All of those are out of territory.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Kyoto, Japan. Nintendo Co., Ltd., 11-1 Hokotate-cho, Kamitoba, Minami-ku, Kyoto 601-8501. Capital ¥10,065.4M; 8,666 group employees (end Mar 2026). ([corporate profile](https://www.nintendo.co.jp/corporate/en/outline/index.html), [securities report FY3/2026](https://www.nintendo.co.jp/ir/pdf/2026/security_q2603.pdf))

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Japan | Nintendo Co., Ltd. (任天堂株式会社) | Corporate no. 1130001011420 `[UNVERIFIED — search summary only]` | [Securities report](https://www.nintendo.co.jp/ir/pdf/2026/security_q2603.pdf) |
| Japan | Nintendo Sales Co., Ltd. (任天堂販売㈱) | Not found (capital ¥300M) | Securities report |
| South Korea | Nintendo of Korea Co., Ltd. | Not found (capital KRW 25,000M) | [Corporate profile](https://www.nintendo.co.jp/corporate/en/outline/index.html) |
| Hong Kong | Nintendo (Hong Kong) Limited | Not found (capital HK$49.3M) | Corporate profile |
| Taiwan | Nintendo of Taiwan Co., Ltd. | Not found (capital NT$5M) | Corporate profile |
| Australia / NZ | Nintendo Australia Pty Limited | ACN 060 566 083 | [AU/NZ Nintendo Account Agreement](https://accounts.nintendo.com/term/eula/AU?lang=en-US) |
| Singapore | Nintendo Singapore Pte. Ltd. | Not found (est. 2025-09-26, SGD 8M) | [Nintendo release 2025-09-30](https://www.nintendo.co.jp/corporate/release/en/2025/250930.html) |
| Thailand | Nintendo Thailand Co., Ltd. | Not found (est. ~2025-11-17, THB 22M) | `[UNVERIFIED — search summary only]` [VGChartz](https://www.vgchartz.com/article/466355/nintendo-establishes-nintendo-thailand/) |
| China | 神游科技有限公司 (iQue), development role only | Not found | Securities report |
| USA / Canada / Germany | Nintendo of America Inc. / Nintendo of Canada Ltd. / Nintendo of Europe SE | Not researched | Securities report |

**Seller of record for eShop content** (Nintendo Account agreements):

| Region | Seller | Source |
|---|---|---|
| Japan | Nintendo Co., Ltd. | [eula/JP](https://accounts.nintendo.com/term/eula/JP?lang=ja-JP) |
| Korea | 닌텐도주식회사 (Nintendo Co., Ltd.), **not** Nintendo of Korea | [eula/KR](https://accounts.nintendo.com/term/eula/KR?lang=ko-KR) |
| Hong Kong / Taiwan | Nintendo Co., Ltd. | [eula/HK](https://accounts.nintendo.com/term/eula/HK?lang=en-US), [eula/TW](https://accounts.nintendo.com/term/eula/TW?lang=zh-TW) |
| SG / MY / TH / PH (EN-SEA, effective 2025-11-17, updated 2026-07-21) | Nintendo Co., Ltd., Japanese law, Kyoto District Court | [eula/SG](https://accounts.nintendo.com/term/eula/SG?lang=en-US) |
| Australia / NZ | **Nintendo Australia Pty Ltd** ("NAL is the seller … NCL is not the seller") | [eula/AU](https://accounts.nintendo.com/term/eula/AU?lang=en-US) |
| India / other | Nintendo Co., Ltd. (generic agreement) | [eula/IN](https://accounts.nintendo.com/term/eula/IN?lang=en-US) |

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| Japan | Yes (#2) | ✅ NCL is the seller | N/A, home market | Low. Foreign cards are blocked outright instead |
| South Korea | Yes (#10) | ⚠️ Entity exists, but the seller is NCL (Japan) | Not verified for this case; check the current rule | **Yes** `[INFERENCE, not confirmed]`: a Japanese seller, with the only local wallet routed through Alipay+, a cross-border wallet network |
| Singapore / Malaysia / Thailand | No | ⚠️ SG entity (TH reported), seller is NCL (Japan) | Not verified | **Likely** `[INFERENCE, not confirmed]`: the SEA eShop is sold from Kyoto |
| Hong Kong / Taiwan | No | ⚠️ Entities exist, seller is NCL (Japan) | Not verified | Likely `[INFERENCE, not confirmed]` |
| Australia / NZ | Partial | ✅ NAL is the seller | No | Low |
| Indonesia / India / Philippines / Vietnam | ID only, via .co.jp | ❌ | Not verified | No local eShop found (PH "being worked on"; Indonesia hardware reportedly Dec 2026 `[UNVERIFIED]`) |

> *Warning: Potential cross-border operation in South Korea. Korea is a top-10 traffic market where the seller of record is the Japanese parent, not Nintendo of Korea, and the only local rail runs through Alipay+. Transactions are likely processed cross-border, with higher scheme costs, lower approval rates and FX exposure.* `[INFERENCE, not confirmed]`. The acquirer for Korean transactions was not found.

> *Regulatory gate check:* the APAC reference flags Korea as a market where domestic acquiring is effectively gated by local presence. **I did not find a current source**, so it is not cited as fact and no ❌🔒 is applied.

> **MANUAL:** Check which entity appears on a Korean and a Singaporean eShop receipt or card statement descriptor.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Global eShop web (region split unproven) | **Adyen**: `EXTERNAL_ERROR_ADYEN_PSP_APL_ERROR` ("5912"), `EXTERNAL_ERROR_ADYEN_PSP_INTERNAL_ERROR` ("5922") | [Source Code] | https://ec.nintendo.com/ (Next.js chunks under `/_next/static/chunks/`, fetched 2026-10-19) |
| Europe (Nintendo Store, NoE) | **Adyen** RevenueProtect, receiving "cardholder's name, token ID and expiry date" | [Terms/Privacy Policy] | https://store.nintendo.com/en-gb/_sites/nintendo.be/privacy-and-cookies |
| Global (eShop, NSO, Store) | **PayPal**: billing-agreement routes for purchases, NSO auto-renew and pre-orders; `isPaypalAvailable` | [Source Code] [Terms/Privacy Policy] | ec.nintendo.com bundle; EU privacy URL above; launch: https://techcrunch.com/2017/08/22/nintendo-adds-paypal-support-to-the-nintendo-switch/ |
| Korea | **Alipay+ → KakaoPay**: "카카오페이(Alipay+ Partner)"; `/kakaopay/agreement` routes in the bundle | [Checkout docs] [Source Code] | https://support.nintendo.com/kr/switch/eshop/index.html |
| Japan (web Store) | **Paidy**: 1 payment, or 3 or 6 instalments; 18+ with ID check | [Press Release] | https://www.nintendo.com/jp/topics/article/ab5aebd2-e3b0-4918-a5b8-2a881f8cf24a ; https://paymentnavi.com/paymentnews/177233.html |
| JP web Store / US Store / EU Store | **Apple Pay, Google Pay** | [Press Release] [Source Code] | JP topics URL above; US store bundle enum `{GOOGLE_PAY, APPLE_PAY, PAYPAL, ECASH, VISA, MASTER}` |
| US | Sovos: tax calculation, **not a PSP** | [Source Code] | ec.nintendo.com bundle |
| Japan | Card acquirer / gateway | **Not found**: no GMO-PG, SBPS, Veritrans or KOMOJU in searches or the bundle | — |
| — | Cybersource, Worldpay, Braintree, Stripe, Checkout.com | **Not found** | — |

#### 3B. Payment Orchestrator

**Classification: In-house orchestration layer.**
- Evidence `[Source Code]`: the ec.nintendo.com error map references Nintendo's own services. `SHOGUN` handles eShop purchasing (e.g. `shogun.error.rejected_by_3dsecure`). `KANAT` handles card payment (`kanat.error.vcspas_card_declined`, `account_on_paymenthold`). `WHARF` handles payment methods and tokens (`wharf.error.invalid_token`, `payment_country_restricted`). `ZENITH` handles prepaid and `BATTERA` handles balance.
- Evidence `[Job Listing]`: Nintendo Systems is recruiting for the 決済基盤 (payment platform) behind the Nintendo Store and eShop, citing integration with external services and per-country legal requirements.
- Nintendo Systems is the Nintendo × DeNA JV, operating since 2023-04-03 ([Gematsu](https://gematsu.com/2022/11/nintendo-and-dena-to-establish-joint-venture-company)).
- No third-party orchestrator found (Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno, Juspay: all searched).
- **Nuance for the pitch:** this is a payment abstraction with **one visible card PSP**. There is no evidence of multi-acquirer routing, failover or local acquiring per market. "You already built the layer. The bottleneck is how fast each country's rails reach the console."

> **MANUAL:** On a Japanese and a Korean console or web purchase, use DevTools on ec.nintendo.com to capture which payment host the card form posts to (Adyen client-key domain vs other).

---

### Section 4: Alternative & Local Payment Methods

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| Japan (console eShop) | Credit card | Cards | Active in checkout (1 of 3) | https://support.nintendo.com/jp/switch/eshop/purchase.html |
| Japan (console eShop) | Nintendo prepaid card / number (sold at konbini, toy shops, Amazon.co.jp, Rakuten Books) | Cash/voucher (indirect) | Active in checkout | same; https://www.nintendo.com/jp/software/howtodl/prepaidcard/index.html |
| Japan (console eShop) | PayPal (18+) | Digital wallet | Active in checkout | same |
| Japan (NSO auto-renew / pre-orders) | Card, PayPal, balance only | Cards / wallet | Mentioned in docs | https://support.nintendo.com/jp/switch/eshop/account.html |
| Japan (web Nintendo Store) | Paidy, incl. 3 or 6 instalments | BNPL/Instalments | Active since 2026-08-07 | https://www.nintendo.com/jp/topics/article/ab5aebd2-e3b0-4918-a5b8-2a881f8cf24a |
| Japan (web Nintendo Store) | Apple Pay (JCB/VISA/MC), Google Pay (VISA/MC) | Digital wallet | Active since 2026-08-07 | same |
| Japan (all channels) | **PayPay** | Digital wallet | **Not found**: absent from the eShop's three-method list and from the Aug-2026 Store additions | purchase.html + topics URL |
| Japan (all channels) | **Konbini payment** (direct) | Cash/voucher | **Not found** as a payment method; konbini appears only as a place to buy prepaid cards | same |
| Japan (all channels) | **Carrier billing** (d払い / au / SoftBank) | Carrier billing | **Not found** | same; also no `docomo`/`carrier` strings in the ec.nintendo.com bundle |
| Japan | Card instalments (分割払い) on cards | BNPL/Instalments | Not found | — |
| South Korea (console eShop) | KakaoPay via Alipay+ | Digital wallet | Active in checkout | https://support.nintendo.com/kr/switch/eshop/index.html |
| South Korea (console eShop) | Prepaid (balance cap ₩200,000) | Cash/voucher | Active in checkout | same |
| South Korea (console eShop) | Credit card, PayPal | Cards / wallet | **Commented out** in page HTML: likely disabled | https://support.nintendo.com/kr/switch/eshop/account.html |
| South Korea | Naver Pay, Toss, Samsung Pay | Digital wallet | Not found | KR index page |
| Hong Kong (console eShop) | Credit card, prepaid | Cards / voucher | Mentioned in docs | https://support.nintendo.com/hk/switch/support/eshop/index.html |
| Hong Kong | AlipayHK, Octopus, FPS, PayPal | Wallet / A2A | Not found | same |
| Hong Kong (web Store) | UnionPay, Alipay | Cards / wallet | Third-party only, Jan 2020 `[UNVERIFIED]` | https://www.gcores.com/articles/119119 |
| Taiwan (console eShop) | Credit card (only method listed) | Cards | Mentioned in docs | https://support.nintendo.com/tw/switch/support/eshop/index.html |
| Taiwan | JKOPay, LINE Pay, convenience store, ATM transfer | Wallet / cash | Not found | same |
| Australia / NZ (eShop) | Card (same-country issuer), PayPal (18+), eShop card | Cards / wallet / voucher | Active | https://www.nintendo.com/au/support/articles/how-to-add-funds-on-nintendo-eshop/ |
| Australia (physical Store) | VISA / MC only; "PayPal not accepted" | Cards | Mentioned in docs | https://www.nintendo.com/au/support/articles/what-payment-methods-are-available-for-nintendo-store/ |
| Australia | Afterpay, Zip, PayTo, Apple Pay, Google Pay | BNPL / A2A / wallet | Not found | same |
| SG / MY / TH (eShop, launched 2025-11-18) | Any | — | Unknown: support pages return 403 | https://support.nintendo.com/sg/switch/eshop/index.html |
| Global | 3DS | — | Built in (`/3d_secure/callback` routes) | ec.nintendo.com bundle |

> *Warning: In Japan, PayPay is widely used but not currently supported by Nintendo on the console eShop.* **Prominence source not gathered in this run.** Cite a current PayPay user or merchant figure before putting this in an email. The *absence* is sourced; the *prominence* is not.

> *Warning: In South Korea, the console eShop offers one local wallet, routed via Alipay+, and appears to offer no direct card option.* Naver Pay and Toss prominence is not sourced in this run.

> **MANUAL:** VPN or local-account check of the SG/MY/TH eShop add-funds screen: does it offer PayNow, DuitNow/FPX/Touch 'n Go, PromptPay/TrueMoney, or cards only? This is the single most valuable unknown in the report.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Declined transactions: four cards from three banks plus PayPal all failing (2813-2470); Nintendo told the customer to use prepaid cards or wait a month | Nintendo Life forum (UK) | Isolated (one thread read in full) | Jun 2023 | https://www.nintendolife.com/forums/help/unable_to_make_payments |
| Declined transactions: long-used card suddenly declined; PayPal as workaround | Reddit r/nintendohelp (US) | Isolated | Jun 2025 | `[UNVERIFIED — search summary only]` https://teddit.bsalzberg.com/r/nintendohelp/comments/1l3z07p/suddenly_unable_to_purchase_anything_on_the_eshop |
| Policy-driven blocking: overseas cards and PayPal refused on the JP eShop and Store "to prevent fraudulent use" | Nintendo Japan announcement | High impact (affects every foreign buyer) | Effective 2025-03-25 | https://www.nintendolife.com/news/2025/01/japans-switch-eshop-will-soon-no-longer-accept-overseas-payment-methods |
| Card errors are documented as a standing support category (2813-2470, 2813-1470 saved card, 2813-0119, 9001-2470); the guidance is to check the card country matches the account country and contact the issuer | Nintendo support | Structural | Current | https://www.nintendo.com/au/support/articles/error-code-2813-2470/ ; https://en-americas-support.nintendo.com/app/answers/detail/a_id/48688 |
| Opaque declines: Nintendo "isn't able to provide the specific reason" a charge failed | Nintendo UK support | Structural | Current | https://www.nintendo.com/en-gb/Support/Troubleshooting/Error-Message-Check-With-Your-Credit-Card-Company-1501605.html |

> *Pattern: Nintendo's decline-recovery playbook is "try another card, PayPal or a prepaid card." There is no retry or alternate-acquirer path visible, and decline reasons are not surfaced. This points to single-path card processing per region, which is the failover and retry argument.* `[INFERENCE, not confirmed]`
>
> No Japan-, Korea- or Australia-specific payment complaints were found. That is a gap in what the searches returned, not evidence that there are none.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 2026-08-07 | Paidy, Apple Pay, Google Pay added to the JP Nintendo Store (web only, not the console eShop or NSO) | Tech / payment change | https://www.nintendo.com/jp/topics/article/ab5aebd2-e3b0-4918-a5b8-2a881f8cf24a |
| 2 | 2026-06-09 (listing update) | Nintendo Systems hiring a server engineer for the Store/eShop payment platform | Payment Infrastructure Hiring | https://herp.careers/careers/companies/nscareer/jobs/6fWhZUEJvoag |
| 3 | 2026-05-07 | NoA "Manager, Payments" (Payments & Fraud): auth rates, payment cost, coordination with NCL | Payment Infrastructure Hiring | `[UNVERIFIED — page now 500]` https://careers.nintendo.com/jobs/4140793009/ |
| 4 | 2025-11-18 | eShop and Switch Online launched in Singapore, Malaysia and Thailand; Philippines in progress | Market Expansion | https://www.nintendo.com/sg/news/article/tngPVu8X1gJcAMRvRJR7M |
| 5 | 2025-09-26 / ~2025-11-17 | Nintendo Singapore Pte. Ltd. founded; Nintendo Thailand reportedly founded | Market Expansion | https://www.nintendo.co.jp/corporate/release/en/2025/250930.html ; Thailand `[UNVERIFIED]` |

Also relevant:
- China eShop (Tencent) stopped sales on 2026-03-31; downloads and redemption ended 2026-05-15 `[UNVERIFIED — search summary only]`.
- Indonesia hardware launch reportedly Dec 2026 `[UNVERIFIED]`.
- Switch 2 price increases from May 2026 (US $499.99 from 2026-09-01) `[UNVERIFIED — press]`.

**No public payment-related RFP found.**

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 2026-08-07 | Nintendo Store Japan adds Paidy (first pay-later), Apple Pay, Google Pay | New rails, web only | https://paymentnavi.com/paymentnews/177233.html |
| 2 | 2026-09 | Scheduled maintenance on Apple/Google Pay (Store) and PayPal (eShop) | Shows the multi-provider operational surface | `[UNVERIFIED — search summary only]` https://otakukart.com/nintendo-announces-september-2026-maintenance-for-eshop-payments-and-parental-controls/ |
| 3 | 2025-01-30 (effective 2025-03-25) | JP eShop and Store stop accepting overseas cards and PayPal accounts (fraud prevention) | Fraud handled by geo-block | https://www.inside-games.jp/article/2025/01/30/163843.html |
| 4 | 2022-01-18 | Credit cards removed from 3DS / Wii U eShop in Japan | Legacy platform wind-down | https://news.denfaminicogamer.jp/news/220111h `[UNVERIFIED — search summary only]` |
| 5 | 2021-01-01 | 3DS required for EEA eShop payments (PSD2), with a QR-code web fallback from the console | 3DS architecture | https://nintendo.com/en-gb/Support/Nintendo-Switch/3D-Secure-Information-regarding-the-online-payment-authentication-1921169.html |

> **REMOVAL:** In Japan, Nintendo discontinued acceptance of overseas-issued credit cards and overseas PayPal accounts on the eShop and My Nintendo Store as of 2025-03-25. Source: https://www.nintendolife.com/news/2025/01/japans-switch-eshop-will-soon-no-longer-accept-overseas-payment-methods

---

### Section 8: Checkout Experience Audit

*Full checkout flow not accessible. Findings limited to publicly observable elements. The console eShop needs hardware, and store-jp.nintendo.com sits behind a Queue-it / Akamai waiting room.*

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | Custom-built Next.js front-end (ec.nintendo.com) over in-house services | — | Custom-built |
| Guest checkout | No. Digital purchases require a Nintendo Account by design | N/A | Content is tied to the account |
| Steps to complete payment | Not observed | — | — |
| Card input experience | Card callback routes plus Adyen error codes suggest a PSP-hosted or tokenized form | — | Tokenized `[INFERENCE]` |
| Payment methods visible | JP: 3 · KR: 2 · HK: 2 · TW: 1 (console eShop) | **Poor** for APAC | See Section 4 |
| Location-based method display | Per-region stores; the card country must match the account country | Fair | Strict region lock |
| Instalment / EMI options | None on the eShop; Paidy 3/6 instalments on the JP web Store only | Poor (console) | — |
| 3DS implementation | 3DS callback routes for every purchase type and for NSO and top-up; EEA mandatory since 2021 | Good | No Japan-specific notice found |
| PCI indicator | Token IDs passed to Adyen (EU policy) | — | Reduced scope `[INFERENCE]` |
| Mobile responsiveness | 75.6% of nintendo.com traffic is mobile web | Not tested | — |
| Multi-currency / local pricing | Regional stores in local currency | Fair | SEA local currency `[UNVERIFIED]` |
| Saved payment methods | One saved card per account (18+); PayPal/KakaoPay billing agreements | Fair | — |
| Error message clarity | Numeric codes; Nintendo "isn't able to provide the specific reason" | **Poor** | Section 5 |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found | — |
| Card data handling | Not found directly. The EU policy says saved cards are stored "separately in accordance with the credit or debit card provider's regulations" and a token ID is passed to Adyen | https://store.nintendo.com/en-gb/_sites/nintendo.be/privacy-and-cookies |
| Recommended Yuno integration | Back-to-back API: there is an existing in-house platform and console clients | — |

*No direct PCI compliance documentation found publicly for Nintendo.*

`[INFERENCE, not confirmed]`: Adyen token IDs plus `wharf.error.invalid_token` suggest card data is tokenized at the PSP, so Nintendo's PCI scope is likely reduced, with Adyen handling card data at least in Europe.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: The payment platform team says per-country methods are "essential", but the console eShop in four APAC markets offers 1–3 methods**
> **Evidence:**
> - S3B: the Nintendo Systems payment-platform job text.
> - S4: JP has 3 methods ([purchase.html](https://support.nintendo.com/jp/switch/eshop/purchase.html)), KR 2, HK 2, TW 1.
> - S6: the Aug-2026 JP Store additions are explicitly excluded from the console.
>
> **Pain Point:** every new rail is a bespoke integration into an in-house platform, then a separate console-client rollout. Even Japan, the home market, has no PayPay, konbini payment or carrier billing on the device where digital revenue (¥407.6bn) happens.
> **Yuno Value Proposition:** a single integration from the in-house platform (WHARF/KANAT layer) to the local rails per market, so adding PayPay or Naver Pay becomes configuration, not a new integration project.
> **Best Success Case:** NetEase Games: a multi-market Asian games business on Yuno for wallet- and cash-heavy markets.
> **Outreach Angle:** "Your payments team's own posting says per-country methods are essential. On the Switch eShop in Japan that's three methods today, and the August Store additions don't reach the console."
> **Suggested Subject Line:** "3 methods on the JP eShop"

> **Insight #2: Kyoto sells into Korea, HK, Taiwan and SEA, so those markets probably run cross-border**
> **Evidence:**
> - S2: the Nintendo Account agreements make NCL (Japan) the seller in KR/HK/TW/SG/MY/TH.
> - S1: Korea is a top-10 traffic market.
> - S4: Korea's only local rail is KakaoPay via Alipay+, with cards commented out.
>
> **Pain Point:** cross-border acquiring on local cards, which means approval-rate and fee drag `[INFERENCE, not confirmed]`, plus dependence on a cross-border wallet network for Korea.
> **Yuno Value Proposition:** local acquiring and local wallets per market, routed from one integration. This can be done while keeping NCL as seller of record, or aligned with Nintendo Singapore as SEA scales.
> **Best Success Case:** NetEase Games (multi-market Asia).
> **Outreach Angle:** "Nintendo Co., Ltd. is the seller on the Korean and SEA eShops, and in Korea the one local option runs through Alipay+. Who decides how those markets get local acquiring?"
> **Suggested Subject Line:** "Korea eShop: one wallet, via Alipay+"

> **Insight #3: The Southeast Asian eShop is 11 months old: a new rails decision is still open**
> **Evidence:**
> - S6: the eShop launched in SG/MY/TH on 2025-11-18, the Philippines is pending, and the Nintendo Singapore entity was set up in Sep 2025.
> - S4: SG/MY/TH methods are unknown.
> - S2: NCL Kyoto is the seller.
>
> **Pain Point:** each new SEA market (PH next, Indonesia hardware reportedly Dec 2026) brings its own dominant rails: PayNow, DuitNow/FPX, PromptPay, GCash, QRIS.
> **Yuno Value Proposition:** launch-ready local rails for the next SEA markets without a per-country build.
> **Best Success Case:** NetEase Games.
> **Outreach Angle:** "With the Philippines next after SG/MY/TH, is GCash on the plan for launch, or cards first?" *(Confirm SEA methods before sending; see Manual Research.)*
> **Suggested Subject Line:** "eShop Philippines: GCash at launch?"

> **Insight #4: Declines are recovered by telling the customer to try something else**
> **Evidence:**
> - S5: Nintendo's support guidance is "another card, PayPal or prepaid", with no specific decline reason.
> - S3A: one card PSP is visible (Adyen), with no multi-acquirer routing found.
> - S6: the NoA Payments Manager remit covers authorization rates `[UNVERIFIED]`.
>
> **Pain Point:** lost purchases on the console, where switching methods is high-friction.
> **Yuno Value Proposition:** retry and failover across acquirers inside one layer, plus decline-code-aware routing.
> **Best Success Case:** NetEase Games (Yuno markets "smart retries and failover" on the gaming page).
> **Outreach Angle:** "When a card fails on the eShop, the recovery path is the customer finding another card. Is there a second acquirer behind KANAT, or is it single-path per region?"
> **Suggested Subject Line:** "2813-2470"

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. Nintendo Systems' payment-platform posting says per-country methods are "essential", yet the Japan eShop's own help page lists exactly three ways to add funds.
2. The Paidy, Apple Pay and Google Pay launch on 7 August reached the Nintendo Store but, per your own notice, not the console eShop or Switch Online.
3. On the Korean eShop the only local option is KakaoPay via Alipay+, and Nintendo Co., Ltd. in Kyoto is the seller.

**Cold call openers (conversational, one sentence each):**
1. "I noticed the August Store update added Paidy and Apple Pay but explicitly not on the console, so I'm curious what the gating factor is for getting new methods onto the eShop."
2. "With SG, Malaysia and Thailand live since November and the Philippines next, how are you deciding which local methods go in at launch?"
3. "Your recruiting page for the payment platform mentions per-country legal requirements; how many PSP integrations does that team maintain today?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| Sony Interactive Entertainment (PlayStation) | playstation.com | Japan / US | ~$31.7B (TAL, unverified) | Global incl. JP/APAC | Not established. Paysafecard via Worldpay (EU, 2016) `[UNVERIFIED]`; **no Adyen link found** | https://www.finextra.com/pressarticle/62972/paysafecard-comes-to-sony-playstation |
| Microsoft (Xbox) | xbox.com | USA | Not researched | Global incl. APAC | **Worldpay** (online card processing for storefronts "including Xbox", incl. APAC, 2021); **Adyen** (Microsoft-wide) `[UNVERIFIED]` | https://www.worldpay.com/en/press-releases/microsoft-expands-payments-relationship-worldpay-fis-globally ; https://thefintechtimes.com/adyen-collaborates-with-microsoft-to-launch-network-token-optimisation/ |
| Valve (Steam) | store.steampowered.com | USA | Not researched | Global | Xsolla (2011, Russia) `[UNVERIFIED]` | https://thepaypers.com/online-payments/russia-valve-selects-xsolla-to-monetise-steam--745632 |
| Epic Games Store | epicgames.com | USA | Not researched | Global | Xsolla, PayPal (Epic help page) `[UNVERIFIED]` | https://www.epicgames.com/help/c-202300000001642/c-202300000001747/purchase-errors-when-entering-paypal-and-xsolla-payment-information-a202300000014680 |
| Tencent Games / Level Infinite (Midasbuy) | levelinfinite.com | China / Singapore | Not verified | JP, SEA, KR | In-house top-up store (Midasbuy); TAL notes in-house | accounts/apac-tal.csv |
| NetEase Games | netease.com | China | — | Global incl. JP/SEA | **Yuno** (existing Yuno merchant) | https://y.uno/en/industries/gaming.md |

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Cygames | cygames.co.jp | Mobile/PC games (JP) | Japan, global | GMO-PG for Japan, Xsolla elsewhere; in-house `country_code==='JP'` switch with no failover. Closest Japanese analogue | 2-ready-to-outreach/cygames.md |
| HoYoverse | hoyoverse.com | Games | Global, APAC | 11 PSPs incl. Adyen behind an in-house platform: the same "built it ourselves" posture | 2-ready-to-outreach/hoyoverse-mihoyo.md |
| Com2uS | com2us.com | Mobile games (KR) | KR, JP, global | PortOne orchestrator inside the Hive billing platform | 2-ready-to-outreach/com2us.md |
| Square Enix | square-enix.com | Publisher (JP) | Global | TAL lists cards and PayPal, no orchestrator | accounts/apac-tal.csv |
| Bandai Namco Entertainment | bandainamcoent.com | Publisher (JP) | Global | Not established; an Xsolla deal exists with sister Bandai Co. (Tamagotchi web shop) `[UNVERIFIED]` | https://www.businesswire.com/news/home/20240416204583/en |
| Capcom / Sega / Konami | — | Publishers (JP) | Global | Not established (one shared search each) | accounts/apac-tal.csv |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| NetEase Games | Yuno | Not dated (Singapore setup referenced in Yuno's Sep 2025 APAC release `[UNVERIFIED]`) | Games | https://y.uno/en/industries/gaming.md |
| Com2uS | PortOne | Not established | Mobile games (KR) | 2-ready-to-outreach/com2us.md |
| Webzen | PortOne (KR mobile) | PG list effective 2025-12-26 | Games (KR) | 2-ready-to-outreach/webzen.md |
| Mythical Games | Gr4vy | 2023-03-03 | Web3 games (US, out of territory) | https://thepaypers.com/payments/news/mythical-games-choses-gravys-pop |

#### 11D. Prospect Scoring

These are partial scores. Competitors were not fully researched, and only verified signals are counted, so these are floors.

| Company | Verified signals | Partial score | Evidence Source |
|---|---|---|---|
| Sony Interactive Entertainment | 3+ countries (global storefront) `[INFERENCE]` | Not scorable | — |
| Square Enix | Cards and PayPal only (TAL, unverified) | Not scorable | apac-tal.csv |
| Cygames | Already scored in its own file | See file | 2-ready-to-outreach/cygames.md |
| HoYoverse | Already scored in its own file | 23/29 ⭐ | 2-ready-to-outreach/hoyoverse-mihoyo.md |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Sony Interactive Entertainment | Direct competitor | JP, global | Not scored | Research next | Same console-store model, Japan HQ | ✅ |
| 2 | Bandai Namco Entertainment | Peer | JP, global | Not scored | Research | Sister company already on Xsolla | ✅ |
| 3 | Square Enix | Peer | JP, global | Not scored | Research | Cards/PayPal-only per TAL | ✅ |
| 4 | Capcom | Peer | JP, global | Not scored | Research | — | ✅ |
| 5 | Sega | Peer | JP, global | Not scored | Research | — | ✅ |
| 6 | Konami Digital Entertainment | Peer | JP, global | Not scored | Research | — | ✅ |
| 7 | DeNA | Adjacent (co-built Nintendo Account; JV partner in Nintendo Systems) | JP | Not scored | Research | Relationship route into Nintendo Systems | ✅ |

No strong prospect off the TAL was identified. Microsoft, Valve and Epic are US-HQ'd and out of territory.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue | ¥2,313,051M (FY3/2026); ≈US$15bn `[ESTIMATE, not confirmed — FX not sourced]` | https://www.nintendo.co.jp/ir/pdf/2026/260508e.pdf |
| Latest quarter | Q1 FY3/2027 net sales ¥517,813M | https://www.nintendo.co.jp/ir/pdf/2026/260806e.pdf |
| Digital sales | ¥407.6bn FY3/2026 (+25.0%), 54.6% of software; ¥132.7bn in Q1 FY3/27 (61.5%). Third-party sales booked net, so gross spend is higher | https://www.nintendo.co.jp/ir/pdf/2026/260508_4e.pdf ; https://www.nintendo.co.jp/ir/pdf/2026/260806_2e.pdf |
| Average Transaction Value | Not disclosed | — |
| Est. Annual Transactions | Not computable from sourced inputs (no ATV) | — |
| **Monthly transaction count** | ✅ **DERIVED (floor): ≥340,000/month**, realistically millions. ¥407.6bn ÷ 12 = ¥34.0bn/month, divided by a deliberately absurd ¥100,000 ceiling on average ticket (a full-price game is $79.99). The revenue input is sourced; the ceiling is a bound I chose, not a sourced ATV. Billing unit: eShop purchases and balance top-ups. Gate cannot fire. | IR above |
| Active Customers / Users | Annual playing users ">100 million" (Nintendo's wording; excludes eShop-only use). Nintendo Accounts ~366M (Nov 2024) `[UNVERIFIED]`. NSO members not disclosed in current IR | IR above |
| Primary Currency | JPY (reporting); local-currency regional stores | — |
| Top 3 Markets by Revenue | Americas ¥935.3bn · Europe ¥551.5bn · Japan ¥534.9bn (FY3/2026); "Other" ¥291.4bn, region definition not confirmed | IR above |
| Billing channel split (web vs app store) | Console eShop and web Store are **first-party billing** (Nintendo is seller of record). Mobile IAP sits in a far smaller line (IP-related income ¥73.5bn, which also includes non-mobile IP). Exact split not disclosed | IR above; Nintendo Account agreements |
| Switch 2 installed base | 19.86M at 2026-03-31; 23.68M life-to-date after Q1 FY3/27 | IR above |

---

### Overall Research Confidence

**Medium-High.**
- **Strong:** the PSP and orchestration findings come from first-hand production code and Nintendo's own privacy policy. APAC payment methods come from Nintendo's own support pages, which I re-fetched. Entities and financials come from Nintendo IR and the securities report, and the seller of record from the Nintendo Account agreements.
- **Limited:** SEA payment methods (pages return 403); the Japan card acquirer (unknown); complaints (thin, US/UK-skewed, nothing APAC-specific); checkout (no console access, and store-jp sits behind a waiting room); competitors (shallow beyond Microsoft and NetEase).
- **Traffic data was supplied** (SimilarWeb Sales Intelligence, top-10 only, shares only). Per-country visits are derived. The data is web-only, which the app-heavy caveat warns about. It is used here as a market-mix signal only, and it did not drive the transaction gate.

---

### Manual Research Recommendations

> **Area:** Monthly transaction count
> **Why it matters:** this is the only gate signal. The floor is derived, not measured.
> **Suggested manual action:** not urgent: no plausible average ticket brings the count near 40k. Ask in discovery how many eShop transactions APAC runs per month.

> **Area:** SG / MY / TH eShop payment methods (Section 4)
> **Why it matters:** this decides whether Insight #3 is a gap story or a coverage-depth story.
> **Suggested manual action:** with a VPN to SG/MY/TH, open support.nintendo.com/{sg,my,th}/switch/eshop/ in a browser (it returned 403 to scripts). Or ask a contact in the region to screenshot the eShop's add-funds screen.

> **Area:** Japan and Korea card acquirer (Section 3A)
> **Why it matters:** Adyen is proven for Europe and present in the global bundle. Whether it processes JP/KR cards changes the cross-border argument.
> **Suggested manual action:** DevTools on an ec.nintendo.com purchase from a JP and a KR account. Check the card-form host or client key and the 3DS ACS domain.

> **Area:** Korea card option (Section 4)
> **Why it matters:** the card and PayPal sections are commented out. Confirm cards are truly gone before using "one wallet" in outreach.
> **Suggested manual action:** check the add-funds screen on a Korean-region Nintendo Account.

> **Area:** PayPay / Naver Pay prominence
> **Why it matters:** the absence is sourced; prominence is not, and the email rules require a source.
> **Suggested manual action:** pull a current PayPay registered-user figure from PayPay's own newsroom before using it.

> **Area:** Buyer persona
> **Why it matters:** the visible payments roles are at NoA (out of territory) and Nintendo Systems (engineering). The decision sits with NCL Kyoto.
> **Suggested manual action:** Sales Navigator search for NCL / Nintendo Systems titles containing 決済 or "payment", and the NoA Payments & Fraud lead who coordinates with NCL. Consider coordinating with the Americas AE.

---

### Appendix: All Source URLs

**Traffic:** accounts/traffic/nintendo.md (SimilarWeb, supplied 2026-10-19)

**Section 2:**
- https://www.nintendo.co.jp/corporate/en/outline/index.html
- https://www.nintendo.co.jp/ir/pdf/2026/security_q2603.pdf
- https://www.nintendo.co.jp/corporate/release/en/2025/250930.html
- https://www.vgchartz.com/article/466355/nintendo-establishes-nintendo-thailand/
- https://houjin.jp/c/1130001011420
- https://accounts.nintendo.com/term/eula/AU?lang=en-US
- https://accounts.nintendo.com/term/eula/SG?lang=en-US
- https://accounts.nintendo.com/term/eula/HK?lang=en-US
- https://accounts.nintendo.com/term/eula/TW?lang=zh-TW
- https://accounts.nintendo.com/term/eula/KR?lang=ko-KR
- https://accounts.nintendo.com/term/eula/JP?lang=ja-JP
- https://accounts.nintendo.com/term/eula/IN?lang=en-US

**Section 3:**
- https://ec.nintendo.com/
- https://store.nintendo.com/en-gb/_sites/nintendo.be/privacy-and-cookies
- https://techcrunch.com/2017/08/22/nintendo-adds-paypal-support-to-the-nintendo-switch/
- https://support.nintendo.com/kr/switch/eshop/index.html
- https://paymentnavi.com/paymentnews/177233.html
- https://gematsu.com/2022/11/nintendo-and-dena-to-establish-joint-venture-company
- https://docs.adyen.com/payment-methods/kakaopay

**Section 4:**
- https://support.nintendo.com/jp/switch/eshop/purchase.html
- https://support.nintendo.com/jp/switch/eshop/account.html
- https://www.nintendo.com/jp/software/howtodl/prepaidcard/index.html
- https://www.nintendo.com/jp/topics/article/ab5aebd2-e3b0-4918-a5b8-2a881f8cf24a
- https://support.nintendo.com/kr/switch/eshop/account.html
- https://support.nintendo.com/hk/switch/support/eshop/index.html
- https://www.gcores.com/articles/119119
- https://support.nintendo.com/tw/switch/support/eshop/index.html
- https://www.nintendo.com/au/support/articles/how-to-add-funds-on-nintendo-eshop/
- https://www.nintendo.com/au/support/articles/how-to-link-paypal-to-a-nintendo-account/
- https://www.nintendo.com/au/support/articles/what-payment-methods-are-available-for-nintendo-store/
- https://support.nintendo.com/sg/switch/eshop/index.html
- https://en-americas-support.nintendo.com/app/answers/detail/a_id/22327
- https://www.nintendo.com/en-gb/Support/Purchases-Subscriptions/Nintendo-Store-Payments-3057873.html

**Section 5:**
- https://www.nintendolife.com/forums/help/unable_to_make_payments
- https://teddit.bsalzberg.com/r/nintendohelp/comments/1l3z07p/suddenly_unable_to_purchase_anything_on_the_eshop
- https://www.nintendolife.com/news/2025/01/japans-switch-eshop-will-soon-no-longer-accept-overseas-payment-methods
- https://www.nintendo.com/au/support/articles/error-code-2813-2470/
- https://en-americas-support.nintendo.com/app/answers/detail/a_id/48688
- https://www.nintendo.com/en-gb/Support/Troubleshooting/Error-Message-Check-With-Your-Credit-Card-Company-1501605.html

**Sections 6–7:**
- https://herp.careers/careers/companies/nscareer/jobs/6fWhZUEJvoag
- https://careers.nintendo.com/jobs/4140793009/
- https://www.nintendo.com/sg/news/article/tngPVu8X1gJcAMRvRJR7M
- https://www.inside-games.jp/article/2025/01/30/163843.html
- https://otakukart.com/nintendo-announces-september-2026-maintenance-for-eshop-payments-and-parental-controls/
- https://news.denfaminicogamer.jp/news/220111h
- https://nintendo.com/en-gb/Support/Nintendo-Switch/3D-Secure-Information-regarding-the-online-payment-authentication-1921169.html

**Section 8:** https://www.nintendo.com/us/store/products/mario-kart-world-switch-2/

**Section 11:**
- https://y.uno/en/industries/gaming.md
- https://www.worldpay.com/en/press-releases/microsoft-expands-payments-relationship-worldpay-fis-globally
- https://thefintechtimes.com/adyen-collaborates-with-microsoft-to-launch-network-token-optimisation/
- https://www.finextra.com/pressarticle/62972/paysafecard-comes-to-sony-playstation
- https://thepaypers.com/online-payments/russia-valve-selects-xsolla-to-monetise-steam--745632
- https://www.epicgames.com/help/c-202300000001642/c-202300000001747/purchase-errors-when-entering-paypal-and-xsolla-payment-information-a202300000014680
- https://www.businesswire.com/news/home/20240416204583/en
- https://thepaypers.com/payments/news/mythical-games-choses-gravys-pop
- Repo files: 2-ready-to-outreach/{cygames,hoyoverse-mihoyo,com2us,webzen}.md

**Section 12:**
- https://www.nintendo.co.jp/ir/pdf/2026/260508e.pdf
- https://www.nintendo.co.jp/ir/pdf/2026/260508_4e.pdf
- https://www.nintendo.co.jp/ir/pdf/2026/260806e.pdf
- https://www.nintendo.co.jp/ir/pdf/2026/260806_2e.pdf

</details>
