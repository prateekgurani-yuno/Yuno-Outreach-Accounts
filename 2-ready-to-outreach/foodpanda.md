# Foodpanda

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 17 / 29 → ⭐ High Priority **on arithmetic** — **ANALYST OVERRIDE applied, tier set DOWN to 🟢 Medium.** See the ICP breakdown for the reasoning.
**Industry:** Super Apps & On-Demand Delivery — food and grocery delivery (Delivery Hero's Asia brand) · **HQ:** Parent Delivery Hero SE, Berlin; Asian operating entities incl. **Delivery Hero (Singapore) Pte. Ltd.**, 63 Robinson Road, Singapore · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **In-house** — Delivery Hero runs a central *"Payment Orchestration domain, within Payments Tribe"* over several PSPs (Adyen, Cybersource, Checkout.com, MPGS, Alipay+/Antom and local aggregators). Antom publicly describes itself as providing *"orchestration and unified payment interface"* for foodpanda. Not greenfield.
**⛔ READ BEFORE ANY OUTREACH — three conflicts / timing issues:**
1. **Uber is buying Delivery Hero.** Cash offer of €41.50/share (~US$14.8bn equity) announced 16 Jul 2026; completion expected **H2 2027**. **Uber is a Yuno customer** (y.uno: *"Yuno powers payments for McDonald's, inDrive, Rappi, NetEase, GoFundMe, Uber…"*). Clear this with whoever owns Uber at Yuno before sequencing.
2. **Ant Group is a Yuno customer** (y.uno "trusted by" list), and Antom is foodpanda's unified-interface provider across six APAC markets — the same conflict flagged on Lazada.
3. **Taiwan — #2 web market (23%) — is being sold to Grab** for US$600m. The Taiwan Fair Trade Commission's decision is due **27 Oct 2026** (8 days after this report). Treat Taiwan as leaving the account.

---

> # 🔒 PHASE 0 — QUALIFICATION GATE
>
> | Rule | Result |
> |---|---|
> | PSP / gateway / acquirer / orchestrator | **Does not fire — but flag it.** **Delivery Hero (Singapore) Pte. Ltd. is a MAS Major Payment Institution** licensed for Account Issuance, Domestic Money Transfer, **Merchant Acquisition** and **E-money Issuance** ([MAS FID, last updated 25 Aug 2026 — fetched](https://eservices.mas.gov.sg/fid/institution/detail/426483-DELIVERY-HERO-SINGAPORE-PTE-LTD)). Delivery Hero Philippines, Inc. is a BSP-registered **Operator of Payment System (OPSCOR-2020-0113)** for the closed-loop pandapay account ([foodpanda.ph pandapay T&C](https://www.foodpanda.ph/contents/pandapaytermsandconditions) — Agent 2 fetch; 403 on my re-check). **Unlike Grab, no evidence was found that Delivery Hero sells acceptance to third-party merchants.** pandapay is closed-loop, card-top-up only, capped at S$1,000 and non-withdrawable ([SG pandapay T&C](https://www.foodpanda.sg/contents/pandapay-user-account-terms-and-conditions)). `[INFERENCE, not confirmed]`: the merchant-acquisition licence most likely covers collecting on behalf of its own restaurant vendors (marketplace model). **My call: merchant with captive licensed payments, not payment infrastructure.** If Partnerships reads the MAS licence differently, this flips. |
> | Existing Yuno customer | **foodpanda / Delivery Hero: no.** `y.uno/en/success-stories` (fetched 2026-10-19) has zero hits for foodpanda, Delivery Hero, talabat, Baemin or Glovo. **But Uber (acquiring DH) and Ant Group (Antom, foodpanda's wallet aggregator) are both on Yuno's customer list.** Flag, not a rejection. |
> | No online payment volume | Does not fire. |
> | HQ west of Dubai with no APAC operations | Does not fire. Parent is in Berlin, but foodpanda's operations are all in APAC (10 markets per the DH FY2025 Annual Report), with Singapore/Malaysia operating entities. |
> | Monthly transactions < 40,000 (sourced) | **Does not fire.** No sourced foodpanda order count exists. Assumed far above 100k/month — see Section 12. |

> # ⚠️ METHOD NOTES — disclosed up front
>
> 1. **Traffic was supplied**: `accounts/traffic/foodpanda.md`, Similarweb Sales Intelligence, pulled 2026-10-19, Jul–Sep 2026. Its caveats apply throughout this report:
>    - **(a)** Only the top 10 countries per domain were supplied, as shares only. Per-country visits below are `[DERIVED from supplied share, not a SimilarWeb figure]`.
>    - **(b)** Shares are single-domain. The combined split was built visits-first (share × domain average monthly visits, summed), never by averaging percentages.
>    - **(c)** **Mobile app traffic is excluded.**
>    - **(d)** **foodpanda is app-first.** Web traffic is used as a market-mix signal only. It was **not** used to size transactions or test the 40k gate.
>    - **(e) Coverage gap.** The file covers only **5 of foodpanda's 10 live markets** (.pk, .com.tw, .ph, .my, .sg). It has no traffic for **Hong Kong, Bangladesh, Cambodia, Laos or Myanmar**. Hong Kong and Bangladesh are likely material markets, so the country profile below is a five-market view, not the full footprint.
> 2. **Fetch partly worked.** WebFetch and curl both worked at the start of the run. foodpanda's help centres (`/contents/*` payment-method pages) then began returning **HTTP 403 (bot protection)**, and so did foodpanda.sg on my later re-fetch. Earlier captures of the country T&C pages succeeded and were read in full.
> 3. **Page-code evidence comes in two strengths:**
>    - **Strong:** per-market **Adyen merchant account IDs** (`Foodpanda_PK`, `Foodpanda_PH`, `Foodpanda_MY`, `Foodpanda_TW`, `Foodpanda_BD`, `Foodpanda_KH`, `Foodpanda_MM`, `Foodpanda_LA`, plus `DeliveryHero` shared by SG and HK). I extracted these myself from each country's T&C page config.
>    - **Weak:** PSP-prefixed payment-method strings (`CYBERSOURCE_*`, `ANTFINANCIAL_*`, `XENDIT_*`, `RAZER_*`, `REDDOT_*`, `SSL_*`). They sit in a **translation bundle shared by every Delivery Hero brand worldwide**, which also contains Turkish and Nordic PSPs. They show that DH has an integration. They do **not** show which market uses it.
> 4. **Search summaries are not sources.** Several agent findings were search-summary only and are labelled. The Uber deal terms were confirmed on a fetched page (ESM Magazine). The Uber 10-Q I fetched confirms US$1.6bn of total return swaps on Delivery Hero stock.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** foodpanda is Delivery Hero's food and grocery delivery brand in Asia. Its live markets are Pakistan, Taiwan, Philippines, Malaysia, Singapore, Hong Kong, Bangladesh, Cambodia, Laos and Myanmar. It exited Thailand in May 2025, Taiwan is being sold to Grab, and the whole group is being taken over by Uber. Delivery Hero's Asia segment (which also includes Baemin in Korea) did **€20.8bn GMV in FY2025, down 11.2%**. Payments run through a central DH payments organisation with its own orchestration domain and a regional "Payments Acceptance" team in Singapore.

**SimilarWeb total visits:** **~10.46M / month** (Jul–Sep 2026 average, sum of 5 country domains) — **supplied** 2026-10-19. Web only; the app, where most orders happen, is excluded. HK/BD/KH/LA/MM domains not supplied.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇵🇰 Pakistan | 27.4% (~2.86M/mo) | Cards (Adyen `Foodpanda_PK`), easypaisa wallet, JazzCash wallet, COD, pandapay (refund/stored balance) | **Raast not found** (help centre 403 — not confirmed absent) | ✅ Delivery Hero Pakistan (Pvt) Ltd, Karachi |
| 2 | 🇹🇼 Taiwan | 23.0% (~2.40M/mo) | Cards (Adyen `Foodpanda_TW`), Apple Pay, LINE Pay, PX Pay / 全支付 (Jul 2025), COD | **JKOPay not confirmed** (string only in shared bundle); Taiwan Pay / CVS not found. ⚠️ **Market being sold to Grab** | ✅ Foodpanda Taiwan Co., Ltd. (富胖達股份有限公司) |
| 3 | 🇵🇭 Philippines | 17.2% (~1.79M/mo) | Visa, Mastercard, PayPal, GCash (T&C §7.5.1), COD, **QR Ph on delivery** (May 2026), Google/Apple Pay | **Maya native checkout not confirmed; InstaPay/online banking not confirmed** (Xendit direct-debit strings for PH banks in shared bundle only) | ✅ Delivery Hero Philippines Inc. (BSP OPS OPSCOR-2020-0113) |
| 4 | 🇲🇾 Malaysia | 16.6% (~1.73M/mo) | Cards (Adyen `Foodpanda_MY`), FPX → DuitNow Online Banking (Razer MS), Touch 'n Go eWallet + pandacredit, **DuitNow QR on delivery** (T&C §8.10), PayPal, COD | **Boost, ShopeePay, BNPL not confirmed** | ✅ Delivery Hero Malaysia Sdn Bhd |
| 5 | 🇸🇬 Singapore | 10.4% (~1.09M/mo) | Cards (Adyen `DeliveryHero`), PayPal (production flag), pandapay (MAS-licensed e-money), COD; PayLah! (string only) | **PayNow not found** — no PayNow string anywhere in the bundle (hypothesis, not confirmed absence) | ✅ Delivery Hero (Singapore) Pte. Ltd. (MAS MPI) |

Every top-5 market has a local operating entity. **No regulatory acquiring gate applies in the top 5.** One cross-border finding: per the Cambodia and Laos T&Cs, **Delivery Hero Malaysia Sdn Bhd processes payments for Cambodia, Laos and Myanmar.**

### Legal entities
- **Delivery Hero (Singapore) Pte. Ltd.** (Singapore) — MAS Major Payment Institution; 63 Robinson Road #11-01 — UEN not found
- **Delivery Hero APAC Pte. Ltd.**, **DH Financial Services APAC Holding Pte. Ltd.** (Singapore) — 100% DH (AR 2025)
- **Delivery Hero Pakistan (Pvt) Ltd** (Pakistan, Karachi); pandapay PK issued by **R-Sc Internet Services Pakistan (Pvt) Ltd**
- **Foodpanda Taiwan Co., Ltd. / 富胖達股份有限公司** (Taiwan) — being sold to Grab
- **Delivery Hero Philippines Inc.** (Philippines, Makati) — BSP OPSCOR-2020-0113
- **Delivery Hero Malaysia Sdn Bhd** (Malaysia) — also payment processor for KH/LA/MM
- **Delivery Hero Food Hong Kong Limited** (HK) · **Foodpanda Bangladesh Limited** (BD) · **Delivery Hero (Cambodia) Co. Ltd.** · **Delivery Hero (Lao) Sole Co. Ltd.** · **DH (Myanmar) Co. Ltd.** · **Foodpanda (B) Sdn. Bhd.** (Brunei)

### Known PSPs
- **Adyen** — [Source Code] — per-market merchant accounts in PK, TW, PH, MY, BD, KH, MM, LA; shared `DeliveryHero` account for SG and HK; recurring enabled everywhere
- **Cybersource (Visa)** — [Press Release] + [Provider Case Study] — local acquiring + Token Management Service across *"10+ markets"* (Jul 2024)
- **Antom / Alipay+ (Ant International)** — [Provider Case Study] — unified wallet interface: GCash (PH) first, then MY, TH, PK, BD, HK; Touch 'n Go (MY)
- **Razer Merchant Services (Fiuu)** — [Press Release] — FPX / DuitNow Online Banking (MY)
- **Checkout.com, Adyen, MPGS** — [Job Listing] — named as global partners of DH's Singapore Regional Payments Acceptance team
- **PayPal** — [Source Code] — production in SG, PH, MY, HK

### Orchestration status
**In-house orchestration layer, with Antom as a unified-interface layer underneath for wallets.**
- DH job ads describe a *"Payment Orchestration domain, within Payments Tribe"* ([DH careers](https://careers.deliveryhero.com/job/product-manager-payments-fintech-in-berlin-germany-jid-10326)).
- A DH executive says *"we have built a payment recommendation system and a fallback system"* on top of Antom ([Antom, 6 Nov 2025 — fetched](https://knowledge.antom.com/delivery-hero-antom-shaping-tomorrows-digital-platform-payments)).
- No third-party orchestrator found (Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno — all negative). An IXOPAY engagement from 2019 was for rider cash collection; its current status is unknown.

### Buying signals
- 🤝 **Ownership change** — Uber's ~US$14.8bn cash takeover of Delivery Hero, completion expected H2 2027 ([ESM Magazine](https://www.esmmagazine.com/technology/uber-launches-14-8bn-offer-for-delivery-hero-to-create-global-platform-316659)); **Taiwan sale to Grab**, TFTC decision due 27 Oct 2026 ([TechNews](https://finance.technews.tw/2026/07/22/fair-trade-commission-20260722/) · [Taipei Times](https://www.taipeitimes.com/News/editorials/archives/2026/10/14/2003865916))
- 💼 **Payments acceptance hire (Singapore)** — "Specialist, Digital Payments", Regional Payments Acceptance team covering foodpanda, foodora and Yemeksepeti. The role runs PSP and payment-method RFPs, owns **Cost Per Order**, and handles routing changes and renegotiations; it names Checkout.com, Adyen and MPGS. Listing removed 4 May 2026 ([builtin](https://builtin.com/job/specialist-digital-payments/7605072))
- 📉 **Cost pressure** — Asia GMV −11.2% in FY2025 on competition and *"lower average basket sizes"*; DH says it is *"working with multiple payment service providers to lower payment costs"* ([DH Annual Report 2025](https://www.lobbyregister.bundestag.de/media/d4/45/775186/Delivery-Hero-Annual-Report-2025.pdf))
- 🚀 **Cash digitisation** — QR Ph on delivery in the Philippines (May 2026, [Newsbytes](https://newsbytes.ph/2026/05/16/foodpanda-adds-qrph-payments-for-cash-on-delivery-orders/)) and DuitNow QR on delivery in Malaysia ([foodpanda.my T&C §8.10](https://www.foodpanda.my/contents/terms-and-conditions.htm))

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Foodpanda` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 17 / 29 (arithmetic) → override to 🟢 Medium
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | +5 | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. [ASSUMPTION — not researched.]** Basis: ~10.5M monthly web visits on 5 domains, excluding the app where most orders happen; DH Asia GMV €20.8bn FY2025 (includes Korea); foodpanda Taiwan alone did **US$1.8bn GMV in 2025** ([Grab 6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000051/foodpandtaiwan-finalannoun.htm)). No sourced foodpanda average order value exists, so no derivation is possible. Billing unit = one consumer order (pandapro subscription billing is separate and recurring). Band scored per the disclosure rule; **not a measurement.** |
| Orchestration status | +1 | ✅ In-house orchestration layer (DH Payment Orchestration domain; recommendation and fallback system) over multiple PSPs, with Antom as wallet aggregator. |
| 3+ countries | +3 | ✅ 5 markets >1% combined web traffic; 10 markets with local entities (AR 2025). |
| Multiple PSPs | +3 | ✅ Adyen (per-market merchant IDs, [Source Code]) + Cybersource ([Press Release]) + Antom/Alipay+ ([Provider Case Study]) + Razer MS (MY, [Press Release]). |
| Local rail or licensing gap in a top-3 market | 0 | ⬜ Raast (PK), JKOPay (TW) and InstaPay/Maya-native (PH) **not found** — but help centres returned 403, so **absence is not confirmed**. Entity gaps: none. Uncertain = 0. |
| Recent expansion | 0 | ❌ No new market in the last 12 months. HK Deliveroo asset buy (Mar 2025) is outside the window. The direction is contraction: Thailand exited May 2025, Taiwan being sold. |
| Payment issues reported | 0 | ⬜ The recurring theme is refunds defaulting to the pandapay wallet. That is a **policy** (confirmed in the PK/TW T&Cs), not a payment failure. "Failed but charged" threads are undated; Trustpilot 2026 items are search-summary only. Not enough to call moderate. |
| Funding >$10M | 0 | ❌ Wholly owned by DH; no separate funding. A takeover offer is not a funding round. |
| High traffic outside home | +2 | ✅ No market exceeds 27.4% of combined web traffic; Singapore (regional licensed entity) = 10.4%. |
| Competitor using orchestration | +2 | ✅ **Swiggy** and **Zepto** (Asian food / q-commerce peers) each have a Juspay customer-story page ([juspay.io/customer-stories/swiggy](https://juspay.io/customer-stories/swiggy), [/zepto](https://juspay.io/customer-stories/zepto) — both HTTP 200, bodies JS-rendered). ⚠️ India-only — **no market overlap** with foodpanda. Rappi (LatAm delivery) is a Yuno customer. |
| Payment job postings | +1 | ✅ DH Singapore "Specialist, Digital Payments" (Regional Payments Acceptance; PSP RFPs, Cost Per Order, routing), removed May 2026; DH "Product Manager Payments (FinTech)" — Payment Orchestration domain. |

**Tier on arithmetic:** 17 → ⭐ High Priority.

**ANALYST OVERRIDE → 🟢 Medium.** Four reasons:
1. **Double-counting and a disappearing market.** "3+ countries" and "high traffic outside home" both fire on one fact: foodpanda is a multi-country brand with no dominant home market. Taiwan, 23% of the measured web footprint and US$1.8bn GMV, is about to leave. Without Taiwan the footprint still qualifies, but the top-3 list changes (PK, PH, MY).
2. **The stack decision is about to move upstream.** Uber's takeover is expected to complete in H2 2027. Payment strategy for foodpanda is likely to be set in Berlin or San Francisco, not Singapore, from 2027. `[INFERENCE, not confirmed]`
3. **In-house orchestration plus a Yuno-customer aggregator.** DH built its own routing and fallback layer, and the wallet layer is Antom (Ant Group is a Yuno customer). This is the hardest motion, and a political one.
4. **Uber is a Yuno customer.** That is a potential warm path, not a reason to cold-sequence. Pitching the target of a Yuno customer's acquisition without that account team's knowledge is the fastest way to create an internal problem.

What keeps it at Medium and not Low:
- The volume is very large.
- DH runs payments as an explicit cost line: Cost Per Order ownership, PSP RFPs, *"lower payment costs"* in the annual report.
- DH itself is publicly hiring for **"payment orchestration, routing, or multi-PSP environments"**. It knows exactly what Yuno does.
- The Uber relationship could turn this into an **introduced** conversation rather than a cold one.

### Source Notes
- ✅ MAS Major Payment Institution — Delivery Hero (Singapore) Pte. Ltd., incl. Merchant Acquisition and E-money Issuance — MAS FID, fetched by me 2026-10-19
- ✅ Per-market Adyen merchant IDs, recurring enabled — extracted by me from each country T&C page's embedded config
- ✅ PH T&C §7.5.1: *"Our payment partners: Visa, Mastercard, PayPal, GCash"*; card/GCash/COD refunds to pandapay
- ✅ MY T&C §8.10: DuitNow QR presented by rider on delivery
- ✅ SG/PK/PH/MY T&Cs: card data *"will be stored with our third party payment service provider(s)… foodpanda does not store your credit card or payment information"*
- ✅ Antom page (6 Nov 2025): orchestration/unified interface for foodpanda; markets PH, MY, TH, PK, BD, HK; DH's own recommendation and fallback system; multi-acquirer per country discussed as a **future** idea — fetched by me
- ✅ Uber offer terms (€41.50, US$14.8bn, Prosus selling ~17%, H2 2027) — ESM Magazine, fetched by me; Uber 10-Q confirms US$1.6bn TRS on DH stock
- ✅ DH AR 2025: Asia GMV €20,779.7m (−11.2%), 10 foodpanda markets, Thailand exit May 2025, Taiwan sale, *"working with multiple payment service providers to lower payment costs"*
- ✅ Yuno site: Uber and Ant Group on customer lists; no DH brand
- ⚠️ Cybersource partnership (Jul 2024) — Marketech + Visa customer story, via agent; not re-fetched by me
- ⚠️ Razer MS FPX→DuitNow (May 2023) — Razer newsroom, via agent
- ⚠️ PK "nearly half of orders online" (HBL partnership, Oct 2026) — ProPakistani returned 403; search summary only
- ⚠️ SSW Partners 14-market list — search summary only; reportedly contains no APAC foodpanda market
- ⚠️ Uber's exact pre-offer stake (24.99% vs "just under 37% incl. derivatives") — sources differ
- ⚠️ The TAL row "EASI" for foodpanda.com.tw is wrong — the operator is **Foodpanda Taiwan Co., Ltd. (富胖達股份有限公司)**

### Success Case Alternatives
- **Rappi** — ⭐ **closest profile match.** A multi-country delivery platform with many local methods and automatic rerouting across 20+ processors ([y.uno/en/success-stories/rappi](https://www.y.uno/en/success-stories/rappi)). Results are LatAm; do not imply Asian numbers. Use the published figures verbatim or not at all (the "10% approval lift" appears only as a testimonial).
- **inDrive** — multi-country mobility; relevant only for the "time-to-live in a new market" point, which is weak here because foodpanda is contracting, not expanding.
- **Uber (Yuno customer)** — **not a case to cite. It is a relationship to use internally.** Ask the Uber account owner what Uber runs on Yuno and whether Delivery Hero integration planning has started.

---

## Executive Summary

foodpanda is Delivery Hero's Asian food and grocery delivery brand, live in ten markets. Its five largest web markets are Pakistan (27%), Taiwan (23%), the Philippines (17%), Malaysia (17%) and Singapore (10%). Its payments are **not greenfield**:
- Delivery Hero runs an **in-house payment orchestration domain** with its own recommendation and fallback engine over multiple PSPs. These are Adyen (per-market merchant accounts), Cybersource, Checkout.com and MPGS, with **Antom/Alipay+** as the wallet aggregation layer and local aggregators (Razer MS in Malaysia).
- Its Singapore entity holds a **MAS Major Payment Institution licence** including merchant acquisition and e-money issuance, used for the closed-loop pandapay wallet.

The account is in structural flux. **Taiwan is being sold to Grab**, with the regulator's decision due 27 Oct 2026. **Uber, a Yuno customer, is acquiring the whole group**, with completion expected H2 2027. The motion is **in-house**. The only realistic opening is cost-per-order and multi-acquirer depth per country, ideally introduced through the Uber relationship rather than cold.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** **Supplied** — Similarweb Sales Intelligence, `accounts/traffic/foodpanda.md`, pulled 2026-10-19, Jul–Sep 2026, desktop + mobile web. **App traffic excluded.**

**Per-domain average monthly visits (supplied):** foodpanda.pk 3.063M · foodpanda.com.tw 2.454M · foodpanda.ph 1.940M · foodpanda.my 1.874M · foodpanda.sg 1.125M · **Total 10.456M**

**Combined country split** — built visits-first (share × that domain's monthly visits, summed across domains, ÷ 10.456M). Each domain's tail outside its top 10 (0.7%–3.3%) is unattributed, so smaller shares are lower bounds. **Not covered: foodpanda.hk, .com.bd, .com.kh, .la, .com.mm.**

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | Pakistan | 27.35% | ~2.86M `[DERIVED]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | Taiwan | 22.99% | ~2.40M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |
| 3 | Philippines | 17.15% | ~1.79M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |
| 4 | Malaysia | 16.57% | ~1.73M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |
| 5 | Singapore | 10.43% | ~1.09M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |
| 6 | United States | 1.00% | ~0.105M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |
| 7 | Indonesia | 0.41% | ~0.042M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |
| 8 | United Arab Emirates | 0.32% | ~0.033M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |
| 9 | United Kingdom | 0.26% | ~0.027M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |
| 10 | Japan | 0.25% | ~0.026M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |

- **High priority (>5%):** Pakistan, Taiwan, Philippines, Malaysia, Singapore. Each domain's home country is 91–98% of its own traffic, so this is five domestic businesses, not cross-border demand.
- **Device mix:** mobile web 57–87% by domain (PK 87%, MY 84%, PH 73%, SG 69%, TW 57%).
- Countries 6–10 are diaspora or expat visits, all under 1.1%. They are not separate markets, and Indonesia (0.41%) is not a foodpanda market.
- **Global rank:** not captured (Sales Intelligence view).
- All top-5 markets have a local entity (Section 2).

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Parent **Delivery Hero SE**, Berlin, Germany. In Asia: **Delivery Hero (Singapore) Pte. Ltd.**, 63 Robinson Road #11-01, Singapore 068894 (MAS FID); **Delivery Hero APAC Pte. Ltd.** (SG). A DH APAC regional team remains in Bangkok after the Thailand exit ([Marketech APAC](https://marketech-apac.com/foodpanda-to-exit-thailand-market-citing-geostrategy-optimisation/)). No source names a single regional HQ city.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Singapore | Delivery Hero (Singapore) Pte. Ltd. — MAS Major Payment Institution | Not found | [MAS FID](https://eservices.mas.gov.sg/fid/institution/detail/426483-DELIVERY-HERO-SINGAPORE-PTE-LTD) · [SG T&C](https://www.foodpanda.sg/contents/terms-and-conditions.htm) |
| Singapore | Delivery Hero APAC Pte. Ltd.; DH Financial Services APAC Holding Pte. Ltd.; Tabsquare Pte. Ltd. | Not found | [DH AR 2025, subsidiary list](https://www.lobbyregister.bundestag.de/media/d4/45/775186/Delivery-Hero-Annual-Report-2025.pdf) |
| Pakistan | Delivery Hero Pakistan (Pvt) Ltd, Karachi | Not found | [PK T&C](https://www.foodpanda.pk/contents/terms-and-conditions.htm) · AR 2025 |
| Pakistan | R-Sc Internet Services Pakistan (Pvt) Ltd — pandapay issuer | Not found | [PK pandapay T&C](https://www.foodpanda.pk/contents/pandapay-user-account-terms-and-conditions) |
| Taiwan | Foodpanda Taiwan Co., Ltd. (富胖達股份有限公司) | Not found | [TW T&C](https://www.foodpanda.com.tw/contents/terms-and-conditions.htm) · AR 2025 |
| Philippines | Delivery Hero Philippines Inc., Makati — BSP OPS | OPSCOR-2020-0113 (BSP registration) | [PH pandapay T&C](https://www.foodpanda.ph/contents/pandapaytermsandconditions) · [PH T&C](https://www.foodpanda.ph/contents/terms-and-conditions.htm) |
| Malaysia | Delivery Hero Malaysia Sdn Bhd | Not found | [MY T&C](https://www.foodpanda.my/contents/terms-and-conditions.htm) |
| Hong Kong | Delivery Hero Food Hong Kong Limited | Not found | [HK T&C](https://www.foodpanda.hk/contents/terms-and-conditions.htm) |
| Bangladesh | Foodpanda Bangladesh Limited | Not found | [BD T&C](https://www.foodpanda.com.bd/contents/terms-and-conditions.htm) |
| Cambodia / Laos / Myanmar | Delivery Hero (Cambodia) Co. Ltd.; Delivery Hero (Lao) Sole Co. Ltd.; DH (Myanmar) Co. Ltd. | Not found | AR 2025 · KH/LA T&Cs |
| Brunei | Foodpanda (B) Sdn. Bhd., Muara | Not found | AR 2025 (not listed as an operating market) |

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| Pakistan | ✅ #1 | ✅ | Not researched live | Low |
| Taiwan | ✅ #2 | ✅ | Not researched live | Low (but exiting) |
| Philippines | ✅ #3 | ✅ | N/A — entity present | Low |
| Malaysia | ✅ #4 | ✅ | N/A — entity present | Low |
| Singapore | ✅ #5 | ✅ (MAS MPI) | N/A | Low |
| Cambodia / Laos / Myanmar | Not in supplied data | ✅ local entities, **but payments processed by Delivery Hero Malaysia Sdn Bhd** | Not researched live | ⚠️ **Yes — MY entity processes payments for KH/LA/MM** (KH/LA T&Cs, Khmer and Lao text, via Agent 1) |

No top-5 market lacks a local entity, so no cross-border warning applies to the top 5. The KH/LA/MM arrangement is the only cross-border processing pattern found. Card acquiring for those markets runs under per-market Adyen merchant IDs (`Foodpanda_KH`, `Foodpanda_MM`, `Foodpanda_LA`), and the contracting entity is Malaysian. `[INFERENCE, not confirmed]`: issuer approval rates on Cambodian, Lao and Myanmar cards processed against a Malaysian entity are likely to be weaker than domestic acquiring would give. These markets are small.

> **MANUAL:** Registration numbers were not found in any market. Check ACRA (SG), SECP (PK), SEC (PH), SSM (MY).

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| PK, TW, PH, MY, BD, KH, MM, LA (per-market accounts); SG + HK (shared `DeliveryHero` account) | **Adyen** — client-side encryption keys, `adyen_recurring_enabled: true` | [Source Code] | Embedded config on each `foodpanda.{cc}/contents/terms-and-conditions.htm` page (captured 2026-10-19) |
| APAC "10+ markets" | **Cybersource (Visa)** — local acquiring + Token Management Service; Visa cites +3.3% payment success | [Press Release] + [Provider Case Study] | [Marketech APAC, Jul 2024](https://marketech-apac.com/foodpanda-partners-with-cybersource-to-elevate-customer-checkout-experience/) · [Visa customer story](https://corporate.visa.com/en/customer-stories/foodpanda.html) |
| PH, MY, TH (historic), PK, BD, HK | **Antom / Alipay+ (Ant International)** — unified wallet interface; tokenised GCash; local settlement partners where Antom lacks rails | [Provider Case Study] | [Antom Knowledge, 6 Nov 2025](https://knowledge.antom.com/delivery-hero-antom-shaping-tomorrows-digital-platform-payments) · [Alipay+ sponsored, 2022](https://sponsored.bloomberg.com/article/alipay/upwardly-mobile-how-asia-largest-food-delivery-platform-creating-inclusive-digital-economy) |
| MY | **Touch 'n Go eWallet** via Alipay+ (Feb 2023); **pandacredit** stored value inside TNG (Mar 2025) | [Press Release] | [Business Wire](https://www.businesswire.com/news/home/20230131005758/en/) · [TechNode Global](https://technode.global/2025/03/03/foodpanda-malaysia-tng-digital-join-forces-to-launch-pandacredit-ewallet/) |
| MY | **Razer Merchant Services (Fiuu)** — FPX → DuitNow Online Banking with PayNet | [Press Release] | [Razer newsroom, May 2023](https://www.razer.com/newsroom/company-news/razer-merchant-services-scores-three-firsts-in-its-collaboration-with-paynet-to-enhance-the-payment-experience-for-foodpanda-merchants) |
| Group (SG team) | **Checkout.com, Adyen, MPGS** — "global partners" | [Job Listing] | [builtin — DH Specialist, Digital Payments](https://builtin.com/job/specialist-digital-payments/7605072) · [DH careers jid-7283](https://careers.deliveryhero.com/job/specialist-digital-payments-in-singapore-jid-7283) |
| SG, PH, MY, HK | **PayPal** (`paypal_environment: production`; PK/TW sandbox) | [Source Code] + PH T&C | Page config (Agent 2) · [PH T&C §7.5.1](https://www.foodpanda.ph/contents/terms-and-conditions.htm) |
| TW | **HSBC Taiwan** — trust account for collected merchant funds | [Terms/Privacy Policy] | [TW T&C §7.13](https://www.foodpanda.com.tw/contents/terms-and-conditions.htm) |
| SG | Rider payouts over FAST (also TH/MY real-time rails) — **HSBC** | [Provider Case Study] | [HSBC PDF](https://www.gbm.hsbc.com/-/media/media/gbm-global/pdf/articles/smarter-business-with-hsbc-foodpanda.pdf?download=1) `[UNVERIFIED — search summary only]` |
| HK | **HSBC PayMe** at checkout | [Provider Case Study] | [HSBC HK](https://www.business.hsbc.com.hk/en-gb/insights/optimising-sales/foodpanda-reduces-cash-on-delivery-with-payme) `[UNVERIFIED — search summary only]` |
| Shared bundle only (market not attributable) | Xendit (direct debit BPI/UBP/RCBC/Chinabank; PromptPay), Red Dot (PayLah!), SSLCommerz (BD: Nagad, bKash, upay, BanglaQR), Global Payments (PX Pay, TW), JazzCash direct | [Source Code] — weak (see Method note 3) | Agent 2 / Agent 4 page captures |

**Not found:** Stripe, Braintree, Worldpay, 2C2P, Omise, iPay88, Midtrans, PayMongo, Dragonpay, TapPay, ECPay, NewebPay.

**Single-PSP dependency:** No. At least two card acquirers per market are plausible (Adyen per-market accounts plus Cybersource "local acquiring" in 10+ markets). `[INFERENCE, not confirmed]` — which processor takes which share per market is not public.

#### 3B. Payment Orchestrator

**Classification: In-house orchestration layer.**

| Evidence | Type | Source |
|---|---|---|
| DH has a *"Payment Orchestration domain, within Payments Tribe"* delivering products *"via Delivery Hero's regional platforms"*; the posting lists *"payment orchestration, routing, or multi-PSP environments"* | [Job Listing] | [DH careers jid-10326](https://careers.deliveryhero.com/job/product-manager-payments-fintech-in-berlin-germany-jid-10326) |
| *"Software Engineer – Java/Kotlin (Fintech, Payment Orchestration)"* (expired) | [Job Listing] | [DH careers jid-4059](https://careers.deliveryhero.com/job/software-engineer-java-kotlin-fintech-payment-orchestration-in-berlin-germany-jid-4059) |
| *"we have built a payment recommendation system and a fallback system"* — Vaibhav Kanth, Product & Business Head, FinTech, DH | [Provider Case Study] | [Antom, 6 Nov 2025](https://knowledge.antom.com/delivery-hero-antom-shaping-tomorrows-digital-platform-payments) |
| *"that sort of orchestration and unified payment interface really saves a lot of payment operations OPEX for Foodpanda"* — Diego Garcia, 2C2P/Antom | [Provider Case Study] | same |
| Multi-acquirer per country: *"instead of having one acquirer, perhaps you can have 10 acquirers for each country"* — said as a **future** idea, not current practice | [Provider Case Study] | same |
| SG payments role owns "routing changes" and "routing strategy improvements" across Adyen, Checkout.com, MPGS | [Job Listing] | [builtin](https://builtin.com/job/specialist-digital-payments/7605072) |

> *"Confirmed orchestration-aware. The opening is coverage and depth, not the case for orchestration itself."* DH built its own layer. Argue reach and opportunity cost: more acquirers per country, local rails, and what the in-house team is not getting to. **Never** argue "you need orchestration".

Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno: no evidence. IXOPAY worked with DH in 2019 on rider cash collection ([IXOPAY](https://www.ixopay.com/en/news/delivery-hero-chooses-ixopay-to-streamline-the-cash-collection-process)); foodpanda is not named and the current status is unknown.

> **MANUAL:** Walk through app checkout in SG and PK with a proxy (Charles/mitmproxy) to see which processor hosts tokenise cards per market.

---

### Section 4: Alternative & Local Payment Methods

**Access caveat:** all `/contents/*` help-centre pages returned 403 to the method agent. "Not found" below means **not seen**, never **confirmed absent**.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| PK | Debit/credit cards | Cards | Active in checkout (Adyen `Foodpanda_PK`); press | Page config · [Daily Pakistan op-ed, Nov 2024](https://en.dailypakistan.com.pk/14-Nov-2024/why-paying-online-is-the-smart-choice) |
| PK | easypaisa | Digital wallet | Mentioned in press (Aug 2023) | [APP](https://www.app.com.pk/?p=678212) |
| PK | JazzCash | Digital wallet | Mentioned in press (Nov 2024 op-ed by foodpanda PK Head of Fintech). The 2018 deal was rider payouts only | [Daily Pakistan](https://en.dailypakistan.com.pk/14-Nov-2024/why-paying-online-is-the-smart-choice) · [JazzCash 2018](https://jazz.com.pk/media-center/detail/jazzcash-digitalizes-foodpandas-rider-payments) |
| PK | Cash on delivery | Cash | Mentioned in press — roughly half of orders `[UNVERIFIED — search summary only]` | [ProPakistani, Oct 2026](https://propakistani.pk/2026/10/09/foodpanda-and-hbl-expand-strategic-partnership-for-greater-digital-payment-adoption/) |
| PK | pandapay (stored balance, PKR 10k cap) | Closed-loop wallet | Mentioned in docs | [PK pandapay page](https://www.foodpanda.pk/contents/pandapay) |
| PK | **Raast** | Bank transfer / A2A | **Not found** | — |
| TW | Credit cards, Apple Pay, LINE Pay | Cards / wallet | Mentioned in press (Jul 2025) | [TechNews](https://technews.tw/?p=1406384) |
| TW | 全支付 PX Pay | Digital wallet | Mentioned in press (launched Jul 2025) | [TechNews](https://technews.tw/?p=1406384) |
| TW | COD (貨到付款) | Cash | Mentioned in docs | [TW T&C §6.2](https://www.foodpanda.com.tw/contents/terms-and-conditions.htm) |
| TW | **JKOPay** | Digital wallet | String in shared bundle only; **not confirmed live** | — |
| TW | Taiwan Pay, convenience store, instalments | — | **Not found** | — |
| PH | Visa, Mastercard, PayPal, GCash, COD | Cards / wallet / cash | Mentioned in docs | [PH T&C §7.5](https://www.foodpanda.ph/contents/terms-and-conditions.htm) |
| PH | Google Pay / Apple Pay | Wallet | Mentioned in docs (temporary-hold clause) | PH T&C |
| PH | **QR Ph on delivery** (any QR Ph bank/wallet incl. GCash, Maya) | A2A QR | Mentioned in press (16 May 2026) | [Newsbytes](https://newsbytes.ph/2026/05/16/foodpanda-adds-qrph-payments-for-cash-on-delivery-orders/) |
| PH | Maya (native in-app) | Digital wallet | **Not confirmed** (forum only) | [expat.com forum](https://www.expat.com/en/forum/asia/philippines/1095378-food-delivery-and-apps-in-the-philippines.html) |
| PH | InstaPay / online banking direct debit | Bank transfer | **Not confirmed** (Xendit PH-bank strings in shared bundle only) | — |
| MY | Cards | Cards | Active (Adyen `Foodpanda_MY`) | Page config |
| MY | FPX → DuitNow Online Banking | Bank transfer | Mentioned in press (May 2023) | [Razer newsroom](https://www.razer.com/newsroom/company-news/razer-merchant-services-scores-three-firsts-in-its-collaboration-with-paynet-to-enhance-the-payment-experience-for-foodpanda-merchants) |
| MY | **DuitNow QR on delivery** | A2A QR | Mentioned in docs | [MY T&C §8.10](https://www.foodpanda.my/contents/terms-and-conditions.htm) |
| MY | Touch 'n Go eWallet; pandacredit (inside TNG) | Digital wallet | Mentioned in press (Feb 2023; Mar 2025) | [Lowyat](https://lowyat.net/2023/294324/foodpanda-touch-n-go-ewallet) · [TechNode](https://technode.global/2025/03/03/foodpanda-malaysia-tng-digital-join-forces-to-launch-pandacredit-ewallet/) |
| MY | Boost, ShopeePay, BNPL (Atome etc.) | Wallet / BNPL | **Not found** | — |
| SG | Cards; PayPal; pandapay; COD | Cards / wallet / cash | Mentioned in docs (T&C §7.6, §7.7); PayPal production flag | [SG T&C](https://www.foodpanda.sg/contents/terms-and-conditions.htm) |
| SG | DBS PayLah! | Digital wallet | String only (Red Dot); app listing names foodpanda as a merchant — weak | [AppFollow](https://apps.appfollow.io/ios/dbs-paylah/878528688?country=sg) |
| SG | **PayNow** | A2A | **Not found** — no PayNow string anywhere in the captured bundles | — |
| Global | **pandapro subscription** | Recurring card billing | Mentioned in press (Nov 2025); 3DS-failure string for subscriptions in bundle | [Kyodo PR Wire](https://kyodonewsprwire.jp/index.php/release/202511219646) |

**Gaps worth flagging (all "not seen", none confirmed):**
- **Singapore — PayNow.** PayNow is the national A2A rail. Its absence from every captured string bundle is a **hypothesis to test in the app, not a claim to make**.
- **Pakistan — Raast.** Not seen. With COD at roughly half of orders `[UNVERIFIED]`, the A2A gap matters more than in any other market, but PK is digitising through wallets and cards (easypaisa, JazzCash, HBL).
- **Taiwan — JKOPay.** Not confirmed. This is moot once Grab takes over.

> **MANUAL:** VPN into SG, PK and PH and step through app checkout. Screenshot the payment-method list per market. This is the single most valuable manual check for this account.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Slow refunds — refund locked in pandapay wallet, not returned to card | News (via Reddit), SG | Isolated (press-amplified) | Undated | [The Independent SG](https://theindependent.sg/man-says-foodpanda-is-forcing-me-to-spend-this-refund-on-their-platform/) |
| Slow refunds — wallet-default refunds by policy | Official T&C, PK / TW / PH | Policy, not incident | Current | [PK pandapay](https://www.foodpanda.pk/contents/pandapay) · [TW T&C §6.3.1](https://www.foodpanda.com.tw/contents/terms-and-conditions.htm) · PH T&C |
| Checkout errors — "payment failed" but charged; refund not received after a week | TechEnclave forum | Isolated | Undated | [TechEnclave 1](https://techenclave.com/t/foodpanda-app-failed-payment-issue/231815) · [TechEnclave 2](https://techenclave.com/threads/foodpanda-app-failed-payment-issue.174031/) |
| Card charged during a platform outage | Technave, MY | Isolated | Likely 2021 | [Technave](https://technave.com/gadget/Update-foodpanda-app-is-now-back-online-25213.html) |
| Refund handling | Marketing-Interactive | Isolated | Undated | [Marketing-Interactive](https://www.marketing-interactive.com/foodpanda-called-out-for-ridiculous-way-of-handling-refund-requests) |
| Refund not given (SG) / prepaid order not delivered, not refunded (PK) | Trustpilot | Moderate `[UNVERIFIED — search summary only]` | May–Jul 2026 (SG); Feb 2026 (PK) | [Trustpilot SG](https://ie.trustpilot.com/review/www.foodpanda.sg) · [Trustpilot PK](https://www.trustpilot.com/review/foodpanda.pk?page=7) |

> *"The pattern is refunds routed into the closed-loop pandapay wallet. That is a deliberate retention design, not an infrastructure failure. It maps to Yuno only weakly. Do not pitch it as a payment problem."*

App Store / Google Play reviews and X were **not** covered (no results surfaced in budget).

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 16 Jul 2026 | **Uber offers €41.50/share cash for Delivery Hero** (~US$14.8bn equity value, ~34% premium). Prosus (~17%) has agreed to sell; 50%+1 acceptance threshold; completion expected **H2 2027**. DH to sell businesses in 14 markets to SSW Partners for ~€1.4bn (list unverified; reportedly no APAC foodpanda market) | M&A | [ESM Magazine (fetched)](https://www.esmmagazine.com/technology/uber-launches-14-8bn-offer-for-delivery-hero-to-create-global-platform-316659) · [TimesLive/Reuters](https://www.timeslive.co.za/news/sci-tech/2026-07-16-uber-launches-148bn-takeover-bid-for-delivery-hero/) · [Uber 10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000032/uber-20260630.htm) |
| 2 | 23 Mar 2026 → 27 Oct 2026 | **Grab to buy foodpanda Taiwan** for US$600m cash (2025 GMV US$1.8bn). TFTC extended its review on 22 Jul 2026; **decision due 27 Oct 2026**. Users to migrate to Grab by early 2027 | M&A | [Grab 6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000051/foodpandtaiwan-finalannoun.htm) · [TechNews](https://finance.technews.tw/2026/07/22/fair-trade-commission-20260722/) · [Taipei Times, 14 Oct 2026](https://www.taipeitimes.com/News/editorials/archives/2026/10/14/2003865916) |
| 3 | to 4 May 2026 | DH Singapore hiring **"Specialist, Digital Payments"** — Regional Payments Acceptance: PSP/payment-method **RFPs**, **Cost Per Order** ownership, routing changes, renegotiations; names Checkout.com, Adyen, MPGS | Payment Infrastructure Hiring | [builtin (fetched by agent)](https://builtin.com/job/specialist-digital-payments/7605072) |
| 4 | 23 May 2025 | **foodpanda exits Thailand** ("geostrategy optimisation"); foodpanda.co.th now redirects to robinhood.co.th; DH APAC regional team stays in Bangkok | Market Exit | [Marketech APAC](https://marketech-apac.com/foodpanda-to-exit-thailand-market-citing-geostrategy-optimisation/) · DH AR 2025 |
| 5 | Mar 2025 | Delivery Hero Food Hong Kong buys Deliveroo HK assets (€20.1m) as Deliveroo exits HK | M&A | DH AR 2025 · [WageIndicator](https://wageindicator.org/what-we-do/news-stories/gig-news/2025/march-2025-deliveroo-exits-hong-kong-sells-assets-to-foodpanda-amidst-rising-competition-from-keeta-and-foodpanda/) |

- **Public payment RFP:** *No public payment-related RFP found.* The SG job ad says the team **runs** PSP and payment-method RFPs, but that is internal process, not a public RFP. **No RFP override.**
- **Orchestration hiring:** DH Product Manager Payments (FinTech) — Payment Orchestration domain ([jid-10326](https://careers.deliveryhero.com/job/product-manager-payments-fintech-in-berlin-germany-jid-10326)).
- **Licences:** DH Singapore MAS MPI (incl. merchant acquisition, e-money) — current as of 25 Aug 2026. No new licence application found.
- **Leadership:** the last confirmed foodpanda APAC CEO appointment is John Fang, Oct 2023 ([Marketech](https://marketech-apac.com/foodpanda-names-john-fang-as-new-ceo-as-jakob-angele-steps-down-from-role)). No 2026 confirmation found that he is still in the role.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 9 Oct 2026 | foodpanda Pakistan and HBL expand partnership for digital payment adoption; "nearly half of all orders now made through online payments" | PK cash-to-digital; card/issuer alliance, not a gateway | [ProPakistani](https://propakistani.pk/2026/10/09/foodpanda-and-hbl-expand-strategic-partnership-for-greater-digital-payment-adoption/) `[UNVERIFIED — 403]` |
| 2 | 16 May 2026 | foodpanda PH launches QR-on-Delivery via QR Ph — quote from Lhecks De Castro, Director of Finance, foodpanda PH | Digitising COD; no PSP named | [Newsbytes (fetched)](https://newsbytes.ph/2026/05/16/foodpanda-adds-qrph-payments-for-cash-on-delivery-orders/) |
| 3 | 6 Nov 2025 | Delivery Hero × Antom: "shaping tomorrow's digital platform payments" — unified interface, tokenised GCash, 6 markets | Confirms wallet layer + in-house fallback engine | [Antom (fetched)](https://knowledge.antom.com/delivery-hero-antom-shaping-tomorrows-digital-platform-payments) |
| 4 | Jul 2025 | foodpanda Taiwan adds 全支付 PX Pay | TW wallet expansion (pre-sale) | [TechNews](https://technews.tw/?p=1406384) |
| 5 | Mar 2025 | foodpanda MY × TNG Digital launch pandacredit e-wallet inside Touch 'n Go | Wallet strategy via licensed partner in MY | [TechNode Global](https://technode.global/2025/03/03/foodpanda-malaysia-tng-digital-join-forces-to-launch-pandacredit-ewallet/) |

No provider removals found. The **Thailand exit (May 2025)** removed TrueMoney / PromptPay flows from the footprint.

---

### Section 8: Checkout Experience Audit

*Full checkout flow not accessible. Findings limited to publicly observable elements. The app was not tested, and the web bundle strings are group-wide.*

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | Custom-built DH checkout; Adyen client-side encryption keys embedded | N/A | [Source Code] |
| Guest checkout | String `GUEST_CHECKOUT_AUTH_ENTRY_CTA: "Continue without Registration"` exists; TW T&C §2.1 says an account is required | Unknown | Conflicting; market-specific |
| Steps to complete payment | Not observed | — | — |
| Card input experience | Adyen CSE (card encrypted in browser) | Good `[INFERENCE]` | — |
| Payment methods visible | Not observed per market (403) | — | See Section 4 |
| Location-based method display | Per-market config (Adyen merchant ID, PayPal environment differ by domain) | Good | — |
| Instalment / EMI options | Atome "3 payments, 0% interest" string in bundle; not attributable to a market | Unknown | — |
| 3DS implementation | 3DS strings incl. subscription 3DS failure; Agent 2 reports Adyen 3DS enabled except TW | Fair | Version not detected |
| PCI indicator | PSP-side card storage per T&Cs; Adyen CSE; Cybersource TMS tokens | Good | — |
| Mobile responsiveness | Mobile web 57–87% of web visits; app-first | N/A | App not tested |
| Multi-currency / local pricing | Single local currency per domain | N/A | — |
| Saved payment methods | "Saved payment methods", "Save this card for your next payment", PayLah! express checkout | Good | — |
| Error message clarity | "We're unable to process your payment"; `ApiPaymentFailureInvalidSavedInstrument` | Fair | — |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **Not found** — no attestation published for foodpanda or DH | — |
| Card data handling | *"With your consent, your credit card / payment information will be stored with our third party payment service provider(s)… foodpanda does not store your credit card or payment information."* Adyen CSE on web; Cybersource TMS tokens | [SG T&C](https://www.foodpanda.sg/contents/terms-and-conditions.htm) · [Visa story](https://corporate.visa.com/en/customer-stories/foodpanda.html) |
| Recommended Yuno integration | Back-to-back API (DH has its own orchestration layer and checkout; Yuno would sit as an additional routing/acquiring layer, not replace the front end) | `[INFERENCE, not confirmed]` |

`[INFERENCE, not confirmed]`: based on PSP-side card storage, Adyen CSE and Cybersource Token Management Service, the company's PCI scope is likely reduced, with the PSPs holding card data. Visa says Cybersource offloads foodpanda from PCI requirements in multiple markets.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: The stack decision is about to move — and the buyer is a Yuno customer.**
> **Evidence:**
> - §6: Uber's ~US$14.8bn cash offer for DH, completion H2 2027 ([ESM](https://www.esmmagazine.com/technology/uber-launches-14-8bn-offer-for-delivery-hero-to-create-global-platform-316659)).
> - §6: Taiwan is moving to Grab, users by early 2027 ([Grab 6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000051/foodpandtaiwan-finalannoun.htm)).
> - §3A: DH runs multiple acquirers plus its own orchestration domain.
> - Phase 0: Yuno's site says *"Yuno powers payments for … Uber"*.
>
> **Pain Point:** Two overlapping payment stacks, DH's in-house layer and Uber's Yuno-routed stack, will need to be reconciled after close. Meanwhile, Taiwan's acquiring and wallet contracts unwind. `[INFERENCE, not confirmed]`
> **Yuno Value Proposition:** If Uber already routes through Yuno, foodpanda's APAC acquirers and wallets become connectors on the same layer, not a second integration programme.
> **Best Success Case:** Uber as an **internal relationship**, not a citable case. **Rappi** as the citable multi-country delivery case.
> **Outreach Angle:** **Do not cold-email this.** Take it to Yuno's Uber account owner first. The right first move is an internal intro, timed to Uber's integration planning.
> **Suggested Subject Line:** *(internal)* foodpanda APAC acquirers ahead of the DH close

> **Insight #2: DH said on stage that per-country multi-acquirer routing is the next step. They don't have it yet.**
> **Evidence:**
> - §3B: on Antom's own stage, multi-acquirer per country (*"perhaps you can have 10 acquirers for each country"*) was presented as **future**, not current ([Antom](https://knowledge.antom.com/delivery-hero-antom-shaping-tomorrows-digital-platform-payments)).
> - §3A: there is one Adyen merchant account per market, with Cybersource as the second card path.
> - §6: the SG Payments Acceptance team owns routing changes and PSP RFPs ([builtin](https://builtin.com/job/specialist-digital-payments/7605072)).
>
> **Pain Point:** The in-house layer recovers failures with a recommendation and fallback engine, but depth per market is limited to the acquirers DH has integrated itself. Each new local acquirer is an engineering project for the central Payments Tribe.
> **Yuno Value Proposition:** Additional local acquirers per country behind DH's own routing logic, without the in-house team building each connector.
> **Best Success Case:** **Rappi** — multi-country delivery, 20+ processors, automatic rerouting ([y.uno](https://www.y.uno/en/success-stories/rappi)).
> **Outreach Angle:** "Your team said on Antom's stage that ten acquirers per country is where this goes. Curious how far the in-house layer has got on that in Pakistan and the Philippines."
> **Suggested Subject Line:** Ten acquirers per country

> **Insight #3: Cost Per Order on shrinking baskets.**
> **Evidence:**
> - §12 / AR 2025: Asia GMV −11.2%, attributed partly to *"lower average basket sizes"*.
> - AR 2025: DH says it is *"working with multiple payment service providers to lower payment costs"*.
> - §6: the SG Payments Acceptance role **owns the Cost Per Order metric** and runs renegotiations ([builtin](https://builtin.com/job/specialist-digital-payments/7605072)).
>
> **Pain Point:** Smaller baskets mean fixed per-transaction fees take a larger share of each order. Payment cost per order rises even when rates are flat. `[INFERENCE, not confirmed]`
> **Yuno Value Proposition:** Least-cost routing across acquirers and local rails per market, and leverage in PSP renegotiations from a credible multi-acquirer alternative.
> **Best Success Case:** Rappi (delivery, multi-processor). Use only Yuno's published figures, verbatim.
> **Outreach Angle:** "Delivery Hero's annual report blames part of Asia's GMV drop on smaller baskets. On a smaller basket, the fixed part of the payment fee is a bigger share of every order."
> **Suggested Subject Line:** Payment cost on a smaller basket

> **Insight #4: Cash is being digitised at the doorstep — but only through QR, not at checkout.**
> **Evidence:**
> - §4 / §7: QR Ph on delivery (PH, May 2026) and DuitNow QR on delivery (MY T&C §8.10).
> - Pakistan: about half of orders still COD `[UNVERIFIED]`.
> - §4: PayNow (SG) and Raast (PK) were **not seen** at checkout.
>
> **Pain Point:** Doorstep QR digitises COD but keeps the rider in the cash loop, with reconciliation at delivery. National A2A rails at checkout would move those orders to prepaid. `[INFERENCE, not confirmed]`
> **Yuno Value Proposition:** Local A2A rails (PayNow, Raast, InstaPay) as checkout connectors without a per-market build.
> **Best Success Case:** Rappi (many local methods across markets).
> **Outreach Angle:** Use as a **question only**: "You've put QR Ph and DuitNow QR at the door. Is A2A at checkout on the roadmap for PK and SG, or is the doorstep the deliberate design?" **Do not assert PayNow or Raast are missing** — this has not been verified.
> **Suggested Subject Line:** QR at the door vs QR at checkout

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. Your Antom panel put "ten acquirers per country" in the future tense. I'd like to know how far the in-house layer has got on that in Pakistan and the Philippines.
2. Delivery Hero's annual report blames part of Asia's GMV drop on smaller baskets, and on a smaller basket the fixed part of every payment fee gets heavier.
3. You've moved COD to QR Ph in Manila and DuitNow QR in Malaysia, but only at the door. Is checkout-side A2A deliberate or next?

**Cold call openers:**
1. "Saw your payments team owns Cost Per Order and runs the PSP RFPs. Quick question on how you're thinking about acquirer depth per market."
2. "Your team said on stage that the fallback engine is built in-house. I'm calling about what sits behind it, not about replacing it."
3. "QR at the door in the Philippines is a smart COD move. I'm curious whether checkout-side A2A is on the list."

⚠️ **Do not mention Uber, the takeover or Taiwan in cold outreach.** Uber is a Yuno customer and the deal has not closed. Taiwan is being sold. Neither is a hook for a stranger to raise.

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| GrabFood (Grab) | grab.com | Singapore | $22.1bn on-demand GMV FY2025 | SG, MY, PH, KH, MM, (TW from close) | In-house GrabLink gateway (licensed); Adyen, Stripe | `not-icp/grab.md` · [Grab 20-F](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm) |
| Uber Eats | ubereats.com | USA | — | TW (and acquiring DH) | **Yuno customer** (group level) | y.uno site |
| ShopeeFood (Sea) | shopee.com | Singapore | Not found | MY, SG | Nothing found | — |
| LINE MAN Wongnai | lineman.line.me | Thailand | Not found | TH (foodpanda exited) | Owns LINE Pay TH | [LMWN careers](https://careers.lmwn.com/line-pay) `[UNVERIFIED]` |
| Pathao Food | pathao.com | Bangladesh | Not found | BD | Own PSP licence; Pathao Pay (Jul 2025) | [TBS](https://www.tbsnews.net/economy/pathao-gets-payment-service-provider-license-609806) `[UNVERIFIED]` |
| Keeta (Meituan) | keeta.com | China / HK | Not found | HK | Not researched | WageIndicator (above) |
| Bykea / Cheetay | bykea.com | Pakistan | Not found | PK | Nothing found | [Pakistan Today, 2020](https://profit.pakistantoday.com.pk/2020/09/19/careem-vs-foodpanda-who-will-dominate-the-food-delivery-space-in-pakistan) |

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Swiggy | swiggy.com | Food delivery / q-commerce | India | Juspay customer story — orchestration-aware delivery peer | [juspay.io/customer-stories/swiggy](https://juspay.io/customer-stories/swiggy) |
| Zepto | zeptonow.com | Q-commerce | India | Juspay customer story | [juspay.io/customer-stories/zepto](https://juspay.io/customer-stories/zepto) |
| Baemin (DH) | baemin.com | Food delivery | South Korea | Sister DH brand; opened Apple Pay to foreign cards Jun 2026 | [Daum](https://v.daum.net/v/20260531105754068) `[UNVERIFIED]` |
| Lalamove | lalamove.com | On-demand logistics | HK, SEA | HSBC PayMe API / Omni Collect | [HSBC HK](https://www.business.hsbc.com.hk/en-gb/insights/managing-cash-flow/lalamove-enhances-ux-and-drives-growth-with-hsbcs-business-solutions) `[UNVERIFIED]` |
| StoreHub (Beep) | storehub.com | F&B ordering | MY | Launched delivery on 2C2P in 48 hours | [casestudies.com](https://www.casestudies.com/company/2c2p/case-study/beep-launches-delivery-in-48-hours-with-2c2p-helping-1500-fb-businesses-go-online) `[UNVERIFIED]` |
| Rappi | rappi.com | Super app / delivery | LatAm | **Yuno customer** — the closest profile case | [y.uno](https://www.y.uno/en/success-stories/rappi) |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| Swiggy | Juspay (Hyperswitch) | Not dated | Food delivery | [juspay.io](https://juspay.io/customer-stories/swiggy) |
| Zepto | Juspay | Not dated | Q-commerce | [juspay.io](https://juspay.io/customer-stories/zepto) |
| Rappi | Yuno | Not dated | Delivery super app (LatAm) | [y.uno](https://www.y.uno/en/success-stories/rappi) |
| Grab | In-house (GrabLink) | FY2025 20-F | Super app | `not-icp/grab.md` |

No case study found of a foodpanda-overlap competitor (Grab aside) adopting a third-party orchestrator.

#### 11D. Prospect Scoring

Peers were not fully scored. Budget went to the target, and most peers lack verified market, PSP and volume data. Scores below are partial and verified-only.

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| Grab — see `not-icp/grab.md` | 17 → 🟢 override | Routed to Partnerships | Repo |
| Baemin — DH sister brand; same parent decision | Not scored | ⬜ | — |
| Pathao — own PSP licence | Not scored | Likely Phase-0 flag (licensed PSP) | TBS `[UNVERIFIED]` |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | **foodpanda** | Target | PK, TW, PH, MY, SG, HK, BD, KH, LA, MM | 17 → 🟢 | 🟢 Medium | Uber takeover; in-house orchestration; CPO-owned payments team | ✅ Yes |
| 2 | Grab | Competitor | SEA + TW pending | 17 → 🟢 | Partnerships | Licensed in-house gateway | ✅ (not-icp) |
| 3 | Baemin | DH sister brand | KR | Not scored | 🟢 | Same Uber decision; foreign-card push | ✅ Yes |
| 4 | Lalamove | Peer | HK, SEA | Not scored | 🟢 | Multi-market, HSBC-heavy | ✅ Yes |
| 5 | LINE MAN Wongnai | Competitor | TH | Not scored | 🟡 | Owns LINE Pay TH | ✅ Yes |
| 6 | Deliveroo HK | Competitor | — | — | ❌ | Exited HK Mar 2025 — **stale TAL row** | ✅ Yes |
| 7 | StoreHub (Beep) | Peer | MY | Not scored | 🟡 | On 2C2P; mid-size | ❌ **Not in TAL** |
| 8 | ShopeeFood | Competitor | MY, SG | Not scored | 🔴 | Likely in-house (Sea) | ❌ (Shopee is) |
| 9 | Pathao | Competitor | BD | Not scored | 🔴 | Own PSP licence — likely Phase-0 | ✅ Yes |
| 10 | Cheetay | Competitor | PK | Not scored | 🔴 | Status unverified | ❌ Not in TAL |

**Genuine find not on the TAL:** StoreHub (MY) — modest. **Stale TAL rows to clean:** Deliveroo HK (exited); "EASI" for foodpanda.com.tw (wrong name — Foodpanda Taiwan Co., Ltd., and being sold to Grab).

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | foodpanda not reported separately. DH Asia segment revenue **€4,417.7m FY2025** (+8.5%), incl. Baemin (Korea) | [DH AR 2025](https://www.lobbyregister.bundestag.de/media/d4/45/775186/Delivery-Hero-Annual-Report-2025.pdf) |
| GMV | DH Asia **€20,779.7m FY2025** (−11.2%; −9.3% like-for-like excl. Thailand), 42.2% of group GMV. **foodpanda Taiwan: US$1.8bn 2025 GMV** | AR 2025 · [Grab 6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000051/foodpandtaiwan-finalannoun.htm) |
| Average Transaction Value (USD) | **Not found** — DH does not disclose Asia AOV | — |
| Est. Annual Transactions | Not calculable (no sourced AOV) | — |
| **Monthly transaction count** | **⚠️ NOT FOUND — ASSUMED ≥100,000/month. [ASSUMPTION — not researched.]** Basis: ~10.5M monthly **web** visits on 5 of 10 domains with the app excluded; US$1.8bn Taiwan GMV alone. At any plausible delivery basket, that is millions of orders a year in Taiwan alone. No AOV is sourced, so this is **not** a derivation. Billing unit: consumer order. pandapro subscription billing is additional and recurring. | Per the disclosure rule |
| Active Customers / Users | Not found for foodpanda | — |
| Primary Currency | PKR, TWD, PHP, MYR, SGD, HKD, BDT (+ KHR/USD, LAK, MMK) | Country domains |
| Top 3 Markets by Revenue | Not disclosed. By web traffic: PK, TW, PH | Section 1 |
| Billing channel split (web vs app store) | Orders are paid through foodpanda's own checkout (in-app via its PSPs), not Apple/Google IAP. Physical goods and services fall outside app-store billing rules `[INFERENCE, not confirmed]` | — |

---

### Overall Research Confidence

**Medium.**
- **Traffic was supplied** (SimilarWeb, 2026-10-19), but covers only 5 of 10 markets, web only, with no per-country visit counts.
- **Strong:** Phase 0 (MAS register fetched), PSP stack (per-market Adyen IDs extracted first-hand, Cybersource and Antom provider pages), orchestration classification (DH job ads + DH executive quote), and corporate developments (Uber, Grab, Thailand — fetched or first-party filings).
- **Weak:**
  - Section 4: help centres blocked (403), so every rail gap is "not seen".
  - Section 5: complaints mostly undated or search-summary only; app-store reviews not covered.
  - Section 8: app not tested.
  - Section 12: no AOV and no foodpanda order count.
  - Section 11D: peers not scored.

---

### Manual Research Recommendations

> **Area:** Monthly transaction count (Section 12)
> **Why it matters:** It is the only gate that can reject an account, and it is assumed here. It is almost certainly irrelevant at this scale, but it must be sourced.
> **Suggested manual action:** Ask in discovery, or find DH's Q3 2026 trading update for Asia order counts.

> **Area:** Uber relationship and deal timing (Phase 0, Insight #1)
> **Why it matters:** Uber, a Yuno customer, is acquiring the parent. Cold outreach to foodpanda without that account team's knowledge risks an internal conflict and a wasted thread.
> **Suggested manual action:** Message the Yuno Uber account owner before any sequence. Ask whether Uber's Yuno footprint covers Uber Eats and whether DH integration planning has started.

> **Area:** Ant Group / Antom conflict (Section 3A)
> **Why it matters:** Ant Group is a Yuno customer and is foodpanda's wallet aggregation layer in six markets. This is the same issue as Lazada.
> **Suggested manual action:** One question to Partnerships covering both accounts: is Antom a connector partner at Yuno, or a competitor at the checkout?

> **Area:** Phase 0 — MAS merchant-acquisition licence (Phase 0)
> **Why it matters:** If DH Singapore acquires for third parties, the gate fires and this routes to Partnerships.
> **Suggested manual action:** Partnerships to confirm. The working read is captive marketplace collection.

> **Area:** Checkout methods per market (Section 4)
> **Why it matters:** PayNow (SG), Raast (PK) and Maya/InstaPay (PH) are hypotheses only.
> **Suggested manual action:** Install the foodpanda app with a VPN to SG, PK and PH and screenshot the payment-method list.

> **Area:** Taiwan TFTC decision (Section 6)
> **Why it matters:** It is due 27 Oct 2026 and determines whether Taiwan, 23% of web traffic, leaves the account.
> **Suggested manual action:** Check the TFTC announcement on or after 27 Oct.

---

### Appendix: All Source URLs

**Phase 0 / Section 2**
- https://eservices.mas.gov.sg/fid/institution/detail/426483-DELIVERY-HERO-SINGAPORE-PTE-LTD
- https://www.foodpanda.sg/contents/terms-and-conditions.htm
- https://www.foodpanda.sg/contents/pandapay-user-account-terms-and-conditions
- https://www.foodpanda.ph/contents/pandapaytermsandconditions
- https://www.foodpanda.ph/contents/terms-and-conditions.htm
- https://www.foodpanda.pk/contents/terms-and-conditions.htm
- https://www.foodpanda.pk/contents/pandapay-user-account-terms-and-conditions
- https://www.foodpanda.pk/contents/pandapay
- https://www.foodpanda.my/contents/terms-and-conditions.htm
- https://www.foodpanda.com.tw/contents/terms-and-conditions.htm
- https://www.foodpanda.hk/contents/terms-and-conditions.htm
- https://www.foodpanda.com.bd/contents/terms-and-conditions.htm
- https://www.lobbyregister.bundestag.de/media/d4/45/775186/Delivery-Hero-Annual-Report-2025.pdf
- https://www.y.uno/en/success-stories
- https://marketech-apac.com/foodpanda-to-exit-thailand-market-citing-geostrategy-optimisation/

**Section 3**
- https://marketech-apac.com/foodpanda-partners-with-cybersource-to-elevate-customer-checkout-experience/
- https://corporate.visa.com/en/customer-stories/foodpanda.html
- https://knowledge.antom.com/delivery-hero-antom-shaping-tomorrows-digital-platform-payments
- https://sponsored.bloomberg.com/article/alipay/upwardly-mobile-how-asia-largest-food-delivery-platform-creating-inclusive-digital-economy
- https://www.businesswire.com/news/home/20230131005758/en/
- https://technode.global/2025/03/03/foodpanda-malaysia-tng-digital-join-forces-to-launch-pandacredit-ewallet/
- https://www.razer.com/newsroom/company-news/razer-merchant-services-scores-three-firsts-in-its-collaboration-with-paynet-to-enhance-the-payment-experience-for-foodpanda-merchants
- https://builtin.com/job/specialist-digital-payments/7605072
- https://careers.deliveryhero.com/job/specialist-digital-payments-in-singapore-jid-7283
- https://careers.deliveryhero.com/job/product-manager-payments-fintech-in-berlin-germany-jid-10326
- https://careers.deliveryhero.com/job/software-engineer-java-kotlin-fintech-payment-orchestration-in-berlin-germany-jid-4059
- https://www.ixopay.com/en/news/delivery-hero-chooses-ixopay-to-streamline-the-cash-collection-process
- https://www.gbm.hsbc.com/-/media/media/gbm-global/pdf/articles/smarter-business-with-hsbc-foodpanda.pdf?download=1
- https://www.business.hsbc.com.hk/en-gb/insights/optimising-sales/foodpanda-reduces-cash-on-delivery-with-payme

**Section 4**
- https://www.app.com.pk/?p=678212
- https://en.dailypakistan.com.pk/14-Nov-2024/why-paying-online-is-the-smart-choice
- https://jazz.com.pk/media-center/detail/jazzcash-digitalizes-foodpandas-rider-payments
- https://technews.tw/?p=1406384
- https://newsbytes.ph/2026/05/16/foodpanda-adds-qrph-payments-for-cash-on-delivery-orders/
- https://www.expat.com/en/forum/asia/philippines/1095378-food-delivery-and-apps-in-the-philippines.html
- https://lowyat.net/2023/294324/foodpanda-touch-n-go-ewallet
- https://apps.appfollow.io/ios/dbs-paylah/878528688?country=sg
- https://kyodonewsprwire.jp/index.php/release/202511219646

**Section 5**
- https://theindependent.sg/man-says-foodpanda-is-forcing-me-to-spend-this-refund-on-their-platform/
- https://techenclave.com/t/foodpanda-app-failed-payment-issue/231815
- https://techenclave.com/threads/foodpanda-app-failed-payment-issue.174031/
- https://technave.com/gadget/Update-foodpanda-app-is-now-back-online-25213.html
- https://www.marketing-interactive.com/foodpanda-called-out-for-ridiculous-way-of-handling-refund-requests
- https://ie.trustpilot.com/review/www.foodpanda.sg
- https://www.trustpilot.com/review/foodpanda.pk?page=7

**Sections 6–7**
- https://www.esmmagazine.com/technology/uber-launches-14-8bn-offer-for-delivery-hero-to-create-global-platform-316659
- https://www.timeslive.co.za/news/sci-tech/2026-07-16-uber-launches-148bn-takeover-bid-for-delivery-hero/
- https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000032/uber-20260630.htm
- https://www.sec.gov/Archives/edgar/data/1855612/000185561226000051/foodpandtaiwan-finalannoun.htm
- https://finance.technews.tw/2026/07/22/fair-trade-commission-20260722/
- https://www.taipeitimes.com/News/editorials/archives/2026/10/14/2003865916
- https://wageindicator.org/what-we-do/news-stories/gig-news/2025/march-2025-deliveroo-exits-hong-kong-sells-assets-to-foodpanda-amidst-rising-competition-from-keeta-and-foodpanda/
- https://marketech-apac.com/foodpanda-names-john-fang-as-new-ceo-as-jakob-angele-steps-down-from-role
- https://propakistani.pk/2026/10/09/foodpanda-and-hbl-expand-strategic-partnership-for-greater-digital-payment-adoption/

**Section 11**
- https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm
- https://juspay.io/customer-stories/swiggy
- https://juspay.io/customer-stories/zepto
- https://www.y.uno/en/success-stories/rappi
- https://careers.lmwn.com/line-pay
- https://www.tbsnews.net/economy/pathao-gets-payment-service-provider-license-609806
- https://profit.pakistantoday.com.pk/2020/09/19/careem-vs-foodpanda-who-will-dominate-the-food-delivery-space-in-pakistan
- https://v.daum.net/v/20260531105754068
- https://www.business.hsbc.com.hk/en-gb/insights/managing-cash-flow/lalamove-enhances-ux-and-drives-growth-with-hsbcs-business-solutions
- https://www.casestudies.com/company/2c2p/case-study/beep-launches-delivery-in-48-hours-with-2c2p-helping-1500-fb-businesses-go-online

**Local**
- `accounts/traffic/foodpanda.md` (SimilarWeb, supplied 2026-10-19)
- `accounts/apac-tal.csv` (Foodpanda, EASI, Baemin rows)
- `not-icp/grab.md`

</details>
