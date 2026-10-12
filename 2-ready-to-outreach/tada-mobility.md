# TADA Mobility

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 19 / 29 → ⭐ **High Priority**
**Industry:** Mobility & Ridesharing — zero-commission ride-hailing (MVL / Mass Vehicle Ledger group; brands TADA, Throo, COOP) · **HQ:** Singapore — **TADA Mobility (Singapore) Pte. Ltd.**, 63 Ubi Road 1 #01-48, Oxley Bizhub, Singapore 408728; group parent **MVL Foundation Pte. Ltd.** (Singapore) · **Researched:** 2026-10-12 · **First email sent:** —
**Motion:** **GREENFIELD (qualified)** — Stripe confirmed as the sole named PSP via Stripe's own customer story; no orchestrator detected anywhere. But they already *buy* acceptance optimisation from Stripe (Adaptive Acceptance), so skip the "you need orchestration" education layer and lead on the markets and rails Stripe does not acquire in.
**⭐ PITCH SPINE (build the sequence on this):** In a zero-commission model, **payment success IS revenue collection.** Their own HK rider terms put TADA in the money flow as the driver's *"payment collection agent"* — ***"unless paid in cash"*** — and send a declined rider to settle the fare **and TADA's platform fee** in cash **directly with the driver**. So a decline is not an abandoned cart; it is a receivable against their own driver. See **Insight #1** in Section 10.
**⛔ DO NOT lead on approval rates.** TADA publishes a **98% authorisation rate** (+2.8% from Adaptive Acceptance, 0% disputes). Concede it and attack its denominator — cash rides and riders lost to a missing rail are not in that number. See the **Approval-Rate Dossier** in Section 10.

---

> ## 🔒 PHASE 0 NOTE — read before anything else
>
> **"Tada" appears on Yuno's own site-wide customer logo wall.** Verified live by Prateek: `https://y.uno/en` serves `/logos/tada_logo.svg` with `alt="Tada"`, and the name is quoted in this repo's outreach library — *"McDonald's, Samsung, Uber, Carrefour, Ant Group, NetEase, Crypto.com, Qatar Airways, Rappi, inDrive, Copa Airlines, Despegar, Garena, GoFundMe, Hotmart, Viva Aerobus, Kavak, Moon Active, Whop, Reserva, **Tada**, Livelo, Wingo, and many more."* (`.claude/commands/full-outreach.md` L543–545).
>
> **Which Tada could not be determined from the asset.** The SVG is pure path data with no `<title>`/`<desc>`; `/en/success-stories/tada` 404s. Prateek's labelled inference was that it is more likely **TaDa Delivery** (AB InBev's LATAM app), given the LATAM-heavy logo neighbourhood — and the list position supports that: "Tada" sits between **Reserva** and **Livelo**, both Brazilian Yuno cases.
>
> **✅ Prateek confirmed on 2026-10-12 that TADA Mobility is NOT a Yuno customer.** The Phase 0 existing-customer gate is **cleared on that basis**. Nobody needs to rediscover this. If the question resurfaces, the resolution is Prateek's confirmation, not the logo wall.
>
> ⚠️ **Operational consequence:** do not name "Tada" from Yuno's customer list in any outreach — to this account or any other — until the logo is positively attributed. Naming it to TADA Mobility would be read as naming them as an existing customer.

---

> ## ⚠️ METHOD DEVIATIONS AND DATA GAPS — disclosed up front
>
> ### 1. 🚨 NO TRAFFIC DATA WAS SUPPLIED, AND NONE WAS OBTAINED
> `accounts/traffic/` contains no `tada.md` or `mvl.md` file, and none was pasted into the conversation. **No SimilarWeb data of any kind underpins this report.** Consequences, per the skill's own rule:
> - **Section 1 (Website Traffic Analysis) cannot be completed.** No country split is given. None is invented.
> - The country profile in Quick Look is marked **`[ESTIMATE, not confirmed]`** and is built from operating-market evidence (geofences, legal entities, support addresses, press), **not** from traffic.
> - **Two ICP signals are unverifiable and therefore score 0:** *"High traffic outside home"* (needs home-country share <60% from Section 1) and the traffic-weighted ranking of rail gaps.
> - **Overall Research Confidence is downgraded one level on this basis** — see that section.
> - A `site:similarweb.com` WebSearch fallback was available but was **not spent**, for the reason below.
>
> ### 2. ⭐ Web traffic would be a BAD proxy here even if we had it
> TADA is **app-first ride-hailing**. There is no web checkout: `tada.global` is a Vite marketing SPA with no cart, no card fields and no payment route; `go.tada.global` is a live-trip share/tracking page. Every fare is paid inside a native app. A SimilarWeb visit count would measure brochure traffic and app-store hand-offs, not transactions. **App and ride metrics are the right proxies, and those were found** — see Section 1-ALT and Section 12.
>
> ### 3. ⛔ No subagents — single-threaded execution
> The Agent/Task tool was **not available** in this run. Phases 1 → 2 → 3 were executed **sequentially by one analyst**, with the five per-agent search/fetch budgets treated as one pooled budget per workstream. Nothing in the method was skipped, but the parallel cross-checking that normally comes from five independent agents was replaced by one pass plus two independent scans by the coordinating analyst (whose bundle findings are reconciled, including one divergence, in Source Notes).
>
> ### 4. WebFetch vs curl
> WebFetch was not used. All fetching was done with Bash `curl -sS -L --compressed`, which is confirmed working. `--compressed` was mandatory: `tada.global` and `policy.tada.global` both return `content-encoding: br`, and an uncompressed fetch would have returned zero on every vendor grep.
>
> ### 5. Fetches that failed (403 at origin, not at our proxy)
> `businesswire.com` (the 24 Mar 2026 TADA US-entry release), `ababank.com` (both KHQR pages) and `axios.com` (Throo Denver) all returned **HTTP 403**. Claims that rest only on those are labelled `[UNVERIFIED — search summary only, page not fetched]`. The BusinessWire headline figure is independently confirmed by a fetched PRNewswire copy, so nothing load-bearing depends on a blocked page.

---

---

> ## 🔍 ANALYST AUDIT — Prateek, 2026-10-12
>
> I verified the load-bearing claims in this report personally against live sources rather than accepting them, and I ran an independent scan of the payment bundle **before** reading the research so my baseline was not anchored on its conclusions. What follows is what the audit changed.
>
> ### ✅ Verified verbatim against the live Stripe case study (`stripe.com/customers/tada`, HTTP 200)
> The page is real and is **positively this TADA** — it names Kay Woo, MVLLABS, Kenneth Tay (Head of Product), and the SG/KH/VN/TH/HK market set. Confirmed word-for-word: *"processed in Singapore dollars (SGD)"* · *"Riders can use the card they store in their account profile across all the countries that TADA operates in"* · *"Adaptive Acceptance, which uses machine learning to optimize authorization requests, retries, and routing combinations"* · *"we have maintained a 0% dispute rate"* · *"we increased authorization rates by 2.8%, so we now process 98% of all transactions"* · *"Regional payment integration processes usually take a lot of time"* (Kenneth Tay) · PromptPay as something TADA *"hopes to"* add. **The motion classification stands.**
>
> ### ✅ Verified verbatim against Fortune
> The 78–92¢ flat driver software fee, the 11.1% 2022 Singapore share (Measurable AI), the 2019 Cambodia/Vietnam and 2024 Thailand/Hong Kong launches, and the Denver trial are all in Fortune's own prose.
>
> ### ✅ Verified myself in the production bundle
> The `payment_*` catalogue, and the zero-occurrence results for Bakong, KHQR, PayNow, PromptPay, TrueMoney, QRIS, GoPay, OVO, DANA, ZaloPay, VNPay, VietQR, NAPAS, GrabPay, Octopus and AlipayHK. Also: **no PSP, gateway or orchestrator name appears anywhere in the 839KB bundle** (31 vendors checked). Markets independently corroborated two ways — the merchant's own *"our offices in Singapore, Cambodia, Thailand, Vietnam, and Hong Kong"* string, and embedded local emergency-service links (Thai police + NIEMS, SCDF + SG police, HK police). `tada.global` serves **no CSP header**, so there is no asset map for this account.
>
> ### ⚠️ What the audit CHANGED in this file
> 1. **A direct contradiction, fixed.** `payment_momopay_p` was assigned to **Cambodia** in Section 4 and to **Vietnam** in Section 3A. Its market is **not evidenced either way**; it is now marked unresolved in both places.
> 2. **"Five Cambodian integrations" cut to four.** The evidence line said five while every outreach-facing line said four. **Four is now the figure everywhere** — it is the defensible floor and every name in it is unambiguously Cambodian.
> 3. **A caveat added on all per-market attribution.** The i18n block is a **single flat object with no market grouping** — I read it directly. The catalogue proves which methods exist, not which market each serves. Absences are unaffected and remain robust.
> 4. **A rebuttal risk added to Insight #2 (the SGD/cross-border one).** The same Stripe page says TADA wanted *"credit card payments using **local currencies**"*, which a prospect can answer the SGD observation with. Ask, do not assert.
> 5. **Revenue provenance downgraded.** Fortune **hyperlinks the $19.8M to `getlatka.com`**, a third-party aggregator — it is not a company disclosure. Volume Derivation B is weakened accordingly; **lead with Derivation A**.
>
> ### ❌ What I could NOT confirm
> - **Ryde's listing venue** — `rydesharing.com` names none. Do not edit the TAL on this without an exchange or SEC source.
> - **The acquirer behind the eight local wallet rails** — the single highest-value open question. Resolving it moves this account to 22/29.
> - **The cash-vs-digital split** — unresolved, and it is what sizes the business case. Does not change the tier.
>
> ### ✔️ Safety checks passed
> No credential value is transcribed anywhere (presence named, value withheld — grep-verified). No calendar or booking link. No Yuno competitor appears outside the internal negative-check lists and the India peer rows where the TAL itself names them. ICP arithmetic re-added independently: **5+4+3+0+3+2+0+0+0+2+0 = 19 across 11 rows.** ✅
>
> ### 📝 A trap worth adding to the environment list
> **Smart quotes defeat a straight-apostrophe grep.** My check for `"let's ride"` returned **zero** and I nearly flagged the quote as fabricated — the page uses U+2019 (`let’s`). The quote is genuine. Always test both apostrophe forms before calling a quote unsourced.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** TADA is a zero-commission ride-hailing platform launched in Singapore in 2018 by Kay Woo and Jay Han, operated by **TADA Mobility (Singapore) Pte. Ltd.** under the **MVL (Mass Vehicle Ledger) / MVL Foundation Pte. Ltd.** group. It takes no percentage of driver fares — instead it charges the driver a **flat per-ride software fee of roughly US$0.78–0.92** and the rider a **booking/app fee ("Platform Fees")**, and acts as the drivers' **payment collection agent** for card and wallet fares. It runs in **Singapore, Cambodia, Vietnam, Thailand and Hong Kong**, and since June 2026 in the **United States** under a separate brand, **Throo** (New York City, TLC-licensed) and **COOP** (Colorado). The company claims **more than 150 million rides and nearly US$2 billion in cumulative GMV**.

**SimilarWeb total visits (last full month):** ❌ **NOT AVAILABLE — no traffic data supplied, none obtained.** See the methods box above. App-first business; web traffic would be a poor volume proxy regardless.

### Top 5 markets — `[ESTIMATE, not confirmed]`
> ⚠️ **This is NOT a traffic ranking.** No traffic data exists for this account. The ordering below is a reasoned ranking from operating evidence (city-count in the production geofence, entity presence, localisation depth, press), and it is explicitly labelled an estimate. Do not quote the rank order as measured.

| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 `[EST]` | **Cambodia** (Phnom Penh, Siem Reap, Sihanoukville, KPK) | ❌ No data | Cash · Credit/debit card · **ABA Pay** · **Wing Pay** · **Pi Pay** · **Chip Mong Pay** · **MOMO Pay** · TADA Wallet (stored value) · Apple Pay · Google Pay · Alipay+ · Corporate | 🚩 **Bakong** · 🚩 **KHQR** (the national interoperable QR rail — absent, while four of its participant institutions are wired in separately) | ⚠️ No Cambodian entity found. Rider terms and privacy policy are served under the **KH** region but name no Cambodian company; the contracting party is a Singapore entity |
| 2 `[EST]` | **Singapore** | ❌ No data | Cash · Credit/debit card (Stripe, **processed in SGD**) · **NETS QR** · **OCBC Digital** · Apple Pay · Google Pay · TADA Wallet · Corporate | 🚩 **PayNow** (zero occurrences in the method catalogue) · GrabPay | ✅ **TADA Mobility (Singapore) Pte. Ltd.** — 63 Ubi Road 1 #01-48, Oxley Bizhub, Singapore 408728 |
| 3 `[EST]` | **Vietnam** (Ho Chi Minh City, Hanoi) | ❌ No data | Cash · Credit/debit card · **MoMo** · Apple Pay · Google Pay · Corporate | 🚩 **ZaloPay** · 🚩 **VNPay / VietQR** · 🚩 **NAPAS** domestic cards | ❌🔒 **No Vietnamese entity.** The Vietnamese-language rider terms contract the rider to **TADA Technologies Pte. Ltd** — a **Singapore** entity. Vietnam gates intermediary payment services behind SBV licensing; verify current rules before citing |
| 4 `[EST]` | **Thailand** (Bangkok) | ❌ No data | Cash · Credit/debit card · Apple Pay · Google Pay · Corporate · Alipay+ | 🚩 **PromptPay** — named in Stripe's own Nov-2024 case study as a planned addition; **still zero occurrences in the Oct-2026 method catalogue** · 🚩 TrueMoney | ✅ **TADA MOBILITY (THAILAND) CO., LTD.** — 2322 Pracha Songkhro Road, Din Daeng, Bangkok |
| 5 `[EST]` | **Hong Kong** | ❌ No data | Cash · Credit/debit card · Apple Pay · Google Pay · **Alipay+** · Corporate | 🚩 **FPS** · 🚩 **Octopus** · 🚩 AlipayHK as a domestic wallet (Alipay+ is the cross-border aggregator, not the same thing) | ⚠️ HK office stated by the company; **no HK entity found.** HK rider terms and privacy policy both route data disclosure *"within or outside of **Singapore**"* and are governed from Singapore |

**🚩 TAL correction:** the TAL row reads `SG/KH/VN/TH`. **Hong Kong is missing.** Sourced to TADA's own string catalogue: *"Operating across the Asia-Pacific region, our offices in **Singapore, Cambodia, Thailand, Vietnam, and Hong Kong** are ready to support you."* Corrected value: **SG/KH/VN/TH/HK** (+ US: NY/CO, out of territory).

