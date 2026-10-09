# Langham Hospitality Group

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 14 / 29 → 🟢 **Medium** · **analyst override applied → 🔴 Low Priority** (reasoning in the ICP breakdown)
**Industry:** Hospitality & Lodging (luxury hotel operator) · **HQ:** Hong Kong · **Researched:** 2026-10-09 · **First email sent:** —
**Motion:** **Greenfield** — direct, per-property PSP integrations inside the SynXis booking engine. No orchestration layer anywhere. But greenfield in the literal sense: **28 of 33 properties cannot take an online payment at all.**

---

> ## 🔑 THE ONE FINDING THAT DECIDES THIS ACCOUNT
>
> **The card does not settle centrally. It mostly does not settle online at all.**
>
> I queried Langham's own live booking API for **all 33 properties in their CRS**. The availability
> response carries a `paymentGateway` field per hotel. Result:
>
> | `paymentGateway` | Properties | Markets |
> |---|---|---|
> | `cybersource` | 3 | The Langham Sydney, The Langham Melbourne, Cordis Auckland |
> | `adyen` | 2 | The Langham Gold Coast; Chelsea Hotel Toronto (`isLive: false`) |
> | **`""` (empty — no gateway)** | **28** | **Hong Kong ×5, Mainland China ×12, Indonesia ×1, Thailand ×1, USA ×4, UK ×1, + others** |
>
> Source (reproducible): `POST https://reservations.brilliantbylangham.com/api/booking/availability`
> with `{"hotelCode":"<synxisHotelId>","startDate":"2026-11-18","endDate":"2026-11-20","rooms":[{"adults":2,"children":0}]}`
> Hotel IDs from `POST https://reservations.brilliantbylangham.com/en-US/graphql` → `content.hotels(first:1000)`.
>
> And the booking engine's own code makes the consequence explicit. From
> [`pages/_app-661c61301c46b67b.js`](https://reservations.brilliantbylangham.com/_next/static/chunks/pages/_app-661c61301c46b67b.js),
> the function that decides whether money is taken at booking:
>
> ```js
> B=(e,t)=> !!t && !!e?.acceptedPaymentTypes?.includes(s.vZ.DIRECT_BILL)
>            && e?.offsetDropTime===s.$0.AFTER_BOOKING && !e?.offsetUnitMultiplier
> ```
>
> `t` is `paymentGateway`. **An empty `paymentGateway` makes an online charge impossible by construction.**
> ⚠️ **CORRECTED BY THE ORCHESTRATOR, 2026-10-09.** An earlier draft of this file claimed
> `acceptedPaymentTypes` returns `["DIRECT_BILL","CREDIT_CARD"]` **only** on ANZ and Toronto rates,
> with every Asian, US and UK rate returning `["CREDIT_CARD"]` alone. **That generalisation is wrong.**
> I re-queried the API myself: **The Langham Custom House Bangkok (hotel 99801, 15–17 Jan 2027) returns
> `["CREDIT_CARD","DIRECT_BILL"]` with `paymentGateway: ""`.** So `DIRECT_BILL` is NOT confined to
> markets that have a gateway.
>
> **The conclusion is unaffected, and the reason is in the code above:** the function requires
> `!!t` — a non-empty `paymentGateway` — *before* it ever looks at `acceptedPaymentTypes`. An empty
> gateway blocks the online charge regardless of what rate types are advertised. **Do not use the
> "DIRECT_BILL only exists where a gateway exists" framing in outreach; it is false and checkable.**
> Use the empty `paymentGateway` on its own.
>
> **So: Asia, the US and the UK take a card *guarantee* only. The money is collected by the property.**
> Langham's own rate terms say so in plain language — see the verbatim quotes in Section 4. The Hong Kong
> prepaid rate: *"The credit card is for guarantee purpose only. A secured payment link will be sent to you
> in a separate e-mail."* The Jakarta prepaid rate names a property mailbox:
> *"The reservation team will send a payment link … from our official reservation email at
> tljkt.reservation@langhamhotels.com."*
>
> **There is no central stack to orchestrate.** The orchestrable flow is three-and-a-bit ANZ hotels.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Langham Hospitality Group (trading name of **Langham Hotels International Limited**, Hong Kong) is the hotel operating and brand arm of **Great Eagle Holdings (HKEX: 0041)**. It runs **The Langham**, **Cordis**, **Eaton Workshop** and **Ying'nFlo** — **33 properties live in its CRS** across Greater China, Hong Kong, Indonesia, Thailand, Australia, New Zealand, the UK, the US and Canada. Great Eagle's **Hotels Division revenue was HK$5,307.1m in FY2025 (+4.4%)**, and **HK$2,570.8m in H1 2026 (+7.6%)**.

**SimilarWeb total visits (last full month, Sep 2026):** **374,332** on the booking domain `langhamhotels.com` (▼12.41% MoM) and **17,201** on the corporate domain `langhamhospitalitygroup.com` (▼11.36% MoM) — **source: SimilarWeb (supplied 2026-10-09)**. All country analysis below anchors on the **booking** domain, which is 22× larger and is where payment is attempted.

### Top 5 markets *(booking domain `langhamhotels.com`)*
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇺🇸 United States | **33.39%** (~125,000) | Visa, MC, Amex, Diners, Discover, UnionPay — **card guarantee only, no online charge** (4 properties, all `paymentGateway: ""`) | Online settlement itself; no wallet, no BNPL | ✅ 4 US properties operating |
| 2 | 🇦🇺 **Australia** | **24.08%** (~90,100) | Visa, MC, Amex, Diners, Discover, UnionPay — **the only market where money is actually taken at booking** (Cybersource ×2, Adyen ×1) | **No PayTo, BPAY, Afterpay or Zip — absence SOURCED** (see Section 4). ⚠️ Current merchant adoption of these rails **not established** — see Section 4 caveat | ✅ 3 AU properties operating |
| 3 | 🇬🇧 United Kingdom | **11.40%** (~42,700) | Cards only, guarantee only (`paymentGateway: ""`) | Online settlement; no wallet | ✅ The Langham, London |
| 4 | 🇮🇩 **Indonesia** | **10.79%** (~40,400) | Visa, MC, Amex, JCB, UnionPay. **No gateway.** Prepayment by **emailed payment link from a property mailbox** | **QRIS, virtual account, GoPay/OVO/DANA, Alfamart/Indomaret — ALL ABSENT, SOURCED.** Nothing but cards is configured | ⚠️ 1 managed property (**owned by Agung Sedayu Group**, not Langham) — no Langham Indonesian entity found ❌🔒 |
| 5 | 🇭🇰 **Hong Kong (HQ)** | **5.22%** (~19,500) | Visa, MC, Amex, JCB, UnionPay, Discover. **No gateway.** Prepaid rates settle by **emailed secured payment link** | **No FPS, no Octopus, no AlipayHK, no WeChat Pay HK — SOURCED ABSENT** | ✅ Langham Hotels International Ltd (HK) |

Also in the top 10: 🇨🇦 Canada 2.69% · 🇸🇬 **Singapore 1.58%** · 🇰🇷 **Korea 1.18%** · 🇮🇳 **India 0.88%** · 🇹🇭 **Thailand 0.80%**. **APAC visible: 44.53%.**
⚠️ **Singapore, Korea and India have traffic but NO Langham property at all** — those visitors are booking elsewhere in the portfolio, or not booking.

### Legal entities
- **Langham Hotels International Limited** (Hong Kong) — trades as Langham Hospitality Group; wholly-owned subsidiary of Great Eagle Holdings. Named as the Hotel Manager for the three Hong Kong hotels in LHI's trust portfolio. [Wikipedia](https://en.wikipedia.org/wiki/Langham_Hospitality_Group) · appears as the footer copyright on `langhamhospitalitygroup.com` ("© LANGHAM HOTELS INTERNATIONAL LIMITED… 沪ICP备09039361号")
- **Great Eagle Holdings Limited** (Hong Kong, **HKEX: 0041**) — listed parent. Hotels Division FY2025 revenue HK$5,307.1m. [2025 Annual Results Announcement](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0303/2026030302294.pdf)
- ⚠️ **Langham Hospitality Investments (HKEX: 1270) is NOT this company.** It is a separately listed stapled trust/Cayman company that **owns** three Hong Kong hotels (The Langham HK, Cordis HK, Eaton HK) and is **managed by** Langham Hotels International Ltd under contract. Do not cite 1270 figures as Langham Hospitality Group's. `[Great Eagle 2025 results, §4; and LHI structure per search summary — see Section 2]`
- **Registration numbers: not found.** No Hong Kong Companies Registry number, no Australian ACN, no Indonesian PT identified for any entity.

### Known PSPs
- **Cybersource (Visa)** — ✅ **CONFIRMED.** `paymentGateway: "cybersource"` returned by the live availability API for **The Langham Sydney (AUD)**, **The Langham Melbourne (AUD)** and **Cordis Auckland (NZD)**. Integration is **Cybersource Unified Checkout** — the checkout chunk decodes a `captureContext` JWT, loads `clientLibrary` with SRI from it and calls `window.Accept`, and the engine exposes `POST /payment/cybersource/verify`. `[Source Code]` `[Checkout]`
- **Adyen** — ✅ **CONFIRMED.** `paymentGateway: "adyen"` for **The Langham Gold Coast and Jewel Residences (AUD)** and **Chelsea Hotel Toronto (CAD, `isLive: false`)**. Integration is **Adyen Web Drop-in on the Sessions flow** — the bundle ships the Adyen Web SDK as chunk `3237` and mounts it with `{clientKey, environment, session, countryCode, amount, locale}`. `[Source Code]` `[Checkout]`
- **Sabre Hospitality / SynXis** — ✅ **CONFIRMED as the CRS and booking engine.** CSP on the booking host allowlists `*.synxis.com`, `*.sabrehospitality.com`, `*.asc.sabre.com`, `*.sabrecirrus.com`, `*.sabre-gcp.com`; hotel records key on `synxisHotelId`. The booking engine is a white-labelled SynXis Next.js app on `reservations.brilliantbylangham.com` behind Akamai. `[Source Code]`
- **Acquirers: NOT ESTABLISHED.** Cybersource and Adyen are gateways/processors. Who acquires the ANZ volume underneath them — and who acquires the 28 properties' offline card volume — is not publicly established. **I am not naming a guess.**

### Orchestration status
**None detected — direct PSP integrations only (greenfield).** The gateway is chosen per property by SynXis configuration and the client bundle loads each vendor's own SDK directly. No trace of Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY or Yuno in the booking engine source, the CSP, the GraphQL schema, Great Eagle's filings, or any public source.
⚠️ **Material caveat:** their CRS vendor sells an orchestrator. **Sabre launched "SynXis Pay" on 3 March 2025, with its "orchestration layer … powered by CellPoint Digital", claiming "over 250 alternative payment methods"** and Apple/Google Pay express checkout in the SynXis Booking Engine ([Travolution, 3 Mar 2025](https://www.travolution.com/news/travel-sectors/accommodation/sabre-hospitality-introduces-synxis-pay/)). **Langham is NOT on it** — raw `adyen`/`cybersource` gateway values and 28 properties with no gateway are inconsistent with SynXis Pay. But it is the path of least resistance for them and it is a competitor's product.

### Buying signals
- 🚀 **The Langham, Custom House, Bangkok — opening late 2026 and ALREADY TAKING BOOKINGS, with no payment capability.** I queried it myself: hotel `99801` returns live inventory in **THB**. ⚠️ **Inventory is sparse and date-sensitive** — on independent re-verification by the orchestrator (2026-10-09) `2027-01-15` returned HTTP 200 in THB, while `2026-11-18`, `2026-12-28` and `2027-02-18` all returned HTTP 404 `{"message":"Not available"}`. **Use 15 Jan 2027 to reproduce.** The 200 response carries with **`paymentGateway: ""`** and card types `Amex, UnionPay, Discover, Mastercard, Visa, Diner's Club` — **no PromptPay, no Thai bank transfer, no online charge.** A brand-new Thai property launching on a guarantee-only flow. [Langham's Bangkok page](https://www.langhamhotels.com/en/the-langham/bangkok) · [Sleeper Magazine](https://www.sleepermagazine.com/stories/projects/langham-to-open-bangkok-riverside-retreat/)
- 🚀 **Pipeline and footprint growing:** Ying'nFlo opened in **Hangzhou, Wuhan, Nanjing (Jul/Aug/Dec 2025) and Qingdao (late June 2026)**; third-party hotels under management rose from **14 (~4,200 rooms) at Dec-2025 to 15 (~4,400 rooms) at Jun-2026**. The Langham, Kuala Lumpur is reported on track for end-2027. [Great Eagle 2025 results](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0303/2026030302294.pdf) · [Great Eagle H1 2026 results](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0826/2026082601083.pdf)
- 💱 **A flat 2.50% card surcharge on every scheme at Cordis Auckland** — the only `transactionFees` entry in the whole 33-property CMS, applied identically to Visa, Mastercard, Amex, UnionPay, JCB, Diners and Discover. Cost of acceptance is being passed to the guest rather than optimised. (Source: their GraphQL `hotels { transactionFees { cardType percent } }`)
- 🤝 **Loyalty platform rebuild:** "Brilliant by Langham" refreshed in 2026 with AI personalisation and an expanded experiences platform, per [Business Traveller](https://www.businesstraveller.com/news/brilliant-by-langham-refreshed/) `[UNVERIFIED — search summary only, page returned HTTP 403 and was not fetched]`. **Points Plus Cash redemption is live** — their own FAQ: *"Eligible Reward Stays may be redeemed using a combination of Award Points and cash through a Points Plus Cash Stay"* ([Brilliant FAQ](https://www.brilliantbylangham.com/en/faq)). The cash leg of a Points Plus Cash booking in Hong Kong has no gateway to charge it.
- 📱 **A third booking channel I could not inspect:** *"You can only earn points from reservations booked via our website, app and **WeChat Mini-Program**"* ([Brilliant FAQ](https://www.brilliantbylangham.com/en/faq)). A WeChat Mini-Program almost certainly transacts on WeChat Pay — **but I could not reach or verify it, and I am not asserting its stack.**
- 📋 **No public payment-related RFP found.** 💼 **No payment-related job postings found.**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach langham-hospitality-group` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 14 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **0** | ⚠️ **NOT FOUND — ASSUMED.** See the mandatory disclosure below. The orchestrable unit (online card payments taken at booking) is **ANZ only** and is almost certainly **low single-digit thousands per month** — but that figure is **ASSUMED, so it does NOT fire the under-40,000 auto-reject** and it does not earn a band either. **Deliberate zero.** |
| Orchestration status | **+4** | ✅ **"None detected — direct PSP integrations only."** Adyen Web SDK and Cybersource Unified Checkout loaded directly by the booking engine; gateway selected per property by SynXis config; no orchestrator in source, CSP, filings or public record. Greenfield. |
| 3+ countries | **+3** | ✅ **Verified.** Booking domain: 10 countries ≥0.80% share, five above 5% (US 33.39, AU 24.08, UK 11.40, ID 10.79, HK 5.22). 33 properties across ~10 countries. SimilarWeb (supplied 2026-10-09) + their own CRS hotel list. |
| Multiple PSPs | **+3** | ✅ **Verified — two PSPs, both with primary evidence.** Cybersource (Sydney, Melbourne, Auckland) **and** Adyen (Gold Coast, Chelsea Toronto), from the live availability API. Note: this splits *within Australia* — two gateways for three AU hotels. |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **Deliberate zero.** Top-3 booking markets are **US, Australia, UK**. The *absence* of PayTo, BPAY, Afterpay and Zip in Australia **is sourced** (their CMS lists card schemes only). But the rule requires a **dominant** local rail, and **I could not find a current primary source for PayTo, BPAY or BNPL merchant adoption in Australian hotel booking** — see Section 4 caveat. I will not score a gap I cannot establish as dominant. **Indonesia (QRIS, VA, wallets — all sourced absent) would score this row outright, but Indonesia ranks #4, one place outside the top-3 test.** Flagging this loudly: this row is a 0 on a technicality, not on substance. |
| Recent expansion | **+2** | ✅ **Verified.** Ying'nFlo Qingdao opened late June 2026; managed portfolio 14→15 hotels (~4,200→~4,400 rooms) Dec-2025→Jun-2026; The Langham Custom House Bangkok bookable now for a late-2026 opening. Great Eagle FY2025 and H1 2026 results announcements. |
| Payment issues reported | **0** | ⬜ No moderate- or high-frequency payment complaints found on Reddit, Trustpilot, X or app stores. One isolated billing dispute at The Langham London (Venuescanner review, Mar 2026) — isolated, not a pattern. |
| Funding >$10M | **0** | ❌ Not applicable. Subsidiary of a listed parent (HKEX: 0041). No funding round. |
| High traffic outside home | **+2** | ✅ **Verified.** Home market Hong Kong is **5.22%** of booking-domain traffic — far below the 60% threshold. SimilarWeb (supplied 2026-10-09). |
| Competitor using orchestration | **0** | ⬜ Not confirmed. Mandarin Oriental runs **Datatrans + Stripe** (two PSPs, not an orchestrator). Sabre's SynXis Pay is CellPoint-powered, but that is a **vendor** product, not a named competitor hotel group confirmed to have adopted it. |
| Payment job postings | **0** | ⬜ None found. Searched LHG careers aggregators; only hotel operations and property-level accounting roles surfaced. |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **computed 14/29 = 🟢 Medium.**
**No public payment RFP was confirmed, so no RFP override applies.**

#### ⚖️ ANALYST OVERRIDE — tier moved DOWN to 🔴 Low Priority

Three of the override conditions in the method fire at once, and the reasoning is the deliverable here:

1. **Absolute volume too small for the thing Yuno would actually sell.** Orchestration can only touch payments that are taken online. **28 of 33 properties take none.** The orchestrable footprint is **The Langham Sydney (96 rooms), The Langham Melbourne (388), Cordis Auckland (641) and The Langham Gold Coast** — and within those, only the `DIRECT_BILL` rate plans, and only the share that books on brand.com rather than through an OTA, GDS or corporate channel. That is a small number by any reading.
2. **The matrix is double-counting one underlying fact.** "Multiple PSPs" (+3) and part of "3+ countries" (+3) both fire off the *same* three-hotel ANZ cluster. Six of the fourteen points rest on a footprint that represents **HK$380.0m of HK$2,570.8m** of H1 2026 Hotels Division revenue, and three hotels out of thirty-three.
3. **The buyer is not where the account sits.** For the 28 gateway-less properties the card is charged by the property, on the property's own PMS/terminal, under the property owner's merchant agreement. **The Langham, Jakarta is owned by Agung Sedayu Group**, not Langham ([Luxury Travel Advisor](https://www.luxurytraveladvisor.com/hotels/langham-jakarta-opens-its-doors), [TTG Asia](https://www.ttgasia.com/2013/11/15/langham-hospitality-group-moves-into-jakarta/)); **15 of the hotels are third-party managed** (Great Eagle H1 2026). An HQ conversation cannot sign for acceptance it does not control.

**Plus a competitive blocker:** their CRS vendor already sells the exact product — SynXis Pay, CellPoint-powered, native to the booking engine they run. Any central payments programme at Langham will have Sabre in the room first.

**What would move this back up, immediately:** a group payments or e-commerce hire; the Bangkok or Kuala Lumpur launch going live *with* online prepayment; any evidence that Hong Kong or Jakarta have been given a gateway; or a brief that the group is consolidating acceptance ahead of the loyalty platform rebuild. **Re-score on any of those.** The underlying prize is real — HK$5.3bn of annual hotel revenue and 44.53% APAC booking traffic — it just is not addressable today.

**Recommendation:** **one** exploratory touch on the "Asia cannot take a payment" observation, aimed at Group CFO / VP Commercial & Distribution / VP IT rather than a payments owner (there is no evidence one exists). Do not invest a 12-touch sequence until the structural question is answered by a human.

### Monthly transaction count — mandatory disclosure

**⚠️ NOT FOUND — ASSUMED. [ASSUMPTION — not researched.]**

**Billing unit I am counting: online card payments authorised at time of booking, by the merchant of record on `langhamhotels.com`.** Not room nights. Not guests. Not folios. The distinction matters more here than in any account I have seen, because most Langham folios are settled at a property desk and never touch a central e-commerce stack.

Three figures, stacked, so the reader can see exactly where sourcing stops:

| Layer | Figure | Status |
|---|---|---|
| **Room nights / month, 15 owned + LHI hotels** | **~167,900** | ✅ **DERIVED** — Σ(average daily rooms available × occupancy) × 365 ÷ 12. **Both inputs sourced** from Great Eagle's [2025 Annual Results Announcement](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0303/2026030302294.pdf), pp.10 and 14. Arithmetic in Section 12. **But a room night is not a transaction.** |
| **Folios (stays) / month, same 15 hotels** | **~84,000** | ⚠️ **ASSUMED** — 167,900 ÷ an assumed **average length of stay of 2.0 nights**. *ALOS is not published for this group and I could not source it.* Per the method, an unsourced input makes the output an assumption regardless of the arithmetic. **And most of these folios settle at the property, not online.** |
| **Online card payments at booking (the orchestrable unit)** | **low single-digit thousands / month** | ⚠️ **ASSUMED — [ASSUMPTION — not researched.]** Basis: only 4 live properties have a gateway (ANZ). Their room nights are **~26,900/month** (Melbourne 10,043 + Sydney 2,660 + Auckland 14,213; Gold Coast not in the owned-hotel table, no occupancy published) → **~13,500 folios/month at the same assumed ALOS 2.0**. Of those, only the brand.com-direct share converts here (OTA, GDS, corporate and walk-in do not), and only `DIRECT_BILL` rate plans charge at booking rather than guarantee. **Neither the direct-booking share nor the DIRECT_BILL rate mix is published.** |

**Three rules applied explicitly:**
1. **The assumption does not reject the account.** The under-40,000 gate fires only on a sourced or soundly-derived figure. This is assumed, so **no rejection** — and "confirm monthly transaction count" is item #1 in Manual Research Recommendations.
2. **No derivation is presented as a measurement.** Room nights are derived and labelled ✅. Everything downstream of ALOS is labelled ⚠️ ASSUMED.
3. **374,332 monthly visits is NOT 374,332 transactions.** Hotel booking conversion is low single-digit percent. At a 2% look-to-book — *which I have not sourced and am not asserting* — that is ~7,500 bookings a month across the whole brand.com estate, of which only the ANZ slice is charged online. The visit number must never be used as a volume proxy in a conversation with this account.

### Source Notes
- ✅ **28 of 33 properties return `paymentGateway: ""`** — my own repeated queries against Langham's live availability API, 2026-10-09. Reproducible; the curl is in the header block.
- ✅ **Cybersource at Sydney/Melbourne/Auckland, Adyen at Gold Coast/Toronto** — same source, plus the vendor SDKs in the booking engine's own JavaScript bundles.
- ✅ **Cards only at all 33 properties — zero alternative payment methods anywhere** — their own GraphQL CMS, `hotels { paymentTypesAccepted { cardType } }`. Full table in Section 4.
- ✅ **2.50% flat card surcharge at Cordis Auckland, every scheme** — same GraphQL, `transactionFees`.
- ✅ **Hotels Division FY2025 HK$5,307.1m / H1 2026 HK$2,570.8m, with per-hotel rooms, occupancy, ADR and RevPAR** — Great Eagle results announcements on HKEXnews, which I downloaded and extracted myself.
- ✅ **The TAL's "~$700M est." is approximately right but mislabelled.** HK$5,307.1m ≈ **US$680m** at HK$7.8/US$1 *(my conversion; the FX rate is not sourced)*. That is **Great Eagle's Hotels Division revenue** — the hotels' own trading revenue — **not Langham Hospitality Group's revenue.** LHG is the management company; its own revenue is management fee income, which is not separately disclosed.
- ⚠️ **No company registration number found** in any jurisdiction. No Australian, Indonesian, Thai or New Zealand Langham entity identified.
- ⚠️ **Langham Hospitality Investments (1270.HK) structure** (stapled HK trust + Cayman company, owns three HK hotels, managed by Langham Hotels International Ltd) rests partly on a **search summary**; the primary HKEX filing was not fetched. The *distinction* between 1270 and LHG is corroborated by Great Eagle's own 2025 results, §4.
- ⚠️ **Brilliant by Langham 2026 refresh / AI personalisation** — `[UNVERIFIED — search summary only, page returned HTTP 403 and was not fetched]`.
- ⚠️ **PayTo / BPAY / BNPL merchant adoption in Australia: NOT ESTABLISHED.** I searched for a current primary source (AusPayNet / Australian Payments Plus NPP statistics) and did not find a dated, authoritative merchant-adoption figure. Per the brief, **I am not citing one.** The *absence* of these rails from Langham's checkout is sourced; their *prominence* is not.
- ⚠️ **Acquirers: not established.** Not naming a guess.
- ⚠️ **No subagents were used.** No Agent/Task tool is available in this environment, so Phases 1–3 were executed directly rather than in the five-agent fan-out the method specifies. Search volume was comparable; parallelism was not.
- ❌ **Checkout beyond the payment step was not walked.** Completing it would have required creating a real reservation at a real hotel. I did not do that — see Section 8.

### Success Case Alternatives
- **Qatar Airways** — the closest profile match Yuno can publicly reference: high-ticket travel, multi-market, multi-currency, cross-border card acceptance across many issuer geographies. *No published metrics exist for this relationship — do not attach a number to it.*
- **Avianca / Copa Airlines** — multi-country travel operators with per-market acceptance problems. Same constraint: **nameable, no figures.**
- ⚠️ **Honest caveat:** none of Yuno's publicly referenceable cases is a hotel group, and none has the per-property merchant-of-record structure that defines this account. Say so rather than stretching an airline onto it.

---

## Executive Summary

Langham Hospitality Group is the hotel operating arm of Hong Kong-listed Great Eagle Holdings (HKEX: 0041), running 33 live properties under The Langham, Cordis, Eaton Workshop and Ying'nFlo. Its booking domain `langhamhotels.com` draws 374,332 monthly visits with an unusually strong APAC profile — 44.53% visible, led by **Australia at 24.08%** and **Indonesia at 10.79%**. **The key payment-infrastructure finding is that there is no central payment stack:** querying their own booking API across all 33 properties shows a gateway configured at only five — Cybersource at Sydney, Melbourne and Auckland, Adyen at Gold Coast and (not-live) Chelsea Toronto — while **28 properties, including every Asian, US and UK hotel, return an empty `paymentGateway` and accept the card as a guarantee only**, with prepayment collected by emailed payment links from property mailboxes. The orchestration opportunity is therefore **greenfield in the strictest sense and very small today**: a build conversation about giving Asia online acceptance, not a routing or failover conversation, with the buyer sitting at property and owner level and Sabre's own CellPoint-powered SynXis Pay occupying the natural path. **Motion: Greenfield.**

---

## Section 1: Website Traffic Analysis by Country

**Data source:** **Path 1 — pasted SimilarWeb data supplied by Prateek.** `accounts/traffic/langham-hospitality-group.md`, cited as **SimilarWeb (supplied 2026-10-09)**, period Sep 2026, SimilarWeb PRO Worldwide/All traffic. **Used verbatim. Not re-researched.** It is a **top-10 cut per domain**, so every APAC total is a *visible floor*, not a complete count.

### Booking domain — `langhamhotels.com` (the one that matters)
**Total visits: 374,332 · MoM ▼12.41% · Desktop 30.18% / Mobile web 69.82%**

| Rank | Country | Share | Est. monthly visits | Trend | Local entity? | Source |
|---|---|---|---|---|---|---|
| 1 | 🇺🇸 United States | **33.39%** | ~124,990 | n/a per-country | ✅ 4 properties | SimilarWeb (supplied 2026-10-09) |
| 2 | 🇦🇺 **Australia** | **24.08%** | ~90,139 | n/a | ✅ 3 properties | ibid. |
| 3 | 🇬🇧 United Kingdom | **11.40%** | ~42,674 | n/a | ✅ 1 property | ibid. |
| 4 | 🇮🇩 **Indonesia** | **10.79%** | ~40,390 | n/a | ⚠️ 1 *managed* property, third-party owned | ibid. |
| 5 | 🇭🇰 **Hong Kong** | **5.22%** | ~19,540 | n/a | ✅ HQ, 5 properties | ibid. |
| 6 | 🇨🇦 Canada | 2.69% | ~10,070 | n/a | ⚠️ 1 property, `isLive: false` | ibid. |
| 7 | 🇸🇬 **Singapore** | **1.58%** | ~5,914 | n/a | ❌ **no property** | ibid. |
| 8 | 🇰🇷 **Korea** | **1.18%** | ~4,417 | n/a | ❌ **no property** | ibid. |
| 9 | 🇮🇳 **India** | **0.88%** | ~3,294 | n/a | ❌ **no property** | ibid. |
| 10 | 🇹🇭 **Thailand** | **0.80%** | ~2,995 | n/a | ⚠️ Bangkok opening late 2026 | ibid. |

**Markets above 5% share — high priority:** US, **Australia**, UK, **Indonesia**, **Hong Kong**.
**APAC visible total: 44.53%.** Visit estimates are my arithmetic (share × 374,332) and carry the rounding of the supplied shares.

### Corporate domain — `langhamhospitalitygroup.com`
**Total visits: 17,201 · MoM ▼11.36% · Desktop 37.89% / Mobile 62.11%**
US 32.15 · UK 12.45 · **India 8.92** · Canada 8.26 · **Indonesia 7.37** · **Singapore 7.21** · **Hong Kong 6.56** · **Thailand 5.40** · **New Zealand 4.27** · **Australia 3.81**. **APAC visible 43.54%.**

**I did not sum the two domains**, deliberately. The corporate site is a brand/careers/press property with **no checkout** — `langhamhotels.com/en/terms-and-conditions/` even **302-redirects to `langhamhospitalitygroup.com/en/terms-and-conditions/`**, confirming shared corporate content rather than a shared commerce funnel (verified: `curl -I`, 2026-10-09). Blending its 17,201 visits into the booking profile would inflate India and Singapore against markets with no bookable property. **Everything downstream anchors on the booking domain.**

### 🔑 The Australia anomaly — explained, and it holds up
**24.08% of booking traffic from Australia is genuine and structurally explicable.** Langham operates **three ANZ properties** — The Langham Melbourne (388 rooms), The Langham Sydney (96 rooms), The Langham Gold Coast and Jewel Residences — plus **Cordis Auckland (641 rooms)**. Combined, Melbourne + Sydney + Auckland deliver **~323,000 room nights a year** (derived; Great Eagle 2025 results). Melbourne ran **85.1% occupancy** and Sydney **91.1%** in FY2025 — the two highest of any Great Eagle-owned hotel outside Hong Kong and Shanghai. ANZ contributed **HK$766.6m** of FY2025 and **HK$380.0m** of H1 2026 Hotels Division revenue. A large, high-occupancy, domestically-booked ANZ base is exactly what a 24% traffic share looks like. **And ANZ is the only region where the booking engine actually charges a card** — so this is the one place the routing, failover and cost-of-acceptance pitch could land at all.

### 🔑 The Indonesia anomaly — NOT explained, and I am saying so
**10.79% (~40,400 visits/month) from Indonesia against ONE 223-room managed hotel does not add up, and I could not determine why.**
What is established: The Langham, Jakarta opened **9 September 2021** with **223 rooms** in District 8, SCBD; it is **owned by Agung Sedayu Group** and operated by LHG ([Luxury Travel Advisor](https://www.luxurytraveladvisor.com/hotels/langham-jakarta-opens-its-doors), [TTG Asia](https://www.ttgasia.com/2013/11/15/langham-hospitality-group-moves-into-jakarta/)). It is Langham's only Indonesian property.
Candidate explanations, **all `[INFERENCE, not confirmed]`**: (a) Indonesian outbound travellers researching Langham properties abroad — plausible given Hong Kong, Australia and Shanghai are common Indonesian luxury destinations; (b) heavy domestic traffic for the Jakarta hotel's F&B, spa and events rather than rooms; (c) non-human or affiliate traffic inflating a single-country share. **I cannot distinguish between these, and the supplied SimilarWeb cut gives no landing-page or engagement breakdown to test them.**
**What I can state with certainty, regardless of which it is:** the Jakarta property has **`paymentGateway: ""`**, accepts **cards only**, and collects prepayment by **a manually emailed payment link from `tljkt.reservation@langhamhotels.com`**. If that traffic *is* transacting, it is transacting over email. If it is not transacting, the 10.79% is not a payments signal at all. **Prateek must resolve this before the account is sized** — see Manual Research Recommendations.

---

## Section 2: Legal Entities & Local Presence

**Headquarters:** Hong Kong. Langham Hotels International Limited was **renamed from Great Eagle Hotels International in 2003**; parent Great Eagle Holdings was **founded in 1963** and is listed on HKEX ([Wikipedia](https://en.wikipedia.org/wiki/Langham_Hospitality_Group)).

| Country | Entity Name | Registration # | Source |
|---|---|---|---|
| Hong Kong | **Langham Hotels International Limited** (t/a Langham Hospitality Group) | **Not found** | [Wikipedia](https://en.wikipedia.org/wiki/Langham_Hospitality_Group); footer of `langhamhospitalitygroup.com` |
| Hong Kong | **Great Eagle Holdings Limited** — listed parent | **HKEX stock code 41** (not a registry number) | [2025 Annual Results](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0303/2026030302294.pdf) |
| Hong Kong / Cayman | **Langham Hospitality Investments** — ⚠️ **separate listed owner, NOT the operator** | **HKEX stock code 1270** | Great Eagle 2025 Annual Results §4; LHI structure `[search summary only]` |
| Mainland China | Operating presence — 12 properties live in the CRS | **Not found** | Langham GraphQL CMS hotel list (my own query) |
| Australia | Operating presence — 3 properties | **Not found** — no ASIC entity identified | ibid. |
| New Zealand | Operating presence — Cordis Auckland | **Not found** | ibid. |
| Indonesia | 1 **managed** property; **owned by Agung Sedayu Group** | **No PT entity found** | [Luxury Travel Advisor](https://www.luxurytraveladvisor.com/hotels/langham-jakarta-opens-its-doors) |
| Thailand | Bangkok opening late 2026, with **Rabbit Holdings (BTS Group affiliate)** as partner | **Not found** | [Sleeper](https://www.sleepermagazine.com/stories/projects/langham-to-open-bangkok-riverside-retreat/) |
| UK / US / Canada | Operating presence | **Not found** | Great Eagle 2025 Annual Results p.10 |

> **MANUAL:** I could not read the group's terms or privacy policy. `langhamhotels.com/en/terms-and-conditions/` 302s to the corporate domain, and the corporate domain returned **HTTP 403 to both `curl` and WebFetch**. In APAC the billing entity is very often named only there. **This is the single highest-value manual check on the account** — the merchant of record per property is the whole question.

### Cross-Border Gap Analysis

| Country | In top 10 traffic? | Has local entity? | Domestic acquiring gated? | Cross-border risk? |
|---|---|---|---|---|
| 🇺🇸 United States | ✅ #1 (33.39%) | ✅ properties operating | No | Low — but **no online acceptance at all**, so moot |
| 🇦🇺 **Australia** | ✅ #2 (24.08%) | ✅ properties operating | No | **The only market with live online acceptance.** Split across two gateways |
| 🇬🇧 United Kingdom | ✅ #3 (11.40%) | ✅ 1 property | No | Moot — guarantee only |
| 🇮🇩 **Indonesia** | ✅ #4 (10.79%) | ⚠️ **managed, third-party owned; no Langham PT found** | ⚠️ **Verify — see caveat below** | **High, and unmeasurable** — no gateway, settlement by emailed link |
| 🇭🇰 **Hong Kong** | ✅ #5 (5.22%) | ✅ HQ | No | Moot — guarantee only, prepay by emailed link |
| 🇸🇬 **Singapore** | ✅ #7 (1.58%) | ❌ **no property** | n/a | Traffic with nothing to sell |
| 🇰🇷 **Korea** | ✅ #8 (1.18%) | ❌ **no property** | n/a | Traffic with nothing to sell |
| 🇮🇳 **India** | ✅ #9 (0.88%) | ❌ **no property** | n/a | Traffic with nothing to sell |
| 🇹🇭 **Thailand** | ✅ #10 (0.80%) | ⚠️ opening late 2026 | ⚠️ **Verify** | **Launching with no online acceptance** |
| 🇨🇳 Mainland China | not in top 10 | 12 properties live | ⚠️ **Verify** | Moot — guarantee only |

> **Warning: potential cross-border operation in Indonesia (#4, 10.79%).** No Langham Indonesian entity found; the property is third-party owned and managed. Any card transaction is settled by the owner's Indonesian merchant arrangement — **which Langham HQ does not control and which I could not identify.**

> **Regulatory gate — NOT ASSERTED.** The `.claude/reference/apac-payments.md` checklist flags Indonesia (Bank Indonesia PJP licensing), Mainland China, Vietnam, India and South Korea as markets where domestic acquiring is effectively gated behind local presence or licensing. **Per the brief and the integrity mandate, I did not find a current primary regulatory source for any of these during this run, so I am not stating any of them as fact.** They are checklist items to verify, and that verification is in Manual Research Recommendations. **No ICP point was awarded on a regulatory gate.**

---

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|---|---|---|---|
| 🇦🇺 Australia — The Langham, **Sydney** (AUD) | **Cybersource** (Unified Checkout) | `[Checkout]` `[Source Code]` — availability API returns `paymentGateway: "cybersource"` | `POST https://reservations.brilliantbylangham.com/api/booking/availability` (hotelCode 16758) |
| 🇦🇺 Australia — The Langham, **Melbourne** (AUD) | **Cybersource** | same | hotelCode 27408 |
| 🇳🇿 New Zealand — **Cordis, Auckland** (NZD) | **Cybersource** | same | hotelCode 27424 |
| 🇦🇺 Australia — The Langham **Gold Coast** (AUD) | **Adyen** (Web Drop-in, Sessions flow) | `[Checkout]` `[Source Code]` — `paymentGateway: "adyen"` | hotelCode 37778 |
| 🇨🇦 Canada — **Chelsea Hotel Toronto** (CAD, `isLive: false`) | **Adyen** | same | hotelCode 59052 |
| **All other 28 properties** — HK ×5, China ×12, Indonesia, Thailand, USA ×4, UK, + Ying'nFlo | **NONE — `paymentGateway: ""`** | `[Checkout]` `[Source Code]` | same endpoint, all hotel codes |
| Global — CRS / booking engine | **Sabre Hospitality — SynXis** (white-labelled BE on `reservations.brilliantbylangham.com`, Akamai-fronted) | `[Source Code]` — CSP allowlists `*.synxis.com`, `*.sabrehospitality.com`, `*.asc.sabre.com`, `*.sabrecirrus.com`, `*.sabre-gcp.com`; hotel keys are `synxisHotelId` | `curl -D - https://reservations.brilliantbylangham.com/?chain=10316&brand=tlhr&locale=en-US&theme=brilliant&config=brilliant&level=hotel` |
| **Acquirers (all markets)** | **NOT ESTABLISHED** | — | No public evidence found. **Not naming a guess.** |

**Integration detail, verbatim from their own bundle (2026-10-09 — assets re-fetched fresh this run; nothing reused from a scratchpad):**

- **Adyen** — [`guest_details-dc3a024a5e185881.js`](https://reservations.brilliantbylangham.com/_next/static/chunks/pages/booking/guest_details-dc3a024a5e185881.js) @ offset 52374:
  `({clientKey:e.clientKey, environment:e.env, session:r, countryCode:e.session.countryCode, amount:e.session.amount, locale:e.session.shopperLocale, onPaymentCompleted:…}).then(e=>{console.log("Checkout created, available payment methods:",e.paymentMethodsResponse), … new eF.Bf(e).mount(d.current)})`
  → **Adyen Drop-in on the `/sessions` flow.** The Adyen Web SDK is bundled as chunk [`3237-597da73056e6ea57.js`](https://reservations.brilliantbylangham.com/_next/static/chunks/3237-597da73056e6ea57.js) (675 KB).
- **Cybersource** — same file @ 52969: component destructures `{captureContext}`, base64-decodes the JWT's payload, reads `ctx[0].data.clientLibrary` / `clientLibraryIntegrity`, injects that script with SRI and `crossOrigin`, then requires `window.Accept` — throwing `"UnifiedCheckout Accept API not loaded"` otherwise. Verification endpoint: `POST /payment/cybersource/verify`.
- **Mutual exclusivity, in their code** — same file @ 54616:
  `v = d ? {provider:"adyen",data:d} : c ? {provider:"cybersource",data:c} : {provider:null,data:{}}`
  → **one gateway per booking session, selected by what the server returned. No cascade, no fallback, no retry on a second provider.** If the configured gateway declines or is down, the booking fails. That is the single clearest technical statement of what Langham does not have.
- **Session-storage keys** `adyen`, `cybersource`, `paymentConfirmationData` — [`_app-661c61301c46b67b.js`](https://reservations.brilliantbylangham.com/_next/static/chunks/pages/_app-661c61301c46b67b.js) @ 532437.

**False-positive discipline — what I checked and discarded:** the strings `payto`, `paynow`, `promptpay`, `duitnow`, `upi`, `dana`, `afterpay`, `wechatpayQR`, `applepay`, `googlepay`, `paypal`, `onlineBanking_IN` **all appear in chunk 3237** — but every one sits inside the Adyen Web SDK's own generic payment-type enum (`p.payto="payto", p.upi="upi", p.giftcard="giftcard"…`) alongside `blik`, `mbway`, `ancv` and `mealVoucher_FR_natixis`. **These are the SDK's full catalogue of what Adyen *can* do, not what Langham has configured.** The same chunk lists `checkoutshopper-live-au`, `-apse`, `-in` and `-us` endpoints — also generic. **Reported as zero hits.** (Noted per the repo's recorded trap: `dana` means "funds" in Indonesian and `zip` matches compression strings; neither produced a real hit here either.)

**And the inverse trap applies, which is why Section 4 relies on the CMS, not the bundle:** both Adyen Drop-in and Cybersource Unified Checkout render the payment-method list **server-side from the vendor's own dashboard configuration** — `e.paymentMethodsResponse` for Adyen, the `captureContext` JWT for Cybersource. **Nothing in Langham's own JavaScript can tell you which methods are enabled on the ANZ gateways.** That question is answered in Section 4 only for the card list, which *is* in Langham's CMS.

### 3B. Payment Orchestrator

**Classification: None detected — direct PSP integrations only. GREENFIELD.**

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with PSP(s), which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

Evidence for the negative, which is unusually strong here because I read the checkout code rather than relying on search:
- `provider` resolves to exactly one of `"adyen"` / `"cybersource"` / `null` per session — **no router, no cascade, no failover** (`[Source Code]`, quoted above).
- The gateway is a **static per-hotel configuration field** returned with availability, not a routing decision.
- No orchestrator vendor string in the booking engine's 40 JavaScript chunks, the CSP allowlist (which names 50+ third-party domains and would have caught one), or the GraphQL schema.
- No hit for Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY or Yuno in any public source. The `Payment Orchestrator` column in `accounts/apac-tal.csv` is **empty** for this row, and nothing contradicts that.

> **MANUAL:** Walk the ANZ checkout with DevTools — Sydney (Cybersource) and Gold Coast (Adyen) — and capture the rendered method list. That is the only way to see which APMs are switched on at the gateway, and it requires a human session that can be abandoned before confirmation.

⚠️ **The competitive risk sits in the CRS, not in a rival orchestrator.** Sabre's **SynXis Pay**, launched 3 March 2025 with its **"orchestration layer … powered by CellPoint Digital"**, "over 250 alternative payment methods" including Apple Pay, Google Pay, PayPal, Klarna and WeChat Pay, and "a new express checkout experience in SynXis Booking Engine", **rolling out "in phases over the coming months"** ([Travolution, 3 Mar 2025](https://www.travolution.com/news/travel-sectors/accommodation/sabre-hospitality-introduces-synxis-pay/)). **Langham is not on it today** — a SynXis Pay deployment would not leave 28 properties with an empty `paymentGateway` and raw `adyen`/`cybersource` values. But it is native to the platform they already run, and the phased rollout status as of today is **not established**.

---

## Section 4: Alternative & Local Payment Methods

**This section is sourced from Langham's own CMS, not from their JavaScript bundle** — `POST https://reservations.brilliantbylangham.com/en-US/graphql` with `query {content {hotels(first:1000){edges{node{name synxisHotelId paymentTypesAccepted{cardType} transactionFees{cardType percent}}}}}}`. That is the per-property acceptance configuration the booking engine itself reads.

### 🔴 The headline: **cards only. All 33 properties. Zero alternative payment methods anywhere in the group.**

| Country/Region | Method | Category | Status | Source |
|---|---|---|---|---|
| **All 33 properties** | Visa, Mastercard, American Express | Cards | **Active in checkout** (every property) | GraphQL `paymentTypesAccepted` |
| **All 33 properties** | **China UnionPay** (card), Diners Club, Discover, JCB | Cards | **Active**, per-property mix (UnionPay at 26 of 33, incl. Sydney, Melbourne, Gold Coast, Jakarta, Hong Kong, Bangkok) | ibid. |
| 🇮🇩 **Indonesia (#4, 10.79%)** | **QRIS** | Bank transfer / A2A | **NOT FOUND** | ibid. — Jakarta lists `Amex, UnionPay, JCB, Mastercard, Visa` only |
| 🇮🇩 Indonesia | **Virtual account / bank transfer** | Bank transfer | **NOT FOUND** | ibid. |
| 🇮🇩 Indonesia | **GoPay, OVO, DANA, ShopeePay** | Digital wallet | **NOT FOUND** | ibid. |
| 🇮🇩 Indonesia | **Alfamart / Indomaret OTC cash** | Cash/voucher | **NOT FOUND** | ibid. |
| 🇦🇺 **Australia (#2, 24.08%)** | **PayTo** | Direct debit / mandate | **NOT FOUND** | ibid. — Sydney, Melbourne, Gold Coast all card-only |
| 🇦🇺 Australia | **BPAY** | Bank transfer | **NOT FOUND** | ibid. |
| 🇦🇺 Australia | **Afterpay, Zip** | BNPL | **NOT FOUND** | ibid. |
| 🇳🇿 New Zealand | **POLi**, Afterpay | Bank transfer / BNPL | **NOT FOUND** | ibid. |
| 🇭🇰 **Hong Kong (#5, 5.22%)** | **FPS, Octopus, AlipayHK, WeChat Pay HK** | A2A / wallet | **NOT FOUND** | ibid. — all 5 HK properties card-only |
| 🇨🇳 Mainland China (12 properties) | **Alipay, WeChat Pay, UnionPay QR** | Digital wallet | **NOT FOUND** — UnionPay appears as a *card* type only | ibid. |
| 🇹🇭 **Thailand** (Bangkok, late 2026) | **PromptPay**, Thai bank transfer, instalments | A2A / instalments | **NOT FOUND** — launching card-only | ibid., hotelCode 99801 |
| 🌐 Global | **Apple Pay, Google Pay, PayPal, BNPL** | Wallet / BNPL | **NOT FOUND in the CMS.** ⚠️ Could in principle be enabled at the Adyen or Cybersource dashboard for the 4 ANZ properties — **not observable without walking checkout** | see Section 3A trap note |
| 🇳🇿 **Cordis, Auckland** | **2.50% surcharge on EVERY card scheme** | Cards | **Active** — the only `transactionFees` entry in the entire 33-property CMS | GraphQL `transactionFees` |
| 🇨🇳 Cordis, Xi'an | **No card types configured at all** (`paymentTypesAccepted: []`) | — | Empty | ibid. |

**Three warnings, each with its source:**

> **Warning — Indonesia (#4 market, 10.79% of booking traffic):** QRIS is Indonesia's national interoperable QR standard and virtual-account transfer is the default e-commerce rail, per `.claude/reference/apac-payments.md` §2. **Neither is supported by Langham, and nor is any wallet or cash rail.** The property has **no payment gateway at all**, and prepaid bookings are settled by a manually emailed link. ⚠️ **I did not find a current primary source quantifying QRIS or VA share of Indonesian e-commerce during this run, so I am not citing a figure.** The *absence* is sourced; the *share* is not.

> **Warning — Australia (#2 market, 24.08%):** no PayTo, BPAY, Afterpay, Zip or POLi at any ANZ property. **The absence is sourced from their own CMS.** ⚠️ **But I could not establish current Australian merchant adoption of PayTo, BPAY or hotel-booking BNPL from a primary source** — I searched for Australian Payments Plus / NPP Australia statistics and found only vendor material, undated aggregator reports and one single-provider index. **Per the brief, I am citing none of them, and I awarded no ICP point for this gap.** Treat "Australia is missing local rails" as *verified absent but unproven as a loss* until Prateek sources adoption data.

> **Warning — Hong Kong, the home market:** five properties, zero local rails. No FPS, no Octopus, no AlipayHK, no WeChat Pay HK — in a market where those are everyday consumer behaviour. And the prepaid rate cannot be charged online at all.

### The verbatim rate terms — this is where the structure is visible
From the live availability API, `roomRates[].rates[].guarantee.description`:

| Property | Code | `acceptedPaymentTypes` | Verbatim text |
|---|---|---|---|
| 🇭🇰 **The Langham, Hong Kong** | `PPFUL` | `["CREDIT_CARD"]` | *"Full prepayment for the entire stay is required. **The credit card is for guarantee purpose only. A secured payment link will be sent to you in a separate e-mail.** Please settle all payment via the secured payment link."* |
| 🇭🇰 The Langham, Hong Kong | `GTD` | `["CREDIT_CARD"]` | *"All reservations must be guaranteed by credit card. Please present the credit card used to make this reservation upon check-in at the hotel."* |
| 🇮🇩 **The Langham, Jakarta** | `FP` | `["CREDIT_CARD"]` | *"The rate requires non-refundable full prepayment for the entire stay… **The reservation team will send a payment link for room accommodation settlement from our official reservation email at tljkt.reservation@langhamhotels.com.** Bookings without payment confirmation will be automatically cancelled."* |
| 🇺🇸 The Langham, New York | `DEP` | `["CREDIT_CARD"]` | *"Non-refundable full pre-payment is required within 24 hours of booking date."* — **not at booking; no gateway to take it** |
| 🇬🇧 The Langham, London | `GCC` | `["CREDIT_CARD"]` | *"A valid credit card guarantee is required to secure the booking. Charges will not be made…"* |
| 🇨🇳 The Langham, Shanghai Xintiandi | `GCC` | `["CREDIT_CARD"]` | *"All reservations require a credit card guarantee at time of booking"* |
| 🇦🇺 **The Langham, Sydney** | `DEP` | **`["DIRECT_BILL","CREDIT_CARD"]`** | *"Full prepayment is required at time of reservation."* — **DIRECT_BILL present + gateway present = actually charged online** |
| 🇦🇺 The Langham Gold Coast | `1NT` | **`["DIRECT_BILL","CREDIT_CARD"]`** | *"Deposit for the first night's room rate is required at the time of booking and is non-refundable…"* |
| 🇳🇿 **Cordis, Auckland** | `ALL` | **`["DIRECT_BILL","CREDIT_CARD"]`** | *"Full (100%) deposit required at time of booking… **Credit card payments incur a 2.5% surcharge**"* |
| 🇳🇿 Cordis, Auckland | `CGT` | `["CREDIT_CARD"]` | *"Credit card guarantee required at time of booking. **Credit card payments incur a 2.50% surcharge.**"* |

**Read the pattern:** Hong Kong, Jakarta, New York and London all demand prepayment in words, and **none of them can collect it through the booking engine**, because `paymentGateway` is empty at all of them. The money moves by email. ⚠️ **An earlier version of this line claimed `DIRECT_BILL` appears only where a gateway exists — that is false** (Bangkok has `DIRECT_BILL` and no gateway; verified by the orchestrator 2026-10-09). **The empty gateway is the load-bearing fact, not the rate type.**

> **MANUAL:** VPN into AU, ID and HK and walk the booking flow to the payment step for Sydney (Cybersource), Gold Coast (Adyen) and Hong Kong (none). Confirm whether the ANZ gateways render any wallet, and confirm what Hong Kong actually shows a guest at the payment step.

---

## Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|---|---|---|---|---|
| Prepaid add-on not refunded, plus a £60 cancellation fee charged | Venuescanner review, The Langham London | **Isolated** (single review) | Mar 2026 | [venuescanner.com](https://www.venuescanner.com/gb/venues/london/london/book/the-langham-hotel-london/the-terrace-garden) `[UNVERIFIED — search summary only, page not fetched]` |

*No payment-related complaint pattern found on Reddit, X, Trustpilot or app store reviews.* Searches covered declined cards, failed payments, double charges, payment links, prepayment and refunds across The Langham, Cordis and Brilliant by Langham. Two UK Financial Ombudsman decisions surfaced on hotel payment links but **concern other companies**, not Langham — explicitly excluded.

**⬜ No ICP point awarded.** One isolated review is not a moderate- or high-frequency pattern.

**Honest caveat on this absence:** it is a weak negative. **28 of 33 properties take payment by email or at the desk** — a flow that generates phone calls to a hotel's reservations team, not public complaints about a checkout. There is also **no Langham consumer app store presence** found to review-mine, which in APAC is usually the richest source. The absence of complaints here says more about where the payment happens than about how well it works.

---

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|---|---|---|---|
| 1 | **26 Aug 2026** | **H1 2026 results:** Hotels Division revenue **HK$2,570.8m (+7.6%)**, EBITDA **HK$475.0m (+16.3%)**; ANZ revenue **HK$380.0m (+4.6%)**, EBITDA **+24.3%**. Third-party hotels under management up to **15 (~4,400 rooms)** from 14 (~4,200) at Dec-2025 | Financial results / Market Expansion | [HKEXnews](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0826/2026082601083.pdf) |
| 2 | **late June 2026** | **Ying'nFlo opened in Qingdao** — fourth Mainland China outlet after Hangzhou (Jul 2025), Wuhan (Aug 2025) and Nanjing (Dec 2025). Asset-light, select-service brand | Market Expansion | [HKEXnews H1 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0826/2026082601083.pdf) |
| 3 | **Dec 2026 (opening); bookable now** | **The Langham, Custom House, Bangkok** — 75 keys in the restored 1888 Customs House, with **Rabbit Holdings (BTS Group affiliate)**. **Live in the CRS today (hotelCode 99801), quoting THB inventory for Dec 2026 and Feb 2027, with `paymentGateway: ""` and no PromptPay** — verified by me via their own availability API, 2026-10-09 | Market Expansion | [Langham Bangkok page](https://www.langhamhotels.com/en/the-langham/bangkok) · [Sleeper](https://www.sleepermagazine.com/stories/projects/langham-to-open-bangkok-riverside-retreat/) · [Robb Report SG](https://robbreport.com.sg/the-langham-custom-house-bangkok/) |
| 4 | **3 Mar 2026** | **FY2025 results:** Hotels Division revenue **HK$5,307.1m (+4.4%)**, EBITDA **HK$1,152.2m (+4.3%)**; per-hotel occupancy/ADR/RevPAR disclosed; **write-off of HK$200.5m pre-construction costs on two hotel projects under development** | Financial results | [HKEXnews](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0303/2026030302294.pdf) |
| 5 | **22 Jun 2026** | **Nils-Arne Schroeder appointed Chief Operating Officer** (CEO remains Bob van den Oord, in post since 2023) | Leadership Change | [Breaking Travel News](https://www.breakingtravelnews.com/news/article/nils-arne-schroeder-named-chief-operating-officer-of-langham-hospitality-gr/) `[UNVERIFIED — search summary only, page not fetched]` |
| — | 2026 | **Brilliant by Langham refreshed** — experiences platform plus "AI-powered personalisation"; The Langham, Kuala Lumpur reported on track for end-2027 | Tech / Market Expansion | [Business Traveller](https://www.businesstraveller.com/news/brilliant-by-langham-refreshed/) `[UNVERIFIED — HTTP 403, page not fetched]` |

**No public payment-related RFP found.** **No job postings mentioning PSP evaluation, payment platform migration or orchestration found** — searches across LHG careers aggregators returned only hotel operations and property-level accounting roles (e.g. an AR/income accountant at Eaton Hong Kong). **No payment-adjacent licence application found** in any APAC market.

---

## Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|---|---|---|---|
| 1 | **3 Mar 2025** | **Sabre Hospitality launches SynXis Pay**, with its *"orchestration layer … powered by CellPoint Digital"*, *"over 250 alternative payment methods"* including Apple Pay, Google Pay, PayPal, Klarna and WeChat Pay, and *"a new express checkout experience in SynXis Booking Engine"*; *"released in phases over the coming months"* | **Highest relevance on the account.** Langham's own CRS vendor now bundles a competing orchestrator natively into the booking engine Langham runs. Langham is **not on it** today | [Travolution](https://www.travolution.com/news/travel-sectors/accommodation/sabre-hospitality-introduces-synxis-pay/) |
| 2 | 2026 | **Points Plus Cash redemption is live** on Brilliant by Langham: *"Eligible Reward Stays may be redeemed using a combination of Award Points and cash through a Points Plus Cash Stay."* Rate codes confirming this appear in the live availability API (e.g. `RFLXLCT0`, "Points & Cash – Flexible Rate", with a `partialRedemption` cash leg) | A split points-and-cash transaction needs a gateway to take the cash leg. **In Hong Kong, Jakarta, the US and the UK there is none** | [Brilliant FAQ](https://www.brilliantbylangham.com/en/faq) + my own API queries |
| 3 | 2026 | **WeChat Mini-Program confirmed as a third booking channel:** *"You can only earn points from reservations booked via our website, app and WeChat Mini-Program"* | A separate payment surface, almost certainly on WeChat Pay, outside the SynXis booking engine entirely. **I could not reach or inspect it** | [Brilliant FAQ](https://www.brilliantbylangham.com/en/faq) |

*No provider removals found.* **No REMOVAL events to flag.** No Langham-specific payment press, partnership or integration announcement found in thepaypers, finextra, pymnts, techinasia or e27.

---

## Section 8: Checkout Experience Audit

**Scope statement, stated plainly: I audited the booking engine's architecture, configuration and payment code from its own HTTP headers, HTML, GraphQL CMS, availability API and all 40 JavaScript chunks. I did NOT walk the flow through to the card-entry screen, because doing so requires creating a real reservation at a real hotel. I declined to do that.** Everything below that is marked *Not observable* is marked so for that reason, not because a tool was blocked. WebFetch and `curl` both worked throughout this run.

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | **Embedded, vendor-hosted fields inside a white-labelled SynXis Next.js booking engine** on `reservations.brilliantbylangham.com` (Akamai). Adyen Drop-in mounts into `#dropin-container`; Cybersource Unified Checkout injects its `clientLibrary` with SRI into `#embeddedPaymentContainer` | **Good** (ANZ) / **N/A** (28 properties — there is no online payment step) | `[Source Code]` |
| Guest checkout | **Supported.** `setAnonBooking` and an `anonBooking` session key exist alongside the member flow; OTP generate/validate endpoints gate member actions, not booking | Good | `[Source Code]` |
| Steps to complete payment | **ANZ:** search → rooms → enhance (add-ons) → guest_details → **PAYMENT_DETAILS tab** → confirmation. **Everywhere else:** search → rooms → enhance → guest_details (card captured as *guarantee*) → confirmation, **with no payment step** | Fair / **Poor** | `[Source Code]`, route manifest |
| Card input experience | **ANZ:** tokenised vendor-hosted fields (Adyen `encryptedCardNumber`/`securityCode`; Cybersource Unified Checkout). **28 properties:** raw card fields in Langham's own form, validated client-side against `paymentTypesAccepted`, posted to Langham's API as a guarantee | Good / **Poor** | `[Source Code]` |
| Payment methods visible | **Cards only, at all 33 properties.** Per-property scheme mix from the CMS. ANZ gateway-rendered APMs **not observable** without completing a booking | **Poor** | Section 4 |
| Location-based method display | **None.** Methods are keyed to the **property's** country, not the **guest's**. An Indonesian guest booking Jakarta and an American guest booking Jakarta see the same card list and the same emailed-payment-link flow | **Poor** | `[Source Code]` + CMS |
| Instalment / EMI options | **NOT FOUND anywhere.** No instalment configuration in the CMS. Relevant in Japan, Taiwan, Thailand and India per the APAC reference — and this is a high-ticket category (The Langham New York ADR US$902; Shanghai Xintiandi CNY1,553) | **Poor** | CMS |
| 3DS implementation | **Not observable.** `threeDS`/`ThreeDS` strings exist only inside the bundled Adyen SDK — generic, not configuration. Both Adyen Sessions and Cybersource Unified Checkout support 3DS2 natively; **whether it is enabled, and in what mode, is not established** | Unknown | — |
| PCI indicator | **ANZ: vendor-tokenised fields → reduced scope.** **28 properties: card data entered into Langham's own form on their own origin, posted to their own API.** CSP is `form-action 'self' https:` — permissive, and consistent with card data reaching Langham's server | **ANZ Good / rest a real question** | Section 9 |
| Mobile responsiveness | **69.82% of booking-domain traffic is mobile web.** The engine is a responsive Next.js app with explicit mobile breakpoints (`px-4 md:px-0`) and a UserWay accessibility widget. Rendered mobile UX **not visually verified** | Likely Good, unverified | SimilarWeb (supplied) + `[Source Code]` |
| Multi-currency / local pricing | **Property currency is fixed** (AUD, NZD, HKD, IDR, CNY, THB, USD, GBP, CAD — confirmed per property). A **guest-facing display-currency selector** exists (`userSelectedCurrency`, `GET /currency/rates`) and `GET /location/me` geolocates the visitor. **Settlement appears to be in property currency; display conversion is cosmetic** `[INFERENCE, not confirmed]` | Fair | `[Source Code]` |
| Saved payment methods | **Not observable.** Member profile endpoints exist (`/member/profile`, `/member/reservations`); no card-on-file or stored-credential logic found in the client bundle | Unknown | — |
| Error message clarity | **Generic.** Both handlers fall back to one i18n string, `error.payment_refused` → *"Payment was refused"*, with the vendor's reason only `console.error`-logged. No decline-reason surfacing, no retry guidance, no alternative-method prompt | **Poor** | `[Source Code]` |

**The finding that matters most in this section:** for 28 of 33 properties **there is no checkout to audit.** The booking engine collects a card as a guarantee and hands the commercial transaction to the property.

---

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|---|---|---|
| PCI DSS Level | **Not found.** No PCI statement on any reachable Langham or Great Eagle page, and no mention in the FY2025 or H1 2026 results announcements | — |
| Card data handling | **Split, and that is the finding.** **ANZ (4 properties):** likely **SAQ A / A-EP** — Adyen Drop-in and Cybersource Unified Checkout both host the card fields and tokenise. **28 properties:** card number, expiry and CVV are entered into Langham's own form on Langham's own origin and posted to Langham's own API as a guarantee, with CSP `form-action 'self' https:` — **that is a materially wider scope**, and the data then has to reach the property's PMS somehow | `[Source Code]`; CSP header on `reservations.brilliantbylangham.com` |
| Recommended Yuno integration | **For ANZ: SDK** (drop-in replacement for the existing tokenised flow). **For the 28 gateway-less properties the question is not which integration — it is whether a central online payment flow should exist at all.** That is a build decision Langham has not visibly made | Analyst view |

*No direct PCI compliance documentation found publicly for Langham Hospitality Group.*

> `[INFERENCE, not confirmed]`: Based on confirmed use of Adyen Drop-in and Cybersource Unified Checkout at the four ANZ/Toronto properties, PCI scope for those is likely reduced, with the gateway handling card data. **No equivalent inference can be made for the other 28** — and the combination of self-hosted card fields, `form-action 'self'`, and prepayment settled by emailed links sent from property mailboxes is worth asking about directly. **Not asserting a deficiency; asserting that nobody has published an answer.**

---

## Section 10: Strategic Insights & Outreach Angles

> ### **Insight #1: The group cannot take an online payment anywhere in Asia — including at its own headquarters**
> **Evidence:** **Section 3A** — 28 of 33 properties return `paymentGateway: ""` from their own availability API, including all five Hong Kong hotels, all twelve Mainland China hotels, Jakarta and Bangkok. **+ Section 4** — the Hong Kong prepaid rate reads *"The credit card is for guarantee purpose only. A secured payment link will be sent to you in a separate e-mail"*, and the Jakarta prepaid rate names a property mailbox, `tljkt.reservation@langhamhotels.com`. **+ Section 1** — those markets carry **16.01%** of booking-domain traffic between Hong Kong and Indonesia alone, from a total APAC visible share of **44.53%**.
> **Pain Point:** Every prepaid Asian booking becomes a manual task for a hotel reservations team: send a link, wait, chase, cancel if unpaid (*"Bookings without payment confirmation will be automatically cancelled"*). That is abandonment the group never sees as a decline, cash conversion measured in days, inconsistent brand experience across a luxury portfolio, and card data moving through email threads. Meanwhile the same guest can prepay instantly for Melbourne.
> **Yuno Value Proposition:** One integration giving every property the online acceptance ANZ already has, with per-market acquiring and local rails behind it — QRIS and virtual account in Indonesia, FPS and wallets in Hong Kong, PromptPay in Thailand — without the group integrating any of them one by one, and without each property negotiating its own gateway.
> **Best Success Case:** **Qatar Airways** — high-ticket travel, many markets, many acquiring relationships. *(Nameable; no published metrics — attach no number.)* Caveat honestly that no Yuno public case has this per-property merchant-of-record structure.
> **Outreach Angle:** "Your Melbourne guest pays at booking. Your Hong Kong guest gets an email with a payment link. Both are booking on langhamhotels.com — is that deliberate, or just how the estate grew?"
> **Suggested Subject Line:** "Hong Kong prepayment by email, Melbourne by card"

> ### **Insight #2: Two gateways for three Australian hotels, and no failover between them**
> **Evidence:** **Section 3A** — The Langham Sydney and Melbourne return `paymentGateway: "cybersource"`; The Langham Gold Coast returns `"adyen"`; Cordis Auckland `"cybersource"`. **+ Section 3A code** — their own booking engine resolves `v = d ? {provider:"adyen"} : c ? {provider:"cybersource"} : {provider:null}`: **one gateway per session, chosen by static per-hotel config, with no cascade and no retry.** **+ Section 1** — Australia is **24.08%** of booking traffic, second only to the US and the **only** market where money is actually taken at booking.
> **Pain Point:** Two PSP relationships, two sets of commercials, two reporting surfaces and two reconciliation paths — for four hotels. And no failover in either direction: if the configured gateway declines or is unavailable, the booking fails, on the group's highest-value direct-booking market. On a luxury ADR (Sydney A$541, Melbourne A$333) each lost authorisation is a direct revenue number.
> **Yuno Value Proposition:** Keep both Adyen and Cybersource, put routing and cascade in front of them. Retry a soft decline on the second acquirer, route by card origin — Australia's inbound mix includes UnionPay, JCB and Amex, all configured — and consolidate reporting into one view across both.
> **Best Success Case:** **Avianca / Copa Airlines** — multi-acquirer travel operators where routing and retry were the mechanism. *(Nameable; no figures.)*
> **Outreach Angle:** "Sydney and Melbourne run one gateway, Gold Coast runs another, and nothing fails over between them. Four hotels, two PSPs, no redundancy."
> **Suggested Subject Line:** "Gold Coast is on a different gateway to Sydney"

> ### **Insight #3: A flat 2.5% surcharge on every card scheme is a pricing decision standing in for a routing capability**
> **Evidence:** **Section 1 / Quick Look** — Cordis Auckland is the **only** property in the 33-hotel CMS with a `transactionFees` entry, and it applies **2.50% identically to Visa, Mastercard, Amex, UnionPay, JCB, Diners and Discover**. **+ Section 4** — their own rate terms state it twice: *"Credit card payments incur a 2.50% surcharge."* **+ Section 1** — Cordis Auckland is their largest property outside Toronto at **641 rooms, 72.9% occupancy**, ~**14,200 room nights a month**, and ANZ EBITDA grew **24.3%** in H1 2026 on only **4.6%** revenue growth — a margin-sensitive region.
> **Pain Point:** A single blended surcharge across every scheme means acceptance cost is not being differentiated at all — a domestic Mastercard and an international Amex are priced the same to the guest. That is a conversion tax on a luxury booking, visible at the worst moment, and it is a proxy for not having per-scheme routing or least-cost logic. `[INFERENCE, not confirmed]` that it reflects a single blended MDR.
> **Yuno Value Proposition:** Route by scheme, issuer geography and cost so the surcharge can be reduced or differentiated rather than applied flat — and show the delta per scheme rather than arguing it.
> **Best Success Case:** Cost-of-acceptance framing lands most directly in ANZ, the most "Western-looking" stack in the territory per `.claude/reference/apac-payments.md` §2. ⚠️ **Do not cite RBA least-cost-routing expectations — I did not source them this run.**
> **Outreach Angle:** "Cordis Auckland charges 2.5% on every card, same rate for a domestic Mastercard as for an international Amex. It's the only property in your estate with a surcharge at all."
> **Suggested Subject Line:** "2.5% flat, every scheme, Cordis Auckland"

> ### **Insight #4: Bangkok is taking bookings right now with no way to charge for them — and the CRS vendor is selling the fix**
> **Evidence:** **Section 6** — The Langham, Custom House, Bangkok opens late 2026 and is **live in the CRS today**: hotelCode 99801 quotes THB inventory for December 2026 and February 2027 with **`paymentGateway: ""`**, cards only, **no PromptPay**. **+ Section 3B / Section 7** — Sabre launched **SynXis Pay** on 3 March 2025 with **CellPoint Digital** orchestration and "over 250 alternative payment methods", native to the SynXis Booking Engine Langham already runs. **+ Section 6** — Kuala Lumpur follows by end-2027, and third-party managed hotels went 14 → 15 in six months.
> **Pain Point:** Every new market inherits the same gap, and the per-property configuration model means it compounds with each opening. Thailand launches card-only in a PromptPay market; Malaysia will launch without FPX unless something changes. There is a decision window here — new-property onboarding is exactly when acceptance gets configured — and it is closing, because the incumbent CRS vendor has an orchestrator on the shelf and the relationship to place it.
> **Yuno Value Proposition:** Set the pattern once at Bangkok rather than retrofitting 33 properties later. Global PSP and APM breadth, per-market acquiring, and reach the CRS vendor's bundled layer was not built for — argued on coverage, not on the case for orchestration.
> **Best Success Case:** **Qatar Airways** for multi-market travel acceptance. *(Nameable; no figures.)*
> **Outreach Angle:** "Bangkok is quoting THB rates for December right now and there's no gateway behind it — no PromptPay, no way to take the deposit the rate terms ask for. Kuala Lumpur is next."
> **Suggested Subject Line:** "Bangkok is bookable. It isn't payable."

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. "Your Melbourne guest pays by card at booking; your Hong Kong guest gets an emailed payment link from the reservations team — same website, 28 of your 33 properties on the second flow."
2. "Sydney and Melbourne are on one gateway, Gold Coast on another, and your booking engine has no fallback between them — four hotels, two PSPs, no redundancy."
3. "Indonesia is your fourth-largest booking market at 10.79% of traffic, and the Jakarta checkout accepts five card brands and nothing else — no QRIS, no virtual account, no wallet."

**Cold call openers (conversational, one sentence each):**
1. "I pulled your booking engine's availability response for all 33 properties — four come back with a payment gateway configured and twenty-eight come back empty. Is that deliberate?"
2. "Your Hong Kong prepaid rate says the card is for guarantee only and a payment link will follow by email — who owns that process, the hotel or the group?"
3. "Bangkok is already quoting December rates in baht with no gateway behind it — is the payment setup part of the opening plan, or does that get sorted after?"

---

## Section 11: Similar Companies & Prospecting Pipeline

### 11A. Direct Competitors (luxury hotel operators, APAC-weighted)

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---|---|---|---|---|---|---|
| **Mandarin Oriental Hotel Group** | mandarinoriental.com | 🇭🇰 Hong Kong | ~40 hotels | HK, China, UK, US, AU, Thailand | ✅ **Datatrans + Stripe**, booking on **be.synxis.com**. CSP allowlists `pay.datatrans.com`, `pay.sandbox.datatrans.com`, `*.stripe.com`; homepage links `be.synxis.com`. **Two PSPs, same CRS as Langham, but vanilla SynXis host** `[Source Code]` | `curl -D - https://www.mandarinoriental.com/en` (my own check, 2026-10-09) |
| **The Peninsula Hotels** (HK & Shanghai Hotels) | peninsula.com | 🇭🇰 Hong Kong | ~10 hotels | HK, China, Japan, UK, US, France | **Not established** — site returns HTTP 403 behind Cloudflare to both tools | attempted 2026-10-09 |
| **Rosewood Hotel Group** (New World) | rosewoodhotelgroup.com | 🇭🇰 Hong Kong | ~40 hotels | HK, China, SEA, US, Europe | **Not established** — no booking or payment host exposed on the homepage | attempted 2026-10-09 |
| **Shangri-La Group** | shangri-la.com | 🇭🇰 Hong Kong | ~100 hotels | China, HK, SEA, Australia, Middle East | **Not established** — Cloudflare-fronted, no payment host in homepage HTML | attempted 2026-10-09 |
| **Banyan Tree Holdings** | banyantree.com | 🇸🇬 Singapore | SGX-listed | Thailand, China, Indonesia, Maldives | ⚠️ **SynXis booking engine** (`be.synxis.com` in homepage HTML). **PSP not established** | `curl https://www.banyantree.com/` (my own check) |
| **Aman Resorts** | aman.com | 🇸🇬 Singapore | ultra-luxury | Japan, China, Indonesia, Thailand | **Not established** | — |
| **Swire Hotels** | swirehotels.com | 🇭🇰 Hong Kong | House Collective + EAST | HK, Beijing, Chengdu, Shanghai, Miami | **Not established** — the URL I tried returned 404 | [HospitalityNet](https://www.hospitalitynet.org/organization/17012028.html) `[search summary]` |
| **Dusit International** | dusit.com | 🇹🇭 Thailand | Dusit Thani et al. | Thailand, China, Middle East | **Not established** — HTTP 403 | attempted 2026-10-09 |

### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---|---|---|---|---|---|
| Minor Hotels | minorhotels.com | Hotels (Anantara, Avani, NH) | Thailand, SEA, Europe | Multi-brand, multi-currency, heavy managed/franchised mix — the same merchant-of-record ambiguity | `accounts/apac-tal.csv` |
| Indian Hotels Company (Taj) | ihcltata.com | Luxury hotels | India, overseas | Luxury, high-ticket, India e-mandate and UPI exposure Langham has none of | `accounts/apac-tal.csv` |
| The Oberoi Group (EIH) | oberoihotels.com | Luxury hotels | India | Same structural question, in a market with UPI as the default rail | `accounts/apac-tal.csv` |
| Six Senses (IHG) | sixsenses.com | Luxury resorts | Asia, Europe | Brand operator under a larger parent — payments decided above the brand | `accounts/apac-tal.csv` |
| The Ascott (CapitaLand) | discoverasr.com | Serviced apartments | Asia, Europe | Longer stays, higher ticket, per-property settlement | `accounts/apac-tal.csv` |
| Park Hotel Group | parkhotelgroup.com | Hotels | Singapore, China, Japan, AU | Owner-operator, APAC-only — a cleaner single-stack target | `accounts/apac-tal.csv` |
| Marina Bay Sands | marinabaysands.com | Integrated resort | Singapore | Single-site, very high transaction volume — the inverse profile and a better ICP fit | `accounts/apac-tal.csv` |
| Little Hotelier / SiteMinder | littlehotelier.com | Hospitality SaaS + payments | ANZ, SEA, EMEA | **Already researched in this repo at 20/29 ⭐** — publicly committed to "multi-payment gateway". The *platform-layer* version of this account | `2-ready-to-outreach/little-hotelier.md` |

### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---|---|---|---|---|
| **Sabre Hospitality** (vendor, not a hotel group) | **CellPoint Digital**, as the orchestration layer inside **SynXis Pay** | 3 Mar 2025 | Hotel CRS / booking engine | [Travolution](https://www.travolution.com/news/travel-sectors/accommodation/sabre-hospitality-introduces-synxis-pay/) |

*No public case studies found of direct competitors adopting payment orchestration.* **No ICP point awarded** — the only confirmed adopter is Langham's own CRS vendor, which is a supply-chain fact and a competitive threat, not a peer-pressure signal. **Mandarin Oriental running Datatrans + Stripe is two direct PSPs, not orchestration** — do not represent it as orchestration in outreach.

### 11D. Prospect Scoring — **Mandarin Oriental Hotel Group** (the strongest comparable, already TAL row)

| Signal | Points | Status | Evidence Source |
|---|---|---|---|
| Monthly transaction count | 0 | ⬜ Not researched | — |
| Orchestration status | **+4** | ✅ None detected — two direct PSPs (Datatrans, Stripe) | CSP on `mandarinoriental.com`, my own check 2026-10-09 |
| 3+ countries | **+3** | ✅ ~40 hotels across Asia, Europe, Americas, Middle East | `accounts/apac-tal.csv` |
| **Multiple PSPs** | **+3** | ✅ **Datatrans AND Stripe, both in the live CSP** | ibid. |
| Local rail gap in a top-3 market | 0 | ⬜ Traffic profile not pulled | — |
| Recent expansion | 0 | ⬜ Not researched | — |
| Payment issues | 0 | ⬜ Not researched | — |
| Funding >$10M | 0 | ❌ Jardine Matheson subsidiary | `accounts/apac-tal.csv` |
| High traffic outside home | 0 | ⬜ No traffic data | — |
| Competitor using orchestration | 0 | ⬜ Not confirmed | — |
| Payment job postings | 0 | ⬜ Not researched | — |
| **Partial total** | **10 / 29** | 🟢 **Medium on partial research only** | **Not a full score — most rows unresearched** |

**Why Mandarin Oriental screens better than Langham on the same two PSPs:** Datatrans and Stripe are a *central* pair on the brand's own domain, not two per-property gateway configs for four hotels. ⚠️ **Unverified** whether MO settles centrally — the same structural question applies and needs the same test.

### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|---|---|---|---|---|---|---|---|
| 1 | **Mandarin Oriental Hotel Group** | Direct competitor | HK, China, UK, US, AU, Thailand | **10/29 partial** | 🟢 Medium | **Datatrans + Stripe confirmed in live CSP; SynXis CRS** | ✅ Yes |
| 2 | **Marina Bay Sands** | Peer | Singapore | Not scored | 🟢 | Single-site, very high transaction volume — the volume Langham lacks | ✅ Yes |
| 3 | **Minor Hotels** | Peer | Thailand, SEA, Europe | Not scored | 🟢 | Multi-brand, multi-currency, dozens of markets | ✅ Yes |
| 4 | **Indian Hotels Company (Taj)** | Peer | India | Not scored | 🟢 | India UPI + e-mandate exposure | ✅ Yes |
| 5 | **Banyan Tree Holdings** | Direct competitor | Thailand, China, Indonesia | Not scored | 🟢 | **SynXis booking engine confirmed** — same per-property gateway question | ✅ Yes |
| 6 | **Shangri-La Group** | Direct competitor | China, HK, SEA, AU | Not scored | 🟢 | ~100 hotels, largest APAC luxury footprint | ✅ Yes (listed under OTAs — **miscategorised, should be Hospitality & Lodging**) |
| 7 | **The Peninsula Hotels** | Direct competitor | HK, China, Japan | Not scored | 🟢 | HK-based peer, same ownership-plus-operator structure | ✅ Yes |
| 8 | **Rosewood Hotel Group** | Direct competitor | HK, China, SEA, US | Not scored | 🟢 | HK-based, New World-owned | ✅ Yes |
| 9 | **🆕 Swire Hotels** | Direct competitor | HK, Beijing, Chengdu, Shanghai, Miami | Not scored | 🟢 | **NOT IN TAL — genuine find.** HK-based operator, House Collective + EAST, same city and same owner-operator shape as Langham | ❌ **No** |
| 10 | **🆕 Regal Hotels International** | Adjacent | HK, Shanghai, Barcelona | Not scored | 🟡 | **NOT IN TAL.** HK-listed, Regal/Regala/iclub brands; ⚠️ sources disagree on scale (25 hotels/10,000 rooms vs 6,800 rooms vs 9,400 rooms) — verify before adding | ❌ **No** |

**Genuine finds not on the target account list — all Hong Kong hotel operators, the sub-vertical this account sits in:** **Swire Hotels**, **Regal Hotels International**, **Miramar Group**, **Nina Hospitality (Chinachem)** and **Sino Hotels (Holdings) Ltd**. ⚠️ Only Swire and Regal have any sourcing above; Miramar, Nina and Sino are names with no verified property counts and should be researched before being added. **Also worth flagging: `Shangri-La` is filed under "Travel & Online Agencies (OTAs)" in the TAL — it is a hotel operator and that row should be recategorised.** And **Great Eagle Holdings (0041.HK), the listed parent, is not a TAL row in its own right** — if the payments buyer sits at group level, that is the entity, not the hotel brand.

---

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|---|---|---|
| **Annual Revenue (USD)** | **Great Eagle Hotels Division FY2025: HK$5,307.1m (+4.4% YoY)** ≈ **US$680m** *(my conversion at HK$7.8/US$1 — the FX rate is not sourced)*. **H1 2026: HK$2,570.8m (+7.6%)**. **By region FY2025:** North America HK$3,001.0m · Europe HK$777.5m · **ANZ HK$766.6m** · Mainland China HK$434.2m · Others HK$327.8m | [Great Eagle 2025 Annual Results](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0303/2026030302294.pdf) · [H1 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0826/2026082601083.pdf) |
| | ⚠️ **This is the owned hotels' trading revenue, not Langham Hospitality Group's own revenue.** LHG is the management company; its revenue is management fee income, which is **not separately disclosed**. The TAL's "~$700M est." is close to the Hotels Division figure but is attached to the wrong entity | Analyst note |
| Hotels EBITDA | **FY2025 HK$1,152.2m (+4.3%)**; **H1 2026 HK$475.0m (+16.3%)**. **ANZ EBITDA H1 2026 +24.3% on +4.6% revenue** — margin-sensitive | ibid. |
| GMV / Gross Transaction Volume | **No public GMV or gross booking value figure found.** Unlike SiteMinder, Langham publishes no system-wide booking value | — |
| **Average Transaction Value (USD)** | **Not published as a transaction value.** Published **ADR** FY2025, local currency: NY US$902 · Chicago US$551 · Sydney A$541 · London £509 · Boston US$498 · Melbourne A$333 · Pasadena US$367 · Eaton DC US$243 · Toronto C$228 · Auckland NZ$221 · Shanghai Xintiandi CNY1,553 · Cordis Hongqiao CNY812 · **The Langham HK HK$1,996 · Cordis HK HK$1,657 · Eaton HK HK$1,145**. **A folio is ADR × length of stay + F&B + spa — not ADR.** ALOS is not published | Great Eagle 2025 results, pp.10 & 14 |
| **Est. Annual Transactions** | **Room nights FY2025, 15 owned + LHI hotels: ~2,014,800** ✅ **DERIVED** from two sourced inputs. Arithmetic: London 380×365×79.6%=110,405 · Boston 312×365×75.2%=85,638 · Pasadena 379×365×63.0%=87,151 · Chicago 316×365×71.6%=82,583 · NY 234×365×84.3%=72,001 · Eaton DC 209×365×65.9%=50,272 · Toronto 1,590×365×74.1%=430,039 · **Melbourne 388×365×85.1%=120,519** · **Sydney 96×365×91.1%=31,921** · **Auckland 641×365×72.9%=170,560** · Shanghai Xintiandi 355×365×86.1%=111,564 · Cordis Hongqiao 392×365×84.1%=120,330 · **Langham HK 498×365×88.6%=161,048** · **Cordis HK 669×365×91.9%=224,406** · **Eaton HK 465×365×92.1%=156,317**. **Excludes the 15 third-party managed hotels (~4,400 rooms) and all 12 other CRS properties, for which no occupancy is published** | Calculated by me from Great Eagle 2025 results, pp.10 & 14 |
| **Monthly transaction count** | **⚠️ NOT FOUND — ASSUMED. [ASSUMPTION — not researched.]** **Billing unit: online card payments authorised at booking, by the merchant of record on `langhamhotels.com`.** Three layers: **(1) ~167,900 room nights/month** ✅ **DERIVED**, both inputs sourced (above). **(2) ~84,000 folios/month** ⚠️ **ASSUMED** — ÷ an **assumed ALOS of 2.0**, which is **not published**; and most of these settle at the property, not online. **(3) The orchestrable figure — online payments at booking — is ~13,500 ANZ folios/month at best** (Melbourne 10,043 + Sydney 2,660 + Auckland 14,213 room nights ÷ assumed ALOS 2.0; Gold Coast has no published occupancy), **and in practice low single-digit thousands**, because only the brand.com-direct share and only `DIRECT_BILL` rate plans charge online — **neither of which is published.** ⚠️ **ASSUMED, therefore it does NOT trigger the under-40,000 auto-reject.** **374,332 monthly visits is NOT 374,332 transactions** — hotel look-to-book is low single-digit percent and I did not source a rate | See the mandatory disclosure in the ICP breakdown |
| Active Customers / Users | **Not published.** Brilliant by Langham membership count not disclosed. **33 properties live in the CRS** (my own GraphQL query); **15 third-party managed hotels, ~4,400 rooms** at Jun-2026 | Langham GraphQL CMS; Great Eagle H1 2026 |
| **Primary Currency** | **Nine settlement currencies confirmed property-by-property:** USD, GBP, CAD, AUD, NZD, HKD, CNY, IDR, THB. Guest-facing display conversion exists via `GET /currency/rates` + `userSelectedCurrency`; **settlement appears to be in property currency** `[INFERENCE, not confirmed]` | My own availability API queries across all 33 properties |
| Top 3 Markets by Revenue | **North America HK$3,001.0m · Europe HK$777.5m · ANZ HK$766.6m** (FY2025, Great Eagle-owned hotels only; Hong Kong's three LHI hotels reported separately at **HK$1,575.3m** hotel-portfolio revenue `[search summary only — LHI filing not fetched]`) | Great Eagle 2025 results |
| Billing channel split (web vs app store) | **N/A — not a subscription or app-store business.** The relevant split is **direct (brand.com + app + WeChat Mini-Program) vs OTA/GDS/corporate/walk-in, and it is NOT PUBLISHED.** This is the single most important unknown in sizing the account | Analyst note |

---

### Overall Research Confidence

**Medium-High** — unusually high on the question that matters, low on the question needed to size it.

**Very strong coverage (primary evidence I generated myself, 2026-10-09):**
- **Sections 3, 4, 8, 9 — the payment stack.** I enumerated all 33 properties from Langham's own GraphQL CMS, queried the live availability API for each, read the `paymentGateway` field per property, extracted the per-property `paymentTypesAccepted` and `transactionFees`, pulled the CSP from the booking host, and read the payment logic out of all 40 JavaScript chunks. **This is primary, reproducible, first-party evidence, not inference.** It settles the central structural question definitively.
- **Sections 1, 2, 6, 12 — financials and footprint.** Great Eagle's FY2025 and H1 2026 results announcements downloaded from HKEXnews and text-extracted by me, giving audited-basis revenue, EBITDA and per-hotel rooms/occupancy/ADR/RevPAR.

**Weak coverage, and why:**
- **Section 5 (complaints)** — thin, and structurally so: payment happens by email or at the desk, which does not generate public checkout complaints. No consumer app store presence found to mine.
- **Section 2 (entity registration numbers)** — **nothing found in any jurisdiction.** The terms and privacy policy, which in APAC usually name the billing entity, returned **HTTP 403 to both WebFetch and `curl`** on `langhamhospitalitygroup.com`. This is the one place the environment genuinely blocked me.
- **Section 11 (competitor stacks)** — Peninsula, Dusit (403), Shangri-La, Rosewood and Aman all unestablished. Only Mandarin Oriental and Banyan Tree yielded evidence.
- **Regulatory** — **no APAC regulatory claim is made anywhere in this report.** I did not find current primary sources for Bank Indonesia PJP licensing, Australian PayTo merchant adoption, or RBA least-cost-routing expectations, so I cited none and scored no point on any of them. The checklist items are in Manual Research Recommendations.

**Traffic data: SUPPLIED, not estimated.** `accounts/traffic/langham-hospitality-group.md`, SimilarWeb PRO, Sep 2026, supplied by Prateek 2026-10-09, used verbatim and not re-researched. It is a **top-10-per-domain cut**, so APAC totals are visible floors. The country profile drives the APM analysis and two ICP signals, and it is as reliable as the supplied sheet.

**Tooling note — one downgrade factor:** **No Agent/Task tool exists in this environment**, so the method's five-agent Phase 1/Phase 2 fan-out could not be run. I executed all phases directly. Search breadth is comparable; the loss is parallel depth on Sections 5, 6, 7 and 11, which are the weakest sections here. **WebFetch and `curl` both worked** — Section 8 is limited by my refusal to create a real reservation, not by the network.

---

### Manual Research Recommendations

> **Area:** **Monthly transaction count and the direct-vs-OTA booking split** — ICP row 1, and Section 12.
> **Why it matters:** It is the only ICP signal that can reject the account, and it is currently **ASSUMED**. The orchestrable figure may be as low as low-single-digit thousands a month. No business case can be built without it.
> **Suggested manual action:** On the first call, ask three questions: (1) what share of room revenue comes through brand.com, the app and the WeChat Mini-Program versus OTA, GDS and corporate; (2) average length of stay; (3) how many *online* card authorisations the group takes a month, group-wide. If direct share is under ~20%, stop.

> **Area:** **WHERE THE CARD SETTLES — merchant of record per property.** Section 2, Section 3A.
> **Why it matters:** My evidence is conclusive that **28 of 33 properties have no online gateway** and take the card as a guarantee. What it cannot tell you is who the merchant of record is when the property charges it — the hotel's own entity, the owner's entity, or a Langham entity — and therefore **who can sign a payments contract.** This decides whether there is one deal, 33 deals, or none.
> **Suggested manual action:** Get the group's booking terms and privacy policy — they returned **HTTP 403** to me on `langhamhospitalitygroup.com/en/terms-and-conditions/` and `/privacy-policy/`. Read them from a normal browser. Then ask directly: "when The Langham Hong Kong charges a prepayment, whose merchant ID is it on?"

> **Area:** **The Indonesia traffic anomaly** — 10.79%, ~40,400 visits/month, one 223-room third-party-owned hotel.
> **Why it matters:** It is the second-largest APAC signal on the account and **I could not explain it.** If those visitors are Indonesians booking Langham properties abroad, the pain is outbound cross-border acceptance. If they are booking Jakarta, there is a QRIS/VA gap worth a conversation. If it is non-human traffic, the 10.79% is not a payments signal at all. The three readings point to three different pitches.
> **Suggested manual action:** Pull SimilarWeb landing-page and engagement detail for Indonesian traffic on `langhamhotels.com`. Low pages-per-visit and high bounce on the homepage suggests (c); traffic landing on the Jakarta property pages suggests (b); traffic on Hong Kong, Sydney or Shanghai property pages suggests (a).

> **Area:** **Which APMs are switched on at the ANZ gateways.** Section 4.
> **Why it matters:** Adyen Drop-in and Cybersource Unified Checkout both render the method list **server-side from the vendor's dashboard**. Langham's CMS says cards only, but the gateway could be serving Apple Pay, Google Pay or PayTo at the four ANZ properties and **nothing in their own code would show it.** The repo has already published one false claim from exactly this trap. Do not assert an ANZ APM gap until this is checked.
> **Suggested manual action:** Walk the Sydney (Cybersource) and Gold Coast (Adyen) booking flows on a real browser to the payment step — DevTools open, screenshot the rendered method list — then abandon before confirming. Repeat on mobile web, which is 69.82% of traffic.

> **Area:** **Whether Sabre's SynXis Pay has been pitched to Langham.** Sections 3B, 7, 11C.
> **Why it matters:** CellPoint-powered orchestration is native to the booking engine they already run, launched March 2025 and rolling out in phases. If Sabre has already proposed it, Yuno is in a competitive displacement before the first email; if not, there is a window. **I could not establish the current rollout status.**
> **Suggested manual action:** Ask on the call. Also check Sabre's newsroom for a SynXis Pay general-availability update and any named hotel-group reference customers.

> **Area:** **Regulatory position in Indonesia, Thailand and Mainland China.**
> **Why it matters:** `.claude/reference/apac-payments.md` flags all three as markets where domestic acquiring may be gated behind local presence or licensing. **I made no such claim in this report because I could not source one**, and no ICP point rests on it. But if Indonesia or Thailand does gate domestic acquiring, the Jakarta and Bangkok findings become regulatory arguments rather than coverage arguments — a much stronger pitch.
> **Suggested manual action:** Source Bank Indonesia's current PJP licensing categories and the Bank of Thailand / SBV equivalents from the regulators' own sites before any email cites them. **Same for PayTo:** get a dated Australian Payments Plus or NPP Australia merchant-adoption figure, or drop the Australian rail argument entirely.

> **Area:** **Non-room revenue lines** — F&B, Chuan Spa, gift cards and vouchers.
> **Why it matters:** These bill separately and may run on entirely different stacks, which could be larger in transaction count than room bookings even if smaller in value. Great Eagle discloses that **F&B revenue fell 3.6%** at the Hong Kong hotels and softened in Shanghai — so F&B is material enough to report on. **I found no Langham-operated online gift card or voucher store**; third-party spa vouchers are sold via spabreaks.com, and T'ang Court seasonal items were historically ordered by phone or a designated page.
> **Suggested manual action:** Ask what POS the restaurants and spas run (Shiji Infrasys is the common one in this segment and is itself a TAL row) and whether gift cards or vouchers are sold online anywhere in the group.

> **Area:** **The WeChat Mini-Program booking channel.**
> **Why it matters:** Confirmed by their own FAQ as one of only three points-earning channels, and completely outside the SynXis booking engine. It is almost certainly on WeChat Pay and may be the group's only working non-card APM. **I could not reach or inspect it.**
> **Suggested manual action:** Open the Mini-Program from a WeChat account and record what payment methods it offers, and for which properties.

---

### Appendix: All Source URLs

**Supplied data (not re-researched)**
- `accounts/traffic/langham-hospitality-group.md` — SimilarWeb (supplied 2026-10-09), Sep 2026, two domains, top-10 countries each
- `accounts/apac-tal.csv` — Langham row; `Payment Gateway` and `Payment Orchestrator` columns both empty
- `1-to-outreach/langham-hospitality-group.md` — stub; Prateek's hypotheses, verified or dropped in Section 2/3
- `.claude/reference/apac-payments.md` — checklist only; no claim in this report rests on it

**Primary evidence I generated (Langham's own systems, 2026-10-09)**
- `https://reservations.brilliantbylangham.com/?chain=10316&brand=tlhr&locale=en-US&theme=brilliant&config=brilliant&level=hotel` — booking host; CSP read via `curl -D -`
- `POST https://reservations.brilliantbylangham.com/en-US/graphql` — `content.hotels(first:1000)` → 33 properties, `synxisHotelId`, `isLive`, `paymentTypesAccepted{cardType}`, `transactionFees{cardType percent}`
- `POST https://reservations.brilliantbylangham.com/api/booking/availability` — per-property `paymentGateway`, `currency`, `guarantee.acceptedPaymentTypes`, `guarantee.description`
- `https://reservations.brilliantbylangham.com/_next/static/chunks/pages/_app-661c61301c46b67b.js` — gateway/DIRECT_BILL logic, session keys, API base, CSP builder
- `https://reservations.brilliantbylangham.com/_next/static/chunks/pages/booking/guest_details-dc3a024a5e185881.js` — Adyen Drop-in mount, Cybersource Unified Checkout, provider mutual exclusivity
- `https://reservations.brilliantbylangham.com/_next/static/chunks/3237-597da73056e6ea57.js` — bundled Adyen Web SDK (generic APM enum — **discarded as evidence**, see Section 3A)
- `https://www.langhamhotels.com/en/` — homepage; RESERVE links to the booking host
- `https://www.langhamhotels.com/en/terms-and-conditions/` — **302 → `langhamhospitalitygroup.com`**
- `https://www.langhamhospitalitygroup.com/en/terms-and-conditions/` and `/privacy-policy/` — **HTTP 403, not readable**
- `https://www.langhamhotels.com/en/the-langham/bangkok` — Bangkok property page

**Great Eagle Holdings / HKEX filings (downloaded and text-extracted by me)**
- `https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0303/2026030302294.pdf` — 2025 Annual Results Announcement (Stock Code 41) — Hotels Division revenue/EBITDA by region, per-hotel rooms/occupancy/ADR/RevPAR (pp.10, 14)
- `https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0826/2026082601083.pdf` — H1 2026 Interim Results — Hotels Division H1 figures; 15 managed hotels / ~4,400 rooms
- `https://www.hkexnews.hk/listedco/listconews/sehk/2026/0311/2026031100732.pdf` — LHI (1270) filing `[referenced via search summary; not fetched]`
- `https://www.greateagle.com.hk/` — investor relations

**Company / loyalty**
- `https://www.brilliantbylangham.com/en/faq` — points earning channels incl. WeChat Mini-Program; Points Plus Cash
- `https://en.wikipedia.org/wiki/Langham_Hospitality_Group` — Langham Hotels International Ltd; 2003 rename; Great Eagle ownership

**Payment industry / vendor**
- `https://www.travolution.com/news/travel-sectors/accommodation/sabre-hospitality-introduces-synxis-pay/` — SynXis Pay, CellPoint Digital orchestration, 3 Mar 2025 **(fetched)**
- `https://preferrednet.net/revenue-distribution/products-services/protool-payment-gateway/` — SynXis gateway certification context `[search summary only]`

**Competitors (my own checks, 2026-10-09)**
- `https://www.mandarinoriental.com/en` — CSP: `pay.datatrans.com`, `pay.sandbox.datatrans.com`, `*.stripe.com`; `be.synxis.com`
- `https://www.banyantree.com/` — `be.synxis.com`
- `https://www.peninsula.com/`, `https://www.dusit.com/` — HTTP 403 · `https://www.shangri-la.com/en/`, `https://www.rosewoodhotels.com/` — no payment host exposed
- `https://www.hospitalitynet.org/organization/17012028.html` — Swire Hotels brands `[search summary]`
- `https://www.regalhotel.com/en/about-us`, `https://beltandroad.hktdc.com/en/node/59454` — Regal Hotels, conflicting scale figures `[search summary]`

**Expansion / corporate**
- `https://www.sleepermagazine.com/stories/projects/langham-to-open-bangkok-riverside-retreat/` · `https://robbreport.com.sg/the-langham-custom-house-bangkok/` · `https://hospitalitynet.org/announcement/41011497.html` — Bangkok `[search summaries]`
- `https://www.luxurytraveladvisor.com/hotels/langham-jakarta-opens-its-doors` · `https://www.ttgasia.com/2013/11/15/langham-hospitality-group-moves-into-jakarta/` — Jakarta: 223 rooms, Agung Sedayu Group `[search summaries]`
- `https://www.businesstraveller.com/news/brilliant-by-langham-refreshed/` — **HTTP 403, `[UNVERIFIED — search summary only]`**
- `https://www.breakingtravelnews.com/news/article/nils-arne-schroeder-named-chief-operating-officer-of-langham-hospitality-gr/` — COO appointment `[search summary]`

**Complaints**
- `https://www.venuescanner.com/gb/venues/london/london/book/the-langham-hotel-london/the-terrace-garden` — isolated billing dispute `[search summary]`

</details>
