# Practo

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 13 / 29 → 🟢 Medium
**Industry:** Healthtech — doctor discovery, tele/in-clinic consultations, lab tests, surgeries, Practo Plus memberships, plus clinic/hospital SaaS (Ray, Insta) · **HQ:** Bengaluru, India — Practo Technologies Pvt Ltd; Singapore holdco Practo Pte. Ltd. (reverse flip to India announced, completion not confirmed) · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **Unresolved — treat as In-house / Razorpay-native until checkout is verified.** Razorpay (UPI Suite with Dynamic Routing + UPI Switch) is the only provider-confirmed PSP, and Practo's web checkout calls its own payments service. **The TAL's "Juspay" tag could not be confirmed anywhere** — do not open with Juspay displacement.

---

> # 🔒 PHASE 0 — QUALIFICATION GATE
>
> | Rule | Result |
> |---|---|
> | PSP / gateway / acquirer / orchestrator | **Does not fire.** Practo is a healthcare marketplace + provider SaaS. It runs a closed-loop wallet/credits (Practo Wallet, HealthCash) seen in its own front-end code, but no RBI PA/PPI licence or payments subsidiary was found. |
> | Existing Yuno customer | **No.** `https://y.uno/en` fetched 2026-10-19: zero occurrences of "practo". (The 4 "juspay" hits are Yuno's own "Yuno vs. Juspay" comparison page, not a relationship.) |
> | No online payment volume | Does not fire — paid teleconsults, lab tests, Practo Plus subscriptions. |
> | HQ west of Dubai | Does not fire — Bengaluru HQ. UAE traffic/launch is a market the company sells into, which keeps it in scope. |
> | Monthly transactions < 40,000 (sourced) | **Does not fire.** Sourced: ">100,000 teleconsultations a month" (Financial Express, 25 May 2026). See Section 12. |

> # ⚠️ METHOD NOTES — disclosed up front
>
> 1. **Traffic was supplied** (`accounts/traffic/practo.md`, Similarweb **Sales Intelligence**, pulled 2026-10-19, Jul–Sep 2026, practo.com only). Its caveats are carried through this report:
>    **(a)** only the top 10 countries are shown, share only — per-country visits below are `[DERIVED from supplied share, not a SimilarWeb figure]` (share × 9.107M avg monthly visits);
>    **(b)** single domain, so no cross-domain aggregation was needed (no regional Practo domains carry traffic; `/en-sg`, `/en-id`, `/en-ph` are legacy paths on practo.com);
>    **(c)** **mobile app traffic is excluded** — device split shown is desktop 13.69% / mobile web 86.31%;
>    **(d)** **Practo is app-heavy: web traffic was NOT used to size transactions or the 40k gate.** The country split is used as a market-mix signal only. The transaction figure in Section 12 comes from a sourced press quote.
> 2. **Fetch worked** (WebFetch and curl). Phase 2 agents ran in parallel with Agent 1 because supplied traffic already fixed the market list. Several high-value pages could not be read: Practo's T&Cs and privacy policy render client-side (no entity or PSP text in the HTML), the payment-method selector sits behind OTP login, and yourstory.com / arabianbusiness.com / theweek.in returned 403.
> 3. **WebSearch summaries are not sources.** Claims I could only see in a search summary are labelled `[UNVERIFIED — search summary only, page not fetched]`. Claims labelled verified were read on the page itself (by me or by an agent, via WebFetch/curl).

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Practo is a Bengaluru-based digital health platform — doctor discovery and booking, teleconsultations, lab tests, surgery coordination (Practo Care) and the Practo Plus membership — plus clinic and hospital software (Ray, Insta HMS) that the company says is now ~80% of revenue. It reported its first operating-EBITDA-positive year in FY25 (revenue ₹234 Cr, GMV ₹3,500 Cr), has pushed its IPO to 2027 while negotiating a $100–125M pre-IPO round, and has launched consumer services in the **UAE (May 2025)** and the **US (announced Jan 2026)**. Payments: Razorpay powers UPI ([Razorpay case study](https://razorpay.com/blog/practo-and-razorpay/)); no other PSP and no orchestrator could be confirmed.

**SimilarWeb total visits (last full month):** **~9.1 million / month** (Jul–Sep 2026 average; 27.32M over 3 months) — **supplied** 2026-10-19. Web only; the app, where most transactions happen, is excluded.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇮🇳 India | 87.17% (~7.94M/mo) | UPI (via Razorpay); credit/debit cards (bank-offer T&Cs, 2021); no-cost EMI on Practo Care surgeries; auto-debit on Practo Plus; Practo Wallet / HealthCash; insurance cashless (Plus); GPay/PhonePe/Paytm in-app mini-app channels (source code) | **Not confirmed either way** (checkout behind login): netbanking (third-party list only), third-party wallets, BNPL, card/cardless EMI on consults and lab tests. The **rail behind Plus auto-debit** (UPI Autopay / card mandate / e-NACH) is not identified. | ✅ Practo Technologies Pvt Ltd (CIN U72900KA2008PTC046374 / U72900TZ2008PTC038088 — registries disagree) |
| 2 | 🇺🇸 United States | 4.43% (~403k/mo) | **Not found** — no evidence of international cards, PayPal or wallet acceptance | Cannot be assessed: no US checkout found. No confirmed international acquirer. | ❌ None found |
| 3 | 🇦🇪 UAE | 1.23% (~112k/mo) | **Not found** — no AED checkout or UAE PSP identified | Cannot be assessed | ❌ None found (not checked whether local presence is required — see Section 2) |
| 4 | 🇬🇧 United Kingdom | 0.57% (~52k/mo) | Not researched (<1%) | — | ❌ None found |
| 5 | 🇵🇰 Pakistan | 0.50% (~46k/mo) | Not researched (<1%) | — | ❌ None found |

**Read this table with care.** India is 87% of web traffic and is where nearly all known payment volume runs. US and UAE traffic is small but sits on top of company-claimed GMV run-rates (US >$75M, UAE ₹100 Cr) with **no confirmed foreign entity and no confirmed non-INR acceptance**. That is the gap worth probing; it is not yet a confirmed gap.

### Legal entities
- **Practo Technologies Private Limited** (India, operating co.) — CIN **U72900KA2008PTC046374** (Infyner, Feb 2026) / **U72900TZ2008PTC038088** (Tofler, Oct 2026). The registries disagree; `[INFERENCE, not confirmed]` the registered office may have moved from Karnataka to Tamil Nadu (Hosur). Verify on MCA21.
- **Practo Pte. Ltd.** (Singapore, likely holdco) — UEN **201228154Z**, "Live" in an open-data snapshot from roughly June 2026. A move back to India was announced and is not confirmed as completed.
- **Knighthealth Technologies Pvt Ltd** (India, subsidiary per Tofler)

### Known PSPs
- **Razorpay** — [Provider Case Study] (India; UPI Suite — Dynamic Routing + UPI Switch, teleconsults and lab tests). UPI success rate went from **76% to 81%** over six months (vendor-reported, May 2025).
- *GPay / PhonePe / Paytm mini-app containers* — [Source Code] — Practo's checkout detects and handles these as payment channels. This is **not** evidence of a PhonePe PG or Paytm PG acquiring contract.

### Orchestration status
**Unresolved — no third-party orchestrator detected; the TAL's Juspay tag is unconfirmed.**
- Practo's web checkout calls its own endpoints: `/payment/request`, `/payment/cards` (saved cards), `/is_transaction_possible` and `practo_wallet/balance`. That is an in-house payment service sitting in front of the PSP. [Source Code, practo.com/consult JS bundle]
- From outside, there's no way to tell whether that service routes across several PSPs.
- Juspay's own pages (juspay.io/in, /hypercheckout, llms.txt) do not mention Practo. The web bundle contains no Juspay or HyperSDK code. The native app was not inspected.

### Buying signals
- 🚀 **International consumer expansion:** UAE launch May 2025 (50k MAU, ₹100 Cr GMV run-rate within weeks — [Entrackr](https://entrackr.com/exclusive/exclusive-practo-eyes-global-markets-after-6-profitable-quarters-pilots-underway-in-us-9624045)). US launch announced 8 Jan 2026 with ">200,000 doctors listed" and a ">USD 75 million" GMV run-rate ([Entrepreneur India](https://india.entrepreneur.com/news-and-trends/practo-enters-us-after-uae-success-targets-specialist-care/501698)).
- 💼 **New technical and commercial leadership:**
  - **Srijesh Kumar**, Global CPTO, appointed 14 Apr 2026 ([Inc42](https://inc42.com/buzz/ipo-bound-practo-appoints-srijesh-kumar-as-global-cpto/)).
  - **Jagnoor Singh**, CEO, effective 1 Sep 2026 ([People Matters](https://www.peoplematters.in/news/leadership/practo-reshuffles-leadership-team-appoints-jagnoor-singh-as-ceo-52174)).
- 💰 **IPO preparation:** listing pushed to 2027; a $100–125M pre-IPO round is in talks, not closed ([Inc42](https://inc42.com/buzz/exclusive-practo-in-talks-to-raise-100-mn-in-pre-ipo-round)).
- 📋 **Payment processors on a product mandate:** a Technical PM role owns the "integration roadmap for third-party systems — EMRs, LIS/RIS, insurance gateways, **payment processors**" ([Weekday job listing](https://jobs.weekday.works/practo-technical-product-manager-senior-technical-product-manager-at-practo-wkdybjsedb); posting date not confirmed).

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Practo` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 13 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **SOURCED: >100,000/month — ">100,000 teleconsultations a month" and "around 10 million appointments annually" (CEO Shashank ND to Financial Express, 25 May 2026, reproduced in an [NSE filing](https://nsearchives.nseindia.com/corporate/AAFCS9987G_25052026183753_Newspaper.pdf)).** The billing unit counted is **paid teleconsultations only**, which are prepaid online. Most in-clinic appointments are likely free to book and paid at the clinic `[INFERENCE, not confirmed]`, so the 10M/year appointment figure is **not** treated as a payment count. Lab tests, Plus subscriptions and surgery payments come on top. The figure clears ≥100k without relying on any of them. |
| Orchestration status | 0 | ⬜ **Uncertain.** The TAL says Juspay; nothing public confirms it. The evidence that does exist shows Razorpay (with Razorpay's own UPI routing) plus a Practo in-house payment service, and whether that service routes across PSPs is unknown. It is neither confirmed greenfield (+4), nor confirmed Juspay (+3), nor confirmed in-house orchestration (+1). |
| 3+ countries | +3 | ✅ Three countries are above 1% of supplied traffic: India 87.17%, US 4.43%, UAE 1.23%. They are backed by launches the company itself announced in the US and UAE. Note that UAE only just clears the threshold. |
| Multiple PSPs | 0 | ❌ **Only Razorpay is confirmed.** GPay/PhonePe/Paytm mini-app handling is a channel, not a PSP contract. No PayU, Cashfree, CCAvenue, BillDesk, Stripe or Adyen evidence was found. |
| Local rail or licensing gap in a top-3 market | 0 | ⬜ **Uncertain.** UPI is present in India. For the US and UAE, the absence of local acceptance or an entity is *not found*, which is not the same as sourced-absent. Whether UAE requires local presence for domestic acquiring was not checked. |
| Recent expansion | +2 | ✅ US entry was announced 8 Jan 2026 ([Entrepreneur](https://india.entrepreneur.com/news-and-trends/practo-enters-us-after-uae-success-targets-specialist-care/501698)), inside 12 months. The same article says the company "entered the US market in April 2025", and Entrackr described a 50–60-customer pilot in Aug 2025, so the US timeline is inconsistent. The UAE launch (May 2025) is outside the 12-month window. |
| Payment issues reported | +2 | ✅ **High frequency, but the wrong kind.** Trustpilot is 1.4/5 from 191 reviews, 93% one-star, and the dominant theme is refunds not arriving after cancellations, running through Sep–Oct 2026 ([Trustpilot](https://ca.trustpilot.com/review/practo.com)). These are refund-operations complaints, not decline or gateway failures. The point is awarded on the rule, but it is weak evidence for an orchestration pain. |
| Funding >$10M | 0 | ❌ No closed round since Aug 2020. The $100–125M pre-IPO round is "in talks" (Feb 2026), and no close has been found. |
| High traffic outside home | 0 | ❌ India is 87.17% of traffic. |
| Competitor using orchestration | 0 | ⬜ The TAL tags Apollo 24\|7, Tata 1mg and PharmEasy as Juspay, but none of those tags was confirmed. Tata 1mg and MediBuddy are publicly on **Razorpay**. |
| Payment job postings | +1 | ✅ The Technical PM / Senior TPM role explicitly owns the integration roadmap for "payment processors" ([Weekday](https://jobs.weekday.works/practo-technical-product-manager-senior-technical-product-manager-at-practo-wkdybjsedb)). It sits on the B2B (clinic/hospital software) side, and the posting date is unconfirmed (search suggested Jul 2026). |

**Tier:** 13 → **🟢 Medium.** No public payment RFP found. **No analyst override applied.** Three points of sensitivity:
- **Upward:** if checkout confirms *no* orchestrator and direct Razorpay only, orchestration scores +4 and the account reaches **17 ⭐**. If Juspay is confirmed, it scores +3 and the account reaches **16 🟢**. If an international acquirer gap in the US or UAE is sourced, the rail/licensing signal adds +3.
- **Downward caution:** the "3+ countries" and "recent expansion" points both come from the same US/UAE push, which partly double-counts one fact. "Payment issues" is refund operations, not processing.
- **Net:** the arithmetic and the judgement agree on 🟢 Medium, with an obvious path to ⭐ once one walkthrough of the checkout is done.

### Source Notes
- ✅ Razorpay UPI Suite at Practo; UPI success rate 76% → 81% — https://razorpay.com/blog/practo-and-razorpay/ (8 May 2025, page read)
- ✅ FY25 revenue ₹234 Cr, op. EBITDA ₹15 Cr, GMV ₹3,500 Cr; UAE 50k MAU, ₹100 Cr GMV run-rate; US pilot 50–60 paying customers — Entrackr, 4 Aug 2025 (page read). These are Practo's own figures from its annual letter, unaudited.
- ✅ US: >200k doctors, >USD 75M GMV run-rate — Entrepreneur India, 8 Jan 2026 (page read). This is a company claim and is inconsistent with "50–60 paying customers" five months earlier.
- ✅ >100,000 teleconsults/month; ~10M appointments/year; "profitable through FY26"; IPO planned for 2027 — FE, 25 May 2026, via an NSE filing PDF (page read)
- ✅ CEO change effective 1 Sep 2026; "40% YoY growth" — People Matters, 18 Sep 2026 (page read)
- ✅ CPTO Srijesh Kumar, 14 Apr 2026 — Inc42 (page read)
- ✅ Practo Plus auto-debit can be disabled "from the payment section on the Practo App" — help.practo.com Plus FAQ (page read)
- ✅ No-cost EMI on Practo Care — practo.com/care (agent-read)
- ⚠️ Juspay as Practo's orchestrator — **TAL only; not found in any public source**
- ⚠️ Srijesh Kumar's background (ex-Salesforce, Expedia, Adobe, Microsoft) — search summary only
- ⚠️ HealthPlix acquisition talks — reported by Inc42 and **denied by HealthPlix**. Search summary only.
- ⚠️ Dec 2024 termination of Juspay partnerships by PhonePe, Razorpay and Cashfree — search summary only. If true, a Juspay + Razorpay stack would be less likely.

### Success Case Alternatives
Yuno has no healthcare case on file. Every match below is Tier 2 (same payment pattern) and must be framed as LATAM or global, never as APAC.
- **Livelo** — +5% approval, 50% of failed transactions recovered through instant retry on a secondary acquirer ([y.uno](https://y.uno/en/success-stories/livelo)). It matches the 19% UPI failure rate on a single confirmed PSP. Caveat: Livelo already ran 2+ acquirers and Practo has one confirmed.
- **inDrive** — about 90% approval and 10 new countries in under 8 months ([y.uno](https://y.uno/en/success-stories/indrive)). It matches the US/UAE launches built on an India-first stack.
- **Rappi** — provider breadth with no implementation delays ([y.uno](https://y.uno/success-cases/rappi)). It matches the multi-vertical marketplace pattern: consults, labs, surgeries, subscriptions, corporate wallets.

---

## Executive Summary

Practo is India's best-known doctor-discovery and teleconsultation platform. It has 50M+ patients served by its own count, a profitable FY25 on ₹234 Cr revenue and ₹3,500 Cr GMV, and a 2027 IPO in preparation. Its consumer business runs over **100,000 paid teleconsultations a month** in India, alongside lab tests, surgeries and the Practo Plus subscription. The only confirmed payment provider is **Razorpay**, used for UPI, where Razorpay itself reports Practo's UPI success rate rose from 76% to 81%. Behind the checkout sits an in-house payment service, and **no orchestrator, Juspay included, could be confirmed**. The opening is not "you need orchestration". It is the combination of (1) one confirmed PSP carrying a UPI rail that still fails roughly one in five times on the vendor's own numbers, and (2) a new US and UAE consumer business with no confirmed non-INR acquiring. **Motion: unresolved, in-house / Razorpay-native until verified.**

---

### Section 1: Website Traffic Analysis by Country

**Data source:** **Supplied** — Similarweb Sales Intelligence, `accounts/traffic/practo.md`, pulled 2026-10-19, Jul–Sep 2026, practo.com, desktop and mobile web. Total 27.32M visits (3 months), **9.107M average per month**. Device split: desktop 13.69%, mobile web 86.31%. Global rank was not captured.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | India | 87.17% | ~7.94M `[DERIVED from supplied share, not a SimilarWeb figure]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | United States | 4.43% | ~403k `[DERIVED]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 3 | United Arab Emirates | 1.23% | ~112k `[DERIVED]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 4 | United Kingdom | 0.57% | ~52k `[DERIVED]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 5 | Pakistan | 0.50% | ~46k `[DERIVED]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 6 | Indonesia | 0.41% | ~37k `[DERIVED]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 7 | Australia | 0.39% | ~36k `[DERIVED]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 8 | Canada | 0.38% | ~35k `[DERIVED]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 9 | Philippines | 0.29% | ~26k `[DERIVED]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 10 | Sri Lanka | 0.28% | ~25k `[DERIVED]` | Not supplied | SimilarWeb (supplied 2026-10-19) |

The top 10 cover 95.65% of traffic. The remaining 4.35% is spread across countries not listed.

**Caveats carried from the supplied file:**
1. **Web only.** The Practo app is the main transacting surface, and per the Plus page, Plus benefits are app-only. **These shares do not represent the payment mix.**
2. **High priority (>5%):** India only. The US (4.43%) is the next market and the only other one above 2%.
3. **US, UK, Canada and Australia are classic NRI diaspora corridors**, and UAE adds a Gulf-diaspora one. `[INFERENCE, not confirmed]` Some of this traffic may be diaspora users booking care for family in India (the APAC reference §3 "outbound diaspora" pattern). No source confirms that pattern for Practo.
4. **No local entity was found in any top-10 market except India.** See Section 2.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Bengaluru, India. Incorporated 8 May 2008 (Tofler). The registered office may now be in Hosur, Tamil Nadu (Tofler shows a TZ-coded CIN and a Hosur address; Infyner shows a KA-coded CIN in Bangalore).

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| India | Practo Technologies Private Limited | U72900TZ2008PTC038088 (Tofler, updated 16 Oct 2026) / U72900KA2008PTC046374 (Infyner, Feb 2026). **Conflict — verify on MCA21.** | https://www.tofler.in/practo-technologies-private-limited/company/U72900KA2008PTC046374 ; https://www.infyner.com/company/practo/U72900KA2008PTC046374 |
| India | Knighthealth Technologies Pvt Ltd (subsidiary, 2019) | Not found | Tofler (above) |
| India | Practo Rx Services Pvt Ltd; Qikwell Technologies India Pvt Ltd (share a director; **not confirmed as subsidiaries**) | Not found | Tofler (above) |
| Singapore | Practo Pte. Ltd. (likely holdco) | UEN 201228154Z; 9 Raffles Place, #15-06 Republic Plaza; "Live" (open-data snapshot, roughly Jun 2026) | https://acrawatch.sg/company/practo-pte-ltd |
| US | Not found | — | — |
| UAE | Not found | — | — |
| Indonesia / Philippines / Malaysia / Brazil | Historical operations, 2015–17. No current entity checked. | — | `[UNVERIFIED — search summary only, page not fetched]` (TechCrunch, Jan 2017) |

**Redomicile:** in Dec 2025 Practo planned to "shift its Singapore holding entity back to India… re-domicile expected by February" 2026 ([IPO Central](https://ipocentral.in/practo-ipo-targets-h2-2026-listing/)). On 24 Feb 2026 it was still "considering a reverse flip" ([Inc42](https://inc42.com/buzz/practos-mega-meal-whatsapp-vs-cci-more)). Completion is not confirmed.

**Contracting entity on practo.com:** **not confirmed.** The `/company/terms` and `/company/privacy` pages build their text client-side, and the static HTML holds only nav and a "© 2017, Practo" footer.

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| India | ✅ #1 (87.17%) | ✅ | N/A — local entity present | No |
| United States | ✅ #2 (4.43%) | ❌ Not found | Not researched | **Yes, if US patients pay directly.** No US acquirer or entity found despite a claimed >$75M US GMV run-rate. |
| UAE | ✅ #3 (1.23%) | ❌ Not found | Not researched — no source checked | **Yes, if UAE consumers pay directly.** ₹100 Cr UAE GMV run-rate (company-reported). |
| UK, Pakistan, Indonesia, Australia, Canada, Philippines, Sri Lanka | ✅ (each <1%) | ❌ Not found | Not researched | Low materiality |

> *"Warning: Potential cross-border operation in the **United States** and **UAE**. No local entity found. If consumers in these markets pay Practo directly, transactions are likely processed cross-border — higher scheme costs, lower approval rates and FX exposure."*
> **Caveat:** It is not established that US/UAE GMV flows through Practo's checkout at all. In the US model ("200,000 doctors listed") and the UAE model (insurance-led, facility-level) patients may pay providers or insurers directly `[INFERENCE, not confirmed]`. **This is the first discovery question.**

> **MANUAL:** Check the practo.com T&Cs and privacy policy in a real browser (they are JS-rendered), and look for a US or UAE terms variant. In APAC the billing entity is often named there and nowhere else.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| India | **Razorpay** — UPI Suite (Dynamic Routing, UPI Switch) for teleconsultations and lab-test bookings. UPI success rate 76% → 81% over six months. | [Provider Case Study] | https://razorpay.com/blog/practo-and-razorpay/ (8 May 2025) |
| India | GPay Microapps / Paytm mini-app / PhonePe in-app containers. Practo's checkout detects them and sets the app as `googlepay` / `paytmWallet` / `phonepe`, with a `retryMicroappPayment` handler. **Channel handling, not a confirmed acquiring contract.** | [Source Code] | https://www.practo.com/consult (bundle `client.fcb0913c6bcd908a390c.js`, pulled 2026-10-19) |
| India | **Practo in-house payment service**: `/payment/request`, `/payments/request`, `/payment/cards` (saved cards), `/is_transaction_possible`, `user/practo_wallet/balance`, redirect by Practo `transaction_id` | [Source Code] | same bundle |
| India | PayU, Cashfree, CCAvenue, BillDesk, PhonePe PG, Paytm PG | **Not found** | — |
| US / UAE / international | Stripe, Adyen, Checkout.com or any non-INR acquirer | **Not found** | — |

**Single-PSP dependency:** **probable but not proven.** Razorpay is the only PSP confirmed by any source. The in-house payment layer could front more than one PSP, and the native app (Android package `com.practo.fabric`) was not inspected.

#### 3B. Payment Orchestrator

**Classification: Uncertain. No third-party orchestrator detected; in-house payment service present; TAL Juspay tag unconfirmed.**

- **TAL:** `accounts/apac-tal.csv` lists Payment Orchestrator = **Juspay**, Payment Gateway = blank.
- **Juspay's own pages:** I curled juspay.io/in, juspay.io/in/hypercheckout and juspay.io/llms.txt. "Practo" appears 0 times.
- **Search:** a search for "Practo" "Juspay" returned only pages that list both companies separately (vendor customer walls, M&A advisor portfolios). Nothing showed a relationship.
- **Code:** Practo's web consult bundle contains no Juspay, HyperSDK or `expresscheckout` code.
- **Razorpay routing:** Razorpay's Dynamic Routing / UPI Switch routes *within Razorpay* across UPI rails and banks. That is PSP-native routing, not third-party orchestration.
- **TAL reliability:** 18 of the TAL's Indian healthcare rows carry an identical "Juspay" tag with a blank gateway. For Tata 1mg, which is publicly on Razorpay ([Razorpay](https://razorpay.com/blog/tata-1mg-and-razorpay/)), that tag also could not be confirmed. **Treat it as a bulk tag until proven.**

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with Razorpay behind its own payment service, which limits multi-acquirer routing and failover to whatever Razorpay provides natively."*
> Hold this statement until the app or checkout is inspected. **Do not use it in outreach as fact.** If Juspay turns out to be live, the motion flips to displacement (APAC reference §4).

> **MANUAL:** Walk through a paid teleconsult checkout in the app and on the web with DevTools, or capture app traffic. Look for `api.razorpay.com`, `checkout.razorpay.com`, `in.juspay.hypersdk`, `api.juspay.in`, or a second PG domain.

---

### Section 4: Alternative & Local Payment Methods

Scope: India (>1%) and the US and UAE (>1%), plus global methods. Checkout method selection is behind OTP login, so first-party confirmation is limited.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| India | UPI | Bank transfer / A2A | Mentioned in press (PSP case study) | https://razorpay.com/blog/practo-and-razorpay/ |
| India | GPay / PhonePe / Paytm in-app (UPI-branded channels) | Digital wallet / A2A | Mentioned in docs (source code) | practo.com/consult JS bundle |
| India | Credit/debit cards | Cards | Mentioned in press (bank offer T&Cs, 2021, expired) | https://sc.com/in/terms-and-conditions/practomay ; https://www.icici.bank.in/offers/get-started/pockets/pockets-practo-offer |
| India | Saved cards (tokenised by PSP — `[INFERENCE, not confirmed]`) | Cards | Mentioned in docs (source code, `/payment/cards`) | practo.com/consult JS bundle |
| India | RBL Bank × Practo Plus co-branded Mastercard (2019; current status unknown) | Cards | Mentioned in press | https://inc42.com/?p=165146 |
| India | Netbanking | Bank transfer | Unknown, checkout not accessible. Listed only by a coupon site (low reliability). | https://cashkaro.com/stores/practo-order-coupons |
| India | Paytm / Amazon Pay / Mobikwik wallets (as payment instruments) | Digital wallet | Not found | — |
| India | No-cost EMI — Practo Care surgeries | BNPL/Instalments | Mentioned in docs ("No-Cost EMI Options available"); lender not named | https://www.practo.com/care |
| India | Card EMI / cardless EMI on consults or lab tests | BNPL/Instalments | Not found | — |
| India | BNPL (Simpl, LazyPay, ZestMoney) | BNPL | Not found (the "simpl" hit in page source is part of the word "simple") | — |
| India | Lab tests: pay at sample collection (COD) | Cash | Mentioned in docs (default `payment_mode: "COD"` in the lab order form) | https://www.practo.com/tests (source) |
| India | Practo Plus auto-debit (recurring) | Direct debit / mandate | Mentioned in docs. **The rail (UPI Autopay / card e-mandate / e-NACH) is not identified.** | https://help.practo.com/practo-plus/faqs-for-practo-plus/ |
| India | Practo Wallet, HealthCash, corporate/employer wallets | Closed-loop credits | Mentioned in docs (source code) | practo.com/consult and /plus source |
| India | Insurance cashless / reimbursement (Plus Infinity) | Third-party payer | Mentioned in docs | https://help.practo.com/practo-plus/practo-plus-infinity-terms-conditions/ |
| US / UAE | International cards, AED/USD pricing, PayPal, Apple Pay, Google Pay | Cards / Wallet | **Not found** — nothing confirms or rules it out | — |

**Rail-gap assessment:**
- **India:** the dominant rail, UPI, is present. Nothing can be claimed missing, because the checkout was not seen.
- **Real question in India:** **which rail carries Plus auto-debit.** Plus is ₹1,199/1 mo, ₹2,499/3 mo, ₹2,999/12 mo (page source). India's e-mandate rules make renewals of this kind hard (APAC reference §2). That is a discovery question, not a claim.
- **US / UAE:** no evidence of local-currency acceptance. Not sourced as absent.

> **MANUAL:** Book a ₹-priced teleconsult in the app (VPN optional) and screenshot the method list. Check whether a US or UAE IP sees USD/AED pricing and international cards.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Slow / missing refunds after cancellation by Practo or the doctor (incl. an auto-cancelled prepaid online consult) | Trustpilot (1.4/5, 191 reviews, 93% 1-star) | **High** — the dominant theme | to Sep 30 – Oct 1, 2026 | https://ca.trustpilot.com/review/practo.com |
| Lab-test refund not received (₹1,599 order with missing tests) | Trustpilot | Moderate | May 2026 | https://ca.trustpilot.com/review/practo.com |
| Lab-test refund pending for weeks (Jan 2025 booking) | Trustpilot p.3 | Moderate | Jan–Feb 2025 | https://ca.trustpilot.com/review/practo.com?page=3 `[UNVERIFIED — search summary only, page not fetched]` |
| Price mismatch: ₹629 "Instant Consult" against a ₹199 listed fee; clinic charged more than the listing | Trustpilot; Reddit | Moderate | Jan–Jul 2026 | Trustpilot (above); Reddit snapshot `[UNVERIFIED — search summary only, page not fetched]` |
| Plan upsell confusion (₹1,200 plan didn't cover specialists) | Trustpilot | Isolated | Jul 2026 | https://ca.trustpilot.com/review/practo.com |
| Clinic-side (B2B) subscription refunds refused (₹49,856 "Reach" package; others) | Trustpilot | Moderate | Dec 2025 – Sep 2026 | https://ca.trustpilot.com/review/practo.com |
| Double charges, "money deducted but booking failed", UPI failures, Plus auto-debit disputes | Reddit / X / app stores | **Not found** | — | — |

> *"Pattern of slow refunds after cancellations on Trustpilot points to refund-operations and policy friction, **not** to authorisation or routing failures."*
> Orchestration's link to this is indirect: unified refund status across PSPs, and refunds back to the original instrument. **Do not lead with complaints.** The only processing-failure data point is the vendor-reported 76% → 81% UPI success rate (Section 3A).

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 18 Sep 2026 (effective 1 Sep) | Jagnoor Singh named CEO. Founder Shashank ND becomes MD & Executive Chairman. Company cites 40% YoY growth and 2.5+ years of profitability. | Leadership Change | https://www.peoplematters.in/news/leadership/practo-reshuffles-leadership-team-appoints-jagnoor-singh-as-ceo-52174 |
| 2 | 25 May 2026 | CEO tells FE: ~10M appointments a year, >100k teleconsults a month, "profitable through FY26", revenue to "nearly triple by FY27" including acquisitions, IPO planned for 2027 | Funding / M&A signal | https://nsearchives.nseindia.com/corporate/AAFCS9987G_25052026183753_Newspaper.pdf |
| 3 | 14 Apr 2026 | Srijesh Kumar appointed Global Chief Product & Technology Officer, to "lead the product and technology teams… as it scales globally" | Leadership Change | https://inc42.com/buzz/ipo-bound-practo-appoints-srijesh-kumar-as-global-cpto/ |
| 4 | 23 Feb 2026 | In talks for a $100–125M pre-IPO round (equity + debt) at ~$700M valuation; FY26 revenue reportedly +35% YoY. **Not closed.** | Funding | https://inc42.com/buzz/exclusive-practo-in-talks-to-raise-100-mn-in-pre-ipo-round |
| 5 | 8 Jan 2026 | US market entry announced: >200k doctors listed, >USD 75M annualised GMV run-rate (company claim) | Market Expansion | https://india.entrepreneur.com/news-and-trends/practo-enters-us-after-uae-success-targets-specialist-care/501698 |

Earlier context:
- **May 2025:** UAE consumer launch, covered in Entrackr, 4 Aug 2025.
- **Dec 2025:** banks explored for an IPO originally targeted at H2 2026 ([Digital Health News](https://www.digitalhealthnews.com/practo-explores-banks-for-potential-2026-ipo)).
- **~May 2026:** HealthPlix acquisition talks reported, then **denied by HealthPlix** `[UNVERIFIED — search summary only, page not fetched]`.

- **Public payment RFP:** *No public payment-related RFP found.*
- **Licence applications:** none found (no RBI PA or PPI).
- **Payment hiring:** a Technical PM / Senior TPM role (Bengaluru, B2B products) owns the "integration roadmap for third-party systems — EMRs, LIS/RIS, insurance gateways, **payment processors**" ([Weekday](https://jobs.weekday.works/practo-technical-product-manager-senior-technical-product-manager-at-practo-wkdybjsedb), posting date not confirmed). No dedicated payments-engineering roles were found.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 8 May 2025 | "How Razorpay UPI Powers Practo" — UPI Suite (Dynamic Routing, UPI Switch) lifted the UPI success rate from 76% to 81% over 6 months | **High** — the only named PSP, and a quantified failure rate | https://razorpay.com/blog/practo-and-razorpay/ |
| 2 | 4 Aug 2025 | UAE platform: 50k MAU and ₹100 Cr GMV run-rate within weeks; "cross-border access between Indian and UAE patients and providers" | High — non-INR payment flows | https://entrackr.com/exclusive/exclusive-practo-eyes-global-markets-after-6-profitable-quarters-pilots-underway-in-us-9624045 |
| 3 | 2021 (launch) | Practo Care Surgeries: no-cost EMI and a target of ₹1,000 Cr in healthcare financing over 3 years (lender not named) | Medium — instalments on high-ticket care | https://biovoicenews.com/practo-forays-into-secondary-healthcare-launches-practo-care-surgeries/ |
| 4 | Aug 2019 | RBL Bank × Practo Plus co-branded Mastercard credit card, earning HealthCash | Low — legacy | https://inc42.com/?p=165146 |
| 5 | Feb 2026 | UAE described as the "epicenter" of Practo's global consumer expansion, adapting to insurance-led systems | Medium | https://enterpriseam.com/mena-india/2026/02/11/why-uae-markets-remain-the-epicenter-of-practos-global-consumer-expansion/ (page fetched; article body not extractable) |

No provider removals found.

---

### Section 8: Checkout Experience Audit

*"Full checkout flow not accessible. Findings limited to publicly observable elements (page source of practo.com, /plus, /tests, /consult, pulled 2026-10-19)."*

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | Custom, built on Practo's own `/payment/request` service, redirecting to the PSP by `transaction_id` | Not assessed | Custom-built front end with PSP redirect |
| Guest checkout | **No.** Mobile number + OTP login is required (`login_signup_otp`) | Fair | Normal for Indian health apps |
| Steps to complete payment | Not observable | — | Behind login |
| Card input experience | Not observable. A saved-card endpoint exists. | — | — |
| Payment methods visible | Not observable. GPay and PhonePe logos are in the checkout assets. | — | — |
| Location-based method display | Not found | — | Legacy locale paths `/en-sg`, `/en-id`, `/en-ph` exist. CSS has USD/IDR/PHP/BRL glyphs (legacy). |
| Instalment / EMI options | No-cost EMI on surgeries only | Fair | None found on consults or lab tests (low ticket) |
| 3DS implementation | Not detected | — | — |
| PCI indicator | Not determinable | — | The "pci" string in source is an Akamai mPulse parameter, not a compliance claim |
| Mobile responsiveness | 86% of web traffic is mobile web; Plus benefits are app-only | Not assessed | App-first |
| Multi-currency / local pricing | INR only observed | — | No USD or AED pricing found |
| Saved payment methods | `/payment/cards` endpoint present | Not assessed | — |
| Error message clarity | `retryMicroappPayment` handler present | Not assessed | — |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found | — |
| Card data handling | Not found. A saved-cards endpoint exists. Under India's card-on-file tokenisation regime this is normally PSP- or network-tokenised `[INFERENCE, not confirmed — regulation not re-verified for this report]`. | practo.com/consult bundle |
| Recommended Yuno integration | SDK, given the app-first surface and the hosted PSP redirect `[INFERENCE, not confirmed]` | — |

*"No direct PCI compliance documentation found publicly for Practo."* UpGuard's external security rating of "A" `[UNVERIFIED — search summary only, page not fetched]` says nothing about PCI.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: One confirmed PSP, and UPI still failing about one time in five**
> **Evidence:** S3A — Razorpay is the only confirmed PSP. Its own case study puts Practo's UPI success rate at 76%, rising to 81% after UPI Switch ([Razorpay](https://razorpay.com/blog/practo-and-razorpay/)). S12 — more than 100,000 paid teleconsults a month ([FE via NSE](https://nsearchives.nseindia.com/corporate/AAFCS9987G_25052026183753_Newspaper.pdf)). S3B — no third-party failover layer detected.
> **Pain Point:** At >100k teleconsults a month, plus lab orders, a 19% UPI failure rate is a lot of patients bouncing at the moment they want care. Routing that lives inside one PSP can't fail over to another PSP's UPI stack or to a second acquirer.
> **Yuno Value Proposition:** Cross-PSP smart routing and instant retry on a second processor, without re-integrating — Yuno adds to Razorpay rather than replacing it.
> **Best Success Case:** **Livelo** (Tier 2, LATAM loyalty). 50% of failed transactions were recovered by routing to a secondary acquirer, with +5% approval. Same pattern: recovering declines through a second route. Caveat: Livelo already ran 2+ acquirers.
> **Outreach Angle:** "Razorpay published that Practo's UPI success went from 76% to 81% with UPI Switch. Solid gain, but at 100k+ teleconsults a month the remaining 19% is the number I'd want to talk about."
> **Suggested Subject Line:** "the other 19% of Practo's UPI payments"
> ⚠️ This is a May 2025 vendor-reported figure. Say "Razorpay published", and do not claim it is the current rate.

> **Insight #2: US and UAE launched on an India-first stack**
> **Evidence:** S1 — US is 4.43% and UAE 1.23% of web traffic (supplied). S6 and S7 — company-claimed US GMV run-rate above $75M and UAE ₹100 Cr run-rate ([Entrepreneur](https://india.entrepreneur.com/news-and-trends/practo-enters-us-after-uae-success-targets-specialist-care/501698); [Entrackr](https://entrackr.com/exclusive/exclusive-practo-eyes-global-markets-after-6-profitable-quarters-pilots-underway-in-us-9624045)). S2 — no US or UAE entity found. S3A and S4 — no non-INR acquirer or method found.
> **Pain Point:** If US and UAE consumers pay Practo directly, an INR-centric stack either can't take USD or AED locally or takes them cross-border, with lower approval rates and FX cost. Each new country becomes another one-off PSP integration.
> **Yuno Value Proposition:** One integration to local acquirers and methods in the US and UAE, and in whatever market comes next, with India routing left untouched.
> **Best Success Case:** **inDrive** (Tier 2, global mobility). Launched in 10 new countries in under 8 months at about 90% approval.
> **Outreach Angle:** "Practo went live in the UAE and US within a year. Curious how USD and AED collections are running alongside Razorpay in India, or whether patients there pay providers directly."
> **Suggested Subject Line:** "Practo's AED and USD collections"
> ⚠️ It is not established that US or UAE money flows through Practo's checkout. Frame this as a question, not a claim.

> **Insight #3: New CPTO and CEO inside six months, with "payment processors" on the integration roadmap**
> **Evidence:** S6 — Srijesh Kumar became Global CPTO on 14 Apr 2026 with a mandate to unify product and tech "as it scales globally" ([Inc42](https://inc42.com/buzz/ipo-bound-practo-appoints-srijesh-kumar-as-global-cpto/)). Jagnoor Singh became CEO on 1 Sep 2026 ([People Matters](https://www.peoplematters.in/news/leadership/practo-reshuffles-leadership-team-appoints-jagnoor-singh-as-ceo-52174)). The TPM role owns "payment processors" integration ([Weekday](https://jobs.weekday.works/practo-technical-product-manager-senior-technical-product-manager-at-practo-wkdybjsedb)). S3A — in-house payment service.
> **Pain Point:** A platform being consolidated ahead of a 2027 IPO, across consumer, B2B SaaS, wallets, insurance and two new countries, is building more payment integrations one at a time.
> **Yuno Value Proposition:** Consolidate PSP integrations behind one API so the product and tech team ships markets, not gateways.
> **Best Success Case:** **Rappi** (Tier 2, multi-vertical super app). Hundreds of methods with zero implementation delays and 80% less analyst work.
> **Outreach Angle:** To Srijesh Kumar: "Six months into unifying Practo's product and tech for global scale, and payment processors are on the integration roadmap next to EMRs and insurance gateways. That's the layer we take off the roadmap."
> **Suggested Subject Line:** "payment processors on Practo's integration roadmap"

> **Insight #4: Practo Plus renewals under India's mandate rules**
> **Evidence:** S4 — Plus auto-debit exists and can be disabled "from the payment section on the Practo App" ([help.practo.com](https://help.practo.com/practo-plus/faqs-for-practo-plus/)). Plans are ₹1,199/1 mo, ₹2,499/3 mo, ₹2,999/12 mo (practo.com/plus source). Billing appears to be direct, not app-store. S3A — one confirmed PSP.
> **Pain Point:** Hypothesis only: recurring card and UPI debits in India sit under e-mandate rules that complicate retries. The rail Practo uses is not known.
> **Yuno Value Proposition:** Mandate-aware recurring billing across PSPs, with retry logic.
> **Best Success Case:** No subscription case with numbers on file (Open English has none). Use as a discovery question, not an E4.
> **Outreach Angle:** Phase 2 question only: "How are Plus renewals collected — UPI Autopay, card mandates, or both?"
> **Suggested Subject Line:** "Practo Plus renewals"

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. Razorpay published that UPI Switch took Practo's UPI success rate from 76% to 81% — at 100k+ teleconsults a month, I'd be curious what the remaining 19% looks like today.
2. Practo launched consumer services in the UAE and the US inside a year — how are AED and USD collections running next to the India stack?
3. Your TPM job description puts "payment processors" on the same integration roadmap as EMRs and insurance gateways — that's a lot of separate integrations for a team prepping an IPO.

**Cold call openers (conversational, one sentence each):**
1. "I saw Razorpay's write-up on your UPI success rate — is the 81% roughly where it still sits, or has it moved?"
2. "With the UAE and US live now, are those patients paying through Practo's own checkout or straight to providers?"
3. "Srijesh, you're six months into unifying product and tech — is payments one of the integrations you're trying to collapse?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| Tata 1mg | 1mg.com | India | FY25 consolidated revenue ₹2,392 Cr | India | **Razorpay** (gateway + saved cards, verified). TAL says Juspay, unverified. | https://entrackr.com/fintrackr/tata-1mg-revenue-nears-rs-2400-cr-in-fy25-trims-losses-9534620 ; https://razorpay.com/blog/tata-1mg-and-razorpay/ |
| MediBuddy | medibuddy.in | India | Not found (low-quality source claims ~22% of organised digital health) | India | **Razorpay** (homepage preconnects to `checkout.razorpay.com`, curl 2026-10-19) | medibuddy.in homepage source |
| Apollo 24\|7 (Apollo HealthCo) | apollo247.com | India | FY25 GMV ₹3,007 Cr `[UNVERIFIED — search summary only, page not fetched]` | India | Not found publicly; TAL says Juspay, unverified | Apollo Q2 FY26 transcript `[UNVERIFIED — search summary only]` |
| PharmEasy (API Holdings) | pharmeasy.in | India | Not found | India | **Cashfree Payouts** for retailer settlements (2022 press release) | https://www.cashfree.com/news-room/cashfree-payments-partners-with-pharmeasy-to-facilitate-convenient-payment-settlements-to-its-retail-partners/ |
| Truemeds | truemeds.in | India | $85M round, 2025 `[UNVERIFIED — search summary only]` | India | Not found | finder.techleap.nl `[UNVERIFIED]` |
| Pristyn Care | pristyncare.com | India | $4M Jul 2025; reportedly in talks for $100M `[UNVERIFIED]` | India | Not found | entrackr.com `[UNVERIFIED]` |
| Netmeds (Reliance Retail) | netmeds.com | India | Majority acquired by Reliance in 2020 for $83.2M `[UNVERIFIED]` | India | Not found | relianceretail.com `[UNVERIFIED]` |

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Doctor Anywhere | doctoranywhere.com | Telehealth + clinics | SG, TH, MY, VN, PH | Multi-market SEA telehealth; local rails in five countries | mobihealthnews.com `[UNVERIFIED — search summary only]` |
| Halodoc | halodoc.com | Telehealth + pharmacy | Indonesia | QRIS / VA / wallet market | mobihealthnews.com `[UNVERIFIED]` |
| Alodokter | alodokter.com | Telehealth | Indonesia | Same; claims 20M+ MAU | 500.co `[UNVERIFIED]` |
| KonsultaMD (mWell) | konsultamd.com | Telehealth | Philippines | GCash/Maya market; acquired by MPIC's mWell in Feb 2025 | techleap `[UNVERIFIED]` |
| Ping An Good Doctor | — | Telehealth | China | FY2025 revenue RMB 5.47B | bolsamania.com `[UNVERIFIED]` |
| JD Health | — | E-pharmacy + telehealth | China | FY2025 revenue RMB 73.4B | HKEX filing `[UNVERIFIED]` |
| HealthifyMe | healthifyme.com | Health subscriptions | India + international | India-HQ subscriptions billed abroad; TAL says Juspay, unverified | apac-tal.csv |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| Bask Health (US) | Juspay Hyperswitch | Not stated | Health-tech marketplace (non-APAC) | https://hyperswitch.io/case-studies/bask-health |

*"No public case studies found of direct competitors adopting payment orchestration."* The TAL's Juspay tags on Apollo 247, Tata 1mg, PharmEasy and 15 other Indian healthcare rows are unconfirmed.

#### 11D. Prospect Scoring

These are partial scores: only signals verified during this run are counted, and most rows lack traffic and transaction data.

| Company | Verified signals | Partial score | Evidence Source |
|---------|------------------|---------------|-----------------|
| Tata 1mg | Single confirmed PSP (Razorpay); India only | Not scorable (no transaction count, traffic or orchestrator check) | razorpay.com case study |
| MediBuddy | Razorpay on live homepage; India only | Not scorable | homepage source |
| Doctor Anywhere | 5 SEA markets (3+ countries +3) `[UNVERIFIED]`; funding >$10M not within 12 months | ≤3 verified | mobihealthnews `[UNVERIFIED]` |
| Halodoc / Alodokter | Single market; Alodokter round Sept 2025 (amount not confirmed) | Not scorable | — |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Doctor Anywhere | Peer | SG, TH, MY, VN, PH | Not scored | Investigate | Five-market SEA telehealth | **❌ No — genuine find** |
| 2 | Halodoc | Peer | ID | Not scored | Investigate | Indonesia rails (QRIS/VA) | **❌ No** |
| 3 | Alodokter | Peer | ID | Not scored | Investigate | 20M+ MAU claim; 2025 round | **❌ No** |
| 4 | MediBuddy | Competitor | IN | Not scored | Investigate | Razorpay on live site; Practo's closest rival | **❌ No — genuine find** |
| 5 | Pristyn Care | Competitor | IN | Not scored | Investigate | High-ticket surgeries (EMI); reported $100M raise | **❌ No** |
| 6 | Truemeds | Competitor | IN | Not scored | Investigate | $85M 2025 round `[UNVERIFIED]` | **❌ No** |
| 7 | KonsultaMD (mWell) | Peer | PH | Not scored | Investigate | Philippines telehealth, recently consolidated | **❌ No** |
| 8 | Tata 1mg | Competitor | IN | Not scored | Medium | Razorpay confirmed; TAL Juspay tag contradicted | ✅ Yes |
| 9 | Apollo 24\|7 | Competitor | IN | Not scored | Medium | HealthCo demerger planned | ✅ Yes |
| 10 | PharmEasy | Competitor | IN | Not scored | Low | Cashfree payouts | ✅ Yes |

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | FY25 revenue from operations **₹234 Cr** (~US$27M `[ESTIMATE, not confirmed — FX conversion at ~₹85–88/USD]`), company-reported and unaudited. Standalone Indian entity FY25: ₹155.4 Cr. FY26: "+35% YoY" per sources (~₹315 Cr implied — `[ESTIMATE, not confirmed]`). | Entrackr 4 Aug 2025; Tofler; Inc42 23 Feb 2026 |
| GMV / Gross Transaction Volume | **₹3,500 Cr (FY25)**, "steady" | Entrackr 4 Aug 2025 |
| Average Transaction Value (USD) | Not found. ₹3,500 Cr ÷ 10M appointments ≈ ₹3,500 is an **upper bound only**, since GMV includes hospital, surgery and software flows. Not usable as an average transaction value. | Calculated, not usable |
| Est. Annual Transactions | ≥1.2M paid teleconsults a year (100k × 12), plus lab orders, Plus subscriptions and surgeries (not found) | Derived from FE |
| **Monthly transaction count** | **✅ SOURCED: >100,000/month — ">100,000 teleconsultations a month" (CEO to Financial Express, 25 May 2026, https://nsearchives.nseindia.com/corporate/AAFCS9987G_25052026183753_Newspaper.pdf).** Billing unit: one prepaid teleconsult. The "~10 million appointments annually" (~833k/month) is **not** counted as payments, since in-clinic bookings are likely paid at the clinic `[INFERENCE, not confirmed]`. Lab tests and Plus come on top. | See ICP matrix disclosure rule |
| Active Customers / Users | 50M+ patients served (cumulative); 5 lakh doctors; 640+ cities; UAE 50k MAU. No India MAU found. | Entrackr 4 Aug 2025 |
| Primary Currency | INR. US and UAE flows (USD/AED) are company-claimed, but no acceptance was confirmed. | — |
| Top 3 Markets by Revenue | India; about one-fifth of revenue is international, mainly hospital software in SEA, the Middle East and Africa. US and UAE consumer GMV is claimed. | IPO Central, Dec 2025 (agent-read) |
| Billing channel split (web vs app store) | **Direct, not app-store `[INFERENCE, not confirmed]`.** The store listings show no in-app-purchase flag, Plus auto-debit is managed in Practo's own payment section, and real-world healthcare services generally fall outside store billing. | App Store / Play listings; help.practo.com |
| Revenue mix | Provider side (software + services) is ~80% of revenue. That B2B SaaS revenue is largely invoiced, not checkout. **Consumer GMV is the orchestration-relevant flow.** | FE 25 May 2026 |

---

### Overall Research Confidence

**Medium.**
- **Traffic:** supplied by Prateek (Similarweb Sales Intelligence, 2026-10-19). Strong as a market-mix signal, but web-only and without per-country counts.
- **Strong coverage:** financials and scale (verified Entrackr, FE and Inc42 pages), corporate developments and leadership (verified), the transaction count (sourced), and Razorpay (provider case study).
- **Weak coverage:**
  - The checkout itself: login-gated, so the payment-method list, PSP domains and 3DS were not seen.
  - The orchestrator question: TAL Juspay versus no evidence.
  - The contracting entity: T&Cs are JS-rendered.
  - Whether US and UAE revenue flows through Practo's checkout at all.
  - The native app, which is the main transacting surface and was not inspected.

---

### Manual Research Recommendations

> **Area:** Orchestrator status (Section 3B) — TAL says Juspay; no public evidence
> **Why it matters:** It decides between +4 (greenfield, which takes the account to ⭐ 17) and +3 (displacement, a different pitch). Opening with the wrong motion burns the thread.
> **Suggested manual action:** Find where the TAL's Juspay tag came from. Run one paid teleconsult in the app with a proxy (Charles or mitmproxy) or on web with DevTools, and look for `api.juspay.in` / `hypersdk` against `api.razorpay.com`.

> **Area:** Payment-method list and Plus mandate rail (Section 4)
> **Why it matters:** These are the only two places a rail gap could exist in India, and the Plus renewal rail is a strong Phase 2 hook.
> **Suggested manual action:** Log in, start a Plus purchase and a lab-test checkout, and screenshot the methods and the auto-debit options.

> **Area:** US and UAE payment flows (Sections 2 and 4)
> **Why it matters:** Insight #2 depends on whether US and UAE patients pay Practo directly in USD or AED, and through what acquirer and entity.
> **Suggested manual action:** Visit practo.com from a UAE or US IP (VPN). Check for a separate UAE app or terms page, and check DED/DHA or a US state registry for a Practo entity.

> **Area:** Contracting entity and CIN conflict (Section 2)
> **Why it matters:** Needed for the business case and to know which entity signs.
> **Suggested manual action:** Read /company/terms in a browser, and look up both CINs on MCA21.

---

### Appendix: All Source URLs

**Traffic**
- `accounts/traffic/practo.md` (Similarweb Sales Intelligence, supplied 2026-10-19)

**Phase 0**
- https://y.uno/en

**Section 2**
- https://www.tofler.in/practo-technologies-private-limited/company/U72900KA2008PTC046374
- https://www.infyner.com/company/practo/U72900KA2008PTC046374
- https://acrawatch.sg/company/practo-pte-ltd
- https://ipocentral.in/practo-ipo-targets-h2-2026-listing/
- https://inc42.com/buzz/practos-mega-meal-whatsapp-vs-cci-more
- https://www.practo.com/company/privacy
- https://www.practo.com/company/terms

**Section 3**
- https://razorpay.com/blog/practo-and-razorpay/
- https://www.practo.com/consult (JS bundle `/consult/static/js/client.fcb0913c6bcd908a390c.js`)
- https://juspay.io/in
- https://juspay.io/in/hypercheckout
- https://juspay.io/llms.txt
- https://razorpay.com/blog/tata-1mg-and-razorpay/

**Section 4**
- https://help.practo.com/practo-plus/faqs-for-practo-plus/
- https://help.practo.com/practo-plus/practo-plus-infinity-terms-conditions/
- https://www.practo.com/plus
- https://www.practo.com/tests
- https://www.practo.com/care
- https://sc.com/in/terms-and-conditions/practomay
- https://www.icici.bank.in/offers/get-started/pockets/pockets-practo-offer
- https://inc42.com/?p=165146
- https://cashkaro.com/stores/practo-order-coupons
- https://apps.apple.com/in/app/practo-consult-doctor-online/id953772015
- https://biovoicenews.com/practo-forays-into-secondary-healthcare-launches-practo-care-surgeries/

**Section 5**
- https://ca.trustpilot.com/review/practo.com
- https://ca.trustpilot.com/review/practo.com?page=3 (unverified)
- https://voxya.com/consumer-complaints/practo-has-charged-500-extra-for-the-lab-test-they-have-done-with-thyrocare/37419 (unverified, 2019)

**Sections 6 and 7**
- https://www.peoplematters.in/news/leadership/practo-reshuffles-leadership-team-appoints-jagnoor-singh-as-ceo-52174
- https://nsearchives.nseindia.com/corporate/AAFCS9987G_25052026183753_Newspaper.pdf
- https://inc42.com/buzz/ipo-bound-practo-appoints-srijesh-kumar-as-global-cpto/
- https://inc42.com/buzz/exclusive-practo-in-talks-to-raise-100-mn-in-pre-ipo-round
- https://india.entrepreneur.com/news-and-trends/practo-enters-us-after-uae-success-targets-specialist-care/501698
- https://entrackr.com/exclusive/exclusive-practo-eyes-global-markets-after-6-profitable-quarters-pilots-underway-in-us-9624045
- https://www.digitalhealthnews.com/practo-explores-banks-for-potential-2026-ipo
- https://enterpriseam.com/mena-india/2026/02/11/why-uae-markets-remain-the-epicenter-of-practos-global-consumer-expansion/
- https://jobs.weekday.works/practo-technical-product-manager-senior-technical-product-manager-at-practo-wkdybjsedb
- https://inc42.com/buzz/practo-turns-profitable-in-fy25-revives-ipo-plans/

**Section 11**
- https://entrackr.com/fintrackr/tata-1mg-revenue-nears-rs-2400-cr-in-fy25-trims-losses-9534620
- https://www.cashfree.com/news-room/cashfree-payments-partners-with-pharmeasy-to-facilitate-convenient-payment-settlements-to-its-retail-partners/
- https://hyperswitch.io/case-studies/bask-health
- medibuddy.in homepage source (curl, 2026-10-19)

**Yuno cases**
- https://y.uno/en/success-stories/livelo
- https://y.uno/en/success-stories/indrive
- https://y.uno/success-cases/rappi

</details>
