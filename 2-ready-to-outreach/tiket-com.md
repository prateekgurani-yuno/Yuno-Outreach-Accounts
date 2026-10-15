# tiket.com

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 19 / 29 → ⭐ **High Priority**
**Industry:** Online travel agency — flights, hotels, trains, attractions, events · **HQ:** **Jakarta, Indonesia** — `PT Global Tiket Network`, 99.99%-owned by **PT Global Digital Niaga Tbk (Blibli, IDX: BELI)** · **Researched:** 2026-10-15 · **First email sent:** —
**Motion:** ⚠️ **DISPLACEMENT** — **Juspay is confirmed, current, and named in a Juspay case study quoting a tiket.com Senior Product Manager.** Read the two boxes below before writing a line.

---

> ## 🔀 THE MOTION — Juspay is in, and the internal TAL row was right
>
> Our target list carried `Payment Orchestrator = Juspay` as an unverified lead. **It is correct.** I verified the
> source myself: `https://juspay.io/customer-stories/tiket` — **200 at 25,466 B against a 404 control at 19,873 B**, with
> clean token deltas (`Tiket` 33/0, `Arief` 1/0, `GrabPay` 2/0, `FPX` 2/0, `PromptPay` 1/0). Note `orchestration` is
> **37/27** because Juspay's own nav carries it — diffing matters.
>
> Headline, verbatim: ***"Tiket Adds 40 Local Payment Methods with Juspay as it Scales Beyond Singapore"***
> Banner metrics: **40 Local Payment Methods · 15 Currencies · 3 Countries**
>
> > *"Tiket, a fast-growing online travel and entertainment platform based in Indonesia, set out to expand into 10+
> > countries across Southeast Asia…"*
> > *"Until recently, Tiket primarily handled multi-currency acceptance through credit and debit cards."*
> > *"Intelligent Payment Orchestration with smart routing to optimize success rates by location and currency."*
> > — and a named quote from **Arief R Ramadhan, Senior Product Manager, Tiket**.
>
> Products in use: **Express Checkout, Payment Orchestration, Tokenization, Unified Dashboard.** Juspay *"acted as
> Tiket's extended payments team"* and Tiket chose it ***"rather than building integrations in-house."***
>
> ⛔ **Never pitch the case for orchestration.** They have already bought it, and explicitly rejected building it.
>
> ⚠️ **Two honest caveats.** The page says **"Tiket"** and never *"tiket.com"*, *"Blibli"* or *"PT Global Tiket
> Network"* — `tiket.com` and `Blibli` both return **0** on it. Identification rests on Indonesia + OTA + the named PM.
> And there is **no date and no go-live timestamp anywhere on the page or Juspay's newsroom**; "current" rests on a live
> 2026-copyright page with present-tense and forward-looking language.

> ## 🎯 THE HOOK — nobody orchestrates the 87% of the business that is Indonesia
>
> **Juspay covers the cross-border expansion markets. It does not touch Indonesia domestic.** This is the finding, and
> I verified both halves personally.
>
> | | Who runs it | Evidence |
> |---|---|---|
> | **Singapore, Malaysia, Thailand** (~3.4% of web traffic) | **Juspay orchestration** — GrabPay, PayNow, Apple Pay, Google Pay (SG); FPX, DuitNow, GrabPay (MY); Bank Transfer, PromptPay, TrueMoney (TH) | Juspay case study, fetched |
> | **Indonesia** (**86.8%** of web traffic) | **Midtrans, direct** — GoPay, QRIS, Indomaret OTC | infobanknews, fetched |
> | **16-currency international card flow** | **Stripe (Asia-Pacific)**, since May 2023 | TTG Asia, fetched ⚠️ 2023 claim, 2026 status unverified |
>
> **The Juspay page carries ZERO Indonesian rails** — I checked every one: `QRIS` **0**, `GoPay` **0**, `OVO` **0**,
> `DANA` **0**, `ShopeePay` **0**, `LinkAja` **0**, `Alfamart` **0**, `Indomaret` **0**, `Virtual Account` **0**.
> Indonesia appears twice on that page, both times only as *"based in Indonesia"* — never as a served market.
>
> **So the orchestration layer sits on the smallest part of the business and the largest part runs on direct
> integrations.** That is a split stack, and it is the entry point: not "you need orchestration" — they have it — but
> *"why is 87% of your volume outside it?"*

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** tiket.com is one of Indonesia's two largest OTAs, selling flights, hotels, trains, attractions and events.
It was acquired by Blibli in 2017 and now sits inside **PT Global Digital Niaga Tbk**, listed on the IDX as **BELI** —
which means its payment volume is visible in audited public filings. As of June 2026 it carries **151 airlines serving
240+ countries, 3.6m+ accommodation options, ~112,000 activities and 4,500+ events.**

