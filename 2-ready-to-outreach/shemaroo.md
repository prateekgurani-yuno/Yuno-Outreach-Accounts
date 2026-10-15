# Shemaroo Entertainment (ShemarooMe)

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 20 / 29 → ⭐ by the matrix, **overridden DOWN to 🟢 Medium Priority** (see override note)
**Industry:** Media & entertainment — Hindi, devotional and regional content; ShemarooMe is the SVOD service · **HQ:** **Mumbai, India** — `Shemaroo Entertainment Limited`, CIN `L67190MH2005PLC158288`, **BSE 538685 / NSE SHEMAROO** · **Researched:** 2026-10-15 · **First email sent:** —
**Motion:** ⚠️ **DISPLACEMENT** — **Juspay is confirmed in production code on the India path.** But there is an **in-house switch sitting above it**. Both constraints bind. Read the two boxes below before writing a line.

---

> ## 🔀 THE MOTION — the TAL row was right, and three of four agents got this wrong
>
> Our target list carried `Payment Orchestrator = Juspay` as an unverified lead. **It is correct**, and I verified it
> myself in served production code:
>
> ```js
> localStorage.setItem("payment_mode_in", "juspay")
> Netcore_Subscription_Checkout('juspay', [...], response, total_price_charged, ...)
> ```
>
> **Reproduced across three independent Indian IPs** (`49.36.0.1`, `103.21.58.1`, `117.200.0.1`) on
> `https://www.shemaroome.com/plans`, each returning ~219,5xx B with dial code `+91`.
>
> ⛔ **Why this nearly got recorded as "greenfield".** `shemaroome.com` is **geo-variant**, and every research agent
> on this run egresses from the **US**. All three that looked at the checkout saw `payment_mode_in = "stripe"` and
> reported **`juspay` = 0**, concluding the TAL row was stale. One stated it as *"refuted on all available evidence."*
> **They were reasoning correctly from a render that does not exist in India.** I only found it because I forced the
> geo with an `X-Forwarded-For` header, which this origin honours.
>
> **The generalisable lesson, logged:** on a geo-routed merchant, a US-egress agent fleet cannot see the home market's
> payment stack. Absence of a vendor token from a US render is not absence from the merchant.
>
> ⚠️ **Honest limit.** Juspay is confirmed **present and current on the India web checkout**. I did **not** establish
> which Juspay products are in use, when it went live, or whether it also serves the apps. There is **no Juspay case
> study, press release or merchant-list entry naming Shemaroo** — four separate search angles found nothing. The
> confirmation rests entirely on production code, which is strong evidence of presence and silent on scope.

> ## 🎯 THE HOOK — a hand-rolled switch with six legs, and the paying markets it cannot reach
>
> **Juspay does not orchestrate this business. Shemaroo's own front-end does, and Juspay is one branch of it.**
>
> The live switch variable is `payment_mode_in`. I verified **six distinct values** across the served page and the
> 426,689 B application bundle (control: a nonsense bundle path returns 3,521 B):
>
> | Value | Scope | Evidence |
> |---|---|---|
> | `juspay` | **India** (67.27% of traffic) | `/plans`, India geo, 3 IPs |
> | `stripe` | **26 allowlisted countries** | `/plans`, US/AU geo + `js.stripe.com/v3/` |
> | `lazypay` | India BNPL | **43 hits** in bundle, own `/payment/lazypay_response` route + bespoke OTP flow |
> | `unifi` | **Telekom Malaysia** telco billing | 4 hits, own `/payment/unifi_response` route + own OTP flow |
> | `coupon` | 100%-off path | `/plans` |
> | *(Razorpay)* | site-wide script tag | `checkout.razorpay.com/v1/razorpay.js` on every page |
>
> **Each leg has its own callback route and its own hand-written OTP/redirect code.** That is per-gateway integration
> code, written and maintained in-house, on top of an orchestrator they already pay for.
>
> ### And the geography is the sharp end
>
> `/plans` carries a hidden input, `stripe_regions`, with an **explicit 26-country allowlist**:
>
> ```
> AU, NZ, SG, US, CA, GB, AT, BE, CY, EE, FI, FR, DE, GR, IS, IE, IT, LV, LT, LU, MT, NL, PT, SK, SI, ES
> ```
>
> India routes to Juspay. These 26 route to Stripe. **Everywhere else gets neither.** I probed eight markets and
> read the rendered plan ladder in each:
>
> | Market | Traffic | Routed to | Plans rendered |
> |---|---|---|---|
> | 🇮🇳 India | **67.27%** | **Juspay** | ₹299/qtr · ₹499/yr · ₹699/2yr — **enabled** |
> | 🇺🇸 US | 3.32% | **Stripe** | $8.99/mo · $12.99/qtr · $34.99/yr · $49.99/2yr — **enabled** |
> | 🇦🇺 Australia | 2.02% | **Stripe** | AUD 19/qtr · AUD 49/yr — **enabled** |
> | 🇵🇰 **Pakistan** | **8.05% ▲24%** | **none** | PKR 299/mo · 800/qtr · 1500/yr — **ALL `disabled`** |
> | 🇧🇩 Bangladesh | 2.06% | **none** | BDT 3/day · 20/wk · 80/mo · 150/qtr · 250/6mo · 400/yr — **ALL `disabled`** |
> | 🇸🇦 Saudi Arabia | 1.52% ▲**379%** | **none** | SAR 39/qtr · SAR 120/yr — **ALL `disabled`** |
> | 🇦🇪 UAE | 1.29% | **none** | AED 3.25/day · 15/wk · 30/mo — **ALL `disabled`** |
> | 🇱🇰 Sri Lanka | 0.61% | **none** | LKR 999/qtr · LKR 1990/yr — **ALL `disabled`** |
>
> **Somebody priced all of this.** Bangladesh has a six-tier ladder down to **BDT 3/day**; UAE has **AED 3.25/day**.
> That is deliberate micro-pricing for low-ARPU, high-frequency markets — built, localised, and switched off on web.
>
> Their own FAQ says what happens instead, verbatim and live:
>
> > **"How can I Subscribe outside India and US region?"**
> > *"Outside India and the US region, there are two ways to purchase a subscription. Customers can subscribe on
> > Android devices **via Google Play**. iOS customers can purchase a subscription **through the App Store**."*
>
> **~13.5% of traffic — a bloc larger than the ~10.6% that Stripe serves — is handed to Apple and Google at 15–30%.**
>
> ⚠️ **The honest counterweight, and it is substantial.** Shemaroo is **not** ignoring these markets — it monetises
> them through **direct carrier billing** instead. Verified press: Feb 2024 added **Zain, STC, Mobily (Saudi)** and
> **Vodafone (Qatar)** via DCB partners **3A net** and **One97 Communications**, claiming ~29 telco operators across
> SEA, SAARC and MENA; an Aug 2023 round added **Batelco, Grameenphone (Bangladesh), XL Axiata, Ooredoo**. **That is
> almost certainly the Saudi ▲379% explanation.** So the argument is **not** "you cannot collect" — it is
> **"you collect through the most expensive rails available."**
>
> **Pakistan is the exception that survives the counterweight.** 8.05% of traffic, growing 24%, the #2 market —
> and **no named telco partner, no local rail, no enabled web plan.** Two agents searched; neither found a Pakistani
> operator in any DCB release. The Feb 2024 release says "SAARC", which *could* include Pakistan, but **no source
> names a Pakistani carrier.** That gap is the single cleanest hook in this file.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Shemaroo Entertainment is a BSE/NSE-listed Mumbai media company (Hindi film, devotional and regional
content) whose SVOD service **ShemarooMe** runs a six-leg, hand-built payment switch — Juspay for India, Stripe for
26 allowlisted countries, LazyPay, Telekom Malaysia's unifi, Razorpay site-wide, and a coupon path — with Apple IAP,
Google Play user-choice billing and ~29 telco DCB operators beside it.

