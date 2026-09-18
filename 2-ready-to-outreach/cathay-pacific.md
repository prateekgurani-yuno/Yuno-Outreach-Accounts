# Cathay Pacific

**Status:** 🟢 Ready to outreach — 12-touch sequence drafted
**ICP Score:** 18 / 29 → ⭐ **High Priority** — earned on arithmetic, no override
**Industry:** Airlines (full-service + wholly-owned LCC) · **HQ:** Hong Kong — Cathay Pacific Airways Ltd, **HKEX 00293** · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** **Coverage play, not displacement.** No orchestrator detected, but **Adyen is confirmed and consolidated — in six markets out of 100+ destinations.** The pitch is the gap between those two numbers, never "you need orchestration".

---

> ## ⚠️ FIRST — a number in our own skill file was wrong, and it has been corrected
>
> `.claude/commands/full-outreach.md` said Cathay *"expanded to Adyen direct acquiring across **45+ markets**"*. **That is false.** I fetched the Adyen release myself:
>
> **Adyen provides direct acquiring for Cathay Pacific in six markets — Hong Kong, Australia, New Zealand, the United States, Japan and, most recently, India.** (Adyen newsroom, **23 March 2026**.) **The number 45 appears nowhere on the page**, nor in any syndication of it. Fintech Hong Kong headlined it *"Across 6 Key Markets"*.
>
> **Walking in citing 45 markets would have been repeating a number the merchant knows is false.** The skill file is fixed.
>
> Also from the release: the relationship **began in 2014**, Adyen is **not** described as sole, exclusive or primary, and Cathay reported a **10% authorisation-rate increase in India** after implementation. Named exec: **Kinto Chan, General Manager, Sales and Distribution**.

---

> ## 🎯 THE HOOK — six acquiring markets, thirty-three tenders, a hundred-plus destinations
>
> Cathay runs **33 distinct payment tenders**, enumerated on their own payment-options page: eight card schemes including **UnionPay and UATP**, Apple Pay and Google Pay, and **25 alternative methods** — among them **Digital Renminbi (e-CNY), FPS, PayMe, VietQR, QRPh, PayTo, UPI, RuPay, PayTM, PromptPay, KCP, Alipay, AlipayHK, WeChat Pay, Atome, Klarna, Affirm, Zip, iDeal and Sofort** — plus **Miles Plus Cash** split tender.
>
> **Adyen's direct acquiring covers six markets.** Cathay sells across **100+ destinations**, and **56% of all revenue originates in Greater China** — where Adyen's acquiring covers Hong Kong but **not mainland China or Taiwan.**
>
> **They already measure this.** The India result is on the public record: **+10% authorisation rate** from adding one market. That is a merchant that thinks in per-market auth rates and has published the proof.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Cathay Pacific is Hong Kong's flag carrier — **FY2025 group revenue HK$116,766m (+11.9%, ~US$15.0bn)**, attributable profit **HK$10.8bn**, its best since 2010. **28.9 million passengers** on the mainline plus **7.9 million on HK Express**, its wholly-owned and currently loss-making LCC, which runs a visibly separate payment stack.

**SimilarWeb total visits:** **Not obtained.** Geography below uses **revenue by origin of sale** from their own results, which is the better source anyway — origin of sale is where the payment is actually taken.

### Revenue by origin of sale — FY2025, HK$m
| Origin | 2025 | 2024 | Adyen direct acquiring? |
|---|---|---|---|
| **North Asia — Chinese Mainland, Hong Kong, Taiwan** | **65,846** | 61,442 | ⚠️ **Hong Kong only** |
| Americas | 16,011 | 14,615 | ✅ US |
| **Southeast Asia & Oceania** | **14,648** (+19.7%) | 12,239 | ⚠️ Australia, NZ only |
| Europe | 10,620 (+28.8%) | 8,247 | ❌ none |
| North Asia — Japan & Korea | 4,912 | 4,253 | ⚠️ **Japan only, not Korea** |
| **South Asia, Middle East & Africa** | **4,729 (+32.3%)** | 3,575 | ⚠️ **India only** |
| **Total** | **116,766** | 104,371 | |

