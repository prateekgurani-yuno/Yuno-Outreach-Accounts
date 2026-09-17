# bitFlyer

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 15 / 29 → 🔴 **Low** — *downward analyst override applied; arithmetic says 15 (🟢 Medium). See the override.*
**Industry:** Crypto & digital assets (retail exchange) · **HQ:** Tokyo, Japan (株式会社bitFlyer, under bitFlyer Holdings, Inc.) · **Researched:** 2026-09-17 · **First email sent:** —
**Motion:** **Greenfield on paper — but greenfield in the sense of *nothing to orchestrate*, not an unserved opportunity.**

---

> ## ⚠️ READ BEFORE DRAFTING ANY OUTREACH
>
> **bitFlyer accepts no card payments anywhere in the group, and has not since 2018.** Japan is bank transfer / quick deposit / konbini. The US is **wire only** — they explicitly cannot take ACH. The EU is SEPA transfer, with PayPal switched off.
>
> There is **no multi-PSP estate to route, no card approval rate to lift, no MDR to reduce, and no APM gap to close.** The orchestrator check returns "none detected" because there is nothing there — not because an opportunity is sitting unserved.
>
> **The reason cards are off is a card-scheme and issuer policy decision on crypto, which Yuno cannot reverse.** Verified at source, below.
>
> This is written up in full because the reasoning is the value. **Do not run `/full-outreach` on it without a deliberate decision from Prateek.**

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** bitFlyer is Japan's largest independent cryptocurrency exchange — #1 in domestic BTC trading volume for ten consecutive years by its own JVCEA-derived count — operating regulated entities in Japan, the United States and the European Union. It is a **lean, domestic-retail, bank-rail business**: 60 employees, ¥1.05tn of customer assets in custody, 99.98% of Japanese exchange accounts held by domestic residents, and fiat moving exclusively over bank transfer, Pay-easy quick deposit and convenience-store cash.

**SimilarWeb total visits:** ~2.3M/month (Aug 2026, 3-month average, +11.37% MoM) — Japan **91.52%**, US 1.15%. `[ESTIMATE, not confirmed]` — modelled, not measured, and **it misses the mobile app entirely**, which is where most exchange activity sits. Not used for anything load-bearing here.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | **Japan** | **91.52%** `[EST]` | 銀行振込 (SMBC, ドコモSMTBネット銀行, GMOあおぞら) · **クイック入金** (ドコモSMTB free, others ¥330) · **コンビニ** ¥330 (Lawson, FamilyMart, MiniStop, Daily Yamazaki, Seicomart) | **Cards — deliberately terminated 2018.** No PayPay/wallet/QR. **No 7-Eleven.** 楽天銀行 Pay-easy suspended | ✅ 株式会社bitFlyer — 暗号資産交換業者 関東財務局長 第00003号 |
| 2 | United States | 1.15% `[EST]` | **Wire transfer only** — *"we are not able to accept ACH transfers"* | ACH, cards, everything else | ✅ bitFlyer USA — NMLS 1528491, **49 states + DC** |
| 3 | EU / Luxembourg | <1% | **Bank transfer** + PayPal *(Currently Unavailable)* | Cards, iDEAL, SEPA DD, everything else | ✅ bitFlyer EUROPE S.A. — **MiCA CASP, CSSF, Jun 2026** |
| 4 | India | 0.32% `[EST]` | — no service | — | ❌ |
| 5 | France | 0.31% `[EST]` | served via EU entity | — | via Luxembourg |

### Legal entities
- **株式会社bitFlyer** (Tokyo) — 暗号資産交換業者 **関東財務局長 第00003号**; 金融商品取引業者 **関東財務局長（金商）第3294号**; JVCEA member. **100% held by bitFlyer Holdings** (10,000 shares, at 31 Dec 2025)
- **bitFlyer Holdings, Inc.** — parent
- **bitFlyer USA, Inc.** — FinCEN MSB 31000245897927, NMLS 1528491, NYDFS BitLicense
- **bitFlyer EUROPE S.A.** (Luxembourg) — Payment Institution licence since Jan 2018; **MiCA CASP granted 2026-06-30**
- **Custodiem, Inc.** — **the former FTX Japan K.K.**, acquired outright Jul 2024, renamed Aug 2024. Institutional custody
- **bitFlyer Blockchain, Inc.** — "miyabi" private chain. Not the exchange
- **bitFlyer ASIA Pte. Ltd.** (Singapore, inc. 2015) — no current activity found; `[INFERENCE, not confirmed]` dormant

