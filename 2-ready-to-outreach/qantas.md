# Qantas Airways Limited

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 19 / 29 → ⭐ **High**
**Industry:** Aviation — full-service and low-cost airlines, freight, loyalty · **HQ:** Qantas Airways Limited, ABN 16 009 661 901, 10 Bourke Road, Mascot NSW 2020, Australia (ASX: QAN) · **Researched:** 2026-10-06 · **First email sent:** —
**Motion:** 🛑 **IN-HOUSE / PSS-EMBEDDED — the card vault sits inside Amadeus.** Verified first-hand (see below). **Never say they need orchestration.** Anchor on concentration risk and reach.

---

> ## ⭐ THE FINDING — Qantas publishes, in its own words, that its card vault lives at Amadeus
>
> I pulled `https://www.qantas.com/en-au/book/flights/payment-options/cards` myself (HTTP 200, 15,071 bytes, control: 27 `payment` hits). The string `Amadeus` appears at byte offsets **14165** and **14271**. Verbatim, under the heading **Security**:
>
> > "If you elect to store your card information for future use against your Frequent Flyer membership number (either during the booking process or by selecting the 'Payment Cards' option in your profile), these details are encrypted through HTTPS protocol and then sent from qantas.com to **Amadeus, Qantas' external booking engine service provider**. Your credit card information will be stored on **Amadeus' secure platform** in accordance with our Privacy policy."
>
> **This is the single most useful fact on the account.** It establishes, from Qantas' own published terms, that:
> 1. Stored-credential custody is **not** Qantas-side — it is in the PSS.
> 2. Payments are **not** architecturally separate from the booking engine. They run through it.
> 3. There is no merchant-controlled routing or vaulting tier between qantas.com and Amadeus.
>
> Qantas has been on the full **Amadeus Altéa** suite since 2008 — it was the first airline to complete migration across sales, reservations, inventory and departure control.
>
> ⚠️ **What this does NOT establish, and I will not claim:** the acquirer set. **No PSP or acquirer for Qantas or Jetstar is publicly disclosed anywhere.** Zero hits for Adyen, Cybersource, Worldpay, Braintree, Checkout.com, Stripe, CellPoint, Spreedly, Primer or Gr4vy across every qantas.com page pulled. Amadeus' payments arm **Outpayce** is the *plausible* rail given Amadeus holds the vault — but there is **no evidence of a named Qantas–Outpayce relationship**, and I am not asserting one. Nor is Qantas on **Amadeus Nevio** (confirmed Nevio customers are British Airways, Air France-KLM and Saudia — not Qantas). Treat the acquirer as a discovery question, not a research failure.

---

> ## 🎯 THE HOOK — single-provider concentration, in the exact layer that holds the cards
>
> On **28 June 2017**, an outage on the Amadeus platform took Qantas booking services down, alongside multiple airlines worldwide. Attributed to a hardware issue, explicitly unrelated to the ransomware wave that week.
>
> That is a **dated, concrete instance of single-provider failure in the same layer that custodies Qantas' stored cards.** This is not a hypothetical about resilience — it already happened, to them, in the component they still depend on. It is the cleanest version of the failover-and-redundancy argument available on any account in this batch, and it lands on their own history rather than on an assertion.
>
> Pair it with the second hook, which is narrower and impossible to argue with:
>
> **Google Pay is absent while Apple Pay is live.** Verified: zero `google pay` hits on the payment-options pages; Apple Pay is documented as available on AU departures. Qantas web traffic is **63.82% mobile**, in a market where Android holds the larger mobile share. One wallet is on the checkout and the other is not.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Australia's flag carrier and largest airline group — Qantas mainline (domestic and international), QantasLink, Jetstar (AU/NZ), freight, and Qantas Loyalty. FY26 revenue **A$25,516M** (+7.1%), statutory profit after tax **A$1,289M**, **55.9M passengers** carried, 372 aircraft. Qantas Loyalty alone has **18.9M members** and generated **A$625M underlying EBIT** at a 21.7% margin.

**SimilarWeb total visits:** **14.87M** (Aug 2026), Australia 81.26% — **supplied by Prateek**, Similarweb PRO. Full table in `accounts/traffic/qantas.md`.

### Transaction volume — DERIVED, and I am showing the arithmetic
| Input | Value | Status |
|---|---|---|
| FY26 Group passengers | 55,945,000 | **SOURCED** — AR2026 operating statistics |
| ÷ 12 | ~4.66M passengers/month | DERIVED |
| Bookings < passengers (multi-pax PNRs, return itineraries = one payment) | **~2.5–3.5M card transactions/month** | **DERIVED — Qantas publishes no booking or transaction count** |

