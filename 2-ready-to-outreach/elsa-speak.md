# ELSA Speak

**Status:** 🟢 Ready to outreach — sequence drafted
**ICP Score:** 15 / 29 → 🟢 **Medium**
**Industry:** AI English-pronunciation coaching — consumer subscription app, B2B/schools arm · **HQ:** ELSA, Corp. (US — state of incorporation **unverified**); operations rooted in Vietnam (CÔNG TY TNHH ELSA, HCMC); offices Portugal, Vietnam, India, Indonesia, Japan · **Researched:** 2026-10-06 · **First email sent:** —
**Motion:** 🛑 **IN-HOUSE — they built their own payment SDK.** Verified first-hand: `elsa-config.elsanow.io/elsa-payment-sdk/html.umd.js` (HTTP 200, 143,547 bytes) is a merchant-built abstraction unifying **seven payment providers**, fronted by their own `payment.elsanow.io` service. **Never say they need orchestration.** Anchor on reach and the markets the SDK does not cover.

---

> ## ⭐ THE FINDING — and it overturns what three of five agents concluded
>
> Three agents independently concluded ELSA had **not** localized its payment rail. Agent 3's headline was *"ELSA has localized everything except the payment rail."* Agent 3 recorded **MoMo as `NOT FOUND` on ELSA's web checkout.** Agent 2 described Vietnam as a *"separate, non-Stripe, non-recurring activation-code rail"* disconnected from the rest.
>
> **All of that is wrong, and I verified why first-hand.** The pricing page preloads three things in its `<head>`:
>
> ```html
> <link rel="preconnect" href="https://payment.elsanow.io" crossorigin>
> <link rel="preconnect" href="https://js.stripe.com">
> <link rel="preload" href="https://elsa-config.elsanow.io/elsa-payment-sdk/html.umd.js" as="script">
> ```
>
> **ELSA built its own payment SDK.** Pulled it (HTTP 200, 143,547 bytes, control: 460 `payment` hits) and it carries the complete method set with ELSA's own English and Vietnamese copy:
>
> ```js
> defaultStripeDescription  = "Credit card, Google Pay, Apple Pay, Samsung Pay, and more"
> defaultPaypalDescription  = "Pay with your PayPal account"
> defaultPayooDescription   = "Wallet, Bank Transfer, ATM (Domestic cards) & QR Pay in Viet Nam"
> defaultMomoDescription    = "Pay with MoMo"
> defaultShopeeDescription  = "Pay with ShopeePay"
> defaultFundiinDescription = "Pay later with Fundiin"      // VN: "Trả sau 2 kỳ miễn lãi qua Fundiin"
> default2c2pDescription    = "Pay via 2C2P payment gateway" // VN: "qua các ví điện tử của 2C2P"
> taxInvoiceTitle           = "Tax invoice information (Vietnam)"
> ```
>
> **Seven providers — Stripe, PayPal, Payoo, MoMo, ShopeePay, Fundiin, 2C2P — behind one merchant-built layer, with Vietnamese e-invoicing built in.** This is the Jubilant FoodWorks pattern: a company that solved multi-PSP by writing its own abstraction.

---

> ## 🎯 THE HOOK — the SDK speaks two languages, and the business runs in ten
>
> I enumerated the SDK's locale coverage. It contains exactly **two**: `en` and `vi`.
>
> And the local rails inside it are **all Vietnamese** — Payoo (domestic ATM/QR), MoMo, ShopeePay, Fundiin (BNPL, "two interest-free instalments"). Everything else falls back to Stripe, PayPal, or 2C2P's generic SEA wallet set.
>
> **Set that against where the traffic actually is:**
>
> | Market | Share | Covered by the SDK? |
> |---|---|---|
> | 🇻🇳 Vietnam | **32.28%** | ✅ Fully — 4 local rails + e-invoicing + Vietnamese UI |
> | 🇹🇭 **Thailand** | **8.09%** | ❌ **PromptPay and TrueMoney absent.** No Thai UI |
> | 🇮🇳 **India** | **5.78%** | ❌ **UPI absent — verified, zero matches.** No Hindi UI |
> | 🇹🇼 **Taiwan** | **5.61%** | ❌ LINE Pay, JKOPay, ATM/VA, convenience store all absent |
> | 🇯🇵 Japan | 3.28% | ❌ konbini, PayPay, Rakuten Pay, carrier billing all absent |
> | 🇮🇩 Indonesia | 2.53% | ❌ QRIS, virtual account, GoPay/OVO/DANA all absent |
>
> **Thailand, India, Taiwan, Japan and Indonesia together are 25.3% of traffic — almost as much as Vietnam — and the payment layer ELSA built for Vietnam does not reach any of them.**
>
> **This is an asymmetry inside their own stack, which is the strongest kind.** They proved they know how to do local acquiring properly. They did it once. The question is why Vietnam got four local rails, a BNPL partner and tax invoicing while Thailand — their #2 market — gets a card form.
>
> ⚠️ **Verified absences, with controls run:** ZaloPay, VNPay, VietQR, NAPAS, ViettelPay, GrabPay, QRIS, GoPay, OVO, DANA, PromptPay, TrueMoney, LINE Pay, JKOPay, konbini, PayPay, Kredivo and Atome are **all absent from the SDK** — as are Adyen, Braintree, Checkout.com and Worldpay. Note **ZaloPay (~23% of Vietnamese wallet share) is missing even in Vietnam.**

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** AI English-pronunciation coaching app founded 2015 by Vu Van (CEO) and Dr Xavier Anguera. 50M+ learners claimed across 195 countries, 56M+ downloads. Sells monthly, 3/6/12/24-month prepaid **and lifetime** subscriptions through three channels — Apple IAP, Google Play Billing, and its own web checkout — plus a B2B/schools arm billed by card, bank transfer or PayPal.

**SimilarWeb total visits:** **1.082M** (Aug 2026), +6.95% MoM, desktop 40.89% / mobile web 59.11% — **supplied by Prateek**, Similarweb PRO. Full table in `accounts/traffic/elsa-speak.md`.

