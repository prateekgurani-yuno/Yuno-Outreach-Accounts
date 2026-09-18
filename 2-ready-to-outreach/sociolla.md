# Sociolla

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 13 / 29 → 🟢 **Medium**
**Industry:** Beauty retail, omnichannel (e-commerce + 150 physical stores + SOCO app) · **HQ:** Jakarta Barat, Indonesia — **PT Social Bella Indonesia** · **Owner:** **General Atlantic, 54% since 23 Dec 2025** · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** **In-house layer** — a dedicated first-party payments microservice, verified live in June 2026. Respect the build; anchor on opportunity cost and reach, never "you need orchestration".

---

> ## 🎯 THE HOOK — a new majority owner, a hand-built payments service, and cards declining that work elsewhere
>
> **They built their own payments layer.** From Sociolla's own homepage source, captured June 2026 and **verified by me**, the site declares a microservice estate:
>
> `payments-api.sociolla.com` · `carts-api` · `orders-api` · `shipping-api` · `catalog-api1…5` · `soco-api` · `sso-broker.sociolla.com`
>
> **A separately-deployed payments service that has survived at least two front-end rewrites** — a home-grown abstraction sitting over Midtrans, a direct BCA integration, Kredivo and Vospay.
>
> **And it is visibly straining.** From the Apple App Store, Indonesian storefront, **22 June 2026**, one star, verbatim:
>
> > *"payment pke CC bolak balik gk bs, cb pke cc lain gk bs. **pdhl di app lain aman aja**"*
> > — *"Card payment fails over and over. I tried a different card, that fails too. Yet it works fine on other apps."*
>
> **Two different cards declining on Sociolla while working elsewhere is not a customer problem.** That is the exact failure mode a second acquirer and retry routing exist to fix.
>
> **The timing:** **General Atlantic took 54% on 23 December 2025.** New majority owner, nine months in, with a 500-store ASEAN expansion plan.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Sociolla is Indonesia's largest beauty retailer, operating sociolla.com, the SOCO app and **150 physical stores across Indonesia**, plus a Vietnamese storefront. Founded 2014, backed by Temasek, East Ventures, Jungle Ventures and L Catterton, and majority-acquired by **General Atlantic in December 2025**.

**SimilarWeb total visits:** **Not obtained.** `sociolla.com` is behind CloudFront/WAF (403) and no data was supplied. ecdb puts **97% of revenue in Indonesia** — the only geographic split available.

### Markets
| Market | Status | Evidence |
|---|---|---|
| **Indonesia** | ✅ Primary — 150 stores, ~45+ cities, 97% of revenue | Nikkei Asia; ecdb |
| **Vietnam** | ✅ Live — `vn.sociolla.com` crawled 2026-06-17 | Wayback CDX |
| Thailand, Philippines, Malaysia, Singapore | 🎯 Stated targets | `[UNVERIFIED — search summary only]` |

*The 2025 site revamp ships a country switcher with exactly two flags, `flag-id.svg` and `flag-vn.svg`. **No third market on the web front-end.***

### Known PSPs
- **Midtrans / Veritrans** — ✅ **confirmed from their own page source.** `api.midtrans.com/v2/token` and the Midtrans tokenisation JS both embedded, plus `veritrans.png` / `midtrans.png` on their own checkout and a `/veritrans-payment` callback route
- **BCA KlikPay** — ✅ **confirmed, and it is a direct bank integration, not a gateway passthrough.** Five dedicated routes: `klikpay-inquiry`, `klikpay-payment`, `klikpay-payment-flag`, `klikpay-validation`, `klikpay-thankyou`
- **Kredivo** (BNPL) — ✅ dedicated routes live to Jan 2025
- **Vospay** (cicilan/instalments) — ✅ dedicated route live to Apr 2024
- ❌ **Not found:** Xendit, DOKU, Faspay, iPay88, 2C2P, Espay, NicePay, Winpay, Durianpay, Stripe, Adyen, Checkout.com

### Orchestration status
**In-house layer.** Affirmatively evidenced by `payments-api.sociolla.com` as a distinct microservice, current June 2026. **No third-party orchestrator detected** — zero hits for Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY and Yuno, though that half is an absence of search hits rather than affirmative proof.

