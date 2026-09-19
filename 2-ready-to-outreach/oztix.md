# Oztix

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 13 / 29 → 🟢 **Qualified**
**Industry:** Live-music, festival and venue ticketing (agent-of-promoter; collects from buyers, settles to organisers) · **HQ:** Brisbane, Australia — **Ticket Solutions Pty Ltd (ABN 94 106 907 206) trading as Oztix** · **Researched:** 2026-09-19 · **First email sent:** —
**Motion:** **Greenfield** — a **single** gateway, no orchestrator, no failover visible. Oztix's own privacy policy refers to the provider in the singular, twice.

---

> ## 🎯 THE HOOK — they blame their payment gateway for onsale failures, in writing, on their own help pages
>
> Oztix's **own privacy policy**, verbatim and **re-verified by me on 2026-09-19** at `https://www.oztix.com.au/privacy/`:
>
> > *"…we do not store your entire credit card number on our system, as this is held by **our financial institution and our payment gateway provider**."*
>
> And again in the disclosure list:
> > *"financial institutions (banks) and **our payment gateway provider**; and our other contractors…"*
>
> **Singular, both times.** One gateway carrying an entire national ticketing business through onsales — the single most bursty, most time-boxed traffic pattern in e-commerce.
>
> **And they have already told their customers what that costs.** The checkout FAQ attributes onsale failures to *"the payment gateway is experiencing high demand"* — Oztix pointing at its own single provider as the reason a customer could not buy. `[agent-sourced — see the verification note; I could not re-reach this page]`
>
> ### The second half — a card-on-file instalment product with no account updater
> **Pay Over Time** runs as a separate ASP.NET application at `payovertime.oztix.com.au`. **I confirmed it is the same merchant** — the page footer reads *"© 2026 **Ticket Solutions Pty Ltd** • Powered by Oztix"* — and the privacy policy confirms the rail, listing *"bank account details, **direct debit**, credit card details, billing address, **repayment information** and invoice details."*
>
> It takes a deposit and bills instalments against a stored card, with **no account updater and no self-service card update — the customer must phone 1300 762 545** — and, per the agent, a forfeiture clause if an instalment fails:
> > *"if… We are not able to process any of the instalments on their due date, Your reservation… will be cancelled and your deposit and any booking fee paid shall be forfeited."*
>
> ⚠️ **That quote is agent-sourced and I could NOT re-verify it** (see the verification note). **Do not put it in an email until someone reads it on the page.** If it holds, it is the sharpest line in the file: *an expired card silently forfeits a paid deposit on a festival ticket*.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Oztix is Australia's largest independent ticketing company, Brisbane-headquartered, founded ~2003, running its own Australian-hosted platform. It is **domestic-only**, which caps its ICP score hard — but the payment setup is a textbook greenfield case: **one gateway, no orchestrator, no failover, a card-on-file instalment product with no account updater, and a publicly-blamed gateway under onsale load.**

> ⚠️ **No SimilarWeb data was supplied** and none was obtained. Oztix is a single-market business, so the country profile is not load-bearing here — but two ICP signals were scored on entity evidence rather than traffic.

### Volume — **GATE CLEARS**
**Re-verified verbatim by me, 2026-09-19**, at `https://www.oztix.com.au/about/`. **The B2B-route technique worked again** — `/about/` is plain S3/CloudFront with no bot wall, while the consumer estate is a JS SPA.

> *"For over 20 years, we've partnered with **22,000+ event organisers** to deliver **33 million tickets** across music, venues, shows, sports, and government events nationwide."*
>
> *"By the numbers … **33,000,000+ tickets sold** · **22,000+ event organisers** · **7M+ ticket buyers** · 20+ years in events · Service company of the year 2025 Australian Event Awards"*

Two more figures the original pass missed, both first-party from the same page:
> *"Australia's largest attendee database **reaching 25% of the population**"*
> *"ISO 9001:2015 certified · **PCI DSS Level 2 compliant** · Australian Privacy Policy compliant · **99.99% SLA uptime** · Data Act compliant"*
> *"our platform is … built and continuously improved in-house by our **50+ full-time team** plus casual workforce nationwide"*

**Derivation:** 33M tickets over 20+ years is cumulative, so it must be annualised carefully. Three constructions give **~48,000–83,000 orders/month**. **Break-even for the 40,000/month gate is a basket of 2.99 tickets/order** — i.e. the gate only fails if the average Oztix order is three tickets or more, which is above the typical live-music basket of 2–2.5.

**Verdict: PASS**, with reasonable headroom. ⚠️ **Derived, not sourced** — Oztix publishes no order count.

