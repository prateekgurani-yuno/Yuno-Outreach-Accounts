# Ixigo

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 17 / 29 → computed ⭐ High Priority → **analyst override DOWN to 🟢 Medium** (reasoning in the ICP breakdown)
**Industry:** Travel & OTA (trains, flights, buses, hotels) · **HQ:** Gurugram, India · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** ⚠️ **Unconfirmed — treat as orchestration-aware.** Multi-PSP with "backup for each method" is self-stated; Juspay is named as a client only in a 2023 vendor boilerplate. Never open with "you have no orchestration layer."

---

> ## ⛔ READ FIRST — the TAL's "Juspay" is NOT confirmed. Pitch as if it might be.
>
> The TAL cell `Payment Orchestrator = Juspay` (for ixigo, AbhiBus and ConfirmTkt) was tested independently:
> - **No Juspay customer story exists.** `juspay.io/customer-stories/ixigo`, `/abhibus`, `/confirmtkt` all return the same 404 as a nonsense-path control (196,011 bytes each). The live index lists 33 stories (Agoda, IndiGo, tiket, Wego, TravClan, BookMyShow…) — not ixigo.
> - **The only Juspay link is a one-word boilerplate mention.** Juspay's IndiGo press release (c. 2023) lists *"Amazon, Flipkart, Swiggy, Big Basket, Cred, Ajio, Airtel, Ixigo, Axis Bank…"* as clients. No product, scope or date. Verified first-hand: [juspay.io/newsroom/…indigo](https://juspay.io/newsroom/juspay-to-power-payments-for-india-s-leading-airline-indigo).
> - **What ixigo's own payments lead says in 2024–25 points elsewhere.** Every public statement is about **Razorpay-native** features: TokenHQ, Native OTP, CVV-less checkout, Turbo UPI. ixigo calls Razorpay its *"preferred Payment Aggregator for several years"* ([Razorpay, 15 May 2025](https://razorpay.com/blog/from-drop-offs-to-takeoffs-how-razorpays-card-payments-powered-ixigos-growth/)).
> - **But they do run routing of some kind.** Same interview: *"By integrating multiple payment methods and **backup for each of the methods**…"*. Whether that's Juspay, an in-house layer or PSP-level failover is **unknown**.
>
> **Rule for outreach:** assume they already route across PSPs. The opening is **success rate at their scale, and payments for the international business they just bought**. It is not "you need orchestration."

> ## 🎯 THE HOOK — they publish what one point of success rate is worth, and they just went cross-border
>
> 1. **They have told the market success rate is their #1 payment metric, and put a price on it.** *"At ixigo, our primary focus in payment is centered around success rates"* ([Razorpay, 19 Jul 2024](https://razorpay.com/blog/ixigo-unlocks-1-click-payments-with-razorpay-turbo-upi/)). *"In a particular month alone, ixigo has seen a **2.43% bump in Card Success Rate**, with **more than 5 Cr of incremental GTV**"* ([Razorpay, 15 May 2025](https://razorpay.com/blog/from-drop-offs-to-takeoffs-how-razorpays-card-payments-powered-ixigos-growth/)). That is their own number for what about 2.4 points on cards is worth in one month.
> 2. **They went international in 2026, and the new business sits in another currency on another continent.** They set up **IXIGO PTE. LTD. (Singapore)** on 18 Dec 2025. Through it they bought **60% of Trenes.com, Spain's second-largest train OTA**, consolidated from 1 Mar 2026. They also took **45.02% of Squad As A Service, S.L.** ([FY26 Annual Report](https://rocket.ixigo.com/investors/Le-Travenues-Technology-Limited---Annual-Report-FY-2025-26-new.pdf)). The rest of Trenes is due in two earn-out tranches. The India stack (Razorpay, UPI, RuPay) does not acquire EUR. **They run two payment stacks on two continents with no common layer we can see.**
> 3. **They have ₹1,295.6 Cr of fresh Prosus money earmarked for "selective inorganic opportunities."** That suggests more acquisitions are coming, and each one brings its own payment stack.
>
> ⚠️ **Territory flag:** ixigo is India-HQ'd, so it is Prateek's account. **Trenes/Spain is an EMEA market.** If the conversation turns into a European acquiring deal, loop in EMEA. Don't sell it as APAC coverage.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** ixigo is the brand of **Le Travenues Technology Ltd** (NSE: IXIGO, BSE: 544192; listed June 2024). It is an AI-led Indian OTA running four consumer brands: **ixigo** (trains, flights, buses, hotels), **ConfirmTkt** (trains), **AbhiBus** (buses) and, since March 2026, **Trenes.com** (Spain, 60%). FY26 figures: **GTV ₹18,692.7 Cr (+25%)**, **revenue ₹1,228 Cr (+34%)**, **4.06M monthly transacting users**, **141.5M passenger segments**. Customers are concentrated in India's Tier II/III cities (93.96%), and 80% of users pay by UPI.

**SimilarWeb total visits (last full month):** **~10.82M avg/month (Jul–Sep 2026, ixigo.com only)**. Source: SimilarWeb Sales Intelligence (supplied by Prateek, 2026-10-19). ⚠️ **Web only, and ixigo is app-first.** Mobile-app traffic is excluded, and ConfirmTkt, AbhiBus and trenes.com were not pulled. Use these numbers as a market-mix signal only, not as a volume figure.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇮🇳 India | **93.55%** | UPI (incl. Razorpay Turbo 1-Click UPI), cards (incl. RuPay; AU SFB co-brand), netbanking, wallets (unnamed), ixigo Credit PayLater/EMI, card EMI, ixigo money | No sourced dominant-rail gap. Named wallets (Paytm/PhonePe/Amazon Pay) not confirmed. No UPI Autopay (no recurring product found) | ✅ Le Travenues Technology Ltd (CIN L63000HR2006PLC071540) |
| 2 | 🇦🇪 UAE (EMEA) | 0.74% | Not found (checkout not reachable) | International-card acceptance unverified | ❌ None found |
| 3 | 🇺🇸 United States | 0.60% | Not found | International cards, Apple Pay, PayPal: not found | ❌ None found |
| 4 | 🇸🇬 Singapore | 0.49% | Not found | PayNow not found (0.49% share, so not material) | ✅ IXIGO PTE. LTD. (holding co, inc. 18 Dec 2025) |
| 5 | 🇬🇧 United Kingdom | 0.30% | Not found | — | ❌ None found |

*No ❌🔒 cells: none of the non-India top-5 markets is an APAC acquiring-gated market, and each is under 1% of traffic. 🇪🇸 Spain is not in the ixigo.com top 10, but it has two group entities and its own domain (trenes.com, not pulled).*

