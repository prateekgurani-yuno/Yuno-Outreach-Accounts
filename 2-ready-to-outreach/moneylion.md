# MoneyLion

**Status:** 🔴 Not ICP — rejected at the Phase 0 territory gate ("HQ'd west of Dubai with no APAC operations"). **Saved to `2-ready-to-outreach/` on request; run `/mark_not_icp MoneyLion` to move it to `not-icp/`.**
**ICP Score:** Not scored — rejected at the Phase 0 qualification gate, before scoring
**Industry:** US consumer fintech (cash advances, banking, credit-builder, investing, marketplace) · **HQ:** United States: New York, NY per search summaries; T&Cs mailing address is Tempe, AZ (Gen Digital's HQ). Wholly owned by **Gen Digital** since 2025-04-17. · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** N/A

---

## Rejection Rationale

**Out of territory. MoneyLion has no APAC customers and no APAC payment volume. Its products are open only to US residents. Its one APAC presence is an engineering office in Kuala Lumpur, which is a cost centre and does not take payments.**

1. **US residents only, in MoneyLion's own terms.** The T&Cs say the platform is for *"legal residents of the United States"* and that users must *"Reside in the United States"*. The operator is **MoneyLion Technologies Inc.**, with mailing address *60 E Rio Salado Pkwy #1000, Tempe, AZ 85281*. [moneylion.com/terms-and-conditions](https://www.moneylion.com/terms-and-conditions/) (fetched 2026-10-19)
2. **The banking product has the same restriction.** RoarMoney requires users to be *"a resident of the fifty (50) United States or the District of Columbia"*. [moneylion.com/checking-accounts/roarmoney](https://moneylion.com/checking-accounts/roarmoney) `[UNVERIFIED — search summary only, page not fetched]`
3. **Supplied traffic says the same thing.** 97.39% of moneylion.com web traffic is US, and Puerto Rico (a US territory) adds another 0.56%. The only APAC markets in the top 10 are India at 0.23%, Australia at 0.10%, Malaysia at 0.10% and Japan at 0.08%. That is consistent with diaspora, staff and bot traffic, not demand. MoneyLion cannot serve customers in those markets anyway (point 1). See the traffic section below.
4. **The Malaysian presence is engineering only.** Kuala Lumpur is MoneyLion's main technology hub. There are live engineering postings there: Backend Engineer II (Mar 2026), Mobile Engineer II (Jan 2026) and Director of Engineering, R&D. Some of these name **Gen** as the employer. [edisonpartners: Backend Engineer II](https://jobs.edisonpartners.com/companies/moneylion/jobs/70169300-backend-engineer-ii-moneylion) · [builtin: Director of Engineering, R&D](https://builtin.com/job/director-rd/2788972). A 2021 Edge Malaysia piece puts the team at 250+ technologists. [The Edge Malaysia](https://theedgemalaysia.com/article/tech-moneylion-%E2%80%94-american-digital-bank-powered-malaysians) `[UNVERIFIED — search summary only, page not fetched; 2021, headcount stale]`. **No Malaysian or other APAC product, licence or customer offering was found.** An engineering office does not move payment volume, so the gate's "APAC operations" exception does not apply.

**Where the buying centre sits:** this is a US account. Payments for MoneyLion are decided either in the US business or at **Gen Digital** group level. Gen Digital already has a full report in this repo: [`2-ready-to-outreach/gen-digital.md`](gen-digital.md) (17/29, override down to 🟢). Any MoneyLion angle belongs in that thread, not in a separate SDR sequence.

### Why the other Phase 0 rules don't change the answer
| Rule | Result |
|---|---|
| PSP / gateway / acquirer / orchestrator | Not fired. MoneyLion is a consumer fintech, not a payment-infrastructure vendor. `[INFERENCE, not confirmed]`: it does run money movement (advances, debit card) through bank partners, but it sells to consumers, not merchants. |
| Existing Yuno customer | Not checked. No evidence either way. |
| No online payment volume | Not fired. It has volume, all of it in the US. |
| HQ west of Dubai, no APAC operations | **FIRES** (above) |
| Monthly transactions < 40,000 | Not assessed. Per the traffic file caveats, web traffic cannot size this (see below). Moot, since the territory gate already fires. |

---

## Gen Digital thread: the only usable APAC-team signal

These items are already in `gen-digital.md` and are repeated here only so this file stands alone:
- 💼 **MoneyLion eCommerce Senior Billing Performance Analyst**, posted 2026-01-16, built around a weekly "Billing Success Rate". Aggregator listing; open status not confirmed. [edisonpartners](https://jobs.edisonpartners.com/companies/moneylion/jobs/65287990-ecommerce-senior-billing-performance-analyst)
- 🤝 **The acquisition closed on 2025-04-17**, at roughly $1B. [Nasdaq / Gen press release](https://www.nasdaq.com/press-release/gen-completes-acquisition-moneylion-accelerating-companys-leadership-financial)
- 🧠 **Norton Financial Scan** (MoneyLion AI) is rolling out to Norton 360 customers in Gen's largest markets. [Gen Q1 FY27](https://newsroom.gendigital.com/2026-08-06-Gen-Further-Accelerates-in-Q1-FY27-and-Raises-Full-Year-Guidance). This is MoneyLion technology going into Norton's existing footprint, which already includes APAC. It does not take MoneyLion's own payment flows outside the US.

**What this means for Gen outreach:** MoneyLion's billing-success hire is a reasonable talking point inside the Gen sequence. Point it at Norton/Avast renewal recovery in APAC, not at MoneyLion.

---

## Traffic: SimilarWeb (supplied 2026-10-19), with caveats

**Source:** `accounts/traffic/moneylion.md`. Similarweb Sales Intelligence, Jul–Sep 2026, worldwide, desktop + mobile web, moneylion.com only.
**Avg monthly visits:** 6.227M (18.68M over 3 months) · **Device:** Mobile web 90.92% / Desktop 9.08% · **Global rank:** not captured

| Rank | Country | Traffic Share | Est. Monthly Visits |
|---|---|---|---|
| 1 | United States | 97.39% | ~6.06M `[DERIVED from supplied share, not a SimilarWeb figure]` |
| 2 | Puerto Rico | 0.56% | ~35K `[DERIVED]` |
| 3 | India | 0.23% | ~14K `[DERIVED]` |
| 4 | Canada | 0.20% | ~12K `[DERIVED]` |
| 5 | United Kingdom | 0.18% | ~11K `[DERIVED]` |
| 6 | Saudi Arabia | 0.14% | ~9K `[DERIVED]` |
| 7 | Australia | 0.10% | ~6K `[DERIVED]` |
| 8 | Malaysia | 0.10% | ~6K `[DERIVED]` |
| 9 | Norway | 0.10% | ~6K `[DERIVED]` |
| 10 | Japan | 0.08% | ~5K `[DERIVED]` |

**Caveats, from the supplied file:**
1. **This is the Sales Intelligence view**, which gives top-10 shares only. The supplied file has no per-country visit counts. The figures above are share × 6.227M, done by me.
2. **Single domain.** moneylion.com is the only domain supplied, and no regional domains were checked. That is moot for a US-only product.
3. **App traffic is excluded.** MoneyLion is app-first: advances, banking and card spend happen in the app, so web visits understate activity heavily.
4. **Do not size transaction volume from this data.** The country split is a market-mix signal only, and here it shows effectively zero APAC demand.
5. **Home-country share is 97.39%** (97.95% including Puerto Rico). The "high traffic outside home" signal would fail even if the account were scored.

---

## Overall Research Confidence

**High for the rejection, and nothing else was researched.** I fetched the territory finding directly from MoneyLion's T&Cs, and the supplied traffic backs it up independently. The other evidence (KL office, RoarMoney eligibility, NY HQ) comes from job listings and search summaries and is labelled that way. None of it would reverse the verdict. Phases 1–3 (PSP stack, APMs, complaints, competitors) were deliberately not run, as the Phase 0 gate requires.

## Manual Research Recommendations

> **Area:** Any plan to launch MoneyLion outside the US
> **Why it matters:** This is the only development that would bring MoneyLion into APAC scope. Today the KL office is engineering only.
> **Suggested manual action:** Watch Gen earnings for a MoneyLion launch outside the US, or for an APAC-licensed MoneyLion product. If one appears, re-run `/research MoneyLion`.

> **Area:** HQ city
> **Why it matters:** Small. Search summaries say New York; the T&Cs mailing address is Tempe, AZ (Gen's HQ). Either way it is US, so the verdict holds.
> **Suggested manual action:** None needed for qualification.

## Appendix: Source URLs
- https://www.moneylion.com/terms-and-conditions/ (fetched)
- https://moneylion.com/checking-accounts/roarmoney (search summary)
- https://jobs.edisonpartners.com/companies/moneylion/jobs/70169300-backend-engineer-ii-moneylion
- https://builtin.com/job/director-rd/2788972
- https://theedgemalaysia.com/article/tech-moneylion-%E2%80%94-american-digital-bank-powered-malaysians (search summary)
- https://jobs.edisonpartners.com/companies/moneylion/jobs/65287990-ecommerce-senior-billing-performance-analyst
- https://www.nasdaq.com/press-release/gen-completes-acquisition-moneylion-accelerating-companys-leadership-financial
- https://newsroom.gendigital.com/2026-08-06-Gen-Further-Accelerates-in-Q1-FY27-and-Raises-Full-Year-Guidance
- `accounts/traffic/moneylion.md` (SimilarWeb, supplied 2026-10-19)

*Marked: 2026-10-19*
