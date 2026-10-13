# PropertyGuru

**Status:** 🔴 Not ICP — under 40k monthly transactions (derived ~4,600/mo; volume gate fired)
**ICP Score:** 12 / 29 → 🟢 Medium (10–16) — **OVERRIDDEN DOWN to 🔴 Low / recommend not-ICP. See the override block.**
**Industry:** Property Classifieds Marketplace (PropTech) · **HQ:** Singapore · **Researched:** 2026-10-13 · **First email sent:** —
**Motion:** Greenfield (no orchestration layer detected) — **but the volume gate fails. Do not work this account as a standard greenfield.**

> ## 🛑 READ THIS FIRST — THE BILLING-UNIT GATE DECIDED THIS ACCOUNT
>
> PropertyGuru's billing unit is **one upfront payment per agent per year**, not a consumer checkout.
> From the FY2023 Form 20-F, verbatim:
>
> > *"Our revenue model is predominantly subscription-based, where agents currently pay **upfront fees for an annual subscription** that provides them with a number of credits they can use to promote their listings. In all our Priority Markets other than Vietnam, agents can currently select one of our **annual subscription packages**…"*
>
> With **"over 55,000 agents in our Priority Markets"**, the dominant billing line produces
> **~4,600 payment events per month group-wide** — roughly **11% of the 40,000/month floor**.
>
> **There is no consumer payment flow.** Consumers browse free. PropertyGuru Finance is
> brokerage/referral — the *banks and insurers are invoiced*, not the home buyer. The one
> consumer-facing business (Sendhelper) has had its domain **301'd onto the main portal**.
>
> **Recommendation: analyst override downward — route to `not-icp/` unless Prateek wants to keep
> it as a long-horizon enterprise-invoicing watch item.** This is a real, well-evidenced "no",
> not a research failure. No pitch has been manufactured.

---

---

> ## 🔍 ANALYST AUDIT — Prateek, 2026-10-13
>
> **The rejection stands, and the basis is cleaner than an override: the volume gate fired on a DERIVED figure.** 55,000+ agents ÷ 12 months = **~4,600 billing events/month**, both inputs sourced to the same audited FY2023 Form 20-F. The method's auto-reject fires on a *sourced or soundly-derived* figure under 40,000 — this qualifies, so this is a gate failure, not a judgement call. **~11% of the floor.**
>
> ### ⛔ THIS RUN CORRECTED TWO ERRORS IN MY OWN BRIEFING. Both were mine; both are fixed.
> 1. **I told the agent PropertyGuru was NOT on the TAL. It is — line 805, as "PropertyGuru International" (`propertygurugroup.com`).** My pre-flight matched company names exactly, so the longer name never matched "propertyguru". **This is a methodological flaw in my pre-flight, not a one-off:** any TAL row whose name carries a suffix ("International", "Group", "Holdings", "Ltd") will be missed by an exact-match check. **Use substring matching from now on.** So this is an existing never-contacted row, not a new find — and **Adyen + Braintree is net-new TAL intelligence against two empty cells.**
> 2. **I asserted in the traffic notes that Rumah123 was a group brand. It is not.** I verified independently: `rumah123.com` is a live 470,356-byte site with **zero** `propertyguru` references against a working control of 784 `rumah` hits. PropertyGuru's Indonesian portal was **Rumah.com**, which ceased operating **30 Nov 2023**; `rumah.com` is now a ~5,756-byte parked page. **So Indonesia ↓43.58% is a decommissioned business, not a declining market.** The traffic file has been corrected.
>
> ### ✅ Verified first-hand
> - **PropertyGuru's TAL row at line 805**, with empty `Payment Gateway` and `Payment Orchestrator` cells — confirming Adyen+Braintree is new intelligence.
> - **Rumah123's independence and Rumah.com's parked state** (above).
> - **I could NOT resolve the Vietnam question either.** `batdongsan.com.vn` and `ddproperty.com` both return **403 Cloudflare challenge pages at ~5.6 KB**. ⚠️ Note the discipline point: that challenge page contains `0` `propertyguru` references, and **that zero is non-informative** — it is a block page, not the site. No conclusion may be drawn from it in either direction.
>
> ### ⚠️ THE ONE THING THAT WOULD OVERTURN THIS REJECTION
> **Vietnam (Batdongsan) is explicitly "pay-as-you-go" with ~1.5m listings/quarter.** If listings are paid for individually rather than debited from a prepaid balance, that alone is **~500,000 payment events/month** — two orders of magnitude above the derived figure, and the gate would not fire. **Neither the run nor I could source the top-up frequency.** The run handled this correctly: it rejected on the **subscription line**, which the 20-F itself calls the *predominant* revenue model, and put "confirm Vietnam top-up frequency" at the top of Manual Research rather than rejecting on an assumption. **That caveat must travel with this verdict** — if Prateek ever wants this account reopened, that is the single question to answer, and it may belong to Batdongsan as a separate account rather than to PropertyGuru.
>
> ### 📋 Rows I examined but did not change
> The run flagged the double-count itself and I agree: **5 of the 12 points (3+ countries +3, high traffic outside home +2) fire off the single SG/MY split**, and "high traffic outside home" is **substantively false here** — it fires only because Malaysia is large, while this is a two-market domestic operator with local acquiring in both. Net of the double-count the honest score is **~9/29**. I left the arithmetic as computed and recorded the distortion rather than hand-editing rows, since the gate decides the outcome regardless.
>
> ### ✔️ Safety checks passed
> No credential value (the published Malaysian bank account number is correctly held as `[account number published on the page — value deliberately not recorded]`). No booking link. Structure 3/3. ICP re-added independently: **0+4+3+3+0+0+0+0+2+0+0 = 12 across 11 rows.** ✅

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** PropertyGuru Group is Southeast Asia's largest property classifieds operator, running PropertyGuru (Singapore, Malaysia), iProperty (Malaysia), DDproperty and thinkofliving (Thailand) and Batdongsan (Vietnam). Consumers search for free; revenue comes almost entirely from **real-estate agents and property developers buying annual subscription packages, listing credits and advertising depth products**. It was taken private by EQT in December 2024 at a ~US$1.1bn equity value and is no longer an SEC filer.

**SimilarWeb total visits (last full month):** Not supplied as an absolute figure — the supplied dataset gives **country shares only** (Jul–Sep 2026, `propertyguru.com.sg` + 4 further domains, 83 countries). Source: SimilarWeb (supplied 2026-10-13), `accounts/traffic/propertyguru.md`. **No absolute visit count is available, so no visit-derived volume figure is computed anywhere in this report.**

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | **Singapore** | **47.03%** ↑5.68% | Not verified — `.sg` agent help-centre unreachable (403 incl. control path). Group-level stack is cards + online bank transfer + cheque | **PayNow — NOT FOUND, but absence is NOT sourced** (see §4 caveat) | ✅ PropertyGuru Pte. Ltd.; Sendtech Pte. Ltd. |
| 2 | **Malaysia** | **41.84%** ↑6.10% | ✅ Online bank transfer via **Adyen**; cards via **Braintree**; **Atome** BNPL (3/6/9/12 mo); CIMB & Public Bank card instalments; cheque | **DuitNow — Not found.** Touch 'n Go — terms page exists, mechanics unconfirmed | ✅ PropertyGuru International (M) Sdn Bhd; iProperty.com Malaysia Sdn. Bhd. |
| 3 | United States | 1.57% ↑10.48% | N/A — no sales operation | N/A — diaspora/expat browsing, not a market | ❌ None — and none needed |
| 4 | Australia | 1.14% ↓4.37% | N/A — no sales operation | N/A — awards events only | ❌ None |
| 5 | India | 1.05% ↑8.92% | N/A — no sales operation | N/A — Bengaluru tech office only | ⚠️ Tech/GRC staff present, no revenue entity confirmed |

> ⚠️ **Ranks 3–5 are rounding errors, not markets.** Singapore + Malaysia = **88.87%** of traffic. Third place is 1.57%. No rail work outside SG/MY is justified, and none was done.

### Legal entities
Confirmed from the FY2023 20-F and the Malaysia agent help centre:
- **PropertyGuru Group Limited** — Cayman Islands exempted company (ultimate parent)
- **PropertyGuru Pte. Ltd.** (Singapore) — group site footer carries unlabelled number `200615063H` ⚠️ *the page does not say what this number is; treat as probable Singapore UEN, unverified*
- **PropertyGuru International (M) Sdn Bhd** / "PropertyGuru International (Malaysia) Sdn Bhd" (Malaysia) — Suite 35.01, Level 35, The Gardens South Tower, Mid Valley City, Kuala Lumpur
- **iProperty.com Malaysia Sdn. Bhd.**, **Brickz Research Sdn. Bhd.**, **IPGA Management Services Sdn. Bhd.** (Malaysia)
- **PropertyGuru International (Thailand) Co., Ltd.**, **DDProperty Media Ltd.**, **iProperty (Thailand) Co., Ltd.**, **Prakard IPP Co., Ltd.**, **Kid Ruang Yu Co., Ltd** (Thailand)
- **PropertyGuru Viet Nam Joint Stock Company** (Vietnam)
- **Sendtech Pte. Ltd.** (Singapore) — the Sendhelper entity
- **Epsilon Asia Holdings II Pte. Ltd.** (Singapore)

### Known PSPs
- **Adyen** — `[Regulatory Filing]` FY2023 20-F names it directly: *"Adyen Payment Gateway for payment collection"*; and `[Terms/Help Centre]` as the processor for **online bank transfer** on the agent payment page (Malaysia, page updated 2026-08-19)
- **Braintree** — `[Terms/Help Centre]` *"directly with your credit or debit card (powered by Braintree payment gateway)"* (Malaysia, page updated 2026-08-19)
- **Atome** — `[Terms/Help Centre]` BNPL, *"currently enabled for PropertyGuru Malaysia payments only… not yet available for iProperty (Malaysia)"*
- **CIMB Bank / Public Bank** — `[Terms/Help Centre]` interest-free credit-card instalment plans; CIMB Bank is also the cheque-collection bank for the Malaysian entity

### Orchestration status
**None detected — direct PSP integrations only (greenfield).** Two gateways are wired side by side and **split by payment method, not by geography**: Adyen takes bank transfers, Braintree takes cards, on the same checkout page. No evidence of any third-party orchestration or routing layer, and no in-house routing layer referenced in the 20-F, the help centre or any job posting. The 20-F's own third-party vendor list names Adyen alongside NetSuite, Salesforce, Cloudsense, Google and Meta — a procurement-style, one-vendor-per-function stack.

