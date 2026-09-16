# YesStyle

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 19 / 24 → ⭐ High Priority — earned on arithmetic, no override needed
**Industry:** Cross-border e-commerce (Asian beauty & fashion) · **HQ:** 5/F KC100, 100 Kwai Cheong Road, Kwai Chung, Hong Kong · **Researched:** 2026-09-16 · **First email sent:** —
**Motion:** **Greenfield** — multiple gateways, directly integrated, no routing layer. They pick the gateway; the gateway picks the acquirer.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** YesStyle is the flagship B2C platform of **YesAsia Holdings Limited (HKEX: 2209)**, a Hong Kong-listed cross-border retailer shipping Asian beauty and fashion to **over 50 countries**. FY2025 group revenue **US$501,544,000** (+45.0%), net profit US$23,140,000. YesStyle Platforms alone did US$347,479,000 across **2,855,000 customers** at an average order of **US$65.1**. Because the parent is listed, this account has something no other file in this repo has: **an audited, itemised cost of acceptance.**

**SimilarWeb total visits (last full month):** 15.1M — but the page labels this "last 3 months combined", so treat as ambiguous `[ESTIMATE, not confirmed]`. **Traffic is not used for geography in this report** — only 5 countries are public and 47.66% sits in an undifferentiated "Others". **The audited revenue-by-country table in Section 1 is far better and is used instead.**

### Top 5 markets *(by audited FY2025 revenue, not traffic)*
| Rank | Country/Bloc | Revenue | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | **EU bloc** | **US$156,709k · 31.2%** | Cards, PayPal, Apple Pay/Google Pay (Braintree), **iDEAL** (NL only), **BLIK + P24** (PL only) | **Bancontact, SOFORT/giropay, SEPA, Cartes Bancaires, Klarna-native — all SOURCED ABSENT** | ❌ none — 3PL warehouse (Germany) only |
| 2 | **United States** | **US$102,925k · 20.5%** | Cards, PayPal, Apple Pay, Google Pay, **PayPal Pay in 4** (possibly retired) | **Affirm, Afterpay, Klarna, Shop Pay — SOURCED ABSENT** | ⚠️ 30% dormant associate only (Candy Doll YS LLC); 3PL near LA; **first physical store opened May 2026** |
| 3 | **South Korea** | **US$37,650k · 7.5%** | Visa, MC, Amex, JCB, Google Pay | **KakaoPay, Naver Pay and local card PG — SOURCED ABSENT**, despite two Korean entities and a warehouse | ✅ YesAsia.com (Korea) Ltd + ABW Korea Inc + 147,000 sq ft warehouse |
| 4 | **Hong Kong** *(home)* | **US$35,146k · 7.0%** | Cards, **PayMe, FPS, Tap & Go, Octopus**, Direct Deposit/Check — the richest method set anywhere | — | ✅ HQ + 2 robotics warehouses |
| 5 | **Canada** | **US$30,811k · 6.1%** | Cards, PayPal, Apple Pay, Google Pay | — | ❌ none |

*Also disclosed: UK US$29,769k (5.9%), **Mexico US$17,776k (3.5%)**, Australia US$14,424k (2.9%), UAE US$13,327k (2.7%), Others US$63,007k (12.6%).*

**Named APAC revenue (South Korea + Hong Kong + Australia) = US$87,220k = 17.4%.** Real, but the business is overwhelmingly outbound to non-APAC markets. **HQ is Hong Kong, so the buying centre sits squarely in territory.**

### Legal entities
- **YesAsia Holdings Limited** — incorporated in **Hong Kong**, HKEX **2209**. Principal bankers HSBC and Standard Chartered
- **YesStyle.com Limited** (Hong Kong) — the contracting entity, 100% indirectly held, issued capital HK$1
- **YesAsia.com. Japan Kabushiki Kaisha** (Japan) · **YesAsia.com (Korea) Limited** (South Korea) · **AsianBeautyWholesale Korea Inc.** (South Korea) · **廣州喆麗科鑠電子商務有限公司** (Mainland China, **70%**) · YesAsia.com Ltd, ABW (HK) Ltd, YA Logistics Ltd (Hong Kong)
- **No US, UK or EU operating subsidiary.** US presence is a 30% dormant associate plus outsourced 3PL (LA, Sheffield, Hahn). **85.6% of non-current assets sit in Hong Kong**

### Known PSPs
- **PayPal** — ✅ **confirmed and named**, and the relationship dates to **2000**. PayPal's own newsroom: *"In 2000, PayPal partnered with YesAsia as its global payments platform."* CEO fronted a PayPal partnership video as recently as 30 Jul 2026
- **Apple Pay, Google Pay, Alipay** — named in the IPO prospectus / dedicated help pages
- **OXXO (Mexico cash voucher)** — dedicated help page exists `[UNVERIFIED — page 403]`
- **Binance Pay / USDT** — accepted since Aug 2023 `[UNVERIFIED]`
- **CyberSource** — fraud/decisioning layer `[UNVERIFIED — search summary only]`
- **Braintree (PayPal-owned)** — ✅ **confirmed as the wallet gateway.** Their own help-page JSON uses the constants **`GOOGLEPAY_BRAINTREE`** and **`APPLEPAY_BRAINTREE`**
- **Reach (withreach.com)** — ✅ **confirmed present in the card flow**, via a bank-statement descriptor on YesStyle's own credit-card help page: *"in some cases… a different name may be listed (e.g., **CKO Withreach.com** or **Withreach.com**)."* **Reach is a cross-border merchant-of-record and local-acquiring provider.** Note the wording: *"usually YESSTYLE… in some cases"* — so Reach is an **exception path, not confirmed as the primary acquirer**
- **CyberSource (Visa-owned)** — ✅ **confirmed as the fraud-screening vendor**, named verbatim on the same page. **It replaced Retail Decisions between Feb 2014 and Sep 2017** — proof they actively change payment-chain vendors
- **HSBC Hong Kong** — the Direct Deposit help page names an HSBC Hong Kong account in the name of **YESSTYLE.COM LIMITED**
- ⚠️ **The raw-card acquirer is still never named**, in 606 pages of prospectus or three annual reports. Their own help page calls it only *"an international payment gateway"*. A grep of all archived pages for Adyen, Stripe, Checkout.com, dLocal, EBANX, Nuvei, Worldpay, CyberSource, Conekta, Openpay and Airwallex returned **only Braintree**

### Orchestration status
**None detected — direct integrations to multiple gateways (greenfield).** `orchestrat*` appears **0 times** in the 606-page IPO prospectus and 0 times in the FY2023/24/25 annual reports; no hits against Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY or Yuno.

> ⚠️ **Caveat on the record:** the architectural detail comes from the 2021 IPO prospectus describing 2018–2020 operations, when revenue was roughly a quarter of today's. "None detected" means *no orchestrator found up to 2021 and nothing since to contradict it* — **not a verified 2026 greenfield.**

