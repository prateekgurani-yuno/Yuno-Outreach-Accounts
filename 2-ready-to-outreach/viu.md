# Viu

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 14 / 24 → ⭐ High Priority
**Industry:** OTT / subscription video streaming · **HQ:** Hong Kong (PCCW Limited, HKEX: 0008) · **Researched:** 2026-09-17 · **First email sent:** —
**Motion:** **Greenfield** — no orchestrator detected. But see the ⚠️ below before any outreach is drafted.

---

> ## ⚠️ THIS ACCOUNT IS ALREADY IN FLOW — AND ITS CENTREPIECE CLAIM IS REFUTED
>
> **1. Viu is not a new prospect.** `accounts/apac-tal.csv` row 732 records **STAGE = `Contacting`**, LAST ACTIVITY `In Flow`, and *"Already did research, can target as a P1."* Viu is also **Sample 1 in `.claude/reference/email-samples.md`** — the ~700-word long-form first touch that is this repo's voice anchor. **An email has already been sent to this account.**
>
> **2. The Adyen claim in that sent email is not supported by any source.** The email states: *"your Terms name Adyen as 'Viu's authorised direct credit card and debit card payment gateway'."* I fetched Viu's actual Terms & Conditions and **Adyen appears zero times. No PSP is named anywhere in the document.** Full evidence in Section 3A. This needs a decision from Prateek, not a quiet correction — it has already gone to a prospect.
>
> **3. `/full-outreach` must NOT be run on this file until (2) is resolved.** The existing sequence would inherit the refuted claim.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Viu is PCCW's pan-regional subscription video streaming service, built on Korean, Chinese and local-language drama. It runs across **15 markets** in Southeast Asia, the Middle East and South Africa, reaching **16.8 million paid subscribers** (excluding Myanmar) at December 2025. The commercial shape that matters for payments: a very high-frequency, low-ticket recurring book (tiers as short as **3-day ฿15** and **R7/day**) collected across at least four distinct billing channels — own-checkout cards, ~11 telco direct-carrier-billing relationships, Apple/Google in-app purchase, and a voucher reseller.

**SimilarWeb total visits:** **Not obtained.** No traffic data was supplied (`accounts/traffic/viu.md` does not exist), no SimilarWeb MCP tools are configured, and a WebSearch fallback was not treated as sufficient. **Geography in this report is therefore taken from PCCW's audited FY2025 disclosure, not from traffic.** That is the better source here — but it means two ICP signals that normally key off traffic share were scored against filing evidence instead, and that is stated where it happens.

### Top 5 markets *(by PCCW's own statement of performance, not traffic)*
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | **Thailand** | No data | **AIS** carrier billing, **True/TrueID** carrier billing, **TrueMoney Wallet** (dedicated Viu landing page), Visa/Mastercard | **PromptPay — NOT FOUND, and NOT sourced-absent.** No enumerated TH method list was reachable | ❌ none confirmed |
| 2 | **Indonesia** | No data | **Telkomsel** pulsa + **IndiHome** add-on; via Coda: GoPay, **DANA**, **QRIS**, **ShopeePay**, **OVO**, **LinkAja**, DOKU Wallet, bank VA, Indomaret, Alfamart, Kredivo | None established | ❌ none confirmed |
| 3 | **Malaysia** | No data | **CelcomDigi** (≥6 distinct Viu products), Apple IAP (10 MYR tiers), Visa/Mastercard | **FPX, Touch 'n Go — NOT FOUND, and NOT sourced-absent.** No enumerated MY list reachable | ❌ none confirmed |
| 4 | **Singapore** | No data | **Singtel CAST**, **Singtel Prepaid**, **StarHub TV+** add-on (S$10.98/mo) | PayNow, GrabPay — Not found | ⚠️ PCCW OTT Singapore Pte Ltd referenced in hiring listings, not registry-confirmed |
| 5 | **Hong Kong** *(home)* | No data | **1O1O / csl** bundle, **SUN Mobile** "Viu Premium Lite", Visa/Mastercard | PayMe, FPS, Octopus — Not found | ✅ PCCW OTT Hong Kong Limited (Apple developer-of-record) |

*Also in the 15: Philippines (Globe carrier billing, Coda/GCash), Vietnam (nothing found — cannot confirm Viu sells directly), South Africa (MTN airtime + card, Vodacom), UAE/Bahrain/Egypt/Saudi and the rest of MENA.*

> **Territory note.** Viu's 15 markets include Middle East and South Africa, which sit with **EMEA**. Per `CLAUDE.md`, an **APAC-HQ'd company is in scope** — HQ is Hong Kong, and the buying centre sits there. Worth a word with EMEA before touching the Gulf-facing side.

### Legal entities
- **PCCW Limited** — Hong Kong, **HKEX: 0008**. Parent.
- **Vuclip Middle East FZ LLC**, d/b/a Viu — **the merchant of record on Viu's own checkout.** Its T&C state: *"United Arab of Emirates is our country of domicile."* UAE free-zone entity.
- **PCCW OTT Hong Kong Limited** — the registered Apple App Store developer (listed as "Vuclip, Inc. (PCCW OTT Hong Kong Limited)").
- **Vuclip, Inc.** — legacy US entity name still carried on the Apple listing.
- **PCCW OTT Singapore Pte Ltd** — referenced in hiring listings `[UNVERIFIED — not registry-confirmed]`.
- **Canal+** holds **36.8%** of Viu — see Buying signals.

