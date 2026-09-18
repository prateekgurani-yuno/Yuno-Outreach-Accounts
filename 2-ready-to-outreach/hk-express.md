# HK Express

**Status:** 🟢 Ready to outreach — 12-touch sequence drafted
**ICP Score:** 18 / 29 → ⭐ **High Priority**
**Industry:** Airlines (low-cost carrier, short-haul) · **HQ:** Hong Kong — wholly owned by **Cathay Pacific** · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** **In-house** — and it is the best-evidenced in-house call in this repo, on live architecture rather than absent search hits (see 3B). **Respect the build decision. Never argue they need orchestration.**

---

> ## 🎯 THE HOOK — one group, two completely disjoint payment stacks, and the LCC built its own
>
> We researched **Cathay Pacific mainline** earlier in this batch. Setting the two side by side is the entire pitch, and **every line below was verified by me first-hand today.**
>
> | | **Cathay mainline** | **HK Express** |
> |---|---|---|
> | **Acquiring** | **Adyen direct acquiring, 6 markets**, since 2014, **+10% auth in India** | **Zero Adyen.** Own service at `manage.hkexpress.com/w/payment` |
> | **3DS** | Adyen-native | **CardinalCommerce** — `cardinalPostMessageUrl:"https://client.cardinaltrusted.com"` |
> | **Fraud** | not established | **Accertify**, CNAME'd onto `acfrvpprdslbprod.hkexpress.com` |
> | **PSS** | Amadeus Altéa | **Navitaire New Skies** (`nsk_token`) |
> | **Cost recovery** | **0.70% ad valorem** on AU/NZ, capped AUD 120 / NZD 70 | **Flat fee per segment by point of origin** — see below |
> | **Surcharged markets** | AU, NZ | **JP, TW, CN, TH, KR, PH, VN — zero overlap** |
>
> **The Adyen release scopes itself to "the airline" — mainline only.** HK Express appears in it solely as About-us boilerplate.
>
> ### The E-Payment Fee — verified verbatim from their own fees page
> > **"E-Payment Fee (i.e. Convenience Fee)** — The fee is charged to each passenger when booking flights departing from the following departure regions… **Per customer per segment: JPY 810 · TWD 220 · CNY 43 · THB 230 · KRW 7,700 · PHP 350 · USD 7.** E-payment fee will be applied to bookings **not originating from Hong Kong and Malaysia.**"
>
> **Read what that is.** It recovers acceptance cost by **geography of sale**, not by tender — a flat nominal amount per segment, unchanged in at least 21 months (byte-identical Wayback snapshots at `20241230084717` and `20250527123703`) through a period when JPY, KRW and THB all moved materially against HKD. **That is what it looks like when a merchant cannot see acceptance economics per rail.** Hong Kong and Malaysia are exempt — the two markets where its wallet mix is presumably cheapest.
>
> ### And the home-market rail gap
> **Hong Kong is the origin or destination of every single flight, and the checkout carries no FPS, no PayMe and no Octopus online.** Octopus is accepted **inflight only** — *"The accepted payment methods onboard will be Octopus card, Visa, Mastercard and JCB"* — and appears nowhere in the booking flow. **The home carrier's home rails are the ones missing.**

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** HK Express is Hong Kong's only LCC, wholly owned by Cathay Pacific, flying short-haul to Japan, Korea, Taiwan, Mainland China, Southeast Asia and Saipan. **FY2025: 7,912,000 passengers (+29.7%), passenger revenue HK$6,394m (+6.7%) — and a loss before net finance charges and tax of HK$(996)m, roughly five times worse than FY2024.** Yield fell 15.3% and revenue per ASK fell 19.1%. It is the group's only loss-making airline segment, at ~5.5% of group revenue.

**SimilarWeb total visits:** **Not obtained.** No data supplied. Country profile unverified; **no split invented.**

