# ANA (All Nippon Airways)

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 23 / 29 → ⭐ **High Priority**
**Industry:** Airlines (passenger, + Nippon Cargo Airlines consolidated FY2025) · **HQ:** Tokyo, **Japan** — ANA Holdings Inc., **TSE 9202** · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** **Greenfield** — none detected. Unusually well-evidenced for a greenfield call: ANA's own payment pages show three *separate* point-to-point hand-offs rather than one routing layer (see 3B).

> **Highest-scoring account in this repo to date.** The margin comes from three rows that are sourced rather than inferred: a first-party exhaustive method table, a first-party live defect list, and a first-party results release.

---

> ## 🎯 THE HOOK — ANA has been publicly apologising for its own booking-and-payment system for fifteen months, and paid-seat refunds on international are still not possible online
>
> ANA is migrating its domestic passenger service system onto **Amadeus Altéa**, the platform its international business already runs — **domestic go-live 29 May 2025**.
>
> **On 6 August 2026 — fifteen months later — ANA's own FAQ page still opens with an apology.** Verbatim, fetched by me from `ana.co.jp/ja/jp/notice/renewal-2025-2026/faq/`:
>
> > 「この度は国内線サービスのリニューアルに伴い、お客様には多大なるご不便とご心配をおかけしておりますことを、**深くお詫び申し上げます**。搭乗手続き等で発生していた**システムエラー**につきましては、多くのお客様にご利用いただく機能から優先して、順次修正・改善に努めてまいりました。」
>
> *"We deeply apologise for the great inconvenience and concern caused to customers by the domestic service renewal. Regarding the **system errors** occurring during boarding procedures, we have been fixing and improving them, prioritising the functions used by the most customers."*
>
> **And the live functional-restrictions page carries three money-movement defects right now.** All three fetched by me from `ana.co.jp/ja/jp/promotion/renewal-2025-2026/special-notice/`:
>
> | Defect, verbatim | What it means |
> |---|---|
> | **（国際線）有料座席指定の取消・変更** — 「現在、ANAウェブサイトで有料座席指定の取消・変更を承ることができません。…ANA予約・案内センターまでお問い合わせください。」 | **A paid ancillary that cannot be cancelled or changed online at all.** Every one of those refunds goes through a phone agent. |
> | **ANA SKY コイン払い戻し時の金額非表示** — 「払い戻し金額が表示がされませんが、正常に受付されております。」 | A refund that **processes without showing the customer the amount**. |
> | **特典航空券の払い戻し** — 「払戻完了メールを送信することができません。」 | A refund that **completes without a confirmation email**. |
>
> **This is the cleanest possible opener and none of it is our characterisation — it is ANA's own words on ANA's own live pages.** The angle is not "your migration went badly." It is: *a core-platform migration is exactly when the payment layer stops being able to absorb change, and the ancillary and refund paths are where it shows first.*

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** ANA Holdings is Japan's largest airline group. **FY2025 (year ended 31 Mar 2026) operating revenue ¥2,539.2bn — a record**, with operating income ¥217.4bn and net income ¥169.0bn, all record highs. It is mid-flight on a domestic PSS migration to Amadeus Altéa that it is still apologising for. **FY2026 guidance takes operating income down to ¥150.0bn — a 31% fall** on revenue guided *up* to ¥2,770.0bn.

**SimilarWeb total visits:** **Not obtained.** No data supplied. Country profile is estimate-grade; **no split invented.**

### Accepted methods — first-party, exhaustive, verified by me directly
✅ Fetched from ANA's own payment hub, **both language versions**, `ana.co.jp/{ja,en}/jp/guide/reservation/payment/`. The English page carries **two** tables — one for domestic, one headed *"Payment Methods for ANA Website International Flight Reservation & Purchasing Service"*.

