# Grab

**Status:** 🔴 Not ICP — Phase 0 payment-infrastructure gate fired (licensed acquirer). **Route to Partnerships, not SDR outreach.**
**ICP Score:** 17 / 29 → ⭐ High Priority **on arithmetic** — **ANALYST OVERRIDE applied, tier set DOWN to 🟢 Medium.** See "ICP Score breakdown" for the full reasoning and for the alternative 19/29 reading.
**Industry:** Super Apps & On-Demand Delivery — deliveries, mobility and digital financial services across eight Southeast Asian markets · **HQ:** Singapore — principal executive office **3 Media Close, #01-03/06, Singapore 138498**; registrant **Grab Holdings Limited**, incorporated in the **Cayman Islands** (NASDAQ: GRAB / GRABW, SEC Commission File 001-41110) · **Researched:** 2026-10-13 · **First email sent:** —
**Motion:** **IN-HOUSE** — confirmed from Grab's own 20-F: **GrabLink** is *"our in-house PCI-compliant secure payment gateway and acquiring service licensed under the Payments Services Act of Singapore aimed at reducing dependency on third-party providers."* Respect the build. Anchor on **reach and opportunity cost**. **Never argue they need orchestration** — they are the most orchestration-literate prospect in this repo.
**⭐ PITCH SPINE (if this account is worked at all):** Grab did not build a gateway to replace acquirers — it built one to stop paying for them. Its own 20-F still says it *"will likely continue to rely on"* **Adyen and Stripe** to process and remit payments. So the question is never "do you need orchestration" — it is **"which markets and rails can your layer not reach, and what is that costing you in Taiwan?"** See **Insight #1** and **Insight #2**.
**⛔ DO NOT pitch a routing layer, a decline cascade or a failover story as if it were new to them.** They run `PAYMENT_RECOMMENDATION` logic in their own PaySDK. Lead on **coverage**, not on **mechanism**.

---

