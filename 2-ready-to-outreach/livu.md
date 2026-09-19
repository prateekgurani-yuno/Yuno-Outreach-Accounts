# LivU (莱熙)

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 11 / 29 → 🟢 **Medium**
**Industry:** Live random video chat / social discovery (consumer, coin-based virtual currency + recurring subscription) · **HQ:** Hong Kong — **Clash Arts (HK) Limited**, Hopewell Centre, Wanchai · **Researched:** 2026-09-17 · **First email sent:** —
**Motion:** **In-house orchestration** — a self-built routing and reconciliation layer over **five acquirers** on their own gateway. Classification is affirmative, from their own production bundle (see 3B). Respect the build; anchor on opportunity cost and reach, never "you need orchestration".

---

> ## 🎯 THE HOOK — Apple is gone, and three of their own artefacts haven't noticed
>
> **LivU is not on the Apple App Store.** I verified this myself, four ways:
>
> - `https://apps.apple.com/hk/app/livu-live-video-chat/id1273950116` → **HTTP 404**
> - `https://itunes.apple.com/lookup?id=1273950116` → `"resultCount": 0` — and **0 across all eight storefronts I checked**: us, hk, tr, id, ph, in, sg, br
> - **Their own production config still links to a dead store page.** `window.baseConfig` on `livuchat.com/payment` carries `"iosDownload": "https://itunes.apple.com/cn/app/livu-…/id1273950116?mt=8"` — I followed it: **404**
> - **Their own corporate site still markets the ranking.** `rileycillian.com/products.html`, live today: *"Ranked #1 Lifestyle App on **Apple App Store** in 94 countries since 2017"*
>
> And their Terms of Service, still published, still says: *"**We work with Google and Apple** to ensure that any payments and refunds are managed effectively."*
>
> **Three independent artefacts — marketing site, legal terms, production JavaScript — all still assume an Apple rail that no longer exists.** Whatever share of revenue Apple carried has been forced onto their web till and a reseller rail, and nothing in their published stack has been updated to reflect it.
>
> **The second hook is in the same bundle:** `enableCheckoutV2` plus two live Checkout.com keys. They are hand-migrating an acquirer integration **right now**.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** LivU is a live random video-chat app under the **Riley Cillian** group (Hong Kong, founded 2014), monetised through **coins** — bought in-app, on a **first-party web top-up store at `livuchat.com/payment`**, and through a **Coda Payments / Codashop reseller rail**. **69,952,626 Google Play installs.** The account list's *"billed largely through Apple and Google"* is **refuted on both halves** — Apple is delisted entirely, and Google is now one of three rails, with the company actively pushing users off-store via emailed discount links.

**SimilarWeb (livuchat.com):** ~310.1K visits / 3 months (~103K/month) — Turkey **45.55%**, US 13.57%, Brazil 12.03%, France 6.17%, UK 5.16%. Top channel **Mail 55.61%**. `[ESTIMATE, not confirmed]` — SimilarWeb modelled data, surfaced by the research agent. **I could not re-fetch it: `similarweb.com` returned a 202 challenge to my own curl.** Treat as second-hand.

> ⚠️ **This is the web *till*, not the business.** LivU is app-first; `livuchat.com` is reached mainly by emailed and in-app-inbox discount links. Play IAP, Codashop, carrier billing and reseller volume appear nowhere in it. **Read the country mix as web-checkout mix, never revenue mix.**

### Markets
| Surface | Markets | Evidence |
|---|---|---|
| **Web till** (`livuchat.com`) | Turkey 45.55%, US 13.57%, Brazil 12.03%, France 6.17%, UK 5.16% | SimilarWeb `[EST]` — **agent-sourced, not re-verified** |
| **Codashop reseller** — APAC rails, historical localised storefronts | **Indonesia:** DANA, QRIS, ShopeePay, OVO, LinkAja, DOKU, bank transfer, cards · **Malaysia:** MAE, Touch 'n Go, FPX, ShopeePay, GrabPay, Boost, cards · **Philippines:** Globe/TM + Smart/TNT carrier billing, GCash, GrabPay, 7-Eleven, OTC, bank transfer, cards · **Thailand:** storefront existed, methods not captured | Wayback snapshots, URLs in Section 4 |
| **Group self-declared availability** | 100+ countries, list names **Australia, Japan, South Korea, Philippines, China, Malaysia, Indonesia, Sri Lanka, India, Pakistan** — and also UAE, Saudi, Turkey, Israel, Egypt and most of Western Europe | `https://www.rileycillian.com/` — **I fetched this myself** |

### Legal entities
- **Clash Arts (HK) Limited** — the contracting entity. ToS §1.1, verbatim: *"When we refer to 'Riley Cillian Group,' 'LivU,' 'we,' 'us,' or 'our' in these Terms, we mean **Clash Arts (HK) Limited** and its affiliates, including **Riley Cillian Ireland Limited**."* Registered office **Suite 3705, Hopewell Centre, 183 Queen's Road East, Wanchai, HK**
- **Google Play developer of record:** *Clash Arts HK Limited* (display name "LIVU Team"), `Rm 3705A HOPEWELL CTR, 183 QUEEN'S RD E, 灣仔, 香港島, Hong Kong`, `+852 8494 0920` — **I read this off the live Play listing**
- **Riley Cillian Ireland Limited** — EU/GDPR entity, Dublin 2
- ⚠️ **Three geography-split merchant-of-record shells**, ToS §7.8 verbatim: *"(i) **Harvest Green Limited** if you are based in the EU… (ii) **Baker Street Digital Technology Service Limited** if you are based in the UK… (iii) **GoQun Limited** if you are based in the **rest of the world**"* — **GoQun is the APAC-facing payment counterparty.** None of the three traced to a registry.
- **China nexus:** privacy policy — *"Our network includes servers in the EU, and personal information may also be processed in **Hong Kong and China**."*

