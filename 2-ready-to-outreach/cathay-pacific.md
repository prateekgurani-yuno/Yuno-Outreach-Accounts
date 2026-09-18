# Cathay Pacific

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 18 / 29 → ⭐ **High Priority** — earned on arithmetic, no override
**Industry:** Airlines (full-service + wholly-owned LCC) · **HQ:** Hong Kong — Cathay Pacific Airways Ltd, **HKEX 00293** · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** **Coverage play, not displacement.** No orchestrator detected, but **Adyen is confirmed and consolidated — in six markets out of 100+ destinations.** The pitch is the gap between those two numbers, never "you need orchestration".

---

> ## ⚠️ FIRST — a number in our own skill file was wrong, and it has been corrected
>
> `.claude/commands/full-outreach.md` said Cathay *"expanded to Adyen direct acquiring across **45+ markets**"*. **That is false.** I fetched the Adyen release myself:
>
> **Adyen provides direct acquiring for Cathay Pacific in six markets — Hong Kong, Australia, New Zealand, the United States, Japan and, most recently, India.** (Adyen newsroom, **23 March 2026**.) **The number 45 appears nowhere on the page**, nor in any syndication of it. Fintech Hong Kong headlined it *"Across 6 Key Markets"*.
>
> **Walking in citing 45 markets would have been repeating a number the merchant knows is false.** The skill file is fixed.
>
> Also from the release: the relationship **began in 2014**, Adyen is **not** described as sole, exclusive or primary, and Cathay reported a **10% authorisation-rate increase in India** after implementation. Named exec: **Kinto Chan, General Manager, Sales and Distribution**.

---

> ## 🎯 THE HOOK — six acquiring markets, thirty-three tenders, a hundred-plus destinations
>
> Cathay runs **33 distinct payment tenders**, enumerated on their own payment-options page: eight card schemes including **UnionPay and UATP**, Apple Pay and Google Pay, and **25 alternative methods** — among them **Digital Renminbi (e-CNY), FPS, PayMe, VietQR, QRPh, PayTo, UPI, RuPay, PayTM, PromptPay, KCP, Alipay, AlipayHK, WeChat Pay, Atome, Klarna, Affirm, Zip, iDeal and Sofort** — plus **Miles Plus Cash** split tender.
>
> **Adyen's direct acquiring covers six markets.** Cathay sells across **100+ destinations**, and **56% of all revenue originates in Greater China** — where Adyen's acquiring covers Hong Kong but **not mainland China or Taiwan.**
>
> **They already measure this.** The India result is on the public record: **+10% authorisation rate** from adding one market. That is a merchant that thinks in per-market auth rates and has published the proof.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Cathay Pacific is Hong Kong's flag carrier — **FY2025 group revenue HK$116,766m (+11.9%, ~US$15.0bn)**, attributable profit **HK$10.8bn**, its best since 2010. **28.9 million passengers** on the mainline plus **7.9 million on HK Express**, its wholly-owned and currently loss-making LCC, which runs a visibly separate payment stack.

**SimilarWeb total visits:** **Not obtained.** Geography below uses **revenue by origin of sale** from their own results, which is the better source anyway — origin of sale is where the payment is actually taken.

### Revenue by origin of sale — FY2025, HK$m
| Origin | 2025 | 2024 | Adyen direct acquiring? |
|---|---|---|---|
| **North Asia — Chinese Mainland, Hong Kong, Taiwan** | **65,846** | 61,442 | ⚠️ **Hong Kong only** |
| Americas | 16,011 | 14,615 | ✅ US |
| **Southeast Asia & Oceania** | **14,648** (+19.7%) | 12,239 | ⚠️ Australia, NZ only |
| Europe | 10,620 (+28.8%) | 8,247 | ❌ none |
| North Asia — Japan & Korea | 4,912 | 4,253 | ⚠️ **Japan only, not Korea** |
| **South Asia, Middle East & Africa** | **4,729 (+32.3%)** | 3,575 | ⚠️ **India only** |
| **Total** | **116,766** | 104,371 | |

> **The two fastest-growing origins are the two least covered.** South Asia/MEA +32.3% with acquiring in India only; Europe +28.8% with none at all.

