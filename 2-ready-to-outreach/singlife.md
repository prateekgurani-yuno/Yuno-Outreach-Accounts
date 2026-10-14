# Singlife

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 13 / 29 → 🟢 **Medium**
**Industry:** Insurance — life, health, general + a consumer savings/wallet product · **HQ:** Singapore (5 Straits View, #01-18, The Heart, 018935) · **Researched:** 2026-10-14 · **First email sent:** —
**Motion:** **IN-HOUSE.** Not inferred — I read two separate home-grown routing layers out of their production bundles, one per market.

---

> ## 🎯 THE HOOK — they repriced their own rails twice in six months. Cards stayed free. The national QR rail doubled.
>
> Reconstructed from **their own fee page** across four points in time, via archived snapshots. Every figure verbatim.
>
> | Date | Bank / e-wallet (BPI, UnionBank, GCash, Maya) | QR Ph | Debit / credit card |
> |---|---|---|---|
> | **Aug 2025** | *"Enjoy free cash-in from: BPI, UnionBank"* — **free** | not offered | — |
> | **11 Feb 2026** | PHP 15, **first 5 free** | **PHP 15** | **free** |
> | **~Apr 2026** — Annual Report | *"credit cards, debit cards, and QR Ph with **no extra fees**"* | | |
> | **Aug 2026** — live now | PHP 15, **first 2 free** | **PHP 30** | **free** |
>
> In twelve months they went from free cash-in on every rail to charging on every rail **except cards** — cut the free
> allowance from five to two, and **doubled QR Ph from PHP 15 to PHP 30**. Their own annual report was still marketing
> QR Ph as fee-free four months before they doubled it.
>
> **They are absorbing full card MDR while charging for the national QR rail and for bank transfers.** That is backwards
> on cost-of-acceptance unless per-transaction rail economics are biting hard enough to force two repricings in six
> months. Sources: live page `https://singlife.com.ph/about/faqs/is-there-a-fee-for-cashin-and-cashout/` ·
> archived `web.archive.org/web/20260710164859` and `/20250803204217` · PH AR2025
> `https://6rt99wqv.media.zestyio.com/2025_Singlife_Annual_Report-_v8small_Publishing_04292026.rJLeIfkRWx.pdf`.

> ## 🔀 THE ASYMMETRY — the same product, same group, rails priced in opposite directions
>
> | | 🇸🇬 Singapore Singlife Account | 🇵🇭 Philippines Singlife Account |
> |---|---|---|
> | Card funding | **None. No card path exists.** | **Yes — and it is the only free rail** |
> | Funding rails | FAST / PayNow, **own-name bank account only** | Card, bank, e-wallet, QR Ph |
> | Third-party money | *"may lead to… return of funds to the source"* | wallet is own-name for withdrawal |
> | Wallet/card issuer | — | **EON (UnionBank)** prepaid account + Visa card |
>
> **Control-tested, not assumed:** `credit card` returns **0** on the SG account page and the SG funding FAQ, against
> **32** on the SG policy-servicing page — with `FAST`=6, `PayNow`=5, `Singlife Account`=34 on the same asset proving the
> grep works. A real absence, not a broken search.
>
> **Do not pitch "open cards in Singapore."** The SG closure is regulatory — MAS keeps cards out of own-name deposit-like
> flows, the same wall found at StashAway and Syfe. The pitch is the **PH cost structure** plus the **cross-border
> servicing gap**, never a card-enablement argument in SG.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Singlife is Singapore's fifth-largest life insurer, **100% owned by Sumitomo Life of Japan** since 2024, with
FY2025 gross premiums of **S$5.342bn**. It runs a licensed life insurer in Singapore and a wholly-owned licensed life
insurer in the Philippines — **two markets, not the 33 the traffic file implies.** The consumer proposition in both is a
"Singlife Account": an insurance savings product in SG, and an EON-powered prepaid wallet with a Visa debit card in PH.

**Why it scores 13 and not higher.** The intelligence here is strong but the matrix rewards breadth, and this is a deep
two-market story: only two operating countries (**0/3**), Singapore at **84.68%** of traffic so no outside-home signal
(**0/2**), local rails already well covered in both markets (**0/3**), an in-house layer rather than greenfield (**1/4**),
and no recent growth round (**0/2**). It clears the ≥10 threshold and proceeds — but on pitch quality, not breadth.

**Verified vendor stack.** 🇸🇬 **2C2P (by Antom)** on the **AMEX leg only**, behind an Aviva-inherited in-house redirect
layer · **eNETS** · **Visa/MC Click to Pay** · **UOB and DBS** instalments negotiated bank-by-bank · **MuleSoft** as
integration middleware · Salesforce Agentforce. 🇵🇭 **`pay.singlife.ph`** — Singlife's own AWS API Gateway service — with
**direct OAuth2 integrations** into BPI and UnionBank, plus GCash and Maya, and the wallet/card on **EON (UnionBank)**.

**Top outreach angles, in order:**
1. **The PH rail repricing** — two increases in six months, cards free, QR Ph doubled. Dated and self-sourced.
2. **Network tokenisation is not deployed** and their own gateway's case study says they *"want to explore"* it — while
   their SG dunning deactivates the payment method after **3 failed attempts**. The gap and the symptom, both sourced.
3. **Four separate GIRO mandate paths** in SG plus a Zurich-era book still serviced on its own forms since 2018.
4. **Method availability is hardcoded per product journey** — Motor carries nine methods, Personal Accident carries
   Visa/Mastercard only. Same company, same checkout codebase.

**Primary targets:** 🇸🇬 **Romil Sharma, Group Head of Technology and Operations** — a combined technology *and*
operations mandate is the one role owning both gateway integration and GIRO collections. 🇵🇭 **Allen Alexander P. Reyes,
CEO since 5 Oct 2026** — a career CFO, ex-CFO of Security Bank Corporation. Cost-of-acceptance framing will land with
Reyes in a way product framing would not have with his predecessor.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Singlife` to draft the 12-touch sequence, or call this from `/prepare_batch`.*

⚠️ **Read the two boxes at the top of this file before writing a word.** Two hard constraints:
- **Never pitch card enablement for the Singapore Singlife Account.** It is closed by MAS rules on own-name deposit-like
  flows, not by a build gap. Asserting otherwise is factually wrong and burns the thread on email one.
- **The motion is IN-HOUSE.** They have already decided they need a layer and built two. Anchor on opportunity cost and
  reach — never on "you need orchestration."

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

## Section 1: Website Traffic Analysis by Country

**SimilarWeb (supplied 2026-10-13).** Full record and caveats in `accounts/traffic/singlife.md`.

| Country | Share | Change MoM |
|---|---|---|
| 🇸🇬 Singapore | **84.68%** | not recorded |
| 🇵🇭 Philippines | **9.06%** | ▲ **244.96%** |
| 31 further countries | **not recorded** | — |

⚠️ **Partial record.** The full per-country table did not survive this session's context compaction and has **not** been
reconstructed or estimated. 33 countries in the dataset; the pull spans `singlife.com` **plus two further domains**,
which the supplied view did not name.

**Engagement:** avg. visit ~**00:00:26**, bounce **77.92%**. Servicing-and-leave behaviour, not shopping. **Consequence,
honoured throughout: visit volume is a poor proxy for transaction volume here and no transaction count in this file is
derived from traffic.**

**The 84.68% home share scores 0** on the outside-home ICP row, which requires the home market below 60%.

**The Philippines spike — most probable cause, dated.** The **"Singlife 100-in-1 Medical Plan Get-A-Quote Program"** ran
**2 September → 30 September 2026**: first-time visitors opening the Singlife Shop inside **AUB's HelloMoney** or
**HelloPag-IBIG** apps and completing a Get-A-Quote flow received 30 days of free ₱100,000 accident cover. A zero-price,
quote-gated giveaway through two mass-market bank apps is the mechanic that produces a one-month step-change, and it fits
the 26-second / 77.92%-bounce profile exactly. Source: `https://tribune.net.ph/2026/09/02/aub-singlife-offer-free-p100k-accident-coverage`
(2 Sept 2026). **The causal attribution is an inference** — no source states it. The enabling channel is genuinely new:
the AUB/HelloMoney tie-up launched **October 2025**, and HelloPag-IBIG was still *"coming soon"* in March 2026.

⚠️ **Open question that decides whether this is a blip or a run-rate:** was the campaign extended past 30 September or
repeated? Not established.

**Domains resolved** (all with nonsense-path controls): `singlife.com` → 200, locale-prefixed AEM · `singlife.com.ph` →
200, Zesty.io · `singlifefa.com` → 200, own 404, a genuine separate property · **`singlife.ph`** → a **separate
registrable domain** hosting the PH payment service · `quotebuy.singlife.com` → the SG general-insurance checkout SPA ·
`planandprotect.singlife.com.ph` → the PH app landing. No legacy Aviva Singapore or Singapore Life domain still resolves
— that estate is retired, not redirected.

## Section 2: Legal Entities & Local Presence

Authoritative source: **MAS Notice 124 Public Disclosure, FY ended 31 Dec 2025** —
`https://singlife.com/content/dam/public/sg/documents/merger/fy25-public-disclosure.pdf` (fetched and text-extracted).

| Entity | Jurisdiction | Role |
|---|---|---|
| **Singapore Life Ltd.** | Singapore — **UEN 196900499K** | MAS-licensed direct insurer, **life AND general**. The billing entity in every footer. |
| Singapore Life Holdings Pte. Ltd. | Singapore | Immediate holding company; 100% parent of Singlife Philippines |
| **Sumitomo Life Insurance** | Japan | **Ultimate holding company, 100%** |
| Singlife Financial Advisers Pte Ltd | Singapore | Advisory; own domain `singlifefa.com` |
| Professional Advisory Holdings Ltd | Singapore | Holds PIAS |
| Navigator Investment Services Ltd | Singapore | CMS licence — collective investment schemes + custody |
| Singlife Propel Pte Ltd | Singapore | Related company; function not established |
| **Singlife Philippines Inc.** | Philippines | **Philippine Insurance Commission-licensed life insurer** |

**⚠️ No payments, e-money or stored-value licence found for any Singlife entity.** The SG Singlife Account is deliberately
structured as insurance to stay inside the insurance licence: *"The Singlife Account is an insurance savings plan. It is
neither a bank savings account nor a fixed deposit."* In PH the wallet and Visa card sit on **EON, UnionBank's
BIN-sponsorship platform** — so UnionBank, not Singlife, is the e-money issuer and BIN holder.

**Entity-naming trap.** Singapore Life Ltd. (**196900499K**) is the **renamed former Aviva Ltd**, not the original
Singlife entity (Singapore Life Pte. Ltd., 201405619W), following a scheme of transfer effective ~1 Jan 2022. The 1969
UEN is why ACRA and OpenCorporates lookups on "Singlife" mislead.

**Ownership timeline:** Sumitomo Life's initial investment **2019**; bought Aviva's 25.9% and TPG's ~35% across 2023;
**completed to 100% in March 2024** at a **S$4.6bn** valuation (the S$4.6bn is sourced from Singlife's own newsroom; the
18 March date is trade-press only). **Still 100% at 31 Dec 2025** per the MAS disclosure.

**Philippines ownership:** now **100%** held by Singapore Life Holdings. **Aboitiz Equity Ventures exited March 2026** —
2.4m shares = **5.33%** at **₱53.00/share ≈ ₱127.2m**, board approval 25 Feb 2026, Deed of Assignment 10 Mar 2026, PSE
disclosure 11 Mar 2026 (`https://tribune.net.ph/2026/03/11/aboitiz-cashes-out-of-singlife`). ⚠️ **Two unresolved gaps:**
AEV's original 2019 stake was **15%** and it sold only 5.33% — the dilution path is unexplained; and **the Di-Firm exit
(originally 20%) is not publicly disclosed anywhere reachable.** Di-Firm is privately held with no PSE obligation.

**Markets with traffic but no entity:** every market except SG and PH. Specifically checked and **not found**: Hong Kong,
Vietnam, Indonesia, Malaysia, Japan, Taiwan, Thailand, Australia.

**Third-market verdict: UNKNOWN, trending ABANDONED.** The entire evidence base is 2022-vintage intent — then-CEO Pearlyn
Phau hunting assets in Indonesia and Vietnam. Nothing closed. Post-Sumitomo the framing changed to *knowledge exchange*,
because **Sumitomo already owns those markets directly**, which removes Singlife's rationale for entering them.
**Pitch SG + PH only.**

## Section 3: Payment Providers & Payment Stack

### Singapore — 2C2P on one leg, behind an Aviva-inherited in-house router

**Primary evidence: Singlife's own production bundle**, `https://quotebuy.singlife.com/qnb/gi/assets/index-CGJsbPhn.js`.
I verified every token personally. Control: `payment` = **578**; nonsense path returns HTTP 500 at 50 B with **0** for
every token below.

**The complete method map, verbatim:**
```
const PaymentMethodMasterData = { credit_card:"V", click_to_pay:"O", enets:"E",
  pay_now:"P", uob_ipp:"UV", dbs_ipp:"DV", offline_payment:"OP",
  amex:"A", full:"F", full_voucher:"FV" }
```

So beyond the life-side rails: **eNETS is live** · **Click to Pay (Visa/MC SRC) is live** · **AMEX is a separate method**
· and **DBS instalments exist alongside UOB**, which contradicts the life-side *"only available with UOB"* and matches
2C2P's account of bank-by-bank IPP deals.

**The routing layer — the architectural finding.** Hardcoded in a conditional branch:
```
PaymentMethodMasterData[ue] === PaymentMethodMasterData.amex && (_r = `${$t}?currency=...
  &gatewaySource=2C2P&IssuingBank=AMEX`)
openAvivaPay$4(_r)
```
with `openAvivaPay$1 = ue => { window.open(ue,"_self") }` — ten occurrences across five variants.

Three things follow, all verified:
1. **`gatewaySource` is a literal routing parameter**, and it is set to `2C2P` **only on the AMEX leg**. Everything else
   routes elsewhere through the same signed redirect. A merchant with one PSP does not need a field named `gatewaySource`.
2. **The payment URL is chosen server-side at runtime** — `generatePaymentResponseData.paymentUrl`, destructured
   alongside `signature`, `secureHash`, `securityLayer`, `sourceContext`. Not hardcoded client-side. That is a routing
   decision made by Singlife's backend.
3. **The function fronting every SG card payment in production in October 2026 is named `openAvivaPay`** — the
   Aviva-era payment service, four years after the merger.

**⭐ My own addition, which the research run missed: method availability is hardcoded per product journey.** The Personal
Accident flow carries, verbatim:
```
Ft = { payInFull:[ { methodLabel:"Visa/Mastercard", methodIcons:[VisaIcon,MasterCardIcon], name:"credit_card" } ] }
```
**One method.** Motor carries the full nine-method ladder. Same codebase, same company, same checkout — and the ladder is
written into each journey by hand rather than configured once. This is the maintenance-cost argument in their own source.

**Middleware: MuleSoft (Salesforce Anypoint)** — 97 occurrences, `mulesoftConfig`, `mulesoftProtocol = axios.create(...)`,
auth route `auth/authorizeSOL`. Never publicly announced; first-party evidence only, which makes it stronger than a press
release. MuleSoft is a Salesforce company, so the integration layer and the Agentforce layer are one vendor family.

**Vendor case study — 2C2P, published 2 July 2026** (`https://2c2p.com/case-studies/singlife/`). Singlife integrated
2C2P's Payment Gateway *"starting with AMEX"*; quoted is **Alvino Kor, Executive Director**. Three things it concedes:
IPP since 2016 *"required Singlife to maintain separate negotiations with individual banks such as DBS and UOB"*;
Singlife *"wants to explore network tokenisation"* — **so it is not deployed**; and digital wallets are interest, not
implementation. Treat as vendor marketing — the scope is characterised by 2C2P, not Singlife.

### Philippines — the "payment gateway" is first-party

**`pay.singlife.ph`**, declared in the PH production config as the payments service. My own probe: **HTTP 403,
`application/json`, 42 B, `{"message":"Missing Authentication Token"}`** — the **AWS API Gateway** signature response.
PH payments terminate on Singlife's own AWS endpoint, not a PSP-hosted domain.

**Cash-in rails are direct bank integrations, not an aggregator.** The enum is exactly the four PHP 15 rails —
`{BPI:"bpi", UNION_BANK:"unionbank", GCASH:"gcash", MAYA:"maya"}` — wired to **BPI's and UnionBank's own OAuth2 partner
APIs**. No open-banking middleman.

**The wallet and card issuer — answered, verbatim from their own T&C in the production bundle:**
> *"The Wallet is a prepaid account **powered by EON** that comes with a Visa Card upon request (herein referred to as
> Singlife Card)."*

