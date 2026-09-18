# Interpark Ticket (NOL 티켓)

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 10 / 29 → 🟢 **Medium** (clears the ≥10 outreach bar; see the scoring note)
**Industry:** Event ticketing (concerts, musicals, theatre, sport) · **HQ:** Seoul, **South Korea** — **(주)놀유니버스 NOL Universe Co., Ltd.**, Yanolja group · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** **In-house** — self-licensed PG, own wallet and vault, dual card PGs in parallel. Affirmative evidence, not absent hits (see 3B).

---

> ## ⚠️ ICP JUDGEMENT CALL — read this before anything else
>
> **NOL Universe holds its own Korean e-finance licences** and publishes 전자금융거래약관 as the provider of **전자지급결제대행 (PG)**, **결제대금예치 (escrow)** and **선불전자지급수단 발행·관리 (prepaid instrument)**.
>
> Under `CLAUDE.md`, *"Company is a PSP, gateway, acquirer or orchestrator → out of ICP, route to Partnerships."* **On a literal reading this account could be gated out.**
>
> **My read: keep it in ICP.** It is a ticketing marketplace that self-licensed to run its own flows and wallet — standard for large Korean e-commerce (11번가, G마켓 do the same). **It sells no payment services to third parties.** It is a merchant with a licence, not a PSP.
>
> **But it does change the pitch**, and it is Prateek's call to overrule. Flagging rather than deciding silently.

---

> ## 🎯 THE HOOK — they have already priced their own cross-border payment pain, itemised it, and published it to their promoters
>
> **Verified by me verbatim**, from Interpark's own merchant-facing notice at `tmanager.interpark.com/html/reservationFee.html`:
>
> > 「[인터파크글로벌 예매수수료] 본인인증이 적용된 상품은 **예매수수료 8,000원**이 적용됩니다. 예매수수료는 웹사이트 운영, **결제수수료** 외에도 **본인인증/부정예매방지** 및 **글로벌 예매 시스템 운영 비용**이 포함돼 있습니다.」
>
> *"A booking fee of **₩8,000** applies to products with identity verification. The fee includes, in addition to website operation and **payment processing fees**, the costs of **identity verification / fraud prevention** and **operating the global booking system**."*
>
> And the stated reason for the increase:
> > 「**Fraud Detecting System 지원 결제프로세스** 및 부정예매 방지 기술 도입에 따른 예매수수료 인상」
>
> **They are charging foreign buyers ₩8,000 a ticket to cover cross-border payment cost, fraud tooling and the running of a second booking system — and they wrote it down for their own promoters.** We are not hypothesising a pain point. They have quantified it.
>
> ### And the identity gate that sits on top
> Same page, verified: **eKYC mandatory since 2024-07-01** for musical and concert products on the global side, **passport required, one passport per account**, and — 「인터파크글로벌은 글로벌 회원을 대상으로 하는 예매 서비스이므로, **대한민국 여권으로는 본인인증을 할 수 없습니다**」 — **Korean passports cannot verify there at all.** Domestically, 본인인증 gained a **1-year expiry on 2024-07-11**; expired customers **cannot book until they re-verify**, and Korean 본인인증 runs on a **Korean mobile number**. No Korean phone, no domestic storefront.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Korea's largest event-ticketing platform. ⚠️ **The stub is stale on ownership** — the operating entity is **(주)놀유니버스 (NOL Universe)**, not "Interpark Triple", following the March 2025 group rebrand (Yanolja → NOL, Interpark Ticket → **NOL 티켓**). **Use "NOL Universe" in outreach.**

**SimilarWeb total visits:** **Not obtained.** No data supplied. Country profile unverified; **no split invented.**

### Known PSPs — verified by me from the legally-mandated 위탁 disclosure
Source: §6⑥ of the NOL Universe 개인정보처리방침, fetched and read in full. This is a **primary merchant legal disclosure**, the strongest PSP evidence class available.