### Accepted methods — ~25 tenders, dense Asian wallet coverage
**Cards:** Visa · Mastercard · Amex · JCB · **China UnionPay** · **Diners Club / Discover**
**China:** Alipay CN · AlipayHK · Alipay International · **Alipay+** (umbrella) · WeChat Pay
**Japan:** PayPay · **Korea:** Kakao Pay · NAVER Pay · Toss Pay
**Philippines:** GCash · Maya · BillEase · BPI · **Thailand:** Rabbit LINE Pay · TrueMoney · K PLUS
**Malaysia:** Boost · Touch'n Go eWallet · FPX · **Regional:** GrabPay · **HK:** Divit
**Loyalty:** **Asia Miles AND reward-U points** — two loyalty currencies, with a dedicated `/v1/payment/miles-otp` endpoint
**Currencies:** nine (HKD, JPY, USD, CNY, KRW, THB, TWD, PHP, MYR) with per-tender restrictions, plus a live **DCC quote** endpoint

⚠️ **Apple Pay / Google Pay — genuinely ambiguous.** Image keys exist in the live IBE dictionary, so they are wired in, but **neither appears on the published Payment Options page or the Payment FAQ**, and a dated App Store review (2025-11-27, 2★) is titled 消失的Apple Pay — *"the disappearing Apple Pay"*. **Do not assert either way.**

### ❌ Absent — sourced against their own tender dictionary
**FPS · PayMe · Octopus (online) · UATP · Digital Renminbi (e-CNY) · VietQR · QRPh · PayTo · UPI · RuPay · PayTM · PromptPay · KCP · Atome · Klarna · Affirm · Zip · iDeal · Sofort**

### Known PSPs
| Layer | Finding |
|---|---|
| **Payment abstraction** | ✅ **In-house** — `manage.hkexpress.com/w/payment`, with `/external/v1/payment/create-payment` **and** `/external/v2/...` live in parallel, plus session, cancel, DCC-quote and miles-OTP paths |
| **3DS** | ✅ **CardinalCommerce (Visa) Centinel** — verified in the chunk and corroborated by `form-action … cas.client.cardinaltrusted.com` in the CSP |
| **Fraud** | ✅ **Accertify (Amex)** — collector CNAME'd onto an hkexpress.com host |
| **PSS** | ✅ **Navitaire New Skies** — `nsk_token`; first-party confirmation on their Travel Agents page: *"we can connect you via our easy-to-implement Navitaire NewSkies API"* |
| **Acquirer / gateway** | ❌ **NOT ESTABLISHED.** Terminated server-side behind their own `/w/payment`. CardinalCommerce points at **Cybersource** (both Visa-owned) but **that is inference, not evidence. Do not name one.** |

### 🧩 A third stack nobody controls
**HK Express Holidays is white-labelled Expedia** — `hk.holidays.hkexpress.com` serves Expedia Group's `blossom-flex-ui` / `uitk` bundles from `c.travel-assets.com` with the OneKey/Expedia mark. **Packages payment is Expedia's, not the airline's.** Three payment stacks across one group.

### Buying signals
- 🔴 **HK$996m loss, ~5× worse YoY; yield −15.3%, RASK −19.1%** — cost pressure is acute and documented
- 💳 **A flat origin-based convenience fee unchanged for 21+ months** while FX moved
- 🇭🇰 **No FPS, no PayMe, no Octopus online in its own home market**
- 🏗️ **~25 tenders, 9 currencies, 37 destinations, 7 surcharge-bearing markets — all self-maintained**
- 📈 **Passengers +29.7%**, "launching multiple new routes" cited by the parent
- 🤝 **Cebu Pacific — a direct regional LCC competitor it overlaps with on Manila and Clark — runs CellPoint Digital orchestration** (established in our own Cebu file)

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

### Pain Vector Extraction

