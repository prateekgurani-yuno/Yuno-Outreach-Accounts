# StashAway

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 12 / 29 → 🟢 Medium (computed) · **analyst override DOWN → 🔴 Low Priority**
**Industry:** Digital wealth management / robo-advisory (Investment Platforms) · **HQ:** Singapore · **Researched:** 2026-10-13 · **First email sent:** —
**Motion:** In-house — per-market bank-rail collections layer assembled from point vendors

---

---

> ## 🔍 ANALYST AUDIT — Prateek, 2026-10-13
>
> I verified the load-bearing claims against live sources and resolved the domain set myself **before** reading the report. **The score and the override both stand: 12/29 computed, overridden DOWN to 🔴 Low Priority.** No row changed. The reasoning below is why I am confident enough to act on a *negative* verdict, which is the harder call.
>
> ### ✅ THE GATE IS CONFIRMED, ON THE STRONGEST EVIDENCE TYPE AVAILABLE
> The decisive claim is "no cards in any market". An *absence* of card mentions would be weak — but what their own help centre actually carries is an **affirmative exclusion**. Verified verbatim by me on the live Hong Kong deposit article (HTTP 200, 104,142 b, distinct from my 117,665-byte nonsense-path control):
>
> > *"You can make deposits in either HKD or USD. **We accept deposits from all licensed banks in Hong Kong.** You can refer to a list of banks here [links to the HKMA's own `list_of_lb.xls`]. **If you make a deposit from other non-bank financial institutions, we may reject the deposit and return the funds to the sender.** Please note that acceptance of your funds will be subject to our Anti-Money Laundering (AML) checks."*
>
> That is a positive statement that money must arrive **from a licensed bank**, with a stated right to reject and return anything else. It is not an inference from silence. The same article documents the flow as *"Manage Deposits" → "Put Money in" → "One-time" or "Monthly" Deposit plan → transfer method → transfer instructions* — i.e. **bank transfer instructions, with a monthly plan as the recurring mechanism.** On that page `credit card`, `debit card`, `visa` and `mastercard` all return **0**, and the single `card` hit is `twitter:card` meta, correctly not counted.
>
> ### ⭐ THE RUN'S BEST METHODOLOGICAL MOVE, AND I WANT IT ON RECORD
> It **proved a false negative against itself** — the Malaysia help centre returned **0 hits for FPX while FPX is demonstrably live** via HSBC Omni Collect and Acme — and then **applied that disconfirming evidence to its own conclusions**, capping every "rail absent" reading at *"not documented", never "confirmed absent", including Hong Kong*. It consequently **scored the local-rail-gap row 0 instead of +3**, declining three points it could easily have taken. That is exactly the discipline this repo needs, and it is why the remaining conclusions are trustworthy: the one claim it *did* assert hard is the one backed by an affirmative exclusion rather than a zero.
>
> ### ✅ Also confirmed first-hand (before the run reported it)
> - **`stashaway.com` → 302 → `www.stashaway.sg`.** Not a separate global site; the TAL's `WEBSITE` cell is misleading.
> - The five live properties are **`.sg` / `.my` / `.hk` / `.ae` / `.co.th`**, matching SimilarWeb's "+4" exactly. **Malaysia is `stashaway.my`, not `.com.my`**, which does not resolve.
> - **`stashaway.ae` returns 200**, so the UAE's ↓85.69% is not a dead domain.
> - All five run on **Vercel** and **none serves a CSP**, so no asset map exists for this account.
> - ⚠️ **`/help-center/deposits` and `/help-centre` are soft-404s** — both return a byte-identical 117,665 to my nonsense control. Only `/help-center` is real. Anyone re-checking this account should use a control.
>
> ### 📌 Why the DOWN override is right, in one line
> **Yuno orchestrates card and APM pay-ins. StashAway has none, by design, in every market, and says so in writing.** The management fee is deducted from assets rather than collected over a rail. The same pattern holds at Syfe, Endowus, Moomoo and Tiger Brokers, so there is no competitive wedge either. A 🟢 Medium tier here would send a real SDR into a conversation with no product fit.
>
> ### ⚠️ What remains unverified, and what would reverse this
> - **Monthly transaction count is ASSUMED**, not sourced or derived — StashAway discloses no AUM, client count or inflow figures. It is the single largest row in the matrix (+3) and the least evidenced. Per the disclosure rule an assumption can never fire the under-40k rejection, so no Phase 0 reject was triggered.
> - **The UAE collapse has no established cause.** Four were ruled out (domain alive, DFSA registration live, new UAE products shipped, retail-pivot hypothesis tested and rejected). Most likely a content-marketing decline or a SimilarWeb artefact. Either way **the UAE is Gulf → EMEA, so that volume is not Prateek's**.
> - **Indonesia ↑503% has no established cause** — no entity, no licence, no product, and `.co.id`/`.id` do not resolve.
> - **Reversal condition, stated plainly:** evidence of **cards in any flow**, or a **sourced deposit count above 100k/month**. Either would justify re-opening this account.
>
> ### ✔️ Safety checks passed
> No credential value anywhere. No booking link. Structure 3/3 collapsibles. ICP re-added independently: **3+1+3+3+0+0+0+0+2+0+0 = 12 across 11 rows.** ✅
>
> ### ➡️ Recommended next step — Prateek's call, not actioned
> Run **`/mark_not_icp StashAway`** to move this to `not-icp/` with the rejection rationale. I have **not** done it: the computed score is 12, which is above the automatic threshold, so the move rests on the override and that is a judgement call to confirm rather than assume.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** StashAway is a Singapore-headquartered licensed digital wealth manager (robo-advisor) that builds and manages ETF and multi-asset portfolios for retail, accredited and high-net-worth clients. It operates five licensed entities across Singapore, Malaysia, Hong Kong, Thailand and the UAE (DIFC). Revenue is annual management fees of 0.2%–0.8% p.a. charged against assets under management — **not** per-transaction merchant revenue.

**SimilarWeb total visits (last full month):** **Not found.** The supplied dataset (`accounts/traffic/stashaway.md`) provides country *shares*, changes and engagement metrics only — no absolute visit total. Source: SimilarWeb (supplied 2026-10-13), Jul–Sep 2026, "include all country domains" ON.

