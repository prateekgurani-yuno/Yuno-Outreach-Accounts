# Singtel

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 14 / 29 → 🟢 **Medium** (read the analyst note — two of the 14 points are soft)
**Industry:** Telecommunications — mobile, broadband, pay TV, enterprise ICT · **HQ:** Singapore · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **Greenfield** — no orchestrator found. The card processor behind the bill-pay and eShop flows is **not public**. It is the single biggest open question on this account.

---

> ## 🎯 THE HOOK — Singtel's own treasury already told the market that card MDR hurts
>
> In Singtel's Adam Smith Awards Asia 2021 entry (Highly Commended, Best New Technology Solution), it described rebuilding collections with **Citi** for the **physical store, post-paid billing credit management and eStore**. Verbatim:
>
> *"Even though the existing credit card solution can offer an immediate solution, the merchant discount rate for credit cards can be quite high which incur additional costs to Singtel should more consumers use it. They therefore adopted a significantly lower cost method, which is utilising Singapore's tokenised instant payment solution PayNow…"*
>
> Source (fetched): https://treasurytoday.com/asa-asia-winners-2021/best-new-technology-solution-highly-commended-singapore-telecommunications-ltd-singtel/
>
> **Why it matters:** this is a sourced, on-record statement that card acceptance cost is a treasury-level concern, and that Singtel acts on it by steering volume between rails. Five years on, card payment is still offered one-off and as monthly recurring auto-billing in My Account and the My Singtel app. That is the volume where acquirer choice and routing move the MDR line.
>
> ⚠️ **It is a 2021 document.** Use it as "you've said this before" context, not as a claim about today's stack. Do not assert who acquires their cards today. Nobody publicly knows.

> ## 🧭 THE STRUCTURAL CHANGE — the wallet Singtel owned now belongs to Western Union
>
> - **Dash** was Singtel's own wallet. **Western Union completed its acquisition** (reported 2 Apr 2026): https://fintechnews.sg/128438/e-wallets/western-union-dash/
> - Singtel's bill-pay page **still lists Dash** as a way to pay a bill (scan the QR on the bill email): https://www.singtel.com/personal/support/billing/bill-payment-methods. The prepaid top-up page now reads "Dash by Western Union": https://www.singtel.com/personal/products-services/mobile/prepaid-plans/top-up-manage-account
> - The prepaid base leans on non-card rails. **"Migrant and foreign domestic workers make up 60% of Singtel's prepaid customers, and more than half a million of them are hi!App monthly active users"**, and NETS Click was added for customers "without internet banking, debit or credit cards". This is a 2020 release: https://www.singtel.com/about-us/media-centre/news-releases/singtel-and-nets-introduce-in-ap-payment-mode-for-singtel-prepaid-hi!ap-users
>
> **Read:** a payment rail that used to be first-party is now a third party's product inside Singtel's own app and bills. `[INFERENCE, not confirmed]` — whether that changes the commercial terms of the channel is unknown and is a good discovery question. It is not an assertion for email.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Singapore Telecommunications Ltd (UEN 199201624D) is Singapore's incumbent telco. FY26 group revenue was **S$14.26bn**, across four units:
- **Singtel Singapore** — S$3.69bn
- **Optus** (Australia) — A$8.35bn
- **NCS** (IT services) — S$3.20bn
- **Digital InfraCo** (Nxera data centres) — S$0.49bn

It also holds large associate stakes in Airtel, Telkomsel, AIS and Globe. Singtel Singapore has **4.496M mobile customers** and 686k fixed broadband lines (31 Mar 2026). Consumer billing runs through a custom My Account / My Singtel app front end, with a deep set of Singapore-local rails.

**SimilarWeb total visits (last full month):** ~5.5 million (avg monthly, Jul–Sep 2026, singtel.com only) — **supplied 2026-10-19**. Desktop and mobile web only; **app traffic excluded**, and this is an app-heavy business.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | Singapore | 80.13% | Cards (one-off + recurring), GIRO, PayNow/SGQR, GXS account link, internet/ATM banking (7 banks), AXS, SAM, 7-Eleven (NETS/CashCard/cash), NETS Click (prepaid app), Dash QR, Singtel PayLater (devices) | Apple Pay, Google Pay, GrabPay, PayPal **not found** on any fetched page (not confirmed absent) | ✅ Singapore Telecommunications Ltd |
| 2 | Indonesia | 3.73% | N/A — Singtel does not sell consumer services in Indonesia | N/A | ⚠️ Associate only (Telkomsel 30.1%) |
| 3 | Malaysia | 2.54% | N/A | N/A | ❌ No controlled consumer entity verified |
| 4 | India | 1.71% | N/A | N/A | ⚠️ Associate only (Airtel 27.5% → 26.9%) |
| 5 | United States | 1.20% | N/A | N/A | ❌ None verified |

**Ranks 2–5 are not billing markets.** Singtel Singapore only bills Singapore services. The non-SG web traffic is most plausibly migrant workers (60% of the prepaid base, per Singtel 2020), roamers and visitors. `[INFERENCE, not confirmed]` No cross-border acquiring or regulatory-gate analysis applies.

### Legal entities
- Singapore Telecommunications Limited (Singapore) — UEN **199201624D**
- Optus (Australia) — consolidated business unit; ownership % not verified in this run
- NCS (Singapore + regional; 51% of Yondu, Philippines)
- New in H2 FY26: Singtel Brazil Ltda, Nxera DC Japan Pte Ltd (43.46% indirect), Nxera Japan Co., Ltd, PT Teknologi Data Infrastruktur (Indonesia, 30.36% indirect) — all infrastructure or IT, not consumer billing