```
=== PAIN VECTOR EXTRACTION ===

Motion: IN-HOUSE, and the evidence is unusually strong. They built a real
        payment abstraction and it works. NEVER "you need orchestration."
        Anchor on reach and opportunity cost, exactly as the motion override says.

Observable setup facts (verified first-hand today, 2026-09-18):
- ZERO Adyen in any HK Express asset, while the mainline runs Adyen direct
  acquiring in six markets with a published +10% auth result in India
- Own payment service: endpointPaymentHost + /external/v1/payment/create-payment,
  AND /external/v2/... live in parallel, plus session, cancel, DCC-quote, miles-OTP
- cardinalPostMessageUrl:"https://client.cardinaltrusted.com"  (CardinalCommerce 3DS)
- accertifyDataCollectorUrl CNAME'd onto acfrvpprdslbprod.hkexpress.com  (Accertify)
- nsk_token  (Navitaire New Skies), confirmed on their own Travel Agents page
- E-Payment Fee, verbatim: "Per customer per segment JPY 810 / TWD 220 / CNY 43 /
  THB 230 / KRW 7,700 / PHP 350 / USD 7 ... not originating from Hong Kong and Malaysia"
- That fee table is byte-identical in Wayback snapshots 20241230084717 and
  20250527123703 — unchanged 21+ months through material JPY/KRW/THB moves
- ~25 tenders, 9 settlement currencies, 37 destinations, live DCC quote endpoint
- NO FPS, NO PayMe, NO online Octopus — in Hong Kong. Octopus is inflight only.
- FY2025: 7,912,000 pax (+29.7%), passenger revenue HK$6,394m, LOSS HK$(996)m
  ~5x worse YoY, yield -15.3%, RASK -19.1%

Selected observations for Phase 1 (E1 bullets, ranked by materiality):
1. The origin-based fee -> "Your e-payment fee is a flat amount per segment set by
   point of origin — JPY 810, KRW 7,700, THB 230 — with Hong Kong and Malaysia
   exempt. It's read the same on your fees page since at least December 2024."
   MATERIALITY: highest. First-party, quantified, and the 21-month freeze is the
   part that says something: acceptance cost is being recovered by geography
   rather than by rail, and it is not being repriced as FX moves.
2. The home-market rail gap -> "You carry around 25 tenders including PayPay,
   Kakao Pay, GCash and Touch'n Go — and no FPS, no PayMe, and Octopus only
   inflight."
   MATERIALITY: high. An asymmetry inside their own tender list: dense coverage
   of everyone else's local rails, none of their own.

   HELD AT 2. DELIBERATELY NOT IN E1: the Cathay comparison. It is the strongest
   card in the deck and it is also the one most likely to read as "your parent
   does it better," so it goes in E3 as a question about whether the group result
   travels, once a conversation exists. The loss figures are NEVER used — quoting
   a HK$996m loss at someone who works there is not an observation, it's a jab.

Bridge variant: B — limitations
Rationale: a single visible payment estate plus strong growth signals (pax +29.7%,
ASK +31.9%, new routes). B's "at your stage, that kind of setup usually comes with
some limitations" is the only transition that fits a merchant who built their own
layer without implying the build was a mistake.

Hypothesis for Phase 2 (E3):
The in-house layer was built to make payments work, and it does — but it doesn't
give them acceptance economics per rail, which is why cost gets recovered by
geography instead.
Backing logic: a flat nominal fee per point of origin, unchanged for 21 months
through material FX movement, is what you charge when you cannot see what each
tender actually costs you in each market. Twenty-five tenders across nine
currencies and seven surcharge-bearing origins is a lot of surface to price
blind. And the two markets that are exempt are the two where the wallet mix is
presumably cheapest — which suggests someone already knows the mix matters.

Success case for Phase 3 (E4):
Selected case: Wingo
Tier: 1 on industry (airline, the only quantified airline case), 2 on pattern.
      STATED AS SUCH.
Match rationale: Wingo is an LCC, which matters — the cost-per-transaction
conversation is an LCC conversation. Its "1,000+ payment methods through one
integration" bullet speaks to carrying 25 tenders without maintaining 25
integrations, which is precisely HK Express's standing cost.
Numbers: +14% approval rate (initial implementation phase) · 1,000+ methods
through one integration · 3DS and fraud tooling in the same layer
Plus one line naming Qatar Airways, Copa Airlines and Avianca — NO NUMBERS.
Optional benchmark: SKIP. The ~8% figure is Yuno's own blog, and the IATA/EDC
$20.3bn figure is untraced to primary source per our own skill file.

Touch-by-touch angles:
- E2 angle: the origin-based fee -> ONE mechanism: per-rail, per-market cost and
  approval visibility in one layer, so acceptance can be priced by tender rather
  than by country
- LK1 angle: the fee table unchanged since 2024, one sentence
- LK2 angle: you can't price what you can't see per rail
- LK3 angle: Wingo — 1,000+ methods on one integration
- LK4 angle: FRESH — Octopus accepted inflight but not online
- E8 angle: clean exit, offer to circle back after the FY2026 interim

*** NEVER IN ANY TOUCH ***
- "You need orchestration." They built one.
- The HK$996m loss, the yield decline, or any financial distress framing.
- Any acquirer or PSP name — we do not know theirs, and naming CardinalCommerce
  or Accertify as though we do would be wrong and obvious.
- Any Yuno competitor, including the one Cebu Pacific runs.
- Apple Pay or Google Pay as absent. Genuinely ambiguous.
```

