# Email Samples — Voice Anchor

Real outreach written by Prateek. `/full-outreach` reads this file to match his voice.

Recipient names are replaced with `{{recipient.first_name}}`. Prospect-specific facts are
kept as-is because they show *how* he grounds a claim, which is the point of the sample.

---

## Precedence rule — read before drafting

**The samples supply the voice. `full-outreach.md` wins on conflict.**

Prateek's instruction, verbatim: *"Use mix of both, Yamin's rulebook overrule mine."*

Where his natural writing and the rulebook disagree, the rulebook governs. The resolved
conflicts, so no one has to re-litigate them:

| Conflict | Sample does | Rulebook requires | Winner |
|---|---|---|---|
| Opening | *"Hope you're having a good week"* | No pleasantry, straight in | **Rulebook** |
| Em dashes | Used as separators throughout | Full stops, commas, or restructure | **Rulebook** |
| CTA | *"Worth 30 minutes? Happy to work around your calendar"* | A specific day and two specific times, prospect-local | **Rulebook** — and it matters more here than in EMEA, because there is no booking link to fall back on |
| Asserting pain | *"are likely consuming a disproportionate share of your team's time"* | *"tends to"* / *"usually"*, describing the pattern not the prospect | **Rulebook** (the sample already half-hedges; go the rest of the way) |
| Additive framing | Implied | Stated outright: *"keep your stack, add what's missing"* | **Rulebook** |
| Social proof | Long customer list mid-email | Quantified case in E4 only, with a source | **Rulebook** |

Where the rulebook is **silent**, the sample governs — these are additions, not conflicts:

- **The embedded discovery question.** *"How long does it take you today to spot a file that
  didn't reconcile, and does that sit with finance or payments?"* Gives the reader something
  easy to answer that isn't yes/no to a meeting. Use it.
- **Grounding observations in the prospect's own documents** — their Terms, their annual
  results, their help centre — and quoting the phrase. Far stronger than a third-party
  source, and it is the single most repeatable habit in this sample.
- **The diplomatic clause.** *"not because anyone's doing it badly."* Keeps a hard
  observation from reading as criticism. Costs six words, worth it when the observation
  stings.
- **Multi-threading in the sign-off.** *"If reconciliation sits elsewhere, happy to be
  pointed there."*
- **Naming the asymmetry.** See the sample. Contrasting two of the prospect's own systems
  against each other beats any external benchmark, because they cannot dispute either half.

**Length caveat.** Sample 1 is a single long-form email, not a 12-touch Phase 1 opener.
Phase 1 in the sequence stays short and observation-only. Sample 1's density is the right
model for **E3 and E4**, where assertion and proof are allowed. Do not import its length
into E1.

---

## SAMPLE 1 · Viu · streaming / OTT, 15 APAC markets · long-form first touch

Prateek's original, as sent. ~700 words.