### Known PSPs
- **Citi** — collections partner for PayNow/FAST across store, postpaid billing and eStore — [Third-Party Report] (SG, 2021)
- **NETS** — NETS Click in-app payment for prepaid hi!App — [Press Release] (SG, 2020)
- **Card processor / acquirer** — **Unknown.** No public source names one. The bill-pay page HTML carries no PSP signature, and neither does the shop.singtel.com homepage.

### Orchestration status
**None detected — direct integrations only.** Searches for Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, "payment orchestration" and "payment routing" returned nothing. Singtel runs a custom AEM-based front end, which suggests rail-by-rail integration. There is no evidence of a routing layer, and also no evidence against one.

### Buying signals
- 🔄 **Dash divested to Western Union** (completed ~2 Apr 2026). The owned wallet rail is now third-party — [fintechnews](https://fintechnews.sg/128438/e-wallets/western-union-dash/)
- 💰 **Cost discipline is strategy.** Singtel28 asset recycling reached S$6.8bn of a S$9bn target by Aug 2026, and Singtel Singapore revenue fell 3.1% in FY26 on mobile price competition — [FY26 MD&A](https://links.sgx.com/1.0.0/corporate-announcements/7DAX544PTU347WL1/889652_FY26-MDA.pdf), [Investor Day 2026](https://links.sgx.com/1.0.0/corporate-announcements/CMWV5JCH9XBU8DEJ/902529_Investor%20Day%202026%20-%20Singtel%20Group.pdf)
- 📉 **MDR on record as a treasury concern** — [Treasury Today 2021](https://treasurytoday.com/asa-asia-winners-2021/best-new-technology-solution-highly-commended-singapore-telecommunications-ltd-singtel/)
- 🛡️ **Billing-impersonation phishing roughly every month** since Jun 2025, including "unable to debit from your nominated card" (19 Jan 2026) — [Singtel scam advisories](https://www.singtel.com/secured.html)
- 📋 No payment RFP, payments hire or licence application found.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Singtel` to draft the 12-touch sequence, or call this from `/prepare_batch`.*

⚠️ **Constraints before writing:**
- **Never name a current card processor.** None is public.
- **Do not pitch local APMs.** Singapore rail coverage is already deep: PayNow, GIRO, NETS, AXS, SAM and 7-Eleven. A "you're missing PayNow" line is factually wrong.
- **Do not pitch cross-border or local-acquiring in ID/MY/IN.** Singtel does not bill there.
- **The angle is cost of card acceptance and recurring-card reliability on a domestic book**, plus the post-Dash wallet question. Optus is a **separate TAL row** — a group-level conversation is possible, but nothing here is verified about Optus's stack.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 14 / 29
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | +5 | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. [ASSUMPTION — not researched.]** Basis: 4,496k Singapore mobile customers plus 686k fixed broadband lines (sourced, [FY26 MD&A](https://links.sgx.com/1.0.0/corporate-announcements/7DAX544PTU347WL1/889652_FY26-MDA.pdf)). Postpaid lines bill monthly, and prepaid tops up. That implies millions of billing events a month. The **card-processed share is unknown**: GIRO, PayNow, AXS, banking and 7-Eleven are all non-card. Even a low single-digit card share of that base clears 100k, but that share is not sourced. Billing unit = one monthly postpaid bill payment or one prepaid top-up. |
| Orchestration status | +4 | ✅ None detected (greenfield). Classification rests on the absence of evidence; the card PSP itself is unknown. |
| 3+ countries | +3 | ✅ By rule: SG, ID, MY, IN and US are each >1% of web traffic. **Soft** — these are web visitors, not billing markets (see analyst note). |
| Multiple PSPs | 0 | ⬜ Citi (PayNow collections) and NETS (NETS Click) are sourced, but no card acquirer is identified. A bank collection partner plus a domestic debit scheme is not a multi-PSP card stack. |
| Local rail or licensing gap in a top-3 market | 0 | ❌ Singapore rails are well covered. Indonesia and Malaysia are not billing markets. |
| Recent expansion | +2 | ✅ By rule: new entities in H2 FY26 (Nxera Japan, an Indonesian data-centre JV, Singtel Brazil) — [706A](https://links.sgx.com/1.0.0/corporate-announcements/HVHTA24E2HQXCS41/889656_20260521-Ann%20LR706A.pdf). **Soft** — infrastructure and IT, not consumer billing. |
| Payment issues reported | 0 | ❌ No organic complaints found. Phishing advisories are not payment failures. |
| Funding >$10M | 0 | ❌ Listed company; no funding round. Asset recycling is not funding. |
| High traffic outside home | 0 | ❌ Singapore is 80.13%. |
| Competitor using orchestration | 0 | ⬜ No Singapore telco stack is public. "Vodafone and Jio" on Juspay is Juspay's own claim and was not fetched. The TAL's Juspay tags for Airtel and CelcomDigi have no web source. |
| Payment job postings | 0 | ❌ None found. |

**Tier:** 14 → 🟢 **Medium.** No public payment RFP found, so no RFP override.

**Analyst note — held at 🟢, not overridden, but read this.** Five of the 14 points are soft:
- The "3+ countries" (+3) and "recent expansion" (+2) signals both fire on facts with no bearing on consumer payments.
- Without them, the honest core is **9 → 🔴**: an assumed-but-certain large volume plus greenfield.

I am not overriding down, for three reasons:
- **Absolute volume is undeniably large.** 4.5M sourced mobile customers is not a false-positive volume case.
- **There is a sourced MDR pain statement in Singtel's own words.**
- **The unknown card processor is a discovery gap, not a negative.**

But this is a **single-market, rail-rich, enterprise-cycle** account. Yuno's addressable slice is the **card book** (one-off plus recurring) and wallet coverage, not APMs or cross-border. Treat it as a long-cycle enterprise account and consider pairing it with **Optus** (separate TAL row) for a group conversation.

### Source Notes
- ✅ UEN 199201624D; FY26 financials; customer counts; associate stakes — SGX filings (fetched)
- ✅ Dash sold to Western Union, completed ~2 Apr 2026 — fintechnews.sg (fetched)
- ✅ Bill-pay methods list — singtel.com bill-payment-methods (fetched)
- ✅ Citi/PayNow collections and the MDR quote — Treasury Today 2021 (fetched)
- ✅ NETS Click; migrant workers are 60% of prepaid; 500k+ hi!App MAU — Singtel release, 25 Jun 2020 (fetched)
- ✅ Singtel PayLater eligibility (SC/PR/EP only, 21+) — Singtel blog (fetched, undated)
- ✅ Monthly billing-impersonation phishing advisories — singtel.com/secured.html (fetched)
- ⚠️ HQ address (31 Exeter Road, Comcentre) — search summary only; verify on ACRA
- ⚠️ Recurring card billing stops on card reissue and requires re-enrolment — UOB Singtel card FAQ, search summary only
- ⚠️ Amex accepted for recurring Singtel bills — Amex promo page, search summary only
- ⚠️ Amdocs as BSS vendor (2015 selection) — not fetched; current status unknown
- ⚠️ M1 sale to Simba/Tuas lapsed May 2026 — search summaries only; confirm on SGX/ASX

### Success Case Alternatives
- **Yuno telecom ebook (LATAM telco, failed-renewal recovery)** — the only telco-specific Yuno material found: https://landings.y.uno/yuno-ebook-modernizing-telecom-payments-infrastructure-for-global-scale. The profile match is recurring-billing recovery. ⚠️ Confirm internally which customer it is and whether the figures can be quoted.
- No APAC telco orchestration case study was found from any vendor.

---

## Executive Summary

Singtel is Singapore's incumbent telco: FY26 group revenue S$14.26bn, and 4.5M Singapore mobile customers. Its Singapore consumer billing sits on a broad set of local rails (PayNow/SGQR, GIRO, NETS, AXS, SAM, 7-Eleven, bank bill pay) alongside one-off and recurring card payments. **No card processor and no orchestration layer is publicly identifiable.** The motion is greenfield, but the opportunity is narrow:
- **Cost of card acceptance and recurring-card reliability** on a domestic book. Singtel itself publicly framed card MDR as a cost to be engineered away (2021).
- **The wallet gap left by selling Dash** to Western Union (2026).

It is not a cross-border or APM-gap story.

---

## Section 1: Website Traffic Analysis by Country

**Data source:** SimilarWeb Sales Intelligence, **supplied by Prateek 2026-10-19** (`accounts/traffic/singtel.md`). Period Jul–Sep 2026. singtel.com only. 16.63M visits over 3 months (avg 5.545M/month); 90.84% mobile web.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | Singapore | 80.13% | ~4.44M `[DERIVED from supplied share, not a SimilarWeb figure]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | Indonesia | 3.73% | ~207k `[DERIVED]` | Not supplied | same |
| 3 | Malaysia | 2.54% | ~141k `[DERIVED]` | Not supplied | same |
| 4 | India | 1.71% | ~95k `[DERIVED]` | Not supplied | same |
| 5 | United States | 1.20% | ~67k `[DERIVED]` | Not supplied | same |
| 6 | Australia | 0.92% | ~51k `[DERIVED]` | Not supplied | same |
| 7 | Thailand | 0.88% | ~49k `[DERIVED]` | Not supplied | same |
| 8 | Bangladesh | 0.76% | ~42k `[DERIVED]` | Not supplied | same |
| 9 | Russia | 0.72% | ~40k `[DERIVED]` | Not supplied | same |
| 10 | Italy | 0.52% | ~29k `[DERIVED]` | Not supplied | same |

**Caveats carried from the traffic file (mandatory):**
1. **Sales Intelligence view.** Top 10 only, share only. Per-country visit counts are derived as share × 5.545M and are **not** SimilarWeb figures.
2. **Single domain.** Only singtel.com was supplied. shop.singtel.com may be counted as part of singtel.com. Optus and GOMO are not included.
3. **Mobile app traffic is excluded.** Singtel steers bill payment, top-up and plan management to the My Singtel app and the hi!App. The 2020 release alone cites 500k+ hi!App MAU among migrant prepaid customers.
4. **Do not size payment volume from this data.** It is used here as a market-mix signal only. Global rank and trend were not captured.

**High priority (>5%):** Singapore only. Non-SG traffic does not correspond to Singtel billing markets — see Section 2.

---

## Section 2: Legal Entities & Local Presence

**Headquarters:** Singapore. The address 31 Exeter Road, Comcentre, Singapore 239732 is `[UNVERIFIED — search summary only, page not fetched]`.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Singapore | Singapore Telecommunications Limited | 199201624D | [SGX 706A, 21 May 2026](https://links.sgx.com/1.0.0/corporate-announcements/HVHTA24E2HQXCS41/889656_20260521-Ann%20LR706A.pdf) |
| Australia | Optus (consolidated business unit; 10.72M mobile customers) | Not found | [FY26 MD&A](https://links.sgx.com/1.0.0/corporate-announcements/7DAX544PTU347WL1/889652_FY26-MDA.pdf) |
| Philippines | Yondu (51% via NCS) | Not found | FY26 MD&A |
| Brazil | Singtel Brazil Ltda (IT services, under SGO Holding) | Not found | SGX 706A |
| Japan | Nxera DC Japan Pte Ltd (43.46% indirect, JV with Hitachi); Nxera Japan Co., Ltd | Not found | SGX 706A |
| Indonesia | PT Teknologi Data Infrastruktur (30.36% indirect, DC JV with Telkom) | Not found | SGX 706A |

**Associates** (effective interest at 31 Mar 2026, per the FY26 MD&A):

| Associate | Market | Effective interest | Mobile customers |
|---|---|---|---|
| Airtel | India / Africa | 27.5% (26.9% at 30 Jun 2026, per Investor Day) | 556.8M |
| Telkomsel | Indonesia | 30.1% | 153.7M |
| AIS | Thailand | 24.8% (26.8% at 30 Jun 2026) | 46.9M |
| Globe | Philippines | 46.6% economic / 22.2% voting | 66.6M |

Other holdings:
- Gulf Development: 7.7%, held as an FVOCI investment after the Intouch merger on 1 Apr 2025.
- Also: NetLink NBN Trust 24.8%, GXS Bank, SingPost, Indara.

The Mar→Jun 2026 moves in the Airtel and AIS stakes are unexplained in the sources found.

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| Singapore | Yes (80.13%) | ✅ | N/A | No — domestic biller |
| Indonesia | Yes (3.73%) | ⚠️ Associate only (Telkomsel); DC JV | Not assessed | **No** — Singtel does not bill Indonesian consumers |
| Malaysia | Yes (2.54%) | ❌ None verified | Not assessed | **No** — not a billing market |
| India | Yes (1.71%) | ⚠️ Associate only (Airtel) | Not assessed | **No** — not a billing market |
| United States | Yes (1.20%) | ❌ None verified | Not assessed | **No** — not a billing market |
| Australia | Yes (0.92%) | ✅ Optus | N/A | Separate business on its own domain |

The usual "potential cross-border operation" warning **does not apply.** Singtel Singapore sells Singapore telecom services. Overseas web visitors are most likely workers paying for or topping up Singapore lines, or roamers. `[INFERENCE, not confirmed]` One gap is worth a question: **no Singtel page documents how a payer abroad, or a foreign-issued card, pays a Singtel bill.** Every documented channel is Singapore-local.

> **MANUAL:** Check https://www.singtel.com/terms-billing (not fetched) for the billing entity and any named payment processor.

---

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| SG | **Citi** — PayNow/FAST collections with API connectivity for physical store, postpaid billing credit management and eStore (2021) | [Third-Party Report] | https://treasurytoday.com/asa-asia-winners-2021/best-new-technology-solution-highly-commended-singapore-telecommunications-ltd-singtel/ |
| SG | **NETS** — NETS Click in-app payment for prepaid hi!App, using NETS ATM cards from DBS, OCBC and UOB (Jun 2020) | [Press Release] | https://www.singtel.com/about-us/media-centre/news-releases/singtel-and-nets-introduce-in-ap-payment-mode-for-singtel-prepaid-hi!ap-users |
| SG | **Card acquirer / gateway: Not found.** Card on file exists ("Verify card", monthly recurring); the HTML carries no PSP signature. Scripts are served from cdn.aws.singtel.com and AEM clientlibs. | [Checkout] (static HTML only) | https://www.singtel.com/personal/support/billing/bill-payment-methods |
| SG | shop.singtel.com — no PSP signature in homepage HTML (scripts from cdn1.singteldigital.com and GTM only); checkout not reached | [Checkout] (homepage only) | https://shop.singtel.com/ |
| SG (historical) | Wirecard — BIN sponsor for the Dash virtual Visa (2017). Issuing, not acceptance; defunct. | [Press Release] `[UNVERIFIED — not fetched]` | https://www.wirecard.com/uploads/tx_nenews/PM_2017_08_16_EN_Singtel.pdf |
| AU (Optus, context only) | Processor not named. "Visa Checkout" appears in page HTML. | [Checkout] | https://www.optus.com.au/support/answer/how_to_pay_your_bill_1315 |

No Adyen, Stripe, Cybersource, Worldpay, Braintree, 2C2P, MPGS, Fiserv or Global Payments link to Singtel or Optus was found in any of 18 searches.

### 3B. Payment Orchestrator

**Classification: None detected.**

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with PSP(s), which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

The custom front end and the breadth of rails suggest in-house integration of each rail. `[INFERENCE, not confirmed]` There is no evidence of a routing layer. The TAL's `Payment Gateway` and `Payment Orchestrator` columns for Singtel are both empty.

> **MANUAL:** Add a device to cart on shop.singtel.com, and start a one-off card bill payment in My Account. Watch the DevTools network tab for the card iframe host. This one step resolves the account's biggest unknown.

---

## Section 4: Alternative & Local Payment Methods

Singapore only. No other market is a Singtel billing market.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| SG | Credit/debit card, one-off (app / My Account; posts immediately) | Cards | Active in checkout | [bill-payment-methods](https://www.singtel.com/personal/support/billing/bill-payment-methods) |
| SG | Credit/debit card, monthly recurring auto-billing (starts next cycle) | Cards / recurring | Active in checkout | same |
| SG | Card networks by name (Visa/MC/Amex/UnionPay) | Cards | Not found on Singtel pages. Amex recurring is mentioned on an Amex promo page `[UNVERIFIED]`. | — |
| SG | GIRO / eGIRO (recurring) | Direct debit / mandate | Active (reflects 2 working days after due date) | bill-payment-methods; [payment-not-reflected](https://www.singtel.com/personal/support/billing/payment-not-reflected) |
| SG | PayNow / SGQR on the bill | Bank transfer / A2A | Active (posts immediately) | same |
| SG | GXS Savings Account linked in the My Singtel app | Bank transfer / A2A | Active | bill-payment-methods |
| SG | Internet/ATM banking (DBS, UOB, OCBC, SCB, Maybank, HSBC, Bank of India) | Bank transfer / A2A | Active | bill-payment-methods |
| SG | AXS / SAM kiosks | Cash/voucher | Active | bill-payment-methods; payment-not-reflected |
| SG | 7-Eleven (NETS, CashCard, cash) | Cash/voucher | Active | bill-payment-methods |
| SG | NETS Click / NETS bank card in hi!App (prepaid) | Bank card / debit | Active | [top-up page](https://www.singtel.com/personal/products-services/mobile/prepaid-plans/top-up-manage-account); NETS 2020 release |
| SG | Physical hi! top-up cards; marketplace and kiosk top-up | Cash/voucher | Mentioned in docs (undated FAQ PDF) | hi! SIM FAQ PDF (singtel.com content/dam) |
| SG | Prepaid top-up charged to a postpaid line; automated recurring top-ups | Carrier billing (internal) / recurring | Active | top-up page |
| SG | Dash QR — now **Dash by Western Union** | Digital wallet | Active, but now third-party-owned | bill-payment-methods; top-up page; [fintechnews](https://fintechnews.sg/128438/e-wallets/western-union-dash/) |
| SG | Singtel PayLater — 0% over 12/24/36 months, charged to the Singtel bill, devices bought online | BNPL/Instalments (in-house) | Mentioned in docs (blog, undated) | [Singtel PayLater blog](https://www.singtel.com/personal/singtel-blog/singtel-paylater) |
| SG | Bank card IPP for devices | BNPL/Instalments | Not confirmed | — |
| SG | Atome / ShopBack PayLater / Grab PayLater | BNPL | Not found (named only as comparisons in the Singtel blog) | Singtel PayLater blog |
| SG | Apple Pay / Google Pay / GrabPay / PayPal | Digital wallet | **Not found** on any fetched page or in searches | — |
| SG | Cheque | — | **Deprecated** 31 Jan 2024 | payment-not-reflected |
| SG | Google Play direct carrier billing (Singtel as billing provider) | Carrier billing | Mentioned in docs `[UNVERIFIED — not fetched]` | https://singtel.com/personal/products-services/more/direct-carrier-billing/google-play-store |

**Gaps:**
- **No dominant Singapore rail is missing.**
- **Apple Pay, Google Pay and GrabPay were not found**, which is not the same as confirmed absent. This needs a checkout walk-through before use.
- **Singtel PayLater excludes Work Permit and S Pass holders** (eligibility is SC/PR/EP, aged 21+). So the 60%-migrant prepaid base has no device-financing path. That is a product decision, not a payments gap.

> **MANUAL:** Walk the eShop checkout and the My Singtel app bill-pay on iOS and Android to confirm wallet presence.

---

## Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Organic payment complaints | Reddit / HardwareZone / app stores / Trustpilot | **None found** (Reddit fetch blocked with 403; searches returned only Singtel help pages) | — | — |
| Failed recurring payments: recurring card charge stops when the card is reissued, and the customer must re-enrol | UOB Singtel card FAQ (issuer side) | Isolated / FAQ-level | Undated | https://www.uob.com.sg/personal/cards/cashback/singtel-card.page `[UNVERIFIED — search summary only, page not fetched]` |
| Billing-impersonation phishing (12 Jun 2025 "unsuccessful in payment deduction"; 19 Jan 2026 "unable to debit from your nominated card"; 16 Feb, 21 Feb, 19 May, 28 May, 20 Jun, 7 Jul, 16 Oct 2026) | Singtel scam advisory page | High (roughly monthly) | Jun 2025 – Oct 2026 | https://www.singtel.com/secured.html |

*"No payment-related complaints found on Reddit, X, Trustpilot, or app store reviews"* — with the caveat that Reddit could not be fetched.

**Pattern:** scammers repeatedly copy *card-debit failure* messages. `[INFERENCE, not confirmed]` That suggests real failed-auto-debit notices are a familiar customer experience, familiar enough to be worth impersonating. This is a soft discovery angle on recurring-card failure rates, **not** evidence of a failure problem. Do not cite it as one.

---

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 27 Aug 2026 | Investor Day: Singtel28 asset recycling at S$6.8bn of a S$9bn target (75%); S$2bn buyback 44% deployed | Tech Blog / Conference Signal | [Investor Day 2026](https://links.sgx.com/1.0.0/corporate-announcements/CMWV5JCH9XBU8DEJ/902529_Investor%20Day%202026%20-%20Singtel%20Group.pdf) |
| 2 | 21 May 2026 | FY26 results: revenue S$14.26bn; underlying net profit S$2.77bn (+12%); Singtel Singapore revenue −3.1% | Financial | [FY26 slides](https://links.sgx.com/1.0.0/corporate-announcements/7DAX544PTU347WL1/889653_FY26%20slides.pdf) |
| 3 | H2 FY26 (to 31 Mar 2026) | New entities: Nxera Japan (JV with Hitachi), Indonesian DC JV with Telkom, Singtel Brazil Ltda | Market Expansion (infrastructure) | [SGX 706A](https://links.sgx.com/1.0.0/corporate-announcements/HVHTA24E2HQXCS41/889656_20260521-Ann%20LR706A.pdf) |
| 4 | ~2 Apr 2026 | Western Union completes the Dash acquisition | M&A (payments divestment) | https://fintechnews.sg/128438/e-wallets/western-union-dash/ |
| 5 | 4 Feb 2026 | KKR–Singtel deal for the remaining 82% of STT GDC (S$6.6bn; Singtel 25%). Investor Day says completion is on track for August 2026. | M&A | [Investor Day 2026](https://links.sgx.com/1.0.0/corporate-announcements/CMWV5JCH9XBU8DEJ/902529_Investor%20Day%202026%20-%20Singtel%20Group.pdf); deal terms from [SGX analysis](https://links.sgx.com/1.0.0/corporate-announcements/Y85UPC7OFANTRQ15/874054_20260204-analysis.pdf) `[UNVERIFIED — not fetched]` |

**Other:**
- *"No public payment-related RFP found."*
- No payment-infrastructure job postings found.
- A 2026 report says ex-Airtel executive Siddharth Sharma is joining Singtel in a senior role `[UNVERIFIED — search summary only]`: https://www.communicationstoday.co.in/singtel-taps-siddharth-sharma-for-senior-leadership-role/

---

## Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | ~2 Apr 2026 | Western Union completes the Dash purchase from Singtel — its first wallet in APAC | High: the owned wallet rail is gone | https://fintechnews.sg/128438/e-wallets/western-union-dash/ |
| 2 | Oct 2024 | Western Union agrees to acquire Dash (~1.4M users) | Context | https://www.fintechfutures.com/digital-payments/western-union-acquires-singtel-s-mobile-wallet-dash `[UNVERIFIED — not fetched]` |
| 3 | 31 Jan 2024 | Singtel stops accepting cheques | Rail rationalisation | https://www.singtel.com/personal/support/billing/payment-not-reflected |
| 4 | 2021 | Singtel and Citi PayNow collections — MDR cited as the reason to shift from cards | High: cost-of-acceptance mindset | https://treasurytoday.com/asa-asia-winners-2021/best-new-technology-solution-highly-commended-singapore-telecommunications-ltd-singtel/ |
| 5 | 25 Jun 2020 | NETS Click added to hi!App for migrant prepaid customers | Rail coverage for the unbanked | https://www.singtel.com/about-us/media-centre/news-releases/singtel-and-nets-introduce-in-ap-payment-mode-for-singtel-prepaid-hi!ap-users |

> **REMOVAL:** Singtel divested Dash (Western Union, completed ~2 Apr 2026). Dash remains listed as a bill-pay method, now as a third-party wallet. Source: https://fintechnews.sg/128438/e-wallets/western-union-dash/

---

## Section 8: Checkout Experience Audit

*"Full checkout flow not accessible. Findings limited to publicly observable elements."* Static HTML was fetched; cart and login flows were not reached.

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | Custom-built front end (AEM clientlibs, cdn.aws.singtel.com) | N/A | PSP iframe not observable |
| Guest checkout | Bill pay requires OnePass login (My Account / app) | Not assessed | eShop not reached |
| Steps to complete payment | Not observed | — | — |
| Card input experience | "Enter your card details. Then tap Verify card." | Not assessed | Iframe vs custom fields unknown |
| Payment methods visible | 10+ bill-pay channels documented | Good (breadth) | Section 4 |
| Location-based method display | N/A — single market | — | — |
| Instalment / EMI options | Singtel PayLater (in-house, bill-based); bank IPP not confirmed | Fair | PayLater excludes WP/S Pass holders |
| 3DS implementation | OTP on card add-on purchases `[UNVERIFIED — not fetched]` | Not detected | — |
| PCI indicator | Not determinable | — | — |
| Mobile responsiveness | 90.84% of web visits are mobile | Not assessed | App-first |
| Multi-currency / local pricing | SGD only (inferred from a single-market business) | — | `[INFERENCE, not confirmed]` |
| Saved payment methods | Yes — "Saved methods", recurring card | Good | — |
| Error message clarity | Not observed | — | — |

---

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found | — |
| Card data handling | Not found | — |
| Recommended Yuno integration | Back-to-back API, given a custom front end and an existing vault `[INFERENCE, not confirmed]` | — |

*"No direct PCI compliance documentation found publicly for Singtel."* (Optus Business SmartPay's 2011 PCI certification is a product Optus sells, not merchant acceptance.)

---

## Section 10: Strategic Insights & Outreach Angles

> **Insight #1: The card book is the addressable slice, and Singtel already prices it as a cost problem**
> **Evidence:**
> - S3A/S7: the Treasury Today 2021 MDR quote and the shift of collections to PayNow via Citi.
> - S4: card one-off and recurring auto-billing are still active in My Account and the app.
> - S6: Singtel Singapore revenue −3.1% in FY26, with active cost and capital discipline (Singtel28).
>
> **Pain Point:** a cost line Singtel has openly called "quite high". It cannot be removed for customers who want cards and recurring card billing.
> **Yuno Value Proposition:** multi-acquirer routing for the card book, so acquirer choice becomes a lever rather than a fixed contract. Network tokens and account updater cover recurring.
> **Best Success Case:** the Yuno telecom ebook (LATAM telco). Same vertical and recurring billing profile. Confirm quotability internally.
> **Outreach Angle:** "Your treasury team called card MDR 'quite high' and moved collections to PayNow. For the customers who still pay by card every month, the acquirer behind that card book is the remaining lever."
> **Suggested Subject Line:** "The card book after PayNow"

> **Insight #2: Recurring card billing breaks on card reissue**
> **Evidence:**
> - S4: monthly recurring card billing is active and starts from the next cycle.
> - S5: the UOB co-brand FAQ says recurring charges stop on card reissue and need re-enrolment `[UNVERIFIED]`.
> - S5: the phishing pattern copies "unable to debit your nominated card" (verified page).
>
> **Pain Point:** involuntary payment failure on a 4.5M-customer base. Each failure becomes a GIRO, kiosk or collections follow-up, or a late fee.
> **Yuno Value Proposition:** network tokens and account updater inside the routing layer, plus decline-code-aware retry.
> **Best Success Case:** the Yuno telecom ebook (failed-renewal recovery).
> **Outreach Angle:** ask, don't assert. "When a customer's card is reissued, does the Singtel auto-billing survive it, or does it fall back to a manual re-enrol?"
> **Suggested Subject Line:** "When the card on file gets reissued"
> ⚠️ Verify the UOB FAQ page before using the reissue detail.

> **Insight #3: The wallet slot left by Dash**
> **Evidence:**
> - S7: Dash divested to Western Union (Apr 2026).
> - S4: Dash is still listed for bill pay; Apple Pay, Google Pay and GrabPay were not found.
> - S1: 90.84% of web visits are mobile web, and the business is app-first.
>
> **Pain Point:** the only wallet in the bill-pay list is now a competitor-adjacent third party's product.
> **Yuno Value Proposition:** add Apple Pay, Google Pay and GrabPay through one integration rather than one project each.
> **Best Success Case:** match on wallet breadth; pick from the Yuno library at outreach time.
> **Outreach Angle:** "With Dash now part of Western Union, which wallets do you want sitting next to PayNow in the My Singtel app?"
> **Suggested Subject Line:** "My Singtel app, after Dash"
> ⚠️ Confirm wallet absence via a checkout walk-through first.

> **Insight #4: The migrant prepaid base is served by non-card rails, and that is already solved**
> **Evidence:**
> - S1: Bangladesh, India and Indonesia web traffic.
> - S3A: NETS Click release — 60% of prepaid are migrant and foreign domestic workers; 500k+ hi!App MAU.
> - S4: AXS, SAM, 7-Eleven and top-up cards.
>
> **Pain Point:** none clearly established. **Do not lead with this.** It is context for discovery, e.g. home-country wallets for family top-ups `[INFERENCE, not confirmed]`.

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks:**
1. "Singtel's treasury team once said card MDR was 'quite high' and moved collections to PayNow. The card book that's left is where acquirer choice still matters."
2. "With Dash now part of Western Union, the My Singtel app's wallet line-up is worth a fresh look."
3. "Monthly card auto-billing on a 4.5M-line base lives or dies on what happens when cards get reissued."

**Cold call openers:**
1. "You moved collections to PayNow to get away from card MDR. I'm curious what you did with the card volume that didn't move."
2. "Now that Dash sits with Western Union, are you rethinking which wallets show up at bill pay?"
3. "When a customer's card gets reissued, does your auto-billing carry over, or do they get bumped to GIRO or a reminder?"

---

## Section 11: Similar Companies & Prospecting Pipeline

### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| StarHub | starhub.com | SG | ~US$1.7B revenue (TAL, unverified) | SG | Not found | TAL row; payment page 404 |
| M1 | m1.com.sg | SG | Not found | SG | Not found | Sale to Simba/Tuas lapsed 21 May 2026 `[UNVERIFIED — search summaries]`: https://theonlinecitizen.com/2026/05/22/australia-s-tuas-terminates-s-1-43-billion-m1-acquisition-after-imda-halts-regulatory-review |
| Simba Telecom (Tuas) | simba.sg | SG | Not found | SG | Not found | https://www.singaporelawwatch.sg/Headlines/imda-suspends-review-of-proposed-telco-merger-between-simba-and-m1 `[UNVERIFIED]` |
| Circles.Life | circles.life | SG | ~US$100M (TAL, unverified) | SG (+AU/JP/TW per TAL) | Not found (homepage fetched) | — |
| MVNOs (MyRepublic, giga, GOMO, Zero1, redONE, Eight) | — | SG | — | SG | Not found | — |

### 11B. Industry Peers

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Optus (Singtel-owned) | optus.com.au | Telco | AU | 10.7M mobile customers; card surcharge regime `[UNVERIFIED]` | FY26 MD&A |
| Telstra | telstra.com.au | Telco | AU | Tyro is a referral partner for Telstra business customers, not Telstra's own acceptance | Tyro press release `[UNVERIFIED — not fetched]` |
| Bharti Airtel | airtel.in | Telco | IN | TAL says Juspay; no web source found | TAL row 1031 |
| CelcomDigi | celcomdigi.com | Telco | MY | TAL says Juspay; no web source found | TAL row 1042 |
| Vodafone Idea | myvi.in | Telco | IN | TAL says Juspay; third-party list only | TAL row 1088 |
| Telkomsel | telkomsel.com | Telco | ID | Midtrans mentioned on a forum post only | `[UNVERIFIED]` |
| Globe | globe.com.ph | Telco | PH | GCash parent ecosystem (Mynt) | FY26 MD&A |

### 11C. Companies Recently Adopting Payment Orchestration

*"No public case studies found of direct competitors adopting payment orchestration."* Juspay's own description lists "Vodafone and Jio" as customers `[UNVERIFIED — search summary only, page not fetched]`.

### 11D. Prospect Scoring

Peers cannot be scored on verified signals. No telco payment stack in the set is publicly sourced beyond unsourced TAL tags. All orchestration and PSP signals are ⬜. Scoring them would be manufacturing numbers.

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Optus | Peer (same group) | AU | Not scored | 🟢 candidate | 10.7M mobile customers; group pairing with Singtel | ✅ |
| 2 | StarHub | Direct competitor | SG | Not scored | — | Same market, same rails | ✅ |
| 3 | Circles.Life | Direct competitor | SG, AU, JP, TW | Not scored | — | Digital-first, multi-market | ✅ |
| 4 | Bharti Airtel | Peer | IN | Not scored | — | TAL Juspay tag (displacement) | ✅ |
| 5 | CelcomDigi | Peer | MY | Not scored | — | TAL Juspay tag (displacement) | ✅ |
| 6 | Telkomsel | Peer | ID | Not scored | — | Rail-heavy market | ✅ |
| 7 | M1 | Direct competitor | SG | Not scored | — | Ownership uncertainty after the failed sale | ❌ **not on TAL** |
| 8 | Simba Telecom | Direct competitor | SG | Not scored | — | Under IMDA scrutiny | ❌ not on TAL |
| 9 | Telstra | Peer | AU | Not scored | — | Largest ANZ telco | ✅ |
| 10 | Globe | Peer | PH | Not scored | — | Mynt/GCash ecosystem | ✅ |

**Genuine finds not on the TAL:** M1 and Simba. Both are small, and M1's ownership is in flux. They are low urgency.

---

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | Group S$14,261M (FY26); Singtel Singapore S$3,691M | [FY26 MD&A](https://links.sgx.com/1.0.0/corporate-announcements/7DAX544PTU347WL1/889652_FY26-MDA.pdf) (SGD; not converted) |
| GMV / Gross Transaction Volume | Not found | — |
| Average Transaction Value (USD) | Not found. Mobile ARPU S$23/month is a proxy, not an ATV. | FY26 MD&A |
| Est. Annual Transactions | Not calculable from sourced inputs | — |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. [ASSUMPTION — not researched.]** Basis: 4,496k SG mobile customers + 686k broadband lines (sourced) each generate roughly one bill or top-up a month, i.e. millions of billing events. The card-processed share is unsourced. Billing unit: monthly postpaid bill payment or prepaid top-up. | FY26 MD&A |
| Active Customers / Users | 4,496k SG mobile; 686k SG fixed broadband; Optus 10,722k mobile | FY26 MD&A |
| Primary Currency | SGD | — |
| Top 3 Markets by Revenue | Australia (Optus A$8.35bn), Singapore (S$3.69bn); NCS regional | FY26 MD&A |
| Billing channel split (web vs app store) | N/A — telco billing, not IAP. Web-vs-own-app split not found. | — |

**App-store trap:** does not apply. Singtel bills its own services directly.

---

### Overall Research Confidence

**Medium.**
- **Strong:** financials, entities, customer counts (SGX filings), the bill-pay method list (fetched), and the Dash divestment (fetched).
- **Weak:** the card PSP and acquirer (not public), checkout internals (behind login and cart), and complaints (Reddit blocked, nothing organic found).
- **Traffic was supplied** (SimilarWeb Sales Intelligence, 2026-10-19), but it is single-domain, excludes the app, and has no per-country visit counts.
- **Monthly transaction count is assumed, not sourced.**

---

### Manual Research Recommendations

> **Area:** Monthly transaction count — card share
> **Why it matters:** it is the only rejecting signal. The volume is certainly large, but the card-processed slice is what Yuno can touch.
> **Suggested manual action:** in discovery, ask what share of bill payments are card (one-off and recurring) versus GIRO and PayNow.

> **Area:** Card processor / acquirer (S3A)
> **Why it matters:** the pitch shape depends on whether this is a single-acquirer contract.
> **Suggested manual action:** start a one-off card bill payment in My Account, add a device to cart on shop.singtel.com, and capture the payment iframe host in DevTools.

> **Area:** Wallet presence (S4)
> **Why it matters:** Insight #3 depends on Apple Pay, Google Pay and GrabPay actually being absent.
> **Suggested manual action:** walk bill pay in the My Singtel app on iOS and Android.

> **Area:** Recurring card behaviour on reissue (S5)
> **Why it matters:** Insight #2.
> **Suggested manual action:** open the UOB Singtel card FAQ and Singtel's recurring-card help page and confirm the wording.

> **Area:** Stakeholders
> **Why it matters:** no payments owner was identified.
> **Suggested manual action:** search Sales Navigator for the Singtel Singapore head of billing and collections, group treasury (the 2021 Citi project owner), and the digital or eCommerce lead.

---

### Appendix: All Source URLs

**Traffic:** `accounts/traffic/singtel.md` (SimilarWeb, supplied 2026-10-19)

**Entities & financials:**
- https://links.sgx.com/1.0.0/corporate-announcements/7DAX544PTU347WL1/889653_FY26%20slides.pdf
- https://links.sgx.com/1.0.0/corporate-announcements/7DAX544PTU347WL1/889652_FY26-MDA.pdf
- https://links.sgx.com/1.0.0/corporate-announcements/CMWV5JCH9XBU8DEJ/902529_Investor%20Day%202026%20-%20Singtel%20Group.pdf
- https://links.sgx.com/1.0.0/corporate-announcements/HVHTA24E2HQXCS41/889656_20260521-Ann%20LR706A.pdf
- https://links.sgx.com/1.0.0/corporate-announcements/Y85UPC7OFANTRQ15/874054_20260204-analysis.pdf (not fetched)

**Payment stack & methods:**
- https://treasurytoday.com/asa-asia-winners-2021/best-new-technology-solution-highly-commended-singapore-telecommunications-ltd-singtel/
- https://www.singtel.com/about-us/media-centre/news-releases/singtel-and-nets-introduce-in-ap-payment-mode-for-singtel-prepaid-hi!ap-users
- https://www.singtel.com/personal/support/billing/bill-payment-methods
- https://www.singtel.com/personal/support/billing/payment-not-reflected
- https://www.singtel.com/personal/products-services/mobile/prepaid-plans/top-up-manage-account
- https://www.singtel.com/personal/singtel-blog/singtel-paylater
- https://shop.singtel.com/
- https://www.optus.com.au/support/answer/how_to_pay_your_bill_1315
- https://www.wirecard.com/uploads/tx_nenews/PM_2017_08_16_EN_Singtel.pdf (not fetched)
- https://singtel.com/personal/products-services/more/direct-carrier-billing/google-play-store (not fetched)

**Complaints & news:**
- https://www.singtel.com/secured.html
- https://www.uob.com.sg/personal/cards/cashback/singtel-card.page (not fetched)
- https://fintechnews.sg/128438/e-wallets/western-union-dash/
- https://www.fintechfutures.com/digital-payments/western-union-acquires-singtel-s-mobile-wallet-dash (not fetched)
- https://www.communicationstoday.co.in/singtel-taps-siddharth-sharma-for-senior-leadership-role/ (not fetched)

**Competitors:**
- https://theonlinecitizen.com/2026/05/22/australia-s-tuas-terminates-s-1-43-billion-m1-acquisition-after-imda-halts-regulatory-review (not fetched)
- https://www.singaporelawwatch.sg/Headlines/imda-suspends-review-of-proposed-telco-merger-between-simba-and-m1 (not fetched)
- https://landings.y.uno/yuno-ebook-modernizing-telecom-payments-infrastructure-for-global-scale

</details>
