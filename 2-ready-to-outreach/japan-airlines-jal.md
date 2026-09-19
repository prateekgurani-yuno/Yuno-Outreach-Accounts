# Japan Airlines (JAL)

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 17 / 29 → ⭐ **High Priority**
**Industry:** Airlines (full-service, domestic + international, cargo, mileage commerce) · **HQ:** Tokyo, **Japan** — 日本航空株式会社, **TSE 9201** · **Researched:** 2026-09-19 · **First email sent:** —
**Motion:** **Greenfield** — none detected. Same architectural shape as ANA: cash rails on a third-party vendor, fraud on a separate 2015-vintage engine, card acquirer undisclosed, region-gated storefronts with different method sets.

---

> ## ⚠️ TWO PREMISES I HELD GOING IN WERE WRONG — both are corrected here
>
> **1. "JAL refuses third-party wallets" — WRONG.** My earlier JAL check (run during the ANA batch) used the **domestic** payment page only. **Apple Pay is present on the international flow** — verified by me, 3 occurrences on JAL's own international payment page. The correct statement is narrower and sharper: **JAL accepts no Japanese domestic *code* wallet** (PayPay, d払い, au PAY, Rakuten Pay, LINE Pay) anywhere found.
>
> **2. "JAL is mid-PSS-migration like ANA" — WRONG, and it inverts the angle.** JAL completed its move to **Amadeus Altéa in November 2017** — **nine years ahead of ANA**, unifying domestic and international onto one PSS. It also wound down its own GDS subsidiary **AXESS International Network** (operations ended 31 Mar 2021). **The ANA opener does not transfer.** `[Altéa dates UNVERIFIED — 2014–2019 announcements, search-summary corroborated; say "has run Altéa since 2017", not "runs Altéa today".]`

---

