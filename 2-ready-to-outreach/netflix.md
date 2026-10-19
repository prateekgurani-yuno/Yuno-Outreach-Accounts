# Netflix

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 11 / 29 → 🟢 Medium **on arithmetic** — **ANALYST OVERRIDE applied, tier set DOWN to 🔴 Low.** See the ICP breakdown for the reasoning.
**Industry:** Subscription video streaming (SVOD, consumer) · **HQ:** Los Gatos, California, USA — Netflix, Inc.; APAC hub entity **Netflix Pte. Ltd.** (Singapore) · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **In-house** — Netflix runs its own commerce/payments platform with a dedicated APAC payments function. Not greenfield; no third-party orchestrator found.
**⛔ READ BEFORE ANY OUTREACH:** The buying centre for payments is Netflix's global commerce platform in the US, not APAC. Check account ownership with your manager (global/enterprise coverage) before sequencing from APAC.

---

> # 🔒 PHASE 0 — QUALIFICATION GATE
>
> | Rule | Result |
> |---|---|
> | PSP / gateway / acquirer / orchestrator | **Does not fire.** Netflix is a merchant. |
> | Existing Yuno customer | **Not found.** `https://www.y.uno/` and `https://y.uno/en` fetched 2026-10-19: zero occurrences of "netflix" in the HTML. Caveat: an image-only logo without alt text would not show up in this check. |
> | No online payment volume | Does not fire. |
> | HQ west of Dubai with no APAC operations | **Does not fire, but borderline.** HQ is in the US. APAC operations exist: Netflix Pte. Ltd. (Singapore) is a significant subsidiary in the FY2025 10-K ([Ex-21.1](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/ex211-q425.htm)), and there are APAC offices in Singapore, Tokyo, Mumbai and Seoul ([jobs.netflix.com](https://jobs.netflix.com/region/asia-pacific)). |
> | Monthly transactions < 40,000 (sourced) | **Does not fire.** Derived floor is in the millions per month — see Section 12. |

> # ⚠️ METHOD NOTES — disclosed up front
>
> 1. **Traffic was supplied** (`accounts/traffic/netflix.md`, Similarweb Sales Intelligence, pulled 2026-10-19, Jul–Sep 2026, netflix.com only). Its caveats apply throughout this report:
>    - **(a)** Only the top 10 countries are shown, as share only. Per-country visits below are `[DERIVED from supplied share, not a SimilarWeb figure]` (share × 1.573B average monthly visits).
>    - **(b)** It covers a single domain. Netflix has no regional ccTLD variants to combine (country paths sit under netflix.com, e.g. `/in/`), so no recombination was needed.
>    - **(c)** **Mobile app and TV/console traffic is excluded.** Similarweb counts desktop and mobile web only. The 86% desktop share reflects this.
>    - **(d)** **Netflix is app- and TV-heavy.** Web traffic is used only as a market-mix signal. It was **not** used to size transactions or for the 40k gate.
>    - **(e)** The top 10 cover only 57.06% of traffic. The other 42.94% (which will include Australia, Indonesia, the Philippines, Taiwan and others) is unlisted, so APAC markets outside the top 10 have **no** traffic figure here.
> 2. **Fetch worked** (WebFetch and curl). The Phase 2 agents ran in parallel with Agent 1 because the supplied traffic already fixed the market list.
> 3. **Netflix's country payment pages were read directly.** `help.netflix.com/en/node/116380/{cc}` serves country-specific lists (the HTML is tagged `data-countries=",IN,"` and so on). I re-fetched the India and Korea pages myself. **These are the backbone of Section 4.**
> 4. **Territory weighting.** Only 3 of the top 10 traffic markets are in territory: India (#2), South Korea (#8) and Japan (#9). The research focuses on those three. US, Brazil and EU markets were not researched for methods.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Netflix is the largest global subscription streaming service, operating in 130+ countries ([InfoQ, QCon London 2026](https://infoq.com/news/2026/03/netflix-dvds-to-global-streaming/)). Q2 2026 revenue was $12.6B, of which APAC was $1.51B (+16% YoY) ([Q2'26 8-K](https://www.sec.gov/Archives/edgar/data/0001065280/000106528026000211/ex991_q226.htm)). All memberships are billed monthly ([help.netflix.com](https://help.netflix.com/en/node/116380/in)). Billing runs direct on web, with app-store billing largely exited and telco/partner bundles used heavily across APAC.

**SimilarWeb total visits (last full month):** ~1.573B average monthly visits (Jul–Sep 2026, 4.720B over 3 months). Source: supplied. Web only; app and TV traffic excluded.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | United States | 20.27% | Visa/MC/Amex/Discover, prepaid, gift cards, PayPal, partners | Out of territory, not assessed | ✅ Netflix, Inc. (HQ) |
| 2 | **India** | 6.68% | Visa/MC (credit, debit, prepaid), **UPI AutoPay**, partner bundles (Airtel, Jio, Vi, Tata Play, ACT, Flipkart Plus) | **RuPay, Amex, Diners, netbanking, wallets; @paytm UPI handle removed; gift cards not sold** | ⚠️ Netflix Entertainment Services India LLP (named in press and a tax tribunal ruling; LLPIN not verified) |
| 3 | Brazil | 4.79% | Not researched (out of territory) | — | Not researched |
| 4 | United Kingdom | 4.48% | Not researched (out of territory) | — | Not researched |
| 5 | France | 4.16% | Not researched (out of territory) | — | Not researched |
| *8* | ***South Korea*** | *3.07%* | *Locally issued cards only (BC, Hana, Hyundai, KB, KEB, Lotte, NH, Samsung, Shinhan, UnionPay), KakaoPay, telco/Naver bundles* | ***Foreign-issued cards; Naver Pay, Toss, PAYCO, bank debit*** | *⚠️ Netflix Services Korea Ltd. (press only; reg # not found)* |
| *9* | ***Japan*** | *2.89%* | *Visa/MC/Amex/Diners/JCB, PayPay, konbini postpaid (atone), gift cards at konbini, docomo/au/SoftBank carrier billing* | *Paidy, LINE Pay, Rakuten Pay, PayPal (minor)* | *⚠️ Netflix G.K. (older 10-K exhibits; corporate number not found)* |

*The italic rows are APAC markets outside the overall top 5, added because they are the only other in-territory markets in the top 10.*

### Legal entities
- **Netflix, Inc.** (USA, HQ: 121 Albright Way, Los Gatos, CA). Named as service provider ([corpinfo](https://help.netflix.com/legal/corpinfo)).
- **Netflix Pte. Ltd.** (Singapore). UEN 201531197W `[UNVERIFIED — search summary only]`. Its existence is confirmed in [10-K Ex-21.1](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/ex211-q425.htm).
- **Netflix Entertainment Services India LLP** (India). LLPIN not found.
- **Netflix Services Korea Ltd.** (South Korea). Registration number not found.
- **Netflix G.K.** (Japan). Corporate number not found.
- **Netflix Australia Pty Ltd** (Australia). ABN 81 601 296 771 `[UNVERIFIED]`.

### Known PSPs
- **Adyen**: `[Third-Party Report]`, 2016–2018 only (CNBC/Bloomberg on Adyen's IPO). **Stale and unverified; the current relationship is unknown.**
- **Cardinal Commerce (Visa) 3DS**: `[Source Code]` strings in netflix.com/in. This is an inference from code strings, not observed in a live checkout.
- **Visa Token Service**: Netflix was the first merchant to tokenize cards-on-file with Visa ([Visa, Oct 2018](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.15916.html)).
- **No PSP is named for India, Japan or Korea.**

### Orchestration status
**In-house orchestration layer.** Evidence:
- A Netflix principal engineer (commerce architecture) described a home-built commerce platform at QCon London 2026, with a *"deliberate decision to duplicate vendor integration code rather than create shared components"* ([InfoQ, Mar 2026](https://infoq.com/news/2026/03/netflix-dvds-to-global-streaming/)).
- 2014–15 Netflix engineering decks describe 15+ processors, routing logic and an in-house tokenizer `[UNVERIFIED — search summary only, stale]`.
- No third-party orchestrator (Juspay, Spreedly, Primer, Gr4vy, Yuno) was found.

### Buying signals
- 🤝 **Korea, Naver Plus bundle.** Netflix launched it in Nov 2024 ([Netflix](https://about.netflix.com/en/news/netflix-now-available-through-naver-plus-membership)). The upgrade price was cut from 1 Jul 2026 ([Asia Economy](https://view.asiae.co.kr/en/article/2026062516554754886), `[UNVERIFIED — search summary only]`).
- 📈 **APAC is the second-fastest-growing region.** Q2'26 revenue was +16% reported and +18% F/X-neutral ([8-K](https://www.sec.gov/Archives/edgar/data/0001065280/000106528026000211/ex991_q226.htm)).
- 🧪 **Japan pricing test.** The Q2'26 letter mentions a low-cost first-month test in Japan and free-trial re-tests outside the US/UK (same 8-K). These are acquisition-funnel experiments that touch payment flows.
- ⚠️ **No funding, RFP or confirmed APAC payments hire.** The WBD acquisition is **dead**: Paramount paid Netflix a $2.8B break fee on 27 Feb 2026 ([TheWrap](https://www.thewrap.com/industry-news/deals-ma/paramount-pays-netflix-warner-bros-breakup-fee/)). Do not use it as a trigger.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach netflix` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 11 / 29
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | +5 | ✅ **DERIVED (floor): ≥ ~16.8M/month in APAC alone.** Q2'26 APAC revenue of US$1,510M ÷ 3 = US$503M/month ([8-K](https://www.sec.gov/Archives/edgar/data/0001065280/000106528026000211/ex991_q226.htm)), and every membership is billed monthly ([help.netflix.com](https://help.netflix.com/en/node/116380/in)). Dividing by a deliberately inflated ATV of US$30 gives ~16.8M/month. US$30 is about twice the highest APAC plan price sourced (Japan Premium ¥2,290 ≈ US$15, [Gigazine](https://gigazine.net/gsc_news/en/20260327-netflix-raises-prices)), so this is a floor, not a measurement. Even if 90% of APAC revenue ran through partner bundles, direct transactions would still be over 1.6M/month. **Billing unit:** one monthly membership charge. Partner-billed (telco/Naver/Jio) members are billed by the partner and do not appear as Netflix card/UPI transactions. |
| Orchestration status | +1 | ✅ **In-house layer** (InfoQ/QCon 2026, verified fetch; 2014–15 decks stale). Hardest sell. |
| 3+ countries | +3 | ✅ 10 countries above 2.8% each (supplied Similarweb). |
| Multiple PSPs | 0 | ⬜ Only Adyen is named, and only in 2016–18 third-party coverage. "15+ processors" comes from a 2015 deck, unverified. |
| Local rail or licensing gap in a top-3 market | 0 | ❌ **Not met.** India (#2) has UPI AutoPay, the dominant recurring rail. RuPay and netbanking are absent ([help page](https://help.netflix.com/en/node/116380/in)), but neither is the rail this signal names. US and Brazil are out of territory. Korea and Japan are not top-3. |
| Recent expansion | 0 | ❌ No new-market launch in the last 12 months. Netflix already operates in 130+ countries. |
| Payment issues reported | 0 | ⬜ Complaints are isolated (Voxya, a Reddit mirror, a Jupiter forum). The Oct 2021 RBI e-mandate disruption is more than 12 months old and was a forecast, not measured. |
| Funding >$10M | 0 | ❌ N/A. Public company, no funding round. |
| High traffic outside home | +2 | ✅ US is 20.27% of traffic, well below 60%. |
| Competitor using orchestration | 0 | ⬜ No verified direct competitor on an orchestrator. TAL rows showing "Juspay" for SonyLIV, Zee5 and U-NEXT are flagged as bulk-filled, and the SonyLIV row conflicts with NPCI naming Razorpay. ELEVEN Sports on Gr4vy is a peer, not a direct competitor. |
| Payment job postings | 0 | ⬜ "Principal PM, Payment Platform" and "Group PM, Payments Product Journey" turned up via search summary only, US/remote, dates unclear. No APAC payments role was found. |

**Arithmetic tier:** 11 → 🟢 Medium.

**⚖️ ANALYST OVERRIDE — tier set DOWN to 🔴 Low.** Reasoning:
1. **The matrix is double-counting scale.** Eight of the 11 points (transaction volume, 3+ countries, traffic outside home) are true of any global consumer giant. None of them indicates a payments gap or a buying trigger.
2. **In-house, and deliberately so.** Netflix has:
   - a principal engineer leading commerce architecture;
   - a named Director of Payments Asia Pacific (Shalini Khatwani, 2022; [Netflix](https://about.netflix.com/en/news/alternative-methods-of-payment-apac); current role unverified);
   - 16+ local payment partners added in APAC by 2021 (same source);
   - first-merchant status on UPI AutoPay (2021) and on Visa card-on-file tokenization (2017–18).

   They chose to duplicate vendor integrations to move faster ("Some duplication is cheaper than coordination", [InfoQ](https://infoq.com/news/2026/03/netflix-dvds-to-global-streaming/)). "You need orchestration" will not land, and the gaps found below look more like deliberate choices than neglect.
3. **The buying centre is out of territory.** Payments architecture sits with the global commerce platform team in the US. APAC is ~12% of revenue ($1.51B of $12.6B in Q2'26).
4. **A large slice of APAC billing is untouchable.** The India, Korea and Japan pages each list 8–15 telco, ISP and bundle partners that bill on Netflix's behalf. Their share is not disclosed.

**What would reverse this:** a confirmed APAC payments hire or RFP, evidence that Netflix is consolidating vendors, or a warm path into the commerce platform team. Until then, treat this as a **named strategic account for manager or enterprise review, not an SDR cold sequence.**

### Source Notes
- ✅ India accepts Visa and Mastercard only, plus UPI AutoPay. The @paytm handle was removed and partner bundles are listed. Verified by direct curl on 2026-10-19: [help.netflix.com/en/node/116380/in](https://help.netflix.com/en/node/116380/in)
- ✅ Korea accepts locally issued cards only, KakaoPay is the only wallet, and partners include Naver. Verified by direct curl on 2026-10-19: [help.netflix.com/en/node/116380/kr](https://help.netflix.com/en/node/116380/kr)
- ✅ The commerce platform is in-house with duplicated vendor integrations, and the India RBI response used mandates, 3DS and pre-debit notifications. Verified fetch: [InfoQ](https://infoq.com/news/2026/03/netflix-dvds-to-global-streaming/)
- ✅ Q2'26 financials and APAC segment. Verified fetch: [SEC 8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/0001065280/000106528026000211/ex991_q226.htm)
- ✅ The APAC alternative-payments post (16 partners added; alternative-method sign-ups tripled 2020→21). Verified fetch: [about.netflix.com](https://about.netflix.com/en/news/alternative-methods-of-payment-apac)
- ⚠️ **UPI AutoPay launch date conflict.** Netflix's newsroom dates it 30–31 Aug 2021 ([about.netflix.com](https://about.netflix.com/en/news/now-you-can-use-upi-autopay-on-netflix), verified fetch), while Madhyamam reports a 2023 rollout. The primary source wins: **2021**.
- ⚠️ Adyen as Netflix's processor rests only on 2016–18 press `[UNVERIFIED — search summary only]`. Do not cite it in outreach.
- ⚠️ Netflix Pte. Ltd.'s UEN, Netflix Australia's ABN, and the India and Korea entity financials come from search summaries only.
- ⚠️ India FY25 entity turnover of ₹3,768.98 cr ([exchange4media](https://www.exchange4media.com/digital-news/netflix-india-profit-up-61-in-fy25-revenue-surges-over-32-148719.html)) and Korea CY2025 revenue of ₩1.0542T ([inews24](https://inews24.com/view/2015019)) are both `[UNVERIFIED — search summary only]`.

### Success Case Alternatives
- **No strong Yuno success case match.** No published Yuno case covers a global SVOD with an in-house payments platform. Any case cited in outreach must come from Yuno's current case library, verified at time of use. Do not pull from memory.

---

## Executive Summary

Netflix is a US-headquartered global subscription streaming service in 130+ countries. APAC generated $1.51B in Q2 2026, growing faster than UCAN and EMEA. It runs an **in-house commerce and payments platform**, has a dedicated APAC payments function, and has been an early mover on APAC rails: UPI AutoPay in India (2021), PayPay and konbini in Japan, KakaoPay in Korea, and GoPay/OVO/DANA/ShopeePay in Indonesia. The verifiable gaps are narrow:
- **India:** card acceptance is limited to Visa and Mastercard (no RuPay, Amex or Diners), and the @paytm UPI handle was lost to RBI restrictions.
- **Korea:** foreign-issued cards are excluded entirely, and KakaoPay is the only wallet.

**Motion: in-house**, which is the hardest sell. Combined with a US buying centre, this is a manager-review account, not a cold-sequence target.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** Supplied Similarweb (Sales Intelligence, pulled 2026-10-19, Jul–Sep 2026), `accounts/traffic/netflix.md`. Visits are `[DERIVED from supplied share, not a SimilarWeb figure]`: share × 1.573B average monthly visits. Desktop is 86.17% and mobile web 13.83%. **App and TV traffic are excluded.**

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | United States | 20.27% | ~318.9M [DERIVED] | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | **India** ⭐ | 6.68% | ~105.1M [DERIVED] | Not supplied | same |
| 3 | Brazil | 4.79% | ~75.3M [DERIVED] | Not supplied | same |
| 4 | United Kingdom | 4.48% | ~70.5M [DERIVED] | Not supplied | same |
| 5 | France | 4.16% | ~65.4M [DERIVED] | Not supplied | same |
| 6 | Germany | 4.09% | ~64.3M [DERIVED] | Not supplied | same |
| 7 | Canada | 3.82% | ~60.1M [DERIVED] | Not supplied | same |
| 8 | **South Korea** | 3.07% | ~48.3M [DERIVED] | Not supplied | same |
| 9 | **Japan** | 2.89% | ~45.5M [DERIVED] | Not supplied | same |
| 10 | Spain | 2.81% | ~44.2M [DERIVED] | Not supplied | same |

- **High priority (>5%) in territory:** India only.
- **In-territory top-10 markets:** India, South Korea, Japan. Each has a local entity named in some source, but none has a primary-verified registration number (see Section 2).
- **42.94% of traffic is unlisted.** Australia, Indonesia, the Philippines, Taiwan, Thailand and others have no figure. Do not infer their rank.
- **Global rank:** not captured in the supplied view.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Los Gatos, California, USA. Netflix, Inc. is named as service provider and data controller ([corpinfo](https://help.netflix.com/legal/corpinfo)). Founding year not checked this run.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| USA | Netflix, Inc. | — | [help.netflix.com/legal/corpinfo](https://help.netflix.com/legal/corpinfo) (verified fetch) |
| Singapore | Netflix Pte. Ltd. | UEN 201531197W `[UNVERIFIED]` | [10-K FY2025 Ex-21.1](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/ex211-q425.htm) (verified fetch, existence only); UEN via [acrawatch.sg](https://acrawatch.sg/company/netflix-pte-ltd) |
| Netherlands | Netflix International B.V. | — | Same Ex-21.1 |
| India | Netflix Entertainment Services India LLP | Not found | [ITAT ruling summary](https://tpcases.com/india-vs-netflix-entertainment-services-india-llp-october-2025-income-tax-appellate-tribunal-ita-no-6857-mum-2024/) describes it as a "non-exclusive distributor of access to the Netflix Service in India" `[UNVERIFIED — search summary only]` |
| South Korea | Netflix Services Korea Ltd. (넷플릭스서비시스코리아 유한회사) | Not found | [inews24](https://inews24.com/view/2015019) `[UNVERIFIED — search summary only]` |
| Japan | Netflix G.K. (合同会社) | Not found | Older 10-K Ex-21 ([2023](https://www.sec.gov/Archives/edgar/data/1065280/000106528023000035/ex211-q422.htm)) `[UNVERIFIED]` |
| Australia | Netflix Australia Pty Ltd | ABN 81 601 296 771 `[UNVERIFIED]` | [IBISWorld](https://www.ibisworld.com/australia/company/netflix-australia-pty-ltd/432575/) |

**Contracting party:** Search snippets of the en, id and vi Terms of Use say the service is "provided to you by Netflix, Inc." `[UNVERIFIED — search summary only]`. The India, Korea and Japan versions were not confirmed.

`[INFERENCE, not confirmed]` The India and Korea entities look like distributor/reseller vehicles, not merchant of record. The Korean entity reportedly passes ~81% of revenue to the parent at a ~1.9% operating margin ([inews24](https://inews24.com/view/2015019), unverified), and the ITAT ruling describes the India entity as a "non-exclusive distributor". Which entity sits on the acquiring contract is not established.

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| India | Yes (#2) | ⚠️ Named, not registry-verified | Domestic rails (UPI AutoPay) are live, so local processing is evidently in place | Low on the evidence. UPI AutoPay cannot run cross-border. |
| South Korea | Yes (#8) | ⚠️ Named, not registry-verified | Netflix accepts **only locally issued cards**, which is consistent with domestic PG processing `[INFERENCE]` | Low for Korean cardholders. **Foreign-card holders in Korea are excluded entirely.** |
| Japan | Yes (#9) | ⚠️ Named, not registry-verified | PayPay, konbini and carrier billing are live, which implies local partners | Low on the evidence |

No "warning" language applies. Netflix visibly runs domestic rails in all three in-territory markets.

> **MANUAL:** Verify the India LLPIN (MCA), the Korean business registration (DART), the Japan corporate number (houjin-bangou.nta.go.jp), and the contracting entity on the India, Korea and Japan Terms of Use.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Global | Adyen. **STALE, 2016–18; current status unknown.** | [Third-Party Report] `[UNVERIFIED — search summary only]` | [CNBC 2018](https://www.cnbc.com/2018/08/22/dutch-payments-firm-adyen-first-half-profit-surges.html); [Bloomberg 2018](https://www.bloomberg.com/news/articles/2018-06-12/amsterdam-s-adyen-valued-at-8-36-billion-in-european-ipo) |
| Global | Visa Token Service (network tokens on card-on-file; first merchant; live in 19 countries in 2018) | [Press Release] (verified fetch) | [Visa, 18 Oct 2018](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.15916.html) |
| India (netflix.com/in) | Cardinal Commerce 3DS. Inferred from strings: "3ds" appears 15 times and "Cardinal" 4 times in the page bundle. | [Source Code] `[INFERENCE, not confirmed]` | netflix.com/in (curl, 2026-10-19) |
| Global | "15+ payment processors & verification services", "2M transactions a day" (2015 deck) | [Tech Blog / Conference] `[UNVERIFIED — search summary only, STALE]` | [SlideShare 2015](https://www.slideshare.net/slideshow/payments-inthecloud/46195495) |
| India / Japan / Korea / ANZ | **Not found** | — | No PSP is named in the UPI AutoPay announcement, the checkout source, or the Privacy Statement |

**The Privacy Statement names no processors.** It refers generically to "payment processing" service providers and to partners that "collect payment for the service" ([help.netflix.com/legal/privacy](https://help.netflix.com/en/legal/privacy), `[UNVERIFIED — search summary only]`).

#### 3B. Payment Orchestrator

**Classification: In-house orchestration layer.**
- [Tech Blog / Conference, verified fetch] At QCon London 2026, Netflix's principal engineer for commerce architecture described a home-built billing and payments platform serving 130+ countries. On vendor integrations: *"a deliberate decision to duplicate vendor integration code rather than create shared components, enabling each team to move independently and much faster. 'Some duplication is cheaper than coordination.'"* ([InfoQ](https://infoq.com/news/2026/03/netflix-dvds-to-global-streaming/)).
- [Tech Blog, stale, unverified] 2014–15 Netflix decks describe processor routing logic, an in-house tokenizer, and traffic forking across processors.
- [Job Listing, unverified] A 2026 "Principal Product Manager, Payment Platform" role covers "managing and optimizing integrations with payment providers, processors" ([TCV portfolio jobs](https://portfoliojobs.tcv.com/companies/netflix/jobs/71363778-principal-product-manager-payment-platform)).
- **Third-party orchestrators:** none found (Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno).

> *Motion implication:* Netflix does not need to be told why orchestration matters. It already built one. The only defensible angles are **marginal reach** (specific rails or issuer segments it has not covered) and **opportunity cost** (engineering time on APAC long-tail integrations). Never pitch "you need orchestration".

> **MANUAL:** Check netflix.com/in and /kr signup network calls in DevTools for acquirer and 3DS-server hostnames.

---

### Section 4: Alternative & Local Payment Methods

All APAC rows come from Netflix's country-specific help pages, fetched 2026-10-19. Absence means "not on Netflix's own list for that country". The checkout itself was not tested by VPN.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| All | Monthly billing only; no annual, multi-month or lifetime plans | — | Mentioned in docs | [node/116380/in](https://help.netflix.com/en/node/116380/in) |
| Global | Apple IAP | App store | **Deprecated.** Ended for new members Dec 2018; legacy members told to switch Feb 2024 | [BGR 2018](https://bgr.com/2018/12/28/netflix-in-app-subscription-itunes-payment-method-dead/); [Gigazine 2024](https://gigazine.net/gsc_news/en/20240227-netflix-apple-payment-update) `[UNVERIFIED — search summary only]` |
| Global | Google Play billing | App store | Unknown. Netflix added it in 2016 and declined a 10% rate in 2017 (Epic v. Google); current status not found | [droid-life](https://www.droid-life.com/2016/04/26/coming-soon-pay-netflix-google-play-billing/); [Android Authority](https://androidauthority.com/google-play-store-netflix-lower-billing-fee-3384510) `[UNVERIFIED]` |
| Global | Apple Pay / Google Pay | Digital wallet | Not found on any country page checked | node/116380/{us,in,jp,kr,au} |
| India | Visa, Mastercard (credit, debit, virtual, co-branded, prepaid) | Cards | Mentioned in docs | [node/116380/in](https://help.netflix.com/en/node/116380/in) (verified) |
| India | **UPI AutoPay** (most consumer UPI apps) | Direct debit / mandate | Mentioned in docs. Live since Aug 2021 | Same; [Netflix newsroom](https://about.netflix.com/en/news/now-you-can-use-upi-autopay-on-netflix) |
| India | Paytm UPI handle (@paytm) | A2A | **Deprecated.** "No longer available due to local restrictions" | Same (verified) |
| India | **RuPay** | Cards | **Not found** | Same (verified; "rupay" appears 0 times in the page) |
| India | Amex, Diners | Cards | Not found (reportedly accepted in 2021, `[UNVERIFIED]`) | Same |
| India | Netbanking | Bank transfer | Not found | Same |
| India | Wallets (Paytm, PhonePe, Amazon Pay as wallet) | Digital wallet | Not found | Same |
| India | Gift cards | Voucher | Not sold in India | [node/32950/in](https://help.netflix.com/en/node/32950/in) |
| India | Airtel, Reliance Jio, Vi/Vodafone Idea, Tata Play, ACT, Flipkart Plus | Carrier / partner billing | Mentioned in docs | node/116380/in (verified) |
| Japan | Visa, MC, Amex, Diners, **JCB**; virtual and prepaid | Cards | Mentioned in docs | [node/116380/jp](https://help.netflix.com/en/node/116380/jp) |
| Japan | **PayPay** | Digital wallet | Mentioned in docs. Live since 14 Feb 2022 | Same; [PayPay notice](https://paypay.ne.jp/notice/20220214/01/) |
| Japan | **Konbini postpaid by atone** | Cash / BNPL | Mentioned in docs | node/116380/jp |
| Japan | Gift cards (7-Eleven, FamilyMart, Lawson) | Cash / voucher | Mentioned in docs | [node/32950/jp](https://help.netflix.com/en/node/32950/jp) |
| Japan | NTT docomo, KDDI/au, SoftBank, UQ mobile, plus 10+ ISPs/bundles | Carrier billing | Mentioned in docs | node/116380/jp |
| Japan | Paidy, LINE Pay, Rakuten Pay, PayPal | Wallet / BNPL | Not found | node/116380/jp |
| South Korea | **Locally issued cards only**: BC, Hana, Hyundai, KB, KEB, Lotte, NH, Samsung, Shinhan, UnionPay; virtual cards | Cards | Mentioned in docs | [node/116380/kr](https://help.netflix.com/en/node/116380/kr) (verified) |
| South Korea | Foreign-issued Visa/MC/Amex | Cards | **Not accepted**. Policy dates to at least May 2016 | Same; [Korea Times 2016](https://www.koreatimes.co.kr/www/tech/2025/01/129_204110.html) |
| South Korea | **KakaoPay** | Digital wallet | Mentioned in docs (launch date not found) | node/116380/kr (verified) |
| South Korea | Naver Pay, Toss, PAYCO, Samsung Pay, bank debit | Wallet / A2A | **Not found** | node/116380/kr (verified) |
| South Korea | KT, LG U+, SK Telecom, SK Broadband, KT Skylife, LG Electronics, LINEYahoo, **Naver Package** | Carrier / partner billing | Mentioned in docs | node/116380/kr (verified) |
| Indonesia *(not in top 10)* | Cards, Dana, GoPay, OVO, ShopeePay; Telkomsel, IndiHome | Wallet / carrier | Mentioned in docs. **QRIS not listed** | [node/116380/id](https://help.netflix.com/en/node/116380/id) |
| Philippines *(not in top 10)* | Cards, **GCash, Maya**; Smart, PLDT, Converge | Wallet / carrier | Mentioned in docs | [node/116380/ph](https://help.netflix.com/en/node/116380/ph) |
| Australia *(not in top 10)* | Cards, PayPal, gift cards; Telstra (closed to new), Optus/SubHub, Foxtel, Hubbl | Mixed | Mentioned in docs. PayTo not listed | [node/116380/au](https://help.netflix.com/en/node/116380/au) |

**Gaps worth stating (sourced absence on Netflix's own list):**
> *India:* RuPay, India's domestic card scheme, is not on Netflix's accepted-card list. Only Visa and Mastercard logos appear ([help.netflix.com](https://help.netflix.com/en/node/116380/in)). RuPay's prominence must be sourced live before use in outreach. It is not cited here.

> *Korea:* Netflix accepts only locally issued Korean cards and one wallet (KakaoPay). Naver Pay, the wallet of its own bundle partner Naver, is not a payment method ([help.netflix.com](https://help.netflix.com/en/node/116380/kr)).

**UPI AutoPay is present**, so the dominant-rail gap signal does not fire for India. Japan's coverage is strong: JCB, PayPay, konbini, all three carriers. **The global-stack "missing local rails" pitch does not apply to Netflix.**

> **MANUAL:** VPN-test netflix.com/in signup for a RuPay card BIN (does it decline, or is it silently accepted despite the logo list?). Also VPN-test /kr with a foreign-issued card.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Failed recurring payments (RBI e-mandate rules, market-wide) | Press | High (market-wide **forecast**, not a measured Netflix outcome) | Sep–Oct 2021 | [MediaNama](https://www.medianama.com/2021/09/223-netflix-upi-autopay-rbi-regulations/); [TechRadar](https://www.techradar.com/news/your-auto-payment-for-amazon-netflix-may-fail-from-tomorrow-this-is-why) `[UNVERIFIED — search summary only]` |
| UPI mandate cannot be revoked / unexpected ₹499 charge (Amazon Pay UPI) | Reddit (mirror) | Isolated | Feb 2026 | [reddit mirror](https://reddit.sentinel-team.org/posts/1r8r821/snapshots/2026-02-19T11%3A36%3A06.98046Z) `[UNVERIFIED]` |
| Payment deducted, not reflected; autopay de-registration | Voxya (IN) | Isolated–moderate | 2022–2023 | [Voxya 1](https://voxya.com/consumer-complaints/payment-issue/209708); [Voxya 2](https://voxya.com/consumer-complaints/autopay-option-needs-to-be-stopped/148754) `[UNVERIFIED]` |
| Duplicate autopay entries after retry | Jupiter community | Isolated | Undated | [Jupiter](https://community.jupiter.money/t/autopay-setup-bug/31038?page=3) `[UNVERIFIED]` |
| Card declines possibly linked to 3DS (India) | HotUKDeals | Isolated, anecdotal | Undated | [HotUKDeals](https://www.hotukdeals.com/discussions/netflix-india-vpn-not-working-anymore-4518107) `[UNVERIFIED]` |

Netflix's own error E101 help article lists cards "not enabled for recurring" and charges treated as international among the causes of an account hold ([help.netflix.com/en/node/2065](https://help.netflix.com/en/node/2065), `[UNVERIFIED]`). The India payment page carries its own decline message: *"Your bank must support recurring payments through UPI AutoPay. If the charge is declined, please choose a different payment option."*

**Pattern:** India recurring friction (mandate set-up, bank support for UPI AutoPay, card recurring enablement) is the only recurring theme. The evidence is **isolated and anecdotal**. **Do not claim a decline problem in outreach.** App store reviews were not reached within budget.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 2026-07 (Q2'26 letter) | APAC revenue $1,510M, +16% YoY (+18% F/X-neutral); low-cost first-month test in Japan; free-trial re-tests outside US/UK | Market Expansion (funnel) | [8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/0001065280/000106528026000211/ex991_q226.htm) (verified) |
| 2 | ~2026-07-29 | Kumar Kanagasabapathy hired as Director, Brand Partnerships APAC (Singapore) | Leadership Change (non-payments) | [exchange4media](https://www.exchange4media.com/people-movement-news/kumar-kanagasabapathy-joins-netflix-as-director-brand-partnerships-for-apac-156747.html) `[UNVERIFIED]` |
| 3 | 2026-06-25 | Korea: Naver Plus bundle upgrade price cut, effective 1 Jul 2026 | Partnership | [Asia Economy](https://view.asiae.co.kr/en/article/2026062516554754886) `[UNVERIFIED]` |
| 4 | 2026-03-17 | QCon London talk on Netflix's in-house commerce architecture | Tech Blog / Conference Signal | [InfoQ](https://infoq.com/news/2026/03/netflix-dvds-to-global-streaming/) (verified) |
| 5 | 2026-02-27 | WBD acquisition terminated; Paramount paid Netflix a $2.8B break fee | M&A (dead) | [TheWrap](https://www.thewrap.com/industry-news/deals-ma/paramount-pays-netflix-warner-bros-breakup-fee/) (verified) |

- **No public payment-related RFP found.**
- **Payment job postings:** "Principal PM, Payment Platform" ([TCV](https://portfoliojobs.tcv.com/companies/netflix/jobs/71363778-principal-product-manager-payment-platform)) and "Group PM, Payments Product Journey" ([BuiltIn LA](https://www.builtinla.com/job/group-product-manager-payments-product-journey/10368611)) were both seen in search summaries only, US/remote, dates unclear. **No APAC payments role found** in Singapore, Tokyo, Seoul or Mumbai.
- **No new licence application** found.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 2026-03-26 | US price rise on all plans. Japan unchanged (¥890 / ¥1,590 / ¥2,290) | Pricing; ATV reference | [Gigazine](https://gigazine.net/gsc_news/en/20260327-netflix-raises-prices) (verified) |
| 2 | 2025-05 | Korea price rise: Standard with ads ₩5,500→₩7,000; Basic ₩9,500→₩12,000 for existing users | Pricing | [Korea Times](https://www.koreatimes.co.kr/amp/business/tech-science/20250511/netflix-under-fire-for-rate-hike-as-rivals-freeze-fees) `[UNVERIFIED]` |
| 3 | 2024-11-25 | Netflix available through Naver Plus membership (Korea) | New partner billing channel | [Netflix](https://about.netflix.com/en/news/netflix-now-available-through-naver-plus-membership) |
| 4 | 2024-02 | Legacy Apple-billed members told to move to another payment method | App-store exit complete | [Gigazine](https://gigazine.net/gsc_news/en/20240227-netflix-apple-payment-update) `[UNVERIFIED]` |
| 5 | 2022-06-28 | "Alternative methods of payment" (APAC): 16 new payment partners; alternative-method sign-ups more than tripled 2020→21; GoPay (ID), carrier billing (TW, KR), UPI (IN) | APAC payments strategy | [Netflix](https://about.netflix.com/en/news/alternative-methods-of-payment-apac) (verified) |

> **REMOVAL:** Netflix India no longer accepts the @paytm UPI handle "due to local restrictions". The help page links the RBI press release on Paytm Payments Bank (2024). Source: [help.netflix.com/en/node/116380/in](https://help.netflix.com/en/node/116380/in) (verified 2026-10-19).

India prices are unchanged since the Dec 2021 cut (₹149 / ₹199 / ₹499 / ₹649), per the live netflix.com/in page on 2026-10-19. An undated NavBharat Live "India price hike" claim contradicts the live site and is disregarded.

---

### Section 8: Checkout Experience Audit

*Full checkout flow not accessible (no account / VPN test). Findings are limited to the server-rendered netflix.com/in page bundle and the help centre.*

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | Custom-built multi-step SPA, server-rendered shell | N/A | Custom-built |
| Guest checkout | Account creation is required (subscription) | N/A | Inherent to the model |
| Steps to complete payment | Not observed | — | — |
| Card input experience | "Set up your credit or debit card" flow; tokenization approach not observed | — | — |
| Payment methods visible | IN bundle strings: card, UPI AutoPay ("Select your UPI app", "Confirm your UPI ID"), gift code, wallet, carrier ("Contract Mobile Phone Number") | Good | String presence ≠ enabled |
| Location-based method display | Yes. Per-country method lists on help pages; country-path site | Good | — |
| Instalment / EMI | N/A (monthly subscription) | N/A | — |
| 3DS implementation | "3ds" ×15 and "Cardinal" ×4 in the bundle | — | `[INFERENCE]` Cardinal 3DS |
| PCI indicator | Not determined | — | — |
| Mobile responsiveness | Not tested | — | — |
| Multi-currency / local pricing | INR pricing on /in (₹149–₹649, pre-tax) | Good | — |
| Saved payment methods | N/A | — | — |
| Error message clarity | UPI decline guidance on the help page | Fair | — |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found | — |
| Card data handling | Not found. Network tokenization with Visa on card-on-file since 2017–18 | [Visa](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.15916.html) |
| Recommended Yuno integration | Back-to-back API (in-house platform with its own vault/tokenizer is the likely architecture `[INFERENCE]`) | — |

*No direct PCI compliance documentation found publicly for Netflix.* Stating a level would be an assumption.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: Korea is a closed loop — local cards plus one wallet**
> **Evidence:**
> - S4: Netflix Korea accepts only locally issued cards and KakaoPay; Naver Pay, Toss and PAYCO are absent ([node/116380/kr](https://help.netflix.com/en/node/116380/kr)).
> - S1: Korea is #8 by traffic (3.07%).
> - S7: Naver is already a bundle partner ([Netflix](https://about.netflix.com/en/news/netflix-now-available-through-naver-plus-membership)).
>
> **Pain Point:** Netflix is the Korean SVOD leader, yet foreign-card holders in Korea are locked out, and direct payers have one wallet option. Whether Netflix chose this or is constrained is unknown.
> **Yuno Value Proposition:** Adding Korean wallets and foreign-card acceptance through one integration instead of another in-house vendor build. **Opportunity-cost framing only.**
> **Best Success Case:** No verified match. Use only a current Yuno case with Korean wallet coverage, confirmed at time of use.
> **Outreach Angle:** "Netflix Korea's payment page lists one wallet and Korean-issued cards only. Curious whether that's a deliberate funnel choice or a vendor-coverage constraint."
> **Suggested Subject Line:** "Korea: one wallet, local cards only"

> **Insight #2: India — Visa and Mastercard only, and one UPI handle already lost to regulation**
> **Evidence:**
> - S4: the India card list shows Visa and Mastercard logos only, with no RuPay, Amex or Diners; the @paytm handle was removed "due to local restrictions" ([node/116380/in](https://help.netflix.com/en/node/116380/in)).
> - S1: India is the #2 traffic market (6.68%) and the largest in territory.
> - S5: recurring friction complaints are isolated but recurring in theme.
>
> **Pain Point:** Netflix's recurring acceptance in its largest APAC traffic market depends on two card schemes and UPI AutoPay. Its own page tells declined UPI users to "choose a different payment option", and that option set is narrow. The Paytm episode shows the exposure to a single provider being regulated out.
> **Yuno Value Proposition:** Redundancy across Indian processors for mandates, plus RuPay acceptance, without another in-house integration.
> **Best Success Case:** No verified match.
> **Outreach Angle:** "Your India page lists Visa and Mastercard only and tells declined UPI AutoPay users to pick another method. What's the recovery rate on that fallback?" (Ask it; don't assert it.)
> **Suggested Subject Line:** "India fallback after a UPI AutoPay decline"

> **Insight #3: They built it on purpose. Argue opportunity cost, not orchestration**
> **Evidence:**
> - S3B: an in-house platform with deliberately duplicated vendor integrations ("Some duplication is cheaper than coordination", [InfoQ](https://infoq.com/news/2026/03/netflix-dvds-to-global-streaming/)).
> - S7: 16 new APAC payment partners were added by 2021 ([Netflix](https://about.netflix.com/en/news/alternative-methods-of-payment-apac)).
> - S4: 8–15 partner billers per APAC market.
>
> **Pain Point:** Every new APAC rail is a per-team vendor integration Netflix maintains itself. They have accepted that cost knowingly.
> **Yuno Value Proposition:** Long-tail APAC rails as a managed connector set, so Netflix's engineers stay on the core. **This argues against their stated philosophy.** Expect pushback.
> **Best Success Case:** No verified match.
> **Outreach Angle:** Only via a warm intro to commerce platform or APAC payments leadership. A cold email on this will read as not having done the homework.
> **Suggested Subject Line:** "Duplication vs. coordination — APAC long tail"

**Not an insight (deliberately omitted):** "You lack local rails". The evidence says otherwise: UPI AutoPay, PayPay, konbini, KakaoPay, GoPay, OVO, DANA, ShopeePay, GCash and Maya are all live. "Cross-border approval losses" is also omitted, because domestic rails are evidently in place in IN, JP and KR.

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. Netflix Korea's payment page accepts Korean-issued cards only and one wallet (KakaoPay), even though Naver is already a bundle partner.
2. In India, Netflix's card list shows only Visa and Mastercard, and its own help page tells declined UPI AutoPay users to "choose a different payment option".
3. Netflix lost the @paytm UPI handle to "local restrictions". That is a reminder of how fast an India rail can disappear.

**Cold call openers (conversational, one sentence each):**
1. "I read the QCon write-up on how Netflix duplicates vendor integrations on purpose. How's that holding up as APAC adds rails?"
2. "When a UPI AutoPay mandate fails in India, what's the fallback recovery like, given the page only lists Visa and Mastercard?"
3. "Is Korea's local-cards-only setup a choice, or a vendor constraint you'd lift if it were cheap to?"

---

### Section 11: Similar Companies & Prospecting Pipeline

*Market-share figures below are search-summary-only. They were measured on different bases (engagement, subscriptions, revenue). Do not cite them without opening the source.*

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| JioHotstar (JioStar) | jiohotstar.com | India | 18% India SVOD engagement, Q2'26 `[UNVERIFIED]` | India | **PhonePe PG** for UPI AutoPay on RuPay credit (Oct 2025) | [PhonePe press](https://www.phonepe.com/press/phonepe-pg-rupay-and-jiohotstar-collaborate-to-simplify-subscription-payments-with-upi-autopay/) `[UNVERIFIED — search summary only]`; [medianews4u](https://www.medianews4u.com/netflix-surges-as-indias-svod-streaming-wars-tighten-justwatch-q1-2026-report/) |
| Amazon Prime Video | primevideo.com | USA | 22–23% India engagement; 19.3M JP subs `[UNVERIFIED]` | IN, JP | Not found (Amazon in-house) | [AVIA](https://avia.org/japans-premium-vod-market-reaches-inflection-point-scaling-reach-deepening-engagement-monetization/) |
| SonyLIV | sonyliv.com | India | Not found | India | **Razorpay** named by NPCI for UPI AutoPay (Jan 2022); TAL says "Juspay" (conflict) | [NPCI PDF](https://www.npci.org.in/PDF/npci/press-releases/2022/NPCI-Press-Release-UPI-AUTOPAY-feature-goes-live-on-SonyLIV.pdf) `[UNVERIFIED]` |
| ZEE5 | zee5.com | India | Not found | India + diaspora | The "Juspay" link was **debunked** in our own `yupptv.md` (republished press release, not a merchant relationship) | `2-ready-to-outreach/yupptv.md` |
| TVING | tving.com | South Korea | 23.3% of KR SVOD subs `[UNVERIFIED]` | KR | Not found | [3Vision](https://www.3vision.tv/news-insights/coupang-play-the-wildcard-reshaping-south-koreas-streaming-market) |
| Coupang Play | coupangplay.com | South Korea | 3.8M subs `[UNVERIFIED]` | KR, TW | Parent TAL row: in-house (Coupang Pay) | Same |
| Wavve | wavve.com | South Korea | 12.7% of KR SVOD subs `[UNVERIFIED]` | KR | Not found | Same |
| U-NEXT | video.unext.jp | Japan | 17.1% of JP SVOD revenue 2025 (#2 behind Netflix 27.1%) `[UNVERIFIED]` | JP | Not found. TAL "Juspay" is implausible and unevidenced | [GEM Partners](https://www.gem-standard.com/p/en/183) |

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Spotify | spotify.com | Audio subscription | Global | Adyen; moved cross-border to local acquiring for authorisation gains (2017–18) | [Adyen blog](https://adyen.com/en_GB/blog/spotify) `[UNVERIFIED — search summary only]` |
| Crunchyroll | crunchyroll.com | Anime SVOD | Global, SEA | Dropped GCash Feb 2025 (Philippines rail gap) | [Crunchyroll help](https://help.crunchyroll.com/hc/en-us/articles/35315613381780-GCash-Payment-No-Longer-Supported-What-You-Need-to-Know) `[UNVERIFIED]` |
| ELEVEN Sports | elevensports.com | Sports OTT | Global | Gr4vy orchestration customer | [Gr4vy](https://gr4vy.com/posts/eleven-case-study) |
| Viu | viu.com | SVOD | SEA, HK | Already on the TAL, stage "Contacting"; see `viu.md` | `2-ready-to-outreach/viu.md` |
| YuppTV | yupptv.com | OTT (diaspora) | India + diaspora | Juspay confirmed in production code (own research) | `2-ready-to-outreach/yupptv.md` |
| Apple TV+ / YouTube Premium / DAZN | — | Subscription video | Global | Platform-owned or not researched | — |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| ELEVEN Sports | Gr4vy | Not stated | Sports OTT | [Gr4vy case study](https://gr4vy.com/posts/eleven-case-study) (vendor marketing) |
| Setplex | Gr4vy | Not stated | IPTV / OTT platform (India gateway) | [Gr4vy](https://gr4vy.com/posts/setplex-chose-gr4vy-to-empower-payment-acceptance-on-their-ott-platform/amp/) |
| YuppTV | Juspay | Confirmed in prior repo research | Indian OTT | `2-ready-to-outreach/yupptv.md` |

*No public case studies found of direct Netflix competitors (top-tier APAC SVOD) adopting payment orchestration.*

#### 11D. Prospect Scoring

Not scored individually this run. Competitor payment evidence is mostly search-summary-only, and none of the top-tier competitors has a verified orchestration or PSP finding strong enough to award points. Only SonyLIV (Razorpay via NPCI) and JioHotstar (PhonePe PG) have a named PSP, and both are single-PSP and unverified.

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | TVING | Competitor | KR (+JP/TW per TAL) | Not scored | — | KR #2 SVOD; Wavve merger pending | ✅ Yes |
| 2 | Coupang Play | Competitor | KR, TW | Not scored | — | Growing MAU; parent in-house | ✅ Yes |
| 3 | U-NEXT | Competitor | JP | Not scored | — | JP #2 SVOD by revenue | ✅ Yes (orchestrator column suspect) |
| 4 | SonyLIV | Competitor | IN + diaspora | Not scored | — | Single named PSP (Razorpay) | ✅ Yes (orchestrator column conflicts) |
| 5 | Wavve | Competitor | KR | Not scored | — | Merger integration = payment consolidation window `[INFERENCE]` | ✅ Yes |
| 6 | ZEE5 | Competitor | IN + diaspora | Not scored | — | Diaspora cross-border billing | ✅ Yes |
| 7 | AbemaTV | Competitor | JP | Not scored | — | — | ✅ Yes |
| 8 | **JioHotstar** | Competitor | IN | Not scored | — | Single named PG (PhonePe) | ❌ **Not on TAL — genuine find** (large; check whether it routes to Partnerships given Jio Financial / Jio Payments Bank affiliations) |
| 9 | **Crunchyroll** | Peer | Global, SEA | Not scored | — | Dropped GCash in PH | ❌ **Not on TAL** — US HQ (Sony); same territory caveat as Netflix |
| 10 | Viu | Peer | SEA, HK | See `viu.md` | — | Already in progress | ✅ Yes (Contacting) |

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | FY2025 ~$45.2B `[UNVERIFIED — search summary only]`; FY2026 guidance $51.0–51.4B (verified) | [THR](https://hollywoodreporter.com/tv/tv-news/netflix-q4-2025-earnings-results-passes-325-million-subs-1236478604); [Q2'26 8-K](https://www.sec.gov/Archives/edgar/data/0001065280/000106528026000211/ex991_q226.htm) |
| APAC revenue | Q2'26 $1,510M (+16%); Q2'25 $1,305M | Q2'26 8-K (verified) |
| Other regions, Q2'26 | UCAN $5,432M · EMEA $4,034M · LATAM $1,584M | Same |
| India entity turnover | FY25 ₹3,768.98 cr (+32.4%) | [exchange4media](https://www.exchange4media.com/digital-news/netflix-india-profit-up-61-in-fy25-revenue-surges-over-32-148719.html) `[UNVERIFIED]` |
| Korea entity revenue | CY2025 ₩1.0542T | [inews24](https://inews24.com/view/2015019) `[UNVERIFIED]` |
| GMV / Gross Transaction Volume | N/A (subscription; revenue ≈ billed volume net of partner arrangements) | — |
| Average Transaction Value (USD) | Not disclosed. APAC ARM last seen $7.17 (Q2 2024) `[UNVERIFIED]`. Plan prices: IN ₹149–₹649; JP ¥890–¥2,290 | [Nasdaq](https://www.nasdaq.com/articles/netflixs-apac-focus-boosts-prospects-will-momentum-continue); netflix.com/in; [Gigazine](https://gigazine.net/gsc_news/en/20260327-netflix-raises-prices) |
| Est. Annual Transactions (APAC) | ≥ ~200M/year (floor) | $503M/month × 12 ÷ $30 inflated ATV |
| **Monthly transaction count** | **✅ DERIVED (floor): ≥ ~16.8M/month, APAC only.** $1,510M Q2'26 APAC revenue ÷ 3 ÷ $30 deliberately inflated ATV (≈2× the highest sourced APAC plan price). Both the revenue and the monthly-only billing are sourced; the ATV is a ceiling assumption chosen to make this a **floor, not a measurement**. Billing unit: one monthly membership charge. Partner-billed members are not Netflix transactions; even at a 90% partner share the figure exceeds 1.6M/month. | 8-K (verified); [help.netflix.com](https://help.netflix.com/en/node/116380/in) |
| Active Customers / Users | Global: "over 325M" paid memberships (Q4'25 letter) `[UNVERIFIED]`. APAC: 57.5M at end-2024 `[UNVERIFIED — 10-K via search summary]`. No longer reported | [THR](https://hollywoodreporter.com/tv/tv-news/netflix-q4-2025-earnings-results-passes-325-million-subs-1236478604); [FY2024 ARS](https://www.sec.gov/Archives/edgar/data/1065280/000119312525084431/d914423dars.pdf) |
| Primary Currency | USD reporting; local-currency pricing (INR, JPY, KRW) | netflix.com/in |
| Top 3 Markets by Revenue | By region: UCAN, EMEA, LATAM/APAC (Q2'26). By country: not disclosed | 8-K |
| Billing channel split (web vs app store) | **Web/direct and partner-billed dominate. Apple IAP exited** (2018 for new members; legacy migrated 2024). Google Play status unknown. **Partner/telco share not disclosed** | Section 4 sources |

---

### Overall Research Confidence

**Medium.**
- **Strong:**
  - **Traffic was supplied** (Similarweb, top 10 share only; derived visits labelled).
  - APAC payment methods come from Netflix's own country help pages, with India and Korea re-verified by direct fetch.
  - In-house architecture: QCon 2026, verified.
  - Q2'26 financials: SEC 8-K, verified.
- **Weak:**
  - No current PSP or acquirer is named for any market.
  - None of the APAC entity registration numbers is primary-verified.
  - Complaint data is anecdotal.
  - Competitor stacks are search-summary-only.
  - The checkout was not walked.
- **Structural limit:** the supplied traffic excludes app and TV, which dominate Netflix usage, and lists only the top 10 countries. Indonesia, the Philippines, Australia and Taiwan are therefore invisible in the country profile.

---

### Manual Research Recommendations

> **Area:** Account ownership
> **Why it matters:** The buying centre is Netflix's US commerce platform. An APAC SDR sequence may collide with global or enterprise coverage.
> **Suggested manual action:** Confirm with your manager whether Netflix is a named global account before any touch.

> **Area:** APAC payments leadership (S6/S10)
> **Why it matters:** The only plausible entry is the APAC payments function. Shalini Khatwani was Director, Payments APAC in 2022.
> **Suggested manual action:** Check LinkedIn / Sales Nav for the current Netflix APAC payments lead (Singapore) and the commerce platform team.

> **Area:** India RuPay / Korea foreign-card acceptance (S4)
> **Why it matters:** These are the two verifiable gaps. Both are from help pages, not checkout.
> **Suggested manual action:** VPN-test netflix.com/in signup with a RuPay BIN and /kr with a foreign card.

> **Area:** PSP stack (S3A)
> **Why it matters:** No current acquirer is known.
> **Suggested manual action:** Use DevTools on /in, /jp and /kr signup to capture acquirer and 3DS hostnames.

> **Area:** Partner-billed share (S12)
> **Why it matters:** If most APAC members are telco- or Naver-billed, the addressable volume shrinks sharply.
> **Suggested manual action:** Discovery question only. It is not public.

---

### Appendix: All Source URLs

**Traffic:** `accounts/traffic/netflix.md` (Similarweb Sales Intelligence, supplied 2026-10-19)

**Phase 0 / Entities (S2):**
- https://help.netflix.com/legal/corpinfo
- https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/ex211-q425.htm
- https://www.sec.gov/Archives/edgar/data/1065280/000106528023000035/ex211-q422.htm
- https://acrawatch.sg/company/netflix-pte-ltd
- https://tpcases.com/india-vs-netflix-entertainment-services-india-llp-october-2025-income-tax-appellate-tribunal-ita-no-6857-mum-2024/
- https://inews24.com/view/2015019
- https://www.ibisworld.com/australia/company/netflix-australia-pty-ltd/432575/
- https://jobs.netflix.com/region/asia-pacific
- https://www.y.uno/ (customer check)

**PSP / Orchestration / PCI (S3, S9):**
- https://infoq.com/news/2026/03/netflix-dvds-to-global-streaming/
- https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.15916.html
- https://www.cnbc.com/2018/08/22/dutch-payments-firm-adyen-first-half-profit-surges.html
- https://www.bloomberg.com/news/articles/2018-06-12/amsterdam-s-adyen-valued-at-8-36-billion-in-european-ipo
- https://www.slideshare.net/slideshow/payments-inthecloud/46195495
- https://help.netflix.com/en/legal/privacy
- https://portfoliojobs.tcv.com/companies/netflix/jobs/71363778-principal-product-manager-payment-platform
- https://www.builtinla.com/job/group-product-manager-payments-product-journey/10368611

**APMs (S4):**
- https://help.netflix.com/en/node/116380/in
- https://help.netflix.com/en/node/116380/jp
- https://help.netflix.com/en/node/116380/kr
- https://help.netflix.com/en/node/116380/us
- https://help.netflix.com/en/node/116380/au
- https://help.netflix.com/en/node/116380/id
- https://help.netflix.com/en/node/116380/ph
- https://help.netflix.com/en/node/32950/in
- https://help.netflix.com/en/node/32950/jp
- https://about.netflix.com/en/news/now-you-can-use-upi-autopay-on-netflix
- https://paypay.ne.jp/notice/20220214/01/
- https://www.koreatimes.co.kr/www/tech/2025/01/129_204110.html
- https://bgr.com/2018/12/28/netflix-in-app-subscription-itunes-payment-method-dead/
- https://gigazine.net/gsc_news/en/20240227-netflix-apple-payment-update
- https://www.droid-life.com/2016/04/26/coming-soon-pay-netflix-google-play-billing/
- https://androidauthority.com/google-play-store-netflix-lower-billing-fee-3384510

**Complaints (S5):**
- https://www.medianama.com/2021/09/223-netflix-upi-autopay-rbi-regulations/
- https://www.techradar.com/news/your-auto-payment-for-amazon-netflix-may-fail-from-tomorrow-this-is-why
- https://reddit.sentinel-team.org/posts/1r8r821/snapshots/2026-02-19T11%3A36%3A06.98046Z
- https://voxya.com/consumer-complaints/payment-issue/209708
- https://voxya.com/consumer-complaints/autopay-option-needs-to-be-stopped/148754
- https://community.jupiter.money/t/autopay-setup-bug/31038?page=3
- https://www.hotukdeals.com/discussions/netflix-india-vpn-not-working-anymore-4518107
- https://help.netflix.com/en/node/2065

**Developments & News (S6, S7):**
- https://www.sec.gov/Archives/edgar/data/0001065280/000106528026000211/ex991_q226.htm
- https://www.thewrap.com/industry-news/deals-ma/paramount-pays-netflix-warner-bros-breakup-fee/
- https://www.exchange4media.com/people-movement-news/kumar-kanagasabapathy-joins-netflix-as-director-brand-partnerships-for-apac-156747.html
- https://view.asiae.co.kr/en/article/2026062516554754886
- https://about.netflix.com/en/news/netflix-now-available-through-naver-plus-membership
- https://about.netflix.com/en/news/alternative-methods-of-payment-apac
- https://gigazine.net/gsc_news/en/20260327-netflix-raises-prices
- https://www.koreatimes.co.kr/amp/business/tech-science/20250511/netflix-under-fire-for-rate-hike-as-rivals-freeze-fees

**Competitors (S11):**
- https://www.phonepe.com/press/phonepe-pg-rupay-and-jiohotstar-collaborate-to-simplify-subscription-payments-with-upi-autopay/
- https://www.medianews4u.com/netflix-surges-as-indias-svod-streaming-wars-tighten-justwatch-q1-2026-report/
- https://avia.org/japans-premium-vod-market-reaches-inflection-point-scaling-reach-deepening-engagement-monetization/
- https://www.npci.org.in/PDF/npci/press-releases/2022/NPCI-Press-Release-UPI-AUTOPAY-feature-goes-live-on-SonyLIV.pdf
- https://www.3vision.tv/news-insights/coupang-play-the-wildcard-reshaping-south-koreas-streaming-market
- https://www.gem-standard.com/p/en/183
- https://adyen.com/en_GB/blog/spotify
- https://help.crunchyroll.com/hc/en-us/articles/35315613381780-GCash-Payment-No-Longer-Supported-What-You-Need-to-Know
- https://gr4vy.com/posts/eleven-case-study
- https://gr4vy.com/posts/setplex-chose-gr4vy-to-empower-payment-acceptance-on-their-ott-platform/amp/

**Financials (S12):**
- https://hollywoodreporter.com/tv/tv-news/netflix-q4-2025-earnings-results-passes-325-million-subs-1236478604
- https://www.exchange4media.com/digital-news/netflix-india-profit-up-61-in-fy25-revenue-surges-over-32-148719.html
- https://www.nasdaq.com/articles/netflixs-apac-focus-boosts-prospects-will-momentum-continue
- https://www.sec.gov/Archives/edgar/data/1065280/000119312525084431/d914423dars.pdf

</details>
