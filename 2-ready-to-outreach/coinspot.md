# CoinSpot

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 15 / 29 → 🟢 **Medium**
**Industry:** Crypto & Digital Assets — Australian retail exchange · **HQ:** **Casey Block Services Pty Ltd**, Australia (`coinspot.com.au`) · **Researched:** 2026-10-06 · **First email sent:** —
**Motion:** ✅ **GREENFIELD — no orchestrator, and card deposits redirect to an unbranded third-party hosted portal.** No routing or cascade layer exists.

---

> ## ⚠️ QUALIFICATION — in scope as a merchant, but read the caveat before pitching
>
> **CoinSpot holds an AFSL, and it is specifically a non-cash payments authorisation.** From CoinSpot's own announcement (created 2026-04-30, updated 2026-07-25), verbatim:
>
> > "As Australia's largest & most established cryptocurrency exchange, CoinSpot is proud to have been granted an Australian Financial Services Licence (AFSL) by ASIC **for non-cash payments**. … CoinSpot has secured an Australian Financial Services Licence, **for the provision of non-cash payment facilities**, positioning the business well as Australia's digital asset regulatory framework continues to evolve."
>
> AFSL reported as **562554**, granted **29 April 2026**, held by Casey Block Services. `[UNVERIFIED — search summary only]`
>
> **Why this is still a merchant and NOT a Partnerships referral:**
> - The non-cash payment facility authorisation exists to cover **CoinSpot's own consumer products** — the AUD wallet balance and the CoinSpot Mastercard. It is a **stored-value/NCP licence, not an acquiring, PayFac or gateway licence.**
> - **CoinSpot sells nothing payments-related to third parties.** No merchant acquiring, no gateway, no PayFac, no payouts-as-a-service, no API for other businesses to take payments. Their API is a **trading** API.
>
> **🔑 Contrast with PDAX in this same batch, which was rejected:** PDAX markets cross-border settlement, payroll payouts and merchant settlement to *other financial institutions* and holds an **EMI** licence. **That is payment infrastructure. CoinSpot's NCP licence covers its own wallet. The distinction is what a third party can buy from them — and from CoinSpot, nothing.**
>
> ⚠️ **Still, flag it to Prateek before sending.** An exchange holding a payments licence is a borderline call, and if he disagrees it routes to Partnerships.
>
> **Australia's incoming digital asset platform (DAP) licensing regime** under the Corporations Act is also live context. ⚠️ **Do NOT cite any deadline from background knowledge — verify at the time of writing.**

---

> ## ⛔ MY BRIEF'S HYPOTHESIS WAS INVERTED — and the real answer is a BETTER pitch
>
> I briefed the research expecting a 1–2.5% card-deposit fee as evidence of cost-of-acceptance pain. **There is no such fee.**
>
> **I fetched `https://www.coinspot.com.au/fees` myself (HTTP 200, 45,697 bytes). The published table, verbatim:**
>
> | Type | Fee |
> |---|---|
> | PayID | **Free** |
> | Direct Deposits | **Free** |
> | **Cash** | **2.5%** |
> | **Card** | **Free** |
> | PayPal | **Free** |
> | Bank Withdraw AUD | Free |
> | PayPal Withdraw AUD | 2% |
>
> And from their own card article: *"**Is there a fee for Card Deposit?** Any deposit made through a Debit or Credit card are processed instantly & **FREE**."*
>
> **This is a STRONGER cost-of-acceptance argument, not a weaker one, and it is the pitch:**
>
> 1. **CoinSpot absorbs 100% of card acceptance cost as a P&L line.** No surcharge, no pass-through. **Every basis point of interchange, scheme fee and acquirer margin on card, Apple Pay and Google Pay deposits is CoinSpot's cost, not the customer's.**
> 2. **They DO charge 2.5% on cash — proof they will price a rail when they choose to.** Zero-rating cards is therefore a **deliberate acquisition subsidy**, not an oversight.
> 3. **They push the issuer's cost onto the user instead:** *"Please note, if deposits are made via Credit Cards, **Bank Fees may apply**."* **They absorb their own acceptance cost but disclaim the issuer's.**
> 4. **🔑 The limit structure is the tell.** Card, Apple Pay and Google Pay are each capped at **A$5,000/24h**, while **PayID and Direct Deposit have NO LIMIT.** **Free rails get unlimited headroom; card rails get capped. That gap is where the economics live.**

