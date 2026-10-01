# ANA (All Nippon Airways)

**Status:** 🔵 Outreached — sequence active
**ICP Score:** 23 / 29 → ⭐ **High Priority**
**Industry:** Airlines (passenger, + Nippon Cargo Airlines consolidated FY2025) · **HQ:** Tokyo, **Japan** — ANA Holdings Inc., **TSE 9202** · **Researched:** 2026-09-18 · **First email sent:** 2026-10-01
**Motion:** **Greenfield** — none detected. Unusually well-evidenced for a greenfield call: ANA's own payment pages show three *separate* point-to-point hand-offs rather than one routing layer (see 3B).

> **Highest-scoring account in this repo to date.** The margin comes from three rows that are sourced rather than inferred: a first-party exhaustive method table, a first-party live defect list, and a first-party results release.

---

> ## 🎯 THE HOOK — ANA has been publicly apologising for its own booking-and-payment system for fifteen months, and paid-seat refunds on international are still not possible online
>
> ANA is migrating its domestic passenger service system onto **Amadeus Altéa**, the platform its international business already runs — **domestic go-live 29 May 2025**.
>
> **On 6 August 2026 — fifteen months later — ANA's own FAQ page still opens with an apology.** Verbatim, fetched by me from `ana.co.jp/ja/jp/notice/renewal-2025-2026/faq/`:
>
> > 「この度は国内線サービスのリニューアルに伴い、お客様には多大なるご不便とご心配をおかけしておりますことを、**深くお詫び申し上げます**。搭乗手続き等で発生していた**システムエラー**につきましては、多くのお客様にご利用いただく機能から優先して、順次修正・改善に努めてまいりました。」
>
> *"We deeply apologise for the great inconvenience and concern caused to customers by the domestic service renewal. Regarding the **system errors** occurring during boarding procedures, we have been fixing and improving them, prioritising the functions used by the most customers."*
>
> **And the live functional-restrictions page carries three money-movement defects right now.** All three fetched by me from `ana.co.jp/ja/jp/promotion/renewal-2025-2026/special-notice/`:
>
> | Defect, verbatim | What it means |
> |---|---|
> | **（国際線）有料座席指定の取消・変更** — 「現在、ANAウェブサイトで有料座席指定の取消・変更を承ることができません。…ANA予約・案内センターまでお問い合わせください。」 | **A paid ancillary that cannot be cancelled or changed online at all.** Every one of those refunds goes through a phone agent. |
> | **ANA SKY コイン払い戻し時の金額非表示** — 「払い戻し金額が表示がされませんが、正常に受付されております。」 | A refund that **processes without showing the customer the amount**. |
> | **特典航空券の払い戻し** — 「払戻完了メールを送信することができません。」 | A refund that **completes without a confirmation email**. |
>
> **This is the cleanest possible opener and none of it is our characterisation — it is ANA's own words on ANA's own live pages.** The angle is not "your migration went badly." It is: *a core-platform migration is exactly when the payment layer stops being able to absorb change, and the ancillary and refund paths are where it shows first.*

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** ANA Holdings is Japan's largest airline group. **FY2025 (year ended 31 Mar 2026) operating revenue ¥2,539.2bn — a record**, with operating income ¥217.4bn and net income ¥169.0bn, all record highs. It is mid-flight on a domestic PSS migration to Amadeus Altéa that it is still apologising for. **FY2026 guidance takes operating income down to ¥150.0bn — a 31% fall** on revenue guided *up* to ¥2,770.0bn.

**SimilarWeb total visits:** **Not obtained.** No data supplied. Country profile is estimate-grade; **no split invented.**

### Accepted methods — first-party, exhaustive, verified by me directly
✅ Fetched from ANA's own payment hub, **both language versions**, `ana.co.jp/{ja,en}/jp/guide/reservation/payment/`. The English page carries **two** tables — one for domestic, one headed *"Payment Methods for ANA Website International Flight Reservation & Purchasing Service"*.

| Method | Scope, verbatim |
|---|---|
| **Credit card** | Domestic table: *"lump-sum payments only"* (一括払いのみ). **International table instead links to a "Credit Card Payment Service" page for instalment and revolving payments.** |
| **Apple Pay** | ✅ Present — **but restricted.** 「航空券の新規ご購入時**のみ**ご利用になれます。ご購入後の予約変更時の差額支払いにはご利用になれません」 — **new purchases only; cannot be used for fare differences on a rebooking**, nor for award tickets or ANA-card discount fares. |
| **ANA SKY COINS** | Miles converted to coins; split tender with a card. |
| **PayPal** | ✅ Present. **¥1,000,000 cap.** Separate redirect flow at `/payment/paypal/`. |
| **Online banking (ネット振り込み)** | Bank transfer to a designated account; prior registration with the bank required. |
| **Konbini — six chains** | Seven-Eleven, Lawson, MINISTOP, FamilyMart, **Seicomart**, Daily Yamazaki / Yamazaki Daily Stores. Multimedia-terminal slip or 13-digit / 11-digit payment number. |
| **Pay-Easy ATM** | *"Mizuho Bank, Sumitomo Mitsui Banking, MUFG Bank, Resona Bank, or Japan Post Bank."* |

