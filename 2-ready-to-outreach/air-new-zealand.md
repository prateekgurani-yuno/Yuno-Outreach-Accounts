# Air New Zealand

**Status:** 🟢 Ready to outreach — sequence drafted
**ICP Score:** 16 / 24 → ⭐ High Priority
**Industry:** Airlines · **HQ:** Auckland, New Zealand · **Researched:** 2026-09-14 · **First email sent:** —
**Motion:** Greenfield — no orchestrator detected

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** New Zealand's national carrier, 51% Crown-owned, listed on NZX and ASX. Carried **15.9 million passengers** in FY25 on NZ$6.76bn revenue, across a domestic network, trans-Tasman routes and long-haul services to Asia, North America and the Pacific. It runs **19 country storefronts in 11 currencies** off a single global acquiring configuration, has localised its payment rails in exactly **three** of them, and discloses **one** non-NZ incorporated subsidiary.

**SimilarWeb total visits (last full month):** Not shown in the supplied view. Source: SimilarWeb (supplied 2026-09-10), Jun–Aug 2026, `airnewzealand.com` with **"Include all country domains" ON — merged across 23 domains**, so the country profile is group-wide rather than a single-site artefact.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | New Zealand | 67.68% | Cards (Visa/MC/Amex/Diners/JCB/Discover), **POLi** (A2A), Airpoints, Airpoints Flexipay, Air NZ Travelcard, flight credits, vouchers | None material | ✅ Air New Zealand Limited, NZBN 9429040402543 |
| 2 | Australia | 11.15% | Cards, debit card, Air NZ Travelcard, Airpoints | **No A2A rail at all** — POLi named for NZ and absent from the AU paragraph on the same page. No BPAY, no PayTo/PayID | ✅ Air New Zealand (Australia) Pty Ltd + parent ABN 70 000 312 685 |
| 3 | United States | 6.42% | Cards; USD storefront and USD service fees | No PayPal, no Affirm/Klarna found | ❌ no entity in the FY25 subsidiary list |
| 4 | Japan | 2.30% | Credit and debit card only — JP FAQ has zero mentions of konbini, PayPay, Rakuten Pay or instalments | **konbini, PayPay, card instalment/bonus payment** | ⚠️ 法人番号 4700150003018, third-party source only |
| 5 | Taiwan | 1.48% | TWD storefront; no payment help article on the property | ATM/virtual account, convenience-store cash, domestic instalments | ❌ no entity found |

### Legal entities
- **Air New Zealand Limited** (New Zealand) — NZBN 9429040402543, NZX: AIR / ASX: AIZ, registered office 185 Fanshawe Street, Auckland
- **The Crown holds 51.01%** — 1,686,990,261 of 3,306,993,443 ordinary shares at 30 Jun 2025, plus the non-listed "Kiwi Share"
- **Air New Zealand (Australia) Pty Limited** — *the only subsidiary incorporated outside New Zealand* in the entire FY25 disclosure
- Parent registered in Australia: **ABN 70 000 312 685**
- UK: registrations **FC008870 and BR013134 appear CLOSED** `[UNVERIFIED]`, yet a live `.co.uk` storefront sells in GBP
- **No confirmed entity: United States, Singapore, Hong Kong, mainland China, Canada, Taiwan, Indonesia, Thailand, South Korea**

> **Eight currencies of sale. Nineteen storefronts. One non-NZ subsidiary.**

### Known PSPs
- **None named.** Seventeen searches and five fetches produced no acquirer, gateway or orchestrator for any market
- **POLi Payments** — confirmed as an NZ A2A method (Air NZ operates its own POLi help page), not a card PSP
- Multi-currency pricing active on Visa/MC/JCB/Amex/Diners/Discover — **MCP vendor unnamed**
- Amadeus holds a **distribution** agreement — GDS only, no evidence of Amadeus Payment Platform

### Orchestration status
**None detected — no orchestrator evidence found.** CellPoint Digital's published airline roster (Icelandair, Virgin Atlantic, Arajet, Cebu Pacific, Air Europa, Emirates, Oman Air, Riyadh Air, Southwest and others) does **not** include Air NZ. No orchestration SDK in any fetched page. **Not a Yuno customer.**

Positive architectural evidence pointing the same way: Air NZ runs **two booking engines concurrently** — a modern Next.js `/fly/` funnel on `flightbookings.airnewzealand.co.nz` and a legacy `/vbook/actions/` engine on `flightbookings.airnewzealand.jp`, with NZ servicing still on the legacy `/vmanage/actions/`. A unifying orchestration layer is precisely what would collapse that split.

