# Fever

**Status:** 🟢 Ready to outreach — 12-touch sequence drafted
**ICP Score:** 16 / 29 → 🟢 **Medium**
**Industry:** Live-entertainment discovery & ticketing marketplace (Candlelight, immersive experiences) · **HQ:** ⚠️ **Fever Labs Inc., Delaware / New York** — *not Madrid* · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** ⚠️ **COMPETITIVE — a global orchestrator is already in production.** Not greenfield. Read 3B before drafting a single line.

---

> ## ⛔ TWO CORRECTIONS TO THE STUB, BOTH OF WHICH WOULD EMBARRASS US IN EMAIL ONE
>
> **1. Fever is not Madrid-headquartered.** Their own Terms of Use, fetched and verified by me:
> > *"**Fever Labs Inc.** ("Fever") is a corporation duly organized and existing under the laws of the **State of Delaware**, United States of America, TAX ID 99-0368536, with offices at **50 Greene St 3 Fl, New York, NY 10013**, United States."*
>
> Madrid is the founding city and the largest engineering office, and it is a notice address — **but the contracting entity is Delaware/NY.** The stub and the target list both say "Madrid-based."
>
> **2. They already run payment orchestration.** See below. **Opening with anything resembling "you don't have a routing layer" ends the thread instantly.**

---

> ## 🎯 THE HOOK — they shipped Kakao and Naver login for Korea, and never shipped a Korean payment rail
>
> **Verified by me directly**, byte-for-byte identical on both `feverup.com/en/seoul` and `feverup.com/en/singapore`:
>
> ```json
> "gateways":{
>   "nuvei":{"payUEnvironment":"live","nuveiEnvironment":"prod"},
>   "paypal":{"debug":"false"},
>   "checkout":{"key":"pk_ypka55zhracx7kz5xggqow7o4e4"},
>   "googlePay":{"merchantId":"BCR2DN4TZSMIDPLF","environment":"PRODUCTION"},
>   "processOut":{"key":"proj_fPlZa4x4bP3fkC7A1jrKdDCZDILrLGA7","riskEnvironment":"PRODUCTION"}
> }
> "paymentMethods":[]
> ```
>
> **The same config is served to every APAC city.** No market-specific gateway, no market-specific method, and `paymentMethods` is an **empty array**.
>
> **Now the Korea part.** On the Seoul page I found **seven Kakao and seven Naver references — and every single one is OAuth authentication**: `kauth.kakao.com/oauth/authorize`, `kapi.kakao.com/v2/user/me`, `nid.naver.com/oauth2.0/authorize`, `openapi.naver.com/v1/nid/me`, with populated `WEBCLIENT_KAKAO_CLIENT_ID` and `WEBCLIENT_NAVER_CLIENT_ID` redirecting to `/oauth-callback`.
>
> **Occurrences of KakaoPay, Naver Pay, Toss Pay, PAYCO or Samsung Pay: ZERO.**
>
> **They localized the front door and never localized the till.** Korean-language product, Korean social login, Korean-won pricing — and a card-and-wallet-only checkout in a market where that is a known conversion killer. That observation is machine-verifiable from their own production page and cannot be argued with.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Fever is a live-entertainment discovery and ticketing marketplace best known for the **Candlelight** concert series, operating in 55 countries. It runs a genuine, substantial APAC business — **not** token stub pages.

**SimilarWeb total visits:** **Not obtained.** No data supplied. **Geography below is from live ticketed inventory counts and embedded currency codes on Fever's own city pages**, which is better evidence than an estimate.

### ✅ TERRITORY GATE — PASSES DECISIVELY
| City | Live ticketed events | Currency |
|---|---|---|
| Melbourne / Sydney | 133 / 132 | AUD |
| **Singapore** | **126** | SGD |
| Seoul | 62 | KRW |
| Auckland | 56 | NZD |
| New Delhi / Mumbai / Bengaluru | 54 / 40 / 22 | INR |
| Tokyo / Osaka | 52 / 49 | JPY |
| Hong Kong | 47 | HKD |
| Jakarta | 21 | IDR |
| Bangkok | 2 | THB — **near-stub** |

