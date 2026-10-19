# Philippine Airlines

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 20 / 29 → ⭐ **High Priority** — earned on arithmetic, no override
**Industry:** Aviation — flag carrier, full-service · **HQ:** Pasay City, **Philippines** — `Philippine Airlines, Inc.`, held by **PAL Holdings, Inc. (PSE: PAL)**, Lucio Tan Group · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** 🛑 **IN-HOUSE / PSS-EMBEDDED — the orchestration layer is Amadeus's own.** PAL runs **Outpayce XPP**, and its CFO is publicly on record endorsing it. **Never say they need orchestration.**

---

> ## ⛔ THE MOTION — PAL already has orchestration, and the CFO said so on the record
>
> The internal target list left PAL's orchestrator column **empty**, which invited a greenfield read. That would have
> been wrong. I verified the following myself on Outpayce's own newsroom (HTTP **200 at 11,559 B** against a 404
> control at **466 B**; `XPP` 10/0, `Philippine Airlines` 3/0, `orchestration` 3/0, `Bengzon` 1/0):
>
> **"Philippine Airlines becomes the first carrier to implement IATA Pay through Outpayce's Xchange Payment
> Platform"** — Outpayce (an Amadeus company), **5 September 2024**, last updated 16 June 2025.
>
> > *"Outpayce's XPP system helps us to **intelligently accept a wide range of payment methods** used by travelers
> > across the international markets we serve. Moreover, we can access **various payment methods and partners
> > through XPP**, with detailed analytics on the performance of payment flows and back-end reconciliation support."*
> > — **Anna Isabel Bengzon, Chief Financial Officer, Philippine Airlines**
>
> The same page describes **"XPP's powerful orchestration, analytics and reporting capabilities"** — that phrase sits
> in the block attributed to **Juan Antonio Rodriguez, Director Financial Settlement Operations, IATA**, not in
> Outpayce's own voice. Minor, but attribute it correctly if it is ever quoted.
>
> **So the economic buyer for payments has already bought orchestration, from her PSS vendor, and praised it in a
> press release.** Any sequence that opens on "you have no routing layer" is dead on arrival.
>
> ### Why this is the hardest version of the sale
> | Layer | Vendor | Evidence |
> |---|---|---|
> | PSS | **Amadeus Altéa** (reservations, inventory, DCS) | Press release, agent-fetched ⚠️ date unreliable |
> | Payment orchestration + acceptance | **Outpayce XPP** (wholly Amadeus) | Outpayce newsroom, **verified by me** |
> | Multi-currency pricing | **Amadeus FX Box** — PAL was the first carrier to deploy it | The Paypers, 25 Aug 2021, agent-fetched |
> | Digital commerce storefront | **Datalex** | 2016 five-year reselection ⚠️ **term lapsed ~2021, no renewal found** |
>
> **The orchestration arrived bundled with the PSS.** There is no standalone orchestrator contract to displace and no
> procurement cycle to catch. This is the Qantas/Amadeus pattern (repo: `qantas.md`, 19/29 ⭐) and it is *harder* —
> Qantas had the card vault inside Amadeus; PAL has the routing layer itself inside Amadeus.
>
> ⚠️ **An honest classification caveat.** Outpayce is also sold commercially as a PSP-agnostic travel orchestration
> platform — i.e. a genuine Yuno competitor. A reasonable analyst could label this **Competitive** rather than
> **In-house/PSS-embedded**. I chose PSS-embedded because the incumbency is *structural* rather than competitively
> won, and that distinction drives the angle. **It scores +1 either way**, so the ambiguity does not move the tier.

> ## 🎯 THE HOOK — a payments roadmap shipping every few months, with two conspicuous holes
>
> PAL publishes a **dated, append-only log of every alternative payment method it has switched on.** I verified it
> first-party via the AEM content API (`/ph/en/faq/online-booking.model.json`, **HTTP 200 at 11,701 B** against a
> nonsense control at **404 / 2,392 B**). It is effectively their published payments roadmap:
>
> | Effective | Method | Currencies |
> |---|---|---|
> | 11 May 2021 | **GCash** · GrabPay | PHP · PHP/SGD/MYR |
> | 20 May 2021 | Alipay · **Dragonpay** | multi · PHP |
> | 31 May 2021 | WeChat Pay | multi |
> | 13 Jul 2021 | Financial Process Exchange (**FPX**) | MYR |
> | 21 Sep 2021 | **Billease** (BNPL) · UnionPay · Online Banking | PHP · multi · THB/IDR |
> | 10 Sep 2024 | **PromptPay** · **DuitNow** | THB · MYR |
> | 13 Nov 2024 | **VietQR** · **Faster Payment System** | VND · HKD |
> | 16 May 2025 | **QR Ph** | PHP |
> | **18 Mar 2026** | **PayNow** | SGD |
> | **26 May 2026** | **Korean Local Cards** (Shinhan, Samsung, Hyundai, KB Kookmin, Lotte, Hana, Woori, BC) | KRW |
> | **2 Oct 2026** | **Apple Pay** | no currency restriction stated |
>
> **Three launches in 2026, the most recent 17 days before this research.** This is not a dormant stack — it is an
> actively funded programme with a team and a budget. **That is the single most important commercial fact here:**
> there is someone to talk to, and they are mid-roadmap.
>
> ### Hole #1 — the ASEAN instant-rail sweep has exactly one gap, and it is Indonesia
>
> Thailand got **PromptPay**. Malaysia got **DuitNow**. Hong Kong got **FPS**. Vietnam got **VietQR**. The
> Philippines got **QR Ph**. Singapore got **PayNow**. Every major instant rail in the region, shipped in sequence
> over two years.
>
> **Indonesia has no QRIS.** `QRIS` returns **0** on the master method page; IDR is a supported quoting currency
> served only by generic "Online Banking" and UnionPay. GoPay, OVO and DANA are all absent.
>
> **India is the same shape:** `UPI` returns **0**, and INR appears in exactly one list — UnionPay. The irony worth
> probing gently: **PAL is the world's first carrier on IATA Pay, and IATA Pay's own named rails include UPI (India)**
> — yet UPI is not on PAL's published method list.
>
> ### Hole #2 — Apple Pay shipped 17 days ago. Google Pay is absent everywhere.
>
> `Google Pay` returns **0** across the entire first-party corpus, in every market. Apple Pay went live **2 October
> 2026** with no currency restriction. PAL's biggest markets after the Philippines are the US, Canada and Australia,
> and its APAC footprint is Android-dominant. **One wallet is on the checkout and the other is not** — and the one
> that is missing is the cheap, obvious next item on a roadmap that just shipped its counterpart.
>
> ### The currency picture — and a correction to the obvious read
>
> PAL supports **19 quoting currencies**: PHP, USD, AUD, CAD, GBP, HKD, JPY, NZD, SGD, CNY, MYR, **AED**, KRW, MOP,
> IDR, THB, TWD, INR, VND. ⚠️ **This is genuinely good multi-currency coverage, delivered through Amadeus FX Box
> (PAL was the first airline to deploy it).** Do **not** run the standard "every cross-border sale is a PHP auth
> against a foreign issuer" pitch — for USD, JPY, AUD, CAD, GBP, HKD, SGD, KRW and TWD it is simply false.
>
> **The real currency gap is narrow and specific: there is no SAR and no QAR** — and `mada`, the Saudi domestic
> scheme, returns **0**. PAL runs dedicated `/sa/` and `/qa/` market sites and launched **NDC selling in Saudi
> Arabia and Qatar in June 2025**, yet prices neither in local currency and reaches no local rail. Two of the
> largest overseas-Filipino labour markets on earth.
>
> ⚠️ **Precision required:** multi-currency **quoting** is confirmed first-party. Multi-currency **settlement and
> acquiring** is **not** — who bears the FX and where the margin sits is unknown, and is a discovery question.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Philippine Airlines is the Philippines' flag carrier, operating domestic and international routes with a
business heavily weighted to the overseas-Filipino (OFW/VFR) market. It carried **16.3 million passengers in 2025** on
**$3.22 billion** of revenue. Payments run through **Outpayce XPP**, the payment arm of its PSS vendor Amadeus.