**SimilarWeb: ~9.9M monthly visits (Sept 2026)** `[ESTIMATE, not confirmed]` — third-party, not supplied.
⚠️ **Web only. For an Indonesian OTA the app is very likely the majority channel, so treat 9.9M as a floor, not a measure.**

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇮🇩 Indonesia | **86.8%** | QRIS, GoPay, BCA VA, Indomaret OTC, BCA Mastercard co-brand, Indodana BNPL | OVO/DANA/ShopeePay/LinkAja **not named** — but may be served via QRIS interoperability | ✅ `PT Global Tiket Network` |
| 2 | 🇸🇬 Singapore | 1.32% | GrabPay, PayNow, Apple Pay, Google Pay *(via Juspay)* | — | ❌ none for tiket.com |
| 3 | 🇲🇾 Malaysia | 1.17% | FPX, DuitNow, GrabPay *(via Juspay)* | — | ⚠️ `Global Tiket Malaysia Sdn. Bhd.` — **unverified** |
| 4 | 🇺🇸 United States | 1.17% | Cards, USD *(via Stripe multi-currency)* | — | ❌ none |
| 5 | 🇹🇭 Thailand | 0.87% | Bank Transfer, PromptPay, TrueMoney *(via Juspay)* | — | ❌ none |

All traffic figures `[ESTIMATE, not confirmed]`.

### Legal entities
- **`PT Global Digital Niaga Tbk`** — listed parent, **IDX: BELI**. Sarana Jaya Building, Jl. Budi Kemuliaan I No.1, Gambir, **Jakarta Pusat 10110**.
- **`PT Global Tiket Network`** — the tiket.com operator, acquired 2017, **99.99%** held. App-store seller name confirms it: **"Global Tiket Network, PT"**, bundle `com.mobile.ios.Tiket`.
- **`Global Tiket Network Co., Ltd.`** — **Saitama, Japan, established November 2025** ✅ confirmed from **JETRO**, a Japanese government agency.
- ⚠️ `Global Tiket Malaysia Sdn. Bhd.` (202201044688, Dec 2022) — **unverified**, source 403s.
- Group parent: **PT Global Investama Andalan (Djarum Group)**.

### Known PSPs
- **Juspay** — orchestration, SG/MY/TH cross-border `[Provider Case Study, fetched]`
- **Midtrans** — Indonesia domestic, 7 Mar 2025 `[Press Release, fetched]`
- **Stripe (Asia-Pacific)** — 16-currency international flow, May 2023 `[Press Release, fetched]` ⚠️ 2026 status unverified
- **BCA** — co-brand Mastercard issuing + Virtual Account acceptance `[Provider page, fetched]`
- **Indodana** — white-label lender behind group BNPL

### Orchestration status
**Regional orchestrator confirmed — Juspay — covering cross-border only.** Indonesia domestic shows **no orchestrator**,
which rests on absence. No evidence of Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails or Yuno.

