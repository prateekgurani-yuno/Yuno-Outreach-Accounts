# Kling AI (kling.ai) — Kling AI Pte. Ltd. · parent Kuaishou Technology, HKEX: 1024

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 21 / 29 → ⭐ High Priority (18 on the addressable global stack alone — still ⭐; see override note)
**Industry:** AI video generation — consumer credit subscriptions + developer/enterprise API · **HQ:** Beijing, China (international billing entity: Kling AI Pte. Ltd., Singapore) · **Researched:** 2026-09-28 · **First email sent:** —
**Motion:** In-house (thin) — a group-built cashier layer, but **one live acquirer (Stripe) for every market outside China**

---

> ## 🎯 THE HOOK — China gets three local rails. The other 223 countries get one list.
>
> **Verified first-hand in Kling's production bundle (`kling-web/assets/js/territory-text-Dd9qiWMx.js`), 2026-09-28:**
>
> ```js
> paymentMethodConfig:{
>   [CN]:     { methods:["alipay","wechatpay","unionpay"], preferred:"alipay", currency:"CNY" },
>   [GLOBAL]: { methods:["stripe","paypal"],               preferred:"stripe", currency:"USD" }
> }
> ```
>
> Kling says it serves users in 224 countries and regions. Its code has exactly two payment regions. One is China. The other is everyone else — **India (#1 market, 15.21% of traffic), the US, Korea, Brazil, Indonesia and Pakistan all get the same `["stripe","paypal"]` in USD.** PayPal is configured but no PayPal code path was found live; in practice it is Stripe.
>
> ### And their own app already does what their website doesn't
>
> The iOS app (seller: KLING AI PTE. LTD.) sells **India-only price points** — *100 Credits ₹149, Standard Membership one week ₹99 / ₹149, and a ₹49 week offer* — and **Indonesia-only ones** — *100 Credits Rp29rb, one week Rp19rb*. Verified on `apps.apple.com/in` and `/id`, 2026-09-28. The US storefront has no 100-credit pack at all.
>
> On the web, the same buyer gets USD list prices ($6.99 first month / $8.80 Standard) on a card, with Stripe Adaptive Pricing converting the currency at checkout. **Currency conversion, not local pricing, and no local rail.**
>
> ### The market has noticed
>
> Paid intermediaries exist **specifically to take local money for Kling**: Indonesian *"jasa bayar Kling AI"* services accepting QRIS/IDR (*"Kartu debit lokal, GoPay, OVO, atau DANA tidak dapat digunakan langsung di situs Kling"* — joinbareng.com), a Brazilian reseller taking Pix, and Russian SBP intermediaries. When a third party builds a business out of your checkout gap, the gap is real.
>
> **Why now:** Kling just raised ~US$2B+ from outside investors (HKEX filing, 2 Jul 2026) to fund *"independent commercial operations"*, with a Hong Kong IPO intended within ~12 months, and a post-closing obligation to acquire an overseas operating company. The international stack is about to be reorganised whether or not anyone pitches it.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Kling is Kuaishou's AI video-generation product — text/image-to-video models (Kling 3.0 series, native 4K as of Q2 2026) sold as credit-based consumer subscriptions on web and app, plus a developer/enterprise API. Revenue **>RMB850M in Q2 2026 (+200% YoY)** and an ARR of **~US$500M (March 2026)**. In July 2026 it raised its first external round (~US$2B initial tranche, up to ~RMB19–20bn) from Tencent, Alibaba, Baidu and others ahead of a planned Hong Kong IPO.

**SimilarWeb total visits (last full month):** **Not supplied** — screenshot gives shares only (Jun–Aug 2026, `kling.ai`, 121 countries, top 7 rows visible). Source: SimilarWeb (supplied 2026-09-28), `accounts/traffic/kling-ai.md`. ⚠️ China runs on a separate domain and is not in this data.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇮🇳 India | **15.21%** ▼0.06% | Stripe card (USD list, Adaptive Pricing FX); Apple/Google IAP in INR | UPI, **UPI Autopay**, RuPay, netbanking, EMI — none in Kling's code or docs ⚠️ one user report of a PhonePe UPI payment, channel unknown (likely Google Play) | ❌ None |
| 2 | 🇺🇸 United States | **11.75%** ▼10.03% | Stripe card, Apple Pay on web (user report), IAP | — (card market) | ❌ None |
| 3 | 🇰🇷 South Korea | **5.08%** ▲7.51% | Stripe card in USD; IAP in KRW | KakaoPay, Naver Pay, Toss, domestic card PG / instalments | ❌ None ⚠️ (acquiring gate not verified — see S2) |
| 4 | 🇧🇷 Brazil | **4.47%** ▲9.41% | Stripe card; IAP in BRL | **Pix**, boleto, parcelamento | ❌ None |
| 5 | 🇷🇺 Russia | **3.92%** ▼8.06% | Effectively unserved on web (Russian cards fail; users go via SBP intermediaries) | Mir, SBP | ❌ None — *out of territory, and sanctions context; corridor evidence only* |
| 6 | 🇮🇩 Indonesia | 3.35% ▼**46.45%** | Stripe card; IAP in IDR | **QRIS**, GoPay, OVO, DANA, virtual account | ❌ None |
| 7 | 🇵🇰 Pakistan | 2.77% ▼26.08% | Stripe card | JazzCash, Easypaisa, Raast | ❌ None |

### Legal entities
- ⭐ **KLING AI PTE. LTD.** (Singapore) — UEN **202502609E**, incorporated 17 Jan 2025, registered at 1 Raffles Place #36-01 (Maples corporate-secretary address). Contracting party for ToS, Privacy Policy and Terms of Paid Service; App Store and Google Play seller.
- **Beijing Kling (北京可灵)** (PRC) — *"principally engaged in the development and operation of Kling AI"*; the vehicle for the July 2026 raise. Kuaishou's stake falls to ~68.33% if fully subscribed.
- **Lucky Labs Limited**, **Fortune Ever** (Hong Kong) — Kuaishou investment holding companies.
- **Kuaishou Technology** (Cayman) — listed parent, HKEX 1024.

### Known PSPs
- **Stripe** — [Source Code] live `pk_live_51TE4m…`, Checkout Elements custom UI with `adaptivePricing:{allowed:!0}` + Stripe Tax + Stripe Billing portal; [Terms] named in the auto-renewal clause. **All non-CN web markets.**
- **PayPal** — [Source Code] *configured* in `paymentMethodConfig[GLOBAL]`; no PayPal SDK or live code path found. Treat as unconfirmed.
- **Apple IAP / Google Play Billing** — [App Store]/[Terms]. Mobile, all storefronts except CN.
- **Alipay, WeChat Pay, UnionPay** via **Kuaishou Pay cashier** (`kspay-cashier-sdk`, kuaishoupay.com) — [Source Code]. China build and enterprise deposits.
- **Offline corporate bank transfer** — [Terms] enterprise prepaid top-ups (`CRM_RECHARGE` → "offline-top-up").

### Orchestration status
**In-house orchestration layer — thin on the international side.** A group-built cashier abstraction (`PROVIDER_CASHIER`, backend-returned `supportProviders`, `providerSecret` vs `payUrl`) sits over the stack, and Kuaishou runs its own payment gateway for China. But the only client-side routing is a binary **CN vs GLOBAL** switch, and **the only live acquirer outside China is Stripe.** No third-party orchestrator: 0 hits for Juspay, Spreedly, Primer, Gr4vy, Payrails, Yuno across 1,500 production bundles and searches.

### Buying signals
- 💰 **~US$2B+ first external round**, HKEX-filed 2 Jul 2026, to fund *"independent commercial operations"*; HK IPO intended within ~12 months ([HKEX](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0702/2026070204065.pdf), [SCMP](https://www.scmp.com/tech/article/3359250/kuaishou-files-us3-billion-kling-ai-funding-round-hong-kong-stock-exchange))
- 🏗️ **Post-closing obligation to acquire 100% of "an overseas operating company"** via ODI — the international entity structure is being reorganised over the coming months (same HKEX filing)
- 🚀 Revenue **>RMB850M in Q2 2026, +200% YoY**; ARR ~US$500M in March 2026 ([PR Newswire](https://www.prnewswire.com/news-releases/kuaishou-technology-announces-second-quarter-and-interim-2026-unaudited-financial-results-302855081.html))
- 🏢 Enterprise API push — sales form with budget tiers to **"150,000+ USD/month"**, localised EN/JA/KO ([kling.ai/dev/pricing](https://kling.ai/dev/pricing))
- ⚠️ Trustpilot **1.2/5, 398 reviews, 90% one-star**, dominated by renewal/cancellation billing ([Trustpilot](https://www.trustpilot.com/review/klingai.com)) — reply material, not opener

### ✅ Export-control check — clean (verified by me)
Kuaishou / Kling / Beijing Dajia: **0 hits** on OFAC SDN, OFAC consolidated (non-SDN, incl. NS-CMIC) lists, and the Federal Register (BIS Entity List). The only "Kwai" hits are *Kwai Chung*, Hong Kong addresses of unrelated entities. Not among the June 2026 1260H additions (which did add Alibaba and Baidu — both now Kling investors; that is a DoD-procurement list and does not restrict commercial payments). **No z.ai-style block.**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach kling-ai` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 21 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. [ASSUMPTION — not researched.]** Basis: Q2 2026 revenue >RMB850M ≈ US$39M/month (sourced). Consumer tickets are sourced at $1.19–$160/month plus $5 credit packs; average ticket and the consumer/API split are **not** sourced. Even if 40% of revenue were enterprise API, $23M/month ÷ $160 (the *highest* monthly consumer ticket) ≈ 146,000. 60M+ creators and 10M+ Google Play installs point the same way. Billing unit: subscription charges + credit-pack purchases; IAP transactions are Apple's/Google's, not Kling's. Figure includes China revenue. |
| Orchestration status | +1 | ✅ In-house cashier layer (group-built) — see override note: the global side is effectively single-PSP |
| 3+ countries | +3 | ✅ 7 countries >1% traffic (SimilarWeb supplied) |
| Multiple PSPs | +3 | ✅ Stripe + Alipay/WeChat/UnionPay via Kuaishou Pay + Apple/Google IAP + offline transfer [Source Code][Terms] |
| Local rail or licensing gap in a top-3 market | +3 | ✅ India (#1): no UPI / UPI Autopay in code, docs or terms; Korea (#3): no KakaoPay / Naver Pay / Toss. Absence evidenced by 1,500-bundle grep + Terms of Paid Service naming Stripe/IAP only. ⚠️ Stripe Payment Element methods are set server-side and can't be fully read from client code. |
| Recent expansion | 0 | ⬜ Product launches (Kling 3.0, 4K) and Korean film partnerships, but no verified new *market* launch in 12 months |
| Payment issues | +2 | ✅ High — Trustpilot 1.2/5 (398 reviews, 90% 1-star), billing-dominated; 21 Sikayetvar complaints incl. double charge, charged-not-credited |
| Funding >$10M | +2 | ✅ ~US$2B+ initial tranche, 2 Jul 2026 (HKEX) |
| High traffic outside home | +2 | ✅ China absent from kling.ai's top 7; India + US alone 27% |
| Competitor using orchestration | 0 | ❌ None found across 8 AI-video competitors |
| Payment job postings | 0 | ❌ None found |

**Tier:** 21 → ⭐ **High Priority**

**Analyst override check — tier held, with two notes:**
- **Double-counting.** "Multiple PSPs" fires only because of the CN/GLOBAL split, and Yuno cannot address the China rails (Kuaishou Pay, Alipay, WeChat). Scored strictly on the addressable international stack, Kling is **single live PSP + app stores → 18/29, still ⭐.** That single-PSP reality is the pitch, not a weakness of the account.
- **App-store trap: not triggered, but unquantified.** No web-vs-IAP split is disclosed. Enterprise API (no IAP exposure; buyers "on contract rather than through the App Store" per Sacra) and web Stripe subscriptions are both material. ~75% of ARR is overseas per a secondary source only. **Confirm the web/IAP split on the first call.**
- **Transaction count is assumed**, not sourced — first item in Manual Research Recommendations.

### Source Notes
- ✅ `paymentMethodConfig` CN vs GLOBAL — read by me in `territory-text-Dd9qiWMx.js`, 2026-09-28
- ✅ `adaptivePricing:{allowed:!0}` in `PayStripeComponent-BHQwd1Al.js` — read by me
- ✅ App Store seller KLING AI PTE. LTD. in us/in/id/kr/br; INR/IDR/KRW/BRL storefronts; India ₹149 / ₹99 / ₹49 and Indonesia Rp29rb / Rp19rb IAP — read by me on apps.apple.com
- ✅ Sanctions / Entity List / 1260H — checked by me against primary lists
- ✅ Entity, terms, financials — agent-read from kling.ai docs, HKEX PDF, PR Newswire copy of Kuaishou results
- ⚠️ "~75% of ARR overseas" — Digital Applied blog attributing it to Kuaishou; not found in a primary filing
- ⚠️ ">100M users in 224 countries and regions; ~50,000 enterprise customers" — BigGo/36Kr secondary; not in Q2 release
- ⚠️ Consumer plan prices — third-party captures (Magic Hour, Sep 2026); kling.ai's plan page is client-rendered
- ⚠️ India UPI user report (₹3,038.83 "via PhonePe UPI") — channel not stated; **do not claim "no UPI" outright** in outreach
- ⚠️ Trustpilot/Sikayetvar quotes — extracted via summarizer; re-check verbatim before quoting

### Success Case Alternatives
- **Vibra** (Tier 2 — same payment pattern) — first-time payers in emerging markets; new-user approval +30pp to 80%, launched new methods on top of the existing stack. **Brazil is Kling's #4 market (4.47%)**, so the market is genuinely shared. Used for MiniMax — don't reuse verbatim if both accounts see the same AE.
- **No AI-video orchestration case exists anywhere** (Section 11C). Any E4 proof must be a payment-pattern match, not a vertical match. Say so rather than stretch.

---

## Executive Summary

Kling AI is Kuaishou's AI video-generation business, billing every international user from a single Singapore entity (Kling AI Pte. Ltd.) and growing fast (>RMB850M Q2 2026 revenue, ~US$500M ARR). Its production code has exactly two payment regions: China gets Alipay, WeChat Pay and UnionPay in CNY via Kuaishou's own payment gateway; the rest of the world — led by India (15.21%), the US, Korea, Brazil and Indonesia — gets Stripe (with PayPal configured but not seen live) in USD, with currency conversion but no local rail. The opportunity is local-rail coverage and local acquiring in India, Korea, Brazil and Indonesia on top of Stripe, timed to a ~US$2B spin-off round, a planned HK IPO and an announced reorganisation of the overseas operating entity. Motion: **in-house (thin)** — respect the group-built cashier, argue reach.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** SimilarWeb (supplied 2026-09-28), screenshot, `kling.ai`, Jun–Aug 2026, all traffic, 121 countries. Shares only; no visit count; ranks 8–121 not visible. `klingai.com` 301s to `kling.ai` (checked). China product on a separate domain, excluded.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | India | 15.21 | Not supplied | Stable (▼0.06%) | SimilarWeb (supplied) |
| 2 | United States | 11.75 | Not supplied | Declining (▼10.03%) | same |
| 3 | South Korea | 5.08 | Not supplied | Growing (▲7.51%) | same |
| 4 | Brazil | 4.47 | Not supplied | Growing (▲9.41%) | same |
| 5 | Russia | 3.92 | Not supplied | Declining (▼8.06%) | same |
| 6 | Indonesia | 3.35 | Not supplied | Sharply declining (▼46.45%) | same |
| 7 | Pakistan | 2.77 | Not supplied | Declining (▼26.08%) | same |

- **High priority (>5%):** India, US, Korea. None of the top 7 has a local Kling entity (Section 2).
- India's audience share (20.90%) exceeds its traffic share — more distinct users, fewer visits each; consistent with a price-sensitive, trial-heavy market.
- Indonesia −46% and Pakistan −26% over the period. [INFERENCE, not confirmed] could reflect payment friction; equally could be competitive or seasonal. Do not assert the cause.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Beijing, China (Beijing Kling / Kuaishou). International contracting from Singapore.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Singapore | KLING AI PTE. LTD. | UEN 202502609E (inc. 17 Jan 2025) | https://kling.ai/docs/user-policy ; https://recordowl.com/company/kling-ai-pte-ltd ; https://companieshouse.sg/kling-ai-pte-ltd-202502609E |
| China | Beijing Kling (北京可灵) + 6 subsidiaries (mostly dormant) | Not found | https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0702/2026070204065.pdf |
| Hong Kong | Lucky Labs Limited; Fortune Ever (holding) | Not found | same |
| Cayman | Kuaishou Technology (HKEX 1024) | — | same |

Terms: Singapore law, SIAC arbitration seated in Singapore, class-action waiver. Data stored in Singapore (Korea supplement: processing in "[Singapore, Malaysia]"). Jurisdictional supplements for Brazil, India, Indonesia, UAE, Mexico, Korea, Vietnam, California name **no local entity**.

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| India | ✅ #1 | ❌ | Not verified this run | ⚠️ Yes |
| United States | ✅ #2 | ❌ | No | ⚠️ Yes (SG merchant, US cards) |
| South Korea | ✅ #3 | ❌ | Not verified this run | ⚠️ Yes |
| Brazil | ✅ #4 | ❌ | Not verified this run | ⚠️ Yes |
| Russia | ✅ #5 | ❌ | Sanctions-driven; out of territory | Effectively unserved |
| Indonesia | ✅ #6 | ❌ | Not verified this run | ⚠️ Yes |
| Pakistan | ✅ #7 | ❌ | Not verified this run | ⚠️ Yes |

> *Warning: Potential cross-border operation in India, the US, South Korea, Brazil and Indonesia. No local entity found. Transactions are likely processed cross-border by a Singapore merchant, with higher scheme costs, lower approval rates and FX exposure.*

> **Regulatory gates:** not asserted. The APAC reference flags India, Indonesia, Korea and Vietnam as markets where domestic acquiring is often gated behind local presence, but no current source was pulled this run. **Verify before citing.**

**Timing note:** the HKEX filing obliges Beijing Kling to acquire 100% of an unnamed "overseas operating company" post-closing via ODI. [INFERENCE, not confirmed] this is Kling AI Pte. Ltd. — the international billing entity is mid-reorganisation.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Global (non-CN) web | **Stripe** — `pk_live_51TE4m…`, `initCheckoutElementsSdk({clientSecret, adaptivePricing:{allowed:!0}})`, Stripe Tax, Billing portal `billing.stripe.com/p/login/dR66qy9gVgqW8bS144` | [Source Code] [Terms/Privacy Policy] | `kling-web/assets/js/PayStripeComponent-BHQwd1Al.js`; https://kling.ai/docs/payment-policy |
| Global | **PayPal** — in `paymentMethodConfig[GLOBAL].methods` and i18n `payment-channel-PAYPAL`; **no SDK or live path found** | [Source Code] | `territory-text-Dd9qiWMx.js`; `json-DIpgW6xR.js` |
| China | Alipay, WeChat Pay, UnionPay (QR) | [Source Code] | `territory-text-Dd9qiWMx.js`; `ComponentPaymentV2-Cupy05nI.js` |
| China / enterprise | **Kuaishou Pay** in-house cashier SDK — *"快手支付平台网关系统前端"*, e-bank, remittance | [Source Code] | `vendor-yoda-js-Bp1RyIqT.js`; `kling-web-tob/assets/pay-Cxd_gGO5.js` |
| iOS / Android | Apple IAP, Google Play Billing | [Terms] [App Store] | https://apps.apple.com/us/app/id6738049229 ; https://play.google.com/store/apps/details?id=kling.ai.video.chat |
| Enterprise | Offline corporate bank transfer (prepaid top-up) | [Terms] [Source Code] | https://kling.ai/docs/payment-policy §6.2.3; `CRM_RECHARGE` in tob `Index-KbiV4jEF.js` |

Payment-channel enum (`json-DIpgW6xR.js`): ALIPAY, APPLE, CARD_FRAME, CARD_SUBSCRIBE ("Stripe"), GOOGLE, OFFLINE, PAYPAL, PROVIDER_CASHIER ("Stripe"), REDEEM, SINGLE_PAYMENT ("Stripe"), WECHAT. **Three of the eleven channel labels resolve to Stripe.**

Zero real hits in 1,500 bundles: Adyen, Checkout.com, Braintree, Airwallex, PayerMax, Antom, Razorpay, PayU, Cashfree, Paytm, Xendit, Midtrans, 2C2P, dLocal, EBANX, Paddle, FastSpring, Xsolla, LemonSqueezy, Juspay, Spreedly, Primer, Gr4vy, Yuno, Payrails. (Crawl capped at 1,500 files with 118 chunks uncrawled.)

#### 3B. Payment Orchestrator

**In-house orchestration layer** [Source Code] — medium confidence. A backend cashier returns `supportProviders` and either a Stripe `providerSecret` (embedded) or a `payUrl` (redirect); the client switches only on CN vs GLOBAL. Kuaishou Group runs its own payment gateway (kuaishoupay.com) for China.

> *The layer exists, but on the international side it routes to one acquirer. There is no per-country logic for IN, KR, BR or ID anywhere in the client, and no failover target. Pitch reach and local acquiring, never "you need orchestration" — Kuaishou builds payment infrastructure and will say so.*

---

### Section 4: Alternative & Local Payment Methods

**Pricing & currency:** Global config currency USD. Web plans list in USD (Standard $6.99 first month / $8.80; Pro $25.99 / $32.56; Premier $64.99 / $80.96; Ultra $127.99 / $159.99 — Magic Hour capture, Sep 2026). Stripe **Adaptive Pricing** converts currency at checkout (observed INR charge ₹3,038.83 with paise precision — consistent with FX conversion). **No PPP / regional web pricing found.** The App Store *does* localise: India 100 Credits ₹149, week ₹99/₹149/₹49; Indonesia 100 Credits Rp29rb, week Rp19rb (verified by me).

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| Global | Stripe cards (Visa/MC) | Cards | Active in checkout | kling.ai/docs/payment-policy; PayStripeComponent JS |
| Global | Apple Pay (web) | Digital wallet | Active — single user report, May 2026 | https://www.sikayetvar.com/en/kling-ai-us/unauthorized-charge-for-cancelledkling-aisubscription |
| Global | Google Pay (web) | Digital wallet | Unknown, checkout not accessible | — |
| Global | PayPal | Digital wallet | Configured in code; live status unknown | territory-text JS |
| Global | Apple IAP / Google Play | App store | Active | App Store / Play listings; Terms |
| Global | Crypto | Crypto | Not found | https://www.solcard.cc/blog/pay-kling-ai-with-crypto |
| Enterprise | Offline bank transfer | Bank transfer | Mentioned in docs | kling.ai/docs/payment-policy |
| India | UPI, **UPI Autopay**, RuPay, netbanking, Paytm, EMI | A2A / mandate / cards / instalments | Not found (one PhonePe-UPI user report, channel unstated) | https://www.truefan.ai/blogs/kling-ai-alternatives-india-2026 ; https://www.sikayetvar.com/en/kling-ai-us/kling-ai-refund-request-after-prompt-errors-and-wasted-credits |
| South Korea | KakaoPay, Naver Pay, Toss, domestic-card instalments | Wallets / cards | Not found; Korean guides say billing is USD | https://aijeong.com/%ED%81%B4%EB%A7%81ai-%EA%B5%AC%EB%8F%85%EB%A3%8C-%EA%B0%80%EA%B2%A9-%EC%B4%9D%EC%A0%95%EB%A6%AC/ |
| Brazil | Pix, boleto, parcelamento | A2A / cash / instalments | Not found; reseller Hub Império sells access via Pix | https://hubimperio.com/ |
| Indonesia | QRIS, GoPay, OVO, DANA, VA | A2A / wallets | **Not found** — resellers take QRIS/IDR | https://joinbareng.com/jasa-bayar/kling-ai ; https://www.dibayarin.id/jasa-bayar-kling-ai-premium-dari-indonesia/ |
| Pakistan | JazzCash, Easypaisa, Raast | Wallets / A2A | Not found | — |
| Russia | Mir, SBP | Cards / A2A | Not found; users route via intermediaries | https://vc.ru/services/3081018-kak-kupit-kling-podpisku-iz-rossii |
| Any | Carrier billing, BNPL | — | Not found | — |

> *Warning: In India, UPI is widely used but not currently supported in Kling's web checkout.* NPCI: 24.51bn UPI transactions in Aug 2026 — https://www.business-standard.com/finance/news/upi-transactions-august-2026-record-volume-npci-126090100506_1.html. **Kling bills monthly and yearly auto-renewing plans; UPI Autopay is the local recurring rail.**

> *Warning: In Brazil, Pix is widely used but not currently supported by Kling.* BCB: record 318.07m Pix transactions in one day, 4 Sep 2026 — https://www.metropoles.com/brasil/r-18689-bilhoes-pix-bate-recorde-diario-de-operacao-diz-banco-central

> *Warning: In Indonesia, QRIS is widely used but not currently supported by Kling.* BI: 12.55bn QRIS transactions in H1 2026 — https://www.antaranews.com/berita/5682285/bi-transaksi-qris-capai-1255-miliar-pada-semester-i-2026

> *Warning: In South Korea, easy-pay wallets are widely used but not supported by Kling.* BoK H1 2026: 38.22m easy-pay transactions/day; fintechs hold 55.4% of value — https://biz.newdaily.co.kr/site/data/html/2026/09/18/2026091800179.html

⚠️ **Methodology limit:** Stripe's Payment Element renders methods enabled server-side, so a method could appear at checkout without appearing in client code. The absence claims rest on code + Terms + user/reseller reports together. Frame outreach as "your config lists…", not "you cannot…".

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Failed recurring / charged after cancellation (retries on a cancelled sub) | Trustpilot | High | 2025–Sep 2026 | https://www.trustpilot.com/review/klingai.com |
| Auto-renewal charged, refund refused under policy | Trustpilot | High | Aug–Sep 2026 | same |
| Credits reset / reduced after plan change or renewal | Trustpilot | Moderate | Nov 2025–Sep 2026 | same |
| Duplicate charge, plan not activated (Nigeria, Mastercard 2 × ₦2,320) | Sikayetvar | Isolated | Sep 2026 | https://www.sikayetvar.com/en/kling-ai-us |
| Charged but not credited (Google Play: Indonesia, Chile; web: May 2026) | Sikayetvar | Moderate | May–Sep 2026 | same |
| Unrecognised charge "GOOGLE*KLING AI" RM413.09 | Sikayetvar | Isolated | Sep 2026 | same |
| "Unable to buy kling ai subscription. Getting error" | Facebook group | Isolated | — | https://www.facebook.com/groups/846203050725189/posts/990653489613477/ |
| Workaround-card / crypto vendors marketing to Kling buyers whose local cards fail | Vendor blogs | Moderate (commercial bias) | Jul 2026 | https://www.solcard.cc/blog/pay-kling-ai-with-crypto ; https://help.mp.net/en/articles/15424948-tutorial-subscribing-to-kling-ai-via-mpchat-virtual-card |

Trustpilot aggregate: **1.2/5, 398 reviews, 90% 1-star.** Terms: *"Once the Paid Service … is activated, the fee paid … is non-refundable"*; cancellation within one day of renewal *"may have already processed the deduction."* Reddit not accessed (403).

> *Pattern: the dominant pain is subscription lifecycle — cancellation, renewal and entitlement — not declines. That is mostly Kling's own billing logic and policy, not something routing fixes.* The decline signal is indirect (workaround-card vendors, reseller economy). **Do not lead with complaints and do not claim an approval-rate problem.**

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 2 Jul 2026 | First external round: RMB13.8bn (~US$2.03bn) initial tranche, up to ~RMB19–20bn; Tencent, Alibaba, Baidu among investors; funds "independent commercial operations"; HK IPO intended within ~12 months | Funding | https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0702/2026070204065.pdf ; https://technode.com/2026/07/03/kuaishous-kling-ai-raises-nearly-3-billion-in-funding/ |
| 2 | 2 Jul 2026 | Post-closing obligation: Beijing Kling to acquire 100% of an overseas operating company via ODI | M&A / restructuring | same HKEX PDF |
| 3 | 19 Aug 2026 | Q2 revenue >RMB850M, +200% YoY | Financial | https://www.prnewswire.com/news-releases/kuaishou-technology-announces-second-quarter-and-interim-2026-unaudited-financial-results-302855081.html |
| 4 | Q2 2026 | Kling 3.0 Turbo, native 4K; enterprise API sales tiers to $150k+/month (EN/JA/KO) | Product / enterprise | https://kling.ai/dev/pricing |
| 5 | 21 Apr 2026 | New Terms of Service, Privacy Policy and Terms of Paid Service took effect under Kling AI Pte. Ltd. | Legal / billing | https://kling.ai/docs/payment-policy |

- **No public payment-related RFP found.**
- **No payment/billing job postings found** for Kling. Kuaishou's "Cartão Kwai" Brazil roles relate to Kwai, not Kling.
- Bloomberg (17 Jun 2026) reported General Atlantic in talks to lead at US$18bn; the filed co-lead list differs, so GA's final role is unconfirmed.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 21 Apr 2026 | Terms of Paid Service name Stripe as the auto-renewal payment channel; enterprise prepaid via offline transfer | Confirms single named PSP | https://kling.ai/docs/payment-policy |
| 2 | 2026 | Kling listed on AWS Marketplace | Alternative B2B billing rail for the API | https://aws.amazon.com/marketplace/pp/prodview-6636lqgc4tu2w |
| 3 | 2026 | Indonesian "jasa bayar Kling AI" reseller services accept QRIS/IDR | Market-built workaround for missing rails | https://joinbareng.com/jasa-bayar/kling-ai |

No PSP partnership, provider removal or payments-press coverage found (thepaypers, finextra, pymnts, techinasia, e27). **No removals.**

---

### Section 8: Checkout Experience Audit

*Full checkout flow not accessible (login required; plan page client-rendered). Findings from production code and public pages.*

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | Embedded Stripe Checkout Elements (custom UI); enterprise console uses hosted Stripe redirect | Good | `initCheckoutElementsSdk`, `createPaymentElement` |
| Guest checkout | No — Stripe component renders only when `userLoggedIn` | Fair | Normal for credit-based SaaS |
| Steps to complete payment | Not accessible | — | |
| Card input experience | Stripe iframe (Payment Element), billing name suppressed | Good | |
| Payment methods visible | Config: stripe, paypal (GLOBAL) | Poor for APAC | Stripe server config may add methods — unverified |
| Location-based method display | Binary CN vs GLOBAL only | Poor | No per-country method sets |
| Instalment / EMI options | Not found | Poor | Annual plans to $1,430 with no instalments in IN/KR/BR |
| 3DS implementation | Stripe-managed; card metadata (`cardThreeDSecureUsage`) captured | Fair | No merchant-side 3DS control evident |
| PCI indicator | PSP iframe | Good | |
| Mobile responsiveness | Not assessed; mobile buyers pushed to IAP | — | |
| Multi-currency / local pricing | Stripe Adaptive Pricing (FX presentment) + currency selector; USD list | Fair | App Store has true local price points; web does not |
| Saved payment methods | Yes (`add_payment_method`, default method API) | Good | |
| Error message clarity | Not accessible | — | |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found | — |
| Card data handling | Stripe iframes (Payment Element) | PayStripeComponent JS |
| Recommended Yuno integration | SDK (keep card data in PSP/Yuno iframes) | — |

> `[INFERENCE, not confirmed]`: Based on confirmed use of Stripe's embedded Payment Element, the company's PCI scope is likely reduced (SAQ A-type), with Stripe handling card data.

No direct PCI documentation found publicly for Kling AI.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: Two payment regions for 224 countries**
> **Evidence:** S3 `paymentMethodConfig` CN → alipay/wechatpay/unionpay; GLOBAL → stripe/paypal, USD + S1 India 15.21%, Korea 5.08%, Brazil 4.47%, Indonesia 3.35% + S4 none of UPI/QRIS/Pix/KakaoPay found.
> **Pain Point:** The top four non-US markets are served with a card-first, USD-listed checkout while the dominant local rails are A2A and wallets.
> **Yuno Value Proposition:** One integration above the existing Stripe setup adds UPI, Pix, QRIS and Korean wallets as configuration, not as four PSP projects.
> **Best Success Case:** Vibra — first-time payers in an emerging market (Brazil, Kling's #4), new methods added on top of the existing stack.
> **Outreach Angle:** "Your code has two payment regions: China, with Alipay, WeChat Pay and UnionPay, and everyone else, with Stripe."
> **Suggested Subject Line:** Two regions, 224 countries

> **Insight #2: The app already prices locally; the website doesn't**
> **Evidence:** S4 App Store India ₹149 / ₹99 / ₹49 and Indonesia Rp29rb / Rp19rb SKUs + S4 web USD list with Stripe FX conversion + S1 India #1 market.
> **Pain Point:** The cheapest, most local way to pay Kling in India or Indonesia runs through Apple or Google, at app-store fees; the web — where Kling keeps the margin — offers neither the price point nor the rail.
> **Yuno Value Proposition:** Local rails on web make the direct channel competitive with the app store in the markets where it currently isn't.
> **Best Success Case:** Vibra (new-method launch); pair with a web-vs-app-store fee framing only once they share their split.
> **Outreach Angle:** "Your iOS app sells a ₹99 week in India. Your website sells in dollars on a card."
> **Suggested Subject Line:** ₹99 in the app, USD on the web

> **Insight #3: Recurring billing into India without UPI Autopay**
> **Evidence:** S4 monthly/yearly auto-renewing plans (Terms of Paid Service) + S1 India #1 + S4 no UPI Autopay + S5 high volume of renewal-related complaints.
> **Pain Point:** Recurring card debits in India sit under the RBI e-mandate framework (verify current rules before citing); a US-style card-on-file renewal from a Singapore merchant is the fragile path.
> **Yuno Value Proposition:** Local recurring rail (UPI Autopay) and local acquiring for the renewal, via one integration.
> **Best Success Case:** None vertical-matched; use the subscription reference's mechanism framing, no numbers.
> **Outreach Angle:** For E3 hypothesis only — first renewals from Indian buyers are where a card-only, cross-border stack is weakest.
> **Suggested Subject Line:** India renewals

> **Insight #4: The overseas stack is being rebuilt anyway**
> **Evidence:** S6 ~US$2B round for "independent commercial operations" + HK IPO within ~12 months + ODI acquisition of an overseas operating company + S2 single SG billing entity + S3 single live international PSP.
> **Pain Point:** Separating from Kuaishou's shared infrastructure and moving the overseas opco will reopen payments; single-acquirer dependency is also an IPO-diligence talking point.
> **Yuno Value Proposition:** Add acquirers and rails during the reorganisation instead of after it; failover beyond one PSP.
> **Best Success Case:** Tier-2 pattern match only.
> **Outreach Angle:** Timing hook for E2/E3, never the opener — "independent commercial operations usually means rebuilding a few things you used to borrow."
> **Suggested Subject Line:** After the round

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks:**
1. Your code has two payment regions: China, with Alipay, WeChat Pay and UnionPay, and everyone else, with Stripe.
2. Your iOS app sells a ₹99 week in India and a Rp19rb week in Indonesia; your website sells in dollars on a card.
3. There are Indonesian businesses whose whole product is taking QRIS payments and buying Kling subscriptions on the buyer's behalf.

**Cold call openers:**
1. "India's your biggest market by traffic — how are Indian buyers paying on the web today?"
2. "With the round closed and the overseas entity moving, is payments part of what's being rebuilt?"
3. "What share of your consumer revenue comes through the app stores versus the website?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| Hailuo (MiniMax) | hailuoai.video | China (SG billing) | H1'26 rev US$116.6M | VN, IN, US, BR, KR | Stripe + Airwallex, in-house switch | `2-ready-to-outreach/minimax-io.md` |
| Vidu (Shengshu) | vidu.com | China | Not found | Global | Stripe only (`"global"===SITE?["stripe"]:["alipay"]`) | vidu.com bundle (curl) |
| PixVerse (AIsphere) | pixverse.ai | China / Singapore (conflicting) | ~US$439M Series C, >US$2B valuation (Jul 2026) | Global | Stripe + PayPal + IAP + CN Alipay; no orchestrator | https://techcrunch.com/2026/07/13/video-generation-startup-pixverse-raises-439m-valuation-soars-past-2b/ |
| Runway | runwayml.com | US | >US$200M ARR | Global | Stripe only | https://www.techtimes.com/articles/326994/20260908/runway-ai-hits-200m-arr-enterprise-video-adoption-triples-existing-spend.htm |
| Higgsfield | higgsfield.ai | US | ~US$700M annualised (Sacra est.) | Global | Stripe | https://sacra.com/c/higgsfield/ |
| Luma AI | lumalabs.ai | US | US$4B valuation | Global | Stripe | https://sacra.com/c/luma-ai/ |
| Pika | pika.art | US | Not verified | Global | Stripe | pika.art/pricing bundle (curl) |
| Dreamina / Seedance (ByteDance) | dreamina.capcut.com | Singapore / China | ByteDance | Global | Card + PayPal; acquirer unidentified | https://dreamina.capcut.com/pricing/dreamina-price |

#### 11B. Industry Peers

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Canva | canva.com | Creative SaaS | Global, strong IN | Offers **UPI Autopay** in India — the rail Kling lacks | https://www.canva.com/help/pay-upi-autopay/ |
| Invideo AI | invideo.io | AI video | IN, US, global | **Consolidated onto Stripe** (2023) — expect the "Stripe is enough" objection | https://stripe.com/customers/invideo |
| Meitu (Wink) | meitu.com | AI imaging | CN, APAC | 18.44M paying subscribers; PSP not found | https://www.businesswire.com/news/home/20260827842032/en/ |
| CapCut (ByteDance) | capcut.com | Creative apps | Global | Card + PayPal | as Dreamina |
| MiniMax Talkie | talkie-ai.com | AI companion | Global | Mostly IAP | repo |

#### 11C. Companies Recently Adopting Payment Orchestration

*No public case studies found of direct competitors adopting payment orchestration.* Across eight AI-video competitors, every web checkout inspected is Stripe-first; multi-rail stacks (Hailuo, PixVerse) route in-house. Invideo moved the opposite way.

#### 11D. Prospect Scoring (verified signals only, abbreviated)

| Company | Orchestration | 3+ countries | Multi-PSP | Funding >$10M (12 mo) | Payment issues | Est. score | Note |
|---------|---------------|--------------|-----------|------------------------|----------------|------------|------|
| PixVerse | +4 (none) | ⬜ | +3 (Stripe + PayPal + IAP) | +2 | ⬜ | ~9 + unscored signals | Research-worthy; China/SG HQ — run export check |
| Vidu | +4 (none) | ⬜ | ⬜ | ⬜ | ⬜ | ≥4 | Already TAL P3 |
| Invideo AI | +1 (consolidated Stripe) | ⬜ | ❌ | ⬜ | ⬜ | Low | TAL P1 looks optimistic given the Stripe consolidation |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Kling AI | Target | IN, US, KR, BR | 21 | ⭐ | Two payment regions for 224 countries | ❌ **No row** (only parent Kuaishou) |
| 2 | Hailuo / MiniMax | Direct | VN, IN, US | 23 | ⭐ | Already researched | ✅ P1 |
| 3 | PixVerse | Direct | Global | Partial | 🟢 | US$439M raise, multi-rail no orchestrator | ❌ **Genuine find** |
| 4 | Vidu | Direct | Global | Partial | 🟢 | Hardcoded stripe/alipay binary | ✅ P3 |
| 5 | Meitu | Peer (HKEX 1357) | CN, APAC | Unscored | 🟢 | 18.44M paying subs | ❌ Not in TAL |
| 6 | Canva | Peer | Global | Unscored | — | Already runs UPI Autopay | ✅ |
| 7 | Invideo AI | Peer | IN, US | Low | 🔴 | Consolidated on Stripe | ✅ P1 |

Not ranked: US-HQ competitors (Runway, Higgsfield, Luma, Pika) are out of territory.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | FY2025 ~RMB1.04–1.1bn (~US$150M); H1 2026 >RMB1.5bn; ARR ~US$500M (Mar 2026) | Caixin; HKEX PDF; TechNode |
| GMV / Gross Transaction Volume | Not found | — |
| Average Transaction Value (USD) | Not found as an average. Consumer range $1.19 (IAP week) – $159.99/mo, annual to $1,429.99; credit packs from $5; API contracts to $150k+/mo | Magic Hour; App Store; kling.ai/dev/pricing |
| Est. Annual Transactions | Not calculable from sourced inputs | — |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. [ASSUMPTION — not researched.]** Basis: ~US$39M/month revenue (sourced, Q2 2026) ÷ an unsourced ticket; even at the highest monthly consumer ticket ($160) on 60% of revenue ≈ 146,000. Includes China. | See ICP breakdown |
| Active Customers / Users | 60M+ creators, 30,000+ enterprise users (Dec 2025); >100M users, ~50,000 enterprises (Jun 2026, secondary) | PR Newswire Dec 2025; BigGo (secondary) |
| Primary Currency | USD (global), CNY (China) | Source code |
| Top 3 Markets by Revenue | Not disclosed; ~75% of ARR overseas (secondary only) | Digital Applied |
| Billing channel split (web vs app store) | **Not disclosed** | — |

Net loss (Beijing Kling pro-forma): RMB0.5bn (2024), RMB1.9bn (2025) — HKEX PDF. Kuaishou's "overseas segment" is Kwai, not Kling; Kling sits in "other services".

---

### Overall Research Confidence

**Medium-High.** Traffic was **supplied** (SimilarWeb screenshot) but partial — shares only, top 7 rows, no visit count. PSP stack, region routing, currency handling and card capture are strong: read directly from 1,500 production bundles and the Terms of Paid Service. Entity and financials are strong (HKEX filing, Kuaishou results). Weaker: the logged-in checkout (which methods Stripe actually renders), the web-vs-IAP split, and any sourced transaction count. Complaints are well evidenced but skew to lifecycle issues, not declines. Reddit was not accessed.

---

### Manual Research Recommendations

> **Area:** Monthly transaction count (S12)
> **Why it matters:** The only signal that can reject an account; currently assumed.
> **Suggested manual action:** Ask on the first call, or look for paying-user disclosures in Kuaishou's Q3 results (Nov 2026) or the Kling IPO prospectus.

> **Area:** Logged-in checkout per market (S4, S8)
> **Why it matters:** Stripe may render methods (e.g. UPI, Pix) server-side that the code can't show; the hook must not overclaim.
> **Suggested manual action:** Free account, VPN to India, Brazil, Korea and Indonesia, open the Pro plan checkout, screenshot the Payment Element. Confirm PayPal too.

> **Area:** Web vs app-store revenue split (S12)
> **Why it matters:** The app-store trap. If IAP dominates the consumer book, only the API and web slice is addressable.
> **Suggested manual action:** Discovery question; also check whether the upcoming IPO prospectus discloses channel mix.

> **Area:** Full SimilarWeb export
> **Why it matters:** Ranks 8–121 and absolute visits are missing (Japan, Vietnam, Philippines, Thailand shares unknown).
> **Suggested manual action:** Download the xlsx from the Geography panel and drop it in `accounts/traffic/kling-ai.md`.

> **Area:** Regulatory acquiring gates (S2)
> **Why it matters:** "No local entity" could be a hard gate in India, Korea or Indonesia rather than just a cost issue — a stronger argument, but only if sourced.
> **Suggested manual action:** Pull current RBI / Korean PG / BI rules before using any gating claim.

> **Area:** Contacts
> **Why it matters:** Kling is becoming a standalone company; payments ownership may be moving from Kuaishou group to Kling.
> **Suggested manual action:** Look for Kling overseas commercial/monetisation leads and Kling AI Pte. Ltd. finance; `klingaiapi_overseas@kuaishou.com` surfaced as an overseas API contact.

---

### Appendix: All Source URLs

**S1:** `accounts/traffic/kling-ai.md` (SimilarWeb, supplied 2026-09-28)
**S2:** https://kling.ai/docs/user-policy · https://kling.ai/docs/privacy-policy · https://recordowl.com/company/kling-ai-pte-ltd · https://companieshouse.sg/kling-ai-pte-ltd-202502609E · https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0702/2026070204065.pdf
**S3:** https://kling.ai/docs/payment-policy · production bundles under `https://s15-kling.klingai.com/kos/s101/nlav112918/kling-web/assets/js/` (`territory-text-Dd9qiWMx.js`, `PayStripeComponent-BHQwd1Al.js`, `json-DIpgW6xR.js`, `fns-DGjDubOd.js`, `index-DSwglY3c.js`) and `kling-web-tob/assets/pay-Cxd_gGO5.js` · https://apps.apple.com/us/app/id6738049229 · https://play.google.com/store/apps/details?id=kling.ai.video.chat
**S4:** https://apps.apple.com/in/app/kling-ai-ai-image-video-maker/id6738049229 · https://apps.apple.com/id/app/kling-ai-ai-image-video-maker/id6738049229 · https://magichour.ai/blog/kling-ai-pricing · https://www.eesel.ai/blog/kling-ai-pricing · https://www.truefan.ai/blogs/kling-ai-alternatives-india-2026 · https://toolsly.in/compare-ai-subscription-costs-across-leading-ai-platforms/ · https://aijeong.com/%ED%81%B4%EB%A7%81ai-%EA%B5%AC%EB%8F%85%EB%A3%8C-%EA%B0%80%EA%B2%A9-%EC%B4%9D%EC%A0%95%EB%A6%AC/ · https://note.com/yappyinsta/n/n01dd90acf143 · https://hubimperio.com/ · https://joinbareng.com/jasa-bayar/kling-ai · https://www.dibayarin.id/jasa-bayar-kling-ai-premium-dari-indonesia/ · https://vc.ru/services/3081018-kak-kupit-kling-podpisku-iz-rossii · https://dtf.ru/howto/5149878-oplata-kling-ai-iz-rossii · https://www.business-standard.com/finance/news/upi-transactions-august-2026-record-volume-npci-126090100506_1.html · https://www.metropoles.com/brasil/r-18689-bilhoes-pix-bate-recorde-diario-de-operacao-diz-banco-central · https://www.antaranews.com/berita/5682285/bi-transaksi-qris-capai-1255-miliar-pada-semester-i-2026 · https://biz.newdaily.co.kr/site/data/html/2026/09/18/2026091800179.html
**S5:** https://www.trustpilot.com/review/klingai.com · https://www.sikayetvar.com/en/kling-ai-us · https://www.solcard.cc/blog/pay-kling-ai-with-crypto · https://help.mp.net/en/articles/15424948-tutorial-subscribing-to-kling-ai-via-mpchat-virtual-card · https://www.facebook.com/groups/846203050725189/posts/990653489613477/ · https://rainaiservices.com/reviews/kling-ai/
**S6/S7:** https://technode.com/2026/07/03/kuaishous-kling-ai-raises-nearly-3-billion-in-funding/ · https://www.scmp.com/tech/article/3359250/kuaishou-files-us3-billion-kling-ai-funding-round-hong-kong-stock-exchange · https://www.bloomberg.com/news/articles/2026-06-17/kuaishou-kling-ai-seeks-2-billion-at-18-billion-value-from-general-atlantic · https://www.prnewswire.com/news-releases/kuaishou-technology-announces-second-quarter-and-interim-2026-unaudited-financial-results-302855081.html · https://technode.com/2026/08/20/kuaishous-kling-ai-revenue-tops-rmb850-million-in-q2-up-more-than-200/ · https://www.caixinglobal.com/2026-03-25/kuaishou-ramps-up-ai-commercialization-as-kling-revenue-hits-150-million-102427380.html · https://www.prnewswire.com/news-releases/kling-ai-annualized-revenue-run-rate-hits-usd240-million-in-december-2025-302659847.html · https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-launches-30-model-ushering-era-where-everyone-can-be · https://aws.amazon.com/marketplace/pp/prodview-6636lqgc4tu2w · https://kling.ai/dev/pricing · https://sacra.com/c/kling/ · https://www.digitalapplied.com/blog/kling-ai-3b-funding-18b-valuation-video-revenue-2026 · https://finance.biggo.com/news/2429f0cc-93ae-4da9-b60b-6984bbc3c127
**Export control:** https://www.federalregister.gov/documents/full_text/text/2026/08/24/2026-17231.txt · https://www.treasury.gov/ofac/downloads/sdn.csv · https://www.treasury.gov/ofac/downloads/consolidated/cons_prim.csv · https://www.wilmerhale.com/en/insights/client-alerts/20260611-pentagon-adds-65-new-entities-to-the-1260h-list-of-chinese-military-companies
**S11:** https://techcrunch.com/2026/07/13/video-generation-startup-pixverse-raises-439m-valuation-soars-past-2b/ · https://www.techtimes.com/articles/326994/20260908/runway-ai-hits-200m-arr-enterprise-video-adoption-triples-existing-spend.htm · https://sacra.com/c/higgsfield/ · https://sacra.com/c/luma-ai/ · https://dreamina.capcut.com/pricing/dreamina-price · https://www.canva.com/help/pay-upi-autopay/ · https://stripe.com/customers/invideo · https://www.businesswire.com/news/home/20260827842032/en/Meitu-2026-Interim-Results-AI-Applications-for-Productivity-Continue-to-Break-New-Ground-as-Net-Profit-Grows-39.5-YoY

</details>