**SimilarWeb visits:** **3.8M** — ⚠️ `[ESTIMATE, not confirmed]`, SimilarWeb free tier, September 2026. **No
SimilarWeb data was supplied for this account**, so the entire country profile is estimate-grade. See Section 1 below.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods (confirmed) | Missing / unresolved | Local entity |
|------|---------|---------|------------------------------|----------------------|--------------|
| 1 | 🇵🇭 Philippines | **57.46%** | Cards+3DS, **GCash**, **QR Ph**, **Dragonpay**, **Billease** (BNPL), GrabPay, PayPal, 0% instalments, 22+ OTC cash partners | **Maya** (main flow), BancNet, InstaPay/PESONet | ✅ HQ |
| 2 | 🇺🇸 United States | 16.75% | Cards, PayPal, **Apple Pay**, Alipay, WeChat Pay, UnionPay, PNB Global Remit OTC | **Google Pay**, BNPL, instalments | ❌ none found |
| 3 | 🇨🇦 Canada | 5.51% | Cards, PayPal, Apple Pay, Alipay, WeChat Pay, UnionPay | **Interac**, **Google Pay**, instalments | ❌ none found |
| 4 | 🇦🇺 Australia | 4.67% | Cards, PayPal, Apple Pay, Alipay, WeChat Pay, UnionPay | **PayTo, BPAY, Afterpay/Zip**, Google Pay | ❌ **GSA model** — Sydney office closed |
| 5 | 🇯🇵 Japan | 2.19% | Cards (JCB + J/Secure), PayPal, Apple Pay, Alipay, WeChat Pay, UnionPay | **konbini**, PayPay/Rakuten Pay, Google Pay | ❌ none found |

⚠️ All traffic shares are `[ESTIMATE, not confirmed]`. Entity column reflects **absence of evidence**, not evidenced
absence — only **Singapore** (`PHILIPPINE AIR LINES, INC.`, UEN **S70FC1978G**) was found, via a third-party ACRA
aggregator.

### Legal entities
- **PAL Holdings, Inc.** (Philippines) — PSE: PAL, SEC ID **PW-94** `[UNVERIFIED]`; 8/F PNB Financial Center, Pasay City
- **Philippine Airlines, Inc.** (Philippines) — the contracting carrier; SEC registration number **not found**
- **Air Philippines Corporation** / PAL Express (Philippines)
- **PHILIPPINE AIR LINES, INC.** (Singapore branch) — UEN **S70FC1978G**, registered 17 Mar 1970 `[UNVERIFIED]`
- ⭐ **Philippine Airlines, Inc. (Korea)** — **Business Registration Number 516-84-00029**, VAT-telecom reg.
  2-01-25-0155, Seoul Finance Center, Jung-gu; representative **Maria Clara Cayabyab De Castro** — **first-party,
  from the `/kr/ko/` footer**

### Known PSPs
- **Outpayce XPP (Amadeus)** — orchestration + acceptance · `[Press Release]`, **verified by me**
- **PayPal** — 11 of PAL's 19 currencies, website only · `[PAL's own FAQ]`, **verified by me**
- **IATA Pay** (A2A, QR Ph in PH) — PAL is the **first carrier globally** on it via XPP · **verified by me**
- **Amadeus FX Box** — multi-currency pricing, PAL was first carrier · `[Third-Party Report]`
- ❌ **No card acquirer or underlying PSP is named in any public source.** Completely opaque.

### Orchestration status
**In-house / PSS-embedded — Outpayce XPP (Amadeus).** Confirmed on Outpayce's newsroom with a CFO quote, 5 Sep 2024.
Honest caveat: arguably **Competitive**, since Outpayce is commercially sold as a PSP-agnostic orchestrator. +1 either way.

### Buying signals
- 🚀 **NDC platform live 19 Jun 2025** across US, CA, SG, HK, JP, AU, UAE, QA, SA — **payments not mentioned once**
- 🚀 **New routes:** Manila–Chicago from 9 Nov 2026 (8th US point); Manila–Palau from 29 Mar 2026
- 🤝 **ARC Direct Connect** partnership (17 Jun 2025); **Travelfusion** (3 Jul 2025); **NDC on Trip.com** (4 Sep 2025)
- 💸 **Margin shock:** H1 2026 swung to a **$25.1m net loss** from $136.7m profit, fuel +$219.5m, passengers −3.1% `[UNVERIFIED]`
- 📋 **No public payment RFP found.** No payment job postings found by two independent agents.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Philippine Airlines` to draft the 12-touch sequence.*

⚠️ **Seven hard constraints:**
- **Motion is PSS-EMBEDDED.** They have orchestration (Outpayce XPP) and **the CFO endorsed it in a press release**.
  Never make the case for orchestration itself. Anchor on **reach, local-rail depth and opportunity cost**.
- **Never name Outpayce, Amadeus, Datalex, CellPoint or any competitor** in outreach-facing text.
- **Do NOT claim a cross-border decline problem.** A dedicated agent hunted it and found **no current evidence**;
  the decline material is undated and isolated. Asserting it would be manufactured and they would know.
- **Do NOT say Cebu Pacific "is orchestrated today."** Adoption is confirmed 2020–21; there is **no CellPoint–Cebu
  coverage in 2025 or 2026**. The defensible line is *"has run multi-acquirer dynamic routing since 2020."*
- **Do NOT pitch growth.** H1 2026 was a **loss** on an 88% Q2 fuel spike with passengers down 3.1%. The correct
  frame is cost of acceptance and recovered revenue to a CFO under margin pressure.
- **Do NOT quote a CellPoint outcome percentage.** The case study contains **no uplift figure, no cost saving and no
  named acquirer** — established in our own `cebu-pacific.md`.
- **Do NOT run the cross-border FX pitch.** PAL supports **19 quoting currencies** via Amadeus FX Box and was the
  first airline to deploy it. For the US, Japan, Australia, Canada, UK, HK, Singapore, Korea and Taiwan the "PHP auth
  against a foreign issuer" story is **false**. The narrow, true gap is **SAR and QAR**.
- **Do NOT say they lack e-wallets in the home market.** GCash and QR Ph are both live. The precise gap is **Maya**,
  which appears only as a Travel Credits top-up, not on the main booking flow.

