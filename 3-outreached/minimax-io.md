# MiniMax (minimax.io) — MiniMax Group Inc., HKEX: 0100

**Status:** 🔵 Outreached — sequence active
**ICP Score:** 23 / 29 → ⭐ **High** — ties z.ai for the highest score in this pipeline, **and unlike z.ai it has no compliance blocker.** This is the actionable one.
**Industry:** AI / LLM — developer API platform + consumer subscription apps (Hailuo AI video, Talkie companion, MiniMax Audio) · **HQ:** Shanghai, China · **Listco:** Cayman Islands · **Billing entity:** Nanonoble Pte. Ltd. (Singapore) · **Researched:** 2026-09-24 · **First email sent:** 2026-10-01
**Motion:** 🛑 IN-HOUSE · two live acquirers already
**Motion detail:** ⚠️ **IN-HOUSE, and not a thin one.** Stripe **and** Airwallex both live in production, plus Alipay on the China build, plus Apple/Google IAP, plus offline bank transfer — all switched by hand-written build flags and a null-check. **Never say "you need orchestration." They built one. Twice.**

---

> ## 🎯 THE HOOK — Apple localises their prices in 15 currencies. They bill the same customers in USD.
>
> **All verified first-hand, 2026-09-24.**
>
> I pulled Talkie Lab's App Store listing storefront by storefront through the iTunes lookup API. Apple charges MiniMax's customers in **VND, IDR, THB, PHP, MYR, KRW, JPY, HKD, SGD, AUD, BRL, MXN, NGN, RUB, GBP and USD** — sixteen currencies.
>
> Their own web checkout does none of that. From the production code: `currency: i.a1 ? "USD" : "CNY"`. Two values. The ToS says *"all payments are in USD."* The price template has the dollar sign **baked in** — `subscribe_modal_price_format = "${{amount}}"`. And the platform ships `locales: ["en"]`.
>
> **They have paid to translate the product into Vietnamese, Portuguese, Korean and Japanese** — the locale map carries `{en, zh-Hans, zh-Intl, zh-Hant, ko, de, ja, fr, vi, pt}` and `hailuoai.video/robots.txt` enumerates live `/vi/`, `/pt/`, `/ko/`, `/ja/` route trees — **and then charges every one of those users in dollars on a card.**
>
> ### And their #1 market cannot be served by their primary acquirer at all
>
> **Vietnam is 15.33% of traffic — their largest market, ahead of India and the US.** Vietnam does not appear anywhere on Stripe's supported-countries page (I checked: 0 occurrences, while Thailand, Singapore, Indonesia, India, Malaysia, Japan, Brazil, Mexico, Nigeria and Hong Kong all appear). Stripe offers **no Vietnamese local rail** — no MoMo, no ZaloPay, no VNPay, no NAPAS.
>
> This is not a dashboard toggle they forgot. **It is an acquirer gap**, and it is the one thing orchestration fixes that a Stripe optimisation cannot.
>
> ### The asymmetry is inside their own business, which is why it can't be argued with
>
> | | Via Apple | Via their own checkout |
> |---|---|---|
> | A Vietnamese buyer pays in | **VND** | **USD** |
> | A Brazilian buyer pays in | **BRL** | **USD** |
> | A Korean buyer pays in | **KRW** | **USD** |
> | Local rail available | — | **none, in any of 122 countries** |
>
> They do not have to take our word for any of it. Both halves are theirs.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** MiniMax is one of China's "AI Tigers" — HKEX-listed January 2026 (stock code **0100**), Cayman listco, Shanghai R&D, and an entire international book contracted out of **two Singapore subsidiaries**. Three revenue lines: the **Open Platform** developer API (`platform.minimax.io`), **Hailuo AI** video (`hailuoai.video`), and **Talkie** AI companion (`talkie-ai.com`). H1 2026 revenue **US$116.6M, +283.1% YoY** — more than the whole of FY2025 — with the Open Platform at **63.4% of revenue**, up from 30.3% a year earlier.

**SimilarWeb traffic:** supplied by Prateek 2026-09-24 as an xlsx export, `minimax.io` + subdomains, 06–08.2026, **122 countries**. ⚠️ **Shares only — no absolute visit count**, so transactions cannot be derived from traffic. Full data: `accounts/traffic/minimax-io.md`.

⚠️ **Scope caveat that matters for sizing.** I resolved the domains myself: `minimaxi.com` → **`minimax.cn`** and `hailuo.ai` → **`agent.minimax.cn`**, so `minimax.io` is the international property and the China business is out of dataset (hence China at only 3.24%). But **Hailuo and Talkie sit on separate domains — `hailuoai.com`, `hailuoai.video`, `talkie-ai.com` — none of which is in this export.** The supplied data therefore covers the developer/API/agent estate only. **Ask Prateek for `talkie-ai.com` and `hailuoai.com` traffic before sizing.**

### Top markets against the accepted payment set
The accepted set is identical in all 122 international markets: **card, via Stripe or Airwallex, in USD.** There is no geo-adaptation of rails — only of price *display*.

| Rank | Country | Traffic | Accepted | Missing | Local entity |
|---|---|---|---|---|---|
| 1 | 🇻🇳 **Vietnam** | **15.33%** ▼18.38% | Card, USD | ❌ **MoMo, ZaloPay, VNPay/VietQR, NAPAS, Viettel Money** — *and Stripe cannot serve any of them* | ❌ None |
| 2 | 🇮🇳 India | **10.94%** ▲38.96% | Card, USD | ❌ **UPI, UPI Autopay, netbanking, RuPay, EMI** | ❌ None |
| 3 | 🇺🇸 United States | **9.08%** ▲16.96% | Card, Apple Pay, Google Pay, Link | — | ❌ None |
| 4 | 🇧🇷 Brazil | **5.23%** ▲1.04% | Card, USD | ❌ **Pix, boleto, parcelamento** | ❌ None |
| 5 | 🇰🇷 South Korea | **3.45%** ▲7.89% | Card, USD | ❌ **KakaoPay, Naver Pay, Toss, local card PG** | ❌ None |
| 6 | 🇨🇳 China | 3.24% ▲**33.16%** | **Alipay + WeChat Pay, CNY** — *but only on `minimax.cn`/`hailuoai.com`* | Those rails on the `.io` property | ✅ 3 PRC entities |
| 7 | 🇮🇩 Indonesia | 2.87% ▼2.47% | Card, USD | ❌ **QRIS, virtual account, GoPay/OVO/DANA, OTC cash** | ❌ None |
| 8 | 🇲🇽 Mexico | 2.78% ▲0.16% | Card, USD | ❌ **OXXO, SPEI, meses sin intereses** | ❌ None |
| 9 | 🇳🇬 Nigeria | 2.24% ▲**47.99%** | Card, USD | ❌ Local rails, USSD, bank transfer | ❌ None |
| 10 | 🇷🇺 Russia | 2.10% ▲32.21% | — | ❌ **Effectively unserved.** Stripe does not acquire in Russia. ❌ Mir, SBP | ❌ None |
| 17 | 🇰🇿 Kazakhstan | 1.62% ▲**277%** | Card, USD | ❌ **Kaspi.kz** | ❌ None |
| 18 | 🇹🇭 Thailand | 1.51% ▲12.86% | Card, USD | ❌ PromptPay, TrueMoney | ❌ None |
| 23 | 🇹🇼 Taiwan | 1.12% ▲14.11% | Card, USD | ❌ JKOPay, LINE Pay, store cash, instalments | ❌ None |
| 24 | 🇸🇬 Singapore | 1.09% ▲**52.77%** | Card, USD | ❌ PayNow, GrabPay | ✅ **Nanonoble + SUBSUP** |
| 30 | 🇯🇵 Japan | 0.74% ▲**130%** | Card, USD | ❌ konbini, PayPay, Rakuten Pay, Paidy | ❌ None |

⚠️ **Brazil, Mexico, Nigeria, Russia, Kazakhstan and Egypt are out of APAC territory.** MiniMax is China-HQ'd so the *account* is in scope per `CLAUDE.md`; those rows are corridor evidence only.

