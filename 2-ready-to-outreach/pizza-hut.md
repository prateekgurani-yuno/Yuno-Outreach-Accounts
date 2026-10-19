# Pizza Hut

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 16 / 29 → 🟢 Medium **on arithmetic** — **ANALYST OVERRIDE applied, tier set DOWN to 🔴 Low for "Pizza Hut" as a single account.** Re-target as two accounts instead (see the breakdown): **Pizza Hut Malaysia → QSR Brands** and **Pizza Hut India → Devyani International (post-merger)**.
**Industry:** Quick-service restaurants / pizza delivery, franchised market by market · **HQ:** Brand owner changed in 2026. Yum! Brands sold "Pizza Hut Ex-China" to **LongRange Capital** (US private equity) and Pizza Hut China to **Yum China** (SEC 8-K). APAC markets are run by separate franchisees. · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **Split by market.** **India:** direct multi-PSP integrations (Razorpay, Paytm, PhonePe) in the **global Pizza Hut web codebase**. No third-party orchestrator found in the code, so this is neither greenfield-for-the-franchisee nor clearly in-house. **Malaysia:** replatformed onto **Fynd Commerce** around Mar 2026. The TAL says Juspay; this is **unverified**.

---

> # 🔒 PHASE 0 — QUALIFICATION GATE
>
> | Rule | Result |
> |---|---|
> | PSP / gateway / acquirer / orchestrator | Does not fire. QSR brand. |
> | Existing Yuno customer | **Does not fire.** y.uno home page and `/en/success-stories` fetched 2026-10-19 (HTTP 200) have zero hits for Pizza Hut, Yum, KFC, Devyani, Sapphire, QSR Brands or LongRange. **McDonald's / Arcos Dorados is a Yuno customer** (direct competitor brand, different region), so it's usable as proof. |
> | No online payment volume | Does not fire. Own web and app ordering exists in both APAC markets. |
> | HQ west of Dubai with no APAC operations | **Does not fire, with a caveat.** The brand owner is US-based (LongRange Capital), but APAC operations exist through local operators: QSR Brands in Malaysia, Devyani and Sapphire in India. **The real APAC buyers are those operators, not the brand.** |
> | Monthly transactions < 40,000 (sourced) | **Does not fire.** No sourced order count. Assumed far above 100k/month across ~970 India and ~400 Malaysia stores. See Section 12. |

