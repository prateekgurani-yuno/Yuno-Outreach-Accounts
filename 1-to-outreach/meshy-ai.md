# Meshy AI

**Website:** meshy.ai · **Industry:** AI 3D asset generation (consumer + API + physical goods) · **HQ:** ⚠️ **disputed — see below**
**Priority:** P1 · **Added:** 2026-10-14

> ## ⛔ HELD AT PHASE 0 — TERRITORY. Needs Prateek's ruling before Phase 2 runs.
>
> **The APAC-HQ premise this account was handed to me under does not survive their own
> legal pages.** The contracting and billing entity is **Meshy LLC, Murphy Square, 111 West
> Evelyn Avenue, Suite 304, Sunnyvale, CA 94086** — governing law **State of California**,
> arbitration seated in **San Francisco County**.
>
> I verified this personally rather than taking the research agent's word for it, and the
> decisive detail is that **the Chinese-language property serves the same US terms**:
>
> | Token | `www.meshy.ai/terms-of-use` | `meshy.cn/terms-of-use` | nonsense control |
> |---|---|---|---|
> | `Meshy LLC` | **5** | **5** | 0 |
> | `Sunnyvale` | **13** | **13** | 0 |
> | `San Francisco County` | **1** | **1** | 0 |
>
> Controls: `/terms-of-use-zzz-nonsense-9183` → real 404 at 5,863 B against 236,375 B and
> 245,009 B for the live pages, so the zeros are real zeros, not soft-404s.
>
> **But it is not a US-native company and the APAC operations are real,** which is why this
> is a judgement call and not an auto-reject:
>
> - Founded **Beijing, February 2021**, trading as **太极图形 / Taichi Graphics**.
> - **`taichi-graphics.com` now 301s to `meshy.cn`** — byte-identical, 334,623 B both. The old
>   China company's domain serves the China property.
> - `meshy.cn` carries a **Beijing ICP filing, 京ICP备2021025803号-9**, plus Beijing
>   public-security filing `11010802049972`. An ICP filing legally requires a PRC-registered
>   entity.
> - Offices/hiring across **Beijing, Shanghai, Shenzhen, Singapore, Tokyo** alongside the two
>   California addresses.
> - Probable PRC entity **北京太琦图形科技有限公司** (Beijing Taiqi Graphics, Haidian,
>   incorporated 2021-02-25, legal rep 胡渊鸣) — registry record is sourced, but the link to
>   `meshy.cn` is **[INFERENCE, not confirmed]**: the MIIT ICP registrant lookup returned 403.
>
> **The CLAUDE.md test is HQ, and on HQ this reads United States → AMER/EMEA, not APAC.**
> It is *not* the clean "west of Dubai with no APAC operations" auto-reject, because the APAC
> operations are substantial. **Prateek decides. I have not spent Phase 2 on it.**

## Notes

### Why it would be a strong account if the territory call goes our way

**The payments story is unusually good, and I verified all of it against passing controls.**

**1. A PRC-filed property that prices entirely in US dollars.** `meshy.cn/pricing` carries
**7 of 7 `priceCurrency` values as `USD`** — and **zero** CNY, **zero** RMB, **zero** ¥/￥
glyphs, against 594 dollar signs. A Beijing-ICP-filed, Chinese-language site billing in
dollars through a Delaware-or-California LLC. Both halves are theirs and neither is disputable.

**2. Two parallel processors, and they documented the second one's degradation themselves.**
Stripe and PayPal run side by side — but the PayPal path is functionally second-class, in
their own UI strings (each at 1 occurrence, control 0):

| String | What it concedes |
|---|---|
| `PayWithStripe` / `PromoStripeOnly` | **Promotions work on Stripe only** |
| `PayPalNoDiscount` | *"Discounts cannot be used with PayPal — please use another payment method to get the discount"* |
| `PaypalTaxDisabledTitle` | tax handling disabled on the PayPal path |
| `PaypalDisabledTitle` / `PaypalBlocked` | the path gets switched off |
| `PayPalFullPriceNote` | PayPal customers pay list price |
| — | *"PayPal subscriptions cannot be auto-upgraded to Studio. Please cancel your PayPal plan."* |