### Legal entities — the whole international book sits in Singapore
Verified by me in the platform ToS and privacy policy, and corroborated in the HKEX prospectus:
- ⭐ **Nanonoble Pte. Ltd.** — **152 Beach Road, #14-02 Gateway East, Singapore 189721**. Incorporated **19 March 2024**, SGD 50,000, 100% indirect. *"This website is operated by Nanonoble Pte. Ltd."* **Bills the Open Platform, Hailuo and MiniMax Audio.** Contact `contact.nanonoble@minimax.io`.
- **SUBSUP Pte. Ltd.** — Singapore, incorporated **14 September 2022**, SGD 50,000, 100% indirect. **Bills Talkie**; independently confirmed by me as the App Store seller-of-record (`sellerName: SUBSUP PTE. LTD.`, bundle `com.tara.ai`).
- Prospectus, verbatim, read by me: *"As at the Latest Practicable Date, our Company has **2 major subsidiaries, Subsup Pte. Ltd. and Nanonoble Pte. Ltd.** (the 'Singapore Subsidiaries')."*
- **MiniMax Group Inc.** — Cayman Islands listco, WVR structure, HKEX **0100**.
- PRC: Shanghai Xiyu Technology, Shanghai Xiyu Jizhi, Beijing Xiyu Jizhi (R&D and the domestic platform).
- **Governing law Singapore; arbitration SIAC.** Clean paper, no PRC-entity procurement friction.

⚠️ **`Nanonoble` contains no reference to MiniMax.** That is the mirror image of the z.ai trap: there the *listed* name was stale, here the *operating* name is unbranded. A name-only screen tells you nothing either way.

### Known PSPs — five channels, and they wrote the switch themselves
| Channel | Evidence (mine) | Scope |
|---|---|---|
| **Stripe** | `plan.detail.autoRenewMethod` = **"Stripe auto-renewal"**; *"Payment details are securely processed by Stripe"*; **MiniMax is a named Stripe reference customer** | Primary card rail, overseas |
| **Airwallex** | **35 hits across 4 chunks of the live `prod-en-0.1.869` build**, incl. the real SDK loader (`checkout.airwallex.com` with prod/demo/staging/dev env map), Elements SDK **v1.142.1**, and `type:"airwallex"` in the payment tracker | **Hailuo only.** It is a first-class member of the platform channel enum (`AirWallex=1`) but no `platform.minimax.io` call site *creates* an Airwallex charge — consistent with it being the **legacy** acquirer, surviving in the Hailuo fallback branch |
| **Alipay** | `type:"alipay"`, `aliJumpUrl`, QR flow — **hostname-gated to `.cn`** | China build only |
| **Apple / Google IAP** | `store_type` enum `AppleAppStore=1, GooglePlay=2, WebStripe=3` | Talkie primarily |
| **Offline bank transfer** | Merchant's own FAQ, twice (below) | Open Platform |

**Orchestrator: NONE.** Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY, Yuno — zero hits across 427 production chunks pulled from six codebases. Also absent: Adyen, Checkout.com, Braintree, PayerMax, Antom, Paddle, dLocal, **and PayPal anywhere**.

**What exists instead is a hand-written switch.** I read the branch myself in `ch/c29.js` of the live build:
```js
if (C.a1 && y.jumpUrl) { … type:"stripe";  navigate(y.jumpUrl); return; }   // overseas + server gave a URL → Stripe
if (C.Xy)              { … alipay QR / aliJumpUrl }                          // China build
else                   { … type:"airwallex";  Airwallex SDK }                // overseas fallback
```
And from `agent.minimax.io`: `function E(){ return i.a1 ? r.xZ.Stripe : r.xZ.AliPay }`. **Two build flags and a null-check are the entire routing layer.** Airwallex also carries the card-on-file recurring path: `recurringOptions:{card:{next_triggered_by:"merchant", merchant_trigger_reason:"scheduled"}}`.

### The three findings that would open a conversation
1. **Apple bills their customers in 16 currencies; they bill in one.** Verified storefront by storefront. See the hook.
2. **Provisioning is decoupled from authorisation, and it is costing them money in public.** Trustpilot **1.4/5** across 94 reviews, **82% one-star**, dominated by billing. 18+ open GitHub payment issues. Their own UI ships two separate **"Do not pay again"** strings.
3. **They never touch card data, and have no 3DS control of their own.** Zero `pk_live_*` keys and zero `confirmCardPayment`/`requiresAction` handling across 507 mined files — **every card flow is a server-created hosted redirect.** ⭐ **That is the opposite of z.ai**, which captures cards itself on Stripe Elements and shipped a `confirmCardPayment` crash to a buyer. MiniMax is architecturally safer and PCI-lighter — **and it means they have no control over 3DS exemptions or challenge rates at all.** Those decisions sit entirely inside Stripe and Airwallex.
4. **They have already migrated payment platforms once and already run two acquirers.** Their own i18n: *"Due to our transaction platform change, early invoices need to be retrieved via this link."* And Stripe's case study quotes their GM: *"**Compared to our previous payment solution**, Stripe required fewer development resources."*

</details>

<details>
<summary><h2>✉️ Section 2 — Full Outreach Sequence</h2></summary>

### Pain Vector Extraction

**Motion:** **IN-HOUSE** — and not a thin one. Stripe primary, Airwallex live on Hailuo, Alipay on the China build, Apple/Google IAP, plus offline bank transfer. Routed by two build flags and a `jumpUrl` null-check. A live public config shows `backend_payment_migration_percent: 100`, i.e. they have **just finished** rebuilding the payment backend themselves. **Never imply they need orchestration, and never imply the build was wrong.**

**App-store trap checked (§4, `subscription-payments.md`): PASSES.** IAP does not dominate. H1 2026 is 63.4% Open Platform, which carries no IAP at all, and ~70–80% of the consumer book runs on web rails. Roughly **85% of revenue is addressable.** The mix inverted from 67% consumer in FY2025, so the old objection no longer holds.

**Observable setup facts (all verified first-hand, see Section 3):**
- Apple bills their customers in **16 currencies** (VND, IDR, THB, PHP, MYR, KRW, JPY, HKD, SGD, AUD, BRL, MXN, NGN, RUB, GBP, USD) — iTunes lookup, storefront by storefront
- Their own checkout is USD-only: `currency: i.a1 ? "USD" : "CNY"`, `$` hardcoded in the price template, `locales: ["en"]`, and the ToS reads *"all payments are in USD"*
- Their own docs publish the accepted set twice: *"two ways to fund your account: **Online Payment** and **Bank Transfer**"* — source: `platform.minimax.io/docs/faq/about-account.md`
- **Vietnam is the #1 market at 15.33%** of traffic; Stripe has **no Vietnamese local rail at all** and Vietnam is absent from its supported-countries page
- They shipped `vi`, `pt`, `ko`, `ja` locales with live route trees, and bill all of them in USD
- CNY 36 against USD 5 in a public config: a **hardcoded 7.2 FX peg**, not a rate feed
- Prospectus risk factor, verbatim: *"We collaborate with third-party online payment channels for payment collection. Any interruption of their services… Any interruption in their payment services could adversely affect our payment collection, and in turn, our revenue."*
- Talkie was pulled from Apple's App Store for ~2 months from mid-December 2024; **average daily downloads fell ~16,800** (prospectus)
- Every card flow is a server-created hosted redirect, so **no 3DS or retry control sits with them**

**Selected observations for Phase 1 (ranked by materiality):**
1. **Currency asymmetry inside their own business** → *"Apple bills your users in sixteen currencies. Your own checkout bills in one."* Highest materiality: both halves are theirs, neither is disputable, and it is the exact shape the voice anchor calls strongest.
2. **Vietnam #1 with no reachable local rail** → *"Vietnam is your largest market and your docs list two ways to pay: online payment and bank transfer."* Uses their own document, per the samples' most repeatable habit.
3. **Localisation/payment split** → *"You shipped Vietnamese, Portuguese, Korean and Japanese, and charge all four in dollars."*

**Bridge variant:** **A — complexity.** Five payment channels across two regional builds and two Singapore entities, with the switch hand-written. Not "limitations" — the estate is genuinely multi-provider.