> **The two fastest-growing origins are the two least covered.** South Asia/MEA +32.3% with acquiring in India only; Europe +28.8% with none at all.

### Accepted methods — 33 tenders, enumerated first-party
**Cards (8):** Visa · Mastercard · Amex · JCB · Diners Club · Discover · **UnionPay** · **UATP**. 3DS via Verified by Visa, Mastercard SecureCode, Amex SafeKey, J-Secure.
**Wallets:** Apple Pay · Google Pay.
**Other (25), verbatim:** Alipay · Affirm · AlipayHK · Atome · **Digital Renminbi (e-CNY)** · **FPS** · GrabPay · iDeal · KCP Credit Card · Klarna · Online Banking · **PayMe** · PayPal · PayPay · PayTM · **PayTo** · PromptPay · **QRPh** · RuPay · Sofort · **UPI** · **VietQR** · Wallets India · WeChat Pay · Zip.
**Plus Miles Plus Cash** — *"We also offer a mix of Miles Plus Cash as a payment option"*, minimum 5,000 miles, works on partner flights.

**Sourced absent:** ❌ **Octopus** — Hong Kong's flagship stored-value scheme, missing from the home carrier's checkout · ❌ PayNow (Singapore) · ❌ konbini (PayPay covers Japan instead) · ❌ GCash by name (QRPh covers PH via the national rail).

**Surcharging, confirmed and quantified:** **0.70%** on bookings departing **Australia** and **New Zealand**, capped **AUD 120 / NZD 70** per transaction, charged on the cash portion only for Miles Plus Cash, base including fare, taxes, fuel surcharges and ancillaries.

### Known PSPs
- **Adyen** — ✅ confirmed, direct acquiring in **six markets**, relationship since 2014, **+10% auth rate in India**
- ⚠️ **No second PSP could be named.** Checked the privacy notice, CSP headers and 653 KB of booking SPA bundles against 20+ vendors. **Zero hits** for Worldpay, Cybersource, Braintree, Stripe, Checkout.com, AsiaPay/PayDollar, Global Payments, Amadeus, Accelya, CellPoint. **This is not evidence of a single-PSP stack** — the payment step sits behind a live booking session nobody could reach.
- 📌 **UATP is at minimum one non-Adyen rail in production** — it settles on the airline-owned network, not a standard acquirer.

### Orchestration status
**None detected.** ⚠️ **Absence of hits, not affirmative evidence.** Searched Juspay, Spreedly, Primer, Gr4vy, APEXX, Payrails, IXOPAY, Yuno and "payment orchestration" across the privacy notice and the JS bundles. **CellPoint Digital checked hardest — it names Cebu Pacific, not Cathay.**

> **The distinction nobody could resolve, and it is the single best reason to get on a call:** is this *"Adyen as one integration with no routing layer"* or *"an in-house layer sitting above Adyen and others"*? Their self-hosted `api.` / `book.` / `flights.` topology is consistent with the latter. Consistent-with is not proof.

### Buying signals
- 📈 **+10% authorisation rate in India, published March 2026** — they measure auth by market and say so publicly
- 🌏 **20 new destinations launched in 2025; ~10% passenger capacity growth guided for 2026**; HK$100bn+ committed to fleet, cabin, lounges **and "digital innovation"**
- ✈️ **HK Express is loss-making and on a separate stack** — see the wedge below
- 🏆 **Singapore Airlines, their closest direct competitor, is on Juspay** (per our own airline reference)
- ❌ No payment RFP, no payments hire found, no named payments owner below Kinto Chan

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

### Pain Vector Extraction