**The three facts that matter:**
1. **Juspay is in, on India (67% of traffic).** Confirmed in production code, reproduced across three Indian IPs.
   Never pitch the case for orchestration.
2. **The orchestrator is one branch of Shemaroo's own switch**, which has five other hand-wired legs with bespoke
   callback routes and OTP flows. The opportunity-cost argument is real and evidenced.
3. **Pakistan — the #2 market at 8.05% and growing 24% — has priced plans rendered `disabled`, no local rail and no
   named carrier partner.** Verified in their own served markup.

**Financial context that shapes the conversation:** FY26 consolidated revenue **₹589 cr, net loss ₹218 cr** (2.6×
wider YoY), borrowings **~₹300 cr** against a **₹416 cr** market cap, a **₹192 cr** disputed GST demand, and a
**CARE Ratings downgrade in March 2026**. Digital is the only growing line (+6.65% 9M-FY26 while traditional fell
17.59%). **Read it as a trigger, not a blocker:** they are under instruction to grow digital revenue while cutting
cost, which is exactly where MDR reduction and recovered failed payments land.

**Primary contact:** **Saurabh Srivastava — Chief Operating Officer, Digital Business** (titled exactly this, and the
quoted spokesperson in the Feb 2024 DCB release). No CTO, CPO or payments-specific role surfaced for this company.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Shemaroo` to draft the 12-touch sequence.*

⚠️ **Six hard constraints:**
- **Motion is DISPLACEMENT.** Juspay is in production on India. **Never make the case for orchestration itself** and
  never open with "you have no orchestration layer" — it is factually wrong and burns the thread.
- **But also respect the in-house build.** They wrote a six-leg switch by hand. Anchor on **opportunity cost and
  reach**, not on the build being a mistake.
- **Never name Juspay, LazyPay, Stripe, Razorpay or Adyen** in outreach-facing text. Say "your orchestration layer",
  "your routing".
- **Do NOT claim they cannot collect in Pakistan/Gulf/Bangladesh.** They collect via carrier billing. The argument is
  **cost of acceptance and margin**, not absence. Getting this wrong is the easiest way to be factually corrected on
  email one.
- **Do NOT quote a price or a subscriber number.** India INR pricing has two conflicting reads, and management has
  stated on the record they do not disclose subscribers. The `disabled` plan ladders ARE quotable — I verified them.
- **Do not lead with app-store fees to a company this leveraged** without pairing it to the DCB cost story; the
  Apple-locked share is real but unquantified.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 20 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **2** | ⚠️ **ASSUMED — not sourced, not soundly derived.** Scored at the lowest non-reject tier deliberately. See disclosure below. |
| Orchestration status | **3** | ✅ **Regional orchestrator (Juspay) confirmed in production code**, India path, 3 independent IPs — displacement, short education cycle |
| 3+ countries | **3** | ✅ Enabled checkouts in India + 26 Stripe-allowlisted countries; entities in India, **US** and **UAE**; ~29 telco DCB markets; FAQ claims availability in "more than 200 countries" |
| Multiple PSPs | **3** | ✅ **Six legs**: Juspay, Stripe, Razorpay, Adyen (named in Terms), LazyPay, unifi — each independently evidenced |
| Local rail or licensing gap in a top-3 market | **3** | ✅ **Pakistan is the #2 market (8.05%, ▲24%) with zero local rails.** No JazzCash, Easypaisa, 1LINK or Raast; web plans priced in PKR and rendered `disabled`; no Pakistani DCB partner found by two agents |
| Recent expansion | **2** | ✅ **ShemarooVerse Digital Limited (UAE) incorporated 04.02.2025**; Aikyam Entertainment 08.05.2025; DCB expansion Feb 2024; Plans Page redesign shipped **11 Aug 2026** |
| Payment issues | **2** | ✅ **Specific and diagnostic, honestly moderate.** 28 of 616 Apple reviews (4.5%) carry hard payment-failure language; "amount debited, subscription not activated" ×6 in India 2023→2025; one double-charge across two rails; 5× cancelled-but-still-charged. Play: **13.4% one-star** (5,113 of 38,246) |
| Funding >$10M | **0** | ❌ No round. Loss-making listed company; the only raise was a **₹15.51 cr preferential allotment converting promoter debt** (Mar 2026) |
| High traffic outside home | **0** | ❌ **India 67.27%**, above the 60% threshold. Scored 0 despite the diaspora story — the row does not fire |
| Competitor using orchestration | **2** | ✅ **YuppTV has Juspay confirmed in production code — our own repo, 15/24 ⭐.** A direct Indian-OTT peer. SonyLIV listed as a Juspay client on a third-party vendor profile `[UNVERIFIED]` |
| Payment job postings | **0** | ❌ **Two agents searched; no Shemaroo job posting of any kind was reached.** No careers host located. Scored 0 rather than inferred |

**Matrix tier: ⭐ High Priority (17+).**

### ⚠️ ANALYST OVERRIDE — DOWN to 🟢 Medium Priority

**Applied on one ground only: the volume gate is not demonstrably met, and the honest range straddles it.**

Yuno's minimum is 40,000 transactions/month. The figure here is **ASSUMED**, and the pessimistic case falls below.
The strongest independent check is unflattering: **Shemaroo Media & Entertainment LLC — the entity its own Terms
name as the operator — had total FY26 turnover of ₹761.82 Lakhs (₹76.2 Mn).** At the US annual price of $34.99 that
is **~26,000 annual subscriptions ≈ 2,200 charges/month**; even all-monthly at $8.99 is **~8,500/month**. The entire
international leg cannot clear 40,000 on its own, so the gate rests wholly on India — where the web plan ladder has
**no monthly option** (minimum quarterly) and the page actively upsells to annual (*"Pay just ₹250 more to get a
yearly subscription"*), both of which **minimise** transaction count.

**What I explicitly did NOT override on:**
- **Financial distress is not a downgrade reason here.** Widening losses, a credit downgrade and digital as the only
  growing line mean they are being told to grow digital revenue while cutting cost. That is a buying trigger.
- **The app-store trap does not void this account.** Shemaroo runs **Google Play user-choice billing** and presents
  its own checkout as a selectable alternative to Play Billing on its own plans page. A company does not enrol in
  that programme unless it wants transactions on its own stack. See Section 8.

### Monthly transaction count — MANDATORY DISCLOSURE

**Verdict: ASSUMED.** Not SOURCED. Not DERIVED.

**Billing unit:** one subscription charge per plan period per subscriber, on auto-renewal. Confirmed verbatim in the
Terms of Use: *"you authorize us to charge your subsequent period's membership fee to your Payment Method, **on an
auto-renewal basis**"*.

**Why not DERIVED.** A derivation needs ShemarooMe's subscription revenue or its subscriber count. **Neither exists
publicly, by policy rather than oversight.** From the June 2026 earnings call transcript:

> **Analyst:** do you publish DAUs/MAUs/paid or total subscribers?
> **Hiren Gada (CEO):** *"**No, we have not been. And at this point, at least we don't intend to.**"*
> **Arghya Chakravarty:** *"we **don't give out any of the numbers on Shemaroo**[Me]. But it is a very strong revenue
> trajectory is all we can say."*

The filings cannot close the gap either. AR 2025-26 note 34.2: *"The Group has identified "Entertainment" as the
**only primary reportable business segment**"*. Advertising and subscription are **fused into one line item**
(₹37,455.35 Lakhs FY26). The quarterly deck's "Digital Media" division (₹2,082 Mn, 9M-FY26) explicitly comprises
**Digital Syndication + YouTube + Facebook + ShemarooMe** — and the AR notes Shemaroo runs *"more than 100 channels
on YouTube garnering more than 100 mn views a day"*, so YouTube AVOD plausibly dominates it. **ShemarooMe's share of
that division is the unsourced input that breaks every derivation.**

**Inverted instead of invented — what would ShemarooMe have to be to clear the gate?**
Breakeven = 480,000 charges/year.

| Plan mix (ASSUMED) | Revenue needed/yr | As % of annualised Digital Media (₹2,776 Mn) |
|---|---|---|
| 100% annual @ ₹699 | ₹336 Mn | **12.1%** |
| 100% annual @ ₹499 | ₹240 Mn | **8.6%** |
| 50/50 annual–monthly | ~₹100 Mn | ~3.6% |
| 100% monthly @ ₹199 | ₹96 Mn | ~3.4% |

**So ShemarooMe needs to be ~9–12% of Digital Media revenue on an all-annual mix, or ~3–4% on a monthly-heavy one.**
`[ESTIMATE, not confirmed]` The only published growth datapoint — AR 2025-26: ShemarooMe *"recording **over 30%+
year-on-year growth**"* — **is a rate with no base and bounds nothing.**

**Bottom line: plausibly 40,000–100,000 charges/month across all rails, but no point estimate is defensible, and a
credible pessimistic case falls well below.** The deciding variables are the India plan mix and ShemarooMe's share of
Digital Media. **Both are discovery questions for a call, not desk research.** The gate did **not** fire — the rule is
that only a sourced or soundly-derived sub-40k figure rejects, and an assumption never does.

---

## Section 1: Website Traffic Analysis by Country

Full record: `accounts/traffic/shemaroo.md`. **SimilarWeb, supplied by Prateek 2026-10-15**, Jul–Sep 2026,
all-country-domains **ON**, 68 countries. Total visits and global rank were not in the supplied view.

India **67.27%** ▼9.80% · **Pakistan 8.05% ▲23.96%** · US 3.32% ▲19.37% · Bangladesh 2.06% ▼22.07% · Australia
2.02% ▼52.15% · UK 1.90% · Canada 1.52% · **Saudi Arabia 1.52% ▲379.00%** (00:06:14, 7.08 pages, 22.99% bounce —
the deepest engagement in the dataset) · UAE 1.29% · Germany 0.90% · South Africa 0.66% · Sri Lanka 0.61% · France
0.48% · Netherlands 0.44% · Singapore 0.42% · Nepal 0.41%.

**Two reads that matter.** India at 67.27% is **above** the 60% ICP threshold, so the outside-home row scores 0 —
though India is falling while Pakistan and the US rise, so it may fire on the next pull. And **Australia is down
52.15% in a market that has an enabled Stripe checkout** — cause unknown, not investigated, flagged so it is not
mistaken for a payment problem.

## Section 2: Legal Entities & Local Presence

**Parent:** Shemaroo Entertainment Limited, CIN `L67190MH2005PLC158288`, Shemaroo House, Plot No. 18, Marol Co-op
Indl. Estate, Off Andheri Kurla Road, Andheri (E), Mumbai 400059. BSE 538685 / NSE SHEMAROO.
Officers: **Raman Maroo** (Chairman & MD, DIN 00169152), **Hiren Gada** (WTD & CEO, DIN 01108194), **Amit Haria**
(CFO), **Meenakshi A. Pansari** (Company Secretary). Source: AR 2025-26, board-approved 16 May 2026.

**Complete subsidiary list, Form AOC-1, FYE 31 Mar 2026** (INR Lakhs). The AOC-1 states no subsidiary was liquidated
or sold during the year, so this is exhaustive:

| Subsidiary | Jurisdiction | Reg. No. | Incorporated | Turnover FY26 | PAT FY26 | Holding |
|---|---|---|---|---|---|---|
| Canopy Entertainment Pvt Ltd | India | U22130MH2012PTC237345 | 30.12.2012 | 28.98 | (9.36) | 100% |
| Shemaroo Contentino Media LLP | India | AAE-6434 | 29.10.2015 | 3,108.27 | 168.36 | 72.50% |
| Aikyam Entertainment Pvt Ltd | India | U64100MH2022PTC467115 | 08.05.2025 | 3,464.94 | (20.91) | 100% |
| **ShemarooVerse Digital Limited** | **UAE** | 9893 | **04.02.2025** | nil | (5.24) | 100% |
| **Shemaroo Media & Entertainment LLC** | **USA** | 0450263305 | 24.04.2018 | **761.82** | 301.70 | 100% |

⚠️ **No UK, Singapore, Canada or Australia entity exists** as at 31 Mar 2026 — despite enabled Stripe checkouts in
all four. A 2019 disclosure reportedly listed a UK entity; it is absent from the FY26 list and I did not source its
wind-up. **Do not claim a UK entity.**

### ⭐ The billing entity — and a documentation gap worth noting

**I fetched the Terms of Use under both India and US geo. They are byte-identical (241,830 B).** The Terms are
**not** geo-variant, which resolves an open question from the entities agent. Verbatim:

> *"This Terms of Use... describes the terms and conditions applicable to your access and use of all services,
> website and Apps operated by **Shemaroo Media & Entertainment LLC.** and/ or its affiliates..."*

So **Indian subscribers contract with the US LLC**, under **New Jersey** jurisdiction (4 mentions). The Indian parent
appears only in the footer copyright line. And on payments:

> *"**E. Payments and Termination:** We currently use **Adyen** as the third party service provider for payment
> services (e.g. card acceptance, merchant settlement, and related services)."*

⚠️ **`Razorpay` = 0, `Juspay` = 0, `Stripe` = 0 in the entire Terms document, under both geos.** The legal
documentation names **one** PSP; production code runs **six** legs and does not include a single Adyen SDK. **The
customer-facing legal terms are materially out of step with the live stack.** That is an observation about their
documentation, offered as a factual asymmetry — not a compliance allegation, which I am not qualified to make.

## Section 3: Payment Providers & Payment Stack

| Vendor | Evidence | Scope | Confidence |
|---|---|---|---|
| **Juspay** | `payment_mode_in = "juspay"` + `Netcore_Subscription_Checkout('juspay',...)` on `/plans`, **3 Indian IPs** | **India** | **High** — me, first-party |
| **Stripe** | `<script src="https://js.stripe.com/v3/">`, `stripe_client_secret`, `stripe_pub_key`, `#stipe_section`, `#payment-request-button` | **26 allowlisted countries** | **High** — me, first-party |
| **Razorpay** | `<script src="https://checkout.razorpay.com/v1/razorpay.js">`, served site-wide | Site-wide; India presumed | **High** — me, first-party |
| **Adyen** | **Named as sole PSP in the Terms**; `adyen.png` (695 B, the Adyen wordmark — I rendered it); API field `adyen_disc_amount` → `first_purcahse_us_promo_disc_amt`; `#adyenzip_code` AVS input | International/US cards | **High that it is present; current-vs-legacy UNRESOLVED** |
| **LazyPay** | **43 hits** in the 426,689 B bundle; `payment_gateway=lazypay`; `/payment/lazypay_response`; `#lazypay_otp_confirm` flow | India BNPL | **High** |
| **unifi (Telekom Malaysia)** | `payment_gateway=unifi`; `/payment/unifi_response`; `/plans/otm_otp_valid`, `/plans/otm_resnd_otp` | Malaysia telco billing | **High** |
| **Apple IAP** | App Store listing, seller "Shemaroo Entertainment Ltd.", bundle `com.shemaroo.shemaroome` | iOS global | **High** |
| **Google Play Billing** | User-choice billing selector on `/plans`; `com.saranyu.shemarooworld` | Android global | **High** |
| **DCB: 3A net, One97, TimWE, Boost Connect, SLA Digital** | Two fetched press releases (Feb 2024, Aug 2023) | ~29 telcos, SEA/SAARC/MENA | **High** |
| **Amazon Pay** | Apr 2020 partnership (fetched); Login-with-Amazon SDK live in shell; `amazon_pay.png` icon; `type=amazon` deep-link | India wallet | **Confirmed 2020; current checkout status inferred** |
| **PayPal** | `#ad_paypal` → `/users/add_bank_account`, US-region-gated | **PAYOUTS, not checkout** | **High — do not list as a checkout method** |