**Hypothesis for Phase 2 (E3):** Buyers in Vietnam, India, Brazil and Nigeria paying a USD card cross-border against a Singapore entity are the least likely in their base to hold an international card and the most likely to be declined by their issuer — and because every flow is a hosted redirect, the retry and 3DS decisions sit with the PSP rather than with MiniMax.
**Backing logic:** ~37% of traffic sits in markets where cards are the minority rail; the same users pay Apple in local currency, so the willingness to pay is demonstrated and the gap is at the rail, not at the price.

**Success case for Phase 3 (E4):** **Vibra** · **Tier 2 — same payment pattern, different industry.**
Match rationale: MiniMax is acquiring **first-time payers** in emerging markets, which is exactly what Vibra's numbers measure, and Vibra also launched new methods rather than only tuning existing ones. Honest adjacency worth stating: Vibra's results came from **Brazil, which is MiniMax's #4 market at 5.23%** — so the market is genuinely shared, and no APAC claim is implied.
Numbers to lead with: new-user approval lifted **more than 30 percentage points, to 80%**; launched **Apple Pay, Nu Pay and Google Pay**; same orchestration layer above the existing stack.
Optional benchmark: **SKIP.** The ~8% routing uplift traces to Yuno's own blog, not an independent study.

**Touch-by-touch angles:**
- **E2:** currency/rail asymmetry → *one integration to add any method, no per-rail rebuild* (plus the additive point, which matters more here than usual given the replatform they just finished)
- **LK1:** Apple's sixteen currencies against their one
- **LK2:** the cross-border decline hypothesis, one sentence
- **LK3:** Vibra's first-time-buyer number
- **LK4:** Vietnam, stripped to one line
- **E8:** clean exit, no new argument

---

### 📅 Schedule — shifted to clear China's Golden Week

⚠️ **Day 1 is Thursday 8 October 2026, not today.** China's National Day falls on **1 October** and the holiday week runs **1–7 October**; Mid-Autumn Festival is **25 September**. A sequence starting 24 September would land E3, LK2 and E4 — the diagnosis email and two of the five meeting asks — inside Golden Week, when nobody at a Shanghai company is reading cold email. Weekend touches are pushed to the next business day.

| Touch | Day | Send date |
|---|---|---|
| E1 | 1 | Thu 8 Oct 2026 |
| E2 | 3 | Fri 9 Oct 2026 |
| LK1 | 5 | Mon 12 Oct 2026 |
| E3 ★ | 7 | Wed 14 Oct 2026 |
| LK2 ★ | 9 | Fri 16 Oct 2026 |
| E4 ★ | 11 | Mon 19 Oct 2026 |
| E5 *(manual)* | 13 | Tue 20 Oct 2026 |
| E6 *(manual)* | 15 | Thu 22 Oct 2026 |
| LK3 ★ | 17 | Mon 26 Oct 2026 |
| E7 *(manual)* | 19 | Tue 27 Oct 2026 |
| LK4 ★ | 21 | Wed 28 Oct 2026 |
| E8 | 23 | Fri 30 Oct 2026 |

All proposed meeting times are **China Standard Time (UTC+8)**. Prateek is IST, CST minus 2:30, so every slot below is comfortable at both ends.

---

### Phase 1 — Curiosity (Days 1–5)

#### Touch 1 — Email 1 · Day 1 · Thu 8 Oct

**Subject:** Sixteen currencies, then one

```text
Hey {{recipient.first_name}},

Spent some time looking at MiniMax's payment setup. A few things stood out.

Apple bills your users in sixteen currencies. I checked storefront by storefront: dong,
rupiah, baht, peso, won, yen, real. Your own checkout bills in dollars.

Vietnam is your largest market by traffic. Your docs list two ways to fund an account,
online payment and bank transfer.

You shipped Vietnamese, Portuguese, Korean and Japanese, and charge all four in dollars.

That kind of setup usually comes with some complexity.

I work at Yuno, top-100 fintech, a16z-backed. We consider ourselves the "everything
payments" platform: one integration, every PSP, every method, every market.

Rather than pitch you based on assumptions, is there anything payment-related you're working
through that we might be able to help with?

Best,
Prateek
```

#### Touch 2 — Email 2 · Day 3 · Fri 9 Oct · REPLY IN THREAD

```text
Hey {{recipient.first_name}},

Following up. Wanted to put a bit more behind what Yuno actually does, and how it would
address what I flagged.

We sit above the providers you already run, so nothing gets ripped out. You keep Stripe.
Routing happens per BIN, market and method, to whichever rail performs best for that
transaction. If a provider degrades, traffic moves without anyone being paged. And adding a
new method, acquirer or rail is a config change on one integration rather than a build.

That last one is the piece that matters for the currency gap. MoMo in Vietnam, UPI in India,
Pix in Brazil: those arrive as methods on the integration you already have, not as four
separate projects.

I'll keep sharing what I'm seeing every few days. If your stack's where you want it, just
say the word and I'll back off. Otherwise happy to go deeper.

Cheers,
Prateek
```

#### Touch 3 — LinkedIn message 1 · Day 5 · Mon 12 Oct

```text
Hey {{recipient.first_name}}, figured I'd flag this here too in case more useful than email.

Quick one: Apple bills MiniMax users in sixteen currencies, your own checkout bills in
dollars. I went storefront by storefront to check.

Curious if that maps to anything you're working through on the payments side.
```

---

### Phase 2 — Diagnosis (Days 7–9)

#### Touch 4 — Email 3 · Day 7 · Wed 14 Oct · NEW EMAIL

**Subject:** Read on your Vietnam exposure

```text
Hey {{recipient.first_name}},

Going to take a swing at this. Based on what I can see, my read is that your approval rate
is weakest exactly where your growth is: buyers in Vietnam, India, Brazil and Nigeria paying
a dollar card, cross-border, against a Singapore entity.

Those are the buyers least likely to hold an international card and the most likely to be
declined by their own issuer, not because anyone's doing it badly. And the same users pay
Apple in their own currency, so the willingness to pay is already proven. The gap sits at
the rail.

Worth asking: when a first-time buyer in Vietnam fails, do you see it as a decline or as
someone who changed their mind?

At Yuno, a16z-backed and top-100 fintech, we sit above your existing PSPs so you can reach
local rails per market without another payments project. Keep your stack, add what's
missing.

Monday the 19th is open for me. Would 3pm or 4:30pm your time work for a quick 15 minutes?
If payments sits elsewhere, happy to be pointed there.

All the best,
Prateek
```

#### Touch 5 — LinkedIn message 2 · Day 9 · Fri 16 Oct

```text
Hey {{recipient.first_name}}, sent a longer note over email this week.

Short version: the buyers driving your growth in Vietnam, India and Brazil are the ones a
dollar card cross-border tends to serve worst, and they already pay Apple in local currency.

If that's anywhere on your radar, would Tuesday the 20th at 11:30am your time work for a
quick 15?
```

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · Mon 19 Oct · NEW EMAIL

**Subject:** How Vibra solved this

```text
Hey {{recipient.first_name}},

On the read I shared last week, sharing a quick example of what solved looks like.

Vibra runs a retail and loyalty business in Brazil, which is your fourth-largest market. Most
of their buyers were paying for the first time, same as yours in Vietnam and India. They
partnered with Yuno to lift approval on exactly that cohort:

- New-user approval went up more than 30 percentage points, to 80% (you read that right)
- Launched Apple Pay, Nu Pay and Google Pay on the same integration
- No change to the providers already underneath

Different industry, same payment pattern: first-time payers in a market where the card is
not the default rail. I'd rather be straight that this is a pattern match than dress it up
as an AI case.

For adjacency closer to home, NetEase Games and Garena both run on us across Asia. No
published numbers on either, so I won't invent any.

Thursday the 22nd is open. Would 11am or 4pm your time work for 15 minutes?

Full case here if useful: https://y.uno/en/success-stories/vibra

Looking forward to it,
Prateek
```

#### Touch 7 — Email 5 · Day 13 · Tue 20 Oct · MANUAL
*Placeholder — manual creative approach. Do not auto-write.*

