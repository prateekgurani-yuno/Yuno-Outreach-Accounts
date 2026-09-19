# Peatix

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 21 / 29 → ⭐ **High Priority**
**Industry:** Event ticketing & registration platform (marketplace; collects from attendees, remits to organisers) · **HQ:** New York — **Peatix Inc.**, 413 W 14th Street 2nd Floor, NY 10014; operating centre of gravity is **Peatix Japan K.K.**, Shibuya, Tokyo · **Researched:** 2026-09-19 · **First email sent:** —
**Motion:** **Greenfield** — no orchestration layer. Verified first-hand on the production bundle: Peatix calls **Stripe Elements directly** and **Stripe Connect directly**, with a separate, unnamed legacy Japanese collection stack bolted alongside. Classification rests on affirmative evidence, not absent hits.

---

> ## 🎯 THE HOOK — they turned off every wallet in their own checkout with one line of code, and their reviewers are telling them what it costs
>
> **Verified first-hand, 2026-09-19**, in Peatix's live production bundle
> `https://cdn.peatix.com/assets/production/static/peaz-frontend/js/app-D2wR6Jv-.js` (784,795 bytes):
>
> ```js
> .elements({clientSecret:i.stripeAddCardKeys.clientSecret,appearance:Ur,loader:`never`})
> .create(`payment`,{layout:{type:`tabs`,defaultCollapsed:!1},
>   wallets:{applePay:`never`, googlePay:`never`, link:`never`}})
> .mount(`#card-element`)
> ```
>
> **Apple Pay, Google Pay and Stripe Link — all three suppressed, explicitly, in one line.** This is not a vendor ceiling. It is not a legacy constraint. Somebody wrote `never` three times.
>
> **And their own help centre still advertises Apple Pay.** Verbatim, from the Japanese attendee help centre:
> > 「※ Apple Payでのお支払いに利用できるのは、VISA、MasterCard、AMEX、Discoverです。」
>
> So the documentation promises Apple Pay while the new frontend hard-codes it off. **Their reviewers are living in the gap.** From the Japanese App Store, verbatim and dated:
> - **2026-02-12, 1★** 「Apple Payでの支払いがエラー — 支払い方法でApple Payを選択すると『エラーが発生しました』と表示されて決済を進められない」
> - **2026-08-23, 1★** 「アプリ版でカード決済しようとすると『エラー』表示がエンドレスで表示されます。仕方なくブラウザ版でやったらすんなり決済出来ました」
>
> That is a documented method, a suppressed implementation, and a one-star review describing exactly the error the suppression would produce.
>
> **The second half of the hook is that the same file proves they are mid-migration.** The payment-method enum, verbatim:
> ```js
> function T(e){return e===Nr.STRIPE_CONNECT.code||e===Nr.STRIPE_JYP.code||e===Nr.STRIPE_SGD.code}
> ```
> **`STRIPE_JYP` and `STRIPE_SGD`** — Japan and Singapore are on, or moving onto, Stripe platform accounts, alongside Stripe Connect for organiser payouts. (`JYP` is their own typo for JPY.) A platform halfway through a payments re-platform is the best possible moment to arrive.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Peatix is a Japan-origin event ticketing and registration marketplace operating in **22 countries**, collecting from attendees and remitting to **1,000+ new organisers every month**. It is a **high-transaction, low-value** account: derived **93,000–187,000 paid transactions/month** against only **~US$2–3.3M/month of GMV**. The Japan entity posted a **¥27.4M net loss in FY2025** and the company is **retrenching** — country count fell 27 → 22, and five markets were closed to new events in July 2024.

> ⚠️ **No SimilarWeb data was supplied for this account** and I did not obtain any. The country profile below is built from Peatix's **own published fee-and-currency table**, not from traffic. Two ICP signals that normally lean on traffic are therefore scored on entity and currency evidence instead. Flagged in Research Confidence.

### Volume — **GATE PASSES, on a derived basis. Read the second number too.**

| Input | Value | Status |
|---|---|---|
| Annual event participants (Jul 2024–Jun 2025) | **5,600,000/yr → 466,667/month** | SOURCED (Peatix media kit p.4 + press release 2026-05-26) |
| Events listed at any time | 25,000+ | SOURCED |
| New organisers joining | **1,000+/month** | SOURCED |
| Countries served | **22** (was 27 in Dec-2023) | SOURCED |
| Take rate | **4.9% + ¥99/ticket**; free tickets and door-pay cost ¥0 | SOURCED |
| Paid-vs-free split | **NEVER DISCLOSED** | ⚠️ **the one input the gate turns on** |

Break-even for the 40,000/month gate is **8.57% of participants being paid tickets**. At that share, global ticket-fee revenue would be **~¥118M/yr** — against a Japan entity carrying **¥1.48bn total assets**, 63–100 staff in Shibuya, plus US, Singapore and Malaysia entities. Tokyo payroll alone is on the order of ¥600–800M/yr. **¥118M is not a survivable number, so the paid share is materially above 8.57%.**

**Verdict: PASS.** Base case **93,000–187,000 paid transactions/month** (p = 20–40%). Bear case at p=10% still gives ~47,000.

⚠️ **But derived annual GMV is only ¥3.4–5.9bn (~US$23–40M)** — roughly **US$2–3.3M/month spread across 22 countries and 13 currencies**. **Peatix clears a transaction gate and would fail a GMV gate.** Qualify accordingly: this is a volume-not-value account.

### ⚠️ The stub's "~$30M revenue" is refuted
$30M of *revenue* at a 4.9%+¥99 take rate needs ~18M paid tickets/yr — **3.2× Peatix's entire annual participant count including free registrations.** The stub almost certainly confused GMV with revenue; even read as GMV it sits at the top of the derived range. **Do not carry that number into outreach.** Peatix Japan K.K.'s actual FY2025 result is a **¥27.4M net loss** (官報, https://catr.jp/companies/7d96b/167311).

### Japan — accepted methods, first-party enumeration
Source: https://help-attendee.peatix.com/ja-JP/support/solutions/articles/44001821736 — **re-fetched and verified verbatim by me, 2026-09-19.**

| Method | Status | Detail |
|---|---|---|
| Credit / debit / prepaid | **CONFIRMED** | VISA, MasterCard, JCB, AMEX, Discover, Diners Club |
| **Konbini** | **CONFIRMED** | 「ローソン、ファミリーマート、ミニストップ、デイリーヤマザキ、セイコーマート」 — **⚠️ NO 7-ELEVEN** (`セブン` = 0 hits on the page). ¥330/order, cap <¥300,000 |
| Pay-easy / ATM | **CONFIRMED** | 「Pay-easy、ゆうちょ銀行、Paypay銀行(旧ジャパンネット銀行）、楽天銀行」 — **four, and au Jibun Bank is NOT among them** (`じぶん銀行` = 0 hits) |
| PayPal | **CONFIRMED** | Bank-funding supported, but 「ゆうちょ銀行および三井住友銀行の口座からのお支払いを一時的に停止しています」 |
| Bank transfer (virtual account) | **CONFIRMED** | Web only; 「海外からの送金には対応しておりません」 |
| Apple Pay | **CONTRADICTORY** | Documented (VISA/MC/AMEX/Discover) but **hard-disabled in the new Stripe element** — see the hook |
| **PayPay QR** | **SOURCED ABSENCE** | 「PayPayのQRコード決済には対応しておりません」 — only the PayPay残高カード prepaid card works, processed as a card |
| Rakuten Pay, d払い, au PAY, LINE Pay, Merpay, Amazon Pay, Google Pay, carrier billing | **SOURCED ABSENCE** | None offered; the page enumerates the full accepted set |

### ⚡ The finding worth recording — this is NOT the Wellnet vendor ceiling
Peatix's Japanese wallet coverage is **no better than ANA / JAL / Korean Air / Jetstar Japan**, which this repo mapped to a **Wellnet vendor ceiling**. Zero code wallets; konbini + Pay-easy + card + PayPal only.

It is arguably **worse**: the carriers at least carry 楽天Edy / モバイルSuica / JCBプレモ electronic money via Wellnet. Peatix carries none, **and its konbini set excludes 7-Eleven — Japan's largest chain at ~21,000 stores** — on a platform whose own marketing deck leads with konbini as the reason non-card-holders and seniors can buy.

**So the Japanese wallet gap is not airline-specific.** But Peatix is the cleaner case, because **Peatix has no legacy reservation system to blame and wrote the suppression line itself.**

> **Wellnet: NOT FOUND.** Peatix does not appear on Wellnet's published 収納代行加盟店一覧. No Peatix–Wellnet link established in either direction. The *shape* of the konbini + Pay-easy + multi-bank-ATM set is classic マルチペイメントネットワーク 収納代行, so a Japanese collection agent certainly exists — it is simply never named. **Sourced-absence on Wellnet's list; unchecked-absence otherwise.**

### ⚠️ PayPal may be acquiring the Japanese card flow — underplayed and important
Verbatim from the same page, **verified by me**:
> 「※クレジットカードのお支払いには**外部の決済会社**を利用しています。**カードの種類によっては、決済時にPayPalアカウントの作成が必須です。**ご利用上限は**PayPal社の審査**により異なります。」

*"Card payments use an external payment company. **Depending on card type, creating a PayPal account is mandatory at checkout.** The spending limit varies according to PayPal's review."*

**Forcing a PayPal account signup mid-checkout on a ticket purchase, with a spend cap set by a third party's underwriting, is a conversion event.** This is Peatix's own documentation, not an inference. It also partially answers the "unnamed Japanese processor" question: **PayPal is in the card path**, not merely an alternative button.

### Markets, currency and payout rails
Source: https://help-organizer.peatix.com/ja-JP/support/solutions/articles/44001824033 · **currency is set by event host country, not buyer**

| Market | Currency | Fee/ticket | Payout rail |
|---|---|---|---|
| Japan | JPY | 4.9% + ¥99 | Local bank transfer (¥210/payout) |
| Singapore | SGD | 4.9% + S$0.99 | Local bank (BIC + 4-digit bank + 3-digit branch) |
| Malaysia | MYR | 4.9% + RM1.99 | Local bank (SWIFT BIC) |
| Hong Kong | HKD | 4.9% + HK$6.99 | Local bank |
| Taiwan | TWD | 4.9% + NT$35.00 | **PayPal Payouts** |
| Thailand | THB | 4.9% + ฿35.00 | **PayPal Payouts** |
| Philippines | PHP | 4.9% + ₱50.00 | **PayPal Payouts** |
| **India, Indonesia, South Korea, Vietnam, Sri Lanka** | **USD** | 4.9% + $1.50 | **PayPal Payouts** |
| US / Canada / AU / NZ / EU / UK | local | 4.9% + ~1.00 | mixed |

⚠️ **India, Indonesia, South Korea and Vietnam are priced and paid in USD** — four major APAC markets with no local currency, no local rail, and PayPal as the only way to get an organiser paid.

### ⚠️ Retrenchment, dated
- **Since 2024-07-29**, new events can no longer be created or published in **China, Sri Lanka, Australia, Canada and Hong Kong.**
- Country count **27 → 22** between the Dec-2023 doc and the 2026 media kit.
- Peatix Japan K.K. net profit: **¥322M (FY2021, COVID peak) → ¥87M (2022) → ¥0.7M (2023) → ¥13.5M (2024) → ¥27.4M LOSS (2025)**. Accumulated deficit ¥66.7M.
- **May 2025:** new 代表取締役 at the Japan entity, Yuji Fujita.

**This is a company cutting scope, not expanding it.** Scored 0 on the expansion row, and it changes the tone of any outreach — a cost-and-conversion argument will land; a growth-and-new-markets argument will not.

### Legal entities
- **Peatix Inc.** — New York, NY 10014. CEO **Taku Harada (原田 卓)**. Incorporated Dec 2011.
- **Peatix Japan K.K.** — Shibuya, Tokyo. 代表取締役 **Yuji Fujita (藤田 祐司)**, appointed May 2025. Corporate number 2011001071283. Founded Oct 2011 as part of Orinoco Inc.
- **Peatix Asia Pte. Ltd.** — Singapore 408533. Est. Jul 2013.
- **Peatix Malaysia Sdn. Bhd.** — No. 201401028628, Petaling Jaya, Selangor. Est. Aug 2014.

**Cross-border structure tell**, verbatim from the JP help centre: 「ピーティックス は**米国のPeatix Inc.が提供するプラットフォームを利用して運営している**ため、コンビニ/ATM支払いの手数料330円は不課税となります。」 — the Japanese operation is explicitly a licensee of the US platform, which is why the konbini fee is non-taxable.

</details>

<details>
<summary><h2>✉️ Section 2 — Full Outreach Sequence</h2></summary>

*Not yet generated. Run `/full-outreach Peatix`.*

**Before drafting, note:**
1. **This is a subscription-adjacent account** — the payout help page references 「定額課金プラン」 (recurring billing plans), so read `.claude/reference/subscription-payments.md` before Phase 2.
2. **Do not lead with PCI scope reduction.** Cards were never in Peatix's scope — see the breach section. It would be a wasted opening.
3. **Lead with the payout leg or the wallet suppression, not "you need orchestration."**

</details>

<details>
<summary><h2>🔬 Section 3 — Full Research</h2></summary>

## Verification note

**Everything in the hook and the Japan methods table was re-fetched and verified first-hand on 2026-09-19**, not taken from the research agent's summary. Specifically re-run by me:
- the production bundle (784,795 bytes, HTTP 200) and every Stripe/orchestrator grep
- the Japanese attendee payment-methods help article
- the organiser payout help article

**Two agent claims were corrected in the process:**
1. **"au Jibun Bank" is REFUTED.** The ATM list is 「Pay-easy、ゆうちょ銀行、Paypay銀行、楽天銀行」 — four entries. `じぶん銀行` returns **0 hits** on the page.
2. **The PayPal card-acquiring line was underplayed.** The agent recorded PayPal as an acceptance method; the page actually says card payments run through an external payment company and that **a PayPal account is mandatory at checkout for some card types**. That is a materially stronger finding.

### False-positive discipline — one NEW class recorded

| Match | Reality |
|---|---|
| `gmo` ×25 in the bundle | **24 are `debugMode`/`SettingMobile`**; the 25th is **`/^Can't find variable: gmo$/` inside a Sentry `ignoreErrors` array**. ⚠️ **NEW CLASS: a Sentry error-ignore regex list → false PSP hits.** Not GMO Payment Gateway. |
| `omise` ×21 | All inside `Promise` / `promise`. Not Omise. |
| `wise` | Inside `bitwise`. |
| `PayPay銀行` | PayPay **Bank** (旧ジャパンネット銀行), an ATM funding source — **not** the PayPay wallet. Consistent with the existing running list. |

