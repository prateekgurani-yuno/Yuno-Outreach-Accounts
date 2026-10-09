# SpinX Games

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 14 / 29 → 🟢 Medium
**Industry:** Gaming — social casino (free-to-play slots, virtual-currency top-ups) · **HQ:** Hong Kong · **Researched:** 2026-10-09 · **First email sent:** —
**Motion:** In-house (hand-routed) — splitting into single-vendor dependency on new titles

---

> ## ✅ Orchestrator audit — independently re-verified 2026-10-09
>
> I re-ran the load-bearing checks myself rather than accept them. **All held.**
>
> **The storefront discovery method is real and reproducible.** `tpp.spinxbi.com/payment/appcharge`
> returns a `Content-Security-Policy: frame-ancestors` header enumerating **exactly 21 permitted
> hosts**. I fetched it and read them off:
>
> ```
> shop.cash-frenzy.com · webtest.cash-frenzy.com · jackpot-world.com · www.jackpot-world.com
> jackpotworld.spinxvip.com · www.lotsa-slots.com · lotsa.spinxbi.com · dafu.spinxbi.com
> cash-rally.com · cr.spinxbi.com · cashclubcasino.com · cc.spinxbi.com
> jackpot-wins.com · jackpotwinscasino.com · jackpotwinscasinoslots.com · www.jackpotwinsslots.com
> prime.jackpot-crush.com · jc.spinxbi.com · vf.spinxbi.com · http://myfile.bolevpn.com
> ```
>
> 🔑 **The CSP header is the asset map.** Worth reusing as a technique on any merchant that frames a
> payment page: the `frame-ancestors` list is the merchant's own enumeration of every storefront it
> owns, and it is served to anyone who asks.
>
> **The Cash Frenzy domain correction is confirmed.** `cashfrenzy.com` fails outright (curl exit code
> `000`, no response). **`shop.cash-frenzy.com` returns HTTP 200.** Earlier attempts reset because the
> domain is hyphenated.
>
> **The split-motion finding is confirmed.** `shop.cash-frenzy.com` is a Nuxt SPA served from
> `d1cse7lsiayene.cloudfront.net/cash-frenzy/production/`. Its entry bundle scores **`appcharge` ×2
> and ZERO for `airwallex`, `gash`, `mycard`, `paypal` and `xsolla`.** So the newer storefronts really
> do bypass the in-house gateway and run Appcharge alone, while the flagship keeps the five-processor
> stack. **Two different payment architectures inside one company.**
>
> ⚠️ **One of my own checks was initially wrong and is recorded here as a method note.** My first
> Appcharge scan returned zero — because I had grepped `www.cash-frenzy.com` (a 5,191-byte marketing
> page) rather than the shop's 979-byte SPA shell and its CloudFront bundle. **A zero against the
> wrong asset is not a negative finding.** Same family of error as the Brotli and stale-scratchpad
> traps already logged in this repo.
>
> ### 🚩 Phase 0 conflict worth acting on, found while cross-checking
>
> **`Gamania Digital Entertainment` is on `accounts/apac-tal.csv`** (Gaming, Taiwan, Not Contacted) —
> and **Gamania owns GASH**, the Taiwanese payment rail SpinX uses. Under the standing ICP rule a
> company selling payment infrastructure to third parties routes to **Partnerships**, not outreach.
> **Resolve which Gamania entity is the target before anyone touches that account.** Precedent in this
> repo: PDAX was rejected on exactly this test while CoinSpot was kept, the question being what a
> third party can actually buy.
>
> **Peer scores the report cites were also checked against the repo and match exactly:** Com2uS
> **21/29**, Cygames **19/29**, Asiasoft PlayPark **17/29**.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** SpinX Games Ltd is a Hong Kong social-casino developer, wholly owned by Korea's Netmarble since 2021, whose free-to-play slots titles (Jackpot World / 大福Online, Lotsa Slots, Cash Frenzy, Jackpot Wins, Cash Club Casino, Jackpot Crush, Cash Rally) monetise through virtual-currency top-ups. It sells those top-ups on **at least seven live web storefronts plus a downloadable Windows client and a SpinX-controlled payment flow inside its mobile apps** — not only through app-store IAP. It runs its own payment gateway at `tpp.spinxbi.com` across six processors, with channel availability managed by hand.

**SimilarWeb total visits (last full month):** ⚠️ **NOT AVAILABLE for any revenue-bearing domain.** The supplied figure of 337,627 visits (Sep 2026) measures `spinxgames.com`, an 894-byte brochure SPA whose router contains no shop, cart, checkout or payment route — see `accounts/traffic/spinx-games.md` §CORRECTION. **No traffic data exists for `jackpot-world.com`, `lotsa-slots.com`, `shop.cash-frenzy.com` or the other four storefronts.** Two ICP rows could not be scored as a direct result.

### Top 5 markets
⚠️ **Cannot be completed.** A ranked market table requires traffic data for the storefront domains, and none exists. Below are the markets where a **payment surface is confirmed first-hand**, which is a different and weaker claim than a traffic ranking — these are not ranked and no share is implied.

| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| — | 🇹🇼 Taiwan | Not found | GASH (convenience-store cash voucher), MyCard, cards via Airwallex ([source code](https://d13ac69ufeumng.cloudfront.net/live/assets/index-a6b23cbd.js)) | JKOPay, LINE Pay, ATM/virtual-account transfer, domestic instalments — all 0 hits in bundle | ❌ none found |
| — | 🇯🇵 Japan | Not found | Cards via Airwallex, Apple Pay, GASH voucher redemption (ja-localised in gateway) | konbini, PayPay, LINE Pay, Rakuten Pay, carrier billing, Paidy — all 0 hits | ❌ none found |
| — | 🇭🇰 Hong Kong | Not found | Cards via Airwallex **Hong Kong entity**, PayPal, Apple Pay | FPS, Octopus, AlipayHK, WeChat Pay HK — all 0 hits | ✅ SpinX Games Limited |
| — | 🇺🇸 United States | Not found | Cards via Airwallex, PayPal, Appcharge, Apple Pay | — (card-native market) | ❌ none found |
| — | 🇷🇺 Russia | Out of territory | Xsolla — **but marked `is_close: true` in the live config while the code still hard-routes `RU` to it** | n/a | ❌ none found |

🛑 **Notably absent from the entire stack:** UPI, QRIS, PayNow, PromptPay, GCash, FPX, DuitNow, konbini, Alipay, WeChat Pay, UnionPay, JKOPay, LINE Pay, Octopus, TrueMoney, MoMo, ZaloPay, VNPay — every one scanned and returning zero across six production bundles. **South Asia and Southeast Asia have no local rail coverage at all.**

### Legal entities
- **SpinX Games Limited** (Hong Kong) — registration # not found. Named as Apple App Store seller of record for Jackpot World ([apps.apple.com](https://apps.apple.com/US/app/id1356980152)) and in the first-party footer copyright *"Copyright © 2020-2026 SpinX Games Ltd. All rights reserved."* ([jackpot-world.com](https://www.jackpot-world.com/en/support/faq))
- **Grande Games Limited** — jurisdiction not established; registration # not found. Co-defendant in the Washington class action ([topclassactions.com](https://topclassactions.com/lawsuit-settlements/consumer-products/mobile-apps/spinx-games-grande-games-beijing-bole-technology-casino-apps-3-5m-class-action-settlement/)). Jackpot World's Android package id is `com.grandegames.slots.dafu.casino` ([bluestacks.com](https://www.bluestacks.com/campaign/com.grandegames.slots.dafu.casino/tr/))
- **Beijing Bole Technology Co., Ltd.** (China) — registration # not found. Co-defendant in the same action; corroborated first-hand because SpinX's own help centre is served from **`bolegames.helpshift.com`** and is titled *"SpinX Games Support"* ([bolegames.helpshift.com](https://bolegames.helpshift.com/hc/en/14-jackpot-world/))
- **Leonardo Interactive Holdings** (Cayman Islands) — SpinX's parent vehicle acquired by Netmarble ([gamblinginsider.com](https://www.gamblinginsider.com/news/12749/netmarble-purchases-spinx-after-acquiring-leonardo-interactive-holdings), [yogonet.com](https://www.yogonet.com/international/news/2021/08/02/58626-south-korean-game-developer-netmarble-acquires-social-casino-spinx))
- **Parent: Netmarble Corporation** (South Korea, KOSPI 251270) — acquired 100% of SpinX for ₩2.5 trillion / $2.19bn, announced 2021-08-03 ([pocketgamer.biz](https://www.pocketgamer.biz/netmarble-picks-up-social-casino-developer-spinx-games-for-219-billion)). First-party confirmation inside the Jackpot World production bundle: *"Jackpot World, by SpinX (Netmarble subsidiary)"*

⚠️ **Discrepancy:** pocketgamer.biz places SpinX in **Sheung Wan**; the German App Store listing gives *"Suite nos. 6B-7, 19/F, China Hong Kong City Tower 3, 33 Canton Road, Kowloon"* — **Kowloon, not Sheung Wan** `[UNVERIFIED — search summary only, page not fetched]`. Both are Hong Kong; the specific district is unresolved.

### Known PSPs
- **Airwallex** — primary card processor. `[Source Code]` + `[Terms/Privacy Policy]`, 32 hits. Consumer-facing disclosure verbatim: *"Jackpot World uses Airwallex to process payments. By proceeding to pay, you will provide your payment information and purchase information to Airwallex."* Links the **Hong Kong** entity's privacy policy. (Global, incl. US/JP/TW/HK)
- **GASH** (Gamania, Taiwan) — `[Source Code]`, 147 hits in the web bundle + 21 in the gateway. Convenience-store cash voucher redemption with its own PIN/error-code flow. (Taiwan, ja-localised)
- **MyCard** (Taiwan) — `[Source Code]`, 73 hits. (Taiwan)
- **Appcharge** — `[Source Code]`, production tokens on five separate storefronts. Specialist gaming web-shop vendor. (Global)
- **PayPal** — `[Source Code]`, 4 hits in web bundle + 19 in gateway, route `/paypal/DF/website`. (Global)
- **Xsolla** — `[Source Code]`, 7 hits. Russia-only fallback, **currently `is_close: true` in the live config.** (Russia — out of territory)

**Explicitly scanned and absent (0 hits across all six bundles):** Adyen · Stripe · Checkout.com · Nuvei · 2C2P · Coda · Razer · dLocal · PayerMax · Worldpay · Braintree · Primer · Spreedly · Gr4vy · Juspay · Xendit · Midtrans · iPay88 · PayU · Razorpay · Paytm. *(`dlocal`, `omise`, `upi`, `fpx`, `sofort`, `boku`, `wechat` all returned apparent hits that were confirmed false positives on context inspection — see Section 3A.)*

### Orchestration status
**In-house orchestration layer — built, but routed by hand.** `tpp.spinxbi.com` is SpinX's own payment gateway (HTTP 200; metadata verbatim: *"Spinx Games, Third Party Payment, Online Payment, Jackpot World, Cash Frenzy, Airwallex, Paypal"*), serving eleven routes across three channels per title (`WEB` / `EXE` / `APP`). Channel selection is driven by a server-side config endpoint `/payment/getPaymentConfig` carrying per-channel `is_close` / `close_date` kill switches. **There is no third-party orchestrator and no automated routing logic** — the only country condition in the entire stack is one hard-coded string, `if (t === "RU") return ["xsolla"]`.

### Buying signals
- 🚀 **Four storefronts built or rebuilt in the last six weeks.** Prerender timestamps embedded in the live pages: Cash Club Casino **2026-08-28**, Jackpot Crush **2026-09-08**, Cash Frenzy **2026-09-17**. Cash Club ships four locales (`en, jp, zh_hk, de`). ([shop.cash-frenzy.com](https://shop.cash-frenzy.com/), [cashclubcasino.com](https://cashclubcasino.com/), [prime.jackpot-crush.com](https://prime.jackpot-crush.com/))
- 🚀 **Two more storefronts staged but not live:** Vegas Friends (`vf.spinxbi.com`) runs `appchargeEnv: "sandbox"` / `ENV: "preview"`; Cash Rally (`cash-rally.com`, 94KB of storefront) returns `payment_config: null`. **Both are pre-launch payment integrations in flight right now.**
- 🤝 **Appcharge has been promoted ahead of Airwallex in the live channel order.** The shipped bundle default is `["airwallex","paypal","appcharge"]`; the config served today is `["appcharge","airwallex","paypal"]`. A vendor is being moved to first position on the flagship title.
- 📉 **Netmarble's commission-to-revenue ratio has fallen for five straight quarters — 35.7% → 35.1% → 33.8% → 32.3% → 31.6%** ([Netmarble's own IR host, 4Q25 deck](https://sgimage.netmarble.com/images/netmarble/nmOfficial/20260205/8sto1770273390151.pdf)). The line is undifferentiated, so this is *consistent with* own-channel migration but does not prove it.
- 💼 Payment-related hiring: **no SpinX payment role found.** No public payment RFP found.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach spinx-games` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 14 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ⚠️ **NOT FOUND — ASSUMED ~280,000/month. [ASSUMPTION — not researched.]** Billing unit counted: **virtual-currency top-up purchases settled on SpinX's own channels** (web storefronts, Windows EXE client, in-app alternative billing). **App-store IAP purchases are Apple's and Google's transactions, not SpinX's, and are excluded.** Basis: SpinX revenue ≈ **US$418M/yr DERIVED** from two sourced inputs (below) → US$34.9M/month total; × an assumed 20% own-channel share → US$6.98M/month; ÷ an assumed US$25 average top-up → ~279,000. **Both the channel share and the average top-up value are assumptions, not sources**, so the whole figure is an assumption regardless of the arithmetic. Sensitivity grid: 10% share → 232k ($15) / 139k ($25) / **70k ($50)**; 20% share → 465k / 279k / 139k; 28% share → 651k / 390k / 195k. Eight of nine corners land in the ≥100,000 band; only 10%-share-at-$50-ATV drops to the 50–99,999 band. Awarded the band the central assumption implies. **⚠️ This figure must never be used to reject the account, and has not been.** |
| Orchestration status | **+1** | ✅ **In-house layer confirmed** — own gateway at `tpp.spinxbi.com`, server-driven channel config, no third-party orchestrator. Scores +1, not +4: this is not greenfield. |
| 3+ countries | **+3** | ✅ Four named legal entities with sources across **three jurisdictions** — Hong Kong (SpinX Games Limited), China (Beijing Bole Technology Co., Ltd.), Cayman Islands (Leonardo Interactive Holdings), plus Grande Games Limited (jurisdiction not established). ⚠️ No registration numbers found for any of them. Awarded on entity count per the rule's wording; **not** awarded on traffic, which is unavailable. |
| Multiple PSPs | **+3** | ✅ Six processors confirmed by first-hand source-code evidence: Airwallex, GASH, MyCard, Appcharge, PayPal, Xsolla. Comfortably met. |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **CANNOT BE SCORED — the supplied traffic measures the wrong domain.** The rail gap itself is verified and wide (no UPI / QRIS / PayNow / PromptPay / GCash / konbini / Alipay / WeChat Pay anywhere in the stack, Section 4), and Japan and Taiwan are both confirmed live payment surfaces — but the rule requires the gap to sit in a **top-3 traffic market**, and no top-3 can be established for any revenue-bearing domain. Scored 0 rather than assumed. **This row would most likely convert to +3 on a storefront SimilarWeb re-pull.** |
| Recent expansion | **+2** | ✅ Dated first-hand evidence of storefront expansion inside the last six weeks — prerender timestamps 2026-08-28 (Cash Club, 4 locales), 2026-09-08 (Jackpot Crush), 2026-09-17 (Cash Frenzy), plus two pre-launch stores (Vegas Friends in Appcharge sandbox, Cash Rally with a null payment config). |
| Payment issues | **0** | ❌ **Isolated, not moderate.** Trustpilot `spinxgames.com` scores 2.5/5 "Poor" across 31 reviews with 90% at one star, but only **two** reviews are payment-specific once game-fairness and payout complaints are excluded. Two instances on one platform does not meet the moderate/high bar. Not inflated. |
| Funding >$10M | **0** | ❌ No funding round in the last 12 months. The $2.19bn Netmarble transaction was a 100% acquisition in **2021** — an M&A event, not a round, and five years stale. |
| High traffic outside home | **0** | ⬜ **CANNOT BE SCORED — wrong-domain traffic.** Netmarble's group split (N.A. 39% / Korea 23% / Europe 12% / SEA 12% / Japan 7%, 4Q25) describes the **parent group**, not SpinX's storefronts, and cannot stand in for this row. |
| Competitor using orchestration | **0** | ❌ No public case study found of any social-casino competitor adopting a payment orchestrator. The closest peer, SciPlay, built its **own** proprietary D2C platform rather than buying orchestration (Section 11C). |
| Payment job postings | **0** | ❌ No SpinX payment-related role found. Searches surfaced payment roles at AviaGames, NetEase Games and HoYoverse, none at SpinX. |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **🟢 Medium (14/29)**

No public payment RFP was confirmed, so no RFP override applies.

**Analyst override — considered and DECLINED, in both directions. Reasoning in full:**

- **Downward (app-store trap) — declined.** The documented `not-icp` failure mode does not apply. SpinX operates its own payment gateway, its own merchant checkout, stored-card consents, a Windows client billing path and a SpinX-controlled in-app payment flow. The app-store channel exists alongside, but it does not own the billing relationship on these surfaces. Phase 0 cleared this and the present run re-verified the gateway independently.
- **Downward (absolute volume) — declined.** Derived revenue of ~US$418M/yr is not negligible by any reading.
- **Upward to ⭐ — declined, but only for want of one input.** **Three of the eleven rows, carrying 5 points, are unscoreable purely because the supplied traffic measures a brochure site rather than the storefronts.** Were a storefront re-pull to show three markets above 1% share with a home market under 60% — which the confirmed Taiwan, Japan, Hong Kong and US surfaces make plausible — the local-rail row (+3) and the traffic-outside-home row (+2) would likely both fire, taking this to **19/29 ⭐ High Priority.** I am not awarding points for a plausible outcome. The score is 14/29 today, and the single action that would move it is in Manual Research Recommendations #1.
- **Double-counting — checked, none found.** "Multiple PSPs" fires off six source-code-confirmed processors; "3+ countries" fires off four named legal entities. Independent facts.
- **Regulatory reality — no blocker.** Hong Kong HQ, no market where Yuno could not practically serve them.

### Source Notes
- ✅ Full PSP stack re-verified first-hand on 2026-10-09 across six decompressed production bundles fetched into a clean directory
- ✅ Live server-side `payment_config` captured from the SSR state of four separate storefronts — this is runtime configuration, not a shipped default
- ✅ Per-title Netmarble revenue share sourced to **Netmarble's own IR host** (`sgimage.netmarble.com`), replacing the third-party `investgame.net` mirror
- ✅ Cash Frenzy storefront **located and loaded** at `shop.cash-frenzy.com` — the gate's `[INFERENCE]` is now an observation
- ✅ Washington class action verified on a fetched page: case no. 20-cv-01310-RSM, W.D. Wash.
- ✅ SciPlay D2C channel split read directly from a fetched SEC 10-Q
- ⚠️ **TAL's "~$1B est." revenue is REFUTED.** Derived ~US$418M/yr; corrected in Section 12
- ⚠️ No traffic data for any revenue-bearing domain — two ICP rows unscoreable
- ⚠️ Web-vs-app-store billing split **not published by Netmarble and not separately filed by SpinX**
- ⚠️ Japan 特定商取引法 disclosure carried as a Phase 0 gate finding; the policy host is a document-by-id SPA and I could not re-open the document text in this environment
- ⚠️ Kentucky settlement (~$285,500) remains `[UNVERIFIED — search summary only, page not fetched]` and is not used
- ⚠️ Airwallex's underlying acquirer is **not established** — searched and not found
- ⚠️ HQ district conflict (Sheung Wan vs Kowloon) unresolved

### Success Case Alternatives
- **NetEase Games** — the closest APAC gaming reference Yuno can name publicly. Match: large Chinese-HQ publisher selling virtual goods across many APAC markets through its own channels, with the same multi-rail acceptance problem SpinX has in SEA and South Asia. ⚠️ **No published metrics exist for this account — never attach a number to it.**
- **Garena** — Southeast Asia gaming at scale, the region where SpinX's rail coverage is emptiest. ⚠️ **No published metrics — never attach a number.**
- **inDrive** — use strictly as a **stated pattern match for multi-country scale**, not as a gaming case: a merchant operating across many countries that needed one integration rather than per-market builds. Say "a pattern we see in multi-country consumer businesses," never "a gaming customer."
- **Rappi** — same caveat, used strictly as a **stated pattern match for provider breadth** across many local rails.

> **Best Success Case for this account: NetEase Games**, named without numbers. SpinX is a Greater-China-rooted publisher of virtual goods with a self-built billing stack; that is the profile NetEase matches, and the absence of published figures is less damaging here than a mismatched case would be, because the evidence in this report is SpinX's own code rather than a benchmark.

---

## Executive Summary

SpinX Games Ltd is a Hong Kong social-casino developer, 100%-owned by Netmarble since 2021, selling virtual-currency top-ups for seven slots titles across at least seven live web storefronts, a downloadable Windows client and a SpinX-controlled payment flow inside its mobile apps. **The key payment finding is that SpinX has built its own multi-channel payment gateway — and then split in two.** Its flagship (Jackpot World / DAFU) runs an in-house router across Airwallex, PayPal, Appcharge, GASH and MyCard whose channel availability is managed by hand through dated `is_close` kill switches, with exactly one country condition in the whole codebase; its six newer storefronts bypass that router entirely and sit on **Appcharge alone**. The orchestration opportunity is therefore not "you need orchestration" — they built one — but that the thing they built does not route, does not fail over, and does not reach a single local rail in South Asia or Southeast Asia, while the newer titles have traded hand-routing for single-vendor dependency. **The motion is in-house, and the argument is reach and opportunity cost, never the case for orchestration itself.**

---

## Section 1: Website Traffic Analysis by Country

**Data source:** Path 1 — pasted SimilarWeb data supplied by Prateek (`accounts/traffic/spinx-games.md`, Similarweb PRO, Worldwide, All traffic, Sep 2026, captured 2026-10-09). **The supplied data was then invalidated for this purpose.**

🛑 **THE SUPPLIED TRAFFIC MEASURES A DOMAIN THAT SELLS NOTHING.**

`spinxgames.com` is a corporate brochure site. Verified: an **894-byte** SPA shell whose router contains only `/`, `/about`, `/cookie_notice`, `/data_delete`, `/ethics`, `/game`, `/join_social`, `/privacy`, `/terms`. Keyword counts in its bundle: `shop` 0, `payment` 0, `cart` 0, `checkout` 0, `coins` 0.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| — | **Not applicable** | — | — | — | The supplied table describes `spinxgames.com` only. Reproducing it here ranked by country would imply it describes SpinX's payment surface. **It does not.** See `accounts/traffic/spinx-games.md` for the raw figures and the correction notice. |

**For the record, and explicitly NOT to be used for sizing or for market prioritisation:** the supplied sheet reports 337,627 visits for `spinxgames.com` in Sep 2026, ▼5.15% MoM, 91.33% United States, with an APAC visible total of 0.86% (India 0.32%, Japan 0.30%, Australia 0.24%) and 98.96% mobile web. **None of those figures describe a storefront.** In particular, the 0.86% APAC share must not be used to argue this account has no APAC exposure — Section 4 shows live, localised, cash-accepting payment surfaces in Taiwan and Japan.

**The revenue-bearing domains, all confirmed live first-hand on 2026-10-09, none ever measured:**

| Domain | What it is | Verified |
|---|---|---|
| `jackpot-world.com/en/shop/token` | Jackpot World token store | ✅ HTTP 200, **78,737 bytes** |
| `jackpot-world.com/en/shop/gash` | Jackpot World GASH/MyCard store | ✅ HTTP 200, 36,577 bytes, `<title>Top Up via GASH/MyCard \| Jackpot World</title>` |
| `jackpot-world.com/ja/shop/token` | Japanese token store | ✅ HTTP 200, 70,642 bytes, hiragana confirmed by byte-level detection |
| `dafu.spinxbi.com` | Second Jackpot World front (`<title>Jackpot World…</title>`), **separate payment config** | ✅ HTTP 200, 77,305 bytes |
| `www.lotsa-slots.com` + `/web_store` | Lotsa Slots store, `showStore: 1` | ✅ HTTP 200 |
| **`shop.cash-frenzy.com`** | **Cash Frenzy store — located and loaded this run** | ✅ HTTP 200, `isShopEnable: true`, production Appcharge token |
| `jackpot-wins.com` (+ `www.jackpotwinsslots.com`, `jackpotwinscasino.com`, `jackpotwinscasinoslots.com`) | Jackpot Wins store, PWA titled "JW Store" | ✅ HTTP 200, production Appcharge token |
| `cashclubcasino.com` | Cash Club Casino store, locales `en, jp, zh_hk, de` | ✅ HTTP 200, production Appcharge token |
| `prime.jackpot-crush.com` | Jackpot Crush store | ✅ HTTP 200, production Appcharge token |
| `cash-rally.com` | Cash Rally store, **`payment_config: null`** | ✅ HTTP 200, 94,051 bytes — **pre-launch** |
| `vf.spinxbi.com` | Vegas Friends store, `ENV: preview`, `appchargeEnv: sandbox` | ✅ HTTP 200 — **pre-launch** |
| `tpp.spinxbi.com` | SpinX's own payment gateway | ✅ HTTP 200 |

🔑 **How the full storefront list was found:** the `Content-Security-Policy: frame-ancestors` header on `tpp.spinxbi.com` enumerates every domain permitted to frame the gateway. That header is the authoritative inventory of SpinX's payment surface and it names 21 hosts, including `shop.cash-frenzy.com` and `webtest.cash-frenzy.com` — which is how the Cash Frenzy store was reached after `cashfrenzy.com` and `cfweb.spinxgames.com` had failed. The header also lists `http://myfile.bolevpn.com`, over plain HTTP, tying back to the Beijing Bole entity.

**Conclusion:** the country profile is **unverified**, and therefore the APM gap analysis in Section 4 is presented per *confirmed payment surface* rather than per *traffic market*, and two ICP signals score zero. No country split has been invented.

---

## Section 2: Legal Entities & Local Presence

**Headquarters:** Hong Kong. Founded **2014** ([pocketgamer.biz](https://www.pocketgamer.biz/netmarble-picks-up-social-casino-developer-spinx-games-for-219-billion)). ⚠️ District disputed — Sheung Wan per pocketgamer.biz; Kowloon (33 Canton Road) per the German App Store listing `[UNVERIFIED — search summary only, page not fetched]`.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Hong Kong | SpinX Games Limited | Not found | [apps.apple.com](https://apps.apple.com/US/app/id1356980152) (seller of record); [jackpot-world.com](https://www.jackpot-world.com/en/support/faq) (footer, *"Copyright © 2020-2026 SpinX Games Ltd."*) |
| Not established | Grande Games Limited | Not found | [topclassactions.com](https://topclassactions.com/lawsuit-settlements/consumer-products/mobile-apps/spinx-games-grande-games-beijing-bole-technology-casino-apps-3-5m-class-action-settlement/); Android package `com.grandegames.slots.dafu.casino` ([bluestacks.com](https://www.bluestacks.com/campaign/com.grandegames.slots.dafu.casino/tr/)) |
| China | Beijing Bole Technology Co., Ltd. | Not found | [topclassactions.com](https://topclassactions.com/lawsuit-settlements/consumer-products/mobile-apps/spinx-games-grande-games-beijing-bole-technology-casino-apps-3-5m-class-action-settlement/); help centre served from `bolegames.helpshift.com`, titled *"SpinX Games Support"* ([bolegames.helpshift.com](https://bolegames.helpshift.com/hc/en/14-jackpot-world/)) |
| Cayman Islands | Leonardo Interactive Holdings (parent vehicle) | Not found | [gamblinginsider.com](https://www.gamblinginsider.com/news/12749/netmarble-purchases-spinx-after-acquiring-leonardo-interactive-holdings); [yogonet.com](https://www.yogonet.com/international/news/2021/08/02/58626-south-korean-game-developer-netmarble-acquires-social-casino-spinx) |
| South Korea | Netmarble Corporation (ultimate parent, KOSPI 251270) | Not found | [pocketgamer.biz](https://www.pocketgamer.biz/netmarble-picks-up-social-casino-developer-spinx-games-for-219-billion) |

> **MANUAL:** Verify all five against the Hong Kong Companies Registry and China's NECIPS. No registration number was obtainable for any entity in this environment.

**Cross-Border Gap Analysis:**

⚠️ This table normally keys off top-10 traffic. **There is no traffic data for any storefront**, so the "In Top 10 Traffic?" column cannot be completed for any row. It is keyed instead to **confirmed payment surfaces**, which is a weaker basis and is marked as such.

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| Hong Kong | **Unknown — no data** | ✅ SpinX Games Limited | No | Low. Airwallex's **Hong Kong** entity processes the cards and the merchant is HK-domiciled. |
| Taiwan | **Unknown — no data** | ❌ None found | Verify — not sourced this run | **High.** A live, localised, cash-accepting storefront with GASH and MyCard both integrated, and no Taiwanese entity found. |
| Japan | **Unknown — no data** | ❌ None found | Verify — not sourced this run | **High.** A live Japanese storefront and a 特定商取引法 disclosure (gate finding) imply direct selling to Japanese consumers with no Japanese entity found. |
| United States | **Unknown — no data** | ❌ None found | No | Moderate. Likely the largest market by revenue (Netmarble group N.A. = 39%, 4Q25) with cards acquired via a Hong Kong processor entity. |
| China | **Unknown — no data** | ✅ Beijing Bole Technology Co., Ltd. | Yes, per `apac-payments.md` §2 — **verify currently** | Not assessable. No Alipay, WeChat Pay or UnionPay anywhere in the stack, so there is no evidence of a mainland consumer payment surface at all. |

> *"Warning: Potential cross-border operation in Taiwan, Japan and the United States. No local entity found in any of the three. Transactions are likely processed cross-border, with higher scheme costs, lower approval rates and FX exposure."*

> *"Regulatory gate: `apac-payments.md` §2 flags domestic acquiring in China, India, Indonesia, Vietnam and South Korea as effectively gated behind local entity and/or local licensing. **This run did not source current rules for any of those markets and therefore asserts no mandate.** Verify before using in outreach — per the reference's own standing instruction, nothing in that file may be stated as fact on its own authority."*

---

## Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Global (incl. US, JP, TW, HK) | **Airwallex** — primary card processor, 32 hits | `[Source Code]` `[Terms/Privacy Policy]` | [index-a6b23cbd.js](https://d13ac69ufeumng.cloudfront.net/live/assets/index-a6b23cbd.js) · [tpp gateway bundle](https://d13ac69ufeumng.cloudfront.net/payment/test/assets/index-4dee6280.js) (48 hits) |
| Taiwan (+ ja-localised) | **GASH** (Gamania) — 147 hits web, 21 gateway | `[Source Code]` `[Checkout]` | [index-a6b23cbd.js](https://d13ac69ufeumng.cloudfront.net/live/assets/index-a6b23cbd.js) · [jackpot-world.com/en/shop/gash](https://jackpot-world.com/en/shop/gash) |
| Taiwan | **MyCard** — 73 hits | `[Source Code]` `[Checkout]` | [index-a6b23cbd.js](https://d13ac69ufeumng.cloudfront.net/live/assets/index-a6b23cbd.js) |
| Global | **Appcharge** — production tokens on 5 storefronts | `[Source Code]` `[Checkout]` | [shop.cash-frenzy.com](https://shop.cash-frenzy.com/) · [cashclubcasino.com](https://cashclubcasino.com/) · [prime.jackpot-crush.com](https://prime.jackpot-crush.com/) · [jackpot-wins.com](https://jackpot-wins.com/) · [LS bundle](https://d13ac69ufeumng.cloudfront.net/LS/assets/index-0885118a.js) |
| Global | **PayPal** — 4 hits web, 19 gateway | `[Source Code]` | [index-a6b23cbd.js](https://d13ac69ufeumng.cloudfront.net/live/assets/index-a6b23cbd.js) |
| Russia only (**currently closed**) | **Xsolla** — 7 hits | `[Source Code]` | [index-a6b23cbd.js](https://d13ac69ufeumng.cloudfront.net/live/assets/index-a6b23cbd.js) |
| Global (wallet on own checkout) | **Apple Pay** — `applePayButton.vue` bundled into `/payment/DF/WEB` and `/payment/DF/EXE` alongside `airwallex-42209866.js`, 14 hits | `[Source Code]` | [tpp gateway bundle](https://d13ac69ufeumng.cloudfront.net/payment/test/assets/index-4dee6280.js) |

**Airwallex is the sole card processor.** No second card acquirer appears anywhere in any bundle. GASH and MyCard are voucher/wallet rails for Taiwan, not card acquirers; Appcharge is a web-shop vendor; PayPal is a wallet; Xsolla is closed. **The underlying acquiring bank behind Airwallex is not disclosed and was not established** — searches returned Airwallex's Hong Kong SVF licence (via the UniCard acquisition) and an SFC asset-management licence, neither of which is a merchant-acquiring arrangement.

**Airwallex API surface, verbatim from the bundle:** `createAirwallexIntent`, `authorizeAirwallex`, `airwallexCallback`, `airwallexModal`, `showAirwallexModal`.

**Stored credentials — confirmed:** `/token/createPaymentConsents`, `/token/updatePaymentConsents`, `/token/disablePaymentConsents`, `/windows/disablePaymentConsents`, `getConsentInfo`, `saveUserConsent`, `setConsent`, `save_card`. **SpinX operates its own saved-card vault on Airwallex Payment Consents, including a Windows-client consent path.** They run stored-credential flows themselves rather than delegating them.

**Other confirmed endpoints:** `/payment/getPaymentConfig` (the live channel config), **`/payment/getLocalPrice`** (local-currency pricing), `/token/sendPaymentErrMsg` (client-side payment-failure telemetry), `/paymentNew/common/getPaymentUrl`, `/paymentNew/common/getAppchargeUrl`, `/paymentNew/pl/createAppchargePreview`, `/paymentNew/paypal/authorizeIntent`, `/gash/getGashRate`, `/gash/getPaymentHtml`, `/gash/gashCallback`, `/mycard/getMycardRate`, `/mycard/myCardTrade`, `/token/getXsollaUrl`.

**False positives recorded and dismissed on context inspection** — logged so the next run does not re-chase them:

| Apparent hit | Count | What it actually was |
|---|---|---|
| `dlocal` | 8 / 5 / 26 / 5 | `appendLocaleToChain`, `loadLocaleMessages`, `domainFromLocale` — i18n machinery |
| `omise` | 74 / 67 / 102 / 92 | `Promise` |
| `sofort` | 9 | The German word *sofort* ("immediately") in the de i18n bundle |
| `upi` | 8 / 9 | `getTopupInfo`, `topupActCollect`, `topup…` |
| `boku` | 1 | The chunk filename `BGBOKU_4.js` |
| `fpx` / `doku` / `qris` | 5 / 1 / 1 | Base64 noise inside inline data URIs |
| `wechat` | 2 | A donation link in the bundled `eruda` debug console (`surunzi.com/wechatpay.html`) — a third-party dev tool, not an integration |

#### 3B. Payment Orchestrator

**Classification: IN-HOUSE ORCHESTRATION LAYER — built, but routed by hand. `[Source Code]`**

Evidence, all first-hand on 2026-10-09:

**1. They own the gateway.** `tpp.spinxbi.com` returns HTTP 200. Metadata verbatim: *"Spinx Games, Third Party Payment, Online Payment, Jackpot World, Cash Frenzy, Airwallex, Paypal"*; description: *"your reliable platform for secure third-party payment solutions… including popular games like Jackpot World and Cash Frenzy."* Its router enumerates eleven routes — three channels per title:

```
/payment/CF/APP   /payment/CF/EXE   /payment/CF/WEB      (CF = Cash Frenzy)
/payment/DF/APP   /payment/DF/EXE   /payment/DF/WEB      (DF = DAFU / Jackpot World)
/payment/appcharge   /paypal/DF/website   /airwallex/DF/APP   /payment   /
```

`WEB` = browser storefront, `EXE` = the downloadable Windows client (corroborated by the state fields `price_exe`, `currency_exe`, `uid_exe`, `saveExePayDetail` and the route `/windows/disablePaymentConsents`), `APP` = **a SpinX-controlled payment flow inside the mobile app — alternative/external billing, not IAP.**

**2. The routing config, live from the server today, not the shipped default.** Captured from the SSR `__INITIAL_STATE__` of `jackpot-world.com/en/shop/token`:

```json
"token": { "is_close": false,
  "payment_channel": ["appcharge","airwallex","paypal"],
  "payment_config": {
    "airwallex":{"is_close":false,"close_date":[1760889600000,1760950800000]},
    "paypal":   {"is_close":false,"close_date":[1729353600000,1729414800000]},
    "xsolla":   {"is_close":true},
    "appcharge":{"is_close":false,"close_date":[1769097600000,1772208000000]}},
  "close_date":["2025-10-20 00:00:00","2025-10-21 00:00:00"] },
"card":  { "is_close": false,
  "payment_channel": ["gash","mycard"],
  "payment_config": {
    "gash":  {"is_close":false,"close_date":[1789401600000,1789488000000]},
    "mycard":{"is_close":false,"close_date":["2025-06-08T23:59:59.000Z","2025-06-09T01:31:00.000Z"]}},
  "close_date":["2025-09-15 00:00:00","2025-09-16 00:00:00"] }
```

**3. It is routing by hand, and the hand-set state has drifted.** Four distinct findings:

- 🔑 **Channel availability is managed through dated, per-channel kill switches, logged to the minute.** Decoded windows: PayPal 2024-10-19 16:00→2024-10-20 09:00; Airwallex 2025-10-19 16:00→2025-10-20 09:00; MyCard 2025-06-08 23:59:59→2025-06-09 **01:31**; GASH 2026-09-14 16:00→2026-09-15 16:00; Appcharge 2026-01-22→2026-02-27. **A 91-minute MyCard window recorded to the minute is a human scheduling a vendor outage by hand.** This is the orchestration pain in raw form, and it is dated evidence rather than inference.
- 🔑 **Two storefronts for the same title carry two different, independently maintained configs.** `dafu.spinxbi.com` is titled *"Jackpot World-Free Slots & Vegas Casino Games Online"* — the same title as `jackpot-world.com` — yet serves `"card": {"is_close": true}`, `"token": {"is_close": true}`, `"appcharge": {"is_close": true}`, a **different channel order** (`["airwallex","paypal","appcharge"]` rather than `["appcharge","airwallex","paypal"]`), and close windows that **expired on 2026-09-01, five weeks before this report**. Because the drop condition is `is_close && now < close_date[1] && now > close_date[0]`, those lapsed windows mean the channels are *not* actually dropped — the flags are set true against windows that have already closed. **The config is internally contradictory and nobody has reset it.** That is what hand-managed routing looks like after a year.
- 🔑 **Airwallex cannot be switched off by the kill-switch logic.** The channel-filter function excludes it explicitly: `c.is_close && … ? p!=="airwallex" && (a.push(p), …) : a.push(p)`. The sole card processor is hard-wired past the only failover mechanism in the system. **There is no card failover. At all.**
- 🔑 **There is almost no geography in the system.** The entire country logic across the whole stack is one string: `zf = async t => { if (t === "RU") return ["xsolla"]; … }`. And `xsolla` is `is_close: true` in the live config — **a Russian user is routed to a channel the config marks closed.** In the payment gateway itself, `country`/`region` keywords appear twice, both inside `Intl.NumberFormat` option lists. No BIN routing, no issuer-geography logic, no per-market channel selection anywhere.

**4. Per-channel user allowlists are hard-coded.** `{appcharge:[], airwallex:[], mycard:[], gash:[], paypal:[23293042]}` — PayPal is gated to a single hard-coded user id.

**5. And the newer titles bypass all of it.** Lotsa Slots, Cash Frenzy, Jackpot Wins, Cash Club Casino and Jackpot Crush do **not** route through `tpp.spinxbi.com`. Each is a Nuxt storefront carrying a production Appcharge token and nothing else — zero hits for Airwallex, GASH, MyCard, PayPal or Xsolla in any of their bundles. Lotsa Slots' only payment calls are `/payment/getTokenConfig`, `/payment/getAppchargeUrl` and `/payment/sendPaymentErrMsg`, with the checkout payload `priceDetails{price,currency}`, `offer{name:"Lotsa Cash", sku}` and line-item SKUs.

> **This is the finding that decides the motion.** SpinX built an in-house router for its flagship, then declined to put six newer storefronts on it, reaching instead for a single specialist vendor. They have already concluded that hand-routing does not scale. But Appcharge is a **web-shop and merchant-of-record product**, not a routing layer: it supplies the storefront, the checkout and the tax/MoR wrapper. ([TechCrunch](https://techcrunch.com/2024/11/25/appcharge-raises-26m-to-help-gaming-apps-cut-out-apple-and-google-from-virtual-goods-revenues) reports Appcharge acts as merchant of record and sets up local merchant accounts; [appcharge.com](https://appcharge.com) advertises 500+ methods and 100+ currencies — **company marketing, not independently verified, and whether SpinX uses the MoR tier or the plain Checkout tier is NOT established.**) The result is a company with two payment architectures, neither of which routes: a hand-managed router with no card failover on the flagship, and single-vendor dependency on everything new.

> *"Confirmed orchestration-aware — they built their own. The opening is reach and opportunity cost, not the case for orchestration itself. Do not tell SpinX they need orchestration; they will correctly reply that they have run one for years."*

> **MANUAL:** Walk `shop.cash-frenzy.com` and `jackpot-world.com/en/shop/token` through DevTools with a funded account. Confirm whether Appcharge is engaged as merchant of record or as checkout-only, and capture the live method list Appcharge renders per geography — that is the one thing source code cannot tell you.

---

## Section 4: Alternative & Local Payment Methods

⚠️ **This section cannot be organised by traffic share**, because no traffic data exists for any storefront (Section 1). It is organised by **confirmed payment surface**. Every "Not found" below is a **zero-hit result from a keyword scan of six decompressed production bundles**, which is a sourced absence rather than an assumption.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| Global | Cards (via Airwallex) | Cards | **Active in checkout** | [JW bundle](https://d13ac69ufeumng.cloudfront.net/live/assets/index-a6b23cbd.js) — `cardNumber`, `cvc`, `createAirwallexIntent` |
| Global | Apple Pay | Digital wallet | **Active in checkout** | [tpp bundle](https://d13ac69ufeumng.cloudfront.net/payment/test/assets/index-4dee6280.js) — `applePayButton.vue` in `/payment/DF/WEB` + `/EXE` |
| Global | PayPal | Digital wallet | **Active in checkout** (gated to one uid in the bundle default) | [JW bundle](https://d13ac69ufeumng.cloudfront.net/live/assets/index-a6b23cbd.js) — `/paymentNew/paypal/authorizeIntent` |
| Global | Saved cards / stored credentials | Cards | **Active** — own vault on Airwallex consents | `createPaymentConsents`, `save_card`, `/windows/disablePaymentConsents` |
| Global | Appcharge aggregated methods | Multiple | **Active in checkout** on 5 storefronts; **specific methods not establishable from source** | [shop.cash-frenzy.com](https://shop.cash-frenzy.com/) |
| 🇹🇼 Taiwan | **GASH** (convenience-store cash voucher) | **Cash/voucher** | **Active in checkout** | [jackpot-world.com/en/shop/gash](https://jackpot-world.com/en/shop/gash), 147 bundle hits, `/gash/getGashRate`, `/gash/getPaymentHtml`, "GASH Order History" |
| 🇹🇼 Taiwan | **MyCard** | **Digital wallet / voucher** | **Active in checkout** | 73 bundle hits, `/mycard/myCardTrade`, "MyCard Order History" |
| 🇹🇼 Taiwan | JKOPay | Digital wallet | **Not found** (0 hits) | Bundle scan |
| 🇹🇼 Taiwan | LINE Pay | Digital wallet | **Not found** (0 hits) | Bundle scan |
| 🇹🇼 Taiwan | ATM / virtual-account transfer | Bank transfer / A2A | **Not found** (0 hits) | Bundle scan |
| 🇹🇼 Taiwan | Domestic instalments | BNPL/Instalments | **Not found** (0 hits) | Bundle scan |
| 🇯🇵 Japan | konbini (convenience-store cash) | **Cash/voucher** | **Not found** (0 hits) | Bundle scan |
| 🇯🇵 Japan | PayPay | Digital wallet | **Not found** (0 hits) | Bundle scan |
| 🇯🇵 Japan | LINE Pay / Rakuten Pay | Digital wallet | **Not found** (0 hits) | Bundle scan |
| 🇯🇵 Japan | Carrier billing | Carrier billing | **Not found** — Boku, Fortumo, Centili all 0 | Bundle scan |
| 🇯🇵 Japan | Paidy | BNPL/Instalments | **Not found** (0 hits) | Bundle scan |
| 🇭🇰 Hong Kong | FPS / Octopus / AlipayHK / WeChat Pay HK | A2A / wallet | **Not found** (0 hits) | Bundle scan |
| 🇨🇳 China | Alipay / WeChat Pay / UnionPay | Digital wallet | **Not found** (0 hits) | Bundle scan |
| 🇮🇳 India | **UPI**, netbanking, RuPay, EMI, Paytm | A2A / cards / instalments | **Not found** (0 hits — the 8–9 apparent `upi` hits were `getTopupInfo`) | Bundle scan |
| 🇮🇩 Indonesia | **QRIS**, GoPay, OVO, DANA, virtual account, Alfamart/Indomaret | A2A / wallet / cash | **Not found** (0 hits) | Bundle scan |
| 🇸🇬 Singapore | **PayNow**, GrabPay | A2A / wallet | **Not found** (0 hits) | Bundle scan |
| 🇲🇾 Malaysia | **FPX**, DuitNow, Touch 'n Go | A2A / wallet | **Not found** (0 hits — the 5–6 apparent `fpx` hits were base64) | Bundle scan |
| 🇹🇭 Thailand | **PromptPay**, TrueMoney | A2A / wallet | **Not found** (0 hits) | Bundle scan |
| 🇵🇭 Philippines | **GCash**, Maya, OTC cash | Wallet / cash | **Not found** (0 hits) | Bundle scan |
| 🇻🇳 Vietnam | MoMo, ZaloPay, VNPay | Wallet / A2A | **Not found** (0 hits) | Bundle scan |
| 🇦🇺🇳🇿 ANZ | PayTo, BPAY, Afterpay, Zip, POLi | A2A / BNPL | **Not found** (0 hits) | Bundle scan |
| 🇷🇺 Russia | Xsolla | Multiple | **Deprecated** — `is_close: true` in live config, yet still hard-routed in code | SSR `payment_config` |

**🔑 Taiwan is the strongest confirmed APAC surface, and it is a cash surface.** GASH *and* MyCard are both integrated — two competing Taiwanese rails side by side, which is itself a sign of hand-assembled coverage rather than a routed strategy. The site is localised to zh-hant as **大福Online** (confirmed by byte-level CJK detection on the zh-hant pages). GASH points are bought as cash in convenience stores: [BitTopup](https://news.bittopup.com/news/gash-card-taiwan-top-up-guide-spring-2026-promotions) reports 7-Eleven and FamilyMart carry physical GASH cards with a 500-point minimum ⚠️ *(BitTopup is a competing seller of GASH PINs and its figures are partly community estimates — treat as indicative, and verify against gash.com.tw before using in outreach)*. **This is live convenience-store cash acquiring in a territory market.**

🔑 **And it visibly fails on region mismatch.** SpinX ships this consumer-facing error string, verbatim from the gateway bundle: **`text_3907: "Wrong GASH card region, please confirm the region and try again."`** — alongside `text_2001: "This GASH card has already been used"` and `text_2: "Wrong GASH card password…"`. The GASH flow is region-locked and SpinX surfaces the mismatch as a hard decline to the player. The whole redemption flow is also localised into **Japanese** (`deposit_method_gash: "GASH"`, `GASHポイント`, `チャージ失敗`), which means Japanese-language players are being offered a Taiwan-region voucher rail that can reject them on region.

**🔑 Japan sells direct but accepts almost nothing Japanese.** The `ja` storefront is live and rendering (70,642 bytes, hiragana confirmed), the payment gateway carries full `ja` localisation, and the Phase 0 gate verified a **特定商取引法** (Act on Specified Commercial Transactions) disclosure at `spinxgames-policy.com` — a filing required of a merchant selling direct to Japanese consumers, so the Japanese web store is operating, not planned. ⚠️ *I could not re-open that document in this environment: the policy host is a document-by-id SPA (`/:id/view`) whose content loads from an API, and the bundle contains no legal text. Carried as a gate finding.* Against that live Japanese surface: **no konbini, no PayPay, no LINE Pay, no Rakuten Pay, no carrier billing, no Paidy.** Cards and Apple Pay only.

> *"Warning: In Japan, konbini and PayPay are widely used but not currently supported by SpinX."* — Prominence per `apac-payments.md` §2, which is a checklist and **not a citable source**. ⚠️ **Source the Japanese share figures live before putting any number in an email.**

> *"Warning: In Taiwan, JKOPay, LINE Pay and ATM/virtual-account transfer are widely used but not currently supported by SpinX."* — Same caveat: source before citing.

> **MANUAL:** VPN into Taiwan, Japan and Hong Kong and capture the live method list the Appcharge checkout renders on `shop.cash-frenzy.com`. Appcharge advertises 500+ methods; whether SpinX has any of them *enabled* for those markets is the single biggest unknown left in this report, and it is not answerable from source code.

---

## Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| **Duplicate charges** — *"New policy you get money taken twice for one pack."* | Trustpilot (Adriana C) | Isolated — 1 instance | 2023-08-26 | [trustpilot.com/review/spinxgames.com](https://www.trustpilot.com/review/spinxgames.com) |
| **Unrecognisable statement descriptor → chargeback** — *"Seen charges labeled as other, disputed with bank"* | Trustpilot (Fence Post) | Isolated — 1 instance | 2025-05-16 | [trustpilot.com/review/spinxgames.com](https://www.trustpilot.com/review/spinxgames.com) |
| Coins purchased but not credited | App Store review, reported second-hand; reviewer *"disputed with iTunes and within a couple of days, received a full refund"* | Isolated | Not dated | `[UNVERIFIED — search summary only, page not fetched]` |

**Overall Trustpilot standing:** TrustScore **2.5 / 5 ("Poor") across 31 reviews, 90% at one star** ([trustpilot.com](https://www.trustpilot.com/review/spinxgames.com)).

⚠️ **Separating payment complaints from the rest, as instructed.** The overwhelming majority of those 31 reviews concern **game economics, not payments** — *"they scam you out of real money for fake in game currency"*, *"Never pays things that you are entitled to properly"*, *"spending lots of real money get you nothing completed"*, *"I have spent well over $1000 dollars on this site"*, *"how I spend 7000 euro to buy items and coins in lotsa slots"*. **These are value and payout grievances about a free-to-play slots economy. They are not payment-infrastructure findings and have not been counted as such.** App crashes, equally, would be an Apple-rail issue and not a SpinX payments issue.

After that filter, **exactly two reviews describe a payment-mechanics failure.** That is **isolated frequency**, and the ICP row scores **zero**. Inflating it would have been easy and wrong.

> *"Pattern: too thin to call a pattern. But the one descriptor complaint is worth noting on its own merits — a cardholder who cannot recognise a charge on their statement disputes it, and a dispute on a social-casino MCC is expensive. An unrecognisable descriptor is a solvable acquiring-configuration problem, and the fact that SpinX bills under at least seven brand names through two architectures makes descriptor hygiene a live risk rather than a theoretical one. Raise it as a question on the call, not as a claim in an email — n=1."*

⚠️ **Google Play and App Store review bodies were not retrievable in this environment.** `apac-payments.md` and the research method both identify app-store reviews as the richest complaint source in APAC, and that source is missing here. The complaint picture rests on 31 Trustpilot reviews for a brochure domain. Treat the "isolated" classification as **weakly evidenced** — see Manual Research Recommendations #3.

---

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | **2026-09-17** | Cash Frenzy storefront built/prerendered at `shop.cash-frenzy.com`, Appcharge production token, `isShopEnable: true` | Payment Infrastructure / Market Expansion | [shop.cash-frenzy.com](https://shop.cash-frenzy.com/) (prerender timestamp 1789629673526) |
| 2 | **2026-09-08** | Jackpot Crush storefront built at `prime.jackpot-crush.com`, Appcharge production token | Payment Infrastructure | [prime.jackpot-crush.com](https://prime.jackpot-crush.com/) (prerender 1788833408307) |
| 3 | **2026-08-28** | Cash Club Casino storefront built at `cashclubcasino.com` with **four locales — `en`, `jp`, `zh_hk`, `de`** | Market Expansion / Payment Infrastructure | [cashclubcasino.com](https://cashclubcasino.com/) (prerender 1787887906562) |
| 4 | **Current, undated** | **Two storefronts staged pre-launch:** Vegas Friends (`vf.spinxbi.com`, `ENV: preview`, `appchargeEnv: sandbox`) and Cash Rally (`cash-rally.com`, 94KB storefront, `payment_config: null`) | Payment Infrastructure | [vf.spinxbi.com](https://vf.spinxbi.com/) · [cash-rally.com](https://cash-rally.com/) |
| 5 | **2026-08-05** | Netmarble Q2 2026: revenue ₩749.2bn (+4.4% YoY), 78% overseas; **Lotsa Slots 7%, Jackpot World 7%, Cash Frenzy 7%** of group revenue | Parent Financials | [invenglobal.com](https://www.invenglobal.com/articles/24480/netmarble-reports-q2-revenue-of-7492-billion-and-operating-profit-of-801-billion) · [pocketgamer.biz](https://www.pocketgamer.biz/netmarble-makes-5051m-in-q2-2026-with-the-seven-deadly-sins-success/) |
| 6 | **2026-02-05** | Netmarble FY2025: revenue **₩2,835bn**; 4Q25 ₩797.6bn; **commission-to-revenue ratio down for a fifth straight quarter to 31.6%**; Jackpot World 7%, Lotsa Slots 6%, Cash Frenzy 6% | Parent Financials / Cost Structure | [sgimage.netmarble.com (Netmarble's own IR host)](https://sgimage.netmarble.com/images/netmarble/nmOfficial/20260205/8sto1770273390151.pdf) |

**Public payment RFP:** *No public payment-related RFP found.*

**Payment-related hiring:** *No SpinX payment-related job posting found.* Searches surfaced payment roles at AviaGames (Hong Kong, Sep 2025), NetEase Games (Hong Kong, treasury) and HoYoverse (Singapore) — **none at SpinX**. SpinX's Dealroom profile lists HQ Hong Kong Island and launch date 2014 but shows no current openings `[UNVERIFIED — search summary only, page not fetched]`.

**Licence applications:** *No public licence application found* in any APAC market.

🔑 **The three dated storefront builds are the strongest buying signal on this account.** Three new storefronts in a three-week window, two more staged pre-launch, all on Appcharge, while the flagship's own router sits on a stale hand-maintained config. A company shipping payment surfaces at that rate is making vendor decisions right now.

---

## Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | **Live, undated** | **Appcharge promoted ahead of Airwallex in the live channel order.** Bundle default `["airwallex","paypal","appcharge"]`; config served 2026-10-09 `["appcharge","airwallex","paypal"]` | **High** — a vendor moved to first position on the flagship token store | [SSR state, jackpot-world.com/en/shop/token](https://jackpot-world.com/en/shop/token) |
| 2 | **Live, undated** | **Xsolla switched off** — `"xsolla": {"is_close": true}` in the live config, while the web bundle still hard-routes `if (t==="RU") return ["xsolla"]` | **High** — a provider removal that the routing code has not caught up with | [SSR state, jackpot-world.com/en/shop/token](https://jackpot-world.com/en/shop/token) |
| 3 | **Expired 2026-09-01** | **DAFU storefront's payment config left in a contradictory state** — `card.is_close: true` and `token.is_close: true` against windows that lapsed five weeks ago | **High** — direct evidence of hand-managed config drift | [dafu.spinxbi.com](https://dafu.spinxbi.com/) |
| 4 | 2026-02-05 → 2026-08-05 | Netmarble's **commission-to-revenue ratio fell for five consecutive quarters: 35.7% → 35.1% → 33.8% → 32.3% → 31.6%**, with the deck noting *"Commission-to-revenue ratio continues to decline"* | **Medium** — consistent with own-channel migration, but the line is undifferentiated (store commissions, IP royalties and PG fees combined), so it does **not** prove it | [sgimage.netmarble.com](https://sgimage.netmarble.com/images/netmarble/nmOfficial/20260205/8sto1770273390151.pdf) |
| 5 | 2024-11-25 | Appcharge raised $26M to help gaming apps bypass Apple and Google for virtual-goods revenue; acts as **merchant of record**, sets up local merchant accounts and handles tax | **Medium** — context on what SpinX's chosen vendor does and does not do | [techcrunch.com](https://techcrunch.com/2024/11/25/appcharge-raises-26m-to-help-gaming-apps-cut-out-apple-and-google-from-virtual-goods-revenues) |

> **REMOVAL: SpinX has switched off Xsolla.** `"xsolla": {"is_close": true}` in the config served on 2026-10-09, while `zf()` in the shipped bundle still routes every `RU` user to it unconditionally. Source: [SSR `payment_config`, jackpot-world.com/en/shop/token](https://jackpot-world.com/en/shop/token). Russia is outside APAC territory, so this is not a revenue story — it is **evidence of what happens when a channel is retired in a hand-managed stack: the config changes and the routing code does not.**

*No payment-specific coverage of SpinX was found in `thepaypers.com`, `finextra.com`, `pymnts.com`, `techinasia.com`, `e27.co` or `entrackr.com`. Everything in this section is first-hand observation or parent-company filings.*

---

## Section 8: Checkout Experience Audit

**Partially accessible.** HTML, SSR state, CSP headers and six production JavaScript bundles were retrieved and read in full. **A funded transaction was not attempted and no account was created**, so every dimension requiring an authenticated session is marked as such. `currencyList: {"coin":[],"token":[]}` is empty until login, and `payment_config` channel availability resolves per-user.

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | **Custom-built, self-hosted** on `tpp.spinxbi.com` for Jackpot World / DAFU / Cash Frenzy; **third-party hosted** (Appcharge) for the five Nuxt storefronts | Fair | Two architectures in one company |
| Guest checkout | **No.** `is_login_store: false` gates the store; Facebook and Google OAuth redirect handlers on every storefront (`fbRedirectUrl`, `ggRedirectUrl`) | Poor | Account required — expected for virtual-currency crediting, but it is friction |
| Steps to complete payment | Not determinable without an authenticated session | Unknown | |
| Card input experience | SpinX renders its own field chrome — i18n strings `cardNumber_placeholder`, `cvc_placeholder`, `expiry_placeholder`, `firstname_placeholder` with validation messages — around Airwallex components loaded from `airwallex-42209866.js` | Fair | `[INFERENCE, not confirmed]`: own form furniture over Airwallex hosted inputs. Whether the card fields are Airwallex-hosted iframes or SpinX-served DOM **was not established and determines PCI scope** |
| Payment methods visible | Token store: Appcharge, Airwallex (cards), PayPal, Apple Pay. Card store: GASH, MyCard | Fair | Two separate stores with two separate channel sets — the player must know which store to enter |
| Location-based method display | **Effectively none.** The only country condition in the stack is `if (t==="RU")`. The gateway contains no country routing at all | **Poor** | A player in Tokyo and a player in Taipei are offered the same channel list, which the GASH region error then rejects |
| Instalment / EMI options | **Not found** (0 hits). Absent in Japan and Taiwan, both instalment-cultured markets per `apac-payments.md` §2 | Poor | Low-ticket top-ups, so commercially minor |
| 3DS implementation | **Not detected.** Zero hits for `3ds`/`threeds` in the gateway bundle | Unknown | Likely handled inside Airwallex's own flow — `[INFERENCE, not confirmed]` |
| PCI indicator | PSP-integrated via the Airwallex SDK; card data posted to Airwallex per the consumer disclosure | Fair | See Section 9 |
| Mobile responsiveness | Strong. PWA manifests on most storefronts, `apple-mobile-web-app-title` set ("JW Store", "LS PWA", "SM PWA"), `webStorePC`/`webStoreMobile` component split, mobile viewport locks | **Good** | App-first market handled properly |
| Multi-currency / local pricing | **Yes** — a dedicated `/payment/getLocalPrice` endpoint, plus `currency`, `formatted_price`, `default_price`, `currency_exe` in state and `Intl.NumberFormat` in the gateway | **Good** | Local pricing is genuinely built |
| Saved payment methods | **Yes** — own vault on Airwallex Payment Consents, including a Windows-client path (`/windows/disablePaymentConsents`) | **Good** | `save_card`, `setConsent`, `getConsentInfo` |
| Error message clarity | **Specific and well-built for GASH** — `text_2001` (card already used), `text_2` (wrong password), `text_3907` (wrong card region) — plus a client-side failure telemetry endpoint `/token/sendPaymentErrMsg` and `is_show_topupfailure_modal` | **Good** | They instrument and explain failures. The decline *causes* are the problem, not the messaging |

**Notable build-hygiene observation, stated as observed and not as a security claim:** the production payment gateway serves its bundle from `https://d13ac69ufeumng.cloudfront.net/payment/**test**/assets/index-4dee6280.js`, and the Jackpot World GASH store loads its favicon from `/test/logo_new.png`. Separately, the SSR `payment_url` default embedded identically in all four Jackpot World / DAFU pages points at **`checkout-v2-sandbox.appcharge.com`** with `product=CR`. Because that value and its session token are **byte-identical across four different pages**, it is a **static placeholder in the shipped initial state, not a live session** — so this is *not* evidence that SpinX processes real money through a sandbox. It is evidence that production and non-production artefacts are not cleanly separated. Raise it as an engineering observation if it comes up; do not lead with it.

---

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **Not found** | No PCI documentation, AOC or compliance statement found for SpinX Games Limited |
| Card data handling | **Not established.** `[INFERENCE, not confirmed]`: likely reduced scope. The consumer disclosure states card data goes to Airwallex — *"you will provide your payment information and purchase information to Airwallex"* — and integration is via the Airwallex SDK (`createAirwallexIntent` → `authorizeAirwallex` → `airwallexCallback`), which points to **SAQ A-EP** rather than SAQ A, because SpinX serves the payment page itself from `tpp.spinxbi.com` and renders its own field chrome. **Whether the card inputs are Airwallex-hosted iframes or SpinX-served DOM was not determined, and that distinction is exactly what decides SAQ A vs A-EP.** | [JW bundle](https://d13ac69ufeumng.cloudfront.net/live/assets/index-a6b23cbd.js) |
| Tokenization approach | **Own vault on Airwallex Payment Consents.** `createPaymentConsents`, `updatePaymentConsents`, `disablePaymentConsents`, `/windows/disablePaymentConsents`, `saveUserConsent`, `save_card` | [JW bundle](https://d13ac69ufeumng.cloudfront.net/live/assets/index-a6b23cbd.js) |
| Recommended Yuno integration | **SDK**, not back-to-back API | Rationale below |

*No direct PCI compliance documentation found publicly for SpinX Games.*

> `[INFERENCE, not confirmed]`: Based on confirmed use of Airwallex SDK-based checkout with stored payment consents, the company's PCI scope is likely reduced, with Airwallex handling card data. **Yuno's SDK is the right integration shape**: it preserves the reduced scope SpinX already has, and it matters more here than usual because they run stored credentials themselves — a back-to-back API integration would pull card data into SpinX's own scope and reverse a decision they have already made. **Network tokens and account updater inside the routing layer is the concrete mechanism to lead with**, since they are already managing consents by hand across one processor.

---

## Section 10: Strategic Insights & Outreach Angles

> ### Insight #1: The only card processor is the one channel that cannot be switched off
> **Evidence:** **Section 3A** — Airwallex is the sole card acquirer across every bundle; no second card processor appears anywhere ([JW bundle](https://d13ac69ufeumng.cloudfront.net/live/assets/index-a6b23cbd.js)). **Section 3B** — the kill-switch filter explicitly exempts it: `c.is_close && … ? p!=="airwallex" && (a.push(p), …) : a.push(p)`, and the no-config fallback is `const or = ["airwallex"]` ([same bundle](https://d13ac69ufeumng.cloudfront.net/live/assets/index-a6b23cbd.js)). **Section 8** — no country-based method selection anywhere.
> **Pain Point:** SpinX built a kill switch for every channel *except* the one that carries the cards. If Airwallex degrades in a corridor — a BIN range, an issuer, a region — there is no mechanism in the system to move that traffic. The hand-set `is_close` flags, the one tool they have, cannot touch it. Every card decline in every market is final.
> **Yuno Value Proposition:** Multi-acquirer routing with automated failover on decline code and issuer geography, so a degrading corridor reroutes without a deploy and without someone editing a config at 1am. They already have the config plumbing and the failure telemetry (`/token/sendPaymentErrMsg`) — what is missing is a second card path and the logic to choose it.
> **Best Success Case:** **NetEase Games** — same profile of a Greater-China-rooted publisher selling virtual goods across many markets on a self-built stack. ⚠️ Name only; no published metrics exist, so attach no number.
> **Outreach Angle:** Their own code exempts Airwallex from the only failover mechanism they have — worth asking what happens on a bad day in a single corridor.
> **Suggested Subject Line:** The one channel your kill switch can't reach

> ### Insight #2: Six new storefronts went to a single vendor rather than onto the router they already own
> **Evidence:** **Section 3B** — Lotsa Slots, Cash Frenzy, Jackpot Wins, Cash Club Casino and Jackpot Crush carry a production Appcharge token and **zero** hits for Airwallex, GASH, MyCard, PayPal or Xsolla; Lotsa Slots' only payment calls are `/payment/getAppchargeUrl` and `/payment/getTokenConfig` ([LS bundle](https://d13ac69ufeumng.cloudfront.net/LS/assets/index-0885118a.js)). **Section 6** — three of those were built in a three-week window, 2026-08-28 to 2026-09-17, with two more staged pre-launch ([shop.cash-frenzy.com](https://shop.cash-frenzy.com/), [cashclubcasino.com](https://cashclubcasino.com/), [vf.spinxbi.com](https://vf.spinxbi.com/)).
> **Pain Point:** They have already decided that hand-routing the in-house gateway does not scale to new titles — that is what the Appcharge choice says. But they have swapped hand-routing for single-vendor dependency, and Appcharge is a web-shop and merchant-of-record product, not a routing layer ([techcrunch.com](https://techcrunch.com/2024/11/25/appcharge-raises-26m-to-help-gaming-apps-cut-out-apple-and-google-from-virtual-goods-revenues)). Five live storefronts now have exactly one path to money, and the flagship's hand-built router and the new titles' vendor stack share nothing — no common reporting, no common vault, no common failover.
> **Yuno Value Proposition:** One integration behind every storefront, so a new title inherits the whole provider and rail set on day one instead of starting from one vendor, and so the flagship and the new titles stop being two companies. **Respect the build** — the in-house gateway was the right call for 2020; the question is whether every new storefront should cost a vendor decision.
> **Best Success Case:** **inDrive** — stated plainly as a **pattern match for multi-country scale**, not a gaming case: a merchant that needed one integration rather than a per-market build each time it opened a surface.
> **Outreach Angle:** Three new storefronts in three weeks, all on one vendor, none on the gateway they already run — that is a pattern worth a conversation before the next two launch.
> **Suggested Subject Line:** Cash Rally and Vegas Friends — before they go live

> ### Insight #3: A live Japanese and Taiwanese storefront, and not one Japanese or Taiwanese rail beyond a region-locked voucher
> **Evidence:** **Section 4** — the `ja` storefront renders live (70,642 bytes, hiragana confirmed), the gateway is fully ja-localised, and the gate verified a 特定商取引法 filing, which is required only of a merchant selling direct to Japanese consumers; against that, **konbini, PayPay, LINE Pay, Rakuten Pay, Paidy and carrier billing all return zero hits**. Taiwan has GASH and MyCard but **no JKOPay, no LINE Pay, no ATM transfer, no instalments** ([JW bundle](https://d13ac69ufeumng.cloudfront.net/live/assets/index-a6b23cbd.js)). **Section 2** — no local entity found in either market. **Section 4 again** — and the one cash rail they do have ships a region-decline string, `text_3907: "Wrong GASH card region, please confirm the region and try again."`
> **Pain Point:** They went to the trouble of a Japanese legal filing and a Japanese storefront, then offered Japanese players cards, Apple Pay, and a Taiwanese voucher that can reject them for being in the wrong region. Every non-card Japanese payer is unaddressed, and every cross-border card is acquired through a Hong Kong entity into Japanese issuers.
> **Yuno Value Proposition:** Local rails for both markets through one integration — konbini and PayPay for Japan, the domestic Taiwanese wallets alongside the voucher rails they already run — plus local acquiring in the cardholder's geography to lift approval on the cards they are already losing. The corridor argument here is specific and supportable: cards issued in Japan processed against a Hong Kong entity.
> **Best Success Case:** **Garena** — named as the APAC gaming reference closest to this rail-coverage problem. ⚠️ No published metrics; attach no number.
> **Outreach Angle:** They filed a 特商法 disclosure to sell direct in Japan and then shipped a checkout with no konbini and no PayPay — the filing says the intent is there.
> **Suggested Subject Line:** 特商法 filed, konbini missing

> ### Insight #4: The hand-managed config has already drifted, and it is visible from outside
> **Evidence:** **Section 3B** — `dafu.spinxbi.com` and `jackpot-world.com` are the same title (identical `<title>`) on two web properties serving **different** channel orders and different kill-switch state, with DAFU's `is_close: true` flags set against windows that **expired 2026-09-01** ([dafu.spinxbi.com](https://dafu.spinxbi.com/)). **Section 7** — Xsolla is `is_close: true` in the live config while the shipped code still hard-routes every `RU` user to it ([SSR state](https://jackpot-world.com/en/shop/token)). **Section 3B again** — per-channel user allowlists are hard-coded, with PayPal gated to the single uid `23293042`, and a MyCard outage window is recorded to the minute (23:59:59 → 01:31).
> **Pain Point:** Channel availability is a human job here, performed per storefront, and it has not been reconciled in over a year. A minute-precise vendor outage window logged by hand is someone's evening. Two fronts for one title with divergent configs means a change has to be made twice and was not. A retired provider still being routed to means the code and the config have separate owners.
> **Yuno Value Proposition:** Channel availability becomes a rule rather than a date typed into a config — provider health drives routing, one control plane covers every storefront, and retiring a provider is one change rather than a config edit plus a code deploy plus remembering the second front.
> **Best Success Case:** **Rappi** — stated plainly as a **pattern match for provider breadth** across many providers and rails under one control plane, not as a gaming case.
> **Outreach Angle:** Two Jackpot World fronts are serving two different payment configs, and one of them has had its channels flagged closed since early September — that is the cost of managing this by hand.
> **Suggested Subject Line:** Your two Jackpot World fronts disagree

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. Your channel-filter code exempts Airwallex from the kill switch (`p!=="airwallex"`), which means the one provider carrying all your cards is the one you cannot route around.
2. Cash Frenzy, Jackpot Crush and Cash Club Casino all went live in a three-week window in late August and September, each on a single payment vendor, none of them on the gateway you already run at `tpp.spinxbi.com`.
3. You filed a 特定商取引法 disclosure to sell direct to Japanese consumers and then shipped a Japanese storefront with no konbini and no PayPay on it.
4. `dafu.spinxbi.com` and `jackpot-world.com` are the same title serving two different payment configs, and DAFU's channels have been flagged closed against a window that expired on 1 September.
5. Your GASH flow ships a dedicated error for *"Wrong GASH card region"* — which is a decline you are showing players because the voucher rail is region-locked and there is no second local option behind it.

**Cold call openers (conversational, one sentence each):**
1. "I was looking at how you've built payments across the Jackpot World stores — you've clearly run your own gateway for years, so I wanted to ask about something narrower: what happens when Airwallex has a bad day in one corridor?"
2. "You've got five or six web storefronts live now and two more staged — Cash Rally and Vegas Friends — and I noticed the newer ones didn't go onto your own gateway. Was that a deliberate call?"
3. "You've got GASH and MyCard both wired up for Taiwan and a Japanese storefront with a 特商法 filing behind it — so the intent to sell direct in those markets is obviously there. What's stopping konbini and the Taiwanese wallets going on?"

---

## Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors (social casino)

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| SciPlay (Light & Wonder) | sciplay.com | USA | $368M H1 2026 (segment) | US, global | **Own proprietary D2C platform** — in-house, no orchestrator named | [SEC 10-Q](https://www.sec.gov/Archives/edgar/data/0000750004/000075000426000033/lnw-20260630.htm) |
| Playtika | playtika.com | Israel | Not found | US, global | Not found | [SciPlay 10-K FY2022](https://www.sec.gov/Archives/edgar/data/1760717/000176071723000010/scpl-20221231.htm) |
| DoubleDown Interactive | doubledowninteractive.com | South Korea | ~$310M (FY24) ⚠️ TAL figure, unverified | US, Korea | Not found | `accounts/apac-tal.csv` |
| DoubleU Games | doubleugames.com | South Korea | Not found | US, Korea | Not found | [SciPlay 10-K FY2022](https://www.sec.gov/Archives/edgar/data/1760717/000176071723000010/scpl-20221231.htm) |
| Product Madness / Big Fish (Aristocrat) | productmadness.com | Australia / UK | Not found | Global | Not found | [SciPlay 10-K FY2022](https://www.sec.gov/Archives/edgar/data/1760717/000176071723000010/scpl-20221231.htm) |
| Playstudios | playstudios.com | USA | Not found | US, global | Not found | [SciPlay 10-K FY2022](https://www.sec.gov/Archives/edgar/data/1760717/000176071723000010/scpl-20221231.htm) |
| Huuuge Games | huuugegames.com | Poland | Not found | Global | Not found | [SciPlay 10-K FY2022](https://www.sec.gov/Archives/edgar/data/1760717/000176071723000010/scpl-20221231.htm) |
| GSN Games / Bash Gaming (Scopely) | gsngames.com | USA | Not found | US | Not found | [SciPlay 10-K FY2022](https://www.sec.gov/Archives/edgar/data/1760717/000176071723000010/scpl-20221231.htm) |

*The competitor set is drawn from SciPlay's own 10-K, which names: "Playtika, Playstudios, Product Madness/Big Fish Games (subsidiaries of Aristocrat), DoubleU Games/Double Down Interactive, GSN Games/Bash Gaming (subsidiaries of Scopely), AppLovin and Huuuge Games."* ⚠️ **Note the territory problem: social casino is a structurally US/Israel/Poland-centred vertical. Most of SpinX's direct competitors are out of APAC territory**, which is why 11B carries more prospecting weight than 11A on this account.

#### 11B. Industry Peers / Same Vertical (APAC virtual-goods publishers with own-channel billing)

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| **Asiasoft (PlayPark)** | playpark.com | Gaming | TH, SG, VN | **In-house PlayMall — self-built 7-currency wallet routing ~100 top-up channels.** The closest structural match to SpinX in the whole TAL: a self-built multi-channel wallet, routed in-house. Researched 2026-09-20, ICP 17/29 | `2-ready-to-outreach/asiasoft-playpark.md` |
| **Cygames** | cygames.co.jp | Gaming | JP + ~190 countries | **In-house: two PSPs joined by a single `country_code==='JP'` boolean, no failover or routing.** Near-identical pathology to SpinX's `if (t==="RU")`. Researched 2026-09-20, ICP 19/29 | `2-ready-to-outreach/cygames.md` |
| **Com2uS** | com2us.com | Gaming | KR + 15 storefront languages | Web shop opened 2026-06; **PortOne orchestrator incumbent**, Xsolla as global MoR, MyCard direct in APAC. Shows a Korean peer that bought orchestration. Researched 2026-09-20, ICP 21/29 | `2-ready-to-outreach/com2us.md` |
| **Netmarble** | netmarble.com | Gaming | KR + global, 78% overseas | **SpinX's own parent, and already on the TAL.** FY2025 revenue ₩2,835bn (~$1.91bn) | [sgimage.netmarble.com](https://sgimage.netmarble.com/images/netmarble/nmOfficial/20260205/8sto1770273390151.pdf); `accounts/apac-tal.csv` |
| **Gamania Digital Entertainment** | gamania.com | Gaming | TW | ⚠️ **Gamania owns GASH**, which is one of SpinX's rails. A gaming publisher on the TAL, but its payments arm is infrastructure — **check before pitching whether the relevant entity is the publisher or GASH, because GASH would route to Partnerships** | `accounts/apac-tal.csv` |
| **Boyaa** | boyaa.com | Gaming — card/board | HK/CN + SEA | ~$100M (FY24) ⚠️ TAL figure. HK-listed, same HK base and same Greater-China social-gaming category as SpinX | `accounts/apac-tal.csv` |
| **Efun** | efun.com | Gaming | TW, SEA | TAL note: *"heavy local payment method use"* — the inverse of SpinX, and a useful reference for what TW/SEA coverage looks like done properly | `accounts/apac-tal.csv` |
| **Century Games** | centurygames.com | Gaming | CN + global | TAL note: *"large overseas revenue via app stores and direct web shops"* — same dual-channel shape | `accounts/apac-tal.csv` |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| Com2uS | **PortOne** (regional orchestrator, inside the Hive billing platform) | Confirmed as of 2026-09-20 | Gaming — mobile | `2-ready-to-outreach/com2us.md` |
| SciPlay | **None — built its own** proprietary D2C platform, launched 2023 | 2023 onward | Social casino | [SEC 10-Q](https://www.sec.gov/Archives/edgar/data/0000750004/000075000426000033/lnw-20260630.htm) |

*No public case study found of a direct social-casino competitor adopting a third-party payment orchestrator.* The nearest evidence points the other way: SciPlay, the closest listed comparable, built its own. **Com2uS is a gaming peer in the territory that did buy orchestration, but it is not a social-casino competitor**, so it is honest competitive context rather than "your competitor did this." The ICP row scored **0**.

🔑 **The sourced benchmark worth carrying into the conversation.** SciPlay's SEC filings break out exactly the channel split Netmarble does not disclose:

| Period | Direct-to-consumer | Third-party platforms | Total | D2C share |
|---|---|---|---|---|
| H1 2025 | $63M | $339M | $402M | **15.7%** |
| H1 2026 | $103M | $265M | $368M | **28.0%** |
| Q2 2026 | $53M | $129M | $182M | **29.1%** |

Source: [Light & Wonder 10-Q, period ended 2026-06-30](https://www.sec.gov/Archives/edgar/data/0000750004/000075000426000033/lnw-20260630.htm) (percentages computed from the filed figures). Earlier filings put it at ~9% for H1 2024 and ~10% for 9M 2024 `[UNVERIFIED — search summary only, page not fetched]`, and the FY2025 annual report shows FY2024 D2C of $88M on $821M ≈ 10.7% `[UNVERIFIED — search summary only, page not fetched]`.

**Read: the closest listed social-casino comparable has taken its own-channel share from roughly 10% to 28% in two years, while its total revenue fell.** ⚠️ **This is SciPlay's number, not SpinX's. It must never be presented as SpinX's web share.** It is the best available evidence that the channel SpinX is building out is where this vertical's economics are going — and it is why three new storefronts in three weeks matters.

#### 11D. Prospect Scoring

Applied to **Asiasoft (PlayPark)** as the closest structural match, using only signals already verified in this repo:

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| Monthly transaction count | — | ⬜ Not re-derived here | `2-ready-to-outreach/asiasoft-playpark.md` |
| Orchestration status | +1 | ✅ In-house — PlayMall centralised 7-currency wallet | `accounts/apac-tal.csv` |
| 3+ countries | +3 | ✅ Thailand, Singapore, Vietnam | `accounts/apac-tal.csv` |
| Multiple PSPs | +3 | ✅ Fiuu (SG) + PayPal direct | `accounts/apac-tal.csv` |
| Local rail gap in top-3 market | ⬜ | Not re-verified in this run | — |
| **Recorded total** | **17/29 ⭐** | Scored 2026-09-20 | `2-ready-to-outreach/asiasoft-playpark.md` |

*Scores for Cygames (19/29), Com2uS (21/29) and Asiasoft (17/29) are carried from their own files, all scored against the /29 matrix on 2026-09-20 and therefore directly comparable to SpinX's 14/29.*

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Com2uS | Peer | KR + 15 languages | 21/29 | ⭐ | PortOne incumbent — displacement | ✅ |
| 2 | Cygames | Peer | JP + ~190 countries | 19/29 | ⭐ | One `country_code` boolean, no failover | ✅ |
| 3 | Asiasoft (PlayPark) | Peer | TH, SG, VN | 17/29 | ⭐ | Self-built 7-currency wallet, ~100 channels | ✅ |
| 4 | **SpinX Games** | **Target** | **HK, TW, JP, US** | **14/29** | **🟢** | **In-house router, no card failover** | **✅** |
| 5 | Netmarble | Parent / peer | KR + global | Not scored | — | ₩2,835bn FY2025, 78% overseas; owns SpinX | ✅ |
| 6 | Efun | Peer | TW, SEA | Not scored | — | *"heavy local payment method use"* | ✅ |
| 7 | Century Games | Peer | CN + global | Not scored | — | App stores **and** direct web shops | ✅ |
| 8 | Boyaa | Peer | HK/CN + SEA | Not scored | — | HK-listed, same category and base as SpinX | ✅ |
| 9 | DoubleDown Interactive | Competitor | US, KR | Not scored | — | Korean social casino, closest APAC-HQ competitor | ✅ |
| 10 | **Playtika** | **Competitor** | **Global** | **Not scored** | — | **Named in SciPlay's 10-K; Israel HQ** | ❌ **out of territory** |

**Genuine finds not on the TAL — and the honest verdict on each:** Playtika, SciPlay, DoubleU Games, Huuuge Games, Product Madness, Playstudios and Scopely are all absent from `accounts/apac-tal.csv`. **None of them is a territory addition**: all are HQ'd in the US, Israel, Poland or Australia with no APAC headquarters, so under CLAUDE.md's rule they are out of territory and correctly absent. **Social casino as a vertical is structurally EMEA/Americas.** The prospecting value from this account is therefore *not* in its competitors — it is in the **APAC virtual-goods publishers with self-built billing stacks** in 11B, where the TAL is already strong and where SpinX's pathology (in-house router, no failover, thin local rails) repeats almost exactly in Cygames and Asiasoft.

---

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | **~US$418M / yr [DERIVED — both inputs sourced]** ⚠️ **The TAL's "~$1B est." is REFUTED.** | **Input 1:** Netmarble quarterly revenue — 4Q25 ₩797.6bn and FY2025 ₩2,835bn from [Netmarble's own IR host](https://sgimage.netmarble.com/images/netmarble/nmOfficial/20260205/8sto1770273390151.pdf); 2Q26 ₩749.2bn and H1 2026 ₩1,400.9bn (so 1Q26 = ₩651.7bn) from [invenglobal.com](https://www.invenglobal.com/articles/24480/netmarble-reports-q2-revenue-of-7492-billion-and-operating-profit-of-801-billion). **Input 2:** three-SpinX-title share of group revenue — 4Q25 19% (JW 7 + LS 6 + CF 6, Netmarble's own deck, verbatim: *"Jackpot World 7%, Lotsa Slots 6%, Cash Frenzy 6%"*); 2Q26 21% ([pocketgamer.biz](https://www.pocketgamer.biz/netmarble-makes-5051m-in-q2-2026-with-the-seven-deadly-sins-success/)); 1Q26 24% `[UNVERIFIED — search summary only, page not fetched]`. **Arithmetic:** 4Q25 ₩797.6bn × 19% = ₩151.5bn; 1Q26 ₩651.7bn × 24% = ₩156.4bn; 2Q26 ₩749.2bn × 21% = ₩157.3bn → **₩620bn annualised ÷ 1,483 KRW/USD = US$418M.** FX rate implied by pocketgamer.biz's own ₩749.2bn → $505.1M conversion. **Cross-check:** SpinX's audited pre-acquisition 2020 revenue was ₩497bn / **$432M** ([pocketgamer.biz](https://www.pocketgamer.biz/netmarble-picks-up-social-casino-developer-spinx-games-for-219-billion)) — the derivation lands within 4% of a known anchor six years later. ⚠️ Excludes the four smaller titles (Jackpot Wins, Cash Club, Jackpot Crush, Cash Rally), which Netmarble does not break out, so this is a **floor** for SpinX total revenue. |
| GMV / Gross Transaction Volume | *No public GMV data found.* For a virtual-currency seller, revenue ≈ gross consumer spend, so the figure above is the better proxy | — |
| Average Transaction Value (USD) | **Not published.** The only sourced price points are Apple's IAP tiers for Jackpot World: **$0.99, $1.99, $2.99, $4.99, $5.99, $7.99, $9.99, $11.99, $14.99, $19.99** ([apps.apple.com](https://apps.apple.com/US/app/id1356980152)). ⚠️ **These are app-store tiers, not SpinX's own-channel prices**, and web storefronts in this category typically sell larger packages. SpinX's own `currencyList` is empty until login | — |
| Est. Annual Transactions | **~3.3M/yr on own channels [ASSUMPTION]** — see the row below; derived from the same assumed inputs, so it carries the same label | Calculated |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ~280,000/month. [ASSUMPTION — not researched.]** **Billing unit: virtual-currency top-up purchases settled on SpinX's own channels** — the web storefronts, the Windows EXE client, and the SpinX-controlled in-app payment flow. **App-store IAP purchases are Apple's and Google's transactions, not SpinX's, and are excluded from this count.** **Why it is an assumption and not a derivation:** the own-channel share of revenue is **not published** (Netmarble's decks break out region and genre only, and SpinX does not file separately), and the average own-channel top-up value is **not published**. Two unsourced inputs means the output is an assumption regardless of the arithmetic. **Basis:** US$418M/yr ÷ 12 = US$34.9M/month total × **20% assumed own-channel share** = US$6.98M ÷ **US$25 assumed average top-up** ≈ 279,000. The 20% sits between SciPlay's filed H1 2025 (15.7%) and H1 2026 (28.0%) D2C shares — **a peer's figure used to shape an assumption, never as SpinX's number.** **Sensitivity:** 10% share → 232k / 139k / **70k** at $15 / $25 / $50 ATV; 20% → 465k / 279k / 139k; 28% → 651k / 390k / 195k. Eight of nine corners land ≥100,000. **Scored the band the central assumption implies (+5), marked ⚠️, and this figure has not been used to reject the account and must never be.** | See the disclosure rule in the ICP matrix |
| Active Customers / Users | *No public DAU/MAU figure found.* ⚠️ **Deliberately not estimated, and no install or DAU number has been fed into the transaction count above** | — |
| Primary Currency | **USD**, with genuine multi-currency support — a dedicated `/payment/getLocalPrice` endpoint plus `currency`, `currency_exe`, `formatted_price` in state | [JW bundle](https://d13ac69ufeumng.cloudfront.net/live/assets/index-a6b23cbd.js) |
| Top 3 Markets by Revenue | **Not published for SpinX.** Netmarble group 4Q25: N.A. 39%, Korea 23%, Europe 12%, SEA 12%, Japan 7%, others 7% — ⚠️ **this is the parent group across all titles and must not be read as SpinX's split** | [sgimage.netmarble.com](https://sgimage.netmarble.com/images/netmarble/nmOfficial/20260205/8sto1770273390151.pdf) |
| **Billing channel split (web vs app store)** | 🛑 **NOT PUBLISHED, and this is the single most important gap in the business case.** Netmarble's 4Q25 deck was scanned for `App Store`, `Google`, `Apple`, `web shop`, `own channel`, `direct`, `D2C`, `in-app` and `third-party`: the four `App Store` hits are **chart footnotes crediting Apptopia for iOS ranking data on unrelated titles** (*"About: (iOS App Store version) … Apptopia"*), not a revenue-channel breakout. The deck breaks out revenue by **region and genre only.** SpinX does not file separately. The sole platform-cost signal is an **undifferentiated "Commission" line** — ₩252.3bn in 4Q25, 31.6% of revenue, down from 35.7% five quarters earlier, with the deck noting *"Commission-to-revenue ratio continues to decline"* — which mixes store commissions, external-IP royalties and payment fees and therefore **cannot be decomposed.** **The channel exists and is heavily built out — seven live storefronts, two staged, six processors, own gateway — but nothing public sizes it, and no part of this report should be read as implying a share.** | [sgimage.netmarble.com](https://sgimage.netmarble.com/images/netmarble/nmOfficial/20260205/8sto1770273390151.pdf) |
| High-risk vertical status | **Social casino, NOT sweepstakes.** SpinX's own App Store listing states *"Jackpot World Casino does not offer real money gambling games"* and *"'Coins' and 'Bonus' mentioned above are game currency, not real currency."* No real-money redemption → **materially lower acquirer risk than a sweepstakes operator.** No card-network action found. **Not a PSP:** `tpp.spinxbi.com` is SpinX's own in-house merchant payment page, not a product sold to third parties — **no Partnerships routing.** | [apps.apple.com](https://apps.apple.com/US/app/id1356980152) |
| Litigation relevant to payments | **$3.5M US class-action settlement, verified.** *William Heathcote v. SpinX Games Limited, et al.*, **Case No. 20-cv-01310-RSM, U.S. District Court for the Western District of Washington.** Defendants: **SpinX Games Limited, Grande Games Limited, Beijing Bole Technology Co., Ltd.** Games covered: Cash Frenzy, Lotsa Slots, Jackpot World, Vegas Friends, Jackpot Mania, Jackpot Fever, DAFU, Cash Bash, Jackpot Crush. Claims under Washington gambling law, the Washington CPA and unjust enrichment, over virtual-coin sales. Class: Washington residents who played before 2022-01-31. Final approval hearing 2022-11-10; claim deadline 2023-01-26; listed as closed. **"The defendants haven't admitted any wrongdoing."** ⚠️ **Relevant to a payments conversation only because Washington-style exposure is why operators geo-fence and why per-channel kill switches exist in code. It is NOT a gate failure, and nothing in this report implies wrongdoing.** A separate Kentucky settlement (~$285,500) is `[UNVERIFIED — search summary only, page not fetched]` and is **not used.** | [topclassactions.com](https://topclassactions.com/lawsuit-settlements/consumer-products/mobile-apps/spinx-games-grande-games-beijing-bole-technology-casino-apps-3-5m-class-action-settlement/) · [casino.org](https://www.casino.org/news/social-casino-games-platforms-agree-3-5m-class-action-settlement/) |

---

## Overall Research Confidence

**Medium-High** — unusually high on payment infrastructure, unusually low on market sizing, and the split is worth stating plainly because it determines what can and cannot be said in outreach.

**Strong coverage (first-hand, re-verified this run):**
- **Section 3 (PSP stack & orchestrator)** — the strongest section. Six production bundles fetched decompressed into a clean directory and scanned against 55 vendor and rail keywords, with every apparent hit context-checked and seven false positives logged. The live server-side `payment_config` was captured from four storefronts, so the routing claims rest on runtime configuration rather than shipped defaults. The CSP `frame-ancestors` header gave an authoritative storefront inventory.
- **Section 4 (local methods)** — every "Not found" is a zero-hit scan result across six bundles, which is a sourced absence.
- **Section 12 (revenue)** — derived from two sourced inputs, with the primary input moved onto **Netmarble's own IR host**, and the result cross-checked to within 4% of an independent 2020 anchor.
- **Section 8 (checkout)** — accessible to the limits of an unauthenticated session, and those limits are marked.

**Limited coverage, and why:**
- 🛑 **Section 1 (traffic) — effectively absent.** **Traffic data was SUPPLIED, not API-sourced or estimated — but it measures `spinxgames.com`, an 894-byte brochure shell with no shop, cart or checkout route.** No traffic data exists for any of the seven revenue-bearing domains. This is the report's central weakness: it **removes two ICP rows worth 5 points** (local-rail gap in a top-3 market; home market under 60% of traffic), it makes the Quick Look "Top 5 markets" table impossible to complete as designed, and it forces Sections 2 and 4 to be organised by *confirmed payment surface* instead of *traffic market* — a weaker basis, marked as such wherever used.
- ⚠️ **Section 5 (complaints) — weakly evidenced.** Trustpilot was retrievable only via WebFetch (plain `curl` returns 403 from bot protection), and **Google Play and App Store review bodies were not retrievable at all** — the source the method identifies as richest in APAC. The complaint picture rests on 31 reviews for a brochure domain, of which two are payment-specific. Treat "isolated" as provisional.
- ⚠️ **Section 2 (entities) — no registration numbers.** Four entities are named with sources but not one registration number was obtainable; no corporate registry was reachable.
- ⚠️ **Section 9 (PCI) — nothing published**, and the one determination that matters (Airwallex hosted iframes vs SpinX-served card fields, which decides SAQ A vs A-EP) needs an authenticated DevTools session.
- ⚠️ **The Japan 特商法 disclosure** is carried as a Phase 0 gate finding. The policy host is a document-by-id SPA whose text loads from an API, and I could not re-open the document in this environment.
- ⚠️ **Section 11A** is built almost entirely on one source, SciPlay's 10-K competitor list, because social casino is a structurally non-APAC vertical and APAC trade press carries little on it.

**Confidence was NOT downgraded for fetch access.** Both WebFetch and `curl` worked. Two environment traps were hit and cleared, and are logged for the next run: CloudFront serves Brotli, so `curl --compressed` is mandatory (a plain fetch stores compressed bytes and every vendor grep returns a false zero); and the gateway bundle is served with a **malformed `content-encoding: utf-8` header** that makes `curl --compressed` fail outright with *"Unrecognized content encoding type"* — it must be fetched with an explicit `Accept-Encoding` and decoded by inspection. `grep -P` is unavailable and fails silently; `LC_ALL=C grep` with byte patterns was used for CJK detection throughout. `pdftotext` is unavailable; the Netmarble deck was read by decompressing its FlateDecode streams in Python and pulling the text operands.

**No Agent/Task tool was available in this environment**, so Phase 2's Agents 2–5 could not be launched in parallel as the method specifies. All four workstreams — PSP stack and orchestrator, alternative and local payment methods, complaints/news/checkout, and competitors — were executed directly and sequentially instead, within the same evidence standard. The method's per-agent search and fetch budgets did not bind.

---

## Manual Research Recommendations

> **1. Area:** **Re-pull SimilarWeb on the storefront domains. This is the highest-value missing input on the account by a wide margin.**
> **Why it matters:** It is the one action that fixes four things at once. It would (a) give a real country profile for the domains that actually take money, (b) unlock the two ICP rows that currently score zero and plausibly move this account from **14/29 🟢 to 19/29 ⭐**, (c) let the Quick Look "Top 5 markets" table be completed as designed, and (d) **convert the monthly transaction count from ASSUMED to DERIVED**, which is the other top-priority gap below. Everything currently qualified with "no traffic data exists" in this report resolves on this one input.
> **Suggested manual action:** Pull Similarweb PRO for **`jackpot-world.com`** and **`lotsa-slots.com`** first — they are the two largest confirmed storefronts and the ones the correction notice already flags. Then add **`shop.cash-frenzy.com`**, **`jackpot-wins.com`**, **`cashclubcasino.com`**, **`prime.jackpot-crush.com`** and **`dafu.spinxbi.com`**, which this run discovered from the gateway's CSP header and which have never been measured. Sum visits per country across all seven and recalculate shares from the combined total — do **not** treat `jackpot-world.com` alone as the account. Request the full country list, not a top-10 cut.

> **2. Area:** **Confirm the monthly transaction count and the own-channel revenue share.**
> **Why it matters:** The transaction count is **ASSUMED**, and it is the only ICP signal that can reject an account on its own. It scored +5 on an assumption, correctly marked, but the business case cannot be built on it. The blocker is that two inputs are unpublished: the share of SpinX revenue settling on its own channels, and the average own-channel top-up value. **Netmarble does not disclose either, and SpinX does not file separately** — so this cannot be closed by desk research and must come from the merchant.
> **Suggested manual action:** Make both a discovery question, and use the sourced peer benchmark to earn the answer rather than asserting one: SciPlay's SEC filings show its own-channel share going from ~10% (FY2024) to **28% (H1 2026)** while total revenue fell. Ask what share of SpinX top-ups settle on their own rails today versus the stores, and what a typical web package is worth against the $0.99–$19.99 app-store tiers. **Never put SciPlay's percentage forward as SpinX's.**

> **3. Area:** **App Store and Google Play review bodies — the complaint source this run could not reach.**
> **Why it matters:** Section 5 rests on 31 Trustpilot reviews for a brochure domain, of which exactly two are payment-specific, and the "isolated frequency" call that zeroed the ICP row is weakly evidenced as a result. In this category store reviews are the richest source, and the distinction that matters commercially is narrow: **payment-mechanics failures (duplicate charges, declines, unrecognisable descriptors, coins paid for and not credited) are findings; "the slots are rigged" and "the app crashed" are not.**
> **Suggested manual action:** Read the review bodies for Jackpot World (`id1356980152`), Cash Frenzy (`id1404165333`) and Lotsa Slots on both stores, filtered to the last 12 months, and tally only payment-mechanics complaints. Pay particular attention to **statement-descriptor confusion** — the one Trustpilot instance (*"charges labeled as other, disputed with bank"*, 2025-05-16) is n=1 today, and SpinX bills under at least seven brand names through two architectures, which makes descriptor hygiene a plausible systemic issue worth confirming before it is raised on a call.

> **4. Area:** **Walk the live checkout per geography with a funded account.**
> **Why it matters:** Three things cannot be answered from source code and all three shape the pitch. **(a)** Appcharge advertises 500+ methods, but whether SpinX has *any* local APAC methods enabled is unknown — if Appcharge is already serving konbini in Japan, Insight #3 weakens materially. **(b)** Whether Appcharge is engaged as **merchant of record** or checkout-only changes who owns the payment relationship on five of the seven storefronts, and is **not established**. **(c)** Whether the Airwallex card fields are hosted iframes or SpinX-served DOM decides SAQ A vs SAQ A-EP and therefore which Yuno integration shape to propose.
> **Suggested manual action:** VPN into **Taiwan, Japan and Hong Kong** and open `shop.cash-frenzy.com` and `jackpot-world.com/en/shop/token` with DevTools recording. Capture the rendered method list per geography, the merchant-of-record name on the Appcharge checkout, the statement descriptor if a test purchase is possible, and whether the card inputs sit in a cross-origin iframe.

> **5. Area:** **Corporate registry confirmation and the Airwallex acquiring relationship.**
> **Why it matters:** Four entities are named without a single registration number, and the +3 "3+ countries" ICP row rests on entity count rather than traffic — so if the entity picture is wrong, the score is wrong. Separately, **Airwallex is the sole card processor with no failover** (Insight #1), and whether it is also the merchant of record, and which bank sits behind it, determines whether the Yuno conversation is "add a second acquirer" or "change who the merchant is."
> **Suggested manual action:** Search the **Hong Kong Companies Registry** for SpinX Games Limited and Grande Games Limited, and China's **NECIPS** for Beijing Bole Technology Co., Ltd. Resolve the Sheung Wan / Kowloon HQ conflict from the registry record rather than the App Store listing. Then ask SpinX directly whether Airwallex is MoR, which acquiring bank is behind it, and whether any second card acquirer exists that is simply not referenced in the client bundles.

---

## Appendix: All Source URLs

**SpinX first-party — storefronts and payment surface (all fetched 2026-10-09)**
- https://tpp.spinxbi.com/ — own payment gateway; CSP `frame-ancestors` header is the storefront inventory
- https://d13ac69ufeumng.cloudfront.net/payment/test/assets/index-4dee6280.js — gateway bundle (192,956 bytes)
- https://jackpot-world.com/en/shop/token — token store (78,737 bytes) + live `payment_config`
- https://jackpot-world.com/en/shop/gash — GASH/MyCard store (36,577 bytes)
- https://jackpot-world.com/ja/shop/token — Japanese store (70,642 bytes)
- https://www.jackpot-world.com/zh/shop/gash — zh-hant store
- https://www.jackpot-world.com/en/support/faq — footer entity, locales, Payment Terms link
- https://d13ac69ufeumng.cloudfront.net/live/assets/index-a6b23cbd.js — Jackpot World bundle (382,732 bytes)
- https://dafu.spinxbi.com/ — second Jackpot World front, divergent `payment_config`
- https://www.lotsa-slots.com/ and /web_store — Lotsa Slots store
- https://d13ac69ufeumng.cloudfront.net/LS/assets/index-0885118a.js — Lotsa Slots bundle (236,197 bytes)
- https://shop.cash-frenzy.com/ — **Cash Frenzy store, located this run**
- https://d1cse7lsiayene.cloudfront.net/cash-frenzy/production/_nuxt/DodO8R0c.js — Cash Frenzy bundle
- https://jackpot-wins.com/ + https://d1cse7lsiayene.cloudfront.net/jackpot-wins/production/_nuxt/CEvJ3zNO.js
- https://cashclubcasino.com/ + https://d1cse7lsiayene.cloudfront.net/cash-club/production/_nuxt/CBPiXZzs.js
- https://prime.jackpot-crush.com/ + https://d1cse7lsiayene.cloudfront.net/jackpot-crush/production/_nuxt/BBCgtCaA.js
- https://cash-rally.com/ — pre-launch, `payment_config: null`
- https://vf.spinxbi.com/ — pre-launch, Appcharge sandbox
- https://spinxgames-policy.com/jackpot-world/view — policy host (document-by-id SPA; text not retrievable)
- https://bolegames.helpshift.com/hc/en/14-jackpot-world/ — help centre, titled "SpinX Games Support"

**Netmarble (parent) financials**
- https://sgimage.netmarble.com/images/netmarble/nmOfficial/20260205/8sto1770273390151.pdf — **Netmarble's own IR host**, 4Q25/FY2025 deck
- https://www.invenglobal.com/articles/24480/netmarble-reports-q2-revenue-of-7492-billion-and-operating-profit-of-801-billion
- https://www.pocketgamer.biz/netmarble-makes-5051m-in-q2-2026-with-the-seven-deadly-sins-success/
- https://investgame.net/wp-content/uploads/2026/08/2026-08-05-netmarble_q2_2026_wp.pdf — third-party mirror (superseded)

**Ownership and corporate history**
- https://www.pocketgamer.biz/netmarble-picks-up-social-casino-developer-spinx-games-for-219-billion
- https://www.gamblinginsider.com/news/12749/netmarble-purchases-spinx-after-acquiring-leonardo-interactive-holdings
- https://www.yogonet.com/international/news/2021/08/02/58626-south-korean-game-developer-netmarble-acquires-social-casino-spinx
- https://mobilemarketingmagazine.com/netmarble-acquires-spinx-games-for-2-19bn/
- https://www.koreajoongangdaily.com/business/netmarble-agrees-to-buy-spinx-a-social-casino-game-company/10865090

**Entities, app listings, litigation**
- https://apps.apple.com/US/app/id1356980152 — Jackpot World; seller of record, IAP tiers, "not real money gambling"
- https://www.bluestacks.com/campaign/com.grandegames.slots.dafu.casino/tr/ — Grande Games package id
- https://topclassactions.com/lawsuit-settlements/consumer-products/mobile-apps/spinx-games-grande-games-beijing-bole-technology-casino-apps-3-5m-class-action-settlement/
- https://www.casino.org/news/social-casino-games-platforms-agree-3-5m-class-action-settlement/
- https://www.bonus.com/news/spinx-kentucky-class-action-lawsuit-settlement/ — Kentucky, `[UNVERIFIED]`, not used

**Complaints**
- https://www.trustpilot.com/review/spinxgames.com — 2.5/5, 31 reviews (WebFetch only; `curl` 403)

**Vendors and benchmarks**
- https://techcrunch.com/2024/11/25/appcharge-raises-26m-to-help-gaming-apps-cut-out-apple-and-google-from-virtual-goods-revenues
- https://appcharge.com — company marketing, not independently verified
- https://developers.appcharge.com/docs
- https://www.pocketgamer.biz/appcharge-launches-new-checkout-aimed-at-boosting-mobile-d2c-revenue
- https://news.bittopup.com/news/gash-card-taiwan-top-up-guide-spring-2026-promotions — ⚠️ competing GASH reseller
- https://www.airwallex.com/newsroom/airwallex-receives-regulatory-approval-and-completes-acquisition-of-unicard — HK SVF licence (not acquiring)
- https://www.sec.gov/Archives/edgar/data/0000750004/000075000426000033/lnw-20260630.htm — SciPlay D2C split
- https://www.sec.gov/Archives/edgar/data/1760717/000176071723000010/scpl-20221231.htm — SciPlay competitor list

**Internal**
- `accounts/apac-tal.csv` · `accounts/traffic/spinx-games.md` · `1-to-outreach/spinx-games.md`
- `2-ready-to-outreach/asiasoft-playpark.md` · `cygames.md` · `com2us.md` · `not-icp/devsisters-cookie-run.md`
- `.claude/reference/apac-payments.md` · `.claude/reference/subscription-payments.md`

</details>