---

> ## 🎯 THE HOOK — CoinSpot publicly documents a card approval-rate problem and tells customers to fall back by hand
>
> From their own "Help using Card Deposit" troubleshooting list, verbatim:
>
> > "**Why is my Card Deposit failing to process?** … Exceeding your Debit/Credit card daily withdrawal limit. · Insufficient funds in your Debit/Credit card. · There is a temporary lock applied on your Debit/Credit card. · **Your banking institution does not allow Debit/Credit card deposits to cryptocurrency exchanges.** … If you are still experiencing failed deposits, we recommend you to reach out to your banking provider… **Alternatively, you can utilise other deposit methods such as PayID or Direct Deposit.**"
>
> And from the Google Pay article's own table of contents: **"Why does my card show 'Unavailable for this merchant'?"**
>
> **This is CoinSpot publicly conceding an issuer-driven card-deposit decline problem, and publicly instructing customers to switch rails MANUALLY. That manual fallback is exactly what a cascade automates.** It is the highest-value quotable evidence on the account, and it is in their own help centre.
>
> Corroborating, from their PayID article: *"PayID deposits, especially if this is your first deposit or you have deposited a large amount, **can often be held for security reasons**."*
>
> ### The second hook — instant in, T+1 out
> > "Submit your request before **2pm (AEDT)** on a weekday to see the funds in your nominated bank account **within the next day** … requests are generally processed the same day with the funds clearing **the following business day** … depending on your banking institution, withdrawals may take **up to two business days**, notably weekend withdrawal requests."
>
> **CoinSpot takes money in instantly over NPP/Osko and pays it out on a batched, cut-off-driven, next-business-day cycle.** There is **no Osko/NPP outbound payout, no PayTo, no real-time withdrawal** anywhere in their documentation. **For a retail exchange competing on UX in a market where outbound Osko is table stakes for neobanks, that is a live competitive liability — and it is a payout-orchestration problem, not a banking problem.**

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Australia's largest and longest-established retail crypto exchange, operating since 2013, aimed at beginners. **"Join 3 million other users"** — verified on their own fees page today, 2026-10-06 (⚠️ **marketing copy, treat as such**). Reported ~65% share of the Australian DCE market `[UNVERIFIED — IBISWorld summary]`.

**SimilarWeb total visits:** **2.648M** (Aug 2026), **−6.98% MoM**, 71.66% mobile web, **Australia 90.04%** — supplied by Prateek.

### 🛑 Cross-border is explicitly OFF
**90.04% domestic, AUD only, withdrawals only to an Australian account in the holder's own name, no international bank account offered.** Per `.claude/reference/apac-payments.md` §6b there is no corridor to argue. **ANZ is the one sub-region where routing, failover and cost-of-acceptance framing lands most directly — use that.**

### Transaction volume — DERIVED
**Method A — web-visit conversion (deliberately harsh):**
```
2,648,000 visits/mo × ASSUMED 2%–5% deposit-session conversion
                              =  52,960 – 132,400 fiat deposits/month   ✅ floor clears the gate
```
⚠️ **And this method structurally UNDERSTATES**, because SimilarWeb counts web only while **CoinSpot's two newest rails are exclusively in-app** — *"Apple Pay Deposit is only available through the CoinSpot Mobile App for iOS devices"*, *"Google Pay Deposit is only available through the CoinSpot Mobile App for Android devices"*. **Total deposit sessions are materially higher than web visits imply.**

**Method B — registered-user activity:**
```
3,000,000 registered (SOURCED, their own footer)
× ASSUMED 2%–3% monthly-active-depositor rate (high dormancy expected — registrations accumulate since 2013)
                              =  60,000 – 90,000 depositing users/mo
× ASSUMED 1.2–1.5 deposits each
                              =  72,000 – 135,000 fiat deposits/month
```

**🎯 Gate verdict: CLEARS on both methods, floor ~53,000/month. Label DERIVED** — no sourced transaction count exists.