**Best entry points:** **Justin Warby, VP Sales and Distribution** (verified name + exact title, publicly owns the
NDC programme) and **Anna Isabel Bengzon, CFO** (the economic buyer, already on record on payments).

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 20 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **5** | ✅ **DERIVED — ≥100,000/month, robust across the plausible range.** See the mandatory disclosure below. |
| Orchestration status | **1** | ⚠️ **In-house / PSS-embedded (Outpayce XPP)** — the lowest band, correctly. Hardest incumbency: bundled with the PSS, no contract to displace |
| 3+ countries | **3** | ✅ Five countries above 1% traffic (PH 57.46, US 16.75, CA 5.51, AU 4.67, JP 2.19); NDC selling live in nine markets |
| Multiple PSPs | **3** | ✅ **Outpayce XPP** and **PayPal** both confirmed first-party and independently. ⚠️ The card acquirer behind XPP is **unknown** |
| Local rail / licensing gap in a top-3 market | **0** | ⬜ **Scored 0 deliberately, against temptation.** Top-3 are PH, US, CA. The Philippines is **well covered**: GCash (May 2021), QR Ph (May 2025), Dragonpay, Billease, GrabPay and 0% instalments are all live and first-party confirmed. The genuine absences — **Maya** on the main flow, **Interac** in Canada, **Google Pay** everywhere — are real and sourced, but none is *the* dominant rail of a top-3 market in the way the matrix means. **The big rail gaps (QRIS/Indonesia, UPI/India) are in markets outside the top 3**, so they cannot score here |
| Recent expansion | **2** | ✅ **NDC launch 19 Jun 2025 across nine markets** (fetched); Manila–Chicago 9 Nov 2026; Manila–Palau 29 Mar 2026 |
| Payment issues | **2** | ✅ **Moderate, current and geographically spread.** Trustpilot **1.5/5 over 539 reviews**; 6 payment-adjacent on one recency page dated **Sep–Oct 2026** from UAE, Saudi, US, Netherlands, Australia, PH. Pattern is **refund settlement latency**, plus one double-billing at check-in |
| Funding >$10M | **0** | ❌ No round. Listed carrier; H1 2026 was a net loss |
| High traffic outside home | **2** | ⚠️ **Philippines 57.46%, under the 60% threshold.** ⚠️ **Softest row in the matrix** — it rests on a SimilarWeb free-tier estimate and clears by only 2.5 points. See the sensitivity note |
| Competitor using orchestration | **2** | ✅ **Cebu Pacific — the direct domestic rival — on CellPoint Digital** (our own `cebu-pacific.md`, case study fetched 27 Feb 2024). Also **Sun PhuQuoc Airways** on 2C2P/M-PAY "PACO", **March 2026** — new, not previously in the repo |
| Payment job postings | **0** | ❌ **Two independent agents searched; none found.** No careers host reached, so no title was taken from a snippet |

**Tier: ⭐ High Priority (17+). No analyst override applied.**

This is consistent with repo precedent: **`qantas.md` scored 19/29 ⭐ on the same PSS-embedded motion.** The
difficulty of the motion is carried in the motion note and the outreach constraints, not by suppressing the score.
I scored **0** on three rows where the evidence did not support a point, including the local-rail row where the
temptation was strongest.

> ⚠️ **Score sensitivity.** The "high traffic outside home" row (+2) rests on a SimilarWeb **estimate** showing the
> Philippines at 57.46% against a 60% threshold. **If Prateek supplies real SimilarWeb data and the home market comes
> in above 60%, this becomes 18/29 — still ⭐.** The tier is not sensitive; the score is.

### Monthly transaction count — MANDATORY DISCLOSURE

**Verdict: ✅ DERIVED — ≥100,000/month.** Band **+5**.

**Billing unit: a card-charged booking (one PNR = one charge), plus separately-charged ancillaries.** These are not
the same as passengers, and the error runs in both directions — stated explicitly below.

**Sourced input, verified by me** (portcalls, published 1 Apr 2026; HTTP 200 at 30,760 B against a 404 control at
21,452 B; `16.3 million` 2/0, `301.2` 1/0, `3.22 billion` 2/0):
> *"PAL carried 16.3 million passengers during the year, a 4.3% increase from 2024"* · *"Ancillary revenues likewise
> rose 24.9% year-on-year to **$301.2 million** mainly due to higher volumes of **seat upgrades**. Ancillary revenues
> now represent 9.4% of PAL's total revenues."*

**Primary arithmetic:** 16,300,000 ÷ 12 = **1,358,333 passengers/month** `[DERIVED — sourced figure + calendar]`.

**Two conversions are ASSUMED and I am not dressing them up:** passengers-per-booking (no source exists) and the
direct-vs-agency split (no PAL figure exists; Euromonitor paywalls it). Both push the number **down**: one card
charge can cover a family on one PNR, and GDS/OTA tickets are acquired by the agent or settled through ARC/BSP, not
by PAL. PAL's own statement that its NDC platform *"will operate alongside the existing GDS"* confirms indirect
volume remains material.

**So I tested the conclusion rather than asserting a point estimate.** Even at an extreme **4 passengers per
booking**, PAL generates **339,583 bookings/month**; the gate fails only if PAL's direct share is **below ~11.8%**.

**The independent floor is what makes this DERIVED rather than ASSUMED.** Ancillaries — PAL's own disclosure says
these are *mainly seat upgrades* — are sold post-booking in PAL's own channels, so they are **disproportionately
PAL-acquired even on agency-sold tickets**:

> $301,200,000 ÷ 12 = **$25.1m of ancillary revenue per month**.
> For ancillary transactions *alone* to fall below 40,000/month, the **average ancillary charge would have to exceed
> $627**. For seat upgrades and baggage, that is not a plausible number.
> At a $150 average: **167,000/month**. At $50: **502,000/month**. Both clear the gate by more than 4×.

**Conclusion: the gate passes on every plausible assumption set and fails only on a compound implausible corner.**
The ancillary line is also growing **8× faster than total revenue** (24.9% vs 3.0%), so the transaction count is
rising faster than the top line.

⚠️ **Open:** the direct-vs-agency split is the single most valuable missing number on this account, and it is a
discovery question, not a research failure.

### Source Notes
- ✅ **Verified by me, control-tested:** Outpayce XPP + CFO quote; PAL FY2025 financials and ancillary line; PAL's
  11 PayPal currencies; PAL's offline-payment partner lists; PAL's 0% instalment programme and channel split;
  the AEM/Angular shell; the DNS wildcard; the Imperva wall on `booking.`
- ⚠️ **Agent-sourced, page-fetched:** NDC launch (19 Jun 2025); Trustpilot corpus; iOS app listing; Datalex 2016;
  Amadeus Altéa; FX Box.
- ⚠️ **Search-summary only — do not quote:** all H1/Q1/Q2 2026 financials; PAL Holdings ownership percentages;
  Singapore UEN; the Australia GSA model; CARE-equivalent credit events; all leadership titles except Justin Warby's.

### Success Case Alternatives
- **An APAC carrier with a diaspora-weighted book** — the match is the OFW corridor and multi-currency reach, not
  airline-ness in general.
- ⚠️ **Do not use Cebu Pacific as a proof point.** It is the rival, it is on a competitor's platform, and the case
  study contains no numbers.

---

## Section 1: Website Traffic Analysis by Country

**Data source: WebSearch/WebFetch fallback — SimilarWeb free tier. No data was supplied for this account and no
SimilarWeb MCP tool exists in this environment. Everything here is `[ESTIMATE, not confirmed]`.**

| Rank | Country | Traffic Share | Est. Monthly Visits | Source |
|------|---------|---------------|---------------------|--------|
| 1 | 🇵🇭 Philippines | **57.46%** | — | SimilarWeb, Sept 2026 `[ESTIMATE]` |
| 2 | 🇺🇸 United States | **16.75%** | — | as above |
| 3 | 🇨🇦 Canada | 5.51% | — | as above |
| 4 | 🇦🇺 Australia | 4.67% | — | as above |
| 5 | 🇯🇵 Japan | 2.19% | — | as above |
| — | Others | 13.42% | — | as above |

