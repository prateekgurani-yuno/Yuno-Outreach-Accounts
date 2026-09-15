---
name: full-outreach
description: Generate the complete 12-touch outreach sequence for an APAC prospect — 5 auto-written emails + 4 LinkedIn messages + 3 manual placeholders across 23 days. Direct voice, observation-led, no pain projection. Escalates curiosity → hypothesis → proof → close. Composes into the existing 2-ready-to-outreach/{name}.md file's Section 2.
argument-hint: <company-name> [| optional context] [| past interactions]
allowed-tools: Read, Edit, Glob, Bash, WebSearch, WebFetch
---

# /full-outreach

Generate the full 12-touch sequence: 5 auto-written emails + 4 LinkedIn messages + 3 manual
placeholders across 23 days.

Phases:
- **Phase 1 — Curiosity (Days 1–5):** observations only, no projected pain, no meeting
  ask. E1 lands observations + soft CTA. E2 walks through the Yuno mechanism mapped to the
  sharpest E1 observation + opt-out. LK1 echoes the strongest observation.
- **Phase 2 — Diagnosis (Days 7–9):** assertions about likely pain, direct meeting request.
- **Phase 3 — Proof (Days 11–17):** matched success case with quantified results (E4), two
  manual creative touches (E5, E6), hard LK ask (LK3).
- **Between phases (Day 19):** E7 manual creative bridge.
- **Phase 4 — Breakup (Days 21–23):** final hard LK ask (LK4), soft break-up email (E8).

Voice is direct, peer-level, humble. First-person ("I work at Yuno"), conversational, never
sales-y. Yuno is always additive, never replacement.

---

## Identity

- **Name:** Prateek Gurani
- **Company:** Yuno
- **Territory:** APAC
- **Email:** prateek.gurani@y.uno
- **Booking link:** none. Prateek does not use one.

> **No booking link exists, by decision.** Every CTA in this sequence is a plain time
> proposal — *"would Tuesday 3pm work?"* — and the reply itself is the booking mechanism.
> Never insert a calendar URL, a Calendly-style link, or a "grab a slot here" line anywhere
> in the sequence. This makes the proposed times load-bearing: they must be specific,
> plausible in the prospect's local zone, and varied across the sequence.

---

## Inputs

`$ARGUMENTS` split on `|`:
- **Segment 1 (required):** Company name.
- **Segment 2 (optional):** Brief context — *"met at Seamless Asia"*, *"warm intro from X"*.
- **Segment 3 (optional):** Past interaction history (Salesforce activity, meeting notes,
  prior threads). Free-form.

If Segment 2 reads as detailed past-interaction data, treat it as Segment 3.
If no company name is provided, stop and ask Prateek.

---

## Step 0 — Parse arguments and detect day

Auto-detect today's date. Calculate CTA day suggestions for the five meeting-request touches
(E3, LK2, E4, LK3, LK4). With no booking link, these proposed times are the entire CTA —
a vague ask has nothing to fall back on:

- Propose meeting times **2–3 business days after the next business day**. Skip weekends.
- **Time zones matter in this territory.** Prateek sits in IST. A prospect in Japan, Korea or
  ANZ has a narrow overlap window — propose slots that work for the prospect's local
  business hours, not Prateek's convenience. For ANZ, morning IST is afternoon local; for
  Japan/Korea, late morning IST is mid-afternoon local; for SEA, most of the day overlaps.
  State times in the prospect's local time zone.
- Default slots: morning (10 or 11 AM) or afternoon (3 or 4 PM) prospect-local. Vary across
  the sequence — five distinct day/time combos.
- **Check the market's working week.** Most of APAC runs Mon–Fri; do not propose a slot that
  lands on a local public holiday if research surfaced one.

**Contact name:** use the `{{recipient.first_name}}` placeholder throughout. Never guess.

---

## Step 1 — Load research file

This skill READS, MODIFIES, WRITES — it does not create a new file. The sequence composes
INTO the existing file's Section 2 collapsible.

Normalize the company name using the same rules as `/research`, then read
`2-ready-to-outreach/{normalized-name}.md`. If the exact filename isn't found, Glob
`*{normalized-name}*` in that folder. Multiple matches: list them and ask.
No file: stop and tell Prateek to run `/research [Company]` first.

**Verify structure:** the file must contain a Section 2 `<details>` block with the
placeholder text. If the placeholder is already replaced, stop and ask before overwriting.

**Read the ICP breakdown and the Motion line in the header.** The motion determines the
entire angle — see Step 6a.

---

## Step 2 — Load voice anchor

Read `.claude/reference/email-samples.md`.

**Precedence — Prateek's standing instruction:** *"Use mix of both, Yamin's rulebook overrule
mine."* The samples supply the voice; **this skill wins on conflict.** The already-resolved
conflicts are tabled in the samples file — opening pleasantries, em dashes as separators,
vague CTAs, asserting pain as fact, implied additive framing, and mid-email customer lists
all lose to the rulebook. Do not re-litigate them per prospect.

Where this skill is **silent**, the samples govern. Carry these habits into every draft:

- **Ground observations in the prospect's own documents** — their Terms, annual results,
  help centre — and quote the phrase. Stronger than any third-party source, and the most
  repeatable move in the sample set.
- **Name an asymmetry inside the prospect's own stack** where one exists. Contrasting two of
  their systems against each other beats an external benchmark: they cannot dispute either
  half. (Sample 1: operator rails retry until the balance tops up, the card book gets one
  attempt and calls it churn.)
- **One embedded discovery question**, in E3 or E4 only — something easy to answer that is
  not yes/no to a meeting. Never in Phase 1, which stays observational.
- **A diplomatic clause** when an observation stings: *"not because anyone's doing it badly."*
- **Multi-threading in the sign-off:** *"If [area] sits elsewhere, happy to be pointed there."*