### Known PSPs
- ⚠️ **None named anywhere.** The quick-deposit / Pay-easy / konbini bundle runs through what bitFlyer calls only *"提携収納機関"* (partner collection institution) — **the 収納代行 processor is never named** in the FAQ, ToS, fee page or 特商法 page. This is the single most valuable unknown on the account.
- **No card acquirer — because there is nothing to acquire.** A Japanese vendor sweep (GMO / SBペイメントサービス / Veritrans / KOMOJU / DGフィナンシャルテクノロジー / ZEUS / ソニーペイメント) found nothing.
- **Partner banks:** 三井住友銀行 (SMBC — the payout/settlement bank), **ドコモSMTBネット銀行**, GMOあおぞらネット銀行. Quick deposit also via イオン銀行, PayPay銀行, and Pay-easy across 三菱UFJ/三井住友/みずほ/りそな.

### Orchestration status
**None detected — direct bank integrations only.** Zero hits across Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY, BR-DGE, Yuno, "payment orchestration" and "決済オーケストレーション".

> ⚠️ **This is the key nuance in the whole file.** "None detected" here means **there is no multi-provider estate to orchestrate**, not that an opportunity is unserved. See the override in Section 3.

### Buying signals
- 🚀 **MiCA CASP licence, 2026-06-30** — first Japan-origin exchange licensed under EU crypto regulation, passportable across 27 states
- 🚀 **bitFlyer USA added West Virginia, Jun 2026** → 49 states + DC
- 🤝 **bitFlyer Prime announced 2026-07-13** — prime brokerage for institutions and corporates, **service launch planned 2027**. OTC by bitFlyer KK, custody by Custodiem. *The one genuine new-build with a real buying trigger*
- 💼 **入出金オペレーション (JPY deposit/withdrawal operations) role open** — brief includes *"確認、照合、処理"*, *"エラー、差戻し、イレギュラーケースの一次確認"* and *"エラー削減、処理スピード改善"*. **Manual fiat reconciliation and exception handling.** Also **トレジャリー** roles. Notably: **zero** payment-platform, PSP-integration, card or billing engineering roles across all 71 open positions
- 📋 **IPO preparation is real but unannounced** — an **IPO準備室** job posting, a 9,407.5:1 share consolidation on 2025-03-28, EY as auditor. **No timing, venue or listing entity announced.** Treat as circumstantial

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated — and **not recommended** on current evidence. See the override in Section 3. If Prateek decides to proceed anyway, the only defensible angles are fiat reconciliation, the switched-off EU PayPal rail, and bitFlyer Prime's 2027 launch — not approval rates, MDR or APM coverage.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 15 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5 ⚠️** | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. [ASSUMPTION — not researched.]** See the full disclosure below. **This assumption scores its band but cannot and does not reject or carry the account.** |
| Orchestration status | **+4** | ✅ "None detected" on the letter of the rule. **But this award is the single clearest false positive in the matrix** — see the override. |
| 3+ countries | **+3** | ✅ Three regulated operating entities confirmed: Japan, US (49 states + DC), EU (MiCA). |
| Multiple PSPs | **0** | ⬜ **No PSP is named anywhere.** The 収納代行 behind quick deposit/konbini is undisclosed. Partner *banks* are not PSPs. |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ Japan is the home market and the domestic rail set is complete for this vertical (bank, Pay-easy, konbini). **No sourced rail gap exists.** |
| Recent expansion | **+2** | ✅ MiCA CASP (Jun 2026) and West Virginia (Jun 2026), both inside 12 months. |
| Payment issues reported | **0** | ⬜ A structural 168-hour funds lock and fee complaints were surfaced, but **every supporting page was unfetched** — all `[UNVERIFIED]`. Not scored. |
| Funding >$10M | **0** | ❌ No round in the last 12 months. The ACA Group approach was **2022 and abandoned**; the May 2026 JPYC transaction is unconfirmed in direction and size. |
| High traffic outside home | **0** | ❌ Japan is **91.52%** of traffic — far above the 60% threshold. |
| Competitor using orchestration | **0** | ❌ **No crypto exchange anywhere** was found publicly using any orchestrator. No urgency angle exists and none should be manufactured. |
| Payment job postings | **+1** | ✅ 入出金オペレーション (JPY deposit/withdrawal ops) and トレジャリー roles open. |

**Tier:** arithmetic **15 / 29 → 🟢 Medium**. **Overridden down to 🔴 Low.**

---

#### 🔻 ANALYST OVERRIDE — applied, downward

The matrix is arithmetic; judgement outranks it. Two of the override conditions fire at once:

**1. The matrix is producing a false positive on orchestration status.** The +4 is awarded for *"no orchestrator detected"* — but the reason none is detected is that **bitFlyer has no card acceptance and no alternative-payment acceptance in any of its three geographies.** There is no PSP estate to route between. The rule was written to reward a merchant running multiple direct PSP integrations without a routing layer. bitFlyer runs *bank transfers*. Awarding greenfield points here inverts the signal's meaning.