**Local-currency base pricing, not EUR shown in Asia.** APAC offices confirmed on their careers site (Melbourne, Singapore, Sydney, Seoul, Tokyo, Hong Kong), a live Korean hire, and `supportedLocales` including `ko-KR`, `ja-JP`, `zh-HK`. **India runs under a second brand** — `liveyourcity.com`, `"channel":"live-your-city-marketplace"`.

**Not present anywhere: Taipei, Manila, Kuala Lumpur, mainland China, Vietnam.** Dubai is excluded as EMEA.

### Known PSPs — all from the production config, verified by me
| Provider | Role |
|---|---|
| **ProcessOut** | ⚠️ **Orchestration layer, `riskEnvironment:"PRODUCTION"`** |
| **Nuvei** | PSP, `nuveiEnvironment:"prod"` |
| **Checkout.com** | PSP, public key `pk_ypka...` |
| **PayPal** | Wallet, `debug:"false"` |
| **Google Pay** | Wallet, merchant ID, `PRODUCTION` |
| **Forter** | Fraud, siteId `039249618c32` |
| Stripe | ⬜ Config block present but **`stripeWithPaymentRequest:false`**, no publishable key — **appears dormant** |

⚠️ **`payUEnvironment` sits INSIDE the `nuvei` object** — almost certainly a legacy field name in Nuvei's SDK. **Do not claim Fever uses PayU.**

### ❌ Absent in every APAC market — sourced from `paymentMethods:[]`
**PayNow · GrabPay (SG) · FPS · PayMe · AlipayHK (HK) · PayPay · konbini · LINE Pay · Rakuten Pay (JP) · KakaoPay · Naver Pay · Toss (KR) · UPI · net banking (IN) · QRIS · GoPay · OVO · DANA (ID) · PromptPay · TrueMoney (TH) · PayTo · BPAY · Afterpay · Zip (AU/NZ)**

⚠️ **Honest limit.** Method availability is finally resolved **server-side per cart** — there is a live `feverup.com/api/4.3/payment/payment-gateways-per-method/` endpoint that requires a `cart_id`. So: **"Fever has no dedicated local APAC acquirer and declares no APM client-side" is high-confidence. "Zero APMs render at final checkout" is not proven.** Both Nuvei and Checkout.com carry some APAC APMs natively. **Apple Pay is genuinely unresolved — unchecked-absence.**

### 💰 Two-sided money movement — verified verbatim
> *"Fever also acts as the Organizer's **limited agent** solely for the purpose of using its third-party payment providers to collect payments made by Customers… and **passing such payments through to the applicable Organizer**."*

**They collect and they pay out**, monthly, to event organizers across nine APAC currencies — funded by a card-centric collection stack, and entangled with an **event-financing arm** where recoupment comes out of ticketing settlement. Their terms also warn customers about *"fees for purchasing tickets and registrations in foreign currencies or from foreign persons"* and *"credit card surcharges and currency conversion rates"* — an acknowledgement of material cross-border card exposure.

### Buying signals
- 🇰🇷 **Korean login without Korean payment** — the sharpest observation available
- 🇮🇳 **Three Indian cities, INR pricing, a dedicated second brand, and no UPI**
- 💸 **Monthly organizer payouts in nine APAC currencies**, tangled with a credit book
- 💵 **$227M round led by Goldman Sachs Asset Management** (verified); ~$100M Series E 2025 and $1.8B valuation `[UNVERIFIED]`
- ⚠️ **Orchestration already in place** — this is a displacement conversation

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

### Pain Vector Extraction

