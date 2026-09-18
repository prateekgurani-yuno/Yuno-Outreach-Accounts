# Interpark Ticket (NOL 티켓)

**Status:** 🟢 Ready to outreach — 12-touch sequence drafted
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

### Pain Vector Extraction

```
=== PAIN VECTOR EXTRACTION ===

Motion: IN-HOUSE, and unusually so — they hold the PG licence themselves.
        Respect it completely. The pitch is NOT their domestic stack, which is
        excellent and entity-gated anyway. The pitch is the cross-border leg,
        and they have already costed it in writing.

Observable setup facts (verified first-hand, 2026-09-18):
- Merchant-facing notice, verbatim: 「본인인증이 적용된 상품은 예매수수료 8,000원이
  적용됩니다. 예매수수료는 웹사이트 운영, 결제수수료 외에도 본인인증/부정예매방지 및
  글로벌 예매 시스템 운영 비용이 포함돼 있습니다.」
  — a ₩8,000 global booking fee, itemised as covering PAYMENT PROCESSING FEES,
  identity verification, fraud prevention and running a SECOND booking system
- Stated cause of the increase: 「Fraud Detecting System 지원 결제프로세스 및
  부정예매 방지 기술 도입에 따른 예매수수료 인상」
- Global eKYC mandatory since 2024-07-01 for concerts and musicals; passport
  required; one passport per account; 「대한민국 여권으로는 본인인증을 할 수 없습니다」
- Domestic 본인인증 gained a 1-year expiry on 2024-07-11; expired customers
  cannot book until they re-verify; it runs on a Korean mobile number
- Processor disclosure names ㈜KG이니시스 AND 토스페이먼츠 on ONE line for ONE
  identical scope, plus Hecto Financial, Naver, Kakao Pay, PAYCO, Viva
  Republica, KG Mobilians, Galaxia Moneytree, Coocon — 8+ counterparties
- The 국외이전 table discloses exactly ONE overseas recipient: Braze, for CRM.
  No foreign payment processor anywhere.
- globalinterpark.com and ticket.interpark.com/global both 301 to world.nol.com

Selected observations for Phase 1 (E1 bullets, ranked by materiality):
1. Their own fee itemisation -> "Your global booking fee notice puts ₩8,000 a
   ticket against website operation, payment processing, identity verification
   and running a second booking system."
   MATERIALITY: highest in the entire batch. It is their own document, to their
   own promoters, and it means we are not hypothesising a pain point — they
   have measured it and written it down. Nothing else here comes close.
2. The passport gate -> "Global buyers need passport eKYC before they can book
   a concert, and a Korean passport can't be used there at all."
   MATERIALITY: high. Structural, first-party, and it explains the fee.

   HELD AT 2. The dual-PG point is saved for E3 backing logic, and the
   instalment-on-wallets exclusion for LK4.

Bridge variant: SKIP.
Rationale: the observations already bridge. A merchant that has itemised its own
cross-border payment cost does not need to be told that setups like theirs
"usually come with limitations" — they have written the limitation down. Adding
a stock bridge line after their own number would read as padding.

Hypothesis for Phase 2 (E3):
The domestic stack is genuinely well built, and the cross-border leg is running
as a second system with its own fee, its own identity gate and its own booking
platform — because the domestic rails could not be extended to foreign buyers.
Backing logic: two card PGs contracted in parallel for one identical scope,
eight-plus payment counterparties integrated point to point, a self-run PG
licence, and not one foreign payment processor in the cross-border disclosure.
That is a stack built to serve Korea extremely well. The foreign demand then
had to go somewhere, and it went into a parallel system that customers are
being charged ₩8,000 a ticket to run.

Success case for Phase 3 (E4):
Selected case: inDrive
Tier: 2 — same payment pattern (cross-border coverage expansion), different
      industry. STATED AS SUCH.
Match rationale: the question here is reach into foreign demand, not approval
mechanics and not operational load. inDrive's "10 new countries in under 8
months" is the number that answers "how fast could the foreign leg actually be
served properly." Wingo and Livelo both prove approval-rate mechanics, which
is not this account's problem.
Numbers: ~90% approval rate · 10 new countries live in under 8 months ·
50+ countries through one integration
Optional benchmark: SKIP. The ~8% figure is Yuno's own blog.

Touch-by-touch angles:
- E2 angle: the ₩8,000 fee -> ONE mechanism: the foreign leg served through the
  same layer rather than as a parallel system, so cross-border acceptance stops
  being a separate platform with separate costs
- LK1 angle: the fee itemisation, one sentence
- LK2 angle: the domestic stack is excellent and the foreign leg is a second system
- LK3 angle: inDrive — 10 new countries in under 8 months
- LK4 angle: FRESH — 무이자 할부 unavailable on every wallet they support
- E8 angle: clean exit

*** NEVER ***
- NEVER pitch replacing their Korean PG. Domestic acquiring is entity-gated;
  KG Inicis and Toss Payments stay. Getting this wrong marks us as not
  understanding the market, and it is the fastest way to lose this thread.
- NEVER say "Interpark Triple." It is NOL Universe / NOL 티켓.
- NEVER say PayPal is on the global site. Zero occurrences on the live page.
- NEVER say UnionPay is rejected. A live NOL World X UnionPay promo says otherwise.
- NEVER assert KRW-only presentment for TICKETING. Those strings sit in an
  accommodation block and may govern stays. Use the ₩8,000 fee instead.
- NEVER quote "Interpark Ticket does ~$500M revenue." That figure is
  group-level NOL Universe commission revenue, not ticketing, and not GMV.
```

