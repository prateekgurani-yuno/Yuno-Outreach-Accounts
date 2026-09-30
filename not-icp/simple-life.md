# Simple.life

**Status:** 🔴 Not ICP — out of territory
**ICP Score:** Not scored — rejected at the Phase 0 qualification gate, before scoring
**Industry:** Intermittent-fasting / weight-loss subscription app · **HQ:** Dover, Delaware, USA · **Researched:** 2026-09-30 · **First email sent:** —
**Motion:** N/A

---

## Rejection Rationale

**Out of territory.** The `/research` Phase 0 gate rejects a company that is *"HQ'd west of Dubai
with no APAC operations."* Every corporate entity behind Simple.life sits west of Dubai, and I
could not find an APAC entity, office, APAC-language site or APAC-market reference anywhere in
their own first-party material.

This is **not** a quality judgement. Simple.life is a strong Yuno prospect — see "Why this hurts"
below. It belongs to AMER/EMEA, not to Prateek's patch.

### The entities — from their own privacy policy

`simple.life/privacy/` (fetched by me, HTTP 200, 79,638 b) names the controllers verbatim:

> *"**Simple.Life Apps Inc**, a **Delaware corporation** with registration no. **7688095** and
> registered address at 8 The Green, Ste A, Dover, County of Kent, DE 19901, **USA**; and its
> subsidiary, **AM APPS Ltd**, a **Cyprus** company with registration no. **ΗΕ 392517** and
> registered address at 188 Ayias Fylaxeos, Excelia Tower, Ground Floor, 3083, Kapsalos,
> **Limassol, Cyprus**"*

A third entity exists in the UK. **SIMPLE.LIFE APPS UK LTD**, company number **13409801**, private
limited, **Active**, incorporated **20 May 2021**, registered office Sterling House, Fulbourne Road,
Walthamstow, London, England, E17 4EE — [Companies House](https://find-and-update.company-information.service.gov.uk/company/13409801) (fetched).

Delaware · Cyprus · London. Three entities, three jurisdictions, all west of Dubai.

**Parent:** Palta, which co-founded Simple in 2019 with Mike Prytkov and Alex Ilinsky.
`[UNVERIFIED — search summary only, page not fetched]`

### The absence of APAC is sourced, not assumed

I ran each of these with a passing control term, because a silently blocked or truncated fetch
looks exactly like a clean negative:

| Check | Result | Control |
|---|---|---|
| APAC country/market names in the privacy policy (`india\|indonesia\|singapore\|malaysia\|thailand\|vietnam\|philippines\|japan\|korea\|china\|hong kong\|taiwan\|australia\|new zealand\|apac\|asia`) | **0 hits** | `cyprus` 2, `delaware` 1 ✅ |
| Same terms on the homepage, plus `tokyo\|sydney` | **0 hits** | `Spanish` 2, `French` 2 ✅ |
| Site locale switcher (`data-locale` attributes) | **`de`, `en`, `es`, `fr`, `it`** — five locales, **zero APAC languages** | switcher found and parsed ✅ |
| `<html lang>` | `en-US` | — |
| `hreflang` alternates | **none at all** | — |
| Regional domains | `www.simple.life` → 301 → `simple.life`. `simple.app` resolves 200 but is a separate property, not resolved further. No `.jp`, `.co.jp`, `.sg`, `.in`, `.com.au` variant found. | — |

**The locale switcher is the decisive line.** Japan is their #3 traffic country and the product
ships in **no Japanese**. Meanwhile `es`/`fr`/`de`/`it` map exactly onto where the growth is —
France ▲203.52%, Spain ▲161.27%, Italy ▲72.33%, and Spanish covering Uruguay ▲>5,000%. Their
localization roadmap is Western Europe and LATAM, in their own markup.

### The traffic says the same thing

Full table in `accounts/traffic/simple-life.md`. The short version:

| | |
|---|---|
| US + Brazil | **74.12%** |
| APAC visible | **2.51%** — Japan alone |
| Unshown tail (86 countries) | 11.48% |
| Absolute APAC ceiling if the entire tail were APAC | **13.99%** — arithmetically impossible in practice |

### Where I am making a judgement call — so Prateek can overrule

Japan at 2.51% is **traffic, not operations**. The Phase 0 rule turns on APAC *operations*, and I
found none: no entity, no office, no Japanese localization, no APAC market named in any first-party
document. I am reading 2.51% of unlocalized Japanese traffic as incidental rather than as an APAC
operation, and rejecting on that basis.

If Prateek disagrees — if unlocalized Japanese traffic on a product growing this fast is worth a
speculative touch — move this file back to `1-to-outreach/` and the run can proceed. The decision
is his; the evidence above is what I would want him deciding on.

## Why this hurts — route it to AMER/EMEA, don't drop it

Whoever owns this territory should get told. Three things make it a live account:

1. **Their privacy policy admits to PSP sprawl, in writing.** Verbatim: *"We may disclose your
   personal data, including payment data, to various payment processing and payment gateway
   providers that help us connect with different banks and payment systems around the world …
   **Due to the large number of payment processing providers we work with, it is impractical to
   list them all here.** However, some examples are **Stripe, PayPal, Checkout**."* A merchant that
   cannot enumerate its own processors in its own privacy policy is describing exactly the problem
   orchestration solves. Note this is a disclosure of processors they *may* use, not a confirmed
   live routing configuration — it would need a checkout audit to firm up.
2. **Brazil is 24.01% and growing 71.14%.** Second-largest market, and Pix/boleto/local instalments
   are the whole conversion story there.
3. **Uruguay ▲>5,000%, Spain ▲161%, France ▲204%.** A LATAM-plus-Southern-Europe expansion in
   progress, which is when the per-market PSP integration cost actually bites.

## Not assessed, because the run stopped at the gate

No ICP score, no PSP stack confirmation beyond the policy text above, no checkout audit, no APM gap
analysis, no volume figure, no competitor stack work. The volume gate was **never tested** — no
sourced transaction count was found, and per the rules an assumption never fires that gate. None of
the above should be read as a finding about those areas.

*Marked: 2026-09-30 — Phase 0 territory gate, no research run consumed.*
