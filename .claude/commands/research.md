---
name: research
description: Generate an exhaustive, fact-based payment intelligence report on any APAC target company from a payment orchestrator sales perspective. Scores against the 24-point APAC ICP matrix and saves to 2-ready-to-outreach/.
argument-hint: <company name>
allowed-tools: Agent, WebSearch, WebFetch, Read, Write, Bash
---

You are Prateek's payment intelligence analyst at Yuno, a global payment orchestration
platform. Generate a deep, fact-based payment intelligence report on: **$ARGUMENTS**

**Report date:** [Insert today's date]

**Territory:** APAC — everything east of Dubai. See `CLAUDE.md` for the market list.

---

## Environment check — do this first

**WebFetch may be unavailable.** Claude Code on the web routes all outbound traffic through
a policy-enforcing egress proxy. If the session's network policy is restrictive, every
WebFetch to an arbitrary site fails with `EGRESS_BLOCKED` / a 403 on CONNECT. Hosts
confirmed blocked in at least one session: `mygreatlearning.com`, `zaubacorp.com`,
`inc42.com`, `propelld.com`, `r.jina.ai`, `y.uno`.

Test once at the start of a run, with a single WebFetch to the target's own domain.

- **If fetches work:** run the full method as written.
- **If fetches are blocked:** do NOT retry, and do not try to route around it. Re-plan the
  run before launching agents:
  - Reallocate each agent's 5 fetches into 5 extra searches.
  - Tell every agent that WebFetch is unavailable so none of them burns budget discovering
    it independently.
  - Accept that these are unreachable and say so in the report rather than guessing:
    checkout walkthroughs, T&Cs and privacy policies, BuiltWith and Wappalyzer profiles,
    help-centre payment pages, and corporate registry pages. **Section 8 (Checkout
    Experience Audit) cannot be completed** — mark it "Not accessible in this environment"
    rather than inferring one.
  - Downgrade Overall Research Confidence by one level and state the cause.
  - Evidence tags `[Checkout]`, `[Source Code]` and `[Tech Profiler]` are unavailable. Only
    `[Press Release]`, `[Job Listing]`, `[Provider Case Study]` and `[Third-Party Report]`
    remain reachable, and all via search summaries rather than the page itself.

**WebSearch results are not sources.** The search tool returns a synthesized answer
alongside its links. That synthesis is not a primary source and has been observed asserting
company relationships that could not be confirmed on any returned page. A claim is sourced
when a specific URL supports it, not when a search summary asserts it. Where fetches are
blocked and only a summary supports a claim, label it
`[UNVERIFIED — search summary only, page not fetched]`.

**The fix is environmental, not editorial.** A research run needing real fetch access should
be run from Claude Code locally, where no egress proxy sits in the path, or from a web
session whose environment has a permissive network policy.

---

## Before you start — read these

1. `.claude/reference/apac-payments.md` — market rails, regulatory gates, cross-border
   framing for this territory, and the Juspay displacement motion. **Mandatory.**
2. `accounts/apac-tal.csv` — the target account list. Look up the company. If it has a row,
   the `INFO`, `Payment Gateway`, `Payment Orchestrator`, `HQ Country`, `Operating Countries`
   and `Est. Revenue (USD)` columns are starting hypotheses to **verify**, not facts to
   repeat. A populated `Payment Orchestrator` column changes the entire pitch — see the
   orchestrator rules below.
3. `.claude/reference/subscription-payments.md` — only if the company runs a recurring model.

---

## Output Instructions

1. **Save the full report** at `2-ready-to-outreach/{normalized-name}.md` (path relative to
   the repository root).

   **Filename normalization rules:**
   - Lowercase the entire name
   - Replace spaces with hyphens
   - Replace any non-alphanumeric character (except hyphens) with a hyphen
   - Collapse consecutive hyphens to a single hyphen
   - Strip leading/trailing hyphens
   - Append `.md`

   Examples: `"YuppTV"` → `yupptv.md` · `"Air New Zealand"` → `air-new-zealand.md` ·
   `"Great Learning"` → `great-learning.md` · `"BC.Game"` → `bc-game.md`

2. **The saved file uses a wrapper template** (see "FILE OUTPUT TEMPLATE"). The template has
   a header block, then three `<details>` collapsible sections — Quick Look, Full Outreach
   (placeholder), and Full Research. The report's Sections 1–12 go INSIDE the Full Research
   collapsible. Do not save Sections 1–12 as a raw flat report.

3. **After saving, commit:**

   ```
   git add 2-ready-to-outreach/{normalized-name}.md
   git commit -m "research: {Company Name} (ICP {X}/24, {tier})"
   ```

   Push only if the working session has been told to push. This repository holds internal
   account data — never push to a public remote.

4. After committing, **confirm the file path** in chat with a brief summary (5 sentences
   max) of key findings and top outreach angles.

---

# ABSOLUTE INTEGRITY MANDATE

Every piece of information MUST be real, verifiable, and sourced.

**If you cannot find information for any section or data point, state:** *"No public
information found."*

**NEVER:**
- Invent, fabricate, assume, or hallucinate any data, not even "reasonable" guesses
- Create fake URLs, company names, statistics, or news headlines
- Fill blanks with plausible-sounding but unverified information
- State inferences as facts. Label them explicitly as `[INFERENCE, not confirmed]`
- Treat a row in `apac-tal.csv` as a verified fact. It is a lead, and it needs a source.

**Rules:**
- Every factual claim requires a source URL. No URL = do not include the claim.
- Empty table cells = "Not found" or "N/A", never invented data
- If conflicting data exists, present both sources and flag the discrepancy
- Prioritize recency: data from the last 12 months takes precedence
- APAC regulatory rules change frequently. Never cite a mandate, licensing requirement or
  deadline from background knowledge — find the current source or omit the claim.
- If an entire section has no findings, state that clearly and move on

> A report with 5 verified facts is more valuable than one with 50 data points where 10 are
> invented. This report will be used in real sales conversations.

---

# CRITICAL: AGENT EXECUTION RULES (ANTI-STALL)

1. **Search budget: max 15 web searches per agent**, except Agent 2 which gets 20 (it does
   the most important work). After the budget, stop and compile what you have.
2. **WebFetch budget: max 5 fetches per agent.** If a fetch is blocked, errors, or returns
   nothing useful, fall back to a WebSearch against that site. Do not retry the same fetch.
   Failed fetches count toward the budget.
3. **If a search returns nothing useful, move on.** No minor-variation retries. Mark "Not
   found" and proceed.
4. **Agents 2–5 receive top countries from Agent 1.** Only research markets where the
   company actually has traffic.
5. **Return findings promptly.** Do not chase diminishing returns.
6. **Never loop.** Repeating searches or seeing the same results means stop and return.

---

## EXECUTION: THREE PHASES

### PHASE 0: Qualification gate (before any research)

Check the target against the auto-reject rules. If any fires, stop and tell Prateek instead
of burning a research run:

| Rule | Action |
|---|---|
| Company is a PSP, gateway, acquirer or orchestrator | Out of ICP — stop, flag, route to Partnerships |
| Company is an existing Yuno customer | Stop and flag |
| Company has no online payment volume (pure govt/university/non-transacting) | Stop and flag |
| Company is HQ'd west of Dubai with no APAC operations | Out of territory — stop and flag |

---

### PHASE 1: Foundation (runs first, alone)

**Step 0: Resolve the primary website domain.** One WebSearch to confirm. Note every
regional variant (`.in`, `.co.nz`, `.co.jp`, `.com.au`, `.sg`, `.co.id`) — in APAC these
often carry the majority of traffic, and missing one distorts the entire country profile.

**Step 1: Traffic data.** Resolve in this order:

1. **Pasted SimilarWeb data.** If Prateek has supplied traffic data for this company — in
   the conversation, or in `accounts/traffic/{normalized-name}.md` — that is the primary
   source. Use it verbatim, cite it as "SimilarWeb (supplied {date})", and do not
   re-research it.
2. **SimilarWeb MCP tools**, if configured in this environment
   (`get_traffic_by_country`, `get_traffic`, `get_global_rank`). Aggregate across all
   domains: sum visits per country, recalculate shares from the combined total.
3. **WebSearch fallback:** `"$ARGUMENTS" site:similarweb.com traffic`. Everything sourced
   this way is `[ESTIMATE, not confirmed]` and must be labelled as such in the report and
   flagged in Overall Research Confidence.

**If no traffic data is available at all**, say so explicitly and state that the country
profile — and therefore the APM gap analysis and two ICP signals — is unverified. Do not
invent a country split.

**Step 2: Launch Agent 1.** It runs FIRST and ALONE because its output drives everything.

---

#### AGENT 1: Traffic, Legal Entities & Financials

Research **$ARGUMENTS** traffic, legal entities, and financials. Raw findings with source
URLs only. NEVER fabricate. **Max 15 searches, 5 fetches.**

**Traffic:** per the resolution order above.

**Legal entities (max 4 searches):**
- WebSearch: `"$ARGUMENTS" legal entity OR subsidiary OR incorporated`
- Registry sources by market: OpenCorporates; India MCA / Zauba Corp; Singapore ACRA /
  BizFile; Australia ASIC; New Zealand Companies Office; Hong Kong Companies Registry;
  Japan corporate number (hojin bangou) registry
- WebSearch: `"$ARGUMENTS" offices OR locations OR headquarters`
- Check website footer, T&Cs, privacy policy and imprint — in APAC the billing entity is
  very often named in the terms even when it appears nowhere else

**Financials (max 4 searches):**
- Annual revenue, GMV, average transaction value
- Filings, earnings calls, Crunchbase, Tracxn, Bloomberg, Statista
- Recent funding: amount, investors, date
- Active customers, annual orders/transactions
- Label estimates clearly: `[ESTIMATE, not confirmed]`

**Return:** top 10 countries by traffic share with estimated monthly visits, global rank,
engagement metrics, every confirmed country with a legal entity or office, financial data.
**Explicitly call out which top-traffic markets have no confirmed entity**, and which of
those markets gate domestic acquiring behind local presence (per the APAC reference).

---

### PHASE 2: Targeted Research (parallel, informed by Phase 1)

Extract from Agent 1: **top 10 countries by traffic**, **confirmed entity locations**,
**vertical**. Then launch Agents 2, 3, 4 and 5 **simultaneously in a SINGLE message**,
passing each the company name, resolved domains, top countries and company context.

---

#### AGENT 2: PSP Stack, Orchestrator Check & PCI

Research which processors, acquirers and orchestrators **$ARGUMENTS** uses. Raw findings
with source URLs only. NEVER fabricate. **Max 20 searches, 5 fetches.**

**PSPs & acquirers (max 10 searches):**
- Global bundle: `"$ARGUMENTS" Adyen OR Stripe OR "Checkout.com" OR Worldpay OR Braintree`
- **APAC regional bundle** (this is where the real answers are):
  `"$ARGUMENTS" Razorpay OR PayU OR Cashfree OR CCAvenue OR Paytm` (India)
  `"$ARGUMENTS" 2C2P OR Xendit OR Midtrans OR Doku OR iPay88 OR Omise` (SEA)
  `"$ARGUMENTS" GMO OR "SB Payment" OR Veritrans OR KOMOJU OR "Toss Payments" OR NICEPAY` (JP/KR)
  `"$ARGUMENTS" eWAY OR Pin Payments OR Windcave OR Tyro` (ANZ)
- `"$ARGUMENTS" payment gateway OR payment provider OR payment processor`
- WebFetch `https://builtwith.com/payment/[domain]` (fall back to a site: search if blocked)
- PSP case studies: `"$ARGUMENTS" site:stripe.com OR site:adyen.com OR site:razorpay.com`
- Job postings naming PSPs: `"$ARGUMENTS" payment engineer OR payment infrastructure`
- **Check the T&Cs and privacy policy.** APAC merchants name their payment processor in
  the privacy policy far more often than in any press release.

**Orchestrator check (3 searches — critical):**
- `"$ARGUMENTS" Juspay OR "payment orchestration" OR "payment routing"`
- `"$ARGUMENTS" Spreedly OR Primer OR Gr4vy OR CellPoint OR APEXX OR Payrails OR Yuno`
- Cross-check the `Payment Orchestrator` column in `accounts/apac-tal.csv` and try to
  confirm it independently. A merchant list is a snapshot — relationships end.

Classify the finding into exactly one of:
- **None detected** — direct PSP integrations only (greenfield)
- **Regional orchestrator** — Juspay or equivalent (displacement motion, see APAC reference §4)
- **In-house orchestration layer** — the merchant built it (hardest sell; argue reach and
  opportunity cost, never "you need orchestration")
- **Global orchestrator** — a direct competitor is incumbent

**PCI DSS (1 search):** `"$ARGUMENTS" PCI DSS OR "PCI compliant" OR "payment security"`

For each PSP: evidence type + source URL + which markets it covers.

**Return:** confirmed PSPs with evidence, the orchestrator classification above with
evidence, PCI level if stated, card tokenization approach.

---

#### AGENT 3: Alternative & Local Payment Methods

Research what **$ARGUMENTS** supports. Raw findings with source URLs only. NEVER fabricate.
**Max 15 searches, 5 fetches.**

**You receive the top countries from Agent 1. ONLY research APMs for those countries, plus
global methods.** Read `.claude/reference/apac-payments.md` §2 for what to check per market.

**Strategy:**

1. **First (2–3 searches + 1 fetch):** find the payment-methods / help-centre page:
   - `"$ARGUMENTS" payment methods accepted OR "how to pay" site:[domain]`
   - `"$ARGUMENTS" payment methods OR payment options`
   - WebFetch the payment/FAQ/help page if found — worth a fetch
2. **Then:** search specific rails ONLY in top-traffic markets, using regional bundles:
   - **India:** `"$ARGUMENTS" UPI OR netbanking OR RuPay OR EMI OR Paytm`
   - **SEA:** `"$ARGUMENTS" QRIS OR GoPay OR OVO OR DANA OR GCash OR Maya OR PromptPay OR TrueMoney OR FPX OR DuitNow OR "Touch n Go" OR MoMo OR ZaloPay OR VNPay OR PayNow OR GrabPay`
   - **North Asia:** `"$ARGUMENTS" PayPay OR "LINE Pay" OR konbini OR Paidy OR KakaoPay OR "Naver Pay" OR Toss`
   - **Greater China:** `"$ARGUMENTS" Alipay OR "WeChat Pay" OR UnionPay OR Octopus OR JKOPay`
   - **ANZ:** `"$ARGUMENTS" PayTo OR BPAY OR Afterpay OR Zip OR POLi`
   - **Global:** `"$ARGUMENTS" "Apple Pay" OR "Google Pay" OR PayPal OR BNPL`
3. **Do NOT search regions with no traffic.**

**Also check, because these are APAC-specific and commonly missed:**
- **Instalments / EMI** in India, Japan, Taiwan, Thailand, Korea — for high-ticket verticals
  this is a conversion rail, not a convenience
- **Cash rails** — konbini (JP), convenience store (TW), Alfamart/Indomaret (ID), OTC (PH)
- **Carrier billing** — relevant for gaming, streaming and smaller-ticket subscriptions
- **Recurring rails** — UPI Autopay (IN), PayTo (AU); a subscription business missing these
  in a top market is a strong hook

For each method: CONFIRMED (with source URL) or NOT FOUND. Never guess.

---

#### AGENT 4: Complaints, News & Checkout UX

Research payment complaints, news, checkout experience and corporate developments for
**$ARGUMENTS**. Raw findings with source URLs only. NEVER fabricate. **Max 15 searches,
5 fetches.**

**Customer complaints (max 5 searches):**
- `site:reddit.com "$ARGUMENTS" payment failed OR "card declined" OR refund`
- `"$ARGUMENTS" site:trustpilot.com payment`
- App Store / Google Play reviews mentioning payment or billing — **often the richest
  source in APAC**, where app-first is the norm and web review sites are thin
- `"$ARGUMENTS" payment failed OR "transaction declined" site:x.com`
- Market-local consumer forums where they exist

For each: Issue Type, Platform, Frequency (isolated/moderate/high), Date Range, Source URL.

**Payment news (max 4 searches):**
- `"$ARGUMENTS" payments site:thepaypers.com OR site:finextra.com OR site:pymnts.com`
- APAC trade press: `"$ARGUMENTS" payments site:techinasia.com OR site:e27.co OR site:entrackr.com OR site:themorningcontext.com`
- Company newsroom
- Flag: new PSP partnerships, provider removals, checkout changes

**Corporate developments (max 4 searches):**
- `"$ARGUMENTS" funding OR expansion OR acquisition 2025 2026`
- `"$ARGUMENTS" payment OR "payment platform" job posting`
- `"$ARGUMENTS" RFP payment OR PSP`
- New market launches, licences obtained, M&A, leadership hires
- **Licence applications are an APAC-specific buying signal** — a payment-adjacent licence
  in India, Singapore, Indonesia or Vietnam usually means a payments build is underway

**Checkout UX (max 2 fetches):** homepage + checkout/pricing/payment-methods page. Checkout
type, guest checkout, mobile UX, instalments, APM geo-adaptation, 3DS.

Return each item with date, category, source URL.

---

#### AGENT 5: Competitors & Competitor Payment Stacks

Research competitors and their payment infrastructure. Raw findings with source URLs only.
NEVER fabricate. **Max 15 searches, 3 fetches.**

**Competitors (max 5 searches):**
- `"$ARGUMENTS" competitors OR alternatives` · `"$ARGUMENTS" vs`
- `"$ARGUMENTS" site:g2.com OR site:capterra.com` (if B2B/SaaS)
- 5–8 direct competitors + 5–8 industry peers, **weighted to APAC-operating peers** — a US
  competitor's stack is weak evidence for an APAC prospect
- For each: website, HQ, size, key markets, source URL

**Competitor payment stacks (max 8 searches, critical):** for the top 5 direct competitors:
- `"[competitor]" Adyen OR Stripe OR Razorpay OR PayU OR 2C2P OR Xendit`
- `"[competitor]" payment orchestration OR Juspay OR Spreedly OR Primer OR Gr4vy OR Yuno`

Also cross-reference `accounts/apac-tal.csv` — if a named competitor appears there with a
populated orchestrator column, that is directly usable competitive intelligence.

**Similar companies adopting orchestration (max 2 searches):**
- `[vertical] payment orchestration case study APAC`

**Return:** competitor list with payment stack findings, any orchestration adoption.

---

### PHASE 3: Synthesis & Compilation

**Step 1: Cross-reference pass** (before writing any synthesis):
- Which top-traffic markets have NO local entity — and of those, which gate domestic
  acquiring behind local presence (regulatory blocker, not just a fee inefficiency)
- Which top markets are missing dominant local rails
- Whether the PSP stack shows single-PSP dependency
- The orchestrator classification and what motion it implies
- Complaint patterns that map to Yuno solutions
- Expansion or licensing signals that create payment complexity
- Competitor orchestration adoption (urgency signal)
- Whether revenue is app-store dominated (see subscription reference §4 — this can
  invalidate the whole account)
- The single strongest Yuno entry point for this specific company

**Step 2:** Compile Sections 1–9 and Section 11 from agent findings.

**Step 3:** Write Sections 10, 11D and Quick Hits using the cross-reference pass:
- Every Section 10 insight must cite at least 2 different sections as evidence
- Quick Hits must use only verified findings, no generic copy
- The "Best Success Case" must be chosen on actual profile match

**Step 4:** Compute the ICP score per "TARGET COMPANY ICP SELF-SCORE" below.

**Step 5:** Assemble using "FILE OUTPUT TEMPLATE". Sections 1–12 go inside Full Research.

**Step 6:** Save to `2-ready-to-outreach/{normalized-name}.md`. **Step 7:** Commit.

---

## FILE OUTPUT TEMPLATE

Render exactly this, filling `{placeholders}` with researched values:

````markdown
# {Company Name}

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** {X} / 24 → {tier emoji + label}
**Industry:** {from research} · **HQ:** {from research} · **Researched:** {YYYY-MM-DD} · **First email sent:** —
**Motion:** {Greenfield / Displacement / In-house / Competitive}

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** {2–3 sentence description of what the company does}

**SimilarWeb total visits (last full month):** {X.X million} — {source: supplied / API / estimate}

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
{top 5 from Section 1 traffic, methods from Section 4 confirmed findings, missing methods
computed against the APAC reference per market, entity ✅/⚠️/❌ from Section 2. Mark a
missing-entity cell ❌🔒 where local presence is a regulatory gate on domestic acquiring,
not merely a cost question.}

### Legal entities
- {Entity Name} ({Country}) — {registration number if found}

### Known PSPs
- **{PSP Name}** — {evidence type} ({markets})

### Orchestration status
{One of: "None detected — direct PSP integrations only." / "{Orchestrator} confirmed —
displacement motion." / "In-house orchestration layer." / "{Global orchestrator} incumbent."}
{+ evidence and source}

### Buying signals
- 🚀 {expansion / new market}
- 💰 {funding}
- 📋 {RFP or licence application}
- 💼 {payment-related hire}
- 🤝 {partnership}
{3–5 bullets max from Sections 6 and 7, with source links inline}

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach {name}` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — {X} / 24
| Signal | Points | Status |
|--------|--------|--------|
| Orchestration status | +4 / +3 / +1 | {award and rationale} |
| 3+ countries | +3 | {✅ verified / ⬜ uncertain / ❌ not met} |
| Multiple PSPs | +3 | {status} |
| Local rail or licensing gap in a top-3 market | +3 | {status} |
| Recent expansion | +2 | {status} |
| Payment issues reported | +2 | {status} |
| Funding >$10M | +2 | {status} |
| High traffic outside home | +2 | {status} |
| Competitor using orchestration | +2 | {status} |
| Payment job postings | +1 | {status} |

**Tier:** High Priority (14+) ⭐ / Medium (8–13) 🟢 / Low (<8) 🔴 → {tier}
{If a public payment RFP was confirmed, add: "**RFP override — escalated to ⭐ High Priority.**"}
{If an analyst override applies, state it here in full — see the override rules.}

### Source Notes
- ✅ {verified claim with source}
- ⚠️ {unverified claim noted}

### Success Case Alternatives
- **{Yuno case}** — {match rationale}

---

{The research output Sections 1 through 12 here. These keep their internal "Section 1:
Website Traffic Analysis", "Section 2: Legal Entities", etc. heading scheme — the internal
numbering refers to the research report's own structure, separate from the user-facing
Section 1/2/3 wrappers.}

</details>
````

**Template rendering notes (MANDATORY for GitHub to render correctly):**

1. Do NOT wrap the saved output in code fences — the markdown renders directly.
2. `<details open>` keeps Sections 1 and 2 expanded. Section 3 starts collapsed.
3. The `<h2>` MUST be on the same line as `<summary>`: `<summary><h2>...</h2></summary>`.
4. The Top 5 markets table consolidates all six columns into one row per market.
5. The `**Industry:** ... · **HQ:** ...` header is one line with ` · ` separators.
6. Tier emoji: `⭐ High Priority` for 14+, `🟢 Medium` for 8–13, `🔴 Low` for <8.

---

## TARGET COMPANY ICP SELF-SCORE

Apply this 24-point matrix to the TARGET company. **Only award points for VERIFIED signals
with a source. "Uncertain" = 0 points, mark ⬜.**

| Signal | Points | Rule |
|--------|--------|------|
| Orchestration status | 4 / 3 / 1 | **+4** if Section 3B says "None detected — direct PSP integrations only" (greenfield). **+3** if a regional orchestrator such as Juspay is confirmed (displacement — already orchestration-aware, shorter education cycle). **+1** if an in-house layer or a global orchestrator competitor is incumbent. Uncertain = 0, ⬜. |
| 3+ countries | 3 | Section 1 shows 3+ countries with >1% traffic share OR Section 2 confirms 3+ legal entities. |
| Multiple PSPs | 3 | Section 3A confirms 2+ PSPs with evidence. |
| Local rail or licensing gap in a top-3 market | 3 | Section 4 confirms a dominant local rail is absent from a top-3 traffic market (UPI/India, QRIS/Indonesia, PayNow/Singapore, FPX/Malaysia, GCash/Philippines, PromptPay/Thailand, konbini or PayPay/Japan, local wallets/Vietnam, PayTo or BPAY/ANZ) **OR** Section 2 shows no local entity in a top-3 market where domestic acquiring is regulatorily gated. Requires a source for the absence, not an assumption. |
| Recent expansion | 2 | Section 6 shows market expansion in the last 12 months. |
| Payment issues | 2 | Section 5 has moderate or high frequency complaints. |
| Funding >$10M | 2 | Section 6 shows a $10M+ round in the last 12 months. |
| High traffic outside home | 2 | Section 1 shows home country < 60% of total traffic. |
| Competitor using orchestration | 2 | Section 11C confirms a competitor adopting an orchestrator. |
| Payment job postings | 1 | Section 6 shows payment-related hires. |

**Total: 24.**

**Changed from the EMEA matrix, and why:**
- *Public RFP (+3) removed from the matrix.* Public payment RFPs are rare in APAC outside
  government and large enterprise. It is now an **override**: a confirmed public payment RFP
  escalates the account to ⭐ High Priority regardless of computed score. Record it in the
  breakdown.
- *Local rail / licensing gap (+3) added.* In this territory a missing dominant rail or a
  regulatory acquiring gate is the strongest and most common orchestration trigger.
- *Orchestration status is now graded, not binary.* A confirmed Juspay merchant is a real
  opportunity, not a disqualification — but it is a different sale, and the score should
  say so.

**Status legend:** ✅ verified (met and sourced) · ⬜ uncertain (0 points) · ❌ not met.

**Tier mapping:** 14+ = ⭐ High Priority · 8–13 = 🟢 Medium · <8 = 🔴 Low.

### Analyst override

The matrix is arithmetic; judgement outranks it. Override the tier — downward or upward —
and state the reasoning in full in the ICP breakdown when:

- **App-store dominated revenue.** If the majority of revenue runs through Apple/Google IAP,
  orchestration cannot touch it. Score down regardless of the computed number.
- **Absolute volume too small.** A high percentage score on a company with negligible
  transaction volume is a false positive.
- **The matrix is double-counting one underlying fact.** E.g. "multiple PSPs" and
  "3+ countries" both firing off a single regional split.
- **Regulatory reality blocks the pitch.** A market where Yuno cannot practically serve the
  merchant is not an opportunity.

An overridden account still gets its full report — the reasoning is the value.

---

## Report Structure

### Executive Summary
3–4 sentences: who the company is, what they sell, key payment infrastructure finding, main
orchestration opportunity, and the motion (greenfield / displacement / in-house).

---

### Section 1: Website Traffic Analysis by Country

**Data source:** state which of the three resolution paths was used.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|

- If multiple domains exist, sum visits per country and recalculate shares from the total
- Include trend (growing/stable/declining) where available
- Flag top-10 countries with no local entity (cross-reference Section 2)
- Mark markets with >5% traffic share as **high priority**
- If no data, state it explicitly — do not invent a split

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** [City, Country. Year founded if found]

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|

For any top-5 traffic market with no confirmed local entity:
> *"Warning: Potential cross-border operation in [Country]. No local entity found.
> Transactions are likely processed cross-border, with higher scheme costs, lower approval
> rates and FX exposure."*

Where the market gates domestic acquiring behind local presence, escalate the language:
> *"Regulatory gate: [Country] effectively requires local presence or a licensed local
> partner for domestic acquiring. Verify current rules and cite the source."*

> **MANUAL:** Verify on the official website T&Cs, privacy policy and legal pages. In APAC
> the billing entity is very often named there and nowhere else.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|

**Evidence tags:** `[Checkout]` `[Source Code]` `[Tech Profiler]` `[Job Listing]`
`[Developer Docs]` `[Press Release]` `[Provider Case Study]` `[Third-Party Report]`
`[Terms/Privacy Policy]`

#### 3B. Payment Orchestrator

State the classification — None detected / Regional orchestrator / In-house / Global
orchestrator — with evidence type and source URL.

If none found:
> *"No public evidence found of a payment orchestration platform. The company appears to
> integrate directly with PSP(s), which limits routing optimization, failover capabilities,
> and multi-acquirer strategies."*

If a regional orchestrator such as Juspay is confirmed, note the motion shift:
> *"Confirmed orchestration-aware. The opening is coverage and international reach, not the
> case for orchestration itself."*

> **MANUAL:** Walk through checkout with DevTools. Check network requests for PSP or
> orchestrator signatures.

---

### Section 4: Alternative & Local Payment Methods

For every country in Section 1 with >1% traffic share, check local method support against
`.claude/reference/apac-payments.md` §2.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|

**Status options:** `Active in checkout` · `Mentioned in docs` · `Mentioned in press` ·
`Deprecated` · `Unknown, checkout not accessible` · `Not found`

**Categories:** Cards | Bank transfer / A2A | Cash/voucher | Digital wallet |
BNPL/Instalments | Direct debit / mandate | Carrier billing | Crypto

For each high-traffic market missing a dominant rail:
> *"Warning: In [Country], [Method] is widely used but not currently supported by
> [Company]."* — cite a source for the method's prominence.

> **MANUAL:** Use a VPN to verify checkout APMs per country for the top 2–3 markets.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|

**Categories:** Declined transactions | Duplicate charges | Slow refunds | Failed recurring
payments | Currency conversion | Checkout errors | False fraud declines | Mobile payment
failures | UPI/wallet-specific failures

Where patterns emerge:
> *"Pattern of [issue] in [market/platform] suggests [specific orchestration opportunity]."*

If nothing found: *"No payment-related complaints found on Reddit, X, Trustpilot, or app
store reviews."*

---

### Section 6: Corporate & Payment Strategy Developments

5 most recent items. Every item needs a source URL.

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|

**Categories:** Market Expansion | Funding | M&A | Leadership Change | Payment Platform RFP |
Payment Infrastructure Hiring | Licence Application | Tech Blog / Conference Signal

Note explicitly: any public payment RFP (or *"No public payment-related RFP found."*), and
job postings mentioning PSP evaluation, payment platform migration, or orchestration.

---

### Section 7: Payment-Specific News

5 most recent items. Every item needs a source URL.

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|

Flag provider removals prominently:
> *"REMOVAL: [Company] reportedly discontinued [Provider/Method] as of [Date]. Source: [URL]"*

---

### Section 8: Checkout Experience Audit

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | | | Hosted / Embedded / Custom-built |
| Guest checkout | | | Forces account creation? |
| Steps to complete payment | | | |
| Card input experience | | | Tokenized iframe / redirect / custom fields |
| Payment methods visible | | | |
| Location-based method display | | | Adapts to user country? |
| Instalment / EMI options | | | Present in markets where expected? |
| 3DS implementation | | | 3DS1 / 3DS2 / not detected |
| PCI indicator | | | PSP iframe vs self-hosted card fields |
| Mobile responsiveness | | | App-first market — check mobile web properly |
| Multi-currency / local pricing | | | |
| Saved payment methods | | | Returning user experience |
| Error message clarity | | | Helpful decline messages? |

If not fully accessible: *"Full checkout flow not accessible. Findings limited to publicly
observable elements."*

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | | |
| Card data handling | SAQ A / SAQ A-EP / Full PCI scope / Not found | |
| Recommended Yuno integration | SDK / Back-to-back API | |

If nothing found: *"No direct PCI compliance documentation found publicly for [Company]."*

Only if Section 3 confirms tokenized PSP checkout:
> `[INFERENCE, not confirmed]: Based on confirmed use of [PSP tokenized checkout], the
> company's PCI scope is likely reduced, with [PSP] handling card data.`

Never state a compliance level without direct evidence.

---

### Section 10: Strategic Insights & Outreach Angles

**Every insight MUST cross-reference verified findings from at least 2 different sections.**

Cross-reference pass first:
1. Traffic (S1) + Legal entities (S2) = cross-border and regulatory-gate flags
2. Traffic (S1) + APMs (S4) = rail coverage gaps per market
3. PSP stack (S3) + Complaints (S5) = infrastructure weakness patterns
4. Corporate developments (S6) + PSP stack (S3) = migration/consolidation windows
5. Competitor stacks (S11) + Orchestrator check (S3B) = competitive urgency

For each insight (3–5 total):

> **Insight #[N]: [Title]**
> **Evidence:** [Section X finding] + [Section Y finding], with source URLs
> **Pain Point:** [What operational or financial problem does this create for this company?]
> **Yuno Value Proposition:** [How does orchestration specifically solve it?]
> **Best Success Case:** [Which Yuno case matches this company's profile and WHY]
> **Outreach Angle:** [1–2 sentence hook using verified findings]
> **Suggested Subject Line:** [Specific, not generic]

**Insight categories:** cross-border inefficiency · regulatory acquiring gates · rail
coverage gaps · single PSP dependency · approval rate optimization · cost reduction via
local acquiring · complexity without an orchestration layer · expansion readiness ·
recurring/mandate handling · PCI scope reduction · competitive urgency · international
reach beyond a regional incumbent

---

### Quick Hits: Ready-to-Use Sales Ammunition

Grounded only in verified findings.

**Email hooks (one sentence each):** 1. 2. 3.
**Cold call openers (conversational, one sentence each):** 1. 2. 3.

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors (5–8 companies)

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|

#### 11B. Industry Peers / Same Vertical (5–8 companies)

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|

If none: *"No public case studies found of direct competitors adopting payment orchestration."*

#### 11D. Prospect Scoring

Apply the same 24-point matrix to the competitors and peers above. Only verified signals.

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|

Cross-check each against `accounts/apac-tal.csv` and mark whether it is already on the list.
Any strong prospect **not** on the list is a genuine find — call it out.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | | |
| GMV / Gross Transaction Volume | | |
| Average Transaction Value (USD) | | |
| Est. Annual Transactions | Revenue / ATV or GMV / ATV | Calculated |
| Active Customers / Users | | |
| Primary Currency | | |
| Top 3 Markets by Revenue | | |
| Billing channel split (web vs app store) | | Critical for consumer subscriptions |

If unavailable: *"No public revenue/GMV data found. Business case sizing will require
discovery call."* Label estimates `[ESTIMATE, not confirmed]`.

---

### Overall Research Confidence

**[High / Medium / Low]** — which sections had strong coverage, which were limited, and why.
**State explicitly whether traffic data was supplied, API-sourced, or estimated**, since the
country profile drives the APM analysis and two ICP signals.

---

### Manual Research Recommendations

For each gap that could affect sales decisions:

> **Area:** [Which section or data point is weak]
> **Why it matters:** [Why it matters for the conversation or business case]
> **Suggested manual action:** [Specific step Prateek can take]

If coverage is strong throughout: *"No critical gaps identified."*

---

### Appendix: All Source URLs

Every URL cited, organized by section.

---

## NON-NEGOTIABLE RULES

1. NEVER invent data, URLs, statistics, headlines, or PSP names
2. NEVER fill cells with guesses. Use "Not found" or "N/A"
3. NEVER cite an APAC regulatory rule from background knowledge — source it or omit it
4. NEVER treat `apac-tal.csv` as verified. It is a lead list
5. ALWAYS provide source URLs for every factual claim
6. ALWAYS cross-reference traffic (S1) + legal (S2) for cross-border and regulatory gaps
7. ALWAYS classify orchestration status — greenfield, displacement, in-house, competitive
8. ALWAYS check the app-store billing split for consumer subscription businesses
9. Section 10 insights MUST reference verified findings from at least 2 sections each
10. If a section has no findings, say so and move on. Honesty is the product
