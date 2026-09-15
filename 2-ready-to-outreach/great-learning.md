# Great Learning

**Status:** 🟢 Ready to outreach — sequence drafted
**ICP Score:** 9 / 24 → 🟢 Medium *(see analyst note — the matrix understates this account)*
**Industry:** E-Learning & EdTech · **HQ:** Bengaluru, India · **Researched:** 2026-09-14 · **First email sent:** —
**Motion:** Greenfield — no orchestrator detected

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Indian online upskilling company selling high-ticket professional programmes with university partners (UT Austin McCombs, Johns Hopkins, MIT, Duke, Harvard, Chicago Booth, IIT Bombay). FY25 revenue ₹1,039 Cr, claims 13.8M learners across 170+ countries. **It already made a local-payment-methods-and-instalments buying decision for Latin America in 2023, and has no equivalent anywhere else.**

**SimilarWeb total visits (last full month):** **No usable data.** The supplied pull measured `greatlearning.in`, which 301-redirects to `www.mygreatlearning.com` — a redirect stub, not a property. See `accounts/traffic/great-learning.md` for why it was rejected. **Three ICP signals are unevaluable as a result.**

### Top 5 markets
**Cannot be populated.** No verified country traffic profile exists. What is evidenced about geography:

| Market | Evidence | Accepted methods | Missing methods | Local entity |
|--------|----------|------------------|-----------------|--------------|
| India | HQ, ₹1,039 Cr revenue, all consumer complaints in INR | Not observed — India flow never rendered | UPI/netbanking **not found**, but never sourced as absent | ✅ Bengaluru (HSR Layout) |
| United States | USD-priced programmes, US university partners, US-geo pages served | Bank transfer, credit/debit card **only** (sourced) | **No PayPal, no wallets, no Apple/Google Pay** (sourced absence) | ❌ none found |
| Mexico · Brazil · Colombia | **dLocal partnership, Sep 2023** — local currency, up to 12 instalments | Local methods via dLocal | — | ❌ none found |

### Legal entities
- **Great Learning Education Services Pvt Ltd** — HSR Layout, Plot 1501, 19th Main Rd, Sector 1, Bengaluru 560102
- Great Lakes E-Learning Services Private Limited — CIN U80302DL2010PTC211483 `[UNVERIFIED]`
- No entity found in the US, Singapore, or any LatAm market despite selling in all three

### Known PSPs
- **dLocal** — `[Press Release]` Mexico, Brazil, Colombia only
- **Affirm · Climb Credit · Splitit** — `[Source Code]` international financing facilitators, from `intl/` logo markup
- **Eduvanz · Propelld** — named by complainants as India loan partners. `[UNVERIFIED]` — no primary source
- **No card acquirer or gateway identified for India, the US, or anywhere else.** Zero PSP signatures across 2.0 MB of fetched HTML

### Orchestration status
**None detected — direct integrations only.** No Juspay, Hyperswitch, Primer, Gr4vy, Spreedly, Payrails, IXOPAY or Yuno signature in any fetched page, and no search result connecting Great Learning to any orchestrator. Caveat: no checkout page is publicly reachable, so this is no public evidence rather than proven absence.