```
=== PAIN VECTOR EXTRACTION ===

Motion: COVERAGE PLAY. Not greenfield in spirit, not displacement, not in-house.
        Cathay is consolidated on a strong provider and it is demonstrably working.
        The pitch is the gap between six acquiring markets and a hundred-plus
        destinations. NEVER "you need orchestration" — they have a working setup and
        published proof of it. Treat this like the in-house override: anchor on REACH,
        never on the existing decision being wrong.

Observable setup facts (verified first-hand, 2026-09-18):
- Adyen direct acquiring in SIX markets: Hong Kong, Australia, New Zealand, the United
  States, Japan, India. Relationship since 2014. NOT described as sole or exclusive.
  (Adyen newsroom, 23 Mar 2026.) *** THE NUMBER IS SIX. NEVER 45. ***
- Cathay reported a +10% authorisation-rate increase in India after implementation —
  their own published number
- 100+ destinations; 33 distinct payment tenders enumerated on their own page
- FY2025 revenue by origin of sale: North Asia (Mainland/HK/Taiwan) HK$65,846m = 56%;
  South Asia/MEA HK$4,729m +32.3%; Europe HK$10,620m +28.8%
- Adyen acquiring covers Hong Kong but NOT mainland China and NOT Taiwan — inside the
  origin region that is 56% of all revenue
- Octopus — Hong Kong's flagship stored-value scheme — is absent from a 33-tender list
  that does include e-CNY, FPS, PayMe, VietQR, QRPh, UPI, RuPay and PayTo
- Surcharging of 0.70% on AU and NZ departures, capped AUD 120 / NZD 70
- HK Express, wholly owned, loss-making, visibly separate payment stack
- 20 new destinations in 2025; ~10% capacity growth guided 2026; HK$100bn+ committed
  including "digital innovation"

Selected observations for Phase 1 (E1 bullets, ranked by materiality):
1. Their own India result -> "You published a 10% authorisation uplift in India after
   adding local acquiring there in March."
   MATERIALITY: highest. It is THEIR number, it is flattering rather than critical, it
   proves they already measure auth per market, and it makes the next bullet inevitable
   without us having to assert anything.
2. Coverage vs growth -> "That acquiring covers six markets. You fly to a hundred-plus,
   and your two fastest-growing origins — South Asia and the Middle East up 32%, Europe
   up 29% — are the two least covered."
   MATERIALITY: high. An asymmetry entirely inside their own published numbers. Both
   halves come from their own results release, so neither can be disputed.

   HELD AT 2 ON PURPOSE. Octopus is deliberately saved for LK4 and HK Express for the
   E7 manual bridge, so every later touch has fresh material rather than a re-run.

Bridge variant: B — limitations
Rationale: one visible PSP, strong multi-market growth signals. That is textbook B, and
B's "at your stage, that kind of setup usually comes with some limitations" is the only
transition that describes a coverage gap without implying the current setup is a mistake.

Hypothesis for Phase 2 (E3):
Acquiring coverage has not kept pace with where the revenue is actually growing, because
standing up local acquiring is a per-market project rather than a configuration change.
Backing logic: they proved the mechanism works and published the number — +10% in India,
from one market. The same shaped opportunity sits unharvested in mainland China, Taiwan,
Korea and the whole of Europe. Greater China alone is 56% of origin-of-sale revenue with
acquiring in Hong Kong only, and Europe grew 28.8% with none at all. This is not a
capability gap, it is a throughput gap: the rate at which new acquiring markets can be
added is slower than the rate at which the network is growing.

Success case for Phase 3 (E4):
Selected case: inDrive
Tier: 2 — same payment pattern (multi-country coverage expansion), different industry.
      STATED AS SUCH in the email.
Match rationale: DELIBERATELY NOT WINGO, and the reason matters. Wingo is the Tier 1
airline case but its numbers are approval-via-retry, and the hypothesis here is REACH.
inDrive's "10 new countries in under 8 months" is the number that actually answers the
question Cathay would ask. Forcing the airline case because the prospect is an airline
would mean proving the wrong thing. The airline credibility is supplied separately by
naming Qatar Airways, Copa Airlines and Avianca — with NO NUMBERS attached, ever.
Numbers to lead with: ~90% approval rate · 10 new countries live in under 8 months ·
50+ countries on one integration
Optional benchmark: SKIP, twice. The "~8% average authorisation uplift" is Yuno's own
blog figure, not third-party evidence — and it would be absurd to quote an 8% average at
a merchant that has published its own 10%. The IATA/EDC "$20.3bn / 2.1% of industry
revenue" figure is untraced to the primary source per our own skill file. Not used.

Touch-by-touch angles:
- E2 angle: six markets vs a hundred-plus -> ONE mechanism: routing to local acquirers
  per geography, added as configuration rather than as a per-market integration project
- LK1 angle: the India +10% and the question it invites, one sentence
- LK2 angle: coverage has not kept pace with where the revenue is growing
- LK3 angle: inDrive — 10 new countries live in under 8 months
- LK4 angle: FRESH — Octopus absent from a 33-tender list, on the home carrier's checkout
- E8 angle: clean exit, offer to circle back after the FY2026 interim results
```

