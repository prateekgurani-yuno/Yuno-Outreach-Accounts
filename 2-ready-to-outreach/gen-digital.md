# Gen Digital

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 17 / 29 → ⭐ High Priority **on arithmetic** — **ANALYST OVERRIDE applied, tier set DOWN to 🟢 Medium.** See the ICP breakdown for the reasoning.
**Industry:** Consumer cyber-safety subscriptions (Norton, Avast, AVG, Avira, LifeLock, CCleaner) + consumer fintech (MoneyLion) · **HQ:** Dual — Tempe, Arizona (US) and Prague (Czech Republic); NASDAQ: GEN. APAC hub contracting entity **NortonLifeLock Singapore Pte. Ltd.** · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **In-house** — Gen runs its own multi-brand checkout (`buy.norton.com/estore`, `buy.avast.com/genStore`) that picks the PSP server-side per market. **Plus a long tail of third-party merchants of record on Avast** (Noventiq, Nexway, Cleverbridge, 2Checkout) that Gen is visibly pulling back in-house. Argue reach and migration risk, never "you need orchestration."
**⚠️ READ BEFORE ANY OUTREACH — account ownership:** Gen is a US/Czech-HQ'd global enterprise. **APJ is 8% of revenue ($406M of $5.0B, FY26).** The payments decision-maker almost certainly sits in Tempe or Prague, not Singapore or Tokyo. It is in territory (Singapore Pte. Ltd., Japan entity, Australia Pty Ltd all confirmed), but **check with your manager whether an AMER/EMEA AE already owns Gen before sequencing.**

---

> ## 🎯 THE HOOK — Gen paid $66M to get its customers back from a merchant of record, and still has four more on Avast
>
> Verbatim, FY26 10-K ([SEC](https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000017/gen-20260403.htm)):
> > "During fiscal 2025, in connection with a legal settlement terminating our agreement with an Avast e-commerce partner that acted as payment processor and merchant of record for a subset of customers, we released our claims to $66 million of outstanding accounts receivable (net of any fees payable) in exchange for the transfer of the related customer information to us."
>
> And Avast's own live billing FAQ ([support.avast.com](https://support.avast.com/en-us/article/sale-billing-faq/), read 2026-10-19) still lists the providers that "manage the online sales and distribution of our products and services in certain regions":
>
> | Provider | Card descriptor |
> |---|---|
> | Noventiq (formerly Softline) | AVAST, ASSIST, CY / AVAST ASSIST AVAST LIMASSOL |
> | Nexway | CB AVAST NEXWAY |
> | Nexway – PayPal | PAYPAL *NEXWAY |
> | Cleverbridge | CBA*AVAST Software s.r.o |
> | 2Checkout | (named in the monthly-billing-date rules) |
> | Google Play / Apple App Store | Google Play Apps / APPLE.COM/BILL |
>
> **Every one of those regions is a future migration onto Gen's own estore**, and each needs local acquiring and local rails on day one, because it is a live renewal book, not a new launch.
>
> **The cautionary tale is public and comes from Gen's #1 competitor in Japan.** Trend Micro, FY2025 results ([newsroom.trendmicro.com](https://newsroom.trendmicro.com/2026-02-18-Trend-Micro-Reports-Earnings-Results-for-Q4-2025-and-FY-2025), fetched): *"the aftereffects of previous payment processing challenges continued to impact the overall revenue of Trend's consumer business throughout the year, resulting in a 9% YoY decline in net sales for 2025."* The Q2 2025 release confirms the cause: *"the successful migration completed to a new merchant of record for processing credit card transactions"* ([newsroom.trendmicro.com](https://newsroom.trendmicro.com/2025-08-07-Trend-Micro-Reports-Earnings-Results-for-Q2-2025)).
>
> **The pitch is MoR-exit insurance:** move each remaining Avast region onto Gen's own stack without a Trend-style renewal hole, by routing through local acquirers and rails that are already live. ⚠️ Do not name Trend Micro to Gen in an email (never-name-competitors rule). Use it in your own head and on a call, if asked, as "a public example in your category."

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Gen Digital is the consumer cyber-safety group behind Norton, Avast, AVG, Avira, LifeLock and CCleaner. Since April 2025 it also owns the US consumer fintech MoneyLion. FY26 revenue was $5.0B and it has 81M paid customers (Q1 FY27), sold mostly as annual auto-renewing subscriptions through its own e-commerce platform, mobile apps and telco/OEM partners.

