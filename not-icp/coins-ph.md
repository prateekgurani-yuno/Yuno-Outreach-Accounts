# Coins.ph

**Status:** 🔴 **Not ICP — Phase 0 gate: payment infrastructure. Routes to Partnerships.**
**ICP Score:** Not computed. The gate fires before scoring, per `CLAUDE.md` and `/research` Phase 0.
**Industry:** Crypto exchange, e-money wallet **and payment infrastructure** · **HQ:** Taguig City, Philippines · **Researched:** 2026-09-25 · **First email sent:** —
**Motion:** — *(none; not a sales account)*

---

> ## 🛑 WHY THIS STOPPED
>
> `CLAUDE.md`: *"All industries with the exception of PSPs and payment infrastructure companies (Adyen, Stripe, Checkout.com, Razorpay, PayU, Juspay, **2C2P**, Xendit, Midtrans, etc.). If a prospect turns out to be one, stop and flag rather than researching it — those route to Partnerships."*
>
> **Coins.ph is on the same BSP registry as 2C2P, sells a product it calls a payment gateway, and lists PSPs as a customer segment.** Three of those facts are primary and two I verified myself. The research was stopped at that point rather than completed.

<details open>
<summary><h2>📊 Section 1 — The gate, and the evidence</h2></summary>

### 1. The regulator files them as payment infrastructure, alongside a company named in our own exclusion list

Both Philippine entities appear on the **"List of BSP-Registered Operator of Payment System (OPS)"**, as of **28 August 2026**:

| Entity | OPS registration | Issued | Trade names |
|---|---|---|---|
| **Betur, Inc.** | `OPSCOR-2020-0051` | 24 Mar 2020 | Coins.ph; Coins Pro |
| **DCPAY Philippines, Inc.** | `OPSCOR-2020-0048` | 21 Mar 2020 | Coins.ph |

Source: `https://www.bsp.gov.ph/PaymentAndSettlement/COR.pdf`

**The same 314-entry registry contains 2C2P Philippines (`OPSCOR-2020-0081`), AIPH Merchant Services / Ant International, Paynamics, PayMongo and Ksher Philippines.** 2C2P is named explicitly in the `CLAUDE.md` exclusion list. This is not an analogy — it is the same list, maintained by the same regulator, under the same category.

### 2. They sell a payment gateway — verified by me

`https://www.coins.ph/en-ph/webpay` — the page's own `<title>`, fetched 2026-09-25:

> **"Coins WebPay - The Trusted Payment Gateway in the Philippines | Coins.ph"**

API-based checkout, settlement, reconciliation, and accepted methods listed as **"Coins PH / QRPh / Credit and Debit Card"**, priced per successful transaction.

### 3. They target PSPs as a customer segment — verified by me

`https://www.coins.ph/en-ph/business`, fetched 2026-09-25, verbatim:

> **"Payment Service Providers (PSPs) — Scale your network with our robust, regulated digital asset infrastructure. Contact Sales"**

Same page: *"Trusted by 2,000+ Verified Businesses"*, *"2000+ Merchants"*, *"$20B Total Volume Processed in 2025"*, and *"In-store QR codes, plus **credit card acceptance through POS terminals**."*

### 4. The CEO says the company has become infrastructure

Wei Zhou, interviewed 22 Aug 2026, published 23 Sep 2026 (`https://bitpinas.com/feature/coinfest-asia-wei-zhou-coins-ph-interview/`):

> Retail crypto is *"deader than dead"* · *"If B2C is dead, you got to figure out how to get into the B2B world"* · the company *"completely pivot[ed] into backend financial infrastructure"* · aiming to be *"a **global digital clearinghouse**"*

Named customers: *"cross-border businesses, payment aggregators, and remittance platforms."* He positions on price against **Wise** (*"Wise can't get lower than 40 to 50 bips, whereas we let them get to 5 bips"*) and pitches banks to plug in for stablecoin liquidity. Roughly **$100M/day** in USDT/USDC↔PHP.

</details>

<details open>
<summary><h2>🔍 Section 2 — The second reason: even setting the gate aside, there is no deal here</h2></summary>

**This matters, because the exclusion could be argued.** They *are* also a consumer exchange with a large retail base. So the question worth answering is: if we ignored the gate, what would Yuno actually sell them?