| Counterparty | Disclosed scope, verbatim |
|---|---|
| **㈜KG이니시스 + 토스페이먼츠** | 「결제(신용카드, 무통장, 실시간 계좌이체, 지류상품권 및 기타 결제수단), 환불계좌 인증 및 결제 도용방지」 — **two card PGs named on ONE line for an IDENTICAL scope** |
| **주식회사 헥토파이낸셜** | 가상계좌 입금 (virtual accounts) |
| **네이버㈜** | 네이버페이 |
| **㈜카카오페이** | 카카오톡 간편결제 + 본인확인 |
| **엔에이치엔페이코㈜** | PAYCO |
| **㈜비바리퍼블리카** | Toss 간편결제 |
| **㈜KG모빌리언스 + 갤럭시아머니트리** | 휴대폰 소액결제 — **two carrier-billing vendors in parallel** |
| **㈜쿠콘** | 계좌 유효성 검증 |

**Sourced absence** — read the whole table: **NHN KCP, NICE, Danal, Settle Bank, KSNET, Payletter** are not in it. Nor is **any foreign PSP** — Adyen, Stripe, Checkout.com, Worldpay, Cybersource, 2C2P all absent.

> 📌 **The §7 국외이전 (cross-border transfer) table discloses exactly ONE overseas recipient: Braze Inc (US), for CRM.** No overseas payment processor at all — strong negative evidence that **there is no foreign acquirer in the stack**, exactly as Korea's entity-gating would predict.

### Domestic methods — comprehensive, and that matters
신용카드 · 가상계좌 · 무통장입금 · 휴대폰 결제 (capped ₩200,000) · 실시간 계좌이체 (**movies only**) · 상품권 (컬쳐캐쉬, 해피머니) · 예매권 · **카카오페이 · 네이버페이 · 페이코 · 토스페이** · **인터파크페이 / NOL 인터파크페이** (own wallet, stores card *or* bank account, PIN checkout).

**There is essentially no domestic rail gap.** The gap is the cross-border leg.

> ⚠️ **One real domestic conversion leak:** 무이자 할부 (interest-free instalments) — the biggest lever on ₩150k–300k concert tickets — is **blocked on every wallet they support**: 「무이자할부는 개인 신용카드 결제시에만 적용되며, 네이버페이, 카카오페이, 페이코, 토스페이, NOL 인터파크페이 등 간편결제로 결제한 건에 대해서는 혜택이 적용되지 않습니다」. `[UNVERIFIED — search summary; direct fetch to benefit.interpark.com was reset]`

### The global storefront
`globalinterpark.com` and `ticket.interpark.com/global` both **301 to `world.nol.com`** — verified by me. The separate global storefront no longer exists as a separate brand.

**Payment strings in the shipped bundle, verified by me:** `"order_page_oversea_card":"Credit/Debit Card"` · `"order_page_ali_pay":"Alipay"` · `"order_page_wechat_pay":"WeChat Pay"`. **PayPal: zero occurrences** — secondary sources claim it; **the live page contradicts them. Do not put PayPal in an email.**

Also verified: `"Refunds are processed in **KRW**. The final amount received may vary depending on your card issuer's exchange rate."`

> ⚠️ **TWO CAVEATS I FOUND THAT THE RESEARCH DID NOT FLAG, and both matter:**
> 1. **Those `order_page_*` strings sit inside a block of ACCOMMODATION strings** — `common_stay_promotion_badge`, `stay_date_range_late_check_in_guide`, and the KRW refund line is `cancellation_policy_details_note_6`. **NOL World is Yanolja's travel platform. These may govern the STAY booking flow, not the TICKET checkout.** The methods and the KRW-only refund are verified as present in the bundle; **they are NOT verified as governing ticketing.**
> 2. **A live "NOL World X UnionPay — Save Up to ₩40,000" promotional banner is on the page.** That **contradicts** the relayed claim that "UnionPay gets rejected on some events" — which came from an unverified commercial blog. **The first-party promo wins. Do not repeat the rejection claim.**