### Buying signals
- 🤝 **[dLocal partnership, 21 Sep 2023](https://www.businesswire.com/news/home/20230921634934/en/Great-Learning-Partners-With-dLocal-Enabling-Local-Payment-Methods-and-Installments-in-Mexico-Brazil-and-Colombia)** — local payment methods and up to 12 instalments in Mexico, Brazil and Colombia. **They have already bought this category once, for a region that is not their home market.**
- ⚠️ **A structurally guaranteed dispute pattern** — admission fee collected before third-party financing is underwritten, refund refused when the lender declines. Documented 2021–2024.
- 💰 FY25 revenue ₹1,039 Cr (+4.7%), operating profit tripled to ₹40.23 Cr — margin extraction, not growth `[UNVERIFIED — search summary]`
- 🔄 Ownership: acquired by Byju's Jul 2021 (~$600M), **reacquired by founder Mohan Lakhamraju Jan 2024** `[UNVERIFIED — Tracxn]`
- ❌ No payment RFP, no payments hiring, no funding in the last 12 months

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

### Pain Vector Extraction

```
Motion: Greenfield — no orchestrator signature in 2.0 MB of fetched HTML, and no search
result connects them to one. Caveat carried from research: no checkout is publicly
reachable, so this is "no public evidence" rather than proven absence. The sequence never
asserts they have no routing layer; it argues from the coverage gap instead, which holds
either way.

Observable setup facts (from research, with sources):
- dLocal partnership, 21 Sep 2023: local payment methods and up to 12 instalments across
  Mexico, Brazil and Colombia — source: BusinessWire press release, first-party
- "You can pay via bank transfer or credit/debit cards" — source: international programme
  FAQ, fetched. An ENUMERATED list, so a genuine sourced absence: no PayPal, no wallets,
  no Apple or Google Pay on that flow
- UT Austin programme priced USD 3,950, with an admission fee of USD 800-1,000 followed by
  three instalments — source: programme page, fetched
- Terms reference "payment gateways", plural, and name none — source: /terms, fetched
- Privacy policy: refunds may be paid to a "bank account, payment gateway or e-wallet"
  — source: /privacy-policy, fetched. Refunds may not return to the original instrument
- Affirm, Climb Credit and Splitit appear in logo markup under images/template-pp/intl/
  — source: page source. The intl/ path proves a separate regional configuration exists
- No card acquirer or gateway identified for India or the US — zero PSP signatures found

Selected observations for Phase 1 (E1 bullets, ranked by materiality):
1. dLocal 2023 bought local methods and up to 12 instalments, for three countries
   → "You added local methods and up to 12 instalments for Mexico, Brazil and Colombia."
2. The international flow enumerates two method types on a USD 3,950 ticket
   → "The international programme FAQ says bank transfer or credit/debit card."
3. Their Terms name no gateway despite using the plural
   → "Your Terms mention payment gateways, plural, without naming one."

THE ASYMMETRY (the samples' strongest move, and it is entirely first-party here):
A learner in Mexico gets local methods and up to twelve instalments. A learner buying the
same category of programme in USD gets an admission fee and three bank transfers. Both
halves are Great Learning's own published material, so neither is disputable.

Bridge variant: B — limitations
Rationale: exactly one PSP is publicly identifiable (dLocal), covering three of a claimed
170+ countries. That is a single-provider footprint against a multi-market business, which
is B. It is not A, because there is no evidence of two parallel stacks to be complex about.

Hypothesis for Phase 2 (E3):
The LatAm decision was right and it stopped at three countries. The same high-ticket
conversion problem exists in every other market they sell into, and the USD flow is the
clearest case.
Backing logic: buying instalments for LatAm is itself proof they believe high-ticket
education converts on them. The international flow then enumerates two method types on a
USD 3,950 ticket. Nothing in the file suggests the belief changed; it just was not extended.

Success case for Phase 3 (E4):
Selected case: Vibra
Tier: 2 — same payment pattern, different industry and region. Stated as such in the copy.
Match rationale: Vibra's problem was first-time buyers being declined, solved by bringing
more providers in, routing per transaction, and launching new methods. Great Learning's
buyers are almost entirely first-time purchasers, since an upskilling programme is a
one-off high-ticket purchase, not a repeat one. That pattern match is tighter than the
edtech label would be.
Numbers to lead with: new-user approval up more than 30 percentage points, reaching 80% ·
Apple Pay, Nu Pay and Google Pay launched in record time · more providers into the
operation with each transaction routed on data
⚠️ HONEST DEVIATION: Vibra publishes TWO hard numbers, not three. The third bullet is a
mechanism, not a metric, and is written as one. Livelo carries three quantified results
(+5% approval, 50% of failed transactions recovered, millions of R$ saved) and is the
swap if Prateek wants three numbers, but its mechanism is decline recovery, and nothing in
the research evidences a decline problem at Great Learning. Matching the mechanism was
judged more important than hitting the bullet count. Verified live at source 2026-09-15.
Open English carries the edtech relevance as a one-line name only, no numbers, per the
library rule.
Optional benchmark: SKIP. The "~8% average authorisation uplift" traces to Yuno's own blog,
so it is marketing rather than independent evidence.

Touch-by-touch angles:
- E2 angle: method coverage stops at three countries → one integration to add any method,
  no per-rail rebuild
- LK1 angle: 12 instalments in LatAm, bank transfer or card on the international flow
- LK2 angle: the LatAm decision was right and stopped at three countries
- LK3 angle: Vibra's first-time buyers stopped hitting a decline on their first purchase
- LK4 angle: refunds may be paid to a bank account, gateway or e-wallet (held back, fresh)
- E8 angle: clean exit, no new observation
```

---

### Phase 1 — Curiosity (Days 1–5)

#### Touch 1 — Email 1 · Day 1 · Tue 15 Sep

**Subject:** 12 instalments in LatAm only

```text
Hey {{recipient.first_name}},

Spent some time looking at Great Learning's payment setup. Three things stood out.

In September 2023 you added local methods and up to 12 instalments across Mexico, Brazil
and Colombia, through dLocal.

Your international programme FAQ offers bank transfer or credit/debit card. That's on a
USD 3,950 ticket.

Your Terms mention payment gateways, plural, without naming one.

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

Following up. Wanted to put a bit more behind what Yuno actually does, and how it maps to
what I flagged.

We sit above the providers you already run. dLocal stays exactly where it is.

One integration covers the methods, so extending local rails and instalments into a fourth
market, or a fortieth, becomes configuration rather than a new provider evaluation.

Routing then decides per BIN, market and method which provider a transaction takes, and
moves traffic automatically when one degrades.

The 2023 decision is the part worth building on. You already concluded local methods and
instalments move high-ticket enrolments. What's left is extending that, not re-testing it.

I'll keep sharing what I'm seeing every few days. If your stack's where you want it, say
the word and I'll back off. Otherwise happy to go deeper.

Cheers,
Prateek
```

#### Touch 3 — LinkedIn message 1 · Day 5 · Sat 19 Sep

> ⚠️ **Lands on a Saturday.** Shift to Mon 21 Sep, or pull forward to Fri 18 Sep.

```text
Hey {{recipient.first_name}}, figured I'd flag this here too in case it's more useful than
email. Quick one: a learner in Mexico gets local methods and up to 12 instalments, while
your international FAQ offers bank transfer or card on a USD 3,950 programme. Curious
whether that gap is deliberate or just hasn't come up yet.
```

---

### Phase 2 — Diagnosis (Days 7–9)

#### Touch 4 — Email 3 · Day 7 · Mon 21 Sep · NEW EMAIL

**Subject:** Read on the three-country ceiling

```text
Hey {{recipient.first_name}},

Going to take a swing at this. My read is that the 2023 LatAm decision was right and
stopped at three countries.

Buying instalments for those markets says you concluded high-ticket education converts on
them. That conclusion just wasn't extended.

The international FAQ then offers two ways to pay on a USD 3,950 programme. Not because
anyone's doing it badly, but a list that short tends to reflect how many providers are
wired in.

At Yuno (a16z-backed, top-100 fintech) we sit above your existing providers, so a market
gets local methods without a new integration behind it. Keep your stack, add what's missing.

Thursday the 24th is open. Would 11am or 4pm your time work for 15 minutes? If payments
sits elsewhere, happy to be pointed there.

All the best,
Prateek
```

#### Touch 5 — LinkedIn message 2 · Day 9 · Wed 23 Sep

```text
Hey {{recipient.first_name}}, sent a longer note over email this week. Short version: the
LatAm instalments decision looks right, and it looks like it stopped at three countries
rather than being extended. If that's anywhere on your radar, would Monday the 28th or
Tuesday the 29th at 3pm your time work for a quick 15?
```

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · Fri 25 Sep · NEW EMAIL

**Subject:** How Vibra solved this

```text
Hey {{recipient.first_name}},

On the read I shared last week, here's what solved looks like.

Vibra is Brazil's fifth-largest company. Inside Premmia, its loyalty and payments app, too
many first-time users hit a decline on their first purchase. They brought Yuno in:

- New-user approval up more than 30 percentage points, reaching 80% (not too bad, right?)
- Apple Pay, Nu Pay and Google Pay live in record time
- More providers into the operation, with each transaction routed on data rather than a
  fixed path

Different industry, but a professional programme is a one-off purchase, so almost every
buyer of yours is a first-timer too. Open English, an online English school across 30-plus
countries, runs on the same layer if you want the education version.

Same orchestration layer above their existing stack. No rip-out.

When a learner outside the dLocal markets wants to pay in instalments, what happens today?

Wednesday the 30th, would 10am your time work for 15 minutes?

Full case here if useful: https://y.uno/en/success-stories/vibra

Best,
Prateek
```

#### Touch 7 — Email 5 · Day 13 · Sun 27 Sep · MANUAL

> ⚠️ **Lands on a Sunday.** Shift to Mon 28 Sep.

*Placeholder — manual creative approach. Do not auto-write.*

Suggested angle for this account: a side-by-side of the LatAm enrolment flow against the
international one, screenshotted. The asymmetry does the arguing without a word of pitch.

#### Touch 8 — Email 6 · Day 15 · Tue 29 Sep · MANUAL

*Placeholder — second manual approach, different format than E5.*

Suggested angle: a short Loom attempting a UT Austin enrolment as a learner in a market
dLocal does not cover, stopping at the point where the options run out.

#### Touch 9 — LinkedIn message 3 · Day 17 · Thu 1 Oct

```text
Hey {{recipient.first_name}}, Vibra's problem was that first-time buyers kept hitting a
decline on their very first purchase, which is most of your buyers too. Worth 15 minutes to
see whether it maps? Tuesday the 6th at 4pm your time is open.
```

---

### Touch 10 — Email 7 · Day 19 · Sat 3 Oct · MANUAL

> ⚠️ **Lands on a Saturday.** Shift to Fri 2 Oct, except that is Gandhi Jayanti. Use Mon 5 Oct
> and move LK4 out, or send Thu 1 Oct alongside LK3.

*Placeholder — manual creative bridge. Anchor to something fresh.*

Suggested anchors: the IIT Bombay and Johns Hopkins programme partnerships, or the FY25
results. ⚠️ **Do not anchor to the ownership change** (the BYJU'S sale and the founder
reacquisition) until it is verified at source. It is `[UNVERIFIED — Tracxn]` in the research
and getting an ownership fact wrong in writing would end the thread.

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21 · Mon 5 Oct

```text
Hey {{recipient.first_name}}, last LinkedIn ping from me on this. One thing I never raised:
your privacy policy says refunds may go to a bank account, gateway or e-wallet, so money
doesn't always return the way it arrived. If that's worth 15 minutes, Friday the 9th at
11am your time is open.
```

#### Touch 12 — Email 8 · Day 23 · Wed 7 Oct · REPLY IN THREAD to Touch 4 or 6

```text
Hey {{recipient.first_name}},

Going to stop pinging unless you want to pick this back up.

If the timing's just off, happy to circle back next quarter, once the current programme
cycle has run.

If it ever comes back up, just reply here.

Cheers,
Prateek
```

---

### Source Notes

- ✅ **dLocal partnership, local methods and up to 12 instalments in Mexico, Brazil and
  Colombia, 21 Sep 2023** — [BusinessWire](https://www.businesswire.com/news/home/20230921634934/en/Great-Learning-Partners-With-dLocal-Enabling-Local-Payment-Methods-and-Installments-in-Mexico-Brazil-and-Colombia),
  first-party. Named in E1, E2, E3, LK1 and E4.
- ✅ **"You can pay via bank transfer or credit/debit cards"** — international programme FAQ,
  fetched during research. This is an enumerated list, which is what makes it a sourced
  absence rather than a guess.
- ✅ **USD 3,950 programme, admission fee then three instalments** — UT Austin programme
  page, fetched.
- ✅ **Terms reference "payment gateways", plural, naming none** — /terms, fetched.
- ✅ **Refunds may be paid to "bank account, payment gateway or e-wallet"** — /privacy-policy,
  fetched. Used in LK4 only.
- ✅ **Vibra: +30 percentage points to 80% new-user approval; Apple Pay, Nu Pay and Google
  Pay in record time** — re-verified at source 2026-09-15. Region stated as Brazil in the
  copy, so nothing implies an APAC or India result.
- ✅ **Open English, 30-plus countries** — named with no metric attached, per the library rule
  that it carries no public numbers.
- ⚠️ **India is never mentioned in any touch, deliberately.** Research could not render the
  India flow, so UPI and netbanking are recorded as *not found*, not as *sourced absent*.
  Claiming a UPI gap would be asserting an unchecked absence. If Prateek gets the India-geo
  page from an Indian IP, that becomes the strongest touch in the sequence and E1 should be
  rewritten around it.
- ⚠️ **E1 and E3 run over their word budgets** (112 against ~85–110, and ~135 against
  ~90–120). Everything left in E3 is rulebook-mandated: hypothesis, two lines of backing,
  Yuno re-state, CTA. Cut the "not because anyone's doing it badly" clause if Prateek wants
  it inside budget, at the cost of the observation reading harder.
- ⚠️ **E4 carries two quantified bullets, not three.** Vibra publishes two. See the deviation
  note in the extraction block; Livelo is the three-number swap if wanted.
- ⚠️ **No named contact.** `{{recipient.first_name}}` throughout. Research surfaced no
  payments decision-maker, and the ownership position is unverified, so the recipient needs
  picking manually before send.
- ⚠️ **Three touches land on weekends** (LK1 Sat 19 Sep, E5 Sun 27 Sep, E7 Sat 3 Oct), and
  **Fri 2 Oct is Gandhi Jayanti**, a national holiday in India. No CTA proposes the 2nd.
  Flagged inline.
- ⚠️ **Trustpilot findings stay out of the sequence entirely** — the chargeback, the 4%
  processing fee on a refund and the EMIs continuing after cancellation are all
  search-summary only, since Trustpilot returned 403 on every fetch. Do not add them.
- ⚠️ **The refund-dispute pattern stays out of the auto-written touches** even though it is
  sourced (8 of 11 complaints on consumercomplaints.in). Leading a cold email with a
  customer-complaint pattern reads as combative. It belongs in a manual touch or a call,
  once there is a relationship to carry it.

### Notes on what this sequence deliberately does not claim

The research file scores this 9/24 and carries an analyst note explaining that three signals
score zero because **data is missing, not because the signal is absent**. The sequence is
built only on what is actually evidenced, which is why it argues coverage rather than
approval rates: there is no traffic data, no PSP identified for India or the US, no PCI
posture and no reachable checkout.

**The highest-value action on this account is still not an email.** It is re-pulling
SimilarWeb against `www.mygreatlearning.com` rather than `greatlearning.in`, and rendering
the India programme page from an Indian IP. Either could reshape the opening, and the India
one could make it substantially stronger.

### Success Case Alternatives

- **Livelo** — swap for E4 if three quantified bullets matter more than mechanism fit:
  +5% approval, 50% of failed transactions recovered, millions of R$ saved. Its story is
  decline recovery via a secondary acquirer, which the research does not evidence here.
- **Open English** — the only edtech logo in the library, used here as a one-line relevance
  signal. It cannot carry an E4 because it publishes no numbers.
- **inDrive** — Tier 2 fallback if the conversation turns to market expansion rather than
  method coverage: roughly 90% approval, 10 new countries in under 8 months, LATAM.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 9 / 24
| Signal | Points | Status |
|--------|--------|--------|
| Orchestration status | +4 | ✅ **None detected.** No orchestrator signature in 2.0 MB of fetched HTML; no search result links them to any. Greenfield |
| 3+ countries | +3 | ✅ India (HQ), US (USD programmes), Mexico/Brazil/Colombia (dLocal). 170+ claimed |
| Multiple PSPs | 0 | ⬜ **Only one named — dLocal.** Their Terms say "payment **gateways**" plural and name none. A second provider almost certainly exists, since dLocal covers three LatAm markets and cannot be serving India or the US. **Logically near-certain, evidentially unconfirmed — scored 0 rather than stretched** |
| Local rail or licensing gap in a top-3 market | 0 | ⬜ **Unevaluable.** No traffic data means no top-3. The sourced absence (bank transfer and cards only, no wallets) is scoped to the US-served international flow; India's rails were never rendered |
| Recent expansion | 0 | ❌ dLocal was Sep 2023, outside 12 months. IIT Bombay and Johns Hopkins are academic tie-ups, not market entry |
| Payment issues reported | +2 | ✅ **Confirmed and concentrated.** 8 of 11 complaints on consumercomplaints.in are refund disputes, spanning Mar 2021 → May 2024 |
| Funding >$10M | 0 | ❌ None in the last 12 months |
| High traffic outside home | 0 | ⬜ **Unevaluable** — no traffic data |
| Competitor using orchestration | 0 | ❌ None found at upGrad, Simplilearn, Scaler, Emeritus or Coursera India |
| Payment job postings | 0 | ❌ None found |

**Tier:** 🟢 Medium (9).

> ### Analyst note — the matrix understates this account, and here is precisely why
>
> **No override applied to the tier**, because inflating a score on missing data is exactly the failure this matrix exists to prevent. But the number should not be read as the account's quality.
>
> **Three of the ten signals score zero because data is absent, not because the signal is absent.** Multiple PSPs, local rail gap and traffic-outside-home are all unevaluable without a valid country profile. A clean `mygreatlearning.com` SimilarWeb pull would plausibly move this account by 5–8 points on its own.
>
> **The matrix has no line for the strongest signal in the file.** Great Learning partnered with dLocal in September 2023 to add local payment methods and 12-month instalments across Mexico, Brazil and Colombia. That is a merchant who has already run this evaluation, understood the category, and signed — for a region that is not their home market. No ICP signal captures "has already bought this exact thing once." It is worth more than several signals that do score.
>
> **Counterweight, stated honestly:** the sale is counsellor-led with no public self-serve checkout, so where money is actually captured is invisible from outside. If a large share of Indian programme value is originated as an NBFC loan rather than collected on a checkout, the orchestrable volume is smaller than ₹1,039 Cr implies. That is the first question for a discovery call.

### Source Notes
- ✅ **dLocal partnership** — BusinessWire press release, 21 Sep 2023, first-party
- ✅ **Terms say "payment gateways" (plural), name none; merchant does not store card data** — mygreatlearning.com/terms, fetched
- ✅ **Privacy policy: refunds may be paid to "bank account, payment gateway or e-wallet"** — mygreatlearning.com/privacy-policy, fetched. Refunds may not return to the original instrument
- ✅ **UT Austin programme: USD 3,950, admission fee 800 or 1,000 USD plus three instalments** — programme page, fetched
- ✅ **Accepted methods: "You can pay via bank transfer or credit/debit cards"** — programme FAQ, fetched. An enumerated list, so a genuine sourced absence for the international flow
- ✅ **Affirm, Climb Credit, Splitit** — logo markup under `images/template-pp/intl/`, fetched. The `intl/` path proves a separate regional set exists
- ✅ **8 of 11 refund complaints, Eduvanz named twice, Propelld once** — consumercomplaints.in, page opened and all 11 read
- ✅ **No orchestrator, no PSP signature** — grep across 2.0 MB of fetched HTML returned zero
- ⚠️ **Trustpilot findings are the most interesting and least verified.** A USD 2,500 chargeback, a 4% processing fee deducted from a refund, EMIs continuing after course cancellation — **all search-summary only; Trustpilot returned 403 on every fetch attempt.** Do not use in outreach without re-reading at source
- ⚠️ **Ownership, FY25 financials, learner counts** — Tracxn, Entrackr and Crunchbase summaries, not read at source
- ⚠️ **Eduvanz and Propelld appear only in consumer complaints.** Directionally credible, not citable
- ❌ **No traffic data. No PSP for India or the US. No PCI posture. No checkout reachable**

### Success Case Alternatives
- **Open English** — Tier 1 pattern: edtech, subscriptions, 30+ countries, multi-market recurring. Closest vertical match in the library
- **inDrive** — Tier 2: multi-country acquiring at scale. LATAM results; label them as such
- ⚠️ **Do NOT use Qatar Airways** — withdrawn from the credibility defaults, no source connects it to Yuno

---

## Executive Summary

Great Learning sells high-ticket professional education (USD 3,950 on the UT Austin programme; ₹2.75 lakh on Indian equivalents) to learners in a claimed 170+ countries, through a counsellor-led sale with no public self-serve checkout. It has **no payment orchestration layer** and no publicly identifiable card acquirer in any market. The defining finding is that it **already solved the local-methods-and-instalments problem once, for Latin America, via a dLocal partnership in September 2023** — and has no equivalent for India, the US, or anywhere else. The motion is **greenfield**, and the opening is not the case for orchestration but the question of why the solution stopped at three countries.

---

### Section 1: Website Traffic Analysis by Country

**Data source: none usable.**

The supplied SimilarWeb pull (2026-09-10) was taken against `greatlearning.in`. That domain **301-redirects to `www.mygreatlearning.com`** — verified by following the redirect chain. It is a redirect stub, so the traffic attributed to it is an artefact: India country rank #95,988, Pakistan at 19% of traffic with 98.21% bounce and exactly 1.00 pages per visit, seven markets showing change of exactly −100%. That data is rejected and recorded as such in `accounts/traffic/great-learning.md`.

**No country profile is asserted here.** Consequences, stated plainly:
- The Top 5 markets table cannot be built
- The APM gap analysis cannot be anchored to traffic share
- Two ICP signals (high traffic outside home, local rail gap in a top-3 market) are unevaluable

**What geography is evidenced, without shares:**

| Market | Evidence | Source |
|---|---|---|
| India | HQ Bengaluru; FY25 revenue ₹1,039 Cr; every consumer complaint denominated in INR | Entrackr `[UNVERIFIED]`; consumercomplaints.in |
| United States | USD-priced programmes; US university partners; US-geo pages served in USD with zero INR strings | programme page, fetched |
| Mexico, Brazil, Colombia | dLocal partnership for local methods and instalments | BusinessWire, Sep 2023 |
| 170+ countries (claimed) | Company/Tracxn claim of 13.8M learners across 170+ countries | Tracxn `[UNVERIFIED]` |

> **MANUAL — highest-value action in this file:** re-pull SimilarWeb against `www.mygreatlearning.com` with "Include all country domains" ON. `greatlearning.in` merging in is now expected rather than suspicious.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Bengaluru, India — Plot 1501, 19th Main Rd, 1st Sector, HSR Layout, Bengaluru 560102.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| India | **Great Learning Education Services Pvt Ltd** | not found | Address and website confirmed on a consumer-complaint record naming `www.mygreatlearning.com` |
| India | Great Lakes E-Learning Services Private Limited | CIN U80302DL2010PTC211483 | `[UNVERIFIED — surfaced in a prior pass, registry page not opened]` |
| US / Singapore / LatAm | **None found** | — | — |

**Ownership chain** `[UNVERIFIED — Tracxn and Crunchbase summaries, not read at source]`:
- Jul 2021 — acquired by BYJU'S (Think & Learn), valuation cited ~USD 600M
- Jan 2024 — recorded as "Acquired – II": reacquired by founder **Mohan Lakhamraju** from BYJU'S

**This matters commercially and is not yet confirmed.** An account mid-ownership-change has either a frozen budget or a brand-new decision-maker. Resolve before writing.

**Cross-Border Gap Analysis:**

| Country | In traffic profile? | Local entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|--------------------|---------------|---------------------------|---------------------|
| India | Unevaluable | ✅ Bengaluru | **YES 🔒** — India gates domestic acquiring behind local presence | Low — entity clears the gate |
| United States | Unevaluable | ❌ | No | **High** — USD programmes sold, no entity found |
| Mexico / Brazil / Colombia | Unevaluable | ❌ | Verify per market | **Mitigated** — dLocal is a cross-border specialist, which is precisely what it was hired for |

> *"Warning: Great Learning prices programmes in USD and sells into the United States with no confirmed US entity. Those transactions are likely acquired cross-border out of India."*

The LatAm case is the interesting inversion: the company **recognised this exact problem and bought a solution for it** — in three countries.

> **MANUAL:** Fetch the India-geo version of a programme page from an Indian IP. The `intl/` path in the financing logo URLs proves a separate regional configuration exists that was never rendered to this research.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Mexico, Brazil, Colombia | **dLocal** | `[Press Release]` | https://www.businesswire.com/news/home/20230921634934/en/ |
| International (non-India) | **Affirm** — lender-financed | `[Source Code]` `images/template-pp/intl/affirm.jpg` | programme page |
| International (non-India) | **Climb Credit** — lender-financed | `[Source Code]` `intl/climb.png` | programme page |
| International (non-India) | **Splitit** — instalments as auth holds on the learner's existing card, so it settles on card rails | `[Source Code]` `common/splitit.png` | programme page |
| India | Eduvanz, Propelld | `[UNVERIFIED]` — named by complainants only | consumercomplaints.in |
| **Any market** | **Card acquirer / gateway** | **NOT FOUND** | — |

**Negative check:** grep across `terms`, `privacy-policy` and the UT Austin programme page (2.0 MB combined) for `razorpay|payu|ccavenue|cashfree|billdesk|paytm|juspay|hyperswitch|stripe|braintree|paypal|adyen|checkout.com|instamojo|easebuzz|zaakpay|pinelabs|worldline|dlocal|primer|gr4vy|spreedly|payrails|ixopay` returned **zero hits**. The only matches in the entire corpus were `affirm`, `climb` and `splitit`.

These are marketing pages, not checkout pages, so this is a weak negative — but it is consistent with the counsellor-led model in Section 8, where no checkout is served to the public web at all.

**From the Terms, verbatim:**
> "Great Learning does not store any of your credit card information… and **has partnered with payment gateways** for the payment towards the Services. By using a third-party payment provider, you shall abide by the terms of such a payment provider, including any collection/facilitation charges levied by such third-party."

**From the Privacy Policy, verbatim — and payments-relevant:**
> "we do not collect or store sensitive cardholder data, such as full credit card numbers or card authentication data. However, **in the case of scholarships, refunds or referrals, we may collect your bank account, payment gateway or e-wallet account related information.**"

Refunds are collected to a **bank account or e-wallet**, not necessarily returned to the original instrument. That is a manual, out-of-band refund process — and it is a plausible mechanical cause of the refund-delay complaints in Section 5.

#### 3B. Payment Orchestrator

**None detected — direct PSP integrations only.**

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with PSP(s), which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

No orchestrator string in any fetched page. A targeted search connecting Great Learning to Juspay, Hyperswitch, Primer, Gr4vy, Spreedly, Payrails, IXOPAY or Yuno returned nothing — results were generic orchestration-market content with no mention of this merchant.

**Caveat:** no checkout page is publicly reachable, so this is *no public evidence* rather than *proven absent*.

> **MANUAL:** The decisive test. Get a payment link from a counsellor, open it with DevTools, and read the gateway from the network requests. That single action resolves both the PSP identity and the orchestration question.

---

### Section 4: Alternative & Local Payment Methods

**Accepted-methods list, verbatim from the merchant's own programme FAQ:**
> "**What payment methods are available to pay my course fee?** You can pay via bank transfer or credit/debit cards."

That is an enumerated answer, which makes the omissions a genuine sourced absence — **for the international flow only.**

| Market | Method | Category | Status | Source |
|--------|--------|----------|--------|--------|
| International | Credit / debit card | Cards | **Active** | programme FAQ |
| International | Bank transfer / wire | Bank transfer | **Active** | programme FAQ |
| International | Merchant-run instalment plan (admission fee + 3 monthly) | EMI, merchant-collected | **Active**, amounts published | programme page |
| International | Affirm, Climb Credit | Lender-financed | **Active** | logo markup |
| International | Splitit | Card-based instalments | **Active** | logo markup |
| International | Corporate sponsorship | B2B invoicing | Mentioned in docs | programme FAQ |
| **International** | **PayPal, Apple Pay, Google Pay, any wallet** | Wallet | **ABSENT from an enumerated list — sourced** | programme FAQ |
| India | UPI, netbanking, RuPay, Paytm, PhonePe | Local rails | **Not found** — India flow never rendered. **NOT a sourced absence** | — |
| India | Eduvanz, Propelld financing | Lender-financed | `[UNVERIFIED]` — complaints only | consumercomplaints.in |
| LatAm | Local methods, up to 12 instalments | Various | **Active via dLocal** | BusinessWire |

**The published international instalment structure, verbatim:**
> "Option 1 Admission Fees: 800 USD | Installment 1 1000 USD | Installment 2 1000 USD | Installment 3 1150 USD. Option 2 Admission Fees: 1000 USD | … Total Fee Payment 3950 USD"

Four merchant-collected tranches, no lender, no interest, presented **above** the third-party financing options. `emi` appears 35 times and `installment` 13 times in that page's source — financing is central merchandising, not a footnote.

**Critical scoping note:** everything above was observed on a USD-priced page served to a US IP. The `intl/` path segment in the financing logo URLs is direct evidence that Great Learning serves **a different financing set by region**. Forcing `?visitor_country=IN` with an `en-IN` header returned a byte-equivalent response — geo resolution is IP-based. **No INR price was found on any page.** Do not extend the international read to India.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source |
|------------|----------|-----------|------------|--------|
| **Admission fee paid → financing loan declined → refund refused** | consumercomplaints.in | Recurring, ≥2 documented | Nov 2021, May 2024 | page opened, all 11 read |
| Loan originated without consent, refund and cancellation refused | consumercomplaints.in | Isolated | May 2023 | same |
| Cancellation within days, refund refused | consumercomplaints.in | Recurring | Jun 2022, Jan 2023 | same |
| Admission fee non-refund (₹25,000 + GST) | consumercomplaints.in | Recurring | 2021–2023 | same |
| Refund delay, 4% fee deducted, **USD 2,500 chargeback filed** | Trustpilot | Unknown | undated | **403 — `[UNVERIFIED]`** |
| EMI continuing after course discontinued | Trustpilot | Unknown | undated | **403 — `[UNVERIFIED]`** |

**Verbatim, from a page opened directly:**
> "she asked me to pay 25,000 + GST to confirm the scholarship. She also mentioned that the remaining amount will be sanctioned as loan. **But the loan partner Eduvanz rejected my loan due to low salary** and now they are asking me to pay the remaining fees… **they are not willing to give the refund. 29,500 is definitely not a small amount for me.**"

**The mechanism, and it is the designed flow rather than an aberration:**
1. Counsellor quotes the total (₹2,75,000 + GST in documented cases)
2. Learner "qualifies" for a scholarship
3. Learner pays **₹25,000 + GST = ₹29,500** to confirm it — money collected **before** financing is underwritten
4. Balance is to be sanctioned as a third-party NBFC loan
5. **Lender declines**
6. Refund refused; the balance is demanded instead

**The merchant's own page corroborates the structure**: the published plan opens with *"Admission Fees: 800 USD"* against a 3,950 USD total, followed by *"Check out different payment options with third party credit facility providers."* Deposit first, underwriting second.

> *"Pattern: a non-refundable deposit collected on a purchase whose completion depends on a third party's underwriting decision the merchant does not control. That is a structurally guaranteed dispute generator, and at least one documented chargeback has resulted."*

**Honest frequency assessment: moderate in volume, highly concentrated in kind.** Raw counts are small — 11 complaints on consumercomplaints.in, 13 on Voxya (38.46% satisfaction) — against ₹1,039 Cr revenue. But **8 of the 11 are unambiguously about money not coming back**, spanning March 2021 to May 2024. Essentially the entire Indian consumer-complaint footprint is refund disputes, which is unusual for edtech, where content and placement grievances normally dominate. On Trustpilot, by contrast, payment complaints are a thin slice of ~5,000+ reviews.

**Genuine negative finding: no evidence of declined cards, failed transactions or double charges anywhere.** That is consistent with the counsellor-led model — if the sale closes on a call and a payment link, checkout failures do not surface publicly. **The payment pain here is post-transaction, not at the transaction.**

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|------|-------------|----------|--------|
| 1 | FY25 | Revenue ₹1,039 Cr (+4.7% from ₹992 Cr); operating profit tripled to ₹40.23 Cr; marketing spend ₹371.2 Cr | Financials `[UNVERIFIED]` | entrackr.com |
| 2 | Jan 2024 | Reacquired by founder Mohan Lakhamraju from BYJU'S | Ownership `[UNVERIFIED]` | tracxn.com |
| 3 | Feb 2025 | Launched "AI Mentor" and "AI Teacher" | Product `[UNVERIFIED]` | entrackr.com |
| 4 | FY25 | New academic tie-ups: IIT Bombay, Johns Hopkins | Partnerships `[UNVERIFIED]` | indianstartuptimes.com |
| 5 | Jul 2021 | Acquired by BYJU'S, ~USD 600M | Ownership `[UNVERIFIED]` | crunchbase.com |

**No public payment-related RFP found. No payments, finance or revenue-operations hiring found. No funding round in the last 12 months.**

Payment-adjacent read on the financials: 4.7% topline growth with operating profit tripled means FY25 was **margin extraction, not growth**. Marketing at ₹371 Cr is roughly 36% of revenue. Neither is a payments datapoint, but both shape how a cost-per-transaction or recovered-revenue argument lands — this is a company counting costs.

---

### Section 7: Payment-Specific News

| # | Date | Headline | Relevance | Source |
|---|------|----------|-----------|--------|
| 1 | **21 Sep 2023** | **"Great Learning Partners With dLocal Enabling Local Payment Methods and Installments in Mexico, Brazil, and Colombia"** — learners pay in local currency, in up to 12 instalments | **The most important item in this file.** A documented, deliberate local-methods-and-instalments buying decision for a non-home region, executed with a cross-border specialist | https://www.businesswire.com/news/home/20230921634934/en/ |
| 2 | Ongoing | Eduvanz named as India loan partner by two complainants (2021, 2024) | Indian financing rail | consumercomplaints.in `[UNVERIFIED]` |
| 3 | Ongoing | Propelld named as a loan originator in a consent dispute | Indian financing rail | consumercomplaints.in `[UNVERIFIED]` |

**No PSP or gateway partnership announcement was found for APAC, India, or any market outside LatAm.**

---

### Section 8: Checkout Experience Audit

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| **Checkout type** | **None served to the public web** | — | **The sale is counsellor-led.** See evidence below |
| Guest checkout | N/A | — | No checkout exists to be guest or otherwise |
| Payment methods visible | Bank transfer, credit/debit card | — | From FAQ text, not a rendered payment form |
| Instalment / EMI options | Merchant-run 4-tranche plan, plus Affirm/Climb/Splitit | Good | Published to the dollar, international flow |
| Location-based display | IP-based geo; `?visitor_country=IN` does not override it | — | `intl/` asset path proves a regional split exists |
| Multi-currency | USD served to US IP, zero INR strings. Complaints cite ₹2,75,000 | — | Geo-switched pricing is probable but untested |
| 3DS / tokenisation / PCI | **Not observable** | — | No payment form served on any reachable page |
| Mobile responsiveness | Viewport meta correct | Good | — |

**The counsellor-led finding, with its evidence:**
- **Zero payment-gateway references** in 1.08 MB of programme-page source
- **Zero enrolment, checkout, cart or payment hrefs** — "Apply Now" is JS-driven, not a link to a payment surface
- CTAs counted from source: **`download brochure` ×14**, `apply now` ×6
- Their own FAQ omits the fee and says *"Please contact the Program Advisor for details on payment options"*
- Both category fee hubs (`/data-science/courses/fees`, `/artificial-intelligence/courses/fees`) publish **no prices at all** — every row is a "View fee" lead gate
- **Every complainant names a human counsellor** — Ayushi, Ayushi Sethi, Sargam, Raman. Nobody describes a self-serve purchase

> *"The public web property is a lead-generation surface, not a commerce surface. Where money is actually captured — a hosted page, a link sent after the call, a partner-domain portal, or bank transfer — is not publicly observable and could not be determined."*

**Surface fragmentation worth noting:** the site links out to 10+ university-branded enrolment domains — `onlineexeced.mccombs.utexas.edu`, `online.lifelonglearning.jhu.edu`, `gl.fuqua.duke.edu`, `professional-education-gl.mit.edu`, `gl.hms.harvard.edu`, `gl.hsph.harvard.edu`, `gl.chicagobooth.edu`, `gl.mbs-education.com`, plus `olympus.mygreatlearning.com` and `www.greatlearning.ai`. The `gl.` prefix indicates Great Learning operates these as white-label surfaces. **Each is potentially a separate enrolment and payment funnel.** None was fetched — this is a lead, not a finding.

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **No public information found** | — |
| Card data handling | Merchant disclaims storing card data | mygreatlearning.com/terms, /privacy-policy |
| Recommended Yuno integration | Not determinable without seeing the capture surface | — |

> "Great Learning does not store any of your credit card information… we do not collect or store sensitive cardholder data, such as full credit card numbers or card authentication data."

> `[INFERENCE, not confirmed]: the disclaimer is consistent with a hosted or redirect checkout operated by a third-party gateway, which would keep PCI scope reduced. No attestation, level or AOC exists publicly.`

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: They solved this once, for three countries, and stopped**
> **Evidence:** §7 — dLocal partnership (Sep 2023) for local methods and 12-month instalments in Mexico, Brazil and Colombia. §3A — no PSP or gateway identifiable for India, the US or anywhere else, and no equivalent partnership announced for any other region.
> **Pain Point:** The category is understood internally; someone already ran this evaluation and signed. But the solution is scoped to one region and one vendor, which means every other market either runs on whatever the home stack provides or gets nothing.
> **Yuno Value Proposition:** One layer covering every market rather than a point solution per region, without unpicking what already works in LatAm.
> **Best Success Case:** Open English — edtech, subscriptions, 30+ countries. Tier 1 vertical match.
> **Outreach Angle:** You added local methods and 12-month instalments for Mexico, Brazil and Colombia in 2023. I couldn't find the equivalent anywhere else.
> **Suggested Subject Line:** Local methods in three countries
>
> **Insight #2: A deposit collected before the underwriting decision**
> **Evidence:** §5 — documented complaints 2021–2024 where an admission fee was paid, the financing partner declined, and the refund was refused. §4 — the merchant's own published plan opens with "Admission Fees: 800 USD" ahead of "third party credit facility providers."
> **Pain Point:** Money is taken on a purchase whose completion depends on a third party's credit decision the merchant does not control, and the deposit is treated as non-refundable when the answer is no. That generates disputes structurally, and at least one chargeback is documented.
> **Yuno Value Proposition:** Routing and retry across providers lifts the approval side; unified visibility of failed and disputed transactions replaces a manual, out-of-band refund process that per §3A collects bank or e-wallet details rather than returning to the original instrument.
> **Best Success Case:** Livelo — failed-transaction recovery. Tier 2 pattern, LATAM, label it.
> **Outreach Angle:** Your instalment plans start with an admission fee, and the financing decision comes after it. That ordering shows up in your complaint record.
> **Suggested Subject Line:** Deposit first, underwriting second
> **Caution:** sharp, and it names their own dispute record. Phase 2 at the earliest, with the diplomatic clause.
>
> **Insight #3: No checkout, ten enrolment surfaces**
> **Evidence:** §8 — no payment gateway, no checkout href and 14 brochure CTAs across 1.08 MB of source; every complainant names a human counsellor. §8 — 10+ university-branded enrolment domains operated as white-label surfaces.
> **Pain Point:** A counsellor-originated, payment-link model spread across ten-plus branded surfaces in India, the US and Europe has no single place where approval rates, retries or reconciliation can be seen.
> **Yuno Value Proposition:** One layer behind every surface, so the payment experience stops being per-domain.
> **Best Success Case:** Rappi — provider breadth added without per-integration delay. Tier 2, label it.
> **Outreach Angle:** You run enrolment on ten-plus university-branded domains. I was curious whether payments behind them are one stack or ten.
> **Suggested Subject Line:** Ten enrolment domains

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks:**
1. You added local payment methods and 12-month instalments for Mexico, Brazil and Colombia in 2023, and I couldn't find the equivalent for any other market.
2. Your published instalment plan starts with an admission fee, and the third-party financing decision comes after it.
3. Your programme FAQ says learners can pay by bank transfer or credit and debit card. That's the whole list.

**Cold call openers:**
1. You went to a cross-border specialist for LatAm payments three years ago. What made that region the one worth solving?
2. Your enrolment runs across ten-plus university-branded domains. Is payments one stack behind all of them, or one per partner?
3. When a learner pays the admission fee and the financing partner then declines, what happens to that money today?

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ | Overlap | Known PSP/Orchestrator | Source |
|---------|---------|----|---------|------------------------|--------|
| upGrad | upgrad.com | Mumbai | High — same programmes, same price points | **Not found** — fetch geo-redirected to US variant, inconclusive | inc42.com |
| **Simplilearn** | simplilearn.com | Bengaluru (Blackstone-owned) | High | **Liquiloans + Propelld + ShopSe — CONFIRMED from live page config.** No card PSP found | grep, §11 raw evidence |
| Scaler | scaler.com | Bengaluru | Medium | **Not found** — apparent Razorpay/Stripe hits are false positives | grep |
| Emeritus | emeritus.org | Mumbai / Singapore | High — university-partner model | Not found | jaroeducation.com |
| Coursera (India) | coursera.org | US | Medium | Not found | riseupp.com |
| Jaro Education · Imarticus | jaroeducation.com · imarticus.org | Mumbai | Medium | Not found | — |

> ⚠️ **False-positive warning, recorded so it is not rediscovered.** Scaler's page returns 8 `Razorpay` hits and 1 `Stripe` hit. **All nine are worthless:** `"after_role":"Associate Analyst, Razorpay"` and `"Ex-Razorpay, Ex-Samsung"` are alumni-placement and instructor-bio strings; `"Spring Boot, JPA, OAuth2, Stripe payments, Redis"` is a course syllabus. Edtech sites are full of employer names and technology curricula, which makes mechanical grepping unusually dangerous in this vertical.

#### 11B. Industry Peers

| Company | Why Similar (Payment Context) | Source |
|---------|-------------------------------|--------|
| upGrad, Emeritus | High-ticket, university-partnered, multi-country, counsellor-led | inc42.com |
| Propelld, Eduvanz, GrayQuest, Liquiloans | Not competitors — the **financing layer** the whole vertical routes through | yourstory.com, kenresearch.com |

#### 11C. Companies Recently Adopting Payment Orchestration

*"No public case studies found of direct competitors adopting payment orchestration."*

No Juspay, Hyperswitch, Primer, Gr4vy, Spreedly or Yuno signature at upGrad, Simplilearn, Scaler, Emeritus or Coursera India. Juspay names no edtech customer publicly.

**The structural finding instead — and it may matter more.** Simplilearn's live programme page carries a working **Liquiloans** EMI API config, a **Propelld** application-form integration and a **ShopSe** EMI feature flag, with **zero card-PSP signatures on the same page**. Across the vertical the dominant model is that the edtech pays the interest so the learner sees "no-cost EMI": Propelld runs its own NBFC across 2,000+ institutions, GrayQuest raised ₹80 Cr for an education *payments* platform, and Ken Research counts 25+ players in Indian edu-financing.

**For high-ticket Indian upskilling, a material share of fee value is originated as an NBFC loan rather than collected on a checkout.** Any sizing that assumes gross programme revenue flows through a PSP will be overstated. **No public figure quantifies the financed-versus-direct split** — that is the number that would size this vertical properly, and it does not exist publicly.

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Score | Top Signal | In TAL? |
|------|---------|------|-------|------------|---------|
| 1 | upGrad | Direct competitor | Not scored | Largest unresearched stack in Indian edtech; markets "no-cost EMI" without naming a lender | To check |
| 2 | Simplilearn | Direct competitor | Not scored | Three financing rails confirmed, no card PSP found | To check |
| 3 | Emeritus | Direct competitor | Not scored | University-partner model, India/SEA/US/LatAm | To check |
| 4 | Scaler | Direct competitor | Not scored | Stack genuinely unknown | To check |

Scores deliberately blank — none was researched to this report's standard, and a guessed score is worse than none.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue | **₹1,039 Cr FY25** (≈US$120M), up 4.7% from ₹992 Cr FY24 | entrackr.com `[UNVERIFIED]` |
| Operating profit | ₹40.23 Cr FY25, tripled from ₹13.82 Cr | entrackr.com `[UNVERIFIED]` |
| Marketing spend | ₹371.2 Cr — ~36% of revenue, largest line item | entrackr.com `[UNVERIFIED]` |
| Learners | 13.8M claimed across 170+ countries; 1,750 programmes | Tracxn `[UNVERIFIED]` |
| Average ticket | **USD 3,950** (UT Austin AI/ML); **₹2,75,000 + GST** on Indian equivalents per complaints | programme page, fetched; complaints |
| Admission fee | USD 800–1,000 international; **₹25,000 + GST (₹29,500)** India | programme page; complaints |
| Est. annual transactions | **Not calculable** — no reliable learner-to-paying-enrolment ratio | — |
| Primary currency | USD internationally, INR in India. No INR price observed on any page | fetched |
| **Financed vs direct split** | **NOT PUBLIC — the decisive unknown** | — |

**Sizing note:** ₹1,039 Cr is the revenue anchor, but the orchestrable share depends entirely on how much is collected on a checkout versus originated as an NBFC loan. That number is not public for Great Learning or for the vertical.

---

### Overall Research Confidence

**Medium.**

**Strong coverage:** payment methods, instalment structure and financing facilitators on the international flow are sourced from the merchant's own fetched pages, including an enumerated accepted-methods answer that produces a genuine sourced absence. The complaint analysis rests on a page opened directly with all 11 entries read. The dLocal partnership is a first-party press release. The counsellor-led sales model is evidenced from page source rather than inferred.

**Weak coverage:** **no traffic data at all**, which removes the country profile and makes three ICP signals unevaluable. **No card acquirer or gateway identified in any market.** No PCI posture. No checkout reachable. The India flow was never rendered — every method finding is scoped to a US-served page, and the `intl/` asset path proves a separate Indian configuration exists that was not observed. Ownership and financials rest on aggregator summaries not read at source. The most commercially interesting complaint material (a USD 2,500 chargeback, a 4% refund fee) is Trustpilot-sourced and 403-blocked.

**Traffic data was neither supplied, API-sourced nor estimated — it does not exist in this file.** The supplied pull measured a redirect stub and was rejected.

---

### Manual Research Recommendations

> **Area:** Traffic profile (§1)
> **Why it matters:** Three ICP signals are unevaluable without it, and the score would plausibly move 5–8 points.
> **Suggested manual action:** Re-pull SimilarWeb against `www.mygreatlearning.com` with "Include all country domains" ON.

> **Area:** PSP identity and the orchestration question (§3)
> **Why it matters:** The single largest gap. No gateway is identifiable for any market, and the greenfield classification rests on absence of public evidence.
> **Suggested manual action:** Request a payment link from a Program Advisor, open it with DevTools, read the gateway from the network requests. One call resolves both questions.

> **Area:** The India payment flow (§4)
> **Why it matters:** Every method finding is scoped to a US-served page. The `intl/` asset path proves a separate Indian configuration exists.
> **Suggested manual action:** Open a programme page from an Indian IP and record the price, currency, financing partners and methods offered.

> **Area:** Financed-versus-direct split (§12)
> **Why it matters:** Determines how much volume orchestration could actually touch. Not public for this merchant or the vertical.
> **Suggested manual action:** Ask on the first call, framed as scoping: *"what share of programme fees comes in through your own checkout versus a financing partner?"*

> **Area:** Ownership (§2)
> **Why it matters:** A founder buyback from Byju's in Jan 2024 would mean a new decision-maker and a different budget posture. Currently unverified.
> **Suggested manual action:** Confirm via MCA filings or a dated primary news source before writing.

---

### Appendix: All Source URLs

**Company primary sources (fetched)**
- https://www.mygreatlearning.com/terms
- https://www.mygreatlearning.com/privacy-policy
- https://www.mygreatlearning.com/pg-program-online-artificial-intelligence-machine-learning
- https://www.mygreatlearning.com/data-science/courses/fees · https://www.mygreatlearning.com/artificial-intelligence/courses/fees
- https://www.mygreatlearning.com/grievance-redressal *(not opened — lead)*

**Payments**
- https://www.businesswire.com/news/home/20230921634934/en/Great-Learning-Partners-With-dLocal-Enabling-Local-Payment-Methods-and-Installments-in-Mexico-Brazil-and-Colombia

**Complaints**
- https://www.consumercomplaints.in/bycompany/great-learning-a589649.html *(opened, all 11 read)*
- https://voxya.com/company/great-learning-complaints/1229587 *(aggregate only, bodies JS-gated)*
- https://www.trustpilot.com/review/www.mygreatlearning.com *(403 — unread)*
- https://www.pissedconsumer.com/great-learning/RT-F.html *(unread)*

**Corporate & financials**
- https://entrackr.com/news/great-learnings-scale-goes-past-rs-1039-cr-in-fy25-10612710
- https://tracxn.com/d/companies/great-learning/__1CkAbCPeFWWQ5p4tnBmDexvLereSClzJvTon_s8NvAM
- https://www.crunchbase.com/organization/great-learning-great-lakes-e-learning

**Vertical financing**
- https://yourstory.com/2021/03/india-education-finance-startups-affordable-learning-students
- https://yourstory.com/2024/05/propellds-nbfc-edgro-secures-25m-debt-funding-student-loans-edtech
- https://www.kenresearch.com/industry-reports/india-edufin-industry

</details>
