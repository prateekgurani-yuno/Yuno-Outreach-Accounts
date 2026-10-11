# Salmon Group

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 8 / 29 → 🔴 Low
**Industry:** Consumer Finance — in-store POS lending, personal/motorcycle loans, rural banking & deposits · **HQ:** Manila, Philippines (operating); **Salmon Group Ltd is registered in ADGM, Abu Dhabi** — see the territory flag in Section 2 · **Researched:** 2026-10-11 · **First email sent:** —
**Motion:** In-house

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Salmon is a Philippine consumer lender built around in-store point-of-sale instalment credit — a Salmon Ambassador is physically stationed in a partner retailer, the shopper applies in about ten minutes with one government ID, and Salmon pays the merchant the full purchase amount the next day and holds the credit risk. It also owns **Salmon Bank (Rural Bank) Inc.**, a BSP-licensed rural bank (formerly Rural Bank of Sta. Rosa (Laguna), Inc., est. 1963, acquired Jan 2024, renamed 2025) which takes deposits at up to 8% p.a. and issues a Salmon Mastercard. Borrowers repay across 11+ named rails — in-app auto-debit, QR Ph, e-wallet and bank redirects, over-the-counter cash, and Salmon-as-a-biller inside GCash, Maya, ECPay and others.

**SimilarWeb total visits (last full month):** **Not shown** — the supplied pull reports country *shares* only, with no visit total and country rank reading `-` on every row. Source: **SimilarWeb (supplied 2026-10-11)**, `salmon.ph` **+2 domains**, Jul–Sep 2026, 41 countries.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇵🇭 Philippines | **77.93%** (audience 81.34%) · ▼41.62% QoQ | QR Ph (generate + scan-to-pay), in-app auto-debit on linked e-wallet/bank, e-wallet redirect, bank redirect, OTC cash by barcode/reference, biller inside GCash · Maya · Globe · BDO · PalawanPay · Cebuana Lhuillier · TrueMoney · Puregold · ECPay · ETap; Salmon-issued Mastercard | **None identified.** Every dominant Philippine consumer rail in `.claude/reference/apac-payments.md` §2 (GCash, Maya, InstaPay/PESONet bank transfer, OTC cash, cards) is present. | ✅ Salmon Bank (Rural Bank) Inc.; Salmon Finance Inc.; FHL Financing Company, Inc. |
| 2 | 🇷🇺 Russia | 5.09% | n/a — **not a market** | n/a | ❌ none |
| 3 | 🇯🇵 Japan | 3.18% | n/a — **not a market** | n/a | ❌ none |
| 4 | 🇰🇷 Republic of Korea | 1.86% | n/a — **not a market** | n/a | ❌ none |
| 5 | 🇺🇸 United States | 1.84% | n/a — **not a market** | n/a | ❌ none |

> 🛑 **Rows 2–5 are not markets and must not be treated as ones.** The supplied traffic file flags Russia (3-second visits, 1.13 pages, 92.98% bounce) and Japan (1-second visits, 1.03 pages, 94.83% bounce) as bot-shaped. Korea (5s, 1.53 pages) and the US (39s) are thin. Salmon sells in **one country**. Separately, I found first-hand corroboration for *why* the Russia and Georgia rows exist at all — see Section 1 of the research below.

### Legal entities
- **Salmon Bank (Rural Bank) Inc.** (Philippines) — formerly Rural Bank of Sta. Rosa (Laguna), Inc., est. 1963; BSP rural banking licence + Basic EPFS licence; PDIC-insured to ₱1M/depositor; AMLC-registered. Registered office: F. Gomez Street, Barangay Malusak, Santa Rosa City, Laguna.
- **Salmon Finance Inc.** (Philippines) — formerly Sunprime Financing (inc. 2 Oct 2019, renamed 11 Feb 2026). SEC Reg. No. **CS201916698**, Certificate of Authority No. **1241** (Online Lending Platform, trading as "LoanOnline").
- **FHL Financing Company, Inc.** (Philippines) — SEC Reg. No. **2022100071291-07**, C.A. **F-22-0038-29** (Oct 2022). "Service App only."
- **Salmon Group Ltd** (**Abu Dhabi, UAE — ADGM**) — formerly **Fintech Holdings Ltd**. Registered address per the IPOPHL trademark certificate: *"2475-2476 ResCo-work 09, 24, Al Sila Tower, ADGM Square, Al Maryah Island, Abu Dhabi, United Arab Emirates."* Owns and controls the Salmon App.

### Known PSPs
- **No third-party PSP, gateway, acquirer or orchestrator was found anywhere.** Not in the production CSP, not in the client web-app bundle, not in the T&Cs, not in the privacy policy, not in press. "Not established" is the correct answer — see Section 3A.
- **AllBank (A Thrift Bank), Inc.** — **QR Ph-P2M rail partner** `[Press Release]`, Salmon's own newsroom, 3 Apr 2024. The closest thing to a named payment provider in the whole account. Also an EMI-Bank on the current BSP register.
- **Electronic Commerce Payments, Inc. (ECPay)** — bills-payment aggregator, 490,000+ OTC and 3,000+ digital touchpoints `[Press Release]`, 25 Apr 2024.
- 🔴 A bills-payment aggregator probably sits behind part of the biller footprint, but **no vendor is named and I will not name one.** `[INFERENCE, not confirmed]`

### Orchestration status
**In-house orchestration layer — CONFIRMED, by Salmon's own words.** Salmon announced *"the completion of its **proprietary in-house payment orchestration platform**"* on **18 August 2025**, describing *"real-time routing, automatic fallbacks, and retries,"* a system that *"detects downtime or errors and switches instantly to alternative providers without any action from the customer,"* plus duplicate-charge prevention, timeout handling and ISO 20022-certified rails. Source: `https://salmon.group/tpost/salmon-upgrades-payment-backbone`.
Corroborated first-hand: `payments.salmon.ph` is live in the production Content-Security-Policy on `salmon.ph` alongside three non-production siblings (`payments.uat.fhl.world`, `payments.int-ra.uat.fhl.world`, `payments.loc.uat.fhl.world`), and responds behind a service-mesh authorization layer. `[Source Code]`
🔴 **This refutes the pre-research hypothesis of "+4 greenfield."** It is the single most consequential finding of this run.