> ## 🎯 THE HOOK — the PSS was modernised nine years ago and the payment layer underneath it was not
>
> **JAL already paid the platform-modernisation cost and consolidated two PSSs into one.** Underneath that:
>
> | Layer | What is actually there |
> |---|---|
> | **Cash / bank rails** | **Wellnet (ウェルネット)** — a vendor running since **May 2000** |
> | **Fraud** | **NTT Data CAFIS Brain**, in full operation since **January 2015** — an eleven-year-old domestic rules engine in front of a global airline |
> | **Card acquiring** | ❌ **undisclosed — nobody can name it** |
> | **Storefronts** | **region-gated POS sites with different method sets per region** |
>
> ### ★ AND THE CATEGORY FINDING — Wellnet is why neither JAL nor ANA takes PayPay
>
> **✅ Verified by me directly, and it explains an absence I previously could only describe.**
>
> JAL's own international payment page links its financial-institution list to **`multiple-payment.biz`** — and that domain is **the only non-analytics third party on the entire page** (everything else is Google Fonts, Akamai mPulse, social links and JAL's own domains). I fetched it: it is titled **「ウェルネット（WELLNET）マルチペイメントサービス」**.
>
> Wellnet's own copy, verbatim:
> > 「2000年5月から稼動開始。**国内主要航空会社の全て**、主要高速バス会社、その他大手通信販売などで現在もご利用いただいている」
> > — *"In operation since May 2000. Used by **all of Japan's major domestic airlines**…"*
>
> **And here is the constraint.** Wellnet's complete method set, from its own FAQ:
> > 「クレジットカード/コンビニ(現金）/ATM(ペイジー)/ネットバンク/**電子マネー(楽天Edy,モバイルSuica,JCBプレモ)**/支払秘書」
>
> **The e-money list tops out at Rakuten Edy, Mobile Suica and JCB Premo. There is no PayPay. There is no code wallet of any kind.**
>
> 📌 **So the reason ANA and JAL both lack Japan's dominant wallet is not preference — it is that the vendor carrying their cash and bank rails does not offer it.** That is a far better observation than "you don't take PayPay," it is true of the whole category, and it reframes the conversation from a missing feature to a structural ceiling.
>
> ⚠️ **Precision, because it matters:** I verified that **JAL links to Wellnet for the Pay-easy / net-transfer institution list**. I did **not** observe a full-page Wellnet redirect in a live JAL checkout the way I did for ANA, and **Wellnet's own case-study page names bus operators and a baseball stadium — not JAL.** The airline claim is generic on Wellnet's homepage. **Say "the same vendor sits behind both carriers' cash rails", not "JAL redirects to Wellnet".**

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** JAL is Japan's second-largest carrier. **FY2025 (year ended 31 Mar 2026) revenue ¥2,012,515 million — ¥2.01 trillion, +9.1%, the first time above ¥2 trillion since the 2012 relisting.** EBIT ¥218,004m (+26.4%), net income attributable ¥137,604m (+28.6%) — all records.

**SimilarWeb total visits:** **Not obtained.** No data supplied, and `jal.co.jp` returns **HTTP 403** to both curl and WebFetch. Country profile unverified; **no split invented.**

### ❌ THE STUB'S REVENUE FIGURE IS REFUTED
The stub and the target list both say **$11.4B**. ✅ **I extracted the primary 決算短信 myself:** revenue is **¥2,012,515m**, which at ¥149–155/USD is **~US$13.0–13.5bn**. Getting to $11.4B needs ~¥176/USD, which did not prevail in the period. **The stub figure is stale — the prior year was ¥1,844,095m. Use the yen figure primarily**, which matters anyway given JAL prices in multiple currencies.

### Accepted methods — verified by me on BOTH flows
| Method | Domestic | International (Japan region) |
|---|---|---|
| **クレジットカード** | ✅ | ✅ **with 多通貨決済 (MCP) — customer picks the settlement currency, JAL applies its own FX conversion fee** |
| **Apple Pay** | ❌ **absent** | ✅ **present** — Amex, Mastercard, Visa. Carve-out: *"JALカードはMastercardのみ"* |
| **e JALポイント** | ✅ | ✅ full or partial, remainder on card |
| **コンビニ（現金）** | ✅ | ✅ **JMB members only** — Lawson, FamilyMart, Seven-Eleven; cutoff 10 days before departure |
| **銀行・郵便局ATM (Pay-easy)** | ✅ | ✅ |
| **インターネット振込** | ✅ | ✅ **two distinct rails** — Pay-easy 払込 (Mizuho, MUFG, SMBC, Suruga, Yucho) *and* インターネット振込サービス (PayPay銀行, 楽天銀行, 住信SBI, auじぶん) |
| **JAL旅行券** | ✅ phone only | ✅ phone only |

> ⚠️ **TRAP, and it is the same one as ANA: 「PayPay銀行」 is PayPay *Bank*, in the net-banking list. NOT the wallet.** One occurrence on the page. Do not misread it.

### ❌ Sourced-absent from BOTH flows
**PayPay · Rakuten Pay · LINE Pay · d払い · au PAY · Amazon Pay · Paidy · Google Pay · any at-checkout instalment (分割/リボ)** — instalment conversion is **post-purchase and issuer-side only**.

⚠️ **BUT the Japan-region page is not the whole international story.** JAL runs **region-gated POS sites** with different method sets, proven by JAL's own JAL Pay terms excluding 「海外地区でのご購入」 as a separate channel. A live JAL FAQ article exists titled 「**国際線｜Alipayで購入する際に…**」 — JAL would not publish Alipay troubleshooting for a method it does not accept. **Alipay is strong-signal; UnionPay and PayPal are search-summary only and unconfirmed.** Regional FAQ origins found: `jal-cn-jp`, `faq-en`, `faq-sr`, `faq-ar-en`, plus a `jal.co.jp/world/en/` site. **None could be read.**

### 💳 JAL Pay — the real ANA differentiator, and it is subtler than it looks
- ✅ **It does buy tickets on jal.co.jp** — double base miles when used, on JAL/JTA/JAC/RAC tickets bought on the **Japan-region site**, Japan counters or Japan reservation centres.
- 📌 **But it is not a separate checkout button. It is a Mastercard prepaid credential** — it rides the existing card rail or Apple Pay. JAL's own page excludes 「コード決済やタッチ決済など」 from the bonus. That is why it does not appear as a method on the payment page.
- **Operator: JALペイメント・ポート株式会社** — a **JAL × SBI Holdings** joint venture. **Banking layer: 住信SBIネット銀行**, JAL holding a banking-agency licence 関東財務局長(銀代)第336号.
- **Merchant descriptors it settles against are informative** — 「JAL国内線航空券類」「JAL国際線航空券類」「日本航空 国際線チケットレス」「日本航空 国際線自動発売機」「日本航空 **国際線サインレス**」. **Separate international signature-less and ticketless descriptors imply distinct international CNP acquiring from domestic.**

> **Read the posture correctly.** JAL is not a wallet refusenik — it accepts Apple Pay, very likely Alipay in-region, and **runs its own Mastercard-rail prepaid programme with a bank JV.** What it does not accept is any **Japanese code wallet** — while JAL Pay itself has code-payment capability at other merchants. **Combined with the Wellnet constraint above, the honest read is: the cash-rail vendor cannot carry code wallets, and JAL has its own wallet it would rather you used.**

### Known PSPs
| Layer | Finding |
|---|---|
| **Cash / Pay-easy / net banking** | ✅ **Wellnet** — verified via JAL's own outbound link; see the Hook, and read the precision caveat |
| **Fraud** | ✅ **NTT Data CAFIS Brain**, live since **January 2015**, from JAL's own press release |
| **PSS** | ✅ **Amadeus Altéa** since Nov 2017 |
| **Card gateway / acquirer** | ❌ **NOT ESTABLISHED** — the single biggest hole |

❌ **Searched, no evidence found:** GMO Payment Gateway, SB Payment Service, Veritrans/DG Financial, KOMOJU, Sony Payment Services, Adyen, Stripe, Checkout.com, Worldpay, Cybersource, Braintree, Accelya, CellPoint Digital. **Unchecked-absence, not sourced-absence.**
⚠️ **A 2017 JAL Card notice about a GMO-PG data-leak incident on unrelated government sites is NOT evidence of a JAL–GMO-PG relationship. Do not use it.**

### Buying signals
- 🏗️ **PSS modernised 2017; payment layer beneath it is 2000-vintage cash rails and a 2015 fraud engine**
- 🌏 **Region-gated storefronts with different method sets** — almost certainly different integrations per region
- 💱 **MCP multi-currency with JAL's own FX conversion fee** — they are already in the FX business on their own checkout
- 💳 **JAL Pay / JAL Payment Port (JAL × SBI)** — an active fintech build-out, and a banking-agency licence
- 🔴 **23 Dec 2025: ANA *and* JAL simultaneously unable to take reservations or issue tickets** (Nikkei). **Both carriers, same day — points at a shared upstream.** `[UNVERIFIED — paywalled, not fetched]`
- 🔴 **26 Dec 2024: JAL Pay transaction failures** — JAL's own notice, 「一部のお取引が成立していない事象」
- ✈️ **Hawaiian Airlines partnership ENDS 21 Apr 2026**, transferring to Alaska after the HA/Alaska merger

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Japan Airlines (JAL)` to draft the 12-touch sequence.*

**Five instructions for whoever drafts it:**
1. **The opener is the modernisation asymmetry**: the PSS was consolidated in 2017 and the payment layer underneath it wasn't. It is flattering about the hard thing they did and observational about the thing they didn't.
2. **The Wellnet constraint is the second observation and it is the category insight** — the vendor behind the cash rails tops out at Rakuten Edy, Mobile Suica and JCB Premo. **Frame it as "the rail set looks vendor-bounded," never as "you don't take PayPay."**
3. ⛔ **Do NOT reuse the ANA opener.** JAL finished its migration nine years ago. Claiming otherwise would be instantly wrong to anyone there.
4. ⛔ **Do NOT say JAL refuses wallets.** Apple Pay is live on international. The accurate claim is **no Japanese code wallets**.
5. **The Dec 2025 dual-carrier outage is potentially the best cold open in the batch — but it is paywalled and unverified. Verify before using it.**

**Never claim:** any card gateway or acquirer (none established), UnionPay or PayPal acceptance (search-summary only), that JAL redirects to Wellnet (implied, not observed), or the $11.4B revenue figure (refuted).

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 17 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED as a bound, from a primary filing I extracted myself.** **Revenue ¥2,012,515m FY2025.** Even at an implausibly high **¥300,000 (~US$2,000) per booking**, that is ~6.7m bookings/year = **~560k/month**, and ancillaries bill separately. **Every plausible divisor clears 100k by a wide margin.** ⚠️ Passengers, international/domestic split and cargo share could NOT be obtained — so no passenger-derived figure is offered. |
| Orchestration status | **+4** | ✅ **None detected.** Same shape as ANA: a third-party vendor on cash rails, a separate 2015 fraud engine, an undisclosed card acquirer, and region-gated POS sites with differing method sets. ⚠️ Rests partly on absent hits for the card layer, but the **region-fragmented method sets are affirmative** evidence of per-region integration rather than one routed layer. |
| 3+ countries | **+3** | ✅ International network, **MCP multi-currency pricing**, and at least four regional FAQ/POS origins (`jal-cn-jp`, `faq-en`, `faq-sr`, `faq-ar-en`) plus a `world/en` site. |
| Multiple PSPs | **+2** | ✅ **Structurally proven:** Wellnet on the cash/bank rails is demonstrably not the card acquirer, and JAL's own JAL Pay descriptors show **separate international "サインレス"/"チケットレス" merchant descriptors** from domestic — implying distinct international CNP acquiring. ⚠️ Only **Wellnet** and **CAFIS Brain** can be named, and CAFIS Brain is fraud, not acquiring. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Sourced absence on both flows, verified by me.** No PayPay, Rakuten Pay, LINE Pay, d払い, au PAY, Amazon Pay, Paidy or Google Pay, and no at-checkout instalments. ⚠️ **Read the nuance before pitching:** the Wellnet e-money ceiling explains the absence structurally, and JAL runs its own competing prepaid wallet. **The gap is real; the framing must be vendor-constraint, not oversight.** |
| Recent expansion | **0** | ⬜ Not awarded. The **Hawaiian → Alaska transition (21 Apr 2026)** is a partnership change, not expansion, and new routes could not be established. |
| Payment issues reported | **0** | ⬜ **Not awarded — and this is the row most likely to move.** A strong corpus exists but **not one item was fetched**: the 23 Dec 2025 **dual-carrier ANA+JAL outage** (Nikkei, paywalled), a 26 Dec 2024 **JAL Pay transaction-failure notice** on JAL's own site, an open **JAL app v6.0.0 defect** from 15 Apr 2026, a standing FAQ where pressing the internet-transfer button 10+ times hard-errors and blocks purchase, and a standing FAQ where **Alipay payment succeeds but confirmation fails** — a textbook capture-succeeded-reconciliation-failed pattern. **I do not award points on unverified data.** Verifying any two of these likely makes this +2. |
| Funding >$10M | **0** | ❌ TSE-listed (9201). No round. |
| High traffic outside home | **0** | ⬜ No traffic data, and the domestic/international split could not be obtained. |
| Competitor using orchestration | **0** | ❌ **JAL's closest competitor is ANA, and our own ANA file scores it greenfield with no orchestration.** The honest read for a Japanese carrier is that nobody in the peer set has adopted. |
| Payment job postings | **0** | ⬜ Not found. |

**Tier: 17 / 29 → ⭐ High Priority.** No override applied.

> **Compare with ANA (23/29) deliberately.** ANA scores higher on three rows JAL cannot match — a live, publicly-apologised-for migration; verified money-movement defects; and a JV partner already running orchestration. **JAL's case is quieter and structurally cleaner: the platform modernisation is done, so the payment layer is the obvious remaining seam.**

### Source Notes
- ✅ **The international method table, Apple Pay's presence, MCP, the absence of instalments and the Wellnet outbound link were all verified by me** from Wayback snapshot `20260309053322` of `jal.co.jp/jp/ja/inter/payment/`. `multiple-payment.biz` is **the only non-analytics third-party host on that page.**
- ✅ **Wellnet's identity, its "all of Japan's major domestic airlines" claim and its complete method set were verified by me** at `multiple-payment.biz`, which is **directly fetchable with no WAF**.
- ✅ **FY2025 financials extracted by me from the primary 決算短信 PDF** (filed 2026-04-30): 売上収益 ¥2,012,515m (+9.1%), EBIT ¥218,004m (+26.4%), 親会社帰属当期利益 ¥137,604m (+28.6%), prior year ¥1,844,095m.
- ✅ **CAFIS Brain** is from JAL's own January 2015 press release.
- ⚠️ **The domestic method set** was verified by me during the ANA batch, from Wayback snapshot `20260606014023`.
- ⚠️ **Altéa dates (2017 go-live, 2019 extension, AXESS wind-down 2021)** are search-summary corroborated across multiple outlets, **not re-confirmed for 2026.**
- ⚠️ **Alipay/UnionPay/PayPal on regional sites** — Alipay has a JAL FAQ article title behind it; the other two are search-synthesis only.
- ❌ **`jal.co.jp` AND `press.jal.co.jp` both return 403 (Akamai).** Add both to the blocklist. Wayback works for both.
- ❌ **`faq-jp.jal.co.jp` returns 200 but is a Salesforce Experience Cloud SPA** — curl gets a loading shell only.
- 🚩 **ENVIRONMENT FAULT WORTH RECORDING.** Two fetch attempts against `faq.jal.co.jp/app/answers/detail/...` returned **HTTP 000 with proxy-injected content from an entirely unrelated site — a Ticketek press release.** The agent discarded that output and no claim rests on it. **The agent proxy can mis-serve a host's content. That is a new false-positive class, alongside substring collisions and stale scratchpad artifacts: always confirm fetched content actually belongs to the host you asked for.**

### Manual Research Recommendations
> **1. One Wayback fetch of `jal.co.jp/footer/security.html` and `/footer/policy/`.** Japanese privacy policies routinely enumerate 委託先 by name — **this is the likeliest place the card acquirer is disclosed**, and it is the biggest hole.
> **2. Verify the 23 Dec 2025 dual-carrier outage.** Both ANA and JAL down the same day is the best potential cold open in this batch, and it would also tell us whether there is a shared upstream worth naming.
> **3. Read one regional POS site** (`jal-cn-jp`, or the `world/en` site). **This is where the orchestration pain actually lives** — different methods per region almost certainly means different integrations per region.
> **4. Get passengers, the domestic/international split and cargo share** from the 決算短信 or 「JALグループ早わかり」.

---

## Executive Summary

JAL posted **record FY2025 revenue of ¥2.01 trillion (+9.1%)** — a figure I extracted from the primary filing, and one that **refutes the target list's $11.4B**, which is stale by roughly a year and a currency move. The account's defining feature is an asymmetry: **JAL completed the hard, expensive platform work nine years ago**, consolidating domestic and international onto Amadeus Altéa in 2017 and retiring its own GDS subsidiary — **while the payment layer underneath it did not move with it.** Cash and bank rails sit with **Wellnet**, a vendor operating since May 2000; fraud runs on **NTT Data CAFIS Brain**, live since January 2015; the **card acquirer is undisclosed and nobody can name it**; and the estate is split across **region-gated storefronts with different method sets per region**. The most useful thing found is a category insight rather than a company one: JAL's own payment page links out to Wellnet, whose site claims **all of Japan's major domestic airlines** as customers and whose electronic-money set stops at Rakuten Edy, Mobile Suica and JCB Premo — **no PayPay, no code wallets of any kind.** That is why neither JAL nor ANA offers Japan's dominant wallet, and it turns a feature gap into a structural ceiling. Two premises I carried in were wrong and are corrected in this file: **JAL does accept Apple Pay**, on international, and **JAL is not mid-migration** — which means the ANA opener must not be reused here.

</details>
