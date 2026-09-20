# Com2uS Corp

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 21 / 29 → ⭐ **High Priority** — earned on arithmetic, no override applied
**Industry:** Mobile game publisher — Summoners War, Com2uS Pro Baseball, Starseed · **HQ:** Seoul, South Korea — **Com2uS Corp (KOSDAQ: 078340)** · **Researched:** 2026-09-20 · **First email sent:** —
**Motion:** ⚠️ **DISPLACEMENT — a regional orchestrator is incumbent.** **PortOne** holds the orchestration seat inside the Hive billing platform, with **Xsolla** as global MoR and **MyCard** direct in APAC. **Never open with "you have no orchestration layer."** Open on **coverage and reach** — see §2.

---

> ## 🎯 THE HOOK — the web shop is three months old, and it is already leaking
>
> **Verified first-hand** on Com2uS's own Summoners War Web Shop content API (`summonerswar-shop-api.com2us.com/content/site?lang=en`, fetched 2026-09-20). From their own standing notice, verbatim:
>
> > *"**If you force-close the background app while making a payment in the Web Shop via an external browser, the product may not be credited.**"*
>
> And from the Korean version of the same notice: *"동일한 상품을 웹상점, PC 결제, 모바일 기기에서 동시에 결제 시도하시거나… **상품 지급이 정상적으로 진행되지 않을 수 있으니**"* — a double-payment hazard across three channels. `[The Korean line is agent-sourced; the English line I verified myself.]`
>
> **That is a merchant publicly documenting the failure mode of redirect-based web checkout, in its own storefront notice, as a warning to customers.** It is the single most quotable line on the account.
>
> ### And the timing is unusually good
>
> The Summoners War Web Shop is **roughly three months old** — their help article *"Please explain about the Web Shop in details"* carries `addTime: 2026-06-04`, and the standing article *"I did not receive a purchased pack"* was **updated on 2026-06-30 to add a Web Shop branch** alongside Google Play and Apple. `[Agent-sourced from the Hive support API.]`
>
> **They are standing up D2C billing right now, and the first thing they had to write was a warning about purchases not being credited.**
>
> ### The reach observation — 15 languages, and no local rail outside Korea
>
> **My own read of that same API:** the shop serves **`en, zh-hant, zh-hans, vi, tr, th, ru, pt, ko, ja, it, id, fr, es, de`** — fifteen storefront languages including Vietnamese, Thai and Indonesian. Sibling shops price in **TWD** (Starseed) and **USD** (Ace Fishing).
>
> **Korea's method list is documented in detail** — cards from nine issuers, Naver Pay, Samsung Pay, KakaoPay, PAYCO, Toss Pay, carrier billing, Toss Payments Quick Transfer — because Korean law requires a payment-limits disclosure. **There is no equivalent disclosure, and no evidenced local rail, for any other market.** No PayPay or konbini for Japan, which is a real revenue market with its own subsidiary. No QRIS, GCash, PromptPay, FPX or PayNow for the SEA languages they ship.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

### ✅ GATE 1 — Phase 0: PASSES, with one adjacency to note
Audited FY2025 subsidiary schedule: 25 subsidiaries, all game dev/service, VFX, broadcast content and entertainment management. No payments, e-money or PG entity. Four segments: Game, VFX/New Media, Broadcast Content, Performances. **Zero hits** for Yuno, Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails or IXOPAY across the full Hive Developers docs search index (6.9 MB) and 62 production JS bundles from two live web shops.

⚠️ **Adjacency worth flagging to Partnerships, not a blocker:** a *sister* company, **Com2uS Platform Corp** (컴투스플랫폼, under Com2uS **Holdings**, not consolidated into Com2uS Corp), operates the Hive platform and **resells PG connectivity** (PortOne, Xsolla, MyCard) to third-party game studios. It is a platform/SDK vendor that integrates PSPs, not a PSP. **No public information** on whether it holds a Korean 전자금융업/PG registration. `[Agent-sourced.]`

### ⚠️ GATE 2 — App-store trap: **PARTIALLY APPLIES. Read this before scoring the account in your head.**