> # ⚠️ METHOD NOTES — disclosed up front
>
> 1. **Traffic is supplied SimilarWeb data with real caveats** (`accounts/traffic/pizza-hut.md`, Sales Intelligence view, Jul–Sep 2026):
>    - Only the top 10 countries per domain, shares only.
>    - **No per-country visit counts.** All per-country visits below are `[DERIVED from supplied share, not a SimilarWeb figure]` (share × that domain's average monthly visits).
>    - **Desktop and mobile web only — app traffic is excluded.** This is an app- and aggregator-heavy QSR business, so web traffic understates transactions badly. It is used here as a **market-mix signal only**, never for sizing.
>    - Only **three domains** were pulled: `pizzahut.com`, `pizzahut.co.in`, `pizzahut.com.my`. **No other APAC domains were supplied** (AU, SG, ID, PH, TH, JP, HK, TW). So the "APAC country profile" is really just India plus Malaysia, and the Australia and Singapore rows are spill-over visitors to the wrong domain, not those markets' Pizza Hut customers.
>    - `pizzahut.com` is 97.28% US and is a different operator. Combining it into one total makes the US look like 91.7% of "Pizza Hut", which is an artefact of the pull.
> 2. **WebFetch worked** in this session, so the full method ran. The strongest evidence is **[Source Code]** from the live `pizzahut.co.in` JS bundle and the `pizzahut.com.my` page HTML, both pulled 2026-10-19 and re-checked by me after the agents reported.
> 3. **Most financials are search-summary only** (Devyani/Sapphire quarterly numbers, QSR Brands growth). The NSE investor PDFs returned 403. They are labelled `[UNVERIFIED — search summary only, page not fetched]`.
> 4. **One agent finding was rejected after checking.** An agent read India-style payment strings on `pizzahut.com.my` (Paytm UPI, PhonePe UPI, CCAvenue, JioOnePay) as proof that India and Malaysia share one platform. Those strings sit next to `"fynd_cash":"Fynd Cash"` and `"partner_pay"`, which places them in **Fynd's generic i18n dictionary**. The India site loads from `api.pizzahut.io` instead. **The two markets run on different platforms.**

---

> ## 🎯 THE HOOK (India) — the gateway says "success", the order never exists
>
> The same symptom appears across years and across rails:
> - **25 Jan 2026:** a customer paid ₹403.20 twice in the Pizza Hut India app, once by **Paytm** and once by **GPay (UPI)**. Both showed "failed" in the app, with "no record on app but money deducted". Paytm showed `SUCCESS`. Unresolved. ([consumercomplaints.in](https://www.consumercomplaints.in/pizza-hut-india-money-deducted-two-times-from-upi-paytm-and-google-pay-but-no-order-placed-on-app-unable-ro-reach-company-for-refund-c3539095), fetched)
> - The same page links five more "[Resolved]" Pizza Hut India complaints of the same class: "payment successful but order not placed in pizza hut app", "money deducted … by gpay but no order was placed", "waiting refund since 4 weeks".
> - Voxya has a run of the same complaint from Aug 2023 to Sep 2025 (search summary only, see Section 5).
> - Google Play reviews of **"Pizza Hut India - Delivery App"** describe "payment deducted but no order ID" and "the payment gateway integration is bad" ([Play listing](https://play.google.com/store/apps/details?id=com.phdv.universal&hl=en_IN), fetched).
>
> **Why it matters:** the bundle shows Razorpay's "Online Payment" flow running through a **`RazorpayPollingModal`**, meaning order creation waits on polling the payment status. A payment confirmed at the PSP but never reconciled into an order is exactly the failure that produces "money deducted, no order". `[INFERENCE, not confirmed]` that polling is the cause. The pattern is real; the root cause is not proven.
>
> **The official answer to this failure is a 21-business-day refund window** ([online.pizzahut.co.in/faqs](https://online.pizzahut.co.in/faqs), fetched): "if payment is debited but the order was not placed … refunded within 21 business days".

> ## ⛔ READ BEFORE PITCHING INDIA — Razorpay and orchestrators
> Razorpay is Pizza Hut India's web "Online Payment" PSP ([Source Code]). In Jan 2025, Razorpay said it would **"pause all integrations through third-party routing platforms"** and Cashfree said the same. This was verified by direct fetch of [Entrackr, 20 Jan 2025](https://entrackr.com/news/after-phonepe-razorpay-and-cashfree-suspend-direct-integrations-with-juspay-8638638) in `2-ready-to-outreach/jubilant-foodworks.md` (2026-10-05). **Confirm with Yuno Solutions/Partnerships whether Yuno can route Razorpay volume in India before any India outreach.**

> ## 🧭 THE STRUCTURAL POINT — who actually decides payments
> - **India web checkout is built by the global brand, not the franchisee.** `pizzahut.co.in` loads `/order/js/in.4244cdc0c48062144e76.js` from `api.pizzahut.io`. The same bundle carries en-GB and fr-CA locales and handlers for **Worldpay, HiPay, VTEX, PayPal, Visa Click to Pay and Cybersource**, which serve non-APAC Pizza Hut markets. The India app is published as `com.phdv.universal` by **Pizza Hut Digital Ventures** (Play listing). PSP choice for India therefore sits at least partly with the **Pizza Hut international digital team**, which now belongs to LongRange and runs on Yum's **Byte by Yum!** platform under a transition services agreement ([SEC 8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/0001041061/000119312526271893/d158986dex991.htm), fetched).
> - **The LongRange carve-out is a global replatforming trigger, but not an APAC one.** A TSA ends. When Pizza Hut Ex-China has to stand up its own commerce and payments stack outside Byte by Yum!, that is a multi-market payment decision. It will most likely be made in the US. **Flag to the NA/global team; it is not Prateek's to run.** `[INFERENCE, not confirmed]` that a re-platform follows the TSA. No TSA term or end date was found.
> - **Malaysia already made its 2026 platform decision.** It moved to Fynd around Mar 2026, with the FAQ section "What's New with Pizza Hut's New Website & App", migrated Slices balances, and lost order history. A buyer seven months past a replatform is a poor cold target for another payments project, unless the Fynd payment layer is causing pain.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Pizza Hut is a global pizza QSR brand that was owned by Yum! Brands until 2026. Yum sold Pizza Hut Ex-China to LongRange Capital for about US$1.5bn and Pizza Hut China to Yum China for about US$1.2bn (announced 16 Jun 2026). In APAC the brand is run by independent operators: QSR Brands in Malaysia and Singapore; Devyani International and Sapphire Foods in India (merging); and others such as Sarimelati (ID), Flynn Group (AU), PH Capital (TH) and Jardine Restaurant Group (HK/TW). Each runs its own payments, except where the brand's global web platform is used (India).

**SimilarWeb total visits (last full month):** Q3 2026 monthly average **13.43M** across three domains: pizzahut.com 12.66M, pizzahut.com.my 0.415M, pizzahut.co.in 0.360M. Source: SimilarWeb (supplied 2026-10-19). **APAC-relevant: ~0.83M/month.** Web only, so it materially understates orders in this app- and aggregator-heavy business.

### Top 5 markets (APAC only; US 91.7% and Canada 0.5% excluded as out of territory and a different operator)
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | Malaysia | ~403,950/mo (3.01% of combined; 48.6% of APAC) | Cards, "e-wallets" (no brand named), COD, cash at pickup; "online banking" for vouchers only ([T&C](https://www.pizzahut.com.my/en/terms-and-conditions)) | FPX, DuitNow, TNG, GrabPay, Boost, ShopeePay **not named**. Absence is not confirmed: checkout not reached. | ⚠️ QSR Brands (M) Holdings operates it [SS]. The T&Cs say only "Pizza Hut Malaysia". No SSM number. |
| 2 | India | ~354,740/mo (2.64%; 42.7% of APAC) | Razorpay "Online Payment", Paytm, PhonePe channel, cash ([Source Code]) | UPI, netbanking and wallet enums exist in code. **Live status not confirmed.** No gap is provable. | ⚠️ Devyani International / Sapphire Foods (listed franchisees); website operator entity **not found** (T&C/privacy URLs 404) |
| 3 | Australia | ~51,340/mo (0.38%) — **spill-over to pizzahut.com/.co.in/.com.my, not pizzahut.com.au** | Not researched (domain not supplied) | N/A | ❌ not researched. Operator: Flynn Group [SS] |
| 4 | Singapore | ~12,140/mo (0.09%) — spill-over | Not researched | N/A | ❌ not researched. Operator: QSR Brands [SS] |
| 5 | China | ~6,330/mo (0.05%) — spill-over | N/A, Yum China's own stack | N/A | Yum China (separate listed company) |

All per-country visit figures are `[DERIVED from supplied share, not a SimilarWeb figure]`.

### Legal entities
- **QSR Brands (M) Holdings Sdn Bhd** (Malaysia): operator of Pizza Hut Malaysia; JCorp majority [SS]. No registration number found.
- **Devyani International Ltd** (India, NSE: DEVYANI): 626 Pizza Hut stores, Q1 FY27 [SS].
- **Sapphire Foods India Ltd** (India, NSE: SAPPHIRE): 346 Pizza Hut India stores, Q1 FY27 [SS]. Merging into Devyani.
- **Pizza Hut Digital Ventures**: publisher of the India app `com.phdv.universal` (Google Play, fetched). Country of incorporation not confirmed.
- **Yum! Restaurants (India) Pvt Ltd**: holding company of Pizza Hut India Marketing [SS]. No CIN found.

### Known PSPs
- **Razorpay** — [Source Code] (India web; enum `RAZORPAY="razorpay"`, India label "Online Payment", `RazorpayPollingModal`)
- **Paytm** — [Source Code] (India web; `securegw.paytm.in/order/process`)
- **PhonePe** — [Source Code] (India; `PHONEPE:"phone-pe"` channel constant; probably a PhonePe Switch channel)
- **Cybersource** — [Source Code] (in the shared international bundle, with Cardinal 3DS, Microform and the Google Pay gateway; **live in India not confirmed**)
- **Malaysia** — **no PSP found.** Fynd checkout config loads client-side (`"payment_options":{},"aggregators_config":{}}` in the server render).

### Orchestration status
**India: none detected.** Direct PSP integrations live inside the global Pizza Hut web codebase: the bundle has 0 hits for juspay, payu, hyperswitch or other orchestrator SDKs ([Source Code]). An in-house routing layer cannot be ruled out because the backend is not visible. **Malaysia: unverified.** The TAL says Juspay. Fynd supports Juspay as a PG ([Fynd docs](https://docs.fynd.com/commerce/set-up-website/payments/juspay/add-juspay) [SS]), but no Pizza Hut-specific evidence exists and Juspay's customer index has no Pizza Hut story ([juspay.io/customer-stories](https://juspay.io/customer-stories), fetched). **Overall: uncertain.**

### Buying signals
- 🤝 **Brand ownership change:** Yum sold Pizza Hut Ex-China to LongRange Capital, with Byte by Yum! retained under a TSA ([SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001041061/000119312526271893/d158986dex991.htm)). Closed around 1 Sep 2026 [SS].
- 🤝 **India consolidation:** Devyani and Sapphire are merging (announced 1 Jan 2026; 177:100 share swap; ~US$933m), giving one Indian Pizza Hut operator ([Bloomberg Law](https://news.bloomberglaw.com/mergers-and-acquisitions/kfc-pizza-hut-india-operators-to-merge-in-933-million-deal-2) [SS]). CCI/NCLT approvals were still pending at last check.
- 🚀 **Malaysia replatform** onto Fynd Commerce, around Mar 2026 ([Source Code] + site FAQ).
- 💼 **Pizza Hut India has no permanent digital and tech head.** The CMO has held the Digital & Technology mandate "on an interim basis" since 15 Sep 2025 ([media4growth](https://www.media4growth.com/talent/people/manish-guptaa-takes-charge-as-chief-marketing-officer-of-pizza-hut-india-79653?amp=1), fetched).
- 💼 Yum! **Global PCI Manager** role, covering Byte Commerce and Pizza Hut ([Built In Chicago](https://www.builtinchicago.org/job/global-pci-manager/9989760), fetched; "reposted 2 months ago").

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach {name}` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

> **Recommendation: do not run `/full-outreach Pizza Hut`.** Run `/research QSR Brands` (stub already in `1-to-outreach/`) and add **Devyani International** to the TAL for a separate run after the merger clears. Both are sharper buyers than the brand.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 16 / 29 (arithmetic) → override to 🔴 Low
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | +5 | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. [ASSUMPTION — not researched.]** Basis: ~970 Pizza Hut stores in India (Devyani 626 + Sapphire 346, Q1 FY27 [SS]). Devyani Pizza Hut revenue is ~₹184 Cr/quarter [SS] and Sapphire's ~₹136 Cr [SS]; QSR runs ~400 Malaysian stores [SS]. **No sourced average order value**, so no derivation is possible. Billing unit = one consumer order paid on Pizza Hut's own web or app. **Aggregator orders (Swiggy, Zomato, GrabFood, foodpanda) do not touch Pizza Hut's PSPs and must be excluded.** Band scored per the disclosure rule; this is not a measurement. |
| Orchestration status | 0 | ⬜ Uncertain. India: direct PSPs in the code, no orchestrator SDK, backend unknown. Malaysia: TAL says Juspay, unverified. The account has no single status. |
| 3+ countries | +3 | ✅ On arithmetic: US 91.7%, Malaysia 3.0% and India 2.6% of combined web traffic each exceed 1%. **This is an artefact of combining three separately operated domains.** See override. |
| Multiple PSPs | +3 | ✅ Razorpay + Paytm (+ PhonePe channel) in the live India bundle [Source Code]. |
| Local rail or licensing gap in a top-3 market | 0 | ⬜ India: UPI, netbanking and wallet enums exist and Razorpay's hosted checkout likely carries UPI, so no gap is provable. Malaysia: FPX and brand wallets are not named, but "online banking" and "e-wallets" are. Absence not confirmed. |
| Recent expansion | 0 | ❌ No new APAC market in 12 months. The Malaysia replatform and the India merger are not expansion. |
| Payment issues reported | +2 | ✅ Moderate, recurring "money deducted, no order" and slow-refund complaints for the India app, 2023 to Jan 2026 (fetched consumercomplaints.in item plus Voxya series and Play reviews). Malaysia Play reviews mention payments marked failed after the account was charged (Agent 3, fetched listing). |
| Funding >$10M | 0 | ❌ An acquisition by PE (LongRange) and a merger by share swap (Devyani/Sapphire) are not funding rounds. |
| High traffic outside home | 0 | ❌ Each domain is 96–97% its home market; combined, the US is 91.7%. |
| Competitor using orchestration | +2 | ✅ **Domino's India (Jubilant)** runs an in-house `unifiedpayment` layer across 7 gateways ([Source Code], `2-ready-to-outreach/jubilant-foodworks.md`). Juspay's customer index lists **McDonald's** and **Burger King** (fetched; **market not stated**). |
| Payment job postings | +1 | ✅ Yum! Global PCI Manager, with scope including Byte Commerce and Pizza Hut (fetched). ⚠️ Yum no longer owns Pizza Hut; the role is relevant only through the Byte TSA. |

**Tier on arithmetic:** 16 → 🟢 Medium.

**ANALYST OVERRIDE → 🔴 Low (for "Pizza Hut" as one account).** Four reasons:
1. **No single APAC buyer.** India and Malaysia have different operators, platforms and PSPs. Australia, Indonesia, Thailand, Singapore and HK/TW are further separate operators that weren't even in the traffic pull. An account called "Pizza Hut" has nobody to email.
2. **The matrix double-counts one artefact.** "3+ countries" fires only because a 97%-US domain was combined with two single-market domains. Without it the score is 13, and that 13 still includes an assumed +5.
3. **The India stack is decided outside APAC and is in transition.** India's web checkout is the global Pizza Hut codebase (Pizza Hut Digital Ventures), now owned by LongRange and running on Yum's Byte under a TSA. Its main India PSP, Razorpay, has said it is pausing third-party routing integrations.
4. **Malaysia just replatformed.** It moved to Fynd around Mar 2026, so the payment-stack decision for 2026 has been taken.

**What to do instead:**
- **QSR Brands** (P1, stub in `1-to-outreach/qsr-brands.md`): owner of Pizza Hut and KFC Malaysia/Singapore and KFC Brunei/Cambodia. It is multi-brand and multi-country, with one buyer.
- **Devyani International**: **not in the TAL — a genuine find.** Post-merger it becomes the sole Indian operator of KFC and Pizza Hut (~3,000 stores, [Outlook Business](https://www.outlookbusiness.com/corporate/devyani-sapphire-merger-to-create-qsr-giant-with-nearly-3000-stores) [SS]), plus Sri Lanka via Sapphire's subsidiary and Devyani's international stores. Check first whether KFC India also runs on the brand's global platform. The app is published under Yum! Restaurants India (App Store [SS]).
- **Pizza Hut Ex-China global (LongRange)**: hand to the NA/global team as a TSA-exit replatforming signal.

### Source Notes
- ✅ Razorpay, Paytm, PhonePe, Cybersource, Worldpay, HiPay and VTEX strings in `pizzahut.co.in/order/js/in.4244cdc0c48062144e76.js`. Pulled and grep-verified 2026-10-19.
- ✅ Razorpay's India label is "Online Payment" in the India locale strings of that bundle.
- ✅ `pizzahut.com.my` runs on Fynd: 816 "fynd" hits, `company_id:14273`, MYR currency, empty server-side payment config.
- ✅ Yum sale terms and Byte by Yum! TSA: SEC 8-K Ex-99.1, fetched.
- ✅ Malaysia T&C payment-method wording, "Last updated 26 Mar 2026": fetched.
- ✅ Jan 2026 India double-debit complaint: consumercomplaints.in, fetched.
- ✅ India 21-business-day refund window: online.pizzahut.co.in/faqs, fetched (COVID-era page; still live).
- ✅ Pizza Hut India interim digital mandate: media4growth, fetched.
- ✅ Arcos Dorados / McDonald's case on y.uno, fetched.
- ⚠️ TAL claim "Pizza Hut Malaysia → Juspay": **unverified.** Do not use in outreach.
- ⚠️ TAL claim "QSR Brands runs Pizza Hut in Brunei and Cambodia": **probably wrong.** Sources split it as KFC in MY/SG/BN/KH and Pizza Hut in MY/SG only [SS].
- ⚠️ All Devyani/Sapphire/QSR financials, store counts and merger status: search summary only.
- ⚠️ Closing of the LongRange deal (1 Sep 2026) and the Yum China deal (7 Aug 2026): search summary only.
- ⚠️ The "Fynd is Reliance-owned" framing is background knowledge, not sourced this run. Do not state it.
- ❌ Rejected: the agent inference that India and Malaysia share one Pizza Hut platform (strings were Fynd boilerplate).

### Success Case Alternatives
- **Arcos Dorados (McDonald's), the best match** — the world's largest McDonald's franchisee "unified payments across 21 countries and 2,400+ restaurants with Yuno, replacing a fragmented mix of PSPs and acquirers with a single platform" ([y.uno](https://y.uno/en/success-stories/mcdonalds), fetched). It is a franchisee of a global QSR brand running multi-country, which is exactly the Devyani post-merger and QSR Brands profile.
- **Rappi** — "cuts new provider implementation time to zero" (y.uno success-story index, fetched). A delivery-native fit if the pitch is about adding PSPs and wallets fast. Weaker profile match.

---

## Executive Summary

Pizza Hut is a global pizza QSR brand that Yum! Brands sold in 2026: Ex-China to LongRange Capital, China to Yum China. In APAC it is run market by market by independent operators. The two APAC markets in the supplied traffic run completely different stacks:
- **India** uses the global Pizza Hut web codebase, wired directly to Razorpay, Paytm and PhonePe with no orchestrator SDK. It has a recurring "money deducted, no order" complaint pattern that it handles with a 21-business-day refund window.
- **Malaysia** (QSR Brands) replatformed onto Fynd Commerce around March 2026. Its PSP is unknown, and the TAL's Juspay tag is unverified.

The ICP arithmetic gives 16/29 (🟢), but an override takes the brand-level account to 🔴. The real motions are separate: **QSR Brands** (Malaysia/Singapore, platform-mediated) and **Devyani International** (India, after the merger). The India PSP, Razorpay, has said it is pausing third-party routing integrations, which needs clearing internally first.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** Path 1, supplied SimilarWeb, cited as "SimilarWeb (supplied 2026-10-19)", Jul–Sep 2026, from `accounts/traffic/pizza-hut.md`.
- Sales Intelligence view: top 10 countries per domain, shares only.
- **Desktop and mobile web only; app traffic excluded.**
- Combined by converting each domain's share to visits (share × the domain's average monthly visits), summing per country, and recalculating shares against **13,434,382** combined monthly visits.
- Countries outside a domain's top 10 are missing from that domain's contribution, so smaller rows are floors.
- No trend data was supplied.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | United States | 91.74% | ~12,325,290 | N/A | SimilarWeb (supplied) — **out of territory** |
| 2 | **Malaysia** | 3.01% | ~403,950 | N/A | SimilarWeb (supplied); pizzahut.com.my 97.40% |
| 3 | **India** | 2.64% | ~354,740 | N/A | SimilarWeb (supplied); pizzahut.co.in 96.08% + small spill-over |
| 4 | Canada | 0.50% | ~66,510 | N/A | out of territory |
| 5 | Australia | 0.38% | ~51,340 | N/A | spill-over; pizzahut.com.au **not supplied** |
| 6 | Mexico | 0.20% | ~26,590 | N/A | out of territory |
| 7 | Singapore | 0.09% | ~12,140 | N/A | spill-over |
| 8 | UAE | 0.06% | ~7,660 | N/A | out of territory (EMEA) |
| 9 | Belgium | 0.06% | ~7,600 | N/A | out of territory |
| 10 | Egypt | 0.06% | ~7,600 | N/A | out of territory |

Every per-country visit figure is `[DERIVED from supplied share, not a SimilarWeb figure]`.

**Device split:**

| Domain | Mobile web | Desktop |
|---|---|---|
| pizzahut.com.my | 91.82% | 8.18% |
| pizzahut.co.in | 86.22% | 13.78% |
| pizzahut.com | 83.38% | 16.62% |

**High-priority markets (>5% share):** only the US on the combined basis. **On an APAC-only basis (~831k/month):** Malaysia 48.6%, India 42.7%, Australia 6.2%.

**Caveat:** the Australia figure is not Pizza Hut Australia's traffic.

**Entity cross-check:**
- Malaysia and India have identified operators (QSR Brands; Devyani/Sapphire), but no registry numbers were found.
- Australia and Singapore operators are identified only by search summary (Flynn Group; QSR Brands).

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** The brand owner is now **LongRange Capital** (Pizza Hut Ex-China) after Yum's sale, expected to close Q3 2026 ([SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001041061/000119312526271893/d158986dex991.htm), fetched). The deal reportedly closed and was announced 1 Sep 2026, with an interim CEO, Eduardo Luz ([NRN](https://www.nrn.com/restaurant-finance/pizza-hut-s-sale-to-longrange-capital-is-complete) [SS]). Pizza Hut's post-deal HQ city was not verified.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Malaysia | QSR Brands (M) Holdings Sdn Bhd (operator; Johor Corporation majority) | Not found | [plunkettresearch](https://www.plunkettresearch.com/?p=1889612) [SS]; site T&Cs name only "Pizza Hut Malaysia" ([fetched](https://www.pizzahut.com.my/terms-and-conditions)) |
| India | Devyani International Ltd (franchisee, 626 Pizza Hut stores) | NSE: DEVYANI | [DSIJ Q1 FY27](https://insights.dsij.in/markets/reports/report-details/devyani-international-ltd/44862) [SS] |
| India | Sapphire Foods India Ltd (franchisee, 346 Pizza Hut India stores) | NSE: SAPPHIRE | [Kalkine](https://www.kalkine.co.in/article/announcements/sapphire-foods-nsesapphire-what-drove-15-revenue-growth-in-q1-fy27) [SS] |
| India | Yum! Restaurants (India) Pvt Ltd (holding company of Pizza Hut India Marketing) | Not found | [Business Standard](https://business-standard.com/amp/topic/yum) [SS] |
| India / global | Pizza Hut Digital Ventures (publisher of the India app) | Not found | [Google Play](https://play.google.com/store/apps/details?id=com.phdv.universal&hl=en_IN) (fetched) |
| Sri Lanka | Gamma Pizzakraft Lanka (Sapphire subsidiary) | Not found | [Sunday Times LK](https://www.sundaytimes.lk/260621/news/india-franchisee-woos-pizza-hut-sri-lanka-operator-while-yum-brands-sheds-chain-646689.html) [SS] |
| Singapore | QSR Brands (Pizza Hut rights MY + SG) | Not found | [qsrbrands.com](https://qsrbrands.com/?p=9215) [SS] |
| Australia | Flynn Group (master franchise since 2023) | Not found | [Restaurant Business](https://restaurantbusinessonline.com/financing/greg-flynn-goes-global-australian-pizza-hut-acquisition) [SS] |
| Indonesia | PT Sarimelati Kencana Tbk | IDX: PZZA | [IDN Financials](https://www.idnfinancials.com/news/61626/pizza-hut-issuer-explores-new-business-as-core-operations-slow-down) [SS] |
| Thailand | PH Capital (70% Thoresen Thai Agencies) | Not found | [Seatrade Maritime](https://www.seatrade-maritime.com/asia/thoresen-thai-bulks-pizza-hut-thailand-buy) [SS] |
| HK / TW / Macau | Jardine Restaurant Group | Not found | [MPU career fair PDF](https://www.mpu.edu.mo/careerfair/assets/files/F2-1.pdf) [SS] |
| Mainland China | Yum China Holdings (owns the Pizza Hut China brand outright; closed 7 Aug 2026 [SS]) | NYSE: YUMC / HKEX: 9987 | SEC 8-K (fetched) |
| Japan, Philippines | Not found | — | — |

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| Malaysia | Yes (#2) | Yes, local operator | Not assessed; local operator in any case | No |
| India | Yes (#3) | Yes, local listed franchisees | Not relevant; local operator, local PSPs (Razorpay/Paytm) | No |
| Australia | Yes (#5, spill-over) | Separate operator (Flynn Group) | N/A | N/A — not this account's traffic |
| Singapore | Yes (#7, spill-over) | QSR Brands | N/A | No |

**No cross-border warning applies.** Every APAC market is locally operated with local acquiring, so the cross-border inefficiency and regulatory-gate angles **do not exist on this account.**

> **MANUAL:** The pizzahut.co.in footer and legal pages (T&C and privacy URLs tried both 404) should name the website operator. Check in a browser.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| India (web) | **Razorpay**: payment-type enum `RAZORPAY="razorpay"`; India locale label `PAYMENT_LABEL[RAZORPAY]:"Online Payment"`; flags `display_razorpay_options`, `razorpay_notes_as_string`; `RazorpayPollingModal` (14 refs) | [Source Code] | https://www.pizzahut.co.in/order/js/in.4244cdc0c48062144e76.js |
| India (web) | **Paytm**: `PAYTM_SECUREGATEWAY_URL:"https://securegw.paytm.in/order/process"` | [Source Code] | same bundle |
| India | **PhonePe**: `PHONEPE:"phone-pe"` channel constant; footer changes when the channel is PhonePe. Likely a PhonePe Switch/mini-app channel, not necessarily PhonePe PG `[INFERENCE, not confirmed]` | [Source Code] | same bundle |
| Shared international codebase | **Cybersource**: `secureacceptance.cybersource.com/silent/pay`, Cardinal 3DS, Microform, Google Pay `gateway:"cybersource"`. **Live in India not confirmed** | [Source Code] | same bundle |
| Shared international codebase (non-APAC) | Worldpay, HiPay, VTEX, PayPal, Visa Click to Pay, Apple Pay. **Do not attribute to India** | [Source Code] | same bundle |
| India (historic) | Razorpay named in 2018–19 consumer complaints about Pizza Hut orders | [Third-Party Report] | [voxya 21706](https://voxya.com/consumer-complaints/payment-was-successful-but-the-company-denied/21706) [SS] |
| India (in-store, Devyani) | HDFC Bank BharatQR / BHIM UPI at POS, ~2020 | [Third-Party Report] | [NPCI newsletter](https://npci.org.in/newsletter/January-2020/power-of-partnerships.html) [SS] |
| Malaysia | **Not found.** Platform is Fynd Commerce (`cdn.fynd.com`, `company_id:14273`); server-rendered payment config empty | [Source Code] | https://www.pizzahut.com.my/ |

**Searched and not found:**
- India: CCAvenue, BillDesk, Cashfree, PayU, Juspay, Hyperswitch, Pine Labs (0 hits in the India bundle).
- Malaysia: iPay88, Razer/Fiuu/MOLPay, eGHL, 2C2P, Adyen, Stripe.
- No Yum-wide global PSP deal was found in press.

**Single-PSP dependency:** No for India. Razorpay is the general "Online Payment" option, with Paytm and PhonePe as separate rails. Unknown for Malaysia.

#### 3B. Payment Orchestrator

**India: None detected.** The bundle shows direct integrations to Razorpay, Paytm and PhonePe, selected by payment method, inside the global Pizza Hut web codebase. There is no orchestrator SDK. The agent proposed an "in-house orchestration layer", but that is only an `[INFERENCE, not confirmed]`: the code shows method-based PSP selection, and backend routing is invisible.

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with PSP(s), which limits routing optimization, failover capabilities, and multi-acquirer strategies."* This applies to India web only.

**Malaysia: Regional orchestrator (Juspay) per the TAL — UNVERIFIED.** The only supports are the TAL row (`accounts/apac-tal.csv`: Pizza Hut Malaysia → Payment Orchestrator = Juspay) and Fynd's native Juspay PG integration ([Fynd docs](https://docs.fynd.com/commerce/set-up-website/payments/juspay/add-juspay) [SS]). Juspay's customer-stories index has no Pizza Hut entry (fetched). If it can't be confirmed, the honest fallback is "None detected — platform-mediated via Fynd".

**Byte by Yum!:** launched Feb 2025 as Yum's platform for online and mobile ordering, POS, kitchen and delivery ([BusinessWire](https://www.businesswire.com/news/home/20250206765566/en) [SS]). It continues to serve Pizza Hut Ex-China under a services arrangement after the sale (SEC 8-K, fetched). No source says Byte centralizes APAC payment processing.

> **MANUAL:** Place a test order on pizzahut.com.my with DevTools open. Look for `api.juspay.in` or Hyper SDK calls versus iPay88, Fiuu or eGHL endpoints. That one check settles the Malaysia motion.

---

### Section 4: Alternative & Local Payment Methods

**Malaysia** ([T&C, "Last updated 26 Mar 2026"](https://www.pizzahut.com.my/en/terms-and-conditions), fetched). Verbatim: "We accept the following payment methods: Credit and Debit Cards / E-Wallets / Cash on Delivery (for Delivery orders) / Cash at Pickup (for Takeaway orders)."

| Method | Category | Status | Source |
|--------|----------|--------|--------|
| Credit/debit cards | Cards | Mentioned in docs | T&C |
| "E-Wallets" (no brand named) | Digital wallet | Mentioned in docs | T&C |
| Cash on delivery / cash at pickup | Cash | Mentioned in docs | T&C |
| Online banking (voucher purchases only; likely FPX `[INFERENCE]`) | Bank transfer / A2A | Mentioned in docs | T&C |
| FPX (by name) | A2A | Not found | 0 hits in T&C and page HTML; the one "FPx" hit is a CSS class name |
| DuitNow QR, Touch 'n Go, Boost, GrabPay, ShopeePay | Wallet / A2A | Not found by name | — |
| SPayLater promo | BNPL | Conflict: a search summary claims a T&C promo, but curl of the T&C found 0 hits | [UNVERIFIED] |
| Apple Pay / Google Pay | Wallet | Unknown, checkout not accessible (Fynd generic strings only) | — |

**India** (pizzahut.co.in bundle, [Source Code]; payment-type enum includes `CARD`, `CASH`, `NETBANKING`, `WALLET`, `UPI`, `PAYTM`, `RAZORPAY`, `PHONEPE`, `GOOGLE_PAY`)

| Method | Category | Status | Source |
|--------|----------|--------|--------|
| Razorpay "Online Payment" (hosted; typically covers cards, UPI and netbanking `[INFERENCE]`) | Mixed | Mentioned in code (India label) | bundle |
| Paytm | Wallet / PG | Mentioned in code | bundle |
| PhonePe | Wallet / UPI | Mentioned in code | bundle |
| UPI, netbanking, wallet (generic enums) | A2A / wallet | Mentioned in code; live status unknown | bundle |
| Cash | Cash | Mentioned in code (label "Cash") | bundle |
| UPI in store | A2A | Outlet pages "Accepts UPI payments" | [restaurants.pizzahut.co.in Bardoli](https://restaurants.pizzahut.co.in/pizza-hut-ph-bardoli-pizza-restaurant-baben-bardoli-129248/Home) [SS] |
| RuPay, Pluxee/Sodexo online, BNPL (Simpl/LazyPay) | — | Not found | — |

No rail-gap warning is issued. **Neither market has a sourced absence of its dominant rail.** UPI-capable rails are wired in India, and Malaysia claims e-wallets and online banking.

> **MANUAL:** Check the live checkout in both markets for which e-wallets sit behind "E-Wallets" (MY) and whether UPI is a direct option or only inside Razorpay (IN).

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Double debit; failed payment with money deducted (Paytm + GPay UPI, ₹403.20 ×2; PSP shows SUCCESS, app shows failed) | consumercomplaints.in (fetched) | Moderate (page links 5 more of the same class) | Jan 2026 | [link](https://www.consumercomplaints.in/pizza-hut-india-money-deducted-two-times-from-upi-paytm-and-google-pay-but-no-order-placed-on-app-unable-ro-reach-company-for-refund-c3539095) |
| Paid via GPay, no order in app | Voxya | Moderate (series) | Aug 2023 | [voxya 209034](https://voxya.com/consumer-complaints/payment-done-but-food-order-not-placed/209034) [SS] |
| Order cancelled, amount deducted, no refund | Voxya | — | Dec 2023 | [voxya 218366](https://voxya.com/consumer-complaints/order-canceled-amount-deducted-no-refund-yet/218366) [SS] |
| Refund "issued" but no bank credit | Voxya | — | Jan 2024 | [voxya 220158](https://voxya.com/consumer-complaints/amount-refund/220158) [SS] |
| Payment done, order not showing in app | Voxya | — | Feb 2025 | [voxya 242241](https://voxya.com/consumer-complaints/order-pizza-payment-done-but-order-is-not-showing-on-app/242241) [SS] |
| Refund pending from Aug 2025 cancellation; customer redirected to store | Voxya | — | Sep 2025 | [voxya 251222](https://voxya.com/consumer-complaints/refund-pending-since-august-2025-order-cancellation/251222) [SS] |
| "Payment deducted but no order ID"; "payment gateway integration is bad" | Google Play, India app | Anecdotal | Listing updated Dec 2025 | [Play](https://play.google.com/store/apps/details?id=com.phdv.universal&hl=en_IN) (fetched) |
| Payment marked failed after the account was charged; vouchers consumed after a payment crash | Google Play, Malaysia app | Anecdotal | Listing updated Sep 2026 | [Play](https://play.google.com/store/apps/details?id=com.pizzahut.malaysia) (fetched) |

> *Pattern of "PSP-success / order-missing" failures in India, across Paytm, GPay/UPI and earlier Razorpay, suggests the fault is in the payment-to-order reconciliation leg rather than any single PSP. That is the class of problem a routing layer with unified status handling and webhooks owns as a product.* `[INFERENCE, not confirmed]`. Absolute volume is low (complaint aggregators). Reddit, X and Malaysian forums returned nothing.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 1 Sep 2026 (announced close) | LongRange Capital completes the purchase of Pizza Hut Ex-China (~US$1.5bn + up to US$75m earn-out); Byte by Yum! continues under a TSA | M&A | [SEC 8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/0001041061/000119312526271893/d158986dex991.htm) (terms, fetched); [QSR Magazine](https://www.qsrmagazine.com/news/yum-brands-completes-sale-of-pizza-hut-to-longrange-capital/) (close) [SS] |
| 2 | 7 Aug 2026 | Yum China closes its ~US$1.2bn purchase of Pizza Hut China | M&A | [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001041061/000104106126000187/a8kex991912026.htm) [SS] |
| 3 | 26 Aug 2026 | Sapphire board approves a revised merger scheme with Devyani after the promoter secondary-sale deal was terminated; NSE/BSE no-objection received; CCI/NCLT pending | M&A | [sahi.com](https://www.sahi.com/news/devyani-international-changes-merger-plan-as-mutual-agreement-ends-secondary-sale-deal-3433-PE1_COR), [tijorialerts](https://www.tijorialerts.com/companyUpdates/devyani-international-gets-nse-bse-no-objection-for-sapphire-merger-108653/) [SS] |
| 4 | ~Mar 2026 | Pizza Hut Malaysia relaunches its website and app on Fynd Commerce; Slices loyalty migrated to Points / Hut Rewards; order history not migrated | Tech platform signal | pizzahut.com.my HTML and FAQ ([Source Code]); date inferred from Fynd object IDs |
| 5 | 15 Sep 2025 | Manish Guptaa named CMO of Pizza Hut India, also holding the Digital & Technology mandate on an interim basis | Leadership Change | [media4growth](https://www.media4growth.com/talent/people/manish-guptaa-takes-charge-as-chief-marketing-officer-of-pizza-hut-india-79653?amp=1) (fetched) |

*No public payment-related RFP found.* Payment-infrastructure hiring: only Yum's Global PCI Manager (brand-level, US). No PSP-evaluation or orchestration job posts were found at Devyani, Sapphire, QSR Brands or Pizza Hut India.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | Feb 2025 | Yum launches Byte by Yum!, consolidating ordering, POS and delivery tech across its brands | Platform that still serves Pizza Hut Ex-China under the TSA | [BusinessWire](https://www.businesswire.com/news/home/20250206765566/en) [SS] |
| 2 | 20 Jan 2025 | Razorpay and Cashfree pause integrations via third-party routing/orchestration platforms | Directly affects any orchestration pitch on India's Razorpay leg | [Entrackr](https://entrackr.com/news/after-phonepe-razorpay-and-cashfree-suspend-direct-integrations-with-juspay-8638638) (fetched in the Jubilant report) |
| 3 | ~2020 | Touch 'n Go eWallet RM5 dine-in promo with Pizza Hut Malaysia | Only TNG link found; no current partnership evidence | [TNG T&C PDF](https://cdn-web.tngdigital.com.my/images/awesome-pizza/doc-20jan/pizza-tnc.pdf) [SS] |
| 4 | ~2020 | 346 Devyani outlets enabled for BHIM UPI at POS via HDFC Bank BharatQR | In-store only; old | [NPCI](https://npci.org.in/newsletter/January-2020/power-of-partnerships.html) [SS] |

No provider removals found. No 2025–26 India payment news found.

---

### Section 8: Checkout Experience Audit

*Full checkout flow not accessible (both are JS apps requiring a cart and address). Findings are limited to publicly observable elements in page HTML and JS.*

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | IN: custom React SPA on the global Pizza Hut platform (`api.pizzahut.io`). MY: Fynd Commerce hosted storefront | N/A | Custom-built / platform |
| Guest checkout | MY: "Continue as Guest" string present. IN: not observed | Fair (MY) | Untested |
| Steps to complete payment | Not observed | N/A | |
| Card input experience | IN: Cybersource Microform / Secure Acceptance Silent Post in the codebase (hosted fields); Razorpay and Paytm redirect or hosted | N/A | India live use of Cybersource unconfirmed |
| Payment methods visible | See Section 4 | N/A | |
| Location-based method display | Per-market builds (`in.*.js`); per-market Fynd config in MY | N/A | |
| Instalment / EMI | Not relevant at this ticket size; `PAYLATER_*` enums in the shared code | N/A | |
| 3DS implementation | Cardinal Commerce 3DS (Cybersource) flows in the shared code | N/A | India use unconfirmed |
| PCI indicator | Hosted fields and redirects, no self-hosted card fields observed | N/A | |
| Mobile responsiveness | Web is 86–92% mobile, but most orders are in-app | N/A | Apps not analysed |
| Multi-currency / local pricing | Local currency (INR; MYR in Fynd state) | Good | |
| Saved payment methods | MY: Fynd RBI-style card-save copy is platform boilerplate; IN: not observed | N/A | |
| Error message clarity | Complaints show the app reporting "failed" while the PSP reports success | Poor (from complaints) | See Section 5 |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found for Pizza Hut India, Devyani, Sapphire, QSR Brands or pizzahut.com.my. Yum ran a Global PCI programme (Internal Security Assessor role) covering Byte Commerce and Pizza Hut | [Built In Chicago job](https://www.builtinchicago.org/job/global-pci-manager/9989760) (fetched) |
| Card data handling | Not found. See inference below | — |
| Recommended Yuno integration | IN: back-to-back API behind the existing global web platform. MY: depends on Fynd's PG extension model. `[INFERENCE, not confirmed]` | — |

`[INFERENCE, not confirmed]`: Based on Cybersource Microform / Secure Acceptance and hosted Razorpay and Paytm flows in the India bundle, card data likely never touches Pizza Hut's servers (SAQ A / A-EP-style scope).

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: The India "money deducted, no order" loop is a reconciliation problem across three rails**
> **Evidence:** Section 5 (Jan 2026 Paytm + GPay double debit with PSP `SUCCESS`; Voxya series 2023–25; Play reviews) + Section 3A (three direct PSP integrations, `RazorpayPollingModal`) + Section 8 (app shows "failed" while the PSP shows success).
> **Pain Point:** Each incident triggers a refund under a 21-business-day window ([FAQ](https://online.pizzahut.co.in/faqs)), plus support cost and lost repeat orders. Store-level redirection of refund queries (Sep 2025 complaint) suggests no central owner.
> **Yuno Value Proposition:** One status and webhook model across Razorpay, Paytm and PhonePe, with idempotent order creation and automated reconciliation and refunds. Failover sits behind a single integration.
> **Best Success Case:** Arcos Dorados — replaced "a fragmented mix of PSPs and acquirers with a single platform" across 2,400+ restaurants. Same franchisee-of-a-global-QSR profile.
> **Outreach Angle:** "Your Paytm gateway said SUCCESS and your app said failed — twice, for the same customer, in January. When three rails show the same symptom it's usually the handoff, not the PSP."
> **Suggested Subject Line:** "SUCCESS at the gateway, nothing in the app"
> ⚠️ Clear the Razorpay orchestrator question (Section 7 #2) first.

> **Insight #2: Devyani becomes India's only Pizza Hut and KFC operator — one buyer, two brands, one payments conversation**
> **Evidence:** Section 6 #3 (merger, revised scheme Aug 2026; ~3,000 stores combined [SS]) + Section 2 (Sapphire's Sri Lanka subsidiary; Devyani international stores) + Section 3A (India web channel PSPs are wired by the global platform, so the franchisee may not own them).
> **Pain Point:** Post-merger integration of two operators' payment contracts, in-store POS acquiring and own-channel reporting across India and Sri Lanka. It's unclear which of these the franchisee controls versus the brand platform. `[INFERENCE, not confirmed]`
> **Yuno Value Proposition:** Consolidate acquiring relationships under one orchestration layer without re-integrating each channel, and give a unified view across brands and countries.
> **Best Success Case:** Arcos Dorados — "consolidated, acquired, and deployed tokenized payments" across 21 countries.
> **Outreach Angle:** Run this as a **separate Devyani account** after the merger clears CCI/NCLT. Lead on consolidation, not on Pizza Hut alone.
> **Suggested Subject Line:** "One operator, two brands, how many acquirers?"

> **Insight #3: Malaysia just replatformed. The only opening is the payment layer Fynd brought with it**
> **Evidence:** Section 6 #4 (Fynd relaunch ~Mar 2026) + Section 3B (TAL Juspay unverified; Fynd's native Juspay PG) + Section 4 (no wallet brand or FPX named publicly) + Section 5 (Play reviews: payment failed after the account was charged).
> **Pain Point:** Unknown until confirmed. If Malaysian wallets and FPX run through an India-centric platform's PG extensions, local rail depth and approval performance are worth asking about. `[INFERENCE, not confirmed]`
> **Yuno Value Proposition:** Local Malaysian rails (FPX, DuitNow, TNG, GrabPay, Boost) and acquirer choice behind one integration, independent of the commerce platform.
> **Best Success Case:** Arcos Dorados.
> **Outreach Angle:** **Run through QSR Brands, not Pizza Hut.** Discovery question: "Which acquirer sits behind 'E-Wallets' on the new app, and did it change with the relaunch?"
> **Suggested Subject Line:** "After the relaunch: who's behind 'E-Wallets'?"

> **Insight #4 (hand-off, not Prateek's): the LongRange TSA exit is a global replatforming window**
> **Evidence:** Section 6 #1 (Byte by Yum! continues under a TSA) + Section 3A (one global web codebase carrying Worldpay, HiPay, VTEX, Cybersource, Razorpay, Paytm and PhonePe across markets) + the competitor orchestration in Section 11 (Jubilant in-house; Juspay lists McDonald's and Burger King).
> **Pain Point:** When the TSA ends, Pizza Hut Ex-China must own a multi-market commerce and payments stack it currently rents. `[INFERENCE, not confirmed]`. No TSA end date was found.
> **Outreach Angle:** Route to the NA/global team. The decision-maker is US-based.

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks** (India hooks only after the Razorpay clearance; Malaysia hooks via QSR Brands):
1. "A Pizza Hut India customer paid ₹403.20 twice in January, once by Paytm and once by GPay. Both gateways said success; the app said failed both times."
2. "Your India FAQ gives a 21-business-day window for 'payment debited but order not placed'. That window is the cost of the reconciliation gap, not the gap itself."
3. "Arcos Dorados, the largest McDonald's franchisee, replaced a patchwork of PSPs and acquirers across 2,400+ restaurants with one platform. The franchisee owned the decision, not the brand."

**Cold call openers:**
1. "With Sapphire folding into Devyani, who ends up owning payments for the combined KFC and Pizza Hut estate?"
2. "On the new Pizza Hut Malaysia app, which acquirer sits behind 'E-Wallets', and did that change with the relaunch?"
3. "When Paytm says success and your app says failed, whose queue does that land in today: the store, the app team or the PSP?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| Domino's India (Jubilant FoodWorks) | dominos.co.in | India | ~3,636 stores; FY26 rev ₹9,512.51 cr | India, Sri Lanka | **In-house `unifiedpayment`** over 7 gateways incl. Razorpay, PayU, BillDesk, Paytm | `2-ready-to-outreach/jubilant-foodworks.md` |
| Domino's Malaysia (Domino's Pizza Enterprises) | dominos.com.my | Australia (DPE) | 287 stores MY/SG/KH at 2022 acquisition | Malaysia, Singapore | Not found | [Inside Retail](https://insideretail.com.au/business/financial/dominos-pizza-buys-businesses-in-three-southeast-asian-markets-202208) [SS] |
| McDonald's India W&S (Westlife / Hardcastle) | mcdelivery.co.in | India | 482 restaurants (30 Jun 2026) | India | TAL: Juspay (unverified). Juspay lists "McDonald's" (market unstated). Simpl (2023) | [restaurantindia](https://www.restaurantindia.in/news/westlife-foodworld-q1-fy27-revenue-rises-12-percent-to-rs-736-billion.n16867) [SS]; [juspay.io/customer-stories/mcdonalds](https://juspay.io/customer-stories/mcdonalds) (fetched) |
| Burger King India (Restaurant Brands Asia) | burgerking.in | India | 577 restaurants (Dec 2025); ownership changing | India, Indonesia | TAL: Juspay. Juspay lists "Burger King" (market unstated) | [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/india-cci-approves-lfpl-led-150257100.html) [SS]; juspay.io index (fetched) |
| KFC India (Devyani / Sapphire) | online.kfc.co.in | India | Same operators | India | Not found (app published under Yum! Restaurants India) | [App Store](https://apps.apple.com/in/app/kfc-india-online-ordering-app/id915824379) [SS] |
| McDonald's Malaysia (Gerbang Alaf) | mcdonalds.com.my | Malaysia | ~300 outlets (2020) | Malaysia | eGHL (2020) | [The Edge](https://theedgemalaysia.com/article/ghls-online-payment-arm-enables-wider-mcdelivery-payment-options) [SS] |
| Marrybrown | marrybrown.com | Malaysia | Not verified | Malaysia | Not found | TAL only |

#### 11B. Industry Peers

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| QSR Brands | qsrbrands.com.my | QSR operator | MY, SG, BN, KH | Pizza Hut Malaysia's own parent; multi-brand, multi-country | TAL; Agent 1 [SS] |
| Yum China | yumchina.com | QSR operator | China | Now owns Pizza Hut China outright; app/mini-program volume | TAL; SEC 8-K |
| Jollibee Foods | jollibee.com.ph | QSR operator | PH + intl | Direct PSPs (Maya, GCash), no orchestrator | `2-ready-to-outreach/jollibee-foods-corp.md` |
| ZUS Coffee | zuscoffee.com | F&B chain | Malaysia | Single gateway (Fiuu) in app | `2-ready-to-outreach/zus-coffee.md` |
| Sarimelati Kencana (Pizza Hut Indonesia) | — | QSR operator | Indonesia | Separate Pizza Hut franchisee; IDX-listed | [IDN Financials](https://www.idnfinancials.com/news/61626/pizza-hut-issuer-explores-new-business-as-core-operations-slow-down) [SS] |
| Starbucks Malaysia (Berjaya Food) | starbucks.com.my | F&B licensee | Malaysia | Licensee of a global brand | TAL |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| McDonald's (market not stated; Pluxee mention hints India `[INFERENCE]`) | Juspay (Payment Orchestration, Tokenization, Offers) | Not dated | QSR | [juspay.io/customer-stories/mcdonalds](https://juspay.io/customer-stories/mcdonalds) (fetched) |
| Burger King (market not stated) | Juspay | Not dated | QSR | [juspay.io/customer-stories](https://juspay.io/customer-stories) (fetched index) |
| Starbucks (market not stated) | Juspay | Not dated | F&B | same index |
| Arcos Dorados (McDonald's LATAM) | **Yuno** | Not dated | QSR | [y.uno](https://y.uno/en/success-stories/mcdonalds) (fetched) |
| Jubilant FoodWorks (Domino's India) | In-house `unifiedpayment` | — | QSR | `2-ready-to-outreach/jubilant-foodworks.md` |

#### 11D. Prospect Scoring (verified signals only; quick pass)

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| QSR Brands: 3+ countries | 3 | ✅ (MY/SG/BN/KH entities claimed) | qsrbrands.com [SS] — verify |
| QSR Brands: competitor using orchestration | 2 | ✅ (same as Pizza Hut) | 11C |
| Devyani: multiple countries | 3 | ✅ India + international stores (400 international [SS]) | BOB research [SS] |
| Devyani: payment issues (Pizza Hut India app) | 2 | ✅ | Section 5 |

Full scoring requires a dedicated `/research` run for each.

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Devyani International | Peer / successor buyer | India, Sri Lanka, intl | Not scored | High | Sole Indian Pizza Hut + KFC operator post-merger | ❌ **No — genuine find** |
| 2 | QSR Brands | Parent of target | MY, SG, BN, KH | Not scored | High | Pizza Hut + KFC across 2–4 markets | ✅ P1 (stub in 1-to-outreach) |
| 3 | Domino's Pizza Malaysia (DPE) | Competitor | MY, SG, KH | Not scored | Medium | 287+ stores; no PSP found | ✅ P1 (stub) |
| 4 | Yum China | Peer | China | Not scored | Medium | Took Pizza Hut China in-house | ✅ P1 (stub) |
| 5 | Westlife Foodworld (McDonald's W&S) | Competitor | India | Not scored | Medium (displacement) | TAL Juspay | ✅ as Hardcastle Restaurants, P3 |
| 6 | Restaurant Brands Asia (BK India/ID) | Competitor | India, Indonesia | Not scored | Medium (displacement) | Ownership change; TAL Juspay | ✅ as Burger King India, P2 |
| 7 | Sarimelati Kencana (Pizza Hut ID) | Peer | Indonesia | Not scored | Medium | Separate Pizza Hut franchisee | ❌ No |
| 8 | Marrybrown | Competitor | MY + intl | Not scored | Low–Med | — | ✅ P1 (stub) |
| 9 | Jubilant FoodWorks | Competitor | India, SL, BD | 18/29 (existing file) | High | In-house orchestration | ❌ Not in TAL; file exists |
| 10 | Starbucks Malaysia (Berjaya Food) | Peer | Malaysia | Not scored | Low | — | ✅ P1 |

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | Not found for "Pizza Hut APAC". India Pizza Hut: Devyani ~₹184 Cr (Q1 FY27) and Sapphire ~₹136 Cr (Q1 FY27) | [DSIJ](https://insights.dsij.in/markets/reports/report-details/devyani-international-ltd/44862), [Kalkine](https://www.kalkine.co.in/article/announcements/sapphire-foods-nsesapphire-what-drove-15-revenue-growth-in-q1-fy27) [SS]. QSR Brands: FY2025 revenue +31% across KFC and Pizza Hut Malaysia, no ringgit total ([NST](https://www.nst.com.my/amp/business/corporate/2026/01/1364282/qsr-brands-posts-31pct-revenue-growth-kfc-pizza-hut) [SS]) |
| GMV / Gross Transaction Volume | Not found | — |
| Average Transaction Value (USD) | **Not found** | No sourced Pizza Hut India or Malaysia AOV |
| Est. Annual Transactions | Cannot be calculated | Missing ATV |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. [ASSUMPTION — not researched.]** Basis: ~970 India Pizza Hut stores and ~₹107 Cr/month combined India Pizza Hut revenue across all channels (summing the two quarterly figures ÷ 3, both [SS]), plus ~400 Malaysian stores [SS]. Even a small own-channel share at QSR ticket sizes clears 100k orders/month, but no AOV or channel split is sourced. **Billing unit:** one consumer order paid on Pizza Hut's own web or app. Aggregator-paid orders and dine-in POS are excluded from what an e-commerce orchestrator would see. | Disclosure rule |
| Active Customers / Users | Not found | — |
| Primary Currency | INR (India), MYR (Malaysia) | Site state / bundle |
| Top 3 Markets by Revenue | Not found on a comparable basis | — |
| Billing channel split (web vs app store) | Not applicable (food orders are not app-store IAP). Own app vs aggregator split: not found. Sapphire delivery is 43% of revenue mix, Q1 FY27, all brands ([Quartr](https://quartr.com/events/sapphire-foods-india-limited-sapphire-investor-presentation_FP72PB3G) [SS]) | — |

---

### Overall Research Confidence

**Medium.**
- **Strong:** the PSP stack for India (live JS bundle, re-verified); Malaysia's platform (Fynd, from page HTML); the brand sale (SEC 8-K, fetched); Malaysia payment-method wording (T&C, fetched); one dated India complaint (fetched).
- **Weak:** all operator financials and store counts (search summary only; NSE PDFs 403); Malaysia's PSP and orchestrator (unverified); the live checkout in both markets (not reached); the mobile apps where most orders happen (not analysed).
- **Traffic was supplied** (SimilarWeb Sales Intelligence, Jul–Sep 2026), but it is web-only, top-10-only, shares-only, and limited to three domains. One of those is 97% US.

---

### Manual Research Recommendations

> **Area:** Monthly transaction count
> **Why it matters:** The only signal that can reject the account; currently assumed.
> **Suggested manual action:** Open the Devyani Q1 FY27 press release (https://nsearchives.nseindia.com/corporate/DEVYANI_29072026130146_Press_Release30062026_sd.pdf) and the Sapphire deck in a browser for Pizza Hut ADS, AOV and delivery or own-app mix. Do the same in QSR Brands filings for Malaysia.

> **Area:** Malaysia orchestrator (TAL says Juspay)
> **Why it matters:** It decides greenfield versus displacement for QSR Brands.
> **Suggested manual action:** Place a test order on pizzahut.com.my with DevTools open and look for `api.juspay.in` / Hyper SDK versus iPay88, Fiuu or eGHL endpoints.

> **Area:** Razorpay and orchestration in India
> **Why it matters:** Razorpay is India's main web PSP and paused third-party router integrations in 2025.
> **Suggested manual action:** Ask Yuno Solutions/Partnerships whether Razorpay volume can be routed today.

> **Area:** Who owns India payment decisions: brand platform or franchisee?
> **Why it matters:** It decides whether Devyani can buy at all for the web and app channel.
> **Suggested manual action:** Check the pizzahut.co.in footer for the operating entity. On a first call with Devyani, ask who contracts the online PSPs.

> **Area:** Other APAC Pizza Hut markets (AU, ID, TH, SG, HK/TW)
> **Why it matters:** These were not in the traffic pull; each is a separate operator and potential account.
> **Suggested manual action:** Pull SimilarWeb for pizzahut.com.au, pizzahut.co.id and pizzahut.com.sg only if those operators are worth separate runs. Sarimelati (ID) is not in the TAL.

---

### Appendix: All Source URLs

**Traffic:** `accounts/traffic/pizza-hut.md` (SimilarWeb, supplied 2026-10-19)

**Section 1–2 (entities, corporate):**
- https://www.sec.gov/Archives/edgar/data/0001041061/000119312526271893/d158986dex991.htm (fetched)
- https://www.sec.gov/Archives/edgar/data/0001041061/000104106126000187/a8kex991912026.htm
- https://www.nrn.com/restaurant-finance/pizza-hut-s-sale-to-longrange-capital-is-complete
- https://www.qsrmagazine.com/news/yum-brands-completes-sale-of-pizza-hut-to-longrange-capital/
- https://www.smartcompany.com.au/hospitality/pizza-hut-sliced-up-3-8-billion-deal/ (reports "$3.8 billion"; conflicts with the SEC's US$2.7bn, likely AUD)
- https://www.plunkettresearch.com/?p=1889612
- https://www.pizzahut.com.my/terms-and-conditions (fetched)
- https://insights.dsij.in/markets/reports/report-details/devyani-international-ltd/44862
- https://www.barodaetrade.com/Reports/DevyaniInternational-Q1FY27ResultReview29Jul26-Research.pdf
- https://www.kalkine.co.in/article/announcements/sapphire-foods-nsesapphire-what-drove-15-revenue-growth-in-q1-fy27
- https://business-standard.com/amp/topic/yum
- https://www.sundaytimes.lk/260621/news/india-franchisee-woos-pizza-hut-sri-lanka-operator-while-yum-brands-sheds-chain-646689.html
- https://qsrbrands.com/?p=9215
- https://restaurantbusinessonline.com/financing/greg-flynn-goes-global-australian-pizza-hut-acquisition
- https://insideretail.com.au/sectors/food-beverage/pizza-hut-plots-10-million-complete-reset-in-australia-202609
- https://www.idnfinancials.com/news/61626/pizza-hut-issuer-explores-new-business-as-core-operations-slow-down
- https://www.seatrade-maritime.com/asia/thoresen-thai-bulks-pizza-hut-thailand-buy
- https://www.mpu.edu.mo/careerfair/assets/files/F2-1.pdf

**Section 3 (PSPs, orchestration, PCI):**
- https://www.pizzahut.co.in/order/js/in.4244cdc0c48062144e76.js (pulled)
- https://www.pizzahut.com.my/ (pulled)
- https://docs.fynd.com/commerce/set-up-website/payments/juspay/add-juspay
- https://juspay.io/customer-stories (fetched)
- https://juspay.io/customer-stories/mcdonalds (fetched)
- https://www.businesswire.com/news/home/20250206765566/en
- https://www.builtinchicago.org/job/global-pci-manager/9989760 (fetched)
- https://npci.org.in/newsletter/January-2020/power-of-partnerships.html
- https://entrackr.com/news/after-phonepe-razorpay-and-cashfree-suspend-direct-integrations-with-juspay-8638638

**Section 4 (APMs):**
- https://www.pizzahut.com.my/en/terms-and-conditions (fetched)
- https://online.pizzahut.co.in/faqs (fetched)
- https://play.google.com/store/apps/details?id=com.phdv.universal&hl=en_IN (fetched)
- https://play.google.com/store/apps/details?id=com.pizzahut.malaysia (fetched)
- https://restaurants.pizzahut.co.in/pizza-hut-ph-bardoli-pizza-restaurant-baben-bardoli-129248/Home

**Section 5 (complaints):**
- https://www.consumercomplaints.in/pizza-hut-india-money-deducted-two-times-from-upi-paytm-and-google-pay-but-no-order-placed-on-app-unable-ro-reach-company-for-refund-c3539095 (fetched)
- https://voxya.com/consumer-complaints/payment-done-but-food-order-not-placed/209034
- https://voxya.com/consumer-complaints/order-canceled-amount-deducted-no-refund-yet/218366
- https://voxya.com/consumer-complaints/amount-refund/220158
- https://voxya.com/consumer-complaints/order-pizza-payment-done-but-order-is-not-showing-on-app/242241
- https://voxya.com/consumer-complaints/refund-pending-since-august-2025-order-cancellation/251222
- https://voxya.com/consumer-complaints/payment-was-successful-but-the-company-denied/21706

**Section 6–7 (developments, news):**
- https://news.bloomberglaw.com/mergers-and-acquisitions/kfc-pizza-hut-india-operators-to-merge-in-933-million-deal-2
- https://www.outlookbusiness.com/corporate/devyani-sapphire-merger-to-create-qsr-giant-with-nearly-3000-stores
- https://www.sahi.com/news/devyani-international-changes-merger-plan-as-mutual-agreement-ends-secondary-sale-deal-3433-PE1_COR
- https://www.tijorialerts.com/companyUpdates/devyani-international-gets-nse-bse-no-objection-for-sapphire-merger-108653/
- https://www.media4growth.com/talent/people/manish-guptaa-takes-charge-as-chief-marketing-officer-of-pizza-hut-india-79653?amp=1 (fetched)
- https://cdn-web.tngdigital.com.my/images/awesome-pizza/doc-20jan/pizza-tnc.pdf
- https://www.nst.com.my/amp/business/corporate/2026/01/1364282/qsr-brands-posts-31pct-revenue-growth-kfc-pizza-hut

**Section 11 (competitors):**
- https://y.uno/en/success-stories/mcdonalds (fetched)
- https://insideretail.com.au/business/financial/dominos-pizza-buys-businesses-in-three-southeast-asian-markets-202208
- https://www.restaurantindia.in/news/westlife-foodworld-q1-fy27-revenue-rises-12-percent-to-rs-736-billion.n16867
- https://finance.yahoo.com/markets/stocks/articles/india-cci-approves-lfpl-led-150257100.html
- https://apps.apple.com/in/app/kfc-india-online-ordering-app/id915824379
- https://theedgemalaysia.com/article/ghls-online-payment-arm-enables-wider-mcdelivery-payment-options
- `2-ready-to-outreach/jubilant-foodworks.md`, `2-ready-to-outreach/jollibee-foods-corp.md`, `2-ready-to-outreach/zus-coffee.md`

**Section 12:**
- https://quartr.com/events/sapphire-foods-india-limited-sapphire-investor-presentation_FP72PB3G

`[SS]` = `[UNVERIFIED — search summary only, page not fetched]`.

</details>
