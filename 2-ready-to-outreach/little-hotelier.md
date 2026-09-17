# Little Hotelier

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 20 / 29 → ⭐ **High Priority**
**Industry:** Hospitality SaaS (channel manager, booking engine, PMS) + embedded payments · **HQ:** Sydney, Australia — **SiteMinder Limited, ASX: SDR** · **Researched:** 2026-09-17 · **First email sent:** —
**Motion:** **Greenfield** — SiteMinder Pay is single-rail on Stripe Connect, with no orchestration layer.

---

> ## ⚠️ TWO THINGS BEFORE YOU READ ON
>
> **1. Little Hotelier is not an account — it is a SiteMinder product line.** SiteMinder reports **one operating segment** and publishes **no separate revenue, ARR, customer or property count** for Little Hotelier. FY26 Annual Report, Note 4, verbatim: *"The Group operates within one business segment… The CODM does not review or assess financial performance on a geographical basis **or by product categories**."* **This file is therefore a SiteMinder account file.** Note also that **SiteMinder is already TAL row 433** — row 124 (Little Hotelier) duplicates it, the same way row 660 (CodeCanyon) duplicates Envato. **Recommend merging row 124 into row 433.**
>
> **2. The Phase 0 PSP gate was tested and does NOT fire.** SiteMinder sells "SiteMinder Pay", which looks payment-company-shaped. It isn't: **SiteMinder Pay is Stripe Connect, white-labelled.** Evidence in Section 3. **In ICP — do not route to Partnerships.**

> ## 🎯 THE HOOK — they told the ASX they're building what you sell
>
> From SiteMinder's **FY26 investor presentation** (25 Aug 2026), on the FY27 product-roadmap slide, under **"Pay:"** — **I downloaded the 50-page PDF and extracted this myself**:
>
> > **"Pay: Region expansion · Multi-payment gateway · Auto Payment workflow enhancements"**
>
> **"Multi-payment gateway" is a public, dated, board-level commitment to move off single-processor Stripe** — declared to the ASX, alongside expanding Pay into new regions. That is a build-vs-buy decision they have already announced they are making, in the current financial year.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** SiteMinder is an ASX-listed hotel-commerce platform — channel manager, booking engine, and the **Little Hotelier** PMS for small properties — serving **56,000 properties** with **more than A$85 billion of gross booking value** flowing through its systems annually. It monetises through SaaS subscriptions plus a fast-growing **transaction** line that includes **SiteMinder Pay / Little Hotelier Pay**, its embedded guest-payment product.

**SimilarWeb total visits:** **Not obtained.** No supplied data, no MCP tools, and a WebSearch fallback was not accepted. **Geography instead comes from SiteMinder's audited segment note**, which is a better source here.

### Top 5 markets *(by FY26 audited revenue, not traffic)*
| Rank | Region / Country | Revenue | Accepted methods (Little Hotelier Pay) | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | **EMEA** — UK, Spain, Germany | **A$114.3m · 43.0%** | Visa, MC, Amex, JCB, UnionPay, Discover, Diners, OTA virtual cards, Apple Pay, Google Pay, **iDEAL/Wero** | — | ✅ UK, Ireland, Germany, Spain, Estonia |
| 2 | **APAC** — **Australia, Thailand, New Zealand** | **A$83.3m · 31.3%** (+21.8% cc) | Same card set; **no local rails** | **PromptPay (Thailand — a named major market) · PayTo, BPAY (Australia — home market) — SOURCED ABSENT** | ✅ AU, NZ, Thailand, India, Philippines |
| 3 | **AMER** — US, Canada | **A$68.5m · 25.8%** | Same | — | ✅ US, Mexico |
| — | **Little Hotelier Pay live in 32 countries** | — | In-territory APAC: **Australia, NZ, Singapore, Hong Kong, Malaysia, Thailand** | **Absent: India, Indonesia, Philippines, Vietnam, Japan, South Korea, Taiwan, China** — despite entities/offices in India, Philippines and Thailand | — |