**2. Regulatory/commercial reality blocks the core pitch.** Card purchase of crypto was terminated on **9 March 2018** — verified at source — *"because of a policy change by the card companies we contract with"* (契約しているカード会社の仮想通貨購入に関する方針変更のため). This is a card-scheme and issuer stance on crypto MCCs, not a routing problem, not a provider problem, and **not something orchestration can reverse.**

Strip those out and what remains — bank-file reconciliation, treasury operations, a 収納代行 with no redundancy — is a real operational pain but is **not the product Yuno sells**. Three separate research passes reached this conclusion independently, and two of them recommended against advancing the account.

**What would change this verdict:** confirmation that **bitFlyer Prime** (institutional, launching 2027) involves corporate fiat settlement across the US and EU entities, or confirmation of the **May 2026 JPYC stablecoin transaction**. Either would create a genuine multi-market payment build. Both are currently unestablished.

---

#### Monthly transaction count — mandatory disclosure

> ⚠️ **NOT FOUND — ASSUMED ~300,000–1,800,000 fiat transactions/month. `[ASSUMPTION — not researched.]`**
>
> **This is an assumption, not a measurement, and not a derivation.** Stating that plainly is the point.
>
> **Why nothing could be sourced — this is a hard negative, not a thin search:**
> - **JVCEA publishes no transaction counts at all.** Its monthly member statistics table has columns for 数量 (coin quantity) and 金額 (yen value) only — there is **no 件数 column**. The string `件数` appears **zero times** in the full FY2024 annual report.
> - **JVCEA data is industry-aggregate across ~30 members — there is no per-exchange breakdown.**
> - The one fiat-flow series that exists (JVCEA FY2024 annual report p.32, 「入出金状況月次推移」) is **an unlabelled bar chart**; only the axis gridlines (0 / 3,000 / 6,000 / 9,000 億円) are in the PDF text layer. Industry-wide monthly fiat flows top out around **¥900bn/month**, and that is the only extractable fact.
> - **bitFlyer's own FSA disclosure contains nothing** — zero hits for 件数, 取引高, 口座, 預託, 入金, 出金, ユーザー.
> - bitFlyer publishes a **rank** (#1 in domestic BTC volume, ten years running) but **never an absolute figure**.
>
> **Basis for the assumption, so it can be argued with:** JVCEA reports **8,858,935 active accounts** industry-wide (July 2026). If bitFlyer — the largest independent, #1 by BTC volume — holds 10–20% of active accounts, that is 0.9M–1.8M accounts. At a fiat deposit or withdrawal every one to three months per active retail user, monthly fiat transactions land in the 300k–1.8M range. **That is three stacked assumptions and should be treated as a shape, not a number.**
>
> **Billing unit being counted: JPY deposits and withdrawals** — the Yuno-relevant unit. **Not crypto trades**, which are orders of magnitude higher and are not a payment transaction. And note the sting: even if the count is large, **these are bank transfers and konbini cash payments, not card transactions** — so a high count does not translate into addressable volume here.

### Source Notes
- ✅ **Audited FY2025 financials** — 事業報告（第12期）pulled from the archive and read directly.
- ✅ **The enumerated JPY fee schedule** — fetched by me from `bitflyer.com/ja-jp/s/commission`, archive capture **2026-08-31**, so current.
- ✅ **Card termination verified at source** — ITmedia, 2018-03-06, fetched and read.
- ✅ **The bank rename verified at primary source** — see the correction below.
- ⚠️ **bitflyer.com is behind Akamai Bot Manager** (`/akam/13/pixel_` in the archive). WebFetch → 403; curl → empty reply or HTTP/2 INTERNAL_ERROR. **All first-party content here came via `web.archive.org` with `curl --compressed`.** Their Next.js bundles use **hashed i18n keys**, so strings are not recoverable from JS.
- ❌ **A "3 million registered users" figure was surfaced and rejected** — it circulates on affiliate sites with no primary source. The newest *official* figure is **2.5 million group-wide, announced 11 March 2020** — six and a half years stale. **Do not use either.**
- ❌ **An "ACA Group acquiring bitFlyer" line was surfaced and rejected as current news.** It is **2022**, the founder publicly opposed it, and it did not complete — Kano is CEO today.

> ### 🔧 CORRECTION CARRIED FROM THIS RUN — do not write 住信SBIネット銀行
> An early pass identified bitFlyer's free-deposit bank as **住信SBIネット銀行** and built a competitive argument on it belonging to SBI — a rival exchange's parent. **That is out of date.** Verified against [the bank's own release](https://www.netbk.co.jp/contents/company/press/2025/1219_004783.html) and [NTT Docomo's](https://www.docomo.ne.jp/info/news_release/2025/12/19_00.html): it became a **Docomo consolidated subsidiary on 2025-10-01** and was renamed **株式会社ドコモSMTBネット銀行 on 2026-08-03**, under joint Docomo / 三井住友信託銀行 control. **SBI has exited entirely.** bitFlyer's current fee page already uses the new name; older FAQ pages still say the old one.

### Success Case Alternatives
- **Deliberately none selected.** The honest position: no streaming, crypto or exchange orchestration case study was found anywhere, and this account's payment surface does not match the profile of any case in the library. Picking one would be reverse-engineering a fit.

---

## Executive Summary

bitFlyer is Japan's largest independent crypto exchange — ¥13,567M FY2025 revenue (down 9.0%), ¥2,461M net income (down 67%), ¥1.05tn of customer assets, and **60 employees**. Its payment surface is unusually narrow: JPY in via bank transfer, Pay-easy quick deposit and konbini cash; US via **wire only**; EU via SEPA transfer with PayPal switched off. **Card acceptance was terminated across the group on 9 March 2018 on card-company policy grounds and has never returned.** The orchestrator check returns greenfield, but with nothing to orchestrate — so the motion is **Greenfield in name and weak-fit in substance**, and the account is overridden down to 🔴 Low despite scoring 15/29 on arithmetic.

### Section 1: Website Traffic Analysis by Country

**Data source:** WebSearch fallback against SimilarWeb — **path 3 of 3**. Everything here is `[ESTIMATE, not confirmed]`.

| Rank | Country | Share | Est. Monthly Visits | Source |
|---|---|---|---|---|
| 1 | Japan | **91.52%** | ~2.1M | SimilarWeb, Aug 2026 `[EST]` |
| 2 | United States | 1.15% | ~26k | `[EST]` |
| 3 | India | 0.32% | ~7k | `[EST]` |
| 4 | France | 0.31% | ~7k | `[EST]` |

Total ~2.3M visits/month (+11.37% MoM). Global rank #27,353; Japan rank #1,928. Bounce 43.42%, 4.12 pages/visit, 4m25s.

> ⚠️ **Two limits, both material.** This is modelled, not measured. And **it misses the mobile app**, where most exchange activity happens — so it under-represents the business and must never be used as a transaction proxy.

### Section 2: Legal Entities & Local Presence

**Headquarters:** Tokyo, Japan. 株式会社bitFlyer, founded 2014, capital ¥4,100,238,000 incl. reserve. Auditor **EY ShinNihon**.

| Country | Entity | Registration | Source |
|---|---|---|---|
| Japan | 株式会社bitFlyer | 暗号資産交換業者 関東財務局長 **第00003号** · 金商 **第3294号** | Site footer + fee page, 2026 capture |
| Japan | bitFlyer Holdings, Inc. | 100% owner (10,000 shares) | FSA disclosure 【2025年12月期】 |
| USA | bitFlyer USA, Inc. | FinCEN MSB 31000245897927 · NMLS 1528491 · NYDFS BitLicense | bitflyer.com/en-us/states |
| Luxembourg | bitFlyer EUROPE S.A. | Payment Institution (Jan 2018) · **MiCA CASP 2026-06-30** | CSSF / AMF CASP white list |
| Japan | Custodiem, Inc. | ex-FTX Japan K.K., acquired Jul 2024 | bitflyer.com/pub/20240726-… |

**Cross-Border Gap Analysis:**

| Country | Top market? | Local entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---|---|---|---|---|
| Japan | ✅ #1 | ✅ yes | n/a — licensed locally | **Low** |
| USA | #2 | ✅ yes | Licensed per state | **Low** |
| EU | #3 | ✅ yes | MiCA-licensed | **Low** |

> **No cross-border warning applies.** bitFlyer holds a licensed operating entity in every market it serves, and **99.98% of Japanese exchange accounts are held by domestic residents** (JVCEA FY2024). **The cross-border approval-rate argument — the most common Yuno opening — does not apply to this account at all.** Recording that explicitly so nobody reaches for it.

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Region | Provider | Evidence Type | Source |
|---|---|---|---|
| Japan | **Unnamed 収納代行** — *"提携収納機関"* | `[Terms/Privacy Policy]` | Not named in FAQ, ToS, fee page or 特商法 page |
| Japan | 三井住友銀行 (payout/settlement bank) | `[Checkout]` fee schedule | `/ja-jp/s/commission`, capture 2026-08-31 |
| Japan | ドコモSMTBネット銀行, GMOあおぞらネット銀行 | `[Checkout]` | FAQ 6-15, capture 2026-08-31 |
| Global | **No card acquirer — none exists** | `[Press Release]` | ITmedia 2018-03-06 |

**Two card-adjacent things that are NOT acquiring. Do not confuse them:**
1. **bitFlyer クレカ is an *issued* co-brand credit card**, Mastercard, **issued by 株式会社アプラス (APLUS)**, launched Dec 2021, contactless added Oct 2025. Their own homepage describes it as *"決済額に応じて、ビットコインがキャッシュバックされるクレジットカードです"* — a card that **pays Bitcoin back on spend**. This is outbound issuing. **No Yuno surface.**
2. **GMO Payment Gateway invested in bitFlyer in Sept 2014** — but the direction is the reverse of how it reads: **GMO-PG sold bitcoin acceptance to its own merchants and settled it inside bitFlyer's platform.** bitFlyer was GMO-PG's crypto rail, not its merchant. 2014 vintage; no evidence it is still live.

#### 3B. Payment Orchestrator

**None detected — direct bank integrations only.**

> *"No public evidence found of a payment orchestration platform."*

> ⚠️ **But do not read this as opportunity.** bitFlyer has **no card acceptance and no APM acceptance in any geography** — only bank transfer, a domestic Japanese quick-deposit/Pay-easy/konbini bundle, US wire and SEPA. **There is no multi-PSP estate for an orchestrator to route.** The in-house work that exists is bank-file reconciliation and treasury, not PSP routing.

### Section 4: Alternative & Local Payment Methods

| Region | Method | Category | Status | Source |
|---|---|---|---|---|
| Japan | 銀行振込 — SMBC / ドコモSMTB / GMOあおぞら, per-customer 振込先口座 | Bank transfer | **Active** | FAQ 6-15 |
| Japan | クイック入金 — ドコモSMTBネット銀行 | Bank pull | **Active, free** | Fee page 2026-08-31 |
| Japan | クイック入金 — イオン銀行, PayPay銀行, Pay-easy (三菱UFJ/三井住友/みずほ/りそな) | Bank pull | **Active, ¥330** | FAQ 6-2, 6-3 |
| Japan | **コンビニ入金** — Lawson, FamilyMart, MiniStop, Daily Yamazaki, Seicomart. **Cap ¥300,000** | Cash/voucher | **Active, ¥330** | FAQ 6-2 |
| Japan | 楽天銀行 Pay-easy | Bank pull | **Suspended** | FAQ 6-3 |
| Japan | 新生銀行 | Bank pull | **Excluded** | FAQ 6-3 |
| Japan | **7-Eleven** | Cash | **Absent from the enumerated konbini list** | FAQ 6-2 |
| Japan | **Credit/debit cards** | Cards | **TERMINATED 2018-03-09** | ITmedia ✅ fetched |
| Japan | PayPay, LINE Pay, d払い, au PAY | Wallet | **Not found** | — |
| USA | Wire transfer | Bank | **Active** | FAQ deposit_us |
| USA | **ACH** | Bank | **Explicitly refused** — *"we are not able to accept ACH transfers"* | FAQ deposit_us |
| EU | Bank transfer (SEPA) | Bank | **Active** | FAQ deposit_eu |
| EU | **PayPal** | Wallet | **"Currently Unavailable"** — no date, no reason published | FAQ 23-20 |

> **The card termination, verified at source.** ITmedia, 6 March 2018: *"クレジットカードで仮想通貨を購入できるサービスを、3月9日に停止すると発表した。「**契約しているカード会社の仮想通貨購入に関する方針変更のため**」としている。"* They had accepted **Japan-issued Visa/Mastercard**. The same article notes JP Morgan, Bank of America and Lloyds had banned card crypto purchases weeks earlier, and Zaif stopped on 9 February. **This was an industry-wide issuer/scheme stance on crypto, not a bitFlyer provider failure.**

### Section 5: Payment Issues & Customer Complaints

> ⚠️ **Every item below is `[UNVERIFIED]`** — the supporting pages were not fetched (Akamai). Not scored in the ICP.

| Issue | Rail | Frequency | Source |
|---|---|---|---|
| **168-hour (7-day) funds lock** after quick deposit or konbini from any bank other than ドコモSMTBネット銀行 — blocks JPY withdrawal and crypto send; trading allowed. Stated reason: AML source-of-funds checking | Quick deposit, konbini | **Structural** | FAQ 6-20 `[UNVERIFIED]` |
| クイック入金 受付番号 expiry / connection-drop errors forcing restart | Quick deposit | Recurring | JP guides `[UNVERIFIED]` |
| JPY withdrawal **14:30 JST cut-off**, T+1/T+2, with a manual approval step | Bank withdrawal | Structural | FAQ 6-5 `[UNVERIFIED]` |
| Deposit and withdrawal **fees** cited as the dominant negative review theme | All fiat | High | Review aggregators `[UNVERIFIED]` |

> **The 168-hour lock is the most interesting item on the account** — a seven-day funds freeze exists *because* the cheap quick-deposit rail is not trusted for AML. That is a genuine payment-experience defect. **But it is an AML/risk design choice, not a routing problem**, and it was not verifiable from a fetched page.

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | 2026-07-29 | Selected as reference exchange for the **JPX-QUICK crypto index series** | Partnership | Press index ✅ |
| 2 | **2026-07-13** | **bitFlyer Prime announced** — prime brokerage for institutions/corporates; OTC by bitFlyer KK, custody by Custodiem. **Launch planned 2027** | New product | bitflyer.com/pub/20260713… ✅ |
| 3 | **2026-06-30** | **bitFlyer EUROPE obtains MiCA CASP licence** — first Japan-origin exchange under EU crypto regulation | Licence | CSSF ✅ |
| 4 | 2026-06-30 | **bitFlyer USA live in West Virginia** → 49 states + DC | Expansion | ✅ |
| 5 | 2025-10-14 | bitFlyer credit card: contactless added; Platinum annual-fee revised | Product (issuing) | PR Times ✅ |

**Public payment RFP:** *No public payment-related RFP found.*

**Payment hiring:** **入出金オペレーション（マネージャー／メンバー）**, Roppongi — *"日本円の入金・出金に関する確認、照合、処理"*, *"エラー、差戻し、イレギュラーケースの一次確認"*, *"エラー削減、処理スピード改善"*. Plus **トレジャリー** roles. An **AI戦略** role explicitly names **ステーブルコイン決済**. Across all **71 open roles**: 決済基盤 0, カード 0, コンビニ 0, ペイジー 0. **No payment-platform or PSP-integration engineering role exists.**

### Section 7: Payment-Specific News

**No public information found.** bitFlyer has never announced a PSP, gateway, orchestration or billing-vendor partnership, and no payments trade press covers it. **Read that as absence of a payment build, not as a solved problem.**

### Section 8: Checkout Experience Audit

**Not accessible in this environment.** `bitflyer.com` is behind **Akamai Bot Manager** — WebFetch returns 403, curl returns an empty reply or an HTTP/2 INTERNAL_ERROR. Findings below are from archived captures only.

| Dimension | Finding |
|---|---|
| Checkout type | No checkout in the e-commerce sense. Funding is **bank push/pull + konbini cash**, inside an authenticated account |
| Card input | **None — no card acceptance anywhere** |
| Methods visible | Bank transfer, quick deposit, konbini (JP); wire (US); SEPA (EU) |
| Geo-adaptation | Yes — separate `ja-jp`, `en-us`, `en-eu` properties with different rail sets |
| Virtual accounts | Yes — *"お客様専用の振込先口座"* per bank; the ドコモSMTB leg uses a 5-digit reference instead |
| Recurring | **かんたん積立** — automated recurring crypto purchase, funded from the account balance |
| 3DS | **Not applicable — no cards** |
| Multi-currency | JPY, USD, EUR — one currency per regulated entity |

### Section 9: PCI DSS Compliance

**No direct PCI compliance documentation found publicly for bitFlyer.** Their compliance page covers AML/CFT only.

> `[INFERENCE, not confirmed]`: with **no card acceptance in any geography**, bitFlyer would have **no PCI scope to certify**. The absence is consistent with the stack rather than a gap. **Do not raise PCI scope reduction with this prospect** — there is nothing to reduce.

### Section 10: Strategic Insights & Outreach Angles

> ⚠️ Only three insights are offered, and each carries its own constraint. The usual angles — cross-border approval rate, MDR reduction, APM coverage, PCI scope, single-PSP failover — **all fail on this account** and are listed as dead at the end.

> **Insight #1: Manual fiat operations, evidenced by their own hiring**
> **Evidence:** Section 6 (an open 入出金オペレーション role whose brief is *"確認、照合、処理"* and *"エラー削減、処理スピード改善"*) **+** Section 3A (the 収納代行 is unnamed and single-source, with no redundancy).
> **Pain Point:** JPY in/out is reconciled and exception-handled by people, against a 14:30 cut-off with a manual approval step, at a 60-person company.
> **Yuno Value Proposition:** reconciliation and settlement-file matching across providers in one view.
> **Outreach Angle:** they are hiring for the problem, which is the cleanest possible evidence it exists.
> **Suggested Subject Line:** The 入出金 reconciliation role you're hiring for
> ⚠️ **Constraint:** this is a reconciliation and treasury argument, not orchestration. Be honest about which product it maps to.

> **Insight #2: The EU PayPal rail is switched off**
> **Evidence:** Section 4 (EU accepted methods read *"Bank transfer / PayPal (Currently Unavailable)"*) **+** Section 6 (MiCA CASP licence granted Jun 2026, passportable across 27 states).
> **Pain Point:** the one non-bank rail the group ever ran outside Japan is dark, at the exact moment the EU footprint becomes passportable.
> **Outreach Angle:** a genuine discovery question — why is it off, and what would it take to turn a non-bank rail back on across 27 markets?
> ⚠️ **Constraint:** no date or reason is published. **This is a question, not a claim** — and the EU entity routes to EMEA, not APAC.

> **Insight #3: bitFlyer Prime, launching 2027**
> **Evidence:** Section 6 (announced 2026-07-13, institutions and corporates, launch planned 2027) **+** Section 2 (three separately licensed entities across three banking ecosystems).
> **Pain Point:** an institutional product spanning JP/US/EU means corporate fiat settlement across three regimes.
> **Outreach Angle:** the only genuine new-build with a real buying trigger on this account.
> ⚠️ **Constraint:** nothing is published about its settlement design. Purely speculative until someone asks.

**Angles that are DEAD on this account — recorded so nobody reaches for them:**
- ❌ **Cross-border approval rate** — 99.98% domestic residents; licensed entity in every market served
- ❌ **MDR / cost of acceptance** — no cards to price
- ❌ **APM coverage gaps** — the Japanese rail set is complete for this vertical
- ❌ **Single-PSP failover** — no PSPs
- ❌ **PCI scope reduction** — no card scope
- ❌ **Competitive urgency** — no crypto exchange anywhere uses an orchestrator

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors
| Company | Owner | Payment stack finding | Source |
|---|---|---|---|
| **Coincheck** | Monex Group | JPY deposit accounts at **GMOあおぞらネット銀行** and **楽天銀行**; bank transfer, konbini, quick deposit | coincheck.com/ja/article/33 ✅ fetched |
| **GMO Coin** | GMO Internet | Free instant deposit, free withdrawals to ¥30m. Group owns **GMOあおぞらネット銀行** *and* **GMOペイメントゲートウェイ** | `[INFERENCE]` on in-house rails — flagged as inference, not sourced |
| **SBI VC Trade** | SBI Group | Free withdrawals; group owns 住信SBI (now Docomo SMTB). **Absorbed all DMM Bitcoin accounts 2025-03-08** | sbigroup.co.jp ✅ |
| **DMM Bitcoin** | DMM | ❌ **Dead** — wound up after the 2024-05-31 hack (¥48.2bn). **Remove from any competitor list.** | bitcoin.dmm.com ✅ |
| **bitbank** | Independent | No payment-rail information established | — |

> **The genuine competitive observation:** Coincheck (Monex), GMO Coin (GMO), SBI VC Trade (SBI) and Rakuten Wallet (Rakuten) all sit inside financial conglomerates that own a bank — and in GMO's case a PSP too. They can subsidise fiat in/out to zero. **bitFlyer is the largest independent, with no captive bank and no captive PSP**, which is consistent with fees being its dominant review complaint.
>
> ⚠️ **But note the correction above:** the argument that bitFlyer's free-deposit bank belongs to a rival's parent **no longer holds** — SBI exited that bank in Oct 2025.

#### 11C. Companies Recently Adopting Payment Orchestration
> ❌ **"No public case studies found of direct competitors adopting payment orchestration."** No crypto exchange anywhere. The only JP precedent for an exchange buying aggregated rails is **econtext → QUOINE EXCHANGE, 2017-03-23** `[UNVERIFIED]` — and QUOINE became Liquid and was wound down post-FTX. A dead reference.

### Section 12: Business Case Data

| Metric | Value | Source |
|---|---|---|
| **Operating revenue FY2025** | **¥13,567M** (−9.0% YoY) | 事業報告 第12期 ✅ audited, EY ShinNihon |
| Operating revenue FY2024 | ¥14,904M | ✅ |
| **Ordinary profit FY2025** | **¥4,415M** (FY2024 ¥9,095M) | ✅ |
| **Net income FY2025** | **¥2,461M** (−67% YoY) | ✅ |
| Total assets | ¥1,079,982M | ✅ |
| **Customer assets in custody** | **¥1,047,251M** at 31 Dec 2025 (from ¥1,178,804M) | ✅ |
| **Employees** | **60** (−15 YoY), average age 36.5 | ✅ |
| Revenue (USD) | ~US$90M `[ESTIMATE — my arithmetic at ~¥150/US$]` | — |
| **GMV / volume** | **Not disclosed.** bitFlyer publishes a rank (#1 domestic BTC, 10 years) but never a figure | — |
| Average transaction value | **Not found** — no Japanese exchange discloses this | — |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ~300k–1.8M fiat transactions/month. `[ASSUMPTION — not researched.]`** Billing unit: **JPY deposits/withdrawals**, not trades. See the full disclosure in the ICP breakdown | — |
| Active users | **Not found.** Newest official: **2.5M group-wide, March 2020** — six and a half years stale. A "3M+" figure circulates with no primary source and **must not be used** | prtimes.jp ✅ for the 2020 figure |
| Primary currency | JPY (also USD, EUR via separate entities) | ✅ |
| Billing channel split | **N/A** — no app-store IAP; exchange funding is bank rails | — |

> **This is a lean, cost-focused business in a down year.** Revenue −9%, net income −67%, headcount −15, running ¥1tn of custody with 60 people. FY2024 was the bull peak; FY2025 is the hangover. **Pitch cost and consolidation, not growth spend** — if pitching at all.

### Overall Research Confidence

**Medium-High on financials, entities and rails. Low on complaints and volume. The limits are environmental and are stated rather than papered over.**

**High confidence** (primary source, fetched and read):
- Audited FY2025 business report and the FSA disclosure, pulled from the archive and parsed
- The enumerated JPY fee schedule, capture **2026-08-31**
- Card termination — ITmedia 2018-03-06, fetched
- The ドコモSMTBネット銀行 rename — both the bank's and Docomo's own releases
- MiCA CASP, NMLS/state licences, the FTX Japan → Custodiem acquisition

**Medium confidence:** the deposit rail inventory (archived first-party FAQ, current captures, but FAQ pages not individually re-verified by me); the 71-role hiring sweep.

**Low confidence:** complaints — **every supporting page unfetched**; traffic — **WebSearch fallback only, `[ESTIMATE]`**; and **transaction volume, which does not exist publicly in any form**.

**Traffic data was ESTIMATED via WebSearch fallback** — not supplied, not API-sourced. Given Japan is 91.52% and every market has a licensed entity, the country profile does no real work in this report.

### Manual Research Recommendations

> **Area:** Monthly transaction count — **the top gap, and now a gating ICP signal**
> **Why it matters:** it is assumed, not sourced, and assumptions cannot carry or reject an account. JVCEA publishes no count column at all and gives no per-exchange split.
> **Action:** ask directly on any call. Specify **fiat deposits and withdrawals per month**, not trades — the two differ by orders of magnitude here.

> **Area:** The unnamed 収納代行 behind quick deposit, Pay-easy and konbini
> **Why it matters:** it is the only third-party payment provider in the Japanese stack, it has no visible redundancy, and it is never named in the FAQ, ToS, fee page or 特商法 page.
> **Action:** a residential-IP walk of the deposit flow with DevTools open would likely name it in minutes. The konbini set (Lawson/FamilyMart/MiniStop/Daily Yamazaki/Seicomart, **no 7-Eleven**) is a distinctive fingerprint — but **do not name a candidate without a source.**

> **Area:** bitFlyer Prime's settlement design
> **Why it matters:** the only genuine new-build on the account, launching 2027 across three regulated entities. If it involves corporate fiat settlement across JP/US/EU it is the one thing that would overturn the override.
> **Action:** read the 2026-07-13 release in full; ask on a call.

> **Area:** The May 2026 JPYC transaction
> **Why it matters:** a bitFlyer↔JPYC (JPY stablecoin) link would be the most payment-relevant thing on the account.
> **Action:** direction, size and even existence are unconfirmed — the only source is paywalled. Needs a human check. **Do not use in outreach as it stands.**

### Appendix: All Source URLs

**Primary (fetched and read):**
- https://www.itmedia.co.jp/news/articles/1803/06/news061.html — card termination, 2018-03-09
- https://bitflyer.com/ja-jp/s/commission — fee schedule, archive capture 2026-08-31
- https://bitflyer.com/pub/business-report-12th.pdf — audited FY2025 (事業報告 第12期)
- https://bitflyer.com/pub/financial-disclosure-202512.pdf — FSA disclosure
- https://www.netbk.co.jp/contents/company/press/2025/1219_004783.html — bank rename
- https://www.docomo.ne.jp/info/news_release/2025/12/19_00.html — bank rename
- https://jvcea.or.jp/statistics/information/ — JVCEA monthly member statistics
- https://jvcea.or.jp/cms2026/wp-content/uploads/2025/09/tokei_20250930.pdf — JVCEA FY2024 annual report
- https://bitflyer.com/pub/20240726-Completion-of-FTX-Japan-K.K.-Share-Acquisition-en.pdf
- https://bitflyer.com/pub/20260713-announcement-of-bitFlyer-prime-ja.pdf
- https://prtimes.jp/main/html/rd/p/000000009.000047991.html — 2.5M users, March 2020

**Secondary / URL-only:**
- https://bitflyer.com/ja-jp/faq/6-2, /6-3, /6-15, /6-20, /6-5 — deposit rails and the 168h lock
- https://bitflyer.com/en-us/faq/deposit_us · https://bitflyer.com/en-eu/faq/deposit_eu, /faq/23-20
- https://www.luxembourgforfinance.com/en/news/bitflyer-europe-secures-casp-licence-from-cssf/
- https://www.dfs.ny.gov/industry_guidance/enforcement_discipline/ea20230501_bitflyer_usa_inc
- https://news.aplus.co.jp/news/down2.php?attach_id=1766 — APLUS card issuing
- https://www.gmo-pg.com/corp/newsroom/press/gmo-paymentgateway/2014/1081.html — 2014 GMO-PG
- https://coincheck.com/ja/article/33 · https://www.sbigroup.co.jp/news/2024/1225_15139.html
- https://www.coingecko.com/en/exchanges/bitflyer · https://www.similarweb.com/website/bitflyer.com/

</details>
