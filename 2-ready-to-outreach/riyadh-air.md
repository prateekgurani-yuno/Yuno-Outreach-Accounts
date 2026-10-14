# Riyadh Air

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 21 / 29 on the arithmetic → **🟢 Medium, analyst override applied DOWN from ⭐ — see the override note**
**Industry:** Full-service airline — digitally-native, Offer & Order native (no legacy PSS) · **HQ:** Riyadh, **Saudi Arabia**; operating entity reported as "Aviation Service Company" (CR unverified); **wholly owned by the Public Investment Fund** · **Researched:** 2026-10-14 · **First email sent:** —
**Motion:** ⚠️ **COMPETITIVE — CellPoint Digital, the airline-vertical orchestrator, is the confirmed incumbent.** Read the three boxes below before writing a line.

---

> ## 🛑 TERRITORY — this account is in the APAC pipeline on an explicit exception, not on the rules
>
> CLAUDE.md: *"Gulf markets (UAE, Saudi) are **out of territory** — they sit with EMEA… An APAC-HQ'd company
> selling into the Gulf is still in scope; **a Gulf-HQ'd company is not**."* Riyadh Air is Gulf-HQ'd and
> PIF-owned. **Prateek instructed "take this one as exception"** and that instruction is the sole basis
> for this file sitting here. **Both the entities agent and the news agent independently flagged it
> unprompted.** Recorded so it is never mistaken for a precedent or a territory ruling.
>
> The substantive counter-argument, for the record: **seven of the twelve routes launched between June
> and September 2026 are APAC** — Kuala Lumpur, Mumbai, Dhaka, Islamabad, Lahore, Manila, Bangkok — plus
> regulatory approval for Beijing and Shanghai. On destinations this is substantially an APAC airline.
> On HQ it is not. The rule as written is about HQ.

> ## ⚠️ THE MOTION IS COMPETITIVE — do not pitch "you need orchestration"
>
> **CellPoint Digital Payment Orchestration is confirmed.** I verified this personally against the AACO
> release (28,466 B page vs a 15,181 B 404 control; `Payment Orchestration` 13 hits, `CellPoint` 18,
> control 0), bilingual EN/AR and **sourced to Riyadh Air itself**:
>
> > *"The partnership supplies Riyadh Air with CellPoint Digital's **Payment Orchestration platform**,
> > enabling the carrier to process **local and cross-border transactions** efficiently… Riyadh Air chose
> > to partner with CellPoint Digital and **embrace Payment Orchestration from the outset**."* — 12 June 2024
>
> The `/research` skill is explicit that Competitive is the hardest motion and should only proceed on a
> concrete gap. **Three concrete gaps exist** (mada, BNPL, APAC acquiring) and are set out in Section 10.
>
> ⛔ **Two corrections to the research run, both of which would have reached outreach as false:**
> 1. An agent attributed a quote about *"intelligent routing, taking into consideration the pricing,
>    processing and acceptance currency…"* to the AACO release. **`intelligent routing` returns 0 on that
>    page.** It is from a reprint, not the cited source. Do not quote it as sourced there.
> 2. An agent recommended `careers-riyadhair.icims.com` as the richest substitute for the blocked
>    checkout. **It is not.** Every URL on that host returns the same ~28.8 KB client-rendered shell — a
>    nonsense job ID returns **200 at 28,832 B** against the real search page's 28,801 B, with
>    `orchestr` = 0 on all four responses. **The job content is not in the HTML.**

> ## 🎯 THE HOOK — their own app names four card methods. Their national competitor's names mada.
>
> Verified by me through **Apple's iTunes lookup API, keyed to bundleId** — which matters, because the
> rendered Play page produces false positives for mada, STC Pay, Tabby and Tamara that all belong to
> neighbouring apps in the carousel. The structured API cannot do that.
>
> | App | bundleId | Verbatim payment sentence |
> |---|---|---|
> | **Riyadh Air** v1.0.17, 2026-10-02 | `com.riyadhair.digital` | *"Pay securely in local or preferred currency using **Visa, Mastercard, Amex, or Apple Pay**."* |
> | **Saudia** v4.7.1, 2026-09-16 | `com.saudia.iphone` | *"Pay with Visa, Master Card, American Express, **MADA or SADAD**."* |
>
> **Same sentence slot. Same storefront. Same API call. Riyadh Air names four card rails; the national
> flag carrier names mada and SADAD.** Saudi Arabia is **52.36%** of Riyadh Air's traffic, and SAMA's
> mada e-commerce series **excludes Visa/Mastercard credit** — so this is volume a card-only stack does
> not address at all.
>
> ⚠️ **This is marketing copy, not a walked checkout.** mada may be live and simply unlisted, and method
> sets are frequently geo-conditional. **Take it into outreach as a question, never as an assertion.**

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Riyadh Air is Saudi Arabia's second flag carrier, wholly owned by the Public Investment
Fund, announced March 2023 and in scheduled revenue service only since **10 June 2026**. It is the
first full-service airline built natively on an **Offer & Order platform (FLYR)** rather than a legacy
PSS — so there is **no Amadeus Altéa or SabreSonic card vault** anywhere in the stack. As of August 2026
it flew **9 destinations with 8 aircraft** (7 Boeing 787-9 in service), targeting 22 destinations by
March 2027.