| Method | Scope, verbatim |
|---|---|
| **Credit card** | Domestic table: *"lump-sum payments only"* (一括払いのみ). **International table instead links to a "Credit Card Payment Service" page for instalment and revolving payments.** |
| **Apple Pay** | ✅ Present — **but restricted.** 「航空券の新規ご購入時**のみ**ご利用になれます。ご購入後の予約変更時の差額支払いにはご利用になれません」 — **new purchases only; cannot be used for fare differences on a rebooking**, nor for award tickets or ANA-card discount fares. |
| **ANA SKY COINS** | Miles converted to coins; split tender with a card. |
| **PayPal** | ✅ Present. **¥1,000,000 cap.** Separate redirect flow at `/payment/paypal/`. |
| **Online banking (ネット振り込み)** | Bank transfer to a designated account; prior registration with the bank required. |
| **Konbini — six chains** | Seven-Eleven, Lawson, MINISTOP, FamilyMart, **Seicomart**, Daily Yamazaki / Yamazaki Daily Stores. Multimedia-terminal slip or 13-digit / 11-digit payment number. |
| **Pay-Easy ATM** | *"Mizuho Bank, Sumitomo Mitsui Banking, MUFG Bank, Resona Bank, or Japan Post Bank."* |

### ❌ Affirmatively ABSENT — and this is sourced absence, not unchecked absence
The table above is ANA's **complete** published method set on its own payment hub. **None of the following appears anywhere on it:**

**PayPay · Rakuten Pay · d払い · au PAY · LINE Pay · Amazon Pay · Merpay · Paidy · Google Pay · UnionPay · Alipay · WeChat Pay · carrier billing · any BNPL**

> 🛑 **DO NOT LEAD ON PAYPAY. I checked JAL and the answer went against us.**
>
> ✅ **Verified by me** from JAL's own domestic payment page (Wayback snapshot `20260606014023` of `jal.co.jp/jp/ja/dom/payment/` — JAL's live site returns **HTTP 403** to both curl and WebFetch). JAL's complete domestic method set is:
>
> **クレジットカード · e JALポイント · コンビニ（現金） · 銀行・郵便局ATM (Pay-easy) · インターネット振込 · JAL旅行券** *(the voucher is phone-only)*
>
> **JAL takes no PayPay either — and no Apple Pay, no Rakuten Pay, no LINE Pay, no d払い, no au PAY, no Amazon Pay, no Google Pay and no Paidy.** The two stacks are near-identical in shape: card, an in-house points currency, konbini, Pay-easy, bank transfer, voucher. ANA is marginally *ahead* — it has Apple Pay and PayPal, JAL has neither.
>
> **This is a Japanese legacy-carrier category norm, not an ANA failing.** Opening on it invites the true and fatal reply *"JAL doesn't either."* **The rail gap belongs in E3 as a question about roadmap, never in E1 as an observation.**
>
> ⚠️ **Same trap on both sites: 「PayPay銀行」 appears in the Pay-easy bank list on JAL's page. That is PayPay *Bank*, not the wallet.** Two hits, both in that list. Do not misread it as acceptance on either carrier.

### Known PSPs
| Provider | Role | Evidence |
|---|---|---|
| **Wellnet Inc. (ウェルネット)** | 決済代行 for konbini / Pay-easy / net-transfer rails | ✅ **Verified by me directly.** `ana.co.jp/ja/jp/guide/reservation/payment/pay-howto/` walks the customer through **STEP5 「次画面（ウェルネット社サイト）に移動するための同意確認」** and **STEP6 「ウェルネット社サイトに遷移」**, with the body text 「**決済代行会社「ウェルネット社」のページに遷移します。**」 |
| **PayPal** | Wallet, own redirect | ✅ First-party, own sub-page and ¥1m cap |
| **Card acquirer / gateway** | ❌ **NOT ESTABLISHED** | Checked against GMO Payment Gateway, SB Payment Service, Veritrans/DG Financial, KOMOJU, Sony Payment Services, JCB, NTT Data/CAFIS, Adyen, Stripe, Checkout.com, Worldpay, Cybersource, Braintree, Accelya, CellPoint Digital. **Nothing disclosed.** |

**UATP** and **IATA settlement** are airline-specific rails and were flagged as accepted by the research agent; **I have not verified either first-hand.** Treat as unconfirmed.

### Orchestration status
**None detected — greenfield.** Unlike most greenfield calls in this repo, this one has **affirmative architectural evidence**, not just absent search hits:
- Konbini / Pay-easy **leaves ana.co.jp entirely** for Wellnet's hosted site, behind a consent interstitial
- PayPal is a **separate** redirect with its own cap and its own sub-page
- The card path stays on ANA and is handled by an undisclosed third party
- Apple Pay is **scoped to one transaction type** and cannot follow the booking through its lifecycle

