# Simple.life

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 19 / 29 → ⭐ **High Priority** on the matrix — ⚠️ **but see the analyst override. This is not an APAC account.**
**Industry:** AI intermittent-fasting / weight-loss consumer subscription app · **HQ:** **Simple.Life Apps Inc**, Delaware (reg. **7688095**), Dover DE; subsidiary **AM APPS Ltd**, Cyprus (**ΗΕ 392517**); **SIMPLE.LIFE APPS UK LTD**, London (**13409801**). Parent **Palta** · **Researched:** 2026-10-06 · **First email sent:** —
**Motion:** 🔴 **COMPETITIVE — Primer is the live, incumbent orchestrator. Verified first-hand.**

---

> ## ⛔ READ FIRST — three things that decide this account
>
> **1. Primer already owns the seat.** I pulled their live production config myself:
> `https://configs.cdn-simple-life.com/content-api/feature_flags.json` — **HTTP 200, 2,170 bytes, publicly served, unauthenticated:**
>
> ```json
> "paymentGateway": "primer",
> "accountPageDelay": { "palta": 8000, "primer": 8000, "stripe": 8000 },
> "dLocal": { "br": true, "mx": false },
> "creditCard": true, "applePayStripe": true, "googlePay": false, "paypal": true, "paywall": true
> ```
>
> **Primer is a direct Yuno competitor and it is the live gateway.** Per `/full-outreach` Step 6a this is the **Competitive** motion — explicitly the hardest, and the rule is to proceed *only* on a concrete gap, otherwise flag rather than send a weak sequence. **CLAUDE.md also forbids naming Primer in any outreach.**
>
> **2. The buying centre is Palta's London payments team, not Simple, and not APAC.** Primer publishes a case study featuring **Gianluca Cassaro, VP of Payments at Palta** and **Elaine Nguyen, Global Payments Operations Lead** — I fetched it (HTTP 200, 217,450 bytes; **21 Palta mentions, 96 Primer, 29 Flo, 4 Zing, 3 "3DS", 8 "Fallback", 6 "tokeniz", 2 "chargeback"**). Palta runs payments **centrally** across Flo, Simple, Zing and Lovi, with **Adaptive 3DS, Fallbacks and Network Tokenization already live.** Cassaro came from ~7 years of payments at Badoo and Bumble `[UNVERIFIED — summary only]`.
>
> **3. APAC is 3.52% of traffic and the currency list proves the commitment stops at Japan + ANZ.** I enumerated `common.currencies_short` from their live i18n bundle — **18 currencies:**
> `AED ARS AUD BRL CAD CHF CLP COP DKK EUR GBP JPY MXN NOK NZD SEK TRY USD`
> **APAC present: JPY, AUD, NZD. APAC absent: INR, SGD, MYR, THB, IDR, PHP, VND, KRW, CNY, HKD, TWD — every one.** Also absent: **ZAR**, despite South Africa being their fastest-growing market (▲98.51%).

---

> ## ⭐ THE REAL GAP — APAC is the ONLY unserved region in a stack that demonstrably buys local rails
>
> ⚠️ **I published an earlier draft of this file claiming Brazil had no Pix. That was wrong and I corrected it.** The error is worth recording because it is instructive: I grepped the i18n bundles, found no Pix, and under-weighted my own caveat that **Primer renders its method list client-side from its own dashboard, not from the merchant's strings.** The paywall bundle settles it.
>
> **Verified first-hand in `PaywallView` / `StripeKlarna-07MMwSRC-B-k2goFs.js`:**
> ```js
> e.DLOCAL_PIX="pix"   e.DLOCAL_PIX_AUTOMATICO="pix"   e.PIX="pix"
> e.ADYEN_IDEAL="ideal"   e.KLARNA="klarna"   e.AFFIRM="affirm"
> e.FLEX_CARD="flex_card"   e.VAULT="vault"   e.PAYPAL_BILLING_AGREEMENT="paypal"
> tabsOrder: ["paymentRequest","google","ideal","paypal","card","pix"]
> IS_PIX_PAYMENT_METHOD_FOR_BR_EXP
> ```
>
> **So Brazil is WELL served: dLocal local acquiring, Pix, AND `DLOCAL_PIX_AUTOMATICO` — recurring Pix.** The Netherlands gets **Adyen iDEAL**. They invest in local rails, properly, when a market matters to them.
>
> **And they split it correctly by transaction type** — subscriptions take recurring Pix, one-off purchases take plain Pix:
> ```js
> pix_automatico: IS_PIX_PAYMENT_METHOD_FOR_BR_EXP && this.isSubscriptionAction ? 1 : 0,
> pix:            IS_PIX_PAYMENT_METHOD_FOR_BR_EXP && !this.isSubscriptionAction ? 1 : 0
> ```
> That is a considered implementation, not a checkbox integration.
>
> ⚠️ **One precision point for outreach: Pix is gated behind a live A/B experiment, `web_pix_payment_method_for_br`** — it sits in the same experiment registry as their pricing and paywall tests. The capability is unambiguously built and shipped; **what share of Brazilian traffic is in the treatment group cannot be determined from outside.** Safe phrasing: *"you're running Pix and Pix Automático through dLocal in Brazil."* **Do NOT say "all your Brazilian customers can pay by Pix."**
>
> Note also the in-bundle default is `dLocal:{br:!1,mx:!1}` — **the live CDN config is what switches Brazil on.**
>
> ### And they have done nothing at all for APAC
>
> Grepped explicitly across every bundle: **zero hits for konbini, PayPay, LINE Pay, Rakuten Pay, Paidy, carrier billing, JCB, PayTo, BPAY, Afterpay, Zip, UPI, QRIS, PayNow, PromptPay, GCash, Alipay, WeChat Pay.** Their entire local-method investment is **Brazil and the Netherlands.**
>
> **That is the wedge, and it is much stronger than the Brazil one I originally wrote.** The argument is no longer "you are neglecting local payments" — it is *"you proved in Brazil that you will build local rails, down to recurring Pix. Japan is your fastest-growing market and your most engaged audience, and it has none."* They cannot answer that with "we don't do local methods," because they demonstrably do.
>
> **Supporting: the currency map draws the same line.** 18 currencies — `AED ARS AUD BRL CAD CHF CLP COP DKK EUR GBP JPY MXN NOK NZD SEK TRY USD`. **APAC present: JPY, AUD, NZD. Absent: INR, SGD, MYR, THB, IDR, PHP, VND, KRW, CNY, HKD, TWD.** Also absent: **ZAR**, despite South Africa growing ▲98.51%.

---

