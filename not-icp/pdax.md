# PDAX

**Status:** 🔴 Not ICP — **Phase 0 qualification gate: payment infrastructure / e-money issuer**
**ICP Score:** not scored — the gate fired before research
**Industry:** Crypto & Digital Assets — Philippine Digital Asset Exchange · **HQ:** Philippines (`pdax.ph`) · **Researched:** 2026-10-06
**Route to:** 🤝 **Partnerships**

---

## Rejection Rationale

**PDAX is excluded by CLAUDE.md on two independent grounds, both evidenced from PDAX's own website and both verified first-hand.** The `/research` Phase 0 gate instructs me to **stop and flag rather than research** when a prospect turns out to be a PSP, gateway, acquirer, e-money issuer or payment infrastructure company. It fired, so the fiat-rail, financials, orchestrator and complaints work was **not** completed.

### Ground 1 — PDAX holds an EMI (Electronic Money Issuer) licence, not just VASP

**I fetched `https://pdax.ph/caas/` myself (HTTP 200, 90,716 bytes).** Verbatim from the page:

> **"Remittance & Transfer Company (RTC)** — Facilitate remittances and money transfers · Convert foreign currencies to PHP"
>
> **"Electronic Money Issuer (EMI)** — Transact using PDAX E-wallet · **Enable pay-outs to banks and other e-wallets**"

And the page's own description of who it sells to:

> "…for financial apps, **payment providers**, and fintech platforms. However, building the infrastructure from scratch takes time and resources. With PDAX Platform Solutions, you can integrate tokenized asset solutions into your platform whether for remittances, **payment**, trading, or treasury."

PDAX's commercial B2B page states it leverages its **"VASP, RTC, and EMI licenses"** from the Bangko Sentral ng Pilipinas **so that partners do not need their own.**

**Electronic money issuers are explicitly on the CLAUDE.md exclusion list.**

Third-party corroboration that PDAX holds an EMI licence: PDAX appears as entry **"24. PDAX"** in the EMI-NBFI section of a compiled Philippine EMI list (data as of 30 Sep 2020) — `bitpinas.com/feature/list-electronic-money-issuers-emi-license-philippines/`. ⚠️ That page does **not** claim to reproduce BSP's own register verbatim.

### Ground 2 — PDAX sells cross-border payments, payroll payouts and merchant settlement to third parties

**`https://pdax.ph/remittance/` (fetched, HTTP 200, 81,040 bytes)** markets **PDAX Remit** to *"remittance companies"* and *"businesses and financial partners"*, offering:
- **B2B payments** — cross-border settlement
- **Remittances** — stablecoin-rail transfers *"settled locally in PHP"*
- **Payroll** — employee and freelancer payouts
- **Merchant payments** — *"PHP settlements through stablecoins"*

Payout reach described as *"banks and e-wallets participants to remittance centers, convenience stores, and pawnshops"*, over *"Institution-Grade APIs"*.

**That is a payment-infrastructure product line sold to other financial institutions and to remittance companies. Yuno would be selling orchestration to an entity that itself sells cash-in/cash-out, payout and settlement infrastructure.**

### Verdict
**Payment infrastructure. Route to Partnerships.** The 30,001 visits/month web footprint is **irrelevant to this decision** — the account fails on **licence and product category, not on volume.** The traffic file's own warning (that visits are not transactions and must not be used to reject an app-first exchange) stands and was respected; the volume gate was never reached.

### ⚠️ Contrast with CoinSpot, which was kept in this same batch
CoinSpot also holds a payments licence (an **AFSL for non-cash payments**), but it covers **CoinSpot's own consumer products** — its AUD wallet and its Mastercard — and **CoinSpot sells nothing payments-related to third parties.** PDAX markets payout, settlement and wallet-as-a-service **to other institutions.** **The distinction is what a third party can buy from them.** From CoinSpot, nothing; from PDAX, a payments stack.

---

## Trap corrections worth recording

