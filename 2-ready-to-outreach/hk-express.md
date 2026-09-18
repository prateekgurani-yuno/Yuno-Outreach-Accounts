# HK Express

**Status:** 🟡 Research complete — outreach not yet generated
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

*Not yet generated. Run `/full-outreach HK Express` to draft the 12-touch sequence.*

**Five instructions for whoever drafts it:**
1. **Motion is IN-HOUSE. They made a deliberate build decision and it is a competent one.** Anchor on opportunity cost and reach, never on the build being wrong. The observation is *"you built the layer"*, not *"you need a layer."*
2. **The group asymmetry is the opener** — the mainline runs Adyen direct acquiring in six markets with a published +10% India result, and the LCC runs its own gateway. **Frame as a question about whether the group result travels, not as "your parent is doing it better."**
3. **The origin-based convenience fee is the sharpest commercial observation.** It is first-party, quantified, and hasn't moved in 21 months.
4. **The home-market rail gap is the third** — no FPS, no PayMe, no Octopus online, in Hong Kong.
5. ⛔ **Never name their 3DS, fraud or PSS vendors as though we know their acquirer.** We do not. And never name a Yuno competitor, including the one Cebu Pacific runs.

**Never claim:** any acquirer or PSP name (zero established); that Apple Pay or Google Pay is absent (ambiguous); anything from LIHKG, Dcard or discuss.com.hk (all 403, contents unread); or the `PGW_NSK_*` error taxonomy — **I could not find it in the chunk it was attributed to.**

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