**Calendar.** Day 1 anchored to **Monday 5 October 2026**, deliberately clearing **National
Day (1 Oct)** and the Mid-Autumn holiday week entirely rather than threading between them.

> ⚠️ **Two Hong Kong holidays inside the window are NOT verified and must be checked before
> send: the day following Mid-Autumn Festival (late Sep) and Chung Yeung Festival (mid-to-late
> Oct, lunar-dated).** I have not confirmed either 2026 date and will not guess at one. **Day 11
> is placed on Tue 20 Oct rather than Mon 19 Oct as a hedge against Chung Yeung.** Re-check
> against the Hong Kong Government's published 2026 general holidays before Touch 1 goes out.

**Times are HKT (UTC+8), which is IST+2:30.** Slots run 14:00–16:00 HKT, i.e. 11:30–13:30 IST —
comfortably inside both working days.

---

### Phase 1 — Curiosity (Days 1–5)

#### Touch 1 — Email 1 · Day 1 · Mon 5 Oct

**Subject:** Your India auth result, and the other markets

```text
Hey {{recipient.first_name}},

Spent some time on Cathay's payment setup. Two things stood out:

- You published a 10% authorisation uplift in India after adding local acquiring there in March.
- That acquiring covers six markets. You fly to a hundred-plus — and your two fastest-growing origins, South Asia and the Middle East up 32% and Europe up 29%, are the two least covered.

At your stage, that kind of setup usually comes with some limitations.

I work at Yuno — top-100 fintech, a16z-backed. We consider ourselves the 'everything payments' platform: one integration, every PSP, every method, every market.

Rather than pitch you based on assumptions, is there anything payment-related you're working through that we might be able to help with?

Best,
Prateek
```

#### Touch 2 — Email 2 · Day 3 · Wed 7 Oct · REPLY IN THREAD

```text
Hey {{recipient.first_name}},

Following up — wanted to put a bit more behind what Yuno actually does, and how it would address what I flagged.

- We sit above your existing providers. Additive, and nothing you have today gets touched.
- Routing is per geography, so cards issued in a market can be acquired locally in that market rather than cross-border.
- Adding an acquirer in a new market becomes a configuration change rather than an integration project.
- One integration covers every PSP, method and market, so the next twenty destinations don't each need their own build.

On the coverage point specifically — the India result already proved the mechanism at Cathay. The constraint isn't whether local acquiring lifts auth, you've published that it does. It's how many markets a year you can stand one up in.

I'll keep sharing what I'm seeing every few days. If your stack's where you want it, just say the word and I'll back off — otherwise happy to go deeper.

Cheers,
Prateek
```

