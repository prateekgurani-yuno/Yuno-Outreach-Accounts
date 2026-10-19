# Shangri-La

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 21 / 29 → ⭐ **High Priority** *(no override; see breakdown for why it was considered and rejected)*
**Industry:** Hospitality & Lodging (luxury hotel owner-operator; TAL row mis-tags it as an OTA) · **HQ:** Shangri-La Asia Limited (Bermuda-incorporated, HKEX 0069); website, app and payments operated by Shangri-La International Hotel Management Limited, Quarry Bay, Hong Kong · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** 🛠️ **IN-HOUSE: Shangri-La built and runs its own central payment layer (`pay.shangri-la.com`, internally "paycenter" / "CashierPlatform").** It already routes each payment method to a different gateway. Do not tell them they need orchestration. The argument is method coverage and the cost of building every new connector in-house.

---

> ## ⭐ THE FINDING: Shangri-La built its own cashier, and it only speaks China and cards
>
> I pulled `www.shangri-la.com`, its Next.js bundles and the cashier bundles myself on 2026-10-19. All returned HTTP 200:
> - `s.shangri-la.com/sl-fe-pay-prod/js/payment.a4b2676032c4bd7beb66.js` (1.89 MB)
> - `s.shangri-la.com/sl-fe-h5pay-prod/js/index.476aa032b1.js` (0.75 MB)
>
> **1. There is one central cashier, and it settles money.** The site's `_app` bundle hard-codes the production payment environment:
>
> ```js
> env:"prod", websiteHost:"//www.shangri-la.com", paymentHost:"//pay.shangri-la.com"
> payUrl:"https://pay.shangri-la.com/paycenter/api/client"   // app / mobile
> pay:"/paycenter/api/website/", appPay:"/paycenter/api/client"
> ```
>
> Every paid flow on the site hands off to this cashier with a `transactionId`:
> - `"/{locale}/pay/?transactionId={transactionId}&hotelCode={hotelCode}"` serves a page titled **"New Reservation"**, so room bookings go through it.
> - `"/{locale}/pay-common/?transactionId=…&successRedirect=…"` serves in-room dining orders (`createIRDOrder`, with `PREPAY` as a pay method).
> - Fast check-in deposit (`getFastCheckInPayInfo` → `payForm.cashierUrl`, page events `PREAUTH` / `PREAUTH_UNAVAILABLE`) also goes through the cashier, as do parking, pre-arrival upsell carts and the WeChat Mini Program (`openMpNative({url: …pay, query:{transactionId…}})`).
>
> This is the opposite of Mandarin Oriental, Langham and Peninsula. Their central sites only capture a card guarantee and leave settlement to each property. **Shangri-La's central layer actually takes payments.**
>
> **2. It already routes by method to multiple gateways.** The cashier asks the server for `payWays` per transaction, then picks a gateway per card type with `payGateway = getPayGateway(cardType, payWays)`. The gateway identifiers in the shipped code, verbatim, are:
>
> ```js
> ["ALIPAY_CHINA","ALIPAY_GLOBAL","INGENICO_ALIPAY","INGENICO_UNIONPAY","ADYEN_WECHAT_PAY"]
> ```
>
> - **Adyen is live.** The bundle loads `https://checkoutshopper-live.adyen.com/checkoutshopper/sdk/6.3.0/adyen.js` with `environment:"live"` and a live client key (`live_C5QZ…`, redacted). It is used *only* to render the WeChat Pay QR code: `AdyenCheckout(f).then(t => t.createFromAction(e,{countdownTime:15}).mount("#wechatQrCodeContainer"))`.
> - **Ingenico carries Alipay and UnionPay.** Ingenico's online arm is the 2015/2018 "global payment partner" ([chinatechnews, 30 Jan 2018](https://www.chinatechnews.com/2018/01/30/25637-ingenico-integrates-seamless-payment-capability-in-shangri-las-next-generation-mobile-app)).
> - **Alipay is also connected directly**, as two separate gateways (China and Global).
> - **Forter** device tokens (`forterSiteId`, `forterTokenCookie`) handle fraud screening. **Geetest** handles the CAPTCHA.
>
> **3. Card data goes to Shangri-La's own servers, not to a PSP iframe.** The card form is Shangri-La's own fields (`cardNumber`, `expMonth`, `expYear`, `cvv`). They are serialised as `cardInfo: Base64.encode(JSON.stringify(card))` with `encryptVersion:"0"`, signed, and POSTed to the paycenter. Cards can also be saved (`saveCardWithGc`, `cardList`, `creditTokenUsable`). 3DS2 browser data is gathered client-side (`challengeCanvasSize`, `colorDepth`, `screenWidth`…) and sent with the request. **The card gateway or acquirer is chosen server-side, so it is not visible.** `[INFERENCE, not confirmed]`: Shangri-La very likely runs its card flow in full PCI DSS scope (SAQ D-type) and tokenises cards itself.
>
> **4. What the cashier can take, and what it cannot.**
>
> | | Status in the cashier code |
> |---|---|
> | Visa, Mastercard, Amex, JCB, Diners, UnionPay | ✅ Present (card-brand images and logic) |
> | Alipay (China and Global), WeChat Pay | ✅ Present (gateway codes above) |
> | **Apple Pay** | ❌ **0 occurrences.** Yet 7 of the 8 property pages I checked list `APPLEPAY` in their "Online payment methods we accept at selected platforms" block. |
> | GCash, Maya, PayNow, FPX, DuitNow, PromptPay, UPI, PayPay, konbini, PayPal, Google Pay, Afterpay | ❌ 0 occurrences each |
>
> **The #1 traffic market is the Philippines (13.78%), and the payment layer Shangri-La built has no Philippine rail in it.** The same is true for Malaysia (#5), Singapore (#6), Thailand (#10), India (#8) and Japan (#9). The cashier's entire non-card vocabulary is built for the mainland Chinese guest. That guest is #7 by web traffic (4.62%), even though Mainland is the largest revenue market (US$627.9M FY25).
>
> ⚠️ **What this does NOT establish, and I will not claim:**
> - **Who the card acquirer is.** No card gateway name appears client-side.
> - **What share of room revenue settles through the cashier rather than at the property folio.** Guarantee-only rates still settle at checkout via OPERA/Infrasys.
> - **Whether the Ingenico contract is still with Worldline today.**

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:**
- Shangri-La is Hong Kong's largest listed hotel group: **107 hotels, ~42.6k rooms** at 30 Jun 2026 ([H1 2026 interim, HKEX](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0827/2026082700608.pdf)).
- Brands: Shangri-La, Kerry, JEN, Traders and the new Shangri-La Signatures.
- **FY2025 revenue US$2,234.1M**, of which rooms US$1,107.5M and F&B US$766.7M ([FY2025 results, HKEX](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0326/2026032600950.pdf)).
- Unlike its HK luxury peers, it built its own booking engine *and* its own central cashier.