⚠️ **Adyen: current or legacy — UNRESOLVED and it should stay that way in outreach.** Arguments both ways: the icon
is live in a customer-facing accepted-payments strip (merchants prune those), and the Terms name Adyen exclusively;
against that, the live switch writes `stripe`/`juspay`, no Adyen SDK loads anywhere, and `#adyenzip_code` duplicates
`stripe_billing_address`. **`web.archive.org` is blocked by the egress proxy**, which closed the one method that
would have dated it. Zero co-occurring search results tie Shemaroo to Adyen or to Stripe publicly.

**PCI DSS / tokenization: No public information found.** Zero results mentioning Shemaroo.

## Section 4: Alternative & Local Payment Methods

**Authoritative first-party source — the live `/faq`, verbatim** (I verified this sits in live markup, not inside an
HTML comment; large parts of that page are commented-out dead content):

> *"**Android Phones and on the Web**, there are multiple options available as follows: **UPI | Paytm | Credit Card |
> Debit Card | Amazon Pay | Mobikwik | Net Banking**"*
> *"**iOS:** To purchase a plan from the iOS platform, subscribers can do so through the Appstore."*
> *"**TV Platforms:** Indian customers can buy ShemarooMe plans on Mi TV & Android TV… pay via **Paytm**."*

| Market | CONFIRMED | NOT FOUND |
|---|---|---|
| **India** | UPI · Cards · Netbanking · Paytm · Amazon Pay · Mobikwik · LazyPay · coupons · gift-a-sub · voucher redemption | **UPI Autopay** · **RuPay** · **PhonePe** · e-mandate / eNACH / SI · EMI · Freecharge |
| **Pakistan** | *(nothing)* | **JazzCash · Easypaisa · 1LINK/1BILL · Raast** — zero occurrences anywhere |
| **Bangladesh / Sri Lanka / Nepal** | *(nothing on own checkout)* | bKash · Nagad · any local rail |
| **Saudi / UAE** | DCB via Zain/STC/Mobily | **mada** — zero occurrences (checked for the `nomada`/`llamada` false positive; there were no hits at all) |
| **Global** | — | **PayPal checkout · Apple Pay · Google Pay** (the wallets — distinct from Apple IAP / Google Play, do not conflate) |