**Length calibration.** The samples are long-form single emails, not sequence touches.
Sample 1's density belongs in **E3 and E4**, where assertion and proof are allowed. Phase 1
stays short: 2–3 factual bullets, no imported density. If a sample and a touch's word budget
disagree, the word budget wins.

**Coverage gaps in the sample set** — flag these to Prateek rather than inventing a voice:
no short-form first touch under 150 words, and no LinkedIn sample at all, so LK1–LK4 are
drafted from the rulebook templates alone.

---

## Step 3 — Subscription fork

If the research indicates subscription, recurring revenue, SaaS or membership, read
`.claude/reference/subscription-payments.md`.

**First, check §4 of that file — the app-store trap.** If the research shows revenue is
dominated by Apple/Google IAP, stop and flag to Prateek before drafting. Orchestration
cannot touch that revenue and the sequence will not survive a reply.

Apply subscription data in:
- **Phase 2 (E3):** involuntary churn, first-renewal drop-off, retry and network token
  coverage, and — for India-heavy prospects — e-mandate and UPI Autopay handling
- **Phase 3 (E4):** subscription-vertical success case; benchmarks inside bullets

**Do not** force subscription pain into Phase 1 — that is hypothesis-grade, and Phase 1 is
observation-only.

---

## Step 4 — Past interaction parsing (if Segment 3 provided)

Extract: people, timeline, topics and pains already surfaced, deal status, sentiment, open
commitments, objections raised.

**Application:**
- **E1 hook:** replace the cold opener with a relationship reference if a real touchpoint
  exists.
- **Pain vector selection:** prioritize pains they already told us about.
- **CTA calibration:** warm with no objections → propose times from Phase 1. Cold or
  stalled → soft through Phase 1, time proposals Phase 2+. Timing objection → drop the
  meeting push entirely, reframe as low-pressure catch-up, and end Phase 4 with an explicit
  *"happy to circle back in [their stated timeframe]"*.
- **E4 success case:** match against any competitor or pain area they named.

**Do not** use past interaction data if it's stale enough to feel like padding, references a
fallen-through deal in a way that creates pressure, or would make the email awkward.

---

## Step 5 — Pain Vector Extraction (MANDATORY · output before drafting)

```
=== PAIN VECTOR EXTRACTION ===

Motion: [Greenfield / Displacement / In-house / Competitive]  ← from the research header

Observable setup facts (from research, with sources):
- [Fact 1] — source: [where]
- [Fact 2] — source: [where]
- ...

Selected observations for Phase 1 (E1 bullets, ranked by materiality):
1. [Setup signal] → [observation phrasing for E1]
2. [Setup signal] → [observation phrasing for E1]
3. [Setup signal] → [observation phrasing for E1]
   (Flex 2–3 based on research strength. Never pad to 3.)

Bridge variant: [A — complexity / B — limitations / C — friction / SKIP]
Rationale: [why this variant fits this specific setup]

Hypothesis for Phase 2 (E3):
Most likely pain based on observations: [one sentence]
Backing logic: [why these observations point to this pain at this prospect's volume /
vertical / stage / market mix]

Success case for Phase 3 (E4):
Selected case: [Customer name]
Tier: [1 = exact industry match / 2 = same payment pattern / 3 = credibility default]
Match rationale: [why this case fits]
Numbers to lead with: [3 results from the case]
Optional benchmark: [verified benchmark with source — or SKIP]

Touch-by-touch angles:
- E2 angle: [sharpest E1 observation] → [specific Yuno mechanism, per the E2 mapping table]
- LK1 angle: [single sharpest observation from E1 set]
- LK2 angle: [pointed one-sentence version of the Phase 2 hypothesis]
- LK3 angle: [one-line proof point from E4]
- LK4 angle: [final stripped-down hook]
- E8 angle: [optional final observation, OR clean exit]
```

**Materiality test:** how much operational or revenue pain does this signal create for *this
specific* prospect, given their volume, geography, vertical and stage? A missing rail matters
most when it dominates the prospect's #1 market. A single-PSP dependency matters more at
scale. Never default to "APMs and cross-border" for everyone.

---

## Step 6 — Signal → observation → hypothesis grid