### ❌ Affirmatively ABSENT — and this is sourced absence, not unchecked absence
The table above is ANA's **complete** published method set on its own payment hub. **None of the following appears anywhere on it:**

**PayPay · Rakuten Pay · d払い · au PAY · LINE Pay · Amazon Pay · Merpay · Paidy · Google Pay · UnionPay · Alipay · WeChat Pay · carrier billing · any BNPL**

> 🛑 **DO NOT LEAD ON PAYPAY. I checked JAL and the answer went against us.**
>
> ✅ **Verified by me** from JAL's own domestic payment page (Wayback snapshot `20260606014023` of `jal.co.jp/jp/ja/dom/payment/` — JAL's live site returns **HTTP 403** to both curl and WebFetch). JAL's complete domestic method set is:
>
> **クレジットカード · e JALポイント · コンビニ（現金） · 銀行・郵便局ATM (Pay-easy) · インターネット振込 · JAL旅行券** *(the voucher is phone-only)*
>
> **JAL takes no PayPay either — and no Apple Pay, no Rakuten Pay, no LINE Pay, no d払い, no au PAY, no Amazon Pay, no Google Pay and no Paidy.** The two stacks are near-identical in shape: card, an in-house points currency, konbini, Pay-easy, bank transfer, voucher. ANA is marginally *ahead* — it has Apple Pay and PayPal, JAL has neither.
>
> **This is a Japanese legacy-carrier category norm, not an ANA failing.** Opening on it invites the true and fatal reply *"JAL doesn't either."* **The rail gap belongs in E3 as a question about roadmap, never in E1 as an observation.**
>
> ⚠️ **Same trap on both sites: 「PayPay銀行」 appears in the Pay-easy bank list on JAL's page. That is PayPay *Bank*, not the wallet.** Two hits, both in that list. Do not misread it as acceptance on either carrier.
>
> ### ★ UPDATE 2026-09-19 — WE NOW KNOW *WHY*, AND IT IS BETTER THAN THE ORIGINAL OBSERVATION
>
> Researching JAL surfaced the mechanism behind the shared absence. **JAL's own international payment page links out to `multiple-payment.biz` — the only non-analytics third party on the page — which is Wellnet's product site**, titled 「ウェルネット（WELLNET）マルチペイメントサービス」. ✅ **Both verified by me.**
>
> Wellnet's own copy: 「2000年5月から稼動開始。**国内主要航空会社の全て**…」 — *"in operation since May 2000. Used by all of Japan's major domestic airlines."*
>
> **And its complete method set, from its own FAQ:**
> > 「クレジットカード/コンビニ(現金）/ATM(ペイジー)/ネットバンク/**電子マネー(楽天Edy,モバイルSuica,JCBプレモ)**/支払秘書」
>
> **The e-money ceiling is Rakuten Edy, Mobile Suica and JCB Premo. No PayPay. No code wallet of any kind.**
>
> 📌 **ANA is named on its own site as using 決済代行会社「ウェルネット社」 for exactly these rails.**
>
> ### ⛔ CORRECTION — 2026-09-19. The vendor-ceiling reading was WRONG. Do not pitch it.
>
> I previously concluded from this that ANA's missing wallets were **a vendor constraint, not a choice**. **That causal claim is refuted**, and the refutation comes from inside ANA's own holding company.
>
> **Peach Aviation is a Wellnet customer AND carries five code wallets.** Verified first-hand on Peach's own payment page, `https://www.flypeach.com/lm/fares/payment`, 2026-09-19 — a dedicated **バーコード決済** section in the navigation and in the availability matrix, listing **楽天ペイ · PayPay · d払い · Alipay · WeChat Pay**, each with its own currency and channel columns. PayPay carries the restriction 「PayPayでの決済は、あらかじめチャージされた「PayPay残高払い」のみご利用いただけます」. (Peach's Wellnet relationship: Wellnet's own 2012-01-11 release, retrieved via Wayback, describes 「Peach Aviationとウェルネットサーバが直接接続され24時間稼動」. Continuation to 2026 is **strong inference, not verified** — Peach's current page names no 決済代行会社.)
>
> **So Wellnet's e-money ceiling is a ceiling on *that one rail*, not on the airline.** Peach simply runs a second, parallel wallet rail alongside Wellnet's konbini/Pay-easy rail. ANA could do the same and has not.
>
> ### ✅ The replacement framing — which is *stronger*, not weaker
> This turns **"they can't"** into **"they haven't"**, and it puts the counter-example **inside ANA's own consolidation scope**. A sister airline in the same holding company, on the same konbini vendor, made the opposite choice and has been shipping wallets since 2017.
>
> ⚠️ **Carry this caveat into outreach so a call cannot correct you:** this refutes the *causal* claim only. It does **not** prove ANA evaluated wallets and rejected them. The honest framing is **"your own LCC does this and you don't"** — never "you were wrong about your vendor".