**IAP dominates today. The web shop is real, multi-title and multi-currency — but it is new, deliberately gated, and Com2uS discloses nothing about its share.**

**Evidence that IAP still dominates (audited):** Com2uS's sales-channel disclosure in the half-year report filed **2026-08-14** — i.e. *after* the web shop opened — still reads: 「모바일게임은 각 플랫폼별/이동통신사별 애플리케이션 마켓인 앱스토어, 구글 플레이스토어 **등**을 통해 판매가 이루어지고 있습니다… 플랫폼 사업자가 발행하는 청구서나 신용카드 이용대금 청구서 등에 당사의 게임 요금이 **합산 청구**되며」. *(That wording repeats verbatim year on year and plausibly lags reality — say so rather than hiding it.)*

**And 지급수수료 shows no channel-shift fingerprint yet:**

| Basis | Revenue | 지급수수료 | Ratio |
|---|---|---|---|
| Standalone FY2024 | ₩557,260m | ₩290,689m | **52.2%** |
| Standalone FY2025 | ₩535,019m | ₩272,846m | **51.0%** |
| Consolidated FY2025 | ₩696,424m | ₩290,938m | 41.8% |
| Consolidated H1 2026 | ₩301,752m | ₩133,605m | **44.3% — up** |

The standalone ratio fell **1.2pp** in a year and the consolidated ratio **rose** in H1 2026. ⚠️ **This line blends platform fee, IP royalty, server and PG fee and cannot be decomposed. No payment-processing commission rate is disclosed anywhere.**

**Evidence the web shop matters anyway:**
- **Five live, distinct Com2uS-operated web shops** (all HTTP 200): `summonerswar-shop`, `cpbv-shop`, `cpbm-shop`, `starseed-shop`, `acefishing-shop` — all `.com2us.com`. Plus Hive-hosted shops at `shop.withhive.com/SWRUSH` and `/SpiritTales`.
- **Linked from the top-level nav of the official game site** — `<a href="https://summonerswar-shop.com2us.com/" target="_blank">Web Shop</a>`. Not a hidden asset.
- **Multi-currency, from the shops' own unauthenticated product APIs:** `{"price":49.99,"currency":"USD"}` · `{"price":300,"currency":"TWD"}` · `{"price":11000,"currency":"KRW"}`.
- **Com2uS frames it publicly as a fee-reduction strategy**, in its own newsroom: 「앱 마켓 수수료 절감, 낮은 결제 수수료를 통한 수익 개선, 유연한 글로벌 결제 전략 구성」.

**Evidence it is still small and deliberately suppressed** — **verified by me** on the live content API:
- *"Guest accounts cannot use the official Web Shop."*
- ***"The Web Shop is only available for accounts that have a history of in-app purchases in Summoners War from 2026 onwards."*** — a hard gate excluding the entire non-2026-paying base.
- *"Product prices can be checked after signing in"* — prices hidden pre-login (`is_price_visible: 0` on every SKU).
- **Only 9 SKUs.**

❌ **NOT ESTABLISHED: the web-store share of billings.** Not in the annual report, the half-year report, segment note 4 or revenue note 32. Note 32 splits only point-in-time vs over-time transfer — a recognition split, not a channel split. Geographic note 4 is by legal-entity location (Korea ₩666.6bn of ₩696.4bn), so it is useless for end-user geography. **Anyone claiming a web-store share percentage for Com2uS is making it up.**

### Financials — target-list figure CONFIRMED

**"~$500M (FY24)" — CONFIRMED.** FY2024 consolidated revenue **₩693,943 million**; at 1,300–1,400 KRW/USD that is **US$496M–534M**. *(FX range is arithmetic on the audited KRW figure; no specific rate sourced.)* `[Agent-sourced from DART.]`

| KRW m | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---|---|---|---|
| Mobile games — domestic | 135,664 | 174,193 | 195,479 | 99,587 |
| Mobile games — **export** | 409,778 | 385,092 | **348,902** | 158,096 |
| **Mobile games total** | 545,442 | 559,285 | 544,381 | 257,684 |
| Online games etc. | 16,585 | 19,217 | 29,221 | 14,279 |
| Media/content | 177,611 | 115,442 | 122,822 | 29,789 |
| **Total** | **739,639** | **693,943** | **696,424** | **301,752** |