### Buying signals
- 🚀 **Japan entity established Nov 2025** (JETRO, fetched) — *"currently developing its operational framework"*
- 🌏 **Juspay's own page: tiket.com *"plans to enter up to 10 new countries"*** — each a new acquiring problem
- 📉 **3P Retail TPV declined two periods running** (FY25 −2%, 1H26 −4%) while group TPV grew +8%/+12% — a monetisation-over-volume story, from their own filings
- 💰 **No funding round** — tiket.com reportedly raised ~USD 1M from angels only and nothing since the 2017 acquisition
- 💼 **A dedicated payments function exists** — a named Senior Product Manager for payments, plus a Jakarta backend payments role ⚠️ posting text unverified

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach tiket.com` to draft the 12-touch sequence.*

⚠️ **Four hard constraints:**
- **Motion is DISPLACEMENT.** They bought orchestration and explicitly rejected building in-house. **Never make the case for orchestration itself.**
- **Never name Juspay** (or any competitor) in outreach-facing text. Reference "your orchestration layer."
- **Do not pitch "you're missing DANA/OVO/ShopeePay."** QRIS is mandated-interoperable in Indonesia, so a single QRIS acceptance may already reach those users. Asserting a gap we cannot see would be wrong on email one.
- **Lead on the split stack and the 10-country roadmap**, not on rail gaps.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 19 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **5** | ✅ **DERIVED, both inputs sourced from the same filing.** See disclosure below. |
| Orchestration status | **3** | ✅ **Regional orchestrator (Juspay) confirmed** — displacement, already orchestration-aware, short education cycle |
| 3+ countries | **3** | ✅ Four countries above 1% traffic (ID 86.8%, SG 1.32%, MY 1.17%, US 1.17%); plus entities in Indonesia and Japan |
| Multiple PSPs | **3** | ✅ **Midtrans** (domestic) + **Stripe APAC** (cross-border) + **Juspay** (orchestration) — three, independently sourced |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **Rails are well covered and I will not manufacture a gap.** Indonesia has QRIS, GoPay, BCA VA and Indomaret OTC confirmed; SG/MY are served by Juspay. The unnamed wallets may be reached via QRIS interoperability — unresolvable without the checkout. |
| Recent expansion | **2** | ✅ **Japan entity Nov 2025** (JETRO, government source) + a stated 10+ country roadmap on Juspay's own page |
| Payment issues | **0** | ⬜ **NOT RESEARCHED** — the complaints agent had not returned at write time. A gap, **not** a finding of "no complaints". |
| Funding >$10M | **0** | ❌ No round. tiket.com reportedly raised ~USD 1M from angels and nothing since 2017; the parent is listed, not raising. |
| High traffic outside home | **0** | ❌ **Indonesia 86.8%**, far above the 60% threshold |
| Competitor using orchestration | **2** | ✅ **Agoda is on Juspay** — verified by me (`juspay.io/customer-stories/agoda`, 25,891 B vs 20,113 B control, `Agoda` 35/0). **Wego** is a confirmed regional-orchestrator displacement in our own repo at 23/29. |
| Payment job postings | **1** | ⚠️ A payments function is evidenced (named Senior PM for payments; a Jakarta backend payments role) but **the posting text could not be confirmed** — the fetch returned a rotated aggregator page |

**Tier: ⭐ High Priority (17+).** **No analyst override applied.** The score is not inflated by any single fact: volume,
orchestration status, multi-country and multi-PSP each rest on separate, independently sourced evidence, and I scored
**0** on three rows where the evidence did not support a point.

**Note: the score would rise, not fall, with the missing agent.** Payment issues (2) is unassessed, so **19 is a floor.**

### Monthly transaction count — MANDATORY DISCLOSURE

✅ **DERIVED: the segment containing tiket.com runs ~2.58 million orders per month. Both inputs are sourced from the
same earnings release, so this is a derivation, not an assumption.**

**Inputs**, both verbatim from `Earnings-Release-FY25-PT-Global-Digital-Niaga-Tbk.pdf`, which I downloaded and
text-extracted myself (1.92 MB, real text layer):
- **3P Retail TPV FY25 = Rp 53,187 bn.** Units header: *"(Rp bn, unless stated otherwise)"*. 3P Retail is defined as
  *"platform revenue generated from sales of products and services of various categories from third party (3P) sellers
  through its online commerce and online travel agent (OTA) platforms"* — **so it contains tiket.com, alongside
  Blibli's 3P marketplace.**
- **AOV FY25 = Rp 1.72 mn**, defined as *"TPV on online platforms divided by the total number of orders for paid purchases."*

**Arithmetic:** Rp 53,187 bn ÷ Rp 1.72 mn = **30.92 m orders/year = ~2.58 m orders/month** for the segment.
Group-wide (Total TPV Rp 83,316 bn) the figure is **~4.04 m orders/month**.

**Sensitivity — tiket.com's share of the segment is not disclosed, so here is the whole range:**

| tiket.com share of 3P Retail | Orders/month | Band |
|---|---|---|
| 50% | 1,288,000 | **+5** |
| 25% | 644,000 | **+5** |
| 10% | 258,000 | **+5** |
| **5%** | **129,000** | **+5** |
| 2% | 52,000 | clears gate |
| 1% | 26,000 | below gate |

**tiket.com clears the top band at anything above ~4% of the segment**, and GDN's own commentary attributes 3P Retail's
movement *"mainly"* to the OTA business — so the real share is far higher. **Scored 5 with confidence.**

**Billing unit: paid orders.** TPV is defined as *"total value of paid and delivered purchases"*, so this counts
completed bookings, not payment attempts. Actual payment *attempts* will be higher.

### Source Notes
- ✅ **Juspay** — fetched, control-tested, named tiket.com PM quoted
- ✅ **Juspay does NOT cover Indonesia** — nine Indonesian rails all return 0 on that page
- ✅ **Midtrans domestic** — fetched, dated 7 Mar 2025, control-tested
- ✅ **FY25 financials** — PDF downloaded and extracted by me, definitions verbatim
- ✅ **Japan entity** — JETRO, a government source, control-tested
- ✅ **Agoda on Juspay** — fetched, control-tested
- ✅ **Legal seller "Global Tiket Network, PT"** — Apple's app metadata
- ⚠️ **Stripe multi-currency is a 2023 claim** — 2026 status unverified
- ⚠️ **Malaysia entity unverified** — source 403s
- ⚠️ **Traffic is third-party estimate**, web-only, app excluded
- ⚠️ **Checkout never walked** — tiket.com 403s on every path

### Success Case Alternatives
- **An OTA running split domestic/cross-border stacks** — exact profile match.
- ⚠️ **Do not use Agoda or Wego as proof points** — both run the same incumbent we would be displacing.

---

## Section 1: Website Traffic Analysis by Country

**Data source: path 3 — third-party WebSearch/SimilarWeb estimate.** No data was supplied and no MCP tool is configured,
so **everything here is `[ESTIMATE, not confirmed]`** and the country profile is the weakest part of this report.

| Rank | Country | Share | Note |
|---|---|---|---|
| 1 | 🇮🇩 Indonesia | **86.8%** | **high priority** · Indonesia rank #127 · #1 in Travel & Tourism – Other (ID) |
| 2 | 🇸🇬 Singapore | 1.32% | Juspay market |
| 3 | 🇲🇾 Malaysia | 1.17% | Juspay market |
| 4 | 🇺🇸 United States | 1.17% | no entity, no Juspay market — Stripe/cards only |
| 5 | 🇹🇭 Thailand | 0.87% | Juspay market |
| — | Other | 8.66% | |

Global rank **#4,244**. Direct traffic 51.07% (desktop). ~**9.9M monthly visits**, Sept 2026.

⚠️ **Two caveats that materially limit this section.** SimilarWeb covers **web only** — for an app-first Indonesian
consumer brand the app is very likely the larger channel, and **no app-vs-web split is public**. And the **domain estate
is unresolved**: no country subdomains or locale paths were found, and tiket.com appears to handle internationalisation
**inside one site via a currency selector in the user profile** rather than separate country sites.

## Section 2: Legal Entities & Local Presence

**Headquarters: Jakarta, Indonesia.** Registered address printed in the FY25 and 1H26 earnings releases: *Sarana Jaya
Building, Jl. Budi Kemuliaan I No.1, Gambir, Jakarta Pusat, DKI Jakarta 10110.*

| Country | Entity | Reg # | Source |
|---|---|---|---|
| 🇮🇩 Indonesia | **PT Global Digital Niaga Tbk** (IDX: BELI) | not found | FY25 earnings release |
| 🇮🇩 Indonesia | **PT Global Tiket Network** — operates tiket.com, 99.99% | not found | FY25 release p.7; Apple seller name |
| 🇯🇵 Japan | **Global Tiket Network Co., Ltd.**, Saitama — **est. Nov 2025** | — | **JETRO (government), fetched** |
| 🇲🇾 Malaysia | ⚠️ `Global Tiket Malaysia Sdn. Bhd.` | 202201044688 (1490385-H) | **UNVERIFIED — source 403s** |
| 🇸🇬 Singapore | `Global Distribution Niaga Pte. Ltd.` — **a Blibli entity, NOT tiket.com** | — | `[UNVERIFIED]` |

> ⛔ **Three TAL corrections.** Our list said `tiket.com → HQ Country = Australia` — **wrong, it is Indonesia**, and no
> Australian connection was found at all. It also said `Blibli → HQ Country = Singapore` — **also wrong**; the Singapore
> entity is a subsidiary, not the HQ. And `Blibli → Est. Revenue ~$1B (FY24)` is roughly right on **net revenue**
> (Rp 16,716 bn) but **understates the account by roughly 5× as a payment-volume proxy** — for a marketplace/OTA, net
> revenue is a small fraction of TPV. **Use TPV, not revenue.**

**Cross-Border Gap Analysis**

| Country | Top-5 traffic? | Local entity? | Cross-border risk |
|---|---|---|---|
| 🇮🇩 Indonesia | ✅ 86.8% | ✅ | None — domestic |
| 🇸🇬 Singapore | ✅ 1.32% | ❌ | Acquiring runs through the orchestration layer, not a local entity |
| 🇲🇾 Malaysia | ✅ 1.17% | ⚠️ unverified | — |
| 🇺🇸 United States | ✅ 1.17% | ❌ | **Cards only, no local rails, no entity** |
| 🇹🇭 Thailand | ✅ 0.87% | ❌ | — |

> ⚠️ **Deliberately NOT asserted: whether Singapore, Thailand, Japan, Malaysia or the US gate domestic acquiring behind
> local presence.** No sourced regulatory rule was obtained for any of them, and I will not state one from background
> knowledge. **This is a question for the prospect, not a claim for an email.**

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Market / flow | Provider | Evidence | Source |
|---|---|---|---|
| **SG, MY, TH cross-border** | **Juspay** — Express Checkout, Payment Orchestration, Tokenization, Unified Dashboard | `[Provider Case Study]` **fetched, control-tested** | juspay.io/customer-stories/tiket |
| **Indonesia domestic** | **Midtrans** (GoTo group) — "kemitraan strategis", GoPay + QRIS + Indomaret OTC | `[Press Release]` **fetched**, 7 Mar 2025 | infobanknews.com |
| **International, 16 currencies** | **Stripe (Asia-Pacific)** — "Tiket Multi-Currency" | `[Press Release]` **fetched**, 24 May 2023 ⚠️ 2026 status unverified | ttgasia.com |
| **Indonesia** | **BCA** — tiket.com co-brand Mastercard (**issuing**) + Virtual Account (**acceptance**) | `[Provider page]` fetched | bca.co.id |
| **Indonesia** | **Indodana** — white-label lender behind "Blibli Tiket PayLater" | `[Press]` `[UNVERIFIED]` | multiple outlets |

**Explicitly NOT found, searched:** Adyen, Checkout.com, Worldpay, Braintree, Cybersource, Xendit, Doku, Faspay, iPay88,
Espay, Finpay, Winpay. **No named acquiring bank beyond BCA** — who acquires tiket.com's card volume is **unestablished**.

### 3B. Payment Orchestrator

**Classification: Regional orchestrator confirmed — Juspay — on cross-border flows only.**

> *"Confirmed orchestration-aware. The opening is coverage and international reach, not the case for orchestration itself."*

**The presence half is firm** (named case study, named tiket.com PM). **The Indonesia half rests on absence** — I found
no source either way on who orchestrates domestic flow, and the Juspay page's silence on Indonesian rails is strong
circumstantial evidence but not a statement. **Say "no evidence Juspay covers Indonesia", not "Juspay does not cover Indonesia".**

**One competitive wedge worth knowing, and worth handling carefully:** in March 2025 Juspay open-sourced its orchestrator
after **Razorpay, Cashfree and PhonePe terminated partnerships with it**, reportedly over concerns it was prioritising
its own payment-aggregator business. `[UNVERIFIED — search summary only]` That is channel conflict in Juspay's **home**
market, not APAC. **It is a legitimate question to raise, not a fact to assert, and it would read as mud-slinging if
led with.**

## Section 4: Alternative & Local Payment Methods

| Market | Method | Status | Source |
|---|---|---|---|
| 🇮🇩 Indonesia | **QRIS** | ✅ CONFIRMED | infobanknews (fetched) |
| 🇮🇩 Indonesia | **GoPay** | ✅ CONFIRMED | same |
| 🇮🇩 Indonesia | **Indomaret OTC (cash)** | ✅ CONFIRMED | same |
| 🇮🇩 Indonesia | **BCA Virtual Account** | ✅ CONFIRMED | bca.co.id, 10 Jul 2026 (fetched) |
| 🇮🇩 Indonesia | VA — Mandiri, BRI, Permata, CIMB | ❌ NOT FOUND | — |
| 🇮🇩 Indonesia | **Mastercard** (incl. co-brand) | ✅ CONFIRMED | bca.co.id (fetched) |
| 🇮🇩 Indonesia | **Visa, JCB, UnionPay, GPN debit** | ❌ **NOT FOUND** | see the correction below |
| 🇮🇩 Indonesia | OVO · DANA · ShopeePay · LinkAja | ❌ NOT FOUND | **may be served via QRIS — see below** |
| 🇮🇩 Indonesia | Alfamart | ❌ NOT FOUND | Indomaret confirmed; **do not assume symmetry** |
| 🇮🇩 Indonesia | **Blibli Tiket PayLater** (Indodana) | ⚠️ `[UNVERIFIED]` | ~10% of transactions per group CEO; 250k users H1-24 |
| 🇮🇩 Indonesia | Kredivo | ❌ **NOT FOUND — evidence of the opposite**; the original partnership *"was not continued"* | dailysocial `[UNVERIFIED]` |
| 🇮🇩 Indonesia | Bank instalments (cicilan 0%) | ⚠️ `[UNVERIFIED]` — CIMB Niaga, OCBC, BRI promos | bank promo pages |
| 🇸🇬 Singapore | GrabPay, PayNow, Apple Pay, Google Pay | ✅ CONFIRMED | Juspay (fetched) |
| 🇲🇾 Malaysia | FPX, DuitNow, GrabPay | ✅ CONFIRMED | Juspay (fetched) |
| 🇹🇭 Thailand | Bank Transfer, PromptPay, TrueMoney | ✅ CONFIRMED | Juspay (fetched) |
| Global | **16 currencies** — IDR, AUD, CAD, CHF, CNY, EUR, GBP, HKD, JPY, MYR, NZD, PHP, SGD, THB, USD, VND | ✅ CONFIRMED (2023) | ttgasia (fetched) |

> ### ⚠️ Why I am NOT claiming a rail gap in Indonesia
> OVO, DANA, ShopeePay and LinkAja are unevidenced — but **QRIS is a mandated-interoperable national standard, so a
> single QRIS acceptance can reach all of those wallets' users without tiket.com integrating any of them.** The absence
> of named wallet tiles may be an architecture choice, not a coverage gap. **These two cases cannot be distinguished
> without walking the checkout, which is 403.** Pitching "you're missing DANA" could be flatly wrong.

> ⛔ **A correction worth recording.** A search summary attributed *"BCA Debit Mastercard, BCA Credit Card
> (Mastercard/JCB/UnionPay/Visa & Amex)"* to tiket.com. Fetching the page showed that scheme list belongs to **a
> different BCA promotion entirely** (a concert). **Four payment methods would have entered this file as false
> positives.** Visa, JCB, UnionPay and domestic debit are therefore **NOT FOUND**, not confirmed.

**Note the currency list has no KRW, no INR and no TWD** despite the North and South Asia footprint.

## Section 5: Payment Issues & Customer Complaints

**NOT RESEARCHED at write time** — the complaints agent had not returned. **This is an explicit gap, not a finding of
"no complaints found."** For a high-volume consumer OTA, refund-delay and failed-payment complaints would be the
expected categories and the app stores and **mediakonsumen.com** are the places to look.

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | **Nov 2025** | **Global Tiket Network Co., Ltd. established in Saitama, Japan**; *"currently developing its operational framework"* | Market Expansion | **JETRO (fetched)** |
| 2 | **7 Mar 2025** | **Midtrans strategic partnership** for Indonesian domestic rails | Payment Infrastructure | **infobanknews (fetched)** |
| 3 | **FY25 / 1H26** | **3P Retail TPV −2% then −4%** while group TPV +8%/+12%; growth attributed to *"monetization expansion of ancillary revenues in the Company's OTA business"* | Filing | **FY25 + 1H26 releases (fetched)** |
| 4 | undated | **tiket.com *"plans to enter up to 10 new countries"*** | Market Expansion | **Juspay (fetched)** |
| 5 | **24 May 2023** | **Stripe APAC multi-currency, 16 currencies** | Payment Infrastructure | **ttgasia (fetched)** |

**No public payment RFP found.** **No funding round** — tiket.com reportedly raised ~USD 1M from angels and nothing
since the 2017 acquisition `[UNVERIFIED]`.

## Section 7: Payment-Specific News

Covered in Section 6 — the vendor announcements are the payment news. **No provider removal announced**, with one
exception worth noting: **Kredivo's BNPL partnership "was not continued"** and was replaced by in-group Indodana
`[UNVERIFIED — search summary only]`. If accurate, BNPL is now exclusively in-group, which is an exclusivity signal.

## Section 8: Checkout Experience Audit

**Not accessible in this environment.** `tiket.com`, `www.tiket.com` and `blibli.com` return **HTTP 403 on every path**,
verified against a nonsense-path control that 403s at a near-identical size (11,565 / 11,570 / 11,576 B).

| Dimension | Finding |
|---|---|
| Payment methods visible | **Unobserved.** Everything in Section 4 is third-party or vendor-sourced |
| Multi-currency | ✅ 16 currencies, set in **user profile settings**, applying to payments **and refunds** |
| Location-based display | **Unresolved** — and the key question: does a USD/SGD buyer see cards only? |
| 3DS, tokenization, guest checkout, saved methods | **Not determinable.** Tokenization is listed as a Juspay product in use, with no architecture detail |

**Two tiket.com URLs are known to exist and are unreadable:** `tiket.com/info/bliblipay` and `tiket.com/cicilan`.
Those two pages would settle BlibliPay and instalments outright.

## Section 9: PCI DSS Compliance

**No public PCI DSS level, AoC or attestation found for tiket.com.** Every search result was generic PCI educational
material with zero mention of the company.

**Tokenization: present via Juspay** — listed among products in use on the case study (fetched). No detail on scheme vs
network vs PSP tokens, and no vault architecture. **3DS: no public information found** for tiket.com; Juspay markets
3DS as a capability but the case study does not list it.

⚠️ **Indonesian regulatory position deliberately left open.** No current sourced rule on Bank Indonesia processing
domicile or data residency was obtained. **Treat it as an open question, not a known constraint.**

## Section 10: Strategic Insights & Outreach Angles

> ### Insight #1 — The orchestration layer covers 3.4% of the traffic. Indonesia is 86.8%.
> **Evidence:** S3B (Juspay confirmed for SG/MY/TH; nine Indonesian rails all return **0** on that page) + S1 (Indonesia
> 86.8% of web traffic) + S3A (Midtrans direct for domestic, 7 Mar 2025).
> **Pain:** two stacks, two routing logics, two reconciliations — and the bigger one has no routing layer at all. Every
> optimisation they built for Singapore stops at the Indonesian border.
> **Yuno value:** one layer spanning both, so domestic Indonesia gets the same routing, retry and failover as the
> expansion markets.
> **Outreach angle:** they orchestrate the 3%, not the 87%.
> **Subject:** `Indonesia outside the routing layer`

> ### Insight #2 — Their own filings say volume is flat while revenue climbs.
> **Evidence:** S6/S12 (3P Retail TPV **−2% FY25, −4% 1H26** while group TPV **+8%/+12%** and group revenue **+34%/+55%**;
> growth attributed to *"monetization expansion of ancillary revenues"*) + S3 (split stack).
> **Pain:** when volume is flat, margin has to come from the transaction itself — which makes **cost of acceptance and
> approval rate** a P&L lever rather than an ops detail. This is the strongest commercial framing available because it
> comes from their own published numbers.
> **Yuno value:** routing to the cheapest/highest-approval path per BIN and market lifts the same line management is
> already pushing on.
> **Subject:** `Flat TPV, rising take rate`

> ### Insight #3 — Ten new countries, on a layer that today covers three.
> **Evidence:** S6 (Juspay's own page: *"plans to enter up to 10 new countries"*; Japan entity established Nov 2025 per
> JETRO) + S2 (entities confirmed in only Indonesia and Japan; **no entity in Singapore, Thailand or the US**).
> **Pain:** each new market is a fresh acquiring, licensing and local-method problem, and they are currently adding
> markets faster than entities.
> **Yuno value:** coverage depth per market is exactly where an incumbent built for three countries gets tested.
> **Subject:** `Ten countries, three on the layer`

> ### Insight #4 — A 2023 Stripe integration is carrying the entire 16-currency book.
> **Evidence:** S3A (Stripe APAC multi-currency, May 2023, 16 currencies set in profile) + S1 (US 1.17% with **no entity
> and no local rails**) + S4 (no KRW, INR or TWD in the currency list).
> **Pain:** one foreign PSP carrying all non-IDR flow is a single point of failure on the highest-value bookings, and
> the currency list already has holes against their stated footprint.
> ⚠️ **Caveat to respect:** the only source is the 2023 launch. **Ask whether it is still the cross-border rail; do not
> assert that it is.**
> **Subject:** `16 currencies, one rail`

### Quick Hits

**Email hooks:**
1. Your orchestration layer covers Singapore, Malaysia and Thailand — about 3% of your web traffic. Indonesia is 87%.
2. Your own filings show 3P Retail TPV down 2% in FY25 and 4% in 1H26 while group revenue rose 34% and 55%.
3. Juspay's page says you plan to enter up to ten new countries; you have confirmed entities in two.

**Cold call openers:**
1. "You've got routing live across SG, MY and TH — what's handling Indonesia, which is 87% of your traffic?"
2. "Your TPV in the OTA segment has gone backwards two periods running while revenue's up — is cost of acceptance on the table?"
3. "You stood up a Japan entity in November and you're talking about ten more countries. How does acquiring scale with that?"

## Section 11: Similar Companies & Prospecting Pipeline

### 11C. Competitors adopting orchestration — unusually strong, and double-edged

| Company | Orchestrator | Evidence |
|---|---|---|
| **Agoda** | **Juspay** | ✅ **Verified by me** — `juspay.io/customer-stories/agoda`, 25,891 B vs 20,113 B control, `Agoda` 35/0. Juspay opened an APAC hub in Singapore Apr 2025 and signed Agoda for regional orchestration and reconciliation `[UNVERIFIED]` |
| **Wego** | Regional orchestrator confirmed | ✅ Our own prior research — **23/29 ⭐, displacement motion, "confirmed live and publicly expanded"** |
| **tiket.com** | **Juspay** | ✅ This report |

> ⚠️ **Read this honestly: it cuts both ways.** Three major APAC OTAs on the same orchestrator is a strong urgency
> signal — the vertical is consolidating and standing still has a cost. **But it also means Juspay has real vertical
> momentum and reference customers in exactly this segment**, which makes displacement harder, not easier. **Do not use
> Agoda or Wego as proof points in outreach** — they are the incumbent's references, not ours.

### Other peers in the repo
Garuda Indonesia (16/24 ⭐, in-house since 2013) · Lion Air (19/29 ⭐, greenfield) · Grab (17/29, in-house GrabLink, routed to Partnerships).
⚠️ **/24 scores are not comparable to /29** — do not rank across them.

### Prospect find
**Blibli itself** is on the TAL (line 655) but **has never been researched**, and the parent carries **Rp 83,316 bn total
TPV** — materially larger than the OTA segment alone. **Worth stubbing as its own account**, noting the HQ field needs
the same Indonesia correction.

## Section 12: Business Case Data

| Metric | Value | Source |
|---|---|---|
| **Group total TPV FY25** | **Rp 83,316 bn** (+8% y.o.y) | FY25 release, **fetched + extracted** |
| **3P Retail TPV FY25** (contains tiket.com) | **Rp 53,187 bn** (−2% y.o.y) | same |
| 3P Retail TPV 1H26 | Rp 26,272 bn (−4% y.o.y) | 1H26 release |
| Group net revenue FY25 | Rp 22,361 bn (+34%) | FY25 release |
| 3P Retail net revenue FY25 | Rp 1,551 bn (+12%) | same |
| **AOV FY25** | **Rp 1.72 mn** (+1%) | same |
| Transacting users FY25 | **5.1 mn** (+13%) | same |
| Group take rate FY25 | 8.5% (from 6.9%) | same |
| 3P Retail segment take rate | **5.35%** FY25 — **DERIVED** (2,847 / 53,187); this is GPBD/TPV, **not an OTA commission rate** | derived |
| **Monthly transaction count** | ✅ **DERIVED ~2.58 m orders/month for the segment containing tiket.com** | See the disclosure above. **Billing unit: paid orders.** |
| USD equivalents | ~**USD 5.2 bn** group TPV, ~**USD 3.3 bn** 3P Retail @ IDR 16,000 — **DERIVED, rate assumed not sourced** | — |
| Primary currency | **IDR**, plus 16 presentment currencies | ttgasia |
| Scale (Jun 2026) | 151 airlines / 240+ countries · 3.6 m+ accommodation · ~112,000 activities · 4,500+ events | 1H26 release |
| Billing channel split | **No public information found** — app vs web unknown | — |

⚠️ **Indonesian number formatting warning for anyone re-checking these:** Indonesian filings use `.` as the thousands
separator and `,` as the decimal, and the TPV tables are headed *"(Rp bn, unless stated otherwise)"*. Misreading either
is a 1,000× error.

## Overall Research Confidence

**MEDIUM-HIGH overall, but it splits sharply by section.**

- **HIGH — the payment stack and the financials.** Juspay, Midtrans, the Japan entity, Agoda and the FY25 filings were
  all fetched and control-tested, several by me personally. **The volume derivation rests on two inputs from the same
  audited-style release** — this is the best-evidenced volume figure in the repo.
- **MEDIUM — the method list.** Assembled from third-party press and vendor pages because the checkout is 403.
- **LOW — traffic.** Third-party estimate, web-only, app excluded, no supplied data. **This is the weakest input and it
  drives the market ranking.**
- **ABSENT — complaints.** The agent had not returned at write time.

**Traffic data was NOT supplied and NOT API-sourced — it is a third-party estimate**, which is why the country profile
and anything derived from it carry an explicit estimate tag.

## Manual Research Recommendations

> **Area: SimilarWeb pull.** **Why:** the country profile is the weakest input and drives the market ranking. **Action:**
> pull `tiket.com` with all-country-domains ON. ⚠️ "tiket" is the Indonesian word for "ticket" — expect noise.

> **Area: The checkout, from an Indonesian IP.** **Why:** it would settle whether OVO/DANA/ShopeePay appear as named
> tiles or are subsumed under QRIS — which decides whether Insight #1 can mention rails at all. **Action:** load the
> payment step on an Indonesian IP, then repeat in SGD or USD to see whether a foreign buyer gets cards only.

> **Area: Is Stripe still the cross-border rail?** **Why:** Insight #4 rests on a 2023 announcement. **Action:** ask on
> the call; do not assert it.

> **Area: Does Juspay now cover Indonesia?** **Why:** it is the hinge of the whole pitch. **Action:** ask directly — the
> absence is circumstantial, however strong.

> **Area: The audited annual report.** **Why:** the subsidiaries note gives the full entity list by jurisdiction, and
> may disclose merchant-of-record arrangements. **Action:** `asset-about.blibli.com` is **not** WAF-blocked even though
> `www.blibli.com` is — the annual report PDF is very likely there under an unguessed path.

> **Area: Complaints.** **Why:** an unassessed +2 row. **Action:** app-store reviews and mediakonsumen.com, searching
> Indonesian terms. ⚠️ *"dana tidak kembali"* means "funds not returned" — **not** the DANA wallet.

</details>