> 🛑 **READ THIS FIRST — THE GATE THAT DEFINES THIS ACCOUNT**
> **StashAway does not accept cards for funding in any market.** A "payment" here is a client moving money into a licensed investment account, and it is **bank transfer or bank mandate only**: PayNow + eGIRO + eGIRO FAST (SG), FPX via HSBC (MY), manual bank transfer (HK), Pay by Bank via Lean (UAE), QR / biller-ID transfer (TH). Verified against the correct asset — the per-market help centres — where **652 occurrences of "deposit" sit alongside 0 occurrences** of `credit card`, `debit card`, `Visa`, `Mastercard`, `Apple Pay`, `Google Pay` or any card PSP. Corroborated by direct competitors Syfe and Endowus funding identically.
> **Consequence:** Yuno's core value props — cross-border card approval-rate optimization, MDR reduction via PSP diversification, tokenization, 3DS — have no surface to act on. See the analyst override in Section 3.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | Singapore | **39.82%** (↑74.97%) | PayNow; manual iBanking/FAST transfer; **eGIRO** direct debit; **eGIRO FAST**; SRS/CPF monies. SGD + USD. [src](https://www.stashaway.sg/help-center/900000800423-how-do-i-deposit-funds-into-my-stashaway-account) | No cards (deliberate). No GrabPay. Deposits accepted **only** from MAS-licensed FIs. | ✅ Asia Wealth Platform Pte Ltd (201624878Z), MAS CMS100604 |
| 2 | Malaysia | **24.54%** (↑4.30%) | **FPX** via HSBC Omni Collect + Acme integration; manual transfer; customer-side standing instruction. Any currency, converted to MYR→USD. [src](https://www.tryacme.com/case-study-stashaway) | DuitNow / DuitNow QR not confirmed. Touch 'n Go, Boost, GrabPay not found. No cards. | ✅ StashAway Malaysia Sdn Bhd (201701046385), SC Malaysia eCMSL/A0352/2018 |
| 3 | Hong Kong | **7.60%** (**↑210.32%**) | Manual bank transfer from **any licensed HK bank**, HKD or USD; recurring only via customer-side standing instruction. [src](https://www.stashaway.hk/help-center/900005434863-how-do-i-fund-my-stashaway-account-and-what-are-the-financial-institutions-fi-you-accept-deposits-from) | ⚠️ **FPS, autopay and eDDA not documented** — 0 hits on the dedicated HK "Deposits and Withdrawals" help centre. **Treated as UNVERIFIED, not confirmed absent** — see Section 4 and the ICP note. | ✅ StashAway Hong Kong Limited, SFC CE No. BQE542 |
| 4 | United Arab Emirates | 4.71% (**↓85.69%**) | **"Pay by Bank"** (formerly "FastTransfer") — open-banking payment initiation **powered by Lean**, 15 UAE banks, recurring supported; plus manual deposit. [src](https://www.stashaway.ae/help-center/19627971665177-what-is-fasttransfer-and-why-should-i-choose-it-over-a-manual-deposit) | No cards. | ✅ StashAway Management (DIFC) Limited (CL 3982), DFSA F006312, retail endorsement |
| 5 | United States | 3.81% (↓16.01%) | N/A — no entity, no product, no licence. Almost certainly diaspora/expat and research traffic. | N/A | ❌ None found |

*Also material:* UK 2.94%, **Thailand 2.26%** (licensed entity + own ccTLD), Indonesia 1.77% (**↑503.32%**, no entity/licence), India 1.58%, Korea 1.36%.

### Legal entities
- **Asia Wealth Platform Pte Ltd** (201624878Z) — Singapore. MAS Capital Markets Services licence **CMS100604**; Fund Management + Dealing in Capital Markets Products (CIS); also Exempt Financial Adviser. CEO on register: Nandini Joshi. [MAS FID](https://eservices.mas.gov.sg/fid/institution/detail/201134-ASIA-WEALTH-PLATFORM-PTE-LTD)
- **StashAway Malaysia Sdn Bhd** (201701046385) — Securities Commission Malaysia, licence **eCMSL/A0352/2018**. [src](https://www.stashaway.my/help-center)
- **StashAway Hong Kong Limited** — SFC **CE No. BQE542**. [src](https://www.stashaway.hk/help-center)
- **StashAway Management (DIFC) Limited** (CL 3982) — DFSA **F006312**, retail endorsement; Office 611, Level 6, Liberty House, DIFC. [src](https://www.stashaway.ae/help-center)
- **StashAway Asset Management (Thailand) Co., Ltd** (0105562135522) — Thai SEC, Securities Business Licence Type C Private Fund Management (**Lor Khor-0136-01**). [src](https://www.stashaway.co.th/help-center)

### Known PSPs / payment vendors
These are **bank-rail collections providers, not card PSPs.** No card acquirer exists anywhere in this stack.
- **Acme Technology (Acme) Pte Ltd** — `[Provider Case Study]` Singapore eGIRO: new bank integration, instant eGIRO deposit method, automated deposit reconciliation; live in under 12 weeks; 2–4 business days → **under 2 minutes**. Also phase-two integrator for **Malaysia FPX**. StashAway CTO Jensen Bryan Ching quoted. ([SG/MY case study](https://www.tryacme.com/case-study-stashaway))
- **HSBC** — `[Provider Case Study]` **StashAway's chosen lead payments and collections partner in Malaysia**; FPX collections via **HSBC Omni Collect** (phase 1) with Transaction Enquiry APIs for real-time credit notification. Described as "a replicable blueprint across HSBC's network." ([src](https://www.tryacme.com/case-study-stashaway))
- **Lean Technologies** — `[Terms/Help Centre]` UAE "Pay by Bank" open-banking payment initiation, FSRA-regulated, 15 banks (ADCB, ADIB, Citi, DIB, Mashreq, FAB, RAK, CBD, EIB, ENBD, HSBC, Standard Chartered…). Named by StashAway itself. ([src](https://www.stashaway.ae/help-center/19627971665177-what-is-fasttransfer-and-why-should-i-choose-it-over-a-manual-deposit))
- **Curlec** — `[Press Release]` Malaysia **Direct Debit service provider** as of July 2020, named during the duplicate-debit incident. **Historical; current status unverified.** ([src](https://vulcanpost.com/707206/stashaway-malaysia-users-direct-debit-issue/))
- **Unnamed FX vendor** — Thailand help centre: "we've worked with our FX vendor to bring you one of the lowest foreign exchange rates in the market." Vendor not named. ([src](https://www.stashaway.co.th/help-center/4405204491033-how-do-i-deposit-funds-into-my-stashaway-account))

### Orchestration status
**In-house orchestration layer.** StashAway stitches together per-market bank-rail vendors itself — Acme (SG eGIRO, MY FPX), HSBC Omni Collect (MY lead collections bank), Lean (UAE Pay by Bank), Curlec (MY direct debit, historical) — with no single orchestration platform above them. **No payment orchestrator of any kind was found**, and no card gateway. The TAL's empty `Payment Gateway` / `Payment Orchestrator` cells happen to be directionally right, but for the wrong reason: it is not that they haven't got round to it, it is that **their flows are bank collections, not card acceptance.**

### Buying signals
- 🚀 **HNW / private-markets product expansion across three markets in 12 months** — HK launched Unicorn Top 20 + Multi-Strategy Hedge Fund 12 Mar 2026, available HK/SG/UAE; UAE semi-liquid private infrastructure + PE with Hamilton Lane, Dec 2025. ([HK](https://www.stashaway.hk/r/stashaway-hedge-fund-unicorn-top-20), [UAE](https://www.zawya.com/en/press-release/companies-news/stashaway-broadens-private-market-access-for-uae-based-hnwis-amid-strong-growth-otnms4yn))
- 💳 **Active payments programme completed as recently as June 2026** — the HSBC × Acme Malaysia FPX collections build. They are *already* investing in exactly this layer. ([src](https://www.tryacme.com/case-study-stashaway))
- 🔁 **"Regular Investing Advantage" launched April 2026** — pays an extra **0.15% p.a.** on cash to clients who invest *every month*. StashAway is paying money to maximise recurring monthly deposit volume. ([src](https://www.stashaway.sg/help-center/regular-investing-advantage), [confirmed date](https://www.hubbis.com/news/stashaway-says-first-half-revenue-rose-42-percent-as-singapore-business-turns-profitable))
- 📉 **July 2026: ~20 roles cut (~10% of headcount), product & engineering, concentrated in Kuala Lumpur.** Cuts capacity to build payment plumbing in-house. ([src](https://www.hubbis.com/news/stashaway-says-first-half-revenue-rose-42-percent-as-singapore-business-turns-profitable))
- 💰 **No qualifying funding.** Last raise **US$12.5M in January 2025**; Series D US$25M April 2021. Both outside the 12-month window. ([Jan 2025](https://www.hubbis.com/news/stashaway-says-first-half-revenue-rose-42-percent-as-singapore-business-turns-profitable), [Series D](https://fintechnews.sg/50543/funding/stashaway-to-raise-us-25-million-in-series-d-funding-round-led-by-sequoia-capital-india/))
- 📋 **No public payment RFP found.**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach StashAway` to draft the 12-touch sequence, or call this from `/prepare_batch`.*

⚠️ **Do not generate outreach before reading the analyst override in Section 3.** A card-orchestration pitch to this account would be factually wrong and would burn the thread on the first email.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 12 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+3** | ⚠️ **NOT FOUND — ASSUMED ~50,000–99,999/month.** `[ASSUMPTION — not researched.]` **Billing unit: one client deposit / top-up into an investment account = one transaction.** StashAway discloses no deposit count, no customer count and **no AUM** (explicitly "not disclosed" in the Aug 2026 Tech in Asia/Hubbis interview). Basis for the assumption: Google Play installs **1,071,465** ("1M+", 6.41K reviews) across five markets `[SOURCED]`; **no minimum deposit** in Singapore (recommended S$10) so deposits are frequent and small; and the April 2026 Regular Investing Advantage programme explicitly pays clients to deposit *every month*, so recurring monthly deposits are a deliberately large share of flow. **Scored at the conservative band.** A sourced figure could move this to +5 or below the 40,000 floor. **Per the disclosure rule, an assumed figure never triggers the auto-reject — no Phase 0 rejection fires.** ⬅ **AUDIT FIRST** |
| Orchestration status | **+1** | ✅ **In-house orchestration layer.** Per-market bank-rail vendors (Acme, HSBC Omni Collect, Lean, historically Curlec) assembled by StashAway, no orchestration platform, no card gateway. Hardest-sell classification per the method. |
| 3+ countries | **+3** | ✅ **Verified both ways.** 10 countries >1% traffic share (supplied SimilarWeb) **and** 5 licensed legal entities with registration + licence numbers, each independently sourced from that market's own site footer. |
| Multiple PSPs | **+3** | ✅ **Verified — but read the caveat.** Four named vendors with evidence: Acme (SG+MY, case study), HSBC Omni Collect (MY, case study), Lean (UAE, company help centre), Curlec (MY, 2020 press). ⚠️ **These are bank-collections and open-banking providers, not card PSPs.** The row's intent — "merchant juggling several acceptance providers" — is only partly met. ⬅ **AUDIT** |
| Local rail or licensing gap in a top-3 market | **0** ⬜ | ⬜ **Uncertain — deliberately NOT awarded.** The candidate gap is **FPS / autopay / eDDA in Hong Kong** (#3 market, 7.60%, +210.32%): 0 hits across the dedicated HK "Deposits and Withdrawals" help centre, which enumerates funding and names only manual bank transfer. **I refuse to score it**, because this exact evidence type produced a **proven false negative in Malaysia** — the MY help centre showed 0 hits for FPX while FPX is demonstrably live via HSBC + Acme. The rails are revealed in the logged-in app, not the marketing help centre. **Top manual-verification item.** |
| Recent expansion | **0** ❌ | ❌ **Not met as written.** No *new market* entered in 12 months — all five markets predate the window (TH, UAE 2020, HK 2021). The substantial activity is **product-line** expansion into existing markets (HK/SG/UAE HNW and private markets). Judgement call: if Prateek counts product expansion across three markets, this becomes **+2** and the total 14. Logged rather than inflated. |
| Payment issues | **0** ❌ | ❌ **Not met.** The one documented incident is **July 2020** (Malaysia, 26–27 duplicate direct debits, Curlec named, fully refunded within ~24h, 6-month fee voucher). Six years old, isolated, remediated — not "moderate or high frequency." Lowyat forum users report FPX settlement at T+2/T+3 and slow withdrawals, but that page returned 403 and is user-generated. `[UNVERIFIED — search summary only, page not fetched]` |
| Funding >$10M | **0** ❌ | ❌ **Not met — date-checked as instructed.** Last raise **US$12.5M, January 2025**. 12-month window opens 2025-10-13, so it misses by ~9 months. Prior: Series D US$25M, announced ~26 April 2021. Cumulative "US$86.5 million invested in our team" per StashAway's own About page. |
| High traffic outside home | **+2** | ✅ **Verified.** Singapore **39.82%**, well below the 60% threshold; 60.18% of traffic sits outside the home market. Supplied SimilarWeb, Jul–Sep 2026. |
| Competitor using orchestration | **0** ❌ | ❌ **Not met.** Syfe and Endowus fund via the *same* rails (eGIRO / PayNow / FAST, no cards) with no orchestrator found. Acme names Moomoo and Tiger Brokers as having adopted eGIRO collections — that is a shared **vendor and rail**, not payment orchestration. No competitor confirmed on any orchestrator. |
| Payment job postings | **0** ❌ | ❌ **Not met.** Careers page: 0 hits for `payment`, `settlement`, `reconcil`, `banking`; no reachable ATS. The 2 "Treasury" hits were the **StashAway Corporate → Treasury Management** product link, not a role. Direction of travel is the opposite: ~20 product/engineering roles cut in KL, July 2026. |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **computed 12/29 = 🟢 Medium**

**No public payment RFP found**, so no RFP override.

> ### 🔴 ANALYST OVERRIDE — recommend DOWN from 🟢 Medium to 🔴 Low Priority
>
> **This is the override the brief anticipated, and I am recommending it on evidence rather than suspicion.** Five grounds, three of which are explicit override triggers in the method:
>
> **1. There is no card volume to orchestrate — verified against the correct asset.** Across the five per-market help centres and every deposit-mechanics article, **652 occurrences of "deposit" coexist with zero occurrences** of `credit card`, `debit card`, `card payment`, `Visa`, `Mastercard`, `Amex`, `UnionPay`, `Apple Pay`, `Google Pay`, and zero of `Stripe`, `Adyen`, `Braintree`, `2C2P`, `Xendit`, `iPay88`, `Checkout.com`, `Worldpay`, `payment gateway` or `payment orchestration`. Control greps on the same files confirm the method works (`deposit` 652, `bank` 193, `transfer` 125, `Lean` 10). Singapore goes further and **positively excludes** non-bank money: *"We accept deposits from Financial Institutions (FI) that are licensed by the Monetary Authority of Singapore… If you make a deposit from an FI that is not licensed by MAS, we may reject the deposit and return the funds to the sender."* Hong Kong mirrors it for licensed HK banks. **Cross-border approval-rate optimization, MDR reduction via PSP diversification, tokenization and 3DS have no surface here.**
>
> **2. It is a category property, not a StashAway gap.** Direct competitors **Syfe** (eGIRO, PayNow, FAST, wire) and **Endowus** (FAST, PayNow, eGIRO, CPF/SRS) fund identically, with no cards. Card-funded investing carries AML, chargeback and cost-of-acceptance problems, so the whole SG/MY/HK robo-advisory category deliberately avoids it. There is no competitive wedge to lever.
>
> **3. The matrix is double-counting one structural fact — an explicit override trigger.** "Multiple PSPs" (+3) and "3+ countries" (+3) are both firing off the *same* underlying reality: one licensed entity per market, each with its own local bank and local collections vendor. That is 6 of 12 points describing a single fact about regulated per-market licensing, not two independent signals.
>
> **4. Regulatory reality constrains the pitch — an explicit override trigger.** Money moves into a licensed, trustee-held investment account, swept to trustee accounts daily, subject to AML source-of-funds checks and (in SG and HK) accepted only from licensed banks. Inserting an orchestrator into that flow is a licensing and compliance question before it is a routing question. StashAway holds **CMS/fund-management and advisory authorisations only — it is NOT a Payment Services Act licensee** (verified live on the MAS FID, which lists no PSA licence), so it has no payments licence of its own to lean on.
>
> **5. The incumbent path is a global bank, and the build is already done.** StashAway's own stated collections roadmap runs through **HSBC Omni Collect** — explicitly "a replicable blueprint across HSBC's network" — plus **Acme** as integrator. HSBC Omni Collect already bundles FPX, cards, e-wallets and DuitNow QR and is live in 12 markets including Singapore, Hong Kong, Malaysia and Thailand. The Malaysia programme completed **June 2026** and the Singapore eGIRO rebuild is also done. Yuno would be arguing against a just-finished build, delivered by their lead bank.
>
> **What would reverse this override** (and is worth one disqualifying question, not a sequence): evidence that StashAway accepts cards for *any* flow — a card-funded top-up, a card-paid advisory fee, or a debit-card product — or a sourced deposit count materially above 100,000/month combined with a decision to move off the HSBC/Acme path. Absent that, this belongs in `not-icp/` with the reasoning preserved, not in an outreach sequence.
>
> **This is a legitimate, valuable outcome of the run, not a failed run.** The research below is the asset: it is a complete, sourced map of how an entire regulated APAC vertical moves money, reusable across the 63 Investment Platform rows on the TAL.

### Source Notes
- ✅ **Five live per-market properties resolved and redirect-tested.** `stashaway.com` **302s to `www.stashaway.sg`** — it is not a separate global site. Live distinct properties: `stashaway.sg` (235,833 b), `stashaway.my` (207,285 b), `stashaway.hk` (259,600 b), `stashaway.ae` (216,167 b), `stashaway.co.th` (255,059 b). **`stashaway.com.my` does not resolve** (proxy 502); Malaysia is `stashaway.my`. This matches SimilarWeb's "`stashaway.sg` + 4 domains" exactly.
- ✅ **Nonsense-path control run.** `https://www.stashaway.sg/zzz-nonsense-qwerty-12345` returns a genuine **404 at 27,741 bytes**, distinct in both code and size from the real article pages (26,696–28,811 b). Every 200 cited here is a real page, not a soft-404.
- ✅ **MAS licence verified live**, not from memory: Capital Markets Services (Fund Management; Dealing in CMP: CIS) + Exempt Financial Adviser. **No Payment Services Act licence listed.** Page last updated 22 Sep 2026.
- ✅ **No CSP header on any of the five properties** (all Vercel-hosted), so there is no CSP asset map for this account. Noted so nobody re-spends budget on it.
- ⚠️ **Two false positives caught and discarded in the Google Play listing.** `FPX` resolved to **base64 PNG noise**, and `debit card` / `bank transfer` resolved to **neighbouring apps' descriptions in the similar-apps carousel** (a UK/EU neobank and a remittance app) — not StashAway's listing. Both are documented traps; neither is a finding. StashAway's own Play description names no payment method.
- ⚠️ **`FAST` and `FPS` checked in both directions, as instructed.** Every one of the SG `FAST` hits is the genuine product name **"eGIRO FAST"** — no "breakfast"-class noise. HK `FPS` returned **0 hits with no base64 or frame-rate noise to discount**, so the zero is clean but, per the Malaysia lesson, still only means "not documented on this asset."
- ⚠️ **PROVEN FALSE NEGATIVE — the single most important methodological finding here.** My Malaysia help-centre grep returned **0 for FPX and 0 for DuitNow** against working controls (`deposit` 142, `stashaway` 953). **FPX is nonetheless live in Malaysia**, confirmed by the HSBC/Acme case study and by independent Lowyat user discussion. **StashAway's marketing help centre does not document the rails that exist inside the logged-in app.** Every "rail absent" reading in this report is therefore capped at "not documented", never "confirmed absent" — including Hong Kong. This is why the local-rail ICP row scores 0 rather than +3.
- ⚠️ **AUM is not disclosed by the company.** Third-party figures conflict badly: "over SGD 4 billion as of June 2026" (Kopi Notes, a review blog) vs "US$1.5 billion" (older company announcement) vs the US$1bn milestone reached ~2021. `[UNVERIFIED — search summary only, page not fetched]` for all three. An independent cross-check — H1 2026 net revenue SGD 11.5m annualised ≈ SGD 23m ÷ a 0.2–0.8% p.a. fee band — implies roughly SGD 3–7bn, which is consistent with the SGD 4bn claim but is `[ESTIMATE, not confirmed]` and rests on assuming all revenue is AUM fees.
- ⚠️ **The HSBC attribution is a vendor claim.** Acme's page states the case study was HSBC-published in June 2026, but **no StashAway case study is findable on HSBC's own site**, and HSBC's Malaysia client-stories section surfaces Zuellig Pharma instead. The FPX-in-Malaysia *fact* is independently corroborated by Lowyat users; the *HSBC-published* framing is not.
- ⚠️ **Curlec is historical.** Named as Malaysia direct-debit provider in July 2020 only. Current status unverified — Acme/HSBC may have displaced it. Do not state it as current.
- ⚠️ **No credentials, keys or merchant IDs were encountered or recorded.** Nothing of that kind appears in this file.
- ❌ **The UAE collapse is NOT explained.** See Section 7. I ruled out the obvious causes but did not find the real one. Reported as unresolved rather than guessed.

### TAL corrections required (`accounts/apac-tal.csv`)
| Cell | Current | Should be | Evidence |
|---|---|---|---|
| `Operating Countries` | `Singapore` | `Singapore; Malaysia; Hong Kong; Thailand; United Arab Emirates` | ⛔ Contradicts the row's **own** INFO cell. Five licensed entities, each sourced from its market's site footer. StashAway's own About page: *"Trusted by clients across Singapore, Malaysia, Hong Kong, Thailand, and the UAE."* |
| `INFO` | names SG, MY, HK and the UAE | add **Thailand** | The INFO cell omits Thailand, which has its own licensed entity (Thai SEC Lor Khor-0136-01), its own ccTLD `stashaway.co.th`, its own biller ID, and 2.26% of traffic. |
| `WEBSITE` | `stashaway.com` | `stashaway.sg` (+ `.my`, `.hk`, `.ae`, `.co.th`) | `stashaway.com` **302s to `www.stashaway.sg`**; it is not a distinct property. Misleading as the canonical domain for a five-ccTLD business. |
| `Payment Gateway` | *(empty)* | `None — no card acceptance in any market` | Verified across five help centres with working controls. Empty ≠ unknown here; the correct value is an explicit "none, by design". |
| `Payment Orchestrator` | *(empty)* | `None — in-house per-market bank-rail layer (Acme, HSBC Omni Collect, Lean)` | See Section 3B. |

### Success Case Alternatives
**No Yuno success case is a good match for this account, and I am not going to force one.** The published Yuno case base is card-and-APM acceptance for merchants selling goods and services. StashAway is a licensed asset manager whose money-in flow is bank collections into a trustee account. Presenting any Yuno customer as analogous here would misrepresent both parties, and the rules forbid attaching numbers to customers without published metrics. If this account is ever revisited, the honest framing is a **multi-market A2A/bank-rail coverage** conversation, and it needs a reference built for that shape.

---

## Executive Summary

StashAway is a Singapore-HQ'd licensed digital wealth manager running five licensed entities across Singapore, Malaysia, Hong Kong, Thailand and the UAE, monetised through 0.2%–0.8% p.a. management fees on AUM rather than per-transaction revenue. **The defining payment finding is negative and decisive: StashAway accepts no cards for funding in any market.** Client money enters exclusively over bank rails — PayNow, eGIRO and eGIRO FAST in Singapore; FPX via HSBC Omni Collect with Acme as integrator in Malaysia; manual bank transfer in Hong Kong; Lean-powered open-banking "Pay by Bank" in the UAE; QR and biller-ID transfer in Thailand — and Singapore and Hong Kong positively restrict deposits to licensed banks only. The orchestration motion is therefore **in-house**: StashAway has itself assembled a per-market bank-rail collections layer from point vendors, completing a Malaysia FPX programme as recently as June 2026 and an eGIRO rebuild in Singapore, with its lead bank HSBC explicitly positioning the work as "a replicable blueprint across HSBC's network." The computed ICP score is 12/29 (🟢 Medium), but **I recommend an analyst override down to 🔴 Low**: there is no card volume for Yuno to route, the same pattern holds across every direct competitor, and two of the four scoring rows are double-counting a single fact about regulated per-market licensing.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** **Path 1 — pasted/supplied SimilarWeb data**, `accounts/traffic/stashaway.md`, supplied by Prateek 2026-10-13 (screenshot). Period Jul–Sep 2026, all traffic, "include all country domains" ON. 39 countries listed. **Used verbatim; not re-researched**, per the method's resolution order.

⚠️ **No absolute visit total was supplied**, so "Est. Monthly Visits" cannot be computed for any row. Marked Not found throughout rather than invented.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | Singapore | **39.82%** 🔺high priority | Not found | ↑ 74.97% — growing sharply | SimilarWeb (supplied 2026-10-13) |
| 2 | Malaysia | **24.54%** 🔺high priority | Not found | ↑ 4.30% — stable/slow growth | SimilarWeb (supplied 2026-10-13) |
| 3 | Hong Kong | **7.60%** 🔺high priority | Not found | **↑ 210.32%** — fastest riser | SimilarWeb (supplied 2026-10-13) |
| 4 | United Arab Emirates | 4.71% | Not found | **↓ 85.69%** — largest move in the table 🚩 | SimilarWeb (supplied 2026-10-13) |
| 5 | United States | 3.81% | Not found | ↓ 16.01% | SimilarWeb (supplied 2026-10-13) |
| 6 | United Kingdom | 2.94% | Not found | ↑ 37.65% | SimilarWeb (supplied 2026-10-13) |
| 7 | Thailand | 2.26% | Not found | ↑ 36.67% | SimilarWeb (supplied 2026-10-13) |
| 8 | Indonesia | 1.77% | Not found | **↑ 503.32%** 🚩 | SimilarWeb (supplied 2026-10-13) |
| 9 | India | 1.58% | Not found | ↓ 15.29% | SimilarWeb (supplied 2026-10-13) |
| 10 | Republic of Korea | 1.36% | Not found | ↑ 24.84% | SimilarWeb (supplied 2026-10-13) |

Listed total 90.39%; remaining ~9.61% across 29 further countries.

**Domain set resolved — the "+4 unnamed domains" are no longer unknown.** Independently redirect-tested 2026-10-13:

| Domain | Final URL | Code | Bytes | Verdict |
|---|---|---|---|---|
| `stashaway.com` | `https://www.stashaway.sg/` | 200 | 43,811 | **302 redirect — NOT a distinct property.** Its traffic is an artefact of the `.sg` property. |
| `stashaway.sg` | `https://www.stashaway.sg/` | 200 | 235,833 | ✅ Live property (Singapore) |
| `stashaway.my` | `https://www.stashaway.my/` | 200 | 207,285 | ✅ Live property (Malaysia) |
| `stashaway.hk` | `https://www.stashaway.hk/` | 200 | 259,600 | ✅ Live property (Hong Kong) |
| `stashaway.ae` | `https://www.stashaway.ae/` | 200 | 216,167 | ✅ Live property (UAE) — **alive, so the ↓85.69% is not a dead domain** |
| `stashaway.co.th` | `https://www.stashaway.co.th/` | 200 | 255,059 | ✅ Live property (Thailand) |
| `stashaway.com.my` | — | 000 | 0 | ❌ Does not resolve |
| `stashaway.co.id` / `stashaway.id` | — | 000 | 0 | ❌ Do not resolve — **no Indonesian property exists** |

**The per-market ccTLD structure maps exactly onto per-market entities, licences and funding rails** — Prateek's hypothesis in the supplied notes is confirmed on all three counts. Each ccTLD carries its own licensed entity in its footer, its own regulator, and its own deposit mechanics.

**Top-10 markets with NO local entity (cross-ref Section 2):** United States (3.81%), United Kingdom (2.94%), Indonesia (1.77%), India (1.58%), Republic of Korea (1.36%). Together 11.46%. **None of these is a servable market** — StashAway is not licensed to manage money for residents there, and no `.id`/`.in`/`.kr` property exists. This traffic is best read as diaspora, expat, prospective-relocator and research traffic, which is **not a cross-border acquiring opportunity** because there is no transaction behind it.

**Engagement — and the hard constraint it imposes.** Singapore 00:00:54 / 1.97 pages / 52.67% bounce; Malaysia 00:01:11 / 2.16; Hong Kong 00:01:33 / 2.27; Thailand 00:00:30; India 00:00:37; **Korea 00:00:15 / 1.34 pages**. As Prateek's notes state, this is *expected* for a wealth manager: the marketing ccTLD is a thin front door and all real activity happens inside the logged-in app at `app.stashaway.sg`, which SimilarWeb cannot see. **Consequence, honoured throughout this report: these visit shares are a weak proxy for deposit volume and have NOT been used to derive any transaction count.** The Section 12 figure is derived from installs and product mechanics instead, and is labelled an assumption regardless.

**Two anomalous rows, treated with suspicion rather than excitement, as instructed:**
- **UAE — 00:07:26 dwell but only 1.40 pages and 59.14% bounce.** Seven and a half minutes on 1.4 pages is not a browsing pattern; it is consistent with abandoned open tabs, automated traffic, or a measurement artefact. Combined with the ↓85.69% collapse, this row's *absolute* level should not be trusted either.
- **Indonesia — 00:12:15 dwell, 2.10 pages, 24.04% bounce, ↑503.32%.** Twelve minutes with almost no depth and an improbably low bounce rate, in a market where **no StashAway entity, licence or domain exists** and where the company cannot legally take a deposit. **This is not demand.** Most likely non-human or misattributed traffic, possibly driven by StashAway's Malaysian/Singaporean content ranking for Bahasa-language finance queries. I could not establish a cause. **Do not build an Indonesia angle on this row.**

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Singapore. Registered address on the MAS register: 175A Bencoolen Street, Burlington Square #07-04, Singapore 189650. Founded 2016 (entity 201624878Z); first product launched 2017.

| Country | Entity Name | Registration # | Licence / Regulator | Source |
|---------|-------------|----------------|---------------------|--------|
| Singapore | Asia Wealth Platform Pte Ltd | 201624878Z | **MAS CMS100604** — Capital Markets Services (Fund Management; Dealing in CMP: Collective Investment Schemes) + Exempt Financial Adviser | [MAS FID](https://eservices.mas.gov.sg/fid/institution/detail/201134-ASIA-WEALTH-PLATFORM-PTE-LTD) · [site footer](https://www.stashaway.sg/help-center) |
| Malaysia | StashAway Malaysia Sdn Bhd | 201701046385 | **Securities Commission Malaysia eCMSL/A0352/2018** | [site footer](https://www.stashaway.my/help-center) |
| Hong Kong | StashAway Hong Kong Limited | Not found | **SFC CE No. BQE542** | [site footer](https://www.stashaway.hk/help-center) |
| UAE (DIFC) | StashAway Management (DIFC) Limited | CL 3982 | **DFSA F006312** — arranging custody, arranging deals in investments, advising on financial products, managing assets, **with retail endorsement** | [site footer](https://www.stashaway.ae/help-center) |
| Thailand | StashAway Asset Management (Thailand) Co., Ltd | 0105562135522 | **Thai SEC, Securities Business Licence Type C — Private Fund Management (Lor Khor-0136-01)**, issued by the Ministry of Finance | [site footer](https://www.stashaway.co.th/help-center) |

**Phase 0 regulatory check — cleared.** StashAway is a **licensed asset manager, not a PSP, gateway, acquirer or orchestrator**, so it is in ICP on the vertical test and does not route to Partnerships. Critically, the MAS Financial Institutions Directory lists **only** Capital Markets Services and Exempt Financial Adviser authorisations for Asia Wealth Platform Pte Ltd — **no Payment Services Act licence appears**, so StashAway is not itself a payment-services licensee. Verified live on the register (page last updated 22 Sep 2026), not from background knowledge.

*Nice corroboration detail:* the Thai entity's registration number `0105562135522` is the Thai biller ID `010556213552200` minus its two trailing digits — the bill-payment identity is literally derived from the company registration.

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| Singapore | ✅ #1 (39.82%) | ✅ Yes | N/A — no card acquiring at all; deposits restricted to MAS-licensed FIs | **None.** Domestic bank rails, domestic entity. |
| Malaysia | ✅ #2 (24.54%) | ✅ Yes | N/A — FPX collections via local bank (HSBC) | **None.** Domestic FPX, domestic entity, local lead bank. |
| Hong Kong | ✅ #3 (7.60%) | ✅ Yes | N/A — deposits restricted to licensed HK banks | **None.** Domestic bank rails, domestic entity. |
| UAE | ✅ #4 (4.71%) | ✅ Yes (DIFC) | N/A — open-banking initiation via FSRA-regulated Lean | **None.** ⚠️ Out of APAC territory — sits with EMEA. |
| Thailand | ✅ #7 (2.26%) | ✅ Yes | N/A — domestic QR/biller transfer | **None.** |
| United States | ✅ #5 (3.81%) | ❌ No | — | **No risk, because no transaction.** Not a servable market. |
| United Kingdom | ✅ #6 (2.94%) | ❌ No | — | Same. |
| Indonesia | ✅ #8 (1.77%) | ❌ No | Yes, in principle (BI PJP licensing) — **moot, no product** | **No risk, because no transaction.** See the Section 1 anomaly note. |
| India | ✅ #9 (1.58%) | ❌ No | Yes, in principle (RBI PA authorisation) — **moot, no product** | Same. |
| Republic of Korea | ✅ #10 (1.36%) | ❌ No | Yes, in principle — **moot, no product** | Same. |

> **The usual cross-border warning does NOT apply to this account, and it would be wrong to issue it.** The method's standard language — *"potential cross-border operation, transactions likely processed cross-border with higher scheme costs and lower approval rates"* — presumes a merchant accepting cards from customers it has no entity near. StashAway has a **licensed entity in every market where it takes money**, and takes money **only** in those five markets, over **domestic bank rails**. Every top-5 traffic market has a local entity. The five entity-less markets in the top 10 generate no transactions at all. **There is no cross-border acquiring gap, no scheme-cost premium and no FX-on-card exposure to sell against.** This is the single biggest reason the standard Yuno cross-border motion does not fit.

**The one genuine cross-border flow is FX, not acquiring.** Deposits arrive in SGD, USD, MYR, HKD, THB and AED and must be converted to **USD** to buy US-listed ETFs. Malaysia is explicit that non-MYR deposits are "converted to MYR first before being converted to USD at the currency conversion rate by the bank", and the Thai help centre references an unnamed **"FX vendor"**. This is a treasury and FX-cost conversation. **Yuno is a payment orchestrator, not an FX provider**, so I am flagging this as context rather than an angle — overselling it would be the easiest way to lose credibility on the first call.

> **MANUAL:** All five entities were read from each market's own site footer and the Singapore one confirmed against the MAS register. Hong Kong's companies-registry number was not located; the SFC CE number is confirmed.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Singapore | **Acme Technology (Acme) Pte Ltd** — eGIRO direct-debit integration, instant eGIRO deposit method, automated deposit reconciliation, new bank integration. Live in <12 weeks. 2–4 business days → **under 2 minutes**. 50% of eGIRO adopters had never used eGIRO before. | `[Provider Case Study]` | https://www.tryacme.com/customer-stories-stashaway |
| Malaysia | **HSBC** — StashAway's chosen **lead payments and collections partner**; **FPX** collections via **HSBC Omni Collect**, with Transaction Enquiry APIs giving real-time push notification on deposit credit (phase 1). | `[Provider Case Study]` | https://www.tryacme.com/case-study-stashaway |
| Malaysia | **Acme Technology** — phase 2 integrator: single API connection to HSBC; detects and verifies **FPX** payments, notifies StashAway in real time, moves funds between accounts, pays out withdrawals, and **sweeps collected funds to trustee accounts daily**. | `[Provider Case Study]` | https://www.tryacme.com/case-study-stashaway |
| Malaysia | **Curlec** — Direct Debit service provider as at July 2020. **Historical; current status unverified.** | `[Press Release]` | https://vulcanpost.com/707206/stashaway-malaysia-users-direct-debit-issue/ |
| UAE | **Lean Technologies** — "Pay by Bank" (formerly "FastTransfer") open-banking payment initiation; named by StashAway itself; "nationally regulated by FSRA"; 15 connected banks; transfers complete in under 180 seconds (up to 1 business day above AED 25,000); recurring deposits supported. | `[Terms/Help Centre]` | https://www.stashaway.ae/help-center/19627971665177-what-is-fasttransfer-and-why-should-i-choose-it-over-a-manual-deposit |
| Thailand | **Unnamed FX vendor** — "we've worked with our FX vendor to bring you one of the lowest foreign exchange rates in the market." Not named. | `[Terms/Help Centre]` | https://www.stashaway.co.th/help-center/4405204491033-how-do-i-deposit-funds-into-my-stashaway-account |
| Singapore (scheme) | **BCS (Banking Computer Services)** — operator of eGIRO; charges implementation fees alongside the banks. Scheme infrastructure, not a StashAway vendor relationship. | `[Third-Party Report]` | https://www.tryacme.com/blog/egiro-the-hidden-promise-behind-near-term-challenges |
| **All markets** | **No card acquirer, card gateway or card PSP of any kind.** 0 hits for Stripe, Adyen, Braintree, 2C2P, Xendit, iPay88, Razer, Checkout.com, Worldpay, Visa, Mastercard, Amex, UnionPay, Apple Pay, Google Pay across all five help centres, against controls of `deposit` 652 / `bank` 193. | `[Source Code]` + `[Terms/Privacy Policy]` | Verified 2026-10-13 across `stashaway.{sg,my,hk,ae,co.th}/help-center` and all deposit articles |

#### 3B. Payment Orchestrator

**Classification: In-house orchestration layer.**

StashAway operates **no payment orchestration platform and no card gateway**. What it has instead is a self-assembled, per-market bank-rail collections layer: **Acme** for Singapore eGIRO and as Malaysia's FPX integrator, **HSBC Omni Collect** as Malaysia's lead collections bank, **Lean** for UAE open-banking initiation, **Curlec** historically for Malaysian direct debit, plus an unnamed FX vendor and domestic QR/biller rails in Thailand. StashAway itself is the integration point across these; nothing sits above them.

> *"No public evidence found of a payment orchestration platform."* — but the standard follow-on sentence in the method (*"which limits routing optimization, failover capabilities, and multi-acquirer strategies"*) **does not apply and must not be used in outreach.** There are no acquirers to route between and no card declines to fail over. Routing optimisation is not a meaningful concept for a push-based bank transfer that the customer initiates from their own banking app.

**Searches run for orchestrators, all negative:** Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno, "payment orchestration", "payment routing" — 0 hits across all five properties' help centres and deposit articles, against working controls. The TAL's empty `Payment Orchestrator` cell is **independently confirmed as genuinely empty** — which, per the brief's warning, is not something I assumed from the blank cell.

**Why this is the hardest of the four motions:** per the APAC reference, an in-house layer means arguing reach and opportunity cost, never "you need orchestration." Here even that argument is weak, because the reach they want next (Hong Kong, Thailand) is already covered by HSBC Omni Collect's 12-market footprint and Acme's 17-market coverage — both incumbents they are actively paying.

> **MANUAL:** The decisive evidence sits behind the login at `app.stashaway.sg`. Walking the in-app deposit screen with DevTools in each market — especially **Hong Kong** — is the only way to settle the per-market rail question, because the marketing help centre is demonstrably stale (see the proven Malaysia false negative in Source Notes).

---

### Section 4: Alternative & Local Payment Methods

Checked against `.claude/reference/apac-payments.md` §2 for every market with >1% traffic share.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| Singapore | **PayNow** | Bank transfer / A2A | **Active in checkout** — in-app deposit flow Step 5: *"You will find the PayNow and ibanking instructions"* | [help centre](https://www.stashaway.sg/help-center/900000800423-how-do-i-deposit-funds-into-my-stashaway-account) |
| Singapore | **eGIRO** (direct debit mandate) | Direct debit / mandate | **Active in checkout** — dedicated help-centre category; one-time or recurring; 8 banks | [help centre](https://www.stashaway.sg/help-center/14264118368025-which-banks-can-i-use-to-set-up-egiro-payments) |
| Singapore | **eGIRO FAST** | Direct debit / mandate (instant) | **Active in checkout** — dedicated category, "Fast Direct Debit Transfer" | [help centre](https://www.stashaway.sg/help-center/egiro-fast) |
| Singapore | Manual iBanking / FAST transfer | Bank transfer / A2A | **Active in checkout** — with a unique reference code per portfolio | [help centre](https://www.stashaway.sg/help-center/900000800423-how-do-i-deposit-funds-into-my-stashaway-account) |
| Singapore | **SRS** and **CPF** monies | Regulated retirement scheme | **Active** — dedicated SRS category; CPF calculators | [help centre](https://www.stashaway.sg/help-center) |
| Singapore | Cards (credit/debit) | Cards | **Not found — 0 hits.** Deposits accepted **only** from MAS-licensed FIs; others "may be rejected and returned to the sender" | [help centre](https://www.stashaway.sg/help-center/360007398953-what-financial-institutions-do-you-accept-deposits-from) |
| Singapore | GrabPay | Digital wallet | Not found (0 hits) | — |
| Malaysia | **FPX** | Bank transfer / A2A | **Active** — via HSBC Omni Collect + Acme. ⚠️ **Not documented in the MY help centre** (0 hits) — this is the proven false negative | [case study](https://www.tryacme.com/case-study-stashaway) |
| Malaysia | Direct Debit | Direct debit / mandate | **Active as at 2020 via Curlec**; current provider unverified. Acme case study notes direct debits "could take weeks to set up" | [press](https://vulcanpost.com/707206/stashaway-malaysia-users-direct-debit-issue/) |
| Malaysia | Manual transfer + customer standing instruction | Bank transfer / A2A | **Active in checkout** — the only method the MY help centre documents | [help centre](https://www.stashaway.my/help-center/900000950666-how-do-i-make-changes-to-my-one-time-and-monthly-deposits) |
| Malaysia | **DuitNow / DuitNow QR** | Bank transfer / A2A | **Not found** (0 hits). HSBC Omni Collect *does* support DuitNow QR, so it may be live in-app — unverified either way | — |
| Malaysia | Touch 'n Go eWallet, Boost, GrabPay | Digital wallet | Not found (0 hits each) | — |
| Malaysia | Cards | Cards | Not found (0 hits) | — |
| Hong Kong | Manual bank transfer, HKD or USD | Bank transfer / A2A | **Active in checkout** — from **any licensed HK bank**; non-bank FI deposits "may be rejected" | [help centre](https://www.stashaway.hk/help-center/900005434863-how-do-i-fund-my-stashaway-account-and-what-are-the-financial-institutions-fi-you-accept-deposits-from) |
| Hong Kong | Customer-side standing instruction | Direct debit / mandate (customer-initiated) | **Active** — recurring handled at the client's own bank, not by StashAway | [help centre](https://www.stashaway.hk/help-center/900005434803-how-do-i-make-changes-to-my-one-time-and-monthly-deposits) |
| Hong Kong | **FPS** | Bank transfer / A2A | ⚠️ **Unknown, not documented.** 0 hits on the dedicated HK deposits category, with no base64/frame-rate noise to discount. **Not scored as absent** — see Source Notes | — |
| Hong Kong | **Autopay / eDDA** | Direct debit / mandate | ⚠️ **Unknown, not documented.** 0 hits each | — |
| Hong Kong | Octopus, AlipayHK, WeChat Pay HK | Digital wallet | Not found (0 hits each) | — |
| UAE | **Pay by Bank** (ex-"FastTransfer") via **Lean** | Bank transfer / A2A (open banking) | **Active in checkout** — 15 banks, <180s, recurring supported | [help centre](https://www.stashaway.ae/help-center/19627971665177-what-is-fasttransfer-and-why-should-i-choose-it-over-a-manual-deposit) |
| Thailand | **QR transfer + biller ID** `010556213552200` | Bank transfer / A2A | **Active in checkout** — save QR in-app, pay from mobile banking | [help centre](https://www.stashaway.co.th/help-center/4405204265881-what-is-stashaways-biller-id) |
| Thailand | Recurring transfer (DCA) via customer's bank | Direct debit / mandate (customer-initiated) | **Active** — set up in the client's own banking app | [help centre](https://www.stashaway.co.th/help-center/7740290910745-how-to-set-up-a-standing-instruction-for-dca-plan) |
| Thailand | **PromptPay** (by name) | Bank transfer / A2A | Not found by name; the QR + biller-ID mechanism is consistent with the domestic bill-payment/PromptPay infrastructure but is not named as such | — |
| All | BNPL / instalments / carrier billing / cash-voucher / crypto funding | — | **Not found and not applicable.** Inappropriate for funding a regulated investment account | — |

**The one rail gap worth a conversation, stated honestly:**

> *"In Hong Kong — StashAway's #3 market at 7.60% of traffic and by far its fastest-growing (↑210.32%) — no automated or embedded funding rail is documented. The dedicated 'Deposits and Withdrawals' help centre enumerates the funding flow and names only manual bank transfer from a licensed HK bank, with recurring deposits pushed back onto the client's own bank as a standing instruction. Neither FPS, autopay nor eDDA appears. By contrast Singapore has eGIRO, eGIRO FAST and PayNow, and the UAE has Lean-powered Pay by Bank."*

⚠️ **I have deliberately not scored this as a confirmed gap, and nor should outreach assert it.** The identical evidence type returned a **false negative for FPX in Malaysia**, where FPX is demonstrably live. The honest formulation for a call is a **question** — "is Hong Kong still on manual transfer while Singapore runs eGIRO?" — not a claim. Asserting an absence that turns out to be live is precisely how this thread would be lost.

I am also **not** issuing the method's standard "widely used but not supported" warning for Hong Kong, because doing so requires a live source for FPS's prominence, and citing an APAC rail's market share from background knowledge is forbidden. No such source was obtained within budget.

> **MANUAL:** VPN into HK and MY and walk the in-app deposit screen. This is the single highest-value manual check in the file.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| **Duplicate charges** — technical fault caused **26–27 back-to-back Direct Debit collections** of each user's monthly deposit amount. Malaysia-only; Singapore unaffected. Banks hit: Maybank, HSBC, Hong Leong, CIMB. Direct Debit provider **Curlec** named. Fully refunded within ~24h; 6-month free-investing voucher as compensation; post-mortem published 30 Jul 2020. | Facebook groups, press | **Isolated (single incident)** | 27–30 Jul 2020 | [Vulcan Post](https://vulcanpost.com/707206/stashaway-malaysia-users-direct-debit-issue/) · [The Star](https://www.thestar.com.my/tech/tech-news/2020/07/29/stashaway-users-in-malaysia-affected-by-multiple-direct-debit-transactions-due-to-technical-issue) · [RinggitPlus](https://ringgitplus.com/en/blog/investment/stashaway-to-prioritise-refunding-affected-users-after-direct-debit-mishap.html) |
| **Slow settlement / slow withdrawals** — users describe FPX deposits settling T+2/T+3 and ask for faster withdrawals | Lowyat Forum (MY) | Unclear | Undated | [Lowyat](https://forum.lowyat.net/topic/4750563/+20) — ⚠️ **403 on fetch.** `[UNVERIFIED — search summary only, page not fetched]` |
| **Pre-rebuild reconciliation lag** — eGIRO deposits took **2–4 business days** to process and reconcile before the Acme rebuild; now stated as under 2 minutes | Vendor case study | Resolved | Pre-2026 | [Acme](https://www.tryacme.com/customer-stories-stashaway) |
| **Mandate-cancellation-on-insufficient-funds** — StashAway's own documented failure mode, not a complaint: if the client's account is underfunded, the scheduled deposit fails, **the bank cancels the eGIRO mandate outright**, and the bank "might charge a cancellation fee" | Company help centre | Documented design behaviour | Current | [help centre](https://www.stashaway.sg/help-center/15529112835353-what-happens-to-my-egiro-deposit-if-i-dont-have-sufficient-funds-in-my-bank-account) |

**Assessment: frequency is LOW, and the ICP row scores 0.** The one serious incident is **six years old**, isolated, remediated inside 24 hours, compensated, and publicly post-mortemed. No current pattern of declined transactions, failed recurring payments, checkout errors or false fraud declines was found on Reddit, Trustpilot, X or app-store reviews. Google Play shows 6.41K reviews at a healthy rating; the SG App Store listing shows ~4.3 / ~996 ratings (⚠️ attribution uncertain — the iOS page carries similar-app rating counts in the same markup).

> **The one pattern that does matter, and it is a design pattern rather than a complaint:** StashAway's documented eGIRO failure mode is unusually punitive. An underfunded client account does not merely miss one deposit — **the bank cancels the mandate** and may charge the client a fee, so the client must re-enrol through the bank's 10–20-step eGIRO portal flow to resume. Since **April 2026** this also **breaks the client's Regular Investing Advantage streak** and forfeits the 0.15% p.a. boost they were being paid to maintain. That is a genuine, verified, compounding retention mechanism — the closest thing in this account to the involuntary-churn dynamic in `subscription-payments.md` §1.
>
> ⚠️ **But note what it is not.** This is a *bank-side mandate cancellation on an A2A debit*, not a card decline. The orchestration playbook for involuntary churn — network tokens, account updater, decline-code-aware retries, MIT flagging, routing the renewal to a local acquirer — **has no purchase on it**, because there is no card, no issuer and no acquirer in the flow. Per the brief, I am explicitly **not** forcing the subscription frame: a recurring deposit into an investment account is not a SaaS subscription, and only the mandate-failure logic rubs off.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | **Jun 2026** | **StashAway × HSBC FPX collections programme in Malaysia goes public.** HSBC named as StashAway's **lead payments and collections partner**; FPX via HSBC Omni Collect (phase 1), **Acme** as third-party integrator (phase 2) handling FPX detection/verification, real-time notification, inter-account fund movement, withdrawal payouts and **daily sweeps to trustee accounts**. Positioned as "a replicable blueprint across HSBC's network." | **Payment Infrastructure** | https://www.tryacme.com/case-study-stashaway |
| 2 | **Jul 2026** | **~20 employees cut (~10% of headcount)**, in product and engineering, **concentrated in the Kuala Lumpur office.** CEO framed it as shifting skills needs for growth priorities. | Leadership / Restructuring | https://www.hubbis.com/news/stashaway-says-first-half-revenue-rose-42-percent-as-singapore-business-turns-profitable |
| 3 | **Apr 2026** | **"Regular Investing Advantage" launched** — an extra **0.15% p.a.** on cash for clients who invest **every month**. A deliberate, funded push to maximise recurring monthly deposit volume and streak retention. | Product / Payment Strategy | https://www.hubbis.com/news/stashaway-says-first-half-revenue-rose-42-percent-as-singapore-business-turns-profitable · https://www.stashaway.sg/help-center/regular-investing-advantage |
| 4 | **12 Mar 2026** | **Hong Kong launches Unicorn Top 20 and a Multi-Strategy Hedge Fund portfolio**, available in HK, Singapore and the UAE. HK AUM **doubled** and its client base grew **four-fold** in 2025. | Market/Product Expansion | https://www.stashaway.hk/r/stashaway-hedge-fund-unicorn-top-20 · https://www.capital-hk.com/investment-strategy/StashAway012601 |
| 5 | **Dec 2025** | **UAE: semi-liquid private infrastructure and private equity portfolios** for HNW clients, managed by **Hamilton Lane**, with lower minimums, lower fees and monthly liquidity. | Product Expansion | https://www.zawya.com/en/press-release/companies-news/stashaway-broadens-private-market-access-for-uae-based-hnwis-amid-strong-growth-otnms4yn |
| 6 | **Jan 2025** | **US$12.5M raised** from existing institutional investors plus a new family-office investor. **Outside the 12-month ICP window** (window opens 2025-10-13). | Funding | https://www.hubbis.com/news/stashaway-says-first-half-revenue-rose-42-percent-as-singapore-business-turns-profitable |

**Public payment RFP:** **No public payment-related RFP found.** No RFP override applies.

**Payment-related job postings:** **None found.** The `/careers` page is a client-rendered shell with no reachable ATS; 0 hits for `payment`, `settlement`, `reconcil` and `banking`. The two `Treasury` hits were the **StashAway Corporate → Treasury Management** product link, not a vacancy — logged explicitly because it is exactly the kind of hit that would otherwise be miscounted as a payments hire. The direction of travel is negative: product and engineering roles were **cut** in July 2026.

**Licence applications:** none found beyond the five existing licences. No payment-adjacent licence application was found in any market — consistent with StashAway holding no Payment Services Act licence and showing no intent to acquire one.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | Jun 2026 | StashAway × HSBC: FPX collections in Malaysia, with Acme as integrator. Challenge stated as "direct debits and other methods could take weeks to set up, which created friction for investors." | **Highest.** Confirms an active, recent, bank-led collections build in their #2 market — and that they solve this layer by buying from their bank, not from an orchestrator. | https://www.tryacme.com/case-study-stashaway |
| 2 | Undated (© 2026) | StashAway introduces instant eGIRO in Singapore via Acme: new bank integration + instant deposit method + automated reconciliation, live in <12 weeks; **2–4 business days → under 2 minutes**; **50% of eGIRO adopters had never used eGIRO before.** CTO Jensen Bryan Ching quoted. | **High.** The Singapore equivalent of (1), and evidence that deposit UX is treated as a growth lever. | https://www.tryacme.com/customer-stories-stashaway |
| 3 | Undated (© 2026) | Acme notes that robo-advisory and brokerage platforms **including Moomoo, Tiger Brokers and StashAway** "have introduced eGIRO collections to encourage recurring bank transfers to investment portfolios." eGIRO launched 2021 via ABS; operator **BCS**; implementation fees charged by both banks and BCS; portal setup "easily 10–20 steps and several back and forths" across four roles. | **High** — vertical-wide pattern, and both named peers are on the TAL. | https://www.tryacme.com/blog/egiro-the-hidden-promise-behind-near-term-challenges |
| 4 | Jul 2020 | Malaysia Direct Debit fault: 26–27 duplicate collections per affected user; **Curlec** named as the Direct Debit service provider; full refunds inside ~24h; post-mortem 30 Jul. | Medium — historical, but the only documented payment failure and the only evidence of Curlec. | https://vulcanpost.com/707206/stashaway-malaysia-users-direct-debit-issue/ |
| 5 | Current | UAE "FastTransfer" **renamed "Pay by Bank"** — the help-centre URL slugs still read `fasttransfer` while all display copy reads "Pay by Bank". A payment-product rebrand mid-flight. | Low-medium — shows the UAE rail is actively maintained, not abandoned. | https://www.stashaway.ae/help-center/19627951639961-fasttransfer |

**No provider removals found.** No evidence that any PSP, rail or payment method was discontinued in any market.

#### 🚩 The UAE collapse (↓85.69%) — investigated, four causes ruled out, cause NOT established

Prateek's instruction was to explain this before writing anything about MENA. I could not, and I am not going to invent a cause. Here is exactly what I ruled out and what remains.

**Ruled out:**
1. **Domain death / migration.** `stashaway.ae` returns **200 at 216,167 bytes** with a full, current site. Not a dead or redirecting domain. (By contrast `stashaway.com` *does* 302 to `.sg` — but that affects the `.com`/`.sg` attribution, not `.ae`.)
2. **Licence loss or change.** **DFSA F006312 remains on the public register** for StashAway Management (DIFC) Limited, with retail endorsement intact. (⚠️ The DFSA register page itself returned **403** to direct fetch; this rests on search-surfaced register content. `[UNVERIFIED — search summary only, page not fetched]`. Some *authorised individuals* were withdrawn in 2024 and 2026 — individual withdrawals are not a firm closure.)
3. **Market exit.** The opposite is documented: StashAway **launched new UAE products in Dec 2025** (Hamilton Lane private infrastructure and PE) and included the UAE in the Mar 2026 Unicorn Top 20 / hedge-fund rollout. No exit, closure or wind-down reporting was found.
4. **Retail → HNW-only pivot** (my own hypothesis, tested and rejected). The `.ae` site still fully markets retail products — `general-investing`, `simple`, `flexible-portfolios`, `shariah-global-portfolios`, `referrals`, `welcome-bonus` — with 0 hits for `accredited` or `high-net-worth` gating. Retail has not been withdrawn.

**What remains, unresolved:** the most likely explanations are now (a) a **collapse in paid or organic content-marketing traffic** to the `.ae` blog, or (b) a **SimilarWeb measurement or attribution artefact**. (b) is actively supported by the row's own engagement profile — **00:07:26 dwell on 1.40 pages with a 59.14% bounce** is not a human browsing pattern, so the *prior* period's figure may have been inflated by non-human traffic that has since been filtered out. Under that reading the collapse is a **data correction, not a business event.**

> **Therefore: do not treat the UAE as a growth market, and do not treat it as a declining one either.** The 4.71% share is not trustworthy in either direction. **And note the territory rule independently: the UAE is a Gulf market and sits with EMEA, not APAC** (`CLAUDE.md`). StashAway is APAC-HQ'd so the *account* is in scope, but UAE volume is not Prateek's to sell. Combined, the UAE should simply be excluded from the addressable picture.

#### 🚩 Hong Kong (↑210.32%) — explained and corroborated
**Genuine growth.** StashAway's Hong Kong **AUM doubled year-on-year and its client base grew roughly four-fold in 2025** (Capital HK, Jan 2026), and it launched two new HK portfolios on 12 Mar 2026 plus HNW Reserve and private-credit access. A licensed market with real product investment behind it. The traffic rise is consistent with the business.

#### 🚩 Indonesia (↑503.32%) — cause NOT established; do not treat as demand
**No StashAway entity, no licence, no product and no Indonesian domain** (`stashaway.co.id` and `stashaway.id` both fail to resolve). StashAway cannot legally accept an Indonesian resident's deposit. The engagement profile is implausible — **00:12:15 dwell, 2.10 pages, 24.04% bounce**. The most plausible readings are non-human traffic or Bahasa-language content from the `.my`/`.sg` properties ranking in Indonesian search. **I could not establish the cause and am not treating 1.77% from an unlicensed market as demand.**

---

### Section 8: Checkout Experience Audit

**There is no checkout.** This is not an access failure — it is the finding. StashAway sells no goods and takes no card payment; the equivalent flow is an authenticated **deposit instruction** inside the logged-in app at `app.stashaway.sg`, available only to an onboarded, KYC'd and AML-screened client of a licensed entity. It cannot be audited without an account in each of five jurisdictions. The table below records what the public help centre documents about that flow.

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | **No checkout. Authenticated in-app deposit instruction**, generating bank-transfer details, a PayNow/QR target, or an eGIRO/Pay-by-Bank mandate | n/a | Custom-built, in-app, behind login |
| Guest checkout | **Not possible by law.** Account opening requires identity documents, tax residency/TIN, risk profiling and AML checks | n/a | Regulatory, not a UX choice |
| Steps to complete payment | **5 documented steps** (SG): Deposit → account type → eGIRO or Manual → one-time or monthly → amount → receive PayNow/iBanking instructions. HK and TH are also 4–5 steps | Fair | Then the client leaves the app to push funds from their own bank — the core friction, and exactly what eGIRO/Lean remove |
| Card input experience | **None — no card fields anywhere** | n/a | 0 card hits across all five markets |
| Payment methods visible | SG: PayNow, manual iBanking/FAST, eGIRO, eGIRO FAST, SRS/CPF · MY: FPX (in-app), manual, standing instruction · HK: manual bank transfer · UAE: Pay by Bank (Lean), manual · TH: QR + biller ID, recurring bank transfer | Good in SG/UAE, **weakest in HK** | Per-market, not a single global set |
| Location-based method display | **Yes — by ccTLD and by entity.** Each market has its own domain, entity, help centre and rail set | Good | Structural rather than dynamic |
| Instalment / EMI | **None, and correctly so** — nonsensical for funding an investment account | n/a | Not a gap |
| 3DS implementation | **Not applicable — no cards** | n/a | — |
| PCI indicator | **Out of scope — no card data touched** | n/a | See Section 9 |
| Mobile responsiveness | App-first: **Google Play 1,071,465 installs** ("1M+", 6.41K reviews), iOS and **Huawei AppGallery** (C100318407) all linked from the footer | Good | App-first, as APAC norm demands |
| Multi-currency / local pricing | SG: SGD + USD · HK: HKD + USD · MY: any currency → MYR → USD · TH: THB → USD via an unnamed FX vendor · UAE: AED | Fair | A real FX cost layer; client bears bank charges on USD transfers in SG |
| Saved payment methods | **Yes, as mandates:** eGIRO supports multiple saved bank accounts (8 banks, SG); Lean supports multiple connected banks (15 banks, UAE) | Good in SG/UAE | HK and MY have no equivalent documented |
| Error message clarity | The underfunded-eGIRO article is clear and candid: deposit fails, **bank cancels the mandate**, bank may charge a cancellation fee | Fair | Honest, but a harsh failure mode |

> *Full deposit flow not accessible — it sits behind authenticated, KYC-gated login in five jurisdictions. Findings limited to publicly observable help-centre documentation.*

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **Not found** — and almost certainly **not applicable** | — |
| Card data handling | **No card data handled.** 0 occurrences of any card brand, card field or card PSP across all five markets' help centres and deposit articles, against controls of `deposit` 652 / `bank` 193 / `transfer` 125 | Verified 2026-10-13 across `stashaway.{sg,my,hk,ae,co.th}` |
| Recommended Yuno integration | **None applicable.** A card SDK or back-to-back card API has nothing to integrate against | — |

*No direct PCI compliance documentation found publicly for StashAway.* The method's conditional inference (reduced PCI scope via a tokenized PSP checkout) **cannot be drawn, because there is no PSP checkout at all.** The accurate statement is that StashAway appears to sit **outside PCI scope entirely** by never touching card data — which also removes "PCI scope reduction" from the list of available Yuno value propositions for this account.

Their `/security` page exists on all five properties but was not fetched within budget — worth a look if this account is ever revisited, since it may name infrastructure vendors.

---

### Section 10: Strategic Insights & Outreach Angles

> ⚠️ **Read this first.** Per the analyst override, **my recommendation is not to run a sequence against this account.** The insights below are written to be *honest* rather than persuasive: each is cross-referenced across at least two sections, and each states plainly where Yuno's claim is weak. If Prateek overrules the override, these are the only three defensible openings — and all three are **questions**, not assertions, because the one thing that would destroy credibility here is asserting a rail gap that turns out to be live in-app.

> **Insight #1: Hong Kong is funded by manual bank transfer while Singapore runs eGIRO — in their fastest-growing market**
> **Evidence:** **(S1)** Hong Kong is the #3 market at 7.60% of traffic and the fastest riser at **↑210.32%**, with AUM doubled and clients up ~4x in 2025 ([Capital HK](https://www.capital-hk.com/investment-strategy/StashAway012601)) + **(S4)** the dedicated HK "Deposits and Withdrawals" help centre documents **only** manual bank transfer from a licensed HK bank, with recurring pushed onto the client's own bank as a standing instruction, while Singapore has eGIRO, eGIRO FAST and PayNow ([HK](https://www.stashaway.hk/help-center/900005434863-how-do-i-fund-my-stashaway-account-and-what-are-the-financial-institutions-fi-you-accept-deposits-from), [SG](https://www.stashaway.sg/help-center/900000800423-how-do-i-deposit-funds-into-my-stashaway-account)) + **(S6)** they are visibly investing in HK, launching two new portfolios on 12 Mar 2026.
> **Pain Point:** Every HK deposit requires the client to leave the app, open their bank, enter a reference code and push funds — the exact friction Acme's Singapore work removed, cutting 2–4 business days to under 2 minutes. In a market growing 4x on clients, that friction scales with the growth.
> **Yuno Value Proposition:** One integration for local A2A and mandate rails across markets, so a rail that exists in one market does not need a separate per-market bank project to reach the next. **Honest caveat:** their lead bank HSBC already covers Hong Kong through Omni Collect, and Acme's coverage already lists Hong Kong — so Yuno is competing against two incumbents they already pay, not filling a vacuum.
> **Best Success Case:** **None appropriate.** No published Yuno case matches a licensed wealth manager collecting over domestic bank rails. Do not substitute a card-acceptance case.
> **Outreach Angle:** Ask, don't tell: whether Hong Kong is still on manual transfer while Singapore runs eGIRO, and what it would take to close that gap given HK is now their fastest-growing book.
> **Suggested Subject Line:** Hong Kong deposits vs Singapore eGIRO
>
> **Insight #2: A different funding rail, and a different vendor, in every market**
> **Evidence:** **(S3A)** four distinct named vendors across five markets — Acme (SG eGIRO, MY FPX integration), HSBC Omni Collect (MY lead collections bank), Lean (UAE Pay by Bank), Curlec (MY direct debit, 2020) plus an unnamed Thai FX vendor + **(S2)** five separate licensed entities under five different regulators, each with its own domain and its own bank relationship + **(S4)** five materially different rail sets, from eGIRO/PayNow in SG to a bare biller ID in Thailand.
> **Pain Point:** Each new market has meant a fresh bank integration, a fresh vendor contract and a fresh reconciliation path. Acme's own material describes the generic version of this cost: eGIRO portal setup alone is "easily 10–20 steps and several back and forths" across four roles, with implementation fees charged by both the banks and BCS.
> **Yuno Value Proposition:** Opportunity cost — engineering time spent on per-market bank plumbing is time not spent on portfolio products, which is where their revenue actually comes from. This argument is sharpened by **(S6)**: they cut ~20 product and engineering roles in Kuala Lumpur in July 2026, so in-house build capacity just shrank.
> **Best Success Case:** **None appropriate.**
> **Outreach Angle:** Note the observable structure — five entities, five domains, a different funding rail in each — and ask who carries the integration load now that the KL team is smaller.
> **Suggested Subject Line:** Five markets, five funding rails
>
> **Insight #3: They pay clients 0.15% to never miss a monthly deposit — and a missed one cancels the mandate**
> **Evidence:** **(S6)** "Regular Investing Advantage", launched April 2026, pays an extra **0.15% p.a.** on cash to clients who invest every single month ([Hubbis](https://www.hubbis.com/news/stashaway-says-first-half-revenue-rose-42-percent-as-singapore-business-turns-profitable)) + **(S5)** their own help centre documents that an underfunded eGIRO deposit fails, **the bank cancels the mandate**, and the bank "might charge a cancellation fee" ([src](https://www.stashaway.sg/help-center/15529112835353-what-happens-to-my-egiro-deposit-if-i-dont-have-sufficient-funds-in-my-bank-account)) + **(S4)** in HK, MY and TH recurring deposits live entirely at the client's own bank, where StashAway has **no visibility at all** into whether the instruction is still active.
> **Pain Point:** A single underfunded month costs the client their mandate, possibly a bank fee, and their 0.15% streak — and costs StashAway the recurring inflow it just paid to acquire. In three of five markets StashAway cannot even see the instruction, let alone retry it.
> **Yuno Value Proposition:** A unified view of failed and cancelled mandates across providers and markets, rather than per-vendor dashboards and bank-side instructions it cannot observe. **Honest caveat, and it is a big one:** this is a *bank-side mandate cancellation on an A2A debit*, so the standard recurring toolkit — network tokens, account updater, decline-code-aware retries, MIT flagging, local-acquirer routing — **does not apply.** What is left is visibility and mandate re-enrolment, which is a narrower claim than Yuno usually makes.
> **Best Success Case:** **None appropriate.**
> **Outreach Angle:** Their own documentation says a missed eGIRO deposit cancels the mandate at the bank. Since April they have been paying 0.15% for unbroken monthly investing — ask how they see a cancelled mandate in Hong Kong or Malaysia, where the instruction sits at the client's bank.
> **Suggested Subject Line:** When a missed deposit cancels the mandate

**Insight categories deliberately NOT used, and why — each would have been factually wrong:**
- ❌ *Cross-border inefficiency* — every market where they take money has a local entity and domestic rails (S2). There is no cross-border acquiring.
- ❌ *Regulatory acquiring gates* — they are licensed in all five operating markets. No gate is unmet.
- ❌ *Single PSP dependency* — they have four vendors, not one (S3A).
- ❌ *Approval rate optimization* — there are no card authorisations to approve or decline (S3A, S9).
- ❌ *Cost reduction via local acquiring* — they are already local everywhere, and there is no acquiring (S2, S3A).
- ❌ *PCI scope reduction* — they never touch card data, so there is no scope to reduce (S9).
- ❌ *Competitive urgency* — no competitor is on an orchestrator (S11C).
- ❌ *Expansion readiness* — no new market entered in 12 months (S6).

### Quick Hits: Ready-to-Use Sales Ammunition

⚠️ **Issued under protest.** These are grounded only in verified findings and are all phrased as questions. If the override stands, none of them should be sent.

**Email hooks (one sentence each):**
1. Your Singapore clients can set up an eGIRO mandate across eight banks, but your Hong Kong help centre still routes deposits through a manual bank transfer and a standing instruction at the client's own bank — in the market where your AUM doubled last year.
2. Five licensed entities, five country domains and, as far as I can tell from the outside, a different funding rail and a different vendor behind each one.
3. Since April you have been paying clients 0.15% a year to invest every month, while your own help centre warns that one underfunded month gets the mandate cancelled by their bank.

**Cold call openers (conversational, one sentence each):**
1. "I looked at how money actually gets into a StashAway account in each market, and Singapore and Hong Kong seem to work completely differently — is that still right?"
2. "You went live with FPX collections in Malaysia through HSBC and Acme this year — was Hong Kong meant to be next on that blueprint?"
3. "With the Kuala Lumpur product and engineering team smaller after July, who picks up the next market's bank integration?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| **Syfe** | syfe.com | Singapore | Not found | SG, HK, AU | **eGIRO, PayNow (QR + UEN), FAST, wire transfer, online remittance. No cards.** No orchestrator found | [Syfe help centre](https://help.syfe.com/hc/en-us/articles/4411625672473-What-are-the-funding-methods-available) `[UNVERIFIED — 403 on direct fetch]` |
| **Endowus** | endowus.com | Singapore | Not found | SG, HK | **FAST, PayNow (unique virtual account number), eGIRO, CPF, SRS. No cards.** Own-name accounts only. No orchestrator found | [Endowus help centre](https://help.endowus.com/hc/en-sg/articles/360000661013-How-do-I-transfer-cash-to-my-Endowus-account-SG) `[UNVERIFIED — 403 on direct fetch]` |
| **Autowealth** | autowealth.sg | Singapore | Not found | SG | Not found | TAL row only — unverified |
| **FSMOne** (iFAST) | fsmone.com | Singapore | Listed (iFAST Corp) | SG, HK, MY, CN | Not found | TAL row only — unverified |
| **Moomoo / Futu** | — | HK / SG | Listed (NASDAQ: FUTU) | SG, HK | **eGIRO collections confirmed** — named by Acme as having "introduced eGIRO collections to encourage recurring bank transfers to investment portfolios" | [Acme blog](https://www.tryacme.com/blog/egiro-the-hidden-promise-behind-near-term-challenges) |
| **Tiger Brokers** (Up Fintech) | — | SG | Listed (NASDAQ: TIGR) | SG, AU, NZ, MY | **eGIRO collections confirmed** — same Acme source | [Acme blog](https://www.tryacme.com/blog/egiro-the-hidden-promise-behind-near-term-challenges) |

> **This is the most important table in the report for the override.** Both of StashAway's closest direct competitors fund through the **identical rail set** — eGIRO, PayNow, FAST, bank transfer — and **neither accepts cards**. Two listed brokerage peers are on the **same eGIRO rail** via the same category pattern. **No card acceptance and no orchestrator anywhere in the comparison set.** This is a structural property of regulated investment platforms in Singapore, Malaysia and Hong Kong, not a StashAway-specific gap — so there is no competitive wedge, and no "your competitor already did this" urgency to create.

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Saxo Markets | — | Investment platform | SG, AU, HK | Multi-market licensed broker; bank-transfer funding; multi-currency FX leg | `accounts/apac-tal.csv` |
| Webull Singapore | — | Investment platform | SG | SG retail brokerage; same PayNow/FAST/eGIRO rail environment | `accounts/apac-tal.csv` |
| uSMART Securities | — | Investment platform | HK, SG | HK+SG dual market — the same HK rail question applies | `accounts/apac-tal.csv` |
| Longbridge | — | Investment platform | SG, HK | Same | `accounts/apac-tal.csv` |
| IG Markets Singapore | — | Investment platform | SG | Same | `accounts/apac-tal.csv` |
| Interactive Brokers Singapore | — | Investment platform | SG | Same | `accounts/apac-tal.csv` |
| PhillipCapital (POEMS) | — | Investment platform | SG | Incumbent SG broker; bank-rail funding | `accounts/apac-tal.csv` |
| Rakuten Trade | — | Investment platform | MY | Malaysia-only; the FPX/DuitNow question in its purest form | `accounts/apac-tal.csv` |

⚠️ **Payment stacks for 11B were NOT researched** — budget was spent on the target's own funding gate, which the brief ranked above everything else. All 11B rows are TAL leads requiring verification, not findings.

#### 11C. Companies Recently Adopting Payment Orchestration

*No public case studies found of direct competitors adopting payment orchestration.*

What was found instead is competitors adopting the **same bank-rail collections vendor and rail** — Moomoo, Tiger Brokers and StashAway all on eGIRO, per Acme. **That is vendor adoption on a domestic A2A rail, not payment orchestration, and it must not be scored or pitched as such.**

⚠️ **The brief's warning about Juspay on Indian investment-platform rows was checked and found not to transfer.** 13 Indian platforms on the TAL show `Juspay` (5paisa, Dhan, Upstox, smallcase, Paytm Money, Kotak Securities, Nuvama, Religare, Tickertape, Univest, Gullak, Aura Gold, Sahi), but **India is 1.58% of StashAway's traffic and StashAway holds no Indian entity, licence or product.** Those rows are weak evidence here and I have not used them. No Singapore, Malaysia or Hong Kong competitor was confirmed on any orchestrator, so the ICP row scores 0.

#### 11D. Prospect Scoring

Applied to the two closest competitors only, and only on verified signals. Both score low for **the same structural reason as StashAway**, which is itself the finding.

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| **Syfe — monthly transaction count** | ⬜ 0 | Not found; not researched | — |
| Syfe — orchestration status | ⬜ 0 | Uncertain; no orchestrator found, but not positively classified | Help centre `[UNVERIFIED]` |
| Syfe — 3+ countries | +3 | ✅ SG, HK, AU referenced | TAL + help centre |
| Syfe — multiple PSPs | ⬜ 0 | No PSP named; rails only | Help centre `[UNVERIFIED]` |
| Syfe — local rail gap in top-3 market | ❌ 0 | **Not met** — eGIRO, PayNow, FAST all present in SG | Help centre `[UNVERIFIED]` |
| Syfe — card acceptance | n/a | **None found** — same category property | Help centre `[UNVERIFIED]` |
| **Syfe subtotal** | **~3** | 🔴 Low | — |
| **Endowus — monthly transaction count** | ⬜ 0 | Not found; not researched | — |
| Endowus — orchestration status | ⬜ 0 | Uncertain | Help centre `[UNVERIFIED]` |
| Endowus — 3+ countries | ⬜ 0 | SG + HK only = 2 confirmed | TAL + help centre |
| Endowus — multiple PSPs | ⬜ 0 | No PSP named; rails only | Help centre `[UNVERIFIED]` |
| Endowus — local rail gap in top-3 market | ❌ 0 | **Not met** — FAST, PayNow, eGIRO, CPF, SRS all present | Help centre `[UNVERIFIED]` |
| **Endowus subtotal** | **~0** | 🔴 Low | — |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| — | **Syfe** | Direct competitor | SG, HK, AU | ~3 | 🔴 Low | Same bank-rail, no-card structure as StashAway | ✅ Yes |
| — | **Endowus** | Direct competitor | SG, HK | ~0 | 🔴 Low | Same | ✅ Yes |
| — | **Autowealth** | Direct competitor | SG | Not scored | 🔴 Low | SG-only, recurring contributions | ✅ Yes |
| — | **FSMOne** (iFAST) | Direct competitor | SG, HK, MY, CN | Not scored | ⬜ Unknown | Multi-market; listed parent | ✅ Yes |
| — | **Moomoo / Futu** | Peer | SG, HK | Not scored | ⬜ Unknown | eGIRO confirmed; listed | ✅ Yes |
| — | **Tiger Brokers** | Peer | SG, AU, NZ, MY | Not scored | ⬜ Unknown | eGIRO confirmed; listed | ✅ Yes |

> **I am not producing a padded Top 10.** Only six of these carry any verified signal, and the two I scored properly both land 🔴 Low for the same structural reason as the target. **Every company found is already on the TAL — there are no genuine new finds to report.**
>
> **⚠️ The real pipeline conclusion is a negative one, and it is worth more than a ranked list: the "Investment Platforms" segment in Singapore, Malaysia and Hong Kong looks systematically weak for Yuno.** Across StashAway, Syfe, Endowus, Moomoo and Tiger Brokers, the pattern is identical — licensed entity per market, domestic A2A and mandate rails, **no card acceptance**, no orchestrator, and funding-rail work bought from banks and specialist bank-connectivity integrators. **There are 63 Investment Platform rows on the TAL.** Before more research runs are spent on the SG/MY/HK subset, it is worth deciding whether the segment qualifies at all. The Indian subset is a genuinely different proposition — cards, UPI, Juspay incumbency, RBI e-mandate complexity — and that is where this vertical's real Yuno opportunity most likely sits.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | **US$13.1M FY2025** (+25% YoY), with a **pre-tax loss of US$11.7M** (widened 39%). **H1 2026 group net revenue SGD 11.5M** (~US$9M), **+42% YoY** | [Hubbis / Tech in Asia, Aug 2026](https://www.hubbis.com/news/stashaway-says-first-half-revenue-rose-42-percent-as-singapore-business-turns-profitable) |
| GMV / Gross Transaction Volume | **Not found.** Deposits, inflows and net new money are all explicitly **not disclosed** | Same source states "not disclosed" |
| AUM (stock, not flow) | **Not disclosed by the company.** Third-party claims conflict: "over SGD 4bn" (Jun 2026, review blog), "US$1.5bn" (older company announcement), US$1bn milestone ~2021. Independent cross-check: SGD 11.5m H1 → ~SGD 23m annualised ÷ 0.2–0.8% p.a. fee ⇒ **roughly SGD 3–7bn** `[ESTIMATE, not confirmed]` | [Hubbis](https://www.hubbis.com/news/stashaway-says-first-half-revenue-rose-42-percent-as-singapore-business-turns-profitable) · [fee band](https://www.stashaway.sg/pricing) |
| Average Transaction Value (USD) | **Not found.** Known anchors only: **no minimum deposit in SG** (S$10 recommended); **HKD 10,000 initial deposit in Hong Kong** `[UNVERIFIED — search summary only]`; AED 25,000 is the Lean same-day threshold in the UAE, not a minimum | [SG minimum](https://www.stashaway.sg/help-center/900000812086-is-there-a-minimum-deposit-or-fixed-amount-i-need-to-invest) |
| Est. Annual Transactions | **Cannot be computed.** Revenue ÷ ATV is invalid here — revenue is an **annual AUM fee**, not transaction-derived, so the standard formula would produce a meaningless number | — |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ~50,000–99,999/month. `[ASSUMPTION — not researched.]`**<br>**Billing unit counted: one client deposit / top-up into an investment account = one transaction.** Withdrawals are a separate flow and are not counted. StashAway's annual management fee is deducted from portfolio assets, **not collected over a payment rail**, so fee charges are not transactions in this sense.<br>**Basis for the assumption:** Google Play installs **1,071,465** across five markets `[SOURCED]`; **no minimum deposit in Singapore**, so deposits are frequent and small; **"Regular Investing Advantage" (April 2026) explicitly pays 0.15% p.a. for depositing every month** `[SOURCED]`, so recurring monthly deposits are a deliberately maximised share of flow; five markets with 4x client growth in Hong Kong in 2025 `[SOURCED]`. Installs materially overstate funded accounts (multi-market, lapsed, non-converting), so I have not scaled from them directly.<br>**Scored at the conservative band (+3), not the optimistic one.** A sourced figure could move this to +5 or below the 40,000 floor.<br>⚠️ **Per the disclosure rule, an assumed figure NEVER fires the under-40,000 auto-reject. No Phase 0 rejection is triggered.**<br>⛔ **Explicitly NOT derived from web traffic**, per Prateek's analyst note: the marketing ccTLDs are a thin front door and all deposit activity happens inside the logged-in app, invisible to SimilarWeb. | Mandatory disclosure rule, `research.md` |
| Active Customers / Users | **Not disclosed.** Only qualitative: a "substantial number" of clients hold **US$2m–US$10m**, and HNW is the fastest-growing segment. Proxies: **1,071,465 Play installs / 6.41K Play reviews**; SG App Store ~4.3 / ~996 ratings `[attribution uncertain — carousel noise]` | [Hubbis](https://www.hubbis.com/news/stashaway-says-first-half-revenue-rose-42-percent-as-singapore-business-turns-profitable) · [Play](https://play.google.com/store/apps/details?id=com.awp.stashaway) |
| Primary Currency | **USD is the investment currency** (US-listed ETFs). Deposit currencies: SGD + USD (SG), HKD + USD (HK), any → MYR → USD (MY), THB → USD (TH), AED (UAE) | Per-market help centres |
| Top 3 Markets by Revenue | **Not disclosed.** Only Singapore is broken out: EBITDA-positive two years running, profitable after tax in 2025, **18% EBITDA margin in H1 2026** (vs −8% a year earlier). By traffic the top 3 are SG, MY, HK | [Hubbis](https://www.hubbis.com/news/stashaway-says-first-half-revenue-rose-42-percent-as-singapore-business-turns-profitable) |
| Billing channel split (web vs app store) | ✅ **NOT APPLICABLE — and this is a positive finding.** Revenue is an **AUM management fee deducted from portfolio assets**, not an app-store in-app purchase. The `subscription-payments.md` §4 app-store trap — which can invalidate a consumer subscription account outright — **does not fire here.** The account is invalidated by the *absence of cards*, not by store billing | [pricing](https://www.stashaway.sg/pricing) |
| Other financials | Cash at end-2025 **US$12.1M**; net cash used in operations 2025 **US$6.8M**; FY2025 personnel **US$14.9M**, marketing **US$3.5M** (more than tripled); adjusted-EBITDA profitable ex-marketing as of Q2 2026; cumulative funding **"US$86.5 million invested in our team"** | [Hubbis](https://www.hubbis.com/news/stashaway-says-first-half-revenue-rose-42-percent-as-singapore-business-turns-profitable) · [About](https://www.stashaway.sg/about-us) |

---

### Overall Research Confidence

**Medium-High**, and unusually asymmetric — very strong exactly where the brief said the account would be decided, weak on commercial sizing.

**Traffic data was SUPPLIED**, not API-sourced and not estimated: `accounts/traffic/stashaway.md`, SimilarWeb, Jul–Sep 2026, supplied by Prateek 2026-10-13. It was used verbatim and not re-researched, per the method's resolution order. Because the country profile drives the APM analysis and two ICP signals, it matters that this is first-party supplied data rather than a `[ESTIMATE]` — the "high traffic outside home" row (+2) rests directly on it and is solid. The one real limitation is that **no absolute visit total was supplied**, so every "Est. Monthly Visits" cell is honestly empty.

**Strong coverage:**
- **The funding gate (Sections 3, 4, 12)** — the question the brief ranked above everything. Settled across all five markets from the companies' own help centres, with working controls, a nonsense-path 404 control, and both the `FAST` and `FPS` false-positive traps checked in both directions.
- **Legal entities and licences (Section 2)** — five entities, five regulators, five licence numbers, each from that market's own footer, with Singapore confirmed live against the MAS register. The Phase 0 "is it a payment licensee?" question is answered definitively: no.
- **Payment vendor stack (Section 3A)** — four named vendors with case-study and first-party evidence, including the Lean relationship named by StashAway itself.
- **Domain resolution (Section 1)** — all five ccTLDs resolved and redirect-tested; the `.com` redirect and the non-existence of `.com.my`, `.co.id` and `.id` established by test rather than assumption.
- **Competitive rail comparison (11A)** — the decisive evidence for the override.

**Limited coverage, and why:**
- **Commercial sizing (Section 12).** StashAway discloses no AUM, no client count and no deposit volume. The monthly transaction count is therefore an **assumption**, clearly labelled, and it is the single largest contributor to the computed score. This is the weakest load-bearing number in the file.
- **The Hong Kong rail question (Section 4).** Unresolved in both directions, and deliberately scored 0 rather than guessed, because the same evidence type demonstrably produced a false negative in Malaysia.
- **The UAE traffic collapse (Section 7).** Four causes ruled out; the actual cause not established.
- **The Indonesia traffic spike (Section 7).** Cause not established.
- **Section 8** is structurally incompletable — the deposit flow sits behind KYC-gated login in five jurisdictions.
- **Three key pages returned 403** to direct fetch (Syfe help centre, Endowus help centre, DFSA public register) and one returned 403 on a forum (Lowyat). Claims resting on them are labelled `[UNVERIFIED — search summary only, page not fetched]`.
- **11B payment stacks were not researched at all**, by deliberate choice of priority.

**Methodological disclosure (mandatory):** I had **no Agent/Task tool**, so Phases 1→2→3 were run **single-threaded** by one agent, with the per-agent search and fetch budgets treated as per-workstream totals. This is a declared deviation from the method's five-parallel-agent design. In practice the budget went disproportionately to the funding gate, which the brief ranked first; the visible cost is Section 11B.

---

### Manual Research Recommendations

> **Area:** Monthly transaction count (Section 12 and the ICP row that carries the score)
> **Why it matters:** It is the only signal that can reject the account outright, it is the single largest contributor to the computed 12/29, and it is currently an **assumption**. The entire band — and whether the account clears the 40,000 floor at all — rests on it.
> **Suggested manual action:** Ask for deposits per month per market on any first call. Failing that, the SG ACRA filing for Asia Wealth Platform Pte Ltd (201624878Z) and the Malaysian SSM filing for StashAway Malaysia Sdn Bhd (201701046385) may disclose client numbers or AUM; the Thai SEC also publishes private-fund AUM returns for licensed managers.

> **Area:** Hong Kong funding rails — FPS, autopay, eDDA (Section 4; the ⬜ local-rail ICP row)
> **Why it matters:** It is the only plausible rail gap in the account, in the #3 and fastest-growing market, and it is the entire basis of Insight #1. I scored it **0 rather than +3** precisely because I could not evidence it, so confirming it would raise the score to 15/29 — and refuting it would remove the last remaining angle.
> **Suggested manual action:** Open a Hong Kong account (or VPN into HK with an existing one) and walk the in-app deposit screen at `app.stashaway.hk`. **Do not rely on the help centre** — it returned a proven false negative for FPX in Malaysia.

> **Area:** Whether cards are accepted for *any* flow, anywhere (the override's reversal condition)
> **Why it matters:** This single fact decides whether the account is Low or viable. My evidence is strong but is drawn from help centres, which I have proven can be stale.
> **Suggested manual action:** Check the in-app deposit screen in each market for a card option, and check whether advisory or subscription-style fees (e.g. any StashAway Reserve or Corporate fee) are ever card-collected rather than deducted from AUM. One screenshot settles the account.

> **Area:** Current Malaysian direct-debit provider (Section 3A)
> **Why it matters:** Curlec is evidenced only as at July 2020. If Acme or HSBC has displaced it, the vendor count and the "multiple PSPs" +3 row change. Naming a six-year-stale vendor on a call would be an unforced error.
> **Suggested manual action:** Check the MY in-app recurring-deposit setup screen for the provider name, and the MY privacy policy's data-processor list.

> **Area:** The UAE traffic collapse (Section 7)
> **Why it matters:** 4.71% of traffic moved 85.69% and I could not establish why. It is also out of APAC territory, so it should probably just be excluded rather than explained.
> **Suggested manual action:** Low priority — the territory rule removes UAE volume from Prateek's number regardless. If curiosity persists, SimilarWeb's own paid/organic channel breakdown for `stashaway.ae` across the two periods would separate a marketing collapse from a measurement correction.

> **Area:** Segment-level qualification for the 63 TAL "Investment Platforms" rows (Section 11 pipeline note)
> **Why it matters:** This is the most valuable output of the run. If SG/MY/HK investment platforms systematically take no cards — and StashAway, Syfe, Endowus, Moomoo and Tiger Brokers all point that way — then further research runs on that subset will keep reaching this same conclusion.
> **Suggested manual action:** Spot-check the funding pages of three more SG/HK platforms (Moomoo SG, Webull SG, uSMART) for card acceptance. If all three are bank-rail-only, deprioritise the SG/MY/HK subset wholesale and concentrate the vertical's effort on the **Indian** rows, where cards, UPI, Juspay incumbency and RBI e-mandate complexity make a genuine orchestration case.

---

### Appendix: All Source URLs

**Section 1 — Traffic & domains**
- `accounts/traffic/stashaway.md` — SimilarWeb, supplied by Prateek 2026-10-13
- Redirect and byte-size tests run 2026-10-13 against `stashaway.com`, `stashaway.sg`, `stashaway.my`, `stashaway.hk`, `stashaway.ae`, `stashaway.co.th`, `stashaway.com.my`, `stashaway.co.id`, `stashaway.id`
- Nonsense-path control: https://www.stashaway.sg/zzz-nonsense-qwerty-12345 (404, 27,741 b)

**Section 2 — Entities & licences**
- https://eservices.mas.gov.sg/fid/institution/detail/201134-ASIA-WEALTH-PLATFORM-PTE-LTD
- https://www.stashaway.sg/help-center · https://www.stashaway.my/help-center · https://www.stashaway.hk/help-center · https://www.stashaway.ae/help-center · https://www.stashaway.co.th/help-center (entity footers)
- https://www.dfsa.ae/public-register/firms/stashaway-management-difc-limited (403 — unverified)

**Sections 3 & 4 — Payment stack & rails**
- https://www.tryacme.com/customer-stories-stashaway
- https://www.tryacme.com/case-study-stashaway
- https://www.tryacme.com/blog/egiro-the-hidden-promise-behind-near-term-challenges
- https://www.tryacme.com/ · https://www.tryacme.com/products/coverage
- https://www.stashaway.sg/help-center/900000800423-how-do-i-deposit-funds-into-my-stashaway-account
- https://www.stashaway.sg/help-center/360007398953-what-financial-institutions-do-you-accept-deposits-from
- https://www.stashaway.sg/help-center/900000812086-is-there-a-minimum-deposit-or-fixed-amount-i-need-to-invest
- https://www.stashaway.sg/help-center/14265575441817-whats-the-difference-between-egiro-deposit-and-manual-deposit
- https://www.stashaway.sg/help-center/14264118368025-which-banks-can-i-use-to-set-up-egiro-payments
- https://www.stashaway.sg/help-center/15529112835353-what-happens-to-my-egiro-deposit-if-i-dont-have-sufficient-funds-in-my-bank-account
- https://www.stashaway.sg/help-center/900000812866-what-currency-can-i-deposit-in-my-stashaway-account
- https://www.stashaway.sg/help-center/900000800563-how-do-i-make-changes-to-my-one-time-and-monthly-deposits
- https://www.stashaway.sg/help-center/14264012779161-egiro · https://www.stashaway.sg/help-center/egiro-fast
- https://www.stashaway.sg/help-center/regular-investing-advantage
- https://www.stashaway.my/help-center/115000365693-getting-started
- https://www.stashaway.my/help-center/900000950666-how-do-i-make-changes-to-my-one-time-and-monthly-deposits
- https://www.stashaway.my/help-center/900000970543-what-currency-can-i-deposit-in-my-stashaway-account
- https://www.stashaway.hk/help-center/900000697566-deposits-and-withdrawals
- https://www.stashaway.hk/help-center/900005434863-how-do-i-fund-my-stashaway-account-and-what-are-the-financial-institutions-fi-you-accept-deposits-from
- https://www.stashaway.hk/help-center/900005434803-how-do-i-make-changes-to-my-one-time-and-monthly-deposits
- https://www.stashaway.ae/help-center/19627951639961-fasttransfer
- https://www.stashaway.ae/help-center/19627971665177-what-is-fasttransfer-and-why-should-i-choose-it-over-a-manual-deposit
- https://www.stashaway.ae/help-center/19628542987417-which-banks-can-i-use-to-set-up-fasttransfer-payments
- https://www.stashaway.co.th/help-center/4405204491033-how-do-i-deposit-funds-into-my-stashaway-account
- https://www.stashaway.co.th/help-center/4405204265881-what-is-stashaways-biller-id
- https://www.stashaway.co.th/help-center/7740290910745-how-to-set-up-a-standing-instruction-for-dca-plan
- https://www.business.hsbc.com.my/en-gb/solutions/hsbc-omni-collect
- https://www.hsbc.com.my/ways-to-bank/online-banking/fpx/

**Section 5 — Complaints**
- https://vulcanpost.com/707206/stashaway-malaysia-users-direct-debit-issue/
- https://www.thestar.com.my/tech/tech-news/2020/07/29/stashaway-users-in-malaysia-affected-by-multiple-direct-debit-transactions-due-to-technical-issue
- https://ringgitplus.com/en/blog/investment/stashaway-to-prioritise-refunding-affected-users-after-direct-debit-mishap.html
- https://forum.lowyat.net/topic/4750563/+20 (403 — unverified)

**Sections 6, 7 & 12 — Corporate, news & financials**
- https://www.hubbis.com/news/stashaway-says-first-half-revenue-rose-42-percent-as-singapore-business-turns-profitable
- https://www.stashaway.hk/r/stashaway-hedge-fund-unicorn-top-20
- https://www.zawya.com/en/press-release/companies-news/stashaway-broadens-private-market-access-for-uae-based-hnwis-amid-strong-growth-otnms4yn
- https://www.capital-hk.com/investment-strategy/StashAway012601
- https://fintechnews.sg/50543/funding/stashaway-to-raise-us-25-million-in-series-d-funding-round-led-by-sequoia-capital-india/
- https://eightroads.com/en/news/stashaway-raises-25-million-in-series-d
- https://www.stashaway.sg/about-us · https://www.stashaway.sg/press · https://www.stashaway.sg/pricing · https://www.stashaway.sg/careers
- https://play.google.com/store/apps/details?id=com.awp.stashaway
- https://apps.apple.com/sg/app/stashaway-simple-investing/id1229966330
- https://appgallery.huawei.com/app/C100318407

**Section 11 — Competitors**
- https://help.syfe.com/hc/en-us/articles/4411625672473-What-are-the-funding-methods-available (403 — unverified)
- https://help.endowus.com/hc/en-sg/articles/360000661013-How-do-I-transfer-cash-to-my-Endowus-account-SG (403 — unverified)
- `accounts/apac-tal.csv` — Investment Platforms rows (63)

</details>