Verified at `https://planandprotect.singlife.com.ph/_next/static/chunks/4791-2a2ab3d2e9a6f103.js` — 1 hit, `Wallet`=12
as passing control, **0** on the 404 control. **EON is UnionBank's digital-banking/BIN-sponsorship platform**, and
UnionBank is the first PH BIN sponsor in Visa's FinTech Fast Track programme. Corroborated by the PH AR: the Singlife
Visa Debit Card *"allows for free cash withdrawals at any UnionBank ATM nationwide"*, and the Aug 2025 fee page gave free
cash-in from UnionBank **and** free wallet→UnionBank transfer. Three free rails pointing at one bank.

**⚠️ The one remaining hard gap: the card acquirer behind `pay.singlife.ph`.** PH card acceptance is **native-app-only**
(`ph.com.singlife.app`, seller "Singlife Philippines Inc.") — the PH **web** app has no card-entry path at all, only
BPI/UnionBank/GCash/Maya. UnionBank/EON acquiring is the plausible hypothesis given EON powers the wallet, but **no
source states it and it is not asserted here.** Resolving it needs the Android APK.

**Tested and NOT present, with controls passing** (`unionbank`=112, `gcash`=112, `instapay`=49): PayMongo, Dragonpay,
Xendit, Magpie, Brankas, Netbank, GrabPay, Coins.ph, BancNet, Adyen, Stripe, CyberSource, Braintree, Worldpay,
Checkout.com, Nuvei, iPay88, AsiaPay, 2C2P, Antom. **Zero.**