### Buying signals
- 💰 **$100M raised, announced 20–21 April 2026** — $60M equity + $40M bonds at 102% of par / 13.7% effective yield under a $150M Nordic bond programme; oversubscribed; led by Spice Expeditions with WUSTL Investment Management, Moore Strategic Ventures and FJ Labs; prior backers IFC, ADQ/Lunate, Antler. ~$310M raised to date. ([fintech.global](https://fintech.global/2026/04/21/salmon-raises-100m-to-fuel-philippines-expansion/))
- 🚀 **"Daily Banking" payments build underway** — Salmon Bank *"plans to expand its offerings in 2026 with Daily Banking, which will integrate payments, cards, and transfers into the Salmon app."* ([salmon.group, 29 Oct 2025](https://salmon.group/tpost/salmon-bank-nearly-triples-deposits-and))
- 🤝 **QR Ph-P2M partnership with AllBank** and an **ECPay** bills-payment integration — both bilateral, both from Salmon's own newsroom.
- 🚩 **Credit-quality inflection, Q2 2026.** Gross NPL ratio **6.32%** (vs 2.34% at Q1 2026 and 2.10% at Dec 2025) and the gross loan portfolio **down 25.1% quarter on quarter**, per the BSP-mandated Published Balance Sheet. This is a *caution* signal as much as a buying signal — see Section 12.
- 📋 **No public payment-related RFP found.**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Salmon Group` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 8 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ⚠️ **NOT FOUND — ASSUMED ~170,000–290,000 repayment-collection events/month. [ASSUMPTION — not researched.]** Neither Salmon, its regulator nor any credible third party publishes a borrower count, loan-account count or repayment-event count. **Basis:** Salmon Bank's gross Total Loan Portfolio at 30 Jun 2026 is **₱3,426,514,104** (sourced, BSP Published Balance Sheet) and the flagship Product Loan runs **₱1,000–₱60,000** over **4–12 months** (sourced, `salmon.ph/product-loan` and `salmon.ph/merchants`). An average outstanding balance of ₱12,000–₱20,000 across a small-ticket in-store book implies ~171,000–286,000 live accounts; a monthly-amortising book bills **every account every month**. Salmon Finance Inc.'s separate book sits outside the bank's balance sheet and is additive. **Sensitivity:** the figure only drops below 100,000/month if the average outstanding balance exceeds ~₱34,000 — more than half the cap of a product that starts at ₱1,000. **This is an assumption and therefore CANNOT and DOES NOT trigger the under-40,000 rejection.** Billing unit stated in Section 12. |
| Orchestration status | **+1** | ✅ **In-house orchestration layer — confirmed.** Salmon publicly announced *"the completion of its proprietary in-house payment orchestration platform"* with *"real-time routing, automatic fallbacks, and retries"* that *"switches instantly to alternative providers"* ([salmon.group, 18 Aug 2025](https://salmon.group/tpost/salmon-upgrades-payment-backbone)); `payments.salmon.ph` confirmed live in the production CSP. **Not greenfield.** Hardest motion in the matrix. |
| 3+ countries | **0** | ❌ **Not met.** One market. Only two countries clear 1% traffic share besides the Philippines — **Russia 5.09% and Japan 3.18% — and both are bot-shaped** (3s/1s visit duration, 1.13/1.03 pages per visit, 92.98%/94.83% bounce). All three legal entities are Philippine; the fourth, Salmon Group Ltd, is an ADGM holding company, not an operating market. Awarding this row on junk traffic would be false. |
| Multiple PSPs | **0** | ⬜ **Uncertain → 0.** No third-party PSP or acquirer confirmed at all, let alone two. AllBank (QR Ph-P2M rail) and ECPay (bills-payment aggregator) are named and sourced but neither is a gateway/acquirer relationship, and there is no second of the same kind. |
| Local rail or licensing gap in a top-3 market | **0** | ❌ **Not met, and this is a positive finding about Salmon, not a gap.** Every dominant Philippine consumer rail is live: GCash, Maya, QR Ph (both directions), bank redirects, OTC cash, cards. There is no missing-rail story, and no regulatory acquiring gate — Salmon holds the local bank licence itself. Markets 2–5 are not markets. |
| Recent expansion | **0** | ❌ **Not met.** No new market entered in the 12 months to 2026-10-11. "Southeast Asia" / "500 million underserved customers" is stated ambition in every press release, not a launch. Branch and product expansion inside the Philippines is not market expansion. |
| Payment issues reported | **0** | ⬜ **Uncertain → 0.** Payment-*mechanics* complaints are real and sourced (payments not reducing the balance; collections chasing an already fully-paid item; absent payment reminders; small repayments flagged "suspicious" and the account restricted). But only a handful of reviews are retrievable without JS, against 158K Play ratings and 55K App Store ratings, so **frequency cannot be established** — and the loud, numerous complaints are about **interest rates, penalty fees and collections conduct**, which are lending-practice issues and are explicitly **not** scored here. |
| Funding >$10M | **+2** | ✅ **$100M announced 20–21 April 2026** ($60M equity + $40M bonds, 13.7% effective yield, within a $150M Nordic bond programme; oversubscribed). Within the 12-month window. ([fintech.global, 21 Apr 2026](https://fintech.global/2026/04/21/salmon-raises-100m-to-fuel-philippines-expansion/)) |
| High traffic outside home | **0** | ❌ **Not met — explicitly not awarded.** Philippines is **77.93%** of traffic and **81.34%** of audience, far above the 60% threshold on any reading. |
| Competitor using orchestration | **0** | ⬜ **No evidence found.** No Philippine consumer lender or BNPL was found running a third-party payment orchestrator. Home Credit Philippines collects through 15 individually named online channels and 39,000+ OTC partners with **no gateway, aggregator or orchestrator named** on its own payment pages. BillEase and Atome run the *opposite* pattern — they are distributed *as payment methods inside other PSPs' checkouts* (Xendit, PayMongo, Payrex, Maya Business). |
| Payment job postings | **0** | ⬜ **Not met in window.** `careers.salmon.ph` runs an Ashby ATS whose role list is JS-rendered and not retrievable here. The one payment-adjacent hire announcement I could source — Denis Padiarov as Head of Debit Products — is dated **3 May 2023**, well outside 12 months. |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **🔴 Low (8/29)**

**No public payment RFP was confirmed, so no RFP override applies.**

**Analyst override: none applied — and deliberately not applied upward.** The arithmetic and the judgement agree here, which is unusual and worth stating plainly. Salmon is a genuinely in-ICP company (it is a lender and a bank, not payment infrastructure — see the gate evidence below) that is nonetheless a **weak commercial target for Yuno**, for four independent reasons that do not overlap:
1. **It already built the product.** Salmon does not merely lack an orchestrator — it designed, shipped and now *markets* an in-house one, by name, as a competitive differentiator, with uptime and success-rate figures attached. The Phase 1 observation cannot be "you have no orchestration layer"; it would be factually wrong and would burn the thread.
2. **One market, no rail gap, no regulatory gate.** The two strongest and most common APAC orchestration triggers (`apac-payments.md` §1, §3) are both absent. Salmon holds the Philippine bank licence itself, so domestic acquiring is not gated for it.
3. **No PSP to displace and no second PSP to consolidate.** The collection estate is bilateral integrations to banks, wallets and biller networks — not a gateway stack.
4. **The one genuinely orchestratable surface is a payout leg, not a checkout.** Salmon pays merchants the full purchase amount next day, across 5,000–10,000 stores. That is real, but it is a disbursement/payout product conversation, not the core routing pitch.
I am **not** overriding downward either: the computed 🔴 Low already reflects reality. I am also **not** awarding the matrix's benefit of the doubt anywhere — five rows that a looser read could have scored (3+ countries, multiple PSPs, payment issues, competitor orchestration, payment hires) are scored 0.

### Source Notes
- ✅ **Salmon is NOT a BSP-registered Operator of Payment System.** 0 hits across all variants in the 314-entry register (`https://www.bsp.gov.ph/PaymentAndSettlement/cor.pdf`), sanity-checked against present known-good entries. Verified by the orchestrator; carried forward.
- ✅ **Salmon is NOT a BSP-supervised Electronic Money Issuer.** **Newly resolved in this run** — see Section 2 for the method and the sanity check.
- ✅ **In-house payment orchestration platform**, stated verbatim by Salmon, 18 Aug 2025. `[Press Release]` + `[Source Code]` corroboration.
- ✅ **AllBank (A Thrift Bank), Inc. is the named QR Ph-P2M partner.** `[Press Release]`, salmon.group, 3 Apr 2024.
- ✅ **Salmon Bank's quarterly Published Balance Sheets** (BSP-mandated, signed by Georgy Chesakov, President & CEO) decoded for Q4 2025, Q1 2026 and Q2 2026. Every column sum-verified, and each filing's "previous quarter" column matches the prior filing's "current quarter" column exactly — so the figures below are internally and serially consistent.
- 🔴 **CORRECTION, carried prominently: `Salmon_IPO_Registration.pdf` is NOT an IPO filing.** "IPO" is the **Intellectual Property Office of the Philippines**. The document is trademark registration **4/2024/00522723** for the mark "SALMON FINANCE MADE EASY", filed 17 Aug 2024, registered 2 Nov 2024, 10-year term. **It contains no financial, borrower or loan-book data of any kind.** It does disclose that the registrant is **Salmon Group Ltd (formerly Fintech Holdings Ltd), of ADGM, Abu Dhabi**.
- ⚠️ **Do not read the trademark's Nice Class 36 wording as a description of Salmon's business.** It recites *"exchanging money, electronic funds transfer, processing of credit card and debit card payments, issuance of travellers' cheques"* — that is standard Class 36 boilerplate claimed to protect the mark, **not evidence that Salmon processes payments for third parties**, and it must never be quoted as such. It would be the single easiest way to mis-reject this account.
- ⚠️ **Card issuer not machine-readable.** The Salmon Access Card T&Cs are legible enough to confirm the card is *"a physical and/or virtual payment instrument issued by [issuer] pursuant to a licen[c]e from MasterCard International, which is regulated by the Bangko Sentral ng Pilipinas (BSP)"*, but the issuer's name sits in a 14-font subset encoding this environment could only partially decode. A BSP-regulated group entity is the only candidate set; **Salmon Bank is the obvious inference but it is `[INFERENCE, not confirmed]`.** No issuer processor is named.
- ⚠️ **No BSP primary text on what a Basic EPFS licence permits was obtained**, and nothing in this report rests on one. Per the standing instruction, no Philippine regulatory rule is cited from memory anywhere in this file.
- ⚠️ **Discrepancy, Salmon's own site, both live today:** `salmon.ph/merchants` FAQ says *"over 5,000 partner stores"*; `salmon.ph/product-loan` says *"Available in over 10,000 stores across the Philippines."* **I quote the 5,000 figure where a number is needed**, because it appears in the merchant-facing FAQ that also describes the commercial terms. Both URLs are cited.
- ⚠️ **Discrepancy, stale entity credit:** `salmon.ph/howtorepay` still credits *"Sunprime Finance, Inc."* in its LoanOnline disclaimer while the page's own footer says *"Salmon Finance, Inc."* This is residue from the 11 Feb 2026 rename, **not a second entity**.
- ⚠️ **Discrepancy, founding date:** July 2022 (press releases) vs October 2022 (elsewhere); Sunprime incorporated 2019; the bank dates to 1963. **"Founded 2022" refers to the brand only.**
- ⚠️ **Discrepancy, FY2024 baseline:** the 29 Jul 2025 press release says the bank *"grew total assets by 43% to ₱1.8 billion in the first half of 2025, compared with year-end 2024"* and that net loans grew *"from ₱909 million to ₱1.2 billion."* Those do not reconcile with the Published Balance Sheet series, which puts total assets at ₱2.70bn and net loans at ₱1.60bn as at 30 Sep 2025. The press basis is not stated. **I use the Published Balance Sheets, not the press releases, for every balance-sheet figure.**
- ⚠️ **The "+2 domains" in the SimilarWeb pull are not named in the screenshot and I could not confirm them.** Best-evidenced candidates and the contamination consequence are in Section 1.
- ⚠️ **No PSP is named for Salmon's collections anywhere.** This is the correct, evidenced answer, not a gap in the search.
- 🚩 **Near-miss already cleared, not re-flagged:** the footer line about Salmon Group Ltd offering *"platform-as-a-service"* names only its own subsidiaries (Salmon Finance Inc., FHL Financing Company, Inc.). Intra-group. The same logic clears the in-house orchestration platform — see Section 2.

### Success Case Alternatives
- **No Yuno customer case study with a matching profile was located in this run**, and I will not name one on a guess. The profile that would actually match is specific and narrow: a **domestic-only consumer lender collecting monthly amortising repayments across a biller/OTC/wallet estate, with an existing in-house routing layer it is not looking to replace**. If such a reference exists it should be surfaced by the AE before any call, because this account's objection will be *"we built this and we publish our uptime"* — and only a reference that beats an in-house platform on reach or payout breadth will move it.
- ⚠️ Per the standing rule: no Yuno customer is named here, and no metric is attached to any customer.

---

## Executive Summary

Salmon Group is a Philippine consumer lender and rural-bank owner whose core product is in-store point-of-sale instalment credit at over 5,000 partner retailers, funded by deposits at up to 8% p.a. and by a $150M Nordic bond programme, with ~$310M raised to date including a $100M round announced in April 2026. Its payment surface is genuinely large and genuinely interesting — a monthly-amortising loan book collected across 11+ named rails including QR Ph, in-app auto-debit on linked wallets and banks, OTC cash, and Salmon-as-a-biller inside GCash, Maya, ECPay and others. **The decisive finding is that Salmon has already built this: on 18 August 2025 it publicly announced "the completion of its proprietary in-house payment orchestration platform," with real-time routing, automatic fallback and retry across providers, and markets it as a differentiator** — which I corroborated first-hand by finding `payments.salmon.ph` live in the production CSP. No third-party PSP, gateway, acquirer or orchestrator exists anywhere in the account. The motion is therefore **in-house**, the hardest in the matrix, and it is compounded by a single market with no rail gap and no regulatory acquiring gate: **8/29, 🔴 Low**.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** **Path 1 — pasted SimilarWeb data supplied by Prateek**, transcribed at `accounts/traffic/salmon-group-philippines.md`. Cited as **SimilarWeb (supplied 2026-10-11)**. Scope `salmon.ph` **+2 domains**, "include all country domains" ON, period **Jul–Sep 2026**, 41 countries. **Not re-researched.** ⚠️ **No total visit count is shown and country rank reads `-` on every row**, so this section can report shares and engagement only — not absolute volume. Nothing in this report derives a transaction count from traffic.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | 🇵🇭 **Philippines** — high priority | **77.93%** (audience 81.34%) | **Not shown** | ▼ **41.62%** QoQ — unexplained | SimilarWeb (supplied 2026-10-11) |
| 2 | 🇷🇺 Russia — **bot-shaped, discount** | 5.09% | Not shown | ▲47.19% | SimilarWeb (supplied 2026-10-11) |
| 3 | 🇯🇵 Japan — **bot-shaped, discount** | 3.18% | Not shown | ▼79.13% | SimilarWeb (supplied 2026-10-11) |
| 4 | 🇰🇷 Republic of Korea — thin | 1.86% | Not shown | ▲2.91% | SimilarWeb (supplied 2026-10-11) |
| 5 | 🇺🇸 United States | 1.84% | Not shown | ▲26.91% | SimilarWeb (supplied 2026-10-11) |
| 6 | 🇦🇺 Australia — thin | 0.86% | Not shown | ▲83.34% | SimilarWeb (supplied 2026-10-11) |
| 7 | 🇪🇸 Spain | 0.72% | Not shown | ▼100.00% — **artefact, unusable** | SimilarWeb (supplied 2026-10-11) |
| 8 | 🇬🇪 Georgia | 0.72% | Not shown | ▲>5,000% — **artefact, unusable** | SimilarWeb (supplied 2026-10-11) |
| 9 | 🇰🇿 Kazakhstan | 0.65% | Not shown | ▼100.00% — **artefact, unusable** | SimilarWeb (supplied 2026-10-11) |
| 10 | 🇨🇦 Canada | 0.63% | Not shown | ▲32.18% | SimilarWeb (supplied 2026-10-11) |
| 11 | 🇮🇳 India | 0.54% | Not shown | ▲47.49% | SimilarWeb (supplied 2026-10-11) |

**Markets above 5% share:** Philippines (77.93%) and Russia (5.09%). **Only the Philippines is a real market.**

**Engagement, which is what decides this table:**

| | 🇵🇭 Philippines | 🇷🇺 Russia | 🇯🇵 Japan |
|---|---|---|---|
| Visit duration | **02:23** | **00:03** | **00:01** |
| Pages / visit | **2.94** | **1.13** | **1.03** |
| Bounce rate | **48.73%** | **92.98%** | **94.83%** |

A one-second, single-page visit that bounces 95% of the time is a crawler signature, not a prospective borrower. Per the supplied file's own instruction: **no Japan or Russia line is built on these rows.**

#### 🔎 New finding — why the Russia and Georgia rows exist at all

This was not supplied; I found it first-hand. The production `Content-Security-Policy` header on `https://salmon.ph/howtorepay` explicitly whitelists Google's **Russian and Georgian** country endpoints in both `img-src` and `connect-src`, alongside Philippine and Singaporean ones:

> `*.google.ru www.google.ru *.google.nl www.google.nl *.google.com.ph www.google.com.ph *.google.ge www.google.ge`

The same policy whitelists **`rick.ai`**, a Russian-language marketing-analytics vendor, in `script-src` and `connect-src`. Salmon's founders (Pavel Fedorov, George/Georgy Chesakov, Raffy Montemayor) are named in its own releases as banking and fintech veterans from "various parts of the world," and the group's internal engineering domain is `fhl.world`.

**Reading:** the Russia (5.09%) and Georgia (0.72%, ▲>5,000%) rows are far better explained by Salmon's own team, staging and ad/analytics infrastructure than by Filipino-market demand. `[INFERENCE, not confirmed]` — the CSP proves the configuration, not the origin of the sessions. **Either way the conclusion is identical: these are not prospects, and the "3+ countries" ICP row is correctly scored 0.**

#### 🔎 The "+2 domains" — identified as far as the evidence allows, and the contamination is real

The screenshot does not name them. Every host referenced anywhere on `salmon.ph`, `salmon.group`, `moto.salmon.ph` and `careers.salmon.ph`, plus the production CSP and the client web-app bundle, yields exactly **three** non-`salmon.ph` root domains in the Salmon estate:

| Root domain | What it is | Verified |
|---|---|---|
| **`salmon.group`** | Corporate / press-room / investor-facing site. HTTP 200. | ✅ fetched |
| **`slmn.ph`** | Asset and document host. Root 404s; `s.slmn.ph` serves every legal PDF and financial statement, `web.slmn.ph` is a CSP-referenced app host. | ✅ fetched |
| **`fhl.world`** | Internal engineering domain — `web.uat.fhl.world`, `cdn.fhl.world`, `payments.uat.fhl.world`, `api.pos.fhl.world`. Not consumer-facing. | ✅ seen in CSP + app bundle |

**Most likely "+2": `salmon.group` and `slmn.ph`** — the two public-facing root domains. `[INFERENCE, not confirmed]` — the SimilarWeb screenshot does not name them and I could not verify the pull's composition.

> 🚩 **The traffic profile IS contaminated, and this conclusion does not depend on which two domains were added.** Everything below rolls into `salmon.ph` at root-domain level:
> - **`careers.salmon.ph`** — a recruitment site running the **Ashby** ATS (`*.ashbyhq.com`, `*.ashbyprd.com` in its CSP). Job-seeker and recruiter traffic from anywhere on earth, with no relationship to Philippine borrower demand. This alone can distort a country split.
> - **`moto.salmon.ph`** — a motorcycle-loan storefront with its own backend and CDN.
> - **`merchant.salmon.ph`** and **`merchant-application.salmon.ph`** — the merchant-acquisition funnel, i.e. retailers, not borrowers.
> - **`client.salmon.ph`** and **`app.salmon.ph`** — the authenticated borrower web app (an S3/CloudFront React SPA).
> - **`cdn.salmon.ph`** (2,638 references across four pages) and **`s.slmn.ph`** — pure asset/CDN hosts.
>
> **Consequence:** the 77.93% Philippine share and the ▼41.62% QoQ fall mix at least five functionally different audiences — borrowers, merchants, job applicants, and asset requests. **The country split should not be treated as a borrower-demand measurement, and the QoQ fall cannot be attributed to any one cause from this data.** The supplied file's instruction to establish *why* Philippine traffic fell 41.62% stands, and Section 12 now gives it a second, independent data point to test against.

**Flagged top-10 countries with no local entity:** Russia, Japan, Korea, US, Australia, Spain, Georgia, Kazakhstan, Canada, India — all of them. **None is a market and none creates a cross-border exposure**, because Salmon does not sell in any of them.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Manila, Philippines (operating; "more than 120 professionals in its Manila office" as at May 2023, per Salmon's own release). Brand founded **July 2022**. Group holding company **Salmon Group Ltd** is registered in **ADGM, Abu Dhabi, UAE**.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| 🇵🇭 Philippines | **Salmon Bank (Rural Bank) Inc.** — formerly Rural Bank of Sta. Rosa (Laguna), Inc., est. 1963; acquired Jan 2024 (59.7% controlling stake), renamed 2025. BSP rural banking licence; Basic EPFS licence; PDIC-insured to ₱1M/depositor; AMLC-registered. | BSP-licensed (register link published by Salmon); Amended AOI and AMLC registration published as PDFs | `salmon.ph/salmonbank`; `s.slmn.ph/docs/bank/Amended_AOI_Salmon_bank_Rural_Bank_Inc.pdf`; `s.slmn.ph/docs/bank/AMLC_Registration_Salmon%20Bank.pdf`; audited FS name the registered office as F. Gomez St., Brgy. Malusak, Santa Rosa City, Laguna |
| 🇵🇭 Philippines | **Salmon Finance Inc.** — formerly Sunprime Financing, inc. 2 Oct 2019, renamed 11 Feb 2026. SEC financing company; SEC Online Lending Platform ("LoanOnline"). | SEC Reg. **CS201916698**, C.A. **1241** | `salmon.ph/our-story`; `salmon.ph/howtorepay` footer; `s.slmn.ph/docs/Sunprime_Finance_Inc_Certificate_of_Incorporation_and_Authority_to_Operate_as_a_Financing_Company.pdf` |
| 🇵🇭 Philippines | **FHL Financing Company, Inc.** (Oct 2022) — "Service App only" | SEC Reg. **2022100071291-07**, C.A. **F-22-0038-29** | `salmon.ph/our-story`; `s.slmn.ph/docs/our_story/FHL_Services_Inc_SEC_Certificate_of_Incorporation.pdf` |
| 🇦🇪 UAE (ADGM) | **Salmon Group Ltd** — formerly **Fintech Holdings Ltd**. Owns and controls the Salmon App; controlling shareholder of Salmon Bank. | Trademark registrant of record, IPOPHL Reg. **4/2024/00522723** | `s.slmn.ph/docs/our_story/Salmon_IPO_Registration.pdf` (decompressed and read in this run) |

#### 🚩 Territory flag — raise this before any outreach, do not bury it

`CLAUDE.md` is explicit: *"Gulf markets (UAE, Saudi) are out of territory — they sit with EMEA. An APAC-HQ'd company selling into the Gulf is still in scope; a Gulf-HQ'd company is not."*

**The group holding company, Salmon Group Ltd, is registered in ADGM, Abu Dhabi** — verified from the IPOPHL trademark certificate, which gives its address as *"2475-2476 ResCo-work 09, 24, Al Sila Tower, ADGM Square, Al Maryah Island, Abu Dhabi, United Arab Emirates."* It is also the entity that owns and controls the Salmon App and that signs the Salmon App General Terms and Conditions (dated 17 June 2026).

**My read, offered as a judgement rather than a fact:** this is a **holding-company domicile, not an operating HQ**. The operating business is 100% Philippine — three Philippine licensed entities, every customer, every transaction, every branch, Philippine governing law and exclusive Philippine court jurisdiction in the T&Cs, a Manila office, and ADQ (Abu Dhabi's sovereign wealth fund) as an investor rather than a market. On substance this is an APAC account. **But the entity that would sign a Yuno contract may well be the ADGM company, and that is an EMEA-territory question, not mine to settle.** ⚠️ **Confirm territory ownership with the APAC/EMEA split before Prateek invests outreach cycles in this account.** This was not flagged in the Phase 0 gate and it should have been.

#### 🔑 The ICP gate, restated with the new evidence

The gate verdict — **IN ICP, Salmon is a lender and a bank, not payment infrastructure** — holds, and this run adds two independent confirmations on top of the BSP OPS register.

**Confirmation 1 — the EMI register, newly resolved (this was the one open disqualifying test).**

`https://www.bsp.gov.ph/Lists/Directories/Attachments/7/emi.pdf` — **"List of BSP Supervised Electronic Money Issuers (EMIs) As of 31 May 2026"**. Retrieved with WebFetch (BSP resets curl), FlateDecode streams decompressed in Python (`pdftotext` is not installed), non-printables stripped, letter-spacing collapsed, searched with `LC_ALL=C grep -a`.

| Entity / variant | On the EMI register? |
|---|---|
| **Salmon · Salmon Bank · Salmon Finance · Sunprime · Sta. Rosa · FHL · Fintech Holdings · slmn** | **0 hits, every variant** |
| **PDAX** — *rejected Philippine precedent* | ✅ **"Philippine Digital Asset Exchange, Inc.", EMI-NBFI #25** |
| **DCPAY Philippines, Incorporated** — *Coins.ph* | ✅ EMI-NBFI #5 |
| Maya Philippines · AIPH Merchant Services (Alipay PH) · Paynamics · Starpay · TrueMoney PH · ShopeePay PH · Cebuana Lhuillier Services · AllEasy · G-Xchange · Wise Pilipinas · I-Remit · TagCash · TayoCash · Toktokwallet | ✅ all present |
| **Toyota Financial Services Philippines Corporation** | ✅ **present as EMI-NBFI #35** |
| "Rural Bank" entries among the **29 EMI-Banks** | **4** — Cebuana Lhuillier Rural Bank, Dungganon Bank (A Microfinance Rural Bank), Netbank (A Rural Bank), Rural Bank of Guinobatan |
| **AllBank (A Thrift Bank), Inc.** — *Salmon's QR Ph partner* | ✅ **EMI-Banks #2** |

🔑 **The zero is sanity-checked, not an artefact.** Twenty-plus known-good entities return hits from the same decoded text, including both rejected Philippine precedents. And the absence is a **real negative, not a category exclusion**: rural banks are eligible (four are listed), thrift banks are eligible (AllBank is listed), and — most directly on point — **a consumer finance company is eligible, because Toyota Financial Services Philippines Corporation is on the register.** Salmon is not.

**Verdict: 🟢 NOT a BSP-supervised Electronic Money Issuer, as of 31 May 2026, from BSP's own current register. The last open disqualifying test is closed.** (Noted for completeness: even an EMI licence covering only Salmon's *own* wallet would have been the CoinSpot pattern and non-disqualifying. It does not arise.)
⚠️ A third-party Scribd re-upload of a September 2024 snapshot exists. **It was not used and should not be.**

**Confirmation 2 — the in-house orchestration platform does not make Salmon payment infrastructure, and here is why.**

This is the one genuinely new near-miss this run produced, so it gets answered rather than waved at. Salmon announcing a "proprietary in-house payment orchestration platform" sounds, on its face, like the exclusion list. It is not, on four grounds:

1. **It collects Salmon's own receivables.** Salmon's own words: it *"supports all transactions across Salmon — including loan repayments, deposits, and fund transfers."* Not third-party volume.
2. **Nothing is sold from it.** No API, no SDK, no developer documentation, no pricing, no sandbox, no partner tier — I looked. `api-merchant.salmon.ph` and `api.pos.fhl.world` are its own in-store POS and merchant-portal backends, reached only by Salmon's own clients, all behind service-mesh authorization.
3. **The regulator agrees.** An entity operating a payment system *for others* in the Philippines appears on the OPS register. Salmon does not, across all variants, in a 314-entry register that does contain 2C2P, Maya, G-Xchange, PayMongo, DragonPay, Xendit, Coins.ph and PDAX.
4. **It is exactly the CoinSpot pattern** this repo already settled: infrastructure built for the company's own consumer products, with nothing a third party can buy. The test is what a third party can buy. From Salmon: a loan, a deposit, a card. Nothing payments-related.

**Commercially this is the opposite of a disqualification — it is the reason the account is hard.** Salmon has built and now publicly markets the capability Yuno sells.

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| 🇵🇭 Philippines | ✅ #1, 77.93% | ✅ **Yes — three licensed entities incl. a BSP-licensed bank** | **No — Salmon holds the local bank licence itself** | **None.** 100% domestic collection in PHP. |
| 🇷🇺 Russia | ✅ #2 (bot-shaped) | ❌ | n/a | **None — not a market.** |
| 🇯🇵 Japan | ✅ #3 (bot-shaped) | ❌ | Not applicable — no operations | **None — not a market.** |
| 🇰🇷 Korea | ✅ #4 (thin) | ❌ | Not applicable — no operations | **None — not a market.** |
| 🇦🇪 UAE (ADGM) | ❌ | ✅ Salmon Group Ltd (holding only) | n/a | **Territory-ownership question, not a payments one.** See the flag above. |

**No cross-border warning is issued for any market**, and the standard "potential cross-border operation" language is deliberately *not* used here. It would be wrong. Salmon is a single-market domestic lender that holds its own banking licence — structurally the least cross-border-exposed profile in this repo. The APAC reference's strongest argument (§3: *"Regulatory gating is the third and strongest"*) has no purchase on this account.

> **MANUAL:** Confirm which entity would contract — Salmon Group Ltd (ADGM) or a Philippine subsidiary — and therefore which Yuno territory owns the account.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| 🇵🇭 Philippines | **No third-party PSP, gateway or acquirer identified.** Not established. | `[Source Code]` + `[Terms/Privacy Policy]` + `[Press Release]` — exhaustive negative, method below | — |
| 🇵🇭 Philippines | **AllBank (A Thrift Bank), Inc.** — **QR Ph-P2M provider.** *"AllBank will extend the reach of its QR Ph-P2M system to merchants and customers"*; Salmon repayments generate a QR Ph code in-app which the borrower uploads to any wallet or bank app. | `[Press Release]` | `https://salmon.group/tpost/syeud5cse1-the-salmon-group-partners-with-allbank-t` (3 Apr 2024) |
| 🇵🇭 Philippines | **Electronic Commerce Payments, Inc. (ECPay)** — bills-payment aggregator; *"490,000+ over-the-counter and 3,000+ digital payment touchpoints"*, incl. convenience stores, pawnshops, remittance centres and rural banks. | `[Press Release]` | `https://salmon.group/tpost/51evppz8m1-salmon-expands-payment-channels-with-ecp` (25 Apr 2024) |
| 🇵🇭 Philippines | **Bilateral repayment channels, named by Salmon:** M Lhuillier, SM Bills Payment Centers (SM Stores), **UnionBank**, **BPI**, **RCBC**, plus pre-existing 7-Eleven and Cebuana Lhuillier (5,500 stores). *"+3,070 new in-person repayment locations, a 56% increase."* Online repayment redirects the borrower to the partner bank's own page for login + OTP. | `[Press Release]` | `https://salmon.group/tpost/tv5v7v7vl1-salmon-simplifies-loan-repayment-for-its` (29 Aug 2023) |
| 🇵🇭 Philippines | **Auto-debit partners:** **GCash, Maya, UnionBank, BPI** — borrower links the account to the Salmon app; Salmon notifies before the due date and debits on it. | `[Press Release]` | `https://salmon.group/tpost/52pc5j9h81-salmon-introduces-auto-debit-for-seamles` (29 Jun 2024) |
| 🇵🇭 Philippines | **Salmon as a biller:** GCash · Maya · Globe · BDO · PalawanPay (apps); Cebuana Lhuillier · TrueMoney · Puregold (stores/pawnshops/supermarkets); **ECPay · ETap** (self-service kiosks). **₱18 commission applies on this route.** | `[Checkout]` (public repayment page) | `https://salmon.ph/howtorepay` |
| 🇵🇭 Philippines | **Mastercard International** — card scheme licence for the Salmon Access Card (physical + virtual). **Issuer name not machine-readable**; T&Cs state the issuer *"is regulated by the Bangko Sentral ng Pilipinas (BSP)."* No issuer processor named. | `[Terms/Privacy Policy]` | `https://s.slmn.ph/docs/Salmon_Card_Terms_and_Conditions.pdf` |

**How the negative was established — five independent checks, each of which would have caught a PSP:**

1. **Production CSP header** on `https://salmon.ph/howtorepay`, read with `curl -D`. `connect-src`, `script-src` and `frame-src` enumerate **every** host the page may talk to, and they are exhaustive by construction. Every payment-related host is **first-party**: `payments.salmon.ph`, `offers-api.salmon.ph`, `api-merchant.salmon.ph`, `dictionaries.salmon.ph`, `confirmations.salmon.ph`, `ml-risks-salmon-score-api.*`, plus their `*.uat.fhl.world` / `*.tech.fhl.world` siblings. The only third parties present are analytics and advertising: Google, TikTok, Meta, LinkedIn, Reddit, Taboola, IntentIQ, Sentry, OneLink, `rick.ai`, `webhook-n8n.*`. **Not one PSP, gateway, acquirer or orchestrator domain.** Confirmed identically on `salmon.group`, and on `moto.salmon.ph` (which additionally names its own `moto-salmon-ph-backend.salmon.ph`).
2. **Borrower web-app bundle** — `https://client.salmon.ph/static/js/main.49353ba7.js`, 1.52MB decompressed, grepped raw (not extracted text). Every API host is first-party: `auth-api.salmon.ph`, `sapp-api.salmon.ph`, `operations-api.salmon.ph`, `data-collector.salmon.ph`, `auth.salmon.ph`, `api.pos.fhl.world`, `pos-api.int-ra.tst.fhl.world`. Third parties: Amplitude, Sentry. **No PSP SDK of any kind.** The repayment flow in the bundle generates a QR Ph code for the borrower to upload to GCash, Maya "or any other bank app" — *"Download this QR Ph code on your device's photo gallery"*, *"Use the app's QR payment feature to upload or scan the saved QR Ph code and complete the payment"*.
3. **Terms & Conditions** — Salmon App General T&Cs (17 June 2026, 93 sections) read in full. **No payment processor, gateway or aggregator named.** Governing law and exclusive venue: the Philippines.
4. **Privacy policy** — `salmon.ph/privacy-policy` is a directory of ten entity-specific privacy notices. **No processor is named on the index.** ⚠️ The individual notice PDFs were not opened; APAC merchants do name processors in privacy notices more often than in press, so this is the one remaining stone — see Manual Research Recommendations.
5. **Press, 2023–2026** — Salmon's own newsroom names rail and channel partners freely (AllBank, ECPay, M Lhuillier, SM, UnionBank, BPI, RCBC, 7-Eleven, Cebuana Lhuillier, GCash, Maya). **It has never named a PSP**, and in August 2025 it explained why: it built the layer itself.

> **The headline answer: there is no PSP behind Salmon's collections. Not "not found" — not present.** Salmon reaches banks, wallets and biller networks through its own payments service, and the QR Ph leg runs through **AllBank**, a BSP-licensed thrift bank and EMI, rather than through a gateway. Salmon Bank being itself a BSP-licensed institution is the plausible reason no acquirer is needed for the rails it touches directly `[INFERENCE, not confirmed — no BSP primary text on QR Ph participation eligibility was obtained, and none is cited here]`. **Do not name a vendor in any outreach.**

#### 3B. Payment Orchestrator

**Classification: 🔵 In-house orchestration layer.** `[Press Release]` + `[Source Code]`

The standard "no public evidence found" language does **not** apply and must not be used for this account. There is direct, first-party, unambiguous evidence. From `https://salmon.group/tpost/salmon-upgrades-payment-backbone`, Manila, **18 August 2025**, verbatim:

> *"Salmon Group Ltd today announced the completion of its **proprietary in-house payment orchestration platform**, which now powers transactions across its lending and savings products."*
>
> *"The platform delivers **99.9% uptime and a 99% success rate on QR Ph payments**…"*
>
> *"The infrastructure supports all transactions across Salmon — including loan repayments, deposits, and fund transfers — **connecting to a wide network of local banks, e-wallets, and payment providers**."*
>
> *"**Unlike a standard payment gateway, the platform uses real-time routing, automatic fallbacks, and retries** to maintain transaction reliability during network issues or downtime. **It detects downtime or errors and switches instantly to alternative providers without any action from the customer**, so payments 'just work' with no need to retry or wait for resolution."*
>
> *"The platform's **auto-debit capability is paired with advance reminders and multiple payment attempts**, reducing missed payments…"*
>
> *"As one of the **early adopters of QR Ph** in the Philippines, Salmon offers both **scan-to-pay and generate-QR** options in-app…"*
>
> *"…the system includes **duplicate charge prevention, timeout handling, and ISO 20022-certified payment rails**…"*
>
> *"**Owning its payment infrastructure** lets Salmon continuously optimize for customer experience and operational efficiency."*

Corroborated independently and first-hand: **`payments.salmon.ph` is live**, declared in the production CSP `connect-src` of both `salmon.ph` and `salmon.group`, and returns a service-mesh authorization denial to an unauthenticated request — i.e. a real, running, access-controlled service, not a placeholder. It is accompanied by three non-production environments (`payments.uat.fhl.world`, `payments.int-ra.uat.fhl.world`, `payments.loc.uat.fhl.world`), which is what a maintained internal platform looks like rather than a one-off script.

> *"In-house orchestration layer. The hardest sell in the matrix. Salmon has not merely failed to buy orchestration — it has built it, named it, measured it and published the numbers. Argue reach, payout breadth and opportunity cost. **Never argue that they need orchestration.**"*

**What this means for the motion, concretely:**
- ❌ **Do not** open on routing, failover, retries, cascading or smart routing. Salmon's own press release claims all five by name, with figures.
- ❌ **Do not** open on "you have no orchestration layer." It is factually false and will end the thread, exactly as `apac-payments.md` §4 warns for Juspay accounts — except here the incumbent is the prospect itself, which is worse.
- ✅ The only honest openings are **reach Salmon's own platform was not built for** (international PSP/APM breadth if and when it leaves the Philippines), **merchant payout breadth** across 5,000–10,000 stores, and **engineering opportunity cost** — every quarter spent maintaining four environments of a payments platform is a quarter not spent on credit and deposits. All three are weak against a company that treats owning this as strategy.

> **MANUAL:** Walk the authenticated app repayment flow with DevTools, which is the only way to see whether `payments.salmon.ph` fans out to third parties behind the scenes. The public evidence cannot resolve what sits *behind* the in-house layer.

---

### Section 4: Alternative & Local Payment Methods

Checked for the Philippines (77.93%) against `.claude/reference/apac-payments.md` §2. **No other country clears 1% on non-bot traffic, so no other market is researched** — per the method's instruction not to research regions with no real traffic.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| 🇵🇭 PH | **QR Ph** — generate-QR in-app **and** scan-to-pay | Bank transfer / A2A | **Active in checkout** | `salmon.ph/howtorepay`; app bundle strings; `salmon.group/tpost/salmon-upgrades-payment-backbone` |
| 🇵🇭 PH | **In-app auto-debit** on a linked e-wallet or bank account (GCash, Maya, UnionBank, BPI named) | Direct debit / mandate | **Active in checkout** | `salmon.ph/howtorepay`; `salmon.group/tpost/52pc5j9h81-salmon-introduces-auto-debit-for-seamles` |
| 🇵🇭 PH | **GCash** — auto-debit, QR Ph scan, and as a biller | Digital wallet | **Active in checkout** | `salmon.ph/howtorepay` |
| 🇵🇭 PH | **Maya** — auto-debit, QR Ph scan, and as a biller | Digital wallet | **Active in checkout** | `salmon.ph/howtorepay` |
| 🇵🇭 PH | **Bank app redirect** (login + OTP at the bank's own page) — UnionBank, BPI, RCBC, BDO named | Bank transfer / A2A | **Active in checkout** | `salmon.ph/howtorepay`; `salmon.group/tpost/tv5v7v7vl1-salmon-simplifies-loan-repayment-for-its` |
| 🇵🇭 PH | **Over-the-counter cash** by barcode / reference number — 7-Eleven, Cebuana Lhuillier, M Lhuillier, SM Bills Payment, Puregold, TrueMoney, ECPay (490,000+ touchpoints), ETap kiosks, PalawanPay | Cash / voucher | **Active in checkout** | `salmon.ph/howtorepay`; ECPay release |
| 🇵🇭 PH | **Globe** (telco app, as a biller) | Carrier / biller channel | **Active in checkout** | `salmon.ph/howtorepay` |
| 🇵🇭 PH | **Salmon Access Card — Mastercard**, physical + virtual, 0.5% cashback on QR and card spend | Cards | **Active** (Salmon is the *issuer*, not the acceptor) | `s.slmn.ph/docs/Salmon_Card_Terms_and_Conditions.pdf` |
| 🇵🇭 PH | **Instalments** — the entire product. Product Loan ₱1,000–₱60,000 over **4–12 months**, 0%–70% down payment; Credit Line to ₱250,000; Moto loans | BNPL / Instalments | **Active — this IS the product** | `salmon.ph/product-loan`; `salmon.ph/merchants` |
| 🇵🇭 PH | **Card acceptance for repayment** (pay your loan by card) | Cards | **Not found** | — |
| 🇵🇭 PH | **ShopeePay · GrabPay** as repayment channels | Digital wallet | **Not found** | — |
| 🇵🇭 PH | **Apple Pay / Google Pay** | Digital wallet | **Not found** | — |
| 🇵🇭 PH | **Online-checkout / e-commerce integration** (Salmon as a payment method at a third-party online checkout) | BNPL | **Not found — and deliberately absent.** 0 hits across `salmon.ph` for `e-commerce`, `online checkout`, `Shopee`, `Lazada`, `TikTok Shop`, against **28 hits for "in-store"**. | `salmon.ph` (grepped) |

> **No "warning" is issued for this market, and that is itself the finding.** Every rail the APAC reference flags as worth checking for the Philippines — *"GCash, Maya, InstaPay/PESONet bank transfer, over-the-counter cash, cards"* with the note that *"GCash is close to table stakes for consumer flows"* — is present and live. Salmon's repayment estate is **broader than most merchants' entire checkouts**: 5 in-app methods plus 11 named biller destinations. **The local-rail ICP row is correctly scored ❌ 0, because there is no gap to sell against.**

**Two structural notes that matter more than any single rail:**
- **Salmon charges the borrower nothing in-app** (*"No hidden fees — Transparent repayments without additional processing fees"*; *"Instant payment processing — All payments are posted in real-time"*) but **₱18 on the biller route**. That ₱18 is the only visible unit economic in the whole collection estate, and it is the one number a cost conversation could anchor on.
- **Salmon charges the merchant nothing at all**, and positions explicitly against PSPs: *"You'll get paid upfront, while we handle the loan, collections, and all fees — unlike other providers that may charge you up to 2%."* `salmon.ph/merchants`. **Lending economics, not payment economics** — which is why the ICP gate passes and why a cost-of-acceptance pitch has nothing to attach to.

> **MANUAL:** Use a VPN to verify the authenticated app repayment sheet from a Philippine IP. The public page lists the methods; only the app shows ordering, defaults and failure handling.

---

### Section 5: Payment Issues & Customer Complaints

⚠️ **Read the separation rule before reading the table.** Philippine lending apps attract very large review volumes, and most of it concerns interest rates, penalties and collections behaviour. **Those are lending-practice issues, not payments findings, and they are listed separately below and excluded from scoring.** Only payment-*mechanics* failures belong in the first table.

**A. Payment-mechanics complaints (relevant to Yuno)**

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| **Payments not reducing the balance** — *"imbis na mabawasan yung balance pag nagbayad ka"* (Tagalog: "instead of the balance going down when you pay"), reviewer says the balance kept growing | Apple App Store (PH) | **Cannot establish** — 1 retrievable instance | 19 Apr (year not shown on page) | `https://apps.apple.com/ph/app/salmon-finance-made-easy/id6446115147` |
| **Collections chasing an already-settled account** — *"still following up on payment for an item that I already fully paid"* — a reconciliation / payment-posting failure, distinct from the conduct complaint in the same review | Apple App Store (PH) | **Cannot establish** — 1 retrievable instance | 30 Jan (year not shown) | `https://apps.apple.com/ph/app/salmon-finance-made-easy/id6446115147` |
| **Payment delays** — *"there were some delays at first"*; developer replied and the reviewer reports it resolved | Apple App Store (PH) | **Cannot establish** — 1 retrievable instance | 8 Apr (year not shown) | `https://apps.apple.com/ph/app/salmon-finance-made-easy/id6446115147` |
| **No payment reminders → missed due dates** — *"There are no payment reminders, so it's easy to miss your due date."* 🚩 **Directly contradicts Salmon's own 18 Aug 2025 claim** that *"auto-debit capability is paired with advance reminders and multiple payment attempts."* | Google Play (PH) | **Cannot establish** — 1 retrievable instance | undated on page | `https://play.google.com/store/apps/details?id=com.fhl.salmon` |
| **Small repayments flagged as "suspicious"; account restricted** — *"they flagged my account for 'suspicious' multiple small payments to them, and restricted my account and demanded an explanation… They should not allow small flexible payments to them if they will flagged it as 'suspicious'."* A **false-positive risk-engine decline on inbound repayments** | Google Play (PH) | **Cannot establish** — 1 retrievable instance | undated on page | `https://play.google.com/store/apps/details?id=com.fhl.salmon` |

**B. Lending-practice complaints — recorded for context, explicitly NOT scored as payment issues**

| Issue | Platform | Source |
|---|---|---|
| High interest and penalty fees on late payment; *"even if you pay the full interest, they would still add up amounts with bigger interest and hidden fees"*; *"They don't even give options for you to pay in installment!"* | Apple App Store, Google Play | as above |
| Unexpected ₱199 card charge on a card expected to be free | Apple App Store | as above |
| **Collections conduct** — representatives *"disrespected the people inside the house"* | Apple App Store | as above |
| A long defensive review explaining that complainants confuse a term loan with a revolving credit line | Google Play | as above |

**Aggregate app metrics (sourced, and a growth signal in their own right):**

| | Google Play (`com.fhl.salmon`) | Apple App Store (`id6446115147`) |
|---|---|---|
| Rating | 4.8 | 4.8 |
| Ratings / reviews | **158K reviews** | **55K ratings** |
| Downloads | **5M+** | not shown |
| Seller / developer | — | **Salmon Group Ltd** |
| Last updated | **8 Oct 2026** | 24 Sept, v2.42.1 |

Against Salmon's own **18 Aug 2025** figures of *"15,000+ ratings"* (App Store) and *"56,000+ ratings"* (Google Play), ratings have grown roughly **3.7×** and **2.8×** in about fourteen months. Both stores still read 4.8.

**Frequency assessment — and why the ICP row scores 0.** Five distinct payment-mechanics failure modes are confirmed, every one with a source, and two of them (payments not reducing the balance; collections chasing a settled account) are exactly the reconciliation failures orchestration is supposed to prevent. **But five reviews against 213,000 ratings is not a frequency measurement**, and both stores paginate reviews behind JavaScript that this environment cannot execute. Per the matrix's own rule — *uncertain = 0, mark ⬜* — the row scores **0**. Awarding +2 here would be reading a pattern into a sample of five.

> *"Pattern of payment-posting and reconciliation failures in the Philippines suggests a settlement-reconciliation and retry-visibility opportunity — but the sample is five reviews and the frequency is NOT established. Do not use the word 'pattern' in outreach on this evidence."*

⚠️ **One finding here is genuinely usable even at n=1**, because it is a self-contradiction rather than a complaint: Salmon publicly claims *"advance reminders"* as a feature of its platform, and a borrower publicly says there are none. That is checkable in a discovery call without accusing anyone of anything.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | **20–21 Apr 2026** | **$100M raised** — $60M equity + $40M bonds at 102% of par, 13.7% effective yield, under the existing $150M Nordic bond programme. Oversubscribed. Equity led by **Spice Expeditions**, with **WUSTL Investment Management, Moore Strategic Ventures, FJ Labs**. Prior: **IFC, ADQ/Lunate, Antler, Argentem Creek Partners**. ~**$310M** raised to date. | **Funding** | `https://fintech.global/2026/04/21/salmon-raises-100m-to-fuel-philippines-expansion/` · `https://salmon.group/tpost/salmon-group-raises-usd-100-million` |
| 2 | **17 Mar 2026** | **Salmon Bank FY2025 results** — customer base **doubled**; deposits **3.9×**; loan portfolio **2.3×**; NIM **40%**; **total assets 2.3× to ₱4.4bn**; gross NPL **2%**; equity being raised to **₱1.6bn** via a **₱400M** injection from Salmon Group Ltd, completing April 2026. | Funding / Results | `https://salmon.group/tpost/salmon-bank-doubles-customer-base-and-grows` |
| 3 | **5 Feb 2026** | **Client base doubled in 2025**, driven by time deposits; **~85% of depositors are affluent clients**, mostly time-deposit holders. "Bank on Eight" promo — **8% p.a. on ≥₱1,000,000**, 1–5 year terms, running **1 Dec 2025 – 1 Jun 2026** (DTI Fair Trade Permit No. FTEB-242399 Series of 2025). | Results / Product | `https://salmon.group/tpost/salmon-banks-client-base-doubles-in-2025` |
| 4 | **29 Oct 2025** | **Q3 2025** — deposits and equity nearly tripled YoY; loan portfolio **+40%+ QoQ**; CAR 3× the BSP requirement. Reported a **99% payment success rate** and 4.8 app-store rating. 🚀 **"Salmon Bank plans to expand its offerings in 2026 with Daily Banking, which will integrate payments, cards, and transfers into the Salmon app."** | Results / **Payment platform roadmap** | `https://salmon.group/tpost/salmon-bank-nearly-triples-deposits-and` |
| 5 | **18 Aug 2025** | 🔵 **Completion of the proprietary in-house payment orchestration platform.** 99.9% uptime, 99% QR Ph success rate, real-time routing, automatic fallback, retries, duplicate-charge prevention, ISO 20022-certified rails. | **Payment Infrastructure** | `https://salmon.group/tpost/salmon-upgrades-payment-backbone` |

**Earlier, for the payments timeline:** 29 Jul 2025 H1 2025 bank results (total assets +43% to ₱1.8bn, ROE 58.9%, ROA 24.9%, CAR 32.7%, equity 2.7× to ₱707M, deposits +66.7% to ₱952M, net loans ₱909M→₱1.2bn) · Jun 2025 $88M (US$60M bond drawdown + US$28M equity, $150M three-year Nordic framework) · Sep 2025 $50M oversubscribed Nordic tap (Roschier reports USD 110M total via a USD 60M initial issue plus a USD 50M tap; **Pareto Securities sole bookrunner**) · Oct 2024 Series A-2 $30M · 2 Nov 2024 IPOPHL trademark 4/2024/00522723 registered · Jan 2024 59.7% of Rural Bank of Sta. Rosa acquired · 18 Apr 2024 Sunprime loan accounts transferred to the bank · Apr 2024 AllBank QR Ph and ECPay partnerships · Apr 2024 Series A-1 $25M · Oct 2022 Series A $16M · 2023 $20M debt from Argentem Creek Partners.

**No public payment-related RFP found.**

**Payment-related hiring:** the only sourceable payment-adjacent appointment is **Denis Padiarov as Head of Debit Products, 3 May 2023** (`https://salmon.group/tpost/74bnrcxna1-salmon-builds-its-debit-products-team`) — **outside the 12-month window**, so the ICP row scores 0. `careers.salmon.ph` runs an **Ashby** ATS whose role list is JavaScript-rendered and not retrievable in this environment; **a live role list could change this row** and is in Manual Research Recommendations. Other sourceable appointments from the newsroom slugs (not individually fetched, so `[UNVERIFIED — newsroom index only]`): a CTO appointment (Boris Voskresenskii), a Security Operations lead, a Corporate Development chief, and Franchette Chingcuanco.

**Licence activity:** no new licence application found in the window. The group's existing licences — BSP rural banking + Basic EPFS (Salmon Bank), SEC financing company × 2, SEC Online Lending Platform — are all pre-window, and **neither an OPS nor an EMI registration exists**, which is the point of Section 2.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | **18 Aug 2025** | **"Salmon upgrades payments backbone to support growing customer base"** — completion of a proprietary in-house payment orchestration platform with real-time routing, automatic fallback and retries across providers. | 🔵 **Decisive.** Sets the motion to in-house and caps the orchestration ICP row at +1. | `https://salmon.group/tpost/salmon-upgrades-payment-backbone` |
| 2 | **29 Oct 2025** | **"Daily Banking" announced for 2026** — will *"integrate payments, cards, and transfers into the Salmon app."* | 🚀 A payments build is underway. The only live window where an external platform conversation is even timely. | `https://salmon.group/tpost/salmon-bank-nearly-triples-deposits-and` |
| 3 | **25 Apr 2024** | **"Salmon Expands Payment Channels with ECPay Partnership"** — 490,000+ OTC and 3,000+ digital touchpoints. *"half of whom don't have a traditional bank account."* | Cash is structural, not legacy. Half the borrower base is unbanked. | `https://salmon.group/tpost/51evppz8m1-salmon-expands-payment-channels-with-ecp` |
| 4 | **3 Apr 2024** | **"The Salmon Group Partners with AllBank to Launch the QR Ph Payment Method"** — AllBank extends its **QR Ph-P2M** system; borrower generates a QR Ph code in the Salmon app and uploads it to any wallet or bank app. | The single named payment-rail provider in the entire account. | `https://salmon.group/tpost/syeud5cse1-the-salmon-group-partners-with-allbank-t` |
| 5 | **29 Jun 2024** | **"Salmon Introduces Auto-Debit"** — links GCash, Maya, UnionBank or BPI to the Salmon app; pre-due-date notification, automatic debit on the due date, push/SMS confirmation. *"With the expanding range of partner banks…"* | Mandate-style recurring collection, built bilaterally bank by bank. The scaling cost of that approach is the only credible wedge. | `https://salmon.group/tpost/52pc5j9h81-salmon-introduces-auto-debit-for-seamles` |

**No provider removal found.** No evidence that Salmon has discontinued any payment channel or provider. The direction of travel is additive throughout 2023–2026 (5,500 → +3,070 locations → ECPay's 490,000 → biller listings in ten+ apps and networks).

⚠️ **One partnership is NOT confirmed current:** the **SM Store** partnership rests on a February 2023 release. It is not referenced on any page fetched today, and the merchants page's named testimonials are Nhadz Thaiparts, D' Exclusive Shoppe and Dan J Moto instead. **Do not state that Salmon is live in SM Store.** The **FC Home Center** rollout (targeting 106 stores) is likewise unverified as complete.

---

### Section 8: Checkout Experience Audit

⚠️ **Framing note before the table.** Salmon **has no checkout** in the sense this section assumes. There is no online cart, no payment page, no guest/account decision and no card-entry form — because the loan is originated **in a physical store by a Salmon Ambassador**, and the only payment flow Salmon operates is **inbound repayment collection** inside an authenticated app. The table below therefore audits the **repayment flow**, and says so. Auditing a checkout that does not exist would be the easiest way to put fiction in this file.

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | **No online checkout exists.** Origination is in-store, human-assisted, ~10 minutes, one government ID, approval in 10 seconds–1 minute. Repayment is **custom-built, first-party, in-app**, served by `payments.salmon.ph`. | — | Custom-built. Not hosted, not embedded, no PSP page. |
| Guest checkout | **N/A.** Repayment requires an authenticated Salmon account — except the **biller route**, which works from inside GCash/Maya/BDO/ECPay etc. using only a phone number or the 10/12-digit loan agreement number. | Good | The biller route *is* effectively guest repayment, and it is the broadest channel. |
| Steps to complete payment | In-app: select product → *"Go to Payment"* → choose method. QR Ph route adds: generate code → save to gallery → open wallet/bank → upload or scan. | Fair | The QR-Ph-via-photo-gallery hop is a real friction point and Salmon documents it as the normal path. |
| Card input experience | **No card-entry surface found anywhere.** Salmon *issues* a Mastercard; it does not accept cards for repayment. | — | Nothing to assess; nothing to tokenize. |
| Payment methods visible | 5 in-app (auto-debit, QR Ph, e-wallet redirect, bank redirect, OTC barcode/reference) + 11 named biller destinations. | **Good** | Unusually broad for a single-market lender. |
| Location-based method display | **N/A** — one country. | — | |
| Instalment / EMI options | **The product is instalments.** ₱1,000–₱60,000 over 4–12 months, 0%–70% down. Credit Line to ₱250,000. | **Good** | Present exactly where expected. |
| 3DS implementation | **Not detected / not applicable** — no card acceptance. | — | No 3DS surface. |
| PCI indicator | **No card acceptance ⇒ no acquirer-side PCI surface.** Card *issuing* carries its own obligations; no public documentation. | — | See Section 9. |
| Mobile responsiveness | App-first by design: iOS, Google Play and **Huawei AppGallery** (`appgallery.huawei.com/app/C108007333`). 5M+ Play installs. *"More than 80% customers use Salmon app for payments"* (Aug 2023). | **Good** | Correct posture for the market. |
| Multi-currency / local pricing | **PHP only.** Card T&Cs specify a credit limit *"in PHP funds."* | — | No FX leg anywhere. |
| Saved payment methods | **Yes** — auto-debit persists a linked e-wallet or bank account as a standing mandate. | **Good** | Bilateral, per institution. |
| Error message clarity | Not assessable unauthenticated. The app bundle contains a dedicated `"[Browser] Qr Repayment Error"` event and `PaymentError_Opened` / `PaymentSuccess_Opened` / `PaymentOptions_Tap` analytics events, so failures are instrumented. | **Unknown** | Instrumented, which is a good sign; the copy itself is unseen. |

**Full repayment flow not accessible** — it sits behind authentication and a Philippine phone number. Findings above are limited to publicly observable elements, the production CSP, and the unauthenticated client bundle.

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **No direct PCI compliance documentation found publicly for Salmon.** "PCI" returns **0 hits** across every `salmon.ph` page fetched. | `salmon.ph` (grepped) |
| Card data handling | **No card acceptance surface exists**, so there is no acquirer-side SAQ to classify. Salmon is a card **issuer** (Salmon Access Card, Mastercard licence, physical + virtual) — a different obligation set entirely, undocumented publicly. | `s.slmn.ph/docs/Salmon_Card_Terms_and_Conditions.pdf` |
| Security certification actually held | **ISO/IEC 27001:2022**, *"ISO-certified with over 30 security controls."* Plus two-step verification on account creation **and on making a payment**, 24/7 fraud monitoring, device biometrics and encryption. | `salmon.ph/security` |
| Recommended Yuno integration | **Not applicable on the collection side** — there are no card-not-present card payments to route. If anything were ever relevant it would be **back-to-back API** for payouts and A2A, not an SDK. | — |

**No inference about reduced PCI scope is drawn**, because the condition for drawing one (Section 3 confirming a tokenized PSP checkout) is not met — there is no PSP and no card checkout. Nothing here supports a PCI-scope-reduction pitch, and attempting one would signal that the account was not read.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: Salmon already built and publicly markets what Yuno sells — the opening observation must start from that, or the thread is over**
> **Evidence:** **S3B** — Salmon's own 18 Aug 2025 release announces *"the completion of its proprietary in-house payment orchestration platform"* with *"real-time routing, automatic fallbacks, and retries"* that *"switches instantly to alternative providers"* (`https://salmon.group/tpost/salmon-upgrades-payment-backbone`) + **S3A** — `payments.salmon.ph` live in the production CSP with three non-production siblings, and **zero** third-party PSP, gateway or orchestrator domains anywhere in `connect-src`, `script-src` or `frame-src`.
> **Pain Point:** Not a payments gap — an **ownership cost**. Salmon maintains four environments of a payments platform, bilateral integrations to GCash, Maya, UnionBank, BPI, RCBC, BDO, AllBank, ECPay, ETap and others, plus the reconciliation and retry logic behind them, with an engineering team that it could instead be pointing at credit models and deposit products. Every new rail is a new integration it owns forever.
> **Yuno Value Proposition:** The only honest one is **substitution of ongoing integration and maintenance burden**, not capability. Yuno does not give Salmon routing it lacks; it would give Salmon the option to stop building and maintaining rail connections one at a time.
> **Best Success Case:** **None in this repo matches, and I am not naming one.** The required reference is a company that replaced a *working, publicly marketed* in-house orchestration layer — a much narrower and much harder reference than a greenfield or displacement case. If the AE cannot produce one, this insight should not be led with.
> **Outreach Angle:** Credit them explicitly for the platform and the published 99.9% uptime / 99% QR Ph success rate, then ask the only question the press release leaves open: how many engineer-weeks a new rail costs them, now that the biller footprint is at eleven destinations and Daily Banking is adding cards and transfers.
> **Suggested Subject Line:** "Your 99% QR Ph success rate — and the cost of rail number twelve"

> **Insight #2: The merchant payout leg, not the checkout, is the only unclaimed payments surface in the account**
> **Evidence:** **S2/S4** — Salmon pays the merchant *"the full purchase amount by the next day"* across *"over 5,000 partner stores"* (`salmon.ph/merchants`; `salmon.ph/product-loan` says over 10,000 — **discrepancy flagged**), charging the merchant **nothing** and positioning against PSPs: *"unlike other providers that may charge you up to 2%"* + **S3B** — Salmon's own description of its platform covers *"loan repayments, deposits, and fund transfers"*, and every public claim about it (uptime, QR Ph success rate, routing, fallback) is about **inbound collection**. **Outbound merchant disbursement is never mentioned.**
> **Pain Point:** Thousands of next-day payouts to small retailers — motorcycle dealers, appliance shops, parts stores — across a long tail of banks and wallets. Next-day is a settlement promise, and a promise at that scale carries failed-payout handling, bank-detail validation, and reconciliation per store. This is the part of the estate where Salmon has published nothing.
> **Yuno Value Proposition:** Payout orchestration and reach — multiple payout rails with failover and automated retry, so a missed next-day settlement to a dealer is handled by the platform rather than by operations.
> **Best Success Case:** **Not identified in this run.** The matching profile is a marketplace or lender with high-frequency, small-value domestic payouts to a long tail of SME counterparties. ⚠️ No Yuno customer is named and no metric is attached to one.
> **Outreach Angle:** Their merchant page promises the full purchase amount the next day at zero cost to the store, which is the hardest promise in the whole model — and the one thing their payments-platform announcement never mentions.
> **Suggested Subject Line:** "Next-day settlement to 5,000 stores — what happens when one fails?"

> **Insight #3: Q2 2026 is a credit-quality inflection, and it changes the conversation from growth to reliability-under-pressure**
> **Evidence:** **S12** — Salmon Bank's BSP-mandated Published Balance Sheet at **30 Jun 2026**: gross Total Loan Portfolio **₱3,426,514,104, down 25.1%** from ₱4,576,492,489 at 31 Mar 2026; **gross NPL ratio 6.32%**, up from 2.34% (Q1 2026) and 2.10% (Dec 2025); ROE **(8.16%)** and ROA **(1.97%)**; allowance for credit losses **₱804,297,074 = 23.5% of the gross book**; cash at BSP **tripled** to ₱4,295,357,359 while deposits grew **37%** to ₱6,280,830,541 (`s.slmn.ph/docs/bank/Q2_2026_published_balance_sheet.pdf`, cross-validated against the Q1 2026 and Q4 2025 filings) + **S1** — Philippine web traffic **down 41.62% quarter on quarter** in the Jul–Sep 2026 SimilarWeb pull.
> **Pain Point:** Two independently sourced declines pointing the same way — the loan book contracting while deposits pile up at the central bank is the signature of **deliberate origination tightening**, not a data artefact. A lender retrenching on credit does not buy new infrastructure; it cuts cost and defends collection performance on an existing book.
> **Yuno Value Proposition:** In this state the only proposition with any purchase is **collection success rate on a stressed book** — every repayment that fails for a technical reason on a 6.32%-NPL portfolio is indistinguishable from a credit event until someone reconciles it.
> **Best Success Case:** **Not identified.** ⚠️ Do not improvise one.
> **Outreach Angle:** Do **not** lead with this. It is diagnostic intelligence for qualifying and for timing, not an opener — and a cold email that opens on a prospect's rising NPL ratio will not get a reply. Use it to decide whether to work the account at all this quarter.
> **Suggested Subject Line:** *(none — this insight is not for a first touch)*

> **Insight #4: Nobody in Philippine consumer lending uses an orchestrator, which is whitespace and a long education cycle at the same time**
> **Evidence:** **S11C** — no Philippine lender or BNPL was found on any third-party orchestration platform; **Home Credit Philippines**, the direct peer, collects through **15 individually named online channels** and **39,000+ OTC partners** with **no gateway, aggregator or orchestrator named anywhere** on its own payment pages (`homecredit.ph/pay-loans/pay-online`) + **S3A** — Salmon's estate has exactly the same shape: bilateral, first-party, no PSP.
> **Pain Point:** The whole peer set has independently converged on hand-wired bilateral channel integrations. Each one is carrying the same maintenance burden and none of them has named it as a problem — which means there is no internal champion, no budget line and no vocabulary for the category.
> **Yuno Value Proposition:** First-mover category education in Philippine consumer lending. Genuine whitespace.
> **Best Success Case:** **Not identified in this run.** The honest observation is that `accounts/apac-tal.csv` carries two Philippine orchestration data points — **Cebu Pacific / CellPoint Digital** and **Ikano (IKEA) / Juspay** — which show orchestration does land in this market. ⚠️ **Both are TAL rows, which the method treats as leads requiring independent confirmation, not facts. Neither was verified in this run and neither may be asserted in outreach.**
> **Outreach Angle:** Every lender in the market has built the same thing separately, and none of them has had to think about what happens when the rail count doubles.
> **Suggested Subject Line:** "Eleven biller destinations, eleven integrations — the maths after Daily Banking"

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. You published 99.9% uptime and a 99% success rate on QR Ph in August 2025 — which is better than most of the gateways in this market will put in writing, so I am curious what rail number twelve costs you in engineer-weeks rather than in uptime.
2. Your merchants page promises every partner store the full purchase amount the next day at zero cost, explicitly against providers that "may charge you up to 2%" — and that outbound promise is the one part of the estate your payments-platform announcement never mentions.
3. Daily Banking is adding payments, cards and transfers to the Salmon app in 2026 on top of a collection estate that already spans auto-debit, QR Ph, e-wallet and bank redirects, over-the-counter cash and eleven named biller destinations — that is the point where most teams stop adding integrations one at a time.

**Cold call openers (conversational, one sentence each):**
1. "I read your August 2025 release on the in-house payment orchestration platform — I am not calling to tell you that you need orchestration, you clearly have it, I wanted to ask what it costs you to keep."
2. "You pay 5,000-plus partner stores the full purchase amount the next day and charge them nothing — how do you handle the ones that fail?"
3. "Half your borrowers don't have a bank account, by your own ECPay release — what does that do to your collection success rate versus the auto-debit cohort?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| **Home Credit Philippines** | homecredit.ph | Philippines (Czech parent) | 18,000+ partner stores `[UNVERIFIED — third-party aggregation]`; **39,000+ payment partner channels** | Philippines — **the direct in-store POS lending peer** | **None named.** 15 named online channels: Maya, GOtyme, Shopee, Palawan Pay, UnionBank Online, AUB Hello Money, AUB Online, CIMB, Coins.ph, M Lhuillier Online Wallet, Super U App, Bayad PH App, Cebuana Xpress, BDO Online, RCBC Online. *"Direct payments to Home Credit have no processing fee."* Bank auto-debit via BPI, Metrobank, RCBC, UnionBank, BDO. **No gateway, aggregator or orchestrator on the page.** **Also absent from the BSP OPS register.** | `https://homecredit.ph/pay-loans/pay-online` |
| **BillEase** (First Digital Finance Corp.) | billease.ph | Philippines | $20M raised (BusinessWorld) | Philippines — **online-checkout BNPL** | **Distributed *as a payment method inside* other PSPs:** **Xendit** (API, hosted checkout, Shopify/WooCommerce/Wix plug-ins), **PayRex**, **Maya Business** (checkout + QRPh terminals). 22,000+ offline repayment locations; ₱25 OTC fee, **ECPay 1.5%**, GCash 2.41%. **On the BSP OPS register.** | `https://fintechalliance.ph/xendit-partners-billease-to-offer-bnpl-for-filipino-merchants/` · `https://fintechnews.ph/68975/payments/payrex-partners-billease-bnpl-philippine-merchants/` · `https://www.crowdfundinsider.com/?p=239730` |
| **Atome** (Advance Intelligence Group) | atome.ph | Singapore | 500+ PH retailers at launch; $345M facility `[UNVERIFIED — third-party]` | Philippines + SEA — online + offline BNPL | **Distributed via PayMongo** to its 10,000+ merchant network, no extra annual or service fees. **On the BSP OPS register.** | `https://fintechnews.ph/56341/payments/paymongo-ties-up-with-atome-to-offer-bnpl-acceptance-to-filipino-merchants/` |
| **Cashalo** | cashalo.com | Philippines | Not found | Philippines — consumer lending, POS + cash loans | **Not found** | — |
| **Tala** | tala.co | USA (PH ops) | Not found | Philippines — mobile consumer lending | **Not found** | — |
| **Plentina** | plentina.com | Philippines/USA | Not found | Philippines — BNPL | **On the BSP OPS register** (gate finding). No PSP found. | — |
| **JuanHand** (WeFund Lending) | juanhand.com | Philippines | Not found | Philippines — app-based cash loans | **Not found** | — |
| **GCash GGives** (G-Xchange / Mynt) | gcash.com | Philippines | Not found | Philippines — in-wallet BNPL | **G-Xchange is itself an EMI-NBFI and on the OPS register** — it *is* the rail. | BSP EMI register (read in this run) |

🔑 **The competitor table carries the cleanest confirmation of the ICP line in this file.** **BillEase and Atome are sold *into* other companies' checkouts** — Xendit, PayMongo, PayRex and Maya Business all distribute them as selectable payment methods, and both appear on the BSP OPS register. **Salmon is in nobody's checkout**, has no API, SDK or developer docs, and appears on no register. **Home Credit, the only true in-store POS peer, is absent from the OPS register exactly as Salmon is.** The regulator's line and the commercial reality agree: **online-checkout BNPL is payment infrastructure; in-store POS consumer finance is not.** That is the cleanest ICP justification available for this account, and it now rests on three independent legs — the OPS register, the EMI register, and the distribution pattern of the peer set.

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| **Toyota Financial Services Philippines** | toyotafinancial.ph | Captive consumer finance | Philippines | Closest structural analogue — a consumer finance company collecting instalments. **Unlike Salmon it IS an EMI-NBFI on the BSP register**, which is what makes Salmon's absence meaningful. | BSP EMI register (read in this run) |
| **Netbank (A Rural Bank), Inc.** | netbank.ph | Banking-as-a-service rural bank | Philippines | A rural bank that **is** an EMI-Bank — proof the licence class is open to Salmon Bank's charter type. | BSP EMI register (read in this run) |
| **AllBank (A Thrift Bank), Inc.** | allbank.ph | Thrift bank | Philippines | **Salmon's own QR Ph-P2M partner** and an EMI-Bank. The counterparty, not a prospect. | `salmon.group/tpost/syeud5cse1-…`; BSP EMI register |
| **Cebu Pacific** | cebupacificair.com | Airlines | PH + Asia | PH merchant with heavy OTC cash and e-wallet reliance; TAL lists **CellPoint Digital** as orchestrator. ⚠️ **TAL row — unverified lead, not a fact.** | `accounts/apac-tal.csv` |
| **Robinsons Retail Holdings** | robinsonsretailholdings.com.ph | Retail | Philippines | ~$3.5B FY24; multi-format retail, heavy cash. A plausible **partner-side** counterpart to Salmon's in-store model. ⚠️ TAL row. | `accounts/apac-tal.csv` |
| **SM Retail** | sminvestments.com | Retail | Philippines | Salmon's Feb-2023 named partner (⚠️ **not confirmed still live**) and the operator of SM Bills Payment Centers, one of Salmon's repayment channels. ⚠️ TAL row. | `accounts/apac-tal.csv`; Salmon press |
| **Globe Telecom** | globe.com.ph | Telecom | Philippines | ~$3.2B FY24; very high small-value volume; **Globe is one of Salmon's biller destinations**. ⚠️ TAL row. | `accounts/apac-tal.csv`; `salmon.ph/howtorepay` |
| **Metro Department Store** | metroretail.com.ph | Retail | Philippines | ~$500M est.; domestic chain, heavy cash and local-method reliance. ⚠️ TAL row. | `accounts/apac-tal.csv` |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| — | — | — | — | — |

***"No public case studies found of direct competitors adopting payment orchestration."*** Searched across Philippine lenders and BNPLs (Atome, BillEase, Tala, Cashalo, Plentina) for orchestration adoption: **nothing**. What exists instead is the inverse pattern — PH BNPLs being *distributed by* gateways (Xendit, PayMongo, PayRex, Maya Business) through single API integrations. **No Philippine consumer lender was found running a third-party payment orchestrator.** The ICP row scores **0**, and this is also a genuine market-structure finding: the category is unestablished in this vertical and geography.

⚠️ `accounts/apac-tal.csv` carries two Philippine orchestration rows — **Cebu Pacific → CellPoint Digital** and **Ikano (IKEA) → Juspay**. **Both are unverified leads** per the method, neither was independently confirmed in this run, and **neither may be cited in outreach**. Confirming Cebu Pacific in particular would be worth doing: a confirmed Philippine orchestration reference in any vertical materially helps the category-education problem Insight #4 describes.

#### 11D. Prospect Scoring

Applied to the strongest alternative, **Home Credit Philippines**, since it is the only true direct peer and is **not** on `accounts/apac-tal.csv`.

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| Monthly transaction count | **0** ⬜ | Not sourced. 39,000+ payment partner channels implies large volume but no account or transaction count is published. | `homecredit.ph/pay-loans/pay-over-the-counter` |
| Orchestration status | **+4** ✅ | **None detected — direct bilateral integrations only.** 15 named online channels and 39,000+ OTC partners, **no gateway, aggregator or orchestrator named**; absent from the BSP OPS register. **Greenfield.** | `homecredit.ph/pay-loans/pay-online` |
| 3+ countries | **0** ⬜ | Philippine entity; Czech group operates many markets but that is the parent, unverified here. | — |
| Multiple PSPs | **0** ⬜ | No PSP named at all. Channels are banks and wallets, not PSPs. | `homecredit.ph/pay-loans/pay-online` |
| Local rail/licensing gap | **0** ❌ | Maya, GOtyme, ShopeePay, PalawanPay, five banks, 39,000+ OTC. No gap. | `homecredit.ph/pay-loans/pay-online` |
| Recent expansion | **0** ⬜ | Not researched in this run. | — |
| Payment issues | **0** ⬜ | Not researched in this run. | — |
| Funding >$10M | **0** ⬜ | Not researched in this run. | — |
| High traffic outside home | **0** ⬜ | No traffic data pulled. | — |
| Competitor using orchestration | **0** ⬜ | None found in the vertical. | §11C |
| Payment job postings | **0** ⬜ | Not researched in this run. | — |
| **Total** | **4 / 29** 🔴 | **Partial scoring only — six rows were not researched.** This is a screening score, not a report. | |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | **Home Credit Philippines** | Direct competitor | Philippines | 4/29 *(partial — 6 rows unresearched)* | 🟢 **Worth a full run** | **Greenfield: 15 bilateral online channels + 39,000+ OTC partners, no gateway or orchestrator named, absent from the OPS register.** Same shape as Salmon but **without** the in-house platform. | ❌ **No — genuine find** |
| 2 | **Robinsons Retail Holdings** | Industry peer | Philippines | Not scored | 🟢 Medium | ~$3.5B FY24 multi-format retail, heavy cash | ✅ Yes |
| 3 | **Metro Department Store** | Industry peer | Philippines | Not scored | 🟢 Medium | ~$500M est., domestic chain, local-method reliance | ✅ Yes |
| 4 | **Cebu Pacific** | Industry peer | PH + Asia | Not scored | ⚠️ Verify first | TAL says CellPoint Digital — **displacement if confirmed** | ✅ Yes |
| 5 | **Globe Telecom** | Industry peer | Philippines | Not scored | 🟢 Medium | ~$3.2B FY24, very high small-value volume | ✅ Yes |
| 6 | **Cashalo** | Direct competitor | Philippines | Not scored | ⚠️ Gate first | PH consumer lender; **check the OPS register before researching** | ❌ No |
| 7 | **JuanHand** (WeFund Lending) | Direct competitor | Philippines | Not scored | ⚠️ Gate first | App-based cash lender; **check the OPS register** | ❌ No |
| 8 | **Tala** | Direct competitor | PH (US HQ) | Not scored | ⚠️ Territory check | US-HQ'd — confirm APAC ownership before working it | ❌ No |
| 9 | **SM Retail** | Industry peer | Philippines | Not scored | 🟢 Medium | Part of SM Investments ~$11B; also a Salmon repayment channel | ✅ Yes |
| 10 | ~~BillEase · Atome · Plentina · GCash GGives~~ | — | Philippines | — | 🔴 **DO NOT RESEARCH** | **All on the BSP OPS register and/or distributed as payment methods inside other PSPs' checkouts. Phase 0 gate fires. Route to 🤝 Partnerships.** | ❌ No |

🔑 **The genuine find is Home Credit Philippines**, and it is **not on the TAL**. It is Salmon's closest structural peer — in-store POS consumer finance, Philippine, absent from the OPS register, so it clears the same gate Salmon clears — but with one decisive difference: **its collection estate is bilateral and greenfield, with no in-house orchestration platform announced or found.** That makes it a materially better Yuno target than Salmon on the single row that matters most. **Recommend adding it to `accounts/apac-tal.csv` and running `/research` on it.**

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | **No group figure published.** Salmon Bank only, and only partially: **₱66M** year-to-date revenue as at May 2024 (+432% from ₱12M) with **₱40M** net income (from ₱1.7M). ⚠️ **Over two years stale, bank-only, and on a basis that does not reconcile with the Published Balance Sheets.** | `gmanetwork.com/news/money/companies/910542/…` (19 Jun 2024) |
| GMV / Gross Transaction Volume | **No public information found.** | — |
| **Salmon Bank gross Total Loan Portfolio** | **₱3,426,514,104** at 30 Jun 2026 | ✅ **SOURCED** — `s.slmn.ph/docs/bank/Q2_2026_published_balance_sheet.pdf` |
| **Salmon Bank total assets** | **₱8,208,062,461** at 30 Jun 2026 | ✅ **SOURCED** — same filing |
| **Salmon Bank deposit liabilities** | **₱6,280,830,541** at 30 Jun 2026 | ✅ **SOURCED** — same filing |
| Average Transaction Value (USD) | **Not published.** Product Loan principal **₱1,000–₱60,000**; Credit Line to **₱250,000**; down payment 0%–70%; tenor **4–12 months** (merchants FAQ) / 4–24 months (third-party). | `salmon.ph/product-loan`; `salmon.ph/merchants`; `sacra.com/c/salmon` |
| Est. Annual Transactions | **~2.0M–3.4M repayment-collection events/year** — ⚠️ derived from the assumed monthly figure below, therefore **also an assumption**. | See the monthly row |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ~170,000–290,000/month. [ASSUMPTION — not researched.]** Neither Salmon, BSP, SEC nor any credible third party publishes a borrower count, loan-account count, disbursement count or repayment-event count. **Basis:** ₱3,426,514,104 gross TLP (sourced) ÷ an assumed ₱12,000–₱20,000 average outstanding balance = ~171,000–286,000 live accounts; a monthly-amortising 4–12 month book bills **every account every month**. Salmon Finance Inc.'s separate book is additive and unquantified. **Sensitivity:** falls below 100,000/month only if the average outstanding balance exceeds ~₱34,000, on a flagship product capped at ₱60,000 and starting at ₱1,000 — implausible. **Corroborating (not proof):** 5M+ Google Play installs; 158K Play + 55K App Store ratings; *"More than 80% customers use Salmon app for payments."* **This is an assumption and CANNOT trigger the under-40,000 rejection. "Confirm monthly transaction count" is the first Manual Research Recommendation.** | See the disclosure rule in the ICP matrix |
| **Billing unit being counted** | **Monthly loan-repayment collection events** — one per active amortising loan account per month, arriving over any of 5 in-app methods or 11 named biller destinations. **Explicitly NOT counted and additive:** (a) **merchant disbursements** — one per loan origination, next-day, 5,000–10,000 stores, a payout leg; (b) **deposit cash-in** on a ₱6.28bn deposit book; (c) **Salmon Mastercard** transactions; (d) multiple part-payments against one instalment (a borrower review confirms these happen — *"multiple small payments"*); (e) failed and retried attempts, which Salmon's own platform generates deliberately via *"multiple payment attempts."* **Each of (a)–(e) raises the true payment-event count above the loan-account count.** | Method note |
| Active Customers / Users | **No absolute figure published.** Only growth rates: customer base **doubled in 2025**; deposit client base **doubled in 2025** with ~85% affluent/time-deposit. ⚠️ `multiples.vc` asserts *"over 1 million customers across Southeast Asia"* — **`[UNVERIFIED — third-party aggregator; the same page gives a 2018 launch date that contradicts every primary source. Do not use.]`** | `salmon.group/tpost/salmon-bank-doubles-customer-base-and-grows`; `salmon.group/tpost/salmon-banks-client-base-doubles-in-2025` |
| Primary Currency | **PHP, exclusively.** Card credit limit *"in PHP funds."* No FX leg anywhere in the business. | `s.slmn.ph/docs/Salmon_Card_Terms_and_Conditions.pdf` |
| Top 3 Markets by Revenue | **Philippines — and only the Philippines.** | §1, §2 |
| Billing channel split (web vs app store) | **Not applicable, and favourably so.** Salmon is a lender: revenue is interest and fees on a loan book, not in-app purchases. **No Apple/Google IAP exposure whatsoever**, so the app-store analyst override in the method cannot fire. *"More than 80% customers use Salmon app for payments"* — app-channel, but Salmon's own rails, not IAP. | `salmon.group/tpost/tv5v7v7vl1-…` (29 Aug 2023) |

#### 🔴 Salmon Bank (Rural Bank) Inc. — BSP-mandated Published Balance Sheet series

Decoded from the quarterly filings Salmon publishes at `salmon.ph/financial-statements`, each signed *"(original signed) Georgy Chesakov, President and CEO."* Every column was sum-verified, and **each filing's "previous quarter" column matches the prior filing's "current quarter" column exactly**, so the series is serially consistent. All figures in PHP.

| | 30 Sep 2025 | 31 Dec 2025 | 31 Mar 2026 | **30 Jun 2026** |
|---|---|---|---|---|
| Total assets | 2,704,963,138 | 4,352,459,007 | 6,088,261,620 | **8,208,062,461** |
| Due from BSP | 764,584,540 | 152,049,893 | 1,206,961,307 | **4,295,357,359** |
| **Gross Total Loan Portfolio** | 1,709,207,139 | 3,483,900,214 | 4,576,492,489 | **3,426,514,104** |
| Allowance for credit losses | (112,498,766) | (544,592,242) | (823,954,827) | **(804,297,074)** |
| Net Total Loan Portfolio | 1,596,708,373 | 2,939,307,973 | 3,752,537,662 | **2,622,217,029** |
| Deposit liabilities | 1,770,413,831 | 2,803,734,807 | 4,583,002,499 | **6,280,830,541** |
| Total equity | — | — | 1,154,487,848 | **1,667,888,092** |
| Undivided profits | — | — | (68,655,127) | **(55,165,052)** |
| **Gross NPL ratio** | — | **2.10%** | **2.34%** | **🔴 6.32%** |
| Return on equity | — | — | **(24.22%)** | **(8.16%)** |
| Return on assets | — | — | **(5.91%)** | **(1.97%)** |
| Net interest margin | — | — | 26.20% | 59.30% |
| Capital adequacy ratio | — | — | 16.43% | 29.63% |
| Minimum liquidity ratio | — | — | 33.42% | 75.51% |

**Sources:** `s.slmn.ph/docs/bank/Q4_2025_Published_Balance_Sheet.pdf` · `s.slmn.ph/docs/bank/Q1_2026_Published_Balance_Sheet.pdf` · `s.slmn.ph/docs/bank/Q2_2026_published_balance_sheet.pdf`

**What the series says, and what it does not:**
- ✅ **Salmon's FY2025 press claims check out against its own regulatory filing.** The 17 Mar 2026 release said total assets grew *"2.3× to ₱4.4 billion"* and gross NPL *"held steady at 2%"* — the Q4 2025 filing shows ₱4,352,459,007 and 2.10%. **The company reported FY2025 accurately.** That is worth knowing before using any other Salmon number.
- 🔴 **2026 is a different story, and it is not in any press release.** Gross NPL **2.10% → 2.34% → 6.32%** across three quarters. The gross loan book **contracted 25.1%** in Q2 2026 while deposits grew 37% and cash at BSP tripled — the signature of **deliberate origination tightening with the funding parked**. ROE and ROA print **negative in both 2026 quarters**. The allowance for credit losses stands at **23.5% of the gross book**.
- ⚠️ **The ratio labels were reconstructed from the decoded text's visual order, then validated by the exact match between the Q1 2026 current column and the Q2 2026 previous column.** That cross-check is strong, but **the computation basis (quarterly, year-to-date or annualised) is not stated on the BSP form**, so the negative ROE/ROA should be read as "loss-making on the published basis" rather than as a precise quarterly return.
- 🔗 **Cross-reference to §1:** Philippine web traffic fell **41.62%** QoQ over Jul–Sep 2026; the gross loan book fell **25.1%** QoQ over Apr–Jun 2026. Two independent sources, one quarter apart, pointing the same way. The traffic file asked for the explanation of its decline and listed four candidates — **this is evidence for the fourth, a genuine contraction in origination**, though the traffic contamination in §1 means it cannot be the whole story. ⚠️ `[INFERENCE, not confirmed]` — the two series are not formally linked and one leads the other.

**No group-level revenue or GMV data found. Business case sizing will require a discovery call.**

---

### Overall Research Confidence

**Medium.**

**Strong coverage, first-hand and primary-sourced:**
- **Regulatory status (§2).** Both disqualifying registers now closed against BSP's own current documents, each with a sanity check confirming known-good entries before any zero was trusted. **The EMI question, which was the one open test handed to this run, is resolved.**
- **Payment stack (§3).** Unusually strong for a negative finding, because the production CSP enumerates every host the page may contact — a closed list, not a sample — and it was corroborated by the client web-app bundle, the T&Cs, the privacy index and six years of press. Five independent checks, all agreeing.
- **Orchestration status (§3B).** The strongest single finding in the file: the company's own press release, in its own words, corroborated by a live first-party service in the production CSP.
- **Financials (§12).** Four quarters of BSP-mandated filings, sum-verified and serially cross-validated. Better than most accounts in this repo get.
- **Rails (§4).** Enumerated from Salmon's own public repayment page and app bundle.

**Limited coverage, and why:**
- **Transaction volume.** The pre-research brief's best lead — the IPO registration PDF — **turned out to be a trademark certificate**, and the Nordic bond investor reporting was not locatable publicly (Pareto Securities was sole bookrunner; no trustee or exchange filing surfaced). **The monthly transaction count remains ASSUMED and is labelled as such everywhere it appears.** It does not and cannot reject the account.
- **Complaints (§5).** Five payment-mechanics failure modes confirmed, **frequency not establishable** — both app stores paginate reviews behind JavaScript this environment cannot execute, against 213,000 total ratings. Scored 0 rather than guessed.
- **Checkout audit (§8).** Reframed as a repayment-flow audit, because **Salmon has no checkout.** The authenticated flow needs a Philippine phone number.
- **Card issuer.** The Salmon Access Card T&Cs use a 14-font subset encoding that only partially decoded here. Mastercard licence and BSP-regulated issuer confirmed; the issuer's name is not.
- **Individual privacy notices.** Ten entity-specific notice PDFs were not opened. In APAC these name processors more often than press does — the one remaining stone, and it is in Manual Research Recommendations.

**Traffic data: SUPPLIED, not API-sourced and not estimated.** `accounts/traffic/salmon-group-philippines.md`, SimilarWeb, Jul–Sep 2026, used verbatim and not re-researched. **Three caveats that matter, because the country profile drives the APM analysis and two ICP rows:** (1) **no total visit count is shown and country rank reads `-` on every row**, so no absolute volume can be derived and none is; (2) **two of the top three rows are bot-shaped** and were discounted per the file's own instruction; (3) 🚩 **the profile is contaminated** — the pull rolls up a careers site on the Ashby ATS, a merchant-acquisition funnel, a motorcycle-loan storefront, the authenticated borrower app and two asset/CDN hosts into one `salmon.ph` figure, and **the "+2 domains" are never named.** The country split should not be read as borrower demand. This does not change the two ICP rows it drives — both are correctly scored **0**, and would be 0 on any reading.

> ⚠️ **Method deviation, disclosed as required.** **No Agent or Task tool exists in this environment**, so Phase 2's Agents 2–5 could not be launched in parallel as the method specifies. **All four workstreams were run by me, sequentially, under the same per-agent search and fetch budgets.** Phase 1 was satisfied by the supplied traffic file plus the gate's verified entity and funding findings; Phase 3's cross-reference pass and synthesis were performed in full. The practical effect is less parallel breadth and more depth on the two questions that mattered — the EMI register and the PSP behind collections — both of which are now answered. **Per the method, Overall Research Confidence is stated one level below what the evidence alone would support: the regulatory and payment-stack work would justify High, and it is recorded as Medium.**

---

### Manual Research Recommendations

> **Area:** Monthly transaction count (§12) — the only ASSUMED figure in the file
> **Why it matters:** It is the heaviest row in the matrix (+5 of 8 points) and the only one that can reject an account outright. Every other number in this report is sourced; this one is not, and the report's score depends on it.
> **Suggested manual action:** Ask on the first call for active loan accounts and monthly repayment transactions. Failing that, chase the Nordic bond investor reporting — the bonds are listed and **Pareto Securities was sole bookrunner** (`roschier.com/newsroom/salmon-group-secures-usd-110-million-via-initial-usd-60-million-bond-issue-and-usd-50-million-tap-issue`); periodic reports to the bond trustee would carry loan-book composition and account counts. Also open **`s.slmn.ph/docs/bank/2025_Audited_Financial_Statement.pdf`** and **`s.slmn.ph/docs/bank/2025_salmon_bank_rural_bank_Inc._annual_report.pdf`** (87MB) in a real PDF reader — the loans-and-receivables note will carry account-level detail that could not be extracted here.

> **Area:** Territory ownership — Salmon Group Ltd is registered in **ADGM, Abu Dhabi** (§2)
> **Why it matters:** `CLAUDE.md` places the Gulf with EMEA. The operating business is entirely Philippine, but the entity that owns the app, signs the T&Cs and would likely sign a contract is Emirati. **This was not surfaced at the Phase 0 gate.**
> **Suggested manual action:** Settle account ownership with the APAC/EMEA split **before** investing outreach cycles. My read is that this is a holding-company domicile and the account is substantively APAC — but it is not mine to decide.

> **Area:** The 41.62% quarter-on-quarter fall in Philippine traffic (§1) against the 25.1% fall in the gross loan book (§12)
> **Why it matters:** Two independent declines a quarter apart. If Salmon is tightening origination through a credit cycle, it is not buying payment infrastructure this year — and that is a go/no-go on timing, not a detail.
> **Suggested manual action:** Re-pull SimilarWeb for `salmon.ph` **alone**, with subdomains excluded if the tool allows, to strip the careers/merchant/CDN contamination. Then read the Q3 2026 Published Balance Sheet when it posts at `salmon.ph/financial-statements` and see whether gross TLP and the 6.32% NPL turn.

> **Area:** The ten individual privacy-notice PDFs at `salmon.ph/privacy-policy`
> **Why it matters:** The single remaining place a third-party payment processor could be named. APAC merchants disclose processors in privacy notices far more often than in press, and this is the only one of five checks in §3A that was not completed.
> **Suggested manual action:** Open `s.slmn.ph/docs/privacy_policy/SLMNB-Data_Privacy_notice.pdf`, `s.slmn.ph/App_User-Clients_Privacy_Notice.pdf`, `s.slmn.ph/Sunprime-Privacy_Notice_for_Clients.pdf` and `s.slmn.ph/FHLFC-Privacy_Notice_for_Merchants.pdf` and search the data-sharing / third-party-recipient sections. **If a processor is named there it changes §3A and the "Multiple PSPs" ICP row.**

> **Area:** Salmon Access Card issuer and issuer processor
> **Why it matters:** Card issuing is the one part of the estate where a third-party processor is genuinely likely, and "Daily Banking" is adding cards and transfers in 2026.
> **Suggested manual action:** Open `s.slmn.ph/docs/Salmon_Card_Terms_and_Conditions.pdf` in a real PDF reader (it did not fully decode here) and read the issuer clause. The legible text confirms a **Mastercard International** licence and a **BSP-regulated** issuer; the name is the gap.

> **Area:** Live payment-related roles at `careers.salmon.ph`
> **Why it matters:** Decides the "Payment job postings" ICP row, currently 0 on a 2023 hire. More usefully, payments roles would reveal whether "Daily Banking" is being built in-house again or bought.
> **Suggested manual action:** Open `careers.salmon.ph` in a browser — the Ashby role list is JS-rendered and was not retrievable here — and filter for payments, treasury, settlement and acquiring.

> **Area:** Home Credit Philippines — **not on `accounts/apac-tal.csv`**
> **Why it matters:** Salmon's closest structural peer, clears the same Phase 0 gate (absent from the OPS register), and is **greenfield** on the row where Salmon is in-house. On present evidence it is the better Yuno target of the two.
> **Suggested manual action:** Add it to the TAL and run `/research` on it.

> **Area:** Whether the SM Store partnership is still live (§7)
> **Why it matters:** It is Salmon's only blue-chip named retail partner and it rests on a February 2023 release. Citing a dead partnership in a first touch is unrecoverable.
> **Suggested manual action:** Check the store locator behind *"View all on map"* on `salmon.ph/merchants` for SM locations, or ask on the call. **Do not state Salmon is live in SM Store until confirmed.**

---

### Appendix: All Source URLs

**Supplied data**
- `accounts/traffic/salmon-group-philippines.md` — SimilarWeb (supplied 2026-10-11), `salmon.ph` +2 domains, Jul–Sep 2026
- `accounts/apac-tal.csv` — **Salmon is NOT on the target account list; this is a new account.** 1,219 rows checked.
- `not-icp/pdax.md`, `not-icp/coins-ph.md` — rejected Philippine precedents
- `.claude/reference/apac-payments.md` §2 (Philippines), §1, §3, §4, §5

**Regulatory — primary**
- `https://www.bsp.gov.ph/Lists/Directories/Attachments/7/emi.pdf` — List of BSP Supervised Electronic Money Issuers (EMIs), **as of 31 May 2026**. 29 EMI-Banks + 40 EMI-NBFIs. **0 Salmon hits, all variants.** Retrieved via WebFetch (BSP resets curl); FlateDecode streams decompressed in Python; searched with `LC_ALL=C grep -a` after stripping non-printables and collapsing letter-spacing.
- `https://www.bsp.gov.ph/PaymentAndSettlement/cor.pdf` — List of BSP-Registered Operators of Payment System, 314 registrations. **0 Salmon hits** (verified by the orchestrator, carried forward).

**Salmon — own properties, fetched 2026-10-11**
- `https://salmon.ph/our-story` · `https://salmon.ph/howtorepay` · `https://salmon.ph/merchants` · `https://salmon.ph/salmonbank` · `https://salmon.ph/financial-statements` · `https://salmon.ph/product-loan` · `https://salmon.ph/security` · `https://salmon.ph/privacy-policy` · `https://salmon.ph/terms-and-conditions`
- `https://salmon.group/` · `https://careers.salmon.ph/` · `https://moto.salmon.ph/` · `https://merchant.salmon.ph/` · `https://client.salmon.ph/`
- `https://client.salmon.ph/static/js/main.49353ba7.js` — borrower web-app bundle `[Source Code]`
- Production CSP header on `https://salmon.ph/howtorepay` (and on `salmon.group`, `moto.salmon.ph`, `careers.salmon.ph`) `[Source Code]`

**Salmon — documents**
- `https://s.slmn.ph/docs/our_story/Salmon_IPO_Registration.pdf` — **IPOPHL trademark registration 4/2024/00522723, NOT an IPO filing.** Registrant: Salmon Group Ltd (formerly Fintech Holdings Ltd), ADGM, Abu Dhabi.
- `https://s.slmn.ph/docs/bank/Q2_2026_published_balance_sheet.pdf` · `Q1_2026_Published_Balance_Sheet.pdf` · `Q4_2025_Published_Balance_Sheet.pdf`
- `https://s.slmn.ph/docs/bank/2025_Audited_Financial_Statement.pdf` — Salmon Bank (Rural Bank) Inc., audited by **Punongbayan & Araullo** (Grant Thornton Philippines); ⚠️ statement pages not fully extractable here
- `https://s.slmn.ph/docs/bank/2025_salmon_bank_rural_bank_Inc._annual_report.pdf` (87MB, not extracted) · `https://s.slmn.ph/docs/bank/2025_financial_condition_and_results_of_operation%20.pdf` (not opened)
- `https://s.slmn.ph/App_User-Terms-and-Conditions.pdf` — Salmon App General T&Cs, **17 June 2026**. No processor named; Philippine law and exclusive Philippine venue.
- `https://s.slmn.ph/docs/Salmon_Card_Terms_and_Conditions.pdf` — Mastercard International licence; BSP-regulated issuer; ⚠️ issuer name not machine-readable
- `https://s.slmn.ph/docs/Sunprime_Finance_Inc_Certificate_of_Incorporation_and_Authority_to_Operate_as_a_Financing_Company.pdf` · `https://s.slmn.ph/docs/our_story/FHL_Services_Inc_SEC_Certificate_of_Incorporation.pdf` · `https://s.slmn.ph/docs/bank/Amended_AOI_Salmon_bank_Rural_Bank_Inc.pdf` · `https://s.slmn.ph/docs/bank/AMLC_Registration_Salmon%20Bank.pdf`
- `https://s.slmn.ph/docs/merchants/Retailer_Access_Terms_and_Conditions_v2.pdf` (not opened)

**Salmon — newsroom (salmon.group)**
- `/tpost/salmon-upgrades-payment-backbone` — **18 Aug 2025, the in-house payment orchestration platform**
- `/tpost/syeud5cse1-the-salmon-group-partners-with-allbank-t` — 3 Apr 2024, AllBank QR Ph-P2M
- `/tpost/51evppz8m1-salmon-expands-payment-channels-with-ecp` — 25 Apr 2024, ECPay
- `/tpost/52pc5j9h81-salmon-introduces-auto-debit-for-seamles` — 29 Jun 2024, auto-debit
- `/tpost/tv5v7v7vl1-salmon-simplifies-loan-repayment-for-its` — 29 Aug 2023, five repayment institutions
- `/tpost/salmon-bank-doubles-customer-base-and-grows` — 17 Mar 2026, FY2025 results
- `/tpost/salmon-banks-client-base-doubles-in-2025` — 5 Feb 2026
- `/tpost/salmon-bank-nearly-triples-deposits-and` — 29 Oct 2025, Q3 2025 + **Daily Banking 2026**
- `/tpost/salmons-banking-announces-financial-and-operating` — 29 Jul 2025, H1 2025
- `/tpost/sef8hz7a51-sunprime-finance-inc-announces-loan-acco` — 18 Apr 2024, loan-account transfer
- `/tpost/74bnrcxna1-salmon-builds-its-debit-products-team` — 3 May 2023, Head of Debit Products
- `/tpost/salmon-group-raises-usd-100-million` (index entry)

**App stores**
- `https://play.google.com/store/apps/details?id=com.fhl.salmon` — **5M+ downloads, 158K reviews, 4.8, updated 8 Oct 2026**
- `https://apps.apple.com/ph/app/salmon-finance-made-easy/id6446115147` — **55K ratings, 4.8, v2.42.1**, seller **Salmon Group Ltd**
- `https://appgallery.huawei.com/app/C108007333` (listed, not fetched)

**Press & third party**
- `https://fintech.global/2026/04/21/salmon-raises-100m-to-fuel-philippines-expansion/` — $100M, April 2026
- `https://www.roschier.com/newsroom/salmon-group-secures-usd-110-million-via-initial-usd-60-million-bond-issue-and-usd-50-million-tap-issue` — USD 110M bonds, **Pareto Securities sole bookrunner**
- `https://www.gmanetwork.com/news/money/companies/910542/salmon-group-eyes-2-b-loan-portfolio-in-next-five-years/story/` — 19 Jun 2024, $2bn target; May 2024 bank figures
- `https://sacra.com/c/salmon` — third-party aggregation: funding history, product parameters, deposit base, NPL. ⚠️ Estimates labelled as such.
- `https://multiples.vc/private-comps/salmon` — ⚠️ **"over 1 million customers" NOT used**; the page's 2018 launch date contradicts every primary source.
- `https://www.fintechfutures.com/press-releases/salmon-raises-88-million-to-grow-its-business-in-the-philippines-sets-up-a-150-million-nordic-bond-framework-agreement-for-scaling-up` — Jun 2025, $88M + $150M Nordic framework

**Competitors**
- `https://homecredit.ph/pay-loans/pay-online` — 15 named online channels, no gateway named
- `https://www.homecredit.ph/pay-loans/pay-over-the-counter` — 39,000+ payment partner channels `[UNVERIFIED — search summary only, page not fetched]`
- `https://fintechalliance.ph/xendit-partners-billease-to-offer-bnpl-for-filipino-merchants/` `[UNVERIFIED — search summary only, page not fetched]`
- `https://fintechnews.ph/68975/payments/payrex-partners-billease-bnpl-philippine-merchants/` `[UNVERIFIED — search summary only, page not fetched]`
- `https://fintechnews.ph/56341/payments/paymongo-ties-up-with-atome-to-offer-bnpl-acceptance-to-filipino-merchants/` `[UNVERIFIED — search summary only, page not fetched]`
- `https://www.crowdfundinsider.com/?p=239730` — BillEase × Maya Business `[UNVERIFIED — search summary only, page not fetched]`
- `https://blog.billease.ph/2024/08/30/easy-ways-to-pay-your-billease-installments/` — ₱25 OTC, ECPay 1.5%, GCash 2.41% `[UNVERIFIED — search summary only, page not fetched]`

**Environment notes for the next run on this account**
- `pdftotext` and `pdftoppm` are **not installed**; no `pypdf`, `pdfminer`, `fitz` or `pdfplumber` either. Every PDF in this report was decoded by decompressing FlateDecode streams in Python. **Salmon's quarterly balance sheets are Figma exports with per-font `FigmaPDF` ToUnicode CMaps — they need per-font resource resolution and `Tf`-tracking, not a global CMap merge.** The working decoder is reusable.
- **BSP resets `curl`; WebFetch retrieves BSP PDFs** and writes the binary to disk for local decompression. Confirmed again this run.
- 🚩 **New substring traps found and confirmed here, worth adding to the standing list:**
  - **`etap` → `SsrMetaProvider`** (Next.js internal). Returned 6+ false hits per page. ETap *is* a real Salmon kiosk partner, confirmed separately from visible page text.
  - **`maya` → `may also` / `may arise`** once whitespace is stripped for matching. Both "maya" hits in the Salmon App T&Cs were this. Maya *is* a real Salmon channel, confirmed from `salmon.ph/howtorepay`. **The standing warning to check `maya` context both ways is correct and this is a third variant of it.**
  - **`omise` → `Promise`** — reconfirmed: 89 false hits in the client bundle, every one of them JavaScript.
- `grep -P` unavailable; `LC_ALL=C grep -a` used throughout. All downloads went to fresh empty directories, with scripts kept in a separate directory and run with `python3 -I`.
- 🔒 **No credential, API key, token, cookie or secret value is transcribed anywhere in this file.** Salmon's production responses do set identifier cookies and its CSP exposes internal hostnames; **hostnames are named where they are evidence, values never are.**

</details>