⭐ **UPI Autopay is absent, and this is the highest-leverage single gap in India.** Zero hits for `autopay`,
`mandate`, `recurring` or `e-mandate` in live markup. The only "Remove Autopay" string on `/faq` **sits inside an
HTML comment** — dead content. For a subscription business where 67% of traffic is India, UPI Autopay is the local
recurring rail and it is not visible anywhere.

⚠️ **But do not conclude they have no auto-renewal — one agent did and it is wrong.** I verified a live FAQ answer,
*"How do I cancel the Auto-renewal payment of my subscription plan?"*, describing a self-serve flow **on the
ShemarooMe account itself** (Profile → Account details → View active plans → unsubscribe), separate from the iTunes
path. Auto-renewal exists on their own rail. What is missing is any **named UPI Autopay / e-mandate mechanism** —
so how they satisfy RBI e-mandate (registration, AFA, pre-debit notification) on India card renewals is **unknown,
and is an excellent discovery question.**

**False positives I cleared:** `emi` → all 13 hits on `/faq` are **"Premiere"**. `upi` → verified in payment context
only. `visa` → only `visa.png`/`mastercard.png` icon filenames, no immigration noise. `mada` → zero hits at all.

## Section 5: Payment Issues & Customer Complaints

**Method and honest denominator:** Apple customer-review RSS for `id=1439041310`, with `id=1439041310` verified in
every feed's `rel="self"` link. **616 unique reviews** across six storefronts (India 500, US 60, Canada 28, Australia
14, UK 13, Saudi 1). **28 (4.5%) contain hard payment-failure language.** That is the real base rate — this is not a
platform in open revolt, but the failure *modes* are specific.