Plus ancillaries (seats, bags, Wi-Fi), Hotels/Holidays/TripADeal, and Qantas Marketplace (**A$141M** redemption revenue, up from A$103M). **The volume gate is not in play** — this clears 40,000/month by roughly two orders of magnitude.

### Cross-border — Qantas' own point-of-sale accounting
AR2026 Note 4A splits net passenger and freight revenue **by point of sale**:

| | FY26 | Share |
|---|---|---|
| Australia | A$17,472M | 75.2% |
| **Overseas** | **A$5,756M** | **24.8%** |

**24.8% of ticket revenue is sold outside Australia — and Qantas tracks this itself.** Note this materially exceeds the 18.74% non-Australia share of *web traffic*, which is consistent with higher revenue per visit on international/premium mix.

⚠️ **And they have just removed their two APAC operating entities.** Jetstar Asia ceased operations **31 July 2025** and the Singapore entity is being liquidated; the 33% Jetstar Japan stake is being divested to JAL (binding agreement 4 August 2026, completion expected by June 2027). So that A$5.76bn of offshore selling is increasingly done **from an Australian base**, not from in-market entities.

### Payment methods — verified first-hand from qantas.com
| Method | Markets | Status |
|---|---|---|
| Visa, Mastercard | All | ✅ |
| American Express | All **except Papua New Guinea** | ✅ |
| **UATP** | All except PNG | ✅ airline-industry rail |
| **JCB** | AU, China incl. HK SAR & Taiwan, Japan, Korea, NZ, Singapore, UK | ✅ |
| Apple Pay | **AU departures only** | ✅ |
| **PayID** | **AU only**, AUD only, redirect-out to online banking, 10-min window | ✅ |
| BPAY | AU only, fee-free | ✅ |
| PayPal | AU, NZ, UK, US | ✅ |
| **Zip** (BNPL) | **AU only** | ✅ only instalment rail found |
| **Alipay** | **mainland China departures, Chinese-language site only** | ✅ fee-free |
| Flight Credits | — | ✅ whole or partial |
| Book Now, Pay Later | AU, CA, FR, JP, NZ, SG, UK, US | ✅ hold-and-settle, **not** an instalment product |

**Verified ABSENT (zero hits):** **Google Pay**, **PayTo**, Afterpay, Klarna, Humm, Latitude, **UnionPay**, **WeChat Pay**, IATA Pay.

⚠️ **False positive caught:** a `poli` match was the substring inside **"policy"**. POLi is **not** offered. Re-grepped to confirm.

⚠️ **PayID is not PayTo.** PayID is an addressed *push* credit transfer the customer initiates; PayTo is a *mandated pull* rail. Conflating them in an email would get Prateek corrected on the call.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

> **Not yet generated.** Run `/full-outreach Qantas` to compose the 12-touch sequence into this section.
>
> **Motion is IN-HOUSE / PSS-embedded.** Per `/full-outreach` Step 6a, the sequence must **respect the build decision** and anchor on opportunity cost and reach — never on "you need orchestration." Qantas did not fail to build a routing layer; they deliberately run payments inside the PSS that runs their airline.
>
> **ANZ is the one sub-region where cost-of-acceptance and failover framing lands most directly** (per `.claude/reference/apac-payments.md` — ANZ stacks look most like EMEA/US). Use it.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

## Section 1: Company & Entities

**Parent:** Qantas Airways Limited, ASX: QAN, ABN 16 009 661 901 / ACN 009 661 901. Registered office 10 Bourke Road, Mascot NSW 2020. For-profit company limited by shares, incorporated in Australia (AR2026 Note 1).

**Entities that transact separately:**
- **Jetstar Airways Pty Limited** (AU/NZ) — separate brand, separate booking flow, separate checkout. Plus Jetstar Group Pty Limited, Jetstar Services Pty Limited.
- **Jetstar Asia Airways Pte. Ltd.** (Singapore) — **being wound down and liquidated.**
- **Jetstar Japan Co. Ltd.** — 33.32% equity-accounted associate, never consolidated, **being divested to Japan Airlines.**
- **Qantas Frequent Flyer Operations Pty Limited** — the loyalty operating entity.
- **QantasLink Pty Ltd** — newly incorporated **11 December 2025.**
- **Trip A Deal Pty Ltd / Trip A Deal Holdings Pty Ltd / TAD Holdco Pty Ltd.**
- Holding vehicles of note: **Qantas Singapore Holdings Pty Ltd**, **Qantas Asia Investment Company Pty Ltd.**