**Calendar.** Day 1 anchored to **Monday 2 November 2026**, clearing Korea's autumn holiday
cluster — **Chuseok (24–26 Sep)**, **National Foundation Day (3 Oct)** and **Hangeul Day
(9 Oct)** — entirely rather than threading between them. No Korean public holiday falls
inside 2 Nov – 2 Dec.

**Times are KST (UTC+9), IST+3:30.** Per the rulebook Korea gets afternoon-local slots so they
land as late morning for Prateek — every slot is **14:00–16:00 KST = 10:30–12:30 IST**.

---

### Phase 1 — Curiosity (Days 1–5)

#### Touch 1 — Email 1 · Day 1 · Mon 2 Nov

**Subject:** Your ₩8,000 global booking fee

```text
Hey {{recipient.first_name}},

Spent some time on NOL 티켓's payment setup. Two things stood out:

- Your global booking fee notice puts ₩8,000 a ticket against website operation, payment processing, identity verification and running a second booking system.
- Global buyers need passport eKYC before they can book a concert, and a Korean passport can't be used there at all.

I work at Yuno — top-100 fintech, a16z-backed. We consider ourselves the 'everything payments' platform: one integration, every PSP, every method, every market.

Rather than pitch you based on assumptions, is there anything payment-related you're working through that we might be able to help with?

Best,
Prateek
```

#### Touch 2 — Email 2 · Day 3 · Wed 4 Nov · REPLY IN THREAD

```text
Hey {{recipient.first_name}},

Following up — wanted to put a bit more behind what Yuno actually does, and how it would address what I flagged.

- We sit above your existing providers. Additive, and your domestic stack doesn't move.
- The foreign leg runs through the same layer as everything else, rather than as a separate platform with its own costs.
- Cards issued abroad get acquired closer to the issuer, which is usually where the approval difference on cross-border sits.
- Adding a foreign-market method becomes configuration rather than a new integration.

To be explicit about what I'm not proposing: nothing about KG Inicis or Toss Payments. Korean domestic acquiring is where it needs to be, and it isn't the part I'd have anything useful to say about. It's the foreign-demand leg — the one you're currently charging ₩8,000 a ticket to run — that I'd be curious about.

I'll keep sharing what I'm seeing every few days. If your stack's where you want it, just say the word and I'll back off — otherwise happy to go deeper.

Cheers,
Prateek
```

#### Touch 3 — LinkedIn message 1 · Day 5 · Fri 6 Nov

```text
Hey {{recipient.first_name}} — figured I'd flag this here too in case more useful than email. Quick one: your own promoter notice itemises the ₩8,000 global booking fee as covering payment processing, identity verification and running a second booking system. Curious if that maps to anything you're working through on the payments side.
```

---

### Phase 2 — Diagnosis (Days 7–9)

#### Touch 4 — Email 3 · Day 7 · Tue 10 Nov · NEW EMAIL

**Subject:** Read on your cross-border leg

```text
Hey {{recipient.first_name}},

Going to take a swing at this — based on what I see, my read is that the domestic stack is genuinely well built, and the foreign leg ended up as a second system because the domestic rails couldn't be extended to buyers outside Korea.

What points that way is how thorough the domestic side is. Two card PGs contracted in parallel for the same scope, virtual accounts, carrier billing through two vendors, four wallets, your own PIN-checkout wallet. That's a lot of deliberate work, and none of it reaches a fan in Jakarta or Taipei.

So the foreign demand went somewhere else — a separate platform, a passport gate, and a fee that you've itemised yourself.

At Yuno (a16z-backed, top-100 fintech), we sit above your existing providers so the foreign leg runs through the same layer as the domestic one — keep your stack, add what's missing.

Thursday is open for me — would 14:00 or 15:00 your time work for a quick 15 minutes?

Best,
Prateek
```

#### Touch 5 — LinkedIn message 2 · Day 9 · Thu 12 Nov

```text
Hey {{recipient.first_name}} — sent a longer note over email this week. Short version: the domestic stack is excellent and the foreign leg is a second system with its own fee and its own identity gate. If that's anywhere on your radar, would Monday the 16th at 15:00 your time work for a quick 15?
```

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · Mon 16 Nov · NEW EMAIL