### Fiat deposit rails — all fees published by CoinSpot itself
| Rail | Status | Fee | 24h limit | Min | Speed |
|---|---|---|---|---|---|
| **PayID (NPP)** | ✅ CONFIRMED | **Free** | **NO LIMIT** (bank-set) | $1 | Instant; 1–2 BD on first/large |
| **Direct bank transfer / Osko (NPP)** | ✅ CONFIRMED | **Free** | **NO LIMIT** (bank-set) | $1 | Instant via Osko |
| **Debit/credit card (Visa & MC)** | ✅ CONFIRMED | **FREE** | **$5,000** | $1 | Instant |
| **Apple Pay** | ✅ CONFIRMED (launched 26 May 2025) | **FREE** | **$5,000** | $1 | Instant — **app only** |
| **Google Pay** | ✅ CONFIRMED (launched 26 May 2025) | **FREE** | **$5,000** | $1 | Instant — **app only** |
| **Cash (Blueshyft newsagents)** | ✅ CONFIRMED | **2.5%** | **$8,000** | $50 | Instant, QR code in store |
| **PayPal** | ✅ CONFIRMED | **Free** (deposit) | **$10,000** | $1 | Instant |
| **POLi** | 🛑 **DISCONTINUED 28 Sep 2023** | — | — | — | — |
| **BPAY** | ❌ **NOT OFFERED** | — | — | — | — |
| **PayTo** | ❌ **NOT FOUND** | — | — | — | — |

Note their own framing: *"Each payment method has its own 24hr limit and **these limits are independent from each other. You can use a combination of deposit methods to fund your CoinSpot account.**"* — i.e. **the customer is doing the rail-cascading manually.**

### 🛑 Rail claims circulating online that are WRONG — do not repeat these
- **"1.88% card fee"** — from `helpcentersupoorttttttttttttt.zohodesk.in` and Goodreads quote pages. **These are SEO/scam pages carrying fake CoinSpot "support" phone numbers (+61-3-5929-4808). Do not cite, do not call.** Contradicted by CoinSpot's own fee page and help centre, both updated 2026-09-30, which say **FREE**.
- **"1.22% Apple Pay/card fee"** — from plisio.net / therocktrading.com / datawallet.com. Contradicted by CoinSpot's own articles: *"Apple Pay Deposits are **FREE** & have a $5,000 AUD 24 hour deposit limit"*; *"Google Pay has an AUD Deposit limit of $5,000 AUD per 24hr & **NO FEE**."*
- **"PayTo is live on CoinSpot"** — asserted in search summaries. **A query of CoinSpot's own help-centre API containing "PayTo" returned 31 results and NOT ONE is a PayTo article; the string appears in no article body. PayTo is NOT FOUND.**
- **"POLi and BPAY are current methods"** — asserted by review sites and the scam pages. **POLi was killed 28 Sep 2023; BPAY is not offered.** BPAY appears only incidentally inside bank-app screenshot instructions in their PayID guides.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

> **Not yet generated.** Run `/full-outreach CoinSpot` to compose the 12-touch sequence into this section.
>
> **Motion is GREENFIELD.** But ⚠️ **reason carefully rather than defaulting:** for a licensed exchange an in-house treasury/payments function is the norm, and the card-deposit flow redirects to an unbranded third-party hosted portal. **No orchestrator and no routing layer is evidenced — that is the claim, and it is as far as the evidence goes.**
>
> **🛑 Flag the AFSL question to Prateek before sending** (see Qualification).
>
> **Lead with the zero-rated card rail against the 2.5% cash rail and the A$5,000 cap — all three published by CoinSpot themselves.**

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

## Section 1: Withdrawal / payout rails

| Rail | Fee | Limit | Speed |
|---|---|---|---|
| **AUD bank withdrawal (BSB/account)** | **FREE** | **No min, no max** | ⚠️ **NOT real-time** — see The Hook |
| **PayPal AUD withdrawal** | **2%** ⚠️ see conflict | — | Next business day |
| International bank account | ❌ **NOT OFFERED** | — | — |

⚠️ **CoinSpot contradicts itself on the PayPal withdrawal fee.** `/fees` states *"PayPal Withdraw AUD — **2%**"* with no cap. The help centre states *"users who are completing AUD Withdrawals via PayPal will incur a **2% fee capped at $1.25**."* **A 2% fee capped at A$1.25 binds at A$62.50, which makes the stated 2% meaningless above trivial amounts. One of the two is wrong — quotable as-is.**

