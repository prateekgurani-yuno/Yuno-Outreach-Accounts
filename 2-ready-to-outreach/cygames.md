# Cygames, Inc.

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 19 / 29 → ⭐ **High Priority** — earned on arithmetic, no override applied
**Industry:** Mobile & browser game developer — Uma Musume Pretty Derby, Granblue Fantasy, Shadowverse, Princess Connect · **HQ:** Tokyo, Japan — 〒150-0036 東京都渋谷区南平台町16番17号 · 64.5% owned by **CyberAgent, Inc. (TSE: 4751)** · **Researched:** 2026-09-20 · **First email sent:** —
**Motion:** **In-house orchestration** — two PSPs joined by a single hard-coded boolean. Never pitch "you need orchestration." Anchor on **reach and the cost of the next market**, not on the build being wrong.

---

> ## 🎯 THE HOOK — ~190 countries of direct billing, routed by one line of JavaScript
>
> **Verified first-hand in the live Cygames WebStore production bundle**, `webstore.cygames.com/_app/immutable/chunks/`, fetched 2026-09-20. The payment-provider enum, verbatim:
>
> ```js
> var m = {gmo:1, xsolla:2}
> ```
>
> And the entire routing logic, from `DnIl86T3.js`:
>
> ```js
> ee = n(c, e => { let t = {};
>   for (let n in e) t[n] = e[n]?.userInfo?.country_code === `JP`;
>   return t })
> ```
>
> That store is called **`$willUseGMO`**, and `CoKsEfPu2.js` — the checkout component — consumes it directly.
>
> **`willUseGMO` is literally `country_code === 'JP'`.** Japan goes to GMO Payment Gateway. The other ~190 countries go to Xsolla. Unresolved account defaults to GMO. **No failover, no retry routing, no per-market provider choice, no third-party orchestrator anywhere in the stack.**
>
> ### Why this lands now, and not in six months
>
> CyberAgent's audited FY2025 filing, MD&A p.26 — **read by me in the PDF**, verbatim:
>
> > 「ゲーム事業…売上高は216,710百万円（前年同期比10.6％増）となりました。営業利益は**外部決済への移行効果等もあり**60,063百万円（前年同期比**96.5％増**）となりました。」
>
> **CyberAgent publicly credits the migration to external payment with a 96.5% jump in game-segment operating profit.** They have already proved the thesis to themselves and banked the money. The conversation is not whether to bill off-platform — it is what the next thirty markets cost on a two-provider router built for one.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

### ✅ GATE 1 — Phase 0: PASSES
Game developer. CyberAgent's 有価証券報告書 lists ㈱Cygames 主要な事業の内容 = 「ゲーム事業」, 64.5% owned, 資本金 ¥124M. Not a PSP. **Not a Yuno customer** — `yuno` returns **0 hits across all 141 production bundles** I fetched and grepped.

### ✅ GATE 2 — App-store trap: **ESCAPED, and the escape is the story**

Both halves are true, and the timing is unusually good.

**(a) Historically, platform-intermediated billing dominated — and this is audited.** CyberAgent's FY2025 filing carries a **Key Audit Matter specifically on 「株式会社Cygamesのゲーム売上高」**. Verbatim from p.119, read by me in the PDF:

> 「連結子会社である株式会社Cygames…は、**主にプラットフォーム運営事業者が提供するプラットフォーム内で**モバイルゲームをユーザーに提供するゲーム事業を行っている。」

The auditor's substantive procedure is to reconcile against 「**プラットフォーム運営事業者が発行した証憑**」 — statements issued by the platform operators. That is an audited statement that platform billing was the main route through FY2025.

**(b) But Cygames is now merchant of record in its own name.** Verified by me on the legally-required 特定商取引法 page at `webstore.cygames.com/law/`:

> 販売事業者の名称および住所: **株式会社Cygames** 〒150-0036 東京都渋谷区南平台町16番17号 · 代表取締役 渡邊 耕一

