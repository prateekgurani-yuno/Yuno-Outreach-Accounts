# The Peninsula Hotels

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 14 / 29 → 🟢 Medium
**Industry:** Luxury Hotels & Lodging · **HQ:** Hong Kong SAR · **Researched:** 2026-10-09 · **First email sent:** —
**Motion:** Greenfield (vendor-embedded — no orchestration layer, but the room payment surface is owned by Sabre/SynXis)

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** The Peninsula Hotels is the hotel division of The Hongkong and Shanghai Hotels, Limited (HSH), a Hong Kong company incorporated in 1866 and listed on HKEX under stock code 45. It operates 12 luxury hotels — Hong Kong, Shanghai, Beijing, Tokyo, Bangkok, Manila, London, Paris, Istanbul, New York, Chicago and Beverly Hills — totalling **3,106 rooms**, alongside commercial property, the Peak Tram, clubs and a merchandising arm. One consumer domain, `peninsula.com`, feeds a Sabre SynXis booking engine configured **per property, in that property's local currency only**.

**SimilarWeb total visits (last full month):** **819,297** (Sep 2026, ▲9.43% MoM) — source: SimilarWeb (supplied 2026-10-09), top-10 country cut only

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇺🇸 United States | 34.27% · ~280,772 visits | Credit card via SynXis (card capture on `be.synxis.com`); Apple Pay host whitelisted in booking-engine CSP | Not established — booking engine payment step not reachable | ✅ 3 US hotels (NY, Chicago, Beverly Hills); named US entity not found |
| 2 | 🇯🇵 **Japan** | **17.93%** · ~146,900 visits | Credit card via SynXis, **JPY only** (single-currency config, hotel 17695); Japanese site locale (`ja`) live | **Not established.** Konbini exists as a processor rule on their SynXis platform (code `KB`, JPY, 7-day lead) but enablement for Peninsula Tokyo is unverified. No Japanese wallet host (PayPay / LINE Pay / Rakuten Pay / Paidy) appears in the booking engine's CSP — `[INFERENCE, not confirmed]` | ⚠️ Peninsula Tokyo is a consolidated HSH hotel, but no named Japanese legal entity found |
| 3 | 🇭🇰 **Hong Kong** | **9.09%** · ~74,474 visits | Credit card via SynXis, **HKD only** (single-currency config, hotel 12597) | **Not established** — FPS, Octopus, AlipayHK, WeChat Pay HK, PayMe all unverified at checkout | ✅ The Hongkong and Shanghai Hotels, Limited (HKEX: 45), 8/F St George's Building, 2 Ice House Street, Central |
| 6 | 🇮🇳 **India** | **4.40%** · ~36,049 visits | No Peninsula property in India — traffic is **outbound demand**, paying a foreign property cross-border | UPI / RuPay / netbanking / EMI all absent by construction (no Indian acquiring, no Indian property) | ❌ No entity, no property — cross-border by design, not a gap to close |
| 7 | 🇹🇭 **Thailand** | **4.25%** · ~34,820 visits | Credit card via SynXis (Peninsula Bangkok); currency config not fetched | **Not established** — PromptPay, TrueMoney, Thai card instalments unverified | ⚠️ Peninsula Bangkok is a consolidated HSH hotel; named Thai entity not found |

### Legal entities
- **The Hongkong and Shanghai Hotels, Limited** (Hong Kong SAR) — HKEX stock code 45; incorporated in Hong Kong with limited liability; registered office 8/F St George's Building, 2 Ice House Street, Central. Registration number: Not found.
- **The Palace Hotel Ltd** (China Mainland — Beijing) — operator of The Peninsula Beijing, 8 Goldfish Lane, Wangfujing. Registration number: Not found.
- **The Peninsula Shanghai Waitan Hotel Company Limited** (China Mainland — Shanghai) — No. 32, The Bund 32 Zhongshan Dong Yi Road. Registration number: Not found.
- **Peninsula Merchandising (Shenzhen) Company Limited** (China Mainland — Shenzhen) — D16, F/8, Block B, Aerospace Science and Technology Plaza, Nanshan District. Registration number: Not found.
- **Techsembly Pte. Ltd** (Singapore) — not an HSH entity; named in HSH's privacy policy as the operator of the gift-platform API. Included here because it is the commerce platform of record for `gifts.peninsula.com`.

### Known PSPs
- **RECON (RECON Payment Limited, operated by Cityline (Hong Kong) Limited)** — `[Terms/Privacy Policy]` named in Peninsula's own privacy policy, Annex II (China), as the **"e-Payment solution"** receiving "Name and credit card number". Markets: China-facing online channels. RECON self-describes as "a fast-growing PCI-DSS certified online payment gateway in Hong Kong" that integrates "to various payment service providers".
- **Stripe** — `[Source Code]` the public store configuration of `gifts.peninsula.com` carries `stripe_statement_descriptor_suffix: "HSHHQ"`, a Stripe-only API field populated with HSH's own descriptor. Markets: the central gifting / e-commerce line, default currency USD. The publishable key is not exposed in the storefront shell, so Stripe sits server-side.
- **Rooms acquirer / processor: NOT ESTABLISHED.** Card capture for room bookings happens inside the Sabre SynXis booking engine on `be.synxis.com`. Its CSP contains no third-party PSP host and restricts XHR to `'self'` and `*.synxis.com`, so the acquirer is terminated behind Sabre and is not publicly observable. **No acquirer is named here, deliberately.**

### Orchestration status
**None detected — no payment orchestration layer.** No evidence of Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails or Yuno. Equally, no evidence of direct merchant-side PSP integration for rooms: the payment surface is **vendor-embedded** — Sabre SynXis for rooms (`window.synxisBookingEnabled = 'true'` on peninsula.com; hotel IDs passed to `/make-a-booking`), Sabre/Techsembly for gifting, RECON for China online channels. Evidence: peninsula.com page source via Wayback (2026-08-09); `be.synxis.com` live config for hotels 17695 and 12597 (fetched 2026-10-09); HSH privacy policy Annex II (2026-07-11).