**Calendar.** Day 1 anchored to **Monday 9 November 2026**, deliberately **after the Cathay
Pacific sequence in this same batch finishes (5 Nov)**. ⚠️ **This is not an arbitrary offset:
Cathay's own E7 manual touch is *about* HK Express.** Running both in parallel would have
Prateek raising HK Express with the parent while separately pitching the subsidiary. **Do not
bring this sequence forward without re-reading the Cathay file's Day 19 touch.**

**Times are HKT (UTC+8), IST+2:30.** Slots 14:00–16:00 HKT = 11:30–13:30 IST. No Hong Kong
public holiday falls inside 9 Nov – 9 Dec; **Christmas holidays begin after the window closes.**

---

### Phase 1 — Curiosity (Days 1–5)

#### Touch 1 — Email 1 · Day 1 · Mon 9 Nov

**Subject:** Your e-payment fee by point of origin

```text
Hey {{recipient.first_name}},

Spent some time on HK Express's payment setup. Two things stood out:

- Your e-payment fee is a flat amount per segment set by point of origin — JPY 810, KRW 7,700, THB 230 — with Hong Kong and Malaysia exempt. It's read the same on your fees page since at least December 2024.
- You carry around 25 tenders including PayPay, Kakao Pay, GCash and Touch'n Go, and no FPS, no PayMe, and Octopus only inflight.

At your stage, that kind of setup usually comes with some limitations.

I work at Yuno — top-100 fintech, a16z-backed. We consider ourselves the 'everything payments' platform: one integration, every PSP, every method, every market.

Rather than pitch you based on assumptions, is there anything payment-related you're working through that we might be able to help with?

Best,
Prateek
```

#### Touch 2 — Email 2 · Day 3 · Wed 11 Nov · REPLY IN THREAD

```text
Hey {{recipient.first_name}},

Following up — wanted to put a bit more behind what Yuno actually does, and how it would address what I flagged.

- We sit above what you've already built. Additive, and your own payment service stays where it is.
- Every tender, market and currency reports into one place, so cost and approval are visible per rail rather than per country.
- Adding a method or a provider becomes configuration rather than an integration.
- The same layer carries 3DS and fraud, so those stop being separate vendor relationships to maintain.

On the fee specifically — a flat amount by point of origin is a perfectly rational way to recover acceptance cost when you can't see what each tender costs you in each market. That visibility is the bit we'd add. What you do with it commercially is your call.

I'll keep sharing what I'm seeing every few days. If your stack's where you want it, just say the word and I'll back off — otherwise happy to go deeper.

Cheers,
Prateek
```

#### Touch 3 — LinkedIn message 1 · Day 5 · Fri 13 Nov

```text
Hey {{recipient.first_name}} — figured I'd flag this here too in case more useful than email. Quick one: your e-payment fee table reads the same today as it did in December 2024, across seven points of origin, while JPY, KRW and THB have all moved against HKD. Curious if that maps to anything you're working through on the payments side.
```

---

### Phase 2 — Diagnosis (Days 7–9)

#### Touch 4 — Email 3 · Day 7 · Tue 17 Nov · NEW EMAIL

**Subject:** Read on your acceptance economics

```text
Hey {{recipient.first_name}},

Going to take a swing at this — based on what I see, my read is that the in-house layer was built to make payments work, and it does, but it doesn't give you cost and approval per rail. So acceptance gets recovered by geography instead.

Two things point that way. The fee is a flat nominal amount per point of origin rather than anything that tracks tender mix, and it hasn't been repriced in roughly two years while the currencies underneath it moved. And the two exempt markets, Hong Kong and Malaysia, are the two where your wallet mix is presumably cheapest — which suggests someone already suspects the mix matters.

Twenty-five tenders across nine currencies is a lot of surface to price blind.

At Yuno (a16z-backed, top-100 fintech), we sit above what you've built so cost and approval are visible per method and per market — keep your stack, add what's missing.

Thursday is open for me — would 15:00 or 16:00 your time work for a quick 15 minutes?

Best,
Prateek
```