### Known PSPs
| Provider | Role | Evidence |
|---|---|---|
| **Wellnet Inc. (ウェルネット)** | 決済代行 for konbini / Pay-easy / net-transfer rails | ✅ **Verified by me directly.** `ana.co.jp/ja/jp/guide/reservation/payment/pay-howto/` walks the customer through **STEP5 「次画面（ウェルネット社サイト）に移動するための同意確認」** and **STEP6 「ウェルネット社サイトに遷移」**, with the body text 「**決済代行会社「ウェルネット社」のページに遷移します。**」 |
| **PayPal** | Wallet, own redirect | ✅ First-party, own sub-page and ¥1m cap |
| **Card acquirer / gateway** | ❌ **NOT ESTABLISHED** | Checked against GMO Payment Gateway, SB Payment Service, Veritrans/DG Financial, KOMOJU, Sony Payment Services, JCB, NTT Data/CAFIS, Adyen, Stripe, Checkout.com, Worldpay, Cybersource, Braintree, Accelya, CellPoint Digital. **Nothing disclosed.** |

**UATP** and **IATA settlement** are airline-specific rails and were flagged as accepted by the research agent; **I have not verified either first-hand.** Treat as unconfirmed.

### Orchestration status
**None detected — greenfield.** Unlike most greenfield calls in this repo, this one has **affirmative architectural evidence**, not just absent search hits:
- Konbini / Pay-easy **leaves ana.co.jp entirely** for Wellnet's hosted site, behind a consent interstitial
- PayPal is a **separate** redirect with its own cap and its own sub-page
- The card path stays on ANA and is handled by an undisclosed third party
- Apple Pay is **scoped to one transaction type** and cannot follow the booking through its lifecycle

**Four methods, four different paths, and one of them cannot survive a rebooking.** That is a point-to-point estate, not a routed one.

### Buying signals
- 🔴 **A fifteen-month-old public apology** for system errors, still live on 2026-08-06
- 🔴 **Three live money-movement defects** on ANA's own restrictions page, including a paid ancillary with **no online cancellation path at all**
- 🏗️ **Amadeus Altéa domestic PSS migration** — go-live 2025-05-29, announced in a 2023 group press release as a domestic/international system integration. **A platform migration is the single best window for a payment-layer conversation.**
- 📉 **FY2026 operating income guided down 31%** (¥217.4bn → ¥150.0bn) on revenue guided *up* 9%. **Margin compression with volume growth is exactly the shape that makes cost-of-acceptance and auth-rate arguments land.**
- 🌏 **Network expansion** — Narita=Perth, Narita=Mumbai and Narita=Brussels added Dec–Mar; Narita/Haneda=Hong Kong frequencies up; three new routes launched H2 FY2024; 40th anniversary of international scheduled ops in March
- 🤝 **Joint venture with Singapore Airlines**, joint fares launched in May — and **SQ is a confirmed CellPoint Digital customer** (established in the Cathay Pacific file). ANA's JV partner already runs airline payment orchestration.
- ❌ No payment RFP and no payments hire found

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

### Pain Vector Extraction

