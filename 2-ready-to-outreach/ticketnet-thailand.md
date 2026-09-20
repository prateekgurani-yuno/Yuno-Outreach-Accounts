# ThaiTicketMajor

**Status:** 🟠 **BLOCKED — Phase 1 research complete, Phase 2 DELIBERATELY NOT RUN.** See the blocker.
**ICP Score:** ⚠️ **PROVISIONAL / NOT COMPUTABLE — 4 of 5 research agents were not run by decision.** A score computed now would read ~2/29 purely because the unresearched rows score 0. **That would be a false rejection and must not be recorded as one.**
**Industry:** Live event ticketing (concerts, theatre, sport), agent-of-promoter with heavy offline counter/cash distribution · **HQ:** Bangkok, Thailand — **THAITICKETMAJOR COMPANY LIMITED / บริษัท ไทยทิคเก็ตเมเจอร์ จำกัด**, DBD reg. **0105543020073** · **Researched:** 2026-09-20 · **First email sent:** —
**Motion:** Not established — orchestrator check not run.

---

> ## ⛔ BLOCKER — Ticketmaster / Live Nation owns part of this company. **This is the Moshtix situation again.**
>
> **Verified first-hand from Ticketmaster's own press release**, `business.ticketmaster.com`, **21 July 2022**:
>
> > *"Ticketmaster, the global leader in live event ticketing, today announced a **part acquisition of Thai Ticket Major (TTM)**, headquartered in Bangkok, Thailand. The acquisition is scheduled to complete in Q3 (subject to customary closing conditions being satisfied)."*
>
> TTM's own quote in the same release: *"it was the natural next step for us to **join the world's leading ticketing company, Ticketmaster**… **Being part of Ticketmaster** gives us the opportunity to elevate our ticketing solutions."*
>
> Also in the release: **Mark Yovich, President of Ticketmaster** quoted; **MD Komkrit Sirirat** continues to lead Thai operations; founded **1999 by Tero Entertainment**; and Ticketmaster's stated rationale — ***"90 percent of Western tours in Asia route through Bangkok."***
>
> ⚠️ **What is NOT established:** the acquired **percentage**, the **price**, and **whether the deal actually closed.** The DBD record still shows an independent Thai limited company. TTM's own language ("being part of Ticketmaster") reads as completed, but that is the company's words in an announcement, not a filing.
>
> **`moshtix.md` was parked on 2026-09-20 for exactly this reason.** Same ultimate parent, same question: a payments decision at a Live Nation subsidiary is plausibly a global-account call, not an APAC SDR one. **Consistency demands the same treatment unless Prateek decides otherwise.**

> ## ⛔ SECOND BLOCKER — the volume gate is genuinely unresolved and may sit BELOW threshold
>
> **Two independent derivations disagree by ~2.5×, and the gate sits inside the range.**
>
> **Derivation A — from traffic (suggests AT or ABOVE):** ~2.7M monthly visits (SimilarWeb Aug 2026, `[ESTIMATE]`) × conversion rate. At 1.0% → 27,000/mo (**fails**); 1.5% → 40,500 (**at gate**); 2.0% → 54,000 (**passes**); 3.0% → 81,000. **The conversion rate is unsourced and the answer flips on it.**
>
> **Derivation B — from cumulative tickets (suggests BELOW):** 8,000,000 tickets **cumulative** over 20+ years (queue-it.com case study) ÷ ~26 years = ~25,600 tickets/month ÷ ~2 tickets per concert order = **~12,800 orders/month. Fails by ~3×.** *(Both divisors unsourced; the 8M figure is undated vendor marketing and likely predates the post-COVID and K-pop surge, so this is probably understated.)*
>
> **Honest range: 15,000–50,000 monthly transactions.** ⚠️ **An assumption never fires the under-40k auto-reject** — so this account is **NOT rejected on volume**. But the case for qualification is **not made**.
>
> ### ⚡ And the structural evidence cuts against it — from their own terms
> **Verified first-hand** on `corporate.thaiticketmajor.com/policies.php`:
> > 「หากเป็นการชำระเงินโดยเลือกช่องทางอื่น **ที่ไม่ใช่ การตัดบัตรเครดิต หรือ เดบิต** ให้ถือว่า **การซื้อนั้น ยังไม่สมบูรณ์ เป็นเพียงขั้นตอนการจองที่นั่ง**」
> > *"If payment is made by any channel **other than credit or debit card**, the purchase is **not complete — it is only a seat reservation**."*
>
> **Their own terms split the business in two.** Card = a completed online transaction. **Everything else = a reservation pending offline payment.** For an orchestrator, only the card/wallet leg is addressable, and this sentence says it is a *subset* of orders. **That is the counter/cash drag, stated by the merchant.**

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** ThaiTicketMajor is Thailand's dominant event-ticketing company — a vendor case study claims **90% of Thai performance tickets** — selling concerts, theatre and sport through a hybrid model: online seat selection, then payment and physical ticket collection across a large offline network. Founded 1999 by Tero Entertainment. **Part-acquired by Ticketmaster (Live Nation) in 2022.**