**Also found:** **Onfido** is the PH KYC/IDV vendor (SDK CSS classes — a real finding, not payments). **Merimen**
(`singapore.merimen.com`) is referenced on SG general-insurance pages — a motor/GI **claims** platform, so payouts rather
than acceptance. Not investigated.

## Section 4: Alternative & Local Payment Methods

**Singapore — rails are well covered, which is why the local-rail-gap row scores 0.**
- **Premiums:** eGIRO and paper Interbank GIRO are primary and actively recommended — *"We recommend that you pay your
  premiums using interbank GIRO."* Participating banks: DBS/POSB, Citibank, OCBC, UOB, Standard Chartered, Maybank, Bank
  of China, HSBC, MariBank, CIMB, ICBC. Paper GIRO activation takes *"up to 6 weeks depending on your bank."*
- **Cards:** accepted, tokenized (*"we will only capture your credit card token"*), deducted 1 working day before due
  date — but gated: *"credit card payment is accepted for **selected plans only**"* and *"We accept payment by **Visa /
  Mastercard credit card only**"* — no Amex on the life side, though Amex **is** live in general insurance.
- **PayNow:** inbound premium QR from the MySinglife app; outbound payouts via PayNow-NRIC/FIN, CPF Ordinary Account,
  Direct Credit and Telegraphic Transfer.
