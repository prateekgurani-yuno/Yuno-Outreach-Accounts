# Peach Aviation

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 22 / 29 → ⭐ **High Priority**
**Industry:** Low-cost carrier (direct-to-consumer, >95% of sales through own website) · **HQ:** Osaka, Japan — **Peach Aviation Limited**, an **ANA Holdings** subsidiary · **Researched:** 2026-09-19 · **First email sent:** —
**Motion:** **Greenfield** — no orchestration layer. But note the build culture: Peach runs a bespoke Rails + React booking stack, **holds a patent application on its own payment technology**, and has added wallets one at a time over nine years, each its own project and its own press release. There is nothing to displace; the argument is reach and opportunity cost, not "you need orchestration."

---

> ## 🎯 THE HOOK — their in-flight payment vendor went bankrupt and took card acceptance off the aircraft for five months
>
> **Peach's own notice**, `https://www.flypeach.com/news/20250901`, verbatim:
>
> > 「この度、機内決済システムの**アプリケーション開発会社から破産手続き開始の通知**を受け、同システムの継続利用が困難な状況となったため**機内決済システムの利用を停止**いたします」
>
> *"We have received notice of the commencement of bankruptcy proceedings from the application developer of our in-flight payment system, and as continued use has become difficult, we are suspending the in-flight payment system."*
>
> The timeline, from Peach's own updates to that page:
> - **2025-09-01** — onboard card payments stop. **Cash (JPY) only. No receipts or itemised statements can be issued.** Peach CARD's "10% off in-flight meals when you pay with the card" is downgraded to "10% off when you *show* the card."
> - **2025-12-08** — foreign-currency cash acceptance resumes.
> - **2026-01-26** — card payments finally resume. **A ~5-month outage of onboard card acceptance.**
>
> **The same developer took down JTA and Solaseed Air simultaneously.** Three Japanese carriers lost onboard card acceptance because one supplier filed for bankruptcy. That is single-vendor concentration risk with a date, a duration and a named business consequence — and it is Peach's own published account of it, not a third party's.
>
> ### And four months ago a payment-system change *removed* currency coverage
> `https://www.flypeach.com/news/2026052902`, and the notice is still on the live payment page today:
> > 「2026年5月29日より、**AlipayおよびWeChat Payでご利用いただける通貨は、JPY（日本円）およびCNY（中国元）のみ**となります。」
>
> Alipay and WeChat Pay **lost HKD, THB and SGD** — on routes Peach actually flies to Hong Kong, Bangkok and Singapore — with affected customers told to fall back to a credit card. Verbatim from the release: 「**決済システムの変更に伴い**」 — *"in conjunction with a change to the payment system."* Peach never said what changed or why.
>
> **Two independent, dated events in twelve months where a payments supplier — not Peach — decided what Peach could accept.**

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Peach is ANA Holdings' LCC, carrying **9.456 million passengers in FY2025** on **¥143.3bn revenue**, selling **over 95% through its own website**. It settles in **seven currencies** and accepts an unusually broad Japanese method set — including **five code wallets** that its own parent airline does not offer. It buys its own payment stack; there is no ANA-group payment platform above it.

> ⚠️ **No SimilarWeb data was supplied** and none was obtained. Market weighting below comes from Peach's own **settlement-currency matrix**, which is first-party and arguably better evidence for a payments conversation than traffic share.

### Volume — **GATE CLEARS on a sourced figure**
From **ANA Holdings' own IR deck**, 2026年3月期決算説明会資料, 2026-04-30, **page 43** (`https://www.ana.co.jp/group/investors/data/kessan/pdf/2026_04_1.pdf`):

| Metric | FY2024 | **FY2025** | YoY |
|---|---|---|---|
| 旅客数 (千人) | 9,100 | **9,456** | **+3.9%** |
| 売上高 (億円) | 1,393 | **1,433** (~US$960m) | +2.9% |
| 座席利用率 | 84.4% | 84.3% | −0.1pt |
| 単価 (円/pax) | 15,309 | **15,155** | −1.0% |

**FY2026 guidance:** 旅客数 **10,349千人 (+9.4%)**, 売上高 **¥1,595億 (+11%)**. Fleet 38 aircraft, 35 leased. ANA HD also flags a **brand renewal from April 2026** and a capacity shift from international back to domestic.

