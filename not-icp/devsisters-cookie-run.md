# Devsisters (Cookie Run)

**Status:** 🔴 **Not ICP — analyst override.** The app-store trap fires, confirmed in the merchant's own words.
**ICP Score:** 17 / 29 on the matrix — **overridden.** The matrix score is real and is recorded below so the trade-off is visible, but it is computed over a channel that carries ~1% of the company's transactions.
**Industry:** Mobile game developer/publisher — Cookie Run series · **HQ:** Seoul, South Korea — **Devsisters Corp. (KOSDAQ: 194480)** · **Researched:** 2026-09-20
**Motion:** n/a — rejected.

---

> ## 🚫 THE REJECTION — Devsisters says it in writing on its own help centre
>
> **Verified first-hand** via the Zendesk help-centre API (`cs-cookierunkingdom.devsisters.com/api/v2/help_center/en-us/articles.json`, 35 articles pulled 2026-09-20), article *"Who processes in-app purchases?"*, verbatim:
>
> > *"Here at Devsisters, **we neither process in-app purchases, nor have access to your credit card information. All purchases are processed by Apple and Google Play.** They also manage your personal information."*
>
> And *"I didn't get an item I purchased!"*: *"**All purchases are processed by Apple and Google.**"*
> And *"Rules on in-app purchases and cancellations"*: *"**We cannot access your in-app purchase records and billing information.** Therefore, please contact Apple for iOS devices and Google for Android devices for refunds."*
>
> **This is `.claude/reference/subscription-payments.md` §4 — the app-store trap — in its purest documented form.** The merchant is not the merchant of record. There is no card rail to route, no approval rate to lift, no local method to add. A sequence built on any of those would not survive the first reply.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

### The corroboration — three independent sources, same answer

**1. The audited filing.** DART FY2025 사업보고서 §II-4 (판매경로 및 판매방법): *"당사 및 당사의 종속회사에서 개발한 게임을 자체적으로 퍼블리싱하여, **글로벌 마켓(구글 플레이스토어, 애플 앱스토어 등)에 직접 공급**하고 있습니다… 게임 부문의 매출은 당사 전체 매출의 약 **94.25%**를 차지하고 있습니다."* **No 자체 플랫폼 / own-platform revenue line exists anywhere in the filing.** `[Agent-sourced from DART — I did not re-pull the filing; the help-centre quotes above, which I did verify, carry the rejection on their own.]`

**2. The commission ratio.** 지급수수료 (fees paid) was **KRW 105.05bn in FY2025 = 38.2% of game revenue** (FY2024: 36.6%). A ~30% store take plus other service fees is the only plausible decomposition. `[INFERENCE — the filing gives one aggregated line and does not break it down.]`

**3. No web shop exists.** `shop.`/`store.`/`pay.`/`payment.`/`webshop.` on devsisters.com, cookierun-kingdom.com and devplay.com **all fail to resolve.** The "CookieRun store" link in the devsisters.com footer resolves to an **Amazon brand storefront** — merchandise, not game currency. The cookierun-kingdom.com production bundle contains zero payment hosts, PSP names or method enums.

### What the addressable channel actually is

The only revenue Devsisters bills itself is **merchandise and IP** — plush, figures, and the Braverse TCG — through Cafe24 and Shopify storefronts. **Verified by me on the live payment guides:**

| Storefront | Methods stated |
|---|---|
| `tw.cookierunstore.com/shopinfo/guide.html` | 支付寶 (Alipay) · **EXIMBAY：信用卡付款** · PayPal (Visa/Master/JCB/Amex, 3DS-only for direct card) |
| `en.cookierunstore.com/shopinfo/guide.html` | *"We accept the following forms of payment: Credit Card — Visa, MasterCard, American Express, Discover — PayPal"* |

**Sizing it, with every assumption labelled:**

| Input | Value | Status |
|---|---|---|
| FY2025 상품판매수익 (goods sales) | KRW 11.77bn ≈ **US$8.2M** | **SOURCED** (DART §III-3) · FX **ASSUMED** at 1,435 |
| DTC web share vs wholesale/distributor | 40–80% | **ASSUMED — the weakest link** |
| AOV (plush/figures/TCG, USD-priced, international shipping) | US$35–55 | **ASSUMED** |
| → **Monthly web orders** | **~5,000 – 16,000** | derived |

Against the group total of **~1.2–1.8M transactions/month**, of which **0% is orchestratable**.

**The addressable channel is roughly one-tenth of the 40,000/month floor**, on assumptions I have flagged as soft. It is the reason the override stands even though the matrix score does not.

### The honest counterweight — why this is "revisit", not "never"