**Suggested angle, strongest material available:** a short annotated walkthrough of the currency asymmetry. Two screenshots side by side — the Talkie App Store listing in the Vietnam storefront showing a dong price, and their own checkout showing dollars. Nothing needs saying over the top of it.

#### Touch 8 — Email 6 · Day 15 · Thu 22 Oct · MANUAL
*Placeholder — second manual approach, different format from E5.*

**Suggested angle:** quote their own prospectus risk factor back to them, one line, no commentary: *"Any interruption in their payment services could adversely affect our payment collection, and in turn, our revenue."* Then one sentence on what a second rail with automatic failover does to that sentence.

#### Touch 9 — LinkedIn message 3 · Day 17 · Mon 26 Oct

```text
Hey {{recipient.first_name}}, one proof point rather than another argument.

Vibra lifted first-time-buyer approval past 80% on the providers they already had, by adding
local methods on one integration rather than rebuilding per rail.

Worth 15 minutes to see if it maps to your setup? Wednesday the 28th at 3:30pm your time is
open.
```

---

### Touch 10 — Email 7 · Day 19 · Tue 27 Oct · MANUAL
*Placeholder — manual creative bridge. Anchor to something fresh.*

**Fresh anchors available, unused so far in the sequence:** the Team Token Plan withdrawal effective 5 September 2026 (packaging churn, worth a genuine question); the H1 2026 results, where Open Platform revenue grew 703% and became 63.4% of the business; or the HKEX listing itself if a relevant filing lands in the window.

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21 · Wed 28 Oct

```text
Hey {{recipient.first_name}}, last LinkedIn ping from me on this.

Your Korean and Japanese buyers are on the same dollar card as everyone else, and both
markets have local rails that convert better.

If timing works, Monday the 2nd at 12pm your time is open for a quick 15.
```

#### Touch 12 — Email 8 · Day 23 · Fri 30 Oct · REPLY IN THREAD to Touch 4 or 6

```text
Hey {{recipient.first_name}},

Going to stop pinging unless you want to pick this back up.

If the timing is just off, happy to circle back in the new year. And if it ever comes back
up, just reply here.

All the best,
Prateek
```

---

### Source Notes

- ✅ **Apple bills in 16 currencies** — iTunes lookup API, `id=6740326134`, tested per storefront 2026-09-24: VND, IDR, THB, PHP, MYR, KRW, JPY, HKD, SGD, AUD, BRL, MXN, NGN, RUB, GBP, USD
- ✅ **Own checkout is USD-only** — `currency: i.a1 ? "USD" : "CNY"` in production bundles; `subscribe_modal_price_format = "${{amount}}"`; `locales: ["en"]`; ToS *"all payments are in USD"*
- ✅ **"Online Payment and Bank Transfer"** — `platform.minimax.io/docs/faq/about-account.md`, and again in the homepage FAQPage JSON-LD
- ✅ **Vietnam 15.33%, #1 market** — SimilarWeb supplied by Prateek 2026-09-24, `accounts/traffic/minimax-io.md`
- ✅ **Stripe has no Vietnamese rail** — Vietnam absent from `stripe.com/global`, 0 occurrences, while 10 other named markets appear
- ✅ **vi / pt / ko / ja locales shipped** — locale map plus live route trees in `hailuoai.video/robots.txt`
- ✅ **Vibra numbers** — https://y.uno/en/success-stories/vibra
- ✅ **NetEase Games and Garena nameable** — Yuno's site-wide "TRUSTED BY GLOBAL TEAMS" list. **No numbers exist for either; none used**
- ✅ **Brazil is MiniMax's #4 market at 5.23%** — same SimilarWeb export
- ✅ **Prospectus payment-channel risk factor** (E6 placeholder) — HKEX prospectus, read directly
- ✅ **Team Token Plan withdrawal, 5 Sept 2026** (E7 anchor) — live public config `code_plan_detail`
- ⚠️ **Not used anywhere, deliberately:** Trustpilot 1.4/5, the 18+ open GitHub payment threads, and the "Do not pay again" strings. All verified, all true, all far too close to naming a merchant's public complaints in a cold thread. They are reply material, not opening material.
- ⚠️ **Not used:** the US$800M ARR figure. Secondary only, and it contradicts the first-party H1 2026 number.
- ⚠️ **Not used:** the Disney/Hollywood copyright suit and the Anthropic distillation accusation. Live reputational matters, irrelevant to payments, and raising either would end the thread.

### Success Case Alternatives

- **Livelo** — the decline-cascade case: +5% approval, 50% of failed transactions recovered. The better choice if a reply shifts the conversation onto failover between Stripe and Airwallex specifically, since Livelo is the case where a secondary acquirer recovers declines.
- **inDrive** — ~90% approval across 50+ countries, 10 new countries in under 8 months. Use if the conversation turns to market breadth rather than approval on a cohort.
- **Rappi** — hundreds of methods, 80% less analyst work. Use if they raise the engineering cost of maintaining the switch themselves.

</details>

<details>
<summary><h2>🔍 Section 3 — Full Research</h2></summary>

## 1. ICP Score Breakdown — 23 / 29 ⭐

| Signal | Max | Awarded | Basis |
|---|---|---|---|
| Transaction volume / company size | 5 | **5** | HKEX **0100**, market cap ~**HK$97bn**. H1 2026 revenue **US$116.6M**, +283.1% YoY. **Sourced floor: 1,771,600 AI-native paying users in 9M2025** against the prospectus's own definition — *"a user who has made **at least one monetary transaction** in a given period"* — i.e. **≥197,000 transactions/month, ~5× the 40k floor**, and that is 2025 data against a business that has since roughly quadrupled. |
| Orchestration status | 4 | **1** | **In-house.** Two live acquirers + Alipay + IAP + bank transfer, routed by build flags. |
| Operates 3+ countries | 3 | **3** | 122 countries in traffic; **">230 countries and regions"** per the company. |
| Multiple PSPs | 3 | **3** | Stripe, Airwallex, Alipay (CN), Apple/Google IAP, offline bank transfer. Genuinely multiple and separately reconciled. |
| Local rail gap | 3 | **3** | **Zero APMs in all 122 international markets.** Maximum award. |
| Recent expansion | 2 | **2** | HKEX IPO Jan 2026. Open Platform **+703.1%** YoY. CEO's stated **Southeast Asia pivot**. Token consumption **20× Jan→Jul 2026**. |
| Known payment issues | 2 | **2** | Trustpilot **1.4/5** (82% 1-star), 18+ open GitHub payment issues, two "Do not pay again" strings. The strongest payment-failure corpus of any account in this pipeline. |
| Recent funding | 2 | **2** | IPO ~**HK$4.8bn**; cash **US$1,322.8M** at 30 Jun 2026. |
| Traffic outside home market | 2 | **2** | China 3.24% of traffic (**96.76% non-China**); **>70% of revenue international**; **APAC 61.1% of revenue** (9M2025). |
| Competitor orchestration | 2 | **0** | **None.** Verified across both consumer sets and the LLM-API peer group. |
| Payment job postings | 1 | **0** | None found. |
| **Total** | **29** | **23** | ⭐ **High** |

**⭐ The comparison that matters:** this ties z.ai at 23/29 — **and it has no export-control blocker.** Of the two, this is the one to work.

## 2. Export control — checked myself, and it is clean

I ran the identical methodology that found z.ai on the Entity List. **Every grep sanity-checked against a known positive.**

| Regime | Result | Sanity control |
|---|---|---|
| **BIS Entity List** (current eCFR, Supp. 4 to 15 CFR 744) | **0 hits** | Zhipu 8, Huawei 185 ✅ |
| **Federal Register**, all time | **2 hits — both the German fire-protection company** (*Halon Alternatives Research Corporation* notices, 2011 & 2015). `Xiyu` 0, `稀宇` 0 | count field read verbatim |
| **OFAC SDN** | 0 | SBERBANK 71 ✅ |
| **OFAC Consolidated** (incl. NS-CMIC) | 0 | HUAWEI 7 ✅ |
| **DoD Section 1260H** | 0 | Inspur 2 ✅ |
| **BIS Denied Persons** | 0 | 382 rows ✅ |

