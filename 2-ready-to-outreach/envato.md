# Envato

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 20 / 29 → ⭐ **High Priority**
**Industry:** Digital-goods marketplace + creative subscription (two-sided) · **HQ:** Melbourne, Australia — **wholly owned by Shutterstock, Inc. (NYSE: SSTK) since 22 July 2024** · **Researched:** 2026-09-17 · **First email sent:** —
**Motion:** **Greenfield** — two hard-coded, single-PSP-per-surface integrations with no routing layer. The classification is affirmative, not a "couldn't find" (see 3B).

---

> ## 🎯 THE HOOK — they diagnosed it themselves, in writing
>
> From Envato's own troubleshooting page, verbatim:
>
> > *"Check for international transaction blocks — **since Envato is Australia-based, some card issuers block overseas payments by default** until you approve them directly with your bank."*
>
> And from their own Accepted Payment Methods page:
>
> > *"If you need a payment method that isn't currently available—**especially a regional payment provider specific to your country**—please get in touch with our support team to let us know."*
>
> A global marketplace billing **USD-only** off a **single PayPal-family gateway**, telling its own buyers that their cards get blocked because of where it acquires, and publicly inviting requests for local rails. **You can quote them to themselves.**
>
> ⚠️ **But read the territory flag first — the contracting entity is now Shutterstock, Inc.**

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Envato runs **Envato Elements** (creative-asset subscription) and the **Envato Market** marketplaces — ThemeForest, CodeCanyon, VideoHive, AudioJungle, GraphicRiver, PhotoDune — selling digital goods worldwide and paying out to a global author base. It is genuinely two-sided: money in from buyers in USD on four card brands plus PayPal, and money out to **42,000+ earning authors across 173 countries** in **137 currencies**.

**SimilarWeb total visits:** **~5.79M/month combined across five domains** (Aug 2026) — `[ESTIMATE, not confirmed]`, free-tier panel data, and a **floor**: four further Envato domains were not covered.

> ⚠️ **Aggregation mattered enormously here.** On themeforest.net alone India reads **19.57%**; across the combined estate it falls to **14.67%**, because Elements — 62% of all traffic — skews toward the US, Brazil and Mexico. A single-domain read would have overstated India by a third. **58.1% of traffic is unattributed** (free tier exposes only top-5 countries per domain), so every share below is a floor.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | **India** | **14.67%** `[EST]` | Visa, Mastercard, Amex USD-only, PayPal (+Apple Pay on Elements) — **USD only** | **UPI, netbanking, RuPay, EMI, UPI Autopay — SOURCED ABSENT** | ❌ none |
| 2 | **United States** | **11.67%** `[EST]` | As above | — | ✅ Envato USA, Inc. (Utah) |
| 3 | **Indonesia** | **4.73%** `[EST]` | As above | **QRIS, GoPay, OVO, DANA, ShopeePay, virtual account — SOURCED ABSENT** | ❌ none |
| 4 | Brazil | 2.91% `[EST]` | As above | Pix, boleto — sourced absent | ❌ none |
| 5 | **Pakistan** | **2.17%** `[EST]` | As above | JazzCash, Easypaisa — sourced absent | ❌ none |

*Also: Mexico 2.49%, Bangladesh 0.88%, Russia 0.79%. **58.1% unattributed.** Australia — the HQ — does not appear at all.*

### Legal entities
- **Shutterstock, Inc.** (NYSE: SSTK) — ⚠️ **the contracting entity in Envato's current terms.** Envato Market User Terms, rev. **14 Aug 2026**, define *"Envato, we, us or our"* as **"Shutterstock, Inc."** Same in the Elements User Terms and the Elements Author Terms (rev. 1 Jul 2026)
- **Envato Pty Ltd** — ABN 11 119 159 741, Level 3, 551 Swanston St, Carlton VIC 3053. **Survives only in residual roles** — DMCA copyright agent and a creator-programme contract
- Acquisition **completed 22 July 2024**, US$245m cash

### Known PSPs
- **Braintree** (PayPal-owned) — ✅ **the card gateway across both properties.** Affirmative evidence: the checkout-scoped **Content-Security-Policy** on `themeforest.net/checkout` and `codecanyon.net/checkout` allowlists `*.braintree-api.com`, `*.braintreegateway.com` and `*.paypal.com` — **and nothing else payment-related**. Corroborated in Envato's own words: their failed-payments page sends declined buyers to the *"**Braintree Prohibited Transactions** page"*
- **PayPal** — ✅ confirmed, both properties
- **Stripe** — ✅ confirmed on the newer subscription/account layer: *"you are sent to a **Stripe Invoice page**… This is an official invoice for your Envato subscription, **which is managed by Stripe**."* `account.envato.com` serves a CSP allowlisting `js.stripe.com` and `api.stripe.com` — **and no Braintree**
- **Trolley** (trolley.com) — ✅ **the payouts and tax-compliance provider**, named by Envato itself: *"Envato transitioned to a new tax compliance system managed by our third-party provider, **Trolley**"*
- ❌ **No ANZ-domestic gateway anywhere** — no eWAY, Pin Payments, Windcave, Tyro or Airwallex in any CSP or source