**APAC/Pacific associates (AR2026 Note 15):** Fiji Resorts Pte Ltd 21% · Hallmark Aviation Services L.P. 49% · HT&T Travel Philippines Inc. 28% · Holiday Tours and Travel (Thailand) Ltd 37% · Holiday Tours and Travel (GSA) Ltd 37% · PT Holiday Tours & Travel (Indonesia) 37% · Jetstar Japan 33%.

⚠️ **Per-market legal entity list — NOT VERIFIED.** The subsidiary schedule obtained is the Deed of Cross Guarantee list, which is **Australian-incorporated entities only**. The qantas.com subsidiary-companies page returned HTTP 503. Qantas historically runs overseas markets as **branches of Qantas Airways Limited rather than local subsidiaries** — the normal IATA-carrier structure — but that is `[INFERENCE, not confirmed]`. **Whether Qantas settles locally (local acquiring, local currency) in the US, NZ, UK, Japan, Singapore, HK or India is not publicly disclosed.** This is a genuine discovery question, and a good one: point-of-sale currency ≠ settlement currency, and Qantas does not say which it does.

⚠️ **"Qantas Money" is a brand, not an entity** in the AR2026 schedule. **NAB (National Australia Bank Limited) is the credit provider and issuer** of Qantas Premier cards on behalf of Qantas Airways Limited, having acquired the book from Citigroup Pty Limited and appointed Citi to help administer it. **This is issuing-side, not acquiring-side.** Do not pitch Qantas as the card issuer, and do not overweight it.

## Section 2: Financials

| Metric | FY26 | FY25 |
|---|---|---|
| Revenue and other income | **A$25,516M** | A$23,823M (+7.1%) |
| Underlying PBT | A$2,064M | A$2,394M |
| Statutory PBT | A$1,828M | — |
| Statutory profit after tax | **A$1,289M** | A$1,605M (−19.7%) |
| Statutory EPS | 85.4c | — |

Statutory profit was dragged by Jetstar Asia closure costs, the **July 2025** cyber incident (A$15M), legal provisions and redundancies.

**Segment revenue FY26 (A$M):** Qantas Domestic 7,489 · Qantas International 9,326 · Jetstar Group 5,825 · Qantas Loyalty 2,857 · Corporate 9 · Unallocated 10.