### Traffic — `[ESTIMATE, not confirmed]`
SimilarWeb, **August 2026**. ⚠️ **No data was supplied for this account**; this was agent-fetched and SimilarWeb's own labelling was ambiguous between monthly and 3-month-average, so treat ~2.7M with that caveat.

| Rank | Country | Share |
|---|---|---|
| 1 | **Thailand** | **74.91%** |
| 2 | Vietnam | 2.91% |
| 3 | United States | 2.24% |
| 4 | Taiwan | 2.08% |
| 5 | Kazakhstan | 1.92% |

**~2.7M visits/mo** · global rank **#10,609** · Thailand **#127** · **#1 in Ecommerce > Tickets, Thailand** · +3.6% MoM
**Engagement: bounce 36.45%, 15.87 pages/visit, 4m32s.** That pages/visit figure is extremely high — consistent with seat-map browsing and queue-waiting, i.e. real purchase intent, **but it also means visits ≠ buyers, which is why Derivation A is unreliable.**

⚠️ **Thailand at 74.91% is >60%, so the "high traffic outside home" signal is NOT met.** The foreign traffic reads as diaspora/tourist inbound, not multi-market operations.

### Accepted payment methods — first-party, verified by me
Source: `https://corporate.thaiticketmajor.com/policies.php` — **fetched and parsed 2026-09-20**

| Method | Status | Evidence |
|---|---|---|
| **Credit / debit card** | **CONFIRMED** | 「การตัดบัตรเครดิต หรือ เดบิต」 — the only channel that completes a purchase instantly |
| **Counter Service (cash)** | **CONFIRMED** | 「ชำระด้วยเงินสดที่จุดรับชำระเคาน์เตอร์เซอร์วิสทุกสาขา」 — **5-hour window, auto-cancel** (see below) |
| **TRUE WALLET** | **CONFIRMED** | named in the fee clause |
| **AIRPAY** | **CONFIRMED — but STALE** | named in the fee clause. ⚠️ **AirPay rebranded to ShopeePay in 2021**, so this terms page is carrying a name that is ~5 years out of date |
| **Bill payment** | **CONFIRMED** | 「ค่าธรรมเนียมที่ชำระผ่าน Bill payment」 |
| **Bank transfer** | **CONFIRMED** | 「โอนเงินผ่านธนาคาร」 |
| **PromptPay** | ⚠️ **NOT FOUND — but NOT a sourced absence** | Thailand's dominant A2A rail is absent from the fee clause. **However this clause is about fees and refunds, not a closed enumeration of accepted methods** — and the stale "AIRPAY" proves the page is not maintained. **Verify on a live checkout before treating as a gap.** |

**Fees, verbatim:** 「ค่าบริการใบละ **30 บาท**, **Payment services fee 3%** ของบัตรเครดิต/เดบิต, TRUE WALLET, AIRPAY」 — **THB 30 per ticket service fee plus a 3% payment services fee on card, TrueMoney and AirPay.** The customer bears it: 「ค่าธรรมเนียมการชำระเงิน… เป็นค่าบริการจากทางผู้รับชำระ… ทาง Thaiticketmajor **ไม่ได้มีส่วนรับผิดชอบ**」.

### ⚡ The abandonment mechanic — dated, first-party, and sharp
> 「ชำระด้วยเงินสดที่จุดรับชำระเคาน์เตอร์เซอร์วิสทุกสาขา **ภายในระยะเวลา 5 ชั่วโมง** หลังจากทำรายการสั่งซื้อเสร็จสมบูรณ์แล้ว หากท่านไม่ได้ชำระเงินภายในระยะเวลาที่กำหนด **หมายเลขการสั่งซื้อของท่านจะถูกยกเลิกโดยอัตโนมัติ**」
>
> **Cash at Counter Service: 5 hours to pay, or the order auto-cancels.** Phone orders get 24 hours. Refunds take **15 business days**.
>
> This is structurally the same finding as Peach Aviation's 24-hour konbini auto-cancel — a hard, merchant-documented window where a reserved seat becomes a lost sale.