### Known PSPs
- ⚠️ **NO card PSP or acquirer is named anywhere.** Viu's own T&C says only that card details *"will be provided directly to **our payment provider** via a secured connection"* — singular, unnamed. This is the central gap in the account.
- **Coda Payments / Codashop** — ✅ confirmed voucher and local-method reseller channel (Indonesia, Philippines). Page names Viu as *"PCCW's leading pan-regional OTT service."*
- **SLA Digital** — ✅ confirmed direct-carrier-billing aggregator, but **MENA only and dated 28 Mar 2018**; no evidence it still holds.
- **Apple App Store IAP** — ✅ confirmed live (10 published MYR price tiers).
- **Google Play IAP** — ✅ confirmed as a live channel.
- **~11 telco direct-billing relationships** across 8 markets — AIS, True, Telkomsel, CelcomDigi, Globe, Singtel, StarHub, 1O1O/csl, SUN Mobile, MTN, Vodacom.
- ❌ **Adyen — REFUTED.** See Section 3A.

### Orchestration status
**None detected — direct integrations only (greenfield).** Zero hits for Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY or Yuno. No payments trade press (thepaypers, pymnts, finextra) has ever covered a Viu PSP or billing-vendor partnership.

> ⚠️ **Honest limit:** absence of a *public* orchestrator is weak evidence — most merchants never announce one. The stronger circumstantial signal is the **estate shape**: 4+ billing channel types, ~11 telco relationships, a reseller and a separate MENA aggregator, across 15 markets, with no visible unifying layer.

