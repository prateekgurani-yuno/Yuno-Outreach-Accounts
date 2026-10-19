# Sony Interactive Entertainment (PlayStation)

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 22 / 29 → ⭐ High Priority **on arithmetic**. **ANALYST OVERRIDE applied: tier set DOWN to 🟢 Medium.** The reasoning is in the ICP breakdown.
**Industry:** Gaming. Console platform and first-party digital store (PlayStation Store on PS5/PS4, web and PlayStation App), plus PlayStation Plus subscriptions · **HQ:** San Mateo, California (SIE global HQ). APAC contracting entity: **Sony Interactive Entertainment Inc.**, 1-7-1 Konan, Minato-ku, Tokyo. Parent: Sony Group Corp. (Tokyo) · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **In-house.** SIE runs its own payment orchestration layer. A current SIE job ad lists "payment orchestration" as a programme area, and its Payments Analyst role measures performance "across providers". Adyen is visible in the web checkout code as the APM redirect environment, and Boku handles carrier billing. Never pitch "you need orchestration." Pitch coverage: the local rails and local acquiring this layer has not reached in India, Southeast Asia and Oceania. Yuno would plug in as a provider underneath SIE's orchestrator, not replace it.

---

> ## 🎯 THE HOOK: India is sold from London, by card only, and the cards don't work
>
> **1. The seller for India is a UK company.** The PlayStation Network Terms of Service for India name *"Sony Interactive Entertainment Network Europe Limited, company number 06020283, incorporated in England and Wales"* as the contracting party ([playstation.com/en-in/legal/terms-of-service](https://www.playstation.com/en-in/legal/terms-of-service/), fetched). The same ToS licenses products for *"Europe, the Middle East, Africa, India and Oceania"*. India sits in SIE's European region, not its Asian one. For Australia, which runs on the same UK entity, PlayStation states the consequence outright: *"Purchases from PlayStation Store are processed overseas, and your card issuer or bank may charge an international transaction fee"* ([en-au payment methods](https://www.playstation.com/en-au/support/store/payment-methods-accepted-on-ps-store/), fetched).
>
> **2. India's accepted methods, from PlayStation's own page, are complete in one line:** *"Visa Mastercard Apple Pay"* (Maestro can also be saved) ([en-in payment methods](https://www.playstation.com/en-in/support/store/payment-methods-accepted-on-ps-store/), fetched). There is no UPI, RuPay, netbanking or wallet. The checkout's own JavaScript agrees: its payment-method list includes PayPay, KakaoPay, Naver Pay, Rakuten Pay, Merpay, ShopeePay, Alipay, WeChat Pay, iDEAL, Klarna and PIX, and has **no UPI entry at all** (checkout.playstation.com bundle, retrieved 2026-10-19).
>
> **3. The result, as reported by Indian games journalist Rishi Alwani (2026-07-08):** *"The PS Store India payments infrastructure is beyond broken … near impossible for most gamers in the country to buy PlayStation games digitally with a debit or credit card issued in the country."* Players fall back on retailer gift-card top-ups. According to retailers, those are now capped at **INR 500,000 a week per retailer** ([0451 Games](https://0451games.substack.com/p/playstation-ps6-digital-future-no-discs-india-ps5), fetched). The same piece says people familiar with the company's plans call UPI "possible" but say the install base hasn't justified the investment, while Xbox already takes UPI.
>
> **4. The timing:** PS Plus prices in India rose up to ~30% for **existing** subscribers, from the next billing cycle on or after **2026-07-19** ([Smartprix](https://smartprix.com/bytes/sony-hikes-ps-plus-prices-in-india-all-three-tiers-now-cost-more-effective-july-19-2026/), fetched). Outlook Respawn reports India has *"at least 500K PlayStation Plus subscribers"* ([Outlook Respawn](https://respawn.outlookindia.com/gaming/gaming-news/playstation-plus-prices-see-up-to-30-hikes-in-india), fetched; their figure, attributed as "reportedly"). Every one of those renewals now runs at a higher ticket, on a foreign-acquired card, with no local fallback rail.
>
> **Who owns it:** India and Oceania payments sit with SIE Network Europe (London) and SIE's Global Payments team (San Diego / San Mateo), **not** Tokyo. Route the conversation accordingly.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Sony Interactive Entertainment runs the PlayStation platform: PS5/PS4 consoles, the PlayStation Store (console, web and PlayStation App), the PlayStation Plus subscription, and first-party studios. It is Sony Group's Game & Network Services (G&NS) segment, with FY2025 sales of **¥4,685.7bn** and a record operating income of **¥463.3bn** ([Sony Q4 FY25 deck, SEC 6-K](https://www.sec.gov/Archives/edgar/data/0000313838/000110465926057456/tm2613222d2_6k.htm), fetched). PSN had **125M monthly active users** in March 2026 (same source).

**SimilarWeb total visits (last full month):** ≈62.96M/month average, playstation.com only, Jul–Sep 2026 (188.8M over 3 months). Source: SimilarWeb (supplied 2026-10-19). **Caveats from the supplied file:** (1) the Sales Intelligence view shows top-10 shares only, with no per-country visits; (2) only playstation.com was pulled, not store.playstation.com or sonyinteractive.com; (3) mobile apps and console traffic are excluded; (4) **most PlayStation Store purchases happen on console and in the app, so web traffic is a market-mix signal and is never used here to size payments.**

### Top 5 markets
Ranked by the supplied playstation.com share. Only Japan is in territory among the top 5; India is #8. The APAC table below carries the pitch.

| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇺🇸 United States *(out of territory)* | 22.68% | Not assessed. The checkout code includes Venmo, Cash App, PayPal, Klarna | Not assessed: out of territory | ✅ SIE LLC (San Mateo) `[UNVERIFIED — search summary only]` |
| 2 | 🇯🇵 **Japan** | 7.08% | Visa, MC, JCB, Amex, PayPay, Rakuten Pay, Merpay, PayPal, carrier billing (docomo, au/KDDI, SoftBank), Apple Pay, PS Store card | Konbini payment, Paidy (BNPL) | ✅ SIE Inc. (seller of record) |
| 3 | 🇩🇪 Germany *(out of territory)* | 6.21% | Not assessed | Not assessed | ✅ Covered by SIENE (UK) / NL branch |
| 4 | 🇬🇧 UK *(out of territory)* | 6.01% | Not assessed | Not assessed | ✅ SIENE (UK) |
| 5 | 🇧🇷 Brazil *(out of territory)* | 5.62% | Not assessed. PIX is in the checkout code | Not assessed | Not researched |

### APAC markets (where the pitch actually is)
| Market | Traffic | PlayStation Store methods (official page, fetched 2026-10-19) | Missing methods | Seller of record / entity |
|---|---|---|---|---|
| 🇯🇵 Japan | 7.08% | Cards (Visa/MC/JCB/Amex), PayPay, Rakuten Pay, Merpay, PayPal, docomo/au/SoftBank carrier billing, Apple Pay, Store card | Konbini, Paidy | ✅ SIE Inc. (Tokyo) |
| 🇮🇳 **India** | 3.36% | **Visa, Mastercard, Apple Pay** (Maestro can be saved) | **UPI, UPI Autopay, RuPay, netbanking, wallets, EMI** | ❌ **SIENE (UK, 06020283).** No SIE India entity found |
| 🇰🇷 Korea | Not in top 10 | Naver Pay, KakaoPay, SKT/KT/LG U+ carrier billing, Visa/MC/JCB/Amex, Apple Pay, gift card | Toss; no domestic card brand named | ⚠️ Seller SIE Inc. (Japan). SIE Korea Inc. is the local agent |
| 🇦🇺 Australia | Not in top 10 | Visa, MC, Amex, PayPal, Apple Pay. *"Processed overseas"* | Afterpay, Zip, PayTo | ❌ SIENE (UK). No SIE Australia entity found |
| 🇳🇿 New Zealand | Not in top 10 | Visa, MC, PayPal, Apple Pay | POLi, BNPL | ❌ SIENE (UK) |
| 🇭🇰 Hong Kong | Not in top 10 | Visa/MC/Amex, Alipay, AlipayHK, WeChat Pay, WeChat Pay HK, PayPal, Apple Pay | Octopus, FPS | ⚠️ Seller SIE Inc. SIE Hong Kong Ltd `[UNVERIFIED — search summary only]` |
| 🇹🇼 Taiwan | Not in top 10 | Visa/MC/JCB, Apple Pay, carrier billing (Chunghwa, FarEasTone, Taiwan Mobile) | JKOPay, LINE Pay, convenience-store payment | ⚠️ Seller SIE Inc., which issues TW e-invoices itself |
| 🇸🇬 Singapore | Not in top 10 | Visa/MC/Amex, Alipay, PayPal, Apple Pay, ShopeePay | PayNow, GrabPay | ⚠️ Seller SIE Inc. SIE Singapore Pte. Ltd. `[UNVERIFIED]` |
| 🇮🇩 Indonesia | Not in top 10 | Visa/MC/JCB, ShopeePay | **QRIS, virtual account, GoPay, OVO, DANA** | ❌ Seller SIE Inc. No local entity found |
| 🇲🇾 Malaysia | Not in top 10 | Visa/MC, Apple Pay, ShopeePay (e-KYC) | **FPX, DuitNow, Touch 'n Go, GrabPay** | ❌ Seller SIE Inc. No local entity found |
| 🇹🇭 Thailand | Not in top 10 | Visa/MC/JCB, PayPal, Rabbit LINE Pay, ShopeePay | **PromptPay, TrueMoney** | ❌ Seller SIE Inc. No local entity found |
| 🇵🇭 Philippines | Not in top 10 | *"PlayStation online services are not available in the Philippines"* | The whole market (GCash, Maya) | ❌ Not served |

### Legal entities
- Sony Interactive Entertainment Inc. (Japan), 1-7-1 Konan, Minato-ku, Tokyo. **Seller of record for JP, KR, HK, TW, CN-template, SG, ID, MY, TH, PH, VN.** Corporate number not found.
- Sony Interactive Entertainment Network Europe Limited (UK). Company no. 06020283; NL branch 000051647869. **Seller of record for India, Australia, New Zealand.**
- Sony Interactive Entertainment Korea Inc. (Korea). Local agent; business reg. 106-86-02673 (from the ToS footer; attribution to SIE Korea is likely but the footer is ambiguous). Mail-order filing 2026-공정-0024.
- Sony Interactive Entertainment Singapore Pte. Ltd. (Singapore). Incorporated May 2019 `[UNVERIFIED — search summary only]`.
- Sony Interactive Entertainment Hong Kong Limited (Hong Kong) `[UNVERIFIED — search summary only]`.
- Sony Interactive Entertainment LLC (USA, San Mateo). Global HQ (out of territory).

### Known PSPs
- **Adyen** — `[Source Code]`: the checkout.playstation.com bundle has feature flag `FEATURE_APM_ADYEN_OVERRIDE_ENVIRONMENT`, which sets `ADYEN_ENVIRONMENT=ADYEN` on APM redirect URLs. Confirms Adyen in the alternative-payment-method (APM) redirect path. Which markets, and whether Adyen also acquires cards, is **not proven**.
- **Boku** — `[Source Code]` (payment methods `BOKU` / `BOKUDI` / `DCB_HOSTED` in the checkout bundle) + `[Third-Party Report]` (2013–2014 carrier-billing launches incl. Japan docomo/au, [Mobile Payments Today](https://www.mobilepaymentstoday.com/news/boku-expands-reach-of-carrier-billing-to-the-playstation/) `[UNVERIFIED — search summary only]`). Carrier billing.
- **PayPal** — `[Source Code]` + official payment pages (JP, AU, NZ, HK, SG, TH).
- **"Multiple providers"** — `[Job Listing]`: the SIE Payments Analyst role tracks *"authorization rates, chargebacks, declines, and processing costs across providers, regions, and payment methods"* ([anitab mirror](https://jobs.anitab.org/companies/sony-interactive-entertainment-2/jobs/81685282-payments-analyst), fetched, posted Jun 5, 2026).
- **The card acquirer(s) for any APAC market: not found.** No GMO, SBPS, Veritrans, KCP, Inicis, Razorpay, PayU, 2C2P, Xendit or similar was found anywhere.

### Orchestration status
**In-house orchestration layer.** Evidence:
- SIE's **Director, Program Management** posting (Greenhouse, first published 2026-08-28) is to *"Lead programs related to digital commerce, checkout modernization, payment processing, payment orchestration, subscriptions, entitlements, taxation, fraud prevention"* and to *"collaborate effectively with payment providers"* ([Greenhouse](https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6145077004), fetched via the Greenhouse API).
- The Payments Analyst role measures performance "across providers" (above).
- The checkout code is one commerce front end ("ONE_COMMERCE") with per-region legal variants (`SIEE`, `SIEJA`, `NON_SIEE`). It sits in front of a long list of per-method integrations.
- Sony Engagement Platform postings describe helping *"Sony operating companies consume SIE's payment orchestration capabilities"* `[UNVERIFIED — search summary only, page not fetched]`.

No Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails or Yuno found. Not a Yuno customer (Yuno's gaming page names NetEase only).

### Buying signals
- 💼 **Commerce & Payments Transformation leadership hire.** The Director, Program Management role names "checkout modernization … payment orchestration" and "improve conversion, payment success rates" ([Greenhouse](https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6145077004), published 2026-08-28, updated 2026-09-22).
- 💼 **Payments Analyst** (San Diego, posted 2026-06-05) tracks auth rates and costs across providers and methods ([anitab](https://jobs.anitab.org/companies/sony-interactive-entertainment-2/jobs/81685282-payments-analyst)). **Sr Manager, Fraud Operations, Investigations & Grey Markets** (published 2026-08-26) owns chargebacks and disputes ([Greenhouse](https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6162239004)).
- 💰 **India PS Plus repricing hits existing subscribers** at renewals from 2026-07-19, up to ~30% ([Smartprix](https://smartprix.com/bytes/sony-hikes-ps-plus-prices-in-india-all-three-tiers-now-cost-more-effective-july-19-2026/)).
- 🤝 **APMs are being added one market at a time.** Rakuten Pay and Merpay went live in Japan (now on the [official JP page](https://www.playstation.com/ja-jp/support/store/payment-methods-accepted-on-ps-store/); the 2025-11-14 launch date comes from third-party news, [usedoor.jp](https://usedoor.jp/news/2025-11-14-playstation-store-rakuten-pay-merpay/) `[UNVERIFIED — not fetched]`). LINE Pay was removed in Japan on 2025-03-28 when LINE Pay shut down ([Game*Spark](https://www.gamespark.jp/article/2025/02/18/149598.html) `[UNVERIFIED — not fetched]`).
- 📋 **India top-up channel capped.** Retailers report a INR 500,000/week ceiling on PlayStation wallet top-up sales ([0451 Games](https://0451games.substack.com/p/playstation-ps6-digital-future-no-discs-india-ps5), fetched). The fallback channel is being throttled while the primary channel (cards) fails.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Sony Interactive Entertainment (PlayStation)` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 22 / 29 (arithmetic) → override to 🟢 Medium
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | +5 | ✅ **DERIVED (floor): ≥1.9M/month even at absurd assumptions; realistically far higher.** G&NS FY2025 sales ¥4,685.7bn ([Sony 6-K](https://www.sec.gov/Archives/edgar/data/0000313838/000110465926057456/tm2613222d2_6k.htm), fetched). Strip out half as hardware/retail (the unverified segment split puts hardware at ~¥1.39tn, ~30%) → ¥2,343bn/yr → ¥195bn/month. Divide by a deliberately absurd ¥100,000 average ticket (roughly 10× a full-price game) → **~1.95M transactions/month**. The halving and the ticket are bounds I chose, not sourced figures, but no plausible values bring the count near 40,000. PSN MAU is 125M (same source). **Billing unit:** PlayStation Store purchases, wallet top-ups and PS Plus renewals, billed by SIE as merchant of record on its own store (not app-store IAP). The 40k gate cannot fire. |
| Orchestration status | +1 | ✅ In-house layer: "payment orchestration" in SIE's own Director posting (2026-08-28); "across providers" in the Payments Analyst posting |
| 3+ countries | +3 | ✅ All 10 supplied countries are above 1% web share; 3 seller-of-record entities across 15+ markets |
| Multiple PSPs | +3 | ✅ Adyen (APM redirect, `[Source Code]`), Boku (carrier billing, `[Source Code]`), PayPal (`[Source Code]` + official pages). The job ad confirms "across providers" |
| Local rail or licensing gap in a top-3 market | +3 | ✅ **Scored on in-territory rank.** India is the #2 APAC market by supplied traffic (#8 overall). UPI is absent from PlayStation's own India page and from the checkout code's payment-method list. The market is also served cross-border from a UK entity. **Under a strict overall-rank reading (top 3 = US, Japan, Germany), this is 0**: Japan has PayPay, and konbini alone is a weak gap. The tier is the same either way. |
| Recent expansion | 0 | ❌ No new market launch in 12 months. Rakuten Pay / Merpay (JP) are new rails, not expansion. The Philippines is still unserved. |
| Payment issues reported | +2 | ✅ Moderate. A fetched, named journalist piece (2026-07-08) describes India card payments as failing for "most" domestic cards. Retailer blogs corroborate it (JioGames, Jan 2026 `[UNVERIFIED]`). Sony keeps a per-region support page for general payment error E-8210604A. **Thin on first-hand complaints:** Reddit and app-store reviews could not be read in this run. |
| Funding >$10M | 0 | ❌ Wholly owned Sony subsidiary; no funding rounds |
| High traffic outside home | +2 | ✅ The US (HQ) is 22.68% of web traffic; Japan (APAC seller entity) is 7.08% |
| Competitor using orchestration | +2 | ✅ NetEase Games, a Yuno customer: *"With Yuno, NetEase brings those methods together on a single platform"* ([y.uno gaming](https://y.uno/en/industries/gaming.md), fetched 2026-10-19) |
| Payment job postings | +1 | ✅ Director (Commerce & Payments Transformation), Payments Analyst, Sr Manager Fraud Ops. All are 2026 postings, fetched |

**Tier on arithmetic:** 22 → ⭐ High Priority. No public payment RFP found.

**ANALYST OVERRIDE → 🟢 Medium.** Four reasons:
1. **SIE is an orchestrator, not a candidate for one.** It runs its own orchestration layer and reportedly sells it to other Sony companies through the Sony Engagement Platform (unverified). The best realistic outcome is Yuno as a **connectivity provider under SIE's orchestrator**: India local rails and acquiring, SEA wallets, ANZ local acquiring. That is a narrower, partnership-shaped deal than the matrix assumes. A +1 orchestration score doesn't capture how much it narrows the pitch.
2. **The APAC gaps sit outside the APAC volume core.** Japan, Korea and Hong Kong are already well covered (PayPay, Rakuten Pay, Merpay, carrier billing; Naver/KakaoPay; Alipay/WeChat Pay). The gaps are in India (3.36% web share; insiders cite a small install base), SEA and ANZ. These are real, but they are smaller markets for this account.
3. **Double-counting.** "3+ countries" and "high traffic outside home" both fire on one fact: SIE is a global business. The rail-gap +3 relies on the in-territory reading (above). Strip the duplicate and the gap → **17**, which is still ⭐ on paper but only just.
4. **The buyers are not in APAC.** India and Oceania belong to SIENE (London) and Global Payments (San Diego / San Mateo); SEA belongs to SIE Inc. (Tokyo) / SIE Singapore. That makes it a multi-stakeholder enterprise sale with a long cycle.

What keeps it at Medium and not Low: enormous volume, a payments leadership hire with "payment orchestration" and "checkout modernization" in the brief, and a sourced, specific India failure story. SIE has shown it adds APMs market by market (Japan 2025), and its own checkout code has no UPI.

### Source Notes
- ✅ India seller = SIENE (UK, 06020283); India + Oceania licensed under the European region. PSN ToS en-in/en-au/en-nz, fetched and grep-verified by me.
- ✅ SEA/HK/TW/KR/JP seller = SIE Inc. Regional ToS pages, fetched (KR, JP and TW confirmed by the research agent; SEA/HK template text grep-verified by me).
- ✅ Payment methods for IN, JP, KR, AU, NZ, HK, TW, SG, MY, ID, TH, PH: all 12 official pages fetched; text extracted by me.
- ✅ "Purchases from PlayStation Store are processed overseas": the en-au page, verbatim.
- ✅ Adyen APM flag, Boku, and the full payment-method enum (no UPI, GCash, QRIS, PromptPay or FPX): checkout.playstation.com JS bundle, downloaded and grepped by me on 2026-10-19.
- ✅ 3DS2 flow (threeDSMethod, cReq/cRes, challenge, `supported3DSFlow`): same bundle.
- ✅ G&NS ¥4,685.7bn / OI ¥463.3bn / MAU 125M / FY26 forecast ¥4,420bn: Sony 6-K, fetched and grepped by me.
- ✅ Director, Program Management (payment orchestration): Greenhouse API JSON, grepped by me. Payments Analyst ("across providers"): anitab mirror, fetched by me.
- ✅ India "beyond broken" + INR 500,000 weekly cap: 0451 Games, fetched by me.
- ✅ India PS Plus price rise for existing subscribers from 2026-07-19: Smartprix, fetched by me. "At least 500K PS Plus subscribers": Outlook Respawn, fetched; it is their "reportedly".
- ⚠️ Digital software ¥2,415bn / network services ¥763bn / hardware ¥1,392bn (FY2025): envalith.com via search summary; not cross-checked against Sony's supplemental data.
- ⚠️ SIE global HQ in San Mateo: SIE about-us page via search summary only.
- ⚠️ Sony Engagement Platform "SIE's payment orchestration capabilities" postings: search summary only (the page returned a stub).
- ⚠️ Rakuten Pay/Merpay launch date (2025-11-14) and LINE Pay removal (2025-03-28): third-party news, not fetched. The current method lists are verified.
- ⚠️ India RBI e-mandate impact on PS Plus renewals: JioGames retailer blog via search summary only. The retailer sells gift cards, so it has a commercial interest.

### Success Case Alternatives
- **NetEase Games (Yuno customer)**: the only named Yuno gaming case. It is a large Asian games company "across dozens of markets" with wallets, cash top-ups, gift cards and BNPL on a single platform ([y.uno](https://y.uno/en/industries/gaming.md)). It matches the multi-market, wallet-heavy problem. It is a weaker match on structure: SIE is a platform with its own orchestrator, not a publisher. **No NetEase metric is published; never attach a number.**

---

## Executive Summary

Sony Interactive Entertainment runs PlayStation: consoles, the PlayStation Store and PlayStation Plus. G&NS sales were ¥4,685.7bn in FY2025 and PSN has 125M MAU. SIE is the merchant of record on its own store, which makes it orchestration-addressable, and it already runs an **in-house payment orchestration layer** with Adyen (APM redirects), Boku (carrier billing) and PayPal visible in its checkout code. In APAC the layer covers Japan, Korea and Hong Kong well, but leaves three clear gaps. **India** is sold by a UK entity and accepts only Visa, Mastercard and Apple Pay, with no UPI anywhere in the checkout code, and payment failures are publicly described as severe. **SEA** has one regional wallet (ShopeePay) and none of QRIS, FPX or PromptPay, and the Philippines is not served. **ANZ** is processed "overseas" from the UK. The motion is **in-house**: Yuno pitches as a coverage and local-acquiring layer underneath SIE's orchestrator, with India as the lead.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** Path 1, pasted SimilarWeb data: `accounts/traffic/sony-interactive-entertainment-playstation.md`, SimilarWeb Sales Intelligence, supplied 2026-10-19. Not re-researched.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | United States | 22.68% | ~14.28M `[DERIVED from supplied share, not a SimilarWeb figure]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | **Japan** (APAC) | 7.08% | ~4.46M `[DERIVED]` | Not supplied | same |
| 3 | Germany | 6.21% | ~3.91M `[DERIVED]` | Not supplied | same |
| 4 | United Kingdom | 6.01% | ~3.78M `[DERIVED]` | Not supplied | same |
| 5 | Brazil | 5.62% | ~3.54M `[DERIVED]` | Not supplied | same |
| 6 | France | 4.21% | ~2.65M `[DERIVED]` | Not supplied | same |
| 7 | Mexico | 3.77% | ~2.37M `[DERIVED]` | Not supplied | same |
| 8 | **India** (APAC) | 3.36% | ~2.12M `[DERIVED]` | Not supplied | same |
| 9 | Canada | 2.87% | ~1.81M `[DERIVED]` | Not supplied | same |
| 10 | Spain | 2.85% | ~1.79M `[DERIVED]` | Not supplied | same |

- Derived visits = share × 62.96M average monthly visits.
- **High priority (>5%):** US, Japan, Germany, UK, Brazil. Only Japan is in territory.
- The listed top 10 cover 64.66%. **35.34% is unlisted.** Korea, Australia, Hong Kong, Taiwan and SEA fall inside that remainder, so their individual shares are **unknown** (each is below 2.85%).
- Device split: desktop 29.71% / mobile web 70.29%.
- **Caveats (from the supplied file):** single domain (playstation.com); store.playstation.com was not separated; mobile app and console traffic are excluded. **Web traffic understates transactions**, because most purchases happen on console and in the app. The country split is used as a market-mix signal only.
- **Correction to the traffic file's framing:** the console store and the PlayStation App store are **SIE's own storefront**. SIE is the seller of record (PSN ToS, §2) and bills through its own checkout, so this is not the app-store IAP trap described in `subscription-payments.md` §4. The shared checkout code carries console telemetry (`client:threeDsInfo`, platforms `["console"]`), which suggests the same commerce stack serves console `[INFERENCE, not confirmed]`.
- **Top-10 markets with no local seller entity:** India (sold by SIENE UK). See Section 2.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** San Mateo, California (SIE LLC, 2207 Bridgepointe Pkwy) per SIE's about-us page `[UNVERIFIED — search summary only]`. APAC contracting entity: Sony Interactive Entertainment Inc., Tokyo (ex-Sony Computer Entertainment, founded 1993). CEO: Hideaki Nishino, sole President & CEO since April 2025 ([Stevivor](https://stevivor.com/news/hideaki-nishino-to-be-sole-ceo-of-sony-interactive-entertainment) `[UNVERIFIED — search summary only]`; "대표: Hideaki Nishino" also appears in the KR ToS footer, fetched).

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Japan | 株式会社ソニー・インタラクティブエンタテインメント / Sony Interactive Entertainment Inc. | Not found | [ja-jp ToS](https://www.playstation.com/ja-jp/legal/terms-of-service/) (fetched) |
| South Korea | Seller: SIE Inc. Local agent: Sony Interactive Entertainment Korea Inc., 8F POSCO Tower Yeoksam, Gangnam-gu, Seoul | Business reg. 106-86-02673; mail-order 2026-공정-0024 | [ko-kr ToS](https://www.playstation.com/ko-kr/legal/terms-of-service/) (fetched) |
| Singapore | Sony Interactive Entertainment Singapore Pte. Ltd. (est. May 2019; runs SEA) | Not found | [gameindustry.ph](https://www.gameindustry.ph/reference/ysfydo) `[UNVERIFIED — search summary only]` |
| Hong Kong | Sony Interactive Entertainment Hong Kong Limited | Not found | same `[UNVERIFIED]` |
| India | **No SIE entity.** Seller: Sony Interactive Entertainment Network Europe Limited (UK). Hardware via Sony India `[UNVERIFIED]` | UK 06020283 | [en-in ToS](https://www.playstation.com/en-in/legal/terms-of-service/) (fetched) |
| Australia / NZ | **No SIE entity found.** Seller: SIENE (UK) | UK 06020283 | [en-au ToS](https://www.playstation.com/en-au/legal/terms-of-service/), [en-nz ToS](https://www.playstation.com/en-nz/legal/terms-of-service/) (fetched) |
| Taiwan | No local entity found. Seller SIE Inc., which issues TW uniform e-invoices itself (ToS §6.8) | Not found | [zh-hant-tw ToS](https://www.playstation.com/zh-hant-tw/legal/terms-of-service/) (fetched) |
| ID / MY / TH / PH / VN | No local entity found. Seller SIE Inc. (*"This Agreement is a contract between you and Sony Interactive Entertainment Inc."*) | — | en-id / en-my / en-th / en-ph / en-vn ToS (fetched) |
| China (mainland) | Not found. The zh-hans-cn ToS is the Greater China SIE Inc. template | — | zh-hans-cn ToS (fetched) |

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| Japan | ✅ #2 | ✅ SIE Inc. | N/A (entity present) | Low |
| India | ✅ #8 | ❌ Sold by SIENE (UK) | Not verified in this run; see note | **High.** Foreign-merchant cards, with failures reported |
| Korea | ❌ (unlisted) | ⚠️ Agent only; seller is SIE Inc. (JP) | Not verified in this run | Medium |
| Australia / NZ | ❌ (unlisted) | ❌ SIENE (UK) | No | **Confirmed:** *"processed overseas"* (official page) |
| HK / TW / SEA | ❌ (unlisted) | ⚠️ / ❌ Seller SIE Inc. (JP) | Not verified | Medium–High (share unknown) |

> *"Warning: Potential cross-border operation in India. No local entity found. Transactions are likely processed cross-border, with higher scheme costs, lower approval rates and FX exposure."* Supporting evidence: the seller is a UK company; the AU page under the same UK entity explicitly says purchases are "processed overseas"; and a named journalist reports most Indian-issued cards fail. Whether Indian acquiring is processed in the UK or elsewhere is `[INFERENCE, not confirmed]`.

> **Regulatory gate (India):** domestic UPI acceptance for a foreign merchant would normally need a locally licensed partner. **I did not source the current RBI rule in this run, so it is not cited as fact.** Verify before using.

> **MANUAL:** Check the India ToS payment clauses and the PS Store India receipt or bank statement descriptor (merchant name and country) to confirm where Indian card transactions are acquired.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Global (APM redirect path) | **Adyen** | `[Source Code]`: `FEATURE_APM_ADYEN_OVERRIDE_ENVIRONMENT` → `searchParams.set("ADYEN_ENVIRONMENT","ADYEN")` on APM redirects | checkout.playstation.com JS bundle (retrieved 2026-10-19) |
| Carrier billing (JP, TW, KR + others) | **Boku** | `[Source Code]` (`BOKU`, `BOKUDI`, `ONE_COMMERCE_NON_SIEE_DIGITAL_PREORDER_BOKU`) + `[Third-Party Report]` (2013–14 launches) | bundle; [Mobile Payments Today](https://www.mobilepaymentstoday.com/news/boku-expands-reach-of-carrier-billing-to-the-playstation/), [VS Daily](https://vsdaily.com/sony-extends-direct-carrier-billing-via-boku-outside-japan/) `[UNVERIFIED — search summary only]` |
| JP, AU, NZ, HK, SG, TH (+ global) | **PayPal** | `[Source Code]` + official payment pages | e.g. [en-au](https://www.playstation.com/en-au/support/store/payment-methods-accepted-on-ps-store/) |
| Europe (2016) | Paysafe / paysafecard via Worldpay (voucher method only) | `[Press Release]` | [Finextra](https://www.finextra.com/pressarticle/62972/paysafecard-comes-to-sony-playstation) `[UNVERIFIED — search summary only]` |
| Global | "Multiple providers" | `[Job Listing]`: "processing costs across providers, regions, and payment methods" | [anitab](https://jobs.anitab.org/companies/sony-interactive-entertainment-2/jobs/81685282-payments-analyst) (fetched) |
| Any APAC market: card acquirer | **Not found** | — | No GMO, SBPS, Veritrans, KOMOJU, KCP, Inicis, NICEPAY, Toss, Razorpay, PayU, Cashfree, CCAvenue, BillDesk, 2C2P, Xendit, Midtrans, Omise or iPay88 evidence |

The US privacy policy (v10, 08.2026) names processors only by category: *"Financial organisations and payment processors in order to obtain payment"* and *"Updated payment information provided by financial institutions or payment processors"*. The second points to an account-updater service ([privacy policy](https://www.playstation.com/en-us/legal/privacy-policy/), fetched by agent).

#### 3B. Payment Orchestrator

**Classification: In-house orchestration layer.**
- `[Job Listing]` Director, Program Management (Commerce & Payments Transformation): *"payment processing, payment orchestration, subscriptions, entitlements, taxation, fraud prevention"* ([Greenhouse](https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6145077004)).
- `[Job Listing]` Payments Analyst: performance "across providers" (above).
- `[Source Code]` A single "ONE_COMMERCE" checkout with per-legal-region variants (`SIEE`, `SIEJA`, `NON_SIEE`, `SCEE_EEA`, `SCEE_NON_EEA_AUSTRALIA`) and 25+ payment-method types behind one cart.
- `[Job Listing]` Sony Engagement Platform: "consume SIE's payment orchestration capabilities" `[UNVERIFIED — search summary only, page not fetched]`.

No third-party orchestrator found (Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno: all negative). The TAL `Payment Orchestrator` column is empty for this row. (The SonyLIV row shows Juspay, but SonyLIV is a separate Sony Pictures Networks India business, not SIE.)

> **Motion:** argue reach and opportunity cost, never "you need orchestration." SIE builds. The question is how many more one-off rail integrations (UPI, QRIS, FPX, PromptPay, GCash, PayTo) its team wants to build and maintain, versus plugging in one provider that already has them.

> **MANUAL:** Walk through checkout with DevTools on an IN and an SG account. Note the card-tokenisation iframe host (it identifies the card PSP) and the APM redirect domains.

---

### Section 4: Alternative & Local Payment Methods

All statuses come from PlayStation's official "Payment methods accepted on PS Store" pages, fetched 2026-10-19 (URL pattern `playstation.com/{locale}/support/store/payment-methods-accepted-on-ps-store/`). "Not found" means the method is absent from the official list **and** from the checkout code's payment-method list.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| Japan | Visa, MC, JCB, Amex | Cards | Active in checkout | [ja-jp](https://www.playstation.com/ja-jp/support/store/payment-methods-accepted-on-ps-store/) |
| Japan | PayPay, Rakuten Pay, Merpay, PayPal, Apple Pay | Digital wallet | Active (Rakuten Pay rolling out gradually on PS5) | same |
| Japan | docomo, au/KDDI, SoftBank (incl. Y!mobile, LINEMO) | Carrier billing | Active | same |
| Japan | PS Store card/ticket; Sony Bank WALLET (2% cashback) | Cash/voucher; cards | Active | same |
| Japan | Konbini payment | Cash/voucher | **Not found** (cards sold at retail are not a checkout method) | same |
| Japan | Paidy | BNPL | Not found | same |
| Japan | LINE Pay | Digital wallet | **Deprecated** 2025-03-28 (LINE Pay JP shut down) | [Game*Spark](https://www.gamespark.jp/article/2025/02/18/149598.html) `[UNVERIFIED — not fetched]` |
| **India** | Visa, Mastercard (Maestro can be saved) | Cards | Active | [en-in](https://www.playstation.com/en-in/support/store/payment-methods-accepted-on-ps-store/) |
| India | Apple Pay | Digital wallet | Active (listed) | same |
| India | **UPI, UPI Autopay** | Bank transfer / A2A; mandate | **Not found** (page + code) | same; checkout bundle |
| India | RuPay, netbanking, Paytm/PhonePe, EMI | Cards; A2A; wallet; instalments | Not found | same |
| India | PayPal | Digital wallet | Not found on the current page (an undated third-party blog says it once worked) | same |
| Korea | Naver Pay, KakaoPay, Apple Pay | Digital wallet | Active | [ko-kr](https://www.playstation.com/ko-kr/support/store/payment-methods-accepted-on-ps-store/) |
| Korea | SKT, KT, LG U+ | Carrier billing | Active | same |
| Korea | Visa, MC, JCB, Amex (no domestic brand named) | Cards | Active | same |
| Korea | Toss | Digital wallet | Not found | same |
| Australia | Visa, MC, Amex, PayPal, Apple Pay | Cards; wallet | Active, *"processed overseas"* | [en-au](https://www.playstation.com/en-au/support/store/payment-methods-accepted-on-ps-store/) |
| Australia | Afterpay, Zip, PayTo, BPAY | BNPL; A2A | Not found | same |
| New Zealand | Visa, MC, PayPal, Apple Pay | Cards; wallet | Active | [en-nz](https://www.playstation.com/en-nz/support/store/payment-methods-accepted-on-ps-store/) |
| Hong Kong | Visa, MC, Amex, Alipay, AlipayHK, WeChat Pay, WeChat Pay HK, PayPal, Apple Pay | Cards; wallets | Active | [zh-hant-hk](https://www.playstation.com/zh-hant-hk/support/store/payment-methods-accepted-on-ps-store/) |
| Hong Kong | Octopus, FPS | Wallet; A2A | Not found | same |
| Taiwan | Visa, MC, JCB, Apple Pay | Cards; wallet | Active | [zh-hant-tw](https://www.playstation.com/zh-hant-tw/support/store/payment-methods-accepted-on-ps-store/) |
| Taiwan | Chunghwa Telecom, FarEasTone, Taiwan Mobile | Carrier billing | Active | same |
| Taiwan | JKOPay, LINE Pay, convenience store, ATM transfer | Wallet; cash; A2A | Not found | same |
| Singapore | Visa, MC, Amex, Alipay, PayPal, Apple Pay, ShopeePay | Cards; wallets | Active | [en-sg](https://www.playstation.com/en-sg/support/store/payment-methods-accepted-on-ps-store/) |
| Singapore | PayNow, GrabPay | A2A; wallet | Not found | same |
| Malaysia | Visa, MC, Apple Pay, ShopeePay (e-KYC) | Cards; wallet | Active | [en-my](https://www.playstation.com/en-my/support/store/payment-methods-accepted-on-ps-store/) |
| Malaysia | FPX, DuitNow, Touch 'n Go, GrabPay, Boost | A2A; wallets | Not found | same |
| Indonesia | Visa, MC, JCB, ShopeePay | Cards; wallet | Active | [en-id](https://www.playstation.com/en-id/support/store/payment-methods-accepted-on-ps-store/) |
| Indonesia | QRIS, virtual account, GoPay, OVO, DANA, Alfamart/Indomaret | QR; A2A; wallets; cash | Not found | same |
| Thailand | Visa, MC, JCB, PayPal, Rabbit LINE Pay, ShopeePay | Cards; wallets | Active | [en-th](https://www.playstation.com/en-th/support/store/payment-methods-accepted-on-ps-store/) |
| Thailand | PromptPay, TrueMoney | A2A/QR; wallet | Not found | same |
| Philippines | — | — | **Market not served:** *"PlayStation online services are not available in the Philippines."* | [en-ph](https://www.playstation.com/en-ph/support/store/payment-methods-accepted-on-ps-store/) |
| Global | Instalments | BNPL/Instalments | **Capability exists in code** (`isInstallmentsEligible`, `FEATURE_INSTALLMENT_SELECTOR`, `INSTALLMENT_PAYMENT_INELIGIBLE_DEBIT_CARD_TRANSACTION`); live markets unknown | checkout bundle |

**Checkout-code payment-method list (complete, from the bundle):** `ALIPAY_PI`, `APPLE_PAY`, `BANCONTACT_MBL`, `BOKU`, `BOKUDI`, `CASHAPP`, `credit-card`, `DCB_HOSTED`, `IDEAL`, `IDEAL_DIRECT`, `KAKAOPAY`, `KLARNA`, `LINEPAY_PI`, `MERPAY`, `NAVERPAY`, `PAYPAL`, `PAYPALDI`, `PAYPAY_PI`, `PIX`, `RABBIT_LINE_PAY`, `RAKUTENPAY`, `SHOPEEPAY`, `VENMO`, `WECHATPAY_PI` (+ `WECHAT_CHINA`, `WECHAT_HONGKONG`). **Absent:** UPI, GCash, QRIS, DANA, OVO, GoPay, FPX, Touch 'n Go, PromptPay, TrueMoney, PayNow, GrabPay, JKOPay, Afterpay, PayTo, konbini, Paidy.

> *"Warning: In India, UPI is widely used but not currently supported by PlayStation Store."* For UPI's prominence, the only source in this run is the 0451 Games piece, which says UPI *"makes up a majority of online payments in the country"* ([0451 Games](https://0451games.substack.com/p/playstation-ps6-digital-future-no-discs-india-ps5)). Cite an NPCI/RBI figure before using a number in outreach.

> SEA dominant-rail prominence (QRIS, FPX, PromptPay) was **not separately sourced in this run**. The absences are sourced; their market share is not.

> **MANUAL:** VPN-check the IN and SG checkout to confirm the list matches the support page (e.g. whether ShopeePay shows on mobile web).

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Declined transactions: Indian-issued cards fail on PS Store India | Games journalism (0451 Games) | High (author's claim, not measured) | Published 2026-07-08 | [0451 Games](https://0451games.substack.com/p/playstation-ps6-digital-future-no-discs-india-ps5) (fetched) |
| Checkout errors: no UPI, so players use retailer gift cards, now capped at INR 500,000/week per retailer | Same | Structural | 2026 | same (fetched) |
| Failed recurring payments: PS Plus auto-renew failing on Indian cards (RBI e-mandate); gateway failures in the Jan 2026 sale | Retailer blog (JioGames) | Moderate (claim) | Jan 2026 | [JioGames](https://store.jiogames.com/blog/buy-gaming-gift-cards-using-upi), [JioGames sale](https://store.jiogames.com/blog/playstation-january-sale-2026) `[UNVERIFIED — search summary only]` |
| Generic payment error E-8210604A (re-register card, wait, use a store card) | Official support (per region) | Recurring (Sony maintains per-region pages) | Undated | [en-au E-8210604A](https://www.playstation.com/en-au/support/error-codes/ps4/e-8210604a/) `[UNVERIFIED — not fetched]` |
| False fraud lockouts: 24-hour block after repeated card updates; card country must match store region | Official support | Policy | © 2026 | [en-us card problems](https://www.playstation.com/en-us/support/store/ps-store-credit-debit-card-problems/) (fetched by agent) |
| Japan store refuses foreign-issued cards | Guides/forums | Long-standing, anecdotal | Older | [nihongoperapera](https://nihongoperapera.com/store/what-good-are-japanese-psn-cards.html) `[UNVERIFIED]` |
| Debit card accepted for PS Plus but "no longer valid" for games | Lowyat forum (MY) | Isolated | Feb 2021 | [Lowyat](https://forum.lowyat.net/topic/5102339/last) `[UNVERIFIED]` |

Reddit, X and app-store reviews could not be read in this run (the search tool can't reach reddit.com). That is a gap, not a finding of "no complaints".

> *"Pattern of card declines and renewal failures in India, on a stack that sells to India from a UK entity with no local rail, suggests a local-acquiring plus UPI / UPI Autopay opportunity."*

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 2026-10-15 | Sr. IT SOX Governance Lead posting, aligning SOX "with other compliance programs including PCI" | Payment Infrastructure Hiring | [Greenhouse](https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6216927004) (fetched) |
| 2 | 2026-08-28 | Director, Program Management: Commerce & Payments Transformation (checkout modernization, payment orchestration, payment success rates) | Payment Infrastructure Hiring | [Greenhouse](https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6145077004) (fetched) |
| 3 | 2026-08-26 | Sr Manager, Fraud Operations, Investigations & Grey Markets (chargebacks, disputes) | Payment Infrastructure Hiring | [Greenhouse](https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6162239004) (fetched) |
| 4 | 2026-06-05 | Payments Analyst: auth rates, declines, costs "across providers, regions, and payment methods" | Payment Infrastructure Hiring | [anitab](https://jobs.anitab.org/companies/sony-interactive-entertainment-2/jobs/81685282-payments-analyst) (fetched) |
| 5 | May 2026 (FY25 results) | FY2025 G&NS record OI ¥463.3bn, incl. ¥120.1bn Bungie impairment; FY26 forecast sales ¥4,420bn, OI ¥600bn | Financial | [Sony 6-K](https://www.sec.gov/Archives/edgar/data/0000313838/000110465926057456/tm2613222d2_6k.htm) (fetched) |

Also:
- **2025-04-01:** Hideaki Nishino became sole SIE President & CEO (Leadership Change) `[UNVERIFIED — search summary only]`.
- **2026-07-31:** Q1 FY26 results. G&NS sales ¥937.1bn, OI ¥202.0bn; FY26 forecast raised to ¥4,540bn sales, ¥660bn OI `[UNVERIFIED — search summary only]`.
- A frontofficesports URL carries a 2026-10-12 header about PlayStation layoffs after a missed sales target. Its date is unconfirmed (it may be 2024 coverage), so it is not used.

No public payment-related RFP found. The Director posting is the strongest signal of an active payments programme ("checkout modernization", "payment orchestration").

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 2026-07-08 | "The PS Store India payments infrastructure is beyond broken": no UPI; retailer top-ups capped at INR 500,000/week | India rail gap, failures | [0451 Games](https://0451games.substack.com/p/playstation-ps6-digital-future-no-discs-india-ps5) (fetched) |
| 2 | 2026-05-21/22 | PS Plus India up to ~30%, applied to **existing** subscribers from the billing cycle on or after 2026-07-19 | Recurring-billing pressure in India | [Smartprix](https://smartprix.com/bytes/sony-hikes-ps-plus-prices-in-india-all-three-tiers-now-cost-more-effective-july-19-2026/), [Outlook Respawn](https://respawn.outlookindia.com/gaming/gaming-news/playstation-plus-prices-see-up-to-30-hikes-in-india) (fetched) |
| 3 | 2026-05 | PS Plus Essential price rises for new subscribers in several regions | Global pricing | [Shacknews](https://www.shacknews.com/article/149181/ps-plus-price-increase-may-2026) `[UNVERIFIED — search summary only]` |
| 4 | 2025-11-14 | Rakuten Pay and Merpay added to PS Store Japan | APM addition, one market at a time | [usedoor.jp](https://usedoor.jp/news/2025-11-14-playstation-store-rakuten-pay-merpay/) `[UNVERIFIED — not fetched]`; methods confirmed on the [official JP page](https://www.playstation.com/ja-jp/support/store/payment-methods-accepted-on-ps-store/) |
| 5 | 2025-03-28 | LINE Pay removed from PS Store Japan | Provider removal | [Game*Spark](https://www.gamespark.jp/article/2025/02/18/149598.html) `[UNVERIFIED — not fetched]` |

> *"REMOVAL: PlayStation Store Japan discontinued LINE Pay as of 2025-03-28. Source: Game*Spark (above)."* This followed LINE Pay's own Japan shutdown, so it is not a PSP decision by SIE.

No PlayStation PSP partnership coverage found on The Paypers, Finextra or PYMNTS for 2025–2026.

---

### Section 8: Checkout Experience Audit

Full checkout flow not accessible (sign-in required). Findings are limited to publicly observable elements and the public checkout JS bundle.

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | Custom-built, centralised "ONE_COMMERCE" cart at checkout.playstation.com (Next.js) | Good (architecture) | Shared across web; console telemetry in the same code `[INFERENCE]` |
| Guest checkout | `ONE_COMMERCE_GUEST_COOKIE` exists; digital purchases need a PSN account | N/A | Account model inherent to the platform |
| Steps to complete payment | Not observable | — | — |
| Card input experience | Not observable (iframe host unknown) | — | MANUAL check |
| Payment methods visible | 25+ method types in code; per-market lists in Section 4 | Good (JP/KR/HK) / **Poor (IN, SEA, ANZ)** | |
| Location-based method display | Yes. Per-country lists; `MOBILE_APM_TO_FEATURE_FLAG_MAP` toggles methods per device | Good | |
| Instalment / EMI options | Capability in code; no APAC market confirmed; no India EMI | Fair | |
| 3DS implementation | **3DS2**: `threeDSMethod`, `cReq`/`cRes`, `challenge3dsUrl`, `supported3DSFlow`, `threeds2ResolutionRequired`, plus trusted-merchant (`threeDsIsOfferedTrustedMerchant`) fields | Good | `[Source Code]` |
| PCI indicator | Not determined | — | — |
| Mobile responsiveness | 70.29% of web visits are mobile web; mobile-specific APM flags exist | — | |
| Multi-currency / local pricing | Local pricing per store (e.g. INR PS Plus pricing) | Good | |
| Saved payment methods | Up to 3 cards + 1 payment service; wallet top-up model | Good | Official pages |
| Error message clarity | Specific APM error strings (`apmPurchaseExpired_*`, `THREE_DS_ERROR`, `PAYMENT_NOT_COMPLETED_ERROR`) | Fair | User-facing wording not observed |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found publicly. PCI is named as an SIE compliance programme in a current job ad | [Greenhouse SOX Lead](https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6216927004) (fetched) |
| Card data handling | Not found (SAQ type unknown). Card-on-file storage plus account-updater behaviour per the privacy policy | [privacy policy](https://www.playstation.com/en-us/legal/privacy-policy/) |
| Recommended Yuno integration | **Back-to-back API** as a provider under SIE's own orchestrator. The SDK is not relevant: SIE owns the front end | `[INFERENCE, not confirmed]` |

No direct PCI compliance documentation found publicly for Sony Interactive Entertainment. The 2011 PSN breach is historical context only and is not used.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: India is sold cross-border with a card-only checkout, and the cards fail**
> **Evidence:** S2: India's seller is SIENE (UK, 06020283), with India licensed under the European region ([en-in ToS](https://www.playstation.com/en-in/legal/terms-of-service/)). S4: official methods are Visa, Mastercard and Apple Pay, and there is no UPI in the checkout code. S5: "beyond broken… near impossible… with a debit or credit card issued in the country" ([0451](https://0451games.substack.com/p/playstation-ps6-digital-future-no-discs-india-ps5)). S7: PS Plus up ~30% for existing subscribers from 2026-07-19 ([Smartprix](https://smartprix.com/bytes/sony-hikes-ps-plus-prices-in-india-all-three-tiers-now-cost-more-effective-july-19-2026/)).
> **Pain Point:** Indian demand leaks to gift-card resellers (now capped), US accounts, or nowhere. PS Plus renewals at higher prices run on cards that fail on a foreign merchant. The market has ≥500K PS Plus subscribers (Outlook Respawn, "reportedly").
> **Yuno Value Proposition:** one integration under SIE's orchestrator for local Indian acquiring, UPI and UPI Autopay for PS Plus renewals, plus RuPay and netbanking, instead of a one-off build SIE has reportedly deferred for lack of install-base justification.
> **Best Success Case:** NetEase Games: multi-market gaming with wallet and cash rails on one platform. It matches the "many local rails, one integration" problem.
> **Outreach Angle:** "Your India store sells from a UK entity and takes Visa, Mastercard and Apple Pay. The press calls Indian card payments there 'beyond broken', and your PS Plus renewals in India just went up 30%."
> **Suggested Subject Line:** PS Store India: Visa, Mastercard, Apple Pay, and no UPI

> **Insight #2: SIE adds APMs one market at a time. Japan got three wallets; India and SEA got none**
> **Evidence:** S4/S7: Japan has PayPay, Rakuten Pay, Merpay and carrier billing, with Rakuten Pay and Merpay added in late 2025. The checkout code has 25+ method types. S4: SEA has one regional wallet (ShopeePay) and India has no local rail. S3B/S6: the Director role owns "payment orchestration… checkout modernization… payment success rates"; the Payments Analyst tracks costs "across providers".
> **Pain Point:** every new rail is a separate build in SIE's in-house layer. The backlog falls on the smaller markets (IN, ID, MY, TH, PH) where UPI, QRIS, FPX, PromptPay and GCash dominate.
> **Yuno Value Proposition:** reach and opportunity cost. A single provider connection adds the long-tail APAC rails without SIE's team building each one.
> **Best Success Case:** NetEase Games: "brings those methods together on a single platform… rather than managing integrations market by market" ([y.uno](https://y.uno/en/industries/gaming.md)).
> **Outreach Angle:** "Your checkout already handles PayPay, KakaoPay, Naver Pay and Merpay. UPI, QRIS, FPX and PromptPay aren't in it."
> **Suggested Subject Line:** PayPay and Merpay are in; QRIS, FPX and PromptPay aren't

> **Insight #3: Australia and NZ are processed "overseas", with no local BNPL or PayTo**
> **Evidence:** S2: the ANZ seller is SIENE (UK). S4: official AU page: *"Purchases from PlayStation Store are processed overseas, and your card issuer or bank may charge an international transaction fee"*. Methods are cards, PayPal and Apple Pay only; no Afterpay, Zip or PayTo.
> **Pain Point:** Australian cardholders pay international transaction fees on every purchase and renewal, and issuers treat the transactions as cross-border, with an approval-rate cost `[INFERENCE — no AU approval data sourced]`.
> **Yuno Value Proposition:** local acquiring in Australia routed beneath SIE's orchestrator, plus PayTo/BNPL coverage.
> **Best Success Case:** NetEase Games (only named gaming case). The profile match is weak for ANZ, so frame on mechanism.
> **Outreach Angle:** "Your own AU support page tells customers their bank may charge an international fee on every PS Store purchase."
> **Suggested Subject Line:** "Processed overseas": PS Store Australia

> **Insight #4: The Philippines is unserved, while peers sell there**
> **Evidence:** S4: *"PlayStation online services are not available in the Philippines"* (official page). S2: all SEA is contracted by SIE Inc. (Tokyo). S11: Steam reportedly accepts GCash in the Philippines ([NoypiGeeks](https://www.noypigeeks.com/how-tos/buy-steam-games-gcash/) `[UNVERIFIED — search summary only]`).
> **Pain Point:** a whole SEA market with no store. Any launch would need GCash/Maya from day one.
> **Yuno Value Proposition:** expansion readiness: launch-day local rails without a new integration project.
> **Best Success Case:** NetEase Games.
> **Outreach Angle:** use this only as a discovery question on a call. The reason PSN is unavailable in PH may not be payments.
> **Suggested Subject Line:** (Call topic, not an email lead.)

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. PlayStation's India page lists exactly three ways to pay (Visa, Mastercard, Apple Pay), and there's no UPI anywhere in your checkout code.
2. Your India and Australia stores are both sold by SIE Network Europe in London, and your AU page tells customers purchases are "processed overseas".
3. Your checkout already supports PayPay, Merpay, KakaoPay and Naver Pay; QRIS, FPX, PromptPay and GCash aren't in it.

**Cold call openers (conversational, one sentence each):**
1. "I saw the India PS Plus repricing went to existing subscribers in July. How are those renewals landing on Indian cards against a UK merchant?"
2. "Your Director of Commerce & Payments Transformation brief mentions payment orchestration. Is long-tail APAC rail coverage on that roadmap or parked?"
3. "Japan got Rakuten Pay and Merpay last year. What would it take to do the same for UPI in India?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| Nintendo | nintendo.com | Japan | ¥2,313.1bn net sales FY3/26 | JP, KR, HK, TW, SEA, ANZ | In-house platform; Adyen, PayPal, Alipay+ (KakaoPay), Paidy | `2-ready-to-outreach/nintendo.md` |
| Microsoft (Xbox) | xbox.com | USA | Not researched | Global | Worldpay (Microsoft storefronts incl. Xbox, 2021); Adyen (Microsoft globally, 2020) | [Business Wire](https://www.businesswire.com/news/home/20211026005071/en), [Adyen](https://www.adyen.com/press-and-media/adyen-and-microsoft-launch-network-token-optimization) `[UNVERIFIED — search summary only]` |
| Valve (Steam) | store.steampowered.com | USA | Private | Global incl. SEA | GCash (PH) via Smart2Pay/Nuvei; BoaCompra (LatAm) | [NoypiGeeks](https://www.noypigeeks.com/how-tos/buy-steam-games-gcash/) `[UNVERIFIED]` |
| Epic Games Store | epicgames.com | USA | Private | Global | Own payment service; Xsolla, PayPal | [Epic help](https://fortnitehelp.epicgames.com/help/en-US/billing-support-c99/general-support-c102/what-forms-of-payment-can-i-use-to-make-a-purchase-a3398) `[UNVERIFIED]` |
| Tencent Games / Level Infinite | levelinfinite.com | China / Singapore | Not researched | JP, KR, SEA | In-house (Midasbuy); TAL: In-house | TAL |
| NetEase Games | neteasegames.com | China | Not researched | JP, SEA | **Yuno** | [y.uno gaming](https://y.uno/en/industries/gaming.md) (fetched) |

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| HoYoverse | hoyoverse.com | Games | Global, APAC | In-house platform over 11+ PSPs; no UPI in India | `2-ready-to-outreach/hoyoverse-mihoyo.md` |
| Krafton | krafton.com | Games | KR, IN | Investment in Neon Commerce to "fully launch its proprietary payment system" (2026-07-23) | [Edaily](https://en.edaily.co.kr/news/eda202607235422) (fetched by agent) |
| Com2uS | com2us.com | Games | KR, global | PortOne orchestrator + Xsolla MoR | `2-ready-to-outreach/com2us.md` |
| Cygames | cygames.co.jp | Games | JP, global | GMO-PG (JP) / Xsolla split by a hard-coded country switch | `2-ready-to-outreach/cygames.md` |
| Webzen | webzen.com | Games | KR, SEA, LatAm | In-house Wcoin; PortOne on KR mobile | `2-ready-to-outreach/webzen.md` |
| Gravity | gravity.co.kr | Games | TW, SEA, LatAm | Greenfield, direct per-region PSPs | `2-ready-to-outreach/gravity.md` |
| Square Enix | square-enix.com | Games | JP, global | Cards + PayPal (TAL) | `accounts/apac-tal.csv` |
| Bandai Namco Entertainment | bandainamcoent.com | Games | JP, global | Not established | `accounts/apac-tal.csv` |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| NetEase Games | Yuno | Not dated publicly (cited 2025-09-26) | Games | [y.uno](https://y.uno/en/industries/gaming.md), [Fintech News SG](https://fintechnews.sg/119287/payments/yuno-apac-expansion-singapore-china/) |
| Com2uS | PortOne | Not dated | Games (KR) | `2-ready-to-outreach/com2us.md` |
| Webzen | PortOne (KR mobile) | PG list effective 2025-12-26 | Games (KR) | `2-ready-to-outreach/webzen.md` |
| Krafton | Neon Commerce (investment + in-house system; not a classic orchestrator) | 2026-07-23 | Games (KR) | [Edaily](https://en.edaily.co.kr/news/eda202607235422) |

The big platforms (Microsoft, Valve, Epic, Tencent, Nintendo) show no public third-party orchestrator. All build in-house or work with PSPs directly, as SIE does.

#### 11D. Prospect Scoring

Peers already scored in this repo (against the same /29 matrix); no rescoring in this run.

| Company | Score | Status | Evidence Source |
|---------|-------|--------|-----------------|
| Gravity | 24 / 29 ⭐ | Scored | `2-ready-to-outreach/gravity.md` |
| HoYoverse | 23 / 29 ⭐ | Scored | `2-ready-to-outreach/hoyoverse-mihoyo.md` |
| Nintendo | 22 / 29 ⭐ (reality check) | Scored | `2-ready-to-outreach/nintendo.md` |
| Com2uS | 21 / 29 ⭐ | Scored | `2-ready-to-outreach/com2us.md` |
| Razer | 20 / 29 → override 🟢 | Scored | `2-ready-to-outreach/razer.md` |
| Cygames | 19 / 29 ⭐ | Scored | `2-ready-to-outreach/cygames.md` |
| Webzen | 19 / 29 ⭐ | Scored | `2-ready-to-outreach/webzen.md` |
| Krafton | Not scored | Strong signal: building its own payment system with Neon (2026-07-23) | [Edaily](https://en.edaily.co.kr/news/eda202607235422) |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Gravity | Peer | TW, SEA, LatAm | 24 | ⭐ | Greenfield | Yes |
| 2 | HoYoverse | Peer | Global | 23 | ⭐ | No UPI in India | Yes |
| 3 | Nintendo | Competitor | JP, KR, HK, TW | 22 | ⭐ | JP console eShop rail gaps | Yes |
| 4 | Com2uS | Peer | KR | 21 | ⭐ | PortOne displacement | Yes |
| 5 | Cygames | Peer | JP | 19 | ⭐ | Hard-coded two-PSP split | Yes |
| 6 | Webzen | Peer | KR, SEA | 19 | ⭐ | PortOne on mobile | Yes |
| 7 | Krafton | Peer | KR, IN | Not scored | — | Building a proprietary payment system now | Yes |
| 8 | Bandai Namco Entertainment | Peer | JP | Not scored | — | — | Yes |
| 9 | Square Enix | Peer | JP | Not scored | — | — | Yes |
| 10 | Capcom | Peer | JP | Not scored | — | — | Yes |

Every peer here is already in the TAL. **Krafton** is the live one to research next: a July 2026 payments build with a large Indian base.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | G&NS sales ¥4,685.7bn FY2025 (to Mar 2026) ≈ **US$29.9bn** at the FY25 average ¥156.7/US$ | [Sony 6-K](https://www.sec.gov/Archives/edgar/data/0000313838/000110465926057456/tm2613222d2_6k.htm) (both figures from the deck). TAL says $31.7B (unsourced; likely a different rate or year) |
| GMV / Gross Transaction Volume | Not disclosed. Digital software & add-on content ¥2,415bn; network services ¥763bn (FY2025) `[UNVERIFIED — search summary only]`. Third-party digital sales are reported net, so consumer GMV is higher | envalith.com |
| Average Transaction Value (USD) | Not found | — |
| Est. Annual Transactions | Not computable from sourced inputs | — |
| **Monthly transaction count** | ✅ **DERIVED (floor): ≥1.9M/month.** ¥4,685.7bn × 50% (generous hardware strip) ÷ 12 ÷ ¥100,000 (absurd ceiling ticket). Revenue sourced; the strip and ticket are bounds I chose, not sourced. Billing unit: PS Store purchases, wallet top-ups, PS Plus renewals | See ICP row |
| Active Customers / Users | 125M PSN MAU (March 2026) | [Sony 6-K](https://www.sec.gov/Archives/edgar/data/0000313838/000110465926057456/tm2613222d2_6k.htm) |
| Primary Currency | JPY (reporting); local-currency stores | — |
| Top 3 Markets by Revenue | Not disclosed (no G&NS geographic split found) | — |
| Billing channel split (web vs app store) | SIE bills as merchant of record on its own store (console, web, PS App). Not app-store IAP. Exact console/web split not disclosed | PSN ToS |

---

### Overall Research Confidence

**Medium-High.** Traffic data was **supplied** (SimilarWeb, playstation.com only, top-10 shares only). APAC markets outside JP and IN are inside the unlisted 35%, so their individual shares are unknown.
- **Strong:** seller-of-record entities (ToS pages fetched); payment methods for 12 APAC markets (all official pages fetched); orchestration status (current job ads fetched); checkout payment-method list, Adyen and Boku (JS bundle grepped); financials (Sony 6-K fetched).
- **Limited:** card acquirer identity in any APAC market (not found); complaints (Reddit and app stores not reachable, so they rest on one fetched journalist piece plus retailer blogs); SEA rail market-share figures (not sourced); India regulatory gating (not sourced).

---

### Manual Research Recommendations

> **Area:** India card acquiring location and decline rates
> **Why it matters:** The lead insight assumes Indian cards are acquired cross-border. The ToS proves the UK seller, not the acquirer location.
> **Suggested manual action:** Ask an Indian PS Store buyer for the bank-statement descriptor (merchant name and country). Check the card-entry iframe host in DevTools on an en-in account.

> **Area:** UPI prominence and the RBI rules for foreign merchants / PS Plus e-mandate
> **Why it matters:** Needed before any number or regulatory claim goes into an email.
> **Suggested manual action:** Pull the current NPCI UPI share data and the RBI e-mandate and PA-CB circulars. Cite them in the outreach.

> **Area:** Who owns India/ANZ payments
> **Why it matters:** India and Oceania sit with SIENE (London) and Global Payments (San Diego), not Tokyo.
> **Suggested manual action:** On LinkedIn, find the Director, Program Management (Commerce & Payments Transformation) hire once filled, and the Payments Strategist EMEA / Global Payments leads.

> **Area:** First-hand complaint volume
> **Why it matters:** Payment-issues points rest on one journalist piece.
> **Suggested manual action:** Search r/IndianGaming and r/PS5 for "PS Store card declined India", and PlayStation App reviews on Google Play India.

> **Area:** Card PSP identity
> **Why it matters:** Adyen is proven only in the APM redirect path.
> **Suggested manual action:** DevTools on checkout (card iframe host, network calls) on IN, SG and AU accounts.

---

### Appendix: All Source URLs

**Traffic**
- `accounts/traffic/sony-interactive-entertainment-playstation.md` (SimilarWeb, supplied 2026-10-19)

**Legal entities (Section 2)**
- https://www.playstation.com/en-in/legal/terms-of-service/
- https://www.playstation.com/en-au/legal/terms-of-service/
- https://www.playstation.com/en-nz/legal/terms-of-service/
- https://www.playstation.com/ja-jp/legal/terms-of-service/
- https://www.playstation.com/ko-kr/legal/terms-of-service/
- https://www.playstation.com/zh-hant-tw/legal/terms-of-service/
- https://www.playstation.com/en-sg/legal/terms-of-service/ (and en-id, en-my, en-th, en-ph, en-vn, zh-hans-cn)
- https://www.gameindustry.ph/reference/ysfydo
- https://www.playstation.com/corporate/about-us/
- https://stevivor.com/news/hideaki-nishino-to-be-sole-ceo-of-sony-interactive-entertainment

**PSP stack (Section 3)**
- checkout.playstation.com JS bundle (retrieved 2026-10-19)
- https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6145077004
- https://jobs.anitab.org/companies/sony-interactive-entertainment-2/jobs/81685282-payments-analyst
- https://www.playstation.com/en-us/legal/privacy-policy/
- https://www.mobilepaymentstoday.com/news/boku-expands-reach-of-carrier-billing-to-the-playstation/
- https://vsdaily.com/sony-extends-direct-carrier-billing-via-boku-outside-japan/
- https://www.finextra.com/pressarticle/62972/paysafecard-comes-to-sony-playstation
- https://www.wearedevelopers.com/jobs/ext/7169773/payments-operations-analyst

**Payment methods (Section 4)**
- https://www.playstation.com/ja-jp/support/store/payment-methods-accepted-on-ps-store/
- https://www.playstation.com/en-in/support/store/payment-methods-accepted-on-ps-store/
- https://www.playstation.com/ko-kr/support/store/payment-methods-accepted-on-ps-store/
- https://www.playstation.com/en-au/support/store/payment-methods-accepted-on-ps-store/
- https://www.playstation.com/en-nz/support/store/payment-methods-accepted-on-ps-store/
- https://www.playstation.com/zh-hant-hk/support/store/payment-methods-accepted-on-ps-store/
- https://www.playstation.com/zh-hant-tw/support/store/payment-methods-accepted-on-ps-store/
- https://www.playstation.com/en-sg/support/store/payment-methods-accepted-on-ps-store/
- https://www.playstation.com/en-my/support/store/payment-methods-accepted-on-ps-store/
- https://www.playstation.com/en-id/support/store/payment-methods-accepted-on-ps-store/
- https://www.playstation.com/en-th/support/store/payment-methods-accepted-on-ps-store/
- https://www.playstation.com/en-ph/support/store/payment-methods-accepted-on-ps-store/
- https://usedoor.jp/news/2025-11-14-playstation-store-rakuten-pay-merpay/
- https://www.gamespark.jp/article/2025/02/18/149598.html

**Complaints (Section 5)**
- https://0451games.substack.com/p/playstation-ps6-digital-future-no-discs-india-ps5
- https://store.jiogames.com/blog/buy-gaming-gift-cards-using-upi
- https://store.jiogames.com/blog/playstation-january-sale-2026
- https://www.playstation.com/en-au/support/error-codes/ps4/e-8210604a/
- https://www.playstation.com/en-us/support/store/ps-store-credit-debit-card-problems/
- https://nihongoperapera.com/store/what-good-are-japanese-psn-cards.html
- https://forum.lowyat.net/topic/5102339/last

**Corporate & news (Sections 6–7)**
- https://www.sec.gov/Archives/edgar/data/0000313838/000110465926057456/tm2613222d2_6k.htm
- https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6162239004
- https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6216927004
- https://smartprix.com/bytes/sony-hikes-ps-plus-prices-in-india-all-three-tiers-now-cost-more-effective-july-19-2026/
- https://respawn.outlookindia.com/gaming/gaming-news/playstation-plus-prices-see-up-to-30-hikes-in-india
- https://www.shacknews.com/article/149181/ps-plus-price-increase-may-2026
- https://envalith.com/en/companies/6758/segments

**Competitors (Section 11)**
- https://y.uno/en/industries/gaming.md
- https://fintechnews.sg/119287/payments/yuno-apac-expansion-singapore-china/
- https://en.edaily.co.kr/news/eda202607235422
- https://www.businesswire.com/news/home/20211026005071/en
- https://www.adyen.com/press-and-media/adyen-and-microsoft-launch-network-token-optimization
- https://www.noypigeeks.com/how-tos/buy-steam-games-gcash/
- https://fortnitehelp.epicgames.com/help/en-US/billing-support-c99/general-support-c102/what-forms-of-payment-can-i-use-to-make-a-purchase-a3398
- Repo files: `2-ready-to-outreach/nintendo.md`, `hoyoverse-mihoyo.md`, `com2us.md`, `cygames.md`, `webzen.md`, `gravity.md`, `razer.md`; `accounts/apac-tal.csv`

</details>
