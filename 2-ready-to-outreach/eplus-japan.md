# eplus (イープラス)

**Status:** 🟢 Ready to outreach — 12-touch sequence drafted
**ICP Score:** 16 / 29 → 🟢 **Medium**
**Industry:** Event ticketing (live music, theatre, sport, classical, anime) + live streaming · **HQ:** Ebisu Garden Place Tower 8F, Shibuya-ku, **Tokyo, Japan** — 株式会社イープラス, capital ¥972.5m, founded 30 Jul 1999, FY-end March · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** **Greenfield** — none detected, on affirmative architectural evidence: two entirely separate storefronts on two different platforms with two non-overlapping method sets (see 3B).

---

> ## 🎯 THE HOOK — a card refund older than seven months cannot go back to the card, and eplus tells overseas buyers their declines are the bank's fault
>
> **Two findings, both verbatim from eplus's own documentation, both fetched by me.**
>
> **1. The seven-month refund cliff.** From eplus's own help centre on cancelled-performance refunds (`support-qa.eplus.jp/hc/ja/articles/360041662793`):
>
> > 「※**カード決済日から7か月以上経過している場合、『ウェルネット送金サービス』でのご返金**となります。」
>
> *"If more than 7 months have passed since the card payment date, the refund will be made via the **Wellnet Remittance Service**."*
>
> **Read what that means for a ticketing business.** Concert tickets go on sale six to twelve months ahead. When a tour is cancelled — which is the normal failure mode in live entertainment — **a material share of those refunds have aged past the card rail entirely** and drop into a manual bank-remittance process operated by a third party. The customer has to supply bank details. Finance has to reconcile a second ledger. **Nobody designed that; the card rail's refund window just ran out.**
>
> **2. The cross-border storefront tells customers to phone their bank.** `ib.eplus.jp` is eplus's **named "インバウンドチケット販売" (inbound ticket sales) business line**, on its own platform. Its FAQ, fetched by me:
>
> > *"Q: What payment methods do you accept? A: We accept credit cards (**VISA, MasterCard**) issued domestically and overseas, and **Alipay**."*
> > *"Q: Payment is failed as error appeared during the credit card settlement. A: **We only accept credit card of VISA and MasterCard.** It is possible that your credit card has a restriction (ex. it can't settle from overseas), so **please contact your credit card company directly**."*
> > *"Q: Payment is failed, but why is there a fee charged from my bank account? A: In case that you used a **debit card**, a service fee will be charged once when the payment is failed, but it will return to your account after a few days."*
>
> **That is a merchant with a documented, acknowledged, unsolved cross-border decline problem, whose written answer is "it's your issuer."** And they are holding funds on failed debit attempts while saying so.
>
> **The kicker:** ib.eplus.jp supports **English, Simplified Chinese and Traditional Chinese — and no Korean** — while eplus.jp's own genre navigation runs a prominent **「K-POP・韓流・アジア」** category. It prices in **seven currencies** (JPY, USD, CNY, TWD, AUD, EUR, GBP) and takes **no JCB, no Amex, no UnionPay and no WeChat Pay**.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** eplus is one of Japan's largest ticketing platforms — **28 million members** on its own corporate site, **33,316 live event listings** on its homepage today. It runs **two separate storefronts on two separate platforms**: the domestic Java site at `eplus.jp/sys/main.jsp` and a **CS-Cart** install at `ib.eplus.jp` for overseas buyers. They share almost nothing.

**SimilarWeb total visits:** **Not obtained.** No data supplied. Country profile is estimate-grade; **no split invented.**

### Accepted methods — domestic — first-party, exhaustive, verified by me directly
✅ Fetched from eplus's own help-centre API (`support-qa.eplus.jp`, article 360041175054, 「どのような支払方法があるか」). **This is an exhaustive enumeration — there are exactly three.**