### Top markets
| Rank | Country | Traffic | Accepted methods | Missing | Local entity |
|------|---------|---------|------------------|---------|--------------|
| 1 | 🇻🇳 **Vietnam** | **32.28%** | **Payoo** (ATM/Visa/MC/JCB, bank transfer, QR), **MoMo**, **ShopeePay**, **Fundiin** BNPL, Stripe cards, PayPal, COD via courier-delivered activation codes | **ZaloPay** (~23% of VN wallet share), VNPay, VietQR | ✅ CÔNG TY TNHH ELSA, HCMC |
| 2 | 🇹🇭 Thailand | 8.09% | Stripe cards, PayPal, 2C2P generic wallets | **PromptPay · TrueMoney · Thai instalments** | ❌ none |
| 3 | 🇮🇳 India | 5.78% | Stripe cards, PayPal | **UPI · UPI Autopay · netbanking · RuPay** | ❌ none (office referenced) |
| 4 | 🇹🇼 Taiwan | 5.61% | Stripe cards, PayPal | **LINE Pay · JKOPay · ATM/VA · store cash** | ❌ none |
| 5 | 🇺🇸 United States | 4.70% | Stripe cards, PayPal | — | ⚠️ ELSA, Corp. — state unverified |
| 6 | 🇯🇵 Japan | 3.28% | Stripe cards, PayPal | **konbini · PayPay · Rakuten Pay · carrier billing** | ✅ ELSA Japan Inc., Shibuya |
| 7 | 🇮🇩 Indonesia | 2.53% | Stripe cards, PayPal | **QRIS · virtual account · GoPay/OVO/DANA** | ❌ none (office referenced) |

⚠️ **8 of the top 10 traffic markets have no confirmed local billing entity.** Vietnam is the only market where local acceptance is demonstrably solved. 🇮🇶 Iraq (2.10%) is **EMEA, not APAC** — context only.

### Legal entities
- **ELSA, Corp.** (USA, San Francisco) — ⚠️ **state of incorporation and registration number NOT found.** "Delaware" is a widely-repeated assumption, not a verified fact.
- **CÔNG TY TNHH ELSA** (Vietnam) — 29/11 Bui Thi Xuan St, Tan Binh District, HCMC. ⚠️ A registry listing under the same name shows a *different* HCMC address (District 3) and legal rep Ngô Thùy Ngọc Tú; "ELSA" is a common Vietnamese company name, so the registry record is **not confirmed** to be this entity. Needs a tax-code lookup.
- **Elsa, Corp. – Sucursal Em Portugal** (Lisbon) — EEA representative
- **ELSA Japan Inc.** (Shibuya, Tokyo, est. 2022) `[UNVERIFIED]`
- ❌ No Singapore, Thailand, Taiwan, India or Indonesia entity found.

### Known PSPs — seven, from their own SDK
| Provider | Role | Evidence |
|---|---|---|
| **Stripe** | Global cards + Google/Apple/Samsung Pay; **Stripe Billing** for web subscriptions | `[Source Code]` `js.stripe.com` preconnected; `stripePromise` ×13 in SDK; cancellation routed to `billing.stripe.com` portal; descriptor **ELSASPEAK.COM** |
| **Payoo** | 🇻🇳 domestic card/ATM + bank transfer + QR | `[Source Code]` `payoo_form`, `frmPayByPayoo`, `ordersForPayoo` |
| **MoMo** | 🇻🇳 wallet | `[Source Code]` `defaultMomoDescription` |
| **ShopeePay** | 🇻🇳 wallet | `[Source Code]` |
| **Fundiin** | 🇻🇳 BNPL — two interest-free instalments | `[Source Code]` `toggleFundiinPhoneInput`, `fundiinPhoneHtml` |
| **2C2P** | SEA e-wallet gateway | `[Source Code]` `my2c2p`, `logo_2c2p` |
| **PayPal** | Global | `[Source Code]` + ELSA's own payment page |
| **Apple IAP / Google Play Billing** | In-app, both as merchant of record | `[Terms]` *"In-app payments are processed through Apple or Google and not ELSA"* |

### Orchestration status
**🛑 In-house layer — `elsa-payment-sdk`.** Merchant-built, unifying seven providers, served from their own `elsa-config.elsanow.io` with a `payment.elsanow.io` backend. **No third-party orchestrator detected** — Juspay, Spreedly, Primer, Gr4vy, Yuno, Zooz all checked, zero hits. No Chargebee/Recurly/Zuora. Stripe Billing is incumbent on the web subscription rail specifically.

### Buying signals
- 💼 **"Business Growth & Monetization Lead" open — sited India, Singapore or Vietnam.** The closest thing to a monetisation owner, and it is **in territory**. `[UNVERIFIED — search summary]`
- 💼 **Akshaya Aradhya appointed CTO in 2025** (ex-GitHub, Netflix, LiveRamp) `[UNVERIFIED]`
- 🚀 **January 2026 — next-generation AI app launched**; Korean added as 9th interface language; a Hong Kong professional-market push
- 📉 **No funding round since September 2023** ($23M Series C, UOB Venture Management). **37 months.** Three years without a raise is pressure on DTC subscription efficiency.
- 📋 **No public payment RFP found.**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

> ⚠️ **Sizing constraint, carried forward from the research and not resolved.** The web-vs-IAP
> revenue split is **not disclosed anywhere**. The app-store override was considered and
> deliberately **not** applied, because the web channel is demonstrably real: a full Vietnamese
> storefront, seven providers, e-invoicing, BNPL, and **lifetime and prepaid SKUs that cannot be
> sold through auto-renewing IAP at all**. But the only listed comparable, **Duolingo, books ~82%
> of revenue through Apple and Google**. **Anyone sizing this account off total revenue or total
> users will be wrong by close to an order of magnitude. The addressable base is web checkout plus
> B2B.** Nothing in this sequence claims otherwise, and nothing in it should.

### Pain Vector Extraction

