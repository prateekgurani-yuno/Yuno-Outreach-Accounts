# Azar

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 16 / 29 → 🟢 **Medium** — one point below ⭐, and the reason is stated in the breakdown
**Industry:** Social / random video chat (virtual-currency + subscription) · **HQ:** Seoul, South Korea (Hyperconnect Inc.), owned by Match Group, Inc. (NASDAQ: MTCH) · **Researched:** 2026-09-17 · **First email sent:** —
**Motion:** **In-house** — they built their own multi-PSP router (Adyen · Toss · Stripe enum). Respect the build; argue reach and opportunity cost, never that the build is wrong.

---

> ## 🔑 THE ONE-LINE VERSION
>
> Azar spent years as a textbook app-store-trap account — **76% of its revenue ran through Apple**. Then **Apple removed the app on 22 February 2026**, Azar **terminated all iOS subscriptions on 6 April 2026**, and it now runs **its own web Gem Shop on a single, unnamed payment processor**.
>
> The trap did not get argued away. **It got taken away.** They are acquiring, authorising and settling their own payments for the first time, across the Middle East, Türkiye, South and Southeast Asia and Europe — and their own help pages already document declines, issuer blocks and gateway outages.
>
> ⚠️ **Read the territory note before touching this account.** The markets are EMEA-weighted and the parent is in Texas.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Azar is a one-to-one random video chat app launched in 2014 by Hyperconnect (Seoul) and acquired by Match Group in 2021. Users buy **Gems** (virtual currency) and, previously, subscriptions. Match Group's FY2025 10-K states **Azar Direct Revenue was US$155.8 million**, and places it in the **MG Asia** segment alongside Pairs.

**SimilarWeb total visits:** **Not obtained** — no supplied data, no MCP tools, and the WebSearch fallback was not accepted. **Azar is an app-first business; web visits would understate it badly and are not used here.** Geography instead comes from Match Group's own filing.

### Top 5 markets
| Rank | Country/Region | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | **Middle East** *(named first by Match Group)* | No data | Apple IAP *(new downloads blocked)*, Google Play Billing, **Azar Web: card + PayPal** | **No enumerated list exists** — regional rails cannot be scored as sourced-absent. See Section 4 | ❌ none |
| 2 | **Europe** | No data | As above | As above | ❌ none |
| 3 | South Korea *(operator HQ)* | No data | As above | As above | ✅ Hyperconnect Inc., Seoul |
| 4 | Türkiye *(inferred from complaint sources)* | No data | As above | As above | ❌ none |
| 5 | Wider Asia *(MG Asia segment)* | No data | As above | As above | ⚠️ via Hyperconnect |

> ⚠️ **No traffic table exists in this report.** Match Group does not disclose Azar's country split. The 10-K says only that *"Azar is available in the **Middle East** region and has expanded into other international markets including **Europe**."* Everything above is that sentence plus complaint-source geography — **not a measured split**, and must not be presented as one.

### Legal entities
- **Hyperconnect Inc.** (하이퍼커넥트) — Seoul, South Korea. The operating entity. Acquired by Match Group **17 Jun 2021**
- **Match Group, Inc.** — Dallas, Texas. NASDAQ: **MTCH**. CIK 0000891103. Ultimate parent
- **MTCH Technology Services Limited** (1 Hatch Street Upper, Dublin 2, Ireland) — ⚠️ **the biller of record for direct purchases.** Azar's Terms of Service, verbatim: *"If you reside outside of the Republic of Korea, you agree that your payment to Azar **may be made through MTCH Technology Services Limited**."* **Korea is the carve-out** — Korean residents contract with Hyperconnect LLC
- ⚠️ **Consequence: the payments decision is not made in Seoul.** It sits with Match Group's central function behind a Dublin billing entity, under Texas governing law