### Known PSPs — five acquirers, all from live production config
- **Stripe** — `"stripeKey":"pk_live_51IiHKHIgpLjV5WPq…"` (live-mode key)
- **Checkout.com** — `"checkoutKey":"pk_031a1e51-798f-487e-a659-b1f92036066c"` **and** `"checkoutKeyV2":"pk_ax77p4mgbtjqy27c6twfcsyevi"`, gated by an `enableCheckoutV2` flag
- **dLocal** — `"dlocalPublicKey":"a9857ed7-a771-4e06-a5ad-6cb6b489c589"`, `"dlocalRedirect":"https://proxyweb.livuchat.com"`
- **PayerMax** — `payCompanyCode === "payermax"` in `app.8cde0939a4f4c8a3f610.js`
- **Airwallex** — `payCompanyCode === "airwallex"` in the same bundle
- **Coda Payments** — the Codashop rail, cited by LivU's own help centre
- **Forter** (fraud) — `"forterSiteId":"907fd01d633b"`; the code reads `ext.forterData.payment[0].creditCard.cardBank`
- **TrustDecision** (device fingerprinting) — `static.trustdecision.com/tdfp/de/49a1070ee5594f34b3bc8027e40f5bd9/fm.js`
- ❌ **Searched and not found:** Adyen, Braintree, Xsolla, PayPal (first-party), PingPong, Lianlian, Oceanpayment

### Orchestration status
**In-house orchestration layer.** Zero hits against Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY, Yuno. What exists instead is a bespoke build on their own gateway — `"gatewayApi":"https://portal.rcplatformhk.com"` — with an acquirer-routing key, a reconciliation service and a country-keyed method catalogue. Full endpoint inventory in 3B.

### Buying signals
- 💥 **Delisted from Apple.** Verified across eight storefronts. Whatever Apple carried now has to run through rails that were built as the secondary path.
- 🔄 **`enableCheckoutV2` — an acquirer re-integration in flight today.** Two live Checkout.com keys, a feature flag, and a `localStorage.removeItem("enableCheckoutV2")` kill switch. Someone is hand-rolling a migration.
- 🔁 **Recurring card-on-file billing on their own till** — weekly and monthly coin subscriptions, plus a stored-card vault. See 3B. This is the involuntary-churn conversation, and none of it is app-store revenue.
- 🧩 **ONE payment estate across the brand portfolio — now proven, not inferred.** See the dedicated estate section below. **Tumile runs its own till on its own domain and it is wired into LivU's own payment infrastructure**, down to a byte-identical fraud partition ID. **One integration change propagates across every brand.**
- 📦 **Sibling apps expand the deal** — **Tumile** (verified same estate) and **Yaar**, which Riley Cillian describes as *"an Android Application Package (APK) available for **direct download only**"* — i.e. **100% off-store billing by construction**.
- 🌏 **Reseller rail proves APAC local-method demand** — they built ID/MY/PH/TH Codashop storefronts rather than serve those rails first-party.
- ❌ **No funding round, no payments job posting, no public RFP found.**


### 🏗️ THE PROPERTY ESTATE — deep research, 2026-09-19

**Question asked:** map every app and domain in the group and establish each one's payment stack, hunting for divergence.
**Answer: they diverge at the brand layer and converge completely at the payment layer. It is one estate.**

#### ✅ VERIFIED BY ME DIRECTLY — LivU and Tumile are one payment system

I fetched both tills and both bundle sets and diffed them. `www.tumile.me/payment` and `www.livuchat.com/payment` are separate builds — different app-bundle hashes (`app.6c48d5a6…` vs `app.8cde0939…`), a Tumile-specific `tumilemanifest.js`, and no redirect between them.

**And yet Tumile's own payment page declares LivU's payment infrastructure:**

| Host declared on BOTH tills | What it is |
|---|---|
| `portal.rcplatformhk.com` | the group gateway |
| `api.livuchat.com` | **LivU-branded API host** |
| `proxyweb.livuchat.com` | **the dLocal redirect** (established in 3B) |
| `h5.livuchat.com` | **LivU-branded CDN origin** |

**Tumile's till routes through hosts branded `livuchat.com`.** The only hosts that differ between the two pages are the policy pages — `privacy.`/`safety.tumile.me` versus `privacy.`/`safety.livuchat.com`.

**Inside the bundles, the payment layer is character-for-character identical:**
- Same gateway endpoints: `gatewayApi+"/plutus-order-service/api/1/orders"`, `…/1/subscriptions`, `…/plutus-user-sync/api/users/1/`, `gatewayApi2+"/facade/api/switch/asyncConfig"`
- Same acquirer routing primitives: `payermax`, `airwallex`, `checkout`, plus `thirdPaymentRecon`
- Same logging host `rclog.rcplatformhk.com`
- **The same TrustDecision fraud partition ID — `tdfp/de/49a1070ee5594f34b3bc8027e40f5bd9` — byte-identical on both pages**
- **`Vivah` appears in BOTH app bundles**, confirming the white-label rebrand is shared code, not LivU-specific
- **Both vendor bundles are exactly 523,428 bytes** — same source, different build config
- `appId: baseConfig.appType` is threaded through every API call — **the properties are tenants on one codebase, multiplexed by appId**

> 📌 **THIS IS THE COMMERCIAL POINT.** A deal here is not one app. **The payment path is a single shared system and every brand is a tenant on it** — so one integration lands the whole portfolio, and conversely every brand inherits the same acquirer set, the same fraud vendor and the same five-acquirer routing decision. **Lead with this.**

#### ⚠️ WHAT THE RESEARCH CLAIMED THAT ITS OWN VERIFICATION PANEL KILLED