**SimilarWeb:** supplied 2026-10-14, Jul–Sep 2026, `riyadhair.com`, **all-country-domains toggle OFF**,
74 countries. No total-visit figure shown.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇸🇦 Saudi Arabia | **52.36%** | Visa, Mastercard, Amex, Apple Pay | **mada**, SADAD, STC Pay, urpay, Tabby, Tamara | ✅ the only one |
| 2 | 🇮🇳 India | **7.56%** | Visa, Mastercard, Amex | **UPI**, RuPay, net banking, EMI | ❌ GSA only (Bird Travels) |
| 3 | 🇵🇰 Pakistan | **6.03%** | Visa, Mastercard, Amex | JazzCash, Easypaisa, 1Link | ❌ cargo agent only |
| 4 | 🇪🇬 Egypt | 5.58% | Visa, Mastercard, Amex | Fawry, Meeza | ❌ cargo GSSA only |
| 5 | 🇬🇧 United Kingdom | 5.20% | Visa, Mastercard, Amex, Apple Pay | PayPal, Klarna | ❌ passenger GSA only |

**All "missing methods" are NOT FOUND, not confirmed-absent** — the checkout could not be walked.

### Legal entities
- **One jurisdiction of incorporation: Saudi Arabia.** Reported as "Aviation Service Company"; the app
  store seller name is **`AVIATION SERVICE COMPANY`**, which independently corroborates the name — but
  **the CR number is unverified and must not go into outreach.**
- **Riyadh Cargo** (announced 21 Jan 2026) is the only subsidiary, and it is domestic.
- **Zero confirmed legal entities outside Saudi Arabia.** Every foreign presence is a GSA or cargo
  GSSA — a sales agent, not an establishment, and **no local acquiring capability.**

### Known payment stack — five vendors in 26 months
- **CellPoint Digital** — payment orchestration, 12 Jun 2024 `[Press Release, verified]`
- **noon Payments** — gateway, Aug 2024 — **a PIF sister company** `[Press Release]`
- **Saudi Awwal Bank** — mandated as an e-commerce **acquirer**; **HSBC** for Middle East **and Asia**
  treasury (virtual accounts, Omni Collect), May 2025 `[Search summary]`
- **Mastercard** — "RX Pay" issuing + B2B travel-trade virtual cards, with a **Saudi exclusivity**, Feb/Jul 2026 `[Search summary]`
- **barq** — "strategic payment technology partner", **"full payment lifecycle"**, 13 Aug 2026 `[Press Release]`

### Orchestration status
**Global orchestrator incumbent — CellPoint Digital**, the airline-vertical specialist. Rests on
**presence**, not absence, so the blocked domain does not weaken it. **No source confirms CellPoint is
still live in October 2026**, and the barq deal is scoped broadly enough to overlap or displace it.

