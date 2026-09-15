# Bangkok Airways

**Status:** 🟢 Ready to outreach — sequence drafted
**ICP Score:** 14 / 24 → ⭐ High Priority
**Industry:** Airlines (regional full-service, plus airport ownership) · **HQ:** Bangkok, Thailand · **Researched:** 2026-09-15 · **First email sent:** —
**Motion:** **Greenfield** — no orchestration layer detected, and the method list is hardcoded into the front end

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Bangkok Airways PCL (SET: **BA**, IATA: **PG**), "Asia's Boutique Airline" — a Thai regional full-service carrier that also owns and operates Samui, Sukhothai and Trat airports. FY2025 revenue **THB 26,067.2m (~US$800m)**, net profit THB 3,580.3m, **4.23m scheduled passengers**, fleet down to **22 aircraft**. Skytrax World's Best Regional Airline for the ninth consecutive year. The defining fact for us: **roughly half to three-quarters of its web traffic originates outside Thailand, it has no legal entity anywhere outside Thailand, and its local payment rails are switched off for any itinerary not departing Thailand.**

**Traffic: SimilarWeb, supplied by Prateek 2026-09-15** — `bangkokair.com`, subdomains included, worldwide, Jun–Aug 2026. Full 69-country breakdown in [`accounts/traffic/bangkok-airways.md`](../accounts/traffic/bangkok-airways.md). **Thailand 45.40%, so 54.60% of traffic originates outside the home market, across 19 countries above 1%.**
⚠️ **Absolute visit volume is still unverified.** The supplied export gives shares, not totals. The earlier ~612K / ~623K figures remain estimates and must not be multiplied by these shares.

### Top 5 markets
Verified shares from the supplied SimilarWeb export. Methods and absences are from Bangkok Airways' own enumerated payment page.

| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇹🇭 Thailand | **45.40%** (+10.9%) | Cards (Visa, Master, JCB, Diners, Discover), Union Pay, Ali Pay, WeChat Pay, Line Pay, ShopeePay, TrueMoney, card instalments (min THB 3,000, six banks), direct debit, ATM/iBanking/bank counter, counter cash (Lotus, Big C, PayPost, TrueMoney) | **Amex.** **7-Eleven / Counter Service** — Thailand's largest counter network. **PromptPay is contested** (absent from the published page, `PG_PROMPTPAY` in the live config — see Section 4) | ✅ HQ + 11 Thai offices |
| 2 | 🇸🇬 Singapore | **5.15%** (+122.1%) | Cards, Union Pay, wallets only | **No PayNow.** Singapore's dominant A2A rail, sourced-absent from the enumerated page. Also no GrabPay | ⚠️ Own office listed, but a third-party GSA is named there too — unresolved |
| 3 | 🇺🇸 USA | **5.04%** (−12.8%) | Cards, Union Pay, wallets only | **No Apple Pay, no Google Pay, no PayPal** | ❌ GSA only |
| 4 | 🇮🇱 Israel | **4.08%** (+141.2%) | Cards, Union Pay, wallets only | **Everything local.** Instalments, direct debit, ATM and counter are all restricted to flights departing Thailand | ❌ GSA only |
| 5 | 🇬🇧 UK | **3.64%** (+36.1%) | Cards, Union Pay, wallets only | No local rails | ❌ GSA only |

*Then Australia 3.40%, Germany 3.25%, India 2.42%, Kazakhstan 2.42%, UAE 1.76%. Nineteen countries sit at or above 1%.*

**Israel is the standout on engagement**: 11m14s average visit, 7.26 pages/visit, 33.4% bounce, +141% growth. The most engaged large market in the table by a distance.

### Legal entities
- **Bangkok Airways Public Company Limited** — Registration No. **0107556000183**, registered capital THB 2,100,000,000. HQ: 99 Mu 14, Vibhavadirangsit Rd., Chom Phon, Chatuchak, Bangkok 10900.
- **All 16 consolidated subsidiaries and all 4 associates are Thai-registered** (catering, ground handling, cargo, airport management, training, REIT management). Associates include **U-Tapao International Aviation (40%)** and the SET-listed **BA Airport Leasehold REIT**.
- **No legal entity anywhere outside Thailand.** Their own 56-1 One Report describes non-Thai presence purely as selling agents: *"We operated selling agents located in Canada, Australia, Europe, Thailand, Singapore, Hong Kong, Cambodia, Laos and Myanmar."*
- Own offices in 15 locations: 11 in Thailand, plus Luang Prabang (Laos), Phnom Penh and Siem Reap (Cambodia), and Singapore. **GSAs in 36 further markets** including Israel, USA, Germany, Australia and the UK.
- Major shareholders: the **Prasarttong-osoth family controls ~58% directly**; **Bangkok Bank PCL holds exactly 5.00%**.

### Known PSPs
- **2C2P** — `[Press Release]`, named by their own President in 2018 for the alternative-method set. **Eight years old and never renewed publicly.** See the caveat in Section 3A.
- **Amadeus Altéa PSS + Amadeus Digital / e-Retail front end** — confirmed by hard technical evidence in the live JS bundle and named in their own 56-1 supplier table as *"Reservation and Ticketing services"*.
- **Sabre AirVision Revenue Manager** — revenue management only, not payments, in use since 2008.
- **BIRTS** ("Bangkok Airways Internet Reservation and Ticketing System", versions 1 and 4) — their own registered software copyright. They own the booking front end, which is the integration surface.
- **No card acquirer identified.** Their 56-1 says only *"all revenues from Internet sales are received directly by our acquiring bank"* — unnamed.
- ❌ **"OnePAY Payment Gateway" is NOT evidenced.** It surfaced in a search snippet; I fetched `/booking-conditions` myself and the string does not appear. Discarded.

### Orchestration status
**None detected — direct PSP integration only.** Two independent lines of evidence:

1. **Zero hits** for CellPoint, Juspay, Spreedly, Primer, Gr4vy, APEXX, Payrails, Outpayce, Yuno, IXOPAY, Corefy, 2C2P or Adyen across the production JS chunks (my own scan: 32 chunks reachable from the homepage; a parallel scan across the full 138-chunk build manifest also returned zero).
2. **The accepted-method list is a hardcoded string compiled into the front end.** Verified first-hand in `static/chunks/`:

```js
""!==T && L.push({key:"binNumber", value:T}),
L.push({key:"paymentMethodsToDisplay",
        value:"PG_CC, PG_EXT, PG_EWALLET, PG_PROMPTPAY, PG_IP, PG_MOBILEBANK"})
```

A fixed six-value string, shipped to every browser, passed into the Amadeus booking engine as a portal fact. **To change what a customer can pay with, they ship a front-end release.** There is no routing logic, no acquirer failover and no dynamic method eligibility anywhere in the bundle.