> ## 🔑 THE BUYING SIGNAL — they are A/B-testing their way OFF their orchestrator
>
> Three live experiment flags in production code, verified first-hand in `useStandaloneStepEvents-BFmWjaA4.js`:
> ```js
> IS_STRIPE_DIRECT_INTEGRATION_EXP   → t("web_stripe_direct_integration")
> IS_PRIMER_PAYPAL_VS_NATIVE         → t("web_primer_paypal_vs_native")
> IS_AP_GP_VIA_DLOCAL_IN_BRAZIL_EXP  → t("web_ap_gp_via_dlocal_in_brazil")
> ```
>
> **They are measuring direct Stripe against Primer-routed Stripe, and native PayPal against Primer-routed PayPal, in production, right now.** `paypalService.js` confirms the native path is real — it loads `https://www.paypal.com/sdk/js` directly.
>
> **Someone at Palta is not fully convinced by the incumbent, and they are gathering evidence.** That is the single most commercially interesting fact on this account, and it is evidenced rather than projected. It is also the only honest reason to approach a Competitive account like this one.

---

> ## 🎯 THE JAPAN ASYMMETRY — and a correction to our own September file
>
> **The September `not-icp` file said Simple has "zero APAC languages." That was wrong, and I nearly repeated it.**
>
> The funnel bootstrap at `simple.life/survey/` carries **15 locales**, verbatim:
> ```js
> availableLanguages = ["en","es","pt","de","it","fr","sv","es-419","pl","tr","nl","da","nb","ja","ar"]
> ```
> **`ja` is there.** The Japanese bundle is **270,591 bytes — the largest of the three — fully translated**, with the same 2,720-leaf key set as English. I confirmed Japanese renders on the legal pages too: `simple.life/tos/ja` is HTTP 200 with **247 lines carrying Japanese UTF-8 lead bytes**, against **zero** in `tos/en`. Sample text: 「プライバシーポリシー」「サブスクリプション」(×52) 「返金」(×15) 「支払」(×11).
>
> ⚠️ **Methodology note worth keeping:** my first check reported **zero** Japanese characters. That was a false negative — **`grep -P` is unavailable in this environment and failed silently with an unsupported-escape error.** The raw-byte check caught it. **A silently-failing grep looks identical to a clean negative.**
>
> ### So the real asymmetry is sharper and more specific than "they ignored Japan"
>
> | Layer | Japanese? |
> |---|---|
> | Marketing / funnel UI | ✅ fully translated |
> | Checkout UI | ✅ 「クレジットカード」 |
> | JPY local pricing | ✅ ¥ |
> | Terms of Use + Privacy Policy | ✅ `tos/ja`, `privacy/ja` both HTTP 200 |
> | **Subscription Terms** (billing, auto-renewal, cancellation) | ❌ **`/subscription-terms/ja` → 404** |
> | **Refund policy** | ❌ **`/refund/ja` → 404** |
> | **Japanese payment rails** | ❌ **none — zero konbini, PayPay, LINE Pay, Rakuten Pay, Paidy, carrier billing, JCB** |
> | **Japanese help centre** | ❌ **English only** (help-centre `hreflang`: de, en, es, fr, it, pt-BR, sv, tr — **no ja**) |
>
> **Simple has already paid the expensive part of entering Japan — full UI translation and JPY pricing — and stopped at the cheap part.** They ask a Japanese customer to pay by credit card, in a market where konbini and carrier billing are default expectations for digital subscriptions, then give them **English-only support and an English-only refund policy** when it fails.
>
> **The internal investment case for Japan is already made. The rails just were not finished.** That is a far better conversation than "you ignored Japan" — and unlike the original framing, it is true.
>
> ### The same gap hits Brazil harder
> **`/subscription-terms/pt` → 404 as well.** The page explaining billing, auto-renewal, cancellation and refunds exists only in **de/en/es/fr/it**. **Their #2 market (24.07%) and their #3 market (2.75%) cannot read their billing terms in their own language**, despite both having fully translated Terms of Use and Privacy Policy. That is a gap in the *commercial* layer specifically, and it is first-party verifiable.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** AI-driven intermittent-fasting and weight-loss subscription app, founded 2019, CEO **Mike Prytkov**. Sold through a quiz funnel (`simple.life/survey/`) that terminates at a web paywall, plus App Store and Google Play. **~1,000,000 subscribers (Sep 2026), $160M ARR (2025), 21M+ downloads.** Part of **Palta**, a consumer-health app group (Flo, Simple, Zing, Lovi, Prisma Labs) that runs payments centrally.

**SimilarWeb (supplied 2026-10-06, Jul–Sep 2026, all country domains ON, 93 countries):** US 45.69% ▼27.51% · Brazil 24.07% ▼43.08% · **Japan 2.75% ▲38.48%** · Uruguay 2.25% · France 2.18% · Canada 1.83% · UK 1.73% · Türkiye 1.26% · Spain 1.09% · Italy 1.08% · **Australia 0.77% ▲16.81%**. Full table and the Jun–Aug comparison in `accounts/traffic/simple-life.md`.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|---|---|---|---|---|---|
| 1 | 🇺🇸 United States | 45.69% | Card, PayPal, Apple Pay (via Stripe), **FSA/HSA cards**, Klarna (lifetime plan only) | Google Pay (**built, flag=false**), ACH | ✅ Simple.Life Apps Inc (DE) |
| 2 | 🇧🇷 **Brazil** | **24.07%** | Card (BRL, R$), **dLocal local acquiring**, **Pix**, **Pix Automático (recurring)**, CPF/CNPJ capture | boleto · native parcelamento — **well served overall** | ❌ none found |
| 3 | 🇯🇵 **Japan** | **2.75%** | Card only (JPY, ¥) | **konbini · PayPay · LINE Pay · Rakuten Pay · Paidy · carrier billing · JCB** | ❌ none found |
| 4 | 🇺🇾 Uruguay | 2.25% | Card | No UYU currency; no local rails | ❌ none |
| 5 | 🇫🇷 France | 2.18% | Card, PayPal, Apple Pay | SEPA Direct Debit, Cartes Bancaires | ⚠️ AM APPS Ltd (Cyprus) / UK Ltd — EU-adjacent |

🇦🇺 **Australia (0.77%, ▲16.81%):** card + AUD (A$) confirmed. **PayTo, BPAY, Afterpay, Zip all NOT FOUND.**

### Legal entities
- **Simple.Life Apps Inc** (USA — Delaware) — reg. **7688095**, 8 The Green Ste A, Dover, DE 19901
- **AM APPS Ltd** (Cyprus) — reg. **ΗΕ 392517**, Limassol
- **SIMPLE.LIFE APPS UK LTD** (United Kingdom) — Companies House **13409801**, incorporated 20 May 2021, London
- Parent: **Palta** — HQ unresolved (London / Vilnius / Cyprus / New York all cited by different sources)