> # 🔒 PHASE 0 — THE EXCLUDED-INDUSTRY GATE. READ FIRST.
>
> ### My verdict: **THE GATE FIRES.** On the letter of `CLAUDE.md`, Grab is a payment-infrastructure company and the primary route is **Partnerships**, not SDR outreach.
>
> Prateek raised this before the run and chose **"full research anyway" on 2026-10-13**. The full method was run. This is the finding, on the record, with sources.
>
> `CLAUDE.md` excludes *"PSPs and payment infrastructure companies"*. The `/research` Phase 0 table auto-rejects a *"company [that] is a PSP, gateway, acquirer or orchestrator"*. Grab is **all four of those things in at least one market**, by its own disclosure:
>
> | # | What Grab says about itself | Where |
> |---|---|---|
> | 1 | **"GrabLink, our in-house PCI-compliant secure payment gateway and acquiring service licensed under the Payments Services Act of Singapore** aimed at reducing dependency on third-party providers, and helps us reduce our cost of funds across Grab transactions." | [20-F FY2025, Item 4.B](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm) |
> | 2 | The Singapore PS Act 2019 licences *"e-money issuance, domestic or cross-border money transfer, **merchant acquisition service** and digital payment token services"*, and Grab is twice described as *"**a major payment institution such as Grab**"* | same 20-F, Regulatory Environment — Singapore |
> | 3 | In the Philippines, *"Operators of Payment Systems ('OPS'), **which includes GrabPay and GrabLink**, [must] register with the BSP"*, and *"the Regulatory Framework for Merchant Payment Acceptance Activities ... requires an OPS engaging in **merchant acquisition** to obtain a **Merchant Acquisition License** from the BSP"* | same 20-F, Regulatory Environment — Philippines |
> | 4 | *"Merchant-partners that have entered into contractual agreements with Grab **pay us a commission fee, based on transaction volumes**, to support the GrabPay e-wallet services we provide or facilitate for merchant-partners and consumers."* | same 20-F, Revenue |
> | 5 | Grab **sells acceptance to third-party merchants** on its own website: *"Accept GrabPay or PayLater at your Online Store ... Tap on our **pre-built integrations** with e-commerce shop builders such as **Shopify, WooCommerce, Magento, EasyStore ... Wix**, payment partners or **via our Direct API** ... **next-day settlement** ... **Tokenisation** allows for seamless repeat purchases and subscription payments ... Easily issue **refunds** at any time via the GrabMerchant app and portal"* | [grab.com/sg/merchant/checkout-solutions](https://www.grab.com/sg/merchant/checkout-solutions/) · [grab.com/my/merchant/checkout-solutions](https://www.grab.com/my/merchant/checkout-solutions/) |
> | 6 | Grab is **distributed as a payment method by PSPs**, including two of Yuno's own connector set. Named "Key Partners" logo carousel on the SG page: **Adyen** (`ayden-logo.png`), **2C2P**, **Stripe**, **FOMO Pay**, **Liquid Pay**, + one unidentified (`uniweblogosvg.svg`). On the MY page (assets uploaded Dec 2025): **2C2P, ADAPTIS by NTT DATA, Adyen, Fiuu, Revenue Harvest, Revenue Monster, senangPay** | same two pages (logo filenames; see Source Notes for the identification caveat) |
> | 7 | *"As the first fintech platform with access to **e-money licenses in the major six economies in ASEAN**, Grab Financial has built the largest merchant network, covering **more than 600,000 merchants** ... 'Pay with GrabPay' agreements have also been signed with some of the region's biggest **merchant gateways, including Adyen**."* ⚠️ dated **18 Sep 2019** — old, directionally confirmed by items 1–6 | [Adyen Knowledge Hub](https://www.adyen.com/en_SG/knowledge-hub/grabpay-enabling-smoother-payments-in-southeast-asia) |
> | 8 | Grab is **currently hiring** an **"Off-Platform Payment Operations Manager"** and a **"Commercial Strategy Lead, PayLater Lending & OmniCommerce"** — off-platform payment operations is, by name, acceptance outside Grab's own app | [grab.careers job search "payments", fetched 2026-10-13](https://www.grab.careers/en/jobs/?search=payments) |
>
> ### The one qualification that keeps this from being a clean rejection
>
> **Grab is genuinely dual-natured, and the merchant half is large and real.** GrabLink is described as serving *"**Grab** transactions"* and reducing *"**our** cost of funds"* — i.e. **captive** acquiring, built for its own volume, not a service sold to the open market. And Grab remains a **buyer** of third-party acquiring at group level: *"We rely on strategic partnerships with financial institutions such as Visa and Mastercard and third parties such as **Adyen and Stripe** to process and remit payments to and from consumers and driver- and merchant-partners. Although we may develop in-house payment processing capabilities, **we will likely continue to rely on these strategic partnerships and third-party services**."* ([20-F risk factors](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm)) That is a merchant sentence, not an infrastructure sentence — and it sits behind **$22.1bn of FY2025 on-demand GMV**.
>
> ### What I recommend, stated plainly so the decision is on the record either way
>
> 1. **Primary route: Partnerships.** GrabPay and PayLater are **payment methods** Yuno would want to *connect*, in five to six ASEAN markets, already distributed through Adyen, Stripe and 2C2P. That is a connector conversation, not an SDR conversation. This is also the only route that is not conflicted.
> 2. **Secondary, and only with Partnerships' knowledge: the merchant side.** The acceptance Grab *buys* for its own $22.1bn GMV is in ICP on volume and footprint. The entry point is **Taiwan** (Insight #2), not routing.
> 3. **Do not run a cold 12-touch sequence on this account without that alignment.** Pitching orchestration to a company that holds a gateway-and-acquiring licence reads as not having read their 20-F, and it is the single fastest way to burn an enterprise thread.
>
> ### ✅ Grab is NOT an existing Yuno customer
> Verified live 2026-10-13: `https://y.uno/en` returns **zero** occurrences of the string "grab", and Grab appears nowhere in the site-wide customer logo set actually served on that page (`antgroup, carrefour, copaairlines, despegar, garena, gofundme, hotmart, indrive, kavak, livelo, mcdonalds, moonactive, netease, rappi, reserva, tada, uber, vivaaerobus, whop, wingo`). Same evidentiary standard the repo used to clear TADA. The existing-customer gate does **not** fire.

---

> # ⚠️ METHOD DEVIATIONS AND DATA GAPS — disclosed up front
>
> ### 1. 🚨 NO TRAFFIC DATA WAS SUPPLIED, AND NONE WAS OBTAINED
> Prateek stated explicitly that there is none for Grab. `accounts/traffic/grab.md` does not exist. **No SimilarWeb data of any kind underpins this report.** Per the skill's own rule:
> - **Section 1 (Website Traffic Analysis) cannot be completed.** No traffic split is given. None is invented.
> - **Two ICP signals are unverifiable and therefore score 0:** *"High traffic outside home"* and the traffic-weighted ranking used by *"local rail or licensing gap in a top-3 market"*. Both are marked ⬜ with the reason stated.
> - A `site:similarweb.com` fallback was available and was **deliberately not spent** — see §2.
>
> ### 2. ⭐ BUT THE COUNTRY PROFILE IS NOT ESTIMATE-GRADE — IT IS AUDITED
> This is the one place where this report is **better** off than a traffic-fed one. Grab is NASDAQ-listed and files a **20-F with an IFRS 8 geographic-information note**, so there is an **audited revenue-by-country split** for FY2025. That beats any SimilarWeb estimate for this account, and it is what Section 1-ALT uses. Web traffic would have been a poor proxy anyway: Grab is app-first (**100M+ Google Play downloads**, 8 markets, 900+ cities) and its web surfaces (`food.grab.com`, `book.grab.com`, `express.grab.com`) are a small minority of volume.
>
> ### 3. ⛔ No subagents — single-threaded execution
> The Agent/Task tool was **not available** in this run. Phases 1 → 2 → 3 were executed **sequentially by one analyst**. The five per-agent search/fetch budgets were treated as one pooled budget per workstream. Nothing in the method was skipped, but the independent cross-checking that normally comes from five parallel agents was replaced by one pass plus a deliberate control-test discipline on every negative result (see §5).
>
> ### 4. WebFetch vs curl
> WebFetch was not used. All fetching was done with Bash `curl -sS -L --compressed`, confirmed working. `--compressed` was mandatory throughout.
>
> ### 5. Every zero in this report was control-tested. Four traps fired.
> | Trap | What happened |
> |---|---|
> | **Lost working directory** | A first pass converted the 4.1 MB 20-F to text, then the file **vanished from the scratch directory** before the greps ran — every vendor grep returned **0**. Caught only because a `grep -c "Singapore"` control also returned 0 on a 20-F. Re-fetched into a fresh directory; real counts then appeared. **A zero against a missing file looks exactly like a finding.** |
> | **Font Awesome / Ant Design icon sets** | `developer.grab.com`'s 6.5 MB bundle returned hits for Stripe, Adyen, Alipay, 3DS and "acquir". **Every one was an icon definition or Chart.js**: `faCcStripe`, `faStripe`, `faStripeS`, `faAlipay`, `AlipayCircleFill`, `acquireContext`. The developer portal is a client-rendered shell with **no payment-vendor content at all**. Discarded entirely. |
> | **Soft-404s** | `help.grab.com/passenger/en-{sg,id,th,ph,vn,my,kh}/` all return **HTTP 200 at exactly 1,316 bytes** — and so does `help.grab.com/passenger/nonsense-zzz/`. Byte-identical SPA shell. **A 200 is not a page.** The help centre was abandoned as a source. By contrast `www.grab.com` serves honest 404s (32.7–32.8 KB) distinguishable from real pages (37–40 KB), so the per-country probe results there are trustworthy. |
> | **False positives in the production bundle** | In `food.grab.com`'s 4.8 MB bundle: `omise` → `Promise` (5 hits, zero real); `Wing` → 0 case-sensitive (60 case-insensitive hits were all `following`); `ABA` → the base64 of a 1×1 transparent GIF; `WeChat` → a `ua-parser` browser-detection regex; `Alipay` → Ant Design icons; `Maya`/`MoMo`/`Yuno` → zero in context. **All checked both ways.** |
>
> ### 6. Fetches that failed
> `investors.grab.com` (403), `trustpilot.com/review/grab.com` (403), `grab.careers` individual job pages (403), SEC EDGAR directory and `-index.htm` listings (403 — worked around via the EDGAR full-text-search API), `eservices.mas.gov.sg` Financial Institutions Directory (SPA + blocked). **The MAS FID failure matters:** it is the one source that would enumerate exactly which PS Act licence classes **GPay Network (S) Pte Ltd** holds. It is in Manual Research Recommendations.
>
> ### 7. No credential, key, token or merchant ID appears anywhere in this report
> None was encountered. A CSP `style-src` nonce was seen on `paysuite.grab.com` and `paysuite.moca.vn`; **values deliberately not recorded** (they are per-response anyway).

---

---

> ## 🔍 ANALYST AUDIT — Prateek, 2026-10-13
>
> **The Phase 0 verdict is correct and I have verified it against the primary source myself. Grab is a licensed acquirer. The gate fires.**
>
> ### ✅ VERIFIED VERBATIM from Grab's own audited FY2025 Form 20-F
> I fetched the filing directly from SEC EDGAR (4.19 MB, controls passing: `Singapore` 117, `Grab` 310, `Deliveries` 119) and confirmed all three decisive passages:
>
> 1. > *"**GrabLink, our in-house PCI-compliant secure payment gateway and acquiring service licensed under the Payments Services Act of Singapore** aimed at reducing dependency on third-party providers, and helps us reduce our cost of funds across Grab transactions."*
> 2. > *"We rely on strategic partnerships with financial institutions such as Visa and Mastercard and third parties such as **Adyen and Stripe** to process and remit payments to and from consumers and driver- and merchant-partners. Although we may develop in-house payment processing capabilities, **we will likely continue to rely on these** strategic partnerships and third-party services."*
> 3. > *"…the mandatory safeguarding of customer monies (for a **major payment institution such as Grab**), the requirement to furnish security (for a major payment institution such as Grab)…"* — under a PS Act whose regulated services expressly include **"merchant acquisition service"**.
>
> **That is a company operating a licensed payment gateway and acquiring service.** `CLAUDE.md` excludes *"PSPs and payment infrastructure companies"* and the Phase 0 table auto-rejects *"a PSP, gateway, acquirer or orchestrator"*. **It fires, on Grab's own words in an audited filing.** `/prepare_batch`'s hard rule then applies: record as not-ICP with the gate reason and **do not run outreach**.
> **Also confirmed: `Taiwan` appears ZERO times in the FY2025 20-F**, so the TAL's `+ TW (2026)` is wrong as written. The acquisition is agreed and unclosed.
>
> ### 📌 This is a ROUTING decision, not a quality judgement — and it is reversible
> Prateek raised the Phase 0 question before this run and chose "full research anyway". **The research has now answered the question he authorised asking, and the answer routes the account.** The work is not wasted: the intelligence below is exactly what Partnerships needs, and it is preserved in full. **If Prateek disagrees with the routing, moving this back is a one-line change** — the file, the score and the evidence all stand either way.
>
> ### ⭐ Why this is a genuinely valuable Partnerships lead, not a dead account
> Grab built GrabLink to stop *paying* third parties, but **by its own filing it remains a buyer**: Adyen and Stripe sit behind **$22.1bn of FY2025 GMV**, and Grab says it *"will likely continue to rely on"* them. **The prize is real; the door is wrong.** GrabPay and PayLater as Yuno connectors is the Partnerships motion. Any merchant-side conversation should happen only with Partnerships' knowledge, and **no cold 12-touch sequence** until that is resolved — naming an orchestration pitch to a licensed acquirer is the fastest way to lose the thread.
>
> ### 🚩 What carried the arithmetic, had it mattered
> 17/29, re-added by hand: **5+1+3+3+0+2+0+0+0+2+1 = 17 across 11 rows** ✅. Three rows carried 11 of the 17: volume **+5** (✅ genuinely SOURCED as a floor — Q2'26 Group MTUs 53.9m against the 20-F's own MTU definition, with an assumption-free cross-check), 3+ countries **+3** (audited revenue in six countries each >7%), multiple PSPs **+3** (Adyen and Stripe, verified above). The run **refused four rows** it could have stretched, and flagged rather than took an alternative 19/29 reading using audited revenue-by-geography in place of traffic share. That restraint is the right instinct.
>
> ### ⚠️ Carried forward for Partnerships
> - **Which acquirer covers which market is not disclosed anywhere** — the highest-value open question on the account.
> - **Which MAS PS Act licence classes GPay Network (S) Pte Ltd holds** was not obtainable (MAS FI Directory is an unreachable SPA). That is what would make this verdict airtight rather than strongly evidenced — though the 20-F language alone is sufficient for the routing call.
> - **GrabPay third-party-merchant TPV is never disclosed**, and it sizes the Partnerships opportunity.
> - ✅ **Not an existing Yuno customer** — `y.uno/en` fetched live returns zero occurrences of "grab".
>
> ### ✔️ Safety
> No credential anywhere. No booking link. The nine banned competitor names appear once in total, inside an internal zero-occurrence check. Structure 3/3.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Grab is Southeast Asia's leading superapp, operating **deliveries, mobility and digital financial services in over 900 cities across eight countries — Cambodia, Indonesia, Malaysia, Myanmar, the Philippines, Singapore, Thailand and Vietnam**. FY2025 revenue was **$3,370m** on **$22,138m of on-demand GMV**; Q2 2026 revenue was **$997m (+22% YoY)** on **$6,463m of quarterly on-demand GMV**, with a record **53.9m Group Monthly Transacting Users**. It owns **GrabPay** (e-money wallet, SG/MY/PH/TH and Indonesia via **OVO**), **GrabLink** (a licensed in-house payment gateway and acquiring service), **PayLater** (BNPL/instalments), and digital banks **GXS Bank** (SG), **GXBank** (MY) and **Superbank** (ID, consolidated from June 2026). It is **NASDAQ-listed (GRAB)** and profitable. [Q2 2026 press release](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000123/a2026q2-earningspressrelea.htm) · [20-F FY2025](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm)

**SimilarWeb total visits (last full month):** ❌ **NOT AVAILABLE — no traffic data supplied, none obtained.** See the methods box. App-first business; web traffic would be a poor volume proxy regardless.

### Top 5 markets — ✅ **AUDITED, not estimated** (FY2025 revenue by geography, 20-F IFRS 8 note)
> ⚠️ **This is a revenue ranking, not a traffic ranking.** It is the audited geographic-information note in Grab's own 20-F, which is a *better* source than traffic for this account — but it is not interchangeable with traffic share for ICP scoring, and it has one distortion flagged below the table. "Missing methods" are **absences in Grab's own web checkout method catalogue only** — see the hard caveat under Section 4.

| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | **Malaysia** — **$1,039m**, 30.8% of FY2025 revenue, **+27% YoY** | ❌ No traffic data | Cash · Card (**Visa / Mastercard only** on web) · GrabPay · PayLater (4 / 8 / 12 instalments) · GrabPay **DuitNow QR** *(acceptance side — Grab as the acquirer, not as the payer)* | 🚩 **FPX** · 🚩 **DuitNow** as a pay-in rail · 🚩 **Touch 'n Go eWallet** · 🚩 Boost — **none found in the web method catalogue** | ✅ Multiple. Grab was **first incorporated in July 2011 as MyTeksi Sdn. Bhd., a Malaysian private limited company**. **GrabFin Operations (Malaysia) Sdn. Bhd.** (licensed money lender); **GX Bank Berhad** (BNM-licensed digital bank); Jaya Grocer and Everrise retail. **BNM-approved e-money issuer** — *"Approved e-money issuers, such as us"* |
| 2 | **Singapore** (home) — **$727m**, 21.6%, **+26% YoY** | ❌ No traffic data | Cash · Card (**Visa / Mastercard only** on web) · **GrabPay Credits** · PayLater (postpaid + instalments) · `postpaidBilling` · GrabPay **Web3 Wallet** (digital tokens) | 🚩 **PayNow** · 🚩 NETS — **not found in the web method catalogue** | ✅ **GrabTaxi Holdings Pte. Ltd. — Company No. 201316157E** · **GPay Network (S) Pte Ltd** ("GPNS") · **GFin Services (S) Pte. Ltd.** (BNPL) · **GXS Bank Pte. Ltd.** · **major payment institution** under the MAS PS Act 2019 |
| 3 | **Indonesia** — **$715m**, 21.2%, **+11% YoY** | ❌ No traffic data | Cash · Card (**Visa / Mastercard only** on web) · **OVO** (the market wallet — Grab's own: `{ID:"OVO"}`) · **OVO Points** · **OVOPayLater** | 🚩 **QRIS** · 🚩 bank transfer / virtual account · 🚩 GoPay · 🚩 DANA · 🚩 ShopeePay · 🚩 Alfamart / Indomaret cash — **none found in the web method catalogue** | ✅ **PT Visionet Internasional** (OVO), a subsidiary of **PT Bumi Cakrawala Perkasa** ("BCP") · **PT Indonusa Bara Sejahtera** t/a OVO Finansial (P2P lending) · **PT Super Bank Indonesia Tbk** (IDX: SUPA, >50% from June 2026). ⚠️ **OVO is subject to an 85% foreign-investment limit and a 49% foreign voting-power cap** under Bank Indonesia payment-system regulation |
| 4 | **Philippines** — **$316m**, 9.4%, **+19% YoY** | ❌ No traffic data | Cash · Card (**Visa / Mastercard only** on web) · GrabPay · PayLater | 🚩 **GCash** · 🚩 **Maya** · 🚩 InstaPay / PESONet · 🚩 OTC cash — **none found in the web method catalogue** | ✅ **Grab PH Holdings**. GrabPay is a **BSP-approved Electronic Money Issuer**; **GrabPay and GrabLink are both registered Operators of Payment Systems with the BSP** |
| 5 | **Thailand** — **$288m**, 8.5%, **+14% YoY** | ❌ No traffic data | Cash · Card (**Visa / Mastercard only** on web) · GrabPay Wallet · PayLater · **credit/debit card payment processing for Dine Out** | 🚩 **PromptPay** · 🚩 **TrueMoney** · 🚩 card instalment plans · 🚩 JCB — **none found in the web method catalogue** | ✅ Licensed under the **Payment Systems Act B.E. 2560 (2017)**; licence from the Ministry of Finance via the **Bank of Thailand**, covering *"GrabPay Wallet and processing credit/debit card payment for Dine Out service"*. Currently hiring a **"Head, Payment and Insurance — Thailand"** |
| 6 | **Vietnam** — **$255m**, 7.6%, **+12% YoY** | ❌ No traffic data | Cash · Card (**Visa / Mastercard only** on web) · **Moca** — the market wallet (`{VN:"Moca"}`), served from **`paysuite.moca.vn`**, a live Grab PaySuite host on a Vietnamese domain | 🚩 **MoMo** · 🚩 **ZaloPay** · 🚩 **VNPay / VietQR** · 🚩 **NAPAS** domestic cards — **none found in the web method catalogue**. GrabPay itself is **not listed for Vietnam** in the 20-F | ⚠️ **No Vietnamese entity name found in any first-party document.** The Moca relationship is evidenced only by Grab's own production assets (CSP + JS constant), not by the filing — **"Moca" appears zero times in the 20-F**. ⚠️ Vietnam gates intermediary payment services (e-wallet and gateway) behind an **SBV licence** under Decree 52/2024/ND-CP with minimum charter capital |
| 7 | **Rest of SEA** (Cambodia + Myanmar) — **$30m**, 0.9%, **+100% YoY** | ❌ No traffic data | Not found in any first-party asset | 🚩 **Bakong / KHQR** (KH) · 🚩 ABA / Wing / Pi Pay (KH) — not found | ⚠️ Not found. Grab operates in both per the 20-F; no KH or MM entity identified |

**Revenue shares computed from the 20-F's own figures: 1,039 + 727 + 715 + 316 + 288 + 255 + 30 = 3,370 ✓.** [20-F FY2025, Note 19(ii) Geographic information and Item 5.A](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm)

> ⚠️ **ONE DISTORTION, FLAG IT BEFORE USING THE RANKING.** Malaysia outranks Indonesia on revenue largely because Grab **owns grocery retail there** — Jaya Grocer and Everrise — and recognises **grocery retail revenue gross**, not as a net commission. Grab's own Q2 2026 release attributes rising cost of revenue *"mainly from the expansion of Jaya and Everrise stores"*. **Malaysia's #1 revenue rank almost certainly overstates its share of payment volume.** Do not say "Malaysia is your biggest market" in outreach without that caveat.

> 🚩 **TAL CORRECTIONS — three.**
> 1. `Operating Countries = "SG/MY/ID/PH/VN/TH/KH/MM + TW (2026)"`. The **eight** SEA markets are **confirmed verbatim** in the 20-F and in the Q2 2026 release. **Taiwan is NOT yet a Grab market.** "Taiwan" appears **zero times** in the FY2025 20-F. Grab has an **agreed but unclosed** acquisition — see the next line. Corrected value: **SG/MY/ID/PH/VN/TH/KH/MM; TW agreed, not closed**.
> 2. `Est. Revenue = "$955M Q1'26 (+24% YoY); FY26 guide ~$4.05B"`. The Q1 figure is **✅ exactly right** ($955m, +24%). The guidance is **superseded**: raised at Q2 to **$4.10bn–$4.15bn** (previous $4.04bn–$4.10bn), with Adjusted EBITDA guidance **$720m–$740m**.
> 3. `Payment Gateway = "In-house GrabPay stack + external acquiring partners"` and `Payment Orchestrator = "In-house Routing"`. **Both independently confirmed** — and this time the TAL is right. See Section 3B. The named external acquirers are **Adyen and Stripe**, which the TAL only gestured at.

### Legal entities
- **Grab Holdings Limited** — **Cayman Islands**; principal executive office 3 Media Close, #01-03/06, Singapore 138498; NASDAQ **GRAB** / **GRABW**; SEC Commission File **001-41110**; CIK **0001855612**. [20-F cover page](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm)
- **GrabTaxi Holdings Pte. Ltd.** (Singapore) — **Company No. 201316157E**. Incorporated **June 2013** as the then-ultimate parent; still the employer of record for executive officers, the **iOS App Store provider** (`GRABTAXI HOLDINGS PTE. LTD.`) and the licensor behind the consumer apps. [20-F Item 4.A](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm) · [Web3 Wallet terms](https://www.grab.com/sg/terms-policies/web3-wallet) · [App Store](https://apps.apple.com/sg/app/grab-app/id647268330)
- **GPay Network (S) Pte Ltd** ("**GPNS**") (Singapore) — ⭐ **the payments operating entity.** Named in Grab's own PayLater terms as the party that auto-purchases GrabPay Credits, auto-deducts, and acts as *"disbursement agent"* and *"collection agent"*. This is the entity whose MAS licence classes matter most and the one the MAS directory would resolve. [PayLater terms](https://www.grab.com/sg/terms-policies/paylater)
- **GFin Services (S) Pte. Ltd.** (Singapore) — the BNPL contracting entity. *"BNPL services are not regulated by the Monetary Authority of Singapore (MAS). The Company is a BNPL Provider as defined under the Singapore BNPL Code of Conduct and **is in the process of obtaining accreditation** under the BNPL Code of Conduct."* [PayLater terms](https://www.grab.com/sg/terms-policies/paylater)
- **Grab Holdings Inc.** ("GHI") — Cayman Islands exempted company. **AA Holdings Inc.** ("GFG") — Cayman Islands, holding company for the financial services businesses including the Digital Banking JV. [20-F definitions](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm)
- **GXS Bank Pte. Ltd.** (Singapore, MAS digital bank, JV with Singtel) · **GX Bank Berhad** (Malaysia, BNM-licensed, foundational phase) · **PT Super Bank Indonesia Tbk** (IDX: **SUPA**, consolidated from June 2026)
- **PT Visionet Internasional** ("OVO") (Indonesia) — subsidiary of **PT Bumi Cakrawala Perkasa** ("BCP"); *"our payment system services business is conducted through"* BCP. **PT Indonusa Bara Sejahtera** t/a **OVO Finansial** — P2P lending.
- **GrabFin Operations (Malaysia) Sdn. Bhd.** — licensed money lender, 40% acquired via **Grab Financial Services Asia Inc.** ("GFSA"). **Grab PH Holdings** (Philippines).
- **Eastern Grocer Sdn. Bhd. ("Everrise")** — 80% acquired 3 Mar 2025 (Malaysia). **Jaya Grocer** (Malaysia). **Validus Capital** (SG SME lending, via GXS Bank). **Infermove** (China, AI robotics).
- **Stash Financial, Inc.** (United States) — 100% acquired, closing **1 July 2026**. Out of APAC territory.
- **Neuroncredit Pte. Ltd. ("Atome Financial")** — **60% pending** for $1.49bn, expected to complete by Q3 **2027**.
- **"Moca" (Vietnam)** — `[INFERENCE, not confirmed]` as a legal entity. Evidenced only as a **live production host** (`paysuite.moca.vn`, HTTP 200, serving Grab's PaySuite CSP) and as Grab's own per-market wallet constant `{VN:"Moca"}`. **No corporate name or registration number found. "Moca" appears zero times in the 20-F.**
- **Registration numbers:** only **201316157E** (GrabTaxi Holdings Pte. Ltd.) was obtained. ACRA/BizFile, Malaysian SSM, Indonesian AHU and Vietnamese registry pages were **not reached in this environment**. Not found ≠ does not exist.

### Known PSPs
- **Adyen** — ⭐ **CONFIRMED by Grab's own 20-F**, in two distinct roles: (a) a **third party Grab relies on "to process and remit payments to and from consumers and driver- and merchant-partners"**; and (b) a **distribution partner for GrabPay acceptance** (named in both the SG and MY merchant "Key Partners" carousels, and in Adyen's own 2019 interview with Grab Financial Group). `[Third-Party Report / Terms]` + `[Provider Case Study]` [20-F](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm) · [Adyen](https://www.adyen.com/en_SG/knowledge-hub/grabpay-enabling-smoother-payments-in-southeast-asia)
- **Stripe** — ⭐ **CONFIRMED by the same 20-F sentence**, same role. Also on the SG merchant Key Partners carousel. **Market coverage per acquirer is NOT disclosed anywhere** — see Manual Research.
- **Visa** and **Mastercard** — named in the same sentence as *"strategic partnerships with financial institutions"*. These are the **only two card brands** in the GrabFood web method catalogue (`[Visa,"MasterCard"]`); no Amex, JCB or UnionPay found anywhere.
- **GrabLink** — ⭐ **Grab's own licensed gateway and acquiring service.** Not a vendor; the in-house alternative to one. SG-licensed under the PS Act; BSP-registered OPS in PH.
- **An unnamed single "third-party payment processor"** — the 20-F contains a reimbursement obligation in the singular: *"We have also agreed to reimburse **our third-party payment processor** for any reversals, chargebacks, and fines assessed due to rule violations."* Which of Adyen or Stripe (or neither) this refers to is **not stated**. `[Terms/20-F]`
- **Distribution-side PSPs for GrabPay acceptance** (these acquire *for third-party merchants accepting GrabPay*, not for Grab): **2C2P**, **FOMO Pay**, **Liquid Pay** (SG); **2C2P**, **ADAPTIS by NTT DATA**, **Adyen**, **Fiuu**, **Revenue Harvest**, **Revenue Monster**, **senangPay** (MY). Identified from logo filenames on Grab's own pages — see Source Notes for the caveat.
- **❌ NOT FOUND anywhere:** Checkout.com, Worldpay, Braintree, PayPal, Xendit, Midtrans, Doku, iPay88, Omise, Razorpay, PayU, Cashfree, GMO, SB Payment, KOMOJU, Toss Payments, NICEPAY, eWAY, Windcave, Tyro.

### Orchestration status
**IN-HOUSE ORCHESTRATION LAYER — confirmed three independent ways.** This is not an unchecked TAL cell.

1. **By Grab's own words:** *"**GrabLink**, our in-house PCI-compliant secure payment gateway and acquiring service licensed under the Payments Services Act of Singapore aimed at **reducing dependency on third-party providers**, and helps us **reduce our cost of funds** across Grab transactions."* [20-F](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm)
2. **By live CSP headers — a real asset map, with no `strict-dynamic` to invalidate the negative.** `paysuite.grab.com` and `paysuite.moca.vn` both serve `script-src 'self' https://www.googletagmanager.com https://www.google.com https://www.gstatic.com https://scribe-web-sdk.{stg-myteksi,grab}.com https://mcd-gateway.grabtaxi.com` — **not one third-party PSP script host**. `merchant.grab.com` serves `connect-src 'self' https://*.grab.com https://browser-intake-datadoghq.com https://myteksi.s3.ap-southeast-1.amazonaws.com https://*.grabtaxi.com` — **no PSP, no orchestrator, no vendor endpoint of any kind** — and `frame-src` enumerating **only first-party payment hosts**: `paysdk-web.grab.com`, `paysuite.grab.com`, `paysuite.moca.vn`, `pay.grab.com`.
3. **By the production bundle:** `food.grab.com` loads **`window.PaySDK`** from a Grab-hosted `paysdkWebSdkUrl`, with modes **`PAYMENT_RECOMMENDATION`** and **`PAYMENT_LIST`**, its own `fetchPaySdkToken`, its own `payment_method_selected` events and `paymentTypeID` space, and its own card-add flow with **`add_credit_card_failed_3ds`** error handling. **Grab's own SDK renders the method list, ranks methods, collects the card and handles 3DS.** That is an orchestration layer by function, built in-house.

**Zero occurrences** of Juspay, Spreedly, Primer, Gr4vy, CellPoint, Payrails, APEXX, BR-DGE, Pagos or Yuno across the 4.8 MB `food.grab.com` production bundle, the 4.1 MB 20-F, four earnings releases, six transaction 6-Ks, four first-party legal documents and five live CSP headers. (`Yuno` returned 1 case-insensitive hit in the bundle and **0 in context** — noise.)

> ⚠️ **Two honest limits on the negative.** (a) These are **web** assets. Virtually all of Grab's volume runs through **native apps**, and absence in web code is not absence in an app binary. (b) **A browser CSP cannot see server-to-server acquirer calls.** Adyen and Stripe are confirmed by the 20-F precisely because they sit behind the layer, where no CSP reaches. The classification rests on the 20-F plus the first-party SDK, not on the CSP negatives alone.

### Buying signals
- 🚀 **TAIWAN — a ninth market, agreed and not yet closed.** 23 Mar 2026: Grab agreed to acquire **Delivery Hero's foodpanda delivery business in Taiwan for $600m cash**, cash-free/debt-free, *"expected to take place in the second half of 2026"*, subject to regulatory approval. Filed to the **Taiwan Fair Trade Commission on 27 March 2026**; as of **18 Aug 2026** the TFTC had **not** decided. The TFTC **blocked Uber Eats' bid for the same asset in Dec 2024**, and is examining *"whether Uber has any degree of control over Grab"*. [6-K, 23 Mar 2026](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000051/a6-kxgarnetannouncement.htm) · [Taiwan News, 2 Jul 2026](https://www.taiwannews.com.tw/en/news/6393766) · [mlex, 18 Aug 2026 — `[UNVERIFIED — search summary only, page not fetched]`](https://www.mlex.com/articles/2514542)
- 🤝 **ATOME FINANCIAL — $1.49bn for 60%, announced 15 Sep 2026.** BNPL / consumer cash loans / BNPL cards / digital lending across **Singapore, Malaysia, the Philippines, Indonesia and Thailand**, with a **network of over 30,000 brands** and a **$1bn gross loan portfolio**. Grab's own framing: *"unlocking opportunities for us to serve Atome's large merchant network."* Completion expected **by Q3 2027**. [6-K + Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000133/exhibit991-atometransactio.htm)
- 💼 **PAYMENT HIRING IS LIVE AND BROAD.** Seven current payment-titled openings on Grab's own careers site (fetched 2026-10-13), including **Off-Platform Payment Operations Manager**, **Engineering Manager II, Payments**, **Senior Analytics Manager, Payments**, **Senior Product Designer, Payments**, **Assistant Manager, Consumer Payments (GrabFin)**, **Head, Payment and Insurance — Thailand**, and **Commercial Strategy Lead, PayLater Lending & OmniCommerce**. [grab.careers](https://www.grab.careers/en/jobs/?search=payments)
- 🚀 **SUPERBANK CONSOLIDATED (ID), May–June 2026** — Grab's combined stake rose above 50%; a **$307m one-time gain** on consolidation flowed through Q2 2026 profit. Total deposits across GXS / GXBank / Superbank reached **$2.5bn**. [6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000085/a6-kxsuperbankconsolidatio.htm) · [Q2 2026](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000123/a2026q2-earningspressrelea.htm)
- 📋 **No public payment RFP found.** The RFP override does **not** apply.
- 💰 **NO funding round in the last 12 months — and this is a capital-returning company.** The **$1.5bn zero-coupon convertible senior notes due 2030** were issued in **June 2025**, 16 months before this report. Since then: a **$750m** new repurchase authorisation (Aug 2026) taking cumulative authorisation to **$1.75bn since 2024**, and Atome funded *"entirely from our existing cash"*. Gross cash liquidity **$7.4bn**.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated.*

> ⛔ **DO NOT run `/full-outreach` on this account until the Phase 0 routing decision above is made.** Grab holds a payment gateway and acquiring licence. A cold orchestration sequence to a licensed acquirer is the fastest way to lose the thread, and it cuts across whatever Partnerships is doing with GrabPay as a payment method. Resolve the route first; then, if the merchant-side motion is approved, run `/full-outreach grab` built on **Insight #2 (Taiwan)**, not on routing.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — **17 / 29** on arithmetic → ⭐ High Priority (17+) → **OVERRIDDEN DOWN to 🟢 Medium**

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | ✅ **+5** | ⭐ **LOAD-BEARING.** **✅ SOURCED (floor, not a point estimate): ≥53,900,000 consumer transactions per month.** See the derivation box below. Band ≥100,000 → +5. **The under-40,000 auto-reject cannot fire by three orders of magnitude.** |
| Orchestration status | ✅ **+1** | **In-house orchestration layer — confirmed.** GrabLink is a *licensed* in-house gateway and acquiring service; PaySDK/PaySuite is a first-party method-list, method-recommendation, card-capture and 3DS stack. **Capped at +1 by rule** (in-house layer incumbent). Not 0 — the classification is firmly evidenced, not uncertain. |
| 3+ countries | ✅ **+3** | ⭐ **LOAD-BEARING.** **Six countries each above 7% of audited FY2025 revenue** (MY 30.8%, SG 21.6%, ID 21.2%, PH 9.4%, TH 8.5%, VN 7.6%) plus Cambodia and Myanmar, and **3+ confirmed legal entities** (GrabTaxi Holdings Pte Ltd SG, GX Bank Berhad MY, PT Visionet Internasional ID, Grab PH Holdings PH, and more). Awarded on the **legal-entity and revenue-share limb**, not on traffic. [20-F Note 19(ii)](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm) |
| Multiple PSPs | ✅ **+3** | ⭐ **LOAD-BEARING.** **Adyen and Stripe both named in Grab's own 20-F** as third parties it relies on *"to process and remit payments"*, alongside Visa and Mastercard, alongside its own GrabLink acquiring. Two-plus PSPs, first-party sourced. |
| Local rail or licensing gap in a top-3 market | ⬜ **0** | **Deliberately NOT awarded. Three reasons, any one of which is sufficient.** (a) The rule specifies a top-3 **traffic** market and **there is no traffic data**; revenue rank is not the same measure. (b) The absences I can evidence are in the **GrabFood web** method catalogue only — a minor surface — and I have **no evidence of absence in the native apps**, where the volume is. (c) I obtained **no live-cited source for the market dominance** of FPX, PayNow or QRIS; `apac-payments.md` is explicitly a checklist, not a source. **The licensing limb fails affirmatively in the other direction:** Grab holds local entities and payment licences in *every* operating market — SG major payment institution, MY BNM-approved e-money issuer, PH BSP EMI + OPS, TH BOT/MOF payment licence, ID Bank Indonesia payment-system business via BCP/OVO, VN SBV-gated and served via Moca. **This is the least regulatorily-gated merchant in the repo.** What would move the row: a VPN walkthrough of the native app per market plus a live citation for each rail's share. |
| Recent expansion | ✅ **+2** | **Taiwan — a new country — agreed 23 Mar 2026 ($600m, foodpanda TW), filed to the TFTC 27 Mar 2026, closing expected H2 2026.** Plus **Stash (US) completed 1 Jul 2026**, **Superbank (ID) consolidated May–Jun 2026**, **Atome (5 markets) agreed 15 Sep 2026**. All inside 12 months. ⚠️ **Taiwan is agreed, not closed** — the row is awarded on the pattern, and Taiwan's status is stated honestly everywhere it appears. |
| Payment issues | ⬜ **0** | **Deliberately NOT awarded.** I could not establish *moderate or high* frequency. **trustpilot.com returned HTTP 403** and was not readable. What search surfaced was **two isolated Trustpilot anecdotes** (one early-2026 reviewer reporting 3DS verification failing on new cards; one June-2025 reviewer reporting a card not recognised after a $1 test transaction) and a **paid-report marketing page** summarising Google Play reviews — which is not a source. The iOS app rates **4.8/5 on 252k ratings**; Google Play shows **100M+ downloads** and ~16.6M ratings. **Isolated ≠ moderate.** 0 points, and "verify complaint frequency" is in Manual Research. |
| Funding >$10M | ❌ **0** | **Not met, and the direction is the opposite.** The **$1.5bn zero-coupon convertible notes due 2030** were issued **June 2025** — **16 months before this report, outside the 12-month window**. Inside the window Grab *returned* capital: cumulative repurchase authorisation **$1.75bn since 2024**, a new **$750m** tranche authorised Aug 2026, **$7.4bn gross cash liquidity**, and the $1.49bn Atome deal funded *"entirely from our existing cash"*. |
| High traffic outside home | ⬜ **0** | **Scored 0 per the no-traffic rule.** ⚠️ **But flag this for Prateek:** on the better available evidence the row **would** fire. Audited FY2025 revenue by geography puts **Singapore (home) at 21.6% of group revenue — far under the 60% threshold**, with Malaysia larger at 30.8%. **If Prateek accepts revenue-by-geography as a substitute for traffic share, this row becomes +2 and the total becomes 19 / 29.** I have not taken that liberty myself; the arithmetic is here both ways. |
| Payment job postings | ✅ **+1** | **Seven live payment-titled openings** on grab.careers (fetched 2026-10-13), including **Off-Platform Payment Operations Manager** and **Head, Payment and Insurance — Thailand**. [Source](https://www.grab.careers/en/jobs/?search=payments) |
| **Total** | **17 / 29** | 5 + 1 + 3 + 3 + 0 + 2 + 0 + 0 + 0 + 2 + 1 = **17**. Re-added independently. ✅ |

**Tier on arithmetic:** ⭐ **High Priority (17+)**.

> ### ⚖️ ANALYST OVERRIDE — tier set DOWN to 🟢 Medium
>
> The method permits an override where *"regulatory reality blocks the pitch"* and where the account is not practically servable as a merchant. Both apply, for one reason:
>
> **Grab is itself a licensed payment gateway and acquiring service, an e-money issuer across six ASEAN economies, a BSP-registered Operator of Payment Systems, and a seller of payment acceptance to third-party merchants with its own Direct API, Shopify/WooCommerce/Magento plugins, tokenisation, next-day settlement and refund tooling.** Under `CLAUDE.md`'s excluded-industries rule and the `/research` Phase 0 table, **that is the definition of a company that routes to Partnerships.** A 17/29 that tells an SDR to open a cold orchestration thread with a licensed acquirer is a false positive, however good the underlying volume signals are.
>
> **What the override does NOT say.** It does not say Grab is a bad account. The merchant half is enormous and genuinely in ICP: $22.1bn FY2025 on-demand GMV, tens of millions of consumer card and wallet transactions a month, bought acquiring from two global PSPs, and a ninth market about to switch on. It says the **route** is wrong, not the **prize**. 🟢 Medium is "worth working, through the right door."
>
> **What would flip it back to ⭐.** Partnerships confirming there is no GrabPay connector conversation in flight, plus a named owner on the merchant side (Group payments engineering or the Taiwan integration lead). Then re-score at 17–19 and treat it as enterprise, not SDR.
>
> **Two override grounds I checked and rejected:**
> - *App-store-dominated revenue* — ❌ **does not apply.** Grab sells physical services, and I verified it: the string "In-App Purchases" appears **zero times** on the iOS listing for `id647268330`, and "In-app purchases" **zero times** on the Google Play listing for `com.grabtaxi.passenger` (394 occurrences of the bundle id on the page, so this is not a neighbour-carousel artefact). **None of Grab's consumer revenue runs through Apple or Google IAP.** Orchestration can touch all of it.
> - *Double counting* — ❌ **does not apply.** "Multiple PSPs" fires off a 20-F risk factor naming Adyen and Stripe; "3+ countries" fires off an audited geographic revenue note. Independent facts, independent sources.

> ### 📐 MONTHLY TRANSACTION COUNT — mandatory disclosure
>
> **✅ SOURCED: ≥53,900,000 per month.** This is a **floor**, derived from a definition, not an estimate.
>
> **BILLING UNIT I AM COUNTING: consumer-paid on-demand orders and rides inside Grab's own apps — Deliveries GMV + Mobility GMV.** Explicitly **excluded**: GrabPay wallet transactions at third-party merchants (volume **not disclosed**), loan disbursements, advertising invoices, driver and merchant payouts, and grocery in-store retail at Jaya/Everrise.
>
> **The arithmetic, both inputs sourced to Grab's own filings:**
> - Q2 2026: **Group MTUs 53.9 million**, described in the same release as *"a record 54 million Monthly Transacting Users"*. [Q2 2026 press release](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000123/a2026q2-earningspressrelea.htm)
> - The 20-F defines the metric: *"**MTUs** means monthly transacting users, defined as the **monthly number of unique users who transact** via Grab's apps, where **transact means to have successfully paid for or utilized** any of Grab's products or services."* [20-F definitions](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm)
> - A monthly transacting user transacts **at least once** in the month. **≥53.9 million unique transactors ⟹ ≥53.9 million transactions per month.**
>
> **Two honesty notes on that floor.** (a) The definition says *"paid for **or utilized**"*, and explicitly admits a non-paying tail — *"including offline Jaya Grocer transactions where users record their Jaya Grocer loyalty points on the Grab app."* So not every MTU necessarily paid. **Discount it entirely and the conclusion is unchanged:** FY2025 **Mobility MTUs alone averaged 29.7 million per month** and **Deliveries MTUs 25.4 million**, each ~300× the rejection threshold. (b) Independent sanity check from the other direction: on-demand GMV was **$2,154m per month** in Q2 2026 ($6,463m ÷ 3). Even at an implausibly high **$100** average order value that is **21.5 million transactions per month**. The gate cannot fire on any assumption about order size.
>
> **What I am NOT relying on:** the 20-F's 2025 corporate milestone *"Our on-demand businesses exceeded 20 billion transactions."* It sits in a **list of lifetime corporate milestones by year**, which reads as **cumulative since inception**, not as an annual figure — and 20bn/year against 47.2m FY2025 MTUs would imply ~35 transactions per user per month, which is not credible for food and rides. **Period ambiguous; not used.** Flagged because someone will find it and quote it as an annual number.
>
> **No ATV / AOV figure was published or obtainable.** "average transaction value", "average order value" and "per transaction" each return **zero or one irrelevant hit** in the 20-F. Any revenue ÷ ATV derivation would be an assumption; none is offered.

### Source Notes
- ✅ **Adyen and Stripe as Grab's processors** — verbatim from the 20-F risk factors, quoted in full in Section 3A. The load-bearing finding of this report. **What it does NOT say:** which acquirer covers which market, or what share each carries. That is the open question.
- ✅ **GrabLink as a licensed gateway and acquiring service** — verbatim from the 20-F business description. The load-bearing Phase 0 fact.
- ✅ **Audited revenue by country FY2025** — the 20-F's IFRS 8 geographic note. Shares recomputed from the printed figures and they sum to the printed total. Stronger than any traffic estimate.
- ✅ **The per-market wallet map `{ID:"OVO", VN:"Moca", SG:"Grabpay"}` and the card-brand list `[Visa,"MasterCard"]`** — read directly out of Grab's own `food.grab.com` production bundle. First-party. **Caveat: this is the GrabFood *web* surface.** It proves which methods that surface offers; it does **not** prove what the native app offers, and absences must be read that way everywhere in this file.
- ✅ **The in-house payment stack** — five live CSP headers (`merchant.grab.com`, `paysuite.grab.com`, `paysuite.moca.vn`, `pay.grab.com`, `www.grab.com`), **none using `strict-dynamic`**, so vendor absence in them is meaningful rather than vacuous. Hosts: `paysdk-web.grab.com`, `paysuite.grab.com`, `paysuite.moca.vn`, `pay.grab.com`, `paysdk-demo.grab.com`, plus surfaces `book.grab.com`, `food.grab.com`, `express.grab.com`.
- ⚠️ **The "Key Partners" PSP rosters are identified from logo image filenames, not alt text.** The carousel `<div>`s carry **no `alt` attributes** (the only `alt` values on the SG page are the three testimonial headshots). The identifications rest on filenames: `ayden-logo.png` → Adyen *(note Grab's own misspelling)*, `2c2p.png`, `Stripe_logo_revised_2016.png`, `fomopay.png`, `LIQUIDPAY-1.png`, `2C2P.png`, `ADAPTIS-by-NTT-DATA.png`, `Adyen_Corporate_Logo.svg_.png`, `Fiuu_blue.png`, `Revenue-Harvest-.v1.png`, `Revenue-Monster.png`, `SenangPay.png`. **One logo is unidentified: `uniweblogosvg.svg`.** Treat the roster as high-confidence but filename-derived. The SG assets were uploaded **2019–2022**; the MY assets **Dec 2025** — so the MY roster is the current one.
- ⚠️ **`Splytech` appears in two Grab CSPs and is NOT a payment vendor.** `www.grab.com` sends `x-frame-options: allow-from splytech.io` and `frame-ancestors 'self' https://splytech.io https://*.splytech.io`; `pay.grab.com` allows `widget-grab.splytech.io`, `widget-grab-pp.splytech.io` and `widget-grab-live.sandbox.splytech.io` as frame ancestors. Splyt is a **mobility supply aggregator** — Grab rides surfaced inside partner apps. It means **Grab's payment page is embedded in a third-party booking widget**, which is a distribution finding, not a PSP finding. Do not report it as a payment vendor.
- ⚠️ **"Moca" is not in the 20-F.** Zero occurrences. The Vietnam wallet identification rests entirely on Grab's own production assets. Label it as such.
- ⚠️ **Taiwan is agreed, not closed**, and the TFTC had not decided as of 18 Aug 2026 (that status line is `[UNVERIFIED — search summary only, page not fetched]`; mlex was not fetched). The **$600m, the 23 Mar 2026 date and the H2 2026 expectation are first-party from the 6-K**. The **27 Mar 2026 TFTC filing date and the Uber-control question** come from a **fetched** Taiwan News page.
- ⚠️ **The Adyen GrabPay page is from 18 Sep 2019.** The "600,000 merchants" and "e-money licences in the major six ASEAN economies" figures are **seven years old**. Do not quote them as current.
- ⚠️ **Grab's SG privacy notice names no payment vendor.** It discloses data to *"payment processors and facilitators"*, *"payment network providers"* and *"our business partners, such as ... payment providers"* — generic categories only. The 20-F, not the privacy policy, is where the names are. Noted because the method expects the opposite in APAC.
- ❌ **Per-market acquirer allocation — NOT FOUND.** The single highest-value open question on this account.
- ❌ **Which MAS PS Act licence classes GPay Network (S) Pte Ltd actually holds — NOT FOUND.** The MAS Financial Institutions Directory was unreachable. The 20-F establishes that Grab is *"a major payment institution"* and that GrabLink's acquiring is *"licensed under the Payments Services Act"*; it does not enumerate the classes. This is the gap that would make the Phase 0 verdict airtight rather than strongly evidenced.
- ❌ **GrabPay third-party-merchant transaction volume — NOT DISCLOSED anywhere.** Grab reports Financial Services *revenue* ($134m in Q2 2026) but no payments TPV.
- ❌ **Cambodia and Myanmar** — no entity, no rails, no payment detail found. $30m combined ("Rest of Southeast Asia"), 0.9% of revenue. The repo's existing KH intel (Grab Cambodia on **ABA PayWay** for pay-in and **ABA accounts for automatic driver payouts**, [b2b-cambodia, 3 Sep 2025](https://b2b-cambodia.com/news/milestone-in-digital-integration-aba-and-grab-advance-cashless-ecosystem-in-cambodia)) is **reused verbatim from `2-ready-to-outreach/tada-mobility.md` and was NOT independently re-fetched in this run.** Label it accordingly.

### Success Case Alternatives
- **inDrive** — ⭐ **the right case for this account.** Multi-country ride-hailing, 50+ countries, published results *~90% approval, 10 new countries in under 8 months*. The second half of that is the whole pitch to Grab: **time-to-live in a new market**, which is exactly Taiwan. [y.uno/en/success-stories/indrive](https://y.uno/en/success-stories/indrive)
- **Rappi** — super app, marketplace, multi-country: *zero implementation delays, hundreds of methods, 80% less analyst work*. The closest **business-model** analogue in the library — a multi-country super app with deliveries, mobility and a wallet. [y.uno/success-cases/rappi](https://y.uno/success-cases/rappi)
- **Uber** — ✅ confirmed Yuno customer, verified live on y.uno 2026-10-13. **Nameable only; no published metrics exist, never attach a number.** Carries unusual weight here because Uber is **Grab's largest institutional shareholder at 13.1%** — but see the caution in Insight #5 before using it.
- **McDonald's / Arcos Dorados** — QSR across 21 countries, unified processing. Relevant to the GrabFood merchant side. No public link.
- ❌ **Do NOT use Livelo, Wingo, Vibra or Reserva here.** All are single-market or LATAM-retail decline-cascade cases. Grab already runs its own routing; a cascade case misreads the account.

---

## Executive Summary

Grab is Southeast Asia's leading superapp — NASDAQ-listed, profitable, **$3.37bn FY2025 revenue** on **$22.1bn of on-demand GMV**, **53.9m monthly transacting users**, eight markets and 900+ cities. The key payment-infrastructure finding is that Grab sits on **both sides** of the payments market: it has built **GrabLink**, *"our in-house PCI-compliant secure payment gateway and acquiring service licensed under the Payments Services Act of Singapore"*, and it sells GrabPay and PayLater acceptance to third-party merchants through its own Direct API, Shopify/WooCommerce/Magento plugins and a named roster of distributing PSPs — while **simultaneously still buying acquiring from Adyen and Stripe** for its own consumer volume, by its own 20-F admission. **The orchestration opportunity is therefore not orchestration.** It is reach: the markets and rails Grab's own layer cannot acquire in, with **Taiwan — a ninth market, $600m agreed in March 2026 and still awaiting Fair Trade Commission clearance — as the single live entry point.** The motion is **in-house**; the honest Phase 0 verdict is that the excluded-industry gate **fires** and the primary route is **Partnerships**.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** ❌ **NONE.** No traffic data was supplied by Prateek, no `accounts/traffic/grab.md` exists, no SimilarWeb MCP tool is configured in this environment, and the search fallback was deliberately not spent (see Method Deviations §2).

**This section cannot be completed. No country traffic split is given and none is invented.**

Consequences, stated so they are not rediscovered: the ICP row *"High traffic outside home"* scores **0**; the *"local rail or licensing gap in a top-3 market"* row cannot use a traffic ranking and scores **0**; and Overall Research Confidence is downgraded one level on this basis.

---

### Section 1-ALT: Audited scale and footprint (what replaces traffic here)

**Why this is better than traffic for this account.** Grab is app-first and files a 20-F. Its web surfaces are a minority channel. The right proxies are its own disclosed operating metrics, and they are audited rather than modelled.

#### Revenue by geography — FY2025 (audited, 20-F Note 19(ii) / Item 5.A)

| Rank | Country | FY2025 ($m) | Share | FY2024 ($m) | YoY | Local entity? |
|---|---|---|---|---|---|---|
| 1 | **Malaysia** | **1,039** | **30.8%** | 816 | **+27%** | ✅ (see distortion note) |
| 2 | **Singapore** (home) | **727** | **21.6%** | 578 | **+26%** | ✅ |
| 3 | **Indonesia** | **715** | **21.2%** | 643 | +11% | ✅ |
| 4 | **Philippines** | **316** | **9.4%** | 265 | +19% | ✅ |
| 5 | **Thailand** | **288** | **8.5%** | 252 | +14% | ✅ licensed |
| 6 | **Vietnam** | **255** | **7.6%** | 228 | +12% | ⚠️ not found by name |
| 7 | **Rest of Southeast Asia** (Cambodia, Myanmar) | **30** | **0.9%** | 15 | **+100%** | ⚠️ not found |
| — | **Total** | **3,370** | 100% | 2,797 | **+20%** | — |

**Six markets above 7% each. Home market 21.6%.** Revenue is presented **net of incentives** (FY2025: partner incentives $1,002m, consumer incentives $1,268m). ⚠️ Malaysia's rank is inflated by gross-recognised grocery retail — see the distortion note in Quick Look.

#### Group operating metrics

| Metric | Q2 2026 | Q2 2025 | YoY | Source |
|---|---|---|---|---|
| Revenue | **$997m** | $819m | +22% (+21% cc) | [Q2 2026](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000123/a2026q2-earningspressrelea.htm) |
| On-Demand GMV | **$6,463m** | $5,354m | +21% (+22% cc) | same |
| On-Demand GMV per MTU | **$131** | $127 | +3% | same |
| **Group MTUs** | **53.9m** | 46.2m | **+17%** | same |
| Gross loan portfolio | **$2,318m** | $781m | **+197%** | same |
| Profit for the period | **$235m** | $20m | NM (incl. $307m one-time Superbank gain) | same |
| Adjusted EBITDA | **$168m** | $109m | +54% | same |

| Metric | Q1 2026 | Source |
|---|---|---|
| Revenue | **$955m (+24% YoY)** | [Q1 2026](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000077/a42026q1-earningspressrele.htm) |
| On-Demand GMV | **$6.1bn (+24% YoY)** | same |
| Profit / Adj. EBITDA | $120m / $154m | same |

| Metric | FY2025 | FY2024 | Source |
|---|---|---|---|
| On-demand GMV | **$22,138m** | $18,364m (+21%) | [20-F](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm) |
| — Deliveries GMV | **$14,236m** (64.3% of on-demand GMV) | $11,724m (+21%) | same |
| — Mobility GMV | **$7,901m** (35.7%) | $6,640m (+19%) | same |
| Group MTUs (monthly average) | **47.2m** | 41.3m (+14%) | same |
| — Deliveries MTUs | **25.4m** | 21.7m (+17%) | same |
| — Mobility MTUs | **29.7m** | 25.3m (+18%) | same |
| — Financial Services MTUs | **30.7m** | 26.4m (+16%) | same |
| On-demand GMV per MTU (annual) | **$513** (mobility $266, deliveries $561) | $494 | same |
| Revenue mix | Deliveries **53.4%** / Mobility **36.2%** / Financial Services **10.3%** / Others 0.1% | 53.4 / 37.4 / 9.1 | same |
| FY2026 guidance (raised at Q2) | **Revenue $4.10–4.15bn (+22–23%)**, Adj. EBITDA **$720–740m** | — | [Q2 2026](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000123/a2026q2-earningspressrelea.htm) |
| 2028 targets (raised at Atome) | **Adj. EBITDA $1.7bn**, **30%+ revenue CAGR 2025–28**, Financial Services Adj. EBITDA **$500m**, GLP **>$6bn** | — | [Atome Ex-99.1](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000133/exhibit991-atometransactio.htm) |

#### App footprint (fetched 2026-10-13)

| Store | Metric | Source |
|---|---|---|
| Google Play (`com.grabtaxi.passenger`, SG) | **100M+ downloads**, ~16.6M ratings. **"In-app purchases" flag: absent** | [Play](https://play.google.com/store/apps/details?id=com.grabtaxi.passenger) |
| Apple App Store (`id647268330`, SG) | **4.8 / 5 from 252k ratings**, **No. 2 in Travel**, v5.432.0, 457 MB, provider **GRABTAXI HOLDINGS PTE. LTD.**, © GrabTaxi Holdings, EN + 10 more languages. **"In-App Purchases": absent.** Privacy *"Data Linked to You"* includes **Purchases → Purchase History** and **Financial Info → Payment Info** | [App Store](https://apps.apple.com/sg/app/grab-app/id647268330) |

⚠️ Play's ratings count appeared twice on the page as **16.6M** and **16.8M**; the discrepancy is unresolved and the lower figure is used. The **100M+ downloads** figure is unambiguous.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Singapore — 3 Media Close, #01-03/06, Singapore 138498. Registrant **Grab Holdings Limited** is incorporated in the **Cayman Islands**. **First incorporated July 2011 as MyTeksi Sdn. Bhd. (Malaysia)**; mobility launched **June 2012** in Malaysia as MyTeksi; **GrabTaxi Holdings Pte. Ltd.** incorporated **June 2013** (Singapore); rebranded to Grab in 2016; NASDAQ listing via the December 2021 Business Combination.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Cayman Islands | **Grab Holdings Limited** (registrant) | SEC CIK 0001855612; Commission File 001-41110 | [20-F cover](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm) |
| Cayman Islands | **Grab Holdings Inc.** ("GHI") | Not found | 20-F definitions |
| Cayman Islands | **AA Holdings Inc.** ("GFG") — financial-services holdco | Not found | 20-F definitions |
| Singapore | **GrabTaxi Holdings Pte. Ltd.** | ✅ **201316157E** | [Web3 Wallet terms](https://www.grab.com/sg/terms-policies/web3-wallet) |
| Singapore | **GPay Network (S) Pte Ltd** ("GPNS") — payments operator | Not found | [PayLater terms](https://www.grab.com/sg/terms-policies/paylater) |
| Singapore | **GFin Services (S) Pte. Ltd.** — BNPL provider | Not found | [PayLater terms](https://www.grab.com/sg/terms-policies/paylater) |
| Singapore | **GXS Bank Pte. Ltd.** — MAS digital bank (JV with Singtel) | Not found | 20-F |
| Singapore | **Validus Capital** — SME lending, acquired via GXS Bank (2025) | Not found | 20-F |
| Malaysia | **MyTeksi Sdn. Bhd.** — original 2011 incorporation | Not found | 20-F Item 4.A |
| Malaysia | **GX Bank Berhad** — BNM-licensed digital bank | Not found | 20-F |
| Malaysia | **GrabFin Operations (Malaysia) Sdn. Bhd.** — licensed money lender (40% via GFSA, option over 60%) | Not found | 20-F related-party note |
| Malaysia | **Eastern Grocer Sdn. Bhd. ("Everrise")** — 80% acquired 3 Mar 2025 | Not found | 20-F Note 27 |
| Indonesia | **PT Visionet Internasional** ("OVO") | Not found | 20-F definitions |
| Indonesia | **PT Bumi Cakrawala Perkasa** ("BCP") — *"our payment system services business is conducted through"* BCP | Not found | 20-F, Indonesia regulatory |
| Indonesia | **PT Indonusa Bara Sejahtera** t/a **OVO Finansial** — P2P lending | Not found | 20-F risk factors |
| Indonesia | **PT Super Bank Indonesia Tbk** — IDX **SUPA**; >50% consolidated from June 2026 | IDX: SUPA | [6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000085/a6-kxsuperbankconsolidatio.htm) |
| Philippines | **Grab PH Holdings** | Not found | 20-F |
| Vietnam | **"Moca"** — `[INFERENCE, not confirmed]`; evidenced only by the live host `paysuite.moca.vn` and Grab's own `{VN:"Moca"}` constant. **Zero occurrences in the 20-F** | Not found | live CSP + `food.grab.com` bundle |
| Thailand | Entity name **not found**; licensed under the Payment Systems Act B.E. 2560 via MOF/BOT | Not found | 20-F, Thailand regulatory |
| Cambodia / Myanmar | **Not found** | — | — |
| United States | **Stash Financial, Inc.** — 100% acquired, closed 1 Jul 2026. **Out of territory** | Not found | [6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000097/a6-kxgrabcompletionofstash.htm) |
| Singapore (pending) | **Neuroncredit Pte. Ltd. ("Atome Financial")** — 60% for $1.49bn, closing by Q3 2027 | Not found | [Atome Ex-99.1](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000133/exhibit991-atometransactio.htm) |
| Germany (investment) | **Vay Technology GmbH** — remote-driving tech, agreement signed 10 Nov 2025 | Not found | [6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561225000063/a6-kxvaytransactionannounc.htm) |
| China (acquired) | **Infermove** — AI robotics for first/last-mile delivery (2025) | Not found | 20-F milestones |

**Cross-Border Gap Analysis**

| Country | In top revenue 6? | Has local entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|---|---|---|---|
| Malaysia | ✅ #1 (30.8%) | ✅ Yes, multiple; **BNM-approved e-money issuer** | e-money issuance requires **prior BNM approval under the Financial Services Act 2013**, plus customer funds in a dedicated trust account (sourced to the 20-F) | **Low** — licensed and present |
| Singapore | ✅ #2 (21.6%) | ✅ Yes; **major payment institution** under the PS Act 2019 | PS Act licensing covers e-money issuance, money transfer, **merchant acquisition** and DPT services | **Low** |
| Indonesia | ✅ #3 (21.2%) | ✅ Yes (BCP / OVO) | Bank Indonesia payment-system regulation; **85% foreign-investment limit and 49% foreign voting cap on OVO** | **Low on acquiring; a structural constraint on ownership** |
| Philippines | ✅ #4 (9.4%) | ✅ Yes | **BSP**: EMI approval (Circular 1166/2023), OPS registration (RA 11127) for **GrabPay and GrabLink**, and a **Merchant Acquisition License** (Circular 1198) for an OPS engaging in merchant acquisition | **Low** |
| Thailand | ✅ #5 (8.5%) | ⚠️ Entity not named | **Payment Systems Act B.E. 2560 (2017)**; MOF licence via **BOT** covering GrabPay Wallet and *"processing credit/debit card payment for Dine Out service"*; emergency decree on technological crimes also applies | **Low on licence; entity unconfirmed** |
| Vietnam | ✅ #6 (7.6%) | ❌🔒 **No entity name found** | **Yes** — intermediary payment services (e-wallet and **intermediary payment gateway**) require an **SBV licence** under the Law on Financial Institutions, AML Law 14/2022/QH15 and **Decree 52/2024/ND-CP**, with minimum charter capital | ⚠️ **The one market where I cannot name the licensed vehicle.** Grab plainly operates there and plainly serves it through "Moca", but I could not evidence the corporate entity. See Manual Research. |
| Cambodia / Myanmar | ❌ 0.9% combined | ❌ Not found | Not researched — the 20-F's KH/MM sections were not extracted within budget | ⚠️ Unknown, immaterial at 0.9% |
| **Taiwan** | ❌ **not yet a market** | ❌ **None — zero mentions of Taiwan in the FY2025 20-F** | ⚠️ **NOT RESEARCHED LIVE. I will not cite Taiwanese payment or e-money licensing from memory.** | 🚩 **The live question. See Insight #2.** |

> **Regulatory gate — the finding runs the opposite way to most accounts in this repo.** Grab is **not** a cross-border merchant eating approval-rate losses for want of local presence. It holds payment licences or approvals in **at least five of its six material markets**, is a **major payment institution** in Singapore and an **approved e-money issuer** in Malaysia, and is a **BSP-registered Operator of Payment Systems** in the Philippines. **Do not open with a cross-border or licensing argument.** It is factually wrong here and it will read as not having done the reading. The only market where a licensing argument is live is **Taiwan**, where Grab has no licence because it has no business there — yet.

> **MANUAL:** verify **GPay Network (S) Pte Ltd** in the MAS Financial Institutions Directory to enumerate its PS Act licence classes, and find the Vietnamese licensed entity behind `paysuite.moca.vn`.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|---|---|---|---|
| **Group-wide (market split NOT disclosed)** | **Adyen** — *"third parties such as Adyen and Stripe to process and remit payments to and from consumers and driver- and merchant-partners"* | `[Third-Party Report]` — the issuer's own SEC annual report | [20-F FY2025](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm) |
| **Group-wide (market split NOT disclosed)** | **Stripe** — same sentence, same role | `[Third-Party Report]` | same |
| Group-wide | **Visa**, **Mastercard** — *"strategic partnerships with financial institutions such as Visa and Mastercard"*. The **only** two card brands in the web method catalogue | `[Third-Party Report]` + `[Source Code]` | same + `food.grab.com` bundle |
| Group-wide | **An unnamed single "third-party payment processor"** that Grab reimburses *"for any reversals, chargebacks, and fines assessed due to rule violations"* | `[Third-Party Report]` | same |
| **Singapore (own licence)** | **GrabLink** — *"our in-house PCI-compliant secure payment gateway and acquiring service licensed under the Payments Services Act of Singapore"* | `[Third-Party Report]` | same |
| **Philippines (own registration)** | **GrabPay and GrabLink** — both registered **Operators of Payment Systems** with the BSP | `[Third-Party Report]` | same |
| Singapore / own stack | **PaySDK**, **PaySuite** (`paysdk-web.grab.com`, `paysuite.grab.com`, `pay.grab.com`, `paysdk-demo.grab.com`) | `[Source Code]` + live CSP | `merchant.grab.com` CSP; `food.grab.com` bundle |
| Vietnam / own stack | **PaySuite on `paysuite.moca.vn`** — Grab's PaySuite CSP served from a Vietnamese domain | `[Source Code]` + live CSP | `https://paysuite.moca.vn/` response headers |
| Cambodia | **ABA PayWay** gateway for pay-in; **ABA accounts** for automatic driver payouts; KHQR top-up | `[Third-Party Report]` — ⚠️ **reused from `2-ready-to-outreach/tada-mobility.md`, NOT re-fetched in this run** | [b2b-cambodia, 3 Sep 2025](https://b2b-cambodia.com/news/milestone-in-digital-integration-aba-and-grab-advance-cashless-ecosystem-in-cambodia) |
| **Distribution side — PSPs through which third-party merchants accept GrabPay (SG)** | **Adyen, 2C2P, Stripe, FOMO Pay, Liquid Pay** + one unidentified (`uniweblogosvg.svg`) | `[Source Code]` — "Key Partners" logo filenames, no alt text; assets uploaded 2019–2022 | [grab.com/sg/merchant/checkout-solutions](https://www.grab.com/sg/merchant/checkout-solutions/) |
| **Distribution side (MY)** | **2C2P, ADAPTIS by NTT DATA, Adyen, Fiuu, Revenue Harvest, Revenue Monster, senangPay** | `[Source Code]` — logo filenames; assets uploaded **Dec 2025** (current) | [grab.com/my/merchant/checkout-solutions](https://www.grab.com/my/merchant/checkout-solutions/) |
| Historic / corroborating | *"'Pay with GrabPay' agreements have also been signed with some of the region's biggest merchant gateways, **including Adyen**"* ⚠️ dated 18 Sep 2019 | `[Provider Case Study]` | [Adyen Knowledge Hub](https://www.adyen.com/en_SG/knowledge-hub/grabpay-enabling-smoother-payments-in-southeast-asia) |
| — | **Checkout.com, Worldpay, Braintree, PayPal, Xendit, Midtrans, Doku, iPay88, Omise, Razorpay, PayU, Cashfree, GMO, SB Payment, KOMOJU, Toss Payments, NICEPAY, eWAY, Windcave, Tyro** | **NOT FOUND** in any source checked | — |

> ⚠️ **`omise` produced 5 hits in the production bundle and all five were `Promise`.** Checked both ways; recorded as a false positive, not a finding.

#### 3B. Payment Orchestrator

**Classification: IN-HOUSE ORCHESTRATION LAYER.** `[Third-Party Report]` + `[Source Code]` + live CSP headers. Evidence set out in full under "Orchestration status" in Quick Look.

> *"Confirmed orchestration-aware — in fact orchestration-owning. The opening is coverage and reach, not the case for orchestration itself."*

**Nuance that matters for the pitch, and that the TAL cell does not capture:** this is **not** a pure in-house build. It is an **in-house layer sitting on top of external acquirers**. Grab's own words: *"**Although we may develop in-house payment processing capabilities, we will likely continue to rely on these strategic partnerships and third-party services.** If these companies become unwilling or unable to provide these services on acceptable terms, **or if we are forced to migrate to other providers, our business would be disrupted by a transition requiring significant time and management resources.**"* That second sentence is the only migration-pain admission in the filing, and it is the one place where a reach-and-redundancy conversation has a hook that Grab itself wrote.

> **MANUAL:** walk the native app checkout in SG, ID, MY, PH, TH and VN with a VPN and a proxy. Everything in this section about **method availability** is from web surfaces; the apps carry the volume.

---

### Section 4: Alternative & Local Payment Methods

> # ⚠️ READ THIS BEFORE USING ANY ROW BELOW
> **Every "Status" in this table describes Grab's own `food.grab.com` web checkout method catalogue, read directly out of its production JavaScript. It does NOT describe the native Grab app.** Grab's volume is overwhelmingly native-app. A `NOT FOUND` below means *"absent from the web method catalogue"*, **not** *"Grab does not support this"*. I have **no evidence either way** for the apps, and I have not asserted any. This is why the "local rail gap" ICP row scores **0**.

**The first-party catalogue, verbatim from Grab's own bundle:**
```
cash · "GrabPay Credits" · "GrabPay Credits UNACTIVED" · "OVO Points" · "OVOPayLater" ·
"PayLater" · {ID:"OVO", VN:"Moca", SG:"Grabpay"} · "Visa" · "postpaidBilling" ·
["Visa","MasterCard"] · {CASH:"CASH", CARD:"CARD", GPCONLY:"GPCONLY"}
```

| Country/Region | Method | Category | Status | Source |
|---|---|---|---|---|
| All markets | **Cash** | Cash | ✅ **Active in checkout** (`CASH`) | `food.grab.com` bundle |
| All markets | **Visa**, **Mastercard** | Cards | ✅ **Active in checkout** (`CARD`; `["Visa","MasterCard"]`) | same |
| All markets | **Amex, JCB, UnionPay, Diners, RuPay** | Cards | ❌ **NOT FOUND — zero occurrences** | same |
| SG | **GrabPay Credits** (+ an `UNACTIVED` state) | Digital wallet | ✅ **Active** (`{SG:"Grabpay"}`) | same |
| SG / MY / PH / TH | **GrabPay** wallet | Digital wallet | ✅ Confirmed per market by the 20-F: *"available in Indonesia (through OVO), Malaysia, the Philippines, Singapore, and Thailand"* | [20-F](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm) |
| ID | **OVO** + **OVO Points** + **OVOPayLater** | Digital wallet / loyalty / BNPL | ✅ **Active** (`{ID:"OVO"}`) | bundle + 20-F |
| VN | **Moca** | Digital wallet | ✅ **Active** (`{VN:"Moca"}`); corroborated by the live `paysuite.moca.vn` host | bundle + live CSP |
| All markets | **PayLater** — postpaid (pay next month) and instalments (**4 / 8 / 12** in MY, **4** in SG) | BNPL / Instalments | ✅ **Active** (`PayLater`, `postpaidBilling`) | bundle + [SG](https://www.grab.com/sg/merchant/checkout-solutions/) / [MY](https://www.grab.com/my/merchant/checkout-solutions/) merchant pages |
| SG | **GrabPay Web3 Wallet** (supported digital tokens) | Crypto | ✅ Terms published and live | [web3-wallet terms](https://www.grab.com/sg/terms-policies/web3-wallet) |
| SG | **GrabCoins** loyalty redemption (OVO Points in ID) | Loyalty | ✅ Confirmed | 20-F |
| **MY** | **FPX** · **DuitNow** (as a pay-in rail) · **Touch 'n Go eWallet** · **Boost** | A2A / wallet | ❌ **NOT FOUND in the web catalogue** — ⚠️ absence in the app NOT established. *(Grab does use **DuitNow QR** on the acceptance side — it offers merchants "a customised GrabPay DuitNow QR code")* | bundle; [MY merchant page](https://www.grab.com/my/merchant/checkout-solutions/) |
| **SG** | **PayNow** · **NETS** | A2A | ❌ **NOT FOUND in the web catalogue** — absence in the app NOT established | bundle |
| **ID** | **QRIS** · bank transfer / virtual account · **GoPay** · **DANA** · **ShopeePay** · Alfamart / Indomaret cash | A2A / wallet / cash | ❌ **NOT FOUND in the web catalogue** — absence in the app NOT established. ⚠️ Note Grab's own 20-F names **Dana**, **GoPay** and **ShopeePay** as *competitors*, which cuts against expecting them as accepted methods | bundle; 20-F competition |
| **PH** | **GCash** · **Maya** · InstaPay / PESONet · OTC cash | Wallet / A2A / cash | ❌ **NOT FOUND in the web catalogue** — absence in the app NOT established. ⚠️ `Maya` returned 6 case-insensitive hits and **0 in context**; checked both ways | bundle |
| **TH** | **PromptPay** · **TrueMoney** · card instalment plans | A2A / wallet / instalments | ❌ **NOT FOUND in the web catalogue** — absence in the app NOT established | bundle |
| **VN** | **MoMo** · **ZaloPay** · **VNPay / VietQR** · **NAPAS** domestic cards | Wallet / A2A / cards | ❌ **NOT FOUND in the web catalogue** — absence in the app NOT established. ⚠️ `MoMo` returned 8 case-insensitive hits and **0 in context** | bundle |
| **KH** | **Bakong** · **KHQR** · ABA Pay · Wing · Pi Pay | A2A / wallet | ❌ **NOT FOUND.** ⚠️ `Wing` = 0 case-sensitive (60 case-insensitive hits were all `following`); `ABA` = the base64 of a 1×1 GIF. Both checked both ways. *(ABA **PayWay** in Cambodia is evidenced only by the reused `tada-mobility.md` source)* | bundle |
| Global | **Apple Pay** · **Google Pay** · **PayPal** | Wallet | ❌ **NOT FOUND in the web catalogue** — absence in the app NOT established. ⚠️ Grab's 20-F names **Google Pay** as a *competitor* in digital payment services | bundle; 20-F |
| Greater China | **Alipay** · **WeChat Pay** · **UnionPay** | Wallet / cards | ❌ **NOT FOUND.** ⚠️ `Alipay` hits were **Ant Design icon definitions**; `WeChat` hits were a **`ua-parser` browser-detection regex**. Both checked in context | bundle |
| All markets | **Carrier billing** · **Direct debit / mandate** | Carrier / mandate | ❌ **NOT FOUND** | bundle |

**The one genuine, first-party-sourced acceptance observation:** **Grab's web checkout takes Visa and Mastercard and nothing else in card.** No Amex, no JCB, no UnionPay, no domestic debit scheme — across markets representing **100% of audited revenue**, including Thailand and Vietnam where JCB and domestic schemes are material. ⚠️ **Web surface only.** Ask about it; do not assert it about the app.

> **MANUAL:** VPN + proxy walkthrough of the native app checkout in the top three markets (MY, SG, ID). This is the single piece of fieldwork that would turn Section 4 from "web catalogue" into a real rail map, and it is what the "local rail gap" ICP row is waiting on.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|---|---|---|---|---|
| 3DS verification failing on newly added cards; card payments ceasing to work | Trustpilot | **Isolated** (single review) | early 2026 | ⚠️ `[UNVERIFIED — search summary only, page not fetched]`. **trustpilot.com returned HTTP 403.** [profile](https://www.trustpilot.com/review/grab.com) |
| App not recognising a card after a successful $1 test authorisation | Trustpilot | **Isolated** (single review) | Jun 2025 | ⚠️ same 403 limitation |
| Difficulty with card transactions; problematic refunds | Google Play reviews, as summarised by a **paid-report marketing page** | **Cannot assess — not a source** | sample review Dec 2024 | ⚠️ A vendor report landing page is not evidence. Recorded only so nobody re-finds it and treats it as one. |

**Net finding:** **no pattern of payment complaints could be established.** Two isolated Trustpilot anecdotes, both reached only through a search summary because Trustpilot blocked the fetch, plus a marketing page. Against that: **iOS 4.8/5 on 252k ratings** and **100M+ Play downloads**. Reddit returned nothing relevant.

**Therefore the ICP "Payment issues" row scores 0.** Isolated is not moderate. If this account is worked, "establish complaint frequency properly" is the second item in Manual Research.

One historical item found and **explicitly not used**: a 2018 Vietnamese report of Grab apologising for disruption when it replaced GrabPay with **GrabPay by Moca** to comply with a State Bank of Vietnam rule. Eight years old, and the only reason to record it is that it independently corroborates the **Moca → Vietnam licensing** story. `[UNVERIFIED — search summary only, page not fetched]`

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | **15 Sep 2026** | **Grab to acquire a controlling 60% of Atome Financial for $1.49bn cash** (BNPL loans, consumer cash loans, BNPL cards, digital lending; SG/MY/PH/ID/TH; 25m cumulative transacted users; **>30,000 brands**; **$1bn gross loan portfolio**). Remaining 40% ~2 years after completion at 13.0× annualised adj. EBITDA / 2.5× revenue, floor $2.0bn, cap $4.5bn. **Completion expected by Q3 2027.** 2028 targets raised to **$1.7bn Adj. EBITDA** and **30%+ revenue CAGR** | **M&A / Payment Platform** | [6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000133/a6-kxatometransactionannou.htm) · [Ex-99.1](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000133/exhibit991-atometransactio.htm) |
| 2 | **4 Aug 2026** | **Record Q2 2026**: revenue $997m (+22%), on-demand GMV $6.46bn (+21%), profit $235m, Adj. EBITDA $168m (+54%), **record 53.9m MTUs**. **FY26 guidance raised** to $4.10–4.15bn / $720–740m. **New $750m share repurchase authorised** (cumulative $1.75bn since 2024) | **Funding (return of capital) / Earnings** | [Q2 2026](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000123/a2026q2-earningspressrelea.htm) |
| 3 | **6 Jul 2026** | **Dara Khosrowshahi (Uber CEO) stepped down from Grab's Board of Directors**, effective same day | **Leadership Change** | [6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000114/a6-kxboardupdate.htm) |
| 4 | **1 Jul 2026** | **Completed acquisition of 100% of Stash Financial, Inc.** (US digital financial services). 50.1% paid at closing; remainder at fair market value over three years. Consolidated into Financial Services from Q3 2026. **Out of APAC territory** | **M&A / Market Expansion** | [6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000097/a6-kxgrabcompletionofstash.htm) · agreed [12 Feb 2026](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000009/a6-kxsapphiretransactionan.htm) |
| 5 | **20 May 2026** | **Superbank (PT Super Bank Indonesia Tbk, IDX: SUPA) consolidated** — Singtel Alpha's stake transferred to GXS Bank, taking Grab above 50%. Drove a **$307m one-time gain** in Q2 2026 | **M&A / Licence** | [6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000085/a6-kxsuperbankconsolidatio.htm) |
| 6 | **23–27 Mar 2026** | ⭐ **TAIWAN. Agreement to acquire Delivery Hero's foodpanda delivery business in Taiwan for $600m cash**, cash-free/debt-free, *"expected to take place in the second half of 2026"*, subject to regulatory approvals. **Filed to the Taiwan Fair Trade Commission 27 Mar 2026.** As of **18 Aug 2026 the TFTC had not decided**; the TFTC blocked Uber Eats' bid for the same asset in Dec 2024 and is examining *"whether Uber has any degree of control over Grab"* | **Market Expansion** | [6-K, 23 Mar 2026](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000051/a6-kxgarnetannouncement.htm) · [Taiwan News, 2 Jul 2026](https://www.taiwannews.com.tw/en/news/6393766) · [mlex, 18 Aug 2026 — `[UNVERIFIED]`](https://www.mlex.com/articles/2514542) |
| 7 | **Live, fetched 2026-10-13** | ⭐ **Payment-infrastructure hiring.** Current openings include **Off-Platform Payment Operations Manager**, **Engineering Manager II, Payments**, **Senior Analytics Manager, Payments**, **Senior Product Designer, Payments**, **Assistant Manager — Consumer Payments (GrabFin)**, **Head, Payment and Insurance — Thailand**, **Commercial Strategy Lead, PayLater Lending & OmniCommerce**, **Senior Engineering Manager, Fraud** | **Payment Infrastructure Hiring** | [grab.careers](https://www.grab.careers/en/jobs/?search=payments) |
| 8 | **10 Nov 2025** | Investment in **Vay Technology GmbH** (remote driving) | **M&A / Investment** | [6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561225000063/a6-kxvaytransactionannounc.htm) |

**No public payment-related RFP found.** The RFP override does not apply.

**Payment-role detail from secondary job boards** (`[UNVERIFIED — search summary only, grab.careers job pages return 403]`): a **Principal Engineer, Payments** scope covering *"acquiring services for merchants"* and spanning *"authorization, capture, settlement, reconciliation, disbursements, refunds and disputes, and wallets and real-time bank transfers"*; an **Engineering Manager II, Payments (GrabFin)** owning a *"Central Reconciliation Platform"*; teams named **Payments FundsCore** (Payment Platform, Driver Payouts, Fee Platform) and **PayCore Foundation**. The **titles** are confirmed against Grab's own fetched careers search; the **scope quotes** are not.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 15 Sep 2026 | Grab to acquire 60% of **Atome Financial** for $1.49bn — BNPL, consumer lending, BNPL cards, **>30,000-brand merchant network** across 5 ASEAN markets | ⭐ Pulls a scaled third-party BNPL acceptance network inside Grab's payment perimeter. Reinforces the Phase 0 verdict | [Ex-99.1](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000133/exhibit991-atometransactio.htm) |
| 2 | 23 Mar 2026 | **$600m for foodpanda Taiwan** — a ninth market, pending TFTC clearance | ⭐ The only live greenfield payment build at Grab. See Insight #2 | [6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000051/a6-kxgarnetannouncement.htm) |
| 3 | 6 Mar 2026 | 20-F FY2025 filed — discloses **GrabLink** as a licensed in-house gateway and acquiring service, and names **Adyen and Stripe** as processors it relies on | ⭐ The two most load-bearing facts in this report | [20-F](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm) |
| 4 | 20 May / Aug 2026 | **Superbank consolidated**; deposits across GXS / GXBank / Superbank reach **$2.5bn**; gross loan portfolio **+197% YoY to $2.3bn**; **$1.2bn** of loans disbursed in Q2 alone | Financial Services is now the fastest-growing segment (+59% revenue YoY) | [6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000085/a6-kxsuperbankconsolidatio.htm) · [Q2 2026](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000123/a2026q2-earningspressrelea.htm) |
| 5 | 18 Sep 2019 ⚠️ **old** | Adyen × Grab Financial Group on GrabPay: *"first fintech platform with access to e-money licenses in the major six economies in ASEAN"*, *"more than 600,000 merchants"*, *"'Pay with GrabPay' agreements ... signed with ... merchant gateways, including Adyen"* | The clearest statement of GrabPay-as-infrastructure, but **seven years old — do not quote the figures as current** | [Adyen](https://www.adyen.com/en_SG/knowledge-hub/grabpay-enabling-smoother-payments-in-southeast-asia) |

**No provider removal found.** No evidence that Grab has dropped Adyen, Stripe or any named method.

---

### Section 8: Checkout Experience Audit

**Scope:** the **web** surfaces only — `food.grab.com` (GrabFood web ordering, a real 54 KB page), its 4.8 MB `_next` bundle set, `merchant.grab.com`, and the payment hosts in its CSP. The **native-app checkout was not accessible** in this environment. **Full checkout flow not completed** — no basket was taken to payment.

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | **Custom-built, first-party, embedded.** `window.PaySDK` is loaded from a Grab-hosted `paysdkWebSdkUrl` into a container the page owns, with `PAYMENT_LIST` and `PAYMENT_RECOMMENDATION` modes and `payment_method_selected` events | **Good** | This is a merchant that built its own checkout SDK. No hosted third-party page, no PSP-branded redirect |
| Guest checkout | Not determined — `book.grab.com` and `express.grab.com` are SPA shells (580 / 1,249 bytes) that render nothing without JS | — | `food.grab.com` renders a real page |
| Steps to complete payment | Not determined (no flow walked) | — | |
| Card input experience | **Grab's own PaySDK collects the card.** Error codes include `add_credit_card`, `add_credit_card_failed`, **`add_credit_card_failed_3ds`**, `add_credit_card_disabled`, `add_credit_card_success`, `sto_session_expired` | **Good** — but it puts Grab, not a PSP, in PCI scope | ⭐ The most consequential finding in this section: card data enters a **Grab-controlled** surface |
| Payment methods visible | `CASH` / `CARD` / `GPCONLY`; Visa + Mastercard; GrabPay Credits; PayLater; `postpaidBilling`; per-market wallet (`OVO` / `Moca` / `Grabpay`); OVO Points; OVOPayLater | **Fair** | Thin for the region — see Section 4's caveat |
| Location-based method display | ✅ Yes — the wallet brand is keyed on market (`{ID:"OVO", VN:"Moca", SG:"Grabpay"}`) and the SDK receives a `location` argument | **Good** | Geo-adaptive by design |
| Instalment / EMI options | ✅ **PayLater**: postpaid (next month) and instalments — **4 in SG**, **4 / 8 / 12 in MY** | **Good** | First-party BNPL, not a third-party provider |
| 3DS implementation | ✅ **Present** — a dedicated `add_credit_card_failed_3ds` error path. **Version not determinable** (`3-D Secure`, `3DS1`, `3DS2`, `EMV 3DS` all return zero in the 20-F) | **Fair** — present, unversioned | |
| PCI indicator | **Self-hosted card fields behind Grab's own licensed gateway.** The 20-F: *"we are subject to the Payment Card Industry Data Security Standard (PCI DSS) with respect to the acceptance of payment cards in the various jurisdictions in which it operates"*, and GrabLink is *"PCI-compliant"* | — | Not a reduced-scope SAQ A posture |
| Mobile responsiveness | Not assessed. ⚠️ Material gap for an app-first business | — | |
| Multi-currency / local pricing | Local-currency pricing is implied by the audited per-country revenue and by constant-currency reporting across *"our transacted currencies other than the U.S. dollar"*. No currency list found in the bundle; **country-metadata currency tables were not treated as a supported-currency list** | — | |
| Saved payment methods | ✅ Yes — *"Tokenisation allows for seamless repeat purchases and subscription payments by enabling single-click payments at checkout"* (merchant-facing); `postpaidBilling` and `OVOPayLater` imply stored credentials; PayLater has an **auto-top-up / auto-deduct** mandate that may fall back across *"any other User's Funding Source"* | **Good** | ⭐ The PayLater fallback chain is itself a routing behaviour — across **funding sources**, not acquirers |
| Error message clarity | Rich, specific, localised error taxonomy: `invalid_payment_method`, `concurrent_spend_limit_check`, `invalid_group`, `judge_location`, `add_credit_card_disabled`, each with its own i18n key and button handler | **Good** | A mature payments front end |

**Asset map (live CSP headers, none using `strict-dynamic`):**
- `merchant.grab.com` → `frame-src 'self' https://message-center-webview.grab.com https://paysdk-web.grab.com https://p.grabtaxi.com https://help.grab.com https://sso.agc.gov.sg https://paysuite.grab.com https://paysuite.moca.vn https://pay.grab.com https://www.grab.com` · `connect-src 'self' https://*.grab.com https://browser-intake-datadoghq.com https://myteksi.s3.ap-southeast-1.amazonaws.com https://*.grabtaxi.com`
- `paysuite.grab.com` and `paysuite.moca.vn` → identical policies; `frame-ancestors` enumerates `paysdk-web.grab.com`, `paysdk-demo.grab.com`, `book.grab.com`, `express.grab.com`, `food.grab.com` and their staging twins
- `pay.grab.com` → `frame-ancestors 'self' https://widget-grab-pp.splytech.io https://widget-grab.splytech.io https://widget-grab-live.sandbox.splytech.io/ https://paysdk-web.grab.com https://paysdk-demo.grab.com https://book.grab.com`
- `www.grab.com` → `frame-ancestors 'self' https://splytech.io https://*.splytech.io`, plus `x-frame-options: allow-from splytech.io`
- `food.grab.com` → `frame-ancestors https://lkpp-portal.festiware.com https://bela-portal.festiware.com https://belapengadaan.lkpp.go.id` — Indonesian **government e-procurement** portals. Not payment; recorded because it shows a B2G channel.

> **MANUAL:** the app checkout is the real surface. VPN + proxy, per market.

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|---|---|---|
| PCI DSS Level | **Not found.** No level stated anywhere. Grab confirms it is *"subject to the Payment Card Industry Data Security Standard ('PCI DSS') with respect to the acceptance of payment cards in the various jurisdictions in which it operates"*, and describes **GrabLink** as *"PCI-compliant"* | [20-F](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm) |
| Card data handling | **Full PCI scope — the merchant's own, not a PSP's.** Card capture happens inside Grab's own PaySDK (`add_credit_card*` flows incl. a 3DS error path) behind Grab's own licensed gateway. **This is not SAQ A or SAQ A-EP.** | 20-F + `food.grab.com` bundle |
| Card network rules | Grab explicitly carries scheme-rule risk: *"we must comply with payment card network operating rules ... Failure to comply may subject us to fines, higher transaction fees, or the loss of our ability to accept online payments. We have also agreed to **reimburse our third-party payment processor for any reversals, chargebacks, and fines** assessed due to rule violations."* | 20-F |
| Tokenization | ✅ Confirmed on the acceptance side: *"Tokenisation allows for seamless repeat purchases and subscription payments."* The **consumer-side** card-on-file tokenization approach (network token vs PAN) is **not disclosed** | [SG merchant page](https://www.grab.com/sg/merchant/checkout-solutions/) |
| **Recommended Yuno integration** | ⭐ **Back-to-back API, not SDK.** Grab holds its own PCI scope, its own gateway licence, its own card vault and its own checkout SDK. An SDK integration would ask them to give up the surface they built and licensed. A **server-to-server, back-to-back** integration behind GrabLink is the only shape that respects the build — and it is also the only shape that fits the actual opportunity (extra acquirer and APM reach in markets their layer cannot cover). | Derived from the above |

`[INFERENCE, not confirmed]`: because card data is captured in Grab's own surface rather than a PSP iframe, Grab's PCI scope is **wider**, not reduced — the opposite of the usual finding. **No compliance level is asserted.**

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: They built a gateway to stop paying for one — and their own filing says they still pay for one.**
> **Evidence:** §3B / 20-F — **GrabLink** is *"our in-house PCI-compliant secure payment gateway and acquiring service licensed under the Payments Services Act of Singapore **aimed at reducing dependency on third-party providers**, and helps us **reduce our cost of funds** across Grab transactions"* **+** §3A / the same 20-F — *"We rely on strategic partnerships with financial institutions such as Visa and Mastercard and third parties such as **Adyen and Stripe** to process and remit payments ... **Although we may develop in-house payment processing capabilities, we will likely continue to rely on these strategic partnerships and third-party services**"* **+** §1-ALT — six markets, each >7% of audited revenue, on that mixed footing. [20-F](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm)
> **Pain Point:** The build has a stated economic purpose — cost of funds and vendor dependency — and the filing concedes it has not finished the job. Two global acquirers across eight markets with eight different domestic rail sets means **per-market acquiring coverage is bounded by what Adyen and Stripe can locally acquire**. Everything outside that boundary is a bespoke integration that Grab's own engineering team has to build, license and reconcile — and they are hiring a Central Reconciliation Platform team and an Off-Platform Payment Operations Manager to do exactly that.
> **Yuno Value Proposition:** **Reach behind their layer, not instead of it.** A back-to-back API that adds acquirers and local methods per market without touching GrabLink, PaySDK or the licensed surface they built. They keep the gateway, the vault, the PCI scope and the routing logic; they stop building the long tail of per-market integrations one at a time. The argument is **opportunity cost of engineering**, not capability.
> **Best Success Case:** **inDrive** — multi-country ride-hailing, *10 new countries in under 8 months*. The relevant half is time-to-live, not approval rate. Secondary: **Rappi**, the closest business-model analogue — multi-country super app, *hundreds of methods, zero implementation delays, 80% less analyst work*.
> **Outreach Angle:** Your 20-F says GrabLink exists to reduce dependency on third-party providers — and in the same document that you'll likely keep relying on two of them. I'm curious which markets that boundary actually bites in.
> **Suggested Subject Line:** GrabLink's boundary

> **Insight #2: ⭐ Taiwan is a ninth market, a rail set Grab has never touched, and the only greenfield payment build on their roadmap.**
> **Evidence:** §6 / 6-K 23 Mar 2026 — **$600m cash for Delivery Hero's foodpanda Taiwan delivery business**, cash-free/debt-free, closing *"expected ... in the second half of 2026"*, subject to regulatory approvals; filed to the **Taiwan Fair Trade Commission 27 Mar 2026** and **still undecided as of 18 Aug 2026** **+** §2 / the FY2025 20-F contains **zero occurrences of "Taiwan"** — Grab has no Taiwanese entity, no Taiwanese payment licence and no Taiwanese rail integration, because it has never operated there **+** §2 / by contrast Grab holds payment licences or approvals in **five of its six material markets**, so it knows exactly what a new-market payment build costs it. [6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000051/a6-kxgarnetannouncement.htm) · [Taiwan News](https://www.taiwannews.com.tw/en/news/6393766) · [20-F](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm)
> **Pain Point:** On the day the TFTC clears, Grab inherits a live Taiwanese consumer business and has to serve it with a payment stack built for eight ASEAN markets. The rails are different, the acquiring relationships are new, and a market Grab is paying **$600m** for will be running on whatever its in-house layer can reach in Taiwan — which, on the filing evidence, is nothing yet. Every week of integration lag after close is revenue on an asset they have already bought.
> **Yuno Value Proposition:** Day-one local method and acquirer coverage in a market where GrabLink has no licence and no local acquiring, delivered behind their existing layer so nothing in the ASEAN stack changes. This is the one place where the pitch is additive rather than competitive — and where "ship a market in weeks, not quarters" is a number they can put against the $600m.
> **Best Success Case:** **inDrive** — *10 new countries in under 8 months* is the exact shape of this problem.
> **Outreach Angle:** You've agreed $600m for foodpanda Taiwan and the FTC hasn't ruled yet, so the integration window is still open. Worth asking what the Taiwanese rail set looks like against a payment stack built for eight ASEAN markets.
> **Suggested Subject Line:** Taiwan rails before the FTC rules
> ⚠️ **Before sending: verify the current TFTC status and the actual Taiwanese rail set against live sources.** I did **not** research Taiwanese rails or licensing in this run, and `apac-payments.md` is a checklist, not a source. **Ask the question; do not assert which rails they are missing.** Naming a Taiwanese rail wrongly to the company that just paid $600m for the market is a one-email account.

> **Insight #3: Their web checkout takes Visa and Mastercard and nothing else — across 100% of audited revenue.**
> **Evidence:** §4 / Grab's own `food.grab.com` production bundle declares the card-brand list as **`["Visa","MasterCard"]`** and the payment-type enum as `{CASH, CARD, GPCONLY}`, with no Amex, JCB, UnionPay or domestic debit scheme anywhere in 4.8 MB **+** §1-ALT / that surface serves markets representing **$3,370m of audited FY2025 revenue** — Malaysia 30.8%, Singapore 21.6%, Indonesia 21.2%, Philippines 9.4%, Thailand 8.5%, Vietnam 7.6% **+** §3A / the 20-F names only Visa and Mastercard as its card-network partnerships.
> **Pain Point:** On the web surface, a JCB holder in Thailand or Vietnam, a UnionPay holder, or an Amex holder cannot pay by card at all — they fall back to cash or a wallet, or they leave. Grab's own 20-F already argues the other side of this, noting that *"a significant portion of the population in these markets does not have access to credit or debit cards"* and that GrabPay exists because of it — which makes the card tail genuinely marginal in volume terms, and genuinely cheap to add.
> **Yuno Value Proposition:** Additional card-scheme and domestic-debit coverage per market without a new acquiring relationship per scheme.
> **Best Success Case:** **Rappi** — *hundreds of payment methods* across a multi-country super app.
> **Outreach Angle:** Your web checkout declares Visa and Mastercard and no third brand. Is that a deliberate call on the economics, or just the order the integrations happened in?
> **Suggested Subject Line:** Two card brands, six markets
> ⚠️ **This is a WEB finding. Do not claim it about the app.** Phrase it as an observation about the web surface and a question about the app, exactly as written above.

> **Insight #4: Atome puts 30,000 third-party brands inside Grab's payment perimeter — and that makes this a Partnerships conversation, not an SDR one.**
> **Evidence:** §6 / the Atome Ex-99.1 — 60% for **$1.49bn**, five ASEAN markets, *"over 30,000 brands"*, a **$1bn** gross loan portfolio, and Grab's own stated rationale of *"unlocking opportunities for us to serve Atome's large merchant network"* **+** Phase 0 items 5–6 / Grab already sells GrabPay and PayLater acceptance to third-party merchants through its own Direct API and through **2C2P, Adyen, Stripe, Fiuu, Revenue Monster, senangPay, FOMO Pay, Liquid Pay and ADAPTIS**.
> **Pain Point / Opportunity:** This is Grab expanding its **acquiring-side** footprint, not its merchant-side one. Post-close it will be an even larger payment-method issuer with an even larger merchant network.
> **Yuno Value Proposition:** **Connector, not customer.** GrabPay and PayLater as payment methods available through Yuno across five to six ASEAN markets — distribution for them, coverage for Yuno's merchants.
> **Best Success Case:** n/a — this is a partnership shape, not a merchant case.
> **Outreach Angle:** ⛔ **None. Route to Partnerships.** Do not send a merchant-side email on the back of this insight.
> **Suggested Subject Line:** n/a

> **Insight #5: Uber owns 13.1% of Grab and runs its payments on Yuno. Handle with care.**
> **Evidence:** §2 / the 20-F principal-shareholders table — **Uber Technologies, Inc.: 535,902,982 shares, 13.1% of ordinary shares, 5.5% of voting power** (per Uber's Schedule 13D), the largest institutional holder ahead of SB Investment Advisers (9.8%) and Toyota (5.4%) **+** Yuno's own site, verified live 2026-10-13, which serves `/logos/uber_logo.svg` on `y.uno/en`.
> **Pain Point / Opportunity:** Grab's largest institutional shareholder is a global ride-hailing operator that solved the multi-market acceptance problem by buying orchestration rather than extending a build.
> **Yuno Value Proposition:** Credibility, not capability. It is the single strongest proof point that an in-house-first mobility operator at global scale still chose an orchestration layer for reach.
> **Best Success Case:** **Uber** — ✅ confirmed customer, **nameable only, never with a number attached.**
> **Outreach Angle:** ⚠️ **Use sparingly and never as leverage.** Three reasons. (1) The evidence that Uber is a Yuno customer is **Yuno's own customer list**, not independent reporting — state it as a relationship, never as a case study, and never attach a metric. (2) **Dara Khosrowshahi stepped down from Grab's board on 6 July 2026**, so the governance link is weaker than the shareholding suggests. (3) **The Taiwan FTC is actively examining *"whether Uber has any degree of control over Grab"*** — invoking Uber to Grab while that question is live in a $600m merger review is a genuinely bad idea. **My recommendation: hold this one for a live call, not a cold email.**
> **Suggested Subject Line:** n/a — do not lead with this

### Quick Hits: Ready-to-Use Sales Ammunition

*Grounded only in verified findings. None names a Yuno competitor. None asserts a rail absence in the native app. None contains a booking link.*

**Email hooks (one sentence each):**
1. Your 20-F describes GrabLink as an in-house gateway built *"aimed at reducing dependency on third-party providers"* — and a few pages later says you'll likely keep relying on two of them; I'm curious where that boundary actually sits per market.
2. You've agreed $600m for foodpanda Taiwan and the Fair Trade Commission hasn't ruled yet — which means the payment build for a ninth market is still a decision rather than a deadline.
3. Your web checkout declares exactly two card brands across six markets that are 100% of your audited revenue, which reads like an integration backlog rather than a pricing decision.

**Cold call openers (conversational, one sentence each):**
1. I read your 20-F rather than a press release, so I'll skip the part where I tell you that you need a routing layer — you licensed one.
2. Taiwan's the reason I called: you're buying a market your payment stack has never touched, and the FTC clock is the only part of that you don't control.
3. You're hiring an Off-Platform Payment Operations Manager and a Central Reconciliation Platform team at the same time — that usually means the integration tail is growing faster than the team is.

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---|---|---|---|---|---|---|
| **GoTo / Gojek** | gotocompany.com · gojek.com | Indonesia | Part of GoTo | **ID** (+ SG) — Grab's primary rival | **In-house Routing**; Midtrans + GoPay. Grab's own 20-F names **GoPay** and **Dana** as competitors in digital payments | `accounts/apac-tal.csv` (verified by CSV parse) + 20-F |
| **foodpanda (Delivery Hero)** | foodpanda.com | Singapore | Part of Delivery Hero | **SG, MY, TH, PH, KH, MM** + **Taiwan — the asset Grab is buying** | None named in the TAL | TAL + [6-K](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000051/a6-kxgarnetannouncement.htm) |
| **EASI** | foodpanda.com.tw | **Taiwan** | Not found | **TW** — ⭐ **this is the business Grab agreed to buy for $600m** | None named | TAL + 6-K |
| **Sea / ShopeeFood (ShopeePay)** | — | Singapore | Not in TAL under this name | SG, ID, MY, TH, VN, PH | Grab's 20-F names **ShopeePay** as a digital-payments competitor | 20-F |
| **LINE MAN (LINE MAN Wongnai)** | lmwn.com | Thailand | Not found | **TH** | None named | TAL |
| **Lalamove** | lalamove.com | Hong Kong | ~$1.5bn est. (private) | HK + Asia + LATAM | None named | TAL |
| **TADA Mobility** | tada.global | Singapore | ~$50m est. (MVL) | **SG, KH, VN, TH** | **Stripe** (sole named PSP, Payments + Radar + Adaptive Acceptance); **no orchestrator** | `2-ready-to-outreach/tada-mobility.md` (ICP 19/29 ⭐) |
| **Ryde Group Ltd** | rydesharing.com | Singapore | ~$20m, listed NYSE American: RYDE | **SG** | None named. **Announced a 12-month "next-generation payment capabilities" programme on 30 Sep 2026** | `tada-mobility.md` + [Newswire](https://www.newswire.com/news/ryde-advances-ryde-2-0-with-ai-powered-mobility-ev-fleet-technology-and-next) |
| **ComfortDelGro (CDG Zig)** | cdgtaxi.com.sg | Singapore | ~$3.3bn (FY24) | **SG** (+ AU/UK/CN) | None named; Alipay+ / Touch 'n Go deployment `[UNVERIFIED]` | `tada-mobility.md` |
| **Uber** | uber.com | USA | — | ⚠️ **Not an operating competitor in SEA** — Grab acquired Uber's SEA business in 2018 under a non-competition agreement. But **Uber holds 13.1% of Grab** | ⭐ **Yuno customer.** **No published metrics — nameable only** | 20-F + y.uno customer list |
| **inDrive** | indrive.com | — | 50+ countries | Emerging-market overlap | ⭐ **Yuno customer** — *~90% approval, 10 new countries in under 8 months* | [y.uno](https://y.uno/en/success-stories/indrive) |
| **Didi** | didiglobal.com | China | ~$29bn (FY24) | CN + LATAM/APAC — no SEA overlap | **In-house Routing** | TAL (verified) |
| **Maxim** | taximaxim.com | ⚠️ TAL says Singapore — **doubtful**, flagged in `tada-mobility.md` | Not found | SEA overlap claimed | None found | TAL |

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---|---|---|---|---|---|
| Rappi | — | Super app, multi-country | LATAM | ⭐ **The closest business-model analogue anywhere** — deliveries + mobility + wallet across many markets. **Yuno customer**: *hundreds of methods, zero implementation delays, 80% less analyst work* | [y.uno/success-cases/rappi](https://y.uno/success-cases/rappi) |
| Rapido | rapido.bike | Bike-taxi aggregator | India | Huge small-ticket ride volume; TAL shows a **regional orchestrator** — proof that mobility peers buy orchestration | TAL |
| Ola | olacabs.com | Ride-hailing | India | $632m; TAL shows a **regional orchestrator** | TAL |
| Pathao | pathao.com | Super app | Bangladesh + Nepal | $50m; same multi-rail, driver-payout shape at a smaller scale | TAL |
| Kakao Mobility | kakaomobility.com | Mobility | South Korea | Domestic-PG-intermediated market; no orchestrator named | TAL |
| Baemin · Coupang Eats | baemin.com · coupangeats.com | Delivery | South Korea | Korea gates domestic acquiring behind a local entity — a market Grab does not serve | TAL |
| Deliveroo Hong Kong | deliveroo.com.hk | Delivery | Hong Kong | FPS / Octopus market; no orchestrator named | TAL |
| J&T Express | jtexpress.co.id | Logistics | Indonesia | COD-heavy, same ID rail set | TAL |
| Namma Yatri / Odisha Yatri | — | Zero-commission ride-hailing | India | Flat-fee-per-ride economics make acceptance cost a direct share of revenue | TAL |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---|---|---|---|---|
| **Uber** | **Yuno** | Not stated | Ride-hailing — **and Grab's largest institutional shareholder at 13.1%** | y.uno site-wide customer list, verified live 2026-10-13 (`/logos/uber_logo.svg`) |
| **inDrive** | **Yuno** | Not stated | Ride-hailing, 50+ countries | [y.uno/en/success-stories/indrive](https://y.uno/en/success-stories/indrive) |
| **Rappi** | **Yuno** | Not stated | ⭐ Super app — closest model analogue | [y.uno/success-cases/rappi](https://y.uno/success-cases/rappi) |
| **Ola** · **Rapido** | A regional orchestrator | Not stated | Mobility, India | `accounts/apac-tal.csv` — ⚠️ TAL entries, need independent confirmation |
| **Grab** · **GoTo / Gojek** · **Didi** | **In-house routing** (not a third-party orchestrator) | — | Super apps / mobility | `accounts/apac-tal.csv`, and for Grab **independently confirmed in this report** |
| — | **No case study found** for foodpanda, Delivery Hero, Sea/Shopee, Lazada or LINE MAN adopting an orchestrator | — | — | Searched; nothing found |

> **The usable competitive line — and its limit.** Every multi-market mobility and super-app peer has an orchestration layer of *some* kind: Uber, inDrive and Rappi **bought** one; Grab, GoTo and Didi **built** one. **Grab is not behind its peers — it is in the "built it" camp with the other three largest players.** That is why the pitch cannot be "you need orchestration" and has to be "your build has a reach boundary, and Taiwan is where it shows." ⚠️ The Uber / inDrive / Rappi evidence is **Yuno's own customer list**, not independent third-party reporting: state it as a customer relationship, never attach a number to Uber, and use inDrive's and Rappi's published figures verbatim or not at all.

#### 11D. Prospect Scoring — LINE MAN Wongnai (`lmwn.com`)

Chosen because it is the one large, independent, single-market delivery platform in Grab's territory with **no payment stack named anywhere in the TAL** — i.e. a possible greenfield. ⚠️ **It was NOT researched in this run; the budget went to the target.** The score below is an artefact of that, not a verdict.

| Signal | Points | Status | Evidence Source |
|---|---|---|---|
| Monthly transaction count | ⬜ 0 | Not researched | — |
| Orchestration status | ⬜ 0 | None named in the TAL; **not independently checked** | TAL |
| 3+ countries | ❌ 0 | Thailand only per the TAL | TAL |
| Multiple PSPs | ⬜ 0 | Not researched | — |
| Local rail / licensing gap in a top-3 market | ⬜ 0 | Not researched | — |
| Recent expansion | ⬜ 0 | Not researched | — |
| Payment issues | ⬜ 0 | Not researched | — |
| Funding >$10M | ⬜ 0 | Not researched | — |
| High traffic outside home | ❌ 0 | Single market | TAL |
| Competitor using orchestration | ✅ **+2** | Uber, inDrive and Rappi are Yuno customers; Grab, GoTo and Didi run in-house routing | y.uno lists; TAL |
| Payment job postings | ⬜ 0 | Not researched | — |
| **Total** | **2 / 29** | 🔴 **Low on current evidence — and the score is meaningless.** A dominant Thai delivery platform in a PromptPay/TrueMoney/instalment market with no named orchestrator is a far better prospect than 2/29 implies. **Re-score properly before dismissing.** | — |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|---|---|---|---|---|---|---|---|
| 1 | **Grab** | **Target** | SG/MY/ID/PH/TH/VN/KH/MM (+TW pending) | **17/29 → overridden 🟢** | 🟢 **Medium — route via Partnerships** | $600m Taiwan entry pending TFTC clearance; licensed in-house gateway buying acquiring from two global PSPs | ✅ Yes |
| 2 | **LINE MAN Wongnai** | Direct competitor | TH | 2/29 ⚠️ under-researched | 🟢 **Re-score** | Dominant independent Thai delivery platform, **no payment stack named anywhere** | ✅ Yes |
| 3 | **foodpanda / Delivery Hero (APAC)** | Direct competitor | SG, MY, TH, PH, KH, MM, HK, TW | Not scored | 🟢 | 8 APAC markets, **no orchestrator named**, and **actively divesting Taiwan to Grab** — a stack in flux is a buying window | ✅ Yes |
| 4 | **GoTo / Gojek** | Direct competitor | ID | Not scored | 🟢 | In-house routing like Grab, but with Midtrans as a captive PSP — the same reach-boundary argument applies | ✅ Yes |
| 5 | **Ryde Group Ltd** | Direct competitor | SG | 3/29 in `tada-mobility.md` ⚠️ | 🟢 **Re-score** | **Announced a 12-month "next-generation payments" programme on 30 Sep 2026**, at a company with public filings | ✅ Yes |
| 6 | **TADA Mobility** | Direct competitor | SG/KH/VN/TH/HK | **19/29** | ⭐ **High** | Already researched and sequenced in this repo — single SGD acquirer across five countries | ✅ Yes |
| 7 | **Lalamove** | Peer | HK + Asia + LATAM | Not scored | 🟢 | *"Driver payouts in many currencies"* — same dual pay-in/payout shape, wider corridor set, no orchestrator named | ✅ Yes |
| 8 | **Pathao** | Peer | BD + NP | Not scored | 🟢 | Super app in a wallet-dominated market with no orchestrator named | ✅ Yes |
| 9 | **Kakao Mobility** | Peer | KR | Not scored | 🟢 | Korea gates domestic acquiring behind local presence — a structural hook Grab does not offer | ✅ Yes |
| 10 | **EASI (foodpanda Taiwan)** | Competitor / acquisition target | TW | Not scored | 🔴 **Deprioritise** | ⚠️ **About to become part of Grab.** Keep on the list only as a Taiwan-market intelligence source | ✅ Yes |

**Genuine finds not on the TAL: none.** Every company named above already has a TAL row. **Sea / ShopeeFood (ShopeePay)** appears in Grab's 20-F as a competitor and I did **not** find it in the TAL under that name — worth a check, though as a payments operator it would hit the same Phase 0 gate Grab does.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|---|---|---|
| Annual Revenue (USD) | **$3,370m FY2025** (+20% YoY). FY2026 guidance **$4.10–4.15bn**. Q1'26 $955m, Q2'26 $997m | [20-F](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm) · [Q2 2026](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000123/a2026q2-earningspressrelea.htm) |
| GMV / Gross Transaction Volume | **$22,138m on-demand GMV FY2025** (Deliveries $14,236m + Mobility $7,901m). Q2'26 **$6,463m** for the quarter | same |
| Average Transaction Value (USD) | ❌ **NOT DISCLOSED.** "average transaction value", "average order value" and "per transaction" each return zero or one irrelevant hit in the 20-F. **No proxy is offered, because an unsourced ATV would make every downstream figure an assumption.** The closest published figures are **on-demand GMV per MTU: $513/year (FY2025), $131/quarter (Q2'26)** — a *per-user*, not *per-transaction*, measure | 20-F |
| Est. Annual Transactions | **≥646 million/year** (= the ≥53.9m monthly floor × 12). A floor, not an estimate. ⚠️ A 20-F corporate milestone reads *"2025 • Our on-demand businesses exceeded 20 billion transactions"* — **period ambiguous, reads as cumulative since inception, deliberately not used** | derived from MTU definition; see the disclosure box |
| **Monthly transaction count** | ⭐ **✅ SOURCED (floor): ≥53,900,000/month.** **BILLING UNIT: consumer-paid on-demand orders and rides inside Grab's own apps (Deliveries + Mobility GMV).** Excludes GrabPay third-party-merchant wallet transactions (volume **not disclosed**), loan disbursements, advertising invoices, driver/merchant payouts and Jaya/Everrise in-store retail. Basis: Q2 2026 **Group MTUs 53.9m** × the 20-F's own definition of MTU as *"the monthly number of unique users who **transact**"*, where *"transact means to have successfully paid for or utilized"* a Grab service ⟹ ≥1 transaction each ⟹ **≥53.9m/month**. Cross-check that needs no assumption: on-demand GMV was **$2,154m/month** in Q2'26, so even at an implausible **$100** AOV the count exceeds **21.5m/month**. Band **≥100,000 → +5**. **The under-40,000 reject cannot fire.** | [Q2 2026](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000123/a2026q2-earningspressrelea.htm) + [20-F definitions](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm) |
| Active Customers / Users | **53.9m Group MTUs (Q2 2026, record)**; FY2025 monthly average **47.2m** (Deliveries 25.4m · Mobility 29.7m · Financial Services 30.7m). **100M+ Google Play downloads**; **252k iOS ratings at 4.8/5** | same + store listings |
| Primary Currency | **USD reporting**; operations in **MYR, SGD, IDR, PHP, THB, VND** and *"our transacted currencies other than the U.S. dollar"*. GrabPay has a **Web3 Wallet** with supported digital tokens in SG | 20-F · [web3-wallet terms](https://www.grab.com/sg/terms-policies/web3-wallet) |
| Top 3 Markets by Revenue | ✅ **AUDITED FY2025: Malaysia $1,039m (30.8%) · Singapore $727m (21.6%) · Indonesia $715m (21.2%)**. ⚠️ Malaysia is inflated by gross-recognised Jaya/Everrise grocery retail | [20-F Note 19(ii)](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm) |
| Billing channel split (web vs app store) | ⭐ **Neither Apple nor Google IAP is used.** Verified: "In-App Purchases" appears **0 times** on the iOS listing for `id647268330`; "In-app purchases" **0 times** on the Play listing for `com.grabtaxi.passenger` (394 bundle-id occurrences on the page, so not a neighbour-carousel artefact). Grab sells physical services, so IAP does not apply. **The app-store-dominated-revenue override does NOT fire — all of this volume is addressable.** Web vs native **split itself is not disclosed**; it is overwhelmingly native on the evidence of the app footprint | [App Store](https://apps.apple.com/sg/app/grab-app/id647268330) · [Play](https://play.google.com/store/apps/details?id=com.grabtaxi.passenger) |
| Other financial context | Profit for the period **$235m** (Q2'26, incl. a **$307m one-time Superbank gain**); **Adjusted EBITDA $168m**, 18th straight quarter of growth; **gross cash liquidity $7.4bn**, net **$5.4bn**; TTM Adjusted FCF **$450m**; gross loan portfolio **$2,318m (+197%)**; deposits across the three digibanks **$2.5bn**; FY2025 incentives **$1,002m partner + $1,268m consumer**; 2028 targets **$1.7bn Adj. EBITDA, 30%+ revenue CAGR** | [Q2 2026](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000123/a2026q2-earningspressrelea.htm) · 20-F · [Atome Ex-99.1](https://www.sec.gov/Archives/edgar/data/1855612/000185561226000133/exhibit991-atometransactio.htm) |

---

### Overall Research Confidence

**MEDIUM-HIGH** — unusually high for a no-traffic account, and the reason is that Grab is a **NASDAQ registrant**. One downgrade is applied for the missing traffic data, as the method requires; without it this would be High.

**Traffic data was NOT supplied, is NOT API-sourced, and was NOT estimated.** There is none. Section 1 is empty by design. Two ICP rows score 0 as a direct consequence, and both say so in the row.

| Section | Coverage | Why |
|---|---|---|
| **Phase 0 / excluded-industry gate** | 🟢 **Very strong** | Eight independent evidence items, six of them first-party from the 20-F or Grab's own websites. The verdict is stated, not hedged. |
| **1 — Traffic** | ❌ **None** | No data supplied, none obtained, none invented. |
| **1-ALT — Scale & country profile** | 🟢 **Very strong** | **Audited** revenue by geography from an IFRS 8 note, plus four earnings releases and two app-store listings. Better than traffic would have been. |
| **2 — Legal entities** | 🟢 **Strong on names, weak on numbers** | ~20 entities identified from the 20-F and first-party legal pages. **Only one registration number obtained** (201316157E) — no registry was reachable. **Vietnam's operating entity is the real gap.** |
| **3A — PSPs** | 🟢 **Strong at group level, ❌ absent at market level** | Adyen and Stripe named by the issuer itself. **Which acquirer covers which market is the single biggest unknown on this account.** |
| **3B — Orchestrator** | 🟢 **Very strong** | Confirmed three independent ways (filing, live CSP, production bundle). The TAL cell is right and now verified. |
| **4 — APMs** | 🟡 **Medium, and honestly bounded** | The first-party web method catalogue is excellent evidence for the **web**. It is **no evidence at all** for the native apps, which carry the volume. Every absence is labelled accordingly. |
| **5 — Complaints** | 🔴 **Weak** | Trustpilot 403'd; only isolated anecdotes via search summaries. ICP row scored 0 as a result. |
| **6 / 7 — Developments & news** | 🟢 **Very strong** | Eight developments, seven from Grab's own SEC filings with exact dates. |
| **8 — Checkout** | 🟡 **Medium** | Real findings from a real production bundle and five live CSPs, but **no flow was walked and the native app was inaccessible**. |
| **9 — PCI** | 🟡 **Medium** | Scope direction established (wide, first-party) and the integration recommendation follows from it. **No level disclosed.** |
| **11 — Competitors** | 🟡 **Medium** | Strong on TAL peers and on the Uber/inDrive/Rappi orchestration line. **LINE MAN, foodpanda APAC and Sea/Shopee were not researched** — budget went to the target. |
| **12 — Business case** | 🟢 **Strong, with one honest hole** | Audited revenue, GMV, MTUs, segment mix, guidance and the IAP check. **No ATV exists and none was invented**, which is why the transaction count is given as a sourced floor rather than a point estimate. |

---

### Manual Research Recommendations

> **Area:** Which acquirer processes which market (§3A)
> **Why it matters:** The **single highest-value open question on this account.** Grab's 20-F names Adyen and Stripe but not their geographic split. Without it, Insight #1's "reach boundary" is a well-founded hypothesis rather than a specific, named gap — and a specific gap is what makes an enterprise first call land.
> **Suggested manual action:** BIN/acquirer identification from a live app transaction per market (a test ride or small order in SG, MY, ID, TH and VN), plus the Q3 2026 earnings call transcript and Q&A once published. Ask directly on the first call: *"which markets does GrabLink acquire in today, and which still route through a partner?"*

> **Area:** Native-app payment methods per market (§4, §8)
> **Why it matters:** Everything in Section 4 is a **web** finding. The ICP "local rail gap" row is sitting at **0** purely because I cannot evidence app-level absence. If QRIS, PromptPay, FPX, PayNow or GCash genuinely are missing from the app in a top-three market, that row becomes **+3** and the account moves to **20/29**. If they are present — which is more likely — then Section 4's absences should be narrowed to the web surface in any outreach, and Insight #3 must stay a question.
> **Suggested manual action:** VPN + mitmproxy on the native Grab app in MY, SG and ID. Screenshot the method list per market.

> **Area:** Taiwan — current TFTC status and the actual Taiwanese rail set (§6, Insight #2)
> **Why it matters:** Insight #2 is the strongest merchant-side angle in this report and it is **time-boxed by a regulator**. The last status I could evidence is **18 Aug 2026 (undecided)** — nearly two months before this report date — and it came from a **search summary, not a fetched page**. I also did **not** research Taiwanese rails or licensing live, and I will not cite them from memory.
> **Suggested manual action:** check the TFTC's own announcements and Grab's Q3 2026 6-K before any Taiwan email goes out. Separately, source the Taiwanese rail set and e-money licensing live. **Do not name a Taiwanese rail to Grab until that is done.**

> **Area:** MAS licence classes held by **GPay Network (S) Pte Ltd** (§2, Phase 0)
> **Why it matters:** This is what would make the Phase 0 verdict airtight rather than strongly evidenced. If GPNS holds a **merchant acquisition** licence class under the PS Act, the excluded-industry gate is beyond argument and the Partnerships route is settled.
> **Suggested manual action:** MAS Financial Institutions Directory (`eservices.mas.gov.sg/fid`) — it was an unreachable SPA in this environment but works in a normal browser. Search both "GPay Network" and "GrabPay".

> **Area:** The Vietnamese licensed entity behind `paysuite.moca.vn` (§2)
> **Why it matters:** Vietnam is 7.6% of audited revenue and the **only** material market where I could not name the operating entity. "Moca" appears **zero times** in the 20-F, so the identification rests entirely on Grab's own production assets. Vietnam also gates intermediary payment gateway services behind an SBV licence, which makes the entity question substantive rather than cosmetic.
> **Suggested manual action:** Vietnamese National Business Registration Portal for "Moca"; cross-check against the SBV's published list of licensed intermediary payment service providers.

> **Area:** Complaint frequency (§5)
> **Why it matters:** The ICP row scores **0** only because Trustpilot returned 403 and search surfaced nothing systematic. If there is a real pattern — particularly the **3DS-on-new-cards** failure one reviewer described — that row becomes **+2** and it becomes a concrete, non-generic hook.
> **Suggested manual action:** read Trustpilot and Google Play reviews directly in a browser, filtered to 2026 and to payment keywords, per market. Note that Grab's **own PaySDK owns the 3DS path**, so a 3DS complaint points at their code, not an acquirer's.

> **Area:** GrabPay third-party-merchant TPV (§12, Insight #4)
> **Why it matters:** It sizes the Partnerships opportunity. Grab discloses Financial Services *revenue* ($134m in Q2'26) but **no payments volume at all**.
> **Suggested manual action:** MAS annual e-money statistics; Bank Indonesia and BSP e-money aggregates; Grab earnings-call Q&A.

---

### Appendix: All Source URLs

**SEC / first-party filings (primary)**
- https://data.sec.gov/submissions/CIK0001855612.json (filing index)
- https://www.sec.gov/Archives/edgar/data/1855612/000185561226000020/ck0001855612-20251231.htm (**20-F FY2025**, filed 6 Mar 2026)
- https://www.sec.gov/Archives/edgar/data/1855612/000185561226000123/a2026q2-earningspressrelea.htm (Q2 2026 results, 4 Aug 2026)
- https://www.sec.gov/Archives/edgar/data/1855612/000185561226000123/a6-kxearningsrelease2026q2.htm (Q2 2026 6-K)
- https://www.sec.gov/Archives/edgar/data/1855612/000185561226000077/a42026q1-earningspressrele.htm (Q1 2026 results, 5 May 2026)
- https://www.sec.gov/Archives/edgar/data/1855612/000185561226000011/a2025q4-earningspressrelea.htm (Q4 2025 results)
- https://www.sec.gov/Archives/edgar/data/1855612/000185561226000133/exhibit991-atometransactio.htm (**Atome**, 15 Sep 2026)
- https://www.sec.gov/Archives/edgar/data/1855612/000185561226000133/a6-kxatometransactionannou.htm (Atome 6-K)
- https://www.sec.gov/Archives/edgar/data/1855612/000185561226000051/a6-kxgarnetannouncement.htm (**foodpanda Taiwan $600m**, 23 Mar 2026)
- https://www.sec.gov/Archives/edgar/data/1855612/000185561226000085/a6-kxsuperbankconsolidatio.htm (Superbank consolidation, 20 May 2026)
- https://www.sec.gov/Archives/edgar/data/1855612/000185561226000097/a6-kxgrabcompletionofstash.htm (Stash completion, 1 Jul 2026)
- https://www.sec.gov/Archives/edgar/data/1855612/000185561226000009/a6-kxsapphiretransactionan.htm (Stash agreement, 12 Feb 2026)
- https://www.sec.gov/Archives/edgar/data/1855612/000185561225000063/a6-kxvaytransactionannounc.htm (Vay investment, 10 Nov 2025)
- https://www.sec.gov/Archives/edgar/data/1855612/000185561226000114/a6-kxboardupdate.htm (Khosrowshahi board departure, 6 Jul 2026)

**Grab first-party web properties**
- https://www.grab.com/sg/ (CSP: `frame-ancestors` splytech.io)
- https://www.grab.com/sg/merchant/checkout-solutions/ (**GrabPay/PayLater merchant acceptance, SG; Key Partners roster**)
- https://www.grab.com/my/merchant/checkout-solutions/ (**same, MY; current Dec-2025 partner roster; GrabPay DuitNow QR**)
- https://www.grab.com/sg/consumer/finance/pay/ · https://www.grab.com/th/consumer/finance/pay/
- https://www.grab.com/sg/terms-policies/ · https://www.grab.com/sg/terms-policies/privacy-notice/
- https://www.grab.com/sg/terms-policies/paylater (**GPay Network (S) Pte Ltd; GFin Services (S) Pte. Ltd.; BNPL Code of Conduct status**)
- https://www.grab.com/sg/terms-policies/web3-wallet (**GrabTaxi Holdings Pte Ltd, Company No. 201316157E**)
- https://food.grab.com/ + its `/_next/static/**` chunks (**the payment method catalogue, PaySDK, 3DS error codes**)
- https://merchant.grab.com/en-my (**CSP asset map**)
- https://paysuite.grab.com/ · https://paysuite.moca.vn/ · https://pay.grab.com/ · https://paysdk-web.grab.com/ (**live CSP headers**)
- https://book.grab.com/ · https://express.grab.com/ (SPA shells)
- https://help.grab.com/passenger/en-sg/ (**soft-404, 1,316 bytes, identical to a nonsense path — unusable**)
- https://developer.grab.com/docs/grabpay/ + `/static/js/app.4e437f56.js` (**client-rendered shell; all vendor hits were Font Awesome / Ant Design icons and Chart.js — no payment content**)
- https://www.grab.careers/en/jobs/?search=payments (**seven live payment openings**)

**App stores**
- https://apps.apple.com/sg/app/grab-app/id647268330 (4.8/5, 252k ratings, GRABTAXI HOLDINGS PTE. LTD., **no IAP flag**)
- https://play.google.com/store/apps/details?id=com.grabtaxi.passenger (**100M+ downloads, no IAP flag**)

**Third-party**
- https://www.adyen.com/en_SG/knowledge-hub/grabpay-enabling-smoother-payments-in-southeast-asia (18 Sep 2019 — GrabPay as infrastructure; Adyen as distribution partner)
- https://www.taiwannews.com.tw/en/news/6393766 (2 Jul 2026 — TFTC filed 27 Mar 2026; Uber ~13.5% stake per CNA; Uber-control question)
- https://www.taipeitimes.com/News/biz/archives/2026/04/03/2003854926 (fetched; no usable content extracted)
- https://www.mlex.com/articles/2514542 (18 Aug 2026, TFTC undecided — `[UNVERIFIED — search summary only, page not fetched]`)
- https://www.trustpilot.com/review/grab.com (**HTTP 403 — not readable**)
- https://b2b-cambodia.com/news/milestone-in-digital-integration-aba-and-grab-advance-cashless-ecosystem-in-cambodia (3 Sep 2025 — Grab Cambodia on ABA PayWay + ABA driver payouts; ⚠️ **reused from `tada-mobility.md`, not re-fetched in this run**)
- https://www.newswire.com/news/ryde-advances-ryde-2-0-with-ai-powered-mobility-ev-fleet-technology-and-next (Ryde 2.0 payments programme — reused from `tada-mobility.md`)

**Yuno**
- https://y.uno/en (site-wide customer logo set, verified live 2026-10-13: **zero occurrences of "grab"**)
- https://y.uno/en/success-stories/indrive · https://y.uno/success-cases/rappi

**Repo**
- `accounts/apac-tal.csv` (Grab row; peers Gojek, GoTo, foodpanda, EASI, LINE MAN, Lalamove, TADA, Ryde, Maxim, Didi, Ola, Rapido, Pathao, Kakao Mobility, Baemin, Coupang Eats, Deliveroo HK, J&T Express)
- `2-ready-to-outreach/tada-mobility.md` (competitive intel reused: Grab Cambodia / ABA, Ryde, ComfortDelGro, Uber/inDrive orchestration line)
- `.claude/reference/apac-payments.md` (**checklist only — nothing in this report is stated as fact on its authority**)


## Rejection Rationale

**Phase 0 payment-infrastructure gate fired, on primary-source evidence.** Grab's own audited FY2025 Form 20-F describes **GrabLink** as *"our in-house PCI-compliant secure payment gateway and acquiring service **licensed under the Payments Services Act of Singapore**"*, and the same filing twice refers to *"a **major payment institution such as Grab**"* under a PS Act whose regulated services expressly include **merchant acquisition service**. Grab also sells GrabPay and PayLater acceptance to third-party merchants with a Direct API, e-commerce plugins, tokenisation and settlement. `CLAUDE.md` excludes PSPs and payment-infrastructure companies, and the `/research` Phase 0 table auto-rejects a PSP, gateway, acquirer or orchestrator. All three descriptions fit.

**Routed to Partnerships, not rejected as worthless.** By its own filing Grab remains a *buyer* of third-party acquiring — Adyen and Stripe sit behind $22.1bn of FY2025 GMV and Grab says it *"will likely continue to rely on"* them. The GrabPay/PayLater-as-connector motion is real and the research is preserved in full for that conversation. **No cold SDR sequence should run on this account**, and any merchant-side approach needs Partnerships' knowledge first.

⚠️ **Reversible.** Prateek raised the Phase 0 question before the run and chose to research anyway; this records the answer. If he judges the merchant side separable from the licensed-acquirer side, moving this back is a one-line change and the evidence stands either way.

</details>