**Subject:** How inDrive added 10 countries in 8 months

```text
Hey {{recipient.first_name}},

On the read I shared last week — an example of what solved looks like. It's mobility rather than ticketing, and I've picked it on purpose: the airline and retail cases in our library prove approval-rate mechanics, and your question isn't approval, it's reach into foreign demand.

inDrive put Yuno above its existing providers:

- 10 new countries live in under 8 months (you read that right)
- ~90% approval rate across the estate
- 50+ countries running through one integration

Same layer above their existing stack — no rip-out, and in your case nothing domestic would change at all.

One thing I'm genuinely curious about: when you sized the ₩8,000 fee, roughly how much of it was the payment leg versus the identity and fraud tooling? Those usually move very differently once the foreign flow isn't a separate system.

Wednesday the 18th is open — would 16:00 your time work?

Full case here if useful: https://y.uno/en/success-stories/indrive

Thanks,
Prateek
```

#### Touch 7 — Email 5 · Day 13 · Wed 18 Nov · ⚠️ MANUAL

> **Placeholder — Prateek writes this one.**
>
> **Suggested angle:** the proxy-buying industry. A paid service sector exists specifically to
> buy Korean concert tickets on behalf of foreign fans, and it markets itself on exactly this
> failure — Korean-only on-sales and declined foreign cards. ⚠️ **Verify at least one such
> service's marketing copy first-hand before referencing it**; everything we have on this is
> search-summary level. Framed carefully, "there is a business model built on your checkout
> being hard to use from abroad" is a very strong, non-insulting observation.

#### Touch 8 — Email 6 · Day 15 · Fri 20 Nov · ⚠️ MANUAL

> **Placeholder — different format from E5.**
>
> **Suggested angle:** a two-column comparison of the domestic method set against the global
> one, built entirely from their own pages. Domestic: four wallets, carrier billing, virtual
> accounts, gift certificates, instalments. Global: card, Alipay, WeChat Pay. **The asymmetry
> is the argument.** ⚠️ **Confirm the global method list governs ticketing before using it —
> see the caveat in Section 1.**

#### Touch 9 — LinkedIn message 3 · Day 17 · Tue 24 Nov

```text
Hey {{recipient.first_name}} — inDrive went live in 10 new countries in under 8 months on one integration, without touching their existing domestic setup. Worth 15 minutes to see if it maps to your foreign leg? Thursday the 26th at 14:30 your time is open.
```

---

### Between Phases (Day 19)

#### Touch 10 — Email 7 · Day 19 · Thu 26 Nov · ⚠️ MANUAL

> **Placeholder — manual creative bridge.**
>
> **Freshest unused anchor:** the **1-year domestic 본인인증 expiry** introduced 11 July 2024.
> An existing, verified, paying customer is silently blocked from booking the moment it
> lapses — on a product where the on-sale window is measured in seconds. **That is a
> conversion question, not a payments one, which is exactly why it is an interesting thing
> for a payments person to raise.**

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21 · Mon 30 Nov

```text
Hey {{recipient.first_name}} — last LK ping from me on this. One thing I keep coming back to: 무이자 할부 is the biggest lever you have on a ₩200,000 ticket, and it's unavailable on every wallet you support. If timing works, Wednesday the 2nd at 15:30 your time is open for a quick 15.
```

#### Touch 12 — Email 8 · Day 23 · Wed 2 Dec · REPLY IN THREAD to E3

```text
Hey {{recipient.first_name}},

Going to stop pinging unless you want to pick this back up.

You're heading into year-end on-sales, which is the worst possible time to open a payments workstream. If timing's just off, happy to circle back in the new year.

If it ever comes back up, just reply here — and if the global side sits with a different team, happy to be pointed there.

All the best,
Prateek
```

---

### ⚠️ Send-time checklist

1. ⛔ **Never pitch replacing the Korean PG.** Entity-gated. E2 says so explicitly and that line is load-bearing — it is what proves we understand the market.
2. ⛔ **Never say Interpark Triple.** NOL Universe / NOL 티켓.
3. ⛔ **Never say PayPal; never say UnionPay is rejected.** Both contradicted by the live page.
4. ⛔ **Never quote the ~$500M figure** as Interpark Ticket revenue.
5. ⚠️ **Do not use the KRW-only argument** until someone confirms those strings govern ticketing rather than stays.
6. ⚠️ **Re-verify the ₩8,000 notice is still live** at `tmanager.interpark.com/html/reservationFee.html` before Touch 1. It is the entire opener.
7. ⚠️ **Re-read the ICP judgement call at the top of this file.** If Prateek decides the self-held PG licence routes this to Partnerships, **this sequence must not send.**

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