**9.456M passengers/month-averaged is ~788k passengers/month — the gate clears by a wide margin even before ancillaries.** ⚠️ **Passengers are not transactions — do not conflate them.** Peach is direct-heavy and sells per-segment ancillaries (seats, bags, changes) as separate charges, so transaction count is plausibly well above 9.456M/yr, but **there is no basis to put a number on it and outreach must not.**

### Accepted methods — first-party, from Peach's own 支払方法 matrix
Source: `https://www.flypeach.com/lm/fares/payment` — **re-fetched and verified verbatim by me, 2026-09-19.**

| Method | Currencies | Channels | Notes |
|---|---|---|---|
| **Cards** (credit/debit/prepaid) | **JPY, KRW, CNY, TWD, HKD, THB, SGD** | web · contact centre · airport (new + change) | Visa, Mastercard, JCB, Diners, Amex, Discover, **UnionPay** (SMS OTP required) |
| **コンビニ / ATM / ネットバンキング** | JPY | **web only** (× contact centre, × airport) | <¥300,000 · ≥72h before departure · **24h to pay or the booking auto-cancels** · Pay-easy institutions only · no receipt issued |
| **バーコード決済** | | | **the five wallets — see below** |
| 楽天ペイ (Rakuten Pay) | JPY | web · centre · airport | Live 2023-12-11, direct from 楽天ペイメント株式会社 |
| **PayPay** | JPY | web · centre · airport | 「あらかじめチャージされた「PayPay残高払い」のみ」 — **stored balance only, no あと払い** |
| d払い | JPY | web · centre · airport (new only, **× for changes**) | |
| Alipay | **JPY + CNY** | web · centre · airport | 「中国本土の住民票を確認済みの場合のみ」 · 「Alipay HKはご利用いただけません」 |
| WeChat Pay | **JPY + CNY** | web · centre · airport | |
| ピーチポイント | issued currency only | all four | |
| 現金 | — | **airport counter only** | |

**Payment fee:** 「*お一人ご利用区間ごとに支払手数料がかかります。」 — **charged per passenger, per segment.** Yen amounts render from JS/images and did not extract; a search summary gave ¥670 for konbini/ATM `[UNVERIFIED]`. **Do not quote a figure.**

### Sourced absences — read off the complete first-party table
**au PAY · メルペイ · Amazon Pay · Paidy · キャリア決済 · any BNPL · Apple Pay · Google Pay · PayPal · 銀行振込 · Suica / transit IC · Rakuten Edy · nanaco · WAON · 支払秘書.**

Two of these are worth naming:
- **No Apple Pay and no Google Pay on a mobile-first LCC** whose own five wallets are all barcode-based. That is a real conversion gap on the highest-intent mobile channel.
- **支払秘書 is Wellnet's own smartphone wallet**, launched on Peach in March 2019 and **no longer on the list** — a Wellnet product dropped while non-Wellnet wallets were being added.

**LINE Pay** is a nice fossil: launched 2020-11-16, since removed (consistent with LINE Pay's exit from Japan), with the logo `<li>` still **commented out in the page's markup.**

### ⚡ This account refuted my own prior conclusion — and the correction is recorded upstream
This repo previously concluded that Japanese carriers lack code wallets because **Wellnet** sits underneath them and Wellnet's e-money set stops at Rakuten Edy / Mobile Suica / JCB Premo. **Peach kills that theory.** It is a Wellnet customer (per Wellnet's own 2012-01-11 release: 「Peach Aviationとウェルネットサーバが直接接続され24時間稼動」) **and** carries five code wallets on a parallel rail.

**`ana-all-nippon-airways.md` and `japan-airlines-jal.md` have both been patched with an explicit retraction.** The replacement framing for ANA is *stronger*: the counter-example sits inside ANA's own holding company — **"your own LCC does this and you don't."**

⚠️ Wellnet's *continuation* as Peach's konbini vendor in 2026 is **strong inference, not verified** — Peach's current page names no 決済代行会社 anywhere, unlike ANA's.

### Legal entity & group position
**Peach Aviation Limited**, Osaka. ANA Holdings subsidiary; a named line item in ANA HD's segment revenue table (p.27) with two dedicated slides (pp.43–44).