**Almost nothing. Their merchant-side surface is close to empty.**

| Consumer cash-in channel | Third party in the path? |
|---|---|
| InstaPay | ❌ No — reached directly as a BSP-licensed EMI / OPS / clearing participant |
| PESONet | ❌ No — same |
| Intrabank direct transfer (UnionBank, Sterling Bank of Asia, Security Bank) | ❌ No |
| Crypto deposit | ❌ No — on-chain |
| **Over-the-counter cash at remittance centres** | ✅ **Yes — Dragonpay** (Palawan, Cebuana Lhuillier, M Lhuillier, Pera Hub, Villarica; ₱25 fixed fee) |

⭐ **And there is no card cash-in at all.** Four separate help-centre searches found no card-funding article; every card reference is about *paying* credit-card bills through the wallet, not funding with one. Sources: `support.coins.ph` articles `201322620` (updated 17 Aug 2026), `115000164002` (23 Jun 2026), `28522311646617` (9 Jul 2026).

**So Yuno's core pitch has nothing to attach to.** No card acquiring means no approval-rate problem, no MDR on funding, no cross-border decline surface, no PSP diversification argument. **One third-party channel, Dragonpay, out of five** — and its share is not published anywhere.

**The clean asymmetry:** where they behave like a merchant (consumer cash-in, PH and TH), they have essentially no third-party acquiring to orchestrate, because their licences let them reach the rails directly. Where they have real payment volume, multi-rail complexity and spend ($100M/day, 2,000+ merchants, cards, QR, disbursement, cross-border), **they are the provider, not the buyer.** The two halves do not overlap.

And the merchant-shaped half is the **shrinking** half, by the CEO's own account.

</details>

<details>
<summary><h2>📚 Section 3 — Research captured before the stop</h2></summary>

The run was halted at the gate, so this is partial by design. Recording it because it is verified and because the competitive intelligence is reusable.

## Rejection Rationale

Coins.ph is a **BSP-registered Operator of Payment System** listed alongside 2C2P — a company named explicitly in the `CLAUDE.md` PSP exclusion — it markets a product titled *"The Trusted Payment Gateway in the Philippines"*, and it sells to **Payment Service Providers** as a named customer segment. Its CEO describes the company as having *"completely pivoted into backend financial infrastructure."* Independently of the gate, the account also fails on substance: of five consumer cash-in channels, four are rails Coins reaches directly under its own EMI/OPS licences and **no card funding exists at all**, leaving a single third-party channel (Dragonpay OTC) of unpublished size. **Routes to Partnerships.**

## Licences held — useful for the Partnerships conversation