| Issue | Platform | Frequency | Range | Quote |
|---|---|---|---|---|
| **Amount debited, subscription not activated** | iOS India | **Moderate — 6 distinct dated instances in 500** | Apr 2023 – Apr 2025 | *"money deducted from my account but still account shown as inactive… they say that send screenshots… after 4 days that still not activated"* |
| Same, explicitly **UPI** | iOS India | isolated | Sep 2024 | *"the payment has been successful through UPI app, the money has not been credited to the app"* |
| ⭐ **Double charge across two rails** | iOS India | isolated but **mechanistically the most valuable in the set** | Mar 2025 | *"I subscribed through web and paid through phone pe and money was deducted but when I logged in to mobile app it was still showing plan not activated and I paid through apple. Now it's showing same 2 active plans and I am charged twice"* |
| Cancelled but still charged | iOS IN + UK | Moderate (5) | Oct 2023 – Jun 2026 | *"they cut money three times after Cancellation"* (UK) |
| Refund friction | iOS IN/US/CA | Moderate (7+) | 2021 – Aug 2026 | *"also not mentioned refund policy in FAQ"* |

⭐ **The double-charge complaint is corroborated by their own data model.** The analytics payload carries
`active_plan_end_date_1`/`active_payment_mode_1` **and** `..._2`/`active_payment_mode_2` — **two simultaneous plans
with two different payment modes is a first-class concept in their schema.** That is exactly the state the reviewer
ended up in, and it is the predictable consequence of six uncoordinated payment legs.

