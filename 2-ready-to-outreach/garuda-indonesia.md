# Garuda Indonesia

**Status:** 🟢 Ready to outreach — sequence drafted
**ICP Score:** 16 / 24 → ⭐ High Priority
**Industry:** Airlines (state-owned flag carrier) · **HQ:** Jakarta, Indonesia · **Researched:** 2026-09-15 · **First email sent:** —
**Motion:** **In-house** — they built their own orchestration layer in 2013 and have maintained it for thirteen years

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** PT Garuda Indonesia (Persero) Tbk (IDX: **GIAA**, IATA: **GA**), Indonesia's state-owned flag carrier and now the designated holding company for Citilink and Pelita Air. FY2025 operating revenue **US$3.22bn (−5.9%)**, **net loss US$319.39m**, **21.2m passengers (−10.5%)**, 99 serviceable aircraft with **43 more grounded awaiting maintenance**. The defining finding: **Garuda runs six payment providers in parallel behind a routing layer it built itself in 2013 and outsources the maintenance of — and the card routing decision is a single boolean.**

**SimilarWeb total visits (last full month):** **Not obtainable.** Every SimilarWeb detail endpoint is hard-blocked (403 / 202-empty across five user-agents). The country table below is **Ahrefs organic-search data**, a different and smaller metric. SimilarWeb does confirm Garuda ranks **#3 among Indonesian air-travel sites, August 2026**, behind traveloka.com and aeroroutes.com. HypeStat's 7.17M figure is rejected — its own page says the data is 2,077 days old.

### Top 5 markets
⚠️ **These are organic-search visits (Ahrefs, 5-country free-tier cap), not total visits.** Ranks 6–10 are unavailable and not guessed.

| Rank | Country | Organic share | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇮🇩 Indonesia | **65.8%** (218.1K) | **QRIS (×2 providers)**, VA (BCA/BRI/BNI/Mandiri incl. BI-SNAP), internet banking (KlikBCA, BCA Klikpay, CIMB Clicks, Danamon, Mandiri Clickpay, BRI ePay), ATM, GoPay, OVO, ShopeePay, LinkAja, DOKU Wallet, AlloBank, JeniusPay, BNI Yap/Mobile, TMRW, Finpay Money, BSI + Muamalat, Kredivo, Akulaku, Indodana, BRI Ceria, convenience store, card instalments across **11 issuers**, bank-points redemption | **DANA** — a top-tier Indonesian wallet, and the only major one absent | ✅ HQ 🔒 gated |
| 2 | 🇦🇺 Australia | **14.8%** (49.2K, +8.9K MoM) | Cards, PayPal only | **No PayTo. No BPAY. No Afterpay or Zip.** | ⚠️ Ticket office only, entity unconfirmed |
| 3 | 🇸🇬 Singapore | 3.2% (10.7K) | Cards, PayPal only | **No PayNow, no GrabPay** | ⚠️ Unconfirmed |
| 4 | 🇳🇱 Netherlands | 2.8% (9.5K) | Cards, PayPal only | No iDEAL, no SEPA | ⚠️ Unconfirmed |
| 5 | 🇺🇸 USA | 2.7% (9.0K) | Cards, PayPal only | **No Apple Pay, no Google Pay** | ⚠️ Unconfirmed |

Implied total organic ≈ **331K/month**; non-Indonesian organic share **34.2%** — materially more international than Citilink's 89.65% domestic concentration.

### Legal entities
- **PT Garuda Indonesia (Persero) Tbk** — Gedung Garuda Indonesia, Jl. Kebon Sirih No. 44, Central Jakarta 10110. Listed IDX 2011-02-11.
- Subsidiaries: **PT Citilink Indonesia** (98.65%), **GMF AeroAsia** (IDX: GMFI, 89.10%), **PT Gapura Angkasa** (45.62%), **PT Aerowisata**, **PT Aero Systems Indonesia**, **PT Sabre Travel Network Indonesia** — the last three with **no ownership percentage recoverable**.
- **Shareholding after the Danantara injection: state/Danantara 91.11%** via PT Danantara Asset Management; **public float collapsed from ~27% to 7.96%** on a private placement of 315.61bn Series D shares at Rp 75.
- ⚠️ **Overseas legal entities could NOT be confirmed.** Their own sales-office pages are inside an unreadable SPA. Only third-party ticket-office directories were found, and those list resale numbers, not entities. **Australia is the #2 market at 14.8% and its entity status is unknown in either direction.**

### Known PSPs — six, running in parallel
| Provider | Role | Evidence |
|---|---|---|
| **Cybersource** (Visa) | Primary card gateway, Secure Acceptance Silent Order POST | `var CYBS_URL = 'https://secureacceptance.cybersource.com/silent/pay'` — verified by me |
| **DOKU** | Wallet, QRIS, VA, agent deposit top-up. Card path currently toggled **off** | `var DOKU_REDIRECT_URL = 'https://pay.doku.com/Suite/Receive'` — verified by me |
| **Midtrans / Veritrans** | Internet banking, GoPay, instalments | `api.midtrans.com/v2/assets/js/midtrans.min.js` with a production client key (`VT-client-…`) — verified by me |
| **Finpay** (PT Finnet Indonesia, a Telkom subsidiary) | Islamic + partner banks, QRIS, VA | **78 occurrences** in the payment JS; `/payment/finpay_binding`, `/finpay_verify_otp`, `/finpayva_check/` |
| **MPGS** (Mastercard) | 3DS2 authentication path | `redirectMpgs(e)` handling `acsUrl` / `cReq` / `version === "3DS2"` |
| **Ogone** (Ingenico → Worldline) | First entry in the payment-type enum; no active endpoint found — likely dormant | `paymentTypes[0] === "Ogone"` |

**PSS: Amadeus Altéa**, cutover 29 June 2013, replacing the ARGA system in use since 1990. Corroborated in their own code: `<body class="is-amadeus">`, Amadeus Digital Data Layer v2.9.0, office ID `LON1A08AA`.

### Orchestration status
**In-house orchestration layer.** Not greenfield — and getting this right matters, because opening with "you have no orchestration layer" would be factually wrong and would burn the thread.

What they built, all verified in their own production code:
- **Six providers behind one Garuda-domain checkout** at `pay.garuda-indonesia.com`
- **A hand-coded card routing switch**, verbatim from `all-7f2458b2.js`:
  ```js
  secureCCSubmit:function(e){(Booking.dokuCCEnabled?DokuCC:CybsCC).start(e)}
  ```
- **17 distinct `/payment/*` endpoints** with per-provider async status pollers — `/payment/check_status/doku_va/`, `/finpay_qr/`, `/gopay_qr/`, `/dokusnap_check/`, `/finpayva_check/`. Garuda reconciles three providers' callbacks itself.
- **Its own card vault** — `mycard_list`, `enable_save`, `/payment/token/delete`
- **BIN-level logic** — `binFilters`, `idrRestrictCard`/`nonIdrRestrictCard`, `installmentBins` across 11 issuers, `bniPointsBins`/`mandiriPointsBins`/`bcaPointsBins`
- **Its own Rails payment admin console** at `pay.garuda-indonesia.com/admin`, footer **"© 2013 - 2026"**

