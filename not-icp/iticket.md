# iTICKET

**Status:** 🔴 Not ICP — under 40k monthly transactions
**ICP Score:** not scored → **volume gate fired before scoring**
**Industry:** Event ticketing (community, theatre, festivals) · **HQ:** Kingsland, Auckland, **New Zealand** — ITICKET.CO.NZ LIMITED, founder-owned · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** n/a — rejected at Phase 0

---

> ## 🔴 REJECTED ON THE VOLUME GATE — and the binding constraint is their own traffic number
>
> **✅ Verified by me directly** on iTICKET's own promoter site, `hello.iticket.co.nz`:
>
> > **10M+** Tickets sold · **3k+** Event & venue partners · **185k+** Monthly website visitors · **20+** Years of experience
>
> **The 185,000 monthly visitors figure is what settles it**, because it caps orders regardless of any other assumption:
>
> | Visitor→order conversion | Orders/month |
> |---|---|
> | 5% | 9,250 |
> | 10% | 18,500 |
> | 15% | 27,750 |
> | **20%** | **37,000 — still under** |
>
> **To clear 40,000 you would need more than 21.6% of every unique monthly visitor to complete a paid order** on a public what's-on browsing site. That is not credible; ticketing converts well but nowhere near that.
>
> **A second, independent derivation agrees.** 10M tickets over 22 years = ~455,000 tickets/year; at a 2.5-ticket NZ basket that is ~182,000 orders/year = **~15,200/month**. Even skewing hard to recent years — assuming the current year alone is 10% of all lifetime volume, aggressive for a 22-year-old business — and taking a small 2.0 basket gives ~41,700/month, **the only construction that clears the bar, and it needs both aggressive assumptions at once.**
>
> **A third cross-check agrees again.** ~1,200–1,250 distinct event pages per year (counted from the Wayback CDX index: 1,202 in 2024, 1,249 in 2025) × ~200 tickets per event ÷ ~2.5 per order ≈ **8,300/month**.
>
> **Three independent methods land between ~8k and ~25k against a 40,000 floor.** New Zealand is a market of 5.3 million and iTICKET is explicitly not the leader — its own positioning is *"challenging the big multinationals"*, alongside Ticketmaster NZ and Ticketek NZ.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** iTICKET is an independent, founder-owned New Zealand ticketing platform operating since 2004, with 40 physical outlets and a separate Australian business launched in 2012. **Healthy and independent — this is a size rejection, not a distress rejection.**

### Accepted methods — first-party, stated identically on two pages
> *"The only platform that accepts **all major credit cards, eftpos, bank transfers, Afterpay and flexible instalments via PayPlan**."*

**Sourced absence** from that exhaustive list: **POLi · Laybuy · Zip · PayPal**. ⚠️ **Amex, Apple Pay and Google Pay are unchecked-absence** — marketing copy often omits wallets, and the checkout could not be reached.

📌 **They run their own BNPL-equivalent — PayPlan** (deposit plus weekly/fortnightly/monthly instalments on a stored card) — **alongside** Afterpay, rather than adding Laybuy or Zip.

### The architecture is genuinely interesting, and worth keeping on file
| Finding | Detail |
|---|---|
| **Two card gateways side by side** | *"processed using **Stripe or Worldline**"* — ⚠️ `[UNVERIFIED — search summary of iticket.co.nz/legal/privacy; page could not be fetched]`. Worldline NZ is the former **Paymark**. |
| **Dual merchant-of-record model** | Transactions run **either** through iTICKET's own merchant account (funds held in trust, iTICKET handles refunds) **or** through the promoter's own merchant account (funds go direct, iTICKET disclaims refund liability) — **and the two are visually distinguished at checkout.** ⚠️ `[UNVERIFIED — search summary of their T&Cs]` |
| **Card-on-file vaulting + MIT** | PayPlan deposits are *"securely tokenised and stored by iTICKET's third-party payment processor"*, with scheduled instalments auto-charged. ⚠️ `[UNVERIFIED]` |
| **Windcave / Payment Express** | ✅ **Confirmed historically** — `paymentexpress.com/iticket` is live with a dedicated client page, while `windcave.com/iTICKET` **404s**. **[INFERENCE, not confirmed]** they migrated off it. |
| **Settlement** | ✅ First-party: *"Fast post-event settlement — with funds transferred within days."* Funds held in trust for the iTICKET-MOR share only. |