| Setup signal | Phase 1 observation phrasing | Phase 2 hypothesis angle |
|---|---|---|
| Single PSP dependency | *"Your checkout shows [PSP] across all [N] markets — single processor, no fallback visible."* | "If [PSP] degrades during a peak window, the whole flow is exposed. Rate leverage on one processor is structurally weaker too." |
| Multiple PSPs in parallel | *"You're running [PSP A] in [market] and [PSP B] in [market] — two parallel stacks."* | "Reconciliation across two ledgers eats finance ops time; routing logic spread across teams creates blind spots." |
| No entity in a top market | *"Your top 3 markets include [country], but there's no entity there."* | "Locally-issued cards acquired cross-border tend to see materially lower approval rates than local acquiring, plus FX on top." |
| Regulatory acquiring gate | *"You're live in [country], where domestic acquiring effectively needs local presence or a licensed partner."* | "That usually means the local rail is either unavailable or routed through a workaround — both cap what the market can convert." |
| Missing dominant local rail | *"You're live in [country] but [rail] isn't on the checkout."* | "[Rail] carries a large share of online payments in [country] — card-only checkouts there tend to leak at the cart." |
| Missing instalments in a high-ticket market | *"Your [India/Japan/Taiwan] checkout is full-ticket only — no EMI or instalment option visible."* | "High-ticket categories in that market convert heavily on instalments; full-ticket-only checkouts tend to lose the mid-funnel." |
| Recurring on cards in India | *"You're billing recurring on cards for Indian subscribers."* | "Indian recurring sits under the RBI e-mandate rules — mandate registration, AFA, pre-debit notification. Retry logic built for other markets usually doesn't survive it, and UPI Autopay is the local rail." |
| Diaspora / outbound cross-border | *"Your traffic is [X]% outside [home market] — US, UK, Gulf and Australia — but the stack looks built for [home market]."* | "Billing a diaspora audience from a home-market stack means every renewal is a cross-border auth against a foreign issuer." |
| New market expansion signal | *"Your careers page lists [N] roles in [city], including [role]."* | "Standing up local acquiring per market is integration overhead; orchestration cuts that to one stack." |
| Licence application | *"You applied for [licence] in [market] in [timeframe]."* | "Licence work usually creates parallel payment integration projects unless an orchestration layer absorbs them." |
| Regional orchestrator incumbent | *"You're already running an orchestration layer across [markets]."* | "The question stops being whether to orchestrate and becomes reach — global PSP and rail coverage as [Company] moves outside [home region]." |
| In-house orchestration layer | *"You've built the routing layer in-house across [N] providers."* | "In-house works until the provider count and market count grow faster than the team. The cost shows up as engineering time, not as a line item." |
| High-risk vertical | *"You're operating in [vertical] with [acquirer set] across [markets]."* | "MCC-driven auth drag and chargeback exposure usually push high-risk operators toward acquirer diversification." |
| Review / app-store friction | *"Your Play Store reviews from [country] flag payment failures — [N] of the last 50 mentions."* | "Reviews citing failures are usually the visible edge of an auth-rate problem or a missing local rail." |

### 6a. Motion overrides — read before drafting

The research header carries a **Motion**. It changes what Phase 1 may claim:

- **Greenfield** (no orchestrator): the standard sequence. Observations can note the absence
  of a routing layer.
- **Displacement** (regional orchestrator such as Juspay confirmed): **never open with "you
  have no orchestration."** It is factually wrong and burns the thread. Open on coverage and
  reach — global PSP and rail breadth outside the home region, multi-region routing,
  international expansion the incumbent wasn't built for. Still never name the incumbent.
- **In-house**: the merchant made a deliberate build decision. Respect it. Anchor on
  opportunity cost and reach, not on the build being wrong.
- **Competitive** (a global orchestrator is incumbent): hardest. Only proceed if research
  surfaced a concrete gap. Otherwise flag to Prateek rather than sending a weak sequence.

### 6b. Cross-border framing in APAC

Unlike EMEA, there is **no regional interchange cap regime** — no APAC equivalent of the
IFR. Cross-border framing is available across the territory, but it must be argued per
corridor, not per region:

- **Name the corridor**, never "APAC cross-border." *"Cards issued in India processed
  against your Singapore entity"* is a claim; *"cross-border in APAC"* is noise.
- **Lead with approval rate, not fee.** Domestic issuers in India, Indonesia, Japan and
  Korea decline foreign-acquired transactions at higher rates than local-acquired ones.
  Cite a source or keep it qualitative — never invent a percentage.
- **FX is the second line** where local-currency pricing exists.
- **Regulatory gating is the strongest line** where it applies: "the local rail is not
  reachable at all without local presence" beats any fee argument.
- **ANZ is the exception** — those stacks look most like EMEA/US, so the routing, failover
  and cost-of-acceptance framing lands most directly there.

Any specific regulatory claim must be verified live at research time. See
`.claude/reference/apac-payments.md`.

---

## Step 7 — APAC rail reference

Full detail in `.claude/reference/apac-payments.md` §2. Condensed for drafting:

| Market | Expected rails | Typical gap on a global-only stack |
|---|---|---|
| India | UPI, cards/RuPay, netbanking, EMI, UPI Autopay | UPI, EMI, UPI Autopay for recurring |
| Indonesia | QRIS, virtual account, GoPay/OVO/DANA, OTC cash | QRIS and virtual account almost always |
| Malaysia | FPX, DuitNow, Touch 'n Go, Boost | FPX |
| Thailand | PromptPay, TrueMoney, instalments | PromptPay |
| Vietnam | MoMo, ZaloPay, VNPay/VietQR, NAPAS, COD | Most of them |
| Philippines | GCash, Maya, InstaPay, OTC cash | GCash |
| Singapore | PayNow, GrabPay, cards | PayNow |
| Japan | konbini, PayPay, LINE Pay, Rakuten Pay, Paidy, instalments | konbini and PayPay |
| South Korea | KakaoPay, Naver Pay, Toss, local card PG | Usually all — entity-gated |
| China | Alipay, WeChat Pay, UnionPay | Requires licensed local path |
| Hong Kong | FPS, Octopus, AlipayHK | FPS |
| Taiwan | JKOPay, LINE Pay, ATM transfer, store cash, instalments | Most |
| Australia | PayTo, BPAY, Afterpay, Zip | PayTo, BPAY |
| New Zealand | Cards, POLi (verify availability), Afterpay | Local A2A |
| Pakistan/Bangladesh | JazzCash, Easypaisa / bKash, Nagad, COD | Almost universally |

---

## Step 8 — Draft the 12 touches

Draft all auto-written touches in sequence. For the three manual touches, output placeholder
markers only.

### Phase 1 — Curiosity (Days 1–5)

Goal: get a reply, not a meeting. No projected pain. No meeting ask.

#### Touch 1 — Email 1 · Day 1

~85–110 words.

1. Greeting: *"Hey {{recipient.first_name}},"*
2. Opener: *"Spent some time looking at [Company]'s payment setup. A few things stood out:"*
   (or a relationship hook if past interaction exists)
3. **2–3 short factual bullets** (flex; never pad to 3)
4. **Transition line** (variant per Step 9):
   - A: *"That kind of setup usually comes with some complexity."*
   - B: *"At your stage, that kind of setup usually comes with some limitations."*
   - C: *"That kind of setup usually has some friction worth checking on."*
