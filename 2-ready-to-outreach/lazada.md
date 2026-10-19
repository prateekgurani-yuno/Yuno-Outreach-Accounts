# Lazada

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 17 / 29 → ⭐ High Priority **on arithmetic** — **ANALYST OVERRIDE applied, tier set DOWN to 🟢 Medium.** See the ICP breakdown for the reasoning.
**Industry:** Online marketplace (general e-commerce, B2C + LazMall) across six Southeast Asian markets · **HQ:** Singapore — holdco **Lazada South East Asia Pte. Ltd.** (incorporated 19 Jan 2012), a consolidated subsidiary of Alibaba Group · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **In-house / captive** — card acquiring, processing, settlement and the card vault run through **Alipay / Ant entities** (Lazada's sister group), with local aggregators such as **2C2P** (also Ant-owned) underneath. Not greenfield. Not a third-party orchestrator displacement.
**⛔ READ BEFORE ANY OUTREACH:** **Ant Group is on Yuno's own site-wide customer list.** Lazada's acquirer is a Yuno customer's affiliate. Clear this with your manager / Partnerships before sequencing — see Phase 0 note and Insight #1.

---

> # 🔒 PHASE 0 — QUALIFICATION GATE
>
> | Rule | Result |
> |---|---|
> | PSP / gateway / acquirer / orchestrator | **Does not fire.** Lazada is the marketplace operator. Its payment licences are held by **others**: the PH Lazada E-Wallet *"is operated by Alipay Philippines Inc. ("Alipay") for Lazada E-Services Philippines, Inc."* ([lazada.com.ph/terms-of-use](https://www.lazada.com.ph/terms-of-use/)); the MY Lazada Wallet sits on **AIMY Merchant Services Sdn Bhd (formerly Alipay Malaysia)**'s BNM e-money licence ([BNM register](https://www.bnm.gov.my/en/-/alipay-malaysia-sdn-bhd)); SG card acquiring is contracted to **Alipay** entities ([Alipay Merchant Acquisition Services Agreement, Lazada SG](https://img-ovs.alicdn.com/other/common/8423899fc94b48b9a3f5224c66cf6bfa)). No payment licence in a Lazada entity's own name was found in any market. One loose end: "**Lazada Payfin**" is named as a LazPayLater MY counterparty by a seller-tool blog ([BigSeller](https://www.bigseller.pro/blog/articleDetails/4202/lazada-paylater-2026.htm)); its licensing status is unverified. |
> | Existing Yuno customer | **Lazada: no.** `https://y.uno/en` fetched 2026-10-19 contains zero occurrences of "lazada" or "alibaba". **But "antgroup" appears in the site-wide customer logo set** (3 occurrences). Ant Group is not Lazada — but Ant entities are Lazada's acquirer. **Flag, not a rejection.** |
> | No online payment volume | Does not fire. |
> | HQ west of Dubai | Does not fire — Singapore HQ, all six markets in territory. |
> | Monthly transactions < 40,000 (sourced) | **Does not fire.** No sourced figure exists either way (Alibaba does not break out Lazada orders). Assumed far above 100k/month — see Section 12. |

> # ⚠️ METHOD NOTES — disclosed up front
>
> 1. **Traffic was supplied** (`accounts/traffic/lazada.md`, Similarweb Sales Intelligence, pulled 2026-10-19, Jul–Sep 2026). Its caveats are carried through this report: **(a)** only top-10 countries per domain, share only — per-country visits below are `[DERIVED from supplied share, not a SimilarWeb figure]`; **(b)** shares are single-domain, so the combined split was built visits-first (share × domain avg monthly visits), never by averaging percentages; **(c)** **mobile app traffic is excluded**; **(d)** **Lazada is app-first — web traffic is used as a market-mix signal only and was NOT used to size transactions or the 40k gate.**
> 2. **Fetch worked** (WebFetch and curl both). Phase 2 agents were launched in parallel with Agent 1 because the supplied traffic already fixed the market list (SG, ID, MY, TH, VN, PH).
> 3. **Lazada's help centre and four of six T&C pages are JavaScript-rendered.** Curl/WebFetch returned shells. I rendered the help centre with headless Chromium: the payment-methods pages now return a **Lazada-generated AI summary**, not the article. The **PH and MY summaries are single-market and match the live footers** and are used (labelled). The **SG summary is contaminated** — it lists TrueMoney, GCash, Maya and "Sacombank Bank Card" (Thai/Philippine/Vietnamese methods) on the Singapore site — and is **excluded** except where noted.
> 4. **The WebFetch tool's own summary is not a source either.** My first WebFetch of lazada.sg reported "UPI" in the footer — the image is **UnionPay**, not India's UPI (logo checked by Agent 3).

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Lazada is Alibaba's Southeast Asian e-commerce marketplace, operating in Singapore, Indonesia, Malaysia, Thailand, Vietnam and the Philippines through local operating companies under a Singapore holdco. It is the #3 SEA platform behind Shopee and TikTok Shop/Tokopedia and is shrinking: Alibaba's FY2026 filings cite a **revenue decline at Lazada**, and it cut ~5% of staff across all six markets in June 2026. Its payments run on **captive Ant/Alipay infrastructure** — Alipay is contractually the SG acquirer and card vault, and Ant's 2C2P aggregates Thai local methods.

**SimilarWeb total visits:** **~68.9M / month** (Jul–Sep 2026 average, sum of six country domains) — **supplied** 2026-10-19. Web only; the app — where most orders happen — is excluded.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇹🇭 Thailand | 34.0% (~23.4M/mo) | COD, Visa/MC/JCB/UnionPay (footer); TrueMoney (Lazada promo page); 20+ channels via 2C2P incl. wallets, online/mobile banking, card instalments (2C2P case study) | **PromptPay / Thai QR not found** by name (not confirmed absent — likely within 2C2P's channels) | ⚠️ Lazada Limited — secondary sources only, no reg. no. |
| 2 | 🇵🇭 Philippines | 17.7% (~12.2M/mo) | Lazada Wallet, GCash, Maya, Visa/MC/JCB/Amex/UnionPay, COD, instalments incl. BDO, LazPayLater (CIMB) | **InstaPay / online banking and OTC cash (7-Eleven, Bayad) not found** | ✅ Lazada E-Services Philippines, Inc. (SEC CS201203115) |
| 3 | 🇮🇩 Indonesia | 15.1% (~10.4M/mo) | Visa/MC/UnionPay, COD, QRIS-on-delivery via DANA (2023), 0% instalments (banner), Lazada Credit via DANA/EDIK | **Virtual account / bank transfer and QRIS at online checkout not found** (dominant rails) | ✅ PT Ecart Webportal Indonesia |
| 4 | 🇻🇳 Vietnam | 10.7% (~7.4M/mo) | Visa/MC/JCB, NAPAS, MoMo, ZaloPay, card instalments, COD | **VietQR / VNPay not found** | ✅ Recess Company Limited (tax code 0308808576) |
| 5 | 🇲🇾 Malaysia | 7.6% (~5.2M/mo) | Lazada Wallet, cards (Visa/Amex/UnionPay), online banking (8 banks), Touch 'n Go eWallet, 7-Eleven/99 Speedmart cash, Maybank instalments, LazPayLater, COD | **DuitNow not found**; FPX probable (bank logos) but never named | ⚠️ Ecart Services Malaysia Sdn Bhd (2022 affiliate T&C, not consumer T&C) |

All six markets have a local operating entity. Singapore (HQ) is #6 at 6.6%. **No regulatory acquiring gate applies** — this is not a cross-border story.

### Legal entities
- **Lazada South East Asia Pte. Ltd.** (Singapore, holdco) — incorporated 19 Jan 2012; reg. no. not found
- **Lazada Singapore Pte. Ltd.** (Singapore) — UEN **201403859E**
- **Lazada E-Services Philippines, Inc.** (Philippines) — **CS201203115**
- **PT Ecart Webportal Indonesia** (Indonesia) — reg. no. not found
- **Recess Company Limited** (Vietnam) — tax code **0308808576**
- **Ecart Services Malaysia Sdn Bhd** (Malaysia) — reg. no. not found; medium confidence
- **Lazada Limited** (Thailand) — low confidence, secondary sources only

### Known PSPs
- **Alipay (Ant Group) entities** — [Terms/Privacy Policy] — merchant acquirer, processor, settlement agent and card vault (**SG**, contract v3.0 Nov 2022); Lazada Wallet operator (**PH**); wallet licence-holder and registered merchant acquirer (**MY**, AIMY); named in the ID payment-protection policy
- **2C2P** (Ant-owned, "2C2P by Antom") — [Provider Case Study] — single-point aggregation of 20+ local channels, single settlement (**TH**)
- **DANA / PT Espay Debit Indonesia Koe** — [Terms/Privacy Policy] — Lazada Credit balance; QRIS-on-delivery (**ID**)
- **CIMB Bank PH** — [Third-Party Report] — LazPayLater credit line (**PH**); **Atome + "Lazada Payfin"** — LazPayLater (**MY**)

### Orchestration status
**In-house orchestration layer (captive group infrastructure).** Ant/Alipay entities are contractually the acquirer and processor in SG ([agreement cl. 3.1, 3.7](https://img-ovs.alicdn.com/other/common/8423899fc94b48b9a3f5224c66cf6bfa)), hold the stored cards (cl. 3.8), and run the wallet in PH and MY. A Sept 2026 Lazada job ad has payments finance working *"closely with Ant International payment stakeholders"* ([job ad](https://jobs.menlovc.com/companies/luca-2/jobs/95280802-regional-finance-manager-payments-marketing-solutions)). **No third-party orchestrator found** (Juspay, Spreedly, Primer, Gr4vy, Payrails, Yuno — all negative).

### Buying signals
- 💼 **Payments finance hire, posted 30 Sep 2026** — Regional Finance Manager, Payments & Marketing Solutions: owns *"payment channel P&L"*, *"payment cost optimisation"*, *"incentive economics for payment partners"* and chargeback-loss escalation ([job ad](https://jobs.menlovc.com/companies/luca-2/jobs/95280802-regional-finance-manager-payments-marketing-solutions))
- 📉 **Cost pressure** — Alibaba FY2026: international retail revenue growth *"partly offset by … a 3% decline from Lazada"* ([Alibaba FY2026 Annual Report](https://www.sec.gov/Archives/edgar/data/1577552/000119312526274928/d133513dex991.pdf)); ~5% workforce cut across six markets, Jun 2026 ([Vulcan Post](https://vulcanpost.com/911933/lazada-southeast-asia-singapore-layoffs-2026/))
- 💰 **Payment-fee repricing** — LazPayLater MY seller fee raised 3.5% → 4.5% + SST from 1 Jan 2026 ([BigSeller](https://www.bigseller.pro/blog/articleDetails/4202/lazada-paylater-2026.htm)) — payments is being run as a P&L line
- 🤝 **Competitor orchestration** — Zalora runs BridgerPay as a *"single orchestration layer"* across SEA (Nov 2025) ([BridgerPay](https://bridgerpay.com/learn/bridger-stories/Jyg0jmdNvp2xUmIJedJ4))

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Lazada` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 17 / 29 (arithmetic) → override to 🟢 Medium
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | +5 | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. [ASSUMPTION — not researched.]** Basis: ~68.9M monthly web visits on six domains *excluding* the app, where most orders happen; #3 SEA marketplace; Alibaba invested ~US$7.7bn. Alibaba does not disclose Lazada orders, GMV or buyers. Band scored per the disclosure rule; **not a measurement.** |
| Orchestration status | +1 | ✅ In-house / captive Ant-Alipay acquiring and vault (SG contract; PH, MY wallet licences). |
| 3+ countries | +3 | ✅ Six markets >1% combined traffic; six local operating entities. |
| Multiple PSPs | +3 | ✅ Alipay (SG acquiring) + 2C2P (TH aggregation) + DANA (ID) + CIMB/Atome (BNPL). **Caveat:** Alipay and 2C2P are both Ant-owned — see override. |
| Local rail or licensing gap in a top-3 market | 0 | ⬜ PromptPay (TH), VA/QRIS-at-checkout (ID), InstaPay/OTC (PH) **not found** — but no source confirms **absence**, and help centres were only partly readable. Uncertain = 0. No entity gaps. |
| Recent expansion | 0 | ❌ None in 12 months. Contraction (layoffs, revenue decline). |
| Payment issues reported | 0 | ⬜ Refund-handling complaints on Trustpilot are search-summary only; payment-failure complaints found are isolated and 2018–2020. |
| Funding >$10M | 0 | ❌ Last sourced Alibaba injection is US$230M in May 2024 — outside 12 months. |
| High traffic outside home | +2 | ✅ Singapore (HQ) = 6.6% of combined web traffic. |
| Competitor using orchestration | +2 | ✅ Zalora → BridgerPay (vendor case study, fetched). |
| Payment job postings | +1 | ✅ Regional Finance Manager, Payments & Marketing Solutions (posted 30 Sep 2026). |

**Tier on arithmetic:** 17 → ⭐ High Priority.

**ANALYST OVERRIDE → 🟢 Medium.** Three reasons:
1. **Double-counting.** "3+ countries" and "high traffic outside home" both fire on one fact: Lazada is a six-country business with an HQ in its smallest market. "Multiple PSPs" fires on two providers (Alipay and 2C2P) that are **both Ant Group**. Remove the duplicates and the score is **12 → 🟢 Medium**.
2. **The acquirer is a group affiliate and holds the cards.** Alipay stores buyers' saved cards *"on behalf of the Platform Operators"* (cl. 3.8). Moving routing to a third party means token portability out of Ant, and a commercial decision Alibaba would make about its own sister company. That is a very long and political sale.
3. **Ant Group is a Yuno customer.** Pitching Lazada a layer that routes volume away from Ant's acquiring is a potential conflict. This needs an internal decision before outreach, not after.

What keeps it at Medium and not Low: the volume is very large, payments is explicitly run as a cost-optimised P&L (Sept 2026 job ad, 2026 BNPL fee rise), and Yuno already has an Ant relationship — which could make this a **partner-assisted** conversation rather than a displacement one.

### Source Notes
- ✅ SG card acquiring, processing and card storage by Alipay entities — Alipay Merchant Acquisition Services Agreement (Lazada Singapore), v3.0, 14 Nov 2022, clauses 3.1(a), 3.7, 3.8 (read in full)
- ✅ PH Lazada E-Wallet operated by Alipay Philippines Inc., BSP-regulated — live T&C
- ✅ MY Lazada Wallet on AIMY (formerly Alipay Malaysia) e-money licence; AIMY is also a registered non-bank merchant acquirer — BNM register
- ✅ PCI DSS v4.0 Attestation of Compliance for Lazada South East Asia Pte Ltd (atsec, issued 30 Sep 2024, **expired 29 Sep 2025**) — linked from the live lazada.sg footer
- ✅ Ant International named in the Sept 2026 payments finance job ad
- ⚠️ 2C2P Thailand — vendor case study dated Nov 2023; lists Lazada's needs, does not say 2C2P acquires cards
- ⚠️ Lazada market-share decline (Cube, Momentum Works) — search summaries only, not used for scoring
- ⚠️ CEO James Dong — no 2025–26 source confirms he is still group CEO
- ⚠️ Lazada Payfin — named by one seller-tool blog; entity and licence unverified

### Success Case Alternatives
- **Rappi** — **Tier 1-ish.** A multi-country marketplace / super app with hundreds of local methods. It is the closest pattern to Lazada: one platform, many country-specific rails. Results are LATAM; do not imply Asian numbers.
- **Ant Group (Yuno customer)** — **not a case to cite, a relationship to use.** Ask internally what Ant uses Yuno for. If Antom/2C2P is a Yuno partner rather than a competitor at Lazada's checkout, the pitch changes from "route around your acquirer" to "extend what Ant already does with Yuno".
- **Livelo** — only if discovery shows Lazada runs 2+ acquirers with no failover. No evidence yet.

---

## Executive Summary

Lazada is Alibaba's Southeast Asian marketplace: six local operating companies (SG, ID, MY, TH, VN, PH) under a Singapore holdco, ~68.9M monthly web visits plus a dominant app. Thailand is the largest web market (34%), then the Philippines (18%) and Indonesia (15%). Its payment stack is **captive to Ant Group**: Alipay entities are the contracted acquirer, processor, settlement agent and card vault in Singapore, operate the Lazada Wallet in the Philippines and license it in Malaysia; Ant-owned 2C2P aggregates 20+ Thai channels. **No third-party orchestrator found.** The motion is **in-house/captive** — the hardest kind — and it is complicated by Ant Group being a Yuno customer. The real opening is cost: Lazada's revenue is declining, it is cutting staff, and it is hiring for "payment cost optimisation" and payment-partner incentive economics.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** **Supplied** — Similarweb Sales Intelligence, `accounts/traffic/lazada.md`, pulled 2026-10-19, Jul–Sep 2026, desktop + mobile web. **App traffic excluded.**

**Per-domain average monthly visits (supplied):** lazada.co.th 24.29M · lazada.com.ph 14.36M · lazada.co.id 10.81M · lazada.vn 7.770M · lazada.com.my 6.276M · lazada.sg 5.358M · **Total 68.86M**

**Combined country split** — built visits-first per the file's rule (share × that domain's monthly visits, summed across domains, divided by 68.86M). Each domain's tail outside its top 10 (1.6%–7.5%) is unattributed, so every share is a **lower bound**.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | Thailand | **34.03%** | ~23.43M `[DERIVED]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | Philippines | **17.71%** | ~12.19M `[DERIVED]` | Not supplied | same |
| 3 | Indonesia | **15.14%** | ~10.42M `[DERIVED]` | Not supplied | same |
| 4 | Vietnam | **10.69%** | ~7.36M `[DERIVED]` | Not supplied | same |
| 5 | Malaysia | **7.58%** | ~5.22M `[DERIVED]` | Not supplied | same |
| 6 | Singapore | **6.57%** | ~4.53M `[DERIVED]` | Not supplied | same |
| 7 | United States | 1.47% | ~1.01M `[DERIVED]` | Not supplied | same |
| 8 | China | 1.33% | ~0.92M `[DERIVED]` | Not supplied | same |
| 9 | India | 0.57% | ~0.39M `[DERIVED]` | Not supplied | same |
| 10 | United Kingdom | 0.24% | ~0.17M `[DERIVED]` | Not supplied | same |

- **High priority (>5%):** TH, PH, ID, VN, MY, SG — every Lazada market, each with a local entity.
- Each domain is 79.5%–95.8% domestic. **Lazada is six domestic businesses, not a cross-border one.** US and China traffic is most likely diaspora browsing and sellers. No checkout evidence suggests material cross-border buying.
- **Device split:** Mobile web leads on five domains (56–70%). lazada.com.ph is the exception at 55% desktop.
- **Do not read this as transaction share.** The traffic file itself warns that Lazada is app-first in all six markets. Market-mix signal only.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Singapore. Holdco **Lazada South East Asia Pte. Ltd.**, incorporated 19 Jan 2012, defined by Alibaba as *"our consolidated subsidiary"* ([Alibaba FY2026 Annual Report, SEC 6-K ex. 99.1](https://www.sec.gov/Archives/edgar/data/1577552/000119312526274928/d133513dex991.pdf)). Office per the PCI attestation: 51 Bras Basah Road, #01-21, Lazada One, Singapore ([AoC](https://img.lazcdn.com/us/media/71a069abbbe4a1df9e7801a60341d402-2480-3508.jpg)). Ownership: Alibaba took control in 2016 and went to 83% in 2017 ([TechCrunch](https://techcrunch.com/2017/06/28/alibaba-ups-its-stake-in-southeast-asias-lazada-with-1-billion-investment/), not opened); **current % stake not found**.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Singapore (holdco) | Lazada South East Asia Pte. Ltd. | Not found | [Alibaba FY2026 AR](https://www.sec.gov/Archives/edgar/data/1577552/000119312526274928/d133513dex991.pdf) |
| Singapore | Lazada Singapore Pte. Ltd. | UEN 201403859E | [Seller ToS](https://img-ovs.alicdn.com/other/common/a0a2f2a477de4333a2ac295e94439b3f); [Alipay agreement](https://img-ovs.alicdn.com/other/common/8423899fc94b48b9a3f5224c66cf6bfa) |
| Philippines | Lazada E-Services Philippines, Inc. | SEC CS201203115 | [lazada.com.ph/terms-of-use](https://www.lazada.com.ph/terms-of-use/) |
| Indonesia | PT Ecart Webportal Indonesia | Not found | [lazada.co.id/terms-of-use](https://www.lazada.co.id/terms-of-use/) |
| Vietnam | Recess Company Limited | Tax code 0308808576 | [VN Seller ToS](https://img-ovs.alicdn.com/other/common/fc2d4006a81b4f208ccc28e2b95a6606) |
| Malaysia | Ecart Services Malaysia Sdn Bhd | Not found | [Affiliate T&C, Jan 2022](https://terms.alicdn.com/legal-agreement/terms/suit_bu1_other/suit_bu1_other201808302016_83016.html) — medium confidence |
| Thailand | Lazada Limited (บริษัท ลาซาด้า จำกัด) | Not found | [Brand Inside](https://brandinside.asia/?p=93808); [UnionPay promo](https://www.unionpayintl.com/cardholderServ/serviceCenter/merchant/916921044462?type=1) — low confidence |

**Payment counterparties (not Lazada entities):** Alipay Singapore Investment Holding Pte. Ltd., Alipay Singapore E-Commerce Private Limited, Alipay Merchant Services Pte. Ltd. (SG); Alipay Philippines Inc. (PH); AIMY Merchant Services Sdn Bhd (MY); PT Espay Debit Indonesia Koe (ID, DANA).

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| Thailand | Yes (#1) | ⚠️ Yes, low-confidence source | Not researched — entity present | Low |
| Philippines | Yes (#2) | ✅ Yes | N/A — entity present | Low |
| Indonesia | Yes (#3) | ✅ Yes | N/A — entity present | Low |
| Vietnam | Yes (#4) | ✅ Yes | N/A — entity present | Low |
| Malaysia | Yes (#5) | ⚠️ Yes, 2022 source | N/A — entity present | Low |
| Singapore | Yes (#6) | ✅ Yes | N/A | Low |
| United States | Yes (#7, 1.5%) | No | Not relevant — no evidence of US-card buying volume | Negligible |
| China | Yes (#8, 1.3%) | No | Not relevant | Negligible |

**No cross-border warning applies.** Every material market has a local operating entity.

> **MANUAL:** The TH, MY, SG and VN consumer T&Cs are JS-rendered and were not read. Open lazada.co.th/terms-of-use in a browser to confirm the Thai entity and any named payment operator for the Thai Lazada Wallet.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| SG | **Alipay Singapore Investment Holding Pte. Ltd. + affiliates (Alipay Merchant Services Pte. Ltd., Alipay Singapore E-Commerce Pte. Ltd.)**. Cl. 3.1(a): *"the merchant acquisition services including the payment, settlement, processing and other related services to be provided by Alipay and its affiliates"*. Cl. 3.7: the buyer *"authorizes Alipay or its affiliates to charge that card"*. Client money safeguarded at *"a licensed bank in Singapore"* (unnamed). | [Terms/Privacy Policy] | https://img-ovs.alicdn.com/other/common/8423899fc94b48b9a3f5224c66cf6bfa (v1.0 Jun 2021; v3.0 14 Nov 2022) |
| SG | Same Alipay entities — money transfer services for buyers and individual sellers | [Terms/Privacy Policy] | https://img-ovs.alicdn.com/other/common/57f887c7e1e94a16a4d0377d3d4ae0c9 |
| TH | **2C2P** (Ant-owned) — *"a single-point integration with more than 20 payment channels"* incl. wallets, online/mobile banking, card instalments; Lazada needed a *"single point of fund settlement and reporting"* | [Provider Case Study] | https://2c2p.com/case-studies/lazada/ (Nov 2023) |
| TH | 2C2P — digital goods (utilities, mobile top-up; 1M+ top-up transactions in 2020) | [Provider Case Study] (third-party mirror) | https://www.casestudies.com/company/2c2p/case-study/lazada-drives-1-million-mobile-top-up-transactions-with-2c2p |
| TH | Krungsri — bank-linked Lazada Wallet top-up | [Press Release] — search result only, not opened | https://www.krungsri.com/bank/en-US/NewsandActivities/Krungsri-Banking-News/krungsri-top-up-service-lazada-wallet.html |
| PH | **Alipay Philippines Inc.** — operates the Lazada E-Wallet; BSP-regulated | [Terms/Privacy Policy] | https://www.lazada.com.ph/terms-of-use/ |
| PH | CIMB Bank PH — LazPayLater credit line | [Third-Party Report] (bank FAQ) | https://www.cimbbank.com.ph/en/help-and-support/faqs/my-loan/lazada-paylater-by-cimb/how-can-i-use-lazada-paylater.html |
| MY | **AIMY Merchant Services Sdn Bhd** (formerly Alipay Malaysia) — BNM-listed e-money issuer (white-labelling provider) for *"Lazada Wallet"* and a Registered Merchant Acquirer (Non-bank). **No document says AIMY acquires Lazada MY cards.** | [Terms/Privacy Policy] (regulator register) | https://www.bnm.gov.my/en/-/alipay-malaysia-sdn-bhd |
| MY | Atome + "Lazada Payfin" — LazPayLater buyer repayment | [Third-Party Report] | https://www.bigseller.pro/blog/articleDetails/4202/lazada-paylater-2026.htm |
| ID | Alipay — named in the Lazada Payment Protection Policy (*"sistem apa pun (termasuk Lazada dan Alipay)"*); page loads an Alipay device-fingerprint script | [Terms/Privacy Policy] / [Source Code] | https://www.lazada.co.id/terms-of-use/ |
| ID | **DANA / PT Espay Debit Indonesia Koe** — Lazada Credit balance; QRIS on delivery | [Terms/Privacy Policy]; [Press Release] | https://www.lazada.co.id/terms-of-use/ ; https://www.lazada.co.id/blog/kolaborasi-lazada-dan-dana-hadirkan-pembayaran-di-tempat-dengan-qris-mudahkan-transaksi-pelanggan/ |
| VN | Vietcombank — cross-border merchant payouts (2017) | [Third-Party Report] | https://vietnamnews.vn/bizhub/419124/lazada-inks-agreement-with-vietcombank.html |
| Seller side | WorldFirst (Ant-owned) — cross-border seller collection accounts | [Provider Case Study] | https://worldfirst.com/sg/solution/marketplaces/lazada |

**History (primary press):** Lazada built helloPay in 2014; Ant Financial absorbed it in April 2017 and rebranded it Alipay Singapore/Malaysia/Indonesia/Philippines ([CNBC](https://www.cnbc.com/2017/04/18/alibabas-ant-financial-merges-with-payment-platform-making-alipay-for-singapore-and-more.html); [TechCrunch](https://techcrunch.com/2017/04/19/ant-financial-hellopay)). In Jan 2018 Lazada Indonesia said it was *"migrating from Lazada's technology to Alibaba's"* for its payment gateway ([Jakarta Post](https://www.thejakartapost.com/news/2018/01/17/lazada-to-implement-e-payment-gateway-system-this-year)). **Lazada's payments arm was folded into Ant — that is the origin of today's captive stack.**

**Negative results:** Lazada + Adyen, Stripe, Checkout.com, Cybersource, Worldpay, Xendit, Midtrans, Doku, iPay88 → nothing linking them to Lazada. An undated article in The Ken lists Lazada as a Xendit client `[UNVERIFIED — search summary only]` ([The Ken](https://the-ken.com/sea/story/neutral-payment-gateway-to-soonicorn-the-stakes-keep-rising-for-xendit/)).

**Not found:** the card acquirer in TH, ID, VN or MY.

#### 3B. Payment Orchestrator

**Classification: In-house orchestration layer — captive group infrastructure (Ant/Alipay).** Evidence type: [Terms/Privacy Policy] + [Job Listing].

- Alipay is acquirer, processor, settlement agent and card vault in SG, by contract.
- Alipay/Ant entities hold the wallet licences in PH and MY.
- 2C2P (Ant) sits underneath in TH as a single-settlement aggregator.
- Payments finance works *"closely with Ant International payment stakeholders"* on *"payment channel P&L"* and *"billing with payment partners"* ([job ad, Sep 2026](https://jobs.menlovc.com/companies/luca-2/jobs/95280802-regional-finance-manager-payments-marketing-solutions)).
- The TAL's "In-house Routing" is directionally right. **More precise: "captive Ant/Alipay acquiring + local aggregators".**
- **Caveat:** no engineering blog, talk or job post describes multi-acquirer routing logic. Whether Lazada routes *between* providers at all, or simply hands everything to Ant, is unknown.
- Orchestrator searches (Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno, "payment orchestration") → **all negative.**

> *Confirmed orchestration-aware, through its affiliate. The opening is not the case for orchestration — Ant already does that job. It is cost and coverage that the captive layer does not reach, and it has to be argued with Ant's relationship to Yuno in mind.*

> **MANUAL:** Walk through app checkout in TH and ID with a proxy. Look for Antom/Alipay+, 2C2P and any non-Ant gateway endpoints on the card step.

---

### Section 4: Alternative & Local Payment Methods

Sources: live homepage footers fetched 2026-10-19 (logo alt text — a curated strip, not the full checkout list); Lazada help-centre AI summaries rendered 2026-10-19 (PH, MY only); press. **"Not found" means not found — never "confirmed absent".**

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| **TH** | COD | Cash/voucher | Active in checkout (footer) | https://www.lazada.co.th/ |
| TH | Visa / Mastercard / JCB / UnionPay | Cards | Active in checkout (footer) | https://www.lazada.co.th/ |
| TH | TrueMoney Wallet | Digital wallet | Mentioned in docs (Lazada promo page) | https://pages.lazada.co.th/wow/i/th/THCampaign/true-money-wallet-promotion?hybrid=1 |
| TH | 20+ channels incl. wallets, online/mobile banking, card instalments via 2C2P | Mixed | Mentioned in press (case study, 2023) | https://2c2p.com/case-studies/lazada/ |
| TH | PromptPay / Thai QR | Bank transfer / A2A | **Not found** by name | — |
| TH | Counter Service / 7-Eleven cash | Cash/voucher | Not found | — |
| TH | Lazada Wallet | Digital wallet | Mentioned in press (2018 launch) | https://www.nationthailand.com/in-focus/30337600 |
| **PH** | Lazada Wallet (Alipay PH) | Digital wallet | Active in checkout (footer + help centre) | https://www.lazada.com.ph/ |
| PH | GCash | Digital wallet | Active in checkout (footer + help centre) | https://www.lazada.com.ph/ |
| PH | Maya | Digital wallet | Active in checkout (footer + help centre) | https://www.lazada.com.ph/ |
| PH | Visa / MC / JCB / Amex / UnionPay | Cards | Active in checkout (footer) | https://www.lazada.com.ph/ |
| PH | COD | Cash/voucher | Mentioned in docs (help-centre summary) | helpcenter.lazada.com.ph (rendered) |
| PH | Instalments incl. BDO; "non-credit card holder instalment plans" | BNPL/Instalments | Mentioned in docs (help-centre summary) | helpcenter.lazada.com.ph (rendered) |
| PH | LazPayLater (CIMB) | BNPL/Instalments | Mentioned in docs (CIMB FAQ) | https://www.cimbbank.com.ph/en/help-and-support/faqs/my-loan/lazada-paylater-by-cimb/how-can-i-use-lazada-paylater.html |
| PH | InstaPay / online banking | Bank transfer / A2A | Not found | — |
| PH | 7-Eleven / OTC (Bayad, Dragonpay) | Cash/voucher | Not found | — |
| **ID** | Visa / MC / UnionPay | Cards | Active in checkout (footer) | https://www.lazada.co.id/ |
| ID | COD ("bayar di tempat") | Cash/voucher | Active in checkout (footer) | https://www.lazada.co.id/ |
| ID | QRIS on Delivery via DANA | Digital wallet / QR | Mentioned in press (Lazada blog, May 2023) | https://www.lazada.co.id/blog/kolaborasi-lazada-dan-dana-hadirkan-pembayaran-di-tempat-dengan-qris-mudahkan-transaksi-pelanggan/ |
| ID | Lazada Credit (DANA balance) | Digital wallet | Mentioned in docs (T&C) | https://www.lazada.co.id/terms-of-use/ |
| ID | 0% instalments ("Cicilan 0%") | BNPL/Instalments | Mentioned in docs (homepage banner) | https://www.lazada.co.id/ |
| ID | Virtual account / bank transfer | Bank transfer / A2A | **Not found** | — |
| ID | QRIS at online checkout | Bank transfer / A2A | **Not found** | — |
| ID | GoPay, OVO | Digital wallet | Not found | — |
| ID | Alfamart / Indomaret | Cash/voucher | Not found | — |
| ID | Kredivo / Akulaku | BNPL | Not found (search summary of a YouTube video only) | — |
| **VN** | Visa / MC / JCB | Cards | Active in checkout (footer) | https://www.lazada.vn/ |
| VN | NAPAS domestic cards | Cards | Active in checkout (footer) | https://www.lazada.vn/ |
| VN | MoMo | Digital wallet | Active in checkout (footer); MoMo's own page | https://www.momo.vn/thanh-toan-momo-lazada |
| VN | ZaloPay | Digital wallet | Active in checkout (footer) | https://www.lazada.vn/ |
| VN | Credit-card instalments | BNPL/Instalments | Active in checkout (footer) | https://www.lazada.vn/ ; https://www.momo.vn/blog/tra-gop-tren-lazada-c116dt2760 (Aug 2026) |
| VN | COD | Cash/voucher | Active in checkout (footer) | https://www.lazada.vn/ |
| VN | VietQR / VNPay | Bank transfer / A2A | Not found | — |
| **MY** | Lazada Wallet (AIMY licence) | Digital wallet | Active in checkout (homepage + help centre) | https://www.lazada.com.my/ |
| MY | Visa / Amex / UnionPay (no Mastercard logo in footer) | Cards | Active in checkout (footer) | https://www.lazada.com.my/ |
| MY | Online banking — 8 banks (Maybank, CIMB, Public Bank, RHB, Hong Leong, AmBank, Alliance, Bank Islam) | Bank transfer / A2A | Active in checkout (footer logos + help centre). FPX not named | https://www.lazada.com.my/ |
| MY | Touch 'n Go eWallet | Digital wallet | Active in checkout (footer + help centre) | https://www.lazada.com.my/ |
| MY | 7-Eleven, 99 Speedmart | Cash/voucher | Active in checkout (footer) | https://www.lazada.com.my/ |
| MY | Maybank instalments | BNPL/Instalments | Mentioned in docs (help centre) | helpcenter.lazada.com.my (rendered) |
| MY | LazPayLater (Atome + Lazada Payfin) | BNPL/Instalments | Mentioned in press (Jan 2026) | https://www.bigseller.pro/blog/articleDetails/4202/lazada-paylater-2026.htm |
| MY | COD | Cash/voucher | Mentioned in docs (help-centre summary). A 2019 report said COD would be phased out | helpcenter.lazada.com.my; https://says.com/my/tech/lazada-will-soon-remove-cash-on-delivery-as-a-payment-option-for-buyers |
| MY | DuitNow (online checkout) | Bank transfer / A2A | Not found (DuitNow QR at the door, 2021, search summary only) | — |
| MY | Boost | Digital wallet | Mentioned in press (2022), not in the 2026 footer | https://wise.com/my/blog/lazada-payment-options |
| **SG** | Debit/credit card, **DBS PayLah!**, **Lazada Wallet** | Cards / Digital wallet | Mentioned in docs — footer copy: *"You can pay through debit/credit card, DBS PayLah! or Lazada Wallet"* | https://www.lazada.sg/ |
| SG | Visa / MC / Amex / UnionPay | Cards | Active in checkout (footer logos) | https://www.lazada.sg/ |
| SG | PayNow | Bank transfer / A2A | Not found. Appears only in the contaminated SG help-centre AI summary — not usable | — |
| SG | GrabPay wallet, Atome, Apple Pay, Google Pay | Wallet / BNPL | Not found | — |

**Removals:** none found. GCash is live in the PH footer. MY COD was reported for phase-out in 2019 but is listed in the current help-centre summary.

**Rail-gap warnings — NOT issued.** The rule requires a source for the absence. PromptPay (TH), virtual accounts and QRIS (ID) and InstaPay (PH) are all **not found**, but the help centres were only partly readable and the app checkout was not tested. Thailand's 2C2P integration covers *"20+ channels"* that very probably include PromptPay. **Do not use "you don't support X" in outreach for any of these.**

> **MANUAL:** Screenshot the app checkout in TH and ID. That one step would settle the two biggest gaps in this report.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Slow refunds; refunds credited to Lazada Wallet instead of the original method | Trustpilot (SG, PH) | Moderate (recurring theme) | 2020 – Feb 2026 | https://uk.trustpilot.com/review/lazada.sg ; https://ca.trustpilot.com/review/lazada.com.ph `[UNVERIFIED — search summary only; page behind a WAF challenge]` |
| Declined transactions — card payment shown "unsuccessful" but funds held; Lazada says the bank holds them 5–45 days | PissedConsumer (PH) | Isolated | Jun–Dec 2020 | https://www.pissedconsumer.com/people/2830298.html |
| Unauthorised transactions — dedicated "Unauthorized Transaction" form; scam reports 46 (2022) → 25 (2023) | MHA Singapore | Declining | Page updated 30 Jan 2026 | https://mha.gov.sg/e-commerce-marketplace-transaction-safety-ratings/lazada |
| Checkout errors — Lazada Wallet top-ups failing on 11.11 | RinggitPlus (MY) | Peak-event incident | Nov 2018 | https://ringgitplus.com/en/blog/Online-Shopping/Singles-Day-2018-In-Malaysia-Crippled-By-Payment-Gateway-Issues-On-Lazada-Shopee-And-11street.html `[UNVERIFIED — search summary only]` |
| Unauthorised card charges after account compromise | ABS-CBN (PH) | Isolated | Jan 2019 | https://www.abs-cbn.com/trending/01/11/19/woman-incurs-p200k-credit-card-debt-in-alleged-hacking-bpi-lazada-react `[UNVERIFIED — search summary only]` |

No Reddit threads surfaced. App-store payment reviews were not retrieved.

*Pattern:* complaints are about refunds and fraud, not approval rates. The 2018 11.11 wallet failure is the only routing-relevant incident and is eight years old. **No current complaint pattern supports an orchestration pitch.**

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 30 Sep 2026 (posted; now closed) | Regional Finance Manager, Payments & Marketing Solutions — owns *"Lazada's payment ecosystem"*: channel P&L, *"payment cost optimisation"*, payment-partner incentive economics, reconciliation, chargeback-loss escalation; works with *"Ant International payment stakeholders"* | Payment Infrastructure Hiring | https://jobs.menlovc.com/companies/luca-2/jobs/95280802-regional-finance-manager-payments-marketing-solutions |
| 2 | 18 Aug 2026 | Alibaba merges AIDC, China e-commerce and Freshippo into one "Alibaba E-commerce Group". International e-commerce revenue down 1% YoY; Lazada not mentioned | M&A / restructuring | https://www.sec.gov/Archives/edgar/data/1577552/000110465926099220/tm2623667d1_ex99-1.htm |
| 3 | 23 Jun 2026 | ~5% workforce cut across all six markets after a role review | Leadership / restructuring | https://vulcanpost.com/911933/lazada-southeast-asia-singapore-layoffs-2026/ ; https://www.humanresourcesonline.net/lazada-to-undertake-workforce-reduction-across-southeast-asia-amid-organisational-review |
| 4 | Jun 2026 (FY to 31 Mar 2026) | Alibaba FY2026: international retail growth *"partly offset by … a 3% decline from Lazada"*; AIDC adjusted EBITA loss narrowed to RMB2.05bn from RMB15.14bn | Financial | https://www.sec.gov/Archives/edgar/data/1577552/000119312526274928/d133513dex991.pdf |
| 5 | 1 Jan 2026 | LazPayLater MY seller fee raised to 4.5% + SST (4.86%); auto-enabled for sellers | Payment strategy | https://www.bigseller.pro/blog/articleDetails/4202/lazada-paylater-2026.htm |

Older context: first positive monthly EBITDA in July 2024 ([TechNode](https://technode.com/2024/08/14/alibabas-lazada-makes-first-ebitda-profit-in-july-commits-more-investment/)); US$230M Alibaba injection in May 2024 ([Zetpy](https://www.zetpy.com/2024/05/21/lazada-gets-another-usd-230-million-capital-injection-from-alibaba/)); ~US$7.7bn total Alibaba investment ([KrASIA](https://kr-asia.com/alibabas-lazada-achieves-first-profit-despite-tiktok-shops-2023-market-surge)). Undated, closed: VP Payment and Monetization Strategy, Jakarta, six-market remit ([Dealls](https://dealls.com/en/loker/vp-payment-and-monetization-strategy~lazada)).

**No public payment-related RFP found.** No licence applications found. No job post mentions PSP evaluation, migration or orchestration.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | Jan 2026 | LazPayLater MY seller fee raised to 4.86% all-in | BNPL monetisation — payments run as a revenue line | https://www.bigseller.pro/blog/articleDetails/4202/lazada-paylater-2026.htm |
| 2 | Current | BNM register: AIMY (ex-Alipay Malaysia) is the e-money issuer behind Lazada Wallet MY and a registered merchant acquirer | Confirms Ant licence dependency in MY | https://www.bnm.gov.my/en/-/alipay-malaysia-sdn-bhd |
| 3 | Nov 2023 | 2C2P case study: single integration for 20+ Thai payment channels, single settlement point | Thai LPM stack | https://2c2p.com/case-studies/lazada/ |
| 4 | May 2023 | QRIS on Delivery with DANA (Indonesia) | QRIS used at the door, not confirmed at online checkout | https://www.lazada.co.id/blog/kolaborasi-lazada-dan-dana-hadirkan-pembayaran-di-tempat-dengan-qris-mudahkan-transaksi-pelanggan/ |
| 5 | May 2023 | LazPayLater MY adds 1.5% fee to all plans | BNPL monetisation | https://ringgitplus.com/en/blog/online-shopping/lazada-imposes-1-5-service-fee-on-lazpaylater-one-month-bnpl-payment-plan.html |

No provider removals found. No 2025–26 coverage in The Paypers, Finextra, Tech in Asia or e27.

---

### Section 8: Checkout Experience Audit

*Full checkout flow not accessible (login required; app-first). Findings limited to publicly observable elements.*

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | Custom-built marketplace checkout; payment modules on Lazada paths (`/lazpay-page-module/`, `/ewallet-h5/`, `/paylater/`) with Alipay device-fingerprint scripts | N/A | From page source; internal module names only |
| Guest checkout | No guest-checkout text found; login/sign-up header | Not verified | |
| Steps to complete payment | Not observable | — | |
| Card input experience | Saved cards stored by Alipay (SG agreement cl. 3.8); PCI scope note says only truncated PANs are stored locally | N/A | See Section 9 |
| Payment methods visible | Per-market footer strips (Section 4) | Fair | Footers differ by market — localised |
| Location-based method display | Yes, by country domain | Good | Separate domain per market |
| Instalment / EMI options | VN card instalments; MY Maybank; PH BDO + non-card-holder plans; ID 0% banner; TH via 2C2P | Good | Present in every market checked |
| 3DS implementation | Not detected | — | |
| PCI indicator | PCI DSS badge in every footer, linking to an attestation that **expired 29 Sep 2025** | Fair | See Section 9 |
| Mobile responsiveness | Not tested | — | App-first; mobile web 56–70% of web visits on five domains |
| Multi-currency / local pricing | Local currency per domain | Good | |
| Saved payment methods | Yes, via Alipay vault (SG) | N/A | |
| Error message clarity | Help centre has "Transaction Declined Due to Payment Method Error" article | Not verified | |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **Attestation of Compliance for PCI QSA Assessment, PCI DSS v4.0**, issued to **Lazada South East Asia Pte Ltd (Lazada Group)** by atsec (Beijing). No. atsec-2024-PCI-DSS-C-011476-02252. Initial compliance 30 Sep 2019; issued 30 Sep 2024; **expired 29 Sep 2025**. The level is not stated. **The certificate linked from the live footer today is a year out of date** — a renewal may exist and simply not be linked. | https://img.lazcdn.com/us/media/71a069abbbe4a1df9e7801a60341d402-2480-3508.jpg (linked from the lazada.sg footer, fetched 2026-10-19) |
| Card data handling | AoC scope: *"Only truncated PANs are stored in the local database servers to simplify the cardholder's future payment process … Sensitive authentication data are neither transmitted nor stored."* The SG agreement says saved card details are *"stored by Alipay or its affiliates on behalf of the Platform Operators"*. The two are consistent: **Lazada holds truncated PANs; Alipay holds the vault.** | AoC above; https://img-ovs.alicdn.com/other/common/8423899fc94b48b9a3f5224c66cf6bfa |
| Recommended Yuno integration | **Back-to-back API** `[INFERENCE, not confirmed]` — Lazada has its own QSA-assessed environment and custom checkout modules, so an SDK swap of the checkout is unlikely. **Token migration out of Alipay's vault is the critical-path item.** | — |

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: The acquirer is Ant, and Ant is a Yuno customer. Settle that before anything else.**
> **Evidence:** S3A — Alipay entities are the SG acquirer, processor and card vault ([agreement](https://img-ovs.alicdn.com/other/common/8423899fc94b48b9a3f5224c66cf6bfa)), the PH wallet operator and the MY wallet licence-holder; 2C2P (Ant) aggregates Thailand. S6 — payments finance works *"closely with Ant International payment stakeholders"* (Sep 2026). Phase 0 — "antgroup" is on y.uno's site-wide customer list.
> **Pain Point:** None for Lazada yet. This is Yuno's problem: a routing pitch that pulls volume away from Antom/2C2P could cut across an existing Yuno customer.
> **Yuno Value Proposition:** Depends on what Ant uses Yuno for. If Ant is a Yuno connector/partner, Yuno may be able to sit *with* Ant at Lazada rather than against it.
> **Best Success Case:** None — internal question.
> **Outreach Angle:** Do not send. Ask your manager / Partnerships first: "Ant Group is on our logo wall. Lazada's acquiring is Alipay/2C2P. Are we cleared to pitch Lazada, and is there a warm path through Ant?"
> **Suggested Subject Line:** N/A — internal

> **Insight #2: Payments is now a cost line under active optimisation.**
> **Evidence:** S6 — Sept 2026 job ad: *"payment channel P&L"*, *"payment cost optimisation"*, *"incentive economics for payment partners"*, *"billing with payment partners"*. S6/S12 — Lazada revenue declined 3% in Alibaba's FY2026; ~5% layoffs in June 2026. S7 — LazPayLater MY fee raised to 4.86% in Jan 2026.
> **Pain Point:** A shrinking top line puts pressure on the cost of acceptance. With most volume going through one affiliated provider, Lazada has little leverage to benchmark or negotiate MDR. `[INFERENCE, not confirmed]`
> **Yuno Value Proposition:** A second processing path per market creates real price competition and lets Lazada measure the cost of its current stack. Pitch it as a benchmark, not a replacement.
> **Best Success Case:** Rappi — same marketplace pattern, many local methods, less operational work. Tier 2 (LATAM results).
> **Outreach Angle:** "Saw Lazada is hiring someone to own payment channel P&L and cost optimisation across six markets. Is there a second route in each market today, or is the benchmark only internal?"
> **Suggested Subject Line:** Payment channel P&L across six markets

> **Insight #3: Each market has a different stack under one captive umbrella.**
> **Evidence:** S1 — six domestic businesses, TH 34% / PH 18% / ID 15% / VN 11% / MY 8% / SG 7%. S3A — SG on Alipay acquiring, TH on 2C2P aggregation, ID on DANA, PH on Alipay PH + CIMB, MY on AIMY + Atome. S4 — method sets differ widely by market.
> **Pain Point:** Six different method-and-settlement setups, reconciled by one regional finance team (the Sep 2026 job lists reconciliation and partner billing). `[INFERENCE, not confirmed]` that this is painful — Lazada built it deliberately.
> **Yuno Value Proposition:** One integration and one reconciliation view across the six markets' providers.
> **Best Success Case:** Rappi (multi-country marketplace).
> **Outreach Angle:** Use only after Insight #1 is cleared. Lead on reconciliation and reporting across six markets, not on routing.
> **Suggested Subject Line:** Six markets, one reconciliation view

> **Insight #4: The direct competitor next door just bought an orchestration layer.**
> **Evidence:** S11C — Zalora runs BridgerPay as a *"single orchestration layer"* across SEA and says it doubled its payment methods (Nov 2025, [BridgerPay](https://bridgerpay.com/learn/bridger-stories/Jyg0jmdNvp2xUmIJedJ4)). S3B — Lazada has no third-party orchestration layer.
> **Pain Point:** Weak. Zalora is a fashion vertical player, far smaller; Shopee and TikTok Shop — Lazada's real rivals — run in-house payment stacks.
> **Yuno Value Proposition:** Proof that SEA e-commerce is adopting neutral orchestration.
> **Best Success Case:** Rappi.
> **Outreach Angle:** Supporting evidence only. Do not open with it. Never name the competitor or its vendor in outreach.
> **Suggested Subject Line:** N/A — supporting point

---

### Quick Hits: Ready-to-Use Sales Ammunition

**⚠️ Hold all of these until Insight #1 is cleared internally.**

**Email hooks:**
1. "Your payments finance role posted in September owns channel P&L and cost optimisation across six markets — what's the benchmark for whether a market's acceptance cost is right?"
2. "Thailand is a third of Lazada's web traffic and runs 20+ channels through one aggregator — is there a second path if that one degrades on 11.11?"
3. "Six markets, six different method-and-settlement setups — how many reconciliation views does the regional finance team work from today?"

**Cold call openers:**
1. "I saw the regional payments finance role — is cost of acceptance a live project right now?"
2. "Quick one: when Lazada wants to benchmark its payment costs, what does it compare against?"
3. "I work with marketplaces running many local methods per country — how does your team handle reconciliation across all six?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| Shopee (Sea Ltd) | shopee.com | Singapore | FY2025 GMV US$127.4bn `[UNVERIFIED — search summary only]` | All six + TW, BR | In-house (ShopeePay / Monee) | https://www.businesswire.com/news/home/20260302039769/en/sea-limited-reports-fourth-quarter-and-full-year-2025-results/ |
| TikTok Shop / Tokopedia | shop.tiktok.com / tokopedia.com | Singapore / Jakarta | Not found | ID, MY, TH, VN, PH, SG | Tokopedia backend; GoPay/GoPay Later; TikTok Pay in VN/MY/TH `[UNVERIFIED]` | https://martechvibe.com/article/goto-and-tiktok-indonesia-to-migrate-ecommerce-tech-stack |
| Zalora | zalora.com | Singapore | Not found | SG, MY, ID, PH, HK, TW | **BridgerPay orchestration**; Adyen since 2016 `[UNVERIFIED]` | https://bridgerpay.com/learn/bridger-stories/Jyg0jmdNvp2xUmIJedJ4 |
| Temu (PDD) | temu.com | Not verified | Global | PH, MY, TH + ANZ | **Adyen** (US, CA, EU, Oceania, South Asia) | https://www.adyen.com/press-and-media/temu-expands-partnership-with-adyen-as-it-launches-across-more-markets |
| Blibli | blibli.com | Indonesia | Not found | ID | Not found | — |
| Tiki | tiki.vn | Vietnam | Not found | VN | Not found | — |

#### 11B. Industry Peers

Firmographics not separately sourced this run.

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Coupang | coupang.com | Marketplace | KR, TW | In-house pay arm (Coupang Pay / Rocket Pay) | https://en.bloomingbit.io/feed/news/115961 `[UNVERIFIED]` |
| Rakuten | rakuten.co.jp | Marketplace | JP | In-house (Rakuten Card / Pay) | TAL |
| Mercari | mercari.com | C2C marketplace | JP | In-house (Merpay) | TAL |
| Flipkart | flipkart.com | Marketplace | IN | Juspay | https://www.merchantpaymentsecosystem.com/company/juspay/ `[UNVERIFIED]` |
| Qoo10 | qoo10.sg | Marketplace | SG, JP | Not found | TAL |
| Carousell | carousell.com | C2C marketplace | SG, MY, PH, HK, TW | Not found | TAL |
| Shein | shein.com | Cross-border e-commerce | Global | TAL says Juspay — **no source found** | TAL |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| Zalora | BridgerPay | Case study 18 Nov 2025 | Fashion e-commerce, SEA | https://bridgerpay.com/learn/bridger-stories/Jyg0jmdNvp2xUmIJedJ4 |
| Arrow | Spreedly | Not found | SEA headless checkout (vendor, not a merchant) | https://www.spreedly.com/customers/arrow `[UNVERIFIED]` |

#### 11D. Prospect Scoring (verified signals only; quick pass)

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| Zalora — Orchestration status | +1 | ✅ Global orchestrator incumbent (BridgerPay) | BridgerPay case study |
| Zalora — 3+ countries | +3 | ⬜ Six markets claimed, not traffic-verified | — |
| Temu — Multiple PSPs | 0 | ⬜ Only Adyen confirmed | Adyen press release |
| Temu — Orchestration status | 0 | ⬜ TAL says in-house; not verified | — |
| Blibli / Tiki | — | ⬜ No payment data found | — |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Zalora | Competitor | SEA, HK, TW | Not fully scored | 🟢 Watch | Already on BridgerPay — competitive account | Yes (orchestrator column blank — **should read BridgerPay**) |
| 2 | Temu | Competitor | Global incl. SEA | Not fully scored | 🟢 | Adyen confirmed; TAL "In-house Routing" conflicts with this | Yes |
| 3 | Blibli | Competitor | ID | Not scored | ⬜ | No data | Yes |
| 4 | Tiki | Competitor | VN | Not scored | ⬜ | No data | Yes |
| 5 | Qoo10 | Peer | SG, JP | Not scored | ⬜ | No data; TAL HQ "South Korea" looks wrong | Yes |
| 6 | Carousell | Peer | SG, MY, PH, HK, TW | Not scored | ⬜ | No data; TAL HQ "Malaysia" looks wrong | Yes |
| 7 | Shopee | Competitor | SEA | — | 🔴 | In-house wallet + financial arm | Yes |
| 8 | Tokopedia / GoTo | Competitor | ID | — | 🔴 | In-house (GoPay / Midtrans) | Yes |
| 9 | Coupang | Peer | KR, TW | — | 🔴 | In-house pay arm | Yes |
| 10 | Amazon SG | Competitor | SG | — | ⬜ | Not researched | **No** |

**TAL data fixes surfaced** (not verified beyond the sources above): Zalora orchestrator → BridgerPay; Temu "In-house Routing" contradicted by Adyen; Meesho/Shein "Juspay" unsourced.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | Not disclosed. Alibaba reports only that Lazada revenue declined (FY2026: *"a 3% decline from Lazada"*) | https://www.sec.gov/Archives/edgar/data/1577552/000119312526274928/d133513dex991.pdf |
| GMV / Gross Transaction Volume | Not disclosed. 2030 target of US$100bn GMV (KrASIA, Aug 2024). TAL "~$5B est." is unsourced | https://kr-asia.com/alibabas-lazada-achieves-first-profit-despite-tiktok-shops-2023-market-surge |
| Average Transaction Value (USD) | Not found. 11.11 2025: AOV +123% vs normal days (relative only) | https://lazada-com.oss-ap-southeast-1.aliyuncs.com/229-press-release.pdf |
| Est. Annual Transactions | Cannot be calculated — no revenue/GMV or ATV | — |
| **Monthly transaction count** | **⚠️ NOT FOUND — ASSUMED ≥100,000/month (very likely orders of magnitude above). [ASSUMPTION — not researched.]** Basis: ~68.9M monthly web visits excluding the app; six national marketplaces; ~US$7.7bn cumulative Alibaba investment. Billing unit: marketplace buyer orders (one checkout can span several sellers). Not derived from web traffic, per the traffic file's caveat. | — |
| Active Customers / Users | Not found. 11.11 2025: 451,000 users in one LazzieChat promotion (not an MAU figure). 2030 target: 300M customers | Press release above; KrASIA |
| Primary Currency | THB, PHP, IDR, VND, MYR, SGD — one per market | Country domains |
| Top 3 Markets by Revenue | Not disclosed. By web traffic: TH, PH, ID. Thailand was the first market to turn profitable (2022) | https://technode.com/2024/08/14/alibabas-lazada-makes-first-ebitda-profit-in-july-commits-more-investment/ |
| Billing channel split (web vs app store) | N/A — physical-goods marketplace; app-store IAP not applicable. Web vs app ordering split not found | — |

*No public revenue/GMV data found. Business case sizing will require a discovery call.*

---

### Overall Research Confidence

**Medium.**
- **Strong:** legal entities (four of six from primary documents); the SG payments contract (read in full); wallet licensing in PH and MY (T&C and regulator register); PCI attestation (primary, read); corporate trajectory (Alibaba SEC filings).
- **Limited:** payment methods. Four of six T&Cs and all help-centre articles are JS-rendered. Help-centre AI summaries were usable for PH and MY only. No app checkout was walked. No card acquirer is confirmed outside Singapore.
- **Missing:** any absolute transaction, GMV or revenue figure.
- **Traffic was supplied** (Similarweb, 2026-10-19), web only, top-10 per domain. The country *mix* is reliable as a lower bound. It was **not** used to size volume.

---

### Manual Research Recommendations

> **Area:** Ant Group relationship (Insight #1)
> **Why it matters:** Lazada's acquirer is a Yuno customer's affiliate. Outreach without alignment risks a channel conflict.
> **Suggested manual action:** Ask your manager / Partnerships what Ant uses Yuno for, and whether there is a warm path.

> **Area:** Monthly transaction count
> **Why it matters:** It is the only gating signal, and it is assumed.
> **Suggested manual action:** Confirm in discovery. Realistically this will not reject the account — note it and move on.

> **Area:** App checkout in TH and ID (Section 4)
> **Why it matters:** PromptPay, virtual accounts and QRIS are the dominant rails in Lazada's #1 and #3 markets. Their absence would be the strongest hook; their presence would kill it.
> **Suggested manual action:** Screenshot the payment step in the Lazada app with a TH and an ID account (or ask a contact in-market).

> **Area:** Card acquirer outside Singapore
> **Why it matters:** It decides whether the captive-Ant picture holds in all six markets.
> **Suggested manual action:** Check the payment descriptor on a test purchase in TH or PH, or ask in discovery.

> **Area:** PCI attestation currency
> **Why it matters:** The linked AoC expired 29 Sep 2025. Probably a stale link, not a lapse — do **not** use it in outreach.
> **Suggested manual action:** None needed unless it comes up.

---

### Appendix: All Source URLs

**Traffic**
- `accounts/traffic/lazada.md` — Similarweb Sales Intelligence, supplied 2026-10-19

**Section 2 — Legal entities**
- https://www.sec.gov/Archives/edgar/data/1577552/000119312526274928/d133513dex991.pdf
- https://img-ovs.alicdn.com/other/common/a0a2f2a477de4333a2ac295e94439b3f
- https://img-ovs.alicdn.com/other/common/8423899fc94b48b9a3f5224c66cf6bfa
- https://acrawatch.sg/company/lazada-singapore-pte-ltd
- https://www.lazada.com.ph/terms-of-use/
- https://www.lazada.co.id/terms-of-use/
- https://img-ovs.alicdn.com/other/common/fc2d4006a81b4f208ccc28e2b95a6606
- https://img-ovs.alicdn.com/other/common/1d3ee98ed5614641bbc10159bce8332e
- https://terms.alicdn.com/legal-agreement/terms/suit_bu1_other/suit_bu1_other201808302016_83016.html
- https://brandinside.asia/?p=93808
- https://www.unionpayintl.com/cardholderServ/serviceCenter/merchant/916921044462?type=1
- https://techcrunch.com/2017/06/28/alibaba-ups-its-stake-in-southeast-asias-lazada-with-1-billion-investment/

**Section 3 — Payment stack**
- https://img-ovs.alicdn.com/other/common/57f887c7e1e94a16a4d0377d3d4ae0c9
- https://2c2p.com/case-studies/lazada/
- https://www.casestudies.com/company/2c2p/case-study/lazada-drives-1-million-mobile-top-up-transactions-with-2c2p
- https://www.krungsri.com/bank/en-US/NewsandActivities/Krungsri-Banking-News/krungsri-top-up-service-lazada-wallet.html
- https://www.bnm.gov.my/en/-/alipay-malaysia-sdn-bhd
- https://www.cimbbank.com.ph/en/help-and-support/faqs/my-loan/lazada-paylater-by-cimb/how-can-i-use-lazada-paylater.html
- https://vietnamnews.vn/bizhub/419124/lazada-inks-agreement-with-vietcombank.html
- https://worldfirst.com/sg/solution/marketplaces/lazada
- https://www.cnbc.com/2017/04/18/alibabas-ant-financial-merges-with-payment-platform-making-alipay-for-singapore-and-more.html
- https://techcrunch.com/2017/04/19/ant-financial-hellopay
- https://www.thejakartapost.com/news/2018/01/17/lazada-to-implement-e-payment-gateway-system-this-year
- https://the-ken.com/sea/story/neutral-payment-gateway-to-soonicorn-the-stakes-keep-rising-for-xendit/

**Section 4 — Payment methods**
- https://www.lazada.sg/ · https://www.lazada.co.id/ · https://www.lazada.com.my/ · https://www.lazada.co.th/ · https://www.lazada.vn/ · https://www.lazada.com.ph/
- https://helpcenter.lazada.com.ph/s/faq/knowledge?questionId=1000139669 (rendered)
- https://helpcenter.lazada.com.my/s/faq/knowledge?questionId=1000141822 (rendered)
- https://pages.lazada.co.th/wow/i/th/THCampaign/true-money-wallet-promotion?hybrid=1
- https://www.nationthailand.com/in-focus/30337600
- https://www.lazada.co.id/blog/kolaborasi-lazada-dan-dana-hadirkan-pembayaran-di-tempat-dengan-qris-mudahkan-transaksi-pelanggan/
- https://www.momo.vn/thanh-toan-momo-lazada
- https://www.momo.vn/blog/tra-gop-tren-lazada-c116dt2760
- https://wise.com/my/blog/lazada-payment-options
- https://says.com/my/tech/lazada-will-soon-remove-cash-on-delivery-as-a-payment-option-for-buyers
- https://www.bigseller.pro/blog/articleDetails/4202/lazada-paylater-2026.htm

**Section 5 — Complaints**
- https://uk.trustpilot.com/review/lazada.sg · https://ca.trustpilot.com/review/lazada.com.ph
- https://www.pissedconsumer.com/people/2830298.html
- https://mha.gov.sg/e-commerce-marketplace-transaction-safety-ratings/lazada
- https://ringgitplus.com/en/blog/Online-Shopping/Singles-Day-2018-In-Malaysia-Crippled-By-Payment-Gateway-Issues-On-Lazada-Shopee-And-11street.html
- https://www.abs-cbn.com/trending/01/11/19/woman-incurs-p200k-credit-card-debt-in-alleged-hacking-bpi-lazada-react

**Sections 6–7 — Corporate and payment news**
- https://jobs.menlovc.com/companies/luca-2/jobs/95280802-regional-finance-manager-payments-marketing-solutions
- https://dealls.com/en/loker/vp-payment-and-monetization-strategy~lazada
- https://www.sec.gov/Archives/edgar/data/1577552/000110465926099220/tm2623667d1_ex99-1.htm
- https://www.sec.gov/Archives/edgar/data/1577552/000110465926060224/tm2614494d1_ex99-1.htm
- https://www.sec.gov/Archives/edgar/data/1577552/000110465926032060/tm269353d1_ex99-1.htm
- https://vulcanpost.com/911933/lazada-southeast-asia-singapore-layoffs-2026/
- https://www.humanresourcesonline.net/lazada-to-undertake-workforce-reduction-across-southeast-asia-amid-organisational-review
- https://www.nst.com.my/amp/business/corporate/2026/06/1470818/lazada-cuts-jobs-50pct-amid-rising-competition-report
- https://technode.com/2024/08/14/alibabas-lazada-makes-first-ebitda-profit-in-july-commits-more-investment/
- https://www.zetpy.com/2024/05/21/lazada-gets-another-usd-230-million-capital-injection-from-alibaba/
- https://kr-asia.com/alibabas-lazada-achieves-first-profit-despite-tiktok-shops-2023-market-surge
- https://ringgitplus.com/en/blog/online-shopping/lazada-imposes-1-5-service-fee-on-lazpaylater-one-month-bnpl-payment-plan.html

**Sections 8–9 — Checkout and PCI**
- https://img.lazcdn.com/us/media/71a069abbbe4a1df9e7801a60341d402-2480-3508.jpg

**Section 11 — Competitors**
- https://bridgerpay.com/learn/bridger-stories/Jyg0jmdNvp2xUmIJedJ4
- https://www.adyen.com/press-and-media/temu-expands-partnership-with-adyen-as-it-launches-across-more-markets
- https://www.businesswire.com/news/home/20260302039769/en/sea-limited-reports-fourth-quarter-and-full-year-2025-results/
- https://martechvibe.com/article/goto-and-tiktok-indonesia-to-migrate-ecommerce-tech-stack
- https://en.bloomingbit.io/feed/news/115961
- https://www.merchantpaymentsecosystem.com/company/juspay/
- https://www.spreedly.com/customers/arrow

**Section 12 — Business case**
- https://lazada-com.oss-ap-southeast-1.aliyuncs.com/229-press-release.pdf

**Phase 0**
- https://y.uno/en (fetched 2026-10-19)

</details>
