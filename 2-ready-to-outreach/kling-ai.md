# Kling AI

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 23 / 29 → ⭐ **High Priority**
**Industry:** AI video generation — consumer subscription + enterprise API · **HQ:** Singapore billing entity (**Kling AI Pte. Ltd.**); parent Kuaishou Technology, Beijing · **Researched:** 2026-09-29 · **First email sent:** —
**Motion:** **Greenfield.** Single-PSP Stripe on web. Zero orchestrator evidence anywhere, and none in the entire AI-video peer set.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Kling AI is Kuaishou's AI video-generation product and its self-declared *"second growth curve."* It went from launch (June 2024) to **~US$500m ARR by March 2026**, serves **60m+ creators and 30,000+ enterprise clients**, and is now being carved out — a **~US$3bn raise at ~US$18bn** was filed with HKEX in July 2026 with an IPO targeted for Q1 2027. Global billing runs from a 20-month-old Singapore entity on **one Stripe integration**.

> ## 🎯 THE HOOK — their own renewal copy tells the customer to go fix their bank balance
>
> Pulled by me from the live international i18n manifest on 2026-09-29
> (`kling-ai-web.production.18cac1432bed9628.json`, 1,157,280 bytes, 5,299 keys, `language: ["en","ja","ko"]`):
>
> ```
> renewal-notice             = "Your subscription is frozen. Please make sure to have enough
>                               balance in your payment account while renewal attempts are being made."
> renewal-tag                = "Suspended"
> renewal-description        = "Subscription under renewal. Please ensure the balance."
> subscription-under-renewal = "{membership} Frozen"
> ```
>
> **A failed renewal freezes the account and hands the recovery back to the customer.** There is no dunning ladder in this copy, no retry-window messaging, no alternate-method prompt — the product's answer to a declined renewal is "go top up your account."
>
> Now put that next to **India = 15.21% of their traffic**, card-on-file recurring, priced in USD, cross-border from Singapore. Involuntary churn there is almost certainly material and almost certainly unmeasured. This is observable and quotable — **not a projected pain.**

> ## 💥 THE SECOND HOOK — the whole app is priced in dollars, in three languages
>
> From the same manifest:
> ```
> currency         = "USD"
> price-unit       = "$<i>{price}</i>"          ← the $ glyph is hardcoded into the template
> price-per-period = "$<i>{price}</i> {duration}"
> language         = ["en", "ja", "ko"]
> ```
> **Three languages ship on the international build.** India (15.21%), Brazil (4.47%), Russia (3.92%), Indonesia (3.35%) — four of the top six markets — get English and a dollar sign.
>
> ⚠️ **Do not overstate this.** Stripe's `createCurrencySelectorElement` (Adaptive Pricing) *is* mounted at the Elements layer, below anything observable here — so a user in India may well be *presented* a local amount at the final step. What is sourced is that **the app itself is USD-only and unlocalised**. A Japanese walkthrough describes USD prices converted at card FX of 1.6–3.0% with *the billed amount varying month to month on the same plan* — consistent, but that is one third-party account.

**SimilarWeb total visits:** shares only — no visit count in the supplied view. **Supplied by Prateek 2026-09-29**, Jun–Aug 2026, 121 countries. Full table and my domain-resolution work: `accounts/traffic/kling-ai.md`.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇮🇳 **India** | **15.21%** (audience share 20.90%, 6.79 pages/visit — the engagement leader) | Cards via Stripe; one user report of PhonePe UPI ⚠️ | UPI as a first-class web rail ⬜ · netbanking ⬜ · EMI ⬜ — **none evidenced, none disproved** | ❌ billed cross-border from Singapore |
| 2 | 🇺🇸 United States | 11.75% | Cards, PayPal, Apple, Google Pay | — | ❌ no US entity confirmed in the group |
| 3 | 🇰🇷 Korea | 5.08% (▲7.51%) | Cards; **UI is localised to Korean** | KakaoPay, Naver Pay, Toss — **not found** | ❌ |
| 4 | 🇧🇷 Brazil | 4.47% (▲9.41%) | Cards | Pix ⬜ · boleto ⬜ · instalments ⬜ | ❌ — *and the parent runs Pix through three PSPs on Kwai* |
| 5 | 🇷🇺 Russia | 3.92% | Cards | — | ❌ |

*(then 🇮🇩 Indonesia 3.35% ▼46.45% · 🇵🇰 Pakistan 2.77% · 🇯🇵 Japan 2.69% — **konbini and bank transfer explicitly NOT supported** · 🇩🇪 2.50% · 🇫🇷 2.41% · 🇬🇧 2.39%)*

### Legal entities
- **KLING AI PTE. LTD.** (Singapore) — **UEN 202502609E**, incorporated **17 January 2025**, Live. 1 Raffles Place, #36-01, One Raffles Place, Singapore 048616. SSIC 62011 (development of e-commerce applications). ⚠️ *Third-party ACRA mirror, not BizFile — pull the official profile before anything contractual.*
- **Beijing Kuaishou Technology Co., Ltd.** — the vendor entity on AWS Marketplace **China**, priced in RMB
- **JOYO TECHNOLOGY PTE. LTD.** (Singapore, UEN 201621256R) — sibling international holdco at **the same address and unit**

> 📌 **The entity was incorporated seven months AFTER the product started monetising** (launch June 2024 → incorporation Jan 2025). That is the signature of a payments stack that was bolted on, not designed.

### Known PSPs
- **Stripe** — `[Terms]` *"the payment channel (such as Stripe)"* + `[Source Code]` Elements, Adaptive Pricing currency selector, Stripe Tax. Two enum keys map to it: `PROVIDER_CASHIER` and `SINGLE_PAYMENT`
- **PayPal** — `[Source Code]` `payment-channel-PAYPAL` = `"PayPal"`, enumerated as a **peer of** Stripe's own keys
- **Alipay / WeChat Pay** — `[Source Code]` China path, `supportProviders` array, QR flow
- **Apple / Google Pay / Google Play** — `[Source Code]`
- **`OFFLINE`** — `[Source Code]` a manual bank-transfer channel, matching the enterprise *"corporate payments"* and *"Reissue Invoice"* strings

**The complete enumerated channel set, verbatim:**
```
PROVIDER_CASHIER → Stripe     SINGLE_PAYMENT → Stripe      CARD_FRAME → Card
PAYPAL → PayPal               APPLE → Apple                GOOGLE → Google Pay
ALIPAY → Alipay               WECHAT → WeChat              OFFLINE → OFFLINE
REDEEM → Redeem
```

### Orchestration status
**None detected — direct PSP integrations only. Greenfield.** No orchestrator string appears in any Kling bundle; no orchestrator is named in any Kling or Kuaishou material; and no AI-video peer uses one either (§11C). *Note the contrast with the parent: Kwai runs five acquirers behind an in-house layer — see `2-ready-to-outreach/kuaishou.md`.*