### Orchestration status
**None detected — direct PSP integrations only (greenfield).** Zero hits against Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY and Yuno.

> **This is an affirmative finding, not an absence of evidence.** The checkout CSP allowlists exactly one gateway family. An orchestrator would surface its own domain in `connect-src`/`frame-src`, or several PSP hosts. Neither appears. The architecture is **two hard-coded single-PSP integrations** — Braintree on the legacy marketplace, Stripe on the newer account layer — which is the problem orchestration solves, not a solution to it.

### Buying signals
- 💥 **Getty/Shutterstock merger ABANDONED — Getty terminated 7 July 2026**, after the UK CMA required divestiture of Shutterstock's entire editorial business (15 May 2026) and Getty's board declined (30 June 2026). **Shutterstock is standalone again and needs Envato — the growth asset it paid US$245m for — to perform**
- 💸 **Shutterstock booked a $173.7m goodwill impairment in Q2 2026** after the Getty termination, and fair-valued its entire single reporting unit at **$363.7m** — *less than twice what it paid for Envato alone*. Parent revenue **−17% YoY**; subscribers down to **951,000** from 1,073,000
- 📉 **Envato cut ~200 roles, ~30% of its workforce, in March 2026** across Australia, New Zealand, Mexico and the US `[UNVERIFIED — search summary only]`. **Fewer engineers to build payment integrations in-house — buy-vs-build tilts toward buy**
- 🔄 **Tax and payout systems are already being consolidated into Shutterstock**: *"We are aligning how royalty withholding tax (RWT) works on Envato payments with Shutterstock"*, first affected payout **September 2026**. A live integration programme is running right now
- 🗣️ **They publicly solicit regional payment methods** on their own help page — see the hook above
- 📋 **No public payment RFP found.** No payments engineering roles found — the Greenhouse board is retired (404) and Glassdoor shows 2 open positions company-wide

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Envato` to draft the 12-touch sequence — **after resolving the territory question in Section 3.***

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 20 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+3** | ✅ **DERIVED from Envato's own public counter — ~59,000/month current run-rate, ~97,000/month trailing twelve months.** Envato Market publishes a live cumulative `items sold` figure in its footer. **I verified it reads byte-identical across themeforest.net, codecanyon.net, audiojungle.net and videohive.net** (`78,946,574` at 2026-09-17), which proves it is group-wide, not per-domain. Differenced against archived snapshots to get a rate. **Billing unit: per-item marketplace purchases.** ⚠️ **This EXCLUDES Envato Elements subscription renewals, which are not published in any form.** Total transactions are therefore higher and plausibly ≥100,000 — **but only the Market half is established, so the band is scored on that.** |
| Orchestration status | **+4** | ✅ **None detected — affirmative CSP evidence**, not a failed search. |
| 3+ countries | **+3** | ✅ Sells worldwide; pays authors in **137 currencies across 173 countries**; entities in Australia and the US. |
| Multiple PSPs | **+3** | ✅ **Braintree** (marketplace card) + **PayPal** (wallet) + **Stripe** (subscription/account layer) + **Trolley** (payouts). All first-party sourced. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Now awarded — traffic was obtained late in the run and closed the gap.** Aggregated across five Envato domains, **India is the #1 market at 14.67%** and **Indonesia #3 at 4.73%**. **UPI is absent from Envato's enumerated accepted-method list**, as is QRIS. Both absences are sourced against a closed first-party enumeration, in markets now ranked. |
| Recent expansion | **0** | ❌ No new market entry. The 2026 events are a *contraction* (~30% headcount) and an abandoned merger. |
| Payment issues reported | **+2** | ✅ **Trustpilot 2.2/5 across 9,044 reviews**, plus a concrete checkout-integrity defect quoted below, plus Envato's own documented cross-border decline problem. |
| Funding >$10M | **0** | ❌ Wholly owned by a public parent; no round. |
| High traffic outside home | **+2** | ✅ **Now evidenced, not inferred:** Australia does not appear in the top markets at all. India 14.67%, US 11.67%, Indonesia 4.73%, Brazil 2.91%, Mexico 2.49%, Pakistan 2.17%, Bangladesh 0.88%. |
| Competitor using orchestration | **0** | ❌ None confirmed. **And the brief's merchant-of-record hypothesis was tested and NOT established** — no evidence any competitor uses Paddle, FastSpring or Lemon Squeezy. Do not assert it. |
| Payment job postings | **0** | ⬜ None found; the jobs board is retired. |

**Tier:** **20 / 29 → ⭐ High Priority.** No analyst override applied.

> **Why no override, in either direction.** The app-store trap does not apply — this is web checkout, not IAP. Volume is assumed rather than sourced, but assumptions cannot carry an account, and the other 14 points stand on first-party evidence. **The honest caveat is territory, not score** — see below.

---

### ⚠️ TERRITORY — resolve before outreach

| Factor | Points to |
|---|---|
| Operating site, staff, brand: **Melbourne** | **APAC** ✅ |
| **Contracting entity in current terms: "Shutterstock, Inc."** | **AMER** ❌ |
| Arbitration venue: **New York** | AMER ❌ |
| Tax/payout systems **being aligned to Shutterstock** as of Sept 2026 | AMER ❌ |
| Envato Pty Ltd reduced to **DMCA agent + one creator contract** | AMER ❌ |

**My read:** Envato remains an APAC-HQ'd *operating* entity and is defensible as in-territory, but the payments counterparty is a US-listed parent and a consolidation programme is visibly running. **Check with AMER whether Shutterstock, Inc. is already owned elsewhere on the account list before spending a sequence here.** An APAC-personalised email sent into a Shutterstock payments org will land wrong.

### Source Notes
- ✅ **Envato's three help centres reached via the open Zendesk API** — `help.market.envato.com`, `help.author.envato.com`, `help.elements.envato.com`, `/api/v2/help_center/en-us/articles.json`. **455 articles pulled and parsed by me.** The HTML 403s; the API does not. Same technique that cracked Indodax and Azar.
- ✅ **`envato.com` 301-redirects to `elements.envato.com`** — recorded because a domain that redirects is not a separate property, and any traffic attributed to it is an artefact.
- ✅ **Checkout CSP evidence** — the affirmative basis for the greenfield classification.
- ⚠️ **No traffic data.** Not supplied, no MCP tools, fallback not accepted. This costs 3 ICP points (see the rail-gap row).
- ❌ **Four substring false positives caught and killed** before they reached this file. A raw count over the corpus returned `SEPA` ×101, `Pix` ×27, `UPI` ×13 and `iDEAL` ×9. **Every one was noise:** "separate", "pixel", and — for all nine `iDEAL` hits — the English adjective, e.g. *"Pictorial guides are ideal."* **Envato supports none of those four.**
- ❌ **A "$2 handling fee" figure was surfaced and excluded as current** — it comes from 2018 forum posts. The 2025 help article confirms a fee exists under $150 but **does not state the amount**.
- ❌ **The competitor merchant-of-record hypothesis was tested and failed.** Paddle and FastSpring are MoR vendors; **no evidence any Envato competitor uses one.**

### Success Case Alternatives
- **Chosen on payment pattern:** a two-sided global digital-goods marketplace, USD-only presentment, single card gateway, low-ticket high-frequency. Any case must be verified against a published source before use — this repo has already corrected one case-study misattribution.

---

## Executive Summary

Envato is a two-sided digital-goods business — Envato Elements (subscription) plus six Envato Market marketplaces — HQ'd in Melbourne and **wholly owned by Shutterstock since July 2024**. Buyers pay in **USD only**, through **four card brands, Apple Pay (Elements only) and PayPal**, on a **single PayPal-family gateway (Braintree)**, with **Stripe** on the newer subscription/account layer and **no local payment method anywhere in the world**. Meanwhile Envato pays its authors in **137 currencies over 83 local clearing routes** — it has solved localisation for money *out* and not for money *in*. The motion is **Greenfield**, confirmed affirmatively from checkout CSP headers, and the sharpest asset is that Envato's own help pages both diagnose the cross-border decline problem and invite requests for regional providers.

### Section 1: Website Traffic Analysis by Country

**Data source: WebSearch fallback against SimilarWeb, aggregated across five domains.** Path 3 of 3 — everything here is `[ESTIMATE, not confirmed]`.

| Rank | Country | Share of combined | Est. monthly visits | Source |
|---|---|---|---|---|
| 1 | **India** | **14.67%** | ~848,800 | SimilarWeb Aug 2026 `[EST]` |
| 2 | **United States** | **11.67%** | ~675,000 | `[EST]` |
| 3 | **Indonesia** | **4.73%** | ~273,900 | `[EST]` |
| 4 | Brazil | 2.91% | ~168,300 | `[EST]` |
| 5 | Mexico | 2.49% | ~144,200 | `[EST]` |
| 6 | **Pakistan** | 2.17% | ~125,400 | `[EST]` |
| 7 | **Bangladesh** | 0.88% | ~51,100 | `[EST]` |
| — | **Unattributed** | **58.1%** | ~3,363,200 | free-tier limit |

**Domain mix** (visits/month): elements.envato.com 3.567M (61.6%) · themeforest.net 1.100M (19.0%) · codecanyon.net 0.567M (9.8%) · audiojungle.net 0.295M (5.1%) · videohive.net 0.258M (4.5%). **Combined ~5.79M/month.**

> ⚠️ **Three limits, all material.** (i) The free tier exposes only the **top five countries per domain**, so **58.1% is unattributed** and every share is a **floor**, not a point estimate. (ii) Only **five of nine** Envato domains were covered — graphicriver.net, photodune.net, envato.com and tutsplus.com are missing, so the total is also a floor. (iii) This is modelled panel data, not Envato's analytics.

> 💡 **Aggregation changed the answer.** On themeforest.net alone India reads **19.57%**; across the estate it is **14.67%**, because Elements (62% of traffic) skews to the US, Brazil and Mexico. Reading one domain would have overstated India by a third — exactly the distortion the method warns about.

**APAC markets in territory — India, Indonesia, Pakistan, Bangladesh — are at least ~22.5% of attributed visits**, and certainly more given the unattributed majority.

> ⚠️ **Traffic is not revenue, and here the two diverge sharply.** Shutterstock's Q2 2026 10-Q reports revenue as **North America 53.2%, Europe 26.7%, rest of world 20.1%** — group-wide, with APAC not separated. **India and Indonesia drive volume; North America drives money.** A classic high-traffic / low-ARPU emerging-market skew. Do not present traffic share as revenue share.

### Section 2: Legal Entities & Local Presence

**Headquarters:** Melbourne, Australia. Envato founded 2006.

| Country | Entity | Registration | Source |
|---|---|---|---|
| **USA** | **Shutterstock, Inc.** — ⚠️ **the contracting party in current terms** | NYSE: SSTK | [Envato Market User Terms, rev. 14 Aug 2026](https://help.market.envato.com/hc/en-us/articles/41383541904281-Envato-Market-User-Terms) |
| Australia | Envato Pty Ltd | **ABN 11 119 159 741** | Envato Market IP Policy |

**Cross-Border Gap Analysis:**

| Market | Top market? | Local entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---|---|---|---|---|
| **Worldwide** | Unknown — no data | ❌ none outside AU/US | Not verified | **High — and self-documented** |

> *"Warning: Envato operates a single USD-only checkout worldwide with no local billing entity outside Australia and the United States. Transactions are processed cross-border, with higher scheme costs, lower approval rates and FX exposure."*
>
> **This is not an inference — Envato says it.** *"since Envato is Australia-based, some card issuers block overseas payments by default."*

> ⚠️ **No regulatory acquiring gate is asserted.** None was verified this run.

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Surface | Provider | Evidence Type | Source |
|---|---|---|---|
| **Envato Market** (6 marketplaces) | **Braintree** + **PayPal** | `[Source Code]` — checkout CSP allowlists `*.braintree-api.com`, `*.braintreegateway.com`, `*.paypal.com` and nothing else payment-related | `themeforest.net/checkout`, `codecanyon.net/checkout` |
| **Envato Elements** | **Braintree** | `[Terms/Privacy Policy]` — *"see the **Braintree Prohibited Transactions** page"* | [Failed payments](https://help.elements.envato.com/hc/en-us/articles/4411385939225-Failed-payments) |
| **Elements / account layer** | **Stripe** | `[Terms/Privacy Policy]` + `[Source Code]` — *"managed by Stripe"*; `account.envato.com` CSP allowlists `js.stripe.com`, `api.stripe.com`, **no Braintree** | [Invoices article](https://help.elements.envato.com/hc/en-us/articles/360000621523-How-to-View-Download-Invoices-on-Envato) |
| **Author payouts** | **Trolley** | `[Terms/Privacy Policy]` — named by Envato itself | [Tax Form Troubleshooting](https://help.author.envato.com/hc/en-us/articles/61599514214169-Tax-Form-Troubleshooting-Help) |

**Merchant of record — a nuance that matters.** Envato is **not** a full MoR; it is an **expressly limited agent**. Terms, verbatim: *"**WE DO NOT PROCESS PAYMENTS FOR ANY ENVATO MARKET SERVICES.**… we may use one or more third-party payment processors"* and *"we receive that payment as a **limited agent for the Author**."* The one exception: *"For EU VAT purposes only, **Envato steps into the supply chain as the supplier on record**."*

⚠️ **Open question:** whether **Stripe or Braintree acquires Elements subscription volume today.** Both are live simultaneously — Braintree for declines and restrictions, Stripe for invoices and the account-layer card form. A migration may be in progress. This needs a logged-in checkout observation.

#### 3B. Payment Orchestrator

**None detected — direct PSP integrations only (greenfield).**

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with PSPs, which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

**The evidence is affirmative.** The checkout CSP allowlists exactly one gateway family; `account.envato.com` allowlists only Stripe. An orchestrator would appear in `connect-src` or `frame-src`. **Two hard-coded, single-PSP-per-surface integrations, no routing, no failover, no vault portability.**

> **MANUAL:** walk both checkouts logged in, with DevTools open. That settles the Stripe-vs-Braintree question for Elements in minutes.

### Section 4: Alternative & Local Payment Methods

**Two enumerated first-party lists exist, so absences here are SOURCED.**

| Surface | Method | Category | Status | Source |
|---|---|---|---|---|
| **Elements** | Visa, Mastercard | Cards | **Active** | [Accepted Payment Methods](https://help.elements.envato.com/hc/en-us/articles/360000621543-Accepted-Payment-Methods) |
| Elements | **American Express — USD only** | Cards | **Active, currency-restricted** | Same |
| Elements | **Apple Pay** | Wallet | **Active** (Safari desktop only) | Same |
| Elements | PayPal | Wallet | **Active** | Same |
| **Elements** | **Google Pay** | Wallet | ❌ **SOURCED ABSENT** — *"Google Pay is not currently accepted on Envato"* | Same |
| **Elements** | **Skrill** | Wallet | ❌ **SOURCED ABSENT — explicitly refused** | Same |
| Elements | Wire transfer, invoice billing | Bank | ❌ **Enterprise plans only** | Same |
| Elements | Amex in EUR | Cards | ❌ **Explicitly refused** | Same |
| **Market** | PayPal, Visa, Mastercard, Amex | Cards/wallet | **Active — USD only** | [How do I purchase an item](https://help.market.envato.com/hc/en-us/articles/203269700-How-do-I-purchase-an-item-on-Envato-Market) |
| **Market** | **Apple Pay** | Wallet | ❌ **Absent — and note it DIFFERS from Elements** | Same |
| **Everywhere** | **UPI, QRIS, GoPay, OVO, DANA, ShopeePay, GCash, Maya, PromptPay, FPX, DuitNow, Touch 'n Go, MoMo, PayNow, konbini, Alipay, WeChat Pay, iDEAL, boleto** | All local rails | ❌ **ABSENT from both enumerated lists** | Both |
| **Home market (AU)** | **PayTo, BPAY, POLi, Afterpay, Zip** | A2A/BNPL | ❌ **Absent from the enumerated lists** | Both |

> **Warning: Envato operates six marketplaces and a global subscription with ZERO local payment methods in any market, including its own.** The lists are closed enumerations, so this is sourced absence — not an unchecked gap.

> 💡 **And they know.** Verbatim, same page: *"If you need a payment method that isn't currently available—**especially a regional payment provider specific to your country**—please get in touch with our support team to let us know. We always welcome your feedback."*

**Envato Credits — resolved: dead since 2018.** Envato removed stored-value credits on **2 October 2018**; residual balances expired by Oct 2019. So the business moved from a deposit model (one large transaction, many small draws) to **per-transaction authorisation on every purchase** — the profile where approval-rate optimisation compounds. Note also that **Skrill was accepted in 2018 and is now explicitly refused**: the method set has been *narrowing*.

⚠️ **Do not confuse with "Envato AI Credits"** — a 2025/26 usage allowance for AI generations, not stored value and not a payment method.

**The asymmetry that is the best non-accusatory opener.** On the payout side, Envato states: *"Envato now offers bank transfers into **137 currencies, 83 of which are transferred via local routes called International Automated Clearing Houses (IACHs)**"* — local-currency landing in 1–2 days. **They already believe in localisation. They have applied it to exactly one direction of the flow.** Both halves are first-party sourced from the same help centre.

### Section 5: Payment Issues & Customer Complaints

| Issue | Evidence | Source | Confidence |
|---|---|---|---|
| **Overall sentiment** | **TrustScore 2.2 / 5 across 9,044 reviews** | trustpilot.com/review/www.envato.com | ✅ fetched |
| **Checkout integrity defect** | *"I had to refresh the checkout page due to a bug and without knowing it **changed my monthly subscription to an annual one** and they are refusing to downgrade"* (15 Aug 2026) | Same | ✅ |
| Auto-renewal + refund refusal | *"when your subscription automatically renews at the full, exorbitant price, they refuse to issue a refund"* (20 Aug 2026) | Same | ✅ |
| AI credit repricing backlash | *"a video generation that previously cost 1 generation now costs 6 credits… roughly a 70% reduction"* (19 Aug 2026) | Same | ✅ |
| **Cross-border card blocks** | Envato's own diagnosis — *"since Envato is Australia-based, some card issuers block overseas payments by default"* | [Common PayPal and credit card issues](https://help.market.envato.com/hc/en-us/articles/202821550-What-are-common-PayPal-and-credit-card-issues-on-Envato-Market) | ✅ first-party |
| **Sanctions/region blocking** | *"If your payment has been identified by our providers as **originating from a region that is subject to these restrictions**, you won't be able to finalize your purchase"* | Market help centre | ✅ first-party |
| Author payout failures | **No evidence of a systemic 2025–26 payout problem.** SLA is 1–5 business days | help.author.envato.com | ✅ **verified absence — do NOT claim payout problems** |

> **Honest read, and it matters for the drafting.** The *loud* 2026 complaints are about **AI credit repricing and refund policy**, not declines. **Do not open with "your buyers can't pay you"** — that specific claim is unverified. Open with the method gap and the payout/pay-in asymmetry, both of which are documented.

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | **2026-09** | **Royalty withholding tax on Envato payments being aligned with Shutterstock**; first affected payout Sept 2026 | Systems consolidation | [Upcoming Tax Changes](https://help.author.envato.com/hc/en-us/articles/59238290478361-Upcoming-Tax-Changes-July-2026) ✅ |
| 2 | **2026-07-07** | **Getty terminates the Shutterstock merger agreement** | M&A — **ABANDONED** | Form 425 / SEC ✅ |
| 3 | **2026-05-15** | UK CMA conditions clearance on divesting Shutterstock's entire editorial business | Regulatory | CMA ✅ |
| 4 | **2026-03** | **Envato cuts ~200 roles (~30% of workforce)** across AU, NZ, MX, US | Restructuring | smartcompany.com.au `[UNVERIFIED]` |
| 5 | **2024-07-22** | **Shutterstock completes acquisition of Envato**, US$245m; +650k subscribers → 1.15m group total | M&A — **COMPLETED** | [PR Newswire](https://www.prnewswire.com/news-releases/shutterstock-completes-acquisition-of-envato-302203152.html) ✅ |

**Public payment RFP:** *No public payment-related RFP found.*
**Payment hiring:** **None found.** The Greenhouse board is retired (404); Glassdoor shows 2 open positions company-wide. **The engineering blog `webuild.envato.com` now 301s to `elements.envato.com/learn/`** and the community forums 301 to the help centre — both retired.

### Section 7: Payment-Specific News

**No public information found.** Envato has never announced a PSP, gateway or orchestration partnership. The only payments-adjacent announcement is the **Trolley** payouts partnership (29 June 2023), with a named sponsor — **Keri Thom, Envato Finance Director** — though that quote is pre-acquisition and her current status is unverified.

### Section 8: Checkout Experience Audit

| Dimension | Finding | Quality |
|---|---|---|
| Checkout type | Custom-built, PSP hosted fields | — |
| Guest checkout | **No** — account required at checkout | Fair |
| Card input | **Tokenised PSP-side** — *"card details are stored securely by our payment processor, not by Envato. Card information is never transmitted to or stored on Envato's own servers"* | Good |
| Methods visible | Elements: 4 card brands + Apple Pay + PayPal. Market: 4 card brands + PayPal | **Poor for a global marketplace** |
| **Location-based display** | ❌ **None — the method set is globally uniform** | **Poor** |
| **Multi-currency** | ❌ **USD only.** *"All transactions are processed in US dollars"* | **Poor** |
| Handling fee | *"A handling fee may apply on orders under $150"* — stated repeatedly; **amount not published** | Fair |
| 3DS | **Not observable** | — |
| Saved cards | Yes, vaulted PSP-side | Good |
| Error messages | Detailed self-service troubleshooting, but the remedy offered for cross-border blocks is *"contact your bank"* | Fair |

### Section 9: PCI DSS Compliance

**No direct PCI compliance documentation found publicly for Envato.**

> `[INFERENCE, not confirmed]`: based on the confirmed Braintree/Stripe tokenised integration and Envato's statement that card data *"is never transmitted to or stored on Envato's own servers"*, PCI scope is likely reduced (SAQ A / A-EP) with the PSPs handling card data. **No level is stated anywhere. Do not assert one.**

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: They localised money out, not money in**
> **Evidence:** Section 4 payouts (*"137 currencies, 83 of which are transferred via local routes"*) **+** Section 4 pay-in (four card brands, PayPal, Apple Pay, **USD only, zero local rails**). Both from the same help centre.
> **Pain Point:** the company demonstrably believes local rails matter — it built them for 42,000 authors in 173 countries — and buyers get a USD card form.
> **Yuno Value Proposition:** the same localisation on the collection side, through one integration.
> **Outreach Angle:** flattering, specific and checkable. It credits them with the hard half already done.
> **Suggested Subject Line:** 137 currencies out, one currency in
> ⚠️ **Constraint:** do **not** pitch the payout side. Trolley is a recent, working, publicly-celebrated relationship with a named finance sponsor.

> **Insight #2: They wrote the cross-border diagnosis themselves**
> **Evidence:** Section 5 (*"since Envato is Australia-based, some card issuers block overseas payments by default"*) **+** Section 3B (single gateway, no routing, no failover).
> **Pain Point:** an Australian-acquired USD transaction against a foreign issuer, with no alternative route when it declines — and the published remedy is "contact your bank."
> **Yuno Value Proposition:** local acquiring so the transaction stops being foreign, plus failover when it still declines.
> **Suggested Subject Line:** "Contact your bank" as a checkout strategy
> ⚠️ **Constraint:** you cannot say how *much* they lose. No approval-rate data exists. Frame it as structure, never as a quantified leak.

> **Insight #3: The consolidation window is open right now**
> **Evidence:** Section 6 (Getty merger dead 7 Jul 2026; Shutterstock standalone; tax/payout systems being aligned to Shutterstock as of Sept 2026) **+** Section 6 (~30% of Envato's workforce cut in March 2026).
> **Pain Point:** a live systems-integration programme, materially less engineering capacity, and a parent that now has to prove the US$245m asset performs.
> **Yuno Value Proposition:** buy rather than build, at exactly the moment building got harder.
> **Suggested Subject Line:** Aligning Envato billing with Shutterstock

> **Insight #4: Canva — the same city, the opposite answer**
> **Evidence:** Section 11 (Canva, Melbourne-adjacent Australian creative-tools peer, supports **UPI and UPI Autopay** in India with dedicated country help pages) **+** Section 4 (Envato supports **no UPI**, no local rails anywhere).
> **Outreach Angle:** two Australian creative-platform companies with global prosumer buyers, opposite answers to the same question.
> ⚠️ **Constraint:** Canva's UPI support is `[UNVERIFIED — URLs and titles confirmed by search index, pages not fetched]`. **Verify before naming a competitor in an email.**

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks:**
1. "You pay authors into 137 currencies over 83 local clearing routes. Buyers get a USD card form."
2. "Your own troubleshooting page tells buyers their bank blocks you because Envato is Australia-based."
3. "Your Accepted Payment Methods page asks buyers to email support if their country's payment provider is missing."

**Cold call openers:**
1. "Who owns the decision on adding a payment method — Melbourne, or New York now?"
2. "You built local payout rails for authors in 173 countries. What stopped the same thing happening on the buy side?"
3. "Elements takes Apple Pay and ThemeForest doesn't. Are those two separate integrations?"

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors
| Company | HQ | Payment stack | Source |
|---|---|---|---|
| **Canva** | Australia | **Cards, PayPal, UPI, and UPI Autopay** in India; debit cards not supported there; dedicated country help pages | `[UNVERIFIED — URLs confirmed, pages not fetched]` |
| **Shutterstock** *(now the parent)* | USA | Cards globally; **SEPA direct debit** in eligible countries; PayPal **US/Canada/Europe only** | `[UNVERIFIED]` |
| **Freepik** | Spain | Cards, PayPal, **Google Pay**, **Apple Pay**; no local APAC rails indicated | `[UNVERIFIED]` |
| Adobe Stock, Getty/iStock, Creative Market, TemplateMonster, Motion Array, Storyblocks, Artlist | — | **Not established — budget exhausted** | — |

#### 11C. Companies Recently Adopting Payment Orchestration
> ❌ **"No public case studies found of direct competitors adopting payment orchestration."**
>
> ⚠️ **And the merchant-of-record hypothesis was tested and NOT established.** Paddle, FastSpring and Lemon Squeezy are MoR vendors, but **no evidence was found that any Envato competitor uses one.** Do not assert it either way.

**The one competitive observation that holds up: Canva.** Same country, same creative-tools category, same global prosumer buyer base — and Canva built **UPI and UPI Autopay for recurring billing** plus localised country help pages. Envato has neither. *(Verify the Canva half before it goes in an email.)*

### Section 12: Business Case Data

| Metric | Value | Source |
|---|---|---|
| Acquisition price | **US$245m cash**, completed **22 July 2024** | PR Newswire ✅ |
| Subscribers added | **+650,000**, taking Shutterstock group to **1.15 million** | ✅ |
| **Earning authors** | **42,000+ across 173 countries** | Trolley case study ✅ |
| **Payout currencies** | **137**, of which **83 via local IACH routes** | Envato help centre ✅ |
| Annual revenue | **Not disclosed post-acquisition.** Shutterstock does not break Envato out | — |
| GMV | **Not found** | — |
| Average transaction value | **Not found.** Marketplace items are commonly $19–$59 `[UNVERIFIED]` | — |
| **Monthly transaction count** | ✅ **DERIVED — Envato Market: ~59,000/month current run-rate; ~97,000/month trailing 12 months.** From Envato's own live cumulative counter (`78,946,574 items sold`, verified by me byte-identical across four marketplace domains on 2026-09-17), differenced against archived snapshots. ⚠️ **Excludes Elements subscription renewals — not published anywhere.** Total is higher and plausibly ≥100,000, but only the Market half is established | Envato footer counter + Wayback ✅ |
| **Marketplace volume trend** | ⚠️ **~126,000/month (Sep–Dec 2025) → ~59,000/month (Sep 2026). A >50% collapse in twelve months.** Independently consistent with Shutterstock's reported −17% Q2 2026 revenue | Same derivation |
| **Cumulative community earnings** | **$1,254,306,531** — but Envato's CEO said **"$1.3 billion"** in May 2024. **A cumulative counter cannot go backwards**, so this counter excludes Elements and Placeit payouts | Verified by me |
| Primary currency | **USD only**, globally | ✅ |
| Top 3 markets by revenue | **Not found — Envato publishes no buyer geography** | — |
| Billing channel split | **N/A** — web checkout, no app-store IAP exposure | — |

> **Business case sizing requires a discovery call.** Envato disclosed useful metrics pre-acquisition; Shutterstock does not break it out. What *is* unusually well documented is the **cost structure of the problem** rather than its size: USD-only presentment, single gateway, no local rails, self-reported cross-border blocks.

### Overall Research Confidence

**High on the payment stack, methods and corporate timeline. None on traffic or volume.**

**High confidence** (primary source, fetched and parsed by me):
- **455 help-centre articles** across all three Envato help centres, via the open Zendesk API
- The two enumerated accepted-method lists, and the cross-border and regional-provider quotes
- `envato.com` → `elements.envato.com` redirect, confirmed by my own fetch
- Checkout CSP evidence for Braintree and Stripe

**Medium:** the Shutterstock/Getty timeline (multiple sources, mostly search summaries); Trolley's exact role (payout rail vs tax layer only — Envato never names its payout provider in its own words).

**Low / none:** **traffic — not obtained**; **buyer geography — not published**; revenue and volume; approval rates; PCI; competitor stacks.

**Traffic data was NOT obtained** — not supplied, not API-sourced, and the WebSearch fallback was not accepted across a seven-domain estate. **This is the binding constraint on the score.**

### Manual Research Recommendations

> **Area:** Envato Elements subscription renewals per month — **now the top gap**
> **Why it matters:** the Market half is derived from their own counter (~59k/month). Elements is 62% of traffic and the whole subscription business, and its renewal count is **published nowhere**. It decides whether the true total is ~59k or several hundred thousand — i.e. whether this scores +3 or +5.
> **Action:** discovery question. Do not estimate it; the monthly-vs-annual billing mix is also undisclosed, so it cannot be derived from the subscriber count.

> **Area:** Traffic for the four uncovered domains
> **Why it matters:** the 5.79M/month figure and every country share are floors, and 58.1% of traffic is unattributed.
> **Action:** paste full SimilarWeb data into `accounts/traffic/envato.md` covering graphicriver.net, photodune.net, envato.com and tutsplus.com.

> **Area:** Stripe vs Braintree for Elements subscription volume
> **Why it matters:** it determines whether a PSP migration is already underway — which is either the best possible timing or the worst.
> **Action:** log in and walk the Elements checkout with DevTools open.

> **Area:** Territory ownership
> **Why it matters:** the contracting entity is Shutterstock, Inc., arbitration is in New York, and tax systems are being aligned to the parent.
> **Action:** check with AMER whether Shutterstock is already owned on the account list, before any sequence.

> **Area:** The TAL contains a duplicate
> **Why it matters:** **row 660 "CodeCanyon (Envato)" is an Envato marketplace, not a separate company.** Working both would double-count the account.
> **Action:** merge row 660 into row 117.

### Appendix: All Source URLs

**Primary (fetched and parsed by me):**
- https://help.elements.envato.com/api/v2/help_center/en-us/articles.json — 112 articles
- https://help.market.envato.com/api/v2/help_center/en-us/articles.json — 98 articles
- https://help.author.envato.com/api/v2/help_center/en-us/articles.json — 245 articles
- https://help.elements.envato.com/hc/en-us/articles/360000621543-Accepted-Payment-Methods
- https://help.market.envato.com/hc/en-us/articles/203269700-How-do-I-purchase-an-item-on-Envato-Market
- https://help.market.envato.com/hc/en-us/articles/202821550-What-are-common-PayPal-and-credit-card-issues-on-Envato-Market
- https://help.elements.envato.com/hc/en-us/articles/4411385939225-Failed-payments
- https://help.elements.envato.com/hc/en-us/articles/360000621523-How-to-View-Download-Invoices-on-Envato
- https://help.author.envato.com/hc/en-us/articles/20535795834393-Getting-Started-with-the-Envato-Payout-System
- https://help.market.envato.com/hc/en-us/articles/41383541904281-Envato-Market-User-Terms

**Secondary:**
- https://www.prnewswire.com/news-releases/shutterstock-completes-acquisition-of-envato-302203152.html
- https://trolley.com/blog/envato-trolley-partnering-to-empower-creators/
- https://www.trustpilot.com/review/www.envato.com
- Getty/Shutterstock termination — SEC Form 425 `[UNVERIFIED]`
- smartcompany.com.au — Envato March 2026 layoffs `[UNVERIFIED]`

</details>