The run's headline summary asserts a wider estate — *"Mixu, Solla Chat, Livcam and 1v1chat.me… operated through a second Hong Kong shell, Mastercroff Developer Limited."* **Its own adversarial verification refuted much of that: 16 of 25 claims were killed.** Do not repeat the summary.

| Claim | Verdict |
|---|---|
| **Solla Chat belongs to this group** | 🔴 **REFUTED 0–3.** Attributed by shared CDN and runtime only, never by developer of record. The panel called it an **app-name/category collision candidate**. |
| **Mixu belongs to this group** | 🔴 **Refused.** Its actual Play developer of record is **Breaking Barriers Now B.V., a Dutch entity**, which the panel unanimously declined to treat as group-owned — despite `mixu.rcplatformhk.com` existing on the group's gateway domain. |
| **Mastercroff's Suite 3705A proves common control with Clash Arts' Suite 3705** | 🔴 **Refuted.** Address adjacency in a Hong Kong office tower is suggestive of a shared corporate-services provider, **not proof of common control.** |
| **Solla runs a divergent gateway (`api.mastercroff.com`)** | 🟡 **1–2, not confirmed.** And it only matters if Solla is group-owned, which is refuted. |
| **The corporate site lists exactly three products (sourced absence)** | 🔴 **Refuted 0–3.** |
| **The Apple delisting spans every Apple platform type** | 🔴 **Refuted 0–3.** |

**What survives on the estate question: LivU, Tumile and Yaar.** Tumile and LivU are attributed to **Clash Arts (HK) Limited by the company's own GDPR disclosures**, which is the strongest evidence class available here. **Everything beyond those three is infrastructure adjacency, not ownership.**

#### 🍎 The Apple delisting — scope tightened
✅ **Proven account-wide for Apple developer `id1273950115` = CLASH ARTS HK LIMITED** (alternate display name *LIVU Team*, app *LivU* `id1273950116`): the developer page returns HTTP 200 with an **empty rendered shelf and an empty schema.org offer catalogue**, and **Apple's independent iTunes lookup API returns the artist record with zero software entries.**

⚠️ **But that is the whole of it.** **No sibling Apple developer account was ever searched**, so the absence of Tumile, Yaar or anything else from the App Store is **unchecked, not sourced**. **And no cause, no date and no policy-violation record was found at all — never assert a reason in outreach.**

#### 🏢 The merchant-of-record shells — still untraced, and that is itself the finding
**Harvest Green Limited** (EU), **Baker Street Digital Technology Service Limited** (UK), **GoQun Limited** (rest of world) and the newly-surfaced **Mastercroff Developer Limited** were **not found in the Hong Kong Companies Registry, UK Companies House, the Irish CRO, ACRA or BVI.** All that exists are self-published website footers — **three of which share one site template and one suite number.**

