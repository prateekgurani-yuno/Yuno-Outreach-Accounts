# ChangeNOW

**Status:** 🔴 Not ICP — **three independent Phase 0 gates**
**ICP Score:** not scored — **rejected at Phase 0 before the research run**
**Industry:** Non-custodial instant cryptocurrency exchange — plus a B2B crypto payments/infrastructure arm · **HQ:** **CHN Group LLC**, Euro House, Richmond Hill Road, Kingstown, **Saint Vincent and the Grenadines** · **Researched:** 2026-10-14 · **First email sent:** —
**Motion:** n/a — ChangeNOW does not acquire cards, so there is no payment flow for an orchestrator to sit in front of

---

> ## 🛑 Why this was rejected — three gates, any one of which is sufficient
>
> **No 5-agent research run was spent.** All evidence below is first-party, fetched and
> control-tested by me: `changenow.io` returns a real 404 at **1,576 B** against a **74,141 B**
> homepage, so every zero below is a real zero.

### Gate 1 — Payment infrastructure company → route to Partnerships

ChangeNOW's own site navigation carries a **"For business"** menu listing four products:
**ChangeNOW for Business · NOW Custody · NOWPayments · NOWNodes**. Verbatim from their homepage:

> *"**NOWPayments** — Integrate NOWPayments and start receiving online payments in crypto!"*
> *"**NOW Custody** — Receive, store, convert and manage crypto with the single robust API."*
> *"**NOWNodes** — The ultimate infra provider supporting…"*

Their footer adds **Widget · White Label · API · Development API · For Partners · Asset Listing**.

`NOWPayments` appears **5× on the homepage, 3× in the Terms, 3× in the FAQ** (control: 0).
`NOWNodes` 4/3/3. `white label` 2/2/2.

**NOWPayments is a crypto payment gateway sold by the same group.** That is the Phase 0
"PSP, gateway, acquirer or orchestrator" gate. This is a Partnerships conversation, not an
outbound prospect.

### Gate 2 — ⭐ The decisive one: ChangeNOW never touches a card

There is no acquiring relationship to orchestrate. Verbatim from their own FAQ:

> *"Can I buy cryptocurrency with fiat through ChangeNOW? Yes, you can buy cryptocurrency with
> a USD/EUR card. **This feature is brought to you by our third-party partner services, such as
> Guardarian, Banxa, or Transak.**"*
>
> *"If you want to purchase crypto with USD, EUR, or any fiat currency, you will need to enter
> your email address **on the side of our third-party partners**, Guardarian, Banxa, or Transak."*
>
> *"Your card must comply with the requirements of **our payment provider**: the card must be
> issued by VISA or MasterCard."*

KYC is outsourced too — *"entirely on the side of our third-party partner, Sum & Substance
(Sumsub)"*.

**Token counts, with a passing control:** `Guardarian` 3 · `Banxa` 3 · `Transak` 3 in the FAQ,
against **`credit card` = 0, `debit card` = 0, `bank transfer` = 0, `SEPA` = 0, `Apple Pay` = 0,
`Google Pay` = 0** across homepage, Terms and FAQ. Control page: 0 for everything.

**ChangeNOW's own flow is crypto-in / crypto-out.** The fiat leg is a hand-off to a third party
who is the merchant of record and owns the acquiring. **Guardarian, Banxa and Transak are the
orchestration prospects here — ChangeNOW is not.** Those three are worth adding to the queue.

Note also: the fiat on-ramp is **USD/EUR only**. No local APAC currency, no APAC rail, on the
one leg of the business that touches money at all.

### Gate 3 — Out of territory

Billing entity, verbatim from their own footer: *"© 2017 – 2026 **CHN Group LLC, Company No.
3010 LLC 2023**. Registered address: **Euro House, Richmond Hill Road, Kingstown, Saint Vincent
and the Grenadines**."*

Caribbean — **west of Dubai**. And no APAC operations exist to override that:

| Token | homepage | Terms | FAQ |
|---|---|---|---|
| Singapore · Hong Kong · Japan · Korea · Indonesia · India · Australia | **0** | **0** | **0** |
| Saint Vincent / Kingstown / Grenadines *(control)* | 2 | 2 | 2 |

**Zero mentions of any APAC market across all three documents**, against a passing control.
CLAUDE.md: *"Company is HQ'd west of Dubai with no APAC operations — out of territory, stop and flag."*

---

## Traffic — and why it does not rescue the account

Full record in `accounts/traffic/changenow.md` (SimilarWeb, supplied 2026-10-14, Jul–Sep 2026,
all country domains ON, 93 countries).

**United States 27.44%** — four times the next market. **Visible APAC territory is ~14.3%**
across five markets, none above 6.2%. Users in a market are not operations in it.

⚠️ **The Indonesia row looks like the APAC case and is not.** It is #2 at **6.13%, ▲484.29% MoM**
— on **13-second sessions** and a 56.59% bounce, against US sessions of 4:12 at 9.02 pages. A
crypto swap takes minutes and several pages. A near-500% jump landing on 13 seconds reads as
referral or non-human traffic. **Not usable as a volume argument.**

⚠️ **Kazakhstan (3.35%) left unresolved** — CLAUDE.md says "east of Dubai" but its market table
does not enumerate Central Asia. Flagged for Prateek, not decided here. 🇦🇪 UAE (1.52%) is Gulf,
so EMEA.

---

## Analyst note — the real opportunity is downstream, not here

The rejection is clean, but the research surfaced three genuine prospects: **Guardarian, Banxa
and Transak** are the parties actually acquiring cards for this flow, in USD/EUR, for a global
crypto-buying audience. None is on `accounts/apac-tal.csv`. Whether any is in territory needs
its own check — but they are the companies with the card volume ChangeNOW does not have.

**Volume gate: not assessed, and deliberately not assumed.** No sourced or derivable transaction
count was sought, because Gates 1–3 settle the account without it. Per the disclosure rule, no
figure is stated rather than an unsourced one being invented.
