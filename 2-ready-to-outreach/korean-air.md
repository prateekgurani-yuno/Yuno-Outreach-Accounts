# Korean Air

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 17 / 29 → ⭐ **High Priority**
**Industry:** Airlines (long-haul passenger + major cargo) · **HQ:** Seoul, **South Korea** — 대한항공, **KRX 003490** · **Researched:** 2026-09-19 · **First email sent:** —
**Motion:** **In-house** — direct-to-VAN, gateway-per-region, **no PG intermediary and no orchestrator**. Affirmative evidence from their own processor disclosure. **Respect the build; anchor on reach and consolidation, never "you need orchestration".**

---

> ## ⏰ THE WINDOW IS NOW, AND IT CLOSES IN DECEMBER
>
> **2026-12-17: the integrated Korean Air launches**, absorbing **all** of Asiana's assets, liabilities, rights, obligations and personnel. Flight numbers renumber OZ→KE from 2 Nov; reservations pre-migrate.
> **2027-03-17: 통합 진에어 launches** — Jin Air survives, **Air Busan and Air Seoul dissolve into it**, creating Korea's largest LCC by fleet.
> **Integration cost KRW 900bn–1tn (~US$620–690M)**, to be recouped by **end-2028**, with cost reduction explicitly targeting **구매·정비·IT 통합** — procurement, maintenance and **IT integration**.
>
> 📌 **On 17 December, Korean Air inherits a second, redundant, contractually live payment stack — and three more collapse in March.** There is a board-level mandate to recover ~KRW 1 trillion through IT integration, and **no public plan anywhere addresses what happens to the payment stacks, PSP contracts or merchant accounts.** Searched directly; nothing exists.
>
> **Decisions freeze at cutover. The conversation has to happen before December.**
>
> ⚠️ **One thing that cuts AGAINST the naive pitch, and you should know it before the call: both carriers already run Amadeus Altéa.** This is not a big-bang PSS migration. The Korean press line is precise — *"서로 다른 예약·**유통** 환경"*, different **distribution** environments: KE's GDS is TOPAS, Asiana's is Asiana Sabre. **The hard part is everything hanging off the side of Altéa, and payments is exactly one of those things.**

---