That merchandise channel is the **fastest-growing thing in the business**: goods sales **tripled**, KRW 4.02bn → 11.77bn (+193%) FY2024→FY2025; overseas IP revenue grew 3.7×, KRW 3.00bn → 11.15bn; and **IP/non-game revenue passed 10% of total in H1 2026**, up from 4.71% for FY2025 — while game revenue fell 42.7% YoY in Q2 2026. It runs on **three directly-contracted PSPs across two commerce platforms plus a marketplace, with no routing layer** — textbook greenfield fragmentation.

**If IP revenue holds that growth rate for two more years, this account crosses the threshold.** It does not on 2026-09-20.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

## Rejection Rationale

Rejected by **analyst override at Gate 2 (app-store trap)**, not by matrix score. Devsisters states on its own help centre that it *"neither process[es] in-app purchases, nor ha[s] access to your credit card information — all purchases are processed by Apple and Google Play"*, and its audited FY2025 filing puts the game segment at **94.25% of revenue** supplied directly to Google Play and the App Store with no own-platform line. Orchestration cannot reach that revenue at all. The only channel Devsisters bills itself is a ~US$8.2M/yr merchandise and IP business at an estimated **5,000–16,000 orders/month — roughly a tenth of the 40,000 floor.** That channel is genuinely greenfield and tripled year over year, so this is a **revisit-in-12-months**, not a permanent no.

### ICP Score breakdown — 17 / 29, computed over the merchandise channel only

Recorded so the override is auditable, **not** as a recommendation.

| Signal | Points | Status |
|---|---|---|
| Monthly transaction count | **0** | ❌ **THE OVERRIDE.** ~1.2–1.8M/month total, **0% orchestratable**. Addressable channel ~5k–16k/month, below the floor |
| Orchestration status | **+4** | ✅ Greenfield over the merchandise channel — KG Inicis, Eximbay and PayPal contracted directly, across Shopify **and** Cafe24 **and** Naver Smart Store, with no layer above |
| 3+ countries | **+3** | ✅ Operating subsidiaries in Japan, Taiwan, USA and Germany |
| Multiple PSPs | **+3** | ✅ Three named in their own Korean privacy-policy processor table |
| Local rail gap in a top market | **+3** | ✅ The JP storefront takes cards and PayPal only — **no PayPay, no konbini, no carrier billing**. TW has no JKOPay, no MyCard, no ATM/convenience-store code. **Thailand had no storefront at all while sitting #3 grossing there** |
| Recent expansion | **+2** | ✅ Cookie Run: Classic global 2026-06-25; Crumble global 2026-07-30; IP revenue past 10% of total |
| Payment issues reported | **0** | ❌ **Verified absent, and this is diagnostic.** 49 recent App Store reviews pulled across us/kr/th/tw/jp/id: every payment mention is monetisation sentiment ("課金ゲー", pay-to-win), **zero processing friction.** That is exactly what you see when Apple and Google own the rail — declines and method coverage never reach the merchant |
| Funding >$10M | **0** | ❌ KOSDAQ-listed |
| High traffic outside home | **+2** | ✅ Korea is **28.3%** of revenue; North America **40.1%**, up 2.5× in one year |
| Competitor using orchestration | **0** | ⬜ Not established |
| Payment job postings | **0** | ⬜ Not established |
| **TOTAL** | **17** | 🔴 **Overridden — Not ICP** |

### Financials — the target-list figure is REFUTED (understated)

Audited DART FY2025, KRW thousand:

| Segment | FY2025 | FY2024 | FY2023 |
|---|---|---|---|
| Game — domestic | 77,737,019 | 102,627,820 | 66,663,480 |
| Game — overseas | 200,847,800 | 126,589,312 | 91,336,030 |
| **Game subtotal** | **278,584,819** | **229,217,132** | **157,999,511** |
| IP subtotal | 13,933,259 | 6,222,890 | 2,722,464 |
| Other (VC mgmt fees) | 3,060,269 | 746,533 | 421,354 |
| **TOTAL** | **295,578,347** | **236,186,555** | **161,143,329** |

