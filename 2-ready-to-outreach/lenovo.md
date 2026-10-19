# Lenovo

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 16 / 29 → 🟢 Medium
**Industry:** Consumer and commercial PCs, tablets, smartphones (Motorola), servers and services, sold through channel partners plus a D2C store on lenovo.com · **HQ:** Registered in Hong Kong; operational HQs in Beijing and Morrisville, NC · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **In-house.** Lenovo runs its own payment aggregation product (LePay, from Lenovo's BASD unit) and a central Global Payments team. No third-party orchestrator was found. Pitch reach and speed-to-market, not "you need orchestration".

---

> ## 🎯 THE HOOK: Lenovo Japan's e-commerce lead said on the record that adding a payment method needs global sign-off
>
> In a June 2025 interview, Lenovo Japan's eCommerce Online Business Manager (暮石龍生) said:
> - Global PC brands, Lenovo included, struggle to add new payment methods country by country, because each one needs approval from global.
> - Japan only got Amazon Pay fast because **the US, which controls the whole system** (「システム全体の主導権を握る米国」), had already rolled it out.
>
> After launch, Amazon Pay passed **10% payment share**. The other methods each lost share evenly, and Lenovo reads that as **net new buyers** who would otherwise have abandoned the cart. The article headline claims cart-page CVR rose 30%+.
>
> Source: [netshop.impress.co.jp/node/14122](https://netshop.impress.co.jp/node/14122), 2025-06-05, fetched and quote verified 2026-10-19. **Caveat: it is an advertorial sponsored by Amazon Japan.**
>
> **Why it matters:** this is the Yuno pitch, said by Lenovo:
> - **Local rails are gated by a US-run central stack.** One local APM on a central platform moved Japan's conversion.
> - **The gap is still there.** Japan's terms of sale list card, bank transfer and instalments only. No konbini or PayPay found.
>
> **Angle:** "Every country waits for the US to adopt a method first." Use reach and time-to-launch, not orchestration-101. Lenovo already runs its own aggregation layer.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Lenovo Group (HKEX 0992) is the world's largest PC maker by its own positioning, with three groups:
- **IDG:** PCs, tablets, Motorola phones
- **ISG:** servers and storage
- **SSG:** services

FY2025/26 revenue was reported at **US$83.1B, +20% YoY**. Region split: Americas 34%, EMEA 25%, China 22%, Asia Pacific excluding China 19% `[UNVERIFIED — search summary only]`. D2C runs on lenovo.com, which has country storefronts.

**SimilarWeb total visits (last full month):** **42.54M avg/month** (lenovo.com, Jul–Sep 2026; 127.6M over the quarter). Source: SimilarWeb (supplied 2026-10-19), `accounts/traffic/lenovo.md`.

**Caveats from the supplied file:**
- It is the Sales Intelligence view: top 10 countries by share only, with no per-country visit counts. Per-country figures below are derived.
- It covers desktop and mobile web only. App traffic is excluded.
- It covers lenovo.com only. **China's D2C store is shop.lenovo.com.cn (a separate domain, not in the file)**, so China's 3.85% understates Lenovo China online demand. **motorola.com is also not included.**
- B2B, reseller and retail channels are not reflected. Most of Lenovo's revenue is channel, so traffic is a D2C signal only.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇺🇸 United States *(out of territory)* | 21.71% | PayPal Pay Monthly, Pay in 4, Katapult, Amazon Pay, cards | Not assessed: out of territory | Not researched |
| 2 | 🇮🇳 **India** | 14.93% | Credit/debit cards (domestic and international), **UPI**, net banking, wallet, credit-card EMI and No Cost EMI | RuPay not named; **cardless EMI / debit-card EMI / BNPL not found** | ✅ Lenovo India Pvt Ltd, CIN U72900KA2005PTC035783 (⚠️ conflicting NDSL page, see S2) |
| 3 | 🇯🇵 **Japan** | 5.47% | Credit card, bank transfer (prepay), JACCS shopping-credit instalments, Amazon Pay | **Konbini, PayPay, Paidy (standalone)** not found | ✅ レノボ・ジャパン合同会社 (Lenovo Japan LLC) |
| 4 | 🇧🇷 Brazil *(out of territory)* | 4.35% | Not assessed | Not assessed | Not researched |
| 5 | 🇨🇳 **China** | 3.85% | **Unknown**: the D2C store is shop.lenovo.com.cn, and its checkout was not accessed | Unknown | ✅ 联想（北京）有限公司 (Lenovo (Beijing) Ltd), named in the shop.lenovo.com.cn account agreement |

**Other in-territory market:** 🇮🇩 Indonesia, 2.34%. **No D2C store**: the lenovo.com/id/id/ page meta is `storeType="indirect"` and points to "Where to Buy". The APM gap is moot here. PT Lenovo Indonesia exists `[UNVERIFIED — search summary only]`.

### Legal entities
- Lenovo India Private Limited (India). CIN U72900KA2005PTC035783. Named operator of the lenovo.com/in store ([T&C](https://www.lenovo.com/in/en/terms-and-conditions/), fetched)
- レノボ・ジャパン合同会社 / Lenovo Japan LLC (Japan). Seller for everything except ThinkSystem/ThinkAgile, which is sold by レノボ・エンタープライズ・ソリューションズ合同会社 ([selling agreement](https://www.lenovo.com/jp/ja/selling-agreement/public), fetched). Corporate number 2010401057479 per a third-party database `[UNVERIFIED]`
- 联想（北京）有限公司 / Lenovo (Beijing) Ltd (China). Named in the [shop.lenovo.com.cn](https://shop.lenovo.com.cn/) account agreement (fetched)
- Lenovo (Singapore) Pte Ltd, Lenovo (Australia & New Zealand) Pty Ltd, Lenovo (Hong Kong) Ltd, PT Lenovo Indonesia `[UNVERIFIED — search summary only]`

### Known PSPs
- **Worldpay**: named as an integrated channel in Lenovo's own LePay product page `[Provider Case Study]` ([basd.lenovo.com](https://basd.lenovo.com/en/ProductandServices/ValueChain/Sales/unifiepay.html), fetched). The page does not say which storefronts use it.
- **PayPal via Braintree**: Braintree JS SDK v3.76.2 is in the shared lenovo.com bundle `[Source Code]`. The bundle is global, so this does **not** prove PayPal is live in India or Japan.
- **Amazon Pay**: Japan, since mid-Oct 2024, and US before that `[Press Release]` (impress, fetched)
- **JACCS** (shopping credit / instalments): Japan `[Checkout docs]` ([lenovo.com/jp](https://www.lenovo.com/jp/ja/partner/jaccs-tejun/), per Agent 3 fetch)
- **Razorpay**: India. **Only a customer's claim** in one complaint ("Razorpay (your payment partner)") `[Third-Party Report]` ([consumercomplaints.in](https://www.consumercomplaints.in/lenovo-refund-not-received-invalid-reference-id-provided-urgent-resolution-required-c3530660))
- **Klarna**: 15 European markets, Nov 2024 `[UNVERIFIED — search summary only]`. Out of territory.
- **2C2P**: Lenovo listed as a client on secondary pages, market unknown `[UNVERIFIED — search summary only]`

### Orchestration status
**In-house orchestration layer (probable).** The evidence:
- Lenovo's own **"Digital Payment System – LePay"** describes "global unified digital payment" that covers "China, North America, South America, Europe, and Asia Pacific" and "Integrate[s] mainstream channels… WeChat, Alipay, Worldpay, Amazon, Paypal, Apple Pay, Google Pay" ([basd.lenovo.com](https://basd.lenovo.com/en/ProductandServices/ValueChain/Sales/unifiepay.html), fetched).
- Lenovo has a central "Global Payments team" hiring a Product Manager, Payments Platforms `[UNVERIFIED — job page 404, search summary only]`.
- The Japan interview says the US controls the overall system.
- No Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails or Yuno found.

**Caveat:** no source states that LePay is what runs lenovo.com checkout.

### Buying signals
- 🗣️ Lenovo Japan e-com lead publicly names **slow per-country payment-method rollout under global control** as a constraint; one new method lifted conversion ([impress, 2025-06-05](https://netshop.impress.co.jp/node/14122))
- 💼 Payments hiring `[UNVERIFIED — search summary only]`:
  - Product Manager, Payments Platforms (Global Payments team; [jobs.lenovo.com](https://jobs.lenovo.com/en_US/careers/JobDetail/Product-Manager-Payments-Platforms/76986), page now 404)
  - Product Manager, Subscription Payments (Mexico, ~Jul 2026; [jobs.lenovo.com](https://jobs.lenovo.com/en_US/careers/JobDetail/Product-Manager-Subscription-Payments/79856))
- 🚀 Q1 FY26/27 revenue of US$26.9B, +43% YoY, the "strongest quarter in group history" ([zawya press release](https://www.zawya.com/en/press-release/companies-news/lenovo-delivers-strongest-quarter-in-group-history-hybrid-ai-strategy-powers-growth-momentum-437812)) `[UNVERIFIED — search summary only]`
- 🤝 Infinidat acquisition closed Apr 2026 (ISG, enterprise storage, so not payment-relevant) ([Lenovo newsroom](https://news.lenovo.com/pressroom/press-releases/lenovo-completes-acquisition-of-infinidat-expanding-enterprise-storage-portfolio-enhancing-ai-driven-data-infrastructure/)) `[UNVERIFIED — search summary only]`

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach lenovo` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 16 / 29
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | +5 | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. [ASSUMPTION — not researched.]** Basis: 42.54M avg monthly web visits (supplied) × an assumed 0.3–0.5% D2C conversion ≈ 128k–213k orders/month. A third-party estimate of lenovo.com 2024 GMV, US$2.65B (ECDB, `[UNVERIFIED]`), at an assumed ~US$800 AOV gives ~276k/month. Neither the conversion rate, the GMV nor the AOV is sourced. The billing unit is one lenovo.com order, excluding channel/B2B and China's shop.lenovo.com.cn. With a group revenue of US$83B, the 40k floor is not a realistic risk, but the figure is still an assumption. |
| Orchestration status | +1 | ✅ In-house layer (LePay, Lenovo's own aggregation product, plus a central Global Payments team). Its link to lenovo.com checkout is probable, not proven. |
| 3+ countries | +3 | ✅ US 21.71, IN 14.93, JP 5.47, BR 4.35, CN 3.85, plus 5 more over 1% (supplied). Entities confirmed in IN, JP, CN. |
| Multiple PSPs | +3 | ✅ Worldpay (LePay page), Amazon Pay (JP, fetched), JACCS (JP), PayPal/Braintree (source code) |
| Local rail or licensing gap in a top-3 market | 0 | ⬜ Top 3 are US, IN, JP. India has UPI, net banking, wallet and EMI (T&C, fetched). Japan's terms list "card, bank transfer, instalments, etc." (「など」), and no konbini or PayPay was found. But "etc." means the list is not exhaustive (Amazon Pay is live and not listed), so the absence is **not sourced**. Verify by walking the JP checkout. |
| Recent expansion | 0 | ❌ No APAC market launch in the last 12 months. The Saudi plant (EMEA) and Infinidat (storage) don't count. |
| Payment issues reported | 0 | ⬜ One verified India case (UPI debited, no order, untraceable refund reference, Jun 2025). Trustpilot refund/cancellation complaints are moderate but summary-only. |
| Funding >$10M | 0 | ❌ Public company, no funding round |
| High traffic outside home | +2 | ✅ China (home) is 3.85% of lenovo.com traffic. The CN store sits on another domain, but even generously China is far below 60%. |
| Competitor using orchestration | +2 | ✅ OnePlus (competes with Motorola in India) runs Juspay Payment Orchestration ([juspay.io](https://juspay.io/customer-stories/oneplus), fetched). Xiaomi: Juspay (case-study page 403, summary only) plus Adyen across 18 markets ([adyen.com](https://www.adyen.com/press-and-media/adyen-provides-payments-solutions-to-xiaomi), fetched). |
| Payment job postings | 0 | ⬜ Payments-platform and subscription-payments PM roles appear in search results, but the one fetched returned 404. Undated or unverified. |

**Tier:** 16 → 🟢 Medium. No RFP override. **No analyst override applied.** The case for each direction:
- **Up:** the Japan interview is close to a first-party statement of the exact pain Yuno solves, and volume is very large.
- **Down:** Lenovo built its own aggregation product (LePay) and markets it externally. This is the hardest motion: argue reach and opportunity cost, never "you need orchestration". The India merchant of record is also ambiguous (see S2).

On balance, Medium stands.

### Source Notes
- ✅ India store operator is **Lenovo India Private Limited**, CIN U72900KA2005PTC035783, Bangalore. Payment modes: "Domestic and international Credit cards & Debit cards, UPI, Net banking". Also "Credit card, Debit Card, Internet banking, Wallet or EMI Option". Card data "taken directly by the payment gateway". Source: [lenovo.com/in/en/terms-and-conditions](https://www.lenovo.com/in/en/terms-and-conditions/), fetched 2026-10-19.
- ⚠️ **Conflict:** [lenovo.com/in/en/payment-delivery](https://www.lenovo.com/in/en/payment-delivery/) (also live, fetched by agents) says "shoplenovo.co.in is independently operated by Net Distribution Services Private Limited". It says card statements show NDSL, and it lists cards and net banking but **not UPI**. It references the legacy domain and VbV/SecureCode, so it is probably stale boilerplate. **Both are live Lenovo pages; who is merchant of record in India is unresolved.**
- ✅ Japan seller entities and payment methods: card, bank transfer, instalments "etc." ([selling agreement](https://www.lenovo.com/jp/ja/selling-agreement/public), fetched)
- ✅ Japan Amazon Pay launch, mid-Oct 2024, >10% share, and the "global approval" quote ([impress](https://netshop.impress.co.jp/node/14122), fetched, Amazon-sponsored)
- ✅ LePay aggregates WeChat, Alipay, Worldpay, Amazon, PayPal, Apple Pay, Google Pay across CN/NA/SA/EU/APAC ([basd.lenovo.com](https://basd.lenovo.com/en/ProductandServices/ValueChain/Sales/unifiepay.html), fetched)
- ✅ China D2C store (shop.lenovo.com.cn) account agreement names 联想（北京）有限公司 (fetched)
- ✅ Indonesia lenovo.com page is `storeType="indirect"` (fetched by Agent 3)
- ⚠️ Japan card charges "processed overseas on GMT", which would suggest offshore acquiring ([lenovo.com/jp outlet popup](https://lenovo.com/jp/outlet/ja/merchandising/selling-agreement/popup-forwinfo)) `[UNVERIFIED — search summary only, page not fetched]`. Not found in the main selling agreement.
- ⚠️ Worldpay consolidated Lenovo's domestic acquirers, Japan first, then US/Canada (Motley Fool on a 2019 Worldpay earnings call) `[UNVERIFIED — search summary only]`. That is 7 years old.
- ⚠️ Razorpay in India: one customer's statement only
- ⚠️ All FY25/26 and Q1 FY26/27 financials: search summaries of press releases, not fetched
- ⚠️ `apac-tal.csv` row: PSP and orchestrator columns are blank; revenue "~$57B (FY24/25)" is **outdated**. Reported FY24/25 revenue was US$69.1B and FY25/26 US$83.1B `[UNVERIFIED — search summary only]`.

### Success Case Alternatives
- **inDrive**: 50+ countries, new countries launched fast ([y.uno](https://y.uno/en/success-stories/indrive)). Best match for the "every new APM per country is a central-team project" pain, as a pattern for one integration across many markets. It is not a hardware case.
- **Rappi**: large, multi-market, already sophisticated in-house payments ([y.uno](https://www.y.uno/en/success-stories/rappi)). Use it only if discovery shows Lenovo's team thinks "we already built this".
- There is no Yuno consumer-electronics case in this repo. Do not imply one.

---

## Executive Summary

Lenovo sells PCs, phones (Motorola), servers and services globally. lenovo.com averages 42.5M visits/month, and India (14.9%) and Japan (5.5%) are its #2 and #3 markets after the US.

It is not greenfield:
- Lenovo runs an in-house payment aggregation product (LePay) that integrates Worldpay, PayPal, Amazon Pay, Alipay, WeChat Pay and the wallets.
- A central, US-led team controls which methods each country gets.

The opening is what Lenovo Japan's e-commerce lead described on the record:
- Adding a local method needs global approval.
- The one method that got through (Amazon Pay) passed 10% share and grew net buyers.

**Motion: in-house.** Sell reach and time-to-market for local rails, not orchestration itself.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** Path 1, pasted SimilarWeb data (`accounts/traffic/lenovo.md`, supplied 2026-10-19). Jul–Sep 2026, worldwide, desktop + mobile web, lenovo.com only.

- Average monthly visits: 42.54M
- Device split: desktop 48.20%, mobile web 51.80%
- Global rank: not captured

Per-country visits are `[DERIVED from supplied share, not a SimilarWeb figure]`.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | United States | 21.71% | ~9.24M [DERIVED] | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | **India** ⭐ | 14.93% | ~6.35M [DERIVED] | Not supplied | same |
| 3 | **Japan** ⭐ | 5.47% | ~2.33M [DERIVED] | Not supplied | same |
| 4 | Brazil | 4.35% | ~1.85M [DERIVED] | Not supplied | same |
| 5 | **China** | 3.85% | ~1.64M [DERIVED] | Not supplied | same |
| 6 | Germany | 3.44% | ~1.46M [DERIVED] | Not supplied | same |
| 7 | Canada | 3.24% | ~1.38M [DERIVED] | Not supplied | same |
| 8 | France | 2.74% | ~1.17M [DERIVED] | Not supplied | same |
| 9 | **Indonesia** | 2.34% | ~1.00M [DERIVED] | Not supplied | same |
| 10 | United Kingdom | 2.28% | ~0.97M [DERIVED] | Not supplied | same |

The top 10 account for 64.35%. The remaining 35.65% is spread across unlisted countries, which may include more APAC markets such as AU, SG, KR, PH and TW. **Unknown.**

**Caveats (from the supplied file):**
1. Sales Intelligence view: top 10 countries only, by share.
2. Single-domain shares.
3. Mobile app traffic is excluded.
4. D2C web only. B2B, reseller and retail are not reflected.

**Additional caveats found in research:**
- China's D2C store is **shop.lenovo.com.cn** (fetched, 200), which is not in the supplied file, so China's real online demand is understated.
- Indonesia traffic lands on a **non-transacting** page (`storeType="indirect"`).

**In-territory markets with >5% share:** India and Japan, both high priority. Both have a confirmed local entity (S2).

---

### Section 2: Legal Entities & Local Presence

**Headquarters:**
- Registered office in Hong Kong. Operational HQs in Beijing and Morrisville, North Carolina `[UNVERIFIED — secondary sources: Wikipedia, clay.com]`.
- Listed on HKEX (0992).
- Lenovo started D2C on lenovo.com in 2006 and runs in 34 direct countries `[UNVERIFIED — undated CMO interview, therobinreport.com]`.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| India | Lenovo India Private Limited (registered office RBD Icon, Marathahalli ORR, Bangalore 560037) | CIN U72900KA2005PTC035783 | [lenovo.com/in/en/terms-and-conditions](https://www.lenovo.com/in/en/terms-and-conditions/) (fetched) |
| India (conflicting) | Net Distribution Services Pvt Ltd (NDSL), a distributor named as store operator on the payment-delivery page | Not found | [lenovo.com/in/en/payment-delivery](https://www.lenovo.com/in/en/payment-delivery/) (fetched by agents) |
| Japan | レノボ・ジャパン合同会社 (Lenovo Japan LLC). ThinkSystem/ThinkAgile are sold by レノボ・エンタープライズ・ソリューションズ合同会社 | 2010401057479 `[UNVERIFIED — third-party database data-max.co.jp]` | [lenovo.com/jp/ja/selling-agreement/public](https://www.lenovo.com/jp/ja/selling-agreement/public) (fetched) |
| China | 联想（北京）有限公司 (Lenovo (Beijing) Ltd) | Not found | [shop.lenovo.com.cn](https://shop.lenovo.com.cn/) account agreement (fetched) |
| Indonesia | PT Lenovo Indonesia (Wisma 46, Jakarta) | Not found | [PremiumCare terms PDF](https://static.lenovo.com/asean/premiumcare/PremiumCare%20Terms%20-ID_v1.1%20-%20bilingual.pdf) `[UNVERIFIED — search summary only]` |
| Singapore | Lenovo (Singapore) Pte Ltd | Not found | [lenovo.com/sg/en/terms-and-conditions](https://www.lenovo.com/sg/en/terms-and-conditions) `[UNVERIFIED — search summary only]` |
| Australia / NZ | Lenovo (Australia & New Zealand) Pty Ltd | Not found | [lenovo.com/au/en/legal/new-products-and-warranty-services](https://www.lenovo.com/au/en/legal/new-products-and-warranty-services/) `[UNVERIFIED — search summary only]` |
| Hong Kong | Lenovo (Hong Kong) Ltd | Not found | [lenovo.com/hk/en/cart](https://www.lenovo.com/hk/en/cart) `[UNVERIFIED — search summary only]` |

**Cross-Border Gap Analysis (in-territory markets only):**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| India | ✅ #2 | ✅ Yes (MoR conflict with NDSL) | Not assessed: entity exists | Low on entity. **But who owns the gateway contract, Lenovo or NDSL, is unresolved.** |
| Japan | ✅ #3 | ✅ Yes | n/a | **Possible.** One unverified Lenovo page says card charges are processed overseas on GMT, and Worldpay reportedly consolidated Lenovo's Japan acquiring (2019, unverified). If true, Japanese-issued cards are being acquired offshore, which is an approval-rate argument. **Verify before use.** |
| China | ✅ #5 | ✅ Yes | n/a (local entity, separate .cn store) | Low |
| Indonesia | ✅ #9 | ⚠️ Probable (unverified) | Moot | No D2C store |

No top-5 in-territory market lacks an entity, so the regulatory-gate escalation does not apply.

> **MANUAL:**
> - Resolve the India merchant of record. Place a test order to the payment step on lenovo.com/in and check the merchant name on the gateway page.
> - In Japan, check the descriptor and whether 3DS is issuer-domestic.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Global, incl. APAC (storefronts unspecified) | Worldpay; WeChat Pay; Alipay; PayPal; Amazon Pay; Apple Pay; Google Pay, as channels in LePay | [Provider Case Study] (Lenovo's own product page) | https://basd.lenovo.com/en/ProductandServices/ValueChain/Sales/unifiepay.html (fetched) |
| Global (JP first, then US/CA) | Worldpay, consolidating multiple domestic acquirers | [Third-Party Report] `[UNVERIFIED — search summary only]`, 2019 | https://www.fool.com/investing/2019/03/06/3-reasons-worldpay-is-a-buy.aspx |
| Global storefront code | Braintree (PayPal) JS SDK 3.76.2 | [Source Code] | https://www.lenovo.com/in/en/ (fetched; shared global bundle, **not proof of PayPal in IN**) |
| Japan | Amazon Pay (since mid-Oct 2024) | [Press Release] (Amazon-sponsored) | https://netshop.impress.co.jp/node/14122 (fetched) |
| Japan | JACCS shopping credit (1–60 payments, interest-free up to 48) | [Checkout docs] | https://www.lenovo.com/jp/ja/partner/jaccs-tejun/ (Agent 3 fetch) |
| India | Gateway not named: "the payment gateway provided" / "third party gateways" | [Terms/Privacy Policy] | https://www.lenovo.com/in/en/terms-and-conditions/ (fetched) |
| India | Razorpay, per a customer's complaint ("your payment partner") | [Third-Party Report] (customer claim, single) | https://www.consumercomplaints.in/lenovo-refund-not-received-invalid-reference-id-provided-urgent-resolution-required-c3530660 |
| India (old) | Paytm (2016 cashless tie-up), Pine Labs (EMI) | [Press Release] `[UNVERIFIED]`, likely retail/obsolete | https://www.indiaretailing.com/?p=80101 |
| US | Amazon Pay; PayPal Pay Monthly; Katapult | [Checkout docs] | https://www.lenovo.com/us/en/landingpage/lenovo-financing-options (Agent 3 fetch) |
| EU (15 countries) | Klarna | [Press Release] `[UNVERIFIED]` | https://thepaypers.com/ecommerce/klarna-and-lenovo-partner-to-expand-payments-in-europe--1271124 |
| AU/NZ | PayPal, Zip, Latitude | [Checkout docs] `[UNVERIFIED]` | https://lenovo.com/au/en/shopping-faqs/lenovo-payment-options |
| Global B2B | TreviPay (net terms) | [Provider Case Study] `[UNVERIFIED]` | https://trevipay.com/wp-content/uploads/2025/01/TreviPay-Lenovo-CaseStudy-Deutsch.pdf |
| SEA (unspecified) | 2C2P lists Lenovo as a client | [Third-Party Report] `[UNVERIFIED]` | https://thepaypers.com/company/2C2P/295 |

**Not found:**
- No Adyen, Stripe, Checkout.com or Cybersource link to Lenovo.
- No Japanese PSP (GMO-PG, SBPS, Veritrans, KOMOJU).
- No Indonesian PSP (Xendit, Midtrans, Doku).

#### 3B. Payment Orchestrator

**Classification: In-house orchestration layer** `[Provider Case Study]` + `[Job Listing, unverified]`.
- Lenovo's "Digital Payment System – LePay" is a "global unified digital payment" platform with "standardized payment products" that aggregates domestic and overseas channels across China, the Americas, Europe and APAC ([basd.lenovo.com](https://basd.lenovo.com/en/ProductandServices/ValueChain/Sales/unifiepay.html)). Lenovo also sells it externally.
- A Lenovo "Global Payments team" was hiring a Product Manager, Payments Platforms, covering PSPs, gateways, acquirers, tokenization and PCI `[UNVERIFIED — search summary; page 404]`.
- The Japan interview says the **US controls the overall system** and approves each new method (fetched).
- **No third-party orchestrator found:** Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno.

**Motion:** in-house. Never pitch "you need orchestration". Argue the opportunity cost of central-team bandwidth:
- The time it takes for a market to get its local rails (Japan waited on the US to adopt Amazon Pay).
- The rails that are still missing.

> **MANUAL:** walk JP and IN checkout with DevTools to see whether card fields come from a Worldpay, Braintree or other iframe, and what the gateway redirect in India is.

---

### Section 4: Alternative & Local Payment Methods

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| India | Credit & debit cards (domestic + international) | Cards | Mentioned in docs | [IN T&C](https://www.lenovo.com/in/en/terms-and-conditions/) (fetched) |
| India | UPI | Bank transfer / A2A | Mentioned in docs | IN T&C (fetched); also confirmed in use by the [complaint](https://www.consumercomplaints.in/lenovo-refund-not-received-invalid-reference-id-provided-urgent-resolution-required-c3530660) (PhonePe UPI) |
| India | Net banking | Bank transfer / A2A | Mentioned in docs | IN T&C (fetched) |
| India | Wallet (unnamed) | Digital wallet | Mentioned in docs | IN T&C (fetched) |
| India | Credit-card EMI and No Cost EMI | BNPL/Instalments | Mentioned in docs | IN T&C (fetched); [no-cost-emi page](https://www.lenovo.com/in/en/no-cost-emi/) (Agent 4 fetch) |
| India | RuPay | Cards | Not found (not named) | — |
| India | Debit-card EMI / cardless EMI / BNPL | BNPL/Instalments | Not found. The no-cost-emi page lists credit-card EMI only | [no-cost-emi](https://www.lenovo.com/in/en/no-cost-emi/) |
| India | Cash on delivery | Cash | T&C says "on delivery of the Products (if available)". Not confirmed active | IN T&C (fetched) |
| Japan | Credit card | Cards | Mentioned in docs | [JP selling agreement](https://www.lenovo.com/jp/ja/selling-agreement/public) (fetched) |
| Japan | Bank transfer (prepay) | Bank transfer | Mentioned in docs | same |
| Japan | JACCS shopping credit (up to 60 payments) | BNPL/Instalments | Mentioned in docs | [jaccs-tejun](https://www.lenovo.com/jp/ja/partner/jaccs-tejun/) |
| Japan | Amazon Pay (incl. its pay-later option) | Digital wallet | Mentioned in press, live since Oct 2024 | [impress](https://netshop.impress.co.jp/node/14122) (fetched) |
| Japan | Konbini | Cash/voucher | Not found | — |
| Japan | PayPay / Rakuten Pay / LINE Pay | Digital wallet | Not found | — |
| Japan | Paidy (standalone) | BNPL | Not found | — |
| Japan | Carrier billing | Carrier billing | Not found | — |
| China | Alipay / WeChat Pay / UnionPay | Wallet / Cards | Unknown, checkout not accessible (shop.lenovo.com.cn). LePay integrates Alipay and WeChat | [basd.lenovo.com](https://basd.lenovo.com/en/ProductandServices/ValueChain/Sales/unifiepay.html) |
| Indonesia | QRIS, VA, GoPay/OVO/DANA, Alfamart | — | N/A: no D2C store (`storeType="indirect"`) | https://www.lenovo.com/id/id/ |
| Global | PayPal | Digital wallet | Mentioned in docs (US, AU). In IN/JP only the shared SDK appears | US financing page |
| Global | Apple Pay / Google Pay | Digital wallet | Not found on any lenovo.com storefront page. Listed only as LePay channels | — |

> *Warning (Japan, conditional):* konbini and PayPay were not found on Lenovo Japan's store. The terms list card, bank transfer and instalments "etc.", and Amazon Pay is live but not listed, so the absence is **not proven**. Lenovo's own e-com lead says adding any method needs global approval, which makes the gap plausible. **Verify on checkout before using it in outreach.** No source for PayPay's or konbini's prominence was pulled in this run; source one before quoting market-share figures.

> **MANUAL:** Use a VPN or JP proxy to load a lenovo.com/jp cart and screenshot the payment step.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| UPI/wallet-specific failure: UPI debited (₹65,951), no order created, refund reference rejected as invalid by Razorpay and the bank | ConsumerComplaints.in | Isolated | Jun 2025 | https://www.consumercomplaints.in/lenovo-refund-not-received-invalid-reference-id-provided-urgent-resolution-required-c3530660 (fetched by Agent 4) |
| Slow refunds / cancellations (UK refund ~7 weeks; chatbot cancellation loop) | Trustpilot | Moderate `[UNVERIFIED — search summary only]` | Undated | https://www.trustpilot.com/review/www.lenovo.com?page=6 ; https://nz.trustpilot.com/review/www.lenovo.co.uk?page=5 |
| Duplicate charges after partial cancellation | Steam forum | Isolated `[UNVERIFIED]` | Unknown | https://steamcommunity.com/discussions/forum/12/38596748070144795/ |
| Older India refund delays | Voxya / ConsumerComplaints.in | Isolated, 2018–2021 `[UNVERIFIED]` | 2018–2021 | https://voxya.com/consumer-complaints/replacement-refund-of-laptop-adapter/135572 |

No Reddit threads were found, X was not searched, and no complaints were found for Japan or China.

> *Pattern (weak, one case):* in India, a successful UPI debit that never became an order, with no traceable refund reference, points to a payment-to-order reconciliation gap. It is too thin to lead with. Use it only as a discovery question.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 2026-08-13 | Q1 FY26/27 revenue of US$26.9B (+43% YoY), "strongest quarter in group history" | Tech / financial | https://www.zawya.com/en/press-release/companies-news/lenovo-delivers-strongest-quarter-in-group-history-hybrid-ai-strategy-powers-growth-momentum-437812 `[UNVERIFIED — search summary only]` |
| 2 | ~2026-07-24 | Product Manager, Subscription Payments role (Mexico): recurring billing, retries, credential management | Payment Infrastructure Hiring | https://jobs.lenovo.com/en_US/careers/JobDetail/Product-Manager-Subscription-Payments/79856 `[UNVERIFIED — search summary only]` |
| 3 | 2026-06-12 | Global E-Commerce Director role posted (Chicago) | Leadership / hiring | https://jobs.lenovo.com/en_US/careers/JobDetail/Global-E-Commerce-Director/78823 `[UNVERIFIED]` |
| 4 | 2026-04-09 | Infinidat acquisition closed (ISG storage) | M&A | https://news.lenovo.com/pressroom/press-releases/lenovo-completes-acquisition-of-infinidat-expanding-enterprise-storage-portfolio-enhancing-ai-driven-data-infrastructure/ `[UNVERIFIED — search summary only]` |
| 5 | 2025-06 | Rajesh Thadani moves from APAC eCommerce Executive Director to APAC One Channel Leader, so the APAC e-com head may have changed | Leadership Change | https://www.crnasia.com/news/2025/channel-news/lenovo-unveils-new-asia-pacific-one-channel-leader `[UNVERIFIED]` |

**Undated:** Product Manager, Payments Platforms, Global Payments team ([jobs.lenovo.com/…/76986](https://jobs.lenovo.com/en_US/careers/JobDetail/Product-Manager-Payments-Platforms/76986), now 404). The Saudi Alat manufacturing JV is EMEA and out of territory.

**No public payment-related RFP found.** No payment-licence application found.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 2025-06-05 | Lenovo Japan: Amazon Pay passed 10% share after its Oct 2024 launch. The e-com lead says new methods need global approval | **High.** First-party statement of central-stack friction | https://netshop.impress.co.jp/node/14122 (fetched; Amazon-sponsored) |
| 2 | 2024-11 | Klarna BNPL live on lenovo.com in 15 European markets | Medium. Shows Lenovo adds methods regionally, but via central partnerships | https://thepaypers.com/ecommerce/klarna-and-lenovo-partner-to-expand-payments-in-europe--1271124 `[UNVERIFIED]` |
| 3 | 2024-07 | Amex India Lenovo EMI offer terms | Low | https://americanexpress.com/content/dam/amex/en-in/benefits/Lenovo_EMI_Offer_TnC_July24.pdf `[UNVERIFIED]` |
| 4 | Undated | Lenovo BASD markets LePay, its own unified payment platform | High. Defines the in-house motion | https://basd.lenovo.com/en/ProductandServices/ValueChain/Sales/unifiepay.html (fetched) |
| 5 | 2019-03 | Worldpay CEO cites Lenovo consolidating domestic acquirers onto Worldpay (Japan first) | Medium. Old; whether it still holds is unknown | https://www.fool.com/investing/2019/03/06/3-reasons-worldpay-is-a-buy.aspx `[UNVERIFIED]` |

No provider removals found.

---

### Section 8: Checkout Experience Audit

*Full checkout flow not accessible. Findings are limited to publicly observable elements on lenovo.com/in and /jp policy pages.*

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | India: "EMI options available on selected banks at Checkout/Payment Gateway page" (homepage resource string), which suggests a redirect or hosted gateway | Fair | Not verified live |
| Guest checkout | Not confirmed | — | "guest" strings may be wishlist labels |
| Steps to complete payment | Japan: JACCS flow shown as checkout step 2/2 | — | Agent 3 fetch |
| Card input experience | India T&C: card data "taken directly by the payment gateway" | — | Hosted/iframe likely |
| Payment methods visible | IN: cards, UPI, net banking, wallet, EMI. JP: card, bank transfer, JACCS, Amazon Pay | Fair | |
| Location-based method display | Per-country storefronts with different method sets | Fair | Central approval per method (impress) |
| Instalment / EMI options | IN: credit-card EMI and No Cost EMI. **Conflicting terms:** homepage says Rs 15,000 min and 3/6 months; the no-cost-emi page says 3/6/9/12 months; the T&C says 6 and 9 months; the payment-delivery page says Rs 40,000 min. JP: JACCS up to 60 payments | Fair | No debit or cardless EMI in IN |
| 3DS implementation | IN T&C still references VbV / Mastercard SecureCode (3DS1-era wording) | Poor (documentation) | Actual 3DS version not detected |
| PCI indicator | Gateway-taken card data (IN) | — | See S9 |
| Mobile responsiveness | Not tested | — | Traffic is 51.8% mobile web |
| Multi-currency / local pricing | IN: INR only; foreign cards bear issuer FX | Fair | |
| Saved payment methods | "My Wallet" saved cards and a "$1.00 temporary authorization" string in the global bundle | — | Market not confirmed |
| Error message clarity | Not tested | — | |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found | — |
| Card data handling | India: "Credit card and Debit card information is not stored by us and is not taken by us. This information is taken directly by the payment gateway" | [IN T&C](https://www.lenovo.com/in/en/terms-and-conditions/) (fetched) |
| Recommended Yuno integration | Back-to-back API alongside the in-house LePay layer, or SDK for specific market storefronts | [INFERENCE, not confirmed] |

`[INFERENCE, not confirmed]`: India's gateway-hosted card capture likely keeps Lenovo India in reduced PCI scope. The "My Wallet" vault in the global bundle suggests tokenised saved cards somewhere on lenovo.com. The vault provider is not visible.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: Central control slows local rails, and Lenovo has said so publicly**
> **Evidence:**
> - S7/S3B: the Japan e-com lead says adding a method needs global approval, and the US controls the system ([impress](https://netshop.impress.co.jp/node/14122)).
> - S4: Japan, the #3 market, shows card, bank transfer, JACCS and Amazon Pay, with no konbini or PayPay found.
> - S1: Japan is 5.47% of traffic, ~2.3M visits/month derived.
>
> **Pain Point:** Each local rail waits on a US-led roadmap. Japan's one fast addition (Amazon Pay) passed 10% share and added net buyers, so the cost of every other missing method is real lost conversion.
> **Yuno Value Proposition:** Local methods added through one integration, without each one becoming a central engineering project. Yuno would sit beside LePay, not replace it.
> **Best Success Case:** inDrive. New countries launched fast through one integration.
> **Outreach Angle:** "Your Japan team said adding a payment method means waiting on global, and the one that got through took 10% share. What would it look like if markets didn't have to wait?"
> **Suggested Subject Line:** "Japan's 10% Amazon Pay share, and what's still queued"

> **Insight #2: In-house aggregation (LePay) means reach and bandwidth, not "orchestration"**
> **Evidence:**
> - S3B: LePay is a Lenovo-built unified payment layer with a Global Payments team.
> - S6: payments-platform and subscription-payments PM hiring (unverified).
> - S11C: OnePlus runs Juspay orchestration, and Xiaomi uses Adyen in 18 markets plus Juspay (summary).
>
> **Pain Point:** Building and maintaining every PSP and APM connector in-house competes with a team that also has to handle a new subscription-payments push.
> **Yuno Value Proposition:** Breadth of APMs and acquirers as a service for the long tail of markets, so the in-house team keeps control of the core.
> **Best Success Case:** Rappi, a sophisticated in-house payments team that still added an orchestration layer. Confirm the case fits before citing it.
> **Outreach Angle:** "You built LePay so channels plug in once. The open question is how many more country rails your team wants to build and maintain itself."
> **Suggested Subject Line:** "LePay + the long tail of APAC rails"

> **Insight #3: Japan card acquiring may be offshore, which would be an approval-rate question**
> **Evidence:**
> - S2: a Lenovo JP page reportedly says card charges are processed overseas on GMT `[UNVERIFIED]`.
> - S3A: Worldpay reportedly consolidated Lenovo's domestic acquirers, Japan first `[UNVERIFIED, 2019]`.
> - S1: Japan is the #3 market.
>
> **Pain Point:** If Japanese-issued cards are acquired cross-border, approval rates on ¥100k–¥400k PCs suffer (price range per the impress article). **Both inputs are unverified. Do not use this in outreach until the descriptor or processing location is confirmed.**
> **Yuno Value Proposition:** Domestic acquiring in Japan alongside the global acquirer, with routing by issuer country.
> **Best Success Case:** inDrive (approval-rate lift across many markets).
> **Outreach Angle:** Discovery only: "Are Japanese cards on lenovo.com/jp acquired domestically or via the global acquirer?"
> **Suggested Subject Line:** n/a (discovery question)

> **Insight #4: India: high-ticket EMI only on credit cards, with merchant-of-record ambiguity**
> **Evidence:**
> - S4: India EMI is credit-card only, with no debit or cardless EMI found.
> - S1: India is the #2 market at 14.93%.
> - S2: two live pages name different store operators (Lenovo India vs NDSL).
> - S5: one UPI-debited, no-order case.
>
> **Pain Point:** Laptops are high-ticket, and a credit-card-only EMI excludes the debit-card majority. Unclear MoR means we don't yet know who owns the gateway contract.
> **Yuno Value Proposition:** Wider EMI and cardless options plus UPI resilience, but only once the buyer is clear.
> **Best Success Case:** None matched. Hold until the MoR is resolved.
> **Outreach Angle:** "Lenovo India's No Cost EMI is credit-card only. Is debit or cardless EMI on the roadmap?"
> **Suggested Subject Line:** "No Cost EMI on debit cards at lenovo.com/in"

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. Lenovo Japan's e-commerce lead said publicly that adding a payment method means waiting for global approval, and the one that got through (Amazon Pay) passed 10% of payments.
2. lenovo.com/in offers No Cost EMI on credit cards only, on laptops that cost several weeks of salary.
3. You built LePay to plug channels in once; we take the long tail of local rails off your central team's roadmap.

**Cold call openers (conversational, one sentence each):**
1. "I read your Japan team's Amazon Pay write-up, the point about needing global approval for every new method. Is that still how it works?"
2. "When a country team wants konbini or PayPay, who owns that decision, the US platform team or the market?"
3. "Is lenovo.com/in billed by Lenovo India or still by Net Distribution? Your two policy pages say different things."

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

HQ and size marked `[GK]` are general knowledge, not sourced in this run. Verify them before use.

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| HP Inc. | hp.com | US | [GK] | IN, JP, CN, AU | Not found | — |
| Dell Technologies | dell.com | US | [GK] | IN, JP, CN, AU | Not found | — |
| ASUS | asus.com | Taiwan | [GK] | TW, IN, SEA | 2C2P (SG store, 2022) `[UNVERIFIED]` | https://thepaypers.com/companies/latest-news-on-ASUS--27312 |
| Acer | acer.com | Taiwan | [GK] | TW, IN, AU | Not found | — |
| Apple | apple.com | US | [GK] | CN, JP, IN | Not found | — |
| Samsung | samsung.com | South Korea | [GK] | KR, IN, SEA | Not found | apac-tal.csv |
| Xiaomi | mi.com | China | [GK] | CN, IN, SEA, JP | **Adyen** (18 markets, confirmed) + **Juspay** (summary only) | https://www.adyen.com/press-and-media/adyen-provides-payments-solutions-to-xiaomi ; https://hyperswitch.io/case-studies/xiaomi |
| Huawei | huawei.com | China | [GK] | CN, SEA | Not found | apac-tal.csv |

#### 11B. Industry Peers / Same Vertical
| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| OnePlus | oneplus.com | Phones (vs Motorola) | IN | Juspay orchestration, offers engine, EMI | https://juspay.io/customer-stories/oneplus |
| realme | realme.com | Phones | IN, SEA | Juspay per TAL only | apac-tal.csv |
| Dyson | dyson.com | Consumer electronics D2C | APAC-wide | Multi-market D2C; see `2-ready-to-outreach/dyson.md` | dyson.md |
| Razer | razer.com | Gaming hardware D2C | MY, TH, SG | Single Worldpay acquirer across 15 storefronts; see `razer.md` | razer.md |
| LG Electronics | lg.com | Consumer electronics | KR, IN | High-ticket D2C | apac-tal.csv |
| Oppo / Vivo / Honor | oppo.com / vivo.com / hihonor.com | Phones | CN, IN, SEA | Motorola competitors; no stack found | apac-tal.csv |

#### 11C. Companies Recently Adopting Payment Orchestration
| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| OnePlus | Juspay (HyperCheckout, Payment Orchestration, Offers Engine) | Undated | Phones | https://juspay.io/customer-stories/oneplus (fetched) |
| Xiaomi | Juspay (summary only) + Adyen Unified Commerce | Adyen ~Jul 2026 `[date UNVERIFIED]` | Consumer electronics | https://www.adyen.com/press-and-media/adyen-provides-payments-solutions-to-xiaomi (fetched) |

#### 11D. Prospect Scoring
Not scored. Competitor payment stacks are mostly unknown, and scoring on that basis would be guesswork. Xiaomi is the only peer with a confirmed multi-market stack.

#### Top 10 Prospect Pipeline
| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Xiaomi | Competitor | CN, IN, SEA, JP | Not scored | — | Adyen across 18 markets plus Juspay: a split stack | ✅ Yes (orchestrator column: Juspay; **Adyen missing**) |
| 2 | Samsung | Competitor | KR, IN, SEA | Not scored | — | Large multi-market D2C | ✅ Yes |
| 3 | ASUS | Competitor | TW, IN, SEA | Not scored | — | 2C2P in SG (2022) | ✅ Yes |
| 4 | LG Electronics | Peer | KR, IN | Not scored | — | High-ticket D2C | ✅ Yes |
| 5 | Huawei | Competitor | CN, SEA | Not scored | — | — | ✅ Yes |
| 6 | Oppo | Peer | CN, IN, SEA | Not scored | — | — | ✅ Yes |
| 7 | Vivo | Peer | CN, IN, SEA | Not scored | — | — | ✅ Yes |
| 8 | **Acer** | Competitor | TW, IN, AU | Not scored | — | APAC-HQ'd PC maker with D2C stores | ❌ **Not on TAL: genuine find** |
| 9 | HP Inc. | Competitor | IN, JP, AU | Not scored | — | Live HP India D2C store `[UNVERIFIED]` | ❌ Not on TAL (US-HQ; check territory rules) |
| 10 | Dell | Competitor | IN, JP, AU | Not scored | — | — | ❌ Not on TAL (US-HQ) |

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | US$83.07B (FY25/26, FYE 31 Mar 2026), +20% | https://www.businesswire.com/news/home/20260521007160/en/Lenovo-Group-Q4-and-Full-Year-Financial-Results-202526 `[UNVERIFIED — search summary only]` |
| Latest quarter | Q1 FY26/27 US$26.9B, +43% | zawya / barchart `[UNVERIFIED]` |
| GMV (lenovo.com D2C) | ~US$2.65B (2024) | ECDB, https://ecdb.com/resources/sample-data/retailer/lenovo `[ESTIMATE, not confirmed]` |
| Average Transaction Value (USD) | Not found. The Japan article puts PCs at just under ¥100k to ¥300–400k | https://netshop.impress.co.jp/node/14122 (price range, not ATV) |
| Est. Annual Transactions | Not calculable from sourced inputs | — |
| **Monthly transaction count** | **⚠️ NOT FOUND — ASSUMED ≥100,000/month. [ASSUMPTION — not researched.]** Basis: 42.54M monthly visits × an assumed 0.3–0.5% conversion = ~128k–213k orders. ECDB's US$2.65B GMV (unverified) ÷ an assumed ~US$800 AOV ÷ 12 = ~276k. Billing unit: one lenovo.com D2C order, excluding B2B, channel and shop.lenovo.com.cn. | See ICP rule |
| Active Customers / Users | Not found | — |
| Primary Currency | USD reporting; INR, JPY, CNY in-territory storefronts | Storefronts |
| Top 3 Markets by Revenue | By region: Americas 34%, EMEA 25%, China 22%, AP ex-China 19% | Yahoo Finance summary `[UNVERIFIED]` |
| Billing channel split (web vs app store) | N/A: hardware sold via web D2C and channel; no app-store billing | — |

---

### Overall Research Confidence

**Medium.**

**Traffic:** supplied (SimilarWeb, lenovo.com only). China's .cn store and motorola.com are not covered.

**Strong coverage:**
- **Entities:** India, Japan and China, from fetched Lenovo pages.
- **India and Japan payment methods:** fetched terms.
- **The Japan "global approval" quote:** fetched and verified, Amazon-sponsored.
- **LePay:** fetched.
- **Competitor orchestration:** OnePlus fetched, Xiaomi/Adyen fetched.

**Weak coverage:**
- No live checkout was walked, so no PSP is confirmed per storefront.
- India merchant of record is in conflict between two pages.
- China payment methods are unknown.
- All financials, job postings and complaints beyond one India case are summary-only.

**Environment:** WebFetch returned 403 on lenovo.com, but Bash curl worked, so fetches went through curl.

### Manual Research Recommendations

> **Area:** Monthly transaction count (assumed)
> **Why it matters:** It is the only reject-capable signal, and it is assumed here, though the risk of falling under 40k is negligible.
> **Suggested manual action:** Ask in discovery for D2C order volume for lenovo.com/in and /jp.

> **Area:** Japan checkout methods and acquiring location
> **Why it matters:** It decides whether Insight #1 (missing konbini/PayPay) and Insight #3 (offshore acquiring) can go into outreach.
> **Suggested manual action:** Use a JP VPN, add a laptop to the cart on lenovo.com/jp, screenshot the payment step, and check the iframe domains in DevTools.

> **Area:** India merchant of record (Lenovo India vs NDSL)
> **Why it matters:** It determines who the buyer and gateway-contract owner is in Lenovo's #2 market.
> **Suggested manual action:** Go to the payment step on lenovo.com/in and read the merchant name on the gateway page. Optionally check the MCA record for CIN U72900KA2005PTC035783.

> **Area:** Who owns APAC e-commerce and payments now
> **Why it matters:** The Japan quote points to a US-led central team. The right first contact is probably the Japan e-com manager (champion) plus the Global Payments lead.
> **Suggested manual action:** Use Sales Navigator to search "Lenovo" + "Payments" (Global Payments team) and "Lenovo Japan eCommerce". Verify 暮石龍生's current role.

> **Area:** Whether LePay runs lenovo.com checkout
> **Why it matters:** It decides between "in-house" and "direct PSPs (greenfield)", which changes the score by 3 points and the whole motion.
> **Suggested manual action:** Use DevTools on any lenovo.com checkout and look for LePay/BASD endpoints versus direct Worldpay or Braintree calls.

---

### Appendix: All Source URLs

**Traffic:** `accounts/traffic/lenovo.md` (SimilarWeb, supplied 2026-10-19)

**S2 Entities:**
- https://www.lenovo.com/in/en/terms-and-conditions/
- https://www.lenovo.com/in/en/payment-delivery/
- https://www.lenovo.com/jp/ja/selling-agreement/public
- https://shop.lenovo.com.cn/
- https://www.lenovo.com/id/id/
- https://static.lenovo.com/asean/premiumcare/PremiumCare%20Terms%20-ID_v1.1%20-%20bilingual.pdf
- https://www.lenovo.com/sg/en/terms-and-conditions
- https://www.lenovo.com/au/en/legal/new-products-and-warranty-services/
- https://www.lenovo.com/hk/en/cart
- https://data-max.co.jp/corpo_database/corpo/detail/2010401057479

**S3 PSPs / orchestration:**
- https://basd.lenovo.com/en/ProductandServices/ValueChain/Sales/unifiepay.html
- https://www.fool.com/investing/2019/03/06/3-reasons-worldpay-is-a-buy.aspx
- https://www.lenovo.com/in/en/
- https://jobs.lenovo.com/en_US/careers/JobDetail/Product-Manager-Payments-Platforms/76986
- https://thepaypers.com/company/2C2P/295
- https://trevipay.com/wp-content/uploads/2025/01/TreviPay-Lenovo-CaseStudy-Deutsch.pdf
- https://lenovo.com/jp/outlet/ja/merchandising/selling-agreement/popup-forwinfo

**S4 APMs:**
- https://www.lenovo.com/in/en/no-cost-emi/
- https://www.lenovo.com/jp/ja/partner/jaccs-tejun/
- https://netshop.impress.co.jp/node/14122
- https://www.lenovo.com/us/en/landingpage/lenovo-financing-options
- https://lenovo.com/au/en/shopping-faqs/lenovo-payment-options

**S5 Complaints:**
- https://www.consumercomplaints.in/lenovo-refund-not-received-invalid-reference-id-provided-urgent-resolution-required-c3530660
- https://www.trustpilot.com/review/www.lenovo.com?page=6
- https://nz.trustpilot.com/review/www.lenovo.co.uk?page=5
- https://steamcommunity.com/discussions/forum/12/38596748070144795/
- https://voxya.com/consumer-complaints/replacement-refund-of-laptop-adapter/135572

**S6/S7 Developments and news:**
- https://www.zawya.com/en/press-release/companies-news/lenovo-delivers-strongest-quarter-in-group-history-hybrid-ai-strategy-powers-growth-momentum-437812
- https://www.businesswire.com/news/home/20260521007160/en/Lenovo-Group-Q4-and-Full-Year-Financial-Results-202526
- https://news.lenovo.com/pressroom/press-releases/lenovo-completes-acquisition-of-infinidat-expanding-enterprise-storage-portfolio-enhancing-ai-driven-data-infrastructure/
- https://jobs.lenovo.com/en_US/careers/JobDetail/Product-Manager-Subscription-Payments/79856
- https://jobs.lenovo.com/en_US/careers/JobDetail/Global-E-Commerce-Director/78823
- https://www.crnasia.com/news/2025/channel-news/lenovo-unveils-new-asia-pacific-one-channel-leader
- https://thepaypers.com/ecommerce/klarna-and-lenovo-partner-to-expand-payments-in-europe--1271124
- https://americanexpress.com/content/dam/amex/en-in/benefits/Lenovo_EMI_Offer_TnC_July24.pdf
- https://www.indiaretailing.com/?p=80101

**S11 Competitors:**
- https://www.adyen.com/press-and-media/adyen-provides-payments-solutions-to-xiaomi
- https://hyperswitch.io/case-studies/xiaomi
- https://juspay.io/customer-stories/oneplus
- https://thepaypers.com/companies/latest-news-on-ASUS--27312

**S12 Financials:**
- https://ecdb.com/resources/sample-data/retailer/lenovo
- https://finance.yahoo.com/markets/stocks/articles/lenovos-global-footprint-strengthens-growth-165200926.html

**Yuno cases:**
- https://y.uno/en/success-stories/indrive
- https://www.y.uno/en/success-stories/rappi

</details>