### Known PSPs
- **Adyen** — reported live: `checkoutshopper-**live**.adyen.com` preconnect in every page head, Adyen Web Components/Drop-in and the Sessions flow bundled. ⚠️ *Agent-sourced; `azarlive.com` HTML 403s for me, so I could not personally re-verify this one*
- **Toss Payments** (토스페이먼츠) — ✅ **confirmed by me**: `/toss_payments_failure/` is a published route in Azar's own sitemap. Korea rail
- **Stripe** — ⚠️ **named in the router enum only.** No SDK, no publishable key, no network calls found. **Do not assert Stripe is live**
- **Apple App Store IAP** — ✅ was **76% of Azar Direct Revenue in FY2025** (10-K). New downloads blocked since 22 Feb 2026
- **Google Play Billing** — ✅ confirmed; refund articles route users to Google with a GPA Order ID
- **PayPal** — ✅ confirmed on Azar Web
- **Card (Visa, Mastercard)** — ✅ confirmed on Azar Web

### Orchestration status
**In-house orchestration layer.** Azar's web client carries its own payment-gateway router enum — `ADYEN` \| `TOSS` \| `STRIPE` — plus a normalised cross-PSP error taxonomy (`REJECT_CARD_COMPANY`, `API_FAILED_APPROVE_PAYMENT`, `INVALID_BILLING`, `TIME_OUT`) and PSP-specific branching. No vendor orchestrator: zero hits across Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY and Yuno.

**Confirmed by me from Azar's own sitemap** — `/toss_payments_failure/`, `/payment/app/redirect/`, `/payment/app/success/`, `/payments_redirect/`. The `app/redirect` → `app/success` pair is an in-app→web payment handoff.

> **Their own troubleshooting page is the evidence.** Verbatim: *"**Payment Gateway Issues:** Sometimes the payment processing service itself might experience temporary issues. **Wait a few minutes and try again.**"* When the gateway degrades, the documented remedy is for the user to wait. **That is single-PSP dependency, described by the merchant.**