**No shared payment infrastructure with ANA mainline — none found.** Separate domains, separate stacks (`flypeach.com` on Akamai + Apache/nginx + Rails + React), separate account systems (Peach アカウント and ピーチポイント, not ANA Mileage Club). **The divergent method sets are themselves the evidence**: ANA has PayPal, six-chain konbini and Apple Pay; Peach has five code wallets, UnionPay, Discover and seven settlement currencies but no Apple Pay and no PayPal. **These stacks were not built together.**

**Vanilla Air legacy: none.** Integration completed 2019-11-01; no Vanilla-era host, method or vendor is visible anywhere. Absorbing Vanilla did not leave a second payment estate behind.

**Commercial read: there is no group payment platform to displace and no group procurement to fight. Peach buys its own stack — but sits inside a holding company whose flagship has a demonstrably narrower method set. That makes Peach a reference account with unusual internal leverage.**

</details>

<details>
<summary><h2>✉️ Section 2 — Full Outreach Sequence</h2></summary>

*Not yet generated. Run `/full-outreach Peach Aviation`.*

**Before drafting:**
1. **Lead with the vendor-bankruptcy outage or the 2026-05-29 currency downgrade.** Both are first-party, dated, and describe a supplier deciding what Peach can accept.
2. **Do not claim to know Peach's gateway or acquirer.** CyberSource is confirmed for *fraud screening only*. See "what could not be established."
3. **Do not put a konbini chain count in outreach** — the chain list is image-only and the 2012 list is stale (three of those chains no longer exist).
4. **Do not quote a transaction count.** Passengers ≠ transactions.

</details>

<details>
<summary><h2>🔬 Section 3 — Full Research</h2></summary>

## Verification note
The payment page, the wallet matrix, the PayPay/Alipay restrictions and the 2026-05-29 currency notice were **re-fetched and verified verbatim by me on 2026-09-19** (HTTP 200, 113,308 bytes). The ANA HD IR figures and the Wellnet 2012 release were verified by the research agent from primary PDFs and a Wayback snapshot of Wellnet's own domain.

## 3A. PSPs, gateways, acquirers

### Confirmed, named
- **CyberSource (サイバーソース株式会社, a Visa Inc. subsidiary) — Decision Manager**, in production for card fraud screening on Peach's website since March 2019. Source: `https://paymentnavi.com/paymentnews/81886.html` (2019-03-18). The same article confirms Peach had already implemented **カード情報の非保持化** (card-data non-retention) and **本人認証 (3-D Secure)**, and states **over 95% of Peach's ticket sales come through its own website.**
  ⚠️ **CyberSource is confirmed as the fraud tool only.** Whether it is also the card gateway is **not stated and not established.**
- **Wellnet (ウェルネット株式会社)** — konbini / Pay-easy / net-banking rail. Verified 2012; continuation inferred.
- **楽天ペイメント株式会社** — named by Peach itself as the Rakuten Pay provider, live 2023-12-11 16:00 (`https://www.flypeach.com/news/20231212`).

### Checked and NOT found
**NAVITAIRE — checked hard, and the evidence points away from it.** `booking.flypeach.com` returns `server: nginx` with `x-runtime`, `x-request-id`, `_session_id` and Rails-style HMAC-signed cookies — a **Ruby on Rails** application behind a custom **React** SPA at `/react/assets/`. The booking bundle (`flight-DpHJ030P.js`) was downloaded and grepped: **zero hits** for `navitaire`, `newskies`, `dotrez` or `nsk`. **Peach does not match the HK Express / Jetstar New Skies pattern.**

A search summary asserting Peach "uses Navitaire" is `[UNVERIFIED — search summary only]` **and should be pushed back on.** Counter-evidence: the 2021-04-21 → 04-27 reservation-system outage, which Peach attributed to its platform vendor — 「障害の原因については開発元が「マルウェアの影響」と発表している」 (`https://travel.watch.impress.co.jp/docs/news/1321496.html`). ZIPAIR was down in the same window. That pattern points elsewhere, **but the vendor name was not confirmed from a primary source and is not asserted here. Peach's PSS vendor is an open item.**

**Zero hits, anywhere:** GMO Payment Gateway, SB Payment Service, Veritrans / DG Financial Technology, KOMOJU, Sony Payment Services, NTT Data / CAFIS, Adyen, Stripe, Checkout.com, Worldpay, Braintree, 2C2P.