### Buying signals
- 🚀 **New strategy published 18 Mar 2026** — CEO Benjamin Vuchot's "PERFORM / TRANSFORM" plan names *"enhancing revenue management, pricing, marketing and distribution, improving productivity at both property and group level"* as the PERFORM agenda. ([HKEX, FY2025 Annual Results](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf))
- 💼 **New CEO since 3 March 2025** — Benjamin Vuchot; FY2025 statement concedes *"we have room for improvement in operational performance"* and *"maintaining the status quo is not an option."* ([same](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf))
- 🔧 **The Peninsula Tokyo renovation planned for 2026** to upgrade *"in-room technology, guestrooms, food and beverage outlets and public areas"* — Japan is the #2 traffic market. ([same](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf))
- 🤝 **Competitive urgency:** Radisson Hotel Group moved to CellPoint Digital payment orchestration explicitly to fix *"each hotel operating as a separate entity using different acquirers and payment methods"* ([CellPoint Digital case study, 2 Sep 2025](https://cellpointdigital.com/articles/casestudies/payment-orchestration-as-a-growth-catalyst-the-radisson-hotel-group-case-study)); Minor Hotels signed Checkout.com on 3 Sep 2026 to consolidate payments across 640 hotels ([Macau Business / PR Newswire](https://macaubusiness.com/minor-hotels-partners-with-checkout-com-to-power-high-performance-payments-across-global-hospitality-60/)).
- 📈 **Hotels division growing:** FY2025 combined hotel revenue HK$6,436m, +13%; H1 2026 HK$3,116m, +10%. ([HKEX FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf) · [HKEX H1 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0805/2026080500241.pdf))

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach the-peninsula-hotels` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 14 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **0** | ⚠️ **NOT FOUND — ASSUMED ~24,000–31,000 room bookings/month.** `[ASSUMPTION — not researched]`. **Billing unit counted: room reservations (folios), not room nights and not guests.** Room nights ARE derivable from two sourced inputs — see Section 12 — giving **~61,025 room nights/month**, but converting room nights to bookings needs average length of stay, which HSH does not publish. At an assumed ALOS of 2.0–2.5 nights that is ~24,400–30,500 bookings/month, which falls in the under-40,000 band. **Per the disclosure rule this assumption does NOT trigger the auto-reject.** Scored at the band it implies: 0 points. Compounding the uncertainty: if rooms settle per property (Section 10, Insight #1), the orchestratable count is the *online direct* subset of that, which is smaller again and entirely unsourced. **Top manual-verification item.** |
| Orchestration status | +4 | ✅ Section 3B: "None detected" — no orchestrator, regional or global, and no in-house layer. Scored +4 on the greenfield rule. **Caveat stated in full:** this greenfield is *vendor-embedded*, not direct-integration greenfield — Sabre owns the room payment surface. That raises the practical cost of inserting orchestration and is reflected in the analyst note below, not in a deflated row. |
| 3+ countries | +3 | ✅ Verified. Section 1 shows 10 countries above 0.8% traffic share, 8 above 2%. Section 2 confirms 4 named legal entities in 2 jurisdictions and 12 operating hotels across 10 countries. ([HKEX FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf) · [privacy policy](https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security)) |
| Multiple PSPs | +3 | ✅ Verified — two named providers with evidence, in two different channels: **RECON / Cityline (Hong Kong)** `[Terms/Privacy Policy]` for China online channels, and **Stripe** `[Source Code]` for the central gifting store. Caveat: the largest line — room acquiring — remains unnamed and unproven. |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **Deliberate zero.** Top-3 markets are US (34.27%), Japan (17.93%) and Hong Kong (9.09%). The payment step of the SynXis booking engine could not be reached, so **no absence can be sourced** for konbini, PayPay, LINE Pay, Rakuten Pay or Paidy in Japan, or for FPS, Octopus or AlipayHK in Hong Kong. "No hits found" is a weak negative and is not scored here. On the licensing limb: entities are confirmed in Hong Kong and China Mainland, so no regulatory acquiring gate is demonstrated either. |
| Recent expansion | 0 | ❌ Not met. No new market entry in the 12 months to 2026-10-09. The FY2025 statement explicitly cites *"a limited development pipeline and elevated leverage that restricts investment capacity."* The Peninsula Yangon remains listed as a property under development (70% owned) in the H1 2026 interim report, with no revenue or valuation attributed. A declared TRANSFORM growth strategy is intent, not expansion. |
| Payment issues | 0 | ❌ Not met. No payment-related complaints found on Reddit, Trustpilot, X, consumer forums or app-store reviews. See Section 5. |
| Funding >$10M | 0 | ❌ Not met. HKEX-listed since long before the window; no equity raise in the last 12 months found. |
| High traffic outside home | +2 | ✅ Verified. Home market Hong Kong is **9.09%** of `peninsula.com` traffic — far below the 60% threshold. (SimilarWeb, supplied 2026-10-09) |
| Competitor using orchestration | +2 | ✅ Verified. Radisson Hotel Group → CellPoint Digital payment orchestration ([case study, 2 Sep 2025](https://cellpointdigital.com/articles/casestudies/payment-orchestration-as-a-growth-catalyst-the-radisson-hotel-group-case-study)); Minor Hotels → Checkout.com ([3 Sep 2026](https://macaubusiness.com/minor-hotels-partners-with-checkout-com-to-power-high-performance-payments-across-global-hospitality-60/)). Both are hotel groups operating in APAC. |
| Payment job postings | 0 | ⬜ Uncertain. HSH's careers site carries current digital and e-commerce roles, but the job-description bodies are JS-rendered and could not be read, and no payment-specific role was confirmed. No points awarded. |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **🟢 Medium (14/29)**

**No public payment-related RFP was confirmed**, so no RFP override applies.

**Analyst note — no tier override applied, but two downgrade pressures are on the record:**
1. **Absolute orchestratable volume is small.** The whole group is 3,106 rooms. Even on the generous assumption, central room-booking volume is tens of thousands per month, not hundreds of thousands, and only the online-direct subset is addressable. A high percentage score on a small absolute base is the classic false positive.
2. **The payment surface is vendor-owned.** For rooms, card capture happens inside Sabre's SynXis booking engine; for gifting, inside Sabre's Techsembly platform. Inserting an orchestrator means either a CRS-level decision or a hosted-payment-page swap in front of SynXis — a longer, more political sale than a merchant that owns its own checkout.
3. **Upward pressure, for balance:** 12 properties, 10 countries, **single-currency booking engines per property** and a per-property Shiji PMS estate is a genuine fragmentation story, and the new CEO has put "distribution" and "group-level productivity" in writing.

> **Re-score trigger:** if discovery confirms that room payment is taken only as a card *guarantee* centrally and settled at property POS, this account should be re-scored to 🔴 Low. If discovery instead reveals a central prepaid-rate programme with meaningful share, it moves up.

### Source Notes
- ✅ `window.synxisBookingEnabled = 'true'` in peninsula.com page source — [Wayback capture 2026-08-09](https://web.archive.org/web/20260809143321/https://www.peninsula.com/en/global-pages/website-conditions-of-use)
- ✅ Per-property single-currency SynXis config (Tokyo JPY / Hong Kong HKD), destination code `PENHTLS` (6823), `chainID: ""` — `be.synxis.com`, fetched 2026-10-09
- ✅ RECON / Cityline (HK) named as e-Payment solution — [HSH privacy policy Annex II, Wayback 2026-07-11](https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security)
- ✅ Stripe statement-descriptor suffix `HSHHQ` on the Peninsula Techsembly store — `gifts.peninsula.com` store config, fetched 2026-10-09
- ✅ Shiji Enterprise Platform PMS live at Beijing, Shanghai, Hong Kong, Istanbul, Tokyo, London — [Shiji press release, 10 Oct 2023](https://www.shijigroup.com/press-news/shijis-enterprise-platform-powers-peninsula-hotels-into-the-future-of-luxury-hospitality)
- ✅ All financials and room counts from HKEX filings, not estimates — [FY2024](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0331/2025033100265.pdf) · [FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf) · [H1 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0805/2026080500241.pdf)
- ⚠️ **The stub's ~$1.4B is the listed parent's FY2024 *combined* revenue (HK$10,991m), of which HK$3,452m was a one-off sale of seven Peninsula London Residences. The hotel division alone was HK$5,681m combined in FY2024 and HK$6,436m in FY2025. Do not use $1.4B for the hotel division.**
- ⚠️ Modirum (3-D Secure vendor) and Apple Pay CDN hosts appear in the booking engine's CSP. CSP presence proves the host is permitted, not that the feature is enabled for Peninsula. Labelled as inference where used.
- ⚠️ Konbini, WeChat, UnionPay, Apple Pay, Google Pay, Installments and Nexi all appear as **i18n string keys** in the SynXis bundle. That is the platform's own resource bundle and proves nothing about Peninsula's enablement. Not treated as evidence of support.
- ⚠️ "A credit card guarantee is required at the time of booking" (Peninsula Bangkok offer page) and "all reservations do not require a deposit, except Luxury in Advance Rates and The Peninsula Suite" (third-party Istanbul listing) are `[UNVERIFIED — search summary only, page not fetched]`. Both source hosts returned 403.
- ⚠️ Near-miss recorded for the record: one peninsula.com legal page (2026-08-09) showed a language selector with **English only**, which would have been read as "no Japanese site". A second page from the same site (2026-07-11) shows the real selector — **en, zh-cn, ja, fr, zh, tr-tr, es, pt, ar, kr, ru**. The English-only selector is a page-level artefact. **peninsula.com IS localised into Japanese.**

### Success Case Alternatives
- **NetEase Games** — multi-market APAC merchant with heavy local-rail dependency across several countries. Match rationale: the structural parallel is many markets, many local acquiring relationships, one brand. *No published metrics exist for this relationship — do not attach a number to it.*
- **Qatar Airways** — high-ticket, multi-currency, cross-border travel merchant where approval rate on a single transaction is a direct revenue number. Match rationale: closest to Peninsula's economics — a single declined HK$30,000 booking is a material loss. *No published metrics exist — do not attach a number.*
- **Best fit for the actual conversation: Qatar Airways.** Same vertical economics (travel, high ticket, cross-border inbound), same argument shape (approval rate on high-value authorisations beats fee reduction), and no claim about hotel-specific PMS integration is implied.

---

## Executive Summary

The Peninsula Hotels is the 12-property, 3,106-room hotel division of HKEX-listed The Hongkong and Shanghai Hotels, Limited (stock code 45). Its single consumer domain, `peninsula.com`, drew 819,297 visits in September 2026, growing 9.43% month-on-month, with an unusually international profile: Hong Kong, the home market, is only 9.09%, while Japan is 17.93% and the United States 34.27%.

**The central payment finding is structural, and it is the thing that decides this account.** Booking is centralised on one brand site feeding a Sabre SynXis booking engine — but SynXis is configured **per property, with exactly one currency per property**: The Peninsula Tokyo (hotel 17695) prices and bills in JPY only; The Peninsula Hong Kong (hotel 12597) in HKD only. The SynXis `chainID` is empty; "The Peninsula Hotels" exists in SynXis only as a *destination* grouping (code `PENHTLS` / 6823), not as a chain-level payment entity. Each property runs its own Shiji Enterprise Platform PMS, and the privacy policy describes the folio as assembled *during the stay*. Card data posts to Sabre's own domain — the booking engine's CSP contains no third-party PSP host and restricts XHR to `'self'` and `*.synxis.com`. **There is therefore no single central card-settlement stack for rooms to orchestrate.** The one line that *is* centrally settled is non-room e-commerce: `gifts.peninsula.com` runs on Techsembly (Spree Commerce, acquired by Sabre in 2023) with a Stripe statement descriptor of `HSHHQ` and a USD default currency.

The motion is therefore **greenfield but vendor-embedded**: no orchestrator anywhere, but the payment surface belongs to Sabre, and the buyer is not a payments owner — it is whoever owns the CRS and PMS estate (HSH's Group General Manager, Technology, named publicly in the Shiji announcement) together with the new CEO's PERFORM agenda on "distribution" and "group-level productivity". The strongest entry point is **not** a rails-gap pitch, because no rails gap could be sourced. It is the per-property local-currency configuration against a 90.91%-foreign demand base.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** Path 1 — **pasted SimilarWeb data supplied by Prateek**, stored at `accounts/traffic/the-peninsula-hotels.md`. Used verbatim; not re-researched. Period: September 2026, one month, Similarweb PRO, Worldwide, all traffic, captured 2026-10-09. **This is a top-10 country cut, not the full country list**, so the APAC total below is a visible floor rather than a complete figure.

**Domains:** one — `peninsula.com`. No corporate/booking split; there is no separate `corporate.` or `investors.` consumer property in the data. Regional variants were checked: no `.co.jp`, `.com.hk`, `.co.in`, `.com.au` or `.co.th` Peninsula consumer domains were found. Localisation is handled by locale path on the single domain (`/ja/`, `/zh-cn/`, `/zh/`, `/fr/`, `/tr-tr/`, `/es/`, `/pt/`, `/ar/`, `/kr/`, `/ru/`).

**Total visits:** 819,297 · **MoM:** ▲ 9.43% (growing) · **Desktop:** 23.29% · **Mobile web:** 76.71%

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | 🇺🇸 United States | 34.27% — **high priority** | ~280,772 | — | SimilarWeb (supplied 2026-10-09) |
| 2 | 🇯🇵 **Japan** | **17.93%** — **high priority** | ~146,900 | — | SimilarWeb (supplied 2026-10-09) |
| 3 | 🇭🇰 **Hong Kong** | **9.09%** — **high priority** | ~74,474 | — | SimilarWeb (supplied 2026-10-09) |
| 4 | 🇫🇷 France | 5.62% — **high priority** | ~46,044 | — | SimilarWeb (supplied 2026-10-09) |
| 5 | 🇬🇧 United Kingdom | 5.02% — **high priority** | ~41,129 | — | SimilarWeb (supplied 2026-10-09) |
| 6 | 🇮🇳 **India** | **4.40%** | ~36,049 | — | SimilarWeb (supplied 2026-10-09) |
| 7 | 🇹🇭 **Thailand** | **4.25%** | ~34,820 | — | SimilarWeb (supplied 2026-10-09) |
| 8 | 🇵🇭 **Philippines** | **3.01%** | ~24,661 | — | SimilarWeb (supplied 2026-10-09) |
| 9 | 🇦🇺 **Australia** | **2.61%** | ~21,384 | — | SimilarWeb (supplied 2026-10-09) |
| 10 | 🇹🇷 Turkey | 0.88% | ~7,210 | — | SimilarWeb (supplied 2026-10-09) |

**APAC visible total: 41.29%** across 6 of the top 10 — Japan, Hong Kong, India, Thailand, Philippines, Australia. Turkey (0.88%) is EMEA and is excluded from every APAC total, per `CLAUDE.md`.

**Top-10 markets with no Peninsula property at all — i.e. pure outbound demand:** 🇮🇳 India (4.40%), 🇦🇺 Australia (2.61%). Both generate card-issuance in a market where HSH has no property and therefore no domestic acquiring need; their transactions are cross-border by construction, paying a JPY-, HKD-, THB- or USD-denominated booking elsewhere.

**Markets with a property but no named entity found:** 🇯🇵 Japan, 🇹🇭 Thailand, 🇵🇭 Philippines, 🇬🇧 United Kingdom, 🇫🇷 France, 🇹🇷 Turkey, 🇺🇸 United States. See Section 2.

**Note on the Japan number.** Japan at 17.93% of site traffic does not mean 17.93% of transactions are Japan-acquired. HSH's own FY2024 commentary says The Peninsula Tokyo's strong year was *"driven by robust international business from US, UK and Hong Kong"* ([HKEX FY2024](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0331/2025033100265.pdf)). Japanese traffic therefore plausibly splits between inbound-to-Tokyo research and Japanese residents booking Peninsula properties abroad — the second of which is a Japan-issued card paying a foreign-acquired, foreign-currency booking. Both readings point at the same corridor problem; neither is sourced to a transaction split.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Hong Kong SAR. 8/F St George's Building, 2 Ice House Street, Central, Hong Kong SAR. Phone +852 2926 2888. The Hongkong and Shanghai Hotels, Limited was **incorporated in 1866** and is listed on The Stock Exchange of Hong Kong under stock code 45. Sources: [HSH privacy policy](https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security) · [HKEX FY2025 Annual Results cover](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf) · [Shiji press release](https://www.shijigroup.com/press-news/shijis-enterprise-platform-powers-peninsula-hotels-into-the-future-of-luxury-hospitality)

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Hong Kong SAR | The Hongkong and Shanghai Hotels, Limited | Not found (HKEX stock code 45) | [HKEX](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf) · [privacy policy](https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security) |
| China Mainland (Beijing) | The Palace Hotel Ltd | Not found | [privacy policy, Annex II](https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security) |
| China Mainland (Shanghai) | The Peninsula Shanghai Waitan Hotel Company Limited | Not found | [privacy policy, Annex II](https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security) |
| China Mainland (Shenzhen) | Peninsula Merchandising (Shenzhen) Company Limited | Not found | [privacy policy, Annex II](https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security) |
| Hong Kong SAR | Peninsula Merchandising; Peninsula Clubs and Consultancy Services; Tai Pan Laundry (group clubs-and-services portfolio) | Not found | [Shiji press release, HSH boilerplate](https://www.shijigroup.com/press-news/shijis-enterprise-platform-powers-peninsula-hotels-into-the-future-of-luxury-hospitality) |
| Japan / Thailand / Philippines / UK / France / Türkiye / USA | **No named entity found.** Peninsula Tokyo, Bangkok, Manila, London, New York and Chicago are consolidated HSH subsidiaries and Paris, Istanbul and Beverly Hills are non-consolidated (associate/JV) hotels, per the FY2024 segment note — so operating entities necessarily exist, but none is named in any source reached. | N/A | [HKEX FY2024, revenue by hotel](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0331/2025033100265.pdf) |

HSH's website terms name the group's operated web properties: `hshgroup.com`, `peninsula.com`, `quaillodge.com`, `zbarchicago.com`, `therepulsebay.com`, `thepeak.com.hk`. The terms are governed by the laws of Hong Kong SAR with exclusive Hong Kong jurisdiction, and carry a separate JAMS arbitration clause for US users. ([website conditions of use, Wayback 2026-08-09](https://web.archive.org/web/20260809143321/https://www.peninsula.com/en/global-pages/website-conditions-of-use))

**Peninsula-operated subdomains confirmed:**
- `gifts.peninsula.com` — live, HTTP 200. Techsembly/Spree gifting and gift-card store. (fetched 2026-10-09)
- `ecom.peninsula.com` — resolves (23.200.156.16), HTTP 200 at root with a 21-byte body, 404 on all probed paths. Whitelisted in the SynXis booking engine's CSP. Purpose not established. (fetched 2026-10-09)
- `edm.peninsula.com` — resolves (203.189.170.84), no HTTPS response. Whitelisted in the SynXis CSP. Email-marketing host `[INFERENCE, not confirmed]`.
- `booking.peninsula.com` — whitelisted in the SynXis CSP as `*.booking.peninsula.com` but does **not** resolve from this environment. Either a wildcard reservation or a host not publicly resolvable.
- `pen10cm.peninsula.com` — resolves to Azure App Service, East Asia region (`waws-prod-hk1-007.eastasia.cloudapp.azure.com`). Referenced in the China annex of the privacy policy. (fetched 2026-10-09)
- `peninsulaboutique.com` — resolves, Cloudflare-protected, HTTP 403 to this environment. A 2016 press release cited in search results attributes the store to **Peninsula Merchandising Limited** `[UNVERIFIED — search summary only, page not fetched]`.

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| 🇺🇸 United States | ✅ #1, 34.27% | ⚠️ 3 hotels, entity not named | Not gated (no source cited; no claim made) | Low — properties are US-domiciled and bill in USD |
| 🇯🇵 Japan | ✅ #2, 17.93% | ⚠️ Peninsula Tokyo consolidated; entity not named | Not established — no current primary source found, so **no regulatory claim is made** | **Medium-High** — SynXis bills Tokyo in JPY only, so non-Japanese cards pay a JPY amount; Japanese cards paying other properties pay a foreign currency |
| 🇭🇰 Hong Kong | ✅ #3, 9.09% | ✅ HSH Ltd, HKEX:45 | Not gated (no source cited) | Low domestically; HKD-only pricing pushes FX onto the 90.91% of visitors who are not in Hong Kong |
| 🇫🇷 France | ✅ #4, 5.62% | ⚠️ Peninsula Paris is non-consolidated; entity not named | Not established | Medium |
| 🇬🇧 United Kingdom | ✅ #5, 5.02% | ⚠️ Peninsula London consolidated; entity not named | Not established | Medium |
| 🇮🇳 India | ✅ #6, 4.40% | ❌ No entity, no property | **Not applicable** — there is nothing to acquire domestically | **High by design** — every Indian transaction is an outbound cross-border card payment to a foreign property |
| 🇹🇭 Thailand | ✅ #7, 4.25% | ⚠️ Peninsula Bangkok consolidated; entity not named | Not established | Medium |
| 🇵🇭 Philippines | ✅ #8, 3.01% | ⚠️ Peninsula Manila consolidated; entity not named. HSH maintains a Philippines-specific privacy annex under RA 10173 | Not established | Medium |
| 🇦🇺 Australia | ✅ #9, 2.61% | ❌ No entity, no property | Not applicable | **High by design** — outbound cross-border only |
| 🇹🇷 Turkey | ✅ #10, 0.88% | ⚠️ Peninsula Istanbul non-consolidated; entity not named. HSH maintains a Türkiye-specific privacy annex under KVKK Law No. 6698 | Not established | Out of territory (EMEA) |

> *"Warning: Potential cross-border operation in Japan. No named Japanese legal entity was found in any source reached, despite The Peninsula Tokyo being a consolidated HSH hotel generating JPY 16.18 billion of revenue in FY2024. Transactions on the Tokyo booking engine are denominated in JPY only, which means every non-Japanese card — including the 34.27% of visitors in the United States — pays an FX-converted JPY amount, with the conversion handled outside any card-scheme cost discussion."*

> *"Warning: Potential cross-border operation in India (4.40%) and Australia (2.61%). There is no Peninsula property and no HSH entity in either market. All transactions from these markets are outbound cross-border, settled against a property in a third country, with higher scheme costs, lower domestic-issuer approval rates and FX exposure. This is structural, not fixable by incorporating locally — it is exactly the corridor case orchestration addresses by routing to the acquirer most likely to approve."*

**No regulatory acquiring gate is asserted for any market in this report.** APAC licensing regimes move too fast to cite from background knowledge, and no current primary source for Japan, Thailand, the Philippines or Hong Kong was reached within budget. This is a gap, not a finding — see Manual Research Recommendations.

> **MANUAL:** Verify the Japanese, Thai and Philippine operating entities on each country's registry and in the booking-flow terms for those properties. In APAC the billing entity is very often named in the rate terms and nowhere else — and for this account the billing entity *is* the question.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| China Mainland (online channels) | **RECON** — RECON Payment Limited, operated by **Cityline (Hong Kong) Limited**. Described in Peninsula's own privacy policy as the **"e-Payment solution"** SDK, collecting "Name and credit card number" | `[Terms/Privacy Policy]` | [HSH privacy policy, Annex II – China, SDK table](https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security) |
| Hong Kong (vendor profile, corroborating) | RECON self-describes as *"a fast-growing PCI-DSS certified online payment gateway in Hong Kong"* that integrates *"to various payment service providers to accept a wide range of payment methods including but not limited to credit/debit cards, e-wallet pay, local and China payments"*; merchant portal at `recon.cityline.com` | `[Developer Docs]` / vendor site | [reconpayment.com](https://www.reconpayment.com/) |
| Global (gifting / non-room e-commerce) | **Stripe** — `gifts.peninsula.com` public store configuration carries `stripe_statement_descriptor_suffix: "HSHHQ"`, a Stripe-only API field, populated with HSH's own descriptor. `stripeKey`, `stripeStandardAccountId`, `adyenOriginKey` and `payPalId` are all null or empty in the storefront shell, so the live key sits server-side | `[Source Code]` | `https://gifts.peninsula.com/checkout` (fetched 2026-10-09) |
| Global (rooms — the biggest line) | **NOT ESTABLISHED.** Card capture occurs inside the Sabre SynXis booking engine. The engine's CSP contains **no third-party PSP host**, and `connect-src` falls back to a `default-src` of `'self' *.synxis.com` plus marketing hosts — so card data posts to Sabre's own domain and the acquirer is terminated server-side behind SynXis, per hotel. **No acquirer is named.** | `[Source Code]` (negative) | `https://be.synxis.com/?hotel=17695` and `?hotel=12597` response headers (fetched 2026-10-09) |
| Global (3-D Secure) | **Modirum** — `*.modirum.com` is whitelisted in `script-src`, `child-src`, `worker-src` and `default-src` of the SynXis booking engine. Modirum is an EMV 3-D Secure vendor. CSP presence shows the host is permitted, not that it is invoked for Peninsula specifically | `[Source Code]` | `https://be.synxis.com/?hotel=17695` CSP header (fetched 2026-10-09) |
| Global (wallet) | **Apple Pay** — `*.cdn-apple.com` whitelisted in the SynXis CSP. Same caveat: permitted, not proven enabled | `[Source Code]` | `https://be.synxis.com/?hotel=17695` CSP header (fetched 2026-10-09) |
| Global (ancillary fintech) | **Hopper Technology Solutions** — `fintech-portal.hts.hopper.com` and its staging host are whitelisted in the SynXis CSP; a `sensibleWeatherGuaranteeProductId` field exists in the engine state. Both are SynXis platform features; neither is shown as enabled for Peninsula | `[Source Code]` | `https://be.synxis.com/?hotel=17695` (fetched 2026-10-09) |

**Platform and systems of record (not PSPs, but they determine where payment can live):**

| Layer | Vendor | Evidence | Source |
|---|---|---|---|
| Booking engine / CRS | **Sabre Hospitality — SynXis.** `window.synxisBookingEnabled = 'true'` is set as a global on peninsula.com; booking links carry SynXis hotel IDs (`/ja/make-a-booking?...&hotel=17695`); `be.synxis.com?hotel=17695` returns a live engine titled **ザ・ペニンシュラ東京**; `be.synxis.com?hotel=12597` returns **The Peninsula Hong Kong**. Destination `PENHTLS` / id `6823` = "The Peninsula Hotels". `*.sabrehospitality.com`, `*.asc.sabre.com` and `*.synxis-gcp.com` are in the engine's CSP | `[Source Code]` | [peninsula.com source, Wayback 2026-08-09](https://web.archive.org/web/20260809143321/https://www.peninsula.com/en/global-pages/website-conditions-of-use) · `be.synxis.com` (fetched 2026-10-09) |
| PMS (per property) | **Shiji Enterprise Platform.** Live at The Peninsula Beijing, Shanghai, Hong Kong, Istanbul, Tokyo and London as of October 2023, following a 7-year joint "HSH One PMS" project; a 25-year Shiji–HSH relationship. HSH's Group General Manager, Technology is quoted by name (Michael Garcia) | `[Press Release]` | [Shiji, 10 Oct 2023](https://www.shijigroup.com/press-news/shijis-enterprise-platform-powers-peninsula-hotels-into-the-future-of-luxury-hospitality) |
| Gifting / retail e-commerce | **Techsembly** (Spree Commerce). `cdn-saas.techsembly.com`, `static.techsembly.com`, `saas-storefront-an.techsembly.com`; `_glo_spree_session` cookie; store id `542`, store code "Peninsula Hotels", created 2023-03-13, default currency USD, iframe payment step (600×400), `checkoutFlow: v1`. Named in HSH's privacy policy as **Techsembly Pte. Ltd**, "Gift platform API" | `[Source Code]` + `[Terms/Privacy Policy]` | `https://gifts.peninsula.com/` (fetched 2026-10-09) · [privacy policy](https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security) |
| Ownership link | **Sabre acquired Techsembly in July 2023**, folding its marketplace and gift-card capability into SynXis Retail Studio. So Sabre owns *both* Peninsula's room booking engine and its gifting commerce platform | `[Press Release]` | [TTG Asia, 7 Jul 2023](https://www.ttgasia.com/2023/07/07/sabre-deepens-tech-expertise-with-techsembly-acquisition/) |
| F&B reservations | **TableCheck Inc.** — named in HSH's privacy policy as the "Food and Beverage Table Booking Engine"; `www.tablecheck.com` referenced in the Japanese Tokyo page source | `[Terms/Privacy Policy]` + `[Source Code]` | [privacy policy](https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security) |
| Spa reservations | **CPS Graphics, Inc. dba Tambourine** and **Shiji Concept Online Spa** — two separate spa booking engines named side by side in the privacy policy | `[Terms/Privacy Policy]` | [privacy policy](https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security) |
| Guest management / CRM | **TravelClick (Amadeus Hospitality)**; **Sinobase Marketing Technology Corporation**; **Shanghai JINGdigital Co., Ltd.**; **Beijing Shiji Information Technology Co., Ltd.** (WeChat order management for room reservations) | `[Terms/Privacy Policy]` | [privacy policy](https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security) |
| Customer support (gifting) | `peninsula@avenhospitality.com` — Aven Hospitality is the support contact configured on the Peninsula Techsembly store | `[Source Code]` | `https://gifts.peninsula.com/` store config (fetched 2026-10-09) |
| Distribution / metasearch | DerbySoft (`*.derbysoftca.com`, `*.derbysoftsec.com`, `*.derbyclick.com`), Triptease, The Hotels Network, Trivago, TripAdvisor, Sojern — all in the SynXis CSP | `[Source Code]` | `https://be.synxis.com/?hotel=17695` (fetched 2026-10-09) |

**Counted and discounted — substring false positives checked in context, not reported as hits:** `"VI"`, `"AX"`, `"MC"`, `"CA"`, `"DC"`, `"CU"`, `"UP"` all appeared in the SynXis page but every single occurrence was a **country or US/Indian state code** (Virgin Islands, Åland Islands, Monaco, Canada, District of Columbia, Cuba, Uttar Pradesh), not a card-brand code. No accepted-card-brand list could be extracted. Likewise `stripe` and `adyen` appear in the Techsembly **platform** bundle (`assets/adyen-*.js`, `checkout_stripe-auth` chunk) while the Peninsula store's own keys are null — platform capability, not merchant configuration.

#### 3B. Payment Orchestrator

**Classification: None detected — no payment orchestration layer.**

> *"No public evidence found of a payment orchestration platform. Searches against Juspay, Spreedly, Primer, Gr4vy, CellPoint Digital, APEXX, Payrails and Yuno returned nothing for this merchant. Equally, no merchant-side direct PSP integration was found for rooms: the company does not appear to own its own card checkout at all. Payment is terminated inside third-party platforms — Sabre SynXis for rooms, Sabre/Techsembly (Stripe) for gifting, RECON/Cityline for China online channels — which limits routing optimization, failover capabilities and multi-acquirer strategies, and means the company has no single place today where a routing decision could be made."*

The `Payment Gateway` and `Payment Orchestrator` columns of `accounts/apac-tal.csv` are both **empty** for this row. That is consistent with the finding, but an empty column is not evidence; the classification above rests on the source-code and privacy-policy evidence in 3A.

**What this does to the motion.** This is greenfield for orchestration, but it is *vendor-embedded* greenfield rather than *direct-integration* greenfield. The practical consequence: the opening is not "you need orchestration" and not "you have no orchestration layer" — it is "your payment configuration is a per-property artefact of a CRS decision, and it is costing you on a 90.91%-foreign demand base."

> **MANUAL:** Walk through `be.synxis.com?hotel=17695` to the payment step with DevTools open and capture the network requests at card entry. That single step resolves the acquirer question, the accepted-card-brand list, the Japanese APM list and whether a deposit or only a guarantee is taken. It is the highest-value manual action in this file.

---

### Section 4: Alternative & Local Payment Methods

For every country in Section 1 above 1% traffic share, checked against `.claude/reference/apac-payments.md` §2. **The booking engine's payment step is behind a live booking session and could not be reached from this environment**, so most rows below are honestly "Unknown, checkout not accessible". That is the finding; it is not padded.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| Global (rooms) | Credit/debit card | Cards | **Active in checkout** — the SynXis engine state carries `CreditCard`, `CreditCardExpiration`, `guaranteedWithCreditCard`, `paymentMethodToGuaranteeYourRoom` and `NumberYearsCreditCardExpiration: 10` | `be.synxis.com?hotel=17695` (fetched 2026-10-09) |
| Global (rooms) | Apple Pay | Digital wallet | **Unknown** — `*.cdn-apple.com` permitted by CSP; enablement not shown | `be.synxis.com?hotel=17695` CSP (2026-10-09) |
| Global (rooms) | Google Pay | Digital wallet | **Unknown, checkout not accessible** — i18n keys exist in the platform bundle only | `be.synxis.com?hotel=17695` (2026-10-09) |
| Global (rooms) | 3-D Secure | Cards | **Unknown** — Modirum (a 3DS vendor) permitted by CSP; version and enablement not shown | `be.synxis.com?hotel=17695` CSP (2026-10-09) |
| 🇯🇵 Japan | **Konbini** (convenience-store cash) | Cash/voucher | **Available on the platform; enablement NOT established.** The SynXis engine's `paymentProcessorRules` includes `"KB": [{RequiredCurrencyCode: ["JPY"]}, {MinimumLeadDays: "7"}]` — a konbini processor rule requiring JPY and a 7-day lead. These are **platform-level** rules, not hotel-level enablement | `be.synxis.com?hotel=17695` (2026-10-09) |
| 🇯🇵 Japan | PayPay | Digital wallet | **Not found / unknown.** No PayPay host in the booking engine's CSP, and no merchant source names it. `[INFERENCE, not confirmed]`: a Japanese wallet generally requires its own host in `script-src` or `frame-src`, and none is present — but the CSP has no `connect-src` and no `form-action` directive, so this is suggestive, not conclusive | `be.synxis.com?hotel=17695` CSP (2026-10-09) |
| 🇯🇵 Japan | LINE Pay / Rakuten Pay / Paidy | Digital wallet / BNPL | **Not found / unknown.** Same evidence basis and same caveat as PayPay | `be.synxis.com?hotel=17695` CSP (2026-10-09) |
| 🇯🇵 Japan | Card instalments / bonus payment | BNPL/Instalments | **Unknown, checkout not accessible.** `Installments`, `installmentAmount` and `guaranteedWithNexi` exist as i18n keys in the platform bundle. Platform capability only | `be.synxis.com?hotel=17695` (2026-10-09) |
| 🇯🇵 Japan | Multi-currency presentment | — | **Confirmed ABSENT.** The Tokyo engine's currency array has exactly one entry: `{"CurrencyCode":"JPY","DecimalPlaces":0,"Default":true,"Name":"日本円","RateOfExchange":"158.0796055108"}`. **JPY only** | `be.synxis.com?hotel=17695` (2026-10-09) |
| 🇭🇰 Hong Kong | FPS / Octopus / AlipayHK / WeChat Pay HK / PayMe | A2A, wallet | **Unknown, checkout not accessible.** None appears in the booking engine's CSP. RECON (the one named provider) advertises "e-wallet pay, local and China payments" generically, but is scoped in the privacy policy to China channels, not Hong Kong consumer rooms | `be.synxis.com?hotel=12597` (2026-10-09) · [reconpayment.com](https://www.reconpayment.com/) |
| 🇭🇰 Hong Kong | Multi-currency presentment | — | **Confirmed ABSENT.** The Hong Kong engine's currency array has exactly one entry: `{"CurrencyCode":"HKD","DecimalPlaces":2,"Default":true,"Name":"Hong Kong Dollars","RateOfExchange":"7.8478418751"}`. **HKD only** | `be.synxis.com?hotel=12597` (2026-10-09) |
| 🇨🇳 China Mainland | Alipay / WeChat Pay / UnionPay | Wallet / cards | **Unknown.** `*.weixin.qq.com`, `*.wechat.com`, `*.baidu.com`, `*.mediav.com` and `*.360.cn` are whitelisted in the SynXis CSP, but as marketing and tracking hosts, not payment SDKs. RECON is confirmed as the e-payment solution for China online channels and advertises China payments — but no specific rail is named for Peninsula | `be.synxis.com?hotel=17695` CSP · [privacy policy](https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security) |
| 🇹🇭 Thailand | PromptPay / TrueMoney / Thai instalments | A2A / wallet / instalments | **Unknown, checkout not accessible** | — |
| 🇵🇭 Philippines | GCash / Maya / InstaPay / OTC | Wallet / A2A / cash | **Unknown, checkout not accessible** | — |
| 🇦🇺 Australia | PayTo / BPAY / Afterpay / Zip | A2A / BNPL | **Not applicable to domestic acquiring** — no Australian property. Relevant only if Australian cards were to be offered local methods on an outbound booking | — |
| 🇮🇳 India | UPI / RuPay / netbanking / EMI | A2A / cards / instalments | **Not applicable to domestic acquiring** — no Indian property or entity. Indian demand is outbound cross-border | — |
| Global (gifting) | Credit/debit card via Stripe, iframe payment step, USD default | Cards | **Active in checkout** `[INFERENCE from configuration, not a completed purchase]` — Stripe statement descriptor `HSHHQ` set; iframe 600×400; `checkoutFlow: v1` | `https://gifts.peninsula.com/checkout` (2026-10-09) |
| Global (gifting) | Gift cards / stored value | Stored value | **Active** — `gift-card-balance` and `ts-gift-card-balance` components present; `givex_multi_currency: false` flag present (Givex is a stored-value platform; the flag is off and the gateway is not confirmed) | `https://gifts.peninsula.com/checkout` (2026-10-09) |
| Global (gifting) | PayPal / Adyen | Wallet / cards | **Not configured for this store.** `payPalId: null`, `adyenOriginKey: ""` in the Peninsula store settings, even though the Techsembly platform bundle ships both | `https://gifts.peninsula.com/checkout` (2026-10-09) |

> *"Warning: In Japan — 17.93% of all site traffic and the group's #2 market — The Peninsula Tokyo's booking engine prices and bills in JPY and nothing else. We could NOT source the absence of konbini, PayPay, LINE Pay, Rakuten Pay or Paidy, and we are not claiming it. What we can state from the merchant's own engine is that the konbini processor rule exists on the SynXis platform Peninsula already runs, with a JPY requirement and a 7-day minimum lead. Whether it is switched on for Tokyo is the single question to ask on the call."*

> **MANUAL:** Use a Japan and a Hong Kong VPN exit and complete the booking flow to the payment step on `be.synxis.com?hotel=17695` and `?hotel=12597`. Record the exact method list, whether a deposit or only a guarantee is requested, and whether the method list changes by issuer country.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| — | — | — | — | — |

*No payment-related complaints found on Reddit, X, Trustpilot, or app store reviews.* Searches covering duplicate charges, declined cards, refund delays, deposits and pre-authorisation holds returned only generic hotel-industry material and cases involving other brands and OTAs. **No public information found** specific to The Peninsula Hotels.

This is a genuine negative, and for a 3,106-room luxury group with a largely assisted, high-touch booking journey it is unsurprising. It also means the "payment issues" ICP signal scores zero and the complaint-pattern route into the conversation is not available for this account.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 2026-08-05 | **H1 2026 interim results.** Hotels division combined revenue HK$3,116m, +10% year-on-year (group subsidiaries HK$2,699m + associates/JV effective share HK$417m). Group combined revenue excluding residence sales HK$3,951m, +8%. HK$395m of Peninsula London Residences sales recognised in the half | Financial results | [HKEX](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0805/2026080500241.pdf) |
| 2 | 2026-08-05 | **Q2 2026 operating statistics.** RevPAR: Greater China HK$3,108 (+27%), Europe HK$8,606 (+10%), USA HK$6,189 (+14%), Asia excluding Greater China HK$2,569 (−9%). Asia-ex-China is the only region down | Operating statistics | [HKEX](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0805/2026080500261.pdf) |
| 3 | 2026-03-18 | **FY2025 annual results and new strategy.** CEO Benjamin Vuchot (joined 3 March 2025) sets out "PERFORM / TRANSFORM". PERFORM explicitly includes *"enhancing revenue management, pricing, marketing and distribution, improving productivity at both property and group level"*. The statement concedes *"a limited development pipeline and elevated leverage that restricts investment capacity"* and *"we have room for improvement in operational performance… maintaining the status quo is not an option"* | Leadership / strategy | [HKEX](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf) |
| 4 | 2026-03-18 | **The Peninsula Tokyo renovation planned for 2026** — *"to upgrade in-room technology, guestrooms, food and beverage outlets and public areas."* Also flagged: plans to enhance The Peninsula Hong Kong ahead of its 100th anniversary in 2028, and *"selective extensions of The Peninsula brand into adjacent experiences"* | Capital programme | [HKEX](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf) |
| 5 | 2023-10-10 | **Shiji Enterprise Platform PMS deployed** across Peninsula Beijing, Shanghai, Hong Kong, Istanbul, Tokyo and London, out of a 7-year joint "HSH One PMS" project and a 25-year Shiji–HSH relationship. HSH's Group General Manager, Technology quoted by name (Michael Garcia) | Tech / Conference signal | [Shiji](https://www.shijigroup.com/press-news/shijis-enterprise-platform-powers-peninsula-hotels-into-the-future-of-luxury-hospitality) |
| 6 | 2023-07-07 | **Sabre acquires Techsembly**, Peninsula's gifting-commerce platform, to fold its marketplace and gift-card capability into SynXis Retail Studio — consolidating Peninsula's room and non-room digital commerce under one vendor | M&A (supplier) | [TTG Asia](https://www.ttgasia.com/2023/07/07/sabre-deepens-tech-expertise-with-techsembly-acquisition/) |

**Public payment RFP:** *No public payment-related RFP found.*

**Payment-related hiring:** Not confirmed. HSH's careers site (`careers.hshgroup.com`) carries current digital and e-commerce roles — including an Assistant Manager, Digital Product and Content in Hong Kong whose listing was returned in search results — but the job-description bodies are JavaScript-rendered and could not be read from this environment, and no posting mentioning PSP evaluation, payment platform migration or orchestration was confirmed. A separate search result refers to an appointment of a Director of eCommerce and Digital Marketing, undated in the result and therefore not usable `[UNVERIFIED — search summary only, page not fetched]`.

**Licence applications:** None found.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 2026-09-03 | **Minor Hotels partners with Checkout.com** to consolidate payments across 640+ hotels in 67 countries, citing *"AI-powered payment optimization… to improve acceptance rates"* and *"a global payments partner with local acquiring… to reduce lost revenue from failed payments."* Announced from Singapore | **Direct APAC peer.** Minor is Bangkok-HQ'd, operates luxury brands, and has just made exactly the decision Peninsula has not | [Macau Business / PR Newswire](https://macaubusiness.com/minor-hotels-partners-with-checkout-com-to-power-high-performance-payments-across-global-hospitality-60/) |
| 2 | 2025-09-02 | **Radisson Hotel Group adopts CellPoint Digital payment orchestration.** The stated problem is Peninsula's problem verbatim: *"a complex web of property management systems, with each hotel operating as a separate entity using different acquirers and payment methods. The fragmented payment landscape had become a barrier to both operational efficiency and guest satisfaction."* Delivered via a branded hosted payment page in 20+ languages, multi-acquirer intelligent routing and failover, and unified reconciliation across owned, managed and franchised properties | **The single best competitive artefact in this file.** A hotel group publicly describing per-property acquiring as a barrier and solving it with orchestration | [CellPoint Digital](https://cellpointdigital.com/articles/casestudies/payment-orchestration-as-a-growth-catalyst-the-radisson-hotel-group-case-study) |
| 3 | 2021-08 | **Adyen and Shiji Payment Solutions partner** on a hospitality integration combining payments with property management and point-of-sale systems | Peninsula runs the Shiji Enterprise Platform. A payment path through Shiji therefore **exists as a vendor capability** — but there is **no evidence whatsoever** that Peninsula uses it, and none is claimed here | [Adyen](https://www.adyen.com/zh_CN/press-and-media/adyen-shiji-partner-to-streamline-hospitality-payments) |

*No provider removals found.* No evidence that The Peninsula Hotels has added, changed or dropped a payment provider at any point. The absence of any payment news for this merchant over a multi-year window is itself consistent with payment being a vendor-default rather than a managed programme.

---

### Section 8: Checkout Experience Audit

**Partial.** The brand site `peninsula.com`, the boutique site `peninsulaboutique.com` and the HSH corporate site `hshgroup.com` all return HTTP 403 with a Cloudflare bot challenge (`cf-mitigated: challenge`) to this environment. The `/en/make-a-booking` page was additionally behind Imperva at its last archived capture. **The payment step of the room booking flow was not reachable and the findings below are limited to publicly observable elements** — the live SynXis booking engine shell (which *is* reachable at `be.synxis.com`), the Techsembly gifting storefront (reachable), and archived page source.

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type — rooms | **Third-party hosted, per property.** Sitecore-built brand site (`/layouts/system/VisitorIdentification.js`) with `window.synxisBookingEnabled = 'true'`; booking links hand a SynXis hotel ID to `/make-a-booking`; the engine is a React SPA on `be.synxis.com` (build `825001754`, host region 03) | Fair | Hosted by Sabre, not by Peninsula. Peninsula does not own this surface |
| Checkout type — gifting | **Third-party hosted SaaS.** Techsembly on Spree Commerce; Angular SPA served from `saas-storefront-an.techsembly.com`; payment in a 600×400 iframe | Fair | Separate platform, separate merchant descriptor (`HSHHQ`), separate currency default (USD) |
| Guest checkout | **Rooms: yes.** The engine exposes `signUpProfileDetails`, `isCreateProfileSelected: false` and a "My Peninsula" profile path, but account creation is optional. **Gifting: yes** — `/signin-signup` exists alongside `/cart` and `/checkout` | Good | — |
| Steps to complete payment | Not accessible — payment step behind a live session | — | A 2016 press release claims the boutique completes purchase "within three steps" `[UNVERIFIED — search summary only, page not fetched]` |
| Card input experience | **Rooms: card fields rendered by the SynXis SPA and posted to Sabre's own domain.** The engine's CSP has no third-party PSP host, and `connect-src` falls back to `default-src 'self' *.synxis.com`. **Gifting: iframe** (`iframe_width: 600px`, `iframe_height: 400px`) with a `success-iframe` component and a `stripe-auth` chunk | Fair | For rooms, Sabre is in the card path. Note the CSP declares **no `form-action` directive at all**, so form posts are unrestricted — a weaker posture than `form-action 'self'` |
| Payment methods visible | Not accessible. No accepted-card-brand list could be extracted; every apparent brand code in the page was a country or state code | — | See Section 4 |
| Location-based method display | Not accessible. The engine does carry a full `countryDetailList` and locale support | — | The site itself is localised into 11 languages: en, zh-cn, ja, fr, zh, tr-tr, es, pt, ar, kr, ru |
| Instalment / EMI options | Not accessible. `Installments`, `installmentAmount` and `guaranteedWithNexi` exist as platform i18n keys only | — | Japan, Thailand and Taiwan are the markets where this would matter |
| 3DS implementation | **Not detected directly.** Modirum (a 3DS vendor) is whitelisted in the engine's CSP across `script-src`, `child-src`, `worker-src` and `default-src`. Version not determinable | — | `[INFERENCE, not confirmed]`: 3DS is handled inside SynXis via Modirum rather than by a merchant-side PSP SDK |
| PCI indicator | **Rooms: card data posts to a Sabre domain**, so Peninsula's room-booking PCI scope is plausibly SAQ A-EP-like rather than full scope. **Gifting: iframe** → SAQ A-like. Neither is documented | — | See Section 9 |
| Mobile responsiveness | **76.71% of traffic is mobile web** (SimilarWeb, supplied 2026-10-09). The SynXis engine carries explicit mobile state (`selectedMobile`) and the brand site has mobile-specific nav | — | Not testable without rendering. Given three-quarters of demand is mobile, this is a material untested dimension |
| Multi-currency / local pricing | **Confirmed single-currency per property.** Tokyo: JPY only (0 decimal places, RateOfExchange 158.0796055108). Hong Kong: HKD only (2 decimal places, RateOfExchange 7.8478418751). `chainID` is empty; the brand appears only as destination `PENHTLS` / `6823`. Gifting store: `currency_selection_mode: "default_mode"`, default USD | **Poor** — for a merchant whose home market is 9.09% of its traffic | **This is the most important observable finding in the audit** |
| Saved payment methods | Rooms: `walletPaymentVerified` and `cardInfo` fields exist in profile state; behaviour not observable. Gifting: not observable | — | — |
| Error message clarity | Not accessible | — | — |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **Not found** for The Peninsula Hotels or HSH. No merchant level, attestation or compliance statement located | — |
| Third-party PCI claim | **RECON** — Peninsula's named China-channel payment provider — self-describes as *"a fast-growing PCI-DSS certified online payment gateway in Hong Kong."* This is RECON's claim about RECON, not about Peninsula | [reconpayment.com](https://www.reconpayment.com/) |
| Card data handling — rooms | **Not found** as a documented statement. Observed: card fields are rendered by the SynXis SPA and the engine's CSP restricts XHR to `'self'` and `*.synxis.com`, with no third-party PSP host | `be.synxis.com?hotel=17695` (2026-10-09) |
| Card data handling — gifting | **Not found** as a documented statement. Observed: a 600×400 payment iframe plus a Stripe-auth component | `https://gifts.peninsula.com/checkout` (2026-10-09) |
| Security posture note | The Shiji announcement states the platform *"ensures that customer data remains secure and compliant with the strictest privacy regulations"* — a vendor marketing claim with no standard named | [Shiji](https://www.shijigroup.com/press-news/shijis-enterprise-platform-powers-peninsula-hotels-into-the-future-of-luxury-hospitality) |
| Recommended Yuno integration | **Not determinable without the acquirer answer.** If rooms settle per property through Sabre, the realistic first integration is the **gifting/e-commerce line via SDK** (Peninsula already controls that merchant relationship — descriptor `HSHHQ`, Stripe, USD) plus a **hosted-payment-page swap in front of SynXis** on the Radisson pattern. A back-to-back API integration on rooms presumes a central card path that is not established | — |

*No direct PCI compliance documentation found publicly for The Peninsula Hotels.*

> `[INFERENCE, not confirmed]`: Because card capture for rooms occurs on a Sabre domain and for gifting inside an iframe, Peninsula's own PCI scope is likely reduced in both channels, with the processors handling card data. No compliance level is asserted.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: There is no central card-settlement stack for rooms — and that is the whole account.**
> **Evidence:** **Section 3A/3B** — the SynXis booking engine is configured per property with exactly one currency each (Tokyo `hotel=17695` → JPY only; Hong Kong `hotel=12597` → HKD only), `chainID` is empty, and the brand exists in SynXis only as destination `PENHTLS`/`6823`; card data posts to `*.synxis.com` with no third-party PSP host in the CSP ([`be.synxis.com`, fetched 2026-10-09]). Plus **Section 6** — the Shiji Enterprise Platform PMS runs per property, live at Beijing, Shanghai, Hong Kong, Istanbul, Tokyo and London, out of HSH's own "One PMS" project ([Shiji, 10 Oct 2023](https://www.shijigroup.com/press-news/shijis-enterprise-platform-powers-peninsula-hotels-into-the-future-of-luxury-hospitality)). Plus **Section 2** — the privacy policy describes the folio as assembled *"during your stay"* and names separate per-property controller entities ([privacy policy, 2026-07-11](https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security)).
> **Pain Point:** Twelve hotels in ten countries, each with its own currency configuration, its own PMS instance and — by necessary implication — its own acquiring relationship. No single view of approval rate, decline reason, chargeback rate or cost of acceptance across the portfolio. Nowhere to make a routing decision. No failover when one country's acquirer degrades. Reconciliation is twelve exercises, not one. This is the exact condition Radisson published as its reason for buying orchestration.
> **Yuno Value Proposition:** A single orchestration layer in front of the existing per-property acquirers — keeping local acquiring where it earns a better approval rate, adding a second acquirer per market for failover, and consolidating reporting and reconciliation into one place without ripping out Shiji or SynXis. Orchestration here is additive to the vendor stack, not a replacement for it.
> **Best Success Case:** **Qatar Airways** — the closest profile match on economics, not on vertical plumbing: high-ticket, multi-currency, cross-border travel bookings where a single declined authorisation is a direct and large revenue loss. *(No published metrics exist for this relationship — do not attach a number.)*
> **Outreach Angle:** Your Tokyo booking engine quotes in JPY and nothing else; your Hong Kong engine quotes in HKD and nothing else. With 90.91% of peninsula.com traffic coming from outside Hong Kong, almost every booking is a foreign card against a local-currency, locally-acquired amount — and there is no single place in your stack where that corridor can be measured, let alone optimised.
> **Suggested Subject Line:** Twelve hotels, twelve currencies, one question about approval rates

> **Insight #2: Japan is 17.93% of demand against a JPY-only engine — and the konbini rail is already sitting unused on the platform you run.**
> **Evidence:** **Section 1** — Japan is the #2 market at 17.93% (~146,900 visits/month), second only to the US, and well ahead of home-market Hong Kong at 9.09% (SimilarWeb, supplied 2026-10-09). Plus **Section 4** — the Tokyo engine's currency array has one entry, JPY, with an embedded rate of exchange of 158.0796, and the SynXis `paymentProcessorRules` object carries `"KB": [{RequiredCurrencyCode: ["JPY"]}, {MinimumLeadDays: "7"}]` — a konbini processor rule, present on the platform Peninsula already licenses ([`be.synxis.com?hotel=17695`, 2026-10-09]). Plus **Section 6** — a Tokyo renovation is planned for 2026 explicitly covering *"in-room technology"* ([HKEX FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf)).
> **Pain Point:** Two distinct problems sit on the same number. Inbound: non-Japanese cards are charged an FX-converted JPY amount by a Japanese acquirer, which is where issuer declines on foreign-acquired transactions concentrate. Outbound: Japanese residents browsing Peninsula properties abroad are presented a foreign currency and a card-only flow on a market where cash-at-konbini and wallet rails carry real volume. **Neither the konbini gap nor the PayPay gap is proven** — but the group has a 2026 Tokyo technology programme already funded, which is the moment to find out.
> **Yuno Value Proposition:** Per-market method and routing configuration that can turn on a Japanese cash or wallet rail for Japanese issuers without changing the brand site, and route Japan-issued cards to the acquirer with the best observed approval rate per corridor — rather than whichever acquirer the Tokyo property happens to hold.
> **Best Success Case:** **NetEase Games** — a multi-market APAC merchant whose business depends on per-country rail coverage rather than a single global card flow. *(No published metrics exist — do not attach a number.)*
> **Outreach Angle:** Japan is your second-largest source of web demand at 17.93% — bigger than Hong Kong — and your Tokyo engine prices in JPY only. Worth knowing whether the konbini option your CRS already supports is switched on, before the 2026 Tokyo technology work locks in.
> **Suggested Subject Line:** Japan is 17.93% of peninsula.com — a question before the Tokyo refit

> **Insight #3: You already run a central, single-currency, Stripe-settled commerce line — it just isn't the rooms.**
> **Evidence:** **Section 3A** — `gifts.peninsula.com` runs on Techsembly (Spree Commerce), store id 542, created 2023-03-13, with `stripe_statement_descriptor_suffix: "HSHHQ"` and a USD default currency; `payPalId` and `adyenOriginKey` are null and empty (fetched 2026-10-09). Plus **Section 6** — Sabre acquired Techsembly in July 2023 and is folding it into SynXis Retail Studio ([TTG Asia](https://www.ttgasia.com/2023/07/07/sabre-deepens-tech-expertise-with-techsembly-acquisition/)), so the same vendor now holds both the room and non-room commerce surfaces. Plus **Section 3A** — the privacy policy additionally names four more transacting or near-transacting platforms: Techsembly (gifts), TableCheck (F&B), Tambourine and Shiji Concept (two separate spa engines), and RECON (China e-payment) ([privacy policy, 2026-07-11](https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security)).
> **Pain Point:** The non-room revenue lines each sit on their own stack: gifting on Stripe in USD under an HSH HQ descriptor, F&B on TableCheck, spa on *two* different engines, China online channels on RECON. A guest's room, dinner, spa treatment and gift purchase can hit four different merchant records in three currencies. For a group whose PERFORM agenda names *"ancillary"* growth and group-level productivity, that fragmentation is a measurable tax — and unlike the rooms question, Peninsula clearly owns the gifting merchant relationship outright, which makes it the shortest path to a first integration.
> **Yuno Value Proposition:** Consolidate the non-room lines — gifting, retail, spa, F&B deposits, vouchers — behind one orchestration layer with one reporting surface and shared tokenisation, then extend the same layer in front of rooms once the acquiring picture is mapped. A land-and-expand that does not require a CRS decision to start.
> **Best Success Case:** **Garena** — a multi-storefront APAC merchant where the value was consolidating separate commerce surfaces rather than fixing one checkout. *(No published metrics exist — do not attach a number.)*
> **Outreach Angle:** Your gift store settles centrally in USD under an HSH HQ descriptor, while your rooms settle per property in local currency, and your spa bookings run on two different engines. Four revenue lines, four merchant records — worth a look at what that costs you in reconciliation alone.
> **Suggested Subject Line:** Gifting settles centrally, rooms don't — is that deliberate?

> **Insight #4: Two hotel groups solved this in public in the last 13 months. Both of them compete with you in Asia.**
> **Evidence:** **Section 7** — Radisson Hotel Group adopted CellPoint Digital orchestration on 2 Sep 2025, publishing a problem statement that matches Peninsula's structure exactly: *"each hotel operating as a separate entity using different acquirers and payment methods"* ([CellPoint Digital](https://cellpointdigital.com/articles/casestudies/payment-orchestration-as-a-growth-catalyst-the-radisson-hotel-group-case-study)); Minor Hotels signed Checkout.com on 3 Sep 2026 to consolidate payments across 640+ hotels in 67 countries, citing acceptance-rate improvement and local acquiring ([Macau Business / PR Newswire](https://macaubusiness.com/minor-hotels-partners-with-checkout-com-to-power-high-performance-payments-across-global-hospitality-60/)). Plus **Section 3B** — Peninsula has no orchestration layer of any kind and no merchant-owned checkout for rooms.
> **Pain Point:** The competitive gap is no longer theoretical. Radisson has a branded hosted payment page in 20+ languages, multi-acquirer intelligent routing and unified reconciliation across owned, managed and franchised properties. Minor — Bangkok-HQ'd, luxury-brand operator, Peninsula's regional peer set — has just bought the same capability. Peninsula's engine still quotes one currency per hotel. Meanwhile Q2 2026 RevPAR in Asia excluding Greater China was **down 9%** year-on-year, the only region to decline ([HKEX Q2 2026 operating statistics](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0805/2026080500261.pdf)) — conversion is worth more when rate growth stalls.
> **Yuno Value Proposition:** The same capability set Radisson bought — hosted payment page, multi-acquirer routing, failover, unified reconciliation — delivered with genuinely global APM coverage across the ten countries Peninsula actually operates in, rather than a regional footprint.
> **Best Success Case:** **Qatar Airways** — for the approval-rate-as-revenue argument on high-ticket cross-border bookings, which is where a luxury hotel's conversion economics actually live. *(No published metrics exist — do not attach a number.)*
> **Outreach Angle:** Radisson published its reason for moving to orchestration last September: every hotel a separate entity with a different acquirer. Minor signed Checkout.com this September. Your Asia-ex-China RevPAR was down 9% in Q2 — conversion is the cheapest lever you have left.
> **Suggested Subject Line:** What Radisson published about per-property acquirers

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. Your Tokyo booking engine quotes in JPY and nothing else, your Hong Kong engine in HKD and nothing else — yet 90.91% of peninsula.com's 819,297 September visits came from outside Hong Kong.
2. Japan is your second-biggest source of web demand at 17.93%, ahead of your home market, and the konbini payment rule is already sitting in the CRS configuration you license — I just can't tell from outside whether it's switched on.
3. Radisson published, in September 2025, that its payment problem was "each hotel operating as a separate entity using different acquirers and payment methods"; Minor Hotels signed Checkout.com twelve months later — and your Asia-ex-China RevPAR was down 9% in Q2 2026.

**Cold call openers (conversational, one sentence each):**
1. "Quick structural question — when someone books The Peninsula Tokyo on peninsula.com, does the card settle in Japan against the Tokyo entity, or centrally in Hong Kong? Because the booking engine only quotes JPY, which suggests the former."
2. "Your gift store settles centrally in USD under an HSH HQ descriptor, but rooms look like they settle per property in local currency — is that a deliberate split or just how the CRS was set up?"
3. "Asia-ex-China was your only region with RevPAR down in Q2 — when rate growth stalls, how much visibility do you have into what you're losing at the authorisation step across the twelve properties?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors (5–8 companies)

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| Mandarin Oriental Hotel Group | mandarinoriental.com | Hong Kong SAR | Not found | HK, Japan, Thailand, China, UK, France, US | **Not found** — searches returned nothing | Searched; no result |
| Shangri-La Group | shangri-la.com | Hong Kong SAR | Not found | HK, China, Japan, Thailand, Philippines, Australia, UK | **Not found** | Searched; no result |
| Rosewood Hotel Group | rosewoodhotels.com | Hong Kong SAR | Not found | HK, China, Thailand, UK, France, US | **Not found** | Searched; no result |
| Swire Hotels (The House Collective, EAST) | swirehotels.com | Hong Kong SAR | 2 brands | HK, China, UK, US | **Adyen** — reported as Swire Hotels' payments partner, covering more payment options, tokenisation and unified commerce. `[UNVERIFIED — search summary only, page not fetched; hoteltechreport.com returned HTTP 403]` | [Hotel Tech Report](https://hoteltechreport.com/news/swire-hotels-partners-adyen) |
| Minor Hotels (incl. Anantara) | minorhotels.com | Thailand | 640+ hotels, 67 countries | Thailand, China, Australia, UK, Middle East, Europe | **Checkout.com** — confirmed, announced 3 Sep 2026 | [Macau Business / PR Newswire](https://macaubusiness.com/minor-hotels-partners-with-checkout-com-to-power-high-performance-payments-across-global-hospitality-60/) |
| Four Seasons Hotels and Resorts | fourseasons.com | Canada | Not found | Japan, HK, Thailand, Philippines, Australia, US, Europe | **Not found** | Searched; no result |
| Aman Resorts | aman.com | Switzerland / Thailand ops | Not found | Japan, Thailand, China, Philippines | **Not found** | Searched; no result |
| Okura Nikko Hotels | okura-nikko.com | Japan | Not found | Japan, China, Taiwan, SEA | **Not found** | Searched; no result |

#### 11B. Industry Peers / Same Vertical (5–8 companies)

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Radisson Hotel Group | radissonhotels.com | Hotels (mid-to-upscale) | EMEA, APAC, 100+ countries | **The reference case.** Publicly described per-property acquiring as a barrier and bought orchestration to fix it | [CellPoint Digital](https://cellpointdigital.com/articles/casestudies/payment-orchestration-as-a-growth-catalyst-the-radisson-hotel-group-case-study) |
| Frasers Hospitality | frasershospitality.com | Serviced apartments / hotels | Singapore, Malaysia, Australia, Europe | Adyen partnership covering APAC and Europe, with PMS integration cited. `[UNVERIFIED — search summary only, page not fetched]` | [Serviced Apartment News](https://servicedapartmentnews.com/news/technology/frasers-hospitality-adyen/) |
| Anantara Siam Bangkok (Minor property) | anantara.com | Luxury hotel, single property | Thailand | 2C2P QuickPay payment links — a Thai PSP at property level, illustrating exactly the per-property pattern | [casestudies.com / 2C2P](https://www.casestudies.com/company/2c2p/case-study/anantara-siam-bangkok-boosts-transactions-500-in-3-months-with-2c2p) |
| Seibu Prince Hotels Worldwide | princehotels.com | Hotels | Japan, Taiwan, global | Adopted Sabre SynXis CRS, Booking Engine and Channel Connect — the same CRS stack Peninsula runs, in Peninsula's #2 market | [Hospitality Net](https://www.hospitalitynet.org/news/4120196.html) |
| Quail Lodge & Golf Club (HSH-owned) | quaillodge.com | Resort / golf club | USA | An HSH-operated property on its **own domain**, outside peninsula.com — a separate commerce surface inside the same group | [HSH website terms](https://web.archive.org/web/20260809143321/https://www.peninsula.com/en/global-pages/website-conditions-of-use) |
| The Repulse Bay / The Peak (HSH) | therepulsebay.com, thepeak.com.hk | Commercial property, attraction | Hong Kong | Two more HSH-operated domains with their own transaction flows; Peak Tram, Retail & Others was HK$1,024m of FY2025 revenue | [HSH website terms](https://web.archive.org/web/20260809143321/https://www.peninsula.com/en/global-pages/website-conditions-of-use) · [HKEX FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf) |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| Radisson Hotel Group | **CellPoint Digital** (payment orchestration platform) | 2025-09-02 | Hotels | [CellPoint Digital](https://cellpointdigital.com/articles/casestudies/payment-orchestration-as-a-growth-catalyst-the-radisson-hotel-group-case-study) |
| Minor Hotels | **Checkout.com** (consolidated global acquiring + acceptance optimisation; not labelled "orchestration" but functionally the consolidation play) | 2026-09-03 | Hotels (incl. luxury) | [Macau Business / PR Newswire](https://macaubusiness.com/minor-hotels-partners-with-checkout-com-to-power-high-performance-payments-across-global-hospitality-60/) |
| Swire Hotels | **Adyen** (unified commerce + tokenisation) | Date not established | Hotels (Hong Kong luxury) | [Hotel Tech Report](https://hoteltechreport.com/news/swire-hotels-partners-adyen) — `[UNVERIFIED — search summary only, page not fetched]` |

*No public case studies found of Mandarin Oriental, Shangri-La, Rosewood, Four Seasons, Aman or Okura adopting payment orchestration.* Notably, **not one of Peninsula's Hong Kong-HQ'd direct luxury competitors has a publicly disclosed payment stack** — which means the competitive-urgency argument has to be carried by Radisson and Minor, not by a same-tier luxury peer.

#### 11D. Prospect Scoring

Applied to **Minor Hotels** (Bangkok, Thailand) — the strongest APAC prospect surfaced, though note the Checkout.com signing changes the motion to competitive displacement:

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| Monthly transaction count | 0 | ⚠️ Not researched for this prospect | — |
| Orchestration status | +1 | ✅ Global competitor incumbent — Checkout.com signed 2026-09-03 | [Macau Business](https://macaubusiness.com/minor-hotels-partners-with-checkout-com-to-power-high-performance-payments-across-global-hospitality-60/) |
| 3+ countries | +3 | ✅ 67 countries stated | [same](https://macaubusiness.com/minor-hotels-partners-with-checkout-com-to-power-high-performance-payments-across-global-hospitality-60/) |
| Multiple PSPs | +3 | ✅ Checkout.com group-wide + 2C2P at Anantara Siam Bangkok property level | [same](https://macaubusiness.com/minor-hotels-partners-with-checkout-com-to-power-high-performance-payments-across-global-hospitality-60/) · [2C2P case study](https://www.casestudies.com/company/2c2p/case-study/anantara-siam-bangkok-boosts-transactions-500-in-3-months-with-2c2p) |
| Local rail gap in top-3 market | 0 | ⬜ Not researched | — |
| Recent expansion | 0 | ⬜ Not researched | — |
| Payment issues | 0 | ⬜ Not researched | — |
| Funding >$10M | 0 | ⬜ Not researched | — |
| High traffic outside home | 0 | ⬜ Not researched — no traffic data pulled | — |
| Competitor using orchestration | +2 | ✅ Radisson/CellPoint in the same vertical | [CellPoint Digital](https://cellpointdigital.com/articles/casestudies/payment-orchestration-as-a-growth-catalyst-the-radisson-hotel-group-case-study) |
| Payment job postings | 0 | ⬜ Not researched | — |
| **Partial total** | **9 / 29** | Floor only — six rows unresearched | — |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Minor Hotels | Direct competitor / peer | Thailand, China, Australia, Europe, Middle East | 9/29 (partial floor) | 🟢 Medium | Consolidating payments group-wide; Checkout.com incumbent since Sep 2026 → displacement motion | ❌ **Not on the list — genuine find** |
| 2 | Mandarin Oriental Hotel Group | Direct competitor | HK, Japan, Thailand, China, UK, France, US | Not scored | 🟢 Medium | HK-HQ'd luxury peer, same per-property structure likely, **no disclosed payment stack** | ❌ **Not on the list — genuine find** |
| 3 | Shangri-La Group | Direct competitor | HK, China, Japan, Thailand, Philippines, Australia | Not scored | 🟢 Medium | HK-HQ'd, far wider APAC footprint than Peninsula, no disclosed stack | ❌ **Not on the list — genuine find** |
| 4 | Rosewood Hotel Group | Direct competitor | HK, China, Thailand, UK, France, US | Not scored | 🟢 Medium | HK-HQ'd luxury, growing fast, no disclosed stack | ❌ **Not on the list — genuine find** |
| 5 | Okura Nikko Hotels | Industry peer | Japan, China, Taiwan, SEA | Not scored | 🟢 Medium | Japan-HQ'd chain — the konbini/PayPay/instalment thesis is testable on a domestic Japanese operator | ❌ **Not on the list — genuine find** |
| 6 | Seibu Prince Hotels Worldwide | Industry peer | Japan, Taiwan, global | Not scored | 🟢 Medium | Runs the same Sabre SynXis stack as Peninsula — reusable discovery | ❌ **Not on the list — genuine find** |
| 7 | Frasers Hospitality | Industry peer | Singapore, Malaysia, Australia, Europe | Not scored | 🔴 Low | Adyen incumbent → competitive motion, smaller ticket | ❌ Not on the list |
| 8 | Aman Resorts | Direct competitor | Japan, Thailand, China, Philippines | Not scored | 🔴 Low | Very high ticket, very low volume — likely below the transaction floor | ❌ Not on the list |
| 9 | Swire Hotels | Direct competitor | HK, China, UK, US | Not scored | 🔴 Low | Adyen incumbent; small portfolio | ❌ Not on the list |
| 10 | Four Seasons Hotels and Resorts | Direct competitor | Global incl. all APAC | Not scored | 🔴 Low | Canada-HQ'd — would route to the Americas team, not APAC | ❌ Not on the list |

**Cross-check against `accounts/apac-tal.csv`:** **none** of the ten appear on the target account list. The list currently carries The Peninsula Hotels as the only luxury hotel group of this type in the Hong Kong batch. **Mandarin Oriental, Shangri-La and Rosewood are all Hong Kong-headquartered luxury hotel groups with larger APAC footprints than Peninsula and no disclosed payment stack — they are the most obvious additions, and they are missing.**

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) — **listed parent, HSH** | **FY2025: HK$7,978m consolidated / HK$8,784m combined** ≈ **US$1.02bn / US$1.12bn** at the 7.8478 HKD:USD rate embedded in Peninsula's own Hong Kong booking engine. FY2024: HK$10,290m consolidated / HK$10,991m combined ≈ US$1.31bn / US$1.40bn. The year-on-year fall of 20% is almost entirely the drop in one-off Peninsula London Residences sales, from HK$3,452m to HK$395m | Audited, HKEX-filed. [FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf) · [FY2024](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0331/2025033100265.pdf) |
| Annual Revenue — **hotels division only** | **FY2025: HK$5,630m (group subsidiaries) / HK$6,436m (combined, incl. associates & JV effective share), +13%.** FY2024: HK$4,980m / HK$5,681m, +19%. H1 2026: HK$2,699m / HK$3,116m, +10% | [FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf) · [H1 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0805/2026080500241.pdf) |
| **Correction to the target list** | **`accounts/apac-tal.csv` carries "~$1.4B (HSH FY24)". That matches HSH's FY2024 *combined* revenue of HK$10,991m, but it is the listed parent's figure and HK$3,452m of it was a one-off sale of seven London residences. The hotel division was HK$5,681m combined in FY2024 (≈US$724m) and HK$6,436m in FY2025 (≈US$820m). Do not use $1.4B for the hotel business.** | Derived from the two HKEX segment notes above |
| Revenue by hotel (FY2024, HK$m) | Hong Kong 1,069 (+3%) · Tokyo 826 (+11% HKD, **+21% local currency, JPY 16.18bn**) · London 856 (+562%) · Chicago 654 (+6%) · New York 650 (−15%) · Beijing 324 (−1%) · Bangkok 237 (+14%) · Manila 228 (+2%). Non-consolidated: Paris 800 · Beverly Hills 628 · Shanghai 459 · Istanbul 372 | [HKEX FY2024, Hotels Division table](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0331/2025033100265.pdf) |
| Revenue by geography (FY2025, HK$m combined) | Greater China 3,315 · (full table not extracted for the other three regions) · FY2024: Greater China 3,161 · Other Asia 1,365 · US 1,693 · Europe 4,772 | [FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf) · [FY2024](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0331/2025033100265.pdf) |
| **Room count** | **3,106 rooms total** — Greater China 765 · Europe 567 · USA 751 · Asia excluding Greater China 1,023 | ✅ SOURCED. [HKEX FY2025 Annual Results, Operational Review](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf) |
| Occupancy (FY2025) | Greater China 65% (2024: 58%) · Europe 57% (52%) · USA 68% (65%) · Asia ex-GC 66% (59%) | ✅ SOURCED, same filing |
| Average Room Rate (FY2025, HK$) | Greater China 4,053 · Europe 12,584 · USA 7,889 · Asia ex-GC 3,958 | ✅ SOURCED, same filing |
| RevPAR (FY2025, HK$) | Greater China 2,644 · Europe 7,151 · USA 5,394 · Asia ex-GC 2,624. Q2 2026: Greater China 3,108 (+27%) · Europe 8,606 (+10%) · USA 6,189 (+14%) · **Asia ex-GC 2,569 (−9%)** | ✅ SOURCED. [FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf) · [Q2 2026 operating statistics](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0805/2026080500261.pdf) |
| Average Transaction Value (USD) | **Not published.** Approximate per-night room value by region, from ARR above at 7.8478 HKD:USD: Greater China ~US$516 · Europe ~US$1,604 · USA ~US$1,005 · Asia ex-GC ~US$504. **Folio value per stay is higher (room + F&B + spa + arcade) and is not published.** | Derived from sourced ARR; flagged as a per-night room figure, not a transaction value |
| **Room nights sold (DERIVED)** | ✅ **DERIVED: ~732,300 room nights FY2025 ≈ 61,025 room nights/month.** Arithmetic, both inputs sourced from the same HKEX filing: Greater China 765 × 365 × 0.65 = 181,496; Europe 567 × 365 × 0.57 = 117,964; USA 751 × 365 × 0.68 = 186,398; Asia ex-GC 1,023 × 365 × 0.66 = 246,441. Total 732,299 | ✅ Both inputs audited and sourced. [HKEX FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf) |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ~24,000–31,000 bookings/month. `[ASSUMPTION — not researched.]`** **Billing unit counted: room reservations (folios), not room nights and not guests.** Basis: the DERIVED ~61,025 room nights/month above divided by an **assumed** average length of stay of 2.0–2.5 nights, typical for urban luxury hotels. **HSH does not publish average length of stay, so the divisor is unsourced and the output is an assumption, not a derivation, however careful the arithmetic.** Two further honest caveats: **(a)** if rooms settle per property (Section 10, Insight #1), the count that matters for a central orchestration deal is the *online-direct, centrally-charged* subset of these bookings, which is smaller again and entirely unsourced; **(b)** total group card volume including property F&B covers across nine-plus restaurants per hotel, spa, arcade retail, gifting and the Peak Tram is materially higher, but most of it is card-present POS at the property, which orchestration does not address, and no figure for any of it is published. **This assumption does NOT trigger the under-40,000 auto-reject.** | See the mandatory disclosure rule in the ICP matrix. Room-night inputs: [HKEX FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf). ALOS: **no source** |
| GMV / Gross Transaction Volume | Not published separately from revenue | — |
| Active Customers / Users | Not found. "My Peninsula", "Peninsula Perfect Companion" and "Mobile PenKey Concierge" account programmes are named in the privacy policy; no membership numbers published | [privacy policy](https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security) |
| Primary Currency | **Reporting: HKD.** **Transacting: one local currency per property** — confirmed JPY for Tokyo, HKD for Hong Kong. Gifting store default: USD | `be.synxis.com?hotel=17695` and `?hotel=12597`, `gifts.peninsula.com` (all fetched 2026-10-09) |
| Top 3 Markets by Revenue | By geographical segment FY2024 combined: **Europe HK$4,772m** (inflated by HK$3,452m of residence sales), **Greater China HK$3,161m**, **US HK$1,693m**, Other Asia HK$1,365m. Excluding residence sales, **Greater China is the largest** | [HKEX FY2024](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0331/2025033100265.pdf) |
| Billing channel split (web vs app store) | **Not applicable and not a risk here.** This is not an app-store business; there is no IAP exposure. The relevant split is **direct web vs OTA vs assisted/voice**, and it is **not published** — which matters, because the OTA share is volume that never touches Peninsula's own payment stack at all. DerbySoft, Triptease, The Hotels Network, Trivago and TripAdvisor all appear in the booking engine's CSP, confirming heavy third-party distribution | `be.synxis.com?hotel=17695` CSP (2026-10-09) |
| Net result (context for the sale) | FY2024: loss attributable to shareholders HK$943m. FY2025: profit HK$320m, underlying profit HK$105m, **no final dividend declared**. H1 2026: profit HK$23m vs a HK$289m loss a year earlier. FY2025 statement cites *"elevated leverage that restricts investment capacity"* | [FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf) · The Standard figures corroborate but were not independently fetched |

**Business case implication, stated plainly:** the sizing here is weak and the report says so. The hotel division is a real, growing, US$800m+ revenue business, but it is only 3,106 rooms, the transaction count is assumed rather than measured, and the share that is centrally settled is unknown. **Business case sizing requires a discovery call**, and the first question on it is not about volume — it is about where the card settles.

---

### Overall Research Confidence

**Medium.**

**Strong coverage:**
- **Financials (Section 12)** — exceptionally strong. Three audited HKEX filings fetched and parsed directly: FY2024 annual results, FY2025 annual results and H1 2026 interim results, plus Q2 2026 operating statistics. Segment revenue, per-property revenue, room counts, occupancy, ARR and RevPAR are all sourced primary figures, not estimates. This corrected a material error in the target list.
- **Platform and systems of record (Section 3A)** — strong. The Sabre SynXis booking engine was reached **live** for two properties and its configuration read directly; the Techsembly gifting store was reached live and its store configuration read directly; the PMS is confirmed by a dated vendor press release; five further transacting platforms are named in the merchant's own privacy policy.
- **The structural settlement question (Section 10, Insight #1)** — strong for a question that usually cannot be answered from outside. Per-property single-currency configuration, empty `chainID`, per-property PMS, per-property controller entities and a card path that terminates on Sabre's domain are four independent lines of evidence pointing the same way.
- **Competitive intelligence (Sections 7 and 11C)** — strong. Two dated, fetched, primary case studies.

**Limited coverage, and why:**
- **Section 8 (Checkout Experience Audit) is partial.** `peninsula.com`, `peninsulaboutique.com` and `hshgroup.com` all return HTTP 403 behind a Cloudflare bot challenge to this environment; `/en/make-a-booking` was behind Imperva at its last archived capture. WebFetch and Bash `curl` were both tested and both blocked **by the sites, not by the egress proxy** — the proxy itself works, as demonstrated by successful fetches from hkexnews.hk, shijigroup.com, ttgasia.com, cellpointdigital.com, macaubusiness.com, reconpayment.com, be.synxis.com and gifts.peninsula.com. Findings were recovered via Wayback Machine captures (dated and cited individually) and by reaching the SynXis and Techsembly hosts directly. **The payment step itself was never reached**, so no accepted-card-brand list, no APM list and no deposit-versus-guarantee determination could be made.
- **Section 4 (APMs) is largely "Unknown, checkout not accessible"** as a direct consequence. **No local rail absence is claimed anywhere in this report**, and the corresponding ICP row is scored zero on purpose.
- **Section 5 (Complaints) is empty.** A genuine negative after five search angles.
- **Legal entity names outside Hong Kong and China Mainland were not found.** No corporate registry was successfully queried; the four named entities all come from the merchant's own privacy policy.
- **No regulatory claim is made for any market.** No current primary source on Japanese, Thai, Philippine or Hong Kong acquiring requirements was reached within budget, and nothing is cited from background knowledge.
- **The monthly transaction count is ASSUMED**, with the room-night component derived from two sourced inputs and the length-of-stay divisor unsourced.

**Traffic data provenance, stated explicitly:** traffic was **SUPPLIED** by Prateek (SimilarWeb PRO, Worldwide, all traffic, Sep 2026, captured 2026-10-09), not API-sourced and not estimated. It is a **top-10 country cut only**, so the 41.29% APAC figure is a visible floor. Because the country profile drives both the APM analysis and two ICP signals, note that the profile itself is high quality but incomplete at the tail.

**Method deviation, disclosed:** no subagent-spawning tool (Task/Agent) was available in this environment, so Phase 1 and the Phase 2 workstreams of Agents 2–5 were executed sequentially by a single analyst within the same per-agent search and fetch discipline, rather than in parallel. No budget was exceeded; coverage of Agent 5's competitor-stack work and Agent 4's complaint work is thinner than a parallel run would have produced.

---

### Manual Research Recommendations

> **Area:** **Monthly transaction count** — the only ICP signal that can reject this account, and it is currently an assumption.
> **Why it matters:** The derived room-night figure (61,025/month) is solid, but bookings require average length of stay, which HSH does not publish, and the centrally-settled online subset is unknown. A 3,106-room group may simply be below the volume floor for this motion.
> **Suggested manual action:** Ask directly on the first call: monthly direct-web bookings on peninsula.com, average length of stay, and the direct-vs-OTA split. Three numbers settle the whole account.

> **Area:** **Where the card settles — central versus per property.** The headline question.
> **Why it matters:** If rooms settle per property through local acquirers behind SynXis, there is no central stack to orchestrate today, the buyer is the CRS and PMS owner rather than a payments lead, and the deal shape is a hosted-payment-page swap on the Radisson pattern. If a central prepaid-rate programme exists at scale, the deal is conventional.
> **Suggested manual action:** Complete a booking on `be.synxis.com?hotel=17695` (Tokyo) to the payment step with DevTools open. Capture the POST target at card entry, the merchant descriptor, whether a deposit is taken or only a guarantee, and the accepted card brands. Repeat for `?hotel=12597` (Hong Kong). Then read the rate-level terms on a standard rate versus a "Luxury in Advance" rate — the Istanbul third-party listing suggests those differ, and it is the only prepay signal found.

> **Area:** **Japanese payment methods at The Peninsula Tokyo.**
> **Why it matters:** Japan is 17.93% of web demand, ahead of the home market, and the konbini processor rule already exists on the SynXis platform Peninsula licenses (code `KB`, JPY, 7-day lead). Whether it and PayPay, LINE Pay, Rakuten Pay, Paidy or card instalments are enabled could not be established — and the brief was explicit that this gap must be verified, not assumed. **It has not been verified, and no gap is claimed.**
> **Suggested manual action:** With a Japanese VPN exit, reach the payment step on `be.synxis.com?hotel=17695&locale=ja-JP` and photograph the method list. Do the same from a US exit to see whether the list adapts by issuer country.

> **Area:** **Legal entity names in Japan, Thailand, the Philippines, the UK, France, Türkiye and the US.**
> **Why it matters:** The merchant of record per property is the acquiring entity, and that is the per-property settlement thesis made concrete.
> **Suggested manual action:** Query the Japan corporate number (hojin bangou) registry, Thailand DBD, Philippines SEC, UK Companies House and the relevant US state registries for Peninsula/HSH entities. Cross-check against whatever descriptor appears on a test booking.

> **Area:** **Regulatory acquiring requirements in Japan, Thailand, the Philippines and Hong Kong.**
> **Why it matters:** The cross-border and regulatory-gate argument in Section 2 is deliberately unmade because no current primary source was reached. Without it, the only cross-border argument available is the approval-rate and FX one.
> **Suggested manual action:** Pull the current primary sources — Japan FSA / METI on e-commerce card acquiring, Bank of Thailand, BSP Philippines, HKMA — and cite them before any of this reaches an email.

> **Area:** **Stakeholders.** None are recorded in the target list.
> **Why it matters:** The payment decision here almost certainly does not sit with a payments owner.
> **Suggested manual action:** Three named starting points, all public: **Benjamin Vuchot**, CEO since 3 March 2025 and author of the PERFORM/TRANSFORM agenda ([HKEX FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf)); **Michael Garcia**, Group General Manager, Technology, quoted in the Shiji announcement and the most likely owner of the CRS and PMS estate ([Shiji](https://www.shijigroup.com/press-news/shijis-enterprise-platform-powers-peninsula-hotels-into-the-future-of-luxury-hospitality)); and the Hong Kong head-office **Director, Digital Marketing** role, whose own posting says it owns global digital strategy with a focus on direct booking revenue ([careers.hshgroup.com](https://careers.hshgroup.com/Corporate/job/Hong-Kong-Director%2C-Digital-Marketing-HK/1055162766)).

> **Area:** **Three missing TAL additions.**
> **Why it matters:** Mandarin Oriental, Shangri-La and Rosewood are all Hong Kong-headquartered luxury hotel groups with larger APAC footprints than Peninsula and no publicly disclosed payment stack. None is on `accounts/apac-tal.csv`. Minor Hotels and Okura Nikko are also absent.
> **Suggested manual action:** Add all five. The Peninsula discovery — per-property CRS currency configuration, Shiji/Opera PMS estate, Sabre dependency — is directly reusable against every one of them.

---

### Appendix: All Source URLs

**Section 1 — Traffic**
- `accounts/traffic/the-peninsula-hotels.md` — SimilarWeb PRO (supplied by Prateek 2026-10-09; period Sep 2026)

**Section 2 — Legal entities**
- https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security
- https://web.archive.org/web/20260809143321/https://www.peninsula.com/en/global-pages/website-conditions-of-use
- https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf
- https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0331/2025033100265.pdf
- https://www.shijigroup.com/press-news/shijis-enterprise-platform-powers-peninsula-hotels-into-the-future-of-luxury-hospitality
- `https://gifts.peninsula.com/` · `https://ecom.peninsula.com/` (both fetched 2026-10-09)

**Section 3 — Payment stack**
- `https://be.synxis.com/?hotel=17695&arrive=2026-11-10&depart=2026-11-12&adult=2&locale=ja-JP` (fetched 2026-10-09 — response headers and page state)
- `https://be.synxis.com/?hotel=12597&arrive=2026-11-10&depart=2026-11-12&adult=2` (fetched 2026-10-09)
- `https://gifts.peninsula.com/checkout` · `https://gifts.peninsula.com/cart` (fetched 2026-10-09)
- https://www.reconpayment.com/
- https://web.archive.org/web/20260711063806/https://www.peninsula.com/en/global-pages/data-privacy-and-security
- https://web.archive.org/web/20260809143321/https://www.peninsula.com/en/global-pages/website-conditions-of-use
- https://web.archive.org/web/20241127184615/https://www.peninsula.com/en/global-pages/terms-and-conditions
- https://www.shijigroup.com/press-news/shijis-enterprise-platform-powers-peninsula-hotels-into-the-future-of-luxury-hospitality
- https://www.ttgasia.com/2023/07/07/sabre-deepens-tech-expertise-with-techsembly-acquisition/
- https://www.adyen.com/zh_CN/press-and-media/adyen-shiji-partner-to-streamline-hospitality-payments

**Section 4 — Payment methods**
- `https://be.synxis.com/?hotel=17695` and `?hotel=12597` (fetched 2026-10-09)
- `https://gifts.peninsula.com/checkout` (fetched 2026-10-09)
- https://www.reconpayment.com/

**Section 5 — Complaints**
- No sources — nothing found.

**Sections 6 and 7 — Corporate and payment news**
- https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf (FY2025 Annual Results, 18 Mar 2026)
- https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800261.pdf (Q4 2025 operating statistics)
- https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0805/2026080500241.pdf (H1 2026 Interim Results, 5 Aug 2026)
- https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0805/2026080500261.pdf (Q2 2026 operating statistics)
- https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0331/2025033100265.pdf (FY2024 Annual Results, 31 Mar 2025)
- https://www.shijigroup.com/press-news/shijis-enterprise-platform-powers-peninsula-hotels-into-the-future-of-luxury-hospitality
- https://www.ttgasia.com/2023/07/07/sabre-deepens-tech-expertise-with-techsembly-acquisition/
- https://cellpointdigital.com/articles/casestudies/payment-orchestration-as-a-growth-catalyst-the-radisson-hotel-group-case-study
- https://macaubusiness.com/minor-hotels-partners-with-checkout-com-to-power-high-performance-payments-across-global-hospitality-60/
- https://careers.hshgroup.com/Corporate/job/Hong-Kong-Director%2C-Digital-Marketing-HK/1055162766
- https://careers.hshgroup.com/Corporate/job/Hong-Kong-Assistant-Manager%2C-Digital-Product-and-Content-HK/1051644566

**Sections 8 and 9 — Checkout and PCI**
- `https://be.synxis.com/?hotel=17695` · `?hotel=12597` (CSP headers and page state, fetched 2026-10-09)
- `https://gifts.peninsula.com/checkout` (fetched 2026-10-09)
- https://www.reconpayment.com/
- https://web.archive.org/web/20260809143321/https://www.peninsula.com/en/global-pages/website-conditions-of-use

**Section 11 — Competitors**
- https://cellpointdigital.com/articles/casestudies/payment-orchestration-as-a-growth-catalyst-the-radisson-hotel-group-case-study
- https://macaubusiness.com/minor-hotels-partners-with-checkout-com-to-power-high-performance-payments-across-global-hospitality-60/
- https://hoteltechreport.com/news/swire-hotels-partners-adyen (HTTP 403 — summary only, page not fetched)
- https://servicedapartmentnews.com/news/technology/frasers-hospitality-adyen/ (summary only, page not fetched)
- https://www.casestudies.com/company/2c2p/case-study/anantara-siam-bangkok-boosts-transactions-500-in-3-months-with-2c2p (summary only, page not fetched)
- https://www.hospitalitynet.org/news/4120196.html (summary only, page not fetched)
- `accounts/apac-tal.csv` (internal cross-check)

**Section 12 — Business case**
- https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800251.pdf
- https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0805/2026080500241.pdf
- https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0805/2026080500261.pdf
- https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0331/2025033100265.pdf
- `https://be.synxis.com/?hotel=17695` · `?hotel=12597` (currency and FX rate configuration, fetched 2026-10-09)

</details>
