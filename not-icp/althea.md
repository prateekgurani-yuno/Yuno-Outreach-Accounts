# Althea

**Status:** 🔴 Not ICP — no transactable APAC volume (Phase 0 gate)
**ICP Score:** Not scored — rejected at the qualification gate before scoring was meaningful
**Industry:** K-beauty cross-border e-commerce · **HQ:** Seoul, South Korea — **Althea Inc.**, 213 Yeongdong-daero, Gangnam-gu · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** N/A — rejected

---

> ## ⛔ THE FINDING — three of four storefronts cannot take money, and I verified it myself
>
> Althea's surviving storefronts run on Shopify, which publishes each store's status at `/payments/config`. Fetched by me on 2026-09-18:
>
> | Storefront | `checkoutDisabled` | `/checkout` |
> |---|---|---|
> | **my.althea.kr** (Malaysia) | **`true`** | **HTTP 403** |
> | **ph.althea.kr** (Philippines) | **`true`** | — |
> | **sg.althea.kr** (Singapore) | **`true`** | — |
> | us.althea.kr (Althea Global) | `false` | live |
>
> **Malaysia, Philippines and Singapore are browse-only shopfronts that cannot process a payment.** Shopify sets that flag on frozen, paused or unpaid stores. The one storefront that still transacts ships to **the United States and South Korea only**.
>
> Indonesia, Thailand and Taiwan have been eliminated entirely — `id.`, `th.` and `tw.althea.kr` now 301 to the US store. `vn.`, `jp.`, `hk.`, `kr.` and `global.althea.kr` do not resolve. **The main domain `althea.kr` does not complete a TLS handshake.**

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Althea was a Korean K-beauty platform selling cross-border into Southeast Asia. It is legally alive and commercially dormant. There is no public shutdown announcement — the decay is visible only in infrastructure.

**Scale:** **FY2025 revenue KRW 2,040,000 (~US$1,500)**, dated 2025-12-31, filed via NICE 평가정보 and surfaced through Korean recruiting aggregators. **Two employees** enrolled in national employment insurance — the hard, government-sourced headcount figure. `[Third-party aggregator sourcing; the storefront evidence above is the stronger and independently verified basis for this rejection.]`

**Entity**, verbatim from the live Terms of Service: *"…services provided by **Althea Inc.** and its wholly owned subsidiaries, **Althea Beauty Sdn. Bhd.** and **Althea Beauty Pte. Ltd.**"* Governing law: Republic of Korea.

### Current payment stack — what is left of it
Parsed from the live US checkout: **Shopify Payments** (card acquiring, via `AnyStripeSharedTokenPaymentMethod`) plus **exactly one registered gateway — PayPal Express**, merchant ID `VM3XULMF6JSWU`, identical across all four storefronts. **Shop Pay disabled. Apple Pay, Google Pay and Amazon Pay all `null` on every store** — I confirmed those four nulls myself. Card brands displayed: Visa, Mastercard, PayPal.

### What they used to run — the genuinely interesting part
Historical evidence from archived paths, all affirmative:
- **Adyen** — `althea.kr/adyen/process/success`, captured **2019-03-03**. The only global-tier acquirer in their history.
- **MOLPay / Razer Merchant Services** (Malaysia) — `althea.kr/molpay/paymentmethod/redirect`, **2015-08-21**
- **DOKU** (Indonesia) — their own blog documents DOKU Wallet, DOKU OTC via Alfamart and DOKU ATM/internet-banking transfer
- **Paymentwall fronting GCash** (Philippines) — their own March 2021 post: *"Under the payment methods available, select **'SECURE PAYMENTS BY PAYMENTWALL'**"*
- Legacy platform was **Magento**; Malaysia was still a healthy Shopify store as recently as **June 2025**

> 📌 **Worth recording as a segment datapoint:** Althea once ran exactly the fragmented multi-gateway, multi-rail estate Yuno sells into — Adyen plus MOLPay plus DOKU plus Paymentwall across five-plus markets. **They resolved it by shrinking, not by orchestrating.** That says something about this segment. It says nothing that makes this a sellable account.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

