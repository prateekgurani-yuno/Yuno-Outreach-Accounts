# Virgin Australia

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 15 / 29 → 🟢 **Medium**
**Industry:** Aviation — domestic and short-haul international airline, Velocity loyalty · **HQ:** Virgin Australia Holdings Limited, ABN 54 100 686 226 (ASX: **VGN**), Australia; operating entity **Virgin Australia Airlines Pty Ltd ABN 36 090 670 965** · **Researched:** 2026-10-06 · **First email sent:** —
**Motion:** ⬜ **UNCERTAIN — deliberately not classified.** No orchestrator found and no gateway or acquirer evidenced. The checkout is Sabre-resident, which *suggests* payments sit in the PSS layer, but that is a hypothesis, not a finding. **Do not assert a motion in outreach.** Lead on cost of acceptance, which is first-party verified.

---

> ## ⭐ THE FINDING — their cost of acceptance became a P&L line five days ago, on every rail
>
> I pulled `https://www.virginaustralia.com/au/en/help/payment-options/` myself (HTTP 200, 286,004 bytes). The page carries a live AEM notification widget. Verbatim, from the page's own JSON payload:
>
> ```json
> {"errorType":"information",
>  "heading":"From 1 October 2026, Virgin Australia will not apply a payment surcharge to any payment method.",
>  "description":" Some banks and payment providers may charge account fees, interest, late payment fees,
>  foreign currency fees or other charges under your agreement with them. Any such charges are set by
>  your payment provider under your agreement with them, not by Virgin Australia."}
> ```
>
> **Today is 6 October 2026. This took effect five days ago. And note the scope: "any payment method."**
>
> **The RBA mandate is narrower than what Virgin has done.** The ban covers only designated eftpos, Mastercard and Visa. **American Express is explicitly outside it, and so are PayPal and Zip.** Virgin went further than required and dropped recovery on **every rail, including the expensive ones.**
>
> **The surcharges they just gave up** (pre-1-Oct figures from their own payment pages; the live page no longer shows any fee):
>
> | Method | Former surcharge |
> |---|---|
> | PayPal / PayPal Pay in 4 | **0.99%** |
> | **Zip** | **1.27%** |
> | PayID | nil (already fee-free) |
> | POLi | nil (already fee-free) |
>
> **And here is the asymmetry that makes this sharp rather than generic.** Consumer credit interchange is capped at a hard **0.30%** from the same date, down from a ~0.50% weighted average — the RBA estimates ~A$910m/year of system-wide merchant savings. So interchange relief **partly offsets** the surcharge loss on Visa, Mastercard and eftpos.
>
> **But it offsets nothing on Amex, PayPal or Zip — which are uncapped AND now unrecovered.** Zip at 1.27% absorbed on an airfare is a material unit-economics hit, and Zip is a method Virgin actively promotes ("Fly now, pay later with Zip").
>
> **The mix now shifts value hard toward the rails they can neither surcharge nor cap.** That is the entire pitch for this account, it is first-party evidenced, and it is five days old.

---

> ## 🎯 THE SECOND HOOK — and it is the cheapest answer to the first
>
> **PayTo is absent. Verified by direct string count on the retrieved page: `payto` = 0 occurrences.** (`bpay` = 0, `afterpay` = 0, `klarna` = 0.)
>
> ⚠️ **Be precise, because the lazy version of this claim is factually wrong.** They **already run PayID**, which is NPP. A naive "you have no A2A rail" opener gets Prateek corrected immediately.
>
> **The real distinction:** PayID is a **push** payment — the customer initiates a one-off credit transfer from their banking app, no stored mandate. **PayTo is a pull-based, mandated rail** — which is what actually competes with cards for airline use cases: instalments, ancillaries added post-booking, change fees, corporate recurring, and anything needing a re-charge without re-authentication.
>
> **They have the cheap rail for a single upfront payment and nothing mandate-based.** With surcharging gone on all methods as of five days ago, PayTo is the obvious cost-of-acceptance conversation — **and the live PayID integration proves they can already reach NPP.**
>
> **One more detail that lands this.** Their Points + Pay slider historically **affected the credit card surcharge calculation** — the split-tender and surcharge logic were coupled. As of 1 October that coupling is **dead code.** Their checkout's pricing layer has just had to change. That is a concrete, verifiable reason the payment layer is open right now.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Australia's second carrier — domestic and short-haul international, plus the Velocity Frequent Flyer programme. Returned to the ASX **24 June 2025** after Bain Capital ownership. FY26 revenue **A$6.278bn** (+8.1%), underlying NPAT **A$404m** (+22%), **21.3m passengers** (+3.2%), first dividend since re-listing.