**Not Apple. Not DeNA. Not DMM.** And they are a **registered 前払式支払手段 issuer under the 資金決済法**, with statutory deposits: 「資金決済に関する法律に基づき、**供託をすることにより基準日未使用残高の半額を保全**しております」. Per-title prepaid balances with statutory spend caps (<16 ¥5,000/mo · 16–19 ¥10,000/mo · 20+ unlimited). **This is a registered, deposited prepaid business — not a pilot.**

**(c) They moved before the law did.** The Cygames ID / WebStore terms took effect **2024-12-20**, roughly a year ahead of the 스마ホ新法 (Mobile Software Competition Act) coming into full force in December 2025. `[The Dec-2025 date is UNVERIFIED — search summary only.]` **This was not a compliance scramble.**

⚠️ **NOT ESTABLISHED, and it is the right first question on a call:** CyberAgent discloses **no split** between IAP, platform and web billing — at group, segment or entity level. 「支払手数料」 appears **zero times** in the 125-page filing. The KAM's 「主に」 and the deck's 「外部決済効果もあり」 are directional only. **Do not put a percentage in an email.**

### 💥 The trap Cygames walked around — and it is visible in their own code

**Verified by me in `BCTPBaHg.js`**, the WebStore's app registry and country allowlist:

```js
var r = [`JP`,`TW`,`HK`,`MO`,`KR`,`CN`,`BE`,`NL`],   // excluded from umamusume_en
    i = [`CN`,`BE`,`NL`,`VN`],                        // excluded from granbluefantasy
    a = { priconne:[`JP`], umamusume:[`JP`], cycomi:[`JP`],
          granbluefantasy: n.filter(e => !i.includes(e)),
          "shadowverse-wb": n,
          umamusume_en: n.filter(e => !r.includes(e)),
          "gbf-relink": n },
    o = { ...a, granbluefantasy: a.granbluefantasy.filter(e => e !== `JP`) };
```

**The purchase-enabled list `o` strips `JP` from `granbluefantasy` specifically.** Why? Because Japanese Granblue is not Cygames' to bill. **Confirmed by me at DNS level:**

```
$ getent hosts game.granbluefantasy.jp
203.104.238.91   gbf.game.mbga.jp   game.granbluefantasy.jp
```

Japanese GBF resolves to **DeNA's Mobage infrastructure**. It is billed by Mobage, DMM, Yahoo, GREE, Steam, Apple and Google — not by Cygames. **Cygames built direct web billing everywhere a third-party platform does not own the player, and their code says exactly where that line falls.**

| Title | Web store reach | Who bills |
|---|---|---|
| ウマ娘 (JP) | **JP only** | Cygames via **GMO-PG** |
| **Umamusume (global/EN)** | **~180 countries**, excl. JP/TW/HK/MO/KR/CN/BE/NL | Cygames via **Xsolla** |
| **Shadowverse: Worlds Beyond** | **All ~190 countries, incl. JP** | Cygames — GMO in JP, Xsolla elsewhere |
| プリコネ Re:Dive | JP only | Cygames via GMO-PG |
| **GRANBLUE FANTASY** | Worldwide **except CN/BE/NL/VN — and purchase excludes JP** | Non-JP: Cygames via Xsolla. **JP: DeNA/DMM/Yahoo/GREE** |
| GBF Relink | All countries | Cygames |
| Cycomi (manga) | JP only | Cygames |

### Financials — the target-list figure is CONFIRMED, and it was never an estimate

**Verified by me in the filing, p.7 注2** — Cygames is separately disclosed because it exceeds 10% of consolidated revenue:

| Metric | FY ended 2025-09-30 |
|---|---|
| **㈱Cygames 売上高** | **¥137,528M** (≈ **US$917M** at ¥150/USD — **FX is mine, assumed**) |
| 経常利益 | ¥33,045M |
| 当期純利益 | ¥21,782M |
| 純資産 / 総資産 | ¥219,861M / ¥258,991M |
| Share of CyberAgent consolidated revenue | **15%** |
| CyberAgent Game segment revenue | ¥216,710M (+10.6%) |
| **Game segment operating profit** | **¥60,063M (+96.5%)** |