**Export is 64% of mobile-game revenue.** Q2 2026: revenue ₩157,020m, operating profit ₩7,160m.

**No transaction, order or paying-user counts are disclosed anywhere.** Segment note also states **no single customer exceeded 10% of revenue** in FY2024 or FY2025 — notable, because it means **Apple and Google are each booked as <10%**, consistent with gross recognition with platform fee expensed in 지급수수료 rather than netted.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Com2uS`.*

⚠️ **Read before drafting — this is a DISPLACEMENT sequence and the rules are different.**

1. **NEVER write "you have no orchestration layer."** PortOne holds the seat and Com2uS names it in their own newsroom. Saying otherwise is factually wrong and burns the thread. Per `/full-outreach` §6a, open on **coverage and reach**: global PSP and rail breadth outside Korea, multi-region routing, the fifteen-language footprint the incumbent was not built for. **Never name the incumbent.**
2. **Lead with their own force-close warning.** It is their sentence, on their storefront, about their checkout. Nothing needs to be asserted.
3. **The reach asymmetry is the second observation:** Korea's method list is documented down to which card issuer is blocked on which wallet — and there is no equivalent for Japan, Thailand, Indonesia, Vietnam or the Philippines, all of which they ship a storefront language for.
4. **Never imply a web-vs-IAP split.** It is genuinely not knowable from outside.
5. **Do not present 지급수수료 as MDR.** It blends platform fees, IP royalties and PG fees.
6. **Do not quote FY2024 as current** — FY2025 is flat and Q2 2026 revenue is down ~15% YoY.
7. The **2026+ purchase-history gate** on the web shop is worth an embedded discovery question in E3 or E4 — it is an unusual choice and asking why is genuinely curious, not leading.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 21 / 29

| Signal | Points | Status |
|---|---|---|
| Monthly transaction count | **+3** | ⚠️ **Scored 3, not 5, deliberately.** Total billings imply ~2.2M txns/month (range 1.6–3.3M) — enormous. But **the orchestrable subset rests on an entirely unsourced share assumption** (44k–220k/month across a 2–10% range). The gate does not fire; the top band is not earned either |
| Orchestration status | **+3** | ⚠️ **Regional orchestrator incumbent — PortOne.** Displacement motion, per the APAC reference §4 |
| 3+ countries | **+3** | ✅ 15 storefront languages; shops priced in KRW, TWD and USD; subsidiaries in Japan and Vietnam |
| Multiple PSPs | **+3** | ✅ PortOne, Xsolla, MyCard, Terminal3, NHN KCP, Toss Payments, Naver Pay |
| Local rail gap in a top market | **+3** | ✅ **Japan has nothing on web** — no PayPay, no konbini, no carrier billing — despite a local subsidiary and real revenue. **No SEA rail is evidenced for any of the SEA languages they ship** |
| Recent expansion | **+2** | ✅ **The Summoners War Web Shop opened ~2026-06-04** — three months old. A live, dated D2C build |
| Payment issues reported | **+2** | ✅ Their own force-close warning; the help article extended 2026-06-30 to cover Web Shop; **a manual "resend" queue in the Hive console for unprocessed PG payments** |
| Funding >$10M | **0** | ❌ KOSDAQ-listed |
| High traffic outside home | **+2** | ✅ **Export is 64% of mobile-game revenue** (₩348.9bn of ₩544.4bn, audited) |
| Competitor using orchestration | **0** | ⬜ Not established |
| Payment job postings | **0** | ⬜ Not established |
| **TOTAL** | **21** | ⭐ **High Priority** |

### The orchestration seat — PortOne, verified by me

**Verified first-hand** on the Hive Developers console guide (`developers.hiveplatform.ai/ko/v4.24.3.0/operation/billing/pg_mangement/`, fetched 2026-09-20):

- 「**포트원**를 사용할 경우 **포트원 관리자 콘솔**에 IAP 서버 콜백 URL 등록 및 **PG사 설정**」 — Hive registers a webhook at `https://store.withhive.com/payment/result_processing/import` in the **PortOne** admin console, and the PG list is configured **inside PortOne**.
- 「**Xsolla**를 사용할 경우 Project ID와 Secret Key 발급은 별도 문의해 주세요.」
- 「**MyCard**와 **직접 계약**하여 사용할 경우 콘솔 > PG사 설정에서 서비스 국가를 MyCard로 선택하고 해시키 생성합니다.」 — MyCard currencies: **TWD, HKD, MYR, SGD, THB, IDR, PHP, VND, USD**.
- Currency resolution: 「Default : Hive_country로 판단한 국가의 통화」, falling back to **USD** where the Price Tier has no local entry. 「Xsolla : 결제 수단에 따라 유저가 직접 결제할 통화를 선택할 수 있음」.