1. **🛑 PHPX is NOT a PDAX product.** My brief hypothesised PDAX was behind PHPX / the bank-consortium peso stablecoin. **That does not hold up.** PHPX is a bank-collateralised peso stablecoin on Hedera built by **JUST Finance** (an FSCO/Ayannah JV, Singapore-based) with **UnionBank/UBX, RCBC, Cantilan Bank and Rural Bank of Guinobatan** as issuing/governing banks. **PDAX is not named as an issuer or participant in any source seen.** `[UNVERIFIED — search summaries, neither fetched]`. **Do not repeat the PDAX↔PHPX link in any Yuno material.** (PDAX does use stablecoins as its *own* remittance rail per `pdax.ph/remittance/` — a different claim.)
2. **PDAX ≠ PDEX.** The Philippine Dealing & Exchange Corp is a separate regulated securities venue. **No PDEX material contaminated this file** — every cited page is `pdax.ph` or names Philippine Digital Asset Exchange explicitly.
3. **⚠️ PDAX's own "Is PDAX regulated?" help article is thin and outdated.** It cites only the **Sept 2018** virtual-currency-exchange licence under **BSP Circular 944** and says **nothing** about VASP, EMI, RTC or OPS. `support.pdax.ph/support/solutions/articles/1060000097426` (fetched, 200). **The richer licence disclosure is on the commercial CaaS page, not the help centre** — worth knowing if anyone re-checks this account.

## Confirmed baseline facts for the record

- PDAX is an **active BSP-registered non-bank VASP**, alongside Betur Inc. (Coins.ph), Maya Philippines, Moneybees Forex, TopJuan Technologies and WIBS PHP. `[UNVERIFIED — search summary only; BSP's own register page not fetched]`
- Virtual currency exchange licence granted **September 2018** under BSP Circular No. 944 s.2017 — confirmed on PDAX's own support page.
- Institutional product lines: **PDAX Prime** and **PDAX Connect** (CaaS — white-label crypto trading/wallet via API, riding PDAX's licences).

## What was NOT verified, and deliberately not pursued

- **BSP's own published registers.** `bsp.gov.ph`'s VASP, EMI and OPS lists were **not** reached directly. Every licence claim above rests either on PDAX's own marketing page (strong — it is their own statement about themselves) or on third-party compilation. **If Partnerships needs the licence set nailed down, the primary registers on bsp.gov.ph are the next step.** I would not state PDAX's exact EMI/RTC registration numbers or OPS status in writing today.
- **Whether PDAX holds OPS (Operator of Payment System) registration.** Nothing found either way — absence of evidence, not evidence of absence. **Moot for qualification: EMI already triggers the exclusion.**
- **Not researched per the stop-and-flag instruction:** the PHP deposit/withdrawal rail table and fee schedule, monthly fiat transaction estimate, PH SEC entity confirmation, directors (**Nichel Gaba as founder/CEO is UNVERIFIED — not sourced**), funding rounds (**the UnionBank strategic investment and the Tiger Global round are both UNCONFIRMED**; ConsenSys Ventures appeared in results as an investor but was not verified), valuation, user count, trading volume, 2025–26 raises or distress, tokenised government bond distribution, orchestrator classification, payment complaints.

## Research Confidence

**HIGH on the qualification decision. Everything else was correctly left undone.**

- ✅ **Verified first-hand by me:** `pdax.ph/caas/` (HTTP 200, 90,716 bytes) and `pdax.ph/remittance/` (HTTP 200, 81,040 bytes), including the verbatim **"Electronic Money Issuer (EMI) — Transact using PDAX E-wallet, Enable pay-outs to banks and other e-wallets"** and **"Remittance & Transfer Company (RTC)"** licence blocks, and the *"for financial apps, payment providers, and fintech platforms"* positioning.
- Budget used by the research pass: 6 WebSearch, 4 WebFetch (all 200, none blocked, no retries). **No bundle grep was run** — the gate fired before payment-stack work was warranted, and the deposit flow is behind login in any case.