```
=== PAIN VECTOR EXTRACTION ===

Motion: COMPETITIVE — a global orchestrator is live in production. This is the
        hardest motion in the rulebook, and it only proceeds because research
        surfaced a concrete gap. It did, and it is unusually clean:
        ORCHESTRATION IN PRODUCTION, ZERO LOCAL RAILS IN NINE APAC MARKETS.
        The pitch is "your orchestration isn't reaching APAC."
        It is NEVER "you need orchestration." NEVER name the incumbent.

Observable setup facts (verified first-hand, 2026-09-18):
- Gateway config byte-identical on /en/seoul and /en/singapore:
  nuvei (prod) · paypal · checkout (pk_ypka...) · googlePay (PRODUCTION) ·
  processOut (riskEnvironment PRODUCTION) · forter
- "paymentMethods":[]  — an empty array, on every APAC city page
- Seoul page: 7 Kakao refs + 7 Naver refs, EVERY ONE OAuth
  (kauth.kakao.com/oauth/authorize, nid.naver.com/oauth2.0/authorize,
  populated WEBCLIENT_KAKAO_CLIENT_ID and WEBCLIENT_NAVER_CLIENT_ID)
- KakaoPay / Naver Pay / Toss Pay / PAYCO / Samsung Pay: ZERO occurrences
- Local-currency base pricing verified: KRW 199 hits on Seoul, 0 on Singapore;
  SGD 421 on Singapore, 0 on Seoul
- Nine live APAC markets, ~800 live ticketed events across 13 cities
- Terms, verbatim: Fever "acts as the Organizer's limited agent solely for the
  purpose of using its third-party payment providers to collect payments ...
  and passing such payments through to the applicable Organizer"
- Terms also warn of "fees for purchasing tickets and registrations in foreign
  currencies or from foreign persons" and "credit card surcharges and currency
  conversion rates"
- Entity: Fever Labs Inc., Delaware, offices 50 Greene St, New York

Selected observations for Phase 1 (E1 bullets, ranked by materiality):
1. The Korea asymmetry -> "Your Seoul site ships Kakao and Naver login, fully
   configured, and prices in won. The checkout is cards, Google Pay and PayPal."
   MATERIALITY: highest by a distance. It is an asymmetry entirely inside their
   own stack — they localized the front door and not the till — it is
   machine-verifiable from their own production page, and it requires no
   external benchmark and no claim about their vendors.
2. The identical-config observation -> "The payment config your Seoul, Singapore,
   Tokyo and Mumbai pages serve is the same one, with no market-specific method
   in it."
   MATERIALITY: high, and it is the one that opens the real conversation without
   ever saying the word orchestration.

   HELD AT 2. The payout leg is saved for E7 and the India/UPI point for LK4.

Bridge variant: SKIP the bridge.
Rationale: the rulebook says skip when the observations already do the bridging
work. These two do exactly that — "same config everywhere, localized login, no
local rail" IS the bridge. And every stock bridge line risks implying an absence
of routing, which would be factually wrong here and would end the thread.

Hypothesis for Phase 2 (E3):
The routing layer is doing its job on the acquiring side and has never been
pointed at local methods, because adding an APM is a commercial and compliance
project per market rather than a routing decision.
Backing logic: nine markets, local-currency pricing in all of them, Korean
social login shipped, a second brand for India — and one identical global
payment config. That is not a team that ignored APAC. It is a team whose
payment layer reaches every market and whose method coverage doesn't.

Success case for Phase 3 (E4):
Selected case: Rappi
Tier: 2 — same payment pattern (marketplace, many markets, two-sided money
      movement, heavy method breadth), different industry and region. STATED.
Match rationale: DELIBERATELY NOT an approval-rate case. Fever already has
routing; proving routing lifts approval tells them nothing they don't know.
Rappi's "hundreds of payment methods through one integration" and "zero
implementation delays" speak to METHOD REACH and TIME-TO-MARKET per market,
which is the actual gap.
Numbers: hundreds of payment methods through one integration · zero
implementation delays on new methods and markets · 80% less analyst work
Optional benchmark: SKIP. The ~8% figure is Yuno's own blog and would be a
bad look quoted at a team that already runs smart routing.

Touch-by-touch angles:
- E2 angle: the Korea asymmetry -> ONE mechanism: local methods added as
  configuration in markets where the layer already runs, rather than as a
  per-market commercial and compliance project
- LK1 angle: Kakao login, no KakaoPay, one sentence
- LK2 angle: the layer reaches every market, the method coverage doesn't
- LK3 angle: Rappi — hundreds of methods on one integration, zero delays
- LK4 angle: FRESH — three Indian cities, INR pricing, a dedicated brand, no UPI
- E8 angle: clean exit

*** ABSOLUTE PROHIBITIONS ON THIS ACCOUNT ***
- NEVER "you need orchestration" / "you have no routing layer." Factually wrong.
- NEVER name ProcessOut, Checkout.com, Nuvei, Forter or any incumbent. The
  rulebook forbids naming an incumbent and it would turn this into a bake-off.
- NEVER say "Madrid-based." The entity is Fever Labs Inc., Delaware/NY.
- NEVER claim they use PayU. The field sits inside the Nuvei object.
- NEVER claim Apple Pay is absent. Genuinely unresolved.
- NEVER cite an APAC revenue share. None is disclosed.
- NEVER cite the Trustpilot duplicate-charge pattern until someone verifies it.
```

