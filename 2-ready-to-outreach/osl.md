# OSL Group (HKEX: 863)

**Status:** 🟡 Research complete: outreach not yet generated
**ICP Score:** 14 / 29 → 🟢 **Medium** (four signals score 0 because they were not researched, not because they failed. See the breakdown.)
**Industry:** Stablecoin payments and digital-asset trading (OSL Exchange, OSL Pay, Banxa, OSL BizPay) · **HQ:** Hong Kong (OSL Group Limited, HKEX: 863) · **Researched:** 2026-10-22 · **First email sent:** not yet
**Motion:** **Undetermined.** No orchestrator and no acquirer is named in any source reviewed. OSL runs two separate card and wallet on-ramp stacks (OSL Pay and Banxa) with no shared layer found.

**Full research doc (Google Doc):** [OSL x Yuno - Account Research](https://docs.google.com/document/d/1uXsLwixNpEHYJ_AmQ40pn0I3SLKus1u6TEF8K-ZR4l8/edit)

---

> ## 🎯 THE HOOK: OSL Pay publishes its own card approval rates, and they are low
>
> OSL Pay publishes "Card Approval Rate by Bank" pages for 20 currencies (updated 13 to 14 May 2026). On its **USD** table ([OSL Pay docs](https://docs.pay.osl.com/docs/creditdebit-card-success-rate-local-banks-in-us-usd)):
> - **30 to 50% ("lower success rate"):** ZA Bank, Bank of China (Hong Kong), Rakuten Bank, AmBank, Union Bank of the Philippines, Maya Philippines, HSBC Amanah Malaysia, BigPay Malaysia.
> - **Under 30% ("extremely low... not recommended"):** Standard Chartered Bank, Hong Leong Bank, PT Bank Mandiri, AEON Financial Service, Orient Corporation, Emirates NBD, Taiwan Cooperative Bank, Qatar National Bank.
> - The **best** tier is only "over 60%", and users are told to "carefully review this report before making any transactions". The user picks a card by hand instead of the platform routing around weak issuers.
>
> ⚠️ **Phrase it exactly.** These are on OSL Pay's **USD** table (cards paying in USD, issuers worldwide), not a Hong Kong or HKD table. There is no HKD page, and HKD is not in OSL Pay's 138-currency list. Hang Seng Bank is in the over 60% tier on the same page.
>
> ### And the cost line is moving the wrong way
> Fee and commission expenses rose from **HK$26.7M to HK$141.6M** year on year in H1 2026, "mainly due to the channel fees paid to payment gateway providers" ([Interim Report 2026](https://www.hkexnews.hk/listedco/listconews/sehk/2026/0924/2026092400430.pdf)).
>
> ### ⚠️ Read before drafting
> 1. **Revenue is gross.** H1 2026 revenue of HK$55.8B counts the full value of stablecoins OSL buys and sells. Revenue less cost of digital assets sold was only **HK$130.9M**, and loss from continuing operations was **HK$860.9M**. Never quote HK$55.8B as take.
> 2. **Crypto on-ramp is a high-risk MCC.** Before outreach, confirm which Yuno-connected acquirers will take crypto on-ramp volume in HK, the EU, Australia and Japan.
> 3. **Qualification check for Prateek:** parts of OSL are payment providers themselves (Banxa is an embedded on-ramp used by Kraken, Trust Wallet and KuCoin; OSL BizPay is B2B payments). The pitch here treats OSL as a merchant on its own ramps. Decide whether this is a merchant sale or a Partnerships conversation before running `/full-outreach`.
> 4. **Teo Jing Wei left OSL Pay in Jun 2026.** Do not target him.

<details open>
<summary><h2>📊 Section 1: Quick Look</h2></summary>

**Summary:** OSL Group is a Hong Kong-listed "global stablecoin payment and trading platform". It runs an SFC-licensed exchange in Hong Kong, two fiat-to-crypto on/off-ramps (OSL Pay, run from Italy, and Banxa, acquired 2 Jan 2026), OSL BizPay for B2B stablecoin payments, and the USDGO stablecoin (issued by Anchorage Digital Bank). It holds "50+ licenses and registrations across 11 jurisdictions", and 86% of H1 2026 revenue was booked in Asia Pacific.

**SimilarWeb total visits (last full month):** not pulled for this account. No traffic file in `accounts/traffic/`. Markets below are ordered by licensed APAC presence, not traffic.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| n/a | **Hong Kong** | not pulled | Exchange: eDDA, FPS, USD wires. Banxa: HKD cards, Apple Pay, Google Pay | OSL Pay does not list HKD. No FPS, PayMe, AlipayHK or Octopus on either ramp | ✅ OSL Digital Securities Limited (SFC VATP; Type 1, 4, 7, 9; AMLO) |
| n/a | **Japan** | not pulled | JPY cards and wallets (both ramps) | No bank transfer (furikomi), konbini or PayPay on either ramp | ✅ OSL Japan Limited (formerly CoinBest K.K.), FSA-registered |
| n/a | **Indonesia** | not pulled | IDR cards and wallets | No QRIS, virtual accounts or e-wallets (GoPay, OVO, DANA) listed | ✅ PT Multikripto Exchange Indonesia (OJK digital asset trader) |
| n/a | **Australia** | not pulled | PayID, NPP, cards (Banxa) | Covered | ✅ Banxa (AUSTRAC DCE); OSL ASIC AFSL (Jun 2026) |
| n/a | **Singapore** | not pulled | Banxa: SGD cards and wallets | OSL Pay blacklists SG. No PayNow | ❌ OSL SG Pte. Ltd. has no licence; MAS lists it as no longer exempt |

### Legal entities
- OSL Group Limited (Hong Kong listed, HKEX: 863), formerly BC Technology Group
- OSL Digital Securities Limited (Hong Kong): SFC VATP; SFC Type 1, 4, 7, 9; AMLO
- OSL Japan Limited (Japan): FSA-registered crypto exchange, 81.38% held
- PT Multikripto Exchange Indonesia (Indonesia): OJK digital asset trader, 90% held indirectly
- OSL Bermuda Limited (Bermuda): BMA Class F Digital Asset Business licence
- OSL EU GmbH (Austria): MiCAR CASP from the FMA, 7 Jul 2026
- OSL Pay (Italy): OAM VASP registration; MiCAR application filed 5 Dec 2025
- Banxa entities (Australia, Canada, US, EU)
- OSL SG Pte. Ltd. (Singapore): unlicensed, "no longer exempt" per MAS

### Known PSPs
- ⚠️ **No acquirer or gateway is named** for OSL Pay or Banxa. The interim report refers only to "payment gateway providers" (plural, unnamed).
- **StraitsX**: USD dedicated virtual accounts for OSL Pay (press release, Jan 2026)
- **Banking Circle**: BC-Now settlement in AUD, EUR, GBP, HKD, SGD, USD (press release, Sep 2026)
- **Mastercard Crypto Partner Program**: joined 8 May 2026
- Principal bankers (interim report): Bank of China (Hong Kong), Bank of Communications, Chiyu Banking, DBS Bank, Standard Chartered Bank (Hong Kong)

### Orchestration status
**Not established.** No orchestrator is named in any source reviewed, and acquirers are not named either. A dedicated orchestrator search was not run, so this is not scored as greenfield. OSL Pay and Banxa run separate SDKs and entities; the interim report flags the risk of having "to build, integrate and manage additional technology stacks".

### Buying signals
- 🚀 MiCAR CASP authorisation from Austria's FMA, 7 Jul 2026, passportable across 30 EEA states ([release](https://www.osl.com/hk-en/press-release/from-hong-kong-to-europe-osl-clears-micar-in-austria-joining-the-minority-of-platforms-to-meet-europes-stringent-crypto-rulebookf))
- 🚀 ASIC AFSL granted, Jun 2026 ([release](https://www.osl.com/hk-en/press-release/osl-group-secures-australian-financial-services-licence-afsl))
- 💰 Jan 2026 placement, net HK$1,549.8M: about 30% acquisitions, 35% global business including payments and stablecoins, 15% product and technology infrastructure ([Interim Report 2026](https://www.hkexnews.hk/listedco/listconews/sehk/2026/0924/2026092400430.pdf))
- 🤝 Banxa acquisition completed 2 Jan 2026 ([HKEX](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0102/2026010202110.pdf))
- 📋 OSL Pay MiCAR application filed in Italy, 5 Dec 2025

</details>

<details open>
<summary><h2>✉️ Section 2: Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach OSL` to draft the 12-touch sequence, or call this from `/prepare_batch`.*

Suggested order from the research: open with Angle 1 (approval rates) to Eugene Cheung, bring in Ivan Wong on Angle 2 (channel cost), and hold Angle 3 (local methods) for Siwei Gong. See Section 10 below.

</details>

<details>
<summary><h2>📚 Section 3: Full Research</h2></summary>

### ICP Score breakdown: 14 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5 ⚠️** | ⚠️ **NOT FOUND, ASSUMED ≥100,000/month. [ASSUMPTION, not researched.]** Basis: H1 2026 payment volume was HK$61.0B (interim report), about HK$10.2B a month. Average ramp ticket is not published, so no derivation is possible. Even a high average ticket would leave the count well above 100,000, but part of that volume may be large B2B or institutional flows. Billing unit: on/off-ramp fiat payments, not crypto trades. |
| Orchestration status | 0 | ⬜ Uncertain. No orchestrator named in any source reviewed, but no dedicated orchestrator search was run and acquirers are unnamed. |
| 3+ countries | +3 | ✅ Licensed entities confirmed in Hong Kong, Japan, Indonesia, Bermuda, Austria, Italy and Australia (interim report, HKEX announcements, releases). |
| Multiple PSPs | 0 | ⬜ Uncertain. The interim report cites "payment gateway providers" (plural) but names none. OSL Pay and Banxa are OSL's own ramps, not third-party PSPs. |
| Local rail or licensing gap in a top-3 market | 0 | ⬜ Uncertain. Sourced gaps exist (no QRIS in Indonesia, no konbini or PayPay in Japan, per the published method lists), but no traffic data was pulled, so top-3 market rank is not established. |
| Recent expansion | +2 | ✅ MiCAR CASP Austria (Jul 2026), ASIC AFSL (Jun 2026), Banxa acquisition (Jan 2026). |
| Payment issues reported | +2 | ✅ First-party evidence: OSL Pay's own published card success-rate tables put many issuers at 30 to 50% or under 30%. Customer complaints (app stores, Reddit, X) were not checked. |
| Funding >$10M | +2 | ✅ Jan 2026 placement of 104,698,000 shares at HK$14.90, net HK$1,549.8M, completed 4 Feb 2026. |
| High traffic outside home | 0 | ⬜ Not pulled. Revenue: 86% booked in Asia Pacific (HK, SG, AU, JP, ID combined), so no home-share figure. |
| Competitor using orchestration | 0 | ⬜ Not researched. |
| Payment job postings | 0 | ⬜ Not researched. |

**Tier:** High Priority (17+) ⭐ / Medium (10 to 16) 🟢 / Low (<10) 🔴 → **🟢 Medium**
No analyst override applied. Two flags for Prateek: (1) crypto on-ramp is a high-risk MCC, so acquirer appetite must be confirmed before outreach; (2) Banxa and OSL BizPay are payment providers to other platforms, which touches the Phase 0 "PSP or gateway" gate. The merchant angle on OSL's own ramps still stands.

### Source Notes
- ✅ Revenue and its gross accounting basis, revenue by line and region, payment volume, adjusted non-IFRS income, net loss, cash, fee and commission expenses, headcount, principal bankers, board, shareholding, placements, Banxa completion and risk disclosures: OSL 2026 Interim Report (HKEX, 24 Sep 2026).
- ✅ Banxa completion on 2 Jan 2026: HKEX announcement, interim report, Banxa closing release. C$1.55 per share, 51,842,084 shares, C$80.36M aggregate, TSXV delisting 5 Jan 2026.
- ✅ Approval-rate tiers: OSL Pay docs (USD, JPY, MYR, AUD, TWD pages, updated 13 to 14 May 2026). Scoped to the USD table, not HKD.
- ✅ Japan: 81.38% CoinBest stake agreed 4 Nov 2024, completed 17 Jan 2025 (HKEX). Feb 2025 was the rebrand.
- ✅ Indonesia: Koinsayang completed 22 Sep 2025 (HKEX), 90% held indirectly.
- ✅ Liu Shuai stake: 260,653,433 shares, 28.89% (interim report). A 28.98% figure from a secondary site was rejected.
- ✅ Banking Circle expansion announced Sep 2026 (not Oct). The 9 Oct 2026 item is the Siwei Gong Q&A.
- ✅ "Varies by market and acquirer" comes from the Banxa page on osl.com, not OSL Pay docs.
- ✅ Banxa card currencies do not include MYR.
- ❌ Removed as stale or pre-restatement: OSL Pay "HK$55.94M, 29% of revenue" (May to Jun 2025) and "Europe HK$56M in H1 2025". Restated 1H2025 Europe revenue is HK$783.3M.
- ❌ Teo Jing Wei as OSL Pay CEO: his LinkedIn shows OSL Pay CEO from Mar 2025 to Jun 2026, then CEO of BE Trust. Dropped.
- ⚠️ OSL Pay's and Banxa's acquirers: not named anywhere.
- ⚠️ Who now runs OSL Pay after Jun 2026: not found.
- ⚠️ OSL SG's withdrawn MAS MPI application: from the 2023 annual report, not rechecked. The MAS "no longer exempt" listing is confirmed.
- ⚠️ FY2025 customer concentration (top five 27%, largest 17%): secondary summary of the 2025 annual report.
- ⚠️ Banxa FINTRAC registration and 37-jurisdiction US licence list: Banxa's own page, not checked against regulators.
- ⚠️ Banxa "trusted partners" logos (Checkout.com, Worldpay, Worldline, Plaid) did not render when fetched. Worldline has a published Banxa integration as a distribution partner, not confirmed as acquirer.
- ⚠️ Albert Wong (SVP, OSL BizPay): undated OSL X post, probably around Apr 2026. Yun Cheng (CTO): MarketScreener only. Hoi Chan: 2025 LinkedIn activity only. Ben Yu: confirmed Nov 2025, 2026 status unconfirmed.
- ⚠️ OSL HK "#1 in Hong Kong by spot and stablecoin volume" and the Aug 2026 zero-fee stablecoin trading: secondary coverage only.
- ⚠️ App store, Reddit and X complaints about card declines: not checked.

### Success Case Alternatives
- **inDrive**: about 90% approval with Yuno, and live in 10 LatAm countries in under 8 months. Fits Angle 1 (approval rates) and Angle 3 (adding local methods per market).
- Approved proof line: "Trusted by inDrive, Uber and SpaceX". No crypto or exchange case study is used.

---

## Executive Summary

OSL Group is a Hong Kong-listed stablecoin payment and trading platform. H1 2026 reported revenue was HK$55,812.6M (+65.8%), of which payments were HK$49,083.1M (88%), but that revenue is booked gross: revenue less cost of digital assets sold was HK$130.9M and adjusted non-IFRS income was HK$330.9M (+75.5%). Loss from continuing operations was HK$860.9M. Payments run through two on-ramp stacks, OSL Pay and Banxa, whose acquirers are not named. OSL Pay publishes its own card approval rates by issuer, many of them low, and gateway channel fees pushed fee and commission expenses up more than 5x year on year. The motion is undetermined (no orchestrator or acquirer named), with three verified angles: approval rates, channel cost across two stacks, and local methods in markets where OSL already holds licences.

### Section 1: Website Traffic Analysis by Country

**No traffic data.** SimilarWeb was not pulled for osl.com and there is no file in `accounts/traffic/`. Revenue by booking region is used as a proxy below. It is not a traffic split.

**H1 2026 revenue by booking region (HK$M):** Asia Pacific 48,012.7 (HK, SG, AU, JP, ID); Europe 4,744.9 (IT, NL, UK); Bermuda 2,011.5; North America 1,043.5 (CA, US). Source: Interim Report 2026.

### Section 2: Legal Entities & Local Presence

**Headquarters:** Hong Kong. Founded 2003 as BC Technology Group, renamed OSL Group in 2024. Largest shareholder: Crown Research Investments Limited (formerly BGX Group Holding), wholly owned by Liu Shuai through DeltaByte Holdings, 28.89%. SCMP reported BGX had apparent ties to Bitget (2023).

| Market | Entity and licence | Notes |
|---|---|---|
| Hong Kong | OSL Digital Securities Limited: SFC VATP; SFC Type 1, 4, 7, 9; AMLO | Home market. Not among the first HKMA stablecoin issuers: on 10 Apr 2026 the HKMA licensed only HSBC and Anchorpoint ([HKMA](https://www.hkma.gov.hk/eng/news-and-media/insight/2026/04/20260410/)) |
| Japan | OSL Japan Limited (formerly CoinBest K.K.), FSA-registered crypto exchange | 81.38% stake agreed 4 Nov 2024, completed 17 Jan 2025, renamed Feb 2025 |
| Indonesia | PT Multikripto Exchange Indonesia (formerly Koinsayang), OJK digital asset trader | Completed 22 Sep 2025, 90% held indirectly. Joined the ICEx Group SRO in May 2026 |
| Australia | Banxa entity registered with AUSTRAC as a digital currency exchange; OSL ASIC AFSL (Jun 2026) | AFSL covers payment, custody and OTC services for wholesale clients |
| Europe | OSL Pay (Italy, OAM VASP, MiCAR application filed Dec 2025); OSL EU GmbH, MiCAR CASP from Austria's FMA (7 Jul 2026); Banxa EU entity MiCA-licensed in the Netherlands (secondary) | H1 2026 Europe revenue HK$4,744.9M, up from HK$783.3M |
| Bermuda | OSL Bermuda Limited, BMA Class F Digital Asset Business licence | HK$2,011.5M of H1 2026 revenue |
| North America | Banxa entities in Canada and the US; OSL BizPay under a Canadian MSB framework | HK$1,043.5M of H1 2026 revenue. OSL Pay blacklists US issuers, IPs and KYC |
| Singapore | OSL SG Pte. Ltd. | No licence. MAS lists it as no longer exempt ([MAS](https://www.mas.gov.sg/regulation/payments/entities-that-are-no-longer-exempt-pursuant-to-the-ps-esp-r)). Singapore access goes through partners such as MetaComp and StraitsX |

**Cross-Border Gap Analysis:** OSL holds a licensed entity in Hong Kong, Japan, Indonesia and Australia. Singapore is the one APAC market where it has no licence and OSL Pay blacklists SG issuers. No traffic data, so top-market ranking is not established.

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Region | Provider | Evidence Type | Source |
|---|---|---|---|
| Global | **Unnamed "payment gateway providers"** behind OSL Pay and Banxa | `[Annual/Interim Report]` | [Interim Report 2026](https://www.hkexnews.hk/listedco/listconews/sehk/2026/0924/2026092400430.pdf) |
| Global | StraitsX (USD dedicated virtual accounts for OSL Pay) | `[Press Release]` | [StraitsX](https://www.straitsx.com/blog-post/straitsx-enables-seamless-usd-access-for-osl-pay-users) |
| Global | Banking Circle (BC-Now settlement, six currencies) | `[Press Release]` | [osl.com](https://www.osl.com/hk-en/press-release/banking-circle-osl-stablecoin-fiat-expansion) |
| Global | Mastercard Crypto Partner Program | `[Press]` | [PANews](https://www.panews.io/articles/019e0641-bd41-7401-af34-70d00879b380) |
| Institutional | Anchorage Digital Bank (USDGO issuer), Circle (USDC, Apr 2026), Ripple RLUSD listing, MetaComp (HK to SG), Morph (BizPay settlement), CoinPayments (uses OSL's APAC rails, Mar 2026) | `[Press Release]` | See Appendix |

**OSL exchange funding (Hong Kong):** HKD via eDDA ("as fast as 5 minutes with zero handling fees") and FPS; USD via bank transfer, CHATS or telegraphic transfer into OSL's USD trust account. Same-name accounts only, mandatory reference code, no cash. No card, Apple Pay or Google Pay funding found on the exchange ([deposit guide](https://www.osl.com/hk-en/bits/article/osl-fiat-deposit-and-withdrawal-guide)).

**OSL Pay (Italy):** Visa, Mastercard, Apple Pay, Google Pay; OSL marketing also cites bank transfers. 138 fiat currencies including JPY, IDR, PHP, MYR, THB, VND, INR, SGD and TWD; HKD and CNY not listed. Blacklisted for KYC, IP and issuing bank: US, China, Singapore and sanctioned countries. Integration via WebSDK, iOS and Android SDKs, OpenAPI with card-binding and risk SDKs; KYC sharing with Sumsub ([overview](https://docs.pay.osl.com/docs/overview)). Product page promises a "High-Performance API Layer, designed for speed, reliability, and higher approval rates" ([product page](https://docs.pay.osl.com/docs/getting-started)).

**Banxa (acquired Jan 2026):** cards, Apple Pay and Google Pay in 28 currencies (including HKD, SGD, JPY, IDR, AUD, THB, PHP, VND, INR, TWD); PayPal (EU, EUR); PayID and NPP (AU); iDEAL; SEPA; Klarna Pay Now; UK Faster Payments; Interac; ACH (sell only); SPEI; Khipu; South Africa bank transfer; VietQR ([Banxa methods](https://docs.banxa.com/docs/supported-payment-methods)). osl.com describes Banxa's methods as "varying by market and acquirer" ([osl.com/en/banxa](https://www.osl.com/en/banxa)). Banxa names Kraken, Trust Wallet and KuCoin as platforms using it.

#### 3B. Payment Orchestrator

**Not established.** No orchestrator named in any source reviewed; no dedicated orchestrator search was run. Two in-house on-ramp stacks (OSL Pay and Banxa) with separate SDKs and entities. The press release says Banxa's integration is complete, but the interim report says OSL "commenced its wholesale integration during the first half of 2026" and flags the risk of having "to build, integrate and manage additional technology stacks".

### Section 4: Alternative & Local Payment Methods

| Market | Covered | Missing on the ramps |
|---|---|---|
| Hong Kong | Exchange: eDDA, FPS, wires. Banxa: HKD cards and wallets | OSL Pay does not list HKD. No FPS, PayMe, AlipayHK or Octopus on either ramp |
| Japan | JPY cards and wallets (both ramps) | No bank transfer (furikomi), konbini or PayPay on either ramp |
| Indonesia | IDR cards and wallets | No QRIS, virtual accounts or e-wallets (GoPay, OVO, DANA) listed, despite owning OSL Indonesia |
| Singapore | Banxa: SGD cards and wallets | OSL Pay blacklists SG. No PayNow |
| Philippines, Thailand, India | PHP, THB, INR cards and wallets | No GCash or Maya, PromptPay or UPI listed |
| Malaysia | OSL Pay lists MYR | Banxa has no MYR. No DuitNow or FPX listed |
| Vietnam | VietQR on Banxa (OSL Pay VietQR per the Claude draft, not rechecked) | Covered |
| Australia | PayID, NPP, cards | Covered |

Source: published method lists ([Banxa](https://docs.banxa.com/docs/supported-payment-methods), [OSL Pay](https://docs.pay.osl.com/docs/overview)).

### Section 5: Payment Issues & Customer Complaints

| Issue | Rail | Frequency | Source |
|---|---|---|---|
| **Low card approval rates published by OSL Pay itself**: 30 to 50% and under 30% tiers across many APAC issuers; best tier only "over 60%" | Cards | Structural (first-party data) | [OSL Pay USD](https://docs.pay.osl.com/docs/creditdebit-card-success-rate-local-banks-in-us-usd), [MYR](https://docs.pay.osl.com/docs/creditdebit-card-success-rate-local-banks-in-malaysia) |
| MYR table: Standard Chartered Bank Malaysia under 30%. TWD table: Sumitomo Mitsui Card and Taiwan Shin Kong under 30% | Cards | Structural | OSL Pay docs |
| Category-wide card friction: issuers screen crypto merchants, some decline outright, crypto MCC markups of 3 to 5% on debit are normal | Cards | Structural | [Banxa content](https://banxa.com/coins/buy-tether-google-pay) |
| App store, Reddit and X complaints | All | **Not checked** | n/a |

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | Nov 2025 | OSL BizPay and Morph partnership (Ben Yu, Head of OSL BizPay) | Partnership | [osl.com](https://www.osl.com/hk-en/press-release/OSL-Biz-Pay-Partners-with-Morph-to-Power-the-Next-Generation-of-On-chain-Payments) |
| 2 | Dec 2025 | Orlando Merone named GM of OSL Pay (Italy); OSL Pay files for MiCAR in Italy (5 Dec) | Leadership, licence | [aziendabanca.it](https://www.aziendabanca.it/notizie/fintech-insurtech/osl-pay-in-regime-transitorio-micar-assunzioni-nella-sede-di-milano) |
| 3 | 2 Jan 2026 | Banxa acquisition completed (C$1.55 per share); TSXV delisting 5 Jan | M&A | [HKEX](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0102/2026010202110.pdf), [Newsfile](https://www.newsfilecorp.com/release/279359) |
| 4 | 29 Jan 2026 | US$200M placement agreed; OSL Pay adopts StraitsX USD virtual accounts | Funding, partnership | Interim report, StraitsX |
| 5 | Feb 2026 | USDGO launched with Anchorage Digital Bank (US$50M at launch, over US$1.2B by Aug 2026) | Product | Interim report |
| 6 | 27 Mar 2026 | CoinPayments partnership (Eugene Cheung quoted as CCO) | Partnership | [Crypto Briefing](https://cryptobriefing.com/coinpayments-accelerates-apac-expansion-with-osl-group-partnership/) |
| 7 | 10 Apr 2026 | HKMA grants first stablecoin licences to HSBC and Anchorpoint only | Regulatory | [HKMA](https://www.hkma.gov.hk/eng/news-and-media/insight/2026/04/20260410/) |
| 8 | 20 Apr 2026 | Travel Rule integration with Futu's PantherTrade | Partnership | [osl.com](https://www.osl.com/hk-en/press-release/osl-group-and-panthertrade-implement-hong-kong-travel-rule-to-forge-a-trusted-digital-asset-ecosystem) |
| 9 | 22 Apr 2026 | Circle USDC partnership | Partnership | [PR Newswire](https://www.prnewswire.com/apac/news-releases/osl-group-and-circle-announce-partnership-to-expand-access-to-usdc-in-global-markets-302749531.html) |
| 10 | 8 May 2026 | Joins the Mastercard Crypto Partner Program | Partnership | [PANews](https://www.panews.io/articles/019e0641-bd41-7401-af34-70d00879b380) |
| 11 | Jun 2026 | ASIC AFSL granted; Teo Jing Wei leaves OSL Pay (LinkedIn) | Licence, leadership | [osl.com](https://www.osl.com/hk-en/press-release/osl-group-secures-australian-financial-services-licence-afsl) |
| 12 | 7 Jul 2026 | MiCAR CASP authorisation from Austria's FMA (announced 9 Jul) | Licence | osl.com |
| 13 | 7 Aug 2026 | OSL AgentPay launched (stablecoin payments for AI agents) | Product | [GlobeNewswire](https://www.globenewswire.com/news-release/2026/08/07/3340938/0/en/osl-group-launches-osl-agentpay-multi-stablecoin-payment-infrastructure-for-ai-agents.html) |
| 14 | 12 Aug 2026 | CFO Ivan Wong appointed Executive Director | Leadership | Interim report |
| 15 | Sep 2026 | Banking Circle expansion to six currencies; interim report published 24 Sep | Partnership | osl.com |

**Stated priorities (H1 2026):** broaden stablecoin products, drive USDGO adoption, build next-generation stablecoin market infrastructure, agentic payments, operational efficiency, accretive global M&A "with particular attention to high-growth emerging markets".

**Public payment RFP:** none found. **Payment hiring:** not researched.

### Section 7: Payment-Specific News

- Fee and commission expenses up from HK$26.7M to HK$141.6M in H1 2026, "mainly due to the channel fees paid to payment gateway providers" (interim report). IT costs rose from HK$24.5M to HK$100.9M.
- OSL Pay pricing: 1.8% ramp fee on card, Apple Pay and Google Pay buys and card sells, plus spreads (channel 0.5 to 5%, liquidity 0.1 to 0.15%, FX risk 0 to 1.2%, buffer 0 to 0.2%). Fiat deposit fees 0 to 4%. OSL Pay's own worked example gives about 4.5% total spread on a credit card purchase ([pricing](https://www.osl-pay.com/en/pricing-information)).
- 9 Oct 2026: Siwei Gong Q&A on stablecoin-to-fiat settlement in Asia ([TechNode](https://technode.global/2026/10/09/osl-siwei-gong-stablecoin-fiat-settlement-asia-qa/)).

### Section 8: Checkout Experience Audit

**Not performed.** No live checkout walk was done on OSL Pay, Banxa or the OSL exchange. Integration surfaces from docs: OSL Pay WebSDK, iOS and Android SDKs, OpenAPI; Banxa hosted checkout, headless SDK and API.

### Section 9: PCI DSS Compliance

**Not researched.** No PCI documentation was checked for OSL Pay or Banxa.

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: Lift approval rates on the card on-ramp with smart routing and failover**
> **For:** Eugene Cheung and Orlando Merone.
> **Evidence:** OSL Pay's own USD table puts ZA Bank and Bank of China (Hong Kong) at 30 to 50% and Standard Chartered Bank under 30%, and tells users to check the table before paying ([OSL Pay docs](https://docs.pay.osl.com/docs/creditdebit-card-success-rate-local-banks-in-us-usd)). OSL Pay sells "higher approval rates" as a feature.
> **Yuno Value Proposition:** one integration with smart routing and failover across providers, so a weak issuer and acquirer pairing gets a second route instead of a decline. Proof: inDrive reached about 90% approval with Yuno.
> **Opening question:** "Your docs put ZA Bank and BOC HK at 30 to 50%. How many acquiring routes can OSL Pay retry those on today?"

> **Insight #2: One layer over OSL Pay and Banxa to cut channel cost**
> **For:** Ivan Wong.
> **Evidence:** fee and commission expenses rose from HK$26.7M to HK$141.6M, "mainly due to the channel fees paid to payment gateway providers", and the interim report flags the cost of integrating "additional technology stacks" after Banxa ([Interim Report 2026](https://www.hkexnews.hk/listedco/listconews/sehk/2026/0924/2026092400430.pdf)). Operational efficiency is one of six stated priorities.
> **Yuno Value Proposition:** one integration for both ramps, with routing by cost as well as approval.
> **Opening question:** "With channel fees up more than 5x year on year, are OSL Pay and Banxa routing through the same providers yet?"

> **Insight #3: Local payment methods for the APAC licences OSL already owns**
> **For:** Siwei Gong and Kevin Cui.
> **Evidence:** OSL owns licensed entities in Japan and Indonesia, yet the published ramp lists show JPY and IDR as card-only, with no QRIS, virtual accounts, e-wallets, bank transfer or konbini ([Banxa methods](https://docs.banxa.com/docs/supported-payment-methods), [OSL Pay overview](https://docs.pay.osl.com/docs/overview)). M&A is aimed at "high-growth emerging markets".
> **Yuno Value Proposition:** 1,000+ payment methods through one integration, so each new market can add local bank transfer, QR and wallets without a new PSP build. inDrive went live in 10 LatAm countries in under 8 months.
> **Opening question:** "OSL Indonesia is licensed, but the ramps show no QRIS. Is local funding on the 2027 roadmap?"

**Thin margin on big flows:** revenue less cost of digital assets sold was HK$130.9M on HK$55.8B of revenue. Every point of approval rate or processing cost on the on-ramp is material.

**Caveat:** crypto on-ramp traffic is a high-risk MCC. Confirm which Yuno-connected acquirers will take this volume in HK, the EU, Australia and Japan before outreach.

### Key contacts

| Name | Title | Status and evidence | Why |
|---|---|---|---|
| Eugene Cheung | Chief Commercial Officer, OSL Group (since Mar 2025) | Quoted as CCO in Mar and Apr 2026 releases. LinkedIn also shows a current role at 2wa.io, so confirm. linkedin.com/in/ecgold | Owns commercial partnerships across payments and trading |
| Ivan Wong (Wong Kwun Man) | CFO (since Nov 2024), Executive Director (since 12 Aug 2026) | ✅ Verified, 2026 Interim Report | Owns cost, channel fees and efficiency targets |
| Siwei Gong | Global Head of Financial Institution Partnerships | ✅ Verified, TechNode Q&A (9 Oct 2026) | Fiat channels and local rails |
| Orlando Merone | General Manager, OSL Pay (Italy, since Dec 2025) | aziendabanca.it (2 Feb 2026) | Runs the OSL Pay entity |
| Kevin Cui (Cui Song) | Executive Director and CEO, OSL Group | ✅ Verified, interim report and results release | Economic buyer |
| Gary Tiu (Tiu Ka Chun) | Executive Director | ✅ ED verified (interim report). "Head of Regulatory Affairs" from the FY2025 call transcript | Licensing |
| Ben Yu | Head of OSL BizPay | ⚠️ Confirmed Nov 2025. 2026 status not confirmed | B2B payments |
| Albert Wong | SVP, OSL BizPay | ⚠️ OSL X post, undated (likely Apr 2026) | B2B payments |
| Holger Arians | Co-founder, Banxa | ⚠️ Co-CEO at deal close. Current role not confirmed | Banxa side |
| Teo Jing Wei | Former CEO, OSL Pay | ❌ Left Jun 2026 (LinkedIn). Do not target | n/a |

**Gaps:** no named group Head of Payments, Head of Fiat Operations or current OSL Pay CEO found.

### Section 11: Similar Companies & Prospecting Pipeline

**Not researched for this account.** Related files already in this repo: `2-ready-to-outreach/bitflyer.md`, `2-ready-to-outreach/coinspot.md`, `2-ready-to-outreach/indodax.md`, `1-to-outreach/coinjar.md`, `1-to-outreach/swyftx.md`. No competitor orchestration case study was searched for.

### Section 12: Business Case Data

| Metric | Value | Source |
|---|---|---|
| Reported revenue H1 2026 | **HK$55,812.6M** (+65.8%), gross basis. 1H2025 restated to HK$33,671.4M | Interim Report 2026 ✅ |
| Payment revenue H1 2026 | HK$49,083.1M (+69.3%), 88% of revenue; almost all on/off-ramp (HK$49,053.4M) | ✅ |
| Trading revenue H1 2026 | HK$6,707.8M (mainly OTC) | ✅ |
| Revenue less cost of digital assets sold | **HK$130.9M** (1H2025: HK$195.4M). Cost of digital assets sold HK$55,681.8M | ✅ |
| Adjusted non-IFRS income | HK$330.9M (+75.5%) | ✅ |
| Loss from continuing operations | HK$860.9M | ✅ |
| Transaction volume H1 2026 | HK$172.0B (+241.3%). Payment volume HK$61.0B (+65.3%). Ex market-making HK$97.7B | ✅ |
| FY2025 (reported 31 Mar 2026) | Total income HK$489M (+30.4%), core operating income HK$534M (+150.1%), transaction volume HK$201.22B (+200.7%, stablecoins 60%), net loss, net cash HK$1,135.0M. Pre-gross presentation | FY2025 results coverage |
| Fee and commission expenses | HK$141.6M (1H2025: HK$26.7M) | ✅ |
| Cash | Cash after client liabilities HK$1,438.4M; cash and equivalents HK$1,403.4M | ✅ |
| Headcount | 483 (30 Jun 2025: 427) | ✅ |
| Customer concentration | Customer A HK$5,905.1M, about 10.6% of H1 2026 revenue. In 1H2025 four customers each topped 10% | ✅ |
| Banxa contribution | HK$2,039.9M revenue, HK$81.6M net loss in H1 2026 | ✅ |
| Platform (SaaS) revenue | HK$21.7M in H1 2026, down from HK$92.3M | ✅ |
| Average transaction value | **Not found** | n/a |
| **Monthly transaction count** | ⚠️ **NOT FOUND, ASSUMED ≥100,000/month. [ASSUMPTION, not researched.]** Basis: HK$61.0B H1 2026 payment volume (about HK$10.2B a month) with no published average ticket. Billing unit: on/off-ramp fiat payments, not crypto trades | n/a |
| Primary currencies | HKD, USD on the exchange; 138 fiat currencies on OSL Pay; 28 card currencies on Banxa | ✅ |

### Overall Research Confidence

**Medium-High on financials, entities, licences, payment methods and approval-rate data** (HKEX filings, OSL Pay and Banxa developer docs, press releases, all fetched). **Low or absent on:** traffic (not pulled), acquirers (not named anywhere), orchestrator check, complaints, checkout walk, PCI, competitors and hiring (not researched). Prepared from a Claude deep-research draft (329 sources) fact-checked against primary sources on 22 Oct 2026.

### Manual Research Recommendations

> **Area:** Monthly transaction count
> **Why it matters:** assumed, not sourced. Payment volume is known (HK$61.0B in H1 2026) but the average ticket is not.
> **Action:** ask on a call: on/off-ramp payments per month across OSL Pay and Banxa.

> **Area:** Acquirers behind OSL Pay and Banxa
> **Why it matters:** the HK$141.6M channel-fee line goes to unnamed "payment gateway providers". Knowing them sets the displacement or greenfield motion.
> **Action:** a DevTools walk of an OSL Pay and a Banxa card purchase; discovery question.

> **Area:** Crypto acquirer appetite on the Yuno side
> **Why it matters:** high-risk MCC; the pitch fails if no Yuno-connected acquirer will take the volume.
> **Action:** check internally before outreach.

> **Area:** Current OSL Pay leadership and Eugene Cheung's status
> **Why it matters:** Teo Jing Wei left in Jun 2026; Eugene Cheung's LinkedIn lists a founder role at 2wa.io.
> **Action:** LinkedIn check before sequencing.

> **Area:** SimilarWeb, orchestrator search, job postings, competitor orchestration
> **Why it matters:** four ICP signals scored 0 only because they were not researched.
> **Action:** pull `accounts/traffic/osl.md` and rerun the ICP score.

### Appendix: All Source URLs

**Primary (fetched and read):**
- https://www.hkexnews.hk/listedco/listconews/sehk/2026/0924/2026092400430.pdf (Interim Report 2026)
- https://www.osl.com/hk-en/press-release/osl-group-2026-interim-results-stablecoin-payment-infrastructure (H1 2026 results release)
- https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0102/2026010202110.pdf (Banxa completion)
- https://www.newsfilecorp.com/release/279359 (Banxa closing release)
- https://www1.hkexnews.hk/listedco/listconews/sehk/2024/1104/2024110401263.pdf (CoinBest acquisition)
- https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0120/2025012000069_c.pdf (CoinBest completion)
- https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0922/2025092201832.pdf (Koinsayang completion)
- https://docs.pay.osl.com/docs/overview (OSL Pay overview)
- https://docs.pay.osl.com/docs/creditdebit-card-success-rate-local-banks-in-us-usd (OSL Pay USD success rates)
- https://docs.pay.osl.com/docs/creditdebit-card-success-rate-local-banks-in-malaysia (OSL Pay MYR success rates)
- https://docs.pay.osl.com/docs/getting-started (OSL Pay product page)
- https://www.osl-pay.com/en/pricing-information (OSL Pay pricing)
- https://docs.banxa.com/docs/supported-payment-methods (Banxa payment methods)
- https://www.osl.com/en/banxa (Banxa on osl.com)
- https://www.osl.com/hk-en/bits/article/osl-fiat-deposit-and-withdrawal-guide (OSL deposit guide)
- https://www.hkma.gov.hk/eng/news-and-media/insight/2026/04/20260410/ (HKMA stablecoin licences)
- https://www.mas.gov.sg/regulation/payments/entities-that-are-no-longer-exempt-pursuant-to-the-ps-esp-r (MAS no longer exempt list)

**Press and secondary:**
- https://fintechnews.hk/38132/various/osl-group-2025-results-stablecoin-trading-growth/ (FY2025 results coverage)
- https://banxa.com/coins/buy-tether-google-pay (Banxa card decline content)
- https://www.osl.com/hk-en/press-release/osl-group-launches-osl-pay-institutional-grade-fiat-gateway-digital-assets (OSL Pay launch)
- https://www.straitsx.com/blog-post/straitsx-enables-seamless-usd-access-for-osl-pay-users (StraitsX)
- https://www.aziendabanca.it/notizie/fintech-insurtech/osl-pay-in-regime-transitorio-micar-assunzioni-nella-sede-di-milano (Orlando Merone)
- https://it.linkedin.com/in/teojingwei (Teo Jing Wei LinkedIn)
- https://cryptobriefing.com/coinpayments-accelerates-apac-expansion-with-osl-group-partnership/ (CoinPayments)
- https://www.prnewswire.com/apac/news-releases/osl-group-and-circle-announce-partnership-to-expand-access-to-usdc-in-global-markets-302749531.html (Circle)
- https://www.osl.com/hk-en/press-release/osl-group-and-panthertrade-implement-hong-kong-travel-rule-to-forge-a-trusted-digital-asset-ecosystem (PantherTrade)
- https://technode.global/2026/10/09/osl-siwei-gong-stablecoin-fiat-settlement-asia-qa/ (Siwei Gong Q&A)
- https://www.osl.com/hk-en/press-release/banking-circle-osl-stablecoin-fiat-expansion (Banking Circle)
- https://www.panews.io/articles/019e0641-bd41-7401-af34-70d00879b380 (Mastercard program)
- https://www.osl.com/hk-en/press-release/osl-group-secures-australian-financial-services-licence-afsl (ASIC AFSL)
- https://www.osl.com/hk-en/press-release/from-hong-kong-to-europe-osl-clears-micar-in-austria-joining-the-minority-of-platforms-to-meet-europes-stringent-crypto-rulebookf (MiCAR Austria)
- https://www.globenewswire.com/news-release/2026/08/07/3340938/0/en/osl-group-launches-osl-agentpay-multi-stablecoin-payment-infrastructure-for-ai-agents.html (AgentPay)
- https://www.osl.com/hk-en/press-release/OSL-Biz-Pay-Partners-with-Morph-to-Power-the-Next-Generation-of-On-chain-Payments (BizPay and Morph)

**Full research doc:** https://docs.google.com/document/d/1uXsLwixNpEHYJ_AmQ40pn0I3SLKus1u6TEF8K-ZR4l8/edit

</details>