### Buying signals
- 💰 **Canal+ holds 36.8% of Viu and has a discretionary path to majority.** Verified by my own fetch of [Variety](https://variety.com/2024/film/news/canal-viu-asia-streaming-1236042925/): the stake rose to 36.8%, releasing *"the last instalment of its $300 million staggered investment"*, and — verbatim — *"A further investment, at Canal+'s discretion, could lift its ownership stake in Viu to 51%."* **A streamer whose largest minority holder has a funded, live option to control is under sustained pressure to show EBITDA expansion — and payment cost and involuntary churn sit directly on that line.**
- 📈 **FY2025 delivered exactly that expansion:** OTT EBITDA **+56% to HK$620m**, margin **16% → 24%**, subscription revenue **+13%** ([PCCW annual results](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0210/2026021000398.pdf)).
- 🚀 **HBO Max bundle live in five markets since Dec 2025** — a cross-company billing integration, described by PCCW as *"first-of-its-kind."*
- 🚀 **Viu Shorts launched Jan 2026** — micro-drama format, >11% viewership penetration in three weeks. Micro-transactions at micro-tenor.
- 🤝 **A second bundle, with iQIYI, across four SEA markets** — *"billed together but consumed separately"* `[UNVERIFIED — search summary only, paywalled]`. Two multi-party billing integrations inside ~6 months.
- 💼 **A payments architect role in Hong Kong** *(conflicting evidence — see Section 6; one agent found it, another found nothing, and no posting date was established. Do not cite it without confirming it is live.)*

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated — and **blocked** pending the Adyen decision above. An email has already been sent to this account; see `.claude/reference/email-samples.md` Sample 1. Run `/full-outreach Viu` only after Prateek decides how to handle the refuted claim.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 14 / 24
| Signal | Points | Status |
|--------|--------|--------|
| Orchestration status | **+4** | ✅ None detected — greenfield. Zero hits across 9 orchestrators + trade press. Caveat on public-absence noted above. |
| 3+ countries | **+3** | ✅ **15 markets**, stated in PCCW's audited FY2025 results. |
| Multiple PSPs | **+3** | ✅ Coda Payments, SLA Digital, Apple IAP, Google Play IAP and ~11 telco billing rails all confirmed with evidence. **Awarded on provider count, not card-PSP count** — the card acquirer is unnamed. Stated plainly because it is a judgement call. |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **Not awarded.** Thailand and Malaysia have no reachable enumerated method list, so PromptPay/FPX/TnG absences are *unchecked*, not sourced. Indonesia is well covered via Coda. Awarding this would breach the sourced-absence bar. |
| Recent expansion | **+2** | ✅ HBO Max bundle, five markets, Dec 2025; Viu Shorts, Jan 2026. Both in the PCCW filing. |
| Payment issues reported | **0** | ⬜ Complaint pattern found (payment taken, entitlement not provisioned) but **every supporting fetch failed** — all `[UNVERIFIED]`. Not scored. |
| Funding >$10M | **0** | ❌ Canal+'s $300m is real but its final instalment was **June 2024** — outside the 12-month window. Scored honestly at zero despite being the most interesting fact in the file. |
| High traffic outside home | **+2** | ✅ Awarded on filing evidence, not traffic: PCCW names **Thailand, Indonesia and Malaysia** as its strongest markets; Hong Kong is not among them. |
| Competitor using orchestration | **0** | ❌ **Zero streaming/OTT companies anywhere** were found publicly using any orchestrator. There is no competitive-urgency angle here and one must not be manufactured. |
| Payment job postings | **0** | ⬜ Conflicting agent evidence, no posting date, no fetch. Not scored. |

**Tier:** ⭐ **High Priority (14)** — but note it clears the 14 threshold by exactly one point, and two of the awards (Multiple PSPs, High traffic outside home) are reasoned judgements rather than clean matrix hits. Treat it as a strong Medium that earns High on estate complexity.

**Analyst override considered and NOT applied — read this before pitching:**
> The app-store trap (`subscription-payments.md` §4) is the documented `not-icp` failure mode for consumer subscriptions, and **Apple IAP and Google Play IAP are both confirmed live here.** The override was not applied because **the billing-channel split could not be established from any source** — PCCW's filing contains zero mentions of Apple, Google, "app store" or "in-app", and no help page or filing breaks out the mix.
>
> One suggestive data point, offered as hypothesis only: the **iOS-path T&C does not mention iTunes billing at all**, listing only Visa/Mastercard/carrier/wallets — which hints that Viu's own rails are the default even inside the iOS app. A T&C's silence is not proof.
>
> **This is the single question that decides whether this account is real.** It is the first thing to ask on a call, and it is a discovery question, not a claim.

### Source Notes
- ✅ **PCCW FY2025 annual results** downloaded from HKEX and text-extracted locally with pypdf. All financial and market-count figures here come from that document, not from search summaries.
- ✅ **Viu's real T&C** fetched first-hand from `static.viu.com` — the host is **not** geo-gated, unlike `www.viu.com`.
- ✅ **Canal+ 36.8% and the 51% option** verified by my own fetch of Variety, not taken from an agent summary.
- ✅ **shopviu.com GTC** fetched first-hand to test the contamination theory in Section 3A.
- ⚠️ **No traffic data** — not supplied, no MCP tools, fallback not accepted.
- ⚠️ **Complaints (Section 5) are entirely unverified** — all five of that agent's fetches failed (403s and a paywall).
- ❌ **A Trustpilot "2.2-star" rating was surfaced and killed.** No Trustpilot profile appears to exist for the Viu streaming service; the figure traced to a single AI-generated aggregator and was echoed back across multiple queries — a citation loop, not corroboration. **Do not use it.**

### Success Case Alternatives
- Deliberately left thin. The one thing this account most needs — a named streaming/OTT orchestration case study — **does not appear to exist publicly in any region.** Any success case used here should be chosen on *payment pattern* (high-frequency low-ticket recurring, multi-market, multi-channel) rather than on vertical, and every number attached to it must be verified against a published source before it goes in an email. This repo has already had one case-study misattribution corrected (see `air-new-zealand.md`, the Viva Aerobus/NOVA correction).

---

## Executive Summary

Viu is PCCW's pan-regional streamer: 16.8m paid subscribers across 15 markets in SEA, the Middle East and South Africa, run out of Hong Kong with a UAE free-zone entity as merchant of record on its own checkout. The defining payment fact is **channel fragmentation, not acquiring**: subscriptions are collected through own-checkout cards, roughly eleven telco direct-carrier-billing relationships across eight markets, Apple and Google IAP, and a voucher reseller — with no unifying layer visible and **no card PSP named in any public document**. The commercial pressure is real and datable: Canal+ owns 36.8% with a discretionary, fully-funded option to 51%, and FY2025 was a margin story (OTT EBITDA +56%, margin 16%→24%). The motion is **Greenfield**, with the caveat that the strongest available wedge is reconciliation and entitlement across channels rather than card approval rates.

### Section 1: Website Traffic Analysis by Country

**Data source: NONE OBTAINED.** No pasted SimilarWeb data, no MCP tools, and a WebSearch fallback was not accepted as sufficient for a country split.

**Consequence, stated plainly:** there is no traffic table in this report. Geography is taken from PCCW's audited statement instead, which is a *better* source for this particular company but is not substitutable for share-of-traffic. The two ICP signals that normally key off traffic ("3+ countries", "high traffic outside home") were scored against filing evidence and that is disclosed in the breakdown. **Do not infer a country split from anything in this file.**

PCCW's own words (FY2025 results, p.2): Viu operates *"across 15 markets in Southeast Asia ("SEA"), the Middle East, and South Africa"* and *"Strong performance was particularly evident in **Thailand, Indonesia, and Malaysia**."*

One external cross-check worth recording: Media Partners Asia data reported by Deadline puts Viu at **9.9m SEA subscribers** (Q2 2025), #2 regionally behind Netflix `[UNVERIFIED — search summary only]`. That does not contradict the 16.8m global figure but **anyone citing a subscriber number must say which one and cite it.** A wrong scale number in a first email to PCCW ends the conversation.

### Section 2: Legal Entities & Local Presence

**Headquarters:** Hong Kong. Parent PCCW Limited (HKEX: 0008).

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Hong Kong | PCCW Limited | HKEX 0008 | [HKEX filing](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0210/2026021000398.pdf) |
| **UAE** | **Vuclip Middle East FZ LLC** (d/b/a Viu) | Not found | [Viu T&C](https://static.viu.com/pages/viu_ios/p-all/34/en/tc.html) — *"United Arab of Emirates is our country of domicile"* |
| Hong Kong | PCCW OTT Hong Kong Limited | Not found | Apple App Store developer-of-record |
| US (legacy) | Vuclip, Inc. | Not found | Apple App Store listing |
| Singapore | PCCW OTT Singapore Pte Ltd | Not found | `[UNVERIFIED — hiring listings only]` |

**Cross-Border Gap Analysis:**

| Country | Top market? | Local entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------|---------------|---------------------------|---------------------|
| Thailand | ✅ #1 | ❌ none confirmed | Not verified this run | **High** — but largely mitigated by telco rails |
| Indonesia | ✅ #2 | ❌ none confirmed | Not verified this run | **High** — mitigated by Telkomsel + Coda |
| Malaysia | ✅ #3 | ❌ none confirmed | Not verified this run | **High** — mitigated by CelcomDigi |
| Hong Kong | home | ✅ yes | — | Low |

> **Warning: the merchant of record on Viu's own checkout is a UAE free-zone entity (Vuclip Middle East FZ LLC) acquiring into 15 markets spanning SEA, MENA and South Africa.** On the card slice of the book, that is a textbook cross-border approval-rate and FX exposure — cards issued in Bangkok, Jakarta and Kuala Lumpur acquired against a Dubai entity.
>
> ⚠️ **But do not overstate it.** The telco rails carry an unknown and possibly dominant share of volume, and those do not touch card acquiring at all. The cross-border argument applies **only to the direct-billed card slice**, whose size is unknown. Argue it per corridor, and only after establishing the mix.

> **MANUAL:** No APAC regulatory acquiring gate was verified this run. Do not assert one for Thailand, Indonesia or Malaysia without sourcing it live.

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|---|---|---|---|
| Global (own checkout) | **UNNAMED** — *"our payment provider"* | `[Terms/Privacy Policy]` | [static.viu.com T&C](https://static.viu.com/pages/viu_ios/p-all/34/en/tc.html) |
| Indonesia, Philippines | **Coda Payments / Codashop** | `[Checkout]` — merchant page, fetched | [codashop.com/id-id/viu-premium-kode-voucher](https://www.codashop.com/id-id/viu-premium-kode-voucher) · [codashop.com/en-ph/viu](https://www.codashop.com/en-ph/viu) |
| MENA (2018) | **SLA Digital** — carrier billing aggregator | `[Press Release]` — vendor release naming Vuclip as *"a PCCW Media company"* | [sla-digital.com](https://sla-digital.com/news/sla-digital-vuclip-carrier-billing/) |
| Global | **Apple App Store IAP** | `[Checkout]` — 10 published MYR tiers | [apps.apple.com/my/app/viu/id1044543328](https://apps.apple.com/my/app/viu/id1044543328) |
| Global | **Google Play IAP** | `[Third-Party Report]` | Google Play community cancellation threads |
| 8 markets | **~11 telco DCB rails** | `[Press Release]` / telco first-party pages | See Section 4 |

> ### ❌ THE ADYEN CLAIM IS REFUTED — four independent lines of evidence
>
> The claim: *"your Terms name Adyen as 'Viu's authorised direct credit card and debit card payment gateway'."* (Sample 1, already sent.)
>
> **1. Viu's actual T&C names no PSP at all.** I fetched it myself. `Adyen` = **0**. `Stripe`, `Checkout.com`, `Worldpay`, `Braintree`, `2C2P`, `Xendit`, `Midtrans`, `DOKU`, `iPay88`, `Omise`, `Razorpay`, `PayU` = **0 each**. The strings `payment gateway`, `payment service provider` and `authorised` = **0 each**. The complete accepted-methods sentence is, verbatim:
>
> > *"User has the option to pay via Visa, Mastercard, Carrier Billing, Wallets."*
>
> and on card handling, only:
>
> > *"the details you are asked to submit will be provided directly to **our payment provider** via a secured connection."*
>
> **2. The exact quoted phrase does not exist on the indexed web.** An exact-phrase search for *"Viu's authorised direct credit card and debit card payment gateway"* returns **zero** pages.
>
> **3. The Adyen association traces to a different company.** `shopviu.com` is **VIU Eyewear** (VIU Deutschland GmbH), a German/Swiss glasses retailer. I fetched its GTC: `Adyen` appears **6 times**, in standard German e-commerce boilerplate — *"If a payment method offered via the payment service 'Adyen' is selected, payment is processed via the payment service provider Adyen N.V., Simon Carmiggeltstraat 6-50, 1011 DJ, Amsterdam."* Unrelated to PCCW.
>
> **4. But even that page does not contain the quoted wording.** `"authorised direct credit card"` = **0** on shopviu.com too. So this is **not a clean misattribution** — the Adyen *association* can be explained by the eyewear company, but the specific quoted sentence appears to have been **generated, not quoted from anywhere**.
>
> **Verdict: Adyen is not evidenced as a Viu PSP, and the "quote" is not a quote.** It must not be used again. Because it has already been sent, this is Prateek's call, not a silent file edit.
>
> **Wider implication worth acting on:** the failure mode is a search-summary assertion hardening into a quoted fact. It is worth auditing whether any other account file in this repo carries a PSP claim sourced the same way.

#### 3B. Payment Orchestrator

**None detected — direct PSP integrations only (greenfield).**

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with multiple providers and channels, which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

Searched against Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY and Yuno: zero hits. No payments trade press has ever covered a Viu PSP, gateway, orchestration or billing-vendor partnership.

> **MANUAL:** Walk the live checkout from a **residential IP in Thailand, Indonesia or Malaysia** with DevTools open. Inspect network calls and CSP headers on the payment page. This resolves the unnamed-acquirer question in minutes and is by far the highest-yield remaining action — everything reachable from a datacentre IP has been exhausted.

### Section 4: Alternative & Local Payment Methods

| Country | Method | Category | Status | Source |
|---|---|---|---|---|
| Global | Visa, Mastercard | Cards | **Active** | Viu T&C |
| Global | Carrier Billing | Carrier | **Active** | Viu T&C |
| Global | "Wallets" (unnamed) | Wallet | **Active as a category only** | Viu T&C |
| Global | Apple IAP | App store | **Active** | Apple listing (10 MYR tiers) |
| Global | Google Play IAP | App store | **Active** | Play community threads |
| Indonesia | GoPay, DANA, QRIS, ShopeePay, OVO, LinkAja, DOKU Wallet | Wallet / A2A | **Active** (Coda channel) | Codashop ID, fetched |
| Indonesia | Bank VA, Indomaret, Alfamart, Kredivo | A2A / cash / BNPL | **Active** (Coda channel) | Codashop ID, fetched |
| Indonesia | Telkomsel pulsa, IndiHome add-on (Rp39,000/mo) | Carrier | **Active** | telkomsel.com |
| Malaysia | CelcomDigi — **≥6 distinct Viu products** | Carrier | **Active** | help.celcomdigi.com |
| Thailand | AIS (฿149/mo), True/TrueID, TrueMoney Wallet | Carrier / wallet | **Active** | ais.th · true.th · truemoney.com/viu |
| Singapore | Singtel CAST, Singtel Prepaid, StarHub TV+ (S$10.98/mo) | Carrier | **Active** | singtel.com · starhub.com |
| Philippines | Globe (SMS "VIU99" to 8080), GCash via Coda | Carrier / wallet | **Active** | globe.com.ph/apps/viu |
| Hong Kong | 1O1O/csl bundle, SUN Mobile "Viu Premium Lite" | Carrier | **Active** | 1010.com.hk/viu |
| South Africa | MTN airtime (R7/day, R45/mo), card | Carrier / cards | **Active** | play.mtn.co.za, fetched |
| Thailand | **PromptPay** | A2A | **NOT FOUND — not sourced-absent** | No enumerated TH list reachable |
| Malaysia | **FPX, Touch 'n Go** | A2A / wallet | **NOT FOUND — not sourced-absent** | No enumerated MY list reachable |
| Vietnam | MoMo, ZaloPay, VNPay | Wallet | **Not found** | Cannot confirm Viu sells directly in VN |
| Middle East | du, e&, Zain, STC, Fawry, mada | Carrier / cards | **Not found** | Weakest region in this report |

> ### ⚠️ THREE PRIOR CLAIMS CORRECTED
> The already-sent email asserts three method absences. On the evidence:
>
> | Claim | Verdict |
> |---|---|
> | *"Your pages name GoPay as the only wallet in Indonesia — no DANA, OVO, ShopeePay or QRIS"* | **REFUTED.** Codashop's Viu page enumerates GoPay, **DANA, QRIS, ShopeePay, OVO, LinkAja and DOKU Wallet**. Viu's own T&C also says *"Wallets"*, plural. (Caveat: Coda is a reseller channel, not proven to be viu.com's own checkout — but as stated, the claim is wrong.) |
> | *"Malaysia shows no Touch 'n Go or FPX"* | **UNSUPPORTABLE AS WRITTEN.** No enumerated Malaysian method list was reachable. This asserts an absence without an enumerating source. |
> | *"Thailand no PromptPay"* | **UNSUPPORTABLE AS WRITTEN.** Same reason. What *can* be said: the Thai wallet story is **TrueMoney-led** — TrueMoney runs a dedicated Viu landing page. |
>
> **One claim the email got right, and it is the good one:** *"CelcomDigi alone runs four different Viu products"* is an **undercount** — at least **six** distinct CelcomDigi Viu products have their own help articles (postpaid bundle, prepaid SpeedSTREAM, prepaid StreamMORE 5GB, Mega Add-Ons, free Premium on a MegaJimat 12-month device contract, and free 24-month Premium with 5G Home WiFi). **Telkomsel's "two"** (mobile pulsa + IndiHome) **is confirmed**, arguably three with IndiHome Movie tiers.

> **MANUAL:** VPN to Thailand and Malaysia and walk the checkout. Converting the two "NOT FOUND" rows into sourced verdicts is the difference between a usable rail-gap hook and one that cannot be written.
>
> **Cheap lead worth taking first:** `static.viu.com/pages/viu_ios/p-all/{N}/en/tc.html` is **not geo-gated** and is numbered (v10 and v34 both exist). Walking other `{N}` values, other locales, and other platform slugs (`viu_android`, `viu_web`) may surface market-specific terms that enumerate methods.

### Section 5: Payment Issues & Customer Complaints

> ⚠️ **Every item in this section is `[UNVERIFIED]`.** The assigned agent's five fetch attempts all failed (403s, a truncated Play page, and an HTTP 402 paywall). Nothing here was read on the page. **Do not put any number, rating or quote from this section into an email.**

| Issue Type | Platform | Frequency | Date Range | Source |
|---|---|---|---|---|
| **Payment taken, entitlement not provisioned** — user pays, app still shows free tier | Google Play, viu.com web | Moderate–high (4 separate Play Community threads) | 2018–2025 | support.google.com/googleplay/thread/94164192, /181533218, /218864144, /417795482 |
| **Channel-of-purchase confusion → refund deadlock** — paid by card, support says it's a Play sub, neither owns the refund | Card vs Play IAP | Isolated but illustrative | Undated | justanswer.com |
| **Cancellation friction** — auto-debit continues after app deletion; guides tell users to cancel 3 days early | DANA, ShopeePay, Play, Telkomsel | Moderate (≈6 Indonesian publishers wrote cancellation guides) | 2024–2025 | gadgetren.com, kumparan.com |
| **Telco-bundle lock-in** — cancelling a CelcomDigi postpaid Viu add-on before 12 months kills access *and* triggers an early termination fee | CelcomDigi | Structural policy | Current | help.celcomdigi.com |

> **Pattern — and it reframes the pitch.** The dominant complaint is **not** card decline. It is *payment succeeded, entitlement not granted*, plus *cancellation routed to the wrong billing channel*. With Apple IAP, Google IAP, direct card, wallets and ~11 telco rails all live, **every channel is a separate entitlement webhook**. That is a reconciliation-and-entitlement problem, which is a better-evidenced wedge than approval rates.
>
> ❌ **Involuntary churn / failed recurring payment: NO evidence found.** Not one complaint said "my card was declined at renewal." **The retry/dunning angle cannot be claimed on this account** — which matters, because it is the angle the existing email leads with.

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | Jan 2026 | **Viu Shorts** launched — micro-drama; >11% viewership penetration in 3 weeks | Product | [PCCW FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0210/2026021000398.pdf) ✅ |
| 2 | Dec 2025 | **Viu–HBO Max bundle** live in 5 markets; *"first-of-its-kind"* | Partnership | PCCW FY2025 ✅ |
| 3 | 2026 (APOS) | **Viu × iQIYI bundle**, 4 SEA markets, *"billed together but consumed separately"* | Partnership | `[UNVERIFIED — paywalled]` |
| 4 | Jun 2024 | **Canal+ raises stake to 36.8%**, final instalment of $300m; option to 51% at its discretion | Ownership | [Variety](https://variety.com/2024/film/news/canal-viu-asia-streaming-1236042925/) ✅ fetched |
| 5 | Jun 2023 | Canal+ agrees initial 26.1% for $200m; $300m staggered total | Ownership | Bloomberg / Variety `[UNVERIFIED]` |

**Public payment RFP:** *No public payment-related RFP found.*

**Payment hiring — CONFLICTING EVIDENCE, do not cite without checking.** One agent surfaced a *Lead Engineer / Solution Architect — online payment solutions* role in Kowloon Bay, Hong Kong, whose requirements reportedly name subscription/recurring billing, fraud, chargebacks, reconciliation and multi-region HA. A second agent searching the same boards **found no payment roles at all**. Neither fetched a posting, and **no posting date was established**. If live, it is both the best-timed opening in the account *and* a build-not-buy alarm. **Verify before referencing — a cold email citing a closed req reads badly.**

**Myanmar:** excluded from the 16.8m subscriber count via footnote 5 (*"Exclude Myanmar"*) in PCCW's results. **No source was found explaining why.** Do not assert a reason — divestment, sanctions, licensing and payment-rails failure are all consistent with the footnote. It is a good discovery question.

### Section 7: Payment-Specific News

**No public information found.** Zero results for Viu or PCCW OTT across thepaypers.com, pymnts.com and finextra.com. Viu has made **no announced PSP, gateway, orchestration or billing-vendor partnership** that the payments trade press has covered.

> Read that as **greenfield, not as "already solved."**

### Section 8: Checkout Experience Audit

**Not accessible in this environment.** `www.viu.com` is **hard geo-gated**: every market path and locale tested (SG, ID, MY, TH, HK, PH, and root) returned `200` on `https://www.viu.com/ott/no-service/` from this datacentre IP. This is merchant-side geo-blocking, not a proxy denial.

Partial findings from the archived Next.js build, recovered via the Wayback Machine:
| Dimension | Finding |
|---|---|
| Route structure | The complete route list (23 routes) contains **no checkout, payment or billing route**. Subscription lives under `/member`, `/member/[slug]` and `/premium`. |
| Login / identity | An **iframed "universal login" endpoint** on a separate origin, with `OFFER_FAILURE` and `offerId` callbacks — offers are handled inside the iframe. |
| Identity key | The terms chunk references **`msisdn`** — phone-number-keyed identity, consistent with carrier billing. |
| Cancellation | Via a *"My Subscription"* page (Viu's own T&C). |
| Billing cadence | **Monthly, weekly or daily.** |
| Refunds | 12-hour window, unwatched content only, *"within 2 to 45 days."* |
| 3DS | **Not observable.** |

### Section 9: PCI DSS Compliance

**No direct PCI compliance documentation found publicly for Viu or PCCW.** The only card-handling statement is in the T&C: *"All credit/debit cards' details and personally identifiable information will NOT be stored, sold, shared, rented or leased to any third parties"*, alongside *"provided directly to our payment provider via a secured connection."*

> `[INFERENCE, not confirmed]`: that wording is consistent with card data being handled by a third-party processor rather than stored by Viu, which would imply reduced PCI scope. **No provider is named and no compliance level is stated anywhere.** Do not assert a level.

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: Four billing channel types, one entitlement problem**
> **Evidence:** Section 4 (Apple IAP + Google IAP + ~11 telco rails + own-checkout cards + Coda reseller) **+** Section 5 (dominant complaint is *payment succeeded, entitlement not granted*, across 4 Play Community threads and 6 Indonesian cancellation guides).
> **Pain Point:** every channel is a separate entitlement webhook and a separate reconciliation. A payment can succeed in one system while access fails in another, and a cancellation can be routed to a party that does not own the billing.
> **Yuno Value Proposition:** one layer that pulls each provider's settlement file, matches it against what was actually billed, and flags every break — with transactions, refunds and disputes in one view.
> **Outreach Angle:** the asymmetry is inside their own stack and they cannot dispute either half — the telco rails retry a subscriber until the balance tops up, while the card book gets one attempt.
> **Suggested Subject Line:** Four billing channels, one entitlement gap
> ⚠️ **Constraint:** Section 5 is entirely unverified. Frame as an observation about *architecture* (which is sourced), never by citing a complaint volume (which is not).

> **Insight #2: A UAE entity acquiring into 15 markets**
> **Evidence:** Section 2 (merchant of record is **Vuclip Middle East FZ LLC**, *"United Arab of Emirates is our country of domicile"*) **+** Section 1 (strongest markets are Thailand, Indonesia, Malaysia).
> **Pain Point:** on the card slice, locally-issued cards in Bangkok, Jakarta and KL are acquired cross-border against a Dubai entity — approval-rate drag plus FX.
> **Yuno Value Proposition:** routing to local acquirers per geography through one integration.
> **Outreach Angle:** name the corridor, never "APAC cross-border."
> ⚠️ **Constraint:** applies **only** to the direct-billed card slice, whose share is unknown. Do not lead with this until the channel mix is established.

> **Insight #3: Two multi-party bundles in six months**
> **Evidence:** Section 6 (HBO Max, 5 markets, Dec 2025 — PCCW's own filing) **+** the iQIYI bundle, 4 SEA markets, *"billed together but consumed separately"*.
> **Pain Point:** each bundle is another revenue share to split and reconcile, across markets where billing already runs through different telcos.
> **Yuno Value Proposition:** one integration absorbs new partners and markets rather than a per-deal billing build.
> **Outreach Angle:** the bundle strategy is working and is accelerating — the reconciliation surface grows with each one.
> **Suggested Subject Line:** Two bundles, six months, four billing paths

> **Insight #4: The margin story has an owner watching it**
> **Evidence:** Section 6 (Canal+ 36.8%, *"could lift its ownership stake in Viu to 51%"*) **+** FY2025 (OTT EBITDA +56%, margin 16%→24%, subscription revenue +13%).
> **Pain Point:** payment cost and involuntary churn land directly on the line the company is being measured against.
> **Outreach Angle:** use as *context for urgency*, never as a prediction.
> ⚠️ **Hard constraint:** pitch it as *"Canal+ has the option and has said it is eyeing majority."* **Never** as "Canal+ is taking over." No 2025 or 2026 exercise announcement exists.

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks:**
1. "Your Terms list payment as Visa, Mastercard, Carrier Billing and Wallets — four channel types, and that's before Apple and Google IAP sit on top of them."
2. "CelcomDigi alone runs at least six distinct Viu products, Telkomsel two. That's eight settlement shapes from two operator groups, before AIS, True, Globe, Singtel, StarHub, csl, MTN or Vodacom."
3. "Your merchant of record is a UAE entity and your three strongest markets are Thailand, Indonesia and Malaysia."

**Cold call openers:**
1. "When a subscriber pays through Telkomsel and access doesn't switch on, who owns that — payments or the telco team?"
2. "You've got daily and weekly tiers alongside monthly. Does the retry logic differ by tenor?"
3. "Two bundles in six months — HBO Max and iQIYI. How much billing work does each new partner create?"

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors
| Company | Website | HQ | Key Markets | Known PSP/Orchestrator | Source |
|---|---|---|---|---|---|
| Netflix | netflix.com | US | All SEA + MENA | Adyen claimed — **treat as logo-wall, unverified** | `[UNVERIFIED]` |
| **iQIYI International** | iq.com | Beijing (intl. domicile unverified) | TH, ID, MY, PH, KR | **Alipay+ (Ant)** for wallet acceptance — *not orchestration* | [technode.global](https://technode.global/2023/04/20/alipay-e-wallet-partnerships-power-iqiyis-fast-asia-expansion/) |
| WeTV / WeTV iflix | wetv.vip | Shenzhen (Tencent) | TH, ID, PH, MY, VN | **Nothing found** | — |
| **Vidio** | vidio.com | Jakarta | Indonesia | **Fortumo** direct carrier billing (2019) | [thefastmode.com](https://www.thefastmode.com/technology-solutions/15607-indonesias-ott-platform-vidio-launches-direct-carrier-billing-with-fortumo) |
| TrueID | trueid.net | Bangkok | Thailand | Nothing found; likely True's own telco rails `[INFERENCE]` | — |
| Shahid (MBC) | shahid.mbc.net | Riyadh/Dubai | MENA | **Paymob** for Egypt e-wallets (Mar 2023) | `[UNVERIFIED — 5 outlets]` |

*Note: Shahid and StarzPlay are EMEA-owned — competitive colour only, not APAC accounts.*

#### 11C. Companies Recently Adopting Payment Orchestration
> ❌ **"No public case studies found of direct competitors adopting payment orchestration."**
>
> Not one streaming, OTT or video-subscription company — in APAC, MENA or anywhere — was found publicly disclosed as a customer of Juspay, Spreedly, Primer, Gr4vy, CellPoint, Payrails, IXOPAY, APEXX, BR-DGE, Corefy or Yuno. **The competitive-urgency angle does not exist for this account and must not be manufactured.** Unattributed vendor-blog figures were surfaced and are deliberately excluded.

**Structural finding that reframes the vertical** `[UNVERIFIED — search summary only]`: the dominant OTT billing pattern in SEA is **telco aggregation**, not direct-to-consumer card checkout — Telkomsel, Astro, Globe, StarHub, AIS and True all stack third-party subscriptions onto the operator bill. If true, the addressable slice for orchestration is the direct-billed book, not the whole subscriber base. **This deserves verification before it shapes a pitch.**

### Section 12: Business Case Data

| Metric | Value | Source |
|---|---|---|
| **OTT Business revenue FY2025** | **HK$2,579m** (+5%) | PCCW FY2025 ✅ audited |
| **OTT Business EBITDA FY2025** | **HK$620m (+56%)**, margin 16% → 24% | ✅ audited |
| **Viu subscription revenue** | **+13% YoY** | ✅ audited |
| **Paid subscribers** | **16.8m** (+1.3m net), excluding Myanmar | ✅ audited |
| SEA-only subscribers | 9.9m (Q2 2025, MPA) | `[UNVERIFIED]` — reconcile before citing |
| Group revenue | HK$40,252m (+7%) | ✅ audited |
| Price points observed | ฿15/3-day · ฿119/mo (TH) · R7/day · R45/mo (ZA) · RM17.90/mo (MY) · Rp43,290/mo (ID) · S$10.98/mo (SG) | Telco and Coda pages |
| **Billing channel split (web vs app store vs telco)** | ❌ **NOT DISCLOSED ANYWHERE** | — |
| Payment cost / take rate | **Not found** — PCCW does not itemise payment costs | — |
| ARPU | Not disclosed | — |

> **Business case sizing requires a discovery call.** Unlike YesAsia or CKH, PCCW does **not** itemise payment or gateway costs in its filings. The revenue and EBITDA lines are audited and solid; everything about cost of acceptance is unknown.
>
> **The micro-tenor detail is the sharpest commercial observation available:** at **฿15 for 3 days** and **R7/day**, this is an extremely high-frequency, low-ticket recurring book. Decline and failure rates compound fast at that cadence, and per-transaction economics matter far more than at a monthly-only price point.

### Overall Research Confidence

**Medium overall. High on financials and corporate structure; Medium on the payment estate; Low on methods-by-market, complaints and checkout — with the cause being environmental, not editorial.**

**High confidence** (primary-source, fetched and extracted by me):
- PCCW FY2025 annual results — downloaded from HKEX, extracted locally with pypdf. All market counts, subscriber and financial figures.
- Viu's real T&C from `static.viu.com` — merchant of record, accepted-method categories, cancellation, refund terms, and the **zero-PSP finding**.
- Canal+ 36.8% and the 51% option — my own fetch of Variety.
- The shopviu.com / VIU Eyewear contamination test — my own fetch.
- The archived Next.js build manifest and terms chunk, via the Wayback Machine.

**Medium confidence:** the telco rail inventory (first-party telco pages, but URL-only — titles unambiguous, pages not read); Coda's Indonesian method list (fetched, but it is a reseller channel, not proven to be viu.com's own checkout).

**Low confidence:** **complaints (Section 5) — all five fetches failed, everything `[UNVERIFIED]`**; methods in Vietnam and the entire Middle East (near-zero findings); checkout (geo-gated, not completable); 3DS and PCI (not observable).

**Traffic data was NOT obtained** — not supplied, no MCP tools, and the WebSearch fallback was not accepted. Geography comes from PCCW's audited statement instead. This is disclosed in the ICP breakdown wherever it affected a score.

**One environment note worth carrying forward:** `web.archive.org` fails from this session unless `curl` is passed `--cacert /root/.ccr/ca-bundle.crt` explicitly. One agent reported the archive as "blocked by egress policy" and abandoned that line of research; with the CA bundle it works fine. Worth putting in the research skill.

### Manual Research Recommendations

> **Area:** The billing-channel split — IAP vs own rails vs telco
> **Why it matters:** **This decides whether the account is real.** Apple and Google IAP are both confirmed live. If IAP dominates, orchestration cannot touch that revenue and this account scores down to `not-icp` regardless of the 14/24.
> **Action:** ask it directly on the first call. It is not publicly sourceable — PCCW's filing contains zero mentions of Apple, Google, app store or in-app.

> **Area:** The unnamed card acquirer
> **Why it matters:** no PSP is named in Viu's own T&C or any third-party source. It determines who the incumbent is and whether this is a greenfield build or a displacement.
> **Action:** walk the live checkout from a **residential IP in Thailand, Indonesia or Malaysia** with DevTools open — network calls and CSP headers will name it in minutes. Everything reachable from a datacentre IP is exhausted.

> **Area:** Enumerated method lists for Malaysia and Thailand
> **Why it matters:** the FPX / Touch 'n Go / PromptPay absences are currently **unchecked, not sourced**, and cannot be written into an email as they stand. They are also worth 3 ICP points.
> **Action:** cheapest first — walk `static.viu.com/pages/viu_ios/p-all/{N}/en/tc.html` across other `{N}` values, locales and platform slugs (`viu_android`, `viu_web`). That host is not geo-gated. Failing that, VPN and walk the checkout.

> **Area:** The Hong Kong payments architect role
> **Why it matters:** if live, it is the best-timed opening in the account — and simultaneously a build-not-buy warning.
> **Action:** open `hk.jobsdb.com/Viu-jobs` and confirm the posting and its date. Cross-check `linkedin.com/company/viuott` for existing payment/billing/monetisation titles: near-zero headcount means build-from-scratch; ten people means they are scaling an in-house stack and the conversation is harder.

> **Area:** Why Myanmar is excluded from the subscriber count
> **Why it matters:** a market removed from a headline metric usually has a reason worth knowing, and it may be a payments reason.
> **Action:** good discovery question. Do not speculate — no source explains it.

### Appendix: All Source URLs

**Primary (fetched and extracted by me):**
- https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0210/2026021000398.pdf — PCCW FY2025 annual results
- https://static.viu.com/pages/viu_ios/p-all/34/en/tc.html — Viu Terms & Conditions (current)
- https://static.viu.com/pages/viu_ios/p-all/10/en/tc.html — older version
- https://variety.com/2024/film/news/canal-viu-asia-streaming-1236042925/ — Canal+ 36.8% and the 51% option
- https://shopviu.com/en-de/gtc — VIU Eyewear GTC (contamination test)
- https://www.codashop.com/id-id/viu-premium-kode-voucher — Indonesian method enumeration
- https://play.mtn.co.za/get/viu-premium-pass/ — South Africa
- https://apps.apple.com/my/app/viu/id1044543328 — Apple IAP tiers

**Secondary / URL-only:**
- https://sla-digital.com/news/sla-digital-vuclip-carrier-billing/
- https://www.codashop.com/en-ph/viu
- help.celcomdigi.com (6 Viu product articles)
- telkomsel.com/indihome/addon/viu · telkomsel.com/jelajah/jelajah-lifestyle/...
- ais.th/consumers/entertainment/streaming-app/viu · true.th/entertainment/streaming/viu · truemoney.com/viu/
- singtel.com/personal/products-services/lifestyle-services/cast/viu-premium · starhub.com/personal/tvplus/add-ons/viu.html
- globe.com.ph/apps/viu · 1010.com.hk/viu · sunmobile.com.hk/eng/value/147.jhtml
- https://deadline.com/2025/07/southeast-asia-streaming-new-subscribers-premium-vod-mpa-1236475172/
- https://technode.global/2023/04/20/alipay-e-wallet-partnerships-power-iqiyis-fast-asia-expansion/
- https://www.thefastmode.com/technology-solutions/15607-indonesias-ott-platform-vidio-launches-direct-carrier-billing-with-fortumo

</details>