#### Touch 5 — LinkedIn message 2 · Day 9 · Thu 19 Nov

```text
Hey {{recipient.first_name}} — sent a longer note over email this week. Short version: you can't price acceptance per rail if you can't see it per rail, which is usually why it ends up priced per country instead. If that's anywhere on your radar, would Monday the 23rd at 14:00 your time work for a quick 15?
```

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · Mon 23 Nov · NEW EMAIL

**Subject:** How Wingo solved this

```text
Hey {{recipient.first_name}},

On the read I shared last week — an example of what solved looks like. Wingo is a Colombian low-cost carrier, so different region, but the same shape of problem: a lot of tenders, thin margins, and cost per transaction that actually moves the P&L.

They put Yuno above their existing setup:

- 1,000+ payment methods available through one integration, rather than one integration per method (you read that right)
- +14% approval rate from the initial implementation phase
- 3DS and fraud handled in the same layer instead of as separate vendors

That first bullet is the one I'd point at. You're already carrying around 25 tenders across nine currencies — the question isn't whether you can run them, you clearly can. It's what maintaining them costs you every time a market adds a rail.

Same layer above what they'd already built — no rip-out. Qatar Airways, Copa Airlines and Avianca run on it too.

One thing I'm curious about: when you added the Korean and Thai wallets, roughly how much of that was commercial versus engineering time?

Wednesday the 25th is open — would 15:30 your time work?

Full case here if useful: https://y.uno/en/newsroom/wingo-improves-payment-efficiency-with-yuno-as-strategic-partner

Thanks,
Prateek
```

#### Touch 7 — Email 5 · Day 13 · Wed 25 Nov · ⚠️ MANUAL

> **Placeholder — Prateek writes this one.**
>
> **Suggested angle: the group question, handled carefully.** Cathay mainline runs Adyen
> direct acquiring in six markets and published a **+10% authorisation uplift in India**; HK
> Express runs its own stack and shares none of it. **Frame it as "does that result have a
> path to you?"** — a genuine and flattering question about group leverage. ⚠️ **Never as
> "your parent is doing it better."** If it cannot be written that way, skip it.

#### Touch 8 — Email 6 · Day 15 · Fri 27 Nov · ⚠️ MANUAL

> **Placeholder — different format from E5.**
>
> **Suggested angle:** a one-page grid of their own 25 tenders against their nine settlement
> currencies, marking the per-tender restrictions they publish themselves (JCB and UnionPay
> exclude PHP; Alipay is limited to a subset). Built entirely from their Payment Options
> page. **The restriction cells make the maintenance burden visible without a word of
> commentary.**

#### Touch 9 — LinkedIn message 3 · Day 17 · Tue 1 Dec

```text
Hey {{recipient.first_name}} — Wingo got 1,000+ payment methods through a single integration instead of maintaining one per method, and +14% approval alongside it. Worth 15 minutes to see if it maps to your setup? Thursday the 3rd at 14:30 your time is open.
```

---

### Between Phases (Day 19)

#### Touch 10 — Email 7 · Day 19 · Thu 3 Dec · ⚠️ MANUAL

> **Placeholder — manual creative bridge.**
>
> **Freshest unused anchor:** the **Holidays channel is white-labelled Expedia** — a third
> payment stack in the group that the airline doesn't control at all. That is a real
> architecture observation and it is nobody's fault. ⚠️ **Verify it still renders Expedia
> bundles before sending**; white-label arrangements change.

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21 · Mon 7 Dec

```text
Hey {{recipient.first_name}} — last LK ping from me on this. One thing I never worked out: Octopus is accepted onboard but not in the booking flow, in your home market. If timing works, Wednesday the 9th at 16:00 your time is open for a quick 15.
```

#### Touch 12 — Email 8 · Day 23 · Wed 9 Dec · REPLY IN THREAD to E3