> **Had the gate not fired, that dual-MOR router would have been the pitch** — a homegrown per-merchant routing decision with two different liability models. **It is the most interesting architecture in either batch and it belongs to the smallest company in either batch.**

### Cross-border — effectively nil, which independently weakens the fit
A **separate Australian entity** (ABN 49 160 384 403, Melbourne) on a separate domain, in AUD, with a narrower method set (*"Credit Card, Layby"*). **NZD on `.co.nz`, AUD on `.com.au` — two domestic businesses rather than one cross-border one.** No multi-currency pricing, no FX messaging, and no mention of foreign card issues anywhere. **Our lead value proposition has almost no surface here.**

### Corporate
**ITICKET.CO.NZ LIMITED**, incorporated 12 Jan 2004, NZBN 9429035589419. **Sole director and 100% shareholder: Reece Stuart Preston** (Founder & CEO), via a normal family-trust vehicle — **no corporate parent**. Co-founder Phillip Jobbins ceased as director 24 May 2019. iTICKET **sat out** the 2013 NZ ticketing consolidation. ⚠️ `[UNVERIFIED — Companies Office mirrors, not the registry itself]`

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

**None, and none should be generated.** `/full-outreach` must never run on a rejected company.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### Why this was not scored on the 29-point matrix
The volume gate sits at **Phase 0**, before scoring — same treatment as Fly91 in this batch. A number on the matrix would imply a comparability the account does not have.

### Source Notes
- ✅ **The decisive figures were verified by me directly** on `hello.iticket.co.nz` — **10M+ tickets, 3k+ partners, 185k+ monthly visitors, 20+ years** — as was the payment-method sentence, which appears identically on two separate pages of their own B2B site and is therefore treated as exhaustive.
- ✅ **The main site's inaccessibility was reproduced by me**: `www.iticket.co.nz` returns **HTTP 429**. The promoter site `hello.iticket.co.nz` is **not** behind that wall and returns 200 — **that split is the technique that made this account researchable at all, and it is worth remembering for other bot-walled merchants.**
- ✅ **`paymentexpress.com/iticket` is live and `windcave.com/iTICKET` 404s** — fetched by the agent.
- ⚠️ **Stripe and Worldline are NOT confirmed.** Reproduced across two independent search queries and tied to a specific first-party URL, so likely true, but **the page was never loaded. Do not state it as fact.**
- ⚠️ **The dual-MOR model, the trust-account language, the tokenisation clause and the corporate registry details are all search-summary only.** The T&Cs and privacy pages are behind the same 429 wall and **have no Wayback snapshots** — and the Internet Archive went fully offline partway through the run.
- ⚠️ **The ~NZ$5.3m revenue figure is a RocketReach aggregator estimate.** Not a filing. NZ does not publish financials for a private company of this type.
- ⚠️ **The event-count derivation is the agent's own**, from the Wayback CDX index. It independently corroborated their "3k+ partners" claim by finding 3,486 unique venue pages across 225 NZ towns — **a good validity check on the method**, which is why the event counts are usable.
- ❌ **Nothing from the live site could be inspected** — no CSP headers, no JS bundles, no checkout HTML, no gateway hostnames, and **no live count of events on sale**, which was the one input specifically requested.
- 📌 **Absence of complaints is weak evidence here.** No Trustpilot page exists for `iticket.co.nz` (the Trustpilot hits are `iticket.uz`, `iticket.law` and `etickets.com` — **different companies, and an easy false positive**). The quiet mostly reflects low consumer volume, which is itself consistent with the size verdict.

## Rejection Rationale

iTICKET's own first-party numbers — **185,000 monthly website visitors** and **10 million tickets sold across 22 years** — cap monthly transactions well below the 40,000 floor under every plausible construction; clearing the bar would require more than 21.6% of every unique monthly visitor to complete a paid order, and three independent derivations (traffic, lifetime volume, and event count) land between roughly 8,000 and 25,000 a month. The fit is further weakened by the near-total absence of cross-border surface: New Zealand and Australia run as two separate domestic entities on separate domains in separate currencies, with no multi-currency pricing and no foreign-card issues documented anywhere.

> ### 📌 WORTH KEEPING ON FILE ANYWAY
> The **dual merchant-of-record model** — per-transaction routing between iTICKET's own merchant account and the promoter's, with different refund liability on each side and a visual distinction at checkout — is the most interesting payment architecture found in either batch. **If iTICKET is ever acquired into a larger ANZ ticketing group, that group inherits this and the account becomes immediately relevant.** Single decision-maker throughout: Reece Preston owns 100%.

</details>