### Buying signals
- 🤝 **2C2P partnership** — [their own IR newsroom, 4 June 2018](https://investor.bangkokair.com/en/newsroom/corporate-news/125606/bangkok-airways-introduces-new-online-payment-channels), President Puttipong Prasarttong-Osoth quoted. The last public payment-infrastructure decision they announced was **eight years ago**.
- 📉 **Contracting, not expanding.** Fleet 25 → 22, Bangkok–Lampang and Lampang–Mae Hong Son discontinued, Bangkok–Phuket / Samui–Singapore / Bangkok–Maldives capacity cut, jet-to-turboprop downgauging. **1H2026 international passengers −38.4%.** This is a cost-pressure story, not a growth story — which changes the pitch.
- 💰 **Aug 2025: firm ATR order for 10–12 ATR 72-600**, deliveries Q4 2026 → 2028. Reinvesting in regional capacity.
- 📋 **IATA Airline Retailing Maturity status, 30 May 2023** — title and date confirmed; body JS-rendered and unread. An Altéa NDC contract is `[UNVERIFIED — search summary only]`.
- 💼 **No payment or e-commerce job postings found.** Their SuccessFactors portal is fully JS-rendered and returned nothing.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

### Pain Vector Extraction

```
Motion: GREENFIELD. No orchestration layer detected — zero vendor strings across the
production JS bundle, and the accepted-method list is a hardcoded six-value string compiled
into the front end. Phase 1 may therefore note the absence of a routing layer, though the
sequence leads with the concrete facts rather than the abstraction.

Observable setup facts (verified first-hand unless marked):
- The accepted-method list is a fixed string shipped to every browser, verbatim from
  static/chunks/: paymentMethodsToDisplay = "PG_CC, PG_EXT, PG_EWALLET, PG_PROMPTPAY,
  PG_IP, PG_MOBILEBANK". Changing what a customer can pay with means shipping a release.
- BIN already flows through the checkout, sourced from u.cc_bin inside a CAMPAIGN parameter
  block (campaign_name, promo_rbd, promo_code_id). It decides promotional eligibility,
  not routing.
- 15 country sites share one method set — from the disableFxBox config in the same bundle
- Thailand 45.40%; 54.60% of traffic originates outside Thailand; 19 countries at or
  above 1% — source: SimilarWeb geography export supplied by Prateek 2026-09-15
- Singapore is the #2 market at 5.15%, growing +122.1%. PayNow and GrabPay are both
  sourced-absent from their enumerated payment page
- Instalments, direct debit, ATM and counter payment all carry the restriction, verbatim:
  "This payment type will be available for all domestic and international flights departing
  from Thailand only"
- Their FAQ's documented remedy for a declined card is a phone call to 1771, toll-free
  from Thailand only, or +662 270 6699, open 8am to 8pm Bangkok time
- Third-party cards are banned: "The card holder must be one of the traveling party"
- Refunds take 30 business days, to the original card only
- One PSP ever named publicly: 2C2P, from a 2018 press release. No acquirer identified
- Amadeus Altea PSS with their own front end (BIRTS, their registered copyright)
- Contracting: fleet 25 -> 22, two routes closed, 1H2026 international passengers -38.4%

Selected observations for Phase 1 (E1 bullets, ranked by materiality):
1. One method set across 15 country sites -> "Your checkout ships one method list across
   all 15 country sites."
2. Singapore #2 and PayNow absent -> "Singapore is your second-biggest market, up 122%
   last quarter, and PayNow isn't on the list."
3. The hardcoded string -> "The list itself is a fixed six-value string compiled into the
   front end."
Escalating: footprint, then the specific gap, then why it persists. Bullet 3 sets up E2
and E3 without asserting any pain.

Bridge variant: B — limitations
Rationale: exactly ONE PSP has ever been named publicly (2C2P, 2018) and no acquirer is
identified, against 15 country sites and 19 countries above 1% of traffic. That is a single
visible processor spanning many markets, which is B. A is wrong — there is no evidence of
two parallel stacks to be complex about.

Hypothesis for Phase 2 (E3):
The method list was set for Thailand and has not moved as the traffic went international.
Backing logic: 54.60% of traffic is now non-Thai across 19 countries, Singapore is second
and growing fastest, and the local half of the method set is restricted by their own
documentation to itineraries departing Thailand — and is Thai-rail-specific anyway, so it
is unusable to a Singaporean or Israeli buyer regardless. Meanwhile the list is a compiled
string, so adding a rail is a release rather than a configuration change.

Success case for Phase 3 (E4):
Selected case: Wingo
Tier: 1 — airline, and the only airline case in the library carrying numbers
Match rationale: both halves map. "1,000+ payment methods through one integration" answers
the coverage hypothesis directly, and "automatic retries of failed payments through multiple
providers" answers the FAQ observation that a declined card becomes a phone call.
Numbers to lead with: +14% approval rate (initial implementation phase) · 1,000+ payment
methods via one integration · fraud tooling and integrated 3D Secure
Region stated explicitly as Latin America. No APAC implication.
Optional benchmark: SKIP. The "~8% average authorisation uplift" traces to Yuno's own blog.
The IATA/EDC airline cost-of-acceptance figure has only been seen via a vendor blog citing
it, so it is not quotable until traced to the primary source.

Touch-by-touch angles:
- E2 angle: missing local rail -> one integration to add any method, no per-rail rebuild
- LK1 angle: Singapore at #2 with no PayNow
- LK2 angle: the list was set for Thailand and the traffic went international
- LK3 angle: Wingo gave a declined card a second path instead of a dead end
- LK4 angle: the FAQ phone number (held back, unused until here)
- E8 angle: clean exit, no new observation
```

---

### Phase 1 — Curiosity (Days 1–5)

#### Touch 1 — Email 1 · Day 1 · Tue 15 Sep

**Subject:** One method list, 15 markets

```text
Hey {{recipient.first_name}},

Spent some time looking at Bangkok Airways' payment setup. Three things stood out.

Your checkout ships one method list across all 15 country sites.

Singapore is your second-biggest market, up 122% last quarter, and PayNow isn't on that
list.

The list itself is a fixed six-value string compiled into the front end.

At your stage, that kind of setup usually comes with some limitations.

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

We sit above the providers you already run. Nothing gets replaced.

One integration covers the methods, so adding PayNow in Singapore, or anything else in any
market, becomes configuration rather than a front-end release with a provider contract
behind it.

Routing then decides per BIN, market and method which rail a transaction takes, and moves
traffic automatically when one degrades.

Worth noting you already pass BIN through the checkout. It's used to decide promotional
eligibility rather than which rail a payment takes, so the plumbing is largely there.

I'll keep sharing what I'm seeing every few days. If your stack's where you want it, say the
word and I'll back off. Otherwise happy to go deeper.

Cheers,
Prateek
```

#### Touch 3 — LinkedIn message 1 · Day 5 · Sat 19 Sep

> ⚠️ **Lands on a Saturday.** Shift to Mon 21 Sep, or pull forward to Fri 18 Sep.

```text
Hey {{recipient.first_name}}, figured I'd flag this here too in case it's more useful than
email. Quick one: Singapore is your second-largest market and grew 122% last quarter, and
PayNow isn't on your payment page. Curious whether that's deliberate or just hasn't come up.
```

---

### Phase 2 — Diagnosis (Days 7–9)

#### Touch 4 — Email 3 · Day 7 · Mon 21 Sep · NEW EMAIL

**Subject:** Read on your non-Thai markets

```text
Hey {{recipient.first_name}},

Going to take a swing at this. My read is that the method list was set for Thailand and
hasn't moved as the traffic went international.

54.6% of your traffic now comes from outside Thailand, across 19 countries above 1%, and
Singapore is second.

Your payment page limits instalments, direct debit, ATM and counter payment to flights
departing Thailand, and they're Thai bank rails regardless. Not because anyone's doing it
badly, but a Singaporean buyer was never going to use them.

At Yuno (a16z-backed, top-100 fintech) we sit above your existing providers, so a market
gets its own rails without a new integration. Keep your stack, add what's missing.

Thursday the 24th is open. Would 10am or 3pm your time work for 15 minutes? If payments sits
elsewhere, happy to be pointed there.

All the best,
Prateek
```

#### Touch 5 — LinkedIn message 2 · Day 9 · Wed 23 Sep

```text
Hey {{recipient.first_name}}, sent a longer note over email this week. Short version: the
method list looks like it was set for Thailand, and 54.6% of your traffic is now outside it.
If that's anywhere on your radar, would Monday the 28th or Tuesday the 29th at 4pm your time
work for a quick 15?
```

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · Fri 25 Sep · NEW EMAIL

**Subject:** How Wingo solved this

```text
Hey {{recipient.first_name}},

On the read I shared last week, here's what solved looks like.

Wingo is a low-cost carrier flying 37 routes across Latin America. Same shape of problem:
international traffic, a method set that hadn't kept up. From the initial phase with Yuno:

- Approval rate up 14% (not too bad, right?)
- Over 1,000 payment methods through one integration
- Fraud tooling and 3D Secure in the same layer

Smart Routing also retries a failed payment through a different provider automatically, so a
decline gets a second path rather than ending the booking.

Qatar Airways, Copa and Avianca run on the same layer, above the stacks they already had.
No rip-out.

How long does it take today to get a new method into the checkout?

Wednesday the 30th, would 11am your time work for 15 minutes?

Full case here if useful:
https://y.uno/en/newsroom/wingo-improves-payment-efficiency-with-yuno-as-strategic-partner

Best,
Prateek
```

#### Touch 7 — Email 5 · Day 13 · Sun 27 Sep · MANUAL

> ⚠️ **Lands on a Sunday.** Shift to Mon 28 Sep.

*Placeholder — manual creative approach. Do not auto-write.*

Suggested angle for this account: a screenshot of the payment page next to the SimilarWeb
country table. One method set, nineteen countries above 1%. The two images argue it without
a word of commentary.

#### Touch 8 — Email 6 · Day 15 · Tue 29 Sep · MANUAL

*Placeholder — second manual approach, different format than E5.*

Suggested angle: a short Loom booking a Bangkok–Samui flight as a Singaporean buyer,
stopping at the payment step to show what's actually offered.

#### Touch 9 — LinkedIn message 3 · Day 17 · Thu 1 Oct

```text
Hey {{recipient.first_name}}, Wingo's change was that a declined card started falling through
to a second provider automatically instead of ending the booking. Worth 15 minutes to see
whether it maps to your setup? Tuesday the 6th at 2pm your time is open.
```

---

### Touch 10 — Email 7 · Day 19 · Sat 3 Oct · MANUAL

> ⚠️ **Lands on a Saturday.** Shift to Fri 2 Oct or Mon 5 Oct, though Mon 5 collides with LK4.

*Placeholder — manual creative bridge. Anchor to something fresh.*

Suggested anchors: the **Israel market** — 4.08% of traffic, up 141%, with an 11m14s average
visit and 7.26 pages per visit, the most engaged large market in their table by a distance.
Nobody has touched it in the sequence and it is a genuinely interesting thing to have noticed.
Alternatively the **Kuwait spike** (+3,834% to 1.22%, 10m19s average visit).

⚠️ **Do not anchor to growth or expansion.** They are contracting: fleet 25 to 22, two routes
closed, 1H2026 international passengers down 38.4%. An expansion framing would read as
not having done the reading.

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21 · Mon 5 Oct

```text
Hey {{recipient.first_name}}, last LinkedIn ping from me on this. One thing I never raised:
your FAQ says a failed card payment is fixed by calling 1771, toll-free inside Thailand
only, 8am to 8pm. Most of your buyers aren't in Thailand. Thursday the 8th at 9:30am your
time is open.
```

#### Touch 12 — Email 8 · Day 23 · Wed 7 Oct · REPLY IN THREAD to Touch 4 or 6

```text
Hey {{recipient.first_name}},

Going to stop pinging unless you want to pick this back up.

If the timing's just off, happy to circle back next quarter once the current schedule
changes have settled.

If it ever comes back up, just reply here.

Cheers,
Prateek
```

---

### Source Notes

- ✅ **The hardcoded method list** — extracted from the production JS chunks and verified by
  me: `paymentMethodsToDisplay` = `"PG_CC, PG_EXT, PG_EWALLET, PG_PROMPTPAY, PG_IP,
  PG_MOBILEBANK"`. E1 calls it "a fixed six-value string compiled into the front end", which
  is exactly what it is.
- ✅ **BIN already flows through the checkout** — `u.cc_bin` inside a campaign-parameter block
  (`campaign_name`, `promo_rbd`, `promo_code_id`). Verified by me. E2 says it decides
  promotional eligibility rather than routing, which is precisely the finding.
- ✅ **15 country sites** — from the `disableFxBox` config in the same bundle.
- ✅ **Traffic figures** — SimilarWeb geography export **supplied by Prateek 2026-09-15**,
  `bangkokair.com` with subdomains, worldwide, Jun–Aug 2026. Thailand 45.40%, so 54.60%
  non-Thai; Singapore #2 at 5.15%, +122.1%; 19 countries at or above 1%. Full table in
  `accounts/traffic/bangkok-airways.md`.
- ✅ **PayNow and GrabPay sourced-absent** — zero occurrences on their enumerated
  `/payment-channel` page, which I fetched and grepped myself.
- ✅ **The "departing from Thailand only" restriction** — verbatim from that same page.
- ✅ **The FAQ phone number** — 1771 toll-free within Thailand only, or +662 270 6699,
  8am–8pm Bangkok time, given as the documented remedy for a failed card payment.
- ✅ **Wingo: +14% approval, 1,000+ methods, fraud tooling and 3DS** — re-verified at source
  2026-09-15. Region named as Latin America in the copy, so nothing implies an APAC result.
- ✅ **Qatar Airways, Copa, Avianca** — on Yuno's site-wide customer list, named with **no
  metric attached**, per the library rule.
- ⚠️ **PromptPay is deliberately absent from every touch.** It is the one contested method on
  this account: absent from the published payment page but present as `PG_PROMPTPAY` in the
  live config. Raising it risks being wrong in either direction, and Singapore/PayNow makes
  the same argument on unambiguous evidence. **Do not add it without checking the live
  checkout first.**
- ⚠️ **2C2P is never named in the sequence.** It is an eight-year-old datapoint and does not
  establish who acquires their card volume today.
- ⚠️ **No named contact.** `{{recipient.first_name}}` throughout. Research surfaced no
  payments owner, and their careers portal was unreadable, so the recipient needs picking
  manually. Note the Prasarttong-osoth family controls ~58% of the company, so this is a
  closely-held business where the commercial owner may be a family principal.
- ⚠️ **E3 runs ~139 words against a ~90–120 budget.** Everything left in it is
  rulebook-mandated: hypothesis, two lines of backing, Yuno re-state, CTA. The cuttable line
  is "not because anyone's doing it badly", at the cost of the observation reading harder.
  Every other touch is inside budget.
- ⚠️ **Three touches land on weekends** (LK1 Sat 19 Sep, E5 Sun 27 Sep, E7 Sat 3 Oct).
  Flagged inline.
- ⚠️ **Thai public holidays were not verified for the CTA window** (24 Sep – 8 Oct). Research
  did not surface any and I did not check a calendar. Worth thirty seconds before loading
  into Gong.

### Notes on what this sequence deliberately avoids

**Any growth or expansion framing.** Bangkok Airways is contracting: fleet down from 25 to
22, Bangkok–Lampang and Lampang–Mae Hong Son discontinued, Bangkok–Phuket, Samui–Singapore
and Bangkok–Maldives cut back, and **1H2026 international passengers down 38.4%**. The whole
sequence is framed as recovering revenue on traffic they already have, which is the only
frame that survives contact with their own numbers.

**Any claim about their acquirer.** One PSP has ever been named publicly and it was in 2018.
The sequence argues method coverage, which is observable, rather than acquiring economics,
which is not.

### Success Case Alternatives

- **Livelo** — swap if the conversation narrows to declines rather than coverage: +5%
  approval, 50% of failed transactions recovered by instant routing to a secondary acquirer.
  Not an airline, but the tightest mechanism fit to the FAQ observation.
- **Qatar Airways / Copa / Avianca** — airline credibility if Wingo's LATAM footprint draws
  an objection. Nameable only, no published metrics.
- **inDrive** — Tier 2 if the conversation turns to multi-country coverage as a whole:
  roughly 90% approval, 10 new countries in under 8 months, LATAM.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 14 / 24
| Signal | Points | Status |
|--------|--------|--------|
| Orchestration status | **+4** | ✅ **None detected.** Zero orchestrator strings across the production bundle, plus a hardcoded `paymentMethodsToDisplay` list. Greenfield |
| 3+ countries | **+3** | ✅ **Nineteen countries at or above 1%** in the supplied SimilarWeb export. 36 GSA markets, 15 country sites in the front-end config |
| Multiple PSPs | **0** | ⬜ **Only one ever named (2C2P, 2018), and no acquirer identified.** A second provider almost certainly exists — their 56-1 references an unnamed "acquiring bank" separately from the 2C2P wallet set — but that is inference. **Scored 0 rather than stretched** |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Singapore is the #2 market at 5.15% and PayNow is sourced-absent** from their enumerated payment page. Reinforced by the restriction that instalments, direct debit, ATM and counter payment apply, verbatim, to *"all domestic and international flights departing from Thailand only"* — so every non-Thailand-departing itinerary gets cards and wallets only. ⚠️ **Basis changed:** this previously rested on Australia having no PayTo/BPAY, which the supplied data invalidates (Australia is #6, not top-3) |
| Recent expansion | **0** | ❌ The opposite. Fleet 25→22, two routes closed, three cut back, 1H2026 international passengers −38.4% |
| Payment issues reported | **0** | ⬜ **Honestly scored.** Forum complaints are scattered and mostly historical, and TripAdvisor threads could not be opened (403). Their own FAQ is more damning than the forums, but that is a documentation finding, not a complaint-frequency one. A proper app-review pull would likely move this |
| Funding >$10M | **0** | ❌ No round. The THB 2,000m into U-Tapao is an outbound investment, not capital received |
| High traffic outside home | **+2** | ✅ **Thailand is 45.40%** in the supplied export. Comfortably under 60%, now on verified data rather than two conflicting scrapes |
| Competitor using orchestration | **+2** | ✅ Cebu Pacific (CellPoint Digital), Thai Airways (2C2P), Malaysia Airlines (Outpayce XPP), Sun PhuQuoc Airways (2C2P PACO) |
| Payment job postings | **0** | ❌ Not found; careers portal unreadable |

**Tier:** High Priority (14+) ⭐ / Medium (8–13) 🟢 / Low (<8) 🔴 → **⭐ High Priority (14)**

No analyst override. The score lands on the tier boundary and the reasoning is clean: it scores on genuine structural signals (greenfield, international traffic, a real rail gap) and correctly scores zero on the three signals where the evidence is absent or points the other way. **The total is unchanged at 14 after the traffic rework, but two of the signals are now on verified data rather than conflicting scrapes, and one had its basis replaced.** **One caveat worth carrying into any conversation: this is a contracting airline.** Fleet down, routes closed, international traffic down 38.4% in 1H2026. That makes cost-of-acceptance and approval-rate recovery the right frame, and market-expansion framing the wrong one.

### Source Notes
- ✅ **The hardcoded `paymentMethodsToDisplay` string** — I extracted the production JS chunks and grepped them myself. The exact value is quoted above. This is the single most important finding in the file.
- ✅ **`binNumber` handling, and what it is actually for.** The BIN comes from `u.cc_bin` inside a *campaign parameter* block (`campaign_name`, `promo_rbd`, `promo_code_id`, `account_code_id`). So **BIN data already flows through their checkout — it decides promotional eligibility, not routing.** Verified first-hand. This is a sharper observation than "they don't use BIN data".
- ✅ **Amadeus endpoints** — `nodeA3.production.webservices.amadeus.com/1ASIWWEBPG` (the trailing `PG` is their IATA code), `uat.digital.airline.amadeus.com/pg/booking`, and `wav-digital-5.saas.amadeus.com/plnext/BangkokAir/Override.action`. All three pulled from the live bundle by me.
- ✅ **Payment-method page** — fetched `/payment-channel` directly (37.8KB). Confirmed present: Visa, Master, JCB, Diners, **Discover** (genuinely a scheme here, not the English verb), **Union Pay** (spelled with a space), Ali Pay, WeChat Pay, Line Pay, ShopeePay, TrueMoney, Lotus / Big C / PayPost counters, instalments.
- ✅ **Sourced absences from that enumerated page:** **Amex = 0**, **7-Eleven = 0**, **Counter Service = 0**, **Apple Pay = 0**, **Google Pay = 0**, **PayPal = 0**, **PromptPay = 0**.
- ✅ **15 country sites** — from the front-end config: the visible list ends `"MM","LA","MV","SG","HK","MY","CN","VN","ID","JP","AU","AE"`, gating a `disableFxBox` flag. Fifteen selling markets sharing one Thailand-centric method set.
- ✅ **FY2025 financials, revenue split and the direct-channel share** — all from their own filed documents: the [FY2025 MD&A](https://hub.optiwise.io/storage/168/mdna/2025/ba-mdna-fy2025-en.pdf), [Q2-2026 MD&A](https://hub.optiwise.io/storage/168/mdna/2026/ba-mdna-2q2026-en.pdf) and the 316-page [56-1 One Report 2025](https://hub.optiwise.io/storage/168/annual-report/2025/ba-ar2025-en.pdf).
- ⚠️ **2C2P is an eight-year-old datapoint.** It establishes who supplied the wallet set in 2018. It does **not** establish who acquires their card volume today, and no source does. Do not state 2C2P as their current processor.
- ⚠️ **PromptPay is genuinely contested and I am not resolving it.** Absent from the published `/payment-channel` page in every locale, but `PG_PROMPTPAY` is in the live `paymentMethodsToDisplay` string shipped to every booking session. The most likely reading is that it *is* live and the published page has not kept up. **A supporting argument that the page is "five years stale" because it says Tesco Lotus does not hold** — the visible text says "Lotus"; only the image asset is still named `01_tescolotus_new.png`, and I cannot read the logo itself. Treat PromptPay as "probably live, undocumented", and verify at checkout before it appears in an email.
- ✅ **Traffic is now supplied data, not a scrape.** SimilarWeb, provided by Prateek 2026-09-15, `bangkokair.com` with subdomains, worldwide, Jun–Aug 2026, all 69 countries. Thailand 45.40%, Singapore 5.15%, USA 5.04%, Israel 4.08%, UK 3.64%. **This replaced two conflicting scrapes that were both wrong** — see Section 1 and `accounts/traffic/bangkok-airways.md`.
- ⚠️ **Absolute visit volume is still unverified.** The supplied export is a geography report: shares, engagement and country ranks, no totals. The ~612K / ~623K figures are estimates. Do not multiply them by the verified shares.
- ⚠️ **The direct-channel share is by PASSENGER COUNT, not value.** 49.3% (FY2025) and 47.0% (1H2026) of passengers came via website and direct connect. Direct-channel passengers likely skew to lower-fare domestic sectors, so the direct share of *revenue* may be lower.
- ❌ **Section 8 is partial.** `digital.bangkokair.com` and `flightbook.bangkokair.com` sit behind **Imperva** bot protection and were unreachable, so the actual card-entry page was never observed. Single-acquirer is a strong inference from the hardcoded method list, not something directly seen.
- ❌ **No PCI DSS disclosure anywhere** — not on the site, not in the 56-1, not in the MD&As.
- ❌ **"OnePAY Payment Gateway" — discarded.** Search-snippet only; my own fetch of `/booking-conditions` returned zero occurrences of OnePAY, Amex, JCB, MasterCard, 3-D Secure or SecureCode.

### Handling note
Their public JS bundle exposes a hardcoded API key for a payment-adjacent endpoint. **I have deliberately not recorded its value anywhere in this repo, and it must never appear in outreach.** Leading with "I found your API key" is not an opening, and it is not territory we should be in. Recorded only so nobody rediscovers it and thinks it is a usable hook. If Prateek ever wants it raised, it is a responsible-disclosure conversation through their security contact, not a sales one.

### False positives killed
- **`omise` returned ~150 hits across the JS bundle** — every one the substring inside `Promise` / `compromise`. Omise/Opn is **not** present.
- **`Stripe` returned 2 hits** — both the CSS class `RouteMap_routeStripe`.
- **`xpP`** matched a JS internals table, not Outpayce XPP.
- **"Rabbit LINE Pay" on the homepage is promotional**, not a method declaration: the string is *"Please direct access to promotion page via Rabbit LINE Pay Official Account or Rabbit LINE Pay promotional page only"*. **My own first pass over-corrected and killed LINE Pay entirely — that was wrong.** "Line Pay" is separately and genuinely listed on the payment-channel page as an accepted e-wallet. Both things are true: the homepage strings are campaign copy, and the method is real.
- **"QR" ×4 on the homepage is Qatar Airways' IATA code** in a codeshare dropdown, not a QR rail.
- **My own `UnionPay` grep returned 0 and was wrong** — the page spells it **"Union Pay"** with a space. It is accepted.
- **KTC (Krungthai Card)** runs co-branded Bangkok Airways cards. That is loyalty co-branding, **not acquiring**.
- **Impostor domains.** `bangkok-airway.com`, `bangkok-airline.com`, `bangkokairlines.org` and `bangkok-airlines.com` all serve convincing "Payment Guide" and "Refund Request" pages. **None are Bangkok Airways.** The only real domain is `bangkokair.com`. Excluded from this report, and worth knowing as a live brand-fraud problem for them.
- **`bangkokairways.com` is a parked ad page**, not airline-operated. `bangkokair.co.th` 301s to the real domain.

### Success Case Alternatives
- **Wingo** — Tier 1 and the only quantified airline case: +14% approval rate in the initial phase via automatic retries across multiple providers, 1,000+ methods, 3DS. Maps directly to a single-path checkout with no in-session recovery.
- **Qatar Airways / Copa / Avianca** — airline credibility, nameable, **no metrics exist**. Never attach a number.
- **Livelo** — if the conversation turns to decline recovery specifically: +5% approval, 50% of failed transactions recovered via instant routing to a secondary acquirer.

---

## Executive Summary

Bangkok Airways is a Thai regional full-service carrier with **no orchestration layer, one publicly-named PSP from 2018, no card acquirer identified, and a payment-method list hardcoded as a six-value string compiled into its front end**. Between half and three-quarters of its web traffic comes from outside Thailand — Israel, the USA, Germany, Australia and the UK — yet it has **no legal entity outside Thailand**, and its instalment, direct-debit, ATM and counter rails are restricted by its own documentation to itineraries departing Thailand. Foreign buyers, Thai-only acquiring, Thai-only local methods. The motion is **greenfield**, and the opening is cross-border approval rate on inbound bookings, not market expansion — they are contracting.

### Section 1: Website Traffic Analysis by Country

**Data source: SimilarWeb, supplied by Prateek on 2026-09-15** — the primary source under the skill's resolution order. Parameters from the file's own Report Details sheet: domain `bangkokair.com`, **subdomains included**, Worldwide, **Jun–Aug 2026**, device Total. Full 69-country table in [`accounts/traffic/bangkok-airways.md`](../accounts/traffic/bangkok-airways.md).

| # | Country | Share | Change | Avg visit | Pages/visit | Bounce |
|---|---------|-------|--------|-----------|-------------|--------|
| 1 | **Thailand** | **45.40%** | +10.9% | 02:14 | 5.18 | 28.8% |
| 2 | **Singapore** | **5.15%** | **+122.1%** | 01:50 | 3.18 | 57.2% |
| 3 | **United States** | **5.04%** | −12.8% | 04:15 | 4.89 | 45.7% |
| 4 | **Israel** | **4.08%** | **+141.2%** | **11:14** | **7.26** | 33.4% |
| 5 | United Kingdom | 3.64% | +36.1% | 04:06 | 4.00 | 29.8% |
| 6 | Australia | 3.40% | +43.0% | 02:42 | 5.53 | 38.0% |
| 7 | Germany | 3.25% | +5.8% | 06:24 | 7.30 | 34.9% |
| 8 | India | 2.42% | +60.1% | 01:30 | 3.65 | 24.4% |
| 9 | Kazakhstan | 2.42% | **−95.8%** | 07:16 | 1.97 | 60.9% |
| 10 | UAE | 1.76% | −42.1% | 06:23 | 8.26 | 18.9% |

Then France 1.69%, Japan 1.62%, Canada 1.60%, Russia 1.39%, Kuwait 1.22%, Italy 1.17%, Switzerland 1.06%, Netherlands 1.05%, Spain 1.05%. **Nineteen countries at or above 1%; 69 in total.**

**Thailand is 45.40%, so 54.60% of traffic originates outside the home market.** For a carrier whose network is 88.7% domestic Thai passengers, that remains the central tension of the account, and it is now measured rather than inferred.

**Movements worth raising:**
- **Kuwait +3,834%** to 1.22%, with a 10m19s average visit and a 14.5% bounce rate — the lowest in the table. Either a real new demand pocket or a campaign.
- **Kazakhstan −95.8%** and **Russia −80.9%**, both with poor engagement (1.97 and 4.26 pages/visit, 60.9% and 75.1% bounce). Traffic that was probably never converting.
- **Singapore +122.1%** and **Israel +141.2%** are the two fastest-growing markets of real size.

⚠️ **This export gives shares, not totals.** Absolute visit volume remains unverified — the earlier ~612K and ~623K figures are estimates and should not be multiplied by these shares to manufacture a number that looks solid.

⚠️ **What the supplied data overturned.** The report previously ran on two conflicting scrapes. Both were wrong: the SimilarWeb scrape put Thailand at 27.25% (actual 45.40%) and Israel at #2 on 13.39% (actual #4 on 4.08%). Semrush's Thailand figure of 46.13% was close. **The practical consequence is in the ICP table: the rail-gap signal previously rested on Australia being top-3, which is false — Australia is #6. It now rests on Singapore at #2 with no PayNow, which is a cleaner basis and still scores.**

**Subdomain split** (HypeStat, volume unreliable but the split is useful): `bangkokair.com` 91.21% reach, `flightbooking.` 27.55%, `bookflight.` 22.86%. The supplied export includes subdomains, so these are inside the figures above.

### Section 2: Legal Entities & Local Presence

**Headquarters:** 99 Mu 14, Vibhavadirangsit Rd., Chom Phon, Chatuchak, Bangkok 10900. Registration **0107556000183**.

All 16 consolidated subsidiaries are Thai: Bangkok Air Catering (+5 regional catering entities), BFS Ground, SA Services, BFS Cargo DMK, Bangkok Airways Holding, Gourmet Primo, More Than Free (duty free), BA Aviation Training Center, Bangkok Reit Management, **Bangkok Airport Management**, Bangkok Airways Ground Services. Associates: WFS-PG Cargo, **U-Tapao International Aviation (40%)**, UTB, and the SET-listed **BAREIT**.

**Cross-Border Gap Analysis:**

| Country | In top-5 traffic? | Local entity? | Domestic acquiring gated? | Cross-border risk? |
|---|---|---|---|---|
| Thailand | ✅ #1 | ✅ HQ | No | Low |
| Israel | ✅ #2 / #4 | ❌ GSA only | No | **High** |
| USA | ✅ #3 | ❌ GSA only | No | **High** |
| Germany | ✅ #4 | ❌ GSA only | No | **High** |
| Australia | ✅ #5 / #3 | ❌ GSA only | No | **High** |

> **Warning: every single top-five traffic market except Thailand is served with no local entity.** Bookings from Israel, the USA, Germany, Australia and the UK are acquired cross-border out of Thailand, with the scheme cost, approval-rate drag and FX exposure that implies. None of these markets regulatorily gates domestic acquiring, so this is a cost-and-conversion argument rather than an access one — which makes it a *solvable* one.

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Region | Provider | Role | Evidence | Source |
|---|---|---|---|---|
| Multi-currency / APM set | **2C2P** | Alternative payment methods | `[Press Release]` — President quoted | [IR newsroom, 4 Jun 2018](https://investor.bangkokair.com/en/newsroom/corporate-news/125606/bangkok-airways-introduces-new-online-payment-channels) |
| Global | **Amadeus** | Altéa PSS + Digital/e-Retail front end | `[Source Code]` + `[Annual Report]` supplier table | Live JS bundle; 56-1 One Report 2025 p.148 |
| Global | **Sabre AirVision** | Revenue management only | `[Annual Report]` | 56-1 p.61 |
| Thailand | Unnamed **"acquiring bank"** | Card acquiring | `[Annual Report]` | 56-1 p.65 |

Verbatim from the 2018 release, Mr. Puttipong Prasarttong-Osoth, President:
> *"To make sure that the online transactions will be smooth and reliable, Bangkok Airways has teamed up with **2C2P** who are experts in this field of systems management. These added payment channels will also be able to support **multi-currency payments** which should broaden opportunities for Bangkok Airways to tap into some new markets in **South East Asia and China**."*

**The caveat matters as much as the quote.** This is the only primary source naming a PSP and it is from 2018. 2C2P now trades as "2C2P by Antom" under Ant International, which is consistent with the Alipay/WeChat/TrueMoney/ShopeePay spread, but no renewal or current-status announcement exists.

They also run **BIRTS** — "Bangkok Airways Internet Reservation and Ticketing System", versions 1 and 4, registered software copyrights in their own IP table. Combined with the `flightbooking.` and `bookflight.` subdomains, that means **they own the booking front end sitting over Amadeus inventory.** That front end is the integration surface, and it is the thing currently shipping a hardcoded method list.

**Infrastructure note, first-hand:** certificates exist for `pay.`, **`pg01.`** and **`pg02.`** subdomains. `pg01` (119.46.74.87), `pg02` (119.46.74.76) and `booking` (119.46.74.74) all resolve into the **same /24**, while `pay.` sits separately on Google Cloud (34.96.104.231). Two numbered "pg" hosts adjacent to the booking engine is suggestive, but none is publicly reachable and whois was unavailable, so **whether this is two acquirers, an active/standby pair or a migration is `[INFERENCE, not confirmed]`.**

#### 3B. Payment Orchestrator

> **No public or technical evidence of a payment orchestration platform.** Zero matches across the production JS bundle for CellPoint Digital, Juspay, Spreedly, Primer, Gr4vy, APEXX, Payrails, Outpayce, Yuno, IXOPAY or Corefy. The accepted-method list is a hardcoded string. The company integrates directly, which limits routing optimisation, failover and any multi-acquirer strategy.

**One honest uncertainty:** the card-entry step itself lives inside Amadeus Digital behind Imperva, which I could not reach. Airlines on full Altéa are sometimes bundled onto Amadeus's own payment layer (Outpayce XPP). I found **no evidence** of that here and am not asserting it — but *"is there an Amadeus payment layer between you and your acquirer?"* is the single best discovery question on this account.

### Section 4: Alternative & Local Payment Methods

Source of record: **https://www.bangkokair.com/payment-channel**, fetched and verified by me, consistent across EN and TH.

| Method | Category | Status |
|---|---|---|
| Visa, Mastercard, JCB, Diners, **Discover** | Cards | ✅ Active — enumerated on one line |
| **Union Pay** | Cards | ✅ Active — own section |
| **American Express** | Cards | ❌ **SOURCED-ABSENT** from the enumerated scheme line |
| Ali Pay, WeChat Pay, Line Pay, ShopeePay, TrueMoney Wallet | Wallet | ✅ Active — one e-wallet heading |
| Card instalments, min THB 3,000 | BNPL/Instalments | ✅ Active — BBL, SCB/CardX, UOB, Krungsri, TTB, Citi |
| Direct Debit ("Web Pay") | Bank / A2A | ✅ Active — BBL, SCB/CardX, KTB, KBank, Krungsri, TTB |
| ATM / internet banking / bank counter | Bank / A2A | ✅ Active |
| Counter cash — Lotus, Big C, PayPost, TrueMoney | Cash/voucher | ✅ Active — max THB 49,000 (TrueMoney THB 30,000) |
| **PromptPay** | Bank / A2A | ⚠️ **CONTESTED** — absent from the page, `PG_PROMPTPAY` present in live config |
| **7-Eleven / Counter Service** | Cash/voucher | ❌ **SOURCED-ABSENT** — Thailand's largest counter network is not on the list |
| **Apple Pay, Google Pay, PayPal** | Wallet | ❌ **SOURCED-ABSENT** |
| **PayNow** (Singapore) | Bank / A2A | ❌ **SOURCED-ABSENT** — zero occurrences on the enumerated page. **Singapore is the #2 market at 5.15% and growing +122%.** This is the ICP rail-gap signal |
| **GrabPay** (Singapore) | Wallet | ❌ **SOURCED-ABSENT** |
| PayTo, BPAY, Afterpay, Zip (Australia) | A2A / BNPL | ❌ **SOURCED-ABSENT** — Australia is #6 at 3.40%, so this is real but not the top-3 basis |
| Japan konbini, Korea local cards, India UPI | Various | ❌ **SOURCED-ABSENT** — no market-specific method for any inbound market |

**Singapore is the sharpest single gap.** It is the #2 market at 5.15%, growing +122% quarter on quarter, and PayNow — the rail most Singaporean consumers default to — is absent from the enumerated page, as is GrabPay. A Singaporean buyer gets a card form.

**The geographic restriction is the second finding.** Instalments and the entire direct-debit / ATM / counter block carry this restriction verbatim:

> *"This payment type will be available for all domestic and international flights departing from Thailand only"*

So for any itinerary not departing Thailand — a large share of their inbound traffic — the customer gets cards, Union Pay and wallets, and nothing else. **Fifteen selling markets, one Thailand-centric method set, and the local half of it switched off for anyone not starting their journey in Thailand.**

### Section 5: Payment Issues & Customer Complaints

**Honest assessment: low volume, scattered, mostly historical.** No concentrated recent cluster was found, TripAdvisor returned 403 and could not be quoted directly, and I am not going to inflate a handful of threads into a trend. **This scores 0 on the matrix.**

**Their own documentation is the stronger material.** From their FAQ (CMS-dated 2024-04-13):

> Q: *"My credit card payment failed, what should I do?"*
> A: *"Please contact our reservations call center at 1771 (Call from Thailand only) or +662 270 6699 everyday during 8 a.m. - 8 p.m. (BKK local time)"*

A declined card has **no in-session recovery path**. The documented remedy is a phone call, to a line open 12 hours a day, on a toll-free number that only works inside Thailand — for an airline whose buyers are majority non-Thai and in timezones from Israel to Australia to the US West Coast. Every foreign decline outside those hours is a lost booking.

Also from their own material:
- **Third-party cards are banned:** *"The card holder must be one of the traveling party listed in the itinerary."* That blocks family, gift, corporate and PA-booked travel.
- **A physical card check at the airport** is used as a fraud control: a random check of the card used for online payment, with failure to present it requiring the passenger to **buy new tickets for all sectors**.
- Failed payments are pushed into an out-of-session **pay-by-link** retry (`/re-payment`, `/pgpaybylink`), with a *"Your payment link has expired"* state.
- **Refunds take 30 business days**, to the original card only.
- Fraud screening is outsourced: *"Bangkok Airways employs a third party fraud prevention operator to audit all payment transactions."* The operator is not named.

Recurring theme in the forum threads, directional only: **foreign-card rejection** (one user's Business Mastercard declined while a Visa went through).

### Section 6 & 7: Corporate and Payment Developments

| Date | Development | Category |
|---|---|---|
| Jun 2026 | Board approved further THB 2,000.0m into U-Tapao International Aviation | Capital |
| 2Q 2026 | Capacity cuts: Bangkok–Phuket, Samui–Singapore, Bangkok–Maldives; jet→turboprop downgauging | Network contraction |
| Aug 2025 | Firm ATR order, 10–12 × ATR 72-600, deliveries Q4 2026–2028 | Fleet |
| Jul 2025 | Samui Airport aerodrome certificate moved to Bangkok Airport Management Co., Ltd. | Corporate |
| Oct 2025 | **Bangkok–Lampang discontinued** (after Lampang–Mae Hong Son in July 2025) | Network contraction |
| May–Dec 2025 | Share buyback: 25.7m shares (1.23%), THB 361.5m | Capital |
| 30 May 2023 | IATA Airline Retailing Maturity status | Distribution |
| **4 Jun 2018** | **"Bangkok Airways Introduces New Online Payment Channels" — the 2C2P partnership** | **Payment** |

**No public payment RFP found. No payment-related hiring found.**

The most telling line in the whole 56-1: *"In 2010, we upgraded our website to increase Internet sales and reduce agency commissions."* That sentence appears verbatim in the **FY2025** report. The last website milestone they cite is sixteen years old.

### Section 8: Checkout Experience Audit

**Partial.** `digital.bangkokair.com` and `flightbook.bangkokair.com` are behind **Imperva** bot protection (`reese84` interstitial) and the card-entry page was never reached.

| Dimension | Finding |
|---|---|
| Checkout type | Self-built front end (BIRTS) over Amadeus Digital / e-Retail |
| Payment methods visible | Hardcoded six-value list: `PG_CC, PG_EXT, PG_EWALLET, PG_PROMPTPAY, PG_IP, PG_MOBILEBANK` |
| Location-based method display | **No.** One static list for all 15 country sites |
| Instalments | Thailand-departing itineraries only, min THB 3,000 |
| BIN handling | Present, but used for **campaign eligibility**, not routing |
| Multi-currency | 15 country sites gate a `disableFxBox` flag; no published pricing detail |
| Error recovery | **None in-session.** Documented remedy is a phone call; failed payments go to pay-by-link |
| 3DS | Not observable |
| Mobile app | iOS/Android, last documented major version 3.0.0 (Feb 2018) |

### Section 9: PCI DSS Compliance

**No direct PCI compliance documentation found publicly** — not on the site, not in the 56-1, not in the MD&As, not in search. The only payment-security statement is the unnamed third-party fraud operator quoted in Section 5. Their airport card-check policy suggests risk controls are pushed onto ground staff rather than handled in the payment layer.

They did win an **ASOCIO Award 2025 for Cybersecurity Excellence** — which makes the absence of any PCI statement, and the exposed API key noted in the handling note, a genuine contrast worth understanding before assuming the stack is weak everywhere.

### Section 10: Strategic Insights & Outreach Angles

**Insight 1 — Foreign buyers, Thai-only rails, by their own documentation.**
> **Evidence:** Section 1 (**Thailand 45.40%, so 54.60% of traffic is non-Thai across 19 countries above 1%** — supplied SimilarWeb data) + Section 4 (instalments, direct debit, ATM and counter are restricted verbatim to *"flights departing from Thailand only"*) + Section 2 (no legal entity outside Thailand).
The majority of their buyers cannot use the majority of their payment methods. This is the account's defining asymmetry and every half of it comes from their own published material.

**Insight 2 — The method list is a code release, not a configuration.**
> **Evidence:** Section 3B (`paymentMethodsToDisplay` hardcoded as a six-value string) + Section 6 (the last payment-channel announcement was 2018; the last website milestone cited in the FY2025 report is from 2010).
Adding a method means a front-end deployment. That explains an eight-year gap between payment announcements better than any assumption about strategy does.

**Insight 3 — They already pass BIN data, and use it for discounts rather than routing.**
> **Evidence:** Section 3B (`binNumber` sourced from `cc_bin` inside the campaign-parameter block) + Section 4 (bank-specific instalment eligibility across six Thai banks).
The plumbing to make per-BIN decisions exists and runs today. It decides who gets a promotional fare. It does not decide which acquirer takes the transaction.

**Insight 4 — A declined card becomes a phone call.**
> **Evidence:** Section 5 (their FAQ's documented remedy is a 12-hour-a-day call centre on a Thailand-only toll-free number) + Section 1 (buyers in Israel, Europe, the US and Australia, across every timezone).
This is the single best fit for the Wingo case, where retries across multiple providers replaced exactly this kind of dead end.

**Strongest entry point:** cross-border approval rate on inbound bookings, evidenced by their own "departing Thailand only" restriction. Frame it as recovering revenue on traffic they already have — they are contracting, so growth framing will not land.

### Section 11: Competitors & Orchestration Adoption

| Airline | PSP / Acquirer | Orchestrator | Evidence |
|---|---|---|---|
| **Thai Airways** | 2C2P | None named | Trade press |
| **Cebu Pacific** | Multi-acquirer | **CellPoint Digital** | Vendor case study, Feb 2024 (publishes no numbers) |
| **Malaysia Airlines** | 2C2P | **Outpayce XPP** | Vendor case studies — quotes "authorization rates increase by 3-4 per cent" |
| **Sun PhuQuoc Airways** | 2C2P + M-Pay | **2C2P PACO** | Trade press, Mar 2026 |
| **Vietnam Airlines** | Adyen | **2C2P PACO + Outpayce XPP** | See `vietnam-airlines.md` in this repo |
| **VietJet Air** | Galaxy Pay, Cybersource, MPGS, Adyen, 2C2P | In-house | See `vietjet-air.md` |
| **Singapore Airlines / Cathay Pacific** | Adyen direct acquiring | None — consolidated instead | Vendor releases |

**The pattern:** Bangkok Airways' regional peer group has largely moved. Thai Airways shares its PSP; Malaysia Airlines and Cebu Pacific added orchestration layers; Vietnam Airlines and Sun PhuQuoc signed 2C2P PACO. Bangkok Airways is one of the few SEA carriers still on a single direct integration with a hardcoded method list.

### Section 12: Business Case Data

| Metric | Value | Source |
|---|---|---|
| FY2025 total revenue | **THB 26,067.2m (~US$800m)** | FY2025 MD&A |
| **FY2025 passenger revenue** | **THB 17,574.0m (67.4%)** | 56-1 One Report 2025 p.36 |
| FY2025 net profit | THB 3,580.3m (−5.7% YoY) | FY2025 MD&A |
| Scheduled passengers FY2025 | **4,226,000** | IR operating statistics |
| **Average fare per sector** | **THB 4,148.5** (~US$128) | FY2025 MD&A |
| **Direct channel share** | **49.3% of passengers FY2025; 47.0% 1H2026** (website + direct connect) | FY2025 & Q2-2026 MD&A |
| Selling & distribution expense | THB 1,162.3m (−9.7% YoY) | FY2025 MD&A |
| Reservation expense (derived) | ≈ THB 657m `[ESTIMATE]` | Derived from the stated −6.5% / −THB 45.7m |
| Fleet | 22 aircraft (from 25) | FY2025 MD&A |
| Domestic share of passengers | **88.7%** | 56-1 |
| Market cap | THB 32,340m `[ESTIMATE, not confirmed]` | companiesmarketcap.com — inconsistent with 2.1bn shares × THB 19.40 |

**Orchestrable volume is the THB 17,574.0m passenger line, roughly half of which is direct** — so on the order of **THB 8.7bn (~US$267m)** of directly-acquired ticket value per year. The airport-related services line (THB 5,852.1m) is B2B catering and ground handling billed to other airlines, not consumer card payments, and should be excluded from any business case.

### Overall Research Confidence

**Medium-High.** Financials, entity structure and the direct-channel split are **High** — all read from their own filed 56-1 and MD&A PDFs. The payment-stack architecture is **High** — the hardcoded method list, the Amadeus endpoints and the orchestrator absence were verified directly in the production JS bundle. Traffic is now **High** for country mix — supplied SimilarWeb data covering all 69 countries with subdomains included, which resolved a disagreement the earlier scrapes could not — but **Low for absolute volume**, which the export does not contain. Checkout is **Low** — Imperva blocked the card-entry page entirely. Complaints are **Low** and honestly scored as such.

### Manual Research Recommendations

> **Area:** ~~Traffic country mix~~ — **CLOSED 2026-09-15.** Prateek supplied the SimilarWeb geography export. Thailand 45.40%, 19 countries above 1%, all 69 listed.
> **Still open:** absolute visit volume. The geography export does not carry totals, so the business case has no verified denominator.
> **Action:** pull the SimilarWeb Website Performance export for total visits if a sized business case is needed.

> **Area:** The live checkout.
> **Why it matters:** Single-acquirer is inferred from a hardcoded method list, not observed. Whether an Amadeus payment layer sits in the path is unresolved, and it changes the motion.
> **Action:** Walk a real booking from a non-Thai IP with DevTools open. Watch for the acquirer, 3DS flow, and whether PromptPay actually renders.

> **Area:** PromptPay.
> **Why it matters:** It is the one method where their documentation and their code disagree, and it would be embarrassing to assert either way in an email.
> **Action:** One booking attempt from a Thai IP to see whether PromptPay appears at the payment step.
