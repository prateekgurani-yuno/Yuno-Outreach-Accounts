# Neocraft

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 10 / 29 → 🟢 Medium
**Industry:** Gaming — mobile free-to-play MMORPG developer & publisher · **HQ:** Wanchai, Hong Kong · **Researched:** 2026-10-09 · **First email sent:** —
**Motion:** In-house

---

> ## 🔀 IDENTITY VERDICT — one company, and the second TAL row is a dead domain
>
> **`Neocraft` and `Neocraft Studio` are the same company.** The company itself uses both names interchangeably — the page title served at `neocraftstudio.com/en/news.html` is literally `NEOCRAFT - Official Website Homepage| - NEOCRAFT, NEOCRAFT STUDIO`.
>
> | | `neocraftstudio.com` | `neocraft.net` |
> |---|---|---|
> | HTTPS | **200 OK**, 301 → `www.`, Alibaba Cloud WAF (`acw_tc` cookie), EMA CMS (`EMASITEID`) | **Connection reset.** HTTP → **503** `upstream connect error or disconnect/reset before headers` |
> | Domain created | **2018-09-12** (matches "Born in 2018" on the About page) | **2025-09-24** — a re-registration, not a 2018-era asset |
> | Nameservers | AWS Route 53 (4 NS) | **`NS1-DOMAIN-EXPIRED.MYHOSTADMIN.NET`** / `NS2-DOMAIN-EXPIRED...` |
> | Registrar | GoDaddy, all four `client *** prohibited` locks set | Xiamen 35.com Information Co., Ltd. |
>
> **`neocraft.net` serves nothing, sits on literal domain-expired parking nameservers, and has no traffic of its own.** Prateek's traffic sheet was right to pull once. The `Neocraft Studio` row's website field is wrong and the row is a duplicate. Sources: [RDAP .net](https://rdap.verisign.com/net/v1/domain/neocraft.net) · [RDAP .com](https://rdap.verisign.com/com/v1/domain/neocraftstudio.com).
>
> ⚠️ **The name collides three ways.** `neocraft.com` is an **Israeli furniture label** — and the [CB Insights "Neocraft" profile](https://www.cbinsights.com/company/neocraft) is that furniture company ("based in Israel", "furniture label"), **not** the game publisher. A WebSearch summary asserted that this page describes a Hong Kong game publisher with a Mong Kok / Nathan Road HQ. **It does not.** Claim dropped; the only sourced address is the Wanchai one below.

---

> ## 🛑 THE APP-STORE VERDICT — the web store exists, and the bypass *is* the product
>
> **A web top-up store exists, is live, is sophisticated, and is actively incentivised.** The app-store trap in `.claude/reference/subscription-payments.md` §4 **does not fire in its disqualifying form.** Three independent pieces of the merchant's own estate:
>
> **1. Two live web checkouts** — `accounts.neocraftstudio.com/pay/index` (NEO Coins wallet top-up) and `accounts.neocraftstudio.com/payment/default` (direct per-character game recharge). Both reachable without login; both render a country selector and a per-country payment-method wall.
>
> **2. NEO Coins is an explicit App Store / Google Play bypass, in the merchant's own words.** From the [FAQ](https://www.neocraftstudio.com/en/faq-list), verbatim:
> > *"NEO Coins can **only** be acquired through the "Recharge" function on the official NEOCRAFT website."*
> > *"NEO Coins are applicable to all games released by NEOCRAFT. Currently, they are supported in games launched on **App Store and Google Play after January 1, 2024**. When a player's account has a sufficient NEO Coins balance… the system will prompt whether to use NEO Coins for deduction."*
>
> Top up on the **web**, where Neocraft is merchant of record on cards and ~97 local rails; spend **inside the store-distributed app**. That is the whole architecture.
>
> **3. The pull incentives are stacked and public.** Homepage tile: *"Recharge Discounts — **Enjoy Up to 10% Off Discount Now!**"* FAQ: *"Enjoy an additional n% in-game currency rebate when using NEO Coins"*, *"Single recharge supports a maximum of **USD $1,000**"*, *"Periodic promotions with **tax reductions**"*, plus a 1:100 bonus-points accrual.
>
> **Who processes it: NOT ESTABLISHED.** No PSP, acquirer, aggregator or orchestrator is named anywhere I could reach — not in the terms, not in the privacy policy, not in the page source, not in any CSP header, not in any search result. The payment submit (`POST /payment/default/deal-with-v3`) is server-side and login-gated; it returns `{"code":103,"msg":"Missing parameters"}` to an anonymous probe and reveals no downstream host. **I will not name a guess.** The method *labels* are generic channel names — "Card Payments", "Credit Cards Korea", "Bank Transfer Korea", "Cash at Retail Philippines", "Financial Process Exchange" — which reads like an aggregator-fed catalogue rather than branded PSP tiles `[INFERENCE, not confirmed]`.
>
> 🚫 **Coda Payments / Codashop is REFUTED, not merely absent.** Neocraft publishes an [**Unauthorized 3rd-party Top-up Penalty Policy**](https://www.neocraftstudio.com/announcement?language=en): *"some players have been blocked due to invalid recharges made through unauthorized platforms… we strictly prohibit such behaviors. We maintain a zero-tolerance policy… Our operations team is actively monitoring and detecting unauthorized platforms."* They are banning players for using third-party top-up channels, not routing through them.
>
> **Web-vs-IAP revenue split: no public source states it.** Apple, Google Play *and* **Huawei AppGallery** all carry the titles. Mobile F2P default is IAP-heavy, so the untouchable share is probably still the majority `[INFERENCE, not confirmed]`. The addressable channel is real but its size is unmeasured — see the volume gate below.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** NEOCRAFT Limited is a Hong Kong free-to-play mobile MMORPG developer and publisher, founded 2018, ~100+ staff from 7 countries ([About](https://www.neocraftstudio.com/en/about)). Eight live titles — Tales of Wind: Radiant Rebirth, Tree of Savior: NEO, Chronicle of Infinity, Guardians of Cloudia, Immortal Awakening, The Dragon Odyssey, Spirits of Aetheria and the Koei Tecmo-licensed Dynasty Warriors: Overlords XL — distributed through Apple, Google Play and Huawei AppGallery, with a **self-built web recharge store and NEO Coins wallet** used to pull purchases off the app-store rails.

**SimilarWeb total visits (last full month):** **153,134** for Sep 2026, ▲ **26.29% MoM** (desktop 26.92% / mobile web 73.08%) — *SimilarWeb (supplied 2026-10-09)*. Single domain pulled; `neocraft.net` has no traffic because it is a dead domain.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇰🇷 Republic of Korea | **14.91%** (~22,832) | Visa, Mastercard, **Credit Cards Korea**, Amex, Discover, Diners, UnionPay, JCB · **Kakao Pay, Toss Pay, Naver Pay, Payco, Samsung Pay**, Apple/Google Pay, PayPal, WeChat Pay, AliPay · **Culture Voucher, Eggmoney, Teencash, Cashbee, Book Gift Voucher, Happy Voucher**, MINT · **Bank Transfer Korea** | **None found.** The dominant Korean rails are all present | ❌ No Korean entity found — but domestic Korean rails *are* reachable in the live checkout, so a regulatory gate is **not** demonstrated |
| 2 | 🇷🇺 Russia | 10.43% (~15,972) | MIR, Visa, Mastercard, JCB · Sberbank, SBP, TinkoffBank | n/a — **out of territory** | ❌ — out of territory |
| 3 | 🇹🇷 Turkey | 8.75% (~13,399) | Cards, Google/Apple Pay, PayPal, WeChat Pay, AliPay, MINT | n/a — **EMEA, out of territory** | ❌ — out of territory |
| 4 | 🇺🇸 United States | 6.31% (~9,663) | Cards, PayPal, Apple/Google Pay, WeChat Pay, AliPay · **Dollar General, CVS Pharmacy**, MINT | n/a | ❌ |
| 5 | 🇧🇬 Bulgaria | 5.49% (~8,407) | Cards, PayPal, Apple/Google Pay, MINT | n/a | ❌ |

*(6–10: Saudi Arabia 5.43% — EMEA, out of territory · Brazil 4.97% · UK 4.59% · Spain 3.87% · 🇦🇺 Australia 2.46%, which has PayID but no PayTo, BPAY, Afterpay or Zip.)*

⚠️ **APAC visible total is 17.37% across just two of the top ten, despite the Hong Kong HQ.** Hong Kong itself does not appear in the top 10 at all. This is an APAC-domiciled publisher whose web audience is overwhelmingly **not** in APAC — Russia + Turkey + US + Bulgaria + Saudi + Brazil + UK + Spain = 50.39% of visits sit outside the territory. Say this plainly on any internal review: the account is in Prateek's territory because of where the company sits, not where its players are.

### Legal entities
- **NEOCRAFT Limited** / **NEOCRAFT LIMITED** (Hong Kong) — *FLAT/RM 1502, EASEY COMMERCIAL BUILDING, 253-261 HENNESSY ROAD, WANCHAI, HONG KONG*. Registration number **not found** (HK Companies Registry ICRIS not reachable in this environment; OpenCorporates requires an API token). Source: [Contact page](https://www.neocraftstudio.com/en/contact), corroborated by Apple App Store `sellerName: NEOCRAFT LIMITED`.
- **No second entity found in any market** — not Korea, not Japan, not Singapore, not mainland China.
- ⚠️ **Unresolved group affiliation.** The Google Play package IDs are **`com.emagroups.*`** (`com.emagroups.tow`, `.zs`, `.ic2`, `.lod2`, `.tdo`, `.cs`, `.bx`, `.sg`, `.wl`, `.tools`), the recharge page loads CSS/JS from **`static.emagames.cn`**, links `campus.emagames.cn` and `business.facebook.com/EMAGames/`, and the site sets `EMASITEID` / `EMACMSLANG` cookies. An "EMA" group relationship is strongly implied, but **I found no source that states what EMA Games/EMA Groups is or how it relates to NEOCRAFT Limited.** Do not assert a parent company. `[INFERENCE, not confirmed]`

### Known PSPs
- **None. Not established.** No PSP, acquirer, aggregator or payment orchestrator could be named with evidence. "No hits found" is a weak negative, not proof of absence — see Section 3A for exactly what was checked and what it would take to settle it.

### Orchestration status
**In-house orchestration layer** — the merchant built its own checkout, channel catalogue and stored-value wallet. Evidence: a merchant-owned method API (`POST /payment/default/get-manner-list`, keyed on ISO country code, returning `mannerList` / `mannerHistoryList` / `recommendList` / `setMannerList`), a merchant-owned per-method fee table surfaced in checkout as **"Channel service fee"**, a merchant-owned VAT/tax engine (`get-tax-fee-info` returning `vat` / `fee` / `vatFree` / `payNote`), merchant-owned order states (*Incomplete, Complete, Canceled, Re-issued, Subscription, Refunded*) and the **NEO Coins** wallet. **Whether any multi-acquirer routing or failover exists beneath that layer is NOT established.** Scored conservatively at +1 on the Webzen precedent in this repo (self-built wallet over an undetermined provider set).

### Buying signals
- 🚀 **Two global title launches inside 12 months** — Spirits of Aetheria **2026-05-21** and the Koei Tecmo-licensed **Dynasty Warriors: Overlords 2026-07-30**, the latter shipping with **Indonesian, Malay, Vietnamese, Thai and Korean** localisation it did not previously carry ([Apple metadata](https://itunes.apple.com/lookup?id=6757413794&country=us) · [ixbt.games, 31 Jul 2026](https://ixbt.games/en/news/2026/07/31/425853-klassika-musou-v-karmane-na-ios-i-android-sostoialsia-vnezapnyi-reliz-dynasty-warriors-overlords.html)).
- 📈 **The only account in its batch growing on its consumer domain** — ▲26.29% MoM, Korea #1 at 14.91%. `[INFERENCE, not confirmed]` the Dynasty Warriors launch (30 Jul, Korean-localised as 진삼국무쌍-오버로드) is the most plausible driver.
- 💼 **A named payments owner is published on the Contact page** — *"Business Inquiries: (for **localization and payment service**) — Yihan Lai, yihan@neocraftstudio.com"*. Payments is an owned, externally-facing function with a named human. **This is the single best entry point on the account.**
- 🤝 **Huawei AppGallery partnership + Gamescom 2025** — Tree of Savior: NEO won *Best Trending AppGallery Game* at the 2025 Mobile Gamer Awards and was demoed at HUAWEI AppGallery's Hall 9 booth in Cologne ([PR Newswire, 22 Aug 2025](https://www.prnewswire.com/il/news-releases/huawei-appgallery-invites-you-to-dive-into-award-winning-tree-of-savior-neo--live-demos--exclusive-events-await-at-gamescom-2025-302536691.html)). A **third** app-store rail, also unroutable.
- 📋 **No public payment RFP found.**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach neocraft` to draft the 12-touch sequence, or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 10 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **0** | ⚠️ **NOT FOUND — ASSUMED ~5,000–12,000 web recharge orders/month.** `[ASSUMPTION — not researched.]` **Per the disclosure rule, an assumed figure must never trigger the under-40,000 rejection, and it has not.** Basis and arithmetic in Section 12. **Billing unit: paid orders on `accounts.neocraftstudio.com` — NEO Coins top-ups and direct game recharges, where NEOCRAFT Limited is merchant of record. App Store, Google Play and Huawei AppGallery IAP is excluded entirely: those are Apple's, Google's and Huawei's transactions, not Neocraft's, and no orchestrator can touch them.** 0 points because the figure is uncertain, not because it is low. |
| Orchestration status | **+1** | ✅ **In-house layer.** Merchant-built checkout, country-keyed channel catalogue API, own "Channel service fee" table, own VAT engine, own NEO Coins wallet. Underlying acquirers not established. Scored +1, not +4 — this is not greenfield. |
| 3+ countries | **+3** | ✅ All ten top-traffic countries exceed 1% share — SimilarWeb (supplied 2026-10-09). *Note: this fires on traffic only; only **one** legal entity was confirmed.* |
| Multiple PSPs | **0** | ⬜ **Uncertain — zero PSPs named with evidence.** 97 distinct payment channels are confirmed live in the merchant's own API, but not one PSP, acquirer or aggregator behind them could be sourced. A deliberate zero. |
| Local rail or licensing gap in a top-3 market | **0** | ❌ **Not met, and verified not met.** Top-3 by traffic are Korea (14.91%), Russia (10.43%) and Turkey (8.75%). Russia and Turkey are out of territory. **Korea's checkout carries Kakao Pay, Toss Pay, Naver Pay, Payco, Samsung Pay, Credit Cards Korea, Bank Transfer Korea and six Korean cash vouchers** — pulled live from `get-manner-list?code=KR`. There is no Korean rail gap. On the licensing-gate limb: no Korean entity was found, but the presence of working domestic Korean rails is direct evidence *against* a gate, and I have **no primary source** for a Korean local-presence acquiring requirement, so I will not claim one. Real gaps exist in **Japan, India and Taiwan** (Section 4) — none is a top-3 traffic market. |
| Recent expansion | **+2** | ✅ Spirits of Aetheria 2026-05-21; Dynasty Warriors: Overlords 2026-07-30 with five new language localisations (ID/MS/VI/TH/KO). Apple metadata + ixbt.games. |
| Payment issues | **0** | ❌ **Not met — and this is a considered zero.** ~300 App Store reviews across nine apps in two storefronts (US, KR) were pulled and keyword-filtered. Every payment-adjacent review is a **monetisation / pay-to-win / app-bug** complaint, not a payments-rail complaint. Zero declines, zero duplicate charges, zero failed-renewal reports, zero web-recharge failures. See Section 5 for the distinction. |
| Funding >$10M | **0** | ❌ No funding round, investor or raise found. Private company; the About page describes a founder-led team. |
| High traffic outside home | **+2** | ✅ Hong Kong does not appear in the top 10 at all. Largest single market is Korea at 14.91% — home country far below 60%. |
| Competitor using orchestration | **+2** | ✅ **Com2uS — PortOne regional orchestrator incumbent** inside the Hive billing platform, with Xsolla as global MoR; verified in this repo at `2-ready-to-outreach/com2us.md` against Com2uS's own newsroom (「Hive 빌링의 PG 결제는 검증된 솔루션인 **포트원**과 **Xsolla** 페이먼트를 지원한다」). Also `Zupee → Juspay` in `accounts/apac-tal.csv`. |
| Payment job postings | **0** | ⬜ No payment-related job posting found on any board. *Not scored, but noted:* a named payment-service business contact is published on the Contact page, which is a stronger ownership signal than a req would be — it is simply not a job posting. |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **🟢 Medium (10 / 29)**

**No public payment RFP was confirmed, so no RFP override applies.**

#### Analyst override — considered, and deliberately NOT applied

Two override limbs were tested:

1. **App-store dominated revenue.** The usual disqualifier. **It does not fire.** A web store exists, it is the merchant's own, it spans ~97 channels across 40+ countries, it is discounted up to 10% to pull players onto it, and NEO Coins is documented by the merchant as spendable *inside* App Store and Google Play titles. Growing web-checkout share to escape store fees is exactly the qualifier `subscription-payments.md` §4 names. This is the opposite of the Devsisters case in `not-icp/` — Devsisters stated in writing that it does not process purchases at all; Neocraft has built an entire parallel billing stack to make sure it does.
2. **Absolute volume too small.** This is the live risk, and it is real: 153k monthly visits on a domain whose only commerce function is recharge almost certainly implies a web order count below the 40,000/month floor. **But the figure is assumed, not sourced — and rule 1 of the disclosure regime says an assumption never rejects an account.** Downgrading the tier on a number nobody sourced would be the exact error that regime exists to prevent. **No override. Tier stands at 🟢 Medium.**

> **Read the tier honestly.** 10/29 is the floor of Medium, and it is carried by *architecture* (a real merchant-of-record web channel with a named payments owner), not by *verified volume*. **"Confirm the monthly web recharge order count" is the first question on the first call.** If it comes back under 40,000 with a number behind it, this account moves to `not-icp/` on the volume gate and the report above is the reason why.

### Source Notes
- ✅ **One company, not two** — `neocraft.net` serves 503 on domain-expired nameservers, created 2025-09-24; `neocraftstudio.com` created 2018-09-12 on AWS DNS with registrar locks. RDAP, both.
- ✅ **Entity name and registered address** — NEOCRAFT Limited, FLAT/RM 1502, Easey Commercial Building, 253-261 Hennessy Road, Wanchai, Hong Kong. Company's own Contact page + Apple `sellerName`.
- ✅ **Web store exists and is the app-store bypass** — merchant's own FAQ, verbatim.
- ✅ **97 distinct live payment channels**, country-keyed — pulled directly from the merchant's own `get-manner-list` API across 43 country codes.
- ✅ **"Channel service fee" is a player-facing surcharge** — from the merchant's own checkout JS: `var money = amount + tax + fee;` rendered as `<h4>Channel service fee：</h4>`.
- ✅ **Native card fields on the merchant's own page** — `<input id="cardName">`, `#expiryDate`, `#CVC`, `#nameOnCard`, no iframe.
- ✅ **Koei Tecmo licence + 2026-07-30 launch** — ixbt.games.
- ⚠️ **PSP / acquirer / orchestrator: not established.** The most important gap in this report.
- ⚠️ **Web-vs-IAP revenue split: no public source.** The second most important gap.
- ⚠️ **HK company registration number: not found.** Registry unreachable here.
- ⚠️ **"EMA Groups / EMA Games" affiliation: implied by package IDs, CDN and cookies; unexplained by any source.** Do not assert a parent.
- ❌ **Two WebSearch summary claims were checked and found false** — (a) that CB Insights profiles Neocraft as a Hong Kong game publisher in Mong Kok (the page is an **Israeli furniture company**); (b) that VNG Games publishes Neocraft's *Dynasty Warriors: Overlords* in SEA (the VNG title is a **different 2022 game** by **SuperNova Overseas Limited**). Both dropped. This is the documented WebSearch-summary failure mode, twice in one run.
- ❌ **Sensor Tower per-country weekly revenue blog pages were found and deliberately not used** — they are per-country, per-quarter SEO pages credited to *"Timothy, Your Friendly Neighborhood AI"*. Not a usable revenue source.

### Success Case Alternatives
- **NetEase Games** — nameable on Yuno's own customer list. Closest match on profile: a large Asia-HQ'd game publisher running global player monetisation across many markets and rails. **No published metric exists for this relationship — never attach a number to it.**
- **Garena (Sea Limited)** — nameable on Yuno's own customer list. Match on profile: SEA-centred F2P publisher with heavy local-rail and web/direct top-up dependence. **No published metric exists for this relationship — never attach a number to it.**
- *Best fit for this specific account:* **NetEase Games** — the shared shape is an Asian publisher whose paying players are mostly *not* in its home market, which is precisely Neocraft's 17.37%-APAC profile.

---

## Executive Summary

NEOCRAFT Limited is a Hong Kong free-to-play mobile MMORPG developer and publisher (founded 2018, 100+ staff, eight live titles, ~93 million cumulative self-reported users) distributing through Apple, Google Play and Huawei AppGallery. **The decisive finding is positive: Neocraft has built a full merchant-of-record web billing stack — a NEO Coins stored-value wallet plus a direct per-character game recharge store — carrying 97 distinct payment channels keyed to the player's country, with its own fee table, its own VAT engine and a documented in-app redemption path for store-distributed titles.** It discounts web top-ups by up to 10% to pull players off Apple and Google, and publishes a zero-tolerance policy banning players who use third-party top-up platforms. The orchestration motion is therefore **in-house**: the merchant has already built the presentation, wallet and fee layer, and the open question is what sits underneath it — **no PSP, acquirer, aggregator or orchestrator could be identified from any reachable source.** The commercial hook is not rail coverage, which is unusually complete, but the **per-method "Channel service fee" the merchant surfaces to its own players in its own checkout** — 4.50% on Visa in Korea against 3.50% on the domestic Korean card rail and 0.00% on Kakao Pay, 18.00% on TrueMoney in Thailand, 13.75% on GoPay in Indonesia. That table is cost of acceptance, published, priced into conversion. The blocking risk is volume: 153k monthly visits on the only transacting domain.

---

## Section 1: Website Traffic Analysis by Country

**Data source:** **Path 1 — pasted SimilarWeb data supplied by Prateek.** `accounts/traffic/neocraft.md`, transcribed from *HK October Target Accounts — Similarweb Traffic* (Similarweb PRO, Worldwide, All traffic), period **Sep 2026**, captured 2026-10-09 05:15 IST. Cited throughout as **SimilarWeb (supplied 2026-10-09)**. Not re-researched. **This is a top-10 cut, not the full country list**, so the APAC total below is a *visible* floor.

**Domains resolved:** `neocraftstudio.com` (301 → `www.neocraftstudio.com`, HTTP 200). `neocraft.net` resolves in DNS but serves **503 / connection reset** on domain-expired nameservers — **not a separate property, and no traffic may be attributed to it.** No regional ccTLD variants found; the site uses path-based locales (`/en/`, `/cn/`, `/es/`, `/pt/`, `/de/`, `/fr/`, `/ru/`) and per-title subdomains (`tow.`, `tos.`, `coi.`, `goc.`, `ia.`, `tdo.`, `soa.`, `dwo.`), all on the one domain.

**Total visits:** 153,134 · **MoM:** ▲ 26.29% · Desktop 26.92% / Mobile web 73.08%

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | 🇰🇷 Republic of Korea | **14.91%** — **high priority** | ~22,832 | Domain ▲26.29% MoM; per-country trend not supplied | SimilarWeb (supplied 2026-10-09) |
| 2 | 🇷🇺 Russia | **10.43%** — high priority, **out of territory** | ~15,972 | " | " |
| 3 | 🇹🇷 Turkey | **8.75%** — high priority, **EMEA** | ~13,399 | " | " |
| 4 | 🇺🇸 United States | **6.31%** — high priority | ~9,663 | " | " |
| 5 | 🇧🇬 Bulgaria | **5.49%** — high priority | ~8,407 | " | " |
| 6 | 🇸🇦 Saudi Arabia | **5.43%** — high priority, **EMEA** | ~8,315 | " | " |
| 7 | 🇧🇷 Brazil | 4.97% | ~7,611 | " | " |
| 8 | 🇬🇧 United Kingdom | 4.59% | ~7,029 | " | " |
| 9 | 🇪🇸 Spain | 3.87% | ~5,926 | " | " |
| 10 | 🇦🇺 Australia | **2.46%** | ~3,767 | " | " |
| — | *Other / not in top-10 cut* | 32.79% | ~50,213 | Includes Japan, Hong Kong, Taiwan and SEA — **none of which appears in the top 10** | — |

**APAC visible total: 17.37%** across 2 of 10 (Korea, Australia). **50.39% of visits are in markets outside the APAC territory** (Russia, Turkey, US, Bulgaria, Saudi, Brazil, UK, Spain). Hong Kong — the HQ — is absent from the top 10 entirely.

⚠️ **Flag: every one of the top 10 countries has NO confirmed local entity.** Only one entity exists anywhere (Hong Kong). Cross-reference in Section 2.

⚠️ **The diaspora-pattern caution in `apac-payments.md` §3 inverts here.** This is not an APAC business billing a Western diaspora — it is an APAC-domiciled publisher whose paying audience is predominantly Korean, Russian, Turkish, American and European. Every corridor is outbound cross-border from a Hong Kong base.

---

## Section 2: Legal Entities & Local Presence

**Headquarters:** Wanchai, Hong Kong. Founded **2018** ("Born in 2018" — [About](https://www.neocraftstudio.com/en/about); corroborated by `neocraftstudio.com` domain creation 2018-09-12 per RDAP). ~100+ employees from 7 countries, self-reported.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Hong Kong | **NEOCRAFT Limited** (also rendered **NEOCRAFT LIMITED**, **NEOCRAFT GAMES**) — *FLAT/RM 1502, Easey Commercial Building, 253-261 Hennessy Road, Wanchai, Hong Kong* | **Not found** | [Contact page](https://www.neocraftstudio.com/en/contact) · [Privacy Policy](https://www.neocraftstudio.com/en/privacy) ("*'NEOCRAFT LIMITED'… refer to NEOCRAFT LIMITED and all of its subsidiaries*") · [Terms](https://www.neocraftstudio.com/en/terms) (53 occurrences of "Neocraft Limited" as the contracting party) · [Apple developer page](https://apps.apple.com/us/developer/neocraft-limited/id1367784951), `sellerName: NEOCRAFT LIMITED` |
| Korea / Japan / Singapore / Taiwan / mainland China / Australia | **No entity found** | N/A | — |

> **MANUAL:** The HK Companies Registry (ICRIS, `icris.cr.gov.hk`) was not reachable from this environment and OpenCorporates returned `401 Invalid Api Token`. The CR number, incorporation date, directors and share capital are all obtainable there in one lookup for a small fee. Worth doing before a call — it would also settle the EMA question if EMA appears as a shareholder.

**The subsidiaries question.** The privacy policy asserts that NEOCRAFT LIMITED has subsidiaries ("*and all of its subsidiaries*") but **names none**. No subsidiary was found in any market. Treat "one entity" as the sourced position and the subsidiary claim as unresolved.

**The EMA signal, stated as what it is.** Not a conclusion — a cluster of artefacts:
- Google Play package namespace: **`com.emagroups.*`** (10 packages) — [dev page](https://play.google.com/store/apps/dev?id=5566381355836435401)
- Recharge page assets served from **`static.emagames.cn`** (bootstrap, jQuery, md5, select2, header/footer JS and CSS)
- Links to **`campus.emagames.cn`** and **`business.facebook.com/EMAGames/`**
- Cookies **`EMASITEID=13`** and **`EMACMSLANG=en`** set on `.neocraftstudio.com`
- Favicon served from `static.emagames.cn/static/common/images/logo/favicon.ico`

`[INFERENCE, not confirmed]` Neocraft runs on a shared "EMA" group platform, plausibly a mainland-China-based development/publishing group with Neocraft Limited as the Hong Kong overseas-publishing arm. **No source states this.** A search for "EMA Games"/"emagames" returned nothing describing the company or any relationship to Neocraft. Do not put this in an email.

**Cross-Border Gap Analysis**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| Republic of Korea | ✅ #1, 14.91% | ❌ No | **Not demonstrated.** `apac-payments.md` flags Korea as likely gated, but that file is a checklist, not a source, and **I found no primary source.** Counter-evidence: the live checkout serves Credit Cards Korea, Bank Transfer Korea, Kakao/Toss/Naver/Payco — so domestic rails *are* being reached, presumably through a licensed local partner | ⚠️ **Yes on cards.** A Korean issuer seeing a Hong Kong-acquired card transaction is the classic foreign-acquired decline case. The checkout prices this in: Visa carries a **4.50%** channel service fee in Korea vs **3.50%** on the domestic card rail |
| Russia | ✅ #2, 10.43% | ❌ No | n/a — out of territory | ⚠️ Sanctions and settlement complexity; MIR + Sberbank + SBP + Tinkoff are live in the checkout, which implies a local channel partner. Out of Prateek's territory |
| Turkey | ✅ #3, 8.75% | ❌ No | n/a — EMEA | ⚠️ Yes. Route to EMEA |
| United States | ✅ #4, 6.31% | ❌ No | No | ⚠️ Yes — Visa/Mastercard both carry a **4.50%** channel service fee in the US, the joint-highest card fee in the whole catalogue |
| Bulgaria / Saudi / Brazil / UK / Spain | ✅ #5–9 | ❌ No | No | ⚠️ Yes (Saudi → EMEA) |
| Australia | ✅ #10, 2.46% | ❌ No | No | ⚠️ Yes |
| Japan | ❌ not in top-10 cut | ❌ No | Verify current EC 3DS requirements before citing — **no source obtained** | ⚠️ Yes, and materially: Neocraft runs **dedicated Japanese App Store listings** (クロニクル・オブ・インフィニティ id 6450688247, 1,564 JP ratings; 不滅の覚醒 id 6458103025) and both Japanese titles are selectable in the web recharge store — on a Japan method set with **no konbini, no PayPay, no LINE Pay, no Paidy and no carrier billing** |

> *"**Warning: potential cross-border operation in the Republic of Korea, Russia, Turkey, the United States and Bulgaria** — Neocraft's top five traffic markets, together 45.89% of visits. No local entity was found in any of them. Transactions are likely processed cross-border from a Hong Kong base, with higher scheme costs, lower approval rates and FX exposure."*

> **On the regulatory-gate language: I am deliberately not using it.** `apac-payments.md` says Korea "effectively requires local presence or a licensed local partner for domestic acquiring" and tells me to verify. I could not find a current primary source, and the live Korean checkout is evidence that domestic rails are already being reached. Claiming a gate here would be citing a regulatory rule from a checklist — the exact thing the integrity rules forbid.

> **MANUAL:** Verify on ICRIS. Also check whether a Korean or Japanese operating entity exists under a different name — the Japanese App Store listings are under NEOCRAFT LIMITED directly, which suggests not, but a local billing agent may exist.

---

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| All | **NOT ESTABLISHED** | — | — |

**What was checked, so the negative can be weighed properly:**

| Check | Result |
|---|---|
| Homepage, About, Contact, Games, News, Terms, Privacy, FAQ, Announcement — full text | No PSP, acquirer, gateway or orchestrator named. Privacy policy mentions only the generic *"Data from your payment service provider"* among data collected when *"Making a purchase on our Services"* — a category, not a vendor |
| Both checkout pages' full HTML + the recharge JS bundle (`static.neocraftstudio.com/static/accounts/js/recharge3.js`) + `accounts/v3/js/common.js` | **Zero external hosts.** No vendor SDK, no gateway domain, no tokenization library |
| HTTP response headers on `www.`, `accounts.`, `static.` | **No CSP `connect-src` / `script-src` / `frame-src` / `form-action` to read.** `www.` sends only `Content-Security-Policy: frame-ancestors 'none'`; `accounts.` sends none. `static.` is Alibaba Cloud OSS (`server: AliyunOSS`). The infrastructure is Alibaba Cloud WAF (`acw_tc` cookie) behind Google Cloud (`via: 1.1 google`) |
| `POST /payment/default/deal-with-v3` (the order submit) anonymously | `{"code":103,"msg":"Missing parameters"}`. Login-gated beyond that. No downstream gateway host disclosed. I did not create a player account — out of scope for a research run |
| Vendor keyword sweep (`LC_ALL=C grep`, plain patterns) over all retrieved HTML/JS for Xsolla, Appcharge, Stash, Coda/Codashop, Razer, Midasbuy, Nuvei, Payssion, 2C2P, Xendit, Midtrans, Doku, Adyen, Stripe, Checkout.com, Worldpay, Braintree, PayerMax, PacyPay, Oceanpayment, AsiaBill, Airwallex, dLocal, Paymentwall, UniPin, MyCard, Payletter, PayGate, KG Inicis, Boku, Fortumo, Tazapay, Antom, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Juspay, Yuno | **Two hits, both verified false positives:** `omise` inside `new Promise(` and `payCo` inside the function `payCoin()`. Checked by byte-offset context extraction, not line grep. (`Payco` *does* exist as a genuine Korean wallet in the method catalogue — manner_id 131 — so the name appears twice for two different reasons. Context both ways, as the environment notes warn.) |
| WebSearch for Neocraft + each major gaming PSP / web-shop vendor; Neocraft + payment job postings | Nothing. Not a single result referencing Neocraft and any payment vendor together |

> **"No hits found" is a weak negative, not proof of absence.** Something is acquiring 97 payment channels across 40+ countries for this merchant, and it is almost certainly not Neocraft directly. Naming it requires either an authenticated checkout walkthrough (Section 8) or a question on the call.

**What *is* established about the stack, from the merchant's own estate:**

| Finding | Evidence | Source |
|---|---|---|
| **Merchant-owned payment-method catalogue, keyed to player country** | `POST /payment/default/get-manner-list` with `code=<ISO2>` returns `mannerList` (grouped Credit Card / E-Wallet / Cash or prepaid card / Bank transfer), plus `mannerHistoryList`, `recommendList` and `setMannerList` — i.e. remembered, recommended and merchandised method ordering | `[Source Code]` + live API, 43 country codes queried 2026-10-09 |
| **97 distinct live channels** (manner_ids up to 166, so more exist unqueried) | Full catalogue in Section 4 | " |
| **A merchant-owned per-method, per-country fee table, surfaced to the player as "Channel service fee"** | Checkout JS: `var money = amount + tax + fee;` and `html += "…<h4>Channel service fee：</h4><p>$"+fee+"</p>…"`; the fee value arrives in the method API payload and is also written into hidden `<input id="fee" name="fee">` per method tile | `[Source Code]` / `[Checkout]`, `accounts.neocraftstudio.com/pay/index` |
| **A merchant-owned tax/VAT engine** | `POST /pay/get-tax-fee-info` and `/payment/default/get-tax-fee-info` return `vat`, `fee`, `vatFree`, `payNote`; checkout renders a struck-through tax line with a promo note when `vatFree=1` — matching the FAQ's *"Periodic promotions with tax reductions"* | `[Source Code]` |
| **A merchant-owned stored-value wallet — NEO Coins** | `USD $1 = 1 NEO Coin`; obtainable **only** via the website Recharge function; spendable in App Store / Google Play titles launched after 2024-01-01; **non-refundable**; max single recharge **USD $1,000**; tiers $1–$500 plus free-entry custom amount | [FAQ](https://www.neocraftstudio.com/en/faq-list) `[Terms/Privacy Policy]` |
| **Recurring / subscription products exist on the web rail** | Order-status filter includes **`Subscription`** alongside Incomplete / Complete / Canceled / Re-issued / Refunded. Products include *Monthly Spiral*, *Valued Monthly Card*, *VIP Monthly Card* (30 days, stackable), *Legendary Battle Pass*, *Epic Battle Pass*, *Battle Order* | `[Checkout]`, `accounts.neocraftstudio.com/pay/index` + `/payment/default` |
| **Native card fields on the merchant's own origin — no iframe** | `<input class="card-number" id="cardName" … placeholder="Card Number">`, `#expiryDate`, `#CVC` (`placeholder="3 Digits"`), `#nameOnCard`. All plain `type="text"` with no `name` attribute, inside `div.recharge__section__paymentMethod__creditCard`. **No `<iframe>` anywhere on the page.** | `[Source Code]`, `accounts.neocraftstudio.com/pay/index` |
| **Steam as a further distribution rail** | `function isSteamClientInstalled()` probing `steam://` on the account-centre page | `[Source Code]`, `accounts.neocraftstudio.com/client/index` |

**The fee table is the commercial headline.** Selected values, pulled live from the merchant's own API on 2026-10-09 — these are percentages Neocraft adds to the player's total, by method, by country:

| Country | Cheapest card rail | Visa | Mastercard | Cheapest local wallet | Most expensive channel |
|---|---|---|---|---|---|
| 🇰🇷 Korea | **Credit Cards Korea 3.50%** | **4.50%** | **4.50%** | Kakao Pay / Toss Pay / Naver Pay / Payco **0.00%** | Eggmoney 17.00%; MINT 13.00%; Culture Voucher 10.75%; Samsung Pay 4.00% |
| 🇺🇸 US | Credit/Debit Cards 0.00% | **4.50%** | **4.50%** | PayPal / Apple Pay / Google Pay 0.00% | MINT 13.00% |
| 🇦🇺 Australia | Mastercard 2.50% | **4.50%** | 2.50% | PayID 0.00% | MINT 13.00% |
| 🇯🇵 Japan | Mastercard 2.50% | **4.50%** | 2.50% | Google/Apple Pay 0.00% | MINT 13.00% |
| 🇹🇭 Thailand | Mastercard 2.50% | 4.50% | 2.50% | ShopeePay TH 0.00% | **TrueMoney Wallet 18.00%**; Linepay 12.75%; PromptPay 6.00% |
| 🇮🇩 Indonesia | Card Payments 0.00% | 4.50% | 4.50% | DANA / OVO / ShopeePay / LinkAja / DOKU 0.00% | **GoPay 13.75%**; QRIS 4.00% |
| 🇲🇾 Malaysia | Card Payments 0.00% | 2.50% | 2.50% | DuitNow / GrabPay MY / ShopeePay 0.00% | Touch 'n Go 6.05%; Boost 6.05% |
| 🇵🇭 Philippines | Visa 2.50% | 2.50% | 4.50% | PayMaya / GrabPay / Coins.ph 0.00% | GCash 3.75% |
| 🇸🇬 Singapore | Card Payments 0.00% | 4.50% | 4.50% | PayNow / GrabPay / Singtel Dash 0.00% | MINT 13.00%; eNETS 3.70% |
| 🇧🇷 Brazil | Boleto 1.75% | 2.50% | 2.50% | PIX / MercadoPago 0.00% | MINT 13.00% |
| 🇷🇺 Russia | all cards 0.00% | 0.00% | 0.00% | Sberbank / SBP / Tinkoff 0.00% | — |

Read the first row again. **In the account's single largest market, a player paying with a Visa card is charged a full point more than a player paying with a domestic Korean card, and four and a half points more than a player paying with Kakao Pay.** That spread is cost of acceptance, published, and handed to the customer at the moment of purchase.

**Evidence tags used:** `[Checkout]` `[Source Code]` `[Terms/Privacy Policy]` `[Press Release]`. `[Tech Profiler]` was not used — BuiltWith was not retrieved. `[Job Listing]` and `[Provider Case Study]` produced nothing.

### 3B. Payment Orchestrator

**Classification: In-house orchestration layer.**

**Evidence:** the merchant operates its own country-keyed payment-method catalogue API, its own per-method fee table surfaced as "Channel service fee", its own tax/VAT engine, its own order-state machine including a `Subscription` state, its own stored-value wallet (NEO Coins) spendable inside app-store-distributed titles, and its own method merchandising (`recommendList`, `setMannerList`, `mannerHistoryList`). Endpoints: `/pay/get-manner-list`, `/pay/get-tax-fee-info`, `/pay/deal-with-coin`, `/payment/default/get-manner-list`, `/payment/default/get-search-manner-list`, `/payment/default/get-tax-fee-info`, `/payment/default/deal-with-v3`. `[Source Code]` / `[Checkout]`, `accounts.neocraftstudio.com`, retrieved 2026-10-09.

**No third-party orchestrator was detected.** Zero hits for Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY or Yuno across every page and script retrieved, and nothing in search. The `Payment Orchestrator` column is empty for both Neocraft rows in `accounts/apac-tal.csv`, and I could not populate it.

> *"No public evidence was found of a third-party payment orchestration platform. Neocraft appears to have built its own checkout, channel catalogue, fee layer and wallet, integrating directly with one or more underlying providers that could not be identified. **What is explicitly not established is whether any multi-acquirer routing, retry or failover logic exists beneath that layer** — the catalogue is a method *selector*, and a method selector is not a router. The player picks the channel; nothing observed suggests Neocraft re-routes a declined attempt."*

**What the in-house classification means for the motion** — this is the hardest of the four sells, and the approach must respect it:
- **Never say "you have no orchestration layer."** They built one. Saying otherwise is factually wrong and burns the thread.
- The argument is **reach and opportunity cost**: 97 channels, 40+ countries and a per-method fee table are all maintained by hand, by a company of ~100 people whose product is MMORPGs. Every new market, every new rail, every renegotiated rate is engineering time not spent on games.
- The second argument is **what the layer does not do**: there is no observable evidence of routing, retry or failover. A declined Visa attempt in Korea appears to end with the player backing out and choosing a different tile — the same failure mode this repo documented on Webzen's Wcoin wall (`2-ready-to-outreach/webzen.md`).

> **MANUAL:** Register a player account, select a low-value NEO Coins tier, and walk the checkout to the gateway redirect with DevTools open. The network request on `deal-with-v3` will name the PSP in one step. **This is the single highest-value manual action on the account** and it settles both Section 3A and Section 8.

---

## Section 4: Alternative & Local Payment Methods

**Method: direct.** Rather than infer, I queried the merchant's own `get-manner-list` endpoint for each top-10 traffic country plus every APAC market in `CLAUDE.md`'s territory table — 43 country codes on 2026-10-09. Everything below is `Active in checkout`, sourced to `POST https://accounts.neocraftstudio.com/payment/default/get-manner-list` with `code=<ISO2>&op_id=2109`. Figures in parentheses are the merchant's own **channel service fee %**.

### Countries with >1% traffic share (all ten)

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| 🇰🇷 Korea (14.91%) | Visa (4.50), Mastercard (4.50), **Credit Cards Korea** (3.50), Amex (0.00), Discover (3.95), Diners (3.95), UnionPay (2.50), JCB (3.75), Credit/Debit Cards (0.00) | Cards | Active in checkout | `get-manner-list?code=KR` |
| 🇰🇷 Korea | **Kakao Pay (0.00), Toss Pay (0.00), Naver Pay (0.00), Payco (0.00), Samsung Pay (4.00)**, Apple Pay (0.00), Google Pay (0.00), PayPal (0.00), WeChat Pay (0.00), AliPay (3.00) | Digital wallet | Active in checkout | " |
| 🇰🇷 Korea | **Culture Voucher (10.75), Eggmoney (17.00), Teencash (0.00), Cashbee (0.00), Book Gift Voucher (0.00), Happy Voucher (0.00)**, MINT (13.00) | Cash/voucher | Active in checkout | " |
| 🇰🇷 Korea | **Bank Transfer Korea (0.00)** | Bank transfer / A2A | Active in checkout | " |
| 🇷🇺 Russia (10.43%) | MIR (0.00), Visa (0.00), Mastercard (0.00), JCB (0.00); **Sberbank, SBP, TinkoffBank** (0.00) | Cards + A2A | Active in checkout | `code=RU` |
| 🇹🇷 Turkey (8.75%) | Cards; Google/Apple Pay, PayPal, WeChat, AliPay; MINT | Cards + wallet + cash | Active in checkout | `code=TR` |
| 🇺🇸 US (6.31%) | Cards; PayPal, Apple/Google Pay; **Dollar General (0.00), CVS Pharmacy (0.00)**, MINT (13.00) | Cards + wallet + retail cash | Active in checkout | `code=US` |
| 🇧🇬 Bulgaria (5.49%) | Cards; PayPal, Apple/Google Pay; MINT | Cards + wallet + cash | Active in checkout | `code=BG` |
| 🇸🇦 Saudi (5.43%) | Cards; Apple/Google Pay, PayPal; MINT | Cards + wallet + cash | Active in checkout | `code=SA` |
| 🇧🇷 Brazil (4.97%) | Visa (2.50), Mastercard (2.50), **Boleto (1.75)**; **PIX (0.00), MercadoPago (0.00)**; **Safetypay (0.00)** | Cards + A2A + voucher | Active in checkout | `code=BR` |
| 🇬🇧 UK (4.59%) | Cards; Google/Apple Pay, PayPal; MINT | Cards + wallet | Active in checkout | `code=GB` |
| 🇪🇸 Spain (3.87%) | Cards; wallets; **Sofort (0.00)** | Cards + A2A | Active in checkout | `code=ES` |
| 🇦🇺 Australia (2.46%) | Visa (4.50), Mastercard (2.50), Amex, Discover, Diners, UnionPay, JCB; Google/Apple Pay, PayPal, WeChat, AliPay; MINT (13.00); **PayID (0.00)** | Cards + wallet + A2A | Active in checkout | `code=AU` |

### APAC markets below the top-10 cut, checked anyway — this is where the gaps are

| Market | Present | **Absent — and these absences are sourced, not assumed** |
|---|---|---|
| 🇯🇵 **Japan** | Cards (Visa 4.50, MC 2.50, Amex 0.00, JCB 3.75, UnionPay 2.50), Google/Apple Pay, PayPal, WeChat, AliPay, MINT (13.00) | ⚠️ **No konbini. No PayPay. No LINE Pay. No Rakuten Pay. No Paidy. No carrier billing. No bank transfer. No instalment/bonus-payment option.** `get-manner-list?code=JP` returns three groups and fourteen channels, all of them global. **Note: LINE Pay exists in the catalogue (manner_id 58) and is served to Thailand — so it is configured but not enabled for Japan.** |
| 🇮🇳 **India** | Cards (Visa 4.50, MC 4.50, Amex, Discover, Diners, UnionPay, JCB), PayPal, Apple/Google Pay, WeChat, AliPay, MINT | ⚠️ **No UPI. No netbanking. No RuPay. No Paytm / PhonePe. No EMI or card instalments. No UPI Autopay** (relevant: they sell 30-day Monthly Cards). India gets a card-only, global-wallet checkout. |
| 🇹🇼 **Taiwan** | Cards (UnionPay 0.00, Amex 0.00), Google/Apple Pay, PayPal, **MyCard Wallet (0.00)**, WeChat, AliPay, MINT | ⚠️ **No JKOPay. No LINE Pay TW. No convenience-store cash. No ATM / virtual-account transfer. No domestic instalments.** |
| 🇭🇰 **Hong Kong (HQ)** | Cards (UnionPay 0.00, Amex 0.00), Google/Apple Pay, PayPal, **AlipayHK (0.00)**, MyCard Wallet, WeChat, AliPay, MINT | ⚠️ **No FPS. No Octopus.** Its own home market is thinner than Malaysia's. |
| 🇻🇳 Vietnam | Cards, **NGANLUONG, MOMO_VIETQR, VTCPay, VIETQR** (all 0.00), Google/Apple Pay, PayPal, MINT | No ZaloPay; no cash-on-delivery. Reasonably covered. *Note: iOS catalogue in Vietnam is empty of Neocraft games (only the NTools utility).* |
| 🇸🇬 Singapore | **PayNow, GrabPay, Singtel Dash** (0.00), Card Payments (0.00), cards, wallets, **eNETS (3.70)**, MINT | Well covered |
| 🇮🇩 Indonesia | **QRIS (4.00)**, **DANA, OVO, ShopeePay, LinkAja, Sakuku, DOKU Wallet** (0.00), **GoPay (13.75)**, **Gudang Voucher (0.00)**, Card Payments (0.00), cards | Well covered. No Alfamart/Indomaret cash by name (Gudang Voucher is the voucher rail) |
| 🇲🇾 Malaysia | **FPX ("Financial Process Exchange", 0.00)**, **MAE/DuitNow (0.00)**, **Touch 'n Go (6.05)**, **Boost (6.05)**, GrabPay MY, ShopeePay, Mcash, MyCard, Card Payments, cards | Well covered |
| 🇹🇭 Thailand | **PromptPay (6.00)**, **Kplus (0.00)**, **TrueMoney Wallet (18.00)**, **Linepay (12.75)**, ShopeePay TH (0.00), **7-Eleven (0.00)**, cards | Well covered, but note the 18% and 12.75% surcharges on the two most-used wallets |
| 🇵🇭 Philippines | **GCash (3.75)**, **PayMaya (0.00)**, GrabPay, **Coins.ph (0.00)**, **Dragonpay (0.00)**, **Bank Transfer Philippines (0.00)**, **7-Eleven (0.00)**, **Cash at Retail Philippines (0.00)**, cards | Well covered |
| 🇨🇳 Mainland China | **AliPay (3.00)**, **WeChat Pay (0.00)**, **UnionPay (0.00)**, cards, Apple/Google Pay, PayPal, MINT | Covered on the three that matter |
| 🇳🇿 New Zealand | Cards, Google/Apple Pay, PayPal, MINT | No POLi; no A2A at all |
| 🇵🇰 Pakistan | **Easypaisa (15.00), Jazzcash (15.00)** | Covered but at 15% |

**Full channel catalogue observed: 97 distinct methods**, grouped Cards / E-Wallet / Cash or prepaid card / Bank transfer, with ids running to 166 (so more exist in markets not queried). Notable channels beyond those above: iDeal (NL), Bancontact (BE), Blik + Przelewy24 + Bank Transfer Poland (PL), Giropay + Sofort (DE), Carte bancaire (FR), Mybank (IT), OXXO + Todito + Efectivo + Bank Transfer Mexico (MX), RapiPago (AR), PSE + Efecty + Davivienda (CO), NeoSurf, Paga (NG).

> *"**Warning: in Japan, konbini (convenience-store cash) and PayPay are widely used but are not supported by Neocraft** — despite two dedicated Japanese App Store titles under NEOCRAFT LIMITED (1,564 Japanese ratings on クロニクル・オブ・インフィニティ) and both of those titles being selectable in the web recharge store. `apac-payments.md` §2 flags konbini and PayPay absence on a Japan-facing checkout as a concrete gap; **a current market-share citation for either rail must be sourced before this goes in an email** — I did not obtain one."*

> *"**Warning: in India, UPI is the dominant domestic consumer rail and is not supported by Neocraft.** Same caveat: source a current UPI share figure before citing it. India is not in the top-10 traffic cut, so this is a growth argument, not a leak-stopping one."*

**The honest headline on this section: this is not a rail-gap account.** 97 channels, QRIS, FPX, DuitNow, PayNow, GCash, PromptPay, PIX, Boleto, PayID, MIR, and the full Korean wallet set — that is broader coverage than most merchants this repo has researched. **The gap is not which rails exist. It is what each one costs the player.**

> **MANUAL:** VPN into Korea, Japan and Australia and confirm the live checkout matches the API payload, and that the channel service fee is displayed to the player as the JS suggests (`<h4>Channel service fee：</h4>`).

---

## Section 5: Payment Issues & Customer Complaints

**Method and scope.** The App Store customer-review RSS feed was pulled for all nine apps on the US developer page across two storefronts (US and KR) — `https://itunes.apple.com/{us,kr}/rss/customerreviews/page=1/id={appId}/sortby=mostrecent/json` — approximately **300 reviews** in total, then keyword-filtered for recharge / top-up / payment / purchase / charge / refund / declined / transaction / billing. Reddit, Trustpilot and X searches returned nothing referencing Neocraft.

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| **Declined transactions** | — | **None found** | — | — |
| **Duplicate charges** | — | **None found** | — | — |
| **Failed recurring payments** | — | **None found** | — | — |
| **Web recharge / top-up failures** | — | **None found** | — | — |
| **Checkout errors** | — | **None found** | — | — |
| **Currency conversion / FX** | — | **None found** | — | — |
| Entitlement not delivered after paid purchase | App Store (US), The Dragon Odyssey | Isolated — 1 review | Recent (most-recent feed, pulled 2026-10-09) | [RSS, id 6503807938](https://itunes.apple.com/us/rss/customerreviews/page=1/id=6503807938/sortby=mostrecent/json) — *"They also disabled all monthly card privileges even though you pay real money for those. So they basically stole your money."* |
| Refund request refused | App Store (US), Chronicle of Infinity | Isolated — 1 review | Recent | [RSS, id 1369685711](https://itunes.apple.com/us/rss/customerreviews/page=1/id=1369685711/sortby=mostrecent/json) — *"i asked for a refund for the little bit i spent… and they flat out said no"* |
| Account-merge confusion after top-up | App Store (US), Guardians of Cloudia | Isolated — 1 review | Recent | [RSS, id 1544039144](https://itunes.apple.com/us/rss/customerreviews/page=1/id=1544039144/sortby=mostrecent/json) — *"Used Apple ID to login got a bunch of other accounts that aren't mine… top up for nothing"* |
| Monetisation / pay-to-win pressure | App Store, all titles | **High** — the dominant complaint theme across every title | Recent | Same feeds |
| App crashes / bugs / lag | App Store, all titles | Moderate | Recent | Same feeds |

**The distinction matters and it is the finding.** The reviews are loud about money — *"you need to pay at least $200 a month to be decent"*, *"$75 for an outfit"*, *"you'll end up spending $1000"* — but **every one of those is a game-design complaint about how much things cost, not a payments complaint about a payment failing.** Nothing in ~300 reviews describes a declined card, a double charge, a failed renewal, a stuck top-up or a web checkout error. The crash and bug complaints are app-quality issues on Apple's rail, not payments findings.

> *"**No payment-rail complaint pattern found** on Reddit, X, Trustpilot or App Store reviews. Three isolated items touch payments adjacently — one undelivered monthly-card entitlement, one refused refund and one post-top-up account mix-up — and the refund refusal is consistent with Neocraft's own published policy that **'Any purchases of Virtual Goods or Virtual Currency… are final. No refunds will be given'** ([Terms](https://www.neocraftstudio.com/en/terms)) and that **'NEO Coins are non-refundable'** ([FAQ](https://www.neocraftstudio.com/en/faq-list)). No orchestration opportunity can be argued from complaint data on this account. Do not manufacture one."*

⚠️ **One genuine fraud signal, from the merchant rather than the players.** The [Unauthorized 3rd-party Top-up Penalty Policy](https://www.neocraftstudio.com/announcement?language=en) names *"**credit card fraud**, failure to credit recharges, account theft"* among the risks of unauthorised top-up platforms, and says the operations team is *"actively monitoring and detecting"* them while players are being *"blocked due to invalid recharges"*. That is a merchant telling the market, in public, that it is managing chargeback and fraud exposure on its own rail **manually, with account bans.**

---

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | **2026-07-30** | **Dynasty Warriors: Overlords** released on iOS and Android — *"officially licensed by Koei Tecmo"*, shipped ahead of the announced 2026-08-02 date after two slips. Ships with **Indonesian, Malay, Vietnamese, Thai and Korean** localisation; listed in Korea as 진삼국무쌍-오버로드. Marketed on Neocraft's own site as **Dynasty Warriors: Overlords XL** | Market Expansion / Licensed IP | [ixbt.games](https://ixbt.games/en/news/2026/07/31/425853-klassika-musou-v-karmane-na-ios-i-android-sostoialsia-vnezapnyi-reliz-dynasty-warriors-overlords.html) · [Apple](https://itunes.apple.com/lookup?id=6757413794&country=us) |
| 2 | **2026-05-21** | **Spirits of Aetheria** released (MMORPG; EN + ZH) | Market Expansion | [Apple](https://itunes.apple.com/lookup?id=6754444931&country=us) |
| 3 | **2025-08-22** | **Tree of Savior: NEO wins Best Trending AppGallery Game at the 2025 Mobile Gamer Awards**; featured live at HUAWEI AppGallery's Gamescom booth (Hall 9, A.040), Cologne | Partnership / Distribution | [PR Newswire](https://www.prnewswire.com/il/news-releases/huawei-appgallery-invites-you-to-dive-into-award-winning-tree-of-savior-neo--live-demos--exclusive-events-await-at-gamescom-2025-302536691.html) |
| 4 | **2025-06-12** | **Tree of Savior: NEO launches worldwide** (pre-registration opened 2025-03-31) | Market Expansion | [News index](https://www.neocraftstudio.com/en/news.html) · [Apple](https://itunes.apple.com/lookup?id=6742529924&country=us) |
| 5 | **2025-01-09 / 2025-02-25** | **The Dragon Odyssey** and **Tales of Wind: Radiant Rebirth** launch — three new titles in 2025 | Market Expansion | [News index](https://www.neocraftstudio.com/en/news.html) · Apple metadata |

**Payment-platform signals, stated precisely:**
- **No public payment-related RFP found.**
- **No payment-related job posting found** — searched job boards and general web. Weak negative: Neocraft publishes no careers page I could locate.
- ✅ **A named, externally-published payments owner:** *"Business Inquiries: (for localization and payment service) — **Yihan Lai**, yihan@neocraftstudio.com"* ([Contact](https://www.neocraftstudio.com/en/contact)). The company pairs **localization and payment** under one contact, which is exactly how a publisher thinks about market entry. The other two business contacts are Justin Yang (cooperation) and Nick Hu (advertising).
- **No licence application found** in any APAC market.
- **No funding round, investor or M&A event found.**
- ⚠️ **Note what is NOT a payments signal:** the NEO Coins wallet's own cut-off — *"supported in games launched on App Store and Google Play after January 1, 2024"* — dates the web-wallet build to roughly **2024**. That is a two-year-old build, not a current project. **No evidence was found of an active payments re-platforming.** Do not imply one.

---

## Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | Undated (live 2026-10-09) | **"Unauthorized 3rd-party Top-up Penalty Policy"** — Neocraft bans players for topping up via unauthorised platforms; cites personal-data leakage, credit-card fraud, uncredited recharges and account theft; ops team actively detecting | **The most payment-relevant document the company publishes.** It is a merchant defending its own billing channel against third-party top-up aggregators, by hand | [neocraftstudio.com/announcement](https://www.neocraftstudio.com/announcement?language=en) |
| 2 | Live 2026-10-09 | Homepage tile: **"Recharge Discounts — Enjoy Up to 10% Off Discount Now!"** | A standing public discount to pull purchases off Apple/Google onto the merchant's own rail | [Homepage](https://www.neocraftstudio.com/) |
| 3 | Live 2026-10-09 | FAQ: NEO Coins — web-only acquisition, redeemable inside App Store / Google Play titles post-2024-01-01, **USD $1,000 single-recharge ceiling**, *"additional n% in-game currency rebate"*, *"periodic promotions with tax reductions"*, 1:100 bonus points, **non-refundable** | The web-billing architecture, documented by the merchant | [FAQ](https://www.neocraftstudio.com/en/faq-list) |
| 4 | 2025-08-22 | Huawei AppGallery distribution partnership + award | A third app-store rail; also unroutable | [PR Newswire](https://www.prnewswire.com/il/news-releases/huawei-appgallery-invites-you-to-dive-into-award-winning-tree-of-savior-neo--live-demos--exclusive-events-await-at-gamescom-2025-302536691.html) |
| 5 | — | **No PSP partnership, provider removal, checkout migration or payment-infrastructure announcement found** in company news, thepaypers, finextra, pymnts, techinasia, e27 or any trade source | — | [News index](https://www.neocraftstudio.com/en/news.html) |

**No provider removals to flag** — no provider was ever named to begin with.

---

## Section 8: Checkout Experience Audit

Both checkouts were retrieved and read in full source. **Flow beyond method selection is login-gated**, and I did not create a player account. Findings below are everything publicly observable plus the server-rendered payload.

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | **Custom-built, merchant-hosted** on `accounts.neocraftstudio.com`. Two flows: NEO Coins wallet top-up (`/pay/index`) and direct game recharge (`/payment/default`). Yii PHP framework (`/assets/*/yii.js`), jQuery 1.10.1, Bootstrap | Fair | Entirely first-party. No hosted PSP page, no PSP-branded shell |
| Guest checkout | ❌ **No.** Login required; anonymous API calls return `{"code":120,"msg":"Login expired"}` with a redirect to `/client/index?client_id=dRDWKPT8p` | Poor | Unavoidable for a game top-up — the order must bind to a character — but it is friction on top of friction |
| Steps to complete payment | **Game recharge: 3 numbered steps** — ① One-Click Use (game → server → Role ID, with live `check-role` validation) ② Items and Bonus ③ Select Payment Method (country → group → channel). **NEO Coins: 2** — amount tier or custom amount → payment method | Fair | The Role-ID step is a real abandonment risk: the help text itself says *"Check on where to find the character ID after selecting your game"* |
| Card input experience | ⚠️ **Custom fields on the merchant's own origin.** `<input class="card-number" id="cardName">`, `#expiryDate` (`MM/YY`), `#CVC` (`3 Digits`), `#nameOnCard` — plain `type="text"`, digit-stripping `oninput` handlers, **no `name` attributes, and no `<iframe>` anywhere on the page** | **Poor** | PAN and CVV are typed into Neocraft's own DOM. Whether they are then tokenized client-side to a PSP or posted to Neocraft's server could not be observed without login — but the *fields themselves* are first-party either way |
| Payment methods visible | **97 distinct channels** across 4 groups, country-filtered, with per-method fee badges and a **"Common Payments"** row built from the player's own history plus `recommendList` and `setMannerList` | **Good** | This is the strongest part of the experience |
| Location-based method display | ✅ **Yes, and well done.** A full ~200-entry country selector drives `get-manner-list`; the returned set is genuinely market-specific (Korea gets Korean wallets and six Korean cash vouchers; Brazil gets PIX and Boleto; Malaysia gets FPX and DuitNow) | **Good** | Manual country selection rather than geo-IP, as far as can be observed |
| Instalment / EMI options | ❌ **None found in any market** — no India EMI, no Japan instalment or bonus payment, no Taiwan instalments, no Korean card instalments, no BNPL anywhere (no Paidy, Afterpay, Zip, Atome or Klarna in the 97-channel catalogue) | Poor | Low ticket sizes make this less critical than for travel or edtech, but the $500 tier and $1,000 ceiling are not low-ticket |
| 3DS implementation | **Not detected.** No 3DS library, no ACS redirect handler, no challenge-window code in any retrieved script | Unknown | Almost certainly handled downstream by the unidentified PSP. **Cannot be confirmed without an authenticated walkthrough** |
| PCI indicator | ⚠️ **Self-hosted card fields, not a PSP iframe.** See above | **Poor** | See Section 9 |
| Mobile responsiveness | Bootstrap grid with explicit `col-xs-*` classes, a separate mobile logo asset and a mobile nav. **73.08% of traffic is mobile web** (SimilarWeb supplied), so this is the primary surface | Fair | Not verified on a real device |
| Multi-currency / local pricing | ❌ **USD only.** `USD $1 = 1 NEO Coin`; every tier is USD; the confirmation template hardcodes `"$"`. Local *methods* are offered, but **not local currency pricing** | **Poor** | A Korean player pays a USD-denominated amount on a Korean wallet, plus a Neocraft channel service fee, plus whatever their issuer adds for FX. **This is the clearest unaddressed cost stack in the whole audit** |
| Saved payment methods | ✅ Partially. `mannerHistoryList` returns the player's previously used method into a "Common Payments" row | Fair | Method memory, not credential vaulting. **No evidence of card-on-file, network tokens or an account updater anywhere** |
| Error message clarity | Generic. `#error-tips` renders `"Network error"` on AJAX failure; API errors include `"This product does not exist, please contact webmaster! Thank you!"` and `"Login expired"`. A post-payment modal asks *"Please confirm the payment result — if the payment was not successful, please select 'Payment Problem'"* | **Poor** | **The merchant asks the player to self-report whether the payment worked.** That is a reconciliation gap, not a copy problem |
| Tax handling | Merchant-computed. `get-tax-fee-info` returns `vat`, `fee`, `vatFree`, `payNote`; the confirmation shows `Price` / `Tax` / `Channel service fee` / `Payment method`, and strikes the tax line through with a promo note when `vatFree=1` | Fair | Real per-market tax logic, built in-house |
| Recurring products | *Monthly Spiral*, *Valued Monthly Card*, *VIP Monthly Card* (30 days, stackable), *Legendary / Epic Battle Pass*, *Battle Order*; a `Subscription` order state exists | — | **Sold as repeat one-off purchases, with no observable mandate, auto-renewal or stored-credential rail** |

> *"Full checkout flow not accessible — the payment step beyond method selection requires an authenticated player account, which was out of scope. Findings are limited to publicly observable elements plus the server-rendered method payload. **The one unobserved step is also the one that names the PSP.**"*

**Three findings here are outreach-grade on their own:** USD-only pricing on localised rails; self-hosted card fields; and a post-payment modal that asks the player to confirm whether their own payment succeeded.

---

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **Not found.** No PCI statement, AOC, trust-centre page or security page exists on the site | — |
| Card data handling | ⚠️ **Card fields are first-party.** `<input class="card-number" id="cardName">`, `#expiryDate`, `#CVC`, `#nameOnCard` render directly in `accounts.neocraftstudio.com/pay/index` with **no iframe and no PSP-hosted field library**. The privacy policy confirms the data category collected: *"Making a purchase on our Services — Payment data; **Typical credit card information (name, address, credit card number, expiration date and security code)**; Data from your payment service provider"* | [`/pay/index`](https://accounts.neocraftstudio.com/pay/index) `[Source Code]` · [Privacy Policy](https://www.neocraftstudio.com/en/privacy) `[Terms/Privacy Policy]` |
| Likely SAQ scope | `[INFERENCE, not confirmed]` **SAQ A-EP at best, and plausibly full PCI scope.** A merchant whose own page renders the PAN and CVV inputs cannot claim SAQ A. Whether the values are tokenized client-side to a PSP before leaving the browser, or posted to Neocraft's own server, **could not be determined without an authenticated checkout walkthrough** — and that distinction is the whole difference between A-EP and full scope. The privacy policy's explicit listing of *"credit card number… and security code"* as data the company collects is the stronger of the two signals, and it points the wrong way | — |
| Recommended Yuno integration | **SDK (hosted fields / drop-in)** — not back-to-back API. The entire point for this merchant is to get the PAN and CVV out of their own DOM | — |

**Do not state a compliance level.** None is published. What *is* evidenced is that the merchant collects card data in its own page and names that collection in its own privacy policy.

> **MANUAL:** This is the second-highest-value manual action after the gateway walkthrough — and they are the same action. Watch the network tab at card submit. If the PAN goes to a third-party tokenization endpoint, scope is A-EP; if it goes to `accounts.neocraftstudio.com`, scope is full, and PCI-scope reduction becomes a board-level reason to take the meeting.

---

## Section 10: Strategic Insights & Outreach Angles

> ### Insight #1: The channel service fee is a published price list for their own cost of acceptance — and in their largest market the cross-border card rail is the most expensive thing a player can pick
>
> **Evidence:** **Section 3A / Section 4** — the merchant's own `get-manner-list` API, queried 2026-10-09, returns a per-method, per-country fee that the merchant's own checkout JS adds to the player's total and labels **"Channel service fee"** (`var money = amount + tax + fee;`). In Korea: Visa **4.50%**, Mastercard **4.50%**, *Credit Cards Korea* **3.50%**, Kakao Pay / Toss Pay / Naver Pay / Payco **0.00%**. **Section 1 / Section 2** — Korea is the single largest market at **14.91%** of visits and there is **no Korean entity**; the card leg is acquired cross-border from Hong Kong.
> **Pain Point:** Neocraft has priced its own acquiring inefficiency and handed the bill to the customer at the moment of purchase. A Korean player with a Visa card faces a 4.5% surcharge, so they either absorb it, switch method mid-checkout, or abandon. The merchant pays either way — in conversion, in mix shift to whatever is cheapest rather than whatever converts best, or in margin when it eats the fee on a promotion. And the one-point spread between Visa and the domestic Korean card rail is a direct, published, self-reported measure of what cross-border acquiring costs them.
> **Yuno Value Proposition:** Route the Korean card leg to a local acquirer in the cardholder's geography instead of out of Hong Kong, through one integration rather than a new provider contract per market. Local acquiring addresses both legs of the problem at once: the scheme-cost spread that produces the surcharge, and the foreign-acquired decline rate that `apac-payments.md` §3 identifies as the stronger of the two cross-border arguments in this territory. If the surcharge comes down, the fee column stops steering the player away from the method they actually wanted.
> **Best Success Case:** **NetEase Games** — an Asia-HQ'd publisher whose paying players are mostly outside its home market, which is Neocraft's exact shape at 17.37% APAC. *(Nameable on Yuno's own customer list. No published metric exists — attach no number.)*
> **Outreach Angle:** Your recharge page quotes a 4.5% channel service fee on Visa in Korea and 3.5% on the domestic Korean card rail — that one-point spread is what acquiring a Korean card out of Hong Kong costs you, and your players are reading it at checkout.
> **Suggested Subject Line:** The 1-point spread on your Korean recharge page

> ### Insight #2: You built the wallet, the catalogue, the fee table and the tax engine — ninety-seven channels, forty countries, by hand
>
> **Evidence:** **Section 3B** — merchant-built country-keyed method API, fee table, VAT engine, order-state machine with a `Subscription` state, method merchandising, and the NEO Coins wallet, all first-party on `accounts.neocraftstudio.com`, with **no third-party orchestrator detected** (zero hits for Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY or Yuno). **Section 4** — **97 distinct live channels across 40+ countries**, confirmed from the API itself. **Section 2** — delivered by a company of ~**100+ people from 7 countries** whose product is MMORPGs, not payments.
> **Pain Point:** Every market entry now carries a payments project. Dynasty Warriors: Overlords added Indonesian, Malay, Vietnamese, Thai and Korean in July 2026 — five new localisations, each with its own rail expectations, each a channel to source, price, tax-configure and maintain. The fee table is the tell: it is maintained by hand, per method, per country, and it is now visible to customers. This is opportunity cost, not incompetence — the layer works. It just costs a game studio engineering quarters that should be going into games.
> **Yuno Value Proposition:** Keep the NEO Coins wallet, the storefront and the player experience exactly as they are — Yuno sits underneath as the provider and rail layer, so new markets become configuration rather than integration. One integration for the local rails, one place to renegotiate rates, one reconciliation view instead of a per-provider spreadsheet. **Never frame this as "you need orchestration."** They have a layer. The frame is: you built the hard half; stop maintaining the boring half.
> **Best Success Case:** **Garena (Sea Limited)** — a SEA-centred F2P publisher with heavy local-rail and direct top-up dependence; the closest match on channel breadth. *(Nameable on Yuno's own customer list. No published metric exists — attach no number.)*
> **Outreach Angle:** Ninety-seven payment channels across forty-odd countries, a per-method fee table and a stored-value wallet — all of it built in-house, by a studio of a hundred people whose product is MMORPGs.
> **Suggested Subject Line:** 97 channels, 100 people

> ### Insight #3: Your own checkout asks the player whether their payment worked
>
> **Evidence:** **Section 8** — the post-submit modal on `/pay/index` reads *"Please confirm the payment result. If the payment was not successful, please select 'Payment Problem'."* **Section 7 / Section 5** — the public [Unauthorized 3rd-party Top-up Penalty Policy](https://www.neocraftstudio.com/announcement?language=en) names *"credit card fraud, **failure to credit recharges**"* and says the operations team is *"actively monitoring and detecting"* while players are *"blocked due to invalid recharges"*. **Section 8** — no 3DS implementation detected; no card-on-file, network token or account-updater evidence anywhere; error handling degrades to a bare `"Network error"`.
> **Pain Point:** Asking the customer to self-report payment outcome means the merchant does not have reliable real-time settlement status back from whatever sits downstream. That produces exactly the two symptoms the merchant itself publishes: uncredited recharges, and a fraud-and-chargeback problem being managed with manual account bans. It also means nobody can answer "what is our authorisation rate, by market, by method" — because the authorisation result arrives as a support ticket.
> **Yuno Value Proposition:** A single unified transaction and settlement view across every provider and rail, with webhook-driven status instead of player self-attestation; decline-code-aware retry rather than "pick a different tile"; network tokens and account updater inside the routing layer so the 30-day Monthly Card and Battle Pass renewals stop failing on reissued credentials. The reconciliation story is the one that lands first here, because it is the one they have already admitted to in writing.
> **Best Success Case:** **NetEase Games** — scale and multi-market provider breadth. *(No published metric. Attach no number.)*
> **Outreach Angle:** The modal after your recharge submit asks the player to tell you whether the payment succeeded — which means the authorisation result is reaching you as a support ticket rather than a webhook.
> **Suggested Subject Line:** Who tells you the payment worked?

> ### Insight #4: You price in USD and collect in Kakao Pay, PIX, FPX and QRIS
>
> **Evidence:** **Section 8** — `USD $1 = 1 NEO Coin`, every tier USD-denominated, confirmation template hardcodes `"$"`; **no local-currency pricing in any market**. **Section 4** — yet the checkout serves Kakao Pay, Toss Pay, Naver Pay and six Korean cash vouchers in Korea; PIX and Boleto in Brazil; FPX and DuitNow in Malaysia; QRIS and five wallets in Indonesia; PayID in Australia. **Section 1** — Korea 14.91%, Russia 10.43%, Turkey 8.75%, Brazil 4.97%, Australia 2.46%, and only 17.37% of the audience in APAC at all.
> **Pain Point:** Local rails with foreign pricing. The player picks their domestic wallet and is still quoted a dollar amount, then pays Neocraft's channel service fee, then pays their own issuer's or wallet's FX margin. Three cost layers stacked on one transaction, two of them invisible until the statement arrives. `apac-payments.md` §3 is explicit that FX sits outside any scheme-cost discussion — this merchant has an FX leg across more than forty currencies and no local pricing anywhere.
> **Yuno Value Proposition:** Local-currency presentment with local acquiring and settlement per corridor, so the price the player sees is the price in their own money and the FX leg stops being the player's problem. This is the natural second conversation after local acquiring in Korea — same mechanism, different benefit, and it is measurable on the same cohort.
> **Best Success Case:** **Garena (Sea Limited)** — multi-market local-rail collection at consumer ticket sizes. *(No published metric. Attach no number.)*
> **Outreach Angle:** A player in Seoul picks Kakao Pay and is quoted in dollars — the rail is local, the price isn't, and the FX sits on top of your channel service fee.
> **Suggested Subject Line:** Local rail, foreign price

> ### Insight #5: The card fields are on your page, not your provider's
>
> **Evidence:** **Section 8 / Section 9** — `<input class="card-number" id="cardName">`, `#expiryDate`, `#CVC`, `#nameOnCard`, all plain text inputs on `accounts.neocraftstudio.com`, **no iframe on the page**; and the [privacy policy](https://www.neocraftstudio.com/en/privacy) listing *"Typical credit card information (name, address, credit card number, expiration date and security code)"* among the data the company collects. **Section 3A** — no PSP tokenization library of any kind in any retrieved script.
> **Pain Point:** A merchant rendering its own PAN and CVV inputs cannot be in SAQ A. At best this is SAQ A-EP; if the values reach Neocraft's own server it is full PCI scope — annual assessment, segmented infrastructure, pen testing, and a card-data breach that lands on Neocraft rather than a provider. For a hundred-person game studio that is an entirely avoidable category of risk, and the fix is an afternoon's integration work.
> **Yuno Value Proposition:** Yuno's hosted-fields SDK moves card capture off Neocraft's origin entirely, collapsing PCI scope to SAQ A while *keeping* the custom checkout look — and bringing network tokens and account updater with it, which the Monthly Card and Battle Pass products need anyway (Section 8: no stored-credential rail observed).
> **Best Success Case:** **NetEase Games** — large publisher, SDK-based card capture at scale. *(No published metric. Attach no number.)*
> **Outreach Angle:** Your recharge page renders the card number and CVV as its own inputs, and your privacy policy says you collect the security code — that is PCI scope you don't need to be carrying.
> **Suggested Subject Line:** Why is the CVV field on your domain?

---

## Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. Your recharge page quotes a 4.5% channel service fee on Visa in Korea against 3.5% on the domestic Korean card rail — that spread is the cost of acquiring a Korean card out of Hong Kong, and your players read it at checkout.
2. Ninety-seven payment channels across forty-odd countries, a per-method fee table and a stored-value wallet, all built in-house by a hundred-person MMORPG studio — you built the hard half of a payments platform to get off Apple's rail.
3. The modal after your recharge submit asks the player to confirm whether the payment succeeded, which means the authorisation result reaches you as a support ticket rather than a webhook.
4. A player in Seoul picks Kakao Pay and is still quoted in US dollars — local rail, foreign price, your channel fee, then their FX on top.
5. Dynasty Warriors: Overlords shipped in July with Indonesian, Malay, Vietnamese, Thai and Korean — five new localisations, five sets of rail expectations, all of it configured by hand.

**Cold call openers (conversational, one sentence each):**
1. "I was looking at your NEO Coins recharge page — you're one of very few publishers this size that actually built a web store to get purchases off the app stores, and I wanted to ask what that's costing you to maintain."
2. "Quick one: your checkout shows a 4.5% channel service fee on Visa in Korea and nothing on Kakao Pay — is that fee steering your Korean mix, or are you eating it on promotions?"
3. "You publish a policy banning players who top up through third-party platforms — I'm curious how much of that is fraud and chargeback exposure versus just protecting the channel."
4. "Who owns payments over there? Your contact page pairs localisation and payment under one person, which tells me you think about rails at market-entry time — that's rarer than it should be."

---

## Section 11: Similar Companies & Prospecting Pipeline

### 11A. Direct Competitors (F2P mobile MMORPG publishers, APAC-operating, comparable scale)

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| **Gravity** | gravity.co.kr | South Korea | **$388.0M FY2025** (audited 20-F) | KR, TW/HK/MO, SEA, LatAm, US — **near-identical web-top-up shape** | **ECPay, GASH Plus, So-net mpay, MyCard (TW/HK/MO); UniPin, Razer Gold, GOC Pay, OneOne (SEA/TH); EBANX, Xsolla Pay (LatAm); Mobilians (KR); PayPal (US/CA).** **Orchestrator: none detected — greenfield** | `accounts/apac-tal.csv`; verified in `2-ready-to-outreach/gravity.md` (2026-09-20) |
| **Webzen** | webzen.com | South Korea | KRW 174.4bn FY2025 (~$121M) | KR, global portal, TH, BR, JP, EU, US | **Global portal:** ChillPay (TH), Boacompra, PagSeguro, three separate PayPal tiles, Terminal3, paysafecard, EPIN, Multi Game Card. **Korea:** KG Mobilians, Galaxia Money Tree, Toss Payments, Payletter, Hecto Financial, NHN KCP. **Orchestrator: in-house (Wcoin wallet over a hand-wired tile wall) + PortOne incumbent on Korean mobile** | `accounts/apac-tal.csv`; verified in `2-ready-to-outreach/webzen.md` |
| **Com2uS** | com2us.com | South Korea | $496–534M FY2024 (audited) | KR + 15-language global | **PortOne (orchestrator), Xsolla (global MoR), MyCard, Terminal3, NHN KCP, Toss Payments, Naver Pay.** **Orchestrator: PortOne — REGIONAL ORCHESTRATOR INCUMBENT** | `accounts/apac-tal.csv`; verified in `2-ready-to-outreach/com2us.md` against Com2uS's own newsroom |
| **Gamania Digital Entertainment** | gamania.com | Taiwan | Not found | TW, HK, JP, KR, SEA | Not researched | `accounts/apac-tal.csv` |
| **IGG** | igg.com | Singapore | ~$750M (FY24) | Global F2P, SEA + Western | Not researched | `accounts/apac-tal.csv` |
| **SpinX Games** | spinxgames.com | **Hong Kong** | ~$1B est. | Global mobile — **nearest HK-domiciled peer by geography** | Not researched | `accounts/apac-tal.csv` |
| **Efun** | efun.com | China | ~$100M est. | TW/HK + SEA MMORPG publishing — closest overseas-publishing model | Not researched | `accounts/apac-tal.csv` |
| **Zulong** | zulong.com | China | ~$150M est. | Global MMORPG | Not researched | `accounts/apac-tal.csv` |

### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| **Asiasoft (PlayPark)** | playpark.com | Game publishing / portal | TH, SG, MY, ID, PH, VN | **In-house centralised 7-currency wallet (PlayMall)** — the same "build your own wallet to escape the stores" pattern as NEO Coins | `accounts/apac-tal.csv`, verified in-repo |
| **HAGO** | ihago.net | Social / casual gaming | SEA, global | **In-house group pay-center (`pay.ihago.net`) over ~30 providers** — the extreme version of Neocraft's architecture | `accounts/apac-tal.csv`, verified in-repo |
| **SEA Gamer Mall** | seagm.com | Game top-up marketplace | MY, SG, ID, VN, TH, KH | **Greenfield.** Also instructive as the *kind* of third-party top-up channel Neocraft's penalty policy exists to block | `accounts/apac-tal.csv`, verified in-repo |
| **Cygames** | cygames.co.jp | Mobile game dev/publisher | JP + global | **In-house: two PSPs joined by one `country_code` boolean, no failover or routing** — the precise failure mode to probe for at Neocraft | `accounts/apac-tal.csv`, verified in-repo |
| **Devsisters (Cookie Run)** | devsisters.com | Mobile game publisher | KR + global | **The counter-example.** Rejected to `not-icp/` on the app-store trap: Devsisters states in writing it does not process in-app purchases at all. **Neocraft is the opposite case and the contrast is the point** | `not-icp/devsisters-cookie-run.md` |
| **Koei Tecmo** | koeitecmo.co.jp | Game publisher / IP holder | JP + global | ~$600M FY24. **Neocraft's IP licensor for Dynasty Warriors: Overlords.** Already on the TAL, unresearched | `accounts/apac-tal.csv` + ixbt.games |
| **Gametion (Ludo King)** | gametion.com | Mobile F2P | IN + global | ~$50M est. F2P with web-top-up potential and India rails | `accounts/apac-tal.csv` |

### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| **Com2uS** | **PortOne** (regional orchestrator, inside Hive billing; Xsolla as global MoR) | Date of adoption not established | Mobile game publisher, Korea | `accounts/apac-tal.csv` → verified in `2-ready-to-outreach/com2us.md` against Com2uS's own newsroom: 「Hive 빌링의 PG 결제는 검증된 솔루션인 **포트원**과 **Xsolla** 페이먼트를 지원한다」 |
| **Webzen** | **PortOne** on the Korean mobile estate (in-house Wcoin layer on the global portal) | Date not established | Mobile/PC game publisher, Korea | `accounts/apac-tal.csv` → verified in `2-ready-to-outreach/webzen.md` |
| **Zupee** | **Juspay** | Date not established | Mobile skill gaming, India | `accounts/apac-tal.csv` (TAL row — **not independently verified in this run**) |

**No public case study was found of a direct competitor adopting a *global* orchestrator.** The confirmed adoptions are of **PortOne**, a Korean regional orchestrator — which matters for Neocraft because the account's #1 market is Korea, and a Korean publisher peer group that is already orchestration-aware shortens the education cycle considerably. ⚠️ **These are in-repo findings from prior research runs, not public URLs I retrieved in this run.** Treat the Zupee row as a lead.

### 11D. Prospect Scoring

Applied to the three best-evidenced peers above. Only signals with evidence in this repo or in this run.

**Gravity (gravity.co.kr)**

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| Monthly transaction count | ⬜ 0 | Not established in this run | — |
| Orchestration status | **+4** | ✅ Greenfield — zero orchestrator hits across the 20-F and every property retrieved | `2-ready-to-outreach/gravity.md` |
| 3+ countries | **+3** | ✅ Eleven markets | " |
| Multiple PSPs | **+3** | ✅ **Twelve** named providers | " |
| Local rail / licensing gap in a top-3 market | ⬜ 0 | Not re-assessed here | " |
| Recent expansion | ⬜ 0 | Not re-assessed | — |
| Payment issues | ⬜ 0 | Not re-assessed | — |
| Funding >$10M | ❌ 0 | Listed company, no round | " |
| High traffic outside home | **+2** | ✅ Heavily non-Korean revenue | " |
| Competitor using orchestration | **+2** | ✅ Com2uS → PortOne | `2-ready-to-outreach/com2us.md` |
| Payment job postings | ⬜ 0 | Not established | — |
| **Subtotal (signals assessed)** | **14** | Already in `2-ready-to-outreach/` — scored in its own file | — |

**Koei Tecmo (koeitecmo.co.jp)** — ⬜ **unscored.** Not researched. ~$600M FY24, Japan, on the TAL, and now a *known commercial counterparty of Neocraft*. That licensing relationship is a warm-intro path, and it is the single most actionable unresearched row this run surfaced.

**SpinX Games (spinxgames.com)** — ⬜ **unscored.** Not researched. ~$1B est., **Hong Kong**, global mobile. Nearest HK-domiciled gaming peer by both geography and model.

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | **Gravity** | Direct competitor | KR, TW/HK, SEA, LatAm, US | 14+ (partial) | ⭐ | Greenfield + 12 named PSPs across 11 markets | ✅ — already in `2-ready-to-outreach/` |
| 2 | **Koei Tecmo** | IP licensor / peer | JP + global | ⬜ | 🟢 | ~$600M FY24, unresearched, **commercial counterparty of this account** | ✅ |
| 3 | **SpinX Games** | Peer | Global mobile | ⬜ | 🟢 | ~$1B est., **Hong Kong-domiciled** — closest geographic peer | ✅ |
| 4 | **Efun** | Direct competitor | TW/HK, SEA | ⬜ | 🟢 | Closest match on the overseas-publishing model | ✅ |
| 5 | **Gamania** | Direct competitor | TW, HK, JP, KR, SEA | ⬜ | 🟢 | Taiwan portal publisher, unresearched | ✅ |
| 6 | **IGG** | Peer | Global F2P | ⬜ | 🟢 | ~$750M FY24, Singapore | ✅ |
| 7 | **Zulong** | Direct competitor | Global MMORPG | ⬜ | 🔵 | ~$150M est. | ✅ |
| 8 | **Asiasoft (PlayPark)** | Peer | TH, SEA | — | — | In-house PlayMall wallet — same architecture | ✅ — already in `2-ready-to-outreach/` |
| 9 | **Webzen** | Peer | KR + global | — | — | In-house Wcoin + PortOne incumbent | ✅ — already in `2-ready-to-outreach/` |
| 10 | **Com2uS** | Peer | KR + global | — | — | PortOne displacement | ✅ — already in `2-ready-to-outreach/` |

**Every company above is already on `accounts/apac-tal.csv`.** No genuine net-new find — which is expected, since gaming is the largest industry on the list (139 of 1,219 rows). **The real find is a relationship, not a company:** Koei Tecmo licenses IP to Neocraft and sits unresearched on the TAL at ~$600M.

---

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | **No public figure.** Private Hong Kong company; `Est. Revenue (USD)` is empty for both TAL rows; no filing, no funding disclosure, no credible third-party estimate | ⚠️ Sensor Tower blog pages giving per-country weekly revenue for Tales of Wind and Guardians of Cloudia **were found and deliberately not used** — they are per-country, per-quarter, and credited to *"Timothy, Your Friendly Neighborhood AI."* Not a usable source |
| GMV / Gross Transaction Volume | **No public figure** | — |
| Average Transaction Value (USD) | **`[ASSUMPTION — not researched]` ~$10–30 on the web rail.** Basis: published NEO Coins tiers are $1, $2, $5, $8, $10, $20, $100, $300, $500 with a free-entry custom field, a **USD $1,000 single-recharge maximum** and a $500 slider cap; direct game recharge sells Monthly Cards and Battle Passes at typical F2P price points | [FAQ](https://www.neocraftstudio.com/en/faq-list) + [`/pay/index`](https://accounts.neocraftstudio.com/pay/index) for the **tiers**; the AOV itself is unsourced |
| Est. Annual Transactions | **Cannot be derived.** Both inputs (revenue and ATV) are unsourced, so any product of them is an assumption, not a derivation | Per the disclosure rule: *"Never present a derivation as a measurement"* |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ~5,000–12,000 web recharge orders/month.** `[ASSUMPTION — not researched.]` **Basis:** 153,134 total visits to `neocraftstudio.com` in Sep 2026 (**SOURCED** — SimilarWeb supplied 2026-10-09) × an assumed **3–8%** visit-to-paid-order rate (**UNSOURCED**). 3% → ~4,594; 8% → ~12,251. Even an aggressive 20% yields only ~30,627, so the web channel is very likely **below the 40,000/month floor**. **Reasoning behind the 3–8% band:** the domain's only commerce function is recharge and the games are acquired from app stores, so visits are high-intent — but the same domain also absorbs marketing, news, FAQ, account recovery and login traffic, and 73.08% of it is mobile web where the three-step Role-ID flow is heaviest. **Because the conversion input is unsourced, the whole figure is an assumption and it has NOT been allowed to trigger the under-40,000 rejection.** <br><br>**Billing unit, stated explicitly:** *paid orders where NEOCRAFT Limited is merchant of record* — NEO Coins wallet top-ups and direct per-character game recharges on `accounts.neocraftstudio.com`. **Apple App Store, Google Play and Huawei AppGallery in-app purchases are excluded and are not in this number.** Those are the stores' transactions, not Neocraft's; they never appear in the merchant's own transaction count and no orchestrator can route, retry or locally acquire a single one of them | See the disclosure rule in the ICP matrix |
| Active Customers / Users | **~93.35 million cumulative "Users", self-reported and undated** — Tales of Wind 67M, Tree of Savior: NEO 9.5M, Guardians of Cloudia 7M, Chronicle of Infinity 3.7M, Spirits of Aetheria 2.5M, Immortal Awakening 2.5M, The Dragon Odyssey 1.1M, Dynasty Warriors: Overlords XL 0.05M. The About page claims **100,000,000 Players** and **150,000 Daily Active**. 🛑 **These are cumulative registrations and an undated DAU claim. They are NOT transactions and must never be fed into a transaction count** — the About text still references Tales of Wind's 2019 launch and Guardians of Cloudia's 2021 launch, so the DAU figure is of unknown vintage | [Games page](https://www.neocraftstudio.com/en/games.html) · [About](https://www.neocraftstudio.com/en/about) |
| App Store ratings (volume proxy only) | **12,958 US ratings** across 8 games; Chronicle of Infinity alone has 5,371 US and 344 KR; クロニクル・オブ・インフィニティ has 1,564 JP | [iTunes lookup API](https://itunes.apple.com/lookup?id=1369685711&country=us) — a reach proxy, **not** a transaction proxy |
| Primary Currency | **USD only.** `USD $1 = 1 NEO Coin`; every tier and the confirmation template are USD. No local-currency pricing in any market | [FAQ](https://www.neocraftstudio.com/en/faq-list) · [`/pay/index`](https://accounts.neocraftstudio.com/pay/index) |
| Top 3 Markets by Revenue | **Unknown.** By *web traffic*: Korea 14.91%, Russia 10.43%, Turkey 8.75%. Revenue mix is not published and web traffic is a poor proxy for it in F2P, where spend concentrates in a small whale cohort | SimilarWeb (supplied 2026-10-09) |
| **Billing channel split (web vs app store)** | 🛑 **NOT FOUND — no public source states it.** Both channels are confirmed to exist: app-store IAP across **three** stores (Apple, Google Play, Huawei AppGallery) and a merchant-of-record web channel (NEO Coins + direct recharge). `[INFERENCE, not confirmed]` IAP is probably still the majority, as it is for mobile F2P generally. **The direction of travel is the only thing evidenced, and it favours web:** a standing "up to 10% off" recharge discount, an extra in-game rebate for paying with NEO Coins, periodic "tax reduction" promotions, a 1:100 bonus-points accrual, and a published policy of **banning players** who top up anywhere but Neocraft's own store. A merchant does not build and defend that if the web rail is a rounding error — but **"it is being pushed hard" is not the same as "it is large", and nothing I found closes that gap** | FAQ, homepage, announcement, Apple/Google/Huawei listings — all cited above |

> *"No public revenue or GMV data found. **Business case sizing requires a discovery call**, and specifically requires one number: monthly paid orders on `accounts.neocraftstudio.com`. Everything else in the account is well evidenced; this single figure decides whether it is a prospect."*

---

## Overall Research Confidence

**Medium-High.**

**Unusually strong coverage, because the merchant's own payment infrastructure was reachable and interrogable:**
- **Section 3 (payment stack architecture)** — exceptional. The channel catalogue, fee table, tax engine, wallet mechanics, order states and card-field markup all came from the merchant's own live API and page source, not from inference. 43 country codes queried directly.
- **Section 4 (payment methods)** — exceptional and rare. 97 channels enumerated from the merchant's own endpoint rather than guessed at. Absences in Japan, India and Taiwan are *sourced absences*, which is far stronger than "not found".
- **Section 8 (checkout audit)** — strong for everything up to the gateway redirect.
- **The identity question** — settled conclusively on RDAP, DNS and HTTP evidence. One company; `neocraft.net` is a parked, expired-nameserver shell.
- **The app-store question** — settled on the merchant's own FAQ, verbatim.
- **Section 5 (complaints)** — strong *negative*, from ~300 primary App Store reviews across nine apps in two storefronts rather than from a search summary.

**Three material weaknesses, all named:**
1. **No PSP, acquirer or aggregator could be identified.** Section 3A is a confirmed-blank rather than a finding. Everything checked is listed so the negative can be weighed, but it is a hole, and it is closeable in one authenticated checkout walkthrough.
2. **No financials of any kind, and therefore no sourced transaction count.** The monthly figure is explicitly an assumption and is labelled as such everywhere it appears. The web-vs-IAP split — the number that actually sizes this account — is unpublished.
3. **No corporate registry record.** ICRIS was unreachable and OpenCorporates required a token, so the CR number, directors and the "EMA Groups" affiliation are all open.

**Traffic data was SUPPLIED, not estimated** — Prateek's SimilarWeb PRO pull for Sep 2026, used verbatim and not re-researched, which is the strongest of the three resolution paths and means the country profile driving Section 4 and two ICP signals is sound. **One caveat carried from the source file: it is a top-10 cut, not a full country list, so the 17.37% APAC figure is a visible floor** — and notably, Japan, Hong Kong and SEA all sit below that cut despite being deliberately localised markets.

**Network access was available and was not a limiter.** WebFetch was not needed — Bash `curl` worked throughout, including for the merchant's own POST APIs. No egress block was encountered on any host attempted. No confidence downgrade on that account.

⚠️ **Method deviation, disclosed:** `research.md` Phase 2 calls for Agents 2–5 to run in parallel. **No subagent/Task tool exists in this environment** (`ToolSearch` returns no agent-spawning tool), so Phases 1–3 were executed single-threaded by me. Search and fetch budgets were therefore pooled rather than per-agent. This did not reduce coverage — the account's answers were in the merchant's own infrastructure rather than in search results — but it is a departure from the written method and is recorded here.

⚠️ **Two WebSearch summary claims were tested against the underlying pages and found false** (CB Insights/Mong Kok; VNG Games/Dynasty Warriors). Both were dropped. This is the documented WebSearch-summary failure mode firing twice in a single run, and it is the reason every claim in this report carries a URL.

---

## Manual Research Recommendations

> **Area:** **Monthly paid-order count on the web channel** — Section 12, the only ASSUMED figure in the report and the only one that can reject the account.
> **Why it matters:** This is the volume gate. 153k monthly visits on the one transacting domain implies something on the order of 5,000–12,000 orders/month, which is well under the 40,000 floor. It is an assumption, so it has not rejected the account — but if a sourced number confirms it, this file moves to `not-icp/` and the report above becomes the rationale. Everything else is well evidenced; this single figure decides the account.
> **Suggested manual action:** Ask it directly on the first call, in the merchant's own vocabulary: *"How many recharge orders a month go through the website versus the app stores?"* The named contact — **Yihan Lai, yihan@neocraftstudio.com, "localization and payment service"** — will know, and the question is a natural one to ask someone whose title pairs those two things.

> **Area:** **The PSP / acquirer identity** — Section 3A, confirmed blank.
> **Why it matters:** Without it there is no displacement target, no incumbent to position against, no read on whether failover exists, and no way to judge whether the "Channel service fee" reflects an aggregator's rate card or direct acquiring. It also decides whether the PCI story is SAQ A-EP or full scope.
> **Suggested manual action:** **Register a player account on `accounts.neocraftstudio.com`, pick the $1 NEO Coins tier, and walk the checkout to the gateway with DevTools open.** The `POST /payment/default/deal-with-v3` response and the subsequent redirect will name the provider in a single step. This one action closes Sections 3A, 8 and 9 simultaneously and is the highest-value manual task on the account.

> **Area:** **Web vs app-store revenue split** — Section 12, unpublished.
> **Why it matters:** It is the business case. Yuno's addressable share of this merchant is exactly the web number and nothing else. The pull incentives prove intent; they do not prove size.
> **Suggested manual action:** Second discovery question, immediately after the order count. Frame it on their own incentive: *"You're discounting web top-ups up to 10% and giving an extra in-game rebate on NEO Coins — what share of spend has that actually moved off the stores?"*

> **Area:** **Corporate identity — CR number, directors, and the "EMA Groups" affiliation** — Section 2.
> **Why it matters:** The Google Play namespace is `com.emagroups.*`, the recharge page loads from `static.emagames.cn`, and the site sets `EMASITEID` cookies — but no source explains what EMA is. If Neocraft Limited is the Hong Kong publishing arm of a larger mainland group, both the decision-making unit and the addressable volume are bigger than this file assumes. The privacy policy also asserts subsidiaries that are named nowhere.
> **Suggested manual action:** One ICRIS lookup at `icris.cr.gov.hk` for "NEOCRAFT LIMITED" returns the CR number, incorporation date, registered office and shareholders — which would likely settle EMA in the same search. Pair it with a LinkedIn check on `linkedin.com/company/neocraft-limited` for headcount and office locations.

> **Area:** **Japan — a deliberately served market with a rail gap** — Section 4.
> **Why it matters:** Neocraft runs two dedicated Japanese App Store titles under its own name (1,564 JP ratings on クロニクル・オブ・インフィニティ) and both are selectable in the web store, yet the Japan method set has no konbini, no PayPay, no LINE Pay, no Paidy and no carrier billing — while LINE Pay *is* configured in the catalogue and served to Thailand. This is the cleanest concrete rail gap on the account and it is in a market they chose. But Japan is below the supplied top-10 cut, so its size is unknown.
> **Suggested manual action:** Two things. (1) Get Japan's actual traffic share — re-pull SimilarWeb beyond the top 10, which would also give Hong Kong, Taiwan and SEA. (2) **Source a current konbini and PayPay usage citation before any of this goes in an email** — `apac-payments.md` flags the gap but is explicitly not a citable source, and I did not obtain one.

> **Area:** **Korea — whether the local-entity question is a real acquiring constraint** — Section 2.
> **Why it matters:** Korea is 14.91% of traffic with no Korean entity, which looks like the territory's classic regulatory gate. But the live checkout serves Credit Cards Korea, Bank Transfer Korea, Kakao Pay, Toss Pay, Naver Pay and Payco — so domestic rails are demonstrably being reached, presumably through a licensed local partner. I scored this row ❌ rather than claim a gate I could not source, and an incorrect gate claim in an email would be immediately refutable by the prospect.
> **Suggested manual action:** Find a current primary source on Korean domestic card acquiring requirements for foreign merchants (Financial Supervisory Service / Bank of Korea), **or** simply ask on the call who acquires their Korean card volume. The 4.50% Visa vs 3.50% Credit Cards Korea spread is a safe, fully sourced opener either way and does not depend on the regulatory question at all.

---

## Appendix: All Source URLs

**Merchant's own estate (primary, all retrieved 2026-10-09)**
- https://www.neocraftstudio.com/ — homepage; Recharge nav; "Recharge Discounts — Enjoy Up to 10% Off Discount Now!"
- https://www.neocraftstudio.com/en/about — founded 2018, 100+ staff / 7 countries, 100,000,000 players, 150,000 DAU, language list
- https://www.neocraftstudio.com/en/contact — **NEOCRAFT Limited**, Wanchai registered address, **Yihan Lai "localization and payment service"**
- https://www.neocraftstudio.com/en/faq-list — **NEO Coins**: web-only acquisition, App Store/Google Play post-2024-01-01 redemption, $1,000 ceiling, $1–$500 tiers, rebate, tax-reduction promos, non-refundable, 1:100 points
- https://www.neocraftstudio.com/en/terms — Neocraft Limited as contracting party; virtual currency final-sale / no-refund clause
- https://www.neocraftstudio.com/en/privacy — NEOCRAFT LIMITED "and all of its subsidiaries"; *"Typical credit card information… and security code"*; *"Data from your payment service provider"*
- https://www.neocraftstudio.com/announcement?language=en — **Unauthorized 3rd-party Top-up Penalty Policy**
- https://www.neocraftstudio.com/en/games.html — eight titles with cumulative user counts
- https://www.neocraftstudio.com/en/news.html — launch timeline; page title "NEOCRAFT, NEOCRAFT STUDIO"
- https://accounts.neocraftstudio.com/pay/index — NEO Coins top-up; native card fields; method tiles with hidden `fee` inputs; "Channel service fee" JS
- https://accounts.neocraftstudio.com/payment/default — direct game recharge; 3-step flow; subscription products; commented-out penalty-policy banner
- https://accounts.neocraftstudio.com/payment/default/get-manner-list — **the channel catalogue API** (`POST code=<ISO2>&op_id=2109`), 43 countries queried, 97 channels enumerated
- https://accounts.neocraftstudio.com/payment/default/get-tax-fee-info · /get-role-info · /check-role · /select-game · /deal-with-v3 — merchant payment endpoints
- https://accounts.neocraftstudio.com/pay/get-manner-list · /pay/get-tax-fee-info · /pay/deal-with-coin — wallet endpoints (login-gated)
- https://static.neocraftstudio.com/static/accounts/js/recharge3.js · /static/accounts/v3/js/common.js — checkout scripts (no external vendor hosts)

**Domain and entity evidence**
- https://rdap.verisign.com/com/v1/domain/neocraftstudio.com — created **2018-09-12**, AWS DNS, GoDaddy, four registrar locks
- https://rdap.verisign.com/net/v1/domain/neocraft.net — created **2025-09-24**, **`NS1-DOMAIN-EXPIRED.MYHOSTADMIN.NET`**, Xiamen 35.com
- https://www.cbinsights.com/company/neocraft — ⚠️ **a different company** (Israeli furniture label, `neocraft.com`). Cited here to document the false lead

**App store evidence**
- https://apps.apple.com/us/developer/neocraft-limited/id1367784951 — nine apps, `NEOCRAFT LIMITED`
- https://itunes.apple.com/lookup?id=1369685711,1544039144,1631994340,1639263307,6503807938,6739037696,6742529924,6754444931,6757413794&country=us — release dates, languages, ratings, sellerName
- https://itunes.apple.com/lookup?id=...&country=kr (and jp, hk, tw, au, sg, id, th, ph, my, vn, br, tr, ru, gb, es, bg, sa) — per-market availability and localised titles
- https://itunes.apple.com/search?term=クロニクル・オブ・インフィニティ&country=jp&entity=software — Japan-specific listings id 6450688247 (1,564 JP ratings) and id 6458103025, both `NEOCRAFT LIMITED`
- https://itunes.apple.com/us/rss/customerreviews/page=1/id={1369685711,1544039144,1631994340,1639263307,6503807938,6739037696,6742529924,6754444931,6757413794}/sortby=mostrecent/json and the `/kr/` equivalents — ~300 reviews, Section 5
- https://play.google.com/store/apps/dev?id=5566381355836435401&hl=en_US&gl=US — **`com.emagroups.*`** package namespace

**Press and third party**
- https://www.prnewswire.com/il/news-releases/huawei-appgallery-invites-you-to-dive-into-award-winning-tree-of-savior-neo--live-demos--exclusive-events-await-at-gamescom-2025-302536691.html — Huawei AppGallery, 2025 Mobile Gamer Awards, Gamescom 2025 (22 Aug 2025)
- https://ixbt.games/en/news/2026/07/31/425853-klassika-musou-v-karmane-na-ios-i-android-sostoialsia-vnezapnyi-reliz-dynasty-warriors-overlords.html — NEOCRAFT LIMITED released Dynasty Warriors: Overlords 30 Jul 2026, Koei Tecmo licensed
- https://onemoregame.ph/2022/08/dynasty-warriors-overlords-predownload-philippines/ — ⚠️ **a different, 2022 game** published in SEA by VNG Games. Cited to document the false lead
- https://apps.apple.com/mm/app/%E7%9C%9F-%E4%B8%89%E5%9C%8B%E7%84%A1%E9%9B%99%E9%9C%B8/id1590111763 — the 2022 title, `SuperNova Overseas Limited`. Name collision, not the same product

**Internal repo sources (not public URLs)**
- `accounts/apac-tal.csv` — both Neocraft rows (`Payment Gateway`, `Payment Orchestrator`, `Est. Revenue (USD)` all empty); 139 gaming rows; NetEase marked `EXISTING YUNO MERCHANT`; Garena marked `In-house Routing`
- `accounts/traffic/neocraft.md` — **SimilarWeb (supplied 2026-10-09)**, Sep 2026
- `2-ready-to-outreach/com2us.md` — PortOne orchestration seat, verified against Com2uS newsroom
- `2-ready-to-outreach/gravity.md` — greenfield, twelve named providers across eleven markets
- `2-ready-to-outreach/webzen.md` — in-house Wcoin wallet over a hand-wired tile wall; PortOne on Korean mobile
- `not-icp/devsisters-cookie-run.md` — the app-store-trap rejection precedent this account does **not** match
- `.claude/reference/apac-payments.md` · `.claude/reference/subscription-payments.md` — checklists, cited as framing only, never as sources

</details>