#### Touch 3 — LinkedIn message 1 · Day 5 · Fri 9 Oct

```text
Hey {{recipient.first_name}} — figured I'd flag this here too in case more useful than email. Quick one: the 10% auth uplift Cathay published for India came from adding local acquiring in one market, and that acquiring now covers six of a hundred-plus destinations. Curious if that maps to anything you're working through on the payments side.
```

---

### Phase 2 — Diagnosis (Days 7–9)

#### Touch 4 — Email 3 · Day 7 · Tue 13 Oct · NEW EMAIL

**Subject:** Acquiring coverage vs where revenue is growing

```text
Hey {{recipient.first_name}},

Going to take a swing at this — based on what I see, my read is that acquiring coverage hasn't kept pace with where the revenue is actually growing, because standing up a new market is a project rather than a setting.

Two things point that way. Greater China is 56% of origin-of-sale revenue and the acquiring there covers Hong Kong, not the mainland and not Taiwan. And Europe grew 28.8% last year with no local acquiring at all.

None of that is a capability question — you've already published the 10% India result. It's a throughput one.

At Yuno (a16z-backed, top-100 fintech), we sit above your existing PSPs so a new acquiring market is configuration rather than a build — keep your stack, add what's missing.

Thursday is open for me — would 15:00 or 16:00 your time work for a quick 15 minutes?

Best,
Prateek
```

#### Touch 5 — LinkedIn message 2 · Day 9 · Thu 15 Oct

```text
Hey {{recipient.first_name}} — sent a longer note over email this week. Short version: acquiring coverage looks like it's grown slower than the network has, and the two origins growing fastest are the two with the least of it. If that's anywhere on your radar, would Tuesday the 20th at 14:00 your time work for a quick 15?
```

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · Tue 20 Oct · NEW EMAIL

**Subject:** How inDrive added 10 countries in 8 months

```text
Hey {{recipient.first_name}},

On the read I shared last week — sharing an example of what solved looks like. It's mobility rather than aviation, and I've picked it deliberately: the airline cases in our library prove retry and approval, and your question isn't approval, it's reach.

inDrive put Yuno above its existing providers:

- 10 new countries live in under 8 months (you read that right)
- ~90% approval rate across the estate
- 50+ countries running through one integration

Same orchestration layer above their existing stack — no rip-out. On the aviation side, Qatar Airways, Copa Airlines and Avianca run on the same layer.

One thing I'm genuinely curious about: when you added India, how much of the elapsed time was the acquiring relationship versus the integration work on your side?

Thursday the 22nd is open — would 15:30 your time work?

Full case here if useful: https://y.uno/en/success-stories/indrive

Thanks,
Prateek
```

#### Touch 7 — Email 5 · Day 13 · Thu 22 Oct · ⚠️ MANUAL

> **Placeholder — Prateek writes this one.**
>
> **Suggested angle:** the **0.70% AU/NZ departure surcharge**, capped AUD 120 / NZD 70, on a
> base that includes fare, taxes, fuel surcharges and ancillaries. Adyen acquires locally in
> both those markets and Cathay *still* surcharges there — which makes surcharge policy a
> pricing decision rather than a cost pass-through, and a genuinely interesting thing to ask
> about. ⚠️ **Ask, don't assert.** We do not know their cost of acceptance in those corridors
> and guessing at it would be the fastest way to lose a payments audience.

#### Touch 8 — Email 6 · Day 15 · Mon 26 Oct · ⚠️ MANUAL

> **Placeholder — different format from E5.**
>
> **Suggested angle:** a one-page table of their own 33 tenders mapped against the six
> acquiring markets and the six origin-of-sale regions from their results. It is entirely
> built from their own published material, it takes about twenty minutes, and it makes the
> coverage gap visual rather than argued. **The blank cells do the work.**

#### Touch 9 — LinkedIn message 3 · Day 17 · Wed 28 Oct