## Rejection Rationale

**Rejected at the Phase 0 qualification gate: no transactable APAC payment volume.** Three of Althea's four surviving storefronts — Malaysia, Philippines and Singapore — return `checkoutDisabled: true` from Shopify's own configuration endpoint, and Malaysia's `/checkout` returns HTTP 403. **I verified all four endpoints and the 403 directly.** Indonesia, Thailand, Taiwan, Vietnam, Japan and Hong Kong storefronts no longer exist, and the Korean domain does not complete a TLS handshake. The single live store ships to the US and Korea only, carries one gateway (PayPal) plus Shopify Payments, and has Shop Pay and all three wallets disabled. Corroborating but not load-bearing: **FY2025 revenue of KRW 2.04m (~US$1,500)** and **two employees on national employment insurance**.

There is no orchestration pain here because there is no volume, and there is no APAC presence left to orchestrate.

> **Revisit only if** a relaunch is announced or the SEA storefronts return to `checkoutDisabled: false`. The `/payments/config` check is a ten-second test and would settle it.

### Source Notes
- ✅ **All four `/payments/config` endpoints and the Malaysian `/checkout` 403 were fetched and verified by me** on 2026-09-18. This is the basis of the rejection.
- ✅ **Operating entity verbatim** from `https://us.althea.kr/policies/terms-of-service`.
- ⚠️ **Korean financial and headcount data comes from recruiting aggregators republishing NICE 평가정보**, not from a registry I read directly. Treated as corroborating, not decisive.
- ⚠️ **Two conflicting CEO names** across aggregators (강대업 / 신크리스토퍼성윤) and two irreconcilable revenue figures (KRW 2.04m dated 2025-12-31 vs an undated KRW 4.607bn). The dated figure is the current one; the undated one is clearly peak-era. **Unresolved, and it does not change the rejection.**
- ❌ **The "Goldman Sachs-backed" premise in the research brief could NOT be verified and must not be used.** The one article that might support it was unreachable across three attempts. Aggregator summaries name Tekton Ventures, FirstFloor Capital, Korea Development Bank, Bon Angels and 500 Startups — not Goldman.
- ❌ **No shutdown, pivot or acquisition announcement exists** in English or Korean. Checked every storefront DOM for closure banners — nothing.
- ⚠️ **Substring false positives caught and cleared:** raw greps returned `omise` 20+ times (from *"Althea Pr**omise**s"*) and `boost` 20+ times (from `boost_mobile.png` and a "booster" product tag). **Omise is not present.** Adds to the running list alongside `payme` inside "pay**me**nt" and `ppro` inside "Ina**ppro**priate".
- ⚠️ **Dead advertising:** `my.althea.kr` still serves FPX, Touch 'n Go, Boost and GrabPay footer icons for rails that cannot be reached, and the live US FAQ still claims *"Yes, we ship all over the world"* while the checkout offers 64 destinations, all of them US states, US territories or South Korea.
- ❌ **Not established:** the exact date SEA checkout was disabled (bracketed between 2025-06-03 and today), which CEO is current, and what `in.althea.kr` — serving apparel in 2020 — was.

### TAL correction — `accounts/apac-tal.csv`
| Column | Current | Should be |
|---|---|---|
| `INFO` | *"selling K-beauty brands cross-border to Southeast Asian shoppers, priced and paid in local currencies"* | ❌ **Refuted.** No Southeast Asian storefront can process a payment. Indonesia, Thailand, Taiwan and Vietnam are gone; Malaysia, Philippines and Singapore have checkout disabled. |
| `Est. Revenue (USD)` | `~$30M est.` | ❌ **Refuted.** FY2025 filed revenue ~US$1,500. |
| `WEBSITE` | `althea.kr` | Dead — does not complete a TLS handshake. Only `us.althea.kr` transacts. |

</details>