### Known PSPs
- **Primer** — `[Source Code]` live `paymentGateway: "primer"` in production feature flags — **orchestrator, group-wide**
- **Stripe** — `[Source Code]` `applePayStripe: true`, third gateway code path · `[Terms/Privacy Policy]` named in privacy policy
- **dLocal** — `[Source Code]` `dLocal.br: true`, `dLocal.mx: false` — **Brazil local acquiring ON, Mexico explicitly OFF**
- **PayPal** — `[Source Code]` `paypal: true` · `[Terms/Privacy Policy]`
- **"palta"** — `[Source Code]` a third gateway code path, i.e. a group in-house layer
- **Braintree** — `[Source Code]` live key `production_24r2g38n_...`; **legacy and feature-degraded** (*"Braintree does not support pausing subscription"*)
- **Adyen** — `[Source Code]` `ADYEN_IDEAL` — a **connector inside Primer**, serving iDEAL
- **"flex" / `flex_card`** — `[Source Code]` a seventh provider with its own `flexService.js`, routed through `primerApi`. ⚠️ **Could not identify what Flex is — the one genuine unknown in the stack**
- **`stripe_legacy`** — `[Source Code]` a separate legacy Stripe integration, distinct from `stripe`
- **Checkout.com** — `[Terms/Privacy Policy]` named as an example in the privacy policy, **not seen anywhere in code**

### Orchestration status
🔴 **Global orchestrator incumbent — Primer.** Verified first-hand in live production config, and corroborated by Primer's own case study naming Palta's VP of Payments. **Three gateway code paths are maintained simultaneously (`palta`, `primer`, `stripe`), which suggests a migration or an A/B in progress.**