**SimilarWeb total visits:** **5.804M** (Aug 2026), **Australia 92.68%** — **supplied by Prateek**, Similarweb PRO. Full table in `accounts/traffic/virgin-australia.md`.

### 🛑 Do NOT use cross-border approval rates on this account
**92.68% domestic.** Nothing found contradicts it, and the whole stack is built for a domestic flyer: **no UnionPay, no JCB**, PayID restricted to AUD and Australian bank accounts, POLi restricted to NZ departures. Per `.claude/reference/apac-payments.md` §6b, the corridor argument has no corridor here. **ANZ is the one sub-region where routing, failover and cost-of-acceptance framing lands most directly** — use that instead, and this account is the purest example of it in the batch.

### Transaction volume — SOURCED passenger count, DERIVED transactions
| Input | Value | Status |
|---|---|---|
| FY26 passengers carried | **21,300,000** | **SOURCED** — FY26 results, ASX 28 Aug 2026 |
| ÷ 12 | ~1.775M passengers/month | DERIVED |
| FY26 revenue | **A$6.278bn** | **SOURCED** |

**Clears the 40,000/month gate by orders of magnitude.** For scale on the pitch: **10bp of acceptance cost on A$6.278bn ≈ A$6.3m/year**, against **A$753m underlying EBIT**. Basis points are visible at this size. ⚠️ Not all A$6.278bn is card-not-present — do the arithmetic properly before putting a number in an email.

### Payment methods — verified first-hand from virginaustralia.com
| Method | Scope | Status |
|---|---|---|
| Visa, Mastercard, **AMEX**, **Diners**, **UATP** | — | ✅ from the payment-logo assets at `/content/dam/vaa/images/payments/` |
| **Apple Pay** | incl. desktop-to-iPhone QR-scan flow | ✅ |
| **Google Pay** | — | ✅ **present** (unlike Qantas) |
| PayPal | — | ✅ |
| **PayPal Pay in 4** | AUD bookings only, purchase-value limits | ✅ |
| **PayID** | AUD only, Australian bank accounts only, outbound flight must depart an Australian city | ✅ |
| **POLi** | **New Zealand only** — NZ personal bank accounts, outbound flight must depart NZ | ✅ |
| **Zip** | "Fly now, pay later with Zip", AUD only, credit approval | ✅ |
| **Travel Bank** | travel-credit wallet, pay entirely or partially, separate login | ✅ |
| **Velocity Points** | incl. *"a combination of Points plus an eligible payment method"* | ✅ |
| **Pay-by-link** | contact centre: *"we'll send a secure payment link by email or SMS"* | ✅ second distinct channel |

**Verified ABSENT (direct string count = 0):** **PayTo**, **BPAY**, **Afterpay**, **Klarna**. Also no UnionPay, no JCB.

**3DS:** the page says *"Complete any verification requested by your card issuer"* — consistent with 3DS/SCA, **vendor not named.**

⚠️ **False positives caught and resolved:**
- **`poli` — 15 raw hits, 11 spurious**: `policy`, `policies`, `referrerpolicy`, `aria-live="polite"`, `/about-us/policies/`. **But POLi is genuinely offered** — confirmed by the real asset `img/sandbox/poli-logo-blackonwhite`, an outbound link to `polipay.co.nz/consum...`, `<h3>POLi</h3>` and *"Conditions - POLi"*. The method is real; the code-level matches were coincidental.
- **`eWay` — DISCARDED.** The hits were the substring inside `"fightTypeOneWayLabel":"One way"`. Not the eWAY gateway.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

> **Not yet generated.** Run `/full-outreach Virgin Australia` to compose the 12-touch sequence into this section.
>
> **Motion is UNCERTAIN (⬜).** Per `/full-outreach` Step 6a, none of the four motion scripts cleanly applies. **Do not open with "you have no orchestration layer"** — that is unevidenced and the Sabre-resident checkout makes it likely wrong. Open on the surcharge change, which is their own published fact.
>
> **Entry point: Paul Jones, Group Chief Customer & Digital Officer** (ex-Qantas) — owns customer value proposition and digital experience. ⚠️ **No executive with explicit payments ownership exists.** Verify the CIO situation before naming anyone — see Section 6.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

## Section 1: Entities