```
=== PAIN VECTOR EXTRACTION ===

Motion: Greenfield — none detected, affirmatively. Four methods on four separate paths.
        But the framing is LIFECYCLE, never "you have no orchestration layer" and never
        the wallet gap (JAL is identical — see the Hook).

Observable setup facts (verified first-hand, 2026-09-18):
- Apple Pay footnote, ANA's own words: 「航空券の新規ご購入時のみご利用になれます。
  ご購入後の予約変更時の差額支払いにはご利用になれません」 — new purchases only, and
  explicitly NOT for a fare difference on a rebooking
- International paid seat selection: 「現在、ANAウェブサイトで有料座席指定の取消・変更を
  承ることができません」 — no online cancellation or change at all, call centre only
- ANA SKY Coin refunds process without displaying the refund amount
- Award-ticket weather refunds complete without sending a confirmation email
- Konbini and Pay-easy leave ana.co.jp entirely for a hosted site, named verbatim as
  決済代行会社「ウェルネット社」, behind a consent interstitial (STEP5 → STEP6)
- PayPal is a separate redirect with its own ¥1,000,000 cap
- Domestic card is 一括払いのみ (lump-sum only); the international table instead links out
  to a separate "Credit Card Payment Service" page for instalments and revolving
- Amadeus Altea domestic PSS go-live 2025-05-29; ANA still publicly apologising for
  system errors on 2026-08-06
- FY2025 revenue Y2,539.2bn (record); FY2026 operating income guided 217.4bn -> 150.0bn

Selected observations for Phase 1 (E1 bullets, ranked by materiality):
1. The Apple Pay lifecycle asymmetry -> "Apple Pay works for a new booking on your site,
   but your own footnote says it can't pay the fare difference when someone changes one."
   MATERIALITY: highest. It is an asymmetry inside their own stack, sourced to their own
   footnote. It cannot be disputed and it needs no interpretation. This is the voice
   anchor's strongest move applied exactly.
2. The offline ancillary refund -> "Paid seat selection on international can't be
   cancelled or changed on the site at all — your page sends people to the call centre."
   MATERIALITY: high. A paid ancillary whose refund path is a human being.
3. Four methods, four paths -> "Konbini and Pay-easy hand off to a separate hosted site,
   PayPal is its own redirect with a Y1m cap, and cards stay on ANA."
   MATERIALITY: medium, but it does the bridging work into E2 and it is purely factual.

   DELIBERATELY NOT USED: the wallet gap (JAL is identical — see the Hook), anything
   about volume or revenue, and anything that reads as a comment on the migration going
   badly. The migration is CONTEXT, not an accusation.

Bridge variant: C — friction
Rationale: ANA does have 2+ visible processors and is multi-market, which on paper is
variant A. But both lead observations are LIFECYCLE friction, not provider count, and
variant A's "complexity" framing would point the email at the wrong thing. C describes
what the observations actually show.

Hypothesis for Phase 2 (E3):
The payment layer looks built per transaction type rather than per booking — so anything
that happens AFTER the first successful payment tends to fall off the rail it was paid on.
Backing logic: Apple Pay can open a booking but their own footnote says it cannot amend
one. A paid international seat can be sold online but not cancelled online. A SKY Coin
refund completes without showing an amount; an award refund completes without an email.
Four methods, four paths, and the only one that covers the full lifecycle is the raw card.
At ANA's passenger volume, every one of those exceptions is a contact-centre minute — and
FY2026 guides operating income down 31% on revenue guided up.

Success case for Phase 3 (E4):
Selected case: Wingo
Tier: 1 on industry (airline, and the only quantified airline case in the library),
      2 on pattern (Wingo's numbers are approval/retry, my hypothesis is lifecycle).
      STATED AS SUCH in the email — no pretending it is an exact match.
Match rationale: it is the one airline case with published numbers, and the
"1,000+ payment methods through one integration" bullet speaks directly to the lifecycle
point: a method configured once is available everywhere in the booking's life, not only
at first purchase.
Numbers to lead with: +14% approval rate (initial implementation phase) ·
1,000+ payment methods through one integration · 3DS and fraud tooling in the same layer
Plus one line naming Qatar Airways, Copa Airlines and Avianca as running on the same
layer — NO NUMBERS ATTACHED to any of them, ever.
Optional benchmark: SKIP, twice over. The "~8% average authorisation uplift" is Yuno's
own blog figure, not third-party evidence. The IATA/EDC "$20.3bn, 2.1% of industry
revenue" would be the perfect airline hook but the skill file says trace it to the
IATA/EDC primary source first, and nobody has. Not used.

Touch-by-touch angles:
- E2 angle: the Apple Pay asymmetry -> ONE mechanism: a single layer above the existing
  providers where the method and the credential persist across the whole booking — the
  original sale, the change, the ancillary, the refund — instead of being re-integrated
  per transaction type
- LK1 angle: the Apple Pay footnote, one sentence
- LK2 angle: the payment layer is built per transaction type, not per booking
- LK3 angle: Wingo — 1,000+ methods through one integration, +14% approval
- LK4 angle: FRESH — the Singapore Airlines JV. Joint fares launched in May, one
  commercial JV, two entirely different payment stacks underneath
- E8 angle: clean exit, offer to circle back once the Altea cutover has settled
```