- **Instalments:** travel insurance ≥S$300 — *"only available with UOB"*, six or 12 months 0%. **Single-issuer IPP on the
  life side; DBS exists in the GI codebase.** A textbook coverage gap.
- Also live: DBS/POSB and UOB bill payment, Interbank Funds Transfer, **AXS m-Station**, and cash or cheque at the
  Customer Service Hall for MINDEF/MHA.
- **The Singlife Account takes no cards at all** — FAST/PayNow, own-name only, name-match enforced.

**Philippines — also well covered.** Premiums auto-deduct from the in-app wallet; the wallet tops up via card (free),
BPI/UnionBank/GCash/Maya (PHP 15), or **QR Ph** (PHP 30). Policies sold through GCash deduct from the GCash wallet
directly. Activation requires a **₱250** initial cash-in; interest-earning balance capped at **₱1m**; free Singlife Visa
debit card issued self-service in-app, with live FAQs for blocking a card and for unauthorised transactions — i.e. a real
card programme with real dispute volume.

## Section 5: Payment Issues & Customer Complaints

**Dunning is aggressive and self-documented, in both rails:**
- GIRO: *"We will attempt to deduct up to 3 times. Each deduction attempt will be 10 days apart. If… the 3 attempts have
  failed, the GIRO payment method will be **deactivated**."*
