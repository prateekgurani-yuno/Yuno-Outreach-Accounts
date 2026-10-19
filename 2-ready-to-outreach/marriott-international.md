# Marriott International

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 17 / 29 → 🟢 **Medium** *(computed 17 = ⭐; analyst override applied downward — see breakdown)*
**Industry:** Hotel franchising, management & licensing (9,805 properties / 1.78M rooms, 30+ brands, Marriott Bonvoy loyalty) · **HQ:** Bethesda, Maryland, USA · APEC regional office Singapore · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** 🛠️ **IN-HOUSE (inferred)** — Marriott mandates its own global payment brand standard (FreedomPay gateway) and is running an internal "integrated gateway + tokenization" programme tied to OPERA Cloud. No third-party orchestrator found. Never pitch "you need orchestration" — pitch per-country acquiring and local-method coverage *inside the programme they are already running*.

---

> ## ⭐ THE FINDING — Marriott is re-platforming property payments across APAC right now, and its own job ad lists "acquiring" and "local payment methods" as the per-country constraints
>
> Marriott International posted **"Senior Manager, D+TT Payments Specialist"** (Singapore; *"LOCATION: APEC, Hong Kong, Macau or Taiwan"*; *"DURATION: September 2026 – October 2027"*). I fetched the page myself on 2026-10-19 (HTTP 200; listing marked *"removed at 02:14 p.m. (SGT) on Friday, Aug 28, 2026"*, i.e. the role is likely filled and the project live). Verbatim:
>
> - *"assessing current property payment configurations (integrated, hybrid, or standalone) and designing and executing transition plans to a new payment solution that integrates with Opera Cloud and associated tokenization processes."*
> - *"The role supports a multi-hotel, multi-country environment where solution design, purchasing, and implementation steps may vary by property and local market requirements."*
> - *"Define future-state payment solution options aligned to Opera Cloud integration and tokenization requirements; identify country/property-specific constraints (**legal, acquiring, local payment methods**, vendor availability, connectivity)."*
>
> Source: https://builtinsingapore.com/job/senior-manager-d-tt-payments-specialist/10496234
>
> **Why it matters:** this is a dated, funded, 14-month APAC payments programme whose scope document names the exact three things Yuno sells — acquiring per country, local payment methods, and one integration across a fragmented estate. **No vendor is named.** A parallel Shanghai role ("Senior Manager, Payment Solutions – GC", ~500 Greater China properties, "Integrated Payment Gateway and Tokenization" global project) surfaced in search only and is `[UNVERIFIED — search summary only, page returned an empty shell]`.
>
> ⚠️ **What cuts against it — read before pitching:**
> 1. **This is predominantly card-present.** The ad covers *"payment hardware (e.g., pin pads/terminals)"*, *"install payment hardware and server software"*. Property PMS/POS payments, not marriott.com checkout.
> 2. **Marriott already has a global gateway brand standard: FreedomPay** (verified, FreedomPay press release, Nov 2019: *"used across Marriott's lodging portfolio beginning in the United States and Canada and expanding into other global regions"*). The APAC programme may simply be the FreedomPay + OPERA Cloud rollout reaching APAC. Not confirmed either way.
> 3. **The hotel, not Marriott, is very likely the merchant of record.** ~66% of rooms are franchised and ~32% managed; Marriott owns/leases <1% (10-K). Fees are a % of *hotel* revenue. `[INFERENCE, not confirmed]` — the 10-K never states who the merchant of record is.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Marriott International is the world's largest hotel company by rooms — 9,805 properties and 1,779,936 rooms in 145 countries and territories at YE2025, almost entirely franchised or managed (owned/leased <1%). In APAC it runs two segments: Asia Pacific excluding China (APEC, 733 properties / 157,326 rooms, run from Singapore) and Greater China (684 properties / 188,596 rooms). Revenue FY2025 was US$26.2bn, of which US$5.4bn gross fees; Marriott Bonvoy has 295M+ members.

**SimilarWeb total visits (last full period):** 71.28M avg monthly visits to marriott.com (Jul–Sep 2026, 213.8M over 3 months) — source: **SimilarWeb (supplied 2026-10-19)**. ⚠️ Desktop + mobile web only; Bonvoy app and on-property payments are excluded; marriott.com.cn (Greater China) is **not** in the supplied data.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | United States *(home; out of territory)* | 66.96% | Unknown — checkout bot-walled | N/A (out of territory) | ✅ HQ |
| 2 | Canada *(out of territory)* | 5.14% | Unknown — checkout bot-walled | N/A (out of territory) | Not checked (out of territory) |
| 3 | **India** | 4.32% | Unknown — checkout bot-walled. Bonvoy HDFC co-brand card (Diners Club) exists | UPI / RuPay / netbanking / EMI: **NOT FOUND either way** — no source confirms presence or absence | ✅ Marriott Hotels India Pvt Ltd (+2) |
| 4 | **Japan** | 2.75% | Unknown — checkout bot-walled. Bonvoy Amex Japan co-brand card exists | konbini / PayPay / instalments: **NOT FOUND either way** | ✅ Luxury Hotels International of Japan, Inc. (+10) |
| 5 | United Kingdom *(out of territory)* | 2.41% | Unknown | N/A | Not checked |

APAC markets further down: **Australia #7 (1.43%)** — ✅ entity; **Indonesia #10 (0.91%)** — ✅ entity. Afterpay/Zip/PayTo and QRIS/GoPay/OVO/DANA all NOT FOUND either way.