> ## 🎯 THE HOOK — their US/English/USD storefront still produces a cross-border authorisation
>
> **✅ Verified verbatim by me** at [milemoa 9207706](https://www.milemoa.com/bbs/board/9207706), dated **2022-04-06**. A SKYPASS Visa cardholder — three cards, two US corporate and one personal — could not pay on Korean Air's own site:
>
> > 「비자에서 **decline**된 거라고 알려줍니다. 제가 **만불 넘게** 결제를 하다보니 막힌것 같고, 향후에도 **고액 해외 결제는 무조건 막힌다**고 하네요. (**대한항공 사이트는 미국+영어+달러 설정이라도 해외 결제로 인식되는 것 같습니다.**)」
>
> *"Visa told me it was declined by Visa. It seems to have been blocked because I was paying over ten thousand dollars, and they said high-value overseas payments would always be blocked in future. (**It seems Korean Air's site is recognised as an overseas payment even with the US + English + USD setting.**)"*
>
> - **The decline came from the Visa network, not the issuer** — the issuer's records showed no decline at all, which is why it took **six hours** bounced between bank and airline.
> - **Trigger was ticket value over US$10,000** — i.e. precisely the premium long-haul cabin.
>
> ⚠️ **State this accurately or not at all.** It is **one cardholder's first-person account from 2022**, and the cross-border classification is **that user's own inference** (「~인 것 같습니다」 — *"it seems"*), not documentation. It was also ultimately **resolved** via Visa. **Do not present it as proof that all KE foreign transactions are cross-border.** Present it as the observation it is — and note the same complaint exists against **Asiana's** site too, which means **December doubles the problem rather than fixing it.**

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Korea's flag carrier, mid-way through the largest airline integration in Korean history. **FY2025 (standalone, preliminary) revenue KRW 16.50 trillion — a record, +2% YoY — with operating profit KRW 1.54tn, down 19%** on FX, fuel, labour and depreciation.

**SimilarWeb total visits:** **Not obtained.** No data supplied; `koreanair.com` is WAF-403. Country profile unverified; **no split invented.**

### ✅ THE STUB'S $11.3B VERIFIES — with one correction
KRW 16.50tn ÷ ~1,460 KRW/USD ≈ **US$11.3B**. ✅ **But it is standalone Korean Air only** — it excludes Asiana and the LCCs. **Do not use $11.3B as the post-December figure.**

**And the card-addressable base is smaller still.** ✅ Verified from KE's own newsroom (Q4 2025 preliminary results): **여객 (passenger) 56.9% · 화물 (cargo) 27.1% · other ~16%.** **Cargo is invoiced B2B and sits entirely outside a card checkout**, so the realistic card surface is the ~57% passenger line plus ancillaries — **call it US$6.5–7.5B, not $11.3B. Use the honest number; it is still very large.**
⚠️ **A search summary claimed an annual split of 여객 16.3조 / 화물 6.2조. That is refuted — it sums to 22.5조 against a 16.5조 total. Discard it.**

### Known PSPs — ✅ FOURTEEN named entities, verified by me in full
**Source:** Korean Air 개인정보 처리방침 — 개인정보 처리 위탁 현황. The live page is WAF-403; I read it from the **Wayback snapshot of 2020-04-21**.

The payment task row — 「항공권 구매 등 당사의 유상 상품 및 서비스에 대한 **대금 결제**」 — names, verbatim:

> **KICC(한국정보통신) · KOVAN(코밴) · KIS정보통신 · 퍼스트데이터 코리아 · KSNET(케이에스넷) · ㈜카카오페이 · 엔에이치엔페이코㈜ (PAYCO) · 금융결제원 · Wellnet (Konbini) · Alipay · Cybersource · PayEase · Elavon · PayPal**

| Layer | Entity | Function |
|---|---|---|
| **Korean card VANs** | KICC, KOVAN, KIS정보통신, First Data Korea, KSNET | **Five direct VAN connections — and NO payment gateway** |
| Korean wallets | KakaoPay, PAYCO | Domestic alt-payment |
| Korean bank rails | 금융결제원 (KFTC) | 계좌이체 / 가상계좌 |
| **International card** | **Cybersource** (gateway) + **Elavon** (acquirer) | Cross-border card |
| Global wallet | PayPal | International storefronts |
| China | Alipay, **PayEase** | China-market acquiring |
| **Japan** | **Wellnet (Konbini)** | Japanese convenience-store cash |
| PSS / distribution | Amadeus IT Group S.A, 토파스 (TOPAS) | Altéa + GDS |

### ❌ Sourced absence — from a document that names 14 payment entities
**No Korean PG whatsoever:** KG이니시스 **0** · 토스페이먼츠 **0** · KCP **0** · 나이스페이 **0** · 다날 **0** · 헥토 **0** · 세틀뱅크 **0**.
**No global orchestrator or alternative acquirer:** Adyen **0** · Stripe **0** · Worldpay **0** · Braintree **0** · CellPoint **0** · 네이버페이 **0**.

> 📌 **The absence of any Korean PG is the architecturally interesting part.** A merchant this size connects **straight to five VANs** and **self-assembles the routing**. That is the signature of an in-house orchestration layer maintained by hand — across roughly 40 storefronts.

> 🚩 **TWO NEAR-MISSES CAUGHT — both would have put a false claim in an email:**
> 1. **한진정보통신㈜** (Hanjin's captive IT company) sits immediately adjacent to the payment row in a column-major table. **It belongs to the PRECEDING row** — 「웹사이트 프로그램 개발 및 유지보수」, web development and maintenance. ✅ I checked the raw text. **It is NOT the payment operator. Do not assert it.**
> 2. **삼성페이 appears twice in the document — but in the 모바일월렛 section**, where Samsung Electronics receives SKYPASS membership data alongside SK Planet (Syrup), KT (Clip) and PAYCO. **That is a loyalty card held in a wallet, NOT a payment method.** Same class of trap as ANA's `PayPay銀行`.

> ⚠️ **DATE CAVEAT — READ BEFORE USING ANY VENDOR NAME.** This list is **2020-04-21 vintage**. The live page is WAF-403 and the post-2021 site is a client-rendered SPA, so **every Wayback capture after the redesign archives as an empty JS shell.** **The 2026 state is unverified. Treat this as directionally reliable architecture, not a current contract roster — and do not put a vendor name in an email on this basis alone.**

### Payment methods
**Korea domestic (confirmed as processors, not as displayed checkout options):** 신용카드 (five VANs; issuers 비씨, KB국민, 롯데, 신한, KEB하나, 현대, 삼성, NH농협, 씨티…), 카카오페이, 페이코, 계좌이체/가상계좌 via KFTC.
**International:** PayPal, Alipay, China domestic cards via PayEase, **Japanese konbini via Wellnet**, international cards via Cybersource + Elavon.
❌ **UnionPay, WeChat Pay, Apple Pay, Google Pay, Naver Pay, Toss Pay — UNCHECKED, not sourced-absent.** The per-storefront payment pages exist and are indexed but are **WAF-403 to curl and 503 to WebFetch**, and their only Wayback captures are empty JS shells. **Do not claim absence.**

### 💳 Instalments — the sharpest secondary observation
**Korean-issued cards get 무이자 할부; foreign-issued cards do not.** KE's own guidance reportedly states **해외 발행 카드의 경우 할부 결제가 불가** and **해외 발행 법인 카드는 사용할 수 없습니다** — foreign corporate cards cannot be used at all. `[UNVERIFIED — search summary; source pages WAF-blocked]`
**Instalments are the single biggest conversion lever in Korean high-ticket retail, and they are structurally unavailable to exactly the foreign segment.** ⚠️ **Verify before using.**

### Buying signals
- ⏰ **December 2026 merger cutover** with no published payments plan
- 💰 **KRW ~1tn integration cost to recoup by end-2028**, explicitly via IT integration
- 🌏 **~40 storefronts on a hand-maintained direct-to-VAN stack**
- 🔴 **Cross-border decline on the US/USD storefront** at high ticket values
- 🏢 **Asiana still sells on its own stack today** — confirmed by a live Asiana-run KakaoPay promotion, implying a separate merchant account
- ✈️ **Three LCC stacks collapse into one in March 2027**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Korean Air` to draft the 12-touch sequence.*

**Six instructions for whoever drafts it:**
1. **The merger timing is the opener and the reason to write now.** Not the payment stack — the *calendar*. On 17 December they inherit a second live payment estate with a billion-dollar IT-integration mandate and no published answer for payments.
2. ⛔ **Do NOT pitch a PSS migration story.** Both carriers already run Altéa. Getting this wrong marks us as not having done the work. The gap is **distribution and payments**, not the PSS.
3. ⛔ **Do NOT pitch replacing their Korean domestic acquiring.** It is entity-gated and it works. The sellable surface is the **foreign-cardholder leg** and the **consolidation** of two estates into one.
4. **Motion is in-house.** Five direct VAN connections with no PG is a deliberate, competent build. Anchor on reach and opportunity cost.
5. **The cross-border decline is the second observation — and state it as one person's 2022 account**, not as a general truth. Its real power is that **Asiana has the same complaint**, so the merger doubles it.
6. ⛔ **Do NOT name a vendor from the processor list in an email.** It is six years old.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 17 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED as a bound.** Revenue **KRW 16.50tn** FY2025, with a **verified Q4 split of 56.9% passenger / 27.1% cargo** from KE's own newsroom. Against the ~KRW 9.4tn passenger line, even an implausibly high **KRW 3,000,000 (~US$2,050) per booking** gives ~3.1m bookings/year = **~260k/month**, before ancillaries. **Every plausible divisor clears 100k.** ⚠️ FY2025 passengers carried could not be found. |
| Orchestration status | **+1** | ✅ **In-house, on affirmative evidence.** Fourteen named payment entities under one task; **five Korean VANs connected directly with no PG intermediary**; no orchestrator anywhere in the disclosure. Someone at KE maintains that routing by hand. **Amadeus DES is the digital/commerce layer — it is NOT a payment orchestrator** and does no multi-acquirer routing, retry or cascading. Per the matrix, in-house scores +1, and correctly so: it is the hardest motion. |
| 3+ countries | **+3** | ✅ ~40 country storefronts; region-specific acquiring — PayEase and Alipay for China, Wellnet for Japan, Cybersource and Elavon internationally. |
| Multiple PSPs | **+2** | ✅ **The best-evidenced PSP row in this repo.** Fourteen entities named in a legally-mandated disclosure I read in full. |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **Deliberately not awarded, on a discipline point.** Naver Pay, Toss Pay and Samsung Pay are absent from the payment row — but **the document is six years old**, and those rails' current status is unknowable from it. **I will not score a rail gap off a 2020 snapshot.** ⚠️ If someone reads the live payment-guide pages from a Korean IP and the absence holds, **this row is +3 and the account is 20/29.** |
| Recent expansion | **+2** | ✅ **The largest airline integration in Korean history** — full absorption of Asiana on 2026-12-17, three LCCs merging 2027-03-17, well sourced across Korea Times, KE's own newsroom and Korean trade press. |
| Payment issues reported | **+2** | ✅ **Verified verbatim by me** — the milemoa cross-border decline, first-person and dated. Supported by FlyerTalk and Tripadvisor reports of KE requiring **physical card plus photo ID presented at a branch or airport** to verify payment before boarding, and reports that foreign cards fail on **Asiana's** site too. ⚠️ Only the milemoa post was fetched; the rest are search-summary. |
| Funding >$10M | **0** | ❌ KRX-listed. No round. |
| High traffic outside home | **0** | ⬜ No traffic data. |
| Competitor using orchestration | **+2** | ✅ **Singapore Airlines runs a competitor's orchestration layer** (established in the Cathay file), and SQ competes with Korean Air head-on for Asia–US and Asia–Europe long-haul premium traffic — the same competitive set that justified awarding this row for Cathay. ⚠️ **Asiana, the like-for-like domestic comparison, is being absorbed rather than adopting anything.** |
| Payment job postings | **0** | ⬜ Not found. |

**Tier: 17 / 29 → ⭐ High Priority.** No override applied.

### Source Notes
- ✅ **The fourteen-entity processor list was verified by me in full** from the 2020-04-21 Wayback snapshot, including the exact payment task row and the sourced absence of every Korean PG and every global orchestrator.
- ✅ **The two near-misses were checked by me personally** — 한진정보통신 belongs to the web-development row, and 삼성페이 appears only in the mobile-wallet loyalty section.
- ✅ **The milemoa post was fetched and read in full**, including the verbatim Korean.
- ✅ **The Q4 2025 passenger/cargo split** comes from Korean Air's own newsroom release (2026-01-15).
- ⚠️ **FY2025 revenue and operating profit** are from Korean wire coverage of the 2026-01-15 disclosure `[search-summary corroborated across three outlets]`.
- ⚠️ **Merger dates and integration economics** are well-sourced across Korea Times, KE's newsroom and Korean trade press, but were **not individually fetched by me**.
- ⚠️ **Both carriers running Altéa** rests on a 2020 article plus the 수탁사 list naming Amadeus; **Asiana's Altéa migration is search-summary only.**
- ❌ **`koreanair.com` and `flyasiana.com` are both WAF-403.** Per-storefront payment pages are unreadable by every route tried, and post-2021 Wayback captures are empty SPA shells.
- ❌ **Asiana's own processor list could not be obtained** — Akamai 403. **Asiana's PSP set is unknown**; only KakaoPay is confirmed, via a promotion page.
- ❌ **No public statement on payment-stack or merchant-account consolidation exists.** Searched directly.

### Manual Research Recommendations
> **1. Re-pull the current 수탁사 list from a browser or a Korean IP.** The roster is six years old and it is the backbone of this file.
> **2. Load `koreanair.com/us/en` from a US IP and attempt a high-value booking**, inspecting the acquirer descriptor. **This is the crux of the pitch** — it would establish whether Cybersource/Elavon acquiring is per-country or single-entity, which one 2022 forum post can only imply.
> **3. Get Asiana's processor list.** It determines how much redundancy December actually creates.
> **4. Verify the foreign-card instalment exclusion** from the live payment guide.
> **5. Pull the DART 사업보고서** for annual passenger figures and the full-year cargo split.

---

## Executive Summary

Korean Air is mid-way through the largest airline integration in Korean history, and the timing is the account. On **17 December 2026** the integrated carrier launches, absorbing **all** of Asiana's assets and obligations — which legally sweeps in Asiana's separate, contractually live payment stack — and on **17 March 2027** three LCC stacks collapse into one. There is a board-level mandate to recoup **KRW ~1 trillion of integration cost by end-2028, explicitly through IT integration**, and **no public plan anywhere addresses payments.** Underneath, their own processor disclosure — which I read in full — names **fourteen payment entities**: five Korean card VANs connected **directly, with no payment gateway anywhere in the list**, KakaoPay and PAYCO, the KFTC bank rails, **Cybersource and Elavon** for international cards, **PayPal**, **Alipay and PayEase** for China, and **Wellnet** for Japanese convenience-store cash. No Korean PG, no Adyen, no Stripe, no orchestrator. A merchant of this size self-assembling routing across five VANs and roughly forty storefronts **is** the in-house orchestration layer. The sharpest customer-facing evidence is a 2022 first-person account, verified verbatim, in which a US cardholder paying over $10,000 on Korean Air's **US, English, USD** storefront was declined **by the Visa network rather than the issuer**, with the cardholder concluding the site is still treated as a cross-border transaction — and the same complaint exists against Asiana's site, which means December doubles it rather than fixing it. ⚠️ The processor list is **2020-vintage** and the live site is WAF-blocked, so no vendor name should reach an email until someone re-pulls it from a browser.

</details>