- **Virgin Australia Holdings Limited** — listed entity, **ASX: VGN**, ABN 54 100 686 226, incorporated 27 May 2002.
- **Virgin Australia Airlines Pty Ltd** — ABN 36 090 670 965, named in the website footer as the operating entity. Verified first-hand in the payment-options page footer.

**Not a PSP or payment-infrastructure company.** Australia-HQ'd, in territory, in industry. No Partnerships reroute.

⚠️ **`virginmoney.com.au` appears as an outbound link in Virgin Australia homepage HTML** — that is the **co-brand card partner**, i.e. issuing-side. It is **not** Virgin Australia payment infrastructure. Do not treat it as such.

## Section 2: Financials — FY26, ASX announcement 28 August 2026

| Metric | FY26 | Change |
|---|---|---|
| **Revenue** | **A$6.278bn** | +8.1% |
| Statutory NPAT | A$501.2m | +4.7% (FY25: A$478.5m) |
| **Underlying NPAT** | **A$404m** | **+22%** |
| Underlying EBIT | A$753m | +13.4% |
| Underlying EBIT margin | 12% | up |
| **Passengers carried** | **21.3 million** | +3.2% |
| Dividend | 7.6c fully franked | **first since re-listing** |
| **Transformation Program** | **>A$450m gross benefits in FY26** | — |

## Section 3: 🔴 ASX re-listing — a major buying signal

**Virgin Australia returned to the ASX on 24 June 2025** under ticker **VGN**:
- IPO raised **A$685m** (US$439m), **30.2%** of shares on issue
- Priced at **A$2.90/share** — **A$2.3bn** market cap, **A$3.6bn** enterprise value, a **~30% discount to Qantas**
- **Shares rose 8.3% on debut**
- Ownership after float: **Bain Capital reduced to ~40%**, **Qatar Airways 23%**, management 7.8%
- Bain locked up until after the December half-year result

**Why it matters:** 15 months listed, first dividend just declared, **Bain still holding 40% and wanting to exit into a strong price.** Every cost line is now under public-market scrutiny — and payment costs just became a visible, unhedged one.

## Section 4: PSP Stack — an honest nil result on the gateway

**Classification: no orchestrator detected; gateway and acquirer CANNOT be classified on available evidence.** This is a genuine nil result, not an unfinished search.

### Sabre is the PSS — confirmed twice over
- `[Source Code]` Homepage JSON config carries **31 `sabre` references**: `sabreLengthOfStayMinOffset`, `sabrePicDomesticEnabled`, `sabrePointsAndRewardsInCalendarEnabled`, SSO entity ID `spEntityId=sabre-dx` pointing at `https://book.virginaustralia.com/dx/VADX/`. Live Sabre-hosted host: `https://conciergeiq.virginaustralia.sabre.com`.
- `[Press Release]` Switched to Sabre for bookings and check-in **January 2013**; **July 2015** renewed and expanded the **SabreSonic Customer Sales & Service (CSS)** contract, adding Customer Data Hub, Customer Experience Manager, Dynamic Retailer and SabreSonic Select.

The booking engine is **Sabre Digital Experience (`/dx/VADX/`)** on `book.virginaustralia.com`. **The practical implication — that the payment integration sits inside Sabre's payment layer rather than a Virgin-owned orchestration tier — is a HYPOTHESIS, not a finding.** `[INFERENCE, not confirmed]`

⚠️ **Note the contrast with Qantas.** Qantas publishes, in its own terms, that its card vault sits at **Amadeus**. Virgin publishes **no equivalent statement about Sabre.** The architectures may be analogous but the evidence is not — and the Qantas file should not be used to infer Virgin's.

### Accertify = fraud prevention. First-party, unambiguous.
`[Source Code]` The homepage carries a literal developer comment and beacon loader:
```html
<!--To connect with Accertify for fraud prevention purpose-->
<script type="text/javascript" async="true">
   s.setAttribute( 'src', "https://prod.accdab.net/cdn/cs/mCNBIX4OJrsLXHdsDVJl2N8awC8.js");
```
`prod.accdab.net` is Accertify's device-fingerprinting CDN. **Accertify is owned by American Express.** This is the single strongest stack datapoint on the account. ⚠️ **It is fraud prevention. Do not represent it as anything more.**