**Passengers FY26 ('000):** Qantas Domestic incl. QantasLink 21,392 · Jetstar Domestic 16,697 · Qantas International 8,913 · Jetstar International 8,790 · Jetstar Asia 153 (from 2,593) · **Total 55,945** (+0.1%). RPKs 133,398M · ASKs 157,957M · seat factor 84.5%.

**Split that matters:** Qantas-branded 30.3M pax, **Jetstar-branded 25.6M pax — ~46% of the Group.** And Jetstar is where the payments programme sits.

**No capital raise.** Profitable, listed, dividend-paying. Do not pitch on a funding trigger.

## Section 3: PSP Stack & Orchestration

**Classification: IN-HOUSE / PSS-EMBEDDED (Amadeus).** Not "none detected," not "global orchestrator."

Reasoning: card data is explicitly handed to and vaulted at Amadeus, the PSS provider; no independent orchestration layer is in evidence; and payment-method availability is sliced by departure country and basket contents in a way that reads as **PSS/market configuration rather than merchant-side routing logic.** Confidence: moderate-to-high on architecture, **zero on acquirer names.**

**Booking funnel source code** (pages pulled: `/en-au/book`, `/book/flights`, `/en-us/book`, `/payment-options`, `/payment-options/cards`, `/schedule-of-fees`):
- **Adobe Experience Manager** edge delivery — `/scripts/aem.js`
- **Adobe Experience Platform Web SDK (alloy)** — preconnect `edge.adobedc.net`
- **Akamai Bot Manager** — obfuscated sensor paths (`/eAugQS/DYgvOE/rtL/l1y79/...`), visible in my own fetch. This is why deeper paths return 403/503.
- Front end **Preact** with in-house design system `@qantas/react-runway`
- Loyalty on a separate host: `cdn.qantasloyalty.com`
- **No payment scripts or payment-host preconnects on the public funnel pages** — consistent with card capture on a deeper authenticated step handed to Amadeus.

**Tech profiler unavailable:** `builtwith.com/payment/qantas.com` returns *"We cannot lookup results on this domain sorry."*

**Unevidenced, flagged as unknown:** merchant acquirer(s) · whether 3DS2 is deployed and via which vendor · whether any multi-acquirer routing exists beneath Amadeus · tokenisation scheme · Qantas-side fraud tooling. The live card-entry page requires an authenticated booking session past Akamai and **was not reachable**.

## Section 4: Fees & Surcharging — a live cost-of-acceptance signal

- **New Zealand:** a card payment fee **per ticket per card** applies to credit, charge, debit and prepaid cards, **PayPal and Zip**, unless an exception applies.
- **Australia and New Zealand:** card payment fee per ticket per card applies **when using Apple Pay**.
- **Fee-free routes:** PayID and BPAY (AU), Alipay (China), and redeeming entirely in points.
- Points Plus Pay bookings from NZ attract a fee unless a fee-free method is used.

**Qantas is passing acceptance cost to the customer in NZ and steering toward account-to-account rails that are fee-free.** That is a merchant that already thinks in cost-of-acceptance terms.

⚠️ **Contrast worth knowing, and it is live right now:** Virgin Australia's own payment page states *"From 1 October 2026, Virgin Australia will not apply a payment surcharge to any payment method"* — verified first-hand, see `2-ready-to-outreach/virgin-australia.md`. Reporting indicates **Qantas has signalled it will raise base fares rather than absorb the cost.** The two carriers have taken opposite paths on the same regulatory change, five days ago.

## Section 5: Split Tender — genuinely hard, and a credibility-builder

**Points Plus Pay** — *"lets you choose how you pay for your booking using the mix of points and cash that suits you… Simply use the slider on the payment page."*
- Works across **Qantas (QF), Jetstar (JQ) and Jetstar Japan (GK)** flight numbers plus selected partners.
- Explicitly combinable with *"a debit or credit card, **Alipay, PayID, PayPal or Zip**"* — points pair with four non-card rails, **each with its own market restriction.**
- Points also cover taxes, fees and carrier charges.
- **Split tender is blocked** when carbon credit or travel insurance is in the basket.
- **Multi-Currency Pricing is NOT available on Points bookings** — the FX and loyalty rails are mutually exclusive.

**Pay Per Person** — *"each traveller on the same booking can pay for their flights and added extras separately using their own debit or credit card."* Up to **nine travellers and nine payment cards per booking.** Payment must complete for **every** passenger at booking time or the whole booking cancels.

**A nine-way split-tender authorisation with all-or-nothing basket semantics, layered on top of points split-tender.** Worth naming on a call — it demonstrates Prateek understands the actual problem.

## Section 6: Multi-Currency Pricing — DCC-shaped

Available on bookings **departing Australia or New Zealand**, by Mastercard, Visa or Amex, in **10 currencies**: AUD, CAD, EUR, GBP, HKD, JPY, NZD, SGD, CHF, USD.

> *"enter your card details on the Payment page and select the currency you want to pay in. You can then choose to pay in that currency, or the original currency quoted."*

That choose-at-payment-page pattern is **DCC**, not local-currency pricing. *"the exchange rate and any conversion fees will be determined by **your card provider**. The conversion amount shown will include a **Qantas administration charge**."* Refunds are made in the **quoted** currency at the quoted amount.

**So: pricing is AU/NZ-origin-anchored with a customer-elected DCC layer over 10 currencies — not true local-currency pricing per market**, on a carrier with 24.8% of ticket revenue sold offshore.

## Section 7: Loyalty as a transaction environment

- **18.9M Qantas Frequent Flyer members** at June 2026 (17.6M at June 2025, +7%); >1M net new; ~40% of new members under 30.
- Points earned **242B** · points redeemed **202B** (both +9%).
- **Total rewards redeemed reached 10 million in FY26.** Flight Reward seats booked **>5 million** (+3%).
- Qantas Business Rewards **>706,000 members** (+11%) — 1 in 4 Australian SMEs.
- **>260,000 new Qantas Points-earning credit cards acquired in FY26**; >35% market share; **commercial terms re-agreed with the five largest card partners.**
- Hotels, Holidays and Tours **TTV +3%** — and Qantas defines TTV as *"bookings made using cash and/or Qantas Points."*
- New Reward Flight search tool launched **March 2026**: **>20M searches** across Qantas, Jetstar and 30+ partner airlines.

**Loyalty overhaul announced February 2026** — described by Qantas as the most significant changes to earning and retaining status since the programme's inception, rolling out **late 2026 through 2027**: Status Credit rollover (Gold/Platinum up to 50%, Silver 25%), **on-the-ground status earn from everyday spending** (up to 140 Status Credits from non-flying activity), Points Club and Green Tier retired into one pathway.

**Why this is a payments signal:** "earn status from everyday spending" means ingesting third-party and card-linked spend data at scale. **Mixed cash-plus-points checkout is an orchestration problem**, and it is a sharper angle than core air ticketing.

## Section 8: Buying Signals

### ⭐ The Payment Transformation programme — the strongest signal on the account
**"Digital Product Owner – Payment Transformation", Qantas Group**, Melbourne CBD head office, hybrid 3 days onsite, **fixed-term to December 2027.** Per the listing:
- *"help shape and deliver the **Payment Transformation** initiative to transform how **card payments are made by Jetstar customers**"*
- *"will make **security and technology resilience** improvements to how we **process card payments**"*
- *"spans **all Jetstar digital points of sale, channels and flows**"*
- *"work closely with the Payment Transformation squad, I.T., Finance and Legal teams as well as **third party payment providers**"*

**A named, funded, multi-year payments programme with a dedicated squad, scoped to every Jetstar digital checkout, explicitly involving third-party payment providers.** Dec-2027 term means it is mid-flight now.

⚠️ **Two cautions.** (1) **It is Jetstar-scoped, not Qantas mainline.** It is a Group programme, but the customer-facing scope named is Jetstar. Say so, or get corrected on a call. (2) Both source URLs (startup.jobs, ZipRecruiter AU) were **blocked to direct fetch** — startup.jobs returned 403 behind a Cloudflare challenge. The quotes are assembled from two independent search extracts that agree. **Confirm on careers.qantas.com before quoting verbatim to them.**

**Second role:** **"Senior Payments Analyst", Melbourne** — careers.qantas.com/job/senior-payments-analyst-in-melbourne-jid-1644. A standing in-house payments function exists. ⚠️ **The listing could not be read** (503 to WebFetch, empty reply to curl — Akamai). **Do not attribute reconciliation/chargeback/cost-of-acceptance duties to it** — that detail is unverified.

**Third role:** **"Head of Digital", Jetstar, Melbourne** — *"Lead Jetstar's transformation from airline to hyper-personalized travel retailer."* `[UNVERIFIED — title and strapline from search results, not fetched]`. "Airline to travel retailer" is the standard framing that precedes ancillary/payments/offer-order work.

**Public payment RFP: NONE FOUND.** State this as a clean negative. The Payment Transformation role is the substitute signal — work is happening without a public tender.

### Leadership — note the December 2025 reshuffle
| Name | Role | Appointed |
|---|---|---|
| **Vanessa Hudson** | Group CEO & MD | Sep 2023 |
| **Rob Marcolina** | Group CFO | at Qantas since Oct 2012 |
| **Rachel Yangoyan** | **Group Chief Technology, AI and Transformation Officer** | **December 2025** |
| **Andrew Glance** | **CEO, Qantas Loyalty and Customer** | **December 2025** |
| **Cam Wallace** | CEO Qantas International & Freight; **also took Qantas' digital channels** | digital remit **Dec 2025** |
| **Stephanie Tully** | CEO, Jetstar Group | Nov 2022 |
| Andrew Monaghan | Group Chief Risk Officer (incl. cyber) | Nov 2023 |

**There is no CIO, CDO or Chief Digital Officer, and no publicly named payments owner at executive level.** Payments sits functionally under Yangoyan (technology/transformation) and commercially under Wallace (digital channels) for Qantas, and under Tully for Jetstar — with the actual programme staffed at product-owner level in Melbourne.

**Three of the most relevant portfolios were re-cut in the same month (December 2025).** A ~10-month-old org structure with a new technology chief is a live window.

### Network changes — adding selling markets while removing operating entities
- **Trans-Tasman expansion** announced Sep 2025 — ~210,000 extra seats across the Tasman in 2026; first A220 international flights.
- **Feb 2026:** A220 onto Brisbane–Wellington.
- **June 2026:** Jetstar Brisbane–Queenstown (snow season); Qantas returns Gold Coast–Auckland.
- **Mid-2026:** Qantas Sydney–Apia (Samoa) via Auckland.
- **August 2026: Jetstar Melbourne–Colombo** — Australia's first low-cost service to Sri Lanka. **On-territory: Sri Lanka is in the South Asia list, and it is a new Jetstar selling market needing local payment acceptance.**
- Also flagged: new Perth international routes, Western Sydney, Christchurch, Las Vegas.

## Section 9: Complaints & Incidents — read the corrections carefully

### ⚠️ CORRECTION: the cyber incident is July 2025, NOT 2026
- Unusual activity detected **Monday 30 June 2025**; **ASX announcement Wednesday 2 July 2025.**
- Vector: a **third-party customer servicing platform used by a Qantas contact centre** — reported as Salesforce accessed via voice-phishing of offshore call-centre staff.
- **Scale: 6 million service records on the platform; Qantas later confirmed ~5.7 million customers actually impacted.** Use 5.7M.
- Compromised: names, emails, phone numbers, dates of birth, frequent flyer numbers, tier status, gender, meal preferences; **691,600 home addresses.**
- ✅ **NOT compromised: credit card details, personal financial information, passport numbers.** Not stored on the affected system. Also not accessed: frequent flyer accounts, passwords, PINs, login details.
- **On 16 July 2026 the Australian Privacy Commissioner published a report concluding the OAIC's preliminary enquiries did not reveal any omissions or failings** in Qantas' steps to protect personal information or to ensure its third-party provider complied with the Privacy Act. **The OAIC closed the matter without a formal investigation.**
- Cost: A$15M, excluded from Underlying PBT.

**🛑 DO NOT use this as a payments hook.** It is a CRM/contact-centre breach with **no payment-card dimension**, the year in the original brief was wrong, and **the regulator publicly cleared Qantas.** Raising it as a payments issue would be factually wrong and would destroy credibility with a payments buyer.

### ⚠️ The double-charge story is from September 2016 — ten years old
Customers "charged at least twice when they booked with Jetstar and Qantas", including a Wellington customer charged three times. NZ press report dated **15 September 2016.** Qantas' response then: *"a banking glitch had resulted in rare cases of double debiting… There is sometimes a delay when banks and payment providers release pre-authorised funds."* **Useless as a current hook; actively damaging if cited as recent.**

### ⚠️ ACCC "ghost flights" was NOT a payments matter
Qantas sold tickets on 8,000+ already-cancelled flights between May and June 2022. **Settled May 2024, approved by the Federal Court October 2024: A$100M civil penalty + A$20M remediation to ~86,000 customers.** This was a **consumer-law / misleading-conduct matter about selling cancelled inventory** — it did not involve payment systems, card data or a payment failure.

### Refund handling — Qantas settled, Jetstar is still in court
- **Qantas Flight Credits Class Action** (filed Aug 2023): flights 1 Jan 2020 – 1 Nov 2022 cancelled by Qantas, alleged breach of refund obligations. **Qantas announced a settlement 13 March 2026**; court approval hearing **October 2026.** (AR2026 Note 34B, "Concluded legal matters".)
- **🔴 STILL OPEN — and it is Jetstar.** **Jetstar Airways Pty Limited class action, filed August 2024**, Federal Court. Flights 1 Jan 2020 – 1 Nov 2022 cancelled by Jetstar. Alleges Jetstar **breached contractual obligations regarding refunds**, **misled customers about their rights**, and was **unjustly enriched by holding customer funds.** Defence filed October 2024 denying the allegations. **Outcome unknown, no provision recognised** (AR2026 Note 34A).

**Do not describe Qantas refund handling as currently broken.** But *"Jetstar is still in court over holding customer funds, and is simultaneously standing up a Payment Transformation squad scoped to every Jetstar digital checkout"* is a defensible, dated, two-source observation — **and it is the strongest narrative in this research.**

### ProductReview.com.au — honest null
**Qantas: 1.5 stars from 4,621 reviews** (11% positive). **No recent (2025–2026) reviews mentioning card declines, double charges or checkout failures.** Payment/refund complaints are a **minor** category; dominant themes are delays/cancellations, service wait times, baggage and food. **Do not overstate this source.**

The refund-adjacent complaints that do appear are **service-refund, not payment-rail, issues**: a A$100 extra-legroom seat refund taking 14 days after eligibility was acknowledged (~2 Oct 2026); a A$15 credit for a lost premium seat (~2 Oct 2026); a partial-cancellation refund dispute offering A$1,000 against a ~A$6,000 two-passenger booking (~Jul 2026). **Ancillary/seat refund handling and partial-cancellation refund logic are the live friction — not authorisation or capture.**

### Reddit — honest null
The `site:reddit.com` search returned almost nothing; the engine substituted Australian Frequent Flyer threads. **Treat Reddit as a null result, not a corroborating source.**

### Australian Frequent Flyer — the actual richest Australian source
| Issue | Frequency | Note |
|---|---|---|
| Double charge | Moderate, recurring | thread 107710 |
| Card payment error (code 4620) paying taxes on a points booking | Isolated–moderate | thread 95759 |
| **"Avoid PayID payment to Qantas"** | Isolated but recent | thread 111643 |
| Refund routed to a **closed card**, unresolved after 3 months (>A$1,200 taxes to a closed ANZ card) | Isolated | posts 2917652 / 2927022 / 2927087 |
| General Qantas IT gripes incl. booking/payment failures | High-volume thread | thread 92613 |
| Payment-step failures requiring logout / cache-clear to reach the payment screen | Anecdotal | thread 98463 |

**Two are genuinely good:** the **PayID** thread (an Australian A2A rail failing at Qantas checkout — exactly an APM orchestration story) and the **refund-to-closed-card** case (refund routing logic). ⚠️ **Both are `[UNVERIFIED]` as to exact dates — thread URLs captured, pages not fetched. Get the dates before using them, and never put a forum anecdote in an email as fact.**

**Also:** *"Qantas Cancelled Flights 6 Months after Booking Date Because They Failed to Take Payment"* — Qantas was unable to take payment; the customer's bank declined repeat attempts as duplicates or for insufficient credit (ozbargain node 730365, `[UNVERIFIED date]`). **This is a retry-logic / dunning failure mode and is the most Yuno-shaped complaint in the whole set.**

### Outages
| Incident | Date | Payment-related? |
|---|---|---|
| **Amadeus platform outage took Qantas bookings down worldwide**, hardware issue | **28 June 2017** | GDS/booking — **but in the layer holding the card vault** |
| Partner-airline Classic Reward seats wiped from the booking system, premium cabins only | **25–26 Aug 2026** | Booking/inventory, **not payments** |
| Frequent Flyer site down ~4 hours after a system upgrade | **~early 2010s** — the report cites 11.4M members vs 18.9M today | Loyalty redemption. **Do not cite a date** |

**No payment or checkout-specific outage with a confirmed 2025 or 2026 date was found.**

## Section 10: ICP Score — 19 / 29 → ⭐ High

| Signal | Max | Score | Evidence |
|---|---|---|---|
| Transaction volume | 5 | **5** | 55.9M pax FY26, A$25.5bn revenue, ~2.5–3.5M card txns/month DERIVED |
| Orchestration posture | 4 | **1** | **In-house / PSS-embedded (Amadeus)** — verified first-hand |
| Operates 3+ countries | 3 | **3** | 8.9M Qantas Intl + 8.8M Jetstar Intl pax; sells in 8+ named markets |
| Multiple PSPs in parallel | 3 | **0** | ⬜ **Deliberate zero.** Acquirer set is not publicly disclosed anywhere. No evidence either way |
| Local rail gap in a top market | 3 | **3** | **Google Pay absent** while Apple Pay live, 63.82% mobile · no UnionPay/WeChat Pay despite China/HK/TW JCB footprint · Alipay China-only · PayID AU-only |
| Recent market expansion | 2 | **2** | **Jetstar Melbourne–Colombo Aug 2026** · trans-Tasman +210k seats · Gold Coast–Auckland · Sydney–Apia |
| Known payment issues | 2 | **2** | Jetstar class action alleging unjust enrichment from **holding customer funds** (live) · AFF PayID and refund-to-closed-card threads · failed-payment-causes-cancellation case |
| Recent funding | 2 | **0** | ⬜ Profitable, listed, dividend-paying. No raise. **Do not pitch a funding trigger** |
| Traffic outside home market | 2 | **2** | **24.8% of ticket revenue sold offshore (A$5,756M)**, by Qantas' own point-of-sale accounting |
| Competitor on orchestration | 2 | **0** | ⬜ **Deliberate zero.** Virgin Australia: none detected. No APAC carrier peer evidenced on an orchestrator |
| Payment job postings | 1 | **1** | **Payment Transformation programme funded to Dec 2027** + Senior Payments Analyst |
| **TOTAL** | **29** | **19** | ⭐ **High** |

**Three deliberate zeros**, taken because the evidence is not there: multiple PSPs, recent funding, and competitor orchestration. A score of 19 without inflating those rows is a genuinely strong account.

## Section 11: Outreach Angles, Ranked

1. **The card vault and payment path both sit inside the Amadeus PSS.** First-party, verbatim, citable from their own site. **Pair it with the 28 June 2017 Amadeus outage that took Qantas bookings down worldwide** — concentration risk in the layer that holds the cards. This is the ANZ routing/failover/cost-of-acceptance framing landing on evidence, not assertion.
2. **Google Pay absent while Apple Pay is live**, on a property that is 63.82% mobile in an Android-majority market. Narrow, verifiable, hard to argue with.
3. **The Payment Transformation programme** — funded to Dec 2027, dedicated squad, explicitly about card-payment processing, security and resilience, explicitly involving third-party payment providers. ⚠️ Jetstar-scoped — **say so.**
4. **24.8% of ticket revenue sold offshore, while the Singapore and Japan operating entities are being removed.** Ask whether they settle locally. They do not disclose it.
5. **Mixed cash-plus-points checkout at scale** — 18.9M members, 202B points redeemed, 10M rewards, >5M flight-reward seats, TTV defined as cash and/or points, plus a Feb-2026 overhaul pushing earn into everyday spend.
6. **Method availability sliced by departure country and basket contents** — five market-restricted rails, split tender blocked by insurance/carbon-credit line items. Textbook fragmentation.
7. **DCC-shaped Multi-Currency Pricing over 10 currencies, AU/NZ-origin only, mutually exclusive with points.**
8. **Nine-card Pay Per Person with all-or-nothing basket semantics**, layered on points split-tender. Credibility-builder on a call.
9. **The December 2025 leadership reshuffle** — Yangoyan (Technology/AI/Transformation) and Glance (Loyalty + Customer) both new that month; Wallace picked up digital channels the same month.

## Section 12: Do NOT Say

- ❌ That the **July 2025** cyber incident was a payments or card-data breach, or that it was in 2026. No card data was involved and the OAIC cleared Qantas on 16 July 2026.
- ❌ The double-charge story — **September 2016.**
- ❌ That Qantas refund handling is currently broken. Qantas' class action settled 13 March 2026. **Jetstar's is live** — use that, carefully.
- ❌ That ACCC ghost flights was a payments failure. It was misleading conduct over cancelled inventory.
- ❌ That Qantas uses **Outpayce, Nevio, CellPoint, Adyen, Cybersource** or any named PSP. **None is evidenced.**
- ❌ Any **Airwallex** association — judged a search artefact from Airwallex's own marketing pages ranking for the query. Not evidence.
- ❌ Forum payment-failure anecdotes as fact. They are discovery questions.
- ❌ That Qantas issues the Qantas Premier card. **NAB does**, on Qantas' behalf.
- ❌ **POLi** — the grep hit was the substring in "policy". Not offered.
- ❌ **PayTo** when you mean **PayID**. Different rails.
- ❌ Pitching **Jetstar Asia** (closed 31 Jul 2025) or **Jetstar Japan** (being divested, completion by Jun 2027, never consolidated).

## Section 13: Research Confidence

**Overall: HIGH on architecture and methods, ZERO on acquirers.**

- ✅ **Verified first-hand by me:** the Amadeus card-vault text (byte offsets 14165 and 14271, HTTP 200, control 27 `payment` hits), the accepted-card list, the NZ card payment fee, UATP and JCB market restrictions, Google Pay's absence, the POLi false positive.
- ✅ **Primary source:** Qantas Annual Report 2026 (ASX release 27 Aug 2026, 150pp) extracted in full — all financials, passenger statistics, segment data, Note 4A geographic revenue, Notes 33/34 on the cyber incident and litigation.
- ⚠️ **Blocked:** the live card-entry page (requires authenticated session past Akamai Bot Manager) · careers.qantas.com (503/empty) · startup.jobs (403 Cloudflare) · `qantas.com/agencyconnect/.../qantas-payment-policy.html` (503, then HTTP/2 INTERNAL_ERROR) — **this page likely holds the agency/BSP settlement and acquiring detail and is the highest-value unread source. Worth a manual browser look.** · builtwith.com refused the domain · the qantas.com subsidiary-companies page (503).
- ⚠️ **Unresolved:** merchant acquirer(s) · local settlement by market · 3DS2 deployment and vendor · tokenisation scheme · fraud tooling · whether Amadeus/Outpayce performs multi-acquirer routing underneath · dates on the AFF forum threads.

</details>