> **Four billing entities that bill real consumers and appear in no registry anyone can reach.** That is worth understanding before a commercial conversation, and it is a reason to expect the payments owner to be unusually senior.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach LivU` to draft the 12-touch sequence — **after settling the territory question in Section 3**, and note that the **subscription fork applies** (`.claude/reference/subscription-payments.md`): this is recurring card-on-file billing, not one-off top-ups only.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 11 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+2** | ⚠️ **NOT FOUND — ASSUMED ~40,000–50,000/month orchestrable.** `[ASSUMPTION — not researched.]` **No LivU transaction count, TPV, ARPU or paying-user figure exists publicly.** **Basis:** the web till draws ~103K visits/month `[EST]` and is an intent-heavy destination reached by emailed discount links, so it converts far above retail norms — a 25–40% conversion implies ~26–41K web transactions/month, plus an unmeasured Codashop volume on top. **Billing unit counted: web till + reseller top-ups — i.e. the *orchestrable* transactions.** Google Play IAP is excluded because Yuno cannot touch it; including it, total transactions are plausibly ≥100,000/month. **Scored on the conservative orchestrable band.** Per the disclosure rule, an assumption **cannot** fire the under-40k rejection, and this one does not. **"Confirm monthly transaction count" is item 1 in Manual Research Recommendations.** |
| Orchestration status | **+1** | ✅ **In-house layer, affirmatively evidenced** — own gateway domain, own `payCompanyCode` acquirer-routing key, own recon service. Not a failed search. |
| 3+ countries | **+3** | ✅ Five countries >1% on the web till; **three-plus legal entities** (Clash Arts HK, Riley Cillian Ireland, and three MoR shells). |
| Multiple PSPs | **+3** | ✅ **Five acquirers** — Stripe, Checkout.com, dLocal, PayerMax, Airwallex — plus Coda Payments as a reseller rail and two fraud vendors. All first-party sourced from live config. |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **Not scorable — unknown, not absent.** The top-3 web markets are **Turkey, US and Brazil**, none of them APAC, so the rail-gap rule cannot fire on them. And the first-party store's method catalogue is **server-driven and session-gated** — `findCountryPaymentMethod`, `queryCountryList` and `getCoinAndChannel` all return the SPA shell unauthenticated, so I cannot source the absence of QRIS/GCash/UPI/PayNow on the till. **Scoring 0 rather than inventing an absence.** |
| Recent expansion | **0** | ❌ The last 12 months show **contraction**, not expansion: Apple delisting, plus Coda consolidating LivU's country storefronts onto `/international/`. |
| Payment issues reported | **0** | ⬜ No complaint corpus established. The help centre carries a routine *"didn't receive coins after recharging"* article, which is standard coverage, not evidence of frequency. No Reddit or Trustpilot payment-failure body found. |
| Funding >$10M | **0** | ❌ No round found. Privately held. |
| High traffic outside home | **+2** | ✅ **Hong Kong — the HQ — does not appear in the top 5 web markets at all.** Home share is far below 60%. |
| Competitor using orchestration | **0** | ❌ None confirmed. |
| Payment job postings | **0** | ⬜ None found. |

**Tier:** **11 / 29 → 🟢 Medium.** No analyst override applied.

> **Why no override, in either direction.**
> **Not scored down:** the app-store trap is the usual killer in this vertical, and here it is **refuted** — Apple contributes nothing and Google is one of three rails. That is the opposite of the disqualifying case.
> **Not scored up either, and I want to be straight about the temptation.** The qualitative picture — five acquirers, a hand-built router, recurring card-on-file, an in-flight migration, a white-labelled portfolio — reads stronger than 11 points. But two of the three things that would make it a ⭐ are **unproven, not proven**: orchestrable volume is assumed, and APAC revenue centrality is unevidenced. Scoring on what I'd like to be true is exactly the error this matrix exists to prevent.
> **What would move it to ⭐:** (a) a sourced orchestrable transaction count ≥100,000/month (+3 over current), and (b) a top-3 market inside APAC with a sourced rail gap (+3). Either one alone lands 14; both land 17.
> **Note the matrix is structurally harsh here.** In-house scores +1 because it is the hardest sell — but in this case the build *is* the pitch, and its cost is unusually visible.

---

### ⚠️ TERRITORY — settle before outreach

| Factor | Points to |
|---|---|
| Contracting entity: **Clash Arts (HK) Limited**, Wanchai | **APAC** ✅ |
| Google Play developer of record: **Hong Kong** | **APAC** ✅ |
| Group HQ and infrastructure: **`rcplatformhk.com`** | **APAC** ✅ |
| APAC MoR shell: **GoQun Limited** ("rest of world") | **APAC** ✅ |
| Localised reseller rails built for **ID / MY / PH / TH** | **APAC** ✅ |
| **Web till skews Turkey 45.55%, US 13.57%, Brazil 12.03%** | **EMEA / AMER / LatAm** ❌ |
| Group's own market list includes **UAE and Saudi** | **EMEA** ❌ |

**My read: in territory, and it is Prateek's account** — HQ, contracting entity, developer of record and APAC MoR all sit east of Dubai, and the rule is HQ-based. **But the revenue centre is genuinely unproven.** APAC monetisation is real and evidenced (four localised Codashop storefronts, `PayTM` strings in the bundle, the market list), yet the only traffic data available points at Turkey, the US and Brazil. **Worth a note to EMEA and LatAm before a sequence goes out** — not because the account belongs to them, but because Turkey at 45% of the web till is their conversation to have, and Brazil at 12% overlaps the Pix/IOF work already done on YesStyle.

---

### Section 1: Website Traffic Analysis by Country

**Resolution:** no SimilarWeb data supplied by Prateek, no MCP tools configured. The figures below came from the research agent's SimilarWeb read. **I attempted to re-fetch `https://www.similarweb.com/website/livuchat.com/` myself and got HTTP 202 with a zero-byte body — a WAF challenge.** So this is the one material block of data in this file I have *not* personally verified, and it is labelled accordingly throughout.

| Rank | Country | Web-till share `[EST]` | Region |
|---|---|---|---|
| 1 | **Turkey** | **45.55%** | EMEA |
| 2 | United States | 13.57% | AMER |
| 3 | Brazil | 12.03% | LatAm |
| 4 | France | 6.17% | EMEA |
| 5 | United Kingdom | 5.16% | EMEA |
| — | Other | 17.52% | — |

~310.1K visits over three months (~103K/month). **Top channel: Mail 55.61%** — i.e. the till is fed by emailed discount campaigns, consistent with ToS §7.8's *"personalized pricing, that may be dependent on your location or the **payment channel** that you use."* They are paying users to leave the app store.

**App-level, verified by me from the live Play listing** (`play.google.com/store/apps/details?id=com.videochat.livu`):
- **69,952,626 installs** — this is Google's underlying figure inside the page data, not the rounded "50M+" bucket shown to users
- Released **28 July 2017**; last updated **25 August 2026** (actively maintained)
- **4.32 stars, 421,642 ratings, 3,323 written reviews**
- **In-app purchase range: `$0.10 – $253.70 per item`**

> 📌 **Correction to the research agent.** The agent declined to attribute any IAP price band to LivU, reasoning that the `per item` strings on the Play page belong to the "similar apps" section. That caution was right in principle and wrong here: there are **seven** `per item` strings in the page, and **six share an identical structural prefix** (`[2],null,[1,1,0],["…"`) marking them as neighbour-app blocks. The seventh — `$0.10 – $253.70` — sits in a different structure, **immediately between LivU's own install count and its own developer name `["LIVU Team"]`**. It is LivU's. The `$0.10` floor also makes it unique among the seven, which is corroborating rather than coincidental.

**Why the $0.10 floor matters commercially:** a ten-cent minimum item means genuine micro-transactions. Low ticket size is the worst case for fixed-fee-heavy cross-border card economics — the per-transaction component dominates — and it inflates transaction *count* relative to revenue. That is a cost-of-acceptance argument, not a conversion one.

---

### Section 2: Legal Entities & Local Presence

Covered in Quick Look. Additional detail:

- ToS §7.8 names the three procurement companies as the contact of record *"for any payment queries, issues and payment support"* — a **geography-split merchant-of-record chain**, with **GoQun Limited** covering "the rest of the world", which includes all of APAC.
- ❌ **I could not trace GoQun Limited, Harvest Green Limited or Baker Street Digital Technology Service Limited to any registry.** Jurisdictions unverified. Flagged, not guessed.
- Group brand **Riley Cillian** — `rileycillian.com`, footer *"Copyright 2025"*. Infrastructure under `rcplatformhk.com` (`api.`, `wchat.`, `portal.`); app IDs prefixed `RCPlatform_pf_…`.
- **Entity gap against APAC markets:** the group advertises availability in Japan, South Korea, India, Indonesia, Malaysia, Philippines, Australia and mainland China, with **no confirmed operating entity in any of them**. Korea and China gate domestic acquiring behind local presence entirely; India and Indonesia effectively so. Per `.claude/reference/apac-payments.md`, that is the strongest available framing if APAC volume is confirmed — *the local rail is not reachable at all*, not merely expensive.