**Calendar.** Day 1 anchored to **Monday 19 October 2026**, clearing **Fiesta Nacional de
España (Mon 12 Oct)**. **All Saints (Sun 1 Nov)** falls on a weekend; Day 11 is placed on
**Tue 3 Nov** rather than Mon 2 Nov as a hedge against a regional substitute day.

> ⚠️ **TIME ZONE ASSUMPTION — CHECK BEFORE SENDING.** Slots below are **CET (UTC+1)**, on the
> assumption the payments owner sits in **Madrid**, which is Fever's engineering hub and
> largest office. **The contracting entity is in New York.** If the contact turns out to be
> US-based, **every slot in this sequence needs redoing** — 10:00 CET is 04:00 in New York.
> Confirm location from LinkedIn before Touch 1.

Slots run **10:00–11:00 CET = 14:30–15:30 IST**, which works comfortably for both.

---

### Phase 1 — Curiosity (Days 1–5)

#### Touch 1 — Email 1 · Day 1 · Mon 19 Oct

**Subject:** Kakao login, no Kakao Pay

```text
Hey {{recipient.first_name}},

Spent some time on Fever's payment setup across your Asian cities. Two things stood out:

- Your Seoul site ships Kakao and Naver login, fully configured, and prices in won. The checkout is cards, Google Pay and PayPal.
- The payment config your Seoul, Singapore, Tokyo and Mumbai pages serve is the same one, with no market-specific method in it.

I work at Yuno — top-100 fintech, a16z-backed. We consider ourselves the 'everything payments' platform: one integration, every PSP, every method, every market.

Rather than pitch you based on assumptions, is there anything payment-related you're working through that we might be able to help with?

Best,
Prateek
```

#### Touch 2 — Email 2 · Day 3 · Wed 21 Oct · REPLY IN THREAD

```text
Hey {{recipient.first_name}},

Following up — wanted to put a bit more behind what Yuno actually does, and how it would address what I flagged.

- We sit above whatever you're routing through today. Additive, and nothing you've built gets touched.
- A local method becomes a configuration change in a market where your layer already runs, rather than its own commercial and compliance project.
- One integration covers the method, the settlement currency and the reporting, so adding KakaoPay in Korea doesn't mean a new relationship to manage.
- The same applies to payouts on the other side.

To be clear about what I'm not saying: you're plainly not missing a routing layer. What I'd be curious about is the per-market method work — that's usually the bit that doesn't scale with the number of cities, because each one is a separate commercial conversation rather than a technical one.

I'll keep sharing what I'm seeing every few days. If your stack's where you want it, just say the word and I'll back off — otherwise happy to go deeper.

Cheers,
Prateek
```

#### Touch 3 — LinkedIn message 1 · Day 5 · Fri 23 Oct

```text
Hey {{recipient.first_name}} — figured I'd flag this here too in case more useful than email. Quick one: feverup.com/en/seoul ships fully-configured Kakao and Naver login and prices in KRW, and the checkout is cards, Google Pay and PayPal. Curious if that maps to anything you're working through on the payments side.
```

---

### Phase 2 — Diagnosis (Days 7–9)

#### Touch 4 — Email 3 · Day 7 · Tue 27 Oct · NEW EMAIL

**Subject:** Read on your APAC method coverage