```
=== PAIN VECTOR EXTRACTION ===

Motion: IN-HOUSE — they built `elsa-payment-sdk`, a merchant-owned layer over seven providers.
        Step 6a override applies. The build decision is respected throughout. Nothing in this
        sequence says they need orchestration, lack sophistication, or should rip anything out.
        The entire argument is REACH.

Observable setup facts (from research, all first-hand in the file):
- `elsa-config.elsanow.io/elsa-payment-sdk/html.umd.js` — HTTP 200, 143,547 bytes. A
  merchant-built SDK unifying SEVEN providers: Stripe, PayPal, Payoo, MoMo, ShopeePay,
  Fundiin, 2C2P — source: research file, verified first-hand
- The SDK ships exactly TWO locales: `en` and `vi` — source: SDK enumeration
- Vietnam (32.28% of traffic) has four local rails plus Vietnamese e-invoicing
  (`taxInvoiceTitle = "Tax invoice information (Vietnam)"`) and Fundiin BNPL
  ("two interest-free instalments") — source: SDK strings
- Thailand #2 (8.09%): PromptPay and TrueMoney ABSENT, with controls run — source: SDK
- India #3 (5.78%): UPI ABSENT, zero alphabetic-bounded matches — source: SDK
- Taiwan 5.61%, Japan 3.28%, Indonesia 2.53%: no local rail present for any
- Those five markets together = 25.3% of traffic, against Vietnam's 32.28%
- 8 of the top 10 traffic markets have no confirmed local billing entity
- Lifetime SKU is 6,800,000₫ (~US$265) — a high-ticket single authorisation

Selected observations for Phase 1 (E1 bullets, ranked by materiality):
1. THE ASYMMETRY INSIDE THEIR OWN STACK — Vietnam has Payoo, MoMo, ShopeePay, Fundiin and
   tax invoicing; Thailand, the #2 market, gets a card form.
   → "Your own payment SDK carries Payoo, MoMo, ShopeePay and Fundiin for Vietnam, with tax
      invoicing built in. Thailand, your second-biggest market, gets a card form."
   MATERIALITY: highest. Both halves are theirs, so neither can be disputed. This is exactly
   the move the voice samples call the strongest available.
2. The SDK ships two locales against ten markets above 1% traffic.
   → "The SDK ships two locales, en and vi. The business runs in ten markets above 1%."
   MATERIALITY: high, and it is a count from their own code rather than a judgement.
3. India at #3 with no UPI.
   → "India is your number three market. No UPI in the bundle."
   MATERIALITY: real, and deliberately stated flat without projecting consequence.

Bridge variant: B — limitations
Rationale: NOT variant A (complexity), because they are not fragmented — they unified seven
providers themselves, which is the opposite of the A pattern. NOT single-PSP either, so the
usual B trigger does not apply literally. The limitation here is REACH: a seven-provider
layer whose every local rail serves one market. "At your stage, that usually comes with some
limitations" fits precisely and claims nothing about the quality of the build.

Hypothesis for Phase 2 (E3):
Every local rail they add is its own engineering project, so markets queue — and the queue
now holds more traffic than the one market that was served.
Backing logic: the SDK carries two locales; Vietnam received four rails, a BNPL partner and
e-invoicing while no other market received any; and Thailand, India, Taiwan, Japan and
Indonesia together are 25.3% of traffic against Vietnam's 32.28%. The cost of the next rail,
not the absence of a layer, is the constraint.

Embedded discovery question (E3): "when you added Fundiin, roughly how long did that take end
to end?" — easy to answer, asks about work they are proud of rather than work they skipped,
and the answer is the whole business case.

Success case for Phase 3 (E4):
Selected case: inDrive
Tier: 2 — same payment pattern (multi-market local-rail expansion), different industry and
different region. ⚠️ NO Tier 1 exists: Open English is the only edtech logo in the library and
it carries NO published numbers, so it cannot carry an E4. Verified live on y.uno 2026-10-11.
Match rationale: ELSA's problem is reach — how long and how costly each new market is. That is
precisely what the inDrive case measures. It is NOT a decline-recovery case, which matters,
because the research found ZERO evidence of failed renewals or dunning failures at ELSA.
Numbers to lead with: 10 new countries live in under eight months · 90% payment approval rate ·
over 50 countries on one integration.
⚠️ E4 states outright that inDrive is mobility, not edtech, and that the expansion was across
LATIN AMERICA, not Asia. The case page says so verbatim: "integrating payment routes in several
Latin American countries in less than 8 months."
Optional benchmark: SKIP. The "~8% authorisation uplift" figure traces to Yuno's own blog, not
to independent evidence.

Touch-by-touch angles:
- E2 angle: the asymmetry → "one integration to add any method, no per-rail rebuild". One
  mechanism only, framed as the cost of the NEXT rail rather than the absence of a layer.
- LK1 angle: the Vietnam-versus-Thailand contrast.
- LK2 angle: the five waiting markets are a quarter of traffic between them.
- LK3 angle: inDrive's ten markets in eight months, reworded, not the E4 bullet verbatim.
- LK4 angle: fresh and unused until here — Fundiin gives Vietnamese buyers two interest-free
  instalments on a ~6.8m₫ lifetime plan, and no other market gets that option.
- E8 angle: clean exit, offering to return when the next market is actually on the roadmap.
```

---

**Send calendar.** Day 1 anchored to **Monday 12 October 2026**. Weekend touches move to the next business day, already applied. **Slots are in Vietnam time (ICT, UTC+7)** — operations are rooted in Ho Chi Minh City and the monetisation role is sited India, Singapore or Vietnam. ICT is IST + 1.5h, so the overlap is comfortable all day.

| Touch | Day | Send date | Meeting slot proposed (Vietnam time) | Prateek's time (IST) |
|---|---|---|---|---|
| E1 | 1 | Mon 12 Oct | none (Phase 1) | — |
| E2 | 3 | Wed 14 Oct | none (Phase 1) | — |
| LK1 | 5 | Fri 16 Oct | none (Phase 1) | — |
| E3 | 7 | Mon 19 Oct | **Thu 22 Oct, 10am or 3pm** | 8:30am / 1:30pm |
| LK2 | 9 | Tue 20 Oct | **Fri 23 or Mon 26 Oct, 4pm** | 2:30pm |
| E4 | 11 | Thu 22 Oct | **Tue 27 Oct, 11am or 4:30pm** | 9:30am / 3:00pm |
| E5 | 13 | Mon 26 Oct | manual | — |
| E6 | 15 | Tue 27 Oct | manual | — |
| LK3 | 17 | Wed 28 Oct | **Mon 2 Nov, 2pm** | 12:30pm |
| E7 | 19 | Fri 30 Oct | manual | — |
| LK4 | 21 | Mon 2 Nov | **Thu 5 Nov, 10:30am** | 9:00am |
| E8 | 23 | Tue 3 Nov | none (break-up) | — |