### Distribution network — why this is an offline business
「ซื้อที่จุดจำหน่าย Thaiticketmajor **14 สาขา** / โรงภาพยนตร์ **Major & EGV** / **Tesco Lotus** / **BigC** / Website / Call Center / **ที่ทำการไปรษณีย์ไทย**」
— 14 own branches, Major & EGV cinemas, Tesco Lotus, BigC, website, call centre (**02 262 3456**), and Thailand Post. **Six of the seven channels are offline.**

### Legal entity — CONFIRMED
| Field | Value |
|---|---|
| Thai name | **บริษัท ไทยทิคเก็ตเมเจอร์ จำกัด** |
| English name | **THAITICKETMAJOR COMPANY LIMITED** |
| **DBD registration** | **0105543020073** (former: (5)382/2543) |
| Registered | **25 February 2000** |
| Status | Operating (ยังดำเนินกิจการอยู่) |
| Registered address | **3199 Maleenont Tower, 27th Floor, Rama IV Rd, Khlong Tan, Khlong Toei, Bangkok** |
| **Registered capital** | **THB 10,000,010** (~USD 310k) |
| TSIC | 79909 — other reservation services |

⚠️ **Legacy-name flag:** the same registration number appears under the title **"THAITICKETMASTER COMPANY LIMITED"** on a registry mirror — consistent with a rename. **Older PSP or contract records may still say "Thaiticketmaster."** `[INFERENCE, not confirmed]`

📌 **Maleenont Tower is the BEC-Tero / Tero Entertainment HQ**, which corroborates the Tero founding link in the press release.

### 💥 The "~$50M est." revenue premise is REFUTED
The only filed figure surfaced is **THB 174,998,253.20 total revenue / THB 14,750,771.42 net profit, FY2020 ≈ USD 5.6M** — about **one-ninth** of the target-list figure.

⚠️ **Heavily caveated:** `[UNVERIFIED — search summary only]`, the source URL 404'd, **and FY2020 is a COVID year** with Thai live events shut for much of it. **It is a floor, not a run-rate.**

**Two independent reasons the $50M cannot stand as revenue:**
1. **Registered capital is THB 10,000,010 (~USD 310k)** and a registry's own computed valuation is **THB 193M (~USD 6M)** — both confirmed by fetch. Implausibly thin for a USD 50M-revenue business.
2. **Statista puts the entire Thai event-ticket market at ~USD 187.5M by 2028** `[UNVERIFIED — search summary]`. USD 50M of *revenue* would be ~27% of the whole market's value accruing to one commission-based agent.

**Most likely reading: the $50M is GMV mislabelled as revenue, or an unsourced guess.** Ticketing companies book commission, not GMV. **This is the THIRD unsourced TAL revenue figure refuted this week** (after Peatix and Oztix).

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not generated — **deliberately withheld.** Two live blockers (ownership, volume) and Phase 2 research not run. **Do not run `/full-outreach` until both are resolved.***

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ⚠️ SCOPE — read before scoring this account
**This is Phase 1 only, plus my own first-hand technical recon. Agents 2–5 (PSP stack, APMs, complaints/news, competitors) were NOT run — a deliberate stop once two blockers surfaced.**

**Consequently: orchestration status, PSP identity, complaint patterns, competitor stacks and job postings are all UNRESEARCHED, not absent.** Any score computed now would read ~2/29 because those rows are 0 by default. **That is not a finding and must not be filed as a rejection.**

### 🧱 Technical access map — every standard technique is CLOSED here
Verified first-hand 2026-09-20. **This is the hardest-to-research ticketing account in the pipeline.**

| Route | Worked on | ThaiTicketMajor |
|---|---|---|
| Zendesk help-centre API | Ticketek, Moshtix, eplus, Indodax, Azar | ❌ **`help.` and `.zendesk.com` both redirect to `/hc/en-us/restricted`** — sign-in gated; API behind Cloudflare |
| Un-WAF'd payment subdomain | Ticketek (`pay.ticketek.*` → Softix PayGate) | ❌ **`payment.thaiticketmajor.com` resolves but is 403** |
| Un-WAF'd CDN bundle | Moshtix (`cdn.moshtix.com.au`) | ❌ `static.` NXDOMAIN |
| Wayback checkout | Jetstar, Ticketek | ❌ only an **`/intro-2018/` splash page**, jQuery-era, assets `v=20220907` — no payment content |
| **B2B / corporate host** | **Oztix (`/about/`)** | ✅ **THE CRACK — `corporate.thaiticketmajor.com` is OUTSIDE the WAF** (36KB home, 96KB policies) |