## 3B. PSPs, gateways, acquirers

**CONFIRMED: Stripe**, verified by me in the live bundle.

**Buyer side — Stripe Elements:** `stripeAddCardKeys` (×6), `#card-element` (×2), `stripePaymentMethodId`, error string `"Stripe client secret does not defined"`, dedicated chunk `./stripe-BBljcOw9.js`.

**Organiser payout side — Stripe Connect:** `initiateStripeOnboarding`, `stripeOnboardingLink` (×2), `isStripeConnected` (×2), `getStripeAccountInfo` (×4), `STRIPE_CONNECT_STATUS` (×8, INCOMPLETE / SUCCEEDED / FAILED), `AccountSettingPayoutForm`, `StripeTimeline`. UI copy: *"To offer paid tickets to your event connect or create a Stripe account."*

**Payment-method enum:** `STRIPE_CONNECT` · `STRIPE_JYP` · `STRIPE_SGD`.

**NOT FOUND — zero genuine hits**, swept by me across the bundle: GMO-PG, Veritrans / DG Financial Technology, Wellnet, KOMOJU / Degica, Sony Payment Services, SB Payment Service, Paygent, Epsilon, PAY.JP, fincode, Adyen, Braintree, Checkout.com, 2C2P, Xendit, Midtrans, DOKU, Omise/Opn, Razorpay, Worldpay, Cybersource, Nuvei, Rapyd, Airwallex, Paidy.