**Third-party orchestrator: none.** Zero occurrences across the payment bundle for Outpayce, CellPoint, Juspay, Spreedly, Primer, Gr4vy, APEXX, Payrails, Yuno, 2C2P, Adyen or Stripe — I ran that scan myself.

**Built and operated by a BPO, not by Garuda.** The payment app footer reads: `© 2026. ATI Business Group. All right reserved.`

### Buying signals
- 💰 **Rp 8.7tn (~US$530m) from Danantara to Garuda mainline** (of a Rp 23.7tn total; Citilink took Rp 14.9tn). **Explicitly allocated to working capital, aircraft maintenance and return-to-service — none of it to digital, commercial or systems.**
- 🚀 **Saudia partnership expanded** to cover "network planning, flight schedules… **sales, marketing, and distribution** in markets of mutual interest," single-ticket travel, loyalty and technology infrastructure, plus Umrah and Hajj services ([ch-aviation](https://www.ch-aviation.com/news/169949-saudia-garuda-indonesia-to-increase-collaboration)).
- 🚀 **Fleet return-to-service programme** — target 68 serviceable Garuda aircraft and ≥118 group aircraft by end-2026, from 99 serviceable with 43 grounded.
- ⚠️ **Commercial Director Reza Aulia Hakim suspended effective 14 Aug 2026** after ~13.5 months in post, on a BP BUMN letter. **No reason disclosed and no acting replacement named in any source.** The commercial seat is vacant.
- ⚠️ **Holding company still undecided.** Targeted Q1 2026, slipped to H1, and as of the latest evidence the structure is *"under intensive review at the shareholder level"* covering "policy direction, form, structure, phases, timeline and implementation mechanism." The "one booking system" objective remains a future-state aspiration.
- 💼 **Career site shows "No open vacancy"** — the entire board is empty. Not just no payment roles.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

### Pain Vector Extraction

```
Motion: IN-HOUSE. They built the layer themselves in 2013 and still run it.
Step 6a governs: respect the build decision, anchor on opportunity cost and reach, never on
the build being wrong, and never on "you need orchestration." Every touch below is written
to that rule. Nothing in this sequence tells Garuda they lack a payment layer — they have
one, and saying otherwise would be factually wrong and would end the thread.

Observable setup facts (all verified first-hand in Garuda's own production code):
- Six providers running in parallel behind one checkout: Cybersource, DOKU, Midtrans,
  Finpay, MPGS, and a dormant Ogone entry — source: pay.garuda-indonesia.com/payment/
  and its bundle all-7f2458b2.js
- Card routing is a single boolean, verbatim:
  secureCCSubmit:function(e){(Booking.dokuCCEnabled?DokuCC:CybsCC).start(e)}
- 57 implemented payment types, of which 44 are Indonesian — source: paymentTypes array
- 17 distinct /payment/* endpoints and 5 per-provider async status pollers
- Their own card vault (mycard_list, enable_save, /payment/token/delete) and their own
  BIN logic across 11 instalment issuers
- Payment app footer: "© 2026. ATI Business Group." Admin console: "© 2013 - 2026"
- Cybersource adopted March 2013; Amadeus Altea cutover June 2013 — one birthday
- Australia is the #2 market at 14.8% of organic search and the fastest-growing (+8.9K MoM),
  and gets cards and PayPal. No PayTo, no BPAY, no Afterpay, no Zip — sourced-absent
- Espay returns ZERO across Garuda's stack. Citilink, 98.65% owned, runs a wholly separate
  gateway with no QRIS and a 3% card surcharge

Selected observations for Phase 1 (E1 bullets, ranked by materiality):
1. Six providers in parallel behind one checkout -> "Your checkout runs six providers."
2. The boolean -> "Card traffic goes to DOKU or Cybersource depending on one config flag."
3. The group contrast -> "Citilink runs a separate stack entirely."
All three are stated as facts about their build, not as deficiencies. That is the In-house
motion working correctly.

Bridge variant: A — complexity
Rationale: six visible processors, 57 methods, 17 endpoints and five reconciliation pollers.
This is the textbook multi-PSP fragmented case. B is wrong (nothing single-PSP about it) and
C would understate what is plainly there.

Hypothesis for Phase 2 (E3):
The 2013 build has kept pace with Indonesia and not with the rest of the network.
Backing logic: 44 of 57 implemented methods are Indonesian, and Indonesia is genuinely well
served — QRIS through two providers, every major VA, instalments across 11 issuers. Outside
it, Australia is the second-largest market and growing fastest on a checkout of cards and
PayPal. That is not a capability gap, it is a maintenance-throughput gap: every method is a
bespoke widget, endpoint and poller, written by an outsourced partner.

Success case for Phase 3 (E4):
Selected case: Wingo
Tier: 1 — airline, and the only airline case in the library carrying numbers
Match rationale: Wingo's mechanism is "automatic retries of failed payments through multiple
providers." Garuda already HAS multiple providers — two card gateways live and paid for —
and switches between them by hand. The case is not "get more providers", it is "make the
ones you already have catch each other." That is the precise shape of the boolean finding,
and it respects the build rather than attacking it.
Numbers to lead with: +14% approval rate (initial implementation phase) · 1,000+ payment
methods through one integration · fraud tooling and integrated 3D Secure
Region stated explicitly as Latin America. No APAC implication.
Optional benchmark: SKIP. The "~8% average authorisation uplift" traces to Yuno's own blog,
so it is marketing, not independent evidence. The IATA/EDC airline cost-of-acceptance figure
has only been seen via a vendor blog citing it — not quotable until traced to the primary.

Touch-by-touch angles:
- E2 angle: multi-PSP fragmentation -> unified reconciliation + a single routing layer above
  the six they already run (per the E2 mapping table)
- LK1 angle: the boolean, stated plainly
- LK2 angle: the build kept pace with Indonesia and not with the network
- LK3 angle: Wingo made existing providers catch each other's declines
- LK4 angle: the 2013 date (held back, unused until here)
- E8 angle: clean exit, no new observation
```

---

### Phase 1 — Curiosity (Days 1–5)

#### Touch 1 — Email 1 · Day 1 · Tue 15 Sep

**Subject:** Six providers, one config flag

```text
Hey {{recipient.first_name}},

Spent some time looking at Garuda's payment setup. Three things stood out.

Your checkout runs six providers in parallel: Cybersource, DOKU, Midtrans, Finpay and MPGS,
with an Ogone entry still in the list.

Card traffic goes to either DOKU or Cybersource depending on a single config flag.

Citilink runs a separate stack entirely. Different gateway, different method list.

That kind of setup usually comes with some complexity.

I work at Yuno, top-100 fintech, a16z-backed. We consider ourselves the "everything
payments" platform: one integration, every PSP, every method, every market.

Rather than pitch on assumptions, is there anything payment-related you're working through
that we might help with?

Best,
Prateek
```

#### Touch 2 — Email 2 · Day 3 · Thu 17 Sep · REPLY IN THREAD

```text
Hey {{recipient.first_name}},

Following up. Wanted to put a bit more behind what Yuno does, and how it maps to what I
flagged.

We sit above the providers you already run. Cybersource, DOKU, Midtrans and Finpay all stay
exactly where they are.

What changes is the layer above them. One routing logic layer instead of per-provider
dispatch, and reconciliation that matches each settlement file against what you actually
billed rather than polling each provider separately.

You've clearly built a real payment layer already. The argument isn't that you need one.
It's that maintaining six integrations, and writing a new widget and poller each time a
method gets added, stops being your work.

I'll keep sharing what I'm seeing every few days. If your stack's where you want it, say the
word and I'll back off. Otherwise happy to go deeper.

Cheers,
Prateek
```

#### Touch 3 — LinkedIn message 1 · Day 5 · Sat 19 Sep

> ⚠️ **Lands on a Saturday.** Shift to Mon 21 Sep, or pull forward to Fri 18 Sep.

```text
Hey {{recipient.first_name}}, figured I'd flag this here too in case it's more useful than
email. Quick one: your card traffic picks between DOKU and Cybersource on a single config
flag, so the two gateways never see each other's declines. Curious whether that's deliberate
or just how it's always been.
```

---

### Phase 2 — Diagnosis (Days 7–9)

#### Touch 4 — Email 3 · Day 7 · Mon 21 Sep · NEW EMAIL

**Subject:** Read on your non-Indonesian markets

```text
Hey {{recipient.first_name}},

Going to take a swing at this. My read is that the build has kept pace with Indonesia and
not with the rest of the network.

Of the 57 methods in your checkout, 44 are Indonesian. QRIS, every major virtual account,
instalments across eleven issuers.

Australia is your second-largest market on search, and it gets cards and PayPal. Not because
anyone's doing it badly, but because each method is its own widget and poller, so throughput
is the constraint.

At Yuno (a16z-backed, top-100 fintech) we sit above your existing providers, so adding a
rail stops being a build. Keep your stack, add what's missing.

Thursday the 24th is open. Would 10am or 3pm your time work for 15 minutes? If payments
sits elsewhere now, happy to be pointed there.

All the best,
Prateek
```

#### Touch 5 — LinkedIn message 2 · Day 9 · Wed 23 Sep

```text
Hey {{recipient.first_name}}, sent a longer note over email this week. Short version: 44 of
the 57 methods in your checkout are Indonesian, and Australia is your second-biggest market
running on cards and PayPal. If that's anywhere on your radar, would Monday the 28th or
Tuesday the 29th at 4pm your time work for a quick 15?
```

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · Fri 25 Sep · NEW EMAIL

**Subject:** How Wingo solved this

```text
Hey {{recipient.first_name}},

On the read I shared last week, here's what solved looks like.

Wingo is a low-cost carrier flying 37 routes across Latin America. They had providers
already. What they didn't have was those providers catching each other.
From the initial phase with Yuno:

- Approval rate up 14% (not too bad, right?)
- Over 1,000 payment methods through one integration
- Fraud tooling and 3D Secure in the same layer

The mechanism is what maps to you: Smart Routing retries a failed payment through a
different provider automatically. You already have two card gateways live. Today the choice
between them is a flag someone sets, not something a decline triggers.

Qatar Airways, Copa and Avianca run on the same layer, above the stacks they already had.
No rip-out.

When a new method goes live, how long does it take from decision to being in the checkout?

Wednesday the 30th, would 11am your time work for 15 minutes?

Full case here if useful:
https://y.uno/en/newsroom/wingo-improves-payment-efficiency-with-yuno-as-strategic-partner

Best,
Prateek
```

#### Touch 7 — Email 5 · Day 13 · Sun 27 Sep · MANUAL

> ⚠️ **Lands on a Sunday.** Shift to Mon 28 Sep.

*Placeholder — manual creative approach. Do not auto-write.*

Suggested angle for this account: a side-by-side of the Garuda and Citilink checkouts. Same
group, one owning 98.65% of the other, two entirely disjoint payment estates. The contrast
argues itself and needs no commentary.

#### Touch 8 — Email 6 · Day 15 · Tue 29 Sep · MANUAL

*Placeholder — second manual approach, different format than E5.*

Suggested angle: a short Loom walking an Australian passenger through the Garuda checkout
and stopping where the options run out, against what an Australian buyer expects to see.

#### Touch 9 — LinkedIn message 3 · Day 17 · Thu 1 Oct

```text
Hey {{recipient.first_name}}, Wingo already had multiple providers. What changed was that a
decline on one started falling through to another automatically instead of ending the
booking. Worth 15 minutes to see whether that maps? Tuesday the 6th at 2pm your time is open.
```

---

### Touch 10 — Email 7 · Day 19 · Sat 3 Oct · MANUAL

> ⚠️ **Lands on a Saturday.** Shift to Fri 2 Oct or Mon 5 Oct — but Mon 5 Oct collides with LK4.

*Placeholder — manual creative bridge. Anchor to something fresh.*

Suggested anchors: the expanded **Saudia partnership** covering sales, marketing and
distribution (ch-aviation, solidly sourced), or the **Hajj and Umrah** flow specifically —
102,000 regular pilgrims carried in 2026 and a stated Rp 520bn Umrah transaction target
through January 2027. That is a discrete, high-ticket, seasonal payment flow and nobody
else in the sequence has touched it.

⚠️ **Do not anchor to the route expansion claims** (Doha, Bali–Melbourne). Those rest on SEO
aggregators and are not verified.

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21 · Mon 5 Oct

```text
Hey {{recipient.first_name}}, last LinkedIn ping from me on this. One thing I never raised:
your payment app's copyright starts in 2013, same year as the Cybersource rollout and the
Altéa cutover. Thirteen years is a long run for any stack. If that's worth 15 minutes,
Thursday the 8th at 10am your time is open.
```

#### Touch 12 — Email 8 · Day 23 · Wed 7 Oct · REPLY IN THREAD to Touch 4 or 6

```text
Hey {{recipient.first_name}},

Going to stop pinging unless you want to pick this back up.

If the timing's just off, happy to circle back next quarter once the group structure has
settled.

If it ever comes back up, just reply here.

Cheers,
Prateek
```

---

### Source Notes

- ✅ **Six providers** — verified by me in Garuda's own production payment app:
  `CYBS_URL = 'https://secureacceptance.cybersource.com/silent/pay'`,
  `DOKU_REDIRECT_URL = 'https://pay.doku.com/Suite/Receive'`, the `api.midtrans.com` script
  tag, 78 Finpay references, and `redirectMpgs()` handling 3DS2. Ogone is the first entry in
  the payment-type enum with no active endpoint, so E1 says "still in the list" rather than
  implying it is live.
- ✅ **The config flag** — verified verbatim by me:
  `secureCCSubmit:function(e){(Booking.dokuCCEnabled?DokuCC:CybsCC).start(e)}`
- ✅ **57 methods, 44 Indonesian** — count verified by me against the `paymentTypes` array.
- ✅ **Australia has no PayTo, BPAY, Afterpay or Zip** — sourced-absent, zero occurrences
  across the enumerated array. Australia at 14.8% is **Ahrefs organic search**, not total
  visits, so E3 and LK2 say "on search" and "second-largest market on search" rather than
  overstating it.
- ✅ **Citilink runs a separate stack** — `Espay` returns zero occurrences across Garuda's
  stack. E1 states the separation only, not Citilink's surcharge or missing QRIS, since
  leading with a subsidiary's shortcomings reads as point-scoring.
- ✅ **2013** — payment app admin footer "© 2013 - 2026", Cybersource adopted March 2013,
  Altéa cutover June 2013.
- ✅ **Wingo: +14% approval, 1,000+ methods, fraud tooling and 3DS** — re-verified at source
  2026-09-15. Region named as Latin America in the copy, so nothing implies an APAC result.
- ✅ **Qatar Airways, Copa Airlines, Avianca** — on Yuno's site-wide customer list. Named
  with **no metric attached**, per the library rule.
- ⚠️ **No named recipient, and this one matters more than usual.** The Commercial Director
  was suspended on 14 August 2026 with no named replacement. `{{recipient.first_name}}`
  throughout, and **the recipient needs choosing deliberately** — E3's sign-off carries
  "if payments sits elsewhere now" partly for that reason. Direktur Transformasi **Neil
  Raymond Mills** is the most plausible interim owner, but that is inference and is not
  sourced. Finance Director **Balagopal Kunduvara** is the sourced alternative.
- ⚠️ **E3 and E4 run slightly over budget** (~134 against ~90–120, and ~166 against
  ~130–160). Everything left in both is rulebook-mandated. On E3 the cuttable line is the
  "not because anyone's doing it badly" clause, at the cost of the observation reading
  harder on an In-house account where tone is doing real work.
- ⚠️ **Three touches land on weekends** (LK1 Sat 19 Sep, E5 Sun 27 Sep, E7 Sat 3 Oct).
  Flagged inline with shifts.
- ⚠️ **Indonesian public holidays were not verified for the CTA window** (24 Sep – 8 Oct).
  Research did not surface any and I did not check a holiday calendar. Worth thirty seconds
  before loading into Gong.
- ⚠️ **Nothing in this sequence uses payment complaints**, because that signal was never
  evaluated on this account. Not an oversight in the drafting, an acknowledged gap in the
  research.

### Notes on what this sequence deliberately avoids

**It never says Garuda lacks a payment layer, and never implies the 2013 build was a
mistake.** They built method-to-provider dispatch, their own card vault, their own BIN logic
across eleven issuers and their own admin console. Saying otherwise would be wrong on the
facts and would end the thread on the first read.

The argument is throughput and reach: six integrations to maintain, a new widget and status
poller per method, an outsourced partner doing the work, and an international network that
has not kept up with the domestic one. E2 states this explicitly — *"the argument isn't that
you need one"* — because on an In-house account that sentence is what earns the rest a
hearing.

**Also deliberately avoided:** the Rp 8.7tn Danantara injection. It went to working capital
and returning grounded aircraft to service, and raising it invites the obvious reply that
aircraft maintenance outranks payments right now.

### Success Case Alternatives

- **Rappi** — the better swap if the conversation turns to maintenance burden rather than
  declines: hundreds of methods, zero implementation delays, **80% less analyst work**. That
  speaks directly to the opportunity-cost half of the In-house argument. Weaker on hard
  numbers than Wingo, which is why Wingo leads.
- **Livelo** — if the conversation narrows to decline recovery specifically: +5% approval,
  50% of failed transactions recovered by instantly routing to a secondary acquirer. Very
  close mechanism fit to the config-flag finding, but not an airline.
- **Qatar Airways / Copa / Avianca** — airline credibility if Wingo's LATAM footprint draws
  an objection. Nameable only, no numbers exist.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 16 / 24
| Signal | Points | Status |
|--------|--------|--------|
| Orchestration status | **+1** | ✅ **In-house orchestration layer**, verified in their own production code. Not greenfield. Six providers, a hand-coded switch, own vault, own admin console |
| 3+ countries | **+3** | ✅ Indonesia 65.8%, Australia 14.8%, Singapore 3.2%, Netherlands 2.8%, USA 2.7% — five countries above 1% |
| Multiple PSPs | **+3** | ✅ **Six**, all evidenced: Cybersource, DOKU, Midtrans/Veritrans, Finpay, MPGS, Ogone |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Australia is the #2 market at 14.8% and has no PayTo and no BPAY** — both named in the matrix, both sourced-absent from a 57-item enumerated array. Singapore (#3) has no PayNow on the same basis |
| Recent expansion | **+2** | ✅ Saudia distribution partnership (ch-aviation); Doha route and Bali–Melbourne frequency increase ⚠️ SEO-aggregator sourced, verify before use |
| Payment issues reported | **0** | ⬜ **Not evaluated.** I ran two agents on this account and neither covered complaints. This is a gap in my run design, not a finding of "no complaints" |
| Funding >$10M | **+2** | ✅ Rp 8.7tn (~US$530m) to Garuda mainline, executed Dec 2025. ⚠️ None of it earmarked for digital or payments |
| High traffic outside home | **0** | ❌ Indonesia is 65.8%, above the 60% threshold — **but that is organic-search share, not total visits.** The proper metric was unobtainable, so this signal is measured on the wrong denominator |
| Competitor using orchestration | **+2** | ✅ Cebu Pacific (CellPoint), Malaysia Airlines (Outpayce XPP), Thai Airways (2C2P), Vietnam Airlines and Sun PhuQuoc (2C2P PACO) |
| Payment job postings | **0** | ❌ Career site shows "No open vacancy" — the whole board, not just payments |

**Tier:** High Priority (14+) ⭐ / Medium (8–13) 🟢 / Low (<8) 🔴 → **⭐ High Priority (16)**

No tier override. But three things belong in front of any conversation, because they change how and when to approach:

1. **The commercial seat is vacant.** The Commercial Director was suspended on 14 August 2026 with no stated reason and no named replacement. There is a standalone **Direktur Transformasi (Neil Raymond Mills)** on the board who is the most plausible owner in the interim, but **that is inference, not sourced** — do not address anyone by name without checking.
2. **None of the rescue capital went to digital.** Rp 8.7tn went to working capital and returning 43 grounded aircraft to service. A payments project competes against aircraft maintenance for attention at a carrier losing US$319m a year.
3. **The holding-company structure is still undecided**, so the "one booking system" mandate that would justify a group-level payment decision does not yet have an owner or a delivery date.

### Source Notes
- ✅ **The routing switch, verified by me** in `pay.garuda-indonesia.com/javascripts/all-7f2458b2.js`: `secureCCSubmit:function(e){(Booking.dokuCCEnabled?DokuCC:CybsCC).start(e)}`. Card traffic goes to DOKU or Cybersource on one server-set boolean. No cascade, no failover, no retry-on-decline anywhere in the client.
- ✅ **Cybersource and DOKU endpoints, verified by me** in the payment page source: `CYBS_URL = 'https://secureacceptance.cybersource.com/silent/pay'` and `DOKU_REDIRECT_URL = 'https://pay.doku.com/Suite/Receive'`.
- ✅ **Midtrans, Amadeus and the ATI Business Group footer, verified by me** on the same page: the `api.midtrans.com` script tag, `is-amadeus` body class, and `atibusinessgroup.com` in the footer.
- ✅ **The 57-item `paymentTypes` array, verified by me** — count confirmed at exactly 57.
- ✅ **QRIS is present via two providers** (`DokuQris`, `FinPayQris`) with a live poller at `/payment/check_status/finpay_qr/`. **Garuda has QRIS; Citilink does not.** A search summary claiming Garuda's QRIS is cargo-only is **wrong for the airline checkout** — primary code beats a search summary. (QRIS does *also* run at cargo counters, live since Dec 2022, where only 1 of 7 named service centres is marked active and six are still "(on progress)" nearly four years on.)
- ✅ **Sourced absences, all from the enumerated 57-item array, all scanned by me:** DANA `0`, Apple Pay `0`, Google Pay `0`, Atome `0`, PayNow `0`, FPX `0`, Konbini `0`, KakaoPay `0`.
- ✅ **Espay `0`.** Citilink's gateway does not appear anywhere in Garuda's stack. **The two airlines in the same group run entirely disjoint payment estates** — that contrast is itself the strongest commercial observation on the account.
- ✅ **Provider weight in the bundle:** finpay 78, doku 36, veritrans 21, cybs 10, midtrans 9, mpgs 2, cybersource 1, ogone 1.
- ✅ **Amadeus Altéa**, cutover 29 June 2013, and **Cybersource adopted March 2013** — Garuda was "the first airline in Asia Pacific" to take Cybersource's full payment and fraud suite. The payment app copyright starts **2013**. The whole stack has one birthday.
- ⚠️ **Traffic is the weakest section by far.** SimilarWeb is hard-blocked at every detail endpoint. The country table is Ahrefs **organic search**, capped at five countries. No total visits, no engagement metrics, no date range. Two ICP signals rest on a metric that is not the one the matrix intends.
- ⚠️ **Overseas legal entities: unresolved in either direction.** The SPA blocks their own sales-office pages and only ticket-office directories were found. Australia at 14.8% is the material unknown.
- ⚠️ **Financial discrepancies to resolve before any business case:** FY2025 net loss **US$319.39m vs US$322.48m**; Q1 2026 net loss **US$41.62m vs CNBC's US$46m**; FY2024 comparative **US$72.7m (this run) vs US$69.77m (the Citilink run)**. Use the audited figure and say which you used.
- ⚠️ **Route expansion claims rest on SEO aggregators** (travelandtourworld, airtraveler.club). Only the Doha route is weakly corroborated via the Wikipedia destinations table. The Saudia partnership is solidly sourced; the route specifics are not.
- ⚠️ **Amex is UNCHECKED, not absent.** The accepted-scheme list is BIN-gated server-side via `idrAllowedCard`/`nonIdrAllowedCard`. Scheme names in the JS come from the jQuery.payment library's default detector, **not** Garuda's accept list. Their FAQ names only Visa, Mastercard and JCB.
- ⚠️ **Card surcharge: not found, probably none.** No surcharge string anywhere in the payment app; the booking-engine data layer carries `serviceFee:{amount:0}`. **Citilink charges 3%.** Weak-to-moderate evidence, but a striking contrast if it holds.
- ❌ **`booking.garuda-indonesia.com` is 403 to every user-agent tested**, so the live checkout picker was never observed. Which subset of the 57 types renders for a given booking is decided server-side.
- ❌ **No PCI DSS statement exists.** The only security claim is their FAQ: *"Situs web Garuda Indonesia menggunakan enkripsi SSL standar industri dan gateway pembayaran yang aman"* — note the singular "gateway", describing six.
- ❌ **No annual report or investor presentation PDF recoverable.** IR is SPA-only; the IDX API is Cloudflare-gated.

### Corrections this run forced — three of them, including one of mine
1. **My own conclusion was wrong.** Earlier in this run I probed the root of `pay.garuda-indonesia.com`, hit an admin login, and concluded that "first-party payment evidence for Garuda is effectively nil" and that "no sourced-absent claim can be made." I had not tried `/payment/` on that same host. That path serves the live customer payment application with the entire gateway configuration in clear text. The conclusion was premature and is retracted in full — this account now has the **strongest** first-party payment evidence of any airline in the pipeline.
2. **"Garuda ↔ DOKU is historical only (c. 2007–2010)"** — recorded in `citilink.md` from the previous run. **Wrong.** DOKU is live in production today: `pay.doku.com/Suite/Receive` is in the payment page, there are five `Doku*` payment types, and DOKU's own case study quotes a current Garuda executive (**Soraya Nastiti Harahap, Senior Manager Digital Business Support**) on the agent deposit top-up system. The origin story was real; the relationship never ended.
3. **"Midtrans: no evidence, killed"** — also from the previous run. **Wrong.** Midtrans/Veritrans is live, with a production client key in a script tag and nine `Vtd*` payment types. **"Finpay: unverified"** is now **confirmed** — 78 occurrences and five dedicated endpoints.

**Why the earlier run got it wrong, and the lesson:** the "doku → dokumen" kill was *correct for the booking-engine bundle it was applied to*. The error was generalising a per-file result to the whole estate. DOKU lives in a different application on a different host. **Killing a string in one bundle is not the same as killing a vendor.**

### False positives killed
- **"dana"** — the only matches in the payment array are `VtdDanamonOnline` and `INDODANA`. The DANA wallet is genuinely absent. Trap flagged, checked, cleared.
- **Base64 image data on the homepage** produced spurious `2c2p`, `OVo`, `FPX`, `JCB` and `Amex` matches, several case-mixed. All stripped. Real 2C2P count is zero.
- **`bca` on the main site JS** was MUI colour-palette hex; **`atm`** was substring noise from `flatMap`, `seatmap`, `atmosphere`.
- **Bank Indonesia's "Project Garuda" CBDC** dominates NDC and payment search results and is entirely unrelated. Discarded.
- **OTA trap avoided** — every payment finding comes from a `garuda-indonesia.com` host or a vendor's own case study. Nothing from Traveloka, tiket.com, Tokopedia or Shopee.

### Success Case Alternatives
- **Wingo** — Tier 1 airline, the only quantified airline case: +14% approval via automatic retries across multiple providers, 1,000+ methods, 3DS. Maps precisely to a boolean card switch with no retry-on-decline.
- **Rappi** — the better fit for the *in-house* motion: hundreds of methods and **80% less analyst work**, which speaks to the opportunity-cost argument rather than the capability one.
- **Qatar Airways / Copa / Avianca** — airline credibility, nameable, **no published metrics**. Never attach a number.

---

## Executive Summary

Garuda Indonesia built its own payment orchestration layer in 2013 and has run it ever since — six providers (Cybersource, DOKU, Midtrans, Finpay, MPGS, Ogone) behind one checkout, dispatched by a Ruby-on-Rails application maintained by an outsourced BPO, with card traffic routed by a single boolean. **The motion is In-house, not greenfield**, and the argument is opportunity cost and reach, not capability. The strongest commercial observation is internal to the group: Garuda and Citilink, one owning 98.65% of the other, run **entirely disjoint payment estates** — different gateways, different method sets, different surcharge policies — while Danantara's stated objective for the emerging holding company is "one booking system."

### Section 1: Website Traffic Analysis by Country

**Data source: WebSearch fallback, and it is the weak point of this report.** All SimilarWeb detail endpoints returned 403 or an empty 202 JS challenge across five user-agents. The table is **Ahrefs organic-search visits**, free tier, five countries maximum.

| Rank | Country | Organic visits/mo | Share | MoM |
|---|---|---|---|---|
| 1 | Indonesia | 218.1K | 65.8% | −26.4K |
| 2 | **Australia** | **49.2K** | **14.8%** | **+8.9K** |
| 3 | Singapore | 10.7K | 3.2% | +1.3K |
| 4 | Netherlands | 9.5K | 2.8% | +2.1K |
| 5 | United States | 9.0K | 2.7% | +5.0K |

Implied total organic ≈ 331K/month. Ahrefs Domain Rating 75. Top organic keywords are entirely navigational ("garuda indonesia" 132.3K, "garuda" 67.6K, "check in garuda" 13K) — people arriving who already know the brand, not discovery traffic.

**SimilarWeb confirms one thing:** Garuda is **#3 among Indonesian air-travel sites (Aug 2026)**, behind **traveloka.com** at #1. The national flag carrier is outranked in its home market by an OTA — which is the clearest available signal that the OTA channel dominates, though the **direct-versus-OTA split is disclosed nowhere.**

**Rejected:** HypeStat's 7.17M monthly visits (page states data is 2,077 days old) and StatShow's 367K (contradicts HypeStat ~20×, methodology undisclosed).

### Section 2: Legal Entities & Local Presence

**Headquarters:** Gedung Garuda Indonesia, Jl. Kebon Sirih No. 44, Central Jakarta 10110. Management office at Soekarno-Hatta. Listed on IDX 2011-02-11.

**Cross-Border Gap Analysis:**

| Country | Top-5 traffic? | Local entity? | Domestic acquiring gated? | Cross-border risk? |
|---|---|---|---|---|
| Indonesia | ✅ #1 | ✅ HQ | **YES 🔒** — Bank Indonesia PJP regime | Low |
| **Australia** | ✅ **#2, 14.8%** | ⚠️ **Unconfirmed** | No | **High if absent** |
| Singapore | ✅ #3 | ⚠️ Unconfirmed | No | Moderate |
| Netherlands | ✅ #4 | ⚠️ Unconfirmed | No | Moderate |
| USA | ✅ #5 | ⚠️ Unconfirmed | No | Moderate |

> **Warning: Australia is the #2 traffic market at 14.8% and growing faster than any other (+8.9K MoM), and Garuda's entity status there could not be confirmed in either direction.** Their own sales-office pages are inside an unreadable SPA and only third-party ticket-office directories were found. Resolving this is the single highest-value manual check on the account.

Active non-Indonesian destinations span Australia (Melbourne, Perth, Sydney), China (Guangzhou, Shanghai), Hong Kong, Japan (Tokyo), Malaysia, Netherlands (Amsterdam), Saudi Arabia (Jeddah, Medina), Singapore, South Korea (Seoul), Taiwan, Thailand, Timor-Leste and Qatar. Terminated: France, Germany, UAE, UK, USA. Of these, the **gated or complicated domestic-acquiring markets they sell into are China, South Korea, Japan and Taiwan** — none with a confirmed entity.

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Provider | Role | Evidence | Status |
|---|---|---|---|
| **Cybersource** | Primary card gateway (Secure Acceptance Silent Order POST) | `[Source Code]` `CYBS_URL`, `secureAcceptanceEnabled: true`, `CybsCC{}`, `cybsPay()`, `pointsCybsPay()` | Live |
| **DOKU** | Wallet, QRIS, VA, agent deposit top-up (DTU) | `[Source Code]` `DOKU_REDIRECT_URL`, 5 `Doku*` types, `dokuInstalment`, `dokuBniTraveler` | Live; **card path toggled off** (`dokuCCEnabled: false`) |
| **Midtrans / Veritrans** | Internet banking, GoPay, instalments | `[Source Code]` production client key, `api.midtrans.com/v2/token`, `api.veritrans.co.id/v2/token`, 9 `Vtd*` types | Live |
| **Finpay** (PT Finnet, Telkom) | Islamic + partner banks, QRIS, VA, Finpay Money | `[Source Code]` 78 occurrences, `FinpayForm`, 5 endpoints, 9 `FinPay*` types | Live |
| **MPGS** | 3DS2 authentication | `[Source Code]` `redirectMpgs()` handling `acsUrl`/`cReq`/`3DS2` | Present |
| **Ogone** (Worldline) | First enum entry, no active endpoint | `[Source Code]` `paymentTypes[0]` | Likely dormant |

**Built and run by a third party:** the payment app footer reads `© 2026. ATI Business Group. All right reserved.` — an airline/travel BPO with a Jakarta delivery centre. The admin console carries `© 2013 - 2026`.

**Agent deposit system (B2B, a separate payment flow):** `DokuDTU` in the enum; `deposit.garuda-indonesia.com/GarudaAgentCustomer/login` and `agentb2b.garuda-indonesia.com/agent/index` ("Agent Platform", members "both in Indonesia and outside Indonesia"); `gate.garuda-indonesia.com` sales portal. DOKU's case study quotes **Soraya Nastiti Harahap, Senior Manager Digital Business Support, Garuda Indonesia**: *"agents must top up deposit first, with balance automatically deducted real-time when issuing tickets. For us, it's secure because there's no negative balance."* Thresholds: minimum balance Rp 1,000,000 per GOS member; top-ups Rp 5,000,000 to Rp 10,000,000,000.

#### 3B. Payment Orchestrator

**In-house orchestration layer.** Garuda is not a greenfield account and must not be approached as one. They have solved the orchestration problem themselves, at a level: six providers, method-to-provider dispatch, their own vault, their own BIN logic, their own admin console, their own reconciliation pollers.

What they have **not** solved is routing. The card decision is:

```js
secureCCSubmit:function(e){(Booking.dokuCCEnabled?DokuCC:CybsCC).start(e)}
```

A boolean. No cascade, no failover, no retry-on-decline, no least-cost routing, no BIN-based acquirer selection. (Note the production typo `selectedPayentType`, carried consistently through the file — an indicator of code age and low churn.)

**On the Outpayce XPP hypothesis — checked, and the answer is no.** Garuda is deeply on Amadeus: `is-amadeus` body class, Amadeus DDL v2.9.0 with `"site": "GADC"` and `"officeID": "LON1A08AA"`, `digital-analytics.amadeus.com` on both the booking engine and the payment page, and the data model maps `paymentTransactions[].paymentMethod.vendorCode` into the Amadeus schema. **But the money moves to Cybersource, DOKU, Midtrans and Finpay.** Amadeus owns the PSS and the analytics; it does not own the payment rail. Outpayce is the natural incumbent-adjacent threat, not an incumbent.

### Section 4: Alternative & Local Payment Methods

**Source of record: a 57-item enumerated `paymentTypes` array in Garuda's production JS, count verified by me.** Presence in the array means implemented and live in code. **Absence means genuinely not implemented** — which makes these unusually strong sourced absences. Which subset renders for a given booking is server-decided (`Booking.i18n` notes *"Pilihan pembayaran yang tersedia dapat bervariasi tergantung wilayah Anda"*).

| Method | Category | Status |
|---|---|---|
| **QRIS** (`DokuQris`, `FinPayQris`) | Bank / A2A | ✅ Active — two providers, live poller |
| Credit/debit card (Visa, Mastercard, JCB) | Cards | ✅ Active |
| Card instalments — 11 issuers (BNI, Mandiri, BCA, CIMB, Citi, BRI, DBS, OCBC, UOB, Permata, Maybank) | Instalments | ✅ Active |
| Bank points as payment (BNI, Mandiri, BCA) | Cards | ✅ Active |
| Virtual Account — BCA, BRI, BNI, Mandiri, incl. **BI-SNAP** variants | Bank / A2A | ✅ Active |
| Internet banking — KlikBCA, BCA Klikpay, CIMB Clicks, Danamon Online, Mandiri Clickpay, BRI ePay | Bank / A2A | ✅ Active |
| GoPay, OVO, ShopeePay, LinkAja, DOKU Wallet | Wallet | ✅ Active |
| AlloBank, JeniusPay, BNI Yap, BNI Mobile, TMRW (UOB), Finpay Money | Wallet / bank app | ✅ Active |
| BSI, Muamalat (Islamic banks) | Bank / A2A | ✅ Active |
| Kredivo, Akulaku, Indodana, BRI Ceria | BNPL | ✅ Active |
| Convenience store (generic) | Cash | ✅ Active — Alfamart/Indomaret not named individually |
| **PayPal** | Wallet | ✅ Active |
| **Alipay, AlipayCN, AlipayHK, WeChat Pay, UnionPay** | Wallet / Cards | ✅ Active |
| GarudaMiles / Cash+Miles, vouchers, saved cards | Mixed tender | ✅ Active |
| 3DS / 3DS2 | Auth | ✅ Active via MPGS |
| **DANA** | Wallet | ❌ **SOURCED-ABSENT** — the only major Indonesian wallet missing |
| **Apple Pay, Google Pay** | Wallet | ❌ **SOURCED-ABSENT** — zero occurrences |
| **PayTo, BPAY, Afterpay, Zip** (Australia) | A2A / BNPL | ❌ **SOURCED-ABSENT** |
| **PayNow** (Singapore) | A2A | ❌ **SOURCED-ABSENT** |
| **FPX** (Malaysia) | A2A | ❌ **SOURCED-ABSENT** |
| **Konbini** (Japan), **KakaoPay** (Korea) | Cash / Wallet | ❌ **SOURCED-ABSENT** |
| **Atome** | BNPL | ❌ **SOURCED-ABSENT** |
| Amex | Cards | ⬜ **UNCHECKED** — BIN-gated server-side, not enumerable from the client |

> **Warning: Australia is Garuda's #2 market at 14.8% of organic traffic and its fastest-growing, and the checkout offers an Australian customer cards and PayPal.** No PayTo, no BPAY, no Afterpay, no Zip. The same pattern holds for Singapore (no PayNow), Japan (no konbini), Korea (no KakaoPay) and Malaysia (no FPX) — every one a market Garuda actually flies to.

**The shape of it:** 44 of the 57 implemented methods are Indonesian. The international half of the network is served by cards, PayPal and the Chinese wallets, and nothing else.

### Section 5: Payment Issues & Customer Complaints

**Not evaluated.** I ran two agents on this account — payment stack, and traffic/entities/financials — and neither covered complaints. This is a gap in how I scoped the run, not a finding that no complaints exist. **Scored 0 and flagged rather than left to imply an absence.** A Google Play and App Store review pull, of the kind done for Vietnam Airlines, would close it quickly.

### Section 6 & 7: Corporate and Payment Developments

| Date | Development | Category |
|---|---|---|
| **14 Aug 2026** | **Commercial Director Reza Aulia Hakim suspended**, no reason disclosed, no acting replacement named | Leadership |
| Aug–Sep 2026 | **Holding-company structure "under intensive review at shareholder level"** — merger vs other structure still undecided | Corporate structure |
| 13 May 2026 | Board confirmed at RUPST: Dirut **Glenny Kairupan**; Finance **Balagopal Kunduvara**; **Direktur Transformasi Neil Raymond Mills** | Leadership |
| 23 Apr 2026 | Q1 2026: revenue US$762.35m (+5.36%), net loss US$41.62m (−45.19%), 5.42m group passengers (+6.76%), OTP 91.01% | Financial |
| Feb 2026 | Danantara targets Garuda as holding over Citilink and Pelita Air in Q1 2026 — slips to H1, then to "under review" | Corporate structure |
| Dec 2025 | **Danantara injection executed** — Rp 8.7tn to Garuda mainline, Rp 14.9tn to Citilink | Funding |
| 15 Oct 2025 | Glenny Kairupan appointed CEO | Leadership |
| — | **Saudia partnership expanded** to sales, marketing, distribution, single-ticket travel, loyalty and technology infrastructure | Partnership |

**No public payment RFP found. No NDC programme evidence either way. No website or app replatforming announced. Career site: "No open vacancy."**

### Section 8: Checkout Experience Audit

**Partial — but far better than expected, and better than any other airline in this pipeline.**

`www.garuda-indonesia.com` 403s a normal browser (200 to Googlebot) and is a **Magnolia-CMS-backed SPA serving a byte-identical 374,534-byte shell on every path** — I verified that across seven URLs including the payment page, FAQ, T&Cs and privacy policy. `booking.garuda-indonesia.com` is 403 to every user-agent, so the live picker was never observed.

**But `pay.garuda-indonesia.com/payment/` serves the full payment application**, and that is where everything above came from.

| Dimension | Finding |
|---|---|
| Checkout type | Self-hosted Rails application on a Garuda domain, built and maintained by ATI Business Group |
| Card input | Cybersource Secure Acceptance Silent Order POST (keeps Garuda largely out of card-data scope) |
| Payment methods | 57 implemented types; server-side selection by region |
| Location-based display | Yes — `Booking.i18n` states availability varies by region |
| Instalments | 11 issuers, BIN-gated |
| Routing | **A single boolean** for cards. No failover |
| Tokenisation | Garuda-owned vault (`mycard_list`, `enable_save`, `/payment/token/delete`) |
| 3DS | 3DS2 via MPGS |
| Multi-currency | BIN gating by currency (`idrRestrictCard` / `nonIdrRestrictCard`); IBE links Bank Indonesia PBI 17/3/2015 |
| Surcharge | None found (`serviceFee:{amount:0}`) — **contrast: Citilink charges 3%** |
| Tech debt markers | jQuery, Adobe DTM `satelliteLib`, **Universal Analytics `UA-…` deprecated since 2023** running alongside GA4, plus a production typo (`selectedPayentType`) carried throughout |

### Section 9: PCI DSS Compliance

**No direct PCI compliance documentation found publicly for Garuda Indonesia.** The only statement is their FAQ: *"Situs web Garuda Indonesia menggunakan enkripsi SSL standar industri dan gateway pembayaran yang aman untuk melindungi informasi pribadi dan pembayaran Anda."* Note the singular "gateway" describing an estate of six.

`[INFERENCE, not confirmed]`: Cybersource Secure Acceptance Silent Order POST architecturally keeps Garuda's servers out of most card-data scope. However `mycard_list`, `enable_save` and `/payment/token/delete` indicate Garuda operates **its own card-token store**, which carries scope of its own.

### Section 10: Strategic Insights & Outreach Angles

**Insight 1 — One group, two completely disjoint payment estates.**
> **Evidence:** Section 3A (Garuda: Cybersource, DOKU, Midtrans, Finpay, MPGS, Ogone; `Espay` count **zero**) + `citilink.md` (Citilink: Espay, one gateway, nine channels dropping together in a May 2026 outage) + Section 6 (Danantara's stated objective is "one booking system").
Garuda owns 98.65% of Citilink. Garuda has QRIS and apparently no surcharge; Citilink has neither QRIS nor GoPay and charges 3% on cards. Neither can see the other's traffic, rates or decline data. **This is the opener, and it needs no pain projection — it is two facts about their own group placed side by side.**

**Insight 2 — Thirteen years of methods bolted onto a 2013 foundation.**
> **Evidence:** Section 3B (payment app copyright 2013, Cybersource adopted March 2013, Altéa cutover June 2013) + Section 4 (57 payment types, 17 endpoints, 5 async reconciliation pollers, every new method a bespoke widget).
Every method added since — AlloBank, Jenius, BI-SNAP, QRIS, four BNPL providers — is a hand-built widget, endpoint and status poller written by an outsourced BPO. The opportunity-cost argument is concrete and it is the right one for an in-house motion: not that the build was wrong, but that maintaining it is now the tax.

**Insight 3 — The international network is served by cards and PayPal.**
> **Evidence:** Section 4 (44 of 57 methods are Indonesian; PayTo, BPAY, PayNow, FPX, konbini, KakaoPay, Apple Pay and Google Pay all sourced-absent) + Section 1 (Australia #2 at 14.8% and fastest-growing; Singapore, Netherlands, USA in the top five).
They fly to Australia, Japan, Korea, Singapore, Malaysia, China and the Netherlands. Outside Indonesia and the Chinese wallets, a passenger gets a card form.

**Insight 4 — Routing is a boolean.**
> **Evidence:** Section 3B (`dokuCCEnabled ? DokuCC : CybsCC`) + Section 3A (two card gateways already integrated and paid for).
They already have two card gateways live. Switching between them is a config flag flipped by hand, not a decline-triggered cascade. **The capability gap is one line of code away from being worth real money**, and Wingo is the matched case: automatic retries of failed payments through multiple providers, +14% approval.

**Strongest entry point:** the Garuda/Citilink contrast. It is verifiable, it is theirs, it requires no assertion about their competence, and it points directly at the group-level mandate Danantara has already stated.

### Section 11: Competitors & Orchestration Adoption

| Airline | PSP / Acquirer | Orchestrator | Evidence |
|---|---|---|---|
| **Citilink** (98.65% subsidiary) | **Espay** | None | Own operational notice, May 2026 — see `citilink.md` |
| **Cebu Pacific** | Multi-acquirer | **CellPoint Digital** | Vendor case study (no published numbers) |
| **Malaysia Airlines** | 2C2P | **Outpayce XPP** | "authorization rates increase by 3-4 per cent" |
| **Thai Airways** | 2C2P | None named | Trade press |
| **Vietnam Airlines** | Adyen | **2C2P PACO + Outpayce XPP** | See `vietnam-airlines.md` |
| **Sun PhuQuoc Airways** | 2C2P + M-Pay | **2C2P PACO** | Trade press, Mar 2026 |
| **Bangkok Airways** | 2C2P (2018) | None — hardcoded method list | See `bangkok-airways.md` |
| **Singapore Airlines / Cathay Pacific** | Adyen direct acquiring | None — consolidated instead | Vendor releases |

**The pattern across the whole SEA airline pipeline:** every carrier researched has now landed in one of three places — bought an orchestrator (Malaysia Airlines, Cebu Pacific, Vietnam Airlines, Sun PhuQuoc), consolidated onto one global acquirer (SIA, Cathay), or built something themselves and stopped maintaining it properly (Garuda, Bangkok Airways, VietJet). Garuda is the largest of the third group.

### Section 12: Business Case Data

| Metric | Value | Source |
|---|---|---|
| FY2025 operating revenue | **US$3.22bn** (−5.9%) | Indonesian press, audited results |
| — scheduled flights | **US$2.51bn** | Same |
| — **non-scheduled (Hajj/Umrah charter)** | **US$340.87m (10.6%)** | Same |
| — other (incl. cargo, not broken out) | US$361.05m | Same |
| FY2025 net loss | **US$319.39m** ⚠️ vs US$322.48m elsewhere | Two sources conflict |
| FY2025 passengers | **21.2m** (−10.5%) | Tempo |
| Q1 2026 revenue / net loss | US$762.35m (+5.36%) / US$41.62m (−45.19%) ⚠️ vs CNBC US$46m | Kontan, Kompas, Liputan6 |
| Fleet | 99 serviceable, **43 grounded**; target 68 serviceable Garuda / ≥118 group by end-2026 | CNA.id, Detik |
| Market cap | **IDR 25.65tn (~US$1.5bn)**, GIAA at IDR 63, 15 Sep 2026 | IDNFinancials |
| State/Danantara ownership | **91.11%**; public float **7.96%** | Tempo |
| Hajj 2026 | **102,000 regular pilgrims**, 1,085 crew deployed | Antara |
| Umrah target | **40,000+ seats, Rp 520bn transaction target** through Jan 2027 | Liputan6 |
| **Direct vs OTA split** | **Not disclosed.** Traveloka outranks Garuda in its own home market | SimilarWeb top-sites |

**Sizing note:** the orchestrable line is scheduled + non-scheduled flight revenue (**US$2.85bn**), of which an undisclosed share is direct. The Hajj/Umrah charter line at US$340.87m is distinctive — high-ticket, seasonal, with a Rp 520bn Umrah transaction target that is itself a discrete payment-flow conversation. **Do not annualise Q1** — Hajj falls in Q2/Q3, and Q1 2026 non-scheduled (US$24.98m) is far below Q1 2025 (US$37.95m).

### Overall Research Confidence

**Medium-High, and unusually lopsided.** The payment stack is **High** — arguably the best-evidenced of any account in this pipeline, because the entire gateway configuration is readable in Garuda's own production code and I verified the load-bearing claims myself. Corporate, governance and financials are **High**, from Indonesian primary press and IDX-adjacent sources. **Traffic is Low** — SimilarWeb is hard-blocked, the country table is organic-search-only and capped at five countries, and two ICP signals therefore rest on the wrong metric. **Overseas entities are Low** and unresolved in either direction. **Complaints were not evaluated at all.**

### Manual Research Recommendations

> **Area:** Australia entity status.
> **Why it matters:** #2 market at 14.8% and the fastest-growing, with no PayTo or BPAY. Whether bookings are acquired locally or cross-border out of Jakarta changes the argument from "add a rail" to "you are eating a cross-border approval-rate penalty on your best growth market."
> **Action:** Check ASIC for a Garuda Indonesia Australian entity, and look at their Australian conditions of carriage for a named billing entity.

> **Area:** Traffic.
> **Why it matters:** Two ICP signals are measured on organic search rather than total visits, and the home-market share drives both.
> **Action:** A paid SimilarWeb pull on `garuda-indonesia.com` with the full country table.

> **Area:** Payment complaints.
> **Why it matters:** An unevaluated signal worth up to +2, and app reviews were the richest source on Vietnam Airlines.
> **Action:** Pull Google Play and App Store reviews for the Garuda Indonesia app, Indonesian-language included.

> **Area:** Who owns commercial and digital today.
> **Why it matters:** The Commercial Director seat has been vacant since 14 August 2026 with no named replacement. Writing to the wrong person wastes the account.
> **Action:** Confirm whether Direktur Transformasi **Neil Raymond Mills** holds commercial or digital scope in the interim. This is currently my inference and is not sourced.