- Cards: *"We will attempt to deduct up to 3 times… the credit card payment method will be **deactivated** for your
  policy."*
- MINDEF/MHA: deduction on the 10th, one retry on the 25th.

**This is the symptom that pairs with the sourced gap.** Three attempts then deactivation is precisely what network
tokens and an account updater exist to prevent — and 2C2P's own case study, dated July 2026, places network tokenisation
in the *"wants to explore"* column. The gap and its consequence are both sourced, from two independent documents.

**Cross-border servicing gap, acknowledged in their own words.** Overseas policyholders are told to pay *"via internet
banking, AXS mobile or Interbank Funds Transfer"* — and card updates on SL-series policies are **manual, by email**:
*"we will provide you with direct customer support. Please email us."* A policyholder abroad whose GIRO fails has no
self-service card path on most plans. A live PH FAQ — *"I'm an OFW, can I avail a policy?"* — shows the same audience on
the other side.

**Lapse backstop:** an Automatic Premium Loan draws on policy cash value past the grace period, which softens
involuntary churn from failed collections. Worth knowing — it means failed payments show up as loans, not as churn, so
the cost is hidden in the balance sheet rather than visible in retention numbers.

**Two genuine defects in the SG checkout, found in their own code.** Internal colour only — too inside-baseball for a
cold email:
- **Latent DBS instalment bug.** Forward map is `dbs_ipp:"DV"`, reverse map is `D:"dbs_ipp"`. `"DV"` ≠ `"D"`, so DBS IPP
  codes do not round-trip. `uob_ipp:"UV"` / `UV:"uob_ipp"` is correct, so DBS is the broken one. **`amex`, `full` and
  `full_voucher` are missing from the reverse map entirely** — verified in my own extraction.