```text
Hey {{recipient.first_name}},

Going to stop pinging unless you want to pick this back up.

You're heading into peak season with a lot of new routes still maturing, which is the worst possible moment to open a payments workstream. If timing's just off, happy to circle back after the interim results.

If it ever comes back up, just reply here — and if payments sits elsewhere, happy to be pointed there.

All the best,
Prateek
```

---

### ⚠️ Send-time checklist

1. ⛔ **Never suggest they need orchestration.** They built one, it is live, and the evidence is in their own bundles.
2. ⛔ **Never use the loss, the yield decline or the RASK decline.** Not an observation — a jab.
3. ⛔ **Never name an acquirer.** We do not know theirs. CardinalCommerce is 3DS and Accertify is fraud; neither is an acquirer.
4. ⛔ **Never claim Apple Pay or Google Pay is missing.** Ambiguous.
5. ⚠️ **Re-check the fee table is unchanged** before Touch 1 — the 21-month freeze is the whole opener.
6. ⚠️ **Confirm the Cathay sequence has finished** before Day 1. See the calendar note.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 18 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED as a bound.** **7,912,000 passengers FY2025** and **HK$6,394m passenger revenue** from Cathay's 2025 Annual Results; the narrative gives *"an average of 21,700 per day."* Even at an implausibly high **HK$3,000 per booking**, HK$6.4bn yields ~2.1m bookings/year = **~178k/month**. LCC ancillaries (bags, seats, changes) bill separately and push it higher. **Every plausible divisor clears 100k.** |
| Orchestration status | **+1** | ✅ **In-house — the best-evidenced such call in this repo, and it is affirmative, not absence-of-hits.** A live self-hosted payment abstraction with two API versions running in parallel, its own 3DS choreography, its own DCC and miles-OTP paths, and B3 distributed-tracing headers on its own microservice mesh. **+1 per the matrix, and correctly so — this is the hardest sell shape.** |
| 3+ countries | **+3** | ✅ **37 destinations** across Japan, Korea, Taiwan, Mainland China, Southeast Asia and Saipan; **9 settlement currencies**; **7 distinct surcharge-bearing points of origin**. |
| Multiple PSPs | **0** | ⬜ **Zero acquirers or gateways nameable.** CardinalCommerce is 3DS, Accertify is fraud, Navitaire is the PSS — **none of them is an acquirer.** With ~25 tenders across 7 regulatory markets several PSP relationships are near-certain, but **not one can be named.** |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Hong Kong is the origin or destination of every flight, and FPS, PayMe and online Octopus are all absent** — sourced against their own complete tender dictionary and both published payment pages. **The home carrier is missing its home rails**, while carrying 14 Asian wallets the mainline does not. |
| Recent expansion | **+2** | ✅ **Passengers +29.7% YoY**, ASK +31.9%, and the parent's own results cite *"launching multiple new routes that will take time to mature"* as a driver of the loss. First-party, from the filing. |
| Payment issues reported | **+2** | ✅ **The strongest quantitative signal is a platform split: Android 2.1★ from 3,049 ratings versus iOS 4.5★ from 91,185** on the same booking funnel. A 2.4-star gap points at a broken Android checkout path. Supported by dated App Store reviews: a **3-card decline cascade with currency mismatch** (2025-09-17), a **3DS verification freeze** (2026-03-13), *"Can't proceed to payment… empty page while inputting credit card information"* (2026-07-05). ⚠️ **Agent-sourced, not verified by me** — see Source Notes. |
| Funding >$10M | **0** | ❌ Wholly owned subsidiary. No round. |
| High traffic outside home | **0** | ⬜ **No traffic data.** ⚠️ Worth noting though: the convenience fee applies to bookings **not** originating in HK or Malaysia across **seven markets**, which is first-party evidence that foreign-origin sales are material. **No share figure exists, so no points.** |
| Competitor using orchestration | **+2** | ✅ **Cebu Pacific runs CellPoint Digital orchestration**, established first-hand in our own Cebu Pacific file. It is a direct regional LCC competitor and the networks overlap on **Manila and Clark**, both on HK Express's route map. |
| Payment job postings | **0** | ⬜ None found. |

**Tier: 18 / 29 → ⭐ High Priority.** No analyst override applied.