### Buying signals
- 🚀 **Three new international routes from Christchurch** — [Singapore 28 Oct, Tokyo Narita 28 Nov, Perth 30 Nov 2026](https://www.airnewzealandnewsroom.com/press-release-2026-major-international-expansion-set-to-boost-christchurch-and-south-island-growth)
- ⚠️ **FY26 loss before tax of NZ$336m**, against $164m earnings the prior year — a ~$500m swing ([Air NZ newsroom](https://www.airnewzealandnewsroom.com/press-release-2026-air-new-zealand-announces-2026-annual-results)) `[UNVERIFIED — search summary]`. Cost of acceptance lands differently at an airline that just swung to a loss
- 🤝 **A direct competitor consolidated payments in Air NZ's home markets:** [Cathay Pacific expanded to Adyen direct acquiring, March 2026](https://www.adyen.com/press-and-media/cathay-pacific-expands-global-partnership-with-adyen), explicitly covering **New Zealand and Australia**
- 💼 [Economy Skynest™ on sale May 2026](https://www.airnewzealandnewsroom.com/press-release-2026-the-future-of-long-haul-travel-air-new-zealands-economy-skynest-on-sale-from-may) — a new ancillary SKU sold separately from the fare; ancillary revenue grew 15% in FY25
- ⚠️ **A live, self-admitted payment defect on their own help page** — see Section 5

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

### Pain Vector Extraction

**Motion:** Greenfield — no orchestrator detected. Phase 1 may note the absence of a routing layer.

**Observable setup facts** (from research, with sources):
- **19 storefronts across 11 currencies, payment rails localised in exactly 3** — POLi (NZ), SOFORT (EU), Alipay (CN). Probing `/information-about-payment`, `/poli-information` and `/sofort-faqs` across six country properties returned 200 only on `.cn`, `.co.nz` and `.eu` respectively — source: §4
- **Australia, the second-largest market at 11.15%, has no bank rail.** The NZ paragraph on `/fare-rules` names POLi as fee-free; the AU paragraph on the same page names only debit card, Travelcard and Airpoints — source: airnewzealand.co.nz/fare-rules vs airnewzealand.com.au/fare-rules
- **Auckland–Denpasar runs ~7x weekly with no Indonesian storefront, no IDR pricing and no local rail** — source: homepage storefront config, §8
- **China's own published list is Alipay plus Visa/Mastercard/Amex — no UnionPay, no WeChat Pay** — source: airnewzealand.cn/information-about-payment
- **Japan: zero mentions of konbini, PayPay, Rakuten Pay or instalments** in the JP FAQ — source: airnewzealand.jp/faq
- **No orchestrator, no named PSP.** Air NZ absent from CellPoint Digital's published airline roster; two booking engines running concurrently — source: §3B
- **15.9m passengers, NZ$6.76bn revenue FY25**; FY26 swung to a NZ$336m pre-tax loss — source: FY25 Annual Report, newsroom

**Selected observations for Phase 1** (ranked by materiality):
1. Australia has no A2A rail → *"Your NZ fare rules name POLi as a fee-free way to pay. The Australian paragraph on the same page names no bank rail."* — **most material: 11.15% of traffic, second-largest market, and the comparison sits on one page**
2. No native instalment product anywhere → *"No instalment option on any of your own properties. Resellers sell Air NZ seats with Afterpay and Zip on their own merchant record."* — **swapped in 2026-09-15 from Prateek's research doc.** Confirmed and sharpened by §4: no BNPL on any Air NZ property, while Afterpay, Zip, Laybuy, humm, Klarna and Affirm all appear via third-party resellers (Alternative Airlines, Fly Fairly) **off Air NZ's merchant record**. Airpoints Flexipay is points-plus-cash, not credit, and is geo-fenced to NZ and AU. Third parties are earning the instalment demand on Air NZ's own inventory. *(Displaces the Denpasar observation, which stays available for the E5 teardown)*
3. China list omits the domestic rail → *"Your China page lists Alipay and three card schemes. No UnionPay."* — **a sourced absence from an enumerated list, the strongest evidence class available**

**Bridge variant:** A — complexity
**Rationale:** 19 storefronts in 11 currencies, two booking engines running concurrently, and rails localised in three markets is a genuinely fragmented estate. Not variant B: there is no single visible PSP to outscale, because no PSP is visible at all.

**Hypothesis for Phase 2 (E3):**
Most likely pain: payment rails are decided one market at a time, so the sixteen storefronts that never got a local rail run on cards alone, and every provider that does get added arrives with its own reconciliation format.
**Added 2026-09-15 from Prateek's doc:** the reconciliation burden now sits in E3's Yuno line, and E3's backing swaps the Japan detail for the **Qantas contrast** — Qantas publishes PayPal, Zip, BPAY and Alipay on its own payment-options page (§11A, first-party). Two trans-Tasman competitors, both their own public pages, neither half disputable. Stronger than any external benchmark.
Backing logic: three localised rails out of nineteen storefronts is not a strategy, it is a backlog. The `.cn` and `.eu` pages prove the capability exists and has been exercised three times. At airline ticket values the cost of a missing rail surfaces as cart abandonment rather than declines, which is exactly why it survives unnoticed.

**Success case for Phase 3 (E4):**
Selected case: **Wingo** · Tier: **1 (airline, same per-market rail problem)** · Match rationale: an airline that added breadth of methods above an existing stack, which is precisely the shape of Air NZ's gap. Re-verified live on 2026-09-15 against the Yuno press release, which names the mechanism: *"Smart Routing technology helps Wingo maximize its transaction approval rates by enabling automatic retries of failed payments through multiple providers."*
Numbers to lead with: **+14% approval rate** (stated as the initial implementation phase) · **1,000+ payment methods** through one integration · **3D Secure and fraud tooling** on the same layer.
**Airline credibility line, no metrics attached:** Qatar Airways, Copa Airlines and Avianca are all named as Yuno customers on Yuno's own site. They carry the *relationship*, not a number, and E4 uses them exactly that way.
✅ **Corrected on 2026-09-15.** The previous draft's third bullet claimed *"Viva Aerobus, another airline on the same layer, recovered 75% of its failed transactions"* and presented it as a routing result. **That misattributes the mechanism.** Viva Aerobus's 75% comes from NOVA, Yuno's AI voice-callback assistant that phones customers after a failed payment, not from Smart Routing. The bullet has been replaced with Wingo's own 3DS/fraud line and Viva Aerobus moved to the alternatives list, where the mechanism is stated correctly.
Optional benchmark: **SKIP.** The IATA/Edgar Dunn "$20.3bn, 2.1% of industry revenue" airline cost-of-acceptance figure would be ideal here but has only been seen via a vendor blog citing it. Trace it to the primary source before it goes in an email.

**Touch-by-touch angles:**
- E2 angle: Australia's missing bank rail → *one integration to add any method, no per-rail rebuild*
- LK1 angle: the POLi NZ-versus-AU comparison on a single page
- LK2 angle: three of nineteen storefronts localised, and the gaps include markets flown daily
- LK3 angle: Wingo's +14% approval rate, paraphrased rather than repeated from E4
- LK4 angle: **fresh, unused until this point** — Cathay Pacific moved to direct acquiring across NZ and Australia in March 2026, for authorisation rates
- E8 angle: Christchurch–Singapore and Christchurch–Narita going live within two months, door left open

**Source document:** `Air NZ Research` (Google Doc, owner prateek.gurani@y.uno, modified 2026-09-15), read via the Drive connector on 2026-09-15. ⚠️ **The file is 490KB but carries only ~1KB of text — the rest is images, which the connector cannot read.** All five of its text bullets are reflected in this sequence: wallets/BNPL gap → E1 bullet 2; reconciliation → E3; NOVA and the Viva Aerobus 75% → E6; the airline customer list → E4 and LK3. **If the traffic screenshots in that doc say something different from the SimilarWeb split already in §1, that difference has not been seen and is not reflected here.**

**Cadence calendar** (Day 1 = Tue 15 Sep 2026). A Tuesday start is the only weekday start that keeps all nine auto-written touches on business days, bar one:

| Touch | Day | Date | Note |
|---|---|---|---|
| E1 | 1 | Tue 15 Sep | |
| E2 | 3 | Thu 17 Sep | reply in thread |
| LK1 | 5 | **Sat 19 Sep** | ⚠️ **weekend — send Fri 18 or Mon 21 instead** |
| E3 | 7 | Mon 21 Sep | new subject |
| LK2 | 9 | Wed 23 Sep | |
| E4 | 11 | Fri 25 Sep | new subject |
| E5 | 13 | Sun 27 Sep | manual, move to Mon 28 |
| E6 | 15 | Tue 29 Sep | manual |
| LK3 | 17 | Thu 1 Oct | |
| E7 | 19 | Sat 3 Oct | manual, move to Mon 5 |
| LK4 | 21 | Mon 5 Oct | |
| E8 | 23 | Wed 7 Oct | reply in thread |

**Meeting slots — five distinct combos, all Auckland afternoon.** Auckland moves to NZDT (UTC+13) on 27 September, putting it 7h30 ahead of IST, so a New Zealand afternoon is a 7:30–9:30am start for Prateek. Anything earlier in their day is unworkable from India.

| Touch | Proposed | IST equivalent |
|---|---|---|
| E3 | Thursday 24 September, 3pm or 4pm | 08:30 / 09:30 |
| LK2 | Monday 28 September, 4:30pm | 09:00 |
| E4 | Wednesday 30 September, 3:30pm or 4:30pm | 08:00 / 09:00 |
| LK3 | Tuesday 6 October, 3pm | 07:30 |
| LK4 | Thursday 8 October, 4pm | 08:30 |

---

### Phase 1 — Curiosity (Days 1–5)

#### Touch 1 — Email 1 · Day 1 · Tue 15 Sep

**Subject:** No bank rail on your AU checkout

```text
Hey {{recipient.first_name}},

Spent some time on your payment setup. Three things stood out:

- Your NZ fare rules name POLi as fee-free. The Australian paragraph on the same page names no bank rail.
- No instalment option on any of your own properties, but resellers sell your seats with Afterpay and Zip.
- Your China page lists Alipay and three card schemes. No UnionPay.

That kind of setup usually comes with some complexity.

I work at Yuno, a top-100 fintech, a16z-backed. We consider ourselves the "everything payments" platform: one integration, every PSP, every market.

Rather than pitch you on assumptions, is there anything payment-related you're working through?

Best,
Prateek
```

#### Touch 2 — Email 2 · Day 3 · Thu 17 Sep · REPLY IN THREAD

```text
Hey {{recipient.first_name}},

Following up. Wanted to put a bit more behind what Yuno actually does, and how it maps to what I flagged.

We sit above the PSPs you already run, so nothing gets ripped out. Transactions route per market, method and BIN to whichever rail performs best. If a provider degrades, traffic moves across automatically. Adding a new method or acquirer is one integration rather than a per-rail build.

On the Australian gap specifically: putting a local bank rail back on that checkout becomes a configuration change on the layer, not a separate project against a separate provider.

I'll keep sharing what I'm seeing every few days. If your stack's where you want it, just say the word and I'll back off, otherwise happy to go deeper on any of this.

Cheers,
Prateek
```

#### Touch 3 — LinkedIn message 1 · Day 5 · ⚠️ lands Sat 19 Sep, send Fri 18 or Mon 21

```text
Hey {{recipient.first_name}}, figured I'd flag this here too in case it's more useful than email. Quick one: your New Zealand fare rules offer POLi as the fee-free way to pay, and the Australian paragraph on that same page doesn't name a bank rail at all. Curious whether that maps to anything you're working through on the payments side.
```

---

### Phase 2 — Diagnosis (Days 7–9)

#### Touch 4 — Email 3 · Day 7 · Mon 21 Sep · NEW EMAIL

**Subject:** Three of nineteen storefronts

```text
Hey {{recipient.first_name}},

Going to take a swing at this. My read is you've localised payment rails on three of nineteen storefronts, and the rest run on cards alone.

POLi in New Zealand, SOFORT in Europe, Alipay in China. Qantas publishes PayPal, Zip, BPAY and Alipay on its own payment-options page. At your ticket values that tends to surface as cart drop rather than declines.

What decides which markets get a rail?

At Yuno we sit above your existing PSPs, so a rail per market stops being a project per market, and every provider lands in one reconciliation format. Keep your stack, add what's missing.

Thursday 24 September is open. Would 3pm or 4pm your time work for 15 minutes?

All the best,
Prateek
```

#### Touch 5 — LinkedIn message 2 · Day 9 · Wed 23 Sep

```text
Hey {{recipient.first_name}}, sent a longer note over email this week. Short version: you've localised payment rails on three of nineteen storefronts, and the sixteen running on cards alone include markets you fly to daily. If that's anywhere on your radar, would Monday 28 September at 4:30pm your time work for a quick 15?
```

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · Fri 25 Sep · NEW EMAIL

**Subject:** How Wingo solved this

```text
Hey {{recipient.first_name}},

On the read I shared last week, here's what solved tends to look like.

Wingo had the same shape of problem: rails decided one market at a time, with the markets that never got one running on cards alone. They put Yuno above the stack they already had:

- Approval rates up 14%, from automatic retries of failed payments across multiple providers
- Over 1,000 payment methods reachable through one integration (you read that right)
- 3D Secure and fraud tooling on the same layer, nothing rebuilt per market

Same layer above the existing providers, no rip-out. Wingo is a LATAM carrier, so take the 14% as what the pattern does rather than an Asia-Pacific result.

On the airline question more broadly, Qatar Airways, Copa Airlines and Avianca all run on this layer too.

Wednesday 30 September is open. Would 3:30pm or 4:30pm your time work for 15 minutes?

Full case here if useful: https://y.uno/en/newsroom/wingo-improves-payment-efficiency-with-yuno-as-strategic-partner

Cheers,
Prateek
```

#### Touch 7 — Email 5 · Day 13 · MANUAL

*Placeholder — do not auto-write.* Strongest option for this account: a **checkout teardown of one market they fly to and don't serve**. Price AKL–DPS from an Indonesian IP, screenshot the currency and method set an Indonesian customer actually gets, and send it annotated. It converts Insight #1 from an assertion into something they can see. Alternatives: a written business case against the 15.9m passenger base, or a Loom walking the NZ-versus-AU fare-rules pages side by side.

#### Touch 8 — Email 6 · Day 15 · MANUAL

*Placeholder — do not auto-write.* Different format from E5. **Strongest option, and it comes straight from your doc: NOVA.**

Air NZ's own help page documents an unresolved credit-processing defect, so they already carry a population of customers whose payment did not complete. NOVA detects a failed payment and calls the customer automatically; Viva Aerobus recovered **75% of contacted customers** that way. Because that is post-failure recovery rather than routing, it is a clean second act after E4's routing argument instead of a repeat of it, and it is the one place the Viva Aerobus number can be used correctly.

Alternative: the IATA/Edgar Dunn airline cost-of-acceptance study, **traced to the primary source first**, sized against the 15.9m passenger base.

#### Touch 9 — LinkedIn message 3 · Day 17 · Thu 1 Oct

```text
Hey {{recipient.first_name}}, Wingo lifted approval rates by 14% after putting this layer above the stack it already ran, by retrying failed payments across a second provider. Qatar Airways, Copa and Avianca sit on the same layer. Worth 15 minutes to work out whether it maps to yours? Tuesday 6 October at 3pm your time is open on my side.
```

---

### Touch 10 — Email 7 · Day 19 · MANUAL

*Placeholder — do not auto-write.* Manual creative bridge. Freshest available anchors: the **Christchurch international launches** (Singapore 28 Oct, Tokyo Narita 28 Nov), **Economy Skynest** going on sale as a separately-sold ancillary SKU, or the **FY26 result** if the conversation has earned that level of directness.

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21 · Mon 5 Oct

```text
Hey {{recipient.first_name}}, last ping from me on this. One thing I hadn't mentioned: Cathay moved to direct acquiring across New Zealand and Australia in March, specifically for authorisation rates. Thursday 8 October at 4pm your time is open if that's useful.
```

#### Touch 12 — Email 8 · Day 23 · Wed 7 Oct · REPLY IN THREAD to Touch 4 or 6

```text
Hey {{recipient.first_name}},

Going to stop pinging unless you want to pick this back up.

Christchurch to Singapore and Christchurch to Narita both go live in the next two months. If the payment side of those routes ever turns into a question, just reply here.

All the best,
Prateek
```

---

### Source Notes

Every prospect-specific factual claim in the sequence, tagged:

- ✅ **POLi named fee-free in the NZ paragraph, absent from the AU paragraph** — airnewzealand.co.nz/fare-rules and airnewzealand.com.au/fare-rules. Both fetched.
- ✅ **Auckland–Denpasar operates ~7x weekly** — flightsfrom.com schedule data; Air NZ's own destination page still calls it seasonal
- ✅ **No Indonesian storefront** — extracted from Air NZ's own homepage storefront configuration, 19 properties enumerated
- ✅ **China page lists Alipay plus Visa/Mastercard/Amex, no UnionPay** — airnewzealand.cn/information-about-payment, published as static copy
- ✅ **Japan FAQ has no konbini, PayPay or instalment mentions** — airnewzealand.jp/faq, keyword counts all zero
- ✅ **Three localised rail pages across the estate** — 404 probe results across six properties
- ✅ **No native BNPL on any Air NZ property; resellers carry it instead** — §4 of this file: Afterpay, Zip, Laybuy, humm, Klarna and Affirm appear only via Alternative Airlines and Fly Fairly, **off Air NZ's merchant record**; Airpoints Flexipay is points-plus-cash and geo-fenced to NZ/AU. Corroborates the first bullet of Prateek's doc and is the sourced version of it
- ✅ **Qantas publishes PayPal, Zip, BPAY, Alipay and UATP** on its own payment-options page — §11A, `qantas.com/en-au/book/flights/payment-options`. Used in E3 as a competitor contrast, never as an implied Yuno relationship
- ✅ **Wingo +14% approval rate, 1,000+ payment methods, 3DS and fraud tooling** — re-verified live 2026-09-15 by fetching [the Yuno press release](https://y.uno/en/newsroom/wingo-improves-payment-efficiency-with-yuno-as-strategic-partner) (10 Jun 2025) rather than trusting the local case library. The release names the mechanism as Smart Routing with *"automatic retries of failed payments through multiple providers"*, and frames the 14% as the initial implementation phase. URL corrected to the `/en/` path, which is the one that resolves
- ⚠️ **Allegiant Air and Viva Air — named as Yuno customers in Prateek's doc, but NOT used in the written copy.** Neither appears anywhere on y.uno: I grepped every page I pulled (success stories, newsroom, travel vertical, Wingo release) and both returned **zero hits**, while Qatar Airways, Copa, Avianca, Viva Aerobus and Wingo all returned matches. Per the skill's own naming rule, an internally-known relationship that is not publicly referenceable is fine to say **on a call** but is a confidentiality question in writing to a third party. **They are safe for you to mention live; tell me if either is publicly referenceable and I'll add them to E4.** *(Note also that "Viva Air" and "Viva Aerobus" are two different carriers — the y.uno travel list shows only "Viva", which is ambiguous.)*
- ✅ **Qatar Airways, Copa Airlines and Avianca are Yuno customers** — Qatar Airways appears in the site-wide "TRUSTED BY GLOBAL TEAMS" list published on every y.uno page (*"McDonald's, Samsung, Uber, Carrefour, Ant Group, NetEase, Crypto.com, Qatar Airways, Rappi, inDrive, Copa Airlines, Despegar, Garena…"*); Copa Airlines and Avianca additionally appear on the travel and mobility vertical list (*"Trusted by leading travel and mobility brands: Uber, inDrive, Avianca, Copa Airlines, Viva"*). Verified 2026-09-15 on [y.uno/en/success-stories](https://y.uno/en/success-stories). **⚠️ These are customer names only. No published metric exists for any of the three**, so they may be named and nothing more
- ✅ **Viva Aerobus recovered 75% of failed transactions** — Yuno case library
- ✅ **Cathay Pacific moved to Adyen direct acquiring covering NZ and Australia, March 2026** — Adyen press release, first-party. E4 and LK4 name the airline and what it did, never implying a Yuno relationship
- ✅ **Christchurch–Singapore and Christchurch–Narita launching Oct/Nov 2026** — Air NZ newsroom
- ⚠️ **Card surcharge percentages are NOT used anywhere in this sequence.** They rest on trade press because Air NZ's own fee page was proxy-blocked. Do not add them without re-verifying.
- ⚠️ **The Indonesia page-depth anomaly (14.88 pages/visit) is NOT used.** The storefront gap is verified; the causal link to that figure is not, and asserting it would be unsupported.
- ⚠️ **No PSP is named anywhere in this sequence**, because none was identified. E1 and E3 describe the estate, not a vendor. If the manual checkout walkthrough identifies the acquirer, E5 becomes considerably stronger.

### Success Case Alternatives

- **Viva Aerobus** — airline, 75% of *contacted* customers completed their purchase after a callback. ⚠️ **This is a NOVA result, not a routing result**: NOVA is Yuno's AI voice-callback assistant that phones customers after a failed payment. Do not use it to prove a routing or failover argument. It becomes the right case *after* the routing conversation lands, and it is a genuinely strong second act here given the credit-redemption defect on their own help page
- **inDrive** — Tier 2: multi-country acquiring at scale, ~90% approval, 10 countries in 8 months. Use if the conversation moves to market expansion ahead of the Christchurch launches. LATAM results, label them
- **Rappi** — Tier 2: breadth of providers added without implementation delay. Use if they push back that adding rails is an engineering cost
- ✅ **Qatar Airways reinstated 2026-09-15** — the earlier withdrawal was wrong. It was based on a web search returning nothing; y.uno itself was unreachable at the time. The site is now fetchable and Qatar Airways is named on Yuno's own site-wide customer list. **Safe to name, with no number attached.**
- **Copa Airlines / Avianca** — same status: named Yuno travel customers, no published metrics. Useful as additional airline credibility if the thread turns to whether Yuno has carrier experience


</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 16 / 24
| Signal | Points | Status |
|--------|--------|--------|
| Orchestration status | +4 | ✅ **None detected.** CellPoint's airline roster checked and Air NZ is absent; no orchestration SDK found; the dual booking-engine estate is positive evidence against a unifying layer. Caveat: the payment step is session-gated, so this is "no public evidence", not "proven absent" |
| 3+ countries | +3 | ✅ 11 markets above 0.9% traffic; 19 storefronts; 8 currencies of sale |
| Multiple PSPs | 0 | ⬜ **Likely but unconfirmed.** No PSP named for any market. Architecture strongly implies multi-provider (two booking engines, per-market surcharges, NZ-only POLi, CN-only Alipay) but the 3 points require named providers and I do not have them |
| Local rail or licensing gap in a top-3 market | +3 | ✅ **Australia (11.15%, second-largest market) has no account-to-account rail.** Sourced from Air NZ's own `/fare-rules`, where the NZ paragraph names POLi as a fee-free route and the AU paragraph names only debit card, Travelcard and Airpoints. No BPAY, no PayTo/PayID anywhere on the property. *Limit of the evidence: that paragraph enumerates fee-avoidance routes, not the complete accepted-method set* |
| Recent expansion | +2 | ✅ Three new Christchurch international routes launching Oct–Nov 2026 (Singapore, Tokyo Narita, Perth) |
| Payment issues reported | +2 | ✅ Moderate — and uniquely, the strongest evidence is Air NZ's **own live help page** documenting an unresolved credit-processing defect |
| Funding >$10M | 0 | ❌ Listed company, no funding rounds. FY26 swung to a NZ$336m pre-tax loss |
| High traffic outside home | 0 | ❌ New Zealand is 67.68%, above the 60% threshold |
| Competitor using orchestration | +2 | ✅ Emirates appears on CellPoint Digital's own airline customer wall (first-party asset). Cebu Pacific's CellPoint case study states verbatim that it "implemented its multi-acquirer strategy more efficiently" |
| Payment job postings | 0 | ❌ Only a back-office **Payments Clerk** in the Finance Solutions Centre. Not payment infrastructure hiring, and not scored as such |

**Tier:** ⭐ High Priority (16).

> ### Analyst note
>
> **No override applied. This is a cleaner account than YuppTV** despite a comparable score: there is no app-store channel swallowing the transaction base, the merchant is unambiguously merchant-of-record on its own direct sales, and the volume is audited at 15.9 million passengers.
>
> **The one sizing unknown is the direct-versus-agency channel split.** Only direct bookings touch Air NZ's own checkout; agency sales settle through IATA BSP and sit outside any orchestration scope. The FY25 annual report was searched for `NDC`, `BSP`, `UATP`, `travel agent`, `agency`, `GDS`, `OTA`, `distribution cost` and `booking channel` — **zero hits on all of them**. It is not publicly available and must be asked on the call.
>
> **The FY26 loss cuts both ways.** A ~$500m earnings swing makes cost of acceptance and approval-rate leakage materially more salient to a CFO — and simultaneously means any new spend faces harder scrutiny. Lead with recovered revenue, not with new capability.

### Source Notes
- ✅ All FY25 financials — extracted from the audited annual report PDF, not search summaries: https://p-airnz.com/cms/assets/PDFs/airnz-2025-annual-report.pdf
- ✅ Crown shareholding 51.01% — Annual Report p.54, s293 FMCA substantial product holder disclosure
- ✅ Subsidiary list, and the fact that only one is non-NZ — Annual Report p.53
- ✅ Storefront and booking-engine configuration — extracted from `www.airnewzealand.com` page source
- ✅ China accepted-methods list — https://www.airnewzealand.cn/information-about-payment, published as static copy
- ✅ NZ-versus-AU fee-free route difference — https://www.airnewzealand.co.nz/fare-rules and https://www.airnewzealand.com.au/fare-rules
- ✅ Credit-redemption defect and constraints — https://www.airnewzealand.co.nz/credit-redemption, fetched 2026-09-14
- ✅ Cathay Pacific / Adyen direct acquiring including NZ and AU — Adyen press release, March 2026
- ⚠️ **Card surcharge percentages (NZ 1.5%/1.1%, AU 1.1%/0.75%) are trade-press and forum sourced.** Air NZ's own fee page at `airnz.custhelp.com` was blocked by the egress proxy on two attempts. **Do not quote the percentages.** The *structure* — a percentage fee varying by card type, with named fee-free routes — is sourced from Air NZ's own fare-rules pages
- ⚠️ FY26 loss figure — search summary only, not read in the primary release
- ⚠️ UK registration closure, Japan corporate number, India GSA — third-party registries only
- ⚠️ Emirates–CellPoint: the logo on CellPoint's own customer wall is first-party; the **scope** of the engagement is not published
- ❌ **No PSP, acquirer or MCP vendor identified for any market.** The single largest gap

### Success Case Alternatives
- **Wingo** — Tier 1 pattern: airline, approval-rate uplift, broad method coverage. Closest vertical match in the Yuno library
- **Viva Aerobus** — Tier 1 pattern: airline, 75% of failed transactions recovered. Directly relevant to the credit-redemption and retry angle
- **inDrive** — Tier 2: multi-country acquiring at scale. LATAM results; never imply they came from APAC
- ⚠️ **Do NOT use Qatar Airways.** No source connecting it to Yuno could be located; the reference has been withdrawn from the credibility defaults in `full-outreach.md`

---

## Executive Summary

Air New Zealand is a 51% Crown-owned national carrier that flew 15.9 million passengers in FY25 on NZ$6.76bn of revenue, selling through 19 country storefronts in 11 currencies. It has **no payment orchestration layer** and runs two booking engines concurrently — a modern funnel in New Zealand and a legacy engine still serving Japan and all NZ servicing. It has localised its payment rails in exactly **three** markets out of nineteen (POLi in NZ, SOFORT in Europe, Alipay in China), while discloses just **one** non-NZ incorporated subsidiary against eight currencies of sale. The motion is **greenfield**, and the timing hook is that a direct competitor, Cathay Pacific, consolidated onto Adyen direct acquiring covering New Zealand and Australia in March 2026.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** SimilarWeb supplied by Prateek 2026-09-10, Jun–Aug 2026, **merged across 23 domains** ("Include all country domains" ON). Shares are therefore group-wide. Absolute visit volumes were not in the supplied view.

| Rank | Country | Traffic Share | Trend | Flies there? | Storefront? | Source |
|------|---------|---------------|-------|--------------|-------------|--------|
| 1 | New Zealand | 67.68% | ↑ +2.65% | ✅ 20 domestic ports | ✅ NZD | SimilarWeb (supplied) |
| 2 | Australia | 11.15% | ↓ −3.14% | ✅ 7 cities | ✅ AUD | SimilarWeb (supplied) |
| 3 | United States | 6.42% | ↑ +7.30% | ✅ long-haul | ✅ USD | SimilarWeb (supplied) |
| 4 | Japan | 2.30% | ↑ +6.01% | ✅ Tokyo | ✅ JPY | SimilarWeb (supplied) |
| 5 | Taiwan | 1.48% | ↑ **+68.67%** | ✅ Taipei | ✅ TWD | SimilarWeb (supplied) |
| 6 | Thailand | 1.30% | ↑ **+51.08%** | ❌ **not in the FY25 network** | ❌ **none** | SimilarWeb (supplied) |
| 7 | Singapore | 1.23% | ↓ −26.13% | ✅ Singapore | ✅ SGD | SimilarWeb (supplied) |
| 8 | United Kingdom | 1.17% | ↑ +7.58% | ❌ no direct service | ✅ GBP | SimilarWeb (supplied) |
| 9 | Indonesia | 1.16% | ↑ **+1,596.11%** | ✅ **Denpasar, ~7x weekly** | ❌ **none** | SimilarWeb (supplied) |
| 10 | Canada | 1.10% | ↑ +26.73% | ✅ Vancouver | ✅ CAD | SimilarWeb (supplied) |
| 11 | India | 0.92% | ↓ −0.99% | ❌ no flights | ❌ **served off the Singapore site** | SimilarWeb (supplied) |

**High priority (>5% share):** New Zealand, Australia, United States.

**The engagement anomaly:** Indonesia shows **14.88 pages per visit** against a 4–6 site average — a 3x outlier. See Section 8. No complaint evidence ties the figure to a payment problem, and none is asserted here.

**Growth corrected:** there is **no Air NZ route to Taiwan or Thailand**. The Auckland–Bangkok non-stop returning in late 2026 is **Thai Airways**; the Taipei traffic relates to **STARLUX** launching Taipei–Sydney with an Auckland tag. Only Indonesia's growth is plausibly explained by Air NZ's own capacity, where Denpasar moved from thin-seasonal to roughly daily.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Air New Zealand House, 185 Fanshawe Street, Auckland 1010. Incorporated 1940. NZX: AIR (1989), ASX: AIZ (2002).

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| New Zealand | **Air New Zealand Limited** | NZBN 9429040402543 | AR p.111; airnewzealand.com/incorporation-and-listing |
| Australia | **Air New Zealand (Australia) Pty Limited** — *the only non-NZ incorporated subsidiary disclosed* | not disclosed in AR | AR p.53 |
| Australia | Air New Zealand Limited, registered to carry on business | ABN 70 000 312 685 (ACN 000 312 685) | airnewzealand.com/incorporation-and-listing |
| New Zealand | Air Nelson Ltd · Mount Cook Airline Ltd · Air NZ Express Ltd · Air NZ Aircraft Holdings Ltd · Air NZ Associated Companies Ltd · Air NZ Regional Maintenance Ltd · ANNZES Engines Christchurch Ltd · TEAL Insurance Ltd | mostly not disclosed | AR p.53 |
| United Kingdom | FC008870 (overseas company) and BR013134 (UK establishment) — **both appear CLOSED** | — | Companies House `[UNVERIFIED — search summary]` |
| Japan | ニュージーランド航空株式会社, 外国会社等, Chiyoda-ku | 法人番号 4700150003018 | third-party aggregator only `[UNVERIFIED]` |

**Crown shareholding:** The Sovereign in Right of New Zealand holds **1,686,990,261 of 3,306,993,443 ordinary shares = 51.01%** at 30 Jun 2025, plus the non-listed **"Kiwi Share"** carrying rights over ownership and transfer (AR p.54).

**Cross-Border Gap Analysis:**

| Country | Traffic | Flies there | Local entity? | Storefront currency | Domestic acquiring gated? | Cross-Border Risk? |
|---------|---------|-------------|---------------|---------------------|---------------------------|---------------------|
| New Zealand | 67.68% | ✅ | ✅ | NZD | No | Low |
| Australia | 11.15% | ✅ | ✅ (subsidiary + ABN) | AUD | No | Low |
| **United States** | 6.42% | ✅ | ❌ | USD | No | **High — largest gap by traffic** |
| Japan | 2.30% | ✅ | ⚠️ probable, unconfirmed | JPY | No | Medium |
| Taiwan | 1.48% | ✅ | ❌ | TWD | No | **High** |
| Thailand | 1.30% | ❌ | ❌ | **none** | No | **High** |
| Singapore | 1.23% | ✅ | ❌ | SGD | No | **High** |
| United Kingdom | 1.17% | ❌ | ❌ (registrations closed) | GBP | No | **High** |
| **Indonesia** | 1.16% | ✅ ~daily | ❌ | **none** | **YES 🔒** | **High + regulatory** |
| Canada | 1.10% | ✅ | ❌ | CAD | No | **High** |
| **India** | 0.92% | ❌ | ❌ | **none — via SG site** | **YES 🔒** | **High + regulatory** |
| *(China)* | — | ✅ Shanghai | ❌ | CNY | **YES 🔒** | **High + regulatory** |
| *(Hong Kong)* | — | ✅ | ❌ | HKD | No | **High** |

> *"Warning: Air New Zealand publishes market-specific pricing and fee schedules in NZD, AUD, USD, CAD, GBP, EUR, HKD and CNY — eight currencies — while disclosing exactly one non-NZ incorporated subsidiary. The United States is its third-largest traffic market, a long-haul network anchor with USD-denominated pricing, and appears nowhere in the FY25 subsidiary list."*

> *"Regulatory gate: Indonesia, India and mainland China all gate domestic acquiring behind local presence or a licensed local partner. Air NZ flies to Denpasar roughly daily and to Shanghai, publishes CNY fee schedules, and holds no confirmed entity in any of the three. Verify the current rules and cite the source before using this."*

> **MANUAL:** The country-site terms and footer pages for Singapore, Japan, China and Australia were not read (fetch budget). They are the most likely place to find per-market contracting entities.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| New Zealand | **POLi Payments** — A2A bank transfer, not a card PSP. Supported banks: ANZ, ASB (personal), BankDirect, BNZ, Kiwibank, TSB, Westpac | `[Terms/Privacy Policy]` | https://www.airnewzealand.co.nz/poli-information |
| Europe (DACH + BE/NL) | **SOFORT Banking** | `[Terms/Privacy Policy]` | https://www.airnewzealand.eu/sofort-faqs |
| Mainland China | **Alipay** | `[Terms/Privacy Policy]` | https://www.airnewzealand.cn/information-about-payment |
| Global | Multi-currency pricing on Visa/MC/JCB/Amex/Diners/Discover — **vendor unnamed** | `[Terms/Privacy Policy]` | https://www.airnewzealand.com/multi-currency-payment |
| Global (distribution only) | Amadeus — GDS distribution agreement. **No evidence of Amadeus Payment Platform** | `[Press Release]` | https://amadeus.com/en/newsroom/press-releases/air-new-zealand-distribution-agreement |

**No card acquirer or gateway is publicly named for any market.** Adyen, Worldpay, CyberSource, Braintree, Checkout.com, Windcave, eWAY, ANZ Worldline, Global Payments, Fiserv and CellPoint all returned zero Air NZ-specific results across 17 searches.

**Observed architecture — the dual booking estate:**

| | New Zealand | Japan |
|---|---|---|
| Booking host | `flightbookings.airnewzealand.co.nz` | `flightbookings.airnewzealand.jp` |
| Path | `/fly/search` | `/vbook/actions/ext-search` |
| Architecture | Next.js SPA, assets on `a.static.b-airnz.com` | Legacy server-rendered `/actions/` app |

The content layer is shared (`p-airnz.com` on both); the booking-and-payment funnel is not. NZ still routes manage-booking and check-in to the legacy engine at `/vmanage/actions/`, so **both stacks run concurrently even within the home market.**

`[INFERENCE, not confirmed]: two distinct checkout funnels on two distinct hosts most likely means two distinct payment integrations. The architectural split is directly observed; the payment consequence is inference.`

#### 3B. Payment Orchestrator

**None detected.**

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with PSP(s), which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

Checked and absent from **CellPoint Digital's own published airline customer wall**: Air Europa, Arajet, Avianca, Beond, Cebu Pacific, Emirates, GOL, Icelandair, KM Malta, La Compagnie, Oman Air, Riyadh Air, Southwest, Virgin Atlantic — no Air New Zealand. Spreedly, Primer, Gr4vy, APEXX, Payrails, IXOPAY and Yuno all returned zero.

**Caveat, stated plainly:** the payment step is gated behind booking session state and could not be reached. "None detected" means no public evidence, not proven absent. On public evidence it is not possible to discriminate between *no orchestration* and *an in-house routing layer* — though the dual-funnel estate argues against a unifying layer being in place today.

> **MANUAL:** Walk a real booking to the payment step on `airnewzealand.co.nz` and again on `airnewzealand.jp`, devtools open. Compare the payment host and any SDK. This single test resolves both the orchestration question and the multi-PSP ICP point.

---

### Section 4: Alternative & Local Payment Methods

**Method — and why this section is unusually well evidenced.** The same URL path was probed across six country properties. Page existence is itself the evidence:

| Path | NZ | AU | SG | JP | CN | EU |
|---|---|---|---|---|---|---|
| `/information-about-payment` (accepted-methods list) | 404 | 404 | 404 | 404 | **200** | — |
| `/poli-information` (A2A rail) | **200** | not named for AU | **404** | **404** | — | — |
| `/sofort-faqs` (local bank rail) | — | — | **404** | **404** | — | **200** |
| Card surcharge disclosed on `/fare-rules` | ✅ | ✅ | **no section** | — | — | — |

**Air NZ localises its payment rails in exactly three of nineteen storefronts** — POLi for New Zealand, SOFORT for Europe, Alipay for China. Every other property, including all of APAC except China, runs the global card rail plus the loyalty and credit stack. The `.cn` and `.eu` pages prove the CMS and the commercial capability exist.

The MCP card list is **byte-identical across NZ, JP and CN** — Visa, MasterCard, Discover, JCB, Amex, Diners — consistent with one global acquiring configuration and no market-specific scheme additions.

| Country | Method | Category | Status | Source |
|---------|--------|----------|--------|--------|
| NZ | Visa/MC/Amex/Diners/JCB/Discover | Cards | Active | /multi-currency-payment |
| NZ | POLi (7 named banks) | Bank transfer / A2A | Active | /poli-information |
| NZ | Airpoints · Airpoints Flexipay | Loyalty | Active | /airpoints-flexipay |
| NZ | Air NZ Travelcard | Corporate account | Active | /fare-rules |
| NZ | Flight credit (≤2 per booking) | Stored value | Active | /credit-redemption |
| NZ | Voucher (via Koru account) | Stored value | Active | /vouchers |
| AU | Cards, debit card, Travelcard, Airpoints | Cards / Loyalty | Active | .com.au/fare-rules |
| **AU** | **POLi / any A2A rail** | Bank transfer | **ABSENT — sourced** | .com.au/fare-rules (AU paragraph) |
| AU | BPAY, PayTo/PayID, Afterpay, Zip | Bank / BNPL | Not found | — |
| **CN** | **Alipay** | Wallet | **Active** | .cn/information-about-payment |
| CN | Visa / Mastercard / Amex | Cards | Active | same |
| **CN** | **UnionPay (银联), WeChat Pay (微信支付)** | Cards / Wallet | **ABSENT from an enumerated list — sourced** | same |
| JP | Credit card, debit card | Cards | Active | .jp/faq |
| **JP** | **konbini, PayPay, Rakuten Pay, card instalment/bonus** | Cash / Wallet / Instalment | **ABSENT — zero mentions in the JP FAQ** | .jp/faq |
| SG | Cards; Fare Hold deferral | Cards | Active | .com.sg/booking-options |
| **SG (+IN)** | **PayNow, GrabPay, UPI, netbanking, EMI** | Local rails | **ABSENT — no payment section, all rail paths 404** | .com.sg/fare-rules |
| US | PayPal, Affirm, Klarna | Wallet / BNPL | Not found | — |
| TW / TH / ID / CA / UK | local rails | — | Not found | — |
| Global | UATP, Apple Pay, Google Pay on flight checkout | — | Not found | — |

**Confirmed gaps — sourced absences only:**

1. **China — UnionPay and WeChat Pay absent from an explicitly enumerated accepted-methods list.** The strongest single finding: the page names Alipay and three card schemes and nothing else. UnionPay is the domestic rail for the overwhelming majority of Chinese cardholders. Alipay being present proves the site is not APM-hostile; it is one-wallet-deep.
2. **Australia — no account-to-account rail, in the second-largest market.** POLi is named as fee-free for NZ and absent from the AU paragraph of the same page; POLi closed its Australian operation in 2023 and nothing replaced it. No BPAY, no PayTo/PayID.
3. **Japan — no konbini, no PayPay, no card instalments** on a JPY-denominated long-haul ticket, the classic instalment-and-konbini category.
4. **Singapore, and India served off the same property — no local rail of any kind**, and no payment help page at all.
5. **Currency coverage gap.** The flight-credit tool supports NZD, AUD, USD, CAD, EUR, SGD, GBP, JPY, HKD, CNY, TWD, KRW, XPF. **THB, IDR, INR, MYR and PHP are absent** — covering Thailand (1.30%), Indonesia (1.16%) and India (0.92%).

**No BNPL on any Air NZ property.** Afterpay, Zip, Laybuy, humm, Klarna and Affirm appear only via third-party resellers (Alternative Airlines, Fly Fairly), off Air NZ's merchant record. The closest native product is **Airpoints Flexipay** (points plus cash, not credit), which is **geo-fenced to New Zealand and Australia only**.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date | Source |
|------------|----------|-----------|------|--------|
| **Unresolved credit-processing defect — self-admitted** | Air NZ's own help page | **Live** | Fetched 2026-09-14 | https://www.airnewzealand.co.nz/credit-redemption |
| Credit tool cannot process certain credits | Air NZ's own help page | Live | 2026-09-14 | same |
| Refund processing delays — a reported 16-week case | NZ Herald | Isolated, documented | — | nzherald.co.nz `[UNVERIFIED — summary]` |
| Partial refunds, refusal after airline-initiated cancellation | Trustpilot | Moderate | Various | trustpilot.com `[UNVERIFIED — 403 blocked]` |

**The most significant finding in the section is Air New Zealand's own published copy:**

> "If you have not received notification that your credit has been processed, **please note that our Team is currently working on resolving this.** We will be in touch soon with a new booking reference. If you need to use your credit urgently, please call our Contact Centre."

Alongside a documented FAQ for *"The tool doesn't recognise my credits"*, and these constraints, all verbatim:

- "the credit tool can use up to **2 credits per new booking**… Please call our Contact Centre if you want to combine more than 2"
- "only **1 credit** may be used within a transaction" for changes
- "Use up to 2 credits **of the same currency**" — credits are currency-siloed and cannot be mixed
- Residual balance "must be paid using your **credit card**"
- Airpoints-plus-credit combination is **New Zealand and Australia only**, and "airport taxes… need to be paid separately using another payment method"

A single NZ checkout can therefore combine **four tenders** — Airpoints, one or two flight credits, and a card or POLi for the tax residual — against a disclosed **NZ$192M unused travel credit liability** (AR Note 13, FY24: $212M; $35M breakage recognised in FY25).

> *"Pattern: a self-documented credit-processing defect, a two-credit online ceiling with a phone fallback, currency-siloed stored value and a four-tender checkout, sitting against a NZ$192M liability. This is split-tender orchestration complexity described by the merchant itself."*

**Honest frequency assessment: moderate, and a small share of a very large general complaint volume.** No verifiable Air NZ-specific reports of declined cards, failed transactions at the payment step, or double charges were found — the Reddit search returned zero Air NZ results. Air NZ's public complaint volume is dominated by **operational** issues: cancellations, the Pratt & Whitney engine groundings, delays, call-centre waits. Payment and refund is a minority slice, and padding it with operational noise would be dishonest.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|------|-------------|----------|--------|
| 1 | Aug 2026 | **FY26 loss before taxation of NZ$336m**, vs $164m earnings prior year `[UNVERIFIED — summary]` | Financial | airnewzealandnewsroom.com |
| 2 | Aug 2026 | Expanded interline partnership with Air Chathams — new fare/ticketing and settlement integration | Partnership / distribution | airnewzealandnewsroom.com |
| 3 | 2026 | **Three new Christchurch international routes** — Singapore 28 Oct, Tokyo Narita 28 Nov, Perth 30 Nov | Market Expansion | airnewzealandnewsroom.com |
| 4 | May 2026 | **Economy Skynest™** on sale — bookable sleep pods, flying Nov 2026, a new ancillary SKU sold separately from the fare | Product / ancillary retailing | airnewzealandnewsroom.com |
| 5 | FY25 | Ancillary revenue **+15%**; Airpoints Store sales **+14%**; Kia Mau transformation delivered ~$100M of benefits | Financial / retailing | AR p.12 |

**No public payment-related RFP found.**
**No payments, ecommerce or retailing job postings found** — only a back-office Payments Clerk in the Finance Solutions Centre.
**No NDC, "modern airline retailing" or "offer and order" programme found.** Both searches returned generic IATA/PROS industry material. If such a programme exists it is not publicly announced.
Adjacent: a **TCS digital transformation partnership announced March 2025** — plausibly the vehicle for the `/fly/` re-platform, but no payments linkage is claimed.

---

### Section 7: Payment-Specific News

| # | Date | Item | Relevance | Source |
|---|------|------|-----------|--------|
| 1 | Mar 2026 | **Cathay Pacific expands to Adyen direct acquiring across 45+ markets, explicitly naming New Zealand and Australia.** Published rationale: control over authorisation rates, reduced processing fees, transaction-data visibility, no third-party acquiring banks | A direct route competitor consolidated payments in Air NZ's two largest markets | https://www.adyen.com/press-and-media/cathay-pacific-expands-global-partnership-with-adyen |
| 2 | — | **Singapore Airlines on Adyen direct acquiring** — "eliminates the need to run payments across multiple third-party platforms", increased authorisation rate via RevenueAccelerate | Second Asia-Pacific competitor consolidating | https://www.adyen.com/press-and-media/singapore-airlines-partners-with-adyen-to-speed-digital-payment-journeys |
| 3 | May 2026 | **NZ card surcharge ban takes effect — ecommerce explicitly EXEMPT.** The ban covers in-store EFTPOS/Visa/Mastercard surcharges only | Air NZ's **online** card fee is unaffected. Do not pitch this as a compliance deadline | rnz.co.nz, beehive.govt.nz |
| 4 | Nov 2024 | Air NZ named a launch merchant for **Apple Tap to Pay on iPhone in NZ**. Launch platforms: Adyen, ANZ Bank, Stripe, Windcave, Worldline | **In-person acceptance, not online checkout.** Do not conflate — but it does confirm a card-present estate | apple.com/nz/newsroom `[UNVERIFIED]` |

**No new PSP partnership, provider removal, or online BNPL launch found.**

---

### Section 8: Checkout Experience Audit

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | **Unknown** | — | Booking engine on a separate domain per market; payment step requires a live search and session |
| Storefront architecture | **19 storefronts, 13 booking-engine domains, 11 currencies** | — | Extracted from homepage config: co.nz NZD · com.au AUD · .com **USD** · .ca CAD · .co.jp JPY · .com.hk HKD · .com.cn CNY · .com.sg SGD · .co.uk GBP · .eu EUR · .com.tw TWD · pacificislands NZD |
| **Storefront gaps** | **No Indonesia, Thailand, India, Malaysia, Vietnam or Philippines storefront** | Poor | An Indonesian customer booking AKL–DPS is routed to a foreign-currency storefront with no IDR pricing and no local method |
| Payment methods visible | Card, POLi, Airpoints, Flexipay, Travelcard, flight credit, voucher | — | From help articles, not observed at checkout |
| Split tender | **Up to four tenders in one NZ booking** | Fair | Verbatim sequence documented in §5 |
| Location-based method display | Bound to storefront domain, not detected dynamically | — | Pricing currency follows the domain |
| Surcharge display | **`cardPaymentFeeText` is a first-class field on every fare object** in the homepage JSON | — | The card fee is a modeled, storefront-conditional display element |
| 3DS / tokenisation / PCI | **Not observable** | — | Zero hits for 3DS, Cardinal, threeds or tokenisation on any fetched page |
| Instalment / BNPL | **None native** | Poor | Available only via third-party resellers |
| Mobile responsiveness | Not verified | — | — |

*"Full checkout flow not accessible. Findings limited to publicly observable elements."* `https://www.airnewzealand.co.nz/payment/` is a Next.js SPA with an empty `<div id="__next">` — methods render client-side and are invisible to static fetching. **Checkout type is not being inferred.**

**On the Indonesia anomaly (14.88 pages/visit):** the storefront gap above is a verified structural fact. **The causal link to the page-depth figure is unproven** — no complaint evidence, no user reports, no session data. Stated as a hypothesis worth testing on a call, never as a finding.

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **No public information found** | — |
| Card data handling | Not determinable | — |
| Recommended Yuno integration | Not determinable without seeing the checkout | — |

*"No direct PCI compliance documentation found publicly for Air New Zealand."* No attestation, level, AOC or payment-security statement surfaced on any property or in the annual report.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: Flying to markets the storefront doesn't serve**
> **Evidence:** §8 — the homepage config enumerates 19 storefronts in 11 currencies with **no Indonesia, Thailand or India property**; §4 — the flight-credit tool supports 13 currencies and **excludes IDR, THB and INR**; §1 — Air NZ flies Auckland–Denpasar roughly daily and Indonesia is its fastest-growing traffic market.
> **Pain Point:** An Indonesian customer booking a flown Air NZ route is pushed to a foreign-currency storefront, pays a converted fare with MCP margin on top, and has no local rail — no QRIS, no virtual account, no GoPay or OVO. Indonesia also gates domestic acquiring behind local presence, so the card itself is acquired cross-border.
> **Yuno Value Proposition:** One integration adds a local rail and local acquiring per market without standing up a storefront or an entity per country.
> **Best Success Case:** Wingo — airline, approval-rate uplift, broad method coverage. Tier 1 pattern match.
> **Outreach Angle:** You fly Auckland–Denpasar close to daily, but there's no Indonesian storefront, no IDR pricing and no local payment method behind it.
> **Suggested Subject Line:** Denpasar daily, no IDR checkout
>
> **Insight #2: Australia lost its bank rail and nothing replaced it**
> **Evidence:** §4 — Air NZ's own `/fare-rules` names POLi as a fee-free route in the New Zealand paragraph and names only debit card, Travelcard and Airpoints in the Australian paragraph, on the same page; §1 — Australia is 11.15% of traffic, the second-largest market.
> **Pain Point:** Every Australian customer avoiding the card surcharge is pushed to debit card or a loyalty balance. No BPAY, no PayTo, no PayID — the rails most Australians would expect for a high-ticket purchase.
> **Yuno Value Proposition:** Add the local A2A rail back in a single integration, at a lower cost of acceptance than the card it replaces.
> **Best Success Case:** Wingo again, or Viva Aerobus on recovery. Pattern match, labelled.
> **Outreach Angle:** Your NZ fare rules offer POLi as the fee-free way to pay. The Australian paragraph on the same page doesn't offer a bank rail at all.
> **Suggested Subject Line:** No bank rail on your AU checkout
>
> **Insight #3: You've localised three storefronts out of nineteen — and proved you can**
> **Evidence:** §4 — the `/information-about-payment` page exists only on `.cn`, `/poli-information` only on `.co.nz`, `/sofort-faqs` only on `.eu`, with 404s everywhere else; §3A — the MCP card list is byte-identical across NZ, JP and CN, indicating one global acquiring configuration.
> **Pain Point:** The capability demonstrably exists — Alipay in China, SOFORT in Europe, POLi in NZ — and has been used three times in nineteen markets. Japan takes a JPY-denominated long-haul fare with no konbini and no instalment option. China's own list omits UnionPay and WeChat Pay.
> **Yuno Value Proposition:** Per-market rails stop being per-market projects.
> **Best Success Case:** Wingo (1,000+ payment methods through one integration). Tier 1 pattern.
> **Outreach Angle:** Your China site lists Alipay and three card schemes. No UnionPay, no WeChat Pay.
> **Suggested Subject Line:** Alipay yes, UnionPay no
>
> **Insight #4: A competitor consolidated payments in your two biggest markets**
> **Evidence:** §7 — Cathay Pacific expanded to Adyen direct acquiring in March 2026, explicitly covering New Zealand and Australia, citing control over authorisation rates and reduced processing fees; §3B — Air NZ has no orchestration layer and runs two booking engines concurrently.
> **Pain Point:** A direct route competitor is now optimising authorisation rates in Air NZ's home markets while Air NZ runs a modern funnel in NZ and a legacy engine in Japan.
> **Yuno Value Proposition:** Routing and failover across acquirers on top of the existing estate — no rip-out, and no waiting for the legacy engine to be retired first.
> **Best Success Case:** Viva Aerobus — 75% of failed transactions recovered. Labelled as a pattern match, LATAM results.
> **Outreach Angle:** Cathay moved to direct acquiring across New Zealand and Australia in March, specifically for authorisation rates.
> **Suggested Subject Line:** What Cathay changed in March
> **Caution:** naming a competitor's vendor is sharp. Phase 2 or later, and only framed as market context.

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks:**
1. You fly Auckland–Denpasar close to daily, and there's no Indonesian storefront, no IDR pricing and no local payment method behind the route.
2. Your New Zealand fare rules name POLi as the fee-free way to pay; the Australian paragraph on the same page doesn't name a bank rail at all.
3. Your China site publishes exactly what it accepts — Alipay plus Visa, Mastercard and Amex. No UnionPay, no WeChat Pay.

**Cold call openers:**
1. I noticed your flight-credit tool handles thirteen currencies, and none of them is the rupiah, baht or rupee — how do those customers actually pay?
2. You've localised the payment rails on three of your nineteen storefronts. I was curious what decides which markets get one.
3. Cathay went to direct acquiring across New Zealand and Australia in March, citing authorisation rates. Has that conversation come up on your side?

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Airline | Website | HQ | Overlap with Air NZ | Known PSP/Orchestrator | Source |
|---------|---------|----|--------------------|------------------------|--------|
| Qantas | qantas.com | Sydney | Trans-Tasman + domestic NZ via Jetstar | **Not found** — payment-options page shows PayPal, Zip, BPAY, Alipay, UATP as consumer methods; no PSP signature | qantas.com/en-au/book/flights/payment-options |
| Jetstar | jetstar.com | Melbourne | Domestic NZ trunk + trans-Tasman | **Not found** | karryon.com.au |
| Virgin Australia | virginaustralia.com | Brisbane | Trans-Tasman — **also codeshares with Air NZ** (approved Jun 2024) | **Not found** | abc.net.au |
| **Cathay Pacific** | cathaypacific.com | Hong Kong | Year-round AKL–HKG | **Adyen — direct acquiring incl. NZ and AU, Mar 2026** | adyen.com |
| **Singapore Airlines** | singaporeair.com | Singapore | AKL–SIN | **Adyen — direct card acquiring** | adyen.com |
| **Emirates** | emirates.com | Dubai | Only non-stop Middle East–AKL carrier | **CellPoint Digital** — logo on CellPoint's own customer wall; scope unpublished | cellpointdigital.com/industry/airline |
| China Airlines | china-airlines.com | Taipei | ~40 weekly AKL flights via TPE | **Not found** | aucklandairport.net |
| Qatar Airways | qatarairways.com | Doha | Year-round AKL | **Not found** | aucklandairport.net |

**Not verified as Auckland non-stop operators:** Japan Airlines and ANA. The source indicates Air NZ is currently the only non-stop Japan–Auckland operator; JAL and ANA compete only for connecting traffic. Do not assert them as route competitors.

#### 11B. Industry Peers

| Airline | Why Similar (Payment Context) | Source |
|---------|-------------------------------|--------|
| Cebu Pacific | Same vertical, same problem, **published orchestration outcome** — reduced transaction costs, increased acceptance rates, multi-acquirer strategy | cellpointdigital.com case study |
| Icelandair · Virgin Atlantic · Air Europa · Oman Air · Riyadh Air · Southwest | Mid-size carriers that chose an orchestration layer, on CellPoint's published roster | cellpointdigital.com/industry/airline |

#### 11C. Companies Recently Adopting Payment Orchestration

| Airline | Orchestrator | Date | What was published | Source |
|---------|-------------|------|--------------------|--------|
| **Cebu Pacific** | CellPoint Digital | Updated Sep 2025 | Verbatim: *"reduced its transaction costs, increased its payment acceptance rates and implemented its multi-acquirer strategy more efficiently"* | cellpointdigital.com |
| **Virgin Atlantic** | CellPoint Digital | Mar 2022 | Appointed as payment partner for Virgin Atlantic and Virgin Holidays | businesswire.com |
| **Riyadh Air** | CellPoint Digital | — | Implementing orchestration for local and cross-border transactions | aviationweek.com |
| **Emirates** | CellPoint Digital | Logo dated Oct 2024 | Logo on customer wall; **orchestration scope not published** | cellpointdigital.com |

**Adyen direct acquiring — related but not orchestration**, recorded here because the commercial rationale is identical: **Cathay Pacific** (Mar 2026, incl. NZ and AU) and **Singapore Airlines**.

> ⚠️ **Two false positives to avoid.** IndiGo and LATAM Airlines appeared in an initial grep of CellPoint's site — both were artefacts. "indigo20/indigo50" are CSS colour tokens; "LATAM" hits were a conference name and an article slug. **Do not claim either as a CellPoint customer.**

**No airline orchestration case study with a published numeric approval-rate uplift exists.** CellPoint's Cebu Pacific and Virgin Atlantic studies are qualitative only.

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | China Airlines | Direct competitor | TW, AKL, Asia | Not scored | — | ~40 weekly AKL flights, no stack found | To check |
| 2 | Qantas / Jetstar | Direct competitor | AU, NZ, Asia | Not scored | — | No PSP found; the largest unresearched stack in the region | To check |
| 3 | Virgin Australia | Direct competitor | AU, NZ | Not scored | — | No stack found; codeshare partner as well as rival | To check |
| 4 | EVA Air | Adjacent | TW, Asia-Pacific | Not scored | — | Not verified this pass | To check |
| 5 | Fiji Airways | Adjacent | Pacific, NZ, AU | Not scored | — | Pacific overlap with Air NZ | To check |

Scores are deliberately blank — none was researched to this report's evidentiary standard, and a guessed score is worse than none.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| **Passengers carried (Group)** | **15,907,000** | FY25 Annual Report p.111 — the transaction-count proxy |
| — Domestic NZ | 10,142,000 | ibid. |
| — International | 5,765,000 (AU & Pacific 3,840,000 · Asia 1,101,000 · America & Europe 824,000) | ibid. |
| Total operating revenue | **NZ$6,755M** | AR p.62 |
| Passenger revenue | **NZ$5,851M** | AR p.62 |
| Net profit after tax | NZ$126M (FY24: $146M) | AR p.62 |
| **FY26 result** | **Loss before tax NZ$336m** vs $164m earnings prior year | newsroom `[UNVERIFIED — summary]` |
| Revenue by region of **original sale** | NZ 61.3% · Asia/UK/Europe 13.8% · America 13.0% · AU & Pacific 12.0% | AR p.75, Note 1 Segmental Information |
| Average revenue per passenger carried | ~NZ$368 | `[INFERENCE]` — passenger revenue ÷ passengers. Not a ticket price; one ticket covers multiple sectors |
| **Revenue in advance** | **NZ$2,027M** — transportation sales in advance $1,588M current, loyalty $397M | AR Note 13 |
| **Unused travel credits** | **NZ$192M** (FY24: $212M); $35M breakage recognised FY25 | AR Note 13 |
| Airpoints members | "More than five million" — against an NZ population of ~5.3M, treat as accounts not unique actives | AR pp.9, 19 |
| Ancillary revenue | **+15% FY25**; absolute figure not disclosed | AR p.12 |
| Currencies of sale | NZD, AUD, USD, CAD, GBP, EUR, HKD, CNY (fees) — 11 across storefronts | airnewzealand.com/optional-fees; homepage config |
| **Direct vs agency channel split** | **NOT DISCLOSED** — the FY25 report was searched for NDC, BSP, UATP, travel agent, agency, GDS, OTA, distribution cost and booking channel. **Zero hits on all.** | — |

**Sizing note:** 15.9M passengers is the volume anchor, but only the direct-channel share touches Air NZ's own checkout. That share is not public and must be asked.

---

### Overall Research Confidence

**High — the strongest file in the pipeline so far.**

**Strong coverage:** financials are audited and extracted from the annual report PDF, not summarised. Entity structure comes from the company's own disclosure. The payment-methods analysis (§4) is unusually well evidenced because the same URL path was probed across six country properties, making page existence itself the evidence — this produced genuine *sourced absences* rather than the "not found" that limited the YuppTV file. The storefront and booking-engine configuration was extracted from Air NZ's own page source.

**Weak coverage:** no PSP or acquirer identity for any market, despite 17 searches — the single largest gap. PCI posture entirely unknown. The live checkout could not be reached on any property; all method findings come from help articles, with China's static list the one exception. Trustpilot was 403-blocked and Air NZ's own card-fee page was blocked by the egress proxy, so surcharge percentages rest on trade press.

**Traffic data was SUPPLIED** by Prateek from SimilarWeb (Jun–Aug 2026), merged across 23 domains, so the country profile is group-wide and reliable. Absolute visit volumes were not in the supplied view.

---

### Manual Research Recommendations

> **Area:** PSP identity and whether the two booking engines use different providers (§3)
> **Why it matters:** Converts the multi-PSP ICP point from unconfirmed to confirmed, and determines whether the pitch is "add routing" or "unify two stacks".
> **Suggested manual action:** Walk a real booking to the payment step on `airnewzealand.co.nz` and again on `airnewzealand.jp`, devtools open. Compare the payment host, any SDK, and the 3DS flow. Ten minutes, and worth more than another research run.

> **Area:** Direct versus agency channel split (§12)
> **Why it matters:** Only direct bookings are orchestrable. Not disclosed anywhere public.
> **Suggested manual action:** Ask on the first call, framed as scoping: *"what share of tickets sell through your own channels versus agency and OTA?"*

> **Area:** Card surcharge percentages (§7)
> **Why it matters:** Cost of acceptance is the commercial core of the pitch, and Air NZ's own fee page was proxy-blocked.
> **Suggested manual action:** Open `airnz.custhelp.com/app/answers/detail/a_id/2688` in a browser and record the current schedule per market.

> **Area:** Indonesia checkout experience (§8)
> **Why it matters:** Insight #1 rests on there being no IDR storefront. Worth seeing what an Indonesian customer actually gets.
> **Suggested manual action:** VPN to Indonesia, price AKL–DPS, and record the currency shown, the methods offered and whether MCP margin is applied.

> **Area:** Qantas, Jetstar and Virgin Australia payment stacks (§11A)
> **Why it matters:** Air NZ's true head-to-head rivals, and none has a confirmed stack. The competitive angle currently rests on long-haul carriers.
> **Suggested manual action:** Grep the actual booking-flow checkout rather than the marketing page — a real browser session on each.

---

### Appendix: All Source URLs

**Company primary sources**
- https://p-airnz.com/cms/assets/PDFs/airnz-2025-annual-report.pdf (FY25 Annual Report)
- https://www.airnewzealand.com/incorporation-and-listing · https://www.airnewzealand.com/multi-currency-payment
- https://www.airnewzealand.co.nz/fare-rules · https://www.airnewzealand.com.au/fare-rules
- https://www.airnewzealand.co.nz/poli-information · https://www.airnewzealand.co.nz/credit-redemption
- https://www.airnewzealand.co.nz/airpoints-flexipay · https://www.airnewzealand.co.nz/vouchers
- https://www.airnewzealand.cn/information-about-payment · https://www.airnewzealand.eu/sofort-faqs
- https://www.airnewzealand.jp/faq · https://www.airnewzealand.jp/multi-currency-payment
- https://www.airnewzealand.com.sg/fare-rules · https://www.airnewzealand.com.sg/booking-options
- https://www.airnewzealand.com/optional-fees · https://www.airnewzealand.com/fare-hold
- https://careers.airnewzealand.co.nz/job/payments-clerk-in-auckland-nz-jid-369

**Corporate developments**
- https://www.airnewzealandnewsroom.com/press-release-2026-air-new-zealand-announces-2026-annual-results
- https://www.airnewzealandnewsroom.com/press-release-2026-major-international-expansion-set-to-boost-christchurch-and-south-island-growth
- https://www.airnewzealandnewsroom.com/press-release-2026-the-future-of-long-haul-travel-air-new-zealands-economy-skynest-on-sale-from-may
- https://www.airnewzealandnewsroom.com/press-release-2026-air-new-zealand-and-air-chathams-expand-interline-partnership-to-connect-more-of-new-zealand
- https://www.airnewzealandnewsroom.com/press-release-2023-bali-here-we-come-air-nz-resumes-non-stop-flights-to-denpasar
- https://www.futuretravelexperience.com/2025/03/air-new-zealand-and-tata-consultancy-services-announce-tech-driven-partnership-to-deliver-digital-transformation/

**Competitors & orchestration**
- https://www.adyen.com/press-and-media/cathay-pacific-expands-global-partnership-with-adyen
- https://www.adyen.com/press-and-media/singapore-airlines-partners-with-adyen-to-speed-digital-payment-journeys
- https://cellpointdigital.com/industry/airline · https://cellpointdigital.com/resources/case-studies
- https://cellpointdigital.com/articles/casestudies/payment-orchestration-as-a-growth-catalyst-the-cebu-pacific-case-study
- https://www.businesswire.com/news/home/20220327005040/en/CellPoint-Digital-Appointed-by-Virgin-Atlantic-and-Holidays-as-Payment-Partner
- https://www.qantas.com/en-au/book/flights/payment-options · https://aucklandairport.net/flights/airlines/

**Regulatory & market context**
- https://www.rnz.co.nz/news/business/597751/card-payment-surcharge-ban-to-go-ahead-finance-minister-says
- https://www.rba.gov.au/payments-and-infrastructure/review-of-retail-payments-regulation/2025-07/submissions/pdf/a4anz.pdf
- https://www.apple.com/nz/newsroom/2024/11/apple-launches-tap-to-pay-on-iphone-in-new-zealand/
- https://amadeus.com/en/newsroom/press-releases/air-new-zealand-distribution-agreement

**Complaints**
- https://www.nzherald.co.nz/travel/air-nz-refund-how-long-should-you-wait-for-an-airline-refund/ATKJEUNZWJEQZL4SIPCXMKJMB4/
- https://www.trustpilot.com/review/airnewzealand.co.nz *(403 — unread)*

</details>