---

### Section 3: Payment Providers & Payment Stack

#### 3A — Confirmed PSPs

All extracted by me from `https://www.livuchat.com/payment` (HTTP 200) and its bundle `https://www.livuchat.com/static/js/app.8cde0939a4f4c8a3f610.js` (HTTP 200, 135,208 bytes) on 2026-09-17.

| Provider | Evidence | Where it sits |
|---|---|---|
| **Stripe** | `"stripeKey":"pk_live_51IiHKHIgpLjV5WPq…"` in `window.baseConfig` — **live mode** | First-party till |
| **Checkout.com** | `"checkoutKey":"pk_031a1e51-…"`, `"checkoutKeyV2":"pk_ax77p4mgbtjqy27c6twfcsyevi"`, `enableCheckoutV2` flag, `payCompanyCode === "checkout"` | First-party till — **migration in flight** |
| **dLocal** | `"dlocalPublicKey":"a9857ed7-…"`, `"dlocalRedirect":"https://proxyweb.livuchat.com"` | Emerging markets — consistent with the Brazil/Turkey traffic |
| **PayerMax** | `payCompanyCode === "payermax"` in the bundle's Apple Pay eligibility branch | Acquirer in the routing table |
| **Airwallex** | `payCompanyCode === "airwallex"` in the same branch | Acquirer in the routing table |
| **Coda Payments** | Codashop rail, cited by LivU's own help centre (Section 4) | Reseller / local methods |
| **Forter** | `"forterSiteId":"907fd01d633b"`; code path `x.ext.forterData.payment[0].creditCard.cardBank` | Fraud decisioning |
| **TrustDecision** | `static.trustdecision.com/tdfp/de/49a1070ee5594f34b3bc8027e40f5bd9/fm.js` | Device fingerprinting |

> ⚠️ **Precision on PayerMax and Airwallex, because it matters.** My own earlier extraction from `livuapp.com` / `p.livuapp.com` showed only Checkout.com, dLocal, Stripe and Forter — **not** PayerMax or Airwallex. I resolved the discrepancy by fetching the `livuchat.com` bundle directly. Both names appear exactly once each, and **both appear inside the same Apple Pay browser-eligibility branch**, alongside `"checkout"`, as values of `payCompanyCode`. That is real evidence they are acquirers in the routing table — the client would not branch on them otherwise — but note precisely what it proves: **they are acquirers that can serve the `APPLEPAY` channel**. It does **not** prove which countries or methods they carry. The live catalogue is server-side.
>
> A `PayTMAccount` / `PayTMPhone` i18n string pair also exists in the bundle, implying **Paytm (India)** on the first-party till. **Not confirmed live** — do not assert it.

#### 3B — Orchestrator check → **IN-HOUSE**

Searched Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY, Yuno and "payment orchestration" — **nothing**. The TAL's `Payment Orchestrator` column is empty and stays empty.

What they built instead, every item below read by me out of the live bundle:

- **Own gateway:** `"gatewayApi":"https://portal.rcplatformhk.com"` — their domain, not a vendor's
- **Own acquirer-routing key:** every payment-method object carries `payCompanyCode` (`payermax` / `airwallex` / `checkout`) and `thirdPaymentChannelCode` (`APPLEPAY`, `CARD`)
- **Named internal microservices:** `plutus-order-service/api/1/orders`, `plutus-order-service/api/1/subscriptions`, `plutus-user-sync`
- **Sixteen own orchestration endpoints:**
  `thirdPayment/1/placeOrder` · `thirdPayment/1/createPaymentSession` · `thirdPayment/1/applyDropinSession` · `thirdPayment/1/getCustomerInfo` · `thirdPayment/1/getOrderById` · `thirdPaymentRecon/1/queryChannelByCoin` · `thirdPaymentRecon/1/findChannelByCountry` · `thirdPaymentRecon/paymentMethod/1/findCountryPaymentMethod` · `thirdPaymentRecon/1/getCoinAndChannel` · `thirdPaymentRecon/1/flash/seal/getCoinAndChannel` · `thirdPaymentRecon/1/getOrderListByUserId` · `thirdPaymentRecon/1/getPayExtParams` · `thirdPaymentRecon/1/queryCountryList` · `thirdPaymentRecon/1/queryCountryListHot` · `thirdPaymentRecon/1/channelexts/channel` · `thirdPaymentRecon/activity/getActivityByCountry`
- **Hand-rolled per-PSP wallet eligibility** — the Apple Pay browser/platform check is written out **separately for payermax, airwallex and checkout**. Three near-identical branches doing the same job, one per acquirer. That is the maintenance tax made visible.

> 📌 **`thirdPaymentRecon` is a reconciliation service they wrote themselves**, with a country-keyed method catalogue, a per-coin channel lookup and a per-country promotion service hanging off it. **That is not "integrating a few PSPs" — that is an orchestration product with an internal customer.**
>
> I tried `portal.rcplatformhk.com/thirdPaymentRecon/1/queryCountryList` unauthenticated: `{"error_msg":"404 Route Not Found"}`. The catalogue is gated, so the per-country method map stays unknown.

#### 3C — Recurring billing and card vault ⭐ **not in the agent report — found in my own read of the bundle**