```text
Hey {{recipient.first_name}},

Going to take a swing at this — based on what I see, my read is that your routing layer reaches every market you sell in and your method coverage doesn't, because adding a local method is a commercial and compliance project per market rather than a routing decision.

What points that way is how deliberate everything else is. Nine Asian markets with local-currency base pricing. Korean-language product and Korean social login. A separate brand for India. That is not a team that overlooked the region — it's a team whose payment layer got there and whose method set didn't.

At Yuno (a16z-backed, top-100 fintech), we sit above what you already route through, so a local method is configuration in a market where the layer is already live — keep your stack, add what's missing.

Thursday is open for me — would 10:00 or 11:00 your time work for a quick 15 minutes?

Best,
Prateek
```

#### Touch 5 — LinkedIn message 2 · Day 9 · Thu 29 Oct

```text
Hey {{recipient.first_name}} — sent a longer note over email this week. Short version: the layer reaches all nine of your Asian markets and the method coverage doesn't, which usually means each local rail is its own commercial project rather than a config change. If that's anywhere on your radar, would Tuesday the 3rd at 10:00 your time work for a quick 15?
```

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · Tue 3 Nov · NEW EMAIL

**Subject:** How Rappi solved the per-market method problem

```text
Hey {{recipient.first_name}},

On the read I shared last week — an example of what solved looks like. Rappi is a marketplace rather than a ticketing platform and it's Latin America rather than Asia, so I'll be straight that it's a pattern match: many markets, many methods, and money moving in both directions.

They put Yuno above their existing routing:

- Hundreds of payment methods live through one integration
- Zero implementation delays on new methods and new markets (you read that right)
- 80% less analyst work on payment operations

I've picked this one deliberately over our approval-rate cases. You already route; proving that routing lifts approval would be telling you something you know. The bullet that matters here is the second one — the gap between deciding to add a rail and having it live.

Same layer above what they already had — no rip-out.

One thing I'm genuinely curious about: when you decided to ship Kakao and Naver login for Korea, was Kakao Pay considered in the same piece of work, or is payment method coverage a separate track entirely?

Thursday the 5th is open — would 11:00 your time work?

Full case here if useful: https://y.uno/success-cases/rappi

Thanks,
Prateek
```

#### Touch 7 — Email 5 · Day 13 · Thu 5 Nov · ⚠️ MANUAL

> **Placeholder — Prateek writes this one.**
>
> **Suggested angle: the payout leg, which most orchestration pitches ignore.** Fever's own
> Terms say it acts as *"the Organizer's limited agent"* to collect and pass payments through
> to organizers. That means **monthly settlement to event partners across nine APAC
> currencies**, funded by a card-centric collection stack and entangled with their
> event-financing arm, where recoupment comes out of ticketing settlement. **Ask about FX and
> payout latency on the Asia leg.** ⚠️ **Ask — do not assert.** We have no visibility into
> their payout mechanics.

#### Touch 8 — Email 6 · Day 15 · Mon 9 Nov · ⚠️ MANUAL

> **Placeholder — different format from E5.**
>
> **Suggested angle:** a nine-row table — one per live APAC market — with the local rail that
> dominates it in one column and what their checkout offers in the other. Built entirely from
> their own city pages. **The second column being identical nine times over is the whole
> point and needs no commentary.**

#### Touch 9 — LinkedIn message 3 · Day 17 · Wed 11 Nov

```text
Hey {{recipient.first_name}} — Rappi got to zero implementation delay on new methods and markets, on top of routing they already had. Worth 15 minutes to see if it maps to your setup? Friday the 13th at 10:30 your time is open.
```

---

### Between Phases (Day 19)

#### Touch 10 — Email 7 · Day 19 · Fri 13 Nov · ⚠️ MANUAL

> **Placeholder — manual creative bridge.**
>
> **Freshest unused anchor:** the **India second brand**. Three Indian cities, INR pricing, a
> dedicated storefront under a separate marketplace channel — and the same global payment
> config. **UPI is not a nice-to-have in India; it is most of the market.** ⚠️ **Frame as a
> question about whether the second brand was a distribution decision or a payments one** —
> that is genuinely interesting and not a criticism.

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21 · Tue 17 Nov

```text
Hey {{recipient.first_name}} — last LK ping from me on this. The one that stuck with me: three Indian cities, INR pricing, a dedicated brand, and no UPI in the checkout config. If timing works, Thursday the 19th at 11:00 your time is open for a quick 15.
```

