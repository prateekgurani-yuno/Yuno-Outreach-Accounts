# Indodax

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 12 / 24 → 🟢 Medium
**Industry:** Crypto & digital assets (retail exchange) · **HQ:** Millennium Centennial Center, Jl. Jend. Sudirman Kav. 25, South Jakarta, Indonesia · **Researched:** 2026-09-16 · **First email sent:** —
**Motion:** **Greenfield** — no orchestration layer. Multiple parallel integrations, user picks the rail, no router in between.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Indodax (PT Indodax Nasional Indonesia) is Indonesia's largest retail crypto exchange — ~9.9M members, **Rp201.2 trillion** of IDR-market transaction volume in FY2025 (+51.65% YoY) and >40% domestic market share. It is an OJK-licensed Digital Financial Asset Trader (PAKD). Its entire fiat perimeter is domestic by design: IDR only, Indonesian bank accounts only, in the user's own verified name.

**SimilarWeb total visits (last full month):** **Not public** — paywalled on the public page. Rank and country split are available for **August 2026** and are `[ESTIMATE, not confirmed]`. Global rank #56,112, Indonesia rank #2,692, bounce 36.33%, 6.53 pages/visit, 7m02s average visit. Note the trajectory: global rank has moved **34,715 → 38,679 (May 2026) → 56,112 (Aug 2026)** — a sustained decline in ranked traffic through 2026.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | **Indonesia** | 82.3% | VA (BCA, BRI, Mandiri, Bank INA, Artha Graha) · Direct BCA bank transfer w/ unique code · QRIS · DANA, OVO, GoPay, ShopeePay · Permata VA (Quick Buy USDT only) | **Alfamart/Indomaret retail cash — SOURCED ABSENT.** **LinkAja — SOURCED ABSENT.** Cards & PayPal — explicitly refused | ✅ PT Indodax Nasional Indonesia |
| 2 | Singapore | 4.13% | None — no foreign funding rail | Foreign nationals need **KITAS/KITAP** to verify at all | ❌ none |
| 3 | United States | 1.93% | **None — US citizens are barred from opening an account** | n/a — structurally non-convertible traffic | ❌ none |
| 4 | Vietnam | 0.68% | None — no foreign funding rail | KITAS/KITAP wall | ❌ none |
| 5 | Australia | 0.6% | None — no foreign funding rail | KITAS/KITAP wall | ❌ none |

*"Others" is an undifferentiated 10.37% bucket; SimilarWeb does not publish countries 6–10 for this domain and none was invented.*

### Legal entities
- **PT Indodax Nasional Indonesia** (Indonesia) — registration number **not found**. Founded 2014 (Oscar Darmawan, William Sutanto). Disputes go to the South Jakarta District Court
- **No entity, office or subsidiary outside Indonesia.** Single location confirmed on their own About Us page

### Known PSPs
- **Xendit** — ✅ **confirmed**, biller **"Xendit 87909"** named in Indodax's own Mandiri VA payment instructions `[Source Code / first-party help centre]`
- **PT Bank Rakyat Indonesia (BRI)** — direct bank partnership signed **17 Nov 2020**, named branch head, wire-service reported `[Press Release]`
- **In-house "Direct BCA"** — Indodax's own BCA account with a unique-code manual reconciliation flow
- **QRIS, e-wallet and Permata acquirers — NOT FOUND.** Not named anywhere in a 1,501-article corpus

### Orchestration status
**None detected — direct PSP/bank integrations only (greenfield).** Zero hits across Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno and IXOPAY; no engineering blog, conference talk or payments job posting. Positive evidence points the same way: the rails behave **independently** — different fees, different caps, different settlement times, different per-bank AML rules. The user picks the rail; nothing routes. *Their own T&C refers to "payment gateways" in the plural and names none.*