```text
Hi {{recipient.first_name}}, hope you're having a good week.

I'm Prateek, I look after APAC Sales at Yuno. I was chatting with our CRO in our 1:1
yesterday, and the second I mentioned Viu was on our target list he got visibly excited -
he said this is an account worth going all in on. So rather than sending you something
generic, I spent the past couple of days properly mapping your payment setup. Here's what
I found.

Running payments across Viu's 15 markets is a genuinely difficult operational problem -
each one with its own mix of gateways, card rails, alternative payment methods and telco
billing relationships. Reconciliation and chargeback management on top of that are likely
consuming a disproportionate share of your team's time, just to keep visibility across that
many disconnected systems.

The telco side alone shows the scale. Your 2025 results describe the strategy as "deepening
partnerships with leading local carriers such as Thailand's AIS and True, and Indonesia's
Telkomsel". CelcomDigi alone runs four different Viu products - a postpaid add-on, a prepaid
5G SpeedSTREAM bundle, free Premium on a device contract, and the Mega add-on. Telkomsel
runs a mobile one and a separate IndiHome fixed-line one. That's six settlement shapes from
two operator groups, before you count Maxis, Indosat and AIS, or Etisalat, Orange, Vodafone
and Fawry in Egypt.

And carrier billing reconciles worse than cards structurally, not because anyone's doing it
badly: the baseline is still a monthly PDF and CSV, partial and duplicate records are
designed in, and the operator's key is the MSISDN rather than your account ID - so there's
no native join between their charge record and your subscriber.

On the card side, your Terms name Adyen as "Viu's authorised direct credit card and debit
card payment gateway" - one provider underneath every market, so a failed renewal is final.
Two things change that. Routing: traffic moves to a local provider by rule and redistributes
automatically when one degrades, worth an average 8% authorisation uplift. And smart
retries: a declined renewal is retried on its own schedule and can go out through a
different provider entirely, with dunning running alongside it. There's an asymmetry worth
noticing — your operator rails keep retrying a subscriber until their balance tops up, while
your card book gets one attempt and calls it churn.

The checkout has gaps too. Your pages name GoPay as the only wallet in Indonesia - no DANA,
OVO, ShopeePay or QRIS. Malaysia shows no Touch 'n Go or FPX; Thailand no PromptPay. We
carry all of those through one integration. Egypt is the opposite case: two-thirds of the
country is unbanked, so operator billing there is the only rail, and routing and
reconciliation are the whole game.

It all lands in one place. Yuno pulls each provider's settlement file, matches it against
what you actually billed, and flags every break - Reconciled, Not reconciled, Non
reconcilable or Conflict - alongside transactions, refunds, disputes and provider
performance. How long does it take you today to spot a file that didn't reconcile, and does
that sit with finance or payments?

That workload only grows: HBO Max went live in five of your markets in December, and iQiyi
rolls out across four more this half - each one another revenue share to reconcile. Yuno
connects 1,000+ payment methods, PSPs and fraud tools through a single API: routing,
retries, dunning, network tokens, 3DS and reconciliation in one dashboard. NetEase Games,
Garena, Whop and Uber run on us; Hotmart and Open English on the subscription side;
McDonald's across Latin America.

Worth 30 minutes with you and whoever owns payments? Happy to work around your calendar -
and if reconciliation sits with someone else, happy to be pointed at them.
```

### SAMPLE 1a · the same email, rulebook-compliant, 248 words

This is the target shape: Prateek's observations and register, Yamin's discipline.

```text
Hi {{recipient.first_name}},

I'm Prateek, I look after APAC sales at Yuno. Spent a few days mapping Viu's payment setup
across your 15 markets. A few things stood out.

Your Terms name Adyen as Viu's authorised card gateway. One provider under every market, so
a failed renewal is final.

Your carrier rails behave the opposite way. CelcomDigi alone runs four Viu products,
Telkomsel two: six settlement shapes from two operator groups, before Maxis, Indosat, AIS or
Egypt. Carrier billing also tends to reconcile worse than cards structurally. Monthly PDFs
and CSVs, partial and duplicate records designed in, keyed on MSISDN rather than your
subscriber ID, so there's no native join.

The asymmetry is worth sitting with. Your operator rails keep retrying a subscriber until
their balance tops up. Your card book gets one attempt and calls it churn.

Coverage gaps too. Indonesia shows GoPay as the only wallet, no DANA, OVO, ShopeePay or
QRIS. Malaysia no Touch 'n Go or FPX, Thailand no PromptPay.

Yuno sits above what you already run, so you keep Adyen and add what's missing. Routing and
smart retries across providers, dunning, and reconciliation that matches each settlement
file against what you billed and flags the breaks.

How long does it take you today to spot a file that didn't reconcile, and does that sit with
finance or payments?

Thursday is open for me. Would 3pm or 4:30pm your time work for 30 minutes? If
reconciliation sits elsewhere, happy to be pointed there.

Best,
Prateek
```

**What the compression removed, and why it can come back:**
- The CRO anecdote. About the sender, not the reader.
- The per-product carrier enumeration. The count does the same work; keep the detail for the reply, where it proves the research.
- The reconciliation status taxonomy. Demo material.
- HBO Max / iQiyi expansion. Good trigger, third-best argument. First thing to restore at 300 words.
- The 8% authorisation uplift. If restored, attribute it as Yuno's published figure — an
  unattributed number invites *"on what basis?"* as the reply.
- The customer list, which also parks the Garena question until the relationship is
  confirmed publicly referenceable.

---

## Still needed

One sample is thin. Two or three more would let the skill infer register across situations
rather than copying this one. Most useful next:

1. **A short first touch** — under 150 words. Sample 1 is long-form; there is no model yet
   for Phase 1 brevity in Prateek's voice.
2. **A LinkedIn message.** Nothing on file. LK1–LK4 are currently drafted from the rulebook
   templates alone.
3. **One that got no reply**, marked as such. Knowing what misses look like is diagnostic.