**"~$150M (FY24)" is ~13–20% low.** FY2024 audited is **KRW 236.19bn ≈ US$161–173M** depending on rate; FY2025 is **KRW 295.58bn ≈ US$206M**, +25.1% YoY. *(KRW figures audited; USD conversion and FX rate are the analyst's, not sourced.)*

**Q2 2026 has turned, though:** revenue KRW 52.7bn, **−42.7% YoY**, operating loss KRW 16.0bn; H1 2026 operating loss KRW 33.3bn. `[Agent-sourced from a fetched Korean trade-press report of the company's own announcement — devsisters.com/stories/news/2026-2q returns HTTP 500 and the IR tables render client-side.]`

### Regional revenue — audited (KRW thousand)

| Region (as the filing labels it) | FY2025 | share | FY2024 | share |
|---|---|---|---|---|
| Korea | 83,581,610 | 28.3% | 106,596,264 | 45.1% |
| Major North American countries | 118,389,196 | **40.1%** | 48,192,221 | 20.4% |
| All other | 93,607,541 | 31.7% | 81,398,070 | 34.5% |

⚠️ **APAC-ex-Korea is not broken out** — it sits inside the undifferentiated 31.7% bucket. **Thailand, Taiwan, Japan and Indonesia cannot be sized from public data. Do not let anyone put a number on Thailand.**

**One genuine inference worth keeping:** the same note says *"no customer accounts for 10% or more of revenue."* If Apple and Google were the *customers* they would each obviously exceed 10% — so Devsisters books gross and treats the stores as agents, expensing their commission in 지급수수료. **The regional split is therefore end-user geography, not counterparty geography.** `[INFERENCE — the filing does not state its attribution basis, but no other reading fits.]`

### PSPs — from Devsisters' own legally-required processor table

Source: the Korean privacy policy's 개인정보 처리위탁 table, retrieved as Gatsby page-data JSON at `policy.devsisters.com/page-data/ko/privacy/page-data.json`.

| Vendor | Disclosed role |
|---|---|
| **㈜케이지이니시스 (KG Inicis)** | 온라인 결제(PG) |
| **Eximbay** | 온라인 결제(PG) — also named on the live TW payment guide, **verified by me** |
| **PayPal Inc.** | 온라인 결제(PG) — also live in the Cafe24 checkout bundle |
| **Shopify** | 쇼핑몰 플랫폼 관리 |
| **Cafe24** | storefront platform for en/jp/tw |
| **Naver Smart Store** | `cookierunstore.co.kr` 301s to `brand.naver.com/cookierun` |
| Apple / Google Play / **ONE store** / Galaxy Store | in-app purchase processing *(Galaxy Store `[UNVERIFIED — search summary only]`)* |

**NOT FOUND, all grepped across the full privacy-policy and ToS page-data:** Toss Payments · NICEPAY · NHN KCP · PAYCO · Danal · Mobilians · KakaoPay · Stripe · Adyen · Checkout.com · Worldpay · Xsolla · Coda Payments · PayerMax · Razer/Fiuu · 2C2P · Xendit · DOKU · Midtrans · KOMOJU · GMO · SB Payment · **Juspay · Spreedly · Primer · Gr4vy · CellPoint · APEXX · Payrails · IXOPAY · Yuno.**

⚠️ **DevPlay caveat.** Devsisters runs **DEVPLAY**, its own account/platform layer (`coupon.devplay.com` is live; DevPlay account articles exist in the help centre; server-engineering roles were posted). Search summaries describe it as covering *"membership, authentication, payment, push, coupons"* — `[UNVERIFIED — search summary only; the job posting that would confirm it now 404s]`. Even if DevPlay does hold a billing module, it would be an SDK wrapper over store IAP, not a card-rail orchestrator.

### Methodology notes

- **CSP is the no-evidence case here.** `cookierunstore.com`, `en.cookierunstore.com/order/basket.html` and `cookierunstore.com/ko/` return **no `Content-Security-Policy` header at all**, hence no `form-action`. Per the standing rule, the absence of a PSP host from a CSP proves nothing on this estate. Every PSP finding rests on the privacy-policy processor table, the live Cafe24 bundle or the storefront payment guides.
- **The Zendesk help-centre API worked cleanly** — `/api/v2/help_center/{locale}/articles.json?per_page=100` returned all 35 EN articles, and the rejection quotes came from that pull. Supported locales for CookieRun: Kingdom are `de, en-us, fr, ja, ko, th, zh-tw`. **No Indonesian, Vietnamese or Simplified Chinese locale** — treat the stub's Indonesia hypothesis as unsupported.
- **Storefront languages are ko / en / ja / zh-TW only.** There is no Thai storefront.
- 8 of 35 EN help articles are payment-related and **every one hands the user off to Apple, Google or ONE store.** Devsisters runs no payment support function of its own.

### What could NOT be established

1. Any **Apple vs Google vs ONE store vs Galaxy Store** revenue split — not disclosed anywhere.
2. The composition of **지급수수료 (KRW 105.05bn)** — one aggregated line; the ~30% store take is inferred from the ratio.
3. Any **disclosed payment-processing commission rate**.
4. **APAC-ex-Korea revenue by country** — collapsed into "기타 국가".
5. Whether **DevPlay includes a payment/billing module**.
6. **Live checkout method selectors** — the JP/TW/EN lists are *stated on merchant payment guides*, not *observed at a rendered checkout*.
7. **Reddit and Korean/Thai community sentiment** — Reddit's JSON API returns 403 from this environment.
8. Whether a **2026 반기보고서** exists on DART with a more recent region split.

### Overall research confidence — **HIGH on the rejection, MEDIUM on everything else**
The rejection rests on four help-centre articles I pulled and read myself through the Zendesk API, plus two live storefront payment guides I fetched. The DART figures, the Q2 2026 collapse and the privacy-policy processor table are agent-sourced and were not re-pulled by me — they corroborate the rejection rather than carry it.

</details>
