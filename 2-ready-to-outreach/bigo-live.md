# BIGO Live

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 14 / 29 → 🟢 **Medium** — on arithmetic, no override applied. The account is far larger than the score suggests; see the breakdown for why the score stays as it is.
**Industry:** Live streaming / virtual gifting (social entertainment) · **HQ:** **BIGO TECHNOLOGY PTE. LTD.**, 30 Pasir Panjang Road #15-31A, Mapletree Business City, Singapore 117440 · parent **JOYY Inc. (NASDAQ: YY)** · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **In-house orchestration.** BIGO built its own payment platform, branded "BIGO LIVE Pay". It serves a per-country channel tree from its own backend across roughly 20 processors. Never pitch "you need orchestration." Anchor on **processor sprawl, maintenance burden and the growing off-store share**.

---

> # 🔒 PHASE 0 — QUALIFICATION GATE
>
> | Rule | Result |
> |---|---|
> | PSP / gateway / acquirer / orchestrator | **Does not fire.** "BIGO LIVE Pay" is BIGO's *own* recharge checkout for its own virtual currency. It does not process payments for third parties. JOYY's FY2025 20-F describes JOYY as a **payer**: *"we sell almost all of our products and services to our users through third-party online payment systems"* ([20-F](https://www.sec.gov/Archives/edgar/data/1530238/000110465926049917/joyy-20251231x20f.htm)). ⚠️ The caveat carried from the HAGO report still applies at group level: JOYY's sibling segment **Shopline** runs "Shopline Payments" for its merchants. That is a different segment, not BIGO. |
> | Existing Yuno customer | **No.** `https://y.uno/en` fetched 2026-10-19: zero occurrences of "bigo", "joyy" or "likee". |
> | No online payment volume | Does not fire. Live streaming revenue was US$402.6M in Q2 2026 alone ([Q2 2026 release](https://www.sec.gov/Archives/edgar/data/1530238/000110465926101098/tm2624081d1_ex99-1.htm)). |
> | HQ west of Dubai | Does not fire. The Singapore entity is the App Store seller of record ([iTunes lookup](https://itunes.apple.com/lookup?id=1077137248&country=us)). |
> | Monthly transactions < 40,000 (sourced) | **Does not fire.** No sourced count exists. The derived range is ~67k–5.7M per month for **off-store web recharges alone**, and even the harsh case clears the floor. Every scenario rests on assumed inputs. See Section 12. |

> # 🚨 READ THIS FIRST — three things that will burn the thread if missed
>
> 1. **HAGO is the same parent, and is already ⭐ in this folder** (`2-ready-to-outreach/hago.md`, 19/29). Same JOYY group, same Singapore head-office address. **Do not sequence BIGO and HAGO independently.** Decide one JOYY account plan and one entry point first.
> 2. **BIGO does NOT run on the HAGO/JOYY pay-center.** I checked BIGO's production bundles myself. These strings return zero hits: `ihago`, `pay-center`, `charge_currency`, `yuno`. BIGO has its own stack (`/pay-bigolive-flow/*`, assets on `static-pay.bdesk.tech`). **JOYY therefore runs at least two parallel in-house payment platforms**, a fact neither report establishes on its own. Do not assume a HAGO conversation reaches BIGO's payments team, or the reverse.
> 3. **The "Yuno" trap.** JOYY operates a social app literally called **Yuno** (`yunoliveapp.com`, `com.joyy.yuno`; see hago.md). Any internal grep of JOYY code that "finds Yuno" is finding their app, not us. It returns zero hits in BIGO's bundles.

> # ⚠️ METHOD NOTES — disclosed up front
>
> 1. **Traffic was supplied** (`accounts/traffic/bigo-live.md`, Similarweb **Sales Intelligence**, pulled 2026-10-19, Jul–Sep 2026, bigo.tv + bigo.sg). Its caveats are carried through this report:
>    - **(a)** Only the top 10 countries per domain are shown, as share only. Per-country visits below are `[DERIVED from supplied share, not a SimilarWeb figure]`.
>    - **(b)** Shares are single-domain, so I combined them visits-first (share × domain avg monthly visits), never by averaging percentages. A country in only one domain's top 10 is a **lower bound**: its share on the other domain is unknown, below that domain's #10.
>    - **(c)** **Mobile app traffic is excluded.**
>    - **(d)** **BIGO is app-first.** Most diamond recharges happen in the app, via app-store billing or resellers. **Web traffic is a market-mix signal only.** I did NOT use it to size transactions or the 40k gate.
>    - **(e)** Global rank was not captured.
> 2. **Fetch worked.** WebFetch was not used; Bash curl and headless Chromium both reached bigo.tv, the BIGO pay APIs, SEC EDGAR and Codashop. All five research agents ran in parallel, because the supplied traffic already fixed the market list.
> 3. **The strongest evidence in this report is BIGO's own public channel-tree API**, which needs no login: `mobile.bigo.tv/pay-bigolive-flow/live/quickPay/getChannelTree?country={CC}&apk=official&platform=ios_outside&isFromApp=0`. It was pulled for 13 countries. Each channel carries an `id_name` of the form `processor-method`. **I re-pulled ID and KR myself** and the processor lists match. `platform=ios_outside` means the **web, off-store** checkout. In-app IAP is not in this data.
> 4. **Two prefixes hide the processor:** `route_*` and `local_*`. These cover DANA, GoPay, OVO, PromptPay, GCash, Maya, FPX, DuitNow and TnG. The processor behind them is **unknown**, not "direct".
> 5. **Channel "maintenance" tips are not outage evidence.** Several channels carry text such as *"This channel is temporarily unavailable due to system maintenance"* (GCash, PH). But the generic tip appears even on US channels, one tip refers to a past window ("9.22 3:30am to 11:30am"), and the agent read `channel_is_maintained=0` / `run_status=1` on the channels it inspected. **Treat these as stale display text. Do not use them as an outage claim.**

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** BIGO Live is JOYY's global live-streaming app. Viewers buy "diamonds" (virtual currency) to send gifts to hosts. It is available in 23 languages and ~150 countries and is JOYY's core revenue engine: Social Entertainment (Bigo Live, Likee, imo) earned US$422.7M of JOYY's US$590.8M Q2 2026 revenue. BIGO sells diamonds in-app via Apple/Google, through a reseller network, and through its own off-store web checkout, **"BIGO LIVE Pay"**. That checkout carries the banner *"save at least 25%"* and runs on a hand-built, multi-processor stack.

**SimilarWeb total visits (last full month):** **~1.94M / month** (Jul–Sep 2026 average: bigo.tv 1.818M + bigo.sg 0.124M) — **supplied** 2026-10-19. This is web only; the app, where most spend happens, is excluded.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods (first-party web checkout) | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇺🇸 United States | 24.4% (~474k/mo) | Cards ("Dinopay", US-issued V/MC/Amex/Discover/Diners), Apple Pay (Stripe), Google Pay (Onerway), PayPal (via "Ocean Universe"), Cash App (Coda), Lightning (Strike), stablecoin (Stripe) | None of note found. *(Outside the APAC reference.)* | ⚠️ Los Angeles operating presence reported (search summary only); no US entity named |
| 2 | 🇳🇬 Nigeria | 8.1% (~157k/mo) | Card & bank transfer (dLocal); PalmPay wallet, bank transfer, Verve card (PalmPay) | Not assessed (outside the APAC reference) | ❌ None found |
| 3 | 🇮🇩 Indonesia | 7.0% (~136k/mo) | QRIS, ShopeePay (iPay88); DANA, ATM/VA (`local_`); GoPay, OVO, Alfamart (`route_`); Telkomsel, XL, DOKU Wallet (Coda); MOL vouchers / Easy2Pay | **Indomaret, LinkAja, Indosat/Tri/Smartfren carrier billing** not in first-party checkout (all available via Codashop). The dominant rails (QRIS, VA, wallets) **are** covered. | ⚠️ PT Bigo Technology Indonesia, named in Kominfo coverage (news only, not checked on AHU) |
| 4 | 🇷🇺 Russia | 5.8% (~112k/mo) | SBP (`local_transfer_ru`), bank cards (`pmmax_pci`, `lapay`) | Not assessed (outside the APAC reference) | ❌ None found |
| 5 | 🇹🇭 Thailand | 4.3% (~84k/mo) | PromptPay, TrueMoney, internet banking (`route_`); TrueMoney (also via MOL); ShopeePay (Ksher); AIS/TrueMove/dtac carrier and Razer PIN (MOL); bank & counter payment (Coda) | **Cards** not found in TH first-party checkout; Rabbit LINE Pay and named 7-Eleven not found (both on Codashop) | ❌ None found |

**APAC markets in the top 10:** Indonesia #3, Thailand #5, Philippines #6 (3.5%), South Korea #7 (3.2%), Malaysia #9 (2.4%). Singapore, the HQ, is 0.3% (bigo.sg only).

### Legal entities
- **BIGO TECHNOLOGY PTE. LTD.** (Singapore) — operator, Apple seller of record; UEN not found; JOYY acquired it on 2019-03-04 (20-F note 1(c))
- **Bigo Inc.** (Cayman Islands) — investment holding (20-F)
- **Bigo (Hong Kong) Limited** (Hong Kong) — investment holding (20-F)
- **Guangzhou BaiGuoYuan Information Technology Co., Ltd.** (PRC subsidiary) and **Guangzhou BaiGuoYuan Network Technology Co., Ltd.** (PRC VIE) (20-F)
- **Bigo Service India Private Limited** (India) — CIN U93000HR2018FTC072223 (aggregator only, not checked on MCA). BIGO is not monetising in India: the IN channel tree returns no payment methods.
- **PT Bigo Technology Indonesia** (Indonesia) — `[UNVERIFIED — news coverage only]`

### Known PSPs
**Live in BIGO's own web checkout** ([Checkout], from BIGO's channel-tree API):
- **Coda Payments** — US, ID, TH, PH, MY (carrier billing, OTC, Cash App)
- **MOL / Razer** — US, ID, TH, PH, MY (vouchers, Easy2Pay, Thai carriers)
- **iPay88** — ID (QRIS, ShopeePay), MY (Boost, GrabPay)
- **Stripe** — US (Apple Pay, stablecoin)
- **Onerway** — US (Google Pay)
- **Airwallex** — MY cards, KR PAYCO
- **Ksher** — TH (ShopeePay)
- **Paydibs** — PH (DragonPay)
- **dLocal** — NG, BR
- **PalmPay** — NG
- **Waffo** — BR
- **Payoneq** — KR (most methods)
- **Toss** — KR (card, Toss Pay)
- **SettleBank** — KR (virtual account)
- **Ant (Alipay+)** — KR (KakaoPay)
- **9Pay, VTCPay, ZaloPay** — VN
- **PayGuru, V5pay** — TR
- **Strike** — US (Lightning)
- **"Dinopay"** — US cards; legal entity unidentified
- **"Ocean Universe"** — US PayPal; described as "PayPal's authorized partner"
- **Atome** — MY (BNPL)

**In BIGO's code but not live in the countries queried** ([Source Code]):
- **Adyen** — scheme, AU scheme, konbini (econtext), Klarna, iDEAL, TWINT, EPS, Carte Bancaire, Troy
- **Checkout.com** (`cko-card`, `cko_v2-card`)
- **UniPin** — BD voucher
- **Zai** — PayID

**Payouts:**
- **Checkout.com + Visa Direct** — creator payouts in UK/IT/DE/CH/AT ([Press Release](https://www.checkout.com/newsroom/bigo-checkout-com-and-visa-join-forces-to-transform-the-content-creator-economy), 1 Nov 2023)

### Orchestration status
**In-house orchestration layer.**
- BIGO serves a server-side, per-country channel tree from its own backend (`/pay-bigolive-flow/live/quickPay/getChannelTree`).
- Every channel is keyed `processor-method`, and the **same method runs on different processors in different markets**. ShopeePay goes through iPay88 in ID, Ksher in TH and a direct ShopeePay integration in MY. TrueMoney in TH is wired twice (`route_truemoney` and `mol-truewallet`).
- Card acquiring is spread across Dinopay, Stripe, Onerway, Airwallex, Checkout.com, Adyen and Ocean.
- No third-party orchestrator appears: Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails and IXOPAY all return **0 hits** in BIGO's bundles (verified by me).

### Buying signals
- 🚀 **Off-store push is live and explicit.** BIGO LIVE Pay tells users to *"recharge diamonds and save at least 25%"* and that *"m.bigopay.tv is the only official BIGO LIVE diamond acquisition URL"* ([BIGO LIVE Pay](https://mobile.bigo.tv/live/bigolivepay/index.html?lang=en)). Every off-store dollar lands on the in-house stack.
- 📈 **Growth in developed markets.** *"Live streaming revenues in developed markets grew 11.8% year over year"* (Q2 2026). The developed bucket includes South Korea and Singapore ([Q2 2026 release](https://www.sec.gov/Archives/edgar/data/1530238/000110465926101098/tm2624081d1_ex99-1.htm)).
- 💳 **Payments named as a 2026 product priority.** *"AI-powered improvements to content distribution and **payment experience**"* (Q2 2026 release).
- ⚠️ **Audited store-distribution risk.** *"Bigo Live was temporarily removed from the Google Play Store and the iOS App Store in December 2024"* ([FY2025 20-F](https://www.sec.gov/Archives/edgar/data/1530238/000110465926049917/joyy-20251231x20f.htm)).
- 🤝 **Cocodp named BIGO's "first third-party U.S. top-up partner"** (Sep 2025) ([TechNode/PRNewswire](https://technode.global/prnasia/cocodp-becomes-bigo-lives-first-u-s-top-up-partner-bringing-seamless-local-payment-options/)). `[UNVERIFIED — search summary only]`

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach BIGO Live` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

⚠️ **Read before drafting:**
1. **Settle the JOYY account plan with HAGO first** (see banner).
2. **Motion is in-house, and the build is good.** It covers QRIS, PromptPay, DuitNow, FPX, GCash, Maya, KakaoPay, Toss, MoMo, ZaloPay, VietQR, Pix and SBP. **There is no glaring rail gap to lead with.** The opening is the **cost of maintaining ~20 processor integrations** as the off-store share grows, not a missing method.
3. **Do not claim payment failures.** First-hand complaint evidence of declines or double charges is thin (Section 5). Complaints are about price and scams.
4. **Do not quote a Bigo-only revenue, MAU or paying-user figure.** JOYY discloses none. Every metric covers Bigo Live + Likee + imo.
5. **Do not use the 6.4% "payment handling cost" ratio as proof of an off-store split** (Section 12).

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 14 / 29
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | **+5** | ⚠️ **NOT FOUND — ASSUMED ~1.9M/month off-store web recharges** (range ~67k–5.7M). `[ASSUMPTION — not researched.]` Only one input is sourced (Q2 2026 live streaming revenue, US$402.6M, three apps). The Bigo share, off-store share and average ticket are assumed. Even the harsh case clears 40k. See Section 12. **Confirm on the first call.** |
| Orchestration status | **+1** | ✅ **In-house layer**, stated on positive evidence: an own channel-tree backend, `processor-method` keys, the same method on different processors per market, and zero third-party orchestrator hits |
| 3+ countries | **+3** | ✅ 10+ countries above 1% web share (supplied Similarweb). BIGO's own channel tree shows distinct local stacks in 12 countries. |
| Multiple PSPs | **+3** | ✅ ~20 processors live in the first-party checkout (BIGO channel-tree API), plus Adyen and Checkout.com in code |
| Local rail or licensing gap in a top-3 market | **0** | ❌ **Not met.** The top 3 are US, Nigeria and Indonesia. Indonesia's dominant rails (QRIS, VA, GoPay, OVO, DANA, ShopeePay) are all live. Only secondary rails (Indomaret, LinkAja, some carriers) are absent. No regulatory acquiring gate is shown: an Indonesian entity is reported, though unverified. |
| Recent expansion | **0** | ⬜ No dated new-market launch in the last 12 months. Developed-market growth and a US top-up partner (summary only) are growth, not expansion. |
| Payment issues reported | **0** | ❌ Not met at moderate frequency. Payment *failure* complaints are isolated (Razer PIN load failures, one bonus-diamond complaint). Most complaints are about price, scams and bans. |
| Funding >$10M | **0** | ❌ NASDAQ-listed parent, no funding round |
| High traffic outside home | **+2** | ✅ Singapore is 0.3% of web traffic. JOYY's FY2025 revenue is 58.9% from "developed countries", 11.5% Middle East and 19.8% SEA & others. |
| Competitor using orchestration | **0** | ❌ No live-streaming or gifting competitor found on a third-party orchestrator. This is the fourth independent null result in this repo, after livu.md, azar.md and kuaishou.md. |
| Payment job postings | **0** | ⬜ None found |
| **TOTAL** | **14** | 🟢 **Medium** |

**Tier:** 🟢 Medium (10–16). **No RFP override** (no public payment RFP found). **No analyst override applied.**

Why I did not override:
- **Upward was considered and rejected.** On scale alone BIGO is one of the largest payment buyers in this territory: ~US$1.5B/yr of live streaming across the group, ~20 processors. But the matrix is right that **there is no rail gap and no pain signal to open on**, and in-house is the hardest motion. The size argues for treating BIGO as part of a **JOYY group plan with HAGO** (⭐), not for re-tiering BIGO alone.
- **Downward (app-store dominated) was considered and rejected.** The IAP vs off-store split is unknown. But BIGO actively steers users off-store with a 25% discount and runs a large first-party checkout in 12+ countries, so a material off-store perimeter clearly exists.

### Source Notes
- ✅ BIGO's own channel trees (13 countries) were pulled 2026-10-19; I re-verified ID and KR.
- ✅ The BIGO bundle strings (Adyen list, `cko` list, orchestrator zeros, no HAGO pay-center strings) were verified by me in the captured bundles.
- ✅ The FY2025 20-F and Q2 2026 release quotes were checked by me against the downloaded filings.
- ✅ The Checkout.com + Visa payout partnership was read on the Checkout.com newsroom.
- ⚠️ PT Bigo Technology Indonesia, Bigo Service India, TripleA crypto (2022), Cocodp (2025), the Turkey BTK block (Feb 2026) and the Kominfo warnings (2024) come from search summaries or news only.
- ⚠️ Codashop is a **reseller**: the PH page labels Coda "Official Distributor". Codashop methods are not BIGO's checkout.

### Success Case Alternatives
- **Garena / NetEase / Moon Active** — all appear in the customer logo set on `y.uno/en` (fetched 2026-10-19). They are **gaming and digital-goods merchants selling virtual currency across many markets**, the closest profile match to diamond top-ups. ⚠️ I verified the logos only, not any case-study metrics. Pull the internal case before citing numbers.
- **Rappi** — pattern match only for "one platform, many country-specific rails". The vertical is different; do not imply a gifting result.
- **Do not use** HAGO, LivU or Kwai as proof points. They are prospects with in-house stacks, not Yuno customers.

---

## Executive Summary

BIGO Live is JOYY's Singapore-based global live-streaming app. Users buy diamonds to gift hosts, and the app is JOYY's main revenue engine: Social Entertainment earned US$422.7M in Q2 2026. Outside the app stores, BIGO sells diamonds through **its own web checkout, "BIGO LIVE Pay"**, which advertises a 25% discount. That checkout runs on a **hand-built, in-house orchestration layer across ~20 processors**: Coda, MOL/Razer, iPay88, Stripe, Airwallex, dLocal, Payoneq, Toss, Ant and others, plus Adyen and Checkout.com in code. Coverage of dominant APAC rails is strong. The opportunity is not a missing rail. It is **consolidating a fragmented, per-market processor estate** in which the same method runs on three different processors in three countries, as the off-store share grows. **Motion: in-house displacement**, best run as one JOYY plan together with sister app HAGO, which runs a *separate* in-house pay-center.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** **Supplied** — Similarweb Sales Intelligence (supplied 2026-10-19), Jul–Sep 2026, desktop + mobile web, bigo.tv + bigo.sg. Combined visits-first.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | United States | 24.4% | ~474,200 `[DERIVED]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | Nigeria | 8.1% | ~157,300 `[DERIVED]` | Not supplied | same |
| 3 | Indonesia | 7.0% | ~135,500 `[DERIVED]` | Not supplied | same |
| 4 | Russia | 5.8% | ~112,000 `[DERIVED]` | Not supplied | same |
| 5 | Thailand | 4.3% | ~84,000 `[DERIVED]` | Not supplied | same |
| 6 | Philippines | 3.5% | ~67,600 `[DERIVED]` | Not supplied | same |
| 7 | South Korea | 3.2% | ~61,300 `[DERIVED]` | Not supplied | same |
| 8 | Brazil | 2.4% | ~46,700 `[DERIVED]` | Not supplied | same |
| 9 | Malaysia | 2.4% | ~46,000 `[DERIVED]` | Not supplied | same |
| 10 | Turkey | 2.2% | ~42,000 `[DERIVED]` | Not supplied | same |
| — | China | ≥0.8% (lower bound) | ≥16,100 | — | bigo.sg only (12.97% of bigo.sg) |
| — | Mexico | ≥0.8% (lower bound) | ≥15,500 | — | bigo.sg only |
| — | Singapore (HQ) | ≥0.3% | ≥6,200 | — | bigo.sg only |

Notes:
- **High priority (>5%):** US, Nigeria, Indonesia, Russia.
- **Top-10 markets with no confirmed local entity:** US, Nigeria, Russia, Thailand, Philippines, South Korea, Brazil, Malaysia, Turkey. Indonesia has one, unverified.
- **bigo.sg is not a consumer site.** Its root returns a page titled "BIGO TECHNOLOGY PTE. LTD." (activity page `act-15405`). Its traffic mix (China 13%, Mexico 12%) likely reflects corporate, partner or activity use and should not be read as consumer demand.
- **Device:** bigo.tv traffic is 73.7% mobile web.
- **Web traffic ≠ spend.** Revenue is app-led, and JOYY's revenue split is weighted to "developed countries" (58.9%). Treat this table as market mix only.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Singapore — 30 Pasir Panjang Road #15-31A, Mapletree Business City, Singapore 117440. This is JOYY's principal executive office on the 20-F cover and the BIGO developer address. BIGO was acquired by JOYY on 2019-03-04 (20-F note 1(c)). It is reportedly founded 2014 ([Preqin](https://www.preqin.com/data/profile/asset/bigo-technology-pte--ltd-/226738), summary only).

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Singapore | BIGO TECHNOLOGY PTE. LTD. | UEN not found | [FY2025 20-F](https://www.sec.gov/Archives/edgar/data/1530238/000110465926049917/joyy-20251231x20f.htm); [iTunes seller](https://itunes.apple.com/lookup?id=1077137248&country=us) |
| Singapore | Bigo Internet Information Pte. Ltd. | Not found | [FY2022 Ex. 8.1](https://www.sec.gov/Archives/edgar/data/1530238/000141057823000819/tmb-20221231xex8d1.htm) (search snippet, not fetched) |
| Cayman Islands | Bigo Inc. | N/A | FY2025 20-F |
| Hong Kong | Bigo (Hong Kong) Limited | Not found | FY2025 20-F |
| PRC | Guangzhou BaiGuoYuan Information Technology Co., Ltd. (sub); Guangzhou BaiGuoYuan Network Technology Co., Ltd. (VIE) | Not found | FY2025 20-F |
| India | Bigo Service India Private Limited | CIN U93000HR2018FTC072223 | [registrationwala](https://www.registrationwala.com/company/bigo-service-india-private-limited/U93000HR2018FTC072223) (aggregator, summary only) |
| Indonesia | PT Bigo Technology Indonesia | Not found | [Kontan](https://nasional.kontan.co.id/news/menkominfo-ancam-blokir-aplikasi-bigo-live-terkait-judi-online-dan-pornografi) `[UNVERIFIED — search summary only]` |

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| United States | ✅ #1 | ⚠️ Operating presence only (summary) | Not assessed | Low in practice. US cards go through a US card channel ("Dinopay", US-issued cards only). |
| Nigeria | ✅ #2 | ❌ | Not assessed (no current source) | Mitigated: local rails via dLocal and PalmPay |
| Indonesia | ✅ #3 | ⚠️ Reported, unverified | Not verified (no current source fetched) | Mitigated: local rails via iPay88, Coda and `local_`/`route_` channels |
| Russia | ✅ #4 | ❌ | Not assessed | Local SBP + card channels. Out of territory. |
| Thailand | ✅ #5 | ❌ | Not verified | Local rails via MOL, Ksher and `route_` |
| Philippines | ✅ #6 | ❌ | Not verified | Local rails via `local_`, Coda, Paydibs |
| South Korea | ✅ #7 | ❌ | Not verified for BIGO's case; APAC reference flags KR as a likely gate | **Handled through local PGs:** Payoneq, Toss and SettleBank carry most methods |
| Malaysia | ✅ #9 | ❌ | Not verified | Local FPX, DuitNow, TnG; MYR cards via Airwallex |

> *"Warning: Potential cross-border operation in Nigeria, Russia and Thailand (top-5 markets). No local entity found."* **However,** BIGO's own channel trees show **local-currency, local-rail collection in each of these markets** through local processors (dLocal/PalmPay, SBP, PromptPay/TrueMoney). The fee and approval-rate story from the template therefore applies weakly. The more defensible observation is the **number of processors needed to achieve that local coverage**.

> **Regulatory gate:** none confirmed. I fetched no current regulatory source for any market, so none is claimed.

> **MANUAL:** Pull ACRA BizFile+ for the BIGO Technology Pte. Ltd. UEN, and the FY2025 20-F Exhibit 8.1 for the full subsidiary list. Check the in-app T&Cs for the billing entity per market; bigo.tv's agreement pages are JavaScript-rendered and returned shells.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

**Source of `[Checkout]` rows:** BIGO's channel-tree API, `https://mobile.bigo.tv/pay-bigolive-flow/live/quickPay/getChannelTree?country={CC}&apk=official&platform=ios_outside&isFromApp=0`, fetched 2026-10-19. The processor is read from `id_name`.

| Country/Region | PSP/Acquirer | Evidence Type | Source URL / snippet |
|----------------|-------------|---------------|------------|
| US, ID, TH, PH, MY | **Coda Payments** | [Checkout] | `coda-cashapp`, `coda-telkomsel`, `coda-xl`, `coda-doku_wallet`, `coda-otc`, `coda-smart`, `coda-convenience_store`, `coda-celcom` |
| US, ID, TH, PH, MY | **MOL / Razer** | [Checkout] | `mol-molpoint_wallet`, `mol-zgold_molpoint`, `mol-easy2pay_global`, `mol-truewallet`, `mol-ais`, `mol-dtac`, `mol-truemove`, `mol-razerpin` |
| ID, MY | **iPay88** | [Checkout] | `ipay88_v2-qris`, `ipay88_v2-shopeepay`, `ipay88-boost_wallet`, `ipay88-grabpay` |
| TH | **Ksher** | [Checkout] | `ksher-airpay` (ShopeePay) |
| PH | **Paydibs** | [Checkout] | `paydibs-dragonpay` |
| MY | **ShopeePay (direct)** | [Checkout] | `shopeepay-wallet` |
| MY | **Atome** (BNPL) | [Checkout] | `atome-wallet` |
| MY, KR | **Airwallex** | [Checkout] | `airwallex_pci-card_v2` (MYR cards), `airwallex-payco` |
| KR | **Payoneq** | [Checkout] | `payoneq-naverpay`, `payoneq-credit`, `payoneq-virtual`, `payoneq-internet`, `payoneq-mobile_tmoney`, gift-card methods |
| KR | **Toss** | [Checkout] | `toss-card`, `local_toss-toss` |
| KR | **SettleBank** | [Checkout] | `settleBank-vbank` |
| KR | **Ant (Alipay+)** | [Checkout] | `antfinance-kakaopay` |
| KR | **Haipay** | [Checkout] | `haipay-samsungpay` |
| US | **Stripe** | [Checkout] [Source Code] | `stripe-applepay`, `stripe-stable_coin`; `stripe_pci-card`, `stripe-bank_payment` in bundle |
| US | **Onerway** | [Checkout] | `onerway-google_pay_us_v2` |
| US | **"Dinopay"** (entity unidentified) | [Checkout] | `card_payment_us-card_us`, *"We accept VISA, MASTERCARD, Diners Club, Discover, and American Express cards issued in the United States."* |
| US | **"Ocean Universe"** (PayPal partner) | [Checkout] | `outside_card_pay-oceanuniverse_paypal`, *"Payment & support services provided by PayPal's authorized partner: Ocean Universe"* |
| US | **Strike** | [Checkout] | `strike-wallet` (Lightning) |
| NG, BR | **dLocal** | [Checkout] | `dlocal-bank_transfer` (NG); BR cards |
| NG | **PalmPay** | [Checkout] | `palmpay-palmpay_wallet`, `palmpay-bank_card_ng` |
| BR | **Waffo** | [Checkout] | Mercado Pago, Boleto |
| VN | **9Pay, VTCPay, ZaloPay** | [Checkout] | VN channel tree |
| TR | **PayGuru, V5pay, Payoneer** | [Checkout] | TR channel tree |
| RU | **`pmmax_pci`, `lapay`** (providers unidentified) | [Checkout] | RU channel tree |
| Not live in queried countries | **Adyen** | [Source Code] | `static-pay.bdesk.tech/live/assets/bigolivepay/js/index.cd2f08.js`: `K=["ocean-creditCard","adyen-scheme","adyen-scheme_au","adyen-econtext_stores","adyen-klarna_paynow","adyen-ideal","adyen-twint","adyen-eps","adyen-cartebancaire","adyen-troy"]` |
| Not live in queried countries | **Checkout.com** (pay-in) | [Source Code] | `.../js/35.387861.js`: `a=["cko_v2-card","cko-card","stripe_pci-card","adyen_v3-scheme_ca","ocean_v2-creditcard_ca"]`. Reading "cko" as Checkout.com is `[INFERENCE, not confirmed]`. |
| UK, IT, DE, CH, AT (payouts) | **Checkout.com + Visa Direct** | [Press Release] | [Checkout.com newsroom, 1 Nov 2023](https://www.checkout.com/newsroom/bigo-checkout-com-and-visa-join-forces-to-transform-the-content-creator-economy): *"BIGO can now unlock global remittances for our content creators from a single integration."* |
| BD / AU (code) | **UniPin** / **Zai** | [Source Code] | `unipin-bd_unipin_voucher`, `zai-payId` |
| Not stated | **TripleA** (crypto) | [Third-Party Report] | [Fintech News SG](https://fintechnews.sg/66825/crypto/streaming-platform-bigo-live-partners-triplea-to-enable-users-to-pay-with-crypto/) `[UNVERIFIED — search summary only]` |

**Hidden processor:** `route_*` channels (ID GoPay/OVO/Alfamart; TH PromptPay/TrueMoney/iBank; MY TnG/DuitNow; BR PicPay; VN MoMo/VietQR) and `local_*` channels (ID DANA/ATM; PH GCash/Maya; MY FPX; BR Pix; RU SBP). The processor is unknown.

**Single-PSP dependency:** No. The opposite: high fragmentation.

#### 3B. Payment Orchestrator

**Classification: In-house orchestration layer.** Evidence type: [Checkout] + [Source Code].

1. **Own routing backend.** BIGO serves the channel tree from its own servers (`/pay-bigolive-flow/live/quickPay/getChannelTree`, `/pay-bigolive-flow/live/quickPay/payment/pay`). Methods are keyed `processor-method` per country.
2. **The same method runs on different processors by market.** ShopeePay goes through iPay88 (ID), Ksher (TH) and direct (MY). TrueMoney (TH) is wired twice. Cards run on 5+ acquirers by market.
3. **Endpoint switching per processor family** in the front end: `j=K.includes(m),P="/pay-bigolive-flow/live/quickPay/payment/pay",j&&(P="/live/quickPay/payment/pay")`, where K is the Ocean/Adyen list.
4. **An abstraction prefix (`route_`)** on major wallets suggests an internal routing layer that hides the processor. `[INFERENCE, not confirmed]`
5. **A separate stack from JOYY's HAGO pay-center.** Zero hits for `ihago`, `pay-center`, `charge_currency` in BIGO bundles.
6. **No third-party orchestrator.** Zero hits for Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY (verified by me). `apac-tal.csv` Payment Orchestrator column for BIGO Live: blank.

> In-house motion: argue **reach, maintenance cost and opportunity cost**, never "you need orchestration." BIGO has already built what an orchestrator does, per market. The question is what it costs to keep ~20 integrations current.

> **MANUAL:** Log in on web, trigger a recharge in ID/TH/PH with DevTools open, and capture which processor sits behind the `route_`/`local_` channels.

---

### Section 4: Alternative & Local Payment Methods

First-party = BIGO LIVE Pay web checkout (channel tree, `platform=ios_outside`). In-app methods (Apple/Google IAP) are not covered.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| 🇮🇩 ID | QRIS | Bank transfer / A2A (QR) | Active in checkout (iPay88) | Channel tree ID |
| 🇮🇩 ID | DANA, GoPay, OVO, ShopeePay, DOKU Wallet | Digital wallet | Active in checkout | Channel tree ID |
| 🇮🇩 ID | ATM / bank transfer (VA) | Bank transfer | Active in checkout | Channel tree ID |
| 🇮🇩 ID | Alfamart | Cash/voucher | Active in checkout | Channel tree ID |
| 🇮🇩 ID | Telkomsel, XL | Carrier billing | Active in checkout (Coda) | Channel tree ID |
| 🇮🇩 ID | Indomaret, LinkAja, Indosat/Tri/Smartfren | Cash / wallet / carrier | **Not found** first-party; available via **Codashop** reseller | [Codashop ID](https://www.codashop.com/id-id/bigo-live) |
| 🇹🇭 TH | PromptPay, internet banking | A2A | Active in checkout | Channel tree TH |
| 🇹🇭 TH | TrueMoney, ShopeePay | Digital wallet | Active in checkout | Channel tree TH |
| 🇹🇭 TH | AIS, TrueMove, dtac | Carrier billing | Active in checkout (MOL) | Channel tree TH |
| 🇹🇭 TH | Bank & counter payment | Cash/voucher | Active in checkout (Coda) | Channel tree TH |
| 🇹🇭 TH | Cards; Rabbit LINE Pay; 7-Eleven (named) | Cards / wallet / cash | **Not found** first-party; on Codashop | [Codashop TH](https://www.codashop.com/th-th/bigo-live) |
| 🇵🇭 PH | GCash, Maya | Digital wallet | Active in checkout | Channel tree PH |
| 🇵🇭 PH | DragonPay; convenience store | Bank / cash | Active in checkout | Channel tree PH |
| 🇵🇭 PH | Smart | Carrier billing | Active in checkout (Coda) | Channel tree PH |
| 🇵🇭 PH | GrabPay, Globe, cards | Wallet / carrier / cards | **Not found** first-party (GrabPay on Codashop) | [Codashop PH](https://www.codashop.com/en-ph/bigo-live) |
| 🇰🇷 KR | KakaoPay, Naver Pay, Toss Pay, Samsung Pay, PAYCO | Digital wallet | Active in checkout | Channel tree KR |
| 🇰🇷 KR | Domestic cards | Cards | Active in checkout (Toss, Payoneq) | Channel tree KR |
| 🇰🇷 KR | Virtual account, account transfer | Bank transfer | Active in checkout | Channel tree KR |
| 🇰🇷 KR | Culture Land and 5 other gift cards; T-money | Cash/voucher | Active in checkout | Channel tree KR |
| 🇰🇷 KR | Mobile carrier billing | Carrier billing | **Not found** first-party | Channel tree KR |
| 🇲🇾 MY | FPX, DuitNow | A2A | Active in checkout | Channel tree MY |
| 🇲🇾 MY | Touch 'n Go, ShopeePay, Boost, GrabPay | Digital wallet | Active in checkout | Channel tree MY |
| 🇲🇾 MY | Cards (MYR) | Cards | Active in checkout (Airwallex) | Channel tree MY |
| 🇲🇾 MY | Atome | BNPL | Active in checkout | Channel tree MY |
| 🇲🇾 MY | U Mobile, Digi, Celcom | Carrier billing | Active in checkout (Coda) | Channel tree MY |
| 🇲🇾 MY | Maxis, MAE | Carrier / wallet | **Not found** first-party; on Codashop | [Codashop MY](https://www.codashop.com/en-my/bigo-live) |
| 🇻🇳 VN | MoMo, ZaloPay, VietQR, bank transfer, domestic card, VTCPay | Mixed | Active in checkout | Channel tree VN |
| 🇮🇳 IN | — | — | **No payment channels.** Consistent with the June 2020 ban ([Campaign Asia](https://www.campaignasia.com/article/singapores-bigo-technology-awaits-clarity-after-being-hit-by-indian-app-ban/462136), summary only) | Channel tree IN |
| 🇵🇰 PK | MOL PIN only | Voucher | Active in checkout; **no local rails** (JazzCash/Easypaisa not found) | Channel tree PK |
| 🇺🇸 US | Cards, Apple Pay, Google Pay, PayPal, Cash App, Lightning, stablecoin | Mixed | Active in checkout | Channel tree US |
| Global (APAC trees) | Apple Pay / Google Pay / PayPal on web | Wallet | **Not found** outside the US tree | Channel trees |

**Gap call-outs** (prominence of the methods not independently sourced in this run, so framed as questions):
- *Korea:* carrier billing is absent from the web checkout. Worth asking whether it is deliberately in-app-only.
- *Thailand:* there is no card option on the TH web checkout. Rarely matters for a PromptPay-led market; low priority.
- *Pakistan:* only MOL PIN, no local wallet rails. Traffic is outside the top 10; flag only.

**Recurring rails:** not applicable. Diamonds are one-off top-ups.

**Price ladders (first-party, channel tree):**
- ID DANA: Rp5k = 14 diamonds … Rp1M = 2,940
- ID Telkomsel: ~45% fewer diamonds per rupiah than wallets (carrier take-rate visible in pricing)
- TH PromptPay: ฿50 = 75 … ฿150,000 = 242,647
- KR KakaoPay: ₩1k = 31 … ₩2M = 68,265
- US Apple Pay: $5.50 = 276 … $129.99 = 7,085

Tickets range from cents to five-figure USD equivalents.

> **MANUAL:** VPN-check the **in-app** recharge screen on Android in ID/TH/PH. Does the app offer anything beyond Google Play billing, and does it deep-link to BIGO LIVE Pay?

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Diamond / top-up price too high (not a failure) | App Store ID, TH | Moderate (3 of 100 sampled) | 2026-04 to 2026-10 | `itunes.apple.com/{id,th}/rss/customerreviews/page=1/id=1077137248/sortby=mostrecent/json` |
| Promo / bonus diamonds not credited | App Store PH | Isolated (1 of 50) | 2026-05-17 | `itunes.apple.com/ph/rss/customerreviews/...id=1077137248...` |
| Money lost to scam agencies / hosts | Trustpilot (2.0★, 986 reviews) | High within Trustpilot (~5 of 20 recent) | 2026-07 to 2026-10 | [trustpilot.com/review/www.bigo.tv](https://www.trustpilot.com/review/www.bigo.tv?sort=recency) |
| Impersonation top-up fraud ("BIGGO+" ad) | Trustpilot | Isolated | 2026-08-10 | same |
| Razer Gold PIN failed to load; refund refused | Razer Insider forum | Isolated | Undated | [insider.razer.com](https://insider.razer.com/razer-support-45/razor-gold-refund-please-44917) `[UNVERIFIED — search summary only]` |
| Card decline / double charge | — | **Not found first-hand** | — | — |

- BIGO's web bundle contains a dedicated support flow: *"I recharged, but I haven't received the diamonds."* / *"Please upload a screenshot of the deduction record of the recharge channel."* Non-credited recharges are therefore common enough to have their own support path. No frequency is disclosed.
- **Pattern:** reconciliation between processor "deducted" status and diamond credit is a known support category. With ~20 processors, each with its own status and callback semantics, that is a plausible operational cost. `[INFERENCE, not confirmed]`
- ⚠️ A reseller (BitTopup) publishes "68.5% decline rate" / "30–40% recharge failure" figures. This is conflicted marketing content. **Do not use.**

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 2026-08-26 | Q2 2026: revenue US$590.8M (+16.3%); Social Entertainment US$422.7M (+7.4%); developed-market live streaming +11.8%; paying users 1.56M, ARPPU US$220.5. **"AI-powered improvements to … payment experience"** | Tech / Payment signal | [Q2 2026 Ex. 99.1](https://www.sec.gov/Archives/edgar/data/1530238/000110465926101098/tm2624081d1_ex99-1.htm) |
| 2 | 2026-Q1 | JOYY re-segments into Social Entertainment, BIGO Ads and Shopline; no Bigo-only metrics disclosed | Corporate | Q2 2026 Ex. 99.1 |
| 3 | 2026-02-14 | Turkey's BTK reportedly blocks Bigo Live (Turkey is #10 web market) | Regulatory | [gazetebirlik.com](https://www.gazetebirlik.com/genel/bigo-neden-acilmiyor-bigo-kapatildi-mi-erisim-engeli-son-durum-bigo-live-neden-kapatildi/939058) `[UNVERIFIED — search summary only]` |
| 4 | 2025-09-19 | Cocodp named "Bigo Live's first third-party U.S. top-up partner" | Partnership | [TechNode / PRNewswire](https://technode.global/prnasia/cocodp-becomes-bigo-lives-first-u-s-top-up-partner-bringing-seamless-local-payment-options/) `[UNVERIFIED — search summary only]` |
| 5 | 2024-12 / 2025-01 | Bigo Live removed from Google Play and iOS App Store in Dec 2024; reinstated Dec 2024 (Play) and early Jan 2025 (iOS) | Distribution risk | [FY2025 20-F](https://www.sec.gov/Archives/edgar/data/1530238/000110465926049917/joyy-20251231x20f.htm) |

- **No public payment-related RFP found.**
- **No payment-infrastructure job postings found.**
- **No payment licence applications found.**

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 2026-08-26 | JOYY cites "payment experience" improvements among Q2 2026 drivers | Payments is on management's agenda | [Q2 2026 Ex. 99.1](https://www.sec.gov/Archives/edgar/data/1530238/000110465926101098/tm2624081d1_ex99-1.htm) |
| 2 | 2026-04-28 | FY2025 20-F: *"there are currently only a limited number of third-party online payment systems. If any of these major payment systems decides to cease to provide services to us, or significantly increase the percentage they charge us … our results of operations may be materially and adversely affected."* | Self-declared payment-provider concentration risk | [FY2025 20-F](https://www.sec.gov/Archives/edgar/data/1530238/000110465926049917/joyy-20251231x20f.htm) |
| 3 | 2025-09-19 | Cocodp US top-up partnership | Reseller distribution | `[UNVERIFIED — search summary only]` (URL above) |
| 4 | 2023-11-01 | BIGO × Checkout.com × Visa Direct: creator payouts in UK/IT/DE/CH/AT, *"from a single integration"* | BIGO already buys the "single integration" value proposition, on the payout side | [Checkout.com newsroom](https://www.checkout.com/newsroom/bigo-checkout-com-and-visa-join-forces-to-transform-the-content-creator-economy) |
| 5 | 2022-11-15 | TripleA crypto top-ups (BTC/ETH/USDT/USDC) | Crypto rail. Today's live US crypto channels are Strike (Lightning) and Stripe (stablecoin), with no TripleA string seen, so it may be replaced `[INFERENCE, not confirmed]` | [Fintech News SG](https://fintechnews.sg/66825/crypto/streaming-platform-bigo-live-partners-triplea-to-enable-users-to-pay-with-crypto/) `[UNVERIFIED — search summary only]` |

No confirmed provider removals.

---

### Section 8: Checkout Experience Audit

Scope: *"Full checkout flow not accessible. Findings limited to publicly observable elements."* The BIGO LIVE Pay landing page and channel trees are public. Placing an order requires a BIGO ID and login. `bigo.tv/recharge` redirected to a QR-login wall.

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | Custom-built web checkout ("BIGO LIVE Pay"), hosted on BIGO domains; processor-specific redirects or SDKs per channel | Good | `www.bigo.tv/bigolivepay-recharge/`, `mobile.bigo.tv/live/bigolivepay/` |
| Guest checkout | No. A BIGO account / ID is required. | N/A | Expected for crediting a user wallet |
| Steps to complete payment | Not observable (login wall) | — | |
| Card input experience | Card channels carry a `_pci` suffix (`stripe_pci-card`, `airwallex_pci-card_v2`), suggesting PSP-hosted card capture | — | `[INFERENCE, not confirmed]` |
| Payment methods visible | 5–17 per country (KR 17, ID 13, MY 13, TH 10, PH 8, US 8, NG 5) | Good | Channel trees |
| Location-based method display | **Yes.** Country auto-detect (`getSelectCountry`) plus a per-country channel tree | Good | |
| Instalment / EMI options | Atome BNPL (MY) only | Fair | Low relevance for top-ups |
| 3DS implementation | Not detected (`3ds` returns 0 hits in captured bundles) | — | Not observable pre-login |
| PCI indicator | PSP-side card capture likely | — | See Section 9 |
| Mobile responsiveness | `mobile.bigo.tv` variant exists; bigo.tv is 73.7% mobile web | — | |
| Multi-currency / local pricing | **Yes.** Local-currency ladders per country and per method; pricing differs by method (carrier vs wallet) | Good | |
| Saved payment methods | Not observable | — | |
| Error message clarity | A dedicated "recharged but no diamonds" support flow exists | Fair | |

**Off-store steering:** the bigo.tv header shows *"Recharge — 25% off"*. Bundle strings include *"Recharge packages too expensive? Save 25% by using [001] to recharge"* and *"Having trouble with the recharge process? Try the [001] recharge channel"*.

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found (only a reseller blog claims "Level 1"; not credible) | — |
| Card data handling | Not found. `_pci`-suffixed PSP card channels suggest PSP-hosted capture. | Channel tree / bundles |
| Recommended Yuno integration | Back-to-back API: BIGO owns the front end and channel tree and would route behind it | — |

*"No direct PCI compliance documentation found publicly for BIGO Live."*

`[INFERENCE, not confirmed]`: Based on confirmed use of PSP card channels (Stripe, Airwallex, Dinopay), card data is likely held per PSP, with no central BIGO vault seen. That fragments card-on-file across processors.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: The off-store channel is growing, and it all lands on a ~20-processor build**
> **Evidence:**
> - S8: BIGO steers users off-store ("save at least 25%", [BIGO LIVE Pay](https://mobile.bigo.tv/live/bigolivepay/index.html?lang=en)).
> - S6/S7: the audited Dec 2024 store removal and a self-declared payment-concentration risk factor ([20-F](https://www.sec.gov/Archives/edgar/data/1530238/000110465926049917/joyy-20251231x20f.htm)).
> - S3: ~20 processors live in the first-party checkout (channel tree).
>
> **Pain Point:** Every point of share moved off-store raises the load on an in-house layer that must keep ~20 integrations, callbacks and reconciliations current. The visible support flow for "recharged but no diamonds" shows the reconciliation cost is already real.
> **Yuno Value Proposition:** One integration behind BIGO's existing channel tree. BIGO keeps its front end; Yuno carries the processor connections, routing and failover, and consolidates reconciliation.
> **Best Success Case:** A multi-market gaming / virtual-currency merchant from the y.uno customer set (Garena, NetEase, Moon Active), on profile match. Pull the actual case internally; metrics not verified here.
> **Outreach Angle:** "You've already done the hard part, getting users to recharge off-store. The question is what it costs to keep twenty processors behind that page current as the share grows."
> **Suggested Subject Line:** BIGO LIVE Pay — twenty processors behind one page

> **Insight #2: The same method, three processors, three countries**
> **Evidence:**
> - S3/S4 channel trees: ShopeePay via iPay88 (ID), Ksher (TH) and direct (MY).
> - TrueMoney wired twice in TH (`route_truemoney`, `mol-truewallet`).
> - Cards across Dinopay, Stripe, Onerway and Airwallex live, with Adyen, Checkout.com and Ocean in code.
>
> **Pain Point:** Per-market processor choices compound into separate contracts, settlement files, dispute flows and fraud rules for the same consumer method. This is classic in-house orchestration debt.
> **Yuno Value Proposition:** Normalise methods across processors, with routing rules by country and cost, and one reporting layer.
> **Best Success Case:** Same as #1, gaming / digital goods multi-market.
> **Outreach Angle:** "Noticed ShopeePay runs through a different processor in each of Indonesia, Thailand and Malaysia on BIGO LIVE Pay. Deliberate, or history?"
> **Suggested Subject Line:** ShopeePay, three ways

> **Insight #3: JOYY runs two parallel in-house payment platforms**
> **Evidence:**
> - S3B: BIGO's stack (`/pay-bigolive-flow`) shares no code strings with HAGO's pay-center.
> - S11B / hago.md: HAGO's pay-center routes ~25 JOYY apps through ~25 PSPs on its own backend.
> - Processor overlap between the two stacks: Coda, MOL/Razer, Airwallex, Stripe, dLocal, Checkout.com.
>
> **Pain Point:** Two teams maintain overlapping processor integrations, which duplicates engineering and fragments negotiating leverage with shared PSPs.
> **Yuno Value Proposition:** A group-level layer serving both stacks: consolidated volume per PSP, and one integration maintained once.
> **Best Success Case:** None verified for a multi-brand group. Do not cite one.
> **Outreach Angle:** Internal and group-level only. Use in a second meeting with someone who spans both teams, never cold. Cold, it reads as surveillance.
> **Suggested Subject Line:** *(Not for cold use)*

> **Insight #4: Korea is growing, and it takes six processors to serve it**
> **Evidence:**
> - S12: developed-market live streaming +11.8% YoY; South Korea is named in JOYY's "developed" bucket ([Q2 2026](https://www.sec.gov/Archives/edgar/data/1530238/000110465926101098/tm2624081d1_ex99-1.htm)).
> - S4/S3: the KR channel tree runs Payoneq, Toss, SettleBank, Ant (KakaoPay), Haipay and Airwallex for 17 methods.
> - S2: no Korean entity found.
>
> **Pain Point:** Korea is the most processor-dense market in the tree. Without a local entity it depends on local PG intermediation, and carrier billing is absent from the web checkout.
> **Yuno Value Proposition:** Consolidate local-PG access and add rails without new bilateral integrations.
> **Best Success Case:** None verified for Korea. Do not imply one.
> **Outreach Angle:** "Six processors for one market is a lot of plumbing. Is Korea where the payments team spends most of its integration time?"
> **Suggested Subject Line:** Korea on BIGO LIVE Pay

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks:**
1. BIGO LIVE Pay offers "save at least 25%" to pull recharges off-store, and behind it sit about twenty processors keyed market by market.
2. ShopeePay runs through iPay88 in Indonesia, Ksher in Thailand and a direct integration in Malaysia on your web checkout. Is that by design?
3. You already bought "one integration, many destinations" for creator payouts with Checkout.com and Visa in 2023. Pay-ins are where the sprawl is now.

**Cold call openers:**
1. "Quick one: as more recharge moves to BIGO LIVE Pay, who owns keeping twenty-odd processors behind it current?"
2. "I was looking at your Korea checkout. Six different processors for one market. Is that where your integration time goes?"
3. "Your 20-F calls out dependence on a limited number of payment providers. Is that still how the team sees it?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| 17LIVE | 17.live | Taiwan / Japan (SGX) | FY2025 revenue US$158.8M | JP, TW, SEA | Not found (resellers only) | [SGX release](https://links.sgx.com/1.0.0/corporate-announcements/LETB5M3ZLVNSK9TA/876185_17LIVE-FY2025%20Press%20Release.pdf) `[UNVERIFIED — search summary only]` |
| StarMaker | starmakerstudios.com | Not confirmed | Not found | US, global | **PayerMax** + **Oceanpayment** (US) | [StarMaker blog](https://www.starmakerstudios.com/en/blog/product-news/starmaker-payermax-us-payment-collaboration/10) |
| Tango | tango.me | US (Palo Alto) / Israel | Not confirmed | US, India | Not found | [The Captable](https://the-captable.com/2025/04/tango-live-streaming-microtransactions) (paywalled) |
| Uplive (Asia Innovations) | Not verified | Shenzhen / Singapore | 2022 SPAC proposal at US$2.5B (completion unconfirmed) | SEA, MENA | Not found | [SEC 425](https://www.sec.gov/Archives/edgar/data/1843121/000110465922104449/tm2227104d3_425.htm) `[UNVERIFIED — search summary only]` |
| Mico | micoworld.net | China | TAL est. ~US$200M | MENA, Asia | Codashop distribution (pattern-level, per livu.md) | 2-ready-to-outreach/livu.md |
| Chamet | chamet.com | Hong Kong | Not found | MENA, Asia | Codashop distribution (per livu.md) | livu.md, 3-outreached/azar.md |
| Poppo Live | poppo.com | Singapore / China (TAL conflicts) | Not found | ME, South Asia | Not found | — |
| Kumu | kumu.ph | Philippines | Series C US$73.6M (2021, summary only) | PH | GCash billed **via** Google Play / App Store | [Kumu blog](https://blog.kumu.ph/buying-kumu-coins-and-sending-virtual-gifts-now-made-easier-with-new-gcash-feature/) |
| LivU | livuapp.com | Hong Kong | ~70M Play installs | TR, US, BR, APAC | Stripe, Checkout.com, dLocal, PayerMax, Airwallex, Coda; in-house routing | 2-ready-to-outreach/livu.md |

#### 11B. Industry Peers

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| HAGO (JOYY) | ihago.net | Casual game + voice social | SEA, MENA, LatAm | Separate JOYY in-house pay-center, ~25 PSPs | 2-ready-to-outreach/hago.md |
| Likee (JOYY) | likee.video | Short video + gifting | SEA, South Asia, RU, ME | Same group; stack not researched (may share BIGO's) | TAL |
| Kuaishou / Kwai | kuaishou.com | Short video + live | BR, ID, global | In-house routing; dLocal, EBANX, PayerMax, Checkout.com, Stripe | 2-ready-to-outreach/kuaishou.md |
| Azar (Match Group) | azarlive.com | Video chat | TR, MENA, Asia | In-house; web store with cards/PayPal | 3-outreached/azar.md |
| Sea / Garena | garena.com | Gaming | SEA | TAL lists in-house routing; **Garena logo on y.uno** | TAL; y.uno |
| TikTok LIVE | tiktok.com | Short video + live | All | PIPO (ByteDance in-house) + Worldpay, Stripe, PayPal | kuaishou.md |

#### 11C. Companies Recently Adopting Payment Orchestration

*"No public case studies found of direct competitors adopting payment orchestration."* The category pattern is **in-house routing over many PSPs** (BIGO, HAGO, LivU, Kwai).

#### 11D. Prospect Scoring

Verified signals only. Volume is unassessed for all (0, ⬜).

| Company | Orch. | 3+ countries | Multi-PSP | Other verified | Score | Evidence |
|---------|-------|--------------|-----------|----------------|-------|----------|
| StarMaker | ⬜ 0 | ⬜ | ✅ +3 (PayerMax, Oceanpayment) | — | **3+** (under-researched) | StarMaker blog |
| LivU | +1 | ✅ +3 | ✅ +3 | per livu.md | **11** (livu.md) | livu.md |
| HAGO | +1 | ✅ | ✅ | per hago.md | **19** (hago.md) | hago.md |
| 17LIVE | ⬜ | ✅ +3 (JP, TW, SEA) | ⬜ | — | **3+** | SGX (summary) |
| Kumu | ⬜ | ❌ (PH only) | ⬜ | — | **0+** | Kumu blog |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | HAGO | JOYY sister | SEA, MENA | 19 | ⭐ | Separate in-house pay-center | ✅ `HAGO` |
| 2 | Likee | JOYY sister | SEA, South Asia | Not scored | — | Same group, unresearched stack | ✅ `Likee` |
| 3 | **imo** | JOYY sister (messaging + live) | Global | Not scored | — | Counted with Bigo/Likee in JOYY's paying users | ❌ **genuine find: not on the TAL** |
| 4 | **StarMaker** | Competitor | US, global | 3+ | Research | Two acquirers in the US, PayerMax case study (Sep 2026) | ❌ **genuine find: not on the TAL** (only mentioned in the Pavami row) |
| 5 | Kuaishou (Kwai) | Peer | BR, ID | 17 | ⭐ | In-house routing, multi-PSP | ✅ |
| 6 | LivU | Competitor | TR, US, APAC | 11 | 🟢 | In-house routing | ✅ |
| 7 | 17LIVE | Competitor | JP, TW | 3+ | Research | Japan/Taiwan-heavy live gifting | ✅ `17LIVE` |
| 8 | **Tango** | Competitor | US, India | Not scored | Research | Large India gifting revenue (summary only) | ❌ **genuine find: not on the TAL** (US-HQ; territory check needed) |
| 9 | **Uplive / Asia Innovations** | Competitor | SEA, MENA | Not scored | Research | Shenzhen/Singapore, large-scale | ❌ **genuine find: not on the TAL** |
| 10 | Mico | Competitor | MENA, Asia | Not scored | — | Codashop distribution | ✅ `Mico` |

TAL hygiene: Poppo appears twice (`VShow`, `Poppolive`) with conflicting HQ. kuaishou.md line 483 says Likee is not on the TAL, which is wrong; it is.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | **Group:** US$2,124.2M (FY2025). **Old BIGO segment** (Bigo Live + Likee + imo + BIGO Ads): US$1,848.4M (FY2025). **Bigo Live alone: not disclosed.** | [FY2025 20-F](https://www.sec.gov/Archives/edgar/data/1530238/000110465926049917/joyy-20251231x20f.htm) |
| Live streaming revenue | US$1,529.7M (FY2025); US$402.6M (Q2 2026, +7.3%); H1 2026 US$782.9M. Three apps. | 20-F; [Q2 2026](https://www.sec.gov/Archives/edgar/data/1530238/000110465926101098/tm2624081d1_ex99-1.htm) |
| GMV / Gross Transaction Volume | Not disclosed | — |
| Average Transaction Value (USD) | Not disclosed. First-party ladders range from ~US$0.30 (Rp5k) to ~US$4,000+ (฿150k) per pack. | Channel trees |
| ARPPU | US$220.5 / quarter (Q2 2026); core live streaming paying users 1.56M | Q2 2026 |
| Est. Annual Transactions | See next row | — |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ~1.9M/month off-store web recharges.** `[ASSUMPTION — not researched.]` See the derivation below the table. | Disclosure rule |
| Active Customers / Users | Group MAU 277.1M (Q2 2026); paying users 3.6M in FY2025 (Bigo Live, Likee, imo) | Q2 2026; 20-F |
| Primary Currency | USD reporting; local-currency collection in 12+ markets | Channel trees |
| Top 3 Markets by Revenue | Not disclosed per market. FY2025 group split: Developed 58.9% (US, SG, JP, KR, UK named), SEA & others 19.8%, Middle East 11.5%, Mainland China 9.8% | 20-F |
| Billing channel split (web vs app store) | **Not disclosed.** BIGO steers users off-store with a 25% discount. | BIGO LIVE Pay page |
| Payment handling costs | US$98.2M (FY2025, group); 6.4% of live streaming revenue (7.0% in 2023) | 20-F. ⚠️ **Do not read as an off-store share.** Store commissions may be netted or booked elsewhere; the filing does not say. `[INFERENCE, not confirmed]` |

**Monthly transaction count — derivation (ASSUMED):**
- **Billing unit:** one diamond recharge purchase. App-store IAP is excluded because it is not addressable.
- **Basis:** Q2 2026 live streaming revenue of US$402.6M/quarter (**SOURCED**) ≈ US$134.2M/month across three apps. Three inputs are **ASSUMED**: Bigo share, off-store share and average ticket.

| Scenario | Bigo share | Off-store share | Avg ticket | Transactions / month |
|---|---|---|---|---|
| Harsh | 50% | 5% | US$50 | ~67,000 |
| **Base** | **70%** | **30%** | **US$15** | **~1.9M** |
| Generous | 85% | 50% | US$10 | ~5.7M |

- Even the harsh case clears 40k, so the account scores the ≥100k band (+5, ⚠️).
- Sanity check: ARPPU of US$220.5/quarter is ~US$73.5/month per payer, which is plausible at multiple recharges a month.
- **Confirm on the first call.**

---

### Overall Research Confidence

**Medium-High.**
- **Strong:**
  - The payment stack (S3/S4) rests on BIGO's own production channel trees for 13 countries and its live bundles, partly re-verified by me.
  - Financials come from the FY2025 20-F and Q2 2026 release, checked against the downloaded filings.
  - Orchestration classification is based on positive evidence.
- **Limited:**
  - **Traffic was supplied** but is web-only, top-10-only and share-only. bigo.sg's mix is atypical, and the app (where most spend happens) is invisible.
  - No Bigo-only financials exist.
  - The IAP vs off-store split is unknown.
  - The `route_`/`local_` processors are hidden.
  - Entities outside Singapore, HK and PRC are unverified.
  - Complaints were sampled lightly: 150 App Store reviews and 20 Trustpilot reviews, no Google Play.
  - The checkout was not walked past login.

---

### Manual Research Recommendations

> **Area:** Monthly transaction count / off-store share
> **Why it matters:** It is the only gate signal, it is assumed, and it decides how much volume is addressable at all.
> **Suggested manual action:** First-call question: "Roughly what share of diamond recharge now runs through BIGO LIVE Pay versus the stores?"

> **Area:** JOYY account coordination with HAGO
> **Why it matters:** Same parent, separate payment stacks. Two uncoordinated sequences into one group burns both.
> **Suggested manual action:** Agree a single JOYY plan with your manager before sequencing either. Use LinkedIn to find who owns payments for BIGO LIVE Pay vs the HAGO pay-center.

> **Area:** Processors behind `route_` / `local_` channels
> **Why it matters:** Determines whether GoPay, PromptPay, GCash etc. are direct or via an aggregator, which shapes the consolidation pitch.
> **Suggested manual action:** Log in on web with DevTools in ID/TH/PH and capture the redirect host for one `route_` and one `local_` payment.

> **Area:** Legal entities in top markets
> **Why it matters:** Confirms whether Indonesia/Korea flows are domestically acquired.
> **Suggested manual action:** ACRA BizFile+ (SG UEN), Indonesia AHU (PT Bigo Technology Indonesia), and the FY2025 20-F Exhibit 8.1.

> **Area:** Turkey block (Feb 2026)
> **Why it matters:** Turkey is a top-10 web market; a block changes the market mix.
> **Suggested manual action:** Confirm with a primary BTK / news source before referencing it.

---

### Appendix: All Source URLs

**Traffic**
- `accounts/traffic/bigo-live.md` — SimilarWeb Sales Intelligence, supplied 2026-10-19

**Phase 0 / Entities / Financials**
- https://www.sec.gov/Archives/edgar/data/1530238/000110465926049917/joyy-20251231x20f.htm
- https://www.sec.gov/Archives/edgar/data/1530238/000110465926101098/tm2624081d1_ex99-1.htm
- https://data.sec.gov/submissions/CIK0001530238.json
- https://itunes.apple.com/lookup?id=1077137248&country=us
- https://www.sec.gov/Archives/edgar/data/1530238/000141057823000819/tmb-20221231xex8d1.htm
- https://www.registrationwala.com/company/bigo-service-india-private-limited/U93000HR2018FTC072223
- https://nasional.kontan.co.id/news/menkominfo-ancam-blokir-aplikasi-bigo-live-terkait-judi-online-dan-pornografi
- https://www.preqin.com/data/profile/asset/bigo-technology-pte--ltd-/226738
- https://y.uno/en

**Payment stack / methods**
- https://mobile.bigo.tv/live/bigolivepay/index.html?lang=en
- https://mobile.bigo.tv/pay-bigolive-flow/live/quickPay/getChannelTree?country={US,ID,TH,PH,KR,MY,NG,RU,BR,TR,IN,VN,PK}&apk=official&platform=ios_outside&isFromApp=0
- https://mobile.bigo.tv/pay-bigolive-tv/quicklyPay/getSelectCountry?isFromApp=0
- https://www.bigo.tv/_nuxt_cdn_/app.b9737d.js
- https://static-pay.bdesk.tech/live/assets/bigolivepay/js/index.cd2f08.js
- https://static-pay.bdesk.tech/live/assets/bigolivepay/js/35.387861.js
- https://www.checkout.com/newsroom/bigo-checkout-com-and-visa-join-forces-to-transform-the-content-creator-economy
- https://fintechnews.sg/66825/crypto/streaming-platform-bigo-live-partners-triplea-to-enable-users-to-pay-with-crypto/
- https://www.codashop.com/id-id/bigo-live · https://www.codashop.com/th-th/bigo-live · https://www.codashop.com/en-ph/bigo-live · https://www.codashop.com/en-my/bigo-live
- https://www.campaignasia.com/article/singapores-bigo-technology-awaits-clarity-after-being-hit-by-indian-app-ban/462136

**Complaints / news / corporate**
- https://itunes.apple.com/{ph,id,th}/rss/customerreviews/page=1/id=1077137248/sortby=mostrecent/json
- https://www.trustpilot.com/review/www.bigo.tv?sort=recency
- https://insider.razer.com/razer-support-45/razor-gold-refund-please-44917
- https://technode.global/prnasia/cocodp-becomes-bigo-lives-first-u-s-top-up-partner-bringing-seamless-local-payment-options/
- https://www.gazetebirlik.com/genel/bigo-neden-acilmiyor-bigo-kapatildi-mi-erisim-engeli-son-durum-bigo-live-neden-kapatildi/939058

**Competitors**
- https://www.starmakerstudios.com/en/blog/product-news/starmaker-payermax-us-payment-collaboration/10
- https://blog.kumu.ph/buying-kumu-coins-and-sending-virtual-gifts-now-made-easier-with-new-gcash-feature/
- https://links.sgx.com/1.0.0/corporate-announcements/LETB5M3ZLVNSK9TA/876185_17LIVE-FY2025%20Press%20Release.pdf
- https://the-captable.com/2025/04/tango-live-streaming-microtransactions
- https://www.sec.gov/Archives/edgar/data/1843121/000110465922104449/tm2227104d3_425.htm
- Internal: `2-ready-to-outreach/hago.md`, `2-ready-to-outreach/livu.md`, `2-ready-to-outreach/kuaishou.md`, `3-outreached/azar.md`, `accounts/apac-tal.csv`

</details>