### ⚠️ The stub's "~$30M revenue" has no source
The research found **no source whatsoever** for the figure carried in `accounts/apac-tal.csv` and the stub. **Treat it as fabricated until someone produces a source.** Do not carry it into outreach. *(Note: the identical "~$30M est." sits on the Peatix row too, where it was independently refuted as off by roughly an order of magnitude. Two unsourced $30M estimates on adjacent rows in the same vertical is a pattern worth distrusting.)*

### Accepted methods
| Method | Status | Detail |
|---|---|---|
| Visa | **CONFIRMED** | |
| Mastercard | **CONFIRMED** | |
| **Zip** | **CONFIRMED** | Present — note this is the opposite of Moshtix, which discontinued Zip |
| **Amex** | **SOURCED ABSENCE — explicitly refused** | *"Oztix doesn't accept AMEX® or Diners Club® cards"* ⚠️ **agent-sourced, NOT re-verified by me** |
| **Diners** | **SOURCED ABSENCE — explicitly refused** | same quote, same caveat |
| PayPal | **⚠️ CONTRADICTORY — UNRESOLVED** | Confirmed on the **legacy checkout**, absent from the **new FAQ**. Two estates disagree and neither was settled |
| **BECS direct debit** | **CONFIRMED** | Privacy policy lists *"bank account details, direct debit … repayment information"* — the Pay Over Time rail |
| Apple Pay / Google Pay | **NOT ESTABLISHED** | A Google Wallet case-study PDF exists but **has no text layer**. **Do not put Google Pay in an email** |
| PayTo / PayID / BPAY / POLi | **NOT FOUND** | Not established either way |

**Amex and Diners being *explicitly refused* is the unusual signal** — most Australian ticketing platforms accept Amex at a surcharge. A flat refusal points at acquirer economics or a gateway limitation, and it is a sourced absence rather than a gap, **if the quote verifies.**

### Merchant of record & entity
**Ticket Solutions Pty Ltd (ABN 94 106 907 206) trading as Oztix** — **re-verified by me** in the first line of the privacy policy: *"the expressions 'Oztix', 'we', 'us' and 'our' are a reference to **Ticket Solutions Pty Ltd (ABN 94 106 907 206)** trading as Oztix and its Related Bodies Corporate."* ABN independently verified at `abr.business.gov.au`. This is also the name on the buyer's statement, and the footer of the separate Pay Over Time app.

**Founders/directors named on `/about/`:** Stuart Field (Director, Founder), Brian Chladil (Director, Founder), Seth Clancy (Commercial).

### ⚠️ Two misattributions to avoid
1. **Bluesfest was MOSHTIX, not Oztix.** The Bluesfest BNPL case study (+14% AOV, $500+ average order) belongs to Moshtix and its LatitudePay integration. **Do not attribute it to Oztix in any email.**
2. **A "Growth Story Capital" ownership signal is unverified, undated and unsized.** Do not reference it.

</details>

<details>
<summary><h2>✉️ Section 2 — Full Outreach Sequence</h2></summary>

*Not yet generated. Run `/full-outreach Oztix`.*

**Before drafting, three things must be verified manually — none is safe to send as-is:**
1. **The Amex / Diners refusal quote.**
2. **The Pay Over Time forfeiture clause.**
3. **The "payment gateway is experiencing high demand" FAQ line.**

All three are agent-sourced and could not be re-reached. **What IS safe to lead on** — because I verified it myself — is the **singular "our payment gateway provider"** in the privacy policy, the **ABN/MoR structure**, the **direct-debit instalment rail**, and every figure on `/about/`.

</details>

<details>
<summary><h2>🔬 Section 3 — Full Research</h2></summary>

## ⚠️ Verification note — read this before using anything above

**Re-fetched and verified verbatim by me, 2026-09-19:**
- `https://www.oztix.com.au/about/` (HTTP 200, 307,046 bytes) — every volume figure, the compliance list, the team size, the 25%-of-population claim
- `https://www.oztix.com.au/privacy/` (HTTP 200, 247,249 bytes) — the singular gateway references (×2), the MoR entity and ABN, the direct-debit/repayment field list
- `https://payovertime.oztix.com.au/` (HTTP 200) — confirmed live and confirmed as the same merchant via its footer

**Could NOT be re-reached by me, and therefore remain agent-sourced only:**
- The **Amex / Diners refusal quote** — `oztix.com.au/faqs/` and `/faq/` both return a 5,024-byte JS shell with no content
- The **Pay Over Time forfeiture clause** — `payovertime.oztix.com.au/terms` and `/Home/Terms` both **404**; the app root renders only a reservation-timer widget
- The **"payment gateway is experiencing high demand"** checkout FAQ line

