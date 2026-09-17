# Envato

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 19 / 29 → ⭐ **High Priority**
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

**SimilarWeb total visits:** **Not obtained.** No supplied data, no MCP tools, and a WebSearch fallback was not accepted. **This is a multi-domain business** (elements.envato.com, themeforest.net, codecanyon.net, videohive.net, audiojungle.net, graphicriver.net, photodune.net) and any single-domain figure would distort the country profile badly. **No country split is asserted anywhere in this report.**

### Top 5 markets
> ⚠️ **This table cannot be completed.** No traffic data was obtained, and **Envato publishes no buyer-geography breakdown**. The premise that India, Indonesia and Vietnam are top Envato markets is **plausible for a developer/designer buyer base but is NOT verified** — do not put a market ranking in an email. What *is* sourced is that the method set is **globally uniform and USD-only**, so the rail gap applies everywhere rather than market-by-market.

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

### ICP Score breakdown — 19 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5 ⚠️** | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. `[ASSUMPTION — not researched.]`** Envato publishes no order count, no GMV and no revenue since the acquisition; Shutterstock does not break Envato out. **Basis:** Shutterstock's own completion release states the acquisition added **650,000 subscribers, taking the group to 1.15 million**. Subscription renewals alone, at ~1.15m subscribers billed monthly or annually, plus per-item marketplace purchases across six marketplaces, put the figure comfortably above 100,000/month. **Billing unit: Elements subscription renewals + per-item marketplace purchases.** Author payouts are excluded — they are money *out*. **This is an assumption and cannot carry or reject the account.** |
| Orchestration status | **+4** | ✅ **None detected — affirmative CSP evidence**, not a failed search. |
| 3+ countries | **+3** | ✅ Sells worldwide; pays authors in **137 currencies across 173 countries**; entities in Australia and the US. |
| Multiple PSPs | **+3** | ✅ **Braintree** (marketplace card) + **PayPal** (wallet) + **Stripe** (subscription/account layer) + **Trolley** (payouts). All first-party sourced. |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **Not awarded — and this is the painful one.** The rail gap is *sourced*: the Elements list is a closed enumeration and Google Pay is explicitly refused. But the rule requires the gap to be in a **top-3 traffic market**, and **no traffic data was obtained and Envato publishes no buyer geography**. I cannot name a top-3 market, so I cannot award it. **This is a data gap, not an evidence gap — see Manual Research.** |
| Recent expansion | **0** | ❌ No new market entry. The 2026 events are a *contraction* (~30% headcount) and an abandoned merger. |
| Payment issues reported | **+2** | ✅ **Trustpilot 2.2/5 across 9,044 reviews**, plus a concrete checkout-integrity defect quoted below, plus Envato's own documented cross-border decline problem. |
| Funding >$10M | **0** | ❌ Wholly owned by a public parent; no round. |
| High traffic outside home | **+2** | ✅ Awarded on structure, not traffic: an Australian-HQ'd marketplace selling **USD-only worldwide** with authors in 173 countries. Australia is self-evidently a minority of demand. |
| Competitor using orchestration | **0** | ❌ None confirmed. **And the brief's merchant-of-record hypothesis was tested and NOT established** — no evidence any competitor uses Paddle, FastSpring or Lemon Squeezy. Do not assert it. |
| Payment job postings | **0** | ⬜ None found; the jobs board is retired. |

**Tier:** **19 / 29 → ⭐ High Priority.** No analyst override applied.

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

**Data source: NONE OBTAINED.** No supplied SimilarWeb data, no MCP tools, and a WebSearch fallback was not accepted for a country split across a seven-domain estate.

**Consequence, stated plainly:** there is no traffic table, and **no buyer-geography claim appears anywhere in this report**. Envato publishes no breakdown either. **This directly cost 3 ICP points** — the rail gap is sourced but cannot be tied to a named top-3 market. It is the single most valuable gap to close.

One structural fact stands in for geography: the method set and USD-only pricing are **globally uniform**, so the rail gap applies in every market rather than varying by one.

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
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. `[ASSUMPTION — not researched.]`** Basis: ~1.15m group subscribers post-acquisition plus per-item purchases across six marketplaces. **Billing unit: subscription renewals + per-item purchases**, excluding author payouts | Assumption |
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

> **Area:** Buyer geography — **the top gap, and worth 3 ICP points**
> **Why it matters:** the rail gap is fully sourced, but the matrix requires it in a **top-3 traffic market** and no country data exists. Closing this alone moves the account to **22/29**.
> **Action:** pull SimilarWeb across all seven domains and aggregate, or paste the data into `accounts/traffic/envato.md`. **Cheapest, highest-leverage action on the account.**

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