- **Asset mismatch:** `PayNowIcon = "/qnb/gi/assets/Amex-DCsDfo8A.png"` — the PayNow brand icon points at the Amex image.

## Section 6: Corporate & Payment Strategy Developments

- **PH payment-acceptance expansion, 2025** — from the CEO's message in the PH AR2025, verbatim: *"We introduced new
  products, enhanced transfer capabilities, and **expanded payment options through our payment gateway**, allowing
  customers to make **credit and debit card payments via their Singlife Account** and use **QR Ph**."* The best-sourced
  buying trigger on the account: they say on the record they ran a card-acquiring and national-QR expansion programme.
- **Full AWS migration completed** — 39+ mission-critical applications, all data centres exited within 18 months,
  delivered with AWS Professional Services; triggered by the Aviva Singapore merger. ~S$5m annual saving claimed. A
  39-app replatform is where payment integrations get rebuilt.
- **Salesforce Agentforce + Data Cloud**, October 2025 — first Singapore insurer to adopt it; roadmap extends to
  underwriting, claims and distribution. Billing and payment status has to be exposed to that service layer.
- **Zurich Life Singapore book — reframed.** The transfer was announced **January 2018** (~S$6bn of cover; one source
  says S$4.5bn — conflict flagged, not resolved), not recently. ⚠️ **I could not verify completion** — every source
  predates it. But `/en/faq/zurich-plans` is live (200 at 18,541 B against a 138,558 B 404 control) and `zurich` appears
  **8 times** on the servicing page, so the book transferred and is **still serviced on separate Zurich-era GIRO
  mandates eight years on.** The age is what makes the argument, not freshness.
- **⛔ Correction to an earlier premise of mine:** `aviva` returns **0** on the servicing page. The Aviva book was
  rebranded, not separately serviced. **Do not claim a parallel Aviva collection stack.**
- **No core-system or policy-administration replacement found.** An AWS-partner case study exists for migrating an
  **eBao** core platform for *"a leading insurance group in Singapore"* — **the customer is not named and this is NOT
  attributed to Singlife.**
- **⚠️ Stale signal — do not use.** The *"Singlife Philippines Secures ₱600 Million Funding"* headline still on their PH
  homepage is from **2 April 2024**. It was **US$10.65m of intra-group capital from Singapore Life Holdings**, not
  external investment, landing about a month after the Sumitomo buyout closed.

**The four separate GIRO mandate paths in SG**, each with its own form, referenced from the policy-servicing page:
`exxonmobil-giro-application-form.pdf` (a corporate/affinity scheme) · `MHA-MINDEF-giro-application-form.pdf` ·
`interbank-giro-for-portable-medical-policy.pdf` · `Application-Form-for-Interbank-GIRO.pdf`.

## Section 7: Payment-Specific News

The fee-schedule trajectory in the hook box is the entire payment-news story, and it is better than anything in the
trade press because it comes from their own page with dates attached. Nothing else payment-specific surfaced for either
market.

## Section 8: Checkout Experience Audit

**Completed from production source rather than a live purchase.** Full method map, routing parameters, per-journey method
lists, middleware and the PH wallet issuer are all in Section 3, each verified against passing controls. What a live
checkout would still add: **3DS behaviour**, which is genuinely unknown in both markets — hidden behind the SG hosted
redirect page and inside the PH native app. All `3ds` hits in both bundles were base64 noise.

## Section 9: PCI DSS Compliance

**No Singlife PCI DSS level, AoC or compliance claim found anywhere. Reported as a sourced absence.** `pci` = 25 across
25 live singlife.com pages, **all** of them the Akamai mPulse `BOOMR_config.PageParams.pci` beacon flag; 36 in the SG
checkout bundle, all base64. The only "PCI 3DS" text near Singlife is **2C2P's own site footer** — their certification,
not Singlife's.

