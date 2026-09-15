# Bamboo Airways

**Status:** 🔴 Not ICP
**ICP Score:** Not scored — rejected on the analyst override before scoring completed
**Industry:** Airlines · **HQ:** Ho Chi Minh City, Vietnam (registered Quy Nhơn, Bình Định) · **Researched:** 2026-09-15 · **First email sent:** —
**Motion:** N/A

---

## Rejection Rationale

**Bamboo Airways is down to one aircraft and has stopped selling scheduled tickets. There is no transaction volume left to orchestrate.**

I verified the core fact myself rather than taking it from an agent. Dân trí, 2 September 2026, citing Planespotters data updated 1 September, headline and body verbatim:

> *"Bamboo Airways còn 1 máy bay… Từ 22 máy bay năm 2019, Bamboo Airways nay chỉ còn 1 chiếc."*
> — "Bamboo Airways has 1 aircraft left… From 22 aircraft in 2019, Bamboo Airways now has just 1."

> *"Ở chiều ngược lại, Bamboo Airways - hãng từng đạt đỉnh 44 máy bay năm 2022 - đã trải qua những xáo trộn đáng chú ý: từ 8 chiếc hồi đầu năm, hãng thu xẹp lại còn 3 chiếc vào cuối tháng 7, và đến cuối tháng 8 chỉ còn duy nhất 1 chiếc Airbus A321-200 hoạt động."*
> — "Bamboo Airways, which peaked at 44 aircraft in 2022, has been through notable upheaval: from 8 aircraft at the start of this year it shrank to 3 by end-July, and by end-August only a single Airbus A321-200 remains in operation."