### Legal entities
- **Le Travenues Technology Limited** (India). CIN **L63000HR2006PLC071540**. Registered office: 2nd Floor, Veritas Building, Sector 53, Golf Course Road, Gurugram 122002.
- **Zoop Web Services Private Limited** (India). 62% subsidiary.
- **Freshbus Private Limited** (India). 25.66% associate.
- **IXIGO PTE. LTD.** (Singapore). 100% subsidiary, incorporated 18 Dec 2025, 50,000 shares of SGD 1. Holds Trenes.
- **Ixigo Europe, S.L.** (Spain). 100% subsidiary.
- **Online Travel Solutions, S.L. ("Trenes")** (Spain). 60% step-down subsidiary through IXIGO PTE. LTD. NIF B-66144098, Barcelona ([trenes.com/condiciones.php](https://www.trenes.com/condiciones.php)).
- **Squad As A Service, S.L. (Sqaas)** (Spain). 45.02% associate.
- *Source for all except the NIF: [FY26 Annual Report](https://rocket.ixigo.com/investors/Le-Travenues-Technology-Limited---Annual-Report-FY-2025-26-new.pdf), Directors' Report §4 and Notes.*

### Known PSPs
- **Razorpay**: [Provider Case Study] ×2 (May 2025 cards; Jul 2024 Turbo UPI). India. *"Preferred Payment Aggregator for several years."*
- **Cashfree Payments**: [Provider Case Study] (23 May 2022). India. Payment gateway pre-authorisation on train tickets for instant refunds. ⚠️ 2022, not reconfirmed.
- **Juspay**: [Press Release] boilerplate client list only (c. 2023). Scope unknown.
- **Trenes.com (Spain)**: PSP not identified. The T&Cs refer only to *"el proveedor de pagos"*.

### Orchestration status
**Unconfirmed: multi-PSP with self-described per-method backup; the orchestrator, if any, is not identified.** The ixigo name appears in Juspay's boilerplate, but there is no case study, SDK evidence or job listing. ixigo's own 2024–25 statements describe Razorpay-native features. **Score 0 (⬜). Pitch as orchestration-aware.**

### Buying signals
- 🚀 **International expansion:** 60% of **Trenes.com (Spain)**, SPA 13 Feb 2026, consolidated 1 Mar 2026. **IXIGO PTE. LTD. (Singapore)** incorporated 18 Dec 2025. ([Annual Report](https://rocket.ixigo.com/investors/Le-Travenues-Technology-Limited---Annual-Report-FY-2025-26-new.pdf); [Skift](https://skift.com/2026/02/13/ixigo-makes-its-first-major-international-acquisition-what-this-means/))
- 💰 **Prosus (MIH Investments One B.V.): ₹1,295.6 Cr for 10.1%**, allotted 12 Nov 2025. Funds are earmarked partly for "selective inorganic opportunities" ([Annual Report](https://rocket.ixigo.com/investors/Le-Travenues-Technology-Limited---Annual-Report-FY-2025-26-new.pdf); [Entrackr](https://entrackr.com/news/prosus-to-acquire-101-stake-in-ixigo-for-rs-1296-cr-10547000))
- 🏨 **Hotels push:** approved buying 54.66% of **Brevistay** for ₹65.69 Cr, Jun 2026 ([AltexSoft](https://www.altexsoft.com/travel-industry-news/ixigo-bets-6-9-million-on-brevistay-as-hotels-move-up-its-agenda/))
- 📈 **Payment gateway charges ₹70.5 Cr in FY26 (+21.5%)**, rising *"due to … higher transaction volumes processed through payment gateways"* ([Annual Report](https://rocket.ixigo.com/investors/Le-Travenues-Technology-Limited---Annual-Report-FY-2025-26-new.pdf))
- ⚠️ **Failed-debit complaints still arriving:** 2,449 complaints on consumercomplaints.in, the latest dated 6 Oct 2026, mostly "money debited, ticket not booked" ([consumercomplaints.in](https://www.consumercomplaints.in/ixigo-b115673))

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Ixigo` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 17 / 29
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | **+5** | ✅ **SOURCED (floor): ≥4.06M/month.** FY26 Monthly Transacting Users = **4.06M** (FY25 3.34M), [Annual Report p.15](https://rocket.ixigo.com/investors/Le-Travenues-Technology-Limited---Annual-Report-FY-2025-26-new.pdf). Each MTU makes at least one transaction a month, so this is a floor. Cross-check: FY26 passenger segments 104.12M trains + 10.74M flights + 26.66M buses = **141.52M/yr ≈ 11.8M segments/month** (a segment is a passenger-leg, not a payment). **Billing unit:** one booking payment, which can cover several passengers. Either way it is ~40× the ≥100k band. |
| Orchestration status | 0 | ⬜ **Uncertain.** Juspay appears only in a 2023 vendor client list. ixigo self-describes "backup for each of the methods" but names no layer. Not None-detected, so +4 can't be awarded; not confirmed regional, so +3 can't either. |
| 3+ countries | +3 | ✅ Legal entities in **India, Singapore and Spain** (Annual Report §4). ❗ On traffic alone it fails: only India is >1%. |
| Multiple PSPs | +3 | ✅ **Razorpay** (2024, 2025 case studies) + **Cashfree** (2022 case study), plus the self-stated "backup for each of the methods" (2025). ⚠️ Cashfree evidence is 4 years old. |
| Local rail or licensing gap in a top-3 market | 0 | ❌ India (93.55%) has UPI, RuPay, netbanking, cards and EMI, all sourced. UAE and US are not APAC rail markets. |
| Recent expansion | +2 | ✅ Trenes.com (Spain) acquisition, Feb–Mar 2026. Singapore holdco, Dec 2025. Brevistay, Jun 2026. |
| Payment issues reported | +2 | ✅ **Moderate–high.** 2,449 complaints on consumercomplaints.in (861 unresolved), with a recurring "money debited, ticket not booked" theme through 6 Oct 2026. ⚠️ No complaint attributes the root cause (IRCTC vs bank vs ixigo). |
| Funding >$10M | +2 | ✅ Prosus ₹1,295.6 Cr (≈US$146M `[ESTIMATE — FX not sourced]`), allotted **12 Nov 2025**, inside 12 months. |
| High traffic outside home | 0 | ❌ India is 93.55% of ixigo.com web traffic. |
| Competitor using orchestration | 0 | ⬜ OTA *peers* are confirmed on Juspay (Agoda, tiket.com, Wego, TravClan, IndiGo stories). No **direct Indian competitor** is confirmed: MakeMyTrip's Juspay link is a 2016 client list, and redBus's 2026 evidence is **Cashfree** multi-processor. |
| Payment job postings | 0 | ⬜ A "Product Manager – Payments" listing exists on an aggregator, undated `[UNVERIFIED — search summary only]`. |

**Computed tier:** 17 → ⭐ High Priority.

**Analyst override → 🟢 Medium.** Reasoning:
1. **Double-counting one fact.** "3+ countries" (+3) and "recent expansion" (+2) both fire off **the single Trenes deal** and the holdco set up to carry it. Without that, the score would be 14 on an India-only footprint.
2. **The incremental geography is out of territory.** The new market is **Spain (EMEA)**. On APAC payment volume, ixigo is a **one-country, UPI-first** business: 80% of users pay by UPI ([Razorpay 2024](https://razorpay.com/blog/ixigo-unlocks-1-click-payments-with-razorpay-turbo-upi/)), and the blended PG cost is already low (~0.38% of GTV, derived below). That leaves little room for an MDR-reduction or local-rail pitch.
3. **The orchestration status that decides the motion is unknown.** If Juspay is live, this is a displacement sale into an India-only, already-orchestrated stack. That is the hardest version of this deal.
4. **What keeps it above 🔴:** very large sourced volume (≥4M transacting users/month), a stated obsession with success rate plus a published rupee value for SR uplift, fresh capital for acquisitions, and a brand-new cross-border stack (Trenes).

**What would restore ⭐:** (a) evidence that Juspay is *not* live (greenfield, +4 → 21), (b) an ixigo launch in an APAC market outside India (the AR names Vietnam, Japan, South Korea and Indonesia as outbound destinations "witnessing strong traction"), or (c) a payments-platform hire or RFP.

### Source Notes
- ✅ FY26 GTV, revenue, MTU, passenger segments, PG charges, entities, Prosus allotment, Trenes structure: ixigo FY26 Annual Report, downloaded and parsed first-hand.
- ✅ Razorpay quotes ("preferred Payment Aggregator", "backup for each of the methods", "2.43% … 5 Cr", "80% … UPI", "primary focus … success rates"): fetched and verified first-hand.
- ✅ Cashfree pre-auth case study (23 May 2022): fetched and verified first-hand.
- ✅ Juspay boilerplate "…Airtel, Ixigo, Axis Bank…": fetched and verified first-hand. Juspay story 404s were verified against a control.
- ✅ consumercomplaints.in counts (2,449 / 1,588 / 861, updated 6 Oct 2026): fetched first-hand.
- ⚠️ Trenes price (€11.7M for 60%) and Trenes CY25 financials (~₹60 Cr revenue, ~₹15 Cr PAT): agent-fetched Skift/Inc42. The Annual Report gives the consideration as "INR 1,224.34" (units as printed; AR tables are in ₹ million), which is consistent.
- ⚠️ International-card acceptance issues, Trustpilot wallet-refund complaints, AbhiBus refund-as-credit: search summary only.
- ⚠️ TAL `Est. Revenue ~$100M (FY25)`: superseded by FY26 revenue ₹1,228 Cr (≈US$140M `[ESTIMATE — FX not sourced]`).

### Success Case Alternatives
- *No Yuno customer case study was retrieved in this run (y.uno is blocked in some sessions), so none is named here.* Look for a Yuno case on **high-volume travel/ticketing with approval-rate uplift and multi-currency expansion**. The profile match is a large domestic-wallet-first OTA adding a second-currency business by acquisition. Confirm before citing.

---

## Executive Summary

ixigo (Le Travenues Technology Ltd) is India's AI-led train/bus/flight OTA. FY26 GTV was ₹18,692.7 Cr, with 4.06M monthly transacting users and 141.5M passenger segments. In 2026 it made its first international move: a Singapore holdco and 60% of Spain's Trenes.com. The payment stack is **Razorpay-led and UPI-first (80% of users)**. Cashfree has been used for train pre-auth refunds, and ixigo describes "backup for each of the methods." The TAL's Juspay tag rests on a single 2023 vendor boilerplate mention and is **unconfirmed**. The opportunity is **success-rate economics at scale** (ixigo has put its own rupee number on it) plus **a group payments layer that spans the India stack and the new EUR business**. Motion: **treat as orchestration-aware (displacement posture) until Juspay status is confirmed.**

---

### Section 1: Website Traffic Analysis by Country

**Data source:** Path 1, **SimilarWeb (supplied 2026-10-19)**, from `accounts/traffic/ixigo.md`. Sales Intelligence view; Jul–Sep 2026; worldwide; desktop + mobile web; **ixigo.com only**. 3-month total 32.48M visits, **avg 10.82M/month**, device split desktop 21.53% / mobile web 78.47%. Global rank not captured.

**Caveats carried from the supplied file (all apply):**
1. Shares only. Per-country visits below are **[DERIVED from supplied share, not a SimilarWeb figure]** = share × 10.82M.
2. Single-domain. **confirmtkt.com, abhibus.com and trenes.com were not pulled.** trenes.com in particular would put Spain on the map.
3. **Mobile-app traffic is excluded.** ixigo is app-first (810.94M lifetime downloads across brands, per the AR), so web traffic heavily understates activity and must **not** be used to size transactions.
4. The country split is a market-mix signal only.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | India | 93.55% — **high priority** | ~10.12M [DERIVED] | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | United Arab Emirates | 0.74% | ~80k [DERIVED] | Not supplied | same |
| 3 | United States | 0.60% | ~65k [DERIVED] | Not supplied | same |
| 4 | Singapore | 0.49% | ~53k [DERIVED] | Not supplied | same |
| 5 | United Kingdom | 0.30% | ~32k [DERIVED] | Not supplied | same |
| 6 | Saudi Arabia | 0.29% | ~31k [DERIVED] | Not supplied | same |
| 7 | Canada | 0.24% | ~26k [DERIVED] | Not supplied | same |
| 8 | Kazakhstan | 0.21% | ~23k [DERIVED] | Not supplied | same |
| 9 | Russia | 0.20% | ~22k [DERIVED] | Not supplied | same |
| 10 | Pakistan | 0.15% | ~16k [DERIVED] | Not supplied | same |

Top 10 = 96.77%. Non-India listed = 3.22%. The non-India tail (UAE, US, UK, Saudi, Canada) reads as NRI/diaspora booking Indian travel. That is an *outbound cross-border* pattern (APAC ref §3), but at ~3% of web traffic it is a supporting point only. **Only India exceeds 5%.** Top-10 markets with no entity: UAE, US, UK, Saudi, Canada, Kazakhstan, Russia, Pakistan.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Gurugram, Haryana, India. Incorporated 3 June 2006 (New Delhi) as a private company; converted to a public company in 2021; listed June 2024. Founded 2007 by Aloke Bajpai and Rajnish Kumar ([Q4 FY26 media release](https://nsearchives.nseindia.com/corporate/IXIGO_21052026175538_Regulation_30_Media_Release_21052026.pdf)).

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| India | Le Travenues Technology Limited | CIN L63000HR2006PLC071540 | [Annual Report FY26](https://rocket.ixigo.com/investors/Le-Travenues-Technology-Limited---Annual-Report-FY-2025-26-new.pdf) |
| India | Zoop Web Services Private Limited (62%) | Not found | same |
| India | Freshbus Private Limited (associate, 25.66%) | Not found | same |
| Singapore | IXIGO PTE. LTD. (100%, inc. 18 Dec 2025) | UEN not found | same |
| Spain | Ixigo Europe, S.L. (100%) | Not found | same |
| Spain | Online Travel Solutions, S.L. "Trenes" (60%, via IXIGO PTE. LTD.) | NIF B-66144098 | [trenes.com T&Cs](https://www.trenes.com/condiciones.php) |
| Spain | Squad As A Service, S.L. (associate, 45.02%) | Not found | [Annual Report FY26](https://rocket.ixigo.com/investors/Le-Travenues-Technology-Limited---Annual-Report-FY-2025-26-new.pdf) |

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| India | ✅ #1 (93.55%) | ✅ | n/a (local) | No |
| UAE | ✅ #2 (0.74%) | ❌ | Not researched (EMEA) | Low. Likely NRIs paying with foreign cards into the Indian entity |
| United States | ✅ #3 (0.60%) | ❌ | No | Low. Same NRI pattern |
| Singapore | ✅ #4 (0.49%) | ✅ (holdco) | No | Low |
| UK | ✅ #5 (0.30%) | ❌ | No | Low |
| Spain | ❌ (not in ixigo.com top 10; trenes.com not pulled) | ✅ ×3 | n/a | Separate stack. Not cross-border, but a **second, unconnected payments estate** |

> *Warning: Potential cross-border operation in UAE, US and UK. No local entity found. Any foreign-card payments from NRI users are processed cross-border into the Indian entity. Whether ixigo accepts international cards at all is **unverified**: one app-aggregator summary mentions "booking issues with international cards" `[UNVERIFIED — search summary only]`.* At under 1% traffic each, these are supporting details, not the spine.

> **MANUAL:** ixigo.com returned HTTP 403 to automated fetches, so the T&Cs and privacy policy were not read. Check them for a named processor.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| India | **Razorpay**: cards (TokenHQ, Native OTP, CVV-less), *"preferred Payment Aggregator for several years"*; +2.43% card SR in one month, ">5 Cr incremental GTV" (15 May 2025) | [Provider Case Study] | https://razorpay.com/blog/from-drop-offs-to-takeoffs-how-razorpays-card-payments-powered-ixigos-growth/ |
| India | **Razorpay Turbo UPI** (1-Click UPI in app); *"trusted payment partner for years"*; UPI time cut from 18–20s to under 4s (19 Jul 2024) | [Provider Case Study] | https://razorpay.com/blog/ixigo-unlocks-1-click-payments-with-razorpay-turbo-upi/ |
| India | **Cashfree Payments**: Payment Gateway pre-authorisation on train tickets, voided on failed berth allocation for instant refund (23 May 2022) | [Provider Case Study] | https://www.cashfree.com/case-study/ixigo-provides-a-hassle-free-booking-experience-and-instant-refunds-to-train-travellers-with-pre-authorization-by-cashfree-payments/ |
| India | **Juspay**: "Ixigo" in a client list; product unspecified (c. 2023) | [Press Release] (vendor boilerplate) | https://juspay.io/newsroom/juspay-to-power-payments-for-india-s-leading-airline-indigo |
| India | **AU Small Finance Bank**: co-branded credit card (Visa Nov 2023; RuPay variant Jul 2024). This is an issuer partnership, not acquiring | [Press Release] | https://www.aviation-defence-universe.com/ixigo-and-au-small-finance-bank-launch-rupay-variant-of-their-co-branded-travel-credit-card |
| Spain | **Trenes.com**: PSP not named; T&Cs (18 Sep 2026) refer to *"el proveedor de pagos"*, temporary fund authorisations and SCA. No Adyen/Stripe/Redsys/PayPal/Bizum strings on the homepage | [Terms/Privacy Policy] | https://www.trenes.com/condiciones.php |

**Train payments are ixigo's own volume.** The Cashfree pre-auth flow runs on ixigo's gateway, not IRCTC's iPay. The AR's PG-charge line (₹70.5 Cr) and "funds in transit … collected from customers through cards/net banking/UPI" both sit on ixigo's own books.

**Self-stated redundancy:** *"By integrating multiple payment methods and backup for each of the methods…"* (Razorpay, May 2025). Verified first-hand.

**Not found:** PayU, Paytm PG, BillDesk, CCAvenue, PhonePe PG, Adyen, Stripe, Checkout.com, Worldpay, Braintree. PSPs for ConfirmTkt and AbhiBus specifically. (PhonePe is a *distribution* partner: ixigo powers bookings inside PhonePe.)

#### 3B. Payment Orchestrator

**Classification: Unconfirmed. Leans "Regional orchestrator (Juspay)" on weak evidence; "In-house layer" is equally plausible.**
- For Juspay: vendor boilerplate "Ixigo" (c. 2023); TAL tag; self-described per-method backup.
- Against Juspay: no customer story (404, controlled); no SDK, job-listing or LinkedIn evidence; ixigo's 2024–25 statements use Razorpay-native products (TokenHQ, Turbo UPI) that suggest direct integration. A YourStory report (Mar 2025) says Razorpay, PhonePe and Cashfree ended partnerships with Juspay in late 2024 `[UNVERIFIED — search summary only]`.

> *Treat as orchestration-aware. The opening is success-rate economics at their scale and a group layer that spans India and the new international business. It is not the case for orchestration itself.*

> **MANUAL:** Decompile or inspect the ixigo, ConfirmTkt and AbhiBus Android APKs (or check AppBrain/Exodus SDK lists) for `in.juspay.hypersdk` vs `com.razorpay`. That answers the motion question in five minutes.

---

### Section 4: Alternative & Local Payment Methods

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| India | UPI (incl. Razorpay Turbo 1-Click UPI); "primary payment method for 80% of our user base" | Bank transfer / A2A | Active in checkout | [Razorpay 2024](https://razorpay.com/blog/ixigo-unlocks-1-click-payments-with-razorpay-turbo-upi/); [ixigo trains page](https://www.ixigo.com/travel-stories/9-reasons-to-book-train-tickets-on-the-ixigo-trains-app-story-1137329) |
| India | UPI on ConfirmTkt | Bank transfer / A2A | Active (site) | https://www.confirmtkt.com/ |
| India | Credit/debit cards | Cards | Active in checkout | [Razorpay 2025](https://razorpay.com/blog/from-drop-offs-to-takeoffs-how-razorpays-card-payments-powered-ixigos-growth/); [Play listing](https://play.google.com/store/apps/details?id=com.ixigo&hl=en) |
| India | Cards / netbanking / UPI (named as collection rails) | Cards / A2A | Mentioned in docs (AR "funds in transit" note) | [Annual Report FY26](https://rocket.ixigo.com/investors/Le-Travenues-Technology-Limited---Annual-Report-FY-2025-26-new.pdf) |
| India | Netbanking | Bank transfer / A2A | Mentioned in docs | [Play listing](https://play.google.com/store/apps/details?id=com.ixigo&hl=en) |
| India | RuPay credit (AU SFB co-brand; linkable to UPI) | Cards | Mentioned in press | [ADU](https://www.aviation-defence-universe.com/ixigo-and-au-small-finance-bank-launch-rupay-variant-of-their-co-branded-travel-credit-card) |
| India | ixigo Credit: PayLater and EMI up to ₹1L, NBFC-underwritten (NBFC not named) | BNPL/Instalments | Active in checkout (ixigo page) | [ixigo](https://www.ixigo.com/travel-stories/ixigo-credit-your-ticket-to-stress-free-travel-story-1185600) |
| India | Card no-cost EMI (RBL offer; expired) | BNPL/Instalments | Mentioned in docs | [RBL](https://www.rblbank.com/offers-and-promotions/ixigo-flights-hotels) |
| India | Simpl (past promo) | BNPL/Instalments | Mentioned in docs (possibly inactive) | [ixigo](https://www.ixigo.com/travel-stories?p=1184875) |
| India | Wallets (generic "UPI, cards, or wallets") | Digital wallet | Mentioned in docs | [ixigo money page](https://www.ixigo.com/travel-stories/ixigo-money-your-virtual-travel-currency-story-1183909) |
| India | Named wallets: Paytm, PhonePe, Amazon Pay, MobiKwik | Digital wallet | Not found | — |
| India | ixigo money (closed-loop credit, 60-day expiry) | Digital wallet (closed-loop) | Active | [ixigo money page](https://www.ixigo.com/travel-stories/ixigo-money-your-virtual-travel-currency-story-1183909) |
| India | UPI Autopay / e-mandate | Direct debit / mandate | Not found. No subscription product found, so not a gap | — |
| Global | International cards (NRI users) | Cards | Unknown, checkout not accessible | — |
| Global | Apple Pay, Google Pay (global), PayPal | Digital wallet | Not found | — |
| Spain | Trenes.com: methods "indicated during purchase" | — | Unknown, checkout not accessible | [trenes.com T&Cs](https://www.trenes.com/condiciones.php) |

**No sourced dominant-rail gap in India.** UPI, cards, RuPay, netbanking and EMI/PayLater are all present. The rail-coverage pitch does not apply here and must not be used.

> **MANUAL:** Book a test train ticket with a non-Indian card to settle the international-card question, and walk the trenes.com checkout to identify its PSP and APMs (Bizum, PayPal).

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Checkout errors / UPI-wallet-specific failures: "money debited, train ticket not booked" (UPI via GPay/Paytm; also a PNB credit card). The booking isn't shown in My Trips | consumercomplaints.in (2,449 total; 861 unresolved; updated 6 Oct 2026) | **High** (recurring) | Nov 2025 – 6 Oct 2026 | https://www.consumercomplaints.in/ixigo-b115673 |
| Duplicate charges: double debit on one Vande Bharat ticket | consumercomplaints.in | Isolated | 2 Jul 2026 | same |
| Duplicate charges: flight card charged twice and converted to EMI, no ticket | consumercomplaints.in | Isolated | 5 Nov 2025 | same |
| Slow refunds: airline-cancellation refund not passed on (users say IndiGo confirmed it refunded ixigo) | consumercomplaints.in | Moderate | Dec 2025 – Apr 2026 | same |
| Slow refunds: failed-transaction money sent to ixigo wallet, bank refund took 5–7 days, templated replies | Trustpilot | Moderate | 2025–2026 | https://www.trustpilot.com/review/ixigo.com?page=5 `[UNVERIFIED — search summary only]` |
| AbhiBus: UPI debit with booking unconfirmed; refunds given as app credit | consumercomplaints.in / Trustpilot | Moderate | late 2025 – Feb 2026 | https://www.consumercomplaints.in/abhibus-services-india-transport-bus-ticket-booking-c3533312 `[UNVERIFIED — search summary only]` |

> *The pattern of debit-without-booking on train tickets (UPI-heavy, IRCTC-dependent) suggests the opportunity is in **auth/void orchestration and success-rate routing on the UPI leg**. ixigo already built pre-auth with Cashfree for exactly this in 2022.* ⚠️ No complaint attributes the root cause. Many are likely IRCTC-side booking failures, not PSP failures. **Do not pin these on ixigo's payment stack in outreach.**

Reddit could not be searched (the tool blocks reddit.com). No X or Google Play payment-review data surfaced.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 8 Jun 2026 | Approved buying 54.66% of Brevistay Hospitality for ₹65.69 Cr; invested ₹7.5 Cr in Proactai and ₹4.5 Cr in Vestra.AI | M&A | https://www.altexsoft.com/travel-industry-news/ixigo-bets-6-9-million-on-brevistay-as-hotels-move-up-its-agenda/ |
| 2 | 21 May 2026 | FY26 results: GTV ₹18,692.7 Cr (+25%), revenue ₹1,228 Cr (+34%); ixigo NEXT AI-native app launched | Tech / Results | https://nsearchives.nseindia.com/corporate/IXIGO_21052026175538_Regulation_30_Media_Release_21052026.pdf |
| 3 | 13 Feb 2026 (SPA), consolidated 1 Mar 2026 | 60% of Trenes.com (Online Travel Solutions, S.L.), Spain's #2 train OTA, via IXIGO PTE. LTD.; 45.02% of Sqaas. Remaining 40% of Trenes in two earn-out tranches | Market Expansion / M&A | [Annual Report](https://rocket.ixigo.com/investors/Le-Travenues-Technology-Limited---Annual-Report-FY-2025-26-new.pdf); [Skift](https://skift.com/2026/02/13/ixigo-makes-its-first-major-international-acquisition-what-this-means/) |
| 4 | 18 Dec 2025 | Incorporated IXIGO PTE. LTD., Singapore (100%) | Market Expansion | [Annual Report](https://rocket.ixigo.com/investors/Le-Travenues-Technology-Limited---Annual-Report-FY-2025-26-new.pdf) |
| 5 | 10 Oct 2025 (SSA) → 12 Nov 2025 (allotment) | Prosus / MIH Investments One B.V.: ₹1,295.6 Cr preferential issue at ₹280/share, 10.1% fully diluted. MIH now holds 16.18% | Funding | [Annual Report](https://rocket.ixigo.com/investors/Le-Travenues-Technology-Limited---Annual-Report-FY-2025-26-new.pdf); [Entrackr](https://entrackr.com/news/prosus-to-acquire-101-stake-in-ixigo-for-rs-1296-cr-10547000) |

Also: Q1 FY27 (quarter to 30 Jun 2026) GTV ₹5,524.33 Cr (+19%), revenue ₹356.75 Cr (+13%), flights now the largest vertical by GTV ([Business Standard](https://www.business-standard.com/markets/capital-market-news/ixigo-posts-pat-of-rs-34-24-crore-for-q1-fy27-clocks-gtv-of-rs-5-524-crore-126080700276_1.html)). The AR outlook names **Vietnam, Japan, South Korea, Oman, Kenya and Indonesia** as outbound destinations "witnessing strong traction", plus "early signs of organic inbound travel … from the Middle East and Southeast Asia."

*No public payment-related RFP found.* No payment aggregator licence application found. Payments leadership on record: **Ameya Sood, AVP – Product (Payments)** (Razorpay interviews, 2024 and 2025). "Product Manager – Payments" job listing: aggregator only, undated `[UNVERIFIED]`.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | FY26 (Annual Report) | PG charges ₹704.98M (+21.52%), *"due to an overall rise in the Gross Transaction Value, leading to higher transaction volumes processed through payment gateways"* | Cost line growing with volume | [Annual Report](https://rocket.ixigo.com/investors/Le-Travenues-Technology-Limited---Annual-Report-FY-2025-26-new.pdf) |
| 2 | 15 May 2025 | Razorpay card case study: +2.43% card SR, >₹5 Cr incremental GTV in a month; "backup for each of the methods" | Success-rate economics; multi-provider | [Razorpay](https://razorpay.com/blog/from-drop-offs-to-takeoffs-how-razorpays-card-payments-powered-ixigos-growth/) |
| 3 | Jul 2025 (Q1 FY26) | ixigo Credit: No-Cost EMI and Book Now Pay Later via bank/NBFC partners | Instalments in-house | [ixigo](https://www.ixigo.com/travel-stories/ixigo-credit-your-ticket-to-stress-free-travel-story-1185600) `[launch date: search summary only]` |
| 4 | Sep 2025 (FY26) | ixigo powers flight bookings inside CRED for the CRED IndusInd RuPay credit card | Distribution, not processing | [Annual Report](https://rocket.ixigo.com/investors/Le-Travenues-Technology-Limited---Annual-Report-FY-2025-26-new.pdf); [The Week](https://www.theweek.in/wire-updates/business/2025/09/16/dcm65-ixigo.html) |
| 5 | 19 Jul 2024 | Razorpay Turbo UPI live; UPI = 80% of users; "primary focus … success rates" | UPI-first; SR-obsessed | [Razorpay](https://razorpay.com/blog/ixigo-unlocks-1-click-payments-with-razorpay-turbo-upi/) |

No provider removals found.

---

### Section 8: Checkout Experience Audit

*Full checkout flow not accessible. www.ixigo.com returned HTTP 403 to automated fetches and the `/payment-options` path 404s. Findings are limited to publicly observable elements.*

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | Native in-app, with Razorpay native features (Native OTP, Turbo UPI in-app) | Good | Per Razorpay case studies |
| Guest checkout | Not found | — | |
| Steps to complete payment | UPI cut from 18–20s to under 4s (1-Click UPI) | Good | Razorpay 2024 |
| Card input experience | TokenHQ (RBI tokenisation), CVV-less, Native OTP | Good | Razorpay 2025 |
| Payment methods visible | UPI, cards, netbanking, wallets, PayLater & Easy EMI | Good | Play listing / ixigo pages |
| Location-based method display | Not found | — | |
| Instalment / EMI options | ixigo Credit PayLater/EMI (up to ₹1L), card EMI | Good | |
| 3DS implementation | Native OTP (in-app card 2FA) | — | Version not detected |
| PCI indicator | PSP tokenisation (TokenHQ) | — | See Section 9 |
| Mobile responsiveness | 78.47% of web visits are mobile web; app-first | — | Not audited |
| Multi-currency / local pricing | Not found (India INR only; Trenes EUR on a separate site) | — | |
| Saved payment methods | Tokenised cards (TokenHQ) | Good | |
| Error message clarity | Complaints describe failed bookings not shown in My Trips | Poor `[from complaints, not observed]` | |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found | — |
| Card data handling | Not found directly | — |
| Recommended Yuno integration | SDK (mobile app-first; keeps card data in Yuno's vault) | Analyst recommendation |

*No direct PCI compliance documentation found publicly for ixigo.*

`[INFERENCE, not confirmed]`: ixigo uses Razorpay TokenHQ and native card flows, so card data is likely tokenised at the PSP and ixigo's PCI scope is likely reduced. The 2019 security incident involved user accounts (emails and hashed passwords), not card data ([Rankiteo](https://blog.rankiteo.com/ixi3060830103125-ixigo-breach-february-2019/), not fetched).

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: Success rate is their stated #1 metric, and they've published its rupee value**
> **Evidence:** S7: "primary focus in payment is centered around success rates" (2024); +2.43% card SR = ">5 Cr incremental GTV" in one month (2025). S12: ≥4.06M monthly transacting users, ₹18,692.7 Cr GTV. S5: recurring "debited, not booked" complaints.
> **Pain Point:** At ~₹1,560 Cr GTV/month (derived), every basis point of SR is real money. Their own data shows each card-SR point is worth crores a month, and UPI (80% of users) has its own failure modes.
> **Yuno Value Proposition:** Smart routing, cascading retries and real-time PSP health across UPI and cards, on top of whatever providers they already hold. Adds providers without re-integrating.
> **Best Success Case:** A high-volume travel/ticketing approval-rate case. Confirm a Yuno case before citing.
> **Outreach Angle:** "You've publicly put a number on what ~2.4 points of card success rate is worth in a month. Curious how much headroom you think is left on UPI at 4M transacting users."
> **Suggested Subject Line:** ixigo's ₹5 Cr success-rate month

> **Insight #2: Two payment estates on two continents after Trenes, with no common layer**
> **Evidence:** S2: IXIGO PTE. LTD. (SG) holds 60% of Online Travel Solutions, S.L. (Spain), plus Ixigo Europe, S.L. S3A: India stack is Razorpay/Cashfree; Trenes PSP unknown, T&Cs reference a separate "proveedor de pagos." S6: Prosus capital earmarked for "selective inorganic opportunities"; two further Trenes tranches due.
> **Pain Point:** Each acquisition brings its own PSPs, contracts and reporting. Group finance can't see auth rates, costs or reconciliation across INR and EUR in one place. An India-built stack doesn't acquire in Europe.
> **Yuno Value Proposition:** One integration and one dashboard across Indian rails and European acquirers/APMs. Acquired businesses plug in without a re-platform.
> **Best Success Case:** A multi-market merchant consolidating stacks post-acquisition. Confirm before citing.
> **Outreach Angle:** "Trenes is your first business that doesn't settle in rupees. Is the plan to keep its payments separate, or bring it onto one layer before the next acquisition?"
> **Suggested Subject Line:** Trenes + ixigo: one payments layer or two?
> ⚠️ Spain is EMEA. Use this as the *why now*, and loop in EMEA if it becomes a European acquiring deal.

> **Insight #3: Multi-provider already, with an unclear routing layer**
> **Evidence:** S3A: Razorpay (preferred PA) + Cashfree (train pre-auth) + "backup for each of the methods." S3B: Juspay only in a 2023 boilerplate. S11C: OTA peers Agoda, tiket.com and Wego are on published orchestration case studies; redBus runs Cashfree multi-processor routing (Apr 2026).
> **Pain Point:** If failover is in-house, it's engineering capacity competing with their AI roadmap (ixigo NEXT, TARA). If it's a regional orchestrator, it was built for India, not for their new international footprint.
> **Yuno Value Proposition:** Reach beyond India (EUR, outbound destinations) plus routing intelligence, without them maintaining it.
> **Best Success Case:** Confirm before citing.
> **Outreach Angle:** "You've built backup for every payment method, which most OTAs haven't. Who owns that logic today, your team or a vendor?" (a discovery question that also settles the motion)
> **Suggested Subject Line:** Who owns ixigo's payment failover?

> **Insight #4: PG cost is growing with volume (secondary)**
> **Evidence:** S7: PG charges ₹70.5 Cr FY26, +21.5%. S12: ≈0.38% of GTV (derived).
> **Pain Point:** Modest as a percentage (UPI is largely zero-MDR in India), but ₹70 Cr/yr and rising with the 25% GTV growth.
> **Yuno Value Proposition:** Cost-aware routing on the card/EMI share. **Secondary only.** Don't lead with MDR on a UPI-first merchant.
> **Outreach Angle:** Use only in a business-case follow-up, not as an opener.

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. In your Razorpay interview you put a number on it: about 2.4 points of card success rate was worth over ₹5 Cr of GTV in a single month. At 4M+ transacting users a month, where's the next point coming from?
2. Trenes is the first ixigo business that doesn't settle in rupees. Is it staying on its own payment stack?
3. With Prosus capital earmarked for acquisitions, each new business brings its own PSPs. Are you planning one payments layer for the group or one per brand?

**Cold call openers (conversational, one sentence each):**
1. "Saw you've built backup for every payment method. Curious whether that routing logic is in-house or a vendor today?"
2. "Congrats on Trenes. How are you thinking about payments for a EUR business sitting under a Singapore holdco?"
3. "UPI is 80% of your users. When a train booking debits but doesn't confirm, how much of that is the rail or the PSP versus IRCTC?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| MakeMyTrip (incl. Goibibo, redBus) | makemytrip.com | India | FY26 gross bookings $10,390.8M; revenue $1,044.0M | Flights, hotels, buses, trains (IN) | Juspay: 2016 client list only `[stale/unverified]` | [SEC 10-K/20-F](https://www.sec.gov/Archives/edgar/data/0001495153/000119312526318134/mmyt-20260331.htm) |
| redBus (MMT) | redbus.in | India | Not separately disclosed | Buses (vs AbhiBus) | **Cashfree**, multi-processor (2 Apr 2026) | [Cashfree](https://www.cashfree.com/case-study/how-redbus-improved-credit-card-payment-success-rates-by-~4.8-with-cashfree/) |
| EaseMyTrip | easemytrip.com | India | FY25 gross bookings ₹8,691 Cr; revenue ₹587 Cr | Flights, rail, hotels | Not found | [Business News Today](https://business-news-today.com/easemytrips-fy25-report-card-rs-8691cr-in-bookings-new-verticals-and-a-global-push/) |
| Cleartrip (Flipkart) | cleartrip.com | India | FY25 revenue ₹169 Cr; PG charges ₹78.65 Cr | Flights, trains, hotels | Not found (parent Flipkart has a Juspay story; not proof for Cleartrip) | [Entrackr](https://entrackr.com/fintrackr/cleartrip-spent-rs-608-cr-on-discount-and-cashbacks-for-rs-169-cr-net-revenue-in-fy25-10525523) |
| Yatra | yatra.com | India | FY25 revenue ₹7,957M; gross bookings ₹70,910M | Flights, rail, corporate | Not found (Juspay careers claim only `[unverified]`) | [BusinessWire](https://www.businesswire.com/news/home/20250529795206/en) |
| RailYatri / IntrCity | railyatri.in | India | ~₹496–500 Cr FY25 (aggregator/company claim) | Trains + buses (closest model) | Not found | [Inc42](https://inc42.com/company/railyatri/financials/) |
| Zingbus | zingbus.com | India | FY25 revenue ~₹161 Cr | Buses | Not found | [Entrackr](https://entrackr.com/fintrackr/info-edge-backed-zingbus-crosses-rs-150-cr-revenue-in-fy25-10972155) |
| Trainman (Adani) | trainman.in | India | FY23 turnover ₹4.51 Cr | Trains | Not found | [MediaNama](https://www.medianama.com/2023/06/223-adani-acquires-train-ticket-booking-app-trainman/) |

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Agoda | agoda.com | OTA (hotels/flights) | APAC incl. India | Juspay Hyperswitch, 300+ APMs | [Hyperswitch](https://hyperswitch.io/case-studies/agoda/) |
| tiket.com | tiket.com | OTA (trains, flights, hotels) | Indonesia | Juspay customer story; train + flight mix like ixigo | [Juspay](https://juspay.io/customer-stories/tiket) |
| Wego | wego.com | Travel meta + OTA | MENA, India | Juspay (2 countries) | [Juspay](https://juspay.io/customer-stories/wego) |
| Klook | klook.com | Activities / travel | APAC | Adyen APAC partner; +3% authorisation | [Adyen](https://www.adyen.com/knowledge-hub/klook-takes-off-payments-optimization) |
| TravClan | travclan.com | B2B travel | India | Juspay | [Juspay](https://juspay.io/customer-stories/travclan) |
| Traveloka | traveloka.com | OTA | SEA | Not found | — |
| 12Go Asia | 12go.asia | Ground transport OTA (trains/buses) | SEA | Not found. Closest SEA analogue to ixigo's train/bus model | — |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| Agoda | Juspay Hyperswitch | Not dated | OTA | https://hyperswitch.io/case-studies/agoda/ |
| tiket.com | Juspay | Not dated | OTA | https://juspay.io/customer-stories/tiket |
| Wego | Juspay (expanded Sep 2026) | Sep 2026 | Travel meta/OTA | https://juspay.io/customer-stories/wego |
| IndiGo | Juspay | c. 2023 | Airline | https://juspay.io/customer-stories/indigo |
| TravClan | Juspay | Not dated | B2B travel | https://juspay.io/customer-stories/travclan |
| redBus | Cashfree multi-processor (PSP-level, not an orchestrator) | 2 Apr 2026 | Bus OTA | https://www.cashfree.com/case-study/how-redbus-improved-credit-card-payment-success-rates-by-~4.8-with-cashfree/ |
| Cebu Pacific | CellPoint Digital | 2021 → | Airline (PH) | https://www.cellpointdigital.com/articles/casestudies/payment-orchestration-as-a-growth-catalyst-the-cebu-pacific-case-study |

*No direct Indian train/bus competitor confirmed on an orchestrator.*

#### 11D. Prospect Scoring

*Indicative only. Peers were not researched to full-report depth, so most signals are ⬜ and scores are floors. Volume is assumed from public scale, never sourced here.*

| Company | Volume | Orch. | 3+ ctry | Multi-PSP | Rail gap | Expansion | Issues | Funding | Outside home | Comp. orch | Jobs | Floor score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MakeMyTrip | ⚠️ assumed ≥100k (+5) | ⬜ | ⬜ | ⬜ | ❌ | ⬜ | ⬜ | ⬜ | ❌ | ⬜ | ⬜ | 5+ |
| EaseMyTrip | ⚠️ assumed ≥100k (+5) | ⬜ | ⬜ | ⬜ | ❌ | ⬜ (global push, unverified) | ⬜ | ⬜ | ❌ | ⬜ | ⬜ | 5+ |
| Yatra | ⚠️ assumed ≥100k (+5) | ⬜ | ⬜ | ⬜ | ❌ | ⬜ | ⬜ | ⬜ | ❌ | ⬜ | ⬜ | 5+ |
| IntrCity / RailYatri | ⚠️ assumed ≥100k (+5) | ⬜ | ❌ | ⬜ | ❌ | ⬜ | ⬜ | ⬜ (₹250 Cr raise, date unverified) | ❌ | ⬜ | ⬜ | 5+ |
| 12Go Asia | ⬜ | ⬜ | ⬜ (multi-SEA, unverified) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 0+ |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | EaseMyTrip | Direct competitor | India (+ global push) | 5+ (floor) | 🟢 research | No PSP found; orchestrator column blank | ✅ (orch blank) |
| 2 | Yatra | Direct competitor | India | 5+ | 🟢 research | Orchestrator column blank | ✅ (orch blank) |
| 3 | **IntrCity SmartBus** | Direct competitor (bus) | India | 5+ | 🟢 research | ~₹500 Cr revenue, profitable (company claim) | ❌ **Not on TAL (only under RailYatri): genuine find** |
| 4 | 12Go Asia | Peer (ground transport) | SEA | 0+ | 🟢 research | Train/bus model in multi-rail SEA | ✅ (orch blank) |
| 5 | Traveloka | Peer OTA | SEA | 0+ | 🟢 research | ⚠️ TAL lists HQ as "India"; actually Jakarta. **Fix the TAL row** | ✅ |
| 6 | MakeMyTrip | Direct competitor | India | 5+ | 🟡 displacement? | TAL says Juspay (2016 evidence only) | ✅ |
| 7 | redBus | Direct competitor (bus) | India | — | 🟡 | Cashfree multi-processor confirmed 2026; TAL says Juspay (**conflict**) | ✅ |
| 8 | RailYatri | Direct competitor | India | 5+ | 🟢 research | Closest train+bus model | ✅ |
| 9 | Zingbus | Direct competitor (bus) | India | — | 🔴 smaller | ~₹161 Cr revenue | ✅ |
| 10 | Agoda | Peer OTA | APAC | — | 🟡 displacement | Juspay Hyperswitch incumbent | ❌ Not on TAL |

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | ₹1,228 Cr FY26 (+34%) ≈ US$140M `[ESTIMATE — FX not sourced]` | [Q4 FY26 media release](https://nsearchives.nseindia.com/corporate/IXIGO_21052026175538_Regulation_30_Media_Release_21052026.pdf); [AR](https://rocket.ixigo.com/investors/Le-Travenues-Technology-Limited---Annual-Report-FY-2025-26-new.pdf) |
| GMV / Gross Transaction Value | **₹18,692.7 Cr FY26 (+25%)**. Flights ₹7,514.6 Cr, Trains ₹8,279.0 Cr, Buses ₹2,620.7 Cr. Q1 FY27 ₹5,524.3 Cr (+19%) | AR segment snapshots; Business Standard |
| Average Transaction Value (USD) | ✅ DERIVED **~₹1,321 per passenger segment** = ₹186,926.84M GTV ÷ 141.52M segments (both from AR). *Per segment, not per payment* | Calculated |
| Est. Annual Transactions | ≥48.7M payments/yr (floor: 4.06M MTU × 12); 141.52M passenger segments | Calculated from AR |
| **Monthly transaction count** | **✅ SOURCED (floor): ≥4.06M/month.** FY26 Monthly Transacting Users 4.06M ([AR p.15](https://rocket.ixigo.com/investors/Le-Travenues-Technology-Limited---Annual-Report-FY-2025-26-new.pdf)). Each is ≥1 transaction. Billing unit: one booking payment (may cover multiple passengers). Passenger segments ≈11.8M/month as an upper-side cross-check | Band: ≥100,000 → +5 |
| Active Customers / Users | MAU 82.98M; MTU 4.06M; lifetime registered 379.48M; lifetime transacted 56.38M; repeat transaction rate 85.55% | AR |
| Primary Currency | INR (Trenes: EUR) | AR |
| Top 3 Markets by Revenue | India (≈all); Spain (Trenes, from 1 Mar 2026; CY25 revenue ~₹60 Cr per Inc42 `[agent-fetched]`) | AR; [Inc42](https://inc42.com/buzz/ixigo-to-acquire-two-european-travel-tech-startups-for-%E2%82%B9130-cr/) |
| Billing channel split (web vs app store) | Not applicable: travel bookings are paid via the merchant's own PSPs, not IAP. App-first, so traffic is app-heavy | — |
| Payment gateway charges | **₹704.98M FY26 (+21.52%)** consolidated; ✅ DERIVED **≈0.38% of GTV** (704.98 ÷ 186,926.84) | AR "Other Expenses" table |
| Payment mix | UPI = primary method for **80% of users** (2024) | [Razorpay](https://razorpay.com/blog/ixigo-unlocks-1-click-payments-with-razorpay-turbo-upi/) |

---

### Overall Research Confidence

**Medium-High.** **Traffic was supplied** (SimilarWeb Sales Intelligence, ixigo.com only, web only). It is reliable as a market-mix signal and deliberately not used for sizing.
- **Strong:** financials, volume, entities, M&A and funding come from the audited FY26 Annual Report and exchange filings, read first-hand. The PSP evidence (Razorpay ×2, Cashfree) and the Juspay boilerplate were verified first-hand.
- **Limited:** orchestration status, the decisive question for the motion, is unresolved. The checkout, T&Cs and privacy policy were unreachable (ixigo.com returns 403 to automated fetches), so Section 8 is partial. Complaints lack root-cause attribution. Reddit was not searchable. The Trenes PSP is unknown.

---

### Manual Research Recommendations

> **Area:** Orchestration status (S3B), which decides the motion and swings the score by up to 4 points
> **Why it matters:** Juspay-live means a displacement pitch into an India-only stack; not-live means greenfield, +4 and back to ⭐.
> **Suggested manual action:** Check the ixigo, ConfirmTkt and AbhiBus Android APKs (AppBrain/Exodus/APK decompile) for `in.juspay.hypersdk` vs `com.razorpay`. On a live booking, inspect checkout network calls in DevTools (`api.juspay.in` vs `api.razorpay.com`).

> **Area:** International card acceptance (S4)
> **Why it matters:** NRI traffic from UAE/US/UK/Canada. If foreign cards fail, there's a concrete hook.
> **Suggested manual action:** Attempt a flight booking with a non-Indian card on web and app.

> **Area:** Trenes.com PSP and APMs (S3A/S4)
> **Why it matters:** This anchors the "two estates" angle.
> **Suggested manual action:** Walk the trenes.com checkout to payment step; note the PSP iframe/redirect and whether Bizum/PayPal are offered. Pull a SimilarWeb split for trenes.com.

> **Area:** Monthly transaction count is sourced as a floor (MTU), not an exact payment count
> **Why it matters:** Not decision-relevant (40× the top band), but a discovery call can confirm payments/month by rail.
> **Suggested manual action:** Ask: "Roughly how many payment attempts a month, and what share is UPI vs cards?"

---

### Appendix: All Source URLs

**Traffic (S1):** `accounts/traffic/ixigo.md` (SimilarWeb Sales Intelligence, supplied 2026-10-19)

**Financials / entities / developments (S2, S6, S12):**
- https://rocket.ixigo.com/investors/Le-Travenues-Technology-Limited---Annual-Report-FY-2025-26-new.pdf
- https://nsearchives.nseindia.com/corporate/IXIGO_21052026175538_Regulation_30_Media_Release_21052026.pdf
- https://www.business-standard.com/markets/capital-market-news/ixigo-posts-pat-of-rs-34-24-crore-for-q1-fy27-clocks-gtv-of-rs-5-524-crore-126080700276_1.html
- https://entrackr.com/news/prosus-to-acquire-101-stake-in-ixigo-for-rs-1296-cr-10547000
- https://skift.com/2026/02/13/ixigo-makes-its-first-major-international-acquisition-what-this-means/
- https://inc42.com/buzz/ixigo-to-acquire-two-european-travel-tech-startups-for-%E2%82%B9130-cr/
- https://www.altexsoft.com/travel-industry-news/ixigo-bets-6-9-million-on-brevistay-as-hotels-move-up-its-agenda/
- https://www.trenes.com/condiciones.php

**PSP stack (S3):**
- https://razorpay.com/blog/from-drop-offs-to-takeoffs-how-razorpays-card-payments-powered-ixigos-growth/
- https://razorpay.com/blog/ixigo-unlocks-1-click-payments-with-razorpay-turbo-upi/
- https://www.cashfree.com/case-study/ixigo-provides-a-hassle-free-booking-experience-and-instant-refunds-to-train-travellers-with-pre-authorization-by-cashfree-payments/
- https://juspay.io/newsroom/juspay-to-power-payments-for-india-s-leading-airline-indigo
- https://juspay.io/customer-stories (index; ixigo/abhibus/confirmtkt paths 404)
- https://yourstory.com/2025/03/juspay-open-sources-payment-orchestrator-fintech-industry-shakeup-phonepe-razorpay (search summary only)
- https://thepaypers.com/payments/news/ixigo-expands-partnership-with-phonepe

**Payment methods (S4):**
- https://www.ixigo.com/travel-stories/9-reasons-to-book-train-tickets-on-the-ixigo-trains-app-story-1137329
- https://www.ixigo.com/travel-stories/ixigo-credit-your-ticket-to-stress-free-travel-story-1185600
- https://www.ixigo.com/travel-stories/ixigo-money-your-virtual-travel-currency-story-1183909
- https://www.ixigo.com/travel-stories?p=1184875
- https://play.google.com/store/apps/details?id=com.ixigo&hl=en
- https://play.google.com/store/apps/details?id=com.ixigo.train.ixitrain&hl=en
- https://www.confirmtkt.com/
- https://www.rblbank.com/offers-and-promotions/ixigo-flights-hotels
- https://www.aviation-defence-universe.com/ixigo-and-au-small-finance-bank-launch-rupay-variant-of-their-co-branded-travel-credit-card
- https://www.theweek.in/wire-updates/business/2025/09/16/dcm65-ixigo.html

**Complaints (S5):**
- https://www.consumercomplaints.in/ixigo-b115673
- https://www.trustpilot.com/review/ixigo.com?page=5 (search summary only)
- https://www.consumercomplaints.in/abhibus-services-india-transport-bus-ticket-booking-c3533312 (search summary only)

**PCI (S9):** https://blog.rankiteo.com/ixi3060830103125-ixigo-breach-february-2019/

**Competitors (S11):**
- https://www.sec.gov/Archives/edgar/data/0001495153/000119312526318134/mmyt-20260331.htm
- https://www.cashfree.com/case-study/how-redbus-improved-credit-card-payment-success-rates-by-~4.8-with-cashfree/
- https://business-news-today.com/easemytrips-fy25-report-card-rs-8691cr-in-bookings-new-verticals-and-a-global-push/
- https://entrackr.com/fintrackr/cleartrip-spent-rs-608-cr-on-discount-and-cashbacks-for-rs-169-cr-net-revenue-in-fy25-10525523
- https://www.businesswire.com/news/home/20250529795206/en
- https://inc42.com/company/railyatri/financials/
- https://entrackr.com/fintrackr/info-edge-backed-zingbus-crosses-rs-150-cr-revenue-in-fy25-10972155
- https://www.medianama.com/2023/06/223-adani-acquires-train-ticket-booking-app-trainman/
- https://hyperswitch.io/case-studies/agoda/
- https://juspay.io/customer-stories/tiket · https://juspay.io/customer-stories/wego · https://juspay.io/customer-stories/indigo · https://juspay.io/customer-stories/travclan
- https://www.adyen.com/knowledge-hub/klook-takes-off-payments-optimization
- https://www.cellpointdigital.com/articles/casestudies/payment-orchestration-as-a-growth-catalyst-the-cebu-pacific-case-study

</details>
