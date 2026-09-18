# Amorepacific

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 17 / 29 → ⭐ **High Priority** — earned on arithmetic, no override applied
**Industry:** Cosmetics manufacturer and brand owner (Sulwhasoo, Laneige, Innisfree, Etude, Hera, COSRX) · **HQ:** Seoul, South Korea · **Listed:** Amorepacific Corporation, KRX **090430** · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** **Greenfield** — and unusually so: **four separate payment estates with nothing shared between them.** Classification is affirmative, verified by me from three live payment-config endpoints.

---

> ## ⚠️ READ THIS BEFORE ANYTHING ELSE — this is a complexity account, not a volume account
>
> Amorepacific Corp turns over roughly **KRW 4.25tn (~US$3.1bn)**. **Almost none of it touches an Amorepacific checkout.** Their own 1Q26 IR deck defines the "Online" channel as third-party marketplaces, verbatim:
>
> > *"Online: … Posted sales in all major platforms (**Naver, Kakao, Coupang**, etc.)"*
>
> And overseas reads the same: *"Diversified brand portfolio in **Amazon**"*, *"entry into **Sephora**"*, *"sales of **Tmall** increased"*, *"**Qoo10** Megawari"*, *"**TikTok Shop**"*, *"major platforms (**Shopee**, Tiktok)"*. Add **Olive Young and Daiso** (wholesale), department-store concessions, and **travel retail at 17% of domestic business**. Every one of those checkouts belongs to somebody else.
>
> The **only** own-checkout mention in the whole deck: *"sales doubled for the **Global Amore Mall (direct-to-consumer platform)**"* — with no absolute figure and no base.
>
> **If a sequence opens with "you process billions", it is wrong and they will know it in one line.** The addressable estate is low single-digit percent of the top line. What makes this account real is the *shape* of that estate, not its size.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Amorepacific is Korea's largest cosmetics group, selling overwhelmingly through marketplaces, wholesale, department stores and duty free. Its own direct-to-consumer estate is small but **structurally fragmented into four completely independent payment stacks** — a Korean in-house mall on KG Inicis, Korean brand sites on Cafe24, a cross-border global mall on Shopify running PayPal and Eximbay, and per-brand Western Shopify stores each on their own Shopify Payments account.

**SimilarWeb total visits:** **Not obtained** — none supplied and no MCP tools. **Geography below comes from audited IR segment revenue instead, which is the better source anyway** (same approach the YesStyle file took).

### Markets — Amorepacific Corp, 1Q26, from their own IR deck
| Segment | 1Q26 (KRW bn) | Share | YoY |
|---|---|---|---|
| **Domestic** | 626.4 | **55.2%** | +8.5% |
| Americas | 174.7 | 15.4% | +11.2% |
| Other Asia (Japan, ASEAN, India) | 143.1 | 12.6% | +15.0% |
| Greater China | 114.9 | 10.1% | **−13.5%** |
| EMEA | 64.4 | 5.7% | +16.4% |
| **Overseas total** | **497.1** | **43.8%** | +5.8% |

FY2024 direction: **Americas +83%, and it "surpassed Greater China to become the group's largest global market by revenue for the first time"**; EMEA tripled; Greater China −27%.

### The four payment estates — verified by me, first-hand
| # | Estate | Platform | Payment stack |
|---|---|---|---|
| 1 | **amoremall.com** (Korea) | In-house | **KG Inicis** (escrow relationship proven from their own footer) |
| 2 | **laneige.com/kr** etc. (Korea brand sites) | **Cafe24** (`aplaneige.cafe24.com`) | **PG not established** — Cafe24 bundles Inicis/NICEPAY/Toss/KCP |
| 3 | **global.amoremall.com** (cross-border) | Shopify, `shopId 62092247178` | **PayPal + Eximbay.** Shopify Payments **off** |
| 4 | **us.laneige.com · us.sulwhasoo.com · us.innisfree.com · cosrx.com · jp.laneige.com · int.sulwhasoo.com** | Shopify, **one shop ID each** | **Shopify Payments + Shop Pay + Apple Pay + Google Pay + PayPal + Afterpay** |