The till is **not** one-off top-ups only. Verbatim i18n strings from `app.8cde0939a4f4c8a3f610.js`:

> `subscribeCoins: "Subscribe coins package"`
> `subscribeTips: "Subscription will automatically charge you"`
> `weekly: "weekly"`, `monthly: "monthly"`
> `subscribedTime: "Subscription will be renewed at {time}"`
> `subscribeAutomatically: "Your subscription will be automatically charged"`
> `cancelMonthlyTips: "Cancelling the subscription will be effective next month…"`
> `subscribedTips: "You are currently subscribed to the coins package, you cannot subscribe again."`
> `mySubscription`, `cancelSubscription`, `purchaseCategory`, `orderHistory`

Backed by real endpoints: `GET plutus-order-service/api/1/subscriptions?userId=…` and `POST subscriptions/{id}/cancel`.

And a **stored-card vault**: `GET {userCard}/{userId}/cardList`, with front-end routes `/cardList` and a card-add view, plus `usersync/api/users/1/`. There is also a post-auth step — `POST {authenticate}/{orderId}/authenticate` with an `authCode` — consistent with a server-driven challenge flow.

**Why this is the most important paragraph in the file.** A **weekly/monthly recurring card-on-file subscription**, billed cross-border out of Hong Kong to a global user base, through a high-risk-adjacent MCC, routed by hand across five acquirers, with **no Apple rail to fall back on**. Involuntary churn, retry strategy, network tokens and account updater are live problems here, and — unlike every other app in this category — **none of that revenue is locked inside a store**. It is all addressable.

Tiering exists too (`free` / `vipc` / `vipb` / `vipa` / `svip`), so there is a subscription ladder, not a single SKU.

#### 3D — One front-end, several brands

The same bundle rebrands itself: when `appType` is not `20000`, it sets `appName = "Vivah"` and swaps in `Vivah_termsofservice.html` / `Vivah_privacy.html`. LivU's own config also carries `"callbackDomain":"https://www.tumile.me"`. **One payment web app, white-labelled across the group's brands** — which means the integration surface Yuno would replace is shared, and a single change propagates to all of them. Deal-size argument, and a reason the in-house build is stickier than it looks.

#### 3E — PCI DSS
**No public statement found.** They collect card details directly (privacy policy: *"To take payments for premium services. (This does not apply if you make payments via the Apple App Store.) **Payment card details.**"*) and operate a card vault, so scope is real, but no level or AoC is published.

---

### Section 4: Alternative & Local Payment Methods

#### First-party till (`livuchat.com/payment`) — **method list NOT established**
Server-driven and login-gated (`loginToken`; error path *"please login again"*). `findCountryPaymentMethod`, `queryCountryList` and `getCoinAndChannel` all return the SPA shell or 404 unauthenticated. **No APAC local method is either confirmed or sourced-absent on the first-party store.** Do not claim a gap here — this is unchecked absence, not sourced absence.

#### Reseller rail (Codashop) — **APAC local methods CONFIRMED**
LivU's own help centre, verbatim (`https://support.livu.me/hc/en-us/articles/1500005189081-How-can-I-buy-coins`, pulled by me via the open Zendesk API — all 46 articles, HTTP 200, 84,889 bytes):

> *"You can purchase coins the following ways: **Website Recharge link: https://www.livuchat.com/payment** · **Fast Recharge link: https://www.codashop.com/international** （Available for Africa, Americas, Middle East, **Southeast Asia, South Asia**, other)."*

And again, twice more:
> *"You can find our offers for a coin deal on **LivU website recharge platform: https://www.livuchat.com/payment**"* — `…/12151039160599-How-to-Get-Deals-and-Discounts` and `…/4407470686487-What-is-the-pricing-of-coins`

| Market | Methods | Source |
|---|---|---|
| **Indonesia** | **DANA, QRIS**, bank transfer, **ShopeePay, OVO**, credit card, **LinkAja, DOKU Wallet** | `https://web.archive.org/web/20260517115330id_/https://www.codashop.com/id-id/livu` (snapshot 2026-05-17) |
| **Malaysia** | **MAE, Touch 'n Go, FPX, ShopeePay, GrabPay, Boost**, card | `https://web.archive.org/web/20260121183624id_/https://www.codashop.com/en-my/livu` (2026-01-21) |
| **Philippines** | **Globe/TM and Smart/TNT carrier billing, GCash, GrabPay**, bank transfer, OTC, **7-Eleven**, card | `https://web.archive.org/web/20220728132251id_/https://www.codashop.com/en-ph/livu` |
| **Thailand** | Storefront existed (*"LivU (Thailand) - Codashop"*); **method list not captured** — archive served a mismatched asset | — |

⚠️ **Current state, stated honestly.** All country-specific Codashop LivU slugs now 404 (`id-id/livu`, `en-my/livu`, `en-ph/livu`, `th-th/livu`, `en-in/livu`) while game titles on the same storefronts still resolve. LivU, sibling **Tumile**, and competitors **MICO** and **Chamet** are *all* now reachable only under `/international/`. **I verified `https://www.codashop.com/international/livu` returns HTTP 200 today.** This reads as Coda consolidating the live-video-chat category, not as LivU being dropped — but **which local methods survive on `/international/` is unconfirmed**.

**The strategic point stands regardless:** LivU needed DANA, QRIS, GCash, FPX, Touch 'n Go and Philippine carrier billing badly enough to route them through a third-party reseller — paying a reseller margin and losing the customer relationship, the order data and the retry control — rather than serve them on its own checkout. That is the classic "one integration, every method" case, and it is evidenced by their own help centre rather than asserted.

Third-party grey-market UID resellers (TOPUPLive, LootBar, GamsGo, Z2U, Enjoygm, BuffBuff, apptopup, jubaly, 94lives) also carry LivU coins — `[UNVERIFIED — search summary only, pages not fetched]`.