**And Com2uS names both in its own newsroom:** 「Hive 빌링의 PG 결제는 검증된 솔루션인 **PortOne**과 **Xsolla** 페이먼트를 지원한다.」 `[Agent-sourced.]`

**This is not greenfield. The orchestration seat is occupied.**

⚠️ **Nuance worth carrying:** Hive is operated by **Com2uS Platform Corp**, a sibling under Com2uS Holdings — so PortOne is *Hive's* relationship, and Com2uS Corp consumes it. That is still the incumbent for Com2uS's billing, but it means the buying centre may sit across two legal entities. **One discovery question.**

### PSP table

| Vendor | Role | Evidence |
|---|---|---|
| **PortOne (포트원)** | **Korean payment orchestrator** — Hive registers its IAP callback in PortOne's console; Hive auto-imports the PG list configured there; the Hive console can view and cancel PortOne transactions | **Vendor's own production documentation — verified by me** |
| **Xsolla** | Global game PSP / merchant of record; Hive takes Project ID + webhook secret; per-country method selection | **Same doc — verified by me** |
| **MyCard** | **Direct-contract APAC PSP**, not routed via PortOne/Xsolla | **Same doc — verified by me** |
| **Terminal3** (Paymentwall/Xsolla family) | Named alongside Xsolla in the Price Tier and PC-cancellation docs | `[Agent-sourced]` |
| **NHN KCP** | (a) a sub-PG configured under PortOne: 「KCP 의 경우 PG ID를 확인하여 PortOne 관리자 콘솔과 동일하게 활성화」 (b) separately processes **Hive Platform's own KRW B2B subscription billing** | `[Agent-sourced]` |
| **Paymentwall** | Processes **Hive Platform's own USD B2B billing** — *this is Hive billing its own customers, NOT player payments* | `[Agent-sourced]` |
| **Toss Payments** | 「실시간 계좌이체 / **토스페이먼츠 퀵계좌이체**」 on Com2uS's own web-shop payment-limit page | `[Agent-sourced]` |
| **Naver Pay** | Hive console: 「네이버페이와 **직접 계약** 후 연동시에는 Chain Id 값을 반드시 입력해야 합니다」 → direct Naver Pay contract routed through PortOne | `[Agent-sourced]` |

**NOT FOUND anywhere** in the Hive docs index, the newsroom, the shop bundles or the shop pages: Adyen · Stripe · PayPal · Worldpay · Checkout.com · Coda · PayerMax · Razer/Fiuu · 2C2P · Xendit · DOKU · Midtrans · KOMOJU · GMO · SB Payment · Danal · Mobilians · NICEPAY · KG Inicis · Braintree · Airwallex · Nuvei · Rapyd · dLocal.
**Orchestrators NOT FOUND:** Yuno · Juspay · Spreedly · Gr4vy · CellPoint · APEXX · Payrails · IXOPAY.

⚠️ **False positives caught and discarded:** a "dLocal" hit in the Hive docs was `useForegroundLo`**cal**`Push`. `kCP` in two shop HTML files was base64 noise, not NHN KCP (KCP is confirmed separately and properly, above).

### Payment methods

**🇰🇷 Korea — documented in detail, because Korean law requires a payment-limits disclosure** `[Agent-sourced from Com2uS's own two web-shop limit pages, images read.]`