### Orchestration status
**None detected — no orchestrator, no in-house layer, nothing shared.** Zero hits against Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY and Yuno — but the real evidence is structural and positive, not an absent search result. See 3B.

### Buying signals
- 🧩 **Four independent payment estates**, each with its own provider, its own reporting and its own reconciliation
- 🚀 **New market entries named in 1Q26: Brazil and South Africa** (cross-border), IOPE into the Americas, Aestura into Europe and Sephora
- 📈 **Americas now the largest overseas market**, +83% in FY2024, while **Greater China fell 13.5% YoY** and is under active *"offline channel rationalization"*
- 🛒 **COSRX consolidated** — another entirely separate Shopify estate absorbed into the group
- ❌ **No payment RFP, no payments hire, no orchestration vendor found**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Amorepacific` to draft the 12-touch sequence — **after reading the volume warning at the top of this file.***

**Instruction for whoever drafts it:** lead on **fragmentation**, never on volume. The observation that writes itself is the wallet asymmetry in 3C — it is their own configuration, it is machine-readable, and it is not arguable.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 17 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+3** | ⚠️ **NOT FOUND — ASSUMED ~50,000–150,000/month across all four estates combined.** `[ASSUMPTION — not researched.]` **Amorepacific publishes no order count, no DTC GMV, no AOV and no own-mall/marketplace split.** **Basis:** own-checkout revenue is bounded by part of the 22% "Travel Retail & Cross-border" slice of domestic (and travel retail alone is 17% of domestic, so cross-border is the smaller half) plus the Western and Japanese Shopify stores — call it low single-digit percent of KRW 4.25tn, so roughly US$60–150m at a beauty AOV of US$40–60. **Scored the 50k–100k band, deliberately one band below where the midpoint arithmetic lands**, because every input is inferred from disclosed *structure* rather than a published figure. **Deriving this from group revenue would be flatly wrong** — the overwhelming majority of that revenue never touches an Amorepacific checkout. An assumption cannot fire the under-40k gate and this one does not. |
| Orchestration status | **+4** | ✅ **None detected, and affirmatively so.** Three live payment-config endpoints return three independently-configured stacks; Korea runs two more on entirely different platforms. An orchestration layer would normalise them. Nothing does. |
| 3+ countries | **+3** | ✅ Korea, US, Japan, Greater China, EMEA, ASEAN, India — segment-reported. Plus Brazil and South Africa entering. |
| Multiple PSPs | **+3** | ✅ **Four named:** KG Inicis (Korea), Eximbay (cross-border), PayPal (cross-border + West), Shopify Payments (per-brand West/JP). A fifth is unidentified behind Cafe24. |
| Local rail or licensing gap in a top-3 market | **0** | ❌ **Honestly not met.** Korea is the #1 market at 55.2%, and the Korean rails that matter are **present** — KakaoPay, Naver Pay, card instalments (무이자 할부) and bank transfer (무통장입금) are all confirmed on amoremall.com. The wallet gap in 3C is real but it is an *asymmetry*, not an absent dominant rail. **Not awarding points for a gap that isn't there.** |
| Recent expansion | **+2** | ✅ **Brazil and South Africa** named as cross-border entries in the 1Q26 deck; IOPE launched in the Americas; Aestura entering Europe and Sephora. |
| Payment issues reported | **0** | ⬜ Not researched. No complaint corpus established. |
| Funding >$10M | **0** | ❌ KRX-listed. No round. |
| High traffic outside home | **+2** | ✅ **Domestic is 55.2% of revenue, below the 60% threshold**, with overseas at 43.8% and growing faster. ⚠️ **Basis is audited segment revenue, not traffic** — no traffic data exists for this account. The YesStyle file set the precedent for using audited revenue where it is the better source. |
| Competitor using orchestration | **0** | ❌ None confirmed. |
| Payment job postings | **0** | ⬜ None found. |

**Tier: 17 / 29 → ⭐ High Priority.** No analyst override applied.

> **The override was considered and rejected, in the downward direction.** The matrix allows scoring down when *"absolute volume is too small — a high percentage score on a company with negligible transaction volume is a false positive."* That is the obvious risk here, given the whole top of this file argues the addressable estate is a fraction of the headline. **But low single-digit percent of US$3.1bn is still roughly US$60–150m of own-checkout volume**, which is comparable to other accounts in this pipeline and is not negligible. So the score stands.
>
> **What must not happen is a volume-led pitch.** The score is earned on fragmentation, market count, provider count and expansion — not on size. Read the warning at the top of the file before drafting.

---

### Section 3B. Orchestrator check → **NONE DETECTED (affirmative)**

Verified by me on 2026-09-18 by fetching `/payments/config` on three of their live storefronts:

| Storefront | shopId | Apple Pay | Shop Pay | Google Pay | PayPal |
|---|---|---|---|---|---|
| **global.amoremall.com** | 62092247178 | `null` | `null` | `null` | ✅ present |
| **us.laneige.com** | 25501892660 | ✅ present | ✅ present | ✅ present | ✅ present |
| **us.sulwhasoo.com** | 24983994413 | ✅ present | ✅ present | ✅ present | ✅ present |

**Three different shop IDs, three independently-configured payment stacks.** `us.laneige.com` carries `applePayConfig.shopifyPaymentsEnabled = true` and a `googlePayConfig` whose `iframeSrc` points at `checkout.shopify.com/25501892660/...`, i.e. a direct Shopify binding, not an orchestrator-issued token. Add the in-house Korean mall on KG Inicis and the Cafe24-hosted Korean brand sites, and that is **five platforms and at least four providers with no shared layer, no shared vault and no shared reporting.**

### Section 3C. ⭐ The wallet asymmetry — found in their own config, and better than it first looks

`global.amoremall.com/payments/config` returns, verbatim:

```
"applePayConfig": null, "shopifyPayConfig": null, "googlePayConfig": null,
"amazonPayCv2Config": null,
"paypalConfig": { "merchantId": "4WTQVJTHH2X7N", "environment": "production", ... },
"dynamicCheckoutPrioritization": ["ApplePay","ShopifyPay","PayPal","AmazonPayCv2","GooglePay"]
```

**Read the last line against the first.** The storefront's own checkout prioritisation ranks **Apple Pay first and Shop Pay second — and both are `null`.** The configuration expresses an intent the merchant account cannot fulfil: it is set up to lead with wallets that are not enabled, so the flow falls through to PayPal.

**This is the cross-border mall.** It is the storefront serving Korea cross-border, China, Malaysia, Hong Kong, the Philippines, Indonesia and now Brazil and South Africa — presenting in **USD** — and it is the one estate with **no wallet at all**, while `us.laneige.com` and `us.sulwhasoo.com` carry Apple Pay, Google Pay and Shop Pay across six card networks (visa, masterCard, amex, discover, elo, jcb).

> **The one-sentence version for outreach:** *your US brand stores lead with Apple Pay, Google Pay and Shop Pay; your cross-border mall is configured to lead with Apple Pay and Shop Pay too, but neither is switched on.* Both halves come from their own endpoints. Neither is arguable.

### Section 4. Local payment methods — own checkouts only

**global.amoremall.com**, verbatim from their FAQ: *"All region Global Credit Card: VISA, Master, JCB, AMEX, Uionpay [sic] / **Korea:** Local Credit card issued in South Korea, **Kakao Pay, Naver Pay, Payco** / **China: Alipay, WeChat** / **Malaysia: FPX** / **Southeast Asia: Alipay+, DANA** (Indonesia), **Alipay HK**, **GCash** (Philippines), **Touch'n Go** (Malaysia)"*. Footer badges add **PayPal and Klarna**.

**amoremall.com (Korea):** KakaoPay, Naver Pay (`npay.amorepacificmall.com` resolves), **card instalments (무이자 할부)**, **bank transfer (무통장입금)** under KG Inicis escrow. **Payco confirmed cross-border but NOT on the Korean mall.** Apple Pay and Google Pay **not found** on either Korean or global mall.

**US/JP brand stores:** Visa, Mastercard, Amex, Discover, PayPal, Apple Pay, Google Pay, Shop Pay, **Afterpay**.

❌ **Samsung Pay not found anywhere.** ⚠️ **Toss** appears only as a cashback promotion on the Korean mall — treat as *inferred tender, not confirmed*, and do not assert Toss Payments as a PG.

### Source Notes
- ✅ **The three `/payments/config` endpoints were fetched and parsed by me today.** The wallet asymmetry, the shop IDs, the `dynamicCheckoutPrioritization` array and the USD currency on the global mall are all first-hand.
- ✅ **KG Inicis** proven from Amorepacific's own Korean footer escrow disclosure; **Eximbay + PayPal** proven from `global.amoremall.com/pages/faqs` (*"refund the product amount by PayPal or Eximbay(Payment Gateway)"*).
- ✅ **All IR figures come from Amorepacific's own fetched PDFs and press releases**, not from aggregators.
- 📌 **One correction to the agent report.** It stated `"shopifyPaymentsEnabled": true` as a top-level field on the US stores. It is not — it is **nested inside `applePayConfig`**. The claim is right, the location was wrong, and I verified the corrected version myself. Also: I could **not** confirm the reported `supports3DS` flag under `applePayConfig` — that key is absent in the current response, so **do not assert 3DS on these storefronts**.
- ⚠️ **The FY2025 Amorepacific Corp figures are reported in 억원 (KRW 100m)** and were rescaled to KRW 4.2528tn. Arithmetic cross-checks against FY2024 (3.8851tn × 1.09 ≈ 4.235tn). **Re-verify before quoting a revenue number in an email.**
- ⚠️ **The April-2025 "Amorepacific Holdings Corp." rename is aggregator-only and is contradicted** by the company's own Feb-2026 release headed *"Amorepacific Group 2025 Earnings Summary"*. **Do not use the Holdings name.**
- ❌ **"Over 40% of global sales from e-commerce" appeared in a search synthesis and could not be found in any IR document. Do not use it.** Even if true it counts marketplaces as e-commerce, so it would not support a DTC claim.
- ❌ **COSRX deal terms** (38.4% → ~93.2%, KRW 755.1bn, Oct 2023) are search-summary only. The **consolidation itself** is first-party confirmed via the IR PDFs.
- ❌ **No DTC revenue figure exists in any market, at any date.** This is the gap that decides how big the account really is.

### Manual Research Recommendations
> **1. Get a DTC revenue or order figure on the call.** Everything about sizing this account depends on it and nothing public answers it.
> **2. Establish the PG behind the Cafe24 Korean brand sites** — the one estate of five with no identified provider.
> **3. Ask why the global mall has no wallets** when the US stores lead with three. That question is the whole opening.
> **4. Confirm whether Amazon, Sephora, Tmall, Qoo10, TikTok Shop and Shopee volume is genuinely out of scope**, or whether any of it settles back through an Amorepacific entity.

---

## Executive Summary

Amorepacific is a KRW 4.25tn Korean cosmetics group whose revenue runs overwhelmingly through channels it does not own — **Naver, Kakao, Coupang, Olive Young, Amazon, Sephora, Tmall, Qoo10, TikTok Shop, Shopee**, department-store concessions and travel retail. Its own direct-to-consumer estate is small and completely undisclosed in size, but it is **fragmented into five platforms and at least four payment providers with nothing shared between them**: an in-house Korean mall on **KG Inicis**, Korean brand sites on **Cafe24**, a cross-border mall on Shopify running **PayPal and Eximbay**, and a set of Western and Japanese brand stores each on **its own separate Shopify Payments account**. I verified that fragmentation directly from three live payment-config endpoints, which also surfaced the sharpest observation in the file: **the cross-border mall is configured to lead checkout with Apple Pay and Shop Pay, and has both switched off**, while the US stores carry all three wallets. The motion is **greenfield** and the score is **17/29 ⭐** — but it is earned entirely on fragmentation, market count and expansion, **never on volume**, and any sequence that implies otherwise will not survive a reply.

</details>