**Four methods, four different paths, and one of them cannot survive a rebooking.** That is a point-to-point estate, not a routed one.

### Buying signals
- 🔴 **A fifteen-month-old public apology** for system errors, still live on 2026-08-06
- 🔴 **Three live money-movement defects** on ANA's own restrictions page, including a paid ancillary with **no online cancellation path at all**
- 🏗️ **Amadeus Altéa domestic PSS migration** — go-live 2025-05-29, announced in a 2023 group press release as a domestic/international system integration. **A platform migration is the single best window for a payment-layer conversation.**
- 📉 **FY2026 operating income guided down 31%** (¥217.4bn → ¥150.0bn) on revenue guided *up* 9%. **Margin compression with volume growth is exactly the shape that makes cost-of-acceptance and auth-rate arguments land.**
- 🌏 **Network expansion** — Narita=Perth, Narita=Mumbai and Narita=Brussels added Dec–Mar; Narita/Haneda=Hong Kong frequencies up; three new routes launched H2 FY2024; 40th anniversary of international scheduled ops in March
- 🤝 **Joint venture with Singapore Airlines**, joint fares launched in May — and **SQ is a confirmed CellPoint Digital customer** (established in the Cathay Pacific file). ANA's JV partner already runs airline payment orchestration.
- ❌ No payment RFP and no payments hire found

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach ANA (All Nippon Airways)` to draft the 12-touch sequence.*

**Four instructions for whoever drafts it:**

1. **The migration apology is the opener, and quote ANA's own page — not a news story.** Frame it as an observation about what a core-platform migration does to the payment layer, never as a dig. The diplomatic clause is mandatory here: *"not because anyone's doing it badly — a PSS cutover is genuinely hard."*
2. **The sharpest single observation is the international paid-seat cancellation being entirely offline.** It is a paid ancillary whose refund path is a phone call, stated by ANA. That is a concrete, checkable, non-insulting fact.
3. **DO NOT LEAD ON PAYPAY. The gate is resolved and it came back red.** I checked JAL's own domestic payment page: **JAL takes no PayPay either**, and no Apple Pay, Rakuten Pay, LINE Pay, d払い, au PAY, Amazon Pay, Google Pay or Paidy. ANA is if anything slightly ahead of JAL on wallets. **Using the wallet gap as an E1 observation earns the reply "JAL doesn't either" and ends the thread.** It goes in E3 as a roadmap question, phrased as curiosity about where wallets sit on their plan — not as a deficiency.
4. **Do not run the cross-border angle as the primary.** ANA is a domestic-heavy carrier — the corridor story is real but secondary. The primary is **lifecycle**: a booking that can be paid four different ways but changed only one way. Apple Pay not working for a rebooking fare difference is the crispest illustration and it is ANA's own footnote.

**Never claim:** that ANA lacks instalments (the international table explicitly links to instalment and revolving payment information), that we know their acquirer (nobody does), or anything about UATP/IATA settlement (unverified).

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 23 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED as a bound; clears by orders of magnitude.** Sourced input: **FY2025 air transportation passenger and cargo revenue ¥2,313.2bn, +12.4% YoY** (ANA HD release, 30 Apr 2026, fetched by me). **Billing unit is bookings, not passengers**, and ancillaries — paid seats, changes, excess baggage — bill separately, which ANA's own restrictions page confirms by treating paid seat selection as its own transaction. **Presented as a bound because the divisor is unsourced:** even assigning an implausibly high **¥300,000 (~US$2,000)** to every booking and ignoring that domestic fares are a fraction of that, ¥2,313.2bn yields ~7.7m bookings/year = **~640k/month**. ⚠️ NCA cargo is consolidated into that line and is invoiced B2B, outside a card checkout — but **stripping cargo entirely still leaves every plausible divisor clearing the 100,000 band by a wide margin.** Hence ✅, not ⚠️. |
| Orchestration status | **+4** | ✅ **None detected — and this is the best-evidenced greenfield call in the repo.** Not merely an absence of hits: ANA's own pages show a Wellnet full-page redirect for cash rails, a separate PayPal redirect, a separate undisclosed card path, and an Apple Pay integration scoped to a single transaction type. Four methods, four paths. |
| 3+ countries | **+3** | ✅ International network across Europe, North America, Asia, Australia and India; Perth, Mumbai and Brussels added in FY2025; 40th anniversary of international scheduled operations. First-party. |
| Multiple PSPs | **+2** | ✅ **Structurally proven, not inferred.** The konbini/Pay-easy rail demonstrably leaves ANA's domain for Wellnet while the card rail does not — two distinct providers, evidenced on ANA's own walkthrough. ⚠️ Only **one** of them (Wellnet) can be named; the card acquirer is undisclosed. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Best-sourced row — but read the caveat, it changes the email and not the score.** Japan is the #1 market by a wide margin. **PayPay, Rakuten Pay, d払い, au PAY, LINE Pay, Amazon Pay, Merpay, Paidy, Google Pay, UnionPay, Alipay, WeChat Pay, carrier billing and BNPL are all absent from an exhaustive first-party method table I fetched in both languages.** That is **sourced absence**, which is the bar this row exists to clear, so it scores. ⚠️ **But I then checked JAL and found the same shape** — see the Hook. **The gap is a category norm, so it is worth points on fit and worth nothing as an opener.** Prateek may reasonably want this row at +1; I kept it at +3 because the row measures whether the rail is missing in a top market, not whether a competitor also misses it. **Flagging it rather than quietly splitting the difference.** |
| Recent expansion | **+2** | ✅ Three new international routes in H2 FY2024; Narita=Perth, Narita=Mumbai, Narita=Brussels and Hong Kong frequency increases across Oct–Mar; **Singapore Airlines JV with joint fares launched in May**. All from ANA HD's own results release. |
| Payment issues reported | **+2** | ✅ **Not customer complaints — ANA's own defect list.** A standing apology for system errors dated **2026-08-06**, plus three live money-movement defects: international paid-seat cancellation impossible online, SKY Coin refund amount not displayed, award-ticket refund confirmation email not sent. All fetched first-party. |
| Funding >$10M | **0** | ❌ TSE-listed (9202). No round. |
| High traffic outside home | **0** | ⬜ **Scored zero deliberately, and it cuts against us.** ANA is domestic-heavy — the research agent reported ANA International 9,023k, ANA Domestic 45,635k and Peach 9,456k passengers, i.e. ~71% domestic. ⚠️ **`[UNVERIFIED — agent-reported, not confirmed by me]`**, but directionally certain, and it is why the cross-border pitch must be secondary here. |
| Competitor using orchestration | **+2** | ✅ **Singapore Airlines runs CellPoint Digital** (established in the Cathay Pacific file). ⚠️ **Caveat worth stating out loud: SQ is now ANA's *joint venture partner*, not its closest competitor** — that is JAL, and JAL's stack is **NOT ESTABLISHED**. The JV arguably makes this *stronger* evidence of category adoption inside ANA's immediate orbit, but it is not the like-for-like comparison. |
| Payment job postings | **0** | ⬜ None found. |

**Tier: 23 / 29 → ⭐ High Priority.** No analyst override applied.

> **The one row that could move, and the one that could collapse.** The card acquirer is unknown; naming it would sharpen everything and change nothing about the score. The **rail gap (+3) is the row at risk** — not because the absence is wrong, it is verified, but because its *materiality* depends on whether JAL differs. Check JAL before sending. If JAL also takes no PayPay, this is still a 23 but the sequence needs a different lead.

### Source Notes
- ✅ **The complete method table was fetched by me directly in both Japanese and English**, including the two-table split between domestic and international and every footnote restriction.
- ✅ **Wellnet is verified verbatim** — 「決済代行会社「ウェルネット社」のページに遷移します。」 — as STEP5/STEP6 of ANA's own payment walkthrough. This is a **full-page hand-off to a third-party hosted site**, not an embedded integration, which is the architecturally important part.
- ✅ **FY2025 results and FY2026 guidance fetched** from `anahd.co.jp/group/en/pr/202604/20260430.html` (30 Apr 2026). Revenue ¥2,539.2bn, operating income ¥217.4bn, net income ¥169.0bn — all records. FY2026 forecast ¥2,770.0bn revenue, ¥150.0bn operating income. **The −31% operating income figure is my own arithmetic on their two published numbers**, not a quoted figure.
- ✅ **The apology and all three live defects were fetched by me** from ANA's own renewal FAQ and special-notice pages.
- ⚠️ **CORRECTION to the research agent's report: the apology is dated 2026-08-06, not 2026-06-11.** The page the agent cited (`/ja/jp/special-notice/001463.html`) now returns **HTTP 404** — it was a temporary notice and has been removed. The live replacement is more recent and says the same thing, so the finding stands but **the date and URL in the agent report are both wrong. Use the ones in this file.**
- ⚠️ **The agent also reported "domestic fare-difference rebooking erroring out" as an open defect.** It is **not** on the live restrictions page and I could not confirm it. **Do not use it.**
- ⚠️ **Passenger counts (64.1m total; ANA Intl 9,023k / Domestic 45,635k / Peach 9,456k) are agent-reported and unverified by me.** Directionally safe for the domestic-heavy framing; **do not put the exact numbers in an email.**
- ⚠️ **UATP and IATA settlement acceptance — agent-reported, unverified.** Not used anywhere above.
- ❌ **An Alipay data point the agent surfaced rests on a 14-year-old press release.** Excluded entirely. Alipay is listed as absent above and that is the correct present-tense reading of the live method table.
- ⚠️ **Amadeus Altéa go-live 2025-05-29 and the ~June 2026 cutover** are corroborated by ANA's own renewal pages and a 2023 ANA HD press release on integrating the domestic and international PSS. **The Amadeus vendor name is from the 2023 release and the search summary, not from a page I fetched — treat the *vendor* as high-confidence but not first-party-verified; the *migration* itself is beyond doubt.**

### Manual Research Recommendations
> **1. ✅ DONE — JAL checked, see the Hook.** JAL takes no PayPay and no Apple Pay. The wallet gap is a category norm and is demoted out of the opener. ⚠️ **The JAL data is a 2026-06-06 Wayback snapshot because jal.co.jp 403s every automated fetch — re-confirm from a browser before quoting it to anyone.**
> **2. Walk the ANA checkout to the card form and identify the acquirer** — network tab, CSP, iframe origin. Nobody has named it.
> **3. Confirm whether international paid-seat cancellation is still phone-only** at send time. It is the sharpest line in the sequence and it is a *temporary* restriction by definition. **Re-verify on the day.**
> **4. Establish whether Peach runs a separate stack.** Peach is ~9.5m passengers, LCC, and LCCs in Japan typically take a wider wallet set than legacy carriers. If Peach takes PayPay and ANA mainline does not, the group-consolidation story writes itself.
> **5. Get the FY2025 passenger split from the investor deck** rather than relying on the agent's numbers.

---

## Executive Summary

ANA Holdings is Japan's largest airline group and posted **record FY2025 revenue of ¥2,539.2bn** while guiding FY2026 operating income **down 31%** on revenue guided up — margin compression with volume growth, which is the shape that makes payment economics a board-level conversation. Its published method set, which I fetched first-party in both languages, is **card, Apple Pay, ANA SKY Coins, PayPal, bank transfer, konbini across six chains, and Pay-Easy ATM — and nothing else.** No PayPay, no Rakuten Pay, no LINE Pay, no d払い, no au PAY, no Google Pay, no UnionPay, no BNPL. Architecturally the estate is **point-to-point**: konbini and Pay-easy hand off to a third-party hosted site run by **Wellnet**, named verbatim on ANA's own walkthrough; PayPal is a separate redirect with its own ¥1m cap; the card path is handled by an acquirer nobody can name; and **Apple Pay is scoped so tightly it cannot pay a fare difference on a rebooking**. Meanwhile ANA is fifteen months into migrating its domestic passenger service system to **Amadeus Altéa** and is **still publicly apologising for system errors as of 6 August 2026**, with three money-movement defects live on its own restrictions page — including a **paid seat selection that cannot be cancelled or changed online at all**. At **23/29 this is the strongest account in the repo**. **The one thing that would have gone wrong is now pre-empted: I checked JAL, found the identical wallet gap, and moved the rail story out of the opener** — the sequence leads on the migration and the broken refund lifecycle, which are ANA's alone.

</details>