### Buying signals
- 💰 **A self-itemised ₩8,000 cross-border booking fee** naming payment cost as a component
- 🛂 **Passport eKYC on the global side; Korean phone number required domestically**
- 🧩 **Seven-plus payment counterparties, each integrated point-to-point**, plus a self-run PG licence
- 💳 **Instalments — the top Korean conversion lever — blocked on every wallet**
- 🌏 **KRW-only presentment with FX pushed onto the foreign issuer** (subject to caveat 1 above)

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Interpark Ticket` to draft the 12-touch sequence.*

**Six instructions for whoever drafts it:**
1. **The ₩8,000 fee notice is the opener.** It is their own document, to their own promoters, itemising payment cost. Nothing else in this file comes close.
2. ⛔ **Do NOT pitch replacing their Korean PG.** Korea's domestic acquiring is entity-gated; KG Inicis and Toss Payments stay. **The sellable surface is the cross-border leg only.** Getting this wrong marks us as not understanding the market.
3. **Motion is in-house.** They built it and licensed it. Anchor on reach and opportunity cost.
4. **Call them NOL Universe / NOL 티켓**, not Interpark Triple.
5. **Do not assert the KRW-only claim for ticketing** until someone confirms those strings govern the ticket checkout and not the stay flow. **Use the ₩8,000 fee and the eKYC gate instead — both are unambiguous.**
6. **Do not say PayPal. Do not say UnionPay is rejected.** Both are contradicted by the live page.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 10 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ⚠️ **Weakest-evidenced row on the account.** Korea's largest ticketing platform; ticket 거래액 reportedly passed **₩1 trillion in 2023**, then +11% (2024) and +7% (2025) → **~₩1.19tn (~US$850m) GMV**, all `[UNVERIFIED — search summaries; the arithmetic is the agent's]`. **The gate cannot fire — no sourced sub-40k figure exists** — and a ₩1tn-scale ticketing platform clears 100k/month by a wide margin. **But note the asymmetry: the payment evidence here is excellent and the volume evidence is not.** |
| Orchestration status | **+1** | ✅ **In-house, on affirmative evidence.** They are the licensed PG; they run their own wallet and token vault; **two card PGs contracted in parallel for one identical scope** means routing/failover is a decision made inside their own code; and seven-plus counterparties are integrated point-to-point with no unifying layer. |
| 3+ countries | **0** | ⬜ **Deliberately not awarded**, consistent with how eplus was scored. NOL Universe is a **single Korean entity selling into Korea**. The global storefront is cross-border *selling*, not a multi-country footprint. ⚠️ **If this row were read as "sells cross-border into 3+ countries", this account is 13/29.** Flagging rather than quietly choosing the higher number. |
| Multiple PSPs | **+2** | ✅ **The best-evidenced PSP row in this repo** — eight-plus counterparties named in a legally-mandated disclosure I read in full, including two card PGs on one line for one scope. |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **Honestly zero.** Korea is the only market and domestic rail coverage is **comprehensive** — every major wallet, carrier billing, virtual accounts, gift certificates. **There is no local rail gap. The gap is the cross-border leg**, which this row does not measure. Awarding here would be dishonest. |
| Recent expansion | **0** | ⬜ The NOL rebrand is not expansion. |
| Payment issues reported | **+2** | ✅ **First-party and verified by me** — the ₩8,000 fee notice explicitly attributes the increase to 「Fraud Detecting System 지원 결제프로세스」, i.e. they raised a customer-facing fee because of payment and fraud cost. Plus the passport-eKYC gate and the 1-year domestic re-verification requirement, both from the same verified document. **Stronger than any complaint thread.** |
| Funding >$10M | **0** | ❌ Private, Yanolja-owned. No round. |
| High traffic outside home | **0** | ⬜ No traffic data. Foreign demand is obviously material (it is why the global storefront and the ₩8,000 fee exist) but **no share figure exists.** |
| Competitor using orchestration | **0** | ❌ Not established for Yes24, Melon Ticket, Ticketlink or any Korean peer. |
| Payment job postings | **0** | ⬜ Not found. |

**Tier: 10 / 29 → 🟢 Medium.** Clears the ≥10 outreach bar. No override applied.

> **The score and the account quality diverge sharply here, and it is worth understanding why.** Three rows are zero *because the account is good at those things* — comprehensive domestic rails, a single-country footprint, no funding event. **The 29-point matrix is built to find under-served multi-market merchants, and Interpark is a well-served single-market merchant with one specific, expensive, self-documented cross-border problem.** A 10/29 with a verbatim first-party admission of cross-border payment cost is a better conversation than several higher scores in this repo.

### Source Notes
- ✅ **The 위탁 disclosure table was fetched and read in full by me**, confirming KG Inicis + Toss Payments on one line, plus Hecto Financial, Naver, Kakao Pay, PAYCO, Viva Republica, KG Mobilians, Galaxia Moneytree, Coocon and AWS.
- ✅ **The ₩8,000 fee notice, the eKYC/passport gate, the Korean-passport exclusion and the 1-year domestic expiry were all verified verbatim by me.**
- ✅ **The redirect chain `globalinterpark.com` → `world.nol.com` was verified by me**, as were the three `order_page_*` payment strings, the KRW refund string, and **zero PayPal occurrences**.
- 🚩 **Two corrections I issued against the research** (see Section 1): the `order_page_*` strings sit in an **accommodation** string block and may not govern ticketing; and a live **"NOL World X UnionPay"** promo contradicts the relayed UnionPay-rejection claim.
- ⚠️ **The stub's "~$500M revenue" is defensible but MISLABELLED.** NOL Universe FY2025 revenue ₩699.9bn ≈ US$500m — but that is **group-level revenue across travel, accommodation and ticketing**, and it is **commission revenue, not GMV**. **Never say "Interpark Ticket does ~$500M revenue."** `[UNVERIFIED — search summary]`
- ⚠️ **Domestic issuer lists come from a 2023 Wayback snapshot** — the live 결제방법 page is a React SPA rendering nothing server-side. Treat issuer detail as indicative.
- ⚠️ **국민일보 has argued Yanolja/Interpark's ticket statistics are 「꼼수」 (massaged).** `[UNVERIFIED]` — **worth knowing before quoting their GMV numbers back at them.**
- ⚠️ **All complaint threads are search-summary only** — 뽐뿌, PGR21, and the K-pop fan guidance about 3DS and declines. **Do not quote any of it.**
- ❌ **Which PSP processes the GLOBAL transactions is NOT ESTABLISHED.** This is the single biggest commercial gap. Plausibly the same KG Inicis/Toss rails with foreign-card MIDs, but **no evidence either way.**

### Manual Research Recommendations
> **1. Find the PSP behind `world.nol.com`.** Fetch its own privacy/terms pages and inspect a live global checkout. It is the one thing that would make the pitch precise.
> **2. Settle whether the `order_page_*` strings govern ticketing or stays.** The KRW-only argument depends entirely on it.
> **3. Confirm the 무이자 할부 wallet exclusion** from a live page — it is a strong secondary observation.
> **4. Get ticket GMV from a primary source** (DART 감사보고서 or an NOL Universe press release) rather than derived growth rates.

---

## Executive Summary

Interpark Ticket — now **NOL 티켓**, operated by **(주)놀유니버스 NOL Universe**, not the "Interpark Triple" of the stub — is Korea's largest event-ticketing platform. Its domestic payment coverage is **comprehensive**, with every major Korean wallet, carrier billing through two vendors in parallel, virtual accounts, gift certificates and its own PIN-checkout wallet, all sitting on **two card PGs (KG Inicis and Toss Payments) contracted on one line for one identical scope** — verified by me in their legally-mandated processor disclosure, which also shows **no foreign payment processor anywhere** and exactly one overseas data recipient. They are the licensed PG themselves. **So the domestic story is not the opportunity; the cross-border leg is** — and they have already measured it and written it down. Their own merchant-facing notice charges foreign buyers a **₩8,000 per-ticket booking fee** and itemises it as covering *payment processing fees*, identity verification, fraud prevention and **running a second global booking system**, alongside a **passport-based eKYC gate** that Korean passports cannot pass and a domestic gate that requires a Korean mobile number. At **10/29** the matrix scores this account low precisely because it is well-served domestically and operates in one country — but a verbatim, first-party, quantified admission of cross-border payment cost is a stronger opening than most higher scores in this repo.

</details>