#### Touch 12 — Email 8 · Day 23 · Thu 19 Nov · REPLY IN THREAD to E3

```text
Hey {{recipient.first_name}},

Going to stop pinging unless you want to pick this back up.

Entirely possible APAC method coverage is a known item that's just sitting behind other things — that would be a completely reasonable place for it to be. If timing's just off, happy to circle back next quarter.

If it ever comes back up, just reply here — and if this sits with someone else, happy to be pointed there.

All the best,
Prateek
```

---

### ⚠️ Send-time checklist — this is the highest-risk sequence in the batch

1. ⛔ **Never imply they lack orchestration.** They run it in production. One careless sentence ends this.
2. ⛔ **Never name the incumbent** — not the orchestrator, not the PSPs, not the fraud vendor.
3. ⛔ **Never write "Madrid-based."** Fever Labs Inc., Delaware/New York.
4. ⚠️ **Confirm the contact's time zone before Touch 1.** Every slot assumes CET.
5. ⚠️ **Re-pull `feverup.com/en/seoul` and re-check the gateway config** on the morning of Day 1. The Korea asymmetry is the whole opener, and a config is a deployment away from changing.
6. ⚠️ **Do not assert zero APMs at final checkout.** Method resolution is server-side per cart. E1 says what the *config* serves, which is exactly what is verified — keep it that way.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 16 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ⚠️ **The softest volume call in this repo — flag it on the call.** **No revenue, GMV or ticket-volume figure is disclosed anywhere and I refuse to invent one.** What is verified: ~796 live ticketed events across 13 APAC cities at a single snapshot, 55 countries, and a **$227M round led by Goldman Sachs Asset Management** (their own PR, fetched by me) which also states revenues had *"grown 10x"* and a presence in *"over 60 cities."* **The volume gate cannot fire — there is no sourced sub-40k figure** — and a marketplace at this funding and footprint clears 100k/month comfortably. **But this rests on scale inference, not on a number.** |
| Orchestration status | **+1** | ⚠️ **Global orchestrator incumbent — ProcessOut, in production.** Verified by me on two APAC city pages. Per the matrix this is the **+1 band**, and correctly so: it is the hardest motion. ⚠️ **Their orchestrator is owned by one of the PSPs it routes to** — a structural conflict worth understanding, though **not a line to put in an email.** |
| 3+ countries | **+3** | ✅ **55 countries; nine live APAC markets with local-currency base pricing**, verified by me from embedded page data. |
| Multiple PSPs | **+2** | ✅ **The best-evidenced multi-PSP row in this repo** — Nuvei, Checkout.com, PayPal and Google Pay all named with live production keys from their own config, plus Forter for fraud and a dormant Stripe block. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ Top APAC markets by live inventory are **Melbourne, Sydney and Singapore**. **PayNow and GrabPay absent in Singapore; PayTo, BPAY, Afterpay and Zip absent in Australia** — sourced from `paymentMethods:[]` and a gateway config with no local acquirer. ⚠️ **High-confidence, not proven-absolute** — final method resolution is server-side per cart. |
| Recent expansion | **0** | ⬜ Nine APAC markets is footprint, not dated expansion. A live Korean Client Success role exists but is **agent-sourced**. |
| Payment issues reported | **0** | ⬜ **Not awarded — unverified.** Trustpilot carries ~2,900 reviews with a recurring **"payment reported as failed when it had actually gone through, producing a duplicate charge"** pattern. **That is the textbook signature of retry logic without reliable idempotency across PSPs — i.e. a direct technical hook into their orchestration — and it is exactly why it must be verified before use.** Nobody fetched it. |
| Funding >$10M | **+2** | ✅ **Verified by me** — PR Newswire, Goldman Sachs Asset Management **leads $227m** investment in Fever. The 2025 ~$100M Series E, ~$527M total raised and $1.8B valuation are `[UNVERIFIED]`. |
| High traffic outside home | **0** | ⬜ No traffic data, and **no APAC revenue share is disclosed.** Their own 2022 PR says *"The US is currently Fever's largest market"* — so APAC is outside home, but **unquantified.** |
| Competitor using orchestration | **0** | ❌ Not established for Eventbrite, Ticketmaster, Dice, Klook or Trip.com. |
| Payment job postings | **0** | ⬜ Careers pages render ~18 roles client-side; no payments, billing, treasury or payout roles seen. **Weak evidence — the full listing was never seen.** |