**The Zendesk help-centre-API technique that cracked Ticketek, Moshtix and eplus did NOT work here.** Both `oztix.zendesk.com/api/v2/help_center/...` and `help.oztix.com.au/...` return **404** — Oztix does not run Zendesk. The support estate is `oztix.com.au/contact/ticket-buyer-support/`, a JS SPA.

**This is a genuine gap, not a formality.** The three unverified claims are, between them, most of what would make a sharp email. They need a human with a browser before outreach.

## PSPs, gateways, acquirers

**No PSP name was established.** This is the central unanswered question.

- The privacy policy names the role but never the vendor: *"our financial institution and our payment gateway provider"* — twice, singular, unnamed.
- **CSP is `frame-ancestors` only** — no allowlist to mine for gateway hosts. (This is the technique that has named gateways on other accounts in this repo; it is unavailable here.)
- **PCI DSS Level 2** is self-declared on `/about/` — **verified by me**. Level 2 implies roughly 1–6M transactions/yr, which is an independent cross-check that broadly corroborates the derived volume band.
- **Pay Over Time is a separate ASP.NET application** on its own subdomain — a second estate, and a second integration surface.

**Not found / not established:** Stripe, Adyen, Braintree, Checkout.com, eWAY, Windcave, Tyro, Pin Payments, Fat Zebra, CommWeb/MPGS, Worldpay, Cybersource. **Absence here is weak evidence** — unlike Moshtix, no un-WAF'd production bundle was located, so nothing was swept directly.

## Orchestration — none detected
No orchestrator was found, and the privacy policy's **singular** "payment gateway provider" is affirmative evidence for a single direct integration rather than merely an absent hit. **Classification: greenfield.**

⚠️ **Weaker evidence than Moshtix or Peatix**, where production bundles were grepped directly. Here the classification rests on a first-party document's phrasing, not on code.

## 4. ICP Score breakdown — 13 / 29

| Signal | Weight | Score | Basis |
|---|---|---|---|
| Transaction volume | 5 | **5** | ~48k–83k orders/month derived; break-even basket 2.99 tickets. PCI Level 2 corroborates |
| Orchestration (greenfield) | 4 | **4** | Single unnamed gateway, no orchestrator. On the privacy policy's singular phrasing |
| 3+ countries | 3 | **0** | **Australia only** |
| Multiple PSPs | 2 | **0** | **One gateway** — the single-PSP dependency is the hook, but it scores zero on this row |
| Local rail gap | 3 | **2** | Amex and Diners refused; PayTo/BPAY/PayID/POLi not found; Apple/Google Pay unestablished. Partial, and partly unverified |
| Recent expansion | 2 | **0** | None found |
| Payment issues | 2 | **2** | Gateway publicly blamed for onsale failures; Pay Over Time has no account updater and no self-service card update |
| Funding | 2 | **0** | "Growth Story Capital" unverified, undated, unsized |
| Traffic outside home market | 2 | **0** | Domestic only |
| Competitor orchestration | 2 | **0** | Moshtix runs a hand-built router, not a third-party orchestrator; Ticketek runs Softix PayGate |
| Job postings | 2 | **0** | Not established |
| **TOTAL** | **29** | **13** | 🟢 **Qualified** |

**Scored honestly, the single-gateway dependency costs Oztix 2 points on the "multiple PSPs" row while being the strongest thing about the account as a sales target.** That is the matrix working as designed — it measures stack complexity, not opportunity — but it is worth naming so nobody reads 13/29 as "weak account."

## 5. What could NOT be established
1. **The gateway's name** — the central question. No CSP allowlist, no un-WAF'd bundle, no Zendesk corpus.
2. **The three agent-sourced quotes** above — Amex/Diners, the forfeiture clause, the high-demand FAQ line.
3. **The PayPal contradiction** between the legacy checkout and the new FAQ. Two estates disagree; neither was settled.
4. **Apple Pay / Google Pay.** The Google Wallet case-study PDF has **no text layer**. **Do not put Google Pay in an email.**
5. **Ownership** — the "Growth Story Capital" signal is unverified, undated and unsized.
6. **Any revenue figure.** The stub's ~$30M has no source.
7. **Complaint channels** — ProductReview, Reddit and the app stores were not reached for Oztix.

## 6. Overall Research Confidence — **MEDIUM**

**High** on volume, entity, MoR, compliance posture and the single-gateway classification — all re-verified by me against first-party pages.

**Downgraded to Medium because the gateway is unnamed, three of the sharpest claims could not be re-reached, and the PayPal contradiction is unresolved.** Oztix's consumer estate is a JS SPA with no Zendesk corpus and no mineable CSP, so the techniques that worked on Ticketek, Moshtix, eplus and KKday all failed here. **Closing this account properly needs a human with a browser, not another agent run.**

</details>