🪤 **The Entity List returned 6 hits for "Xiyu" — all six are street addresses.** Xiyuan 8th Road (Hangzhou), No. 1899 Xiyuan Avenue (Huawei, Chengdu), Xiyuan 1st Road (UMEC, Chongqing), Manjinghua **Xiyue** Courtyard (Shenzhen). None is a company. **New false positive for the running list: `Xiyuan` / `Xiyue` → Xiyu.**

⚠️ **Process note worth keeping.** My first Denied Persons download truncated at 30KB and the sanity check failed. A silently truncated download looks *exactly* like a clean negative. I re-fetched at 150KB and re-validated before accepting it. **Always sanity-check the grep, not just the result.**

⚠️ Two honest limits: the US list files contain **no CJK at all**, so the `稀宇` = 0 result on them is uninformative — the romanised `Xiyu` search carries the weight. And this is a **screening result, not a legal opinion**; compliance still owns the call. But there is nothing here to block on, and the BIS 50% Affiliates Rule that threatens z.ai on 10 Nov 2026 **does not apply**, because no parent of MiniMax is listed.

Corroborating, from their own prospectus: the Entity List is discussed only **prospectively** — *"Our operations may be negatively affected **if any of our business partners are added to the Entity List**"* — with no disclosure of the company itself being listed, in a document vetted by US counsel. Their ToS also imposes EAR/OFAC compliance on *their* customers. They are the ones screening, not the screened.

## 3. The stack, in their own code

**Channel enum, found independently in four separate codebases with identical values:**
```
AirWallex=1, BusinessWallet=2, Stripe=3, AliPay=4, Wechat=5, Apple=6, Google=7
```
and Talkie's own: `store_type { ALL=0, AppleAppStore=1, GooglePlay=2, WebStripe=3 }`.

**Currency, from every analytics and purchase call:** `currency: i.a1 ? "USD" : "CNY"`. **Two values. No VND, INR, BRL, KRW, IDR, MXN or TRY anywhere.**

**The geo switch is a single boolean, and I verified both sides.** Same code build, server config differs:

| Property | `showWechatPayIcon` | Locale | Currency |
|---|---|---|---|
| `hailuoai.video` (international) | **`false`** | `en` | `$` only |
| `hailuoai.com` (China) | **`true`** | `zh-Hans` | `¥` (64 occurrences) |

Both from the same `initStore.global` config block. Alipay's deep-link builder hardcodes `platform.minimax.cn`, so **Alipay and WeChat are gated by hostname in code, not merely unused.**

⭐ **A payment-platform migration is admitted in their own strings.** i18n key `text_invoices_tip`: *"Due to our transaction platform change, early invoices need to be retrieved via this link."* And `invoice_disabled_toast`: *"该支付方式不支持开票"* ("this payment method does not support invoicing") — i.e. ≥2 methods with divergent invoicing capability. Stripe's own case study closes the loop with their GM's words: *"**Compared to our previous payment solution**, Stripe required fewer development resources."*

### ⭐ They just finished rebuilding the payment backend themselves — and a live public endpoint says so

`platform.minimax.io/setting/get_app_settings` is **open and unauthenticated**, and the shipped bundle routes every payment call between two service prefixes by remote-config percentage:

```js
a = d6 + "/backend/payment"   // new, in-house
s = d6 + "/inner/payment"     // legacy
// whitelist(uid) -> a ;  percent <= 0 -> s ;  bucket(uid) < percent -> a : s
```

**I called it myself. Verbatim response, 2026-09-24:**
```json
GET /setting/get_app_settings?fe_setting_key=backend_payment_migration_percent
{ "percent": 100, "whitelist": ["516653005974216705","505160597037699075"] }
```

**`percent: 100`.** The cutover to their own new payment service is fully rolled out, with the dual-path scaffolding and a two-uid whitelist still shipped in production. Combined with their own i18n string *"Due to our transaction platform change"* and their GM's *"compared to our previous payment solution"* — **this company has replatformed payments at least once and finished doing it recently.** They are not a merchant who hasn't thought about this; they are a merchant who has just paid for it.

⚠️ **Read that carefully before drafting.** It cuts both ways: a team that just shipped a payment replatform has *less* appetite for another project and *more* scar tissue about the cost. The E2 mechanism line should lead with **additive** — Yuno sits above what they just built — not with replacement.

### ⭐ Their CNY price is a hardcoded 7.2× multiple of the USD price

Same open endpoint, verbatim:
```json
GET /setting/get_app_settings?fe_setting_key=price_pre_credit
{ "zh": { "price_per_step_credit": 36, "min_credits": 5000, "max_credits": 9995000, "credit_step": 5000 },
  "en": { "price_per_step_credit": 5,  "min_credits": 5000, "max_credits": 9995000, "credit_step": 5000 } }
```

- **$5 per 5,000 credits**, minimum 5,000, maximum 9,995,000 → **maximum single top-up ≈ US$9,995.**
- **CNY 36 against USD 5 = exactly 7.2.** Two hardcoded integers in a config file, not a rate feed. **The entire CN/international price relationship is one hand-set FX peg**, and it moves only when someone edits a config value. That is the same class of finding as the currency template — pricing localisation done by hand, at two points, for two currencies.

### Packaging is churning right now
Same endpoint, `code_plan_detail`, verbatim English:
> *"Effective September 5, 2026, MiniMax will discontinue new purchases and renewals of Team Token Plans, as well as credit top-ups for Team accounts."*

**19 days before this report they withdrew the team/seat SKU from sale.** Worth a discovery question — pulling a team plan usually means either billing complexity they did not want to carry, or a repackaging underway.

### The credit ledger is genuinely complicated
From `media_plan_faq`: membership credits expire **31 days** from crediting; purchased top-up credits **1 year**; new-user free credits **3 days**; and *"when multiple credit batches exist, the platform consumes the earliest-expiring first."* Four balance types with three expiry regimes and FIFO-by-expiry consumption — on top of the balance-and-voucher waterfall. **This is why a large share of renewals never reach a card, and why their invoicing is manual.**

**Other billing mechanics, verified in the i18n dictionary (661 key/value pairs):**
- Balance-first waterfall: *"Your balance and voucher will be used to complete this payment. No additional charge will be applied."* → **many renewals never touch a card**
- `plan.detail.autoRenewFailed` = "Auto-renewal failed" — renewal failure is a first-class UI state
- **Vouchers** with lifecycle states (notEffective / inEffect / exhausted / expired)
- Subscription shape: `comboType` starter/plus/max/highSpeed × `cycleType` month/quarter/year
- Usage windows of 5-hour / weekly / daily — the same architecture as z.ai's Coding Plan
- **An `Autobilling` auto-recharge feature**, per their own FAQ
- Manual invoicing fallback: *"There are no online payment orders available for self-service invoicing. Please contact api@minimax.io to request an invoice."*
- ⚠️ **A 1%-per-day late fee** and termination at 15 days overdue, from the ToS — so there is a postpaid/invoiced channel alongside the self-serve card book

## 4. Local payment methods — zero, and the merchant says so itself

⭐ **The strongest evidence type available: a positive statement of the accepted set, published twice.**

**Their docs** (`platform.minimax.io/docs/faq/about-account.md`), verbatim:
> *"We offer two ways to fund your account: **Online Payment** and **Bank Transfer**."*

**Their homepage FAQPage JSON-LD** (`www.minimax.io`), verbatim:
> *"MiniMax API Platform currently supports two types of top-up methods: **online payment and offline bank transfer.**"*

**Talkie's ToS** adds the third channel: subscriptions purchased *"within the Apps… processed by the App marketplace partner."*

That is the whole universe: card, bank transfer, IAP. **No wallet, no A2A, no cash rail, no BNPL, no crypto, no instalments, and no PayPal anywhere on any property.**

### The Vietnam argument is structural, not configurational
This is the distinction that makes the account, so it is worth stating precisely:

- **Stripe's supported-countries page does not mention Vietnam at all** — 0 occurrences, verified by me, while Thailand, Singapore, Indonesia, India, Malaysia, Japan, Brazil, Mexico, Nigeria and Hong Kong all appear.
- Stripe offers **no Vietnamese local payment method** — no MoMo, ZaloPay, VNPay or NAPAS exists on the platform.
- ⚠️ **Precision matters here:** a Singapore-registered merchant *can* accept a Vietnamese card through Stripe. What it cannot do is reach a Vietnamese *local rail*. **The claim is "no local rail is reachable," not "Vietnamese buyers cannot pay."** Do not overstate it in outreach.

**Rails Stripe does support that MiniMax simply has not switched on** (one config away): UPI (India), Pix (Brazil), OXXO (Mexico), PromptPay (Thailand), PayNow + GrabPay (Singapore), konbini + PayPay (Japan), LINE Pay (Taiwan), Klarna/Afterpay.

**Rails no Stripe configuration can reach:** MoMo/ZaloPay/VNPay/NAPAS (VN), KakaoPay/Naver Pay/Toss (KR), QRIS/GoPay/OVO/DANA (ID), SPEI (MX), Mir/SBP (RU), Papara (TR), bKash/Nagad (BD), JazzCash/Easypaisa (PK), Kaspi (KZ), Meeza/Fawry (EG), FPS/Octopus (HK), JKOPay (TW), Rakuten Pay/Paidy (JP), RuPay/netbanking/UPI Autopay (IN).

**Recurring rails: no UPI Autopay, no PayTo.** A subscription business with 10.94% of traffic in India and no UPI Autopay is a strong E3 hypothesis.

### ⚠️ Methodology limits on the absence claim — read before quoting it
- **CSP is worthless as evidence here, in either direction.** Every CSP on every checkout page is `frame-ancestors`-only. **No `form-action` directive exists anywhere** on a checkout surface (the one `form-action 'self'` in the estate is on the vendored Mintlify docs site). Per the standing rule, no rail finding rests on CSP.
- ⚠️ **Bundle absence cannot disprove a rail behind a hosted checkout.** Proven concretely: the bundle scan found **zero** `apple_pay`/`google_pay` hits, yet Stripe's own case study confirms both are live — because the wallet buttons render on Stripe's domain. **So for the ~9 rails Stripe *could* serve, absence is high-confidence but not proven**, and the load-bearing evidence is the merchant's own published two-method statement. **For the ~20 rails Stripe structurally cannot serve, absence is certain regardless of configuration.**

### Rejected false positives — 20+ disproved by context-printing
New traps worth adding to the pipeline list:
| Apparent | Actual |
|---|---|
| **UPI** | `getGroupId`, `X-Group-Id`, `opGroupId` ("Gro·upI·d") **and Ant Design keyframes `antZoomUpIn`/`antSlideUpIn`/`antMoveUpIn`** ("·UpI·n") — new variants of the `classGroupId` trap |
| **IDR, AUD** | **H.264/HEVC NAL unit types** — IDR = Instantaneous Decoder Refresh, AUD = Access Unit Delimiter, beside SPS/PPS/SEI. A new `AUD` trap, distinct from `unaudited` |
| **FPS** (Hong Kong) | React scheduler: *"higher than 125 fps is not supported"* |
| **OVO, EMI** | **Trigram tables in a language-detection library** (Croatian `ovo`, Zulu `emi`) |
| **dLocal** ×28 | `addLocale`, `normalizeLocalePath`, `detectDomainLocale`, `generatedLocaleFilePathFormat` |
| **Momo** | `FieldMomoryTitle` — a misspelling of "Memory" |
| **antom** | the character name *"Crush Ph·antom"* |
| **Yuno** ×3 | a **Black Clover anime character** on Talkie's homepage |
| **Visa** | Swedish for "show" (`"Visa som Markdown"`) |
| **Naver Pay** | `handleHardNavError`; and *"NAVER Whale browser"* in a UA parser |
| **PayPal, Pix, KakaoPay, Octopus, Mastercard, Amex, JCB** | **Font Awesome brand-icon name list** in the vendored docs site |
| **Paytm** | Uzbek `ko'paytmasi` ("multiple of") |
| **phonePe** | `microphonePermissionDenied` |
| **Apple Pay** | `"ApplePayError" in e` inside a **FingerprintJS Safari probe** |
| **stripe** (at Kling/Runway) | CSS `el-table__row--striped`; alt text *"navy side-stripe trousers"* |

**Had `dLocal` been taken at face value it would have produced a fabricated "Talkie uses dLocal for emerging-market local methods" — the exact inversion of the truth.**

## 5. Financials — verified against both first-party releases

| | FY2023 | FY2024 | **FY2025** | **H1 2026** |
|---|---|---|---|---|
| Total revenue | US$3.5M | US$30.5M | **US$79.0M** (+158.9%) | **US$116.6M** (+283.1%) |
| — AI-native (consumer) | | US$21.8M | **US$53.1M (67%)** | **US$42.6M (36.5%)** |
| — Open Platform / enterprise | | US$8.7M | **US$26.0M (33%)** | **US$73.9M (63.4%)** |
| Gross profit | | US$3.7M | US$20.1M | US$20.8M |
| Gross margin | −24.7% | 12.2% | **25.4%** | **17.9%** |
| Adjusted net loss | | US$244.2M | US$250.9M | **US$293.0M** |
| Cash | | US$880M | US$1,050.3M | **US$1,322.8M** |

⭐ **The revenue mix inverted in six months, and it matters more than any other number here.** FY2025 was 67% consumer / 33% platform. H1 2026 is **36.5% consumer / 63.4% platform** (up from 30.3% a year earlier). 

**This kills the obvious objection.** The natural pushback on this account is *"most of the revenue is Apple/Google IAP, so orchestration can't reach it."* That was arguable on the FY2025 mix. It is not arguable now: **the Open Platform carries no IAP at all — it is Stripe plus offline bank transfer — and it is the majority of revenue and the fastest-growing part**, at +703.1% YoY.

**Geography (9M2025, prospectus):** **APAC 61.1%** · Americas 23.7% · EMEA 15.2%. And **73.1% of revenue generated outside Mainland China.** AI-native revenue is allocated by *user billing address*. APAC-majority, cross-border, Singapore-contracted — a clean territory fit.

**Other verified figures:** >200 million users of AI-native products · **>1 million enterprises and developers** (H1 2026; was 214,000 at FY2025) · **token consumption 20× Jan→Jul 2026** · 568 employees · 52-week range HK$186.20–HK$1,330.00, i.e. **down ~79% from peak** at HK$279.

**⚠️ Push back on two numbers you will encounter:**
- *"ARR tops US$800 million"* and *"2 million enterprise customers"* — **neither appears in the first-party release.** H1 2026 revenue annualises to ~US$233M. The company's own figure is *">1 million enterprises and developers."* `[UNVERIFIED — secondary aggregator]` **Do not use either.**
- The **stock code is 0100**, verified twice on the prospectus cover. One research pass reported **2610**; that is **wrong**.

**Prices** (first-party): Hailuo **$14.99** Standard / **$54.99** Pro / **$119.99** Master / **$124.99** Ultra / **$199.99** Max; credits at **1,000 = $1**. Open Platform Token Plan **$22 / $55 / $132**; credit packs **$5 / $25 / $100**, **minimum top-up $5**. Talkie Lab IAP: $9.99/mo, $24.99 Pro, Gems $1.99–$19.99. ⚠️ Docs elsewhere list Token Plan at $20/$50/$120 — a consistent ~10% gap that smells like tax-on-top. **Do not quote a Token Plan price without checking which one the buyer sees.**

## 6. Verified payment failures

**Trustpilot for Hailuo — `trustpilot.com/review/hailuoai.video`, fetched by me: TrustScore 1.4/5 across 94 reviews, 82% one-star.** The complaints are billing, not product:
> *"After using it once, I cancelled my account, but not only did the charges continue, **they showed up twice on the same bill**."* — Kelly Eshpeter, Canada, 3 Mar 2026
> *"Soon as you do they block your account. You can't log in to use it but they continue charging you every month to software you can't access."* — A DB, US, 2 Mar 2026
> *"They charged me on the wrong card and never gave a refund… they kept asking me to remove the card information that never existed on their site."* — SR Vidhya, Canada, 15 Apr 2026
> *"I could not find any way to: **Change my payment method. Manage my subscription.**"* — MT McClanahan, US, 1 Jul 2026