**SimilarWeb total visits (avg month, Jul–Sep 2026):** **~23.0 million** combined across norton.com (14.50M) and avast.com (8.494M). Source: SimilarWeb (supplied 2026-10-19). ⚠️ Excludes avg.com, avira.com, lifelock.com, ccleaner.com, gendigital.com and all app traffic.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇺🇸 United States | 40.1% | Cards, PayPal, Klarna Pay in 4, Apple Pay, Google Pay (checkout code) | — (out of territory) | ✅ Gen Digital Inc. |
| 2 | 🇩🇪 Germany | 7.7% | Cards, PayPal, Klarna/Sofort, giropay, direct debit (checkout code) | — (out of territory) | ✅ Avast Software s.r.o / NortonLifeLock Ireland (EU) |
| 3 | 🇯🇵 **Japan** | **≥5.5%** (norton.com only) | Visa/MC/Amex/**JCB**/NICOS/Diners, **konbini** (7-Eleven, FamilyMart, Lawson, MiniStop, Seicomart), Pay-easy, bank & postal transfer | **PayPay, carrier billing (direct), Paidy, PayPal** — not found in terms or checkout code | ✅ NortonLifeLock Japan (KK vs G.K. form unresolved) |
| 4 | 🇫🇷 France | 5.4% | Cards, PayPal (checkout code) | — (out of territory) | ✅ EU entities |
| 5 | 🇬🇧 United Kingdom | 4.6% | Cards, PayPal (checkout code) | — (out of territory) | ✅ NortonLifeLock Ireland |
| — | 🇮🇳 **India** (#6) | 2.9% | Cards incl. **RuPay**, **UPI**, **NetBanking** in checkout code; terms list only cards + PayPal | **UPI Autopay** for renewals — not found | ❌ **None found** — billed cross-border by the Singapore Pte. Ltd. |
| — | 🇦🇺 **Australia** (#11) | ≥1.5% | Cards, PayPal (terms) | Afterpay, PayTo, BPAY — not found | ✅ NortonLifeLock Australia Pty Ltd (billing); contract with the Singapore entity |

### Legal entities
- **NortonLifeLock Singapore Pte. Ltd.** (Singapore) — APAC contracting entity for Australia, China and "Rest of APAC" incl. India. Listed in 10-K Exhibit 21.
- **NortonLifeLock Japan** (Japan) — **株式会社ノートンライフロック** per the JP terms of sale; "Japan KK" per Gen's billing-entity page; **"G.K."** per 10-K Exhibit 21. ⚠️ Discrepancy unresolved. Akasaka, Tokyo.
- **NortonLifeLock Australia Pty Ltd** (Australia) — ABN 59 085 397 100 / ACN 085 397 100 (formerly Symantec (Australia) Pty Ltd), Barangaroo, Sydney. Billing entity.
- **Avast Software s.r.o** (Czech Republic), **NortonLifeLock Ireland Limited** (Ireland), **Gen Digital Inc.** (US) — global billing entities.

### Known PSPs
- **Gen in-house estore / genStore** — [Source Code] — all brands, global. The PSP behind it is selected server-side (`settings.pspValue`) and **not named anywhere public**.
- **Noventiq, Nexway, Cleverbridge, 2Checkout** — [Terms/Privacy Policy] Avast billing FAQ — third-party merchants of record "in certain regions" (regions not stated).
- **PayPal** — [Terms] AU/IN terms, Avast store terms — global.
- **Klarna** (Pay Now / Pay in 4) — [Source Code] — US/EU.
- **Apple App Store / Google Play** — [Terms] — mobile in-app subscriptions, global.
- ❓ **Worldpay** — [INFERENCE, not confirmed] from `-SSL` APM code naming. Do not cite.

### Orchestration status
**In-house orchestration layer.** Gen's own checkout (`checkOutV2.js`, built 28 Sep 2026) carries a server-set `pspValue`, Google Pay with `TOKENIZATION_TYPE: "PAYMENT_GATEWAY"` and a server-injected `gatewayMerchantId`, plus per-country and per-seller method logic (`"JP"===e&&"KONBINI"`, an India-specific `NETPROPHETS` seller mode). No third-party orchestrator was found in code or search. Medium confidence: the code shows routing capability, not how many PSPs sit behind it. [Source](https://buy-static.norton.com/estore/V10062026001/script/checkOutV2.js)

### Buying signals
- 🔁 **Merchant-of-record exit underway.** In FY25 Gen settled out of one Avast MoR, giving up $66M of receivables for the customer data; four third-party MoRs are still live on Avast. ([10-K](https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000017/gen-20260403.htm), [Avast FAQ](https://support.avast.com/en-us/article/sale-billing-faq/))
- 💸 **Payment processing fees +$58M YoY** were named as a cost-of-revenue driver in FY26. ([10-K](https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000017/gen-20260403.htm))
- 💼 **Billing-success hire at MoneyLion (Gen subsidiary):** eCommerce Senior Billing Performance Analyst posted 2026-01-16, built around a weekly "Billing Success Rate." Aggregator listing, not confirmed still open. ([edisonpartners](https://jobs.edisonpartners.com/companies/moneylion/jobs/65287990-ecommerce-senior-billing-performance-analyst))
- 🤝 **Possible M&A:** a GoDaddy takeover approach was reported 2026-09-24 (FT, via secondary outlets; early-stage, unconfirmed). ([stocktwits](https://stocktwits.com/news-articles/markets/equity/go-daddy-shares-surge-on-gen-digital-s-reported-takeover-bid-gen-stock-falls-as-talks-in-early-stages/cZMJ4SYRB9N)) Watch only; do not use as fact.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Gen Digital` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 17 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED (floor): ≥3.37M/month** — 40.4M direct customers (Q4 FY25, the last period Gen reported the metric; [8-K](https://www.sec.gov/Archives/edgar/data/849399/000084939925000025/ex9901q4fy25.htm)) ÷ 12, on the most conservative billing unit (one annual renewal per customer; the 10-K says "most of our subscriptions are offered on annual terms, but we also provide monthly"). Both inputs sourced. Paid customers have since grown to 81M (Q1 FY27). **Billing unit:** subscription purchases/renewals billed by Gen. App-store and partner-billed renewals may not run through Gen's PSPs. Even if only a tenth were Gen-billed, the floor stays above 100k. **APAC-only count:** ⚠️ NOT FOUND — ASSUMED ~390,000/month. [ASSUMPTION — not researched.] Basis: APJ revenue $406M ÷ group direct ARPU $7.27×12 ≈ 4.65M customer-years ÷ 12; assumes APJ ARPU equals the group's. |
| Orchestration status | +1 | ✅ In-house orchestration layer (source code: server-side `pspValue`, gateway tokenization, per-country/per-seller logic). Hardest sell. |
| 3+ countries | +3 | ✅ 11 countries above 1% combined traffic (S1); entities in US, Ireland, Czech Republic, Singapore, Japan, Australia (S2). |
| Multiple PSPs | +3 | ✅ Avast billing FAQ names Noventiq, Nexway, Cleverbridge and 2Checkout as active MoRs, alongside Gen's own estore, PayPal and Klarna. The acquirer(s) behind the estore are not identified. |
| Local rail or licensing gap in a top-3 market | 0 | ❌ Top 3 are US, Germany, Japan. Japan has konbini, JCB and bank transfer, and a local entity. PayPay/carrier-billing absence is only "not found", not a sourced gap. India (#6) has UPI in code; UPI Autopay is not found but India is not top 3. |
| Recent expansion | 0 | ❌ No new-market launch in the last 12 months. MoneyLion closed 2025-04-17, outside the window. Norton Financial Scan is a product rollout, not a market entry. |
| Payment issues reported | +2 | ✅ Moderate: recurring Norton Community threads on charges after cancelling auto-renew, double charges and refused refunds (S5). ⚠️ These are billing-practice complaints, not decline/failure patterns. |
| Funding >$10M | 0 | ❌ Public company; no funding round. |
| High traffic outside home | +2 | ✅ US = 40.1% of combined traffic (<60%). |
| Competitor using orchestration | 0 | ❌ None found (S11C). |
| Payment job postings | +1 | ✅ MoneyLion billing-performance analyst, 2026-01 (aggregator; open status unconfirmed). |
| **Total** | **17** | ⭐ on arithmetic |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **⭐ on arithmetic → ANALYST OVERRIDE DOWN to 🟢 Medium.**

**Override reasoning:**
1. **The matrix is double-counting non-APAC facts.** "3+ countries" (+3) and "high traffic outside home" (+2) both fire because of the US and Europe. Germany, France and the UK carry more traffic than every APAC market except Japan. Neither signal says anything about APAC.
2. **APJ is small and shrinking as a share:** $406M of $5,000M (8%), down from 10% in FY25 ([10-K](https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000017/gen-20260403.htm)). An APAC SDR sale here is a minority-region sale into a global payments team.
3. **In-house layer.** Gen has built the routing capability itself (S3B). Yuno's case is coverage behind that layer plus migration de-risking, not the layer itself.
4. **Part of revenue is out of reach.** Mobile in-app subscriptions bill through Apple/Google (S4). Partner and telco channels (e.g. au shops in Japan) bill through the partner. Gen discloses no split. Not enough to invalidate the account, because direct revenue is 83% and "primarily sold through our e-commerce platform and mobile apps", but it trims the addressable base.

**Why not lower:** transaction volume is enormous (≥3.4M/month floor). Gen has publicly paid to exit an MoR, has four more MoRs live, and reported payment processing fees up $58M. Those are real, sourced triggers. The account is worth a sequence, but only after ownership is cleared.

### Source Notes
- ✅ Avast MoR settlement, $66M ([10-K](https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000017/gen-20260403.htm), verbatim, re-checked).
- ✅ Active Avast MoRs: Noventiq, Nexway, Cleverbridge, 2Checkout ([Avast FAQ](https://support.avast.com/en-us/article/sale-billing-faq/), fetched 2026-10-19).
- ✅ Japan methods: cards incl. JCB, konbini, bank/postal transfer ([JP terms of sale](https://jp.norton.com/terms-of-sale), PDF, clause 7).
- ✅ India/AU methods per terms: Amex/MC/Visa/PayPal, possibly bank transfer/direct debit ([IN terms](https://in.norton.com/terms-of-sale), [AU terms](https://au.norton.com/terms-of-sale)).
- ✅ Checkout code carries UPI, RuPay, NetBanking, Konbini, Pay-easy, Alipay, UnionPay, Klarna, Boleto, Przelewy24, QIWI ([checkOutV2.js](https://buy-static.norton.com/estore/V10062026001/script/checkOutV2.js), grepped directly). ⚠️ Code presence ≠ the method is switched on for that country; a live checkout per country was not observed.
- ✅ APJ revenue $406M / 8% ([10-K](https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000017/gen-20260403.htm)).
- ✅ Trend Micro FY2025 consumer sales −9% on "payment processing challenges" (fetched).
- ⚠️ Worldpay as Gen's acquirer: inference from code naming only. Do not cite.
- ⚠️ India seller "NETPROPHETS" in checkout code: identity unverified.
- ⚠️ Japan entity form (KK vs G.K.): three sources disagree.
- ⚠️ Y!mobile reselling "Norton 360 月額版" at ¥522.5/month: search summary only.

### Success Case Alternatives
- **Livelo** — Tier 2. The decline-cascade case: *"recover customer transactions that initially declined by instantly routing them to a secondary acquirer"* (+5% approval, 50% of failed transactions recovered). Best fit for **renewal recovery** on an annual auto-renew book, where a failed renewal is a lost year of revenue. LATAM results; say so. [y.uno](https://y.uno/en/success-stories/livelo)
- **inDrive** — Tier 2 on **"ten new countries in under eight months."** This speaks directly to the MoR-exit problem: each Avast region that leaves a reseller has to be stood up with local rails fast. Pattern match only. [y.uno](https://y.uno/en/success-stories/indrive)
- **Open English** — subscription, 30+ countries. No public numbers; relevance signal only. [y.uno](https://y.uno/en/success-stories/open-english)
- No Tier 1 (consumer security / subscription software with quantified results) exists in the library.

---

## Executive Summary

Gen Digital (NASDAQ: GEN) is the consumer cyber-safety group behind Norton, Avast, AVG, Avira and LifeLock, plus MoneyLion. FY26 revenue was $5.0B; APJ was $406M (8%). Gen runs its own multi-brand checkout with server-side PSP selection, so the motion is **in-house**. Behind that checkout, Avast still sells through four third-party merchants of record in some regions, and Gen has already paid $66M in receivables to exit a fifth. The Yuno entry point is **de-risking those remaining MoR exits**: local acquiring and rails across Japan, India and other markets on day one of each migration, with renewal recovery across acquirers. The public Trend Micro case shows what a botched MoR migration costs a consumer security company.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** Path 1 — SimilarWeb Sales Intelligence, supplied by Prateek, pulled 2026-10-19 (`accounts/traffic/gen-digital.md`). Period Jul–Sep 2026, worldwide, desktop + mobile web.

**Caveats carried from the supplied file (all material):**
1. **Sales Intelligence view:** only the top 10 countries per domain, with shares only. The visit figures below are **[DERIVED from supplied share, not a SimilarWeb figure]** = share × that domain's average monthly visits (norton.com 14.50M, avast.com 8.494M).
2. **Single-domain shares** were converted to visits per domain, summed, and re-shared against the combined 22.994M. Percentages were not averaged.
3. **Countries outside a domain's top 10 contribute 0 for that domain**, so any country appearing in only one list is a **lower bound** (marked ≥). Japan is not in avast.com's top 10, so its Avast share is below 1.93% (≤0.164M extra).
4. **Mobile app traffic is excluded.** Norton and Avast are app-heavy on mobile, so web traffic understates usage.
5. **Only norton.com and avast.com** were pulled. avg.com, avira.com, lifelock.com, ccleaner.com and gendigital.com are missing; LifeLock in particular is US-heavy.
6. Listed countries cover 85.36% of norton.com and 63.80% of avast.com traffic. The remainder is unallocated.
7. No trend data or global rank was supplied. Device split is ~56% desktop / ~44% mobile web on both domains.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | United States | 40.14% | 9.23M | N/A | SimilarWeb (supplied 2026-10-19) |
| 2 | Germany | 7.70% | 1.77M | N/A | " |
| 3 | **Japan** 🔶 | **≥5.52%** | ≥1.27M (norton.com only) | N/A | " |
| 4 | France | 5.44% | 1.25M | N/A | " |
| 5 | United Kingdom | 4.58% | 1.05M | N/A | " |
| 6 | **India** 🔶 | 2.93% | 0.68M | N/A | " |
| 7 | Brazil | 2.75% | 0.63M | N/A | " |
| 8 | Italy | 1.75% | 0.40M | N/A | " |
| 9 | Canada | ≥1.72% | ≥0.39M | N/A | " |
| 10 | Spain | ≥1.64% | ≥0.38M | N/A | " |
| 11 | **Australia** 🔶 | ≥1.49% | ≥0.34M | N/A | " |
| 12 | Poland | ≥1.02% | ≥0.23M | N/A | " |
| 13 | Mexico | ≥0.71% | ≥0.16M | N/A | " |

🔶 = APAC. **High priority (>5%):** US, Germany, Japan, France. **APAC combined: ≥2.29M visits/month, ≈10% of the combined total.** Japan is the only APAC market above 5%. On norton.com alone Japan is #2 globally at 8.76%. On avast.com India is #4 (4.58%).

**Top-10 markets without a confirmed local entity:** India (billed from Singapore), Brazil, Canada, Italy, Spain (the non-APAC markets were not researched for entities; EU sales likely run through Irish/Czech entities). See Section 2.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Dual HQ, Tempe, Arizona (US) and Prague (Czech Republic) ([gendigital.com](https://www.gendigital.com/us/en/)). Formed from Symantec's consumer business (NortonLifeLock) and the 2022 Avast merger.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Singapore | NortonLifeLock Singapore Pte. Ltd. — contracting entity for AU, China and "Rest of APAC" (incl. India). Addresses differ: 38 Beach Road #23-11 (billing page) vs 8 Marina Boulevard #05-02 (AU/IN terms) | Not found | [10-K Ex. 21](https://www.sec.gov/Archives/edgar/data/849399/000084939926000017/fy26exhibit2101.htm); [Gen billing entities](https://www.gendigital.com/us/en/legal/gen-contracting-billing-entities/); [IN terms](https://in.norton.com/terms-of-sale) |
| Japan | 株式会社ノートンライフロック / NortonLifeLock Japan KK — Ark Mori Building 12F, 1-12-32 Akasaka, Minato-ku, Tokyo. ⚠️ 10-K Ex. 21 lists **"NortonLifeLock Japan G.K."** | Not found (check houjin-bangou.nta.go.jp) | [JP terms](https://jp.norton.com/terms-of-sale); [billing entities](https://www.gendigital.com/us/en/legal/gen-contracting-billing-entities/); [Ex. 21](https://www.sec.gov/Archives/edgar/data/849399/000084939926000017/fy26exhibit2101.htm) |
| Australia | NortonLifeLock Australia Pty Ltd — billing entity; Level 46, Tower One, International Towers Sydney | ABN 59 085 397 100 / ACN 085 397 100 [search snippet of ABR; entity name confirmed on Gen's page] | [ABR](https://abr.business.gov.au/ABN/View/59085397100); [billing entities](https://www.gendigital.com/us/en/legal/gen-contracting-billing-entities/) |
| Ireland | NortonLifeLock Ireland Limited | Not found | [Ex. 21](https://www.sec.gov/Archives/edgar/data/849399/000084939926000017/fy26exhibit2101.htm) |
| Czech Republic | Avast Software s.r.o | Not found | [Ex. 21](https://www.sec.gov/Archives/edgar/data/849399/000084939926000017/fy26exhibit2101.htm) |
| US | Gen Digital Inc.; MoneyLion Inc.; MoneyLion Technologies Inc. | NASDAQ: GEN | [Ex. 21](https://www.sec.gov/Archives/edgar/data/849399/000084939926000017/fy26exhibit2101.htm) |
| India | **None found.** Indian consumers contract with the Singapore entity. Dev centres in Pune/Chennai/Bangalore mentioned only in a secondary source [UNVERIFIED] | — | [IN terms](https://in.norton.com/terms-of-sale) |

The Avast billing FAQ also confirms order-number prefixes billed by "NortonLifeLock Singapore Pte Ltd. / Japan K.K." ([Avast FAQ](https://support.avast.com/en-us/article/sale-billing-faq/)).

**Cross-Border Gap Analysis (APAC):**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| Japan | ✅ #3 | ✅ Yes | Not researched — moot, entity exists | Low on entity; processor unknown |
| India | ✅ #6 | ❌ No — Singapore contracting entity | **Not verified this run.** Do not cite an RBI rule without a current source | **Yes** |
| Australia | #11 (≥1.49%) | ✅ Billing entity (contract with Singapore) | Not researched | Low–medium |

> *"Warning: Potential cross-border operation in **India**. No local entity found. Indian Norton customers contract with NortonLifeLock Singapore Pte. Ltd. under Singapore law. Transactions are likely processed cross-border, with higher scheme costs, lower approval rates and FX exposure."* [INFERENCE, not confirmed — the acquiring location is not disclosed; a local Indian PA could sit behind the Singapore contract. The checkout code's India-specific `NETPROPHETS` seller mode hints at a local partner, unverified.]

> **MANUAL:** Confirm the Japan entity's form and 法人番号. Confirm whether India purchases settle through a local payment aggregator (look at the card descriptor on an Indian purchase).

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Global (all brands) | **Gen in-house estore** (`buy.norton.com/estore/checkOutV5`, `buy.avast.com/genStore`). The PSP is set server-side and not named | [Source Code] | https://buy-static.norton.com/estore/V10062026001/script/checkOutV2.js ; https://www.avast.com/en-us/store |
| "Certain regions" (Avast) | **Noventiq** (formerly Softline) — MoR | [Terms/Privacy Policy] | https://support.avast.com/en-us/article/sale-billing-faq/ |
| "Certain regions" (Avast) | **Nexway** (incl. Nexway–PayPal) — MoR | [Terms/Privacy Policy] | same |
| "Certain regions" (Avast) | **Cleverbridge** — MoR | [Terms/Privacy Policy] | same |
| "Certain regions" (Avast) | **2Checkout** — MoR | [Terms/Privacy Policy] | same |
| Global | **PayPal** | [Terms] | https://in.norton.com/terms-of-sale ; https://www.avast.com/en-us/store |
| US/EU | **Klarna** (Pay Now, Pay in 4) | [Source Code] | checkOutV2.js |
| Global | **Apple Pay / Google Pay** (gateway tokenization, gateway hidden) | [Source Code] | checkOutV2.js |
| Mobile | **Apple App Store / Google Play** in-app billing | [Terms] | https://support.avast.com/en-us/article/mobile-unsubscribe/ ; https://support.norton.com/sp/en/us/home/current/solutions/v118353120 |
| Japan | **Not identified.** The JP terms say only 「弊社は、支払い処理の支援を第三者に依頼します」 (we use third parties to assist with payment processing) | [Terms] | https://jp.norton.com/terms-of-sale |
| India | **Not identified.** Seller mode `NETPROPHETS` in code, identity unverified | [Source Code] | checkOutV2.js |
| Historical | Digital River — Symantec reseller agreement (2006, expired 2010); Digital River has since shut down | [Third-Party Report] | https://www.sec.gov/Archives/edgar/data/849399/000095013406019547/f24382e8vk.htm ; https://tcbmag.com/minnetonka-based-e-commerce-firm-digital-river-to-shut-down/ |
| ❓ | Worldpay — [INFERENCE, not confirmed] from `QIWI-SSL` / `PRZELEWY-SSL` style codes. Do not cite | [Source Code] | checkOutV2.js |

Not detected anywhere: Adyen, Stripe, Checkout.com, Cybersource, Braintree, Razorpay, PayU, GMO, SB Payment, Veritrans, KOMOJU. The fraud tooling at `fpt.norton.com/fp/check.js` matches the ThreatMetrix device-profiling pattern [INFERENCE, not confirmed].

**The unnamed Avast MoR:** the 10-K does not name the partner Gen settled with. **Do not name it in outreach.**

#### 3B. Payment Orchestrator

**Classification: In-house orchestration layer.** Evidence [Source Code]: `settings.pspValue` is set by the server; Google Pay is configured with `TOKENIZATION_TYPE:"PAYMENT_GATEWAY"` and a server-injected `gatewayMerchantId`; method logic branches by country and seller. Searches for Gen/Norton/Avast alongside Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails and Yuno returned nothing.

> *In-house layer: the opening is reach and opportunity cost, not the case for orchestration itself.* Gen has the switch. What it may lack is the local acquirers and rails behind it in each market its MoRs currently cover, and it bears the migration risk of moving renewal books off those MoRs.

> **MANUAL:** Walk through checkout from a Japan and an India IP with DevTools. The gateway name appears in the payment-session API response, not in the static JS.

---

### Section 4: Alternative & Local Payment Methods

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| Japan | Visa / MC / Amex / **JCB** / NICOS / Diners | Cards | Mentioned in docs (terms) | https://jp.norton.com/terms-of-sale |
| Japan | **Konbini** (7-Eleven, FamilyMart, Lawson, MiniStop, Seicomart) | Cash/voucher | Mentioned in docs + present in checkout code | terms; checkOutV2.js; buy.norton.com cart icons |
| Japan | **Pay-easy** | Bank transfer / A2A | Present in checkout assets | buy.norton.com cart |
| Japan | Bank transfer (銀行振込), postal transfer (郵便振替) | Bank transfer | Mentioned in docs | terms |
| Japan | PayPay, Paidy, Rakuten Pay, PayPal | Wallet / BNPL | Not found (absent from terms and checkout code) | — |
| Japan | Carrier billing | Carrier billing | Not found as a Gen method. au shops sell Norton annual licences and a monthly plan via a partner portal (au.pismo.tech, run by DFI Japan); that article does not say carrier billing | https://support.norton.com/sp/ja/jp/home/current/solutions/v20230504142152891 |
| Japan | Y!mobile "Norton 360 月額版" ¥522.5/month (telco resale) | Partner channel | [UNVERIFIED — search summary only] | https://www.ymobile.jp/service/pc_security/ |
| India | Cards incl. **RuPay** | Cards | Present in checkout code; terms list Amex/MC/Visa only | checkOutV2.js; https://in.norton.com/terms-of-sale |
| India | **UPI** (one-off) | Bank transfer / A2A | Present in checkout code (`upiId` field); not in terms | checkOutV2.js |
| India | NetBanking | Bank transfer | Present in checkout assets | buy.norton.com cart |
| India | **UPI Autopay** (recurring) | Direct debit / mandate | **Not found** | — |
| India | EMI | Instalments | Not found (low-ticket product; not material) | — |
| India | Avast via Net Distribution Services (cards, netbanking) | Reseller | [UNVERIFIED — search summary only; page blocked by proxy] | store.avast.com NDS policy page |
| Australia | Amex / MC / Visa, PayPal; "may also allow… bank transfer or direct debit" | Cards / wallet | Mentioned in docs | https://au.norton.com/terms-of-sale |
| Australia | Afterpay, Zip, PayTo, BPAY | BNPL / A2A | Not found | — |
| Global | Apple Pay, Google Pay, Klarna, PayPal | Wallet / BNPL | Present in checkout code | checkOutV2.js |
| China / Korea | Alipay, UnionPay; a `korea_payment` option with Korean card fields | Wallet / cards | Present in checkout code (markets not in the traffic top 10) | checkOutV2.js |

**Coverage is better than a typical global-only stack.** The "missing dominant rail" argument is weak for Japan (konbini and JCB are covered) and only partial for India (one-off UPI exists in code).

> *"Warning: In **India**, UPI Autopay is the local recurring rail, and no evidence was found that Norton or Avast support it, on an auto-renew subscription product."* ⚠️ No source for UPI Autopay's prominence was gathered this run; cite one before using this in outreach. The one India renewal-friction thread found is [UNVERIFIED — search summary only] (https://community.norton.com/t/norton-360-renewal-india/221016).

> *Japan konbini and renewals:* konbini is a one-off cash rail, so konbini buyers cannot auto-renew. That makes them a structural churn cohort at renewal. [INFERENCE, not confirmed — not observed in Gen's data.] The JP terms do say Gen may charge **up to 35 days before the renewal date** and uses card-updater data for failed payments, which shows Gen already manages renewal recovery actively.

**App-store split:** both brands sell mobile subscriptions through Apple and Google IAP, cancellable only in the store. The share is **not disclosed** (10-K, S12).

> **MANUAL:** Use a VPN from Japan and India to see which methods actually render at checkout, and whether UPI appears on auto-renew SKUs.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Charged at renewal after cancelling auto-renew (UK, £89.99), no support reply | Norton Community | Moderate (recurring theme) | May 2025 | https://community.norton.com/t/charged-89-99-by-norton-after-cancelling-auto-renewal-with-no-support-response-and-requesting-a-refund/399380 |
| Duplicate charges, mostly from two active subscriptions | Norton Community | Moderate | Undated | https://community.norton.com/t/charged-twice/225300 ; https://community.norton.com/t/i-have-been-charged-twice-for-my-subscription/227564 |
| Refund refused outside the 60-day window | Norton Community | Moderate | Undated | https://community.norton.com/t/cancel-subscription-and-no-refund-from-them/383006 |
| Free trial converted (€94) despite auto-renew off | Norton Community | Isolated | Undated | https://community.norton.com/t/charged-94-even-though-it-was-supposed-to-be-a-free-trial/397402 |
| Google Play subscription not recognised in the app; card dispute filed | Norton Community | Isolated | Undated | https://community.norton.com/t/my-paid-subscription-is-not-shown-on-google-play-store/482819 |
| Japan: could not find how to stop 自動延長, cancelled by phone | minhyo.jp | Isolated | Undated | https://minhyo.jp/norton [UNVERIFIED — search summary only] |
| Regulator: Norton extended refund rights on auto-renewals after CMA action | UK CMA | n/a | 2021 | https://www.gov.uk/government/news/norton-extends-refund-rights-after-cma-action |

> *Pattern of auto-renewal disputes and duplicate subscriptions suggests a chargeback/dispute cost line.* This is a billing-practice problem more than a routing problem; Yuno's relevance is limited to dispute visibility. **No decline, failed-renewal or currency-conversion complaints were found**, and no Reddit or App Store review data was gathered.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 2026-09-24 | Reported takeover approach for GoDaddy (FT via secondary outlets; early-stage, both companies declined comment) | M&A | https://stocktwits.com/news-articles/markets/equity/go-daddy-shares-surge-on-gen-digital-s-reported-takeover-bid-gen-stock-falls-as-talks-in-early-stages/cZMJ4SYRB9N |
| 2 | 2026-08-06 | Q1 FY27: revenue $1.336B; paid customers 81M; FY27 guidance raised to $5.375–5.475B; Norton Financial Scan (MoneyLion AI) rolling out to Norton 360 customers in largest markets | Tech / product | https://newsroom.gendigital.com/2026-08-06-Gen-Further-Accelerates-in-Q1-FY27-and-Raises-Full-Year-Guidance ; https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000028/ex9901q1fy27.htm |
| 3 | 2026-05-07 / 10-K | FY26 revenue $5.0B (+27%); payment processing fees +$58M YoY; Avast MoR settlement ($66M receivables released, FY25) disclosed | Payment infrastructure | https://newsroom.gendigital.com/2026-05-07-Gen-Crosses-5B-in-FY26-Revenue-with-Growth-Accelerating-to-Double-Digits ; https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000017/gen-20260403.htm |
| 4 | 2026-01-16 | MoneyLion eCommerce Senior Billing Performance Analyst (weekly "Billing Success Rate") | Payment Infrastructure Hiring | https://jobs.edisonpartners.com/companies/moneylion/jobs/65287990-ecommerce-senior-billing-performance-analyst |
| 5 | 2025-04-17 | MoneyLion acquisition closed (~$1B; net consideration $951M per 10-K) | M&A | https://www.nasdaq.com/press-release/gen-completes-acquisition-moneylion-accelerating-companys-leadership-financial |

*No public payment-related RFP found.* No APAC market launches, licence applications or payments leadership hires were found in the last 12 months.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | FY26 10-K (filed May 2026) | Gen terminated an Avast e-commerce partner acting as payment processor and MoR via legal settlement; took back the customer data | **High** — MoR exit, in-house consolidation | https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000017/gen-20260403.htm |
| 2 | Live 2026-10-19 | Avast billing FAQ still lists Noventiq, Nexway, Cleverbridge and 2Checkout as regional MoRs | **High** — remaining migration scope | https://support.avast.com/en-us/article/sale-billing-faq/ |
| 3 | Sep 2026 | New checkout bundle (`checkOutV2.js`, built 2026-09-28) with APMs across ~15 countries and server-side PSP selection | Medium — active investment in the in-house stack | https://buy-static.norton.com/estore/V10062026001/script/checkOutV2.js |
| 4 | Aug 2025 (Q1 FY26 call) | "Unified Gen stack is live for Norton products" | Medium | https://www.marketbeat.com/earnings/reports/2025-8-7-nortonlifelock-inc-stock [UNVERIFIED — search summary of transcript] |

*No PSP partnership announcements (Adyen, Stripe, PayPal, etc.) found in thepaypers, finextra or pymnts.*

> *"REMOVAL: Gen discontinued one Avast e-commerce partner (payment processor and merchant of record, unnamed) during fiscal 2025, by legal settlement. Source: FY26 10-K."*

---

### Section 8: Checkout Experience Audit

*Full checkout flow not accessible.* The buy.norton.com cart redirected the JP request to us.norton.com (geo/bot handling). Findings are limited to the Japan product page and the checkout JavaScript.

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | Hosted in-house cart, one global platform localised by `ctry=` / `lang=` parameters | Good | Custom-built |
| Guest checkout | Not observed | — | |
| Steps to complete payment | Not observed | — | |
| Card input experience | Not observed; server-side gateway tokenization for Google Pay | — | |
| Payment methods visible | Konbini/Pay-easy/JCB icons in JP assets; UPI/RuPay/NetBanking in IN assets | Good (code) | Rendering per country not observed |
| Location-based method display | Yes — country- and seller-specific branching in code | Good | |
| Instalment / EMI options | Klarna Pay in 4 (US/EU); none in APAC | Fair | Low-ticket product |
| 3DS implementation | Not detected | — | |
| PCI indicator | Not determined | — | |
| Mobile responsiveness | Not tested | — | ~44% mobile web |
| Multi-currency / local pricing | JPY on jp.norton.com (e.g. ¥3,480/yr renewal); INR on in.norton.com [UNVERIFIED] | Good | |
| Saved payment methods | Auto-renew on stored card; card-updater retries (JP terms) | Good | |
| Error message clarity | Not observed | — | |

The JP page also discloses auto-renewal at ¥3,480/year, renewal price may exceed the intro price, and a 14-day (monthly) / 60-day (annual) refund window ([jp.norton.com/products](https://jp.norton.com/products)).

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found | — |
| Card data handling | Not found | — |
| Recommended Yuno integration | Back-to-back API behind the existing in-house checkout [INFERENCE, not confirmed] | — |

*No direct PCI compliance documentation found publicly for Gen Digital.* At $5B revenue and millions of card transactions, Gen is almost certainly a Level 1 merchant, but that is not sourced and must not be stated.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: The MoR exit is a migration, and migrations break renewals**
> **Evidence:** S7 (10-K: $66M receivables released to exit an Avast MoR, [SEC](https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000017/gen-20260403.htm)) + S3A (four MoRs still live on Avast, [Avast FAQ](https://support.avast.com/en-us/article/sale-billing-faq/)) + S11 (Trend Micro's MoR migration followed by −9% consumer sales, [Trend Micro](https://newsroom.trendmicro.com/2026-02-18-Trend-Micro-Reports-Earnings-Results-for-Q4-2025-and-FY-2025)).
> **Pain Point:** Every region moved off a reseller is a stored-credential renewal book landing on Gen's own acquirers. Without local acquiring and rails ready in that market, first renewals decline and the revenue leaks.
> **Yuno Value Proposition:** One integration behind Gen's estore that adds local acquirers and APMs per market. Renewals route to the acquirer that performs best for that BIN, with cascade on decline.
> **Best Success Case:** inDrive (ten new countries in under eight months, i.e. standing markets up fast) + Livelo (secondary-acquirer recovery). Both are LATAM results.
> **Outreach Angle:** "Your 10-K shows Gen already paid to bring one Avast reseller book in-house, and the Avast billing page still lists four more. Each of those cutovers is a renewal book changing acquirer overnight."
> **Suggested Subject Line:** "The next Avast reseller cutover"

> **Insight #2: India is billed from Singapore on an auto-renew product, with no UPI Autopay found**
> **Evidence:** S2 (India contracts with NortonLifeLock Singapore Pte. Ltd.; no Indian entity found, [IN terms](https://in.norton.com/terms-of-sale)) + S4 (UPI one-off present in code; UPI Autopay not found) + S1 (India #6 overall, #4 on avast.com at 4.58%).
> **Pain Point:** An annual card renewal on a foreign-contracted subscription is the transaction most exposed to Indian issuer behaviour and recurring-debit rules. ⚠️ The specific RBI e-mandate requirements must be sourced before citing.
> **Yuno Value Proposition:** Local Indian acquiring and UPI Autopay through one integration, without Gen standing up an Indian entity.
> **Best Success Case:** No India case in the library; use Livelo only for the recovery mechanism.
> **Outreach Angle:** "Norton India is contracted out of Singapore and renews annually. Is UPI Autopay on the roadmap, or are renewals still card-only?" (a question, not an assertion).
> **Suggested Subject Line:** "Norton India renewals"

> **Insight #3: Payment processing fees grew $58M in a year, and Gen has no named second acquirer in public**
> **Evidence:** S6/S12 (10-K: "$58 million increase in payment processing fees" within cost of revenues) + S3A (no acquirer named behind the estore; PSP selection exists in code).
> **Pain Point:** Part of that is volume (MoneyLion, 53-week year), but cost of acceptance is now a line Gen discloses as a growth driver.
> **Yuno Value Proposition:** Local acquiring in JP/AU/IN and cost-aware routing behind the existing `pspValue` switch.
> **Best Success Case:** Reserva (+4% approval via smart routing). Weak fit; single-market.
> **Outreach Angle:** "Gen's 10-K calls out $58M more in payment processing fees year on year, and the checkout already picks a PSP server-side. The question is what's on the other side of that switch in Japan and India."
> **Suggested Subject Line:** "Processing fees, FY26" (do not quote their JS variable names in email)

> **Insight #4: Japan is Norton's #2 market, and the channel is fragmented**
> **Evidence:** S1 (Japan ≥8.76% of norton.com, #2 globally) + S4 (konbini/JCB/Pay-easy direct; au-shop monthly plan via a third-party portal run by DFI Japan; PayPay not found) + S2 (local Japan entity).
> **Pain Point:** Direct-web, au-shop and (unverified) Y!mobile channels each bill differently, and konbini buyers cannot auto-renew [INFERENCE].
> **Yuno Value Proposition:** PayPay and wallet coverage for direct renewals. ⚠️ Weak: konbini and JCB are already covered, so this is a secondary angle.
> **Outreach Angle:** Use on a call, not in the opener.

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. "Gen's FY26 10-K says you gave up $66M in receivables to bring one Avast reseller's customers in-house, and Avast's billing page still lists Noventiq, Nexway, Cleverbridge and 2Checkout."
2. "Norton India customers contract with NortonLifeLock Singapore and renew annually; I couldn't find UPI Autopay anywhere in the flow."
3. "The 10-K puts payment processing fees up $58M year on year, on a checkout that already selects its PSP server-side."

**Cold call openers (conversational, one sentence each):**
1. "When the next Avast reseller region moves onto genStore, whose acquirer catches those renewals on day one?"
2. "I noticed Norton's checkout already has a server-side PSP switch, so I'm curious how many acquirers are actually behind it outside the US."
3. "Japan is Norton's second-biggest web market. Is PayPay something you've looked at for direct renewals, or is konbini doing the job?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| **Trend Micro** | trendmicro.com | Japan (Tokyo) | FY2025 Japan net sales ¥65.7B [UNVERIFIED — search summary] | JP, US, global | **New MoR for card processing** (migration completed Q2 2025, provider unnamed); consumer sales −9% in 2025 on payment processing problems | https://newsroom.trendmicro.com/2025-08-07-Trend-Micro-Reports-Earnings-Results-for-Q2-2025 ; https://newsroom.trendmicro.com/2026-02-18-Trend-Micro-Reports-Earnings-Results-for-Q4-2025-and-FY-2025 |
| McAfee | mcafee.com | Not sourced | Not sourced | Global incl. AU | Not identified | https://www.mcafee.com/consumer/en-ca/landing-page/mastercard/msmc.html |
| Kaspersky | kaspersky.com | Not sourced | Not sourced | Global (US-sanctioned) | **Nexway, Digital River, 2Checkout** (multiple MoRs) | https://support.kaspersky.com/us/15921 |
| Bitdefender | bitdefender.com | Not sourced | Not sourced | Global | 2Checkout since ≥2007 [UNVERIFIED — search summary] | https://www.2checkout.com/press/press-single/bitdefender-expands-ecommerce-relationship-with-2checkout-in-france.html |
| Quick Heal | quickheal.co.in | India | FY26 revenue ₹261.0 cr [UNVERIFIED — search summary] | IN | Not identified | https://cxotoday.com/media-coverage/quick-heal-technologies-limited-reports-q4-fy26-results/ |
| Sourcenext (ZERO) | sourcenext.com | Japan | Data dated 2013–14 only | JP | Not identified | [UNVERIFIED — search summary] |
| AhnLab | ahnlab.com | South Korea | V3 >60% Korean share (2013, dated) | KR | Not identified | https://www.inews24.com/view/264707 [UNVERIFIED] |

Gen's own 10-K lists its security competitors as Apple, Bitdefender, ESET, F-Secure, Google, Kaspersky, Malwarebytes, McAfee, Microsoft, Trend Micro and Webroot ([10-K](https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000017/gen-20260403.htm)).

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Nord Security (NordVPN, Surfshark) | nordsecurity.com | Consumer privacy subscriptions | Global | Annual auto-renew, global card base; merged with Surfshark 2022 | [UNVERIFIED — search summary] |
| Proton | proton.me | Privacy subscriptions | Global | Accepts cash/crypto as alternatives | [UNVERIFIED — search summary] |
| ExpressVPN (Kape) | expressvpn.com | VPN subscriptions | Global | Named by Gen as a competitor (Kape) | 10-K |
| Aura | aura.com | Identity protection | US | Direct LifeLock competitor | 10-K |
| 1Password / Dashlane | 1password.com / dashlane.com | Password-manager subscriptions | Global | Same billing model | Not researched |

#### 11C. Companies Recently Adopting Payment Orchestration

*No public case studies found of direct competitors adopting payment orchestration.* Searches covering Primer, Spreedly, Gr4vy, Yuno, Payrails and CellPoint at consumer security/VPN companies returned nothing.

#### 11D. Prospect Scoring — Trend Micro (the one competitor with enough verified signal)

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| Monthly transaction count | 0 | ⬜ Not researched | — |
| Orchestration status | 0 | ⬜ Uncertain (MoR model; orchestration unknown) | Trend Q2 2025 release |
| 3+ countries | 0 | ⬜ Not verified this run | — |
| Multiple PSPs | 0 | ⬜ One new MoR confirmed; old one unnamed | — |
| Local rail gap top-3 | 0 | ⬜ Not researched | — |
| Recent expansion | 0 | ❌ | — |
| Payment issues | +2 | ✅ Company-disclosed payment-processing problems, consumer −9% FY2025 | Trend FY2025 release (fetched) |
| Funding | 0 | ❌ Public | — |
| High traffic outside home | 0 | ⬜ | — |
| Competitor orchestration | 0 | ❌ | — |
| Payment job postings | 0 | ⬜ | — |
| **Verified total** | **2** (heavily under-researched) | | |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | **Trend Micro** | Direct competitor | JP (HQ), global | 2 verified (under-researched) | **High — run `/research`** | Self-disclosed payment-processing revenue hit after an MoR migration | ❌ **Not in TAL — genuine find. Tokyo HQ, in territory.** |
| 2 | Quick Heal | Direct competitor | IN | Not scored | Low–medium | Consumer revenue declining; India-native | ❌ Not in TAL |
| 3 | AhnLab | Direct competitor | KR | Not scored | Low | Korea-domestic | ❌ Not in TAL |
| 4 | Sourcenext | Direct competitor | JP | Not scored | Low | Dated data only | ❌ Not in TAL |
| 5 | Kaspersky | Direct competitor | Global | Not scored | Low (sanctions; HQ outside APAC) | Multi-MoR stack | ❌ Not in TAL |

Only five are listed: the others (McAfee, Bitdefender, Nord, Proton, Aura) are HQ'd outside APAC and were not researched for APAC operations.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | **$5,000M** FY26 (ended 2026-04-03, 53 weeks), +27%; Q1 FY27 $1,336M | [Q4 FY26 8-K](https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000014/ex9901q4fy26.htm); [Q1 FY27 8-K](https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000028/ex9901q1fy27.htm) |
| Direct vs partner revenue | Direct $4,137M (83%) / partner $863M | 10-K |
| APJ revenue | **$406M (8%)**, FY25 $395M (10%) | 10-K, by customer billing location |
| GMV / Gross Transaction Volume | N/A (subscription business) | — |
| Average Transaction Value (USD) | Not found. Direct monthly ARPU $7.27 (Q4 FY25, last reported); JP renewal list price ¥3,480/yr | [Q4 FY25 8-K](https://www.sec.gov/Archives/edgar/data/849399/000084939925000025/ex9901q4fy25.htm); jp.norton.com |
| Est. Annual Transactions | ≥40.4M (direct customers × ≥1 billing/yr) | Calculated, floor |
| **Monthly transaction count** | ✅ **DERIVED: ≥3.37M/month** — 40.4M direct customers (Q4 FY25 8-K) ÷ 12 at one annual renewal each (10-K: "most… annual terms"). Both inputs sourced; floor, since monthly plans bill 12×. APAC-only: ⚠️ NOT FOUND — ASSUMED ~390,000/month [ASSUMPTION — not researched]; basis in the ICP table. | See ICP breakdown |
| Active Customers / Users | 81M paid customers (Q1 FY27); 79M (FY26); ~500M total users | 10-K; Q1 FY27 8-K |
| Primary Currency | USD; main FX exposures EUR, **JPY**, GBP, **AUD**, CZK, CAD | 10-K |
| Top 3 Markets by Revenue | US ($3,309M FY26); no other country >10% | 10-K |
| Billing channel split (web vs app store) | **Not disclosed.** Direct is "primarily sold through our e-commerce platform and mobile apps"; app stores are a named channel | 10-K |

---

### Overall Research Confidence

**Medium-High.** Traffic was **supplied** (SimilarWeb Sales Intelligence, 2026-10-19), but only as top-10 shares on two of six-plus domains with no app traffic, so APAC shares are lower bounds. Financials, entities and the MoR settlement come from primary SEC filings and Gen's own legal pages. The payment-method picture comes from the live checkout JavaScript and terms of sale, which is strong for capability but does not show per-country activation. The weakest areas: the acquirer(s) behind the estore are unnamed, the rendered checkout was not reachable (geo redirect), and complaint data is anecdotal. Network access was unrestricted (WebFetch and curl both worked), so there is no environmental downgrade.

---

### Manual Research Recommendations

> **Area:** Account ownership
> **Why it matters:** US/Czech HQ, 8% APJ revenue; a global AE may already own Gen.
> **Suggested manual action:** Check Gong/CRM and ask your manager before any touch.

> **Area:** Which Avast regions still run on Noventiq / Nexway / Cleverbridge / 2Checkout
> **Why it matters:** That is the size of the migration hook (Insight #1). Noventiq historically covers CIS/emerging markets, which may be largely outside APAC [INFERENCE].
> **Suggested manual action:** Check avast.com store checkouts via VPN in JP, IN, AU, ID, VN and note the descriptor/seller shown.

> **Area:** Acquirer behind the estore in Japan and India
> **Why it matters:** It decides whether the pitch is "add local acquiring" or "add a second acquirer."
> **Suggested manual action:** DevTools on a JP/IN checkout; look at the payment-session response and the card descriptor.

> **Area:** UPI Autopay and RBI e-mandate rules
> **Why it matters:** Insight #2 rests on it; the regulation must be sourced before citing.
> **Suggested manual action:** Pull the current RBI e-mandate circular; check whether UPI appears on auto-renew SKUs on in.norton.com.

> **Area:** Japan entity form and 法人番号
> **Why it matters:** KK vs G.K. discrepancy across three Gen sources.
> **Suggested manual action:** Search houjin-bangou.nta.go.jp for ノートンライフロック.

> **Area:** Trend Micro as a standalone account
> **Why it matters:** Tokyo HQ, in territory, self-disclosed payment-processing revenue loss. Probably a stronger APAC account than Gen.
> **Suggested manual action:** `/research Trend Micro`.

---

### Appendix: All Source URLs

**Traffic:** `accounts/traffic/gen-digital.md` (SimilarWeb, supplied 2026-10-19)

**Entities & financials:**
- https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000017/gen-20260403.htm (FY26 10-K)
- https://www.sec.gov/Archives/edgar/data/849399/000084939926000017/fy26exhibit2101.htm (Exhibit 21)
- https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000014/ex9901q4fy26.htm (Q4 FY26)
- https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000028/ex9901q1fy27.htm (Q1 FY27)
- https://www.sec.gov/Archives/edgar/data/849399/000084939925000025/ex9901q4fy25.htm (Q4 FY25, ARPU/direct customers)
- https://www.gendigital.com/us/en/legal/gen-contracting-billing-entities/
- https://www.gendigital.com/us/en/
- https://abr.business.gov.au/ABN/View/59085397100
- https://jp.norton.com/terms-of-sale · https://au.norton.com/terms-of-sale · https://in.norton.com/terms-of-sale

**Payment stack & methods:**
- https://buy-static.norton.com/estore/V10062026001/script/checkOutV2.js
- https://www.avast.com/en-us/store
- https://support.avast.com/en-us/article/sale-billing-faq/
- https://support.avast.com/en-us/article/mobile-unsubscribe/
- https://support.norton.com/sp/en/us/home/current/solutions/v118353120
- https://support.norton.com/sp/ja/jp/home/current/solutions/v20230504142152891
- https://www.ymobile.jp/service/pc_security/ [unverified]
- https://jp.norton.com/products
- https://www.sec.gov/Archives/edgar/data/849399/000095013406019547/f24382e8vk.htm
- https://tcbmag.com/minnetonka-based-e-commerce-firm-digital-river-to-shut-down/
- https://community.norton.com/t/norton-360-renewal-india/221016 [unverified]

**Complaints:**
- https://community.norton.com/t/charged-89-99-by-norton-after-cancelling-auto-renewal-with-no-support-response-and-requesting-a-refund/399380
- https://community.norton.com/t/charged-twice/225300 · https://community.norton.com/t/i-have-been-charged-twice-for-my-subscription/227564
- https://community.norton.com/t/cancel-subscription-and-no-refund-from-them/383006
- https://community.norton.com/t/charged-94-even-though-it-was-supposed-to-be-a-free-trial/397402
- https://community.norton.com/t/my-paid-subscription-is-not-shown-on-google-play-store/482819
- https://minhyo.jp/norton [unverified]
- https://www.gov.uk/government/news/norton-extends-refund-rights-after-cma-action

**Corporate & news:**
- https://newsroom.gendigital.com/2026-08-06-Gen-Further-Accelerates-in-Q1-FY27-and-Raises-Full-Year-Guidance
- https://newsroom.gendigital.com/2026-05-07-Gen-Crosses-5B-in-FY26-Revenue-with-Growth-Accelerating-to-Double-Digits
- https://www.nasdaq.com/press-release/gen-completes-acquisition-moneylion-accelerating-companys-leadership-financial
- https://jobs.edisonpartners.com/companies/moneylion/jobs/65287990-ecommerce-senior-billing-performance-analyst
- https://stocktwits.com/news-articles/markets/equity/go-daddy-shares-surge-on-gen-digital-s-reported-takeover-bid-gen-stock-falls-as-talks-in-early-stages/cZMJ4SYRB9N
- https://www.marketbeat.com/earnings/reports/2025-8-7-nortonlifelock-inc-stock [unverified]

**Competitors:**
- https://newsroom.trendmicro.com/2025-08-07-Trend-Micro-Reports-Earnings-Results-for-Q2-2025
- https://newsroom.trendmicro.com/2026-02-18-Trend-Micro-Reports-Earnings-Results-for-Q4-2025-and-FY-2025
- https://support.kaspersky.com/us/15921
- https://www.2checkout.com/press/press-single/bitdefender-expands-ecommerce-relationship-with-2checkout-in-france.html [unverified]
- https://cxotoday.com/media-coverage/quick-heal-technologies-limited-reports-q4-fy26-results/ [unverified]
- https://www.inews24.com/view/264707 [unverified]
- https://www.mcafee.com/consumer/en-ca/landing-page/mastercard/msmc.html

**Yuno cases:** https://y.uno/en/success-stories/livelo · https://y.uno/en/success-stories/indrive · https://y.uno/en/success-stories/open-english · https://y.uno/en/success-stories/reserva

</details>
