# Inditex (Zara)

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 10 / 29 → 🟢 Medium *(a verified floor. The core e-commerce PSP is unknown, so the +4 orchestration award and the +3 multi-PSP award are both held at 0. If discovery confirms direct PSP integrations with no routing layer, the score is 17, ⭐. Read the territory caveat in the ICP breakdown before working this account: HQ and the payments decision centre are in Spain.)*
**Industry:** Retail. Apparel (Zara, Pull&Bear, Massimo Dutti, Bershka, Stradivarius, Oysho, Zara Home, Lefties), omnichannel stores + own e-commerce + apps · **HQ:** Arteixo (A Coruña), Spain. Industria de Diseño Textil, S.A. (BME: ITX) · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **Greenfield on the evidence, with a strong in-house tech culture.** No orchestrator and no in-house routing layer found. But the main zara.com PSP/acquirer is also **unknown in every market**, so "greenfield" is a classification by absence, not a confirmed direct-integration stack. Inditex built its own wallet (InWallet, 2016) and builds most tech in-house; assume a sophisticated team that will ask "why not build it".

---

> ## 🎯 THE HOOK: Zara Japan's stores take the wallets its online checkout doesn't
>
> A Japanese payments guide (pricey.jp, last updated 2026-06-12, citing Zara's official payment-methods page; fetched and checked) gives the full split:
>
> | Channel | Accepted | Not accepted |
> |---|---|---|
> | **zara.com/jp + app** | Visa / MC / Amex / JCB, Apple Pay, PayPay, cash on delivery, gift card | **Google Pay, Rakuten Pay** (*"楽天ペイ・Google Payは現時点では非対応です"*), Diners, d払い. No konbini, Paidy or Zara-run instalments found (*"ZARAとして独自の分割払いサービスは提供していません"*) |
> | **Zara stores in Japan** | PayPay, d払い, au PAY, メルペイ, Bank Pay, Alipay, WeChat Pay, transit IC, cards incl. Diners | Rakuten Pay |
>
> Source: https://pricey.jp/web/articles/5788. **Third-party page, not Zara's own** — zara.com blocks automated access. Confirm on zara.com/jp in a real browser before quoting it.
>
> **Why this is the opening:** it is the same store-vs-online gap documented at UNIQLO (see `2-ready-to-outreach/fast-retailing-uniqlo.md`). Zara Japan Corp. is a 100% Inditex entity (FY2019 consolidated accounts), so there is no franchisee in the way. **Caveat:** Japan is not in zara.com's top 10 traffic markets (each below 3.28%), so its web volume is unmeasured.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Inditex is the world's largest fashion group by sales: FY2025 (to 31 Jan 2026) net sales €39.86bn (+3.2%; +7% constant FX), net profit €6.22bn ([FashionUnited](https://fashionunited.com/news/business/inditex-posts-6-22-billion-euro-profit-in-2025-and-3-19-percent-sales-growth/2026031171084)). Online sales were €10.656bn, **26.7% of the total** ([marketing4ecommerce](https://marketing4ecommerce.net/ventas-online-de-inditex-2025/)). "Asia and the rest of the world" was ≈€5.98bn in FY2025 and **15% of sales in H1 2026** ([FashionUnited UK](https://fashionunited.uk/news/business/inditex-hits-new-high-reports-profit-of-2-98-billion-euros-with-7-6-percent-growth-through-july/2026090990227)). That bucket is broader than this territory: it includes the Middle East and other non-APAC markets.

**SimilarWeb total visits (last full month):** ≈102.5M/month on average, Jul–Sep 2026 (zara.com, 307.5M over 3 months) — SimilarWeb, supplied 2026-10-19. Monthly figures not supplied, so this is the 3-month average. **Caveats from the traffic file (`accounts/traffic/inditex-zara.md`):**
- Sales Intelligence view: top 10 countries only, **share only, no per-country visits**. Visit figures below are `[DERIVED from supplied share, not a SimilarWeb figure]`.
- **Mobile app traffic is excluded** (desktop + mobile web only; 72.89% of web visits are mobile web).
- Omnichannel retailer: the Zara app and in-store POS carry a large share of transactions, so web traffic understates payment volume. Use it as a market-mix signal, not for sizing.
- **Only zara.com was pulled.** Pull&Bear, Massimo Dutti, Bershka, Stradivarius, Oysho and inditex.com are excluded. **zara.cn** (China) is not in the data either — not pulled, not checked.
- Global rank not captured.

### Top 5 markets
All five of zara.com's top web markets are **out of territory**. The only APAC market in the top 10 is South Korea (#10, 3.28%). APAC detail is in the next table.

| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇺🇸 United States *(out of territory)* | 13.44% | Not assessed | Not assessed | Not checked |
| 2 | 🇪🇸 Spain *(home, out of territory)* | 8.41% | Not assessed (Bizum reported, unverified) | Not assessed | ✅ HQ |
| 3 | 🇬🇧 United Kingdom *(out of territory)* | 6.71% | Not assessed | Not assessed | Not checked |
| 4 | 🇫🇷 France *(out of territory)* | 5.40% | Not assessed | Not assessed | Not checked |
| 5 | 🇵🇱 Poland *(out of territory)* | 5.07% | Not assessed | Not assessed | Not checked |

### APAC markets
| Market | Traffic | Online methods found | Missing / unknown online | Entity (FY2019 perimeter unless noted) |
|---|---|---|---|---|
| 🇰🇷 South Korea | **3.28% (#10)** ≈3.36M visits/month `[DERIVED]` | **None confirmed.** NHN KCP script detected on zara.com per a tech-profiler listing `[UNVERIFIED — search summary only]` | Everything unknown — no Zara KR payment page indexed | ✅ Zara Retail Korea, Co Ltd. — **80% Inditex / 20% Lotte Shopping** |
| 🇯🇵 Japan | <3.28% (not in top 10) | Cards (V/MC/Amex/JCB), Apple Pay, PayPay, COD, gift card | **Google Pay, Rakuten Pay (explicitly not supported)**, d払い, au PAY online; konbini, Paidy, instalments not found | ✅ Zara Japan Corp. (100%) |
| 🇨🇳 China | Not in data (zara.cn not pulled) | Not found | Unknown | ✅ ITX E-commerce (Shanghai) Co. Ltd (100%) + Zara Commercial entities |
| 🇭🇰 / 🇲🇴 / 🇹🇼 | <3.28% | Not found | Unknown | ✅ Zara Asia, Ltd. (HK); Zara Macau, Ltd.; ITX Taiwan B.V. Zara Taiwan Branch (all 100%) |
| 🇦🇺 / 🇳🇿 | <3.28% | AU: PayPal + major cards **at the 2018 launch only** | Afterpay / Zip / Klarna / PayTo not found | ✅ Group Zara Australia Pty. Ltd.; Zara Retail NZ Limited (100%) |
| 🇮🇳 India | <3.28% | Paytm, PayPal, cards **at the 2017 launch only** | UPI / netbanking / EMI not found (unknown, **not** a sourced gap) | ✅ Inditex Trent Retail India Pvt Ltd — **Trent now 20%** (FY26) |
| 🇸🇬🇲🇾🇹🇭 | <3.28% | SG: conflicting search summaries (cards ± PayPal / Apple Pay) | Unknown | ⚠️ No subsidiary — **franchise inferred**, partner unconfirmed |
| 🇮🇩🇻🇳🇵🇭 | <3.28% | Not found | Unknown | ⚠️ **Franchise:** ID/VN via Mitra Adiperkasa (MAP), PH via SSI Group `[UNVERIFIED — search summary only]` |

### Legal entities
From Inditex's FY2019 consolidated accounts filed with CNMV (fetched; the newest perimeter obtained — re-check against the FY2025 annual report):
- Industria de Diseño Textil, S.A. (Spain) — parent
- Zara Japan Corp. (Tokyo, 100%) + Bershka / Stradivarius / Zara Home Japan entities
- Zara Retail Korea, Co Ltd. (Seoul, **80%**; Lotte Shopping holds 20% under put/call options) + 100% Korea entities for the other brands
- ITX E-commerce (Shanghai) Co. Ltd (100%, "Retail sales"); Zara Commercial (Shanghai / Beijing)
- Zara Asia, Ltd. (Hong Kong, 100%); Zara Macau, Ltd. (100%); ITX Taiwan B.V. (Zara Taiwan Branch)
- Group Zara Australia Pty. Ltd. (Sydney, 100%); Zara Retail NZ Limited (Auckland, 100%)
- Inditex Trent Retail India Private Ltd (Gurgaon; 51% in FY2019 → Trent now **20%** per Trent's FY26 annual report)

### Known PSPs
- **Stripe** — `[Press Release]` 2023-05-22, **Zara Pre-Owned resale marketplace only** (UK, then Europe). "selected as Zara's payments partner to process all payments for the retailer's pre-owned clothing marketplace" ([stripe.com](https://stripe.com/newsroom/news/zara-and-stripe), fetched). Not the main checkout.
- **BBVA** — `[Third-Party Report]` 2020, Spain **in-store card terminals** ("tiene contratado los TPV de las tiendas físicas") ([merca2.es](https://www.merca2.es/bizum-bbva-inditex/)). Out of territory, and six years old.
- **NHN KCP** — Korea `[UNVERIFIED — search summary only, page not fetched]`: a tech-profiler listing reportedly shows zara.com using NHN KCP.
- **The main zara.com PSP/acquirer is unknown in every market.** No Adyen, Worldpay, Checkout.com, Cybersource or APAC-gateway relationship found.

### Orchestration status
**None detected — low confidence.** No Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails or Yuno link found, and no in-house routing layer evidenced. InWallet (2016, "developed entirely in-house") is a consumer wallet, not a routing layer. Because the core PSPs are also unknown, this cannot be called "direct PSP integrations only" with confidence.

### Buying signals
- 🤝 **India JV consolidated under Inditex:** Trent cut its stake in Inditex Trent Retail India to **20%** through a buyback. Zara India FY26 revenue was ₹2,749.28 cr (−1.1%) and profit ₹204.14 cr (−31.9%) on 22 stores ([Outlook Business, 2026-05-30](https://www.outlookbusiness.com/news/zaras-india-fy26-profit-falls-32-to-204-cr-revenue-slips), fetched)
- 🚀 **China reinvestment:** new ~2,000 m² Zara flagship on Huaihai Rd, Shanghai (opened 2026-06-06), positioned as a new global store concept ([Inside Retail](https://insideretail.asia/2026/06/11/zara-opens-flagship-in-shanghai-featuring-new-global-store-concept/)) `[UNVERIFIED — search summary only]`
- 📉 **SEA pruning:** Pull&Bear closed its last Singapore store on 2026-02-22 and its SG site is "currently unavailable for online purchases"; Bershka has no SG stores but still sells online ([Vulcan Post](https://vulcanpost.com/909437/pullbear-to-exit-singapore/), fetched)
- 💼 **Tech leadership turnover:** Global Chief Data & Analytics Officer Diego Teijeiro left for H&M (CIO from 25 May 2026) ([FashionUnited](https://fashionunited.com/news/people/spanish-executive-diego-teijeiro-leaves-inditex-to-lead-h-ms-global-technology-division/2026042371959)) `[UNVERIFIED — search summary only]`
- 📋 No public payment RFP, licence application or payments job posting found.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Inditex (Zara)` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 10 / 29
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | +5 | ✅ DERIVED (floor): **≥3.5M online orders/month group-wide.** FY2025 online sales €10.656bn ([marketing4ecommerce](https://marketing4ecommerce.net/ventas-online-de-inditex-2025/)) ÷ 12 = €888m/month. Even at a €250 average order (a deliberately high ceiling I chose — **not a sourced ATV**), that is ≈3.55M orders/month. Billing unit: online orders (web + app). Excluded: in-store POS across ~5,450 stores. The 40k gate cannot fire. **APAC-only count is not derivable:** online is not split by region. |
| Orchestration status | 0 | ⬜ Uncertain. No orchestrator and no routing layer found (Section 3B), but the core PSP is also unknown, so "direct PSP integrations only" cannot be verified. **Would be +4** if discovery confirms direct integrations. |
| 3+ countries | +3 | ✅ 10 countries above 1% of zara.com traffic; 7+ APAC legal entities in the FY2019 consolidated perimeter (JP, KR, CN, HK, MO, TW, AU, NZ, IN) |
| Multiple PSPs | 0 | ⬜ Two providers are evidenced — Stripe (Zara Pre-Owned) and BBVA (Spain store terminals, 2020) — but neither touches the main e-commerce checkout, and neither is in territory. Not awarded on substance. **Would be +3** once the core PSPs are known to be 2+. |
| Local rail or licensing gap in a top-3 market | 0 | ❌ zara.com's top 3 markets are the US, Spain and the UK — all out of territory. The Japan wallet gap (Google Pay, Rakuten Pay) is sourced, but Japan is not a top-3 market and the source is third-party. |
| Recent expansion | 0 | ❌ No new APAC market in the last 12 months. The Shanghai flagship is a format change in an existing market; Singapore saw a brand exit. |
| Payment issues reported | 0 | ⬜ Moderate pattern in the US (orders cancelled after payment; double charges — SikayetVar, search summary only) and Spain (app reviews citing "errores en el proceso de pago", fetched). **Nothing found in APAC.** Not awarded because the evidence is out of territory and mostly unverified. |
| Funding >$10M | 0 | ❌ Listed company, no rounds |
| High traffic outside home | +2 | ✅ Spain is 8.41% of zara.com traffic; Spain was 15.9% of FY2025 sales |
| Competitor using orchestration | 0 | ⬜ Only Zalora/BridgerPay, a vendor case study with conflicting dates and no Zalora quote. The TAL lists Shein as Juspay; no evidence was found for it. |
| Payment job postings | 0 | ❌ None found |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **🟢 Medium (10)**
No public payment RFP found.

**Analyst override check: no tier override, but read this before spending time here.**
- **Territory reality.** Inditex is HQ'd in Spain. APAC operations are real (owned entities in JP, CN, HK, MO, TW, AU, NZ; JVs in KR and IN), so it passes the territory gate. But the payments decision centre is almost certainly Arteixo (the only payments-adjacent name found, the Deputy CFO, sits in Spain). **Coordinate with the EMEA owner before any outreach** so Inditex is not approached twice from two Yuno regions.
- **APAC is small inside Inditex.** "Asia and rest of world" was 15% of H1 2026 sales and falling one point; only Korea makes zara.com's top-10 web markets. The APAC opportunity is a fraction of a very large account.
- **Franchise markets are not Inditex's checkout.** Indonesia, Vietnam and the Philippines appear to be franchised (MAP, SSI), and the Philippines Zara e-store is reportedly run by SSI. Payments there would sit with the franchisee — a separate sale (see the pipeline in Section 11).
- **Upside case (17, ⭐):** if discovery confirms (a) 2+ PSPs on the main checkout and (b) no routing between them, the matrix adds +4 and +3. That is plausible at this scale but **unevidenced**, so it is not scored.
- **Build-vs-buy risk:** InWallet was built "entirely in-house", and Inditex Tech is a large engineering organisation. Expect the in-house argument, even though no routing layer was found.
- **Not app-store dominated:** Zara is the merchant of record in its own apps. No IAP.

### Source Notes
- ✅ Japan online/in-store method split re-read by me in the fetched pricey.jp page (updated 2026-06-12), including the "Rakuten Pay / Google Pay not supported" and "no Zara-run instalments" lines
- ✅ Trent's 20% stake, the 94,900-share buyback, and Zara India FY26 revenue/profit re-read by me in the fetched Outlook Business article (it quotes Trent's annual report)
- ✅ Stripe / Zara Pre-Owned scope re-read by me on stripe.com (2023-05-22)
- ✅ FY2025 sales €39.86bn, net profit €6.22bn and Asia/RoW ≈€5.98bn re-read in the fetched FashionUnited article; online sales €10.656bn / 26.7% re-read in the fetched marketing4ecommerce article
- ✅ H1 2026 Asia & RoW at 15% (down 1pt) re-read in the fetched FashionUnited UK article
- ✅ APAC entities (Zara Japan Corp., Zara Retail Korea 80% + the Lotte put/call text, ITX E-commerce (Shanghai), Zara Asia, Zara Macau, ITX Taiwan, Group Zara Australia, Zara Retail NZ, Inditex Trent Retail India 51%) grep-checked by me in the FY2019 CNMV accounts
- ✅ Pull&Bear Singapore exit re-read in the fetched Vulcan Post article
- ⚠️ All entity data is **FY2019** (31 Jan 2020). The only post-2019 changes found are India (Trent stake cuts), China (Bershka / Pull&Bear / Stradivarius exit, 2021–22) and Singapore (brand exits, 2026). Others may exist.
- ⚠️ Franchise status of SG, MY, TH, ID, VN and PH is inferred from absence in the FY2019 perimeter. The MAP and SSI partner names come from search summaries only.
- ⚠️ NHN KCP for Korea is a search-summary claim about a tech-profiler listing. It is not a contract.
- ⚠️ The Japan method list is a third-party page that cites Zara's official page; it is not Zara's own page.
- ⚠️ José Manuel Romay (Deputy CFO) as owner of card-scheme/acquirer relationships rests on a 2023 Citi booklet seen only as a search summary (the fetch returned 404).

### Success Case Alternatives
- **Reserva (Yuno customer, Brazilian fashion brand)** — the only fashion-retail Yuno case found. Reported +4% approval in 3 months with Smart Routing (y.uno/success-cases/reserva) `[UNVERIFIED — search summary only, page not fetched; carried from the UNIQLO report]`. It matches the omnichannel apparel profile, but it is LatAm-only and a fraction of Inditex's scale.
- No APAC retail Yuno case found. Do not imply one.

---

## Executive Summary

Inditex (Zara) is a €39.9bn Spanish fashion group with 26.7% of sales online (€10.7bn). Its APAC footprint is a mix of 100%-owned subsidiaries (Japan, China, HK, Macau, Taiwan, Australia, NZ), JVs it controls (Korea 80/20 with Lotte; India, where Trent is now down to 20%) and apparent franchises (SEA). The payment stack is almost entirely opaque. The only named providers are Stripe for the Zara Pre-Owned resale marketplace and BBVA for Spanish store terminals; no orchestrator and no in-house routing layer were found. The motion is **greenfield by absence**, against a strong in-house tech team. The most concrete APAC opening is Japan: per a 2026 third-party guide, Zara's stores accept d払い, au PAY, Alipay and WeChat Pay, but online checkout takes only cards, Apple Pay, PayPay and COD, with Google Pay and Rakuten Pay explicitly unsupported. The account is HQ'd in EMEA and APAC is ~15% of sales or less, so coordinate ownership before outreach.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** Path 1, pasted SimilarWeb data: `accounts/traffic/inditex-zara.md`, SimilarWeb Sales Intelligence (supplied 2026-10-19), Jul–Sep 2026, desktop + mobile web, **zara.com only**.

**Method:** supplied share × zara.com's average monthly visits (102.5M). Every visit figure is `[DERIVED from supplied share, not a SimilarWeb figure]`.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | 🇺🇸 United States *(out of territory)* | 13.44% | 13.78M | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | 🇪🇸 Spain *(home, out of territory)* | 8.41% | 8.62M | Not supplied | same |
| 3 | 🇬🇧 United Kingdom *(out of territory)* | 6.71% | 6.88M | Not supplied | same |
| 4 | 🇫🇷 France *(out of territory)* | 5.40% | 5.54M | Not supplied | same |
| 5 | 🇵🇱 Poland *(out of territory)* | 5.07% | 5.20M | Not supplied | same |
| 6 | 🇹🇷 Turkey *(out of territory)* | 5.07% | 5.20M | Not supplied | same |
| 7 | 🇮🇹 Italy *(out of territory)* | 4.92% | 5.04M | Not supplied | same |
| 8 | 🇩🇪 Germany *(out of territory)* | 4.21% | 4.32M | Not supplied | same |
| 9 | 🇧🇷 Brazil *(out of territory)* | 3.35% | 3.43M | Not supplied | same |
| 10 | 🇰🇷 **South Korea (in territory)** | 3.28% | 3.36M | Not supplied | same |

The top 10 is 59.86% of traffic. The remaining **40.14%** is unlisted, so every other APAC market (Japan, Australia, China, HK, Taiwan, India, SEA) is somewhere below 3.28% each, with no figure.

**Notes**
- Device split: 72.89% mobile web, 27.11% desktop.
- Global rank: not captured in the source.
- **Mobile apps are excluded**, and the Zara app plus in-store POS carry a large share of transactions. Web traffic understates payment volume.
- **Domains not covered:** pullandbear.com, massimodutti.com, bershka.com, stradivarius.com, oysho.com, zarahome.com, inditex.com, and **zara.cn** (China). zara.com serves most markets via country sub-paths (/jp, /kr, /au, /in, /sg…), so those are inside the supplied data; zara.cn is a separate property and is not.
- **Entity cross-check:** South Korea, the only in-territory top-10 market, has a local entity (Zara Retail Korea, 80%). No cross-border gap among measured markets.
- **High priority (>5% share):** none in territory.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Arteixo, A Coruña, Spain. Industria de Diseño Textil, S.A. (Inditex), listed on the Spanish stock exchanges. FY2019 accounts: "operates 202 markets with a network of 7,469 stores in 96 markets", of which 6,357 company-managed and 1,112 franchised ([CNMV filing](https://internet.cnmv.es/AUDITA/2020/18378_en.pdf)).

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Japan | Zara Japan Corp. (Tokyo, 100%) + Bershka Japan, Stradivarius Japan, Zara Home Japan | Not found | [CNMV FY2019 accounts](https://internet.cnmv.es/AUDITA/2020/18378_en.pdf) |
| South Korea | Zara Retail Korea, Co Ltd. (Seoul, **80%**). "The Group holds a call option on 20% of the share capital of Zara Retail Korea, Ltd. This ownership interest is held by Lotte Shopping Co., Ltd." Other brands' Korea entities 100% | Not found | same |
| China | ITX E-commerce (Shanghai) Co. Ltd (100%, "Retail sales"); Zara Commercial (Shanghai), Zara Commercial (Beijing), Zara Fashion (Shanghai) | Not found | same |
| Hong Kong | Zara Asia, Ltd. (100%) + other brand entities | Not found | same |
| Macau | Zara Macau, Ltd. (100%) | Not found | same |
| Taiwan | ITX Taiwan B.V. — Zara Taiwan Branch (100%) | Not found | same |
| Australia | Group Zara Australia Pty. Ltd. (Sydney, 100%) | ABN not found | same |
| New Zealand | Zara Retail NZ Limited (Auckland, 100%) | Not found | same |
| India | Inditex Trent Retail India Private Ltd (Gurgaon). 51% in FY2019; **Trent now holds 20%** after a buyback, per Trent's annual report. Separate Massimo Dutti India Pvt Ltd (Trent 20%) | Not found | CNMV FY2019; [Outlook Business 2026-05-30](https://www.outlookbusiness.com/news/zaras-india-fy26-profit-falls-32-to-204-cr-revenue-slips) |
| Singapore, Malaysia, Thailand | No subsidiary in the FY2019 perimeter → **franchise inferred**; partner not confirmed | — | CNMV FY2019 (by absence) |
| Indonesia, Vietnam | Franchise via PT Mitra Adiperkasa (MAP) `[UNVERIFIED — search summary only, page not fetched]` | — | indonesia-investments.com; brandsvietnam.com/10494-ai-dua-zara-ve-viet-nam |
| Philippines | Franchise via SSI Group, which also reportedly runs the Zara e-store `[UNVERIFIED — search summary only]` | — | malaya.com.ph/business-news/ssi-adds-zara-to-e-commerce-site |

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| South Korea | ✅ #10 | ✅ (80% JV) | Gate satisfied by local entity | No |
| Japan | ❌ (<3.28%) | ✅ | N/A | No |
| China | Not measured (zara.cn) | ✅ incl. an e-commerce entity | Gate satisfied | No |
| HK / Macau / Taiwan | ❌ | ✅ | N/A | No |
| Australia / NZ | ❌ | ✅ | N/A | No |
| India | ❌ | ✅ (JV) | Gate satisfied | No |
| SG / MY / TH / ID / VN / PH | ❌ | ⚠️ Franchise, not Inditex | Franchisee's entity, unverified | Not Inditex's question |

**There is no cross-border or regulatory-gate angle at Inditex itself.** Every owned APAC market has a local entity. In the franchise markets the question belongs to the franchisee, not Inditex.

> **MANUAL:** Confirm the named seller in the zara.com/kr, /jp, /au, /in and /sg terms and privacy policies. The storefronts return 403 to automated fetches (Akamai).

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| UK, then "other European markets" — **Zara Pre-Owned marketplace only** | **Stripe** (incl. Stripe Connect for buyer→seller funds) | `[Press Release]` 2023-05-22, fetched | https://stripe.com/newsroom/news/zara-and-stripe |
| Spain — physical store terminals | **BBVA** | `[Third-Party Report]` 2020-09-03, fetched. "con este banco tiene contratado los TPV de las tiendas físicas" | https://www.merca2.es/bizum-bbva-inditex/ |
| Korea (possibly) | NHN KCP | `[Tech Profiler]` via search summary only — `[UNVERIFIED — search summary only, page not fetched]` (wmtips returned 403) | https://www.wmtips.com/technologies/payments/nhn-kcp/ |
| Denmark — Massimo Dutti in-store "Tap to Pay" | Adyen (hint only) | LinkedIn post by an Adyen employee that does not name Adyen as processor — `[UNVERIFIED — search summary only]` | https://nl.linkedin.com/in/odenes |
| Japan online | PayPay (wallet), Apple Pay — methods, not PSPs. Japan gateway/acquirer **not found** (no GMO-PG, SBPS, Veritrans, KOMOJU) | `[Third-Party Report]` | https://pricey.jp/web/articles/5788 |
| India (2017 launch) | Paytm, PayPal — named as methods at launch | `[Third-Party Report]` 2017-10-04 | https://thepaypers.com/ecommerce/zara-launches-ecommerce-shopping-platform-in-india--770275 |

**Searched with no Inditex-specific result:** Adyen (press/case study), Worldpay, Checkout.com, Redsys, Santander, CaixaBank, Cybersource, KG Inicis, Toss Payments, NICE, KSNET, GMO, SB Payment, Veritrans, Razorpay, PayU, Juspay, CCAvenue, 2C2P, Xendit, iPay88, Afterpay, Zip, Klarna. Adyen's public customer lists name Mango and Zalando, not Inditex.

**In-house payment products:**
- **InWallet** (2016): an Inditex-built wallet. Cards are stored in the app, which shows a temporary QR at the till; launched across brands in Spain, described as "developed entirely in-house" ([The Paypers](https://thepaypers.com/mobile-payments/inditex-to-roll-out-inwallet-in-spain--765523); [FashionNetwork](https://us.fashionnetwork.com/news/Payment-inditex-adopts-its-own-dedicated-app,715365.html)) `[UNVERIFIED — search summary only]`. Current status and APAC availability unknown.
- **Inditex Affinity Card**: co-branded card issued by BBVA Consumer Finance (merca2, fetched). Spain.
- **Bizum** (Spanish A2A) added online for Stradivarius, Massimo Dutti and Oysho in 2022, with a group rollout planned ([FashionNetwork](https://id.fashionnetwork.com/news/Inditex-allows-Stradivarius-Massimo-Dutti-and-Oysho-customers-to-pay-with-Bizum,1379686.html)) `[UNVERIFIED — search summary only]`. Shows Inditex adding local rails market by market.
- No "Zara Pay" / "Inditex Pay" product, and no payment-institution or e-money licence, found. The Banco de España register was not checked, so this is "not found", not "confirmed absent".

**Payments owner:** none publicly titled. The closest lead is **José Manuel Romay, Deputy CFO**, described in a 2023 Citi Client Advisory Board booklet as overseeing relationships with card schemes and merchant acquirers `[UNVERIFIED — search summary only; fetch returned 404]` (https://www.citibank.com/tts/sa/flippingbook/2023/2023-Fall-CAB-Welcome-Book/18). The source is from 2023.

#### 3B. Payment Orchestrator

**Classification: None detected** — low confidence.

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with PSP(s), which limits routing optimization, failover capabilities, and multi-acquirer strategies."* — **Qualified:** the second sentence is the template's language. For Inditex the core PSPs themselves are unknown, so "integrates directly" is an inference, not a finding.

- Searches for Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno, "payment orchestration" and "payment routing" returned only vendor directories with no Inditex mention.
- No in-house routing layer found. InWallet is a consumer wallet.
- `[INFERENCE, not confirmed]`: at Inditex's scale and with its in-house engineering culture, an undisclosed internal routing layer is plausible. Do not state either way in outreach.

> **MANUAL:** Walk through zara.com/jp and /kr checkout with DevTools. Look for `checkoutshopper-live.adyen.com`, `js.stripe.com`, `kcp.co.kr` or Japanese gateway domains in the network calls.

---

### Section 4: Alternative & Local Payment Methods

Only South Korea is in the measured top 10 (3.28%); no other APAC market has a traffic figure above 1% to anchor on. The table covers the APAC markets where any evidence was found.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| South Korea | Card via local PG (NHN KCP?) | Cards | Unknown, checkout not accessible | Tech-profiler search summary only |
| South Korea | Naver Pay | Digital wallet | Mentioned in press — **offline merchant** context, 2022 | https://news.mtn.co.kr/news-detail/2022080515324315414 |
| South Korea | KakaoPay, Toss, Samsung Pay, PAYCO, card instalments | Wallets / Instalments | Not found (a PAYCO verification issue appears in an app-review summary, unverified) | — |
| Japan | Visa / MC / Amex / JCB | Cards | Mentioned in docs (third-party guide citing Zara) | https://pricey.jp/web/articles/5788 |
| Japan | PayPay | Digital wallet | Mentioned in docs (third-party) | same |
| Japan | Apple Pay | Digital wallet | Mentioned in docs (third-party) | same |
| Japan | Cash on delivery | Cash | Mentioned in docs (third-party); fee-free | same |
| Japan | Gift card | Stored value | Mentioned in docs (third-party) | same |
| Japan | **Google Pay, Rakuten Pay** | Digital wallet | **Not supported (stated explicitly)** | same |
| Japan | d払い, au PAY, メルペイ, Alipay, WeChat Pay | Digital wallet | **Stores only** — not online | same |
| Japan | Konbini, Paidy, Amazon Pay | Cash / BNPL / wallet | Not found | — |
| Japan | Instalments | BNPL/Instalments | **No Zara-run plan**; split or revolve via the card issuer only | same |
| Australia | PayPal, Visa/MC/Amex | Wallet / Cards | Mentioned in press — **2018 launch only** | https://www.ragtrader.com.au/news/zara-online-everything-you-need-to-know |
| Australia | Afterpay, Zip, Klarna, PayTo | BNPL / A2A | Not found | — |
| India | Paytm, PayPal, cards | Wallet / Cards | Mentioned in press — **2017 pre-launch only** | https://thepaypers.com/ecommerce/zara-launches-ecommerce-shopping-platform-in-india--770275 |
| India | UPI, netbanking, RuPay, EMI, COD | A2A / Instalments | Not found (**unknown — not a sourced gap**) | — |
| Singapore | Cards (± PayPal / Apple Pay / gift card) | Cards / wallet | `[UNVERIFIED — search summary only]` — summaries contradict each other | https://www.zara.com/sg/en/help-center/PaymentMethods |
| China / HK / Macau / Taiwan | Alipay, WeChat Pay, UnionPay, FPS, Octopus, JKOPay, LINE Pay | Wallets | Not found | — |
| MY / TH / PH / ID / VN | FPX, TnG, PromptPay, GCash, QRIS, MoMo… | Local rails | Not found. Franchise-run (ID/VN/PH) | — |

**Warning (Japan, from a third-party source):** *"In Japan, Google Pay and Rakuten Pay are not currently supported by Zara online"*, while Zara's Japanese stores accept d払い, au PAY, メルペイ, Alipay and WeChat Pay. No konbini option was found. Prominence of Rakuten Pay / konbini in Japan was **not** sourced in this run — cite a METI or industry figure before using it in outreach.

No other sourced gaps. Korea, Australia, India and SEA are **unknown**, not gaps.

> **MANUAL:** Use a VPN to check checkout methods on zara.com/kr, /jp and /au. Korea is the only measured APAC market and has zero confirmed methods.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Checkout errors — payment approved by bank, order auto-cancelled or never created | SikayetVar (Zara US pages) | Moderate (~6 similar posts) — **US, out of territory** | Mostly late 2025 `[UNVERIFIED — search summary only]` | https://www.sikayetvar.com/en/zara-us/i-experience-repeated-zara-order-cancellation-after-payment ; https://www.sikayetvar.com/en/zara-us/zara-charged-my-card-without-creating-an-order |
| Duplicate charges, slow refund | SikayetVar (Zara US) | Isolated to moderate — US | Undated `[UNVERIFIED — search summary only]` | https://www.sikayetvar.com/en/zara-us/zara-charged-me-twice-but-didnt-process-my-order-or-refund-my-money |
| Instalment not applied (charged in one payment instead of 6) | SikayetVar | Isolated — market unclear | Undated `[UNVERIFIED]` | https://www.sikayetvar.com/en/zara-us/zara-processed-my-purchase-as-one-payment-instead-of-6-installments |
| Checkout errors ("errores en el proceso de pago"); unable to buy; card refunds 7–9 days | Zara iOS app reviews (mwm.ai aggregator) | Moderate — Spain, out of territory | Jul–Aug 2026 (fetched) | https://mwm.ai/es/apps/zara/547951480 |
| Card option screen missing the bank; PAYCO verification problem | App review (mwm.ai, possibly Korea) | Isolated | Undated `[UNVERIFIED — search summary only]` | https://mwm.ai/de/apps/zara/547951480 |

*"No payment-related complaints found on Reddit, X, Trustpilot, or app store reviews"* **for APAC markets specifically.** The pattern evidence (order created only after a separate failure-prone step; refund delays) is US/Spain and should not be presented as APAC pain.

> *"Pattern of payment-approved-but-order-cancelled in the US suggests a post-authorisation fraud/stock step that voids orders"* — `[INFERENCE, not confirmed]`, and out of territory. Not an outreach angle for APAC.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 2026-09-09/10 | H1 2026: sales €19.76bn (+7.6%; +9.2% constant FX), net profit €2.98bn (+6.8%). Asia & RoW share down 1pt to 15% | Results | https://fashionunited.uk/news/business/inditex-hits-new-high-reports-profit-of-2-98-billion-euros-with-7-6-percent-growth-through-july/2026090990227 |
| 2 | 2026-06-06 | New ~2,000 m², 5-floor Zara flagship at 988 Middle Huaihai Rd, Shanghai; new global store concept; Massimo Dutti flagship planned nearby `[UNVERIFIED — search summary only]` | Market Expansion (format, existing market) | https://insideretail.asia/2026/06/11/zara-opens-flagship-in-shanghai-featuring-new-global-store-concept/ |
| 3 | FY26 (reported 2026-05-30) | India: Trent tendered 94,900 shares in the ITRIPL buyback, stake now **20%**; Zara India revenue ₹2,749.28 cr (−1.1%), profit ₹204.14 cr (−31.9%), 22 stores | M&A / JV restructuring | https://www.outlookbusiness.com/news/zaras-india-fy26-profit-falls-32-to-204-cr-revenue-slips |
| 4 | 2026-04 | Diego Teijeiro, Global Chief Data & Analytics Officer (19 years at Inditex), leaves to become H&M global CIO from 25 May 2026; successor not found `[UNVERIFIED — search summary only]` | Leadership Change | https://fashionunited.com/news/people/spanish-executive-diego-teijeiro-leaves-inditex-to-lead-h-ms-global-technology-division/2026042371959 |
| 5 | 2026-02-22 | Pull&Bear closes its last Singapore store; SG site "currently unavailable for online purchases". Bershka already store-less in SG but still selling online | Market Exit | https://vulcanpost.com/909437/pullbear-to-exit-singapore/ |

*"No public payment-related RFP found."* No job postings mentioning PSP evaluation, payment platform migration or orchestration were found (a manual LinkedIn check of Inditex Tech is recommended). No licence applications found.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 2026-06-12 (updated) | Japan guide: Zara online takes cards, Apple Pay, PayPay, COD, gift card; Google Pay and Rakuten Pay not supported; stores take a much wider QR-wallet set | **High** — the APAC hook | https://pricey.jp/web/articles/5788 |
| 2 | 2023-05-22 | Stripe becomes Zara's payments partner for Zara Pre-Owned | Medium — only named PSP; resale vertical only | https://stripe.com/newsroom/news/zara-and-stripe |
| 3 | 2022-02 | Inditex adds Bizum online for Stradivarius, Massimo Dutti, Oysho; group rollout planned `[UNVERIFIED — search summary only]` | Low (Spain) — shows market-by-market local-rail adds | https://id.fashionnetwork.com/news/Inditex-allows-Stradivarius-Massimo-Dutti-and-Oysho-customers-to-pay-with-Bizum,1379686.html |
| 4 | 2020-09-03 | BBVA holds Inditex's Spanish store terminals and issues the Affinity Card | Low (Spain, dated) | https://www.merca2.es/bizum-bbva-inditex/ |
| 5 | 2016 | InWallet in-app payment launched across Inditex brands in Spain, built in-house `[UNVERIFIED — search summary only]` | Background — in-house build culture | https://thepaypers.com/mobile-payments/inditex-to-roll-out-inwallet-in-spain--765523 |

No provider removals found. No 2025–2026 Inditex payments story in The Paypers, Finextra, PYMNTS or the Spanish press via search.

---

### Section 8: Checkout Experience Audit

**Not accessible in this environment.** *"Full checkout flow not accessible. Findings limited to publicly observable elements."*
- **zara.com and inditex.com return HTTP 403** (Akamai bot protection) to WebFetch, to curl, and to headless Chromium. This is the site's own protection, not the egress proxy — other hosts were reachable. No attempt was made to evade it.

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | Not accessible | — | — |
| Guest checkout | Not accessible | — | — |
| Steps to complete payment | Not accessible | — | — |
| Card input experience | Not accessible | — | — |
| Payment methods visible | JP only, via third-party guide (Section 4) | Fair (JP) | Narrower online than in store |
| Location-based method display | Separate country sub-paths on zara.com | Not assessed | — |
| Instalment / EMI options | JP: no Zara-run instalments (third-party) | Poor (JP) | Japan has a strong instalment culture — not sourced this run |
| 3DS implementation | Not accessible | — | — |
| PCI indicator | Not accessible | — | — |
| Mobile responsiveness | 72.89% of web visits are mobile web; apps excluded | Not assessed | — |
| Multi-currency / local pricing | Country stores in local currency `[INFERENCE, not confirmed]` | Not assessed | — |
| Saved payment methods | InWallet stores cards (Spain, 2016) | Not assessed | — |
| Error message clarity | Spain app reviews cite payment-process errors | Not assessed | — |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found | — |
| Card data handling | Not found | — |
| Recommended Yuno integration | Back-to-back API `[INFERENCE, not confirmed]` — a large in-house engineering organisation with its own wallet and apps is unlikely to take a drop-in SDK | — |

*"No direct PCI compliance documentation found publicly for Inditex (Zara)."* No tokenized-PSP checkout is confirmed in Section 3, so no PCI-scope inference is made.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: Japan's online checkout is narrower than Zara's own Japanese tills**
> **Evidence:** Section 4 — online takes cards, Apple Pay, PayPay, COD and gift cards only; Google Pay and Rakuten Pay explicitly unsupported; d払い / au PAY / メルペイ / Alipay / WeChat Pay are store-only; no konbini or Zara-run instalments found ([pricey.jp](https://pricey.jp/web/articles/5788)). + Section 2 — Zara Japan Corp. is 100% Inditex, so the decision sits inside the group, not with a franchisee. + Section 11A — UNIQLO shows the same store-vs-online gap in five APAC markets.
> **Pain Point:** Japanese shoppers who pay with Rakuten Pay, d払い or au PAY at the till have no way to use them on zara.com/jp, and Android shoppers lose the one-tap wallet iOS users get. Each new Japanese method is a separate integration for a central team in Spain.
> **Yuno Value Proposition:** add Japan's wallets and konbini through one integration alongside whatever PSP runs the card flow today, without a per-method build from Arteixo.
> **Best Success Case:** Reserva (fashion, omnichannel) — closest profile match; LatAm-only, and its figure is unverified. No APAC retail case exists; do not imply one.
> **Outreach Angle:** "Zara's Japanese stores take d払い, au PAY and Alipay; zara.com/jp takes PayPay and Apple Pay and says Google Pay and Rakuten Pay aren't supported. Is closing that gap on the roadmap, or is Japan's online method list owned centrally?"
> **Suggested Subject Line:** Zara Japan: till vs zara.com/jp

> **Insight #2: Korea is the only measured APAC web market, and its payment stack is invisible**
> **Evidence:** Section 1 — Korea is #10 on zara.com (3.28%, ≈3.36M visits/month derived), the only APAC market in the top 10. + Section 2 — Zara Retail Korea is 80/20 with Lotte Shopping. + Section 3A/4 — no confirmed Korean method or PG; NHN KCP is a single unverified tech-profiler signal.
> **Pain Point:** Korean checkout runs through local PGs by necessity (domestic card networks, local easy-pay wallets). If Zara KR runs on one local PG, it has no fallback in its only measured APAC market. `[INFERENCE, not confirmed]` — single-PG status is not evidenced.
> **Yuno Value Proposition:** multi-PG routing and failover in Korea, plus KakaoPay / Naver Pay / Toss coverage through one integration.
> **Best Success Case:** none matching — no Korean retail case found.
> **Outreach Angle:** discovery question, not a claim: "How many PGs sit behind zara.com/kr today, and what happens to checkout when one has an incident?"
> **Suggested Subject Line:** Zara Korea checkout — one PG or two?

> **Insight #3: India just became an Inditex-controlled business, with sales flat and profit down**
> **Evidence:** Section 6 — Trent's stake in Inditex Trent Retail India fell to 20% after a buyback; FY26 revenue −1.1%, profit −31.9% ([Outlook Business](https://www.outlookbusiness.com/news/zaras-india-fy26-profit-falls-32-to-204-cr-revenue-slips)). + Section 4 — the only India payment evidence is the 2017 launch list (Paytm, PayPal, cards); UPI and EMI support is unknown. + Section 2 — the entity is local, so the domestic-acquiring gate is satisfied.
> **Pain Point:** `[INFERENCE, not confirmed]` — with control shifting to Inditex and India underperforming, the checkout built at the 2017 JV launch may come up for review. India runs on UPI and instalments, and the RBI e-mandate and tokenization rules make a global-only stack hard to run.
> **Yuno Value Proposition:** Indian rails (UPI, netbanking, EMI) and local routing through the same layer used elsewhere, rather than a separate India stack.
> **Best Success Case:** none matching in Indian retail.
> **Outreach Angle:** "Trent's stake in Zara India is now 20%. When Inditex takes the operational lead, does India's checkout move onto the central stack, or stay local?" — **verify first** what zara.com/in accepts today.
> **Suggested Subject Line:** Zara India after the buyback

> **Insight #4 (pipeline, not Inditex): the SEA franchise checkouts belong to MAP and SSI**
> **Evidence:** Section 2 — no Inditex subsidiary in SG/MY/TH/ID/VN/PH in the FY2019 perimeter; ID/VN reportedly franchised to Mitra Adiperkasa and PH to SSI Group, which reportedly runs the Zara e-store `[UNVERIFIED]`. + Section 11 — neither MAP nor SSI is in `apac-tal.csv`.
> **Pain Point:** multi-brand franchise operators run many international brands' checkouts across QRIS, VA, GCash and other local rails.
> **Yuno Value Proposition:** one orchestration layer across a franchise portfolio.
> **Outreach Angle:** run `/research` on MAP and SSI separately. Do not pitch Inditex on SEA rails.

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. Zara's Japanese stores take d払い, au PAY, Alipay and WeChat Pay, but zara.com/jp takes cards, Apple Pay and PayPay and says Google Pay and Rakuten Pay aren't supported. *(Third-party source — confirm on zara.com/jp first.)*
2. Korea is the only APAC market in zara.com's top ten, which makes how many PGs sit behind it a fair question.
3. Trent's stake in Zara India is now 20%, so the checkout built at the 2017 launch is now an Inditex decision.

**Cold call openers (conversational, one sentence each):**
1. "Quick one on Japan: your stores take far more wallets than zara.com/jp does — is that a deliberate choice or a backlog item?"
2. "When a Korean PG has an incident, does zara.com/kr fail over, or does checkout just stop?"
3. "With Inditex now holding most of Zara India, is India's checkout moving onto the central stack?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| Fast Retailing (UNIQLO, GU) | fastretailing.com | Japan | ¥3.96tn (≈US$25bn) FY Aug 2026 | JP, KR, CN, HK, TW, SEA, IN, AU | Adyen (2022) + KSNET / KPN / NHN KCP / NHN Commerce (KR), Net Protections (JP), PayPal (AU). No orchestrator | `2-ready-to-outreach/fast-retailing-uniqlo.md`; https://www.adyen.com/press-and-media/adyen-provides-omnichannel-payments-services-to-uniqlo |
| H&M Group | hm.com | Sweden *(out of territory)* | Not sourced | JP, KR, CN, HK, SEA, IN, AU | Klarna global partnership (expanded to RO/HU Mar 2026); Adyen `[UNVERIFIED — search summary only]` | https://www.businesswire.com/news/home/20260323450464/en/Klarna-Expands-Its-Partnership-With-HM-in-Romania-and-Hungary `[UNVERIFIED]` |
| Shein | shein.com | Singapore | ~US$38bn (TAL, unverified) | AU, JP, KR, SEA | Adyen case study (local methods, 3DS2, RevenueAccelerate); Checkout.com MENA case study `[UNVERIFIED — search summary only]`. TAL says Juspay — **no evidence found** | https://www.adyen.com/knowledge-hub/shein-four-payments-strategies-for-global-expansion |
| Mango | mango.com | Spain *(out of territory)* | Not sourced | APAC mostly via franchise | Adyen (customer list) `[UNVERIFIED — search summary only]` | https://hl.co.uk/shares/shares-search-results/a/adyen-ord/company-information |
| Cotton On Group | cottonongroup.com.au | Australia | ~US$2bn (TAL, unverified) | AU, NZ, SG, MY, HK, IN | **Adyen** (2018, fetched): local acquiring in AU, NZ, HK, SG; "convenient single-platform solution" | https://www.adyen.com/press-and-media/cotton-on-group-partners-with-adyen-to-advance-global-ecommerce-rollout |
| MUJI (Ryohin Keikaku) | muji.com | Japan | ~US$4.5bn (TAL, unverified) | JP, CN, HK, TW, KR, SEA, AU | Adyen since 2018 (vendor case study) `[UNVERIFIED — search summary only]` | https://www.adyen.com/knowledge-hub/case-study-muji |
| Zalora (GFG) | zalora.com | Singapore | ~21% of GFG NMV (TAL) | SG, MY, ID, PH, HK, TW | BridgerPay orchestration (vendor story, fetched); TAL: Adyen + Fiuu/Razer | https://bridgerpay.com/learn/bridger-stories/Jyg0jmdNvp2xUmIJedJ4 |

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Love, Bonito | lovebonito.com | Fashion (DTC + stores) | SG, MY, HK, US | Adyen unified commerce since 2018 `[UNVERIFIED]` | https://www.adyen.com/blog/love-bonito-adyen-unified-commerce-for-todays-empowered-shoppers |
| Charles & Keith | charleskeith.com | Fashion accessories | Asia, Middle East | Omnichannel, multi-market; PSP not found | TAL row |
| Pomelo Fashion | pomelofashion.com | Fashion e-commerce | TH, SEA | PSP not found | TAL row |
| Mitra Adiperkasa (MAP) | map.co.id | Multi-brand franchise retail | ID, VN | **Reportedly runs Zara's ID/VN franchise** `[UNVERIFIED]` — owns the SEA checkout Inditex doesn't | search summary only |
| SSI Group | ssigroup.com.ph | Multi-brand franchise retail | PH | **Reportedly runs Zara PH stores and e-store** `[UNVERIFIED]` | search summary only |
| Lotte Shopping | lotteshopping.com | Retail | KR + Asia | 20% partner in Zara Retail Korea (FY2019 accounts) | CNMV FY2019 |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| Zalora | BridgerPay | Conflicting: 2021-11-21 (search summary) vs 2025-11-18 (fetched page). Vendor claim, no Zalora quote | Fashion e-commerce | https://bridgerpay.com/learn/bridger-stories/Jyg0jmdNvp2xUmIJedJ4 |
| Al-Futtaim brands *(out of territory)* | Juspay | 2026-09 `[UNVERIFIED — search summary only]` | Multi-brand retail | https://enterpriseam.com/uae/2026/10/08/juspay-eyes-the-gccs-payment-fragmentation-to-orchestrate-growth/ |

*"No public case studies found of direct competitors adopting payment orchestration"* beyond the unverified Zalora vendor story. The category pattern is **one global PSP (usually Adyen) plus local providers added market by market**.

#### 11D. Prospect Scoring

Verified signals only. Transaction count is not researched for peers and is excluded, so scores are out of 24.

| Company | Orchestration | 3+ countries | Multi-PSP | Rail gap top-3 | Other | Score (/24 excl. txn) | Evidence Source |
|---------|--------------|--------------|-----------|----------------|-------|-----------------------|-----------------|
| Fast Retailing | +4 | +3 | +3 | 0 | +2 (traffic outside home) | 12 (+5 txn = 17 in its own report) | UNIQLO report |
| Cotton On Group | ⬜ 0 | +3 | ⬜ 0 (Adyen only) | ⬜ | ⬜ | 3 | Adyen 2018 |
| Zalora | +1 (BridgerPay, vendor claim) | +3 | +3 (Adyen + Fiuu/Razer per TAL, unverified) | ⬜ | ⬜ | 4–7 | BridgerPay; TAL |
| Shein | ⬜ | +3 | ⬜ (Adyen + Checkout.com, both unverified) | ⬜ | ⬜ | 3 | search summaries |
| MAP | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | Not researched | — |
| SSI Group | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | Not researched | — |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Fast Retailing (UNIQLO) | Direct competitor | JP, KR, SEA, AU, IN | 17/29 | ⭐ | Store-vs-online rail gaps in 5 APAC markets | ✅ (and already researched) |
| 2 | **Mitra Adiperkasa (MAP)** | Franchise operator (Zara ID/VN) | ID, VN | Not scored | **New find** | Runs many international brands' SEA checkouts | ❌ **Not in TAL** |
| 3 | **SSI Group** | Franchise operator (Zara PH) | PH | Not scored | **New find** | Reportedly runs the Zara PH e-store | ❌ **Not in TAL** |
| 4 | Cotton On Group | Direct competitor | AU, NZ, SG, MY, HK | 3 (partial) | — | Adyen single platform (2018) | ✅ (queued in `1-to-outreach/`) |
| 5 | Zalora | Fashion marketplace | SG, MY, ID, PH, HK, TW | 4–7 (partial) | — | Already orchestration-aware (BridgerPay, vendor claim) | ✅ |
| 6 | Shein | Direct competitor | AU, JP, KR, SEA | 3 (partial) | — | Heavy local-method build | ✅ (Juspay label unsupported) |
| 7 | Lotte Shopping | JV partner (Zara KR) | KR + Asia | Not scored | — | 20% of Zara Retail Korea | ✅ |
| 8 | MUJI | Direct competitor | JP, CN, HK, TW, KR | Not scored | — | Adyen (unverified) | ✅ |
| 9 | Love, Bonito | Peer | SG, MY, HK | Not scored | — | Adyen unified commerce (unverified) | ✅ |
| 10 | Charles & Keith | Peer | Asia | Not scored | — | Multi-market omnichannel | ✅ |

**Genuine finds:** MAP and SSI Group are not in `accounts/apac-tal.csv`. Their franchise role for Zara is unverified, but both are large multi-brand APAC retailers in their own right — worth a `/research` run.

**TAL data issues spotted (do not fix from here):** Shein's `Payment Orchestrator = Juspay` has no supporting evidence; Cotton On's `Payment Gateway` could be filled with Adyen (2018 press release); Charles & Keith's HQ is listed as Malaysia (likely Singapore).

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | FY2025 €39.86bn (≈US$46.3bn per FashionUnited), +3.2%; net profit €6.22bn. H1 2026 €19.76bn (+7.6%) | [FashionUnited](https://fashionunited.com/news/business/inditex-posts-6-22-billion-euro-profit-in-2025-and-3-19-percent-sales-growth/2026031171084); [FashionUnited UK](https://fashionunited.uk/news/business/inditex-hits-new-high-reports-profit-of-2-98-billion-euros-with-7-6-percent-growth-through-july/2026090990227) |
| GMV / Gross Transaction Volume | Online sales FY2025 €10.656bn (+4.8%), 26.7% of total | [marketing4ecommerce](https://marketing4ecommerce.net/ventas-online-de-inditex-2025/) |
| APAC revenue | "Asia & rest of world" ≈€5.98bn FY2025; 15% of H1 2026 sales. **Includes non-APAC markets** (Middle East etc.); online not split by region | FashionUnited (both above) |
| Average Transaction Value (USD) | Not found | — |
| Est. Annual Transactions | Not derivable without ATV | — |
| **Monthly transaction count** | ✅ **DERIVED (floor): ≥3.5M online orders/month group-wide.** €10.656bn ÷ 12 = €888m/month ÷ €250 per order (a ceiling I chose — **not a sourced ATV**) ≈ 3.55M. Billing unit: online orders (web + app). In-store POS excluded. **APAC-only: not derivable** — `⚠️ NOT FOUND`. | Online sales from marketing4ecommerce |
| Active Customers / Users | Not found | — |
| Primary Currency | EUR (reporting); local currency per country store | — |
| Top 3 Markets by Revenue | Not disclosed by country. Regions FY2025: Europe ex-Spain 51.3%, Americas 17.8%, Spain 15.9%, Asia & RoW 15.0% `[UNVERIFIED — search summary only]` | sgieurope.com (fetch returned 405) |
| Billing channel split (web vs app store) | Not applicable — Zara is the merchant of record in its apps. Web vs app vs store not disclosed | — |
| Market-level reference | Zara India (ITRIPL) FY26 revenue ₹2,749.28 cr; Zara Retail Korea 2025 revenue ≈₩459.7bn `[UNVERIFIED — search summary only, catch.co.kr]` | Outlook Business (fetched) |

---

### Overall Research Confidence

**Low–Medium.**
- **Traffic: supplied SimilarWeb**, with the caveats above. It covers zara.com only (top 10, share only, no apps, no other brands, no zara.cn). Only one APAC market is measured, so the APAC country profile behind the APM analysis and two ICP signals is mostly unmeasured.
- **Strong:** group financials (fetched trade press citing the CNMV filing), the FY2019 entity perimeter (CNMV filing itself), India JV change (Trent's annual report via Outlook Business), Stripe/Pre-Owned scope.
- **Weak:**
  - **The core PSP stack is unknown in every market.** This is the biggest gap and it holds the score at 10 instead of 17.
  - zara.com blocks all automated access (Akamai), so there are no first-party payment pages, terms or privacy policies, and no checkout audit (Section 8 not accessible). APAC method data rests on one third-party Japanese guide plus 2017/2018 launch coverage.
  - The entity perimeter is from FY2019.
  - No APAC complaints found; competitor stacks rest largely on search summaries.

---

### Manual Research Recommendations

> **Area:** Account ownership (territory)
> **Why it matters:** Inditex is HQ'd in Spain, and payments are almost certainly decided in Arteixo. A parallel EMEA approach would collide.
> **Suggested manual action:** check with the EMEA SDR/AE who owns Inditex before any outreach.

> **Area:** Core PSP / acquirer per market (JP, KR, AU)
> **Why it matters:** it decides the +4 orchestration and +3 multi-PSP awards (10 → 17, 🟢 → ⭐) and the whole pitch.
> **Suggested manual action:** open zara.com/jp, /kr and /au checkout in a real browser with DevTools and record the payment-domain network calls. Read the zara.com/kr privacy policy's "개인정보 처리위탁" (outsourced processing) section, which by Korean practice names the PGs.

> **Area:** Japan method list (the hook)
> **Why it matters:** the hook rests on a third-party guide.
> **Suggested manual action:** open zara.com/jp help-centre "Payment methods" in a browser and screenshot it. Also pull one source on Rakuten Pay / konbini usage in Japanese e-commerce.

> **Area:** Monthly transaction count (APAC-specific)
> **Why it matters:** the gate is safely passed group-wide, but the APAC slice is unknown.
> **Suggested manual action:** check the FY2025 Inditex annual report for online orders or active customers, and any country-level disclosure.

> **Area:** Current entity perimeter and SEA franchise operators
> **Why it matters:** the FY2019 list may be stale; MAP / SSI as franchisees decide whether SEA is an Inditex or a franchisee sale.
> **Suggested manual action:** download the FY2025 annual report's subsidiary annex from static.inditex.com in a browser; confirm the Zara franchisee per SEA market from MAP and SSI annual reports.

> **Area:** Payments owner
> **Why it matters:** no named contact. The Deputy CFO lead is from a 2023 source.
> **Suggested manual action:** LinkedIn search "Inditex payments" / "Inditex Tech pagos" / "Head of Payments Inditex" and confirm José Manuel Romay's current role.

---

### Appendix: All Source URLs

**Section 1:** `accounts/traffic/inditex-zara.md` (SimilarWeb, supplied 2026-10-19)

**Section 2:**
- https://internet.cnmv.es/AUDITA/2020/18378_en.pdf (FY2019 consolidated accounts; fetched)
- https://www.outlookbusiness.com/news/zaras-india-fy26-profit-falls-32-to-204-cr-revenue-slips (fetched)
- https://vulcanpost.com/909437/pullbear-to-exit-singapore/ (fetched)
- indonesia-investments.com; brandsvietnam.com/10494-ai-dua-zara-ve-viet-nam; malaya.com.ph/business-news/ssi-adds-zara-to-e-commerce-site (search summaries only)

**Section 3:**
- https://stripe.com/newsroom/news/zara-and-stripe (fetched)
- https://www.merca2.es/bizum-bbva-inditex/ (fetched)
- https://www.wmtips.com/technologies/payments/nhn-kcp/ (search summary only)
- https://nl.linkedin.com/in/odenes (search summary only)
- https://thepaypers.com/mobile-payments/inditex-to-roll-out-inwallet-in-spain--765523 (search summary only)
- https://us.fashionnetwork.com/news/Payment-inditex-adopts-its-own-dedicated-app,715365.html (search summary only)
- https://id.fashionnetwork.com/news/Inditex-allows-Stradivarius-Massimo-Dutti-and-Oysho-customers-to-pay-with-Bizum,1379686.html (search summary only)
- https://www.citibank.com/tts/sa/flippingbook/2023/2023-Fall-CAB-Welcome-Book/18 (search summary only; 404)

**Section 4:**
- https://pricey.jp/web/articles/5788 (fetched)
- https://news.mtn.co.kr/news-detail/2022080515324315414
- https://www.ragtrader.com.au/news/zara-online-everything-you-need-to-know
- https://thepaypers.com/ecommerce/zara-launches-ecommerce-shopping-platform-in-india--770275
- https://www.zara.com/sg/en/help-center/PaymentMethods (search summary only)

**Section 5:**
- https://www.sikayetvar.com/en/zara-us/i-experience-repeated-zara-order-cancellation-after-payment
- https://www.sikayetvar.com/en/zara-us/zara-charged-my-card-without-creating-an-order
- https://www.sikayetvar.com/en/zara-us/zara-charged-me-twice-but-didnt-process-my-order-or-refund-my-money
- https://www.sikayetvar.com/en/zara-us/zara-processed-my-purchase-as-one-payment-instead-of-6-installments
- https://mwm.ai/es/apps/zara/547951480 (fetched)
- https://mwm.ai/de/apps/zara/547951480

**Sections 6–7:**
- https://fashionunited.uk/news/business/inditex-hits-new-high-reports-profit-of-2-98-billion-euros-with-7-6-percent-growth-through-july/2026090990227 (fetched)
- https://insideretail.asia/2026/06/11/zara-opens-flagship-in-shanghai-featuring-new-global-store-concept/
- https://fashionunited.com/news/people/spanish-executive-diego-teijeiro-leaves-inditex-to-lead-h-ms-global-technology-division/2026042371959

**Section 11:**
- `2-ready-to-outreach/fast-retailing-uniqlo.md`; `accounts/apac-tal.csv`
- https://www.adyen.com/press-and-media/adyen-provides-omnichannel-payments-services-to-uniqlo
- https://www.adyen.com/press-and-media/cotton-on-group-partners-with-adyen-to-advance-global-ecommerce-rollout (fetched)
- https://bridgerpay.com/learn/bridger-stories/Jyg0jmdNvp2xUmIJedJ4 (fetched)
- https://www.adyen.com/knowledge-hub/shein-four-payments-strategies-for-global-expansion
- https://www.adyen.com/knowledge-hub/case-study-muji
- https://www.adyen.com/blog/love-bonito-adyen-unified-commerce-for-todays-empowered-shoppers
- https://hl.co.uk/shares/shares-search-results/a/adyen-ord/company-information
- https://www.businesswire.com/news/home/20260323450464/en/Klarna-Expands-Its-Partnership-With-HM-in-Romania-and-Hungary
- https://enterpriseam.com/uae/2026/10/08/juspay-eyes-the-gccs-payment-fragmentation-to-orchestrate-growth/

**Section 12:**
- https://fashionunited.com/news/business/inditex-posts-6-22-billion-euro-profit-in-2025-and-3-19-percent-sales-growth/2026031171084 (fetched)
- https://marketing4ecommerce.net/ventas-online-de-inditex-2025/ (fetched)
- https://www.sgieurope.com/financial-results/inditex-posts-record-sales-and-profits-in-fy25/120163.article (405)

</details>