⭐ **GitHub `MiniMax-AI/MiniMax-M2.7#39`** — fetched and verified by me. Author `hansolo0121`, opened **20 May 2026, still open, ZERO comments**. Subscribed 15 May; payment succeeded but **the subscription never activated**; believing it had failed he paid **twice more** — and **switched to a second card**. All three US$50 charges captured. US$100 disputed, US$50 kept.

**The statement descriptor he screenshotted reads "NANONOBLE PTE."** — independently corroborating the billing entity I found in the ToS. Two unrelated sources, same answer.

**Card-switching on retry is exactly what an auth-rate problem looks like from the buyer's side**, and the root cause — authorisation succeeding while provisioning fails — is precisely what a routing layer with proper webhook reconciliation exists to prevent.

**18+ open payment issues across ≥4 MiniMax repos**, clustered May–June 2026, with the newest **22 September 2026 — two days before this report**. Recurring titles: *"Charged twice for Starter to Pro upgrade, but plan did not change"*, *"Pay for credit but did not recieve"*, *"Paid for Token Plan and Never Received it"*, *"Refund Request — Unintended Subscription Renewal"* (×3).

⭐ **Their own UI admits the double-charge problem, twice:**
- `ad_landing_we_could_not_confirm_your_payment_account_an_automatic_refund` = *"We could not confirm your payment account. An automatic refund will be processed. **Do not pay again.**"*
- `ad_landing_unable_to_restore_your_local_photo_retrying_please_do_not` = *"…Retrying. **Please do not pay again.**"*

Plus a large dedicated failure-copy surface: `pay_fail`, `toast_pay_fail`, `subscirbe_fail` *(sic)*, `h5_landing_credit_order_failed`, `h5_landing_subscription_order_failed`, `ad_landing_retry_payment`, `ad_landing_this_payment_session_expired_restore_the_order`.

**And refunds are a hard no**, which is what converts failures into public complaints: *"Unfortunately, refund is not currently supported"*; *"once paid it is non-refundable"*; *"any unused credits worth more than your new plan's cost WON'T BE REFUNDED."*

⭐ **The same failure mode appears at z.ai, in both companies' own error codes.** z.ai returns error 1113 *"Insufficient balance or no resource package"* after a captured payment; MiniMax ships `error_insufficient_balance` = *"Insufficient balance, please recharge to continue."* **This is a vertical-wide pattern, not one company's bug** — and it is the most reusable insight from these three accounts.

⚠️ **Talkie is the exception.** 440 Apple reviews pulled across 11 storefronts; only 11 mention payment and **none is a payment failure** — they are price/ads/value complaints. **Do not claim Talkie payment breakage.**

## 7. Channel dependency — they have already been burned, and they wrote it down

**From the prospectus, verbatim, read by me:**
> *"In December 2024, a prior version of our Talkie app was temporarily removed from Apple's App Store in certain jurisdictions for a period of approximately two months… Apple did not specify the reasons for such removal… the average daily downloads of Talkie app **decreased by approximately 16.8 thousand** compared with its average level prior to such removal."*

**And a standing risk factor specifically about payments:**
> *"**We collaborate with third-party online payment channels for payment collection. Any interruption of their services** or unintended leakage of confidential information may materially and adversely affect our reputation and business… **Any interruption in their payment services could adversely affect our payment collection, and in turn, our revenue.**"*

That is as close to a written admission of the diversification case as a prospectus gets. **It is their language, in a regulatory filing, and it is the single best quote in this file for E2.**

**The cost line is real and named:** platform commission fees of **US$2,360k** on US$26,832k of consumer revenue (9M2025) = **8.8% blended**. Cost of sales fell 124.7% → 87.8% → 76.7% of revenue, and gross margin is explicitly management's headline metric. In a business where a point of gross margin is a board-level talking point, an 8.8% channel-commission line is addressable.

## 8. IAP exposure — quantified, and smaller than it looks

| Property | Web checkout? | Channel | Entity |
|---|---|---|---|
| **Open Platform** | ✅ Yes | **Stripe + offline bank transfer.** No IAP at all | Nanonoble |
| **Hailuo AI** (video/audio) | ✅ Yes | **Stripe → Airwallex fallback** | Nanonoble |
| **Talkie** | ⚠️ Login-gated only | **IAP-primary**, with a `WebStripe` lane; **no public pricing page** — `/subscribe`, `/pricing`, `/plans` etc. all 404 | SUBSUP |

**Two independent routes agree on the IAP share.** Solving the commission line against standard rates gives **18–44% of consumer revenue on IAP**; and Talkie (~100% IAP) is **28.2%** of consumer revenue, which × 30% implies **8.45%** commission against the observed **8.8%**. Both land in the same place.

**So: ~70–80% of the consumer book runs on Stripe/Airwallex, and 100% of the Open Platform book does.** Against the H1 2026 mix, **roughly 85% of total revenue sits on web rails orchestration can address.**

⚠️ Caveat: the prospectus makes no principal-vs-agent disclosure for IAP (I searched — zero hits), so this rests on IAP being booked gross with commission in cost of sales. Their explicit statement that channel commissions *are* in cost of sales supports it but does not prove it for every channel.

## 9. Aggregator leakage — real but far milder than z.ai

- **8 `minimax/*` models on OpenRouter** (vs z-ai 19, deepseek 16, moonshotai 8) across a 458-model catalogue.
- **40 endpoints total; 11 MiniMax's own, 29 third-party across 16 providers.**
- On **`minimax-m3`, the flagship: 13 endpoints and MiniMax's own ranks #10 of 13** — undercut by CoreWeave $0.23/M, GMICloud $0.24/M and DeepInfra $0.28/M against MiniMax's $0.30/M. **Mid-list on the model it most wants volume on.**
- But on `minimax-m2` and `minimax-m1` MiniMax is **cheapest**, and `minimax-m2-her` and `minimax-01` are **exclusive to it**. That is materially better than z.ai's position.
- **Weights are open and ungated** — 21 `MiniMaxAI/*` HuggingFace repos, `gated: None`. That is why third parties can serve them.
- **On aggregator-routed spend, OpenRouter is merchant of record**, per its own terms.
- **A protective clause exists**: ToS §7(c) bars sublicensing/reselling/distributing the services. ⚠️ **But open weights route around it entirely**, since third parties serve from HuggingFace rather than reselling MiniMax's service.

**Consequence: unlike z.ai, the API book is defensible enough to pitch — but the subscription book is still the better target.**

## 10. Competitive set — nobody has solved this, and nobody has an orchestrator