**Additional payout friction, all CoinSpot-documented:**
- Withdrawals require **email confirmation** of each request.
- *"AUD withdrawal requests **may be paused** if CoinSpot determines more information is required regarding the safety of your CoinSpot account."* — **a manual risk hold in the payout path.**
- *"we do not hold funds for you when you create an AUD withdrawal request. Instead we will debit your AUD holdings **once the withdrawal has been processed**."* — **no reservation of funds, so a withdrawal can fail at processing time for insufficient balance.**
- Bank-detail changes gated behind app-based 2FA.
- Withdrawals only to an Australian account **in the account holder's own name**; deposits likewise only from the holder's own personal account — *"As per our Terms of Service CoinSpot can only accept payments from your own personal bank account."*

## Section 2: 🛑 Banking partner / NPP enabler — NOT FOUND. The biggest hole.

**This could not be closed, and it matters.**
- **CoinSpot's PayID and Direct Deposit details are generated per-user behind login** (*"Please log in to your CoinSpot Account … to view your details"*). **The BSB — which would identify the sponsoring ADI or the non-bank Identified Institution — is not publicly visible.**
- **CoinSpot's help centre never names its NPP/PayID enabler.** Every cached help-centre article body was scanned for `Monoova|Zepto|Zai|Cuscal|EML|Novatti|Nium|Stripe|Adyen|Braintree|Airwallex|issued by|issuer` — **the only hit was EML (via press, for the Mastercard), nothing for the deposit rails.**
- **No press release, partner case study or directory listing links CoinSpot to Monoova, Zepto, Zai/AssemblyPay or Cuscal.** Targeted search returned only generic material on those four providers with **nothing connecting any of them to CoinSpot.**
- **The card acquirer/gateway is also NOT FOUND.** CoinSpot documents a **redirect to a third-party hosted page** — *"You will be redirected to the **Card Deposit Payment Portal**. Enter your Card Details (1) > Then select Pay (2)"* — followed by a **CAPTCHA** and a **3DS/OTP step-up** (*"Your banking institution may request you to verify the transaction. An OTP will be sent to your mobile phone number"*). **That is unambiguously an externally hosted payment page, i.e. a third-party gateway — but it is not branded in any public asset and the portal URL sits behind login.**

**Market context (NOT CoinSpot):** Binance Australia lost PayID deposits and AUD bank transfers in 2023 *"due to steps taken by a **third-party payment provider**"* — **the standard Australian failure mode is the ENABLER withdrawing, not the bank.** `[UNVERIFIED — search summary]`

**Only reliable way to close this: read the BSB off a live logged-in deposit page, or ask on the call. Recommend the latter.**

## Section 3: 🔑 Debanking / rail-loss history — two confirmed events, both strong signals

### Event 1 — 2018: CoinSpot shut off AUD deposits entirely
> CoinSpot *"temporarily blocked users from making deposits in Australian dollars… **'We have temporarily disabled new AUD deposits'**… the temporary ban was due to banks being increasingly restrictive about dealings with cryptocurrency providers… CoinSpot assured customers that they would continue to work on **establishing a relationship with a banking partner** so they could resume accepting AUD deposits as soon as possible."* `[UNVERIFIED — search summary]`, corroborated independently on forum.cardano.org.

Restriction in force *"until at least the first week of the new year"* → late 2017/early 2018. **CoinSpot has been fully off-ramped once before and had to go find a new banking partner. There is institutional memory of total rail loss.**

### Event 2 — Sept 2023: the POLi rail killed with ~7 days' notice, outside their control
> "POLi Payments will be concluding its services to Australian users on the **30th September 2023**. POLi Deposit transfers to CoinSpot will no longer be available after the **28th September 2023**. Why? Australia Post has announced they are closing the POLi Payment service in Australia… **The decision for POLi to conclude its services is outside of CoinSpot's control.**"
> — CoinSpot help centre, created 2023-09-21, **still maintained (last updated 2026-01-06)**

CoinSpot had to publish customer comms and re-route users to five other rails. **They wrote "outside of CoinSpot's control" themselves. That sentence is the rail-redundancy pitch, in their own words.**

### Big-four pressure (market-level, not CoinSpot-specific)
- CBA applies a **A$10,000/month transfer limit to crypto exchanges** and holds certain crypto-exchange payments for **24 hours** as an anti-scam measure. `[UNVERIFIED — search summary]`
- Coinbase has publicly accused the big four of systematic crypto debanking; reportedly **up to 60% of fintechs** have faced banking denials. `[UNVERIFIED — search summary]`

**No 2024–2026 CoinSpot-specific debanking event found.** Either it hasn't happened or it wasn't reported.

## Section 4: Orchestrator classification