**PayPal: 0 hits in the new bundle** but confirmed in the help centre — so **the PayPal flow still lives in the legacy app.** Two disjoint estates.

**Infrastructure:** nginx behind a CDN; `x-frame-options: SAMEORIGIN`; `peatix_session` is Secure/HttpOnly/SameSite=Lax. **No Content-Security-Policy header** on `/` or `/signup` — sourced absence, and a concrete gap for a platform that mounts Stripe Elements after a 6.77M-record breach.

## 3C. The organiser payout leg — the strongest commercial hook

**All quotes below re-verified by me, 2026-09-19**, at https://help-organizer.peatix.com/ja-JP/support/solutions/articles/44001821780

| Dimension | Finding |
|---|---|
| **Cycle** | 「各イベント終了後の**5営業日以内**に、チケット販売代金から決済処理費用と振込手数料を差し引いた金額のお振り込み手続きを行います。」 Per **event**, not per period. |
| **Cannot pre-pay** | 「イベントページで設定した**イベント終了日より前にチケット販売代金を振り込むことはできません**。」 Peatix holds funds from sale until the event concludes. |
| **No batching** | 「振り込みは、**イベントページごとに行われます。月ごとなど、まとめての振り込みには対応していません。**」 — **one transfer per event page; monthly consolidation explicitly unsupported.** |
| **No balance / no wallet** | No stored value. Payout details are registrable **only after the event is published** — 「イベント編集中の状態では、代金受取口座の登録欄が表示されません」 — a documented source of delay. |
| **Fee** | **¥210 per payout**, organiser-borne, on top of 4.9% + ¥99/ticket. |
| **Merchant of record** | 「振込人名義は「**ピーテイツクスジヤパン（カ**」となります。」 = Peatix Japan K.K. Collects in its own name; never holds PAN. |
| **PayPal splits payouts** | 「PayPal社の条件により、**複数回に分かれてお振込されることがあります**。」 — a reconciliation problem pushed onto the organiser. |
| **No FX** | 「**海外送金のサービスはございません**」 — no cross-border remittance at all. An organiser without a local account in the event's currency simply cannot be paid. |
| **Minimum threshold** | **NOT FOUND** in either article. Sourced-absence in the JP help centre. |

