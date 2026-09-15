# VietJet Air

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 13 / 24 → 🟢 Medium — **analyst override to ⭐ High Priority, reasoning in the breakdown**
**Industry:** Airlines (low-cost carrier) · **HQ:** Hanoi (registered) / Ho Chi Minh City (operating), Vietnam · **Researched:** 2026-09-15 · **First email sent:** —
**Motion:** **In-house — but the routing is not theirs.** See Section 3B. This nuance is the entire sale.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Vietjet Aviation Joint Stock Company (HOSE: **VJC**) is Vietnam's largest low-cost carrier: **107 aircraft, 254 routes of which 202 are international, 28.2 million passengers and VND 82,093 billion (~US$3.1B) consolidated revenue in FY2025**. It owns **Galaxy Pay**, a State-Bank-licensed payment company that runs the airline's checkout across every market and markets itself as a "Payment Orchestration Platform".

**SimilarWeb total visits (last full month):** **No reliable figure.** Not supplied by Prateek; SimilarWeb bot-blocked (HTTP 202, empty body); Semrush serves `trafficByCountry: visible:false` to logged-out clients; HypeStat has no country table and self-reports its data as **2,071 days stale**. Two search summaries give flatly contradictory splits — **Vietnam 43.55%** vs **Vietnam 99.36%** — and monthly-visit estimates differ 7x (1.2M vs 8.7M). **No country split has been constructed. Two ICP signals are unscoreable as a direct result.**

### Top 5 markets
⚠️ **This is a ROUTE and CURRENCY profile, not a traffic ranking.** Built from the FY2025 annual report's network disclosure and the 21 currencies in their own live booking widget. Traffic shares are genuinely unknown.

| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| — | 🇻🇳 **Vietnam** (home; 52 domestic routes) | Unknown, but #1 on both contradictory estimates | The deepest stack of any airline researched: intl cards · **NAPAS** direct · **VietQR** · **MoMo** · **ZaloPay** · **SkyPay** (own wallet) · **Payoo** cash at bill-payment points · HDBank & VietJet office cash · **HDBank and VPBank co-brand cards** · **Movi** BNPL · **HD Saison** instalments · SkyPOS SoftPOS at airports | **ShopeePay** (Vietnam Airlines carries it). ⚠️ **VNPAY-QR is being switched OFF from 01/06/2026** — see Section 7 | ✅ VJC + **Galaxy Pay Co., Ltd** (100%, SBV-licensed) |
| — | 🇮🇳 **India** (AR2025: *"the airline operating the largest number of routes between Vietnam and India"*) | Unknown | 🚩 **Contested.** Galaxy Pay announced a **PayU** integration with INR, UPI and Net Banking — but **no Indian rail appears in the checkout bundle at all** | **UPI, RuPay, netbanking** all absent from the bundle, despite INR being a live booking currency | ❌🔒 **No Indian entity.** Domestic acquiring is gated on local presence |
| — | 🇹🇭 **Thailand** | Unknown | Four card schemes + counter Pay Later; 2C2P QR / ATM / mobile-banking flows. **Their Thailand payment guide is dated December 2022** | **PromptPay never named**, TrueMoney, Rabbit LINE Pay, instalments all absent | ❌ Only a **9%-held associate**, Thai Vietjet, **not consolidated**, on its own domain and IATA code (VZ) |
| — | 🇰🇷 **South Korea** | Unknown | **SmartroPAY** (local card PG) | **KakaoPay, Naver Pay, Toss** not found | ❌🔒 No Korean entity |
| — | 🇮🇩 **Indonesia** | Unknown | **DOKU** — IDR pricing, local cards, bank transfer, e-wallets and **QRIS** (~Oct 2025) | Nothing material once DOKU is live | ❌🔒 No Indonesian entity |

**Also live:** 🇨🇳 China (**Alipay + WeChat Pay**, no PRC entity, 5 new routes in 2025) · 🇯🇵 Japan (**2C2P**, plus Shizuoka route Apr 2026) · 🇦🇺 Australia (**PayID via AzuPay**) · 🇪🇺 Europe and 🇳🇿 New Zealand (**Klarna, Riverty, Alma, Oney** BNPL on long-haul) · plus Taiwan, Hong Kong, Malaysia, Cambodia, Laos, Russia, Kazakhstan, and **Sri Lanka from August 2026**.

### Legal entities
- **Vietjet Aviation Joint Stock Company** (Vietnam) — tax code **0102325399**, first issued Hanoi 23 Jul 2007, amended for the 31st time 14 Aug 2025; charter capital VND 5,916,113,340,000; **HOSE: VJC**
- **Galaxy Pay Company Limited** (Vietnam) — reg **0316368255** (10 Apr 2024), **100% owned**, **SBV intermediary payment services licence 51/GP-NHNN, 16 Aug 2021**: payment gateway + collection/disbursement + e-wallet. Brands: **Galaxy Pay** (platform), **SkyPay** (wallet), **SkyPOS** (SoftPOS)
- **Thai Vietjet Air Joint Stock Co., Ltd** (Thailand) — reg 0105556100551. ⚠️ **An ASSOCIATE at ~9%, equity-accounted, NOT consolidated.** The 28.2M passenger figure explicitly excludes it
- Swift 247 JSC (~67%) · VietjetAir Cargo JSC (~64%, indirect) · Airport NEO LLC · Victoria Aviation Academy JSC (95%)
- **Aircraft-financing SPVs only, no commercial use:** Vietjet Air Singapore Pte Ltd (201408849N), Vietjet Air Ireland No. 1 Ltd, Vietjet Air IVB No. I and II Ltd (BVI), Skymate Ltd (Cayman). AR2025: *"Vietjet has also established subsidiaries in jurisdictions with favorable tax policies"*
- ❌ **No entity in India, China, Korea, Japan, Taiwan, Indonesia, Australia, Hong Kong, Malaysia, Cambodia, Laos, Russia or Kazakhstan**

### Known PSPs
- **CyberSource (Visa)** and **MPGS (Mastercard)** — `[Vendor site]` + `[Annual Report]`, acquired **through HDBank, Vietcombank and VietinBank**
- **Adyen** — `[Annual Report p.89]` + `[Vendor site]`. Role and markets never scoped publicly. ⚠️ **Not to be confused with Adyen's published Vietnam Airlines relationship — different carrier**
- **PayU** (India) · **DOKU** (Indonesia) · **2C2P** (Thailand *and* Japan) · **SmartroPAY** (Korea) · **AzuPay** (Australia PayID)
- **NAPAS** — direct connection, *"nhằm tối ưu chi phí xử lý"* (to optimise processing cost)
- **Galaxy Pay** itself — own gateway, wallet (SkyPay) and SoftPOS (SkyPOS)
- **Payoo**, **MoMo**, **ZaloPay**, **Movi**, **HD Saison**, **HDBank**, **VPBank**
- Checkout front end runs on a **third-party platform, `vja-ui.useleadr.com`** (Next.js), not built in-house

### Orchestration status
**In-house orchestration layer — and they say so themselves.** Galaxy Pay sells a product named *"Nền tảng điều phối thanh toán"* / *"Payment Orchestration Platform"* and runs a 22-article content category by that name. **No third-party orchestrator:** VietJet appears nowhere on CellPoint Digital's airline roster, and no Juspay, Spreedly, Primer, Gr4vy, APEXX, Payrails or Yuno reference exists.

**But the routing is vendor-supplied, and Galaxy Pay says that too.** See Section 3B for the verbatim quote — this is the single most important finding in the account.