---

### Section 5: Payment Issues & Customer Complaints

**No complaint corpus established.** The help centre carries a routine *"What can I do if I don't receive any coins after recharging?"* article, which is standard coverage rather than evidence of frequency — though it does confirm a first-party order ledger: web orders get their own **19-digit Order ID beginning with "O"** and an order history, so these are their own transactions, not store passthroughs.

Play Store rating is **4.32 across 421,642 ratings** — healthy, and not a distress signal. **Scored 0. Do not claim payment complaints in outreach.**

---

### Section 6: Corporate & Payment Strategy Developments

- **Apple App Store delisting** — date and reason **unknown**. This is the single highest-value open question: it decides whether web billing is a permanent structural necessity or a temporary workaround. Their marketing, ToS and production config all still assume Apple, which suggests it is recent and unaccommodated.
- **Checkout.com v2 migration in flight** — `enableCheckoutV2`, two live keys, a localStorage kill switch.
- **Codashop storefront consolidation** onto `/international/`, category-wide.
- **Play listing last updated 25 August 2026** — active development.
- ❌ No funding round, no acquisition, no payments job posting, no licence application, no public RFP found.

---

### Section 7: Payment-Specific News
**No public information found.** No coverage in thepaypers, finextra, pymnts, techinasia or e27 tying LivU to any payment provider or programme.

---

### Section 8: Checkout Experience Audit

Partially completed — I fetched the till directly.

| Attribute | Finding |
|---|---|
| URL | `https://www.livuchat.com/payment` — HTTP 200 |
| Type | SPA (Vue), **login-gated**; top-up is UID-linked, not guest checkout |
| Method list | **Server-driven** per country; not visible unauthenticated |
| Card storage | **Yes** — vault with `/cardList` route and card-add view |
| Recurring | **Yes** — weekly and monthly coin subscriptions with self-serve cancel |
| Wallets | Apple Pay eligibility computed client-side, **per acquirer**, gated on Safari + mobile |
| 3DS | **Not established.** No `3ds` / `threeDS` string in the bundle; there *is* an `authenticate/{orderId}` step with an `authCode`, which is consistent with a server-side challenge but does not prove 3DS. **Unchecked absence — do not assert "no 3DS".** |
| Fraud | **Forter** (reads card BIN/bank) + **TrustDecision** fingerprint script, fires on page load |
| Support | Zendesk widget embedded (`static.zdassets.com/ekr/snippet.js`) |
| Analytics | GTM `GTM-NKD6R7T`, UA-141921283-1, Kochava `kolovu-web-z0xc20at`, Facebook app ID |

---

### Section 9: PCI DSS Compliance
See 3E. **No public statement found.**

---

### Section 10: Strategic Insights & Outreach Angles

**Motion: In-house.** They made a deliberate build decision and executed it properly. The rulebook is explicit — respect it, anchor on **opportunity cost and reach**, never on the build being wrong.

Ranked angles:

1. **The Apple hole.** They have already been forced off one rail, and their web and reseller paths now carry weight they were not designed for. Every artefact they publish still assumes Apple. *Observation, not accusation* — and it is impossible to dispute, because it is their own 404.
2. **Three Apple Pay branches, one per acquirer.** The clearest possible illustration of in-house cost: the same eligibility logic written three times because there are three acquirers. Add a fourth and it gets written a fourth time. **This is an asymmetry inside their own stack** — the strongest move in the sample set — and neither half is arguable.
3. **`enableCheckoutV2` right now.** They are paying to re-integrate an acquirer by hand today. Timing is rarely this good.
4. **Local rails outsourced to a reseller.** They pay Coda a margin, and lose the order relationship and retry control, to reach DANA, QRIS, GCash, FPX and Philippine carrier billing. That is the reach argument, evidenced by their own help centre.
5. **Recurring card-on-file with no store fallback.** Weekly/monthly subscriptions, a card vault, cross-border from Hong Kong, five acquirers, and 100% of it addressable.
6. **Portfolio leverage.** One white-labelled front-end across LivU, Tumile, Vivah — and Yaar is APK-only, so off-store by construction.

**Do not use:** payment complaints (none established); any claim about which methods the first-party till offers; any APAC revenue-share claim; Paytm (string only); "no 3DS".

---

### Section 11: Similar Companies & Prospecting Pipeline

- **Direct competitors in the category:** MICO, Chamet, Azar (already researched — `2-ready-to-outreach/azar.md`, 16/29, in-house), Omega, HOLLA, GOGO LIVE. MICO and Chamet share the Codashop `/international/` consolidation, so the reseller pattern is category-wide.
- **Azar is the closest analogue already in this repo** and reached the **same in-house classification** — two independent accounts in one vertical both building their own routing layer is a pattern worth naming internally.
- ❌ **No competitor confirmed on any orchestrator.** Scored 0.
- 🔎 **Pipeline candidates surfaced:** **Tumile** and **Yaar** (same group, same platform), **MICO**, **Chamet**, **HOLLA Group** (Omega).

---

### Section 12: Business Case Data

| Metric | Value |
|---|---|
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ~40,000–50,000/month orchestrable** (web till + reseller). `[ASSUMPTION — not researched.]` Basis and billing unit in the ICP breakdown. Including Google Play IAP, total is plausibly ≥100,000/month. **No sourced figure exists.** |
| Active users | **25m daily users across all regions** — *group-wide, self-reported*, `rileycillian.com/products.html`. Not LivU-specific, not audited. |
| Installs | **69,952,626** (Google Play, LivU only) |
| Ratings | 4.32 / 421,642 ratings / 3,323 reviews |
| IAP ticket range | **$0.10 – $253.70 per item** (Google Play) |
| Revenue / GMV / TPV | **No public information found.** |
| Approval rate / chargebacks / MDR | **No public information found.** |
| Primary currency | Not established — presentment currency not visible unauthenticated |
| Top 3 markets by revenue | **Unknown.** Web-till mix is Turkey / US / Brazil `[EST]`; APAC share unmeasured. |
| **Billing channel split (web vs app store)** | **Apple: 0% — delisted.** Google Play: live. First-party web till: live, actively promoted. Codashop reseller: live. **Split unquantified**, but the app-store trap does **not** apply. |

