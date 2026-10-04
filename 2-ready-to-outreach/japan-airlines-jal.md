# Japan Airlines (JAL)

**Status:** 🟢 Ready to outreach — sequence drafted
**ICP Score:** 17 / 29 → ⭐ **High Priority**
**Industry:** Airlines (full-service, domestic + international, cargo, mileage commerce) · **HQ:** Tokyo, **Japan** — 日本航空株式会社, **TSE 9201** · **Researched:** 2026-09-19 · **First email sent:** —
**Motion:** **Greenfield** — none detected. Same architectural shape as ANA: cash rails on a third-party vendor, fraud on a separate 2015-vintage engine, card acquirer undisclosed, region-gated storefronts with different method sets.

---

> ## ⚠️ TWO PREMISES I HELD GOING IN WERE WRONG — both are corrected here
>
> **1. "JAL refuses third-party wallets" — WRONG.** My earlier JAL check (run during the ANA batch) used the **domestic** payment page only. **Apple Pay is present on the international flow** — verified by me, 3 occurrences on JAL's own international payment page. The correct statement is narrower and sharper: **JAL accepts no Japanese domestic *code* wallet** (PayPay, d払い, au PAY, Rakuten Pay, LINE Pay) anywhere found.
>
> **2. "JAL is mid-PSS-migration like ANA" — WRONG, and it inverts the angle.** JAL completed its move to **Amadeus Altéa in November 2017** — **nine years ahead of ANA**, unifying domestic and international onto one PSS. It also wound down its own GDS subsidiary **AXESS International Network** (operations ended 31 Mar 2021). **The ANA opener does not transfer.** `[Altéa dates UNVERIFIED — 2014–2019 announcements, search-summary corroborated; say "has run Altéa since 2017", not "runs Altéa today".]`

---