### ⚠️ False positive caught and recorded
An initial grep of the booking bundle returned **11 hits for "eContext"** (イーコンテクスト, the DG Financial konbini processor). **Every one was a substring of React's `useContext(...)`.** Discarded. **eContext is NOT evidenced at Peach.** Recorded because it would have produced a clean-looking, entirely fabricated vendor name.

> **Running false-positive list — add:** `useContext` → **eContext**.

### Terms / privacy / CSP
- **利用者情報の外部送信について** (`https://www.flypeach.com/fm/privacy_policy/external_information`) — read in full. Lists Google LLC, 株式会社Faber Company (ミエルカヒートマップ), 株式会社Sprocket, 株式会社ジーニー, 株式会社ホワイト・ベアーファミリー. **No payment vendor is disclosed** — the statement is scoped to tracking only.
- **CSP headers: none** on either `www.flypeach.com` or `booking.flypeach.com`. **No CSP allowlist to mine for gateway hosts.** `www` is Akamai-fronted with Bot Manager (`_abck`/`bm_sz`); booking is nginx behind Akamai. Only third-party hosts on the booking page: `p11.techlab-cdn.com` (Sprocket) and Google Fonts.
- **The payment step sits behind a live booking session** and was not reached; `/payment` and `/ja/payment` both 301. **This is the single biggest gap.**

## 3B. Orchestration — None detected, on affirmative architectural evidence

Zero hits for Juspay, Spreedly, Primer, Gr4vy, CellPoint Digital, APEXX, Payrails, IXOPAY, Yuno or 決済オーケストレーション.

**This does not rest on absent hits alone.** Affirmative evidence that Peach builds payments itself:

1. **Custom booking engine** — Rails backend plus bespoke React SPA, no off-the-shelf PSS front end. Headers and bundle inspected directly.
2. **Peach holds a patent application on its own payment technology.** Per `https://paymentnavi.com/paymentnews/103785.html` (2021-03-11), Peach co-developed an in-flight server with 朝日放送テレビ and ティアック whose distinguishing feature is 「独自の技術により、衛星によるインターネット回線を使用することなく、**オフラインの状態でもクレジットカード決済が可能**」, and 「Peachは、同決済技術について、**特許を出願している**」. **An airline that patents its own payment method is building, not buying.**
3. **Serial one-off wallet integrations over nine years**, each separately announced: Alipay + UnionPay (2017-02-22), d払い (2019-12), PayPay (2020-09), LINE Pay (2020-11-16, later removed), Rakuten Pay (2023-12-11). **One connector at a time, each its own project and press release — the signature of direct integrations, not an orchestration layer.**

**The wallet rail's processor is the open question and the orchestration wedge.** Peach's five code wallets cannot be running on Wellnet (whose e-money set stops at Rakuten Edy / Mobile Suica / JCB Premo). Rakuten Pay comes direct from 楽天ペイメント. So Peach runs **at least two, probably three or more, parallel payment rails**: Wellnet for konbini/Pay-easy, something for cards with CyberSource DM on top, and one-or-many wallet connections. **Who aggregates the wallets — or whether anyone does — could not be established.**

## 3C. Incidents & complaints

**🔴 In-flight payment vendor bankruptcy — 5-month card outage.** See the hook. Peach's own notice, three dated updates. Same developer took down **JTA** and **Solaseed Air** simultaneously (`traicy.com`, 2025-08/09). **The developer's name was not disclosed by Peach, JTA, Solaseed or any trade outlet — not established.**

**🔴 Payment-system change forced a method downgrade, 2026-05-29.** Alipay and WeChat Pay lost HKD, THB and SGD. 「決済システムの変更に伴い」. **What actually changed — a PSP migration, a contract change, or something narrower — is unknown.**

**🔴 Reservation-system outage, 2021-04-21 → 04-27** (7 days), attributed by Peach to its platform vendor's malware incident.