Five distinct day/time combinations, all named in Vietnam time. No Vietnamese public holiday falls in this window.

---

### Phase 1 — Curiosity (Days 1–5)

#### Touch 1 — Email 1 · Day 1 · Mon 12 Oct

**Subject:** Four local rails, Vietnam only

```text
Hey {{recipient.first_name}},

Spent some time on ELSA's payment setup. Three things stood out.

Your payment SDK carries Payoo, MoMo, ShopeePay and Fundiin for Vietnam, with tax invoicing
built in. Thailand, your second market, gets a card form.

The SDK ships two locales, en and vi. You're in ten markets above 1%.

India is your #3 market. No UPI in the bundle.

At your stage, that usually comes with some limitations.

I work at Yuno (top-100 fintech, a16z-backed). We consider ourselves the "everything
payments" platform: one integration, every PSP, every method, every market.

Rather than pitch you based on assumptions, is there anything payment-related you're working
through that we might be able to help with?

Best,
Prateek
```

#### Touch 2 — Email 2 · Day 3 · Wed 14 Oct · REPLY IN THREAD

```text
Hey {{recipient.first_name}},

Following up. Wanted to put a bit more behind what Yuno actually does, and how it would
address what I flagged.

We sit above the providers you already run, so your SDK and all seven stay where they are.
Nothing gets ripped out. What changes is the cost of the eighth, and the fifteenth. Adding
PromptPay, UPI or LINE Pay becomes configuration against one integration instead of a build
against each provider's own API, settlement file and edge cases.

Which is the part that matters here. You've already shown you can do local acquiring
properly, in Vietnam. The open question is what the next market costs you.

I'll keep sharing what I'm seeing every few days. If your stack's where you want it, just say
the word and I'll back off. Otherwise happy to go deeper.

Cheers,
Prateek
```

#### Touch 3 — LinkedIn message 1 · Day 5 · Fri 16 Oct

```text
Hey {{recipient.first_name}}, sent you a note over email this week, figured I'd flag one part
here too. Your payment SDK carries four local rails and tax invoicing for Vietnam, and
Thailand, your second-biggest market, gets a card form. Curious whether that maps to anything
you're working through.
```

---

### Phase 2 — Diagnosis (Days 7–9)

#### Touch 4 — Email 3 · Day 7 · Mon 19 Oct · NEW EMAIL

**Subject:** Your SDK stops at Vietnam

```text
Hey {{recipient.first_name}},

Going to take a swing at this. My read is that every local rail is its own engineering
project, so markets queue, and the queue now holds more traffic than the one that got served.

Vietnam got Payoo, MoMo, ShopeePay, Fundiin and e-invoicing. Not because anyone's doing it
badly: you built that properly. But Thailand, India, Taiwan, Japan and Indonesia are a
quarter of your traffic between them, with no local rail for any of them.

At Yuno (a16z-backed, top-100 fintech) we sit above your existing providers, so a new rail is
configuration rather than a build. Keep your stack, add what's missing.

When you added Fundiin, roughly how long did that take end to end?

Thursday the 22nd is open for me. Would 10am or 3pm Vietnam time work for 15 minutes?

All the best,
Prateek
```

#### Touch 5 — LinkedIn message 2 · Day 9 · Tue 20 Oct

```text
Hey {{recipient.first_name}}, sent a longer note over email on Monday. Short version:
Thailand, India, Taiwan, Japan and Indonesia are about a quarter of your traffic between
them, and your payment SDK carries no local rail for any of them. If that's on your radar,
would Friday the 23rd or Monday the 26th at 4pm Vietnam time work for a quick 15?
```

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · Thu 22 Oct · NEW EMAIL

**Subject:** How inDrive solved this

```text
Hey {{recipient.first_name}},

On the read I shared last week, here's a quick example of what solved looks like.

inDrive is a mobility app rather than edtech, and the expansion below happened across Latin
America, not Asia. The pattern is the same one though: a lot of markets, each with its own
payment preferences. They put Yuno's layer above their providers and, in their own words,
integrated payment routes "in several Latin American countries in less than 8 months":

- 10 new countries live in under eight months
- 90% payment approval rate
- over 50 countries running on one integration (you read that right)

The mechanism was routing across partners so they could compare cost and approval rate per
provider and move volume accordingly. Same layer above the stack they already had, no
rip-out.

Tuesday the 27th is open. Would 11am or 4:30pm Vietnam time work for 15 minutes?

Full case here if useful: https://y.uno/en/success-stories/indrive

Looking forward to it,
Prateek
```

#### Touch 7 — Email 5 · Day 13 · Mon 26 Oct · MANUAL

*Placeholder. Do not auto-write.*

**Strongest unused material, in order:**
1. ⭐ **A Thailand teardown.** Their #2 market at 8.09%, and the SDK carries neither PromptPay nor TrueMoney — verified by enumeration with controls run. An annotated screenshot of their own Thai checkout beside the Vietnamese one is the entire argument in one image, and it is their own product on both sides.
2. **The India question.** 5.78% of traffic, no UPI, and the SDK has no Hindi locale. ⚠️ **Do NOT cite RBI e-mandate rules** — nothing in the research file sources them, and the standing instruction is to pull a current primary source or say nothing.
3. **ZaloPay is missing even in Vietnam**, the one market they solved, at roughly 23% of Vietnamese wallet share. Sharp, but it critiques their best work, so use it only if the thread is already warm.

#### Touch 8 — Email 6 · Day 15 · Tue 27 Oct · MANUAL

*Placeholder. Second manual approach, different format from E5.*