**SimilarWeb total visits (last full month):**
- **~1.727M/month** (shangri-la.com, Jul–Sep 2026 average; 5.181M over 3 months). Source: SimilarWeb (supplied 2026-10-19).
- Caveats: Sales Intelligence view, so the top 10 countries carry share only. Desktop plus mobile web only, **no app traffic**. App, OTA and on-property payments are invisible here.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | Philippines | 13.78% | Cards (Visa/MC/Amex/JCB/Diners/UnionPay), Alipay | **GCash, Maya, InstaPay** (absent from the cashier code); Apple Pay is advertised but not in the cashier | ✅ 5 hotels; owning entity "Makati Shangri-La Hotel and Resort, Inc." named in a directory |
| 2 | United States | 11.46% | Cards, Alipay | Apple Pay (advertised, not in the cashier), PayPal, Google Pay | ❌ No US property or entity. All US traffic books cross-border into Asia. |
| 3 | Australia | 9.36% | Cards, Alipay | Apple Pay (advertised, not in the cashier). Afterpay/PayTo are low relevance for hotel stays. | ⚠️ Sydney and Cairns hotels, owned 100%; local entity name not found |
| 4 | Hong Kong | 7.47% | Cards, Alipay | FPS, PayMe, Octopus. AlipayHK is ⬜ unclear (it may sit behind `ALIPAY_GLOBAL`). | ✅ Shangri-La International Hotel Management Ltd (data controller) |
| 5 | Malaysia | 5.52% | Cards (no Diners or Alipay listed for KL) | **FPX, DuitNow, Touch 'n Go eWallet** | ✅ Shangri-La Hotels (Malaysia) Berhad, Bursa 5517, 52.78% owned |

### Legal entities
- **Shangri-La Asia Limited** (Bermuda; HKEX 0069, secondary listing SGX). Listed parent. Registration number not found.
- **Shangri-La International Hotel Management Limited** (Hong Kong). Website, app and data controller; footer copyright holder.
- **Shangri-La Hotel Public Company Limited** (Thailand, SET: SHANG; 73.61%). Named as a Thailand data controller in the privacy policy.
- **Shangri-La Hotels (Malaysia) Berhad** (Malaysia, Bursa 5517; 52.78%).
- **Makati Shangri-La Hotel and Resort, Inc.** (Philippines). Named by directory only.
- **Shangri-La Hotels Pte Limited** (UK representative) and **Shangri-La Hotels (Paris)** (EU representative). Data-protection representatives only.

### Known PSPs
- **Adyen**: `[Source Code]`, live Web SDK 6.3.0 used for WeChat Pay (`ADYEN_WECHAT_PAY`). Global.
- **Ingenico (now Worldline?)**: `[Source Code]` gateway codes `INGENICO_ALIPAY` and `INGENICO_UNIONPAY`, plus `[Press Release]` global partner 2015/2018. Global.
- **Alipay direct**: `[Source Code]` `ALIPAY_CHINA` and `ALIPAY_GLOBAL`. China and outbound Chinese travellers.
- **Forter**: `[Source Code]` fraud screening. Not a PSP.
- **Card gateway/acquirer: not identified.** It is server-side, behind the paycenter.

### Orchestration status
**In-house orchestration layer.** `pay.shangri-la.com/paycenter` is a first-party cashier serving the website, the app and the WeChat Mini Program.
- It selects a gateway per payment method via `getPayGateway(cardType, payWays)`.
- At least four gateway connectors are live: Adyen, Ingenico, Alipay China and Alipay Global.
- Evidence: `[Source Code]`, shangri-la.com `_app` bundle and `sl-fe-pay-prod/js/payment.a4b2676032c4bd7beb66.js`, fetched 2026-10-19.

### Buying signals
- 🚀 **Openings within the last 12 months:**
  - Shangri-La and Traders Hongqiao Airport (Oct 2025; Traders brand relaunch)
  - Shangri-La Kunming (Apr 2026)
  - JEN Hangzhou (Aug 2026)
  - Kyoto (77 keys) projected for 2026
  - Source: [H1 2026 interim](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0827/2026082700608.pdf)