> ## 🎯 THE HOOK — the PSS was modernised nine years ago and the payment layer underneath it was not
>
> **JAL already paid the platform-modernisation cost and consolidated two PSSs into one.** Underneath that:
>
> | Layer | What is actually there |
> |---|---|
> | **Cash / bank rails** | **Wellnet (ウェルネット)** — a vendor running since **May 2000** |
> | **Fraud** | **NTT Data CAFIS Brain**, in full operation since **January 2015** — an eleven-year-old domestic rules engine in front of a global airline |
> | **Card acquiring** | ❌ **undisclosed — nobody can name it** |
> | **Storefronts** | **region-gated POS sites with different method sets per region** |
>
> ### ⛔ THE CATEGORY FINDING — RETRACTED 2026-09-19. Wellnet is NOT why JAL and ANA lack PayPay.
>
> **✅ Verified by me directly, and it explains an absence I previously could only describe.**
>
> JAL's own international payment page links its financial-institution list to **`multiple-payment.biz`** — and that domain is **the only non-analytics third party on the entire page** (everything else is Google Fonts, Akamai mPulse, social links and JAL's own domains). I fetched it: it is titled **「ウェルネット（WELLNET）マルチペイメントサービス」**.
>
> Wellnet's own copy, verbatim:
> > 「2000年5月から稼動開始。**国内主要航空会社の全て**、主要高速バス会社、その他大手通信販売などで現在もご利用いただいている」
> > — *"In operation since May 2000. Used by **all of Japan's major domestic airlines**…"*
>
> **And here is the constraint.** Wellnet's complete method set, from its own FAQ:
> > 「クレジットカード/コンビニ(現金）/ATM(ペイジー)/ネットバンク/**電子マネー(楽天Edy,モバイルSuica,JCBプレモ)**/支払秘書」
>
> **The e-money list tops out at Rakuten Edy, Mobile Suica and JCB Premo. There is no PayPay. There is no code wallet of any kind.**
>
> ### ⛔ CORRECTION — 2026-09-19. Do not pitch the vendor ceiling.
>
> I previously concluded that the wallet absence at JAL and ANA was **a vendor constraint rather than a preference**. **That causal claim is refuted.**
>
> **Peach Aviation is a Wellnet customer AND carries five code wallets** — 楽天ペイ, PayPay, d払い, Alipay, WeChat Pay — verified first-hand on Peach's own 支払方法 page on 2026-09-19, in a dedicated **バーコード決済** section of its availability matrix. Wellnet's e-money ceiling therefore constrains **that one rail**, not the airline: Peach runs a parallel wallet rail alongside it.
>
> **The absence at JAL is a choice, not a ceiling.** That is still usable — but it must be framed as *"your competitors and the LCCs do this"*, never as *"your vendor won't let you."* The latter is factually wrong and will be corrected on a call.
>
> ⚠️ This refutes the causal claim only. It does **not** establish that JAL evaluated wallets and declined them.
>
> ⚠️ **Precision, because it matters:** I verified that **JAL links to Wellnet for the Pay-easy / net-transfer institution list**. I did **not** observe a full-page Wellnet redirect in a live JAL checkout the way I did for ANA, and **Wellnet's own case-study page names bus operators and a baseball stadium — not JAL.** The airline claim is generic on Wellnet's homepage. **Say "the same vendor sits behind both carriers' cash rails", not "JAL redirects to Wellnet".**

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** JAL is Japan's second-largest carrier. **FY2025 (year ended 31 Mar 2026) revenue ¥2,012,515 million — ¥2.01 trillion, +9.1%, the first time above ¥2 trillion since the 2012 relisting.** EBIT ¥218,004m (+26.4%), net income attributable ¥137,604m (+28.6%) — all records.

**SimilarWeb total visits:** **Not obtained.** No data supplied, and `jal.co.jp` returns **HTTP 403** to both curl and WebFetch. Country profile unverified; **no split invented.**

### ❌ THE STUB'S REVENUE FIGURE IS REFUTED
The stub and the target list both say **$11.4B**. ✅ **I extracted the primary 決算短信 myself:** revenue is **¥2,012,515m**, which at ¥149–155/USD is **~US$13.0–13.5bn**. Getting to $11.4B needs ~¥176/USD, which did not prevail in the period. **The stub figure is stale — the prior year was ¥1,844,095m. Use the yen figure primarily**, which matters anyway given JAL prices in multiple currencies.

### Accepted methods — verified by me on BOTH flows
| Method | Domestic | International (Japan region) |
|---|---|---|
| **クレジットカード** | ✅ | ✅ **with 多通貨決済 (MCP) — customer picks the settlement currency, JAL applies its own FX conversion fee** |
| **Apple Pay** | ❌ **absent** | ✅ **present** — Amex, Mastercard, Visa. Carve-out: *"JALカードはMastercardのみ"* |
| **e JALポイント** | ✅ | ✅ full or partial, remainder on card |
| **コンビニ（現金）** | ✅ | ✅ **JMB members only** — Lawson, FamilyMart, Seven-Eleven; cutoff 10 days before departure |
| **銀行・郵便局ATM (Pay-easy)** | ✅ | ✅ |
| **インターネット振込** | ✅ | ✅ **two distinct rails** — Pay-easy 払込 (Mizuho, MUFG, SMBC, Suruga, Yucho) *and* インターネット振込サービス (PayPay銀行, 楽天銀行, 住信SBI, auじぶん) |
| **JAL旅行券** | ✅ phone only | ✅ phone only |

> ⚠️ **TRAP, and it is the same one as ANA: 「PayPay銀行」 is PayPay *Bank*, in the net-banking list. NOT the wallet.** One occurrence on the page. Do not misread it.

### ❌ Sourced-absent from BOTH flows
**PayPay · Rakuten Pay · LINE Pay · d払い · au PAY · Amazon Pay · Paidy · Google Pay · any at-checkout instalment (分割/リボ)** — instalment conversion is **post-purchase and issuer-side only**.

⚠️ **BUT the Japan-region page is not the whole international story.** JAL runs **region-gated POS sites** with different method sets, proven by JAL's own JAL Pay terms excluding 「海外地区でのご購入」 as a separate channel. A live JAL FAQ article exists titled 「**国際線｜Alipayで購入する際に…**」 — JAL would not publish Alipay troubleshooting for a method it does not accept. **Alipay is strong-signal; UnionPay and PayPal are search-summary only and unconfirmed.** Regional FAQ origins found: `jal-cn-jp`, `faq-en`, `faq-sr`, `faq-ar-en`, plus a `jal.co.jp/world/en/` site. **None could be read.**

### 💳 JAL Pay — the real ANA differentiator, and it is subtler than it looks
- ✅ **It does buy tickets on jal.co.jp** — double base miles when used, on JAL/JTA/JAC/RAC tickets bought on the **Japan-region site**, Japan counters or Japan reservation centres.
- 📌 **But it is not a separate checkout button. It is a Mastercard prepaid credential** — it rides the existing card rail or Apple Pay. JAL's own page excludes 「コード決済やタッチ決済など」 from the bonus. That is why it does not appear as a method on the payment page.
- **Operator: JALペイメント・ポート株式会社** — a **JAL × SBI Holdings** joint venture. **Banking layer: 住信SBIネット銀行**, JAL holding a banking-agency licence 関東財務局長(銀代)第336号.
- **Merchant descriptors it settles against are informative** — 「JAL国内線航空券類」「JAL国際線航空券類」「日本航空 国際線チケットレス」「日本航空 国際線自動発売機」「日本航空 **国際線サインレス**」. **Separate international signature-less and ticketless descriptors imply distinct international CNP acquiring from domestic.**

> **Read the posture correctly.** JAL is not a wallet refusenik — it accepts Apple Pay, very likely Alipay in-region, and **runs its own Mastercard-rail prepaid programme with a bank JV.** What it does not accept is any **Japanese code wallet** — while JAL Pay itself has code-payment capability at other merchants. **Combined with the Wellnet constraint above, the honest read is: the cash-rail vendor cannot carry code wallets, and JAL has its own wallet it would rather you used.**

### Known PSPs
| Layer | Finding |
|---|---|
| **Cash / Pay-easy / net banking** | ✅ **Wellnet** — verified via JAL's own outbound link; see the Hook, and read the precision caveat |
| **Fraud** | ✅ **NTT Data CAFIS Brain**, live since **January 2015**, from JAL's own press release |
| **PSS** | ✅ **Amadeus Altéa** since Nov 2017 |
| **Card gateway / acquirer** | ❌ **NOT ESTABLISHED** — the single biggest hole |

❌ **Searched, no evidence found:** GMO Payment Gateway, SB Payment Service, Veritrans/DG Financial, KOMOJU, Sony Payment Services, Adyen, Stripe, Checkout.com, Worldpay, Cybersource, Braintree, Accelya, CellPoint Digital. **Unchecked-absence, not sourced-absence.**
⚠️ **A 2017 JAL Card notice about a GMO-PG data-leak incident on unrelated government sites is NOT evidence of a JAL–GMO-PG relationship. Do not use it.**

### Buying signals
- 🏗️ **PSS modernised 2017; payment layer beneath it is 2000-vintage cash rails and a 2015 fraud engine**
- 🌏 **Region-gated storefronts with different method sets** — almost certainly different integrations per region
- 💱 **MCP multi-currency with JAL's own FX conversion fee** — they are already in the FX business on their own checkout
- 💳 **JAL Pay / JAL Payment Port (JAL × SBI)** — an active fintech build-out, and a banking-agency licence
- 🔴 **23 Dec 2025: ANA *and* JAL simultaneously unable to take reservations or issue tickets** (Nikkei). **Both carriers, same day — points at a shared upstream.** `[UNVERIFIED — paywalled, not fetched]`
- 🔴 **26 Dec 2024: JAL Pay transaction failures** — JAL's own notice, 「一部のお取引が成立していない事象」
- ✈️ **Hawaiian Airlines partnership ENDS 21 Apr 2026**, transferring to Alaska after the HA/Alaska merger

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

### Pain Vector Extraction

```
=== PAIN VECTOR EXTRACTION ===

Motion: GREENFIELD — none detected. Standard sequence; Phase 1 may note the
        absence of a routing layer.

⚠️ CONFLICT RESOLVED BEFORE DRAFTING. The five drafting instructions in this
   file said to frame observation 2 as "the rail set looks vendor-bounded."
   The CORRECTION dated 2026-09-19, further down the same file, REFUTES that
   causal claim: Peach Aviation is a Wellnet customer AND carries five code
   wallets. The correction is later and more specific, so it wins. Nothing in
   this sequence says or implies "your vendor won't let you."

Observable setup facts (all from the research file):
- PSS consolidated domestic + international onto Amadeus Altéa, Nov 2017;
  AXESS GDS wound down 31 Mar 2021  [Altéa dates search-summary corroborated]
- Cash / Pay-easy / net-banking rails on Wellnet, a vendor live since May 2000
  — verified via JAL's own outbound link to multiple-payment.biz
- Fraud on NTT Data CAFIS Brain, in full operation since January 2015 — JAL's
  own press release
- Card acquirer UNDISCLOSED — the single biggest hole in the research
- Region-gated POS storefronts with different method sets, proven by JAL's own
  JAL Pay terms excluding 「海外地区でのご購入」 as a separate channel
- Apple Pay present on international, ABSENT on domestic — verified by me on
  both flows
- No Japanese code wallet anywhere (PayPay, d払い, au PAY, Rakuten Pay, LINE Pay)
- No at-checkout instalment on either flow; 分割/リボ is post-purchase, issuer-side
- MCP multi-currency on international, with JAL's own FX conversion fee
- FY2025 revenue ¥2,012,515m (+9.1%), EBIT ¥218,004m (+26.4%) — records

Selected observations for Phase 1 (E1 bullets, ranked by materiality):
1. Modernisation asymmetry -> "You consolidated both PSSs onto one platform in
   2017. The payment layer under it still runs cash rails from a vendor live
   since 2000 and a fraud engine in production since January 2015."
   MATERIALITY: highest. Flattering about the hard thing they did, observational
   about the thing they didn't. Entirely first-party.
2. Apple Pay asymmetry -> "Apple Pay is on your international flow and not your
   domestic one."
   MATERIALITY: high, and it is the sample-set move — an asymmetry inside their
   own stack. Both halves are theirs, so neither is disputable.
3. Region-gated storefronts -> "Different method sets per region."

   HELD BACK, DELIBERATELY: the code-wallet absence. It is real and
   sourced-absent, but in Phase 1 it reads as "you don't take PayPay", which the
   file forbids. It moves to E3 framed as what the LCCs do, never as a vendor
   ceiling.

Bridge variant: A — complexity
Rationale: multi-region, fragmented. Region-gated storefronts with different
method sets, a separate cash vendor, a separate fraud engine, and an undisclosed
acquirer. That is complexity, not a single-provider limitation.

Hypothesis for Phase 2 (E3):
The 2017 consolidation stopped at the PSS. The payment layer underneath is still
per-region, so every method and every market is its own integration, and the
cost shows up as engineering time rather than as a line item.
Backing logic: different method sets per region + a 2000-vintage cash vendor +
a 2015 fraud engine + no at-checkout instalment in a market that converts
high-ticket on instalments.

Success case for Phase 3 (E4):
Selected case: Wingo
Tier: 1 — airline, and the only airline case in the library carrying numbers
Match rationale: low-cost carrier, multi-market, approval-rate problem solved by
automatic retries across multiple providers. Mechanism matches the hypothesis.
⚠️ Wingo is LATAM. The sequence says so explicitly and never implies Asia.
Numbers to lead with: +14% approval rate (initial implementation phase),
1,000+ payment methods, 3DS and fraud tooling
Optional benchmark: SKIP. The ~8% routing uplift is Yuno's own blog, not an
independent benchmark, and the IATA/EDC $20.3bn airline acceptance-cost figure
has only been seen via a vendor blog citing it — not traced to the primary
source. Neither is used.

Touch-by-touch angles:
- E2 angle: different method sets per region -> one integration to add any
  method or region, no per-region rebuild
- LK1 angle: Apple Pay on international, not domestic
- LK2 angle: the consolidation stopped at the PSS
- LK3 angle: Wingo's +14%
- LK4 angle: the undisclosed acquirer, unused until here
- E8 angle: clean exit, no new observation
```

---

### Phase 1 — Curiosity (Days 1–5)

#### Touch 1 — Email 1 · Day 1 · **Mon 5 Oct 2026**

**Subject:** Apple Pay on one JAL flow

```text
Hey {{recipient.first_name}},

Spent some time looking at JAL's payment setup. Three things stood out:

- You consolidated both PSSs onto one platform back in 2017. The payment layer under it still
  runs cash and Pay-easy rails from a vendor live since 2000, and a fraud engine in production
  since January 2015.
- Apple Pay is on your international flow and not your domestic one.
- Your region-gated storefronts carry different method sets.

That kind of setup usually comes with some complexity.

I work at Yuno, a top-100 fintech, a16z-backed. We consider ourselves the "everything payments"
platform: one integration, every PSP, every method, every market.

Rather than pitch you based on assumptions, is there anything payment-related you're working
through that we might be able to help with?

Best,
Prateek
```

#### Touch 2 — Email 2 · Day 3 · **Wed 7 Oct 2026** · REPLY IN THREAD

```text
Hey {{recipient.first_name}},

Following up. Wanted to put a bit more behind what Yuno actually does, and how it would address
what I flagged.

We sit above the providers you already run, so nothing gets ripped out. Routing happens per BIN,
market and method, to whichever rail performs best at that moment. If a provider degrades, traffic
fails over automatically. And adding a new method, rail or acquirer is a configuration change
rather than a new integration.

That last part is the one that maps to your setup. Right now a method added in one region looks
like it has to be built again for the next. Through one layer, the method goes on once and every
region can carry it.

I'll keep sharing what I'm seeing every few days. If your stack's where you want it, just say the
word and I'll back off. Otherwise happy to go deeper.

Cheers,
Prateek
```

#### Touch 3 — LinkedIn message 1 · Day 5 · **Fri 9 Oct 2026**

```text
Hey {{recipient.first_name}} — figured I'd flag this here too in case it's more useful than email.
Quick one: Apple Pay shows up on JAL's international payment flow but not the domestic one. Curious
whether that's deliberate, and whether it maps to anything you're working through on the payments
side.
```

---

### Phase 2 — Diagnosis (Days 7–9)

#### Touch 4 — Email 3 · Day 7 · **Tue 13 Oct 2026** · NEW EMAIL
*(Mon 12 Oct is スポーツの日 / Sports Day, a public holiday in Japan. Skipped.)*

**Subject:** Where the 2017 consolidation stopped

```text
Hey {{recipient.first_name}},

Going to take a swing at this. Based on what I can see, my read is that the 2017 consolidation
stopped at the PSS, and the payment layer underneath is still per-region.

Different method sets per region usually means a separate integration behind each one. The cost of
that tends not to appear as a line item. It appears as engineering time every time someone asks for
a method in one market and it has to be built again for the next.

The other thing I notice is instalments. Japan converts high-ticket purchases on them, and on both
your flows the conversion is post-purchase and issuer-side. There's nothing at the point of sale.

At Yuno, a16z-backed and top-100 fintech, we sit above your existing providers so you can add
methods and regions without another build. Keep your stack, add what's missing.

When you add a method in one region today, how much of that work carries over to the others?

Thursday is open for me. Would 3pm your time work for 15 minutes, or would Friday 11am be easier?

All the best,
Prateek
```

#### Touch 5 — LinkedIn message 2 · Day 9 · **Thu 15 Oct 2026**

```text
Hey {{recipient.first_name}} — sent a longer note over email this week. Short version: my read is
the 2017 PSS consolidation never reached the payment layer, so each region still carries its own
integration and its own method set. If that's anywhere on your radar, would Tuesday 20th at 4pm
your time work for a quick 15?
```

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · **Mon 19 Oct 2026** · NEW EMAIL

**Subject:** How Wingo solved this

```text
Hey {{recipient.first_name}},

On the read I shared last week, sharing a quick example of what solved looks like.

Wingo, a low-cost carrier in Latin America, partnered with Yuno to stop losing bookings to failed
payments across its markets. Their results, from their region rather than yours:

- Approval rate up 14% in the initial implementation phase (you read that right)
- Over 1,000 payment methods reachable through the one layer
- 3DS and fraud tooling handled in the same place

The mechanism is the part worth borrowing. Yuno retries a failed payment automatically through a
different provider, rather than returning a decline to the passenger. Same orchestration layer above
their existing stack, no rip-out.

Qatar Airways, Copa Airlines and Avianca run on the same layer, though I don't have published
numbers for those three.

Would Thursday 22nd at 10am your time work for 15 minutes, or Friday 23rd at 3pm?

Full case here if useful: https://y.uno/en/newsroom/wingo-improves-payment-efficiency-with-yuno-as-strategic-partner

Looking forward to it,
Prateek
```

#### Touch 7 — Email 5 · Day 13 · **Wed 21 Oct 2026** · MANUAL
*Placeholder — manual creative approach. Do not auto-write.*
**Suggested angle:** the Cathay Pacific comparison. Adyen expanded **direct acquiring** with Cathay to **six markets including Japan** (Adyen newsroom, 23 Mar 2026), with a reported **10% authorisation-rate increase in India**. A direct competitor on JAL's own routes, publicly quantified. Name the airline and what it did; never imply Cathay is a Yuno customer.

#### Touch 8 — Email 6 · Day 15 · **Fri 23 Oct 2026** · MANUAL
*Placeholder — second manual approach, different format from E5.*
**Suggested angle:** a short checkout teardown. The domestic and international flows side by side, screenshots of both method lists, with the Apple Pay line highlighted. Visual, first-party, and it proves the research in a way prose cannot.

#### Touch 9 — LinkedIn message 3 · Day 17 · **Tue 27 Oct 2026**

```text
Hey {{recipient.first_name}} — Wingo lifted approval 14% by retrying failed payments through a
second provider instead of handing the passenger a decline. Worth 15 minutes to see whether it maps
to your setup? Thursday 29th at 2pm your time is open.
```

---

### Touch 10 — Email 7 · Day 19 · **Thu 29 Oct 2026** · MANUAL
*Placeholder — manual creative bridge. Anchor to something fresh.*
**Suggested anchors:** the **Hawaiian Airlines partnership ending 21 Apr 2026** and transferring to Alaska after the HA/Alaska merger — a live commercial change with payment and settlement consequences. Or the FY2025 results: **¥2.01 trillion revenue, first time above ¥2 trillion since the 2012 relisting**. ⛔ Not the Dec 2025 dual-carrier outage — still paywalled and unverified.

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21 · **Mon 2 Nov 2026**
*(Tue 3 Nov is 文化の日 / Culture Day, a public holiday in Japan. Avoided for the slot.)*

```text
Hey {{recipient.first_name}} — last ping from me here. One thing I never worked out from the
outside: who actually acquires your card volume. If that question is interesting to whoever owns it,
Thursday 5th at 11am your time is open for 15 minutes.
```

#### Touch 12 — Email 8 · Day 23 · **Wed 4 Nov 2026** · REPLY IN THREAD to Touch 4 or 6

```text
Hey {{recipient.first_name}},

Going to stop pinging unless you want to pick this back up.

If the timing is just off, happy to circle back after the new year. And if payments sit with someone
else at JAL, I'd be glad to be pointed their way.

If it ever comes back up, just reply here.

All the best,
Prateek
```

---

### Source Notes

- ✅ **PSS consolidated onto Amadeus Altéa, Nov 2017** — research file. ⚠️ Altéa dates are search-summary corroborated; the file's own guidance is to say *"has run Altéa since 2017"*, which E1 and E3 do
- ✅ **Wellnet, cash / Pay-easy / net-banking rails, live since May 2000** — verified via JAL's own outbound link to `multiple-payment.biz`. **E1 says "a vendor", not "Wellnet"** — the file's precision caveat is that JAL links to Wellnet for the institution list, not that JAL redirects to it
- ✅ **NTT Data CAFIS Brain, in full operation since January 2015** — JAL's own press release
- ✅ **Apple Pay present on international, absent on domestic** — verified first-hand on both flows
- ✅ **Region-gated storefronts with different method sets** — JAL's own JAL Pay terms exclude 「海外地区でのご購入」 as a separate channel
- ✅ **No at-checkout instalment on either flow; 分割/リボ post-purchase and issuer-side** — sourced-absent from both flows
- ✅ **Wingo: +14% approval, 1,000+ methods, 3DS and fraud tooling** — y.uno newsroom, verified live 2026-09-15. **E4 states it is Latin America**
- ✅ **Qatar Airways, Copa Airlines, Avianca are Yuno customers** — Yuno's own site-wide list. **No number attached to any of them**, per the library rule
- ⚠️ **Card acquirer is undisclosed** — LK4 asks about it rather than asserting anything. Nothing in the sequence names a gateway or acquirer, because none is established
- ⛔ **Not used: the Dec 2025 dual-carrier outage.** Paywalled and unverified
- ⛔ **Not used: "your vendor won't let you carry code wallets."** Refuted — Peach Aviation is a Wellnet customer and carries five code wallets
- ⛔ **Not used: the $11.4B revenue figure.** Refuted; the primary 決算短信 gives ¥2,012,515m
- ⛔ **Not used: UnionPay or PayPal acceptance.** Search-summary only
- ⛔ **Not used: the ~8% routing uplift or the IATA/EDC $20.3bn figure.** The first is Yuno's own marketing; the second has not been traced to the primary source

### Scheduling notes
- **Mon 12 Oct 2026 is スポーツの日 (Sports Day)** and **Tue 3 Nov 2026 is 文化の日 (Culture Day)**, both Japanese public holidays. Neither carries a send or a proposed slot.
- Five distinct meeting slots, all stated in the prospect's local time: Thu 15 Oct 3pm · Fri 16 Oct 11am · Tue 20 Oct 4pm · Thu 22 Oct 10am / Fri 23 Oct 3pm · Thu 29 Oct 2pm · Thu 5 Nov 11am. JST is IST+3.5, so a 3pm JST slot is 11:30 IST — comfortable for both.
- No booking link anywhere. The reply is the booking.

### Success Case Alternatives
- **Qatar Airways / Copa / Avianca** — nameable airline credibility, but no published metrics, so none can carry E4
- **Viva Aerobus** — airline, but its 75% is a **NOVA** result (AI voice callback after a failed payment), not routing. Right case only if JAL turns out to hand failed payments to a human
- **inDrive** — Tier 2 if a multi-country scale argument is ever needed instead of the airline angle

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 17 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED as a bound, from a primary filing I extracted myself.** **Revenue ¥2,012,515m FY2025.** Even at an implausibly high **¥300,000 (~US$2,000) per booking**, that is ~6.7m bookings/year = **~560k/month**, and ancillaries bill separately. **Every plausible divisor clears 100k by a wide margin.** ⚠️ Passengers, international/domestic split and cargo share could NOT be obtained — so no passenger-derived figure is offered. |
| Orchestration status | **+4** | ✅ **None detected.** Same shape as ANA: a third-party vendor on cash rails, a separate 2015 fraud engine, an undisclosed card acquirer, and region-gated POS sites with differing method sets. ⚠️ Rests partly on absent hits for the card layer, but the **region-fragmented method sets are affirmative** evidence of per-region integration rather than one routed layer. |
| 3+ countries | **+3** | ✅ International network, **MCP multi-currency pricing**, and at least four regional FAQ/POS origins (`jal-cn-jp`, `faq-en`, `faq-sr`, `faq-ar-en`) plus a `world/en` site. |
| Multiple PSPs | **+2** | ✅ **Structurally proven:** Wellnet on the cash/bank rails is demonstrably not the card acquirer, and JAL's own JAL Pay descriptors show **separate international "サインレス"/"チケットレス" merchant descriptors** from domestic — implying distinct international CNP acquiring. ⚠️ Only **Wellnet** and **CAFIS Brain** can be named, and CAFIS Brain is fraud, not acquiring. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Sourced absence on both flows, verified by me.** No PayPay, Rakuten Pay, LINE Pay, d払い, au PAY, Amazon Pay, Paidy or Google Pay, and no at-checkout instalments. ⚠️ **Read the nuance before pitching:** the Wellnet e-money ceiling was **retracted 2026-09-19** — Peach is a Wellnet customer with five code wallets, so the absence is a choice, not a constraint. JAL also runs its own competing prepaid wallet, which is the likelier explanation. **The gap is real; the framing must be competitive, not vendor-constraint.** |
| Recent expansion | **0** | ⬜ Not awarded. The **Hawaiian → Alaska transition (21 Apr 2026)** is a partnership change, not expansion, and new routes could not be established. |
| Payment issues reported | **0** | ⬜ **Not awarded — and this is the row most likely to move.** A strong corpus exists but **not one item was fetched**: the 23 Dec 2025 **dual-carrier ANA+JAL outage** (Nikkei, paywalled), a 26 Dec 2024 **JAL Pay transaction-failure notice** on JAL's own site, an open **JAL app v6.0.0 defect** from 15 Apr 2026, a standing FAQ where pressing the internet-transfer button 10+ times hard-errors and blocks purchase, and a standing FAQ where **Alipay payment succeeds but confirmation fails** — a textbook capture-succeeded-reconciliation-failed pattern. **I do not award points on unverified data.** Verifying any two of these likely makes this +2. |
| Funding >$10M | **0** | ❌ TSE-listed (9201). No round. |
| High traffic outside home | **0** | ⬜ No traffic data, and the domestic/international split could not be obtained. |
| Competitor using orchestration | **0** | ❌ **JAL's closest competitor is ANA, and our own ANA file scores it greenfield with no orchestration.** The honest read for a Japanese carrier is that nobody in the peer set has adopted. |
| Payment job postings | **0** | ⬜ Not found. |

**Tier: 17 / 29 → ⭐ High Priority.** No override applied.

> **Compare with ANA (23/29) deliberately.** ANA scores higher on three rows JAL cannot match — a live, publicly-apologised-for migration; verified money-movement defects; and a JV partner already running orchestration. **JAL's case is quieter and structurally cleaner: the platform modernisation is done, so the payment layer is the obvious remaining seam.**

### Source Notes
- ✅ **The international method table, Apple Pay's presence, MCP, the absence of instalments and the Wellnet outbound link were all verified by me** from Wayback snapshot `20260309053322` of `jal.co.jp/jp/ja/inter/payment/`. `multiple-payment.biz` is **the only non-analytics third-party host on that page.**
- ✅ **Wellnet's identity, its "all of Japan's major domestic airlines" claim and its complete method set were verified by me** at `multiple-payment.biz`, which is **directly fetchable with no WAF**.
- ✅ **FY2025 financials extracted by me from the primary 決算短信 PDF** (filed 2026-04-30): 売上収益 ¥2,012,515m (+9.1%), EBIT ¥218,004m (+26.4%), 親会社帰属当期利益 ¥137,604m (+28.6%), prior year ¥1,844,095m.
- ✅ **CAFIS Brain** is from JAL's own January 2015 press release.
- ⚠️ **The domestic method set** was verified by me during the ANA batch, from Wayback snapshot `20260606014023`.
- ⚠️ **Altéa dates (2017 go-live, 2019 extension, AXESS wind-down 2021)** are search-summary corroborated across multiple outlets, **not re-confirmed for 2026.**
- ⚠️ **Alipay/UnionPay/PayPal on regional sites** — Alipay has a JAL FAQ article title behind it; the other two are search-synthesis only.
- ❌ **`jal.co.jp` AND `press.jal.co.jp` both return 403 (Akamai).** Add both to the blocklist. Wayback works for both.
- ❌ **`faq-jp.jal.co.jp` returns 200 but is a Salesforce Experience Cloud SPA** — curl gets a loading shell only.
- 🚩 **ENVIRONMENT FAULT WORTH RECORDING.** Two fetch attempts against `faq.jal.co.jp/app/answers/detail/...` returned **HTTP 000 with proxy-injected content from an entirely unrelated site — a Ticketek press release.** The agent discarded that output and no claim rests on it. **The agent proxy can mis-serve a host's content. That is a new false-positive class, alongside substring collisions and stale scratchpad artifacts: always confirm fetched content actually belongs to the host you asked for.**

### Manual Research Recommendations
> **1. One Wayback fetch of `jal.co.jp/footer/security.html` and `/footer/policy/`.** Japanese privacy policies routinely enumerate 委託先 by name — **this is the likeliest place the card acquirer is disclosed**, and it is the biggest hole.
> **2. Verify the 23 Dec 2025 dual-carrier outage.** Both ANA and JAL down the same day is the best potential cold open in this batch, and it would also tell us whether there is a shared upstream worth naming.
> **3. Read one regional POS site** (`jal-cn-jp`, or the `world/en` site). **This is where the orchestration pain actually lives** — different methods per region almost certainly means different integrations per region.
> **4. Get passengers, the domestic/international split and cargo share** from the 決算短信 or 「JALグループ早わかり」.

---

## Executive Summary

JAL posted **record FY2025 revenue of ¥2.01 trillion (+9.1%)** — a figure I extracted from the primary filing, and one that **refutes the target list's $11.4B**, which is stale by roughly a year and a currency move. The account's defining feature is an asymmetry: **JAL completed the hard, expensive platform work nine years ago**, consolidating domestic and international onto Amadeus Altéa in 2017 and retiring its own GDS subsidiary — **while the payment layer underneath it did not move with it.** Cash and bank rails sit with **Wellnet**, a vendor operating since May 2000; fraud runs on **NTT Data CAFIS Brain**, live since January 2015; the **card acquirer is undisclosed and nobody can name it**; and the estate is split across **region-gated storefronts with different method sets per region**. The most useful thing found is a category insight rather than a company one: JAL's own payment page links out to Wellnet, whose site claims **all of Japan's major domestic airlines** as customers and whose electronic-money set stops at Rakuten Edy, Mobile Suica and JCB Premo — **no PayPay, no code wallets of any kind.** ⛔ **I originally read that as the cause of the wallet gap at JAL and ANA; that reading is RETRACTED (see the correction block above)** — Peach Aviation runs five code wallets on top of a Wellnet konbini rail, so the ceiling binds the rail, not the airline. Two premises I carried in were wrong and are corrected in this file: **JAL does accept Apple Pay**, on international, and **JAL is not mid-migration** — which means the ANA opener must not be reused here.

</details>
