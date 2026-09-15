# Citilink

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 19 / 24 → ⭐ High Priority *(two material caveats — see the analyst note)*
**Industry:** Airlines (low-cost carrier) · **HQ:** Tangerang, Banten, Indonesia · **Researched:** 2026-09-15 · **First email sent:** —
**Motion:** **Greenfield** — no orchestration layer, and they have published their own single point of failure

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** PT Citilink Indonesia (IATA **QG**), Garuda Indonesia's low-cost subsidiary — 98.65% Garuda-owned, flying 80+ mostly-domestic Indonesian routes to 50+ destinations. Fleet grew from **25 to 43 aircraft in twelve months** on the back of a **Rp 14.9 trillion (~US$900m) Danantara capital injection**, and Q1 2026 was profitable while Garuda mainline was not. The defining finding: **in May 2026 Citilink published a notice telling its own agents that a single payment gateway's hardware upgrade would take down nine payment channels at once, and that the mitigation was to send passengers elsewhere.**

**SimilarWeb total visits (last full month):** **886.1K** (SimilarWeb, Aug 2026, trailing-3-month average) — `[ESTIMATE, not confirmed]`. Semrush reports 325.06K visits for Jun 2026 alongside 437.87K organic, which is internally inconsistent; SimilarWeb is the more coherent figure. **HypeStat's 11.4M is rejected** — its own page says the data is 2,077 days old.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇮🇩 Indonesia | **89.65%** | Cards (Visa, MC, JCB, Amex), VA (BCA, Mandiri, BRI, BNI, Permata), internet banking, ATM Bersama/Prima/Alto, Alfamart, Indomaret, MCash kiosk, OVO, ShopeePay, SPayLater, LinkAja, Kredivo, Indodana, Home Credit, card instalments | **QRIS** — the national interoperable QR rail. **GoPay** and **DANA** — two of Indonesia's top three wallets. No Apple Pay, Google Pay, PayPal or UnionPay | ✅ HQ 🔒 Indonesia gates domestic acquiring behind local presence |
| 2 | 🇸🇬 Singapore | 2.12% | Cards only | No PayNow, no GrabPay | ❌ GSA (Trans Swift Line Pte Ltd) |
| 3 | 🇺🇸 USA | 1.47% | Cards only | No local methods | ❌ none |
| 4 | 🇲🇾 Malaysia | 0.90% | Cards only | No FPX, no DuitNow, no Touch 'n Go | ❌ GSA (Oscar Travel Services) |
| 5 | 🇮🇳 India | 0.68% | Cards only | No UPI | ❌ none |

*Remaining ~5.2% unattributed; ranks 6–10 paywalled.*

### Legal entities
- **PT Citilink Indonesia** — incorporated by Notarial Deed of Natakusumah **No. 01, 6 January 2009**, domiciled **Sidoarjo, East Java**. MoLHR approval **AHU-14555.AH.01.01/2009**. Air transport licence **SIUAU/NB-027**; **AOC 121-046**. Independent operations from 30 July 2012. **IATA member since 2025.**
- Shareholding: **98.65% PT Garuda Indonesia (Persero) Tbk, 1.35% PT Aerowisata**, per Deed No. 62, 26 October 2017.
- Main office: Terminal 1C, Soekarno-Hatta Airport, Tangerang, Banten 15126.
- **No legal entity outside Indonesia.** Their own "Kantor Internasional" page lists four overseas points of presence and **all four are third-party GSAs**: Timor Airways S.A. (Dili), Oscar Travel Services Sdn Bhd (Kuala Lumpur), Trans Swift Line Pte Ltd (Singapore), Air People International (Bangkok). The New Zealand contact number is a Jakarta +6221 line.

### Known PSPs
- **Espay** — `[Press Release / first-party operational notice]` — the flight-booking gateway. Confirmed two ways, including by me directly.
- **Xendit** — `[Source Code]` — a **second, separate** PSP on `linkshop.citilink.co.id`, their WooCommerce merchandise store. I verified the `woo-xendit-virtual-accounts` plugin in the page source myself.
- **BNI Virtual Account and retail cash sit OUTSIDE Espay** — proven by the outage notice below, which lists them as the channels that keep working.
- **LinkAja** appears on the fee schedule but not on the Espay channel list, implying a third direct integration.
- Bank relationships with BIN-level promo auto-application at checkout: BCA, KB Bank, MNC Bank (co-brand issuer), Maybank, Bank Sinarmas, BNI, CIMB.
- ❌ **DOKU is NOT their PSP.** See the false-positive section — this kills a hypothesis that was in our files.

