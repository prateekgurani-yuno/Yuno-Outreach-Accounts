# Vietnam Airlines

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 18 / 24 → ⭐ High Priority on the arithmetic → **🟢 Medium, analyst override applied — see the override note**
**Industry:** Airlines (state-owned flag carrier) · **HQ:** Hanoi, Vietnam · **Researched:** 2026-09-15 · **First email sent:** —
**Motion:** **Competitive** — a direct orchestration competitor was signed on 29 May 2026 and is mid-rollout

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Vietnam Airlines JSC (HOSE: HVN) is Vietnam's state-owned flag carrier — 86.42% state-held, with ANA Holdings at 5.62%. FY2025 consolidated revenue VND 123,858bn (~US$4.7bn), 25.6 million passengers, 103 aircraft, 113 routes across 60 destinations in 21 countries. It sells through **39 country storefronts** on a single domain and is midway through a broad digital re-platforming: Amadeus Altéa PSS (2024), a new e-commerce website, and two separate payment-orchestration contracts.

**SimilarWeb total visits (last full month):** **4.5 million** (August 2026) — source: SimilarWeb free page, fetched by Agent 1. Semrush gives 3.17M (Jun) / 4.1M organic for the same property, so **treat 3–4.5M/month as the honest range**. `[ESTIMATE, not confirmed]`

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇻🇳 Vietnam | 44.89% | MoMo (≤VND 50m), ShopeePay, VNPAY QR + Internet Banking, NAPAS ATM (≤VND 200m), ATM/bank-counter/convenience-store cash, card instalments >VND 3m via NganLuong, intl cards, UnionPay, pay-later, Cash & Miles | **Wallets are hidden entirely on mobile web** (their own published note); no PayPal / Alipay / WeChat Pay (all excluded at VN POS); no ZaloPay; no VietQR-branded rail beyond VNPAY | ✅ HQ |
| 2 | 🇯🇵 Japan | 8.06% | Intl cards (Visa/MC/Amex/UATP/JCB), UnionPay, **Konbini via Adyen** (7-Eleven, Lawson, Ministop, FamilyMart, Seicomart; <JPY 300,000; **website only, not app**), Alipay, WeChat Pay (JPY), PayPal, pay-later, Cash & Miles | **No PayPay** (Japan's dominant wallet), no LINE Pay, no Rakuten Pay, no Paidy, no carrier billing, no card instalments / bonus payment, no Japanese bank transfer | ✅ Tokyo, Osaka, Nagoya, Fukuoka |
| 3 | 🇦🇺 Australia | 7.96% | Intl cards, UnionPay, **Afterpay, Zip**, PayPal, Alipay, WeChat Pay, pay-later, Cash & Miles | **No PayTo, no BPAY, no POLi** | ✅ Sydney, Melbourne, Perth (cargo via GSA) |
| 4 | 🇺🇸 USA | 7.59% | Intl cards, UnionPay, PayPal, Alipay, WeChat Pay, pay-later, Cash & Miles | No Apple Pay, no Google Pay, no Affirm/Klarna/Afterpay, no ACH | ⚠️ San Francisco only — one office for 7.59% of traffic |
| 5 | 🇮🇳 India | 5.27% | Intl cards, UnionPay, pay-later, Cash & Miles — **that is the entire list** | **No UPI, no netbanking, no RuPay, no EMI, no wallet of any kind — and India is explicitly excluded from PayPal, Alipay AND WeChat Pay** | ⚠️ "Branch of Vietnam Airlines JSC in India", New Delhi 🔒 domestic acquiring in India is regulatorily gated |

### Legal entities
- **Vietnam Airlines JSC** (Vietnam) — HOSE: HVN, 3,111,498,211 shares outstanding
- Own branch / city / airport offices confirmed in **21 countries**: Japan, South Korea, Australia, USA, Singapore, Taiwan, Thailand, China, Hong Kong, Germany, France, UK, India, Philippines, Indonesia, Malaysia, Cambodia, Laos, Myanmar, Russia, Canada
- **GSA-only, no VNA presence:** Spain, Poland, Italy, Denmark, Netherlands, Israel, Portugal, Finland, Czechia, Belgium, Sweden, Norway, Turkey, UAE — VNA does not control merchant-of-record or settlement in these
- Operating subsidiaries: **Pacific Airlines** (LCC), **VASCO**, **Air Cambodia** (Phnom Penh — the only non-Vietnam operating subsidiary)
- **Sabre Vietnam JSC** — VNA is in a joint venture with Sabre, despite having migrated its PSS to Amadeus

### Known PSPs
- **Adyen** — gateway since 2017; **global acquiring since 2024** (Japan, Australia, US, Europe). Scope per Adyen's own release: cards + "selected local payment methods like Alipay and WeChat Pay." Named by VNA itself on its Japan page as the Konbini redirect target. [Adyen newsroom](https://www.adyen.com/press-and-media/vietnam-airlines-expands-partnership-with-adyen)
- **2C2P by Antom (Ant International)** — **PACO orchestration platform**, signed 29 May 2026, 8 APAC markets, rollout from H2 2026
- **Outpayce (Amadeus) Xchange Payment Platform (XPP)** — "transitioning to" as of June 2024, on VNA's own press room
- **VNPAY** — Vietnam QR + internet banking, since early 2020
- **NganLuong** — gateway for international-card instalments in Vietnam (named on VNA's own help desk)
- **NAPAS** — domestic Vietnamese card scheme, wired into the booking flow
- **MoMo**, **ShopeePay** — Vietnam wallets · **Payoo** — Vietnam cash/counter rails
- **KCP (NHN KCP)** — South Korea domestic cards · **KakaoPay** — Korea
- **DOKU** — Indonesia · **Alipay+** — the single connection behind Touch 'n Go (MY), GCash (PH) and Rabbit LINE Pay (TH)
- **PCI DSS Level 2** since Aug 2023 — the band is "merchants that process 1–6 million credit card transactions annually", a useful volume proxy. QSA: Crossbow Labs. [VietnamPlus](https://en.vietnamplus.vn/vietnam-airlines-obtains-security-certification-of-pci-dss-compliance-level-2-post266724.vnp)

### Orchestration status
**Global orchestrator incumbent — and there are two of them, stacked.** This is the single most important fact on the account and it inverts the usual pitch.

1. **Outpayce XPP (Amadeus)** — from Vietnam Airlines' own press room, 12 June 2024, verbatim: *"Vietnam Airlines is also transitioning to the **Xchange Payment Platform (XPP) from Outpayce**, Amadeus' payments business. This platform allows Vietnam Airlines to easily accept a wide range of card and alternative payment methods from travelers. **With XPP, the carrier can accept payments globally, by connecting to a wide range of specialist partners.**"* — [VNA press room](https://www.vietnamairlines.com/us/en/vietnam-airlines/press-room/press-release/2024/0612-EN-Vietnam-Airlines-successfully-implemented-Amadeus-Altea-PSS)
2. **2C2P by Antom "PACO"** — announced **29 May 2026** at the Vietnam–Singapore Tech Connect Forum during the state visit by Vietnam's General Secretary/President, signed at CEO level (Le Hong Ha, General Director VNA + Gary Liu, CEO Antom). Vietnamese press describes it verbatim as a *"payment orchestration platform… which enables airlines to **dynamically route transactions across multiple acquirers through a single API integration**… designed with **smart retry logic**."* PCI DSS Level 1; integrated with Amadeus and Sabre. — [VIR](https://vir.com.vn/vietnam-airlines-partners-with-2c2p-to-expand-digital-payment-options-154029.html) · [The Paypers](https://thepaypers.com/payments/news/2c2p-by-antom-partners-with-vietnam-airlines-to-expand-localised-payments-across-asia-pacific)

**Do not pitch "you need orchestration." They have bought that thesis twice and said so publicly.**

### Buying signals
- 🤝 **2C2P/PACO orchestration signed 29 May 2026** — 8 markets (SG, MY, TH, PH, JP, KR, AU, HK), Phase 1 domestic bank transfer/QR/internet banking, Phase 2 mobile wallets, live "from H2 2026." **As of 15 Sep 2026 none of the 8 markets shows a new method on their live payment pages — I re-fetched them today.** ([VIR](https://vir.com.vn/vietnam-airlines-partners-with-2c2p-to-expand-digital-payment-options-154029.html))
- 🚀 **Record network expansion:** +14 international routes in 2025, the most in a single year. London Heathrow and Amsterdam added for 2026. `[route specifics UNVERIFIED — low-quality aggregator sources only]`
- 🚀 **Direct-sales channel extended in 2025 to four new markets** — Australia, Taiwan, Laos and the USA (previously only Japan and Korea). New payment geographies they now own directly rather than through agents. (FY2025 Annual Report)
- 💰 **Capital raise:** Phase 1 completed 2025 (897m shares, ~VND 9tn); **Phase 2 of up to VND 13tn from 2026** — but explicitly for debt repayment, against VND 26.69tn accumulated retained losses.
- 📋 **2026 plan, their own words:** *"Strengthen cooperation with metasearch partners, **e-wallet platforms**, non-aviation partners, and banks to enhance added value for passengers purchasing tickets via **online channels**."* (FY2025 Annual Report)
- 💼 **No payment-specific job postings found** — searched both the VNA careers portal and general job boards.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Vietnam Airlines` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

**⚠️ Read the override note in Section 3 before drafting.** My recommendation is **not** to
run a sequence on this account right now. See "Recommendation on timing."

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 18 / 24
| Signal | Points | Status |
|--------|--------|--------|
| Orchestration status | **+1** | ❌ Not greenfield. **Two** orchestration layers contracted: Outpayce XPP (Jun 2024, VNA's own press room) and 2C2P PACO (May 2026). Competitor incumbent = +1. |
| 3+ countries | **+3** | ✅ 39 country storefronts; 21 countries flown to; own offices in 21 countries; 5 countries >5% traffic. |
| Multiple PSPs | **+3** | ✅ Adyen, 2C2P, Outpayce XPP, VNPAY, NganLuong, NAPAS, MoMo, ShopeePay, Payoo, KCP, DOKU, Alipay+ — all evidenced. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Japan (#2, 8.06%)** has its own dedicated enumerated payment page listing only cards/UnionPay/Alipay/Konbini/WeChat/PayPal/pay-later/Cash&Miles — **no PayPay**, Japan's dominant wallet, and no instalments in a market where instalment culture is strong. Sourced absence from an enumerated list, not an assumption. |
| Recent expansion | **+2** | ✅ Record +14 international routes in 2025; direct-sales channel extended to AU/TW/LA/US in 2025; London and Amsterdam for 2026. |
| Payment issues reported | **+2** | ✅ **Moderate** frequency, and structurally persistent: ~6% of ~300 recent app-store reviews across both platforms describe the same payment-step failure, spanning 19 months and surviving the website relaunch. |
| Funding >$10M | **0** | ❌ Deliberately not awarded. The VND 13tn Phase 2 raise is **state recapitalisation for debt repayment** against VND 26.69tn accumulated losses, not growth capital. Awarding this would be gaming the matrix. |
| High traffic outside home | **+2** | ✅ Vietnam is 44.89% — comfortably below the 60% threshold. |
| Competitor using orchestration | **+2** | ✅ Heavily: Malaysia Airlines (Outpayce XPP), Cebu Pacific (CellPoint Digital), Sun PhuQuoc Airways (2C2P PACO), Thai Airways (2C2P), IndiGo (Juspay). |
| Payment job postings | **0** | ❌ None found on the VNA careers portal or general boards. Only Digital Transformation & Technology and Finance & Accounting departmental listings. |

**Tier:** High Priority (14+) ⭐ / Medium (8–13) 🟢 / Low (<8) 🔴 → arithmetic says **⭐ High Priority (18)**

#### ⚠️ ANALYST OVERRIDE — DOWNGRADED TO 🟢 MEDIUM / MONITOR

**I am overriding the score downward, and the reasoning matters more than the number.**

Two of the override triggers fire at once:

**1. The matrix is double-counting one underlying fact.** Three signals — "3+ countries" (+3), "multiple PSPs" (+3) and "competitor using orchestration" (+2) — total +8 and are all downstream of a single reality: *this is a large multi-market airline*. Meanwhile the one signal that should dominate the account is **capped at +1**. An 18 here is not comparable to an 18 on a greenfield merchant.

**2. The commercial window is closed for roughly the next three quarters.** Vietnam Airlines signed a direct orchestration competitor **109 days before this report**, at CEO level, on stage at a state-visit forum with Vietnam's head of state present, as part of Ant International's broader Vietnam strategy (HCMC International Financial Centre, NAPAS cross-border, Vietcombank). That is not a procurement decision that gets unwound by a good cold email. The rollout is live *right now* — they are mid-implementation across eight markets.

Compounding it: **2026 guidance is revenue VND 138,899bn against a profit-after-tax target of roughly VND 22bn.** There is no discretionary budget for a second orchestration layer in a year with a near-zero profit target, and the payments team's attention is fully committed to the PACO rollout.

**Recommendation on timing.** Do not run a 12-touch sequence now. Log the account, and re-approach in **Q2 2027**, once it is observable what PACO actually shipped and what it left uncovered. The re-approach has a genuine basis — see "The real angle, honestly assessed" below — but it is a coverage-and-consolidation conversation with a finance or digital EVP, not an SDR-led orchestration pitch.

If Prateek wants to touch the account sooner, the only defensible play is a **single low-cost, high-specificity note** on the India gap (below), which is outside PACO's scope entirely and is the cleanest sourced finding on the account. Not a sequence.

### The real angle, honestly assessed

There is a genuine argument here. It is just not a near-term one, and it is not the standard pitch.

**PACO covers 8 markets. Vietnam Airlines sells in 39.** PACO's scope is Singapore, Malaysia, Thailand, Philippines, Japan, South Korea, Australia and Hong Kong. Explicitly outside it:
- **Vietnam itself** — the home market and 44.89% of traffic
- **India** — #5 traffic market at 5.27%, card-only today
- **USA** — #4 at 7.59%
- **Taiwan, mainland China, Macau, Indonesia** (DOKU only)
- **14 European points of sale**, plus Cambodia, Laos, Myanmar, Sri Lanka

**The stack is genuinely sprawling and nobody has consolidated it.** One global acquirer (Adyen), two orchestration layers (Outpayce XPP, 2C2P PACO), and at least six direct local integrations (VNPAY, NganLuong, NAPAS, MoMo/ShopeePay, KCP, DOKU), plus Alipay+ as an aggregator. **No public source explains how XPP and PACO coexist** — either PACO is displacing XPP for APAC APMs, or they are running two orchestrators side by side. That ambiguity is itself the story, and it is a legitimate question to put to them.

**Ant International concentration.** 2C2P/Antom is Ant. Alipay+ is Ant, and already carries three of VNA's wallet markets (Touch 'n Go, GCash, Rabbit LINE Pay). Alipay is Ant. A large and growing share of VNA's APAC alternative-method reach now depends on one corporate group. That is a real neutrality argument — but it is a CFO/risk conversation, not an opener.

**The economics make basis points existential.** VND 138.9tn of 2026 revenue against a ~VND 22bn profit target means a 1% movement in authorisation rate is worth many multiples of the entire year's profit. They already measure this and publicise it — Adyen's expansion produced a publicised "up to a 5% uplift in authorization rates." Note **"up to"**: that is a ceiling, not an average, and anyone pitching against it should not treat it as a settled 5%.

### Source Notes
- ✅ **Adyen relationship, scope and the 5% claim** — fetched and read [Adyen's newsroom release](https://www.adyen.com/press-and-media/vietnam-airlines-expands-partnership-with-adyen) directly (29 Apr 2025). Verbatim: *"The single integration with Adyen allows faster, more reliable transactions in credit cards and **selected local payment methods like Alipay and WeChat Pay**."* Scope is cards + two wallets — it does **not** claim Vietnam domestic, Korea, Indonesia, or the Alipay+ wallets.
- ✅ **Adyen named by VNA itself** — their Japan payment page, verbatim: *"Passengers will be redirected to the **payment gateway partner Adyen's** page."* First-party confirmation, fetched by me.
- ✅ **Outpayce XPP** — fetched VNA's own press room page and read the paragraph directly. Note the word *"transitioning"* — as of June 2024 it was in progress, not complete.
- ✅ **2C2P/PACO** — verified across three independent sources I fetched myself (The Paypers, published 2026-06-02T07:27:31Z; VIR; vietnam.vn/doanhnghiepvn). **I specifically ruled out conflation with the near-identical Sun PhuQuoc Airways / 2C2P PACO deal** — both are real and separate; the sources name Vietnam Airlines explicitly.
- ✅ **39 country storefronts** — parsed from 96 `hreflang` entries on the homepage myself.
- ✅ **Method map and all exclusion lists** — read directly from VNA's own payment pages for VN, IN, TW, JP, KR, CN, HK, plus the Asia / Australia / Europe regional pages.
- ✅ **NganLuong, VNPAY, MoMo, ShopeePay, NAPAS** — named on VNA's own Vietnamese help desk, verbatim: *"Hình thức thanh toán nội địa Việt Nam: **VNPay, Momo, Shopee Pay; Cổng Napas**"* and *"trả góp bằng thẻ quốc tế qua **cổng Ngân lượng**."*
- ✅ **PCI DSS Level 2** (Aug 2023), band = 1–6M card transactions/year.
- ✅ **FY2025 financials** — from the audited FY2025 Annual Report PDF (downloaded and text-extracted by Agent 1).
- ⚠️ **Traffic figures are estimates.** SimilarWeb says 4.5M/month; Semrush says 3.17–4.1M. Only the top 5 countries are exposed on the free tier — **ranks 6–10 are paywalled and unknown**. A March 2026 snapshot showed Germany at 4.11% and no India; the August snapshot shows India at 5.27% and no Germany. **Country mix is volatile between snapshots — do not over-read the ordering.** A real SimilarWeb pull would firm this up considerably.
- ⚠️ **Website launch date conflicts.** The FY2025 Annual Report describes "the commissioning of the new e-commerce website" with 152 functions (implying late 2025); press reports a launch on 6 Feb 2026. Both may be true (soft launch then public launch). Not resolved.
- ⚠️ **FY2025 profit figures conflict.** The audited AR says PBT VND 8,168bn / PAT VND 7,607bn. February 2026 press reported PBT VND 8.45tn / PAT VND 7.71tn (preliminary). A separate figure of VND 5.51tn is *PAT attributable to parent* — a different measure. Use the AR numbers.
- ⚠️ **Route/destination counts vary by source date** — Adyen (Apr 2025) "nearly 100 routes, 52 destinations, 18 countries"; FY2025 AR (Dec 2025) 113 routes, 60 destinations, 21 countries; 2C2P release (May 2026) "118 routes, 61 destinations, 22 countries." Consistent growth, not a contradiction. Use the AR.
- ⚠️ **Direct-channel share is unknown.** The only figure found is 23.8% in H1 2021 with a 50%-by-2025 target, from VNA's own internal staff publication in 2021. **No current disclosure exists.** Do not state their direct-channel share as fact.
- ⚠️ **Sofort still listed** on the Europe page although Klarna has been retiring the SOFORT brand. Flagged as worth checking — I did not verify Klarna's current deprecation timeline in this run, so do not assert it.
- ❌ **Section 8 (Checkout Experience Audit) is partial.** `booking.vietnamairlines.com` sits behind a **Cloudflare managed challenge** (`cf-mitigated: challenge`) and the live checkout could not be reached. Everything in the method map comes from their published payment documentation, not from walking a real basket. The restrictive `permissions-policy: payment=()` on that response is **Cloudflare's own interstitial header and is not attributable to the booking application** — I checked.
- ❌ **Tokenization approach: not found.** No source on network tokens, card-on-file vaulting or 3DS configuration. Their page says only that payments go "via secure payment gate" and that VNA stores no card data.
- ❌ **OnePay is NOT a Vietnam Airlines PSP.** Every source linking the two is a third-party ticket reseller (notably `vietnamairways.fr` — note the name is "Vietnam Airways", a different entity). Publisher check fails. **Do not put OnePay in outreach.**

### False positives killed in this run
Recording these so they do not creep back in:
- **"PayNow"** appears throughout their pages as `components.manageBooking.dashboard.payNowButtonLabel` — it is the **"Pay now" button label**, not Singapore's PayNow rail. VNA does **not** accept PayNow.
- **"POLi"** hits are the substring inside *"Privacy Policy"* / *"policies"* — not the POLi rail.
- **"momo"** appears in three distinct roles: the checkout method, a Lotusmiles *redemption* partner (`'momo': 'Redeem Miles - Non air: MOMO'`), and a `momo-popup` UI component. Only the first is a payment method.
- **An earlier read of mine was wrong and I discarded it:** I initially found the India and Taiwan storefronts rendering an *empty* "Local payment methods" section and nearly wrote that up as a finding. It was a **parsing artifact** — my extraction boundary had landed on a nav block. The pages are identical across points of sale. The real finding is narrower and stated correctly below.
- **"Discover"** appears on the payment page but is UI copy — *"Discover benefits"*, *"Discover results"*, `discoverSpecialNumbers`. **Not the Discover card scheme.** My own first keyword sweep counted five hits and I nearly let it through; Agent 3 caught it and I re-checked the raw HTML to confirm.
- **"UPI"** appears on the homepage only as the substring inside **"Indonesian R*upi*ah"**. Not the Indian rail.
- **Translation gap ≠ market configuration.** The `zh-tw`, `zh` and `ko` payment pages *omit* the Alipay and WeChat Pay sections, which looks like market exclusion. It is not — the `/cn/en/`, `/tw/en/`, `/hk/en/` and `/kr/en/` pages all carry the full set. The omission is untranslated content. Do not read it as absence.
- **The Vietnamese help-desk "master list" is abbreviated, not exhaustive** — it omits GrabPay, GCash, DOKU, KakaoPay, Afterpay, Zip and iDEAL, all of which demonstrably exist. The global payment page and the Asia/Europe/Australia pages are the reliable enumerations; the help desk is illustrative only.
- **Pre-2020 foreign-card decline complaints** (FlyerTalk, TripAdvisor) and **COVID-era refund delays** are stale and predate the current stack. **Do not cite them as current problems.**

### Success Case Alternatives
Selected against this account's actual motion — Competitive, high-ticket travel, multi-market APAC:
- **Wingo** — the closest structural match on the argument that survives here: automatic retries of failed payments across multiple providers, 1,000+ methods, 3DS. Relevant because VNA's own FAQ currently pushes retry onto the passenger manually.
- **Qatar Airways / Copa / Avianca** — airline-vertical credibility. Use as a named-logo credibility line only; **attach no numbers**, none are published.
- **NOVA** (Viva Aerobus, 75% of failed transactions recovered) — a *voice-callback recovery* result, **not** a routing result. Only usable if the conversation is about abandoned/failed bookings specifically. Do not mislabel it as routing.

---

## Section 1: Website Traffic Analysis by Country

**Architecture:** path-based locales on a single domain — `vietnamairlines.com/{cc}/{lang}/`. The bare domain 301s to `/us/en/`. There are **no separate operating ccTLD sites**; VNA-owned ccTLDs (`.co.jp`, `.com.hk`, `.my`, `.co.th`, `.ph`, `.com.kh`, `.co.id`, `.com.sg`, `.com.vn`, `.vn`) are all 301 redirectors on one nginx host.

**39 country points of sale + a global fallback**, confirmed from 96 `hreflang` entries I parsed off the homepage myself:
`at au be bh ca ch cn cz de dk es fr gb gr hk id ie in it jp ke kh kr la lk mm mo my nl no ph ru sa se sg th tw us vn` (+ `go`)

| # | Country | Share | MoM | Implied visits |
|---|---|---|---|---|
| 1 | Vietnam | 44.89% | +2.78% | ~2.02M |
| 2 | Japan | 8.06% | +6.82% | ~363K |
| 3 | Australia | 7.96% | **+18.74%** | ~358K |
| 4 | United States | 7.59% | +1.13% | ~342K |
| 5 | India | 5.27% | **+12.64%** | ~237K |
| — | Other | 26.24% | — | ~1.18M |

Engagement (SimilarWeb, Aug 2026): 5m 04s avg. visit, 6.13 pages/visit, 37.32% bounce, global rank #9,599, #3 in Travel & Tourism > Air Travel (Vietnam).

**Ranks 6–10 are paywalled and unknown.** That is a real limitation — Korea, Taiwan and Germany are all plausible top-10 markets with offices, and I cannot rank them.

**Domain gaps worth noting:** Australia is the #3 market and fastest-growing, with three offices and **no VNA-owned Australian domain** (`.au`, `.com.au`, `.net.au` all NXDOMAIN). Same for Korea (`.co.kr` resolves to an unrelated third party), Taiwan, India and the US.

## Section 2: Legal Entities & Local Presence

Sourced from VNA's own AEM branch-finder dataset (`/content/dam/vna/content-fragments/en/branches.*.json`), which distinguishes owned offices from GSAs — first-party, not scraped from a summary.

**Own offices (21 countries):** Japan (Tokyo, Osaka, Nagoya, Fukuoka) · South Korea (Seoul, Busan) · Australia (Sydney, Melbourne, Perth) · USA (San Francisco) · Singapore · Taiwan (Taipei, Kaohsiung) · Thailand (Bangkok) · China (Beijing, Shanghai, Guangzhou, Chengdu) · Hong Kong · Germany (Frankfurt) · France (Paris) · UK (London) · India (New Delhi — "Branch of Vietnam Airlines JSC in India") · Philippines (Manila) · Indonesia (Jakarta, Bali) · Malaysia (KL) · Cambodia · Laos · Myanmar · Russia (Moscow) · Canada (Vancouver)

**GSA-only (no VNA legal presence):** Spain, Poland, Italy, Denmark, Netherlands, Israel, Portugal, Finland, Czechia, Belgium, Sweden, Norway, Turkey, UAE. In these markets VNA does not control merchant-of-record or settlement.

**Regulatory gating note.** Per the APAC reference, domestic acquiring in **India, Indonesia, China, Vietnam and South Korea** is effectively gated behind local entity and/or licensing. VNA has offices in all five — but an office is not the same as a licensed acquiring relationship, and the India storefront's card-only checkout suggests the Indian branch is not being used to reach domestic rails.

**Ownership:** Ministry of Finance 39.29% + SCIC 47.13% = **86.42% state**; ANA Holdings (Japan) 5.62%; 27,203 shareholders on register.

## Section 3: Payment Providers & Payment Stack

### 3A. Confirmed PSPs and acquirers

| Provider | Role | Markets | Evidence |
|---|---|---|---|
| **Adyen** | Gateway (2017→), **global acquiring (2024→)** | Japan, Australia, US, Europe — cards + Alipay/WeChat Pay | [Adyen newsroom](https://www.adyen.com/press-and-media/vietnam-airlines-expands-partnership-with-adyen); named by VNA on its own Japan page |
| **2C2P by Antom** | **Orchestration (PACO)** | SG, MY, TH, PH, JP, KR, AU, HK — from H2 2026. In Vietnam 2C2P operates via **M-Pay Trade and Technology Services**, a licensed intermediary payment services provider | [VIR](https://vir.com.vn/vietnam-airlines-partners-with-2c2p-to-expand-digital-payment-options-154029.html) |
| **Outpayce (Amadeus)** | **Orchestration (XPP)** | "globally, by connecting to a wide range of specialist partners" | [VNA press room, 12 Jun 2024](https://www.vietnamairlines.com/us/en/vietnam-airlines/press-room/press-release/2024/0612-EN-Vietnam-Airlines-successfully-implemented-Amadeus-Altea-PSS) |
| **VNPAY** | QR + internet banking | Vietnam | VNA help desk; [Tuổi Trẻ, 2020](https://tuoitre.vn/thanh-toan-ma-dat-cho-vietnam-airlines-qua-phuong-thuc-vnpay-qr-20200227214501419.htm) |
| **NganLuong** | International-card instalments | Vietnam | VNA help desk (verbatim, Vietnamese) |
| **NAPAS** | Domestic card scheme / gateway | Vietnam | VNA help desk; `napasLimitWarning` i18n string in the booking bundle |
| **Payoo** | Cash / counter rails | Vietnam | [Payoo, 2020](https://www.payoo.vn/tin-tuc/dich-vu-thanh-toan-ve-vietnam-airlines-chap-canh-cho-nhung-chuyen-bay-xa-8221.html) |
| **KCP (NHN KCP)**, **KakaoPay** | Domestic cards, wallet | South Korea | VNA Asia payment page |
| **DOKU** | E-wallet | Indonesia | VNA Asia payment page |
| **Alipay+** | Wallet aggregator | MY (Touch 'n Go), PH (GCash), TH (Rabbit LINE Pay) | VNA Asia payment page |

**PSS:** migrated to **Amadeus Altéa** (go-live June 2024) from Sabre — while remaining a JV partner in **Sabre Vietnam JSC**. **NDC:** implemented via **ARC Direct Connect**, January 2025.

### 3B. Orchestrator classification

**Global orchestrator incumbent (×2).** See the Quick Look. Explicitly searched and **not found**: Juspay, Spreedly, Primer, Gr4vy, APEXX, Payrails, CellPoint Digital, Yuno.

**The unresolved question, stated plainly:** no public source explains how Outpayce XPP (2024) and 2C2P PACO (2026) coexist, and their scopes overlap — PACO's Japan and Australia are also Adyen's stated acquiring markets, and XPP's remit is "global." Either PACO is displacing XPP for APAC alternative methods, or VNA is running two orchestrators in parallel. **I could not resolve this and am not going to guess.** It is the single best discovery question on the account.

## Section 4: Alternative & Local Payment Methods

### Global set — from the page titled "Payment methods applicable across all points of sales"
- **Cards:** Visa, MasterCard, American Express, **UATP**, JCB · plus **UnionPay** (all POS). **No Diners Club, no Discover** — sourced-absent from the enumerated scheme list on every locale page. UATP (the corporate air-travel scheme) is a slightly unusual inclusion.
- **Explicitly rejects virtual and single-use cards**, and reserves the right to refuse service — a hard, self-declared conversion blocker, and a live problem for anyone paying from a neobank or a corporate virtual-card programme
- **Pay-later** — all POS **except China and Hong Kong**. Over VND 200m must be paid at a bank counter, ATM or convenience store. Payment windows are tight: 1–8 hours depending on route and departure proximity.
- **PayPal** — all POS **except Vietnam, India, South Korea, China**
- **Alipay** — all POS **except Vietnam, India, South Korea, Malaysia, Taiwan, Russia, Denmark, Norway**
- **WeChat Pay** — all POS **except Vietnam, India, Macau, South Korea, Malaysia, Taiwan, Russia, Denmark, Norway, Switzerland**
- **Cash & Miles** (Lotusmiles mixed tender)
- **No Apple Pay. No Google Pay. No Amazon Pay.** Zero occurrences across every VNA page fetched in this run (twelve by me, ~28 across the run), including the global enumerated page. Strong sourced absence **for web**. The **mobile app is UNCHECKED** — no first-party app method enumeration exists and the booking host was unreachable, so do not claim the app lacks them.

**These per-method × per-market exclusion lists are, in effect, a hand-maintained routing and eligibility table published on the open web.** That is the signature of per-POS configuration rather than a policy engine — and it is the most concrete evidence of the underlying architecture available without access to the checkout.

### Local methods — only three regional pages exist: Asia, Europe, Australia

| Market | Confirmed | Sourced-absent (from their own enumerated list) |
|---|---|---|
| 🇻🇳 Vietnam | MoMo (≤VND 50m), ShopeePay, VNPAY QR + Internet Banking, NAPAS ATM (≤VND 200m), ATM/counter/store cash (Vietcombank, BIDV, SCB, Techcombank, Co-op Bank), instalments >VND 3m via NganLuong | ZaloPay; PayPal/Alipay/WeChat all excluded at VN POS. **Instalments are reachable only through the Manage Booking / reservation-code flow, not the primary checkout** |
| 🇯🇵 Japan | Konbini via **Adyen** (7-Eleven, Lawson, Ministop, FamilyMart, Seicomart; <JPY 300,000; **website only**) | **PayPay**, LINE Pay, Rakuten Pay, Paidy, carrier billing, card instalments / bonus payment, bank transfer |
| 🇰🇷 South Korea | KCP domestic cards, KakaoPay | Naver Pay, Toss, domestic instalments |
| 🇸🇬 Singapore | GrabPay SG | **PayNow** |
| 🇲🇾 Malaysia | Touch 'n Go via Alipay+ | **FPX**, DuitNow |
| 🇹🇭 Thailand | Rabbit LINE Pay via Alipay+ | **PromptPay**, TrueMoney |
| 🇵🇭 Philippines | GCash via Alipay+ | Maya, InstaPay/PESONet, OTC cash |
| 🇮🇩 Indonesia | DOKU e-wallet | **QRIS**, virtual account, GoPay/OVO/DANA, Alfamart/Indomaret |
| 🇦🇺 Australia | Afterpay, Zip | PayTo, BPAY, POLi |
| 🇪🇺 Europe | Sofort (DE, FR, NL, CZ, IT, SE, AT, CH), iDEAL (NL only) | Bancontact (despite Belgium being a live POS), Klarna, Przelewy24, Giropay, Trustly, Blik |
| 🇮🇳 India | **Nothing** | **UPI, netbanking, RuPay, EMI, all wallets** — plus excluded from PayPal, Alipay and WeChat Pay |
| 🇹🇼 Taiwan | **Nothing** | JKOPay, LINE Pay TW, ATM/virtual account, convenience store, domestic instalments — **and Taiwan is the only market excluded from *both* Alipay and WeChat Pay while having no local alternative.** They run a Taiwan commerce property (`destinationshopping-tw.vnamall.vietnamairlines.com`) and extended direct selling to Taiwan in 2025, so this is a live contradiction |
| 🇨🇳 Mainland China | Alipay, WeChat Pay (China is *not* on either exclusion list), UnionPay, intl cards, Cash & Miles. Alipay requires "bank accounts opened in China" | **Pay-later excluded. PayPal excluded.** |
| 🇭🇰 Hong Kong | Alipay, WeChat Pay, UnionPay, intl cards, PayPal | **Pay-later excluded.** No FPS, no Octopus, no AlipayHK. *PACO covers HK, so FPS is plausibly inbound* |
| 🇲🇴 Macau | Alipay, UnionPay, intl cards, PayPal | **WeChat Pay excluded.** No local rail |
| 🇰🇭 KH / 🇱🇦 LA / 🇲🇲 MM / 🇱🇰 LK | **Nothing** | Live POS with no local-method entry |

**Methodological note.** Every "sourced-absent" entry above is absent from an **enumerated accepted-methods list published by Vietnam Airlines**, which is strong evidence. Entries I simply could not find a page about are not listed here at all.

**The India finding is the cleanest on the account.** India is a live point of sale, the **#5 traffic market at 5.27%**, has a registered VNA branch in New Delhi — and is *simultaneously* excluded from PayPal, Alipay and WeChat Pay while having no local-methods entry. An Indian customer's entire choice is: international card, UnionPay, pay-later, or Cash & Miles. In a market where UPI is the default consumer rail and high-ticket travel commonly converts on EMI. **And India is outside PACO's eight markets**, so the 2C2P rollout will not fix it.

### The mobile-web conversion hole — published by them, three times
> *"The e-wallet option will **not be displayed** if passengers access the Vietnam Airlines website **using a mobile phone** to purchase tickets and ancillary services."*

Stated separately under Alipay, under WeChat Pay, and under the Vietnam e-wallets block. Wallets *are* available in the app (their wording is consistently "website/app" for the methods themselves), so the gap is specifically **mobile web** — in Vietnam, where MoMo/ShopeePay/VNPAY are the default consumer rails, traffic is mobile-first, and an app install is a high barrier for an annual purchase.

### Instalments are behind a back door
Vietnam is the only market with a card-instalment offering, above VND 3,000,000. But it is **not in the primary checkout** — their own copy places it inside the Manage Booking → "Reservation code payment" section: *"select Pay Now using the available payment methods, **or opt for installment payment by credit card** (applicable to transactions over VND 3,000,000)."* A passenger buying a ticket in the normal flow never sees it. On a high-ticket product in a market where instalments convert, that is a self-imposed gap.

**Instalments are sourced-absent in Japan, South Korea, Taiwan, Thailand, Indonesia and India** — none of their enumerated lists offers one. Korea is the sharpest of those: instalments are standard there for high-ticket purchases, and VNA's Korea entry is only KCP cards + KakaoPay.

Co-branded card portfolio (from their i18n bundle, relevant to any issuer/instalment conversation): Vietcombank Amex, Techcombank Visa, VIB Mastercard, Standard Chartered Visa, VPBank Visa SkyVoyage (corporate), Sacombank Visa, ACB Lotusmiles Pay.

### A second, narrower stack: the Lotusmiles member portal
The i18n bundle inlined on every page shows the `avi` member portal (buy/redeem miles, post-booking ancillaries, card registration) offers only:
`payment.international` = "International Card" · `payment.domestic` = "ATM Card" · `ssr.payment.international` = "International credit/debit card" · `ssr.payment.domestic` = "QR pay & E-banking"

No wallets at all. A two-option checkout sitting alongside the main booking engine's twenty-plus.

## Section 5: Payment Issues & Customer Complaints

**Method:** ~300 recent reviews pulled directly from the Apple RSS feed (app ID 1472323081, VN storefront, 100 reviews, Jan–Sep 2026) and Google Play (`com.vietnamairlines.android.app`, 199 reviews, Feb 2025–Sep 2026). App rating 3.65★ / 4,457 ratings.

**Frequency verdict: MODERATE — and I want to be precise about that.** ~6% of recent reviews across both platforms describe the same payment-step failure. That is **not** "high frequency" in raw volume and should not be characterised as such. What makes it notable is **consistency**: the same failure mode across 19 months, both platforms, and across a website relaunch.

| Issue | Platform | Frequency | Range |
|---|---|---|---|
| **Infinite spinner / hang at the payment step** — the dominant theme | iOS, Android, web | ~8 distinct reports | 2025-04 → 2026-09 |
| **Paid successfully, ticket never issued** (auth/capture ↔ PNR reconciliation gap) | App + web | Recurring — **VNA maintains a dedicated FAQ page for it** | 2025-11 → 2026-01 |
| **Session/state loss at payment** — no resume, restart the whole booking | iOS + Android | 3 reports | 2025-07 → 2026-09 |
| **Miles + cash mixed-tender fails; inventory released mid-payment** | App + web | 3 reports, incl. a Lotusmiles Platinum member | 2026-03 → 2026-07 |
| **3DS failure on a specific issuer/scheme combo** — Vietcombank JCB fails in-app, works on web | Android | 1, but diagnostic | 2025-12 |
| **Currency locked to the wrong market with no override** — a domestic VN flight priced only in TWD | Web + app | 1, but structural | 2026-05 |
| **Third-party-payer failure drove the sale to an OTA** — *"thanh toán lỗi… nên phải đặt qua traveloka"* | App | 1, revealing | 2026-03 |

**The sharpest single fact on the whole account.** Vietnam Airlines' own help page, asked what to do when a payment fails, answers: *"Hành khách vui lòng chọn hình thức thanh toán khác"* — **"Please select a different payment method."** There is no retry and no fallback routing; the failover is manual and pushed onto the passenger. That is precisely the problem a routing layer exists to solve, stated in their own words.

**Staleness caveats — important.** Foreign-card decline threads on FlyerTalk and TripAdvisor run back to ~2009, long before the 2017 Adyen gateway and the 2024 acquiring expansion. Refund-delay complaints are COVID-era mass-cancellation backlog. **Neither is current evidence — do not use them.** Several search hits for Vietnamese card declines were VietJet or AirAsia and were excluded. No Reddit discussion of VNA payment failures was found.

## Section 6: Corporate & Payment Strategy Developments

- **FY2025 (audited AR):** revenue **VND 123,858bn** (~US$4.7bn), PBT **VND 8,168bn**, PAT **VND 7,607bn**, VND 3,291bn to the state budget. Parent-only revenue VND 98,059bn (+16.1%), PBT VND 5,427bn (+94.7%).
- **Operations FY2025:** 156,200 flights, **25.6M passengers** (+12.8%), 340,700t cargo, **103 aircraft** (57 owned / 46 leased), 72 international routes to 38 destinations in 21 countries (**+14 routes, a record**), 41 domestic routes to 22 destinations. Order for **50× B737 MAX 8**, deliveries 2030–2032.
- **2026 guidance: revenue VND 138,899bn (+~12%) against PAT of only ~VND 22bn.** Accumulated consolidated retained losses **VND 26.69tn** at end-2025; no dividends; clearance expected 2030–2032. **This is the most commercially significant number in the report.**
- **Capital raise:** Phase 1 completed 2025 (897m shares, charter capital → ~VND 8.97tn, for debt repayment and expansion). **Phase 2 up to VND 13tn from 2026.** HoSE lifted trading restrictions on HVN from 14 July.
- **Digital programme:** Amadeus Altéa PSS (Jun 2024) → Outpayce XPP transition → NDC via ARC Direct Connect (Jan 2025) → new e-commerce website (152 functions; AR implies late 2025, press reports 6 Feb 2026 launch) built with FPT on Adobe → NIC partnership for the 2025–2030 digital strategy → 2C2P PACO (May 2026). Certified SkaiBlu "Advanced E-commerce Airline"; targeting IATA Digital Airline Ambition 2030.
- **Direct-channel push:** direct international selling extended in 2025 to **Australia, Taiwan, Laos and the USA** (previously Japan and Korea only) — meaning most overseas selling was previously indirect. B2B platforms LSMA, Lotus Biz, Lotus Booker. 2026 plan explicitly names **e-wallet platforms and banks** as online-channel partners.
- **Stated goals:** "digital airline by 2025" (2024 release) → **"5-star airline by 2030"** (2026 releases). 2026–2030 targets: ~VND 640tn cumulative revenue, VND 29tn PBT, 168M passengers.
- **Hiring:** no payment-specific roles found.

## Section 7: Payment-Specific News

| Date | Item |
|---|---|
| **2026-05-29** | **2C2P by Antom / PACO orchestration** signed at the Vietnam–Singapore Tech Connect Forum. 8 markets, H2 2026, two phases. |
| 2026-02-06 | New e-commerce website launched — FPT build on Adobe stack, AI chatbot NEO, abandoned-booking reminders, claims to *"reduce the risk of errors."* |
| 2025-05-19 | NIC partnership for the 2025–2030 digital transformation strategy. |
| **2025-04-29** | **Adyen global acquiring expansion**, publicised "up to a 5% uplift in authorization rates." |
| 2025-01 | **NDC via ARC Direct Connect** — changes form-of-payment control and settlement on the agency side. |
| **2024-06-12** | **Amadeus Altéa PSS go-live + transition to Outpayce XPP.** |

**The timing observation worth using.** The website was rebuilt with an explicit *"reduce the risk of errors"* claim, and payment-step hang complaints continue through **4 September 2026**. The front end was replaced; the payment failure mode was not. That gap is the most defensible single observation available for an opener.

## Section 8: Checkout Experience Audit

**Partially completed — and I want to be explicit about the limit.** `booking.vietnamairlines.com` is behind a **Cloudflare managed challenge** (`cf-mitigated: challenge`, HTTP 403 with a 229KB interstitial). The live checkout could not be walked. Everything in Section 4 comes from published payment documentation, not from a real basket.

What is observable:
- Checkout is **market-bound**: methods, currency, pay-later rules and e-VAT invoicing all key off the country selector, and switching after starting a booking is not offered. One Play Store review reports a domestic Vietnam flight priced only in TWD with no way to reach VND.
- **e-VAT invoices only issue for VND**, forcing a market switch *before* booking or the invoice is lost.
- **Guest checkout** is available; Lotusmiles login unlocks Cash & Miles.
- **Pay-later windows are tight** — 1 to 8 hours depending on route and departure proximity, 1 hour for flights within 24/48 hours and for Vietnam Air Service-operated flights.
- **3DS:** in use (a review reports a Vietcombank JCB 3DS failure in-app that succeeds on web), but configuration is not documented anywhere public.
- Third parties on the page: Adobe DTM/AEM, OneTrust, FPT.AI livechat, airtrfx, loyaltystatus.com. **No payment-domain leakage** — consistent with a redirect model rather than embedded fields.

## Section 9: PCI DSS Compliance

**PCI DSS Level 2**, awarded August 2023, covering both `www.vietnamairlines.com` and the mobile app. Verbatim: *"Vietnam Airlines is currently the first and only carrier of Vietnam to be granted the certification of PCI DSS Compliance Level 2, **which is for merchants that process 1–6 million credit card transactions annually**."* They had previously held certification in the under-1M band — so they crossed 1M card transactions/year before August 2023.

QSA is **Crossbow Labs**, with a live seal embedded on every payment page (credential hosted on Accredible). The certificate detail could not be read (SPA, public API returns not-found), so **the current level and expiry are unverified** — only the 2023 Level 2 award is sourced.

**Worth noting for any technical conversation:** PACO is marketed as PCI DSS **Level 1**; Vietnam Airlines itself is Level 2.

## Section 10: Strategic Insights & Outreach Angles

**Insight 1 — The gap between what they bought and what they sell in.**
> **Evidence:** Section 3B (PACO covers 8 markets: SG, MY, TH, PH, JP, KR, AU, HK) + Section 1 (39 country storefronts; Vietnam 44.89%, USA 7.59%, India 5.27% all outside PACO's scope) + Section 4 (India and Taiwan are card-only).
Roughly 31 of 39 storefronts sit outside the PACO rollout. Adyen covers cards in four regions. The remainder is direct integrations and gaps. This is the only durable argument on the account, and it gets stronger once PACO ships and the boundary is visible.

**The genuinely uncontested remainder** — markets with no local rail today *and* no scheduled fix under PACO: **India, Taiwan, Indonesia (beyond DOKU), mainland China, Macau, Cambodia, Laos, Myanmar, Sri Lanka, Vietnam domestic, the USA and Canada, and 14 European points of sale.**

**Insight 2 — Manual failover, stated by them, against an economics backdrop where it is expensive.**
> **Evidence:** Section 5 (their own FAQ: *"Please select a different payment method"*; payment-step hangs across 19 months and a relaunch) + Section 6 (2026: VND 138.9tn revenue against a ~VND 22bn PAT target).
A 1% authorisation-rate movement dwarfs the entire 2026 profit target. They already measure and publicise auth rate. But note the counter: Adyen's "up to 5%" is the incumbent story any pitch must clear, and **"up to" is a ceiling, not an average** — worth probing rather than accepting.

**Insight 3 — The India anomaly.**
> **Evidence:** Section 1 (India #5 at 5.27%, growing +12.64% MoM) + Section 2 (registered branch in New Delhi) + Section 4 (card-only; excluded from PayPal, Alipay and WeChat Pay; no local-methods entry) + Section 3B (outside PACO's 8 markets).
A top-5 and fast-growing market with a registered local branch, running a card-only checkout in the world's largest UPI market, and not scheduled for improvement by the orchestrator they just signed. If any single note is sent to this account before Q2 2027, it should be this one.

**Insight 4 — Mobile web is the degraded channel.**
> **Evidence:** Section 4 (their own published note, stated three times) + Section 5 (payment-step hang complaints concentrated in app and mobile contexts).
Wallets are suppressed on mobile web in a mobile-first market where wallets are the default rail. Specific, verifiable, and theirs — not an inference.

**Insight 5 — Ant International concentration.**
> **Evidence:** Section 3A (2C2P/Antom and Alipay+ and Alipay are all Ant) + Section 4 (three wallet markets already reached through one Alipay+ connection).
A genuine neutrality argument — but a CFO/risk conversation with a long horizon, not an opener, and one that runs straight into a state-visit-level relationship.

**The strongest entry point, if and when the account reopens:** coverage beyond PACO's eight markets, led by India, framed as complementing what they have rather than replacing it. Never "you need orchestration."

## Section 11: Similar Companies & Prospecting Pipeline

### 11C. Competitor payment stacks

| Airline | PSP / Acquirer | Orchestrator | Evidence |
|---|---|---|---|
| **Cathay Pacific** | Adyen direct acquiring (HK, AU, NZ, US, JP, IN); partnership since 2014, expanded Mar 2026 | None — Adyen-consolidated | Vendor release. **Publicly quotes "a 10% increase in authorization rates" in India.** |
| **Singapore Airlines** | Adyen incl. direct card acquiring | None — Adyen-consolidated | Vendor release (2019), reconfirmed in Adyen's 2026 client list |
| **Malaysia Airlines** | 2C2P | **Outpayce XPP** | Two vendor case studies. Quotes **"authorization rates increase by 3–4 per cent"** and "reduction of payment errors by 5–8 percent". AMOP share grew "from around 10% to nearly 30%" of sales in FY19. |
| **Cebu Pacific** | Multi-acquirer | **CellPoint Digital** | Vendor case study (Feb 2024). **Publishes no numbers** — do not attach a figure. |
| **Thai Airways** | 2C2P | None named | Trade press |
| **Sun PhuQuoc Airways** | 2C2P + M-Pay | **2C2P PACO** | Trade press, Mar 2026 — a brand-new Vietnamese carrier on orchestration from day one |
| **IndiGo** | **Juspay** | Juspay | Vendor newsroom — official payment partner, 26 currencies |
| **VietJet Air** | Galaxy Pay (own licensed company), Cybersource, MPGS, Adyen, 2C2P | In-house | Prior research in this repo |
| **Garuda Indonesia** | DOKU/Midtrans — **blog-tier only, LOW CONFIDENCE** | Unknown | **Do not use without verification** |

**The pattern is the useful part.** Vietnam Airlines' regional flag-carrier peers have split two ways: **Malaysia Airlines and Cebu Pacific added an orchestration layer**; **Singapore Airlines and Cathay Pacific consolidated onto Adyen direct acquiring instead**. Vietnam Airlines has now done *both* — Adyen acquiring *and* two orchestration layers. It is the least consolidated stack among its peer group.

Adyen's own boilerplate names **Cathay Pacific and Singapore Airlines** as customers, alongside Vietnam Airlines — meaning the three largest full-service carriers in the region share an acquirer.

**CellPoint Digital caution:** its `/industry/airline` page names **zero carriers** in text or alt-tags, and 2C2P's `/airlines/` block is logos only. Neither is evidence for any specific airline. Publisher-vs-subject trap confirmed and avoided.

### 11D. Pipeline implications
- **Sun PhuQuoc Airways** — not on the TAL. Launched Oct 2025, 8 aircraft → 25 by end-2026. Already on 2C2P PACO, so not greenfield either, but worth a row.
- **Pacific Airlines** and **VASCO** (VNA subsidiaries) and **Air Cambodia** — separate brands, payment stacks unresearched.
- **Garuda Indonesia, Philippine Airlines, Korean Air, Asiana, ANA, JAL, EVA Air, China Airlines** — no payment-stack evidence found. Genuine whitespace for future research.

## Section 12: Business Case Data

| Metric | Value | Source |
|---|---|---|
| FY2025 consolidated revenue | VND 123,858bn (~US$4.7bn) | FY2025 Annual Report |
| FY2025 PBT / PAT | VND 8,168bn / VND 7,607bn | FY2025 Annual Report |
| **2026 revenue guidance / PAT target** | **VND 138,899bn / ~VND 22bn** | Vietnamese press |
| Accumulated retained losses | VND 26.69tn (end-2025) | Vietnamese press |
| Passengers FY2025 | 25.6 million | FY2025 Annual Report |
| Card transactions/year | **1–6 million** (PCI Level 2 band, as of Aug 2023) | VietnamPlus |
| Monthly web visits | 3–4.5 million | SimilarWeb / Semrush `[ESTIMATE]` |
| Points of sale | 39 countries | hreflang, parsed first-hand |
| Markets covered by PACO | 8 | 2C2P/VIR |
| Direct-channel share of sales | **Unknown** — only a 2021 figure of 23.8% with a 50%-by-2025 target, from an internal staff publication | — |

**Named stakeholders (all publicly sourced):**
- **Le Hong Ha** — General Director (CEO). Present at the 2C2P signing.
- **Nguyen Quang Trung** — Executive Vice President. Quoted on the 2C2P/PACO deal. **Best payments entry point.**
- **Dang Anh Tuan** — Executive Vice President. Quoted on the Altéa PSS implementation and the website launch.
- **Bui Tran Cuong** — Deputy Director of Finance and Accounting. Quoted on the Adyen expansion.

### Open items
- A real **SimilarWeb pull** — ranks 6–10 are paywalled, and the March-vs-August country mix is volatile.
- **Whether PACO has actually shipped** in any of the 8 markets — recheck the Asia/Australia payment pages quarterly. Nothing visible as of 15 Sep 2026.
- **How Outpayce XPP and 2C2P PACO coexist.** The best discovery question on the account.
- Whether **Alipay+**, **KCP** and **DOKU** sit behind XPP/PACO or are direct integrations.
- Whether **Adyen remains** post-PACO — the latest Adyen datapoint is April 2025.
- **Current PCI level** — only the Aug 2023 Level 2 award is sourced.
- Whether **Sofort** is still genuinely live given Klarna's brand retirement.

</details>