**The commercial read.** Peatix pays **thousands of tiny organisers — 1,000+ new ones every month** — across **13 currencies**, with **no netting, no batching, no balance and no FX**, one transfer per event, ¥210 a time, PayPal splitting disbursements unpredictably, and a 5-business-day tail — all against **~US$2–3.3M/month of GMV**. That is an enormous number of tiny, high-touch, multi-rail disbursements.

**This is a treasury and disbursement problem far more than an acceptance problem, and it is the angle to lead with.** The Stripe Connect migration is the trigger: **they have already decided the old payout stack is broken and are part-way through replacing it.**

## 3D. The 2020 breach — cards were NOT in scope

**The number is 6.77 million records, not the 4.2M commonly cited** (4.2M is the HIBP count of *email addresses* in the circulated dump).

| Item | Finding |
|---|---|
| Intrusion | **16–17 October 2020**, foreign IPs, direct access to part of the database |
| Disclosed | **17 November 2020** |
| Scale | up to **6,770,000** records; every account registered before 17 Oct 2020 |
| Taken | Name, email, **encrypted password**, display name, language, country, time zone |
| **Card data** | **CONFIRMED NOT IN SCOPE** — 「クレジットカード情報や金融機関口座情報等の決済に関する情報…が抽出されたことは確認されておりません」 |
| Why | 「お客様のクレジットカード番号等の完全な決済情報は当社では一切保管いたしません」 |
| Attribution | **Never determined** |
| **PPC action** | **NOT FOUND** — unchecked-absence; the PPC's own publication list was not searched |

