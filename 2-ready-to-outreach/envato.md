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
> A global marketplace billing in **three Western currencies** off a **single PayPal-family gateway**, telling its own buyers that their cards get blocked because of where it acquires, and publicly inviting requests for local rails. **You can quote them to themselves.**
>
> ## 🚨 THE STRONGEST EVIDENCE IN THIS FILE — found 2026-09-20
>
> **Envato publishes a help article titled *"Why can't I subscribe to Envato from India?"*** — updated **2026-09-11**. [Link](https://help.elements.envato.com/hc/en-us/articles/4408165799577-Why-can-t-I-subscribe-to-Envato-from-India). Verbatim:
>
> > *"Some users in India are unable to subscribe to Envato, or find that their **existing subscription fails to renew**. This is caused by a **Reserve Bank of India (RBI) mandate** that requires additional customer authentication for recurring credit card transactions. As a result, some Indian banks block these payments before they reach Envato. **This issue affects both new subscriptions and automatic renewals** for customers using India-based bank cards."*
> >
> > *"Because Envato's subscription billing processes renewals automatically, **it may not be able to satisfy this additional authentication step**, causing the payment to be declined by the card issuer."*
> >
> > *"**Envato is currently unable to offer a direct technical workaround for this issue.**"*
> >
> > *"**Will Envato fix this payment issue?** … **Envato is unable to change how this structural authentication works.** The most effective path forward is to contact your card issuer."*
>
> Their remedies to the customer: **phone your bank, try PayPal, check back periodically.**
>
> **Read what this is.** Their **#1 traffic market (14.67%)**. The **80.3%-of-revenue** business. **Recurring billing structurally broken**, and a **published admission that they cannot fix it.** `.claude/reference/subscription-payments.md` §3 calls RBI e-mandate *"the single strongest recurring-payments hook in the territory"* — and here it is confirmed first-party rather than inferred.
>
> ✅ **This also removes the verification risk.** Do **not** cite RBI rules yourself (they change, and the research skill forbids citing them from background knowledge). **Quote Envato's own page instead.**
>
> ### ✅ CROSS-BORDER — CONFIRMED in their own words, three pages, all live
>
> | Their words | Page | Updated |
> |---|---|---|
> | *"…enable recurring **international** payments…"* | Why can't I subscribe from India | **2026-09-11** |
> | *"since Envato is Australia-based, some card issuers block **overseas** payments by default"* | Common PayPal and credit card issues | 2026-09-16 |
> | *"may charge additional fees, **including international transaction fees**"* | Refund policy | 2026-09-16 |
>
> **Structural bound, independent of acquirer domicile:** entities exist only in **AU and US**; top markets are **India 14.67%, US 11.67%, Indonesia 4.73%, Brazil 2.91%, Mexico 2.49%, Pakistan 2.17%** — **Australia does not appear in the top five.** Whether they acquire in Sydney or New York, the large majority of buyers sit outside it. ⚠️ **The acquirer's domicile is still NOT established — do not quote a cross-border percentage.**
>
> ### ⛔ CURRENCY CORRECTION — "USD only" was WRONG for Elements
>
> This file asserted a **single USD-only checkout worldwide**. That is **correct for Market and wrong for Elements**, which is 80.3% of revenue.
>
> - **Market** — *"All transactions are processed in US dollars."* ✅ USD only (updated 2026-09-16)
> - **Elements** — *"Envato subscription fees are in US Dollars, **or if you are in the European Union, in Euros**. We may offer subscription fees in other currencies from time to time."* (User Terms, updated **2026-09-18**); refunds issue in *"either **USD, EUR, or GBP**"* (updated 2026-09-16)
>
> **The claim narrows but survives:** USD, EUR and GBP serve the US and EU and **none of the top emerging markets** — India, Indonesia, Brazil, Pakistan and Mexico all still convert. **Say "three Western currencies, none of them local to your biggest markets", never "USD only".**
>
> ✅ **And the replacement quote is stronger.** Elements User Terms, updated 2026-09-18: *"**You are responsible for all costs of currency conversion**… you may incur additional costs when purchasing from Envato Elements, **which we have no control over.**"*
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
| 1 | **India** | **14.67%** `[EST]` | Visa, Mastercard, Amex USD-only, PayPal (+Apple Pay on Elements) — **USD (Market) / USD-EUR-GBP (Elements)**. ⚠️ **Subscriptions structurally FAIL here — see the RBI block at the top** | **UPI, netbanking, RuPay, EMI, UPI Autopay — SOURCED ABSENT** | ❌ none |
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

### ✅ TERRITORY — RESOLVED 2026-09-19: Prateek is proceeding

| Factor | Points to |
|---|---|
| Operating site, staff, brand: **Melbourne** | **APAC** ✅ |
| **Contracting entity in current terms: "Shutterstock, Inc."** | **AMER** ❌ |
| Arbitration venue: **New York** | AMER ❌ |
| Tax/payout systems **being aligned to Shutterstock** as of Sept 2026 | AMER ❌ |
| Envato Pty Ltd reduced to **DMCA agent + one creator contract** | AMER ❌ |

**Decision — 2026-09-19: Prateek is targeting this account.** The concern below was raised and he has taken the call; Envato remains an APAC-HQ'd *operating* entity in Melbourne and is defensible as in-territory. **Treat the territory question as closed.**

**The residual risk, for drafting only — not for re-opening the targeting decision.** The payments counterparty is a US-listed parent, arbitration sits in New York, and a payments-specific consolidation programme is visibly running (RWT alignment, first affected payout September 2026). **The reader may not be in Australia.**

➡️ **So the sequence must NOT be APAC-personalised.** Lead on the **single USD-only checkout**, the **approval-rate cost**, and the **in/out asymmetry** (137 payout currencies vs one collection currency). **India and Indonesia belong in the email as evidence of scale — proof the gap is expensive — not as the subject of the pitch.** Framed that way it reads correctly whether it lands in Melbourne or New York.

⚠️ **Still worth a one-line check with AMER** on whether Shutterstock, Inc. is already owned elsewhere on the account list — that is a duplicate-coverage question, not a territory one, and it does not block the sequence.

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

Envato is a two-sided digital-goods business — Envato Elements (subscription) plus six Envato Market marketplaces — HQ'd in Melbourne and **wholly owned by Shutterstock since July 2024**. Buyers pay in **USD on Market and USD/EUR/GBP on Elements** — **no local currency in any emerging market** — through **four card brands, Apple Pay (Elements only) and PayPal**, on a **single PayPal-family gateway (Braintree)**, with **Stripe** on the newer subscription/account layer and **no local payment method anywhere in the world**. Meanwhile Envato pays its authors in **137 currencies over 83 local clearing routes** — it has solved localisation for money *out* and not for money *in*. The motion is **Greenfield**, confirmed affirmatively from checkout CSP headers, and the sharpest asset is that Envato's own help pages both diagnose the cross-border decline problem and invite requests for regional providers.

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

> ### ⚠️ Traffic is not revenue — and the regional split you want does NOT exist
>
> **Shutterstock does not break out Envato post-2024.** It reports as a **single reporting unit**; Envato appears in the Q2 2026 10-Q only in the trademark list and in a sentence naming the brands Content is distributed under. **There is no Envato regional split at any point.** The group figures below are group-wide.
>
> ### ✅ BUT ENVATO'S STANDALONE REVENUE *IS* PUBLIC — found 2026-09-19
>
> Shutterstock had to file **PwC-audited Envato financials under Rule 3-05** ([8-K/A, 2024-10-03](https://www.sec.gov/Archives/edgar/data/1549346/000154934624000039/), Ex-99.1 and Ex-99.3) and the acquisition-year contribution under **ASC 805** in the FY2024 10-K. **Revenue is USD thousands as presented in the Article 11 pro forma.**
>
> | Period | Revenue | Source |
> |---|---|---|
> | **FY ended 30 Jun 2023** (audited) | **$190.3M** | 8-K/A Ex-99.3 |
> | Six months to 31 Dec 2022 | $92.3M | same |
> | Six months to 31 Dec 2023 | $99.8M | same |
> | **Calendar 2023** (A−B+C, Shutterstock's own presentation) | **$197.8M** | same |
> | **Q1 2024** (3 months to 31 Mar) | **$49.7M** | same |
> | **22 Jul – 31 Dec 2024** (post-acquisition) | **$90.5M** | [FY2024 10-K](https://www.sec.gov/Archives/edgar/data/1549346/000154934625000011/sstk-20241231.htm) |
>
> FY2024 10-K verbatim: *"For the year ended December 31, 2024, **revenues of $90.5 million**… were included in the Consolidated Statements of Operations related to **Envato**."* Over ~5.3 months that is **~$17.0M/month, ~$204M annualised** — consistent with CY2023.
>
> **P&L shape at acquisition:**
>
> | | CY2023 | Q1 2024 |
> |---|---|---|
> | Revenue | $197.8M | $49.7M |
> | Total opex | $162.7M | $39.6M |
> | **Operating income** | **$35.1M** | **$10.1M** |
> | **Operating margin** | **17.8%** | **20.3%** |
>
> Growth on the comparable half: H2 2022 $92.3M → H2 2023 $99.8M = **+8.1%**.
>
> 💰 **Shutterstock paid US$245m for ~$198M of revenue at a ~20% operating margin — about 1.24× revenue.** A strikingly low multiple.
>
> ⚠️ **The series stops at 2024.** ASC 805 disclosure applies only in the acquisition year, so **there is no Envato revenue line for 2025 or 2026.** Pro forma combined went **FY2024 $1,045.4M → FY2025 $989.9M (−5.3%)**, then H1 2026 **−17.4%** — the decline accelerated sharply after year one, **but that is group and cannot be attributed to Envato from the filings.** The Envato-specific post-acquisition signal is the **marketplace volume collapse in Section 3** (~126k/month → ~59k/month), not anything in the 10-K.
>
> ⚠️ **The PwC opinion is QUALIFIED — and it is benign.** The sole basis: the statements omitted **IFRS 1 first-time-adoption comparatives and transition disclosures**. Not going concern, not a misstatement. **Do not treat it as a red flag and do not raise it in outreach.**
>
> ✅ **This validates the Envato-share arithmetic below.** $197.8M / $1,079.5M pro forma = **18.3% of the combined entity** — close to the ~20% used in the India correction, so that reasoning holds.
>
> ### ⛔ REGIONAL SPLIT FOR ENVATO: CONFIRMED NOT TO EXIST — checked 2026-09-20
>
> **I read all 28 pages of the audited statements.** They are filed as **scanned JPEGs** (`annualfinal-envatofinanc001–028.jpg` in the 8-K/A), which is why the HTML wrapper is only 15KB and why text search finds nothing. **Note 5 Revenue disaggregates by PRODUCT only. There is no segment note and no geographic disclosure anywhere in the document.**
>
> **The reason is structural, so it will never exist for the pre-acquisition years:** Envato Pty Ltd was a **private company**, and **IFRS 8 segment reporting binds only entities with publicly traded debt or equity.** They were never required to disclose geographic revenue. **This is a checked absence — stop looking.**
>
> ### ✅ WHAT NOTE 5 DOES GIVE — the product split, and it is more useful
>
> **FY ended 30 June 2023, USD'000** (the statements are presented in **USD**, confirmed on the note headers — not AUD):
>
> | Line | Amount | Share | Recognition |
> |---|---|---|---|
> | **Platform subscriptions fees** (Envato Elements) | **$152,859** | **80.3%** | **Principal → GROSS sales price** |
> | **Platform one-time service fees** (the six marketplaces) | **$37,454** | **19.7%** | **Agent → COMMISSION receivable only** |
> | **Total revenue from ordinary activities** | **$190,313** | | |
>
> Note 4, verbatim: *"For platform subscriptions fees, the Group has determined that it meets the criteria of acting as a **principal** and therefore recognises the **gross sales price**. For the platform one-time service fees, the Group has determined that it meets the criteria of acting as an **agent** and therefore recognises the **amount of commission receivable**."*
>
> 💥 **Consequence 1 — payment volume is materially larger than revenue.** The $37.5M marketplace line is **commission, not GMV**. Gross buyer spend through that checkout never appears in revenue. Money moving through Envato's checkout ≈ **$153M (Elements, gross) + marketplace GMV**. ⚠️ **Envato's commission rate was NOT verified this session — do not put a GMV figure in outreach until someone checks the published author fee schedule.**
>
> 💥 **Consequence 2 — this is a SUBSCRIPTION business by revenue, not a marketplace.** **80.3% of revenue is recurring billing**, in **USD/EUR/GBP only**, on Braintree/Stripe, **with no local rail anywhere in the world — and structurally failing in India, their #1 market, by their own published admission.**
>
> ⛔ **CORRECTION to earlier drafting advice in this file and in chat:** the marketplace item-sales collapse (~126k → ~59k/month, Section 3) was recommended as the lead signal. **It sits in the 19.7% half.** The subscription side is ~4× larger by revenue and is where recurring-billing failure compounds — involuntary churn, failed renewals, account updater, network tokens, retry logic. **Lead there.** ➡️ **Read `.claude/reference/subscription-payments.md` before drafting; this is not "subscription-adjacent", it is a subscription business.**
>
> 💸 **Also in Note 4 — a USD 18.1M global sales tax provision**, 9.5% of revenue: *"a provision for potential global sales tax exposures across all its products… estimated exposures by country."* A company already carrying a large, country-by-country indirect-tax problem.
>
> ✅ Going concern statement is clean. 🧰 **Technique recorded: SEC exhibits can be scanned JPEGs — a text grep returning nothing does NOT mean the disclosure is absent. Check the filing's `index.json` for image files before concluding.**
>
> 🧰 **False positive recorded:** a raw scan for `AUD` in the pro forma returned 36 hits. **Every one was the substring inside `unaudited`.** Add to the running list: **`unaudited` → AUD.**
>
> **Group revenue by customer location** — [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1549346/000154934626000029/sstk-20260630.htm), filed 2026-08-07, revenue note. Pulled from the primary filing on 2026-09-19; figures in $000s.
>
> | Region | Q2 2026 | share | Q2 2025 | **YoY** | H1 2026 | share | **H1 YoY** |
> |---|---|---|---|---|---|---|---|
> | North America | 118,133 | 53.3% | 147,884 | **−20.1%** | 207,154 | 49.2% | **−22.7%** |
> | Europe | 59,181 | 26.7% | 64,389 | **−8.1%** | 121,902 | 29.0% | **−6.6%** |
> | Rest of the world | 44,487 | 20.1% | 54,717 | **−18.7%** | 91,915 | 21.8% | **−17.2%** |
> | **Total** | **221,801** | | **266,990** | **−16.9%** | **420,971** | | **−17.4%** |
>
> Also disclosed: *"The United States… accounted for **38%** and 42% of consolidated revenue for the six months ended June 30, 2026 and 2025"* and *"**No other country accounts for more than 10%** of the Company's revenue in any period presented."*
>
> **⛔ CORRECTION — 2026-09-19. An earlier version of this line said "India and Indonesia drive volume; North America drives money," citing the <10% disclosure as confirmation. That was overstated and is retracted.**
>
> The 10% is a ceiling on India **at group level**, and Envato is a minority of the group. If Envato is ~20% of group revenue and India contributes ~2% of core Shutterstock, India could be **up to roughly 40% of Envato's revenue** and the filing would read exactly as it does. **India's revenue share at Envato is UNKNOWN, not small.** The low-ARPU inference is still reasonable — but it is an inference from ARPU norms, **not** something the filing establishes. **Never write "India is small for you" in an email**; they know their own numbers.
>
> **⚠️ No region is growing.** All three are declining. Europe's rising *share* is attrition, not growth. **A "help you grow region X" pitch does not fit this company** — down 17% on revenue, ~30% of Envato's workforce cut, $173.7m impairment. **Anchor on conversion and cost: recovered declines are margin on revenue already earned and already paid for.**
>
> **⚠️ Territory note:** "Rest of the world" is tagged `AllRegionsOfTheWorldExceptNorthAmericaAndEuropeMember` — it lumps APAC with LatAm, MEA. **APAC is not separable at any level of this filing, so no revenue-led APAC email can be built from disclosed data.** Use the Envato-specific marketplace volume figure in Section 3 instead — transactions, not traffic, and Envato's own published counter.

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

> *"Warning: Envato operates with no local billing entity outside Australia and the United States, billing in USD on Market and USD/EUR/GBP on Elements — no local currency in any emerging market. Transactions are processed cross-border, with higher scheme costs, lower approval rates and FX exposure."* ⚠️ **Corrected 2026-09-20 — the original said "single USD-only checkout worldwide", which is wrong for Elements.**
>
> **This is not an inference — Envato says it.** *"since Envato is Australia-based, some card issuers block overseas payments by default."*

> ### ⛔ THE IRELAND TRAP — checked 2026-09-20. EU VAT registration is NOT an EU entity.
>
> **VAT on Envato Market FAQ**, updated **2026-09-16**, verbatim:
> > *"Envato collects VAT from EU consumer buyers under EU digital VAT rules, using **VAT number EU372009975**… As of **1 October 2019, Ireland became Envato's Member State of Identification** under the EU VAT Mini One Stop Shop (MOSS) scheme."*
>
> **Read the VAT number: `EU372009975`. The `EU` prefix is a NON-UNION SCHEME registration** — the regime for businesses **not established in the EU**. An Irish-established entity would carry an **`IE`** prefix. **Ireland is the administrative filing point precisely BECAUSE there is no EU establishment.**
>
> Envato confirms it in the same article, twice: *"**Envato is an Australian company** — why does EU VAT apply?"* and *"While **Envato is based in Australia**…"*
>
> ➡️ **EU VAT registration ≠ EU establishment ≠ EU acquiring.** If anyone at Envato answers *"we're registered in Ireland"*, that is a **tax filing, not an acquirer**. Same trap as the *"for EU VAT purposes only, Envato steps into the supply chain as the supplier on record"* line in the Elements terms. **Do not let either be mistaken for local presence.**
> *(Note: Shutterstock's 10-Q separately shows Irish long-lived assets — that is **Shutterstock's** footprint, not Envato's, and does not change the above.)*
>
> ### ⚠️ EUROPE IS THE WEAKEST CROSS-BORDER ARGUMENT IN THIS ESTATE — do not lead on it
>
> 1. **No FX for EU buyers** — billed in **EUR**. Europe, the US and the UK are the only markets where the billing currency matches the buyer. India, Indonesia, Brazil, Pakistan, Mexico all convert.
> 2. **No European equivalent of the India article exists.** Both help centres were searched for **SCA, PSD2, 3D Secure and authentication** — **nothing**. A documented five-year-old unfixed India failure, and no documented Europe failure.
> 3. **That is structurally expected.** Under SCA, recurring **merchant-initiated transactions are generally out of scope** once the mandate is authenticated. India's e-mandate is stricter — it bites on the mandate **and** on above-threshold debits. **Europe genuinely is the easier regime for recurring billing. Do not imply otherwise; it is wrong on the substance and checkable.**
> 4. Europe is **EMEA territory** regardless.
>
> ### ⚠️ REFINED 2026-09-20 — "weakest argument" was too blunt. Split friction from cost.
>
> The four points above are about **customer-facing friction**, and there they hold. **On COST OF ACCEPTANCE, Europe may be a strong argument** — that was under-weighted.
>
> **The interchange point.** EU consumer-card interchange is capped by the **Interchange Fee Regulation at 0.2% debit / 0.3% credit — but only INTRA-EEA**, i.e. issuer *and* acquirer both inside the zone. **An EU-issued card acquired from outside the EEA is inter-regional and falls outside the cap**, at materially higher rates. `apac-payments.md` frames it identically: *"Interchange is capped intra-EEA (IFR), so cross-border framing only applies outside the zone."* **Envato is outside the zone** — confirmed by the `EU`-prefixed VAT number above.
>
> So on an identical EU transaction, an EU-established competitor pays capped interchange and **Envato does not** — plus the scheme's inter-regional assessment on top. **Cost of acceptance on European volume is structurally above the local benchmark.**
>
> **The invisible third cost.** They bill EU customers in **EUR** but presumably settle to AUD or USD. **The buyer sees no FX — Envato absorbs the conversion on the settlement side.** Inverse of India: there the *customer* bears FX and abandons; here the *merchant* bears it and it shows up as margin.
>
> ### ⛔ THE CAVEAT THAT COULD KILL THIS ENTIRE ARGUMENT
>
> **The acquirer's domicile is NOT established**, and there is a specific scenario where none of the above holds. Both gateways have **EEA-licensed entities** — **Stripe Payments Europe (Ireland)** and **PayPal (Europe) S.à r.l. (Luxembourg)**. **If Envato's EU volume is acquired through either, those transactions are intra-EEA and IFR-capped, and the interchange argument collapses entirely.**
>
> Acquiring entity normally follows the **merchant's** domicile, not the customer's — and Envato is AU-operating with a US contracting entity, so inter-regional is the likelier setup. **But "likelier" is not "established."**
>
> ➡️ **Make it a discovery question, never a claim:** *"Is your EU volume acquired through an EEA entity, or from Australia?"* **Yes to Australia → uncapped interchange on a large revenue base. Yes to Ireland → you learned something and lost nothing.**
>
> ⚠️ **Rate discipline.** The 0.2%/0.3% caps are stable law from 2015 but **must be sourced before use** per the research skill. **Never quote inter-regional interchange rates** — they are not in this file because they would be recited from memory, not sourced.
>
> ✅ **Net:** Europe is a **bad conversion story and a possibly good margin story.** Different pitch, different audience — a CFO cares about the second.
>
> ### ✅ USE THE ASYMMETRY INSTEAD — the strongest drafting move in this file
>
> Per `email-samples.md`: contrast two of the prospect's own systems so neither half can be disputed.
>
> > **They localised currency and tax compliance for Europe — EUR pricing, an EU VAT registration, country-by-country tax tables. They localised nothing for India, their largest market by traffic, where their own help page says subscriptions fail and they cannot fix it.**
>
> One company, two markets, two levels of investment, every element sourced from their own pages.

> ⚠️ **No regulatory acquiring gate is asserted.** None was verified this run.

> 🧰 **False positives caught in the Europe sweep — add to the running list:** **`DMCA` → SCA** and **`scam`/`escalate` → SCA** (these flooded a help-centre search for Strong Customer Authentication). Also re-confirmed: `separate` → SEPA, `is ideal for` → iDEAL.

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Surface | Provider | Evidence Type | Source |
|---|---|---|---|
| **Envato Market** (6 marketplaces) | **Braintree** + **PayPal** | `[Source Code]` — checkout CSP allowlists `*.braintree-api.com`, `*.braintreegateway.com`, `*.paypal.com` and nothing else payment-related | `themeforest.net/checkout`, `codecanyon.net/checkout` |
| **Envato Elements** | **Braintree** | `[Terms/Privacy Policy]` — *"see the **Braintree Prohibited Transactions** page"* | [Failed payments](https://help.elements.envato.com/hc/en-us/articles/4411385939225-Failed-payments) |
| **Elements / account layer** | **Stripe** | `[Terms/Privacy Policy]` + `[Source Code]` — *"managed by Stripe"*; `account.envato.com` CSP allowlists `js.stripe.com`, `api.stripe.com`, **no Braintree** | [Invoices article](https://help.elements.envato.com/hc/en-us/articles/360000621523-How-to-View-Download-Invoices-on-Envato) |
| **Author payouts** | **Trolley** | `[Terms/Privacy Policy]` — named by Envato itself | [Tax Form Troubleshooting](https://help.author.envato.com/hc/en-us/articles/61599514214169-Tax-Form-Troubleshooting-Help) |

**Merchant of record — a nuance that matters.** Envato is **not** a full MoR; it is an **expressly limited agent**. Terms, verbatim: *"**WE DO NOT PROCESS PAYMENTS FOR ANY ENVATO MARKET SERVICES.**… we may use one or more third-party payment processors"* and *"we receive that payment as a **limited agent for the Author**."* The one exception: *"For EU VAT purposes only, **Envato steps into the supply chain as the supplier on record**."*

### ✅ NARROWED 2026-09-20 — the evidence now leans clearly to Stripe on Elements

**Re-pulled live CSP headers across the estate.** Mapping the rails onto the Note 5 revenue split:

| Surface | Rail | Revenue (FY-Jun-23) | Share | Confidence |
|---|---|---|---|---|
| **Envato Market** (6 marketplaces) | **Braintree + PayPal** | $37.5M *commission* | **19.7%** | ✅ **Verified 2026-09-20** |
| **Envato Elements** (subscriptions) | **Stripe and/or Braintree — unresolved** | $152.9M *gross* | **80.3%** | ❌ **NOT established** — see retraction below |

⚠️ **The revenue shares above are FY ended 30 June 2023 — over three years stale.** Since then Shutterstock acquired the business and **marketplace item sales reportedly halved** (~126k → ~59k/month, Section 3). Elements clearly dominates, but **the current ratio is unknown — do not quote "80/20" as a present-day fact.**

**PROVEN — Market → Braintree.** Live CSP on `themeforest.net/checkout` and `codecanyon.net/checkout` (served even on a 404):
```
connect-src 'self' account.envato.com ... *.braintree-api.com *.braintreegateway.com *.paypal.com
script-src  ... *.paypal.com
```
**Zero Stripe on either.**

**PROVEN — the account layer → Stripe, exclusively.** `account.envato.com` serves a `strict-dynamic` nonce CSP:
```
script-src  'strict-dynamic' ... https://js.stripe.com https://*.js.stripe.com
frame-src   ... https://js.stripe.com https://*.js.stripe.com
connect-src ... https://api.stripe.com
```
**Braintree absent. PayPal absent.** (Note the Market checkout's `connect-src` includes `account.envato.com` — so the account layer is shared session/identity infrastructure across both estates, while the card rails differ.)

### ⛔ RETRACTED SAME DAY — "Elements runs on Stripe" was OVERSTATED. Do not use it.

An earlier version of this block inferred that **Elements subscription billing runs on Stripe**, from the account layer being Stripe-only plus the *"managed by Stripe"* invoices line. **That inference does not close, for two reasons.**

**1. PayPal breaks the chain.** Elements' Accepted Payment Methods article, **updated 2026-09-15**, states: *"Can I use PayPal to pay for Envato Elements? **Yes, PayPal is fully accepted for Envato subscriptions.**"* But `account.envato.com`'s CSP contains **no PayPal at all**. If that surface were the whole Elements payment path, PayPal would have to appear in it. **It does not, so it isn't.**

**2. The Braintree signal was dismissed too readily.** This file previously called the Elements failed-payments link to **Braintree's Prohibited Transactions page** "documentation, not an acquiring signal." That was weak: **Braintree is PayPal-owned and PayPal is its flagship native method.** Braintree still carrying PayPal on Elements is the simplest explanation for that link, and the article was edited **2026-08-03**.

⚠️ **But the counter-evidence is ALSO weak, and the reason is methodological.** `account.envato.com` serves **no `form-action` directive**. A **redirect-based PayPal flow — a full-page POST out to PayPal — would leave no CSP trace whatsoever.** So PayPal's absence from that CSP proves nothing either.

> 🧰 **METHOD NOTE, applies to every account in this repo.** **CSP evidences what a page loads in-band — scripts, iframes, XHR. It is near-useless for redirect-based payment methods**, which navigate away and need no allowlist entry (absent `form-action`). **Check for a `form-action` directive before treating a CSP absence as a sourced absence.** This file applied the technique sloppily and the correction is recorded here rather than buried.

### ✅ What actually stands

| Claim | Status |
|---|---|
| Market checkout → **Braintree + PayPal** | ✅ **Solid** — live CSP, zero Stripe |
| `account.envato.com` **card rail** → **Stripe** | ✅ **Solid** — Stripe.js in `script-src`, `frame-src` **and** `connect-src` |
| Elements **subscription charges** → Stripe | ❌ **NOT ESTABLISHED** |
| **Braintree still in the Elements path** | 🟡 **Plausible**, on the PayPal link |

➡️ **Safe to say in outreach:** *one customer, two vaults* — Market on Braintree, the account-layer card rail on Stripe, both proven, and a customer who does both has credentials stored in two places. **This does not depend on resolving Elements.**
❌ **NOT safe to say:** "your subscriptions run on Stripe."

❌ **Still not settled:** `elements.envato.com`'s own app CSP. **Every path 403s behind Cloudflare, including `/robots.txt`** — the challenge-page CSP it returns is Cloudflare's, not Envato's, and must not be mistaken for it. **A logged-in browser session is the only way to close this.**

➡️ **Drafting consequence.** The two-vault argument is **clean by business line**: a customer who subscribes to Elements *and* buys on ThemeForest has their card stored **twice, in two vaults, with two updaters and two token sets**. And the recurring-billing conversation — 80.3% of revenue — is a **Stripe** conversation. **Do not argue the wrong gateway on a call.**

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
| **Multi-currency** | ⚠️ **Market: USD only** (*"All transactions are processed in US dollars"*). **Elements: USD/EUR/GBP.** **No local currency in any emerging market.** | **Poor** |
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
| Primary currency | **USD (Market) / USD, EUR, GBP (Elements)** — no emerging-market currency | ✅ |
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