**AI video (Hailuo's set):** Kling (Kuaishou), Vidu (Shengshu), Luma, Pika, Runway, PixVerse.
**AI companion (Talkie's set):** Character.AI, Replika, Chai, PolyBuzz, Janitor AI.

**Every single one bills IAP on mobile and single-rail Stripe on web. Not one uses an orchestrator. Not one accepts a single local payment method.**

⭐ **Vidu is the cleanest artefact in the whole comparison** — a hard regional binary with no third branch:
```js
channels: "global" === w.SITE ? ["stripe"] : ["alipay"]
```
Kling: `STRIPE_MANAGE_URL` with `theme:"stripe-tax"` gated on `region !== CN`. The only MoR-ish layer anywhere in either set is **RevenueCat at Character.AI**, which is IAP subscription infrastructure — not an orchestrator, and it does not touch web card acquiring.

**No orchestration adoption anywhere in these verticals**, and **no cross-border acquiring case study naming a China-origin consumer app** at Airwallex, PingPong, PayerMax or Antom — all four checked. What came back was vendor capability marketing, including one Airwallex example that turned out to be **fictional** (`SaaSOS`/`BizCo` in its own docs).

⚠️ **This cuts both ways, and the honest reading is the second one.** It means no competitor has claimed the category — and it means **Yuno has no social proof here at all.** E4 needs a Tier-2 payment-pattern match, not a vertical match. And the structural reason nobody has sold orchestration into AI-native consumer apps is that IAP owns a large share of that revenue. **That is a real objection to prepare for, not merely absent evidence** — the counter is §8, that MiniMax's mix has shifted to 63.4% Open Platform.

## 11. Verification ledger

**Verified first-hand by me, this session:**
- All six sanctions/export-control regimes, each with a sanity-checked grep; all 6 "Xiyu" hits context-printed and disproved
- Domain resolution: `minimaxi.com` → `minimax.cn`, `hailuo.ai` → `agent.minimax.cn`
- **HKEX prospectus** (716 pages, downloaded and text-extracted): stock code **0100** twice on the cover, issuer name, Cayman/WVR, HK$165 max offer price, *"2 major subsidiaries"* quote, **1,771,600 paying users**, platform commission fees, the **payment-channels risk factor** verbatim, the **Talkie removal + 16.8 thousand downloads** passage
- **Both first-party financial releases** (H1 2026 and FY2025) — every revenue, margin, mix and cash figure in §5
- Platform ToS and privacy policy: Nanonoble entity + address, Singapore law, SIAC, *"all payments are in USD"*, the 1%/day late fee, Stripe as invoice-data source
- The i18n dictionary (661 pairs): auto-renew method, failure states, waterfall, vouchers, `$`-baked price template, Autobilling
- **`showWechatPayIcon` false vs true** on both builds, same config block
- **Airwallex live in the current `prod-en-0.1.869` build** — 35 hits across 4 chunks, real SDK loader, and I read the Stripe/Alipay/Airwallex routing branch myself
- Merchant's published two-method statement, in both the docs and the homepage JSON-LD
- **Talkie Lab seller = SUBSUP PTE. LTD.** across 5 storefronts; **old "Talkie: Soulful AI" (6450140383) gone** — resultCount 0 in 6 storefronts, page 404
- ⭐ **Talkie absent from the India and Taiwan App Stores**, present in 15 others, **with a WhatsApp control proving the India query works**
- **Stripe's case study** — products used, Link at 40% of pay-in volume, Adaptive Pricing on 89% of transactions, Linda Sheng quoted
- **Trustpilot 1.4/5, 94 reviews, 82% 1-star**, five billing reviews verbatim
- **GitHub M2.7#39** — title, author, date, open state, zero comments, the three charges, the NANONOBLE descriptor
- Stripe's supported-countries page: **Vietnam 0 occurrences**
- ⭐ **The live unauthenticated config endpoint**, called by me: `backend_payment_migration_percent` → `{"percent":100,...}`; `price_pre_credit` → the USD 5 / CNY 36 pair and the 9,995,000-credit ceiling; `code_plan_detail` → the Team Token Plan withdrawal notice verbatim; `media_plan_faq` → the 31-day / 1-year / 3-day credit expiry regimes

**NOT verified by me:**
- The 9M2025 revenue-by-line table and the APAC 61.1% / 73.1%-outside-China splits (agent-read from the prospectus; I verified the prospectus is genuine and several other passages in it, but not these tables)
- ACRA/BizFile UEN numbers, directors or filed accounts for Nanonoble or SUBSUP (registry mirrors blocked/timed out; prospectus particulars used instead)
- IPO debut-day figures (HK$4.8bn raised, +109% first day) — search summaries
- Market cap, share count and the 52-week range (stockanalysis.com, not the filing)
- The four-codebase channel enum and the `agent.minimax.io` Stripe/Alipay ternary (agent bundle-mining; I independently verified the equivalent routing in the Hailuo build)
- Competitor stacks for Kling, Vidu, Luma, Character.AI etc. (agent bundle-mining, methodology sound, not re-run)
- OpenRouter endpoint counts and per-model price rankings
- The CEO's Southeast Asia pivot statements — secondary Chinese/Korean press
- Disney/Hollywood copyright suit and the Anthropic distillation accusation — **secondary only, and both are live reputational matters; do not raise either in outreach**
- Google Play listings — every bundle ID tried 404'd
- The 507-file bundle sweep behind the channel enum, the endpoint surface list, and the `/inner/payment` vs `/backend/payment` routing code (agent-mined; I verified the migration endpoint it pointed at, and read the Hailuo Stripe/Alipay/Airwallex branch myself)
- PCI DSS status — **no public information found** on any property. Hosted-redirect architecture implies SAQ A / A-EP scope `[INFERENCE, not confirmed]`
- **ARR "surpassed US$800M" in August 2026** — secondary only, and it contradicts the first-party H1 2026 figure annualising to ~US$233M. ⚠️ **Do not use it.**

**Known contradictions I resolved:**
- **Stock code 0100, not 2610** — prospectus cover, twice.
- **The FY2025 "67% consumer" and H1 2026 "63.4% platform" figures are not contradictory** — they are different periods, and the mix genuinely inverted. Both verified against their own releases.
- **I told Prateek mid-run that Stripe was the only rail. That was wrong** — Airwallex is live in production. Corrected here and to him directly.

## 12. Next actions

1. **Run `/full-outreach minimax.io`.** Nothing blocks it.
2. **Ask Prateek for `talkie-ai.com` and `hailuoai.com` traffic.** The supplied export covers only the `.io` estate; the consumer apps are the likelier home of high-count volume and are invisible here.
3. **Add to the TAL at P1** — MiniMax is not currently on it.
4. **TAL additions from the competitive sweep:** Kling/Kuaishou **P1** (existing Kuaishou row has no priority set), Vidu **raise P3 → P2** (the hardcoded `global→stripe : alipay` binary is the most explicit single-rail evidence found anywhere), PixVerse **P3**, Character.AI **P2** (US-HQ, so the clean comparable with no export-control question). ⚠️ **All but Character.AI are China-HQ — run the Entity List check before outreach, not after.**
5. **Resolve the Token Plan price** ($20/$50/$120 vs $22/$55/$132) before any number goes in an email.
6. **Consider whether the 15 zeroed countries** in the traffic data are a geo-block or a measurement artefact. Not usable until known.

## 13. Methodology notes for the pipeline

- ⭐ **New false positives:** `Xiyuan`/`Xiyue` (street names) → Xiyu · `antZoomUpIn`/`antSlideUpIn`/`antMoveUpIn` and `getGroupId`/`X-Group-Id` → UPI · **H.264 `IDR`/`AUD` NAL unit types** → IDR/AUD · `forceFrameRate…fps` → FPS · Croatian `ovo` / Zulu `emi` in a trigram table → OVO/EMI · `addLocale`/`normalizeLocalePath` → dLocal · `FieldMomoryTitle` → MoMo · *"Crush Phantom"* → Antom · **a Black Clover character named Yuno** · Swedish `Visa` ("show") · `ko'paytmasi` → Paytm · `microphonePermissionDenied` → PhonePe · Font Awesome's `cc-*` brand-icon list → half a dozen rails at once.
- ⭐ **A silently truncated download looks exactly like a clean negative.** My first BIS Denied Persons fetch came back at 30KB instead of 150KB and the grep returned zero — which is indistinguishable from "not listed" unless the sanity check is run. **Always validate the grep against a known positive in the same file.**
- ⭐ **Bundle absence cannot disprove a rail behind a hosted checkout.** Demonstrated here: zero `apple_pay` hits in 88 chunks, while Stripe's case study confirms Apple Pay is live. Wallet buttons render on the PSP's domain.
- ⭐ **A 403 from one tool is not a network verdict.** `curl` to github.com and Trustpilot both 403 in this environment; **`WebFetch` reaches both.** I recorded a z.ai finding as unverifiable on the strength of the curl failure alone and had to go back and correct it.
- **Frontend build hashes roll mid-session.** An agent's chunk URL 404'd ~20 minutes later on the same build version. Re-enumerate chunks from the page rather than reusing a hash.
- **CSP `form-action` rule applied again:** no checkout surface in this estate carries `form-action`, so CSP evidenced nothing and none was used.
- **Naive substring grep on the TAL is dangerous:** `chai` matches 55 rows, all noise (`chain`, `blockchain`, `chairs`); `vidu` matches 6, of which 1 is real (`individual`). Use word boundaries.

</details>