**Remediation (2022-12-27 PDF):** network rebuild, stronger password hashing, dedicated security hires, VPN protection, cloud workload isolation, password re-confirmation when changing the payout bank account, 30-day auto-deletion of form data.

**⚠️ Mandatory account MFA was explicitly declined:** 「現時点でのアカウント多要素認証（2FA）の導入は見送りました」

Read alongside a **2026-04-23 1★ review** — 「クレジット決済の際、多段階認証の機能もないので、悪用された場合の対応も極めて脆弱です」 — there is a coherent authentication-posture story: **no account 2FA by policy, and a user reporting no 3DS step-up at checkout.** Flagged as user-reported; Peatix has never stated its 3DS posture and no live checkout was tested.

**Commercial read: do NOT lead with PCI scope reduction.** Cards were never in scope. Account-takeover and payment-authentication posture is the open wound.

## 3E. Complaints — 150 most recent JP App Store reviews, 41 payment-related

Pulled from the primary Apple RSS feed (`itunes.apple.com/jp/rss/customerreviews/.../id=561632513`), not from summaries.

**Card / checkout failures**
- **2026-07-26, 1★** 「引き落としはかかっているのにチケットはどこにも表示されず… 私のお金はどこにいったのでしょうか」 — **charged, no ticket issued.** Auth/capture reconciliation failure.
- **2026-04-23, 1★** 「カード決済したら手続き中に固まってしまう。クレジット会社から決済完了の通知が来た…チケットは購入できていない。再度購入したら無事に…二重に料金が引き落とせないか非常に不安」 — **duplicate-charge exposure after a hung transaction.**
- **2026-08-23 / 2025-11-27, 1★** — in-app card payment fails endlessly; browser works.