### Source Notes
- ✅ **Verified by me today**, fetching `mybooking.hkexpress.com/_next/static/chunks/3211-8602de6337206745.js` fresh: **zero Adyen references**, `endpointPaymentHost+"/external/v1/payment/create-payment"`, `cardinalPostMessageUrl:"https://client.cardinaltrusted.com"`, `accertifyDataCollectorUrl:"https://acfrvpprdslbprod.hkexpress.com/..."`, `nsk_token`, `get-dcc-quote`, `miles-otp`.
- ✅ **The E-Payment Fee table was verified verbatim by me** on `hkexpress.com/en-HK/Fees/Other-Fees`, including the Hong Kong and Malaysia exemption.
- 🚩 **A FALSE POSITIVE WORTH RECORDING, and the agent caught it itself.** Its first pass returned **28 hits for `adyen-checkout`, `checkoutshopper-live.adyen.com` and `AdyenCheckout`** — all from **stale scratchpad files left by a prior task** (mtime Sep 17; filenames like `pages_cheero-redirect`, `pages_creator-join` belong to another company's site entirely). **That false positive would have inverted the whole answer.** Re-running against only today's freshly-fetched assets gives zero. **Add to the running false-positive list: stale scratchpad artifacts are as dangerous as substring collisions — always re-fetch before asserting a vendor.**
- ⚠️ **I could NOT confirm the `PGW_NSK_*` error taxonomy** in the chunk it was attributed to — my grep returned zero. The in-house classification stands on the endpoints and tracing headers regardless, but **do not cite those error codes.**
- ⚠️ **FY2025 financials** come from the agent's text extraction of Cathay's 2025 Annual Results PDF. Directionally certain and internally consistent, but **not re-extracted by me.**
- ⚠️ **App-store ratings and review text are agent-sourced.** The aggregates are structured machine-readable fields (`aggregateRating`), which is far stronger than search-summary paraphrase — but **re-check before quoting a specific review.**
- ❌ **LIHKG thread 1873952, Dcard 257536564 / 254515036, and discuss.com.hk 26309639 all returned 403 or a JS shell.** Thread **titles** are verified from search results; **contents are unread.** Do not quote them.
- ❌ **Trustpilot (1.6★ / 64) is about baggage fee disputes, not payment processing.** **Do not cite it as payment-failure evidence** — that conflation would be caught immediately.
- 📌 **An Expedia UI component named `shared-ui-retail-affiliates-stripe.js` on the Holidays site is CSS table-striping, NOT Stripe the PSP** (`--table__cell__stripe__background_color`). Another entry for the substring false-positive list.

### Manual Research Recommendations
> **1. Get behind `manage.hkexpress.com/w/payment` and name the acquirer.** It is the one material unknown, and Akamai Bot Manager + hCaptcha + Queue-it block automated access.
> **2. Settle Apple Pay / Google Pay** by loading a real checkout.
> **3. Confirm per-market tender ordering** — everything here is from static bundles and the i18n dictionary, not a live booking.
> **4. Read two of the blocked HK/TW forum threads** from a browser before anyone cites a payment incident.

---

## Executive Summary

HK Express is Cathay Pacific's wholly owned LCC — **7.9 million passengers in FY2025, up 29.7%, on a HK$996m loss that is five times worse than the prior year**, with yield down 15.3%. It runs a payment stack that shares **nothing** with its parent: where the mainline has Adyen direct acquiring across six markets and a published +10% authorisation result in India, the LCC has built **its own payment service** at `manage.hkexpress.com/w/payment`, with two API versions live in parallel, its own 3DS choreography through **CardinalCommerce**, **Accertify** for fraud CNAME'd onto its own domain, and **Navitaire New Skies** underneath — all verified first-hand today, along with the complete absence of Adyen anywhere in its assets. It carries roughly **25 tenders in 9 currencies across 37 destinations**, including fourteen Asian wallets the mainline does not offer, and yet **its own home market is the gap**: no FPS, no PayMe, and Octopus accepted inflight but not online. It recovers acceptance cost through a **flat convenience fee set by point of origin** — JPY 810, KRW 7,700, THB 230 and so on — that has not been repriced in at least 21 months despite material FX movement, which is the signature of a merchant that cannot see acceptance economics per rail. At **18/29** this is a strong account, and the motion is firmly in-house: they built it, it works, and the conversation is about reach and opportunity cost, never about whether they need a layer.

</details>