### Legal entities
- **MVL Foundation Pte. Ltd.** (Singapore) — group parent; the named contracting party in the MVL Platform terms. Also the **Apple App Store seller** for all group apps. [Source](https://policy.tada.global/policies/mvl_terms_en_SG.md)
- **TADA Mobility (Singapore) Pte. Ltd.** (Singapore) — rider and driver contracting entity for SG; data-protection officer at 63 Ubi Road 1 #01-48, Oxley Bizhub, Singapore 408728. Also the **Google Play developer of record**. [Source](https://policy.tada.global/policies/tada_privacy_en_SG.md)
- **TADA MOBILITY (THAILAND) CO., LTD.** (Thailand) — 2322 Pracha Songkhro Road, Din Daeng Sub-district, Din Daeng District, Bangkok; `enquiries_th@tada.global`. [Source](https://policy.tada.global/policies/tada_privacy_en_TH.md)
- **TADA Technologies Pte. Ltd** (Singapore) — the entity named in the **Vietnamese-language** rider terms. [Source](https://policy.tada.global/policies/tada_terms_vn_VN.md)
- **Zero Commission LLC** — a **New York limited liability company**; operator of Throo. Privacy policy last revised **1 Jun 2026**, effective **2 Jun 2026**. [Source](https://policy.tada.global/policies/throo_privacy_en_NY.md)
- **Registration numbers:** Not found. No ACRA/BizFile UEN, Thai registration number or NY DOS ID was obtained — registry pages were not reachable in this environment.
- **No Cambodian, Vietnamese or Hong Kong operating entity was found in any first-party document.** Not found ≠ does not exist; see Manual Research Recommendations.

### Known PSPs
- **Stripe** — ⭐ **CONFIRMED.** `[Provider Case Study]` Stripe's own customer story, verified to be this TADA (names Kay Woo, MVLLABS, Singapore 2018, *"'let's ride' in Korean"*, four countries). Products: **Payments + Radar + Adaptive Acceptance**. Cards **processed in Singapore dollars (SGD)**, pre-authorisation holds configured, network-token-vs-PAN testing, card account updater. Published results: **0% fraudulent dispute rate · 98% authorisation rate · +2.8% authorisation-rate increase**. [Source](https://stripe.com/customers/tada) · corroborated [Nov 2024](https://techcoffeehouse.com/2024/11/07/stripe-powers-tadas-southeast-asia-expansion-amid-intense-ride-hailing-competition/)
- **Stripe (Throo / US)** — `[Terms/Privacy Policy]` Throo's own terms: *"Payment processing may be provided by third-party processors (**for example, Stripe**)."* Hedged wording; treat as indicative, not exclusive. [Source](https://policy.tada.global/policies/throo_terms_en_NY.md)
- **The acquirer behind every local APAC wallet rail — NOT FOUND.** ABA Pay, Wing Pay, Pi Pay, Chip Mong Pay, MOMO Pay, MoMo, NETS QR and OCBC Digital are all present as first-party method keys in TADA's production app catalogue, but **no source names who processes them.** Stripe does not acquire in Cambodia, so these are near-certainly separate direct integrations — but that is an inference, not a sourced fact. `[INFERENCE, not confirmed]`

### Orchestration status
**None detected — direct PSP integration only (greenfield).** Zero occurrences of Juspay, Spreedly, Primer, Gr4vy, CellPoint, Payrails, APEXX, Yuno or any other orchestrator across 839 KB of the production marketing/app bundle, 11 bundles of the rider live-trip app, the 348 KB policy-site bundle and 16 first-party legal documents in five jurisdictions. No orchestrator appears in any press coverage. The TAL's `Payment Orchestrator` column is empty and **independent verification agrees with "none"** — it is not an unchecked blank.

⚠️ **Two honest limits on that negative.** (a) These are **web** assets; the rider checkout is **native-app**, and absence in web code is not absence in the app binary. (b) `tada.global` serves **no Content-Security-Policy header at all**, so there is no CSP asset map for this account — the usual `connect-src` enumeration of payment hosts was unavailable. The classification rests on the Stripe case study plus the first-party method catalogue, not on the web greps alone.

### Buying signals
- 🚀 **US market entry, June 2026** — Throo public beta **10 Jun 2026**, official NYC debut **29 Jun 2026**, TLC-authorised, **50,000+ drivers signed up pre-launch** (company) rising to **53,000+** by August (CEO). Separate brand, separate domain, separate NY entity. A brand-new payment build in a new regulatory regime. [PRNewswire 1 Jul 2026](https://aijourn.com/throo-launches-in-new-york-city-with-lower-fares-for-riders-and-zero-commission-for-drivers/) · [NY1 21 Aug 2026](https://ny1.com/nyc/all-boroughs/news/2026/08/21/new-ride-hail-app-throo-looks-to-take-on-uber--lyft-in-new-york-city)
- 🤖 **⭐ Agentic payments API, shipped July 2026** — *"incorporating an API that lets AI agents request, track, and **autonomously pay for a ride** without a person ever opening the app."* An autonomous machine-initiated card charge is a stored-credential, MIT-flagging and agentic-commerce problem, and it is live now. [Source](https://aijourn.com/throo-launches-in-new-york-city-with-lower-fares-for-riders-and-zero-commission-for-drivers/)
- 🚀 **Third US market: Colorado** — the production config maps `CO → COOP` with a Colorado state geofence, and `NJ`/`CT` already exist in the region enum. Axios reported Throo's Denver push on 23 Sep 2026 `[UNVERIFIED — 403, page not fetched]`. [Config source](https://go.tada.global/assets/productConfig-D7RveucL.js)
- 💳 **TADA Wallet launched in Cambodia, effective 22 Jan 2025** — own stored-value balance, topped up in-app, **non-refundable and non-withdrawable**. A new pay-in flow (top-ups) distinct from per-ride charges. [Source](https://policy.tada.global/policies/wallet_terms_en_KH.md)
- 📋 **Driver-side financial products under construction** — the SG rider terms (last modified **31/12/2025**) add an on-chain loyalty addendum contemplating *"driver incentives, **cash-advance eligibility**, or other financial programs"* underwritten on on-chain ride history. [Source](https://policy.tada.global/policies/tada_terms_en_SG.md)
- ❌ **No public payment RFP found.** ❌ **No payment-related job posting found.** ❌ **No funding round in the last 12 months found.**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach TADA Mobility` to draft the 12-touch sequence, or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 19 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED: ~1.5M–2.1M completed rides per month.** Two independent derivations agree — see below and Section 12. Band ≥100,000 → **+5**. **Billing unit stated in full below; read it before quoting the number.** |
| Orchestration status | **+4** | ✅ **"None detected — direct PSP integrations only" (greenfield).** Stripe is the only named PSP; no orchestrator in 839 KB of production bundle, 11 rider-app bundles, the policy-site bundle, 16 first-party legal documents or any press. Two limits stated: web-only assets, and no CSP header to enumerate payment hosts. |
| 3+ countries | **+3** | ✅ **Verified, five APAC markets + three US states.** Own string catalogue names SG/KH/VN/TH/HK offices; production geofences exist for SG, VN, KH, HK, CO, NY (+ ET); city map lists 10 cities; three separate operating entities confirmed in legal documents (SG, TH, NY); Stripe's case study independently names SG/KH/VN/TH + HK. |
| Multiple PSPs | **0 ⬜** | ⬜ **Cannot evidence 2+ PSPs. Scored down deliberately.** Only Stripe is sourced. The eight local wallet/QR rails (ABA Pay, Wing Pay, Pi Pay, Chip Mong Pay, MOMO Pay, MoMo, NETS QR, OCBC Digital) are **confirmed as methods in TADA's own production catalogue**, but **no source names the acquirer or aggregator behind any of them.** Stripe does not acquire in Cambodia, so separate integrations are near-certain — but that is `[INFERENCE, not confirmed]` and an inference scores zero. **This row is the single best use of the discovery call.** |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Verified, two ways.** (1) **Cambodia** — `bakong` and `khqr` return **zero occurrences** in TADA's own 18-key payment-method catalogue, while KHQR's dominance is third-party sourced (**601.3M transactions / US$75.8bn in 2023; 3.3M+ merchants accepting**). (2) **Thailand** — **PromptPay** was named in Stripe's own case study as a planned addition and still returns **zero occurrences** in the October 2026 catalogue. Both absences are sourced against a first-party artefact, not assumed. |
| Recent expansion | **+2** | ✅ Throo NYC public beta **10 Jun 2026**, official launch **29 Jun 2026**; Denver/Colorado in the production config; Hong Kong launched 2024. Inside 12 months. |
| Payment issues | **0 ❌** | ❌ **Not met, and not fudged.** The complaints found are a **driver dispatch bug** (`My Destination` auto-cancelling jobs, S$1.09 penalty deductions; bug identified 13 Dec 2025, fixed in three days) and a **fare dispute**. Neither is a payment-processing failure. **No declined-transaction, duplicate-charge, failed-refund or checkout-error pattern was found** on Reddit, Trustpilot, X or app-store reviews. Awarding this row would be inventing a pain point. |
| Funding >$10M | **0 ❌** | ❌ No round in the last 12 months. Historic only: Series A **US$5M** (SV Investment-led, with Central Motor and Shimwon), total Series A later reported *"just under US$10M (S$14.2M)"*; a **US$15M Series B** for the ONiON EV programme is reported by Vulcan Post but **undated in the result** and therefore cannot be placed inside the window. |
| High traffic outside home | **0 ⬜** | ⬜ **UNVERIFIABLE — no traffic data exists for this account.** The rule requires a Section 1 home-country share below 60%. There is no Section 1. The operating footprint makes it very likely true, but **likelihood is not evidence** and this row scores zero. |
| Competitor using orchestration | **+2** | ✅ **Verified on Yuno's own public customer list.** **Uber** and **inDrive** are both named on y.uno's site-wide "TRUSTED BY GLOBAL TEAMS" list and its travel/mobility vertical list (*"Trusted by leading travel and mobility brands: **Uber, inDrive**, Avianca, Copa Airlines, Viva."*). Both are direct competitors: **Uber is Throo's named head-to-head rival in NYC**; inDrive competes with TADA across emerging markets on the same driver-economics pitch. Source is Yuno's own site rather than an independent third party — stated plainly. |
| Payment job postings | **0 ⬜** | ⬜ None found. Searched MVL Foundation and TADA Mobility for payment-engineer / payment-infrastructure roles; nothing returned. Careers pages were not reachable. |

**Total: 19 / 29.** **Tier: ⭐ High Priority (17+).** Not a boundary score — two points clear of the threshold, and it survives losing any single row except the volume row.

**No RFP override applies** — *"No public payment-related RFP found."*

#### Analyst override check — none applied, with reasoning
- **App-store-dominated revenue?** ❌ Not applicable, and this matters. Ride fares are physical-world services, not in-app digital goods, so they do **not** route through Apple/Google IAP. TADA's own revenue is a per-ride software fee billed to drivers and a platform fee billed to riders, both collected on cards/wallets outside store billing. **Orchestration can touch essentially all of it.** This is the opposite of the Section-4-subscription trap.
- **Absolute volume too small?** ❌ No. ~1.5–2.1M rides/month against a 40,000 floor.
- **Matrix double-counting?** ❌ No. "3+ countries" rests on geofences/entities; "local rail gap" rests on the method catalogue plus third-party rail-prominence data. Different evidence.
- **Regulatory reality blocking the pitch?** ❌ No. Vietnam and Cambodia gate domestic acquiring in practice, which is an argument *for* orchestration via licensed local partners, not against the account.

#### 🚨 Monthly transaction count — MANDATORY DISCLOSURE

> **✅ DERIVED: ~1,500,000–2,100,000 completed rides per month.**
>
> **Derivation A — cumulative rides ÷ elapsed time.** *"more than 150 million rides worldwide"* (company, in its own 1 Jul 2026 PRNewswire release) ÷ ~99 months since the Singapore launch in 2018 = **~1.52M rides/month** as a lifetime average. Growth-weighted, the current run-rate is **above** this, so treat 1.52M as a floor. [Source](https://aijourn.com/throo-launches-in-new-york-city-with-lower-fares-for-riders-and-zero-commission-for-drivers/)
>
> **Derivation B — revenue ÷ per-ride fee.** Revenue **US$19.8M** for the 12 months to October 2024 (Fortune, from a 24 Dec 2025 interview with Kay Woo) ÷ a flat per-ride driver software fee of **US$0.78–0.92** (same source) ÷ 12 = **1.79M–2.11M rides/month**. ⚠️ **This is an upper bound**, because the $19.8M includes non-ride revenue lines (anonymised driving-data sales, plus group Web3 revenue). ⚠️ **And it rests on an aggregator estimate** — Fortune hyperlinks the $19.8M to `getlatka.com`, so Derivation B is weaker than Derivation A. **Lead with Derivation A (the 1.52M floor), which rests on the company's own cumulative-rides claim.** [Source](https://fortune.com/2025/12/25/the-worlds-leading-blockchain-based-taxi-app-is-setting-its-sights-on-new-york-city/)
>
> **Both derivations are built on sourced inputs, and they agree**: ~1.5M (floor) to ~2.1M (ceiling) rides per month. The ≥100,000 band is cleared by a factor of 15 at minimum. **The under-40,000 auto-reject does not fire.**
>
> **Independent corroboration of the fee quantum:** Singapore drivers report a **S$1.09** deduction per system cancellation penalty (MS News, 2 Jan 2026) — S$1.09 ≈ US$0.80, sitting squarely inside Fortune's US$0.78–0.92 band and confirming the per-ride fee is real and small. [Source](https://mustsharenews.com/tada-my-destination/)

> #### ⭐ THE BILLING UNIT — three different units, and they are not interchangeable
>
> This account has an unusual revenue model and the number above means nothing without this.
>
> | Unit | Who pays | Who collects | Is it a Yuno-orchestratable pay-in? |
> |---|---|---|---|
> | **1. The fare** (the large number) | Rider | **TADA, acting as the drivers' "payment collection agent"** — stated verbatim in the HK terms | ✅ **YES — this is the pay-in.** ~1.5–2.1M/month, minus the cash share |
> | **2. The Platform Fee** (booking/app fee) | Rider | TADA, for itself | ✅ Yes — collected in the **same authorisation** as the fare, not separately |
> | **3. The driver software fee** (~US$0.78–0.92; $1 flat in NYC) | **Driver** | TADA | ⚠️ This is **TADA's revenue**, deducted from driver earnings — a payout-side netting, not a card pay-in |
>
> **Verbatim, from TADA's own production bundle:** *"TADA takes zero commission. **Except for platform and transaction fees for debit/credit cards**, the full amount of the fare is for a driver."* — i.e. **card processing cost is explicitly carved out of the zero-commission promise and passed through.** Acceptance cost is not an abstraction for this merchant; it is a line item they have told drivers about in writing.
>
> **Verbatim, Hong Kong rider terms §3.1:** *"The use of Service involves charges to the Rider which includes fees for the services provided by the Driver ("Fares") and a booking fee / app fee from TADA ("Platform Fees")... TADA facilitates the Rider's payment of the applicable Fares (unless paid in cash) on the Driver's behalf **as a payment collection agent**."*
>
> **Verbatim, NYC (Kay Woo to NY1, 21 Aug 2026):** *"We charge a $1 fee for the drivers. That's it."*
>
> ### 🚩 THE ONE NUMBER NOBODY HAS: the cash share
> **`payment_cash` is the second key in TADA's own method catalogue**, and cash is a first-class option in every market's rider terms (*"You may choose to pay for the transportation service by cash or credit card and/or debit card"*). **A cash ride generates no payment transaction at all.** Cash remains prevalent in Cambodia and Vietnam. **No source — company, press or third party — gives the cash-vs-digital split.**
>
> **This does not change the tier.** Even at a 20% digital share, ~300,000–420,000 orchestratable pay-ins/month still clears the ≥100,000 band. But **it is the first question on the discovery call**, and the business case cannot be sized without it. It is #1 in Manual Research Recommendations.

### Source Notes

- ✅ **Stripe is the confirmed PSP, and the case study is confirmed to be the right TADA.** `https://stripe.com/customers/tada` names Kay Woo, MVLLABS, the Singapore 2018 launch, *"TADA—which means 'let's ride' in Korean"*, Kenneth Tay as Head of Product, and the SG→KH/VN→TH→HK expansion sequence. No ambiguity with TaDa Delivery.
- ✅ **The 18-key payment-method catalogue is first-party and appears in two independent production artefacts** — `https://tada.global/assets/index-BbiHo7SX.js` (839,211 bytes) and the rider live-trip app bundle at `https://go.tada.global/assets/index-CvZmpBc9.js`. The same key set appears in both, in all nine locales. This is the merchant's own enum, not a marketing list.
- ✅ **Geofence bounding boxes were read from production code**, which is stronger than any press claim about markets: SG (1.130–1.478 N, 103.567–104.125 E), VN (9.776–21.385 N), **KH (11.226–11.859 N, 104.481–105.096 E — a tight Phnom Penh-area box, NOT all of Cambodia)**, HK, **CO (37.037–40.982 N, −109.023 to −102.074 — the exact Colorado state box)**, **NY (40.489–40.921 N, −74.272 to −73.740 — the five boroughs)**. [Source](https://policy.tada.global/assets/index-D4hJ-wRu.js)
- ✅ **`ET` — Ethiopia — is a real configured region with a real geofence** (5.754–12.588 N, 35.791–41.889 E, which is Ethiopia's bounding box), its own `et` language and a `wallet_terms_et_ET` fallback path. **Out of APAC territory**, so not pursued, but recorded because it means the group footprint is wider than anyone's notes say.
- ✅ **`quiks_*` legal documents exist in English and Indonesian (`in`)** — `quiks_privacy`, `quiks_driver_terms`, `quiks_delivery_terms` — and `ID` is in the region enum. **This is the only Indonesia evidence in the account, and it is for a different product ("Quiks", delivery), not TADA ride-hailing.** Indonesia scores **zero** city/market strings in the TADA bundle. Do not treat Indonesia as a TADA market.
- ✅ **`easi6_*` documents (en/ko/zh-CN/zh-TW) and `mvltaxi_driver_terms` (ko only)** confirm the group's Korean origin and an earlier Korea/Greater-China cross-border business. `KR` survives in the region enum with **no city map entry and no geofence** — i.e. **Korea is legacy, not live.**
- ✅ **Document staleness is itself a finding.** Rider terms/privacy last-modified dates: **SG 31/12/2025** (recent, includes the on-chain loyalty addendum) · **HK 04/07/2024** · **Cambodia 20/10/2020** · SG privacy **20/10/2020** · MVL platform terms **28/05/2019** · Throo privacy **01/06/2026**. **The market most likely to be TADA's largest is governed by rider terms last touched in October 2020**, which contemplate only cash and cards — while the app offers four Cambodian wallet rails.
- ⚠️ **The SG/KH/TH rider terms contemplate ONLY cash and card.** Verbatim: *"You may choose to pay for the transportation service by cash or credit card and/or debit card ('Card')."* Only the **HK** terms add *"and/or any other available payment method designated in your Account."* Yet the app catalogue carries eight wallet/QR rails. **Two readings are possible and I cannot distinguish them from outside:** (a) the terms are simply stale, or (b) some wallet rails are driver-side/QR-at-the-car collections rather than in-app rider charges. **Ask, do not assert.**
- ⚠️ **Divergence from the coordinator's independent scan, recorded for the audit.** The coordinator's notes list the bundle locales as `en, km, ko, ms, th, vi, zh-CN, zh-TW` and count 17 payment keys. My own extraction of the explicit locale enum — `he={EN:"en",EN_US:"en-US",KO:"ko",KM:"km",VI:"vi",TH:"th",ZH_CN:"zh-CN",ZH_TW:"zh-TW",JP:"jp"}` — finds **nine locales including `jp` and NO `ms`**, and **18 distinct `payment_*` keys** (the extra being `payment_method`, the section label rather than a method). Neither discrepancy is load-bearing; both sets agree there is **no Indonesian (`id`) locale** and **no Malay market**. Flagged so the record is honest rather than smoothed over.
- ⚠️ **`mvlchain.io` was fetched (HTTP 200, 1.16 MB) but not mined.** It is the token/ecosystem site, not a payment surface, and was deprioritised against first-party legal and app artefacts. A gap, stated.
- 🔒 **A live credential pair is embedded in the public production bundle.** HTTP Basic client credentials for the TADA driver app API and for the MVL homepage FAQ client are hard-coded and base64-encoded in `index-BbiHo7SX.js`. **[live credentials present — values deliberately not recorded.]** No authenticated request was made and no state-changing request was attempted. This is **not** a payment credential and proves no payment vendor; it is recorded only because it is a real security exposure Prateek may wish to mention as a goodwill gesture, and because the next analyst should not be tempted to use it.
- ❌ **No registry filing obtained.** ACRA/BizFile, Thai DBD, HK Companies Registry and NY DOS were not reachable. **No evidence of any stock-exchange listing or filing obligation for MVL or TADA was found** — the Korean-listing hypothesis in the brief is **unconfirmed**; searches in Korean returned funding coverage only, no KIND/DART filing. If a listing existed it would be the best revenue source; none was found.
- ❌ **BusinessWire, ababank.com and axios.com all returned HTTP 403.** Nothing load-bearing rests on them.

#### 🪙 MVL token — kept strictly separate from revenue and funding (the Sogni lesson)

| Line | Figure | What it is NOT |
|---|---|---|
| **TADA revenue** | **US$19.8M** (12 months to Oct 2024), up from **US$15.7M** (2023) — [Fortune](https://fortune.com/2025/12/25/the-worlds-leading-blockchain-based-taxi-app-is-setting-its-sights-on-new-york-city/) | The only revenue figure found. ⚠️ **Provenance downgrade (Prateek's audit, 2026-10-12):** Fortune **hyperlinks this figure to `getlatka.com`**, a third-party revenue aggregator — it is **not** a company disclosure and not a figure Kay Woo stated in the interview. Treat as `[ESTIMATE, not confirmed]`, not as reported revenue. The 78–92¢ driver fee, the 11.1% 2022 SG share (Measurable AI) and the Denver trial **are** in Fortune's own prose and I verified all three verbatim |
| **Equity funding** | Series A **US$5M** (SV Investment-led); total Series A later reported *"just under US$10M"*; a Shinhan Bank-led bridge taking cumulative investment to ~KRW 10bn; a **US$15M Series B** for the ONiON EV programme (undated in result) | Equity. Separate from the token |
| **MVL token market cap** | **~US$21–25M** mid-2026 (CoinLore ~US$23M as of 27 Jul 2026; CryptoSlate US$24.8M as of 12 Jul 2026). 30bn total supply, ~27.2–27.8bn circulating, listed on ~4 exchanges | 🚫 **NOT revenue. NOT funding. NOT GMV. NOT a valuation of TADA.** It must not appear in the financials row. Note that it is *smaller* than one year of TADA revenue, so it cannot flatter anything even if someone tried |
| **ICO / token sale proceeds** | ❌ **Not found.** No figure obtained for the original MVL token sale | Must not be conflated with the equity rounds above |

✅ **TADA's own terms draw the same line, which is useful cover on a call.** SG rider terms §3.2: *"TADA Points are loyalty points only. **They are not fiat currency, tokens, securities, or cryptocurrency.** TADA Points cannot be exchanged or redeemed for cash, converted into any cryptocurrency, or traded on any external market."* The in-app loyalty unit and the MVL coin are deliberately different things.

### Success Case Alternatives
- ⭐ **inDrive** — *"~90% approval, 10 new countries in under 8 months"* — [y.uno/en/success-stories/indrive](https://y.uno/en/success-stories/indrive). **The best-matched Tier 1 case in the library for this account, and the one to lead with.** Multi-country ride-hailing, identical driver-economics positioning, and the two published numbers map exactly onto TADA's two live problems: an approval rate they already measure and quote (Stripe's 98%), and market-launch velocity (five APAC markets plus three US states, with NJ and CT already stubbed in the config). ⚠️ **Do not APAC-ify it** — say inDrive, say what it did, and never imply the results came from Asia.
- **Uber** — publicly named on Yuno's site-wide and travel/mobility customer lists. **No published metrics — nameable only, never with a number.** Uniquely pointed here: Uber is Throo's explicit head-to-head rival in New York and the "first wave" incumbent Kay Woo says he is disrupting. Use as a one-line credibility signal, not as proof.
- **Livelo** — the decline-cascade case (*"+5% approval rate · 50% of failed transactions recovered"*). **Hold this one back until the multi-acquirer question is answered.** Its mechanism presumes the prospect already runs 2+ acquirers with no failover, and we have only sourced one acquirer. Deploy it at the point TADA confirms separate local integrations per market.
- ❌ **Do NOT use Viva Aerobus** — that is a NOVA voice-callback case, not routing. Wrong mechanism for this account.
- ❌ **Do NOT use "Tada" from Yuno's customer wall.** See the Phase 0 note.

---

## Executive Summary

TADA is a Singapore-headquartered, zero-commission ride-hailing platform in the MVL group, live in **Singapore, Cambodia, Vietnam, Thailand and Hong Kong** and, since June 2026, in **New York City and Colorado** under the separate Throo and COOP brands. It claims **150M+ cumulative rides and nearly US$2bn GMV**, and reported **US$19.8M revenue** for the year to October 2024 — earned not from a commission but from a **flat ~US$0.80 per-ride software fee on drivers** plus a **rider-paid booking fee**, with card processing cost explicitly carved out of the zero-commission promise and passed through. The key payment finding is that **Stripe is the sole named PSP and every card is processed in Singapore dollars from a Singapore account, while riders use one stored card across all five APAC markets** — the definition of a cross-border acquiring footprint — and that **the national interoperable rail in what is probably their largest market is absent**: `bakong` and `khqr` return zero occurrences in TADA's own 18-key payment-method catalogue, even though four separate Cambodian bank and wallet apps (ABA Pay, Wing Pay, Pi Pay, Chip Mong Pay) are wired in one by one. **Motion: greenfield, qualified** — no orchestrator exists anywhere in their estate, but they already buy acceptance optimisation from Stripe, so the opening is local acquiring and rail coverage in the four markets Stripe does not acquire in, not the case for orchestration itself.

---

## Section 1: Website Traffic Analysis by Country

**Data source:** ❌ **NONE. No traffic data was supplied and none was obtained.**

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| — | — | **No data** | **No data** | — | — |

**This section cannot be completed.** `accounts/traffic/` holds no file for this company and Prateek pasted none. No country split is given, because inventing one is not an option. The `site:similarweb.com` fallback was deliberately not spent — see below.

> ⚠️ **And it would not have helped.** TADA is app-first ride-hailing with **no web checkout at all**: `tada.global` is a client-rendered Vite marketing SPA (6,288 bytes of shell, one `<div id="root">`, zero card fields, zero payment routes), and `go.tada.global` is a live-trip share page. Fares are paid inside native apps. A SimilarWeb visit figure would measure brochure reads and app-store hand-offs and would correlate with transaction volume only by accident. **Spending the fallback search would have produced an estimate-grade number that was also the wrong metric.**

**Consequences, restated so they are not lost:** no APM gap analysis can be traffic-weighted; the ICP row *"High traffic outside home"* scores **0 ⬜**; the Quick Look country table is labelled `[ESTIMATE, not confirmed]` throughout; Overall Research Confidence is downgraded.

### Section 1-ALT: App and ride metrics — the right proxies for this account

| Metric | Value | Source |
|---|---|---|
| **Cumulative rides, worldwide** | **"more than 150 million"** (company claim) | [PRNewswire, 1 Jul 2026](https://aijourn.com/throo-launches-in-new-york-city-with-lower-fares-for-riders-and-zero-commission-for-drivers/) |
| **Cumulative GMV** | **"nearly $2 billion"** (company claim) | same |
| **Implied average ride value** | **~US$13.3** — $2,000M ÷ 150M. `[DERIVED from two company claims in one release]` | derived |
| Google Play installs — rider app `io.mvlchain.tada` | **1M+** band; **35,816 reviews**; developer **TADA MOBILITY (SINGAPORE) PTE. LTD.**; last updated **6 Oct 2026** (six days before this report — actively shipped) | [Play](https://play.google.com/store/apps/details?id=io.mvlchain.tada) |
| Google Play installs — driver app `io.mvlchain.tada.driver` | **1M+** band | [Play](https://play.google.com/store/apps/details?id=io.mvlchain.tada.driver) |
| Apple App Store ratings — rider, SG storefront | **56,455 ratings**; seller **MVL Foundation** | [App Store](https://apps.apple.com/sg/app/tada-ride-hailing/id1412329684) |
| Apple App Store ratings — driver | **~8k** | same developer page |
| Singapore market share | **11.1% in 2022** (Measurable AI, via Fortune) — the only market-share figure found; four years old | [Fortune](https://fortune.com/2025/12/25/the-worlds-leading-blockchain-based-taxi-app-is-setting-its-sights-on-new-york-city/) |
| Riders / drivers | **3M+ riders, 300,000 drivers** per a Dealroom profile and a LinkedIn company page `[UNVERIFIED — profile data, not a primary source]`. An early 2019 e27 report gave 30,000 drivers / 230,000 users across SG+VN+KH | [e27](https://e27.co/blockchain-powered-ride-hailing-tada-officially-operates-in-cambodia-20190509/) |
| Throo NYC, first month | **2,047 drivers made 2,547 trips in June 2026** — **NYC TLC data**, the only regulator-sourced volume figure in this account. Uber and Lyft combined for **over 20 million** trips in the same month | [NY1](https://ny1.com/nyc/all-boroughs/news/2026/08/21/new-ride-hail-app-throo-looks-to-take-on-uber--lyft-in-new-york-city) |
| Throo driver sign-ups | **50,000+** pre-launch (company); **53,000+** by Aug 2026 (CEO) | PRNewswire; NY1 |

> 🚩 **Do not let the Throo numbers distort the account.** 2,547 trips in a month is a rounding error against TADA's APAC base. Throo matters as a **payment-build and expansion signal**, not as volume. Conversely, 53,000 recruited drivers against 2,547 trips says the supply side is far ahead of the demand side in NYC — a real commercial fragility worth knowing before a call, and a reason their APAC P&L is what funds the US push.

---

## Section 2: Legal Entities & Local Presence

**Headquarters:** Singapore. Founded **2018** by **Kay Woo** (Founder/CEO) and **Jay Han**, after an earlier Hong Kong–Shenzhen cross-border mobility business. Group parent **MVL Foundation Pte. Ltd.**; CB Insights describes MVL as a wholly-owned subsidiary of **easi6** `[UNVERIFIED — search summary only, page not fetched; the same profile marks easi6 as dead]`.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Singapore | **MVL Foundation Pte. Ltd.** (group parent; Apple App Store seller of record) | Not found | [mvl_terms_en_SG.md](https://policy.tada.global/policies/mvl_terms_en_SG.md) · [App Store](https://apps.apple.com/sg/app/tada-ride-hailing/id1412329684) |
| Singapore | **TADA Mobility (Singapore) Pte. Ltd.** — 63 Ubi Road 1 #01-48, Oxley Bizhub, Singapore 408728. Google Play developer of record | Not found | [tada_privacy_en_SG.md](https://policy.tada.global/policies/tada_privacy_en_SG.md) · [tada_terms_en_SG.md](https://policy.tada.global/policies/tada_terms_en_SG.md) |
| Singapore | **TADA Technologies Pte. Ltd** — the contracting entity in the **Vietnamese** rider terms | Not found | [tada_terms_vn_VN.md](https://policy.tada.global/policies/tada_terms_vn_VN.md) |
| Thailand | **TADA MOBILITY (THAILAND) CO., LTD.** — 2322 Pracha Songkhro Road, Din Daeng, Bangkok; `enquiries_th@tada.global` | Not found | [tada_privacy_en_TH.md](https://policy.tada.global/policies/tada_privacy_en_TH.md) |
| United States (NY) | **Zero Commission LLC**, a New York limited liability company — operates Throo; `Support@ridethroo.com` | Not found | [throo_terms_en_NY.md](https://policy.tada.global/policies/throo_terms_en_NY.md) · [throo_privacy_en_NY.md](https://policy.tada.global/policies/throo_privacy_en_NY.md) |
| United States | **TADA Mobility (USA) LLC** — appears in job postings per one report `[UNVERIFIED — search summary only, page not fetched]`. Note the first-party Throo terms name Zero Commission LLC, not this | Not found | search summary |
| Cambodia | ❌ **None found** | — | — |
| Vietnam | ❌ **None found** | — | — |
| Hong Kong | ❌ **None found** (company states an HK office) | — | — |

**Corroborating presence evidence (first-party):** per-market support mailboxes `support@tada.global`, `supportkh@tada.global` (KH), `support_th@tada.global` (TH), `support_hk@tada.global` (HK), `hotro@tada.global` (VN — *hỗ trợ*); embedded local emergency links for Thailand (`royalthaipolice.go.th`, `niems.go.th`), Singapore (`police.gov.sg`, `scdf.gov.sg`) and Hong Kong (`police.gov.hk`); production geofences for SG, VN, KH, HK (and CO, NY, ET); `/thaid/callback` and `/thaid/authenticate` routes indicating a **ThaID** national-digital-ID integration for Thai onboarding.

**Cross-Border Gap Analysis**

| Country | In top markets? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| Singapore | ✅ Yes | ✅ Yes (two SG entities) | No — MAS PSA licensing applies only where the merchant touches funds; **verify against the current MAS Payment Services Act before citing** | **Low.** This is the acquiring home base — Stripe processes in SGD here |
| Cambodia | ✅ Yes (`[EST]` largest) | ❌ **No** | ⚠️ Not established in this research. **Do not assert a Cambodian regulatory gate — it was not sourced.** What *is* sourced is that the dominant rail is a domestic NBC-operated system | 🚩 **HIGH.** No local entity, and the only confirmed acquirer processes in SGD |
| Vietnam | ✅ Yes | ❌ **No** — riders contract to a **Singapore** entity | ⚠️ Vietnam gates intermediary payment services behind **State Bank of Vietnam** licensing; `apac-payments.md` flags local-entity expectations. **Verify current SBV rules and cite a live source before using this in an email.** | 🚩🔒 **HIGH + regulatory.** Vietnamese riders on a Singapore contract and a Singapore acquirer |
| Thailand | ✅ Yes | ✅ Yes (TADA Mobility (Thailand) Co., Ltd.) | No evidence of a gate found | **Medium.** Local entity exists, but no evidence card processing was localised to it — Stripe's case study describes SGD processing |
| Hong Kong | ✅ Yes | ❌ **No** | No evidence of a gate found | 🚩 **HIGH.** HK terms and privacy both route data *"within or outside of **Singapore**"*, implying HK is run from the SG entity |

> **Warning: potential cross-border operation in Cambodia, Vietnam and Hong Kong. No local entity found in any of the three.** Stripe's own case study states that riders *"can use the card they store in their account profile **across all the countries that TADA operates in**"* and that developers configured Payments so riders *"can pay for services with credit and debit cards **processed in Singapore dollars (SGD)**"*. **Taken together: a Cambodian, Vietnamese, Thai or Hong Kong cardholder's transaction is being authorised against a Singapore acquiring account in a foreign currency.** That carries higher scheme costs, an FX leg on every non-SGD rider, and — per `apac-payments.md` §3 — materially higher issuer decline rates than local acquiring, which is the stronger argument in this territory than fee. Argue the corridor, not the region: *"cards issued in Cambodia processed against a Singapore entity"* is the claim that can be supported. [Source](https://stripe.com/customers/tada)

> **Regulatory gate: Vietnam.** `apac-payments.md` lists Vietnam among the markets where domestic acquiring is effectively gated behind local entity and/or local licensing, and flags State Bank of Vietnam licensing for intermediary payment services as the item to verify per account. **That verification was not completed in this run** — no live SBV source was obtained. **Do not put a Vietnamese licensing claim in an email until it is sourced.** What can be said without a regulatory source is the plain fact: the Vietnamese-language rider terms name a Singapore company.

> **MANUAL:** T&Cs and privacy policies were obtained in full for five jurisdictions — they are at `https://policy.tada.global/policies/{doc}_{lang}_{REGION}.md` (e.g. `tada_terms_en_SG.md`, `tada_terms_en_KH.md`, `wallet_terms_en_KH.md`). The file-naming scheme and the full document catalogue were recovered from `https://policy.tada.global/assets/index-D4hJ-wRu.js`. Registry lookups (ACRA UEN, Thai DBD, HK CR, NY DOS) remain outstanding.

---

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| **Southeast Asia (SG, KH, VN, TH) + HK** | ⭐ **Stripe** — Payments, **Radar**, **Adaptive Acceptance**. Cards **processed in SGD**. Pre-authorisation holds. Network-token-vs-PAN acceptance testing. Card account updater. Integrated in two weeks. Segment tagged **Enterprise** | `[Provider Case Study]` | [stripe.com/customers/tada](https://stripe.com/customers/tada) |
| Same | Stripe — corroboration, dated **7 Nov 2024**; quotes Sarita Singh (Stripe Regional Head & MD, SEA/India/Greater China) | `[Press Release]` | [techcoffeehouse](https://techcoffeehouse.com/2024/11/07/stripe-powers-tadas-southeast-asia-expansion-amid-intense-ride-hailing-competition/) |
| **United States (Throo)** | **Stripe** — *"Payment processing may be provided by third-party processors (**for example, Stripe**)"*. Hedged; indicative only | `[Terms/Privacy Policy]` | [throo_terms_en_NY.md](https://policy.tada.global/policies/throo_terms_en_NY.md) |
| Cambodia | **ABA Pay · Wing Pay · Pi Pay · Chip Mong Pay · MOMO Pay** — confirmed as **methods**; **acquirer/aggregator NOT FOUND** | `[Source Code]` for the method; **no evidence for the processor** | [index-BbiHo7SX.js](https://tada.global/assets/index-BbiHo7SX.js) |
| Vietnam | **MoMo** (`payment_momo_aof`) — method confirmed; **acquirer NOT FOUND** | `[Source Code]` | same |
| ⚠️ Unresolved | **MOMO Pay** (`payment_momopay_p`) is a **second, distinct** MoMo-branded key. **Its market is NOT established** — see the catalogue caveat in Section 4. Do not assign it to Cambodia or Vietnam in outreach | — | — |
| Singapore | **NETS QR** (two keys: `payment_nets_qr`, `payment_pao`) · **OCBC Digital** (`payment_ocbc_pao`) — methods confirmed; **acquirer NOT FOUND** | `[Source Code]` | same |
| Cross-border inbound | **Alipay+** (`payment_alipay_plus`) — method confirmed; **acquirer NOT FOUND** | `[Source Code]` | same |
| Global | **Apple Pay · Google Pay** — methods confirmed. Stripe's Nov-2024 case study listed Apple Pay as a *planned* addition; it is now in the catalogue, so it shipped | `[Source Code]` + `[Provider Case Study]` | same |
| All | **TADA Wallet** (`payment_tadapay`) — own stored value, top-up in-app, non-refundable, non-withdrawable, effective 22 Jan 2025 | `[Terms/Privacy Policy]` | [wallet_terms_en_KH.md](https://policy.tada.global/policies/wallet_terms_en_KH.md) |
| All | **Corporate** (`payment_corporate`) — a B2B/invoiced billing track, localised in every language (Khmer *គណនីអាជីវកម្ម*, Thai *องค์กร*, Vietnamese *Doanh nghiệp*). **An entirely separate commercial product nobody had on this account** | `[Source Code]` | same |
| All | **Cash** (`payment_cash`) — first-class, every market, named in every version of the rider terms | `[Source Code]` + `[Terms/Privacy Policy]` | same |
| — | ❌ **Not found, and specifically checked:** Adyen, Checkout.com, Worldpay, Braintree, PayPal, 2C2P, Xendit, Midtrans, Doku, iPay88, Omise, Razorpay, PayU, Cashfree, GMO, Veritrans, KOMOJU, NICEPAY, Toss Payments, eWAY, Windcave, Tyro, HitPay, Red Dot, AsiaPay | — | — |

> ⚠️ **Confirmed false positives in this account — checked in context, every one.** `omise` → 66 hits in the TADA bundle and 122 across the rider-app bundles, **all `Promise`/`stripePromise`**. `wing` → 30 hits, all *"following"*, *"showing"*, *"Wind down"*. `aba` → 22 hits, all base64 image data and a mobile-detect UA regex. `fps` → 1 hit, *"frame rates higher than 125 fps"*. `gmo` → 1 hit, an SVG attribute map. `dana`, `maya`, `nets`, `card_number` → `card_number` is an **identity** card number in the KYC flow, not a PAN.
>
> 🚩 **And the trap runs both ways, which is the finding worth keeping.** `wing` and `aba` were **pure noise in raw grep** yet **genuinely present** as `payment_wingpay` and `payment_aba_pay` in the method enum. **A false positive on a plain token does not clear the vendor.** The only reliable route here was extracting the structured `payment_*` key/label pairs, not grepping brand names.

### 3B. Payment Orchestrator

**Classification: None detected — direct PSP integration only (greenfield).**

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with PSP(s), which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

**Evidence for the negative** `[Source Code]` + `[Provider Case Study]`:
- Zero occurrences of **Juspay, Spreedly, Primer, Gr4vy, CellPoint, Payrails, APEXX, Yuno** across: `tada.global/assets/index-BbiHo7SX.js` (839,211 bytes), 11 bundles of the `go.tada.global` rider live-trip app, `policy.tada.global/assets/index-D4hJ-wRu.js` (348,418 bytes), and 16 first-party legal documents across five jurisdictions.
- No orchestrator in any press coverage, in Stripe's own case study, or in TADA's payment-method catalogue.
- The TAL's `Payment Orchestrator` cell is empty; **independent verification agrees with "none"** — this is a checked negative, not an unchecked blank.

**⚠️ What the orchestration-shaped behaviour actually is — and why this is "qualified" greenfield, not naive greenfield.** TADA already buys routing-adjacent optimisation **inside Stripe**: *"TADA adopted **Stripe Adaptive Acceptance**, which uses machine learning to optimize authorization **requests, retries, and routing combinations**"*, plus automatic card-credential updates and network-token-vs-PAN testing. **Stripe's own published result: 98% authorisation rate, +2.8% from Adaptive Acceptance, 0% dispute rate with Radar.** That is single-PSP optimisation, not multi-acquirer orchestration — **but it means the "you have no optimisation" opening is factually wrong and would burn the thread.** The real gap is that every one of those levers stops at Stripe's own acquiring reach, and Stripe does not acquire domestically in Cambodia or Vietnam.

**The one genuine fallback mechanism in the stack, verbatim (HK rider terms §3.1):** *"If your primary account payment method is determined to be expired, invalid or otherwise not able to be charged, you agree that TADA may... use a **secondary payment method in your account**, if available."* **This is instrument-level fallback across the rider's own stored methods — not acquirer-level retry.** When the rider has only one instrument and the issuer declines a foreign-acquired authorisation, the documented fallback is *"settle the Fares in cash directly with the Driver"*. For a platform that earns a fee only on the digital leg, a decline that falls back to cash is revenue that leaves the platform entirely.

**Two limits on the negative, stated plainly:** these are **web** artefacts and the rider checkout is **native-app**, so absence here is not absence in the app binary; and `tada.global` serves **no CSP header at all**, so no `connect-src` asset map was available to enumerate payment hosts. The classification is safe because it rests on the Stripe case study and the first-party method catalogue, but the app binary was not decompiled and that remains the one way to close it.

> **MANUAL:** Walk the rider app checkout on a Cambodian and a Vietnamese SIM with a proxy; watch for non-Stripe payment hosts. That is the single test that would convert the "Multiple PSPs" ICP row from 0 to 3.

### 3C. Driver payouts — the other half of the stack

Ride-hailing moves money **out** as well as in, and TADA's model makes the outbound leg unusually central: the HK terms describe TADA as *"the Driver's **limited payment collection agent**"*, so the platform collects the fare and must then disburse it.

| Finding | Source |
|---|---|
| **Throo (US)** runs a **Driver Balance** with **Cashout on request, any time, no platform-imposed limit**; an automated/manual **Fraud Check** before crediting earnings, *"typically... less than 24 hours"*; earnings available *"within one (1) week"*. Cashouts are *"processed through **one or more third-party payment processors and payment rails**"* to *"bank account, debit card, or other payout method"* | [throo_terms_en_NY.md](https://policy.tada.global/policies/throo_terms_en_NY.md) |
| **Throo privacy policy** lists, among data held: *"For Drivers: **payout details** (e.g., bank account or other payout method info)"* and names *"Payment processing"* as a vendor category | [throo_privacy_en_NY.md](https://policy.tada.global/policies/throo_privacy_en_NY.md) |
| **APAC payout rails: NOT FOUND.** No provider, no mass-disbursement partner, no e-wallet top-out arrangement named in any APAC document or press item | — |
| **Competitive contrast (sourced):** Grab Cambodia's ABA Bank integration explicitly covers *"automatic payouts directly into their ABA accounts, allowing them to receive earnings swiftly and securely"*, alongside ABA PayWay for pay-in and KHQR top-up | [b2b-cambodia, 3 Sep 2025](https://b2b-cambodia.com/news/milestone-in-digital-integration-aba-and-grab-advance-cashless-ecosystem-in-cambodia) |

> 🚫 **Positioning discipline — read before writing any email.** **Yuno is a pay-in orchestration layer.** Nothing in `apac-payments.md` or `subscription-payments.md` states that Yuno performs payouts or mass disbursement. **Do not pitch driver payouts as something Yuno does.** Payouts are recorded here because (a) they are half of this merchant's money movement and will come up on the call, and (b) the pay-in side is where Yuno's argument lives and it is useful to show you know the difference. If asked directly, say payouts are outside what Yuno orchestrates.

---

## Section 4: Alternative & Local Payment Methods

> ⚠️ **CAVEAT ON PER-MARKET ATTRIBUTION — added by Prateek's audit, 2026-10-12.**
> The `payment_*` block in the bundle is a **single flat i18n object with no market grouping of any kind**. I read it directly: Singapore keys (`payment_pao`, `payment_ocbc_pao`), Cambodian keys (`payment_pipay_post`, `payment_cmcb`, `payment_wingpay`, `payment_aba_pay`) and both MoMo keys sit interleaved in one undifferentiated list. **The catalogue proves which methods EXIST. It does not prove which market each one serves.**
> Every per-market method assignment in this report — including the country table in Section 1 — is therefore an **[INFERENCE, not confirmed]** drawn from each brand's known market of origin. That inference is safe for ABA Pay, Wing Pay, Pi Pay and Chip Mong Pay (unambiguously Cambodian institutions) and for NETS QR / OCBC Digital (unambiguously Singaporean). **It is NOT safe for MOMO Pay**, which could be Cambodian or a second Vietnamese key.
> **Absences, by contrast, are robust**: a method absent from a single global catalogue is absent everywhere, regardless of grouping. So the Bakong/KHQR and PromptPay zero-occurrence findings do not depend on this caveat.

**Source for every CONFIRMED row:** TADA's own production payment-method catalogue — the `payment_*` i18n key/label pairs extracted from [`tada.global/assets/index-BbiHo7SX.js`](https://tada.global/assets/index-BbiHo7SX.js), independently reproduced in the rider live-trip app bundle [`go.tada.global/assets/index-CvZmpBc9.js`](https://go.tada.global/assets/index-CvZmpBc9.js). This is the merchant's own enumeration across all nine locales, which is why absence from it is meaningful rather than merely unobserved.

**The complete catalogue — 18 keys, verbatim:** `payment_method` (label) · `payment_cash` Cash · `payment_credit_card` Credit Card · `payment_apple_pay` Apple Pay · `payment_google_pay` Google Pay · `payment_tadapay` TADA Wallet · `payment_corporate` Corporate · `payment_delivery` DELIVERY · `payment_aba_pay` ABA Pay · `payment_wingpay` Wing Pay · `payment_pipay_post` Pi Pay · `payment_cmcb` Chip Mong Pay · `payment_momopay_p` MOMO Pay · `payment_momo_aof` MoMo · `payment_nets_qr` NETS QR · `payment_pao` NETS QR · `payment_ocbc_pao` OCBC Digital · `payment_alipay_plus` Alipay+.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| All | Cash | Cash/voucher | **Active in checkout** | catalogue + every rider terms version |
| All | Credit / debit card (Visa, Mastercard) | Cards | **Active in checkout** — Stripe, processed in SGD | catalogue + [Stripe](https://stripe.com/customers/tada) |
| All | Apple Pay | Digital wallet | **Active in checkout** | catalogue |
| All | Google Pay | Digital wallet | **Active in checkout** | catalogue |
| All | TADA Wallet | Stored value / prepaid | **Active in checkout** (KH wallet terms effective 22 Jan 2025) | [wallet_terms_en_KH.md](https://policy.tada.global/policies/wallet_terms_en_KH.md) |
| All | Corporate account | Invoiced / B2B | **Active in checkout**, localised in all languages | catalogue |
| Cross-border | Alipay+ | Digital wallet (aggregator) | **Active in checkout** | catalogue |
| **Cambodia** | **ABA Pay** | Digital wallet / bank app | **Active in checkout** | catalogue |
| **Cambodia** | **Wing Pay** | Digital wallet | **Active in checkout** | catalogue |
| **Cambodia** | **Pi Pay** | Digital wallet | **Active in checkout** | catalogue |
| **Cambodia** | **Chip Mong Pay** | Digital wallet / bank app | **Active in checkout** | catalogue |
| ⚠️ **Market unresolved** | **MOMO Pay** (`momopay_p`) | Digital wallet | **Active in checkout, but the market it serves is NOT evidenced** — distinct from Vietnam's `momo_aof`. Not counted in the Cambodian total | catalogue |
| **Cambodia** | 🚩 **Bakong** | Bank transfer / A2A (NBC's own rail) | ❌ **NOT FOUND — zero occurrences** | catalogue (checked, sanity-checked) |
| **Cambodia** | 🚩 **KHQR** | Interoperable QR standard | ❌ **NOT FOUND — zero occurrences** | catalogue (checked, sanity-checked) |
| **Cambodia** | USD/KHR dual-currency handling | — | ❌ **NOT FOUND.** No ISO currency table of any kind exists in the bundle (no `USD`, `KHR`, `SGD`, `VND`, `THB`, `HKD` literals) | catalogue |
| **Vietnam** | **MoMo** (`momo_aof`) | Digital wallet | **Active in checkout** | catalogue |
| **Vietnam** | 🚩 ZaloPay · VNPay / VietQR · NAPAS | Wallet / QR / domestic cards | ❌ **NOT FOUND — zero occurrences each** | catalogue |
| **Singapore** | **NETS QR** · **OCBC Digital** | A2A / bank app | **Active in checkout** | catalogue |
| **Singapore** | 🚩 **PayNow** · GrabPay | A2A / wallet | ❌ **NOT FOUND — zero occurrences** | catalogue |
| **Thailand** | 🚩 **PromptPay** | A2A / QR | ❌ **NOT FOUND — zero occurrences.** Named by Stripe in Nov 2024 as a planned addition; **still absent 23 months later** | catalogue + [Stripe](https://stripe.com/customers/tada) |
| **Thailand** | 🚩 TrueMoney | Digital wallet | ❌ **NOT FOUND.** ⚠️ TrueMoney participates in Alipay+, which **is** present — so Thai TrueMoney users may be reachable indirectly. Do not claim they are locked out | catalogue |
| **Hong Kong** | 🚩 **FPS** · **Octopus** · AlipayHK (domestic) | A2A / stored value / wallet | ❌ **NOT FOUND.** Alipay+ is present, but that is the cross-border aggregator, not domestic AlipayHK | catalogue |
| Indonesia | QRIS · GoPay · OVO · DANA · ShopeePay | — | **N/A — Indonesia is not a TADA market.** Zero Indonesia city/market strings. The only ID evidence is `quiks_*` legal docs for a different product | [policy bundle](https://policy.tada.global/assets/index-D4hJ-wRu.js) |
| Japan / Korea / Taiwan / Malaysia | — | — | **N/A — not markets.** `KR` persists in the region enum with no city map and no geofence (legacy); `jp` and `zh-TW` are locales without markets | catalogue + policy bundle |
| Instalments / EMI · carrier billing · BNPL · recurring mandates (UPI Autopay, PayTo) | — | — | ❌ **NOT FOUND, and correctly absent.** Ride fares are low-ticket single-shot payments; instalments and mandates do not apply. **`subscription-payments.md` was not loaded — there is no recurring model in this account.** The TADA Wallet is prepaid top-up, not a subscription | catalogue |

### 🚩 THE CAMBODIA FINDING — stated precisely, because the precise version is the stronger one

> **What is true:** TADA has wired **four separate Cambodian bank and wallet apps** into its checkout one at a time — **ABA Pay, Wing Pay, Pi Pay and Chip Mong Pay**. (A fifth key, **MOMO Pay**, is in the catalogue but **its market is not evidenced** — see the attribution caveat in Section 4. **Use four, not five, in any outreach**: four is the defensible floor and every name in it is unambiguously Cambodian.) **Bakong and KHQR, the National Bank of Cambodia's own interoperable rails, return zero occurrences in the catalogue.**
>
> **What is NOT true, and must not be said:** that Cambodian riders cannot reach TADA with their preferred rail, or that TADA is card-only in its largest market. **It is not card-only — far from it.** And ABA Bank, Wing Bank and Chip Mong Commercial Bank are all **Bakong participants**, with KHQR *"fully enabled in the ABA PAY payment system"* `[UNVERIFIED — ababank.com returned 403; this rests on a search summary of ABA's own pages]`. So much of the KHQR user base is already reachable through the apps TADA integrated individually.
>
> **The accurate and genuinely sharper observation is integration sprawl.** KHQR exists precisely so that a merchant does not have to do this: *"It allows users to make payments by scanning a single QR code, regardless of which [bank app they use]"*, with **3.3 million+ merchants accepting it** and **601.3 million transactions worth US$75.8 billion in 2023** — against a Cambodian digital-payment total equal to **2.4× national GDP** and **19.7 million registered e-wallet accounts**. Bakong itself had processed **175.3 million transactions worth US$54.8 billion** by H1 2024. [Source: Kapron Asia](https://kapronasia.com/insight/blogs/payments-research/asia-payments-research/instant-payments-are-fueling-cambodias-e-commerce-boom)
>
> **So the question to put to them is not "why don't you accept Cambodian wallets" — they do. It is "you are maintaining four Cambodian wallet integrations plus cards where one national rail would cover them, and you are doing the same thing again in every new market."** That is an engineering-cost and time-to-market argument, which is exactly the argument orchestration wins. And it is corroborated by their own behaviour: Stripe's case study has them saying *"Regional payment integration processes usually take a lot of time"* — the pain is already named, in their own words, by their own Head of Product.
>
> ⚠️ **Verify before writing.** The KHQR-participation claim for ABA/Wing/Chip Mong needs a fetchable source — `ababank.com` 403'd. Get it from the NBC or a reachable ABA page before it goes in an email.

### 🚩 THE THAILAND FINDING — a two-year-old published intention, still unshipped

> Stripe's own case study, published **November 2024**, states: *"To facilitate future growth, TADA hopes to implement Stripe Elements... The no-code tools in Elements would enable TADA to expand its payment options to include digital wallets like **Apple Pay**, as well as a Thailand-based payment method called **PromptPay** that allows customers to make a payment by scanning a QR code with their bank app."*
>
> **As of the October 2026 production catalogue: Apple Pay shipped. PromptPay did not.** `promptpay` returns **zero occurrences**. Twenty-three months after a publicly stated intention, with a Thai legal entity in Bangkok, a ThaID identity integration live, and Thai-language terms in production — **the Thai national QR rail is still not in the checkout.** This is the cleanest single-sentence hook in the account, because the gap is measured against their own published roadmap rather than against an outsider's opinion of what they should support.

> **MANUAL:** Verify checkout APMs per country via VPN/SIM for Cambodia, Thailand and Hong Kong. The catalogue proves a key exists in the build; it does not prove the method renders for a given rider in a given city.

---

## Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| **Driver penalties from a dispatch bug** — `My Destination` auto-cancelled matched jobs without driver input; **S$1.09 deducted** per incident; cancellation rate dropped to 96%, requiring 50 further trips to restore. Company confirmed a system bug identified **13 Dec 2025**, rectified within three days, appeals open | Facebook (TADA Drivers Club) → MS News | **Moderate** (multiple drivers, one platform, one bounded incident) | Dec 2025 – Jan 2026 | [mustsharenews.com](https://mustsharenews.com/tada-my-destination/) |
| **Fare dispute** — driver allegedly demanded a further S$30 on a two-stop ride with a S$31 fixed fare, then cancelled mid-trip | Facebook → MS News | Isolated | Undated in result | [mustsharenews.com](https://mustsharenews.com/tada-driver-2-locations/) |
| **Declined transactions / failed payments** | Reddit, Trustpilot, X, app stores | ❌ **NONE FOUND** | — | — |
| **Duplicate charges · slow refunds · currency conversion · checkout errors · false fraud declines · wallet-specific failures** | all | ❌ **NONE FOUND** | — | — |

> *"No payment-processing complaints found on Reddit, X, Trustpilot or app store reviews."* The two issues located are a **dispatch/penalty** problem and a **fare** dispute. Neither is a payments failure, and **neither was counted toward the ICP matrix.** The "Payment issues" row scores **0**.

**Two things worth noting rather than stretching:**
1. **The absence is partly explained by the architecture.** Stripe publishes a **0% fraudulent dispute rate** and a **98% authorisation rate** for this merchant. A genuinely well-performing card stack produces few payment complaints — the quiet is consistent with the technical evidence, not suspicious.
2. **The residual 2% is the whole conversation.** At ~1.5–2.1M rides/month, a 2% decline rate on the digital share is tens of thousands of failed ride payments a month, and the documented fallback is *"settle the Fares in cash directly with the Driver"* — so a decline does not merely annoy a rider, it **removes TADA's fee from that ride entirely.** The 98% is Stripe's aggregate across a footprint whose cross-border legs are the ones most likely to sit in the missing 2%. **That is a question to ask, not a number to assert.**
3. ⚠️ **Coverage caveat.** App-store review text was not mined at scale (the Play and App Store pages were parsed for metadata, not review bodies), and Khmer-, Vietnamese- and Thai-language consumer forums were not searched. **The negative finding is weaker than it looks.** See Manual Research Recommendations.

---

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | **29 Jun / 1 Jul 2026** | **Throo officially launches in New York City** — TLC-authorised, five boroughs, rider and driver apps on iOS and Android; public beta from **10 Jun 2026**; **50,000+** drivers pre-registered. Separate brand, separate domain (`ridethroo.ai` / `ridethroo.com`), separate NY entity (**Zero Commission LLC**) | Market Expansion | [PRNewswire](https://aijourn.com/throo-launches-in-new-york-city-with-lower-fares-for-riders-and-zero-commission-for-drivers/) |
| 2 | **1 Jul 2026** | 🤖 **Agentic payments API shipped** — *"an API that lets AI agents request, track, and **autonomously pay for a ride** without a person ever opening the app"*, pitched for enterprise AI tools and coding agents | Tech Blog / Conference Signal | same |
| 3 | **24 Mar 2026** | **US market entry announced**, citing **150M+ global trips**; driver registration opened 3 Mar 2026 | Market Expansion | [BusinessWire](https://www.businesswire.com/news/home/20260324338681/en/Zero-Commission-Ride-Hailing-Platform-TADA-Enters-U.S.-Market-Following-Completion-of-Over-150-Million-Global-Trips) `[403 — not fetched; headline figure independently confirmed via the fetched PRNewswire copy]` |
| 4 | **31 Dec 2025** | **Singapore rider and driver terms rewritten** — adds an on-chain loyalty addendum ("TADA Points", "Hotpot" self-custody) that contemplates *"driver incentives, **cash-advance eligibility**, or other financial programs"* underwritten on on-chain ride history. **A driver-fintech build, in their own legal documents** | Licence/Product Signal | [tada_terms_en_SG.md](https://policy.tada.global/policies/tada_terms_en_SG.md) |
| 5 | **22 Jan 2025** | **TADA Wallet launched (Cambodia)** — own stored-value balance, in-app top-up, non-refundable and non-withdrawable, indefinite validity unless dormant two years | Payment Infrastructure | [wallet_terms_en_KH.md](https://policy.tada.global/policies/wallet_terms_en_KH.md) |
| 6 | **23 Sep 2026** | **Throo expands to Denver** — corroborated in production config: `CO → COOP` brand with a Colorado state geofence, plus **COOP Rideshare** and **COOP Drivers** apps under MVL Foundation. `NJ` and `CT` are already in the region enum | Market Expansion | [Axios](https://www.axios.com/local/denver/2026/09/23/throo-denver-rideshare) `[403 — not fetched]` + [config](https://go.tada.global/assets/productConfig-D7RveucL.js) |
| 7 | **2024** | **Hong Kong and Thailand launched** | Market Expansion | [Fortune](https://fortune.com/2025/12/25/the-worlds-leading-blockchain-based-taxi-app-is-setting-its-sights-on-new-york-city/) |

**Explicitly:** *"No public payment-related RFP found."* No job posting mentioning PSP evaluation, payment-platform migration or orchestration was found for MVL Foundation or TADA Mobility; careers pages were not reachable, so this is **not found**, not **does not exist**.

**Also on the product roadmap, from the production nav:** `AV (Coming soon)` (autonomous vehicles), `/rentals` ("Rentals (Beta)" — vehicle rentals for TADA drivers), `/transparency` ("On-Chain Dashboard"), and the **ONiON EV** programme (`com.onionev.userapp`) — MVL's electric tuk-tuk/vehicle line for Cambodia. Vehicle rentals to drivers are a **recurring-billing** product, which would be the one place `subscription-payments.md` becomes relevant. It is in beta and no billing detail was found.

---

## Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | **7 Nov 2024** | **"Stripe Powers TADA's Southeast Asia Expansion"** — Stripe named as the payment partner across SG, VN, KH, TH *"and soon Hong Kong"*; Adaptive Acceptance and Radar cited; Apple Pay and **Thailand's PromptPay** named as planned additions | ⭐ **The single most important payment source in this account.** Establishes the incumbent, the architecture, the published metrics and a dated roadmap we can now measure against | [techcoffeehouse](https://techcoffeehouse.com/2024/11/07/stripe-powers-tadas-southeast-asia-expansion-amid-intense-ride-hailing-competition/) |
| 2 | **undated (c. Nov 2024)** | **Stripe customer story** — *"0% fraudulent dispute rate · 98% authorisation rate · 2.8% increase in authorization rates"*; cards processed in SGD; one stored card used across all operating countries; pre-authorisation holds; network tokens | ⭐ The incumbent's own published performance claims — know them before the call | [stripe.com/customers/tada](https://stripe.com/customers/tada) |
| 3 | **1 Jul 2026** | **Throo's agentic payments API** — AI agents can autonomously pay for rides | A live machine-initiated payment flow. Stored credentials, MIT flagging and agentic-commerce acceptance all become live concerns | [PRNewswire](https://aijourn.com/throo-launches-in-new-york-city-with-lower-fares-for-riders-and-zero-commission-for-drivers/) |
| 4 | **25 Dec 2025** | **Fortune interview with Kay Woo** — revenue **US$19.8M** (to Oct 2024) vs **US$15.7M** (2023); per-ride driver fee **~US$0.78–0.92**; SG share **11.1%** in 2022; revenue streams named as platform fees + anonymised driving-data sales + MVL tokens | The only revenue and unit-economics source found. **Also the basis for the TAL revenue correction** | [Fortune](https://fortune.com/2025/12/25/the-worlds-leading-blockchain-based-taxi-app-is-setting-its-sights-on-new-york-city/) |
| 5 | **21 Aug 2026** | **NY1 / NYC TLC** — 53,000+ drivers recruited; **"We charge a $1 fee for the drivers. That's it"**; **profitable in Singapore, Vietnam, Hong Kong and Thailand**; TLC-reported 2,047 drivers / 2,547 trips in June 2026 | Billing unit from the CEO's mouth, plus a regulator-sourced volume figure. 🚩 **Note Cambodia is absent from the profitability list** | [NY1](https://ny1.com/nyc/all-boroughs/news/2026/08/21/new-ride-hail-app-throo-looks-to-take-on-uber--lyft-in-new-york-city) |

**Provider removals:** *"No provider removal found."* No source indicates TADA has dropped Stripe or any payment method. ⚠️ **One unresolved asymmetry, recorded rather than resolved:** Stripe's case study and the Nov-2024 press describe a **four-country-plus-HK** footprint, yet the **SG, KH and TH rider terms contemplate only cash and cards** while the app catalogue carries eight local wallet rails. Either the terms are stale (the KH set was last modified 20/10/2020) or some wallet rails are collected outside the in-app rider charge. **Do not resolve this by assertion; ask.**

---

## Section 8: Checkout Experience Audit

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | **Native in-app only.** No web checkout exists. `tada.global` is a client-rendered Vite marketing SPA (6,288-byte shell, single `<div id="root">`, zero card fields, zero payment route). `go.tada.global` is a Remix live-trip share page on Vercel | n/a | 🚩 **Caution flagged by the method:** a route named `pay/`-anything is not evidence of a payment page. Here there is not even that — the only payment-adjacent public surface is a **read-only trip receipt** showing `Fare`, `Est. Total Fee Charged` and `Payment Method` |
| Guest checkout | ❌ No. Rider terms: *"you must register for and maintain an active account"*, 18+, one account per person | n/a | Account-mandatory by design |
| Steps to complete payment | Rider app: `Ride Request → Driver Matching → Riding → Pay & Feedback`. **Payment is deducted automatically on the driver confirming arrival** — no explicit pay step | Good (frictionless) | From the production string catalogue |
| Card input experience | **Not observable.** Stripe is confirmed, with pre-authorisation holds configured and network-token-vs-PAN testing — consistent with a Stripe mobile SDK and tokenised capture, but the app binary was not inspected | **Not accessible** | `[INFERENCE, not confirmed]` |
| Payment methods visible | **18 keys enumerated** — see Section 4. Per-market rendering not observable from outside | Good (breadth) | First-party catalogue |
| Location-based method display | **Yes, by construction** — the production geofence maps country → cities (`SG:[SIN]`, `KH:[PNH,REP,SHV,KPK]`, `VN:[HCM,HAN]`, `TH:[BKK]`, `HK:[HKG]`, `CO:[DEN]`, `NY:[NYC]`) and brand (`CO→COOP`, `NY→THROO`), and the policy site resolves documents by region via the browser geolocation API | Good | [config](https://go.tada.global/assets/productConfig-D7RveucL.js) |
| Instalment / EMI | None, and **correctly so** — low-ticket single-shot fares | n/a | — |
| 3DS implementation | **Not detected.** No 3DS, EMV or ACS string in any fetched asset. Pre-authorisation holds are confirmed, which is a different mechanism | **Not accessible** | — |
| PCI indicator | Stripe-processed with tokenisation and network tokens → **likely reduced scope** | **Not accessible** | See Section 9 |
| Mobile responsiveness | The product *is* mobile. Marketing site is responsive; `apple-itunes-app`-class app hand-offs via `tada-rider.app.link` / `tada-driver.app.link` (Branch deep links) | Good | — |
| Multi-currency / local pricing | 🚩 **Cards are processed in SGD** per Stripe. **No ISO currency table exists anywhere in the bundle** — no `USD`, `KHR`, `VND`, `THB`, `HKD` literals at all. Fares are presumably displayed in local currency by the app, but **no evidence of local-currency *settlement* was found** | **Poor / unknown — and this is the cross-border story** | [Stripe](https://stripe.com/customers/tada) |
| Saved payment methods | ✅ Yes, and **one stored card works across all operating countries** — Stripe's own wording. Card account updater via Adaptive Acceptance refreshes credentials automatically | Good — *and it is exactly what creates the cross-border exposure* | [Stripe](https://stripe.com/customers/tada) |
| Error message clarity | **Not observable.** The documented failure path is instrument fallback, then cash | **Not accessible** | HK terms §3.1 |

> *"Full checkout flow not accessible. Findings limited to publicly observable elements."* **Section 8 is structurally limited for this account, not through environment failure but because the merchant has no web checkout to audit.** The compensating evidence is unusually strong: the first-party method catalogue, the geofence/brand config, and five jurisdictions of rider terms describing the payment mechanics in prose.

---

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | ❌ **Not found.** No PCI statement, AOC, trust page or security page located | — |
| Card data handling | **Likely SAQ A / SAQ A-EP equivalent via Stripe mobile SDK tokenisation** — `[INFERENCE, not confirmed]` | [Stripe](https://stripe.com/customers/tada) |
| Recommended Yuno integration | **SDK**, for a native-app-only merchant already on a PSP SDK with network tokens. A back-to-back API integration would push them toward holding PAN data they currently avoid | analyst judgement |

*"No direct PCI compliance documentation found publicly for TADA Mobility."*

> `[INFERENCE, not confirmed]`: Based on confirmed use of **Stripe** with tokenised capture, **network tokens** (Adaptive Acceptance *"automatically checks if it can improve acceptance rates by using a network token versus a credit card number"*) and a **card account updater**, TADA's PCI scope is likely reduced, with Stripe handling card data. **No compliance level is stated here because none was evidenced.**

**One adjacent security observation, recorded with deliberate restraint:** the public production bundle contains **hard-coded HTTP Basic client credentials** for the TADA driver app API and the MVL homepage FAQ client. **[live credentials present — values deliberately not recorded.]** These are **not** payment credentials and prove no payment vendor. No authenticated or state-changing request was made. Mentioned only because it is a genuine exposure and because the next analyst should not be tempted to use it.

---

## Section 10: Strategic Insights & Outreach Angles

> ### **⭐ Insight #1 — THE PITCH SPINE: in a zero-commission model, payment success IS revenue collection**
>
> **This is the insight to build the whole sequence on. Everything below it is supporting evidence for this one.** Promoted to #1 by Prateek, 2026-10-12.
>
> **Evidence — TADA's own Hong Kong rider terms, verified verbatim against the live document ([tada_terms_en_HK.md](https://policy.tada.global/policies/tada_terms_en_HK.md)):**
> 1. *"TADA facilitates the Rider's payment of the applicable Fares **(unless paid in cash)** on the Driver's behalf as a payment collection agent."*
> 2. *"If your primary account payment method is determined to be expired, invalid or otherwise not able to be charged... you may choose to **settle the Fares and Platform Fees in full** in cash **directly with the Driver**."*
>
> **The mechanism — an asymmetry inside their own stack:**
> - **Card ride:** TADA sits in the money flow as collection agent. Its fee nets automatically. Zero collection cost.
> - **Cash ride, including every declined card:** TADA is **contractually outside the flow**. The rider hands the fare *and TADA's own Platform Fee* to the driver. TADA's revenue lands in the driver's pocket and must be recovered from them.
>
> **Pain Point:** A decline here does not produce an abandoned cart — the service is still delivered and the driver is still paid. It produces an **account receivable against one of their own drivers**. Acceptance is not a conversion-funnel concern at this merchant; it is the revenue-collection mechanism. At ~1.5–2.1M rides/month against a ~US$0.80 per-ride fee, **every 1 percentage point of rides that falls to cash is roughly US$150–200k/year** that self-collects on a card and has to be chased on cash. That arithmetic is theirs, from their own published figures — we supply no invented number.
>
> **⚠️ Why this beats the cross-border angle, and why it must lead:** TADA **publishes a 98% authorisation rate** (see the Approval-Rate Dossier below). Any pitch shaped like *"your approval rates are leaking"* is rebutted instantly from their own case study. This insight **concedes the 98% and attacks its denominator** — cash rides and riders who bounced off a missing rail are not in that number at all. It is the one angle their headline metric cannot answer.
>
> **How every other finding feeds this one:**
> - **PromptPay absent 23 months** (Insight #4) → a Thai rider's default rail is missing → cash → fee to chase
> - **Bakong/KHQR absent, four wallets wired separately** (Insight #3) → they already know this, which is why they built four integrations in their most cash-heavy market, and still lack the national rail
> - **PayNow absent in Singapore** → the same gap in their home market
> - **SGD cross-border, no local entity in KH/VN/HK** (Insight #2) → raises the decline rate that triggers the cash fallback
> - **Agentic payments API** (Insight #6) → ⭐ a machine-initiated ride has **no cash fallback available**; there is no human in the flow to hand over notes. Their newest product is where this breaks hardest
>
> **Yuno Value Proposition:** Local acquiring and local rails per market behind one integration, so the rider's preferred method is present and the fare stays inside TADA's collection flow instead of falling out of it. Framed as protecting the collection mechanism, not as lifting an auth rate they already report as 98%.
>
> **Best Success Case:** **inDrive** — *~90% approval, 10 new countries in under 8 months.* Multi-country ride-hailing, same driver-economics positioning. ⚠️ Note inDrive's published approval figure (~90%) is **below** TADA's self-reported 98%, so **do not put the two numbers side by side** — use inDrive for the expansion-velocity half of the case, not as an approval-rate benchmark.
>
> **Embedded discovery question (use in E3 or E4):** *"Do you track cash-fallback rate separately by market?"* Easy to answer, not a yes/no on a meeting, flattering rather than accusatory — and it is the single unknown that sizes this entire business case.
>
> **Outreach Angle:** Your HK rider terms say TADA collects the fare as the driver's payment collection agent — *unless it's paid in cash*, and that if a card can't be charged the rider settles the fare and your platform fee directly with the driver. So a decline at TADA isn't a dropped basket, it's a fee you have to go and recover from your own driver. Curious whether cash-fallback rate is something you track per market.
>
> **Suggested Subject Line:** When a decline becomes a driver receivable
>
> **🚩 Three things to get right before sending:**
> 1. **Those two quotes are from the HONG KONG terms.** I checked Singapore — the SG terms are far thinner (*"you may choose to pay for the transportation service by cash or credit card"*), with **no collection-agent language and no cash-fallback clause**. Say "your HK terms", never "your terms". HK is also their newest APAC market and the one missing from our TAL row.
> 2. **Do not assert a cash share.** We do not have one; it is the largest open unknown in this account. The strength of this insight is structural, not quantified.
> 3. **Do not frame it as "you're losing money."** Frame it as the asymmetry — their card book self-collects, their cash book does not — and add the diplomatic clause: this is the zero-commission model working as designed, not anyone doing anything badly.

> ### **Insight #2: One Singapore acquiring account, in Singapore dollars, for five countries**
> **Evidence:** **Section 3A** — Stripe's own case study: developers configured Payments so riders *"can pay for services with credit and debit cards **processed in Singapore dollars (SGD)**"*, and *"Riders can use **the card they store in their account profile across all the countries that TADA operates in**"* ([stripe.com/customers/tada](https://stripe.com/customers/tada)). **+ Section 2** — **no local entity found in Cambodia, Vietnam or Hong Kong**; the Vietnamese rider terms contract riders to a **Singapore** company, **TADA Technologies Pte. Ltd** ([tada_terms_vn_VN.md](https://policy.tada.global/policies/tada_terms_vn_VN.md)), and the HK privacy policy routes data *"within or outside of **Singapore**"* ([tada_privacy_en_HK.md](https://policy.tada.global/policies/tada_privacy_en_HK.md)).
> **Pain Point:** Every Cambodian, Vietnamese, Thai and Hong Kong cardholder is being authorised cross-border against a Singapore account in a foreign currency. Per `apac-payments.md` §3, domestic issuers in this region decline foreign-acquired transactions at materially higher rates than local-acquired ones, and there is no IFR-style cap to blunt the scheme cost. An FX leg sits on every non-SGD rider. And for this merchant the cost of a decline is not a retry — the documented fallback is *"settle the Fares in cash directly with the Driver"*, which removes TADA's fee from the ride altogether.
> ⚠️ **REBUTTAL RISK — found in the same case study during Prateek's audit, 2026-10-12. Read before sending.**
> The SGD sentence sits in the section describing the **original Singapore build** (*"In just two weeks, developers added Stripe Payments to TADA's mobile app so that riders can pay for services with credit and debit cards processed in Singapore dollars (SGD)"*), while *"across all the countries that TADA operates in"* sits in the later **Results** section. Treating the two as one present-tense fact — "all five markets are acquired in SGD today" — is an **[INFERENCE, not confirmed]**, not Stripe's assertion.
> **And the same page cuts the other way.** Its Challenge section states TADA wanted *"accepting credit card payments using **local currencies**"*. So the merchant can legitimately reply *"we process in local currencies."* I verified both sentences verbatim against the live page.
> **How to use it:** ask, do not assert. The question form in the Outreach Angle below is safe because it asks whether they measure the approval gap. A flat claim that every market is acquired cross-border in SGD is **not** safe and would be rebuttable from their own case study. The *robust* half of this insight is the entity finding, which does not depend on the currency at all: **no local entity was found in Cambodia, Vietnam or Hong Kong**, and the Vietnamese rider terms contract riders to a Singapore company.
>
> **Yuno Value Proposition:** Local acquiring per corridor behind one integration, so a Cambodian card is authorised domestically rather than cross-border, with the Singapore Stripe account retained as the fallback leg rather than the only leg.
> **Best Success Case:** **inDrive** — *~90% approval, 10 new countries in under 8 months.* Multi-country ride-hailing, same driver-economics positioning, and the approval-rate metric is the one TADA already publishes a number for.
> **Outreach Angle:** Stripe's case study says a TADA rider's stored card works across all five markets and that cards are processed in Singapore dollars — which means a Phnom Penh rider's card is being authorised cross-border from Singapore. Curious whether the approval gap between your SGD-domestic traffic and your other four markets is something you measure separately.
> **Suggested Subject Line:** Your Cambodian riders' cards, authorised from Singapore

> ### **Insight #3: Four Cambodian wallet integrations where the country built one rail**
> **Evidence:** **Section 4** — TADA's own 18-key payment catalogue carries **ABA Pay, Wing Pay, Pi Pay and Chip Mong Pay** as four separate, unambiguously Cambodian integrations (a fifth key, MOMO Pay, is present but its market is unevidenced — see the Section 4 caveat), while **`bakong` and `khqr` return zero occurrences** ([index-BbiHo7SX.js](https://tada.global/assets/index-BbiHo7SX.js)). **+ Section 3A/7** — their own Head of Product, in Stripe's case study: *"**Regional payment integration processes usually take a lot of time**, but with Stripe, it's never a worry."* **+** third-party rail context: KHQR carried **601.3M transactions / US$75.8bn in 2023** across **3.3M+ merchants**, Cambodian digital payments ran at **2.4× GDP**, and KHQR exists so a merchant can accept *"a single QR code, regardless of which"* bank app the payer uses ([Kapron Asia](https://kapronasia.com/insight/blogs/payments-research/asia-payments-research/instant-payments-are-fueling-cambodias-e-commerce-boom)).
> **Pain Point:** Not coverage — they have coverage. It is **unit cost of coverage**. Four bilateral integrations, four sets of credentials, reconciliation and failure modes, five vendor relationships, in one city-sized market — and the same pattern restarts in every new country. They have already told their PSP's marketing team that regional integration takes too long.
> **Yuno Value Proposition:** One integration, local rails added as configuration rather than engineering. The argument lands on time-to-market and maintenance cost, not on acceptance breadth — because breadth is a problem they have already solved expensively.
> **Best Success Case:** **inDrive** — *10 new countries in under 8 months.* Launch velocity is the matching metric.
> **Outreach Angle:** You have ABA Pay, Wing Pay, Pi Pay and Chip Mong Pay wired in separately, which is four integrations covering institutions that all sit behind one national rail. Your head of product told Stripe that regional payment integration takes a lot of time — that is the part I would want to fix before Denver and New Jersey.
> **Suggested Subject Line:** Four Cambodian integrations, one national rail

> ### **Insight #4: PromptPay — a published roadmap item, 23 months unshipped**
> **Evidence:** **Section 7** — Stripe's case study (November 2024) states TADA planned to add *"a Thailand-based payment method called **PromptPay**"* alongside Apple Pay ([stripe.com/customers/tada](https://stripe.com/customers/tada)). **+ Section 4** — in the October 2026 production catalogue, **Apple Pay is present and PromptPay returns zero occurrences** ([index-BbiHo7SX.js](https://tada.global/assets/index-BbiHo7SX.js)). **+ Section 2** — Thailand has a local entity (**TADA MOBILITY (THAILAND) CO., LTD.**, Bangkok), Thai-language rider terms, Thai emergency-service integration and a live **ThaID** national-identity flow, so this is a committed market, not a toe in the water.
> **Pain Point:** Two years to not ship one QR rail in a market where they have incorporated a company, localised the product and integrated the national identity system. Half the stated roadmap shipped; the half that needed a local rail did not. That is the signature of rails being an engineering project rather than a configuration change.
> **Yuno Value Proposition:** A rail that is a config toggle ships in days, not never. The proof point is sitting in their own backlog.
> **Best Success Case:** **inDrive** — new-market launch velocity.
> **Outreach Angle:** Your Stripe case study from November 2024 lists Apple Pay and PromptPay as what was coming next. Apple Pay shipped. PromptPay still is not in the app two years on, and you have a Bangkok entity and ThaID live. Usually that gap is integration queue, not priority.
> **Suggested Subject Line:** Apple Pay shipped. PromptPay didn't.

> ### **Insight #5: Card cost is carved out of the zero-commission promise — so acceptance is a board-level number here**
> **Evidence:** **Section 12 / Quick Look** — TADA's own production copy: *"TADA takes zero commission. **Except for platform and transaction fees for debit/credit cards**, the full amount of the fare is for a driver"* ([index-BbiHo7SX.js](https://tada.global/assets/index-BbiHo7SX.js)). **+ Section 7** — the entire revenue line is a flat **~US$0.78–0.92** per-ride software fee, on **US$19.8M** of annual revenue ([Fortune](https://fortune.com/2025/12/25/the-worlds-leading-blockchain-based-taxi-app-is-setting-its-sights-on-new-york-city/)), against a **~US$13.3** average ride value derived from their own 150M-rides / ~US$2bn-GMV claims.
> **Pain Point:** On a ~US$13 fare the platform keeps under a dollar. Card acceptance cost is therefore a **double-digit percentage of TADA's own take on every card-paid ride** — and they have put that carve-out in writing to drivers, which means every basis point of MDR is visible to their most vocal stakeholder group. No other merchant archetype has acceptance cost sitting this close to gross margin.
> **Yuno Value Proposition:** MDR reduction through PSP diversification and local acquiring is not a cost-centre optimisation for this merchant — it moves the number they report as revenue. And unlike most cost pitches, this one has a constituency: drivers already know the fee exists.
> **Best Success Case:** **inDrive** — the only multi-country mobility case with published numbers. ⚠️ Its published metrics are approval-rate and launch-velocity, **not cost** — so use inDrive for credibility and keep the cost argument as arithmetic from TADA's own figures rather than implying inDrive proved a cost saving.
> **Outreach Angle:** Your driver page says the full fare goes to the driver except platform and card transaction fees. On a ~$13 average ride where you keep under a dollar, card cost is a meaningful share of your own take — which makes acceptance economics unusually load-bearing for a zero-commission model.
> **Suggested Subject Line:** The one fee you kept in the zero-commission promise

> ### **Insight #6: Five markets, three US states, an agentic payments API — and the acquiring footprint has not moved**
> **Evidence:** **Section 6** — Throo launched in NYC on **29 Jun 2026** with a **live API that lets AI agents autonomously pay for rides** ([PRNewswire](https://aijourn.com/throo-launches-in-new-york-city-with-lower-fares-for-riders-and-zero-commission-for-drivers/)); Denver/Colorado live as **COOP**; **NJ** and **CT** already in the production region enum ([constants](https://go.tada.global/assets/constants-CAXCtKtj.js)); `AV (Coming soon)` and a driver-rentals beta in the nav. **+ Section 3B** — **no orchestration layer anywhere**, and the only confirmed acquiring arrangement is a single Singapore Stripe account. **+ Section 11C** — **Uber and inDrive**, their direct competitors in NYC and in emerging markets respectively, are both publicly named Yuno customers on y.uno's travel/mobility list.
> **Pain Point:** The company is adding jurisdictions and payment *modalities* (machine-initiated, autonomous, no human at the checkout) faster than it is adding acquiring capability. Agent-initiated charges are the hardest category to get authorised — no cardholder present, stored credential, MIT flagging, and issuer models that have never seen the pattern. Attempting that on a single acquirer with no failover is where approval rates go to die, and it is going live in the most competitive ride-hailing market on earth against two incumbents who already run orchestration.
> **Yuno Value Proposition:** Multi-acquirer reach and failover at the moment the transaction mix shifts to machine-initiated — plus one integration to carry NJ, CT and whatever follows, instead of a per-state payments project.
> **Best Success Case:** **inDrive** — *10 new countries in under 8 months* is literally the capability being tested here. **Uber** nameable as a credibility signal only, with **no number attached** — and pointedly, Uber is the rival Throo names in its own launch coverage.
> **Outreach Angle:** You shipped an API in July that lets AI agents pay for rides without a human in the flow, and you are opening New Jersey and Connecticut next. Agent-initiated authorisations are the hardest thing to get approved on a single acquirer — it is the one part of the stack I would not want to be single-threaded on going into that.
> **Suggested Subject Line:** Agent-paid rides on one acquirer


### 📊 APPROVAL-RATE DOSSIER — read before any email that touches auth rates

**TADA publishes an authorisation rate. Know it cold before you write a word about approvals.**

> *"Over the last 12 months, we have maintained a **0% dispute rate** by using Radar,"* said Tay. *"By adding Adaptive Acceptance, we **increased authorization rates by 2.8%**, so we now process **98% of all transactions**."*
> — Kenneth Tay, Head of Product, [stripe.com/customers/tada](https://stripe.com/customers/tada). Verified verbatim against the live page by Prateek, 2026-10-12.

| Attribute | What it actually is |
|---|---|
| **Headline figure** | **98% authorisation rate** · **+2.8%** uplift from Adaptive Acceptance (so ~**95.2%** before it) · **0%** dispute rate |
| **Provenance** | Self-reported by TADA's Head of Product, quoted in **Stripe's own marketing asset**. Never audited, no methodology published |
| **Age** | **~November 2024 — roughly two years stale.** The page carries **no publication date metadata at all**; it is datable internally because it says Thailand launched in 2024 and Hong Kong starts *"over the next three months"*, i.e. it was written **before HK went live**. Corroborating trade press is dated 7 Nov 2024 |
| **Footprint covered** | SG, KH, VN, plus a **brand-new** Thailand. **Hong Kong was not yet live. Throo/NYC and COOP did not exist.** The figure predates two of their seven current markets |
| **Granularity** | 🚩 **Blended. No country split is published anywhere on the page** — I checked for per-market and per-country qualifiers and found none. A 98% blend can conceal a materially worse Cambodia or Vietnam |
| **Denominator** | 🚩 **The critical point. *"98% of all transactions"* means card attempts that reached Stripe.** It excludes cash rides entirely, and excludes riders who never attempted a payment because the rail they wanted was not on the screen |

**How to handle it in outreach — three rules:**

1. **Never attack the 98%.** It is their published number, they are proud of it, and a merchant who reports a +2.8% improvement **measures auth rate and acts on it**. They know their numbers better than we do. An opener shaped like *"your approval rates are leaking"* gets dismissed in one line.
2. **Concede it and go after the denominator.** 98% is **not** 98% of rides — it is 98% of the subset that got as far as a card attempt. The cash book and the bounced-off-a-missing-rail riders sit outside that number completely. **That is where Insight #1 lives, and it is the one place their headline metric cannot answer.**
3. **Never put inDrive's ~90% next to TADA's 98%.** It invites the comparison we lose. Use inDrive for **expansion velocity** (10 new countries in under 8 months), not as an approval benchmark.

**The one approval-rate question that is safe to ask**, because it is the gap in their own disclosure rather than a challenge to it: *"Is the 98% a blended number across all markets, or do you see a spread between your SGD-domestic traffic and the other four?"* They published a blend with no split; asking for the split is legitimate and, if they answer, it hands us the local-acquiring case in their own numbers.

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
0. ⭐ **THE SPINE —** Your HK rider terms say TADA collects the fare as the driver's payment collection agent *unless it's paid in cash*, and that when a card can't be charged the rider settles the fare and your platform fee directly with the driver — so a decline there isn't a dropped basket, it's a fee you have to recover from your own driver.
1. Stripe's own case study says a TADA rider's stored card works across all five of your markets and that cards are processed in Singapore dollars — so a Phnom Penh rider's card is authorised cross-border from Singapore every time.
2. You have ABA Pay, Wing Pay, Pi Pay and Chip Mong Pay wired in as four separate integrations, covering institutions that all sit behind one national rail.
3. Your November 2024 Stripe case study named Apple Pay and PromptPay as next; Apple Pay shipped, PromptPay still is not in the app, and you have had a Bangkok entity and ThaID live the whole time.
4. Your driver page says the full fare goes to the driver except platform and card transaction fees — on a ~$13 average ride where you keep under a dollar, that carve-out is a real share of your own revenue.
5. You shipped an API in July that lets AI agents pay for rides with no human in the flow, and NJ and CT are already in your config — agent-initiated authorisations are the last thing you want single-threaded on one acquirer.

**Cold call openers (conversational, one sentence each):**
1. "I read your Stripe case study — the 98% authorisation rate is strong; is that one number across all five countries, or do Cambodia and Vietnam sit separately?"
2. "You've got four Cambodian wallet apps integrated individually — was that a deliberate call, or just how it accumulated as each bank came to you?"
3. "Kenneth's line in the Stripe piece was that regional payment integration usually takes a lot of time — is that still the bottleneck going into Denver and New Jersey?"
4. "Of your roughly one and a half to two million rides a month, how much of that is actually paid digitally versus cash? That's the number I can't find anywhere."
5. "The agent-pays-for-the-ride API — how are those authorisations performing against your normal rider traffic?"

---

## Section 11: Similar Companies & Prospecting Pipeline

### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| **Grab** | grab.com | Singapore | **$955M Q1'26 (+24% YoY); FY26 guide ~$4.05B** | **SG, KH, VN, TH** — all four of TADA's main markets | **In-house GrabPay stack + external acquiring partners**; **In-house Routing**. In Cambodia: **ABA PayWay** gateway integrated as default pay-in **and ABA accounts for automatic driver payouts** | TAL (verified by independent CSV parse) + [b2b-cambodia, 3 Sep 2025](https://b2b-cambodia.com/news/milestone-in-digital-integration-aba-and-grab-advance-cashless-ecosystem-in-cambodia) |
| **Ryde Group Ltd** | rydesharing.com | Singapore | **~$20M**; listed **NYSE American: RYDE** | **SG** — closest size-comparable listed peer | None named. **30 Sep 2026: announced "next-generation payment capabilities" as part of Ryde 2.0 over the next 12 months** — a payments programme, *not* a confirmed orchestration adoption | [Newswire, 30 Sep 2026](https://www.newswire.com/news/ryde-advances-ryde-2-0-with-ai-powered-mobility-ev-fleet-technology-and-next) |
| **ComfortDelGro (CDG Zig)** | cdgtaxi.com.sg | Singapore | **~$3.3B (FY24)** | **SG** (+ AU/UK/CN) | None named. **Alipay+ / Touch 'n Go eWallet** cashless deployment across taxis `[UNVERIFIED — search summary only, undated]` | TAL + search summary |
| **Gojek / GoTo** | gojek.com · gotocompany.com | Indonesia | Part of GoTo (~$1B) | None direct — Indonesia is not a TADA market | **In-house Routing**; Midtrans + GoPay | TAL (verified) |
| **Maxim** | taximaxim.com | ⚠️ TAL says Singapore — **doubtful** | Not found | SEA overlap claimed | None found | TAL — **see correction note** |
| **inDrive** | indrive.com | — | Multi-country (50+) | Emerging-market overlap; same driver-economics pitch | ⭐ **Yuno customer** — *~90% approval, 10 new countries in under 8 months* | [y.uno](https://y.uno/en/success-stories/indrive) |
| **Uber** | uber.com | USA | — | **NYC — Throo's named head-to-head rival** | ⭐ **Yuno customer.** Named on y.uno's site-wide and travel/mobility lists. **No published metrics — nameable only** | y.uno customer lists |
| **Lyft** | lyft.com | USA | — | **NYC** | None found | — |
| **PassApp** | — | Cambodia | Not found | **KH** | ❌ Not researched — budget exhausted | — |
| **Be / Xanh SM** | — | Vietnam | Not found | **VN** | ❌ Not researched — budget exhausted | — |

### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Lalamove | lalamove.com | On-demand delivery/trucking | HK + Asia + LATAM | *"driver payouts in many currencies"* — same dual pay-in/payout shape, wider corridor set | TAL |
| Rapido | rapido.bike | Bike-taxi aggregator | India | Huge small-ticket ride volume. **TAL shows `Juspay`** — a displacement motion, and the clearest proof that mobility peers do buy orchestration | TAL |
| Namma Yatri / Odisha Yatri | — | Zero/low-commission ride-hailing | India | ⭐ **The closest ideological analogues to TADA anywhere** — explicitly zero-commission, driver-first. Same unit economics problem: a flat fee per ride means acceptance cost is a share of revenue | TAL |
| Zoomcar | zoomcar.com | Self-drive car rental | India + emerging | **TAL shows `Juspay`**. Relevant to TADA's `/rentals` beta | TAL |
| Bolt.Earth | bolt.earth | EV charging | India | **TAL shows `Juspay`**. Many small frequent driver payments — relevant to the ONiON EV programme | TAL |
| Pathao | — | Super app / ride-hailing | Bangladesh | Emerging-market, multi-rail, driver-payout shape | TAL |
| Anywheel / Beam / Neuron | — | Micromobility | SG / ANZ | Small-ticket, app-only, same Singapore acquiring base | TAL |
| Kakao Mobility | — | Mobility | South Korea | MVL's founders are Korean and `mvltaxi_driver_terms` exists in Korean only — relevant if Korea ever reactivates | TAL |

### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| **Uber** | **Yuno** | Not stated | Ride-hailing — **Throo's direct NYC rival** | y.uno site-wide + travel/mobility customer lists (via `.claude/commands/full-outreach.md` L543–545, L530) |
| **inDrive** | **Yuno** | Not stated | Ride-hailing, 50+ countries | [y.uno/en/success-stories/indrive](https://y.uno/en/success-stories/indrive) |
| **Rapido** | **Juspay** | Not stated | Bike-taxi, India | `accounts/apac-tal.csv` — ⚠️ TAL entry, needs independent confirmation |
| **Zoomcar** | **Juspay** | Not stated | Car rental, India | `accounts/apac-tal.csv` — ⚠️ TAL entry, needs independent confirmation |
| **Bolt.Earth** | **Juspay** | Not stated | EV charging, India | `accounts/apac-tal.csv` — ⚠️ TAL entry, needs independent confirmation |
| **Grab / GoTo / Gojek** | **In-house routing** (not a third-party orchestrator) | — | Super apps | `accounts/apac-tal.csv` (verified by CSV parse) |

> **The usable competitive-urgency line:** TADA's two most directly comparable competitors — **Uber** in the market Throo just entered, and **inDrive** in the markets TADA already serves — are **both** publicly named Yuno customers, while Grab and GoTo both built routing in-house. **Every serious multi-market ride-hailing peer has an orchestration layer of some kind. TADA has one acquirer and no layer.** ⚠️ The Uber/inDrive evidence is **Yuno's own customer list**, not independent third-party reporting — say it as a customer relationship, never attach a number to Uber, and use inDrive's published figures verbatim or not at all.

### 11D. Prospect Scoring — Ryde Group Ltd (the one worth scoring)

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| Monthly transaction count | ⬜ 0 | Not derivable from the ~$20M revenue figure without an ATV | TAL |
| Orchestration status | ⬜ 0 | None named; a payments programme was announced but no stack disclosed | [Newswire 30 Sep 2026](https://www.newswire.com/news/ryde-advances-ryde-2-0-with-ai-powered-mobility-ev-fleet-technology-and-next) |
| 3+ countries | ❌ 0 | Singapore only | TAL |
| Multiple PSPs | ⬜ 0 | Not found | — |
| Local rail gap in a top-3 market | ⬜ 0 | Not researched | — |
| Recent expansion | ⬜ 0 | Ryde 2.0 is a transformation plan, not a market entry | Newswire |
| Payment issues | ⬜ 0 | Not researched | — |
| Funding >$10M | ⬜ 0 | Not found | — |
| High traffic outside home | ❌ 0 | Single market | TAL |
| Competitor using orchestration | ✅ **+2** | Uber and inDrive are Yuno customers; Grab runs in-house routing | y.uno lists; TAL |
| **Payment job postings / payment programme** | ✅ **+1** | **"Next-generation payment capabilities" over the next 12 months** — a publicly announced payments workstream at a listed company | Newswire |
| **Total** | **3 / 29** | 🔴 **Low on current evidence — but the score is an artefact of thin research, not a verdict.** A listed company (NYSE American: RYDE) with SEC filings and a just-announced 12-month payments programme is a far better prospect than 3/29 implies. **Re-score properly before dismissing.** | — |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | **TADA Mobility** | Target | SG/KH/VN/TH/HK + US | **19/29** | ⭐ High | Single SGD acquirer across 5 countries; Bakong/KHQR absent; agentic payments API live | ✅ Yes (as `TADA`) |
| 2 | **Ryde Group Ltd** | Direct competitor | SG | 3/29 ⚠️ under-researched | 🟢 **Re-score** | **Announced a 12-month "next-generation payments" programme, 30 Sep 2026**, at a company with public filings | ✅ Yes |
| 3 | **Namma Yatri** | Peer — ideological twin | India | Not scored | 🟢 | Explicitly zero-commission: identical flat-fee-per-ride economics, so identical acceptance-cost exposure | ✅ Yes |
| 4 | **Odisha Yatri** | Peer | India | Not scored | 🟢 | Same zero-commission model | ✅ Yes |
| 5 | **Lalamove** | Peer | HK + Asia + LATAM | Not scored | 🟢 | *"Driver payouts in many currencies"*; multi-corridor; ~$1.5B est. | ✅ Yes |
| 6 | **Pathao** | Peer | Bangladesh | Not scored | 🟢 | Emerging-market super app, multi-rail, wallet-heavy | ✅ Yes |
| 7 | **Rapido** | Peer | India | Not scored | 🟢 **Displacement** | TAL shows **Juspay** — orchestration-aware, so the pitch is reach not education | ✅ Yes |
| 8 | **ComfortDelGro** | Direct competitor | SG/AU/UK/CN | Not scored | 🟢 | **~$3.3B FY24**, four countries, high daily fare volume. ⚠️ TAL `HQ Country` cell is empty | ✅ Yes |
| 9 | ⭐ **MVL Foundation / ONiON EV** | **Adjacent entity at the same account** | KH (+ group) | Not scored | 🟢 **Genuine find** | A **separate app and product line** (`com.onionev.userapp`, ONiON EV electric vehicles sold to Cambodian drivers) under the same parent. **Vehicle sales/leases are high-ticket, recurring, and a completely different payment problem from a $13 fare** — and it is not on the TAL | ❌ **No** |
| 10 | ⭐ **Quiks** (MVL group, Indonesia) | **Adjacent entity at the same account** | ID | Not scored | 🟢 **Genuine find** | `quiks_privacy`, `quiks_driver_terms`, `quiks_delivery_terms` exist in **English and Indonesian**, and `ID` is in the region enum — **an Indonesia-facing delivery product in the MVL group that appears nowhere in our records.** QRIS/GoPay/OVO/DANA territory | ❌ **No** |

**Genuine finds not on the TAL:** **MVL Foundation / ONiON EV** and **Quiks (Indonesia)** — both inside the same corporate group as the target, both with their own payment surfaces, neither recorded anywhere. **Throo / Zero Commission LLC (US)** and **COOP (Colorado)** are also group brands with their own payment builds, but they are **out of APAC territory** and route to the relevant region rather than onto the APAC TAL. **inDrive is correctly absent** from the TAL — it is a Yuno customer, not a target, and that is not a defect.

### 🔧 TAL CORRECTIONS — `accounts/apac-tal.csv`, row 632 (`TADA`) and peers

| # | Field | Current | Should be | Evidence |
|---|---|---|---|---|
| 1 | `TADA` → **Operating Countries** | `SG/KH/VN/TH` | **`SG/KH/VN/TH/HK`** (+ note US: NY/CO, out of territory) | TADA's own strings: *"our offices in Singapore, Cambodia, Thailand, Vietnam, and **Hong Kong**"*; HK geofence in production config; `support_hk@tada.global`; HK rider terms dated 04/07/2024 |
| 2 | `TADA` → **Est. Revenue (USD)** | `~$50M est. (MVL)` | **`$19.8M (TTM to Oct 2024, sourced); $15.7M (2023)`** | [Fortune, 25 Dec 2025](https://fortune.com/2025/12/25/the-worlds-leading-blockchain-based-taxi-app-is-setting-its-sights-on-new-york-city/). The `~$50M` figure is **2.5× the only sourced revenue number** and should not survive |
| 3 | `TADA` → **Payment Gateway** | *(empty)* | **`Stripe (Payments + Radar + Adaptive Acceptance); cards processed in SGD`** | [stripe.com/customers/tada](https://stripe.com/customers/tada) |
| 4 | `TADA` → **Payment Orchestrator** | *(empty)* | **`None detected (verified — greenfield)`** — so the blank is now a checked negative, not an unknown | 839KB bundle + 11 rider-app bundles + policy bundle + 16 legal docs, all negative |
| 5 | `TADA` → **COMPANY** | `TADA` | Consider **`TADA Mobility`** for disambiguation from **TaDa Delivery** (AB InBev, LATAM) — the exact collision that made Phase 0 hard | Phase 0 note |
| 6 | `TADA` → **INFO** | *"operates across several Southeast Asian markets"* | Add: Hong Kong; US entry (Throo/NYC, COOP/Colorado) from Jun 2026; revenue model is a **flat ~US$0.80 per-ride driver software fee + rider platform fee**, not a commission | PRNewswire; NY1; Fortune |
| 7 | **`Ryde`** → Est. Revenue | `~$20M (SGX-listed)` | **Listing venue appears wrong — Ryde Group Ltd trades as `NYSE American: RYDE`.** ⚠️ **Not independently confirmed in Prateek's audit** — `rydesharing.com` names no listing venue anywhere on its homepage. Rests on the Newswire release boilerplate alone. **Confirm against an exchange or SEC source before editing the TAL** | [Newswire, 30 Sep 2026](https://www.newswire.com/news/ryde-advances-ryde-2-0-with-ai-powered-mobility-ev-fleet-technology-and-next) |
| 8 | **`ComfortDelGro`** → HQ Country | *(empty)* | **`Singapore`** — the INFO cell already says *"Singapore-headquartered"*, so the empty cell is a simple gap | TAL internal inconsistency |
| 9 | **`Maxim`** → HQ / Operating Countries | `Singapore` / `Singapore` | ⚠️ **Flagged as doubtful, NOT corrected.** The INFO cell itself says *"Southeast Asia, Russia and other emerging markets"*, which contradicts `Operating = Singapore`. **No source was obtained**, so no correction is proposed — only a flag | TAL internal inconsistency |
| 10 | **New rows to add** | — | **MVL Foundation / ONiON EV** (KH, EV sales to drivers) and **Quiks** (ID, delivery) — both MVL group, both with payment surfaces, neither on the TAL | [policy bundle](https://policy.tada.global/assets/index-D4hJ-wRu.js); [App Store developer page](https://apps.apple.com/sg/app/tada-ride-hailing/id1412329684) |

> ### ✅ RETRACTION — the "Gojek row is corrupted" flag is withdrawn, and I verified it independently
> The brief for this run stated that the `Gojek` row in `accounts/apac-tal.csv` was column-shifted, with `HQ` reading `In-house Routing`. **That is not the case, and I confirmed it myself with a proper CSV parse before the coordinator's retraction arrived.** The Gojek row has **17 fields matching the 17-column header**, with `HQ Country = Indonesia` and `Payment Orchestrator = In-house Routing` — correctly placed. The appearance of corruption comes from reading the row with a naive comma split, which breaks on the quoted commas inside the `INFO` field. **No "Gojek corruption" correction is logged.** The only genuine structural gap found in the peer set is **ComfortDelGro's empty `HQ Country`** (#8 above), and the only genuine content doubt is **Maxim** (#9), which is flagged rather than corrected because no source was obtained.

---

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| **Annual Revenue (USD)** | **US$19.8M** for the 12 months to **October 2024**; **US$15.7M** in **2023** (+26% YoY) | ✅ [Fortune, 25 Dec 2025](https://fortune.com/2025/12/25/the-worlds-leading-blockchain-based-taxi-app-is-setting-its-sights-on-new-york-city/) — attributed to Kay Woo. **Supersedes the TAL's `~$50M est.`** |
| **GMV / Gross Transaction Volume** | **"nearly US$2 billion" — CUMULATIVE since 2018**, not annual | ✅ Company claim, [PRNewswire, 1 Jul 2026](https://aijourn.com/throo-launches-in-new-york-city-with-lower-fares-for-riders-and-zero-commission-for-drivers/). ⚠️ **Do not quote this as an annual figure.** Crude annualisation over ~8.25 years gives ~US$240M/yr `[ESTIMATE, not confirmed]`, but growth-weighting makes the current run-rate higher |
| **Average Transaction Value (USD)** | **~US$13.3 per ride** | ✅ **DERIVED:** ~US$2,000M GMV ÷ 150M rides. Both inputs are company claims from the same release. `[DERIVED — treat as indicative]` |
| **Est. Annual Transactions (rides)** | **~18M (floor) to ~25M (ceiling)** | ✅ **DERIVED** two ways: (A) 150M cumulative ÷ 8.25 years = ~18.2M/yr; (B) US$19.8M revenue ÷ US$0.78–0.92 per-ride fee = 21.5M–25.4M/yr (an **upper bound** — revenue includes non-ride lines) |
| **⭐ Monthly transaction count** | **✅ DERIVED: ~1,500,000 – 2,100,000 completed rides/month.** ≥100,000 band → **+5 ICP points. The under-40,000 auto-reject does not fire.** 🚩 **Of which the orchestratable pay-in share is the NON-CASH portion, and that split is NOT PUBLISHED — see the billing-unit box in the ICP breakdown.** Independent corroboration: NYC TLC reported **2,547 Throo trips in June 2026** (US only, immaterial to the total) | ✅ **DERIVED from sourced inputs — not sourced directly, not assumed.** Arithmetic shown in full in the ICP breakdown. Inputs: [PRNewswire](https://aijourn.com/throo-launches-in-new-york-city-with-lower-fares-for-riders-and-zero-commission-for-drivers/) · [Fortune](https://fortune.com/2025/12/25/the-worlds-leading-blockchain-based-taxi-app-is-setting-its-sights-on-new-york-city/) · [NY1/TLC](https://ny1.com/nyc/all-boroughs/news/2026/08/21/new-ride-hail-app-throo-looks-to-take-on-uber--lyft-in-new-york-city) |
| **⭐ BILLING UNIT** | **Three distinct units — do not conflate.** (1) **The rider's fare**, collected by TADA *"as a payment collection agent"* — **this is the Yuno-orchestratable pay-in**, one authorisation per non-cash ride covering fare + platform fee. (2) **The rider-paid Platform Fee** (booking/app fee), inside the same authorisation. (3) **TADA's own revenue: a flat ~US$0.78–0.92 per-ride software fee charged to the DRIVER** (US$1.00 flat in NYC) — a payout-side netting, not a card pay-in. **Plus a fourth, lower-frequency unit: TADA Wallet top-ups**, which batch many rides into one card charge and therefore *reduce* card transaction count while raising average value | ✅ HK rider terms §3.1 ([source](https://policy.tada.global/policies/tada_terms_en_HK.md)); production bundle (*"Except for platform and transaction fees for debit/credit cards..."*); Fortune; NY1; [wallet terms](https://policy.tada.global/policies/wallet_terms_en_KH.md) |
| **Active Customers / Users** | **3M+ riders, ~300,000 drivers** `[UNVERIFIED — Dealroom/LinkedIn profile data, not primary]`. Firmer: **1M+ install band** on Google Play for *each* of the rider and driver apps; **56,455 Apple ratings** (SG storefront, rider); **35,816 Play reviews** | ⚠️ / ✅ mixed — see Section 1-ALT |
| **Primary Currency** | 🚩 **Cards are processed in Singapore dollars (SGD)** across all operating countries. **No ISO currency table exists anywhere in the production bundle.** Fare display currency per market was not evidenced | ✅ [stripe.com/customers/tada](https://stripe.com/customers/tada) |
| **Top 3 Markets by Revenue** | ❌ **Not found.** No market-level revenue split published. `[EST]` ordering (Cambodia, Singapore, Vietnam) is inferred from city counts in the geofence, localisation depth and press, **not** from revenue. 🚩 Note the CEO named **"Singapore, Vietnam, Hong Kong and Thailand"** as profitable markets to NY1 — **and did not name Cambodia**, which may mean volume ≠ profit there, or may mean nothing. Do not build on it | ⚠️ [NY1](https://ny1.com/nyc/all-boroughs/news/2026/08/21/new-ride-hail-app-throo-looks-to-take-on-uber--lyft-in-new-york-city) |
| **Billing channel split (web vs app store)** | ✅ **100% native app, ~0% app-store billing, 0% web.** Ride fares are physical-world services and do **not** route through Apple/Google IAP. There is no web checkout at all | ✅ **This is a positive finding, not a gap.** The `subscription-payments.md` §4 app-store-revenue trap that invalidates consumer-subscription accounts **does not apply here** — essentially the entire digital payment flow is orchestratable |
| **Market position** | **11.1% of the Singapore ride-hailing market in 2022** (Measurable AI). Four years old; no newer figure found | ⚠️ [Fortune](https://fortune.com/2025/12/25/the-worlds-leading-blockchain-based-taxi-app-is-setting-its-sights-on-new-york-city/) |
| **Profitability** | CEO claim: **"already profitable in other markets including Singapore, Vietnam, Hong Kong and Thailand"** | ⚠️ Company claim, unaudited — [NY1](https://ny1.com/nyc/all-boroughs/news/2026/08/21/new-ride-hail-app-throo-looks-to-take-on-uber--lyft-in-new-york-city) |
| **Funding (equity)** | Series A **US$5M** (SV Investment-led; Central Motor, Shimwon participating); total Series A later reported *"just under US$10M / S$14.2M"*; a Shinhan Bank-led bridge reportedly took cumulative investment to ~**KRW 10bn**; **US$15M Series B** for the ONiON EV programme (**undated in result**) | ⚠️ [Vulcan Post](https://vulcanpost.com/683025/mvl-raises-us-5m-series-a-funding/) · [DealStreetAsia](https://media.dealstreetasia.com/stories/mvl-tada-series-a-funding-165204) — **no round confirmed inside the last 12 months** |
| **🪙 MVL token market cap** | **~US$21–25M** (mid-2026). **🚫 NOT revenue, NOT funding, NOT GMV, NOT a valuation of TADA — recorded in a separate row precisely so it cannot contaminate the financials** | [CoinLore](https://www.coinlore.com/coin/mvl) (~$23M, 27 Jul 2026); CryptoSlate ($24.8M, 12 Jul 2026) |
| **Stock exchange listing** | ❌ **None found.** No KOSDAQ/KRX, SGX or other listing, and no filing obligation identified, for MVL Foundation Pte. Ltd. or TADA Mobility. Korean-language searches returned funding coverage only — no KIND or DART filing. **The brief's Korean-listing hypothesis is unconfirmed.** Note the group's US arm (Zero Commission LLC) and the Korean-only `mvltaxi_driver_terms` confirm Korean roots without implying a listing | ❌ Not found |

**Business case sizing, stated honestly:** the *ride* volume is solid (~1.5–2.1M/month, derived two ways from sourced inputs). The *orchestratable pay-in* volume is the non-cash share of that, **and nobody publishes the split.** At a conservative 20% digital share that is still ~300–420k pay-ins/month; at 50% it is ~750k–1.05M. **Get the split on the call before putting a number in a deck.**

---

## Overall Research Confidence

### **MEDIUM** — downgraded one level from High, and the cause is stated.

**Why the downgrade:** **traffic data was neither supplied nor estimated.** `accounts/traffic/` holds no file for this company, nothing was pasted, and the `site:similarweb.com` fallback was deliberately not spent because TADA has no web checkout and a visit count would have been both estimate-grade and the wrong metric. Consequently **Section 1 does not exist**, the Quick Look country profile is `[ESTIMATE, not confirmed]`, the ICP row *"High traffic outside home"* scores **0 ⬜** rather than being assessed, and no rail gap in this report is traffic-weighted — the market ranking is reasoned from geofences, entities and press, which is defensible but is not measurement. Per the skill's own rule, that is a one-level downgrade. A second, smaller contributor: the method was run **single-threaded with no subagents**, so the five-way independent cross-checking the method assumes was replaced by one sequential pass plus two scans by the coordinating analyst.

**Why it is not Low — the compensating evidence is unusually strong for this account:**

| Section | Coverage | Basis |
|---|---|---|
| **3A — PSP stack** | 🟢 **Strong** | Stripe's **own customer story**, positively identified as this TADA, with named products, named architecture and three published metrics. The best class of evidence available for this question |
| **4 — Payment methods** | 🟢 **Very strong** | The merchant's **own 18-key production enum**, extracted from two independent artefacts in all nine locales. Absences are therefore meaningful, not merely unobserved |
| **2 — Legal entities** | 🟢 **Strong** | Five entities named in **first-party legal documents** across five jurisdictions, with street addresses. Weakness: **no registration number for any of them**, registries unreachable |
| **3B — Orchestrator check** | 🟢 **Strong negative** | ~1.2 MB of production JavaScript plus 16 legal documents, all negative, with the web-vs-app limit stated |
| **6 / 7 — Developments & news** | 🟢 **Strong** | PRNewswire, Fortune, NY1 (with NYC TLC regulator data), Stripe, all fetched and read in full |
| **12 — Business case** | 🟡 **Medium** | Real revenue and real cumulative volume, but **no market split and no cash/digital split** |
| **1 — Traffic** | 🔴 **None** | No data. Stated, not invented |
| **5 — Complaints** | 🔴 **Weak** | Only English-language sources; app-store review *bodies* not mined; no Khmer/Vietnamese/Thai forum search. **The clean payments record is under-tested** |
| **8 — Checkout audit** | 🟡 **Structurally limited** | Not an environment failure — **there is no web checkout to audit.** Compensated by the method catalogue and five sets of rider terms describing the mechanics in prose |
| **9 — PCI** | 🔴 **Inference only** | No PCI documentation found anywhere |
| **11 — Competitors** | 🟡 **Medium** | Strong on TAL peers, Ryde, Grab Cambodia, Uber/inDrive. **PassApp (KH), Be/Xanh SM (VN) and Maxim were not researched — budget exhausted** |

---

## Manual Research Recommendations

> **Area:** 🚨 **The cash-vs-digital ride split — the single most important unknown in this account**
> **Why it matters:** The derived 1.5–2.1M rides/month is solid, but **only the non-cash rides are pay-ins Yuno could orchestrate.** `payment_cash` is the second key in their own catalogue and cash is named in every market's rider terms; cash remains prevalent in Cambodia and Vietnam. No source publishes the split. **Every business-case number downstream depends on it**, and it is the difference between a ~300k/month and a ~1M/month opportunity.
> **Suggested manual action:** Make it the first discovery question — *"of your rides, what share is paid digitally versus cash, and how does that differ Phnom Penh versus Singapore?"* It is a flattering question (it invites them to talk about digitisation progress) and it sizes the deal.

> **Area:** 🚨 **Who acquires the eight local wallet rails — worth 3 ICP points**
> **Why it matters:** ABA Pay, Wing Pay, Pi Pay, Chip Mong Pay, MOMO Pay, MoMo, NETS QR and OCBC Digital are confirmed **methods** but no source names the processor. Stripe does not acquire in Cambodia, so these are near-certainly separate direct integrations — which would convert the "Multiple PSPs" row from **0 to +3** (taking the account to 22/29) and turn Insight #2 from an inference into a fact.
> **Suggested manual action:** Walk the rider app checkout on a Cambodian and a Vietnamese SIM behind a proxy and watch the network calls for non-Stripe payment hosts. Alternatively ask directly — it is a benign question. Secondary route: decompile the Android APK (`io.mvlchain.tada`) and grep the native bundle; the web bundle is clean but the app binary was never inspected.

> **Area:** **The KHQR participation claim for ABA / Wing / Chip Mong needs a fetchable source**
> **Why it matters:** Insight #3 and the whole Cambodia framing depend on it. `ababank.com` returned **HTTP 403** on both relevant pages, so the claim currently rests on a search summary of ABA's own site. **If this goes into an email unsourced and TADA pushes back, the whole Cambodia argument collapses.**
> **Suggested manual action:** Get it from the **National Bank of Cambodia**'s Bakong member list, or a reachable ABA/Wing/Chip Mong page, before writing. Then also pull a 2025 or 2026 Bakong/KHQR statistic — the current figures are from 2023/H1-2024 and `apac-payments.md` warns explicitly against citing stale APAC data.

> **Area:** **Registry filings and any listing**
> **Why it matters:** Registration numbers were obtained for **none** of the five entities, and **no stock-exchange listing or filing obligation was found** for MVL or TADA — so the brief's Korean-listing hypothesis is unresolved. Filings would be the only audited revenue source; everything in Section 12 is company-stated or press-reported.
> **Suggested manual action:** ACRA/BizFile for *MVL Foundation Pte. Ltd.*, *TADA Mobility (Singapore) Pte. Ltd.* and *TADA Technologies Pte. Ltd*; Thai DBD for *TADA Mobility (Thailand) Co., Ltd.*; NY Department of State for *Zero Commission LLC*. Separately, check Korea's **DART** and **KIND** directly for *easi6* and MVL — the group's Korean roots (founder Kay Woo, Korean-only `mvltaxi_driver_terms`, SV Investment and Shinhan Bank as investors) make a Korean filing plausible even though nothing surfaced.

> **Area:** **Complaint coverage is thin and the clean record is under-tested**
> **Why it matters:** "No payment complaints found" is doing real work in this report — it is why the Payment Issues row scores 0 and why Insights #1 and #2 are both framed as questions rather than accusations. But only English sources were searched, app-store review *bodies* were never mined, and Khmer/Vietnamese/Thai forums were not touched.
> **Suggested manual action:** Pull 1-star Play and App Store reviews filtered by the `km`, `vi` and `th` storefronts and search for decline/refund/charge terms. If a decline pattern exists in Cambodia or Vietnam, Insight #1 upgrades from a hypothesis to a documented pain point — and the Payment Issues row would legitimately earn +2.

> **Area:** **The payment-methods asymmetry between the terms and the app**
> **Why it matters:** The SG, KH and TH rider terms contemplate **only cash and cards**, while the app catalogue carries eight local wallet rails. Either the terms are stale (KH last modified **20/10/2020**) or some wallets are collected outside the in-app rider charge. **The answer changes what the Cambodian pay-in flow actually is**, and an email that assumes the wrong one will read as careless.
> **Suggested manual action:** Ask on the call. It is also a credible, non-salesy opener: *"your Cambodian rider terms from 2020 mention only cash and cards, but the app offers ABA Pay and Wing — are those in-app charges or collected at the car?"*

> **Area:** **The agentic payments API — the most interesting and least understood thing here**
> **Why it matters:** An API that lets AI agents *"autonomously pay for a ride without a person ever opening the app"* is live as of July 2026. Machine-initiated authorisations with no cardholder present are the hardest category to get approved, and attempting them on a single acquirer with no failover is a textbook approval-rate problem. **No technical detail whatsoever was found** — no developer docs, no API reference, no auth model.
> **Suggested manual action:** Look for `ridethroo.ai` developer documentation or an API reference; check whether the agentic flow uses stored credentials, and how MITs are flagged. Even one page would make Insight #5 concrete rather than directional.

> **Area:** **Competitors not researched**
> **Why it matters:** **PassApp** (TADA's most direct Cambodian competitor), **Be** and **Xanh SM** (Vietnam) were never researched — budget exhausted. Grab's Cambodian stack is documented in detail and is directly usable; the local challengers are not.
> **Suggested manual action:** One pass on PassApp's and Xanh SM's payment stacks. If a local Cambodian or Vietnamese competitor has shipped KHQR or VietQR, that is a far more pointed competitive-urgency line than anything currently in Section 11C.

---

## Appendix: All Source URLs

**First-party — TADA / MVL production code and configuration**
- https://tada.global/ · https://tada.global/en · https://tada.global/assets/index-BbiHo7SX.js (839,211 bytes — the payment-method catalogue, zero-commission copy, market strings, geofence/city enum)
- https://go.tada.global/ · https://go.tada.global/assets/constants-CAXCtKtj.js (region enum incl. NJ, CT) · https://go.tada.global/assets/productConfig-D7RveucL.js (TADA / COOP / THROO brand map) · https://go.tada.global/assets/index-CvZmpBc9.js (independent reproduction of the payment-method keys)
- https://policy.tada.global/ · https://policy.tada.global/assets/index-D4hJ-wRu.js (document catalogue, region→language map, geofence bounding boxes, `ET`/`ID`/`KR` regions)
- https://mvlchain.io/ (fetched, HTTP 200, not mined)
- https://ridethroo.ai/

**First-party — legal documents (`https://policy.tada.global/policies/{file}`)**
- `tada_terms_en_SG.md` (31/12/2025 — TADA Points/Hotpot addendum, §4 Payment) · `tada_privacy_en_SG.md` (20/10/2020 — SG entity + address)
- `tada_terms_en_KH.md` · `tada_privacy_en_KH.md` (both 20/10/2020) · `wallet_terms_en_KH.md` (22/01/2025) · `wallet_terms_kh_KH.md`
- `tada_terms_en_HK.md` · `tada_privacy_en_HK.md` (both 04/07/2024 — the fullest payment section, "payment collection agent", secondary-method fallback)
- `tada_terms_en_TH.md` · `tada_privacy_en_TH.md` (TH entity + Bangkok address)
- `tada_terms_vn_VN.md` (names TADA Technologies Pte. Ltd)
- `tada_driver_terms_en_SG.md` (31/12/2025) · `mvl_terms_en_SG.md` (28/05/2019 — MVL Foundation Pte. Ltd.)
- `throo_terms_en_NY.md` · `throo_privacy_en_NY.md` (01/06/2026 — Zero Commission LLC, Stripe, Driver Balance/Cashout)

**PSP / provider**
- https://stripe.com/customers/tada ⭐ · https://stripe.com/au/customers/tada · https://stripe.com/en-sg/customers/tada
- https://techcoffeehouse.com/2024/11/07/stripe-powers-tadas-southeast-asia-expansion-amid-intense-ride-hailing-competition/

**Press, financials and volume**
- https://fortune.com/2025/12/25/the-worlds-leading-blockchain-based-taxi-app-is-setting-its-sights-on-new-york-city/ ⭐ (revenue, per-ride fee, market share, launch dates)
- https://aijourn.com/throo-launches-in-new-york-city-with-lower-fares-for-riders-and-zero-commission-for-drivers/ ⭐ (PRNewswire 1 Jul 2026 — 150M rides, ~$2bn GMV, agentic API)
- https://ny1.com/nyc/all-boroughs/news/2026/08/21/new-ride-hail-app-throo-looks-to-take-on-uber--lyft-in-new-york-city ⭐ (NYC TLC data, $1 driver fee, profitability claim)
- https://www.businesswire.com/news/home/20260324338681/en/... `[403 — not fetched]`
- https://www.axios.com/local/denver/2026/09/23/throo-denver-rideshare `[403 — not fetched]`
- https://e27.co/blockchain-powered-ride-hailing-tada-officially-operates-in-cambodia-20190509/
- https://vulcanpost.com/683025/mvl-raises-us-5m-series-a-funding/ · https://media.dealstreetasia.com/stories/mvl-tada-series-a-funding-165204 · https://www.cbinsights.com/company/mvl `[search summary only]`

**App stores**
- https://apps.apple.com/sg/app/tada-ride-hailing/id1412329684 (seller MVL Foundation; 56,455 ratings; sibling apps Clutch Wallet, THROO, ONiON EV, COOP Rideshare, COOP Drivers, THROO Drivers)
- https://apps.apple.com/sg/app/tada-driver/id1414948666
- https://play.google.com/store/apps/details?id=io.mvlchain.tada (1M+; 35,816 reviews; developer TADA MOBILITY (SINGAPORE) PTE. LTD.; updated 6 Oct 2026)
- https://play.google.com/store/apps/details?id=io.mvlchain.tada.driver (1M+)

**Market / rail context**
- https://kapronasia.com/insight/blogs/payments-research/asia-payments-research/instant-payments-are-fueling-cambodias-e-commerce-boom ⭐ (KHQR 601.3M txns / US$75.8bn 2023; 3.3M+ merchants; Bakong 175.3M txns / US$54.8bn H1 2024; 19.7M e-wallet accounts; 2.4× GDP)
- https://opendevelopmentcambodia.net/news/khqr-records-400k-transactions-in-one-year/
- https://www.ababank.com/en/self-banking/aba-mobile/bakong-aba-transfers/ `[403 — not fetched]` · https://ababank.com/aba-news/aba-bank-now-supports-khqr-for-greater-convenience-of-its-qr-paymen `[403 — not fetched]`

**Complaints**
- https://mustsharenews.com/tada-my-destination/ (2 Jan 2026 — S$1.09 penalty, dispatch bug) · https://mustsharenews.com/tada-driver-2-locations/

**Competitors**
- https://www.newswire.com/news/ryde-advances-ryde-2-0-with-ai-powered-mobility-ev-fleet-technology-and-next (30 Sep 2026 — NYSE American: RYDE, "next-generation payment capabilities")
- https://b2b-cambodia.com/news/milestone-in-digital-integration-aba-and-grab-advance-cashless-ecosystem-in-cambodia (3 Sep 2025 — Grab Cambodia on ABA PayWay + ABA driver payouts)

**Token (kept separate from financials)**
- https://www.coinlore.com/coin/mvl · CryptoSlate MVL price page `[search summary only]`

**Internal**
- `accounts/apac-tal.csv` (row 632 `TADA`; peers Grab, Gojek, GoTo, Ryde, Maxim, ComfortDelGro, Rapido, Zoomcar, Bolt.Earth, Namma Yatri, Odisha Yatri, Lalamove, Pathao)
- `.claude/reference/apac-payments.md` (§2 market rails; §3 cross-border framing; §4 displacement motion; §5 vertical notes)
- `.claude/commands/full-outreach.md` (Yuno success-case library; customer-naming rules; inDrive metrics L521; travel/mobility list L530; site-wide list L543–545)
- `.claude/reference/subscription-payments.md` — **consulted and found not applicable.** No recurring model exists in this account; the `/rentals` beta is the only candidate and no billing detail was found

</details>