### Buying signals
- 📋 **They publicly state intent to add deposit methods.** Own FAQ, updated 2026-08-31: *"We'll add more deposit methods in the future to ease your Bitcoin buying process."*
- 🤝 **Three bank co-branding deals in ~12 months** — [BRI debit card, 25 Aug 2025](https://keuangan.kontan.co.id/news/bri-dan-indodax-luncurkan-kartu-debit-co-branding-bri-x-indodax), BNI + Bank INA card, and [Bank INA partnership, 20 Aug 2026](https://investasi.kontan.co.id/news/jalin-kerja-sama-bank-ina-dan-indodax-perluas-akses-perbankan-digital). All **issuing**, none acceptance
- 🚀 **Volume growth +51.65% YoY** — Rp132.6T (2024) → Rp201.2T (2025)
- ⚠️ **OJK summoned management in Jan 2026** over allegedly missing member funds (~Rp600m). Unresolved as of the last reporting found. **Re-check before outreach**
- ❌ **No public payment RFP found.** No payments job posting found

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Indodax` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 12 / 24
| Signal | Points | Status |
|--------|--------|--------|
| Orchestration status | **+4 ✅** | **None detected — greenfield.** Exhaustive negative across all orchestration vendors, plus positive evidence of independent, unrouted rails |
| 3+ countries | **+3 ⚠️** | Literally met — Indonesia 82.3%, Singapore 4.13%, US 1.93% are three countries above 1%. **But see the override note: this is a traffic artifact, not operations** |
| Multiple PSPs | **+3 ✅** | Xendit (Mandiri VA, biller 87909) + direct BRI bank partnership (2020) + in-house Direct BCA manual rail. Three integration types, evidenced |
| Local rail or licensing gap in a top-3 market | **0 ❌** | The dominant Indonesian rails — QRIS, virtual account, the major wallets — are **all present**. Alfamart/Indomaret and LinkAja are genuinely sourced-absent but neither is the dominant rail, and see the note below on why the Alfamart gap is probably deliberate |
| Recent expansion | **0 ❌** | No new market entry. Bank co-branding is distribution, not expansion. No non-Indonesian entity or plan found |
| Payment issues reported | **+2 ✅** | Moderate and dated: Trustpilot 1★ reviews, four mediakonsumen letters (one serious enough that **BCA filed a formal public reply**), and Indodax's own **dedicated per-rail failure FAQs** — self-published evidence each rail generates real support volume |
| Funding >$10M | **0 ❌** | One disclosed round, **Nov 2017**, amount undisclosed. Nothing in the last 12 months |
| High traffic outside home | **0 ❌** | Indonesia 82.3%, well above the 60% threshold |
| Competitor using orchestration | **0 ❌** | Explicit negative — **no Indonesian crypto exchange is orchestrating.** Everyone is single-aggregator |
| Payment job postings | **0 ❌** | None found across JobStreet, Glints, Dealls, LinkedIn |

**Tier:** 12 → 🟢 Medium. **No tier override applied**, but three judgements are recorded below because they matter more than the number.

> ### Analyst notes — read before working this account
>
> **1. The +3 for "3+ countries" is an artifact and I am not treating it as real.** The traffic rule is literally satisfied and sourced, so I awarded it rather than quietly bending the matrix. But it means nothing operationally: **US citizens are barred from opening an account outright** (one of 14 banned nationalities), and every other foreign national needs a **KITAS/KITAP Indonesian residence permit** to complete verification. Withdrawal requires an Indonesian bank account in the user's own verified name. Judged honestly this account is **single-market**, and the working score is nearer **9/24**. Still 🟢 Medium either way, so the tier stands.
>
> **2. Do not pitch cross-border. The thesis is dead and it would get dismantled on the first reply.** Indodax has deliberately closed its fiat perimeter: IDR only, Indonesian banks only, own-name matching, 14 banned nationalities, e-wallet withdrawal killed for AML/CFT. The 17.7% foreign traffic almost certainly funds via **crypto deposit**, which never touches a payment rail. Pitching "unlock your foreign traffic" is pitching against a regulatory posture they chose on purpose.
>
> **3. Cards are not a gap, and neither is Alfamart — probably.** **No** Indonesian crypto exchange accepts cards; Pintu refuses them in writing too. Card refusal is industry-standard here, not a weakness. And the Alfamart/Indomaret absence, though genuinely sourced-absent, is likely deliberate: **every Indodax user must hold an Indonesian bank account in their own name to withdraw**, so a cash-in rail for the unbanked would serve users who could never cash out. Cite it as an observation if useful, never as an obvious oversight.
>
> **4. Sizing caveat.** Rp201.2 trillion is **trading** volume, not fiat on-ramp volume. The deposit/withdrawal flow is the addressable surface and it is **not disclosed**. Do not conflate the two in a business case.
>
> **5. Phase 0 — deliberately adjudicated, not assumed.** Indodax is an OJK-licensed PAKD, which sits near the CLAUDE.md exclusion for "PSPs and payment infrastructure companies". **Call: in scope.** The exclusion names payment processors (Adyen, Stripe, Razorpay, Xendit, Midtrans…). A crypto exchange is a *merchant consuming* payment rails, not a provider of them — and it holds **no Bank Indonesia payments licence**. The repo's own TAL carries a 20-company "Crypto & Digital Assets" category with Indodax at **P1**, so the target list already treats this vertical as in-ICP. Territory is unambiguous: Jakarta HQ.

### Source Notes

**✅ Verified first-hand by me (strongest tier):**
- **Indodax's public Zendesk help-centre API is open.** I pulled the *Deposit Rupiah* (73) and *Withdraw Rupiah* (66) categories with full bodies as JSON; an agent then pulled the **entire 1,501-article corpus** in both `id` and `en-us` locales. Nearly every payment fact in this report is first-party and dated, most updated within the last two months
- **Xendit confirmed** — biller `"Xendit 87909"` in Indodax's own Mandiri VA instructions
- **Per-method fee table** (below) — each fee read from its own dated article
- **Withdrawal-timing table with per-bank blackout windows** — read from the source article, updated 2026-09-15
- **E-wallet withdrawal removal, 23 Jan 2024 13:00 WIB**, with the AML/CFT reason stated verbatim
- **Certificate Transparency**: 32 hostnames across `indodax.com`, **zero payment-shaped subdomains** — a clean negative
- `indodax.co.id` **301-redirects** to indodax.com — not a separate property, so no traffic double-count
- **OJK PAKD status** — an agent downloaded and parsed OJK's own register PDF rather than trusting a summary: `PT Indodax Nasional Indonesia (Indodax) — S-18/D.07/2025 (1 Februari 2025)`, present on the **2 March 2026** register

**❌ Killed before reaching the report — five false positives:**
1. **`doku`** → *"kliring **doku**men"* (document clearing). The exact trap from the Citilink run. Not the DOKU payment gateway
2. **`DANA` on the homepage** → *"Gunakan **dana** idle, prioritaskan **dana** darurat"*. `dana` is Indonesian for "funds". The DANA *wallet* is separately real (11 explicit wallet-context hits), but the raw count of 142 is heavily inflated by the ordinary noun
3. **`omise`** → `Promise` (JavaScript). **`brick`** → `firebrick` CSS colour. **`ovo`** → `toVolume` and `Kosovo`. **`bri`** → `Zabriskie` (the axios author) and `i18nBridge`
4. **Alfamart "matches"** → *"Dolar **tunai**"* and the BCA ATM menu *"Penarikan **Tunai**"*. No retail rail
5. **"Rp80.89 trillion in taxes"** — flagged by an agent as implausible (40% of the company's own annual volume) and excluded

**⚠️ Agent claims I tested against the corpus and REJECTED:**
- **"E-wallets are reached through QRIS, so one provider covers all"** — rejected. **Zero** wallet-titled articles mention QRIS in the body, and the fees differ (OVO 1.67%, GoPay 2%, QRIS 0.7%). Shared rails would share a rate. DANA also requires OTP account-linking, GoPay is app-only, ShopeePay redirects to its own app. **Four separate integrations**
- **"Withdrawal to e-wallets is live at Rp25,000"** — rejected. Three articles, all updated within two weeks, confirm bank-only. The third-party guides behind this claim predate 23 Jan 2024
- **"Alfamart/Indomaret retail is a live Xendit rail"** — rejected as *current*. Zero occurrences across 1,501 articles and absent from the canonical enumerated deposit list. It plausibly existed historically
- **"Permata and Sinarmas are VA deposit rails"** — rejected *as general IDR rails*: both appear in **zero** Deposit Rupiah articles, and Permata's only other appearance is inside a withdrawal maintenance-window table. **But see the reconciliation below — Permata is real in one specific place**

**🔎 The Permata reconciliation — both findings were right:**
Permata is **not** a general IDR deposit rail, **and** it is the **sole** payment method for Indodax's **Quick Buy USDT** product. That is why it never appears in the Deposit Rupiah category. Verbatim, updated 2026-08-18: *"The Indodax system for this instant purchase feature is **centrally configured**, meaning that Quick Buy USDT transactions are currently only available through Permata Bank's Virtual Account (VA). Therefore, **you cannot yet select other payment methods** (such as e-wallets or other banks' VAs)."* Quick Buy economics: min Rp50,000, max Rp10,000,000, payment fee Rp1,665, trading fee 0.2222%.

**⚠️ Unverified / unresolved:**
- **The QRIS, e-wallet and Permata acquirers are unknown.** Xendit → Mandiri VA is the *only* named provider in the entire corpus. QRIS carries the widest method set and its provider is a blank
- **Whether the Aug 2024 BRI/Mandiri/Permata VA reissue moved BRI onto Xendit.** Three banks migrating on one date is an aggregator-cutover signature, but Indodax never says. This is the pivot between "Xendit carries most VAs" and "Xendit carries only Mandiri"
- **Bank Indonesia PJP licence: NOT FOUND**, and indirect evidence says no. Their own QRIS FAQ calls them *"hanya berfungsi sebagai perantara yang menyediakan kode QRIS"* — merchant language, not acquirer language. **Implication: no licence of their own to protect, so provider choice is purely commercial**
- **The foreign-currency correspondent-bank VA route** is documented in one thin article and contradicted in spirit by the USD article. No SWIFT/BIC, no fee, no minimum, no worked example. **Do not present it as a working rail**
- **Trustpilot is flagged by Trustpilot itself** for a guidelines breach and its TrustScore is suppressed; nine 5★ reviews cluster on three dates. **Do not cite the rating in either direction** — cite individual dated 1★ reviews only
- A KITAS-vs-passport inconsistency exists between the T&C and one older article; the T&C position governs but is not perfectly self-consistent

### Success Case Alternatives
- **Livelo** — the decline-cascade case (+5% approval, 50% of failed transactions recovered, millions of R$ saved; *"instantly routing them to a secondary acquirer"*). Best fit **only if** discovery shows a second provider exists to fail over to. Brazil, loyalty/retail — a pattern match, say so
- **Rappi** — provider breadth and zero implementation delay. Fits the "every new rail is a separate build" argument, which is this account's real shape
- **inDrive** — multi-country scale. **Weak fit here** — Indodax is single-market by design. Use only if the conversation turns to method breadth, never to geography
- ⚠️ **No crypto or exchange case exists in the Yuno library**, and **no APAC crypto exchange orchestration case study exists anywhere** — an agent searched specifically. Any case used is explicitly a pattern match. Note Crypto.com appears on Yuno's public customer list, but **it has no published metrics** and must never carry a number

---

## Executive Summary

Indodax is Indonesia's largest retail crypto exchange — ~9.9M members, Rp201.2 trillion FY2025 volume, >40% market share, OJK-licensed. Its fiat stack is a **greenfield, multi-integration sprawl with no routing layer**: five VA banks, a sixth ring-fenced to one product, an in-house manual bank-transfer rail, QRIS, and four separately-integrated e-wallets — with per-rail fees that differ by up to **200×** on the same deposit, settlement that ranges from "Instant" to "1 business day", and nightly per-bank payout blackouts of up to 19 hours. Xendit is confirmed behind the Mandiri VA and behind Tokocrypto too, so the #1 and #2 exchanges (~85% of the market) share one aggregator and neither orchestrates. The motion is **greenfield**; the opening is domestic rail economics and the single-rail concentration on their flagship Quick Buy USDT funnel — **not** cross-border, which their own KYC design has closed.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** WebSearch fallback (resolution path 3) — no data supplied by Prateek, no `accounts/traffic/indodax.md`, no SimilarWeb MCP tool. **All `[ESTIMATE, not confirmed]`.** The SimilarWeb page was fetched (not summarised) for the August 2026 figures.

| Rank | Country | Traffic Share | Est. Monthly Visits | Trend | Source |
|---|---|---|---|---|---|
| 1 | **Indonesia** (high priority) | **82.3%** | Not public (paywalled) | — | [SimilarWeb](https://www.similarweb.com/website/indodax.com/) ✅ fetched |
| 2 | Singapore | 4.13% | Not public | — | same |
| 3 | United States | 1.93% | Not public | — | same |
| 4 | Vietnam | 0.68% | Not public | — | same |
| 5 | Australia | 0.6% | Not public | — | same |
| — | Others (undifferentiated) | 10.37% | — | — | same |

**Global rank trajectory (a real signal):** 34,715 → **38,679 (May 2026)** → **56,112 (Aug 2026)**. Ranked traffic has declined materially across 2026 even as trading volume grew 51.65% in 2025 — worth asking about, not asserting a cause.

**Total visits are not reported** because the public page paywalls them. Conflicting summary-only figures of ~1M and 1.1M exist for a *different* period (May 2026) and one is desktop-only; mixing them with the August all-device split would be fabrication, so no total is given.

**Cross-reference to Section 2 — and it inverts the usual finding.** Normally a top-5 market with no entity is a cross-border warning. Here the opposite is true: **the foreign traffic cannot transact at all.** See Section 2.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Millennium Centennial Center lt.2, Jl. Jend. Sudirman Kav. 25, Karet Kuningan, Setiabudi, South Jakarta, DKI Jakarta 12920. Founded 2014.

| Country | Entity Name | Registration # | Source |
|---|---|---|---|
| Indonesia | **PT Indodax Nasional Indonesia** | **Not found** (no NIB/AHU located) | T&C + [About Us](https://blog.indodax.com/en_US/newsroom-about-us/) |
| — | **No entity, office or subsidiary outside Indonesia** | — | About Us page lists a single location |

**Licensing (primary-source):**
- **OJK — Pedagang Aset Keuangan Digital (PAKD):** `S-18/D.07/2025`, dated **1 February 2025**; still on the **2 March 2026** register. Parsed directly from [OJK's own PDF](https://www.ojk.go.id/id/Fungsi-Utama/ITSK/Perizinan-ITSK-Aset-Keuangan-Digital-Aset-Kripto/Documents/Daftar%20Penyelenggara%20Perdagangan%20Aset%20Keuangan%20Digital%20Posisi%202%20Maret%202026.pdf)
- **Bappebti — PFAK:** `10/BAPPEBTI/PFAK/12/2024`, December 2024 `[UNVERIFIED — summary only]`
- **Supervision moved Bappebti → OJK on 10 January 2025**
- **CFX exchange membership** `SPAB-020/PFAK/CFX/10/2024` and **KKI clearing** `KKI/SPAK-020/X/2024`, both 11 Oct 2024
- **Bank Indonesia PJP / e-money licence: NOT FOUND**, with indirect evidence pointing to no

**Cross-Border Gap Analysis**

| Country | Top-10 traffic? | Local entity? | Domestic acquiring gated? | Cross-border risk? |
|---|---|---|---|---|
| Indonesia | ✅ #1 (82.3%) | ✅ | Yes — BI licensing gates acquiring; Indodax rides third-party PJPs | None — fully domestic |
| Singapore | ✅ #2 (4.13%) | ❌ | n/a | **No risk — foreign users cannot fund in fiat** |
| United States | ✅ #3 (1.93%) | ❌ | n/a | **No risk — US citizens barred from opening an account** |
| Vietnam / Australia | ✅ #4–5 | ❌ | n/a | **No risk — KITAS/KITAP wall** |

> **This is the opposite of the usual cross-border warning, and it is the most important structural fact on the account.** Indodax has deliberately closed its fiat perimeter. Verbatim from the binding T&C (updated 9 April 2026): *"Possess valid personal identification… such as a National Identity Card for Indonesian citizens, or **a passport and KITAS/KITAP for foreign nationals**."* Restated categorically: *"If you do not have a KITAS / KITAP then **you can't continue the verification process**."* A KITAS/KITAP is a **residence permit** — a tourist or offshore trader cannot obtain one.
>
> Further: *"**rupiah withdrawals can only be made to accounts registered in the member's own name**"*, and **14 nationalities are barred outright**, the **United States** among them.
>
> **Consequence:** the 17.7% foreign traffic is structurally non-convertible to fiat payment volume. It almost certainly transacts by **crypto deposit**, which never touches a payment rail. Any pitch built on that traffic is pitching against a deliberate regulatory posture.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Rail | Provider | Evidence Type | Source |
|---|---|---|---|
| **Mandiri VA** (biller 87909) | **Xendit** ✅ | `[Source Code]` — Indodax's own payment instructions name the biller | help centre, Mandiri VA guide |
| **BRI VA (BRIVA)** | **PT Bank Rakyat Indonesia — direct**, at least originally | `[Press Release]` — ANTARA, signing with named branch head, **17 Nov 2020** | [antaranews](https://www.antaranews.com/berita/1844572/pengisian-deposit-indodax-bisa-gunakan-fitur-virtual-account-bri) |
| **BCA VA** | **Not established** | Economics look bank-direct: fee **Rp3,885**, max **Rp50,000,000,000**, settlement **"1 hari kerja"** | [blog.indodax.com](https://blog.indodax.com/deposit-va-bca/) |
| **Bank INA VA** (prefix 78899) | **Not established** | Fee **Rp2,000**, settlement **"Instant"** | [blog.indodax.com](https://blog.indodax.com/deposit-va-bank-ina/) |
| **Bank Artha Graha VA** (prefix 2803…) | **Not established** | Fee Rp1,000 | help centre |
| **Permata VA** — *Quick Buy USDT only* | **Not established** | *"centrally configured… you cannot yet select other payment methods"* | help centre |
| **Direct BCA + unique code** | **In-house** | Manual/semi-manual reconciliation with a user-confirmed "pending deposit id" | help centre |
| **QRIS** | **NOT FOUND** | Carries the widest method set; provider unknown despite targeted searching | — |
| **DANA / OVO / GoPay / ShopeePay** | **NOT FOUND** | Four separate integrations (see below) | help centre |
| **Cards, PayPal** | **None — explicitly refused** | Own FAQ, updated 2026-08-31 | help centre |

**No reference to Midtrans, DOKU, NicePay, Faspay, Espay, Duitku, Winpay, iPaymu, Paylabs or OttoPay was found anywhere** in connection with Indodax. Only Xendit. That is a genuine negative from the full vendor bundle, not a gap in searching.

**Evidence the e-wallets are four separate integrations, not one QRIS wrapper:** zero wallet-titled articles mention QRIS in the body; the fees differ (OVO 1.67%, GoPay 2%, QRIS 0.7%) where a shared rail would share a rate; **DANA** requires OTP account-linking, **GoPay** is app-only and absent from web, **ShopeePay** redirects to its own app or website.

**Verdict: MULTI-PROVIDER, across at least three integration types** — an aggregator (Xendit), at least one direct bank relationship (BRI), and an in-house manual rail (Direct BCA) — with per-rail fees, caps, settlement times and AML rules that Indodax's own help centre exposes as inconsistent.

#### 3B. Payment Orchestrator

**None detected — direct PSP/bank integrations only (greenfield).**

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with PSP(s), which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

To be precise about which "none" this is: multiple parallel integrations with **no routing or failover layer between them — the user picks the rail, not a router.** Indodax obviously has internal deposit-handling code; there is no evidence of an orchestration layer and that is not being called in-house orchestration.

**Caveat, stated plainly:** this is an absence-of-evidence classification. Indodax publishes nothing technical. Certainty has to come from a conversation.

> **MANUAL — highest-value single action:** scan a live Indodax QRIS deposit code and read the merchant/acquirer string. That one step names the QRIS provider, which covers the widest set of methods and is currently a blank.

---

### Section 4: Alternative & Local Payment Methods

Indonesia is 82.3% of traffic; per the APAC reference the rails that matter are QRIS, virtual account, wallets (GoPay/OVO/DANA/ShopeePay), cards as a minority rail, and convenience-store cash.

| Country | Method | Category | Status | Source |
|---|---|---|---|---|
| Indonesia | **QRIS** | QR | **Active in checkout** — fee **0.7%** | help centre, updated 2026-09-15 |
| Indonesia | **Virtual Account — BCA** | A2A | **Active** — Rp3,885, settles **1 business day** | blog + help centre |
| Indonesia | **Virtual Account — BRI** | A2A | **Active** — **Rp1,665** | help centre, updated 2026-09-10 |
| Indonesia | **Virtual Account — Mandiri** | A2A | **Active** — via **Xendit 87909** | help centre |
| Indonesia | **Virtual Account — Bank INA** | A2A | **Active** — **Rp2,000**, **"Instant"** | help centre, updated 2026-08-18 |
| Indonesia | **Virtual Account — Artha Graha** | A2A | **Active** — **Rp1,000** | help centre, updated 2026-09-12 |
| Indonesia | **Virtual Account — Permata** | A2A | **Active, Quick Buy USDT ONLY** — Rp1,665 | help centre, updated 2026-08-18 |
| Indonesia | **Direct BCA bank transfer + unique code** | A2A | **Active** — unique code valid 1×24h | help centre |
| Indonesia | **DANA** | Wallet | **Active** — requires OTP account-linking | help centre, updated 2026-09-14 |
| Indonesia | **OVO** | Wallet | **Active** — fee **1.67%** | help centre, updated 2026-09-04 |
| Indonesia | **GoPay** | Wallet | **Active — APP ONLY**, fee **2%** | help centre, updated 2026-08-19 |
| Indonesia | **ShopeePay** | Wallet | **Active** — app or ShopeePay web | help centre, updated 2026-07-02 |
| Indonesia | **Alfamart / Indomaret retail cash** | Cash | **SOURCED ABSENT** — zero occurrences in 1,501 articles; absent from the canonical enumerated deposit list | help centre |
| Indonesia | **LinkAja** | Wallet | **SOURCED ABSENT for deposit** — appears only in the withdrawal-removal article | help centre |
| Indonesia | **Credit card / debit card / PayPal** | Cards/Wallet | **SOURCED ABSENT — explicit written refusal** | help centre, updated 2026-08-31 |
| Global | **USD deposit / USD withdrawal** | — | **SOURCED ABSENT — explicit "No" on both** | help centre, updated 2026-09-11 / 09-14 |
| Global | **Crypto deposit** | Crypto | **Active, permissionless, no KYC gate in the flow, no geographic restriction** | help centre, updated 2026-09-01 |

**The canonical enumerated list, verbatim** (updated 2026-09-15): *"Indodax offers various safe and convenient payment methods for Rupiah deposits. Choose from **Virtual Account (VA), Bank Transfer, and E-Wallet**."* Because this list is enumerated, absences from it are **sourced**, not merely unfound.

**Cards, explicit refusal, verbatim** (updated 2026-08-31): *"Currently, **you can not deposit to your Indodax account using credit cards, debit cards, or Paypal**… **We'll add more deposit methods in the future** to ease your Bitcoin buying process."*

> **Warning — and the caveats that go with it.** In Indonesia, **convenience-store cash (Alfamart/Indomaret) is a mainstream rail and the only rail for the unbanked**, and it is sourced-absent from Indodax. ⚠️ **Two reasons not to lead with this:** (a) **no** Indonesian crypto exchange offers it, and (b) every Indodax user must hold an Indonesian bank account in their own name to withdraw — so a cash-in rail would serve users who could never cash out. It is most likely a deliberate product decision. **LinkAja** is the cleaner comparative gap: **Pintu (first-party verified), Tokocrypto and Reku all accept it; Indodax accepts it nowhere.**

> **MANUAL:** verify the QRIS and e-wallet acquirers by walking a live deposit. Everything else in this table is first-party sourced.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source |
|---|---|---|---|---|
| Deposit handling poor, "funds are lost" | Trustpilot 1★ | 1 review | 11 May 2026 | [Trustpilot](https://www.trustpilot.com/review/indodax.com) |
| Deposit stuck past stated maintenance window | Trustpilot 1★ | 1 review | 13 May 2026 | same |
| Frequent maintenance during volatility | Trustpilot 1★ | 1 review | 27 Jan 2026 | same |
| Balance disappeared without explanation | Trustpilot 1★ | 1 review | 11 Apr 2024 | same |
| Irregular bank-account data change + withdrawal delay — **BCA filed a formal public reply** | mediakonsumen | 1 letter + official response | 16 Oct 2023 / 1 Nov 2023 | [mediakonsumen](https://mediakonsumen.com/2023/10/16/surat-pembaca/perubahan-data-rekening-yang-janggal-di-indodax) |
| Account hacked, responsibility disclaimed | mediakonsumen | 1 letter | 7 Sep 2025 | [mediakonsumen](https://mediakonsumen.com/2025/09/07/surat-pembaca/akun-diretas-indodax-tidak-bertanggung-jawab) |
| Complaint handling / refunds | mediakonsumen | 2 letters | 2022 | mediakonsumen |
| Site down when prices reverse; couldn't sell | mediakonsumen | 1 letter | 1 Feb 2021 | mediakonsumen |
| Rupiah withdrawal never reached bank account | detik Suara Pembaca | 1 letter | date not established | `[UNVERIFIED]` |

**Indodax's own dedicated per-rail failure FAQs** — self-published evidence that each rail generates enough support volume to warrant its own article: BCA Direct *"Pending deposit id is not valid"*; *"Mengapa Pembayaran Deposit Qris Saya Gagal?"*; *"withdrawal status is success but I have not received it"*; *"too many code requests"*.

> **Pattern, stated at the strength the evidence supports.** **No rail-specific cluster is claimed** — the dated volume per rail is too low. What the evidence *does* support: (1) **BCA is the only bank named more than once**, via the 2023 mediakonsumen case serious enough to draw a formal BCA reply plus Indodax's own dedicated BCA Direct failure article — and BCA Direct is precisely the **manual-reconciliation** rail; (2) **withdrawal complaints outnumber deposit complaints**, so payout is the weaker leg; (3) **zero complaints reference the 60-second e-wallet timeout**, so despite being documented it must **not** be asserted as a pain point.

⚠️ **Do not cite Indodax's Trustpilot rating.** The profile is flagged by Trustpilot for a guidelines breach, its TrustScore is suppressed, and nine 5★ reviews cluster on three dates. Cite individual dated 1★ reviews only.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | **20 Aug 2026** | Bank INA × Indodax expand digital banking access — deepens an **existing** VA rail | Partnership | [kontan](https://investasi.kontan.co.id/news/jalin-kerja-sama-bank-ina-dan-indodax-perluas-akses-perbankan-digital) |
| 2 | **16 Apr 2026** | Seven tokenised US stocks launched on Solana — framed as expanding **Indonesian** access to global assets, i.e. inbound not outbound | Product | antaranews (fetched) |
| 3 | **2–4 Jan 2026** | **OJK summoned Indodax management** over allegedly missing member funds (~Rp600m); OJK notes two conflicting accounts, unresolved. Indodax says its review found **external** compromise (phishing/malware), not internal systems | ⚠️ Regulatory | [kompas](https://money.kompas.com/read/2026/01/02/172205226/buntut-dugaan-dana-pengguna-hilang-ojk-panggil-manajemen-indodax) |
| 4 | **25–28 Aug 2025** | **BRI × Indodax co-branded debit card** — free real-time card transactions, free conversion across up to 12 currencies, cashback to Rp100,000 | Partnership (**issuing**) | [kontan](https://keuangan.kontan.co.id/news/bri-dan-indodax-luncurkan-kartu-debit-co-branding-bri-x-indodax) ✅ fetched |
| 5 | **13 Oct 2024** | Joined the Indonesian crypto bourse (CFX); clearing via KBI | Market structure | kontan `[UNVERIFIED]` |

**Public payment RFP:** *No public payment-related RFP or tender found.* As a private company Indodax has no procurement obligation, so this negative carries no signal.

**Payment hiring:** none found. **No payments job posting** surfaced on JobStreet, Glints, Dealls or LinkedIn.

**Funding:** one disclosed round, **23 Nov 2017**, East Ventures lead with Das Capital and Darmawan Capital; **amount undisclosed**. No 2025/2026 raise, acquisition or IPO. The CEO has said IPO talk is internal only.

---

### Section 7: Payment-Specific News

| # | Date | Item | Relevance | Source |
|---|---|---|---|---|
| 1 | **20 Aug 2026** | Bank INA partnership | Deepens an existing VA rail | kontan |
| 2 | **28 Aug 2025** | "Kartu Debit BRI X Indodax: Jembatan Bank ke Dunia Kripto" | Issuing, not acceptance | kontan |
| 3 | **25 Aug 2025** | BRI co-branded debit card launch | Issuing | kontan ✅ fetched |
| 4 | date not established | BNI + Bank INA debit card | Issuing | kontan `[UNVERIFIED]` |
| 5 | date not established | Blog: "Deposit Makin Mudah dengan E-Wallet & QRIS" | The e-wallet/QRIS deposit launch post | blog.indodax.com `[UNVERIFIED]` |

> **REMOVAL: Indodax discontinued IDR withdrawal via e-wallet on 23 January 2024 at 13:00 WIB**, covering **LinkAja, DANA, OVO, GoPay and ShopeePay**. Verbatim reason: *"mendukung kebijakan **Anti Pencucian Uang (AML)** dan **Counter Financing of Terrorism (CFT)**."* Source: help centre, updated 2026-09-07.
>
> **Handle this correctly.** The removal was **deliberate and compliance-driven**, not a capability loss. "Help you restore e-wallet payouts" is the wrong pitch and would be corrected in one line.

**Strategic read `[INFERENCE, not confirmed]`:** three bank co-branding deals in ~12 months (BRI, BNI, Bank INA) show Indodax building distribution through **issuing** partnerships while its **acceptance** stack stays unchanged. They will help put a card in a user's hand; they will not take a card for a deposit.

---

### Section 8: Checkout Experience Audit

The public site is reachable (HTTP 200) but the deposit flow is **behind login**, so the rendered checkout was not observed. What follows is from the public bundles, DNS/CT, and the first-party help centre.

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | **Wallet/deposit flow, authenticated** | — | Not a retail cart. "Open Deposit" (static VA, no amount) vs "Closed Deposit" (amount entered, payment code rotates) |
| Guest checkout | **No** — verification required before transacting | — | *"Account verification is required before you can make transactions"* |
| Payment methods visible | VA / Bank Transfer / E-Wallet / QRIS | Good breadth domestically | Enumerated first-party |
| Location-based method display | **GoPay is app-only**, absent from web | Poor | A method exists on one channel and not the other |
| Instalments | **N/A** | — | Not applicable to a crypto on-ramp |
| 3DS | **N/A** | — | No cards accepted |
| PCI indicator | **No card fields anywhere** | — | PCI scope genuinely minimal-to-nil |
| Multi-currency | **IDR only** — explicit "No" on USD deposit and withdrawal | — | first-party |
| Settlement speed | **Inconsistent**: Bank INA "Instant" vs BCA VA "1 business day"; VA generally "paling lambat 1 hari kerja Bank" | Poor | Their own docs |
| Timeout behaviour | **E-wallet deposits auto-cancel after 60 seconds** | Poor | Their own docs; **no complaints found referencing it** |
| Public JS bundles | `/v3-exchange/*` — **no PSP or rail strings**; all apparent hits were substring artifacts | — | verified first-hand |
| CT / DNS | 32 hostnames, **zero payment-shaped subdomains** | — | verified first-hand |

---

### Section 9: PCI DSS Compliance

*No direct PCI compliance documentation found publicly for Indodax — and this is the rare case where that is the correct answer rather than a gap.*

| Dimension | Finding | Source |
|---|---|---|
| PCI DSS Level | **Not found — and scope is genuinely minimal-to-nil** | Indodax accepts no cards, so it touches no cardholder data |
| Card data handling | **N/A — no cards accepted** | first-party FAQ |
| Recommended Yuno integration | **Cannot recommend** — Section 3 confirms no tokenized card checkout, so the conditional inference the template permits is unavailable | — |

**What they do hold:** ISO/IEC 27001 (first obtained Oct 2019), ISO 9001:2015, ISO/IEC 27017:2015 (cloud security) `[UNVERIFIED — summary only]`.

⚠️ **Security is a live and sensitive topic here** — the **Sept 2024 hack (~$22M, disputed range $18.2M–$25.47M)** was attributed by SlowMist to *a vulnerability in the withdrawal system*, and the platform went fully offline for four days. A further missing-funds episode drew an OJK summons in Jan 2026. **Do not lead with security.**

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: The flagship fiat-to-crypto funnel runs on one bank VA, and they say so themselves**
> **Evidence:** Section 3A/4 (Quick Buy USDT is **Permata VA only**, *"centrally configured… you cannot yet select other payment methods"*, updated 2026-08-18) + Section 3B (no orchestration layer, so adding a channel is a build, not a config).
> **Pain Point:** Their most conversion-sensitive product — instant fiat-to-stablecoin — depends on a single bank rail with no fallback. If Permata degrades, that funnel stops. They are publicly fielding the complaint in their own FAQ.
> **Yuno Value Proposition:** Routing and failover across the VA banks they already hold, so Quick Buy can offer any rail without a per-rail build.
> **Best Success Case:** **Livelo** — declines routed to a secondary acquirer. State plainly it is Brazil and a pattern match.
> **Outreach Angle:** Quote their own sentence back. Both halves are theirs, and it is the clearest orchestration gap on the account.
> **Suggested Subject Line:** *One bank behind Quick Buy USDT*

> **Insight #2: The deposit fee table inverts against them at trivial ticket sizes**
> **Evidence:** Section 4 published fees (QRIS 0.7%, OVO 1.67%, GoPay 2%) + flat VA fees (Artha Graha Rp1,000, BRI Rp1,665, Bank INA Rp2,000), each read from its own dated article.
> **Pain Point:** Above roughly **Rp50,000 (~US$3)**, GoPay already costs more than the cheapest VA. On a Rp10,000,000 deposit it is **Rp200,000 vs Rp1,000 — a 200× spread** for the same outcome. With no routing layer, the *user* picks, so the expensive path is chosen by default rather than by economics.
> **Yuno Value Proposition:** Route or steer by cost and ticket size instead of leaving it to the deposit screen.
> **Best Success Case:** **Rappi** — provider breadth without per-rail build cost.
> **Outreach Angle:** Their own published numbers, no estimate required. ⚠️ **State it as what they charge users** — whether it mirrors their own cost of acceptance is an inference, and a payments lead will make that distinction immediately.
> **Suggested Subject Line:** *Rp1,000 or Rp200,000, same deposit*

> **Insight #3: Their fiat exit sleeps while the market doesn't**
> **Evidence:** Section 4/8 withdrawal-timing table (updated 2026-09-15): BCA blackout 22:00–04:59, Mandiri 23:00–03:59, BRI 23:45–03:59, **Sinarmas above Rp100m unavailable 14:00–08:59 — a 19-hour daily gap**; withdrawals over Rp250m drop to **SKN/RTGS and bank working hours** + Section 5 (withdrawal complaints outnumber deposit complaints).
> **Pain Point:** Crypto settles in minutes, 24/7. Their payout has per-bank nightly blackouts and the **largest** withdrawals get the **slowest** rail. They even name the chain: *"Bank pengirim. Jaringan switching. Bank penerima."*
> **Yuno Value Proposition:** Payout routing across providers so the destination bank's maintenance window stops being the customer's problem.
> **Best Success Case:** **Livelo** — recovery by routing to an alternative path.
> **Outreach Angle:** Published by them, verifiable in one click, and it is the leg their own complaint pattern points at.
> **Suggested Subject Line:** *Payout windows against a 24/7 market*

> **Insight #4: Three integration types, no router — and the market leader's peer is on the same aggregator**
> **Evidence:** Section 3A (Xendit for Mandiri VA + a direct BRI bank deal + an in-house manual Direct BCA rail; settlement ranges Instant → 1 business day; BCA VA cap Rp50bn vs e-wallet caps far lower) + Section 11 (**Tokocrypto also runs Xendit**, fetched from Tokocrypto's own newsroom).
> **Pain Point:** Every rail was built separately and is exposed to the user as its own choice, with its own fee, cap, settlement time and AML rule. Adding or changing one is an engineering project.
> **Yuno Value Proposition:** One integration above what they already run — keep Xendit, keep the direct bank rails, add routing and a single reconciliation view.
> **Best Success Case:** **Rappi** — new providers with zero implementation delay.
> **Outreach Angle:** Additive framing only. ⚠️ **Never say "your competitors are orchestrating" — none are.** The accurate line is the inverse: nobody in Indonesian crypto orchestrates, and the rail lists have drifted apart anyway.
> **Suggested Subject Line:** *Three integrations, no router*

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks**
1. Your Quick Buy USDT flow is Permata VA only, and your own FAQ says it is centrally configured so users can't select another method yet.
2. A Rp10,000,000 deposit costs Rp1,000 through your Artha Graha VA and Rp200,000 through GoPay, and the person choosing is the customer.
3. Your withdrawal table shows Sinarmas above Rp100m unavailable from 14:00 to 08:59, and anything over Rp250m dropping to SKN/RTGS on bank hours.

**Cold call openers**
1. "You run five VA banks, QRIS and four wallets, all integrated separately. I wanted to ask how a new rail actually gets added today."
2. "Your Quick Buy USDT product is on a single bank VA. What happens to that funnel when Permata has a maintenance window?"
3. "Your deposit fees range from a flat Rp1,000 to 2% depending on which rail the customer picks. Is that spread something finance looks at?"

**Do NOT use:** cross-border or "unlock your foreign traffic" (their KYC design closes it deliberately); "you should accept cards" (no Indonesian exchange does); "your competitors are orchestrating" (none are); the 60-second e-wallet timeout as a pain point (documented but zero complaints reference it); the Trustpilot rating (profile flagged, score suppressed); restoring e-wallet payouts (removed deliberately for AML/CFT); anything security-led.

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ | Size | Overlap | Known PSP/Orchestrator | Source |
|---|---|---|---|---|---|---|
| **Tokocrypto** (Binance-owned) | tokocrypto.com | Indonesia | ~43% share (2023); US$12bn volume (2024) | Indonesia | **Xendit — CONFIRMED** (VA + e-wallet) | [Tokocrypto newsroom](https://news.tokocrypto.com/xendit-x-tokocrypto-kolaborasi-bangun-ekosistem-aset-kripto-di-indonesia/) ✅ fetched |
| **Pintu** | pintu.co.id | Indonesia | Beginner-focused leader | Indonesia | **None disclosed** | [Pintu FAQ](https://pintu.co.id/en/faq/metode-cara-deposit-rupiah-di-pintu) ✅ fetched — accepts **LinkAja** + NOBU; refuses cards and teller cash |
| **Reku** | reku.id | Indonesia | Licensed | Indonesia | None found | reku.id — QRIS **0.7%**, e-wallet **1.665%**, accepts **LinkAja**, Permata VA |
| **Ajaib Kripto** | ajaib.co.id | Indonesia | Part of Ajaib securities | Indonesia | None found | Instant deposit **from RDN brokerage balance** — a rail Indodax structurally cannot match |
| **Nanovest** | nanovest.io | Indonesia | — | Indonesia | None found (Xendit has a published Nanovest case study) | nanovest zendesk |
| **Mobee** | mobee.io | Indonesia | — | Indonesia | None found | App Store listing |
| **Bitocto** | bitocto.com | Indonesia | — | Indonesia | None found | Flat **Rp3,000** VA fee |
| **Upbit Indonesia** | id.upbit.com | Indonesia (Dunamu) | — | Indonesia | None found | **BRI VA only** — narrowest set found; IDR deposit was suspended then reopened |

#### 11B. Industry Peers

| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---|---|---|---|---|---|
| Coinhako | coinhako.com | Crypto exchange | Singapore | **Co-member with Indodax of the DAEA alliance** (Dec 2023) | newsbytes |
| Bitkub | bitkub.com | Crypto exchange | Thailand | Same DAEA alliance; THB on-ramp shape | same |
| Coins.ph | coins.ph | Crypto + payments | Philippines | DAEA convenor; **has in-person cash-in outlets** | support.coins.ph |
| Luno | luno.com | Crypto exchange | Malaysia, SG | Licensed local on-ramps | same |
| CoinDCX / CoinSwitch | — | Crypto exchange | India | INR on-ramp under tight regulation | TAL rows 86, 91 |

*All five are already in `accounts/apac-tal.csv` (rows 82, 86, 87, 89, 91, 94).*

#### 11C. Companies Recently Adopting Payment Orchestration

*No public case studies found of direct competitors adopting payment orchestration.* **Explicit negative.** Not one Indonesian crypto exchange was found using Yuno, Juspay, Spreedly, Primer, Gr4vy, Corefy or any orchestration layer. What competitors actually run is **single Indonesian aggregators** — and the only two named anywhere are Xendit (Indodax's Mandiri VA, and Tokocrypto).

> **The genuinely interesting structural finding: Indodax and Tokocrypto — the #1 and #2 exchanges, ~85% of the market between them — both sit on Xendit, and neither has a routing layer.** Indodax's Bank INA and Artha Graha VAs look like direct relationships bolted on beside it. That is the classic pre-orchestration pattern: one aggregator for the mainstream rails, hand-wired exceptions around it, nothing routing between them. It is a real hook **and it does not require claiming anyone is orchestrating.**

#### 11D. Prospect Scoring & Top Pipeline

Competitor scoring cannot be completed — seven of nine Indonesian competitors have **no identified PSP**, so every orchestration and multi-PSP signal would be ⬜ across the board. Recorded as a gap rather than filled with guesses.

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|---|---|---|---|---|---|---|---|
| 1 | **Tokocrypto** | Direct | Indonesia | Not scored | High | **Xendit confirmed**, Binance-owned, US$12bn 2024 volume | ✅ row 98 (P2) |
| 2 | **Pintu** | Direct | Indonesia | Not scored | High | Broadest verified rail set incl. LinkAja + NOBU | ✅ row 97 (P3) |
| 3 | **Reku** | Direct | Indonesia | Not scored | Medium | Publishes fees nearly identical to Indodax's | ❌ **not in TAL — genuine find** |
| 4 | **Ajaib Kripto** | Direct | Indonesia | Not scored | Medium | RDN instant-deposit rail | ❌ **not in TAL — genuine find** |
| 5 | **Upbit Indonesia** | Direct | Indonesia | Not scored | Medium | Single-bank VA; deposit suspended then reopened | ❌ **not in TAL — genuine find** |
| 6 | Nanovest / Mobee / Bitocto | Direct | Indonesia | Not scored | Low | Smaller, undisclosed stacks | ❌ not in TAL |

> **Three genuine TAL additions: Reku, Ajaib Kripto and Upbit Indonesia.** Also worth noting Tokocrypto sits at **P2** and Pintu at **P3** despite Tokocrypto being the only competitor with a *confirmed* PSP and roughly co-equal market share — **arguably both should be re-prioritised.**

⚠️ **Xendit, Midtrans, Doku, NicePay, Faspay and Duitku appear here only as vendors.** If any ever surfaces as a prospect it routes to **Partnerships**, per the ICP exclusion — not to outreach.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|---|---|---|
| **Trading volume (IDR market)** | **Rp201.2 trillion FY2025**, +51.65% YoY (FY2024: Rp132.6T) | [antaranews, 14 Jan 2026](https://www.antaranews.com/berita/5350481/indodax-catat-volume-transaksi-kripto-rp2012-triliun-selama-2025) ✅ fetched |
| Market share | **>40%** of Indonesian crypto transactions throughout 2025 | same; consistent with OJK's Rp482.23T national total |
| Members | **~9.9 million** | About Us ✅ fetched (page is internally inconsistent: also says 9.8M) |
| Monthly visitors | ~10 million claimed | About Us ✅ fetched |
| Assets listed | 500+ (page also says 490+) | About Us ✅ fetched |
| Asset mix | USDT ~22%, BTC ~13%, ETH ~7% | antaranews |
| **Fiat on-ramp volume** | **NOT DISCLOSED — this is the number that matters** | See caveat |
| Annual revenue / take rate | **Not found** | Private, no filings |
| Average transaction value | **Not found** | — |
| Est. annual transactions | **Cannot be calculated** | Requires ATV and fiat split, neither available |
| Primary currency | **IDR only** — USD deposit and withdrawal both explicitly refused | first-party |
| Billing channel split | **N/A** — not a subscription business; no app-store billing exposure | — |
| Funding | One round, **Nov 2017**, East Ventures lead, **amount undisclosed** | Tracxn / Crunchbase `[UNVERIFIED]` |

> **Sizing caveat, and it is the gate on the business case.** **Rp201.2 trillion is trading volume, not payment volume.** Most of it is crypto-to-crypto and IDR-pair trading that never touches a fiat rail. The addressable surface is the **fiat deposit and withdrawal flow**, which Indodax does not disclose. Unlike a marketplace, though, this business *cannot function* without fiat on-ramp, so the flow is certainly material — it simply is not quantified. **Establish it on the first call.**

---

### Overall Research Confidence

**High on payments, Medium on financials, Low on traffic** — an unusually favourable split, and the inverse of most accounts in this repo.

**High confidence** (first-party, fetched, dated):
- The complete domestic rail set, per-method fees, settlement times, timeout behaviour and withdrawal blackout windows — from **1,501 help-centre articles** pulled via the open Zendesk API, most updated within the last two months
- Xendit behind the Mandiri VA (their own biller instruction)
- Cards, PayPal, USD deposit, USD withdrawal, Alfamart/Indomaret and LinkAja as **sourced absences** against an enumerated list
- The e-wallet withdrawal removal with its AML/CFT reason and exact timestamp
- KITAS/KITAP KYC, own-name bank matching, and the 14 banned nationalities — from the binding T&C
- OJK PAKD licence, parsed from OJK's own register PDF
- Greenfield orchestration status (exhaustive negative + positive evidence of unrouted rails)

**Medium confidence:** trading volume and market share (single wire-service article, company-reported); the Sept 2024 incident (amount disputed across sources $18.2M–$25.47M); the Jan 2026 OJK missing-funds case (unresolved).

**Low confidence:** **traffic is entirely ESTIMATED** via WebSearch fallback — not supplied, not API-sourced. Total visits are paywalled, only 5 of 10 countries are public, and 10.37% sits in an undifferentiated "Others". The country profile drives two ICP signals, and one of them (3+ countries) is an artifact anyway.

**Unknown and material:** the QRIS, e-wallet and Permata acquirers; whether the Aug 2024 VA reissue moved BRI onto Xendit; fiat on-ramp volume.

---

### Manual Research Recommendations

> **Area:** The QRIS / e-wallet / Permata acquirers
> **Why it matters:** QRIS carries the widest method set and its provider is a complete blank. It determines whether this is "Xendit plus exceptions" or a genuinely fragmented multi-vendor stack — which changes the pitch.
> **Action:** Scan a live Indodax QRIS deposit code and read the merchant/acquirer string. One minute, and it is the single highest-value unknown.

> **Area:** Fiat on-ramp volume
> **Why it matters:** It is the entire business case. Rp201.2T is trading volume and must not be used as a proxy.
> **Action:** Ask directly on the first call.

> **Area:** Whether BRI still runs direct or moved onto Xendit in Aug 2024
> **Why it matters:** Pivots the stack between "one aggregator plus exceptions" and "genuinely multi-provider", which changes how the failover argument is framed.
> **Action:** Ask on the call; Indodax never published it.

> **Area:** The Jan 2026 OJK missing-funds case
> **Why it matters:** Unresolved as of the last reporting found. An adverse finding changes the tone of any outreach entirely.
> **Action:** Re-check Indonesian press before the first send.

> **Area:** Google Play / App Store reviews
> **Why it matters:** The richest complaint source in this market, and it went **completely unread** — the Play fetch returned truncated content.
> **Action:** Fetch the Play listing (`id.co.bitcoin`) or a review-aggregator mirror. There is also an academic sentiment dataset of Indodax Play reviews at oalib-perpustakaan.upi.edu.

> **Area:** TAL hygiene
> **Why it matters:** Three real competitors are missing, and priorities look inverted.
> **Action:** Add **Reku, Ajaib Kripto, Upbit Indonesia**. Reconsider Tokocrypto at P2 and Pintu at P3 given Tokocrypto's confirmed Xendit relationship and co-equal share.

---

### Appendix: All Source URLs

**First-party (fetched by me)**
- `https://help.indodax.com/api/v2/help_center/{id,en-us}/...` — categories, articles, full bodies (1,501 articles)
- https://indodax.com/ · https://blog.indodax.com/ · `/v3-exchange/*.js` bundles
- https://crt.sh/?q=%25.indodax.com
- https://blog.indodax.com/en_US/newsroom-about-us/ · https://blog.indodax.com/deposit-va-bca/ · https://blog.indodax.com/deposit-va-bank-ina/

**Regulatory** — https://www.ojk.go.id/id/Fungsi-Utama/ITSK/Perizinan-ITSK-Aset-Keuangan-Digital-Aset-Kripto/Documents/Daftar%20Penyelenggara%20Perdagangan%20Aset%20Keuangan%20Digital%20Posisi%202%20Maret%202026.pdf
**Traffic** — https://www.similarweb.com/website/indodax.com/
**Financial/corporate** — https://www.antaranews.com/berita/5350481/... · https://www.antaranews.com/berita/1844572/... · https://keuangan.kontan.co.id/news/bri-dan-indodax-luncurkan-kartu-debit-co-branding-bri-x-indodax · https://investasi.kontan.co.id/news/jalin-kerja-sama-bank-ina-dan-indodax-perluas-akses-perbankan-digital · https://money.kompas.com/read/2026/01/02/172205226/...
**Incident** — https://www.coindesk.com/markets/2024/09/11/indonesian-crypto-exchange-indodax-hacked-for-22m-pauses-activity-before-bigger-hit
**Complaints** — https://www.trustpilot.com/review/indodax.com · https://mediakonsumen.com/2023/10/16/surat-pembaca/perubahan-data-rekening-yang-janggal-di-indodax
**Competitors** — https://news.tokocrypto.com/xendit-x-tokocrypto-kolaborasi-bangun-ekosistem-aset-kripto-di-indonesia/ · https://pintu.co.id/en/faq/metode-cara-deposit-rupiah-di-pintu · https://reku.id/en/help/category/deposit-rupiah
**Yuno cases** — https://y.uno/en/success-stories/livelo · https://y.uno/en/success-stories/rappi

</details>