Global rank **#10,720**; bounce **30.02%**; pages/visit **6.36**; avg visit **00:05:26**. Total visits **3.8M**
⚠️ shown under a *"Total Visits Last 3 Months"* heading, so it may not be a monthly figure.

⚠️ **Column ambiguity, resolved by arithmetic not by a label.** The SimilarWeb page renders **two unlabelled numeric
columns** per country. I re-fetched it myself to settle which is traffic share: **column 1 sums to exactly 100.00%
once "Others" is included**, so column 1 is the share. The second column (PH 11.89, US 19.31, CA 6.18, AU 3.17,
JP 9.77) sums to 50.32% across five rows and **remains unidentified**. Had column 2 been the share, the US would
outrank the Philippines and the entire profile would change.

⚠️ **Vendor disagreement, unreconciled:** SimilarWeb 3.8M (Sep 2026) vs Semrush 2.81M (Oct, likely 2025) vs Semrush
1.96M (June, year unknown) — roughly a 2× spread. `[UNVERIFIED — search summary only]`

**Only five countries plus "Others" are exposed on the free tier. There is no top-10 split.** Four markets exceed 5%;
the Philippines is the only one above 5% with a confirmed entity.

> **MANUAL:** This is the single highest-value gap on the account. A supplied SimilarWeb pull would firm up the
> country profile, the APM gap analysis and two ICP rows.

## Section 2: Legal Entities & Local Presence

**Headquarters:** Pasay City, Philippines. **PAL Holdings, Inc.** is the PSE-listed vehicle (ticker **PAL**);
**Philippine Airlines, Inc.** is the operating carrier and the contracting entity in the General Conditions of
Carriage, which define *"PAL" means Philippine Airlines, Inc.*

| Country | Entity | Reg. # | Source |
|---------|--------|--------|--------|
| Philippines | PAL Holdings, Inc. | SEC **PW-94** | 17-A FY2022 `[UNVERIFIED]` |
| Philippines | Philippine Airlines, Inc. | **Not found** | — |
| Philippines | Air Philippines Corporation (PAL Express) | — | `[UNVERIFIED]` |
| Singapore | PHILIPPINE AIR LINES, INC. (branch) | UEN **S70FC1978G** | ACRA aggregator `[UNVERIFIED]` |
| **South Korea** | **Philippine Airlines, Inc. (Korea)** | **Biz Reg. 516-84-00029** | ⭐ **PAL's own `/kr/ko/` footer — verified first-party** |

**Cross-Border Gap Analysis**

| Country | Top-5 traffic? | Local entity? | Domestic acquiring gated? | Cross-border risk |
|---|---|---|---|---|
| Philippines | ✅ #1 | ✅ HQ | No | Low |
| United States | ✅ #2 | ❌ not found | No | ⚠️ Moderate |
| Canada | ✅ #3 | ❌ not found | No | ⚠️ Moderate |
| Australia | ✅ #4 | ❌ **GSA model** | No | ⚠️ Moderate |
| Japan | ✅ #5 | ❌ not found | No | ⚠️ Moderate |

> *"Warning: Potential cross-border operation in the United States, Canada, Australia and Japan — no local entity
> found. Transactions may be processed cross-border, with higher scheme costs, lower approval rates and FX
> exposure."*

⚠️ **This warning is weaker than it looks and I am flagging that deliberately.** Absence of a registry hit is **not**
evidence of absence — no annual-report branch schedule was reachable. More importantly, **Outpayce FX Box gives PAL
multi-currency pricing with settlement in its currency of choice**, which blunts the standard FX argument. Do not
lead on cross-border cost here.

⭐ **The Australia finding is the one worth pursuing.** PAL reportedly *"is now conducting all of its Australian
operations through its long-time General Sales Agent, **Rakso Australia Pty Limited**"*, having closed its Sydney
regional office `[UNVERIFIED — undated trade article]`. **If the GSA model generalises beyond Australia, PAL's
overseas selling sits with agents whose acquiring is not PAL's** — which would materially reduce PAL-acquired volume
outside the Philippines. **Unresolved, and the highest-value open question on the account.**

⭐ **Korea is the worked example that the entity gate is real — and that PAL clears it when it wants to.** PAL's
Korean site footer discloses a **Business Registration Number** and a **Value-Added Telecommunications Business
Registration Number** — precisely what local Korean card-PG acceptance requires. **Korean Local Cards (Shinhan,
Samsung, Hyundai, KB Kookmin, Lotte, Hana, Woori, BC) went live 26 May 2026.** Entity first, then the local rail.
That is a template Prateek can point at: it shows PAL already understands the local-presence → local-acceptance
chain, and raises the obvious question of which market is next.

⚠️ **Unresolved ownership conflicts — do not state a number:** PAL Holdings' stake in the airline is reported as
**81.57%** (17-A FY2022) and **98.3%** (TTG 2014). Lucio Tan Group aggregate is **71.25%** from a 31 Dec 2024 PSE
disclosure (Buona Sorte 37.99% + Trustmark 33.26%) against a 2021 Chapter 11 projection of **89.45%**.

**Chapter 11:** filed **3 Sep 2021** (SDNY), plan approved **17 Dec 2021**, exited **31 Dec 2021**; ~$2bn debt
reduction, $505m from the majority shareholder. ⚠️ **PAL Holdings and PAL Express were NOT debtors** — only
Philippine Airlines, Inc. All `[UNVERIFIED — search summary only]`.

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Region | Provider | Evidence Type | Source |
|---|---|---|---|
| Global | **Outpayce XPP (Amadeus)** — orchestration + acceptance | `[Press Release]` **verified by me** | outpayce.com newsroom, 5 Sep 2024 |
| Website, 11 currencies | **PayPal** | `[PAL's own FAQ]` **verified by me** | `/ph/en/faq/paypal` via AEM model API |
| Philippines | **IATA Pay** (A2A via **QR Ph**) — PAL is the first carrier globally | `[Press Release]` **verified by me** | same Outpayce page |
| International | **Amadeus FX Box** multi-currency pricing — PAL first carrier | `[Third-Party Report]` | thepaypers.com, 25 Aug 2021 |
| PH online banking (hotline bookings) | BDO, BPI, Chinabank, **GCash**, Landbank, Maybank, Metrobank, RCBC, Robinsons, Unionbank | `[PAL's own FAQ]` **verified by me** | `/ph/en/faq/offline-payments` |
| PH + US cash OTC | 7-Eleven/ECPay, Bayad Center, Cebuana Lhuillier, M Lhuillier, Palawan, LBC, RD Pawnshop, Robinsons, AUB, BDO, PNB, UnionBank, Security Bank, UCPB, EastWest, Metrobank, RCBC, Chinabank, RuralNet, One Network Bank; **PNB Global Remit (USA)** | `[PAL's own FAQ]` **verified by me** | same |
| PH instalments | **EastWest, UnionBank, HSBC, Metrobank, BPI** (web/app); **+ BDO, PNB, Chinabank** (ticket offices) | `[PAL's own FAQ]` **verified by me** | `/ph/en/faq/credit-card-installment-payment` |
| — | **Card acquirer / underlying PSP** | ❌ **NOT ESTABLISHED** | Searched against Adyen, Stripe, Worldpay, Checkout.com, Cybersource, Braintree, Ingenico, 2C2P, Xendit, iPay88, Omise, Paynamics, Dragonpay, AsiaPay — **zero PAL hits** |

### 3B. Payment Orchestrator

**In-house / PSS-embedded — Outpayce XPP (Amadeus).**