**Inferred scope posture — DERIVED, not sourced.** Both markets push cardholder data off the SPA: SG via a full-page
redirect to a backend-nominated hosted page, PH via the native app against AWS API Gateway. No genuine `cardNumber`,
`card_token` or `cvv` field exists in either bundle. Consistent with SAQ A / A-EP redirect-model scope reduction, the
normal insurer posture.

**Tokenization:** SG life-side card-on-file is confirmed from their own FAQ, but **the vault owner is named nowhere** —
not on their site, not in the 2C2P case study, not in the bundle. **Network tokenisation is not deployed** (2C2P, July
2026). The GI SPA never touches a card. **PH: no public information found.**

## Section 10: Strategic Insights & Outreach Angles

**Insight 1 — The repricing is the whole pitch.** Two increases in six months, cards free throughout, QR Ph doubled,
free allowance cut from five to two, and an annual report marketing fee-free QR Ph four months before it doubled. Lead
here. It is dated, self-sourced, and impossible to dispute.

**Insight 2 — The asymmetry inside their own group.** The same product name accepts no cards in Singapore and makes
cards the only free rail in the Philippines. Contrasting two of their own systems beats any external benchmark because
they cannot dispute either half. **But the SG closure is regulatory**, so frame it as *why PH had to solve it
differently*, never as an SG failing.

