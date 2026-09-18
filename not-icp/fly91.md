# Fly91

**Status:** 🔴 Not ICP — under 40k monthly transactions
**ICP Score:** not scored → **volume gate fired before scoring**
**Industry:** Airlines (regional turboprop, UDAN/RCS) · **HQ:** Goa, **India** — Just Udo Aviation Pvt Ltd, corporate office Vile Parle, Mumbai · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** n/a — rejected at Phase 0

---

> ## 🔴 REJECTED ON THE VOLUME GATE — and the shortfall is not marginal
>
> The qualification rule: **a sourced or soundly-derived monthly transaction count under 40,000 rejects the account.** Fly91's fires on its own published number.
>
> **✅ Verified by me directly** on `fly91.in/press-releases`: **"FLY91 Marks Two Years of Operations, Flies Over 4.8 Lakh Passengers Across Regional India"**, dated **18 March 2026**.
>
> **480,000 passengers ÷ 24 months = ~20,000 passengers per month.**
>
> That is the ceiling before any divisor is applied. Then two divisors both push it down:
>
> | Divisor | Effect |
> |---|---|
> | **Passengers per booking** | One PNR carries several passengers. Indian domestic runs ~1.5–1.9; Fly91's network (Goa, Sindhudurg, Agatti/Lakshadweep, Pune) is leisure-heavy, which skews **higher**. |
> | **Direct-website share** | Confirmed material indirect distribution — a live travel-agent portal at `fly91.in/reservation/ibe/login` serving `agencyBooking.css`, a **Paytm Travel distribution tie-up** (Feb 2025, inventory access — *not* a payments deal), a **MakeMyTrip** partnership, and OTA listings. |
>
> **Even at the absurd best case — 1.0 passenger per booking and 100% direct-website — the lifetime run rate is 20,000 transactions a month, half the floor.**
>
> On current (higher) run-rate inputs the answer does not change. DGCA reports **2.41 lakh passengers Jan–Jun 2026 at 0.3% domestic share** (~40,167 pax/month) and the physical ceiling of 6 ATR 72-600s at 73.2% load factor is ~63,900 pax/month. Take the most generous: **64,000 pax ÷ 1.5 per PNR = ~42,600 all-channel bookings**, and the direct-web share then cuts that to roughly **17,000–26,000**.
>
> **There is no plausible combination of inputs that clears 40,000.** Clearing it would require assuming every passenger books individually *and* that no agent, OTA or GDS sale exists. Both are demonstrably false.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Fly91 is a two-year-old Indian regional carrier operating six ATR 72-600s from Goa (Manohar/Mopa) and a second hub at Hyderabad, across 12–13 destinations under the UDAN regional connectivity scheme. It is **healthy and growing** — this is a size rejection, not a distress rejection.

### ⛔ CORRECTION TO THE TARGET ACCOUNT LIST — the Juspay entry is unsupported
`accounts/apac-tal.csv` carries **`Payment Orchestrator: Juspay`** for Fly91, and the stub repeated it with a VERIFY flag. **It could not be substantiated and the evidence runs the other way:**

- **Zero occurrences of "juspay"** anywhere on `fly91.in` — not the marketing site HTML, not the theme JS, not the IBE login or manage-booking pages, not the booking-framework scripts, not the Terms, Privacy or Conditions of Carriage.
- **Juspay's own airlines page names Air India, Singapore Airlines, SpiceJet and IndiGo.** Fly91 and Just Udo Aviation appear nowhere on it.
- No CSP header on either property, so there is no allowlist to mine either way.

**This is a displacement motion that does not exist.** The row should be cleared — see the TAL correction queue below.