### Accepted methods — 33 tenders, enumerated first-party
**Cards (8):** Visa · Mastercard · Amex · JCB · Diners Club · Discover · **UnionPay** · **UATP**. 3DS via Verified by Visa, Mastercard SecureCode, Amex SafeKey, J-Secure.
**Wallets:** Apple Pay · Google Pay.
**Other (25), verbatim:** Alipay · Affirm · AlipayHK · Atome · **Digital Renminbi (e-CNY)** · **FPS** · GrabPay · iDeal · KCP Credit Card · Klarna · Online Banking · **PayMe** · PayPal · PayPay · PayTM · **PayTo** · PromptPay · **QRPh** · RuPay · Sofort · **UPI** · **VietQR** · Wallets India · WeChat Pay · Zip.
**Plus Miles Plus Cash** — *"We also offer a mix of Miles Plus Cash as a payment option"*, minimum 5,000 miles, works on partner flights.

**Sourced absent:** ❌ **Octopus** — Hong Kong's flagship stored-value scheme, missing from the home carrier's checkout · ❌ PayNow (Singapore) · ❌ konbini (PayPay covers Japan instead) · ❌ GCash by name (QRPh covers PH via the national rail).

**Surcharging, confirmed and quantified:** **0.70%** on bookings departing **Australia** and **New Zealand**, capped **AUD 120 / NZD 70** per transaction, charged on the cash portion only for Miles Plus Cash, base including fare, taxes, fuel surcharges and ancillaries.

### Known PSPs
- **Adyen** — ✅ confirmed, direct acquiring in **six markets**, relationship since 2014, **+10% auth rate in India**
- ⚠️ **No second PSP could be named.** Checked the privacy notice, CSP headers and 653 KB of booking SPA bundles against 20+ vendors. **Zero hits** for Worldpay, Cybersource, Braintree, Stripe, Checkout.com, AsiaPay/PayDollar, Global Payments, Amadeus, Accelya, CellPoint. **This is not evidence of a single-PSP stack** — the payment step sits behind a live booking session nobody could reach.
- 📌 **UATP is at minimum one non-Adyen rail in production** — it settles on the airline-owned network, not a standard acquirer.

### Orchestration status
**None detected.** ⚠️ **Absence of hits, not affirmative evidence.** Searched Juspay, Spreedly, Primer, Gr4vy, APEXX, Payrails, IXOPAY, Yuno and "payment orchestration" across the privacy notice and the JS bundles. **CellPoint Digital checked hardest — it names Cebu Pacific, not Cathay.**

> **The distinction nobody could resolve, and it is the single best reason to get on a call:** is this *"Adyen as one integration with no routing layer"* or *"an in-house layer sitting above Adyen and others"*? Their self-hosted `api.` / `book.` / `flights.` topology is consistent with the latter. Consistent-with is not proof.