**Insight 3 — The sourced gap with the sourced symptom.** Network tokenisation unexplored (their gateway's own words),
against a dunning policy that deactivates the payment method after three failures (their own FAQ). Two documents, one
conclusion.

**Insight 4 — Fragmentation they can count themselves.** Four GIRO forms, a 2018 Zurich book on its own mandates, nine
methods in Motor against one in Personal Accident, instalments negotiated bank-by-bank, and two separate home-grown
payment layers — one Aviva-inherited, one on AWS — with no cross-market reuse.

**Motion handling — IN-HOUSE.** They have already decided they need a layer and built two. The argument is **opportunity
cost and reach**, never "you need orchestration." 2C2P's own case study documents the symptoms: bank-by-bank IPP
negotiation, no network tokens, wallets unbuilt, and *"periodic meetings to educate Singlife's tech team on payment
fundamentals."* That last line is theirs, not mine, and it says the in-house layer is carried by a team that is not a
payments team.

**Who to approach.** 🇸🇬 **Romil Sharma, Group Head of Technology and Operations** — verified from Singlife's own
newsroom. 🇵🇭 **Allen Alexander P. Reyes**, CEO since **5 October 2026**, ex-CFO of Security Bank Corporation, verified
from Singlife's own PH board page. A new CEO with a finance background in his first 90 days is the standard window for a
vendor and cost review. **There is no public PH technology executive**, so PH payment decisions most likely route up to
Sharma's group function with local execution — **inference, not sourced.**

⚠️ **Pearlyn Phau's status as Group CEO is unresolved** — she appears in 2022–2024 sources and on **no** live page I
fetched. Do not name her. `/en/about-us/leadership` and `/our-leaders` both 404; SG leadership is not on a public page.

## Section 11: Similar Companies & Prospecting Pipeline

**The segment finding now has three data points and holds, with a refinement.** StashAway, Syfe and now Singlife all show
the same wall: **regulated own-name deposit-like flows in SG/HK are closed to cards by MAS/SFC rules.** Singlife adds the
workaround — **the PH wallet-topup architecture puts card acceptance one layer above the premium**, which clears the
regulatory problem the SG product cannot. **Segment by flow and jurisdiction, not by company**: the deposit leg is
closed, the subscription/wallet-funding leg is open, and in PH it is already card-borne and free.

Worth prospecting on this pattern: SG/PH insurers and wallet-fronted insurance distributors where a licensed local
partner issues the e-money (the EON/UnionBank structure is reusable and has precedent with other PH fintechs).

## Section 12: Business Case Data

| Metric | Value | Tag |
|---|---|---|
| Gross premiums FY2025 | **S$5,342,153k = S$5.342bn** (+16.0% YoY) | **SOURCED** — MAS Notice 124 filing |
| Gross premiums FY2024 | S$4,606,105k | **SOURCED** |
| Total income FY2025 | S$5,968,569k | **SOURCED** |
| Gross claims settled FY2025 | S$2,966,924k | **SOURCED** |
| Net income FY2025 | **S$45,663k** — halved from S$94,743k | **SOURCED** |
| Insurance contract liabilities | S$14,900,770k | **SOURCED** |
| **Amount payable on demand** | **S$11,060,389,000** (2024: S$9,103,121,000), **+21.5%** | **SOURCED** — closest public proxy for the liquid withdraw-anytime book |
| RBC2 capital adequacy | **187%** (2024: 224%) | **SOURCED** |
| Total assets | **"over S$16 billion as of 31 December 2024"**; rated **"A" (Fitch)** and **"Baa1" (Moody's)** | **SOURCED** — Singlife's own PH site |
| Policies in force / customer count | **No public information found** — `"number of"` and `"in force"` both return **0** hits across the filing | — |

**Monthly transaction count — DERIVED, and the derivation is disclosed because it rests on an assumed divisor.**
S$5.342bn ÷ 12 = **S$445m/month** in gross premium (both inputs sourced). Transaction count = monthly premium ÷ average
collection:

| Average collection | Transactions/month |
|---|---|
| S$100 | ~4.45m |
| S$500 | ~890,000 |
| S$1,000 | ~445,000 |
| S$5,000 | ~89,000 |
| **S$11,125** | **40,000 — the gate** |

**The 40k gate fires only if the average premium collection exceeds ~S$11,125**, which is implausible for an insurer with
a **S$100-minimum** savings account and a MINDEF/MHA group book deducting monthly. So the account clears comfortably at
any plausible assumption — but **no sourced count exists**, and no figure here is derived from traffic. **Billing unit:
per premium collection**, mixed monthly/annual/single, split unknown.

## ICP Score Breakdown — 13 / 29

| Signal | Max | Score | Basis |
|---|---|---|---|
| Transaction volume | 5 | **5** | S$5.342bn gross premiums sourced; gate clears at any plausible average |
| Orchestration status | 4 | **1** | **In-house** — two home-grown layers, verified in production code |
| Operates in 3+ countries | 3 | **0** | **Two markets only** — SG + PH. Entity-verified. |
| Multiple PSPs in parallel | 3 | **3** | 2C2P, eNETS, Click to Pay, UOB, DBS (SG); BPI, UnionBank, GCash, Maya, EON (PH) |
| Local rail gap | 3 | **0** | Rails well covered in both markets; the issue is cost and consistency, not absence |
| Recent expansion | 2 | **2** | PH ▲244.96%, AUB/HelloPag-IBIG campaign Sept 2026, AEV exit Mar 2026, new SKUs |
| Payment issues | 2 | **2** | 3-retries-then-deactivate on both rails, no network tokens, 6-week paper GIRO, DBS map bug |
| Funding > $10M | 2 | **0** | ₱600m is **April 2024** and intra-group; the Sumitomo deal is M&A, not funding. Budget access via the parent is strong but the row is not met. |
| Traffic outside home market | 2 | **0** | Singapore **84.68%**, far above the 60% threshold |
| Competitor orchestration | 2 | **0** | Zero hits for any competing orchestrator, with passing controls |
| Payment job postings | 1 | **0** | None found — but `singlife.darwinbox.com` is not search-indexed, so this is a non-finding, not a negative |

**Overall Research Confidence: HIGH** for the payment stack, entities, financials and the fee trajectory — these rest on
primary sources I fetched and control-tested myself. **MEDIUM** for the PH traffic causation (inference), SG leadership
beyond Sharma, and the Di-Firm exit. **LOW / unresolved**: the PH card acquirer, 3DS in both markets, the SG
tokenization vault owner, and whether the September PH campaign continued.

### Unverified and explicitly left open
- The PH card acquirer behind `pay.singlife.ph` — needs the Android APK.
- 3DS status in both markets.
- The SG life-premium tokenization vault owner — unnamed in every source; only resolvable by asking them.
- Whether the Zurich transfer completed (all sources predate it) and whether it was S$6bn or S$4.5bn.
- The Di-Firm exit from Singlife Philippines, and AEV's 15% → 5.33% dilution path.
- Pearlyn Phau's current status.
- Open roles — `singlife.darwinbox.com` needs a direct crawl.
- Group total assets and the full subsidiary register: the FY2025 Singapore Life Holdings accounts (104 pp) are
  **scanned images with no text layer**, and `tesseract` is not available in this environment, so they cannot be read here.

### ⚠️ Security observations — deliberately not recorded
First-party production assets in both markets exposed secret-hygiene and environment-separation problems. **No values,
hosts, filenames or token names are recorded in this repository, and none of it belongs in outreach.** This repository
is on a public remote, so writing the specifics down would amount to publishing a pointer to a live third-party
vulnerability. Prateek has the detail verbally; the appropriate route is responsible disclosure to Singlife, not a sales
asset.

</details>