---

### Overall Research Confidence

**High on the stack, Medium on the business, Low on volume and geography.**

- ✅ **High** — PSP estate, orchestration classification, entity chain, recurring/vault architecture, Apple delisting. All read by me from live first-party sources today: production config, the JS bundle, the Play listing, the ToS, the privacy policy and the open Zendesk API.
- 🟡 **Medium** — APM coverage. The reseller rails are sourced from archived first-party storefronts; the first-party till's catalogue is gated.
- 🔴 **Low** — **traffic and country mix** (SimilarWeb, second-hand, I could not re-fetch it — 202 challenge) and **transaction volume** (assumed, not sourced).

No confidence downgrade for egress: WebFetch via Bash curl worked throughout with `--cacert /root/.ccr/ca-bundle.crt`.

### Manual Research Recommendations
1. **Confirm the monthly transaction count** — the one number that carries this account, and currently an assumption. Ask on the first call.
2. **Establish why and when Apple delisted them**, and whether it is permanent. Decides whether the hook is a structural shift or a blip.
3. **Log into the till with a real account** and capture the method list per country — the only way to establish the APAC rail gap and score that row.
4. **Confirm APAC's share of revenue.** Everything measurable points at Turkey/US/Brazil; everything structural points at APAC.
5. **Trace GoQun Limited** — the APAC payment counterparty, jurisdiction unknown.
6. **Check which local methods survive on `codashop.com/international/livu`.**

### Source Notes
- ✅ **Verified by me, first-hand, on 2026-09-17:** the Apple 404 and `resultCount: 0` across eight storefronts; the dead `iosDownload` link inside their own config; `livuchat.com/payment` HTTP 200 and its full `window.baseConfig`; the 135KB app bundle including all sixteen orchestration endpoints, `payCompanyCode` values, the subscription i18n block and the card-vault routes; the Play listing (installs, IAP band, ratings, developer of record); the ToS and privacy policy; `rileycillian.com` and its products page; all 46 Zendesk help-centre articles; `codashop.com/international/livu` HTTP 200; and the gated `queryCountryList` 404.
- ⚠️ **Not verified by me:** the SimilarWeb country split (202 challenge on re-fetch) and the Wayback Codashop method tables (agent-sourced, URLs recorded above and re-checkable).
- 📌 **Two corrections issued against the agent report:** it declined to attribute an IAP price band (the structural position proves `$0.10 – $253.70` is LivU's), and it missed the recurring-subscription and card-vault layer entirely — which is the single most commercially relevant finding in this file.
- 📌 **One discrepancy resolved:** my earlier extraction from `livuapp.com` showed only Checkout.com, dLocal, Stripe and Forter. The `livuchat.com` bundle adds PayerMax and Airwallex. Both stacks are real; `livuchat.com` is the current till.
- ❌ **Substring false positives checked for and none found** — `qris`, `gcash`, `upi`, `promptpay`, `paynow`, `paypal`, `adyen`, `braintree`, `xsolla` all returned **zero** raw hits in the bundle, so there was nothing to disambiguate.

### TAL corrections — `accounts/apac-tal.csv` row 108
| Column | Current | Should be |
|---|---|---|
| `INFO` | *"global users buy coins, **billed largely through Apple and Google**"* | ❌ **Refuted.** Apple: **delisted**, contributes nothing. Google: live, but one of three rails alongside a first-party web till and a Codashop reseller rail — and the company actively pushes users off-store. |
| `Payment Gateway` | *(empty)* | Stripe, Checkout.com, dLocal, PayerMax, Airwallex, Coda Payments |
| `Payment Orchestrator` | *(empty)* | **In-house** (`portal.rcplatformhk.com`, `thirdPaymentRecon`) |
| `INDUSTRY` | Dating | Live random video chat / social discovery — not a dating product |
| `WEBSITE` | `livuapp.com` | Payment surface is **`livuchat.com`**; help centre `support.livu.me`; group `rileycillian.com` |
| `HQ Country` | Hong Kong | ✅ **Correct** — Clash Arts (HK) Limited, Wanchai |

---

## Executive Summary

LivU is a Hong Kong-operated live video-chat app under the Riley Cillian group, monetised through coin purchases and — a finding not in the agent report — **weekly and monthly recurring card-on-file subscriptions on its own web till**. The account list's premise that it is *"billed largely through Apple and Google"* is refuted twice over: **LivU is delisted from the Apple App Store entirely**, and it runs both a first-party store at `livuchat.com/payment` and a Coda Payments reseller rail carrying DANA, QRIS, GCash, FPX, Touch 'n Go and Philippine carrier billing. The stack is **five acquirers — Stripe, Checkout.com, dLocal, PayerMax, Airwallex — routed by a self-built orchestration layer** on their own gateway, with a reconciliation service, a country-keyed method catalogue, Apple Pay eligibility logic written out three times (once per acquirer), and a Checkout.com v2 migration in flight today. The motion is **In-house**, and the pitch is reach and opportunity cost, never "you need orchestration". **It scores 11/29 🟢 Medium — held down honestly by two unknowns rather than two absences**: orchestrable transaction volume is assumed, not sourced, and the only traffic data available points at Turkey, the US and Brazil rather than APAC.

</details>