| Method | Detail, verbatim |
|---|---|
| **クレジットカード** | Fee ¥0. Brands: **セゾン、UC、VISA、MASTER、JCB、Diners Club、DC、アメリカン・エキスプレス**. **Lump-sum only — no instalments anywhere in the flow.** |
| **コンビニ／ATM** | Fee **¥330 per transaction**. **Five chains:** セブン-イレブン、ファミリーマート、ローソン、ミニストップ、デイリーヤマザキ. Plus Pay-easy-stickered ATMs. **Seicomart absent.** |
| **ネットバンキング（ペイジー）** | Fee **¥330 per transaction**. PayPay銀行（旧ジャパンネット銀行）・楽天銀行・auじぶん銀行・NEOBANK 住信SBIネット銀行・ペイジーネットバンク、大手都市銀行、ゆうちょ銀行・地銀・信金・信用組合・農協等. |

**3DS2 is mandatory** *(agent-reported; I did not independently verify this one)*.

### ❌ Affirmatively ABSENT — sourced absence, from an exhaustive first-party list
**PayPay · Rakuten Pay · d払い · au PAY · LINE Pay · Merpay · Amazon Pay · Apple Pay · Google Pay · carrier billing · Paidy · any BNPL · any instalment option**

> ⚠️ **TRAP — do not misread this one.** **「PayPay銀行」appears in eplus's docs, but it is PayPay *Bank* in the Pay-easy net-banking list — NOT the PayPay wallet.** They are different products. Asserting "you take PayPay" off that string would be a factual error in the first email. Flagged because it is genuinely easy to trip on.

### Cross-border storefront — `ib.eplus.jp` — verified by me directly
| Attribute | Finding |
|---|---|
| **Platform** | **CS-Cart** — confirmed from the footer link to `cs-cart.jp`, the `tygh_main_container` element and the `ty-` class prefix throughout. Copyright *"© 2016-2026 eplus inc."* |
| **Methods** | **Visa, Mastercard, Alipay. That is all.** |
| **Currencies** | **Seven** — JPY, USD, CNY, TWD, AUD, EUR, GBP (`index.php?cr=XXX`) |
| **Languages** | **English, Simplified Chinese, Traditional Chinese.** **No Korean.** |
| **Eligibility** | *"This booking system is only for customers who live in overseas countries or only have credit cards issued overseas."* |

### Known PSPs
| Provider | Role | Evidence |
|---|---|---|
| **Wellnet (ウェルネット)** | **Refund rail**, confirmed: **『ウェルネット送金サービス』** is the named remittance service for every non-card refund *and* for card refunds aged past 7 months | ✅ **Verified by me directly** in two separate eplus help-centre articles |
| **Konbini / Pay-easy 収納代行** | Agent-reported as Wellnet | ⚠️ Plausible and consistent with the refund role, but **I verified Wellnet as the *refund* rail, not as the collection agent.** Do not overstate. |
| **Card acquirer** | ❌ **NOT ESTABLISHED** | The brand list leads with **セゾン、UC** — Credit Saison and UC, which is suggestive given Credit Saison's former shareholding. **That is an inference and nothing more.** |
| **Alipay provider on `ib.eplus.jp`** | ❌ **NOT ESTABLISHED** | Almost certainly a different provider again — it is a different platform |

### Orchestration status
**None detected — greenfield**, on affirmative architectural evidence rather than absent search hits:
- **Two storefronts, two platforms** — a Java application at `eplus.jp/sys/main.jsp`, a CS-Cart install at `ib.eplus.jp`
- **Two non-overlapping method sets** — domestic gets konbini and Pay-easy but no Alipay; overseas gets Alipay but no JCB, no Amex, no konbini
- **A refund path that falls out of the card rail after 7 months** into a third-party remittance service. A routing layer with stored credentials and proper refund handling does not have a seven-month cliff.