### Buying signals
- 💰 **General Atlantic acquired 54%, 23 December 2025** — new majority owner, reportedly ~US$250m mostly secondary with a ~$10m primary injection
- 🚀 **From 2 stores in 2019 to 150 today**, targeting **500** and naming Thailand, Philippines, Malaysia and Singapore as next markets
- 🔴 **Dated payment failures in 2026 app reviews** — see Section 5
- 🧾 **A hand-reconciled bank-transfer rail may still run:** their T&C requires *"pembeli memberikan konfirmasi pembayaran melalui e-mail ke cs@sociolla.com"* — the buyer emails proof of payment — and a 2026 review still complains of *"2 days payment confirmation"*
- 💼 **Backend engineering roles open (PHP)** — the legacy PrestaShop stack is still being maintained alongside the microservices. **No payments-specific role found**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Sociolla` to draft the 12-touch sequence.*

**Instruction for whoever drafts it:** the motion is **In-house**. They built `payments-api` deliberately and it works. Anchor on **reach and opportunity cost** — 150 stores, two countries, four ASEAN markets on the roadmap, each new rail a build against their own service. **Never suggest the build was a mistake.**

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 13 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+3** | ⚠️ **NOT FOUND — ASSUMED ~50,000–100,000 online transactions/month.** `[ASSUMPTION — not researched.]` **No order count, GMV or AOV is published.** **Billing unit counted: online transactions only** — the 150 physical stores generate card-present volume that orchestration does not address, so counting them would overstate the addressable number. **Basis:** 1M+ SOCO app downloads, 150 stores in ~45 cities, a ~US$595m valuation at the General Atlantic deal. ⚠️ **ecdb's US$6m 2025 web revenue figure is rejected** — it is implausible for a 150-store omnichannel retailer valued near US$600m and is almost certainly a model of the .com web shop alone. **I have not built a derivation on it.** Scored conservatively; an assumption cannot fire the under-40k gate. |
| Orchestration status | **+1** | ✅ **In-house layer, affirmatively evidenced.** `payments-api.sociolla.com` is a distinct deployed service alongside carts, orders, shipping and catalog APIs, still present in the June 2026 capture. |
| 3+ countries | **0** | ❌ **Genuinely not met — this is a two-market business.** Indonesia and Vietnam, and their own country switcher carries exactly two flags. Entities: PT Social Bella Indonesia is confirmed; PT Sociolla Ritel Indonesia and a Singapore holdco are both unverified, so the 3-entity route does not clear either. |
| Multiple PSPs | **+3** | ✅ **Midtrans/Veritrans confirmed from their own page source**, plus a **direct BCA KlikPay integration** with its own five-route inquiry/validation/callback set, plus Kredivo and Vospay. |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **Not scorable, and this is the most consequential gap in the file. QRIS is NOT FOUND — but the last readable payment inventory is 2019–2020**, and the site went to a Vue SPA afterwards, so archived captures return only a 27.8KB shell. QRIS became near-universal in Indonesian retail *after* that inventory. **That is unchecked absence, not sourced absence, and the matrix requires a source.** Same for DANA, ShopeePay and Alfamart OTC. **Do not claim any of these are missing.** |
| Recent expansion | **+2** | ✅ **2 stores in 2019 → 150 today** (Nikkei), targeting 500, with Thailand, Philippines, Malaysia and Singapore named. Vietnam live. |
| Payment issues reported | **+2** | ✅ **Dated, specific, and from the Apple RSS reviews API** — two cards declining while working on other apps (2026-06-22), checkout failing twice with voucher and gift-with-purchase lost (2026-06-03), funds held on a sold-out item with no self-serve refund (2026-09-10). Moderate frequency. ⚠️ **Counterpoint kept on the record:** a 5★ from 2026-07-30 says *"metode pembayaran nya pun mudah"* — payment methods are easy. It is not uniformly bad. |
| Funding >$10M | **+2** | ✅ **General Atlantic took 54% on 23 December 2025** — within 12 months. ⚠️ Mostly a **secondary** purchase with a reported ~$10m primary, so it is a control transaction rather than a growth round. Scored on the capital event and the new owner's mandate. Deal specifics beyond "General Atlantic, 54%, Indonesia" are `[UNVERIFIED — search summary only]`. |
| High traffic outside home | **0** | ❌ Not met. ecdb puts **97% of revenue in Indonesia**. Home-dominant by any measure. |
| Competitor using orchestration | **0** | ❌ None confirmed. |
| Payment job postings | **0** | ⬜ Backend PHP, front-end, PM and design roles found. **No payments-specific role naming a provider.** |

**Tier: 13 / 29 → 🟢 Medium.** No analyst override applied.

> **Why not higher, and why that is the right answer.** Two rows that would lift this are genuinely blocked rather than absent. **QRIS is the big one** — if Sociolla does not run QRIS end-to-end across web, app and 150 stores, that is a +3 row and a much sharper pitch; if they do, the rail argument collapses and the account becomes a pure reach-and-reconciliation story. **Nobody can tell from outside**, because the live site is WAF'd and the archive stops at an SPA shell. And the two-market footprint is a real structural limit, not a research gap.

---

### ⚠️ The strangest finding, and the sharpest one if it still holds

**Vietnam appears to have launched on a copy of the Indonesian checkout.** `vn.sociolla.com` carries `veritrans-payment`, the five `klikpay-*` routes, `faq-kredivo`, `kredivo-notification`, `kredivo-success` and `vospay-transaction-success` — **Midtrans, BCA KlikPay, Kredivo and Vospay are all Indonesian rails**, and all four have routes on the Vietnamese storefront (captured 2022-06-27).

Meanwhile **MoMo, ZaloPay, VNPay and VietQR are all NOT FOUND** for Vietnam.

> **If that is still true in 2026, it is the best observation in this file:** a Vietnamese storefront running Indonesian payment rails, with none of Vietnam's dominant wallets. **But the evidence is from 2022 and the current state is unverified** — the VN site is an SPA shell in every later capture. **Treat as a question to ask, not a claim to make.** Confirming it is the single highest-value manual action on this account.

---

### Section 4. Local payment methods — Indonesia

**⚠️ Read the vintage caveat first.** The last **server-rendered** payment inventory is **2019–2020**. Post-2020 the site is a Vue SPA and archived captures return a 27.8KB shell with no payment content. **"Not found" below usually means "not visible in the last readable inventory", not "absent today".**

**CONFIRMED** from their own `/how-to-pay` tab list and footer icon set: **Bank transfer / VA (BCA, Mandiri, BNI, BRI, Permata, CIMB Clicks, Panin, UOB, digibank, Niaga) · Credit & debit cards (Visa, Mastercard, JCB, American Express) · Indomaret OTC cash · OVO · GoPay · LinkAja (+ legacy TCASH) · Kredivo · Vospay · COD · in-store cash · card instalments (cicilan)**.

**NOT FOUND — and explicitly unchecked, not sourced-absent: QRIS · DANA · ShopeePay · Alfamart OTC · Akulaku · Atome · Indodana.**

*One corroborating signal: a 2026 Play review complains that after topping up OVO the system would not let them change payment method — so **OVO is live today**, which is useful because it dates at least one rail past the 2020 inventory.*

### Section 5. Payment issues

| Date | Rating | Issue | Source |
|---|---|---|---|
| **2026-06-22** | 1★ | **Two different cards declined; both work on other apps** | Apple RSS, Indonesian storefront |
| **2026-06-03** | 3★ | Checkout failed twice; voucher and gift-with-purchase lost; promo amount changed between views | Apple RSS |
| **2026-09-10** | 1★ | Money held on a sold-out item, no refund request path, bot-only CS | Apple RSS |
| undated | — | OVO topped up, then payment method could not be changed | Google Play |
| undated | — | Partial cancellation refunded manually by email | Google Play |
| **2026-07-30** | 5★ | *"metode pembayaran nya pun mudah"* — counterpoint | Apple RSS |

> **Pattern → opportunity.** The card decline is the one that matters: **two cards failing on Sociolla while working elsewhere points at acquirer or auth routing, not at the shopper.** With a single card gateway and an in-house layer above it, there is no second rail for a declined card to fall to. The voucher-lost-on-failed-checkout complaint is the same event seen from the promo engine's side.

### Source Notes
- ✅ **`payments-api.sociolla.com` verified by me** in the 2026-06-08 Wayback capture, alongside `carts-api`, `orders-api`, `shipping-api`, `catalog-api1–5`, `soco-api`, `bj-public-api` and `sso-broker`. This is the basis of the In-house classification.
- ✅ **Midtrans confirmed from Sociolla's own page source** — `api.midtrans.com/v2/token` plus the tokenisation JS. 📌 Note the sloppiness worth knowing about: the **sandbox** JS (`api.sandbox.midtrans.com`) shipped on a production page next to the **production** token endpoint.
- ✅ **PT Social Bella Indonesia** confirmed verbatim in their own Indonesian T&C and site footer, with the Jakarta Barat address.
- ✅ **App review quotes pulled from the Apple RSS customer-reviews API** for the Indonesian storefront — dated and specific, not scraped summaries.
- ⚠️ **The live site, `soco.id` and `payments-api.sociolla.com` all return 403** (CloudFront/WAF). **Their Zendesk does not exist** — `sociolla.zendesk.com`, `socialbella.zendesk.com` and `soco.zendesk.com` all 404 on the help-centre API, and `help.sociolla.com` does not resolve. **That route is dead; do not retry it on this account.**
- ⚠️ **Entity ambiguity unresolved:** ecdb names **PT Sociolla Ritel Indonesia** as the sociolla.com operator, which differs from the PT Social Bella Indonesia on the T&C. A Singapore holdco is also referenced. **Verify before any contract-stage conversation.**
- ❌ **ecdb's US$6m 2025 revenue is rejected as implausible** for a 150-store retailer valued near US$600m. Not used in any derivation.
- ⚠️ **Total raised is contested** — Dealroom gives a $100–500m band; other sources say $220m or $226m. **Do not quote a single number.** Temasek, East Ventures, Jungle Ventures and L Catterton as investors are corroborated.
- ⚠️ **General Atlantic deal specifics** beyond "General Atlantic, 54%, Indonesia, 23 Dec 2025" are search-summary only — the ~$250m value, the secondary/primary split, the Pavilion and L Catterton exits and the ~$595m valuation all `[UNVERIFIED]`. Primary sources are paywalled or removed.
- ❌ **Vietnam payment methods: nothing established.** The Indonesian-rail routes on `vn.sociolla.com` are a strong 2022 lead, not a 2026 conclusion.

### Manual Research Recommendations
> **1. Settle QRIS.** Does Sociolla run QRIS end-to-end across web, app and 150 stores, and who acquires it? This one answer swings the pitch and a +3 ICP row. Nothing public can answer it.
> **2. Confirm whether Vietnam still runs Indonesian rails.** If it does, that is the opening line.
> **3. Confirm Midtrans is still the gateway in 2026.** Last direct evidence is 2019 page source; last indirect is a 2022 route.
> **4. Establish whether the email-proof-of-payment bank transfer flow still runs.** A 2026 review mentioning "2 days payment confirmation" suggests it might.
> **5. Resolve the contracting entity** — PT Social Bella Indonesia vs PT Sociolla Ritel Indonesia vs the Singapore holdco.

---

## Executive Summary

Sociolla is Indonesia's largest beauty retailer — **150 stores, the SOCO app with 1M+ downloads, sociolla.com and a Vietnamese storefront** — majority-acquired by **General Atlantic in December 2025** and targeting 500 stores across ASEAN. It runs an **in-house payments layer**, `payments-api.sociolla.com`, verified as a live distinct microservice in June 2026, sitting over **Midtrans**, a **direct BCA KlikPay integration** with its own five-route callback set, **Kredivo** and **Vospay**. The motion is therefore **In-house**, and the pitch is reach and opportunity cost rather than the case for orchestration itself. The sharpest evidence is a dated 2026 app review reporting **two different cards declining on Sociolla while working on other apps** — a single-acquirer failure mode with no second rail to fall to. **Two things are genuinely unknowable from outside and both matter: whether QRIS runs end-to-end, and whether Vietnam is still running Indonesian payment rails.** Either answer materially changes the account, and the score of 13/29 reflects that uncertainty honestly rather than guessing past it.

</details>