### Legal entities
(SEC FY2025 10-K Exhibit 21 — https://www.sec.gov/Archives/edgar/data/1048286/000104828626000007/mar-2025q4xexx21.htm — names verified by me)
- Marriott Hotels India Private Limited; Bonvoy Hotels & Resorts India Private Limited; Starwood India Private Limited (India)
- Luxury Hotels International of Japan, Inc. + ~10 Japanese management / hospitality-service companies (Japan)
- Marriott International Management Company B.V. (Australian Branch); Starwood Australia Hotels Pty Ltd (Australia)
- PT Marriott International Indonesia; PT Luxury Hotels International Indonesia (Indonesia)
- Starwood Asia Pacific Hotels & Resorts Pte. Ltd. and 6 others (Singapore); Marriott Hong Kong Limited and 6 others (Hong Kong); Starwood Hotels & Resorts (Shanghai) Co., Ltd. and Gingerroot entities (China)
- Registration numbers: not found in this run

### Known PSPs
- **FreedomPay** — [Press Release] global gateway brand standard, US/CA first then "other global regions" (Nov 2019). APAC rollout status: not confirmed.
- **Alipay** — [Press Release] launched at 10 Greater China hotels and on Marriott.com / Marriott.com.cn bookings (Sep 2015); current online status unknown.
- **Chase Paymentech** — acquirer for US & Canada hotels (2015 owner-hub notice) `[UNVERIFIED — search summary only]`. Out of territory.
- **No e-commerce PSP/acquirer for marriott.com, and no APAC acquirer, was found.**

### Orchestration status
**In-house orchestration layer (inferred).** No third-party orchestrator (Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY, VGS, TokenEx) found against Marriott. What exists is a centrally mandated single gateway (FreedomPay) plus an internal "integrated gateway + tokenization" programme for OPERA Cloud. `[INFERENCE, not confirmed]` — no source calls this "orchestration".

### Buying signals
- 💼 APAC payments re-platforming programme, Sep 2026 – Oct 2027, scope includes acquiring and local payment methods per country — [Built In Singapore](https://builtinsingapore.com/job/senior-manager-d-tt-payments-specialist/10496234)
- 🚀 APEC 2025: record 187 organic deals (+32% YoY), 109 openings; **India the #1 signing market with a record 99 deals / 12,000+ rooms** — [Marriott via AAP/PR Newswire, 12 Feb 2026](https://www.aap.com.au/aapreleases/cision20260211ae85567)
- 🤝 Oracle OPERA Cloud PMS selected for Luxury, Premium, Select and Midscale brands (30 Jan 2024) — [Oracle](https://www.oracle.com/news/announcement/oracle-cloud-to-help-elevate-property-management-for-marriott-international-2024-01-30)
- 🚀 citizenM acquisition closed Jul 2025 (37 hotels across US, Europe, APAC) — [Marriott IR](https://marriott.gcs-web.com/news-releases/news-release-details/marriott-international-completes-acquisition-citizenm-brand) `[UNVERIFIED — search summary only]`

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Marriott International` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 17 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED: ~3.45M room nights/month in APEC alone** — 157,326 APEC rooms × 72.2% FY2025 occupancy × 30.4 days. Both inputs from the FY2025 10-K. Billing unit: **room nights**, not folios. Folios ≤ room nights, but to fall under 100,000 folios/month APEC would need an average stay of >34 nights, which is not credible. **Caveat that matters more than the band:** these are *system-wide* hotel transactions, mostly card-present and most likely settled by the owning/franchised hotel as merchant. The count of transactions **Marriott itself** processes card-not-present (marriott.com prepaid, Bonvoy app) is **NOT FOUND**. Section 12. |
| Orchestration status | +1 | ✅ In-house layer (inferred) — FreedomPay single-gateway brand standard + internal gateway/tokenization programme. No third-party orchestrator found. |
| 3+ countries | +3 | ✅ 9 countries >1% traffic share (SimilarWeb supplied); Exhibit 21 entities in 20+ APAC countries. |
| Multiple PSPs | +3 | ✅ FreedomPay (verified press release) + Alipay (press release, fetched by research agent). The 2026 APAC job ad confirms properties currently run "integrated, hybrid, or standalone" configurations that vary by market. ⚠️ Both named-vendor sources are 2015/2019. |
| Local rail or licensing gap in a top-3 market | 0 | ⬜ Top 3 = US, Canada, India. India UPI/RuPay/netbanking: **no source found for presence or absence** (checkout bot-walled). India has a local entity, so no entity gate. Uncertain = 0. |
| Recent expansion | +2 | ✅ APEC record 187 deals in 2025, India 99 deals (fetched, Feb 2026); City Express Japan entry (Dec 2025). |
| Payment issues reported | 0 | ⬜ Pattern of property-level FX/DCC markups on prepaid rates is real but mostly outside APAC and snippet-only. Only 2 payment reviews verified on Trustpilot. Not moderate on verified evidence. |
| Funding >$10M | 0 | ❌ Public company (NASDAQ: MAR); no funding round. |
| High traffic outside home | 0 | ❌ US = 66.96% of marriott.com traffic (>60%). |
| Competitor using orchestration | +2 | ✅ Radisson Hotel Group adopted CellPoint Digital's "full payment orchestration platform" across EMEA and APAC (press release dated 2022-09-06, verified). ⚠️ 4 years old. |
| Payment job postings | +1 | ✅ Singapore "D+TT Payments Specialist" (verified) + Shanghai "Payment Solutions – GC" (unverified). |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → computed **17 = ⭐**

**No public payment RFP found.**

**⚠️ Analyst override — DOWN to 🟢 Medium.** Reasoning:
1. **The volume that scores +5 is mostly not Marriott's, and mostly not card-not-present.** With ~98% of rooms franchised or managed, hotel guest payments are most plausibly acquired under each owner's merchant account, at the property, through PMS/POS terminals `[INFERENCE, not confirmed]`. Orchestration addresses card-not-present flows. The CNP volume Marriott itself controls (prepaid rates on marriott.com, the Bonvoy app, points purchases, gift cards) is undisclosed.
2. **The live trigger is a terminal-and-PMS migration.** The APAC programme is about pin pads, server software and OPERA Cloud tokenization, so Yuno's fit is partial. The parts that are squarely in scope are "acquiring" and "local payment methods" per country.
3. **An incumbent global gateway standard (FreedomPay) exists.** The APAC programme may already be committed to it. Unknown.
4. **Double-counting:** "Multiple PSPs" and "3+ countries" both draw on the same heterogeneous property estate.
5. **Decision locus is Bethesda + Singapore,** and APAC is ~9.4% of marriott.com web traffic (India + Japan + Australia + Indonesia). Greater China runs on a separate domain not covered by the supplied data.

**Re-escalate to ⭐ if discovery confirms either:** (a) Marriott is merchant of record for central prepaid / app bookings in APAC, or (b) the 2026–27 APAC programme includes e-commerce acquiring or local-method selection that is still open.

### Source Notes
- ✅ 9,805 properties / 1,779,936 rooms / 145 countries; "less than one percent" owned/leased; co-brand cards "in 11 countries"; 68% of global room nights booked by Bonvoy members; APEC 157,326 rooms; Greater China 188,596 rooms; APEC occupancy 72.2%, ADR $184.36; total revenue $26,186M. All checked by me in the FY2025 10-K text: https://www.sec.gov/Archives/edgar/data/1048286/000104828626000007/mar-20251231.htm
- ✅ Exhibit 21 entity names for India, Japan, Australia and Indonesia checked by me.
- ✅ APAC payments job ad: fetched by me, quotes verbatim.
- ✅ FreedomPay–Marriott agreement (Nov 2019): fetched by me — https://corporate.freedompay.com/press-release/freedompay-announces-an-agreement-with-marriott-international-for-commerce-technology-innovation/
- ✅ APEC 2025 results (Singapore dateline, 730+ properties, 187 deals, India 99 deals): fetched by me.
- ✅ Radisson × CellPoint Digital (2022-09-06): fetched by me.
- ⚠️ Franchised ~66% / managed ~32% room split: research agent's computation from the 10-K ownership table; not re-checked by me beyond the "<1% owned" line.
- ⚠️ Chase Paymentech (US/CA acquirer), Elavon, Shift4/MerchantLink, POS tokenization 2014, $0/$1 card validation at booking: all from Marriott owner-hub (ofhub.marriott.com) snippets. That site redirects into the bot wall. `[UNVERIFIED — search summary only]`
- ⚠️ Shanghai "Payment Solutions – GC" role (~500 properties): `[UNVERIFIED — search summary only]`
- ⚠️ India: Mastercard/Diners reportedly not accepted on the Bonvoy app (TechnoFino forum): `[UNVERIFIED — search summary only, single anecdote]`. Do not use in outreach.

### Success Case Alternatives
- *No Yuno success case was verified in this run.* The repo holds no case file with confirmed hospitality references, and y.uno is blocked in this environment. Before any outreach, pick a travel/hospitality case from Yuno's current case library. A multi-country airline or travel merchant with per-country acquiring is the closest profile match. Do not name one from memory.

---

## Executive Summary

Marriott International is a US-headquartered, asset-light hotel company (9,805 properties, 1.78M rooms; <1% owned) with large APAC operations: 733 APEC properties run from Singapore plus 684 in Greater China, and local legal entities in every APAC traffic market. The key payments finding is a **live, dated APAC programme (Sep 2026 – Oct 2027)** that moves property payments onto an OPERA Cloud–integrated, tokenized platform. Its own scope names per-country "acquiring" and "local payment methods" as constraints, and no vendor is publicly named. A global gateway brand standard (FreedomPay, 2019) already exists. No third-party orchestrator was found, and the hotel, not Marriott, is most likely merchant of record for most volume. The motion is therefore **in-house**: argue per-country acquiring reach and local-method coverage inside a programme they are already running, never the case for orchestration itself.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** Path 1 — **SimilarWeb (supplied 2026-10-19)**, `accounts/traffic/marriott-international.md`. Sales Intelligence view, Jul–Sep 2026, marriott.com only, desktop + mobile web.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | United States | 66.96% | ~47.73M `[DERIVED from supplied share, not a SimilarWeb figure]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | Canada | 5.14% | ~3.66M `[DERIVED]` | Not supplied | same |
| 3 | **India** ⭐ high priority | 4.32% | ~3.08M `[DERIVED]` | Not supplied | same |
| 4 | **Japan** | 2.75% | ~1.96M `[DERIVED]` | Not supplied | same |
| 5 | United Kingdom | 2.41% | ~1.72M `[DERIVED]` | Not supplied | same |
| 6 | Mexico | 1.74% | ~1.24M `[DERIVED]` | Not supplied | same |
| 7 | **Australia** | 1.43% | ~1.02M `[DERIVED]` | Not supplied | same |
| 8 | United Arab Emirates *(EMEA)* | 1.05% | ~0.75M `[DERIVED]` | Not supplied | same |
| 9 | Germany | 1.01% | ~0.72M `[DERIVED]` | Not supplied | same |
| 10 | **Indonesia** | 0.91% | ~0.65M `[DERIVED]` | Not supplied | same |

Derived visits = share × 71.28M avg monthly visits. Top 10 = 87.72% of traffic. Device split: Desktop 43.81% / Mobile web 56.19%. Global rank not captured.

**Caveats from the supplied file (carried verbatim in substance):**
1. Sales Intelligence view: top 10 countries and share only. Per-country visit counts were **not** supplied, so the column above is derived.
2. Single domain only. **marriott.com.cn is not included**, so Greater China, Marriott's largest APAC segment by rooms, is invisible in this split.
3. **Bonvoy app traffic is excluded.**
4. App bookings and on-property (folio/POS) payments are not web traffic, so **web data understates payment volume**. Use it as a market-mix signal only.

Only India exceeds 5% among APAC markets. No top-10 APAC market lacks a local entity (Section 2).

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Bethesda, Maryland, USA (FY2025 10-K). APEC run from Singapore: the APEC results release is datelined "SINGAPORE" and the APEC CDO is "based in Singapore" per the 10-K. Hong Kong was historically the Asia Pacific development base (10-K bio). A Marriott Tech Accelerator (first global capability centre) in Hyderabad was announced 4 Oct 2024, supported by ANSR — https://www.hospitalitynet.org/news/4123974.html (agent-sourced).

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| India | Marriott Hotels India Private Limited; Bonvoy Hotels & Resorts India Private Limited; Starwood India Private Limited | Not found | [Exhibit 21](https://www.sec.gov/Archives/edgar/data/1048286/000104828626000007/mar-2025q4xexx21.htm) |
| Japan | Luxury Hotels International of Japan, Inc.; Japan Hotel Management Company; Japan Hospitality Service Company; Starwood Hotels Japan Company; The JW Marriott Hotel Management Company (Tokyo) Ltd.; The Ritz-Carlton Property Management Company (Tokyo / Kyoto); Osaka St. Regis Hotel Co., Ltd.; Tokyo / Yokohama / Nara Hospitality Service Company | Not found | Exhibit 21 |
| Australia | Marriott International Management Company B.V. (Australian Branch); Starwood Australia Hotels Pty Ltd; Starwood Pacific Hotels Pty Limited; Sheraton on the Park Pty Ltd | Not found | Exhibit 21 |
| Indonesia | PT Marriott International Indonesia; PT Luxury Hotels International Indonesia; PT Ritz Carlton Indonesia; PT Indo Pacific Sheraton | Not found | Exhibit 21 |
| Singapore | Starwood Asia Pacific Hotels & Resorts Pte. Ltd.; Starwood Customer Contact Centre (AP) Pte. Ltd.; The Ritz-Carlton Hotel Company of Singapore Pte Ltd; International Luxury Hotels (Singapore) Pte. Limited; Design Hotels PTE. LTD.; others | Not found | Exhibit 21 |
| Hong Kong | Marriott Hong Kong Limited; Luxury Hotels International of Hong Kong Limited; Luxury Hotels (China) International Management of Hong Kong Limited; Starwood Holdings (HK) Limited; others | Not found | Exhibit 21 |
| China | Starwood Hotels & Resorts (Shanghai) Co., Ltd. (Beijing, Guangzhou branches); Shanghai Gingerroot Enterprise Management Co., Ltd.; Guangzhou Starwood Customer Contact Centre Co., Ltd.; others | Not found | Exhibit 21 |
| Thailand | Luxury Hotels & Resorts (Thailand) Limited; Starwood Hotels (Thailand) Company Limited | Not found | Exhibit 21 |
| Malaysia, Vietnam, South Korea, Taiwan, Philippines, NZ, Cambodia, Maldives | Branches or local companies (agent summary) | Not found | Exhibit 21 |

Entities in this list are mostly **management / service companies**. Hotels are typically owned by third parties, who are separate legal entities and are very likely the merchants for on-property payments `[INFERENCE, not confirmed]`.

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| India | Yes (#3) | ✅ | Not verified this run | Low on entity grounds. Whether *marriott.com* prepaid INR payments are acquired domestically is unknown |
| Japan | Yes (#4) | ✅ | Not verified | Low on entity grounds; e-com acquirer unknown |
| Australia | Yes (#7) | ✅ (branch of Dutch B.V. + Pty Ltds) | Not verified | Low on entity grounds |
| Indonesia | Yes (#10) | ✅ | Not verified | Low on entity grounds |
| Greater China | Not in data (separate domain) | ✅ | Not verified | Unknown |

**No top-5 APAC traffic market lacks a confirmed entity.** The cross-border question for Marriott is not "do they have an entity" but **"which entity is the merchant for central prepaid bookings"**. The marriott.com terms that would answer it are bot-walled.

> **MANUAL:** Open marriott.com from a real browser in IN/JP/ID/AU locales, book an "Advance Purchase / Prepay" rate to the payment step, and read the card statement descriptor and the rate terms for the charging entity. That one fact decides whether the central CNP volume is Marriott's or the hotel's.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Global (US/CA first, then "other global regions") | **FreedomPay**, commerce platform / gateway brand standard (Nov 2019) | [Press Release] — verified by me | https://corporate.freedompay.com/press-release/freedompay-announces-an-agreement-with-marriott-international-for-commerce-technology-innovation/ |
| EMEA | FreedomPay described as "Marriott's global payment brand standard gateway" in a London job ad (2026) | [Job Listing] `[UNVERIFIED — search summary only; page 404]` | https://careers.marriott.com/manager-payment-solutions-12-month-ftc/job/5232912101E798BA229FA648D92BC9A8 |
| US & Canada | Chase Paymentech, credit card processor for all US & Canada hotels (2015) | [Press Release] (owner hub) `[UNVERIFIED — search summary only]` | https://ofhub.marriott.com/2015/02/marriotts-transition-to-new-credit-card-processor-begins-april-1/ |
| US (legacy) | Elavon and MerchantLink/Shift4 gateways, replaced by FreedomPay (2019) | [Press Release] (owner hub) `[UNVERIFIED — search summary only]` | https://ofhub.marriott.com/2019/11/guidance-regarding-merchantlink-shift4-migration-requirement/ |
| Greater China → Asia | **Alipay**: 10 Greater China hotels in Sep 2015, with discounts for Marriott.com / Marriott.com.cn bookings paid with Alipay; rollout planned across Asia | [Press Release] (fetched by agent) | https://www.journaldespalaces.com/en/pressrelease-46308-marriott-international-welcomes-chinese-travelers-with-alipay.html |
| China | Alipay on the Marriott storefront on Fliggy (Alibaba JV, 2017) | [Third-Party Report] (Skift 2019, fetched by agent) | https://skift.com/2019/07/29/marriotts-alibaba-joint-venture-in-china-is-part-of-its-direct-booking-strategy/ |
| APEC, HK, Macau, TW | New OPERA Cloud–integrated tokenized payment solution, **vendor not named** | [Job Listing] — verified by me | https://builtinsingapore.com/job/senior-manager-d-tt-payments-specialist/10496234 |
| Global | Oracle OPERA Cloud PMS (not a PSP; the integration target) | [Press Release] | https://www.oracle.com/news/announcement/oracle-cloud-to-help-elevate-property-management-for-marriott-international-2024-01-30 |
| Global | Amadeus Central Reservations System replacing Marriott's in-house CRS (2021–22; no go-live date found) | [Press Release] `[UNVERIFIED — search summary only]` | https://amadeus.com/en/newsroom/press-releases/marriott-international-to-deploy-transformative-crs-solution |

**Searched, nothing found for Marriott:**
- Global: Adyen, Stripe, Checkout.com, Braintree/PayPal, Cybersource, Worldpay/FIS, Global Payments, Nuvei, Fiserv, Planet.
- APAC: Razorpay, PayU, CCAvenue, BillDesk, Juspay, 2C2P, Xendit, Midtrans, Alipay+, Tyro, Windcave.
- Not searched (budget): GMO, SB Payment, Veritrans, iPay88, Omise, eWAY, Sabre/SynXis.
- 🚩 help.marriott.com's CSP header allow-lists js.stripe.com, PayPal SDK and checkoutshopper-live.adyen.com. **That is Salesforce Experience Cloud boilerplate, not evidence of checkout PSPs. Do not cite it.**

**Biggest gap:** the e-commerce acquirer for marriott.com, marriott.com.cn and the Bonvoy app. **Not found.**

#### 3B. Payment Orchestrator

**Classification: In-house orchestration layer (inferred).**
- **FreedomPay** is the centrally mandated gateway brand standard (verified, 2019).
- An internal **"Integrated Payment Gateway and Tokenization"** programme is migrating properties in waves across APEC, HK, Macau and Taiwan (verified job ad). Greater China is covered too, per an unverified listing.
- No third-party orchestrator was found: Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY, VGS, TokenEx and Yuno all returned nothing for Marriott. A "TokenEx" string match on marriott.com.cn was a false positive (`userIdTokenExpiresIn`).
- `[INFERENCE, not confirmed]`: no source uses the word "orchestration" for Marriott.

> *"The company runs its own centrally mandated payment standard. The opening is not the case for orchestration. It is per-country acquiring and local-method coverage that a single global gateway standard was not built to provide in markets like India, Indonesia and Japan, which the programme's own scope flags."*

> **MANUAL:** Walk a marriott.com prepaid booking with DevTools in IN and JP locales and capture the payment-iframe domains. That would identify the e-commerce PSP in one session.

---

### Section 4: Alternative & Local Payment Methods

**The marriott.com checkout and help centre were not readable in this environment.** marriott.com returns an Akamai 403; help.marriott.com is a client-rendered Salesforce app. Every "Not found" below means **no evidence either way, not evidence of absence.**

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| Global | Visa / MC / Amex / Discover / JCB / Diners online | Cards | Unknown, checkout not accessible | — |
| Global | UnionPay (guarantee bookings on official site and Bonvoy app; HK/Macau offer 15 Jun 2026 – 30 Jun 2027) | Cards | Mentioned in docs (UnionPay Intl) | https://m.unionpayintl.com/cardholderServ/serviceCenter/wap/merchant/117682348135?type=1 |
| Global | PayPal | Digital wallet | Not found (only a co-brand card earn offer) | — |
| Global | Apple Pay | Digital wallet | Mentioned in press, 2015, front-desk contactless only. Online/app: Not found | https://www.journaldespalaces.com/en/pressrelease-45155-apple-pay-checks-in-to-marriott-first-hotel-company-to-offer-the-service-to-its-guests.html `[UNVERIFIED]` |
| Global | Google Pay | Digital wallet | Not found | — |
| Global | Affirm / Klarna / Uplift | BNPL/Instalments | Not found | — |
| Global | Prepaid "Advance Purchase" vs pay-at-hotel card guarantee | Payment timing | Mentioned in press | https://upgradedpoints.com/how-to-cancel-a-marriott-hotel-reservation `[UNVERIFIED]` |
| India | UPI, RuPay, netbanking, Paytm/PhonePe, EMI | Bank transfer / A2A, Cards, Wallets, Instalments | Not found | — |
| India | Marriott Bonvoy HDFC Bank Credit Card (Diners Club, Aug 2023) | Cards (co-brand) | Mentioned in press | https://news.marriott.com/news/2023/08/24/hdfc-bank-joins-hands-with-marriott-bonvoy-to-launch-indias-first-co-brand-hotel-credit-card |
| Japan | konbini, PayPay, instalments | Cash/voucher, Wallet, Instalments | Not found | — |
| Japan | Marriott Bonvoy American Express (Feb 2022; enhanced Aug 2025) | Cards (co-brand) | Mentioned in press | https://news.marriott.com/news/2022/02/09/marriott-bonvoy-and-american-express-launch-new-cobrand-credit-cards-in-japan |
| Australia | Afterpay, Zip, PayTo | BNPL, Direct debit / A2A | Not found | — |
| Indonesia | QRIS, GoPay, OVO, DANA, virtual account | Wallet, Bank transfer | Not found | — |
| China | Alipay (Marriott.com / .cn, 2015; Fliggy storefront) | Digital wallet | Mentioned in press. Current online checkout status unknown; marriott.com.cn homepage has no Alipay string | Section 3A URLs |
| China | WeChat Pay | Digital wallet | Not found as a payment method (WeChat used for social and mini-program only) | https://www.marriott.com.cn/ (homepage fetched by agent) |

No "Warning: [Method] not supported" statement is made for any market: the absence is unsourced.

> **MANUAL:** VPN-check the prepaid checkout for India (UPI/RuPay/EMI), Japan (konbini/PayPay/JCB) and Indonesia (QRIS/VA). This is the single highest-value manual step: a confirmed India UPI gap would add +3 and give the strongest opener.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Slow / refused refund ($430) | Trustpilot (marriottbonvoy.com, TrustScore 1.3, 437 reviews) | Isolated (verified) | 26 Sep 2026 | https://trustpilot.com/review/marriottbonvoy.com (fetched by agent) |
| Multiple pending authorization holds (~$4,400) | Trustpilot | Isolated | 29 Aug 2026 | same (fetched by agent) |
| Duplicate charge after bill paid | Trustpilot (NO) | Isolated | Sep 2025 | https://no.trustpilot.com/reviews/68bf0110cc75973ea6ff5ba7 `[UNVERIFIED]` |
| Currency conversion: prepaid rate converted at inflated FX by the hotel | LoyaltyLobby | Moderate (recurring theme, non-APAC) | Apr 2026 | https://loyaltylobby.com/2026/04/15/reader-email-artificially-inflated-exchange-rate-at-the-artisan-d-c-hotel-autograph-collection-in-bogota/ `[UNVERIFIED]` |
| Currency conversion: DCC on prepayment (~9% extra) | LoyaltyLobby | Moderate (pattern) | Jul 2021 | https://loyaltylobby.com/2021/07/21/reader-email-another-marriott-scam-in-greece-hotel-processes-prepayment-using-dcc/ `[UNVERIFIED]` |
| Currency conversion: franchisees set own conversion rules (incl. a Dhaka card-rate markup mention) | OMAAT / LoyaltyLobby | Moderate | 2021–2023 | https://loyaltylobby.com/2021/01/25/marriotts-corporate-response-to-property-level-payment-scams/ `[UNVERIFIED]` |
| Declined transactions: Mastercard / Diners reportedly not accepted on Bonvoy (India) | TechnoFino forum | Isolated, anecdotal | Undated | https://technofino.in/community/goto/post?id=1197100 `[UNVERIFIED]` |

> *Pattern of hotel-level FX/DCC markups on prepaid rates, which Marriott attributes to franchisee rules, suggests the prepaid charge is often run by the property, not centrally. That matches the merchant-of-record inference. It also shows Marriott has no central control of currency presentation at settlement, but the evidence is mostly non-APAC.*

No Reddit, App Store or Google Play payment complaints surfaced. No UPI- or Japan-specific complaints were found.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | Aug 2026 (posting removed 28 Aug; project Sep 2026 – Oct 2027) | APAC payments re-platform to OPERA Cloud–integrated tokenized solution; scope covers acquiring + local payment methods per country | Payment Infrastructure Hiring | https://builtinsingapore.com/job/senior-manager-d-tt-payments-specialist/10496234 |
| 2 | 24 Jun 2026 | Strategic agreement with CG Hospitality Global for Series by Marriott in Greater China, ~100 hotels over 10 years | Market Expansion | https://gdeltcloud.com/events/marriott-and-cg-hospitality-global-sign-strategic-agreement--cameoplus_ea023b94 `[UNVERIFIED — single aggregator]` |
| 3 | 12 Feb 2026 | APEC 2025: 187 organic deals (+32%), 109 openings, 730+ properties in 22 countries, India record 99 deals / 12,000+ rooms, Series by Marriott converted 26 India hotels in a day | Market Expansion | https://www.aap.com.au/aapreleases/cision20260211ae85567 |
| 4 | 10 Dec 2025 | City Express by Marriott enters Japan (2 Osaka conversions, reopening 2026) | Market Expansion | https://www.aap.com.au/aapreleases/cision20251210ae43392 `[UNVERIFIED]` |
| 5 | 23 Jul 2025 | citizenM acquisition closed ($355M + up to $110M earn-out; 37 hotels incl. APAC) | M&A | https://marriott.gcs-web.com/news-releases/news-release-details/marriott-international-completes-acquisition-citizenm-brand `[UNVERIFIED]` |

- **No public payment-related RFP found.**
- Payment hiring: Singapore role (verified). Shanghai "Senior Manager, Payment Solutions – GC" (unverified): https://militaryspouseconnection.dejobs.org/shanghai-chn/senior-manager-payment-solutions-gc/5901424F1C0845CFA5DE3E0072D8D8F4/job
- The Hyderabad Tech Accelerator surfaced an application-security role, but **no payments role**.
- No 2025–26 change to APEC leadership was found; Rajeev Menon is still President APEC per the Feb 2026 release.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | Aug 2026 | APAC hotel payments transition to OPERA Cloud tokenized platform (job ad) | Live programme, vendor open in public record | https://builtinsingapore.com/job/senior-manager-d-tt-payments-specialist/10496234 |
| 2 | 30 Jan 2024 | Marriott selects Oracle OPERA Cloud PMS + Sales & Event Management | The integration target for the payment migration | https://www.oracle.com/news/announcement/oracle-cloud-to-help-elevate-property-management-for-marriott-international-2024-01-30 |
| 3 | 24 Aug 2023 | Marriott Bonvoy HDFC Bank Credit Card, India's first co-brand hotel card, on Diners Club | India payments partnership; Diners acceptance question | https://news.marriott.com/news/2023/08/24/hdfc-bank-joins-hands-with-marriott-bonvoy-to-launch-indias-first-co-brand-hotel-credit-card |
| 4 | 12 Nov 2019 | FreedomPay agreement, portfolio-wide commerce platform | Incumbent gateway standard | https://corporate.freedompay.com/press-release/freedompay-announces-an-agreement-with-marriott-international-for-commerce-technology-innovation/ |
| 5 | Sep 2015 | Alipay at Greater China hotels and Marriott.com / .cn bookings | China APM, dated | https://www.journaldespalaces.com/en/pressrelease-46308-marriott-international-welcomes-chinese-travelers-with-alipay.html |

No provider removals found. (FreedomPay replaced Elavon / MerchantLink as the US gateway in 2019, per unverified owner-hub snippets.)

---

### Section 8: Checkout Experience Audit

**Not accessible in this environment.** www.marriott.com returns an Akamai "Access Denied" 403 to both WebFetch and curl. This is an origin-side bot wall: other sites fetched normally in the same session. help.marriott.com renders client-side. Only the marriott.com.cn homepage was readable; it contains no payment SDK or PSP domains, and payment scripts would load in the booking flow, which was not reached.

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| All 13 dimensions | Not accessible | — | Manual browser walkthrough required |
| Card validation at booking | $0 auth (Visa/MC/Discover) or $1 auth (Amex) on marriott.com and app (2017 owner-hub notice) | — | `[UNVERIFIED — search summary only]` https://ofhub.marriott.com/2017/07/payment-validation-at-time-of-booking |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found (no public AoC or statement) | — |
| Card data handling | Not found for e-commerce. POS tokenization made a brand standard in 2014 to take card data out of PCI scope `[UNVERIFIED — snippet]` | https://ofhub.marriott.com/2014/08/global-point-of-sale-to-become-brand-standard |
| Security regulatory context | FTC 20-year consent order + US$52M settlement with 49 states and DC (9 Oct 2024) over 2014–2020 breaches: mandated security programme, biennial third-party assessments, risk assessments of critical IT vendors. UK ICO £18.4M GDPR fine (Oct 2020) for the Starwood breach | https://perkinscoie.com/insights/blog/ftc-and-state-coalition-settle-data-breach-cases-marriott ; https://loyaltylobby.com/2020/10/30/uk-ico-fines-marriott-18-4m-for-starwood-data-breach/ |
| Recommended Yuno integration | Back-to-back API with Marriott's existing token scheme, or SDK on marriott.com prepaid. Undetermined until the e-com PSP is known | — |

*"No direct PCI compliance documentation found publicly for Marriott International."* The 2024 FTC order makes **vendor risk assessment** a formal gate for any new payments vendor, so expect a long security review. That cost is real, but tokenization and PCI-scope reduction are also a credible angle with them.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: The APAC payments programme already lists Yuno's problem set in its scope**
> **Evidence:** S6/S7 — the Singapore job ad names *"country/property-specific constraints (legal, acquiring, local payment methods…)"* across a *"multi-hotel, multi-country environment"*, Sep 2026 – Oct 2027. S2 — Marriott has entities in 20+ APAC countries. S3A — the only named gateway standard (FreedomPay) dates from a 2019 US/CA-first agreement.
> **Pain Point:** One global gateway standard has to be reconciled with a different acquiring answer and a different local-method set in each of 22 APEC countries, with each property's configuration (integrated / hybrid / standalone) different.
> **Yuno Value Proposition:** One integration that exposes local acquirers and local methods per country behind a single token and reporting layer, so the per-country answer becomes configuration rather than a new integration.
> **Best Success Case:** Not verified. Pick a multi-country travel case from the current library.
> **Outreach Angle:** "Your APAC payments transition lists acquiring and local methods as per-country constraints. Those are the two things a single global gateway doesn't solve market by market."
> **Suggested Subject Line:** "Acquiring by country in the OPERA Cloud move"

> **Insight #2: India is Marriott's fastest-growing APAC market and the #3 traffic market, and its local-rail coverage is unknown**
> **Evidence:** S1 — India 4.32%, #3 globally and #1 in APAC. S6 — record 99 India signings in 2025, 26 hotels converted to Series by Marriott in a day. S4 — UPI/RuPay/EMI coverage on marriott.com unverifiable. S7 — the India co-brand card runs on Diners Club.
> **Pain Point:** A fast-growing, increasingly midscale India estate (Series by Marriott) means more domestic leisure guests who default to local rails, not international cards. `[INFERENCE, not confirmed]`
> **Yuno Value Proposition:** Local Indian methods and domestic acquiring through one connection. **Only usable once the UPI gap is confirmed manually.**
> **Outreach Angle:** Lead with the 99 India signings, then ask how domestic guests pay on prepaid rates. Ask; don't assert.
> **Suggested Subject Line:** "99 India signings — and how those guests pay"

> **Insight #3: Card-present is where the programme is; card-not-present is where Yuno fits — find the CNP owner**
> **Evidence:** S3A — the job ad covers pin pads, server software and PMS integration. S2 / 10-K — <1% owned, so hotels most likely take payment. S5 — FX/DCC complaints show prepaid charges are often run at the property.
> **Pain Point:** Prepaid central bookings settled by thousands of property merchant accounts produce inconsistent currency presentation, DCC disputes and refund friction that Marriott's brand takes the blame for (S5).
> **Yuno Value Proposition:** Central CNP collection with local acquiring and consistent currency presentation, *if* Marriott wants to centralise prepaid collection.
> **Outreach Angle:** Discovery question, not a claim: "Who is the merchant on an Advance Purchase booking in Jakarta?"
> **Suggested Subject Line:** "Who settles a prepaid booking in Jakarta?"

> **Insight #4: A peer group running regional orchestration**
> **Evidence:** S11C — Radisson put CellPoint's full orchestration platform across EMEA and APAC (2022); Agoda uses Juspay for local methods `[UNVERIFIED]`. S3B — Marriott runs a single-gateway in-house standard.
> **Pain Point:** Competitors and OTAs that route by country capture local-method bookings Marriott direct may not, while Marriott pushes direct booking (68% of room nights from Bonvoy members, S12).
> **Outreach Angle:** Use peer orchestration only as context. **Never name Radisson or Agoda** in outreach (never-name-competitors rule).
> **Suggested Subject Line:** "Direct booking share vs local payment methods"

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks:**
1. Your APAC payments transition (Sep 2026 – Oct 2027) lists acquiring and local payment methods as constraints that vary by country. That is exactly the layer we sit in.
2. 99 India signings in 2025 and 26 hotels converted in a single day. How do domestic guests pay on prepaid rates once those hotels are on OPERA Cloud?
3. Moving 22 APEC countries to one tokenized platform still leaves a different acquiring answer in each market. Happy to share how we've seen that solved without a new integration per country.

**Cold call openers:**
1. "I saw Marriott's APAC payments transition to OPERA Cloud. Is local acquiring part of that scope, or just the terminals?"
2. "With India now your biggest signing market in APAC, are prepaid bookings there settled by Marriott or by each hotel?"
3. "When you move hotels in Indonesia and Japan to the new tokenized platform, who decides which local methods are switched on?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| IHG | ihg.com | UK | ~6,668 hotels / 986,633 rooms (31 Mar 2025) | Greater China, Japan, India, AU, SEA | FreedomPay (about 4,000 US/CA hotels, Jun 2023 — verified); no APAC stack found | https://corporate.freedompay.com/about-us/press-release/ihg-hotels-resorts-taps-freedompay-to-transform-commerce-technology |
| Hilton | hilton.com | USA | Not verified | All APAC | Not found | — |
| Hyatt | hyatt.com | USA | 1,528 hotels / 372,763 rooms (YE2025) | Greater China, Japan, India, SEA, AU | Not found (Onyx GroupPay is commissions, not guest PSP) | https://www.sec.gov/Archives/edgar/data/1468174/000146817426000007/h-20251231.htm |
| Accor | accor.com | France | Not verified | AU, SEA, Greater China, India, Japan | Group PSP not confirmed (Adyen testimonial from Raffles Singapore only) `[UNVERIFIED]` | https://www.adyen.com/en_SG/industries/hospitality |
| Wyndham | wyndhamhotels.com | USA | 855,400 rooms (30 Sep 2025) | China, India, SEA, AU | Not searched | https://www.sec.gov/Archives/edgar/data/1722684/000172268426000007/wh-20251231.htm |
| Minor Hotels | minorhotels.com | Thailand | 540+ hotels `[UNVERIFIED]` | TH, SEA, AU, Japan, India | 2C2P gateway (2019) `[UNVERIFIED]`; job ad benchmarking Stripe/Checkout.com/Juspay/Adyen `[UNVERIFIED]` | https://2c2p.com/case-studies/minor-hotels/ |
| IHCL (Taj) | ihcltata.com | India | Not verified | India | TAL says Juspay — **not confirmed by web search** | TAL only |

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Agoda | agoda.com | OTA | APAC | Juspay (Hyperswitch) for local methods with failover; Checkout.com acquiring `[UNVERIFIED]` | https://hyperswitch.io/case-studies/agoda/ |
| Trip.com | trip.com | OTA | Greater China, global | Checkout.com partnership (Mar 2026) for local acquiring and 3DS `[UNVERIFIED]` | https://checkout.com/newsroom/trip-com-teams-up-with-checkout-com-to-simplify-payments-for-global-travelers |
| Traveloka | traveloka.com | OTA | SEA | Cybersource gateway + tokenization `[UNVERIFIED]` | https://partners.visaacceptance.com/en-ap/case-studies/traveloka.html |
| MakeMyTrip | makemytrip.com | OTA | India | Juspay (TAL; weak web source) | https://wellfound.com/company/juspay |
| Radisson Hotel Group | radissonhotels.com | Hotels | EMEA, APAC | CellPoint orchestration (verified) | https://cellpointdigital.com/articles/pressReleases/cellpoint-digital-partners-with-radisson-hotel-group |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| Radisson Hotel Group | CellPoint Digital | 2022-09-06 | Hotels (EMEA + APAC) | https://cellpointdigital.com/articles/pressReleases/cellpoint-digital-partners-with-radisson-hotel-group |
| Agoda | Juspay (Hyperswitch) | Undated | OTA | https://hyperswitch.io/case-studies/agoda/ `[UNVERIFIED]` |
| RateGain (RG Pay) | Juspay | Undated | Hotel distribution tech | https://www.zawya.com/en/press-release/companies-news/rategain-and-juspay-partner-to-power-rg-pay-e5s4g7up `[UNVERIFIED]` |

#### 11D. Prospect Scoring

Not scored in full. Competitor signals beyond the stack findings above (traffic splits, transaction counts, complaints) were not researched, and scoring them on the available signals would mostly be zeros marked ⬜. Indicative only:

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| IHG — multiple PSPs / orchestration | ⬜ | FreedomPay only (US/CA) | 11A |
| Minor Hotels — PSP evaluation hiring | ⬜ | Unverified job ad | 11A |
| Hyatt / Hilton / Accor | ⬜ | No stack evidence | 11A |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | IHG | Competitor | Greater China, Japan, India, AU | Not scored | Investigate | FreedomPay = same gateway pattern as Marriott | **No — genuine find** |
| 2 | Hilton | Competitor | All APAC | Not scored | Investigate | Scale; no stack found | **No — genuine find** |
| 3 | Hyatt | Competitor | Greater China, Japan, India | Not scored | Investigate | Scale; no stack found | **No — genuine find** |
| 4 | Accor | Competitor | AU, SEA | Not scored | Investigate | Largest APAC footprint of the Western groups `[INFERENCE]` | **No — genuine find** |
| 5 | Wyndham | Competitor | China, India | Not scored | Investigate | Midscale franchise | No |
| 6 | IHCL (Taj) | Competitor | India | Not scored | Medium | TAL lists Juspay (displacement) | Yes |
| 7 | Minor Hotels | Competitor | TH, SEA | — | **Do not contact (TAL)** | PSP benchmarking job | Yes |
| 8 | H World | Competitor | China | Not scored | Low | China access | Yes |
| 9 | Agoda | OTA | APAC | — | Likely out (Juspay incumbent) | Orchestrated | No |
| 10 | Trip.com | OTA | Greater China | Not scored | Low | "In-house routing" (TAL) + Checkout.com | Yes |

Note: TAL has Traveloka's HQ as "India" (wrong — Indonesia) and Shangri-La categorised as an OTA. Worth correcting in the TAL.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | US$26,186M (FY2025); of which gross fees US$5,438M, cost reimbursements US$19,204M | FY2025 10-K (verified) |
| APAC segment revenue | APEC US$1,073M (gross fees US$376M); Greater China US$590M (gross fees US$261M) | FY2025 10-K Note 14 (agent-sourced) |
| GMV / Gross Transaction Volume | Not disclosed. Indicative APEC system room revenue ≈ 157,326 rooms × 365 × RevPAR US$133.12 ≈ **US$7.6bn/yr** `[DERIVED from 10-K inputs; room revenue only, not Marriott revenue]` | Calculated |
| Average Transaction Value (USD) | ADR APEC US$184.36; Greater China US$114.20; worldwide US$185.81 (FY2025). Per **room night**, not per folio | FY2025 10-K (APEC verified) |
| Est. Annual Transactions | ~41M room nights/yr in APEC (157,326 × 72.2% × 365) | Calculated |
| **Monthly transaction count** | ✅ **DERIVED: ~3.45M room nights/month (APEC only)**, = 157,326 rooms × 72.2% occupancy × 30.4. Both inputs from the FY2025 10-K. Greater China adds ~3.84M (188,596 × 67.0% × 30.4). **Billing unit: room nights.** Folios are fewer, but staying under 100k/month would need a >34-night average stay. ⚠️ **Whose transactions:** system-wide, mostly card-present, very likely settled by the hotel owner as merchant. **Marriott's own CNP count (prepaid web / app) is NOT FOUND.** | See ICP disclosure |
| Active Customers / Users | Marriott Bonvoy "more than 295 million" members (30 Jun 2026); 68% of global room nights booked by members (FY2025) | Q2 2026 earnings release (agent-sourced); 10-K (verified) |
| Primary Currency | USD (reporting) | 10-K |
| Top 3 Markets by Revenue | Not disclosed by country. US & Canada is the largest segment | 10-K |
| Billing channel split (web vs app store) | N/A. Not a subscription business; app-store IAP not relevant. Web vs Bonvoy app booking split: Not found | — |
| Co-brand card economics | Bonvoy co-brand cards in 11 countries; co-brand and other fees added US$105M to FY2025 franchise fees | 10-K |

---

### Overall Research Confidence

**Medium.**
- **Strong:** corporate structure, entities, scale and APAC footprint (SEC filings, verified by me); the APAC payments programme (verified job ad); FreedomPay standard (verified press release); peer orchestration (Radisson, verified).
- **Weak:** the e-commerce payment stack. marriott.com is behind an Akamai bot wall, so the checkout, APMs, PSP iframes, T&Cs and the merchant entity for prepaid rates could not be read. Section 8 is not completed, and Section 4 is entirely "not found either way". Overall confidence would be Medium-High without the bot wall, so it is downgraded one level for this.
- **Traffic data was supplied** (SimilarWeb Sales Intelligence, 2026-10-19), not estimated. It is marriott.com only: it excludes marriott.com.cn and app traffic, and per-country visits are derived from share. The Greater China profile is therefore unverified.

---

### Manual Research Recommendations

> **Area:** Merchant of record for prepaid central bookings (S2, S3, S12)
> **Why it matters:** It decides whether the orchestratable CNP volume belongs to Marriott at all. This is the condition for re-escalating to ⭐.
> **Suggested manual action:** Book (and cancel) an Advance Purchase rate at an APAC property from a real browser; read the payment-step legal text and statement descriptor.

> **Area:** Monthly transaction count — Marriott-controlled CNP volume (S12)
> **Why it matters:** The +5 band is system-wide; the central CNP count is unknown.
> **Suggested manual action:** Discovery-call question: "What share of APAC room revenue is prepaid on marriott.com or the app, and who settles it?"

> **Area:** India / Japan / Indonesia local methods (S4)
> **Why it matters:** A confirmed UPI gap in India (#3 market) adds +3 and is the best opener.
> **Suggested manual action:** VPN to IN, JP and ID, go to the prepaid payment step, screenshot the methods offered, and capture payment-iframe domains in DevTools.

> **Area:** Vendor for the APAC OPERA Cloud payment programme (S3, S6)
> **Why it matters:** If FreedomPay is already committed for APAC, the window is narrower.
> **Suggested manual action:** LinkedIn: find who holds the Singapore "D+TT Payments Specialist" role and the APEC Digital & Technology payments lead. Check FreedomPay / OPERA Cloud payments announcements for APAC.

> **Area:** Yuno success case (S10)
> **Why it matters:** No hospitality case was verified.
> **Suggested manual action:** Pull the current travel/hospitality case from Yuno's internal library.

---

### Appendix: All Source URLs

**Traffic:** `accounts/traffic/marriott-international.md` (SimilarWeb, supplied 2026-10-19)

**Section 2 / 12 (filings):**
- https://www.sec.gov/Archives/edgar/data/1048286/000104828626000007/mar-20251231.htm
- https://www.sec.gov/Archives/edgar/data/1048286/000104828626000007/mar-2025q4xexx21.htm
- https://www.sec.gov/Archives/edgar/data/1048286/000104828626000035/mar-20260630.htm
- https://www.sec.gov/Archives/edgar/data/1048286/000104828626000033/mar-2026q2xex99earningsrel.htm
- https://www.hospitalitynet.org/news/4123974.html

**Section 3:**
- https://corporate.freedompay.com/press-release/freedompay-announces-an-agreement-with-marriott-international-for-commerce-technology-innovation/
- https://careers.marriott.com/manager-payment-solutions-12-month-ftc/job/5232912101E798BA229FA648D92BC9A8
- https://ofhub.marriott.com/2015/02/marriotts-transition-to-new-credit-card-processor-begins-april-1/
- https://ofhub.marriott.com/2019/11/guidance-regarding-merchantlink-shift4-migration-requirement/
- https://ofhub.marriott.com/2014/08/global-point-of-sale-to-become-brand-standard
- https://ofhub.marriott.com/2017/07/payment-validation-at-time-of-booking
- https://www.journaldespalaces.com/en/pressrelease-46308-marriott-international-welcomes-chinese-travelers-with-alipay.html
- https://skift.com/2019/07/29/marriotts-alibaba-joint-venture-in-china-is-part-of-its-direct-booking-strategy/
- https://www.oracle.com/news/announcement/oracle-cloud-to-help-elevate-property-management-for-marriott-international-2024-01-30
- https://amadeus.com/en/newsroom/press-releases/marriott-international-to-deploy-transformative-crs-solution
- https://militaryspouseconnection.dejobs.org/shanghai-chn/senior-manager-payment-solutions-gc/5901424F1C0845CFA5DE3E0072D8D8F4/job

**Section 4:**
- https://m.unionpayintl.com/cardholderServ/serviceCenter/wap/merchant/117682348135?type=1
- https://www.journaldespalaces.com/en/pressrelease-45155-apple-pay-checks-in-to-marriott-first-hotel-company-to-offer-the-service-to-its-guests.html
- https://upgradedpoints.com/how-to-cancel-a-marriott-hotel-reservation
- https://news.marriott.com/news/2023/08/24/hdfc-bank-joins-hands-with-marriott-bonvoy-to-launch-indias-first-co-brand-hotel-credit-card
- https://news.marriott.com/news/2022/02/09/marriott-bonvoy-and-american-express-launch-new-cobrand-credit-cards-in-japan
- https://www.marriott.com.cn/

**Section 5:**
- https://trustpilot.com/review/marriottbonvoy.com
- https://no.trustpilot.com/reviews/68bf0110cc75973ea6ff5ba7
- https://loyaltylobby.com/2026/04/15/reader-email-artificially-inflated-exchange-rate-at-the-artisan-d-c-hotel-autograph-collection-in-bogota/
- https://loyaltylobby.com/2021/07/21/reader-email-another-marriott-scam-in-greece-hotel-processes-prepayment-using-dcc/
- https://loyaltylobby.com/2021/01/25/marriotts-corporate-response-to-property-level-payment-scams/
- https://technofino.in/community/goto/post?id=1197100

**Section 6 / 7:**
- https://builtinsingapore.com/job/senior-manager-d-tt-payments-specialist/10496234
- https://www.aap.com.au/aapreleases/cision20260211ae85567
- https://www.aap.com.au/aapreleases/cision20251210ae43392
- https://gdeltcloud.com/events/marriott-and-cg-hospitality-global-sign-strategic-agreement--cameoplus_ea023b94
- https://marriott.gcs-web.com/news-releases/news-release-details/marriott-international-completes-acquisition-citizenm-brand

**Section 9:**
- https://perkinscoie.com/insights/blog/ftc-and-state-coalition-settle-data-breach-cases-marriott
- https://loyaltylobby.com/2020/10/30/uk-ico-fines-marriott-18-4m-for-starwood-data-breach/

**Section 11:**
- https://corporate.freedompay.com/about-us/press-release/ihg-hotels-resorts-taps-freedompay-to-transform-commerce-technology
- https://www.sec.gov/Archives/edgar/data/1468174/000146817426000007/h-20251231.htm
- https://www.adyen.com/en_SG/industries/hospitality
- https://www.sec.gov/Archives/edgar/data/1722684/000172268426000007/wh-20251231.htm
- https://2c2p.com/case-studies/minor-hotels/
- https://hyperswitch.io/case-studies/agoda/
- https://checkout.com/newsroom/trip-com-teams-up-with-checkout-com-to-simplify-payments-for-global-travelers
- https://partners.visaacceptance.com/en-ap/case-studies/traveloka.html
- https://wellfound.com/company/juspay
- https://cellpointdigital.com/articles/pressReleases/cellpoint-digital-partners-with-radisson-hotel-group
- https://www.zawya.com/en/press-release/companies-news/rategain-and-juspay-partner-to-power-rg-pay-e5s4g7up

</details>