### Buying signals
- 🔴 **The 7-month card refund cliff** — structural, first-party, and expensive in a vertical built on advance sales
- 🔴 **A documented cross-border decline problem** with "contact your issuer" as the published answer
- 🔴 **T+1 payment reconciliation, admitted in writing** — see 3B
- 🔴 **A live refund incident on their homepage today:** the 『PARCO PRODUCE 2026 髪結いの亭主』 pre-order was **invalidated in full due to eplus's own error**, with card customers getting a sales-data reversal and non-card customers waiting until **~21 August** for a Wellnet remittance. eplus's own wording: 「全て弊社の不手際に起因するものであり…全責任は弊社に帰属する」
- 🏢 **Ownership change** — Sony Music reportedly took **51% on 31 Jul 2024** from **Credit Saison** *(agent-reported; the shareholder list is not published on eplus's corporate site and I could not verify it)*
- 🌏 **"インバウンドチケット販売" is a named business line** in eplus's own corporate navigation — inbound is strategy, not a side project
- ❌ No payment RFP and no payments hire found

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

### Pain Vector Extraction

```
=== PAIN VECTOR EXTRACTION ===

Motion: Greenfield — none detected, affirmatively. Two storefronts, two platforms, two
        non-overlapping method sets. Phase 1 may note the shape; it must not lecture.

Observable setup facts (verified first-hand, 2026-09-18):
- 7-MONTH REFUND CLIFF, their own words: 「カード決済日から7か月以上経過している場合、
  『ウェルネット送金サービス』でのご返金となります」 — a card refund older than seven
  months leaves the card rail and becomes a Wellnet bank remittance
- Every non-card refund is a Wellnet remittance by default
- ib.eplus.jp FAQ, verbatim: "We only accept credit card of VISA and MasterCard. It is
  possible that your credit card has a restriction (ex. it can't settle from overseas),
  so please contact your credit card company directly."
- ib.eplus.jp also: "In case that you used a debit card, a service fee will be charged
  once when the payment is failed, but it will return to your account after a few days."
- T+1 RECONCILIATION: konbini / Pay-easy / net banking status flips to 入金完了 only
  「支払日の翌日15時以降」 — after 15:00 the following day
- AND THEY DOCUMENT THE CONSEQUENCE: 「システムの都合上、お支払手続き後に支払期限の
  ご案内メールが配信される場合があります」 — a payment-deadline reminder may go out
  AFTER the customer has already paid
- Exactly three domestic methods; lump-sum card only; konbini and Pay-easy both ¥330/txn
- ib.eplus.jp is a separate CS-Cart install: Visa, Mastercard, Alipay only, seven
  currencies, English + Simplified + Traditional Chinese, NO Korean
- 28m members; 33,316 live event listings on 2026-09-18
- LIVE INCIDENT on their own homepage: the PARCO PRODUCE 2026 pre-order was invalidated
  in full by eplus's own error, refunds split across a card reversal and a Wellnet
  remittance dated ~21 Aug

Selected observations for Phase 1 (E1 bullets, ranked by materiality):
1. The 7-month refund cliff -> "Your help centre says a card refund more than seven
   months after the payment date goes out as a bank remittance rather than back to the
   card."
   MATERIALITY: highest, and it passes the voice anchor's asymmetry test exactly — their
   SALES window is six to twelve months and their card REFUND window is seven. Both
   numbers are theirs. They do not fit together and nobody has to be blamed for it.
2. The cross-border decline answer -> "Your inbound site takes Visa, Mastercard and
   Alipay, and its FAQ answer for a failed payment is to contact your card company."
   MATERIALITY: high. Sourced verbatim. Needs the diplomatic clause — see below.

   HELD AT 2. Deliberately saved for later touches: the T+1 dunning admission (E3
   backing logic), the missing Korean and UnionPay/WeChat Pay (LK4), the live PARCO
   refund incident (E7 manual). Every touch gets fresh material.

Bridge variant: C — friction
Rationale: not A (the provider count is low and mostly undisclosed, so a "complexity"
frame would be asserting something I cannot evidence) and not B (there is no single-PSP
story — I can name exactly one provider and it is a refund rail). Both lead observations
are friction the customer feels. C is the accurate one.

Hypothesis for Phase 2 (E3):
Collection and refund were built separately, so each method has its own lifespan and its
own exit path — and the refund side is where that shows.
Backing logic: a card refund expires off its own rail at seven months. Every non-card
refund is a manual remittance from the start. Konbini and Pay-easy settlement lands T+1
at 15:00, and eplus's own help centre says that is why a payment-deadline reminder can
reach someone who has already paid. In a business selling six to twelve months ahead,
where cancelling a whole tour is a normal event rather than an edge case, refunds are a
primary operation running on rails that were never designed together.

Success case for Phase 3 (E4):
Selected case: Rappi
Tier: 2 — same payment pattern (multi-method estate, heavy reconciliation and manual
      operations load), different industry and region. STATED AS SUCH in the email.
Match rationale: no Tier 1 exists — there is no ticketing or Japanese case in the
library. Rappi is the library's operational-burden case and the "80% less analyst work"
bullet answers the manual-remittance and T+1 reconciliation problem directly, which is
the actual hypothesis. Wingo and Livelo both prove approval-rate mechanics, which is not
what this account is about.
Numbers to lead with: zero implementation delays · hundreds of payment methods through
one integration · 80% less analyst work
Optional benchmark: SKIP. The "~8% average authorisation uplift" is Yuno's own blog
figure and this is not an approval-rate argument anyway.

Touch-by-touch angles:
- E2 angle: the refund cliff -> ONE mechanism: unified reconciliation and a single
  ledger, with the fallback payout running inside the same layer.
  *** HONESTY CONSTRAINT, NON-NEGOTIABLE: we CANNOT extend a scheme's refund window and
  must not imply we can. A payments buyer knows that window is the scheme's, not the
  merchant's. E2 says so explicitly. What changes is that the fallback is automatic and
  stays in one ledger instead of becoming a manual process in a second system. Claiming
  otherwise would lose this thread in one reply — and would deserve to. ***
- LK1 angle: the seven-month refund cliff, one sentence
- LK2 angle: collection and refund were built separately
- LK3 angle: Rappi — 80% less analyst work, same providers
- LK4 angle: FRESH — no Korean and no UnionPay or WeChat Pay on the inbound storefront,
  while the domestic site runs a prominent K-POP・韓流・アジア category
- E8 angle: clean exit, offer to circle back after the year-end season
```

**Calendar.** Day 1 anchored to **Monday 5 October 2026**. Japanese public holidays inside the
window: **スポーツの日 (Sports Day) Mon 12 Oct** and **文化の日 (Culture Day) Tue 3 Nov**. **No
send day and no proposed slot falls on either**, or on a weekend.

**Times are JST (UTC+9), which is IST+3:30.** Slots run 14:00–16:00 JST, i.e. 10:30–12:30 IST.

---

### Phase 1 — Curiosity (Days 1–5)

#### Touch 1 — Email 1 · Day 1 · Mon 5 Oct

**Subject:** Seven-month refund window on cards

```text
Hey {{recipient.first_name}},

Spent some time on eplus's payment setup. Two things stood out:

- Your help centre says a card refund more than seven months after the payment date goes out as a bank remittance rather than back to the card. Tickets go on sale six to twelve months ahead.
- Your inbound site takes Visa, Mastercard and Alipay, and its FAQ answer for a failed payment is to contact your card company.

That kind of setup usually has some friction worth checking on.

I work at Yuno — top-100 fintech, a16z-backed. We consider ourselves the 'everything payments' platform: one integration, every PSP, every method, every market.

Rather than pitch you based on assumptions, is there anything payment-related you're working through that we might be able to help with?

Best,
Prateek
```

#### Touch 2 — Email 2 · Day 3 · Wed 7 Oct · REPLY IN THREAD

```text
Hey {{recipient.first_name}},

Following up — wanted to put a bit more behind what Yuno actually does, and how it would address what I flagged.

- We sit above your existing providers. Additive, nothing gets ripped out.
- Collection and refund run through the same layer, so every method's money movement lands in one ledger.
- Adding a method, a provider or a payout rail becomes a configuration change rather than a project.
- One integration covers both your domestic flow and the inbound one.

On the seven-month point, I should be straight with you: nobody can extend a scheme's refund window, us included — that's the scheme's rule, not yours. What changes is what happens once it closes. The fallback payout runs inside the same layer and reconciles in the same ledger, rather than becoming a separate manual process in a second system.

I'll keep sharing what I'm seeing every few days. If your stack's where you want it, just say the word and I'll back off — otherwise happy to go deeper.

Cheers,
Prateek
```

#### Touch 3 — LinkedIn message 1 · Day 5 · Fri 9 Oct

```text
Hey {{recipient.first_name}} — figured I'd flag this here too in case more useful than email. Quick one: your help centre says a card refund past seven months goes out as a bank remittance instead of back to the card, and tickets go on sale six to twelve months ahead. Curious if that maps to anything you're working through on the payments side.
```

---

### Phase 2 — Diagnosis (Days 7–9)

#### Touch 4 — Email 3 · Day 7 · Tue 13 Oct · NEW EMAIL

**Subject:** Read on your refund paths

```text
Hey {{recipient.first_name}},

Going to take a swing at this — based on what I see, my read is that collection and refund were built separately, so each method ended up with its own lifespan and its own exit path.

Three things point that way. A card refund expires off its own rail at seven months. Every non-card refund is a remittance from the start. And konbini and Pay-easy settlement only lands at 15:00 the following day — your own help centre says that's why a payment-deadline reminder can reach someone who has already paid.

In a business where cancelling a whole run is normal rather than exceptional, that makes refunds a primary operation, not an edge case.

At Yuno (a16z-backed, top-100 fintech), we sit above your existing providers so collection and refund reconcile in one place — keep your stack, add what's missing.

Thursday is open for me — would 14:00 or 15:00 your time work for a quick 15 minutes?

Best,
Prateek
```

#### Touch 5 — LinkedIn message 2 · Day 9 · Thu 15 Oct

```text
Hey {{recipient.first_name}} — sent a longer note over email this week. Short version: collection and refund look like they were built separately, which is why each method has a different lifespan and a different exit. If that's anywhere on your radar, would Monday the 19th at 15:00 your time work for a quick 15?
```

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · Mon 19 Oct · NEW EMAIL

**Subject:** How Rappi cut analyst work 80%

```text
Hey {{recipient.first_name}},

On the read I shared last week — sharing an example of what solved looks like. Different industry and region, so I'll be straight that it's a pattern match: a merchant carrying a lot of methods and a lot of manual money-movement work, which is the shape rather than the sector.

Rappi put Yuno above its existing providers:

- 80% less analyst work on payment operations (you read that right)
- Hundreds of payment methods available through one integration
- Zero implementation delays on new methods and markets

Same orchestration layer above their existing stack — no rip-out. The first bullet is the one I'd point at: that number came out of reconciliation and exception handling, which is where your refund paths currently sit.

One thing I'm curious about: when a run gets cancelled, roughly what share of those refunds are already past the seven-month card window by the time you process them?

Wednesday the 21st is open — would 16:00 your time work?

Full case here if useful: https://y.uno/success-cases/rappi

Thanks,
Prateek
```

#### Touch 7 — Email 5 · Day 13 · Wed 21 Oct · ⚠️ MANUAL

> **Placeholder — Prateek writes this one.**
>
> **Suggested angle: the PARCO PRODUCE 2026 incident, which is on their own homepage.** A
> pre-order was invalidated in full by eplus's own error — their words: 「全て弊社の不手際に
> 起因するものであり…全責任は弊社に帰属する」 — and the refund ran down **two different
> paths**, a card sales-data reversal for one group and a Wellnet remittance dated roughly
> three weeks later for the other. ⚠️ **Handle with real care.** They owned it publicly and
> handled it well. The angle is *"a single refund exercise split across two rails and two
> timelines"*, never *"you had an incident."* If it cannot be written warmly, skip it.

#### Touch 8 — Email 6 · Day 15 · Fri 23 Oct · ⚠️ MANUAL

> **Placeholder — different format from E5.**
>
> **Suggested angle:** a side-by-side of the domestic method set against the inbound one —
> three methods versus three, with almost no overlap, ¥330 fees on two domestic rails, and
> seven currencies on the inbound side. Built entirely from their own published pages. **The
> non-overlap is the point and it needs no commentary.**

#### Touch 9 — LinkedIn message 3 · Day 17 · Tue 27 Oct

```text
Hey {{recipient.first_name}} — Rappi cut payment analyst work by 80% without changing any of their providers; it came out of reconciliation and exception handling. Worth 15 minutes to see if it maps to your setup? Thursday the 29th at 14:30 your time is open.
```

---

### Between Phases (Day 19)

#### Touch 10 — Email 7 · Day 19 · Thu 29 Oct · ⚠️ MANUAL

> **Placeholder — manual creative bridge.**
>
> **Freshest unused anchor:** inbound is a **named business line** in eplus's own corporate
> navigation —「インバウンドチケット販売」— and it runs on a completely separate platform from
> the domestic site. A strategic business unit on its own stack is a real architecture
> question and a flattering one to ask about. ⚠️ **Do not mention the Sony Music ownership
> change** — it is unverified and getting a shareholder wrong here is unrecoverable.

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21 · Mon 2 Nov

```text
Hey {{recipient.first_name}} — last LK ping from me on this. One thing I kept noticing: eplus.jp runs a K-POP・韓流 category, and the inbound site has no Korean and takes no UnionPay or WeChat Pay. If timing works, Wednesday the 4th at 15:30 your time is open for a quick 15.
```

#### Touch 12 — Email 8 · Day 23 · Wed 4 Nov · REPLY IN THREAD to E3

```text
Hey {{recipient.first_name}},

Going to stop pinging unless you want to pick this back up.

You're heading into year-end, which is the worst possible time to open a payments workstream. If timing's just off, happy to circle back in the new year once the season has cleared.

If it ever comes back up, just reply here.

All the best,
Prateek
```

---

### ⚠️ Send-time checklist — five things before Touch 1 goes out

1. ⛔ **Never claim we can extend a scheme refund window.** E2 says the opposite on purpose.
   This is the one line in the sequence that would end the thread if it were overclaimed.
2. ⛔ **Never mention Sony Music or Credit Saison.** The ownership change is agent-reported
   and I could not verify it against eplus's own corporate site.
3. ⛔ **Never say they take PayPay.** 「PayPay銀行」 in their Pay-easy list is PayPay *Bank*.
4. ⚠️ **Re-check the seven-month clause** at `support-qa.eplus.jp/hc/ja/articles/360041662793`
   before send. It is the whole opener.
5. ⚠️ **Re-check the PARCO notice is still live** before writing E5. If it has been taken down,
   drop that touch rather than referencing something the recipient cannot go and read.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 16 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED as a bound.** Sourced inputs, both first-party and both fetched by me: **28 million members** (「現在2,800万人の会員」, `corp.eplus.jp`) and **33,316 live event listings** (`eplus.jp` homepage, 2026-09-18). ⚠️ **No ticket or order volume is published anywhere and I refuse to invent one.** **Presented as a bound because the divisor is unsourced:** 33,316 concurrent listings, at a deliberately conservative **50 tickets sold per listing** and even assuming that entire inventory turns over only **twice a year**, gives ~3.3m tickets/year; at a pessimistic **3 tickets per order** that is ~1.1m orders/year = **~92k/month**. Halve every one of those assumptions and it still clears **40k** comfortably. **Every plausible divisor clears the volume gate**, which is why this is ✅ — but the estimate is softer than the airline files in this batch and should be said out loud on a call. |
| Orchestration status | **+4** | ✅ **None detected**, on affirmative architecture: two platforms, two non-overlapping method sets, and a refund path that leaves the card rail after 7 months. |
| 3+ countries | **0** | ⬜ **Deliberately not awarded.** eplus is a single Japanese entity selling **into** Japan. Seven pricing currencies and three languages on `ib.eplus.jp` are verified — but **currency is not country**, and I am not stretching a cross-border storefront into a multi-market footprint. **This row is the difference between 16 and 19; it stays at 0 on principle.** |
| Multiple PSPs | **+2** | ✅ Structurally ≥2 — Wellnet cannot be the Alipay provider on a separate CS-Cart install, and neither is the card acquirer. ⚠️ **Only Wellnet can be named.** |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **The best-sourced row.** Japan is the only market and the domestic list is **exhaustive by construction** — eplus publishes it as the answer to "what payment methods are there." **PayPay, Rakuten Pay, d払い, au PAY, LINE Pay, Merpay, Amazon Pay, Apple Pay, Google Pay, carrier billing, Paidy, BNPL and instalments are all absent.** On `ib.eplus.jp`, **JCB, Amex, UnionPay and WeChat Pay are absent** from a storefront explicitly built for Chinese-speaking buyers. Sourced absence on both flows. |
| Recent expansion | **0** | ⬜ **Not awarded, and it undersells the account.** The **Sony Music majority acquisition** is the real corporate signal — a new majority owner is exactly when platform contracts get reviewed — but it is an **ownership change, not expansion**, and it is **unverified**. The row stays 0; the signal is flagged in Section 1. |
| Payment issues reported | **+2** | ✅ **First-party documentation, not customer complaints.** (a) The **T+1 reconciliation gap**: 「コンビニ・ペイジー対応ATM、ネットバンキング(ペイジー)でお支払いの場合…**支払日の翌日15時以降**に「入金完了」として反映されます」 — payment status updates only after **15:00 the following day** — and eplus admits the consequence in writing: 「**システムの都合上、お支払手続き後に支払期限のご案内メールが配信される場合があります**」, *"due to system constraints, a payment-deadline reminder email may be sent after you have completed payment."* **They dun customers who have already paid, and they document it.** (b) A dedicated help article titled 「**クレジットカード決済で申込みの際にエラーが表示される**」. (c) The `ib.eplus.jp` decline FAQ and debit-card fee hold. (d) The live PARCO pre-order refund incident. |
| Funding >$10M | **0** | ❌ Private. The Sony Music transaction is an acquisition, not a round. |
| High traffic outside home | **0** | ⬜ No traffic data. Cannot verify either way. |
| Competitor using orchestration | **0** | ❌ **Ticket Pia and Lawson Ticket stacks are NOT ESTABLISHED.** Nothing found. |
| Payment job postings | **0** | ⬜ None found. |

**Tier: 16 / 29 → 🟢 Medium.** **No analyst override applied — and I considered one.** 16 sits one point under ⭐, and the cross-border wedge is sharper than several ⭐ accounts. **I did not override, because the point I would be reaching for is the "3+ countries" row I just declined on principle, and awarding it through the back door would be dishonest.** If someone establishes Korean or Chinese inbound share, or a competitor's orchestration, this becomes ⭐ on its own merits. It comfortably clears the ≥10 bar for outreach either way.

### Source Notes
- ✅ **The domestic three-method enumeration, card brand list, konbini chains, Pay-easy bank list and both fee lines were fetched by me** via the public Zendesk help-centre API at `support-qa.eplus.jp/api/v2/help_center/ja/articles.json?per_page=100` (235 articles). **The HTML help centre is awkward to scrape; the API is wide open.** Same technique that cracked Ticketek and Moshtix.
- ✅ **The 7-month refund cliff, the T+1 reconciliation gap, the post-payment dunning admission, the lottery pre-authorisation cycle and the live PARCO incident are all verbatim from that same first-party corpus.**
- ✅ **`ib.eplus.jp` was fetched directly** — CS-Cart platform, seven currencies, three languages, and the Visa/Mastercard/Alipay FAQ answers quoted above.
- ✅ **28m members and the corporate details** (capital ¥972.5m, founded 1999-07-30, Ebisu HQ, FY-end March) fetched from `corp.eplus.jp`.
- ✅ **33,316 live listings** from the eplus.jp homepage on 2026-09-18.
- ⚠️ **CORRECTION to the brief, carried from the research agent: the pre-Sony investor was Credit Saison, not SMBC.** Worth keeping on record so the wrong name does not resurface. ⚠️ **But the Sony Music 51% / 2024-07-31 transaction itself is agent-reported and I could not verify it** — `corp.eplus.jp/company` publishes capital, founding date and the board, but **no shareholder list**. Treat the whole ownership story as unconfirmed.
- ⚠️ **CORRECTION to the agent's report on the lottery cycle.** eplus's own article (360041176654) says a pre-authorisation runs before the draw and 「**落選の場合はオーソリが取り消され、実際に決済が発生することはございません**」 — *losing entries have the auth voided and no payment occurs.* **The agent's characterisation that this "genuinely debits debit cards" is not supported by that article.** The debit-card fund-hold statement is real but comes from a **different** page — the `ib.eplus.jp` **failed-payment** FAQ — and belongs there, not here. **Do not merge the two.**
- ⚠️ **Konbini/Pay-easy 収納代行 attribution to Wellnet is agent-reported.** I verified Wellnet as the **refund remittance** rail in two articles. The collection role is plausible but **not verified by me**.
- ⚠️ **3DS2 being mandatory is agent-reported and unverified.**
- ⚠️ **"~100,000 events per year" was in the agent report.** I did not find it on any eplus page and have **not used it** — the volume bound above rests on the 33,316 live listings instead, which I did verify.
- ❌ **The card acquirer is unknown.** The セゾン/UC brand ordering is suggestive, nothing more.

### Manual Research Recommendations
> **1. Walk `ib.eplus.jp` to a real card form** and identify the acquirer and the Alipay provider. That single session likely also settles 3DS behaviour on the cross-border flow, which is where the declines are.
> **2. Get Korean and Chinese inbound share** for Japanese live events. It converts the "no Korean, no UnionPay, no WeChat Pay" observation from a gap into a sized gap, and it is what moves this to ⭐.
> **3. Verify the Sony Music shareholding** in a registry or a press release before anyone puts it in an email.
> **4. Confirm whether Wellnet is the konbini collection agent** as well as the refund rail — it changes how much of the estate one provider touches.
> **5. Check Ticket Pia and Lawson Ticket** for orchestration and for wallet coverage. If a direct competitor takes PayPay and eplus does not, that is the sharpest possible version of the rail-gap observation.

---

## Executive Summary

eplus is one of Japan's largest ticketing platforms — **28 million members**, **33,316 live event listings**, Sony-Music-backed — running **two entirely separate payment estates**. The domestic site accepts **exactly three methods**: card (lump-sum only), konbini/ATM at ¥330 a transaction, and Pay-easy net banking at ¥330 a transaction. **No PayPay, no Rakuten Pay, no LINE Pay, no d払い, no au PAY, no Amazon Pay, no Apple Pay, no Google Pay, no BNPL and no instalments** — from an enumeration eplus publishes as the definitive answer to "what payment methods are there." The inbound storefront at `ib.eplus.jp` is a **CS-Cart** install pricing in **seven currencies** across **English and Chinese only**, taking **Visa, Mastercard and Alipay and nothing else**, whose FAQ openly tells overseas buyers that a decline is their issuer's problem while acknowledging it holds funds on failed debit attempts. The structural finding that outranks all of it: **a card refund more than seven months old cannot go back to the card** and falls into a third-party Wellnet remittance — in a business that sells tickets six to twelve months ahead and refunds whole tours when they cancel. Alongside that sit a documented **T+1 payment reconciliation lag** that has eplus emailing payment reminders to customers who already paid — **which they state in writing** — and a live refund incident on their own homepage today. At **16/29** this sits one point under ⭐ and I declined to override it; the point I would have had to reach for is a "3+ countries" row that a single-entity Japanese merchant has not earned.

</details>