> *"Confirmed orchestration-aware. The opening is coverage and international reach, not the case for orchestration
> itself."*

Evidence: Outpayce newsroom, 5 Sep 2024, verified by me with a 404 control — PAL named as the first carrier on IATA
Pay via XPP, CFO quoted on XPP's multi-method acceptance and partner access.

⚠️ **Scope is NOT established.** The release proves XPP is in production; it does **not** establish whether XPP covers
all channels (web, mobile, GDS/agency, airport, call centre) or only the IATA Pay A2A flow. Do not overstate it.
⚠️ Nothing publicly connects **FX Box (2021)** and **XPP (2024)** architecturally.

## Section 4: Alternative & Local Payment Methods

**All CONFIRMED rows below are first-party**, from PAL's AEM content API (`.model.json`), control-tested against a
404 nonsense path. The master list is `/ph/en/faq/online-booking`.

⭐ **Structural finding: PAL does not gate payment methods by market site — it gates them by the itinerary's quoted
currency.** The `/ph/`, `/us/`, `/jp/ja/`, `/au/`, `/ae/`, `/sa/`, `/qa/`, `/sg/`, `/hk/`, `/ca/`, `/gb/`, `/kr/ko/`
and `/tw/` variants all serve **identical payment text**; only the `<title>`, breadcrumb and legal footer differ.
So the table below is currency-keyed, mapped to market.

**Core statement, verbatim:** *"We accept Cash and Credit/Debit Cards (Mastercard/Visa/JCB/American Express, UATP,
Diners Club and Discover) and PayPal."*
**3DS, verbatim:** *"PAL Website is enrolled to the 3D Secure Service for MasterCard (Mastercard SecureCode), Visa
(Verified by Visa), JCB (J/Secure) and American Express (American Express SafeKey)."*

| Market | Method | Category | Status | Effective |
|---|---|---|---|---|
| 🇵🇭 PH | **GCash** | Wallet | ✅ **Active** | 11 May 2021 |
| 🇵🇭 PH | **QR Ph** | A2A / national QR | ✅ **Active** | 16 May 2025 |
| 🇵🇭 PH | **Dragonpay** | Aggregator (bank/OTC) | ✅ Active | 20 May 2021 |
| 🇵🇭 PH | **Billease** | BNPL | ✅ Active | 21 Sep 2021 |
| 🇵🇭 PH | 0% instalments, ≥₱20,000, up to 6 months | Instalments | ✅ Active — **web/app domestic only** | — |
| 🇵🇭 PH | 22+ OTC cash partners (7-11/ECPay, Bayad, Cebuana, M Lhuillier, Palawan, LBC…) | Cash | ✅ Active — **cash only, no cards** | — |
| 🇵🇭 PH | **Maya / PayMaya** | Wallet | ⚠️ **Travel Credits top-up ONLY — absent from the main booking flow** | — |
| 🇵🇭 PH | BancNet · InstaPay · PESONet | Debit / A2A | ❌ **Not found** | — |
| 🇸🇬 SG | **PayNow** | A2A | ✅ Active | **18 Mar 2026** |
| 🇹🇭 TH | **PromptPay** | A2A | ✅ Active | 10 Sep 2024 |
| 🇲🇾 MY | **DuitNow** · **Financial Process Exchange (FPX)** | A2A | ✅ Active | 10 Sep 2024 · 13 Jul 2021 |
| 🇭🇰 HK | **Faster Payment System (FPS)** | A2A | ✅ Active | 13 Nov 2024 |
| 🇻🇳 VN | **VietQR** | A2A | ✅ Active | 13 Nov 2024 |
| 🇮🇩 **ID** | **QRIS** · GoPay · OVO · DANA | A2A / wallet | ❌ **NOT FOUND — the one hole in the ASEAN sweep** | — |
| 🇮🇳 **IN** | **UPI** · RuPay · netbanking | A2A / cards | ❌ **NOT FOUND.** INR appears only in the UnionPay list | — |
| 🇰🇷 KR | **Korean Local Cards** — Shinhan, Samsung, Hyundai, KB Kookmin, Lotte, Hana, Woori, BC | Cards | ✅ Active | **26 May 2026** |
| 🌏 Global | **Apple Pay** | Wallet | ✅ **Active — no currency restriction stated** | **2 Oct 2026** |
| 🌏 Global | **Google Pay** | Wallet | ❌ **NOT FOUND in any market** | — |
| 🌏 Global | PayPal (PHP, USD, AUD, CAD, GBP, HKD, JPY, NZD, SGD, THB, TWD) | Wallet | ✅ Active | base |
| 🌏 Multi | Alipay · WeChat Pay · UnionPay | Wallet / cards | ✅ Active | May 2021 · May 2021 · Sep 2021 |
| 🇯🇵 JP | **konbini** · PayPay · Rakuten Pay · au PAY | Cash / wallet | ❌ **Not found** | — |
| 🇦🇺 AU | **PayTo** · **BPAY** · Afterpay · Zip | A2A / BNPL | ❌ **Not found** | — |
| 🇨🇦 CA | **Interac** | Debit / A2A | ❌ **Not found** | — |
| 🇭🇰 HK | Octopus | Wallet | ❌ Not found | — |
| 🇹🇼 TW | JKOPay · LINE Pay; Alipay/WeChat for TWD | Wallet | ❌ Not found | — |
| 🇸🇦 SA · 🇶🇦 QA | **SAR / QAR pricing** · **mada** | Currency / cards | ❌ **NOT FOUND** — `mada` returns 0 | — |

**Quoting currencies — 19, confirmed first-party:** PHP, USD, AUD, CAD, GBP, HKD, JPY, NZD, SGD, CNY, MYR, **AED**,
KRW, MOP, IDR, THB, TWD, INR, VND. **No SAR. No QAR. No EUR.**

> *"Warning: In Indonesia, QRIS is the mandated national QR standard and GoPay/OVO/DANA dominate, but none is
> supported by Philippine Airlines — while every neighbouring ASEAN instant rail has been shipped."*

> *"Warning: In India, UPI carries the dominant share of online payments and is a named IATA Pay rail, yet it is
> absent from PAL's method list despite PAL being the first carrier live on IATA Pay."*

⚠️ **False positives caught and excluded:** **`BPAY` matched twice — both inside "Gra*bPay*"**. Australia's BPAY is
genuinely **NOT FOUND**. `mada` returned zero hits with no `nomada`/`llamada` noise. `maya` matched only in genuine
payment context ("Pay maya") on the Travel Credits page.

⚠️ **A domestic quirk with real conversion impact.** International bookings originating in the Philippines are
quoted in **USD** at OTC centres, and *"Only select Payment Centers accept USD."* Paying in PHP for an international
booking is possible **only via the Reservations Hotline** — online, *"our bank partners offer foreign exchange
services to settle the international booking quoted in USD."* **A PHP-preferring customer buying an international
ticket online is pushed into a USD transaction or a phone call.**

⚠️ **The Reservations Hotline has a BROADER payment set than the website** — 11 online-banking partners (incl.
GCash) and 23 cash partners, and it is the only PHP route for international tickets. **The self-service channel is
the restricted one**, which is the same asymmetry as the instalment finding.

> **MANUAL:** This list is PAL's **published FAQ**, not an observed checkout. The live booking engine sits behind
> Imperva and could not be rendered. Verify the top 2–3 markets with a real booking attempt.

## Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Customer country | Source |
|---|---|---|---|---|---|
| Refund never received after cancellation | Trustpilot 1★ | Moderate | 9 Sep 2026 | **UAE** | trustpilot.com, fetched |
| Reimbursement delay >2 months | Trustpilot 1★ | Moderate | 10 Sep 2026 | **Saudi Arabia** | same |
| Refund escalation failed | Trustpilot 1★ | Moderate | 8 Oct 2026 | **US** | same |
| Refund refused outright | Trustpilot 1★ | Moderate | 14 Sep 2026 | **Netherlands** | same |
| **Double-billing at check-in** | Trustpilot 1★ | Isolated (1) | 4 Sep 2026 | **Philippines** | same |
| Unexpected gate fee charge | Trustpilot 2★ | Isolated (1) | 1 Oct 2026 | **Australia** | same |

**Trustpilot: 1.5/5 across 539 reviews.** Six payment-adjacent reviews on one recency page.

> *"Pattern of cross-border refund-settlement latency — UAE, Saudi, US, Netherlands, Australia — suggests a
> reconciliation and refund-routing opportunity, not an acceptance problem."*

⚠️ **Three honest corrections, all of which cut against the easy story:**
1. **There is no current cross-border decline pattern.** I specifically briefed an agent to hunt it. It found only
   undated, isolated material (a FlyerTalk post of unknown age; a resolved 2013 double-charge) and **declined to
   assert a pattern**. That was the right call and I am recording it rather than quietly dropping the question.
2. **A 1.5 TrustScore is mostly service, rebooking and cancellation — not payments.** Trustpilot self-selects for
   anger. Do not call this widespread.
3. **The 2025 Philippine regulator refund campaign targeted AirAsia, not PAL.** Do not let it be mis-attributed.

**iOS app** (`id1538570065`, seller Philippine Airlines, Inc., bundle paired before quoting): **3.3/5 from 2.3k
ratings** — visible reviews concern crashes and forced logins, **no payment complaints**. ⚠️ A search summary claimed
"2.2–2.3"; the fetched page says 3.3. **Do not quote app ratings from snippets.**
❌ **Google Play package never confirmed; zero Play review quotes, none invented.** ❌ **Reddit returned nothing
across two attempts** — record as no evidence either way, not as low complaint volume.

📌 **One structural item worth verifying:** PAL's refund policy reportedly excludes **split payments, bank-transfer
and cash bookings, award tickets and reissues** from self-service refunds `[UNVERIFIED]`. *"Split payments cannot be
self-service refunded"* is a genuine orchestration talking point **if** it can be confirmed.

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | **19 Jun 2025** | **Amadeus-powered NDC platform live** across US, CA, SG, HK, JP, AU, UAE, QA, SA. Justin Warby, VP Sales & Distribution, quoted. **Payments not mentioned.** | Platform / Distribution | aviationupdatesph, fetched |
| 2 | 17 Jun 2025 | **ARC Direct Connect** partnership — NDC transactions processed through ARC | Distribution | arccorp.com `[UNVERIFIED]` |
| 3 | 3 Jul 2025 / 4 Sep 2025 | **Travelfusion** partnership; **NDC live on Trip.com** | Distribution | `[UNVERIFIED]` |
| 4 | 9 Nov 2026 | **Manila–Chicago O'Hare** launch, 3x weekly A350-900, 8th US point | Market Expansion | `[UNVERIFIED]` |
| 5 | 29 Mar 2026 | **Manila–Koror (Palau)** launch, 2x weekly | Market Expansion | `[UNVERIFIED]` |

**No public payment-related RFP found. No payment job postings found** by two independent agents.

⚠️ **Financial trajectory — this contradicts the "recovering carrier" premise and must shape the pitch.**
All `[UNVERIFIED — search summary only]`: Q1 2026 net income +2.6% to $78.55m; **Q2 2026 net loss $103.6m** reversing
a $60.2m profit, fuel +88%; **H1 2026 net loss $25.1m** vs $136.7m profit a year earlier, revenue +5.9% to $1.74bn,
**passengers 8.2m, −3.1%**, cash $456.3m.

**Revenue up, volume down, margin destroyed by an input cost they cannot control.** That is precisely the condition
in which cost of acceptance and recovered failed payments become a CFO conversation. **Pitching expansion would be
factually wrong and they would know it.**

**Named leadership:**
| Name | Title | Confidence |
|---|---|---|
| **Justin Warby** | **VP for Sales and Distribution** | ✅ **Verified — fetched page, directly quoted** |
| **Anna Isabel Bengzon** | **Chief Finance Officer** | ✅ **Verified — quoted on the Outpayce release by me** |
| Richard Nuttall | President | ⚠️ snippet; corroborated in the portcalls tag line |
| Eric David Anderson | Chief Commercial Officer (SVP rank) | ⚠️ snippet |

❌ **No CIO, CDO, Chief Digital Officer, Head of E-commerce or Head of Payments is publicly identifiable.**

## Section 7: Payment-Specific News

| # | Date | Headline | Relevance | Source |
|---|---|---|---|---|
| 1 | **5 Sep 2024** | **PAL first carrier to implement IATA Pay via Outpayce XPP** | ⭐ Establishes the motion | outpayce.com, **verified by me** |
| 2 | 25 Aug 2021 | PAL first carrier on **Amadeus FX Box** multi-currency pricing | Multi-currency incumbency | thepaypers.com |
| 3 | 2025 | PAL × **Maya** on Mabuhay Miles (earn/redeem) | ⚠️ **Loyalty, not checkout acceptance** | `[UNVERIFIED]` |
| 4 | May 2021 | PAL accepting **GCash and PayMaya** — cargo, ticket office, airport counters | ⚠️ **Offline channels only** | `[UNVERIFIED]` |
| 5 | 9 Feb 2016 | **Datalex** reselected as digital commerce partner, 5-year term | ⚠️ **Term lapsed ~2021, no renewal found** | datalex.com, fetched |

⭐ **PAL publishes its own payments changelog, and it is the best news source on this account.** From the dated
rollout log in `/ph/en/faq/online-booking` (verified by me): **Apple Pay 2 Oct 2026**, **Korean Local Cards 26 May
2026**, **PayNow 18 Mar 2026**, **QR Ph 16 May 2025**, **VietQR + FPS 13 Nov 2024**, **PromptPay + DuitNow 10 Sep
2024**. **Three launches in 2026 alone, the most recent 17 days before this research.** Re-read that page before any
outreach — it will have moved.

**No provider-removal event found. No checkout redesign found.**

## Section 8: Checkout Experience Audit

⛔ **Not completable in this environment — and the reason is itself a finding.**

| Dimension | Finding |
|---|---|
| Marketing site | **Adobe AEM + Angular SPA.** Homepage **2,399 B** vs 404 control **2,392 B** — a shell with `<div id="spa-root">`. Every valid route returns the same ~2.4 KB shell with a different `<title>` |
| Booking engine | **`booking.philippineairlines.com`** — `/booking` returns **200 at 6,183 B**, which is an **Imperva "Pardon Our Interruption" bot challenge** (`reeseSkipExpirationCheck`, `initializeProtection`, `ds.tl`). 404 control = **58 B**, *"Application described by provided parameters not found"* |
| WAF | **Imperva** confirmed on `booking.` (`x-cdn: Imperva`, `x-iinfo`) |
| API layer | **`api.philippineairlines.com`** = **AWS API Gateway** (`x-amzn-requestid`, `ForbiddenException`), 403 without auth |
| Front-end library | **`ngx-amd`** — a **private** Angular component library: 133 distinct translation keys spanning flight-search, booking-cart, **abandon-cart**, resume-booking, manage-booking, check-in, flight-upgrade, donate-miles. **Not on npm** |
| Instalments | ✅ Present — **web/app domestic only**, international only via **pay-by-link** at contact centre / ticket office |
| Multi-currency | ✅ 11 PayPal currencies; FX Box for card pricing |
| 3DS | ❌ Not established |