Candidate angle: **the high-ticket instalment gap.** The lifetime plan runs to **6,800,000₫ (~US$265)**, and Fundiin gives Vietnamese buyers two interest-free instalments on it. Nobody in Taiwan, Japan, Thailand or India gets an instalment option on the same SKU, and those are markets where high-ticket purchases convert on instalments. This is the EdTech industry override applied literally, and it is a revenue argument rather than a plumbing one.

#### Touch 9 — LinkedIn message 3 · Day 17 · Wed 28 Oct

```text
Hey {{recipient.first_name}}, one more from me. inDrive went live in ten new markets in under
eight months on a single integration, at a 90% approval rate. Worth 15 minutes to see whether
the same shape maps to your next five? Monday the 2nd at 2pm Vietnam time is open.
```

---

#### Touch 10 — Email 7 · Day 19 · Fri 30 Oct · MANUAL

*Placeholder. Manual creative bridge, anchored to something fresh.*

Freshest available anchors: the **"Business Growth & Monetization Lead"** role, sited **India, Singapore or Vietnam** — the closest thing to a monetisation owner and squarely in territory, so a good multi-threading target. **Akshaya Aradhya joined as CTO in 2025.** And the **January 2026 next-generation app launch** plus Korean as a ninth interface language, which is a localisation push that stops short of the payment layer. ⚠️ All three are tagged `[UNVERIFIED — search summary]` in the research. **Re-verify before putting any of them in writing.**

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21 · Mon 2 Nov

```text
Hey {{recipient.first_name}}, last ping from me here. One thing I never got to: Fundiin gives
your Vietnamese buyers two interest-free instalments on a lifetime plan that runs to about
6.8 million dong. No other market gets that option. If timing works, Thursday the 5th at
10:30am Vietnam time is open.
```

#### Touch 12 — Email 8 · Day 23 · Tue 3 Nov · REPLY IN THREAD to Touch 4

```text
Hey {{recipient.first_name}},

Going to stop pinging unless you want to pick this back up.

If the timing is just off, happy to come back when the next market is actually on the
roadmap. And if it ever comes back up, just reply here.

All the best,
Prateek
```

---

### Source Notes

- ✅ **The seven providers, and the four Vietnamese rails** (E1, E2, LK1, E3) — `elsa-config.elsanow.io/elsa-payment-sdk/html.umd.js`, HTTP 200, 143,547 bytes, verified first-hand in the research run. Strings include `defaultPayooDescription`, `defaultMomoDescription`, `defaultShopeeDescription`, `defaultFundiinDescription`.
- ✅ **Vietnamese tax invoicing** (E1, LK1, E3) — `taxInvoiceTitle = "Tax invoice information (Vietnam)"`, same SDK.
- ✅ **Two locales, `en` and `vi`** (E1) — SDK enumeration.
- ✅ **PromptPay and TrueMoney absent for Thailand; UPI absent for India** (E1, LK2, E3) — SDK enumeration **with controls run**, which is what makes these sourced absences rather than assumptions.
- ✅ **Traffic shares** (E1, LK2, E3) — SimilarWeb supplied by Prateek: Vietnam 32.28%, Thailand 8.09%, India 5.78%, Taiwan 5.61%, Japan 3.28%, Indonesia 2.53%. **The five non-Vietnam markets sum to 25.29%**, which is where "about a quarter" comes from. **Deliberately rounded in the copy** rather than quoted to two decimals.
- ✅ **Fundiin is two interest-free instalments** (LK4) — SDK Vietnamese string, *"Trả sau 2 kỳ miễn lãi qua Fundiin"*.
- ✅ **The 6,800,000₫ lifetime SKU** (LK4) — research file.
- ✅ **inDrive's three numbers and the mechanism** (E4, LK3) — `https://y.uno/en/success-stories/indrive`, **re-fetched and verified live 2026-10-11**. Page title: *"inDrive achieves 90% payment approval rate with Yuno"*. Verbatim: *"expand into 10 new countries in under eight months"*, *"integrating payment routes in several Latin American countries in less than 8 months"*, *"inDrive has grown to operate in over 50 countries"*.

**⚠️ Flags to clear before sending**