**WAF: Akamai** (`errors.edgesuite.net` block page) on `www`, `m.` and `payment.` — **the same vendor fronting Ticketek.**

> 🧰 **Technique note for the repo:** the **B2B/corporate-host route** has now worked twice — Oztix `/about/` and ThaiTicketMajor `corporate.`. **When a consumer estate is WAF'd, try `corporate.`, `business.`, `/about/` and `/policies` before giving up.** Also note `event.thaiticketmajor.com` **is** WAF'd (403) despite being indexed — indexed ≠ fetchable.

### Ownership — confirmed and unresolved parts
**A. Ticketmaster / Live Nation — CONFIRMED from Ticketmaster's own press release** (21 Jul 2022, `business.ticketmaster.com`). Part acquisition, scheduled to complete Q3 2022. **Percentage, price and completion NOT established.**

**B. Major Cineplex (SET: MAJOR) held 40%** — an **associate stake, not a parent relationship**. Sourced to MAJOR's 4Q2013 analyst deck and AR2019 `[UNVERIFIED — search summary only, PDFs not fetched]`; TTM still appears in MAJOR's related-transactions disclosure. ⚠️ **Do NOT describe ThaiTicketMajor as a "Major Cineplex subsidiary."** Whether MAJOR still holds 40%, was diluted, or sold into the Ticketmaster deal is unknown.

**C. Origin.** Founded **1999 by Tero Entertainment** (confirmed in the Ticketmaster release). A 2007 merger of Thaiticketmaster with Major Ticketing to form Thaiticketmajor is `[UNVERIFIED — search summary only]`. **CB Insights' "founded 1990" is inconsistent with the DBD registration and is wrong — do not use it.**

### Other findings
- **Market share: 90% of Thai performance tickets** — queue-it.com case study, fetched. **This is a vendor marketing claim**, not an independent measure.
- **8 million tickets cumulative** across 800+ experiences over 20+ years — same source, **explicitly cumulative and undated.**
- **Queue-it is confirmed in use** (virtual waiting room) — consistent with the 15.87 pages/visit and with high-demand on-sales.
- DBD filings for **FY2021–FY2025 exist but are paywalled** (Creden 300+ points; DataforThai returned 403).

### What could NOT be established
1. **Any revenue figure after FY2020.** Filings exist; paywalled.
2. **GMV, average ticket price, annual tickets sold.**
3. **⚠️ The online-vs-counter transaction split** — *the single most decisive missing number.* It alone determines the volume gate.
4. **Post-2022 shareholding** — Ticketmaster %, price, completion; Major Cineplex's current %.
5. **Directors and shareholder register** — paywalled at both registry mirrors.
6. **PSP identity, orchestrator status, APM set, complaints, competitor stacks** — Phase 2 not run.
7. **PromptPay** — absent from the fee clause but the clause is not a closed enumeration.

### Manual research recommendations
> **Area:** Online vs counter transaction split. **Why:** decides the volume gate, which decides the account. **Action:** ask on a discovery call, or buy the DBD filing (FY2021–2025) via Creden to get post-COVID revenue.
>
> **Area:** Ticketmaster stake and whether it closed. **Why:** decides whether payments sit in Bangkok or with Live Nation globally. **Action:** check MAJOR's SET one-report filings for the disposal, and Live Nation's 10-K subsidiary exhibit.
>
> **Area:** Live checkout. **Why:** PromptPay presence, PSP identity and 3DS are all unknown and the estate is WAF'd. **Action:** a Thai-IP browser session on a real on-sale.

### Overall research confidence — **MEDIUM on entity and methods, LOW on everything commercial**
**High** on the legal entity (registry-confirmed), the accepted-method set and fee structure (first-party terms, fetched and parsed by me), the access map (first-hand), and the Ticketmaster relationship (primary press release).

**Low** on revenue (one unverified COVID-year figure), volume (two derivations disagreeing 2.5×), and everything Phase 2 would have covered. **Traffic was estimated, not supplied**, which costs two ICP signals.

</details>