— [dantri.com.vn](https://dantri.com.vn/kinh-doanh/bamboo-airways-con-1-may-bay-buc-tranh-quy-mo-hang-khong-viet-dang-ra-sao-20260902123651502.htm) (fetched 2026-09-15)

For scale, from the same article: **Vietjet 107 aircraft, Vietnam Airlines 97**, and new entrant **Sun PhuQuoc Airways 16** — a carrier that started flying in October 2025. Bamboo is now smaller than an airline eleven months old.

### The fleet timeline

| Date | Operating aircraft |
|---|---|
| 2019 | 22 |
| 2022 (peak) | **44** |
| Start of 2026 | 8 |
| End July 2026 | 3 |
| **End August 2026** | **1 × Airbus A321-200** |

### Everything else points the same way

- **Scheduled ticket sales suspended from 1 August 2026**; last scheduled flights reported 22 August 2026. `[UNVERIFIED — search summary only, but consistent across Aerotime, Aviation Week, AirData News and Aviation News EU]`
- **Zero international scheduled routes.** Every international point on the Wikipedia destination table is marked Terminated: Melbourne, Sydney, Frankfurt, Tokyo Narita, Fukushima, Singapore, Seoul Incheon, Taipei, Kaohsiung, Bangkok, London. Only Sanya, Tianjin, Macau, Tainan and Ibaraki remain as charter.
- **The airline's own flight-network page describes domestic Vietnam routes only** — no international routes at all, and the footer nav offers only "Domestic Journeys / Domestic Flights / Domestic Destinations". — [our-flight-network](https://www.bambooairways.com/vn/en/travel-info/airports-and-network/our-flight-network) (fetched by me)
- **Negative equity** of VND 836bn at end-2022, cumulative losses over VND 17,600bn, cash on hand VND 85bn (~US$3.5m) mid-2023 — [Dân trí](https://dantri.com.vn/kinh-doanh/bamboo-airways-bao-lo-hon-17600-ty-dong-am-von-tien-mat-con-85-ty-dong-20230614161557189.htm)
- **Tax arrears of VND 431.6bn** (30 Apr 2026), and an **exit ban sought against the beneficial owner** over the debt — [doanhnghiephoinhap.vn](https://doanhnghiephoinhap.vn/bamboo-airways-no-thue-hon-440-ty-dong-giua-giai-doan-tai-co-cau-144899.html) · [thoibaotaichinhvietnam.vn](https://thoibaotaichinhvietnam.vn/se-tam-hoan-xuat-canh-doi-voi-chu-so-huu-huong-loi-cua-bamboo-airways-vi-no-thue-201569.html)
- **~VND 9,000bn of debt unresolved after restructuring** — [cafeland.vn](https://cafeland.vn/tin-tuc/khoan-no-9000-ty-dong-cua-bamboo-airways-van-giam-chan-tai-cho-sau-tai-co-cau-146682.html)
- **Regulator involved on refunds.** The National Competition Committee (Ministry of Industry and Trade) worked with the airline in August 2026 over consumer refund complaints on cancelled flights; the airline admitted a spike in refund requests and **has not announced a completion deadline** — [Dân trí](https://dantri.com.vn/kinh-doanh/bamboo-airways-bi-khach-phan-anh-hoan-tien-ve-co-quan-chuc-nang-vao-cuoc-20260820141747637.htm) · [Tuổi Trẻ](https://tuoitre.vn/bamboo-airways-bi-khach-phan-anh-cham-hoan-tien-ve-10026082108245973.htm)
- **Web traffic is tiny and single-market.** Roughly 100K–240K monthly visits depending on source, ~76–99% Vietnam. Two third-party estimates disagree by 2.4x and neither could be loaded properly, so no country split was established and none was invented.

**A restart was announced** for mid-Q3 2026, but the airline had not specified routes, frequencies, aircraft or when ticket sales reopen — [CafeF](https://cafef.vn/bamboo-airways-chuan-bi-cat-canh-tro-lai-18826081209582718.chn). The last hard datapoint, 1–2 September, was still one aircraft. **No source confirms a restart happened.**

### Why this is a rejection and not a low score

The 24-point matrix would have scored this account reasonably well: no orchestrator detected (+4 greenfield), 12 storefronts, multiple payment partners, a documented rail gap outside Vietnam. **That is exactly the false positive the "absolute volume too small" override exists to catch.** A one-aircraft carrier with suspended ticket sales, negative equity and a regulator in the room has no payments budget, no approval-rate problem worth solving, and no PSP diversification project.

The multi-currency storefronts that make the account look interesting are **fossils of the 2022-era network**. They map one-for-one onto routes that are now terminated.

*Marked: 2026-09-15*

---

## 🔄 Revisit trigger

This is worth a second look, but not soon. Re-run `/research` **if** FLC restarts scheduled flying **and** the fleet rebuilds past roughly 10 aircraft **and** international routes return. Realistically 2027 or later. The payment research below stays valid as a starting point — the method map and the card-verification control are unlikely to change shape.

---

## ⚠️ Corrections needed in `accounts/apac-tal.csv`

Not edited — the TAL is your system of record. Both are wrong on the current row:

| Column | Current value | Should be |
|---|---|---|
| `Est. Revenue (USD)` | **$0.5B** | **Stale by three years.** That is the FY2023 figure (VND 12,393bn), from a year when the airline still ran ~20 aircraft including widebodies. It has no bearing on 2026. No FY2024 or FY2025 figures exist publicly — the airline is unlisted. |
| `INFO` / `Operating Countries` | "flying mainly domestic routes after heavy restructuring and fleet cuts" · "Vietnam (restructuring)" | Understates it. As of end-August 2026: **one aircraft, scheduled ticket sales suspended, zero international scheduled routes.** |

---

<details>
<summary><h2>📚 Payment research completed before the rejection (kept so nobody researches this twice)</h2></summary>

The payment picture was fully resolved before the volume override fired. Recording it because the revisit trigger above may eventually bring this account back, and because the method map is unusually clean.

### The accepted-methods map — enumerated first-party, so absences are sourced

From [the airline's own payment-options page](https://www.bambooairways.com/vn/en/book/booking-information/payment-options), fetched and read in both English and Vietnamese:

| Storefront | Methods |
|---|---|
| 🇻🇳 **Vietnam (VND)** | International cards (Visa/MC/JCB) · **NAPAS domestic ATM cards** from 40+ banks · **VietQR** (~40 banks + 5 e-wallets) · **MoMo** · voucher. **Pay Later:** banking apps, ATMs at Vietcombank and BIDV, counters at Vietcombank/SCB/Techcombank, **ViettelPay**, and **cash at convenience stores via Payoo** (WinMart, Circle K, Thế Giới Di Động) |
| 🇨🇳 **China (CNY)** | International cards **+ UnionPay** · **Alipay** |
| 🇸🇬 **Singapore (SGD)** | International cards · **Alipay** |
| **The other 9** — USD, THB, TWD, JPY, KRW, GBP, EUR (DE), EUR (FR), AUD | **International cards only** |

**Twelve storefronts, eleven currencies, and nine of them accept exactly one method while Vietnam accepts ten.** Under different circumstances that asymmetry — entirely internal to their own stack — would have been the opener. It dies on the fact that the nine cards-only storefronts have no live routes behind them.

**Sourced absences** (zero hits across both language versions of an enumerated list): **ZaloPay · ShopeePay · instalments (trả góp) · WeChat Pay · PayPal · Apple Pay · Google Pay.** Note WeChat Pay being absent while Alipay is present — one-wallet-deep in China, the same pattern found on Air New Zealand's China page.

### 🚩 Provider removal: ZaloPay

ZaloPay was announced as Bamboo's **"official payment partner"** in an agreement signed 22 August 2019 — [ZaloPay press release](https://zalopay.com/zalopay-tro-thanh-doi-tac-thanh-toan-chinh-thuc-cua-bamboo-airways.html). It appears **nowhere** on the 2026 enumerated payment-options page, in either language. ZaloPay is one of Vietnam's two dominant wallets. A named official partner dropping off the method list is a removal, and it would have been a strong opening question.

### Payment partners confirmed by press release

| Provider | Role | Evidence |
|---|---|---|
| **MoMo** | Wallet, live at checkout with documented limits (30m VND/day wallet-funded; **only 5m VND/day when funded by a linked Visa/MC/JCB card**, low enough to block a single international ticket). Also a distribution channel — Bamboo is bookable inside the MoMo app | Airline's own pages |
| **VNPAY** | VNPAY-QR as a payment method on web and app | Vendor + airline offer pages |
| **ViettelPay** | Wallet and bill-collection rail | Airline press release |
| **Payoo** | Convenience-store cash collection for Pay Later | Vendor press release |
| **NAPAS** | Domestic card scheme/switch — a **scheme, not a PSP** | Airline payment page |

Each was announced separately, with its own press release. That pattern — a pile of individually negotiated bilateral integrations — is the signature of direct one-by-one PSP integration rather than a routing layer.

### Orchestration status: none detected

No Juspay, Spreedly, Primer, Gr4vy, APEXX, Payrails, CellPoint, IXOPAY or Yuno reference anywhere. **Bamboo does not appear on CellPoint Digital's published airline roster.** Greenfield on paper.

### Booking stack

**Amadeus.** Raw-HTML grep of the booking pages returned `AMADEUS_CUSTOM_PARAMS`, `AMADEUS_CFF_2/3/4`, `AMADEUS_ADULT_CODE`, `value="amadeus"`, and form actions posting to `https://bbc.bambooairways.com/plnext/BambooDX/Override.action` — `/plnext/` is the Amadeus PLNext signature. Corroborated by an [Amadeus press release](https://amadeus.com/en/newsroom/press-releases/bamboo-airways-gears-up-for-global-expansion-with-selection-of-a) announcing Altéa PSS.

⚠️ **Amadeus Altéa PSS is not Amadeus payment acquiring.** No link to Outpayce or the Xchange Payment Platform was found. Do not conflate the two.

**The card acquirer was never identified.** The checkout at `digital.bambooairways.com/book` sits behind an Imperva bot wall (HTTP 200, 6KB, `<title>Pardon Our Interruption</title>`), so no `vpc_` (OnePay) or `vnp_` (VNPAY) parameter could be read. Certificate Transparency surfaced `token.` and `frame.` subdomains that look payment-adjacent; both fail TLS from here.

### 🎯 The most interesting payment finding, and it survives the rejection

**Bamboo runs a manual anti-fraud control on international cards.** Verbatim from their own payment page, and it appears on the **Vietnam and China storefronts both**:

> *"Bamboo Airways may randomly request verification of the payment card used for ticket purchases… Card verification can be performed via email, at Bamboo Airways' official ticket offices, or at designated Bamboo Airways check-in counters at select airports. The cardholder should provide… The cardholder's identification card or passport. **The traveler's identification card or passport (in the case of purchasing tickets on behalf of someone else). Authorization letter for card verification.** Electronic ticket. Documentation confirming the successful payment transaction from the card-issuing bank."*

A card-not-present fraud check discharged by document review at an airport counter. The heaviest burden — three documents — falls on **third-party purchases**, and the airline has built a dedicated "Book a flight for My Family Members/Nominee" booking mode that actively invites exactly that flow. For a foreign cardholder with no Vietnamese ticket office nearby, the only listed route is an email address.

Two further claims were surfaced but **not verified**, and both would be significant if true: that failing verification requires buying **new tickets for all sectors**, and that the authorization letter may need notarising at a commune/ward People's Committee. Either would need a fetch of the online-booking conditions page to confirm.

### Two traps caught

- **"PayGet" is not a payment platform.** A page titled "first launch PayGet platform, pay easily by Visa" looked like a payments product. It is **"Pay & Get"**, a Bamboo Club loyalty feature for earning points on card spend. Reportedly offline for upgrade.
- **OnePay is not confirmed as their gateway.** A search summary asserted Bamboo pays "through the OnePay gateway". The only supporting source was **bambooair.vn — a third-party agency reseller site, not the airline.** An agency's own OnePay checkout says nothing about the carrier's stack. Same publisher-versus-subject trap as the ZEE5/Juspay and App-Store-"Rytr" false positives. **Do not repeat the OnePay claim.**

### One judgement call worth recording

**The refund story is the loudest thing in this account and it is the wrong thing to pitch.** It is a solvency backlog — fleet contraction, mass cancellations, refund surge — with a regulator already engaged. Nothing in the reporting points at a payment rail. Offering to speed up refunds to an airline that cannot fund them would read as naive at best. The legitimate payments-adjacent angle, had the account been workable, is **chargeback exposure building behind an unbounded refund queue with no published completion date**.

### Legal entity

**CÔNG TY CỔ PHẦN HÀNG KHÔNG TRE VIỆT** (Viet Bamboo Aviation JSC), tax code **0107867370**, registered Nhơn Lý, Quy Nhơn, Bình Định; head office moved to Ho Chi Minh City March 2024. Branches `-001` (Hanoi) and `-003` (HCMC). AOC #366. IATA/ICAO **QH / BAV**.
⚠️ Sourced from masothue and thuvienphapluat, which are mirrors of the National Business Registration Portal, not the portal itself. **No foreign legal entity found anywhere.** Airline-office directory sites listing Singapore/Japan/Korea "offices" are spam with fabricated phone numbers and were discarded.

### Ownership

FLC Group (founder Trịnh Văn Quyết, arrested March 2022) → Him Lam Group and associated investors from June 2023 → **back to FLC Group**, EGM September 2025, re-acquisition completed December 2025. CEO turnover has been extreme, five or more since 2022, and current sources conflict. **Do not name a CEO.**

</details>

<details>
<summary><h2>🔍 Appendix — Vietnamese & SEA airline payment stacks (the most valuable output of this run)</h2></summary>

*Added 2026-09-15. Competitor research finished after the rejection. **This matters far more than the Bamboo account did:** four of the carriers below are P1 accounts already sitting in the TAL, and this research changes the motion for every one of them.* Evidence is raw-HTML and i18n-bundle grep on first-party pages, or a vendor press release, unless labelled otherwise.

### 🇻🇳 Vietnam Airlines — P1 in the TAL — **already on Adyen global acquiring**

From [Adyen's own newsroom](https://www.adyen.com/press-and-media/vietnam-airlines-expands-partnership-with-adyen), 29 April 2025, verbatim:

> *"The airline partnered with Adyen in 2017 for its gateway solution and in 2024, expanded the partnership to leverage Adyen's global acquiring capabilities, enabling seamless payment experiences in markets like Japan, Australia, the U.S., and Europe… **Since the expansion of partnership, Vietnam Airlines has seen up to a 5% uplift in authorization rates.**"*

**Read this before anyone pitches them.** They are consolidated on a single global acquirer and are publicly quoting an auth-rate uplift from it. An orchestration pitch has to beat that story, not introduce the concept. Their local-method coverage is also deep and per-market, quoted from their own site: **KCP + KakaoPay** (Korea) · **Konbini** at 7-Eleven, Lawson, Ministop, FamilyMart and Seicomart, under JPY 300,000 (Japan) · **Rabbit LINE Pay via Alipay+** (Thailand) · **GrabPay** (Singapore) · **GCash via Alipay+** (Philippines) · **Touch 'n Go via Alipay+** (Malaysia) · **DOKU** (Indonesia) · **Sofort + iDEAL** (Europe) · **Afterpay + Zip** (Australia) · **MoMo + ShopeePay + VNPAY QR** (Vietnam) · card instalments above VND 3,000,000.

Note the structure: they reach Touch'n Go, GCash and Rabbit LINE Pay through **one Alipay+ connection** rather than three integrations. They have already solved multi-market wallet coverage with an aggregator.

### 🇻🇳 VietJet Air — P1 in the TAL — **owns a licensed payment company**

**Do not pitch orchestration to VietJet as a concept.** They run **MPGS (Mastercard Payment Gateway Services)** for cards and **GalaxyPay — wholly owned by VietJet**, established 2020 with VND 50bn charter capital, **licensed by the State Bank of Vietnam** for payment gateway, collection/disbursement and e-wallet. Rebranded to **SkyPay** from 1 January 2026; added Google Pay April 2026. Plus **2C2P** for Thai banks and Intelisys for the international card group.

Per-market rails from their i18n bundle, grepped verbatim:
```
"VJPALI":"ALIPAY"   "VJPAZID":"AzuPay"    "VJPDOKU":"DOKU"     "VJPMOMO":"MOMO"
"VJPNAPA":"NAPAS"   "VJPSKY":"SKYPAY"     "VJPSMAR":"SmartroPAY"
"VJPVEQR":"VIETQR"  "VJPZALO":"ZAlO"      "VJVNPAY":"VNPAY"    "VJVNQR":"VNPAY QR"
```
**`VJPAZID` = AzuPay**, the Australian **PayID / NPP real-time** provider — a competitor running bank-rail payments on its Australian storefront, surcharge-free. **`VJPSMAR` = SmartroPAY**, a Korean card PG under KT Group. Also **Movi** BNPL and **HDSaison** instalments, *"up to 6 months and no need to prove income."*

**VietJet charges a payment surcharge:** *"55,000 VND/passenger who books domestic flights. 50,000 VND/passenger who books international flights,"* with the AzuPay/AUD option explicitly flagged as the surcharge-free exception. That is a cost-of-acceptance story a competitor is passing to passengers.

### Orchestration in SEA aviation — rosters checked at source, not from SEO pages

| Vendor | Airline roster, extracted from their own site | SEA/APAC relevance |
|---|---|---|
| **CellPoint Digital** | Cebu Pacific, Emirates, Riyadh Air, Oman Air, Avianca, Gol, Arajet, Air Europa, Icelandair, Southwest, Virgin Atlantic, La Compagnie, KM Malta, Beond, Sunrise | **Cebu Pacific is the one SEA carrier**, and it has a named case study, not just a logo. **P1 in the TAL** |
| **Juspay** | Air India, IndiGo, **Singapore Airlines**, SpiceJet, Agoda, Etraveli, KKday, Wego, Accor Plus, Minor | **Singapore Airlines is on Juspay's own airline page. P1 in the TAL.** IndiGo corroborated by its own [press release](https://www.goindigo.in/press-releases/juspay-to-power-payments-for-indias-leading-airline-indigo.html) |

**No Vietnamese carrier uses an orchestrator.** Nothing for Primer, Gr4vy, Spreedly, APEXX or Corefy in the region beyond vendor marketing.

### ⚠️ Motion corrections for four P1 accounts already in the queue

These change the opening for each account and should be applied before any `/research` or `/full-outreach` run on them:

| Account | Likely motion | Why |
|---|---|---|
| **Singapore Airlines** | **Displacement**, not greenfield | On Juspay's own airline page. Also appears in Adyen's merchant list, so probably multi-provider. Never open with "you have no orchestration layer" |
| **Cebu Pacific** | **Competitive** | CellPoint Digital incumbent with a published case study. Per the skill's own rule, only proceed if research surfaces a concrete gap |
| **VietJet Air** | **In-house**, and an unusually strong version of it | They own an SBV-licensed payment institution. Anchor on reach and opportunity cost, never on the build being wrong |
| **Vietnam Airlines** | Consolidated single-acquirer, **not** greenfield | Adyen global acquiring since 2024 with a public 5% auth-uplift claim |

### TAL hygiene notes

- **Jetstar Asia (Singapore) ceased operations 31 July 2025** — [Qantas newsroom](https://www.qantasnewsroom.com.au/media-releases/qantas-group-to-close-its-intra-asia-airline-jetstar-asia). ✅ The TAL row is **Jetstar Airways (jetstar.com, part of Qantas)**, the Australian carrier, which is unaffected. Recorded only so the two are not conflated later.
- **Sun PhuQuoc Airways** — Vietnamese new entrant, commercial launch October 2025, already **16 aircraft** and the third-largest fleet in Vietnam. **Not on the TAL.** Growing fast in a market where no carrier uses orchestration; worth considering as a prospect.

### What this run could NOT confirm

- **PromptPay on any Thai airline storefront.** Vietnam Airlines uses Rabbit LINE Pay for Thailand; VietJet routes Thai banks through 2C2P. The Thai gap is real but it is a wallet gap, not a QR-rail gap. **Do not claim a PromptPay gap without checking the specific carrier.**
- **Taiwan (TWD) local methods** — no JKOPay, LINE Pay TW or ATM transfer on either carrier. Possibly a genuine region-wide gap worth a dedicated look.
- **Japan PayPay** — Vietnam Airlines has Konbini but no PayPay; VietJet has neither.
- Pacific Airlines, VASCO, Vietravel Airlines, Scoot and AirAsia payment stacks — not researched.
- Fleet counts and market shares quoted above are `[UNVERIFIED — search summary only]`.

</details>
