# Delivery Hero

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 17 / 29 → ⭐ High Priority **on arithmetic** — **ANALYST OVERRIDE applied, tier set DOWN to 🔴 Low for cold SDR outreach.** See the ICP breakdown for the reasoning.
**Industry:** Food & grocery delivery / quick commerce marketplace (Baemin in Korea; foodpanda in South & Southeast Asia, HK and Taiwan) · **HQ:** Berlin, Germany — **Delivery Hero SE** · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **In-house** — a group payments platform built and run from Berlin across multiple PSPs (Adyen, Cybersource, Checkout.com, PayPal and others). Baemin appears to run its own separate Korean wallet stack (Baemin Pay).
**⛔ READ BEFORE ANY OUTREACH:** **Uber has agreed to acquire Delivery Hero** (all-cash, €41.50/share, ~€13bn equity, announced 16 Jul 2026, closing expected **H2 2027**). **Uber is on Yuno's own customer list.** After closing, DH's payments platform is set to be integrated with Uber's "over time". This is an **Uber-relationship decision, not a cold sequence**. Clear it with your manager and the Uber account owner before you touch it — see Phase 0 and Insight #1.

---

> # 🔒 PHASE 0 — QUALIFICATION GATE
>
> | Rule | Result |
> |---|---|
> | PSP / gateway / acquirer / orchestrator | **Does not fire.** DH is a marketplace merchant. It runs in-house wallets (pandapay in PK, PH, MY, SG; Baemin Pay in KR) and a PH payment-processing affiliate, **DH Philippines Blue Services, Inc.**, named in foodpanda PH postpaid T&Cs ([foodpanda.ph](https://www.foodpanda.ph/contents/postpaid-terms-and-conditions), search summary only). No e-money or payment-institution licence in a DH entity's name was found. It is a merchant that builds payments, not a PSP. |
> | Existing Yuno customer | **Delivery Hero: no.** `https://y.uno/en`, fetched 2026-10-19, has zero occurrences of "Delivery Hero", "foodpanda", "Baemin", "Woowa", "talabat" or "Glovo". **But "Uber" appears in Yuno's customer copy** ("Today Yuno powers payments for McDonald's, inDrive, Rappi, NetEase, GoFundMe, **Uber** …"), and Uber is DH's agreed acquirer. **Flag, not a rejection.** |
> | No online payment volume | Does not fire. |
> | HQ west of Dubai with no APAC operations | **Does not fire, but there is a territory question.** HQ is Berlin. APAC operations are large: Asia segment GMV was **€20.8bn in FY2025**, ~42% of group GMV. The group payments platform and its decision-makers sit in **Berlin** (EMEA territory). The APAC entry points are **Woowa Brothers (Seoul)** and **foodpanda (Singapore)**. Agree internally who owns the account before outreach. |
> | Monthly transactions < 40,000 (sourced) | **Does not fire.** ✅ SOURCED: group orders were **981m in Q2 2026**, ~327m a month ([DH Q2 2026 Trading Update](https://ir.deliveryhero.com/media/document/7c8c8b86-f69c-4699-a75e-dc2946cb22e0/assets/Delivery_Hero_Q2_2026_Trading_Update.pdf?disposition=inline), p.11). |

> # ⚠️ METHOD NOTES — disclosed up front
>
> 1. **Traffic was supplied.** `accounts/traffic/delivery-hero.md` covers talabat.com, baemin.com and glovoapp.com. `accounts/traffic/foodpanda.md` covers foodpanda .ph, .com.tw, .my, .sg and .pk. Both are Similarweb Sales Intelligence, pulled 2026-10-19, Jul–Sep 2026. Both files' caveats are carried through:
>    - **(a)** Each file shows only the top 10 countries per domain, as shares. Every per-country visit figure below is `[DERIVED from supplied share, not a SimilarWeb figure]`.
>    - **(b)** Shares are single-domain. The combined split was built visits-first (share × that domain's average monthly visits, then summed), never by averaging percentages.
>    - **(c)** **Mobile app traffic is excluded.**
>    - **(d)** **This is an app-first business.** Web traffic is used as a market-mix signal only. It was **NOT** used to size transactions or test the 40k gate; the 40k test uses the reported order count.
>    - **(e)** **Coverage is partial.** deliveryhero.com was not pulled. Brands such as PedidosYa, foodora, efood, HungerStation, Yemeksepeti and Talabat's sister brands were not supplied. foodpanda .hk, .com.bd, .com.kh, .la and Myanmar were not supplied either. The "combined total" below is the sum of **eight supplied domains**, not a group total. APAC's share of it is **not** APAC's share of DH.
> 2. **Web access worked**, with gaps. deliveryhero.com returns 403 to bots. foodpanda country sites bot-walled most fetches. The IR decks (ir.deliveryhero.com), baemin.com, one foodpanda.sg page, y.uno, tech.eu and Malay Mail were read directly.
> 3. **One source-code finding could not be re-checked.** An agent fetch of the foodpanda.sg homepage on 2026-10-19 reported a shared payment-method bundle listing adapters for ~10 PSPs. My re-fetch was bot-walled (403). The Adyen/PayPal configuration **was** re-checked from a saved copy of foodpanda.sg/contents/privacy.htm. The wider adapter list is labelled as not independently re-verified wherever it appears.
> 4. **The footprint is moving.** Thailand has exited (FY25 deck). **Taiwan is being sold to Grab**: Taiwan FTC decision due **27 Oct 2026**, closing expected Q4 2026. The **whole group is under offer from Uber**. Treat Taiwan as leaving the account.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Delivery Hero SE is a Berlin-based food, grocery and quick-commerce delivery group operating in ~65 countries. FY2025 GMV was €49.2bn and revenue €14.1bn; Asia (Baemin and foodpanda) accounts for €20.8bn of GMV. In APAC it runs **Baemin** (Woowa Brothers, South Korea's largest delivery app) and **foodpanda** (Pakistan, Philippines, Malaysia, Singapore, Hong Kong, Bangladesh, Cambodia, Laos, Myanmar, and Taiwan pending its sale to Grab). **Uber agreed in July 2026 to acquire the group**, with closing expected H2 2027.

**SimilarWeb total visits (last 3-month average):** **~26.7M / month** across the 8 supplied domains, of which **~14.7M / month (55%) is APAC** (baemin.com + 5 foodpanda domains). Supplied 2026-10-19. Web only; the apps, where most orders happen, are excluded.

### Top 5 markets (APAC only)
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇰🇷 South Korea (Baemin) | 33.0% of APAC web (~4.86M/mo) | Baemin Pay (Pay Money, linked bank account, Baemin Pay card); **PAYCO incl. mobile meal vouchers** (new Aug 2026); **carrier billing via KG Financial** (May 2026); Apple Pay incl. **foreign-issued cards** (Jun 2026); Naver Pay, Toss Pay (older or unverified); meet-and-pay | **KakaoPay not found** (not confirmed absent) | ✅ Woowa Brothers Corp. (biz reg. 120-87-65763) |
| 2 | 🇵🇰 Pakistan | 19.4% (~2.86M/mo) | Debit/credit cards, JazzCash, Easypaisa, pandapay wallet, COD (all search summary only) | Raast not found | ⚠️ Delivery Hero Pakistan (Private) Limited (T&Cs, search summary only) |
| 3 | 🇹🇼 Taiwan — **being sold to Grab** | 16.3% (~2.40M/mo) | Cards, Apple Pay, LINE Pay, PXPay (全支付); cash ~30% of orders (search summary only) | JKOPay, Taiwan Pay not found | ⚠️ 富胖達股份有限公司 (search summary only) |
| 4 | 🇵🇭 Philippines | 12.1% (~1.78M/mo) | Cards, GCash, Maya, pandapay, COD, **QR Ph on delivery** (May 2026), postpaid (search summary only) | None confirmed missing | ⚠️ Delivery Hero Philippines, Inc. + DH Philippines Blue Services, Inc. (T&Cs, search summary only) |
| 5 | 🇲🇾 Malaysia | 11.7% (~1.73M/mo) | Touch 'n Go eWallet via Alipay+ (2023), cards (Adyen MY acquiring, 2020), COD | FPX, DuitNow, Boost, GrabPay **not found** as named methods | ⚠️ Delivery Hero Malaysia Sdn. Bhd. (fka foodpanda Malaysia), 201201019422 (directory only) |

Singapore is #6 (7.4% of APAC web, ~1.09M/mo). Every APAC market has a local operating entity, so **no regulatory acquiring gate applies**. This is a **domestic-in-each-market** business, not a cross-border one.

### Legal entities
- **Delivery Hero SE** (Germany, group parent)
- **Woowa Brothers Corp. / (주)우아한형제들** (South Korea) — business reg. **120-87-65763**
- **Delivery Hero (Singapore) Pte. Ltd.** (fka foodpanda Singapore Pte. Ltd.) — UEN **201209757Z** (third-party directory)
- **Delivery Hero Malaysia Sdn. Bhd.** (fka Foodpanda Malaysia Sdn. Bhd.) — **201201019422 (989567-W)** (third-party directory)
- **Delivery Hero Philippines, Inc.** and **DH Philippines Blue Services, Inc.** (Philippines) — reg. no. not found
- **Delivery Hero Pakistan (Private) Limited** (Pakistan) — reg. no. not found
- **富胖達股份有限公司** (foodpanda Taiwan) — pending sale to Grab

### Known PSPs
- **Adyen** — [Source Code] — merchant account `"DeliveryHero"`, client-side encryption, **3DS on, recurring on**, in the live foodpanda.sg web config (2026-10-19); Malaysia acquiring launch partner (2020, Adyen press); group risk management (Adyen case study)
- **Cybersource (Visa)** — [Press Release] — tokenized checkout "with local acquiring" in **10+ APAC markets** (Jul 2024), with aims to offload PCI scope and raise authorisation rates
- **Checkout.com** — [Provider Case Study] — group client since 2019; MENA-led; "extending … to APAC and Europe" (2023); network tokenization and cross-border smart routing
- **PayPal** — [Source Code] — production client in the foodpanda.sg config
- **Fiserv** — [Press Release, search summary only] — reportedly named primary acquirer for foodpanda **SG and HK**, Oct 2024
- **Alipay+** (Touch 'n Go MY), **HSBC** (PayMe HK; rider payouts), **KG Financial** (Baemin carrier billing), **NHN PAYCO** (Baemin)

### Orchestration status
**In-house orchestration layer.** A DH Berlin Payments Tribe job ad calls for a PM to "design and deliver **payment orchestration** and platform improvements" via DH's regional platforms. Its nice-to-have is "experience with payment orchestration, routing, or multi-PSP environments" ([DH careers, now expired](https://careers.deliveryhero.com/job/product-manager-payments-fintech-in-berlin-germany-jid-9819)). Checkout.com's case study puts DH's payments team at "over 200 payment professionals in Berlin and about 200 more worldwide" ([Checkout.com](https://www.checkout.com/case-studies/how-localized-payments-is-driving-delivery-hero-s-global-expansion)). **No third-party orchestrator found** (Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails and Yuno were all negative for checkout).

### Buying signals
- 🤝 **Uber takeover** — €41.50/share all-cash offer; boards support it; closing H2 2027. "Business as usual — Delivery Hero and Uber operate independently until closing", with integration onto "one platform over time" after that ([DH Q2 2026 Trading Update](https://ir.deliveryhero.com/media/document/7c8c8b86-f69c-4699-a75e-dc2946cb22e0/assets/Delivery_Hero_Q2_2026_Trading_Update.pdf?disposition=inline), pp.3, 7–8; [tech.eu](https://tech.eu/2026/07/16/uber-to-acquire-delivery-hero-in-13b-deal-creating-platform-spanning-99-countries/))
- 📉 **APAC portfolio pruning** — Thailand exited ([FY25 deck](https://ir.deliveryhero.com/media/document/9e289f1f-e210-4e7d-bc0e-77c3f86814ee/assets/Delivery_Hero_FY_2025_Results.pdf?disposition=inline)); foodpanda Taiwan sold to Grab for US$600m ([Malay Mail](https://www.malaymail.com/news/money/2026/03/23/singapores-grab-snaps-up-foodpanda-taiwan-in-us600m-deal-with-delivery-hero/213612); [Grab 6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000051/foodpandtaiwan-finalannoun.htm))
- 💳 **Baemin is adding methods fast** — carrier billing (May 2026, [ddaily](https://www.ddaily.co.kr/page/view/2026052015503597830)); PAYCO and meal vouchers (Aug 2026, [MTN](https://news.mtn.co.kr/news-detail/2026082709564142678)); foreign-issued cards via Apple Pay (Jun 2026, search summary only)
- 💼 **Payments hiring** — Berlin "Product Manager – Payments, Fintech" (orchestration, multi-PSP; expired, date unknown); foodpanda SG "Specialist, Digital Payments" and Senior PM, Checkout (search summary only; live status unknown)

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Delivery Hero` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

> **Do not generate a cold sequence until the Uber question is cleared internally.** See Insight #1.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 17 / 29 (arithmetic) → override to 🔴 Low (cold outreach)
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | +5 | ✅ **SOURCED: ~327m orders/month (group)** — 981m orders in Q2 2026 ÷ 3 ([Q2 2026 Trading Update](https://ir.deliveryhero.com/media/document/7c8c8b86-f69c-4699-a75e-dc2946cb22e0/assets/Delivery_Hero_Q2_2026_Trading_Update.pdf?disposition=inline), p.11). **Billing unit: one consumer order.** Asia orders are not disclosed. Asia GMV of €5.01bn in Q2 2026 makes APAC volume far above 100k/month on any plausible order value. The APAC-specific count is **not** sourced. |
| Orchestration status | +1 | ✅ In-house orchestration layer: Berlin Payments Tribe job ad ("payment orchestration", "multi-PSP"), 400-person payments organisation, several PSPs live at once. |
| 3+ countries | +3 | ✅ Six APAC countries with >1% of combined web traffic; local entities in KR, SG, MY, PH, PK, TW. |
| Multiple PSPs | +3 | ✅ Adyen and PayPal ([Source Code], foodpanda.sg), Cybersource ([Press Release], TechNode), Checkout.com ([Provider Case Study]). |
| Local rail or licensing gap in a top-3 market | 0 | ⬜ Top 3 APAC markets are KR, PK and TW. KakaoPay (KR) and JKOPay / Taiwan Pay (TW) were **not found**, but no source confirms they are **absent**, and checkouts are in-app. Local entities exist everywhere, so there is no acquiring gate. Uncertain = 0. |
| Recent expansion | 0 | ❌ The 12-month picture is contraction: Thailand exited, Taiwan sold. Baemin's new payment methods are product additions, not market expansion. |
| Payment issues reported | 0 | ⬜ foodpanda SG and PK Trustpilot refund and charge complaints (1.5/5 for SG) are search summary only. The MY payment outage dates from 2021. Not scored. |
| Funding >$10M | 0 | ❌ No funding round. The Uber takeover is M&A, not funding. |
| High traffic outside home | +2 | ✅ Germany does not appear in any supplied domain's top 10. 100% of supplied traffic is outside the home market. **Double-counts the 3+ countries signal — see override.** |
| Competitor using orchestration | +2 | ✅ **Rappi → Yuno** (Yuno case study, y.uno). Rappi competes with DH's PedidosYa in LATAM, **not in APAC**. In APAC, Swiggy and Zepto use Juspay (vendor case studies), but they are peers, not DH competitors. |
| Payment job postings | +1 | ✅ Berlin PM Payments/Fintech (page read; expired, posting date unknown). SG Digital Payments roles are search summary only. |

**Tier on arithmetic:** 17 → ⭐ High Priority.

**ANALYST OVERRIDE → 🔴 Low for cold SDR outreach. Escalate as a strategic / Uber-relationship account instead.** Four reasons:
1. **The buyer is changing, and the new owner is a Yuno customer.** Uber's offer is board-supported. Prosus has irrevocably committed its 16.8% residual stake. Uber already holds 24.99% directly plus 11.8% via instruments ([Naspers, 16 Jul 2026](https://www.naspers.com/news-insights/regulatory-updates/2026/prosus-gives-irrevocable-undertaking-to-sell-residual-stake-in-delivery-hero-to-uber)). DH says the two run independently until H2 2027 closing, then integrate "onto one platform over time". A cold pitch to DH's payments team now is (a) unlikely to win a platform decision during a pending takeover, and (b) a pitch into Uber's future subsidiary that Yuno's Uber team should own.
2. **In-house is the hardest motion.** DH runs a 400-person payments organisation, built its own orchestration layer and spun out Payrails' founders (search summary only). The pitch can only be reach and opportunity cost, never "you need orchestration".
3. **Double-counting.** "3+ countries" and "high traffic outside home" both fire on one fact: DH is a multi-country group with no consumer brand in its home market. Remove one and the score is **15 → 🟢 Medium**, before any judgement about the takeover.
4. **The APAC footprint is shrinking and the decision sits in Berlin.** Thailand is gone, Taiwan is going, and Baemin was on the block in May 2026 before the Uber bid (search summary only). The group payments platform is run from Berlin (EMEA). What is left in APAC for an APAC SDR is Baemin (separate Korean stack) and foodpanda SEA/PK, and both answer to that platform.

**What would reopen it:** (a) the Uber deal fails; (b) the Uber account owner wants an APAC-side door into DH ahead of integration; or (c) Baemin is carved out or sold separately. In (c), re-score **Woowa Brothers** on its own: it is Korea-only, so the 3+ countries signal falls away.

### Source Notes
- ✅ Uber offer €41.50/share, ~€13bn, closing H2 2027, independent operation until closing — DH Q2 2026 Trading Update pp.3, 7–8 (read); tech.eu 16 Jul 2026 (read)
- ✅ Prosus stake sales and irrevocable undertaking; Uber 24.99% + 11.8% — Naspers regulatory update, 16 Jul 2026 (read by Agent 1)
- ✅ Group orders 981m Q2 2026; Asia GMV €20,779.7m FY25 and €9,930.3m H1 2026; Asia revenue €4,107.6m FY25 — Q2 2026 deck (read)
- ✅ Thailand listed as exited in FY24/25 — FY 2025 Results deck (read)
- ✅ foodpanda Taiwan → Grab, US$600m; Taiwan FY25 GMV €1.5bn — Malay Mail (read); Grab 6-K (read by Agent 5, which reports ~US$1.8bn GMV, consistent at FX)
- ✅ Adyen merchant ID "DeliveryHero", 3DS and recurring enabled, guest checkout disabled, PayPal production — foodpanda.sg/contents/privacy.htm page source (saved copy re-checked)
- ✅ Woowa Brothers business reg. 120-87-65763 — baemin.com footer (re-checked)
- ✅ Baemin carrier billing via KG Financial, with quote from Woowa's head of payment & settlement product — ddaily, 20 May 2026 (read by Agent 4)
- ✅ Baemin PAYCO — MTN, 27 Aug 2026 (read by Agent 3)
- ✅ Cybersource APAC partnership — TechNode, 25 Jul 2024 (read by Agent 2)
- ✅ Checkout.com case study (2023) — read by Agent 2
- ✅ Uber and Rappi on Yuno's customer list — y.uno/en (read)
- ⚠️ Fiserv as primary acquirer in SG/HK (Oct 2024) — search summary only; PDF fetch failed twice
- ⚠️ foodpanda.sg multi-PSP adapter bundle (Cybersource, Ant/Alipay+, Xendit, Razer, Reddot, SSLCommerz, Global Payments) — from an agent fetch, **not re-verified** (403 on re-fetch)
- ⚠️ Baemin foreign-card acceptance via Apple Pay, foreign-method orders ~3.7× YoY in Q1 2026 — search summary only
- ⚠️ Baemin sale process (~₩8tn, May 2026) and its halt after the Uber bid — search summary only
- ⚠️ CEO Niklas Östberg to step down by 31 Mar 2027 — search summary only
- ⚠️ All foodpanda APM rows except MY Adyen acquiring — search summaries only; foodpanda help centres are bot-walled

### Success Case Alternatives
- **Uber (Yuno customer)** — **not a case to cite, a relationship to use.** Ask the Uber account owner what Uber runs on Yuno and in which markets. If DH's markets will migrate onto Uber's stack post-close, Yuno's path into DH runs through Uber.
- **Rappi** — **closest profile match.** Multi-country delivery super-app with many local methods; vendor case study on y.uno. Results are LATAM, so do not imply Asian numbers. **Sensitivity:** Rappi competes head-on with DH's PedidosYa, and Yuno's founders are ex-Rappi. A DH payments leader will know both facts.
- **Swiggy / Zepto (Juspay)** — not Yuno cases. They are evidence that APAC delivery and q-commerce players run orchestration, but **never name competitors in outreach**.

---

## Executive Summary

Delivery Hero is a Berlin-based delivery group (FY2025 GMV €49.2bn). Its Asia segment, Baemin in Korea and foodpanda across South and Southeast Asia, is its largest region at €20.8bn GMV. Payments run on an **in-house group platform** built by a ~400-person payments organisation. It uses Adyen (live in foodpanda.sg's web config with 3DS and recurring on), Cybersource for tokenized checkout with local acquiring in 10+ APAC markets, Checkout.com, PayPal, and per-market wallets. Baemin runs its own Korean wallet stack. The motion is **in-house**, the hardest kind. More importantly, **Uber, a Yuno customer, agreed in July 2026 to buy the whole group**, with closing in H2 2027 and integration onto one platform afterwards. This account belongs in an internal conversation with the Uber account owner, not in a cold APAC sequence.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** **Supplied** — Similarweb Sales Intelligence, `accounts/traffic/delivery-hero.md` + `accounts/traffic/foodpanda.md`, pulled 2026-10-19, Jul–Sep 2026, desktop + mobile web. **App traffic excluded.**

**Per-domain average monthly visits (supplied):** glovoapp.com 5.831M · talabat.com 5.506M · baemin.com 4.891M · foodpanda.pk 3.063M · foodpanda.com.tw 2.454M · foodpanda.ph 1.940M · foodpanda.my 1.874M · foodpanda.sg 1.125M · **Total 26.68M**

**Combined country split** — built visits-first per the files' rule. Each domain's tail outside its top 10 (0.13%–15.5%) is unattributed, so every share is a **lower bound**.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | **South Korea** | **18.22%** | ~4.86M `[DERIVED]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | **Pakistan** | **10.72%** | ~2.86M `[DERIVED]` | Not supplied | same |
| 3 | **Taiwan** | **9.01%** | ~2.40M `[DERIVED]` | Not supplied | same |
| 4 | **Philippines** | **6.68%** | ~1.78M `[DERIVED]` | Not supplied | same |
| 5 | **Malaysia** | **6.47%** | ~1.73M `[DERIVED]` | Not supplied | same |
| 6 | Spain *(EMEA)* | 4.84% | ~1.29M `[DERIVED]` | Not supplied | same |
| 7 | Singapore | 4.08% | ~1.09M `[DERIVED]` | Not supplied | same |
| 8 | Italy *(EMEA)* | 4.01% | ~1.07M `[DERIVED]` | Not supplied | same |
| 9 | Qatar *(EMEA)* | 3.60% | ~0.96M `[DERIVED]` | Not supplied | same |
| 10 | Egypt *(EMEA)* | 3.55% | ~0.95M `[DERIVED]` | Not supplied | same |

**APAC-only view** (6 markets, ~14.72M/month = 100%): South Korea 33.0% · Pakistan 19.4% · Taiwan 16.3% · Philippines 12.1% · Malaysia 11.7% · Singapore 7.4%.

- **High priority (>5% of combined):** KR, PK, TW, PH, MY. **Taiwan is being sold to Grab**, so the effective APAC top 3 after closing is **KR, PK, PH**.
- Each APAC domain is 91–99% domestic. Baemin is 99.39% Korea. **These are domestic businesses, not cross-border ones.**
- **Device split:** mobile web dominates on every APAC foodpanda domain (57–87%). foodpanda.pk is the most mobile at 87%.
- **Do not read this as transaction share.** The traffic file itself warns this is an app-heavy food-delivery business. Use it as a market-mix signal only. The Gulf (talabat) and Europe (Glovo) rows are out of territory and shown only to make clear the combined total is not APAC.
- **Not in the data:** foodpanda Hong Kong, Bangladesh, Cambodia, Laos and Myanmar. All are operating markets per search summaries, but no traffic was supplied. **Hong Kong may be material:** foodpanda took over Deliveroo HK's assets in Apr 2025 (search summary only).

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Berlin, Germany. Delivery Hero SE, founded 2011 ([tech.eu](https://tech.eu/2026/07/16/uber-to-acquire-delivery-hero-in-13b-deal-creating-platform-spanning-99-countries/)). APAC regional HQ entity: not confirmed. Singapore is the likely candidate `[INFERENCE, not confirmed]`.

**Ownership (as of Jul 2026):** Uber holds 24.99% directly plus 11.8% via instruments. Prosus has irrevocably undertaken to tender its residual 16.8% to Uber. Aspex bought ~5% from Prosus in May 2026 ([Naspers](https://www.naspers.com/news-insights/regulatory-updates/2026/prosus-gives-irrevocable-undertaking-to-sell-residual-stake-in-delivery-hero-to-uber)). Offer acceptance level: not found.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Germany | Delivery Hero SE | Not researched | [DH IR](https://ir.deliveryhero.com/) |
| South Korea | (주)우아한형제들 / Woowa Brothers Corp. (CEO 김범석) | Biz reg. **120-87-65763**; 통신판매업 2012-서울송파-0515 | [baemin.com footer](https://www.baemin.com/) (read) |
| Singapore | Delivery Hero (Singapore) Pte. Ltd. (fka foodpanda Singapore Pte. Ltd.) | UEN 201209757Z | [sgpbusiness.com](https://www.sgpbusiness.com/company/Delivery-Hero-Singapore-Pte-Ltd) — directory, search summary only; not checked on ACRA |
| Malaysia | Delivery Hero Malaysia Sdn. Bhd. (fka Foodpanda Malaysia Sdn. Bhd.), inc. 7 May 2012 | 201201019422 (989567-W) | [Experian MY](https://buy.experian.com.my/index.php/search/Malaysia-Company/989567/FOODPANDA-MALAYSIA-SDN.-BHD.) — directory, search summary only |
| Philippines | Delivery Hero Philippines, Inc. (platform); **DH Philippines Blue Services, Inc.** (postpaid payment processing) | Not found | [foodpanda.ph postpaid T&Cs](https://www.foodpanda.ph/contents/postpaid-terms-and-conditions) — search summary only |
| Pakistan | Delivery Hero Pakistan (Private) Limited (T&Cs dated 17 Jun 2026); pandapay wallet terms name R-Sc Internet Services Pakistan (Pvt) Ltd | Not found | [foodpanda.pk T&Cs](https://www.foodpanda.pk/contents/terms-and-conditions.htm); [pandapay terms](https://www.foodpanda.pk/contents/pandapay-user-account-terms-and-conditions) — search summary only |
| Taiwan | 富胖達股份有限公司 — **pending sale to Grab** | Not found | [TechNews](https://finance.technews.tw/2026/07/22/fair-trade-commission-20260722/) — search summary only |
| HK, BD, KH, LA, MM | Not found | — | — |

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| South Korea | Yes (#1) | ✅ Yes | Entity present — gate not relevant | Low |
| Pakistan | Yes (#2) | ⚠️ Yes (T&Cs, search summary only) | Entity present | Low |
| Taiwan | Yes (#3) | ⚠️ Yes — being divested | Entity present | Low; leaving the group |
| Philippines | Yes (#4) | ⚠️ Yes (T&Cs, search summary only) | Entity present | Low |
| Malaysia | Yes (#5) | ⚠️ Yes (directory) | Entity present | Low |
| Singapore | Yes (#7) | ⚠️ Yes (directory) | Entity present | Low |

**No cross-border warning applies.** Every material APAC market has a local operating entity. The cross-border angle is **inbound**: foreign tourists paying on Baemin (see Section 7). It is not a missing-entity story.

> **MANUAL:** foodpanda T&Cs are bot-walled. Open foodpanda.pk/.ph/.my/.sg `/contents/terms-and-conditions.htm` in a browser to confirm the contracting entity and any named payment processor per market.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Singapore (web) | **Adyen** — merchant account `"DeliveryHero"`, client-side encryption key, `is_adyen3_d_s_enabled: true`, `is_adyen_recurring_enabled: true` | [Source Code] | [foodpanda.sg/contents/privacy.htm](https://www.foodpanda.sg/contents/privacy.htm) (page source, 2026-10-19) |
| Singapore (web) | **PayPal** — `paypal_environment: "production"` | [Source Code] | same |
| Malaysia | **Adyen** — local acquiring launch merchant (Jul 2020) | [Press Release] | [Adyen](https://www.adyen.com/en_GB/press-and-media/adyen-acquiring-malaysia) (search result; old) |
| APAC, "10+ markets" (unnamed) | **Cybersource (Visa)** — tokenized checkout "with local acquiring"; aims to offload PCI and improve authorisation rate | [Press Release] | [TechNode, 25 Jul 2024](https://technode.global/2024/07/25/foodpanda-partners-visa-solution-cybersource-to-enhance-customer-checkout-experience-in-apac) |
| Singapore, Hong Kong | **Fiserv** — reportedly primary acquirer (Oct 2024) | [Press Release] `[UNVERIFIED — search summary only, page not fetched]` | [Fiserv newsroom](https://newsroom.fiserv.com/node/49896/pdf) |
| Group (MENA-led; "extending to APAC and Europe") | **Checkout.com** — client since 2019; network tokenization; cross-border smart routing | [Provider Case Study] | [Checkout.com](https://www.checkout.com/case-studies/how-localized-payments-is-driving-delivery-hero-s-global-expansion) |
| Group | **Adyen** — risk management (RevenueProtect) | [Provider Case Study] | [Adyen](https://www.adyen.com/zh_CN/knowledge-hub/delivery-hero-tucks-into-risk-management) (search result) |
| Malaysia | **Alipay+** — Touch 'n Go eWallet (Feb 2023) | [Press Release] `[UNVERIFIED — search summary only]` | [Business Wire](https://www.businesswire.com/news/home/20230131005758/en/) |
| Hong Kong | **HSBC PayMe** | [Provider Case Study] `[UNVERIFIED — search summary only]` | [HSBC HK](https://www.business.hsbc.com.hk/en-gb/insights/optimising-sales/foodpanda-reduces-cash-on-delivery-with-payme) |
| SG / TH / MY | **HSBC** — rider payout APIs (payouts, not checkout) | [Provider Case Study] | [HSBC GBM](https://www.gbm.hsbc.com/en-gb/feed/innovation/driving-foodpandas-growth-through-payment-apis) (search result) |
| South Korea | **KG Financial** — carrier billing inside Baemin Pay | [Third-Party Report] | [ddaily, 20 May 2026](https://www.ddaily.co.kr/page/view/2026052015503597830) |
| South Korea | **NHN PAYCO** | [Third-Party Report] | [MTN, 27 Aug 2026](https://news.mtn.co.kr/news-detail/2026082709564142678) |
| South Korea | Card PG (KG Inicis / NHN KCP / Toss Payments / NICEPAY) | **Not found** | — |
| foodpanda (bundle) | Payment-method adapters reported for Cybersource, Ant/Alipay+, Xendit, Razer (MY), Reddot (SG PayLah!), SSLCommerz (BD), Global Payments (TW PXPay) | [Source Code] — **agent fetch of foodpanda.sg homepage, not re-verified** (re-fetch blocked, 403). This is a shared group bundle: it shows adapters exist, not what is live per market. | [foodpanda.sg](https://www.foodpanda.sg/) |

**Read:** DH runs a genuine multi-PSP, multi-acquirer setup in APAC: Adyen and PayPal in live web config, Cybersource with local acquiring, Fiserv (unverified) and Checkout.com at group level. One merchant account name ("DeliveryHero") on a foodpanda storefront points to a **central group platform**, not per-country stacks.

#### 3B. Payment Orchestrator

**Classification: In-house orchestration layer.**

- [Job Listing] DH Berlin, "Product Manager – Payments, Fintech", Payments Tribe. The ad says the role means "bringing key Payments products to market via Delivery Hero's regional platforms" and to "design and deliver payment orchestration and platform improvements". Nice-to-have: "Experience with payment orchestration, routing, or multi-PSP environments". It adds that "Delivery Hero provides payment solutions for customers, riders, and for our family of brands worldwide." ([careers.deliveryhero.com](https://careers.deliveryhero.com/job/product-manager-payments-fintech-in-berlin-germany-jid-9819), page read, marked expired, posting date unknown)
- [Job Listing] "Group Product Manager, Fintech (Global Payment)": "global orchestration product strategy", "global payment integrations platform" ([careers.deliveryhero.com](https://careers.deliveryhero.com/job/group-product-manager-fintech-global-payment-in-berlin-germany-jid-3366)) `[UNVERIFIED — search summary only]`
- [Provider Case Study] "Over 200 payment professionals in Berlin and about 200 more worldwide" ([Checkout.com](https://www.checkout.com/case-studies/how-localized-payments-is-driving-delivery-hero-s-global-expansion))
- [Third-Party Report] Payrails (a payments orchestration vendor) was founded by ex-DH staff who built DH's payment system; DH's CFO was a seed investor ([fintech.global](https://fintech.global/2022/03/17/payment-operating-system-payrails-launches-from-stealth/)) `[UNVERIFIED — search summary only]`. **No evidence DH uses Payrails as a vendor.**
- **Baemin is likely separate.** Baemin Pay (launched 2019; 10M+ users and 600M+ transactions by Jan 2023 per [byline.network](https://byline.network/2023/01/9-127/), search summary only) is Woowa's own wallet. No evidence was found that Baemin runs on DH's Berlin platform `[INFERENCE, not confirmed]`.

> *"Confirmed orchestration-aware, and built in-house. The opening is not the case for orchestration; it is reach, maintenance cost and, now, what happens to this platform when Uber integrates it."*

> **MANUAL:** Walk through the foodpanda SG and PH app checkout with a proxy (Charles or mitmproxy) to see which PSP endpoints card and wallet calls hit per market. Do the same in Baemin to identify the Korean card PG.

---

### Section 4: Alternative & Local Payment Methods

No official help-centre page was readable for any foodpanda market (bot-walled). Rows marked `search summary` were not confirmed on the page itself.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| KR | PAYCO (card, coupons, points) + PAYCO mobile meal vouchers (식권) | Digital wallet | Mentioned in press (Aug 2026, read) | [MTN](https://news.mtn.co.kr/news-detail/2026082709564142678) |
| KR | Carrier billing in Baemin Pay (postpaid, ≤₩1M, via KG Financial) | Carrier billing | Mentioned in press (May 2026, read) | [ddaily](https://www.ddaily.co.kr/page/view/2026052015503597830) |
| KR | Baemin Pay: Pay Money (stored value), linked bank account, Baemin Pay card | Digital wallet / A2A | Mentioned in press — search summary only | [SBS Biz](https://biz.sbs.co.kr/amp/article/20000337807) |
| KR | Apple Pay incl. foreign-issued Visa/MC/JCB/Amex (from 2 Jun 2026) | Cards / wallet | Mentioned in press — search summary only | [ddaily](https://www.ddaily.co.kr/page/view/2026053108445282961) |
| KR | Naver Pay | Digital wallet | Mentioned (namu wiki, date unclear) — search summary only | [namu](https://www.namu.moe/w/N%20Pay) |
| KR | Toss Pay | Digital wallet | Mentioned in press (2022) — current status unknown | [MTN 2022](https://news.mtn.co.kr/news-detail/2022033111405668188) |
| KR | KakaoPay | Digital wallet | **Not found** | — |
| KR | Meet-and-pay (card/cash at door) | Cash | Search summary only (blog) | [brunch](https://brunch.co.kr/@coygray/607) |
| PK | Debit/credit cards, JazzCash, Easypaisa | Cards / wallets | Mentioned in press (Nov 2024 op-ed by foodpanda PK Head of Fintech) — search summary only | [Daily Pakistan](https://en.dailypakistan.com.pk/14-Nov-2024/why-paying-online-is-the-smart-choice) |
| PK | pandapay wallet (split with card allowed; not with COD) | Digital wallet | Mentioned in docs — search snippet only (403) | [foodpanda.pk](https://www.foodpanda.pk/contents/pandapay-5) |
| PK | Cash on delivery | Cash | Mentioned in docs — search snippet only | same |
| PK | Raast | Bank transfer / A2A | **Not found** | — |
| TW | Cards, Apple Pay, LINE Pay, PXPay (全支付, added 2025); cash ~30% of orders | Cards / wallets / cash | Mentioned in press — search summary only | [TechNews](https://technews.tw/?p=1406384) |
| TW | JKOPay, Taiwan Pay | Digital wallet | **Not found** at checkout. A JKOPay adapter was reported in the group bundle (not re-verified). | — |
| PH | Cards, GCash, Maya, COD | Cards / wallets / cash | Search summary only (forum) | [expat.com](https://www.expat.com/en/forum/asia/philippines/1095378-food-delivery-and-apps-in-the-philippines.html) |
| PH | QR Ph on delivery (rider shows QR; GCash, Maya or bank app) — new May 2026 | QR / A2A | Mentioned in press — search summary only | [newsbytes.ph](https://newsbytes.ph/2026/05/16/foodpanda-adds-qrph-payments-for-cash-on-delivery-orders/) |
| PH | pandapay; COD vs online ~50/50 (2023) | Wallet / cash | Search summary only | [newsbytes.ph 2023](https://newsbytes.ph/2023/09/20/pinoys-split-between-cashless-cash-payments-report/) |
| PH | foodpanda × EastWest × Visa co-branded credit card (Nov 2025) | Cards | Mentioned in press — search summary only | [context.ph](https://context.ph/2025/11/27/foodpanda-pushes-filipinos-toward-cashless-payments-with-new-co-branded-credit-card/) |
| MY | Touch 'n Go eWallet (via Alipay+, Feb 2023) | Digital wallet | Mentioned in press — search summary only, several outlets | [The Sun](https://www.thesundaily.my/business/you-can-now-pay-for-foodpanda-deliveries-with-touch-n-go-ewallet-LD10648344) |
| MY | Cards (Adyen local acquiring, 2020) | Cards | Mentioned in press | [Adyen](https://www.adyen.com/en_GB/press-and-media/adyen-acquiring-malaysia) |
| MY | COD | Cash | Search summary only (2021) | [Lowyat](https://lowyat.net/2021/241620/foodpanda-payment-system-currently-facing-issues-cod-as-only-available-option) |
| MY | FPX, DuitNow, Boost, GrabPay | Bank transfer / wallets | **Not found.** FPX via MOLPay and DuitNow via Razer adapters were reported in the bundle (not re-verified). | — |
| SG | Cards, pandapay, Google Pay, PayPal, DBS PayLah!, cash | Mixed | Third-party blog, date unclear — search summary only. PayPal is also in the web config ([Source Code]). | [HoneyKids](https://honeykidsasia.com/food-delivery-apps-in-singapore/) |
| SG | PayNow, GrabPay | A2A / wallet | **Not found** | — |
| HK | Cards, PayPal, AlipayHK, PayMe, WeChat Pay HK, Apple/Google Pay, pay at door | Mixed | Search summary only (~2021; 2026 Octopus promo T&Cs) | [Octopus promo](https://www.octopus.com.hk/en/consumer/latest-promotions/food-panda.html) |
| HK | FPS, Octopus (stored value) | A2A / wallet | **Not found** | — |
| BD | bKash (direct and tokenised; 2026 new-user promo) | Digital wallet | Mentioned in press — search summary only | [bKash](https://www.bkash.com/en/campaign/foodpanda-new-user) |
| Global | pandapro (subscription) — card required (PH, older); bKash or cards (BD) | Recurring | Search summary only | [UNB](https://unb.com.bd/category/Business/foodpanda-launches-pandapro-subscription-in-bangladesh/98022) |
| KR | Baemin Club (₩3,990/month) — billing method not found | Recurring | Search summary only | [SBS Biz](https://biz.sbs.co.kr/amp/article/20000337807) |

**No rail-gap warning is issued.** Nothing above is confirmed *absent*: KakaoPay, JKOPay, FPX, PayNow and Raast are only "not found", and checkouts are in-app. On the evidence, DH covers the dominant local wallets in each market (GCash/Maya, JazzCash/Easypaisa, TNG, LINE Pay, bKash) and is still **adding** rails (Baemin PAYCO and carrier billing, PH QR Ph). This is not a merchant with coverage holes.

> **MANUAL:** VPN plus app install for foodpanda MY and SG checkouts to confirm FPX, DuitNow and PayNow, and for Baemin to confirm KakaoPay.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Slow / missing refunds on cancelled orders | Trustpilot (foodpanda SG; TrustScore 1.5/5, 146 reviews) | Moderate | Undated | [Trustpilot](https://ie.trustpilot.com/review/www.foodpanda.sg) `[UNVERIFIED — search summary only]` |
| Card charged on a COD order; promised refund not received | Trustpilot (foodpanda PK) | Moderate | 2024–2025 | [Trustpilot](https://fr.trustpilot.com/review/foodpanda.pk) `[UNVERIFIED — search summary only]` |
| Online payment outage; COD only; cards charged on failed payments | Press (foodpanda MY) | Single incident, high impact | Jun 2021 | [Lowyat](https://lowyat.net/2021/241620/foodpanda-payment-system-currently-facing-issues-cod-as-only-available-option) `[UNVERIFIED — search summary only]` |
| "Payment failed" but card charged | Forum (techenclave) | Isolated | Undated, likely old | [techenclave](https://techenclave.com/threads/foodpanda-app-failed-payment-issue.174031/) `[UNVERIFIED — search summary only]` |
| Baemin Club refund policy tightened (full refund within 7 days only) | Press (KR) | Policy, not failure | ~May 2025 | [SBS Biz](https://biz.sbs.co.kr/amp/article/20000232915) `[UNVERIFIED — search summary only]` |

No Reddit, X or app-store payment-failure threads were retrieved, and no Baemin payment-error complaints were found. **The refund pattern is a customer-service issue, not a payment-infrastructure one.** It is not usable as an orchestration hook.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 2026-07-16 | **Uber agrees to acquire Delivery Hero**: €41.50/share all-cash, ~€13bn equity, boards support, closing H2 2027; separate sale of 14 non-APAC country businesses to SSW Partners for ~€1.4bn; Prosus tenders its residual 16.8% | M&A | [DH Q2 2026 Trading Update](https://ir.deliveryhero.com/media/document/7c8c8b86-f69c-4699-a75e-dc2946cb22e0/assets/Delivery_Hero_Q2_2026_Trading_Update.pdf?disposition=inline); [tech.eu](https://tech.eu/2026/07/16/uber-to-acquire-delivery-hero-in-13b-deal-creating-platform-spanning-99-countries/); [Naspers](https://www.naspers.com/news-insights/regulatory-updates/2026/prosus-gives-irrevocable-undertaking-to-sell-residual-stake-in-delivery-hero-to-uber) |
| 2 | 2026-07-22 | Taiwan FTC extends its review of Grab–foodpanda Taiwan; **decision due 2026-10-27** | M&A | [Focus Taiwan](https://focustaiwan.tw/business/202607220014) |
| 3 | 2026-05 | Baemin sale process reported (~₩8tn; bidders incl. Uber, Naver, Alibaba, DoorDash), reportedly halted once Uber bid for the group | M&A | [Korea Herald](https://www.koreaherald.com/article/10738059); [Herald Biz](https://mbiz.heraldcorp.com/article/10814779) `[UNVERIFIED — search summary only]` |
| 4 | 2026-03-23 | foodpanda Taiwan sold to Grab for US$600m cash; Grab to migrate users to its app by early 2027 | M&A | [Malay Mail](https://www.malaymail.com/news/money/2026/03/23/singapores-grab-snaps-up-foodpanda-taiwan-in-us600m-deal-with-delivery-hero/213612); [Grab 6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000051/foodpandtaiwan-finalannoun.htm) |
| 5 | 2025-12-09 | Strategic review announced (JPMorgan advising); Taiwan sale described as the "1st step" | M&A | [FY 2025 Results deck](https://ir.deliveryhero.com/media/document/9e289f1f-e210-4e7d-bc0e-77c3f86814ee/assets/Delivery_Hero_FY_2025_Results.pdf?disposition=inline) |

Earlier and related: Thailand exited during FY24/25 (FY25 deck); Uber's first foodpanda Taiwan deal was terminated in Mar 2025 after the FTC blocked it ([TechCrunch](https://techcrunch.com/2025/03/11/uber-terminates-foodpanda-taiwan-acquisition-citing-regulatory-hurdles)); foodpanda took over Deliveroo HK's assets on its Apr 2025 exit ([Asia IP](https://asiaiplaw.com/article/deliveroo-sells-assets-to-rival-foodpanda-before-hong-kong-exit), search summary only).

**Payment RFP:** *No public payment-related RFP found.*
**Payment hiring:** Berlin PM Payments/Fintech (orchestration, multi-PSP; expired); "Principal, Global Payments Commercial Partnerships" covering 30+ markets ([hiretechladies](https://www.hiretechladies.com/jobs/principal-global-payments-commercial-partnerships-delivery-hero-6u), undated, search summary only); foodpanda SG Senior PM, Checkout & Post-Order Fulfilment ([careers.deliveryhero.com](https://careers.deliveryhero.com/job/senior-product-manager-in-singapore-jid-10799), search summary only). Live status unknown for all.
**Licence applications:** none found. Note: a Nov 2025 Korean Electronic Financial Transactions Act amendment reportedly carves delivery-platform settlement out of mandatory PG registration ([Hankyung](https://www.hankyung.com/article/202512056610i), search summary only).

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 2026-08-27 | Baemin adds PAYCO simple pay and PAYCO mobile meal vouchers (alcohol excluded) | Baemin is broadening wallets; corporate meal-voucher flow | [MTN](https://news.mtn.co.kr/news-detail/2026082709564142678) |
| 2 | 2026-05-31 | Baemin accepts **foreign-issued cards via Apple Pay** from 2 Jun 2026, reportedly a first among Korean delivery apps. Foreign-method orders reportedly ~3.7× YoY in Q1 2026; April payment value ~14× YoY | **Inbound cross-border on a domestic stack**, the only cross-border angle in this account | [ddaily](https://www.ddaily.co.kr/page/view/2026053108445282961); [Asia Economy](https://view.asiae.co.kr/article/2026053113285274214) `[UNVERIFIED — search summary only]` |
| 3 | 2026-05-20 | Baemin Pay adds carrier billing via KG Financial. Quote from **Choi Seong-gil (최성길), head of Woowa's payment & settlement product division** | Named Woowa payments leader | [ddaily](https://www.ddaily.co.kr/page/view/2026052015503597830) |
| 4 | 2026-05-16 | foodpanda PH adds QR Ph payment for cash-on-delivery orders | Cash-to-digital push in PH | [newsbytes.ph](https://newsbytes.ph/2026/05/16/foodpanda-adds-qrph-payments-for-cash-on-delivery-orders/) `[UNVERIFIED — search summary only]` |
| 5 | 2025-11-27 | foodpanda × EastWest × Visa co-branded credit card (PH), cashback to pandapay | Wallet/loyalty build | [context.ph](https://context.ph/2025/11/27/foodpanda-pushes-filipinos-toward-cashless-payments-with-new-co-branded-credit-card/) `[UNVERIFIED — search summary only]` |

Older but material: foodpanda × Cybersource APAC tokenized checkout (Jul 2024, [TechNode](https://technode.global/2024/07/25/foodpanda-partners-visa-solution-cybersource-to-enhance-customer-checkout-experience-in-apac)); Fiserv as SG/HK primary acquirer (Oct 2024, search summary only). **No provider removals found.**

---

### Section 8: Checkout Experience Audit

*Full checkout flow not accessible. foodpanda.sg is a JS-rendered SPA and most foodpanda pages are bot-walled. Ordering is app-first. Findings are limited to the web configuration in page source.*

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | Custom-built group platform; Adyen client-side encryption on web | N/A | [Source Code], foodpanda.sg |
| Guest checkout | `is_guest_checkout_enabled: false` (SG web) | Not assessed | Account required on SG web |
| Steps to complete payment | Not accessible | — | — |
| Card input experience | Adyen CSE (card encrypted in browser to Adyen) | Not assessed | [Source Code] |
| Payment methods visible | Not accessible | — | See Section 4 |
| Location-based method display | Shared group method bundle; per-market config `[INFERENCE, not confirmed]` | — | — |
| Instalment / EMI options | Not found | — | Low relevance at food-delivery ticket sizes |
| 3DS implementation | `is_adyen3_d_s_enabled: true` | — | Version not visible |
| PCI indicator | Adyen CSE on web; Cybersource tokenization in APAC | — | See Section 9 |
| Mobile responsiveness | Not assessed | — | App-first |
| Multi-currency / local pricing | Local currency per country domain | — | Domestic businesses |
| Saved payment methods | `is_adyen_recurring_enabled: true`; Cybersource "no card re-entry" | — | Tokens split across PSPs `[INFERENCE, not confirmed]` |
| Error message clarity | A pandapro 3DS failure string exists ("There was some problem is processing your payment…") | — | Agent fetch, not re-verified |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found for DH SE, foodpanda or Woowa. talabat (Gulf) reported Level 1 in Jan 2022. | [Arabian Reseller](https://arabianreseller.com/2022/01/24/talabat-achieves-highest-level-of-pci-dss-certification-for-transactional-security/) (search result) |
| Card data handling | Adyen client-side encryption on web; Cybersource deal aims to offload foodpanda "from PCI-compliance requirements in multiple markets" | [Source Code]; [TechNode](https://technode.global/2024/07/25/foodpanda-partners-visa-solution-cybersource-to-enhance-customer-checkout-experience-in-apac) |
| Recommended Yuno integration | Back-to-back API `[INFERENCE, not confirmed]` — an in-house platform would integrate server-side, not via drop-in SDK | — |

`[INFERENCE, not confirmed]`: Based on Adyen client-side encryption and Cybersource tokenization, foodpanda's PCI scope is likely reduced, with the PSPs holding card data. **That also means stored cards sit in several PSP vaults, not one DH-owned vault.** That matters for any migration, including an Uber integration.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: This is an Uber-relationship decision, not a cold account**
> **Evidence:** Uber's board-supported takeover, closing H2 2027, then integration "onto one platform over time" (S6, [Q2 2026 deck](https://ir.deliveryhero.com/media/document/7c8c8b86-f69c-4699-a75e-dc2946cb22e0/assets/Delivery_Hero_Q2_2026_Trading_Update.pdf?disposition=inline) pp.7–8) + Uber on Yuno's customer list ([y.uno](https://y.uno/en)) + DH's multi-PSP in-house platform (S3)
> **Pain Point:** At closing, two large in-house payment platforms with different PSP footprints have to converge. DH has Adyen, Cybersource, Checkout.com and per-market wallets across Asia; Uber has its own. Tokens sit in several PSP vaults (S9, inference).
> **Yuno Value Proposition:** If Uber already routes some payments through Yuno, DH's 60-odd markets, including €20.8bn of Asia GMV, are a natural expansion of that footprint. A PSP-agnostic layer reduces token-migration and re-integration cost.
> **Best Success Case:** Uber itself (existing relationship), not a cited case.
> **Outreach Angle:** **None external yet.** Internal: brief the Uber account owner with this report. Ask whether Uber's integration plan for DH touches payments, and whether APAC (Baemin, foodpanda) is in scope.
> **Suggested Subject Line:** (internal) "Delivery Hero → Uber: APAC payments footprint brief"

> **Insight #2: Baemin's inbound cross-border flow is new and growing on a domestic stack**
> **Evidence:** Baemin is 33% of DH's supplied APAC web traffic and 99.4% Korean (S1). Foreign-issued cards accepted via Apple Pay since Jun 2026, with foreign-method orders reportedly ~3.7× YoY (S7, search summary only). Woowa has a named payments leader, Choi Seong-gil (S7, [ddaily](https://www.ddaily.co.kr/page/view/2026052015503597830)). No evidence Baemin runs on DH's Berlin platform (S3B).
> **Pain Point:** A stack built for Korean domestic cards and wallets now takes foreign cards from tourists. Approval rates on foreign-issued cards through a domestic Korean setup are a known weak spot `[INFERENCE, not confirmed — no Baemin approval-rate data found]`.
> **Yuno Value Proposition:** Route foreign-issued cards to the acquirer best suited to them, alongside Baemin Pay, without rebuilding the domestic stack.
> **Best Success Case:** Rappi (multi-method delivery app). Do not imply Korean results.
> **Outreach Angle:** "Baemin opening foreign-issued cards through Apple Pay in June is a first for Korean delivery apps. How are approval rates on those cards tracking against domestic?"
> **Suggested Subject Line:** "Baemin's foreign-card orders"
> ⚠️ **Hold until Insight #1 is cleared internally.** Confirm the 3.7× figure on the article itself before using it.

> **Insight #3: A fragmented multi-PSP stack maintained by a 400-person team**
> **Evidence:** Adyen and PayPal in live foodpanda.sg config, Cybersource with local acquiring in 10+ APAC markets, Checkout.com at group level, Fiserv in SG/HK (unverified) (S3A) + per-market wallets in every APAC market (S4) + an in-house orchestration build (S3B, job ad) + "over 200 payment professionals in Berlin and about 200 more worldwide" (Checkout.com)
> **Pain Point:** Every new rail (Baemin PAYCO, carrier billing, PH QR Ph) is an in-house build and maintenance load. The platform is also about to be integrated with Uber's.
> **Yuno Value Proposition:** Reach and opportunity cost. One integration for incremental PSPs and APMs frees the in-house team for differentiation. **Never "you need orchestration"** — they built one.
> **Best Success Case:** Rappi.
> **Outreach Angle:** Only via the Uber relationship, or with Berlin if the EMEA owner takes it. There is no APAC SDR angle while the group platform decides centrally.
> **Suggested Subject Line:** "Every new rail is a build"

> **Insight #4: APAC competitors run in-house too, so there is no competitive-urgency story here**
> **Evidence:** Grab, Shopee, Coupang and Gojek are listed in-house on the TAL (S11); Uber has its own payments platform (S11); only Indian peers (Swiggy, Zepto) use a third-party orchestrator, Juspay, and DH is not in India (S1, S11)
> **Pain Point:** None to project. DH's direct APAC rivals (Grab, Coupang Eats, Keeta) do not give a "your competitors are moving" story.
> **Yuno Value Proposition:** N/A. This insight is a warning: do not build outreach on competitive urgency for DH in APAC.
> **Best Success Case:** —
> **Outreach Angle:** Do not use.
> **Suggested Subject Line:** —

---

### Quick Hits: Ready-to-Use Sales Ammunition

> **⛔ Do not use externally until the Uber question is cleared internally (Insight #1).**

**Email hooks (one sentence each):**
1. Baemin opening foreign-issued cards through Apple Pay in June was a first for a Korean delivery app, and it puts tourist-card approval rates on a domestic stack. *(Confirm the article before use.)*
2. Baemin added PAYCO, meal vouchers and carrier billing within four months this year. Every one of those is an integration someone in Seoul maintains.
3. foodpanda's checkout already runs Adyen with 3DS and stored cards, alongside Cybersource tokenization across 10+ APAC markets, so cards live in more than one vault.

**Cold call openers (conversational, one sentence each):**
1. "I saw Baemin started taking foreign cards through Apple Pay in June — is that running on the same setup as Baemin Pay, or separate?"
2. "You've added three new payment methods at Baemin since May — is your team building each of those in-house?"
3. "With the Uber deal closing next year, is anyone on your side already mapping how the two payment platforms come together?" *(Only with internal clearance — this one touches the Uber relationship directly.)*

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| Grab (GrabFood) | grab.com | Singapore | FY2025 revenue $3.37bn | SG, MY, PH (+TW on close) | Adyen partner since 2016 (GrabPay, 4 markets); TAL: in-house routing | [Adyen](https://www.adyen.com/press-and-media/grab-selects-adyen-as-payment-solution-partner-for-four-markets-in-southeast-asia); [20-F](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm) |
| Coupang Eats | coupangeats.com | South Korea | 37% of top-3 Korea app card spend, Feb 2025 | KR | TAL: Coupang Pay in-house; nothing public for Eats | [KED Global](https://www.kedglobal.com/newsView/ked202503240003) |
| Yogiyo | yogiyo.co.kr | South Korea | Distant #3 | KR | Not found | [JoongAng Daily](https://www.koreajoongangdaily.com/business/yogiyo-drops-commission-fee-to-97-percent-undercutting-baemin-and-coupang-eats/12313641) |
| Meituan Keeta | — | China | Reportedly 43% of HK orders, Q1 2024 (search summary only) | HK | Not found | [Tech Buzz China](https://techbuzzchina.substack.com/p/keeta-meituans-overseas-expansion) |
| Uber Eats | ubereats.com | US | — | TW, (JP) | In-house payments platform; **Yuno customer (Uber)** | [Uber MoneyCon](https://www.uber.com/blog/moneycon) |
| ShopeeFood (Sea) | shopee.com | Singapore | Reportedly #2 in SEA delivery, 2025 (search summary only) | SG, MY, PH | TAL: in-house routing | [DealStreetAsia](https://www.dealstreetasia.com/?p=470756) |
| LINE MAN Wongnai | lmwn.com | Thailand | — | TH (DH exited) | Owns LINE Pay Thailand (search summary only) | [Fintech News SG](https://fintechnews.sg/fintech-startups-thailand/fintech/line-pay/) |

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Rappi | rappi.com | Delivery super-app | LATAM | **Yuno customer** (2023) | [y.uno](https://www.y.uno/en/success-stories/rappi) |
| Swiggy | swiggy.com | Food + q-commerce | India | Juspay orchestration, PSP routing | [Hyperswitch](https://hyperswitch.io/case-studies/swiggy/) |
| Zepto | zeptonow.com | Q-commerce | India | Juspay orchestration | [Juspay](https://juspay.io/customer-stories/zepto) |
| Zomato / Blinkit (Eternal) | zomato.com | Food + q-commerce | India | TAL lists Juspay (not independently confirmed) | TAL |
| DoorDash / Wolt | doordash.com | Delivery | US / EU / JP | No orchestrator found | [DoorDash IR](https://ir.doordash.com/news/news-details/2021/DoorDash-Joins-Forces-with-Wolt/default.aspx) |
| Uber | uber.com | Mobility + delivery | Global | In-house platform + Yuno | [Uber](https://www.uber.com/blog/moneycon) |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| Rappi | Yuno | 2023 | Delivery super-app | [y.uno](https://www.y.uno/en/success-stories/rappi) |
| Swiggy | Juspay | Undated | Food delivery | [hyperswitch.io](https://hyperswitch.io/case-studies/swiggy/) |
| Zepto | Juspay | Undated | Q-commerce | [juspay.io](https://juspay.io/customer-stories/zepto) |

No **APAC direct competitor** of DH (Grab, Coupang Eats, Yogiyo, Keeta, ShopeeFood) was found adopting a third-party orchestrator.

#### 11D. Prospect Scoring

Verified signals only; everything else is ⬜ (0). These are indicative minimums, not full research runs.

| Company | Tx ≥100k | Orch. | 3+ ctry | Multi-PSP | Rail gap | Other | Score (min.) | Note |
|---------|----------|-------|---------|-----------|----------|-------|--------------|------|
| Coupang Eats | ⬜ | ⬜ | ❌ (KR + JP) | ⬜ | ⬜ | — | 0 verified | Needs a research run; Korean domestic stack |
| Meituan Keeta | ⬜ | ⬜ | ✅ (HK, Middle East, Brazil, per search summaries) | ⬜ | ⬜ | — | ~3 | **Not on TAL.** HK-facing and expanding — worth a research run |
| Yogiyo | ⬜ | ⬜ | ❌ | ⬜ | ⬜ | — | 0 | Shrinking (−42.7% card transactions YoY, search summary only) |
| Grab | ⬜ | +1 (in-house) | ✅ | ✅ (Adyen + others, old) | ⬜ | — | ~7 | In-house; acquiring foodpanda TW |
| LINE MAN Wongnai | ⬜ | ⬜ | ❌ | ⬜ | ⬜ | — | 0 | Owns LINE Pay TH; IPO talk (unverified) |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | **Meituan Keeta** | Competitor | HK (+ Middle East, Brazil) | ~3 (min.) | 🟢 Research | HK #1 player, international expansion | ❌ **No — genuine find** |
| 2 | Coupang Eats | Competitor | KR, JP | unscored | 🟢 Research | Fast share gains vs Baemin | ✅ |
| 3 | Grab | Competitor | SEA | ~7 | 🔴 | In-house; absorbing foodpanda TW | ✅ |
| 4 | Zepto | Peer | India | unscored | Displacement (Juspay) | Juspay case study | ✅ |
| 5 | Swiggy | Peer | India | unscored | Displacement (Juspay) | Juspay case study | ✅ |
| 6 | Zomato / Blinkit | Peer | India | unscored | Displacement (Juspay, TAL) | — | ✅ |
| 7 | LINE MAN Wongnai | Competitor | TH | unscored | 🔴 | Own wallet | ✅ |
| 8 | Yogiyo | Competitor | KR | unscored | 🔴 | Declining | ✅ |
| 9 | Demae-can | Peer | JP | not researched | — | — | ❌ (not researched) |
| 10 | Deliveroo Hong Kong | — | — | — | ⛔ | **Exited HK Apr 2025** — candidate for `/mark_not_icp` | ✅ (stale) |

**TAL hygiene:** `Foodpanda`, `Baemin` and `EASI` (foodpanda.com.tw) are separate rows, and all three are DH entities covered by this report. EASI/foodpanda Taiwan is being sold to Grab, and Deliveroo HK has exited. Consider consolidating the DH rows under this report.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | Group FY2025: **€14,059.6m**. Asia segment FY2025: **€4,107.6m** | [Q2 2026 deck](https://ir.deliveryhero.com/media/document/7c8c8b86-f69c-4699-a75e-dc2946cb22e0/assets/Delivery_Hero_Q2_2026_Trading_Update.pdf?disposition=inline) pp.23–24 |
| GMV / Gross Transaction Volume | Group FY2025: **€49,196.8m**. **Asia FY2025: €20,779.7m** (−2.9% LfL); Asia H1 2026: €9,930.3m. Taiwan FY2025: €1.5bn (Malay Mail) / ~$1.8bn (Grab 6-K) | same; [Malay Mail](https://www.malaymail.com/news/money/2026/03/23/singapores-grab-snaps-up-foodpanda-taiwan-in-us600m-deal-with-delivery-hero/213612) |
| Average Transaction Value | Group Q2 2026: **€13.46** (€13,208.6m GMV ÷ 981m orders). Asia AOV not derivable (orders not disclosed) | ✅ DERIVED, both inputs from the Q2 2026 deck |
| Est. Annual Transactions | Group ~3.9bn/year (981m × 4) `[ESTIMATE — annualised from one quarter]` | Calculated |
| **Monthly transaction count** | ✅ **SOURCED: ~327m orders/month (group)** — 981m orders in Q2 2026 ÷ 3 ([Q2 2026 deck](https://ir.deliveryhero.com/media/document/7c8c8b86-f69c-4699-a75e-dc2946cb22e0/assets/Delivery_Hero_Q2_2026_Trading_Update.pdf?disposition=inline), p.11). **Billing unit: one consumer order.** APAC-only count not disclosed. ⚠️ NOT FOUND — ASSUMED ≥100,000/month for APAC alone `[ASSUMPTION — not researched]`. Basis: Asia GMV €5.0bn per quarter, and Baemin Pay alone reported 600M+ cumulative transactions by Jan 2023 (search summary only). | See disclosure rule |
| Active Customers / Users | Baemin Pay 10M+ users (Jan 2023, search summary only); Baemin ~22.5M MAU (WiseApp, year unclear, search summary only) | [byline.network](https://byline.network/2023/01/9-127/) |
| Primary Currency | EUR (reporting); KRW, PKR, PHP, MYR, SGD, HKD, BDT, TWD in APAC | — |
| Top 3 Markets by Revenue | Not disclosed by country. Asia is the largest segment by GMV. Korea named as the growth driver in Q2 2026 (Korea quick-commerce GMV +39% YoY in constant currency) | Q2 2026 deck p.13 |
| Woowa Brothers (Baemin) | FY2025 revenue ₩5.28tn; operating profit ₩592.9bn (consolidated) | [Sidae](https://www.sidae.com/article/2026041015463564146) `[UNVERIFIED — search summary only]` |
| Billing channel split (web vs app store) | Not applicable: physical-goods delivery is outside app-store IAP. Orders are app-first, but payment runs through DH's own PSPs. | — |

---

### Overall Research Confidence

**Medium-High.**
- **Strong:** corporate status (Uber offer, Taiwan sale, Thailand exit, strategic review), read in DH's own IR decks and the Naspers release; group and Asia financials and order count from the decks; Adyen/PayPal config read in foodpanda.sg page source; Woowa's registration from the Baemin footer; the in-house orchestration job ad.
- **Weak:** foodpanda APMs and entity numbers. All help centres and T&Cs are bot-walled, so they rest on search summaries. The Korean card PG is not identified. The Fiserv acquiring claim and the wider PSP adapter bundle are not re-verified.
- **Traffic was supplied** (Similarweb Sales Intelligence, 2026-10-19), but it is **partial** (8 brand domains, no foodpanda HK, BD, KH, LA or MM, no deliveryhero.com) and **web-only** for an app-first business. Country shares are a market-mix signal only.

---

### Manual Research Recommendations

> **Area:** Account ownership and the Uber relationship (Phase 0, Insight #1)
> **Why it matters:** The acquirer is a Yuno customer and the payments decision-makers sit in Berlin. A cold APAC sequence could cut across an existing relationship.
> **Suggested manual action:** Before anything else, take this report to your manager and the Uber account owner. Agree whether DH is an EMEA, strategic or Uber-expansion account, and whether APAC has any role before the H2 2027 close.

> **Area:** Baemin's card PG and whether Baemin sits on DH's group platform (S3)
> **Why it matters:** If Baemin is a separate Korean stack, it is the only APAC piece with its own payments decision-maker (Choi Seong-gil, head of payment & settlement product).
> **Suggested manual action:** Check Woowa's tech blog (techblog.woowahan.com) for payments architecture posts, and look up Choi Seong-gil on LinkedIn.

> **Area:** Baemin foreign-card figures (S7)
> **Why it matters:** "3.7× foreign-method orders" is the strongest hook in the file, and it is search summary only.
> **Suggested manual action:** Open the ddaily 31 May 2026 article and confirm the figures and wording.

> **Area:** Grab–foodpanda Taiwan FTC decision (due 27 Oct 2026)
> **Why it matters:** Taiwan is DH's #3 APAC web market. If the deal is approved, it leaves the account.
> **Suggested manual action:** Check Focus Taiwan or the Taiwan FTC site after 27 Oct.

> **Area:** foodpanda checkout methods per market (S4)
> **Why it matters:** No help-centre page could be read, so all foodpanda APM rows are search summaries.
> **Suggested manual action:** Install the foodpanda app with a SG/MY/PH VPN and screenshot the payment-method list.

---

### Appendix: All Source URLs

**Traffic:** `accounts/traffic/delivery-hero.md`; `accounts/traffic/foodpanda.md` (Similarweb, supplied 2026-10-19)

**Phase 0 / Yuno:** https://y.uno/en · https://www.y.uno/en/success-stories/rappi

**Section 2:** https://www.baemin.com/ · https://www.sgpbusiness.com/company/Delivery-Hero-Singapore-Pte-Ltd · https://buy.experian.com.my/index.php/search/Malaysia-Company/989567/FOODPANDA-MALAYSIA-SDN.-BHD. · https://www.foodpanda.ph/contents/postpaid-terms-and-conditions · https://www.foodpanda.pk/contents/terms-and-conditions.htm · https://www.foodpanda.pk/contents/pandapay-user-account-terms-and-conditions · https://finance.technews.tw/2026/07/22/fair-trade-commission-20260722/ · https://www.naspers.com/news-insights/regulatory-updates/2026/prosus-gives-irrevocable-undertaking-to-sell-residual-stake-in-delivery-hero-to-uber

**Section 3:** https://www.foodpanda.sg/contents/privacy.htm · https://www.foodpanda.sg/ · https://www.adyen.com/en_GB/press-and-media/adyen-acquiring-malaysia · https://www.adyen.com/zh_CN/knowledge-hub/delivery-hero-tucks-into-risk-management · https://technode.global/2024/07/25/foodpanda-partners-visa-solution-cybersource-to-enhance-customer-checkout-experience-in-apac · https://newsroom.fiserv.com/node/49896/pdf · https://www.checkout.com/case-studies/how-localized-payments-is-driving-delivery-hero-s-global-expansion · https://www.businesswire.com/news/home/20230131005758/en/ · https://www.business.hsbc.com.hk/en-gb/insights/optimising-sales/foodpanda-reduces-cash-on-delivery-with-payme · https://www.gbm.hsbc.com/en-gb/feed/innovation/driving-foodpandas-growth-through-payment-apis · https://careers.deliveryhero.com/job/product-manager-payments-fintech-in-berlin-germany-jid-9819 · https://careers.deliveryhero.com/job/group-product-manager-fintech-global-payment-in-berlin-germany-jid-3366 · https://fintech.global/2022/03/17/payment-operating-system-payrails-launches-from-stealth/ · https://byline.network/2023/01/9-127/

**Section 4:** https://news.mtn.co.kr/news-detail/2026082709564142678 · https://www.ddaily.co.kr/page/view/2026052015503597830 · https://www.ddaily.co.kr/page/view/2026053108445282961 · https://biz.sbs.co.kr/amp/article/20000337807 · https://www.namu.moe/w/N%20Pay · https://news.mtn.co.kr/news-detail/2022033111405668188 · https://brunch.co.kr/@coygray/607 · https://en.dailypakistan.com.pk/14-Nov-2024/why-paying-online-is-the-smart-choice · https://www.foodpanda.pk/contents/pandapay-5 · https://technews.tw/?p=1406384 · https://www.expat.com/en/forum/asia/philippines/1095378-food-delivery-and-apps-in-the-philippines.html · https://newsbytes.ph/2026/05/16/foodpanda-adds-qrph-payments-for-cash-on-delivery-orders/ · https://newsbytes.ph/2023/09/20/pinoys-split-between-cashless-cash-payments-report/ · https://context.ph/2025/11/27/foodpanda-pushes-filipinos-toward-cashless-payments-with-new-co-branded-credit-card/ · https://www.thesundaily.my/business/you-can-now-pay-for-foodpanda-deliveries-with-touch-n-go-ewallet-LD10648344 · https://honeykidsasia.com/food-delivery-apps-in-singapore/ · https://www.octopus.com.hk/en/consumer/latest-promotions/food-panda.html · https://www.bkash.com/en/campaign/foodpanda-new-user · https://unb.com.bd/category/Business/foodpanda-launches-pandapro-subscription-in-bangladesh/98022

**Section 5:** https://ie.trustpilot.com/review/www.foodpanda.sg · https://fr.trustpilot.com/review/foodpanda.pk · https://lowyat.net/2021/241620/foodpanda-payment-system-currently-facing-issues-cod-as-only-available-option · https://techenclave.com/threads/foodpanda-app-failed-payment-issue.174031/ · https://biz.sbs.co.kr/amp/article/20000232915

**Sections 6–7:** https://ir.deliveryhero.com/media/document/7c8c8b86-f69c-4699-a75e-dc2946cb22e0/assets/Delivery_Hero_Q2_2026_Trading_Update.pdf?disposition=inline · https://ir.deliveryhero.com/media/document/9e289f1f-e210-4e7d-bc0e-77c3f86814ee/assets/Delivery_Hero_FY_2025_Results.pdf?disposition=inline · https://tech.eu/2026/07/16/uber-to-acquire-delivery-hero-in-13b-deal-creating-platform-spanning-99-countries/ · https://focustaiwan.tw/business/202607220014 · https://www.koreaherald.com/article/10738059 · https://mbiz.heraldcorp.com/article/10814779 · https://www.malaymail.com/news/money/2026/03/23/singapores-grab-snaps-up-foodpanda-taiwan-in-us600m-deal-with-delivery-hero/213612 · https://www.sec.gov/Archives/edgar/data/1855612/000185561226000051/foodpandtaiwan-finalannoun.htm · https://techcrunch.com/2025/03/11/uber-terminates-foodpanda-taiwan-acquisition-citing-regulatory-hurdles · https://asiaiplaw.com/article/deliveroo-sells-assets-to-rival-foodpanda-before-hong-kong-exit · https://www.hiretechladies.com/jobs/principal-global-payments-commercial-partnerships-delivery-hero-6u · https://careers.deliveryhero.com/job/senior-product-manager-in-singapore-jid-10799 · https://www.hankyung.com/article/202512056610i · https://view.asiae.co.kr/article/2026053113285274214

**Section 9:** https://arabianreseller.com/2022/01/24/talabat-achieves-highest-level-of-pci-dss-certification-for-transactional-security/

**Section 11:** https://www.adyen.com/press-and-media/grab-selects-adyen-as-payment-solution-partner-for-four-markets-in-southeast-asia · https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm · https://www.kedglobal.com/newsView/ked202503240003 · https://www.koreajoongangdaily.com/business/yogiyo-drops-commission-fee-to-97-percent-undercutting-baemin-and-coupang-eats/12313641 · https://techbuzzchina.substack.com/p/keeta-meituans-overseas-expansion · https://www.uber.com/blog/moneycon · https://www.dealstreetasia.com/?p=470756 · https://fintechnews.sg/fintech-startups-thailand/fintech/line-pay/ · https://hyperswitch.io/case-studies/swiggy/ · https://juspay.io/customer-stories/zepto · https://ir.doordash.com/news/news-details/2021/DoorDash-Joins-Forces-with-Wolt/default.aspx

**Section 12:** https://www.sidae.com/article/2026041015463564146

</details>