### Buying signals
- 🚀 **Relentless expansion.** 22 new routes in 2025; Russia and Kazakhstan added; 5 new China routes; **Sri Lanka from Aug 2026** (new country); **five new Philippines/Japan/Thailand routes from 10 Nov 2026**; Japan Shizuoka Apr 2026. **2026 plan: 115 aircraft, 31M passengers.** Every new country is a new currency and a new local-methods decision — [AR2025](https://ir.vietjetair.com/File_Upload/financial-information/annual-reports-root/annual-reports/20260417_VJC_AR2025_EN_Final.pdf)
- 📋 **Their own stated objective is the pitch:** *"Global Booking – Local Payment"* — AR2025 p.89, verified in the PDF
- 💼 **New CEO from 29 Apr 2026, Nguyễn Thanh Sơn**, whose VietJet background is **flight product development, distribution systems, marketing and revenue strategy**. A distribution-native CEO is an unusually favourable profile for a checkout conversation — [The Investor](https://theinvestor.vn/vinaconex-vietjet-have-new-ceos-d18987.html)
- 💰 **Galaxy Pay's charter capital raised ~6x to VND 300bn, Aug 2026.** ⚠️ Publicly attributed to **Starlink in-flight internet**, not payments. The defensible read is that the payments subsidiary is the group's digital-investment vehicle and now has board attention and capital — [Vietstock](https://vietstock.vn/2026/08/vietjet-tang-von-tai-cong-ty-vi-dien-tu-gap-6-lan-de-dau-tu-starlink-737-1481203.htm)
- 🤝 **Rails still being added and removed:** Google Pay (7 Apr 2026), DOKU (~Oct 2025), PayU India, and **VNPAY-QR switched off from 01/06/2026**. **PayPal, Trustly and VietQR Global are announced for late 2026 / Q3 2026** — an active roadmap, which means an active decision window

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach VietJet Air` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

**Four constraints before anyone drafts:**
1. **Never suggest they lack local payment methods.** They have more than any airline in this pipeline, they have an in-house licensed payment company executing a named multi-market strategy, and a Deputy CEO fronts it. That opener does not survive first contact.
2. **Never say "you need orchestration."** Galaxy Pay *sells* a Payment Orchestration Platform. The opening is the gap **inside** their orchestration: three card gateways, each doing its own routing, with nothing deciding across them.
3. **Respect the build.** In-house motion. Anchor on reach and opportunity cost — what it costs to hand-build a PSP integration per country as the network adds Sri Lanka, the Philippines, Kazakhstan and Europe.
4. ⚠️ **Do not confuse Vietnam Airlines with VietJet.** Adyen has published a Vietnam Airlines case study quoting a 5% authorisation uplift. That is the *competitor*. Getting this wrong in touch one would end the thread.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 13 / 24
| Signal | Points | Status |
|--------|--------|--------|
| Orchestration status | **+1** | ✅ **In-house layer confirmed**, by their own product marketing. Scored +1 per the matrix. See the override note — the +1 assumes a merchant who built a routing layer, and Galaxy Pay explicitly attributes the routing to its vendors |
| 3+ countries | **+3** | ✅ **254 routes, 202 international**, 15+ destination countries, **21 currencies** in their live booking widget, and 6 legal entities across 5 jurisdictions. Sourced from AR2025 and direct observation |
| Multiple PSPs | **+3** | ✅ Overwhelmingly met: CyberSource, MPGS, Adyen, PayU, DOKU, 2C2P, SmartroPAY, AzuPay, NAPAS, Payoo, MoMo, ZaloPay, plus Galaxy Pay's own gateway. Three acquiring banks behind the card gateways |
| Local rail or licensing gap in a top-3 market | **0** ⬜ | ⬜ **Unscoreable, not unmet.** The rule requires a **top-3 traffic** market, and no traffic ranking exists. Real gaps are documented (PromptPay in Thailand, KakaoPay/Toss in Korea, ShopeePay in Vietnam) and four regulatorily-gated markets have no entity (India, China, Korea, Indonesia) — **but I cannot show any of them is top-3, so I am not awarding the points** |
| Recent expansion | **+2** | ✅ Abundant and recent: Sri Lanka (Aug 2026, new country), five Philippines/Japan/Thailand routes (Nov 2026), Shizuoka (Apr 2026), Russia and Kazakhstan (2025), 22 new routes in 2025 |
| Payment issues reported | **+2** | ✅ **Moderate.** Two distinct clusters: money debited with no ticket issued (**6 distinct threads**, incl. a multi-page VOZ thread on VietQR) and **foreign-issued cards declined** (**5 distinct English threads spanning several years**). Plus a state wire service headline on refund delays. ⚠️ Thread *existence* is verified; **content is search-summary level only** |
| Funding >$10M | **0** ❌ | ❌ Listed company, no funding round. The Galaxy Pay capital injection (~VND 250bn) is an internal transfer publicly attributed to Starlink, not a raise |
| High traffic outside home | **0** ⬜ | ⬜ **Unscoreable.** Two contradictory estimates (Vietnam 43.55% vs 99.36%). With 202 of 254 routes international this is *probably* met, but probably is not sourced |
| Competitor using orchestration | **+2** | ✅ Verified at source during the Bamboo Airways run, from the vendors' own rosters rather than SEO pages: **Cebu Pacific** on CellPoint Digital's airline customer wall with a named case study, and **Singapore Airlines** on Juspay's airline page |
| Payment job postings | **0** ⬜ | ⬜ **Unscoreable.** Five career portals located (careers.vietjetair.com, jobs.vietjetair.com, galaxypay.vn/career, galaxyholdings.co/en/careers, VietnamWorks) — **none read.** One fetch of Galaxy Pay's careers page would likely settle it |

**Tier:** computed **13 / 24 → 🟢 Medium (8–13)**, one point below ⭐.
**No public payment RFP found** — no RFP override.

> #### ⭐ Analyst override — escalate to High Priority
>
> **1. The matrix does not score volume at all, and volume here is exceptional.** **VND 82,093bn (~US$3.1B) revenue, 28.2M passengers, 152,974 flights, 107 aircraft, 254 routes** — all from an audited annual report, not an estimate. Add **VND 25,280bn (~US$965M) of ancillary revenue, 39% of air transport revenue**, which is a second transactional stream on top of tickets, with a stated target of ≥40%. This is the largest verified transaction base in the entire pipeline. The "absolute volume" override exists to score accounts *down*; the same logic applied honestly scores this one up.
>
> **2. Three signals scored 0 on unobtained data, not absent evidence.** "High traffic outside home" and the top-3 framing of the rail gap both fail for want of a SimilarWeb split; "payment job postings" fails for want of one unfetched page. With 202 international routes and 21 checkout currencies, a proper traffic pull would very likely convert +2. **Realistic ceiling is 15–16 / 24**, which is ⭐ on the arithmetic alone.
>
> **3. The +1 for in-house is mis-calibrated for this specific merchant.** That grade marks merchants who built a routing platform and will say "we already have this". Galaxy Pay built an **aggregation and market-localisation layer** and then, in its own marketing, **attributes the routing decision to MPGS, CyberSource and Adyen** (Section 3B). They own the checkout, the tokenisation, the reconciliation and the wallet — but there is no single brain across three card stacks. That is closer to sophisticated multi-PSP than to in-house orchestration, and it is a real, articulable gap.
>
> **Counterweight, stated plainly: this is the hardest sell in the pipeline.** They own a licensed PSP, they market a Payment Orchestration Platform, a Deputy CEO is its legal representative, and they are executing "Global Booking – Local Payment" market by market with visible success. Expect a sophisticated counterparty. Score it ⭐ for the volume and the specificity of the gap, not for ease.
>
> #### ⚠️ Route-to-Partnerships flag — raise with your manager before sending
>
> `CLAUDE.md` excludes PSPs and payment infrastructure companies from ICP and routes them to Partnerships. **VietJet Air the airline is unambiguously in scope** — it is a carrier, and the payment volume is its own. But **Galaxy Pay is a licensed payment intermediary with a merchant portal, public API docs and a claimed "100+ Partnership & Strategic Clients"**, which puts the subsidiary close to that exclusion line. Two live questions: whether Galaxy Pay is a competitor, a channel or a partner; and whether an approach to the airline cuts across a Partnerships conversation. **Worth resolving internally before touch one, not after.**

### Source Notes
- ✅ **Every financial and operating figure re-verified by me directly in the AR2025 PDF**, not taken from an agent: consolidated revenue VND 82,093bn (2024: 72,045, +13.9%); PBT VND 2,630bn (+44.3%); 152,974 flights; 28.2M passengers *(explicitly "excluding Thai Vietjet")*, ~10M international; load factor 86.0%; RPK 50,862m; 107 aircraft incl. 8 A330; 254 routes = 202 international + 52 domestic; ancillary VND 25,280bn, +4.4%, **39%** of air transport revenue; 2026 plan 115 aircraft / 31M passengers
- ⚠️ **The annual report contradicts itself on ancillary.** One passage gives *"ancillary revenue… VND 25,280 billion… accounting for 39%"*; another gives *"Cargo and ancillary revenue reached VND 25,025 billion, accounting for approximately 40%"*. Both verified in the PDF by me. **Quote the 39% / VND 25,280bn version and do not over-precision it**
- ✅ **"Global Booking – Local Payment"** — verified verbatim by me on page 89 of the AR2025 PDF, inside the Galaxy Pay section
- ✅ **The routing attribution** — verified verbatim by me on galaxypay.vn (Section 3B)
- ✅ **Galaxy Pay licence 51/GP-NHNN, 16 Aug 2021**, and the Galaxy Pay / SkyPay / SkyPOS brand split — vendor site footer
- ✅ **Convenience fee of VND 100,000** — read off the live fee schedule
- ✅ **Checkout front end on `vja-ui.useleadr.com`** and **21 currencies** in the booking widget — directly observed
- ⚠️ **No traffic data.** Not supplied, and three providers failed. The country profile in this report is a **route and currency profile**
- ⚠️ **Complaint content is search-summary only.** Thread URLs verified to exist; not one thread was opened. App Store and Play review text never reached
- ❌ **"Intelisys" is NOT a payment vendor.** I passed it to an agent as an established provider and was correctly pushed back on: `groupIntelisys` is VietJet's **internal UI module name** for the international-card group. **Never name it in outreach**
- 🚩 **The payment fee contradicts itself across two live VietJet pages**, both fetched and read by me on 2026-09-15: the payment-methods page says **55,000 VND domestic / 50,000 international**, the fee schedule says **100,000 VND, identical domestic and international**. *(An earlier draft of this report asserted the 100,000 figure and dismissed 55,000 as stale. That was wrong — both are live, on their own site. Quote the contradiction, not a number.)*
- 🚩 **"GPay" is genuinely ambiguous in their own product and the evidence splits.** The i18n code `VJGPAY` resolves to `"GPAY"` and the legacy `PaymentGpay.*` strings reference activating *the GalaxyPay wallet*; but the public page's method 8 links to user guides at `.../hdsd-google-pay/GGP-User+Guide-Web-eng.pdf`, and Galaxy Pay separately announced Google Pay. **"Google Pay" is zero-occurrence in the checkout bundle** (verified by me). **Avoid the term entirely in outreach and ask on the call**
- ❌ **SkyPay is the wallet only, not the platform.** Calling the platform "SkyPay" would read as sloppy to their payments team

### Success Case Alternatives
- **Wingo** — **Tier 1 and an unusually exact mechanism match.** An airline whose fix was *"automatic retries of failed payments through multiple providers"*, +14% approval rate. VietJet has three card gateways with no cross-vendor retry. LATAM carrier — say so
- **Qatar Airways, Copa Airlines, Avianca** — named Yuno customers on y.uno's own lists. Airline credibility for a carrier that will ask whether Yuno knows aviation. **No published metrics — name them, never attach a number**
- **Viva Aerobus** — 75% of contacted customers completed purchase after a NOVA callback. **A post-failure recovery result, not routing.** Relevant later given the "money debited, no ticket issued" complaints, not as the opening proof
- ❌ **NOT inDrive or Rappi** — multi-country scale is not this account's problem

---

## Executive Summary

Vietjet Aviation JSC (HOSE: VJC) is Vietnam's largest low-cost carrier and, on verified FY2025 numbers, the largest transaction base in this pipeline: **US$3.1B revenue, 28.2 million passengers, 107 aircraft and 254 routes of which 202 are international**, plus **US$965M of ancillary revenue** representing 39% of air transport revenue. The decisive payment finding is that VietJet **owns Galaxy Pay**, a State-Bank-licensed payment company that runs its checkout in every market, markets itself as a *"Payment Orchestration Platform"*, and pursues a stated objective of **"Global Booking – Local Payment"**. The opportunity is not local methods and not the concept of orchestration, both of which they have: it is that Galaxy Pay connects **three separate card platforms — MPGS, CyberSource and Adyen — and openly credits the routing intelligence to those vendors rather than to itself**, leaving three parallel card stacks with no single decisioning layer across them. The motion is **in-house**, and it must be argued on reach and opportunity cost, never on the build being wrong.

---

### Section 1: Website Traffic Analysis by Country

**Data source: all three resolution paths failed. No country split exists in this report.**

1. *Pasted SimilarWeb data* — none supplied; no `accounts/traffic/vietjet-air.md`.
2. *SimilarWeb MCP tools* — not configured.
3. *WebSearch fallback* — produced **two mutually exclusive answers**.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| — | **No country split available** | — | — | — | — |

**What was attempted and what happened:**

| Provider | Result |
|---|---|
| SimilarWeb | **HTTP 202, zero-byte body** — bot challenge. Not retried |
| Semrush | Fetched 200, but country data is gated: the embedded JSON literally carries `"trafficByCountry":[0,{"visible":[0,false]}]` with null values for logged-out clients |
| HypeStat | Fetched 200, **no country section at all**, and the page self-reports `Last update was 2071 days ago` (~Jan 2021) |

**The two contradictory estimates, both `[UNVERIFIED — search summary only]`:**

| Version A | Version B |
|---|---|
| Vietnam 43.55%, India 19.07%, South Korea 6.9%, Australia 6.2%, Thailand 4.91% | Vietnam **99.36%** |

These cannot both be true. Version B is very likely a mis-scrape of a *within-Vietnam* category ranking rather than a country-of-origin split. Version A is directionally coherent with the route network but not one number in it could be verified. **Neither belongs in outreach.** Monthly-visit estimates are equally unusable: 1.2M (Apr 2026, unverified) against 8.7M (HypeStat, ~2021 vintage) — a 7x spread.

**Domain map — this part IS verified, by DNS and HTTP probe:**

| Host | Status | What it is |
|---|---|---|
| `www.vietjetair.com` | 200, 10KB | **JS SPA shell.** Carries no server-rendered content |
| `seo.vietjetair.com` | 200, 840KB | **SSR mirror — where the content actually lives** |
| `vja-ui.useleadr.com` | 200, 716KB | **The booking engine's SSR origin — a third-party platform** |
| `th.vietjetair.com` + `vietjetthai.com` | 200 | **Thai VietJet, a separate 9%-held associate** |
| `skyjoy.vietjetair.com` | 200 | SkyJoy / GJOY loyalty |
| `skypos.vietjetair.com` | 200 | **SkyPOS — SoftPOS, i.e. card-present at counters** |
| `agentapi-booking.` / `agents2.vietjetair.com` | — | **Travel-agent booking channel** |
| `ir.vietjetair.com` | 200 | Investor relations |
| `galaxypay.vn` | 200 | Galaxy Pay (subsidiary) |
| `vietjetair.com.vn`, `m.vietjetair.com` | 200 | Both redirect to `www.` |

**NXDOMAIN — do not cite:** `en.` `jp.` `kr.` `tw.` `cn.` `in.` `au.` `sg.` `id.` `my.` `.vietjetair.com`. **There are no country subdomains other than Thailand** — all markets run path-based locales off the main site. Also NXDOMAIN today: `book.`, `agent.` and `visa.vietjetair.com`, which HypeStat's stale subdomain table still lists. A "booking subdomain" claim would be wrong.

> **Structural point that matters more than the missing split:** Thailand is a **separate legal entity on a separate domain with a separate IATA code (VZ)**, so any single-domain figure for `vietjetair.com` structurally **excludes Thai VietJet**, and Thai acquiring almost certainly sits with Thai VietJet's own merchant setup.

**Currencies in the live booking widget — directly observed, 21 of them:**
`VND · USD · AUD · SGD · CNY · THB · JPY · INR · TWD · MYR · KRW · EUR · GBP · CAD · HKD · NZD · AED · SAR · PHP · IDR · CZK`

⚠️ **AED and SAR are present** — VietJet sells into the Gulf. Per `CLAUDE.md` this does **not** put the account out of territory: an APAC-HQ'd company selling into the Gulf is in scope.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** registered at 302/3 Kim Ma Street, Ngoc Ha Ward, **Hanoi**; operating HQ at Vietjet Plaza, 60A Truong Son Street, **Ho Chi Minh City**. Founded 2007, first flight 2011.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| 🇻🇳 Vietnam | **Vietjet Aviation Joint Stock Company** | Tax code **0102325399**, issued 23 Jul 2007, 31st amendment 14 Aug 2025 | AR2025 note 1.1 |
| 🇻🇳 Vietnam | **Galaxy Pay Company Limited** — 100% | **0316368255**, 10 Apr 2024 · **SBV licence 51/GP-NHNN**, 16 Aug 2021 | AR2025 note 1.5; galaxypay.vn footer |
| 🇻🇳 Vietnam | Swift 247 JSC — ~67% | 0315524536, 27 Nov 2023 | AR2025 note 1.5 |
| 🇻🇳 Vietnam | VietjetAir Cargo JSC — ~64%, indirect | 0312759089, 13 Jun 2024 | AR2025 note 1.5 |
| 🇻🇳 Vietnam | Airport NEO LLC | 0109783334, 19 Oct 2021 | AR2025 note 1.5 |
| 🇻🇳 Vietnam | Victoria Aviation Academy JSC — 95% | 0316563111, 31 Dec 2025 | AR2025 note 1.5 |
| 🇸🇬 Singapore | Vietjet Air Singapore Pte. Ltd. — **aircraft trading only** | 201408849N, 27 Mar 2014 | AR2025 note 1.5 |
| 🇮🇪 Ireland | Vietjet Air Ireland No. 1 Limited — aircraft leasing | 544879, 3 Jun 2014 | AR2025 note 1.5 |
| 🇻🇬 BVI | Vietjet Air IVB No. I and No. II Limited — aircraft leasing | 1825671 / 1825613, 27 May 2014 | AR2025 note 1.5 |
| 🇰🇾 Cayman | Skymate Limited — indirect | 327015, 15 Sep 2017 | AR2025 note 1.5 |
| 🇹🇭 Thailand | **Thai Vietjet Air JSC — ASSOCIATE at ~9%, NOT consolidated** | 0105556100551, 25 Jun 2013 | AR2025 note 1.5 |

⚠️ **Vietjet Qazaqstan is NOT a VJC entity.** Qazaq Air was rebranded Vietjet Qazaqstan, but the acquirer was **Sovico Group**, VJC's parent/affiliate. It appears nowhere in VJC's AR2025 group structure — neither subsidiary nor associate. **Do not describe it as a VietJet subsidiary.**

**Cross-Border Gap Analysis:**

| Country | Route presence | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|---------------|-------------------|---------------------------|---------------------|
| 🇻🇳 Vietnam | Home, 52 domestic routes | ✅ VJC + **licensed Galaxy Pay** | Yes | **Low** — the one clean market |
| 🇮🇳 India | *"largest number of routes between Vietnam and India"* | ❌ | **Yes** 🔒 | **Mitigated** — PayU gives INR, UPI and Net Banking without a local entity |
| 🇹🇭 Thailand | Major | ❌ (9% associate only) | Yes | **High** — a non-consolidated associate is not a merchant vehicle |
| 🇰🇷 South Korea | Major | ❌ | **Yes** 🔒 | **High** — SmartroPAY covers cards; no local wallet rails |
| 🇮🇩 Indonesia | Wide-body service | ❌ | **Yes** 🔒 | **Mitigated** — DOKU gives IDR and QRIS |
| 🇨🇳 China | 5 new routes in 2025 | ❌ | **Yes** 🔒 | **High** — Alipay and WeChat Pay reachable only cross-border |
| 🇯🇵 Japan | Growing, +Shizuoka 2026 | ❌ | No | **Medium** — 2C2P |
| 🇦🇺 Australia | 5 largest cities | ❌ | No | **Medium** — PayID via AzuPay |
| 🇹🇼 🇭🇰 🇲🇾 🇰🇭 🇱🇦 🇷🇺 🇰🇿 🇱🇰 🇵🇭 | Live or launching | ❌ | Varies | **Unassessed** |

> *Warning: VietJet sells into 15+ countries across **202 international routes** and prices in **21 currencies**, from essentially **one commercial jurisdiction**. Every overseas entity it holds is an aircraft-financing SPV whose registered activity is "trade and lease aircraft" — none is a merchant vehicle.*

> *Regulatory gate: India, China, South Korea and Indonesia each effectively require local presence or a licensed local partner for domestic acquiring. VietJet has no entity in any of them and has answered with **local PSP partnerships instead of local incorporation** — PayU in India, DOKU in Indonesia, SmartroPAY in Korea. That is a deliberate, working strategy, and it is precisely the strategy that an orchestration layer either accelerates or replaces.*

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Global — Visa | **CyberSource** | `[Vendor Site]` + `[Annual Report]` | [galaxypay.vn](https://galaxypay.vn/cong-thanh-toan-da-te-giai-phap-thanh-toan-the-quoc-te-da-ngoai-te/) · AR2025 p.89 |
| Global — Mastercard | **MPGS** | `[Vendor Site]` + `[Annual Report]` + `[Source Code]` (`choose_payment_vjpmpgs`) | same |
| International | **Adyen** | `[Annual Report]` + `[Vendor Site]` — **role and markets never scoped** | AR2025 p.89 |
| Acquiring banks | **HDBank, Vietcombank, VietinBank** | `[Vendor Site]`, verbatim: *"thông qua việc hợp tác các ngân hàng (HDBank, Vietcombank, Vietinbank)"* | [galaxypay.vn](https://galaxypay.vn/cong-thanh-toan-da-te-giai-phap-thanh-toan-the-quoc-te-da-ngoai-te/) |
| 🇮🇳 India | **PayU** — INR, cards, Net Banking, **UPI**, no FX at checkout | `[Press Release]` | [galaxyholdings.co](https://galaxyholdings.co/en/galaxy-pay-integrates-indias-payu-payment-platform-into-vietjet-airs-website-and-app/) |
| 🇮🇩 Indonesia | **DOKU** — IDR, local cards, bank transfer, e-wallets, **QRIS** (~Oct 2025) | `[Press Release]` | [galaxypay.vn](https://galaxypay.vn/vietjet-air-va-galaxy-pay-mo-rong-phuong-thuc-thanh-toan-noi-dia-tai-indonesia-voi-doku/) |
| 🇹🇭 Thailand **and 🇯🇵 Japan** | **2C2P** | `[Vendor Site]` + `[Checkout]` (`payment_2c2p.pdf`) | orchestration article; vietjetair.com method 6 |
| 🇰🇷 Korea | **SmartroPAY** | `[Vendor Site]` + `[Source Code]` (`VJPSMAR`) | orchestration article |
| 🇦🇺 Australia | **AzuPay** (PayID/NPP) | `[Source Code]` (`VJPAZID`) + `[Press]` | orchestration article |
| 🇻🇳 Vietnam | **NAPAS** — direct connection *"to optimise processing cost"* | `[Vendor Site]` + `[Checkout]` | orchestration article |
| 🇻🇳 Vietnam | **Payoo** (cash/bill-payment), **MoMo**, **ZaloPay**, **Movi**, **HD Saison**, **HDBank**, **VPBank** | `[Checkout]` + `[Source Code]` | payment-methods page; booking i18n |
| All | **Galaxy Pay** — own gateway, **SkyPay** wallet, **SkyPOS** SoftPOS | `[Vendor Site]` + `[Annual Report]` | galaxypay.vn |
| — | **Checkout front end: `vja-ui.useleadr.com`**, a third-party platform | `[Source Code]`, directly observed | — |

**Schemes accepted:** Visa, Mastercard, JCB, American Express, UnionPay, Diners Club, Discover, plus NAPAS domestic.

⚠️ **"Intelisys" is not a vendor.** `PaymentMethodsEdit.groupIntelisys.title` is VietJet's internal module name for the international-card UI group. No external evidence of a payments company by that name exists in Galaxy Pay's partner network, the annual report or any press. **Never name it.**

#### 3B. Payment Orchestrator

**Classification: In-house orchestration layer — with the decisive qualification that the routing is not theirs.**

Galaxy Pay markets a product called **"Nền tảng điều phối thanh toán" / "Payment Orchestration Platform"**, runs a 22-article content category by that name, and titles an article *"Giải quyết bài toán **Payment Orchestration** trong ngành hàng không toàn cầu"* ("Solving the Payment Orchestration problem in global aviation").

**No third-party orchestrator.** VietJet and Thai VietJet appear nowhere on CellPoint Digital's published airline roster (Cebu Pacific, Emirates, Riyadh Air, Oman Air, Avianca, Gol, Arajet, Air Europa, Icelandair, Southwest, Virgin Atlantic, La Compagnie, KM Malta, Beond, Sunrise). No Juspay, Spreedly, Primer, Gr4vy, APEXX, Payrails or Yuno result exists.

**The architecture, verbatim from Galaxy Pay's own article** (verified by me, published 2026-06-16):

> *"Galaxy Pay đã cùng hãng hàng không xây dựng một **hệ sinh thái thanh toán đa tầng** thông qua việc kết nối trực tiếp với **ba nền tảng xử lý giao dịch hàng đầu thế giới gồm MPGS (Mastercard Payment Gateway Services), CyberSource (Visa) và Adyen**."*
> — "Galaxy Pay has built with the airline a **multi-layer payment ecosystem** by connecting directly to **three of the world's leading transaction-processing platforms: MPGS, CyberSource and Adyen**."

**And then, in the same article, the sentence that defines the opportunity:**

> *"Tối ưu tỷ lệ chấp thuận giao dịch: **Thông qua cơ chế định tuyến thông minh của MPGS, CyberSource và Adyen**, mỗi giao dịch được chuyển đến đơn vị xử lý phù hợp nhất theo từng thị trường và loại thẻ. Điều này giúp giảm đáng kể tỷ lệ giao dịch bị từ chối không chính xác (**False Declines**)."*
> — "Optimising transaction approval rates: **through the smart-routing mechanism of MPGS, CyberSource and Adyen**, each transaction is routed to the most suitable processor by market and card type, significantly reducing **false declines**."

**Read it plainly.** Galaxy Pay owns the checkout, the market localisation, the tokenisation, the reconciliation and the wallet. It decides **which rail family a market gets**. But the **cross-acquirer, card-level routing it markets as a benefit is MPGS's, CyberSource's and Adyen's own** — each optimising inside its own estate. **Three parallel card stacks, three separate routing brains, and nothing deciding across them.**

> *Confirmed orchestration-aware, and then some — they sell orchestration. The opening is not whether to orchestrate. It is that the layer they built stops at the gateway boundary, and no component in the stack can move a declined transaction from CyberSource to Adyen.*

**A second, softer wedge:** Galaxy Pay has a merchant portal, public API docs and a claimed "100+ Partnership & Strategic Clients", but the only named non-VietJet relationships are inside the Sovico/HDBank family, and related-party disclosures show the scale — Galaxy Pay's services to VietJet were **VND 230.8bn** in FY2025 versus **VND 1.9bn** to Galaxy Joy and **VND 48.8 million** to HD Insurance. **Roughly 96% of Galaxy Pay's throughput is its own parent.**

> **MANUAL:** the gateway handoff happens in an XHR from the SPA. No `vpc_`, `vnp_`, `SecureHash`, `accessCode` or `merchantId` appears in the SSR mirror. A real booking session with DevTools would reveal which acquirer serves which scheme and market — the single highest-value manual check in this account.

---

### Section 4: Alternative & Local Payment Methods

> **⚠️ How to read this section — the evidence has two different strengths, and they disagree.**
>
> **Source A, the checkout i18n bundle.** VietJet's server-rendered pages inline a complete **23-entry payment-method label table**. That table is the **entire universe of methods the checkout UI can render**, so a method absent from it cannot appear anywhere. Absences here are **sourced and strong**.
>
> **Source B, Galaxy Pay's marketing.** Their orchestration article and partnership pages claim a wider set — Apple Pay, Google Pay, Samsung Pay, WeChat Pay, UnionPay, QRIS, PayPal, Trustly, Klarna and more.
>
> **These conflict, and the conflict is itself a finding.** Galaxy Pay is a PSP serving more than one merchant; what Galaxy Pay *can* process is not the same as what **VietJet's checkout renders**. Where the two disagree below, I give both and say which is which. **A further caveat on Source A:** availability is filtered **server-side at runtime** (`GET_VALID_PAYMENT_METHOD_FAILED`, `HAVE_NO_PAYMENT_METHOD`), so the bundle proves the universe but **not which market gets which method**. That needs a live booking per point of sale.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| 🇻🇳 Vietnam | NAPAS domestic cards (40+ banks) | Cards | **Active in checkout** | payment-methods page |
| 🇻🇳 Vietnam | VietQR / dynamic QR | Bank transfer / A2A | **Active in checkout** | payment-methods page |
| 🇻🇳 Vietnam | MoMo · ZaloPay · **SkyPay** (own) | Digital wallet | **Active** | booking i18n; orchestration article |
| 🇻🇳 Vietnam | **Payoo** cash at bill-payment points; cash at VietJet offices and HDBank | Cash/voucher | **Active** | payment-methods page method 2 |
| 🇻🇳 Vietnam | **Movi** BNPL · **HD Saison** instalments (up to 6 months, no income proof) | BNPL/Instalments | **Active** | booking i18n; VietJet's own guide pages |
| 🇻🇳 Vietnam | HDBank and **VPBank** co-brand cards | Cards | **Active** | AR2025 p.89 |
| 🇻🇳 Vietnam | **ShopeePay** | Digital wallet | ❌ **Not found** — Vietnam Airlines carries it | booking i18n |
| 🇻🇳 Vietnam | **VNPAY-QR** | Bank transfer / A2A | 🚩 **BEING DISCONTINUED from 01/06/2026** | [galaxypay.vn notice](https://galaxypay.vn/thong-bao-ngung-ho-tro-quet-ma-vnpay-qr-tu-01-06-2026/) |
| 🇮🇳 India | **UPI**, Net Banking, local cards, INR pricing | Wallet / A2A / Cards | 🚩 **CONFLICT.** Galaxy Pay announced a **PayU** integration giving INR, UPI and Net Banking. But **UPI, RuPay, netbanking, Paytm and PayU are all zero-occurrence in the checkout bundle**, and INR is a supported booking currency with no Indian rail attached. Either the announcement has not reached the checkout, or PayU renders by redirect without a label. **Ask; do not assert either way.** | galaxyholdings.co vs. i18n bundle |
| 🇮🇩 Indonesia | **DOKU** confirmed in the bundle. **QRIS, virtual account, OVO, DANA, GoPay** absent from it | A2A / Wallet | **DOKU active.** QRIS is claimed in Galaxy Pay's announcement but absent from the bundle — it may be delivered behind DOKU without its own label. **The one absence here I would caveat rather than assert** | galaxypay.vn; i18n bundle |
| 🇹🇭 Thailand | Cards (Visa/MC/Amex/JCB) + **Pay Later at counter**; via 2C2P: global card, **QR into a digital-payment app**, **ATM/kiosk**, **internet/mobile banking**, WebPay/direct debit, **QR scanned in mobile banking** | Cards / A2A / Cash | **Active.** See the Thailand detail below — this is the best-evidenced market in the report | th.vietjetair.com; 2C2P PDF |
| 🇹🇭 Thailand | **PromptPay** · TrueMoney · Rabbit LINE Pay · instalments | A2A / Wallet | ❌ **Not named anywhere.** A Thai QR-into-mobile-banking rail *does* exist via 2C2P, which is structurally the Thai QR standard — **but the PromptPay brand appears nowhere**, including in the raw bytes of 2C2P's own PDF | 2C2P PDF; th. payment page |
| 🇰🇷 Korea | Local card PG | Cards | **Active via SmartroPAY** | orchestration article |
| 🇰🇷 Korea | **KakaoPay · Naver Pay · Toss** | Digital wallet | ❌ **Not found** | — |
| 🇯🇵 Japan | Cards via 2C2P | Cards | **Active** | orchestration article |
| 🇯🇵 Japan | **konbini · PayPay · LINE Pay · Paidy** | Cash / Wallet | ❌ **Not found** — *Vietnam Airlines carries konbini at five chains* | — |
| 🇨🇳 China | **Alipay** (`VJPALI`) confirmed. **WeChat Pay and UnionPay ABSENT from the bundle** — the only `WeChat` hit is a social-media follow link | Digital wallet | Alipay **Active**; WeChat Pay and UnionPay claimed by Galaxy Pay's article but **not renderable by the checkout**. One-wallet-deep in China | i18n bundle vs. orchestration article |
| 🇦🇺 Australia | **PayID** (AzuPay) | A2A real-time | **Active** | orchestration article |
| 🇦🇺 Australia | BPAY · PayTo · Afterpay · Zip | A2A / BNPL | ❌ Not found | — |
| 🇪🇺 Europe, 🇳🇿 NZ | **Klarna · Riverty · Alma · Oney** | BNPL | **Active on long-haul routes** | orchestration article |
| 🇹🇼 Taiwan | JKOPay · LINE Pay TW · ATM · store cash | Wallet / Cash | ❌ Not found | — |
| Global | **Apple Pay · Google Pay · Samsung Pay** | Digital wallet | 🚩 **CONFLICT. All three are zero-occurrence in the checkout bundle.** Galaxy Pay announced Google Pay (reportedly 7 Apr 2026) and lists Apple Pay; the airline's own checkout shows no string for any of them. Possibly app-only, possibly Galaxy-Pay-wide rather than VietJet-specific. **Do not claim VietJet accepts them** | galaxyholdings.co vs. i18n bundle |
| Global | **PayPal · Trustly** | Wallet / A2A | 📅 Announced for end-2026 by Galaxy Pay; **both zero-occurrence in the bundle**, consistent with not-yet-live | orchestration article |
| Global | **VietQR Pay + VietQR Global** | A2A cross-border | 📅 **Announced, expected Q3 2026** | orchestration article |
| All | **SkyPOS** SoftPOS at domestic and international airports | Card present | **Active** | galaxypay.vn |

> *Warning: In Thailand, PromptPay is the dominant domestic A2A rail and was not found on any VietJet property — the Thai storefront routes to bank transfer via 2C2P. **Caveat that matters: Thai VietJet is a separate 9%-held associate with its own merchant setup**, so this gap may not even be VietJet's to fix.*

> *Warning: In Japan, konbini is a mainstream payment channel for travel and was not found. Vietnam Airlines publishes konbini acceptance at 7-Eleven, Lawson, Ministop, FamilyMart and Seicomart under JPY 300,000. That is a direct, verifiable competitive contrast on the same route market.*

> *Warning: In South Korea, KakaoPay, Naver Pay and Toss are all absent; SmartroPAY covers cards only. Vietnam Airlines publishes both KCP and KakaoPay.*

### 🇹🇭 Thailand in detail — the best-evidenced market, and the best single hook

Thai VietJet publishes its own payment page at `th.vietjetair.com/page/payment-method`. Its method rows are **logo images with empty `alt` attributes**, invisible to text scraping — they had to be downloaded and read visually. The complete enumerated list is:

**Credit/Debit Card · MasterCard · American Express · JCB · Pay Later** (payable at the airport counter, within 6 hours from web/app or 12 hours).

**That is the whole list. Four card schemes and a counter-payment option.** No PromptPay, no TrueMoney, no Rabbit LINE Pay, no instalments.

The *"Thailand Banks"* link on the main site resolves to a 2C2P guide PDF enumerating six options: global card payment, **digital payment by QR**, **ATM/kiosk**, **internet/mobile banking**, WebPay/direct debit, and **QR scanned in mobile banking**. Options 2, 4 and 6 are QR-into-a-Thai-bank-app, which is *structurally* the Thai QR standard — but **searching the PDF's raw bytes for `PromptPay`, `TrueMoney`, `Rabbit`, `ShopeePay` and `Counter Service` returns zero hits.** Safe phrasing for outreach: *"Thai QR and mobile-banking transfer via 2C2P, unbranded."* **Never write "VietJet offers PromptPay."**

> 🚩 **And the hook: that Thailand payment guide has not been touched since 23 December 2022.** The PDF's own metadata gives `CreationDate = D:20221223182131+08'00'`. Nearly four years without an update, on the payment documentation for a market where they operate a joint-venture airline with its own AOC.

⚠️ **Whose problem is it?** Thai VietJet is a **9%-held associate, not consolidated**, on its own domain and IATA code. This gap may not be VietJet's to fix, and asserting otherwise to VJC would be a misread. Raise it as a question.

**One more Thailand data point, unverified:** a Thai tech blog reports Vietjet Thailand opened payment via **ShopeePay and SPayLater instalments** until 31 Oct 2026, delivered through **Monee and 2C2P by Antom**. `[UNVERIFIED — third-party blog only]`. It appears on **neither** the Thai payment page nor the checkout bundle, which is consistent with an acquirer-side promotion that never reached their own documentation.

### 🎯 The shape of the estate, counted rather than characterised

**Of the 23 methods in VietJet's checkout bundle, 16 are Vietnam-specific.** Against the nine other APAC markets they fly into, the checkout fields exactly **four** local rails: **Alipay** (China), **AzuPay** (Australia), **DOKU** (Indonesia) and **SmartroPAY** (Korea, cards only).

**Japan, Taiwan and India have no local acceptance at all in the bundle** — despite JPY, TWD and INR all being supported booking currencies. Vietnam Airlines, on the same route markets, publishes konbini at five chains in Japan and KCP plus KakaoPay in Korea.

**This is the real finding, and it is the opposite of what the marketing suggests.** Galaxy Pay's article describes a global, multi-market payment ecosystem. VietJet's actual checkout is a **magnificent Vietnam stack with a thin perimeter**. The gap between those two things is the conversation.

**The honest counterweight, which still stands:** they are closing it, deliberately and recently — PayU for India and DOKU for Indonesia were both announced inside the last 18 months, BNPL runs on Europe and New Zealand long-haul, and PayPal, Trustly and VietQR Global are queued. **A pitch built on "you lack local methods" will be met with a roadmap.** The pitch that survives is about the *rate* at which a per-country integration model can keep up with a network adding Sri Lanka, the Philippines, Kazakhstan and Europe.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| **Money debited, no ticket issued**; duplicate charges on retry | VOZ forum, Facebook groups, baynhe.vn, TripAdvisor | **Moderate — 6 distinct threads**, one running to page 2, another to comment-page 4 | Mostly undated | [VOZ](https://voz.vn/t/mua-ve-may-bay-vietjet-thanh-toan-bang-vietqr-tien-da-chuyen-nhung-mua-ve-van-khong-thanh-cong-co-phai-vietjet-lua-dao.1014081/page-2) · [baynhe.vn](https://baynhe.vn/tin-tuc/canh-bao-loi-thanh-toan-online-ve-vietjetair) · [FB](https://www.facebook.com/groups/touristhelpline/posts/24141205432136236/) |
| **Foreign-issued cards declined or auto-cancelled** | TripAdvisor ×3, FlyerTalk, airlines-inform | **Moderate-to-high — 5 distinct English threads spanning several years**, still recurring | Multi-year | [TripAdvisor](https://www.tripadvisor.com/ShowTopic-g293921-i8432-k15119228-Vietjet_credit_card_not_accepted-Vietnam.html) · [FlyerTalk](https://www.flyertalk.com/forum/other-asian-australian-south-pacific-airlines/1433246-trouble-booking-both-vietnam-airlines-vietjetair-website.html) |
| **Refund delays** on delayed/cancelled flights | VietnamPlus (state wire service) | Authority-level signal | — | [VietnamPlus](https://www.vietnamplus.vn/vietjet-cham-boi-hoan-tien-cho-hanh-khach-khi-cham-huy-chuyen-bay-post571569.vnp) |
| Convenience-fee perception as a hidden charge | VOZ; Tuổi Trẻ national daily | Low-moderate, and **dated** | 2018, 2024 | [Tuổi Trẻ 2024](https://tuoitre.vn/gia-ve-may-bay-hang-bay-choi-chieu-voi-cac-khoan-phu-thu-la-20240526231553514.htm) |

> ⚠️ **Read this before using any of the above.** Thread **existence** at those URLs is verified. **Not one thread was opened** — all content descriptions are search-summary level. App Store and Google Play review text was never reached. The frequency labels reflect *distinct sources counted*, not verified report volume.

> *Pattern: the foreign-card decline cluster is exactly a cross-border approval-rate problem and is the most commercially relevant finding in this section.* **But note the timing:** most of those threads predate the **PayU India** and **DOKU Indonesia** integrations, which are VietJet's own answer to the same problem in two specific markets. Pitching the gap without acknowledging they have already started closing it would be a misread.

**April 2025 mass-delay episode** — VietJet apologised and compensated with e-vouchers (VND 500,000 domestic / 1,000,000 international) for flights delayed 2h+ on 20–21 Apr 2025; passengers publicly demanded cash instead. **This is operational, not payments. Do not stretch it.**

**One observation worth a question:** a page titled *"Refund policy applies to Korea point of sales"* exists, CMS id `1772425411505`. VietJet's CMS ids are epoch-milliseconds, which dates that page to **~2 March 2026**. A Korea-specific refund policy published this year may indicate a Korean regulatory or PG issue. `[INFERENCE from the id scheme, not confirmed]`

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | **Aug 2026** | **Sri Lanka — new country.** HCMC ⇄ Colombo, 4x weekly | Market Expansion | [thetraveler.org](https://www.thetraveler.org/vietjet-vietnam-airlines-reshape-2026-sri-lanka-links/) |
| 2 | **From 10 Nov 2026** | **Five new routes** to the Philippines (HCMC–Cebu, Hanoi–Cebu, HCMC–Clark), Japan and Thailand | Market Expansion | [aviationnews.eu](https://aviationnews.eu/news/2026/08/vietjet-accelerates-asian-network-expansion-with-five-new-routes-to-the-philippines-japan-and-thailand/) |
| 3 | **29 Apr 2026** | **New CEO Nguyễn Thanh Sơn**, previously leading flight product development, **distribution systems**, marketing and revenue strategy. Đinh Việt Phương moves to First Vice Chairman | Leadership Change | [The Investor](https://theinvestor.vn/vinaconex-vietjet-have-new-ceos-d18987.html) · [Vietnam News](https://vietnamnews.vn/economy/1516955/vietjet-has-new-senior-leaders.html) |
| 4 | **Aug 2026** | **Galaxy Pay charter capital raised ~6x to VND 300bn.** ⚠️ Publicly attributed to **Starlink in-flight internet**, not payments | Funding (internal) | [Vietstock](https://vietstock.vn/2026/08/vietjet-tang-von-tai-cong-ty-vi-dien-tu-gap-6-lan-de-dau-tu-starlink-737-1481203.htm) |
| 5 | **2025** | 22 new routes; **Russia (Vladivostok, Kazan) and Kazakhstan** entered; 5 new China routes; wide-body fleet to 8 A330 | Market Expansion | AR2025 |

**No public payment-related RFP found.**
**Payment job postings: NOT CHECKED, not absent.** Five career portals were located and none read — `careers.vietjetair.com`, `jobs.vietjetair.com`, `galaxypay.vn/career`, `galaxyholdings.co/en/careers`, and a VietnamWorks employer page for **Galaxy Digital Holdings**. **Galaxy Pay's careers page is the highest-value unchecked source in this report and is one fetch away.**

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | **7 Apr 2026** | **Google Pay live** on VietJet web and app, tokenised | New method | [galaxyholdings.co](https://galaxyholdings.co/en/galaxy-pay-enhances-the-flight-booking-experience-for-vietjet-air-customers-with-google-pay-as-a-payment-method/) |
| 2 | **~Oct 2025** | **DOKU Indonesia** — IDR pricing, QRIS, local e-wallets | New market rail | [galaxypay.vn](https://galaxypay.vn/vietjet-air-va-galaxy-pay-mo-rong-phuong-thuc-thanh-toan-noi-dia-tai-indonesia-voi-doku/) |
| 3 | Date not found | **PayU India** — INR, UPI, Net Banking, no FX at checkout | New market rail | [galaxyholdings.co](https://galaxyholdings.co/en/galaxy-pay-integrates-indias-payu-payment-platform-into-vietjet-airs-website-and-app/) |
| 4 | **Early 2026** | **Galaxy Pay wallet renamed SkyPay.** Exact date unconfirmed; "beginning of 2026" | Rebrand | [galaxypay.vn](https://galaxypay.vn/chinh-thuc-doi-ten-thanh-vi-skypay/) |
| 5 | **From 01/06/2026** | 🚩 **VNPAY-QR discontinued** | **Provider removal** | [galaxypay.vn](https://galaxypay.vn/thong-bao-ngung-ho-tro-quet-ma-vnpay-qr-tu-01-06-2026/) |

> **REMOVAL: VietJet/Galaxy Pay discontinued VNPAY-QR scanning as of 01/06/2026.** The `VJVNPAY` and `VJVNQR` codes still sit in the live i18n bundle, so the removal may be partial or still propagating. **This is the most time-sensitive hook in the account** — a merchant actively removing a rail is a merchant reviewing its rail mix.

**Announced and not yet live:** PayPal and Trustly (expected end-2026), VietQR Pay and VietQR Global (expected Q3 2026).

---

### Section 8: Checkout Experience Audit

**Partially accessible.** The published payment-methods page and fee schedule were read in full. The live checkout was **not** walked — the booking engine is a JS SPA served from a third-party origin, and the gateway handoff happens in an XHR.

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | **Custom, vendor-hosted front end on `vja-ui.useleadr.com`** (Next.js + MUI), canonical back to `www.vietjetair.com`, `hreflang` for vi/en/th/ko/zh-cn | Fair | **The checkout UI layer is already outsourced.** Changes who an integration conversation is with |
| Guest checkout | **Not observable.** Sign-up/sign-in exists; Manage Booking retrieves by reference rather than login, which is guest-compatible | Unknown | Purchase never walked |
| Card input experience | Native card form rendered in VietJet's own page (`PaymentIntelisys.IntelisysType.cardTitle`, billing-address checkbox); a "Modal Checkout" tag hints at hosted fields | Unknown | Cannot distinguish iframe from self-hosted |
| Payment methods visible | Published page lists **8 channels** | **Poor** | ⚠️ It does **not** mention Google Pay, PayU, DOKU, 2C2P, MPGS, SmartroPAY or AzuPay, all documented live elsewhere. The page's CMS id dates it to **Dec 2020** |
| Location-based method display | **Not observable on the published page** — it is a single static page with no storefront conditionality | Unknown | Either the page is badly stale, or rendering is dynamic and undocumented. **Cannot distinguish without a live checkout** |
| Instalment / EMI options | Movi and HD Saison in Vietnam; Klarna/Riverty/Alma/Oney on Europe and NZ long-haul | Good | Absent in Japan, Taiwan, Korea where instalments are conversion rails |
| 3DS implementation | **No evidence either way.** Grep for `3ds`, `3-d secure`, `threeds`, `securecode`, `tokeni[sz]e` returned **zero matches** on the pre-search page | Unknown | **A null result on the wrong page. Do NOT claim they lack 3DS** |
| PCI indicator | Card capture appears to render in VietJet's own page | Unknown | See Section 9 |
| Mobile | App-first market; own app plus `webcheckin.` and mobile redirects | Not assessed | — |
| Multi-currency | **21 currencies** in the live widget, with the convenience fee **priced separately in 13 of them** rather than FX-converted | **Good** | Genuine multi-currency sophistication |
| Saved payment methods | **Not observable.** One uncorroborated app review alleges card details are stored without prompting — **not usable** | Unknown | — |
| Error message clarity | Not assessed | — | — |

**🚩 The payment fee — and two of their own live pages contradict each other.** I fetched both today and read both myself:

| Page | What it says |
|---|---|
| **Payment methods** ([link](https://seo.vietjetair.com/en/pages/to-have-a-good-flight-1599448842652/payment-methods-1607073707173)) | *"Note: You will have to pay the payment fee as below:"* → **55,000 VND** domestic · **50,000 VND** international |
| **Fee and charges** ([link](https://seo.vietjetair.com/en/pages/to-have-a-good-flight-1599448842652/fee-and-charges-1599130343851)) | *"8. Convenience service charge (/passenger/sector) (Applied for the first payment of all the payment methods)"* → **VND 100,000**, the same domestic and international, plus **VND 235,000** for Australia / Kazakhstan / Europe routes |

**Both are live. Both were fetched on 2026-09-15.** They disagree on the amount and on whether domestic and international differ. **Do not quote a single figure as fact** — quote the contradiction, which is the better observation anyway. *(The fee schedule's INR row renders as "350,000" against USD 5.00, which is absurd — a site typo. Do not quote it.)*

**Three things follow, and they are the sharpest cost-of-acceptance findings in the account:**

1. **It is not a card surcharge.** Both pages say it applies to *"all the payment methods"*, so it is a flat booking fee, not a method-specific one.
2. **There is no per-method fee ladder — the structure is binary.** The only exemption string in the entire bundle is **AzuPay**: `PaymentMethods.azupay.description` = *"No utility fees apply"* and `PaymentMethods.methods.VJAUDNote` = *"No Utility Fee applies to this option."* Australian PayID is free; everything else is charged. Their cost-of-acceptance ranking is expressed as one bit.
3. **They tell passengers to avoid their own default rails.** Verbatim, `PaymentMethods.methods.note`: ***"We recommend you to choose a free Utility Fee payment option which may be available"***. An airline advising customers away from its fee-bearing methods is an airline whose acceptance cost has become a conversion problem. Verified by me in the page source.

**The commerce surface is far wider than tickets:** SkyShop, hotels, e-vouchers, e-SIM, e-visa, **foreign-currency purchase**, insurance, SkyJoy loyalty, Swift247 express shipping, Sky Holidays, duty free, Green SM airport taxi, Power Pass, plus agent portals and SkyPOS at airports. **Each is a payment integration in its own right, and together they are the 39% ancillary line.**

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **Galaxy Pay: PCI DSS Level 1**, the highest, assessed by **Crossbow Labs**. Month given as May; **year not stated — do not cite one** | [galaxypay.vn/tag/pci-dss](https://galaxypay.vn/tag/pci-dss/) |
| | **VietJet Air itself: Not found.** No level, AoC or QSA for the airline entity | — |
| Card data handling | `[INFERENCE, not confirmed]` scope likely pushed down into Galaxy Pay's Level 1 environment | — |
| Recommended Yuno integration | **SDK / hosted fields**, consistent with their current model and with keeping airline-side scope where it is | — |

**Worth noting for contrast:** Vietnam Airlines publicly holds [PCI DSS Level 2](https://en.vietnamplus.vn/vietnam-airlines-obtains-security-certification-of-pci-dss-compliance-level-2-post266724.vnp). VietJet's silence at airline level, against Galaxy Pay's Level 1, is consistent with scope sitting in the subsidiary.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: Three card gateways, three routing brains, nothing deciding across them.**
> **Evidence:** §3B — Galaxy Pay's own article states it connects *"directly to three leading transaction-processing platforms: MPGS, CyberSource and Adyen"*, and then attributes approval-rate optimisation to *"the smart-routing mechanism of MPGS, CyberSource and Adyen"*. + §5 — five distinct multi-year threads of foreign-issued cards being declined or auto-cancelled.
> **Pain Point:** Each gateway optimises inside its own estate. When CyberSource declines a Visa transaction there is no mechanism to retry it on Adyen, because no component sits above all three. They carry the cost and complexity of three card relationships and get intra-gateway optimisation only. On a carrier doing 28.2M passengers a year, the recovered-revenue arithmetic on even a small cross-gateway retry rate is substantial.
> **Yuno Value Proposition:** One decisioning layer above the three they already run — cascade a decline from one gateway to another, retry on a different acquirer, and keep every existing contract. Additive, and it makes the three relationships they have already paid for worth more.
> **Best Success Case:** **Wingo** — an airline whose published fix was *"automatic retries of failed payments through multiple providers"*, +14% approval rate. The mechanism matches exactly. LATAM carrier; say so.
> **Outreach Angle:** "Galaxy Pay's own write-up credits the routing to MPGS, CyberSource and Adyen. That means each one optimises inside its own estate, and a decline on one has nowhere to go."
> **Suggested Subject Line:** Three gateways, three routing engines

> **Insight #2: "Global Booking – Local Payment" is their stated objective, and they are hand-building it one country at a time.**
> **Evidence:** §3B and AR2025 p.89 — the objective, verbatim, in an audited filing. + §4 — **of the 23 methods in their checkout, 16 are Vietnam-specific**; the nine other APAC markets share exactly four local rails between them, and **Japan, Taiwan and India have none at all** despite JPY, TWD and INR being live booking currencies. + §2 — 202 international routes, 21 currencies, **no commercial entity outside Vietnam**. + §6 — Sri Lanka Aug 2026, five more routes Nov 2026, Russia and Kazakhstan in 2025.
> **Pain Point:** The strategy is right and it is working where it has been applied — DOKU closed Indonesia, SmartroPAY covers Korean cards, 2C2P covers Thailand and Japan. But each was a separate integration, contract and engineering project, and the count tells the story: **sixteen methods at home, four across nine foreign markets.** Their Thailand payment guide has not been updated since **December 2022**. The network is adding countries faster than integrations can be hand-built, and the cost lands as engineering time rather than a line item anyone owns.
> **Yuno Value Proposition:** The same objective, but market entry becomes configuration instead of a project. One integration reaches the rails in markets they have not opened yet.
> **Best Success Case:** Wingo for the mechanism; **Qatar Airways, Copa Airlines and Avianca** named as carriers on the same layer, with no numbers attached.
> **Outreach Angle:** "You've written 'Global Booking – Local Payment' into your annual report. Sixteen of the twenty-three methods in your checkout are Vietnamese, and Japan, Taiwan and India have none at all, while you priced all three in their own currency."
> **Suggested Subject Line:** Global Booking, Local Payment

> **Insight #3: They are removing a rail right now.**
> **Evidence:** §7 — VNPAY-QR discontinued from 01/06/2026, announced on Galaxy Pay's own site, while the `VJVNPAY` and `VJVNQR` codes still sit in the live i18n bundle. + §4 — PayPal, Trustly and VietQR Global all announced for later in 2026.
> **Pain Point:** A merchant simultaneously removing one rail and preparing to add three is actively reviewing its rail mix. That is a decision window, and it is open now.
> **Yuno Value Proposition:** Adding or removing a method stops being a release. It is the cheapest possible proof of the orchestration argument, because they are about to do it three more times by hand.
> **Best Success Case:** Not case-led. This one is a timing observation.
> **Outreach Angle:** "You're switching VNPAY-QR off from June and you've got PayPal, Trustly and VietQR Global queued behind it."
> **Suggested Subject Line:** VNPAY off, PayPal and Trustly on

> **Insight #4: Ancillary is 39% of air transport revenue and has its own target.**
> **Evidence:** §12 and AR2025 — ancillary **VND 25,280bn (~US$965M), +4.4%, 39%** of air transport revenue, with a stated goal of **at least 40%**. + §8 — the commerce surface spans SkyShop, hotels, e-visa, e-SIM, insurance, duty free, foreign-currency purchase, Swift247 and SkyPOS.
> **Pain Point:** Ancillary is a second transaction stream with a different basket profile, often bought post-booking on a different device, and every one of those products is a separate payment integration. An explicit growth target on a stream that already produces nearly a billion dollars makes checkout conversion on the *ancillary* flow a board-level number, not an ops detail.
> **Yuno Value Proposition:** One layer across ticket and ancillary flows, so a new ancillary product inherits the full method set instead of being wired individually.
> **Best Success Case:** **Rappi** for breadth of methods added without implementation delay — a pattern match on provider breadth, not an airline case. Say so.
> **Outreach Angle:** "Ancillary is 39% of your air transport revenue and you've said you want it above 40. Every one of those products is its own payment integration."
> **Suggested Subject Line:** The 39% that isn't the ticket

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. "Galaxy Pay's own write-up says approval rates are optimised 'through the smart-routing mechanism of MPGS, CyberSource and Adyen' — which means three engines each optimising inside their own estate, and a decline on one with nowhere to go."
2. "'Global Booking – Local Payment' is in your annual report, and you're delivering it one integration at a time: PayU for India, DOKU for Indonesia, SmartroPAY for Korea, 2C2P for Thailand and Japan."
3. "Your Thailand payment guide has a creation date of December 2022, and Thailand is a market where you run a joint-venture airline with its own AOC."

**Cold call openers (conversational, one sentence each):**
1. "I read Galaxy Pay's piece on the MPGS, CyberSource and Adyen setup. Can I ask what happens today when a card declines on one of the three?"
2. "You've got 202 international routes and no commercial entity outside Vietnam. How are you deciding which market gets a local acquirer next?"
3. "Ancillary is running at 39% of air transport revenue with a target above 40. Who owns checkout conversion on the ancillary flow as opposed to the ticket?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|----|-----------|-----------------|------------------------|--------|
| **Vietnam Airlines** | vietnamairlines.com | 🇻🇳 Hanoi | 96 aircraft, ~42% VN domestic | VN, JP, KR, AU, EU, US, SEA | **Adyen** — gateway since 2017, **global acquiring since 2024**, publicly quoting **"up to a 5% uplift in authorization rates"**. Deep per-market rails: KCP+KakaoPay (KR), **konbini** at 5 chains (JP), Rabbit LINE Pay (TH), GrabPay (SG), GCash (PH), Touch'n Go (MY), DOKU (ID), Sofort+iDEAL (EU), Afterpay+Zip (AU), MoMo+ShopeePay+VNPAY QR (VN) | [Adyen newsroom](https://www.adyen.com/press-and-media/vietnam-airlines-expands-partnership-with-adyen) |
| **Bamboo Airways** | bambooairways.com | 🇻🇳 | **1 aircraft** — effectively ceased scheduled operations | VN domestic | No orchestrator | `not-icp/bamboo-airways.md` |
| **Vietravel Airlines** | vietravelairlines.com | 🇻🇳 | 3–4 aircraft, ~3% share | VN domestic | Not found | — |
| **Sun PhuQuoc Airways** | — | 🇻🇳 Phu Quoc | **16 aircraft**, launched Oct 2025 | VN domestic | Not found | — |
| **Thai VietJet** | vietjetthai.com | 🇹🇭 | 24 aircraft | TH + regional | Implicitly 2C2P; **separate merchant setup** | — |
| **AirAsia** | airasia.com | 🇲🇾 | 253 group-wide | ASEAN | Not researched | — |
| **Scoot** | flyscoot.com | 🇸🇬 | 53 aircraft | SG, SEA, North Asia | Not researched; parent SIA uses Juspay | — |

#### 11B. Industry Peers

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| **Cebu Pacific** | cebupacificair.com | LCC | 🇵🇭 + SEA | **CellPoint Digital orchestration customer with a published case study** — the closest SEA analogue of an LCC that bought orchestration | CellPoint roster |
| **Singapore Airlines** | singaporeair.com | Full service | Global | **On Juspay's own airline page**; also appears in Adyen's merchant list | Juspay airlines page |
| **IndiGo** | goindigo.in | LCC | 🇮🇳 | Juspay-powered, confirmed by IndiGo's own press release | [IndiGo](https://www.goindigo.in/press-releases/juspay-to-power-payments-for-indias-leading-airline-indigo.html) |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| **Cebu Pacific** | CellPoint Digital | Not stated | LCC, Philippines | CellPoint airline roster + case study |
| **Singapore Airlines** | Juspay | Not stated | Full-service, Singapore | Juspay airlines page |
| **IndiGo** | Juspay | Not stated | LCC, India | IndiGo press release |

**No Vietnamese carrier uses a third-party orchestrator.** Rosters were read at source rather than from vendor comparison pages.

#### 11D. Prospect Scoring
Not run — the competitor landscape was established during the Bamboo Airways run and the findings are recorded in `not-icp/bamboo-airways.md`. Scoring these properly needs a dedicated pass.

#### Top Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | **Vietnam Airlines** | Direct competitor | VN + global | Not scored | P1 | **Already on Adyen global acquiring with a public 5% uplift claim — consolidated single-acquirer, NOT greenfield** | ✅ P1 |
| 2 | **Sun PhuQuoc Airways** | Direct competitor | VN domestic | Not scored | **Genuine find** | 16 aircraft within a year of launch, third-largest fleet in Vietnam, no orchestrator anywhere in that market | ❌ **Not on the TAL** |
| 3 | **Cebu Pacific** | Peer | PH + SEA | Not scored | P1 | **CellPoint incumbent — competitive motion, not greenfield** | ✅ P1 |

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | **VND 82,093 billion ≈ US$3.1B** consolidated, FY2025 (+13.9%). Parent-only VND 81,426bn | AR2025, verified by me in the PDF |
| | H1 2026: consolidated **VND 51,536bn (~US$1.96B), +44% YoY** | `[UNVERIFIED — search summary only]`, concurring trade outlets; HOSE filing not opened |
| GMV / Gross Transaction Volume | Not disclosed as such. **Galaxy Pay TPV FY2025 > VND 15,000bn (~US$572M) across >3M transactions**; SkyPay wallet >VND 640bn, >250k transactions | AR2025 p.89 |
| Average Transaction Value (USD) | `[ESTIMATE]` ~**US$190** implied by Galaxy Pay's VND 15,000bn ÷ 3M transactions | My arithmetic on two sourced figures |
| Est. Annual Transactions | `[ESTIMATE]` **28.2M passengers** is the firmer proxy for payment events, before ancillary | AR2025 |
| Active Customers / Users | 28.2M passengers FY2025 (excl. Thai Vietjet), ~10M international. SkyJoy/GJOY: **2M loyalty members** | AR2025 |
| Primary Currency | **VND**, but **21 currencies** priced in the live booking widget | Direct observation |
| Top 3 Markets by Revenue | **Not disclosed.** AR2025 has no geographic revenue segmentation — only route counts and an international passenger count | AR2025 |
| **Billing channel split (web vs app store)** | **No app-store leakage.** The VietJet app is published by "VIETJET AVIATION JOINT STOCK COMPANY" and sells flights, which fall outside Apple IAP. Web, app, agent API and **SkyPOS** all run on VietJet's own rails | iTunes lookup API, checked by me |

> **Sizing note worth putting in front of the business case.** Galaxy Pay's FY2025 TPV of >VND 15,000bn sits against VietJet's own VND 82,093bn of revenue — **roughly a fifth**. SkyPay, the wallet, is under one percent. *(My arithmetic on two sourced figures. Galaxy Pay's TPV may include non-VietJet merchants, and VietJet's revenue includes cargo and non-card items, so treat it as indicative.)* **The implication is the important part: the majority of VietJet's payment volume does not flow through its own payment company.** It flows through CyberSource, MPGS, Adyen, NAPAS, the banks and the local PSPs — which is exactly where a decisioning layer would sit.

---

### Overall Research Confidence

**High on the payment stack and the financials. Low on traffic.**

**Exceptionally strong:** the financial and operating picture comes from the **audited FY2025 annual report**, which I downloaded and read directly rather than taking from an agent — every headline figure in this report was re-verified against the PDF. The payment stack is equally well sourced: the acquirer set, the three card gateways, the acquiring banks and the routing attribution all come from Galaxy Pay's own site and the annual report, and I verified the two load-bearing quotes myself. **State explicitly: traffic data was neither supplied nor obtainable.**

**Weak, and honestly so:**
- **No country traffic split exists.** Three providers failed and the two search estimates contradict each other outright. The Section 1 table is a **route and currency profile**. Two ICP signals scored 0 as a direct result, and a third could not be framed.
- **Complaint content was never read.** Thread URLs are verified; the threads are not. App-store review text was never reached.
- **The live checkout was never walked**, so method rendering by storefront, 3DS, guest checkout and saved cards are all unresolved.
- **Adyen's role is unscoped.** Named three times, never explained.

---

### Manual Research Recommendations

> **Area:** Traffic split — Section 1 is empty.
> **Why it matters:** Two ICP signals are unscoreable, the ⭐ rests on an override rather than arithmetic, and it decides whether India, Korea or Australia is the market to lead with.
> **Suggested manual action:** Pull SimilarWeb for **`vietjetair.com`** with "Include all country domains" ON. **Pull `vietjetthai.com` separately and do not merge it** — Thai VietJet is a 9%-held non-consolidated associate and is a different payments conversation.

> **Area:** Galaxy Pay's careers page.
> **Why it matters:** It is the single highest-value unchecked source in this report, one fetch away, and a payments engineering or product role would convert an ICP signal and reveal what they are building next.
> **Suggested manual action:** Open `galaxypay.vn/career` and `galaxyholdings.co/en/careers`.

> **Area:** A live checkout walk.
> **Why it matters:** Everything in Section 4 is the documented method list, not an observed one, and their published payment page is stale by five years. Which methods actually render for an Indian, Korean or Australian buyer is the difference between a sharp email and a wrong one.
> **Suggested manual action:** Start a real booking on two storefronts with DevTools open. Capture the acquirer in the network tab — `vpc_` indicates MPGS, and a CyberSource or Adyen host will be visible. This also settles 3DS.

> **Area:** The Partnerships question on Galaxy Pay.
> **Why it matters:** Galaxy Pay is a licensed payment intermediary with a merchant portal and an API. Whether it is a competitor, a channel or a partner changes who owns this account.
> **Suggested manual action:** Raise internally before touch one.

> **Area:** Adyen's actual role.
> **Why it matters:** If Adyen already provides global acquiring for VietJet as it does for Vietnam Airlines, the competitive picture changes materially.
> **Suggested manual action:** Ask directly on the call. There is no VietJet–Adyen press release; the widely indexed Adyen–Vietnam-airline story is **Vietnam Airlines**.

---

### Appendix: All Source URLs

**Primary — fetched and verified by me**
- https://ir.vietjetair.com/File_Upload/financial-information/annual-reports-root/annual-reports/20260417_VJC_AR2025_EN_Final.pdf (123pp, read directly)
- https://galaxypay.vn/galaxy-pay-vietjet-air-toi-uu-ha-tang-thanh-toan-toan-cau-buoc-di-chien-luoc-cung-mpgs-cybs-va-ayden/
- https://seo.vietjetair.com/en/pages/to-have-a-good-flight-1599448842652/payment-methods-1607073707173
- https://seo.vietjetair.com/en/pages/to-have-a-good-flight-1599448842652/fee-and-charges-1599130343851
- https://www.vietjetair.com/en/ · https://th.vietjetair.com/ · https://skypos.vietjetair.com/ · https://skyjoy.vietjetair.com/
- https://crt.sh/?q=%25.vietjetair.com
- iTunes lookup/search API (app-store billing check)

**Galaxy Pay**
- https://galaxypay.vn/cong-thanh-toan-da-te-giai-phap-thanh-toan-the-quoc-te-da-ngoai-te/
- https://galaxypay.vn/tag/pci-dss/ · https://galaxypay.vn/en/partnership/ · https://galaxypay.vn/en/homepage-1/
- https://galaxypay.vn/thong-bao-ngung-ho-tro-quet-ma-vnpay-qr-tu-01-06-2026/
- https://galaxypay.vn/chinh-thuc-doi-ten-thanh-vi-skypay/
- https://galaxyholdings.co/en/galaxy-pay-integrates-indias-payu-payment-platform-into-vietjet-airs-website-and-app/
- https://galaxyholdings.co/en/galaxy-pay-enhances-the-flight-booking-experience-for-vietjet-air-customers-with-google-pay-as-a-payment-method/
- https://galaxypay.vn/vietjet-air-va-galaxy-pay-mo-rong-phuong-thuc-thanh-toan-noi-dia-tai-indonesia-voi-doku/

**Corporate / news**
- https://theinvestor.vn/vinaconex-vietjet-have-new-ceos-d18987.html · https://vietnamnews.vn/economy/1516955/vietjet-has-new-senior-leaders.html
- https://vietstock.vn/2026/08/vietjet-tang-von-tai-cong-ty-vi-dien-tu-gap-6-lan-de-dau-tu-starlink-737-1481203.htm
- https://aviationnews.eu/news/2026/08/vietjet-accelerates-asian-network-expansion-with-five-new-routes-to-the-philippines-japan-and-thailand/
- https://www.thetraveler.org/vietjet-vietnam-airlines-reshape-2026-sri-lanka-links/
- https://finance.vietstock.vn/VJC-ctcp-hang-khong-vietjet.htm?languageid=2

**Complaints — `[UNVERIFIED — search summary only]`, URLs verified to exist, content not read**
- https://voz.vn/t/mua-ve-may-bay-vietjet-thanh-toan-bang-vietqr-tien-da-chuyen-nhung-mua-ve-van-khong-thanh-cong-co-phai-vietjet-lua-dao.1014081/page-2
- https://baynhe.vn/tin-tuc/canh-bao-loi-thanh-toan-online-ve-vietjetair
- https://www.tripadvisor.com/ShowTopic-g293921-i8432-k15119228-Vietjet_credit_card_not_accepted-Vietnam.html
- https://www.flyertalk.com/forum/other-asian-australian-south-pacific-airlines/1433246-trouble-booking-both-vietnam-airlines-vietjetair-website.html
- https://www.vietnamplus.vn/vietjet-cham-boi-hoan-tien-cho-hanh-khach-khi-cham-huy-chuyen-bay-post571569.vnp
- https://tuoitre.vn/gia-ve-may-bay-hang-bay-choi-chieu-voi-cac-khoan-phu-thu-la-20240526231553514.htm

**Competitors**
- https://www.adyen.com/press-and-media/vietnam-airlines-expands-partnership-with-adyen
- https://www.goindigo.in/press-releases/juspay-to-power-payments-for-indias-leading-airline-indigo.html
- https://en.vietnamplus.vn/vietnam-airlines-obtains-security-certification-of-pci-dss-compliance-level-2-post266724.vnp

</details>