**Cross-border failures, flagged separately:** 8 instances outside India — US *"unable to purchase subscription as is
linked to another user"*, Canada *"Paid 1 year subscription for nothing… Can't even ask for money back"*, UK
*"I ll be raising a complaint via my card and consumer court"*, Australia *"Paid for one year not working at all"*.

**Counter-evidence, for honesty:** three reviewers praised refunds/auto-renew handling by name (Namrata, Puneeth,
Hemanth). **Support can fix these; the product cannot self-serve them.**

**Google Play:** 4.2★, **38,246 ratings, 5,113 one-star (13.4%)**, 20,349 written reviews, 10M+ installs (raw
**18,010,284**), "Contains ads", updated 11 Aug 2026. ⚠️ **No Play review text was obtainable** — it loads by XHR.
**The carousel trap is severe on that page:** the largest embedded blob (67,573 B) contains **no ShemarooMe data at
all**, only SonyLIV, Sun NXT, Hungama, aha, Lionsgate and `com.shemaroo.shemarootv` (a *different* Shemaroo app).
I independently re-ran this myself: **all seven IAP price tiers on the page sit at byte offsets 1.12M–1.21M, inside
the carousel region, while ShemarooMe's own data clusters at ~927K.** None of those tiers is ShemarooMe's.

**No complaints found on Reddit, Trustpilot, MouthShut, consumercomplaints.in or X** — three searches. Record as
"no public information found", **not** as low complaint volume.

## Section 6: Corporate & Payment Strategy Developments

**FY2025-26 (audited, FYE 31 March), AR 2025-26 + verified trade press:**

| Metric | FY26 | FY25 |
|---|---|---|
| Consolidated revenue (ops + other income) | **₹58,921 Lakhs (₹589 cr)** | ₹69,354 Lakhs |
| Consolidated net loss | **(₹21,815 Lakhs) ≈ ₹218 cr** | (₹8,447 Lakhs) |
| Borrowings (consolidated) | **₹29,973.56 Lakhs (~₹300 cr)** | ₹30,193.51 Lakhs |
| Net worth | **₹2,700 Mn** | — (₹5,818 Mn in FY22, **−54% in four years**) |
| ROCE | **(71.5)%** | — |

- **Divisional split, Q3/9M FY26 deck (NSE, filed 29 Jan 2026):** Digital Media **₹2,082 Mn 9M** (+6.65%) vs
  Traditional **₹2,354 Mn** (−17.59%). **Digital is the only growing line.**
- **Auditor Emphasis of Matter:** a **GST search operation** and resulting demand. **Contingent disputed indirect tax
  demands ₹19,186.23 Lakhs (~₹192 cr)**, unchanged YoY.
- **CARE Ratings downgrade, 25 Mar 2026** (NSE filing) `[UNVERIFIED — URL known, not fetched; verify before use]`.
- **Promoter rescue:** Mar 2026 preferential allotment, 14.10 lakh shares at ₹110, **₹1,551 Lakhs raised by
  converting unsecured debt**. Promoter holding 65.5% → 67.2%.
- **No going-concern qualification.** The phrase appears only in boilerplate. **Do not claim one.**
- CEO on digital profitability: *"the route to profitability is to build a significant base and then to reduce the
  churn… **it is some distance away**, but we are at it."*

**Leadership:**
- ⭐ **Saurabh Srivastava — Chief Operating Officer, Digital Business.** Titled exactly this and the quoted
  spokesperson on the Feb 2024 DCB release. **Primary target.**
- Zubin Dubash — COO Digital as of Apr 2020, owned *"expand our payment options"*. ⚠️ Srivastava appears to hold the
  title by 2024; **treat Dubash as likely moved on.**
- `[UNVERIFIED — search summary only]`: Abhishek Joshi (Head of ShemarooMe, Mar 2023), Abhinav Anand (VP Digital
  Video Business), **Prasanna Patil (Head of Global Telecom Business** — relevant, DCB is a telecom-billing motion).
- **No CTO, CPO or payments-specific role surfaced**, including on a surname-only fallback search. Payments most
  plausibly sits with Srivastava and Joshi.

## Section 7: Payment-Specific News

- **11 Aug 2026 — Plans Page redesign shipped.** Play release notes: *"✨ Explore our redesigned **Plans Page** with a
  fresh, intuitive look."* **Verified first-party** (control `com.saranyu.nonsensecontrolxyz123` → 404/1,673 B).
  **A checkout surface they touched eight weeks ago is a live, current hook.**
- **6 Feb 2024 — DCB round 2:** Zain, STC, Mobily (Saudi), Vodafone (Qatar); partners **3A net** and **One97
  Communications**; *"around 29 telecom providers across Southeast Asia, SAARC, and the MENA region."* Fetched.