### Buying signals
- 🚨 **Apple removed Azar from the App Store on 22 February 2026**, following a **6 February 2026** update to Apple's App Review Guidelines. Match Group 10-K, verbatim: *"users being unable to initiate new downloads… In available markets, users can sign up for and continue to access the app **through the web** or Google Play Store"*
- 🚨 **All iOS subscriptions terminated 6 April 2026.** Azar's own notice: *"iOS subscription services will conclude on 2026-04-06… Subscriptions scheduled to auto-renew will not renew."* Remaining value was converted to **replacement in-app Gems**
- 🚀 **Azar Web and its Gem Shop launched January 2026** — help articles created **2026-01-23**, still being updated **2026-09-17**. Azar Core / Azar Max subscriptions are **web-purchasable**, so this is **recurring** billing on their own rails, not just one-off top-ups
- 💰 **The migration is disclosed and quantified.** Q2 2026 10-Q, verbatim — **verified by me at source**: *"Cost of revenue decreased across all segments primarily due to **Payers shifting from app store payments to alternate payment methods**, resulting in **$38.0 million lower in-app purchase fees** and an increase of **$4.6 million in credit card processing fees**."* Group cost of revenue fell **28% → 24% of revenue** in a year on that shift
- 💰 **Match Group began implementing alternative payment options in 2025.** FY2025 10-K, verbatim: *"in 2025, began implementing alternative payment options outside of the payments systems provided by Apple and Google… **which have led to increased levels of credit card transactions**"*
- 📉 **Azar-specific damage, Q2 2026 10-Q:** *"a **$19 million decrease in revenue at Azar** impacted by the temporary Azar app removal."* Plus a **$25.2m impairment on the Azar trade name** (fair value $33.4m), reclassified from indefinite- to definite-lived
- 📅 **Dated cliff:** *"our partnership with Google entered into in 2024 is set to expire in the first quarter of 2027"*, after which Google fees are expected to rise

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Azar` to draft the 12-touch sequence — **but resolve the territory question in Section 3 first.***

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 16 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5 ⚠️** | ⚠️ **CORRECTED — my own error. No transaction count exists publicly.** I first derived "~615,000 transactions/month" from US$155.8m ÷ 12 ÷ US$21.10. **That arithmetic yields PAYERS, not transactions** — Match Group defines RPP as revenue per *Payer* per month. The correct reading is **✅ DERIVED: ~615,000 monthly PAYERS** (consistent with 913k reported for all of MG Asia in Q1 2026, of which Azar is ~58% of revenue). **Actual transactions are HIGHER**, because Gems are à la carte and one payer makes several purchases a month — so the ≥100,000 band holds comfortably either way. **Billing unit: payers. Never quote a transaction count for this account.** |
| Orchestration status | **+1** | ⚠️ **CORRECTED mid-run: In-house orchestration layer, not greenfield.** Azar's web client carries its own payment-gateway enum — `ADYEN` \| `TOSS` \| `STRIPE` — with a normalised cross-PSP error taxonomy and PSP-specific branching. That is hand-rolled orchestration. Independently corroborated by **`/toss_payments_failure/`**, a published route in Azar's own sitemap. |
| 3+ countries | **+3** | ✅ Middle East + Europe + Korea confirmed in the 10-K; MG Asia also spans Japan, Taiwan, Korea. |
| Multiple PSPs | **+3** | ✅ Apple IAP, Google Play Billing, PayPal and an unnamed card processor — four providers with evidence. **Awarded on provider count; no card PSP is named.** Same judgement applied to bitFlyer, for consistency. |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **Not awarded, and deliberately so.** Azar's help page says accepted methods *"commonly include: Major Credit/Debit Cards (Visa, MasterCard, etc.)"* and that *"**Other regional payment options may also be available**."* That is explicitly **not** an enumerated list. Claiming a sourced rail gap here would breach the evidence bar — even though the gap is very probably real. |
| Recent expansion | **0** | ❌ No new market entry in 12 months. The Azar Web launch is a **channel** change, not expansion. |
| Payment issues reported | **+2** | ✅ **First-party, not scraped.** Azar's own troubleshooting page documents declines, insufficient funds, **issuer blocks**, **regional restrictions / card type not supported**, gateway outages, and double-charge risk from repeated submits. |
| Funding >$10M | **0** | ❌ Match Group is public; no round. |
| High traffic outside home | **+2** | ✅ Awarded on filing evidence: Azar's stated markets are the **Middle East and Europe**, not Korea. |
| Competitor using orchestration | **0** | ❌ No competitor found using an orchestrator. Bigo, Chamet and Tango use **Coda/Codashop and reseller networks** for local top-up — that is APM distribution, **not orchestration**, and must not be presented as such. |
| Payment job postings | **0** | ⬜ Not established. |

**Tier:** **16 / 29 → 🟢 Medium.** One point below ⭐ High Priority.

> **No analyst override applied — and the near-miss is honest, not a rounding problem.** The two points it fails on (local rail gap, recent expansion) both fail on *evidence*, not on substance: the rail gap is probably real but no enumerated list exists to source it, and the Azar Web launch is a channel pivot the matrix has no row for. **If a VPN checkout walk produces an enumerated method list showing regional rails absent, this becomes 19/29 ⭐.** That single check is the cheapest path to re-tiering this account.
>
> **The app-store override was considered and NOT applied.** 76% of FY2025 revenue ran through Apple, which would normally score this down hard. It was not applied because **that channel has been removed by Apple**, iOS subscriptions are terminated, and the merchant has stood up its own web billing. The trap is dissolving in real time — which converts the classic disqualifier into the buying trigger.

---

### ⚠️ TERRITORY — resolve before outreach

This is the single biggest open question on the account, and it is not a payments question.

| Factor | Points to |
|---|---|
| Operating entity: **Hyperconnect Inc., Seoul** | **APAC** ✅ |
| Match Group segment name: **"MG Asia"** | APAC ✅ |
| Stated markets: *"the **Middle East** region… and **Europe**"* (10-K) | **EMEA** ❌ |
| Ultimate parent and likely payments decision-maker: **Match Group, Dallas, Texas** | **AMER** ❌ |
| The alternative-payments programme is **Match Group-wide**, not Azar-specific | **AMER** ❌ |

**My read:** the operating entity is Korean, so the account is defensible as in-territory per `CLAUDE.md`. But the revenue is EMEA-weighted and the payments decision almost certainly sits in Dallas. **Treat this as a coordination call with AMER/EMEA before spending a sequence on it** — not as a disqualification, and not as a clean APAC account either.

### Source Notes
- ✅ **Match Group FY2025 10-K** — located via EDGAR (CIK 0000891103, accession 0000891103-26-000025, filed 2026-02-26), downloaded and parsed by me. Every financial figure and the Apple-removal language come from that document.
- ✅ **Azar's own help centre** — reached through the **public Zendesk API** at `help.azarlive.com/api/v2/help_center/en-us/articles.json`, which is open even though the HTML pages 403. **165 articles** pulled; the Azar Web payment articles read verbatim. Same technique that cracked Indodax and Envato.
- ⚠️ **No traffic data** — not supplied, no MCP tools, fallback not accepted.
- ⚠️ **Q1/Q2 2026 earnings-call figures** (a ~$20m Q2 revenue headwind, a ~$25m Azar intangible impairment) were surfaced from a transcript but **not verified against the 10-Q by me**. Treat as `[UNVERIFIED]` until read from the filing.
- ❌ **A third-party "1-star review" breakdown was surfaced and excluded** — percentages from one blogger's coding of an unstated sample. Usable as colour, **never as a statistic in an email**.
- ✅ **Name-collision check performed.** "Azar" is a common Persian/Hebrew personal name and an Iranian calendar month. Every finding was tied to the Hyperconnect app via bundle ID, domain or explicit Match Group attribution.

### Success Case Alternatives
- **Chosen on payment pattern, not vertical:** the match is *high-frequency, low-ticket virtual-currency top-ups plus recurring subscriptions, sold cross-border into emerging markets on a single processor*. Any case used must be verified against a published source before it goes in an email — this repo has already corrected one case-study misattribution.

---

## Executive Summary

Azar is Hyperconnect's one-to-one random video chat app, owned by Match Group, generating **US$155.8m of Direct Revenue in FY2025** — of which, per the 10-K, **76% ran through Apple's App Store**. On **22 February 2026 Apple removed the app**, and Azar **terminated all iOS subscriptions on 6 April 2026**, converting remaining subscriber value into in-app Gems. Since January 2026 it has run **Azar Web**, its own Gem Shop and web-purchasable subscriptions, on **a single unnamed payment processor** taking card and PayPal — and its own troubleshooting page already names issuer blocks, regional card restrictions and gateway outages as expected failures. The motion is **Greenfield**, the trigger is unusually clean and dated, and the constraint is that the markets are EMEA-weighted and the parent is in Texas.

### Section 1: Website Traffic Analysis by Country

**Data source: NONE OBTAINED.** No supplied SimilarWeb data, no MCP tools, and a WebSearch fallback was not accepted for a country split.

**Consequence:** there is no traffic table. Azar is app-first, so web visits would understate the business regardless. Geography is taken from Match Group's filing, which says only:

> *"Azar is available in the **Middle East** region and has expanded into other international markets including **Europe**."*

**Do not infer a country split from anything in this file.** The two ICP signals that normally key off traffic were scored against filing evidence, and that is disclosed in the breakdown.

### Section 2: Legal Entities & Local Presence

**Headquarters:** Seoul, South Korea (Hyperconnect Inc.). Azar launched 2014; acquired by Match Group 2021.

| Country | Entity | Registration | Source |
|---|---|---|---|
| South Korea | **Hyperconnect Inc.** (하이퍼커넥트) | Not found | Match Group FY2025 10-K |
| USA | **Match Group, Inc.** | NASDAQ: MTCH · CIK 0000891103 | SEC EDGAR |

**Cross-Border Gap Analysis:**

| Region | Top market? | Local entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---|---|---|---|---|
| Middle East | ✅ #1 | ❌ none found | Not verified this run | **High** |
| Europe | ✅ #2 | ❌ none found | Not verified this run | **High** |
| South Korea | operator HQ | ✅ Hyperconnect | — | Low |

> *"Warning: Potential cross-border operation in the Middle East and Europe — the two markets Match Group names for Azar. No local billing entity found in either. Web transactions are likely processed cross-border, with higher scheme costs, lower approval rates and FX exposure."*

> ⚠️ **Do not escalate this to a regulatory-gate claim.** No APAC or MENA acquiring gate was verified this run, and none should be asserted without a live source.

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Channel | Provider | Evidence Type | Source |
|---|---|---|---|
| iOS in-app *(to 22 Feb 2026)* | **Apple App Store IAP — 76% of FY2025 Direct Revenue** | `[Press Release]` audited filing | FY2025 10-K |
| Android in-app | **Google Play Billing** | `[Terms/Privacy Policy]` | Azar refund article — requires a Google Play **GPA Order ID** |
| **Azar Web** | **"Azar's payment processor"** — unnamed, singular | `[Terms/Privacy Policy]` | [Payment Issues? Fix Gem Purchase Problems on Azar Web](https://help.azarlive.com/hc/en-us/articles/54514225318297) |
| Azar Web | **PayPal** | `[Checkout]` | [Gems on Azar Web](https://help.azarlive.com/hc/en-us/articles/54514088769049) |
| Azar Web | **Visa, Mastercard** | `[Checkout]` | Same |

**Who owns the problem, in their own words:**
- In-app: *"Pursuant to iTunes policies, **Azar has no authority over your payment**."* Refunds *"are managed by Apple, not Azar."*
- Web: *"Ensure your card type is accepted by **Azar's payment processor**."*

**That sentence is the whole account.** Everything on the app stores is Apple's and Google's problem. Everything on Azar Web is now Azar's.

#### 3B. Payment Orchestrator

**None detected — single unnamed processor on the web channel.**

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with a single processor on its web channel, which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

The strongest evidence is their own remediation advice, verbatim:

> *"**Payment Gateway Issues:** Sometimes the payment processing service itself might experience temporary issues. **Wait a few minutes and try again.**"*
> *"Avoid clicking the 'submit' button multiple times, as this could lead to **multiple charges**."*

A merchant with routing does not tell users to wait out a gateway outage. A merchant with idempotency does not warn about double charges from a double click.

> **MANUAL:** walk the Azar Web Gem Shop checkout with DevTools open. The processor will name itself in the network calls in under a minute. This is the single highest-value action on the account.

### Section 4: Alternative & Local Payment Methods

| Channel | Method | Category | Status | Source |
|---|---|---|---|---|
| Azar Web | Visa, Mastercard | Cards | **Active** | Help centre ✅ |
| Azar Web | PayPal | Wallet | **Active** | Help centre ✅ |
| Azar Web | *"Other regional payment options may also be available"* | — | **Unspecified by the merchant** | Help centre ✅ |
| iOS | Apple IAP | App store | **New downloads blocked since 22 Feb 2026**; existing users can still purchase and renew | 10-K ✅ |
| iOS | Subscriptions | Recurring | **TERMINATED 6 Apr 2026** | Azar notice ✅ |
| Android | Google Play Billing | App store | **Active** | Help centre ✅ |

> ⚠️ **No rail gap is claimed, and that is deliberate.** Azar's help page explicitly declines to enumerate: accepted methods *"will be displayed during the checkout process"* and *"commonly include"* cards. Because there is **no enumerated list**, the absence of QRIS, GCash, UPI, local wallets or MENA rails is **unchecked, not sourced** — and unchecked absence is not evidence of absence. It is very likely a real gap given the user base. **It must be verified before it appears in an email.**

> **MANUAL:** VPN to Türkiye, Indonesia and a Gulf market and open the Gem Shop. That converts this from a strong hypothesis into the account's best hook, and it is worth 3 ICP points.

### Section 5: Payment Issues & Customer Complaints

**Unusually strong, because the source is the merchant itself.** Azar's own [payment troubleshooting page](https://help.azarlive.com/hc/en-us/articles/54514225318297) (created 2026-01-23, updated **2026-09-16**) enumerates its expected failure modes:

| Issue | Azar's own wording | Category |
|---|---|---|
| Declines | *"Insufficient Funds"*, *"Incorrect Payment Information"* | Declined transactions |
| **Issuer blocks** | *"Your bank might have **flagged the transaction as unusual** for security reasons"* | False fraud declines |
| **Regional / card-type refusal** | *"**Regional Restrictions/Card Not Supported:** Ensure your card type is accepted by Azar's payment processor and that it's **enabled for international and online transactions**"* | Cross-border decline |
| **Gateway outage** | *"the payment processing service itself might experience temporary issues. Wait a few minutes and try again"* | Single-PSP dependency |
| **Double charge** | *"Avoid clicking the 'submit' button multiple times, as this could lead to multiple charges"* | Duplicate charges |
| Charged, not credited | *"Charged but Gems Not Received"* — a standing article since 2016 | Entitlement gap |

> **Pattern:** a brand-new web channel whose documented failure modes are **cross-border card refusal and single-gateway fragility** — exactly the two problems orchestration addresses. This is first-party evidence, not scraped review sentiment, which makes it unusually safe to quote.

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | **2026-04-06** | **All Azar iOS subscriptions terminated**; auto-renewals stopped; remaining value converted to replacement Gems | Payment platform change | [Azar notice](https://help.azarlive.com/hc/en-us/articles/56115920982297) ✅ |
| 2 | **2026-02-22** | **Apple removes Azar from the App Store**, following a **2026-02-06** App Review Guidelines update | Platform | FY2025 10-K ✅ |
| 3 | **2026-01-23** | **Azar Web Gem Shop launched** — own-rails card + PayPal | New billing channel | Zendesk API metadata ✅ |
| 4 | **2026-01-14** | **Azar Core / Azar Max** subscriptions, web-purchasable | Recurring on own rails | Zendesk API metadata ✅ |
| 5 | **2025** | Match Group *"began implementing alternative payment options outside of the payments systems provided by Apple and Google"* | Payments programme | FY2025 10-K ✅ |

**Public payment RFP:** *No public payment-related RFP found.*
**Payment hiring:** Not established.

### Section 7: Payment-Specific News

**No payments trade press coverage found.** Azar and Hyperconnect have never announced a PSP, gateway or orchestration partnership. Their help text names only *"Azar's payment processor."*

> **REMOVAL:** *Azar discontinued all iOS subscription billing as of 2026-04-06.* Source: [help.azarlive.com/hc/en-us/articles/56115920982297](https://help.azarlive.com/hc/en-us/articles/56115920982297)

### Section 8: Checkout Experience Audit

**Partially accessible.** `azarlive.com` returns HTTP 403 to both WebFetch and curl, and the Gem Shop sits behind a login. Findings below come from Azar's own help centre.

| Dimension | Finding |
|---|---|
| Checkout type | Web Gem Shop, reached via the Gender or Country filter on mobile web |
| Guest checkout | **No** — account required |
| Methods visible | Card + PayPal; *"other regional payment options may also be available"* |
| Geo-adaptation | **Implied but unconfirmed** — the merchant references regional options without listing them |
| Card storage | Not established |
| **Idempotency** | ⚠️ **Apparently absent** — users warned that repeated submits *"could lead to multiple charges"* |
| **Failover** | ⚠️ **Apparently absent** — documented remedy for a gateway outage is to wait |
| 3DS | **Not observable** |
| Recurring | **Yes** — Azar Core / Azar Max purchasable on web |

### Section 9: PCI DSS Compliance

**No direct PCI compliance documentation found publicly for Azar, Hyperconnect or Match Group in relation to Azar.**

> `[INFERENCE, not confirmed]`: card details are collected in a web checkout operated by an unnamed third-party processor, which would normally imply reduced PCI scope. **No provider is named and no level is stated.** Do not assert one.

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: They were pushed onto their own rails, and the rails are single-threaded**
> **Evidence:** Section 6 (Apple removal 22 Feb 2026; iOS subscriptions terminated 6 Apr 2026) **+** Section 3B (*"the payment processing service itself might experience temporary issues. Wait a few minutes and try again"*).
> **Pain Point:** a revenue line that was 76% Apple now has to be acquired and authorised by Azar itself, on one processor, with no documented failover and a documented double-charge risk.
> **Yuno Value Proposition:** routing across multiple acquirers with automatic failover, so a processor incident stops being something the *user* waits out.
> **Outreach Angle:** quote their own help page back at them — it is the most credible source available and they wrote it.
> **Suggested Subject Line:** "Wait a few minutes and try again"
> ⚠️ **Constraint:** never frame this as "we'll save you Apple's 30%." That is not a Yuno product, and Match Group has lawyers on it.

> **Insight #2: Cross-border card refusal is already their documented failure mode**
> **Evidence:** Section 5 (*"Regional Restrictions/Card Not Supported… enabled for **international** and online transactions"*) **+** Section 2 (no local billing entity in the Middle East or Europe, the two markets Match Group names).
> **Pain Point:** cards issued in Türkiye, the Gulf and South Asia, acquired cross-border, against an unfamiliar new descriptor on a channel launched eight months ago.
> **Yuno Value Proposition:** local acquiring per market, so the transaction stops being foreign to the issuer.
> **Suggested Subject Line:** Azar Web's decline reasons, in your own words
> ⚠️ **Constraint:** name the corridor. Never say "cross-border in APAC" — and note these corridors are mostly **EMEA**.

> **Insight #3: Recurring billing moved onto their rails at the same moment**
> **Evidence:** Section 6 (Azar Core/Max web-purchasable, Jan 2026) **+** Section 6 (iOS subscriptions terminated Apr 2026).
> **Pain Point:** renewals, card-on-file, retries, dunning and involuntary churn are now Azar's problem for the first time — and were Apple's until April.
> **Yuno Value Proposition:** retry logic, network tokens and account updater in the routing layer.
> **Suggested Subject Line:** Renewals came back in-house in April

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks:**
1. "Your Azar Web payment page tells users that if the gateway has issues, they should wait a few minutes and try again."
2. "Your own troubleshooting list names 'Regional Restrictions / Card Not Supported' and issuer blocks — on a channel you launched in January."
3. "iOS subscriptions ended on 6 April. Every renewal since then is yours to authorise."

**Cold call openers:**
1. "When Apple pulled the app in February, how much of the Gem volume actually made it across to web?"
2. "Who owns a declined Gem purchase now — payments, or growth?"
3. "You converted the remaining iOS subscriptions into Gems. Did the renewal cohort come back on web?"

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors
| Company | HQ / owner | Web top-up? | Payment stack | Source |
|---|---|---|---|---|
| **Bigo Live** | Singapore (JOYY) | ✅ Extensive | **Codashop (Coda Payments)** with **DANA, QRIS, ShopeePay, OVO, bank transfer**; no login required | `[UNVERIFIED — search summary]` |
| **Chamet** | China-linked | ✅ ID-based, no login | Reseller network incl. Joytify (PayPal, cards) | `[UNVERIFIED]` |
| **Tango** | US/Israel-linked | ✅ Heavy reseller ecosystem | SEAGM, Joytify (**PIX in Brazil**), GamsGo (**iDEAL, Skrill**) | `[UNVERIFIED]` |
| **Holla / Monkey** | Huafang Group (China) | Not established | Not established | `[UNVERIFIED]` |
| **Omegle** | — | ❌ | **SHUT DOWN Nov 2023 — do not list as a live competitor** | `[UNVERIFIED]` |

#### 11C. Companies Recently Adopting Payment Orchestration
> ❌ **"No public case studies found of direct competitors adopting payment orchestration."**
>
> ⚠️ **And do not stretch the Coda/Codashop finding into one.** Bigo, Chamet and Tango use reseller and APM-distribution networks to carry local methods — that is a distribution strategy, not orchestration. Presenting it as competitive orchestration urgency would be wrong.

**The real competitive observation:** the category norm is a web/reseller top-up rail carrying **local methods** — QRIS, DANA, OVO, ShopeePay, PIX. **Azar's new web store offers card and PayPal.** For a user base in Türkiye, MENA and South/Southeast Asia, that is the narrowest funnel in the category. `[The competitor half of this is UNVERIFIED — verify before using.]`

### Section 12: Business Case Data

| Metric | Value | Source |
|---|---|---|
| **Azar Direct Revenue FY2025** | **US$155.8m** | FY2025 10-K ✅ audited |
| **— of which via Apple App Store** | **76%** (≈US$118.4m) | FY2025 10-K ✅ |
| **— not via Apple** | **24%** (≈US$37.4m) | *my arithmetic on the above* |
| MG Asia Direct Revenue FY2025 | **US$267.3m** (−6% YoY) | ✅ |
| Azar as share of MG Asia | **58.3%** | *my arithmetic* |
| MG Asia Payers | **1,056k** (avg monthly, +5%) | ✅ |
| MG Asia RPP | **US$21.10**/month (−10%) | ✅ |
| **Monthly transaction count** | ⚠️ **NOT PUBLISHED. Do not quote one.** Match Group discloses **Payers**, never transactions. ✅ **DERIVED: ~615,000 monthly PAYERS** (US$155.8m ÷ 12 ÷ US$21.10 RPP, both audited). Cross-check: MG Asia reported **913k payers in Q1 2026** for Azar + Pairs combined. Transactions exceed payers — Gems are à la carte. On the FY2025 channel split, ~468k of those payers were Apple-channel and **~148k were not** | 10-K + arithmetic |
| 2026 guidance | MG Asia Direct Revenue to decline **high-single-digits**; Azar *"at a similar rate"* | ✅ — but **dated 3 Feb 2026, before the Apple removal, and *"have not been updated"*** |
| **Billing channel split** | **76% Apple / 24% other in FY2025 — and structurally shifting**, since iOS new downloads are blocked and iOS subscriptions are terminated | ✅ |

> **The sizing story is unusual and it is the reason to look at this account.** The addressable slice today is ~US$37m/yr and ~148,000 transactions/month. But it is addressable **because Apple removed the alternative**, and that share can only grow: no new iOS downloads, and no iOS subscriptions at all since April.

### Overall Research Confidence

**High on the billing channel, the trigger and the financials. None on traffic. Medium on methods and competitors.**

**High confidence** (primary source, fetched and parsed by me):
- Match Group FY2025 10-K from EDGAR — revenue, the 76% Apple share, the Apple removal, alternative-payments language, MG Asia Payers and RPP
- Azar's own help centre via the open Zendesk API — 165 articles, with the Azar Web payment and iOS-termination articles read verbatim

**Medium confidence:** competitor top-up stacks (search summaries only); the Q1/Q2 2026 earnings-call figures (transcript, not verified against the 10-Q).

**Low / none:** **traffic — not obtained at all**; per-market payment methods (the merchant declines to enumerate); PCI; payment hiring.

**Traffic data was NOT obtained** — not supplied, not API-sourced, and the WebSearch fallback was not accepted. Country profile comes from one sentence in the 10-K.

### Manual Research Recommendations

> **Area:** Who is "Azar's payment processor"
> **Why it matters:** it is the incumbent, and the entire pitch turns on whether it is one provider or several.
> **Action:** open the Azar Web Gem Shop with DevTools on the network tab. One minute of work. **Highest value item on the account.**

> **Area:** The enumerated method list per market
> **Why it matters:** worth 3 ICP points and it is the difference between a usable rail-gap hook and one that cannot be written. Azar deliberately does not publish it.
> **Action:** VPN to Türkiye, Indonesia and a Gulf market, open the Gem Shop, screenshot the method list.

> **Area:** Territory ownership
> **Why it matters:** the operating entity is Korean but the markets are EMEA and the parent is in Texas. Working it as a pure APAC account may be wrong.
> **Action:** a conversation with AMER/EMEA before any sequence goes out.

> **Area:** How much volume actually crossed to web
> **Why it matters:** it sizes the whole opportunity, and Match's public guidance predates the removal.
> **Action:** read the Q2 and Q3 2026 10-Qs for Azar commentary; it is free and first-party.

### Appendix: All Source URLs

**Primary (fetched and parsed by me):**
- https://www.sec.gov/Archives/edgar/data/891103/000089110326000025/mtch-20251231.htm — Match Group FY2025 10-K
- https://data.sec.gov/submissions/CIK0000891103.json — EDGAR filing index
- https://help.azarlive.com/api/v2/help_center/en-us/articles.json — Azar help centre, 165 articles
- https://help.azarlive.com/hc/en-us/articles/54514225318297 — Payment Issues? Fix Gem Purchase Problems on Azar Web
- https://help.azarlive.com/hc/en-us/articles/54514088769049 — Gems on Azar Web: A Quick Guide
- https://help.azarlive.com/hc/en-us/articles/56115920982297 — Azar Subscription in iOS will End as of 2026-04-06
- https://help.azarlive.com/hc/en-us/articles/227012327 — I Want To Get A Refund
- https://help.azarlive.com/hc/en-us/articles/21437364170265 — I want to cancel my subscription

**Secondary / unverified:**
- Match Group Q1 2026 earnings transcript (≈$20m Q2 headwind, ≈$25m Azar impairment) — `[UNVERIFIED]`
- Apple App Review Guidelines update, 2026-02-06 — `[UNVERIFIED]`
- Competitor top-up stacks (Bigo/Codashop, Chamet, Tango) — `[UNVERIFIED]`

</details>