**I did not attempt to defeat the Imperva challenge.** A full checkout walkthrough requires a live booking from a
foreign IP and is a manual task.

⭐ **Method note for future runs on this site.** The SPA shell is bypassable: **AEM exposes page content at
`.model.json`**. `https://www.philippineairlines.com/ph/en/home.model.json` returns **200 / 81,681 B** against a
nonsense path at **404 / 2,392 B HTML**. That is how every first-party PAL quotation in this file was obtained.
Content root is `/content/palportal/{country}/{lang}/home`.

⚠️ **Three traps recorded for the next analyst:**
1. **DNS wildcard on `*.philippineairlines.com`** — my nonsense subdomain resolved to 216.21.224.199. **Resolution is
   not existence.** This killed a promising lead: an agent reported `prod-cm.philippineairlines.com` as a reachable
   content host; **I tested it and it is the wildcard IP and fails to connect**, identical to my control.
2. **AEM clientlib URLs ignore the content hash.** `clientlib-angular.min.ZZZNONSENSECONTROL.js` returned
   **byte-identical** content (432,013 B, same MD5) to the real bundle. **That control is void.**
3. **`altea` is a FALSE POSITIVE for Amadeus Altéa.** Both hits in the Angular bundle are inside
   `initi**alTea**rdown` (RxJS). I nearly reported a PSS from it. ⭐ **New entry for the false-positive list.**

## Section 9: PCI DSS Compliance

*"No direct PCI compliance documentation found publicly for Philippine Airlines."* No statement, certification or
disclosure exists. No 3DS evidence either way. No fraud/chargeback vendor identified.

`[INFERENCE, not confirmed]`: given PAL runs Outpayce XPP, its card vault plausibly sits with Outpayce — the
Qantas/Amadeus pattern. **No source states this.** Note that Riskified has a published partnership with Outpayce for
airline chargeback guarantee — **this says nothing about PAL** and must not be reported as a PAL relationship.

## Section 10: Strategic Insights & Outreach Angles

> **Insight #1: The ASEAN instant-rail sweep has exactly one hole**
> **Evidence:** §4 (PromptPay/TH, DuitNow/MY, FPS/HK, VietQR/VN, QR Ph/PH, PayNow/SG all shipped 2024–2026, each
> with a published effective date — **QRIS/Indonesia returns 0**) + §7 (PAL is the world's first carrier on IATA
> Pay, a rail family whose own named markets include India/UPI).
> **Pain Point:** a systematic, funded regional rollout with a visible gap in the largest ASEAN economy. Every
> neighbour's rail is live; Indonesia's customers reach only generic online banking and UnionPay.
> **Yuno Value:** QRIS and the Indonesian wallet set added through the same single integration, without another
> per-rail project.
> **Outreach Angle:** *"You've shipped PromptPay, DuitNow, FPS, VietQR, QR Ph and PayNow in two years. Indonesia
> looks like the one that's still open — is that sequencing or something harder?"*
> **Suggested Subject Line:** Six instant rails, one gap

> **Insight #2: Apple Pay shipped 17 days ago. Google Pay isn't anywhere.**
> **Evidence:** §4 (Apple Pay effective **2 Oct 2026**, no currency restriction; `Google Pay` returns **0** across
> the entire first-party corpus, every market) + §1 (US 16.75%, Canada 5.51%, Australia 4.67% of traffic, plus an
> Android-dominant APAC base).
> **Pain Point:** one wallet is on the checkout and the other is not, in markets where the missing one carries the
> larger handset share.
> **Yuno Value:** wallet parity without a separate integration per wallet per market.
> **Outreach Angle:** *"Apple Pay went live at the start of the month. Is Google Pay on the same roadmap, or is
> something blocking it?"*
> **Suggested Subject Line:** Apple Pay live, Google Pay missing

> **Insight #3: The self-service channel is the restricted one — twice over**
> **Evidence:** §4 (0% instalments: web/app **domestic only**, but contact centre and ticket office get **domestic
> and international** via pay-by-link; the Reservations Hotline carries **11 online-banking partners and 23 cash
> partners** and is the **only** PHP route for an international ticket) + §1 (US + Canada + Australia + Japan ≈ 29%
> of traffic).
> **Pain Point:** the cheapest, highest-intent channel offers the weakest payment options, and an overseas customer
> is pushed to a phone call or into USD. This is an asymmetry **inside PAL's own stack** — both halves are their own
> published documents, so neither can be disputed.
> **Yuno Value:** method and instalment parity across web, app and agent channels from one integration.
> **Outreach Angle:** *"Your phone agents can offer an international customer an instalment plan your website
> can't — and they're the only route to paying in pesos for an international ticket."*
> **Suggested Subject Line:** Instalments by phone, not on web

> **Insight #4: Distribution reach ran ahead of acceptance reach in the Gulf**
> **Evidence:** §6 (NDC platform live **19 June 2025**, rollout explicitly naming **UAE, Qatar and Saudi Arabia**,
> with **no mention of payments anywhere in the launch**) + §4 (**no SAR, no QAR** among 19 quoting currencies;
> **`mada` returns 0**; for an AED itinerary the only non-card alternative is UnionPay).
> **Pain Point:** PAL built selling capability in three Gulf markets with large overseas-Filipino populations, and
> local payment capability followed in only one of them.
> **Yuno Value:** local currency and local rail per corridor, on the acceptance side the NDC programme did not cover.
> **Outreach Angle:** *"Your NDC rollout named Saudi and Qatar as launch markets. Neither prices in local currency —
> was the payment side a later phase?"*
> **Suggested Subject Line:** NDC in Saudi, no riyal

> **Insight #5: Korea proves the pattern — entity first, then the local rail**
> **Evidence:** §2 (PAL's Korean footer discloses **Business Registration Number 516-84-00029** and a VAT-telecom
> registration — verified first-party) + §4 (**Korean Local Cards live 26 May 2026**, eight issuers).
> **Pain Point:** none — this one is a credential, not a complaint. It shows PAL already runs the local-presence →
> local-acceptance playbook, which makes the Indonesia and India gaps a sequencing conversation rather than an
> education one.
> **Yuno Value:** reach into markets where standing up a local entity is not commercially worth it on its own.
> **Outreach Angle:** *"You did the entity work in Korea and local cards followed. Which market is next on that
> list?"*
> **Suggested Subject Line:** After Korea, which market

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. *"You've shipped PromptPay, DuitNow, FPS, VietQR, QR Ph and PayNow since 2024 — Indonesia looks like the one
   instant rail still open."*
2. *"Apple Pay went live on your checkout on 2 October. Google Pay doesn't appear in any of your markets."*
3. *"Your contact centre can give an international customer a 0% instalment plan, and your website can only do that
   for domestic flights."*

**Cold call openers (conversational, one sentence each):**
1. *"I noticed PAL was the first airline in the world live on IATA Pay — are you extending that to the other markets
   it covers?"*
2. *"Your ancillary revenue grew 25% last year against 3% on the top line — is that running on the same payment path
   as the tickets?"*
3. *"You did the entity and registration work in Korea and local cards went live in May — is there a similar one in
   the pipeline?"*

## Section 11: Similar Companies & Prospecting Pipeline