**Stored cards not reusable — a direct orchestration pain point**
- **2025-11-23, 1★** 「アカウントにクレジットカードを紐付けているにも関わらず、毎回入力させる意味が分からない。おかげでアプリからは人気のチケットはほぼ取れない」 — card on file must be re-entered every purchase, so **the user cannot win high-demand on-sales.**
- **2025-11-17, 1★** — same, described as long-standing.

**Konbini** — **2026-06-07, 1★**: konbini payment screen never appeared; support said to wait for the window to expire and re-apply; **the event sold out first.** A konbini-flow bug directly cost a sale.

**Refunds** — **2025-08-24, 1★**: no self-serve cancellation; the attendee must DM the organiser from a blank message box and retype the event details from memory.

### ⚠️ Organiser payout complaints — NOT ESTABLISHED
The higher-value complaint set could not be found. The App Store feed is almost entirely attendees (organisers work on web), and the Japanese search for 「主催者 売上 振り込まれない 入金遅延」 returned only Peatix's own help pages. **Unchecked-absence, not sourced-absence** — X, 5ch, note.com and はてブ were not reached. Given the structure in 3C, these complaints should exist. **First follow-up.**

## 3F. Corporate

**History:** founded 2007 as **Orinoco Inc.** → Peatix launched May 2011 → Dec 2011 HQ to Mountain View, Peatix Inc. incorporated, JP entity renamed Orinoco Peatix → 2013 Peatix Inc. to New York → **Jul 2017** JP entity renamed Peatix Japan K.K. (confirmed in the 官報 name-change register, 2017-07-03).

**Funding — `[UNVERIFIED — search summary only, aggregator pages not fetched]`:** ~**$19.3M over 4 rounds**. Named investors: DNX Ventures, **Digital Garage, DG Incubation**, Eight Roads Ventures, Singapore Press Holdings, Itochu Technology Ventures, 500 Startups. Largest: $5M Series B, Mar 2015. **Last round Feb 2019** — nothing recent, hence 0 on the funding row.

⚠️ **Digital Garage owns Veritrans / DG Financial Technology**, which makes a DG-PSP relationship a live hypothesis — but **no evidence was found for it** and the frontend points at Stripe. **Do not assert it.**

**⚠️ JTB capital & business alliance — `[UNVERIFIED — search summary only; source release 404'd]`.** A search result reports JTB concluded a 資本業務提携 with Peatix. **Date, stake size and entity all unknown.** **Verify before outreach** — if real, it is a significant corporate trigger.