### Buying signals
- 🏦 **Ownership change — EQT take-private completed 13 Dec 2024**, US$6.70/share, ~US$1.1bn equity value, BPEA Private Equity Fund VIII; delisted from NYSE. *New owner, new mandate.* ([EQT](https://eqtgroup.com/news/eqt-completes-acquisition-of-propertyguru))
- 💼 **Full board and CEO reset, 13 Jan 2025** — **Lewis Ng** CEO from March 2025; **Trevor Mather** (ex-Auto Trader CEO) chairman; **Ed Williams** (Rightmove founder) director. *EQT installed UK property-portal operators who monetise agents the same way.* ([PropertyGuru](https://www.propertygurugroup.com/newsroom/propertyguru-announces-leadership-transition-and-a-new-board/))
- 💳 **Packaging and pricing overhaul effective 1 Nov 2025** — new "Core+" dual-platform package, **Prime Credits discontinued** with balances expiring 30 May 2026, listing duration standardised to 60 days. *A live billing/packaging change window.* ([PropertyGuru MY](https://www.agentofferings.propertyguru.com.my/?p=11096))
- 🧩 **Payment-stack fragmentation inside one market, stated by the company** — Atome works on PropertyGuru Malaysia but *"not yet available for iProperty (Malaysia)"*, while the same agent can buy a dual-platform package covering both. ([Atome FAQ](https://www.agentofferings.propertyguru.com.my/help-centre/pay-with-atome-my/))
- ❌ **No funding round, no payment-related hire, no RFP, no market expansion** found in the last 12 months. Indonesia was *closed*, not expanded.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not generated — and should not be, on current evidence.*

The volume gate fails on a derived figure roughly an order of magnitude below the floor, and there is no consumer payment flow for orchestration to touch. Running `/full-outreach` here would mean writing a routing-and-approval-rate pitch at a merchant whose entire addressable flow is ~55,000 annual B2B invoices. **Resolve the two open questions in Manual Research Recommendations before any sequence is written.**

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 12 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **0 — REJECT band** | ✅ **DERIVED: ~4,600/month** (group-wide subscription billing events). **Billing unit = one upfront annual subscription payment per agent.** 55,000+ agents ÷ 12 = 4,583. Both inputs sourced to the FY2023 20-F. **<40,000 ⇒ auto-reject band.** See the full disclosure below. |
| Orchestration status | **+4** | ✅ "None detected — direct PSP integrations only." Adyen + Braintree wired directly, split by method. Greenfield by the letter of the rule. |
| 3+ countries | **+3** | ✅ Two independent routes both satisfied: 5 countries >1% traffic share (SG, MY, US, AU, IN), **and** 13+ legal entities confirmed across SG, MY, TH, VN. ⚠️ *But see double-count note.* |
| Multiple PSPs | **+3** | ✅ Adyen **and** Braintree, both named verbatim on a fetched agent payment page updated 2026-08-19, plus Adyen independently named in the 20-F. Strongest-evidenced row in the matrix. |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **UNCERTAIN — deliberately not awarded.** PayNow was not found anywhere, but the Singapore agent help centre returns 403 *including on a nonsense-path control*, so I cannot distinguish "absent" from "unreachable". The rule requires **a source for the absence**. Malaysia's dominant rail is arguably *present*: "online bank transfer → select your preferred bank → redirected to online banking" is the FPX flow, served by Adyen. **Not awarded.** |
| Recent expansion | **0** | ❌ Not met. No new market in 12 months. The most recent market move was a **closure** (Rumah.com Indonesia, ceased 30 Nov 2023). |
| Payment issues | **0** | ❌ No payment complaints found on Reddit, Trustpilot, X or app stores. Agent billing runs through named sales reps, which keeps friction off public channels. |
| Funding >$10M | **0** | ❌ Not met *in window*. The EQT take-private (Dec 2024) is ~22 months before report date, outside the 12-month test. No 2025/2026 financing found. |
| High traffic outside home | **+2** | ✅ Singapore 47.03% < 60%, so the row fires mechanically. ⚠️ **Flagged as a false positive in substance** — see double-count note. |
| Competitor using orchestration | **0** | ❌ No public case study found of any SEA property portal adopting an orchestrator. |
| Payment job postings | **0** | ❌ None found. The only engineering leadership role found covers "marketplaces in Singapore, Malaysia, and Thailand" with no payments scope. |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → computed **🟢 Medium (12/29)**

**No public payment RFP was confirmed.** No RFP override applies.

---

### 🔴 ANALYST OVERRIDE — tier forced DOWN from 🟢 Medium to 🔴 Low / recommend `not-icp`

Three of the four documented override grounds apply simultaneously. The matrix arithmetic is not wrong; it is measuring the wrong thing on this account.

**1. Absolute volume too small — the primary ground.**
The derived figure is **~4,600 payment events/month** against a 40,000 floor. To clear the floor, PropertyGuru would need ~35,400 *additional* monthly payment events from a base of 55,000 agents — meaning roughly **64% of every agent in the group making a separate discretionary purchase every single month**, on top of an annual package that already bundles their credits. That is not plausible for a model the company itself describes as *"predominantly subscription-based… upfront fees for an annual subscription."* A 12/29 score on this volume is the textbook false positive the override exists to catch.

**2. The matrix is double-counting one underlying fact.**
**5 of the 12 points come from the single Singapore/Malaysia traffic split.** "3+ countries" (+3) and "High traffic outside home" (+2) both fire off the same two-market structure. Worse, "high traffic outside home" is *substantively false here*: it fires only because Malaysia happens to be nearly as large as Singapore, not because the business is internationally distributed. This is a **two-market domestic business with local entities and local acquiring in both markets** — the exact opposite of the cross-border profile the row is designed to detect. Discounting the double-count, the real score is nearer **9/29**.

**3. No consumer payment flow exists for orchestration to reach.**
Consumers never pay. The fintech line is **invoiced to banks and insurers**. The one consumer-facing business has been folded in and its domain redirected. There is no checkout, no recurring consumer card-on-file book, no involuntary churn problem, no app-store question. The classic orchestration value drivers — approval-rate lift, retry logic, local acquiring, network tokens — have **almost no surface area** against ~55,000 annual high-ticket B2B invoices that are substantially collected by **bank transfer and cheque**.

**What would reverse this override.** Only one thing, and it is specific: **sourced evidence that Vietnam (Batdongsan) wallet top-ups and/or discretionary Ad Credit purchases run at high frequency.** Vietnam is explicitly a *pay-as-you-go* model and carried ~1.5m listings per quarter in Q2 2024. If those listings are paid individually rather than debited from a prepaid balance, the count changes by two orders of magnitude. I could not source the top-up mechanics in two attempts (see §4 and Manual Research). **This is the single question that decides whether the override stands.**

---

### Monthly transaction count — mandatory disclosure

**Billing unit being counted: a payment event received by PropertyGuru from a paying agent, developer or advertiser.** Explicitly *not* counted: listing-credit debits against an already-paid balance (internal ledger movement, not a payment), and instalment sub-debits under Atome/CIMB/Public Bank plans (the lender collects those from the agent; PropertyGuru is paid once).

> ✅ **DERIVED: ~4,600 payment events/month, group-wide.**
> **Arithmetic:** 55,000 agents ÷ 12 months = **4,583/month.**
> **Input 1 (sourced):** *"Based on our last three months average as of December 31, 2023, we have over 55,000 agents in our Priority Markets."* — [FY2023 20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm)
> **Input 2 (sourced):** *"agents currently pay upfront fees for an annual subscription"* / *"agents with a valid 12-month subscription package"* — same filing.
> Both inputs sourced to the same audited annual report, so this is a derivation, not an estimate. The calculation is deliberately **generous**: it treats all 55,000 agents as annual subscribers even though Vietnam's cohort is pay-as-you-go, which *inflates* the annual-subscription count.

**Cross-check against Singapore alone:** 16,481 Singapore agents (31 Dec 2023) ÷ 12 = **~1,373/month** for the group's largest market, which is 57.3% of revenue. Consistent.

**Components NOT included, because their frequency is not sourced** — stated plainly so the reader is not misled about completeness:
- Discretionary **Ad Credit / depth-product** purchases. *Confirmed to exist* (*"Agents can purchase additional discretionary credits as they utilize those included in their subscription package, or they can purchase certain products directly on a cash basis"*), **frequency unknown**. `[ASSUMPTION — not researched]`
- **Vietnam wallet top-ups.** Model confirmed (*"agents who credit money into their account"*), **frequency unknown and not found in two search attempts.** `[ASSUMPTION — not researched]`
- **Developer, events and data invoices.** Confirmed invoiced; enterprise count, so low volume at high value. `[ASSUMPTION — not researched]`

**Band:** <40,000 → **reject band.** Per the disclosure rule, the gate fires on a *sourced or soundly derived* figure, and the dominant billing line is soundly derived. The unsourced components are acknowledged and **cannot plausibly bridge a 35,400/month gap**, but because they are unsourced the honest framing is: **the gate fires on the derived subscription line, and "confirm discretionary + Vietnam top-up frequency" sits at the top of Manual Research Recommendations.** I have not rejected the account on an assumption.

---

### Source Notes
- ✅ **Billing model is annual upfront subscription** — FY2023 20-F, verbatim quotes above. Highest-grade source available (audited annual report).
- ✅ **Adyen + Braintree confirmed** — 20-F for Adyen; agent help-centre page (updated 2026-08-19) for both, fetched and quoted directly.
- ✅ **EQT ownership, 13 Dec 2024** — EQT's own release, dateline quoted.
- ✅ **CEO Lewis Ng from March 2025, Mather chair, Williams director** — PropertyGuru's own newsroom release, 13 Jan 2025.
- ✅ **Indonesia was closed, not declining** — *"Rumah.com, which ceased to operate on November 30, 2023."* 20-F.
- ✅ **FY2023 revenue S$150.1m with full segment split** — 20-F.
- ⚠️ **PayNow absence in Singapore is NOT sourced.** The `.sg` agent help centre 403s, and my nonsense-path control *also* 403s, so a 403 proves nothing about page existence. Carried as "Not found", scored 0.
- ⚠️ **Vietnam top-up frequency not found** after two searches including Vietnamese-language terms. This is the one material gap.
- ⚠️ **`200615063H`** appears unlabelled in the group site footer. Probable Singapore UEN; not verified against ACRA/BizFile.
- ⚠️ **FY2024 full-year actuals not obtainable** — the company delisted mid-December 2024, so no FY2024 20-F exists. Only FY2024 *guidance* (S$165–180m) and Q1/Q2 2024 actuals are public. All financials here are FY2023 unless stated.
- ❌ **TAL revenue line "~$120M (FY24)" is approximately right but unit-ambiguous** — actual FY2023 was **S$150.1m** (≈US$112m at ~1.34 SGD/USD, conversion `[ESTIMATE]`, no sourced rate). Treat the TAL cell as SGD/USD-confused.

### Success Case Alternatives
**Not found.** No public Yuno case study for a Southeast Asian property classifieds operator, or for any B2B annual-agent-subscription marketplace, was verified in this run. Per the integrity mandate I am not assigning a mismatched case to fill the field, and given the recommended override there is no sequence for one to support.

---

## Executive Summary

PropertyGuru Group is Southeast Asia's leading property classifieds operator, monetising ~55,000 real-estate agents and property developers across Singapore, Malaysia, Thailand and Vietnam; EQT took it private in December 2024 at ~US$1.1bn and replaced the CEO and board in January 2025. The decisive payment finding is the **billing unit**: the company's own annual report states agents **pay upfront fees for an annual subscription**, which puts group-wide payment events at **~4,600/month** — about 11% of the 40,000/month ICP floor — and there is **no consumer payment flow at all**, since consumers browse free and the fintech line invoices banks and insurers rather than home buyers. The stack is nonetheless genuinely greenfield and mildly interesting: **Adyen handles bank transfers and Braintree handles cards on the same page**, split by method rather than geography, with Atome enabled on PropertyGuru Malaysia but *not* on sister portal iProperty Malaysia. **Motion: greenfield on paper, but the volume gate fails — recommended for analyst override and `not-icp`**, reversible only on sourced evidence that Vietnam top-ups or discretionary credit purchases run at high frequency.

---

## Section 1: Website Traffic Analysis by Country

**Data source:** **SimilarWeb, supplied by Prateek 2026-10-13** (screenshot), stored at `accounts/traffic/propertyguru.md`. Used verbatim per the resolution order; **not re-researched**. Period Jul 2026 – Sep 2026, All traffic, "Include all country domains" ON. Domains: `propertyguru.com.sg` + 4 further domains. Countries: 83. **Shares only — no absolute visit figure was supplied.**

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | **Singapore** 🔥 | **47.03%** | Not available — no absolute total supplied | ↑5.68% **growing** | SimilarWeb (supplied 2026-10-13) |
| 2 | **Malaysia** 🔥 | **41.84%** | Not available | ↑6.10% **growing** | SimilarWeb (supplied 2026-10-13) |
| 3 | United States | 1.57% | Not available | ↑10.48% | SimilarWeb (supplied 2026-10-13) |
| 4 | Australia | 1.14% | Not available | ↓4.37% | SimilarWeb (supplied 2026-10-13) |
| 5 | India | 1.05% | Not available | ↑8.92% | SimilarWeb (supplied 2026-10-13) |
| 6 | Indonesia | 0.82% | Not available | ↓43.58% | SimilarWeb (supplied 2026-10-13) |
| 7 | United Kingdom | 0.73% | Not available | ↓15.45% | SimilarWeb (supplied 2026-10-13) |
| 8 | Hong Kong | 0.52% | Not available | ↑17.79% | SimilarWeb (supplied 2026-10-13) |
| 9 | Canada | 0.40% | Not available | ↑5.71% | SimilarWeb (supplied 2026-10-13) |
| 10 | Japan | 0.30% | Not available | ↓16.38% | SimilarWeb (supplied 2026-10-13) |
| 11 | Thailand | 0.30% | Not available | ↑1.30% | SimilarWeb (supplied 2026-10-13) |

**High-priority markets (>5% share): Singapore and Malaysia only.** Nothing else reaches 2%.

### Engagement — confirmed real
Pages/visit 6.64–16.26 and bounce as low as 16.96% (Japan) and 19.54% (Hong Kong). This is classic high-intent classifieds browsing. **No junk rows.** Accepting the supplied analyst note in full.

### ⚠️ The "+4 domains" — RESOLVED, and it changes the reading
The supplied dataset names only `propertyguru.com.sg` plus "4 further domains (unnamed)". I resolved the group's domain estate by redirect chain and TLS/WAF fingerprint:

| Domain | Final URL | Status | Part of the group? |
|---|---|---|---|
| `propertyguru.com.sg` | `www.propertyguru.com.sg` | 403 Cloudflare challenge | ✅ Yes |
| `propertyguru.com.my` | `www.propertyguru.com.my` | 403 Cloudflare challenge | ✅ Yes |
| `propertyguru.com` | **→ `propertygurugroup.com`** | 301 then 403 | ✅ Yes — corporate redirect |
| `commercialguru.com.sg` | `www.commercialguru.com.sg` | 403 Cloudflare challenge | ✅ Yes |
| `iproperty.com.my` | `www.iproperty.com.my` | 403 Cloudflare challenge | ✅ Yes — separate brand |
| `ddproperty.com` | `www.ddproperty.com` | 403 Cloudflare challenge | ✅ Yes — Thailand |
| `thinkofliving.com` | `thinkofliving.com` | 403 Cloudflare challenge | ✅ Yes — Thailand |
| `batdongsan.com.vn` | `batdongsan.com.vn` | 403 Cloudflare challenge | ✅ Yes — Vietnam |
| `brickz.my` | `www.brickz.my` | 403 Cloudflare challenge | ✅ Yes — MY data |
| `asiapropertyawards.com` | `asiapropertyawards.com` | 403 Cloudflare challenge | ✅ Yes — events |
| **`sendhelper.com`** | **→ `www.propertyguru.com.sg`** | **301 Moved Permanently** | ✅ Yes — **folded into the main portal** |
| **`rumah.com`** | `www.rumah.com` | **200**, 1,979-byte static placeholder, no live portal | ⚠️ Parked — business closed 30 Nov 2023 |
| **`rumah123.com`** | `www.rumah123.com` | **200**, live Indonesian portal, **zero "propertyguru" occurrences** in source (control term "rumah123" = 5 hits, so the grep works) | ❌ **NOT a PropertyGuru property** |
| `propertyguru.com.th` / `.vn` / `.co.id` | — | DNS failure, do not exist | ❌ |

> ### ⛔ CORRECTION to the supplied analyst note (note 6)
> The note states the 4 extra domains are *"almost certainly … Thai/Indonesian properties (DDproperty, **Rumah123** and Batdongsan are group brands)."* **Two parts of that are wrong, and both matter:**
>
> **(a) Rumah123 is not a PropertyGuru brand.** Its source carries no PropertyGuru reference, it is not behind the group's Cloudflare estate, and it is absent from the group's own brand footer. PropertyGuru's Indonesian portal was **Rumah.com**, and the 20-F states it *"ceased to operate on November 30, 2023."* `rumah.com` is now a parked placeholder. **Do not treat Rumah123 as a group asset.**
>
> **(b) DDproperty and Batdongsan are group brands but are almost certainly NOT in this dataset.** Batdongsan is Vietnam's largest property portal and DDproperty is Thailand's — yet **Vietnam does not appear in the top 11 at all** and Thailand sits at **0.30%**. If those domains were aggregated in, both countries would rank top-5. The "include all country domains" setting aggregates ccTLD variants of the *same root brand*, so the 4 extra domains are the **`propertyguru.com.*` family** (`.com.my`, `.com`, plus CommercialGuru/agent subdomains), not the sister brands.
>
> **Consequence:** the supplied dataset measures the **PropertyGuru-branded SG+MY business only — ~75.8% of FY2023 group revenue (S$113.7m of S$150.1m)**. Thailand, Vietnam and iProperty Malaysia sit outside it, on separate brands and plausibly separate stacks. The dataset **understates group scale** while **correctly identifying where the money is**.

### ⚠️ Indonesia ↓43.58% is a decommissioned business, not a declining market
The supplied note flags Indonesia as "the one sharp fall". **Sourced explanation:** *"In August 2023, we announced our strategic decision to phase out our Indonesia marketplace business, Rumah.com, which ceased to operate on November 30, 2023."* The residual 0.82% is Indonesian users browsing the SG/MY sites. **Not a churn signal, and not an opportunity.**

### ⭐ The Malaysia audience-share finding — tested against revenue, and it does not hold
The supplied note observes that Malaysia's **audience share 47.94%** exceeds its traffic share 41.84% while Singapore's audience share 37.12% sits below its 47.03% traffic share, correctly concluding Malaysia has the **larger distinct user base** and inviting the hypothesis that *"Malaysia may matter more than the traffic order suggests — check revenue by segment."*

**I checked revenue by segment. The hypothesis is wrong, and decisively so:**

| Market | FY2023 revenue | Share of group | Audience share | Revenue per point of audience share |
|---|---|---|---|---|
| **Singapore** | **S$86.0m** | **57.3%** | 37.12% | **2.32** |
| **Malaysia** | **S$27.7m** | **18.5%** | 47.94% | **0.58** |

**Singapore monetises each unit of audience ~4.0× better than Malaysia** `[DERIVED from two sourced inputs: 20-F segment revenue + supplied SimilarWeb audience shares]`. Malaysia has more users and earns less than a third of Singapore's revenue. The monetisation unit is the **paying agent**, not the consumer, and Singapore's agent base is both larger-spending and better-penetrated — Singapore ARPA reached **S$1,464/quarter** while Malaysia discloses no ARPA at all. **Singapore is the commercial centre of gravity; Malaysia is the traffic centre of gravity.** For a payments conversation this inverts the priority the traffic table implies.

### ⚠️ "High traffic outside home" — double-count risk, as flagged
Singapore at 47.03% is below 60%, so the ICP row fires. **It should be read as a false positive in substance.** It fires only because Malaysia is nearly as large as Singapore — not because the business is globally distributed. PropertyGuru has **local entities and local acquiring in both** of its two markets. This is a two-market *domestic* operator, not a cross-border one, and the row overlaps with "3+ countries" off the same underlying split. Both are discounted in the override.

---

## Section 2: Legal Entities & Local Presence

**Headquarters:** Singapore. Founded 2007 (the 20-F describes "17 years of offering property information across Southeast Asia" as of FY2023). Ultimate parent **PropertyGuru Group Limited** is *"an exempted company limited"* — a **Cayman Islands** vehicle.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Cayman Is. | PropertyGuru Group Limited | Not found | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| Singapore | PropertyGuru Pte. Ltd. | ⚠️ `200615063H` — unlabelled in site footer, probable UEN, **unverified** | [Group site](https://www.propertygurugroup.com/) |
| Singapore | Sendtech Pte. Ltd. (Sendhelper) | Not found | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| Singapore | Epsilon Asia Holdings II Pte. Ltd. | Not found | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| Malaysia | PropertyGuru International (M) Sdn Bhd | Not found | [AgentNet help centre](https://myagentofferings.propertygurugroup.com/help-centre/welcome-to-agentnet/payments/payment-methods-2/) |
| Malaysia | iProperty.com Malaysia Sdn. Bhd. | Not found | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| Malaysia | Brickz Research Sdn. Bhd. | Not found | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| Malaysia | IPGA Management Services Sdn. Bhd. | Not found | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| Thailand | PropertyGuru International (Thailand) Co., Ltd. | Not found | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| Thailand | DDProperty Media Ltd. | Not found | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| Thailand | iProperty (Thailand) Co., Ltd. | Not found | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| Thailand | Prakard IPP Co., Ltd. | Not found | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| Thailand | Kid Ruang Yu Co., Ltd | Not found | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| Vietnam | PropertyGuru Viet Nam Joint Stock Company | Not found | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |

> **MANUAL:** Registration numbers were not obtainable. `zaubacorp.com` and `thecompanycheck.com` are blocked in this environment and ACRA/BizFile was not reachable. Verify `200615063H` and the Sdn Bhd numbers via ACRA BizFile and SSM e-Info directly.

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| **Singapore** | ✅ #1 (47.03%) | ✅ Yes | No — not gated | **None.** Local entity, local acquiring, SGD billing. |
| **Malaysia** | ✅ #2 (41.84%) | ✅ Yes (two entities) | No — not gated | **None.** Local entity, local CIMB bank account, MYR billing, local bank-transfer rail live. |
| United States | ✅ #3 (1.57%) | ❌ No | N/A | **None** — no sales operation; diaspora browsing only. |
| Australia | ✅ #4 (1.14%) | ❌ No | N/A | **None** — awards events only. |
| India | ✅ #5 (1.05%) | ⚠️ Tech staff (Bengaluru), no revenue entity confirmed | ⚠️ Would be gated if they transacted | **None today** — cost centre, not a revenue market. |
| Vietnam | ❌ Not in supplied data | ✅ Yes | ⚠️ Verify SBV intermediary licensing if payments change | Low — local entity present. |
| Thailand | ✅ #11 (0.30%) | ✅ Yes (five entities) | No | Low — local entities present. |

> **There is no cross-border warning to issue on this account.** Both markets that matter have a local entity, local billing and a local rail. This is unusual in this pipeline and it removes the single most common Yuno entry point. **The standard cross-border/approval-rate framing does not apply here and must not be used.**

---

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Group-wide (vendor list) | **Adyen** — *"Adyen Payment Gateway for payment collection"* | `[Regulatory Filing]` FY2023 20-F | [SEC](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| Malaysia (agent billing) | **Adyen** — online bank transfer leg | `[Terms/Help Centre]` page updated 2026-08-19 | [AgentNet](https://myagentofferings.propertygurugroup.com/help-centre/welcome-to-agentnet/payments/payment-methods-2/) |
| Malaysia (agent billing) | **Braintree** — credit/debit card leg | `[Terms/Help Centre]` page updated 2026-08-19 | [AgentNet](https://myagentofferings.propertygurugroup.com/help-centre/welcome-to-agentnet/payments/payment-methods-2/) |
| Malaysia (agent billing) | **Atome** — BNPL, 3/6/9/12-month plans, QR-initiated | `[Terms/Help Centre]` | [Atome FAQ](https://www.agentofferings.propertyguru.com.my/help-centre/pay-with-atome-my/) |
| Malaysia (agent billing) | **CIMB Bank**, **Public Bank** — interest-free card instalments; CIMB also cheque-collection bank | `[Terms/Help Centre]` | [AgentNet](https://myagentofferings.propertygurugroup.com/help-centre/welcome-to-agentnet/payments/payment-methods-2/) |
| Singapore (agent billing) | **Not verified** — `.sg` agent help centre unreachable | — | — |
| Vietnam / Thailand | **Not found** | — | — |

**Verbatim, from the fetched Malaysia agent payment page (updated 2026-08-19):**
> *"You could choose to pay through online bank transfer (powered by Adyen payment gateway), directly with your credit or debit card (powered by Braintree payment gateway) or through interest-free installment plans (through Public Bank & CIMB)."*

**The architecture is a method-split, not a region-split.** Two gateways sit on one checkout page, each owning a payment type: Adyen the bank rail, Braintree the card rail. Braintree is a PayPal-owned gateway; Adyen a full acquirer. That is an unusual, historically-accreted pairing and the one genuinely interesting technical fact on this account.

**Offline rail is live and endorsed, not legacy:**
> *"some agents prefer to pay by cheque, in which we still continue to support this method… Made payable to: 'PropertyGuru International (M) Sdn Bhd'"* with a CIMB Bank account `[account number published on the page — value deliberately not recorded]`. An **"Others"** option routes agents to offline payment, and even offline payers *"must still accept the terms and confirm your order in AgentNet."*

**Card data handling:** card fields are collected in PropertyGuru's own payment page (*"enter your card information: name on card, the 16-digit credit/debit card number, expiration date and security code (CCV)"*) with *"Your credit card details are encrypted and sent over a secured connection."* Whether this is a Braintree hosted-field iframe or self-hosted fields **cannot be determined without walking the authenticated flow** — it materially affects PCI scope. See §9.

### 3B. Payment Orchestrator

**Classification: None detected — direct PSP integrations only (greenfield).**

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with PSP(s), which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

**Evidence for the classification:**
- The FY2023 20-F's third-party vendor paragraph lists payment collection as a single-vendor function alongside NetSuite (ERP), Salesforce (CRM), Cloudsense (order management), Google and Meta (advertising) — *"and Adyen Payment Gateway for payment collection."* No routing or orchestration layer appears anywhere in the filing. `[Regulatory Filing]`
- Raw-text sweep of the full 6.65MB 20-F: **"orchestration" = 0 occurrences** (control term "PropertyGuru" = 207, so the grep is sound).
- The agent payment page describes a **static method-to-gateway mapping** — bank transfer always Adyen, cards always Braintree — which is the signature of two direct integrations, not a routing layer.
- No orchestration vendor appears in any job posting, press release or help-centre page found.

**Honest caveat on the "greenfield" label.** Greenfield here means *no orchestration layer exists*, which is true. It does **not** mean an orchestration opportunity exists. The merchant has two gateways, two markets, local entities in both, no cross-border exposure and ~4,600 payment events a month. **The absence of orchestration at this merchant is a rational architectural choice, not a gap.** Scoring +4 on this row is correct by the rule and misleading as a signal; the override addresses it.

> **MANUAL:** The agent checkout sits behind an AgentNet login, so DevTools inspection requires agent credentials. The help-centre pages are the best public substitute and were used.

---

## Section 4: Alternative & Local Payment Methods

Checked against `.claude/reference/apac-payments.md` §2 for the only two markets with >1% meaningful share. **Per the brief, no rail work was done outside SG/MY.**

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| **Malaysia** | **FPX (online banking)** | Bank transfer / A2A | **Active in checkout** — *"select your preferred bank… redirected to an online banking page to login to your selected bank"*, powered by Adyen. Functionally the FPX flow; **the page never uses the string "FPX"**, so the brand is `[INFERENCE, not confirmed]` while the *mechanism* is confirmed | [AgentNet](https://myagentofferings.propertygurugroup.com/help-centre/welcome-to-agentnet/payments/payment-methods-2/) |
| **Malaysia** | Cards (credit/debit) | Cards | **Active in checkout** via Braintree | [AgentNet](https://myagentofferings.propertygurugroup.com/help-centre/welcome-to-agentnet/payments/payment-methods-2/) |
| **Malaysia** | **Atome** | BNPL/Instalments | **Active in checkout** — PropertyGuru MY only, *"not yet available for iProperty (Malaysia)"*, 3/6/9/12 months, no minimum | [Atome FAQ](https://www.agentofferings.propertyguru.com.my/help-centre/pay-with-atome-my/) |
| **Malaysia** | CIMB / Public Bank card instalments | BNPL/Instalments | **Active in checkout** | [AgentNet](https://myagentofferings.propertygurugroup.com/help-centre/welcome-to-agentnet/payments/payment-methods-2/) |
| **Malaysia** | Cheque / offline bank transfer | Bank transfer | **Active** and explicitly supported | [AgentNet](https://myagentofferings.propertygurugroup.com/help-centre/welcome-to-agentnet/payments/payment-methods-2/) |
| **Malaysia** | **Touch 'n Go eWallet** | Digital wallet | **Unknown** — a terms-and-conditions article for a "Touch 'n Go entitlement" on renewal/upgrade exists in the Payments section of the help centre, but the page 404'd on fetch and its mechanics are unconfirmed. **Possibly a reward, not a payment method.** | Title only, via search index |
| **Malaysia** | **DuitNow** | Bank transfer / A2A | **Not found** | — |
| **Malaysia** | GrabPay, Boost | Digital wallet | **Not found** | — |
| **Singapore** | **PayNow** | Bank transfer / A2A | ⚠️ **Not found — but absence NOT sourced.** See caveat below. | — |
| **Singapore** | Cards | Cards | **Unknown, checkout not accessible** — `[INFERENCE, not confirmed]` that the group-level Adyen/Braintree pairing also serves SG | — |
| **Singapore** | GrabPay | Digital wallet | **Not found** | — |
| Group-wide | Apple Pay / Google Pay / PayPal | Digital wallet | **Not found** | — |
| Group-wide | UPI, QRIS, PromptPay, GCash, konbini, Alipay | — | **Not applicable** — no traffic, no sales operation. Not researched, per the brief. | — |

> ### ⚠️ The PayNow question — why it scores ZERO and not +3
> PayNow is Singapore's dominant A2A consumer rail and Singapore is market #1 by traffic (47.03%) and #1 by revenue (57.3%). PayNow appears **nowhere** in any source I reached. That looks like a textbook +3 "local rail gap in a top-3 market".
>
> **I am not awarding it, for two reasons:**
>
> **1. The absence is not sourced.** `www.agentofferings.propertyguru.com.sg` returns **403 to both curl and WebFetch** — and critically, **my nonsense-path control also returned 403 with a near-identical body size**. On that host a 403 is a Cloudflare managed challenge, so it carries **zero information** about whether a page exists or what it says. I cannot distinguish "PropertyGuru does not offer PayNow" from "I could not read the Singapore page." The ICP rule is explicit: *"Requires a source for the absence, not an assumption."*
>
> **2. PayNow may be the wrong rail to expect here.** PayNow is a *consumer* P2P/P2M rail. The payer is a professional agent settling a ~S$5,200 annual invoice, frequently via corporate bank transfer or cheque. The corporate-grade equivalent already appears to be live. A missing consumer wallet on a high-ticket B2B invoice is a much weaker gap than a missing consumer rail on a consumer checkout.
>
> **This is the one row where more research could legitimately move the score** — but only by +3, to 15/29, still 🟢 Medium and still inside the override.

**Malaysia rail coverage is, if anything, good.** The dominant local bank rail is live via Adyen, cards via Braintree, and **two** instalment mechanisms plus BNPL are offered — appropriate for a high-ticket annual purchase by a commission-paid agent. I can issue **no "widely used but not supported" warning for Malaysia** on the evidence found. The one genuine defect is *internal*: Atome works on one of the two Malaysian portals the company sells as a bundle.

**Recurring rails:** Not applicable in the usual sense. These are **not auto-renewing subscriptions.** Renewal is a **manual, windowed re-purchase** — agents may only renew in an "Early Bird" window (the month before expiry) or the "Actual Month" window, with a discount for renewing early `[via search index; the .sg renewal page itself 403'd]`. There is no card-on-file mandate book, so **no UPI Autopay / PayTo / e-mandate angle exists**, and the involuntary-churn mechanics in `subscription-payments.md` §1 largely **do not apply**: an 80–81% renewal rate on a manually-renewed annual package is a *sales and pricing* outcome, not a failed-payment outcome.

> **MANUAL:** Verify the Singapore agent payment methods from inside AgentNet, or by asking an agent. This is the single highest-value manual check on the account.

---

## Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| — | — | — | — | — |

*"No payment-related complaints found on Reddit, X, Trustpilot, or app store reviews."*

Searches covering agent payment failures, renewal billing, AgentNet charges and refunds returned **no first-party complaint content** — only PropertyGuru's own help-centre pages and unrelated vendors' dunning-product pages.

**This is a structurally expected null, not a gap in research.** Three reasons: (a) the payers are ~55,000 business customers, not millions of consumers, so there is no consumer-review surface; (b) each agent has a **named sales representative** who handles payment verification and activation (*"contact your sales representative to verify your payment"*), which routes friction into a private channel; and (c) at one payment per year per agent there are very few opportunities to fail. **0 points, and no orchestration pain pattern can be claimed.**

---

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | **2026-09-28** | CEO **Lewis Ng** keynote, *"Building Organisations Where AI Works for Humans and Business Wins"*, ET Future Singapore Conference — confirms Ng in post; strategic focus is **AI**, not payments | Leadership / Tech Signal | [Newsroom](https://www.propertygurugroup.com/newsroom/) |
| 2 | **2025-11-01** | **Package and pricing overhaul (MY)** — updated PropertyGuru agent package prices; new **"Core+"** dual-platform entry package; **Prime Credits discontinued**, balances expire **30 May 2026**; listing duration standardised to 60 days from 3 Nov 2025 | Pricing / Billing Change | [PropertyGuru MY](https://www.agentofferings.propertyguru.com.my/?p=11096) |
| 3 | **2025-01-13** | **Leadership transition and new board** — Hari V. Krishnan steps down after a decade to Senior Advisor; **Lewis Ng** CEO from March 2025; **Trevor Mather** (ex-Auto Trader CEO) Chairman; **Janice Leow** (EQT Partner, Head of EQT Private Capital SEA) and **Ed Williams** (Rightmove founder, ex-Auto Trader chairman) directors | Leadership Change | [Newsroom](https://www.propertygurugroup.com/newsroom/propertyguru-announces-leadership-transition-and-a-new-board/) |
| 4 | **2024-12-13** | **EQT completes take-private.** US$6.70/share cash, ~US$1.1bn equity value, BPEA Private Equity Fund VIII; *"the Company has been delisted from the New York Stock Exchange"*; *"PropertyGuru will operate as a privately held company"* | M&A / Ownership | [EQT](https://eqtgroup.com/news/eqt-completes-acquisition-of-propertyguru) |
| 5 | **2023-11-30** | **Indonesia marketplace Rumah.com ceased operating** (announced Aug 2023). Contributed S$2.5m in FY2023. **PropertyGuru FastKey sunset** the same year | Market Exit | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |

**No public payment-related RFP found.**
**No payment-related job postings found.** The only relevant engineering role located — "Head of Engineering", covering *"engineering teams across our marketplaces in Singapore, Malaysia, and Thailand"* — carries **no payments scope**, and notably **excludes Vietnam**, supporting the read that Batdongsan runs on a separate technical stack.
**No funding or financing event in the last 12 months.** The EQT transaction is ~22 months old. No 2025/2026 debt facility or refinancing was found for PropertyGuru itself.

**The board composition is the most strategically interesting finding in this section.** EQT installed **the founder of Rightmove and the former CEO of Auto Trader** — the two most successful agent-subscription classifieds businesses in the UK. Both monetise via agent subscriptions, exactly PropertyGuru's model. This signals a **yield-and-pricing playbook** (raise ARPA on a fixed agent base), which is consistent with the Nov 2025 repricing. **It is not a payments-infrastructure signal.**

---

## Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 2025-11-01 | **Prime Credits withdrawn** from PropertyGuru packages; remaining balances expire 30 May 2026, no reimbursement | **Direct.** Removal of a purchasable credit product — *reduces* discretionary payment events and shrinks an already-small count | [PropertyGuru MY](https://www.agentofferings.propertyguru.com.my/?p=11096) |
| 2 | 2025-11-01 | **"Core+"** launched as a lower-priced dual-platform package spanning PropertyGuru **and** iProperty Malaysia | **Direct.** One payment spanning two portals with *different* payment capabilities (Atome on one, not the other) | [PropertyGuru MY](https://www.agentofferings.propertyguru.com.my/?p=11096) |
| 3 | Undated (≈2025) | **Atome BNPL enabled** for PropertyGuru Malaysia agent payments; QR-initiated, 3/6/9/12-month plans, no minimum; **explicitly not available on iProperty Malaysia** | **Direct.** A genuine new payment method, and the clearest evidence of per-portal stack divergence | [Atome FAQ](https://www.agentofferings.propertyguru.com.my/help-centre/pay-with-atome-my/) |
| 4 | Undated (≈2025–26) | **"Credit Back Rewards"** product update published on both the SG and MY agent portals | Indirect. A credit-incentive scheme; mechanics not fetched | Title only, via search index |
| 5 | 2020-03 | **PropertyGuru Finance** launched as a **mortgage marketplace** — *brokerage-style, not a lending facility* | **Direct and decisive for the consumer question** — see below | [FintechNews SG](https://fintechnews.sg/38380/proptech/propertyguru-launches-mortgage-marketplace/) |

> **REMOVAL: PropertyGuru discontinued "Prime Credits" as part of its updated packages, effective 1 November 2025, with remaining balances expiring 30 May 2026.** Source: [PropertyGuru MY](https://www.agentofferings.propertyguru.com.my/?p=11096). Prime Credits were previously *"available for individual purchase"* — so this removes one of the few recurring discretionary payment events in the model.

### 🛑 The consumer-side question — answered, with sources
The brief required checking whether **any** consumer payment flow exists, since that would change the account completely. **I looked in four places. There is no consumer payment flow.**

1. **PropertyGuru Finance (mortgage marketplace)** — the 20-F revenue-recognition note settles it: *"Loan and insurance referral income is recognised at a point in time upon successful loan approval by financial institutions… **The financial institutions and insurance providers are invoiced** upon loan approval and insurance policy inception."* **PropertyGuru invoices the banks, not the home buyer.** No consumer money moves. Independently characterised in press as *"a brokerage-style offering… not a lending facility."* The whole Fintech & Data segment was **S$1.553m in Q2 2024 — 3.8% of revenue.**
2. **Sendhelper (home services)** — the only business where consumers ever paid. Revenue was *"recognised on a **net basis**… upon completion of a successful rendering of household services by the third-party service providers to consumers"* — a marketplace take-rate model. **But `sendhelper.com` now 301-redirects to `www.propertyguru.com.sg`**, so the standalone consumer property no longer exists. Whatever consumer flow remains is folded into the portal and unquantified.
3. **Booking or application fees on listings** — **not found**. Consumers browse free; the 20-F describes no consumer-paid product.
4. **Data, events and developer products** — all **invoiced** B2B (*"customers are invoiced at the start of the service period"*, *"customers may be invoiced upfront"* for events).

**Conclusion: this is a purely B2B billing operation.** The consumer-marketplace framing that would make PropertyGuru an orchestration target does not apply.

---

## Section 8: Checkout Experience Audit

**Partially accessible.** There is **no consumer checkout to audit** — consumers never pay. The agent checkout sits behind an AgentNet login. The consumer portals (`propertyguru.com.sg`, `.com.my`) return **Cloudflare managed challenges (403, `cf-mitigated: challenge`) to every automated client**, confirmed against a nonsense-path control that returned 403 at near-identical size. Findings below are reconstructed from **fetched agent help-centre pages**, not from walking the flow.

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | **Custom-built**, authenticated, inside AgentNet; initiated from an emailed payment link or a "See Details" button on a pending-payments page. Sales-rep-assisted variant also exists | Fair | B2B order-confirmation flow, not a storefront |
| Guest checkout | **N/A** — AgentNet account mandatory; even offline payers *"must still accept the terms and confirm your order in AgentNet"* | N/A | Correct for B2B |
| Steps to complete payment | **≥5 named steps** (select order → confirm → "Pay Now" → choose method → authorise). Sales-rep involvement for cheque/offline | Fair | Long, but appropriate for a ~S$5,200 purchase |
| Card input experience | **Self-rendered card fields** on PropertyGuru's own page — *"name on card, the 16-digit credit/debit card number, expiration date and security code (CCV)"*; *"encrypted and sent over a secured connection"*. Whether these are Braintree hosted fields could not be determined | ⚠️ **Unknown — material** | Drives PCI scope. See §9 |
| Payment methods visible | MY: online bank transfer (Adyen), cards (Braintree), Atome, CIMB/Public Bank instalments, cheque/"Others". SG: **not verified** | Good (MY) | Strong method breadth for the market |
| Location-based method display | **Per-portal, not per-user-geo** — methods are configured by property (PropertyGuru MY vs iProperty MY differ) rather than adapting to the payer | ⚠️ Poor | Atome on one portal, not the other |
| Instalment / EMI options | **Present and plentiful in Malaysia** — Atome 3/6/9/12 months **plus** CIMB and Public Bank interest-free card instalments | **Good** | Exactly right for a commission-paid agent facing a large annual bill |
| 3DS implementation | **Not detected** — no public reference found | Unknown | Expect 3DS2 via Braintree, unverified |
| PCI indicator | Card fields rendered on PropertyGuru's own payment page; iframe vs self-hosted unresolved | ⚠️ Unknown | See §9 |
| Mobile responsiveness | Not assessable — flow behind login; Cloudflare blocks automated access | Unknown | — |
| Multi-currency / local pricing | **Local currency per market via local entity** — MYR billed by PropertyGuru International (M) Sdn Bhd into a CIMB account; SGD billed by the Singapore entity. **No multi-currency single-entity exposure** | **Good** | Removes the FX angle entirely |
| Saved payment methods | **Not found.** Billing/Receipts history exists in AgentNet ("More" → "Billing" → "Receipts") | Unknown | With annual billing, card-on-file has little purpose |
| Error message clarity | Not assessable | Unknown | — |

*"Full checkout flow not accessible. Findings limited to publicly observable elements."*

---

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **Not found** | — |
| Card data handling | ⚠️ **Ambiguous — cannot be resolved publicly.** Card fields are described as entered on PropertyGuru's own payment page with encryption in transit. That reads as either **SAQ A** (Braintree hosted fields/iframe, PropertyGuru's page merely hosting them) or **SAQ A-EP** (self-hosted fields posting to Braintree). The help-centre wording does not distinguish them | [AgentNet](https://myagentofferings.propertygurugroup.com/help-centre/welcome-to-agentnet/payments/payment-methods-2/) |
| Recommended Yuno integration | **Not applicable on current evidence** — see the override. Were it ever in scope, an SDK/hosted-fields integration would be the only sensible route | — |

*"No direct PCI compliance documentation found publicly for PropertyGuru."* A raw sweep of the FY2023 20-F found **no occurrence of "PCI"** in any compliance discussion.

> `[INFERENCE, not confirmed]`: Based on confirmed use of Braintree for card capture and Adyen for bank transfers, PropertyGuru's card-data scope is **likely reduced**, with Braintree handling card data. The self-rendered-field wording leaves genuine room for SAQ A-EP scope, which would be the only mild technical hook on this account — and it is not enough to carry a sequence.

---

## Section 10: Strategic Insights & Outreach Angles

> **Read this section with the override in mind.** Each insight below is cross-referenced and real. **None of them is strong enough to justify outreach at ~4,600 payment events/month**, and I am not dressing them up as if they were. They are recorded so that if the volume picture changes, the angles are ready.

> **Insight #1: The account fails on billing unit, not on sophistication — and that is the finding worth keeping.**
> **Evidence:** §3A + §12 — the company's own 20-F states agents *"pay upfront fees for an annual subscription"* with *"over 55,000 agents"*, giving ~4,600 payment events/month; §7 confirms the fintech line **invoices banks, not consumers**, and the one consumer property (`sendhelper.com`) now **301s to the main portal**.
> **Pain Point:** None that orchestration addresses. PropertyGuru's payment operation is small, local, well-matched to its model, and already offers the right rails in its second-largest market.
> **Yuno Value Proposition:** **Honestly, none at current volume.** Routing, failover, retry logic and local acquiring all presuppose transaction density that does not exist here. Claiming otherwise would be the error this report exists to prevent.
> **Best Success Case:** Not found — no verified Yuno public case study matches a B2B annual-agent-subscription marketplace.
> **Outreach Angle:** **Do not open this thread on payments.** If Prateek ever contacts them, the only intellectually honest reason is the §12 Vietnam/discretionary-credit question — i.e. a discovery question, not a pitch.
> **Suggested Subject Line:** *N/A — no outreach recommended.*

> **Insight #2: One agent, one bundled package, two portals, two different payment capabilities.**
> **Evidence:** §4 + §7 — Atome is *"currently enabled for PropertyGuru Malaysia payments only… not yet available for iProperty (Malaysia)"* ([Atome FAQ](https://www.agentofferings.propertyguru.com.my/help-centre/pay-with-atome-my/)), while from 1 Nov 2025 the same agent buys *"Plus All-Access Packages"* including **Core+** spanning *"both platforms"* ([package update](https://www.agentofferings.propertyguru.com.my/?p=11096)).
> **Pain Point:** Payment capability is configured **per acquired portal**, so enabling a method is an N-times project across brands. This is the authentic consequence of growth by acquisition — iProperty and Brickz came from REA in 2021, DDproperty and Batdongsan from earlier deals — and it is exactly what a single integration layer removes.
> **Yuno Value Proposition:** One integration, one method catalogue, enabled once and inherited by every brand and portal — instead of per-portal gateway configuration.
> **Best Success Case:** Not found — not asserting one.
> **Outreach Angle:** *Genuinely the strongest observation available* — a specific, verifiable, company-stated inconsistency. **Still not worth a sequence at this volume.**
> **Suggested Subject Line:** *Held — Atome on PropertyGuru MY but not iProperty MY.*

> **Insight #3: Two gateways split by method, inherited rather than designed.**
> **Evidence:** §3A + §3B — Adyen owns bank transfer and Braintree owns cards on the **same** page; the 20-F lists payment collection as a single-vendor procurement line *"Adyen Payment Gateway for payment collection"* alongside NetSuite and Salesforce; **"orchestration" appears 0 times** in the filing against a control of 207 for "PropertyGuru".
> **Pain Point:** Two gateway relationships, two reconciliation surfaces, two sets of failure modes, and a static method→gateway map with no failover if either leg degrades on a renewal day. Renewals concentrate into two windows per agent, so a gateway problem lands on a peak.
> **Yuno Value Proposition:** Consolidated reporting and reconciliation across both providers, with failover between them rather than a hard-coded mapping.
> **Best Success Case:** Not found.
> **Outreach Angle:** Held — accurate but thin, and it describes a two-gateway stack that is adequate for the volume it carries.
> **Suggested Subject Line:** *Held.*

> **Insight #4: The cross-border and rail-gap playbooks both fail here — record it so nobody re-runs them.**
> **Evidence:** §2 + §4 — local entities confirmed in **both** markets that matter (PropertyGuru Pte. Ltd.; PropertyGuru International (M) Sdn Bhd with its own CIMB account), local-currency billing in each, and Malaysia's dominant bank rail **already live** via Adyen. §1 shows 88.87% of traffic in those two markets.
> **Pain Point:** For Yuno, none. For the SDR, a trap: the matrix awards +2 for "high traffic outside home" and +3 for "3+ countries", which together imply an international, cross-border merchant. **It is not one.**
> **Yuno Value Proposition:** N/A — there is no cross-border leg, no FX exposure, and no regulatory acquiring gate in either core market.
> **Best Success Case:** N/A.
> **Outreach Angle:** **Negative finding, deliberately recorded.** Any future email leading on cross-border approval rates or FX would be factually wrong and would burn the thread.
> **Suggested Subject Line:** *N/A.*

---

### Quick Hits: Ready-to-Use Sales Ammunition

> ⚠️ **No outreach is recommended for this account.** Per the integrity mandate I will not write hooks implying a pitch I have just argued against. What follows are **discovery questions** to resolve the volume question if Prateek chooses to make one call — not email hooks.

**Discovery questions (the only honest use of this research):**
1. "In Vietnam you run pay-as-you-go rather than annual packages — when an agent credits money into their Batdongsan account, how often does that actually happen, and what rail do they use?" *(This single answer decides whether the account is viable.)*
2. "Agents can buy discretionary Ad Credits beyond what the annual package bundles — what share of agents top up in a given month?"
3. "Atome is live on PropertyGuru Malaysia but not iProperty Malaysia, while Core+ is sold across both — what does enabling a new method on a second portal involve today?"

**Email hooks:** *None written. The account does not clear the volume gate and no hook would be truthful.*
**Cold call openers:** *None written. See discovery questions above.*

---

## Section 11: Similar Companies & Prospecting Pipeline

### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| **99 Group (99.co + SRX)** | 99.co | Singapore | ~1.31M visits/mo (SG, May 2025) | Singapore, Indonesia | **Not found** | [Vulcan Post](https://vulcanpost.com/721827/99-group-acquires-srx) · [Semrush](https://cw.semrush.com/website/propertyguru.com.sg/competitors) |
| **EdgeProp Singapore** | edgeprop.sg | Singapore | ~800K visits/mo | Singapore | **Not found** | [Semrush](https://cw.semrush.com/website/propertyguru.com.sg/competitors) |
| **SRX / Streetsine** | srx.com.sg | Singapore | ~183K visits/mo | Singapore | **Not found** — acquired by 99 Group (SPA 7 Nov 2020, Streetsine Singapore Pte Ltd) | [Vulcan Post](https://vulcanpost.com/721827/99-group-acquires-srx) |
| **Mudah.my** | mudah.my | Malaysia | ~7.95M visits/mo (Mar 2026) | Malaysia | **Not found** | [Semrush](https://www.semrush.com/website/edgeprop.my/competitors/) |
| **EdgeProp Malaysia** | edgeprop.my | Malaysia | Not found | Malaysia | **Not found** | [Semrush](https://www.semrush.com/website/edgeprop.my/competitors/) |
| **Ohmyhome** | ohmyhome.com | Singapore | ~61K visits/mo | Singapore, Malaysia | **Not found** | [Semrush](https://tr.semrush.com/website/99.co/competitors) |
| ⚠️ **Rumah123** | rumah123.com | Indonesia | Live portal, 200 OK | Indonesia | **Not found** | Direct fetch — **listed here to correct the record: NOT a PropertyGuru brand** |

⚠️ **Mudah.my out-traffics PropertyGuru Malaysia (~7.95M vs ~3.05M visits/mo)** but is a **general** classifieds site, not a property specialist — treat it as an adjacent, not a direct, competitor. All visit figures are **Semrush, different months, `[ESTIMATE, not confirmed]`** and are not market share.

⚠️ A blog post asserting PropertyGuru holds *"82% market share with 5.7x traffic advantage"* was returned by search. **I could not verify it against any primary source and the page self-describes as containing hypothetical scenarios. Do not use this figure.**

### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| **Rightmove** | rightmove.co.uk | Property classifieds | UK | **Same monetisation model** — agent subscriptions. PropertyGuru's board now includes its founder, Ed Williams | [Newsroom](https://www.propertygurugroup.com/newsroom/propertyguru-announces-leadership-transition-and-a-new-board/) |
| **Auto Trader** | autotrader.co.uk | Vehicle classifieds | UK | Dealer-subscription model; PropertyGuru's chairman Trevor Mather is its former CEO | [Newsroom](https://www.propertygurugroup.com/newsroom/propertyguru-announces-leadership-transition-and-a-new-board/) |
| **REA Group** | rea-group.com | Property classifieds | Australia, Asia | **Former PropertyGuru shareholder**; sold iProperty MY/TH to PropertyGuru in 2021 | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| **Carousell Group** | carousell.com | General + property classifieds | SG, MY, PH, TW | SEA classifieds with both consumer and B2B payment flows | [Semrush](https://www.semrush.com/website/propertyguru.com.my/competitors/) |
| **Ohmyhome** | ohmyhome.com | PropTech / brokerage | SG, MY | Nasdaq-listed; takes **transaction-linked** fees, so a genuinely different (and more payment-intensive) model | [Semrush](https://tr.semrush.com/website/99.co/competitors) |

**Vertical lesson, recorded for the pipeline:** property *classifieds* monetise via **low-frequency, high-value B2B agent subscriptions**. On the evidence here, the whole sub-vertical is likely to fail the 40,000/month gate on billing-unit grounds. **Property *brokerage* and *transaction* platforms (e.g. Ohmyhome) are the payment-bearing half of PropTech.** Worth steering future PropTech prospecting toward transaction-fee models and away from classifieds.

### 11C. Companies Recently Adopting Payment Orchestration

*"No public case studies found of direct competitors adopting payment orchestration."*

No SEA property portal was found to have adopted any orchestration platform. **0 points.** Consistent with the sub-vertical's billing model: there is little to orchestrate.

### 11D. Prospect Scoring

Applying the 29-point matrix to the peers above yields **almost nothing scoreable** — none publishes a transaction count, PSP stack or orchestrator, and most are private.

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| Monthly transaction count | 0 | ⬜ Not published for any competitor | — |
| Orchestration status | 0 | ⬜ Uncertain for all | — |
| 3+ countries | 0–3 | ⬜ 99 Group (SG+ID) and Carousell (4+ markets) only plausible candidates; unverified | [Semrush](https://cw.semrush.com/website/propertyguru.com.sg/competitors) |
| Multiple PSPs | 0 | ⬜ No PSP evidence found for any competitor | — |
| All remaining signals | 0 | ⬜ Insufficient public data | — |

**Honest conclusion: no competitor could be scored above "uncertain" on any row.** Fabricating a pipeline table here would breach the integrity mandate.

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | **Carousell Group** | Peer | SG, MY, PH, TW, HK | **Not scored** | 🟢 Worth researching | Multi-market SEA classifieds with **consumer** payment flows + Carousell Pay — a real payment-bearing model, unlike classifieds-only peers | ❌ **Not on TAL — genuine new find** |
| 2 | **Ohmyhome** | Peer | SG, MY | **Not scored** | 🟢 Worth researching | Nasdaq-listed, **transaction-fee** brokerage model — the payment-bearing half of PropTech | ❌ **Not on TAL — genuine new find** |
| 3 | **99 Group (99.co + SRX)** | Direct competitor | SG, ID | **Not scored** | 🟡 Low expectation | Largest SG rival, but same agent-subscription billing unit — likely fails the same gate | ❌ Not on TAL |
| 4 | **Mudah.my** | Adjacent | MY | **Not scored** | 🟡 Low expectation | Highest-traffic MY classifieds (~7.95M/mo); general classifieds may carry consumer payments | ❌ Not on TAL |
| 5 | **EdgeProp SG / MY** | Direct competitor | SG, MY | **Not scored** | 🔴 Skip | Smaller, same billing unit | ❌ Not on TAL |

> ⚠️ **Only five entries are listed, not ten.** I could not identify ten APAC prospects from this account's competitive set that are worth a research run. Padding the table with portals that share PropertyGuru's disqualifying billing unit would waste research budget — the point of this section is to generate leads, not rows.

> ### ⛔ CORRECTION — PropertyGuru **IS** on the TAL
> The brief states: *"I checked: PropertyGuru has NO row. A genuine new find if it scores; say so in Section 11."*
>
> **That is incorrect. There is a row**, at **line 805** of `accounts/apac-tal.csv`:
>
> ```
> PropertyGuru International,propertygurugroup.com,Real Estate & PropTech,
> "Southeast Asian property portal group across Singapore, Malaysia, Thailand and Vietnam;
> agent subscriptions billed in several countries and currencies.",
> ,,Not Contacted,,,,,,Singapore,,~$120M (FY24),Search: PropertyGuru International,
> ```
>
> It was missed because it is filed under **"PropertyGuru International"** with website **`propertygurugroup.com`**, not "PropertyGuru" / `propertyguru.com.sg`. **So this is not a new find — it is an existing, never-contacted TAL account.**
>
> Three things in that row are worth noting:
> - **`Payment Gateway` and `Payment Orchestrator` columns are both empty** — consistent with my independent finding of no orchestrator, and the Adyen/Braintree pairing is net-new intelligence for the TAL.
> - The INFO field's hypothesis — *"agent subscriptions billed in several countries and currencies"* — is **verified correct**, and is precisely what disqualifies the account: agent subscriptions, billed annually.
> - **`~$120M (FY24)`** is approximately right but unit-ambiguous: actual FY2023 revenue was **S$150.1m** (≈US$112m `[ESTIMATE]`). FY2024 actuals do not exist publicly — the company delisted in December 2024.
>
> **Recommended TAL action:** populate `Payment Gateway` = "Adyen (bank transfer) + Braintree (cards)", `Payment Orchestrator` = "None detected", and mark the account **not-ICP on volume** so it is not re-researched.

---

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | **S$150.1m FY2023** (≈US$112m `[ESTIMATE]`, ~1.34 SGD/USD, **no sourced rate**). FY2024 **guidance** S$165–180m; **no FY2024 actual exists** (delisted Dec 2024) | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm); [Q2 2024](https://www.sec.gov/Archives/edgar/data/0001873331/000095017024103090/pgru-ex99_1.htm) |
| GMV / Gross Transaction Volume | **N/A — the concept does not apply.** PropertyGuru never takes custody of property transaction value. Revenue *is* its payment volume | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| Average Transaction Value (USD) | **~S$5,218 per Singapore agent per year** `[DERIVED: S$86.0m ÷ 16,481 agents]`. High-ticket, low-frequency | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| Est. Annual Transactions | **~55,000 subscription payments/year** `[DERIVED: agent count × 1 annual upfront payment]` | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| **Monthly transaction count** | ✅ **DERIVED: ~4,600/month.** **Billing unit = one upfront annual subscription payment per agent.** 55,000 agents ÷ 12 = 4,583. Both inputs sourced to the FY2023 20-F. **<40,000 ⇒ reject band.** Excludes discretionary credit purchases, Vietnam wallet top-ups and developer/events invoices, whose frequencies are **`[ASSUMPTION — not researched]`** | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| Active Customers / Users | **Paying customers: 55,000+ agents** (3-mo avg, 31 Dec 2023), of which **16,481 in Singapore**. **Non-paying: 34m property seekers/month** and 2.8m listings | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| Primary Currency | **SGD** (reporting + Singapore billing) and **MYR** (Malaysia billing via local entity into CIMB Bank). THB and VND for the sister brands. **Each market billed by its own local entity in its own currency — no multi-currency single-entity exposure** | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm); [AgentNet](https://myagentofferings.propertygurugroup.com/help-centre/welcome-to-agentnet/payments/payment-methods-2/) |
| Top 3 Markets by Revenue | **Singapore S$86.0m (57.3%)** · **Malaysia S$27.7m (18.5%)** · **Vietnam S$17.1m (11.4%)**. Then Thailand S$10.7m (7.1%), Indonesia S$2.5m (closed), Fintech & Data ~S$6m | [20-F](https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm) |
| Billing channel split (web vs app store) | **N/A — no app-store exposure.** All billing is B2B invoice/web via AgentNet, plus cheque. **The app-store trap does not apply to this account.** Channel split is better framed as **online (Adyen/Braintree/Atome) vs offline (cheque/bank transfer with sales-rep assistance)** — and the offline share is **unquantified** | [AgentNet](https://myagentofferings.propertygurugroup.com/help-centre/welcome-to-agentnet/payments/payment-methods-2/) |

**Revenue-per-audience-unit, by market** `[DERIVED: 20-F segment revenue ÷ supplied SimilarWeb audience share]`:

| Market | FY2023 revenue | Audience share | Revenue per point of audience share |
|---|---|---|---|
| Singapore | S$86.0m | 37.12% | **2.32** |
| Malaysia | S$27.7m | 47.94% | **0.58** |

**Singapore monetises ~4.0× better per user than Malaysia.** This is the direct answer to the brief's "check revenue by segment" instruction, and it **reverses** the traffic-table hypothesis that Malaysia may matter more.

---

## Overall Research Confidence

**HIGH** — unusually high for this pipeline, and high specifically on the question that decided the account.

**Strong coverage:**
- **Billing model and transaction count (§12)** — answered from an **audited SEC annual report** with verbatim quotes, the strongest source class available. This is the rare account where the decisive metric is documented by the company itself.
- **PSP stack (§3A)** — Adyen named in the 20-F *and* on a live agent help page (updated 2026-08-19); Braintree and Atome named on fetched pages. Two independent source classes agree.
- **Financials and segment split (§12)** — full FY2023 revenue by market from the 20-F.
- **Corporate status and ownership (§6)** — EQT's own release and PropertyGuru's own newsroom, both fetched, datelines quoted. **Verified from primary sources, not from memory**, as instructed.
- **Domain estate (§1)** — resolved empirically by redirect chain and WAF fingerprint, correcting two errors in the supplied notes.
- **Consumer-payment question (§7)** — closed from the 20-F's revenue-recognition notes plus a live 301 redirect.

**Limited coverage, and why:**
- **Singapore agent payment methods** — `www.agentofferings.propertyguru.com.sg` returns **403 Cloudflare challenge to every automated client, including on a nonsense-path control**, so no page on that host could be read or disproved. The PayNow row is scored **0** as a result. This is the only gap that could move the score (+3 at most).
- **Vietnam top-up frequency** — not found in two searches including Vietnamese-language terms. **The one material unknown**, and the only thing that could overturn the override.
- **Registration numbers** — ACRA/BizFile and SSM not reachable; `zaubacorp.com` and `thecompanycheck.com` are blocked in this environment.
- **Malaysia agent count** — never disclosed separately, so a per-market transaction split for Malaysia is impossible. The group figure was used instead.
- **FY2024/FY2025 actuals** — do not exist publicly. The company has filed nothing since delisting in December 2024, so all financials are FY2023 with FY2024 part-year support.

**Traffic data provenance: SUPPLIED.** SimilarWeb data supplied by Prateek on 2026-10-13 and used **verbatim, not re-researched**, per the resolution order. It gives **country shares only with no absolute visit total**, so no visit-derived volume estimate appears anywhere in this report — the transaction derivation rests entirely on the 20-F's agent counts, which is a stronger basis. Two of the supplied analyst notes were **corrected** (Rumah123 ownership; the Malaysia-matters-more hypothesis) and one was **explained** (Indonesia's decline is a 2023 business closure).

**Methodology deviation, disclosed as instructed:** the `/research` method specifies five parallel sub-agents (Phase 1 → Phase 2 → Phase 3). **The Agent/Task tool was prohibited for this run, so all three phases were executed single-threaded by one analyst.** Phase ordering was preserved — traffic and entities first, then stack/APM/news/competitors, then synthesis. Net effect: fewer total searches than the 80-search budget would allow, concentrated on the billing-unit gate as directed. **No section was skipped**, though Sections 5 and 11C returned genuine nulls and Section 8 is partial for the reasons given.

---

## Manual Research Recommendations

> **Area:** **Vietnam (Batdongsan) top-up frequency and discretionary Ad Credit frequency — THE DECIDING QUESTION**
> **Why it matters:** This is the only thing that could overturn the volume rejection. Vietnam is explicitly *"pay-as-you-go"* with agents who *"credit money into their account"*, and carried ~1.5m listings per quarter in Q2 2024. If those listings are paid **individually**, group transaction volume is two orders of magnitude higher than derived and the account becomes viable. If they are **debited from a prepaid balance** (which the "credit money into their account" wording implies), the payment event is the top-up and the derivation stands. I could not source this in two attempts.
> **Suggested manual action:** Open `batdongsan.com.vn` through a Vietnam VPN and find the agent top-up page (`nạp tiền`) — check the minimum top-up, the methods offered (VNPay / MoMo / ZaloPay / bank transfer), and whether listings debit a balance. Alternatively ask a Vietnamese agent directly. **Do this before any further work on the account.**

> **Area:** **Singapore agent payment methods, and PayNow specifically**
> **Why it matters:** Singapore is 57.3% of revenue and 47.03% of traffic. PayNow's absence is the only remaining +3 in the matrix, and I could not source it either way because the `.sg` agent help centre is WAF-blocked to automated clients.
> **Suggested manual action:** Open `https://www.agentofferings.propertyguru.com.sg/help-centre/` in a normal browser (it will pass the Cloudflare challenge interactively where tooling cannot) and read the Payments section. Confirm whether PayNow, GrabPay or GIRO appear, and whether Singapore also uses the Adyen + Braintree split.

> **Area:** **Offline vs online collection share**
> **Why it matters:** Cheque and sales-rep-assisted bank transfer are explicitly supported and endorsed (*"some agents prefer to pay by cheque, in which we still continue to support this method"*). If a large share of the ~55,000 annual payments are cheques, the *electronically processed* count is lower still — reinforcing the rejection. If online is near-universal, the picture is marginally better.
> **Suggested manual action:** A discovery question for any future conversation. Not obtainable from public sources.

> **Area:** **Entity registration numbers**
> **Why it matters:** Needed to confirm the billing entity per market before any commercial conversation, and to verify the unlabelled `200615063H`.
> **Suggested manual action:** ACRA BizFile (Singapore) for PropertyGuru Pte. Ltd. and Sendtech Pte. Ltd.; SSM e-Info (Malaysia) for PropertyGuru International (M) Sdn Bhd. Both blocked or unreachable in this environment.

> **Area:** **Whether the Sendhelper consumer flow still exists inside the portal**
> **Why it matters:** It is the only consumer payment flow the group ever had. `sendhelper.com` now 301s to `propertyguru.com.sg`, but whether home-services booking and payment still runs inside the portal is unresolved. If it were revived at scale it would be a different account.
> **Suggested manual action:** Browse `propertyguru.com.sg` for a home-services section and attempt a booking to see whether payment is collected online.

---

## Appendix: All Source URLs

**Primary filings (SEC EDGAR)**
- FY2023 Form 20-F (main document, 6.65MB — downloaded and grepped locally): https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/pgru-20231231.htm
- FY2023 20-F filing index: https://www.sec.gov/Archives/edgar/data/1873331/000095017024035071/0000950170-24-035071-index.htm
- Q2 2024 results, EX-99.1: https://www.sec.gov/Archives/edgar/data/0001873331/000095017024103090/pgru-ex99_1.htm
- All 20-F filings list (CIK 0001873331): https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001873331&type=20-F&dateb=&owner=include&count=40

**Ownership & corporate (§6)**
- EQT completes acquisition of PropertyGuru (13 Dec 2024): https://eqtgroup.com/news/eqt-completes-acquisition-of-propertyguru
- EQT Private Capital Asia to acquire PropertyGuru (16 Aug 2024): https://eqtgroup.com/news/eqt-private-capital-asia-to-acquire-propertyguru
- EQT portfolio page: https://eqtgroup.com/about/current-portfolio/propertyguru
- Leadership transition and new board (13 Jan 2025): https://www.propertygurugroup.com/newsroom/propertyguru-announces-leadership-transition-and-a-new-board/
- Group corporate site (brands, `200615063H`): https://www.propertygurugroup.com/
- Newsroom index: https://www.propertygurugroup.com/newsroom/

**Payment stack (§3, §4, §7, §8)**
- AgentNet payment methods, updated 2026-08-19 (Adyen, Braintree, CIMB, Public Bank, cheque, MY billing entity): https://myagentofferings.propertygurugroup.com/help-centre/welcome-to-agentnet/payments/payment-methods-2/
- Online Payment help article (MY): https://www.agentofferings.propertyguru.com.my/help-centre/online-payment/
- FAQ: Pay with Atome (Malaysia): https://www.agentofferings.propertyguru.com.my/help-centre/pay-with-atome-my/
- Package updates & Core+, effective 1 Nov 2025: https://www.agentofferings.propertyguru.com.my/?p=11096
- Singapore renewal windows (Early Bird / Actual Month) — **403, title and summary via search index only**: https://www.agentofferings.propertyguru.com.sg/help-centre/agent-packages/manage-your-package/renewal-am-eb/
- Touch 'n Go entitlement terms — **404 on fetch, title only**: https://myagentofferings.propertygurugroup.com/help-centre/welcome-to-agentnet/payments/terms-and-conditions-touch-n-go-renewal-early-upgrade-new-subscriber/

**Fintech / consumer-flow question (§7)**
- PropertyGuru launches mortgage marketplace PropertyGuru Finance: https://fintechnews.sg/38380/proptech/propertyguru-launches-mortgage-marketplace/
- PropertyGuru Finance ventures into home mortgage financing: https://www.asiapropertyawards.com/en/propertyguru-finance-ease-home-buying-process-home-loan-mortgages/
- PropertyGuru enters home services with Sendhelper acquisition: https://www.businesswire.com/news/home/20221013006091/en/PropertyGuru-enters-home-services-with-the-strategic-acquisition-of-Sendhelper-in-Singapore

**Competitors (§11)**
- 99 Group acquires SRX: https://vulcanpost.com/721827/99-group-acquires-srx
- Semrush competitors, propertyguru.com.sg: https://cw.semrush.com/website/propertyguru.com.sg/competitors
- Semrush competitors, propertyguru.com.my: https://www.semrush.com/website/propertyguru.com.my/competitors/
- Semrush competitors, edgeprop.my: https://www.semrush.com/website/edgeprop.my/competitors/
- Semrush competitors, 99.co: https://tr.semrush.com/website/99.co/competitors

**Internal (not web sources)**
- Supplied SimilarWeb traffic + analyst notes: `accounts/traffic/propertyguru.md`
- TAL row 805, "PropertyGuru International": `accounts/apac-tal.csv`
- Stub: `1-to-outreach/propertyguru.md`
- References: `.claude/reference/apac-payments.md`, `.claude/reference/subscription-payments.md`

**Checked and returned nothing usable**
- Payment/billing job postings at PropertyGuru — none found
- Reddit / Trustpilot / X / app stores for payment complaints — none found
- Batdongsan.com.vn top-up mechanics — not found (2 attempts, incl. Vietnamese-language terms)
- 2025/2026 PropertyGuru financing or debt facility — not found
- `propertyguru.com.sg`, `.com.my`, `ddproperty.com`, `batdongsan.com.vn`, `iproperty.com.my`, `commercialguru.com.sg`, `brickz.my`, `asiapropertyawards.com`, `propertygurugroup.com` via curl — **all 403 Cloudflare managed challenge**, confirmed non-informative against a nonsense-path control
- `propertyguru.com.th`, `propertyguru.vn`, `propertyguru.co.id` — **do not exist (DNS failure)**


## Rejection Rationale

**Volume gate fired on a derived figure.** The billing unit is one upfront annual subscription payment per agent; 55,000+ agents across the Priority Markets ÷ 12 months = **~4,600 payment events per month**, both inputs sourced to the audited FY2023 Form 20-F. That is **~11% of the 40,000/month floor**, and the method's auto-reject applies to a soundly-derived figure, not only a directly published one. There is **no consumer payment flow** to add to it — PropertyGuru Finance is referral and the financial institutions are invoiced, and Sendhelper's domain now redirects to the Singapore portal.

Secondary grounds, had the gate not fired: **5 of the 12 ICP points double-count a single Singapore/Malaysia split**, and "high traffic outside home" is substantively false for a two-market domestic operator with local acquiring in both markets. Net of that distortion the honest score is **~9/29**.

⚠️ **Reversal condition, carried deliberately:** sourced evidence that Vietnam (Batdongsan) pay-as-you-go listings are paid individually rather than debited from a prepaid balance. At ~1.5m listings/quarter that would be ~500,000 events/month and the gate would not fire. Neither the research run nor the audit could source it; both Vietnamese and Thai group domains return 403 challenge pages. That question may belong to Batdongsan as a separate account.

</details>
