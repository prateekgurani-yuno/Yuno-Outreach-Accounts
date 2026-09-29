# Kuaishou Technology (HKEX: 1024)

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 17 / 29 → ⭐ **High Priority** — earned on the *addressable* perimeter, see the scope note
**Industry:** Short-video, live-streaming & live-commerce · **HQ:** Beijing, China (Cayman-incorporated parent) · **Researched:** 2026-09-29 · **First email sent:** —
**Motion:** **In-house.** Confirmed, not assumed — they run five acquirers in parallel with the routing config held in their own build.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Kuaishou is China's second-largest short-video platform (410.2m DAU, 724.6m MAU) with a very large live-commerce business (FY2025 GMV **RMB 1,598.1bn**) and FY2025 revenue of **RMB 142.8bn**. Internationally it runs **Kwai** (Brazil-centred), **SnackVideo** (Pakistan/Indonesia) and **Kling AI** (global AI-video subscription). It is a payments *buyer* at RMB-billions scale, not a payment company.

> ## 🎯 THE HOOK — they implement Visa four times and Pix three times, by hand
>
> Mined by me from the live `pay.kwai.com/recharge` production bundle on 2026-09-29. The provider enum carries **five acquirers** — dLocal, EBANX, Liquido, PayerMax, Checkout.com — and the same rail appears once per acquirer:
>
> | Rail | PSPs | Constants |
> |---|---|---|
> | **Visa** | **×4** | `CHECKOUT_VISA` · `DLOCAL_VISA` · `LIQUIDO_VISA` · `PAYERMAX_VISA` |
> | **Pix** | **×3** | `DLOCAL_PIX` · `EBANX_PIX` · `LIQUIDO_PIX` |
> | **Boleto** | **×3** | `DLOCAL_BOLETO` · `EBANX_BOLETO` · `LIQUIDO_BOLETO` |
> | Mastercard | ×3 | `CHECKOUT_MASTERCARD` · `DLOCAL_MASTERCARD` · `LIQUIDO_MASTERCARD` |
> | Amex | ×3 | `CHECKOUT_AMEX` · `DLOCAL_AMERICAN_EXPRESS` · `LIQUIDO_AMEX` |
> | Elo · Discover · Bank transfer | ×2 each | — |
>
> And the routing layer itself is visible — **two card acquirers' SDKs plus a country-suffixed key, in Kuaishou's own build config**:
> ```
> VUE_APP_CARD_PAY_URL          : static.dlocal.com/modules/fields/2.13.1/parent.js
> VUE_APP_CARD_PAY_KEY          : 99389b7a-26e6-4d51-aad9-90718c8e9138
> VUE_APP_CARD_PAY_KEY_EGY      : 1e41e246-3f07-459e-b83f-938a32b6fca4
> VUE_APP_CHECKOUT_CARD_PAY_URL : cdn.checkout.com/js/framesv2.min.js
> VUE_APP_CHECKOUT_CARD_PAY_KEY : pk_5d4itsb32z5onldkqqeyvyhy3ur
> ```
> **They already believe in multi-acquirer. Never pitch "you need orchestration."** The pitch is that a per-market key suffix is what they built instead of a routing engine.

> ## ⏰ DATED TRIGGER — their payment contract expires in ~3 months
>
> HKEX announcement 21 Nov 2023, read by me in the filed PDF:
> > *"The term of the 2023 Payment Services Framework Agreement will commence on January 1, 2024 and **end on December 31, 2026**, subject to renewal upon the mutual agreement of both parties."*
>
> Fees paid to Tencent for payment channels: FY2021 **RMB 896.2m** · FY2022 **RMB 1,009.5m** · 9M2023 **RMB 1,093.8m**. Annual caps: 2024 **1,672.0** · 2025 **1,792.0** · **2026 RMB 2,018.0m**.
>
> And they are **contractually obliged to benchmark**:
> > *"the Group will assess its business needs, and **compare the terms and conditions and services proposed by the Represented Tencent Group with those offered by other comparable service providers**… The Group will only enter into a specific agreement… if the terms are **no less favorable than those offered by other independent third party service providers**."*
>
> ⚠️ This is **China-domestic** and Yuno probably cannot serve it. Its value is that it proves scale, a benchmarking duty and a live renewal decision — it is a *reason to call now*, not the thing being sold.

**SimilarWeb total visits:** ⚠️ **Deliberately not used as a headline.** `kuaishou.com` draws ~3.7–7.8m visits/month against **410.2m app DAU** — web traffic understates this business by roughly two orders of magnitude, and two vendors disagree by 3× on rank. Use DAU/MAU and segment revenue. Full detail and the vendor conflict are in Section 1 of the research.

### Top 5 markets — by business, not by web traffic
| Rank | Country | Traffic / scale | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇨🇳 China | 410.2m DAU; GMV RMB 1,598.1bn | WeChat Pay, Alipay, UnionPay card rails, Kuaishou 月付 (BNPL) | — (fully served, closed loop) | ✅ Beijing Dajia; Beijing Kuaishou Technology |
| 2 | 🇧🇷 Brazil | *"our key market for overseas development"*; 61.5% of kwai.com traffic | Pix ×3, Boleto ×3, cards, Elo/Hipercard/Aura, Mercado Pago, PicPay, PayPal, 6× instalments | 10–12× instalments ⬜ (norm not sourced) | ✅ Joyo Tecnologia Brasil LTDA. |
| 3 | 🇮🇩 Indonesia | `IDN` a declared recharge market; SnackVideo 500m+ installs | Cards, IAP; GoPay/OVO/DANA/ShopeePay in the Shop bundle only | **QRIS ❌🔒** · Alfamart/Indomaret cash ❌ · **no local rail on coin top-up at all** | ❌ **none found in the group structure** |
| 4 | 🇵🇰 Pakistan | `PAK` a declared recharge market | **JazzCash, Easypaisa, HBL Konnect** (all via dLocal) | Well covered — do not pitch a gap here | ❌ none found |
| 5 | 🇮🇳 India | Kling AI only — 15.21% of kling.ai traffic | Kling web/Stripe; one user report of PhonePe UPI | Kwai & SnackVideo **blocked since 2020** | ⚠️ Kwai Technology India Pvt Ltd exists but the apps are banned |

### Legal entities
- **Kuaishou Technology** (Cayman Islands) — exempted company, incorporated 11 Feb 2014; listed HKEX 01024
- **Beijing Dajia Internet Information Technology Co., Ltd.** (PRC) — WFOE; the counterparty on the Tencent payment agreement
- **Beijing Kuaishou Technology Co., Ltd.** (北京快手科技有限公司) — opco
- **JOYO TECHNOLOGY PTE. LTD.** (Singapore) — **ACRA UEN 201621256R**, 1 Raffles Place #36-01. International holdco; app-store publisher of Kwai and SnackVideo
- **Kling AI Pte. Ltd.** (Singapore) — 1 Raffles Place #36-01, **same building and unit as Joyo**. No UEN found
- **Joyo Tecnologia Brasil LTDA.** (Brazil) · Joyo Technology Colombia S.A.S · Joyo Technology Peru S.A.C. · Kwai Kabushiki Kaisha (Japan) · Kwai Technology India Pvt Ltd

### Known PSPs — nine or more, no orchestrator
- **dLocal** — [Source Code] live Smart Fields SDK + two keys (global + Egypt) · Kwai recharge, Kwai Shop Brazil seller KYC
- **Checkout.com** — [Source Code] Frames v2 + live public key · Kwai recharge cards
- **EBANX** — [Source Code] provider enum + Kwai Shop seller KYC strings · Brazil/LatAm
- **Liquido** — [Source Code] provider enum · Brazil (Pix, Boleto, Elo, bank transfer)
- **PayerMax** — [Source Code] provider enum · Turkey/MENA (KNET, NAPS, TROY, Papara)
- **Stripe** — [Terms/Privacy Policy] + [Source Code] · **Kling AI only**
- **Antom** (Ant International) — [Source Code] "Antom Digital Account … Provided by Payment Institution AIBR" · Kwai Shop Brazil seller accounts ⚠️ *agent-reported, not re-verified by me*
- **Tencent / WeChat Pay + Alipay** — [Press Release / HKEX filing] · China domestic
- **Apple IAP / Google Play** — [Source Code] `IOS_IAP` 401, `GOOGLE_IAP` 402