- **~Aug 2023 — DCB round 1:** STC, Zain, Batelco, **Grameenphone (Bangladesh)**, XL Axiata, Ooredoo; partners
  TimWE, Boost Connect, SLA Digital; *~15 operators.* ⚠️ **Conflicts with the Feb 2024 figure of ~29. Do not quote a
  telco count.**
- **20 Apr 2020 — Amazon Pay**, up to 40% cashback. Zubin Dubash: *"We are excited to **expand our payment options**
  on ShemarooMe with Amazon Pay."* Fetched.
- **No gateway removal and no free↔paid model flip found. No 2025–26 payments announcement** — the payments press
  trail goes quiet after Feb 2024.

## Section 8: Checkout Experience Audit

**Completed first-party**, which was only possible after defeating two traps.

⚠️ **Trap 1 — `shemaroome.com` soft-200s nearly every URL.** The homepage, apex and a nonsense control all return
**~476,970 B with identical MD5**. Real pages are separable **only by byte-diff against a nonsense control**:
`/plans` **318,135 B** · `/faq` 291,581 B · `/terms_and_conditions` 241,830 B · `/privacy_policy` 232,456 B ·
`/about-us` 148,559 B are **REAL**; `/terms`, `/refund-policy`, `/payment`, `/checkout`, `/subscribe`, `/gift`,
`/subscription`, `/help`, `/support` are **all shell**. *(Useful: without a browser UA the control returns a clean
302 at 92 B — a cheaper control for future runs.)*

⚠️ **Trap 2 — the origin is geo-routed and honours `X-Forwarded-For`.** This is what unlocked the entire run.
US-egress agents cannot see India's stack.

⚠️ **Trap 3 — my own near-miss, logged.** My first plan extraction used the selector `class="radio-btn plan_sel"`
and returned **zero plans** for Pakistan, Bangladesh, Saudi, UAE and Sri Lanka. I was one step from writing "these
markets render no plans at all." **It was an artefact of my own selector** — those markets use a different markup
(`class="plan_sel"` without `radio-btn`) and the plans are all there, priced in local currency, **every one marked
`disabled`.** I caught it only because `PKR` returned 9 hits on a page I had just called empty. The finding survived;
the overstatement did not.

**Checkout mechanics:** redirect-to-hosted-page (`window.location = response.payment_url`). Gateway chosen
client-side via `localStorage` `payment_mode_in`. Enabled method list fetched per-request server-side
(`var chk_gateway = response.payment_modes`) — **I could not reach that array**; it needs an authenticated session.
The on-page icon strip is explicitly truncated with the literal text **"and more"**, so it bounds nothing in either
direction.

**Google Play user-choice billing — confirmed live on `/plans`**, verbatim:
> *"**Choose how to check out.** Choose who will secure and process your payment and provide customer service…
> Only purchases through Google Play are secured by Google."*

| Rail | Marks shown (India render) |
|---|---|
| **"ShemarooMe"** | upi · visa · mastercard · paytm · mobikwik · "and more" |
| **"Google Play"** | upi · visa · mastercard · discover · amex · "and more" |

**This is the single most important qualifying fact in the file.** Shemaroo has deliberately enrolled in the
programme that lets Android users **bypass** Play Billing in favour of its own rail. A company does not do that
unless it wants the transactions on its own stack. **It is a buying signal, not a disqualifier.**

**US specifics:** full state dropdown with `state_code` in the transaction payload = sales-tax collection,
corroborated by live FAQ (*"Some states in the U.S.A like New Jersey add a sales tax"*). **Roku IAP** also live in
the US.

**Accounts are hard geo-locked** (live FAQ): *"If you relocate internationally, you will not be able to access
content from your account in a different country… you will have to create a new ShemarooMe account and pay for it."*
A diaspora subscriber who moves must re-subscribe from scratch — a structural churn event.

## Section 9: PCI DSS Compliance

**No public information found.** Zero results mentioning Shemaroo for PCI DSS, "PCI compliant", tokenization or
payment security. Structurally, with Juspay/Stripe/Razorpay holding card fields and `stripe_client_secret` implying
Stripe-hosted PaymentIntent confirmation, raw PANs most likely never touch Shemaroo's servers — which is how Indian
merchants satisfy RBI's card-on-file tokenization mandate. `[INFERENCE, not confirmed]`

## Section 10: Strategic Insights & Outreach Angles

**1. The in-house switch is the opportunity-cost argument, and it is evidenced rather than asserted.**
Six legs, each with its own callback route (`/payment/lazypay_response`, `/payment/unifi_response`) and its own
bespoke OTP code — **on top of an orchestrator they already pay for.** Every new rail is a new branch, a new
callback, a new OTP flow. The cost shows up as engineering time, not as a line item. *(Cites: 426,689 B bundle,
control-tested; `payment_mode_in` values; Section 3.)*

**2. Pakistan — the cleanest single hook in the file.** #2 market, 8.05%, **growing 24%**, plans priced in PKR and
rendered `disabled`, **zero** local rails, and **no named carrier partner** after two agents searched. Every other
switched-off market has a DCB answer; Pakistan does not. *(Cites: geo probe; `stripe_regions`; DCB releases.)*

**3. The cost-of-acceptance story, stated correctly.** ~13.5% of traffic routes to Apple, Google or a telco — a
bloc **larger** than the ~10.6% Stripe serves. **Do not say they cannot collect.** Say that the markets growing
fastest are the ones collected on the most expensive rails, while the markets with their own checkout are flat or
falling. *(Cites: traffic file; `/faq` "outside India and the US"; DCB releases.)*