### Buying signals
- 💼 **Tim Wang appointed General Manager, U.S. on 28 Aug 2026** — three days before reporting a US revenue decline. Plus Gary Chow as VP Operations
- 🚀 **First US physical store**, Great Mall, Milpitas CA (May 2026) — adds card-present to a pure-play online stack
- 🚀 **Latin America grew +224% in FY2025 and +178% in H1 2026**; Mexico alone is US$17.8m and already **exceeded its full-year FY2025 figure within H1 2026**
- 🇧🇷 **Brazil is billed in USD, so every Brazilian shopper pays 3.5% IOF on top** (Decreto 12.499/2025, verified at Planalto). **Pix is sourced-absent from their checkout *and* from Reach's entire 38-method set.** Full sizing in **Section 13**
- 📉 **US revenue fell 17.6% YoY in H1 2026** against a record group half (+23.2%) — the **US de minimis exemption ended 29 Aug 2025** and the CEO has spoken publicly on tariff impact
- 📋 **No public payment RFP found.** **No payments job posting found** — though a "Finance Transformation" role leading global accounting operations is open

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach YesStyle` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 16 / 24
| Signal | Points | Status |
|--------|--------|--------|
| Orchestration status | **+4 ✅** | **None detected — greenfield.** `orchestrat*` = 0 across a 606-page prospectus and three annual reports; no vendor hits anywhere. Caveat on vintage recorded above |
| 3+ countries | **+3 ✅** | Audited revenue above 1% in **13+ countries**: US 20.5%, France 8.8%, South Korea 7.5%, Hong Kong 7.0%, Canada 6.1%, UK 5.9%, Germany 5.4%, Mexico 3.5%, Spain 3.3%, Italy 3.0%, Australia 2.9%, UAE 2.7%, Netherlands 1.7%, Poland 1.6%, Belgium 1.0%. Plus operating subsidiaries in 4 jurisdictions |
| Multiple PSPs | **+3 ✅** | **"payment gateway companies" — plural — 10 times in the prospectus**, 9 uses of "payment gateways", and the FY2023 audited receivables note uses the plural too. PayPal named separately |
| Local rail or licensing gap in a top-3 market | **+3 ✅** | **Two enumerated lists were recovered from archived snapshots**, so absences here are genuinely sourced. **South Korea is the #3 market at 7.5% of revenue (US$37.7m) and the KRW row enumerates Visa/MC/Amex/JCB/Google Pay only — KakaoPay, Naver Pay and local card PG are SOURCED ABSENT**, despite two Korean subsidiaries and a 147,000 sq ft Korean warehouse that would permit local acquiring. Germany (5.4%) likewise has no giropay, SOFORT or SEPA |
| Recent expansion | **+2 ✅** | First US physical store (May 2026); Korean warehouse operational Apr 2025; ABW Korea sales office Jan 2025; Polish added as a 9th site language Jul 2025; Madrid pop-up Jul 2026; ABW Offline revenue went US$1,088k → US$49,935k |
| Payment issues reported | **+2 ✅** | Moderate. **9 of 20 fetched 1–2★ Trustpilot reviews are payment/refund related**, all dated ~10–16 Sep 2026; 7,184 one-star reviews in total |
| Funding >$10M | **0 ❌** | Listed company, no round. A share repurchase programme is running |
| High traffic outside home | **+2 ✅** | Home market Hong Kong is **7.0% of revenue** — far below the 60% threshold. Company's own framing: "Non-core markets" = **63.6% of FY2025 revenue, +83.9% YoY** vs core +5.9% |
| Competitor using orchestration | **0 ❌** | Explicit negative — no competitor in the Asian-beauty cross-border set is confirmed on any orchestration layer |
| Payment job postings | **0 ❌** | None found |

**Tier: ⭐ High Priority (19).** **No analyst override applied**, and the override criteria were checked explicitly:
- *App-store dominated?* **No.** App revenue is US$178,681k (35.6% of group revenue) but this is their **own app with their own checkout**, not Apple/Google IAP. Orchestration reaches all of it
- *Volume too small?* **No.** US$501.5m revenue, ~5.34M orders/year, US$11.16m of annual gateway spend
- *Double-counting?* **No.** "Multiple PSPs" rests on prospectus language; "3+ countries" on the audited geography note. Independent
- *Regulatory blocker?* **No**

### Source Notes

**✅ Verified first-hand by me — the strongest evidence base in this repo:**
- **The 606-page IPO prospectus and the FY2025 annual report and H1 2026 interim were downloaded and text-extracted directly.** Nearly every number below is audited, not estimated
- **Payment gateway charges, five-year series:** FY2022 2.6% · FY2023 2.6% · FY2024 **2.5%** · FY2025 **2.2%** · H1 2026 **2.1%** of revenue
- **Net exchange losses:** FY2024 US$2,541k (0.7%) · FY2025 **US$4,886k (1.0%, +92.3%)** · H1 2026 **US$3,296k (1.1%, +51.9%)**
- **The FX causal sentence**, verbatim and repeated in both filings: *"increase in net exchange losses due to **more payments settled by our payment gateway** as a result of revenue increase"*
- **Who does the FX**, verbatim: *"The E-commerce customers of the Group generally settle their invoices **using their designated currencies** upon checkout via secure payment gateways, and the fund is generally transferred to the Group's account in **Hong Kong Dollar and US Dollar upon currency conversion**"*
- **The self-hedge mechanism**, verbatim from the prospectus: *"we adopt **internal currency rates** for customers who checkout with currencies other than U.S. dollars. Such internal rates are determined by our Group according to the exposure of foreign currency rate, **the cost to payment gateway**… to maintain a **premium over the market rates to hedge against possible currency exchange losses resulted from payment gateways currency conversion**"*
- **No hedging policy**, stated in the prospectus and repeated in both 2026 filings: *"Currently, we do not have a formal foreign currency hedging policy."*
- **Settlement lag**, verbatim: *"These platforms typically **settle the amounts received, net of handling charges, within one month after the trade date**"*
- **Float trapped at PSPs:** trade receivables from third-party payment platforms US$2,298k + other receivables US$2,695k = **US$4,993k** at FY2025; **US$7,578k** by H1 2026
- **The architecture**, verbatim: gateway *"will later process the transaction through an acquiring bank or payment provider depending on the location of customer and payment type"*; *"standard agreements with payment gateway companies… without fixed term"*; fee *"generally calculated on a **per country and/or per currency basis**"*
- **`orchestrat*` = 0 and `PCI` = 0** across all 606 prospectus pages
- **PayPal since 2000** — verified by my own fetch of PayPal's APAC newsroom

**⚠️ CORRECTION — my own error, issued and corrected mid-run:**
I initially reported that "payment gateway" was **singular with zero plural uses** in both 2026 filings, and floated a single-PSP dependency on that basis. **That was wrong, and it was a measurement artifact:** my regex ran against raw PDF text where a line break split "secure payment / gateways", so the plural was missed. Corrected counts (whitespace-normalised) show **"payment gateway companies" ×10** and **"payment gateways" ×9** in the prospectus, plus the plural in the FY2023 audited receivables note. **The singular appears only in recycled MD&A boilerplate** carried forward verbatim from FY2023. **This is a multi-gateway merchant, and the pitch must not claim single-PSP dependency.**

**✅ Recovered from archived snapshots (Wayback), after Cloudflare blocked the live pages:**
- **The `helpCurrencies` JSON matrix** — 36 currencies each with an explicit method array, plus the display map `{"AMEX","MASTER","PAYPAL","JCB","VISA","GOOGLEPAY_BRAINTREE","CHECK_MONEY","APPLEPAY_BRAINTREE","PAY_ME"}`. Snapshot dated **2026-09-11**
- **The "About Payment" help index** — the complete local-method inventory, **verified identical in English and German**
- **Braintree identified as the wallet gateway** from those constants — the first time any gateway is named for this merchant in any source
- These are **archived copies of public help documentation**, not a bypass of a live control. The live URLs were left alone after they returned 403

**✅ Added by a dedicated deep-research pass (102 agents, 3-vote adversarial verification):**
- **Reach (withreach.com) is in the card flow** — descriptor *"CKO Withreach.com"* on their own help page, verified across 12 archived captures. **Non-circularly corroborated**: HobbyLink Japan, an unrelated merchant, independently tells its customers they may see *"CKO WithReach"* when paying through Reach — so the string is a real Reach descriptor, not a YesStyle typo
- **CyberSource named as the fraud vendor**, having **replaced Retail Decisions between Feb 2014 and Sep 2017** (the original "fraudlent" typo carries across both versions, which is how the swap was dated). **They change payment-chain vendors deliberately** — a useful precedent to cite
- **No help-page evidence of a card re-platform 2018 → Mar 2026**, which substantially resolves the vintage caveat on the Greenfield classification
- **HK rails are currency-gated, not destination-gated** — pay in HKD and you can use them shipping anywhere

**⚠️ Carried caveats on the Reach finding — do not overstate it:**
- The **"Withreach" half is direct evidence**; the **"CKO = Checkout.com" half is one inferential step.** Reach's own descriptor documentation lists only GIP, RCH, Reach, GoInterpay and Calforex as its prefixes, and **"CKO WithReach" appears nowhere in Reach's docs**
- YesStyle's own wording is *"usually YESSTYLE… **in some cases**"*, so **Reach is an exception path. It is NOT established as the primary or sole card acquirer**, and the acquirer carrying the bulk of card volume remains unnamed in every source examined
- The reason YesStyle gives (*"the transaction may be controlled by your credit card company"*) is **technically wrong merchant boilerplate** and cannot be used to infer routing logic

**❌ A third fabrication caught and killed by the deep-research pass:**
- **"YesStyle cooperates with Przelewy24."** A search-engine AI summary asserted this with no underlying source; the only real przelewy24.pl case study concerns an unrelated Dotpay migration. The **Polish-language** help page was cross-checked directly — PayPro 0, Adyen 0, Stripe 0, PayU 0, *"operator płatności"* 0 — so the absence is not an English-localisation artifact. **The BLIK/P24 provider is genuinely unestablished**

**❌ Two fabrications caught and killed — both would have been damaging:**
1. **"YesStyle Brazil accepts Visa, Mastercard, Elo, Amex, Boleto and Pix, with a 2-hour Pix code expiry."** Entirely false — the detail was scraped from **`countrystyle.com.br`, an unrelated Brazilian retailer**, and conflated with YesStyle. The authoritative currency matrix has **no BRL at all**. Had this reached an email it would have been a **direct factual inversion of the real gap**
2. **"YesStyle accepts Klarna."** It does not, natively. Klarna's store-directory page reflects Klarna's **one-time virtual card**, which functions at any merchant that takes cards. **A Klarna merchant-directory listing is never evidence of an integration**

**⚠️ Deliberately excluded — claims I could not verify:**
- **"~US$6.0m of revenue given up in one Track Record year"** to the internal-rate premium. An agent reported it; **I searched the prospectus passage and could not find it. Not used.**
- **All BNPL evidence.** Sources directly contradict each other and the aggregators are auto-generated junk — one lists "Barclaycard" and "Revolut" as payment methods and marks PayPal "not confirmed". **Klarna merchant-directory pages are not evidence of integration**, because Klarna's app-generated one-time card works at any card-accepting merchant. **Do not put BNPL in outreach**
- **No customer-side FX complaint was found.** The FX story is sourced from filings and their own policy pages only; **do not assert customer FX pain**
- **CyberSource** — search-summary only, appears in no filing
- **Stylevana's regional rails.** A summary claimed iDEAL/GCash/Alipay; the fetched official support article lists only cards, Apple Pay, Google Pay and PayPal. **Do not use the richer list**
- **HK Companies Registry numbers** for YesStyle.com Limited come from a third-party directory, not ICRIS
- One summary claimed **"US 75.91% of traffic"**; the fetched SimilarWeb page says **33.73%**. Discarded

**⚠️ Trustpilot — do not quote the rating.** TrustScore **4.3/5 across 102,574 reviews** with no manipulation flag displayed, **but** YesStyle runs a dedicated help page titled *"Rate on Trustpilot"* soliciting reviews as a support flow. The distribution is a solicited barbell (71% five-star, 7% one-star). **Cite individual dated 1★ reviews only; never the headline score.**

### Success Case Alternatives
- **Livelo** — decline-cascade and secondary-acquirer recovery (+5% approval, 50% of failed transactions recovered). Best fit if discovery shows declines with no failover. Brazil, loyalty/retail — a pattern match, say so
- **Rappi** — provider breadth and zero implementation delay. Fits "every new rail is a separate gateway conversation"
- **inDrive** — multi-country scale, ~90% approval, 10 new countries in under 8 months. **The closest shape**: many markets, one platform
- **McDonald's / Arcos Dorados** — unified processing across 21 countries. No public link
- ⚠️ **LATAM relevance is unusually high here and worth using honestly.** YesStyle's fastest-growing region is exactly where Yuno's case library is strongest. Name the region and what each case did; **never imply LATAM results came from Asia**

---

## Executive Summary

YesStyle is the B2C flagship of HKEX-listed YesAsia Holdings — **US$501.5m FY2025 revenue (+45%)**, 2.86m customers, US$65 average order, shipping to 50+ countries from Hong Kong. Because the parent is listed, **their cost of acceptance is public and audited**: payment gateway charges of **US$11.16m (2.2% of revenue)** and net exchange losses of **US$4.89m (1.0%, up 92.3%)**, which the filings attribute directly to *"more payments settled by our payment gateway"*. They run **multiple gateways with no routing layer** — they choose the gateway, and the gateway then chooses the acquiring bank by country and payment type, pricing *"on a per country and/or per currency basis"*. The motion is **greenfield**, the buying centre is in Hong Kong, and the sharpest opening is FX and routing rather than rate — because they are already winning on rate.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** WebSearch fallback (path 3) — no data supplied, no MCP tool. **`[ESTIMATE, not confirmed]`.** The SimilarWeb page was fetched.

| Rank | Country | Traffic Share | Source |
|---|---|---|---|
| 1 | United States | 33.73% | [SimilarWeb](https://www.similarweb.com/website/yesstyle.com/) ✅ fetched, Aug 2026 |
| 2 | Canada | 6.27% | same |
| 3 | South Africa | 4.20% | same |
| 4 | United Kingdom | 4.13% | same |
| 5 | Brazil | 4.01% | same |
| — | Others (undifferentiated) | **47.66%** | same |

Global rank #2,680; #14 in Lifestyle > Beauty and Cosmetics (US); +7.38% MoM. Total visits 15.1M, **but the page labels this "last 3 months combined"** — treat as ambiguous.

> **Traffic is NOT used for geography in this report.** Only five countries are public, **none of them APAC**, and 47.66% is an unbroken "Others". Any APAC traffic share would be invented. The audited revenue-by-country table in Section 12 is used instead — it is better in every respect.

**Note Brazil at 4.01% of traffic**, consistent with the audited +224% LatAm revenue growth.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** 5/F., KC100, 100 Kwai Cheong Road, Kwai Chung, New Territories, Hong Kong. CEO Lau Kwok Chu; CFO/Company Secretary Ng Sai Cheong; auditor RSM Hong Kong.

| Country | Entity | Capital | Held | Activity |
|---|---|---|---|---|
| **Hong Kong** | YesAsia Holdings Limited (HKEX 2209) | — | Parent | Listed holding company |
| **Hong Kong** | **YesStyle.com Limited** | HK$1 | 100% indirect | *"Trading of fashion wears, cosmetics and accessories"* — the contracting entity |
| Hong Kong | YesAsia.com Limited | HK$39,000,002 | 100% direct | Trading + investment holding |
| Hong Kong | AsianBeautyWholesale (HK) Ltd · YA Logistics Ltd | HK$1 each | 100% indirect | Beauty wholesale / logistics |
| **Japan** | YesAsia.com. Japan Kabushiki Kaisha | JPY10,000,000 | 100% direct | Trading |
| **South Korea** | YesAsia.com (Korea) Limited | KRW50,000,000 | 100% indirect | Trading |
| **South Korea** | AsianBeautyWholesale Korea Inc. | KRW100,000,000 | 100% indirect | Beauty products |
| **Mainland China** | 廣州喆麗科鑠電子商務有限公司 | RMB2,010,000 | **70%** indirect | Beauty wholesale |
| United States | Candy Doll YS LLC (associate) | US$500,000 | **30%** | *"business not yet commenced"* |

*No registration numbers appear in any filing. CR 1038244 / BR 36773655 for YesStyle.com Limited come from a third-party directory — **verify at ICRIS before quoting**.*

**Cross-Border Gap Analysis**

| Country | Top-10 revenue? | Local entity? | Domestic acquiring gated? | Cross-border risk? |
|---|---|---|---|---|
| **EU bloc (31.2%)** | ✅ #1 | ❌ none (3PL Hahn only) | No | **High — every EU sale is cross-border acquired** |
| **United States (20.5%)** | ✅ #2 | ⚠️ dormant 30% associate | No | **High** |
| South Korea (7.5%) | ✅ #3 | ✅ two entities + warehouse | Local acquiring is entity-gated — they have entities | Low |
| Hong Kong (7.0%) | ✅ #4 | ✅ HQ | No | None |
| Canada (6.1%) / UK (5.9%) | ✅ | ❌ (3PL Sheffield in UK) | No | **High** |
| **Mexico (3.5%)** | ✅ | ❌ | No | **High — and the fastest-growing market** |

> **Warning: potential cross-border operation across the entire European bloc, the US, Canada, the UK and Mexico — together roughly 67% of revenue. No local entity exists in any of them.** Transactions are likely processed cross-border, with higher scheme costs, lower approval rates and FX exposure. **This is not speculation here — the FX exposure is quantified in their own audited accounts at US$4.886m for FY2025.**

**The unusual shape of this account:** 85.6% of non-current assets sit in Hong Kong while ~83% of revenue comes from outside it. Operationally Hong Kong, commercially global. **That is exactly why the buying centre is in Prateek's territory even though the customers are not.**

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Market/Rail | Provider | Evidence Type | Source |
|---|---|---|---|
| Global wallet | **PayPal** — since **2000** | `[Press Release]` + `[Prospectus]` | [PayPal APAC newsroom](https://newsroom.apac.paypal-corp.com/How-one-Hong-Kong-merchant-is-bringing-Asian-pop-culture-to-the-world) ✅ fetched |
| Global wallets | **Apple Pay, Google Pay** | `[Prospectus]` p.219 + help page | IPO prospectus ✅ extracted |
| China / cross-border | **Alipay** | `[Terms/Help]` | help page hsi.862 `[UNVERIFIED]` |
| **Mexico** | **OXXO** cash voucher | `[Terms/Help]` — high section ID, recently added | help page hsi.2714 `[UNVERIFIED]` |
| Global crypto | **Binance Pay / USDT** | `[Press Release]`, Aug 2023 | binance.com `[UNVERIFIED]` |
| **Card flow (some transactions)** | **Reach (withreach.com)** — cross-border **merchant of record** + local acquiring | `[Terms/Help]` — bank-statement descriptor, verified across 12 archived captures | yesstyle.com/en/credit-card help page |
| Fraud / decisioning | **CyberSource** (Visa-owned) | `[Terms/Help]` — named verbatim, first-party | same page |
| Bank account (Direct Deposit) | **HSBC Hong Kong**, account in the name of YESSTYLE.COM LIMITED | `[Terms/Help]` | Direct Deposit help page |
| **Primary card acquirer** | **STILL NEVER NAMED** | — | their own help page says only *"an international payment gateway"* (singular, on the card page) |

**Zero hits** across the 606-page prospectus and FY2023/24/25 annual reports for: Adyen, Stripe, Checkout.com, Worldpay, Braintree, Global Payments, AsiaPay, PayDollar, Oceanpayment, Airwallex, PingPong, LianLian, WorldFirst, dLocal, EBANX.

**The architecture — verbatim from the prospectus, and the most useful paragraph in the whole file:**

> *"…an acquiring bank or payment provider **depending on the location of customer and payment type**. Upon receiving the remittance from the payment provider in the currency the transaction was submitted, the payment gateway company will remit the funds, **net of processing fees**, to our account upon our request and **in our designated currencies**. We typically enter into **standard agreements with payment gateway companies… without fixed term**. The payment gateway company charges an agreed processing fee on all successful transactions it processes, which is **generally calculated on a per country and/or per currency basis**."*

Three things matter for the pitch:
1. **They pick the gateway; the gateway picks the acquirer.** Acquirer-level routing is delegated, not controlled
2. **"Standard agreements without fixed term"** — low switching friction, nothing to unwind
3. **Pricing is per-country and per-currency** — they already think in country-level payment economics, which is the frame orchestration sells in

Also: *"Our cash rebate or incentive income represents amounts received from **payment gateways and credit card service providers**"* — they already negotiate volume rebates. This is a commercially sophisticated payments buyer, not a naive one.

#### 3B. Payment Orchestrator

**None detected — direct integrations to multiple gateways (greenfield).**

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with PSP(s), which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

`orchestrat*` = **0** across 606 prospectus pages and three annual reports. No vendor hits. No internal payments platform named. No payments engineering hire found.

> **The vintage caveat is now substantially resolved — this was the biggest weakness in the classification and it has been tested directly.**
> A dedicated deep-research pass pulled every archived capture of the credit-card help page. The bank-statement descriptor paragraph naming **Reach** is **absent from the 25 Jan 2018 snapshot, present from 29 Jul 2020, and character-for-character identical across all 12 subsequent 200-status captures through 3 Mar 2026** (MD5 of the 700-byte window is stable across each era, differing only in surrounding template markup and one trailing space).
>
> **Two consequences:** the Reach arrangement **pre-dates the December 2021 prospectus**, so the prospectus description covers it; and there is **no help-page evidence of a card re-platform across the entire 3.7× revenue growth period.**
>
> ⚠️ **Two limits kept on the record:** an unchanged FAQ is weak evidence of *backend* stability — the claim is scoped to help-page evidence, not to an assertion that no re-platform occurred. And the Jan 2018 → Jul 2020 gap is 2.5 years, so the insertion is only bracketed to that window. **Still worth confirming on the call, but this is no longer a soft classification.**

> **MANUAL:** load a YesStyle checkout in a browser with DevTools and read the payment iframe/redirect hosts. Cloudflare blocks automated access; a human with a browser resolves in ten minutes what 20 searches could not.

---

### Section 4: Alternative & Local Payment Methods

✅ **Two enumerated accepted-methods lists were recovered**, so absences in this section are **genuinely sourced**:
- **(A) A machine-readable `helpCurrencies` JSON matrix** — 36 currencies, each with an explicit method array — embedded in the Payment Currencies help page
- **(B) The "About Payment" help index** — the complete local-method inventory, **verified identical in English and German**, so it is a global doc set

Both live URLs return 403, but both were recovered from **Wayback Machine snapshots** (the most recent dated 2026-09-11, five days before this report). That is archived public documentation, not a bypass of a live control.

**Evidentiary standard applied:** matrix (A) omits iDEAL, BLIK, P24 and OXXO, which demonstrably exist — so absence from (A) alone is weak. **Every SOURCED ABSENT below is absent from BOTH lists.**

| Region | Method | Category | Status | Evidence |
|---|---|---|---|---|
| Global | Visa, Mastercard | Cards | **CONFIRMED** — all 36 currencies | matrix A |
| Global | American Express (26/36) · JCB (21/36) | Cards | **CONFIRMED** | matrix A |
| Global | **PayPal** (24/36) · PayPal One-Click | Wallet | **CONFIRMED** | matrix A + index B |
| Global | **Apple Pay (16/36) · Google Pay (21/36)** — both via **Braintree** | Wallet | **CONFIRMED** | `APPLEPAY_BRAINTREE` / `GOOGLEPAY_BRAINTREE` |
| Global | Direct Deposit / Check | Bank transfer | **CONFIRMED — HKD only** | matrix A |
| **Europe** | **iDEAL** (NL) | Bank redirect | **CONFIRMED** — requires EUR **and** a Netherlands billing address | help page hsi.2222 |
| **Europe** | **BLIK · P24/Przelewy24** (PL) | Bank/mobile | **CONFIRMED** — requires PLN, Polish shipping **and** a Polish IP | help page hsi.2731 |
| Europe | **Bancontact · SOFORT/giropay · SEPA Direct Debit · Cartes Bancaires · Swish · MB Way** | Bank rails | **SOURCED ABSENT** | absent from A **and** B |
| Europe | **Klarna (native)** | BNPL | **SOURCED ABSENT** | absent from A and B — see the trap note below |
| **US** | Cards, PayPal, Apple Pay, Google Pay | — | **CONFIRMED** | USD row |
| US | **PayPal Pay in 4** | BNPL | **CONFIRMED but possibly retired** — US (excl. NM, ND, SD, MO, WI), UK, France only. ⚠️ Its page exists but it is **missing from the current About Payment index in both locales** | hsi.2319 |
| US | Affirm · Afterpay · Klarna · Shop Pay · Sezzle | BNPL | **SOURCED ABSENT** | A + B |
| **LatAm** | **OXXO** (MX) | Cash voucher | **CONFIRMED** — gated on MXN, Mexican shipping, order Mex$10–10,000, **and an RFC or CURP tax ID**. Confirmation takes **up to 48 hours**; **refunds on OXXO orders default to store credit, not cash** | hsi.2714 |
| **LatAm** | **Pix · boleto bancário (BR)** | Instant bank / voucher | **SOURCED ABSENT** | A + B — **and there is no BRL currency at all** |
| LatAm | **SPEI · meses sin intereses / cuotas · Mercado Pago** | Bank / instalments / wallet | **SOURCED ABSENT** | A + B |
| **Middle East** | Cards + PayPal | — | **CONFIRMED** across 10 MENA currencies | matrix A |
| Middle East | **Mada (SA) · KNET (KW) · Tabby · Tamara · STC Pay · cash on delivery** | Domestic cards / BNPL / cash | **SOURCED ABSENT** | SAR row = Visa/MC/Amex/PayPal; KWD row = Visa/MC only |
| **Oceania** | Cards, PayPal, Apple Pay, Google Pay | — | **CONFIRMED** | AUD/NZD rows |
| Oceania | Afterpay · Zip · POLi · PayTo | BNPL / bank | **SOURCED ABSENT** | A + B |
| **Hong Kong** | **PayMe · Tap & Go · FPS · Octopus** | Wallet / instant bank | **CONFIRMED — gated on paying in HKD, *not* on shipping destination.** Their own FAQ: *"as long as you choose to pay in Hong Kong dollars (HKD), you can pay using Tap & Go, FPS, PayMe or Octopus."* Three of the four are **members-only** (PayMe excepted), and refund-to-original-method is **unavailable** for Tap & Go, FPS and Octopus | matrix A + hsi.2526 |
| **South Korea** | **KakaoPay · Naver Pay · local card PG** | Wallet / domestic cards | **SOURCED ABSENT** — KRW row enumerates Visa/MC/Amex/JCB/Google Pay only | matrix A |
| Greater China | Alipay · WeChat Pay · UnionPay | Wallet / cards | **SOURCED ABSENT** — CNY row = Visa/MC/Amex/JCB only | matrix A |
| Japan | konbini · PayPay | Cash / wallet | **SOURCED ABSENT** | JPY row |
| **India** | **UPI · RuPay** | Instant / domestic cards | **SOURCED ABSENT** — **the INR row is Visa/Mastercard only, the thinnest row in the entire 36-currency matrix** | matrix A |
| SEA | PayNow (SG) · PromptPay (TH) · QRIS/DANA/OVO (ID) · GCash (PH) · FPX/GrabPay/Touch'n Go (MY) · Atome | Instant bank / wallets / BNPL | **SOURCED ABSENT** | respective currency rows |

**Multi-currency: 36 currencies, and it is true local-currency pricing** — *"Payment is made according to the currency selected by the customer when placing the order."* Full list: USD, EUR, GBP, CAD, AUD, NZD, HKD, CNY, JPY, KRW, TWD, SGD, MYR, THB, PHP, IDR, INR, MXN, CHF, DKK, NOK, SEK, CZK, HUF, PLN, TRY, AED, SAR, QAR, OMR, KWD, BHD, JOD, ILS, MAD, DZD.

**Does the method set adapt by country? Yes — by currency plus billing/shipping address plus IP**, on one global checkout rather than separate storefronts. iDEAL needs EUR + NL billing; BLIK/P24 need PLN + PL shipping + a Polish IP; OXXO needs MXN + MX shipping + RFC/CURP. Card and wallet availability also varies by currency in ways that look like **acquirer limitations rather than design** — Apple Pay on only 16 of 36 currencies, PayPal on 24 of 36, and India restricted to Visa/Mastercard alone.

> ### ⚠️ Warning — the sharpest finding in this report: **there is no BRL.**
> The matrix carries 36 currencies and **not one South American currency** — no BRL, CLP, COP, ARS, PEN or UYU. **Mexico is the only Latin American market with local-currency pricing.** Every Brazilian, Chilean, Colombian, Argentine and Peruvian customer checks out **cross-border in USD on a Visa or Mastercard**.
>
> That is in the region which is **9.4% of revenue and grew +178.4% in H1 2026**, and **Brazil is their #5 traffic country**. In Brazil — the largest e-commerce market in the region — Pix is now the dominant online rail and card instalments are close to mandatory, and YesStyle has **neither local currency, nor local rail, nor instalments**.
> For contrast they maintain **ten MENA currencies** (AED, SAR, QAR, OMR, JOD, BHD, KWD, ILS, MAD, DZD) for a region at 8.0% of revenue that is growing far more slowly. **The currency footprint is misaligned with where the growth actually is.**

> **The FX mechanism, from their own help pages, and it ties straight to the audited FX losses:** *"Currency conversion on our website is handled according to an **internal exchange rate**, which is **periodically** changed based on our bank's exchange rates."* A periodically-updated internal rate across 35 non-USD currencies is precisely how FX losses accumulate. And separately: *"YesStyle is located in Hong Kong and uses an international payment gateway for its credit card transactions. Some banks or credit card companies will charge transaction fees for international purchases."* **So the shopper pays an issuer cross-border/FX fee on top of YesStyle's internal rate — a double FX hit on the customer, and a well-known driver of cross-border approval-rate decline.**

> **MANUAL:** the remaining method question is whether the matrix is fully current. A VPN check from **Brazil and Germany** would confirm, but the enumerated lists are now strong enough to write from.

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Market | Platform | Frequency | Dates | Source |
|---|---|---|---|---|---|
| Refund never received / refused after non-delivery | GB, RS, CA | Trustpilot | **3 of 20** fetched 1–2★ | ~11–13 Sep 2026 | [Trustpilot 1–2★](https://www.trustpilot.com/review/www.yesstyle.com?stars=1&stars=2) ✅ fetched |
| **Store credit forced in place of cash refund to original method** | GB, AZ | Trustpilot | **2 of 20** | ~11–12 Sep 2026 | same |
| **Chargeback pushed back onto the customer months later** | IT | Trustpilot | 1 of 20 | ~10 Sep 2026 | same |
| Order cancelled after 30+ days; dispute over refund method | GB | Trustpilot | 1 of 20 | ~14 Sep 2026 | same |
| Charged, then out of stock, no refund (coupon value deducted) | US | Trustpilot | 1 of 20 | ~10 Sep 2026 | same |
| Damaged goods → refund dispute | CA | Trustpilot | 1 of 20 | ~16 Sep 2026 | same |
| Card accepted on one order, declined on the next, no reason | — | Trustpilot | `[UNVERIFIED]` | undated | summary only |
| Checkout error on card; **PayPal succeeded where card failed** | — | forum / Play | `[UNVERIFIED]` | undated | summary only |

**Aggregate (fetched):** TrustScore **4.3/5** across **102,574 reviews** — 5★ 71%, 4★ 18%, 3★ 3%, 2★ 1%, **1★ 7% (7,184 reviews)**. App Store 4.8/5 across ~90,000 ratings, developer **YESSTYLE.COM LIMITED** — the app is *not* a productive complaint source.

> **Pattern, at the strength the evidence supports: the payment complaints are overwhelmingly refund-side, not authorisation-side.** Store-credit substitution, refund latency, and one chargeback pushed back onto the customer. **9 of 20** fetched 1–2★ reviews are payment or refund related. That maps to **settlement and reconciliation**, which is consistent with the audited ~30-day gateway settlement lag and US$7.58m sitting in PSP receivables. The auth-side complaints exist but only via unverified summaries — **do not assert an approval-rate problem from this evidence.**

**Geography of the 1–2★ cohort:** US, GB, CA, IT, MX, DK, RS, LT, AZ, AU, JM, SA, AE, SG, FR — overwhelmingly Western and long-tail, consistent with an outbound Hong Kong merchant.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | **31 Aug 2026** | **H1 2026 record**: revenue +23.2% to **US$301.51m**, net profit +30.0% to **US$18.30m**, GP margin 31.2% | Results | [Interim press release](https://www.yesasiaholdings.com/press/e_2209_InterimResultPressRelease2026%201.pdf) ✅ |
| 2 | **28 Aug 2026** | **Tim Wang appointed General Manager, U.S.**; Gary Chow VP Operations — a dedicated US GM **three days before reporting a US decline** | **Leadership** | [Announcement](https://www.yesasiaholdings.com/press/) |
| 3 | **27 May 2026** | **First US physical store**, Great Mall, Milpitas CA — adds card-present to a pure-play online stack | Market expansion | company press |
| 4 | **6 Jul 2026** | Yespresso pop-up café, Madrid — European brand activation | Market expansion | company press |
| 5 | **29 Aug 2025** | **US de minimis exemption ended** for packages under US$800. YesAsia named as affected; YesStyle working with couriers to **pay tariffs on the customer's behalf** | Regulatory/cost | NBC News `[UNVERIFIED]` |

**Public payment RFP:** *No public payment-related RFP found.* Searched explicitly; as an HKEX-listed private-sector company they have no tender obligation, so this negative carries no signal.

**Payment hiring:** none found. A **"Finance Transformation"** role leading global accounting operations for the international e-commerce business is open `[UNVERIFIED]` — adjacent and useful as a trigger, but **not** a payments hire and not to be overclaimed as one.

> **Duty-paid checkout is now a payments problem, not only a logistics one.** Landed-cost calculation, tariff collection at checkout and refunding customs fees all run through the payment layer. The CEO has spoken publicly on tariff impact. This is a dated, acknowledged pressure on their largest historical market.

---

### Section 7: Payment-Specific News

| # | Date | Item | Relevance | Source |
|---|---|---|---|---|
| 1 | **30 Jul 2026** | *"Joshua Lau on How YesAsia and PayPal's Partnership Fuels Global Growth"* — CEO fronting the PayPal relationship personally | **PayPal incumbency is deep and actively promoted** | company media page ✅ |
| 2 | **16 Jan 2023** | PayPal APAC case study: PayPal is YesAsia's *"global payments platform"*, **partnered since 2000**, customers in *"over 50 countries and territories"* in *"multiple currencies"*. **No approval, conversion, chargeback or fraud metric disclosed** | 26-year incumbency | [PayPal newsroom](https://newsroom.apac.paypal-corp.com/How-one-Hong-Kong-merchant-is-bringing-Asian-pop-culture-to-the-world) ✅ fetched |
| 3 | **4 Aug 2023** | **Binance Pay accepted** — crypto checkout, USDT 1:1 to USD; help page still live | They will add an unconventional rail when they see demand | binance.com `[UNVERIFIED]` |
| 4 | undated | OXXO help page live (high section ID = recent) | **First true LatAm local method** | help page `[UNVERIFIED]` |
| 5 | undated | App Store advertises *"20+ currencies (Credit Card, Apple Pay, PayPal)"* — BNPL and local methods absent from the app's own pitch | Possible app-vs-web stack divergence | App Store ✅ fetched |

**Provider/method removals:** **none found.** The direction of travel is purely additive.

---

### Section 8: Checkout Experience Audit

**Not fully accessible in this environment.** `yesstyle.com` sits behind **Cloudflare bot management** (`__cf_bm`, `cf-ray`, `server: cloudflare`) and returns HTTP 403 to a standard browser UA, a Googlebot UA and WebFetch alike. One Googlebot attempt was made — the approach that previously worked on Citilink and Garuda — and it failed identically. **No further circumvention was attempted.**

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | **Unknown** | — | Gateway processes and redirects; architecture from prospectus only |
| Guest checkout | **Not determinable** | — | — |
| Card input | **Unknown** | — | A **US$2 authorisation hold** is applied, *"required by the payment gateway"* `[UNVERIFIED]` |
| Payment methods visible | Cards, PayPal, Apple Pay, Google Pay, Alipay, OXXO, Binance Pay | Fair breadth, thin on local rails | assembled from multiple sources |
| Location-based method display | **Partially — OXXO is Mexico-specific**, so some geo-adaptation exists | — | `[UNVERIFIED]` |
| Instalments | **Not found** | — | Material gap risk in MX/BR if absent |
| 3DS | **Not detected** | — | Nothing disclosed anywhere |
| PCI indicator | **`PCI` appears 0 times in 606 prospectus pages** | — | See Section 9 |
| Multi-currency | **20+ currencies**, with a **double conversion** (internal rate + issuer spread) | **Poor** | Their own Terms |
| Mobile | App: 4.8/5, ~90k ratings, **US$178.7m of revenue (35.6%)** runs through it | Good | audited |

---

### Section 9: PCI DSS Compliance

*No direct PCI compliance documentation found publicly for YesStyle or YesAsia Holdings.*

| Dimension | Finding | Source |
|---|---|---|
| PCI DSS Level | **Not disclosed. "PCI" appears 0 times in the 606-page IPO prospectus** and returns nothing in search | prospectus ✅ extracted |
| Card data handling | **Not disclosed** | — |
| Recommended Yuno integration | **Cannot recommend** — no confirmed tokenized PSP checkout, so the conditional inference the template permits is unavailable | — |

**Two honest readings:** HKEX prospectuses often omit PCI, so absence is weak evidence; but a US$500m card-led cross-border merchant not mentioning PCI DSS anywhere in its listing document is still notable. **Frame as "not publicly disclosed" — never as "not compliant."**

Related, from prospectus risk factors: exposure to *"various rules, regulations and requirements… governing electronic funds transfers"* and the risk of losing card acceptance on non-compliance. A sanctions disclosure notes 28 payments totalling ~US$1,344.89 from Crimea/Iran received **through the payment gateways** — trivial money, but it establishes the gateways as their compliance funnel.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: They are marking up their own customers to cover FX losses their gateways create — and it isn't working**
> **Evidence:** Section 3A/12 (prospectus: *"we adopt internal currency rates… to maintain a **premium over the market rates** to hedge against possible currency exchange losses resulted from **payment gateways currency conversion**"*; and *"we do not have a formal foreign currency hedging policy"*) + Section 12 (net exchange losses **US$2,541k → US$4,886k, +92.3%**, now **1.1% of revenue** in H1 2026 and still climbing).
> **Pain Point:** Their gateways convert currency on remittance into USD/HKD. With no hedging policy, the loss lands on them. Their workaround is a price premium on non-USD checkouts — a conversion tax on the customer — and losses are still rising faster than revenue.
> **Yuno Value Proposition:** Settle in the currency collected via local acquiring, so the conversion stops being a gateway decision they absorb.
> **Best Success Case:** **inDrive** — many markets, one layer. Say plainly it is not an Asian case.
> **Outreach Angle:** Quote their own prospectus. Both halves are theirs, it is audited, and it is not disputable.
> **Suggested Subject Line:** *The premium you add to cover FX*

> **Insight #2: You choose the gateway; the gateway chooses the acquirer**
> **Evidence:** Section 3A (prospectus: gateway routes *"through an acquiring bank or payment provider **depending on the location of customer and payment type**"*, on *"standard agreements… without fixed term"*, priced *"per country and/or per currency"*) + Section 3B (no orchestration layer found).
> **Pain Point:** Acquirer selection — the layer that determines approval rate — is delegated to whichever gateway receives the request. They have country-level *pricing* visibility but no country-level *routing* control.
> **Yuno Value Proposition:** Bring acquirer selection in-house above the gateways they already run, without unwinding any of them.
> **Best Success Case:** **Livelo** — routing a decline to a secondary acquirer.
> **Outreach Angle:** Strictly additive. **PayPal has been in place since 2000 — any rip-and-replace framing will be dismissed on sight.**
> **Suggested Subject Line:** *Who picks your acquirer*

> **Insight #3: Latin America is growing 178% on a stack built for cards and PayPal**
> **Evidence:** Section 12 (LatAm **+224% FY2025, +178% H1 2026**; **Mexico US$17,776k FY2025 and US$17,895k in H1 2026 alone** — it beat its full year inside six months; Brazil is the #5 traffic country) + Section 4 (**OXXO confirmed for Mexico; Pix, boleto, SPEI and instalments all SOURCED ABSENT — and the 36-currency matrix contains no BRL, or any South American currency at all**).
> **Pain Point:** Their fastest-growing region is the one their stack is least suited to, and the gap is now provable rather than suspected. Every Brazilian customer pays cross-border in USD on a Visa or Mastercard, in the market where Pix dominates and instalments are close to mandatory. They already built OXXO for Mexico with tax-ID gating and a 48-hour confirmation window — which proves both the need and the willingness to do the work.
> **Yuno Value Proposition:** BRL pricing, Pix and instalments through one layer, instead of a bespoke per-rail build like the OXXO one.
> **Best Success Case:** **Livelo** or **Rappi** — and unusually the region genuinely matches. Name the region; never imply the results came from Asia.
> **Outreach Angle:** Their own currency list is the evidence. Ten MENA currencies for a region at 8.0%, and not one South American currency for the region growing 178%.
> **Suggested Subject Line:** *Thirty-six currencies, no BRL*

> **Insight #4: Refund and settlement, not authorisation, is where customers feel it**
> **Evidence:** Section 5 (**9 of 20** fetched 1–2★ reviews are payment/refund related, dated Sep 2026; store credit substituted for cash refunds; one chargeback pushed back onto a customer months later) + Section 12 (gateways *"settle… **within one month after the trade date**"*; **US$7,578k** trapped in PSP receivables at H1 2026, up from US$4,993k).
> **Pain Point:** A ~30-day settlement lag across multiple gateways makes refunds slow and reconciliation manual, and the customer experiences it as store credit instead of money back.
> **Yuno Value Proposition:** Unified reconciliation and refund handling across providers rather than per-gateway dashboards.
> **Best Success Case:** **Rappi** — 80% less analyst work on reconciliation.
> **Outreach Angle:** Quote one dated review. **Never generalise 9 reviews into "your refunds are broken."**
> **Suggested Subject Line:** *Thirty days to settle, and the refund queue*

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks**
1. Your prospectus says you set internal currency rates at a premium to market to hedge against exchange losses from your payment gateways' conversion — and your FY2025 accounts still show those losses up 92.3% to US$4.9m.
2. Your filings describe submitting a payment request to a gateway company, which then picks the acquiring bank by customer location and payment type — so the layer that sets your approval rate is the one you don't control.
3. Your payment pages list 36 currencies and not one South American currency, in the region that grew 178% last half.

**Cold call openers**
1. "Your payment gateway charges are an itemised line in your annual report and you've taken them from 2.6% to 2.1%. I wanted to ask about the line underneath it, the exchange losses, which have gone the other way."
2. "Your LatAm revenue grew 178% last half, and your checkout doesn't price in BRL. What's your approval rate in Brazil?"
3. "You've had PayPal since 2000. I'm not here about PayPal — I'm here about what sits underneath the card side."

**Do NOT use:** "you're overpaying on MDR" (their take rate is **falling** — someone owns this and is winning, and this opener will land badly); "you have no orchestration" as a put-down (they run multiple gateways deliberately); any rip-and-replace framing (**PayPal since 2000, and the wallet gateway is PayPal-owned Braintree**); **"you accept Klarna"** (you do not — that is Klarna's one-time virtual card, which works at any card-accepting merchant); **PayPal Pay in 4 in the present tense** (its page exists but it is missing from the current index in both locales); any customer-side FX complaint (**none found**); the Trustpilot 4.3 rating (solicited); "your revenue is falling" (**group revenue grew 23.2%** — only the US fell).

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ | Est. Size | Overlap | Known PSP/rails | Source |
|---|---|---|---|---|---|---|
| **Stylevana** | stylevana.com | **Hong Kong** | ~US$433.6m online sales 2025 `[ESTIMATE]` | Global cross-border — **closest analogue** | **Verified:** Visa, MC, Amex, Apple Pay, Google Pay, PayPal only | [Support article](https://stylevana.zendesk.com/hc/en-us/articles/43813430744857) ✅ fetched |
| **Olive Young (US)** | us.oliveyoung.com | Seoul | CJ Olive Young, 450+ KR stores | US | Cards incl. JCB/UnionPay, PayPal, Apple Pay, **Klarna Pay Later + Pay Over Time** | `[UNVERIFIED — 403]` + Klarna merchant page |
| **Olive Young Global** | global.oliveyoung.com | Seoul | Ships 150 countries | Rest of world | International + Korean cards, PayPal, Apple Pay, **Alipay+** | `[UNVERIFIED]` |
| **StyleKorean** | stylekorean.com | South Korea | ~1.3M visits/mo | US/EU | Cards; billing page *"run by PayPal payment module"* | `[UNVERIFIED]` |
| **Jolse** | jolse.com | South Korea | ~710k visits/mo | US/EU | Cards, PayPal, Alipay, Klarna | `[UNVERIFIED — aggregator]` |
| **Althea** | althea.kr | South Korea | SEA-focused | SEA | PayPal, cards, **DragonPay (PH), COD** | `[UNVERIFIED]` |
| **YesAsia** | yesasia.com | Hong Kong | Sibling, same parent | Global | Assume shared stack | — |

#### 11B. Cross-border benchmarks

| Company | Rails | Why it matters |
|---|---|---|
| **SHEIN (EU)** | **iDEAL** (10 named NL banks), **Bancontact**, **EPS** (~25 AT banks), **Klarna**, PayPal, Afterpay, Google/Apple Pay, cards, **COD** — explicitly per-country | The benchmark for what European shoppers now expect. **Europe is 48.2% of YesStyle revenue** |
| **SHEIN (MX)** | **OXXO** cash voucher, ~13,000 stores | YesStyle has matched this one |
| iHerb, Temu, AliExpress, Zalora | Not researched | — |

#### 11C. Companies Recently Adopting Payment Orchestration

*No public case studies found of direct competitors adopting payment orchestration.* **Explicit negative.** Stylevana and YesStyle were both searched against Adyen, Oceanpayment, Airwallex, PingPong, Checkout.com and against Spreedly, Primer, Gr4vy, Yuno, dLocal, EBANX — **zero hits on either**. These are quiet private merchants who do not publish payment infrastructure.

> **Do not tell the prospect their competitors are orchestrating. None are.** The defensible competitor observation is structural: **Olive Young runs two separate storefronts with two different payment stacks** (Klarna on the US site, Alipay+ on the global site). That is deliberate per-market payment architecture — the thing a gateway-by-gateway setup makes expensive. **And no Asian-beauty competitor offers Pix, boleto or OXXO except YesStyle itself**, which makes LatAm whitespace rather than catch-up.

#### 11D. Prospect Scoring & Top Pipeline

Competitor scoring cannot be completed — **no competitor's PSP or orchestrator is established**, so every orchestration and multi-PSP signal would be ⬜ across the board.

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|---|---|---|---|---|---|---|---|
| 1 | **Stylevana** | Direct | Global cross-border | Not scored | **High** | HK-HQ'd, ~US$434m, **verified card+PayPal-only stack** — same shape, same gaps | ✅ **row 59, P1** |
| 2 | **Olive Young Global / US** | Direct | KR + global | Not scored | High | **Two storefronts, two stacks**; Alipay+ and Klarna | ❌ **not in TAL — genuine find** |
| 3 | **StyleKorean** | Direct | US/EU | Not scored | Medium | PayPal-module billing | ❌ not in TAL |
| 4 | **Jolse** | Direct | US/EU | Not scored | Medium | Cards, PayPal, Alipay | ❌ not in TAL |
| 5 | Althea | Peer | SEA | Not scored | Low | DragonPay + COD | ✅ row 48, P1 |

> **Stylevana is the standout.** Hong Kong-HQ'd, ~86% of YesStyle's revenue by third-party estimate, already **P1 in the TAL**, and its **verified** payment page lists only cards, Apple Pay, Google Pay and PayPal — the same shape as YesStyle with the same local-rail gaps. **Olive Young is a genuine TAL addition.**

---

### Section 12: Business Case Data

| Metric | Value | Source |
|---|---|---|
| **Revenue FY2025** | **US$501,544k** (+45.0%) | AR2025 ✅ audited |
| Revenue H1 2026 | **US$301,510k** (+23.2%) | Interim 2026 ✅ |
| Net profit | FY2025 **US$23,140k** · H1 2026 **US$18,300k** (+30.0%) | ✅ audited |
| Gross margin | 29.6% group; **YesStyle Platforms 35.4%** | ✅ |
| **Segment — YesStyle Platforms** | **US$347,479k (69.3%)** | ✅ |
| **Payment gateway charges** | FY2022 2.6% · FY2023 2.6% · FY2024 **US$8,780k (2.5%)** · FY2025 **US$11,160k (2.2%)** · H1 2026 **US$6,258k (2.1%)** | ✅ audited, itemised |
| **Net exchange losses** | FY2024 US$2,541k (0.7%) · FY2025 **US$4,886k (1.0%, +92.3%)** · H1 2026 **US$3,296k (1.1%, +51.9%)** | ✅ audited |
| **Combined payment cost** | **FY2025 US$16,046k = 3.20% of revenue ≈ 69% of net profit** · H1 2026 US$9,554k = 3.17% ≈ 52% of half-year net profit | *my arithmetic on two audited lines* |
| **Customers (YesStyle)** | **2,855,000** (+26.4%); H1 2026 1,986,000 (+14.9%) | ✅ |
| **Average order value** | **US$65.1** FY2025; **US$70.6** H1 2026 (+8.6%) | ✅ |
| Est. annual orders | **~5.34M** (revenue ÷ AOV) | `[ESTIMATE — my arithmetic]` |
| Customer acquisition cost | US$14.2 FY2025; US$15.5 H1 2026 | ✅ |
| Return rate | **0.3%** FY2025, 0.1% H1 2026 | ✅ — remarkably low |
| App revenue | **US$178,681k (35.6% of group revenue)**, 4.9M downloads | ✅ |
| **PSP settlement float** | **US$4,993k** at FY2025 → **US$7,578k** at H1 2026, on ~30-day settlement terms | ✅ audited |
| **GMV** | **Not disclosed** | — |
| Market cap | ~HK$1.42bn (≈US$182M) | `[UNVERIFIED]` |
| Billing channel split | **N/A — no app-store IAP exposure.** Their app uses their own checkout | — |

> **Business case sizing is unusually strong for this repo.** Most accounts require a discovery call to size. Here the merchant publishes its own cost of acceptance, audited, across five periods — **US$11.16m of gateway charges plus US$4.89m of FX losses in FY2025, together ~3.2% of revenue and roughly 69% of net profit.**
>
> ⚠️ **One honest caveat:** gateway charges are a Group-wide line, and ABW Offline (US$49,935k) is key-channel wholesale unlikely to run through a consumer gateway. If the charges fall mainly on the B2C platforms, the effective take rate on card-paid volume is **higher than 2.2%**. That is an inference from segment mix, not a disclosed figure.

---

### Section 13: Latin America — opportunity sizing *(deep-research pass #2, 107 agents)*

> **Why this section exists.** LatAm is 9.4% of FY2025 revenue and grew **+224.4% in FY2025 and +178.4% in H1 2026** — the fastest-growing region in the business — while US revenue *fell* 17.6% YoY in H1 2026. The checkout prices in 36 currencies and carries **no BRL and no South American currency at all**, while maintaining **ten MENA currencies** for a region at 8.0% of revenue growing far more slowly. This pass asked what that actually costs and what it would take to close.

#### 13A. The IOF wedge — the one hard number

A Brazilian cardholder buying from YesStyle in USD pays **3.5% IOF** on top of the price. A BRL-denominated, locally-acquired or Pix transaction does not trigger it at all.

**Verified by me at primary source** — [Decreto nº 12.499, de 11 de junho de 2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/D12499.htm), Planalto, inciso VII, fetched and text-extracted directly:

> *"nas operações de câmbio destinadas ao cumprimento de obrigações das instituições que participem de arranjos de pagamento de abrangência transfronteiriça na qualidade de emissores destes, decorrentes de **aquisição de bens e serviços do exterior efetuada por seus usuários**… **3,5% (três inteiros e cinco décimos por cento)**"*

That clause describes YesStyle's transaction exactly: a Brazilian issuer settling FX for its user's purchase of goods from abroad. The tax is levied on the FX operation and reaches the shopper on the card statement.

> ⚠️ **Time-sensitive — re-verify before any dated collateral.** The 3.5% rate rests on an **interlocutory STF injunction (Moraes, 16 July 2025)** with the merits still pending before the Plenário. Cite it as *"as of September 2026"*. Sources: [STF](https://noticias.stf.jus.br/postsnoticias/stf-restabelece-parcialmente-decreto-que-eleva-aliquotas-do-iof/) · [Câmara](https://www.camara.leg.br/radio/programas/1182454-aumento-do-iof-para-cartao-internacional-volta-a-valer/)

This sits **on top of** YesStyle's own FX handling — they run internal rates at *"a premium over the market rates"* in lieu of hedging, and still booked **US$4,886k of exchange losses in FY2025**.

#### 13B. What Reach already covers — a correction to the working premise

**The premise "YesStyle cannot serve Brazil, Yuno unlocks it" is WRONG and must never be used.** Reach is already live in their card flow (the `CKO Withreach.com` descriptor), and Reach already does most of Brazil.

**Verified by me directly against `docs.withreach.com`** (apex `withreach.com` resets the connection; `www` and `docs` respond. Docs are current — the Boleto page carries `updatedAt 2026-09-14`):

| Capability | Status | Evidence |
|---|---|---|
| **BRL** | ✅ supported | [Supported countries and currencies](https://docs.withreach.com/docs/supported-countries-and-currencies): `BRL \| R$ \| Brazilian Real \| Brazil \| BR` |
| **BRL ring-fenced** | ⚠️ | *"BRL may only be processed in BR and no other currencies are accepted in BR."* |
| **Enablement** | ⚠️ gated | *"Currencies are made available to suppliers based on supplier risk profiles, Reach's approval results, and locally available payment methods."* — per-merchant approval, not a config toggle |
| **Boleto Bancário** | ✅ full guide | Offline · no chargebacks · no recurring · no partial payment · 3-day voucher expiry · 180-day refund window |
| **Brazilian banking partners** | ✅ | Boleto guide, verbatim: *"our **Brazilian banking partners** will have to get in touch with the customer and send them a bank transfer"* |
| **Elo, Hipercard, Aura** | ✅ | Domestic-only Brazilian card schemes — their presence implies **genuine local acquiring**, not cross-border USD rails |
| **Instalments** | ✅ documented | [Instalments guide](https://docs.withreach.com/docs/instalments) — see 13D |
| **Pix** | ❌ **SOURCED ABSENT** | see 13C |

**Reach's Brazil row**, extracted from the country×method matrix at [supported-payment-methods](https://docs.withreach.com/docs/supported-payment-methods):
`BANKTRANSFER · AURA · BOLETO · ELO · HIPERCARD`

> 🔍 **Method note.** That table renders every method as an `<img>` — tag-stripping returns *empty cells*. The method names live only in the image filenames (`PaymentMethods/PM_BOLETO.png`). Another case where the answer was in the raw HTML and invisible in the text.

#### 13C. Pix — sourced absent from Reach, at two independent levels

1. **The 50-country method matrix** carries **38 distinct method icons**. Pix is not among them — not for Brazil, not for any country.
2. **The enumerated payment-method guide set** under *"Additional payment guides"* has exactly **11 members**: Apple Pay, Bank Transfer, Boleto, Cash App Pay, Credit cards, Instalments, Klarna, OXXO, PagoEfectivo, PayPal, iDEAL/Wero. No Pix.

Zero `pix` occurrences in the docs index, the supported-currencies page, the Boleto guide, or the `/getPaymentMethods` API reference.

**Two enumerated first-party lists → this is SOURCED ABSENT, not NOT FOUND.** Pix is the single real gap in the Brazil story, and it is the one that matters most.

**A Hong Kong entity cannot contract Pix directly.** Pix is central-bank infrastructure reachable only through BCB-authorised participant institutions — [Resolution BCB No. 1/2020](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Pix_Regulation/Resolution_BCB_1.pdf) · [participant list](https://www.bcb.gov.br/en/financialstability/pixparticipants). A merchant of record or locally licensed partner is structurally required.

#### 13D. Instalments — I overturned the run's finding here

The run concluded parcelado was absent from Reach. **That is wrong, and I'm recording the correction rather than the claim.**

Reach publishes a dedicated [Instalments guide](https://docs.withreach.com/docs/instalments) which names Brazil explicitly:

> *"Instalments are popular in areas with low credit penetration and high credit card interest rates (for example, **Mexico and Brazil**)."*

It carries a worked **BRL** example — an R$816.55 order at 6 instalments and a 7.3% rate → R$59.61 financing fee — and a live API field:
```json
"Financing": { "Instalments": 6, "ConsumerPrice": 59.61 }
```
Fee incidence is configurable: supplier pays, consumer pays, or split.

**Why the run got it wrong:** instalments carry **no icon in the country matrix for *any* country**, including Mexico. Instalments are a **financing modifier on card transactions**, not a "payment method" that matrix models. Absence from a table that models no instalments anywhere is not evidence of absence. The agent read the matrix and missed the guide.

#### 13E. SHEIN — the category benchmark, verified verbatim by me

SHEIN is the direct Brazilian benchmark for this exact category. **I fetched `m.shein.com/br/How-to-Pay-a-278.html` myself** rather than trust the summary, because this account has already produced one fabricated "YesStyle Brazil accepts Pix" claim scraped from an unrelated retailer.

Their own enumerated list (the page says "5 opções" and then lists six):

> *"A SHEIN aceita um total de 5 opções de pagamento: 1.Pagamento com **Pix**; 2.**Cartão de crédito brasileiro**; 3.**Boleto bancário**; 4.Cartão de crédito e débito virtual; 5.Cartão de crédito e débito internacional; 6.Pagamento com **Pagaleve**"*

- **Parcelado:** *"Ao usar um cartão de crédito brasileiro, seu pagamento poderá ser dividido em **até 6 parcelas**."* · *"O valor mínimo de cada compra é de R$ 5,00"* · *"**Somente para cartões de crédito emitidos por bancos brasileiros.**"*
- **They warn on international cards, in their own words:** *"Devido a questões de segurança de pagamentos internacionais, sua solicitação de pagamento **poderá ser rejeitada**. Caso isso aconteça, sugerimos entrar em contato com seu banco ou selecionar um método de pagamento diferente."*
- **And they steer away from it:** *"sugerimos usar um cartão de crédito brasileiro (em parcelas) ou PayPal"*
- **PagaLeve** is Pix-based BNPL: *"Os pagamentos são feitos via Pix, sem necessidade de cartão de crédito."*
- Boleto is gated on *"clientes que moram no Brasil e têm um CPF"*, 3 days to pay, and *"não permite reembolsos através do mesmo método de pagamento."*

> ⚠️ **SHEIN evidences shopper expectation, not mechanism.** SHEIN has a Brazilian entity. YesStyle does not. Do not present SHEIN as a template for *how* — only for *what Brazilian shoppers now expect*.

#### 13F. Pix operational fit for a cross-border retailer

- **Refunds work.** Merchants hold a native, discretionary refund right for **90 days**, in full or in multiple partial amounts — [Guia MED, Banco Central](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Guia_MED.pdf).
- **No card-style chargeback liability.** BCB states explicitly that MED is *not* a chargeback mechanism and that good-faith sellers cannot be debited. A genuine risk advantage over cards — though not a guarantee funds are never held.

At a **0.3% return rate**, YesStyle is close to the ideal Pix merchant profile.

#### 13G. Instalment market context — with the scope limits attached

- **Brazil:** 64.5% of interest-free instalment *value* sits in **2–6 parcels**, and 98.1% in 12 or fewer — so even a 3×–6× *sem juros* offer captures the bulk of instalment demand. Source: [ABECS sector balances](https://abecs.org.br/storage/sector_balances/23/01KABN6058KGHQGZQAZ6RHBFGR.pdf).
- **Mexico:** Banco de México frames instalments as a principal instrument for stimulating card sales; 54.6% of comparable-portfolio cards and 51.0% of card balance sit in instalment promotions. Source: [Banxico RIB tarjetas de crédito](https://www.banxico.org.mx/publicaciones-y-prensa/rib-tarjetas-de-credito/%7BB30B21EE-FC4A-34AC-FC8E-60307C8C5E63%7D.pdf).

> ⚠️ **Do not restate these as e-commerce or conversion figures.** ABECS is **economy-wide card spend**, not beauty/fashion e-commerce at an R$350–400 ticket, and its 98.1% denominator is **interest-free instalments only**. Banxico's 51.0% is a share of **credit-card balance across all channels**, includes preferential-rate as well as interest-free promotions (MSI alone is 27.6%), and excludes store cards. Neither is a conversion-lift number.

#### 13H. NOT ESTABLISHED — state plainly, never fill

1. **No quantified cross-border vs. locally-acquired approval-rate penalty** for Brazil or Mexico could be sourced. The one candidate (a Visa LatAm page) was **refuted 0–3** — it says only *"certain Latin American countries"*, quantifies nothing, and breaks out no country. **Do not put an approval-rate percentage for Brazil in an email.** The qualitative version is defensible and is corroborated by SHEIN's own warning; the number is not.
2. **No numeric Pix MDR vs. card MDR comparison.** The BIS bulletin supports the *direction* only. No basis-point figure is sourceable.
3. **Does Reach settle BRL out to a Hong Kong entity, and is its Brazil acquiring genuinely local?** Reach's public docs do not answer it. Elo/Hipercard/Aura support is strong circumstantial evidence for local acquiring, but it is **circumstantial**. This is the pivot of the entire business case and it is a **discovery question, not a claim**.
4. **The provider comparison the brief asked for was not completed** — dLocal, EBANX, Nuvei, Adyen, PagBrasil, Mercado Pago and PayRetailers were not verified. Only Reach was.

#### 13I. Claims killed in this pass

**Ten claims were refuted** during 3-vote adversarial verification, including the most attractive statistics in the whole run. Recorded here so nobody reintroduces them:

- ❌ *"68.4% of Brazilian apparel/footwear/accessories card volume was instalment volume"* — refuted 1–2. The single most quotable line produced by the run. **Do not use it.**
- ❌ *"Interest-free instalments were 42.7% of Brazilian credit card value, 49.3% of card-not-present"* — refuted 0–3.
- ❌ *"43.2% of transacted card value in Q1 2026"* — refuted 0–3, ambiguous denominator.
- ❌ *"62.4% of instalment purchases are 6× or fewer"* — refuted 1–2.
- ❌ **SHEIN's embedded page config names EBANX, dLocal and Adyen as its LatAm acquirers** — refuted 0–3. Tempting and unproven.
- ❌ *"Ordinary e-commerce disputes are explicitly outside MED scope"* — refuted 0–3.
- ❌ A BIS quote circulated as verbatim (*"Success depended on two critical factors…"*) is a **paraphrase that does not appear in the document**. The real sentence is *"the two key ingredients…"*.

> 🔍 **One false negative I caught in the other direction.** The run refuted SHEIN's *"up to 6 parcelas / R$5,00 minimum / Brazilian-issued cards only"* claim 0–3. **All three facts are correct** — I confirmed them verbatim on SHEIN's own page (13E). What deserved refuting was the *inference* bolted onto them: that this is why a cross-border checkout "cannot offer parcelado". The restriction is on the card's **issuer**, not the acquirer. The verifiers killed the facts along with the bad inference. Keep the facts, drop the inference.
>
> 🔍 **And one substring false positive**, for the running list: the first `pix` hit on SHEIN's page was `unit: 'pixel'` in a JS performance config.

#### 13J. What this does to the pitch

The Brazil angle is **real but narrower than it first looked**, and it has to be argued precisely:

1. **Pix is the gap.** Sourced-absent from YesStyle's checkout *and* from their existing provider's entire method set. This is the line that survives scrutiny.
2. **The IOF 3.5% is the number.** Government-levied, lands on the shopper, and disappears entirely on a BRL or Pix transaction. It is the cleanest quantified cost in the file and it is not a Yuno estimate.
3. **Reach is a partial path, not a dead end and not a switch.** BRL, Boleto, local card schemes and instalments are documented; Pix is not; and BRL is approval-gated per merchant. The honest framing is *reach and coverage*, not capability.
4. **Never claim they "can't do Brazil."** They already partly can. A payments lead would know it in one line, and the thread would be over.

> 💡 **Internal note, not for an email.** Reach's own Boleto guide names **Nippon-Yasan** — a cross-border Japanese e-commerce retailer — as its worked integration example. That is the closest public analogue to YesStyle's profile that exists in their current provider's documentation. Useful for understanding what Reach can already do; it is *someone else's* reference customer and does not belong in outreach.

---

### Overall Research Confidence

**High on financials and payment economics — the highest in this repo. Medium on the stack. Low on methods and traffic.**

**High confidence** (primary-source, extracted directly by me):
- The 606-page IPO prospectus, FY2025 annual report and H1 2026 interim, all downloaded and text-extracted. Five years of itemised payment gateway charges, FX losses, settlement terms, receivables, the architecture description and the self-hedge mechanism
- Multi-gateway confirmed by plural usage counts ("payment gateway companies" ×10)
- `orchestrat*` = 0 and `PCI` = 0 across 606 pages
- Audited revenue by country and by segment; operating metrics
- PayPal since 2000, verified by my own fetch
- Trustpilot aggregate and dated 1–2★ reviews, fetched

**Medium confidence:** the gateway *identity* (never named anywhere); whether the 2021 prospectus architecture still holds in 2026 after 3.7× revenue growth.

**Upgraded to High confidence after the archived-snapshot recovery:** **payment methods.** Two enumerated lists were obtained — a 36-currency JSON method matrix and the complete "About Payment" help index (verified identical in English and German) — so method absences are **sourced**, not merely unfound. Every SOURCED ABSENT in Section 4 is absent from **both** lists.

**Low confidence:** **traffic is fully estimated**, with only 5 countries public and 47.66% unallocated; it is deliberately not used for geography. Also unresolved: whether the currency matrix is fully current (it omits iDEAL/BLIK/P24/OXXO, which demonstrably exist, so it is either stale or scoped to card and wallet rails only) and whether PayPal Pay in 4 is still live.

**Traffic data was ESTIMATED via WebSearch fallback** — not supplied, not API-sourced.

**High confidence on the LatAm pass (Section 13), with two named gaps.** The IOF rate, Reach's Brazil coverage and SHEIN's method list were each re-verified by me first-hand at primary source rather than taken from agent summaries — and doing so overturned one agent finding (instalments) and rescued one wrongly-refuted one (SHEIN's parcelado terms). **Not established and deliberately left empty:** any quantified cross-border approval-rate penalty for Brazil or Mexico, and any numeric Pix MDR.

---

### Manual Research Recommendations

> **Area:** Whether the 36-currency matrix is fully current
> **Why it matters:** It omits iDEAL, BLIK, P24 and OXXO, which demonstrably exist — so it is either stale or scoped to card and wallet rails only. The sourced absences already survive this (each is absent from *both* enumerated lists), but a live check would put them beyond argument.
> **Action:** VPN into **Brazil and Germany** and walk the checkout. Lower priority than it was — the archived enumerations are strong enough to write from.

> **Area:** The PRIMARY card acquirer — still the one real gap
> **Why it matters:** Reach is now confirmed in the card flow, but only as an *"in some cases"* exception path. The acquirer carrying the bulk of card volume is named nowhere in 606 prospectus pages, three annual reports, or any first-party page. It determines who the incumbent actually is.
> **Action:** DevTools on a live checkout — read the payment iframe/redirect host. **Or simply place a small test order and read the bank descriptor**, which is now known to be informative on this merchant. A deep-research pass with 102 agents could not close this from public sources; a single test transaction would.

> **Area:** Whether Reach is merchant of record on those transactions
> **Why it matters:** If Reach is MoR, it owns the settlement currency and the FX conversion on that slice — which bears directly on the audited exchange losses and on what Yuno would actually be displacing versus complementing.
> **Action:** Ask on the call. Reach's own consumer terms say statements *"will include a reference to 'Reach' and the Supplier"*.

> **Area:** Whether the 2021 architecture still holds
> **Why it matters:** The greenfield classification rests on it, and revenue has grown 3.7× since.
> **Action:** Ask on the call. It is a natural, non-loaded opening question.

> **Area:** Approval rates in Brazil and Mexico
> **Why it matters:** LatAm is growing 178% on a stack least suited to it. **They very likely do not know the answer**, and the question is worth more than any pitch.
> **Action:** Ask it directly.

> **Area:** TAL hygiene
> **Why it matters:** One real competitor is missing and YesStyle's own revenue is understated.
> **Action:** Add **Olive Young**. Correct YesStyle's TAL revenue from "~$300M (FY24)" to **US$501.5m FY2025 (FY2024 actual US$345.8m)**. Note **Stylevana (row 59)** is the closest analogue and already P1.

---

### Appendix: All Source URLs

**Primary filings (downloaded and extracted by me)**
- IPO prospectus: https://www1.hkexnews.hk/listedco/listconews/sehk/2021/0628/2021062800027.pdf
- FY2025 annual report: https://www.yesasiaholdings.com/pdf/e_2209_annualreport2025.pdf
- H1 2026 interim report: https://www.yesasiaholdings.com/pdf/e_2209_Interimreport2026.pdf
- H1 2026 results press release: https://www.yesasiaholdings.com/press/e_2209_InterimResultPressRelease2026%201.pdf
- IR index: https://yesasiaholdings.com/investor-relations.html

**Payments** — https://newsroom.apac.paypal-corp.com/How-one-Hong-Kong-merchant-is-bringing-Asian-pop-culture-to-the-world ✅ fetched · https://www.binance.com/en/square/post/2023-08-04-binance-pay-now-accepted-on-yesstyle-for-beauty-purchases-910124
**Complaints** — https://www.trustpilot.com/review/www.yesstyle.com?stars=1&stars=2 ✅ fetched
**Traffic** — https://www.similarweb.com/website/yesstyle.com/ ✅ fetched
**Competitors** — https://stylevana.zendesk.com/hc/en-us/articles/43813430744857 ✅ fetched · https://us.oliveyoung.com/help/billing-and-payment · https://global.oliveyoung.com
**Tariffs** — https://www.nbcnews.com/news/asian-america/end-de-minimis-exemption-tariffs-korean-beauty-products-rcna228929
**Yuno cases** — https://y.uno/en/success-stories/livelo · https://y.uno/en/success-stories/rappi · https://y.uno/en/success-stories/indrive

</details>