| Method | v1 page | v2 page (the one the SW shop links to) |
|---|---|---|
| Credit/check card — KB국민, 롯데, 신한, NH농협, 하나, 삼성, 현대, BC, 우리 | ✅ | ✅ |
| **Naver Pay** (incl. Naver Points) | ✅ | ✅ |
| **Samsung Pay** (Hyundai card blocked) | ✅ | ✅ |
| **KakaoPay** (Hana card blocked in v1) | ✅ | ✅ |
| **PAYCO** | ✅ | ✅ |
| **Toss Pay** | ✅ | **absent** |
| **Carrier billing** — SKT, KT, LGU+, MVNO — cap ₩600,000/month | ✅ | ✅ |
| **Toss Payments Quick Transfer** (₩500k/txn, ₩2m/day, ₩5m/month) | ✅ | **absent** |

Korea is material: domestic mobile-game revenue ₩195,479m in FY2025 = **36% of mobile game revenue**.

**Everywhere else**

| Market | Method | Status |
|---|---|---|
| 🇹🇼 Taiwan | **MyCard** | CONFIRMED as an available Hive PG (TWD); Starseed shop prices in TWD. **Not confirmed enabled on any specific title** |
| 🇹🇼 Taiwan | JKOPay, ATM transfer | ❌ **NOT FOUND** |
| 🇯🇵 **Japan** | **PayPay, konbini, carrier billing on web** | ❌ **NOT FOUND** — and Japan is a real revenue market (Com2uS Japan Inc.; ₩13,111m FY2025 entity-level). The only konbini-adjacent reference is Hive IAP receipt code 1000519 「느린 결제(예. 편의점 결제)」, which is a *store* IAP pending-receipt path, not web billing |
| 🇨🇳 China | **Alipay + WeChat Pay** into the in-house **Lebi (러비)** stored-value wallet, priced in CNY | ✅ CONFIRMED — Hive console doc |
| HK/MY/SG/TH/ID/PH/VN | MyCard currencies HKD/MYR/SGD/THB/IDR/PHP/VND | ✅ CONFIRMED **as a platform capability**; ❌ **NOT confirmed enabled on any Com2uS title** |
| 🇮🇩 Indonesia | QRIS, GoPay, DANA, OVO | ❌ **NOT FOUND** |
| 🇵🇭 Philippines | GCash, Maya | ❌ **NOT FOUND** |
| 🇹🇭 Thailand | PromptPay, TrueMoney | ❌ **NOT FOUND** |
| 🇲🇾 Malaysia | FPX, Touch 'n Go | ❌ **NOT FOUND** |
| 🇸🇬 Singapore | PayNow | ❌ **NOT FOUND** |
| 🇻🇳 Vietnam | MoMo, ZaloPay | ❌ **NOT FOUND** (subsidiary present; Vietnam revenue ₩2,228m FY2025) |
| Global | **USD fallback** where the Price Tier has no local currency | ✅ CONFIRMED |
| Anywhere | **PayPal, Apple Pay, Google Pay** | ❌ **NOT FOUND** by name in any Com2uS or Hive source |

### Friction

1. **Their own force-close warning** — quoted in the hook. **Verified by me.**
2. **The standing help article "I did not receive a purchased pack"** (`addTime` 2024-10-19, **`modTime` 2026-06-30**) was updated to add a **Web Shop** branch requiring *"Purchase receipt where we can see the purchase date and time."* `[Agent-sourced from the Hive support API.]`
3. **The Hive console exposes a dedicated queue for failed web payments**: 콘솔 > 빌링 > IAP v4 > **PG결제 지급완료 미처리 내역**, with a manual **재전송 (resend)** button, because 「PG결제가 정상적으로 완료되지 않은 내역」. **An ops team is manually re-driving failed web payments.** `[Agent-sourced.]`
4. **The eligibility gate as friction** — guests excluded, 2026+ IAP history only, prices hidden pre-login, 9 SKUs.
5. Refunds are 1:1 inquiry only; no self-serve.