**4. UPI Autopay in a 67%-India subscription business.** Absent from every live surface. Pair it with the observation
that the India web ladder has **no monthly plan** — minimum quarterly — which is what a business does when it cannot
rely on a recurring rail. **Frame as a question, not an assertion**, since the server-side method array is unreachable.

**5. The asymmetry inside their own stack — the strongest available move per the voice guidance.**
**Their Terms name one PSP. Their code runs six.** Contrasting two of their own systems against each other beats any
external benchmark: they cannot dispute either half.

**6. Timing.** They shipped a **Plans Page redesign on 11 Aug 2026** — eight weeks ago. Someone owns that surface
right now and has budget attention on it.

**Strongest entry point:** the in-house switch and the Pakistan gap, framed as reach — *"you already orchestrate
India; what routes the markets growing fastest?"*

## Section 11: Similar Companies & Prospecting Pipeline

| Peer | Payment stack | Orchestration |
|---|---|---|
| **YuppTV** | **Juspay confirmed in production code** — our own repo, **15/24 ⭐**. Also a 2016 Zain Bahrain carrier-billing deal **via SLA Digital — the same DCB aggregator ShemarooMe later used** | ✅ **Juspay** |
| **SonyLIV** | Listed as a Juspay client on a third-party vendor profile | ⚠️ Likely, `[UNVERIFIED]` |
| **aha** | India: cards, netbanking, UPI, wallets; **Stripe for "International Subscribers"** — verified first-party from aha's own HTML | ❌ None found — Stripe cross-border + separate domestic rails |
| **JioHotstar** | **PhonePe PG + RuPay credit-card UPI AutoPay**, explicitly to stop mandate failures on low balances (2025) | ❌ Not orchestration, but an explicit recurring-success-rate project |
| **ZEE5** | First OTT with UPI on connected TV; Samsung "Scan And Pay" QR | ❌ None found |
| **Eros Now** | Paytm, MobiKwik, Freecharge; telco billing via Jio/Airtel/Idea/Vodafone | ❌ Wallet-sprawl pattern |
| **hoichoi** | Runs a canned help-centre article titled *"amount has been deducted but my subscription has not been activated"* — **the same failure is common enough at a direct diaspora competitor to warrant a KB article** | ❌ Unknown |

⚠️ **/24 scores are not comparable to /29** — do not rank across them.
⚠️ Chaupal, Sun NXT, Ullu and Eros Now were curled and grepped for eleven PSP tokens: **zero hits**. They are SPAs
that load checkout after initial HTML. **Absence of evidence, not evidence of absence.**

**Vendor-risk note worth carrying into the conversation:** in 2025 PhonePe, Razorpay and Cashfree reportedly
terminated partnerships with Juspay (Juspay denied it), and Juspay open-sourced its orchestrator as Hyperswitch in
March 2025. `[UNVERIFIED — search summary only]` If YuppTV and SonyLIV are both on Juspay, that is both an urgency
signal and a wedge — **but verify before using it, and never name the incumbent in outreach.**

## Section 12: Business Case Data

**Verified and quotable:**
- Six payment legs with per-gateway callback routes — first-party, control-tested
- `stripe_regions` 26-country allowlist — first-party
- Plan ladders rendered `disabled` in PK/BD/SA/AE/LK with local pricing — first-party, 8-market probe
- Live FAQ: no own checkout outside India and the US — first-party
- Google Play user-choice billing live — first-party
- FY26 ₹589 cr revenue / ₹218 cr loss / ~₹300 cr borrowings / ₹192 cr disputed GST — AR 2025-26
- 28/616 Apple reviews with payment-failure language; 13.4% Play one-star

**NOT quotable — do not put these in an email:**
- Any subscriber count or ShemarooMe revenue figure (**management refuses to disclose; stated on the record**)
- Any India INR price (**two conflicting reads of the same Apple listing; one is internally incoherent**)
- Any telco count (**~15 vs ~29 across two releases**)
- Adyen as current **or** legacy (**unresolved**)
- The CARE downgrade (**URL known, not fetched**)
- Pakistan's legal/licensing status (**genuinely unverified in both directions**)

### What I could not verify — explicit

1. **ShemarooMe's standalone subscription revenue, subscribers, ARPU or churn** — does not exist publicly, by policy.
2. **The India plan mix (monthly vs annual)** — swings transaction count ~12× and therefore decides the gate.
3. **The split between web checkout / Apple IAP / Play Billing / telco DCB** — **the number that decides this account.**
4. **The server-side `payment_modes` array** — the authoritative enabled-method list; needs an authenticated session.
5. **Whether Adyen is live or legacy** — `web.archive.org` is blocked by the egress proxy, closing the one method
   that would have dated it.
6. **Pakistan's legal/licensing position.** PEMRA's Indian-content bans are **broadcast-sector**; no PEMRA or PTA
   instrument naming OTT apps was found. **Neither confirmed restricted nor confirmed permitted.**
7. **Google Play review text** — loads by XHR, absent from HTML. **Zero Play quotes; none invented.**
8. **Which Juspay products are in use, and since when** — no case study, press release or merchant-list entry names
   Shemaroo anywhere.
9. **Whether ShemarooMe is an Amazon Prime Video Channels / Tata Play / JioHotstar add-on** — no evidence it is;
   treat as unconfirmed rather than disproven.
10. **Any Shemaroo job posting** — two agents, none reached. No careers host located.
11. **Blocked/failed:** `web.archive.org`, `exchange4media.com` (403), `hoichoi.tv` (403),
    `builtwith.com` ("We cannot lookup results on this domain"), `juspay.io/case-studies` (404),
    `zaubacorp.com`, `thecompanycheck.com`, `yourstory.com`.

</details>