### Buying signals
- 💰 **$35M Series B** led by **HartBeat Ventures** (Kevin Hart's VC), Liquidity Capital participating, ~Oct 2025 — earmarked for the AI coach "Avo" `[UNVERIFIED — summary only]`
- 🚀 **1,000,000 subscribers** announced **29 Sep 2026** — [simple.life/blog/one-million-subscribers](https://simple.life/blog/one-million-subscribers)
- 💼 **Palta runs a group payments function** — VP of Payments + Global Payments Operations Lead
- 📋 **Palta job posting:** *"in-house monetization platform for web payments with subscription capabilities, with annual turnover in the tens of millions of USD and aims to grow"* ⚠️ **`[UNVERIFIED]` — the Greenhouse page now 404s, role delisted. Could not be confirmed against the primary page.**
- 🤝 **Primer roadmap already in motion** — 2024 fallback implementation to *"recover failed transactions and boost revenue"*

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

> **🛑 NOT GENERATED — deliberately, and it should not be generated without a decision from Prateek.**
>
> Two independent blockers:
> 1. **Motion is Competitive.** `/full-outreach` Step 6a: *"**Competitive** (a global orchestrator is incumbent): hardest. Only proceed if research surfaced a concrete gap. Otherwise flag to Prateek rather than sending a weak sequence."* Concrete gaps **do** exist (Brazil recurring rails, Japan rails, `googlePay: false`, no mandate rail anywhere) — but the incumbent has Adaptive 3DS, fallbacks and network tokenization already live.
> 2. **Out of territory, and the buying centre is wrong.** See the override below.
>
> If it ever is drafted: **never name Primer** (CLAUDE.md forbids naming Yuno competitors), and the angle is **coverage and reach**, not the case for orchestration — they are already orchestration-aware and will not sit through an education pitch.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 19 / 29

| Signal | Points | Status |
|---|---|---|
| **Monthly transaction count** | **3** | ✅ **DERIVED: ~83,000/month floor.** 1,000,000 subscribers **[SOURCED**, simple.life/blog/one-million-subscribers, 29 Sep 2026**]** × 1 charge/year ÷ 12 = 83,333. That is the **most conservative case the sourced input permits** (every subscriber billed annually); a realistic 1/3/6/12-month mix lands in the hundreds of thousands. Banded on the conservative floor → 50,000–99,999 = **+3**. ⚠️ **This is TOTAL billing events. The addressable share depends on the undisclosed web-vs-IAP split — see Section 12.** |
| Orchestration status | **1** | 🔴 **Global orchestrator incumbent (Primer)** — verified in live production config |
| 3+ countries | **3** | ✅ 93 countries in the traffic data; **18 currencies**; 15 funnel locales |
| Multiple PSPs | **3** | ✅ **Primer + Stripe + dLocal + PayPal + a "palta" in-house path** — five, verified in one config file |
| Local rail or licensing gap in a top-3 market | **3** | ✅ **Fires on Japan (#3, 2.75%): ZERO Japanese rails** — no konbini, PayPay, LINE Pay, Rakuten Pay, Paidy, carrier billing or JCB, confirmed across every bundle. ⚠️ **Does NOT fire on Brazil — Brazil is well served** (dLocal, Pix, Pix Automático, CPF). Corrected from an earlier draft of this file |
| Recent expansion | **0** | ⬜ **No new market launch or localisation announcement found.** The Series B is funding, not expansion |
| Payment issues reported | **2** | ✅ Trustpilot **4.3/5 across 46,412 reviews, ~11% at 1–2★ ≈ ~5,100 negative**, rating down from 4.5; billing-after-cancel complaints; **their own decline-recovery UI tells users to phone their issuer and ask it to unblock "Simple.Life Apps Inc."** |
| Funding >$10M | **2** | ✅ **$35M Series B**, HartBeat Ventures, ~Oct 2025 `[UNVERIFIED — summary only]` |
| High traffic outside home | **2** | ✅ US is **45.69%**, below the 60% threshold |
| Competitor using orchestration | **0** | ⬜ **No competitor found on any orchestrator.** Noom consolidated onto **Stripe**; BetterMe, Yazio, Zoe, WW — nothing found. **The orchestration layer is genuinely unclaimed in this vertical** |
| Payment job postings | **0** | ⬜ The Palta "in-house monetization platform" posting **404s and could not be verified**. Flo's Senior PM Payments role is **Flo, not Simple** |

**Tier:** ⭐ **High Priority (17+)** on the raw matrix.

### 🛑 ANALYST OVERRIDE — downgrade for APAC. Route to EMEA/AMER.

**The 19 is arithmetically correct and commercially misleading for this territory.** Three reasons, in order of weight:

1. **The buying centre is not in APAC.** Payments is run centrally by **Palta's group payments function** — VP of Payments and a Global Payments Operations Lead, operating out of London/Europe. A Primer displacement conversation is run by that team. **There is no APAC payments decision-maker to call.**
2. **No APAC entity, no APAC HQ, no APAC presence.** Delaware, Cyprus, London. The `/research` Phase 0 territory gate rejected this account on 2026-09-30 for exactly this reason. **Prateek explicitly overrode that gate on 2026-10-06** (*"I know it's a Europe Based but I'm working on this account exception"*) and the run proceeded on his instruction — **the override is recorded, and this override does not reverse it.** But the territory facts have not changed, and the currency list independently confirms the commitment stops at JPY/AUD/NZD.
3. **APAC is 3.52% of traffic** (Japan 2.75% + Australia 0.77%). Even winning the whole APAC rail gap moves a small fraction of their volume. **The real money is Brazil at 24.07%, which is AMER.**

**What the override does NOT say:** this is not a weak account. It is a **genuinely strong Yuno prospect for whoever owns EMEA/AMER** — $160M ARR, 1M subscribers, five payment providers, no mandate rail anywhere, a live Brazil local-acquiring deployment through dLocal, and a sibling portfolio (Flo at a reported 7M paid subscribers) on the same group stack. **Route it; do not drop it.**

⚠️ **One correction to the framing in the request:** Simple.life is **not Europe-based**. The controller is a **Delaware corporation**; Cyprus and the UK are subsidiaries. Palta's own HQ is variously reported as London, Vilnius, Cyprus and New York — **genuinely unresolved.**

### Source Notes
- ✅ **Verified first-hand by me:** `feature_flags.json` (HTTP 200, 2,170 b) — `paymentGateway: "primer"`, `dLocal.br/mx`, `googlePay: false`, `applePayStripe`, `paypal`, three gateway paths · the Primer case study (HTTP 200, 217,450 b, 21 Palta / 96 Primer mentions) · all three i18n bundles and the 18-currency list · the 15-locale `availableLanguages` array · `tos/ja` and `privacy/ja` serving real Japanese (247 / 165 lines of CJK lead bytes vs 0 in `tos/en`) · `subscription-terms/ja`, `subscription-terms/pt`, `refund/ja` all **404** · the `pix` → "tracking pixel" false positive · the Subscription Terms billing-descriptor passage
- ⚠️ **Agent-fetched, NOT re-verified by me:** Trustpilot 4.3/46,412 — **my own re-fetch returned HTTP 403**
- ⚠️ `[UNVERIFIED — search summary only]`: the $35M Series B · $100M FY2024 revenue · the Palta job-posting quote (page 404s) · Pix Automático's June 2025 launch · Noom's Stripe +8% claim · Palta's $124M total funding

### Success Case Alternatives
- **A subscription business that added local recurring rails in LATAM** — closest profile match: Brazil-heavy, card-only renewals, involuntary churn. ⚠️ **Do not cite a Yuno customer without a published metric** (standing rule).
- **Avoid** citing Noom's Stripe case study as proof — it argues for *consolidation onto one PSP*, which is the opposite of the orchestration case.

---

## Section 1: Website Traffic Analysis by Country

**Data source:** SimilarWeb, **supplied by Prateek 2026-10-06** (Jul–Sep 2026, "include all country domains" ON, `simple.life` + 11 domains, 93 countries). **Total visits were not shown in either snapshot, so no absolute visit volume can be derived.** Full table and the superseded Jun–Aug snapshot in `accounts/traffic/simple-life.md`.

**The most important traffic finding is the reversal.** In Jun–Aug the core was growing hard (US ▲36.13%, Brazil ▲71.14%, France ▲203.52%, Spain ▲161.27%). In Jul–Sep **all of them are falling** (US ▼27.51%, Brazil ▼43.08%, France ▼43.78%, Spain ▼54.32%).

**Most likely cause: seasonality, not contraction.** Evidence against a decline story, and it is strong:
- **$35M Series B closed ~Oct 2025** — funded, not starved.
- **Operating profitable**, $100M FY2024 revenue, +64% YoY `[UNVERIFIED]`; **$160M ARR in 2025.**
- **The 1M-subscriber milestone was published 29 Sep 2026 — inside the declining quarter**, and framed as growth. A company shedding subscribers does not publish that.
- **No layoffs, funding trouble, pivot or shutdown signal found** for Simple or Palta.
- Diet apps peak in January and trough in the northern autumn. Category decay is documented: **MyFitnessPal 195K → 108K weekly downloads (Jan → Mar)**; **Fastic ~80K → ~24K** `[UNVERIFIED]`. Jul–Sep is the trough.

⚠️ **What seasonality does NOT explain: Brazil at ▼43.08%.** Brazil's summer is Dec–Mar, so pre-summer diet demand there should be *building* in Sep–Oct, not collapsing — and the magnitude is far steeper than the US. **No sourced explanation found.** Unconfirmed hypotheses: a paid-acquisition pullback, an FX/pricing change, or a localisation/payment problem at the Brazilian checkout. **The last would be a direct Yuno hook, and there is zero evidence for it — it must not be asserted.**

**Category headwind that is real:** GLP-1 drugs are reshaping this vertical. **Noom confirmed layoffs** tied to *"a revenue mix shift… towards our fast-growing GLP-1-related products"* `[UNVERIFIED]`. Simple is responding by positioning as a **behavioural companion to GLP-1 medication** and has added GLP-1 tracking. That reads as adaptation, not decline.

## Section 2: Legal Entities & Local Presence

**Headquarters:** Delaware incorporation; operations distributed. Founded 2019. **180 employees across 27 countries** `[UNVERIFIED]`.

| Country | Entity | Registration # | Source |
|---|---|---|---|
| 🇺🇸 USA | Simple.Life Apps Inc | **7688095** | `simple.life/privacy/` (fetched) |
| 🇨🇾 Cyprus | AM APPS Ltd | **ΗΕ 392517** | `simple.life/privacy/` (fetched) |
| 🇬🇧 UK | SIMPLE.LIFE APPS UK LTD | **13409801** | Companies House (fetched, prior run) |

**Cross-border gap analysis**

| Country | Top 10 traffic? | Local entity? | Domestic acquiring gated? | Cross-border risk |
|---|---|---|---|---|
| 🇺🇸 United States | ✅ #1 | ✅ Delaware | No | Low |
| 🇧🇷 **Brazil** | ✅ **#2** | ❌ **none** | Brazil does not hard-gate card acquiring, but **Pix requires a Brazilian bank relationship** | ⚠️ **High** — mitigated by `dLocal.br: true` |
| 🇯🇵 **Japan** | ✅ **#3** | ❌ **none** | No hard gate for cards; **konbini and carrier billing effectively require local partners** | ⚠️ **High** |
| 🇦🇺 Australia | ✅ | ❌ none | No | Moderate |

> **Warning:** Brazil is 24.07% of traffic with **no local entity**. `dLocal.br: true` indicates they solved local acquiring through a provider rather than an entity — the correct move, and it means **the Brazil gap is methods and recurring rails, not acquiring**.

> **Warning:** Japan is 2.75% and the fastest-growing APAC market with **no local entity, no Japanese rails, no Japanese help centre and no Japanese subscription terms** — despite full UI translation and JPY pricing.

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers
| Region | PSP | Evidence | Source |
|---|---|---|---|
| Global | **Primer** (orchestrator) | `[Source Code]` | `configs.cdn-simple-life.com/content-api/feature_flags.json` |
| Global | **Stripe** | `[Source Code]` + `[Terms/Privacy Policy]` | same; `simple.life/privacy/` |
| 🇧🇷 Brazil | **dLocal** | `[Source Code]` `dLocal.br: true` | same |
| 🇲🇽 Mexico | **dLocal — explicitly DISABLED** | `[Source Code]` `dLocal.mx: false` | same |
| Global | **PayPal** | `[Source Code]` `paypal: true` | same |
| Group | **"palta"** in-house path | `[Source Code]` `accountPageDelay.palta` | same |
| 🇳🇱 Netherlands | **Adyen** (iDEAL) | `[Source Code]` — a connector **inside Primer** | `StripeKlarna-*.js` |
| Global | **Braintree** | `[Source Code]` live `production_` key; **legacy, degraded** | `useStandaloneStepEvents-*.js` |
| Global | **`stripe_legacy`** | `[Source Code]` separate legacy Stripe path | `useBilling-*.js` |
| ? | **"flex" / `flex_card`** | `[Source Code]` 7th provider, own service module, routed via `primerApi` — ⚠️ **unidentified** | `flexService-*.js` |
| — | **Checkout.com** | `[Terms/Privacy Policy]` only — named as an example, **not seen anywhere in code** | `simple.life/privacy/` |

**From the privacy policy, verbatim — a merchant describing the problem orchestration solves, in writing:**
> *"We may disclose your personal data, including payment data, to various payment processing and payment gateway providers that help us connect with different banks and payment systems around the world … **Due to the large number of payment processing providers we work with, it is impractical to list them all here.** However, some examples are **Stripe, PayPal, Checkout**."*

### 3B. Payment Orchestrator
🔴 **Global orchestrator incumbent — Primer.**

> *"Confirmed orchestration-aware, and already served. This is a displacement-against-a-competitor motion, not an orchestration-education motion. The opening is coverage and reach — specifically recurring rails and local methods in Brazil and Japan — never the case for orchestration itself."*

**Three gateway code paths co-exist** (`palta`, `primer`, `stripe`), each with its own `accountPageDelay`. `[INFERENCE, not confirmed]` this indicates a migration in progress or an A/B between group in-house, Primer and direct Stripe.

## Section 4: Alternative & Local Payment Methods

**Method inventory from the live i18n bundles** (`en` 233,792 b · `pt` 252,694 b · `ja` 270,591 b, all HTTP 200) plus the feature flags.

| Market | Method | Category | Status | Source |
|---|---|---|---|---|
| Global | Credit/debit (Visa, MC, Amex) | Cards | ✅ **Active** | `form.tab_card`; `billing_errors.cvv.text` |
| Global | PayPal | Wallet | ✅ **Active** | `paypal: true` |
| Global | Apple Pay (via Stripe) | Wallet | ✅ **Active** | `applePayStripe: true`; `form.apple_pay_cta_label` |
| Global | **Google Pay** | Wallet | ⚠️ **BUILT BUT DISABLED** | `form.google_pay_tab` exists; **`googlePay: false`** |
| Global | **Klarna 0% instalments** | BNPL | ⚠️ **LIFETIME PLAN ONLY, routed via Stripe** | `integration:"stripe",paymentMethod:"klarna"`; `StripeKlarna-*.js` |
| Global | **Affirm** | BNPL | ⚠️ **in enum, not seen wired to a tab** | `e.AFFIRM="affirm"` |
| 🇺🇸 US | **FSA/HSA cards** | Cards | ✅ **Active** | `form.hsa_fsa.plan_picker_highlight` = "We accept FSA & HSA cards" |
| Global | Card vaulting / one-click | Recurring | ✅ **Active** | `form.one_click_payment`; `billing_errors.vault.title` |
| 🇧🇷 Brazil | CPF/CNPJ capture | Local compliance | ✅ **Active** | `form.cpf_field`, `form.cpf_error` |
| 🇧🇷 Brazil | **Pix** (one-off purchases) | A2A | ✅ **BUILT & SHIPPED** ⚠️ **behind an A/B flag** | `e.DLOCAL_PIX="pix"`; `PixForm`, `PixSelect`, `pixTabContent`; `pix: IS_PIX_PAYMENT_METHOD_FOR_BR_EXP && !isSubscriptionAction` |
| 🇧🇷 Brazil | **Pix Automático** (subscriptions) | A2A mandate | ✅ **BUILT & SHIPPED** ⚠️ **behind the same A/B flag** | `e.DLOCAL_PIX_AUTOMATICO="pix"`; `pix_automatico: IS_PIX_PAYMENT_METHOD_FOR_BR_EXP && isSubscriptionAction` |
| 🇧🇷 Brazil | CPF/CNPJ tax ID | Local compliance | ✅ CONFIRMED, gated on dLocal | `FEAT_SHOW_TAX_ID(n){return n.dLocal?.br}`; `isShowTaxId(){return countryCode==="br" && FEAT_SHOW_TAX_ID}` |
| 🇧🇷 Brazil | boleto · parcelamento · Elo · Hipercard · Mercado Pago | Cash / instalments / cards | ❌ NOT FOUND | 0 hits across bundles — but Brazil is otherwise well covered |
| 🇯🇵 Japan | **konbini · PayPay · LINE Pay · Rakuten Pay · Paidy · carrier billing · JCB** | Cash / wallet / BNPL / carrier | ❌ **NOT FOUND** | 0 hits incl. コンビニ |
| 🇦🇺 Australia | **PayTo · BPAY · Afterpay · Zip** | Mandate / BNPL | ❌ **NOT FOUND** | 0 hits |
| 🇳🇱 Netherlands | **iDEAL** | A2A | ✅ **CONFIRMED — via Adyen** | `e.ADYEN_IDEAL="ideal"`; `ideal` in tabsOrder |
| 🇪🇺 Europe | **SEPA DD · Bancontact · Cartes Bancaires** | A2A / local | ❌ **NOT FOUND** | 0 hits |
| 🇲🇽 Mexico | **OXXO · SPEI · meses sin intereses** | Cash / A2A / instalments | ❌ **NOT FOUND** | 0 hits; `dLocal.mx: false` |
| 🇹🇷 Türkiye | **taksit · Troy** | Instalments / local cards | ❌ **NOT FOUND** | 0 hits |
| 🇿🇦 South Africa | **ZAR pricing** | Currency | ❌ **NOT FOUND** | not among the 18 currencies |

> **Warning:** In **Brazil**, Pix is the dominant online rail and boleto remains material. Neither appears in the merchant's own strings. ⚠️ **Caveat: Primer renders methods client-side — verify on a BR IP before asserting.**

> **Warning:** In **Japan**, konbini and carrier billing are default expectations for digital subscriptions. **Zero Japanese rails are present**, and the one instalment option (Klarna) **has no meaningful Japanese consumer footprint** — so 「かんたん0%分割払い」 is likely a dead string that never renders for a Japanese shopper.

**Recurring rails.** Card vaulting is the global default (`form.one_click_payment`, `billing_errors.vault.title`, `e.VAULT="vault"`). **But Brazil also has `DLOCAL_PIX_AUTOMATICO` — a genuine mandate rail.** ⚠️ **So the "card-only renewals everywhere" reading is WRONG.** What remains absent: **SEPA Direct Debit (EU), PayTo (AU), ACH (US), and any mandate rail in APAC.** The pattern is that they build mandate rails where they have invested — and they have not invested in APAC.

**All three locale bundles have identical key sets — zero locale-specific keys.** One global card-and-wallet checkout, translated 15 ways. **No market gets a single extra payment method at the string level.**

## Section 5: Payment Issues & Customer Complaints

| Issue | Platform | Frequency | Date | Web or store? | Source |
|---|---|---|---|---|---|
| **Aggregate: 4.3/5 across 46,412 reviews; 1–2★ = 11% ≈ ~5,100 negative; rating down from 4.5** | Trustpilot `simple-life-app.com` | **High volume** | live, Oct 2026 | profile is the **web** billing domain | [trustpilot.com/review/simple-life-app.com](https://www.trustpilot.com/review/simple-life-app.com) ⚠️ **agent-fetched; my re-fetch 403'd** |
| Money taken for "services the victims weren't aware they purchased" | Trustpilot (2★) | — | 5 Oct 2026 | not stated | same |
| Charged full price despite an advertised discount | Trustpilot (4★) | — | 19 Sep 2026 | not stated | same |
| Difficulty cancelling; auto-renewal charge reversed on contact | Trustpilot (5★ ×2) | — | 5 Oct 2026 | not stated | same |
| *"Simple Life keeps billing after cancel"* | **Şikayetvar** (Türkiye) | unknown | unknown | unknown | ⚠️ **HTTP 403, not fetched** |

**The agent's fetch noted that no sampled review referenced an Apple or Google charge — all appeared to reference direct website billing.** Single-page sample; indicative, not conclusive. **But it points the complaint surface at *their* rails, not Apple's.**

**🔑 The strongest complaint evidence is in their own product copy.** `billing_errors.generic` instructs users to **phone their card issuer and ask it to unblock transactions for "Simple.Life Apps Inc."** **You do not build that UI unless cross-border card declines are a known, material problem. That is a decline-rate pain admission, written by them.**

**Corroborating — they are monetizing failure rather than fixing it.** A full `cancellation_fee` string tree exists: `cancellation_fee.confirmation_popup.pay_and_cancel_now`, *"cancel your subscription now for a flat {feeAmount} fee"*, plus commitment-period lock-ins and a type-to-confirm cancellation gate. **They defend retention with contractual friction and exit fees, not with payment-rail coverage.** Usable talking point — and a consumer-protection risk flag in BR/EU/AU.

**🇧🇷 Reclame Aqui — NOTHING FOUND**, searched twice. Simpla Educação, Simpla Club and PUNTU INOVA SIMPLES were all excluded as different companies. Two readings, indistinguishable without more work: no Brazilian presence and so no local complaint channel, or Brazilians paying in USD by card and complaining on Trustpilot instead. **Either is an opening — but it is a hypothesis, not a fact.**

**🇯🇵 Japan — NOTHING FOUND.** Confirmed only that the app is listed on the Japanese App Store.

**Regulatory: no action against Simple or Palta found.** Searched specifically. ⚠️ **Noom's 1,200+ BBB complaints are NOON's, not Simple's** — useful as category evidence that this billing model attracts scrutiny. ⚠️ **Flo's FTC settlement is a sibling app and concerns health data, not payments. Do not attribute either to Simple.**

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | **29 Sep 2026** | **1,000,000 subscribers** | Milestone | [simple.life/blog/one-million-subscribers](https://simple.life/blog/one-million-subscribers) (fetched) |
| 2 | **23 Feb 2026** | **$160M ARR** (reached 2025), 21M+ downloads, ~20M lbs lost | Financial | [insider.fitt.co](https://insider.fitt.co/press-release/simple-reaches-160m-in-arr-fueled-by-its-personalized-sustainable-approach-to-weight-loss) (fetched) |
| 3 | **~Oct 2025** | **$35M Series B**, HartBeat Ventures + Liquidity Capital; for the AI coach "Avo" | Funding | [tech.eu](https://tech.eu/2025/10/02/simple-life-lands-35m-to-scale-its-ai-health-coach/) `[UNVERIFIED]` |
| 4 | — | **Palta group payments function**: VP of Payments (Gianluca Cassaro) + Global Payments Ops Lead (Elaine Nguyen); internal monetization/payment platform; group chargeback management | Payment Infrastructure | [primer.io case study](https://primer.io/case-studies/in-conversation-with-gianluca-cassaro-payments-vp-and-elaine-nguyen-payments-oper) (fetched) |
| 5 | 2024 | Primer roadmap: **fallbacks to "recover failed transactions and boost revenue"** | Payment Infrastructure | same (fetched) |

**No public payment-related RFP found.**
**No payments job posting at Simple specifically.** The Palta "in-house monetization platform for web payments… tens of millions of USD annually… aims to grow" posting **404s and is unverified**. Flo's Senior PM Payments role (Vilnius, owning payments across Web/iOS/Android) is **Flo, not Simple** — but it suggests the portfolio may be **decentralising** payments ownership. `[INFERENCE]`

## Section 7: Payment-Specific News

**No Simple-specific payment news found.** No new PSP partnership, no provider removal, no checkout change announced.

**The one timely category signal, and it is inferential, not evidenced:** US iOS apps can now link out to external web payment following the Epic v. Apple anti-steering ruling (Apple held in civil contempt 30 Apr 2025; 9th Circuit upheld; **Supreme Court agreed to hear Apple's appeal, reported 1 Jul 2026** `[UNVERIFIED]`). **Simple and Palta have said nothing publicly about external link-out, web billing or store fees.** **Frame as a question, never as an assertion.**

## Section 8: Checkout Experience Audit

⚠️ **Partially accessible. The checkout is a client-side SPA and the JS bundle is an ES-module stub that only re-exports chunks; Primer assembles the method list at runtime from its own dashboard. No rendered paywall was observed in any market.**

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | Custom SPA paywall at the end of a quiz funnel, orchestrated by Primer | — | `simple.life/survey/` → paywall |
| Guest checkout | Quiz-first, email captured before paywall | Fair | standard web2app pattern |
| Card input | Primer-hosted fields `[INFERENCE]` | — | not observed |
| Methods visible | Card, PayPal, Apple Pay; Google Pay built but flagged off | Fair | from flags + strings |
| Location-based display | **Geo-IP wired in** — `assets.simple.life/geo.json` returns country/region/city | Good | returned US/Ohio for this egress IP |
| Instalments | **Klarna, lifetime plan only** | Poor | absent from regular plans; no local instalments anywhere |
| 3DS | **Adaptive 3DS live via Primer** | Good | primer.io case study |
| PCI indicator | Reduced scope via orchestrator-hosted fields `[INFERENCE, not confirmed]` | — | no card fields in merchant code |
| Multi-currency | **18 currencies, local pricing with VAT breakout** | **Good** | `{price} ({net} + {vat} VAT)` |
| Saved methods | **One-click / vaulting live** | Good | `form.one_click_payment` |
| Error clarity | Detailed decline-recovery flow — **tells users to call their issuer** | Fair | and see Section 5 |

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|---|---|---|
| PCI DSS Level | **No public documentation found** | — |
| Card data handling | `[INFERENCE, not confirmed]`: **reduced scope**. No PAN/CVV capture fields exist in merchant code; card entry is delegated to the orchestrator/PSP | i18n bundle inventory |
| Recommended Yuno integration | SDK (drop-in), consistent with their current hosted-fields posture | — |

## Section 10: Strategic Insights & Outreach Angles

> **Insight #1: APAC is the only region they have not built for — and they have proved they will build**
> **Evidence:** S3A/S4 — **dLocal local acquiring + Pix + Pix Automático in Brazil; Adyen iDEAL in the Netherlands**, all verified in their own paywall bundle. S4 — **zero APAC local methods anywhere**: no konbini, PayPay, LINE Pay, Rakuten Pay, Paidy, carrier billing, JCB, PayTo, BPAY. S1 — Japan is #3 and the fastest-growing APAC market (▲38.48%) with the **highest pages/visit in the whole table (18.56)**.
> **Pain:** Their most engaged non-US audience pays by card in a konbini-and-carrier-billing market. Every APAC authorisation is cross-border against a local issuer, with no local rail to fall back to.
> **Yuno value:** APAC rails through one integration, additive to the existing stack, without an APAC entity.
> **Best success case:** A subscription business that added APAC local rails. ⚠️ **Only cite a Yuno customer with a published metric.**
> **Angle:** They cannot say "we don't do local methods" — they built recurring Pix in Brazil. The question is only why the same logic stopped at Asia.
> **Subject line:** *"Pix in Brazil, cards in Japan"*

> **Insight #2: Japan got the expensive half of localisation and not the cheap half**
> **Evidence:** S4 — full Japanese UI (270,591-byte bundle), JPY pricing, Japanese ToS and Privacy — but **zero Japanese rails**, `/subscription-terms/ja` and `/refund/ja` both **404**, and no Japanese help centre. S1 — Japan is #3 and the fastest-growing APAC market (▲38.48%) with the **highest pages/visit in the entire table (18.56)**.
> **Pain:** Their most engaged non-US audience is asked to pay by card in a konbini-and-carrier-billing market, then supported in English when it fails.
> **Yuno value:** Japanese rails through one integration, without a Japanese entity.
> **Angle:** The internal case for Japan is already made and funded — the rails are the unfinished part.
> **Subject line:** *"Japanese checkout, English refund policy"*

> **Insight #3: Google Pay is built and switched off**
> **Evidence:** S3A — `googlePay: false` in live production config. S4 — `form.google_pay_tab` and `form.google_pay_cta_label` strings exist, fully translated.
> **Pain:** They paid to build it and are not running it. In Brazil and Türkiye — Android-majority markets totalling 25%+ of traffic — that is a live conversion question.
> **Angle:** A single discovery question, not an assertion: is that a deliberate test or a stalled rollout?
> **Subject line:** *"Google Pay flag"*

> **Insight #4: The decline-recovery copy is an admission**
> **Evidence:** S5 — `billing_errors.generic` tells users to **phone their issuer** and ask it to unblock "Simple.Life Apps Inc." S2 — no local entity in Brazil or Japan, so those are cross-border authorisations against foreign issuers.
> **Pain:** They built a UI for a decline problem instead of routing around it. Cross-border acquiring against local issuers is the standard cause.
> **Yuno value:** Local acquiring per geography inside the existing stack.
> **Angle:** Quote their own error copy back. It is unanswerable and it is theirs.
> **Subject line:** *"Your decline screen"*

### Quick Hits

**Email hooks**
1. Their subscription terms list four different bank-statement descriptors for one product — Simple Premium, Simple Life, Simple App, Simple App Weightloss.
2. Their checkout speaks Japanese; their refund policy and help centre do not.
3. They built recurring Pix for Brazil and shipped Japan a card form — in their fastest-growing and most engaged market.

**Cold call openers**
1. *"You've localised the checkout into fifteen languages — I was curious why the payment methods are the same in all fifteen."*
2. *"Your billing error screen asks customers to ring their bank. Is that mostly Brazil and Japan?"*
3. *"You run Pix Automático in Brazil — is there a reason the same approach hasn't gone to Japan yet?"*

## Section 11: Similar Companies & Prospecting Pipeline

### 11A. Direct competitors
| Company | HQ | Key markets | Known PSP/Orchestrator | Source |
|---|---|---|---|---|
| **Noom** | USA | US-centric | **Stripe** — consolidated all volume; Billing, Payments, Radar; claims **+8% global auth rate** | [stripe.com/customers/noom](https://stripe.com/en-si/customers/noom) `[UNVERIFIED — vendor page, summary only]` |
| **BetterMe** | Ukraine | Global quiz-funnel | **Not found** — searched specifically | — |
| **Yazio** | Germany | EU | Not found | — |
| **Zoe** | UK | UK/US | Not found | — |
| **WeightWatchers** | USA | US/EU | Not found | — |
| **Fastic · DoFasting · Zero · Lifesum · MyFitnessPal** | various | various | Not researched | — |

### 11C. Competitors adopting orchestration
> **"No public case studies found of direct competitors adopting payment orchestration."**

**The orchestration layer is genuinely unclaimed in this vertical.** Cuts both ways: no social proof to point at, and no incumbent to displace **at competitors** — though Simple itself already has one.

⚠️ **Do not use Noom's Stripe case study as proof.** It argues for **consolidation onto a single PSP** — the opposite of the orchestration case. It is useful only to reframe: *Noom chose one processor; Simple chose many and now has to govern them.*

### Top prospect pipeline — a genuine find
**Neither Simple.life nor ANY fasting/weight-loss subscription app appears on the 1,220-row `accounts/apac-tal.csv`.** I checked Simple, Noom, Zoe, Fastic, BetterMe, Yazio, Lifesum, Lose It!, MyFitnessPal, Palta, Flo and Zing. (Apparent hits on "flo" and "zing" were **FlowerAura** and **Zingoy/Zingbus** — false positives, excluded.)

**The entire consumer-health-subscription vertical is absent from the APAC TAL.** ⚠️ Whether that is an oversight or correct scoping is a real question — on this evidence these companies are **not APAC-HQ'd**, so their absence may be right.

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|---|---|---|
| Annual revenue | **$160M ARR (2025)**; $100M FY2024 (+64% YoY) | insider.fitt.co (fetched); tech.eu `[UNVERIFIED]` |
| GMV | Not disclosed | — |
| Average transaction value | **~$160/subscriber/year ≈ $13.3/mo equivalent** `[DERIVED]` | $160M ARR ÷ 1M subscribers. ⚠️ **Periods mismatched** (ARR 2025, subscribers Sep 2026), so true ARPU is likely lower |
| Est. annual transactions | 1M – 12M | subscribers × billing frequency |
| **Monthly transaction count** | ✅ **DERIVED: ~83,000/month floor** — 1,000,000 subscribers **[SOURCED]** × 1 charge/yr ÷ 12. Ceiling 1,000,000/month if all monthly. Realistic mix: several hundred thousand. **Gate CLEARED — no scenario consistent with the sourced subscriber count falls under 40,000.** | simple.life/blog/one-million-subscribers (fetched) |
| **Billing channel split (web vs app store)** | 🛑 **UNDISCLOSED — the single biggest gap on the account.** Four independent search angles found no published, estimated or third-party figure. | — |
| Active users | **1M subscribers** (Simple, Sep 2026) vs **1M MAU** (palta.com) — ⚠️ **metric conflict, unresolved** | both fetched |
| Primary currency | USD, with 18-currency local pricing | i18n bundle (fetched) |
| Top 3 markets by traffic | US 45.69% · Brazil 24.07% · Japan 2.75% | SimilarWeb, supplied |

**🛑 Why the split matters more than the headline:** total billing events clear the gate comfortably, but **IAP transactions are Apple's and Google's, not orchestrable**. At a hypothetical 20% web share the floor scenario drops to ~17k/month; at 50%+ it clears on its own. **Per the rules, an assumed split can never reject the account — and the sourced floor on total events does clear.**

**The strongest available signal on the split is structural, not a number** `[INFERENCE, not confirmed]`: **3DS, network tokenization, PSP fallbacks and chargeback management are card-rail concepts that do not exist in Apple/Google IAP.** Apple and Google handle their own auth and tokens, and there are no merchant-side chargebacks on IAP. **A group that has bought orchestration and staffed a chargeback function is doing material direct card volume.** That establishes web billing is **significant**; it does **not** establish it is the majority.

### Overall Research Confidence

**HIGH on the payment stack and method inventory. MEDIUM on financials. LOW on the billing-channel split and on complaints.**

**Traffic data was SUPPLIED by Prateek**, not API-sourced or estimated — but **total visit counts were not shown**, so no absolute volume figure could be derived from it.

Unusually strong first-party evidence: production feature flags, three full i18n bundles, the locale array and the legal-page locale matrix were all read directly. The weakness is that **no rendered checkout was observed in any market** — the paywall is a client-side SPA whose method list Primer assembles at runtime, and the egress IP geolocates to Ohio, so no non-US branch could be exercised.

### Manual Research Recommendations

> **Area:** Web-vs-IAP billing split · **Why:** Determines the addressable volume and therefore the whole business case. · **Action:** Discovery question. Nothing public will answer it.

> **Area:** What **"flex" / `flex_card`** is · **Why:** It is a seventh payment provider with its own service module, routed through `primerApi`, and it is unidentified. If it is a competitor or an unlisted PSP that changes the competitive picture. · **Action:** Walk the checkout on a non-US IP and watch the network calls from `flexService.js`.

> **Area:** Whether APAC local methods exist in the **mobile app** (not the web bundle) · **Why:** The entire APAC-gap thesis rests on the web stack. Absence in the web bundle does not prove absence in the app. · **Action:** Inspect the iOS/Android build, or ask on a call.

> **Area:** The four statement descriptors — *Simple Premium / Simple Life / Simple App / Simple App Weightloss* · **Why:** Four descriptors usually mean multiple merchant accounts or acquirers, which would corroborate the privacy policy's admission. · **Action:** Search chargeback and "what is this charge" forums for each; those pages often name the acquirer.

> **Area:** The Palta "in-house monetization platform… tens of millions USD" posting · **Why:** If verified it is the single best signal here — a home-grown web payment platform that now needs to grow into Brazil and Japan is exactly the build-vs-buy moment. · **Action:** Sweep Palta's live Greenhouse board (`job-boards.greenhouse.io/paltaltd`). Cheap.

> **Area:** Şikayetvar `simple-us` (HTTP 403) · **Why:** The only platform found with an explicitly payment-shaped, on-brand complaint. · **Action:** Retry from a different client or via cache.

### Appendix: Source URLs
**Verified first-hand:** `configs.cdn-simple-life.com/content-api/feature_flags.json` · `i18n.cdn-simple-life.com/i18n/{en,pt,ja}/web.json` · `simple.life/` · `/privacy/` · `/tos` · `/tos/ja` · `/tos/pt` · `/privacy/ja` · `/subscription-terms` · `/refund` · `/survey/` · `primer.io/case-studies/in-conversation-with-gianluca-cassaro-payments-vp-and-elaine-nguyen-payments-oper` · `assets.simple.life/geo.json` · `help.simple.life/en/`
**Agent-fetched:** `simple.life/blog/one-million-subscribers` · `insider.fitt.co/press-release/simple-reaches-160m-in-arr…` · `palta.com/` · `trustpilot.com/review/simple-life-app.com` (my re-fetch 403'd)
**`[UNVERIFIED — search summary only]`:** `tech.eu/2025/10/02/simple-life-lands-35m…` · `vestbee.com/blog/articles/simple-life-secures-35-m` · `pagbrasil.com/blog/pix/recurring-pix/` · `stripe.com/customers/noom` · `cbinsights.com/company/palta/financials`
**Failed:** `sikayetvar.com/en/simple-us` (403) · `job-boards.greenhouse.io/paltaltd/jobs/5137617004` (404, delisted) · `trustpilot.com/review/simple-life-app.com` (403 on my attempt)

</details>