### 11A. Direct Competitors

| Company | HQ | Overlap | Known PSP / Orchestrator | Source |
|---|---|---|---|---|
| **Cebu Pacific** | Philippines | Direct domestic rival | ⭐ **CellPoint Digital** — multi-acquirer dynamic routing, automated 3DS, instalments, DCC | Our `cebu-pacific.md` (11/29, Competitive) |
| AirAsia Philippines | Philippines | Domestic/regional | GCash + PayMaya acceptance — **not** orchestration | `[UNVERIFIED]` |
| Singapore Airlines / Scoot | Singapore | Regional/long-haul | **CellPoint Digital** (per our `cathay-pacific.md`) | Internal |
| Japan Airlines / ANA | Japan | PH–JP | None established | Our `japan-airlines-jal.md`, `ana-all-nippon-airways.md` |
| Cathay Pacific | Hong Kong | PH–HK | Adyen confirmed, no orchestrator | Our `cathay-pacific.md` (18/29 ⭐) |

### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator | Date | Source |
|---|---|---|---|
| **Sun PhuQuoc Airways** (Vietnam) | **"PACO" via M-PAY, 2C2P technical services** — dynamic routing, single API | **March 2026** | 2c2p.com `[UNVERIFIED]` — ⭐ **new, not previously in the repo** |
| Cebu Pacific | CellPoint Digital | Sept 2020 → Nov 2021 | Internal |
| Riyadh Air | CellPoint Digital | pre-2025 | Our `riyadh-air.md` |

⚠️ **Vendor-claim warning:** every CellPoint source is vendor-produced or vendor-echoed. The Cebu Pacific case study
contains **no acceptance uplift, no cost saving and no named acquirer**. **Do not quote a percentage — there isn't one.**
⚠️ **No CellPoint–Cebu Pacific coverage exists in 2025 or 2026.** Adoption is confirmed; **2026 currency is not.**

### Top Prospect Pipeline — genuine finds not on the TAL

| Company | Type | Why | In TAL? |
|---|---|---|---|
| **Sun PhuQuoc Airways** | Vietnam carrier | Just adopted orchestration via 2C2P/M-PAY (Mar 2026) — competitive intel | ❌ **No — genuine find** |
| **Rakso Australia Pty Ltd** | PAL's Australian GSA | If GSAs hold acquiring for PAL's overseas markets, the GSA is a payment decision-maker | ❌ No |

## Section 12: Business Case Data

| Metric | Value | Source |
|---|---|---|
| Annual Revenue | **$3.22bn** (CY2025, +3.0%) | portcalls, **verified by me** |
| Passenger revenue | **$2.73bn** | same |
| **Ancillary revenue** | **$301.2m (+24.9%), 9.4% of total** | same |
| Cargo revenue | $165.0m | same |
| Net income | **$160.4m (+6.1%)** | same |
| **Passengers carried** | **16.3 million (+4.3%)** | same |
| Load factor | 78.7% (from 79.1%) | same |
| Revenue per passenger | **~$167.5** ($2.73bn ÷ 16.3m) `[DERIVED]` | arithmetic |
| Ancillary per passenger | **~$18.48** `[DERIVED]` | arithmetic |
| **Monthly transaction count** | ✅ **DERIVED — ≥100,000/month.** Billing unit: card-charged booking (PNR) + separately-charged ancillaries. See the mandatory disclosure | portcalls + arithmetic |
| Primary currency | **19 quoting currencies** via Amadeus FX Box (PHP, USD, AUD, CAD, GBP, HKD, JPY, NZD, SGD, CNY, MYR, AED, KRW, MOP, IDR, THB, TWD, INR, VND). **No SAR, QAR or EUR.** PayPal covers 11 of the 19 | PAL FAQ, verified |
| Top 3 markets by traffic | Philippines, United States, Canada | SimilarWeb `[ESTIMATE]` |
| Billing channel split | ❌ **Direct vs agency/GDS — NOT FOUND.** Euromonitor paywalls it | — |

---

### Overall Research Confidence

**Medium-High.**

**Strong:** the orchestration finding (verified by me with a CFO quote and a 404 control); **PAL's complete payment
method set, its 19 quoting currencies and its dated rollout log** — all obtained first-party via the AEM content API
and control-tested, which makes Section 4 unusually reliable and makes every "NOT FOUND" a *sourced* absence from an
exhaustive corpus rather than a failed search; FY2025 financials (verified against a control); the volume gate
(sourced input plus a bounding argument); the **Korean entity** (PAL's own footer); and competitor orchestration
(internal + external corroboration).

**Weak:** **traffic is the biggest gap.** No SimilarWeb data was supplied; the free-tier fallback exposes only five
countries, carries an unlabelled-column ambiguity I could only resolve by arithmetic, and disagrees ~2× with Semrush.
**The country profile, the APM gap analysis and two ICP rows all rest on it.** Overseas entities are near-unevidenced.
All 2026 financials are snippet-derived. **Section 8 could not be completed** — Imperva blocks the booking engine.

### Manual Research Recommendations

> **Area:** Traffic. **Why:** drives the country profile, the APM analysis and two ICP rows; the home-market row
> clears its threshold by only 2.5 points on an estimate. **Action:** supply a SimilarWeb pull for
> `philippineairlines.com`.

> **Area:** Whether the published FAQ matches the live checkout. **Why:** every method in this file comes from PAL's
> **published FAQ**, not an observed checkout — the live booking engine sits behind Imperva and was never rendered.
> The real checkout may offer more or fewer methods. **Action:** a live booking attempt from a PH, US and Gulf IP.

> **Area:** Direct vs agency distribution split. **Why:** the single largest swing factor on PAL-acquired volume.
> **Action:** discovery question — *"what share of tickets sells through your own channels?"*

> **Area:** Whether the Australia GSA model generalises. **Why:** if PAL's overseas selling sits with GSAs, the
> acquiring may not be PAL's at all. **Action:** discovery question.

> **Area:** Is Datalex still the platform incumbent? **Why:** the 2016 five-year term lapsed ~2021 and the 2025
> Amadeus NDC build muddies it. **Action:** do not name Datalex in outreach until confirmed.

### Appendix: Key Source URLs

- Outpayce / IATA Pay / XPP (**verified**): `https://outpayce.com/en/resources/news/iata-and-outpayce-help-airlines-accept-account-to-account-payments`
- PAL FY2025 results (**verified**): `https://portcalls.com/pal-income-rises-6-1-in-2025/`
- PAL PayPal FAQ (**verified**): `https://www.philippineairlines.com/ph/en/faq/paypal`
- PAL Offline Payments FAQ (**verified**): `https://www.philippineairlines.com/ph/en/faq/offline-payments`
- PAL 0% Instalment FAQ (**verified**): `https://www.philippineairlines.com/ph/en/faq/credit-card-installment-payment`
- NDC launch: `https://aviationupdatesph.com/2025/06/pal-modernizes-booking-system-with-new-ndc-technology`
- Amadeus FX Box: `https://thepaypers.com/payments/news/philippine-airlines-selects-amadeus-for-payment-solutions`
- Datalex: `https://www.datalex.com/news/philippine-airlines-leads-with-datalex-digital-commerce/`
- Trustpilot: `https://www.trustpilot.com/review/philippineairlines.com?sort=recency`
- PAL iOS app: `https://apps.apple.com/ph/app/philippine-airlines/id1538570065`
- SimilarWeb `[ESTIMATE]`: `https://www.similarweb.com/website/philippineairlines.com/`

</details>