### Buying signals
- 🚀 **12 routes launched Jun–Sep 2026, seven of them APAC** — KL, Mumbai, Dhaka, Islamabad, Lahore, Manila, Bangkok
- 💼 **Five dedicated payment roles** on their own careers portal, one reportedly mandating a move to an **in-house orchestration platform** ⚠️ unverified
- 🤝 **Air India codeshare + interline MoU**, June 2026 — subject to approvals, not live
- 📋 **No public payment RFP or tender found.** The escalation trigger is **not** met.
- 💰 **No 2026 PIF capital injection found** — searched explicitly

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Riyadh Air` to draft the 12-touch sequence.*

⚠️ **Read the three boxes at the top before writing a word.** Four hard constraints:
- **Motion is Competitive.** An orchestrator is already in. **Never open with "you have no orchestration."**
- **Never name CellPoint** (or any Yuno competitor) in outreach-facing text.
- **mada is a question, not an assertion.** The evidence is their own marketing copy, not a walked checkout.
- **Tact:** their hub was attacked on 10 Oct 2026 with fatalities and flights were cancelled. Do not
  lead on refund or chargeback pain in the near term.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 21 / 29 → overridden to 🟢 Medium

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **2** | ⚠️ **See the mandatory disclosure below. The figure is ASSUMPTION-DRIVEN and therefore cannot reject.** |
| Orchestration status | **1** | ✅ **Global orchestrator incumbent** — CellPoint Digital, verified by me from a primary release with a passing control |
| 3+ countries | **3** | ✅ 9 countries above 1% traffic; 12+ countries served by route |
| Multiple PSPs | **3** | ✅ noon Payments (gateway) + Saudi Awwal Bank (acquirer) + HSBC + barq + Mastercard |
| Local rail or licensing gap in a top-3 market | **3** | ⚠️ **mada absent from Riyadh Air's own app copy while Saudia names it in the identical slot** — verified via Apple's structured API. Saudi is 52.36% of traffic. **Marked ⚠️ not ✅: this is marketing copy, not a walked checkout. If mada is confirmed live, this row drops to 0 and the score becomes 18.** |
| Recent expansion | **2** | ✅ 12 routes in four months, seven of them APAC |
| Payment issues | **2** | ⚠️ ~9 genuine payment-failure reports in 226 App Store reviews — Apple Pay + 3DS-OTP failure, charged-but-no-booking, decline-then-reprice. Three categories rated moderate. **Low absolute volume for a 4-month-old airline.** |
| Funding >$10M | **0** | ❌ **No 2026 PIF injection found.** The SAR 3bn/5bn revolving facility is FII 2024 — outside 12 months, and one source says SAR 50bn, a 10× discrepancy left unresolved |
| High traffic outside home | **2** | ✅ Saudi Arabia **52.36%**, below the 60% threshold |
| Competitor using orchestration | **2** | ✅ From our own verified prior research: **Cebu Pacific** runs CellPoint with a published case study; **Vietnam Airlines** signed a direct orchestration competitor 29 May 2026 |
| Payment job postings | **1** | ✅ Five payment-specific reqs on their own portal |

**Tier on arithmetic: ⭐ High Priority (21). → 🟢 Medium after analyst override.**

### 🛑 Analyst override — DOWN from ⭐ to 🟢. Reasoning in full.

**Primary ground: absolute volume is too small, which the override rules name explicitly** —
*"A high percentage score on a company with negligible transaction volume is a false positive."*
Riyadh Air has **7 widebodies in service, 9 destinations, and four months of scheduled revenue
service.** The derived booking range (~31k–42k/month) sits on the gate rather than above it. The matrix
rewards this account for breadth — 9 countries, 5 vendors, 12 routes — but breadth here is a *network
plan*, not transaction volume. **The ⭐ is an artefact of counting markets instead of payments.**

**Secondary ground: a structural procurement barrier, not a technical one.** The gateway, **noon
Payments, is a PIF sister company** — the same shareholder owns both. **Mastercard holds a Saudi
exclusivity** on RX Pay. And the airline is reportedly staffing to build orchestration **in-house**.
Displacing a competitor is normal; displacing a competitor *plus* a shareholder-affiliated vendor *plus*
an internal build programme is a different proposition.

**What the override is NOT based on:** the territory question (that is Prateek's exception to make, not
mine to re-litigate) and not the quality of the intelligence, which is high.

**Recommendation: revisit in ~12 months.** 9 → 22 destinations by March 2027 and 8 → 130+ aircraft by
2030 means the volume objection is temporary. **This is a timing call, not a disqualification.**

### Monthly transaction count — MANDATORY DISCLOSURE

⚠️ **NOT FOUND — ASSUMPTION-DRIVEN DERIVATION, ~31,000–42,000 ticket bookings/month.**
**[Neither input that does the real work is sourced.]**

- **Sourced inputs:** 7 in-service 787-9s; **290 seats** (F4/J24/W39/Y223); the published route and
  frequency map (4× daily Jeddah, daily LHR/Cairo/Mumbai/Dhaka/Islamabad, 3× weekly Lahore, 7× weekly
  Bangkok from Oct, plus Dubai/Madrid/Manchester/Málaga/Manila/KL).
- **Derived:** ~14–18 departures/day, constrained by the 7 widebodies.
- **ASSUMED, and doing all the work:** an **80% load factor** and **~1.5–1.6 passengers per booking**
  across ~2 journeys per return. **Neither is sourced.** No passenger count, load factor, ASK, RPK or
  average fare is published anywhere — PIF-owned, unlisted, no disclosure obligation.

**Per the disclosure rule, an assumed figure NEVER rejects an account, and this one does not.** It is
scored at the lowest non-reject band (**2**) rather than being allowed to either disqualify the account
or inflate it. **Billing unit counted: ticket bookings.** Ancillaries (seats, bags, upgrades) are
separately-priced order items on an Offer & Order stack and are *additional* payment events — plausibly
lifting total payment events above the ticket count, but that is `[INFERENCE, not confirmed]`.

**→ "Confirm monthly transaction count" is the #1 manual action.**

### Source Notes
- ✅ **CellPoint orchestration** — primary release, verified by me, passing control, sourced to Riyadh Air
- ✅ **App-store payment methods** — Apple's structured lookup API, bundleId-keyed, with a peer control
- ✅ **Routes to India, Pakistan, Bangladesh, Egypt and the UK are LIVE**, not aspirational — Mumbai daily from 4 Aug, Dhaka daily from 7 Aug, Islamabad from 14 Aug, Lahore 3× weekly from 16 Aug
- ✅ **Seller name `AVIATION SERVICE COMPANY`** corroborates the entity name independently
- ⚠️ **CR number unverified** — the LEI candidate is an inference; keep it out of outreach
- ⚠️ **In-house orchestration mandate unverified** — job pages return 410 Gone and the iCIMS host serves a content-free shell
- ⚠️ **Checkout never walked** — `riyadhair.com` 403s on every path behind Akamai
- ⚠️ **Launch date contested** — 26 Oct 2025 (invitation-only) vs **10 Jun 2026** (scheduled service) vs 1 Jul 2026 (public sales). Wikipedia is self-contradictory.

### Success Case Alternatives
- **An airline running multi-market acquiring off a single home entity** — the profile match is exact.
- ⚠️ **Do not reuse the Cebu Pacific comparison in outreach** — Cebu runs the same incumbent.

---

## Section 1: Website Traffic Analysis by Country

**Data source: supplied SimilarWeb screenshot (path 1).** Full record in `accounts/traffic/riyadh-air.md`.

| Rank | Country | Share | Trend | Notes |
|---|---|---|---|---|
| 1 | 🇸🇦 Saudi Arabia | **52.36%** | ▲ 34.24% | **high priority** · country rank **#343** |
| 2 | 🇮🇳 India | **7.56%** | ▼ 39.30% | **high priority** · weakest depth in the set — 2.27 pages/visit |
| 3 | 🇵🇰 Pakistan | **6.03%** | ▼ 24.33% | **high priority** · country rank **#3,192**, far above its share |
| 4 | 🇪🇬 Egypt | 5.58% | ▼ 40.22% | **high priority** · 64.20% bounce, worst in the set |
| 5 | 🇬🇧 United Kingdom | 5.20% | ▼ 0.25% | **high priority** |
| 6 | 🇦🇪 UAE | 3.81% | ▼ 21.15% | rank #2,871 |
| 7 | 🇺🇸 United States | 1.77% | ▼ 31.11% | **not a served route** |
| 8 | 🇧🇩 Bangladesh | 1.14% | ▲ 16.10% | **longest sessions in the dataset — 06:36**, 27.39% bounce |
| 9 | 🇪🇸 Spain | 1.10% | ▲ 17.75% | |

**Visible APAC territory: 14.73%** (India + Pakistan + Bangladesh).

**The declines are explainable and should not be hidden.** India ▼39.30%, Egypt ▼40.22%, Pakistan
▼24.33% fall in a Jul–Sep window that contains the **pre-launch booking surge** for routes that opened
in August. A post-launch drop-off is consistent with that, not contradictory — `[INFERENCE, not confirmed]`.

**The traffic map matches the route map almost exactly**, which is the strongest validation available
that this demand is real: every one of India, Pakistan, Egypt, UK and Bangladesh is a **live served route**.

## Section 2: Legal Entities & Local Presence

**Headquarters:** Riyadh, Saudi Arabia. Announced 12 March 2023 by the Crown Prince; PIF-owned,
chaired by PIF Governor Yasir Al-Rumayyan; CEO **Tony Douglas** (ex-Etihad); **CFO Adam Boukadida**,
who owns payments publicly. IATA **RX**, ICAO **RXI**, callsign RIYADH. GACA approval to commence
operations 6 April 2025.

| Country | Entity | Reg # | Note |
|---|---|---|---|
| 🇸🇦 Saudi Arabia | "Aviation Service Company" (app-store seller: `AVIATION SERVICE COMPANY`) | **unverified** | The only jurisdiction of incorporation |
| 🇸🇦 Saudi Arabia | Riyadh Cargo | — | Only subsidiary, announced 21 Jan 2026 |

**Cross-Border Gap Analysis**

| Country | Top 10 traffic? | Local entity? | Agent only | Cross-border risk |
|---|---|---|---|---|
| 🇮🇳 India | ✅ 7.56% | ❌ **none** | Bird Travels (passenger), Air Logistics (cargo) | **HIGH** |
| 🇵🇰 Pakistan | ✅ 6.03% | ❌ **none** | Crest Cargo | **HIGH** |
| 🇪🇬 Egypt | ✅ 5.58% | ❌ **none** | M&C Aviation (cargo) | **HIGH** |
| 🇬🇧 UK | ✅ 5.20% | ❌ **none** | FlyUs Aviation (passenger GSA) | **HIGH** |
| 🇧🇩 Bangladesh | ✅ 1.14% | ❌ **none** | Envotech (cargo) | **HIGH** |

> **Warning: cross-border operation across every market except Saudi Arabia.** All card revenue from
> India, Pakistan, Egypt, the UK and Bangladesh almost certainly settles to a single Saudi entity, with
> the usual consequences — higher scheme costs, lower issuer approval and FX exposure.
> `[INFERENCE, not confirmed]`

> ⚠️ **Deliberately NOT asserted: whether India, Egypt or Bangladesh legally gate domestic acquiring
> behind local establishment.** Both agents were asked and both declined to source it; I will not state
> a regulatory rule from background knowledge. **This is the single highest-value thing to resolve**,
> because if it holds, ~14% of demand is structurally stuck on cross-border acquiring.

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Market | Provider | Role | Evidence | Source |
|---|---|---|---|---|
| Saudi + cross-border | **CellPoint Digital** | **Payment orchestration** | `[Press Release]` **verified by me, passing control** | aaco.org, 12 Jun 2024 |
| Saudi | **noon Payments** | Gateway — card acceptance + APMs. **PIF sister company** | `[Press Release]` | futuretravelexperience, Aug 2024 |
| Saudi | **Saudi Awwal Bank** | **"mandated as one of the acquirers for e-commerce transactions"** | `[Search summary]` | arabnews / zawya, May 2025 |
| **MEA + Asia** | **HSBC** | Treasury — virtual accounts, Omni Collect, sweeping (**not** card acquiring) | `[Search summary]` | enterpriseam, May 2025 |
| Saudi | **Mastercard** | **RX Pay** issuing + B2B travel-trade virtual cards, **Saudi exclusivity** | `[Search summary]` | futuretravelexperience / gulfbusiness, 2026 |
| Saudi | **barq** | "Strategic payment technology partner", **"full payment lifecycle"** | `[Press Release]` | aaco.org, 13 Aug 2026 |

**Explicitly NOT found, with searches run:** HyperPay, PayTabs, Moyasar, Tap Payments, Geidea, Clickpay,
Telr, STC Pay, urpay, Amazon Payment Services, Adyen, Stripe, Checkout.com, Worldpay, Braintree,
Cybersource, Global Payments, UATP.

**The commercial platform — and why it matters.** Riyadh Air runs **FLYR's Offer & Order Management
System**, not a PSS. FLYR's own site: *"Riyadh Air will leverage FLYR's complete Offer & Order
Management System"* and the OOMS *"empowers airlines to move beyond legacy Passenger Service Systems."*
**Sabre supplies revenue management and retailing only** — a grep of Sabre's own release returned
**SabreSonic = 0, PSS = 0, Altéa = 0, reservation = 0, vault = 0**. **Amadeus is GDS distribution only**
(Aug 2025). IBM Consulting is the integrator.

> **Consequence: there is no legacy PSS card vault to work around.** The usual airline blocker —
> *"payments are locked inside Altéa"* — does not apply. Payments here are an API integration against
> ONE Order orders. That makes the technical sale easier than at Qantas (vault inside Amadeus) or Korean
> Air (direct-to-VAN).

⚠️ **One contradiction left unresolved:** trade press frames FLYR as replacing the PSS, while FLYR's own
product copy elsewhere describes layering on *"your PSS."* Assert only what the evidence supports: **no
Altéa or SabreSonic deal is on public record and the payment layer is contracted separately.**

### 3B. Payment Orchestrator

**Classification: Global orchestrator incumbent — CellPoint Digital.** Based on **presence**: a signed,
press-released, named contract sourced to Riyadh Air itself. No inference required.

> *"Confirmed orchestration-aware. The opening is coverage and international reach, not the case for
> orchestration itself."*

**Three unresolved complications, all commercially material:**
1. **Live status unknown.** Every CellPoint citation traces to the single June 2024 announcement. **No
   source confirms deployment, and none confirms it is still live in Oct 2026.**
2. **barq may overlap or displace it.** The Aug 2026 deal is scoped as "full payment lifecycle" and
   "improving transaction success rates" — orchestration-adjacent language. No source says whether it
   replaces or supplements.
3. **A reported in-house migration.** Job reqs reportedly mandate moving *"from third party systems to a
   scalable in house orchestration platform"*, naming routing intelligence, tokenization and multi-PSP
   architecture. ⚠️ **UNVERIFIED — I could not open any job page**, and the careers host serves a
   content-free shell.

**No evidence of Spreedly, Primer, Gr4vy, APEXX, Payrails, Juspay or Yuno.** That is an absence finding
and, with the domain unreachable, a weak one.

## Section 4: Alternative & Local Payment Methods

| Market | Method | Category | Status | Source |
|---|---|---|---|---|
| Global | Visa, Mastercard, Amex | Cards | **Active (app copy)** | Apple iTunes API, `com.riyadhair.digital` |
| Global | Apple Pay | Wallet | **Active (iOS app)** | same; web availability unresolved |
| Global | Google Pay | Wallet | **Not found** | absent from Android listing |
| Global | PayPal, UATP, IATA Pay | — | **Not found** | — |
| 🇸🇦 Saudi | **mada** | Domestic debit | **NOT FOUND** | absent from app copy; Saudia names it in the same slot |
| 🇸🇦 Saudi | SADAD, STC Pay, urpay | A2A / wallet | **Not found** | — |
| 🇸🇦 Saudi | Tabby, Tamara | BNPL | **Not found (direct)** | only via reseller Alternative Airlines |
| 🇮🇳 India | **UPI**, RuPay, net banking, EMI | A2A / cards / instalments | **Not found** | — |
| 🇵🇰 Pakistan | JazzCash, Easypaisa, 1Link | Wallet | **Not found** | — |
| 🇧🇩 Bangladesh | bKash, Nagad, Rocket | Wallet | **Not found** | — |
| 🇪🇬 Egypt | Fawry, Meeza | Cash / cards | **Not found** | no dedicated search run — weak |
| 🇬🇧 UK | Klarna, PayPal | BNPL | **Not found** | — |
| 🇪🇸 Spain | Bizum | A2A | **Not found** | — |

> **Warning — Saudi Arabia (52.36%):** mada is the dominant domestic scheme. SAMA data via Arab News:
> mada e-commerce reached **873.7m transactions worth SAR 156.9bn in 2023, +28% YoY**, and **the series
> excludes Visa/Mastercard credit** — so it is volume a card-only stack cannot reach.
> `[UNVERIFIED — search summary only]`

> **Warning — India (7.56%):** UPI ran **24,162 crore transactions in FY2025-26**, reported at ~84% of
> India's digital payments. `[UNVERIFIED — search summary only]`

⚠️ **Pakistan rail prominence is NOT sourced to a standard worth defending** — the only figures found are
from a payments vendor's market guide, not the State Bank. **Do not quote a Pakistan wallet share.**

**Multi-currency: CONFIRMED generically** — their own app copy says *"Pay securely in local or preferred
currency."* **Per-market currency sets are unresolved.**

⚠️ **The most likely reason a real local-method stack could be invisible here: geo-conditional rendering.**
App-store copy is one global string. mada may render only on a Saudi IP and UPI only on an Indian IP.
**A single Saudi-IP and India-IP render of the payment step would resolve most of Section 4.**

## Section 5: Payment Issues & Customer Complaints

Evidence base: **226 de-duplicated Apple App Store reviews**, SA/US/GB/IN/AE storefronts, 18 May –
10 Oct 2026. Aggregate **4.67 from 6,461 ratings**, so the 1★ cohort is a vocal minority. **46 mentioned
a payment keyword; ~9 are genuine payment failures.** Trustpilot is **2.0/5 from only 14 reviews** —
too few to call a pattern.

| Issue | Platform | Frequency | Date | Source |
|---|---|---|---|---|
| **Apple Pay fails, bank 3DS/OTP never arrives** | App Store (SA) | Isolated, high severity | 2026-08-09 | apps.apple.com/sa/app/riyadh-air/id6757419085 |
| **Charged but booking not created** | App Store (US) | Isolated | 2026-09-21 | same |
| **Money debited despite failure message, booking invisible** (AR) | App Store (SA) | Isolated | 2026-08-03 | same |
| **Decline-then-retry reprices the fare upward** | App Store (SA) | Isolated | 2026-09-29 | same |
| **In-app checkout too broken, forced to desktop** | App Store (GB) | **Moderate** | 2026-09-28 | same |
| **Generic payment friction / "payment needs maintenance"** | App Store (GB, SA) | **Moderate** | Jul–Aug 2026 | same |
| **Bookings cancelled after successful payment** | App Store (SA) | **Moderate** | Oct 2026 | same |

> **Pattern: the decline-then-reprice report is the most commercially interesting.** A customer whose
> first card declines and who retries on a second card sees the fare jump — *"the price automatically
> increases by a big amount."* On an Offer & Order stack where the offer is repriced on re-entry, a
> **failed authorisation becomes a repriced offer**, not just a retry. That is an orchestration problem
> with a revenue number attached, and it is in their own customers' words.

**Honest counter-evidence:** Apple Pay was praised at launch — *"You can even use Apple Pay!"* (5★, GB,
20 May 2026) — so the August failure reads as a **regression**, not an absence. And multiple 5★ reviews
praise booking ease. **The predicted "slow refunds" pattern is NOT evidenced** — the disputes are about
refund *amount* and eligibility, not timeliness.

**Not obtained:** Google Play listing (package ID never resolved; 404s byte-identical to control),
Reddit (zero results), Skytrax (no profile found), X/Twitter (not searched).

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | **Jun–Sep 2026** | **12 routes launched, seven APAC** — LHR, Jeddah, Dubai, Cairo, Madrid, Manchester, **KL, Mumbai, Dhaka, Islamabad, Lahore, Manila** | Market Expansion | travelextra, insideflyer, aviationweek |
| 2 | **13 Aug 2026** | **barq** strategic payment partnership, "full payment lifecycle" | Payment Infrastructure | aaco.org |
| 3 | **Feb/Jul 2026** | **Mastercard** alliance → **RX Pay**, Saudi exclusivity, B2B travel-trade virtual cards | Payment Infrastructure | thefintechtimes, gulfbusiness |
| 4 | **Jun 2026** | **Air India** codeshare + interline **MoU** — subject to approvals, **not live** | M&A / Partnership | airwaysmag |
| 5 | **2025–2026** | **Five payment job reqs** incl. one reportedly mandating in-house orchestration ⚠️ unverified | Payment Hiring | careers-riyadhair.icims.com |

**No public payment-related RFP found.** Searched explicitly. The escalation trigger is **not** met.
Note they *do* procure formally — ground handling went to Saudi Ground Services *"through a competitive
bidding process"* at ~USD 400m — so a payment tender is plausible later, but none is published.

**No 2026 PIF capital injection found.** The SAR 3bn (+2bn option) Islamic revolving facility dates to
FII 2024, and one source reports **SAR 50bn** — a 10× discrepancy **left unresolved. Do not cite a figure.**

## Section 7: Payment-Specific News

Covered in Section 6 — the vendor announcements *are* the payment news. **No provider removal has been
announced.** The inference that barq may be displacing CellPoint rests on two verified sources plus an
unverified job ad and **must not be stated as fact.**

**Material event, 10 Oct 2026:** Riyadh Air's hub, King Khalid International Airport, was attacked with
at least 12 reported deaths; flights including London and Madrid were cancelled and the fleet reportedly
grounded. A change-fee waiver was offered for travel through 24 Oct. **Single outlet, not independently
confirmed.** Relevant because it will drive refund and chargeback volume — **and because leading on
refund pain right now would be tone-deaf.**

## Section 8: Checkout Experience Audit

**Not accessible in this environment.** `riyadhair.com` sits behind Akamai and returns **HTTP 403 on
every path** — `/`, `/en`, `/robots.txt`, `/sitemap.xml` — with a nonsense-path control 403ing
identically at near-identical byte size, so these are blocks and not findings. `book.` and `api.`
subdomains fail at the egress proxy (CONNECT 502).

| Dimension | Finding |
|---|---|
| Payment methods visible | **Visa, Mastercard, Amex, Apple Pay** — from app-store copy only, not a walked checkout |
| Multi-currency | *"local or preferred currency"* — confirmed generically, per-market set unknown |
| Mobile UX | **Negatively evidenced** — *"The app is very glitchy when making payments. I had to use the desktop site."* |
| Everything else | **Not determinable.** 3DS, tokenization, guest checkout, saved methods, geo-adaptation, error clarity all unresolved |

## Section 9: PCI DSS Compliance

**No published PCI DSS level, AoC or attestation found.** No vendor release mentions PCI, tokenization
or 3DS — confirmed absent from the CellPoint, noon and barq releases. The only PCI references are job
ads (unverified) requiring **PCI DSS compliance** and naming **tokenization**.

> `[INFERENCE, not confirmed]`: with a gateway (noon) and an orchestrator (CellPoint) in the flow, PCI
> scope is likely reduced with card data handled by those vendors. **No source states this.**

**3DS: no public information found** — though the Apple Pay/OTP complaint implies a bank OTP step exists.

## Section 10: Strategic Insights & Outreach Angles

> ### Insight #1 — Their own app names four card rails. The national carrier's names mada.
> **Evidence:** S4 (mada NOT FOUND in Riyadh Air's app copy; Saudia names MADA and SADAD in the identical
> sentence slot, both via Apple's bundleId-keyed API) + S1 (Saudi Arabia **52.36%** of traffic).
> **Pain:** mada e-commerce ran **873.7m transactions / SAR 156.9bn in 2023**, and SAMA's series excludes
> Visa/MC credit. A card-only checkout cannot reach that volume in the market that is over half the business.
> **Yuno value:** one integration to add a domestic scheme without a per-rail rebuild.
> **Outreach angle:** ask rather than assert — their app lists four card rails where the flag carrier
> lists mada and SADAD, and ask whether mada renders on a Saudi IP.
> **Subject:** `mada on your Saudi checkout`

> ### Insight #2 — Five markets live, one entity, zero local acquiring.
> **Evidence:** S2 (zero legal entities outside Saudi Arabia; every foreign presence is a GSA or cargo
> GSSA) + S1/S6 (live daily routes to Mumbai, Dhaka, Islamabad, Cairo, London — India 7.56%, Pakistan
> 6.03%, Egypt 5.58%, UK 5.20%).
> **Pain:** every card from those markets is acquired cross-border into a Saudi entity — higher scheme
> cost, lower issuer approval, FX on top. A GSA sells tickets; it does not give you local acquiring.
> **Yuno value:** routing to local acquirers per geography without a local entity per market.
> **Outreach angle:** twelve routes in four months, seven of them in Asia, against one jurisdiction of
> incorporation.
> **Subject:** `Seven Asia routes, one acquiring entity`

> ### Insight #3 — A declined card doesn't just retry on an Offer & Order stack. It reprices.
> **Evidence:** S5 (customer: *"if you make a payment with the wrong card and it gets declined and then
> use another card, the price automatically increases by a big amount"*) + S3 (FLYR Offer & Order, no
> legacy PSS, offers repriced on re-entry).
> **Pain:** a failed authorisation becomes a repriced offer, so the cost of a decline is not a retry —
> it is an abandoned booking or a customer-service credit. **This is in their own customers' words.**
> **Yuno value:** retry and failover inside the routing layer, before the offer is rebuilt.
> **Outreach angle:** quote the review pattern back, framed as a question about re-entry pricing.
> **Subject:** `Second card, higher fare`

> ### Insight #4 — A competitor sells BNPL on Saudi fares. They don't.
> **Evidence:** S4 (Tabby/Tamara NOT FOUND for Riyadh Air direct) + S11 (flynas partnered with Tamara
> for instalments; resellers offer Tabby/Tamara on Riyadh Air fares — capturing that demand off-platform).
> **Pain:** long-haul fares are a core BNPL category in the Gulf; an OTA is monetising a rail the airline
> doesn't offer, on the airline's own inventory.
> **Yuno value:** BNPL as one more method through the same integration.
> **Subject:** `BNPL on your fares — but not on your checkout`

### Quick Hits

**Email hooks:**
1. Your app lists Visa, Mastercard, Amex and Apple Pay — Saudia's lists MADA and SADAD in the same sentence, and Saudi is half your traffic.
2. Twelve routes in four months, seven of them in Asia, and one jurisdiction of incorporation.
3. Your reviewers say a declined card comes back at a higher fare — on an Offer & Order stack that's a repriced offer, not a retry.

**Cold call openers:**
1. "You've launched Mumbai, Dhaka, Islamabad, Lahore and Manila since August — who's acquiring those cards today?"
2. "Does mada render on your checkout on a Saudi IP? It isn't in your app's method list and it is in Saudia's."
3. "Your CFO said publicly you're in a position to implement many payment solutions at once — I wanted to test that against the Asia routes."

## Section 11: Similar Companies & Prospecting Pipeline

### 11A/B. Peers — from this repository's own verified research

| Company | Motion | Orchestrator status | In TAL? |
|---|---|---|---|
| **Cebu Pacific** | Competitive | **CellPoint Digital, published case study** | ✅ 11/29 |
| **Vietnam Airlines** | Competitive | **Direct competitor signed 29 May 2026, mid-rollout** | ✅ 18/24 |
| Qantas | In-house | **Card vault inside Amadeus** | ✅ 19/29 |
| Korean Air | In-house | Direct-to-VAN, gateway-per-region, no orchestrator | ✅ 17/29 |
| Garuda Indonesia | In-house | Own layer since 2013 | ✅ 16/24 |
| Jetstar | In-house (partial) | Payment service on Navitaire | ✅ 18/29 |
| Lion Air · Bangkok Airways · China Airlines | Greenfield | None detected | ✅ |
| **Saudia** | not researched | — | ❌ **not on TAL** — EMEA territory |
| **flynas** | not researched | **Tamara BNPL confirmed** | ❌ **not on TAL** — EMEA territory |

⚠️ **Scores marked /24 are from the older matrix and are NOT comparable to /29.** Do not rank across them.

### 11C. Competitors adopting orchestration
**Confirmed: Cebu Pacific (CellPoint Digital, published case study) and Vietnam Airlines (29 May 2026).**
Both from our own prior verified research. **This fires the +2 ICP row on first-party evidence.**

### Top prospect find
**flynas and Saudia are genuine finds that are NOT on the TAL** — but both are Saudi, so both are EMEA
territory under the same rule that puts Riyadh Air out of scope. **Route to EMEA rather than adding them here.**

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|---|---|---|
| Annual revenue | **No public information found** | PIF-owned, unlisted, no disclosure obligation |
| GMV / GTV | **No public information found** | — |
| Average transaction value | **No public information found** | no published fare data |
| **Monthly transaction count** | ⚠️ **ASSUMPTION-DRIVEN: ~31,000–42,000 ticket bookings/month** | See the mandatory disclosure in the ICP breakdown. Load factor and pax-per-booking are **both assumed**. **Billing unit: ticket bookings.** |
| Fleet | **8 aircraft; 7 Boeing 787-9 in service**, 290 seats (F4/J24/W39/Y223) | Wikipedia, 9 Oct 2026 |
| Destinations | **9** as of 5 Aug 2026 → target **22 by Mar 2027**, 100+ by 2030 | travelextra |
| Passengers carried | **No public information found** | target of 5–8m/yr is a projection, not an outcome |
| Primary currency | SAR; multi-currency confirmed generically, per-market set unknown | app copy |
| Top 3 markets by traffic | Saudi Arabia, India, Pakistan | SimilarWeb supplied |
| Billing channel split | **N/A** — airline ticketing, not app-store billing | — |

## Overall Research Confidence

**MEDIUM — downgraded one level from High, and the cause is environmental.** `riyadhair.com` is
Akamai-blocked on every path, so `[Checkout]` and `[Source Code]` evidence does not exist in this
report. Section 8 could not be completed.

**Traffic data was SUPPLIED** (SimilarWeb screenshot), which is the strongest of the three paths — so
the country profile and the two traffic-dependent ICP rows are solid.

- **Strong:** orchestrator classification (primary release, control-tested by me), the commercial
  platform stack (FLYR/Sabre/Amadeus, grep-verified), live route map, app-store method list (structured
  API with a peer control), competitor orchestration (our own prior research).
- **Weak:** CR number, in-house migration claim, all per-market rail absences, Pakistan rail prominence,
  the credit-facility figure, PCI and 3DS.
- **Absent:** checkout behaviour, geo-conditional method rendering, per-market currencies, actual volume.

## Manual Research Recommendations

> **Area: Monthly transaction count.** **Why:** the only signal that can reject an account, and it is
> currently assumption-driven and straddling the gate. **Action:** ch-aviation, GACA monthly statistics,
> or OAG/Cirium schedule data for a sourced seat or passenger count.

> **Area: mada on the live checkout.** **Why:** it is Insight #1 and the whole Saudi argument.
> **Action:** load the payment step on a **Saudi IP**. One render settles it.

> **Area: geo-conditional method rendering.** **Why:** if methods are geo-gated, most of Section 4's
> NOT FOUNDs are wrong. **Action:** render the payment step on Saudi and Indian IPs and compare.

> **Area: Is CellPoint still live, and does barq replace it?** **Why:** it decides whether this is a
> displacement or a co-existence conversation. **Action:** CellPoint's 2026 newsroom; ask directly on a call.

> **Area: Does India/Egypt/Bangladesh gate domestic acquiring behind local establishment?**
> **Why:** if yes, ~14% of demand is structurally stuck cross-border — that is Insight #2's business case.
> **Action:** source the current rule per market; **do not assert it until then.**

</details>