| Regulator | Licence | Entity, as the regulator spells it | Source |
|---|---|---|---|
| **BSP** | VASP (active, non-bank, entry #1) | **Betur Inc. (doing business under the name and style of COINS.PH)**, CEO Wei Zhou | `bsp.gov.ph/Lists/Directories/Attachments/19/VASP.pdf`, as of 15 Jul 2026 |
| **BSP** | EMI (non-bank FI, entry #5) | **DCPAY Philippines, Incorporated** | `bsp.gov.ph/Lists/Directories/Attachments/7/emi.pdf`, as of 31 May 2026 |
| **BSP** | Operator of Payment System ×2 | Betur `OPSCOR-2020-0051`; DCPay `OPSCOR-2020-0048` | `bsp.gov.ph/PaymentAndSettlement/COR.pdf`, as of 28 Aug 2026 |
| BSP | RTC, Money Changing, FX Dealing, Virtual Currency Exchange | Betur Inc. | Company help centre only — ⚠️ not confirmed against a BSP directory |
| BSP | "Type A" EPFS — claimed as *"first VASP granted a Type A EPFS license, traditionally reserved for banks"* | "Coins.ph" | Company press release |
| BSP | PHPC peso stablecoin, **regulatory sandbox** (not a standing licence) | "Coins.ph" | Company whitepaper |
| SEC Thailand | Digital asset business operator (broker/dealer claimed) | **Coins TH Co., Ltd.** | ⚠️ Company sources only — `sec.or.th` returned 403 to every attempt |
| FSC Mauritius | **In-principle approvals only**, 4 VASP classes | Coins Digital Markets Limited | Company blog |
| AUSTRAC | Digital Currency Exchange registration | not named | `[UNVERIFIED — search summary only]` |
| SEC Philippines | **CASP — NOT held.** CEO, Aug 2026: *"nobody has it yet"* | — | BitPinas interview |

⚠️ **Two corrections to what is commonly reported about this company:**
1. **Betur does NOT hold the EMI licence.** Their own help centre says it does. Betur appears **zero times** in the BSP EMI list; only DCPay is listed. Their marketing conflates two entities.
2. **The "26 licenses" claim is "Approved *and In-progress*"** — their own wording, not 26 held.

## Entities

- **Betur, Inc.** — TIN `008-475-986-00000`, BIR-registered 16 Apr 2013, 15/F Asian Century Center, BGC Taguig
- **DCPAY Philippines, Inc.** — TIN `009-298-336-00000`, BIR-registered 10 Jun 2016, 35/F Eco Tower, BGC Taguig
- Both named as contracting parties: *"Betur, Inc. and DCpay Philippines, Inc., doing business as 'coins.ph'"*. Philippine law, PDRCI arbitration, seat Taguig.
- **Coins TH Co., Ltd.** — Bangkok. Assets custodied with **BitGo Trust Company, Inc.**
- **Ownership — the Gojek fact is stale.** Acquired by Gojek 2019, **divested April 2022 to Wei Zhou (ex-Binance CFO) and Joffre Capital** at ~$200M. No 2024–2026 change found. Group structure above the PH entities is unresolved: a 2023 AFS references a Singapore parent "GCT", while a commercial database lists Betur as a 99.99% subsidiary of DCPay. Neither verified against a registry.

## ⚠️ The TAL revenue figure is refuted

The target list carries **"~$50M est."** From **Betur Inc.'s 2023 Audited Financial Statements** filed with the Philippine SEC:

| Betur Inc. | FY2022 | FY2023 |
|---|---|---|
| Revenue | ₱929.6M (~$16.5M) | **₱112.9M (~$2.0M)** — down 87.8% |
| Net loss | ₱970.5M | ₱1.09bn |
| Equity | — | **negative ₱666.7M** |

The auditor issued a **going-concern material uncertainty**, and the AFS states Betur **failed BSP capitalisation requirements**. Also disclosed: customer crypto reserve deficits, largest a 5,556,161 XRP shortfall (₱192M) traced to an Oct 2023 hack. The CEO's on-record response is that capital has since been infused and that *"Betur represents only one entity within our broader group"*; Coins said it would refile the 2023 AFS. **No refiled version and no 2024–2026 AFS is public.**

**~$50M is off by roughly 25× for the entity that holds the crypto licence, and unconfirmable at group level.** Do not use it.

## ⚠️ The user counts are stale marketing copy

*"16 million+ registered users, 7 million+ monthly active"* appears on the live About page — and the **same boilerplate appears in a December 2022 press release.** The numbers have not moved in ~4 years of website copy. Treat as undated marketing, not disclosure.

## What I found first-hand in their production bundles

Recorded because it is good technique and reusable, not because the account proceeds.

**Six currencies, five corridors, at least five named providers** — all from their own i18n dictionaries:

| Currency | Rail | Provider named in their code |
|---|---|---|
| PHP | InstaPay, PESONet, OTC cash | **Dragonpay** (OTC reference numbers at remittance centres) |
| THB | PromptPay QR bank transfer | not named |
| **BRL** | **Pix** | **Stark Bank** (`starkBank.title = "Brazilian Real BRL"`) |
| **EUR** | SEPA via virtual IBAN | **Clear Junction** (`clearJunction.title = "Euro"`, Setup IBAN / Create IBAN) |
| **AUD** | **PayID** + BSB bank transfer | not named |

Business-side partner list, *"Trusted by 2,000+ Verified Businesses"*: BCRemit, BDO Unibank, GCash, Higlobe, InstaPay, Mastercard, Maya, PESONet, **Pix**, Remitly, SEPA, UnionBank, Veem, Visa, **Xendit**.

⭐ **The best artefact on the account — a combinatorial outage matrix.** They ship seven pre-written messages covering every single and paired failure of their three Philippine rails:

```
alertPHP1 = "{{type}} services are currently unavailable. Please try again later."
alertPHP2 = "InstaPay & PESONet are currently unavailable..."
alertPHP3 = "InstaPay & Over the counter (OTC) are currently unavailable..."
alertPHP4 = "PESONet & Over the counter (OTC) are currently unavailable..."
alertPHP5 / 6 / 7 = the same, per individual rail
```

Nobody ships seven of those translated unless rails go down often. **The documented remedy in every one is "please try again later" — the user waits, there is no failover.** In a different company this would be the hook of the year. Here, the rails going down are rails they operate themselves.

Also theirs, verbatim: `common.cashin.partnerNotice` = *"All non-PHP funds are held and processed by third-party partners."* And on the Thai flow: *"Deposit from a bank account in your name only (**TrueMoney, Paotang, and other e-wallets are not supported**)."*

## ⚠️ Traffic data caveat

`accounts/traffic/coins-ph.md` holds the supplied SimilarWeb snapshot (Jun–Aug 2026, 53 countries, Philippines 86.99%). **The "include all country domains" toggle was OFF**, and I verified `coins.co.th` is a live sibling on the same codebase, so Thailand is entirely absent and 86.99% is a domain-level share. The non-PH rows are also bounce-level (US 22 seconds, Australia 16 seconds) and are unlikely to be users. The file is kept for reference; it was never used to score this account.

## 🔎 One thing worth a second look — Coins TH

**`coins.co.th` is a materially different shape from the parent** and is the one part of this group that looks like an ordinary merchant:

- Crypto exchange only. **No wallet, no bills payment, no EMI, no merchant or business products.**
- Funded by THB bank transfer from local banks; assets custodied with a third party (BitGo).
- Its Thai terms explicitly contemplate **"third party cash-in providers."**
- **No Thai EMI or payment-operator licence found.**

So Coins TH plausibly *does* buy acquiring rather than provide it. ⚠️ **But it is small, its volume is unpublished, and it sits under a parent that routes to Partnerships** — pitching the subsidiary while the group is a partner conversation is the kind of thing that goes wrong in a QBR. **Raise it with Partnerships rather than opening it as a separate sales account.**

## Source Notes

- ✅ **WebPay page title** and the **PSP customer-segment line** — fetched and read by me, 2026-09-25
- ✅ **BSP VASP, EMI and OPS registries** — agent pulled the actual BSP PDFs and extracted text with pypdf after `bsp.gov.ph` blocked normal fetches; figures are from the documents, not search summaries
- ✅ **BIR Certificates of Registration** for both entities — published by the company at `coins.ph/en-ph/legal`
- ✅ **Betur 2023 AFS figures** — Philippine SEC filing, reported by BitPinas
- ✅ **Cash-in channel list** — company help centre, four articles, all dated 2026
- ✅ **The i18n findings** (Stark Bank, Clear Junction, Dragonpay, the alertPHP matrix, the partner list) — mined and context-printed by me from the live bundles
- ⚠️ **SEC Thailand licence** — company self-description only; `sec.or.th` 403'd every attempt
- ⚠️ **Philippine SEC registration numbers** — not obtained; `sec.gov.ph` 403, ESPARC redirect-loop. BIR TINs used instead
- ⚠️ **Group/consolidated financials** — none public
- ⚠️ **Dragonpay's share of cash-in** — not published. This is the one number that could have changed the substance conclusion
- ❌ **Three of four research agents were stopped** at the gate. PSP-stack, complaints and competitor work is incomplete by design

## 🪤 False positives caught on this account

- ⭐ **`OTC` is genuinely ambiguous here and it is a trap.** In Philippine payments it means convenience-store cash; in crypto it means block trading. Coins.ph has an **"OTC / FX" trade desk** in its nav, and 135 of 135 raw `otc` hits on the PH homepage were CSS class names plus that nav item. The real OTC-cash evidence came from elsewhere entirely.
- **`bux` → `mui-m8ibux`**, a CSS class. BUX is a real Philippine gateway, so this would have looked convincing.
- **`omise` → `Promise`.** The usual.

</details>