**Calendar.** Day 1 anchored to **Monday 28 September 2026** — deliberately *after* Japan's
Silver Week: **敬老の日 (Respect for the Aged Day) Mon 21 Sep** and **秋分の日 (Autumnal
Equinox Day) Wed 23 Sep**. One further Japanese public holiday falls inside the send window:
**スポーツの日 (Sports Day), Mon 12 Oct**. **No send day and no proposed meeting slot falls on
any of the three**, or on a weekend.

**Times are JST (UTC+9), which is IST+3:30.** Per the rulebook, Japan gets afternoon-local
slots so they land as late morning for Prateek — every slot below is 14:00–16:00 JST, i.e.
10:30–12:30 IST.

---

### Phase 1 — Curiosity (Days 1–5)

#### Touch 1 — Email 1 · Day 1 · Mon 28 Sep

**Subject:** Apple Pay on your rebooking flow

```text
Hey {{recipient.first_name}},

Spent some time on ANA's payment setup. Three things stood out:

- Apple Pay works for a new booking on your site, but your own footnote says it can't pay the fare difference when someone changes one.
- Paid seat selection on international can't be cancelled or changed on the site at all — your page sends people to the call centre.
- Konbini and Pay-easy hand off to a separate hosted site, PayPal is its own redirect with a ¥1m cap, and cards stay on ANA.

That kind of setup usually has some friction worth checking on.

I work at Yuno — top-100 fintech, a16z-backed. We consider ourselves the 'everything payments' platform: one integration, every PSP, every method, every market.

Rather than pitch you based on assumptions, is there anything payment-related you're working through that we might be able to help with?

Best,
Prateek
```

#### Touch 2 — Email 2 · Day 3 · Wed 30 Sep · REPLY IN THREAD

```text
Hey {{recipient.first_name}},

Following up — wanted to put a bit more behind what Yuno actually does, and how it would address what I flagged.

- We sit above your existing providers. Additive, nothing gets ripped out.
- One integration covers every method and every market, so a method enabled once is available everywhere.
- The routing layer holds the credential, so the same method can carry a booking and then the change, the ancillary and the refund against it.
- Adding a PSP, an acquirer or a rail becomes a configuration change rather than a project.

On the Apple Pay point specifically — that footnote usually isn't an Apple Pay limitation, it's a sign the wallet was integrated at the point of sale rather than at the booking. Once the method sits in the layer rather than in the checkout, the fare difference is just another auth against the same credential.

I'll keep sharing what I'm seeing every few days. If your stack's where you want it, just say the word and I'll back off — otherwise happy to go deeper.

Cheers,
Prateek
```

#### Touch 3 — LinkedIn message 1 · Day 5 · Fri 2 Oct

```text
Hey {{recipient.first_name}} — figured I'd flag this here too in case more useful than email. Quick one: Apple Pay works for a new booking on ana.co.jp, but your own footnote rules it out for the fare difference on a change. Curious if that maps to anything you're working through on the payments side.
```

---

### Phase 2 — Diagnosis (Days 7–9)

#### Touch 4 — Email 3 · Day 7 · Tue 6 Oct · NEW EMAIL

**Subject:** Read on your post-purchase payment paths

```text
Hey {{recipient.first_name}},

Going to take a swing at this — based on what I see, my read is that the payment layer was built per transaction type rather than per booking, so anything that happens after the first successful payment falls off the rail it was paid on.

Three things point that way. Apple Pay can open a booking but your footnote says it can't amend one. A paid international seat can be sold online but not cancelled online. And a SKY Coin refund completes without showing the customer an amount.

At your passenger volume every one of those exceptions lands in the contact centre, which is an odd place for cost to sit in a year where operating income is guided down.

At Yuno (a16z-backed, top-100 fintech), we sit above your existing PSPs so a method carries the whole booking lifecycle rather than just the sale — keep your stack, add what's missing.

Thursday is open for me — would 15:00 or 16:00 your time work for a quick 15 minutes?

Best,
Prateek
```

> **One embedded discovery question is permitted in E3 or E4 only.** It is placed in E4 below,
> not here — E3 is already carrying the hypothesis and a CTA, and two asks in one email
> dilute both.

#### Touch 5 — LinkedIn message 2 · Day 9 · Thu 8 Oct

```text
Hey {{recipient.first_name}} — sent a longer note over email this week. Short version: the payment stack looks built per transaction type rather than per booking, which is why a method can start a booking but not amend one. If that's anywhere on your radar, would Tuesday the 13th at 14:00 your time work for a quick 15?
```

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · Tue 13 Oct · NEW EMAIL

**Subject:** How Wingo solved this