Given they discount **up to 70%** (`Meshy 3rd Anniversary - Up to 70% OFF`, `New User Offer -
50% OFF Pro Monthly`), "promotions are Stripe-only" means **a PayPal customer cannot buy at
the price the business actually sells at.** That is a conversion asymmetry inside their own
stack, not an external benchmark.

**3. The method ladder is Stripe's catalogue, not a built ladder.** Verbatim from the
`PaymentCanceledDialog.Retry.Method` enum on both properties — Alipay, Amazon Pay, Apple Pay,
Bancontact, Card, Cash App Pay, EPS, Google Pay, iDEAL, Kakao Pay, Klarna, **Korean Local
Card**, Link, Naver Pay, Przelewy24, PAYCO, Pix, **UPI**, US Bank Account (ACH), WeChat Pay.
`Link` and `Cash App Pay` are Stripe's own products, which is what identifies the set.

⚠️ **Do not re-derive UPI/Pix from a raw grep.** Case-insensitive `upi` returns 21 on the
pricing page but **5 of those are `Jupiter`**; `pix` returns 19 of which **14 are `pixel`**.
The real evidence is the escaped enum key — `\"Upi\"` = 1, `\"Pix\"` = 2. Site does **not**
bundle Font Awesome (0 on pricing and terms), so vendor greps here are otherwise trustworthy.

**4. Volume clears the 40k gate with margin.** **$100M+ ARR** self-reported 2026-09-30
(SOURCED, unaudited run-rate) → ~$8.33M/month. Against the **highest** list price of $100/mo
Ultra, that is a hard arithmetic floor of **~83,000 charges/month** — 2.1× the gate — and the
ladder is built for individual creators at $20–$40, so the real figure is far higher.
**DERIVED** (inputs: sourced ARR + sourced price ladder). Credit packs and physical-goods
orders are additional transaction streams on top. Paid-subscriber count is **not public** —
no public information found, and I have not substituted an assumption.

**5. A second, physical transaction stream.** "Creative Lab" / "Meshy Shop" ship customised
products to **24 named countries** with shipping addresses and shipping coupons — a
physical-commerce flow alongside the subscription flow.

### Funding
- Series A **Feb 2022, USD 50M** — Source Code Capital, GGV, BAI, Sequoia China.
- **Series B announced 2026-07-21, ~USD 400M at a USD 1.5bn post-money** — IDG Capital,
  Matrix Partners China, Monolith. **Well above the $10M scoring threshold.**
- ⚠️ **No SEC Form D on file.** Company search returned 0 CIKs and full-text search 0 hits,
  with a **passing control** (`company=stripe` → 10 CIKs). A genuine zero. Consistent with an
  offshore holdco as issuer, which would also bear on the HQ question — **[INFERENCE, not
  confirmed]**.
- >15M registered users and >100M models generated (Sept 2026, self-reported). >3,000
  business/institutional customers (self-reported).

### Open items if this is cleared to proceed
- MIIT ICP registrant for 京ICP备2021025803号 — 403, so the Beijing Taiqi link stays inference.
- California SoS BizFile — 429, so formation state and date unconfirmed.
- Credit-pack price ladder — behind login; recoverable from the authenticated checkout chunks.
- Regional price variance: `/nl/pricing` reportedly lists Studio at $60 vs $70 on `/pricing`
  — **[UNVERIFIED — search summary only]**, worth two minutes.
- The 118 non-US traffic markets. The supplied screenshot gave US 11.95% / 119 countries /
  mostly growing, and the per-country table did not survive compaction.

**No credential, API key, token or merchant ID was transcribed from any asset examined.**