```text
Hey {{recipient.first_name}} — inDrive went live in 10 new countries in under 8 months on one integration, without changing providers. Worth 15 minutes to see if it maps to your setup? Friday the 30th at 14:30 your time is open.
```

---

### Between Phases (Day 19)

#### Touch 10 — Email 7 · Day 19 · Fri 30 Oct · ⚠️ MANUAL

> **Placeholder — manual creative bridge.**
>
> **Freshest unused anchor: HK Express.** Wholly owned, currently loss-making, and running a
> visibly separate payment stack from the mainline. A group that has proved local acquiring is
> worth 10% in one market is running its LCC on different rails entirely. That is a real
> question and it is nobody's fault. ⚠️ **Frame it as a group-architecture question, never as
> "your LCC is losing money"** — that reads as a dig at a business unit the reader may own.

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21 · Tue 3 Nov

```text
Hey {{recipient.first_name}} — last LK ping from me on this. One thing I never worked out: your checkout carries 33 tenders including e-CNY, FPS, PayMe and PayTo, and no Octopus. If timing works, Thursday the 5th at 16:00 your time is open for a quick 15.
```

#### Touch 12 — Email 8 · Day 23 · Thu 5 Nov · REPLY IN THREAD to E3

```text
Hey {{recipient.first_name}},

Going to stop pinging unless you want to pick this back up.

You're coming off the best result since 2010 with capacity guided up around 10%, so a new payments workstream may simply not be this year's problem. If timing's just off, happy to circle back after the interim results.

If it ever comes back up, just reply here.

All the best,
Prateek
```

---

### ⚠️ Send-time checklist — five things before Touch 1 goes out

1. ⛔ **Never say "45 markets." It is six.** The correction at the top of this file exists
   because our own skill file carried the false number. Cathay would know instantly.
2. ⛔ **Never suggest they need orchestration.** They have a working, published, measured
   setup. The entire sequence is about reach, and one sentence breaking that would end it.
3. ⛔ **Never name the orchestrator Singapore Airlines runs.** Naming a competitor is
   forbidden, and it is also the fastest way to make this look like a vendor bake-off.
4. ⚠️ **Verify the 2026 Hong Kong general holidays** — Mid-Autumn and Chung Yeung are lunar
   and I have not confirmed either date. Day 11 is already hedged onto a Tuesday.
5. ⚠️ **Re-confirm the Octopus absence** on the live payment-options page before LK4. It is a
   33-item list and lists change.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 18 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED as a bound, ~600,000+ bookings/month floor.** Sourced from their own FY2025 results: **28.9m mainline passengers plus 7.9m HK Express = 36.8m**, 79,100 and 21,700 per day respectively. **Billing unit: bookings, not passengers** — multi-passenger PNRs settle as one transaction, and agency/GDS/interline volume never touches their checkout at all, settling through BSP/IATA. Pushing back up: ancillaries, change and cancellation fees, the Cathay Shop, Cathay Holidays and Miles Plus Cash each authorise separately. **Even at an implausible 4 passengers per booking with zero ancillaries, 36.8m ÷ 12 ÷ 4 ≈ 767k/month.** Clears the top band under any divisor. ⚠️ Direct-channel share, transaction count and average ticket value are **not disclosed** — do not put a precise number in an email. |