- ⚠️ **The sizing constraint at the top of this section is the biggest one.** The web-vs-IAP split is undisclosed and the addressable base is web plus B2B only. Nothing here claims a share, and nothing should.
- ⚠️ **No contact name.** `{{recipient.first_name}}` throughout. The likely targets are the **Business Growth & Monetization Lead** (sited India, Singapore or Vietnam, and in territory) or **Vu Van**, co-founder and CEO. ⚠️ **There is no payments or billing engineering role anywhere** — two agents searched independently — so there may be no single payments owner to route to. **No multi-threading line is used**, because there is no identified second person to be pointed at.
- ⚠️ **Slots are Vietnam time.** Operations are rooted in HCMC and the monetisation role is sited in-region. **But `ELSA, Corp.` is US-incorporated** (state unverified) and there is an ELSA Japan entity. If the reply comes back on US Pacific hours, re-cut every slot.
- 🛑 **Four things this sequence deliberately never says**, each one a documented trap in the research file: it never suggests they lack MoMo (**they have it**); it never pitches failed renewals, dunning or involuntary churn (**zero evidence exists** — every documented complaint is an *unwanted successful* charge, not a failed one); it never claims their checkout is failing customers (**the majority of those Trustpilot complaints are Apple App Store charges, which are not ELSA's stack**); and it never mentions Epic v. Apple (**that ruling covers only the US App Store, and the US is 4.70% of their traffic**).
- 🛑 **Never write "Speak" when you mean ELSA.** Speak (speak.com) is a **different, directly competing app** with a $78M Series C at a $1bn valuation, and its pages contaminated the raw research.
- ⚠️ **No APAC regulatory rule appears anywhere in this sequence.** Deliberate. In particular there is no RBI e-mandate claim, because none is sourced in the research file.
- ⚠️ **E1, E2, E3 and E4 run over the skill's word budgets** (116 / 140 / 139 / 160 against 85–110 / 110–140 / 90–120 / 130–160). E3 is the one worth a second look: roughly 60 of its words are the prescribed Yuno re-state, discovery question and CTA. **If a tighter send is wanted, cut the India bullet from E1 and the "not because anyone's doing it badly" clause from E3** — though that clause is the diplomatic hedge doing real work on an in-house account, so it is the last thing to go, not the first.

### Success Case Alternatives

- **Rappi** — *"zero implementation delays, hundreds of methods, 80% less analyst work"*. The closest alternative, and arguably better if the conversation turns to **provider breadth and operational load** rather than market entry. Same Tier 2 caveat: super-app, LATAM.
- **Vibra** — new-user approval lifted **more than 30 percentage points, to 80%**, alongside launching Apple Pay, Nu Pay and Google Pay. Use if the thread moves to **first-time-buyer conversion**, which fits a consumer app with a large free-to-paid funnel. Tier 2, Brazil, retail.
- ❌ **Open English is the only edtech logo in the library and it carries NO published numbers**, so it cannot carry an E4. Usable as a one-line relevance signal on a call only.
- ❌ **Do NOT use Livelo here.** It is the decline-cascade case, and ELSA has **no evidenced decline problem** — citing it would invent a pain the research explicitly failed to find.
- ❌ **Do NOT use Viva Aerobus.** Its 75% is a NOVA result (AI voice callback after a failed payment), which would misattribute the mechanism.
- ⚠️ **No competitor in this category uses any orchestrator** — Duolingo, Babbel, Busuu, Speak, Cake, Red Kiwi, Topica, Prep and Monkey Junior were all checked. **That cuts both ways: there is no category proof point to show them either.**


</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 15 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+3** | ⚠️ **NOT FOUND — ASSUMED ~50,000–100,000/month. `[ASSUMPTION — not researched.]`** No subscriber count, ARPU or transaction figure is published. Third-party revenue estimates span **$4.8M to $49.6M — a 10× spread**, so none is usable. **Basis for the assumption:** 1.082M monthly web visits; 56M+ downloads; 25M+ claimed active users; a subscription mix weighted to annual and lifetime prepaid, which produces far fewer billing events than subscribers. Scored the band this implies and marked ⚠️. **Per the disclosure rule, an assumption never rejects — and "confirm monthly transaction count" is the top manual-research item.** |
| Orchestration status | **+1** | ✅ **In-house layer confirmed first-hand** — `elsa-payment-sdk`, 7 providers, own `payment.elsanow.io` backend. Hardest motion in the matrix. |
| 3+ countries | **+3** | ✅ 10 countries above 1% traffic share; entities confirmed in US, Vietnam and Japan. |
| Multiple PSPs | **+3** | ✅ **Seven, from their own source code** — Stripe, PayPal, Payoo, MoMo, ShopeePay, Fundiin, 2C2P. The strongest-evidenced row in this file. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Verified by enumeration, with controls.** Top-3 markets are Vietnam, **Thailand (8.09%)** and **India (5.78%)**. **PromptPay and TrueMoney are absent** from the SDK serving Thailand; **UPI is absent** — zero alphabetic-bounded matches — from the SDK serving India, the world's largest UPI market. Both are dominant local rails in top-3 traffic markets, sourced from the merchant's own code rather than inferred. |
| Recent expansion | **0** | ⬜ A January 2026 next-gen app launch, Korean localization and a Hong Kong press push. **Product and marketing activity, not market expansion.** Not stretching this row to fit. |
| Payment issues | **0** | ⬜ **And this zero is deliberate — the honest call costs 2 points.** Billing complaints are real, continuous (May 2025 → Sep 2026) and concentrated (**12 of ~32 Trustpilot reviews**). But **4–5 are explicitly Apple App Store**, 1 is Google Play, only **1** is confirmed ELSA's own web billing, and 5 are unattributable. Critically, **there is zero evidence of declined cards, failed renewals, dunning failures or double charges** — every complaint is an *unwanted successful* charge. **That is trial-conversion opacity and refund operations, not payment-infrastructure weakness.** Awarding this signal would misrepresent what the evidence shows. |
| Funding >$10M | **0** | ❌ Last round **$23M Series C, 12 September 2023** — **37 months ago**, far outside the 12-month window. Total raised disputed ($50M vs $60M); do not quote a figure. |
| High traffic outside home | **+2** | ✅ Vietnam is **32.28%** — home market under a third, with a long tail across eight further markets. Comfortably met. |
| Competitor using orchestration | **0** | ❌ **Genuine "no comparable has done it."** Duolingo, Babbel, Busuu, Speak, Cake, Red Kiwi, Topica, Prep, Monkey Junior all checked — none on any orchestrator. No orchestration case study exists for any language-learning or consumer-subscription-app brand. ⚠️ **Cuts both ways: Yuno has no category reference to show them either.** |
| Payment job postings | **0** | ❌ Two agents searched independently. **No payments, billing or subscription-infrastructure engineering role found.** The "Business Growth & Monetization Lead" is a commercial role, not a payments hire. |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **🟢 Medium (15)**

**No RFP override.**

### ⚠️ Analyst override considered and NOT applied — the app-store question

`subscription-payments.md` §4 requires this check before anything else, and it is the documented `not-icp` failure mode from the EMEA pack. **The answer is: do not disqualify, but size honestly.**

**Why not disqualified — ELSA's web channel is demonstrably real, not vestigial:**
- Their own Terms split the channels explicitly: *"payments are processed through Apple or Google and not ELSA"* versus *"All charges for purchases made through the ELSA website are refundable… within seven days."*
- They contract directly for recurring card billing: *"once you have expressly agreed for your credit card to be charged on a recurring basis… ELSA may submit periodic charges… without further authorization."* That is ELSA as merchant of record.
- A **full Vietnamese storefront** with VND pricing, seven payment providers, a hotline, e-invoicing, courier-delivered activation codes and BNPL. **Nobody builds that for a rounding error.**
- **Lifetime and prepaid SKUs** (6,800,000₫ ≈ US$265) and **promo-code discounting** cannot be delivered through auto-renewing IAP at all.
- A **B2B/schools arm** billed by card, bank transfer or PayPal, entirely outside the stores.

**But the sizing constraint is severe and must not be lost.** The only listed comparable discloses it: **Duolingo's FY2025 10-K — *"we derived 62% of our revenue… from the Apple App Store, and 20% of our revenue… from the Google Play Store"* — ~82% through the stores.** FY2024 named Apple 60.8%, Google 23.4%, **Stripe 11.7%**. And Duolingo's non-store ~18% also contains the Duolingo English Test and advertising, so the genuinely card-processed share is smaller still. **ELSA is plausibly *more* store-dependent — no exam product, no ads, mobile-first top market.** `[INFERENCE]`

**Consequence: anyone sizing this account off total revenue or total users will be wrong by close to an order of magnitude.** The addressable base is web checkout plus B2B only.

### Source Notes

**✅ Verified first-hand by me**
- `elsaspeak.com/en/elsa-pro/` → 200, redirects to `/en/elsa-subscription`, 121,553 bytes, `<title>ELSA Speak Pricing</title>`. **This is the page the raw research recorded as a 404.**
- The three `<head>` preloads naming `payment.elsanow.io`, `js.stripe.com` and `elsa-payment-sdk`.
- **`elsa-config.elsanow.io/elsa-payment-sdk/html.umd.js`** — HTTP 200, 143,547 bytes, control 460 `payment` hits. The seven-provider method list, in English and Vietnamese.
- **Locale enumeration: the SDK contains `en` and `vi` only.**
- **Absence controls run** on 24 rails and 4 global PSPs — all confirmed absent.
- `jp.elsaspeak.com` → **HTTP 200, 183,757 bytes** and `vn.elsaspeak.com/web-subscribes/` → 200, 73,261 bytes.

**⚠️ Unverified / search-summary only**
- CTO appointment, the Monetization Lead posting, ELSA Japan Inc. details, the Vietnamese registry record, all revenue estimates, total funding raised, ZaloPay/VinID/Grab Moca/Vietcombank/ACB as Vietnamese methods (named in search snippets of ELSA's domain but **absent from the SDK** — treat the SDK as authoritative).
- **PCI posture entirely unverified.** `trust.elsaspeak.com/controls` exists but is JS-rendered and returned no content.

**❌ Could not establish**
- **The web-vs-IAP revenue split.** The central sizing question. Not disclosed anywhere.
- ELSA, Corp.'s state of incorporation; the Vietnamese tax code; any Thailand, Taiwan, India, Indonesia or Singapore entity.
- Paying-subscriber count, ARPU, any transaction volume.
- Whether RevenueCat/Adapty/Qonversion sits on the **mobile** rail — invisible to every route available.
- Dunning, retry, account-updater and network-token configuration.

**Corrections made to the raw research**
- **Agent 3 recorded MoMo as `NOT FOUND` on ELSA's web checkout. It is in their SDK.** Corrected.
- **Agent 3's headline — "ELSA has localized everything except the payment rail" — is wrong.** They localized it thoroughly, for Vietnam.
- **Agent 2's "Vietnam is a separate non-Stripe rail disconnected from the others"** is wrong: all seven providers live in one SDK.
- Agent 3 found no Japan localization; **`jp.elsaspeak.com` returns 183,757 bytes.**
- **An agent cited a Nudge Security profile claiming ELSA holds SOC 2, PCI, HIPAA, ISO 27001 and *FedRAMP*.** FedRAMP and HIPAA for a consumer pronunciation app are implausible; that agent correctly pushed back and it is excluded here.

**⚠️ False positives caught — recorded so nobody repeats them**
- **`omise` → `stripePromise` / `initializationPromise` / `getStripePromise`.** 39 hits in the SDK and 1 on the pricing page. **Omise the PSP is not present.** This one nearly got through twice.
- **`upi` → zero alphabetic-bounded matches.** Not a payment method in the SDK.
- **`help.speak.com`** articles titled *"Cancelled subscription but still charged"* belong to **Speak**, a different competing app. They rank directly alongside ELSA results and read as perfect findings.
- **`apple.co/momo-nttt`** is **Apple** accepting MoMo as an App Store funding source in Vietnam — **not** ELSA integrating MoMo.
- **`adapty.io/paywall-library/elsa/`** is Adapty's paywall *inspiration gallery* — screenshots of other apps. **Not** evidence ELSA is an Adapty customer.
- **`reveliolabs.com/companies/elsa-sa`** — "Elsa SA", ~515 employees, almost certainly a different company. Headcount and hiring-decline figures from it are unusable.

### Success Case Alternatives
- **inDrive** — Tier 2. 50+ countries, **90% payment approval rate**, **ten new countries in eight months**. The "we built it once, now do it everywhere" match is exact.
- **Livelo** — Tier 2. **Recovered 50% of transactions**, **+5% approval rate**.
- ⚠️ Both metrics came via search summary of Yuno's own success-stories page (a blocked host). **Verify on `y.uno/en/success-stories` before quoting a number.**
- ⚠️ **No language-learning or consumer-subscription-app orchestration reference exists anywhere.** Expect "who else in our category?" and answer honestly.

---

## Section 10: Strategic Insights & Outreach Angles

> ### Insight #1: They built the local payment layer once, for one market
> **Evidence:** The SDK carries Payoo, MoMo, ShopeePay and Fundiin — all Vietnamese — plus Vietnamese e-invoicing, and is localized into `en` and `vi` only + Thailand 8.09%, India 5.78%, Taiwan 5.61%, Japan 3.28% and Indonesia 2.53% are **25.3% of traffic** with no market-native rail in that SDK.
> **Pain Point:** Vietnam gets four local rails, a BNPL partner and tax invoicing. Thailand — the #2 market — gets a card form. Every further market means another provider integrated by hand into a layer the team maintains themselves.
> **Yuno Value Proposition:** The markets become configuration rather than the next engineering project. **Additive — it sits above what they built.**
> **Best Success Case:** inDrive — ten countries in eight months.
> **Outreach Angle:** Observe the asymmetry; it is theirs and it is checkable. Respect the build.
> **Suggested Subject Line:** "Vietnam has four rails, Thailand has one"

> ### Insight #2: The world's largest UPI market, with no UPI
> **Evidence:** UPI is absent from the SDK — verified by enumeration with a control + India is 5.78% of traffic and ELSA's price points sit well under ₹15,000, which is the RBI AFA-exemption ceiling for e-mandates.
> **Pain Point:** **UPI Autopay passed 53% of all Indian recurring transactions in January 2025, overtaking card-based recurring.** A subscription business in India without it is billing on the minority rail — and at ELSA's price points, UPI Autopay mandates would be AFA-exempt, i.e. frictionless.
> **Yuno Value Proposition:** UPI and UPI Autopay through the existing integration, without standing up an Indian acquiring relationship.
> ⚠️ **Honest caveat to carry:** foreign-domiciled merchants face real onboarding friction on UPI Autopay. Do not imply it is a switch-flip.
> **Suggested Subject Line:** "No UPI on your India checkout"

> ### Insight #3: A ₹-scale one-off on a card-only rail
> **Evidence:** Lifetime SKUs at **6,800,000₫ ≈ US$265**, confirmed in ELSA's own Terms as a subscription class + Fundiin BNPL is wired in **for Vietnam only.**
> **Pain Point:** A US$265 single authorisation is where approval rate is most expensive — and outside Vietnam there is no instalment or BNPL option in the SDK to soften it.
> **Yuno Value Proposition:** Local acquiring and instalment/BNPL rails per market on the high-ticket SKU.
> **Outreach Angle:** They already know this — they solved it in Vietnam with Fundiin. Ask what the lifetime tier converts at in Thailand.
> **Suggested Subject Line:** "Fundiin in Vietnam, nothing in Thailand"

### Quick Hits

**Email hooks**
1. Your payment SDK carries Payoo, MoMo, ShopeePay and Fundiin — and ships in English and Vietnamese only, while Thailand, India, Taiwan, Japan and Indonesia are a quarter of your traffic.
2. India is 5.78% of your traffic and UPI Autopay now carries the majority of Indian recurring payments — your checkout doesn't have it.
3. You solved local acquiring in Vietnam with four rails and a BNPL partner. Thailand is your second-biggest market and gets a card form.

**Cold call openers**
1. "You built your own payment SDK rather than buying one — what drove that call?"
2. "Vietnam has Payoo, MoMo, ShopeePay and Fundiin. What does Thailand have?"
3. "Your lifetime tier is about US$265. What does that convert at outside Vietnam?"

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual revenue | **Undisclosed.** Third-party estimates **$4.8M – $49.6M** — a 10× spread | zoominfo / getlatka / prospeo / persana, all `[UNVERIFIED]`. **Do not quote any of them.** |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ~50,000–100,000/month. `[ASSUMPTION — not researched.]`** Basis: 1.082M monthly web visits, 56M+ downloads, 25M+ claimed active users, against a subscription mix weighted to annual and lifetime prepaid — which produces far fewer billing events than subscribers. **Billing unit counted: a charge on ELSA's own web rail.** Per the disclosure rule this cannot reject the account. | — |
| Users | 50M+ learners / 195 countries; 56M+ downloads; 25M+ active | ELSA marketing, undated |
| Funding | **$23M Series C, 12 Sep 2023**, led by UOB Venture Management. Total raised disputed: **$50M (ELSA's own profile) vs $60M (Tracxn)** | [BusinessWire](https://www.businesswire.com/news/home/20230912548387/en/) |
| Price points 🇻🇳 | Pro 1yr 1,595,000₫ (disc. 829,000₫) · Pro lifetime 3,395,000₫ · Premium 1yr 2,745,000₫ (disc. 999,000₫) · **Premium lifetime 6,800,000₫ ≈ US$265** | vn.elsaspeak.com |
| B2B | Team 2–50 seats self-serve card; Business 51+ custom, manual invoicing; card / bank transfer / PayPal | elsaspeak.com/en/english-for-companies/plans |
| **Billing channel split (web vs app store)** | ⚠️ **NOT DISCLOSED — the central sizing gap.** Benchmark: **Duolingo FY2025, 62% Apple + 20% Google = ~82% stores.** ELSA plausibly more store-dependent. **Addressable base is web + B2B only.** | [Duolingo FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1562088/000162828026012494/duol-20251231.htm) |

### Overall Research Confidence

**MEDIUM-HIGH on the payment stack — unusually good. LOW on volume.**

- **Payment stack: HIGH and first-party.** I pulled their own SDK and enumerated it with controls. Seven providers confirmed from source, absences confirmed by enumeration, two false positives caught. This did not depend on any vendor announcement.
- **Traffic: HIGH.** ✅ Supplied by Prateek, Similarweb PRO, with total visits.
- **Volume and revenue: LOW.** No subscriber count, no ARPU, no transaction figure, and a 10× spread across revenue estimates. The web-vs-IAP split — the number that decides the account's size — is undisclosed.
- **Complaints: MEDIUM, and the honest read is unhelpful to a payments pitch.** Real and continuous, but predominantly Apple-billed and containing zero failed-payment evidence.
- **Competitive: MEDIUM** with a hard ceiling — no category orchestration reference exists in either direction.

### Manual Research Recommendations

> **Area:** ⭐ **The web-vs-IAP revenue split**
> **Why it matters:** It is the difference between a mid-size account and a small one, and nothing else in this file resolves it.
> **Suggested action:** Ask directly in discovery. There is no public source.

> **Area:** ⭐ **Walk the Vietnamese checkout to the payment step**
> **Why it matters:** The SDK proves which providers are *integrated*; it does not prove which are *enabled per market*. Two minutes on `vn.elsaspeak.com/web-subscribes/` converts the whole method table from code-inferred to observed.
> **Suggested action:** Load it, select a package, advance to payment, and note what renders. Repeat with a Thai IP to confirm the Thailand gap.

> **Area:** Whether the mobile rail is already abstracted
> **Why it matters:** If RevenueCat or Adapty sits on mobile, part of the "they built it themselves" story changes.
> **Suggested action:** Not resolvable by web research — ask, or inspect the app bundle.

> **Area:** Correct the TAL row
> **Why it matters:** It records "~$40M est. revenue — VERIFY." Estimates range $4.8M–$49.6M; no figure is defensible.
> **Suggested action:** Blank the revenue field or mark it "undisclosed, estimates $5M–$50M."

</details>