### What the stack actually looks like
| Layer | Finding |
|---|---|
| **Booking engine** | **IBS Software (iFly Res)** — `cms.ibsplc.aero/.../com.ibsplc.ibe/...` asset paths, session cookie `SECURE_SESSION_COOKIE….IBE_IC_prd_2` (IC = Fly91's IATA code), Spring/Dojo stack behind Cloudflare + AWS ALB. The marketing site is a separate **Drupal 10** property with the IBE path-mounted on the same domain. |
| **Payment gateway** | ⚠️ **INDICATIVE ONLY — Razorpay.** `fly91.in/reservation/common/scripts/common.js` sets `childFOP = "RAZORPAY"` on one radio option. **But the same block also carries `IDEAL`, `SOFORT`, `BKM` (Turkish) and `CREDITCARD`** — this is IBS's shared product library shipped to every airline customer, not a Fly91-specific config. **Suggestive, not proof.** |
| **Methods** | Conditions of Carriage clause 1.9, verbatim: *"Fly91 accepts various forms of payment, such as credit cards, debit cards, net banking, UPI, and wallet, as determined by Fly91 from time to time."* Clause 1.18 confirms foreign-issued cards are accepted but carry extra gateway verification. |

### Company facts
- **Just Udo Aviation Private Limited**; commercial ops from **18 March 2024**, AOC 6 March 2024
- **6 × ATR 72-600**; 13 destinations as of Sept 2026 (Tirupati added 10 Sept 2026)
- **Firm order for 40 × ATR 72-600 announced 3 September 2026** — largest ATR regional order globally in about a decade, deliveries 2027–2032, 60+ fleet target in five years
- Anchor investor **Convergent Finance LLP** (Harsha Raghavan, Chairman) with founder/CEO **Manoj Chacko**
- **No financial distress found.** No suspension, grounding, AOC action or insolvency. The September 2026 aircraft order signals the opposite.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

**None, and none should be generated.** `/full-outreach` must never run on a rejected company.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### Why this was not scored on the 29-point matrix
The volume gate sits at **Phase 0**, before scoring. A company below the minimum transaction floor is out of ICP regardless of how it would score on orchestration, rails or geography — so assigning it a number would imply a comparability it does not have. **Recorded as rejected on the gate, not as a low score.**

### Source Notes
- ✅ **The decisive figure — "Over 4.8 Lakh Passengers" in two years — was verified by me directly** on Fly91's own press-release index, with the 18 March 2026 date.
- ✅ **The agent-distribution evidence was verified**: the Partner Login IBE and the Paytm Travel release, which is explicitly about *"passengers' access to the airline's ticketing inventory on Paytm"* — **a distribution deal, not a payments deal. Do not misread it as a Paytm PG relationship.**
- ✅ **The Juspay refutation** rests on first-party absence across every reachable Fly91 property plus Juspay's own customer page.
- ⚠️ **DGCA monthly figures (2.41 lakh Jan–Jun 2026, 0.3% share, 73.2% PLF, June ~53,900 pax)** are agent-reported and `[UNVERIFIED — not fetched by me]`. **They do not change the outcome** — the first-party 24-month figure alone fires the gate, and the DGCA numbers only corroborate.
- ⚠️ **The 40-aircraft ATR order** is visible as a headline on Fly91's own press index (3 Sept 2026, verified by me); the deliveries/valuation detail is `[UNVERIFIED — search summary only]`.
- ❌ **The live payment page could not be reached** — `/reservation/ibe/payment` and `/paymentOptions` return 403 without a booking session. That is the only thing that would turn Razorpay from indicative into confirmed, and it does not matter while the account is rejected.
- ❌ **Direct-vs-indirect distribution split: never disclosed.** The single biggest uncertainty in the derivation — but it only ever moves the number **down**.

## Rejection Rationale

Fly91's own published milestone — **480,000 passengers in its first 24 months, ~20,000 per month** — puts it below the 40,000 monthly transaction floor before any divisor is applied, and both applicable divisors (passengers per PNR, and a confirmed material agent/OTA channel) push it lower still; on the most generous current-run-rate inputs the figure lands at roughly **17,000–26,000 transactions per month**. The target list's `Payment Orchestrator: Juspay` entry was independently refuted rather than confirmed, so there is no displacement motion here either.

> ### 📅 REVISIT IN 2028 — this is a diarised re-check, not a permanent kill
> The **40-aircraft ATR order placed 3 September 2026** (deliveries 2027–2032, 60+ fleet target) is roughly a **7–10× capacity increase**. That is the only path to clearing the bar, and it is a credible one. **Re-check when the fleet passes ~20 aircraft.** The account is otherwise a clean fit: Indian domestic, UPI-era, IBS booking engine, no incumbent orchestrator.

</details>