| Orchestration status | **+4** | ✅ **None detected.** ⚠️ **Honest caveat: absence of hits, and nobody could distinguish "single Adyen integration" from "in-house layer above it."** Weaker than the affirmative greenfield calls elsewhere in this repo. |
| 3+ countries | **+3** | ✅ **100+ destinations**, revenue reported across **six origin-of-sale regions**, all six above HK$4.7bn. |
| Multiple PSPs | **0** | ⬜ **Only Adyen could be named.** UATP is a scheme settling on an airline-owned network, not a PSP, so it does not satisfy the 2+ rule. **The stack composition beyond Adyen is genuinely unknown** — the checkout requires a live PNR. |
| Local rail or licensing gap in a top-3 market | **0** | ❌ **Deliberately not awarded, and the reason matters.** With **33 tenders including e-CNY, FPS, PayMe, VietQR, QRPh, PayTo and UPI**, this merchant has done local methods unusually well. The only clear absence is **Octopus**, which is dominant in HK transit and retail but marginal for high-ticket online travel. **Awarding a rail gap here would be stretching. The gap in this account is acquiring coverage, not method coverage** — and that is a different and better argument. |
| Recent expansion | **+2** | ✅ **20 new destinations in 2025**, ~10% capacity growth guided for 2026, and **India acquiring added March 2026**. |
| Payment issues reported | **0** | ⬜ None found. Not searched to exhaustion, but nothing surfaced. |
| Funding >$10M | **0** | ❌ HKEX-listed. No round. |
| High traffic outside home | **+2** | ✅ **North Asia including Hong Kong is 56% of origin-of-sale revenue**, so Hong Kong alone is materially below the 60% threshold. ⚠️ **Basis is audited origin-of-sale revenue, not traffic** — no traffic data exists. Same approach the YesStyle and Amorepacific files took. |
| Competitor using orchestration | **+2** | ✅ **Singapore Airlines — Cathay's closest direct competitor — is listed on Juspay's own airline page**, per our airline reference. A premium Asian full-service carrier already running an orchestration layer is directly usable competitive intelligence. |
| Payment job postings | **0** | ⬜ None found; the careers site is JS-rendered and returned nothing server-side. |

**Tier: 18 / 29 → ⭐ High Priority.** No analyst override applied.

> **Why it earns ⭐ despite two zeroes.** The volume is enormous and sourced, the market count is genuine, the expansion is dated and first-party, and a direct competitor is already orchestrated. The two zeroes are honest: only one PSP is nameable, and **I refused to invent a rail gap at a merchant running 33 tenders.** The account's strength is the acquiring-coverage gap, which the matrix has no row for.

---

### ⭐ The sharpest commercial wedge — HK Express

**A wholly-owned, loss-making LCC on a visibly separate payment stack.**

- **FY2025: passenger revenue HK$6,394m (+6.7%), 7.9 million passengers (+29.7%)** — and **explicitly called out in the group release as a drag on profit**
- **Nine pricing currencies** — HKD, JPY, USD, CNY, KRW, THB, TWD, PHP, MYR — with method availability varying by currency
- **Its methods:** major cards, **Alipay, AlipayHK, Alipay+, Apple Pay, Google Pay, PayMe, UnionPay, WeChat Pay**, plus vouchers
- **Two hard differentiators from the mainline:** ① **Alipay+ is on HK Express and NOT on Cathay mainline** — the mainline lists Alipay and AlipayHK as separate tenders, a different wallet-aggregation approach entirely. ② HK Express carries **none** of the mainline's FPS, PayPal, Atome, Klarna, Affirm, Zip, PromptPay, UPI, e-CNY, VietQR, QRPh or UATP
- **Different CMS too** — HK Express on Sitecore Cloud, mainline on Adobe AEM. Independent digital estates
- ⚠️ **No PSP named anywhere on the HK Express estate**, and no Adyen string in its HTML — a weak negative, same caveat as the mainline

> **Why this is the wedge: LCC economics make MDR a board-level line item in a way it never is at a full-service carrier.** A loss-making subsidiary, a fast-growing Japan/Korea/SEA network, nine pricing currencies, a thinner separately-built stack, and no evidence it sits on the parent's Adyen relationship. **Group consolidation across two airlines is a story with a number attached.**

