# Ketto

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 14 / 29 → 🟢 Medium
**Industry:** Online donation crowdfunding (medical, NGO, personal causes) · **HQ:** Mumbai, India (Ketto Online Ventures Pvt Ltd, est. 2012) · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **In-house** — Ketto's backend picks the gateway per order across Razorpay, Juspay, Stripe (two accounts), PayU, PhonePe and CAMSPay, with client-side fallback and A/B routing. Not greenfield. The opening is the **international card leg**, not domestic orchestration.

**⚠️ READ BEFORE ANY OUTREACH**
1. **GoFundMe is a named Yuno customer** (y.uno homepage and success-stories page, both fetched 2026-10-19: *"Yuno powers payments for McDonald's, inDrive, Rappi, NetEase, GoFundMe, Uber…"*). It is the closest profile match Yuno has, but **there is no published GoFundMe case study**, so we can name the logo and nothing more. Check with marketing what can be said before using it beyond the logo.
2. **Domestic India is already well routed.** Five or more Indian gateways sit behind an in-house selector, and Razorpay's own Dynamic Routing runs on top. Pitching "you need orchestration" for INR flows will burn the thread.
3. **FCRA caps the international opportunity.** Fundraisers without FCRA approval *"cannot accept foreign donations"* (Ketto help centre). Foreign volume is structurally limited by regulation, not just by payments.

---

> # 🔒 PHASE 0 — QUALIFICATION GATE
>
> | Rule | Result |
> |---|---|
> | PSP / gateway / acquirer / orchestrator | **Does not fire.** Ketto is a donation marketplace. It collects funds and pays them out to campaigns/hospitals through third-party gateways. |
> | Existing Yuno customer | **Does not fire.** No Ketto mention on y.uno (fetched 2026-10-19). Peer GoFundMe is a customer — see above. |
> | No online payment volume | Does not fire. |
> | HQ west of Dubai, no APAC ops | Does not fire. Mumbai HQ. |
> | Monthly transactions < 40,000 (sourced) | **Does not fire.** ✅ SOURCED ~400,000/month (Razorpay case study, May 2025). See Section 12 for a conflict inside the same source. |