### Legal entities
- **SiteMinder Limited** — Sydney (Level 7, Suite 7.01, 155 Clarence St). **ASX: SDR**
- **12 subsidiaries** (FY26 AR, Note 28): UK, US, Ireland, NZ, Thailand, India, Philippines, Germany, Estonia, Spain, Mexico, Australia. ⚠️ **None is a payments or regulated financial entity**
- APAC offices: **Bangalore, Bangkok, Manila** (plus Sydney)

### Known PSPs
- **Stripe** — ✅ **the processor behind SiteMinder Pay and Little Hotelier Pay.** Stripe **Payments, Connect, Radar, Terminal and Data Pipeline**. Relationship since **2015**; Terminal added 2025
- **GoCardless + Zuora** — ✅ SiteMinder's **own SaaS billing** to hotels, bank debit, Europe-heavy: *"70% of our European customers have chosen GoCardless over credit card"* `[page undated — treat as c.2021–22]`
- **AsiaPay** (PayDollar / PesoPay / SiamPay) — ⚠️ third-party gateway option in the booking engine, announced **18 Nov 2020**. **Six years old, body text blocked — do not assume it is live**
- **BECS** — direct-debit rail used to recover negative balances from Australian hotels

### Orchestration status
**None detected — single-rail on Stripe Connect.** No trace of Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY or Yuno in the terms, the FY26 Annual Report, the FY26 investor presentation, or the Little Hotelier help centre.