### Orchestration status
**In-house orchestration layer — HIGH confidence.** Two card acquirers' SDKs ship in one build with per-market keys; China runs their own 快手收银台 (Kuaishou Cashier) with a `provider` enum and Kuaishou-owned `refund` / `settle` / `autoSettle` / `billQuery` APIs. Zero hits for any orchestrator across ~12 production bundles and every search.

> ⚠️ **The nuance that makes this sellable.** The in-house layer is genuinely well-built **for China**. Internationally what is observable is several direct PSP integrations plus per-market config keys — **not a demonstrable routing/failover engine**. Three acquirers live in Brazil alone, selected by static config. *That gap is the opening, not the wall.*

### Buying signals
- ⏰ **Tencent payment services agreement expires 2026-12-31** — with a contractual duty to benchmark against third parties ([HKEX, 21 Nov 2023](https://www1.hkexnews.hk/listedco/listconews/sehk/2023/1121/2023112100578.pdf))
- 📉 **Overseas flipped back into loss and is shrinking** — Q2 2026 operating loss RMB 25m vs **profit** RMB 19m in Q2 2025; H1 2026 loss RMB 56m vs profit RMB 47m. Overseas revenue Q2 2026 RMB 1,179m, **−9.3% YoY**
- 🚀 **Kling AI is the one thing compounding** — Q2 2026 revenue **>RMB 850m, +200%+ YoY**; Dec 2025 monthly run-rate >US$20m (≈US$240m ARR)
- 😠 **Trustpilot 1.2 / 5 across 398 reviews** for Kling AI, dominated by billing and cancellation failures
- 🇧🇷 One live BD req, **"Cartão Kwai", São Paulo** — ⚠️ read the JD: it is a **benefits/commerce platform, not a card product.** Do not pitch it as a card launch.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Kuaishou`.*

⚠️ **Read before drafting.**

1. **Lead with the rail redundancy: Visa ×4, Pix ×3, Boleto ×3.** It is their own code, it is not disputable, and it names an asymmetry inside their own stack. This is the sharpest observation on the account.
2. **Motion is IN-HOUSE. Never say "you need orchestration."** They built it. The frame is reach, failover and the opportunity cost of maintaining four Visa integrations.
3. **Never quote the Tencent RMB 2,018m cap as a Yuno-addressable number.** It is China-domestic payment channel fees. Use the *expiry date* and the *benchmarking clause*, not the amount.
4. **Do not claim Kuaishou owned a payment licence.** They tried for four years and failed — see the correction in §3.
5. **Do not pitch Pakistan as a gap.** JazzCash, Easypaisa and HBL Konnect are all live via dLocal.
6. **Route Brazil carefully — it is LATAM, not APAC.** Settle territory with the BDM before sending.
7. **The strongest single gap is QRIS in Indonesia**, and it is genuinely sourced. Coin top-up in Indonesia appears to have no local rail at all.
8. **Kling AI has its own file** — `2-ready-to-outreach/kling-ai.md`. If the conversation is about Kling, use that one.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 17 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED (bounded): >100,000/month by an enormous margin.** Sourced input: FY2025 e-commerce GMV **RMB 1,598.1bn** ([results release](https://www.prnewswire.com/news-releases/kuaishou-technology-announces-fourth-quarter-and-full-year-2025-financial-results-302724627.html)). ATV is **not** disclosed, so this is a bound, not a measurement: even at an implausibly high ATV of RMB 10,000, that is 13.3m orders/month. The band conclusion is robust to any plausible ATV. **Billing unit counted: e-commerce orders only** — live-streaming gifting and coin top-ups are additional and uncounted. |
| Orchestration status | **+1** | ✅ **In-house layer confirmed** (see §3B). Graded +1 by the matrix — correctly, it is the hardest sell. |
| 3+ countries | **+3** | ✅ Entities confirmed in China, Singapore, Brazil, Colombia, Peru, Japan, India |
| Multiple PSPs | **+3** | ✅ **Nine or more**, five of them in one bundle with live keys |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **QRIS absent in Indonesia**, a declared recharge market. Absence established by exhaustive bundle mining; QRIS prominence sourced to Bank Indonesia (~40m merchants, 57.6m users, Aug 2025) |
| Recent expansion | **0** | ⬜ No new-market launch in the last 12 months. Overseas revenue is **contracting** (−10.5% H1 2026) |
| Payment issues | **+2** | ✅ Trustpilot **1.2/5, 398 reviews**; named reviewers 2026-08-30 → 2026-09-25 reporting repeat charge attempts after confirmed cancellation |
| Funding >$10M | **0** | ❌ Listed company, no round |
| High traffic outside home | **0** | ❌ Overseas is **3.6% of FY2025 revenue** (RMB 5,074m of 142,776m). Home is overwhelmingly dominant |
| Competitor using orchestration | **0** | ❌ Gr4vy, Spreedly and Primer customer lists pulled directly — **no short-video, live-commerce or creator platform on any of them** |
| Payment job postings | **0** | ❌ **Sourced negative.** All 46 open reqs on the Workday portal enumerated via the CXS API; zero payment/billing/settlement/fraud engineering roles. *(Not checked: Chinese-language boards, where domestic 支付 roles would sit.)* |

**Tier:** ⭐ **High Priority (17+)**

> ### ⚠️ Scope note — read this before treating 17/29 as the whole story
> The score is real, but the **addressable perimeter is much smaller than the group**. China domestic (the overwhelming majority) is a closed loop: Tencent/Alipay channels, a captive UnionPay-and-bank direct arrangement, and a licensing regime Yuno cannot practically enter. **No override applied** — the addressable piece is still large (Kling ≈ RMB 3.4bn annualised + Kwai overseas ≈ RMB 5.1bn, ~US$1.2bn combined) and the multi-PSP evidence is exceptional. But size the business case on **Kling AI + Kwai overseas**, never on RMB 142.8bn.
>
> **Territory flag:** Kuaishou is in scope (China HQ). The overseas centre of gravity is **Brazil = LATAM**. Agree routing with the BDM before outreach.

### Source Notes
- ✅ Five-PSP provider enum, rail redundancy, dLocal/Checkout.com keys — mined by me from the live bundle, 2026-09-29, with 404-body sanity checks passed
- ✅ Tencent agreement term, fees and caps — read by me in the filed HKEX PDF (20 pages, 51,774 chars; controls "Tencent" ×181)
- ✅ FY2025 and Q2 2026 figures — read by me in the company's own results announcements
- ✅ Export-control screen clean on BIS Entity List, OFAC SDN and OFAC Consolidated (controls passed on all three)
- ⚠️ **DoD 1260H not verified** — the 188-entity list sits in regulations.gov docket DOD-2026-OS-1288; three retrieval routes blocked. Law-firm coverage names Tencent, Alibaba, Baidu, BYD — not Kuaishou. *1260H restricts DoD contracting, not payments; Tencent is on it and processes globally. Note, do not hold outreach on it.*
- ⚠️ Antom, the 3DS decline taxonomy and the "30% discount over Pix and cards" string — **agent-reported, not independently re-verified by me**
- ⚠️ Trustpilot figures — agent-verified, not re-fetched by me
- ⚠️ Brazil CNPJ 40.225.615/0001-30 — search-summary only; the entity *name* is confirmed in the prospectus
- ⚠️ Entity list rests on the **January 2021 draft prospectus** — five years stale. `ir.kuaishou.com` returns 403 to this environment

### Success Case Alternatives
- **A multi-market gaming or digital-goods merchant running several acquirers per region** — the profile match is "already multi-PSP, wants routing" rather than "needs its first orchestrator"
- ⚠️ **Do not use the circulating "Netflix +40% APAC subscriptions via orchestration" claim.** It traces to a single payments-vendor marketing page with no Netflix disclosure behind it. It appears fabricated.

---

## Executive Summary

Kuaishou Technology is China's #2 short-video and live-commerce platform — FY2025 revenue **RMB 142.8bn** (+12.5%), e-commerce GMV **RMB 1,598.1bn** (+15.0%), 410.2m DAU. Its international arm (Kwai, SnackVideo) is Brazil-centred and, despite reaching first-ever quarterly profitability in Q1 2025, has **flipped back into operating loss through 2026 with revenue declining ~10% YoY**. The key payment finding is that Kwai's international recharge checkout runs **five acquirers in parallel — dLocal, EBANX, Liquido, PayerMax and Checkout.com — with Visa implemented four times and Pix three times**, and the acquirer selection held as static, country-suffixed keys in their own build config. The motion is therefore **in-house**: they have already decided multi-acquirer is right and built the cheapest possible version of it, which is exactly the conversation Yuno should have. The one thing compounding in the group is **Kling AI**, at >RMB 850m in Q2 2026 (+200%+ YoY), billed from a Singapore entity on a single Stripe integration — covered in its own file.

---

## Section 1: Website Traffic Analysis by Country

**Data source:** WebSearch fallback via SimilarWeb and Semrush — **`[ESTIMATE, not confirmed]` throughout.** No SimilarWeb MCP is configured and no dataset was supplied for these domains. *(A supplied SimilarWeb dataset does exist for `kling.ai` — see `accounts/traffic/kling-ai.md` and the Kling file.)*

> ⚠️ **Do not build an argument on this section.** `kuaishou.com` draws ~3.7–7.8m visits/month against **410.2m app DAU**. This is an app-first business in every market; web traffic understates it by ~two orders of magnitude.

### kwai.com — `[ESTIMATE, not confirmed]`
| Rank | Country | Traffic Share | Est. Monthly Visits | Trend | Source |
|---|---|---|---|---|---|
| 1 | 🇧🇷 Brazil | **61.46%** | ⚠️ not reported — see note | — | similarweb.com/website/kwai.com |
| 2 | 🇺🇸 United States | 8.30% | ⚠️ | — | same |
| 3 | 🇨🇦 Canada | 1.53% | ⚠️ | — | same |
| 4 | 🇩🇪 Germany | 1.40% | ⚠️ | — | same |
| 5 | 🇮🇩 Indonesia | 1.31% | ⚠️ | — | same |

Global rank #433 `[ESTIMATE]`; 135.4m visits/3 months; −12.46% MoM.
⚠️ **Per-country visit counts are withheld deliberately** — the vendor returned internally contradictory figures (Germany at 1.4% share showing *more* visits than Brazil at 61.5%). Only shares are usable. A conflicting search summary gave Brazil 74.23% / US 4.26% / Indonesia 3.08% — `[UNVERIFIED — search summary only]`, and it disagrees with the fetched page.

### kuaishou.com — two vendors, sharply conflicting
| Vendor | Global rank | Visits (Aug 2026) | China share |
|---|---|---|---|
| SimilarWeb | #5,347 | 7.8m / 3 months | **85.82%** (then SG 5.19%, US 3.58%, HK 1.10%, TW 0.92%) |
| Semrush (via Exploding Topics) | **#15,164** | 3,710,853 | **39.46%** (then IN 14.15%, JP 8.08%, US 6.32%, BD 5.62%) |

**The conflict is unresolved — 3× on rank, 46pp on China share.** Directional only.

**Incidental:** Semrush outbound-traffic JSON from `kuaishou.com` shows `klingai.com` (3.7%) and **`kuaishoupay.com` (3.45%)**. `kuaishoupay.com` is a **parked brand page** registered to Beijing Dajia (ICP 京ICP备16009329号-3), **not a live payment product**.

### The reliable data — from the filings
| Period | Avg DAU (Kuaishou APP) | Avg MAU (Kuaishou APP) |
|---|---|---|
| FY2024 | 399.4m | 709.7m |
| **FY2025** | **410.2m** (+2.7%) | **724.6m** (+2.1%) |
| Q1 2026 | 412.7m (+1.2%) | 771.7m (+8.4%) |
| **Q2 2026** | 412.3m (+0.8%) | **797.3m (+11.5%)** |

⚠️ **No per-region MAU/DAU is disclosed in any filing.** Whether "Kuaishou APP" excludes Kwai/SnackVideo is **not defined** in the releases — implied by separate Overseas segment reporting, not stated. The only regional figure found anywhere: **Kwai has ~60m MAU in Brazil, >75 min/day** — a *company statement to Caixin citing unnamed third-party data* (11 Dec 2025), **not a filing figure**.

---

## Section 2: Legal Entities & Local Presence

**Headquarters:** Beijing, China. Parent incorporated in the Cayman Islands, 11 Feb 2014. Listed HKEX 01024.

| Country | Entity Name | Registration # | Source |
|---|---|---|---|
| Cayman | Kuaishou Technology | Exempted co., inc. 2014-02-11 | [HKEX prospectus](https://www1.hkexnews.hk/listedco/listconews/sehk/2021/0205/9616246/sehk21012400103.pdf) |
| PRC | Beijing Dajia Internet Information Technology Co., Ltd. | Inc. 2014-07-02 | prospectus; [HKEX CCT announcement](https://www1.hkexnews.hk/listedco/listconews/sehk/2023/1121/2023112100578.pdf) |
| PRC | Beijing Kuaishou Technology Co., Ltd. (北京快手科技有限公司) | Inc. 2015-03-20 | prospectus |
| PRC | Chengdu Suiyi Culture Communication Co., Ltd. | — | holds the Huarui Fuda licence — see §4 |
| **Singapore** | **JOYO TECHNOLOGY PTE. LTD.** | **ACRA UEN 201621256R**; LEI 9845006AD9E8HF115F24; ACTIVE. 1 Raffles Place #36-01 | [GLEIF](https://api.gleif.org/api/v1/lei-records?filter%5Bentity.legalName%5D=JOYO%20TECHNOLOGY%20PTE.%20LTD.) |
| **Singapore** | **Kling AI Pte. Ltd.** | **No UEN or LEI found** (GLEIF returns nothing). 1 Raffles Place #36-01 — same unit as Joyo | [kling.ai/docs/user-policy](https://kling.ai/docs/user-policy) |
| Brazil | Joyo Tecnologia Brasil LTDA. | CNPJ 40.225.615/0001-30 `[UNVERIFIED — registry blocked 423/403]` | prospectus |
| Colombia | Joyo Technology Colombia S.A.S | 100% Joyo Pte. Ltd. | prospectus |
| Peru | Joyo Technology Peru S.A.C. | 99% Joyo / 1% Qrite (HK) Holdings | prospectus |
| India | Kwai Technology India Private Limited | 100% Joyo Pte. Ltd. | prospectus |
| Japan | Kwai Kabushiki Kaisha | 99%/1% under Joyo | prospectus |

⚠️ **This list rests on the January 2021 draft prospectus — five years stale.** `ir.kuaishou.com` returns 403 to this environment, so the FY2025 annual report's principal-subsidiaries note was never read. Entities may have been added, renamed or wound up.

**Cross-Border Gap Analysis**

| Country | Top traffic? | Local entity? | Domestic acquiring gated? | Cross-border risk? |
|---|---|---|---|---|
| 🇨🇳 China | Yes (#1) | ✅ multiple | ✅ Yes — heavily licensed | N/A, fully domestic |
| 🇧🇷 Brazil | Yes (#2) | ✅ Joyo Tecnologia Brasil | Local acquiring available via dLocal/EBANX/Liquido | Low — locally acquired |
| 🇮🇩 **Indonesia** | Yes (#3, SnackVideo) | ❌ **none found anywhere in the group structure** | ⚠️ BI PJP licensing — verify current rules | **HIGH** |
| 🇵🇰 Pakistan | Yes (#4) | ❌ none found | ⚠️ verify | Moderate — dLocal covers the wallets |
| 🇮🇳 India | Kling only | ⚠️ entity exists, apps banned | ✅ Yes — RBI PA regime | Kling billed cross-border from Singapore |

> **Warning: potential cross-border operation in Indonesia.** No Indonesian entity appears anywhere in the group structure — the word "Indonesia" does not occur in the prospectus's History & Corporate Structure section, and the apps are published by **Joyo Technology Pte. Ltd. (Singapore)**. A claim that SnackVideo sits under "PT Karya Kreatif Nusantara" is `[UNVERIFIED — search summary only]`.

> **Regulatory gate: Indonesia.** Bank Indonesia's PJP licensing regime may require a licensed local partner for domestic acquiring. ⚠️ **Verify the current rules and cite a live source before this goes in an email** — per the APAC reference, never cite an APAC regulatory rule from background knowledge.

---

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

**There are three separate checkouts, not one.** This is the structural finding of the run.

| Surface | Host | Stack |
|---|---|---|
| Kwai coin / diamond recharge | `pay.kwai.com/recharge` | dLocal + EBANX + Liquido + PayerMax + Checkout.com + IAP |
| Kwai Shop (e-commerce) | `m-shop.kwai.com` / in-app | own `kspaySdk`; dLocal + EBANX + Antom on the seller side |
| Kling AI | `kling.ai` | **Stripe only** |

**Kuaishou does not use Stripe outside Kling AI.**

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|---|---|---|---|
| International (recharge) | **dLocal** — Smart Fields v2.13.1, keys `99389b7a-…` + Egypt `1e41e246-…` | `[Source Code]` | [chunk-common.b87d5fd3.js](https://s15-def.ap4r.com/kos/s101/nlav11312/kwai-wallet/static/js/chunk-common.b87d5fd3.js) |
| International (recharge) | **Checkout.com** — Frames v2, key `pk_5d4itsb32z5onldkqqeyvyhy3ur` | `[Source Code]` | same |
| Brazil / LatAm | **EBANX** — `EBANX_PIX/BOLETO/MERCADO_PAGO/PICPAY/PAYPAL/SPEI/PSE/NEQUI/OXXO_PAY` | `[Source Code]` | [diamond~recharge-index.d42e8c33.js](https://s15-def.ap4r.com/kos/s101/nlav11312/kwai-wallet/static/js/diamond~recharge-index.d42e8c33.js) |
| Brazil | **Liquido** — `LIQUIDO_PIX/BOLETO/ELO/VISA/MASTERCARD/AMEX/DISCOVER/BANK_TRANSFER` | `[Source Code]` | same |
| Turkey / MENA | **PayerMax** — `PAYERMAX_KNET/NAPS/TROY/PAPARA/GPAY/VISA/BANK_TRANSFER` | `[Source Code]` | same |
| Pakistan | **dLocal** — `DLOCAL_JAZZCASH`, `DLOCAL_EASYPAISA`, `DLOCAL_HBL_KONNECT` | `[Source Code]` | same |
| Egypt | **dLocal** — `DLOCAL_FAWRY`, `DLOCAL_MEZZA`, `DLOCAL_ALFA`, dedicated Egypt key | `[Source Code]` | same |
| Brazil (Kwai Shop sellers) | **dLocal** — *"dLocal is a payment institution officially cooperated by kwai shop"* | `[Source Code]` | shop `lang.*.js` ⚠️ agent-reported |
| Brazil (Kwai Shop sellers) | **EBANX** — *"EBANX-KYC … initiated by Kwai Shop's official partner bank"* | `[Source Code]` | same ⚠️ agent-reported |
| Brazil (Kwai Shop sellers) | **Antom** (Ant Intl) — *"Antom Digital Account … Provided by Payment Institution AIBR"* | `[Source Code]` | same ⚠️ agent-reported, role unresolved |
| Global (Kling AI) | **Stripe** — Elements, Adaptive Pricing currency selector, Stripe Tax | `[Source Code]` + `[Terms]` | [kling.ai/docs/payment-policy](https://kling.ai/docs/payment-policy) |
| China | **Tencent (WeChat Pay) + Alipay** — via Kuaishou's own cashier | `[Press Release]` | [HKEX CCT](https://www1.hkexnews.hk/listedco/listconews/sehk/2023/1121/2023112100578.pdf) |
| Global (payouts) | **Payoneer**, **PayPal** — creator cash-out | `[Source Code]` | kwai-wallet chunk ⚠️ agent-reported |
| Global | Apple IAP `401` / Google Play `402` | `[Source Code]` | recharge.39f207c8.js |

Full recharge market enum (`web_country`): **BRA, COL, MEX, ARG, PER, CHL, ECU, DOM, TUR, EGY, DZA, SAU, MAR, IRQ, JOR, IDN, PAK**. ⚠️ **Only two APAC markets in the entire list.**

### 3B. Payment Orchestrator

**Classification: IN-HOUSE ORCHESTRATION LAYER. Confidence HIGH.** The TAL's "In-house Routing" hypothesis is **independently confirmed**.

Evidence:
1. **Two card-tokenization SDKs in one production build.** A merchant does not embed both dLocal Smart Fields and Checkout.com Frames v2 unless something above them chooses.
2. **Per-market acquirer keys held by the merchant** — `VUE_APP_CARD_PAY_KEY` vs `VUE_APP_CARD_PAY_KEY_EGY`.
3. **Method list is server-driven** — no method enums hardcoded client-side, only result/error strings.
4. **A real cashier abstraction in China** — `create_order` (via 快手收银台) vs `create_order_with_channel`, a `provider` enum, and Kuaishou-owned `refund`/`settle`/`autoSettle`/`billQuery`.
5. **Nine-plus acquirers, zero orchestrator named** anywhere.
6. **Negative evidence:** no hit for Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno, IXOPAY or Corefy in ~12 production bundles or any search.

⚠️ **Against over-claiming:** no Kuaishou engineering blog, conference talk or repo describing a payment platform was found in English or Chinese. The orchestration reading is drawn from shipped artefacts and public APIs, **not from Kuaishou describing it**. Internationally, the honest reading is *direct integrations + static per-market config*, not a proven routing engine.

> **MANUAL:** Walk `pay.kwai.com/recharge` from a Brazilian IP with DevTools open and watch which acquirer takes the card. The server-side split between dLocal and Checkout.com is the one thing source-mining cannot settle.

---

## Section 4: Alternative & Local Payment Methods

| Market | Method | Category | Status | Source |
|---|---|---|---|---|
| 🇧🇷 Brazil | **Pix** (×3 PSPs) | Bank transfer/A2A | **Active in checkout** | recharge bundle enum |
| 🇧🇷 Brazil | **Boleto** (×3 PSPs) | Cash/voucher | **Active in checkout** | same |
| 🇧🇷 Brazil | **Instalments — up to 6×, min R$5.00** | BNPL/Instalments | **Active in checkout** — *"seu pagamento pode ser parcelado em até 6 vezes com parcela mínima de R$ 5,00"* | Kwai Shop `installment-desc` bundle |
| 🇧🇷 Brazil | Elo, Hipercard, Aura, Cartão Mercado Livre | Cards | **Active in checkout** | recharge enum |
| 🇧🇷 Brazil | Mercado Pago, PicPay, PayPal | Digital wallet | **Active in checkout** | recharge enum |
| 🇧🇷 Brazil | CPF tax-ID capture at checkout | — | **Active in checkout** — `cpf:!0`, 11-digit validator | recharge enum |
| 🇵🇰 Pakistan | **JazzCash, Easypaisa, HBL Konnect** | Digital wallet | **Active in checkout** | recharge enum |
| 🇮🇩 Indonesia | GoPay, ShopeePay, OVO, DANA, Bank Transfer | Digital wallet / A2A | **Mentioned in docs** — ship in the Kwai **Shop** checkout i18n (`k_351411`–`k_351415`), *not* in the recharge registry | shop `confirm-order` bundle |
| 🇮🇩 Indonesia | **QRIS** | Bank transfer/A2A | ❌ **NOT FOUND** — zero occurrences across every Kwai wallet and Shop chunk pulled | — |
| 🇮🇩 Indonesia | **Alfamart / Indomaret cash** | Cash/voucher | ❌ **NOT FOUND** | — |
| 🇮🇩 Indonesia | Any local method on **coin recharge** | — | ❌ **NOT FOUND** — `IDN` is in the market enum but no Indonesian method appears among the enumerated providers | recharge.39f207c8.js |
| 🇨🇳 China | Alipay, WeChat Pay | Digital wallet | **Active in checkout** | Kling `supportProviders`; HKEX filing |
| 🇮🇳 India | UPI via PhonePe **on Kling AI** | Bank transfer/A2A | **Mentioned in press** — a single first-person user report: *"paid ₹3,038.83 via PhonePe UPI"* | sikayetvar.com |
| 🇰🇷 Korea | KakaoPay, Naver Pay, Toss | Digital wallet | ❌ **NOT FOUND** | — |
| 🇯🇵 Japan | **konbini, bank transfer** | Cash / A2A | ❌ **NOT supported on Kling AI** — stated explicitly in a Japanese walkthrough | [note.com](https://note.com/yappyinsta/n/n01dd90acf143) |
| Global | Apple IAP, Google Play IAP | Carrier billing/IAP | **Active in checkout** | provider enum 401/402 |
| Global | **Carrier / direct operator billing** | Carrier billing | ❌ **NOT FOUND** — no DCB provider in any registry | — |

> **Warning: in Indonesia, QRIS is widely used but not supported by Kuaishou.** Bank Indonesia reports QRIS at ~40m merchants and 57.6m users as of Aug 2025 ([Jakarta Globe](https://jakartaglobe.id/business/bi-qris-adoption-hits-40-million-merchants), [Tempo](https://en.tempo.co/read/2036439/bi-qris-surpasses-57-million-users-expands-globally)); FY2025 volume 15.51bn transactions, +148.54% YoY ([Katadata](https://databoks.katadata.co.id/en/finance/statistics/6a2631bbc1a3f/the-number-of-qris-users-increased-74-in-the-q4-2025)). **The sharpest form of this: Kwai Shop got GoPay/OVO/DANA/ShopeePay; the higher-frequency coin-recharge surface got nothing.**

> ⚠️ **Pix is present but implemented three times over** — `EBANX_PIX`, `LIQUIDO_PIX`, `DLOCAL_PIX`. Pix reached ~42% of Brazilian online sales in 2025, overtaking credit cards at 41% — **but both available citations are EBANX-authored**, and EBANX is an incumbent on this very account. Flagging the conflict rather than laundering it.

> ⚠️ **Do NOT claim the Brazilian 6× instalment cap is low.** Brazilian e-commerce commonly runs to 10–12×, but no citable benchmark was found. **Ask it as a question, don't assert it as a deficiency.**

> ⚠️ **Methodology limit, applies to every ❌ above.** The channel endpoint `/rest/o/w/wallet-v2/recharge/third/groupTrail` is login-gated (returns `{"result":109}`), so these are the **client-side provider whitelist**, not a live per-market server response. The code falls back to a generic `REDIRECT` flow for unknown provider IDs — so the server *could* return methods absent from the enum. **Absence from the enum is strong evidence, not proof.**

---

## Section 5: Payment Issues & Customer Complaints

⚠️ All rows agent-verified from Trustpilot; not re-fetched by me.

| Issue Type | Platform | Frequency | Date Range | Source URL |
|---|---|---|---|---|
| **Recurring billing not stopping after cancellation — repeat charge attempts on a cancelled card** | Kling AI (web) | **HIGH** — multiple named, independent reviewers in one month | 2026-08-30 → 2026-09-25 | [trustpilot.com/review/klingai.com](https://www.trustpilot.com/review/klingai.com) |
| Charged after subscription period ended; refund refused citing policy | Kling AI | High (same cluster) | 2026-09-22 | same |
| Payment succeeded but credits not delivered / silently reduced after renewal | Kling AI | Moderate | 2026-09-01, 2026-09-25 | same |
| Kwai Brazil: recarga não creditada, reembolso não realizado, cannot unlink card | Kwai (Brazil) | ⚠️ **cannot state — volume unverified** | undated | `[UNVERIFIED]` reclameaqui.com.br (403 to both curl and WebFetch) |
| Withdrawal failures, IDR balance non-withdrawable | Kwai/SnackVideo (ID, PK) | cannot establish | undated | `[UNVERIFIED — search summary only]` |

**Trustpilot aggregate: TrustScore 1.2 / 5 across 398 reviews.** Billing and cancellation, not product quality, dominate the recent negatives.

Verified verbatim: Анна Владимировна, 2026-09-14 — *"Despite this confirmation, Kling has continued attempting to charge my card. There have now been **three payment attempts after the cancellation was confirmed**."*

> **Pattern:** the dominant complaint is **failure to cease recurring collection** — a subscription-lifecycle and mandate-cancellation failure, not a local-method gap. Be honest in outreach: this is not the classic approval-rate pitch. It *is* a clean argument for a routing layer that owns mandate state across PSPs.

> ⚠️ **Biggest gap in this section:** Reclame Aqui was 403-blocked on both routes, so **Brazil — their largest overseas market — has no quantified complaint volume.**

---

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|---|---|---|---|
| 1 | **2026-12-31** | **Tencent Payment Services Framework Agreement expires.** Caps: 2024 RMB 1,672.0m → 2025 1,792.0m → 2026 **2,018.0m**. Contractual duty to benchmark against third-party providers | **Payment Platform renewal** | [HKEX 21 Nov 2023](https://www1.hkexnews.hk/listedco/listconews/sehk/2023/1121/2023112100578.pdf) |
| 2 | 2026-08-19 | Q2 2026: **Kling AI revenue >RMB 850m, +200%+ YoY**; overseas back to operating loss RMB 25m | Financial | [Q2 2026 release](https://www.prnewswire.com/news-releases/kuaishou-technology-announces-second-quarter-and-interim-2026-unaudited-financial-results-302855081.html) |
| 3 | 2025-11-05 | **華瑞卡 (Huarui Card) business permanently ceased** — the group's only PBOC licence is now a dormant shell | Licence | [The Paper / 移动支付网](https://m.thepaper.cn/newsDetail_forward_31907598) |
| 4 | 2025-04-09 | **Payoneer acquires 100% of PayEco**, the licence Kuaishou chased for four years | M&A (competitive) | [Payoneer 10-Q, SEC](https://www.sec.gov/Archives/edgar/data/1845815/000155837025010514/payo-20250630x10q.htm) |
| 5 | listed through 2026-09-29 | Live req **"Cartão Kwai — Business Development Manager"**, São Paulo (R-25000486) | Hiring (BD, **not** payments) | [Workday](https://kwai.wd3.myworkdayjobs.com/Kuaishou_External/job/Sao-Paulo/Carto-Kwai---Business-Development-Manager_R-25000486) |

**Public payment RFP:** **No public payment-related RFP found.**

**Payment job postings: NONE — and this is a sourced negative.** All **46** open reqs on the external Workday portal were enumerated via the CXS API. Zero payment, billing, settlement, treasury, fraud or fintech engineering roles. Hiring is São Paulo-heavy (23/46), then Jakarta (7), Singapore (4), Bogotá, Cairo, Dubai, Riyadh. ⚠️ Chinese-language boards not checked — "absent" is established for the international portal only.

**Licence applications: NONE FOUND** in Brazil (BCB), Indonesia or Singapore (MAS). You flagged this as the strong APAC buying signal — **it is absent.**

> ⚠️ **Correction on "Cartão Kwai".** Despite the name, the JD describes *"an innovative embedded benefits platform"* covering mobile recharges, discounted data plans, cashback and healthcare — seeking telecom, e-commerce and healthcare partnerships. **It is not a card, wallet or credit product.** No evidence of an issuing or acquiring licence in Brazil. Do not pitch it as a card launch.

---

## Section 7: Payment-Specific News

| # | Date | Headline / Summary | Relevance | Source URL |
|---|---|---|---|---|
| 1 | 2025-11-05 | **REMOVAL: Huarui Payment ceased all 華瑞卡 business** — sales, top-up and spending — citing "内部战略调整", moving to refund servicing only | The group's only PBOC licence is now dormant | [thepaper.cn](https://m.thepaper.cn/newsDetail_forward_31907598) |
| 2 | 2025-04-09 | Payoneer becomes the third foreign platform licensed for online payments in China, via PayEco | The licence Kuaishou failed to get | [Payoneer 10-Q](https://www.sec.gov/Archives/edgar/data/1845815/000155837025010514/payo-20250630x10q.htm) |
| 3 | 2024-11-03 | PBOC approves Huarui Fuda shareholder change to Chengdu Suiyi (Kuaishou co-founders' vehicle) | Licence acquired — then shelved | [Jiemian](https://www.jiemian.com/article/11935020.html) |
| 4 | 2024-08-07 | **Kling AI announces credit-card acceptance** (Visa, Mastercard "and more options") as a *"Payment System Upgrade"* — i.e. cards were **not** available at launch | Kling's card stack is ~2 years old | [x.com/Kling_ai](https://x.com/Kling_ai/status/1821172427797516475) |
| 5 | 2025-12-11 | Kwai Shop launched Brazil 2024; international turned a **first-ever quarterly profit in Q1 2025**; TikTok Shop entered Brazil May 2025 | Competitive pressure in their #1 overseas market | [Caixin](https://www.caixinglobal.com/2025-12-11/kuaishous-kwai-conquers-brazil-by-ditching-the-time-machine-strategy-102392161.html) (paywalled preview) |

**PayEco divestiture coverage from Kuaishou's side: NOT FOUND.** No Chinese or payments trade press explains why they exited or what replaced it. The Q2 2026 release contains **zero** mentions of PayEco, Easylink or "payment licence" (verified by grep on the fetched text).

---

## Section 8: Checkout Experience Audit

Three checkouts, audited to different depths. **The Kwai Shop buyer-side checkout is in-app and was not observable.**

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | Kwai recharge: embedded, hosted card fields (dLocal Smart Fields / Checkout.com Frames v2). Kling: embedded Stripe Elements | Good | PAN never touches their DOM |
| Guest checkout | **Not available on Kling** — *"must be operated after you log in… if you do not log in you will not be able to purchase"* (Terms §6.2.1) | Fair | Deliberate; ties billing to account |
| Card input | Tokenized iframe, both stacks | Good | — |
| Methods visible | Kwai: 5-PSP enum by market. Kling: cards + Alipay/WeChat (CN only) | Mixed | — |
| Location-based method display | Kwai: **yes** — `web_country` enum drives it. Kling: **no affirmative evidence it adapts** | Poor (Kling) | Kling Terms punt: *"payment methods supported by different payment service providers may be different"* |
| Instalments | Brazil 6× min R$5.00. **None evidenced in India, Japan, Taiwan, Korea** | Fair | — |
| 3DS | **Not established.** No source describes 3DS/SCA behaviour on either stack | Unknown | ⚠️ Stripe and hosted fields both perform 3DS server-side — **bundle absence proves nothing.** Do not claim they lack 3DS |
| PCI indicator | Hosted fields / iframe on both | Good | Consistent with SAQ A / A-EP |
| Multi-currency | **Kling: USD-anchored** (*"$1 USD = 66 Credits"*) with a Stripe currency selector mounted. Japanese walkthrough describes USD prices converted at card FX of 1.6–3.0%, *billed amount varying month to month on the same plan* | Poor | ⚠️ Tension unresolved — see Manual Research |
| Saved payment methods | Yes — *"payment account bound with your User Account"*, auto-debited each cycle | Good | `/api/pay/restoreContract`, `/api/pay/uncontract` = stored mandate |
| Enterprise checkout | **Offline corporate bank transfer prepaid top-up only.** No card or invoice rail | Poor | User bears all liability for mis-credited funds |
| Error clarity | Kwai ships an issuer-decline taxonomy they map themselves (`bank_refused`, `card_high_risk`, `card_pay_limit`, `card_not_active`, `black_card`) | Good | ⚠️ agent-reported; did not reproduce in the chunks I pulled |

---

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|---|---|---|
| PCI DSS Level | **No public information found.** No attestation, AOC, or ESG/annual-report mention | — |
| Card data handling | `[INFERENCE, not confirmed]` — SAQ A / SAQ A-EP | See below |
| Recommended Yuno integration | **SDK** (hosted fields), to preserve the reduced scope they clearly want | — |

`[INFERENCE, not confirmed]`: both Kwai card rails use hosted-field/iframe tokenization (dLocal Smart Fields, Checkout.com Frames v2) and Kling uses Stripe Elements — the architecture a merchant picks to keep PAN out of its own environment and stay at SAQ A/A-EP. **Consistent with not holding, and not wanting, a Level 1 Service Provider attestation. Hypothesis, not a claim.**

---

## Section 10: Strategic Insights & Outreach Angles

> **Insight #1: They wrote the orchestration business case themselves, in their own build config**
> **Evidence:** §3A — five acquirers in one bundle with live dLocal and Checkout.com keys, plus a country-suffixed key `VUE_APP_CARD_PAY_KEY_EGY` + §4 — Visa implemented ×4, Pix ×3, Boleto ×3, Mastercard ×3, Amex ×3.
> **Pain Point:** Every new market means another acquirer contract, another SDK, another set of keys compiled into the frontend, and another implementation of rails they already support. Acquirer selection is a build-time constant — changing a route is a release, not a config change. Nobody can answer "which acquirer is converting best on Visa in Brazil this week" without a manual reconciliation across four ledgers.
> **Yuno Value Proposition:** One integration above the five they already run; routing per BIN, market and method; automatic failover when one degrades; one reconciliation surface. Additive — nothing gets ripped out.
> **Best Success Case:** A multi-market digital-goods merchant that already ran several regional acquirers and consolidated the routing without dropping any of them.
> **Outreach Angle:** *"Your recharge flow carries four separate Visa integrations and three separate Pix integrations. That's a deliberate multi-acquirer strategy — I'm curious how you decide which one a given transaction goes to."*
> **Suggested Subject Line:** Four Visa integrations on Kwai recharge

> **Insight #2: Overseas is shrinking while Kling compounds at 200%**
> **Evidence:** §6/§12 — overseas Q2 2026 revenue RMB 1,179m (−9.3% YoY), operating loss RMB 25m against a RMB 19m **profit** a year earlier; H1 2026 loss RMB 56m vs H1 2025 profit RMB 47m + **Kling AI Q2 2026 >RMB 850m, +200%+ YoY**.
> **Pain Point:** The overseas business reached profitability in Q1 2025 and gave it back. Every point of auth rate and every point of cost of acceptance is the difference between a profitable and a loss-making segment at these margins — overseas operating loss is RMB 25m on RMB 1,179m of revenue, i.e. **~2% of revenue**. Payment economics alone are that size.
> **Yuno Value Proposition:** At a ~2%-of-revenue swing point, routing to the best-performing acquirer per corridor and recovering failed authorisations is not an optimisation — it is the segment's P&L.
> **Best Success Case:** Match on "multi-acquirer merchant at thin segment margin", not on vertical.
> **Outreach Angle:** *"Your overseas segment went from a RMB 19m profit to a RMB 25m loss year on year, on revenue of RMB 1.2bn. That's a ~2% swing — roughly the size of the acceptance-cost and auth-rate line itself."*
> **Suggested Subject Line:** Overseas swung 2% of revenue

> **Insight #3: QRIS — a declared market with no local rail on the highest-frequency surface**
> **Evidence:** §4 — `IDN` is in the `web_country` recharge enum, but **zero QRIS occurrences across every Kwai wallet and Shop chunk**; the Indonesian wallets (GoPay/OVO/DANA/ShopeePay) ship only in the *Shop* bundle, not recharge + §2 — **no Indonesian legal entity anywhere in the group structure**.
> **Pain Point:** Coin top-up is the high-frequency, low-ticket, gifting-driven surface — exactly where a card-only flow leaks hardest, and exactly where Indonesia's under-banked base cannot pay. QRIS is at ~40m merchants and 57.6m users.
> **Yuno Value Proposition:** One integration adds QRIS and the virtual-account rails without a per-rail rebuild, and routes to a locally-licensed acquirer without standing up an Indonesian entity.
> **Best Success Case:** A content or gaming merchant that added QRIS and VA into an existing card-first checkout.
> **Outreach Angle:** *"Kwai Shop got GoPay, OVO, DANA and ShopeePay. Coin top-up didn't — and QRIS isn't on either."*
> **Suggested Subject Line:** QRIS missing on Kwai coin top-up

> **Insight #4: The contract clock — and a contractual duty to benchmark**
> **Evidence:** §6 — the 2023 Payment Services Framework Agreement **ends 2026-12-31**, with a clause requiring comparison against *"other comparable service providers"* and terms *"no less favorable than those offered by other independent third party service providers"* + §3A — nine-plus acquirers already in use, so a competitive payment process is normal practice here.
> **Pain Point:** A renewal decision is live now, and the board-level document says they must benchmark.
> **Yuno Value Proposition:** Yuno cannot serve China domestic — **be explicit about that, it buys credibility.** But the same benchmarking exercise is the natural moment to ask what the international stack should look like.
> **Best Success Case:** n/a — this is a timing hook, not a proof point.
> **Outreach Angle:** Use as the *reason for the call's timing*, never as the subject of the pitch.
> **Suggested Subject Line:** ⚠️ Do not put the contract in a subject line — it reads as surveillance. Use it in the body, once, as timing.

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks**
1. Your Kwai recharge flow carries four separate Visa integrations and three separate Pix integrations — one per acquirer.
2. Your overseas segment went from a RMB 19m operating profit to a RMB 25m loss year on year, on revenue of RMB 1.2bn.
3. Kwai Shop supports GoPay, OVO, DANA and ShopeePay in Indonesia; coin top-up supports none of them, and neither surface has QRIS.

**Cold call openers**
1. *"I spent some time in your recharge checkout — you're running five acquirers. I'm curious who decides which one a transaction goes to."*
2. *"Your overseas segment was profitable in Q1 2025 and is back in loss now. Is acceptance cost part of that conversation internally?"*
3. *"You've got a country-specific acquirer key for Egypt compiled into the frontend. Is that how routing works everywhere, or just there?"*

---

## Section 11: Similar Companies & Prospecting Pipeline

### 11A. Direct Competitors — short-video / live-commerce
| Company | Website | HQ | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---|---|---|---|---|---|---|
| ByteDance (Douyin/TikTok/TikTok Shop) | tiktok.com | Beijing | Private | **BR, ID, PK, SEA, Greater China** | **PIPO** — ByteDance's own global payment arm 🟡; Worldpay, Stripe (Tips), PayPal | [fxcintel](https://www.fxcintel.com/research/reports/tiktok-payments-processing-ecommerce-opportunities) |
| Xiaohongshu / RedNote | xiaohongshu.com | Shanghai | ~400m MAU | CN, HK/TW | **Acquired a PBOC licence Nov 2025** via Oriental Electronic Payment | [TechNode](https://technode.com/2025/11/06/xiaohongshu-acquires-china-payment-license-via-full-takeover-of-oriental-electronic-payment/) |
| Bilibili | bilibili.com | Shanghai | ~348m users | CN, HK/TW | Reported building its own payment system 🔴 | [daoinsights](https://daoinsights.com/news/bilibili-plans-to-launch-payment-system/) |
| Likee (BIGO/JOYY) | likee.video | Singapore | ~150m MAU | **SEA, South Asia — overlaps SnackVideo** | Not found | — |
| Instagram Reels (Meta) | instagram.com | US | — | **Brazil** | n/a in-house | [kr-asia](https://kr-asia.com/instagram-takes-on-tiktok-kwai-in-brazil-with-new-video-music-remix-feature) |
| Weibo | weibo.com | Beijing | ~587m users | CN | Not found | — |

⚠️ **Brazil user figures for Kwai vs TikTok are all 2019–2022 vintage. Do not quote them as current.**

### 11B. Industry Peers — AI video subscription (Kling's set)
Covered in `2-ready-to-outreach/kling-ai.md`. Headline: **Runway and Luma both run single-PSP Stripe**, verified verbatim from their own ToS; HeyGen names no PSP.

### 11C. Companies Recently Adopting Payment Orchestration
**"No public case studies found of direct competitors adopting payment orchestration."** Gr4vy, Spreedly and Primer customer lists were pulled directly — not one short-video, live-commerce or creator platform appears on any of them.

> 🚩 **Reject on sight:** the claim *"Netflix integrated UPI/GCash/Alipay through orchestration for +40% APAC subscriptions"* circulates widely. Its only source is a payments-vendor content-marketing page. No Netflix disclosure, filing or report exists. **It appears fabricated. Never use it.**

### 11D. Prospect Scoring & Top Pipeline
| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|---|---|---|---|---|---|---|---|
| 1 | **Kling AI** | Sub-property | Global, India #1 | 16/29 | 🟢 | Single-PSP Stripe, greenfield | ✅ own file |
| 2 | Likee (BIGO/JOYY) | Direct competitor | SEA, South Asia | ⬜ not scored | — | Same markets as SnackVideo, no PSP evidence found | ❌ **genuine find — not on the TAL** |
| 3 | Bilibili | Direct competitor | CN, HK/TW | ⬜ not scored | — | Reported building own payments | ❌ not on the TAL |
| 4 | Xiaohongshu | Direct competitor | CN, HK/TW | ⬜ not scored | — | Just bought a licence — insourcing | ❌ not on the TAL |

⚠️ Competitors were **not** scored against the 29-point matrix — the research did not gather per-company signals at that depth. Marking them ⬜ rather than inventing scores.

---

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|---|---|---|
| Annual Revenue (USD) | **RMB 142,776m ≈ US$19.8bn** (FY2025) | [FY2025 release](https://www.prnewswire.com/news-releases/kuaishou-technology-announces-fourth-quarter-and-full-year-2025-financial-results-302724627.html). ⚠️ TAL said "~$17B (FY24)" — FY2024 was RMB 126,898m, so the TAL figure was roughly right for FY2024 |
| **Addressable revenue (the number to size on)** | **Overseas RMB 5,074m + Kling ≈ RMB 3,400m annualised ≈ US$1.2bn** | Segment table + Kling Q2 2026 ×4 |
| GMV | **RMB 1,598.1bn** (FY2025, +15.0%) | FY2025 release. ⚠️ **Kuaishou stopped publishing absolute GMV in 2026** |
| Average Transaction Value | **Not disclosed** | — |
| Est. Annual Transactions | **Not derivable precisely** — ATV unpublished | — |
| **Monthly transaction count** | ✅ **DERIVED (bounded): >>100,000/month.** GMV RMB 1,598.1bn ÷ 12 = RMB 133bn/month. Even at an implausible ATV of RMB 10,000, that is **13.3m orders/month**. ⚠️ ATV is **not** sourced — this is a bound, not a measurement. **Billing unit: e-commerce orders only**; live-gifting and coin top-ups are additional and uncounted | Band ≥100,000 → **+5**, robust to any plausible ATV |
| Active Users | 410.2m DAU / 724.6m MAU (FY2025); 797.3m MAU (Q2 2026) | Results releases |
| Primary Currency | RMB domestically; **USD for Kling**; BRL, PKR, IDR, EGP, TRY overseas | Bundle enums + Kling Credits Policy |
| Top 3 Markets by Revenue | China (96.4% of FY2025) · Brazil · then the rest of overseas | Segment table |
| **Billing channel split (web vs app store)** | ⚠️ **NOT DISCLOSED — and this is the biggest hole in the business case.** Both `IOS_IAP` and `GOOGLE_IAP` are first-class providers in the Kwai recharge enum, and Kling bills through App Store, Google Play **and** web/Stripe. The orchestrable share is unknown | — |
| Payment channel fees (China) | Tencent: FY2021 RMB 896.2m · FY2022 1,009.5m · 9M2023 1,093.8m. Caps 2024 1,672.0m / 2025 1,792.0m / **2026 2,018.0m** | [HKEX CCT](https://www1.hkexnews.hk/listedco/listconews/sehk/2023/1121/2023112100578.pdf) |

---

## Overall Research Confidence

**HIGH on the payment stack. MEDIUM on traffic and entities. LOW on the billing-channel split.**

- **Payment stack — HIGH.** Five PSPs, live keys and rail redundancy were mined by me from production bundles with 404-body sanity checks, then independently corroborated by a second agent that found the same keys via a different chunk. The orchestrator classification rests on six converging lines of evidence.
- **Financials — HIGH.** Every figure was read by me in the company's own results announcements, with grep controls confirming the documents were complete.
- **Traffic — LOW, and deliberately sidelined.** **Estimate-grade only**; no MCP tools, no supplied dataset for these domains. Two vendors disagree 3× on rank and 46pp on China share, and per-country visit counts came back internally contradictory. The country profile is therefore driven by the *filings and the bundle market enums*, not by traffic. **This is why the APM analysis leans on `web_country` rather than SimilarWeb.**
- **Entities — MEDIUM.** The structure rests on a five-year-old draft prospectus because `ir.kuaishou.com` 403s.
- **Billing-channel split — LOW.** Undisclosed, and it materially bounds the business case.

---

## Manual Research Recommendations

> **Area:** Web vs app-store billing split, group-wide
> **Why it matters:** Both app stores are first-class providers in the recharge enum. If IAP dominates, the orchestrable share of Kwai and Kling revenue is far smaller than the headline. This is the single biggest unknown in the business case.
> **Suggested action:** Ask it in discovery, directly, in the first call.

> **Area:** Which acquirer actually takes a Brazilian card — dLocal or Checkout.com
> **Why it matters:** Both SDKs ship; the split is server-side. It is the one thing source-mining cannot settle, and it tells you whether real routing logic exists or just static config.
> **Suggested action:** Walk `pay.kwai.com/recharge` from a Brazilian IP with DevTools open.

> **Area:** Indonesia — whether the Shop wallets are live or shipped-dark
> **Why it matters:** The QRIS insight is the strongest rail gap on the account, and it rests on the recharge enum. If the Shop wallets are dark too, the gap is bigger; if QRIS quietly went live, the hook dies.
> **Suggested action:** VPN to Indonesia and open both Kwai Shop checkout and coin top-up.

> **Area:** Reclame Aqui complaint volume for Kwai Brazil
> **Why it matters:** Brazil is their largest overseas market and complaint volume there is completely unquantified — 403-blocked on both routes.
> **Suggested action:** Open reclameaqui.com.br/empresa/app-kwai in a normal browser.

> **Area:** Indonesian regulatory position
> **Why it matters:** No Indonesian entity exists anywhere in the group. If BI's PJP regime gates domestic acquiring, that escalates the Indonesia story from a rail gap to a regulatory gate — a much stronger argument.
> **Suggested action:** Verify the current BI PJP rules against a live source. **Do not cite from memory.**

> **Area:** DoD 1260H listing status
> **Why it matters:** Completeness of the compliance file. Not expected to block anything.
> **Suggested action:** Open regulations.gov docket DOD-2026-OS-1288, "Supporting & Related Material" tab.

---

## Appendix: All Source URLs

**Financials & filings:** [FY2025 results](https://www.prnewswire.com/news-releases/kuaishou-technology-announces-fourth-quarter-and-full-year-2025-financial-results-302724627.html) · [Q2/Interim 2026 results](https://www.prnewswire.com/news-releases/kuaishou-technology-announces-second-quarter-and-interim-2026-unaudited-financial-results-302855081.html) · [Q1 2026 results](https://www.prnewswire.com/news-releases/kuaishou-technology-announces-first-quarter-2026-unaudited-financial-results-302782888.html) · [HKEX prospectus](https://www1.hkexnews.hk/listedco/listconews/sehk/2021/0205/9616246/sehk21012400103.pdf) · [HKEX CCT / Tencent payment agreement](https://www1.hkexnews.hk/listedco/listconews/sehk/2023/1121/2023112100578.pdf)

**Payment stack (source code):** [chunk-common.b87d5fd3.js](https://s15-def.ap4r.com/kos/s101/nlav11312/kwai-wallet/static/js/chunk-common.b87d5fd3.js) · [diamond~recharge-index.d42e8c33.js](https://s15-def.ap4r.com/kos/s101/nlav11312/kwai-wallet/static/js/diamond~recharge-index.d42e8c33.js) · [recharge.39f207c8.js](https://s15-def.ap4r.com/kos/s101/nlav11312/kwai-wallet/static/js/recharge.39f207c8.js) · [kling.ai/docs/payment-policy](https://kling.ai/docs/payment-policy)

**China developer docs:** [open.kuaishou.com epay access](https://open.kuaishou.com/docs/develop/server/epay/access.html) · [prePay-new](https://open.kuaishou.com/docs/develop/server/epay/open-api-new/prePay-new.html)

**Licences:** [Jiemian on Payeco & Huarui Fuda](https://www.jiemian.com/article/11935020.html) · [The Paper — Huarui card shutdown](https://m.thepaper.cn/newsDetail_forward_31907598) · [NBD](https://www.nbd.com.cn/articles/2024-11-14/3645619.html) · [Payoneer 10-Q](https://www.sec.gov/Archives/edgar/data/1845815/000155837025010514/payo-20250630x10q.htm)

**Complaints & UX:** [Trustpilot klingai.com](https://www.trustpilot.com/review/klingai.com) · [note.com Japan walkthrough](https://note.com/yappyinsta/n/n01dd90acf143)

**Hiring:** [Kuaishou Workday portal](https://kwai.wd3.myworkdayjobs.com/Kuaishou_External)

**Indonesia QRIS prominence:** [Jakarta Globe](https://jakartaglobe.id/business/bi-qris-adoption-hits-40-million-merchants) · [Tempo](https://en.tempo.co/read/2036439/bi-qris-surpasses-57-million-users-expands-globally) · [Katadata](https://databoks.katadata.co.id/en/finance/statistics/6a2631bbc1a3f/the-number-of-qris-users-increased-74-in-the-q4-2025)

**India ban:** [MediaNama](https://www.medianama.com/2020/10/223-cdep-snack-video-kwai/) · [CyberPeace Corps](https://www.cyberpeacecorps.in/meity-bans-43-mobile-apps-including-ali-express-and-snack-video/)

</details>