> # ⚠️ METHOD NOTES — disclosed up front
>
> 1. **Traffic was supplied:** `accounts/traffic/ketto.md` (Similarweb Sales Intelligence, pulled 2026-10-19, Jul–Sep 2026, ketto.org only). Its caveats apply throughout:
>    - **(a)** Top 10 countries only, as shares only. Per-country visits below are `[DERIVED from supplied share, not a SimilarWeb figure]` (share × 656,910 avg monthly visits).
>    - **(b)** Single domain. No other Ketto domain was found, so nothing was combined.
>    - **(c)** Mobile app traffic is excluded.
>    - **(d)** The file says the business is app-heavy and web traffic understates transactions, so web traffic was **not** used to size volume or test the 40k gate. Volume comes from the Razorpay case study instead.
>    - **Pushback on caveat (d):** the evidence points the other way. The donor app (`org.ketto.sip`) shows **100K+ installs** on Google Play ([Play Store](https://play.google.com/store/apps/details?id=org.ketto.sip&hl=en&gl=IN), fetched 2026-10-19), against ~590K **monthly** mobile-web visits. Ketto's code also detects PhonePe and Paytm in-app webviews. The flow looks mobile-web-first (WhatsApp/social share → browser), not app-first. **Still valid:** don't size volume from web traffic.
> 2. **Fetch worked** (WebFetch and curl). ketto.org is an Angular SPA, so pages return a JS shell. The PSP evidence comes from Ketto's own production JS (`main.a35ce00e342acaff.js` plus 209 lazy chunks), downloaded 2026-10-19 and grepped. I re-checked the key strings myself. The live checkout was **not** clicked through.
> 3. **Search summaries are not sources.** Several help-centre and aggregator findings are labelled `[UNVERIFIED — search summary only]`.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Ketto is India's largest-profile donation crowdfunding platform, founded in 2012 in Mumbai. Individuals raise money mainly for medical treatment; NGOs and personal causes make up the rest. It also runs a monthly-giving product ("SIP"). Ketto earns through fees and voluntary donor contributions on top of donations. It reported FY25 revenue of ~₹71–75 Cr (~US$8.5M) and a small profit (Inc42 aggregator). Payments run through an in-house gateway selector over five or more Indian PSPs, with Stripe handling foreign-currency cards.

**SimilarWeb total visits (last full quarter avg):** **656,910 / month** (Jul–Sep 2026; 1.970M over 3 months) — **supplied** 2026-10-19. 89.93% mobile web. App excluded.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇮🇳 India | 84.65% (~556K/mo) | Cards, UPI (intent, QR, UPI Number, CC-on-UPI, PPI-on-UPI), UPI Autopay, netbanking + eMandate, wallets, bank transfer, BHIM | **None material.** RuPay and EMI not found by name (EMI is irrelevant to donations). | ✅ Ketto Online Ventures Pvt Ltd |
| 2 | 🇸🇦 Saudi Arabia | 5.30% (~35K/mo) | International cards (Stripe), SAR shown as a donation currency in code | **mada, STC Pay, Apple Pay: absent from front-end code** | ❌ None (cross-border from India) |
| 3 | 🇺🇸 United States | 3.17% (~21K/mo) | International cards (Stripe; separate `key_us` Stripe account) | **Apple Pay, Google Pay, PayPal (dormant flags only), ACH: none live in code** | ✅ Ketto Online Ventures Inc (Delaware) |
| 4 | 🇨🇦 Canada | 1.90% (~12K/mo) | International cards (Stripe), CAD in code | Apple/Google Pay, PayPal, Interac — none in code | ❌ None |
| 5 | 🇬🇧 United Kingdom | 0.58% (~4K/mo) | International cards (Stripe) | Apple/Google Pay, PayPal — none in code | ❌ None |

No regulatory acquiring gate applies: India is the home market with a local entity, and the foreign markets are donor-side card corridors. The regulatory constraint is **FCRA** on the receiving side, not acquiring.

### Legal entities
- **Ketto Online Ventures Private Limited** (India) — CIN U74900MH2012PTC238738 `[UNVERIFIED — search summary only]`; registered office WeWork K. Raheja Platinum, Andheri East, Mumbai ([T&Cs](https://www.ketto.org/terms-of-use))
- **Ketto Online Ventures Inc** (USA, Delaware) — wholly owned subsidiary ([T&Cs](https://www.ketto.org/terms-of-use)). Its function is not stated. No 501(c)(3) found.
- **Ketto Foundation** (India) — issues some 80G receipts. Legal form not confirmed `[UNVERIFIED — search summary only]`

### Known PSPs
- **Razorpay** — [Source Code] + [Provider Case Study] (India: UPI suite, netbanking, eMandate, Dynamic Routing; partner since 2019)
- **Stripe** — [Source Code] (cards; two accounts, `key` and `key_us`; recurring cards; all non-INR currencies)
- **Juspay** — [Source Code] (India cards only: `api.juspay.in` card tokenize + `pay.js`)
- **PayU** — [Source Code] (UPI and UPI recurring; A/B-tested via a VWO flag)
- **PhonePe** — [Source Code] (UPI and UPI recurring)
- **CAMSPay** — [Source Code] (UPI, minor branch)
- **Cashfree** — [Provider Case Study, Apr 2022] (Auto Collect virtual accounts, instant settlements, bank account verification; not in current front-end code)

### Orchestration status
**In-house orchestration layer.** Ketto's backend returns a `payment_gateway` value with each order (`razorpay`, `juspay`, `stripe`, `stripe_india`, `stripe_recurring`, `payu`, `payu_recurring`, `phonepe`, `phonepe_recurring`, `camspay`, `razorpay_emandate`), and the client branches on it. The client also retries a failed recurring Stripe charge on the second Stripe account and A/B tests PayU for recurring UPI. Juspay appears only on the card leg. No HyperCheckout/HyperSDK evidence was found. No global orchestrator (Spreedly, Primer, Gr4vy, Yuno) appears in the code.

### Buying signals
- 🤝 Razorpay published a Ketto case study (May 2025) citing a **72% UPI success rate** and a **0.2% routing gain worth ₹1.7 Cr** ([Razorpay](https://razorpay.com/blog/ketto-journey-with-razorpays-upi-suite/)). Ketto measures and cares about success rate.
- 💳 International donations from 12 currencies all run through **one PSP (Stripe)** with custom card fields and **no wallets** ([Source Code](https://www.ketto.org/new/main.a35ce00e342acaff.js)).
- 🧪 Active gateway experimentation: a live A/B test of PayU for recurring UPI, plus Stripe failover logic ([Source Code]).
- 💰 / 🚀 / 📋 / 💼 No funding in the last 12 months, no expansion, no RFP and no payments hiring found.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Ketto` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 14 / 29
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | **+5** | ✅ SOURCED: ~400,000/month — *"managing around 400,000 transactions monthly"*, Razorpay case study, 6 May 2025, [razorpay.com](https://razorpay.com/blog/ketto-journey-with-razorpays-upi-suite/). Billing unit = donation payment (one-time + recurring SIP debits). **Caveats:** this is self-reported promo copy, and the same post's headline says "19K+ Donations a Year", which contradicts the body. It is unclear whether the 400K counts all gateways or only Razorpay. Even the lower reading (2.5 lakh monthly donors in the same post) clears 100K. |
| Orchestration status | **+1** | ✅ In-house layer: backend gateway selector over 5+ PSPs with fallback/A/B logic (Source Code). Juspay is present on the card leg. If Juspay is running its Express Checkout routing there, this could be read as +3 (regional orchestrator), but no evidence of that was found, so the stricter reading applies. |
| 3+ countries | **+3** | ✅ India 84.65%, Saudi Arabia 5.30%, US 3.17%, Canada 1.90% — four countries >1% (supplied Similarweb). |
| Multiple PSPs | **+3** | ✅ Razorpay, Stripe, Juspay, PayU, PhonePe in production JS, plus Razorpay and Cashfree case studies. |
| Local rail or licensing gap in a top-3 market | 0 | ⬜ India (#1) has full UPI coverage. Saudi (#2): mada/STC Pay/Apple Pay are absent from the code, but Saudi is not on the APAC rail list in the matrix and mada cards are commonly co-badged with international schemes (not verified for Ketto's donors). No acquiring gate applies. Not awarded. **This is the real hook, though** — see Insight #1. |
| Recent expansion | 0 | ❌ None found in the last 12 months. |
| Payment issues reported | 0 | ❌ Isolated only: Trustpilot fee/contribution complaints (Jun–Jul 2026), one £25-minimum complaint, a help-centre article on "SIP amount debited twice". Not moderate frequency. |
| Funding >$10M (last 12 months) | 0 | ❌ No round since 2020–22 (and those figures conflict). |
| High traffic outside home | 0 | ❌ India = 84.65%. |
| Competitor using orchestration | **+2** | ✅ **GoFundMe** (global crowdfunding peer, competes for diaspora medical fundraising in the US, UK and Canada) is a named Yuno customer (y.uno, fetched). **JustGiving** moved its card volume to Gr4vy (Aug 2025, fetched). Neither is a direct Indian competitor. No Indian crowdfunding platform was found on an orchestrator. |
| Payment job postings | 0 | ❌ None found. |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **🟢 Medium (14)**

**No override applied, but read this:** the matrix rewards volume and PSP count, both of which Ketto has. What it doesn't capture:
- The domestic INR flow — the bulk of the 400K/month — is low-ticket, UPI-heavy (55% of volume) and already routed in-house. There is little for Yuno to add there.
- The genuine opportunity is the **international card leg**: ~15% of web traffic, 12 currencies, single PSP, no wallets, possible USD-only settlement. Foreign volume is also capped by FCRA.

If discovery shows the international share of GMV is tiny, downgrade to 🔴. If it shows diaspora donations are a material, growing share of GMV, this is a clean, contained Yuno use case with a GoFundMe proof point.

### Source Notes
- ✅ ~400K txns/month, 2.5 lakh monthly donors, UPI 55% of volume, UPI SR 72%, Razorpay since 2019 — Razorpay case study, fetched and read by me
- ✅ Gateway set (Razorpay, Stripe ×2, Juspay, PayU, PhonePe, CAMSPay), 12 donation currencies, no Apple Pay/mada/ACH/PayPal SDK — Ketto production JS, grepped by me
- ✅ Two entities (India Pvt Ltd + Delaware Inc), "Indian payment gateway" vs "Foreign Payment Gateway" split — ketto.org T&Cs, fetched
- ✅ GoFundMe as a Yuno customer — y.uno, fetched
- ✅ Intl donors pay by cards only — Ketto help centre, fetched
- ⚠️ FY24/FY25 revenue and PAT — Inc42 aggregator. Conflicting figures; no RoC filing seen.
- ⚠️ USD-only processing for foreign donations, USD 25 card minimum — help centre via search summary only (URLs dated 2021). Code shows a USD 10 recurring minimum and 12 currencies, so this is likely stale.
- ⚠️ Funding totals ($850K vs $19.6M) — aggregators conflict

### Success Case Alternatives
- **GoFundMe** — same business model (donation crowdfunding, global donors, medical causes). Logo only, no published case study. Best match by profile.
- **inDrive** — Yuno case study ([y.uno/en/success-stories/indrive](https://www.y.uno/en/success-stories/indrive)) for a multi-market, multi-currency acceptance story. Weaker profile match.
- **Approval-rate testimonial** on y.uno ("elevated our payment approval rate by an impressive 10%"). The attribution is not captured here, so check it before citing.

---

### Executive Summary
Ketto is a Mumbai-based donation crowdfunding platform. Its production front end shows an in-house gateway selector across Razorpay, Juspay, PayU, PhonePe, CAMSPay and two Stripe accounts, handling ~400,000 donation transactions a month (Razorpay, May 2025). Domestic INR acceptance is mature: full UPI suite, UPI Autopay for monthly giving, success-rate tracking and dynamic routing. The gap is international. Donors in Saudi Arabia, the US, Canada and the UK (~13% of web traffic combined) are served cards-only through a single PSP (Stripe), with no Apple Pay, Google Pay, mada or PayPal live. Motion: **in-house**. The pitch is reach and approval rate on the diaspora card corridor, plus GoFundMe as the peer proof point, not orchestration itself.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** Supplied Similarweb (Sales Intelligence), `accounts/traffic/ketto.md`, pulled 2026-10-19, Jul–Sep 2026, ketto.org only, desktop + mobile web.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | India | 84.65% | ~556,074 `[DERIVED]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | Saudi Arabia | 5.30% | ~34,816 `[DERIVED]` | Not supplied | " |
| 3 | United States | 3.17% | ~20,824 `[DERIVED]` | Not supplied | " |
| 4 | Canada | 1.90% | ~12,481 `[DERIVED]` | Not supplied | " |
| 5 | United Kingdom | 0.58% | ~3,810 `[DERIVED]` | Not supplied | " |
| 6 | Australia | 0.48% | ~3,153 `[DERIVED]` | Not supplied | " |
| 7 | Germany | 0.42% | ~2,759 `[DERIVED]` | Not supplied | " |
| 8 | Singapore | 0.34% | ~2,233 `[DERIVED]` | Not supplied | " |
| 9 | UAE | 0.27% | ~1,774 `[DERIVED]` | Not supplied | " |
| 10 | Japan | 0.25% | ~1,642 `[DERIVED]` | Not supplied | " |

`[DERIVED from supplied share, not a SimilarWeb figure]` = share × 656,910. Top 10 = 97.36%; the remaining 2.64% is unlisted.

- **High priority (>5%):** India, Saudi Arabia.
- **Non-India traffic:** 15.35% of the total. This is a **diaspora outbound pattern** (APAC reference §3): NRI donors in the Gulf, North America and the UK funding Indian causes.
- **No local entity in the top 10:** Saudi Arabia, Canada, UK, Australia, Germany, Singapore, UAE, Japan. Only India and the US have entities.
- Saudi and UAE are EMEA territory as donor locations, but the merchant is APAC-HQ'd, so in scope.
- **Engagement metrics and global rank:** not captured in the supplied view.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Mumbai, India. Incorporated 12 Dec 2012 per registry aggregator `[UNVERIFIED — search summary only]`; *"Since 2012"* per [Razorpay](https://razorpay.com/blog/ketto-journey-with-razorpays-upi-suite/).

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| India | Ketto Online Ventures Private Limited | CIN U74900MH2012PTC238738 `[UNVERIFIED — search summary only; Zauba returned 403]`; GSTIN 27AAFCK0317C1Z3 `[UNVERIFIED]` | [ketto.org/terms-of-use](https://www.ketto.org/terms-of-use) · [zaubacorp](https://www.zaubacorp.com/company/U74900MH2012PTC238738) |
| USA | Ketto Online Ventures Inc (Delaware; wholly owned subsidiary) | Not found | [ketto.org/terms-of-use](https://www.ketto.org/terms-of-use) |
| India | Ketto Foundation (issues some 80G receipts) | Not found | [help centre](https://customerhappiness.ketto.org/portal/en/kb/articles/why-did-i-receive-an-80g-receipt-from-ketto-foundation-instead-of-the-ngo-i-donated-to) `[UNVERIFIED — search summary only]` |

**T&Cs on gateway routing (fetched):** INR payments by Indian nationals go through an "Indian payment gateway"; payments "in any currency other than INR" go through the "Foreign Payment Gateway". The T&Cs cite FCRA 2010 throughout.

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| India | #1 | ✅ | n/a (home) | No |
| Saudi Arabia | #2 | ❌ | Not researched (donor-side corridor) | **Yes** |
| United States | #3 | ✅ Delaware Inc (function unknown) | No | Possibly. Whether the `key_us` Stripe account is held by the Inc is unknown. |
| Canada | #4 | ❌ | Not researched | **Yes** |
| United Kingdom | #5 | ❌ | Not researched | **Yes** |

> *"Warning: Potential cross-border operation in Saudi Arabia, Canada and the United Kingdom. No local entity found. Transactions are likely processed cross-border, with higher scheme costs, lower approval rates and FX exposure."* The code supports this: all non-INR currencies go to Stripe tokenisation (`"INR"!==iso_currency → getStripeToken`).

**No regulatory acquiring gate applies** in the donor markets. The binding constraint is India's **FCRA**: fundraisers without FCRA approval cannot accept foreign donations ([help centre, fetched](https://customerhappiness.ketto.org/portal/en/kb/articles/why-were-foreign-donations-disabled-on-the-fundraisers)).

> **MANUAL:** Confirm which entity holds the Stripe US account and whether the Delaware Inc collects US donations.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| India | **Razorpay** — checkout.js, UPI links, `razorpay_emandate` | [Source Code] | https://www.ketto.org/new/main.a35ce00e342acaff.js |
| India | **Razorpay** — since 2019; full UPI suite, UPI Autopay, Dynamic Routing | [Provider Case Study] (6 May 2025) | https://razorpay.com/blog/ketto-journey-with-razorpays-upi-suite/ |
| Global (non-INR) + India cards | **Stripe** — js.stripe.com v2/v3, `api.stripe.com/v1/tokens`, keys `key` and `key_us`, gateways `stripe`/`stripe_india`/`stripe_recurring`, saved cards via `customer_id` | [Source Code] | main bundle + chunks (e.g. `2138.aaaa6c4ce6b701f1.js`, `8074.1795fbe9e48f7021.js`) |
| India cards | **Juspay** — `api.juspay.in/card/tokenize`, `pay.js`, used when `payment_gateway=juspay` and mode `CARD` | [Source Code] | main bundle |
| India UPI | **PayU** — `payu`, `payu_recurring`; VWO `payu_AB()` test on recurring UPI | [Source Code] | chunks |
| India UPI | **PhonePe** — `phonepe`, `phonepe_recurring`; PhonePe webview detection | [Source Code] | chunks |
| India UPI | **CAMSPay** — `camspay` branch on UPI (identity as the CAMS gateway is `[INFERENCE, not confirmed]`) | [Source Code] | main bundle |
| India | **Paytm** — QR generation, Paytm Mini App detection; gateway role unclear. Help centre: PG fee *"directly goes to the service providers eg. Paytm"* | [Source Code] + [Terms/Privacy Policy]-equivalent help doc | https://customerhappiness.ketto.org/portal/en/kb/articles/how-does-ketto-s-zero-platform-fee-model-work-7-8-2021 |
| India | **Cashfree** — Auto Collect, instant settlements, account verification (Apr 2022); absent from current front-end code | [Provider Case Study] | https://www.cashfree.com/case-study/ketto-saves-lives-by-facilitating-funds-collection-for-treatment-and-other-relief-campaigns-with-cashfree-payments |
| — | **PayPal** — logo + flags `isPaypalOtd`/`isPaypalSip` initialised false; no SDK, no paypal.com reference. **Not live.** | [Source Code], weak | chunks |

Not found anywhere in the 209 chunks: CCAvenue, BillDesk, Easebuzz, Adyen, Braintree, Checkout.com.

**Single-PSP dependency on the international leg:** every non-INR card goes through Stripe. There are two Stripe accounts, but both are Stripe.

#### 3B. Payment Orchestrator

**Classification: In-house orchestration layer.** [Source Code]
- Order endpoint `fundraisers/{id}/order` returns a `payment_gateway` value; the client dispatches in `submitToPaymentGateway` / `redirectToPaymentGateway`; responses come back via `payment/response/{gateway}`.
- Client-side failover: a failed `stripe_recurring` sets `stripeFailed` and resubmits on the other Stripe key.
- Juspay sits on the India card leg. There is no evidence that it orchestrates the whole stack.
- Razorpay Dynamic Routing runs inside Razorpay: +0.2% success rate, ₹1.7 Cr ([Razorpay](https://razorpay.com/blog/ketto-journey-with-razorpays-upi-suite/)).
- Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails and Yuno: no hits in code or search.
- **Not in `apac-tal.csv`**, so there is nothing to cross-check.

> **Implication:** argue reach and opportunity cost, never "you need orchestration". Ketto has already built the domestic version.

> **MANUAL:** Walk the checkout with DevTools from an Indian IP and from a non-Indian IP (VPN to US/KSA). Note which `payment_gateway` comes back and which methods render.

---

### Section 4: Alternative & Local Payment Methods

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| India | Credit / debit cards | Cards | Mentioned in docs + code | [help: modes of payment](https://customerhappiness.ketto.org/portal/en/kb/articles/different-modes-of-payments-to-donate-6-8-2021) |
| India | UPI (intent, QR, UPI Number, CC-on-UPI, PPI-on-UPI) | Bank transfer / A2A | Mentioned in docs + PSP case study + code | help (above); [Razorpay](https://razorpay.com/blog/ketto-journey-with-razorpays-upi-suite/) |
| India | UPI apps shown: GPay, PhonePe, Paytm, Amazon Pay, BHIM, WhatsApp, MobiKwik | Bank transfer / A2A | Code | main bundle |
| India | Netbanking | Bank transfer / A2A | Docs + case study | help; Razorpay |
| India | Bank transfer (virtual accounts via Cashfree Auto Collect, 2022) | Bank transfer | Docs + case study | help; Cashfree |
| India | Digital wallets (generic) | Digital wallet | Docs | help |
| India | **UPI Autopay** (recurring SIP; *"99% of recurring payments"*) | Direct debit / mandate | PSP case study + code (`*_recurring`) | Razorpay |
| India | Netbanking eMandate (SIP, *"most preferred mode"*) | Direct debit / mandate | Docs + code (`razorpay_emandate`) | [help: SIP options](https://customerhappiness.ketto.org/portal/en/kb/articles/what-are-the-payment-options-for-sip) |
| India | RuPay by name | Cards | Not found (schemes not listed) | — |
| India | EMI | BNPL/Instalments | Not found (not relevant to donations) | — |
| International | Credit / debit cards (Stripe), 12 currencies (INR, USD, GBP, EUR, AED, SAR, SGD, CAD, HKD, QAR, AUD, MYR) | Cards | Docs (cards only) + code (currency list) | help; main bundle |
| Saudi Arabia | mada, STC Pay | Cards / Digital wallet | **Not found** (absent from code) | main bundle + chunks |
| US / CA / UK / AU | Apple Pay, Google Pay (card wallets) | Digital wallet | **Not found** (absent from code) | main bundle + chunks |
| Global | PayPal | Digital wallet | **Not live** (dormant flags only) | chunks |
| US | ACH | Bank transfer | Not found | — |
| Canada | Interac | Bank transfer | Not found (code hits were false positives) | — |

> *"Warning: In Saudi Arabia (#2 market, 5.3%), mada is the domestic debit scheme and is not supported by Ketto."* — the claim about mada's prominence needs a citation before outreach. None was gathered in this run, so don't put a share figure in an email.

> *"Warning: In the US, Canada and the UK, Apple Pay / Google Pay are absent from a mobile-web-dominant (89.93%) donation flow that uses custom card fields."* — this is a code-verified absence. The conversion impact is `[INFERENCE, not confirmed]`.

**Help-centre conflict:** one help article (2021 URL) says non-INR donations are *"only processed in USD"* with a USD 25 card minimum `[UNVERIFIED — search summary only]`. The current code lists 12 currencies and per-currency amount thresholds (one function returns INR 300, USD/AED 60, EUR/GBP/SAR/SGD 30; its exact purpose is not confirmed). Treat the help article as stale until checked in the live checkout. A Sep 2025 Trustpilot review does complain of a £25 minimum.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Checkout add-on contribution ("additional percentage towards… platform-related costs") | Trustpilot | Isolated | Jun 2026 | https://www.trustpilot.com/review/ketto.org |
| Fee transparency / part of donation converted to "diagnostic voucher" | Trustpilot | Isolated | Jul 2026 | same |
| Minimum donation (£25) blocked a repeat GBP donor | Trustpilot | Isolated | Sep 2025 | same |
| One-time donation became an unconsented monthly auto-debit; unauthorised $805 charge | PissedConsumer | Isolated | Undated | https://www.pissedconsumer.com/ketto/RT-F.html `[UNVERIFIED — search summary only]` |
| Duplicate SIP debits (help article exists) | Ketto help centre | Known enough to need a FAQ | Undated | https://customerhappiness.ketto.org/portal/en/kb/articles/why-was-the-sip-amount-debited-twice (title only) |
| Payouts lag the raised amount while money is "in transit through the payment gateway"; INR 1–2 days, USD 5–7 days | Ketto help centre | Known | Undated | https://customerhappiness.ketto.org/portal/en/kb/articles/experiencing-issues-with-withdrawal `[UNVERIFIED — search summary only]` |

Trustpilot is 1.9/5 from 92 reviews. The dominant theme is aggressive post-donation calls and WhatsApp follow-up, not payment failure. No Reddit, X or Play Store payment-failure threads surfaced.

> *Pattern:* two complaints come from **GBP/USD donors** (the minimum amount, the $805 charge). This points to friction on the international card leg rather than domestic UPI. Thin evidence; use it as a discovery question, not a claim.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | Jan 2026 | CEO Varun Sheth on AI and automation for fundraiser success and fraud prevention (StartupTalky "Recap'25") | Tech Blog / Conference Signal | via https://www.cbinsights.com/company/ketto-online-ventures `[UNVERIFIED — search summary only]` |
| 2 | FY25 (filed 2025) | Revenue ₹71.2–74.7 Cr (down 13–15% YoY), PAT ₹3.3–3.4 Cr — profitable | Funding / financials | https://inc42.com/company/ketto/financials/ (aggregator; figures conflict on the same page) |
| 3 | 6 May 2025 | Razorpay case study: UPI suite, UPI Autopay, Dynamic Routing, ~400K txns/month | Tech Blog / Conference Signal | https://razorpay.com/blog/ketto-journey-with-razorpays-upi-suite/ |
| 4 | Apr 2022 | Cashfree case study: Auto Collect, instant settlements, bank verification | Payment infrastructure | https://www.cashfree.com/case-study/ketto-saves-lives-by-facilitating-funds-collection-for-treatment-and-other-relief-campaigns-with-cashfree-payments |
| 5 | Jul 2020 / Oct 2022 | Series A reported: $14.56M "Series A-II" per CB Insights; INR 237M per Preqin. Conflicts with Inc42's "$850K total". | Funding | https://www.cbinsights.com/company/ketto-online-ventures/financials · https://preqin.com/data/profile/asset/ketto-online-ventures-private-limited/126524 `[both UNVERIFIED — search summary only]` |

**No public payment-related RFP found.** No payments job postings found.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 6 May 2025 | "From Click to Cause: Ketto's Journey with Razorpay's UPI Suite Powers 19K+ Donations a Year" | Confirms Razorpay as the anchor PSP, success-rate metrics, UPI Autopay | https://razorpay.com/blog/ketto-journey-with-razorpays-upi-suite/ |
| 2 | 14 Apr 2022 | Cashfree case study (collections, instant settlement) | Second Indian provider on the collections/payout side | Cashfree URL above |

No 2025–2026 gateway announcements in Entrackr, Inc42, ET or Moneycontrol. **No provider removals found.** PayPal flags exist in the code but are off, which may mean a planned or retired integration (`[INFERENCE, not confirmed]`).

---

### Section 8: Checkout Experience Audit

*Full checkout flow not accessible (Angular SPA; the live flow was not clicked through). Findings are limited to front-end code and help docs.*

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | Custom-built; per-order gateway redirect/inline | — | Razorpay hosted checkout.js; Juspay inline form; Stripe.js tokenisation |
| Guest checkout | Not verified | — | |
| Steps to complete payment | Not verified | — | |
| Card input experience | Stripe.js v2 custom card fields → token (`api.stripe.com/v1/tokens`); Juspay tokenize for Juspay card orders | Fair | Tokenised, not raw PAN to Ketto |
| Payment methods visible | India: full UPI app list, netbanking, cards, wallets. Intl: cards | Good (IN) / Poor (intl) | |
| Location-based method display | Currency switch drives gateway (`INR` → Indian PSPs; non-INR → Stripe) | Fair | Methods do not adapt to donor country beyond cards |
| Instalment / EMI options | N/A for donations | — | |
| 3DS implementation | Not detected in front-end strings | — | Likely handled by the PSP; verify |
| PCI indicator | PSP tokenisation (Stripe, Juspay, Razorpay hosted) | — | See Section 9 |
| Mobile responsiveness | 89.93% of visits are mobile web; PhonePe/Paytm webview detection | — | Not visually tested |
| Multi-currency / local pricing | 12 currencies in code | Fair | Help centre says USD-only processing (likely stale) |
| Saved payment methods | Stripe `customer_id` + `save_card`; one-click for repeat Stripe donors | Good | |
| Error message clarity | Not verified | — | |
| Donor contribution / tip | "Voluntary contribution" to Ketto exists; whether it is pre-selected is not verified | — | Trustpilot complaints Jun–Jul 2026 |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found | — |
| Card data handling | Not found as a formal SAQ. Help centre: Ketto does not store card details and sees only the last 4 digits. | https://customerhappiness.ketto.org/portal/en/kb/articles/does-ketto-store-customer-s-payment-details `[UNVERIFIED — search summary only]` |
| Recommended Yuno integration | SDK (front-end tokenisation replacing Stripe.js on the non-INR leg) | — |

`[INFERENCE, not confirmed]`: based on confirmed client-side tokenisation through Stripe.js, Juspay and Razorpay hosted checkout, Ketto's PCI scope is likely reduced, with the PSPs handling card data.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: The diaspora corridor runs on one PSP, cards-only**
> **Evidence:**
> - S1: 15.35% of web traffic is outside India — Saudi 5.30%, US 3.17%, Canada 1.90%, UK 0.58%.
> - S3A: all non-INR currencies route to Stripe (code `"INR"!==iso_currency → getStripeToken`).
> - S4: no Apple Pay, Google Pay, mada or PayPal live; help centre says international donors pay by cards only.
> - S2: no entity in KSA, CA or UK.
>
> **Pain Point:** every foreign donation is a cross-border card transaction on one processor. There is no failover if that processor declines or goes down, and no wallet option on a 90% mobile-web flow. In medical crowdfunding, a failed donation is often not retried.
> **Yuno Value Proposition:** add local acquiring and wallets per corridor (Apple/Google Pay in US/CA/UK, mada in KSA), with smart routing and failover across more than one global acquirer, behind one integration on the non-INR leg only, without touching the domestic stack.
> **Best Success Case:** **GoFundMe** — same model, global donor base (logo-level only).
> **Outreach Angle:** "Your INR stack has five gateways and dynamic routing. Your dollar, riyal and pound donors get one processor and a card form."
> **Suggested Subject Line:** "Ketto's riyal and dollar donors"

> **Insight #2: Ketto already built the orchestration case — for India only**
> **Evidence:**
> - S3B: in-house gateway selector over Razorpay/Juspay/PayU/PhonePe/CAMSPay, Stripe failover, PayU A/B test.
> - S7: Razorpay case study: +0.2% SR = ₹1.7 Cr, UPI SR 72%.
>
> **Pain Point:** the team has proven that routing gains are worth crores, but keeps building and maintaining every gateway integration itself. International coverage hasn't had the same investment (S3A, S4).
> **Yuno Value Proposition:** opportunity cost — extend the routing logic they already believe in to global acquirers and APMs without building each integration.
> **Best Success Case:** the y.uno approval-rate testimonial ("+10%"). Verify its attribution first.
> **Outreach Angle:** "You've shown 0.2% of success rate is worth ₹1.7 Cr on UPI. What's the same number on foreign cards?"
> **Suggested Subject Line:** "₹1.7 Cr from 0.2%"

> **Insight #3: Recurring giving across borders (SIP) is fragile**
> **Evidence:**
> - S4: SIP runs 99% on UPI Autopay domestically; foreign recurring goes through `stripe_recurring` with client-side failover to a second Stripe key.
> - S5: a help article on "SIP amount debited twice", and an unconsented auto-debit complaint from a USD donor.
>
> **Pain Point:** involuntary churn on recurring international donors, and duplicate-charge risk where failover is hand-rolled.
> **Yuno Value Proposition:** network tokens, retry logic and cross-acquirer failover for recurring cards, handled by the platform rather than bespoke client code.
> **Best Success Case:** GoFundMe (recurring giving), logo-level.
> **Outreach Angle:** "Your foreign monthly donors fail over between two Stripe accounts in client code. There's a cleaner way to keep them."
> **Suggested Subject Line:** "Keeping Ketto's monthly donors abroad"

Caveat for every insight: FCRA limits which fundraisers can take foreign money. Size this in discovery before over-investing.

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks:**
1. Razorpay's case study credits Ketto with ₹1.7 Cr from a 0.2% success-rate gain. The same logic hasn't reached your non-INR donors, who all go through one processor.
2. About one in seven ketto.org visits comes from outside India (Saudi, US, Canada, UK), and those donors see a card form with no Apple Pay, Google Pay or mada.
3. You already route INR across five gateways in-house. Yuno does the same for the other 11 currencies you accept, without another build.

**Cold call openers:**
1. "Quick one — your INR stack is properly multi-gateway, but your foreign donations all hit Stripe. Is that by design or just where it landed?"
2. "Saudi is your second-biggest traffic market. How are those donors paying today?"
3. "When the Stripe recurring charge fails, you retry on the second Stripe account. Has that held up?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| ImpactGuru | impactguru.com | India | Rs 950 cr raised (2020); funds from 15+ countries | India + diaspora | **Razorpay** (majority of donations; dynamic routing; UPI SR 72%, cards 92.91%) — fetched | https://razorpay.com/blog/how-razorpay-empowered-impact-guru-to-enhance-donations/ |
| Milaap | milaap.org | India | Rs 1,200 cr+ over ten years (self-reported) | India + diaspora, multi-currency | Razorpay (weak: payment page on pages.razorpay.com) | https://pages.razorpay.com/pl_H3V0eoM9v1TliG/view |
| GiveIndia (Give) | give.do | India | 2.6M+ donors; FY25 revenue ₹7.9 cr+ | India + US donors | Not found | https://inc42.com/company/giveindia/ |
| Donatekart | donatekart.com | India | Seed $360K; 30,000+ donors | India, US, UK | **Razorpay** (since 2018) — fetched | https://razorpay.com/blog/how-donatekart-transformed-crowdfunding-with-razorpays-payment-solutions/ |
| GoFundMe | gofundme.com | US | Global leader | US, CA, UK — Ketto's diaspora markets | **Yuno** (named customer on y.uno) | https://www.y.uno/en/success-stories |

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Give.asia | give.asia | Donation crowdfunding | SG, Asia | Cross-border donors in SEA | https://help.give.asia/article/30-what-is-give-asia |
| SimplyGiving | simplygiving.com | Donation crowdfunding | SG, MY | Status unknown | https://digitalnewsasia.com/sizzle-fizzle/online-donation-startup-simplygiving-seeks-2nd-round-funding |
| Chuffed | chuffed.org | Donation crowdfunding | AU | ANZ card-heavy stack | https://www.smartcompany.com.au/startupsmart/this-charitable-crowdfunding-startups-pretty-chuffed-about-hitting-1-million-in-donations/ |
| JustGiving | justgiving.com | Donation platform | UK, global | Moved card volume to an orchestrator | https://gr4vy.com/posts/powering-purpose-at-scale-how-justgiving-optimized-global-donations-with-gr4vy/ |
| Art of Living (TAL row) | artofliving.org | Donations (religious/NGO) | India + global | TAL says Juspay orchestrator (unsourced) | `accounts/apac-tal.csv` |
| Kitabisa | kitabisa.com | Donation crowdfunding | Indonesia | No data found | — |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| JustGiving | Gr4vy (entire card + Click to Pay volume) | 12 Aug 2025 | Donation platform | https://gr4vy.com/posts/powering-purpose-at-scale-how-justgiving-optimized-global-donations-with-gr4vy/ |
| GoFundMe | Yuno | Date not published | Donation crowdfunding | https://www.y.uno/en/success-stories |

No Indian crowdfunding platform was found on a third-party orchestrator.

#### 11D. Prospect Scoring

Verified signals only; most peers are too thinly researched to score fully.

| Company | Signals verified | Score (partial) | Note |
|---------|-----------------|-----------------|------|
| ImpactGuru | Txn count ⬜; 3+ countries ⬜ ("15+ countries", no traffic); multiple PSPs ❌ (Razorpay only seen); greenfield orchestration (+4, no orchestrator found) | 4 + unknowns | Single-PSP (Razorpay) + diaspora donors. Worth a research run. |
| Milaap | Greenfield (+4); others unverified | 4 + unknowns | Multi-currency diaspora donors; PSP unclear |
| GiveIndia | Greenfield (+4)?; PSP not found | ⬜ | Too thin |
| Donatekart | Greenfield (+4); single PSP | 4 + unknowns | Small (seed-stage) |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Ketto | Target | IN + diaspora | 14 | 🟢 | Single-PSP intl leg, 400K txns/mo | **No — genuine find** |
| 2 | ImpactGuru | Direct competitor | IN + 15 countries | partial | Research next | Razorpay-only, diaspora donors | **No** |
| 3 | Milaap | Direct competitor | IN + diaspora | partial | Research next | Multi-currency, PSP unclear | **No** |
| 4 | GiveIndia | Direct competitor | IN, US | partial | Low | 2.6M donors | **No** |
| 5 | Donatekart | Direct competitor | IN, US, UK | partial | Low | Small | **No** |
| 6 | Give.asia | APAC peer | SG | partial | Low | — | **No** |
| 7 | Art of Living | Donations | IN + global | — | Check TAL | Juspay (unsourced) | Yes |

None of the Indian crowdfunding players are in `apac-tal.csv`. **ImpactGuru and Milaap are the two worth adding.**

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | ₹71.2–74.7 Cr FY25 (~US$8.5M) `[ESTIMATE, not confirmed]`; FY24 ₹83.0–86.1 Cr | Inc42 aggregator (figures conflict on the same page; no RoC filing seen) |
| GMV / Gross Transaction Volume | "INR 200+ crore from 10L+ donors in the past year" (medical) `[UNVERIFIED — search summary only, undated]`; USD 51.7M raised in 2021 `[search summary]` | https://faces.grantthornton.in/sociopreneurs/Varun-Sheth/index.html · https://www.ypo.org/2022/03/inspiration-is-closer-than-you-think-how-varun-sheths-crowdfunding-platform-is-changing-lives-in-asia/ |
| Average Transaction Value (USD) | Not found. ~₹2,000/donor/year implied by the GT figure `[INFERENCE, not confirmed]` | — |
| Est. Annual Transactions | ~4.8M (400K × 12) | Calculated from the sourced monthly figure |
| **Monthly transaction count** | **✅ SOURCED: ~400,000/month** — *"managing around 400,000 transactions monthly"*, Razorpay case study, 6 May 2025, https://razorpay.com/blog/ketto-journey-with-razorpays-upi-suite/. Billing unit: donation payments (one-time + monthly SIP debits). **Flags:** the same post's headline says "19K+ Donations a Year" (contradicts the body); scope (all gateways vs Razorpay only) not stated; vendor promo copy, 17 months old. Same post: >2.5 lakh monthly donors. | Sourced |
| Active Customers / Users | >2.5 lakh monthly donors (Razorpay, May 2025); 72 lakh cumulative donors `[UNVERIFIED]` | Razorpay; CB Insights |
| Primary Currency | INR; 11 foreign currencies accepted | Code |
| Top 3 Markets by Revenue | Not found. By web traffic: India, Saudi Arabia, US | Supplied Similarweb |
| Billing channel split (web vs app store) | Donations are not app-store IAP (payments go through Ketto's PSPs in-app as well). App installs 100K+ vs ~590K monthly mobile-web visits → **web-dominant** | Play Store; code |
| **International share of GMV** | **Not found — the key discovery question** | — |

---

### Overall Research Confidence

**Medium-High.**
- **Strong:**
  - PSP stack and orchestration status, read directly from Ketto's production JS.
  - Transaction count (vendor case study, fetched).
  - Legal entities (T&Cs, fetched).
  - Domestic payment methods.
- **Limited:**
  - Financials (aggregators conflict, no filing).
  - Funding (conflicting totals).
  - Live checkout (not clicked through).
  - International share of donations (not found).
  - Complaints (thin).
- **Traffic was supplied** (Similarweb Sales Intelligence, single domain, shares only; per-country visits derived). I pushed back on its "app-heavy" caveat: the evidence suggests mobile-web-first.

---

### Manual Research Recommendations

> **Area:** International share of donation GMV
> **Why it matters:** the whole Yuno opportunity sits on the non-INR leg. If it's ~2% of GMV, this is 🔴. If it's 10%+, it's a clean, contained deal.
> **Suggested manual action:** ask in discovery. Proxy: count foreign-currency donations on a few large medical campaigns' public donor lists.

> **Area:** Live checkout from a foreign IP
> **Why it matters:** confirms the 12-currency vs "USD-only" conflict, the USD 25 floor, whether wallets render via Stripe's hosted elements, and whether the voluntary contribution is pre-selected.
> **Suggested manual action:** VPN to US and KSA, open a medical fundraiser, go to the payment step, and record the `payment_gateway` returned by `/order` in DevTools.

> **Area:** Which entity holds Stripe `key_us`
> **Why it matters:** decides whether US donations are domestic (Delaware Inc) or cross-border from India.
> **Suggested manual action:** check the statement descriptor on a small test donation in USD.

> **Area:** GoFundMe reference usability
> **Why it matters:** it's the best proof point, but there is no public case study.
> **Suggested manual action:** ask Yuno marketing/AE owner what can be said about GoFundMe beyond the logo.

> **Area:** Contact
> **Why it matters:** Kartik Bhadada (Associate Director – Growth) is the named payments voice in the Razorpay case study, a warm-ish entry point.
> **Suggested manual action:** confirm he is still at Ketto on LinkedIn and find the tech/payments owner alongside him.

---

### Appendix: All Source URLs

**Traffic:** `accounts/traffic/ketto.md` (Similarweb, supplied 2026-10-19) · https://play.google.com/store/apps/details?id=org.ketto.sip&hl=en&gl=IN

**Entities:** https://www.ketto.org/terms-of-use · https://www.zaubacorp.com/company/U74900MH2012PTC238738 · https://knowyourgst.com/gst-number-search/ketto-online-ventures-private-ltd-27AAFCK0317C1Z3 · https://customerhappiness.ketto.org/portal/en/kb/articles/why-did-i-receive-an-80g-receipt-from-ketto-foundation-instead-of-the-ngo-i-donated-to

**PSP / code:** https://www.ketto.org/new/main.a35ce00e342acaff.js (+ lazy chunks via runtime.5718540c36de4240.js) · https://razorpay.com/blog/ketto-journey-with-razorpays-upi-suite/ · https://www.cashfree.com/case-study/ketto-saves-lives-by-facilitating-funds-collection-for-treatment-and-other-relief-campaigns-with-cashfree-payments · https://customerhappiness.ketto.org/portal/en/kb/articles/how-does-ketto-s-zero-platform-fee-model-work-7-8-2021

**Methods:** https://customerhappiness.ketto.org/portal/en/kb/articles/different-modes-of-payments-to-donate-6-8-2021 · https://customerhappiness.ketto.org/portal/en/kb/articles/what-are-the-payment-options-for-sip · https://customerhappiness.ketto.org/portal/en/kb/articles/why-were-foreign-donations-disabled-on-the-fundraisers · https://customerhappiness.ketto.org/portal/en/kb/articles/what-is-ketto-s-foreign-funds-transfer-policy · https://customerhappiness.ketto.org/portal/en/kb/articles/i-have-transacted-in-my-local-currency-but-i-have-been-charged-by-my-bank-in-usd-why-so-6-8-2021 · https://customerhappiness.ketto.org/portal/en/kb/articles/what-is-the-minimum-donation-on-ketto-6-8-2021

**Complaints:** https://www.trustpilot.com/review/ketto.org · https://www.pissedconsumer.com/ketto/RT-F.html · https://customerhappiness.ketto.org/portal/en/kb/articles/why-was-the-sip-amount-debited-twice · https://customerhappiness.ketto.org/portal/en/kb/articles/experiencing-issues-with-withdrawal · https://customerhappiness.ketto.org/portal/en/kb/articles/does-ketto-store-customer-s-payment-details

**Corporate / financials:** https://inc42.com/company/ketto/financials/ · https://www.cbinsights.com/company/ketto-online-ventures/financials · https://preqin.com/data/profile/asset/ketto-online-ventures-private-limited/126524 · https://businessworld.in/article/ketto-raises-700000-funds-led-by-calcutta-angels-the-chennai-angels-83702 · https://faces.grantthornton.in/sociopreneurs/Varun-Sheth/index.html · https://www.ypo.org/2022/03/inspiration-is-closer-than-you-think-how-varun-sheths-crowdfunding-platform-is-changing-lives-in-asia/

**Competitors / orchestration:** https://www.y.uno/en/success-stories · https://razorpay.com/blog/how-razorpay-empowered-impact-guru-to-enhance-donations/ · https://razorpay.com/blog/how-donatekart-transformed-crowdfunding-with-razorpays-payment-solutions/ · https://pages.razorpay.com/pl_H3V0eoM9v1TliG/view · https://inc42.com/company/giveindia/ · https://gr4vy.com/posts/powering-purpose-at-scale-how-justgiving-optimized-global-donations-with-gr4vy/ · https://help.give.asia/article/30-what-is-give-asia

</details>