### Why the checkout could not be read
**Imperva (Incapsula) Advanced Bot Protection fronts the booking engine.** `book.virginaustralia.com/dx/VADX/` returns a 6KB "Pardon Our Interruption" interstitial with `reeseSkipExpirationCheck`, `initializeProtection()` and `/_Incapsula_Resource?NWFURVBO=`. **The payment page is unreachable without executing the bot challenge.** Not a search failure.

**CMS:** Adobe Experience Manager (`/content/dam/vaa/…/_jcr_content/renditions/`) plus Adobe Edge Delivery (`rum.hlx.page`) and Adobe Launch (`assets.adobedtm.com`).

### Searched and NOT found
- **Zero** hits for Adyen, Stripe, Cybersource, Worldpay, Braintree, Checkout.com, CardinalCommerce, Windcave, eWAY, Tyro, SecurePay, Fat Zebra, Pin Payments — in homepage or payment-page HTML, and nothing in public sources.
- **Zero** evidence of CellPoint Digital, Spreedly, Primer, Gr4vy, Juspay or "payment orchestration" in connection with Virgin Australia. Searches surfaced only vendor and comparison pages, none naming the airline.
- **IATA Pay:** no evidence. **Amadeus:** no evidence, and ruled out in practice by the Sabre findings.
- **BuiltWith refused the domain:** *"We cannot lookup results on this domain sorry."*

## Section 5: Velocity Points as payment

- **Points Plus Pay:** every **2,500 Points reduces the fare by A$15**, via a **points/cash slider** in the booking flow.
- **🔑 The slider historically affected credit card surcharges** — split-tender and surcharge calculation were coupled. **As of 1 October 2026 that coupling is redundant logic.** A concrete sign the checkout's pricing layer has just had to change.
- Route-dependent: on long-haul international, Points + Pay reduces **taxes only**; on some short-haul international the threshold exceeds ~70% of standard points.
- `[Source Code]` Homepage config exposes `sabrePointsAndRewardsInCalendarEnabled: true` — points-aware fare display is a **Sabre-side capability**.
- **Velocity "Pay with Points" launched May 2025** — newsroom URL identified (`/au/en/newsroom/2025/5/velocity-lauches-pay-with-points/`) but **NOT fetched.** `[UNVERIFIED]` — worth one fetch before referencing.

**Split tender is a real multi-leg requirement here:** Points + Travel Bank + card/wallet, across the Sabre web checkout **and** pay-by-link. ⚠️ **How many tenders can combine in one transaction is unverified.**

## Section 6: Leadership

| Role | Person | Note |
|---|---|---|
| **CEO** | **Dave Emerson** | appointed March 2025 |
| **CFO** | **Race Strauss** | — |
| **Group Chief Customer & Digital Officer** | **Paul Jones** (ex-Qantas) | owns customer value proposition and digital experience — **best-evidenced entry point** |
| **CIO** | ⚠️ **Cameron Stone departed** to TEG as CTO | **successor and departure date UNKNOWN** |

⚠️ **Two caveats, flagged rather than papered over:**
1. **The date of Cameron Stone's departure and who replaced him could not be established.** The CIO seat may be vacant or recently filled. **Verify before naming anyone in outreach — getting this wrong is an own-goal.**
2. **No executive with explicit payments ownership was found.** For an airline this size that is itself informative: payments likely sits split between Digital and Finance. That shapes who to approach and how.

## Section 7: Job listings — read the distinction carefully

- ⚠️ **"Manager, Customer Success (Financial Services)" — Sydney.** HTML retrieved directly (now closed; title and body still present): requires *"Deep knowledge of Financial Services Industry – cards and payments"* and *"Understanding of Loyalty businesses and concepts."* **This is Velocity co-brand card ISSUING, not merchant acceptance. Do not present it as evidence of a payments-acceptance team** — being sloppy here is exactly what gets a rep caught out.
- ⚠️ **"Growth and Transformation Manager"** — *"Velocity-linked financial services as the payment solutions of choice for members."* Again **issuing/loyalty side.**
- ✅ **"Product Owner, Offer & Order (OOSD)" — Brisbane.** Leading development of the Offer & Order platform. **This one is genuinely relevant.** IATA Offer & Order / NDC modernisation restructures how an airline prices and settles an order, and **the order-level payment layer is squarely in scope.** A real modernisation signal.
- Also: Technical Product Manager (Brisbane), Engineer – Developer Platform & AI-enabled SDLC (Brisbane), Digital Business Analyst (Brisbane), Digital Production Operations Analyst.