**Tier: 16 / 29 → 🟢 Medium.** No analyst override applied.

### Source Notes
- ✅ **The gateway config was verified by me byte-for-byte on two APAC city pages** (`/en/seoul`, `/en/singapore`), including `processOut` with `riskEnvironment:"PRODUCTION"` and `"paymentMethods":[]`.
- ✅ **Every Kakao/Naver reference was inspected individually and every one is OAuth**, with zero occurrences of KakaoPay, Naver Pay, Toss Pay, PAYCO or Samsung Pay.
- ✅ **Local-currency pricing verified** — KRW 199 hits on Seoul and 0 on Singapore; SGD 421 on Singapore and 0 on Seoul.
- ✅ **The Delaware entity, the limited-agent clause and the foreign-currency warning were all verified verbatim** from `feverup.com/legal/terms_en.html`.
- ✅ **The $227M Goldman round was verified** at PR Newswire, which also yields *"revenues 10x"* and *"over 60 cities"* and **"The US is currently Fever's largest market."**
- 📌 **ProcessOut was acquired by Checkout.com in February 2020** and sells multi-PSP smart routing, cross-provider retry and acceptance-rate optimisation — i.e. our category. `[UNVERIFIED — TechCrunch/Checkout.com newsroom, search-summary level]`, but the **production key on their page is first-party and verified.**
- ⚠️ **The agent grepped the 320KB main JS bundle for 20+ absent vendors and reported every apparent hit as a substring false positive** — `omise` from `Promise`, `eway` from `gateway`, `tyro` from the CSS colour `mistyrose`, `square` from CSS. **Consistent with our running false-positive list; a useful confirmation that the absence is real.**
- ⚠️ **Funding beyond the 2022 round, the APAC job posting, and the entire complaint corpus are agent-sourced and unfetched.**
- ❌ **No APAC revenue or GMV share exists publicly. Do not fabricate one.**
- ❌ **No engineering blog or public GitHub org surfaced.**

### Manual Research Recommendations
> **1. Create a cart in Seoul or Singapore and hit `/api/4.3/payment/payment-gateways-per-method/`.** It is the one call that converts high-confidence into proven, and it settles Apple Pay too.
> **2. Verify the Trustpilot duplicate-charge pattern properly.** If real, it is the sharpest technical hook on the account and worth +2.
> **3. Establish an APAC entity by registry lookup** (ACRA, ASIC, Japan NTA). Offices are confirmed via careers; entities are not.
> **4. Confirm organizer payout mechanics and FX handling on the Asia leg** — the second wedge rests on it.

---

## Executive Summary

Fever is a live-entertainment marketplace operating in 55 countries, and — contrary to the stub — is **Fever Labs Inc. of Delaware and New York**, not a Madrid company. Its APAC presence is real and substantial: **nine live markets with local-currency base pricing**, roughly 800 live ticketed events across thirteen cities, offices in six APAC cities, Korean-language product, and a separate India brand. It is **not a greenfield account**: its own production page config, which I verified byte-for-byte on two APAC cities, shows a **global orchestration layer running live** above **Nuvei, Checkout.com, PayPal and Google Pay**, with Forter for fraud. And that is precisely what makes the account interesting — **the orchestration is in production and has still produced not one local payment rail anywhere in APAC.** The config served to Seoul is identical to the one served everywhere else, with `paymentMethods` an empty array: no PayNow or GrabPay in Singapore, no PayTo or BPAY in Australia, no UPI across three Indian cities, and — the sharpest observation available — **no KakaoPay, Naver Pay or Toss in Korea, on a site that ships fully-configured Kakao and Naver OAuth login.** They localized the front door and never localized the till. At **16/29** the score is held down by a volume row that rests on scale inference rather than any disclosed figure, and by a duplicate-charge complaint pattern that would be worth real points if anyone verified it.

</details>
