# Fast Retailing (Uniqlo)

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 17 / 29 → ⭐ High Priority *(borderline. The +4 greenfield award is the fragile point: if discovery shows the HQ "payment system" routes between processors, the score drops to 14, 🟢 Medium. Read the reality check in the ICP breakdown.)*
**Industry:** Retail. Apparel (UNIQLO, GU, plus Theory / PLST / Comptoir des Cotonniers), omnichannel stores + own e-commerce + apps · **HQ:** Yamaguchi City / Tokyo, Japan. Fast Retailing Co., Ltd. (TSE 9983) · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **Greenfield, with an HQ-run payment system.** No third-party orchestrator found. Fast Retailing Co., Ltd. in Japan runs the "payment system" centrally; Adyen is its sub-processor (2022 omnichannel deal). Local providers are bolted on per market: four Korean PG/VANs, Net Protections in Japan, PayPal in Australia. Do not pitch "consolidate your PSPs": in 2022 they consolidated *onto* Adyen to cut supplier contracts. Pitch the per-market rail work that one PSP leaves to HQ, and the gaps that work has left online.

---

> ## 🎯 THE HOOK: UNIQLO's own help centres show stores in SEA accepting rails that online checkout does not
>
> Every regional UNIQLO store publishes its complete online payment list on its Salesforce help centre (fetched 2026-10-19). In five APAC markets, the **store till accepts the local wallet and the website does not**:
>
> | Market | Online checkout (full list per UNIQLO) | Accepted in UNIQLO stores, absent online |
> |---|---|---|
> | 🇭🇰 Hong Kong | Visa/MC/Amex, UnionPay, AliPay, WeChat Pay, PayMe. *"Apple Pay, Google Pay and Octopus… not supported"* online | **Octopus, Apple Pay, Google Pay, EPS** ([online](https://faq-hk.uniqlo.com/pkb_Home_UQ_HK?id=kA0fR0000000yLx&l=en_US) · [store](https://faq-hk.uniqlo.com/pkb_Home_UQ_HK?id=kA0Ie000000TOfo&l=en_US)) |
> | 🇻🇳 Vietnam | Card, COD, pay-in-store (plus "ATM card" on a second page) | **VNPay, QR Pay, e-wallets, Payoo** ([faq-vn](https://faq-vn.uniqlo.com/pkb_Home_UQ_VN?id=kA0Ie000000TOQQ&l=en_US)) |
> | 🇵🇭 Philippines | Cards, COD, pay-in-store within 2h | **GCash, GGives, GrabPay, QRPH**: usable only by walking to a till ([faq-ph](https://faq-ph.uniqlo.com/pkb_Home_UQ_PH?id=kA0Ie000000TOyV&l=en_US)) |
> | 🇹🇭 Thailand | Card (single payment, no Amex, **no foreign-issued cards**), COD, pay-in-store. *"QR code payment for UNIQLO Online is not supported"* | PromptPay / any QR ([faq-th](https://faq-th.uniqlo.com/pkb_Home_UQ_TH?id=kA0Ie000000TOqj&l=en_US)) |
> | 🇯🇵 Japan | Card **single payment only, no instalments or bonus payment**, PayPay & d払い (under ¥55,000; PayPay members only), NP後払い, COD, gift cards | Rakuten Pay, au PAY, merpay, Alipay, WeChat Pay: online orders reach them only via "pay at store register" ([online list](https://faq.uniqlo.com/articles/Knowledge/100001967/) · [store-register](https://faq.uniqlo.com/articles/Knowledge/100004232/)) |
>
> **Why now:** UNIQLO shut its own app wallet, UNIQLO Pay, in January 2026. Its stated reason was that customers had moved to QR-code and card payments ([Impress Netshop, 2025-10-02](https://netshop.impress.co.jp/node/14872); [UNIQLO FAQ](https://faq.uniqlo.com/articles/Knowledge/100006473/)). Fast Retailing has said in writing that shoppers want third-party QR wallets. Online checkout in SEA and HK still doesn't offer most of them.
>
> **Resilience proof point:** on 28 Jul 2026 UNIQLO Indonesia posted a "system maintenance" notice in which **QRIS, credit card and GoPay all went down at 11:58 WIB**. Cards came back at 17:56, about six hours later ([faq-id](https://faq-id.uniqlo.com/pkb_Home_UQ_ID?id=kA0fR0000000SYz&l=en_US)).

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Fast Retailing is the Japanese parent of UNIQLO and GU. It runs 3,510 stores (FY Aug 2026) plus country-by-country e-commerce stores and apps. FY Aug 2026 revenue was ¥3.96tn (≈US$25.0bn, +16.6%). UNIQLO International was ¥2.41tn (+26.2%), now more than double UNIQLO Japan's ¥1.08tn ([FashionUnited](https://fashionunited.com/news/business/uniqlo-international-drives-fast-retailings-16-6-percent-revenue-growth-in-fy2026/2026100875091); [FR segment data](https://www.fastretailing.com/eng/ir/financial/segment_5yrs.html)). FY Aug 2025 e-commerce revenue was ¥152.4bn in Japan and ¥306.4bn internationally ([Yuho FY2025, notes 6–7](https://www.fastretailing.com/eng/ir/library/pdf/yearendreport202508_eng.pdf)).

**SimilarWeb total visits (last full month):** ≈108.4M/month on average, Jul–Sep 2026. That is uniqlo.com 96.28M + gu-global.com 12.15M (SimilarWeb, supplied 2026-10-19). Monthly figures are not supplied, so this is the 3-month average, not "last full month". **Caveats from the traffic file:**
- Sales Intelligence view: top 10 countries per domain, share only.
- Mobile apps are excluded.
- Omnichannel: the apps and in-store POS carry a large share of transactions, so web traffic is a market-mix signal, not a sizing input.
- fastretailing.com was not pulled.

### Top 5 markets
Ranked by combined web traffic. Japan, Korea and Taiwan are in territory; the full APAC list follows.

| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇯🇵 **Japan** | 32.4% | Card (Visa/MC/JCB/Amex-JP/Diners, **single payment only**), PayPay (<¥55k, members only), d払い (<¥55k), NP後払い (pay later, payable at konbini), COD, pay at store till, gift cards | Card instalments / bonus payment, Apple Pay / Google Pay, Rakuten Pay, au PAY, Paidy, Amazon Pay | ✅ UNIQLO CO., LTD.; G.U. CO., LTD. |
| 2 | 🇺🇸 United States *(out of territory)* | 14.9% | Not assessed | Not assessed | ✅ (US stores: 86) |
| 3 | 🇰🇷 **South Korea** | 8.1% | Credit/check card via local PG (with interest-free instalments; "easy pay" inside the card flow), Naver Pay. KakaoPay implied, card-funded only | Bank transfer / virtual account, mobile-phone billing, gift vouchers (all explicitly excluded); Toss Pay / PAYCO / Samsung Pay not named | ✅ FRL Korea Co., Ltd. (FR 51%) |
| 4 | 🇬🇧 United Kingdom *(out of territory)* | 5.1% | Not assessed | Not assessed | Not checked |
| 5 | 🇹🇼 **Taiwan** | 4.9% | Visa/MC/JCB (single payment, 3DS OTP), LINE Pay, JKOPay, COD incl. convenience-store pickup | Instalments, UnionPay, Apple Pay, ATM / virtual account | ✅ 台灣優衣庫有限公司 (named online-store operator) |

### APAC markets beyond the top 5
| Market | Traffic | Online methods (full list per help centre) | Missing online | Entity |
|---|---|---|---|---|
| 🇦🇺 Australia | 4.5% | Visa/MC/Amex, PayPal, PayPal Pay in 4, Apple Pay, Google Pay, gift card | **Afterpay removed online 2025-03-31**; no Zip, no PayTo | ✅ UNIQLO AUSTRALIA PTY LTD |
| 🇮🇩 Indonesia | 2.1% | Visa/MC/JCB, QRIS, VA at 7 banks, COD, pay-in-store, GoPay (app only) | Alfamart/Indomaret, Kredivo/Akulaku; OVO/DANA/ShopeePay only via QRIS | ✅ PT. FAST RETAILING INDONESIA (75%) |
| 🇭🇰 Hong Kong | ≥0.16% (GU only; UNIQLO HK below uniqlo.com's top 10) | Cards, UnionPay, AliPay, WeChat Pay, PayMe | **Octopus, Apple Pay, Google Pay (explicit)**, FPS | ⚠️ UNIQLO HONG KONG, LIMITED (est. 2005, Yuho history only) |
| 🇻🇳 Vietnam | ≥0.03% | Card, ATM card, COD, pay-in-store | MoMo, ZaloPay, VNPay (VNPay is accepted in stores) | ✅ UNIQLO VIETNAM Co., Ltd. (75%) |
| 🇸🇬🇲🇾🇹🇭🇵🇭🇮🇳 | Not in top 10 | SG: cards, GrabPay. MY: cards, GrabPay, online banking (18 banks). TH: card, COD. PH: cards, COD. IN: cards (incl. RuPay), "wallets/UPI" | SG PayNow; MY Touch 'n Go; TH PromptPay/QR; PH GCash/Maya online; IN COD | ✅ TH, IN, PH, SG (holding); ⚠️ MY |

### Legal entities
- FAST RETAILING CO., LTD. (Japan): holding company; runs the group "결제시스템" (payment system) per the KR privacy policy
- UNIQLO CO., LTD. (Japan), JPY 1.0bn capital · G.U. CO., LTD. (Japan)
- FRL Korea Co., Ltd. (South Korea), 51% FR
- 台灣優衣庫有限公司 / UNIQLO Taiwan (Taiwan), unified business no. 25117554 `[UNVERIFIED — third-party sites only]`
- UNIQLO AUSTRALIA PTY LTD (Australia)
- PT. FAST RETAILING INDONESIA (Indonesia), 75%
- UNIQLO (THAILAND) COMPANY LIMITED (Thailand), 75%
- UNIQLO VIETNAM Co., Ltd. (Vietnam), 75%
- UNIQLO INDIA PRIVATE LIMITED (India), 100%
- Fast Retailing Philippines Inc. (Philippines): named in the PH privacy policy
- FAST RETAILING (SINGAPORE) PTE. LTD. (Singapore): holding/management
- Fast Retailing Global Business Services (Malaysia) SDN. BHD.: shared-services accounting, per the KR privacy policy
- Four Mainland China trading entities; UNIQLO HONG KONG, LIMITED (Yuho history only)

### Known PSPs
- **Adyen**: `[Press Release]`, 2022-07-06. "chosen by Fast Retailing… to power payments for the brand's in-store and online checkout in multiple markets" ([adyen.com](https://www.adyen.com/press-and-media/adyen-provides-omnichannel-payments-services-to-uniqlo)). `[Terms/Privacy Policy]`: Adyen N.V. is a current sub-processor of Fast Retailing Co., Ltd. in the KR privacy policy and the card-tokenisation source in the PH privacy policy. **Markets not named**, and Japan is not confirmed.
- **KSNET, KPN (한국결제네트웍스), NHN KCP, NHN Commerce**: `[Terms/Privacy Policy]`, Korea, "주문상품 결제대행" (order payment processing) ([faq-kr](https://faq-kr.uniqlo.com/pkb_Home_UQ_KR?id=kA0Ie000000TO0Z&l=ko))
- **Net Protections (NP後払い)**: `[Third-Party Report]` + help centre, Japan pay-later for UNIQLO and GU since 2017
- **PayPal / PayPal Pay in 4**: help centre (Australia)
- **PayPay, NTT Docomo (d払い), Naver Pay, LINE Pay, JKOPay, GrabPay, GoPay, QRIS**: help centre, as wallets per market
- **SMBC**: `[Press Release]`, built the payment service behind UNIQLO Pay (2021; **discontinued Jan 2026**)
- **The Japan card acquirer/gateway is unknown.** No GMO-PG, SBPS, Veritrans or KOMOJU found. The SEA/IN gateways are unnamed ("independent payment gateway service provider" in the PH/VN terms).

### Orchestration status
**None detected: direct PSP integrations, run from an HQ payment system.** No Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails or Yuno link found. The KR privacy policy lists **Fast Retailing Co., Ltd.** (Japan) as the operator of the group's "전산시스템·고객 상담시스템·결제시스템 운영 및 유지보수" (operation and maintenance of the IT, customer-service and payment systems), with Adyen N.V. as its sub-processor. Korea's local PGs are contracted separately ([faq-kr](https://faq-kr.uniqlo.com/pkb_Home_UQ_KR?id=kA0Ie000000TO0Z&l=ko), fetched). This is a central platform, but there is **no evidence of routing between processors**. Treat it as in-house-adjacent in the pitch.

### Buying signals
- 🚀 **India: 100+ stores targeted by 2031**, up from 20 in June 2026 ([Inside Retail, 2026-07-27](https://insideretail.asia/2026/07/27/uniqlo-eyes-100-plus-stores-in-india-by-2031/)). Vietnam is at 32 stores (from 29); Hanoi Centre opened 2026-03-27 ([Vietstock](https://en.vietstock.vn/2026/03/uniqlo-to-open-new-store-in-ha-noi-974-629709.htm)). The Philippines adds 3 new stores and 3 expansions in FW2026 ([Tribune](https://tribune.net.ph/2026/09/08/uniqlo-expands-philippine-footprint-with-six-stores)).
- 💰 **UNIQLO International revenue +26.2% to ¥2.41tn in FY2026**, with double-digit growth in Korea, SEA, India and Australia ([FashionUnited](https://fashionunited.com/news/business/uniqlo-international-drives-fast-retailings-16-6-percent-revenue-growth-in-fy2026/2026100875091)). No funding round: listed company.
- 🤝 **UNIQLO Pay retired in Jan 2026**, in favour of third-party QR and cards ([Impress](https://netshop.impress.co.jp/node/14872)). **Afterpay removed from AU online on 2025-03-31**; PayPal Pay in 4 replaced it ([faq-au](https://faq-au.uniqlo.com/pkb_Home?id=kA0Ie000000TOwm&l=en_US)). The rail mix is being actively changed.
- 📋 No public payment RFP found. 💼 No payment-specific job postings found.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Fast Retailing (Uniqlo)` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 17 / 29
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | +5 | ✅ DERIVED (floor): **≥250,000/month from Japan e-commerce alone, at a deliberately absurd ticket ceiling.** UNIQLO Japan EC revenue FY Aug 2025 was ¥152,364m ([Yuho, note 6](https://www.fastretailing.com/eng/ir/library/pdf/yearendreport202508_eng.pdf)), so ¥12.70bn/month. Even if every order averaged ¥50,000 (the ceiling is my bound, not a sourced ATV), that is ≈254,000 orders/month. UNIQLO International EC (¥306,429m) on the same bound adds ≈511,000. Billing unit: online orders. Excluded: Adyen-processed in-store transactions across 3,510 stores, which are far larger. The 40k gate cannot fire. |
| Orchestration status | +4 | ✅ None detected. No third-party orchestrator; an HQ payment system with Adyen as sub-processor plus per-market providers. **Fragile:** if that HQ system turns out to route between acquirers, this becomes +1 (in-house). |
| 3+ countries | +3 | ✅ 10 countries above 1% web traffic; 12+ APAC legal entities (Yuho subsidiary table) |
| Multiple PSPs | +3 | ✅ Adyen (press release + KR/PH privacy policies), KSNET / KPN / NHN KCP / NHN Commerce (KR privacy policy), Net Protections (JP), PayPal (AU) |
| Local rail or licensing gap in a top-3 market | 0 | ❌ Not met under the strict rule. Japan (#1) has PayPay and a konbini-payable invoice (NP後払い); Korea (#3) has Naver Pay. Both have local entities. The evidenced Japan gaps (no card instalments or bonus payment, no Apple Pay, wallets capped below ¥55,000) are real but are not the matrix's named rails. The **strong rail gaps are in HK, VN, PH, TH and SG**, all outside the top 3 by web traffic. |
| Recent expansion | 0 | ⬜ No new country in the last 12 months (FY2026 store list has the same countries as FY2025). Store growth inside existing markets (India 16→20, VN 29→32, PH +3) is sourced but is not "market expansion" |
| Payment issues reported | 0 | ⬜ Isolated only: AU duplicate-pre-auth FAQ, ID 28-Jul-2026 multi-method maintenance. Trustpilot refund complaints are UK/EU and unverified |
| Funding >$10M | 0 | ❌ Listed company, no rounds |
| High traffic outside home | +2 | ✅ Japan is 32.4% of combined web traffic; UNIQLO International is 61% of FY2026 revenue |
| Competitor using orchestration | 0 | ⬜ Zalora/BridgerPay (2021, vendor story) and Shein (TAL says Juspay) are both unverified |
| Payment job postings | 0 | ❌ None found |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **⭐ High Priority (17)**
No public payment RFP found.

**Analyst override check: none applied. Reality check:**
- *Borderline:* 17 is exactly the ⭐ floor, and it rests on the +4 greenfield award. On this evidence the classification is correct: no routing layer is evidenced. But the HQ "payment system" is a known unknown, and a single discovery answer could move this to 🟢.
- *Against Yuno's thesis:* the 2022 Adyen decision was explicitly about removing "the need for multiple supplier contracts". Pitching orchestration as "more PSPs" contradicts a decision they made deliberately. The opening is the opposite: they kept one global PSP and still had to add local providers by hand (four in Korea alone), and SEA online checkout still lags their own stores.
- *Not app-store dominated:* UNIQLO is the merchant of record in its own apps; no IAP. The app traffic gap only means web traffic understates volume.
- *No double-counting:* the PSPs are separate per-market contracts, not one regional split.
- *Enterprise cycle:* ¥3.96tn revenue, decisions in Tokyo, Japanese-language buying process. Treat it as a multi-quarter play and do not forecast it.

### Source Notes
- ✅ Adyen press release text re-read by me (adyen.com, dated Amsterdam 2022-07-06)
- ✅ KR privacy policy re-fetched by me. It contains the KSNET/KPN/NHN KCP/NHN Commerce payment-processing row, and Fast Retailing Co., Ltd. as payment-system operator with Adyen N.V. as sub-processor. It also shows Lotte Shopping's e-commerce division running FRL Korea's IT systems.
- ✅ PH privacy policy re-fetched by me: "partial and masked credit card details shared by Adyen N.V."
- ✅ Korea "card or Naver Pay only", Japan "一括払いのみ" (single payment only), PayPay <¥55,000, AU Afterpay removal text, ID 28-Jul maintenance text: all checked by me in the saved help-centre pages
- ✅ Japan and international EC revenue checked against the Yuho text (notes 6–7)
- ⚠️ Adyen's market scope is not stated anywhere. Current use is confirmed only for KR (HQ sub-processor) and PH (tokenisation).
- ⚠️ The KakaoPay inference rests on the KR order guide's line "KakaoPay cannot use charged money".
- ⚠️ VN help pages disagree: 3 vs 4 online methods. The "ATM card" page is likely newer.
- ⚠️ FY2025 group operating/net profit and Lotte's 49% in FRL Korea come from search summaries only.
- ⚠️ UNIQLO HK entity: name from the Yuho history only; not in the current major-subsidiaries table.

### Success Case Alternatives
- **Reserva (Yuno customer, Brazilian fashion brand)**: the only fashion-retail Yuno case found. Reported +4% approval in 3 months with Smart Routing ([y.uno/success-cases/reserva](https://y.uno/success-cases/reserva)) `[UNVERIFIED — search summary only, page not fetched]`. A third party describes the gain as +4pp *conversion*, so use "4%" only with the metric confirmed. It matches the omnichannel apparel profile, but it is LatAm-only and a fraction of the scale.
- No APAC retail Yuno case found. Do not imply one.

---

## Executive Summary

Fast Retailing (UNIQLO, GU) is a ¥3.96tn (≈US$25bn) Japanese apparel retailer with 3,510 stores and separate e-commerce stores in every APAC market it operates in. International sales are now 61% of revenue and grew 26% in FY2026. Its payments run on an HQ-operated platform. Adyen is the global omnichannel PSP (since 2022) and a current sub-processor of Fast Retailing Co., Ltd.; local providers are added per market (four Korean PG/VANs, Net Protections in Japan, PayPal in Australia). No third-party orchestrator was found, so the motion is **greenfield**, but against a team that deliberately consolidated suppliers. The opening is coverage. UNIQLO's own help centres show online checkout in HK, Vietnam, the Philippines, Thailand and Singapore missing the local wallets and QR rails its stores accept. Japan's online card checkout is single-payment only. And UNIQLO retired its own wallet in January 2026, saying customers had moved to QR codes and cards.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** Path 1, pasted SimilarWeb data: `accounts/traffic/fast-retailing-uniqlo.md`, SimilarWeb Sales Intelligence (supplied 2026-10-19), Jul–Sep 2026, desktop + mobile web, uniqlo.com and gu-global.com.

**Method:** per-domain shares × that domain's average monthly visits (uniqlo.com 96.28M, gu-global.com 12.15M), summed per country, shares recalculated over the 108.43M combined total. Every visit figure is `[DERIVED from supplied share, not a SimilarWeb figure]`.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | 🇯🇵 Japan **(high priority)** | 32.41% | 35.14M (uniqlo 25.94M + GU 9.20M) | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | 🇺🇸 United States *(out of territory)* | 14.91% | 16.16M | Not supplied | same |
| 3 | 🇰🇷 South Korea **(high priority)** | 8.11% | 8.80M (almost all uniqlo.com; GU 0.44%) | Not supplied | same |
| 4 | 🇬🇧 United Kingdom *(out of territory)* | 5.10%* | 5.53M | Not supplied | same |
| 5 | 🇹🇼 Taiwan | 4.89% | 5.30M (uniqlo 4.06M + GU 1.24M) | Not supplied | same |
| 6 | 🇦🇺 Australia | 4.51% | 4.89M | Not supplied | same |
| 7 | 🇨🇦 Canada *(out of territory)* | 4.10% | 4.45M | Not supplied | same |
| 8 | 🇫🇷 France *(out of territory)* | 3.25%* | 3.52M | Not supplied | same |
| 9 | 🇩🇪 Germany *(out of territory)* | 2.23% | 2.41M | Not supplied | same |
| 10 | 🇮🇩 Indonesia | 2.10% | 2.28M | Not supplied | same |
| — | 🇭🇰 Hong Kong | ≥0.16%** | ≥0.18M | — | same |
| — | 🇻🇳 Vietnam | ≥0.03%** | ≥0.04M | — | same |

\* UK and France are not in gu-global.com's top 10, so the GU contribution counts as zero. GU's #10 country is 0.13%, so the error is negligible.
\** HK and Vietnam appear only in GU's list. Their uniqlo.com share sits inside the unlisted 20.26%, so these are floors. Each is below 2.31% (uniqlo.com's #10), and the true uniqlo.com HK/VN share is unknown.

**Notes**
- Device split: uniqlo.com 75.4% mobile web; gu-global.com 82.9% mobile web.
- Global rank: not captured in the source.
- **Mobile apps are excluded** and are likely a large share of transactions for an omnichannel retailer, per the traffic file's caveat.
- Use these figures as a market-mix signal only, not for sizing.
- **Entity cross-check:** every in-territory top-10 market has a confirmed local entity (Section 2). There is no cross-border gap.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Fast Retailing Co., Ltd., Yamaguchi City (registered) with Tokyo operations, Japan. Listed on TSE (9983), with HDRs on HKEx.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Japan | FAST RETAILING CO., LTD. (holding) | Not found | [Yuho FY2025](https://www.fastretailing.com/eng/ir/library/pdf/yearendreport202508_eng.pdf) |
| Japan | UNIQLO CO., LTD. (JPY 1.0bn; FY25 revenue ¥1,026.1bn) | Not found | Yuho |
| Japan | G.U. CO., LTD. (JPY 10m) | Not found | Yuho |
| South Korea | FRL Korea Co., Ltd. (KRW 24bn; FR 51%; Lotte Shopping reportedly holds 49% `[UNVERIFIED — search summary]`) | Not found | Yuho |
| Taiwan | 台灣優衣庫有限公司. Online-store operator (企業經營者); 新北市板橋區縣民大道二段68號15樓 | 25117554 `[UNVERIFIED — third-party sites]` | [uniqlo.com/tw contract](https://www.uniqlo.com/tw/company/contract/) (fetched by Agent 1) |
| Australia | UNIQLO AUSTRALIA PTY LTD (Melbourne; AUD 21m) | ABN not found | Yuho |
| Indonesia | PT. FAST RETAILING INDONESIA (IDR 115.2bn; 75%) | Not found | Yuho |
| Thailand | UNIQLO (THAILAND) COMPANY LIMITED (THB 1.82bn; 75%) | Not found | Yuho |
| Vietnam | UNIQLO VIETNAM Co., Ltd. (USD 15.8m; 75%) | Not found | Yuho |
| India | UNIQLO INDIA PRIVATE LIMITED (INR 2bn; 100%) | Not found | Yuho |
| Philippines | Fast Retailing Philippines Inc. | Not found | [PH privacy policy](https://faq-ph.uniqlo.com/pkb_Home_UQ_PH?id=kA0Ie000000TO39&l=en_US) |
| Singapore | FAST RETAILING (SINGAPORE) PTE. LTD. (SGD 86m; holding/management) | Not found | Yuho |
| Malaysia | Fast Retailing Global Business Services (Malaysia) SDN. BHD. (shared services); retail entity not confirmed | Not found | [KR privacy policy](https://faq-kr.uniqlo.com/pkb_Home_UQ_KR?id=kA0Ie000000TO0Z&l=ko) |
| China | FAST RETAILING (CHINA) TRADING CO., LTD.; UNIQLO TRADING CO., LTD.; FAST RETAILING (SHANGHAI) TRADING CO., LTD.; GU (Shanghai) Trading Co., Ltd. | Not found | Yuho |
| Hong Kong | UNIQLO HONG KONG, LIMITED (est. March 2005) | Not found | Yuho (history section only) |

The Yuho also lists 48 further consolidated subsidiaries that are not individually named.

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| Japan | ✅ #1 | ✅ | N/A | No |
| South Korea | ✅ #3 | ✅ FRL Korea, using four local PG/VANs | Gate satisfied (local entity + local PGs) | No |
| Taiwan | ✅ #5 | ✅ | N/A | No |
| Australia | ✅ #6 | ✅ | N/A | No |
| Indonesia | ✅ #10 | ✅ (75% JV) | Gate satisfied | No |
| Hong Kong | ❌ (floor 0.16%) | ⚠️ Historical name only | N/A | Unknown |
| Vietnam | ❌ | ✅ | Gate satisfied | No |

**There is no cross-border or regulatory-gate angle here.** Every in-territory market with meaningful traffic has a local entity, and stores are run per country. Per the AU FAQ, only the AU store ships to AU addresses ([faq-au](https://faq-au.uniqlo.com/articles/en_US/FAQ/Can-I-order-from-UNIQLO-in-a-different-country)). Do not lead with cross-border cost.

> **MANUAL:** Confirm the named seller on the KR, AU, ID and HK store footers and terms. The storefronts return 403 to automated fetches.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| "Multiple markets": in-store + online (not enumerated) | **Adyen** | `[Press Release]` 2022-07-06. Says the integration "removes the need for multiple supplier contracts" | https://www.adyen.com/press-and-media/adyen-provides-omnichannel-payments-services-to-uniqlo |
| Asia, Europe, North America (self-checkout) | Adyen | `[Third-Party Report]` RetailBiz, 2022-07-20 | https://www.retailbiz.com.au/?p=40313 |
| Korea | Adyen N.V. as sub-processor to Fast Retailing Co., Ltd. (operator of "결제시스템", the payment system) | `[Terms/Privacy Policy]` (notice 2026-07-29, effective 2026-08-05) | https://faq-kr.uniqlo.com/pkb_Home_UQ_KR?id=kA0Ie000000TO0Z&l=ko |
| Korea | **KSNET, KPN (한국결제네트웍스), NHN KCP, NHN Commerce**: "주문상품 결제대행" (order payment processing) | `[Terms/Privacy Policy]` | same |
| Philippines | Adyen N.V.: masked card details for repeat purchases (card-on-file) | `[Terms/Privacy Policy]` | https://faq-ph.uniqlo.com/pkb_Home_UQ_PH?id=kA0Ie000000TO39&l=en_US |
| Philippines, Vietnam | Unnamed "independent payment gateway service provider" (redirect / hosted page) | `[Terms/Privacy Policy]` | https://faq-ph.uniqlo.com/pkb_Home_UQ_PH?id=kA0Ie000000TO2m&l=en_US |
| Japan | **Net Protections**: NP後払い pay-later (UNIQLO + GU), since 2017 | `[Third-Party Report]` + help centre | https://netshop.impress.co.jp/node/4705 · https://faq.uniqlo.com/articles/Knowledge/100005136/ |
| Japan | PayPay, NTT Docomo (d払い) | Help centre | https://faq.uniqlo.com/articles/Knowledge/100006848/ · https://faq.uniqlo.com/articles/Knowledge/100007763/ |
| Japan | SMBC: built the UNIQLO Pay service (2021; **discontinued Jan 2026**) | `[Press Release]` | https://www2.smbc.co.jp/news/pdf/j20210119_01.pdf |
| Japan | **Card acquirer / gateway: not found** | — | — |
| Australia | PayPal (incl. Pay in 4) | Help centre | https://faq-au.uniqlo.com/pkb_Home?id=kA0Ie000000TOeD&l=en_US |
| Indonesia, India, SG, MY, TH, TW, HK | **Gateway not named.** ID policy says only "third-party payment providers"; IN FAQ says "the payment gateway" | Help centre | faq-id / faq-in (see Appendix) |

Searched and **not found**:
- Global PSPs: Stripe, Checkout.com, Worldpay, Braintree, Cybersource
- Japan: GMO-PG, SB Payment Service, Veritrans, DGFT, KOMOJU
- Korea: Toss Payments, NICEPAY, KG Inicis
- SEA: 2C2P, Xendit, Midtrans, Doku, iPay88, Omise/Opn
- ANZ: eWAY, Windcave, Tyro
- India: Razorpay, PayU, Cashfree, Paytm

`[INFERENCE, not confirmed]`: Indonesia's method mix (QRIS + 7-bank VA + GoPay) is typical of a local aggregator. The 28-Jul-2026 notice took all three down in the same window, which is consistent with one shared upstream provider. The provider is not named.

#### 3B. Payment Orchestrator

**Classification: None detected (direct PSP integrations), operated from an HQ payment system.**
- Searched with no hits: Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno.
- The KR privacy policy is the clearest view of the architecture. Fast Retailing Co., Ltd. (Japan) operates the payment system, with Adyen N.V. as its sub-processor. FRL Korea separately contracts four Korean PG/VANs.
- FintechFutures ran a 2021 headline on UNIQLO Pay: "Retailer Uniqlo cuts out middlemen with own payments integration" `[UNVERIFIED — page 403, search summary only]`. That fits a team that builds its own.

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with PSP(s), which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

Caveat: the central platform may do some routing internally. Nothing public shows it.

> **MANUAL:** Walk through checkout on uniqlo.com/jp and /kr with DevTools. Look for Adyen Web Drop-in (`checkoutshopper-live.adyen.com`) versus Japanese gateway tokens. This is the single most useful check: it tells you whether Japan is on Adyen.

---

### Section 4: Alternative & Local Payment Methods

Every row comes from the store's own help centre (faq-*.uniqlo.com / faq*.gu-global.com), fetched 2026-10-19. Each market's article lists that store's complete set of online methods, so an absence here means UNIQLO's own list leaves it out.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| JP (UNIQLO) | Visa/MC/JCB/Amex (Japan-issued)/Diners, **single payment only, no 分割 or ボーナス払い**, 3DS | Cards | Active in checkout (per help page) | https://faq.uniqlo.com/articles/Knowledge/100004123/ |
| JP | PayPay: under ¥55,000, members only | Digital wallet | Active | https://faq.uniqlo.com/articles/Knowledge/100006848/ |
| JP | d払い (carrier billing / balance / card): under ¥55,000 | Wallet / carrier billing | Active | https://faq.uniqlo.com/articles/Knowledge/100007763/ |
| JP | NP後払い: invoice payable at konbini / bank / post office; ¥250 fee | BNPL / cash | Active | https://faq.uniqlo.com/articles/Knowledge/100005136/ |
| JP | Cash on delivery: ¥330, ¥55,000 cap | Cash | Active | https://faq.uniqlo.com/articles/Knowledge/100001980/ |
| JP | Pay at store register: the till takes Rakuten Pay, au PAY, merpay, Alipay, WeChat Pay, Bank Pay and others | Cash / wallets (offline) | Active | https://faq.uniqlo.com/articles/Knowledge/100004232/ |
| JP | UNIQLO Pay (app wallet) | Digital wallet | **Deprecated**: ended 15–29 Jan 2026 | https://faq.uniqlo.com/articles/Knowledge/100006473/ |
| JP | Apple Pay / Google Pay / Rakuten Pay / au PAY / Paidy / Amazon Pay online | — | Not found (absent from the full list) | https://faq.uniqlo.com/articles/Knowledge/100001967/ |
| JP (GU) | Card (single payment), PayPay, d払い, store register, NP後払い, COD. UNIQLO gift card not accepted. ORDER & PICK is card-only | Mixed | Active | https://faq.gu-global.com/articles/Knowledge/100001841/ |
| KR | Credit/check card via PG, with "easy pay" and interest-free instalments | Cards / instalments | Active | https://faq-kr.uniqlo.com/pkb_Home_UQ_KR?id=kA0fR0000000EJ7&l=ko |
| KR | Naver Pay | Digital wallet | Active | https://faq-kr.uniqlo.com/pkb_Home_UQ_KR?id=kA0fR0000000EKj&l=ko |
| KR | KakaoPay (card-funded only; "charged money" not usable) | Digital wallet | Mentioned in docs | https://faq-kr.uniqlo.com/pkb_Home_UQ_KR?id=kA0Ie000000TO9e&l=ko |
| KR | Bank transfer / 무통장입금, mobile billing, gift vouchers | A2A / carrier | **Explicitly not available** | https://faq-kr.uniqlo.com/pkb_Home_UQ_KR?id=kA0Ie000000TO9Y&l=ko |
| KR | Toss Pay, PAYCO, Samsung Pay | Wallet | Not found by name | — |
| TW | Visa/MC/JCB (single payment, OTP), LINE Pay, JKOPay, COD (home + convenience-store pickup) | Mixed | Active | https://faq-tw.uniqlo.com/pkb_Home_UQ_TW?id=kA0Ie000000TOxG&l=zh_TW |
| TW | UnionPay, instalments, ATM / virtual account, Apple Pay | — | Not found / UnionPay explicitly unsupported | same |
| TW (GU) | Visa/MC/JCB, LINE Pay, JKOPay, COD (7-11, FamilyMart, home) | Mixed | Active | https://faq-tw.gu-global.com/pkb_Home_GU_TW?id=kA0Ie000000TOrs&l=zh_TW |
| AU | Visa/MC/Amex, PayPal, Apple Pay, Google Pay, gift card; pre-auth, capture at dispatch | Cards / wallets | Active | https://faq-au.uniqlo.com/pkb_Home?id=kA0Ie000000TOwn&l=en_US |
| AU | PayPal Pay in 4 | BNPL | Active | https://faq-au.uniqlo.com/pkb_Home?id=kA0Ie000000TOeD&l=en_US |
| AU | Afterpay | BNPL | **Deprecated online 2025-03-31** (Afterpay Card accepted in store from 2025-04-16) | https://faq-au.uniqlo.com/pkb_Home?id=kA0Ie000000TOwm&l=en_US |
| AU | Zip, PayTo | BNPL / A2A | Not found | — |
| ID | Visa/MC/JCB; QRIS; VA (BCA, Mandiri, BRI, BNI, CIMB, Permata, Danamon); COD; pay in store; GoPay (app only) | Mixed | Active | https://faq-id.uniqlo.com/pkb_Home_UQ_ID?id=kA0Ie000000TOnp&l=en_US |
| ID | Alfamart / Indomaret, Kredivo / Akulaku | Cash / BNPL | Not found | — |
| HK (UNIQLO) | Visa/MC/Amex, UnionPay, AliPay, WeChat Pay, PayMe | Mixed | Active | https://faq-hk.uniqlo.com/pkb_Home_UQ_HK?id=kA0fR0000000yLx&l=en_US |
| HK (UNIQLO) | Octopus, Apple Pay, Google Pay | Wallet | **Explicitly not supported online**; accepted in stores | same + https://faq-hk.uniqlo.com/pkb_Home_UQ_HK?id=kA0Ie000000TOfo&l=en_US |
| HK (GU) | Alipay, **AlipayHK**, WeChat Pay, PayMe, Visa/MC/UnionPay/Amex | Mixed | Active | https://faq-hk.gu-global.com/pkb_Home_GU_HK?id=kA0Ie000000TO7Z&l=zh_TW |
| VN | Card, COD, pay in store; "ATM card" on a second page | Cards / cash | Active | https://faq-vn.uniqlo.com/pkb_Home_UQ_VN?id=kA0Ie000000TOQQ&l=en_US · https://faq-vn.uniqlo.com/pkb_Home_UQ_VN?id=kA0Ie000000TPBJ&l=en_US |
| VN | MoMo, ZaloPay, VNPay online | Wallet | Not found (VNPay accepted in stores) | same |
| SG | Visa/MC/Amex, GrabPay, pay in store. No PayNow | Mixed | Active | https://faq-sg.uniqlo.com/pkb_Home_UQ_SG?id=kA0Ie000000TP7F&l=en_US |
| MY | Visa/MC/Amex, GrabPay, online banking (18 banks), pay in store. No Touch 'n Go | Mixed | Active | https://faq-my.uniqlo.com/pkb_Home_UQ_MY?id=kA0Ie000000TP5i&l=en_US |
| TH | Card (no Amex, no foreign cards, single payment), COD, pay in store. "QR code payment… not supported" | Cards / cash | Active | https://faq-th.uniqlo.com/pkb_Home_UQ_TH?id=kA0Ie000000TOqj&l=en_US |
| PH | Cards, COD (≤PHP 20,000), pay in store (till takes GCash, GrabPay, GGives, QRPH) | Cards / cash | Active | https://faq-ph.uniqlo.com/pkb_Home_UQ_PH?id=kA0Ie000000TOyV&l=en_US |
| IN | Visa/MC/RuPay (India-issued), "wallets/UPI", prepaid only, no COD | Cards / A2A | Active | https://faq-in.uniqlo.com/pkb_Home_UQ_IN?id=kA0Ie000000TP5H&l=en_US |

**Gap warnings.** These need a market-prominence citation before use in outreach; none was sourced in this run.
> *Warning: In Hong Kong, Octopus is widely used but not currently supported by UNIQLO online. UNIQLO's own stores accept it.*
> *Warning: In Thailand, PromptPay / QR is widely used but UNIQLO online explicitly does not support QR payment.*
> *Warning: In Vietnam, MoMo / VNPay are widely used but not supported online. UNIQLO stores accept VNPay.*
> *Warning: In the Philippines, GCash is widely used but is only available by paying at a store till.*

**Japan specifically:** the card checkout allows only single payment (一括払いのみ; no 分割払い, the card instalment option, or ボーナス一括, lump-sum payment at bonus time). There is no Apple Pay. Wallets are capped below ¥55,000, and PayPay is members-only (a third-party blog says guests can't use it `[UNVERIFIED]`). On UNIQLO's ticket sizes, the missing instalment option matters less than the missing wallets `[INFERENCE, not confirmed]`.

> **MANUAL:** Use a VPN to check the HK, TH and VN checkouts. The help centres may lag the live checkout, and app-only methods such as Indonesia's GoPay may exist elsewhere.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Duplicate charges / failed order: checkout timeout leaves a PayPal pre-auth in place; "paid but no order showing" | UNIQLO AU official FAQ | Isolated (a dedicated FAQ implies it recurs; volume unknown) | Undated, live 2026-10 | https://faq-au.uniqlo.com/articles/en_US/Knowledge/Do-you-offer-PayPal |
| Checkout errors: QRIS, card and GoPay all down in one "maintenance"; card down ≈6h | UNIQLO ID official notice | Isolated incident | 2026-07-28 | https://faq-id.uniqlo.com/pkb_Home_UQ_ID?id=kA0fR0000000SYz&l=en_US |
| Payment confirmation not received | UNIQLO ID FAQ | Isolated | Undated | https://faq-id.uniqlo.com/articles/en_US/FAQ/UQID-Payment-Check `[UNVERIFIED — not read]` |
| Checkout error troubleshooting | UNIQLO PH FAQ | Unknown | Undated | https://faq-ph.uniqlo.com/articles/en_US/FAQ/How-to-Troubleshoot-Checkout-Errors `[UNVERIFIED — not read]` |
| Slow / failed refunds | Trustpilot (UK/EU, out of territory) | Moderate | — | https://www.trustpilot.com/review/uniqlo.com?page=3 `[UNVERIFIED — search summary]` |
| UPI debited, no order, later refunded | App Store (India) | Isolated | — | `[UNVERIFIED — search summary only]` |
| Mobile payment issue: Diners Club notice | UNIQLO IN FAQ | Isolated | 2023-11-08 | faq-in.uniqlo.com (Agent 2) |

**Security history:** UNIQLO and GU Japan online stores suffered a credential-stuffing attack from 2019-04-23 to 05-10. Up to 461,091 accounts may have been viewed, including partial card data (name, expiry, first and last 4 digits); CVV was not stored ([Impress Internet Watch](https://internet.watch.impress.co.jp/docs/news/1184354.html)).

> *Pattern: the Indonesia notice shows three methods failing in the same window, consistent with a single upstream dependency `[INFERENCE, not confirmed]`. That is a failover / redundancy conversation, not an approval-rate one.*

No payment-complaint pattern was found on Reddit or X in in-territory markets. **Do not claim approval-rate or MDR pain**: nothing supports it.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 2026-10-08 | FY Aug 2026: revenue ¥3.96tn (+16.6%); operating profit ¥743.1bn (+31.7%); UNIQLO International ¥2.41tn (+26.2%), with double-digit growth in KR, SEA, India, AU; FY2027 guidance ¥4.45tn | Tech Blog / Conference Signal (results) | https://fashionunited.com/news/business/uniqlo-international-drives-fast-retailings-16-6-percent-revenue-growth-in-fy2026/2026100875091 |
| 2 | 2026-09-25 | Philippines: 3 new stores and 3 expansions in FW2026, starting at SM City Zamboanga (first Modest Wear store) | Market Expansion (in-market) | https://tribune.net.ph/2026/09/08/uniqlo-expands-philippine-footprint-with-six-stores |
| 3 | 2026-07-27 | India: 100+ stores targeted by 2031 (20 as of June 2026) | Market Expansion (in-market) | https://insideretail.asia/2026/07/27/uniqlo-eyes-100-plus-stores-in-india-by-2031/ |
| 4 | 2026-03-27 | Vietnam: UNIQLO Hanoi Centre, the 31st VN store | Market Expansion (in-market) | https://en.vietstock.vn/2026/03/uniqlo-to-open-new-store-in-ha-noi-974-629709.htm |
| 5 | 2025-10-02 → 2026-01-29 | UNIQLO Pay shutdown announced and completed | Payment platform change | https://netshop.impress.co.jp/node/14872 |

Store counts, FY2025 → FY2026 ([outlets](https://www.fastretailing.com/eng/ir/financial/outlets.html)):

| Market | FY2025 | FY2026 |
|---|---|---|
| Japan | 794 | 782 |
| China | 902 | 851 |
| Korea | 132 | 129 |
| Taiwan | 71 | 72 |
| HK | 35 | 35 |
| Indonesia | 77 | 77 |
| Australia | 40 | 40 |
| Vietnam | 29 | 32 |
| India | 16 | 20 |
| Philippines | 77 | 80 |
| Thailand | 70 | 73 |

**No new country** was entered in FY2026. The last new country was Poland, in FY2025.

- *"No public payment-related RFP found."*
- No payments-engineering or PSP-evaluation job postings found. Only generic IT, cloud and EC PMO roles.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 2026-07-28 | UNIQLO ID: QRIS, card and GoPay maintenance (resolved 13:04–17:56 WIB) | Resilience / failover | https://faq-id.uniqlo.com/pkb_Home_UQ_ID?id=kA0fR0000000SYz&l=en_US |
| 2 | 2025-10-02 | UNIQLO Pay to end; card registration already closed; payments end Jan 2026; reason: QR and card adoption, low usage | **REMOVAL** of an in-house rail | https://netshop.impress.co.jp/node/14872 |
| 3 | 2025-03-31 | UNIQLO AU removes the Afterpay single-use card from online; PayPal Pay in 4 offered instead | **REMOVAL** of a BNPL provider | https://faq-au.uniqlo.com/pkb_Home?id=kA0Ie000000TOwm&l=en_US |
| 4 | 2022-07-06 | Adyen chosen by Fast Retailing for UNIQLO in-store and online checkout in multiple markets | Core PSP decision | https://www.adyen.com/press-and-media/adyen-provides-omnichannel-payments-services-to-uniqlo |
| 5 | 2021-01-19 | UNIQLO Pay launched with SMBC | Historical in-house wallet | https://www2.smbc.co.jp/news/pdf/j20210119_01.pdf |

> *"REMOVAL: UNIQLO Australia discontinued Afterpay (online) as of 2025-03-31. Source: faq-au.uniqlo.com"*
> *"REMOVAL: UNIQLO Japan discontinued UNIQLO Pay as of Jan 2026. Source: netshop.impress.co.jp/node/14872"*

Japan's EMV 3-D Secure mandate for EC merchants: the UNIQLO and GU JP card pages state 3DS is in use. No date of adoption was found.

---

### Section 8: Checkout Experience Audit

*"Full checkout flow not accessible. Findings limited to publicly observable elements."*
- **Storefronts:** www.uniqlo.com and gu-global.com return HTTP 403 to automated requests, from both WebFetch and curl. This is the site's own bot protection; the egress proxy allowed other hosts.
- **Help centres:** reachable, and the source for everything below.

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | Custom storefront; PH/VN terms describe a redirect to an "independent payment gateway" | Not assessed | Hosted/redirect in PH/VN |
| Guest checkout | JP: PayPay is members-only, which implies guest checkout exists `[UNVERIFIED]` | Not assessed | — |
| Steps to complete payment | Not accessible | — | — |
| Card input experience | PH: Adyen card-on-file (masked) | Not assessed | — |
| Payment methods visible | See Section 4 | Fair | Varies sharply by market and brand |
| Location-based method display | Separate store per country | N/A | — |
| Instalment / EMI options | KR: interest-free instalments. JP/TW/TH: single payment only | Poor in JP/TW/TH | — |
| 3DS implementation | 3DS / OTP stated in JP, GU JP, TW | Not assessed | Version unknown |
| PCI indicator | PSP-held tokens (PH); hosted redirect (PH/VN) | — | — |
| Mobile responsiveness | 75–83% of web visits are mobile web; apps excluded from data | Not assessed | — |
| Multi-currency / local pricing | Local store per country, local currency | Good | — |
| Saved payment methods | PH: Adyen-tokenised masked cards | Not assessed | — |
| Error message clarity | AU FAQ tells customers to re-order after a timeout | Fair | — |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found | — |
| Card data handling | Not found directly. PH: Adyen provides masked card data; PH/VN: redirect to a gateway | PH privacy policy, PH terms |
| Recommended Yuno integration | Back-to-back API (an HQ-run payment system already exists; SDK only for markets on hosted pages) `[INFERENCE, not confirmed]` | — |

*"No direct PCI compliance documentation found publicly for Fast Retailing."*

`[INFERENCE, not confirmed]`: Based on confirmed use of Adyen card-on-file in the Philippines and gateway redirects in PH/VN, PCI scope in those markets is likely reduced, with the PSP handling card data. Not established for Japan or Korea.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: One global PSP, local rails still added by hand, one market at a time**
> **Evidence:**
> - Section 3A: Adyen was chosen in 2022 to remove "the need for multiple supplier contracts". Yet Korea alone lists four local payment processors (KSNET, KPN, NHN KCP, NHN Commerce), Japan adds Net Protections, and AU adds PayPal.
> - Section 4: each market and brand has a different method list. GU HK names AlipayHK; UNIQLO HK does not.
> - Section 3B: all of it is run by Fast Retailing Co., Ltd.'s HQ payment system.
>
> **Pain Point:** every new local rail is an HQ engineering project. The consolidation goal was met for cards but not for local methods. That is why the method lists diverge so much.
> **Yuno Value Proposition:** keep Adyen and add local rails per market through one integration, without new HQ builds or new contracts per rail.
> **Best Success Case:** Reserva (fashion, omnichannel). It is the only apparel match; scale and region are weak matches, so verify the metric before use.
> **Outreach Angle:** "You consolidated onto one PSP in 2022, but Korea still runs through four local processors and every market's checkout looks different. That per-market work is what we take off HQ."
> **Suggested Subject Line:** Four processors in Korea alone

> **Insight #2: The store accepts it, the website doesn't**
> **Evidence:**
> - Section 4: HK online explicitly lacks Octopus, Apple Pay and Google Pay, which stores accept. VN stores take VNPay; online doesn't. PH wallets work only at the till. TH says "QR code payment for UNIQLO Online is not supported".
> - Section 7: UNIQLO Pay was retired because customers moved to QR codes and cards.
>
> **Pain Point:** wallet-first shoppers are pushed offline or to cards. Pay-in-store and COD adds friction and drop-off `[INFERENCE, not confirmed]`.
> **Yuno Value Proposition:** one integration to switch on local wallets and QR (Octopus, PromptPay, MoMo/VNPay, GCash, PayNow) market by market.
> **Best Success Case:** Reserva (omnichannel apparel), with the caveat above.
> **Outreach Angle:** "Your HK stores take Octopus and Apple Pay; your HK website says it doesn't. Same in Vietnam with VNPay, and Thailand online has no QR at all."
> **Suggested Subject Line:** Octopus works in your HK stores, not online

> **Insight #3: Japan, the biggest market, has a narrow online card checkout**
> **Evidence:**
> - Section 1: Japan is 32.4% of web traffic.
> - Section 12: ¥152.4bn Japan EC revenue.
> - Section 4: cards are single-payment only. There is no Apple Pay or Google Pay. PayPay and d払い are capped below ¥55,000, and PayPay is members-only. Rakuten Pay and au PAY are reachable only by paying at a store till.
> - Section 7: the in-house wallet was retired.
>
> **Pain Point:** the largest market's online checkout has fewer wallet options than its own stores (Section 4 store list). Guest shoppers lose PayPay.
> **Yuno Value Proposition:** add Japanese wallets (Rakuten Pay, au PAY, Apple Pay) and Paidy via one connection. HQ keeps the payment system it already runs.
> **Best Success Case:** none APAC-specific. Do not overclaim.
> **Outreach Angle:** "With UNIQLO Pay gone, Japanese online shoppers have card, PayPay or d払い. Rakuten Pay and au PAY are only available if they walk to a till."
> **Suggested Subject Line:** After UNIQLO Pay

> **Insight #4: A single dependency took Indonesia's checkout down for six hours**
> **Evidence:**
> - Section 5 / Section 7: on 2026-07-28, QRIS, card and GoPay all went down together. Card was out for about six hours.
> - Section 3A: the Indonesian gateway is unnamed. One shared upstream provider is likely `[INFERENCE, not confirmed]`.
> - Section 5: the AU duplicate-pre-auth FAQ shows that timeouts already produce visible customer problems.
>
> **Pain Point:** during an outage every method fails at once, and there is no fallback route.
> **Yuno Value Proposition:** multi-acquirer failover and a second local acquirer per market.
> **Best Success Case:** none confirmed for this profile. Use the mechanism, not a case.
> **Outreach Angle:** "On 28 July your Indonesia site lost QRIS, cards and GoPay together, and cards were down for six hours. Did that route through one provider?"
> **Suggested Subject Line:** 28 July, 11:58 WIB

> **Insight #5: Expansion is in the markets where online rails are thinnest**
> **Evidence:**
> - Section 6: India is targeting 100+ stores by 2031 (from 20); Vietnam went from 29 to 32 stores; the Philippines adds 3 new stores and 3 expansions; UNIQLO International grew 26%.
> - Section 4: VN, PH and TH online offer cards plus COD or pay-in-store; India online is prepaid only, with no COD.
>
> **Pain Point:** the growth markets are wallet- and cash-first, but the online stack there is card-led.
> **Yuno Value Proposition:** expansion readiness, with local rails pre-integrated per new market.
> **Best Success Case:** none APAC-specific.
> **Outreach Angle:** "India goes from 20 to 100 stores; Vietnam and the Philippines are both adding stores this year. Online in those markets is still mostly cards and cash on delivery."
> **Suggested Subject Line:** Online in Vietnam and the Philippines

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks:**
1. Your Hong Kong help centre says Octopus, Apple Pay and Google Pay aren't supported online, yet your HK stores accept all three.
2. UNIQLO Pay closed in January because customers had moved to QR codes and cards, but Thailand online still says QR payment isn't supported.
3. Korea's privacy policy lists four separate local payment processors next to Adyen. That is a lot of per-market plumbing for a team that consolidated in 2022.

**Cold call openers:**
1. "Quick one: when UNIQLO Pay closed in January, what replaced it in the roadmap for online wallets outside Japan?"
2. "I noticed the Indonesia site lost QRIS, cards and GoPay in the same window on 28 July. Is that one upstream provider?"
3. "Your Vietnam stores take VNPay and the website doesn't. Is that a priority or a deliberate choice?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| H&M Group | hm.com | Sweden *(out of territory)* | Not sourced | JP, KR, CN, HK, SEA, IN, AU | Adyen (named in Adyen boilerplate; scope unknown) | https://www.adyen.com/press-and-media/adyen-provides-payments-solutions-to-xiaomi |
| Inditex (Zara) | inditex.com | Spain *(out of territory)* | Not sourced | Same | In-house InWallet (2016); PSP not found `[UNVERIFIED]` | https://uk.fashionnetwork.com/news/Payment-inditex-adopts-its-own-dedicated-app,715364.html |
| Shein | shein.com | Singapore | ~$38B (TAL, unverified) | Global incl. AU, JP, KR, SEA | Adyen + Checkout.com case studies `[UNVERIFIED]`; TAL says Juspay, no evidence found | https://www.checkout.com/resources/case-studies/local-payments-expertise-power-shein-s-global-expansion |
| Ryohin Keikaku (Muji) | muji.com | Japan | ~$4.5B (TAL, unverified) | JP, CN, HK, TW, KR, SEA, AU, IN | Unknown; own "MUJI passport Pay" `[UNVERIFIED]` | https://www.muji.com/jp/passport/pay/index.html |
| Cotton On Group | cottonongroup.com.au | Australia | ~$2B (TAL, unverified) | AU, NZ, SG, MY, HK, IN | **Adyen** (listed as Adyen merchant) | https://ecommercenews.com.au/story/uniqlo-operator-chooses-adyen-for-multiple-market-payments |
| Shimamura | shimamura.gr.jp | Japan | Not sourced | JP, TW | Not found | — |
| Adastria | adastria.co.jp | Japan | Not sourced | JP, CN, HK, TW | Not found | — |
| Mango | mango.com | Spain *(out of territory)* | Not sourced | APAC via franchise | Adyen `[UNVERIFIED — third-party listing]` | https://www.intershop.com/en/solution/adyen-online-payments |

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Love, Bonito | lovebonito.com | Fashion | SEA, HK, US | Adyen unified commerce `[UNVERIFIED]` | https://www.adyen.com/blog/love-bonito-adyen-unified-commerce-for-todays-empowered-shoppers |
| Zalora (GFG) | zalora.com | Fashion marketplace | SEA | BridgerPay orchestration (2021) `[UNVERIFIED]`; TAL: Adyen + Fiuu/Razer | https://bridgerpay.com/learn/bridger-stories/Jyg0jmdNvp2xUmIJedJ4 |
| Charles & Keith | charleskeith.com | Fashion | Asia, ME | Multi-currency omnichannel; PSP not researched | TAL |
| Zozo | zozo.com | Fashion marketplace (JP) | JP | Japanese apparel EC; domestic | TAL |
| A.S. Watson / Watsons | watsons.com | Health & beauty retail | 9 APAC markets | Omnichannel, store + app; no PSP found | `2-ready-to-outreach/watsons.md` |
| Lotte Shopping | lotteshopping.com | Retail | KR + Asia | **Its e-commerce division runs FRL Korea's IT systems** (KR privacy policy); FRL Korea JV partner | https://faq-kr.uniqlo.com/pkb_Home_UQ_KR?id=kA0Ie000000TO0Z&l=ko |
| Stylevana | stylevana.com | Beauty e-commerce | Global from HK | Authorize.Net / Braintree / PayPal; no orchestration | `2-ready-to-outreach/stylevana.md` |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| Zalora | BridgerPay `[UNVERIFIED — vendor story]` | 2021 | Fashion marketplace (SEA) | https://bridgerpay.com/learn/bridger-stories/Jyg0jmdNvp2xUmIJedJ4 |
| Reserva | Yuno `[UNVERIFIED — search summary]` | 2024-09 | Fashion (Brazil) | https://y.uno/post/reserva-partners-yuno |
| Al-Futtaim brands | Juspay `[UNVERIFIED]` | 2026-10 | Retail (UAE, out of territory) | https://enterpriseam.com/uae/2026/10/08/juspay-eyes-the-gccs-payment-fragmentation-to-orchestrate-growth/ |

*No verified case study found of a direct APAC apparel competitor adopting payment orchestration.*

**Pattern:** APAC fashion retail is heavily Adyen-consolidated: Cotton On, Love Bonito, H&M, UNIQLO. The story here is single-PSP concentration plus local-rail gaps, not stack fragmentation.

#### 11D. Prospect Scoring

Only verified signals score. Everything not shown is uncertain (0).

| Company | Signals verified | Points | Evidence Source |
|---------|-----------------|--------|-----------------|
| Cotton On Group | 3+ countries (AU, NZ, SG, MY, HK… per traffic file) ✅ +3; high traffic outside home ❌ (ANZ 43%) | 3+ (incomplete) | `accounts/traffic/cotton-on-group.md` |
| Shein | 3+ countries ✅ +3; outside home ✅ +2 | 5+ (incomplete) | TAL / traffic not checked |
| Muji | 3+ countries ✅ +3 `[from TAL; verify]` | ≤3 (incomplete) | TAL |
| Zalora | 3+ countries ✅ +3; multiple PSPs ⬜ (TAL only) | 3+ (incomplete) | TAL |

None of these have been researched; the scores are floors, not tiers.

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Shein | Competitor | Global | Not scored | Research | TAL Juspay flag (unverified) → possible displacement | ✅ |
| 2 | Cotton On Group | Competitor | ANZ, SEA | Not scored | Research | Adyen-consolidated, same pattern as UNIQLO | ✅ |
| 3 | Muji (Ryohin Keikaku) | Competitor | JP, Greater China, SEA | Not scored | Research | Japanese omnichannel, own app wallet | ✅ |
| 4 | Zalora | Peer | SEA | Not scored | Research | Orchestration-aware (BridgerPay, unverified) | ✅ |
| 5 | Love, Bonito | Peer | SEA, HK | Not scored | Research | Adyen unified commerce | ✅ |
| 6 | Charles & Keith | Peer | Asia | Not scored | Research | Multi-currency omnichannel | ✅ |
| 7 | Lotte Shopping | Peer / JV partner | KR, SEA | Not scored | Research | Runs FRL Korea's e-commerce IT | ✅ |
| 8 | **Adastria** | Competitor | JP, CN, HK, TW | Not scored | Research | Japanese apparel with Greater China stores | ❌ **Not in TAL: genuine find** |
| 9 | **Shimamura** | Competitor | JP, TW | Not scored | Low | Mostly domestic | ❌ Not in TAL |
| 10 | Zozo | Peer | JP | Not scored | Low | Domestic marketplace | ✅ |

H&M, Inditex and Mango are HQ'd west of Dubai, so they are out of territory and excluded.

**TAL hygiene:**
- Fast Retailing appears twice: "Fast Retailing (Uniqlo)" and "Uniqlo (Fast Retailing)". Merge them.
- Populate Payment Gateway with "Adyen (2022) + KR local PGs".
- Operating Countries "Japan" is wrong: 20+ countries.
- The "~$21B (FY24)" revenue is superseded: FY2026 is ≈US$25.0bn.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | ≈US$25.03bn (¥3.96tn, FY Aug 2026); FY Aug 2025 ¥3,400.5bn | FashionUnited; Yuho FY2025 |
| GMV / Gross Transaction Volume | E-commerce revenue FY2025: UNIQLO Japan ¥152.4bn, UNIQLO International ¥306.4bn (≈¥458.8bn; GU EC not disclosed) | Yuho FY2025, notes 6–7 |
| Average Transaction Value (USD) | Not published in absolute terms. UNIQLO Japan Sept 2026 average spend per customer was 111.3% YoY | https://www.fastretailing.com/eng/ir/monthly/index.html |
| Est. Annual Transactions | Not derivable without ATV | — |
| **Monthly transaction count** | ✅ **DERIVED (floor): ≥250,000/month (Japan EC alone); ≥760,000/month (UNIQLO EC total)**, at a ¥50,000/order ceiling I chose (not a sourced ATV). ¥152,364m ÷ 12 ÷ ¥50,000 ≈ 254k; + ¥306,429m ÷ 12 ÷ ¥50,000 ≈ 511k. In-store volume across 3,510 stores is excluded. Billing unit: online orders. | Yuho FY2025 |
| Active Customers / Users | Not found | — |
| Primary Currency | JPY, plus KRW, TWD, AUD, IDR, HKD, VND, THB, PHP, SGD, MYR, INR, CNY, USD, EUR, GBP… | Store per country |
| Top 3 Markets by Revenue | UNIQLO Japan ¥1,084.8bn (FY2026); Greater China ¥650.2bn (FY2025); KR+SEA+IN+AU combined ¥619.4bn (FY2025) | Segment data; Yuho p.45–46 |
| Billing channel split (web vs app store) | Not applicable: UNIQLO is merchant of record in its own apps. Web vs app vs store split not published | — |

---

### Overall Research Confidence

**Medium.**
- **Strong:**
  - Traffic: **supplied SimilarWeb**, with the caveats above (top-10 only, no apps, omnichannel).
  - Entities and financials: Fast Retailing's own Yuho and IR pages.
  - Local payment methods: UNIQLO's own help-centre pages for 12 storefronts, full method lists.
  - PSPs: Adyen press release plus the live KR and PH privacy policies.
- **Weak:**
  - Adyen's market scope and the Japan card acquirer are unknown.
  - No checkout walkthrough: the storefronts block automated access.
  - Complaints are thin.
  - Competitor stacks rest mostly on search summaries.
- The orchestration classification (and with it the tier) depends on an unanswered question about the HQ payment system.

---

### Manual Research Recommendations

> **Area:** Japan card acquirer / whether Japan runs on Adyen
> **Why it matters:** it decides whether the pitch is "add rails on top of Adyen" everywhere, or whether Japan runs a separate local gateway (a second integration estate).
> **Suggested manual action:** open uniqlo.com/jp checkout with DevTools and check the network calls for `checkoutshopper-live.adyen.com` or a Japanese gateway domain.

> **Area:** Does the HQ "payment system" route between processors?
> **Why it matters:** this is the +4 vs +1 orchestration award, and therefore ⭐ vs 🟢.
> **Suggested manual action:** ask in discovery: "When a card authorisation fails in Korea, can it retry on another processor?"

> **Area:** HK / TH / VN live checkout
> **Why it matters:** the help centres are the hook's evidence; confirm the live checkout matches before sending.
> **Suggested manual action:** use a VPN to reach uniqlo.com/hk, /th and /vn checkout and screenshot the method list.

> **Area:** Market-prominence citations
> **Why it matters:** the gap warnings in Section 4 need a source for Octopus, PromptPay, VNPay and GCash prominence.
> **Suggested manual action:** pull one central-bank or industry citation per market.

> **Area:** Monthly transaction count (precise)
> **Why it matters:** the derived floor is safe for the gate, but it is not a measurement.
> **Suggested manual action:** check the FY2026 Yuho (late Nov 2026) for EC revenue, and the fact book for customer counts.

---

### Appendix: All Source URLs

**Section 1:** `accounts/traffic/fast-retailing-uniqlo.md` (SimilarWeb, supplied 2026-10-19)

**Section 2:**
- https://www.fastretailing.com/eng/ir/library/pdf/yearendreport202508_eng.pdf
- https://www.uniqlo.com/tw/company/contract/
- https://faq-ph.uniqlo.com/pkb_Home_UQ_PH?id=kA0Ie000000TO39&l=en_US
- https://faq-kr.uniqlo.com/pkb_Home_UQ_KR?id=kA0Ie000000TO0Z&l=ko
- https://faq-au.uniqlo.com/articles/en_US/FAQ/Can-I-order-from-UNIQLO-in-a-different-country
- https://interview.tw/c/YqRp/info

**Section 3:**
- https://www.adyen.com/press-and-media/adyen-provides-omnichannel-payments-services-to-uniqlo
- https://www.retailbiz.com.au/?p=40313
- https://paymentnavi.com/?p=120105
- https://ecommercenews.com.au/story/uniqlo-operator-chooses-adyen-for-multiple-market-payments
- https://faq-kr.uniqlo.com/pkb_Home_UQ_KR?id=kA0Ie000000TO0Z&l=ko
- https://faq-ph.uniqlo.com/pkb_Home_UQ_PH?id=kA0Ie000000TO39&l=en_US
- https://faq-ph.uniqlo.com/pkb_Home_UQ_PH?id=kA0Ie000000TO2m&l=en_US
- https://netshop.impress.co.jp/node/4705
- https://faq.uniqlo.com/articles/FAQ/law/
- https://www2.smbc.co.jp/news/pdf/j20210119_01.pdf
- https://www.bcnretail.com/market/detail/20220203_264710.html
- https://www.fintechfutures.com/paytech/retailer-uniqlo-cuts-out-middlemen-with-own-payments-integration
- https://faq-id.uniqlo.com/pkb_Home_UQ_ID?id=kA0Ie000000TOPh&l=en_US
- https://faq-in.uniqlo.com/?l=en_US&c=category_uq:UQIN_CAT06_01

**Section 4:**
- Japan:
  - https://faq.uniqlo.com/articles/Knowledge/100001967/
  - https://faq.uniqlo.com/articles/Knowledge/100004123/
  - https://faq.uniqlo.com/articles/Knowledge/100006848/
  - https://faq.uniqlo.com/articles/Knowledge/100007763/
  - https://faq.uniqlo.com/articles/Knowledge/100005136/
  - https://faq.uniqlo.com/articles/Knowledge/100001980/
  - https://faq.uniqlo.com/articles/Knowledge/100004232/
  - https://faq.uniqlo.com/articles/Knowledge/100006473/
  - https://faq.uniqlo.com/articles/Knowledge/100001893/
- GU Japan:
  - https://faq.gu-global.com/articles/Knowledge/100001841/
  - https://faq.gu-global.com/articles/Knowledge/100001955/
  - https://faq.gu-global.com/articles/Knowledge/100005165/
- Korea:
  - https://faq-kr.uniqlo.com/pkb_Home_UQ_KR?id=kA0Ie000000TO9Y&l=ko
  - https://faq-kr.uniqlo.com/pkb_Home_UQ_KR?id=kA0fR0000000EJ7&l=ko
  - https://faq-kr.uniqlo.com/pkb_Home_UQ_KR?id=kA0fR0000000EKj&l=ko
  - https://faq-kr.uniqlo.com/pkb_Home_UQ_KR?id=kA0Ie000000TO9e&l=ko
- Taiwan:
  - https://faq-tw.uniqlo.com/pkb_Home_UQ_TW?id=kA0Ie000000TOxG&l=zh_TW
  - https://faq-tw.gu-global.com/pkb_Home_GU_TW?id=kA0Ie000000TOrs&l=zh_TW
- Australia:
  - https://faq-au.uniqlo.com/pkb_Home?id=kA0Ie000000TOwn&l=en_US
  - https://faq-au.uniqlo.com/pkb_Home?id=kA0Ie000000TOeD&l=en_US
  - https://faq-au.uniqlo.com/pkb_Home?id=kA0Ie000000TOwm&l=en_US
- Indonesia: https://faq-id.uniqlo.com/pkb_Home_UQ_ID?id=kA0Ie000000TOnp&l=en_US
- Hong Kong:
  - https://faq-hk.uniqlo.com/pkb_Home_UQ_HK?id=kA0fR0000000yLx&l=en_US
  - https://faq-hk.uniqlo.com/pkb_Home_UQ_HK?id=kA0Ie000000TOfo&l=en_US
  - https://faq-hk.gu-global.com/pkb_Home_GU_HK?id=kA0Ie000000TO7Z&l=zh_TW
- Vietnam:
  - https://faq-vn.uniqlo.com/pkb_Home_UQ_VN?id=kA0Ie000000TOQQ&l=en_US
  - https://faq-vn.uniqlo.com/pkb_Home_UQ_VN?id=kA0Ie000000TPBJ&l=en_US
- Singapore: https://faq-sg.uniqlo.com/pkb_Home_UQ_SG?id=kA0Ie000000TP7F&l=en_US
- Malaysia: https://faq-my.uniqlo.com/pkb_Home_UQ_MY?id=kA0Ie000000TP5i&l=en_US
- Thailand: https://faq-th.uniqlo.com/pkb_Home_UQ_TH?id=kA0Ie000000TOqj&l=en_US
- Philippines: https://faq-ph.uniqlo.com/pkb_Home_UQ_PH?id=kA0Ie000000TOyV&l=en_US
- India: https://faq-in.uniqlo.com/pkb_Home_UQ_IN?id=kA0Ie000000TP5H&l=en_US

**Section 5:**
- https://faq-au.uniqlo.com/articles/en_US/Knowledge/Do-you-offer-PayPal
- https://faq-id.uniqlo.com/pkb_Home_UQ_ID?id=kA0fR0000000SYz&l=en_US
- https://faq-id.uniqlo.com/articles/en_US/FAQ/UQID-Payment-Check
- https://faq-ph.uniqlo.com/articles/en_US/FAQ/How-to-Troubleshoot-Checkout-Errors
- https://www.trustpilot.com/review/uniqlo.com?page=3
- https://internet.watch.impress.co.jp/docs/news/1184354.html
- https://lifestyle.assist-all.co.jp/uniqlo-paypay-guide/

**Section 6:**
- https://fashionunited.com/news/business/uniqlo-international-drives-fast-retailings-16-6-percent-revenue-growth-in-fy2026/2026100875091
- https://www.fastretailing.com/eng/ir/financial/segment_5yrs.html
- https://www.fastretailing.com/eng/ir/financial/outlets.html
- https://www.fastretailing.com/eng/ir/monthly/index.html
- https://tribune.net.ph/2026/09/08/uniqlo-expands-philippine-footprint-with-six-stores
- https://insideretail.asia/2026/07/27/uniqlo-eyes-100-plus-stores-in-india-by-2031/
- https://en.vietstock.vn/2026/03/uniqlo-to-open-new-store-in-ha-noi-974-629709.htm

**Section 7:**
- https://netshop.impress.co.jp/node/14872
- https://faq-au.uniqlo.com/pkb_Home?id=kA0Ie000000TOwm&l=en_US
- https://www.adyen.com/press-and-media/adyen-provides-omnichannel-payments-services-to-uniqlo
- https://www2.smbc.co.jp/news/pdf/j20210119_01.pdf

**Section 11:**
- https://www.adyen.com/press-and-media/adyen-provides-payments-solutions-to-xiaomi
- https://uk.fashionnetwork.com/news/Payment-inditex-adopts-its-own-dedicated-app,715364.html
- https://www.checkout.com/resources/case-studies/local-payments-expertise-power-shein-s-global-expansion
- https://www.muji.com/jp/passport/pay/index.html
- https://ecommercenews.com.au/story/uniqlo-operator-chooses-adyen-for-multiple-market-payments
- https://www.intershop.com/en/solution/adyen-online-payments
- https://www.adyen.com/blog/love-bonito-adyen-unified-commerce-for-todays-empowered-shoppers
- https://bridgerpay.com/learn/bridger-stories/Jyg0jmdNvp2xUmIJedJ4
- https://y.uno/success-cases/reserva
- https://y.uno/post/reserva-partners-yuno
- https://enterpriseam.com/uae/2026/10/08/juspay-eyes-the-gccs-payment-fragmentation-to-orchestrate-growth/

</details>