```text
Hey {{recipient.first_name}},

On the read I shared last week — sharing a quick example of what solved looks like. Different region and a smaller carrier, so I'll be straight that it's a pattern match rather than a like-for-like.

Wingo, the Colombian low-cost carrier, put Yuno above its existing providers:

- +14% approval rate, from the initial implementation phase alone (not too bad, right?)
- 1,000+ payment methods available through one integration — configured once, live everywhere in the booking
- 3DS and fraud tooling in the same layer, rather than per-provider

That middle bullet is the one that maps to your setup. Same orchestration layer above their existing stack — no rip-out. Qatar Airways, Copa Airlines and Avianca run on the same layer.

Genuinely curious about one thing: when someone changes an international booking, does the fare difference go back to the original method, or does it start a fresh payment?

Friday the 16th is open — would 14:00 or 15:00 your time work?

Full case here if useful: https://y.uno/en/newsroom/wingo-improves-payment-efficiency-with-yuno-as-strategic-partner

Thanks,
Prateek
```

#### Touch 7 — Email 5 · Day 13 · Thu 15 Oct · ⚠️ MANUAL

> **Placeholder — Prateek writes this one.**
>
> **Suggested angle:** an annotated screenshot teardown of the ANA payment page showing the
> four separate paths side by side, with the Apple Pay footnote circled. Everything needed is
> already in Section 1 of this file and all of it is first-party. **A Loom walking the
> international rebooking flow would be stronger still** — it makes the lifecycle argument
> visible rather than asserted.

#### Touch 8 — Email 6 · Day 15 · Mon 19 Oct · ⚠️ MANUAL

> **Placeholder — different format from E5.**
>
> **Suggested angle:** the contact-centre cost arithmetic. ANA's own page routes every
> international paid-seat cancellation to a phone agent; pair that with the FY2026 operating
> income guidance (¥217.4bn → ¥150.0bn) and let them do the multiplication. **Do not put a
> number on it ourselves — we don't have their call volumes or their cost per contact, and
> inventing either would be the one thing that loses this thread.**

#### Touch 9 — LinkedIn message 3 · Day 17 · Wed 21 Oct

```text
Hey {{recipient.first_name}} — Wingo got 1,000+ payment methods through a single integration, configured once and live across the whole booking rather than per transaction type. Worth 15 minutes to see if it maps to your setup? Friday the 23rd at 14:30 your time is open.
```

---

### Between Phases (Day 19)

#### Touch 10 — Email 7 · Day 19 · Fri 23 Oct · ⚠️ MANUAL

> **Placeholder — manual creative bridge.**
>
> **Freshest unused anchor:** the **Singapore Airlines joint venture**, with joint fares
> launched in May. Two carriers now selling a shared commercial product across two entirely
> different payment stacks. That is a genuinely interesting operational question and it is
> from ANA's own results release. ⚠️ **Do not state or imply that SQ is a Yuno customer —
> they are not. SQ runs a competitor's layer, and naming it is forbidden.** The angle is the
> JV, not the vendor.

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21 · Tue 27 Oct

```text
Hey {{recipient.first_name}} — last LK ping from me on this. One thing I keep coming back to: the SQ joint venture sells a shared fare across two completely separate payment stacks. If timing works, Thursday the 29th at 15:30 your time is open for a quick 15.
```

#### Touch 12 — Email 8 · Day 23 · Thu 29 Oct · REPLY IN THREAD to E3

```text
Hey {{recipient.first_name}},

Going to stop pinging unless you want to pick this back up.

Fair guess that a payments conversation is not the priority while the Altéa cutover is still settling. If that's the case, happy to circle back once it has — that's usually when the payment layer's edges become obvious anyway.

If it ever comes back up, just reply here.

All the best,
Prateek
```

---

### ⚠️ Send-time checklist — four things to re-verify before Touch 1 goes out

1. **The international paid-seat restriction is temporary by design.** It is the sharpest line
   in E1. **Re-load `ana.co.jp/ja/jp/promotion/renewal-2025-2026/special-notice/` on the
   morning of 28 Sep.** If it has been fixed, swap that bullet for the SKY Coin refund
   amount-not-displayed defect and check that one too.
2. **The Apple Pay footnote** — same page-check discipline, on the payment hub.
3. **Never mention PayPay.** JAL is identical and the reply writes itself. It belongs in a
   later conversation as a roadmap question, not in this sequence.