### Buying signals
- 🚨 **"Multi-payment gateway" is a declared FY27 product priority for Pay** — see the hook above. **Verified by me from the FY26 investor presentation PDF**
- 🚀 **"Region expansion" for Pay** is the priority listed beside it. The recent **Thailand launch** shows what each new market costs on a single rail: hotel-licence collection for 8+ room properties, mandatory e-mail receipts, weekly auto-invoicing with **7% VAT and 3% withholding tax** handling
- 📈 **Transaction revenue grew 30.0% reported / 33.8% cc to A$110.9m**, and **Transaction ARR +26.5% to A$144.3m** — the fastest-growing part of the business, and Pay is named among its key contributors
- 🌏 **APAC is the fastest-growing region by properties** — 18.5k (+14.2%), roughly a third of the 56,000 total
- 💱 **">85% of customer billings denominated in currencies other than AUD"** — their own words, FY26 earnings release

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach SiteMinder` — **note the account should be worked as SiteMinder, not Little Hotelier.***

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 20 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+3** | ✅ **DERIVED — ~56,000/month, on SiteMinder's own SaaS billing to hotels.** 56,000 properties (FY26, audited) × monthly billing; ARPU is reported monthly (A$429/mo), confirming a monthly cycle. **Billing unit: SaaS subscription charges to hotels.** ⚠️ **This EXCLUDES guest payments through SiteMinder Pay, whose volume is not disclosed anywhere** — the true total is higher and plausibly far higher. Scored on what is established. |
| Orchestration status | **+4** | ✅ None detected — single-rail Stripe Connect, affirmatively evidenced in their own terms. |
| 3+ countries | **+3** | ✅ 12 subsidiaries across 12 countries; revenue split across three regions; Little Hotelier Pay live in **32 countries**. |
| Multiple PSPs | **+3** | ✅ Stripe (Pay), GoCardless + Zuora (own billing), AsiaPay (booking engine). ⚠️ **These serve three different money flows, not one estate** — stated because it is a judgement call. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Sourced against an enumerated first-party list.** Little Hotelier Pay's published method set is cards + Apple Pay + Google Pay + iDEAL/Wero. **PromptPay is absent in Thailand — a named major APAC country in the audited segment note — and PayTo/BPAY are absent in Australia, the home market.** |
| Recent expansion | **+2** | ✅ Little Hotelier Pay launched in **Thailand** with market-specific tax and licensing handling; "Region expansion" is a declared FY27 Pay priority. |
| Payment issues reported | **0** | ⬜ **Not researched this run** — the single agent's budget went to the qualification question and the ASX filings. A genuine gap, not a finding of absence. |
| Funding >$10M | **0** | ❌ ASX-listed; no round. |
| High traffic outside home | **+2** | ✅ Awarded on audited revenue, not traffic: EMEA 43.0%, APAC 31.3%, AMER 25.8%. Australia is a fraction of APAC's third. |
| Competitor using orchestration | **0** | ⬜ Not researched this run. |
| Payment job postings | **0** | ⬜ Not researched this run. |

**Tier:** **20 / 29 → ⭐ High Priority.** No analyst override applied.

> **Note on the three zero rows.** Complaints, competitor orchestration and payment hiring were **not researched**, because this run used one agent and its budget went to the qualification question and the filings. **Those are unworked, not negative** — the score is a floor, and closing them could only raise it.
>
> **The "Multi-payment gateway" roadmap item is RFP-grade in substance** — a public, dated commitment to procure or build exactly what Yuno sells. It is not a formal RFP, so the RFP override is not invoked; the account already reaches ⭐ on arithmetic.

---

### ✅ PHASE 0 QUALIFICATION — the PSP gate was tested and does not fire

SiteMinder Pay *looks* like a payments business. It is not one. **SiteMinder Pay is Stripe Connect, white-labelled.** From SiteMinder's own payments terms (last updated **30 June 2026**), verbatim:

- > *"**Account** means an account on any Stripe Services platform that is opened by SiteMinder **on behalf of the Customer**."* → the hotel holds its own Stripe connected account
- > *"**Agreement** means the agreement constituted between SiteMinder and the Customer comprising of the Registration Form, these Terms and Conditions **and the Stripe Services Agreement**."* → tripartite; the hotel contracts directly with Stripe
- > *"The Customer is solely responsible for, and **SiteMinder has no liability in respect of, Chargebacks**."* (cl. 5.4.1)
- > *"**Payment Services Provider** means any bank, payment network or other financial institution…"* → SiteMinder defines PSPs as third parties, **not itself**
- Named Stripe entities by region — and for APAC: *"for any other Customer – **Stripe Payments Australia Pty Ltd** A.C.N. 160 180 343"*

**No licence is disclosed** — no AFSL, e-money authorisation, PSP registration or money-transmitter licence in the FY26 Annual Report, the terms, or any public page. The only compliance claims are certifications: *"The Group is **ISO 27001:2022 and PCI DSS v4.0.1 certified**."* None of the 12 subsidiaries is a regulated financial entity.

> ⚠️ **One thing that could be misread, flagged deliberately.** The FY26 AR states *"The Group recognises revenue as principal, controlling the services and bearing primary fulfilment responsibility"* for transaction revenue. That is **not** a merchant-of-record claim — transaction revenue of **A$110.9m against A$85bn GBV is 0.13%**, plainly net commission, and the terms put the Stripe contract and chargeback liability on the hotel. Commercially SiteMinder behaves as a **Stripe Connect platform** (opens accounts, does KYC, owns the fee schedule, manages disputes on the hotel's behalf) — **payfac-adjacent, but not a licensed payment institution**, and it does not sell payments to anyone outside its own software base.

**Verdict: in ICP. Do not route to Partnerships.**

### Source Notes
- ✅ **FY26 investor presentation** (50pp) and **FY26 earnings release** downloaded from siteminder.com and **extracted locally with pypdf by me**. The "Multi-payment gateway" roadmap line and every financial figure come from those documents.
- ✅ **SiteMinder payments terms**, last updated 30 June 2026 — the basis for the Phase 0 verdict.
- ⚠️ **No traffic data.** Not supplied, no MCP tools, fallback not accepted. Geography comes from the audited segment note instead, which is stronger here.
- ⚠️ **`siteminder.com` and `littlehotelier.com` HTML return 403** (Cloudflare). **But the investor PDFs fetch fine** with `curl --compressed`. `/legal/*` and `/news/*` are blocked. Little Hotelier's help centre is **Intercom** (`helpcentre.littlehotelier.com`, plain HTML, scrapeable); SiteMinder's own help centre is Salesforce and login-gated.
- ❌ **The AsiaPay partnership is six years old (Nov 2020) and its page body is blocked.** Recorded, but **do not assume it is live**.
- ❌ **A$85bn GBV is DISTRIBUTION volume, not payment volume.** Most of it is OTA bookings where money never touches SiteMinder Pay. **Never conflate the two in outreach.**

### Success Case Alternatives
- **Chosen on payment pattern:** a platform embedding payments for a long tail of small merchants across many markets, on a single processor, now expanding regionally. Verify any case against a published source before use.

---

## Executive Summary

SiteMinder (ASX: SDR) is a Sydney-based hotel-commerce platform serving **56,000 properties** with **A$266.1m FY26 revenue**, of which the fastest-growing line — **transaction revenue, A$110.9m, +30%** — includes its embedded payments product, **SiteMinder Pay / Little Hotelier Pay**. That product is **Stripe Connect, white-labelled**: hotels hold their own Stripe connected accounts, SiteMinder holds no payment licence, and **chargeback liability sits with the hotel**. It is therefore in ICP, not a Partnerships route. The motion is **Greenfield** — single-rail, no orchestration layer — and the trigger is unusually explicit: SiteMinder's FY26 investor presentation names **"Multi-payment gateway"** and **"Region expansion"** as FY27 priorities for Pay.

### Section 1: Website Traffic Analysis by Country

**Data source: NONE OBTAINED.** No supplied SimilarWeb data, no MCP tools, and a WebSearch fallback was not accepted.

**Consequence:** there is no traffic table. **Geography is taken from SiteMinder's audited segment note instead, which is a materially better source for a B2B SaaS company** — hotel customers are not web visitors.

**FY26 revenue by geography** (FY26 AR, Note 5):

| Region | Revenue | Share | Growth (cc) | Major countries |
|---|---|---|---|---|
| **EMEA** | A$114.3m | **43.0%** | +24.5% | UK, Spain, Germany |
| **APAC** | A$83.3m | **31.3%** | +21.8% | **Australia, Thailand, New Zealand** |
| **AMER** | A$68.5m | **25.8%** | +17.8% | US, Canada |

**Properties by region** (FY26 presentation appendix): AMER 11.0k (+11.1%), **APAC 18.5k (+14.2% — fastest growth)**, EMEA ~26.5k (derived). **APAC is ~33% of properties.**

### Section 2: Legal Entities & Local Presence

**Headquarters:** Sydney, Australia. SiteMinder Limited, **ASX: SDR**.

| Country | Entity | Source |
|---|---|---|
| Australia | **SiteMinder Limited** (ASX: SDR) · SiteMinder International Pty Ltd | FY26 AR Note 28 |
| India | SiteMinder (India) Pvt Ltd | Same |
| Philippines | SiteMinder Philippines Inc. | Same |
| Thailand | Online Ventures (Thailand) Ltd | Same |
| New Zealand | Online Ventures Ltd | Same |
| UK, Ireland, Germany, Spain, Estonia, US, Mexico | 7 further subsidiaries | Same |

**Cross-Border Gap Analysis:**

| Market | Top region? | Local entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---|---|---|---|---|
| Australia | ✅ APAC major | ✅ yes | — | Low |
| Thailand | ✅ APAC major | ✅ yes | Not verified | **Medium** — Pay is live but PromptPay is not |
| New Zealand | ✅ APAC major | ✅ yes | — | Low |
| **India** | office + entity | ✅ **entity exists** | Not verified | ⚠️ **Pay is NOT live here despite the entity** |
| **Philippines** | office + entity | ✅ **entity exists** | Not verified | ⚠️ **Pay is NOT live here despite the entity** |

> **The notable structural fact:** SiteMinder has **operating entities and offices in India and the Philippines** and sells software in both — but **Little Hotelier Pay is not available in either**. Payments coverage lags the software footprint. ⚠️ *Why* is not established; do not assert a reason.

> ⚠️ **No regulatory acquiring gate is asserted.** None was verified this run.

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers — three separate money flows, kept separate

| Flow | Provider | Evidence Type | Source |
|---|---|---|---|
| **(c) SiteMinder Pay / Little Hotelier Pay** — guest payments | **Stripe** — Payments, **Connect**, Radar, Terminal, Data Pipeline | `[Terms/Privacy Policy]` + `[Provider Case Study]` | siteminder.com/legal/payments-terms (30 Jun 2026); stripe.com/customers/siteminder |
| **(a) SiteMinder's own SaaS billing** to hotels | **GoCardless + Zuora**, bank debit | `[Provider Case Study]` | gocardless.com/stories/siteminder `[undated]` |
| **(b) Guest payments via hotels' own gateways** | **AsiaPay** (PayDollar/PesoPay/SiamPay) and other third-party gateways | `[Press Release]` | siteminder.com/news/siteminder-asiapay-partnership (18 Nov 2020) ⚠️ **six years old** |
| Recovery rail | **BECS** direct debit (AU) | `[Terms]` | payments-terms cl. 6.6 |

**Checked and NOT found anywhere:** Adyen, Checkout.com, Braintree, Worldpay, Airwallex, eWAY, Windcave, Tyro, Pin Payments, Fat Zebra, 2C2P. SiteMinder's public integrations directory has **no payment-gateway category at all**.

#### 3B. Payment Orchestrator

**None detected — single-rail on Stripe Connect.**

> *"No public evidence found of a payment orchestration platform. SiteMinder Pay integrates directly with a single processor, which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

> 💡 **And they have said they intend to change that.** FY26 investor presentation, FY27 priorities for Pay: **"Region expansion · Multi-payment gateway · Auto Payment workflow enhancements."**

> **MANUAL:** the SiteMinder help-centre article listing integrated third-party gateways is **login-gated**. A customer login would resolve the full gateway roster.

### Section 4: Alternative & Local Payment Methods

**Enumerated first-party list** (Little Hotelier Pay FAQ, helpcentre.littlehotelier.com):

| Method | Category | Status | Source |
|---|---|---|---|
| Visa, Mastercard | Cards | **Active** | LH Pay FAQ ✅ |
| **American Express** | Cards | **Active — but explicitly NOT available in Malaysia** | Same |
| JCB, UnionPay, Discover, Diners | Cards | **Active** | Same |
| **OTA virtual cards** | Cards | **Active** — material for this vertical | Same |
| Apple Pay, Google Pay | Wallet | **Active** | Same |
| **iDEAL / Wero** | A2A | **Active** — the *only* local rail in the set, and it is European | Same |
| **PromptPay** (Thailand) | A2A | ❌ **SOURCED ABSENT** — and Thailand is a named major APAC market | Same |
| **PayTo, BPAY** (Australia) | A2A | ❌ **SOURCED ABSENT** — in the home market | Same |
| **PayNow** (Singapore), **FPS** (Hong Kong), **DuitNow/FPX** (Malaysia) | A2A | ❌ **SOURCED ABSENT** — Pay is live in all three | Same |
| UPI, QRIS, GCash, konbini, Alipay | All | ❌ Not applicable — **Pay is not live in those markets at all** | Same |

> **Warning: Little Hotelier Pay is live in six in-territory APAC markets — Australia, New Zealand, Singapore, Hong Kong, Malaysia, Thailand — and carries no local payment rail in any of them.** The only A2A method in the entire set is **iDEAL/Wero**, which is European. Cards and wallets everywhere else.

**Payments are accepted in the property's local currency only.**

**What the Thailand launch reveals about the cost of the single rail:** hotel-licence collection for 8+ room properties, mandatory e-mail receipts, weekly auto-invoicing with **7% VAT** and **3% withholding tax** handling. Every new market is bespoke work on one processor — which is precisely why "Region expansion" and "Multi-payment gateway" appear on the same roadmap line.

### Section 5: Payment Issues & Customer Complaints

**Not researched this run.** This run used a single agent whose budget went to the Phase 0 qualification question and the ASX filings. **This is an unworked section, not a finding of no complaints** — do not read it either way.

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | **2026-08-25** | **FY26 results. "Multi-payment gateway" and "Region expansion" named as FY27 priorities for Pay** | **Payment platform signal** | FY26 investor presentation ✅ **verified by me** |
| 2 | **2026-08-25** | Transaction revenue **+30.0% to A$110.9m**; Transaction ARR **+26.5% to A$144.3m**; adjusted EBITDA **+96.5% to A$28.1m** | Financial | FY26 earnings release ✅ |
| 3 | **FY26** | Little Hotelier Pay **launched in Thailand** with VAT/WHT/licence handling | Market expansion | helpcentre.littlehotelier.com ✅ |
| 4 | **2025** | **Stripe Terminal** added to the SiteMinder stack (card-present) | Payment infrastructure | stripe.com/customers/siteminder ✅ |
| 5 | **2020-11-18** | AsiaPay partnership for Asian booking-engine gateways | Partnership ⚠️ **stale** | siteminder.com/news ⚠️ |

**Public payment RFP:** *No public payment-related RFP found* — though the FY27 "Multi-payment gateway" roadmap item is RFP-grade in substance.
**Payment hiring:** **Not researched this run.**

### Section 7: Payment-Specific News

Beyond the roadmap item and the Stripe relationship, **no payments trade-press coverage was found**. SiteMinder has announced no orchestration or gateway partnership.

### Section 8: Checkout Experience Audit

**Partially accessible.** `siteminder.com` and `littlehotelier.com` HTML return 403; the guest checkout sits inside each hotel's booking engine. Findings from the help centre and terms:

| Dimension | Finding |
|---|---|
| Checkout type | Booking engine, embedded; Stripe-hosted card capture |
| Card input | **Stripe-tokenised** — SiteMinder is PCI DSS v4.0.1 certified |
| Methods visible | Cards + Apple/Google Pay + iDEAL/Wero + OTA virtual cards |
| **Location-based display** | ⚠️ **Effectively none** — the same card-led set in every market |
| **Multi-currency** | **Property's local currency only** |
| 3DS | **Not observable** — Stripe would normally supply it |
| Card-present | **Stripe Terminal**, added 2025 |

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|---|---|---|
| **PCI DSS** | ✅ **"The Group is ISO 27001:2022 and PCI DSS v4.0.1 certified"** | FY26 Annual Report |
| Card data handling | Stripe-tokenised via Connect | payments terms |
| Payment licence | **None disclosed.** Operates under Stripe's licences | FY26 AR, terms |

> Unusually, this account **states its PCI position in an audited annual report** — most files in this repo have nothing. Note it is a **certification, not a licence**.

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: They announced the project to the ASX**
> **Evidence:** Section 6 (FY27 Pay priorities: *"Region expansion · **Multi-payment gateway** · Auto Payment workflow enhancements"*) **+** Section 3B (currently single-rail on Stripe Connect).
> **Pain Point:** they have publicly committed to multi-gateway and regional expansion for Pay, and today have one processor and no routing layer. That is a build they now have to staff, or buy.
> **Yuno Value Proposition:** multi-gateway *is* the product — routing, failover and per-market acquirer coverage through one integration, instead of an in-house router built alongside Stripe Connect.
> **Outreach Angle:** cite their own roadmap slide. Nobody has handed them a build-vs-buy comparison for a project they have already announced.
> **Suggested Subject Line:** Your FY27 "multi-payment gateway" line
> ⚠️ **Constraint:** respect the Stripe relationship — it dates to 2015 and Connect is load-bearing for their whole payout model. Position as *alongside*, never as a rip-out.

> **Insight #2: Payments coverage lags the software footprint**
> **Evidence:** Section 2 (entities and offices in **India, Philippines, Thailand**) **+** Section 4 (Little Hotelier Pay live in 32 countries — **India and the Philippines are not among them**).
> **Pain Point:** they sell software into markets where they cannot yet monetise payments, and transaction revenue is their fastest-growing line at +30%.
> **Yuno Value Proposition:** per-market acquirer coverage without a per-market build.
> **Suggested Subject Line:** Pay is live in 32 countries. Your entities cover more.

> **Insight #3: Six APAC markets live, zero local rails**
> **Evidence:** Section 4 (Pay live in Australia, NZ, Singapore, Hong Kong, Malaysia, Thailand; the only A2A method in the set is **iDEAL/Wero**, which is European) **+** Section 1 (APAC = **31.3% of revenue** and the fastest property growth).
> **Pain Point:** PromptPay in Thailand and PayTo/BPAY in Australia are absent from an enumerated first-party list, in markets the company names as major.
> **Suggested Subject Line:** iDEAL in the Netherlands, cards in Bangkok

> **Insight #4: Every new market is bespoke on one rail**
> **Evidence:** Section 4 (the Thailand launch required licence collection, e-mail receipts, weekly auto-invoicing, 7% VAT, 3% withholding tax) **+** Section 6 (*"Region expansion"* is an FY27 priority).
> **Pain Point:** the marginal cost of each new Pay market is a bespoke integration project, and they have declared they intend to add more.
> **Suggested Subject Line:** What Thailand cost you

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks:**
1. "Your FY26 deck lists 'Multi-payment gateway' as an FY27 priority for Pay. That's the whole of what we do."
2. "Little Hotelier Pay is live in Singapore, Hong Kong, Malaysia and Thailand — and the only A2A method in the set is iDEAL."
3. "You have entities in India and the Philippines. Pay isn't live in either."

**Cold call openers:**
1. "The multi-gateway line in the FY26 deck — is that being built in-house, or is it still open?"
2. "What did adding Thailand to Pay actually cost you in engineering time?"
3. "Transaction revenue is up 30%. How much of that is Pay versus Demand Plus?"

### Section 11: Similar Companies & Prospecting Pipeline

**Not researched this run** — the single agent's budget went to qualification and filings. **Unworked, not empty.**

#### 11C. Companies Recently Adopting Payment Orchestration
**Not established.** No competitor orchestration adoption was searched for. Do not claim competitive urgency on this account.

### Section 12: Business Case Data

| Metric | Value (FY26, 12 months to 30 Jun 2026) | Source |
|---|---|---|
| **Total revenue** | **A$266.1m** (+18.6% reported, **+22.0% cc/organic**) | FY26 ER ✅ audited |
| — Subscription revenue | A$155.2m (+11.6% rep) | ✅ |
| — **Transaction revenue** | **A$110.9m (+30.0% rep, +33.8% cc)** | ✅ |
| **ARR** | **A$313.7m** (+24.1% cc) | ✅ |
| — **Transaction ARR** | **A$144.3m** (+26.5% rep) | ✅ |
| **Properties** | **56,000** (+5,900 net, +11.8%) | ✅ |
| Transaction products adopted | 45.4k (+29.7%) | ✅ |
| Monthly ARPU | **A$429** (+5.9% rep); **Transaction ARPU +19.3%** | ✅ |
| Adjusted EBITDA | **A$28.1m (+96.5%)**, 10.6% margin | ✅ |
| Reported net loss | (A$11.3m), halved from (A$24.5m) | ✅ |
| LTV / CAC | **6.6x** (from 6.2x); LTV A$29,857 | ✅ |
| **GBV through the platform** | **>A$85 billion** / 12 months | ✅ ⚠️ **distribution volume, NOT payment volume** |
| **Monthly transaction count** | ✅ **DERIVED ~56,000/month** — 56,000 properties billed monthly (ARPU reported monthly). **Billing unit: SaaS charges to hotels.** ⚠️ **Excludes SiteMinder Pay guest payments, which are not disclosed** | ✅ + arithmetic |
| **SiteMinder Pay revenue / volume / take rate** | ❌ **NOT DISCLOSED** in the FY26 AR, earnings release or presentation | — |
| Currency exposure | **">85% of customer billings denominated in currencies other than AUD"** | ✅ |
| Little Hotelier standalone | ❌ **Not disclosed — one operating segment** | ✅ |

> **The business case has an unusually good anchor and one hard limit.** The anchor: transaction revenue is A$110.9m growing 30%, and Pay is named among its drivers. The limit: **SiteMinder Pay is never broken out** — no revenue, no volume, no take rate, no attach rate. And **A$85bn GBV is distribution volume**; most of it is OTA bookings that never touch Pay. Conflating the two would be an obvious and costly error in a first call.

### Overall Research Confidence

**High on qualification, financials and the payment stack. None on traffic. Unworked on complaints, competitors and hiring.**

**High confidence** (primary source, fetched and extracted by me):
- FY26 investor presentation (50pp) and FY26 earnings release, downloaded and parsed with pypdf — including the "Multi-payment gateway" roadmap line and every financial figure
- SiteMinder payments terms (30 Jun 2026) — the Stripe Connect structure and the Phase 0 verdict
- FY26 Annual Report — segment note, subsidiary list, PCI/ISO certification

**Medium:** the Little Hotelier Pay method and country lists (Intercom help centre, agent-fetched, not re-verified by me); the GoCardless relationship (undated page).

**Low / none:** **traffic — not obtained**; SiteMinder Pay volume and take rate — not disclosed; the third-party gateway roster — login-gated; **complaints, competitors and payment hiring — not researched**.

**Traffic data was NOT obtained.** Geography comes from the audited segment note, which for a B2B SaaS company is the better source.

### Manual Research Recommendations

> **Area:** The three unworked sections — complaints, competitor orchestration, payment hiring
> **Why it matters:** the 20/29 is a floor. A payments-engineering job posting alone would confirm whether "Multi-payment gateway" is being built in-house right now, which decides whether this is a buy conversation or a competitive one.
> **Action:** re-run with the full five-agent fan-out, or search SiteMinder's careers page for payments roles directly.

> **Area:** SiteMinder Pay attach rate and volume
> **Why it matters:** it is the whole business case and it is disclosed nowhere. 45.4k transaction products are adopted across 56k properties, but that spans six products.
> **Action:** discovery question. Do not estimate it — and never use the A$85bn GBV figure as a proxy.

> **Area:** The login-gated integrated-gateway list
> **Why it matters:** it would reveal whether third-party gateways beyond AsiaPay are already wired into the booking engine — i.e. whether a de facto multi-gateway estate already exists.
> **Action:** a customer login, or ask on a call.

> **Area:** TAL hygiene
> **Why it matters:** **row 124 (Little Hotelier) duplicates row 433 (SiteMinder).** Little Hotelier is a product line with no separate disclosure.
> **Action:** merge row 124 into row 433 and work the account as SiteMinder.

### Appendix: All Source URLs

**Primary (fetched and extracted by me):**
- https://www.siteminder.com/wp-content/uploads/2026/08/Presentation-SiteMinder-FY26.pdf — **the "Multi-payment gateway" roadmap line**
- https://www.siteminder.com/wp-content/uploads/2026/08/Earnings-Release-SiteMinder-FY26.pdf — FY26 financials
- https://www.siteminder.com/wp-content/uploads/2026/08/Annual-Report-SiteMinder-FY26.pdf — segment note, subsidiaries, PCI/ISO

**Secondary:**
- https://www.siteminder.com/legal/payments-terms/ — Stripe Connect structure (30 Jun 2026)
- https://stripe.com/customers/siteminder — Stripe product set, 2015 relationship
- https://helpcentre.littlehotelier.com/en/articles/9187990-little-hotelier-pay-get-started
- https://helpcentre.littlehotelier.com/en/articles/14082826-little-hotelier-pay-in-thailand-get-started
- https://gocardless.com/stories/siteminder/ `[undated]`
- https://www.siteminder.com/news/siteminder-asiapay-partnership/ (2020) ⚠️ stale

</details>