**`None detected (direct integrations — greenfield)`.** No orchestrator evidenced. Searched `CoinSpot "payment orchestration"` and CoinSpot against Juspay, Primer, Spreedly, Gr4vy, Payrails and Yuno — nothing.

⚠️ **Reasoned caveat rather than a default:** for a licensed exchange an in-house treasury/payments function is the norm, and the deposit flow redirects to an externally hosted portal. **What the evidence supports is: no third-party orchestrator, no visible routing or cascade layer, and a manual customer-driven fallback between rails. It does not support a claim that there is no internal payments team.**

## Section 5: Entities, regulation & financials

- **Casey Block Services Pty Ltd** — the operating entity. **AFSL 562554** reported, granted 29 April 2026, **for non-cash payments** `[UNVERIFIED on the number]`. **AUSTRAC DCE registration.** **Russell Wilson** reported as founder/CEO.
- CoinSpot is **private**, so filings are thin. Trading volume reported at **~A$200m/day** as at Nov 2023 `[UNVERIFIED — search summary]`.
- **The 2023 hack:** ~A$2.4m reported private-key exploit. ⚠️ **This is a security incident, not a payment-rail incident. Do not use it as a payments hook.**

## Section 6: Buying signals

1. **🔑 The AFSL for non-cash payments (April 2026)** — they are building regulated payment product (AUD wallet, CoinSpot Mastercard). **A company that just acquired a payments licence is thinking about payments.**
2. **Apple Pay and Google Pay launched 26 May 2025** — recent rail additions, both app-only, both capped at A$5,000.
3. **The CoinSpot Mastercard** — issued via **EML** (the one enabler name that surfaced, and only for the card, not the deposit rails).
4. **Australia's incoming DAP licensing regime** — ⚠️ verify current status live before citing.
5. **Major sports sponsorships** — a marketing-spend signal, i.e. they are in acquisition mode, which is consistent with zero-rating card deposits as a subsidy.

⚠️ **Not established:** payments/engineering job postings · leadership changes beyond the founder · any 2024–2026 debanking event · any public payment RFP.

## Section 7: ICP Score — 15 / 29 → 🟢 Medium

| Signal | Max | Score | Evidence |
|---|---|---|---|
| Transaction volume | 5 | **3** | **~53,000–135,000 fiat deposits/month DERIVED** on two independent methods; 2.648M visits and 3M registered users. **No sourced transaction count exists** |
| Orchestration posture | 4 | **4** | **Greenfield** — no orchestrator, no routing or cascade layer, customer-driven manual rail fallback |
| Operates 3+ countries | 3 | **0** | ⬜ **Deliberate zero.** **Single market.** AUD only, Australian accounts only, no international bank account offered |
| Multiple PSPs in parallel | 3 | **3** | **Genuinely fragmented** — an unidentified NPP/PayID enabler, an unidentified card gateway (hosted portal), **PayPal**, **Blueshyft** for cash, and **EML** for the Mastercard. Five distinct providers ⚠️ **three of them unidentified** |
| Local rail gap in a top market | 3 | **3** | **PayTo NOT FOUND** (verified against their own help-centre API) · **BPAY not offered** · **POLi discontinued 2023** · and **no Osko/NPP OUTBOUND payout at all** — instant in, T+1 out |
| Recent market expansion | 2 | **0** | ⬜ **Deliberate zero.** Single market, no new geographies. The AFSL and the new wallets are *product* expansion, not market expansion |
| Known payment issues | 2 | **2** | **CoinSpot publicly documents issuer-driven card-deposit declines** — *"Your banking institution does not allow Debit/Credit card deposits to cryptocurrency exchanges"* — **and instructs customers to switch rails manually.** Plus *"Unavailable for this merchant"* and PayID security holds |
| Recent funding | 2 | **0** | ⬜ Private, no raise found |
| Traffic outside home market | 2 | **0** | ⬜ **Deliberate zero.** 90.04% Australia |
| Competitor on orchestration | 2 | **0** | ⬜ Not found — no Australian DCE peer evidenced on an orchestrator |
| Payment job postings | 1 | **0** | ⬜ Not established |
| **TOTAL** | **29** | **15** | 🟢 **Medium** |

**Six deliberate zeros.** A concentrated single-market account — the matrix rewards geographic complexity and CoinSpot has none. **What it has instead is a published fee table that proves they absorb all card acceptance cost, a published admission of issuer-driven declines, two documented rail-loss events, and no outbound real-time payout.** Those are concrete and quotable.