4. **Never name our competitors** — not in the SQ JV touch, not anywhere.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 23 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED as a bound; clears by orders of magnitude.** Sourced input: **FY2025 air transportation passenger and cargo revenue ¥2,313.2bn, +12.4% YoY** (ANA HD release, 30 Apr 2026, fetched by me). **Billing unit is bookings, not passengers**, and ancillaries — paid seats, changes, excess baggage — bill separately, which ANA's own restrictions page confirms by treating paid seat selection as its own transaction. **Presented as a bound because the divisor is unsourced:** even assigning an implausibly high **¥300,000 (~US$2,000)** to every booking and ignoring that domestic fares are a fraction of that, ¥2,313.2bn yields ~7.7m bookings/year = **~640k/month**. ⚠️ NCA cargo is consolidated into that line and is invoiced B2B, outside a card checkout — but **stripping cargo entirely still leaves every plausible divisor clearing the 100,000 band by a wide margin.** Hence ✅, not ⚠️. |
| Orchestration status | **+4** | ✅ **None detected — and this is the best-evidenced greenfield call in the repo.** Not merely an absence of hits: ANA's own pages show a Wellnet full-page redirect for cash rails, a separate PayPal redirect, a separate undisclosed card path, and an Apple Pay integration scoped to a single transaction type. Four methods, four paths. |
| 3+ countries | **+3** | ✅ International network across Europe, North America, Asia, Australia and India; Perth, Mumbai and Brussels added in FY2025; 40th anniversary of international scheduled operations. First-party. |
| Multiple PSPs | **+2** | ✅ **Structurally proven, not inferred.** The konbini/Pay-easy rail demonstrably leaves ANA's domain for Wellnet while the card rail does not — two distinct providers, evidenced on ANA's own walkthrough. ⚠️ Only **one** of them (Wellnet) can be named; the card acquirer is undisclosed. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Best-sourced row — but read the caveat, it changes the email and not the score.** Japan is the #1 market by a wide margin. **PayPay, Rakuten Pay, d払い, au PAY, LINE Pay, Amazon Pay, Merpay, Paidy, Google Pay, UnionPay, Alipay, WeChat Pay, carrier billing and BNPL are all absent from an exhaustive first-party method table I fetched in both languages.** That is **sourced absence**, which is the bar this row exists to clear, so it scores. ⚠️ **But I then checked JAL and found the same shape** — see the Hook. **The gap is a category norm, so it is worth points on fit and worth nothing as an opener.** Prateek may reasonably want this row at +1; I kept it at +3 because the row measures whether the rail is missing in a top market, not whether a competitor also misses it. **Flagging it rather than quietly splitting the difference.** |
| Recent expansion | **+2** | ✅ Three new international routes in H2 FY2024; Narita=Perth, Narita=Mumbai, Narita=Brussels and Hong Kong frequency increases across Oct–Mar; **Singapore Airlines JV with joint fares launched in May**. All from ANA HD's own results release. |
| Payment issues reported | **+2** | ✅ **Not customer complaints — ANA's own defect list.** A standing apology for system errors dated **2026-08-06**, plus three live money-movement defects: international paid-seat cancellation impossible online, SKY Coin refund amount not displayed, award-ticket refund confirmation email not sent. All fetched first-party. |
| Funding >$10M | **0** | ❌ TSE-listed (9202). No round. |
| High traffic outside home | **0** | ⬜ **Scored zero deliberately, and it cuts against us.** ANA is domestic-heavy — the research agent reported ANA International 9,023k, ANA Domestic 45,635k and Peach 9,456k passengers, i.e. ~71% domestic. ⚠️ **`[UNVERIFIED — agent-reported, not confirmed by me]`**, but directionally certain, and it is why the cross-border pitch must be secondary here. |
| Competitor using orchestration | **+2** | ✅ **Singapore Airlines runs CellPoint Digital** (established in the Cathay Pacific file). ⚠️ **Caveat worth stating out loud: SQ is now ANA's *joint venture partner*, not its closest competitor** — that is JAL, and JAL's stack is **NOT ESTABLISHED**. The JV arguably makes this *stronger* evidence of category adoption inside ANA's immediate orbit, but it is not the like-for-like comparison. |
| Payment job postings | **0** | ⬜ None found. |

**Tier: 23 / 29 → ⭐ High Priority.** No analyst override applied.

> **The one row that could move, and the one that could collapse.** The card acquirer is unknown; naming it would sharpen everything and change nothing about the score. The **rail gap (+3) is the row at risk** — not because the absence is wrong, it is verified, but because its *materiality* depends on whether JAL differs. Check JAL before sending. If JAL also takes no PayPay, this is still a 23 but the sequence needs a different lead.