**Headcount — `[UNVERIFIED]`:** 63 to ~100, sources disagree.

## 4. ICP Score breakdown — 21 / 29

| Signal | Weight | Score | Basis |
|---|---|---|---|
| Transaction volume | 5 | **5** | Gate passes; 93k–187k/month derived. ⚠️ derived, not sourced |
| Orchestration (greenfield) | 4 | **4** | Direct Stripe Elements + Connect; zero orchestrator hits. Affirmative evidence |
| 3+ countries | 3 | **3** | 22 countries, own published fee table |
| Multiple PSPs | 2 | **2** | Stripe + PayPal + unnamed JP collection agent = two disjoint estates |
| Local rail gap | 3 | **3** | Zero code wallets in JP, PayPay QR sourced-absent, no 7-Eleven; four APAC markets priced in USD |
| Recent expansion | 2 | **0** | **Retrenchment** — 27→22 countries, 5 markets closed 2024-07-29 |
| Payment issues | 2 | **2** | 41 payment-related reviews; charged-no-ticket, duplicate charges, Apple Pay errors |
| Funding | 2 | **0** | Last round Feb 2019 |
| Traffic outside home market | 2 | **2** | 22 countries; SG and MY entities; scored on entity/currency evidence, not traffic |
| Competitor orchestration | 2 | **0** | Not established |
| Job postings | 2 | **0** | Not established — search budget exhausted |
| **TOTAL** | **29** | **21** | ⭐ **High Priority** |

## 5. What could NOT be established

1. **Paid-vs-free split** — the input the gate turns on. Never disclosed. The PASS is a revenue-floor argument, not a sourced count.
2. **Any GMV figure.** The only one seen (¥7bn cumulative to 2016) was a search summary. Do not use it.
3. **The Japanese konbini/Pay-easy collection agent.** Certainly exists, never named. Wellnet ruled out on its published merchant list only.
4. **Non-Japan checkout acceptance.** Payout currency and fees are known per country; what the SG/MY/HK/TW checkouts actually *accept* (PayNow? FPX? GrabPay?) is not.
5. **PPC (個人情報保護委員会) action** on the breach.
6. **JTB alliance specifics** — verify first.
7. **Headcount** — 63 to ~100.
8. **Engineering blog / GitHub / job postings** — not reached.
9. **Organiser payout-delay complaints** — the most regretted gap.
10. **3DS / SCA posture** — one user says there is none; Peatix has never stated a position; untested.

## 6. Overall Research Confidence — **MEDIUM-HIGH**

**High** on the payment stack: the production bundle was fetched and grepped **first-hand**, and the Stripe finding, the wallet suppression and the orchestrator absence are all direct quotes from live code. **High** on payout mechanics and Japanese acceptance — all re-verified verbatim against Peatix's own help centre.

**Downgraded from High because:** no traffic data at all; the volume gate rests on a derived rather than sourced paid share; and three corporate items (JTB, funding, headcount) are search-summary grade.

## 7. The three things to build outreach on

1. **They are mid-migration to Stripe, market by market, and have already conceded the old stack is broken.** `STRIPE_JYP` and `STRIPE_SGD` plus Stripe Connect replacing the PayPal-Payouts-and-SWIFT patchwork.
2. **The payout leg is a genuine treasury problem.** 1,000+ new organisers monthly, 13 currencies, per-event transfers, no batching, no netting, no balance, no FX, ¥210 a pop, PayPal splitting disbursements.
3. **Japan acceptance is a measurable hole and it is a config decision, not a vendor ceiling.** `wallets:{applePay:'never',googlePay:'never',link:'never'}` in their own code, PayPay QR declined in writing, no 7-Eleven — while the help centre still advertises Apple Pay and reviewers report it erroring.

**The honest counterweight:** ~US$23–40M annual GMV across 22 countries is small, the Japan entity just posted a loss, and it is withdrawing from five markets. **Volume-not-value. Price and qualify accordingly.**

</details>