**"~$1B est. (private)" is CONFIRMED** — and it turns out not to be an estimate at all. There is an audited entity-level figure and it lands almost exactly there.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Cygames`.*

⚠️ **Read before drafting.**

1. **Lead with the two-provider router.** `country_code === 'JP'` deciding between GMO and Xsolla, across ~190 countries, is observable, specific and not disputable. Frame it as reach, not as a mistake.
2. **The Japanese method gaps are the companion observation** — their own 特商法 page lists nine methods and **no konbini, no Paidy, and carrier billing for au only.** docomo and SoftBank are the two largest carrier bases in Japan. A gacha store selling under a ¥5,000/month statutory minor cap with **no cash rail at all** is a conspicuous hole.
3. **Motion is in-house.** They built it, it works, and their parent publicly credited it with a 96.5% profit jump. Respect that. The pitch is the cost of the next market, not the wrongness of this one.
4. **Never imply an IAP-vs-web split.** It is not disclosed anywhere.
5. **Do not pitch Granblue Fantasy Japan.** Mobage owns that player. Their own allowlist says so — and knowing that is a credibility asset, so it is worth showing you know.
6. **Do not quote the ~10% WebStore bonus rate** or the Uma Musume lifetime revenue figure — both are unverified (§3).

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 19 / 29

| Signal | Points | Status |
|---|---|---|
| Monthly transaction count | **+5** | ✅ **DERIVED** — floor ~76,000/month, central ~430,000/month, on the Japanese WebStore alone. See below |
| Orchestration status | **+1** | **In-house layer** — affirmatively evidenced from production code, not inferred from absence |
| 3+ countries | **+3** | ✅ ~190-country purchase-enabled footprint already coded for Shadowverse WB and GBF Relink |
| Multiple PSPs | **+3** | ✅ **GMO Payment Gateway and Xsolla**, both confirmed — one from the 特商法 page, one from the provider enum |
| Local rail gap in a top market | **+3** | ✅ **Japan: no konbini, no Paidy, au-only carrier billing** — from their own legally-required disclosure |
| Recent expansion | **+2** | ✅ Overseas Game revenue **6× YoY in Q4 FY2025** (¥20.0bn); 6 of 7 FY2025 releases were global; the 外部決済 migration itself |
| Payment issues reported | **+2** | ✅ **2025-10-29: WebStore purchases broke game login** under concurrent purchase — see below |
| Funding >$10M | **0** | ❌ CyberAgent subsidiary |
| High traffic outside home | **0** | ❌ **Recorded as zero deliberately.** Cygames is Japan-dominant; overseas is growing fast but from a small base, and I have no sourced share. The ~190-country *footprint* is scored under "3+ countries", not double-counted here |
| Competitor using orchestration | **0** | ⬜ Not established |
| Payment job postings | **0** | ❌ **Verified absent** — 決済 and 課金 return **zero** hits on recruit.cygames.co.jp/career/. The only adjacent role is a Cygames ID product manager, not payments engineering |
| **TOTAL** | **19** | ⭐ **High Priority** |

### Payment methods — Japan, from the 特商法 page (verified by me)

| Method | Status |
|---|---|
| クレジットカード — Visa, Mastercard, JCB, American Express, Diners Club | **CONFIRMED** |
| **PayPay** (the wallet — not PayPay銀行) | **CONFIRMED** |
| Google Pay · Apple Pay · Amazon Pay | **CONFIRMED** |
| **au PAY（ネット支払い）** — wallet | **CONFIRMED** |
| **au PAY（auかんたん決済）** — au carrier billing | **CONFIRMED** |
| **d払い** (docomo wallet) | **CONFIRMED** |
| **楽天ペイ** | **CONFIRMED** |
| ❌ **コンビニ決済 (konbini)** | **NOT FOUND** — zero on the 特商法 page and zero across all bundles |
| ❌ **ドコモ払い / SoftBank まとめて支払い** (carrier billing other than au) | **NOT FOUND** |
| ❌ **Paidy** | **NOT FOUND** |
| ❌ LINE Pay · メルペイ · WebMoney · BitCash · ちょコム · 銀行振込 · PayPal · UnionPay · WeChat Pay · Alipay | **NOT FOUND** |

⚠️ **This list is the JP/GMO list.** What Xsolla exposes on the non-JP checkout is **not established** — it is not in the bundles and an authenticated checkout could not be reached.

### PSPs

| Provider | Evidence |
|---|---|
| **GMO Payment Gateway (GMOペイメントゲートウェイ株式会社)** | **CONFIRMED — first-party legal disclosure**, verified by me: 「※クレジットカード決済については、**GMOペイメントゲートウェイ株式会社**が提供する決済代行サービスを利用しています ※お客様のカード番号等の情報は直接決済代行サービスに保存されます ※…弊社には、お客様のカード番号情報は保存されません」 → cards are **vaulted at GMO**, not at Cygames |
| **Xsolla** | **CONFIRMED — production provider enum**, verified by me in `QFD6A6Wy2.js`: `var m={gmo:1,xsolla:2}`, used as `e.payment_provider` against subscription and order history |
| Veritrans/DG, KOMOJU, SB Payment, Econtext, Zeus, F-REGI, Sony Payment, Rakuten Payment, Paygent | **NOT FOUND** |
| Adyen, Stripe, PayPal, Worldpay, Checkout.com, Coda, PayerMax | **NOT FOUND** — my own grep: all 0 files |
| **Juspay, Spreedly, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY, Yuno** | **NOT FOUND** — my own grep: all 0 files |

**False positives caught and discarded, context printed before rejection:** `supprimer` (French privacy policy) and `primero` (Spanish dispute clause) → "Primer" · `rgmo2` (the Macau i18n key, マカオ) → "GMO" · `useContext` → "eContext" · `maybeStripExtension` in libphonenumber → "Stripe" · a base64 asset blob → "SbPS" · Datadog `tracecontext` → "econtext" · a cart `checkout` string + a Shopify meta-tag heuristic → "Checkout.com". **The `primer` and `rgmo2` hits I re-verified myself.**

### The checkout API surface — recurring billing is live on the web

From the bundles, same-origin `/api`: `/services/{app_id}/cart`, `/cart/items`, `/cart/checkout`, **`/cart/payment_start`**, **`/cart/payment_complete`**, `/subscriptions/check`, `/subscriptions/consent`, `/subscriptions/history/{order_id}`, `/products`, `/serial_code`, `/availability_check`. Order state `{processing:1, completed:2, cancelled:3, failed:4}`; cancel state `{none:0, cancelled:1, partialRefund:2}`.

**`auto_renew` subscriptions are live on the web store** — which is where involuntary churn, retry logic and network tokens live, and none of those exist in a two-branch country router.

### Friction

- **2025-10-29 — WebStore purchases broke game login.** Cygames announced that users who bought **multiple items simultaneously on the WebStore** without having logged into the app since 12:00 that day would hit a 通信エラー on login; the workaround was to log into the app once first. This is a **web-store fulfilment/entitlement-sync failure under concurrent purchase** — exactly the order-orchestration seam a payment layer owns. Notices at `webstore.cygames.com/news/w20251029c/` and `umamusume.jp/news/detail?id=2882`; covered by ASCII.jp. `[Agent-sourced — the Cygames notice page is client-side rendered and returns 200 but no extractable text to curl.]`
- ⚠️ `[UNVERIFIED — page not fetched]` A standing FAQ exists at `support.cygames.com/faq/i033/` titled 「【ウマ娘】『2回限定 ジュエル 1650個』が購入できません。」 and a WebStore FAQ hub at `support.cygames.com/faq/webstore/`. **Both are Cloudflare-protected and returned 403 to curl and WebFetch.** The title implies a purchase-limit interaction between the in-app 1500-jewel SKU and the web 1650-jewel SKU. **Worth a manual browser check — it would be a second strong friction signal.**
- ⚠️ `[UNVERIFIED — search summary only]` Japanese guide sites describe a ~10% bonus-jewel incentive and half-price limited SKUs on the WebStore. **No first-party confirmation. Do not use this number.**

### Volume — DERIVED, every input labelled

| # | Input | Value | Status |
|---|---|---|---|
| 1 | Cygames revenue FY Oct-24→Sep-25 | ¥137,528M | **SOURCED** — 有報 p.7 / p.119, verified by me |
| 2 | FX | ¥150 / USD | **ASSUMED** |
| 3 | Share of Cygames revenue from the 3 JP-WebStore titles | 60% | **ASSUMED** — no title-level disclosure exists |
| 4 | WebStore capture rate of those billings | 25% | **ASSUMED** — not disclosed by anyone |
| 5 | Average transaction value | ¥4,000 | **ASSUMED** — product pages are CSR-only and `/api/services/{id}/products` returns `{}` unauthenticated |

| Scenario | Title share | Web capture | Ticket | **Txns/month** |
|---|---|---|---|---|
| **Floor** | 40% | 10% | ¥6,000 | **≈ 76,000** |
| **Central** | 60% | 25% | ¥4,000 | **≈ 430,000** |
| **Ceiling** | 70% | 35% | ¥3,000 | **≈ 936,000** |

**The 40,000/month gate clears by ~1.9× even at the floor**, using only the Japanese WebStore — and all three scenarios exclude the Xsolla-routed international volume across ~190 countries and all of Cycomi.

⚠️ **Known distortion:** per the KAM, Cygames recognises revenue **on consumption of in-game currency, not on sale** (「ユーザーが当該ゲーム内で…ゲーム内通貨を消費することにより発生する」). Revenue is a lagged proxy for billings, not an identity. In a growing title it understates current billings.

### Methodology notes

- ⚠️ **CSP is the no-evidence case here.** `webstore.cygames.com` returns only `content-security-policy: frame-ancestors 'self';` — **no `form-action`**, verified by me. Per the standing rule, the absence of a PSP host from this CSP proves nothing. All PSP findings rest on the 特商法 page and the JS bundles, which are stronger.
- **Bundle hashes rotate.** The SvelteKit chunks are rebuilt often (`last-modified` was recent), so filenames cited here will not resolve later. The `{gmo:1,xsolla:2}` enum lives in a chunk reachable only from the **subscription / purchase-history** routes, not from `/cart/` — I had to crawl those routes to find it.
- **特定商取引法に基づく表記 is legally required in Japan and names the billing entity and the payment methods.** It was the single highest-yield page on this account. Always find it for a Japanese prospect.

### ⚠️ Pipeline hygiene note, worth acting on

The research agent reported that its scratchpad JS directory **was not empty** — it held leftover bundles from a *different account researched earlier in this session* (an airline app with Touch 'n Go, GCash, BillEase, Rabbit LINE Pay, K PLUS), and its first grep returned a **"LINE Pay" hit that was not Cygames at all**. It caught this by printing context per the false-positive rule and re-derived the file list from the live `<link>` tags before re-running every grep. **My own verification used a fresh per-account directory.** Recommend scoping scratchpad subdirectories per account as standing practice — this near-miss would have put a fabricated payment method into an outreach email.

### What could NOT be established

1. **The actual IAP-vs-web revenue split.** Not disclosed at group, segment or entity level. **The right first question on a call.**
2. **Platform-fee expense.** 「支払手数料」 appears zero times in the 125-page filing.
3. **Which methods Xsolla exposes on the non-JP checkout.** Not in the bundles; authenticated checkout unreachable.
4. **Whether Xsolla is merchant of record internationally.** `[INFERENCE, not confirmed]` — it is the standard arrangement and consistent with the JP/non-JP split, but there is no document. The English pages carry no 資金決済法 disclosure because that is a JP-only requirement.
5. **The WebStore bonus/discount rate.**
6. **Cygames' own help content on failed payments** — `support.cygames.com` is Cloudflare-protected, 403 to both curl and WebFetch.
7. **Whether GBF Japan's Mobage currency is モバコイン specifically** — search-summary only.
8. `cystore.com` (physical merchandise, ASP.NET, likely outsourced) — not investigated.

### Overall research confidence — **HIGH**
The provider enum, the `country_code === 'JP'` router, the country allowlist, the GBF-Japan/Mobage DNS resolution, the 特商法 method list and the GMO vaulting disclosure were all read by me directly in live production code and first-party legal pages. The Cygames revenue figure, the 96.5% operating-profit line and the Key Audit Matter were read by me in the filed PDF. What is soft is the friction evidence, which is Cloudflare-blocked and quarantined above.

</details>