### Source Notes
- ✅ **The complete method table was fetched by me directly in both Japanese and English**, including the two-table split between domestic and international and every footnote restriction.
- ✅ **Wellnet is verified verbatim** — 「決済代行会社「ウェルネット社」のページに遷移します。」 — as STEP5/STEP6 of ANA's own payment walkthrough. This is a **full-page hand-off to a third-party hosted site**, not an embedded integration, which is the architecturally important part.
- ✅ **FY2025 results and FY2026 guidance fetched** from `anahd.co.jp/group/en/pr/202604/20260430.html` (30 Apr 2026). Revenue ¥2,539.2bn, operating income ¥217.4bn, net income ¥169.0bn — all records. FY2026 forecast ¥2,770.0bn revenue, ¥150.0bn operating income. **The −31% operating income figure is my own arithmetic on their two published numbers**, not a quoted figure.
- ✅ **The apology and all three live defects were fetched by me** from ANA's own renewal FAQ and special-notice pages.
- ⚠️ **CORRECTION to the research agent's report: the apology is dated 2026-08-06, not 2026-06-11.** The page the agent cited (`/ja/jp/special-notice/001463.html`) now returns **HTTP 404** — it was a temporary notice and has been removed. The live replacement is more recent and says the same thing, so the finding stands but **the date and URL in the agent report are both wrong. Use the ones in this file.**
- ⚠️ **The agent also reported "domestic fare-difference rebooking erroring out" as an open defect.** It is **not** on the live restrictions page and I could not confirm it. **Do not use it.**
- ⚠️ **Passenger counts (64.1m total; ANA Intl 9,023k / Domestic 45,635k / Peach 9,456k) are agent-reported and unverified by me.** Directionally safe for the domestic-heavy framing; **do not put the exact numbers in an email.**
- ⚠️ **UATP and IATA settlement acceptance — agent-reported, unverified.** Not used anywhere above.
- ❌ **An Alipay data point the agent surfaced rests on a 14-year-old press release.** Excluded entirely. Alipay is listed as absent above and that is the correct present-tense reading of the live method table.
- ⚠️ **Amadeus Altéa go-live 2025-05-29 and the ~June 2026 cutover** are corroborated by ANA's own renewal pages and a 2023 ANA HD press release on integrating the domestic and international PSS. **The Amadeus vendor name is from the 2023 release and the search summary, not from a page I fetched — treat the *vendor* as high-confidence but not first-party-verified; the *migration* itself is beyond doubt.**

### Manual Research Recommendations
> **1. ✅ DONE — JAL checked, see the Hook.** JAL takes no PayPay and no Apple Pay. The wallet gap is a category norm and is demoted out of the opener. ⚠️ **The JAL data is a 2026-06-06 Wayback snapshot because jal.co.jp 403s every automated fetch — re-confirm from a browser before quoting it to anyone.**
> **2. Walk the ANA checkout to the card form and identify the acquirer** — network tab, CSP, iframe origin. Nobody has named it.
> **3. Confirm whether international paid-seat cancellation is still phone-only** at send time. It is the sharpest line in the sequence and it is a *temporary* restriction by definition. **Re-verify on the day.**
> **4. Establish whether Peach runs a separate stack.** Peach is ~9.5m passengers, LCC, and LCCs in Japan typically take a wider wallet set than legacy carriers. If Peach takes PayPay and ANA mainline does not, the group-consolidation story writes itself.
> **5. Get the FY2025 passenger split from the investor deck** rather than relying on the agent's numbers.

---

## Executive Summary

ANA Holdings is Japan's largest airline group and posted **record FY2025 revenue of ¥2,539.2bn** while guiding FY2026 operating income **down 31%** on revenue guided up — margin compression with volume growth, which is the shape that makes payment economics a board-level conversation. Its published method set, which I fetched first-party in both languages, is **card, Apple Pay, ANA SKY Coins, PayPal, bank transfer, konbini across six chains, and Pay-Easy ATM — and nothing else.** No PayPay, no Rakuten Pay, no LINE Pay, no d払い, no au PAY, no Google Pay, no UnionPay, no BNPL. Architecturally the estate is **point-to-point**: konbini and Pay-easy hand off to a third-party hosted site run by **Wellnet**, named verbatim on ANA's own walkthrough; PayPal is a separate redirect with its own ¥1m cap; the card path is handled by an acquirer nobody can name; and **Apple Pay is scoped so tightly it cannot pay a fare difference on a rebooking**. Meanwhile ANA is fifteen months into migrating its domestic passenger service system to **Amadeus Altéa** and is **still publicly apologising for system errors as of 6 August 2026**, with three money-movement defects live on its own restrictions page — including a **paid seat selection that cannot be cancelled or changed online at all**. At **23/29 this is the strongest account in the repo**. **The one thing that would have gone wrong is now pre-empted: I checked JAL, found the identical wallet gap, and moved the rail story out of the opener** — the sequence leads on the migration and the broken refund lifecycle, which are ANA's alone.

</details>