- 🤝 **Mastercard group-level cardholder campaign** across HK, SG, KL and Bangkok (Island Shangri-La "Mastercard Exclusive", 5 Oct–30 Dec 2026). This is card-scheme marketing, not acquiring. ([offer page](https://www.shangri-la.com/hongkong/islandshangrila/offer-detail/rooms-suites/isl-mastercard-exclusive-stay-above-the-city-room-package/))
- 💼 **Leadership:**
  - Kuok Hui Kwong became Chairman *and* Group CEO, 1 Aug 2025
  - New Group CFO Teo Nee Chuan from 30 Mar 2026 [UNVERIFIED — search summary only, page not fetched]
  - Source: [H1 2026 interim](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0827/2026082700608.pdf)
- 💰 **RMB 3.2bn of Panda bonds** issued Apr and Jun 2026. This is debt, not an equity round, so it is not scored. ([H1 2026 interim](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0827/2026082700608.pdf))

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Shangri-La` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 21 / 29
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | **+5** | See the full workings below. |
| Orchestration status | **+1** | ✅ **In-house orchestration layer.** First-party paycenter with per-method gateway selection across Adyen, Ingenico and two Alipay connectors (Section 3B). This is the hardest motion: argue reach and opportunity cost. |
| 3+ countries | **+3** | ✅ All 10 listed markets are above 1% share (PH 13.78% … TH 3.76%), plus ~24 countries of operation in the FY25 portfolio. |
| Multiple PSPs | **+3** | ✅ Adyen (live SDK) plus Ingenico (gateway codes) plus Alipay direct, all in shipped code (Section 3A). |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Philippines (#1, 13.78%): no GCash, Maya or InstaPay.** Absence is sourced from Shangri-La's own cashier code (0 occurrences) and from the `paymentModeList` of Makati and EDSA, which lists cards, Alipay and Apple Pay only. |
| Recent expansion | **+2** | ✅ Hongqiao Airport (Oct 2025), Kunming (Apr 2026), JEN Hangzhou (Aug 2026), all within 12 months ([H1 2026 interim](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0827/2026082700608.pdf)). ⚠️ These are new cities and brands inside existing countries, not new countries. Awarded for consistency with the Mandarin Oriental and Rosewood scoring, but it is the weakest +2 on the sheet. |
| Payment issues reported | 0 | ❌ Only isolated property-folio complaints (deposit or late-checkout disputes); no online payment-failure pattern (Section 5). |
| Funding >$10M | 0 | ❌ Listed company with no equity round. The RMB 3.2bn Panda bonds are debt and deliberately not scored. |
| High traffic outside home | **+2** | ✅ Hong Kong is 7.47% of traffic; 92.5% is outside HK. |
| Competitor using orchestration | **+2** | ✅ Radisson Hotel Group → CellPoint Digital ([case study, 2 Sep 2025, fetched](https://cellpointdigital.com/articles/casestudies/payment-orchestration-as-a-growth-catalyst-the-radisson-hotel-group-case-study)). Agoda, which competes for the same room nights, → Juspay [UNVERIFIED — search summary only, page not fetched]. |
| Payment job postings | 0 | ❌ None found. |

**Monthly transaction count, full workings (+5):**
- ✅ **DERIVED: ~537,000 room nights/month**, calculated as US$1,107.5M FY25 rooms revenue ÷ US$172 owned-hotel ADR ÷ 12. Both inputs are audited ([FY2025 results](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0326/2026032600950.pdf)). Approximate, because the ADR basis includes associates.
- **Billing unit:** a stay (folio), not a night. Converting nights to stays needs average length of stay, which was **not found**. The ≥100k band holds for any average stay up to 5.3 nights `[ASSUMPTION — ALOS not researched]`.
- **F&B** (US$766.7M) adds a large separate volume of on-property transactions.
- ⚠️ **The number that matters is unknown:** how many of these settle through `pay.shangri-la.com` rather than at a property terminal.

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **⭐ High Priority (21)**

**Override considered and rejected.**
- *Reasons for a downgrade:*
  - In-house is the hardest motion.
  - The card acquirer is unidentified.
  - Guarantee-only bookings still settle at the property.
- *Reasons it stays ⭐:*
  - **The account clears the bar without the weakest rows.** Remove the soft recent-expansion +2 and it is still 19. Remove the transaction-count +5 as well and it is 14.
  - Mandarin Oriental was overridden down at 17 *because its central tier does not settle money*. Shangri-La's does: prepaid rates, deposits, in-room dining, upsells, parking and Mini Program payments all run through the paycenter.
  - The gap is concrete and sourced from their own code: zero SEA rails in a cashier whose top markets are all SEA.
- **Discovery must open with the settled-volume question.**

### Source Notes
- ✅ Central cashier, gateway codes, Adyen live SDK, Forter, raw-PAN card form: shangri-la.com and s.shangri-la.com bundles, fetched 2026-10-19 (paths in the Appendix).
- ✅ `paymentModeList` for 8 properties: fetched 2026-10-19.
  - Sydney, Tokyo, EDSA Manila, Kowloon: `AMEX, CHINAUNIONPAY, DINERS, JCB, MASTERCARD, VISA, ALIPAY, APPLEPAY`
  - Singapore: no Alipay
  - Kuala Lumpur: no Diners, no Alipay
  - Pudong: WeChat Pay, no Apple Pay
  - Bangkok: all nine logos
- ✅ Financials, portfolio and stakes: HKEX FY2025 and H1 2026 PDFs.
- ✅ Ingenico global partnership (2018): [chinatechnews](https://www.chinatechnews.com/2018/01/30/25637-ingenico-integrates-seamless-payment-capability-in-shangri-las-next-generation-mobile-app), fetched by Agent 4.
- ⚠️ AsiaPay lists "Shangri-La" as a client ([ThePaypers](https://thepaypers.com/company/AsiaPay/50)). [UNVERIFIED — search summary only, page not fetched]. **Not seen in the cashier code.**
- ⚠️ Pace BNPL at Malaysian property POS, Apr 2022 ([Business Today](https://www.businesstoday.com.my/2022/04/07/shangri-la-hotels-and-resorts-teams-up-with-pace-offering-first-ever-bnpl-payments/)). [UNVERIFIED — search summary only, page not fetched]. Pace's current status is unknown.
- ⚠️ CRS history: Sabre SynXis (2008/2010) and OPERA (2004). PMS standard: OPERA plus Infrasys POS, from a job ad. All [UNVERIFIED — search summary only, page not fetched]. The current front-end booking flow is first-party (`hotelOrderService.createBooking`), not `be.synxis.com`.
- ⚠️ The TAL row tags Shangri-La as "Travel & Online Agencies (OTAs)". **This is wrong**; it should be Hospitality & Lodging.

### Success Case Alternatives
- **No Yuno hospitality case was verified in this run.** Do not name one in outreach until it is confirmed internally.
- Profile to match: an APAC merchant with an existing in-house cashier that added local wallets through a single integration rather than per-gateway builds.
- Pick from the internal case library, then cite it.

---

## Executive Summary

- **Who they are:** Shangri-La Asia (HKEX 0069) runs 107 hotels with FY25 revenue of US$2.23bn. Web traffic is led by the Philippines, the US and Australia, not Hong Kong.
- **Key payment finding:** unlike every HK luxury peer in this repo, it has **built its own central payment layer**. `pay.shangri-la.com/paycenter` settles room prepayments, deposits, in-room dining and Mini Program payments. It routes by method to Adyen (WeChat Pay), Ingenico (Alipay, UnionPay) and two direct Alipay connectors, and takes raw card data into Shangri-La's own servers.
- **The opportunity:** that layer was built for one corridor. It carries **no rail for the Philippines, Malaysia, Singapore, Thailand, India or Japan**. Apple Pay is advertised on property pages but absent from the cashier code.
- **Motion: in-house.** Position Yuno as the connector layer under their own cashier, not as a replacement.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** path 1, **SimilarWeb (supplied 2026-10-19)** from `accounts/traffic/shangri-la.md`. Sales Intelligence view, Jul–Sep 2026, worldwide, desktop plus mobile web, single domain `shangri-la.com`.

**Caveats from the supplied file:**
1. **Share only.** Per-country visits are not in the source, so the figures below are derived as share × 1.727M avg monthly visits.
2. **Single domain.** Nothing else is combined; no regional ccTLDs were found (all brands sit under shangri-la.com paths).
3. **No mobile-app traffic.**
4. Shangri-La Circle app bookings, OTA bookings and on-property folio/POS payments are not in web traffic. **Treat this as a market-mix signal, not a payment-volume split.**
5. Global rank was not captured. Trend was not supplied.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | Philippines | 13.78% | ~238k [DERIVED from supplied share, not a SimilarWeb figure] | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | United States | 11.46% | ~198k [DERIVED] | Not supplied | same |
| 3 | Australia | 9.36% | ~162k [DERIVED] | Not supplied | same |
| 4 | Hong Kong | 7.47% | ~129k [DERIVED] | Not supplied | same |
| 5 | Malaysia | 5.52% | ~95k [DERIVED] | Not supplied | same |
| 6 | Singapore | 5.02% | ~87k [DERIVED] | Not supplied | same |
| 7 | China | 4.62% | ~80k [DERIVED] | Not supplied | same |
| 8 | India | 4.22% | ~73k [DERIVED] | Not supplied | same |
| 9 | Japan | 4.11% | ~71k [DERIVED] | Not supplied | same |
| 10 | Thailand | 3.76% | ~65k [DERIVED] | Not supplied | same |

- Top 10 = 69.32%. The remaining 30.68% is unlisted.
- **High priority (>5%):** PH, US, AU, HK, MY, SG.
- **Device split:** 68.35% mobile web.
- **No local property or entity:** the **United States (#2)** has none. **India (#8)** has one managed hotel left (New Delhi) after the Bengaluru agreement terminated at end-Aug 2026 ([H1 2026 interim](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0827/2026082700608.pdf)).
- **China reads low** at 4.62% even though it is the largest revenue market (US$627.9M FY25). This is very likely because mainland guests book through the WeChat Mini Program and app, which web traffic does not capture `[INFERENCE, not confirmed]`.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:**
- Shangri-La Asia Limited is incorporated in Bermuda (Victoria Place, 5/F, 31 Victoria St, Hamilton). Primary listing HKEX 0069, secondary listing SGX.
- Operating HQ: Kerry Centre, 683 King's Road, Quarry Bay, Hong Kong.
- First hotel: Singapore, 1971 [background only; not sourced in this run].

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Bermuda / HK | Shangri-La Asia Limited | Not found | [FY2025 results](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0326/2026032600950.pdf) |
| Hong Kong | Shangri-La International Hotel Management Limited | Not found | [Privacy policy](https://www.shangri-la.com/en/tokyo/shangrila/privacy-policy); website footer |
| Thailand | Shangri-La Hotel Public Company Limited (SET: SHANG), 73.61% | Not found | Privacy policy; FY25 PDF |
| Malaysia | Shangri-La Hotels (Malaysia) Berhad (Bursa 5517), 52.78% | Not confirmed | FY25 PDF |
| Philippines | Makati Shangri-La Hotel and Resort, Inc. | Not found | [AHK directory](https://philippinen.ahk.de/en/membership/members-directory/makati-shangri-la-hotel-and-resort-inc) |
| Philippines | Shang Properties Inc. (co-owner of Shangri-La The Fort; Group 40%) | Not found | FY25 PDF; [Zawya](https://www.zawya.com/company/4295886104/shang-properties) [UNVERIFIED — search summary only, page not fetched] |
| UK | Shangri-La Hotels Pte Limited (UK representative) | Not found | Privacy policy |
| France | Shangri-La Hotels (Paris) (EU representative) | Not found | Privacy policy |
| AU, JP, SG, CN, HK hotels | Owning entities not named in filings | Not found | — |

**Properties in top markets** (from the FY25 and H1 2026 PDFs):

| Market | Properties |
|---|---|
| PH | 5 hotels, 2,660 rooms (Makati, EDSA, Mactan, Boracay, The Fort) |
| AU | Sydney, Cairns. Melbourne is under development. |
| HK | Island, Kowloon, Kerry, JEN |
| MY | 6 owned |
| SG | 4 |
| CN | ~19.7k owned rooms plus 8 managed |
| IN | New Delhi (managed) |
| JP | Tokyo (leased); Kyoto due 2026 |
| TH | Bangkok, Chiang Mai |
| US | **none** |

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| Philippines | #1 | ✅ Properties; one owning entity named | No gate sourced | Low for settlement at PH hotels |
| United States | #2 | ❌ No property | N/A (the guest is the cross-border party) | **High.** US-issued cards paying for Asian stays are cross-border by definition. |
| Australia | #3 | ⚠️ Properties, entity not named | No gate sourced | Low for AU hotels; AU guests abroad are cross-border |
| Hong Kong | #4 | ✅ | No gate sourced | Low |
| Malaysia | #5 | ✅ Berhad | No gate sourced | Low |
| Singapore | #6 | ⚠️ Properties, entity not named | No gate sourced | Low |
| China | #7 | ⚠️ Properties, entity not named | Not verified this run, so not claimed | Handled via Alipay/WeChat connectors |
| India | #8 | ❌ No owned property; 1 managed | Not verified this run, so not claimed | Medium (outbound Indian guests) |
| Japan | #9 | ⚠️ Leased Tokyo | Not verified | Low |
| Thailand | #10 | ✅ PCL | Not verified | Low |

> *"Warning: Potential cross-border operation in the United States. No local entity found. Transactions are likely processed cross-border, with higher scheme costs, lower approval rates and FX exposure."*
>
> Note the direction. These are US-issued cards paying for stays in Asia. **Which acquirer, in which country, processes a US card on a prepaid Manila booking is the discovery question.**

> **MANUAL:** Confirm the merchant-of-record entity on a prepaid booking receipt (card descriptor) for one PH, one AU and one HK property.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Global | **Adyen**: live Web SDK 6.3.0; gateway `ADYEN_WECHAT_PAY` (WeChat Pay QR via `createFromAction`) | `[Source Code]` | `https://s.shangri-la.com/sl-fe-pay-prod/js/payment.a4b2676032c4bd7beb66.js` (fetched 2026-10-19) |
| Global | **Ingenico** (online arm now Worldline, per background knowledge; **current contract not verified**): gateways `INGENICO_ALIPAY`, `INGENICO_UNIONPAY` | `[Source Code]` `[Press Release]` | same bundle; [chinatechnews 2018](https://www.chinatechnews.com/2018/01/30/25637-ingenico-integrates-seamless-payment-capability-in-shangri-las-next-generation-mobile-app) |
| China / outbound CN | **Alipay** direct: `ALIPAY_CHINA`, `ALIPAY_GLOBAL` | `[Source Code]` `[Third-Party Report]` | same bundle; [Marketing-Interactive](https://www.marketing-interactive.com/shangri-la-rolls-out-alipays-online-payment-service-globally) |
| China | **WeChat Pay** (Mini Program and Pay SDK) | `[Source Code]` `[Terms/Privacy Policy]` | `isWechatMiniProgram` / `openMpNative` in the dining bundle; the privacy policy lists the WeChat Payment SDK and Alipay Payment SDK |
| Global | **Forter** (fraud, not a PSP) | `[Source Code]` | payment bundle (`forterSiteId`) |
| HK / SEA? | **AsiaPay** (PayDollar), client-list mention only | `[Third-Party Report]` | [ThePaypers](https://thepaypers.com/company/AsiaPay/50) [UNVERIFIED — search summary only, page not fetched]. Not present in the cashier code. |
| Malaysia (POS) | **Pace** BNPL, 2022 | `[Third-Party Report]` | [Business Today](https://www.businesstoday.com.my/2022/04/07/shangri-la-hotels-and-resorts-teams-up-with-pace-offering-first-ever-bnpl-payments/) [UNVERIFIED — search summary only, page not fetched] |
| Global | Onyx Payments (travel-agent commission, not guest payments) | `[Third-Party Report]` | [BTN](https://www.breakingtravelnews.com/focus/article/onyx-payments-renews-shangri-la-international-hotel-management-ltd.-for-glo/) [UNVERIFIED — search summary only, page not fetched] |
| All | **Card gateway/acquirer** | — | **Not found.** It is selected server-side. |

**Single-PSP dependency:**
- No single-PSP dependency for wallets.
- **For cards it is unknown.** The card gateway is not exposed client-side.

#### 3B. Payment Orchestrator

**Classification: In-house orchestration layer** `[Source Code]`.

`pay.shangri-la.com/paycenter` exposes two APIs, `/paycenter/api/website` and `/paycenter/api/client`.
- **Channels it serves:** website, app, WeChat Mini Program.
- **Flows it serves:**
  - room booking (`/pay/?transactionId&hotelCode`)
  - in-room dining
  - fast check-in pre-auth deposit
  - parking
  - pre-arrival upsell cart
  - points and voucher purchases (`couponService.createOrder`, `payType: POINTS`)
- **How it routes:**
  - The server returns `payWays`.
  - The client resolves `payGateway` per card type, and the server returns a `payAction` of `REDIRECT`, `QRCODE` or a status.
  - At least 4 gateway connectors are live.

> Shangri-La has built what amounts to an orchestration layer. The opening is not "you need orchestration". It is: **every new rail is a new connector your team builds and maintains, and the connectors you built cover one corridor.**

- No third-party orchestrator was found: Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, VGS and Yuno were all searched with zero hits (Agent 2).
- The TAL `Payment Orchestrator` column is blank.

> **MANUAL:** Make a test booking on a prepaid rate (e.g. Makati, Members Online Saver Rate) with DevTools open. The `pay` service response's `payWays[].name` will name the card gateway that the front end does not.

---

### Section 4: Alternative & Local Payment Methods

Two evidence sources were used:
- **(a) Cashier code**, which is what can actually be paid online.
- **(b) The property-page `paymentModeList`**, which is what Shangri-La advertises under "Online payment methods we accept at selected platforms".

Both were fetched 2026-10-19.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| Global | Visa, Mastercard, Amex, JCB, Diners, UnionPay | Cards | Active in checkout (cashier code) | payment bundle; property pages |
| Global / CN | Alipay | Digital wallet | Active in checkout | `ALIPAY_CHINA` / `ALIPAY_GLOBAL` / `INGENICO_ALIPAY` |
| CN (Pudong, Bangkok) | WeChat Pay | Digital wallet | Active in checkout | `ADYEN_WECHAT_PAY`; `paymentModeList` at Pudong and Bangkok |
| Global (7 of 8 properties) | **Apple Pay** | Digital wallet | **Mentioned in docs only.** Advertised in `paymentModeList`; **absent from the cashier code**. It may be on-property NFC. | property pages vs bundle |
| Philippines | **GCash / Maya / InstaPay** | Wallet / A2A | **Not found** (0 in code; not in Makati or EDSA lists). GCash appears only as a points-redemption eGift card. | bundle; [eGift page](https://www.shangri-la.com/corporate/shangrilacircle/redeem-points/lifestyle/product-categories/egift-cards/philippines/gcashphp2000/) [UNVERIFIED — search summary only, page not fetched] |
| Malaysia | FPX / DuitNow / Touch 'n Go | A2A / wallet | **Not found** online. GrabPay and Maybank QR are reported on-property at Tanjung Aru F&B [UNVERIFIED — search summary only, page not fetched]. | bundle |
| Malaysia | Pace BNPL | BNPL | Mentioned in press (POS, 2022, status unknown) | see 3A |
| Singapore | PayNow / GrabPay | A2A / wallet | Not found | bundle |
| Hong Kong | FPS / PayMe / Octopus | A2A / wallet | Not found. AlipayHK: Unknown (may route via `ALIPAY_GLOBAL`). | bundle |
| India | UPI / RuPay / EMI | A2A / card / instalments | Not found | bundle |
| Japan | PayPay / konbini | Wallet / cash | Not found (JCB present) | bundle |
| Thailand | PromptPay / TrueMoney | A2A / wallet | Not found. A KTC Mastercard promo runs on a designated booking site [UNVERIFIED — search summary only, page not fetched]. | bundle |
| Australia | Afterpay / Zip / PayTo | BNPL / A2A | Not found (low relevance for hotel stays) | bundle |
| Global | PayPal / Google Pay | Wallet | Not found | bundle |
| PH / ID | Bank 0% card instalments (Metrobank, OCBC) | Instalments | Bank-run promos at Shangri-La-named malls or hotels, not in Shangri-La's checkout [UNVERIFIED — search summary only, page not fetched] | Agent 3 |

> *"Warning: In the Philippines, GCash is widely used but not currently supported by Shangri-La."*
>
> Prominence source: 24.4M GCash users verified via National ID, stated as 61% of onboarded users ([context.ph, 8 Sep 2026](https://context.ph/2026/09/08/over-24m-gcash-users-verified-with-national-id/)) [UNVERIFIED — search summary only, page not fetched]. Confirm the figure before using it in an email.

**Currency:** the property JSON carries a 36-currency `currencyList`, which looks like a display converter. The charge currency was not verified. Ingenico's 2018 release says "more than 20 currencies" [UNVERIFIED — search summary only, page not fetched].

> **MANUAL:** Over a PH VPN, step through a Makati prepaid booking to the cashier and screenshot the method list. Repeat for KL.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Deposit refund / overcharge (property folio, Qiantan Shanghai) | Travel Weekly Asia | Isolated | Undated | [link](https://www.travelweekly-asia.com/Hotels/Shanghai/Shangri-La-Qiantan-Shanghai-p57901479) [UNVERIFIED — search summary only, page not fetched] |
| Late-checkout charge dispute (EDSA Manila) | thefilam.net / Trustpilot | Isolated | Undated | [thefilam](https://thefilam.net/archives/10158) [UNVERIFIED — search summary only, page not fetched] |
| Deposit charged on an OTA-prepaid stay (Lhasa) | Traveloka | Isolated | Undated | [Traveloka](https://www.traveloka.com/en-th/user/review/consumption/HOTEL/GENERAL/1000000455649) [UNVERIFIED — search summary only, page not fetched] |
| Voucher not usable online (London) | Trustpilot | Isolated | Undated | [Trustpilot](https://nl-be.trustpilot.com/review/www.shangri-la.com) [UNVERIFIED — search summary only, page not fetched] |

- No online payment-failure pattern was found on Reddit, X, Trustpilot or in the Shangri-La Circle app reviews.
- **Do not use complaints as an angle.**

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | Aug 2026 | JEN Hangzhou opens (managed); Bengaluru management agreement terminates at end-Aug | Market Expansion / exit | [H1 2026 interim](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0827/2026082700608.pdf) |
| 2 | Apr–Jun 2026 | RMB 1.2bn and RMB 2.0bn Panda bonds issued | Funding (debt) | same |
| 3 | Apr 2026 | Shangri-La Kunming opens; Traders management agreements signed for Harbin and Zhengzhou | Market Expansion | same |
| 4 | 30 Mar 2026 | Teo Nee Chuan appointed Group CFO | Leadership Change | [Nasdaq](https://www.nasdaq.com/articles/shangri-la-asia-appoints-teo-nee-chuan-cfo) [UNVERIFIED — search summary only, page not fetched] |
| 5 | Oct 2025 | Shangri-La and Traders Hongqiao Airport open (first airport hotels, Traders relaunch) | Market Expansion | [FY2025 results](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0326/2026032600950.pdf) |

- *"No public payment-related RFP found."*
- No payment-infrastructure job postings were found.
- Digital leadership: Daniel Koo, VP Digital (Shangri-La Circle) [UNVERIFIED — search summary only, page not fetched; date unknown]. CTO identity is conflicting across sources: Jiancheng Yang vs Spencer Lam.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 5 Oct–30 Dec 2026 | Island Shangri-La "Mastercard Exclusive" package; similar offers in SG, KL and Bangkok | Card-scheme marketing tie-up, not acquiring | [offer page](https://www.shangri-la.com/hongkong/islandshangrila/offer-detail/rooms-suites/isl-mastercard-exclusive-stay-above-the-city-room-package/) |
| 2 | 2022 | Pace BNPL at Malaysian property POS | On-property instalments, MY only | [Business Today](https://www.businesstoday.com.my/2022/04/07/shangri-la-hotels-and-resorts-teams-up-with-pace-offering-first-ever-bnpl-payments/) [UNVERIFIED — search summary only, page not fetched] |
| 3 | Jun 2019 | WeChat e-services and WeChat Pay at ~50 mainland hotels (Tencent partnership) | China corridor build | [HospitalityNet](https://www.hospitalitynet.org/news/4093545.html) [UNVERIFIED — search summary only, page not fetched] |
| 4 | 30 Jan 2018 | Ingenico extends global partnership; in-app payments; Oracle Micros PMS/CRS integration | Origin of the `INGENICO_*` gateways | [chinatechnews](https://www.chinatechnews.com/2018/01/30/25637-ingenico-integrates-seamless-payment-capability-in-shangri-las-next-generation-mobile-app) |
| 5 | c. 2016 | Alipay online prepayment rolled out across 95 hotels | Origin of the `ALIPAY_*` gateways | [Marketing-Interactive](https://www.marketing-interactive.com/shangri-la-rolls-out-alipays-online-payment-service-globally) |

- No provider removals were found.
- ICBC, CMBC and CITIC co-brand cards (China) are issuing relationships, not acquiring.

---

### Section 8: Checkout Experience Audit

*Full checkout flow not completed (no live booking made). Findings come from the shipped cashier code and public pages.*

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | First-party hosted cashier at `pay.shangri-la.com` (separate Vue/React bundles `sl-fe-pay-prod`, `sl-fe-h5pay-prod`) | Fair | Custom-built |
| Guest checkout | Not verified | — | Fast check-in deposit prompts login or registration (`checkInDepositLogin`) |
| Steps to complete payment | Not verified | — | |
| Card input experience | **Custom first-party fields**; Base64 JSON with `encryptVersion:"0"` POSTed to the paycenter | Poor (PCI scope) | No PSP iframe or hosted fields |
| Payment methods visible | Cards, Alipay, WeChat Pay (server-driven `payWays`) | Fair | No SEA, JP or IN rails |
| Location-based method display | Methods are server-driven per transaction and property; property lists differ (SG and KL have no Alipay; Pudong has no Apple Pay) | Fair | Varies by property, not by guest country |
| Instalment / EMI options | Not found online | Poor | Only bank-run promos |
| 3DS implementation | 3DS2 browser data collected client-side (`challengeCanvasSize`, screen and colour data) | Good | Server-driven |
| PCI indicator | Self-hosted card fields | — | See Section 9 |
| Mobile responsiveness | Dedicated H5 cashier bundle; 68% of web traffic is mobile | Good | |
| Multi-currency / local pricing | 36 display currencies; charge currency not verified | — | |
| Saved payment methods | Yes (`saveCardWithGc`, `cardList`) | Good | Shangri-La-held tokens |
| Error message clarity | Localised `payFailedMsg` / `transactionDeclined` strings | Fair | |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found | — |
| Card data handling | **Full PCI scope likely.** Card number, expiry and CVV are collected in first-party fields and sent to Shangri-La's own API; saved cards are held by Shangri-La. `[INFERENCE, not confirmed]` | payment bundle |
| Recommended Yuno integration | **Back-to-back API** under the existing paycenter, which keeps their cashier and UX. The SDK is an option only if they want to shed PCI scope. | — |

- No direct PCI compliance documentation was found publicly for Shangri-La.
- The privacy policy mentions "third-party payment processors, payment service providers, external banks, credit card companies" but names none ([policies page](https://www.shangri-la.com/en/corporate/policies-pledges/)).

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: A cashier built for one corridor**
>
> **Evidence:**
> - S1: PH #1 at 13.78%; MY, SG and TH together 14.3%.
> - S3B/S4: the paycenter's only non-card connectors are Alipay ×3 and WeChat Pay; there are 0 occurrences of GCash, FPX, PayNow or PromptPay.
>
> **Pain Point:** the payment layer they built cannot serve the dominant wallet in their biggest web market. Every added rail is a new in-house connector.
>
> **Yuno Value Proposition:** one integration under the paycenter exposes the SEA wallets through the same `payWays` model they already use.
>
> **Best Success Case:** none verified. Pick an in-house-cashier merchant that added local rails.
>
> **Outreach Angle:** "Your paycenter already routes WeChat Pay to one gateway and Alipay to two others. The Philippines is your largest web market and it has no rail in there."
>
> **Suggested Subject Line:** "13.78% of shangri-la.com, zero GCash"

> **Insight #2: Apple Pay is on the property pages, but not in the cashier**
>
> **Evidence:**
> - S4: `APPLEPAY` is in the `paymentModeList` for 7 of 8 properties checked.
> - S3/S8: Apple Pay has 0 occurrences in the cashier bundles.
> - S1: 68% of web traffic is mobile; the US (#2) and AU (#3) are Apple Pay-heavy card markets [prominence not sourced this run].
>
> **Pain Point:** an advertised method that is not offered on the mobile web payment step.
>
> **Yuno Value Proposition:** wallets delivered through one connector, alongside network tokens.
>
> **Outreach Angle:** a low-friction, verifiable observation that opens a conversation with the digital team.
>
> **Suggested Subject Line:** "Apple Pay on the hotel page, not at pay.shangri-la.com"

> **Insight #3: The card leg, raw PAN in-house, and an unknown acquirer**
>
> **Evidence:**
> - S3A/S9: card data is POSTed to their own API with `encryptVersion:"0"`; the card gateway is not exposed.
> - S1/S2: the US (#2, 11.46%) has no entity, so US cards on Asian stays are cross-border.
>
> **Pain Point:**
> - Full PCI scope.
> - Card routing is whatever one or a few gateways do; issuer-geography approval optimisation is unclear.
>
> **Yuno Value Proposition:** tokenisation and vault; local-acquirer routing per property country; failover.
>
> **Outreach Angle:** for the call, not the email: "Who acquires a US card on a prepaid Makati booking, and in which country?"
>
> **Suggested Subject Line:** "Where a US card lands on a Manila prepay"

> **Insight #4: Legacy connectors from 2016–2019 still in production**
>
> **Evidence:**
> - S3A/S7: `INGENICO_*` gateways trace to the 2015/2018 Ingenico deal; the Ingenico online business is now Worldline [background, not sourced].
> - S11: peers (Radisson) have moved to orchestration platforms.
>
> **Pain Point:** maintaining bespoke connectors to an acquired, rebranded provider.
>
> **Yuno Value Proposition:** connector maintenance moves off their roadmap.
>
> **Outreach Angle:** use only after the Worldline question is confirmed. Do not assert it.
>
> **Suggested Subject Line:** "The Ingenico gateways in your paycenter"

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks:**
1. "shangri-la.com's own cashier routes WeChat Pay through Adyen and Alipay through two other connectors. The Philippines, your largest web market at 13.78%, has no wallet in there at all."
2. "Seven of the eight property pages I checked list Apple Pay as an online method; the code behind pay.shangri-la.com has no Apple Pay in it."
3. "You've already built the orchestration layer most hotel groups are still buying. The question is how many more connectors your team wants to build into it."

**Cold call openers:**
1. "Quick one: when a Manila guest prepays on shangri-la.com, which methods does your paycenter actually show them?"
2. "I noticed your cashier picks a gateway per payment method. Who owns adding a new one, and how long does it take?"
3. "Is the Apple Pay logo on the property pages meant for the front desk, or for the online cashier?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| Mandarin Oriental | mandarinoriental.com | HK | 48 properties | HK, CN, JP, SEA | VGS vault (in-house); Datatrans/Planet built but off; Stripe (gift cards) | `2-ready-to-outreach/mandarin-oriental-hotel-group.md` |
| The Peninsula (HSH) | peninsula.com | HK | ~US$1.4B | HK, CN, JP, PH, TH | Card capture inside SynXis; RECON (CN); Stripe (gifts) | `2-ready-to-outreach/the-peninsula-hotels.md` |
| Langham | langhamhotels.com | HK | 33 properties | HK, CN, AU | Cybersource (AU/NZ), Adyen (Gold Coast); 28 of 33 properties have no online gateway | `2-ready-to-outreach/langham-hospitality-group.md` |
| Rosewood | rosewoodhotels.com | HK | ~US$1B est. | HK, CN, SEA | Stripe (shop), Shopify HK; rooms PSP not established | `2-ready-to-outreach/rosewood-hotel-group.md` |
| Minor Hotels | minorhotels.com | TH | 540+ hotels, 55 countries | SEA, Oceania | **2C2P** gateway plus APMs at 40+ properties (Minor is a PSP-side reference; TAL says Do Not Contact) | [2C2P case study (fetched)](https://2c2p.com/case-studies/minor-hotels/) |
| Marriott | marriott.com | US | 7,000+ properties | Pan-APAC | FreedomPay global gateway (2019) | [FreedomPay PR](https://corporate.freedompay.com/press-release/freedompay-announces-an-agreement-with-marriott-international-for-commerce-technology-innovation/) [UNVERIFIED — search summary only, page not fetched] |
| IHG | ihg.com | UK | ~4,000 hotels in scope | Pan-APAC | FreedomPay (US/CA, 2023); Alipay (2016) | [FreedomPay PR](https://corporate.freedompay.com/about-us/press-release/ihg-hotels-resorts-taps-freedompay-to-transform-commerce-technology) [UNVERIFIED — search summary only, page not fetched] |

#### 11B. Industry Peers

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Agoda | agoda.com | OTA | Pan-APAC | Competes for the same room nights; Juspay plus Checkout.com | [hyperswitch case](https://hyperswitch.io/case-studies/agoda/) [UNVERIFIED — search summary only, page not fetched] |
| Trip.com | trip.com | OTA | CN, pan-APAC | Worldline; TAL says "In-house Routing" | [Worldline](https://worldline.com/en/home/main-navigation/resources/all-customer-stories/trip-com-customer-story) [UNVERIFIED — search summary only, page not fetched] |
| Klook | klook.com | Travel experiences | HK, SG, PH, ID, MY | Adyen APAC | [Adyen PR](https://www.adyen.com/press-and-media/klook-partners-with-adyen-to-offer-seamless-payment-solutions) [UNVERIFIED — search summary only, page not fetched] |
| Frasers Hospitality | frasershospitality.com | Serviced residences | SG, MY, AU | Adyen with Alipay, WeChat Pay, GrabPay | [CFOtech](https://cfotech.asia/story/adyen-to-streamline-global-payments-for-frasers-hospitality) [UNVERIFIED — search summary only, page not fetched] |
| Dusit International | dusit.com | Hotels | TH, CN | WeChat Pay via Ksher (2017), Alipay | [Dusit newsroom](https://www.dusit-international.com/en/newsroom/news-releases/457/dusit-hotels-and-resorts-becomes-first-hotel-group-in-thailand-to-accept-wechat-pay) [UNVERIFIED — search summary only, page not fetched] |
| IHCL (Taj) | tajhotels.com | Hotels | IN | TAL: Juspay | `accounts/apac-tal.csv` |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| Radisson Hotel Group | CellPoint Digital | Case study 2 Sep 2025 | Hotels (100+ countries) | [CellPoint (fetched)](https://cellpointdigital.com/articles/casestudies/payment-orchestration-as-a-growth-catalyst-the-radisson-hotel-group-case-study) |
| Sabre SynXis Pay (CRS used by Langham, Peninsula, Rosewood) | CellPoint Digital (embedded) | Mar 2025 | Hotel CRS | [Travolution](https://www.travolution.com/news/travel-sectors/accommodation/sabre-hospitality-introduces-synxis-pay/), cited in the Langham file |
| Agoda | Juspay | Not dated | OTA | [UNVERIFIED — search summary only, page not fetched] |
| KKday, tiket.com, Wego | Juspay | — | OTA | repo files |

#### 11D. Prospect Scoring

Peers are already scored in their own files: Mandarin Oriental 17 (overridden to 🟢), Peninsula 14 🟢, Langham 14 (overridden to 🔴), Rosewood 16 🟢. **Not rescored here**; see those files.

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Shangri-La | Target | PH, US, AU, HK | 21 | ⭐ | In-house cashier with no SEA rails | ✅ (industry mis-tagged) |
| 2 | Mandarin Oriental | Competitor | JP, HK, US | 17→🟢 | 🟢 | VGS in-house vault | ✅ |
| 3 | Rosewood | Competitor | HK, CN | 16 | 🟢 | First-party payment API | ✅ |
| 4 | The Peninsula | Competitor | JP, HK | 14 | 🟢 | SynXis-embedded | ✅ |
| 5 | Langham | Competitor | AU, HK | 14→🔴 | 🔴 | 28 of 33 properties without an online gateway | ✅ |
| 6 | Frasers Hospitality | Peer | SG, MY, AU | Not scored | — | Adyen single-PSP | ❌ **Not in TAL as a hotel row. Genuine find.** |
| 7 | Dusit International | Peer | TH | Not scored | — | WeChat/Alipay, no gateway found | ✅ |
| 8 | Banyan Group | Peer | SEA, CN | Not scored | — | SynXis engine (per the Mandarin file) | ✅ |
| 9 | The Ascott | Peer | SEA | Not scored | — | Blank stack; mis-tagged OTA in TAL | ✅ |
| 10 | Agoda | Peer | Pan-APAC | Not scored | — | Juspay displacement | ❌ **Not in TAL** |

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | **US$2,234.1M** (FY25); US$2,185.4M (FY24); H1 26 US$1,124.0M | HKEX FY25 and H1 26 PDFs |
| GMV / Gross Transaction Volume | Hotel Properties revenue US$1,974.1M; rooms US$1,107.5M; F&B US$766.7M | FY25 PDF |
| Average Transaction Value (USD) | ADR US$172 (owned hotels); per-booking value not found | FY25 PDF |
| Est. Annual Transactions | ~6.4M room nights/year (rooms revenue ÷ ADR); stays not computed (no ALOS) | Calculated |
| **Monthly transaction count** | ✅ **DERIVED: ~537,000 room nights/month** = US$1,107.5M ÷ US$172 ÷ 12 (both audited inputs). Stays/month = ⚠️ **ASSUMED ≥100k** for any average stay of 5.3 nights or less `[ASSUMPTION — not researched]`. **Billing unit:** folio or stay. The share settled through `pay.shangri-la.com` is **not found**. | FY25 PDF |
| Active Customers / Users | Shangri-La Circle membership not found | — |
| Primary Currency | USD reporting; charges in property-local currency [not verified] | — |
| Top 3 Markets by Revenue | Mainland China US$627.9M · Hong Kong US$338.1M · Singapore US$255.6M (FY25 Hotel Properties) | FY25 PDF |
| Billing channel split (web vs app store) | N/A. A hotel, not an IAP business. Web vs app vs Mini Program vs property split not found. | — |

---

### Overall Research Confidence

**Medium-High.**
- **Strong:**
  - the payment architecture, from first-party source code fetched directly (central paycenter, gateway codes, Adyen live SDK, card handling, method set)
  - financials and portfolio, from HKEX primary filings
  - traffic, **supplied by SimilarWeb** (share only; no app traffic)
- **Weak:**
  - the card gateway/acquirer, which is server-side and not identifiable
  - the share of revenue settled online vs at the folio
  - local entity names outside TH and MY
  - all complaints and most news, which rest on search summaries and older items (2016–2022)
- WebFetch and curl both worked in this environment, so there was no confidence downgrade for egress.

---

### Manual Research Recommendations

> **Area:** Settled online volume (S12)
> **Why it matters:** this decides the deal size. A guarantee-only stay settles at the property, not in the paycenter.
> **Suggested manual action:** first discovery question: "What share of room revenue is collected through pay.shangri-la.com at booking vs at the folio?"

> **Area:** Card gateway behind the paycenter (S3A)
> **Why it matters:** the card leg is the biggest volume, and the vendor is unknown.
> **Suggested manual action:** make a prepaid test booking (Makati, Member Online Saver) with DevTools and read `payWays[].name` in the `pay` service response; then check the card descriptor.

> **Area:** Ingenico → Worldline status (S3A, Insight #4)
> **Why it matters:** the legacy-connector angle depends on it.
> **Suggested manual action:** ask in discovery; do not assert it in email.

> **Area:** Apple Pay on property pages (S4)
> **Why it matters:** Hook #2 is only safe if Apple Pay is truly absent from the online cashier, not just loaded through a script I did not fetch.
> **Suggested manual action:** check out on an iPhone (Safari) at the payment step.

> **Area:** Shangri-La Boutique e-shop (boutique.shangri-la.com)
> **Why it matters:** a separate checkout (mooncakes, gifts) that may already carry local methods.
> **Suggested manual action:** add an item to the cart and record the platform and payment methods.

> **Area:** TAL hygiene
> **Why it matters:** the row's industry tag is "OTA", which is wrong.
> **Suggested manual action:** retag it as Hospitality & Lodging; fill Payment Gateway = "Adyen, Ingenico, Alipay (in-house paycenter)" and Payment Orchestrator = "In-house".

---

### Appendix: All Source URLs

**Section 1:** `accounts/traffic/shangri-la.md` (SimilarWeb, supplied 2026-10-19)

**Section 2:**
- https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0326/2026032600950.pdf
- https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0827/2026082700608.pdf
- https://www.shangri-la.com/en/tokyo/shangrila/privacy-policy
- https://philippinen.ahk.de/en/membership/members-directory/makati-shangri-la-hotel-and-resort-inc
- https://www.zawya.com/company/4295886104/shang-properties

**Section 3 (source code, fetched 2026-10-19):**
- https://www.shangri-la.com/en/
- https://www.shangri-la.com/fe-static/sl-fe-revamp-prod/_next/static/chunks/pages/_app-4e270247175910fb.js
- https://www.shangri-la.com/fe-static/sl-fe-revamp-prod/_next/static/chunks/pages/reservation/fast-check-deposit-b2929dbfc171f586.js
- https://www.shangri-la.com/fe-static/sl-fe-revamp-prod/_next/static/chunks/pages/mobile-order/guest-information-f4f15d92466f1148.js
- https://pay.shangri-la.com/en/pay/?transactionId=1&hotelCode=SLM
- https://pay.shangri-la.com/en/pay-common/?transactionId=1&successRedirect=x
- https://s.shangri-la.com/sl-fe-pay-prod/js/payment.a4b2676032c4bd7beb66.js
- https://s.shangri-la.com/sl-fe-h5pay-prod/js/index.476aa032b1.js
- https://www.chinatechnews.com/2018/01/30/25637-ingenico-integrates-seamless-payment-capability-in-shangri-las-next-generation-mobile-app
- https://www.marketing-interactive.com/shangri-la-rolls-out-alipays-online-payment-service-globally
- https://thepaypers.com/company/AsiaPay/50
- https://www.shangri-la.com/en/corporate/policies-pledges/
- https://www.breakingtravelnews.com/focus/article/onyx-payments-renews-shangri-la-international-hotel-management-ltd.-for-glo/

**Section 4:**
- Property `services-facilities` pages (fetched 2026-10-19), all under `https://www.shangri-la.com/en/{city}/{hotel}/about/services-facilities/`:
  - sydney/shangrila, singapore/shangrila, tokyo/shangrila, kualalumpur/shangrila
  - shanghai/pudongshangrila, bangkok/shangrila, manila/edsashangrila, hongkong/kowloonshangrila
  - plus manila/makatishangrila and hongkong/islandshangrila (Agent 3)
- https://www.shangri-la.com/corporate/shangrilacircle/redeem-points/lifestyle/product-categories/egift-cards/philippines/gcashphp2000/
- https://context.ph/2026/09/08/over-24m-gcash-users-verified-with-national-id/
- https://www.businesstoday.com.my/2022/04/07/shangri-la-hotels-and-resorts-teams-up-with-pace-offering-first-ever-bnpl-payments/

**Section 5:**
- https://www.travelweekly-asia.com/Hotels/Shanghai/Shangri-La-Qiantan-Shanghai-p57901479
- https://thefilam.net/archives/10158
- https://www.traveloka.com/en-th/user/review/consumption/HOTEL/GENERAL/1000000455649
- https://nl-be.trustpilot.com/review/www.shangri-la.com

**Section 6–7:**
- https://www.nasdaq.com/articles/shangri-la-asia-appoints-teo-nee-chuan-cfo
- https://www.shangri-la.com/hongkong/islandshangrila/offer-detail/rooms-suites/isl-mastercard-exclusive-stay-above-the-city-room-package/
- https://www.hospitalitynet.org/news/4093545.html

**Section 11:**
- https://2c2p.com/case-studies/minor-hotels/
- https://cellpointdigital.com/articles/casestudies/payment-orchestration-as-a-growth-catalyst-the-radisson-hotel-group-case-study
- https://www.travolution.com/news/travel-sectors/accommodation/sabre-hospitality-introduces-synxis-pay/
- https://corporate.freedompay.com/press-release/freedompay-announces-an-agreement-with-marriott-international-for-commerce-technology-innovation/
- https://corporate.freedompay.com/about-us/press-release/ihg-hotels-resorts-taps-freedompay-to-transform-commerce-technology
- https://hyperswitch.io/case-studies/agoda/
- https://worldline.com/en/home/main-navigation/resources/all-customer-stories/trip-com-customer-story
- https://www.adyen.com/press-and-media/klook-partners-with-adyen-to-offer-seamless-payment-solutions
- https://cfotech.asia/story/adyen-to-streamline-global-payments-for-frasers-hospitality
- https://www.dusit-international.com/en/newsroom/news-releases/457/dusit-hotels-and-resorts-becomes-first-hotel-group-in-thailand-to-accept-wechat-pay

</details>