### Source Notes
- ✅ **The Adyen release was fetched and verified by me**, independently of the agent. Six markets, 23 March 2026, +10% India, relationship since 2014, not described as sole or exclusive, **and the number 45 appears nowhere on the page.**
- 📌 **Our own skill file has been corrected.** `.claude/commands/full-outreach.md` previously carried the false "45+ markets" claim in the shared airline reference, which would have propagated into every airline sequence. Fixed 2026-09-18 with the correction recorded inline.
- ✅ **All 33 tenders, the 3DS schemes, the surcharge terms and Miles Plus Cash come from Cathay's own payment-options page**, identical across the en_HK and en_US locales. The page itself notes *"Options may differ by market and product."*
- ✅ **FY2025 financials extracted from the results announcement PDF** and the 11 March 2026 release, not from a news summary.
- ⚠️ **`pay.cathaypacific.com` is NOT a payment gateway.** I checked it myself expecting the Ticketek `pay.` pattern — it is a **card-issuing marketing hub** fronting the Standard Chartered Cathay Mastercard co-brand, titled *"Earn miles faster"*. **Do not read it as acquiring infrastructure.**
- ⚠️ **CSP headers are a dead end here** — `script-src 'self' … https:` is wide open and lists no PSP domains. Absence of PSP JS in the marketing shell is **not** evidence of an in-house stack; the checkout is deeper in the funnel than any unauthenticated fetch reaches. `book.cathaypacific.com` returned 503.
- ⚠️ **The long-tail-APM hypothesis is NOT verified.** It is plausible that a six-market acquirer is not terminating e-CNY, VietQR, QRPh, PayTo and UATP end-to-end — **but nobody checked Adyen's published method coverage.** **Do not claim "Adyen can't do these" until someone reads `docs.adyen.com/payment-methods` method by method.**
- ❌ **Not established:** whether Adyen is sole or one of several; who processes the other ~27 markets; whether an in-house routing layer exists; transaction counts, direct-channel share, average ticket value, ancillary attach rate; current MDR or any auth figure beyond the India +10%; any named payments owner below Kinto Chan.
- 📌 **Highest-value unspent lead:** the **full Annual Report 2025** was never opened. The abbreviated results announcement contains **zero occurrences** of "payment", "digital", "e-commerce" or "ancillary" — the annual report is where a payments programme would surface.

### Manual Research Recommendations
> **1. Open the FY2025 Annual Report.** The unspent lead most likely to name a payments or digital-commerce programme.
> **2. Settle the in-house question on a call** — "is Adyen one integration, or is there a layer above it?" Nothing public answers it, and it decides the entire motion.
> **3. Check Adyen's published method coverage** for e-CNY, VietQR, QRPh, PayTo and UATP before implying any coverage gap.
> **4. Find the payments owner.** Kinto Chan (GM Sales & Distribution) is the only named exec; the actual owner sits below him.

---

## Executive Summary

Cathay Pacific is Hong Kong's flag carrier — **FY2025 revenue HK$116.8bn (~US$15.0bn, +11.9%)**, its best profit since 2010, **28.9 million mainline passengers plus 7.9 million on wholly-owned HK Express**. It runs **33 distinct payment tenders** including e-CNY, FPS, PayMe, VietQR, QRPh, PayTo, UPI, UATP and Miles Plus Cash split tender — an unusually well-built method estate. **The gap is not methods, it is acquiring coverage: Adyen provides direct acquiring in six markets against 100+ destinations**, with **56% of revenue originating in Greater China** where that covers Hong Kong but not the mainland or Taiwan, and with the two fastest-growing origins — South Asia/MEA at +32.3% and Europe at +28.8% — covered by India alone and not at all respectively. **They already measure this and published the proof: +10% authorisation rate in India from adding one market.** The sharpest wedge is **HK Express** — loss-making, called out as a drag on group profit, on a separate CMS, nine pricing currencies, a materially thinner method set, and no evidence it sits on the parent's Adyen relationship. **The motion is coverage and group consolidation, never "you need orchestration"** — and the "45 markets" figure in our own reference file was false and has been corrected.

</details>