### Buying signals
- 💰 **Carve-out raise filed with HKEX 2026-07-02** — a capital increase into **Beijing Kling (北京可灵)** capped at **RMB 20,447.10m / US$3,000.00m** for **~16.67%** of enlarged registered capital, diluting Kuaishou **100% → ~68.33%**. Filing-stated **pre-transaction valuation US$15.00bn**. **Tencent US$200.00m exactly** (RMB 681.57m each via Shanghai Qishan + Parallel Mars); **Alibaba ties it** (Hangzhou AliCloud Apsara, RMB 1,363.14m); **Baidu** RMB 340.79m — all three, which Chinese trade press calls 罕见 (rare)
- ⚠️ **Three things everyone repeats about this deal are wrong — see §6.** There is no filed "US$18bn post-money", no lead investor, and no Q1 2027 IPO target.
- 🚀 **ARR ~US$500m as of March 2026** — verbatim in the Q1 2026 results release; up from US$240m (Dec 2025) and US$100m (Mar 2025)
- 🚀 Q2 2026 revenue **>RMB 850m, +200%+ YoY**; Q1 2026 **>RMB 650m, +300%+ YoY**; H1 2026 **RMB 1.5bn**
- 🤝 **Live AWS Marketplace listing** — a fourth billing rail where **AWS collects and remits**, routing enterprise buyers into private offers
- 💼 **Team Plan** (up to 15 seats) launched Q1 2026 — their first seat-based SKU; enterprise ladder tops out at a self-declared **$150,000+/month** band
- 😠 **Trustpilot 1.2 / 5 across 398 reviews**, dominated by billing and cancellation failures

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Kling AI`.*

⚠️ **Read before drafting.**

1. **Lead with the dunning string.** `renewal-notice` is the sharpest artefact on this account — their own product telling a customer to go top up their balance. Quote it verbatim.
2. **Pair it with India at 15.21%.** Biggest market, best engagement (6.79 pages/visit, 20.90% audience share), English-only UI, USD pricing, cross-border from Singapore. That is the asymmetry, and both halves are theirs.
3. **Motion is GREENFIELD** — noting the absence of a routing layer is fair. But the stronger frame is the **carve-out**: between a $3bn raise and a Q1 2027 IPO, payments stops being inherited and becomes an audited line item.
4. **Never claim they lack UPI, Pix or 3DS.** Stripe renders dashboard-configured methods and performs 3DS server-side — **bundle absence is not sourced absence.** What IS sourced: the app ships three languages and a hardcoded `$`.
5. **The app-store trap is live.** App Store, Google Play, Stripe web, PayPal, OFFLINE, AWS Marketplace — **six channels, split undisclosed.** Do not size the business case without asking.
6. **Do not quote "100 million users."** It is media-sourced and conflicts with a 60m-registered / 12m-MAU figure for April 2026. The safe, primary numbers are **60m creators, 600m videos, 30,000 enterprise clients** (Dec 2025).
7. **Do not use the Kuaishou group revenue** (RMB 142.8bn) for this account. Kling is ~US$500m ARR.
8. **Peer proof is strong here:** Runway and Luma both run single-PSP Stripe, verbatim from their own terms. Nobody in this vertical has orchestration. That cuts both ways — use it as "the category hasn't solved this yet," not as social proof.

---

### ⛔ Five things to get right about the carve-out — verified against the HKEX filing itself, 2026-09-30

A deep-research pass (104 agents, adversarial 3-vote verification) went back to the filed
document. **Four of the five most-repeated claims about this deal are wrong**, and they were
in the first version of this file. Corrected:

| Everyone says | The filing actually says |
|---|---|
| "US$18bn post-money" | **No post-money valuation is stated anywhere.** The filing gives a **pre-transaction valuation of US$15.00bn**. The 18 is arithmetic press did (15 + 3), and press is itself inconsistent — The Information headlined it *"$15 Billion Valuation"*, and a US$20bn figure also circulates |
| "raised US$3bn" | **US$3,000.00m (RMB 20,447.10m) is a contractual CEILING.** ~**RMB 19,047.10m (US$2.79bn)** was committed at signing, with RMB 1,400m left as *"Reserved interests for other Additional Investors"* and a 60-day joinder window |
| "General Atlantic led it" | **GA appears nowhere in the filing** — zero occurrences across ~123,600 extracted characters — and **the filing designates no lead, cornerstone or anchor investor at all.** The GA framing traces to a Bloomberg report of *talks* on 17 June 2026, superseded by a larger, differently-composed closed round |
| "IPO as early as Q1 2027" | **"2027" appears zero times. No venue is named.** The only dated IPO reference is an investor **redemption right: cost + 8% simple annual interest if Beijing Kling has not listed by 30 October 2031.** Q1 2027 is press-reported company intent (Jiemian), not a filed commitment |
| "Tencent is in" | ✅ **True, and exact.** **US$200.00m** — RMB 681.57m each via **Shanghai Qishan Investment** (PRC) and **Parallel Mars Investment** (Cayman) = RMB 1,363.14m at the filing's own 6.8157 rate. **Alibaba ties it** (Hangzhou AliCloud Apsara, RMB 1,363.14m) and **Baidu** took RMB 340.79m |

**Structure:** the vehicle is **Beijing Kling (北京可灵), a PRC entity** — *not* Kling AI Pte. Ltd.,
the Singapore entity that bills customers. Kuaishou dilutes **100% → ~68.33%** (16.67% investors
+ 15.00% incentive schemes). Largest single subscriber: Shanghai Guofang Digital Technology,
RMB 1,690.00m. Others named: CPE Spruce RMB 850.79m · Beijing CAS Generation RMB 943.00m ·
BlueFive (ADGM) RMB 545.26m · China Internet Investment Fund RMB 400.00m · Qiming's QM323
RMB 204.47m · CITIC Securities Investment RMB 100.00m · Monolith Kling Fund RMB 136.31m.

> ### ⚠️⚠️ NEVER call their "ARR" annual recurring revenue
> Kuaishou's own published definition is **`ARR = Monthly Operating Revenue × 12`** — the
> current month's revenue times twelve. It sits **~38% above annualised realised revenue**:
> Q1 2026 annualises to about **US$360m** against the **~US$500m** March run rate.
> **Actual FY2025 revenue was RMB 1.04–1.1bn (~US$150–162m).** If Prateek says "$500m ARR" to
> a CFO who reads it as recurring revenue, the number will not survive the meeting.
> Lead with **Q2 2026: >RMB 850m, +200% YoY** — it is a real quarterly figure.

> ### 💡 The finding that strengthens the pitch
> The carve-out entity is **deeply loss-making**: net loss **RMB 0.5bn (FY2024) → RMB 1.9bn
> (FY2025)**, RMB 2.4bn cumulative, and **negative net assets of −RMB 9m** at 2025-12-31.
> It now has ~US$2.79bn of outside money on the register and a redemption clock. **Growth at
> any cost is over; unit economics are now somebody's job.** That is the real reason payments
> gets looked at, and it is a better frame than the IPO date.

**Additions to the never-use list:**
- ❌ The **"enterprise API ~60% / consumer ~40%"** revenue split — traces solely to
  **macrostream.ai, an AI-generated analyst-summary site**. Not in any transcript, filing or
  Chinese coverage. **The split is genuinely undisclosed.**
- ❌ **"100 million users"** — no company-issued source supporting it was found. Kuaishou's own
  December 2025 wording was *"over 60 million **creators**"* — cumulative creators, not
  registered users and not MAU. The 100m figure is asserted without attribution.
- ❌ **"~75% of revenue from overseas"** — a geographic split attributed to the Q1 2026
  earnings call, not a filing disclosure, and **not verified**.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 23 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED (bounded): >>100,000/month.** Sourced inputs: Q2 2026 revenue **>RMB 850m** ≈ US$119m/quarter ≈ **US$39.7m/month** ([Q2 2026 release](https://www.prnewswire.com/news-releases/kuaishou-technology-announces-second-quarter-and-interim-2026-unaudited-financial-results-302855081.html)) and the published tier ladder **$8.80 / $32.56 / $80.96 / $159.99** per month. Even if **every dollar** billed at the top Ultra tier, that is **248,000 charges/month**; at a realistic blended ~$30 it is ~1.3m. ⚠️ Tier prices are third-party-captured, not read by me off their page, so this is a bound not a measurement — but the ≥100,000 band is robust. **Billing unit: subscription charges + prepaid credit packs; API/marketplace billing is separate and uncounted.** |
| Orchestration status | **+4** | ✅ **Greenfield** — Stripe only, no orchestrator anywhere |
| 3+ countries | **+3** | ✅ 121 countries; 11 above 2% traffic share |
| Multiple PSPs | **+3** | ✅ `payment-channel-PAYPAL` and `payment-channel-ALIPAY`/`WECHAT` are enumerated as **peers of** Stripe's own two keys ⚠️ *enum evidence — it does not prove separate merchant relationships* |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **Withheld deliberately.** Top 3 are India, US, Korea. Korean wallets and Indian UPI are "not found" in the bundle — but **Stripe renders dashboard-side methods invisibly**, so that is not sourced absence. Japan's konbini gap *is* sourced but Japan is #8. **No point awarded without a source for the absence.** |
| Recent expansion | **+2** | ✅ Kling 3.0 (Feb 2026) and 3.0 Turbo; **Team Plan** launched Q1 2026; **Kling MCP + CLI**; #1 on the App Store across 42 countries; AWS Marketplace listing |
| Payment issues | **+2** | ✅ Trustpilot **1.2/5, 398 reviews**; repeat charge attempts after confirmed cancellation, named reviewers, Aug–Sep 2026 |
| Funding >$10M | **+2** | ✅ **Capital increase filed with HKEX 2026-07-02**, capped at US$3,000.00m, with **~US$2.79bn committed at signing**. Clears the threshold by three orders of magnitude |
| High traffic outside home | **+2** | ✅ China does not appear in the top 11 at all — the Chinese product is on a separate host (`klingai.kuaishou.com`). Home share is far below 60% |
| Competitor using orchestration | **0** | ❌ **Runway and Luma both single-PSP Stripe** (their own ToS); HeyGen names none. No orchestration anywhere in the vertical |
| Payment job postings | **0** | ❌ Searched twice, none found. No hiring signal exists to cite |

**Tier:** ⭐ **High Priority (17+)** → **23/29**

> **No analyst override applied — but one was considered.** The app-store trap is live (six billing channels, split undisclosed), which normally scores an account *down*. It is not applied here because a large share of Kling's revenue is demonstrably **not** app-store: 30,000+ enterprise API clients, a prepaid API package ladder to $7,560, an AWS Marketplace listing, and an enterprise lead form whose top band is **$150,000+/month**. That revenue is web- and invoice-billed by construction. **Still ask for the split in discovery — it bounds the business case.**

### Source Notes
- ✅ **Dunning strings, payment-channel enum, `currency`/`price-unit` templates, `language:["en","ja","ko"]`** — pulled by me from the live i18n manifest, 2026-09-29, 404-body check passed
- ✅ **Stripe Elements / Adaptive Pricing / Stripe Tax** — mined by me from `PayStripeComponent-BGhR4Kpi.js`; independently corroborated by a prior sweep recorded in `minimax-io.md` (`STRIPE_MANAGE_URL`, `theme:"stripe-tax"`, gated on `region !== CN`)
- ✅ **Entity, governing law, Stripe naming, Credits pricing** — read by me in kling.ai's own live policy documents
- ✅ **ARR US$500m / Q1 2026 >RMB650m +300% / Q2 2026 >RMB850m +200%** — read by me verbatim in Kuaishou's own results releases
- ✅ **Export-control screen clean** — BIS Entity List, OFAC SDN, OFAC Consolidated, all with passing controls ("Kling" hits were *"Sparkling Wine"*)
- ⚠️ **ACRA UEN 202502609E** — third-party mirror, not BizFile. Address matches my own first-hand read of their ToS, which is good corroboration; the UEN itself is unverified
- ⚠️ **Pricing tiers** — third-party captures (Magic Hour, screenshot dated 2026-09-25; eesel; costbench), with some drift on Ultra ($128 → $180). Not read by me off their page
- ✅ **The carve-out** — verified 2026-09-30 against the **HKEX filing itself** by a 104-agent deep-research pass with adversarial 3-vote verification. See the corrections block in §2
- ⚠️ **Trustpilot and AWS Marketplace** — agent-verified, not re-fetched by me
- ❌ **Pricing tiers, user numbers and the competitive comparison did NOT survive that verification pass** — no claim on any of the three was confirmed. The hedges already in this file stand, and should be treated as *less* certain rather than more: the third-party price captures in §12 remain the only evidence, and the "100m users" conflict is unresolved
- ⚠️ **"100m users June 2026"** — media only (36Kr); conflicts with 60m registered / 12m MAU for end-April 2026. **Hedge or avoid**
- ⚠️ **FY2025 Kling revenue RMB 1.04bn / ~US$150m** — Caixin's figure, not a Kuaishou line. The FY2025 release gives only Q4 (RMB 340m)

### Success Case Alternatives
- **A global consumer-subscription business with a large India base billing cross-border on cards** — the profile match is involuntary churn and local-rail reach, which is exactly the dunning finding
- ⚠️ **Do not use the "Netflix +40% APAC via orchestration" claim.** It traces to a single payments-vendor marketing page with no Netflix source behind it and appears fabricated

---

## Executive Summary

Kling AI is Kuaishou's AI video-generation business, described by its own parent as the group's *"second growth curve"* — **~US$500m ARR as of March 2026**, up from US$100m a year earlier, with Q2 2026 revenue **>RMB 850m (+200%+ YoY)**. It bills the world from **Kling AI Pte. Ltd.**, a Singapore entity incorporated **seven months after the product started monetising**, on **a single Stripe integration**. The decisive payment finding is in their own product copy: a failed renewal **freezes the subscription and instructs the customer to top up their own balance** — with India at 15.21% of traffic, on USD card-on-file recurring, cross-border. The motion is **greenfield**, and the timing is unusually good: a **~US$3bn raise at ~US$18bn** was filed with HKEX in July 2026 with an **IPO targeted for Q1 2027**, which is precisely when payments stops being an inherited arrangement and becomes an audited line item.

---

## Section 1: Website Traffic Analysis by Country

**Data source: SimilarWeb, supplied by Prateek 2026-09-29** (Jun–Aug 2026, `kling.ai`, all traffic, 121 countries). Primary source — used verbatim, not re-researched. Shares only; no visit count in the supplied view.

| Rank | Country | Traffic Share | Est. Monthly Visits | Trend | Source |
|------|---------|---------------|---------------------|-------|--------|
| 1 | 🇮🇳 India | **15.21%** | not shown | ▼ 0.06% — **flat** | SimilarWeb (supplied 2026-09-29) |
| 2 | 🇺🇸 United States | **11.75%** | not shown | ▼ 10.03% | same |
| 3 | 🇰🇷 Republic of Korea | **5.08%** | not shown | ▲ 7.51% | same |
| 4 | 🇧🇷 Brazil | 4.47% | not shown | ▲ 9.41% | same |
| 5 | 🇷🇺 Russia | 3.92% | not shown | ▼ 8.06% | same |
| 6 | 🇮🇩 Indonesia | 3.35% | not shown | ▼ **46.45%** | same |
| 7 | 🇵🇰 Pakistan | 2.77% | not shown | ▼ 26.08% | same |
| 8 | 🇯🇵 Japan | 2.69% | not shown | ▲ 7.72% | same |
| 9 | 🇩🇪 Germany | 2.50% | not shown | ▲ 2.41% | same |
| 10 | 🇫🇷 France | 2.41% | not shown | ▼ 10.19% | same |
| 11 | 🇬🇧 United Kingdom | 2.39% | not shown | ▼ 2.48% | same ⚠️ rank cell partly obscured |

**High priority (>5%): India, United States, Korea.**

**Arithmetic computed by me:** visible top 11 = **56.54%** of total, so **43.46% sits in 110 unshown countries** — no claim about the long tail is supportable. **APAC across the visible rows = 29.10%** (IN 15.21 + KR 5.08 + ID 3.35 + PK 2.77 + JP 2.69), **a floor, not a total**, and **2.5× the United States**.

**Domain resolution — checked by me, 2026-09-29.** The "include all country domains" toggle was OFF, which would normally invalidate the dataset. It does not here:
```
klingai.com → 301 → kling.ai/       www.kling.ai → 301 → kling.ai/
app.klingai.com → 301 → kling.ai/app/     kling.ai → 200, canonical
```
⚠️ **China is absent from the top 11 because the Chinese product lives on `klingai.kuaishou.com`, a separate host.** That is a scoping artefact, not a finding — do not read it as "no China business."

---

## Section 2: Legal Entities & Local Presence

**Headquarters:** billing and contracting from **Singapore**. Parent Kuaishou Technology, Beijing (Cayman-incorporated, HKEX 1024).

| Country | Entity Name | Registration # | Source |
|---|---|---|---|
| **Singapore** | **KLING AI PTE. LTD.** | **UEN 202502609E** — inc. **2025-01-17**, Live, Private Ltd by Shares, SSIC 62011, last AR 2026-07-30 | ⚠️ [RecordOwl ACRA mirror](https://recordowl.com/company/kling-ai-pte-ltd) — **not BizFile** |
| Singapore | *(same, from their own documents)* | 1 Raffles Place, #36-01, One Raffles Place, Singapore 048616; **laws of Singapore** govern | ✅ [kling.ai/docs/user-policy](https://kling.ai/docs/user-policy) — read by me |
| Singapore | JOYO TECHNOLOGY PTE. LTD. | UEN 201621256R; **same address and unit** | GLEIF |
| PRC | Beijing Kuaishou Technology Co., Ltd. | Vendor of record on AWS Marketplace **China**, priced in RMB | AWS Marketplace China listing |

From their own Terms, verbatim: *"a legally binding contract between you and **Kling AI Pte. Ltd.** and its affiliates"*.
They are **GST-registered in Singapore** — the product ships a `singapore-gst-number` = *"Singapore GST Reg No."* field and a `console.order-manage-page.reissueInvoice` = *"Reissue Invoice"* flow.

**Cross-Border Gap Analysis**

| Country | In Top 10? | Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---|---|---|---|---|
| 🇮🇳 India | **Yes (#1)** | ❌ | ✅ **Yes** — RBI Payment Aggregator regime | **HIGH** |
| 🇺🇸 US | Yes (#2) | ❌ | No | Moderate |
| 🇰🇷 Korea | Yes (#3) | ❌ | ✅ **Yes** — domestic card acquiring effectively needs a Korean entity | **HIGH** |
| 🇧🇷 Brazil | Yes (#4) | ❌ *(the parent has one — Joyo Tecnologia Brasil)* | Local acquiring available via local PSPs | **HIGH** |
| 🇯🇵 Japan | Yes (#8) | ❌ *(the parent has Kwai KK)* | No | Moderate |

> **Warning: potential cross-border operation in India.** India is Kling's #1 market at 15.21% with the best engagement in the table, and there is **no Indian entity**. Transactions are processed cross-border against a Singapore entity, with higher scheme costs, lower approval rates on domestically-issued cards, and FX on top.

> **Regulatory gate: India and Korea.** Both markets effectively require local presence or a licensed local partner for domestic acquiring. ⚠️ **Verify the current RBI PA and Korean PG rules against a live source before citing either in an email** — per the APAC reference, never cite an APAC regulatory rule from background knowledge.

> 📌 **The timing detail worth using:** Kling launched **June 2024** and monetised immediately; **Kling AI Pte. Ltd. was incorporated 17 January 2025**. The billing entity followed the revenue by seven months.

---

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Region | PSP/Acquirer | Evidence Type | Source URL |
|---|---|---|---|
| Global (web) | **Stripe** — *"the payment channel (such as Stripe)"*; *"For Stripe subscription payments [Manage my subscription — Cancel subscription — Go to Stripe to manage]"* | `[Terms/Privacy Policy]` | [kling.ai/docs/payment-policy](https://kling.ai/docs/payment-policy) |
| Global (web) | **Stripe** — Elements (`createPaymentElement`), **Adaptive Pricing** (`createCurrencySelectorElement`), `providerSecret`, telemetry `STRIPE_FAILED`, Stripe **Tax** CSS classes | `[Source Code]` | `kling-web/assets/js/PayStripeComponent-BGhR4Kpi.js` (17,451 b) |
| Global | **PayPal** — `payment-channel-PAYPAL` = `"PayPal"`, a peer key to Stripe's own two | `[Source Code]` | live i18n manifest |
| Global | **Apple / Google Pay** — `payment-channel-APPLE`, `payment-channel-GOOGLE` = `"Google Pay"` | `[Source Code]` | same |
| 🇨🇳 China | **Alipay + WeChat Pay** — `supportProviders.includes("ALIPAY")` / `("WECHAT")`, QR copy *"请用支付宝/微信扫一扫完成支付"* | `[Source Code]` | `ComponentPaymentV2-BLrTwZKL.js` |
| Enterprise | **`OFFLINE`** — manual/bank-transfer channel; Terms: enterprise prepaid top-up by **offline corporate bank transfer only** | `[Source Code]` + `[Terms]` | i18n manifest; payment-policy |
| Enterprise | **AWS Marketplace** — *"You will pay recurring monthly usage fees through your AWS bill"*; *"Sold by: KLING AI"*; refunds *"Not currently supported"* | `[Third-Party Report]` | [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-6636lqgc4tu2w) ⚠️ agent-fetched |
| 🇨🇳 China enterprise | **AWS Marketplace China** — vendor **北京快手科技有限公司**, priced ¥1.00→¥0.75/credit | `[Third-Party Report]` | [AWS Marketplace China](https://awsmarketplace.amazonaws.cn/marketplace/pp/prodview-hknqxyvq35qz2) ⚠️ agent-fetched |

**Implementation detail:** the Stripe integration carries a Chinese-language error string — `"Stripe checkout 挂载点不存在"` ("Stripe checkout mount point does not exist") — so it was built in-house by Kuaishou, not by an agency. Recurring mandates are managed through `/api/pay/restoreContract` and `/api/pay/uncontract` (签约 = contract/mandate). Billing periods: `monthly` | `quarterly` | `yearly`, prices in minor units, with a first-period discount mechanism (`prices[0].type === "FIRST"` + `proportion`).

**PCI:** **No public information found.** `[INFERENCE, not confirmed]`: Stripe Elements keeps PAN out of their environment, consistent with a reduced SAQ A scope. Recommended Yuno integration: **SDK**, to preserve it.

### 3B. Payment Orchestrator

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with PSP(s), which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

**Greenfield — confirmed as far as it can be.** No orchestrator string in any Kling bundle; none named in any Kling or Kuaishou material; none used by any AI-video peer.

⚠️ **Two honest caveats:**
1. **The parent is not greenfield.** Kwai runs five acquirers behind an in-house layer. If a Kling conversation escalates to Kuaishou group, the motion changes — see `2-ready-to-outreach/kuaishou.md`.
2. The `OFFLINE` and AWS Marketplace channels mean Stripe is not the *only* money path, even though it is the only PSP.

> **MANUAL:** Walk the Kling checkout with DevTools from an Indian and a Brazilian IP. Stripe's Payment Element renders dashboard-configured methods that **cannot** be seen in the bundle — this is the only way to settle what India and Brazil actually get.

---

## Section 4: Alternative & Local Payment Methods

| Country | Method | Category | Status | Source |
|---|---|---|---|---|
| Global | Cards (Visa, Mastercard) | Cards | **Active in checkout** | [Kling AI, 2024-08-07](https://x.com/Kling_ai/status/1821172427797516475) — announced as a *"Payment System Upgrade"*, i.e. **cards were not available at launch** |
| Global | PayPal | Digital wallet | **Active in checkout** | i18n enum |
| Global | Apple Pay / Google Pay | Digital wallet | **Active in checkout** | i18n enum |
| Global | Apple IAP / Google Play IAP | Carrier billing/IAP | **Active in checkout** | help-centre cancellation copy |
| Enterprise | Offline corporate bank transfer | Bank transfer/A2A | **Active in checkout** | Terms §; `payment-channel-OFFLINE` |
| Enterprise | AWS Marketplace private offers | Bank transfer/A2A | **Active** | AWS listing |
| 🇨🇳 China | Alipay, WeChat Pay | Digital wallet | **Active in checkout** | `supportProviders` |
| 🇯🇵 Japan | JCB, Amex | Cards | *"may be supported"* — author advises falling back to Visa/MC on error | [note.com](https://note.com/yappyinsta/n/n01dd90acf143) |
| 🇯🇵 Japan | **konbini, bank transfer** | Cash / A2A | ❌ **NOT supported** — stated explicitly | same |
| 🇮🇳 India | UPI via PhonePe | Bank transfer/A2A | **Mentioned in press** — one first-person report: *"paid ₹3,038.83 via PhonePe UPI"* ⚠️ could be Google Play India billing, not Stripe web | sikayetvar.com |
| 🇮🇳 India | netbanking, RuPay, EMI, Paytm | — | **Not found** | — |
| 🇰🇷 Korea | KakaoPay, Naver Pay, Toss | Digital wallet | **Not found** | — |
| 🇧🇷 Brazil | Pix, boleto, instalments | A2A / Cash / BNPL | **Not found** | — |
| 🇮🇩 Indonesia | QRIS, virtual account, wallets | — | **Not found** | — |

> **Warning: in Japan, konbini is widely used but not supported by Kling AI** — stated explicitly in a Japanese purchase walkthrough, alongside "bank transfer: not supported" and "prepaid cards generally not supported."

> ⚠️ **METHODOLOGY — this is the most important caveat in the file.** Kling mounts a **Stripe Payment Element**. Which methods that Element renders is configured **in the Stripe dashboard** and is **completely invisible in the JS bundle**. This was proven on MiniMax, where zero `apple_pay` hits coexisted with live Apple Pay. **Every "Not found" above is unresolved, not disproved.** Do not write "you don't support UPI" into an email — a prospect will correct you, and it has already happened once on another account in this repo.
>
> **What IS sourced absence:** the international build ships **three languages** (`["en","ja","ko"]`) and hardcodes `$` into the price template. That is a claim you can make.

---

## Section 5: Payment Issues & Customer Complaints

⚠️ All rows agent-verified from Trustpilot; not re-fetched by me.

| Issue Type | Platform | Frequency | Date Range | Source URL |
|---|---|---|---|---|
| **Recurring billing not stopping after cancellation — repeated charge attempts on a cancelled card** | Web | **HIGH** — multiple named, independent reviewers in one month | 2026-08-30 → 2026-09-25 | [Trustpilot](https://www.trustpilot.com/review/klingai.com) |
| Charged after subscription period ended; refund refused citing policy | Web | High (same cluster) | 2026-09-22 | same |
| Payment taken but credits not delivered / silently reduced after renewal | Web | Moderate | 2026-09-01, 2026-09-25 | same |
| Credits locked behind a forced subscription after a €100 credit purchase | Web | Isolated | 2026-09-01 | same |

**Trustpilot aggregate: 1.2 / 5 across 398 reviews.** Billing and cancellation — not output quality — dominate the recent negatives.

Verbatim (Анна Владимировна, 2026-09-14): *"Despite this confirmation, Kling has continued attempting to charge my card. There have now been **three payment attempts after the cancellation was confirmed**."*

> **Pattern — and it maps exactly onto a verified artefact.** The complaints describe *retry attempts that should have stopped*, and the product's own `renewal-notice` string describes *retry attempts the customer is told to fix themselves*. Both point at the same thing: **mandate and retry state is not being managed centrally.** That is a routing-layer job, and it is the single most defensible opportunity on this account.
>
> Their Terms compound it: **blanket non-refundability** — *"Once the Paid Service… is activated, the fee paid for the Paid Service is non-refundable."*

---

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|---|---|---|---|
| 1 | **2026-07-02** | **Capital increase into Beijing Kling filed with HKEX** — capped RMB 20,447.10m / US$3,000.00m for ~16.67%; pre-transaction valuation **US$15.00bn**; Tencent **US$200.00m**, Alibaba equal, Baidu RMB 340.79m | **Funding / carve-out** | ✅ [HKEX filing, 2026-07-02](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0702/2026070204065.pdf) — **primary source** |
| 2 | 2026-05-12 | Kuaishou shares +11% on spin-off reports; board *"evaluating a restructuring of Kling AI's assets and business, which may involve introducing external financing"* | Corporate | ChinaBizInsider; [SCMP headline](https://www.scmp.com/tech/article/3353214/kuaishou-stock-surges-reports-kling-ai-unit-spin) (403, headline only) |
| 3 | 2026-05-27 | **ARR ~US$500m as of March 2026**; Q1 2026 revenue >RMB 650m, +300%+ | Financial | [Q1 2026 release](https://www.prnewswire.com/apac/news-releases/kuaishou-technology-announces-first-quarter-2026-unaudited-financial-results-302782902.html) — read by me |
| 4 | Q1–Q2 2026 | **Team Plan** (15 seats) — first seat-based SKU; **Kling MCP + CLI** *"enabling AI agents to orchestrate Kling AI for batch content creation"*; native 4K | Product / channel | Q1 & Q2 2026 releases |
| 5 | 2025-01-17 | **Kling AI Pte. Ltd. incorporated in Singapore** — seven months after launch | Corporate | ⚠️ ACRA mirror |

**Public payment RFP:** **No public payment-related RFP found.**
**Payment job postings:** **None found.** Two targeted searches; no careers page, board or listing surfaced. **Do not claim a hiring signal.**
**PSP / billing-platform partnership:** **None announced.** Paddle, Airwallex, Adyen, Recurly, Chargebee — nothing. Stripe remains the only named processor. *(Metronome lists Kling in a public pricing index — that is market-intel content, not a customer relationship.)*

---

## Section 7: Payment-Specific News

| # | Date | Headline / Summary | Relevance | Source URL |
|---|---|---|---|---|
| 1 | 2026-07-02 | Kling AI carve-out capital increase filed with HKEX | The carve-out makes payments an owned line item | ✅ [HKEX filing](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0702/2026070204065.pdf) |
| 2 | 2026-01-13 | **"Kling AI, achieved monthly revenue exceeding USD20 Million in December 2025, corresponding to an ARR of USD240 Million… reached just 19 months after launch"** | The ARR ladder | PR Newswire ⚠️ agent-read via syndicated wire copy |
| 3 | 2025-06-05 | US$100m ARR in month 10. *"Monthly subscription bookings include paid prosumer subscriptions and corporate client API fees"* | Their own billings-vs-revenue framing | PR Newswire ⚠️ agent-read |
| 4 | **2024-08-07** | **"Payment System Upgrade"** — credit cards (Visa, Mastercard "and more options") added. **Cards were not available at launch** | Their card stack is barely 2 years old | [x.com/Kling_ai](https://x.com/Kling_ai/status/1821172427797516475) |
| 5 | 2026-04-21 | Payment Policy and Privacy Policy last updated; **Stripe named**; blanket non-refundability; guest checkout barred | Current contractual position | [kling.ai/docs/payment-policy](https://kling.ai/docs/payment-policy) — read by me |

**No provider removals found.**

---

## Section 8: Checkout Experience Audit

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | Embedded — Stripe Elements mounted in-app | Good | Not a redirect |
| Guest checkout | **Not available** — *"must be operated after you log in… if you do not log in you will not be able to purchase the Paid Services or make payments"* (Terms §6.2.1) | Fair | Deliberate |
| Card input | Tokenized Stripe Element, `billingDetails:{name:"never"}` | Good | PAN never touches their DOM |
| Methods visible | Cards, PayPal, Apple, Google Pay; Alipay/WeChat on the China build | Fair | Dashboard-side config not observable |
| Location-based display | **No affirmative evidence.** Terms punt: *"The payment methods supported by different payment service providers may be different, so please follow the instructions on the payment page"* | Poor | — |
| Instalments / EMI | **None evidenced** in India, Japan, Taiwan, Korea | Poor | — |
| **3DS** | **Not established** | Unknown | ⚠️ Stripe performs 3DS server-side. Bundle grep hits for `sca` were `escape`/`scaleText`. **Do not claim they lack 3DS** |
| PCI indicator | Stripe Elements iframe | Good | Consistent with SAQ A |
| Mobile | Not separately audited | Unknown | — |
| **Multi-currency** | `currency = "USD"`, `price-unit = "$<i>{price}</i>"` — **`$` hardcoded**. Credits Policy: *"Standard Pricing: $1 USD = 66 Credits"*. Stripe currency selector mounted below | **Poor at the app layer** | JP/KR do get `円`/`원` symbols in the `currency` key set; presentment below the app is unresolved |
| Saved payment methods | Yes — *"payment account bound with your User Account"*, auto-debited each cycle | Good | `/api/pay/restoreContract`, `/api/pay/uncontract` |
| **Error / dunning clarity** | **`renewal-notice` = "Your subscription is frozen. Please make sure to have enough balance in your payment account while renewal attempts are being made."** `renewal-tag` = `"Suspended"` | **Poor — and this is the hook** | Recovery pushed onto the customer |
| Enterprise checkout | Offline corporate bank transfer prepaid only; invoice + Singapore GST flow exists | Fair | No card or self-serve enterprise rail |

---

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|---|---|---|
| PCI DSS Level | **No direct PCI compliance documentation found publicly for Kling AI.** | — |
| Card data handling | `[INFERENCE, not confirmed]` SAQ A | Stripe Elements confirmed in §3A |
| Recommended Yuno integration | **SDK** | Preserves the reduced scope they already have |

`[INFERENCE, not confirmed]`: Based on confirmed use of Stripe's tokenized Elements checkout, PCI scope is likely reduced with Stripe handling card data.

---

## Section 10: Strategic Insights & Outreach Angles

> **Insight #1: A failed renewal freezes the account and hands recovery to the customer**
> **Evidence:** §8 — `renewal-notice` = *"Your subscription is frozen. Please make sure to have enough balance in your payment account while renewal attempts are being made."*, `renewal-tag` = *"Suspended"* + §5 — Trustpilot 1.2/5 across 398 reviews with named reviewers reporting **three charge attempts after a confirmed cancellation**.
> **Pain Point:** Retry and mandate state is not centrally owned. Renewals that fail for recoverable reasons — expired card, issuer soft decline, insufficient balance at the wrong moment — become frozen accounts and churned customers, while cancellations that *should* stop retrying don't. Both failure modes come from the same missing layer. At >200% growth, the absolute number of affected subscribers roughly triples a year.
> **Yuno Value Proposition:** Retry logic, network tokens and account-updater in the routing layer, with mandate state owned in one place across every PSP rather than inside one processor's defaults.
> **Best Success Case:** A global consumer-subscription business with a large emerging-market base that cut involuntary churn through smarter retries — profile-matched on churn mechanics, not on vertical.
> **Outreach Angle:** *"Your own renewal notice tells a customer their subscription is frozen and asks them to make sure there's enough balance while retries run. With India at 15% of your traffic on USD card-on-file, I'd expect that to be costing you more than it looks."*
> **Suggested Subject Line:** Frozen renewals on your India base

> **Insight #2: Your biggest and best market gets your least-built experience**
> **Evidence:** §1 — India is #1 at **15.21%**, with **20.90% audience share** and the highest pages/visit in the table (6.79) + §8/§3A — the app ships **three languages** (`["en","ja","ko"]`), `currency = "USD"`, `$` hardcoded into the price template, and **no Indian entity** (§2).
> **Pain Point:** The markets Kling localised for — Japan, Korea, China — are its #8, #3 and (separately hosted) markets. India, its largest and most engaged, gets English, dollars and a cross-border authorisation against a foreign issuer. Domestic issuers in India decline foreign-acquired transactions at materially higher rates than local-acquired ones.
> **Yuno Value Proposition:** Routing to local acquirers per geography, and one integration to add local rails without a per-rail rebuild — without standing up an Indian entity first.
> **Best Success Case:** Match on "global subscription product with a disproportionate India base billed cross-border."
> **Outreach Angle:** *"You've localised into Japanese and Korean. India is three times Japan's traffic and your strongest engagement, and it gets English and a dollar sign."*
> **Suggested Subject Line:** India is 15% of Kling's traffic

> **Insight #3: The carve-out is the moment payments stops being inherited**
> **Evidence:** §6 — **capital increase filed with HKEX 2026-07-02**, ~US$2.79bn committed at signing, Kuaishou diluted to ~68.33%, and an investor **redemption right at cost + 8% simple annual interest if there is no IPO by 30 October 2031** + §2 — **Kling AI Pte. Ltd. incorporated 17 Jan 2025, seven months after monetisation began** + §12 — the carve-out entity carries **RMB 2.4bn of cumulative losses and negative net assets** + §3A — six billing channels and one PSP.
> **Pain Point:** A separately-capitalised, IPO-track entity has to defend its own gross margin, its own approval rates and its own revenue recognition across six channels. The architecture it inherited was stood up after the revenue arrived and has never been designed.
> **Yuno Value Proposition:** One integration above the channels they already run, with reconciliation and routing owned rather than inherited — before the reporting obligations harden.
> **Best Success Case:** n/a — this is a timing argument, not a proof point.
> **Outreach Angle:** *"You incorporated the Singapore entity seven months after Kling started billing. With the carve-out filed and outside investors on the register, I'd guess the payments stack is one of the things now getting a second look."*
> **Suggested Subject Line:** ⚠️ Keep the raise out of the subject line — it reads as surveillance. Use it once, in the body.

> **Insight #4: The category has not solved this — nobody in it has orchestration**
> **Evidence:** §11C — **Runway and Luma both run single-PSP Stripe**, verbatim from their own terms; HeyGen names no PSP; Gr4vy, Spreedly and Primer customer lists contain no AI or creator-tools company + §3B — Kling is the same.
> **Pain Point:** Not a pain for Kling specifically — it is a category-wide default that nobody has revisited. The first mover on approval rates and local rails in this vertical gets an edge over competitors with identical model quality.
> **Yuno Value Proposition:** Differentiation on conversion, in a category where the product itself is converging.
> **Outreach Angle:** Use as a *supporting* line in E4, never as the opener. It is honest but it is not urgent.
> **Suggested Subject Line:** *(do not lead with this one)*

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks**
1. Your renewal notice tells customers their subscription is frozen and asks them to make sure there's enough balance while retries run.
2. India is 15.21% of your traffic and your highest-engagement market — and the app ships in English, Japanese and Korean.
3. Your price template has a dollar sign hardcoded into it.

**Cold call openers**
1. *"I had a look at how Kling handles a failed renewal — it freezes the account and asks the customer to top up. Is involuntary churn something you're measuring by market?"*
2. *"India's your biggest market by some distance. Is it billed any differently from the US?"*
3. *"You've got Stripe, PayPal, Apple, Google, an offline invoice path and an AWS Marketplace listing. Who owns reconciliation across those six?"*

---

## Section 11: Similar Companies & Prospecting Pipeline

### 11A. Direct Competitors — AI video generation
| Company | Website | HQ | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---|---|---|---|---|---|---|
| **Runway** | runwayml.com | New York, US | $315M Series E @ $5.3bn 🔴 | Global / APAC self-serve | **Stripe, Inc. — single PSP** ✅ *"The Company uses Stripe, Inc. … you agree to be bound by Stripe's Privacy Policy"* | ✅ [runwayml.com/terms-of-use](https://runwayml.com/terms-of-use) |
| **Luma AI** | lumalabs.ai | Palo Alto, US | $900M Series C @ $4bn 🔴 | Global | **Stripe, Inc. — single PSP** ✅ *"Payments are processed by Stripe, Inc. … You authorize Stripe to: (a) store your payment information, (b) continue billing your payment method even after expiration"* | ✅ [lumalabs.ai/legal/tos](https://lumalabs.ai/legal/tos) |
| HeyGen | heygen.com | Los Angeles, US | $60M Series A 🔴 | Global | **No PSP named** — only *"our payment service provider"* ✅ verified negative | ✅ [heygen.com/terms](https://www.heygen.com/terms) |
| MiniMax / Hailuo | hailuoai.video | Shanghai, CN | HKEX 0100 | China + global | See `2-ready-to-outreach/minimax-io.md` — in-house | repo |
| Synthesia | synthesia.io | London, UK | $200M @ $4bn 🔴 | Global enterprise | ❌ ToS JS-rendered | — |
| Pika · Vidu · Seedance · Veo · Sora | — | US / CN | — | Global | ❌ not established | — |

⚠️ **All funding and valuation figures for this peer set are search-snippet level from aggregators. Re-verify before any of them go in an email.**

### 11B. Industry Peers
The parent group and its short-video competitors (ByteDance/TikTok, Xiaohongshu, Bilibili, Likee) are covered in `2-ready-to-outreach/kuaishou.md`.

### 11C. Companies Recently Adopting Payment Orchestration
**"No public case studies found of direct competitors adopting payment orchestration."** Gr4vy, Spreedly and Primer customer lists were pulled directly — no AI, creator-tools or video-generation company appears on any of them.

> 🚩 **Reject on sight:** the *"Netflix +40% APAC subscriptions via orchestration"* claim. Single payments-vendor marketing page, no Netflix source. **Appears fabricated. Never use it.**

### 11D. Prospect Scoring & Top Pipeline
| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|---|---|---|---|---|---|---|---|
| 1 | **Kling AI** | Target | Global, India #1 | **23/29** | ⭐ | Dunning gap + carve-out | ✅ (add row) |
| 2 | Kuaishou (parent) | Parent | China, Brazil, ID, PK | 17/29 | ⭐ | Five PSPs, Visa ×4 | ✅ own file |
| 3 | MiniMax | Peer | China + global | 23/29 | ⭐ | In-house | ✅ own file |
| 4 | **Runway** | Direct competitor | Global | ⬜ not scored | — | **Single-PSP Stripe, verified** | ❌ **US-HQ — out of territory** |
| 5 | **Luma AI** | Direct competitor | Global | ⬜ not scored | — | **Single-PSP Stripe, verified** | ❌ **US-HQ — out of territory** |

⚠️ Competitors were not scored against the 29-point matrix — per-company signals were not gathered at that depth. Marking ⬜ rather than inventing scores. **Runway and Luma are US-HQ'd and therefore out of APAC territory** — noted as intelligence, not as leads.

---

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|---|---|---|
| **"ARR"** | **~US$500m (March 2026)** — from US$240m (Dec 2025) and US$100m (Mar 2025) | ✅ [Q1 2026 release](https://www.prnewswire.com/apac/news-releases/kuaishou-technology-announces-first-quarter-2026-unaudited-financial-results-302782902.html), verbatim, read by me. ⚠️ **See the warning below — this is not annual recurring revenue** |
| ⚠️ **What their "ARR" actually means** | **Current month's revenue × 12.** That is Kuaishou's own published definition (*"Annualized Revenue Run Rate (ARR) = Monthly Operating Revenue * 12"*), **not** annual recurring revenue. It runs **~38% above annualised realised revenue** — Q1 2026 annualises to only ~US$360m against the ~US$500m March run rate | Kuaishou's own Note 1, 2026-01-13 release |
| **Actual FY2025 revenue** | **RMB 1.04–1.1bn ≈ US$150–162m** | Corroborated. **Never present the US$240m December run rate as FY2025 revenue** |
| Carve-out entity P&L | **Net loss RMB 0.5bn (FY2024) → RMB 1.9bn (FY2025)**, RMB 2.4bn cumulative. **Negative net assets −RMB 9m** at 2025-12-31 (assets RMB 244m vs liabilities RMB 253m) | ✅ [HKEX filing](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0702/2026070204065.pdf), unaudited |
| Quarterly revenue | Q4 2025 RMB 340m · Q1 2026 **>RMB 650m (+300%)** · Q2 2026 **>RMB 850m (+200%)** · H1 2026 RMB 1.5bn | ✅ Kuaishou results releases |
| FY2025 revenue | RMB 1.04bn ≈ US$150m | ⚠️ **Caixin's figure, not a Kuaishou line** |
| GMV | N/A — subscription and API, not marketplace | — |
| Average Transaction Value | Subscription tiers **$8.80 / $32.56 / $80.96 / $159.99** per month; annual $79.20 / $293.04 / $728.64 / $1,429.99; credit packs $5–$1,200; API packages $9.80–$7,560 | ⚠️ third-party captures, not read by me off their page |
| **Monthly transaction count** | ✅ **DERIVED (bounded): >>100,000/month.** US$39.7m/month ÷ top-tier $159.99 = **248,000** as an absolute floor; at a realistic blended ~$30 ATV, ~1.3m. **Billing unit: subscription charges + credit-pack purchases.** API, marketplace and enterprise invoicing are separate and uncounted. ⚠️ Revenue sourced; ATV third-party — a bound, not a measurement | Band ≥100,000 → **+5** |
| Active Users | **60m+ creators, 600m+ videos, 30,000+ enterprise clients** (Dec 2025, primary) | ⚠️ *"100m users, 224 countries" (June 2026) is media-only and conflicts with 60m registered / 12m MAU for April 2026* |
| Paying subscribers | **Never disclosed anywhere** | — |
| Primary Currency | **USD** — `currency = "USD"`, `$` hardcoded in the price template. RMB on the China build and AWS Marketplace China | ✅ i18n manifest, read by me |
| Top 3 Markets by traffic | India 15.21% · US 11.75% · Korea 5.08% | SimilarWeb (supplied) |
| **Billing channel split (web vs app store)** | ⚠️ **NOT DISCLOSED — six channels: Stripe web, PayPal, App Store, Google Play, OFFLINE/invoice, AWS Marketplace.** The orchestrable share is unknown and this is the biggest hole in the business case | — |

---

## Overall Research Confidence

**HIGH on the payment stack, entity and financials. MEDIUM on pricing. LOW on per-market method availability.**

- **Traffic — SUPPLIED, and therefore the strongest input in the file.** Prateek's SimilarWeb dataset (2026-09-29) is the primary source, and I separately resolved the domain question by curl so the country profile is not a redirect artefact. This is why the country analysis here is materially more reliable than in the Kuaishou file.
- **Payment stack — HIGH.** The i18n manifest, Stripe component, policy documents and channel enum were all pulled and read by me, with 404-body checks. The Stripe finding is independently corroborated by a prior sweep in `minimax-io.md`.
- **Financials — HIGH, with one definitional trap.** ARR and quarterly revenue read verbatim in Kuaishou's own releases, and the carve-out is now verified at the HKEX filing. ⚠️ **But "ARR" is Kuaishou's own formula (month × 12), not recurring revenue** — see the warning in §2.
- **Carve-out terms — HIGH (primary filing).** Four widely-repeated claims about the deal were refuted against the document.
- **User numbers and pricing — LOW, and deliberately so.** A dedicated verification pass failed to confirm any claim on either. Nothing here should be quoted to a prospect without a fresh check.
- **Entity — MEDIUM.** The UEN comes from a third-party ACRA mirror; the address independently matches their own ToS.
- **Pricing — MEDIUM.** Third-party captures with drift between sources.
- **Per-market methods — LOW, structurally.** Stripe's dashboard configuration is invisible from outside. **Nothing in §4 marked "Not found" should be treated as disproved.**

---

## Manual Research Recommendations

> **Area:** What the Stripe Payment Element actually renders in India and Brazil
> **Why it matters:** It is the difference between "no UPI" (a strong, specific hook) and an email a prospect can correct in one line. This repo has already shipped one such error on another account.
> **Suggested action:** VPN to India and Brazil, open the Kling checkout, screenshot the method list. **Do this before the first email.**

> **Area:** The six-way billing-channel split
> **Why it matters:** Stripe web, PayPal, App Store, Google Play, offline invoice and AWS Marketplace. If IAP dominates, the orchestrable share is far smaller than ~$500m ARR suggests.
> **Suggested action:** Ask directly in discovery.

> **Area:** Confirm the ACRA UEN
> **Why it matters:** 202502609E comes from a third-party mirror. Fine for research, not for contracting.
> **Suggested action:** Pull the official BizFile profile (~S$5.50).

> **Area:** Whether local-currency presentment is live
> **Why it matters:** The app is USD-only, but Stripe Adaptive Pricing is mounted. If presentment is live, the FX hook weakens and the approval-rate hook stays. If not, both hold.
> **Suggested action:** Same VPN test as above — check the amount shown at the final step.

> **Area:** Current pricing, read off their own page
> **Why it matters:** All tier prices here are third-party, with drift on Ultra ($128 → $180).
> **Suggested action:** Open kling.ai/membership in a browser and screenshot it.

---

## Appendix: All Source URLs

**Their own documents:** [payment-policy](https://kling.ai/docs/payment-policy) · [user-policy](https://kling.ai/docs/user-policy) · [privacy-policy](https://kling.ai/docs/privacy-policy) · [point-policy](https://kling.ai/docs/point-policy) · [dev/pricing](https://kling.ai/dev/pricing)

**Source code:** live i18n manifest `kling-ai-web.production.18cac1432bed9628.json` · `kling-web/assets/js/PayStripeComponent-BGhR4Kpi.js` · `ComponentPaymentV2-BLrTwZKL.js` · `MembershipViewV2-BBeRzs-W.js`

**Financials:** [Q1 2026](https://www.prnewswire.com/apac/news-releases/kuaishou-technology-announces-first-quarter-2026-unaudited-financial-results-302782902.html) · [Q2/Interim 2026](https://www.prnewswire.com/news-releases/kuaishou-technology-announces-second-quarter-and-interim-2026-unaudited-financial-results-302855081.html) · [FY2025](https://www.prnewswire.com/news-releases/kuaishou-technology-announces-fourth-quarter-and-full-year-2025-financial-results-302724627.html)

**Corporate:** [TechNode — $3bn round](https://technode.com/2026/07/03/tencent-joins-reported-3-billion-funding-round-for-kuaishous-kling-ai/) · [SCMP — spin-off](https://www.scmp.com/tech/article/3353214/kuaishou-stock-surges-reports-kling-ai-unit-spin) · ⚠️ [RecordOwl ACRA mirror](https://recordowl.com/company/kling-ai-pte-ltd)

**Channels:** [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-6636lqgc4tu2w) · [AWS Marketplace China](https://awsmarketplace.amazonaws.cn/marketplace/pp/prodview-hknqxyvq35qz2)

**Complaints & UX:** [Trustpilot](https://www.trustpilot.com/review/klingai.com) · [note.com — Japan walkthrough](https://note.com/yappyinsta/n/n01dd90acf143) · [Kling AI card announcement](https://x.com/Kling_ai/status/1821172427797516475)

**Peers:** [Runway ToS](https://runwayml.com/terms-of-use) · [Luma ToS](https://lumalabs.ai/legal/tos) · [HeyGen Terms](https://www.heygen.com/terms)

**Traffic:** `accounts/traffic/kling-ai.md` (SimilarWeb, supplied 2026-09-29)

</details>