**Public payment RFP: NONE FOUND.** Expected for a listed private-sector airline — they do not tender payments publicly. Stated as a nil result, not an unfinished check.

## Section 8: 🔴 Complaints — a genuine payment-integrity failure

**61,000 passengers overcharged over five years. ACCC notified. Deloitte administering refunds.**
- Virgin Australia is refunding **more than 60,000 / ~61,000 guests** it *"inadvertently overcharged"* on **itinerary changes**
- **Average refund ~A$55**
- Window: **21 April 2020 – 31 March 2025**
- Cause: tickets **"repriced in a way that does not align with its policy"** when customers changed itineraries — described as an **IT error**
- Scale: **~0.1% of all bookings** in the period
- Virgin **proactively notified the ACCC**; claims administered by **Deloitte Australia**; affected guests must **lodge a claim**, 12-month window; unclaimed money donated to charity

**Why this is usable:** it is a **repricing/settlement-logic defect in the change-and-rebook flow**, publicly disclosed, regulator-visible, and **it ran undetected for five years.** That is precisely the failure mode a reconciliation layer surfaces. ⚠️ **Handle it respectfully — they self-reported it.** Do not frame it as a scandal.

**Weaker themes (aggregator-sourced):** refunds owed on cancelled flights, unprocessed credits, **double charges** (noted as especially post-COVID), booking system failures including codeshare errors. Individual case: *"Virgin Australia overcharged me A$4500"* (AFF thread 90830).

⚠️ **ProductReview.com.au — NOT OBTAINED.** `/listings/virgin-australia`, `-airlines`, `-au` and `virginaustralia` all returned HTTP 404; a site-search fetch returned only JS navigation chrome. **No ProductReview rating or review count is in this file. Do not cite one.**

⚠️ **Reddit — honest null.** Site-restricted search returned no Reddit results, only news coverage. **"No significant Reddit pattern" is the result.**

## Section 9: Sector context on the surcharge ban

- **Qantas: analysts put between A$144m and A$270m "at risk"** from the RBA reforms — up to **9.4% of Qantas Loyalty annual revenue.**
- **Qantas, Jetstar, Virgin Australia and Rex are expected to raise base fares 1–2%** to recover lost surcharge revenue; **Qantas has signalled it will raise fares rather than absorb the cost.**
- ⚠️ **No Virgin-specific surcharge revenue figure is public.** Searched for; not found. **Do not invent or extrapolate one.**

**🔑 The sharpest framing available on this account:** Qantas is recovering via fare increases. **Virgin's own page commits to no surcharge on any method.** If Virgin raises fares 1–2% it blunts the price-discount positioning it listed on (a ~30% valuation discount to Qantas). **Reducing cost of acceptance is the alternative to raising fares.** That is genuinely non-generic, specific to this company, at this moment.

## Section 10: ICP Score — 15 / 29 → 🟢 Medium

| Signal | Max | Score | Evidence |
|---|---|---|---|
| Transaction volume | 5 | **5** | 21.3m pax FY26, A$6.278bn revenue — both SOURCED |
| Orchestration posture | 4 | **0** | ⬜ **Deliberate zero.** No orchestrator found; gateway/acquirer unevidenced; Sabre payment residency is a hypothesis only |
| Operates 3+ countries | 3 | **3** | Domestic AU + NZ (POLi NZ-departure rail proves NZ selling) + short-haul international + Qatar Airways long-haul partnership |
| Multiple PSPs in parallel | 3 | **0** | ⬜ **Deliberate zero.** Not a single gateway evidenced, let alone two |
| Local rail gap in a top market | 3 | **0** | ⬜ **Deliberate zero, and it cost 3 points.** Their domestic coverage is genuinely good — PayID, POLi, Apple Pay, Google Pay, PayPal, Zip, Travel Bank, Velocity. **PayTo is a real gap but is not yet a *dominant* Australian rail**, so this row does not honestly fire. The PayTo argument lives in the cost-of-acceptance pitch instead, where it is strong |
| Recent market expansion | 2 | **2** | Qatar Airways partnership wet-lease long-haul from June 2025; Offer & Order platform build |
| Known payment issues | 2 | **2** | **61,000 passengers overcharged, ACCC-notified, Deloitte-administered, five years undetected** — dated and sourced |
| Recent funding | 2 | **2** | **A$685m IPO, 24 June 2025** |
| Traffic outside home market | 2 | **0** | ⬜ **Deliberate zero.** 92.68% domestic. This is the opposite of a signal and the cross-border motion is explicitly off |
| Competitor on orchestration | 2 | **0** | ⬜ Qantas is PSS-embedded (Amadeus), not orchestrated. No ANZ carrier peer evidenced on an orchestrator |
| Payment job postings | 1 | **1** | **Product Owner, Offer & Order (OOSD)** — order-level payment layer in scope |
| **TOTAL** | **29** | **15** | 🟢 **Medium** |