⚠️ **Not established:** no citable corpus of app-store reviews, Reddit threads or Korean community posts about payment failures was obtained. A `forum.com2us.com` refund thread appeared in search results but was not fetched — `[UNVERIFIED]`.

### Volume — DERIVED, and the addressable slice is guesswork

**Step 1 — total.** FY2025 mobile game revenue **₩544,381m** (SOURCED), recognised **gross** of platform commission (supported by the 51% 지급수수료 ratio and the "no customer >10%" disclosure). ÷12 = ₩45,365m/month; at **1,380 KRW/USD (ASSUMED)** ≈ **US$32.9M/month**. At an **ASSUMED US$15 average ticket** → **≈2.2M transactions/month** (range 1.6–3.3M). **Phase 0 volume test passes by ~40×.**

**Step 2 — the orchestrable subset. NO DISCLOSURE EXISTS.**

| Assumed web-shop share | Monthly web GMV | **Monthly PG transactions @ $15** |
|---|---|---|
| 2% | ~$0.66M | **~44,000** |
| 5% | ~$1.64M | **~110,000** |
| 10% | ~$3.29M | **~220,000** |

**Orchestrable volume is plausibly 44k–220k/month — above the floor across the whole assumed range, but the entire result rests on an unsourced share assumption.** The honest framing: *the D2C channel exists, is multi-currency and multi-title, and its size is unknown to anyone outside the company.*

**Not modelled, all upward:** the four other Com2uS web shops (CPBV, CPBM, Starseed, Ace Fishing); the China Lebi wallet (Alipay/WeChat top-ups); Hive's third-party shops *(which are Com2uS Platform's volume, not Com2uS Corp's)*. **Downward:** the 2026+ IAP-history gate suppresses year-one conversion materially.

### Methodology notes

- ⚠️ **CSP is the no-evidence case on every checkout host.** `summonerswar-shop`, `cpbv-shop`, `cpbm-shop` and `shop.withhive.com` return **no CSP header at all**. `com2ustore.com` (Shopify merchandise) has a CSP but **no `form-action`**. **No negative inference is drawn from any of them.**
- **The JS bundles yielded nothing, and that is itself the finding.** All 28 chunks from the Summoners War shop and all 34 from the CPBV shop (3.4 MB) contain **zero PSP references** — because the shops are Next.js front-ends that call `POST /purchase/payment/init` on `{game}-shop-api.com2us.com` and **the PSP is resolved entirely server-side**. `GET /purchase/payment/method` returns `{"code":10010,"msg":"Session expired"}` unauthenticated. **A server-side PSP resolution is what a routing layer looks like from outside.** `[Agent-sourced.]`
- **Merchandise is a separate stack:** `com2ustore.com` / `.co.kr` are **Shopify** (`powered-by: Shopify`), physical goods, out of scope for game billing.

### What could NOT be established

1. **Web-store share of billings.** No filing, IR deck, press release or earnings commentary discloses it. **The single biggest gap, and not fillable from public sources.**
2. **Which PG platform is live per title and per market** (PortOne vs Xsolla vs MyCard) — resolved server-side at `POST /purchase/payment/init`; the method endpoint is session-gated.
3. **Payment methods outside Korea on Com2uS's own shops.** Korea is documented because Korean law requires it; no equivalent page exists for any other market.
4. **Japan entirely** — no PayPay, konbini or carrier evidence for web billing.
5. **Any disclosed payment-processing commission rate.**
6. **Transaction, order, paying-user, MAU or DAU counts** — none disclosed.
7. **Exact web-shop launch date** — best proxy is the help-article creation timestamp, 2026-06-04.
8. **Whether Com2uS Platform holds a Korean PG or e-money licence.**
9. **Any complaint corpus** — no citable review/Reddit/community URLs obtained.

### Overall research confidence — **HIGH on architecture, NIL on the channel split**
The PortOne/Xsolla/MyCard configuration, the fifteen-language footprint, the 2026-IAP-history gate and the force-close warning were read by me on the live Hive documentation and the live shop content API today. The DART financials, the Korean payment-limit pages and the support-API timestamps are agent-sourced and were not re-pulled by me. What does not exist anywhere is the one number that would size the opportunity.

</details>