## Section 8: Outreach Angles, Ranked

1. **They absorb 100% of card acceptance cost** — card, Apple Pay, Google Pay and PayPal deposits are all **FREE to the user**, while **cash is priced at 2.5%**, proving they will price a rail when they choose to. **Zero-rating cards is a deliberate acquisition subsidy, and it sits entirely in their P&L.**
2. **The A$5,000/24h cap on card rails vs NO LIMIT on PayID and Direct Deposit.** Free rails get unlimited headroom; card rails get capped. **That gap is the cost and risk containment, visible from outside.**
3. **They publicly document issuer-driven card declines and tell customers to switch rails by hand.** A cascade automates exactly that.
4. **Instant in, T+1 out** — no Osko/NPP outbound, no PayTo, no real-time withdrawal, a 2pm AEDT cutoff, weekends excluded, plus a manual risk-hold in the payout path and no reservation of funds.
5. **Two documented rail-loss events** — fully off-ramped in 2018 and had to find a new banking partner; **POLi killed with ~7 days' notice, which they themselves described as "outside of CoinSpot's control."**
6. **PayTo absent** while PayID is live — the mandate rail is missing, same structural gap as Virgin Australia in this batch.
7. **The published PayPal withdrawal fee contradicts itself** — 2% on `/fees` vs *"2% capped at $1.25"* in the help centre.

## Section 9: Do NOT Say

- ❌ **Any card deposit fee.** It is **FREE**. The 1.88% and 1.22% figures circulating online are wrong, and **the 1.88% source is a scam page with a fake support number.**
- ❌ **That PayTo, BPAY or POLi are live.** PayTo not found, BPAY not offered, POLi dead since 28 Sep 2023.
- ❌ **Any named NPP enabler, acquirer or gateway** — Monoova, Zepto, Zai, Cuscal, Stripe, Adyen. **None is evidenced.** EML is evidenced **only** for the Mastercard.
- ❌ **The 2023 hack as a payments hook.** It was a private-key security incident, not a payment-rail failure.
- ❌ **Cross-border approval rates or APAC corridor framing.** 90.04% domestic, AUD only.
- ❌ **Any DAP licensing deadline from memory.** Verify live.
- ❌ **"3 million users" as a hard figure** — it is marketing copy on their own fees page.
- ❌ **Crypto deposits and fiat deposits interchangeably.** Only fiat is orchestratable.
- ❌ **Confusing CoinSpot with Coinbase, CoinJar, Swyftx, Independent Reserve or BTC Markets** — several are Australian competitors and results cross-contaminate badly.
- ❌ **Treating a single review as a pattern** — review sites host incentivised reviews.

## Section 10: Research Confidence

**Overall: HIGH on published fees, rails and documented failure modes. ZERO on the providers behind them.**

- ✅ **Verified first-hand by me:** `https://www.coinspot.com.au/fees` (HTTP 200, 45,697 bytes) and the complete fee table extracted line-by-line — PayID Free, Direct Deposits Free, **Cash 2.5%**, **Card Free**, PayPal Free, Bank Withdraw AUD Free, PayPal Withdraw AUD 2% — plus the *"Join 3 million other users"* string.
- ✅ **Primary sources:** CoinSpot's own Zendesk help centre throughout — the AUD Deposit FAQ (created 2019-02-12, **updated 2026-09-30**), AUD Withdrawals FAQ (updated 2026-08-23), the card/Apple Pay/Google Pay/cash/PayPal/PayID/Osko deposit articles, the POLi discontinuation notice, and the AFSL announcement. **A help-centre API query was used to establish PayTo's absence across 31 results** — a genuine negative, not a failed search.
- ⚠️ **Blocked:** one fetch returned 403; the live deposit flow sits behind login so **no checkout or BSB could be read**.
- ⚠️ **Unresolved:** the **NPP/PayID enabler** · the **card acquirer/gateway** (an unbranded hosted portal) · whether any internal routing exists server-side · tokenisation approach · MDR, approval and decline rates, chargeback levels · PCI posture · payments job postings · any 2024–2026 debanking event · the AFSL number from a primary ASIC register (it rests on a search summary) · ProductReview.com.au, Reddit r/CoinSpot and r/AusFinance and Whirlpool were **not retrieved** — complaint sentiment is therefore **not covered**, and the documented help-centre failure modes are better evidence anyway.

</details>