**Five deliberate zeros.** The score understates the account: the matrix rewards cross-border complexity and multi-PSP fragmentation, and Virgin has neither — it is a concentrated domestic carrier. **What it does have is a verified, five-day-old, structural cost-of-acceptance problem**, which the matrix has no row for. Read the 15 as "medium on the matrix, high on timing."

## Section 11: Outreach Angles, Ranked

1. **Cost of acceptance became a P&L line five days ago, on every rail.** Their own page: *"From 1 October 2026, Virgin Australia will not apply a payment surcharge to any payment method."* They went beyond the RBA mandate and dropped recovery on Amex, PayPal (was 0.99%) and Zip (was 1.27%) — **none of which get interchange-cap relief.** Strongest, most timely, first-party evidenced.
2. **PayTo absent while PayID is already live.** On NPP but with no mandate-based pull rail — the cheapest available answer to point 1. **Make the PayID/PayTo distinction precisely.**
3. **>A$450m Transformation Program, 15 months on the ASX, Bain at 40% wanting an exit.** A funded cost-out programme with no payments workstream, under public-market scrutiny.
4. **Qantas is raising fares; Virgin committed to absorbing.** Reducing acceptance cost is the alternative to blunting its own price positioning.
5. **The 61,000-passenger repricing defect** — ACCC-notified, Deloitte-administered, undetected five years in the change-and-rebook flow. Reconciliation proof point. Handle respectfully.
6. **Offer & Order (OOSD) build underway** — active modernisation whose order-level payment layer is in scope.
7. **The points slider / surcharge coupling is now dead code.** A concrete reason the pricing layer is open right now.

## Section 12: Do NOT Say

- ❌ Any **named gateway or acquirer** — none is evidenced.
- ❌ That Virgin **uses an orchestrator** — none detected. Equally, do **not** claim they have no orchestration layer; that is unevidenced too.
- ❌ Any **Virgin-specific surcharge revenue figure** — not public.
- ❌ The **Accertify** relationship as anything beyond fraud prevention.
- ❌ The **Financial Services job postings** as merchant-payments hiring. They are **Velocity card issuing.**
- ❌ Any **ProductReview rating** — not obtained.
- ❌ **Cross-border approval rates or APAC corridor framing.** 92.68% domestic.
- ❌ A naive **"you have no A2A rail."** PayID is live.
- ❌ The **CIO's name** until the successor is verified.
- ❌ **eWAY** — the code hit was the substring in `"fightTypeOneWayLabel"`.
- ❌ Anything attributed to **Virgin Atlantic, Virgin Media, Virgin Active, Virgin Mobile or Virgin Money.** A `community.virginmedia.com` "charged twice" thread surfaced in the double-charge search and was discarded — an easy trap.
- ❌ *"Virgin removes fuel surcharges"* — that is **fuel** surcharges, an older unrelated matter. Surfaced twice in surcharge searches and discarded.

## Section 13: Research Confidence

**Overall: HIGH on methods and the surcharge finding. ZERO on the gateway.**

- ✅ **Verified first-hand by me:** the surcharge notice (HTTP 200, 286,004 bytes, quoted verbatim from the page's own AEM widget JSON), PayTo = 0, BPAY = 0, Afterpay = 0, Klarna = 0, PayID = 6 hits, Google Pay present, and POLi's genuineness despite the `policy` false positives.
- ✅ **Primary sources:** FY26 results (ASX 28 Aug 2026) and FY26 Annual Report; the live payment-options page; homepage JSON config.
- ⚠️ **Blocked:** the actual checkout (Imperva Advanced Bot Protection on `book.virginaustralia.com/dx/VADX/`) · builtwith.com refused the domain · ProductReview.com.au (404s + JS-only) · careers search endpoint (403) · `stocksdownunder.com` (403).
- ⚠️ **Unresolved:** the gateway and acquirer · whether Sabre performs the payment processing · 3DS vendor · how many tenders can combine in one transaction · the CIO succession · the May 2025 "Pay with Points" launch detail · Virgin-specific surcharge revenue.

</details>