### Buying signals
- 📈 **+10% authorisation rate in India, published March 2026** — they measure auth by market and say so publicly
- 🌏 **20 new destinations launched in 2025; ~10% passenger capacity growth guided for 2026**; HK$100bn+ committed to fleet, cabin, lounges **and "digital innovation"**
- ✈️ **HK Express is loss-making and on a separate stack** — see the wedge below
- 🏆 **Singapore Airlines, their closest direct competitor, is on Juspay** (per our own airline reference)
- ❌ No payment RFP, no payments hire found, no named payments owner below Kinto Chan

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Cathay Pacific` to draft the 12-touch sequence.*

**Three instructions for whoever drafts it:**
1. ⛔ **Never say "45 markets."** Six. See the correction at the top.
2. **This is a coverage play.** They are consolidated on a strong provider and it is working. **Do not suggest they need orchestration** — open on the gap between six acquiring markets and a hundred-plus destinations, and on the two fastest-growing origins being the least covered.
3. **The India +10% is the single best opener** — it is their own published number, it proves they measure per-market auth, and it invites the obvious question about the other markets.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 18 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED as a bound, ~600,000+ bookings/month floor.** Sourced from their own FY2025 results: **28.9m mainline passengers plus 7.9m HK Express = 36.8m**, 79,100 and 21,700 per day respectively. **Billing unit: bookings, not passengers** — multi-passenger PNRs settle as one transaction, and agency/GDS/interline volume never touches their checkout at all, settling through BSP/IATA. Pushing back up: ancillaries, change and cancellation fees, the Cathay Shop, Cathay Holidays and Miles Plus Cash each authorise separately. **Even at an implausible 4 passengers per booking with zero ancillaries, 36.8m ÷ 12 ÷ 4 ≈ 767k/month.** Clears the top band under any divisor. ⚠️ Direct-channel share, transaction count and average ticket value are **not disclosed** — do not put a precise number in an email. |
| Orchestration status | **+4** | ✅ **None detected.** ⚠️ **Honest caveat: absence of hits, and nobody could distinguish "single Adyen integration" from "in-house layer above it."** Weaker than the affirmative greenfield calls elsewhere in this repo. |
| 3+ countries | **+3** | ✅ **100+ destinations**, revenue reported across **six origin-of-sale regions**, all six above HK$4.7bn. |
| Multiple PSPs | **0** | ⬜ **Only Adyen could be named.** UATP is a scheme settling on an airline-owned network, not a PSP, so it does not satisfy the 2+ rule. **The stack composition beyond Adyen is genuinely unknown** — the checkout requires a live PNR. |
| Local rail or licensing gap in a top-3 market | **0** | ❌ **Deliberately not awarded, and the reason matters.** With **33 tenders including e-CNY, FPS, PayMe, VietQR, QRPh, PayTo and UPI**, this merchant has done local methods unusually well. The only clear absence is **Octopus**, which is dominant in HK transit and retail but marginal for high-ticket online travel. **Awarding a rail gap here would be stretching. The gap in this account is acquiring coverage, not method coverage** — and that is a different and better argument. |
| Recent expansion | **+2** | ✅ **20 new destinations in 2025**, ~10% capacity growth guided for 2026, and **India acquiring added March 2026**. |
| Payment issues reported | **0** | ⬜ None found. Not searched to exhaustion, but nothing surfaced. |
| Funding >$10M | **0** | ❌ HKEX-listed. No round. |
| High traffic outside home | **+2** | ✅ **North Asia including Hong Kong is 56% of origin-of-sale revenue**, so Hong Kong alone is materially below the 60% threshold. ⚠️ **Basis is audited origin-of-sale revenue, not traffic** — no traffic data exists. Same approach the YesStyle and Amorepacific files took. |
| Competitor using orchestration | **+2** | ✅ **Singapore Airlines — Cathay's closest direct competitor — is listed on Juspay's own airline page**, per our airline reference. A premium Asian full-service carrier already running an orchestration layer is directly usable competitive intelligence. |
| Payment job postings | **0** | ⬜ None found; the careers site is JS-rendered and returned nothing server-side. |

**Tier: 18 / 29 → ⭐ High Priority.** No analyst override applied.

> **Why it earns ⭐ despite two zeroes.** The volume is enormous and sourced, the market count is genuine, the expansion is dated and first-party, and a direct competitor is already orchestrated. The two zeroes are honest: only one PSP is nameable, and **I refused to invent a rail gap at a merchant running 33 tenders.** The account's strength is the acquiring-coverage gap, which the matrix has no row for.

---

### ⭐ The sharpest commercial wedge — HK Express

**A wholly-owned, loss-making LCC on a visibly separate payment stack.**

- **FY2025: passenger revenue HK$6,394m (+6.7%), 7.9 million passengers (+29.7%)** — and **explicitly called out in the group release as a drag on profit**
- **Nine pricing currencies** — HKD, JPY, USD, CNY, KRW, THB, TWD, PHP, MYR — with method availability varying by currency
- **Its methods:** major cards, **Alipay, AlipayHK, Alipay+, Apple Pay, Google Pay, PayMe, UnionPay, WeChat Pay**, plus vouchers
- **Two hard differentiators from the mainline:** ① **Alipay+ is on HK Express and NOT on Cathay mainline** — the mainline lists Alipay and AlipayHK as separate tenders, a different wallet-aggregation approach entirely. ② HK Express carries **none** of the mainline's FPS, PayPal, Atome, Klarna, Affirm, Zip, PromptPay, UPI, e-CNY, VietQR, QRPh or UATP
- **Different CMS too** — HK Express on Sitecore Cloud, mainline on Adobe AEM. Independent digital estates
- ⚠️ **No PSP named anywhere on the HK Express estate**, and no Adyen string in its HTML — a weak negative, same caveat as the mainline

> **Why this is the wedge: LCC economics make MDR a board-level line item in a way it never is at a full-service carrier.** A loss-making subsidiary, a fast-growing Japan/Korea/SEA network, nine pricing currencies, a thinner separately-built stack, and no evidence it sits on the parent's Adyen relationship. **Group consolidation across two airlines is a story with a number attached.**

### Source Notes
- ✅ **The Adyen release was fetched and verified by me**, independently of the agent. Six markets, 23 March 2026, +10% India, relationship since 2014, not described as sole or exclusive, **and the number 45 appears nowhere on the page.**
- 📌 **Our own skill file has been corrected.** `.claude/commands/full-outreach.md` previously carried the false "45+ markets" claim in the shared airline reference, which would have propagated into every airline sequence. Fixed 2026-09-18 with the correction recorded inline.
- ✅ **All 33 tenders, the 3DS schemes, the surcharge terms and Miles Plus Cash come from Cathay's own payment-options page**, identical across the en_HK and en_US locales. The page itself notes *"Options may differ by market and product."*
- ✅ **FY2025 financials extracted from the results announcement PDF** and the 11 March 2026 release, not from a news summary.
- ⚠️ **`pay.cathaypacific.com` is NOT a payment gateway.** I checked it myself expecting the Ticketek `pay.` pattern — it is a **card-issuing marketing hub** fronting the Standard Chartered Cathay Mastercard co-brand, titled *"Earn miles faster"*. **Do not read it as acquiring infrastructure.**
- ⚠️ **CSP headers are a dead end here** — `script-src 'self' … https:` is wide open and lists no PSP domains. Absence of PSP JS in the marketing shell is **not** evidence of an in-house stack; the checkout is deeper in the funnel than any unauthenticated fetch reaches. `book.cathaypacific.com` returned 503.
- ⚠️ **The long-tail-APM hypothesis is NOT verified.** It is plausible that a six-market acquirer is not terminating e-CNY, VietQR, QRPh, PayTo and UATP end-to-end — **but nobody checked Adyen's published method coverage.** **Do not claim "Adyen can't do these" until someone reads `docs.adyen.com/payment-methods` method by method.**
- ❌ **Not established:** whether Adyen is sole or one of several; who processes the other ~27 markets; whether an in-house routing layer exists; transaction counts, direct-channel share, average ticket value, ancillary attach rate; current MDR or any auth figure beyond the India +10%; any named payments owner below Kinto Chan.
- 📌 **Highest-value unspent lead:** the **full Annual Report 2025** was never opened. The abbreviated results announcement contains **zero occurrences** of "payment", "digital", "e-commerce" or "ancillary" — the annual report is where a payments programme would surface.

### Manual Research Recommendations
> **1. Open the FY2025 Annual Report.** The unspent lead most likely to name a payments or digital-commerce programme.
> **2. Settle the in-house question on a call** — "is Adyen one integration, or is there a layer above it?" Nothing public answers it, and it decides the entire motion.
> **3. Check Adyen's published method coverage** for e-CNY, VietQR, QRPh, PayTo and UATP before implying any coverage gap.
> **4. Find the payments owner.** Kinto Chan (GM Sales & Distribution) is the only named exec; the actual owner sits below him.

---

## Executive Summary

Cathay Pacific is Hong Kong's flag carrier — **FY2025 revenue HK$116.8bn (~US$15.0bn, +11.9%)**, its best profit since 2010, **28.9 million mainline passengers plus 7.9 million on wholly-owned HK Express**. It runs **33 distinct payment tenders** including e-CNY, FPS, PayMe, VietQR, QRPh, PayTo, UPI, UATP and Miles Plus Cash split tender — an unusually well-built method estate. **The gap is not methods, it is acquiring coverage: Adyen provides direct acquiring in six markets against 100+ destinations**, with **56% of revenue originating in Greater China** where that covers Hong Kong but not the mainland or Taiwan, and with the two fastest-growing origins — South Asia/MEA at +32.3% and Europe at +28.8% — covered by India alone and not at all respectively. **They already measure this and published the proof: +10% authorisation rate in India from adding one market.** The sharpest wedge is **HK Express** — loss-making, called out as a drag on group profit, on a separate CMS, nine pricing currencies, a materially thinner method set, and no evidence it sits on the parent's Adyen relationship. **The motion is coverage and group consolidation, never "you need orchestration"** — and the "45 markets" figure in our own reference file was false and has been corrected.

</details>