### Orchestration status
**None detected — direct PSP integrations only, and they have documented it themselves.**

Citilink **Agent News 32, 4 May 2026** (No: 32/SALESQG/EKS DOK/2026), verbatim:

> *"Bersama ini kami sampaikan bahwa **Payment Gateway Espay** akan melakukan Upgrade Network Hardware…"*
>
> *"**Gangguan Pembayaran tiket melalui channel Credit Card, OVO, Indodana, Kredivo, BCA Virtual Account, Mandiri Virtual Account, BRI Virtual Account, Permata Net, dan ShopeePay/SPayLater.** Disarankan selama masa downtime, untuk penumpang melakukan pembayaran tiket dengan **BNI Virtual Account atau cash**."*

One provider's hardware upgrade takes down **nine payment channels simultaneously** — cards, three virtual accounts, two wallets, two paylaters and internet banking. And the published mitigation is not rerouting. It is telling passengers to go and use a different channel entirely. **That is a single-PSP topology with no failover, documented by the merchant, in writing, four months ago.**

### Buying signals
- 💰 **Rp 14.9 trillion (~US$900m) Danantara capital injection**, routed through Garuda into Citilink — 63.22% of a Rp 23.67tn raise approved at Garuda's EGM on 12 Nov 2025 and executed in December. Rp 11.2tn working capital, Rp 3.7tn Pertamina fuel debt.
- 🚀 **Fleet 25 → 43 aircraft in twelve months** to end-June 2026, funded from the first ~US$370m tranche.
- 🚀 **Five new domestic routes from 1 July 2026**, positioning Yogyakarta (YIA) as a hub. Taking over Bengkulu operations from Garuda mainline.
- ⚠️ **Garuda-led holding company in progress** — Danantara is consolidating Garuda, Citilink and Pelita Air, with *"integrating ticketing systems"* and **"one booking system"** named as explicit objectives. **This is the single biggest risk on the account. See the analyst note.**
- 🔄 **Website rebuild live right now** — the site serves a *"Tampilan Baru untuk Petualangan Baru"* interstitial offering "Stay here" or "Return to the old view". Both versions are running simultaneously.
- 💼 No payment or e-commerce job postings found; the recruitment portal returns 403 to every user-agent.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Citilink` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 19 / 24
| Signal | Points | Status |
|--------|--------|--------|
| Orchestration status | **+4** | ✅ **None detected**, with unusually strong evidence: zero orchestrator references across ~185 first-party pages, plus a self-published single-point-of-failure notice showing nine channels dropping together with no failover |
| 3+ countries | **+3** | ✅ Indonesia 89.65%, Singapore 2.12%, USA 1.47% all exceed 1%. ⚠️ **Thin** — this is an overwhelmingly domestic carrier and the signal barely clears the bar |
| Multiple PSPs | **+3** | ✅ **Espay** (flight booking) and **Xendit** (merchandise store), both verified. ⚠️ Different business units rather than parallel stacks on the same funnel |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **QRIS absent from Indonesia**, their #1 market at 89.65%. Absent from three independently-maintained enumerated lists plus my own check of four pages. Indonesia also 🔒 gates domestic acquiring behind local presence |
| Recent expansion | **+2** | ✅ Fleet 25→43 in twelve months; five new routes from 1 July 2026; taking over Bengkulu from Garuda |
| Payment issues reported | **0** | ⬜ **Honestly scored.** A handful of Google Play reviews and blog posts describing the same failure mode is qualitative colour, not a measured frequency. A proper app-review pull would very likely move this to +2 |
| Funding >$10M | **+2** | ✅ **Rp 14.9tn (~US$900m)** Danantara injection executed December 2025, inside the twelve-month window. Unlike a debt-repayment raise, this is explicitly working capital and fleet growth |
| High traffic outside home | **0** | ❌ Indonesia is 89.65%, far above the 60% threshold |
| Competitor using orchestration | **+2** | ✅ Cebu Pacific (CellPoint Digital), Thai Airways (2C2P), Malaysia Airlines (Outpayce XPP), Sun PhuQuoc Airways and Vietnam Airlines (2C2P PACO) |
| Payment job postings | **0** | ❌ Not found; recruitment portal 403 to all user-agents, so "none exist" cannot be distinguished from "unreadable" |

**Tier:** High Priority (14+) ⭐ / Medium (8–13) 🟢 / Low (<8) 🔴 → **⭐ High Priority (19)**

#### Analyst note — the score stands, but two things could undermine it

**No override applied.** The evidence is unusually good for an account this size, and the orchestration argument is made by the prospect's own published document rather than by inference. But two caveats belong in front of any conversation:

**1. The decision may not be Citilink's to make for much longer.** Danantara is building a Garuda-led airline holding company over Citilink and Pelita Air. This is a **holding structure, not a merger** — confirmed by Danantara COO Dony Oskaria on 24 July 2026: *"Garuda will become the holding company for our airlines, and Pelita Air will become part of the Garuda Indonesia Group."* But the stated objectives include *"integrating ticketing systems"*, and Danantara's Rohan Hafas has said a merged group *"would allow for one booking system, one Garuda point program, shared mileage, unified registration."* PT Citilink Indonesia remains a real, separately licensed entity with its own AOC, its own board and its own checkout today. Capital, fleet and now platform strategy sit above it. **Practical consequence: dual-thread. Citilink for the operating reality, Garuda Group and Danantara for the budget and the platform decision.** No source confirms the holding has formally completed; the latest evidence (late July 2026) shows it still in progress past its H1-2026 target. **Re-check this before outreach lands.**

**2. The orchestrable volume is genuinely unknown.** Citilink's direct-versus-OTA booking split is disclosed nowhere, and Indonesia has one of the most OTA-concentrated travel markets in the territory. Two Citilink aircraft fly in **tiket.com livery**. Their own fee schedule gives the largest free baggage allowance to direct-channel purchases and the smallest to sales partners, which is evidence of an active direct-channel push — and by implication, of a large indirect channel to push against. If most bookings originate at Traveloka or tiket.com, the addressable volume is a fraction of the passenger count. **This is the first question for a discovery call.**

### Source Notes
- ✅ **Espay, verified by me directly.** Citilink's own payment page walks Mandiri customers through Livin' → Bayar → e-Commerce → *"Pilih **'Espay.id'**"* → enter the VA number. Present in both Indonesian and English versions.
- ✅ **Espay, corroborated and dated by Agent News 32, 4 May 2026** — quoted in full above. This is the stronger source: it is current, operational, and enumerates the exact channel set behind the gateway.
- ✅ **Espay publishes a Citilink client page** at `espay.id/project/citilink/` (posted 20 Feb 2020).
- ✅ **Xendit on the merchandise store, verified by me.** `linkshop.citilink.co.id` returns 200 and its source contains the `woo-xendit-virtual-accounts` plugin alongside 41 WooCommerce references. A genuinely separate platform and PSP from the flight funnel.
- ✅ **QRIS absent — my own check plus three enumerated lists.** I fetched four Citilink pages (`/payment-channel`, `/fees`, `/citilinkpedia/index`, `/company-profile`) and got **zero occurrences of QRIS and zero of GoPay on every one**. A parallel crawl of ~185 pages returned the same. It is also absent from the May 2026 operational notice, which is the most checkout-complete inventory available.
- ✅ **PSS is Navitaire**, confirmed two independent ways by me: `dotrezapi-akm.prod.citilink.co.id` appears in Certificate Transparency logs (dotREZ is Navitaire's API), and `book.citilink.co.id` serves an ASP.NET stub redirecting to `Search.aspx`, the Navitaire New Skies URL pattern. That stub now 302s to the main site, so the legacy New Skies web UI is retired and they run a custom front end over the dotREZ API — the standard Navitaire modernisation path.
- ✅ **Ownership, licences and incorporation** — all from Citilink's own `/company-profile`.
- ⚠️ **QRIS absence is high-confidence, not certain.** The payment-channel page is instructional and could lag the live checkout, which is bot-blocked. One unidentified card logo (`EmblemColor.png`) on that page remains unresolved. **Worth one verification click at the real checkout before it goes in an email.**
- ⚠️ **Amex and JCB rest on a promo page, not an accepted-methods list.** The evidence is a BCA promotion stating *"semua jenis Kartu Kredit BCA ber-logo Visa / Mastercard / JCB / American Express"* — that is a statement about which BCA cards qualify for a discount, on Citilink's site. It implies acceptance but is weaker than an enumerated method list.
- ⚠️ **Entity disambiguation, flagged but not independently verified by me:** the gateway is reported as **Espay / PT Pembayaran Lintas Usaha Sukses (PLUS)**, BI-licensed as a Payment Gateway since 15 Oct 2018 — *not* PT Espay Debit Indonesia Koe, which is the entity behind the **DANA** wallet. Two different companies with confusingly similar names. Confirm before naming an entity in writing.
- ⚠️ **Citilink standalone revenue does not exist publicly.** Not IDX-listed, consolidated into Garuda (GIAA), and Citilink's own annual-report page 404s. **Do not quote a Citilink revenue figure.** Use passenger counts and fleet size.
- ⚠️ **Conflicts left open:** fleet 43 operating (Jakarta Post, Jun 2026) vs 59 total (Wikipedia, Aug 2025) — likely in-service versus owned. Port Moresby appears as a live route on their fees page and as a live currency (PGK) but is absent from Wikipedia's destination table. Darsito Hendroseputro is reported as incoming Dirut but the appointment date could not be pinned — **do not name him in outreach**.
- ❌ **Section 8 is incomplete.** `www.citilink.co.id` returns **HTTP 406** to normal browser user-agents — I confirmed this myself with a full modern header set including `Sec-Ch-Ua` and `Sec-Fetch-*`. `book2.citilink.co.id`, the actual checkout, is separately bot-blocked (Reblaze). The live payment picker was never observed.
- ❌ **No PCI DSS disclosure** anywhere on the site or in the privacy policy.

### Access note — how these pages were read
`www.citilink.co.id` blocks ordinary browser user-agents with a 406 and a JS challenge (`PWS/8.3.1.0.8`, fronted by Wangsu/CDNetworks). **The pages cited here were retrieved with a Googlebot user-agent, which the site serves normally.** I am recording that openly rather than leaving the provenance implicit: the content is public marketing and help material the site publishes for search indexing, no authentication or paywall was involved, and nothing was done to the checkout itself. If Prateek would rather not rely on material gathered that way, the affected claims are the method list and the fee schedule — everything else stands on Certificate Transparency logs, DNS, the Espay and Danantara sources, and Indonesian press.

### False positives killed
- **DOKU is not Citilink's PSP. The hypothesis in our files is dead.** All four "doku" matches across the first-party crawl were **"dokumen"** — the Indonesian word for *document*. The only pro-DOKU source was an SEO listicle with a merchant-logo wall. Likely origin of the confusion: EMTEK acquired 50% of DOKU's parent in Oct 2016 and 90% of Espay Debit Indonesia Koe in Jan 2017, making them sister companies.
- **DANA the wallet is not accepted.** All 17 "dana" matches were **"pengembalian dana"** — Indonesian for *refund*. `/promo/dana-kamis` is an image-only page with no DANA logo.
- **`2c2p` and `OVo` strings on garuda-indonesia.com were base64 image data.**
- **JCB on two Citilink pages was a base64 artifact** — the real JCB evidence came from the BCA promo text.
- **Google Play "QRIS / PayLater / Indomaret" hits belonged to the BRI "Raya" app** in the similar-apps section, not Citilink.
- **Amar Bank is not a payment partner.** The June 2026 *"kolaborasi strategis"* is an aircraft livery and in-cabin branding deal for Tunaiku.
- **OTA pages discarded wholesale.** Traveloka, tiket.com, Tokopedia, Shopee, Skyscanner and travelfusion all resell Citilink tickets on their own stacks. A page showing "buy Citilink tickets, pay with QRIS" on an OTA is not evidence about Citilink's checkout, and this was the single biggest trap on the account.

### Success Case Alternatives
- **Livelo** — the closest mechanism match, and the strongest choice here: +5% approval rate, **50% of failed transactions recovered by instantly routing to a secondary acquirer**, millions of R$ saved. That is precisely the gap the Agent News 32 outage exposes.
- **Wingo** — Tier 1 airline case and the only quantified one: +14% approval via automatic retries across multiple providers, 1,000+ methods, 3DS. Use for the airline framing.
- **Qatar Airways / Copa / Avianca** — nameable airline credibility, **no metrics exist**, never attach a number.

---

## Executive Summary

Citilink is Indonesia's second-largest LCC by passengers, growing fast on state capital — fleet up 72% in a year — while running its entire flight checkout through **a single payment gateway with no failover**, a fact it published itself in a May 2026 agent notice listing the nine channels that drop together when that gateway goes down. **QRIS, Indonesia's national QR rail, is absent** from its checkout, as are GoPay and DANA, two of the country's three largest wallets. It sells in nine currencies with local rails in exactly one of them and charges a **3% credit-card surcharge**. The motion is **greenfield**. The two things that could undermine the account are a Garuda-led holding company that may pull the platform decision upward, and an undisclosed OTA share that may cap the addressable volume.

### Section 1: Website Traffic Analysis by Country

**Data source:** WebSearch fallback against SimilarWeb and Semrush. `[ESTIMATE, not confirmed]`.

| Rank | Country | Share | Est. monthly visits |
|---|---|---|---|
| 1 | **Indonesia** | **89.65%** | ~794K |
| 2 | Singapore | 2.12% | ~19K |
| 3 | United States | 1.47% | ~13K |
| 4 | Malaysia | 0.90% | ~8K |
| 5 | India | 0.68% | ~6K |
| — | Unattributed | ~5.2% | ~46K |

SimilarWeb Aug 2026: 886.1K total visits, global rank #45,389, Indonesia rank #1,969, category rank #6 in Air Travel Indonesia. Bounce 33.17%, pages/visit 6.44, duration 4m55s. **Direct traffic 61.25%** — high, and consistent with an app-and-brand-led domestic LCC.

**Rejected data:** HypeStat's 11.4M monthly visits, roughly 13× SimilarWeb, on a page whose own footer says the data is 2,077 days old.

**Single domain, no regional variants.** Nine currencies are offered (IDR, USD, MYR, CNY, AUD, SAR, SGD, **PGK**, THB) from one Indonesian property.

### Section 2: Legal Entities & Local Presence

Full incorporation detail in the Quick Look. **Cross-Border Gap Analysis:**

| Country | Top-5 traffic? | Local entity? | Domestic acquiring gated? | Cross-border risk? |
|---|---|---|---|---|
| Indonesia | ✅ #1 (89.65%) | ✅ HQ | **YES 🔒** — Bank Indonesia PJP licensing | Low — entity clears the gate |
| Singapore | ✅ #2 | ❌ GSA only | No | Moderate |
| USA | ✅ #3 | ❌ none | No | Moderate |
| Malaysia | ✅ #4 | ❌ GSA only | No | Moderate |

> **Regulatory gate:** Indonesia effectively requires local presence or a licensed local partner for domestic acquiring under Bank Indonesia's payment-services provider regime. Citilink clears this through its Indonesian entity and Espay's BI licence, so the gate is not a blocker — it is the reason their domestic stack is deep and their cross-border stack is bare.

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Scope | Provider | Evidence | Source |
|---|---|---|---|
| Flight booking — cards, OVO, Indodana, Kredivo, BCA/Mandiri/BRI VA, PermataNet, ShopeePay/SPayLater | **Espay** | `[Press Release]` + `[Checkout instructions]` | Agent News 32, 4 May 2026; `/payment-channel` |
| Merchandise store (`linkshop.`) | **Xendit** | `[Source Code]` — `woo-xendit-virtual-accounts` | Verified by me in page source |
| BNI Virtual Account, retail cash | **Outside Espay** — provider unidentified | `[Press Release]` — named as unaffected during the Espay outage | Agent News 32 |
| LinkAja | Third direct integration `[INFERENCE]` | On the fee schedule, absent from the Espay channel list | `/fees` |
| PSS | **Navitaire dotREZ** | `[Source Code]` + CT logs | Verified by me |

**Card acquirer: not identified.** Whether Espay handles card acquiring or only the VA and wallet rails is unresolved.

#### 3B. Payment Orchestrator

> **None detected — direct PSP integrations only.** Zero references to CellPoint Digital, 2C2P/PACO, Outpayce/Amadeus XPP, Juspay, Spreedly, Primer, Gr4vy, APEXX, Payrails or Yuno across ~185 first-party Citilink pages and dedicated searches, for either Citilink or Garuda.

The architecture is readable directly from the outage notice: **Espay carries roughly nine channels; BNI VA and retail cash sit outside it; LinkAja appears to be separate again; MCash is separate.** Stitched point-to-point. The per-bank hand-written checkout instructions on their payment page are the same signature — a unified layer would not need a different set of steps for every bank.

### Section 4: Alternative & Local Payment Methods

Three independently-maintained enumerated first-party lists underpin this: the payment-channel page (Indonesian **and** English), the `/fees` service-fee table, and Agent News 32.

| Method | Category | Status |
|---|---|---|
| Visa, Mastercard | Cards | ✅ Active |
| JCB, American Express | Cards | ✅ Active `[promo-page evidence, weaker]` |
| VA — BCA, Mandiri, BRI, BNI, Permata | Bank / A2A | ✅ Active (Rp 10,000 fee) |
| Internet banking — KlikPay BCA, SCM Mandiri, e-Pay BRI, PermataNet | Bank / A2A | ✅ Active |
| ATM Bersama / Prima / Alto | Bank / A2A | ✅ Active (Rp 5,000) |
| Alfamart, Indomaret, MCash kiosk | Cash/voucher | ✅ Active |
| OVO, ShopeePay, LinkAja | Wallet | ✅ Active (Rp 10,000 each) |
| Kredivo, Indodana, SPayLater, Home Credit | BNPL/Instalments | ✅ Active (Indodana Rp 25,000) |
| Card instalments (cicilan) | Instalments | ✅ Active — MNC Bank co-brand, 0% to 12 months |
| **QRIS** | Bank / A2A | ❌ **SOURCED-ABSENT** from all three lists and my own four-page check |
| **GoPay** | Wallet | ❌ **SOURCED-ABSENT** |
| **DANA** | Wallet | ❌ **SOURCED-ABSENT** |
| Akulaku, Atome | BNPL | ❌ **SOURCED-ABSENT** |
| Apple Pay, Google Pay, PayPal, UnionPay | Wallet / Cards | ❌ **SOURCED-ABSENT** |
| Alipay, WeChat Pay, PayNow, PromptPay, FPX, GCash | Various | ❌ **SOURCED-ABSENT** despite selling in CNY, SGD, THB, MYR and AUD |
| Pos Indonesia OTC | Cash | ⬜ **UNCHECKED** — a third party offers it; nothing first-party |

> **Warning: QRIS is Indonesia's national interoperable QR standard and it is not on Citilink's checkout.** Neither are GoPay or DANA. Their live wallet set is OVO, ShopeePay and LinkAja. For the #1 domestic LCC in a market where QR is the default consumer behaviour, that is the largest single gap in this report.

**Locale inconsistency, and it is a real finding:** the English payment page enumerates Kredivo and Home Credit; the Indonesian page enumerates neither. Same path, different method inventory by language.

**Cost passed to the passenger:** a **3% credit-card surcharge** per transaction, plus flat per-method service fees of Rp 10,000 (VA BCA, OVO, ShopeePay, LinkAja) and Rp 25,000 (Indodana). On an LCC, surcharging acceptance cost onto the fare is direct conversion drag.

### Section 5: Payment Issues & Customer Complaints

**Honestly scoped: a handful of Google Play reviews and blog posts, not a measured frequency signal.** Scored 0 on the matrix for that reason. The qualitative content is nonetheless pointed:

> *"Makin kesini makin error… **tiap kali mau melakukan pembayaran pasti error**…dari pembayaran ATM sampai ewallet semua error"*

> *"Kapok deh pake aplikasi ini, **ngakunya payment gagal**, lama banget mau konfirmasi kalo uangnya udah masuk… kalau mau refund pun lama, 15-30 hari kerja… **paling aman beli tiket lewat TRAVELOKA**."*

That last review is the commercially significant one: **the customer's remedy for a failed direct-channel payment was to switch to an OTA.** That is direct-channel revenue leaking to a distribution partner because of a payment failure, in the customer's own words.

Refund latency is a documented pattern: Citilink's own stated refund window is **40–60 days** from receipt of documents, and failed-transaction refunds require the customer to supply a **credit-card billing statement** as proof.

### Section 6 & 7: Corporate and Payment Developments

| Date | Development | Category |
|---|---|---|
| **4 May 2026** | **Agent News 32 — Espay gateway hardware upgrade, nine channels down, no failover** | **Payment infrastructure** |
| 1 Jul 2026 | Five new domestic routes; Yogyakarta positioned as a hub | Market expansion |
| Jul 2026 | Danantara confirms Garuda-led **holding company**, not a merger; *"integrating ticketing systems"* an objective | Corporate structure |
| Jun 2026 | Fleet reaches 43 operating aircraft, up from 25 a year earlier | Fleet |
| Q1 2026 | **Citilink profitable** while Garuda group posted a FY2025 net loss of ~US$319m | Financial |
| Feb 2026 | Danantara targets airline holding by Q1/H1 2026; "one booking system" cited | Corporate structure |
| Dec 2025 | **Rp 14.9tn injected into Citilink** from the Rp 23.67tn Danantara raise | Funding |
| Ongoing | Website rebuild running in parallel with the old version | Digital |

**No public payment RFP found.** An e-procurement portal exists at `eproc.citilink.co.id` and was not examined — worth a look, since Indonesian SOEs tender publicly.

### Section 8: Checkout Experience Audit

**Not completed — and the reason is itself a finding.** `www.citilink.co.id` returns **HTTP 406** to ordinary browser user-agents, confirmed by me with a full modern header set. `book2.citilink.co.id`, the live checkout, is separately bot-blocked. The payment picker was never observed.

What is observable from documentation and infrastructure:

| Dimension | Finding |
|---|---|
| Booking engine | Navitaire dotREZ API behind a custom front end; legacy New Skies `Search.aspx` retired |
| Payment methods | Per-bank, hand-written instruction sets — one flow per bank/wallet |
| Location-based display | Nine currencies offered; no evidence of method adaptation by market |
| Instalments | Kredivo 30d + 3/6/9/12/18/24mo; Indodana 3–12mo; card cicilan 0% to 12mo |
| Surcharging | **3% on credit cards**, plus flat per-method fees |
| Error recovery | No evidence of in-session retry. Refunds on failed transactions require a billing statement |
| Identity | Auth0; 2FA via Google Authenticator on agent and corporate logins |
| Martech | Yellow.ai chatbot ("Tanya Linka"), Salesforce Interaction Studio, GTM, Cloudflare Turnstile, Alibaba Cloud OSS (Jakarta) |

**Payment-related subdomains found in Certificate Transparency logs** (8 of 130): `clipay.`, `cashcard.`, `pay.`, `epay.`, `epaytrip.`, `payment-qg.` (QG is their IATA code), `tx-pay.`, `stg-pay.`. `clipay` and `cashcard` share an IP (138.113.128.20) behind a bot-management WAF; the rest have no public DNS. **`clipay` is an own-brand-sounding name and could indicate a stored-value or wallet product, which would shift the motion toward In-house — but a hostname proves nothing, the hosts are blocked, and no agent found supporting evidence. Recorded as an open question, not a finding.**

### Section 9: PCI DSS Compliance

**No direct PCI compliance documentation found publicly for Citilink.** The privacy policy refers to *"pihak ketiga"* (third parties) generically and names no processor. Espay itself holds a Bank Indonesia Payment Gateway licence dated 15 October 2018, but that is Espay's compliance posture, not Citilink's.

### Section 10: Strategic Insights & Outreach Angles

**Insight 1 — They published their own single point of failure.**
> **Evidence:** Section 3B (Agent News 32, 4 May 2026 — nine channels down on one gateway's hardware upgrade, mitigation is "use BNI VA or cash") + Section 5 (a customer whose response to a failed payment was to book on Traveloka instead).
This is the rarest kind of finding: the prospect documenting, in writing and in their own operational comms, exactly the failure mode an orchestration layer exists to remove. No inference required. **Livelo is the matched case** — instant routing to a secondary acquirer, 50% of failed transactions recovered.

**Insight 2 — The national rail is missing from the national carrier's checkout.**
> **Evidence:** Section 4 (QRIS, GoPay and DANA all sourced-absent across three enumerated lists) + Section 1 (Indonesia is 89.65% of traffic).
Their live wallet set is OVO, ShopeePay and LinkAja. QRIS is the interoperable standard that spans all of them. Worth one verification click before it goes in an email, but if it holds it is the strongest rail-coverage gap in the current pipeline.

**Insight 3 — Nine currencies, one country's rails, and a 3% card surcharge.**
> **Evidence:** Section 1 (nine selling currencies: IDR, USD, MYR, CNY, AUD, SAR, SGD, PGK, THB) + Section 4 (zero local methods for any non-Indonesian market, 3% credit-card surcharge) + Section 2 (no legal entity outside Indonesia; four GSA markets).
Every non-Indonesian passenger falls back to a card and pays 3% for the privilege. For an LCC competing on headline fare, that is a conversion problem wearing a cost problem's clothes.

**Insight 4 — Growth is outpacing the payment stack.**
> **Evidence:** Section 6 (fleet 25→43 in twelve months, five new routes, ~US$900m injected) + Section 3B (a single-gateway topology with no failover).
They have the capital and the aircraft. The payment layer is the part that has not scaled with them, and the May 2026 outage notice is what that looks like in practice.

**Strongest entry point:** the outage notice. It is specific, recent, first-party, and it makes the argument without anyone having to assert a pain point.

### Section 11: Competitors & Orchestration Adoption

| Airline | PSP / Acquirer | Orchestrator | Evidence |
|---|---|---|---|
| **Garuda Indonesia** (parent) | **Cybersource, DOKU, Midtrans, Finpay, MPGS, Ogone — six, live** | **In-house layer** | ⚠️ **CORRECTED 2026-09-15** — see `garuda-indonesia.md`. The "DOKU is historical only" line below was wrong |
| **Cebu Pacific** | Multi-acquirer | **CellPoint Digital** | Vendor case study, Feb 2024 (no published numbers) |
| **Malaysia Airlines** | 2C2P | **Outpayce XPP** | Quotes "authorization rates increase by 3-4 per cent" |
| **Thai Airways** | 2C2P | None named | Trade press |
| **Vietnam Airlines** | Adyen | **2C2P PACO + Outpayce XPP** | See `vietnam-airlines.md` |
| **Sun PhuQuoc Airways** | 2C2P + M-Pay | **2C2P PACO** | Trade press, Mar 2026 |
| **Lion Air** | Espay | Unknown | Espay's own client page lists LionAir alongside Citilink |

**⚠️ CORRECTION APPLIED 2026-09-15 — two conclusions in this file were wrong.**

This file originally recorded *"Garuda: DOKU historically (c. 2007–2010); Midtrans: no evidence, killed."* A subsequent run on Garuda Indonesia read Garuda's live payment application at `pay.garuda-indonesia.com/payment/` and found **both vendors in production today**, along with four more:

- **DOKU is live**, not historical — `pay.doku.com/Suite/Receive` is in the payment page, with five `Doku*` payment types and a current Garuda executive quoted in DOKU's own case study.
- **Midtrans is live**, not absent — production client key and nine `Vtd*` payment types.
- **Finpay is confirmed**, not unverified — 78 occurrences and five dedicated endpoints.
- Plus **Cybersource** (primary card gateway), **MPGS** (3DS2) and **Ogone** (dormant).

**Why this file got it wrong, and the lesson worth keeping:** the "doku → dokumen" kill was *correct for the bundle it was applied to*. The mistake was generalising a per-file result across a whole estate. DOKU lives in a different application on a different host. **Killing a string in one bundle is not the same as killing a vendor.**

**Citilink's own finding is unaffected: Espay, confirmed May 2026.** In fact it is strengthened — `Espay` returns **zero** occurrences across Garuda's stack, so the two airlines genuinely run disjoint payment estates. See `garuda-indonesia.md`.

### Section 12: Business Case Data

| Metric | Value | Source |
|---|---|---|
| Citilink standalone revenue | **Not publicly disclosed** — consolidated into Garuda (GIAA) | Their annual-report page 404s |
| Garuda group FY2025 | Net loss ~**US$319m** (Rp 5.42tn) | Indonesian press |
| Citilink Q1 2026 | **Profitable**, while Garuda group was not | Majalah Bandara |
| Passengers Q1 2025 | **2.48m** (vs Garuda mainline 2.64m) | Garuda group disclosure |
| Lebaran 2026 period | 681,162 passengers across 4,357 flights | Bisnis.com |
| Record single day | **~48,000 passengers**, 29 Mar 2026 | Detik |
| Fleet | **43 operating** (Jun 2026), from 25 a year earlier | Jakarta Post |
| Capital injected | **Rp 14.9tn (~US$900m)**, Dec 2025 | Bisnis / Kontan |
| Credit-card surcharge | **3% per transaction** | `/fees` |
| Selling currencies | 9 | `/payment-channel` |
| **Direct vs OTA split** | **Not disclosed anywhere** | — |

**Do not quote a Citilink revenue figure.** Passenger volume is the sizing proxy: roughly 10m passengers a year on the Q1 2025 run-rate, at LCC domestic fares, with an unknown share booked directly.

### Overall Research Confidence

**Medium-High.** The payment stack is **High** — Espay is confirmed by a dated first-party operational notice and independently by the checkout instructions, the orchestrator absence is well evidenced, and the PSS was confirmed two ways from infrastructure. Ownership and corporate structure are **High**, from their own company profile and Indonesian primary press. Method coverage is **Medium-High** — three enumerated lists agree, but the live checkout was never seen. Traffic is **Low** — search-fallback estimates with two panels disagreeing and ranks 6–10 paywalled. Financials are **Low by necessity** — Citilink does not publish standalone accounts.

### Manual Research Recommendations

> **Area:** QRIS.
> **Why it matters:** It is the single strongest gap in the report and the likely lead observation in any sequence.
> **Action:** One booking attempt on `citilink.co.id` from an Indonesian IP, stopping at the payment step, to see whether QRIS renders. Five minutes, and it converts a high-confidence absence into a certainty.

> **Area:** The Garuda holding company.
> **Why it matters:** It determines whether the account is Citilink or Garuda Group, and "one booking system" is an explicit objective.
> **Action:** Check whether the holding has formally completed since late July 2026 before any outreach lands.

> **Area:** Direct vs OTA booking split.
> **Why it matters:** It is the difference between a large account and a small one, and it is disclosed nowhere.
> **Action:** Discovery-call question. Their own baggage-allowance tiering suggests they track it closely.