5. **Yuno line:** *"I work at Yuno — top-100 fintech, a16z-backed. We consider ourselves the
   'everything payments' platform: one integration, every PSP, every method, every market."*
6. **Soft meta-CTA:** *"Rather than pitch you based on assumptions, is there anything
   payment-related you're working through that we might be able to help with?"*
7. Sign-off: *"Best, Prateek"*

**Subject:** ≤6 words, describing the strongest observation, no question marks. Examples:
*"UPI gap on your IN checkout"*, *"Single acquirer across 9 markets"*, *"No konbini on your JP flow"*.

**Hard:** no meeting ask, no opt-out line (that's E2).

#### Touch 2 — Email 2 · Day 3 · REPLY IN THREAD

~110–140 words. No new subject.

1. Greeting
2. **Framing:** *"Following up — wanted to put a bit more behind what Yuno actually does, and
   how it would address what I flagged."*
3. **Yuno mechanism (3–4 short factual lines, not promotional):**
   - Sits above existing PSPs — additive, no rip-out
   - Routes per BIN, market and method to whichever rail performs best
   - Automatic failover when a PSP degrades
   - One integration to add new PSPs, rails, acquirers or methods
4. **Map to the sharpest E1 observation (1–2 lines).**
5. **Cadence + opt-out:** *"I'll keep sharing what I'm seeing every few days. If your stack's
   where you want it, just say the word and I'll back off — otherwise happy to go deeper."*
6. Sign-off (vary from E1)

**Mapping reference — pick the one mechanism that fits the sharpest E1 observation:**

| E1 observation type | Yuno mechanism to surface in E2 |
|---|---|
| Single PSP across markets | Smart routing across multiple acquirers + automatic failover |
| Multi-PSP fragmentation | Unified reconciliation + single routing logic layer |
| Missing local rail | One integration to add any method, no per-rail rebuild |
| No entity / regulatory gate in a top market | Routing to local acquirers per geography |
| New market expansion | One integration covers market entry — no per-country PSP build |
| Recurring / subscription | Retry logic, network tokens, account updater in the routing layer |
| Recurring in India | Local mandate rails alongside cards, handled in one integration |
| Regional orchestrator incumbent | Global PSP and rail coverage beyond the home region |
| Review-visible failures | Routing + retry logic typically lifts approval in flagged markets |

Lead with **one** mechanism. E2 stays surgical.

**Never:** auth-rate numbers or revenue claims in E2 (those belong in E4 with sources);
claims without mechanism; a meeting ask; repeating E1's Yuno identity line verbatim;
filler like *"circling back"*.

#### Touch 3 — LinkedIn message 1 · Day 5

~40–60 words.

> *Hey {{recipient.first_name}} — figured I'd flag this here too in case more useful than
> email. Quick one: [single sharpest observation from the E1 set]. Curious if that maps to
> anything you're working through on the payments side.*

**Hard:** no meeting ask.

---

### Phase 2 — Diagnosis (Days 7–9)

Shift from curiosity to assertion. Use *"my read is"*, *"I'd bet"*, *"what I see at
companies with similar setups"*.

#### Touch 4 — Email 3 · Day 7 · NEW EMAIL

~90–120 words.

1. **Subject:** shifts toward the hypothesis — *"Quick read on your India exposure"*,
   *"Single-PSP risk at your scale"*
2. Greeting
3. **Open with the hypothesis, no apology for silence:** *"Going to take a swing at this —
   based on what I see, my read is [hypothesis in one sentence]."*
4. **2–3 lines of backing logic** anchored to E1/E2 observations
5. **Yuno re-state (different framing than E1):** *"At Yuno (a16z-backed, top-100 fintech),
   we sit above your existing PSPs so you can [benefit relevant to the hypothesis] — keep
   your stack, add what's missing."*
6. **Meeting-request CTA:** *"[Day] is open for me — would [time] or [time] work for a quick
   15 minutes?"* Times in the prospect's local zone, named as such (*"3pm your time"*). No
   link — the reply is the booking.
7. Sign-off

**Additive framing required from here on:** *"keep your stack, add what's missing."*

#### Touch 5 — LinkedIn message 2 · Day 9

~50–70 words.

> *Hey {{recipient.first_name}} — sent a longer note over email this week. Short version:
> [pointed pain hypothesis in one sentence]. If that's anywhere on your radar, would [day]
> or [day] at [time] your time work for a quick 15?*

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · NEW EMAIL

~130–160 words.

1. **New subject** referencing the case: *"How [Customer] solved this"*
2. Greeting
3. **Bridge from hypothesis:** *"On the read I shared last week — sharing a quick example of
   what solved looks like."*
4. **[Optional] verified industry benchmark**, one line with source. Skip if unsourced.
   **Two numbers need attribution, not repetition.** The **"~8% average authorisation uplift"
   from smart routing traces to Yuno's own blog** — it is our marketing, not independent
   evidence, so attribute it as Yuno's own figure and never present it as a third-party
   benchmark. **IATA / Edgar, Dunn & Company's "$20.3bn annual airline cost of payment
   acceptance, 2.1% of industry revenue"** would be an excellent airline hook, but it has
   only been seen via a vendor blog citing the study — trace it to the IATA/EDC primary
   source before quoting it.
5. **Setup of the matched case:** *"[Customer], a [comparable descriptor], partnered with
   Yuno to [solve a problem matching the Phase 2 hypothesis]. The results came fast:"*
6. **3 bullets with quantified results**, one carrying a parenthetical aside —
   *"(pretty solid, right?)"* / *"(not too bad, right?)"* / *"(you read that right)"*
7. **Additive framing:** *"Same orchestration layer above their existing stack — no rip-out."*
8. **Meeting-request CTA** (different day/time from E3 and LK2, prospect-local, no link)
9. **Case study link:** *"Full case here if useful: [URL]"*
10. Sign-off (different from E3)

**Success case selection:** Tier 1 = exact industry + comparable footprint · Tier 2 = same
payment pattern regardless of industry · Tier 3 = credibility defaults. If Tier 1 isn't
available, flag the tier and rationale in the Extraction block.

**APAC caveat — read this.** The verified case library (Step 10) is LATAM-weighted. For an
APAC prospect a Tier 1 match will often not exist. Before defaulting, WebSearch
`site:y.uno success case [industry keywords]` and `site:y.uno newsroom [APAC market or
vertical]` for anything newer. **Do not APAC-ify a LATAM case** — if inDrive's results came
from LATAM markets, say inDrive and say what it did; never imply the numbers came from Asia.
Tier 2 framing ("same payment pattern, different region") is honest and works.

#### Touch 7 — Email 5 · Day 13 · MANUAL
Placeholder only. Prospect-specific business case, checkout teardown, Loom walkthrough,
annotated screenshot, market data pull, mutual contact angle.

#### Touch 8 — Email 6 · Day 15 · MANUAL
Placeholder only. Different format from E5.

#### Touch 9 — LinkedIn message 3 · Day 17

~40–60 words. Hard meeting ask, proof-anchored.

> *Hey {{recipient.first_name}} — [Customer from E4] [one-line result]. Worth 15 minutes to
> see if it maps to your setup? [day] at [time] your time is open.*

---

### Between Phases (Day 19)

#### Touch 10 — Email 7 · Day 19 · MANUAL
Placeholder only. Manual creative bridge — anchor to something fresh: recent news, funding,
a hire, a market entry, a shared event, a mutual contact.

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21

~30–50 words. Stripped down — just the ask.

> *Hey {{recipient.first_name}} — last LK ping from me on this. If timing works, [day] at
> [time] your time is open for a quick 15.*

**Differentiation from LK3:** LK3 leads with proof; LK4 doesn't. Don't repeat the case study
line. If LK4 needs more, surface one fresh unused angle from research.

#### Touch 12 — Email 8 · Day 23 · REPLY IN THREAD to E3 or E4

~40–70 words. Break-up. Polite, no pressure, door open.

1. Reply in thread, no new subject
2. *"Going to stop pinging unless you want to pick this back up."*
3. **Optional:** one parting offer — *"If timing's just off, happy to circle back in [Q+1]."*
4. **Optional** one-line door-open: *"If it ever comes back up, just reply here."*
   No link, no slot proposal — E8 is the soft exit.
5. *"All the best, Prateek"*

**Hard:** no guilt-trip language, no *"sorry I missed you"*, no fake urgency.

---

## Step 9 — Bridge variant decision logic

- **Variant A — Complexity:** multi-PSP + multi-market, 2+ visible processors, fragmented stack
- **Variant B — Limitations:** single visible PSP + multi-market or growth signals
- **Variant C — Friction:** signals are real but don't cleanly map to A or B

**Skip the bridge** when observations already do the bridging work.

**Hard rule:** always *"tends to"* or *"usually"* — never *"is"* or *"will."* The line
describes the pattern, not the prospect.

---

## Step 10 — Success case library

| Case | Industry / Pattern | Key result | URL |
|---|---|---|---|
| inDrive | Mobility, multi-country (50+) | ~90% approval, 10 new countries in under 8 months | https://y.uno/en/success-stories/indrive |
| Rappi | Super app, marketplace, multi-country | Zero implementation delays, hundreds of methods, 80% less analyst work | https://y.uno/success-cases/rappi |
| McDonald's / Arcos Dorados | QSR, 21 countries | Unified processing across 21 countries, higher approvals | (internal — no public link) |
| **Livelo** | **Loyalty/rewards. The decline-cascade case** — verbatim: *"Smart Routing also helped Livelo recover customer transactions that initially declined by instantly routing them to a secondary acquirer."* Use this whenever the prospect already runs 2+ acquirers with no failover. | **+5% approval rate · 50% of failed transactions recovered · millions of R$ saved** (3 quantified, verified live 2026-09-14) | https://y.uno/en/success-stories/livelo |
| Reserva | E-commerce, single market | +4% approval rate via smart routing | https://y.uno/en/success-stories/reserva |
| **Vibra** | Retail/loyalty, Brazil. **First-time-buyer approval** — use when the prospect's buyers are mostly first-time purchasers | New-user approval lifted **more than 30 percentage points, to 80%**; launched Apple Pay, Nu Pay and Google Pay | https://y.uno/en/success-stories/vibra |
| **Wingo** | **Airlines — the Tier 1 airline case, and the only one with numbers.** Mechanism, verbatim: *"Smart Routing technology helps Wingo maximize its transaction approval rates by enabling **automatic retries of failed payments through multiple providers**."* LATAM low-cost carrier, Bogotá. | **+14% approval rate** (stated as initial implementation phase) · **1,000+ payment methods** · 3DS + fraud tooling (verified live 2026-09-15) | https://y.uno/en/newsroom/wingo-improves-payment-efficiency-with-yuno-as-strategic-partner |
| **Qatar Airways** | Airlines, global enterprise | ✅ **Confirmed customer, no published metrics.** Named on Yuno's site-wide "TRUSTED BY GLOBAL TEAMS" list. **Nameable; never attach a number.** | y.uno (site-wide customer list) |
| **Copa Airlines** | Airlines, LATAM | ✅ **Confirmed customer, no published metrics.** On the site-wide list *and* the travel/mobility vertical list. Nameable only. | y.uno (site-wide + travel vertical lists) |
| **Avianca** | Airlines, LATAM | ✅ **Confirmed customer, no published metrics.** On the travel/mobility vertical list: *"Trusted by leading travel and mobility brands: Uber, inDrive, Avianca, Copa Airlines, Viva."* Nameable only. | y.uno (travel vertical list) |
| Open English | EdTech, subscriptions, 30+ countries | ⚠️ **No public numbers.** The page says only "increase approval rates, reduce time-to-market, and unify their payment processing." **Cannot carry an E4**, which needs three quantified bullets. Use as a one-line relevance signal only. | https://y.uno/en/success-stories/open-english |
| Viva Aerobus | Airlines | ⚠️ **This is a NOVA case, not a routing case.** The 75% comes from NOVA, Yuno's AI voice-callback assistant that phones customers after a failed payment: *"75% of contacted customers successfully completed their purchase after receiving a call."* Launched in Colombia. **Do not use it to prove a routing, cascade or failover argument** — that misattributes the mechanism. It is the right case when the prospect already hands failed payments back to a human. | https://y.uno/en/success-stories/viva-aerobus |


> ### ✅ Qatar Airways — RESOLVED 2026-09-15. Reinstated, with one limit.
>
> **The earlier withdrawal was wrong and is retracted.** It rested on a web search that
> returned nothing connecting Qatar Airways to Yuno. The search was not the problem: `y.uno`
> was unreachable from the session at the time, so the one source that settles it was never
> consulted. The site is now fetchable, and Qatar Airways is named on Yuno's **site-wide
> "TRUSTED BY GLOBAL TEAMS" customer list**, which appears on every page:
>
> *"McDonald's, Samsung, Uber, Carrefour, Ant Group, NetEase, Crypto.com, **Qatar Airways**,
> Rappi, inDrive, **Copa Airlines**, Despegar, Garena, GoFundMe, Hotmart, Viva Aerobus,
> Kavak, Moon Active, Whop, Reserva, Tada, Livelo, Wingo, and many more."*
>
> That clears the skill's own naming bar: publicly referenceable on Yuno's own site.
> **Qatar Airways, Copa Airlines and Avianca may all be named to an airline prospect.**
>
> **The limit that remains: none of the three has a single published metric.** They carry the
> relationship, not a result. Name them as customers; never attach a number, and never let a
> figure from Wingo or any other case drift onto them. For quantified airline proof there is
> exactly one option, **Wingo**.
>
> **The lesson worth keeping:** the original caution was right in method and wrong in
> conclusion. "No source found" meant "the source was unreachable", not "no relationship
> exists". When a fetch is blocked, record the account as *unverified pending a reachable
> source* rather than as *withdrawn* — and re-check once the environment changes.

### APAC references — verified status: INCOMPLETE

| Case | Industry / Pattern | Results | Verification status |
|---|---|---|---|
| **NetEase Games** | Gaming, multi-region, China-HQ | **No metrics on file** | ✅ **Upgraded 2026-09-15 — now publicly referenceable.** Named on Yuno's site-wide customer list, and carries a "Customer spotlight" on y.uno: *"NetEase Games serves players across dozens of markets with very different payment preferences, from wallets and cash-based top-ups to gift cards and BNPL, including many players who are unbanked."* **Safe to name. Still no published numbers.** |
| **Garena** | Gaming, Southeast Asia | **No metrics on file** | ✅ **Upgraded 2026-09-15 — now publicly referenceable.** Named on Yuno's site-wide customer list, so Prateek's original steer is confirmed on a public source. **Safe to name. Still no published numbers.** |

**The naming question is now settled for both — they are on Yuno's own public customer list.
The numbers question is not.** Rules that still apply:

1. **Never attach a number to either.** There are no verified metrics for them in this repo.
   Do not borrow a figure from another case, an industry benchmark, or Yuno's published
   average and attribute it to NetEase or Garena. That is fabrication, and gaming buyers in
   this territory know both companies well enough to check.
2. **Naming rule.** Only name a customer in a cold email where the relationship is
   **publicly** referenceable — a public case study, a press release, or a logo on Yuno's
   own site. **The site-wide "TRUSTED BY GLOBAL TEAMS" list on y.uno meets this bar**, and is
   the fastest way to settle whether a given logo is safe to put in writing. A relationship
   Prateek knows internally but that is not public is usable on a call; putting it in writing
   to a third party is a confidentiality question, not a copy question.
3. **What they are good for right now:** relevance signalling in Phase 2 or a manual touch —
   *"we work with gaming companies operating across Southeast Asia"* — rather than as the
   quantified E4 proof case, which needs numbers.
4. **To upgrade them to Tier 1 proof**, Prateek needs to supply, per case: markets covered,
   the specific problem solved, and 3 quantified results with an internal or public source.
   Ask for this whenever a gaming prospect enters the pipeline — Gaming is the single
   largest industry in the APAC target list (139 accounts).

> **Environment note — updated 2026-09-14:** `y.uno` **is now reachable** via Bash `curl`
> from a session on the Full network policy. `https://y.uno/success-cases` 301s to
> `https://y.uno/en/success-stories`, and the individual case pages live at
> `/en/success-stories/{slug}`. Fetch the case page and read the mechanism before citing a
> number: the Viva Aerobus correction in the table above was only caught by doing that.
> WebSearch with `site:y.uno` returns nothing useful, so go straight to curl.
> ⚠️ Fetches are intermittent. `https://y.uno/success-cases/indrive` (the old path shape)
> returns a TLS error; the `/en/success-stories/` paths work. Retry once, then move on.

**Default credibility refs when no specific case fits:** Uber, McDonald's. *(Qatar Airways withdrawn pending verification — see the warning above.)*

**Vertical shortcuts for the current P1 queue:**
- **Airlines / travel:** **Wingo carries the numbers** (+14% approval via automatic retries
  across multiple providers, 1,000+ methods, 3DS) and is the only quantified airline case.
  **Qatar Airways, Copa Airlines and Avianca carry the credibility** and may be named, with
  no metric attached. Viva Aerobus is an airline too, but its 75% is a **NOVA** result
  (AI voice callback after a failed payment), so it proves post-failure recovery, **not**
  routing. A strong airline E4 is Wingo's numbers plus a one-line "Qatar Airways, Copa and
  Avianca run on the same layer". Precedent: the Air New Zealand sequence.
  **Competitive context for airline prospects, first-party sourced and usable:** Cathay
  Pacific expanded to Adyen direct acquiring across 45+ markets including New Zealand and
  Australia (Mar 2026); Singapore Airlines consolidated onto Adyen direct acquiring to stop
  "running payments across multiple third-party platforms"; Emirates appears on CellPoint
  Digital's own airline customer wall; Cebu Pacific's CellPoint case study states it
  "implemented its multi-acquirer strategy more efficiently". Name the airline and what it
  did — never imply any of them is a Yuno customer.
- **EdTech / subscriptions:** Open English is the only edtech logo, but it carries **no
  public numbers**, so it cannot carry an E4. For a quantified proof touch use **Livelo**
  (decline recovery via a secondary acquirer) or **Vibra** (first-time-buyer approval) and
  state plainly that it is a pattern match, not an edtech case. Precedent: the WuKong
  Education sequence.
- **Streaming / OTT with a diaspora audience:** no clean case in the library. Search y.uno
  first; otherwise Tier 2 on the multi-country recurring pattern (Open English) and be
  explicit that it's a pattern match.
- **Gaming:** NetEase Games and Garena are the relevant APAC references, but neither has
  verified results on file — see the rules above. For a quantified E4, fall back to a Tier 2
  pattern match (inDrive for multi-country scale, Rappi for provider breadth) and say plainly
  that it's a pattern match, not a gaming case.

**Before defaulting to this table for any APAC prospect**, WebSearch
`site:y.uno success case [industry keywords]` and `site:y.uno newsroom [market or vertical]`.
Ask Prateek for internal APAC references if the search comes up empty — flag it rather than
stretching a LATAM case.

---

## Step 11 — Industry overrides

- **B2B SaaS / AI / Cybersecurity / Hosting:** rail-gap framing is usually *wrong*. Anchor on
  cross-border card processing, approval rates by issuer geography, failover.
- **Streaming / OTT / Dating / Subscription apps:** recurring auth optimization + rail
  coverage in top subscriber markets. Check the app-store split first (Step 3).
- **EdTech:** high-ticket fees, instalments and EMI, recurring collection under local mandate
  rules, international student payments.
- **Airlines / OTA / Travel:** cross-border on bookings, currency mix, high ticket value,
  peak-demand routing, instalments in India/Japan/Taiwan.
- **Gaming / esports:** wallet and carrier-billing rails, high decline sensitivity, frequent
  market entry.
- **Crypto / digital assets:** acquirer appetite, MCC-driven declines, diversification.
  Check local legality per market.
- **Super apps / marketplaces / q-commerce:** multi-corridor settlement, split payouts, local
  rail coverage per country.
- **Investment / trading:** approval rates on deposits, local banking rails, funding speed.
- **PSPs / payment infrastructure:** not in ICP. Stop and flag.

**Event-aware CTAs:** if research or context surfaces an event both parties will attend
(Money20/20 Asia, Seamless Asia, Singapore Fintech Festival, Global Fintech Fest, etc.), swap
the Phase 2 and Phase 3 CTAs to event-based:
> *"Since we'll both be at [event], would it make sense to grab 15 minutes and a coffee there?"*

---

## Step 12 — Compose into the company file

The sequence is NOT written to chat. It composes INTO
`2-ready-to-outreach/{normalized-name}.md`, replacing the Section 2 placeholder.

### 12a. Update the status header
`**Status:** 🟡 Research complete — outreach not yet generated`
→ `**Status:** 🟢 Ready to outreach — sequence drafted`

Other header fields stay untouched.

### 12b–c. Replace the Section 2 placeholder

Keep the `<details open>` wrapper and `<summary><h2>...</h2></summary>` line unchanged; only
the inner content changes. Every email body and LinkedIn message MUST be wrapped in a
triple-backtick `text` code block so GitHub renders a copy button. Subject lines sit outside
the code block as a `**Subject:** ...` line above it.

Structure of the new inner content:

```
### Pain Vector Extraction
{the Step 5 block, rendered as markdown}

---

### Phase 1 — Curiosity (Days 1–5)
#### Touch 1 — Email 1 · Day 1
**Subject:** {≤6 words}
{code block: Email 1 body}
#### Touch 2 — Email 2 · Day 3 · REPLY IN THREAD
{code block: Email 2 body}
#### Touch 3 — LinkedIn message 1 · Day 5
{code block: LK1}

---

### Phase 2 — Diagnosis (Days 7–9)
#### Touch 4 — Email 3 · Day 7 · NEW EMAIL
**Subject:** {new subject}
{code block: Email 3 body}
#### Touch 5 — LinkedIn message 2 · Day 9
{code block: LK2}

---

### Phase 3 — Proof (Days 11–17)
#### Touch 6 — Email 4 · Day 11 · NEW EMAIL
**Subject:** {success case subject}
{code block: Email 4 body}
#### Touch 7 — Email 5 · Day 13 · MANUAL
*Placeholder — manual creative approach. Do not auto-write.*
#### Touch 8 — Email 6 · Day 15 · MANUAL
*Placeholder — second manual approach, different format than E5.*
#### Touch 9 — LinkedIn message 3 · Day 17
{code block: LK3}

---

### Touch 10 — Email 7 · Day 19 · MANUAL
*Placeholder — manual creative bridge. Anchor to something fresh.*

---

### Phase 4 — Breakup (Days 21–23)
#### Touch 11 — LinkedIn message 4 · Day 21
{code block: LK4}
#### Touch 12 — Email 8 · Day 23 · REPLY IN THREAD to Touch 4 or 6
{code block: Email 8 body}

---

### Source Notes
- ✅ {verified claim} — source
- ⚠️ {unverified claim} — what would verify it

### Success Case Alternatives
- **{Alt 1}** — {match rationale, 1 line}
```

**Anything tagged ⚠️ unverified must be rewritten or cut before Prateek sends.**

### 12d. Save
Two Edit replacements: the status header line, and the Section 2 inner content. Do not touch
Section 1 or Section 3.

### 12e. Commit
```
git add 2-ready-to-outreach/{normalized-name}.md
git commit -m "outreach: {Company Name} — 12-touch sequence drafted"
```
Then confirm the path in chat with a 2–3 sentence summary of the Phase 2 hypothesis and the
matched success case.

---

## Voice rules (all auto-written touches)

- **First-person, conversational:** *"I work at Yuno"* not *"Yuno is..."*
- **Humble framing:** *"We consider ourselves..."* not *"We are the..."*
- ***"Tends to"* / *"usually"*** over *"is"* / *"will"*
- **Match the phase:** curiosity → diagnosis → proof → breakup
- **Parenthetical aside** allowed once, in Touch 6 bullets
- **LinkedIn** shorter and more direct than email at the same phase
- **Yuno additive from Phase 2 on:** *"keep your stack, add what's missing"*

**Never use:**
- *"Hope this finds you well"* / *"Just wanted to reach out"* / *"Hope you're well"*
- *"Just bumping this"* / *"Circling back"* / *"Didn't want this to get buried"*
- *"I imagine"* / *"I'd guess this is creating"* / *"You must be"* / *"This must be costing you"*
- *"Seamless"* / *"Leverage"* / *"Synergies"* / *"Cutting-edge"* / *"Best-in-class"* / *"Robust"*
- *"Do the needful"* / *"Revert back"* / *"Kindly"* — regional business-English tics that
  read as boilerplate to a global buyer
- Em dashes used as separators
- Any competitor name: Juspay, Gr4vy, Primer, Spreedly, Payrails, CellPoint, BR-DGE, Pagos

---

## Hard rules

**Never:**
- Project pain in Phase 1
- Invent numbers, vendors, PSPs, markets or stakeholders not verified in research
- Cite an APAC regulatory rule not verified in the research file
- Imply a LATAM case study's results came from an Asian market
- Open a displacement account with "you have no orchestration layer"
- Ask for a meeting in Phase 1 (E1, E2, LK1)
- Insert a booking link anywhere — none exists
- Stack more than 3 observations in E1
- Apologize for silence between touches
- Mention Yuno competitors
- Repeat observations across touches
- Position Yuno as a PSP replacement
- Auto-fill real contact names — always `{{recipient.first_name}}`
- Write bodies for the manual touches (E5, E6, E7)
- Repeat the E4 bullet verbatim in LK3

**Always:**
- Output the Pain Vector Extraction block before drafting
- Check the Motion line and apply the Step 6a override
- Use *"tends to"* / *"usually"* in the Phase 1 transition
- Include the cadence + opt-out line in E2
- Propose meeting times in the prospect's local time zone
- Fact-check every number, market, PSP and stakeholder claim against research
- Source-tag every prospect-specific factual claim in Source Notes
- Vary day/time slots across all five meeting-request CTAs, and name the prospect's time zone
- Vary sign-offs — *"Best,"* / *"Cheers,"* / *"All the best,"* / *"Looking forward to it,"*

---

## Self-review checklist (before output)

- [ ] Motion checked; displacement/in-house override applied if applicable
- [ ] Phase 1: no projected pain, no meeting ask
- [ ] E2 walks the mechanism factually (no percentages, no revenue claims)
- [ ] E2 maps to **one** sharpest E1 observation, includes cadence + opt-out, doesn't repeat E1's Yuno line
- [ ] Bridge variant matches the setup, rationale logged
- [ ] LK1 references that the email exists
- [ ] E3 opens with the hypothesis, no apology
- [ ] E4 bridges from the hypothesis, 3 quantified bullets, one parenthetical, CTA + case link
- [ ] E4 case tier flagged; no LATAM case implied as APAC
- [ ] E5, E6, E7: placeholders only
- [ ] LK3 proof-anchored; LK4 stripped down; E8 short and pressure-free
- [ ] Five distinct day/time combos, all named in prospect-local time
- [ ] No booking link anywhere in the sequence
- [ ] No em dashes as separators, no buzzwords, no competitors named
- [ ] Source Notes complete
- [ ] Subscription fork applied if applicable; app-store split checked
- [ ] Industry override applied if applicable

---

## Edge cases

- **Sparse research:** drop to 2 observations in E1, skip the bridge, flag low confidence.
- **Prospect is a PSP / payment infra:** not in ICP — stop and flag.
- **App-store-dominated revenue:** stop and flag before drafting.
- **Competitive motion with no concrete gap found:** flag rather than sending a weak sequence.
- **No clean success case:** WebSearch y.uno first, then Tier 3 defaults, flag the tier.
- **Hard objection in past interaction:** stop and ask Prateek.
- **Prospect in a market Prateek can't reasonably meet live** (e.g. a narrow overlap window
  with no workable slot): propose an async alternative — a short recorded walkthrough or a
  written teardown — rather than a slot that cannot happen.