**Payment-abandonment mechanics — where Peach structurally leaks bookings:**
- Konbini/ATM/net banking: **24h to pay or the booking auto-cancels** (first-party, verified by me).
- Cards ~10 min, **PayPay ~5 min**, provisional booking auto-cancels after ~1h, and **if the payment screen closes or errors the payment cannot be retried — the customer must rebook from scratch.** `[UNVERIFIED — search summary only; cs.flypeach.com is Cloudflare-403 to automated fetches, support.flypeach.com returned 503 on every attempt, no Wayback snapshot of the 仮予約 article.]` **"Your PayPay customers have five minutes and no retry" is a very sharp opener — verify it manually before using it.**

**User-level complaints:** low-grade card-decline reports (error code E70 on a personal blog; a Yahoo!知恵袋 thread on repeated declines across multiple cards), and a first-party FAQ article titled 「料金が二重で決済されている」 — **the existence of a dedicated double-charge FAQ is itself the signal.** All undated or poorly dated; no attributable X / 5ch / 価格.com threads retrieved. App-store review searches returned a different company's app ("Peach" clinic/salon) — **discarded as mis-hits.**

## 4. ICP Score breakdown — 22 / 29

| Signal | Weight | Score | Basis |
|---|---|---|---|
| Transaction volume | 5 | **5** | 9.456M pax FY2025, sourced from ANA HD IR p.43. >95% direct web |
| Orchestration (greenfield) | 4 | **4** | No layer. Serial point integrations, on affirmative evidence |
| 3+ countries | 3 | **3** | Seven settlement currencies: JPY, KRW, CNY, TWD, HKD, THB, SGD |
| Multiple PSPs | 2 | **2** | Wellnet + card gateway + 楽天ペイメント + wallet connections |
| Local rail gap | 3 | **2** | **No Apple Pay, no Google Pay** on a mobile-first LCC; no au PAY/Merpay/Amazon Pay/Paidy/carrier billing; Alipay & WeChat lost 3 currencies. Partial — the five barcode wallets are genuinely strong |
| Recent expansion | 2 | **2** | FY2026 guidance +9.4% pax / +11% revenue; brand renewal April 2026 |
| Payment issues | 2 | **2** | 5-month onboard card outage; 2026-05-29 currency downgrade; 2021 PSS outage; double-charge FAQ |
| Funding | 2 | **0** | ANA HD subsidiary — no funding events |
| Traffic outside home market | 2 | **2** | Seven settlement currencies; international network. Scored on currency evidence, no traffic data |
| Competitor orchestration | 2 | **0** | Not established |
| Job postings | 2 | **0** | Not established |
| **TOTAL** | **29** | **22** | ⭐ **High Priority** — second only to ANA (23) |

## 5. What could NOT be established

1. **The card gateway and the wallet processor — the biggest gap.** CyberSource is confirmed for fraud screening only. The payment step is behind a live booking session, no CSP header exists to mine, and the public bundle is the flight-search chunk only. **Nobody should claim to know Peach's acquirer or gateway from this file.**
2. **Whether Wellnet is still the konbini vendor in 2026.** Verified 2012, structurally consistent today, not reconfirmed.
3. **The konbini chain list** — image-only on both JA and EN pages (`conveni.png`, alt text 「図説：利用可能なコンビニ」), no OCR available. The 2012 Wellnet list named ローソン/ファミリーマート/サークルK/サンクス/ミニストップ/デイリーヤマザキ/スリーエフ — **three of those chains no longer exist, so that list is stale and must not be quoted.**
4. **Peach's PSS vendor.** The Navitaire claim is search-summary only and the architectural evidence contradicts a New Skies front end.
5. **The bankrupt in-flight payment developer's name.**
6. **What the 2026-05-29 「決済システムの変更」 actually was.**
7. **Merchant descriptors and transaction counts** — both need a live transaction.
8. **Payment surcharge amounts** — 支払手数料 is confirmed as per-passenger-per-segment, but the yen figures render from JS/images.

## 6. Overall Research Confidence — **MEDIUM-HIGH**

**High** on accepted methods, currencies, channel availability and the incident record — all first-party and re-verified verbatim. **High** on volume: the passenger figure comes from ANA HD's own IR deck.

**Downgraded from High because the single most important payments question — who is the gateway and who processes the wallets — is unanswered**, and because the sharpest potential opener (the 5-minute PayPay window with no retry) rests on an unverified search summary.

## 7. Phase 0 gate
Not a PSP or payment-infrastructure company — **no Partnerships routing needed.** Japan-HQ'd — **in APAC territory.**

</details>
