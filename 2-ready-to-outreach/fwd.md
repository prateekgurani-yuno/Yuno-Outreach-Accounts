# FWD

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 20 / 29 → ⭐ High Priority
**Industry:** Insurance — life & health (pan-Asian) · **HQ:** Hong Kong SAR (incorporated Cayman Islands) · **Researched:** 2026-10-09 · **First email sent:** —
**Motion:** Greenfield

---

> ## ✅ Orchestrator audit — independently re-verified 2026-10-09. **The central claim holds.**
>
> I re-fetched `fwd.com.hk/en/support/premiums-payments/` myself (HTTP 200, 103,462 bytes) and
> confirmed the finding this account rests on.
>
> **Hong Kong has no one-off card rail.** The only occurrence of "credit card" in the entire page
> source is inside the string **`credit card autopay)`**. Card exists *only* as an autopay mandate,
> which their own page says takes **~2 months to set up**. Rail counts from the full source:
>
> | Present | Hits | Absent | Hits |
> |---|---|---|---|
> | cheque | 42 | **Octopus** | **0** |
> | FPS | 22 | **AlipayHK** | **0** |
> | PPS · autopay | 12 · 12 | **Apple Pay** | **0** |
> | EPS | 10 | **Google Pay** | **0** |
> | Hongkong Post | 8 | **WeChat Pay** | **0** |
> | JETCO | 2 | | |
>
> ⚠️ **One hit needed disambiguating and I checked it:** `wechat` returns 8 hits, but all eight are
> **"Wechat FWD HK official account"** — a social-media link, not a payment rail. **WeChat Pay is
> genuinely absent.** Recorded because an uninspected count of 8 would have looked like a wallet.
>
> ### 🚩 The method note is the most reusable thing in this file
>
> **Every FWD market site renders client-side.** Stripping `<script>` and `<style>` from that page
> leaves **61 characters** — just the page title *"FWD customer support for personal insurance
> products | FWD HK"*. **All eight payment methods live inside `__NEXT_DATA__`.**
>
> 🔑 **A naive text extraction would have reported "no payment methods found" on the single most
> important page in this report, and the whole account would have read as a greenfield with no rails
> at all.** This belongs with the repo's other silent-failure traps: `grep -P` returning 0, CloudFront
> serving Brotli, and stale scratchpad assets. **On a client-rendered site, grep the raw source, never
> the extracted text.**
>
> **What I did NOT re-verify:** the nine other market tables, the Japan postal dunning cascade, and
> the iPay88/AyoConnect attributions. Those remain as the research agent sourced them. Singapore was
> already marked `[UNVERIFIED]` by the agent — `help.fwd.com.sg` returns HTTP 403 to both tools — and
> that label stands.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** FWD Group Holdings Limited (HKEX: 1828) is a pan-Asian life and health insurer serving over 40 million customers across 10 Asian markets, listed on the Hong Kong Stock Exchange main board in July 2025. It collected **US$12,907 million of premium cash in FY2025** and books US$5,431 million a year in renewal premiums — a recurring-collection business running on eleven separate market websites and at least six separate self-service payment portals, with **no common payment layer anywhere in the group**. ([HKEX FY2025 annual results, stock code 1828](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf) · [FWD newsroom, 26 Aug 2026](https://www.fwd.com/en/newsroom/))

**SimilarWeb total visits (last full month):** 0.79 million across the 2 domains supplied (`fwd.com` 121,500 + `fwd.com.hk` 668,146, Sep 2026) — source: **SimilarWeb (supplied 2026-10-09)**.

> ⚠️ **The traffic sample covers 2 of 11 FWD domains.** FWD's own country selector lists **eleven** properties: `fwd.com` (group), `fwd.com.hk`, `fwd.com.mo`, `fwd.co.th`, `fwd.com.kh`, `fwdlife.co.jp`, `fwd.com.ph`, `fwd.co.id`, `fwd.com.sg`, `fwd.com.vn`, `fwd.com.my`, plus `fwd.cn` (a *China representative office*) and `fwdprivate.com.hk` (Bermuda/HNW). The country profile below is therefore **not the complete picture** — it is heavily weighted to the Hong Kong consumer domain. Thailand, Japan, the Philippines, Indonesia, Vietnam and Malaysia are all materially under-represented. Source for the domain list: `fwd.com` homepage `country_link_list` payload.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇭🇰 Hong Kong | 507,296 (64.24%) | FPS (QR only, ≤HK$400k), online-banking bill payment, JETCO/HSBC/Hang Seng ATM, PPS (merchant 9130), cheque, cash/cheque/EPS in branch, Hongkong Post cash, autopay (bank direct debit or credit-card autopay) — [source](https://www.fwd.com.hk/en/support/premiums-payments/) | **No one-off card payment on the web surface.** Card appears only as a recurring autopay mandate. No Octopus, AlipayHK, WeChat Pay HK, Apple/Google Pay listed. | ✅ FWD Life Insurance Company (Bermuda) Limited (Bermuda/HK/SG) + FWD Life (Hong Kong) Ltd + FWD Life Assurance Company (Hong Kong) Ltd |
| 2 | 🇨🇳 China (Mainland) | 106,369 (13.47%) | Not applicable — no FWD China policy-issuing business. `fwd.cn` is labelled **"China representative office"** by FWD itself. | n/a — see gate note | ❌🔒 **No China insurance subsidiary in the audited principal-subsidiaries list.** Representative office only. |
| 3 | 🇸🇬 Singapore | 70,664 (8.95%) | GIRO / eGIRO, bank transfer, PayNow-to-UEN, credit & debit card (Visa/Mastercard) on some products, telegraphic transfer for AUD/GBP/USD policies, cheque — **`[UNVERIFIED — search summary only, page not fetched]`**, help centre behind Cloudflare | Not established — SG help centre not reachable in this environment | ✅ FWD Singapore Pte. Ltd. (life *and general* insurance) + FWD Life (Bermuda) Singapore branch |
| 4 | 🇹🇼 Taiwan | 20,913 (2.65%) | n/a — no FWD Taiwan property or entity | n/a | ❌ No Taiwan entity, no Taiwan domain |
| 5 | 🇲🇾 Malaysia | 14,092 (1.78%) | Customer Portal: credit/debit card, **FPX (via iPay88)**, e-wallet (Touch 'n Go, Boost, ShopeePay, GrabPay — via iPay88); Boost bill payment; Maybank2u; **JomPAY** (5 biller codes across 2 entities); BSN counter interbank GIRO; monthly recurring Visa/Mastercard — [source](https://www.fwd.com.my/support/payments/) | DuitNow QR not listed on the payments page | ✅ FWD Takaful Berhad (70%) **and** FWD Insurance Berhad (14%) — two entities, two portals, two biller-code sets |

*Combined-domain shares recalculated from the supplied per-domain top-10 cuts (121,500 + 668,146 = 789,646 visits). Listed countries account for 97.2% of the combined total; the residual is outside both top-10 cuts.*

### Legal entities
Audited principal-subsidiaries list, [HKEX FY2025 annual results, note 34](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf):
- **FWD Group Holdings Limited** (Cayman Islands) — listed parent, HKEX stock code 1828
- FWD Limited (Cayman Islands) — investment holding
- FWD Group Limited (Cayman Islands) — investment holding
- FWD Group Management Holdings Limited (Hong Kong) — group management
- FWD Management Holdings Limited (Hong Kong) — investment holding
- **FWD Life Insurance Company (Bermuda) Limited** (Bermuda / Hong Kong / Singapore) — life insurance; has a Singapore branch
- FWD Life (Hong Kong) Limited (Hong Kong) — life insurance
- FWD Life Assurance Company (Hong Kong) Limited (Hong Kong) — life insurance
- FWD Life Insurance Company (Macau) Limited (Macau) — life insurance
- FWD Life Insurance Public Company Limited (Thailand, 87%) — life insurance
- FWD Life Insurance (Cambodia) Plc. (Cambodia) — life insurance
- FWD Life Insurance Company, Limited (Japan) — life insurance
- FWD Reinsurance SPC, Ltd. (Cayman Islands) — life reinsurance
- FWD Life Insurance Corporation (Philippines) — life insurance
- PT FWD Insurance Indonesia (Indonesia, 79%) — life insurance
- PT FWD Insurance Indonesia Syariah (Indonesia, incorporated 1 Dec 2025) — life insurance
- FWD Singapore Pte. Ltd. (Singapore) — **life and general insurance**
- FWD Takaful Berhad (Malaysia, 70%) — life insurance / takaful
- FWD Insurance Berhad (Malaysia, 14%) — life insurance
- FWD Vietnam Life Insurance Company Limited (Vietnam) — life insurance
- Also named on FWD's own pages: **FWD Financial Limited** — "an appointed and licensed insurance agent of FWD Life Insurance Company (Bermuda) Limited and FWD General Insurance Company Limited", operator of the HK premium-payment page ([source](https://www.fwd.com.hk/en/support/premium-payment/))
- Group supervisor: **Hong Kong Insurance Authority** (HKIA). Registration numbers: not found in public filings reviewed.
- **Non-consolidated associate:** BRI Life Indonesia, ~44% held, counted in the customer total.

### Known PSPs
- **iPay88** — Malaysia. `[Provider named on merchant's own payment page]` — "You'll be directed to the iPay88 page where you can select your preferred bank" (FPX) and "directed to the iPay88 page where you can select eWallet as your payment option" ([source](https://www.fwd.com.my/support/payments/)). Covers Malaysia FPX + e-wallet one-off payments through myPortal.
- **AyoConnect** — Indonesia. `[Provider named on merchant's own payment page + in the portal's own JavaScript bundle]` — "You will be re-directed to AyoConnect, which is the third party vendor appointed by FWD Insurance to debit your policy premium" ([source](https://www.fwd.co.id/en/support/premium-payment/)); the FWD Pay Portal bundle itself says *"Selanjutnya proses akan dialihkan ke halaman rekanan FWD Insurance, AyoConnect, yang dikelola langsung oleh AyoConnect"* ([bundle](https://www.fwd.co.id/FWDPayPortal/assets/index-Bg68bk3R.js)). Covers Indonesia card/GPN autodebit mandates.
- **Everything else: not established.** No acquirer or gateway could be identified for Hong Kong, Macau, Thailand, Japan, the Philippines, Singapore, Vietnam or Cambodia. In every one of those markets the card step sits behind an authenticated policy-servicing login (`eservices.fwd.com.hk` returns 403; `payment.fwd.com.ph` proxies everything through its own `/polapi/` endpoints) or inside the FWD Omne mobile app. **"No hits found" here is a weak negative, not proof of absence.**
- Ruled out as false positives after context checks: `omise` (matched the product name *LifePromise* / `life-promise` on the HK and Macau sites), `payu`/`Payu` (matched *payudara*, Indonesian/Malay for "breast", in breast-cancer blog URLs), `stripe`/`Stripe` (matched Chakra UI's `hasStripe` and `striped` table variants in the Indonesia portal bundle), `doku` (matched *dokumen*), `bri` (mostly matched Chakra's `brightness`/`blur` — but one genuine hit, `p.bankCode==="BRI"`, is real Indonesian bank-code logic).

### Orchestration status
**None detected — direct PSP integrations only.** Greenfield.

Positive evidence for fragmentation rather than merely absence of evidence: two *different* named vendors in two adjacent markets (iPay88 in Malaysia, AyoConnect in Indonesia); **at least six separate customer payment surfaces** (`fwd.co.id/FWDPayPortal`, `payment.fwd.com.ph`, `fwd.com.my/myPortal` *and* a separate Malaysian "Customer Portal", `eservices.fwd.com.hk`, `fwd.com.sg/iSmartWeb` + Auth0 SSO at `cusso.fwd.com.sg`, and the FWD Omne app); **three different web stacks** (Contentstack + Next.js for 9 markets, a bare single-page Next.js static export for Cambodia, WordPress for Singapore); and **per-market, per-entity biller codes maintained by hand** — PPS 9130 in Hong Kong, JETCO 105 in Macau, seven Thai bank "Com Codes", five Malaysian JomPAY biller codes across two legal entities. A group running an orchestration layer would not look like this. Searches for Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails and Yuno against FWD returned nothing.

### Buying signals
- 🚀 **HNW distribution build-out, not a new market.** FWD Private HNW hub completed across Hong Kong, Singapore and Bermuda in 2025, with products "primarily distributed via international brokers across Hong Kong, Singapore, **Dubai and Switzerland**" — new *collection* geographies without new insurance entities ([HKEX FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf)).
- 💼 **Senior HNW hire, 18 May 2026** — Mark Bensman appointed Chief Officer, FWD High Net Worth, effective 25 May 2026, from Manulife where he was Chief Distribution Officer ([FWD newsroom](https://www.fwd.com/en/newsroom/press-releases/FWD-Group-makes-key-hire-for-its-high-net-worth-business-Mark-Bensman-to-join-as-Chief-Officer-FWD-High-Net-Worth)).
- 🤝 **New collection rails being signed, market by market.** FWD Cambodia partnered with True Money (Cambodia) Plc in 2025 so customers can pay premiums via the TrueMoney Wallet app or at TrueMoney agent locations; FWD Omne was embedded inside **SCB Easy** (15m+ SCB customers) in Dec 2025 ([HKEX FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf)).
- 📋 **A payment provider is being switched off right now.** FWD Thailand site-wide notice: *"the premium payment service via Advance mPAY Company Limited will be discontinued effective 1 July 2026"* ([source](https://www.fwd.co.th/en/support/premium-payment/cc/)). A live rail migration is an open door.
- 💰 **Record H1 2026, 26 Aug 2026** — APE US$1.35bn (+7%), NB CSM US$996m (+25%), OPAT US$298m (+20%), **"over 40 million customers across 10 markets"** ([FWD newsroom](https://www.fwd.com/en/newsroom/press-releases/FWD-Group-reports-record-profit-amid-continued-growth)). Customer count has gone 38m (Mar 2026) → ~40m (Aug 2026).

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach FWD` to draft the 12-touch sequence, or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 20 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. `[ASSUMPTION — not researched.]`** Basis: FY2025 **renewal premiums of US$5,431m** and **premium cash received of US$12,907m** are both sourced ([HKEX FY2025, note 5.5 p.106 and note 17 p.125](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf)), but **no average premium per policy and no policy count are published anywhere I could reach**, so this is an assumption, not a derivation. The renewal pool alone falls below 100,000 collections/month only if the average annual renewal premium exceeds ~US$4,526 (5,431m ÷ 1.2m). That is implausible for a book that includes micro-insurance distributed through Bank Simpanan Nasional's rural network and mass-market protection in the Philippines, Indonesia, Vietnam and Cambodia. **Billing unit counted:** premium collection events (renewal + first-year + single), not policies and not customers. Premium frequency drives everything here — an annual-mode policy bills once a year, a monthly-mode policy twelve times, and FWD does not disclose the mode mix. **Per the disclosure rule, an assumed figure cannot trigger the under-40,000 rejection, and this one does not.** "Confirm monthly transaction count" is item 1 in Manual Research Recommendations. |
| Orchestration status | **+4** | ✅ **None detected — direct PSP integrations only** (Section 3B). Two different named vendors in adjacent markets, six+ separate payment surfaces, three web stacks, hand-maintained per-entity biller codes. |
| 3+ countries | **+3** | ✅ 13 licensed insurance subsidiaries across 10 markets in the audited principal-subsidiaries list; 7 APAC countries above 1% traffic share in the supplied sample. |
| Multiple PSPs | **+3** | ✅ **iPay88** (Malaysia) and **AyoConnect** (Indonesia), each named on FWD's own payment page; AyoConnect additionally confirmed in the FWD Pay Portal's own JavaScript bundle. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **China is the #2 traffic market at 13.47% of combined visible traffic and FWD has no China insurance subsidiary** — FWD's own country selector labels `fwd.cn` a *"China representative office"*, and the audited principal-subsidiaries list contains no PRC entity. This is a licensing gate on the insurance business itself, upstream of any payment question. |
| Recent expansion | **0** | ❌ Still 10 markets. No new market entry in the last 12 months; the most recent portfolio move was the opposite — the 2024 **exit** from underwriting new business in Thailand's corporate care segment. The HNW/Dubai–Switzerland broker build-out is distribution reach, not a market entry, so it does not earn this row. |
| Payment issues | **+2** | ✅ **Moderate.** 24 of 310 recent Apple App Store reviews of FWD Omne (8 storefronts) mention payment; ~10 describe outright payment failure, card-on-file update failure or amount mismatch, across Philippines, Thailand and Japan, Jan 2024 – Aug 2026 (Section 5). |
| Funding >$10M | **0** | ❌ The HKEX IPO raised ~HK$3.5bn (~US$445m) — but it priced on **7 July 2025**, more than 12 months before this report date. The rule requires a round in the last 12 months. Deliberate zero. |
| High traffic outside home | **0** | ⬜ **Uncertain.** On the supplied sample Hong Kong is **64.24%** of combined visible traffic, above the 60% threshold → not met. But the sample is 2 of 11 domains and one of those two is the Hong Kong consumer site; with `fwd.co.th`, `fwdlife.co.jp`, `fwd.com.ph`, `fwd.co.id`, `fwd.com.vn`, `fwd.com.my`, `fwd.com.sg`, `fwd.com.mo` and `fwd.com.kh` included, Hong Kong would almost certainly fall below 60%. Scoring it 0 rather than guessing. |
| Competitor using orchestration | **0** | ⬜ **Deliberate zero.** No insurer **in FWD's own ten markets** is confirmed on an orchestrator. The Juspay-flagged insurers on `apac-tal.csv` (ACKO, Digit, Galaxy Health, ICICI Lombard, ICICI Prudential Life, IFFCO Tokio, Kotak General, Niva Bupa, Onsurity, Star Health, Tata AIA Life, Zuno) are **all Indian**, and India is not an FWD market. MSIG Thailand and Singlife Singapore are on **2C2P**, which is a gateway, not an orchestrator. Awarding this on Indian evidence would be inflating the row. |
| Payment job postings | **0** | ❌ 9 live roles mention "payment" in FWD's Workday careers site; **none is a payment-infrastructure role** and a search for "payment gateway" returns 0. The closest, *Senior Manager, Backend Technology Delivery* (HK Group Office, posted 2025-09-02), is claims-platform modernisation — "end-to-end assessments of the system lifecycle—from notification to payment" refers to claims payout, not premium collection. |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **⭐ High Priority (20/29)**

No public payment RFP found, so no RFP override.

**Analyst override: NOT applied — tier stands at ⭐. But one caveat must travel with this score.**

The 20/29 is earned on real, sourced signals. It is **not** a claim that FWD's US$12.9bn of annual premium cash is orchestration-addressable, and nobody should walk into a call implying it is. In FY2025 **74% of group APE came through bancassurance (37%) and brokerage/IFA (37%)**, with agency at 19% and "others" — which *includes but is not limited to* D2C digital commerce, affinity, employee benefits, direct marketing and telemarketing — at just **8%** ([HKEX FY2025 p.40](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf)). Where a national champion bank owns the relationship (SCB in Thailand, VCB in Vietnam, BRI in Indonesia, Security Bank in the Philippines, HSBC Amanah and Alliance Bank in Malaysia), the bank frequently owns the debit mandate too. The genuinely addressable surface is the **renewal-collection and self-service layer**: the six market payment portals, the FWD Omne in-app payment flows, card-autopay mandate registration and re-registration, and the wallet/convenience rails. That is a material, growing, demonstrably broken surface — but it is a slice, not the whole book. The three strongest insights in Section 10 all sit inside that slice deliberately.

Two further notes carried rather than scored:
- **China cannot be solved by orchestration.** The constraint is FWD's missing PRC insurance licence, not the payment rail. Yuno can help with Mainland-resident *renewal* collection against FWD's Hong Kong entity; it cannot create a China acquiring path for a business that has no China policy-issuing entity. Lead with the former, never the latter.
- **No app-store trap.** FWD bills insurance premiums, not in-app purchases. The subscription reference §4 failure mode does not apply here.

### Source Notes
- ✅ HKEX listing confirmed from the primary document itself: *"FWD Group Holdings Limited 富衛集團有限公司 (Incorporated in the Cayman Islands with limited liability) **Stock code: 1828** Annual results for the year ended 31 December 2025"* — [HKEXnews PDF, 249 pages](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf). **The TAL's blank revenue cell is now filled.**
- ✅ Ten markets confirmed, and named, from FWD's own site navigation payload and the audited subsidiary list — not from a press summary.
- ✅ Premium collection methods enumerated **per market from FWD's own payment pages**, fetched and parsed from the Contentstack/Next.js data payloads (the pages render client-side, so a plain text extraction returns only the page title — the methods are in `__NEXT_DATA__`).
- ✅ Two PSPs named by FWD itself; one of them twice, once in page copy and once in shipped JavaScript.
- ✅ Complaint evidence from the public Apple App Store review RSS feeds for FWD Omne (track id 1621673678, seller *FWD Group Management Holdings Limited*), 310 reviews across ph/th/id/vn/my/jp/sg/hk storefronts, with per-review star ratings, dates and app versions.
- ⚠️ **Singapore premium-payment methods are `[UNVERIFIED — search summary only, page not fetched]`.** `help.fwd.com.sg` returns HTTP 403 behind a Cloudflare challenge in **both** WebFetch and curl. Not retried, not routed around.
- ⚠️ **Hong Kong Insurance Authority per-insurer statistics are not accessible in this environment** (HTTP 403 in both tools). A search summary referenced FWD Life (Bermuda) at 13,462 policies in the IA's 2024 *linked* individual-life in-force table — **I have not fetched that table, it covers linked products only, and I have deliberately not used it as a derivation input.** `[UNVERIFIED — search summary only, page not fetched]`
- ⚠️ **The IPO prospectus could not be retrieved.** The Chinese-language version is at `hkexnews.hk/.../2025062600018_c.pdf`; the `_e` English variant 404s and the HKEX title-search API returns 403 behind bot protection. This is the single biggest remaining gap — a prospectus would likely disclose policy counts, premium-frequency mix and collection-channel detail.
- ⚠️ Star Health's Juspay/Hyperswitch case study returned HTTP 403 → `[UNVERIFIED — search summary only, page not fetched]`.
- ⚠️ **Customer-count discrepancy, flagged not resolved:** "approximately 34 million" (FWD Workday job boilerplate, role posted 2025-09-02) vs "more than 38 million" ([HKEX FY2025, 16 Mar 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf)) vs "approximately 40 million" (FWD newsroom, 18 May / 2 Jun / 14 Aug 2026) vs "over 40 million" ([FWD newsroom, 26 Aug 2026](https://www.fwd.com/en/newsroom/press-releases/FWD-Group-reports-record-profit-amid-continued-growth)). The progression is consistent with real growth plus stale recruitment boilerplate, but the 38m/40m overlap inside 2026 is not reconciled. Use 40m+ and cite the August release.
- ❌ **No regulatory rule, licence threshold or mandate deadline is cited anywhere in this report.** Not RBI e-mandate, not China acquiring rules, not SVF or PSA licensing. Where a regulatory point is made it is made from FWD's own disclosure of its own licensing position — the audited subsidiary list and FWD's own "China representative office" label — never from background knowledge. Any regulatory claim added to outreach needs its own primary source found at the time of writing.

### Success Case Alternatives
- **Garena** — best profile match. A Southeast Asia-wide consumer business collecting across many markets where the dominant rails are wallets and account-to-account rather than cards, which is exactly FWD's Philippines / Indonesia / Vietnam / Malaysia / Thailand footprint. The parallel is coverage breadth per market under one integration, not transaction size. *(Publicly referenceable Yuno customer; no published metrics, and none are implied here.)*
- **Qatar Airways** — secondary. Multi-market, multi-currency collection against a single home entity, which maps to FWD Hong Kong accepting eight policy currencies (HKD, AUD, CAD, EUR, GBP, RMB, SGD, USD) from Mainland and overseas policyholders. *(Publicly referenceable; no published metrics.)*
- Deliberately **not** used: Clearcover's Adyen authorisation-rate and interchange numbers. Clearcover is a US auto insurer on Adyen's own marketing page, not a Yuno customer, and borrowing its figures onto a pan-Asian life insurer would be exactly the kind of number-transplant the repo's rules forbid.

---

## Executive Summary

FWD Group Holdings Limited (HKEX: 1828) is a Hong Kong-headquartered, Cayman-incorporated pan-Asian life and health insurer operating in ten Asian markets through thirteen licensed insurance subsidiaries, serving over 40 million customers and collecting **US$12,907 million of premium cash in FY2025**, of which **US$5,431 million is recurring renewal premium**. The central payment finding is that **card is a minority rail and the group has no common payment layer**: Hong Kong, its largest market by every measure, offers **eight web/branch premium-payment methods and not one of them is a one-off card payment** — card exists only as an autopay mandate — while Malaysia routes through iPay88, Indonesia through AyoConnect, and Japan's entire recovery path for a failed debit or expired card is a **paper payment slip posted to the policyholder** and settled at a convenience store, a post office, or one of seven barcode-scanning wallet apps. The orchestration opportunity is therefore not "you need orchestration for your premium book" — most of that book is collected by bank partners and agents — but the much narrower and much more defensible **renewal-recovery and self-service collection layer**, where FWD's own documentation and its own customers describe a failure-and-dunning cycle measured in months. Motion: **greenfield** — no orchestrator, no sign of one, and positive evidence of per-market fragmentation.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** **Pasted SimilarWeb data supplied by Prateek** — `accounts/traffic/fwd.md`, cited throughout as **SimilarWeb (supplied 2026-10-09)**. Period Sep 2026, SimilarWeb PRO, Worldwide, All traffic. Not re-researched; not independently verified. Agent 1's traffic budget was reallocated to entities and financials as instructed.

**Domains in the supplied sample: 2 of 11.** This is the most important caveat in the section.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | 🇭🇰 Hong Kong | **64.24%** — high priority | 507,296 | `fwd.com.hk` ▲8.21% MoM | SimilarWeb (supplied 2026-10-09) |
| 2 | 🇨🇳 China (Mainland) | **13.47%** — high priority | 106,369 | n/a (single-period cut) | SimilarWeb (supplied 2026-10-09) |
| 3 | 🇸🇬 Singapore | **8.95%** — high priority | 70,664 | `fwd.com` ▲32.42% MoM, fastest-growing domain in the batch | SimilarWeb (supplied 2026-10-09) |
| 4 | 🇹🇼 Taiwan | 2.65% | 20,913 | n/a | SimilarWeb (supplied 2026-10-09) |
| 5 | 🇲🇾 Malaysia | 1.78% | 14,092 | n/a | SimilarWeb (supplied 2026-10-09) |
| 6 | 🇺🇸 United States | 1.52% | 11,973 | n/a | SimilarWeb (supplied 2026-10-09) |
| 7 | 🇵🇭 Philippines | 1.15% | 9,088 | n/a | SimilarWeb (supplied 2026-10-09) |
| 8 | 🇨🇦 Canada | 1.00% | 7,933 | n/a | SimilarWeb (supplied 2026-10-09) |
| 9 | 🇦🇺 Australia | 0.81% | 6,366 | n/a | SimilarWeb (supplied 2026-10-09) |
| 10 | 🇬🇧 United Kingdom | 0.68% | 5,382 | n/a | SimilarWeb (supplied 2026-10-09) |
| 11 | 🇯🇵 Japan | 0.35% | 2,739 | n/a | SimilarWeb (supplied 2026-10-09) |
| 12 | 🇹🇭 Thailand | 0.32% | 2,491 | n/a | SimilarWeb (supplied 2026-10-09) |
| 13 | 🇻🇳 Vietnam | 0.28% | 2,199 | n/a | SimilarWeb (supplied 2026-10-09) |

Combined total: **789,646 visits**. Visits per country summed across both domains and shares recalculated from the combined total, per the method. Listed countries account for 97.2%; the residual sits outside both supplied top-10 cuts.

**Per-domain detail (verbatim from the supplied sheet):**
- `fwd.com` — 121,500 visits, **▲32.42% MoM**, desktop 38.46% / mobile web 61.54%. Top: Singapore 55.30%, Hong Kong 15.32%, Philippines 7.48%, US 3.53%, Canada 2.46%, Thailand 2.05%, UK 1.90%, Malaysia 1.81%, Vietnam 1.81%, Australia 1.72%. APAC visible 85.49%.
- `fwd.com.hk` — 668,146 visits, **▲8.21% MoM**, desktop 22.83% / mobile web **77.17%**. Top: Hong Kong 73.14%, **China 15.92%**, Taiwan 3.13%, Malaysia 1.78%, US 1.15%, Canada 0.74%, Australia 0.64%, Singapore 0.52%, UK 0.46%, Japan 0.41%. APAC visible 95.54%.

**Reading the two headline traffic facts the stub flagged — what the research actually supports:**

**(a) `fwd.com` at ▲32.42% MoM with Singapore at 55.30%.** `fwd.com` is the **group corporate site**, not a consumer policy site. It has no premium-payment page of its own (`/en/privacy-policy/` and most functional paths 404; the market payment pages all live on the market domains). FWD's Singapore office is at Suntec Tower 4 and carries a visible share of group roles in FWD's Workday listings; the group's HNW hub, FWD Private, spans Hong Kong, Singapore and Bermuda. `[INFERENCE, not confirmed]` The Singapore concentration on a corporate domain most likely reflects employee, investor, broker and careers traffic rather than consumer purchase or payment intent — **so the ▲32.42% growth figure should not be pitched as consumer demand growth.** It is the fastest-growing domain in the batch, which is interesting, but it is growth on a corporate site. Do not build an email on it.

**(b) `fwd.com.hk` with China at 15.92%.** This one is real and structural, and the research sharpens it considerably. FWD's FY2025 disclosure states that for Hong Kong & Macau, *"More than half of FWD Hong Kong & Macau's VNB was achieved domestically"* and *"approximately 44 per cent of offshore VNB [was] from outside of Mainland China"* — which means **the majority of FWD Hong Kong's offshore new-business value comes from Mainland China** ([HKEX FY2025 p.31](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf)). This is the Mainland-visitor (MCV) pattern: policies written in Hong Kong, by FWD's Hong Kong entity, to Mainland-resident customers. **The stub's framing needs correcting in one specific way:** the issue is *not* that FWD is trying to acquire card payments inside Mainland China. It is that an entity with no PRC presence must collect **recurring premium, for years, from policyholders resident in Mainland China**, and it must do so through Hong Kong rails — FPS QR, PPS, HK online-banking bill payment, a Hong Kong cheque, or cash at a Hong Kong branch. FWD's own page confirms the shape of this: its Hong Kong Insurance Solutions Centres accept cash in **HKD, USD or Renminbi**, and its policies are denominated in eight currencies including **RMB** ([source](https://www.fwd.com.hk/en/support/premiums-payments/)). That is a structural collection problem, not a fee problem — and it is the correct version of the argument.

---
### Section 2: Legal Entities & Local Presence

**Headquarters:** Hong Kong SAR (group office at Taikoo Shing). Parent incorporated in the **Cayman Islands**. Established **2013**. Listed on the HKEX main board, **stock code 1828**, July 2025. Group supervisor: **Hong Kong Insurance Authority**. ([HKEX FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf))

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Cayman Islands | FWD Group Holdings Limited (listed parent) | Not found | [HKEX FY2025, note 34](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf) |
| Cayman Islands | FWD Limited · FWD Group Limited · FWD Reinsurance SPC, Ltd. | Not found | Same |
| Hong Kong | FWD Group Management Holdings Limited · FWD Management Holdings Limited | Not found | Same |
| Bermuda / Hong Kong / Singapore | **FWD Life Insurance Company (Bermuda) Limited** (+ Singapore branch) | Not found | Same |
| Hong Kong | FWD Life (Hong Kong) Limited | Not found | Same |
| Hong Kong | FWD Life Assurance Company (Hong Kong) Limited | Not found | Same |
| Hong Kong | FWD Financial Limited (licensed insurance agent) · FWD General Insurance Company Limited | Not found | [fwd.com.hk premium-payment page](https://www.fwd.com.hk/en/support/premium-payment/) |
| Macau | FWD Life Insurance Company (Macau) Limited | Not found | [HKEX FY2025, note 34](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf) |
| Thailand | FWD Life Insurance Public Company Limited (87%) | Not found | Same |
| Cambodia | FWD Life Insurance (Cambodia) Plc. | Not found | Same |
| Japan | FWD Life Insurance Company, Limited | Not found | Same |
| Philippines | FWD Life Insurance Corporation | Not found | Same |
| Indonesia | PT FWD Insurance Indonesia (79%) | Not found | Same |
| Indonesia | PT FWD Insurance Indonesia Syariah (inc. 1 Dec 2025) | Not found | Same |
| Singapore | FWD Singapore Pte. Ltd. (life **and general** insurance) | Not found | Same |
| Malaysia | FWD Takaful Berhad (70%) | Not found | Same |
| Malaysia | FWD Insurance Berhad (14%) | Not found | Same |
| Vietnam | FWD Vietnam Life Insurance Company Limited | Not found | Same |
| Indonesia | BRI Life (associate, ~44%, **not consolidated**) | Not found | [HKEX FY2025 p.36](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf) |
| **Mainland China** | **None — representative office only** | n/a | FWD's own country selector labels `fwd.cn` *"China representative office"*; no PRC entity in the audited list |

Registration numbers are **not found** — FWD's results announcement gives issued share capital rather than registry numbers, and corporate-registry pages were not reachable from this environment. This is a genuine gap, not an omission.

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| Hong Kong | ✅ #1 (64.24%) | ✅ three HK life entities + the Bermuda entity | No | Low for HK residents. **High for the Mainland-resident cohort paying HK-issued policies.** |
| China (Mainland) | ✅ #2 (13.47%) | ❌🔒 **representative office only** | **Verify current rules and cite a source before asserting — not asserted here.** What *is* sourced: FWD itself has no PRC policy-issuing entity. | **Highest in the book.** Multi-year renewal collection from Mainland residents against a Hong Kong entity. |
| Singapore | ✅ #3 (8.95%) | ✅ FWD Singapore Pte. Ltd. + Bermuda-entity branch | No | Low |
| Taiwan | ✅ #4 (2.65%) | ❌ **no entity, no domain** | Not assessed — no FWD Taiwan business to gate | n/a — informational traffic only `[INFERENCE, not confirmed]` |
| Malaysia | ✅ #5 (1.78%) | ✅ two entities (Takaful 70%, Insurance Berhad 14%) | No | Low |
| United States | ✅ #6 (1.52%) | ❌ | Out of territory | Diaspora/informational `[INFERENCE, not confirmed]` |
| Philippines | ✅ #7 (1.15%) | ✅ FWD Life Insurance Corporation | No | Low |
| Canada / Australia / UK | ✅ #8/#9/#10 | ❌ (Australia: none) | Out of territory (CA, UK) | Diaspora/informational `[INFERENCE, not confirmed]` |
| Japan | ✅ #11 (0.35%) | ✅ FWD Life Insurance Company, Limited | No | Low |
| Thailand | ✅ #12 (0.32%) | ✅ FWD Life Insurance PCL (87%) | No | Low |
| Vietnam | ✅ #13 (0.28%) | ✅ FWD Vietnam Life Insurance Co. Ltd | No | Low |
| Macau | not in sample (own domain not pulled) | ✅ FWD Life Insurance Company (Macau) Ltd | No | Low |
| Indonesia | not in sample | ✅ two entities + BRI Life associate | No | Low |
| Cambodia | not in sample | ✅ FWD Life Insurance (Cambodia) Plc. | No | Low |

> *"Warning: Potential cross-border operation in China (Mainland). No local entity found — FWD's own site describes `fwd.cn` as a China representative office, and the audited principal-subsidiaries list contains no PRC entity. Mainland-resident policyholders of Hong Kong-issued policies are therefore paying premium cross-border into a Hong Kong entity, for the full multi-year life of the policy, with FX exposure and no domestic collection rail available to them."*

> *"Regulatory gate: Mainland China. FWD holds no PRC insurance licence, only a representative office. This is a gate on the insurance business, upstream of the payment question — orchestration cannot create a domestic collection path for a business that has no domestic entity. **Do not pitch a China acquiring solution.** The available and honest angle is improving collection from Mainland-resident customers against the existing Hong Kong entity. Any claim about current PRC acquiring or payment-licensing rules must be sourced live before use; none is asserted here."*

Taiwan deserves one line: it is the **#4 traffic market and FWD has no Taiwan entity, no Taiwan domain and no Taiwan product**. Taiwan's 20,913 visits land entirely on `fwd.com.hk`. `[INFERENCE, not confirmed]` The most likely explanations are Taiwanese interest in Hong Kong-issued policies, Chinese-language search spillover from the `/zh/` Hong Kong site, or diaspora policyholders. Worth one discovery question; not worth an outreach claim.

> **MANUAL:** Registry numbers for each entity are unverified. Hong Kong Companies Registry, Singapore ACRA/BizFile, Malaysia SSM and the Philippine SEC would each confirm one. Lower priority than the collection questions below.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Malaysia | **iPay88** | `[Source Code]` + merchant's own payment page — "You'll be directed to the iPay88 page where you can select your preferred bank" (FPX) / "...where you can select eWallet as your payment option" | https://www.fwd.com.my/support/payments/ |
| Indonesia | **AyoConnect** | Merchant's own payment page + `[Source Code]` in the FWD Pay Portal bundle | https://www.fwd.co.id/en/support/premium-payment/ · https://www.fwd.co.id/FWDPayPortal/assets/index-Bg68bk3R.js |
| Hong Kong | **Not established** | Payment step sits behind `eservices.fwd.com.hk` (HTTP 403). The published page lists bank rails, cheque, cash and PPS only — no card checkout to inspect. | https://www.fwd.com.hk/en/support/premiums-payments/ |
| Macau | **Not established** | JETCO merchant code 105 and bank over-the-counter only; no card checkout published | https://www.fwd.com.mo/en/support-claims/premium-payment/ |
| Thailand | **Not established** | Card and QR payment both live inside the FWD Omne mobile app; no inspectable web checkout | https://www.fwd.co.th/en/support/premium-payment/ |
| Japan | **Not established** | Direct debit and card mandates handled by post, form and app; no web card checkout | https://www.fwdlife.co.jp/support/procedure/payment/ |
| Philippines | **Not established** | `payment.fwd.com.ph` is a React SPA whose every call goes to its own `/polapi/` endpoints; the gateway is fetched server-side via a `GET_EPF_PAYMENT_URL` action and redirected to. No vendor identifiable client-side. | https://payment.fwd.com.ph/ |
| Singapore | **Not established** | Help centre HTTP 403 (Cloudflare). `iSmartWeb` bundle (Angular/Ionic/Cordova, 2.8MB) scanned — contains no PSP signature; it is an advisor tool, not a consumer checkout. Customer SSO is **Auth0** (`cusso.fwd.com.sg`) — identity, not payments. | https://www.fwd.com.sg/iSmartWeb/ |
| Vietnam | **Not established** | FWD describes "our safe and secure online payment gateway" accepting ATM cards, Visa/Mastercard/JCB, MoMo and VNPAY-QR — but does not name the gateway | https://www.fwd.com.vn/en/support/premium-payment/ |
| Cambodia | **Not established** | `fwd.com.kh` is a single-page static Next.js export — its route manifest contains only `/`, `/_app` and `/_error`. **There is no web payment surface in Cambodia at all.** | https://www.fwd.com.kh/_next/static/wfkH8t8gmtnq7fFBK2Ek72/_buildManifest.js |

**Infrastructure note (uniform, and therefore interesting).** All eleven domains sit behind **AWS CloudFront** with `server: volt-adc` (F5/Volterra Distributed Cloud ADC) — a single group-standardised edge, consistent with FWD's claim that "99 per cent of utilised applications were migrated to cloud as at 31 December 2025" under its OneMod architecture. **The edge is unified; the payment layer is not.** That contrast is the whole pitch in one sentence.

**CSP analysis.** `connect-src`, `script-src` and `form-action` are absent from all eleven marketing domains (they carry only `frame-ancestors` or `object-src`), so headers yielded no vendor discovery there. **One exception, and it is a significant one.** The Indonesia FWD Pay Portal returns:

```
content-security-policy: script-src 'self'; style-src 'self' 'unsafe-inline'; font-src 'self' data:;
  connect-src 'self'; frame-ancestors 'none'; form-action 'self'; base-uri 'self'; object-src 'none'
```

`form-action 'self'` and `connect-src 'self'` together mean **card data entered in the Indonesia portal posts to FWD's own domain**, with no third-party iframe and no cross-origin XHR. The acquirer relationship is terminated server-side and handed to AyoConnect behind FWD's own perimeter. See Section 9 — this has direct PCI-scope consequences.

#### 3B. Payment Orchestrator

**Classification: None detected — direct PSP integrations only. Greenfield.**

Evidence type: `[Source Code]` + `[Checkout]` + absence across 2 targeted searches.

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with PSP(s) on a market-by-market basis, which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

This is a stronger finding than a simple absence, because the fragmentation is positively documented rather than merely unobserved:

1. **Two different vendors in two adjacent markets** — iPay88 in Malaysia, AyoConnect in Indonesia. An orchestrated group would not need either name to surface in market copy.
2. **At least six separate customer payment surfaces**, on five different hostnames and three different web stacks: `fwd.co.id/FWDPayPortal` (React/Chakra), `payment.fwd.com.ph` (React, nginx, own `/polapi/`), `fwd.com.my/myPortal` **plus** a second Malaysian "Customer Portal", `eservices.fwd.com.hk`, `fwd.com.sg/iSmartWeb` (Angular/Ionic) behind Auth0, and the FWD Omne app.
3. **Biller codes maintained by hand, per entity, per market** — PPS merchant 9130 (HK), JETCO merchant 105 (Macau), seven Thai bank Com Codes (KBank 50026, SCB 0216, Bangkok Bank 14230/FWDLIFE, Krungsri 47769, Krung Thai 6880, GSB FWDL, CIMB Thai FWD01, TMBThanachart 2950/0143), and **five Malaysian JomPAY biller codes split across two legal entities** (1917, 5769, 820647 for FWD Insurance Berhad; 42564, 94201 for FWD Takaful Berhad).
4. **Malaysia alone runs two portals and two biller-code sets for one country**, because Takaful and conventional sit in separate licensed entities.
5. Searches for Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails and Yuno against FWD returned no evidence of any kind. The `Payment Orchestrator` column for FWD in `accounts/apac-tal.csv` is blank, and nothing was found to populate it.

> **MANUAL:** Walk the FWD Omne app payment flow in Thailand and the Philippines with a proxy, and the HK eServices "Policy Payment → Pay with FPS" step with DevTools. Those are the two places where a named acquirer will appear, and both need an authenticated policy to reach.

---

### Section 4: Alternative & Local Payment Methods

**This section is the core of the report.** Every row was read off FWD's own per-market premium-payment page. Where a dominant local rail is absent, the source cited is **FWD's own page** — i.e. a source for the *absence*. It is **not** a source for the rail's market prominence, and the APAC reference file is explicitly a checklist rather than a citation. **Any outreach line claiming a rail is dominant in a market needs its own live source found at the time of writing.**

#### Hong Kong — 8 methods, zero one-off card
| Country/Region | Method | Category | Status | Source |
|---|---|---|---|---|
| Hong Kong | **FPS** (QR scan only, premiums ≤ HK$400,000) | Bank transfer / A2A | Active in checkout | [fwd.com.hk](https://www.fwd.com.hk/en/support/premiums-payments/) |
| Hong Kong | Online-banking **Bill Payment**, merchant "FWD LIFE INSUR CO(BERMUDA) LTD", bill types 01–05 | Bank transfer / A2A | Active | Same |
| Hong Kong | **ATM** bill payment via JETCO / HSBC / Hang Seng | Bank transfer / A2A | Active | Same |
| Hong Kong | **PPS** (merchant code 9130) by phone, internet or app | Bank transfer / A2A | Active | Same |
| Hong Kong | **Cheque** — physical only, crossed, post-dated not accepted; HSBC & BOC(HK) deposit machines | Cheque | Active | Same |
| Hong Kong | **In person** at FWD Insurance Solutions Centres — cash (HKD/USD/RMB, max US$50,000 p.a. per customer), cheque, or **EPS** | Cash / debit at POS | Active | Same |
| Hong Kong | **Hongkong Post** — HKD cash against the QR code on the premium notice, < HK$120,000 per bill | Cash/voucher | Active | Same |
| Hong Kong | **Autopay** — bank direct debit **or credit-card autopay**, set up via eServices, **~2 months to process** | Direct debit / mandate | Active | Same |
| Hong Kong | **One-off credit-card payment on the web** | Cards | **Not found** — card appears only as an autopay mandate | Same |
| Hong Kong | Octopus · AlipayHK · WeChat Pay HK · Apple Pay · Google Pay | Digital wallet | **Not found** on the premium-payment page | Same |

Two further HK details that matter commercially: **eight policy currencies** are supported — *"HKD policies can accept payments paid in HKD only. AUD, CAD, EUR, GBP, RMB, SGD and USD policies can accept payments paid in corresponding policy currency or HKD only"* — and a hard operational limit, *"A single payment transaction covering more than three policies will not be accepted."*

> *"Warning: In Hong Kong — FWD's single largest market at 64.24% of visible traffic and a 77.17% mobile-web share — there is **no one-off card payment** on the published web surface, and autopay enrolment takes approximately two months. A policyholder whose mandate fails has no instant card path to cure it; they must use a bank QR, a bill payment, an ATM, PPS, a post office or a branch."*

#### Thailand — 9 methods, including one being switched off
| Country/Region | Method | Category | Status | Source |
|---|---|---|---|---|
| Thailand | **FWD Omne app — QR Code** ("scan... using your bank's app or other payment channels that use the QR Code system") | Bank transfer / A2A | Active | [fwd.co.th](https://www.fwd.co.th/en/support/premium-payment/) |
| Thailand | **FWD Omne app — credit card: VISA, Mastercard, JCB** | Cards | Active | Same |
| Thailand | Head office / branch — cash, credit card, QR Code (QR at Bangkok HQ & Ratchada only); cash caps THB 100,000 (SCB/former agency) or THB 500,000 (FWD agents) per invoice | Cash / Cards | Active | Same |
| Thailand | **Through agents** — cheque or credit card, temporary receipt issued | Cards / Cheque | Active | Same |
| Thailand | **Bank counter / online banking** — KBank 50026, SCB 0216, Bangkok Bank 14230 (FWDLIFE), Krungsri 47769, Krung Thai 6880, GSB FWDL, CIMB Thai FWD01. SCB Easy to a/c 001-349917-5 "FWD Life" | Bank transfer / A2A | Active | Same |
| Thailand | **ATM** — TMBThanachart 2950/0143, KBank, SCB, Bangkok Bank, Krungsri, Krung Thai | Bank transfer / A2A | Active | Same |
| Thailand | **Internet banking** — ttb, KBank, Bangkok Bank, Krungsri (renewal premiums only) | Bank transfer / A2A | Active | Same |
| Thailand | **Counter services: Lotus and 7-Eleven**, cash, ≤ THB 49,000 per invoice, no fee. **Barcode payment on the FWD Card and policyholder card has been cancelled.** | Cash/voucher | Active (with one deprecation) | Same |
| Thailand | **Auto-recurring credit card** (VISA/Mastercard/JCB), apply ≥10 working days before due date, via FWD Omne or a signed authorisation form emailed to `OP_POS_Admin.th@fwd.com` | Direct debit / mandate | Active | Same |
| Thailand | **Auto-recurring savings-account debit** — applied for at an ATM or in SCB Easy / Krungsri Mobile / Krungthai NEXT / Bangkok Bank app, or by signed form | Direct debit / mandate | Active | Same |
| Thailand | **Advance mPAY** | Carrier/wallet | **BEING REMOVED — see Section 7** | [fwd.co.th](https://www.fwd.co.th/en/support/premium-payment/cc/) |
| Thailand | PromptPay (by name) · TrueMoney · Rabbit LINE Pay · instalment plans | Wallet / BNPL | **Not found** by name. The QR flow is described generically as a bank-app QR scan; PromptPay is not named, and I am not going to assert it. | [fwd.co.th](https://www.fwd.co.th/en/support/premium-payment/) |

Note the explicit anti-duplicate rule: *"To prevent duplicate premium payment, the online premium payment service is not available for policies that already applied for automatic premium payment through credit card or bank account"*, and *"The Online premium payment is not available for Unit linked policies bought through SCB."* These are product-level exclusions enforced by switching the rail off, not by routing around it.

#### Japan — the involuntary-churn case study, written by FWD itself
| Country/Region | Method | Category | Status | Source |
|---|---|---|---|---|
| Japan | **口座振替 — bank account direct debit** | Direct debit / mandate | Active (one of only two primary modes) | [fwdlife.co.jp](https://www.fwdlife.co.jp/support/procedure/payment/) |
| Japan | **クレジットカード払 — credit card** | Cards (mandate) | Active (the other primary mode) | Same |
| Japan | **払込取扱票 (paper payment slip), posted when a debit or card charge fails** — payable at **convenience stores**, **Japan Post Bank / post offices**, or by scanning its barcode in a smartphone app | Cash/voucher | Active | [fwdlife.co.jp/support/cashless-payment/](https://www.fwdlife.co.jp/support/cashless-payment/) |
| Japan | Slip-payment apps **as at 2026-04-15**: **PayPay 請求書払い** (≤¥300,000, PayPay Money balance only, requires in-app identity verification), **d払い**, **au PAY**, **楽天ペイ**, **ゆうちょPay**, **PayB**, **FamiPay** (< ¥50,000) | Digital wallet | Active | Same |
| Japan | Amounts **over ¥300,000** must be paid at Japan Post Bank or a post office | Cash | Active | Same |
| Japan | Konbini (direct, without the slip) · carrier billing · Paidy · card instalment / bonus-payment modes | Cash / Carrier / BNPL | **Not found** on these pages | Same |

**This is the single most valuable finding in the report, because FWD documents its own dunning cascade, step by step** ([source](https://www.fwdlife.co.jp/support/credit_payment/)):

- **Step 1 — postcard.** When the card declines, FWD mails a **はがき** (postcard) saying the charge failed and that it will be re-requested next month. Causes given: *"the credit card registered with us has exceeded its available limit, has passed its expiry date, or for various other reasons the card company has advised that the charge cannot be processed."*
- **Step 2 — envelope with a paper slip.** If the following month also fails, FWD mails a **封筒** containing the 払込取扱票 **and** a QR code to register a new card. The customer must do both: register a new card, *and* pay the arrears by slip.
- **Step 3 — card invalid.** If the card company reports the card is invalid, FWD mails a further envelope asking the customer to change card or switch to direct debit.
- **The consequence, in FWD's own words:** *"期限内にお払込みいただけなかった場合は、ご契約が失効または自動振替貸付制度の適用（対象契約のみ）となります"* — **if not paid by the deadline, the policy lapses (失効) or an automatic premium loan is applied.**
- **And the mechanism that produces the declines:** *"当社では、クレジットカード会社からの要請およびセキュリティ対策の強化に伴い、2022年6月よりクレジットカードの決済時に、カードの有効性確認のためオーソリゼーション（以降「オーソリ」）を行うよう、クレジットカード決済システムを変更いたしました。それに伴い、クレジットカードの有効期限が経過している場合など、オーソリの結果、クレジットカード会社からカードの利用承認がされなかった場合は保険料の決済ができません"* — **since June 2022 FWD Japan runs a validity authorisation before each charge, at the card companies' request, and an expired card fails that check.**

An expired or reissued card therefore triggers a **multi-month, postal, customer-action-dependent recovery loop that ends in lapse**. The subscription reference §1 names the fix for exactly this cause — *"Card expired or reissued → network tokens / account updater: credentials refresh without customer action"*. FWD has built an elaborate, expensive paper process around the absence of that capability. **Do not assert a recovery-rate or churn number; this is a mechanism argument and it is strong enough without one.**

#### Philippines — 7 methods, wallets live
| Country/Region | Method | Category | Status | Source |
|---|---|---|---|---|
| Philippines | **GCash** — "Look for 'FWD Life Insurance Corporation' in the Pay Bills/Insurance section", up to **PHP 100,000** | Digital wallet | **Active** | [fwd.com.ph](https://www.fwd.com.ph/support/premium-payment/) |
| Philippines | **PayMaya (Maya)** — same Pay Bills/Insurance route | Digital wallet | **Active** | Same |
| Philippines | **FWD Payment Portal** — credit or debit card (excludes top-ups, reinstatements >90 days past due, single-pay products, and policies on a monthly plan) | Cards | Active | Same · https://payment.fwd.com.ph/ |
| Philippines | **FWD Omne app** — *"monthly payment option is only available on Omne via ACA/ADA"* | Direct debit / mandate | Active | Same |
| Philippines | **Online banking** — Security Bank BancNet, BDO, BPI, Land Bank, Metrobank, RCBC, UnionBank (prefix 01+ initial, 03+ subsequent) | Bank transfer / A2A | Active | Same |
| Philippines | **Cards accepted**: credit — Visa, Mastercard, American Express, China UnionPay, JCB; debit — Visa, Mastercard; ATM — **BancNet, Expressnet**. POS terminals at all FWD business hubs. | Cards | Active | Same |
| Philippines | **ADA / ACA mandates** via Security Bank, BPI, BDO, Metrobank | Direct debit / mandate | Active | Same |
| Philippines | **Over-the-counter** cash & cheque at Security Bank (Peso & Dollar), BDO, BPI, Metrobank, UnionBank, RCBC; **cash at all LBC branches nationwide** | Cash/voucher | Active | Same |
| Philippines | InstaPay / PESONet (by name) · Shopee/Lazada wallets | Bank transfer / Wallet | **Not found** by name | Same |

The Philippines is FWD's **best-covered market** and the proof that the group *can* run wallet rails when it chooses to. It is also the market with the clearest structural tell: **monthly billing requires a bank mandate (ACA/ADA)** — card-on-file is not offered as a monthly billing rail at all.

#### Malaysia — iPay88, two entities, two portals
| Country/Region | Method | Category | Status | Source |
|---|---|---|---|---|
| Malaysia | **Customer Portal** — credit/debit card, **FPX**, **e-wallet: Touch 'n Go, Boost, ShopeePay, GrabPay**; plus auto-debit via card or bank account | Cards / A2A / Wallet | Active | [fwd.com.my](https://www.fwd.com.my/support/payments/) |
| Malaysia | **myPortal one-off FPX / eWallet → routed to iPay88**, OTP + bank TAC | Bank transfer / A2A / Wallet | Active | Same |
| Malaysia | **Boost** bill payment — "look for FWD Insurance Berhad under the Insurance category"; policy prefixes IL, RP, UR | Digital wallet | Active | Same |
| Malaysia | **Maybank2u** — Maybank account holders, policy prefixes IL, GL, RP | Bank transfer / A2A | Active | Same |
| Malaysia | **JomPAY** — biller 1917 (IL/GL), 5769 (RP), 820647 (2XX) for FWD Insurance Berhad; 42564 "FWD Takaful Berhad-2", 94201 "FWD Takaful Berhad-1". **Not available for the first payment on a new certificate.** | Bank transfer / A2A | Active | Same |
| Malaysia | **Monthly recurring card** — Visa or Mastercard added once via myPortal. *"For debit cards: contact your bank for an auto-debit facility activation... please ensure it's activated with your bank for e-commerce transactions. If your card hasn't been activated, we'll be unable to collect your contribution."* | Cards (mandate) | Active | Same |
| Malaysia | **Over-the-counter at Bank Simpanan Nasional** — counter **interbank GIRO** transfer to a/c 14100-29-86450015-5 | Bank transfer / A2A | Active | Same |
| Malaysia | **Future Premium Payment** — pay in advance, traditional life only, by phone (1 300 22 6262) | Prepayment | Active | Same |
| Malaysia | **DuitNow QR** | Bank transfer / A2A | **Not found** on the payments page | Same |

Malaysia also carries a **Public Advisory: Important Payment Safety Notice** — *"Our agents are not allowed to collect payments on behalf of the company. Always make sure your payment receipt is issued directly by FWD. If you notice any unauthorised payment requests or suspicious activity, please contact our Customer Service Hotline right away."* A fraud-control signal, and a contrast worth noting: Thailand and Vietnam both *do* permit agent collection.

#### Indonesia — three methods only, and the thinnest coverage in the group
| Country/Region | Method | Category | Status | Source |
|---|---|---|---|---|
| Indonesia | **Autodebit (debit or credit card)** via **FWD Pay Portal → redirected to AyoConnect**; supports Mastercard and **GPN** domestic debit (incl. "Classic (RGLR)") with per-bank, per-card-type limits fetched at runtime; **BRI** is special-cased in the limits table | Direct debit / mandate · Cards | Active | [fwd.co.id](https://www.fwd.co.id/en/support/premium-payment/) · [portal bundle](https://www.fwd.co.id/FWDPayPortal/assets/index-Bg68bk3R.js) |
| Indonesia | **Virtual Account** — BCA VA, Permata VA; plus Mandiri and BCA bank accounts | Bank transfer / A2A | Active | [fwd.co.id](https://www.fwd.co.id/en/support/premium-payment/) |
| Indonesia | **BCA Mobile M-payment** — "Asuransi" → "FWD Insurance" | Bank transfer / A2A | Active | Same |
| Indonesia | **QRIS** | Bank transfer / A2A | **Not found** on the premium-payment page | Same |
| Indonesia | **GoPay · OVO · DANA · ShopeePay** | Digital wallet | **Not found** on the premium-payment page | Same |
| Indonesia | **Alfamart / Indomaret convenience-store cash** | Cash/voucher | **Not found** on the premium-payment page | Same |

⚠️ **Trap check, performed deliberately.** `fwd.co.id` does carry a `/id/promo-produk-online/voucher-gopay-rp1-juta/` page — **that is a GoPay voucher offered as a marketing prize, not GoPay as a premium-payment rail.** I also confirmed that `payu` matches on this site resolve to *payudara* (breast, in breast-cancer blog URLs), `doku` to *dokumen*, and `stripe` to Chakra UI's `hasStripe`/`striped` table props. Reporting any of those as vendors would have been wrong.

> *"Warning: In Indonesia, FWD's published premium-payment page lists **three** methods — card autodebit, virtual account, and BCA mobile banking — and does not list QRIS, any e-wallet, or convenience-store cash. FWD operates two licensed Indonesian entities plus a ~44% stake in BRI Life, the country's number-one bancassurer by APE. Cite a current source for QRIS and wallet share before using this in outreach; the absence is sourced from FWD's own page, the prominence is not."*

#### Vietnam — 6 methods, wallets live
| Country/Region | Method | Category | Status | Source |
|---|---|---|---|---|
| Vietnam | **"Our safe and secure online payment gateway" — ATM cards, international cards (Visa, Mastercard, JCB), MoMo, VNPAY-QR** | Cards / Wallet / A2A | Active | [fwd.com.vn](https://www.fwd.com.vn/en/support/premium-payment/) |
| Vietnam | **Bank bill payment** — VCB Digibank ("Pay bills" → "Insurance premium" → "FWD Vietnam"), Agribank E-mobile, Nam A Bank Open Banking; or in person at any VCB/Agribank/Nam A branch | Bank transfer / A2A | Active | Same |
| Vietnam | **Bank transfer** to one of four FWD accounts — VCB Tan Dinh 1212393939, Agribank Sai Gon 1900201453488, Nam A Bank HO 100036505800001, BIDV HCMC 13310000334567 | Bank transfer / A2A | Active | Same |
| Vietnam | **MoMo** — QR scan or deep link straight to the FWD payment page | Digital wallet | Active | Same |
| Vietnam | **Viettel Money** — Finance → Insurance → FWD logo; daily limit VND 100 million | Digital wallet | Active | Same |
| Vietnam | **Payoo** convenience stores | Cash/voucher | Active | Same |
| Vietnam | **FWD office / agent** — "we can only accept payment by ATM, debit or credit cards" | Cards | Active | Same |
| Vietnam | **ZaloPay** | Digital wallet | **Not found** | Same |

#### Macau — 6 methods
| Country/Region | Method | Category | Status | Source |
|---|---|---|---|---|
| Macau | **BOCNET (Personal)** online banking transfer | Bank transfer / A2A | Active | [fwd.com.mo](https://www.fwd.com.mo/en/support-claims/premium-payment/) |
| Macau | **Bank over-the-counter at BNU or LUSO** — cash in **USD/HKD/MOP/RMB**, cheque or transfer. *"Payment in RMB only accepted at LUSO Bank."* | Cash / Bank transfer | Active | Same |
| Macau | **Cheque** by mail or dropped at the Customer Service Centre | Cheque | Active | Same |
| Macau | **JETCO ATM "JET PAYMENT"** — merchant code **105**; plus online banking "FWD LIFE" under bill payments | Bank transfer / A2A | Active | Same |
| Macau | **Customer Service Centre** cash/cheque — annual cap USD 50,000 / MOP 400,000 per policyholder, USD 15,000 / MOP 120,000 per policy; signed Cash Premium Payment Declaration Form required | Cash | Active | Same |
| Macau | **Autopay** — "Direct Debit / Credit Card Authorisation Form"; **two months to process, two months' premium prepayment required** | Direct debit / mandate | Active | Same |

#### Cambodia — no web payment surface
| Country/Region | Method | Category | Status | Source |
|---|---|---|---|---|
| Cambodia | **TrueMoney Wallet app and TrueMoney agent locations nationwide** — 2025 partnership with True Money (Cambodia) Plc, *"to allow customers to pay their FWD insurance premiums through the TrueMoney Wallet app or at any of the nationwide TrueMoney agent locations, and to increase sales opportunity both through True Money agents and online via the app"* | Digital wallet / Cash agent | Mentioned in filing | [HKEX FY2025 p.34](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf) |
| Cambodia | Any FWD-hosted web payment page | — | **Does not exist.** `fwd.com.kh` is a single-page static export; its Next.js route manifest contains only `/`, `/_app`, `/_error`. | https://www.fwd.com.kh/_next/static/wfkH8t8gmtnq7fFBK2Ek72/_buildManifest.js |

#### Singapore — not verifiable in this environment
| Country/Region | Method | Category | Status | Source |
|---|---|---|---|---|
| Singapore | GIRO / eGIRO; direct bank transfer; **PayNow to a company UEN**; credit & debit card (Visa/Mastercard) on some products; telegraphic transfer for AUD/GBP/USD policies; cheque | Mixed | **`Unknown, checkout not accessible`** — `[UNVERIFIED — search summary only, page not fetched]` | help.fwd.com.sg — **HTTP 403 (Cloudflare) in both WebFetch and curl** |
| Singapore | **PayNow for claim and policy-benefit PAYOUTS** — "Important Payout Update", *"To ensure timely receipt of claim and policy benefit payouts, please ensure that your PayNow is linked to your NRIC/FIN"*, view date **27 July 2026** | Disbursement | Active — **this one IS sourced from a fetched page** | [fwd.com.sg](https://www.fwd.com.sg/travel-insurance/) |

Note carefully: **the only PayNow usage I could verify from a fetched FWD page is an outbound payout, not premium collection.** Do not conflate the two.

**Group-level pattern across all nine markets with a published payment page:**

| Rail family | Markets where published | Markets where absent from the page |
|---|---|---|
| **Bank transfer / A2A / bill payment** | **All 9** | — |
| **Bank direct-debit mandate** | HK, MO, TH, JP, PH, MY, ID, (SG per unverified) | VN, KH |
| **Card as a recurring mandate** | HK, MO, TH, JP, PH, MY, ID | VN, KH |
| **One-off card payment** | TH (in-app), PH (portal + POS), MY (portal), VN (gateway) | **HK**, **MO**, **JP**, ID (mandate only), KH |
| **Cash / convenience store / agent** | HK, MO, TH, PH, VN, MY, KH | JP (post office + konbini via slip), ID |
| **Local digital wallet** | PH (GCash, Maya), VN (MoMo, Viettel Money), MY (TnG, Boost, ShopeePay, GrabPay), JP (7 slip apps), KH (TrueMoney) | **HK**, **MO**, **TH**, **ID** |

**The answer to the central question, stated plainly:** FWD collects premium **primarily through bank rails and mandates, not card-on-file**. Bank bill payment or A2A transfer is the only rail present in every single market. Card is a *mandate* rail more often than a *checkout* rail, and in Hong Kong — 64% of visible traffic — there is **no web card checkout at all**. The stub's hypothesis that FWD's digital-first positioning implies a larger web collection surface than a traditional insurer's is **partly true and partly false, and the distinction matters**: FWD has genuinely built digital *acquisition* and *servicing* (91% of new business applications submitted digitally, 73% e-submission rate, FWD Omne, FWD Cube, OneMod, 99% cloud migration) — but its *collection* surface is as bank-rail-dependent as any incumbent's, and in Hong Kong it is **more** so than markets like the Philippines. Digital-first front end, traditional collection back end. That gap is the opportunity.

> **MANUAL:** Use a VPN and a real policy to verify checkout APMs in Hong Kong, Thailand and the Philippines. Hong Kong first — confirming there is genuinely no card checkout, and no Octopus, AlipayHK or WeChat Pay HK, is the highest-value single verification in this report.

---
### Section 5: Payment Issues & Customer Complaints

**Source: public Apple App Store review RSS feeds for FWD Omne** (track id 1621673678, seller *FWD Group Management Holdings Limited*), 8 storefronts (ph, th, id, vn, my, jp, sg, hk), 310 most-recent reviews scanned. **24 mention payment**; ~10 describe an actual payment failure. Date range Jan 2024 – Aug 2026. Frequency assessed **moderate**.

| Issue Type | Platform | Frequency | Date Range | Source URL |
|---|---|---|---|---|
| **Card charged by bank but recorded as failed by FWD** — *"i tried to pay my premium using this app with my card it was unsuccessful due to system error but my bank acknowledge that my payment was successfully push through. It so hassle to coordinate between my bank and FWD."* (1★, v64.0.0) | App Store PH | Isolated but severe | 2026-06-23 | https://itunes.apple.com/ph/rss/customerreviews/id=1621673678/sortby=mostrecent/json |
| **Card-on-file update silently ignored** — *"Change of Payment Doesn't Take Effect. I already change the payment method of my policy. I change the card to be use for recurring payment but the payment was still charge to the previous card. I don't know what happen but they should have message me or email me if the card change was not accepted"* (3★, v63.0.5) | App Store PH | Moderate (recurs in JP too) | 2026-04-21 | Same |
| **Cannot pay at all near the due date** — *"Blank white screen. After entering verification code, it leads nowhere. My policy is almost due, i cant pay because i cant proceed with the app"* (1★, v19.0.1) | App Store PH | Isolated | 2023-08-17 | Same |
| **Amount paid ≠ amount applied to the policy** — *"เงินหาย: สมัครครั้งแรกจ่าย 2 พัน แต่ตัดเข้ากรรมธรรม 1 พัน จบยกเลิก"* ("Money gone: paid 2,000 on first signup but only 1,000 was applied to the policy — cancelled") (1★, v64.4.0) | App Store TH | Moderate | 2026-08-24 | https://itunes.apple.com/th/rss/customerreviews/id=1621673678/sortby=mostrecent/json |
| **Premium paid doesn't match the app** — *"ค่าเบี้ยทึ่จ่ายไปจริงกับที่ขึ้นในแอปไม่ตรงกัน"* ("the premium I actually paid doesn't match what shows in the app") (2★, v64.2.0) | App Store TH | Moderate | 2026-07-26 | Same |
| **False "success" on a card charge** — *"หักบัตรเครดิตงวดสุดท้ายไปแล้ว ใน omne ขึ้นสำเร็จ แต่ในแอปบัตรเครดิตไม่มียอดตัดบัตร สรุปคือจ่ายยัง? ถ้ายังอยู่ในขั้นดำเนินการก็ไม่ควรขึ้นว่าสำเร็จ"* ("The final credit-card deduction went through, Omne shows success, but there's no charge in my credit-card app. So did it pay or not? If it's still processing it shouldn't say success") (1★, v62.1.1) | App Store TH | Moderate | 2025-11-17 | Same |
| **Card-expiry / card-change flow unusable** — four separate 1★ Japanese reviews. *"クレジットカード変更しようとして、アプリダウンロードしたけど反応遅いし、結局開かないし、クレジットカード変更出来ない。webから出来るようにしてほしい"* ("Downloaded the app to change my credit card — slow, never opens, can't change the card. Please let us do it from the web"). *"クレジットカードの期限変更のためだけに、非常に手間がかかりました"* ("Enormous hassle just to change my card expiry date"). *"カードの支払い変更したいのにできない、という事は、いざ保険請求したいときなんて、できないという事？"* ("I want to change my card payment and can't — so when I actually need to claim, will that fail too?"). *"ウェブでできなくなってるわ、アプリもポンコツだわ... 他の保険会社はウェブで簡単にできた"* ("You can't do it on the web any more, and the app is junk... other insurers let me do it easily on the web") | App Store JP | **High within the Japanese cohort** | 2024-01-14 → 2024-11-30 | https://itunes.apple.com/jp/rss/customerreviews/id=1621673678/sortby=mostrecent/json |
| **FWD confirmed and then suspended its own card-change flow for a defect** — *"その後WEBページのほうを確認したら、一部の手続きで変更がされない不具合があったためアプリの手続きを停止してる旨のアナウンスがありました"* ("Checking the web page afterwards, there was an announcement that app procedures had been suspended because of a defect where some changes weren't being applied") (3★, later amended) | App Store JP | — | 2024 | Same |
| **Cannot reach the payment function** — *"ไม่สามารถกดเข้าฟังก์ชัน FWD Insurance เพื่อตรวจสอบข้อมูลกรมธรรม์ หรือชำระเบี้ยได้ค่ะ กดแล้วแอพพลิเคชั่นเด้งออกทุกครั้ง"* ("Can't open the FWD Insurance function to check policy details or pay premium — the app crashes every time") (1★) | App Store TH | Isolated | 2026 | Same |
| **Positive counter-evidence, included for balance** — *"I was ready to cry and spend hours to change my payment method, but I was able to do it in a minute instead. Never happened in all my years in Japan."* (5★, JP). *"It's convenient to change the payment method and quick."* (5★, TH). One Japanese 1★ was amended to 5★ after FWD support resolved an install-time defect. | App Store JP, TH | — | — | Same |

Overall app ratings are good — 4.68 stars on 40,824 ratings in the Thai storefront. The payment complaints are a **minority of a well-liked app**, and the report should say so. But they cluster with unusual precision:

> *"Pattern: three distinct and repeatedly-reported failure modes, each mapping to a named orchestration capability.* **(1) Authorisation-result ambiguity** *— the bank charges the card but FWD records a failure, or FWD shows 'success' with no corresponding card charge (PH 2026-06, TH 2025-11, TH 2026-08). This is what a missing single source of payment truth across providers looks like, and the subscription reference §2 names the fix — a unified view of failed and succeeded transactions across providers rather than per-PSP dashboards.* **(2) Stored-credential update failure** *— a customer changes the card on file and FWD keeps charging the old one, with no notification (PH 2026-04); and in Japan changing an expiring card is reported as near-impossible, with the web route removed and the app route once suspended for a defect. This is precisely the account-updater and network-token gap, and it is the direct upstream cause of the Japanese paper-slip dunning cascade documented in Section 4.* **(3) Reconciliation latency** *— amount-paid/amount-applied mismatches in Thailand, and FWD Singapore maintaining standing help-centre articles titled 'I have already made payment. Why is my policy still showing as unpaid?', 'Why hasn't my insurance payment been updated yet?' and 'How long does it take for my payment to be reflected in my insurance policy?' — the existence of three such articles is itself the finding (`[UNVERIFIED — search summary only, pages not fetched]`, help.fwd.com.sg returns 403)."*

One datapoint FWD publishes that is worth holding against all of the above: its stated **complaint ratio — complaints received per transaction — has been "consistently low at around 0.2 per cent for each year between 2022 and 2025"** ([HKEX FY2025 p.47](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf)). On a collection base of the size implied in Section 12, 0.2% is a large absolute number, and it is a *complaint* ratio rather than a *failure* ratio. Use it as a discovery question — "what does the payments slice of that 0.2% look like?" — not as a stick.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|---|---|---|---|
| 1 | 2026-09-11 | FWD Group publishes its 2026 interim report for the six months ended 30 June 2026 | Tech Blog / Conference Signal (financial reporting) | https://www.fwd.com/en/newsroom/press-releases/FWD-Group-publishes-2026-interim-report |
| 2 | 2026-08-26 | **Record H1 2026** — new business sales **US$1.35bn APE (+7%)**, NB CSM **US$996m (+25%)**, OPAT **US$298m (+20%)**, positive contribution from all four reportable segments; **"over 40 million customers across 10 markets"** | Funding / Financial Results | https://www.fwd.com/en/newsroom/press-releases/FWD-Group-reports-record-profit-amid-continued-growth |
| 3 | 2026-06-02 | **Jeffrey Woo appointed President Director of PT FWD Insurance Indonesia**, following approval from the Financial Services Authority (OJK) | Leadership Change | https://www.fwd.com/en/newsroom/press-releases/FWD-Group-appoints-Jeffrey-Woo-as-President-Director-of-FWD-Indonesia |
| 4 | 2026-05-18 | **Mark Bensman appointed Chief Officer, FWD High Net Worth**, effective 25 May 2026 — 25+ years in life insurance, previously Chief Distribution Officer at **Manulife** for 18 years building their HNW business | Leadership Change | https://www.fwd.com/en/newsroom/press-releases/FWD-Group-makes-key-hire-for-its-high-net-worth-business-Mark-Bensman-to-join-as-Chief-Officer-FWD-High-Net-Worth |
| 5 | 2026-04-30 | **Q1 2026** — new business sales **US$720m APE (+4%)**, NB CSM **US$556m (+18%)**, **11 new products** introduced around the region | Financial Results | https://www.fwd.com/en/newsroom/press-releases/FWD-Group-reports-strong-first-quarter-new-business-update-adding-to-its-consistent-track-record-of-financial-performance |

Also material, slightly older:
- **2025-07-07 — HKEX main board listing, stock code 1828.** ~91.34m shares at HK$38.00, gross proceeds ~HK$3.5bn (~US$445m), ~7.19% of post-offering share capital. Cornerstone investors included Mubadala Capital and a T&D Holdings subsidiary. Confirmed in the FY2025 results narrative: *"we began trading as a publicly listed company, following our July 2025 initial public offering."* ([HKEX FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf))
- **2025-12 / 2026-02 — index inclusions.** Added to the **Hang Seng Composite Index** and the Stock Connect eligible-securities list (Dec 2025), and the **MSCI Hong Kong Small Cap Index** (Feb 2026). ([HKEX FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf))
- **2025-12 — FWD Omne embedded inside SCB Easy**, the banking app serving 15m+ SCB customers in Thailand, delivered in a six-month window, with *"similar integration models... being deployed across other bank and ecosystem partners."* ([HKEX FY2025 pp.41, 46](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf))
- **2025 — FWD Cambodia × True Money (Cambodia) Plc** premium-payment and distribution partnership. ([HKEX FY2025 p.34](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf))
- **2025 — over 30 ecosystem partners** for digital commerce, *"including but not limited to HKT, Traveloka, yuu and GCash."* ([HKEX FY2025 p.43](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf))
- **2025-12-01 — PT FWD Insurance Indonesia Syariah incorporated.** A new licensed Indonesian entity, which in Malaysia's precedent (Takaful vs conventional) means a **separate portal and separate biller codes**. ([HKEX FY2025, note 34](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf))

**Public payment-related RFP:** *No public payment-related RFP found.*

**Payment-related hiring:** 9 roles mention "payment" in FWD's Workday careers site; **none is a payment-infrastructure role**, and a search for "payment gateway" returns 0 results. The closest is *Senior Manager, Backend Technology Delivery* (Hong Kong – Taikoo Shing Group Office, posted 2025-09-02), which is **claims**-platform modernisation: *"supporting the modernization of claims platforms... Conduct end-to-end assessments of the system lifecycle—from notification to payment."* That is claims payout, not premium collection. Note also the stale boilerplate in that posting — *"approximately 34 million customers"* — against the ~40m in the August 2026 release.

**Licence applications:** none found. **Deliberate negative worth stating explicitly:** searches of the 249-page FY2025 results for `payment service`, `e-money`, `payment gateway`, `autopay`, `direct debit`, `credit card` and `payment method` returned **zero** hits for every payment-licensing term. The only licence language in the whole document concerns insurance and takaful licences. This is the primary evidence for the Phase 0 verdict recorded in the ICP breakdown.

**Market expansion:** none in the last 12 months. Still 10 markets. The HNW build-out (FWD Private across Hong Kong, Singapore, Bermuda, with broker distribution into Dubai and Switzerland) extends collection geography without adding insurance entities.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | Effective **2026-07-01** | **REMOVAL — FWD Thailand discontinues premium payment via Advance mPAY Company Limited** | A live provider removal in a market generating US$2,621m TWPI. Site-wide notice: *"We would like to inform you that the premium payment service via Advance mPAY Company Limited will be discontinued effective 1 July 2026. You may continue paying your insurance premiums through the alternative payment."* A rail migration already in flight is the cleanest possible opening. | https://www.fwd.co.th/en/support/premium-payment/cc/ |
| 2 | View date **2026-07-27** | **FWD Singapore "Important Payout Update" — PayNow becomes the preferred claim and policy-benefit payout method**, *"with immediate effect"*; customers told to ensure PayNow is linked to their NRIC/FIN | Disbursement-side modernisation in a top-3 traffic market, in the same year collection remains on GIRO and bank transfer. Shows appetite for rail change; shows it happening payout-first. | https://www.fwd.com.sg/travel-insurance/ |
| 3 | **2025-12** | **FWD Omne integrated inside SCB Easy** (15m+ SCB customers) in a six-month build; *"similar integration models are being deployed across other bank and ecosystem partners"* | Embedding servicing — and therefore collection prompts — inside third-party banking apps multiplies the number of contexts a payment has to succeed in. Each new host is a new integration under the current model. | https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf |
| 4 | **2025** | **FWD Cambodia × True Money (Cambodia) Plc** — premium payment via the TrueMoney Wallet app and at TrueMoney agent locations nationwide | A wallet rail signed market-by-market in the one market with no web payment page at all. The pattern this report documents, in miniature. | https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf |
| 5 | **As at 2026-04-15** | **FWD Japan maintains a seven-app barcode slip-payment list** — PayPay, d払い, au PAY, 楽天ペイ, ゆうちょPay, PayB, FamiPay, with per-app caps (≤¥300,000; FamiPay <¥50,000) | Seven wallet integrations maintained **as a failure-recovery channel**, not as a primary rail. The dated list implies ongoing maintenance of each. | https://www.fwdlife.co.jp/support/cashless-payment/ |

> **REMOVAL: FWD Thailand reportedly discontinued the premium payment service via Advance mPAY Company Limited as of 1 July 2026. Source: https://www.fwd.co.th/en/support/premium-payment/cc/**

Also noted, and older: **FWD Singapore launched electronic claims payouts via PayNow with DBS Bank in June 2018**, replacing claims cheques, capped at S$200,000 per transaction ([source](https://hnworth.com/article/invest/insurance/fwd-insurance-launches-electronic-claims-payments-via-paynow/)). Eight years of PayNow on the payout side is useful context for the July 2026 payout update — and a reminder that FWD's payout rails have modernised faster than its collection rails.

---

### Section 8: Checkout Experience Audit

**Scope note.** FWD sells insurance; "checkout" here means the **premium-payment surface** available to a policyholder, which in eight of ten markets sits behind an authenticated policy-servicing login or inside the FWD Omne mobile app. `eservices.fwd.com.hk` returns HTTP 403; `help.fwd.com.sg` returns 403 behind Cloudflare; the FWD Omne in-app payment flows cannot be reached without a live policy. **Full checkout flow not accessible. Findings below are limited to publicly observable elements** — the published payment pages, their embedded CMS payloads, the shipped JavaScript of the two reachable payment portals, and HTTP response headers.

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | **Custom-built, per market, no common component.** Six+ distinct surfaces on five hostnames across three web stacks (Contentstack+Next.js ×9 markets, bare static Next.js for Cambodia, WordPress for Singapore). | **Poor** (as a group), Fair per market | The clearest observable signal of the absent orchestration layer |
| Guest checkout | **Policy number + date of birth only** in the Indonesia FWD Pay Portal — no account creation needed. Philippines portal similar. Hong Kong and Japan require full eServices/app login for most actions. | Good (ID, PH) / Fair (HK, JP) | Low-friction where it exists |
| Steps to complete payment | Indonesia autodebit registration: portal login → add card → **redirect to AyoConnect** → bank-dependent confirmation → *"your next renewal premium payment will be debited using the related card"* — i.e. **the mandate is not live for the current cycle**. Hong Kong autopay: **~2 months to process**. Macau autopay: **2 months plus two months' premium prepaid**. Thailand card autopay: **apply ≥10 working days before the due date**. | **Poor** | A policyholder in payment trouble cannot fix it in the current cycle in HK, MO or ID |
| Card input experience | **Indonesia: card fields post to FWD's own domain** (`form-action 'self'`, `connect-src 'self'`) — no PSP iframe, no hosted field. Philippines: server-fetched gateway URL then redirect (`GET_EPF_PAYMENT_URL`). Hong Kong, Macau, Japan: **no web card entry at all** — card is registered by form, by post, by app QR code, or not at all. | Poor (ID, on PCI grounds) / Not applicable (HK, MO, JP) | See Section 9 |
| Payment methods visible | 3 (Indonesia) to 9 (Thailand). **Hong Kong: 8 methods, none of them a one-off card.** | Fair, highly uneven | The variance *is* the finding |
| Location-based method display | **None.** Methods are hard-coded per market domain; there is no geo-adaptive method list anywhere. A Mainland Chinese visitor on `fwd.com.hk` — 13.47% of combined traffic — sees the Hong Kong method set, full stop. | **Poor** | Direct consequence of the per-market architecture |
| Instalment / EMI options | **Not found in any market.** Malaysia offers the reverse — "Future Premium Payment", paying *in advance*, by phone call. Thailand and Japan, both instalment-heavy card markets, show no premium instalment option. | Poor | Low relevance for life premium, but a real gap in Japan's bonus-payment culture |
| 3DS implementation | **Not detected.** No 3DS, ThreeDS, Cardinal or equivalent signature in any reachable bundle. **Japan is the one market with an explicitly documented authorisation step** — a validity check ("オーソリ") before each recurring charge since June 2022. | Not established | Any claim about Japan's EC 3DS requirements must be sourced live; none is made here |
| PCI indicator | **Indonesia: self-hosted card fields on FWD's own origin** (`form-action 'self'`). Philippines: server-side gateway handoff. Elsewhere: no card entry surface. **No PSP iframe or hosted-field pattern observed in any market.** | Poor (ID) | See Section 9 |
| Mobile responsiveness | **`fwd.com.hk` is 77.17% mobile web** and FWD's strategy is explicitly mobile-first (FWD Omne, 91% digital new-business submission). Yet Japanese reviewers report the **web** card-change route was *removed*, forcing app-only, and the app route was itself suspended for a defect. | Fair, with a documented regression | Mobile-first that removed the web fallback and then broke the app path |
| Multi-currency / local pricing | **Hong Kong supports eight policy currencies** — HKD, AUD, CAD, EUR, GBP, RMB, SGD, USD — with FWD-published exchange rates; HKD policies take HKD only, the rest take policy currency or HKD. Macau takes cash in USD/HKD/MOP/RMB, RMB only at LUSO Bank. | Good coverage, manual execution | FX is handled by rate tables and branch rules, not at the payment layer |
| Saved payment methods | Yes, as mandates: HK "Register default payment method" / "Change of payment option" (cash/cheque, bank direct debit, credit-card autopay); ID card-on-file via AyoConnect; MY card in myPortal; JP card registered by QR code on a posted letter. | Fair | **Three app-store reviews report the saved method not updating** (Section 5) |
| Error message clarity | **Documented as poor by FWD's own customers.** Omne showing "success" with no corresponding card charge (TH); a bank charge recorded as a system-error failure (PH); a card-on-file change that silently didn't apply, with the customer explicitly asking *"they should have message me or email me if the card change was not accepted"* (PH). Japan's failure messaging is a **postcard, arriving weeks later**. | **Poor** | Section 5 |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **Not found.** No PCI DSS level, AoC or SAQ type is published by FWD in any market. The 249-page FY2025 results announcement contains **zero** occurrences of "PCI". | https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf |
| Card data handling | **Mixed, and at least one market is not SAQ A.** Indonesia's FWD Pay Portal serves `script-src 'self'; connect-src 'self'; form-action 'self'; base-uri 'self'; frame-ancestors 'none'; object-src 'none'` — **card data is entered into and submitted to FWD's own origin**, with no third-party iframe and no permitted cross-origin XHR. That is the signature of **SAQ A-EP or wider scope**, not SAQ A. The Philippines portal fetches a gateway URL server-side (`GET_EPF_PAYMENT_URL`) and redirects, which is more consistent with a redirect model. Hong Kong, Macau and Japan have no web card-entry surface at all, so their scope sits in back-office and mandate-file handling rather than on the web. | https://www.fwd.co.id/FWDPayPortal/login (response headers) · https://payment.fwd.com.ph/static/js/main.b6800dfd.chunk.js |
| Recommended Yuno integration | **Hosted SDK / drop-in, market by market, prioritising Indonesia.** Replacing self-hosted card fields with a hosted tokenised component would move the Indonesia portal from SAQ A-EP toward SAQ A and remove FWD's own origin from the card-data path. **Back-to-back API** is the right fit where the collection event is a mandate debit rather than a cardholder-present payment — Hong Kong autopay, Macau autopay, Thailand's two auto-recurring rails, Japan's 口座振替/card modes, and the Philippines' ACA/ADA. | — |

> `[INFERENCE, not confirmed]`: Indonesia's `form-action 'self'` and `connect-src 'self'` directives indicate card data is posted to FWD's own domain rather than to a PSP, which implies FWD carries card-data scope on that flow. This is read off the live CSP header, not from any FWD statement about its PCI posture. **Confirm with FWD before using it in a conversation** — a CSP can be stricter than the actual data path if the card fields are, for example, a PSP script already inlined under `'self'`.

Also relevant: FWD Japan states it changed its card payment system in June 2022 to perform a validity authorisation before each charge *"at the request of the card companies and in line with strengthened security measures"* — evidence of card-scheme-driven change being absorbed market-by-market, at FWD's own cost, in one market at a time ([source](https://www.fwdlife.co.jp/support/credit_payment/)).

---
### Section 10: Strategic Insights & Outreach Angles

Cross-reference pass performed: traffic (S1) × entities (S2) for the China gate and the Taiwan anomaly; traffic (S1) × methods (S4) for the Hong Kong card absence; methods (S4) × complaints (S5) for the Japan/Philippines credential-update failure; developments (S6/S7) × stack (S3) for the mPAY migration window; competitors (S11) × orchestrator check (S3B) for competitive urgency; billing-channel check (S6, APE mix) for the app-store trap — **not applicable**, FWD bills insurance premium, not IAP.

---

> **Insight #1: Japan's card-failure recovery runs on the postal service, and FWD documented it themselves**
>
> **Evidence:** **Section 4 (Japan)** — FWD's own support pages describe a three-stage postal dunning cascade: a postcard after the first decline, an envelope containing a paper payment slip plus a QR code for re-registering a card after the second, and a third letter if the card company reports the card invalid. Arrears are then settled at a convenience store, a post office, or by barcode in one of seven wallet apps, and *"if not paid by the deadline, the policy lapses (失効) or an automatic premium loan is applied"* ([fwdlife.co.jp/support/credit_payment/](https://www.fwdlife.co.jp/support/credit_payment/) · [fwdlife.co.jp/support/cashless-payment/](https://www.fwdlife.co.jp/support/cashless-payment/)). FWD also states it runs a card-validity authorisation before every charge, since June 2022, *"at the request of the card companies"* — so an expired or reissued card fails deterministically. **+ Section 5 (complaints)** — four separate 1★ Japanese App Store reviews, Jan–Nov 2024, describe being unable to change an expiring card: *"Enormous hassle just to change my card expiry date"*; *"You can't do it on the web any more, and the app is junk... other insurers let me do it easily on the web"*; and FWD itself posted a notice suspending the app's change flow for a defect where some changes weren't applied ([itunes.apple.com/jp/rss/customerreviews/id=1621673678](https://itunes.apple.com/jp/rss/customerreviews/id=1621673678/sortby=mostrecent/json)). **+ Section 12** — Japan contributes **US$1,112m of renewal premium a year**, the group's third largest renewal pool, against only US$114m of first-year premium: Japan is almost entirely a renewal book, which is exactly the book this failure mode attacks ([HKEX FY2025 p.106](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf)).
>
> **Pain Point:** A routine card reissue — an event with no customer intent behind it whatsoever — starts a recovery process measured in months, costed in printing and postage, dependent on the customer successfully completing two separate actions, and ending in lapse or a policy loan. FWD has engineered a careful, humane, expensive paper process around a gap that is normally closed at the credential layer. Every lapse here is a customer who still wanted the cover.
>
> **Yuno Value Proposition:** Network tokens and account updater inside the routing layer, so a reissued or re-expired card refreshes without the customer touching anything and without a per-PSP project — exactly the mechanism the recurring-payments reference names for this cause. Retry sequencing informed by decline code and issuer rather than FWD's fixed next-month re-request. And a single view of failed renewals, so the Japan team sees the failure the day it happens rather than at the next monthly cycle. Nothing here changes FWD's distribution, its bank partners or its product — it operates purely on the credential and the retry.
>
> **Best Success Case:** **Garena.** The match is not vertical, it is mechanism: a multi-market consumer business where credentials and local rails have to keep working across many countries under one integration, rather than per-market. *(Publicly referenceable Yuno customer; no published metrics, and none implied.)*
>
> **Outreach Angle:** Your own support pages lay out the Japan path when a card declines — postcard, then an envelope with a 払込取扱票 and a QR code for a new card, then konbini or Japan Post or one of seven barcode apps, and lapse if the deadline passes. Given you've been running a pre-charge authorisation since June 2022, I'd guess most of what triggers that is just cards being reissued.
>
> **Suggested Subject Line:** The 払込取扱票 path for an expired card

---

> **Insight #2: Hong Kong is 64% of your visible traffic, 77% mobile, and has no card payment**
>
> **Evidence:** **Section 1** — Hong Kong is **64.24%** of combined visible traffic (507,296 of 789,646 visits) and `fwd.com.hk` runs **77.17% mobile web** (SimilarWeb, supplied 2026-10-09). **+ Section 4 (Hong Kong)** — FWD's own premiums-and-payments page lists **eight** methods and **not one is a one-off card payment**: FPS by QR scan only and capped at HK$400,000, online-banking bill payment under merchant "FWD LIFE INSUR CO(BERMUDA) LTD" with five bill-type codes, JETCO/HSBC/Hang Seng ATM, PPS merchant code 9130, physical cheques with post-dated cheques refused, cash/cheque/EPS at a branch, Hongkong Post cash under HK$120,000, and autopay — where autopay takes *"approximately 2 months after autopay application"* to process, and card exists only inside it ([fwd.com.hk/en/support/premiums-payments/](https://www.fwd.com.hk/en/support/premiums-payments/)). No Octopus, no AlipayHK, no WeChat Pay HK, no Apple or Google Pay. **+ Section 8** — there is no geo-adaptive method list anywhere in the group, so the method set is fixed by which domain you landed on.
>
> **Pain Point:** A policyholder on a phone, at the moment of a premium notice, is offered bank QR codes, merchant and bill-type codes to copy, an ATM, a cheque, a post office, or a two-month mandate application. On the largest market, the highest-mobile market, the one carrying eight policy currencies and the Mainland-visitor book. There is no instant path to pay, and no instant path to cure a failed mandate within the cycle.
>
> **Yuno Value Proposition:** One integration that adds the instant rails Hong Kong consumers already hold — card, local wallets, Apple and Google Pay — alongside the bank rails FWD already runs, without rebuilding eServices and without touching the eight-currency policy logic. Hong Kong is also where mandate failure is most expensive to cure, so instant one-off payment is worth more here than anywhere else in the group.
>
> **Best Success Case:** **Qatar Airways.** A multi-market, multi-currency collection business operating against a single home entity — the same shape as FWD Hong Kong accepting eight policy currencies from local, Mainland and overseas policyholders. *(Publicly referenceable; no published metrics.)*
>
> **Outreach Angle:** Your Hong Kong premiums page lists eight ways to pay — FPS QR, bill payment, ATM, PPS, cheque, branch, Hongkong Post, autopay — and no card. With `fwd.com.hk` running close to 77% mobile web, I'm curious whether that's a deliberate cost position or just the order things got built in.
>
> **Suggested Subject Line:** Eight payment methods in Hong Kong, no card

---

> **Insight #3: Two vendors, six portals, five JomPAY codes — and a rail switching off in July**
>
> **Evidence:** **Section 3A/3B** — iPay88 named on FWD Malaysia's own payments page, AyoConnect named on FWD Indonesia's page *and* inside the FWD Pay Portal's shipped JavaScript; six+ separate payment surfaces across five hostnames and three web stacks; hand-maintained per-entity biller codes — PPS 9130 (HK), JETCO 105 (MO), seven Thai bank Com Codes, **five JomPAY biller codes split across FWD Insurance Berhad and FWD Takaful Berhad in one country**. All eleven domains, meanwhile, sit behind one standardised CloudFront + volt-adc edge, consistent with FWD's own claim of 99% cloud migration under OneMod ([HKEX FY2025 p.45](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf)). **The edge is unified. The payment layer is not.** **+ Section 7** — FWD Thailand is **retiring Advance mPAY effective 1 July 2026** ([fwd.co.th](https://www.fwd.co.th/en/support/premium-payment/cc/)), in a market generating US$2,621m of TWPI; FWD Omne went live inside SCB Easy in Dec 2025 with *"similar integration models... being deployed across other bank and ecosystem partners"*; FWD Cambodia signed TrueMoney in 2025; and **PT FWD Insurance Indonesia Syariah was incorporated on 1 December 2025** — which, on Malaysia's precedent, means another portal and another biller-code set. **+ Section 6** — Q1 2026 alone introduced 11 new products across the region.
>
> **Pain Point:** Every new rail, new ecosystem host, new product and new licensed entity is a fresh point-to-point integration, a fresh biller code, a fresh portal, and a fresh thing to decommission later — which is precisely what the mPAY retirement is right now. FWD has already proved it can standardise infrastructure at group level with OneMod and the cloud migration; payments is the layer that did not get that treatment, and the cost shows up as the marginal cost of every single market initiative.
>
> **Yuno Value Proposition:** One integration, one dashboard, provider changes as configuration rather than engineering. The mPAY removal is the concrete case: adding or retiring a rail becomes a switch rather than a release, in each of ten markets, for each of two Malaysian entities and now a third Indonesian one. This is the same argument OneMod already won internally for policy administration — applied one layer down.
>
> **Best Success Case:** **Garena.** Many markets, many local rails, one integration — chosen on the fragmentation profile, not on vertical. *(Publicly referenceable; no published metrics.)*
>
> **Outreach Angle:** Noticed FWD Thailand is retiring the mPAY premium rail on 1 July. With iPay88 in Malaysia, AyoConnect in Indonesia, five JomPAY biller codes across your two Malaysian entities and a new Syariah entity incorporated in December, I'd expect switching a rail off to be a release rather than a setting.
>
> **Suggested Subject Line:** mPAY off on 1 July — how many releases?

---

> **Insight #4: China is your #2 traffic market, the majority of your HK offshore VNB, and you have a representative office**
>
> **Evidence:** **Section 1** — China is **13.47%** of combined visible traffic (106,369 visits), and **15.92%** of `fwd.com.hk` specifically (SimilarWeb, supplied 2026-10-09). **+ Section 2** — the audited principal-subsidiaries list contains **no PRC entity**, and FWD's own country selector labels `fwd.cn` a **"China representative office"**. **+ Section 1 / HKEX FY2025 p.31** — *"More than half of FWD Hong Kong & Macau's VNB was achieved domestically"* and *"approximately 44 per cent of offshore VNB from outside of Mainland China"* — so the majority of FWD Hong Kong's offshore new-business value comes from Mainland China. **+ Section 4 (Hong Kong)** — FWD Hong Kong issues policies in **RMB** among its eight policy currencies, and accepts cash in **HKD, USD or Renminbi** at its Insurance Solutions Centres, capped at US$50,000 per customer per year ([fwd.com.hk](https://www.fwd.com.hk/en/support/premiums-payments/)).
>
> **Pain Point:** A large and strategically important cohort of policyholders lives in Mainland China, holds policies issued by a Hong Kong entity, often denominated in RMB, and must pay premium **every year for the life of the policy** using Hong Kong rails: an FPS QR code, a Hong Kong bill payment, a Hong Kong cheque, or cash handed over in person at a Hong Kong branch. Acquisition happens once, at a branch visit. Collection happens every year, from a thousand kilometres away, on rails designed for Hong Kong residents.
>
> **Yuno Value Proposition:** **Careful positioning required, and this is the honest version.** FWD holds no PRC insurance licence — orchestration cannot and will not create a domestic China collection path for a business with no domestic entity, and anyone who pitches that will be corrected in the first sixty seconds. What orchestration *can* address is the recurring collection experience for Mainland-resident holders of Hong Kong-issued policies: routing, retry and credential handling for cross-border card renewals, and broader instant-rail acceptance against the Hong Kong entity. **Argue the corridor, not the region**, and treat approval rate and completion rate as the metric, not fee.
>
> **Best Success Case:** **Qatar Airways** — collection against one home entity from customers spread across many geographies. *(Publicly referenceable; no published metrics.)*
>
> **Outreach Angle:** Your FY2025 disclosure puts the majority of FWD Hong Kong's offshore VNB with Mainland customers, and `fwd.com.hk` runs about 16% Mainland traffic. Since FWD's China presence is a representative office, those renewals must be coming back through Hong Kong rails every year — FPS QR, bill payment, or cash at a Solutions Centre.
>
> **Suggested Subject Line:** Mainland renewals on Hong Kong rails

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. Your Hong Kong premiums page lists eight ways to pay — FPS QR, bill payment, ATM, PPS, cheque, branch, Hongkong Post, autopay — and no one-off card, on a domain running close to 77% mobile web.
2. Your own Japan support pages describe the path when a card declines: a postcard, then an envelope with a 払込取扱票 and a QR code for a new card, then konbini or Japan Post or one of seven barcode apps, and lapse if the deadline passes.
3. FWD Thailand is retiring the Advance mPAY premium rail on 1 July 2026 — with iPay88 in Malaysia, AyoConnect in Indonesia and five JomPAY biller codes across your two Malaysian entities, I'd guess switching a rail off is a release rather than a setting.
4. Your FY2025 results put the majority of FWD Hong Kong's offshore VNB with Mainland customers, and FWD's China presence is a representative office — so those renewals come back through Hong Kong rails every year, for the life of the policy.
5. Hong Kong autopay takes about two months to process and Macau's needs two months' premium prepaid, which means a policyholder whose mandate just failed can't fix it inside the current cycle.

**Cold call openers (conversational, one sentence each):**
1. "I was reading your Japan support pages — when a card charge fails you post a physical payment slip and the customer settles it at a konbini; is that mostly cards being reissued, or genuinely insufficient funds?"
2. "Your Hong Kong premiums page has eight payment methods and none of them is a one-off card payment — was that a deliberate cost decision, or just the order things got built in?"
3. "You're switching off the mPAY rail in Thailand in July — how many releases does retiring a payment rail actually cost you, across ten markets?"
4. "Malaysia has five JomPAY biller codes across FWD Insurance Berhad and FWD Takaful Berhad, and you've just incorporated a Syariah entity in Indonesia — does that mean a third portal?"
5. "You got 99% of applications onto the cloud under OneMod — did payments ever get that treatment, or is it still per-market?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors (5–8 companies)

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---|---|---|---|---|---|---|
| AIA Group | aia.com | Hong Kong | ~$20B revenue (per `apac-tal.csv`, **unverified**) | HK, MO, TH, PH, ID, SG, VN, MY, CN (licensed), + more | **Not established.** AIA Vietnam ran an API-based claims payout with **DBS** — disbursement, not collection. `[UNVERIFIED — search summary only, page not fetched]` | https://www.dbs.com.sg/corporate/insights/case-studies/api-based-insurance-claim-payment-solution |
| Prudential plc | prudentialplc.com | Hong Kong | Not found | HK, TH, PH, ID, SG, VN, MY, + more | **Not established** | `accounts/apac-tal.csv` (lead list, no source) |
| Manulife (Asia) | manulife.com | Toronto / Asia HQ Hong Kong | ~$20B Asia segment (per `apac-tal.csv`, **unverified**) | HK, JP, PH, ID, SG, VN, MY, KH | **Not established.** Direct talent link: FWD hired Manulife's Chief Distribution Officer as Chief Officer, FWD HNW, May 2026. | https://www.fwd.com/en/newsroom/press-releases/FWD-Group-makes-key-hire-for-its-high-net-worth-business-Mark-Bensman-to-join-as-Chief-Officer-FWD-High-Net-Worth |
| Great Eastern | greateasternlife.com | Singapore | Not found | SG, MY, ID | **Not established** | No source found |
| **MSIG Insurance** | msig.com | Singapore (regional) | Not found | TH, SG, MY, HK, PH, ID, VN | **2C2P — CONFIRMED.** "MSIG Insurance streamlines payments across 20+ branches with 2C2P"; needed *"comprehensive payment channel coverage, secure mobile integration, and the ability to provide installment plans"*; 2C2P became *"the payment backbone for the insurer"* (Thailand). **Gateway, not an orchestrator.** | https://www.casestudies.com/company/2c2p/case-study/msig-insurance-streamlines-payments-across-20-branches-with-2c2p |
| **Singlife** | singlife.com | Singapore | Not found | SG | **2C2P — CONFIRMED.** Lacked preferred payment methods, had integration difficulties, needed multi-bank instalments; integrated 2C2P's Payment Gateway starting with Amex, later interested in digital wallets. `[UNVERIFIED — search summary only, page not fetched]` | 2c2p.com (via search; page not fetched) |
| Sun Life Asia | sunlife.com | Toronto / Asia HQ Hong Kong | Not found | HK, PH, ID, VN, MY | **Not established** | No source found |
| Dai-ichi Life | dai-ichi-life.co.jp | Japan | Not found | JP, TH, VN, ID, KH, MY, AU | **Not established** | No source found |

#### 11B. Industry Peers / Same Vertical (5–8 companies)

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---|---|---|---|---|---|
| bolttech | bolttech.io | Embedded insurance | 30+ markets, SG HQ | Multi-market premium collection with an explicitly digital-first model; ~$300M est. revenue | `accounts/apac-tal.csv` (**unverified**) |
| Cover Genius | covergenius.com | Embedded insurance | AU HQ, global | Multi-market, API-first collection. ⚠️ **I checked Adyen's own insurance page and Cover Genius is NOT named there — only Clearcover is.** Do not repeat the Adyen–Cover Genius link. | https://www.adyen.com/en_SG/industries/financial-services/insurance |
| Igloo | iglooinsure.com | Insurtech | SG HQ, SEA | Wallet and telco-partner collection in exactly FWD's SEA markets | `accounts/apac-tal.csv` (**unverified**) |
| Roojai | roojai.com | Direct insurtech | TH, ID | Direct-to-consumer card and instalment collection in two FWD markets; ~$40M est. revenue | `accounts/apac-tal.csv` (**unverified**) |
| Sunday Insurance | easysunday.com | Insurtech | TH, ID | Same two markets, digital collection; ~$50M est. revenue | `accounts/apac-tal.csv` (**unverified**) |
| Qoala | qoala.app | Insurtech | ID, TH, MY | QRIS / wallet-era collection in three FWD markets; ~$50M est. revenue | `accounts/apac-tal.csv` (**unverified**) |
| PasarPolis | pasarpolis.io | Insurtech | ID, VN, TH | Ecosystem-embedded collection; ~$40M est. revenue | `accounts/apac-tal.csv` (**unverified**) |
| OneDegree | onedegree.hk | Digital insurer | HK | FWD's only digital-native competitor in its largest market; ~$30M est. revenue | `accounts/apac-tal.csv` (**unverified**) |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| Star Health Insurance (India) | **Juspay / Hyperswitch** — vendor case study claims multiple PSPs unified, routing on success rate/cost/network conditions, real-time acceptance monitoring, automated reconciliation, mandate support, instalments, and reduced renewal drop-off. **No before/after figures published.** `[UNVERIFIED — search summary only, page not fetched: HTTP 403]` | Not stated | Health insurance | https://hyperswitch.io/case-studies/star-health-insurance |
| Zurich Insurance | **Juspay Hyperswitch** — a promotional LinkedIn post by a Juspay representative claims Zurich is live across 200+ countries and multiple entities and providers. **Promotional, not a case study.** `[UNVERIFIED — search summary only, page not fetched]` | Not stated | Insurance (global) | LinkedIn (vendor post; page not fetched) |
| 11 Indian insurers on `apac-tal.csv` | **Juspay** per the TAL's orchestrator column — ACKO, Digit, Galaxy Health, ICICI Lombard, ICICI Prudential Life, IFFCO Tokio, Kotak General, Niva Bupa, Onsurity, Star Health, Tata AIA Life, Zuno | Not stated | Insurance | `accounts/apac-tal.csv` — **a lead list, not a source.** Only Star Health is independently corroborated, and that corroboration is itself unfetched. |

> **No public case study found of a direct competitor in FWD's own ten markets adopting payment orchestration.** Two of FWD's regional competitors (MSIG, Singlife) are on **2C2P**, which is a gateway rather than an orchestrator. The insurance vertical in APAC *is* orchestration-aware — but that awareness is concentrated in **India**, which is not an FWD market. This is why the ICP matrix scores the "competitor using orchestration" row **0**. One genuinely useful consequence: FWD is **early**, not late, among pan-Asian life insurers. That is a better story than catch-up, and it is the honest one.

#### 11D. Prospect Scoring

Applying the same 29-point matrix to the peers above, on **verified signals only**. Most of these rows are sparse because `apac-tal.csv` estimates carry no source.

| Signal | Points | Status | Evidence Source |
|---|---|---|---|
| **MSIG Insurance** — multiple PSPs/gateway confirmed | +3 | ✅ 2C2P confirmed as "the payment backbone", Thailand, 20+ branches | https://www.casestudies.com/company/2c2p/case-study/msig-insurance-streamlines-payments-across-20-branches-with-2c2p |
| MSIG — 3+ countries | +3 | ✅ Regional (SG-HQ'd, multi-market APAC operations) | Same + `apac-tal.csv` |
| MSIG — orchestration status | +4 | ✅ None detected; 2C2P is a gateway, not an orchestrator → greenfield | Same |
| MSIG — all other rows | 0 | ⬜ Not researched in this run | — |
| **Singlife** — multiple PSPs/gateway | +3 | ✅ 2C2P Payment Gateway, started with Amex, wallets of interest. `[UNVERIFIED — search summary only]` | 2c2p.com (not fetched) |
| Singlife — 3+ countries | 0 | ❌ Singapore only per `apac-tal.csv` | `apac-tal.csv` |
| Singlife — orchestration status | +4 | ✅ None detected → greenfield | Same |
| **bolttech / Igloo / Qoala / Roojai / Sunday / PasarPolis / OneDegree** | — | ⬜ **Not scored.** Only unsourced `apac-tal.csv` revenue estimates are available; scoring them would be inventing signals. | `apac-tal.csv` |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|---|---|---|---|---|---|---|---|
| 1 | **MSIG Insurance** | Direct competitor | TH, SG, MY, HK, PH, ID, VN | 10+ (partial) | 🟢 Medium+ | **2C2P confirmed as "the payment backbone"** — gateway, not orchestrator; greenfield, and already proven willing to buy payments | ✅ Yes |
| 2 | **Singlife** | Direct competitor | SG | 7+ (partial) | 🟢 Medium | **2C2P gateway confirmed**; publicly wanted more methods and multi-bank instalments | ✅ Yes |
| 3 | AIA Group | Direct competitor | HK, MO, TH, PH, ID, SG, VN, MY, CN | Not scored | ⬜ | Same recurring-premium hook at larger scale; stack not established | ✅ Yes |
| 4 | Prudential plc | Direct competitor | HK, TH, PH, ID, SG, VN, MY | Not scored | ⬜ | Same hook; stack not established | ✅ Yes |
| 5 | Manulife (Asia) | Direct competitor | HK, JP, PH, ID, SG, VN, MY, KH | Not scored | ⬜ | FWD just hired their HNW distribution lead — a live relationship signal | ✅ Yes |
| 6 | bolttech | Peer | 30+ markets | Not scored | ⬜ | Embedded, multi-market collection by design | ✅ Yes |
| 7 | Igloo | Peer | SEA | Not scored | ⬜ | Wallet/telco collection across FWD's SEA markets | ✅ Yes |
| 8 | Qoala | Peer | ID, TH, MY | Not scored | ⬜ | QRIS-era collection in three FWD markets | ✅ Yes |
| 9 | Roojai | Peer | TH, ID | Not scored | ⬜ | D2C card + instalment collection | ✅ Yes |
| 10 | **Great Eastern** | Direct competitor | SG, MY, ID | Not scored | ⬜ | **NOT on `apac-tal.csv`** — a top-3 Singapore/Malaysia life insurer with direct FWD overlap, genuinely missing from the list | ❌ **No — genuine find** |

**Strong prospects not on the list:** **Great Eastern** (Singapore/Malaysia/Indonesia life, direct FWD overlap, absent from `apac-tal.csv`) and, with weaker justification, **Sun Life Asia** (HK, PH, ID, VN, MY — also absent). Both are worth adding.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | **Insurance revenue US$2,911m (FY2025)**, up from US$2,724m (FY2024). Note that under IFRS 17 insurance revenue is **not** the premium collected. | [HKEX FY2025, note 6](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf) — **fills the blank revenue cell in `apac-tal.csv`** |
| **Premium cash received (the collection number that matters)** | **US$12,907m (FY2025)**, vs US$9,017m (FY2024) — **+43% year on year** | [HKEX FY2025, note 17 p.125](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf) |
| GMV / Gross Transaction Volume | **TWPI US$7,783m (FY2025)**, vs US$6,632m (FY2024). By segment: Hong Kong & Macau 2,903 · Thailand & Cambodia 2,621 · Japan 1,232 · Emerging Markets 1,027. TWPI = 100% renewal + 100% first-year + 10% single premiums, before reinsurance ceded. | [HKEX FY2025, note 5.5 p.106](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf) |
| **Renewal premiums — the recurring collection base** | **US$5,431m (FY2025)**, vs US$4,826m (FY2024). Hong Kong & Macau **1,695** · Thailand & Cambodia **2,062** · Japan **1,112** · Emerging Markets **562**. | Same |
| First-year premiums | **US$1,875m.** HK & MO 854 · TH & KH 549 · JP 114 · EM 358 | Same |
| Single premiums | **US$4,761m.** HK & MO 3,540 · TH & KH 99 · JP 56 · EM 1,066 | Same |
| New business sales (APE) | **US$2,446m (FY2025, +25%)**; H1 2026 **US$1.35bn (+7%)**; Q1 2026 **US$720m (+4%)** | [HKEX FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf) · [FWD newsroom](https://www.fwd.com/en/newsroom/) |
| Average Transaction Value (USD) | **Not found.** FWD publishes no average premium per policy and no policy count in any document I could reach. | — |
| Est. Annual Transactions | **Cannot be calculated without an ATV.** See the row below. | — |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. `[ASSUMPTION — not researched.]`** **Basis:** FY2025 renewal premiums of **US$5,431m** and premium cash received of **US$12,907m** are both sourced, but **no average premium and no policy count are published**, so this cannot be derived — it is an assumption. For the renewal pool alone to fall below 100,000 collections per month, the average annual renewal premium would have to exceed **~US$4,526** (5,431m ÷ 1.2m), which is implausible for a book that includes micro-insurance distributed through Bank Simpanan Nasional's rural network in Malaysia and mass-market protection across the Philippines, Indonesia, Vietnam and Cambodia. First-year (US$1,875m) and single (US$4,761m) premium collections sit on top of that. **Billing unit counted: premium collection events, not policies and not customers.** **Premium frequency drives the entire calculation and is not disclosed** — an annual-mode policy bills once a year, a monthly-mode policy twelve times, and the mode mix is unpublished; FWD Philippines states that monthly billing is only available via ACA/ADA bank mandate, which hints that monthly-mode penetration is constrained by mandate enrolment. **Per the disclosure rule, this assumed figure cannot and does not trigger the under-40,000 rejection.** | Sourced inputs: [HKEX FY2025, notes 5.5 and 17](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf). The assumption is mine and is labelled. |
| **Orchestration-addressable share** | **A minority of the above, and this must be stated in any business case.** FY2025 APE by channel: **bancassurance 37%, brokerage/IFA 37%, agency 19%, others 8%** — where "others" *includes but is not limited to* D2C digital commerce, affinity, employee benefits, direct marketing and telemarketing. Where a bank partner owns the relationship (SCB, VCB, BRI, Security Bank, HSBC Amanah, Alliance Bank, BSN), it frequently owns the debit mandate. The addressable surface is the **renewal-collection and self-service layer**: six market payment portals, FWD Omne in-app payment, card-autopay mandate registration and re-registration, and the wallet/convenience rails. **Sizing this properly requires a discovery call. Do not present US$12.9bn as addressable.** | [HKEX FY2025 p.40](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf) |
| Active Customers / Users | **Over 40 million across 10 markets (Aug 2026)**, including BRI Life. Progression: ~34m (Workday boilerplate, Sep 2025) → **38m** (FY2025, Mar 2026) → ~40m (May/Jun/Aug 2026). **Discrepancy flagged, not resolved** — see Source Notes. | [FWD newsroom, 26 Aug 2026](https://www.fwd.com/en/newsroom/press-releases/FWD-Group-reports-record-profit-amid-continued-growth) · [HKEX FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf) |
| Distribution scale | **40,000+ agents**; **33 bancassurance partnerships** (7 exclusive in SEA) reaching a partner customer base of **over 350 million**; **~2,800 IFA and brokerage partners**; **30+ ecosystem partners** incl. HKT, Traveloka, yuu and GCash | [HKEX FY2025 pp.40–43](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf) |
| Primary Currency | **USD reporting.** Collection currencies: HKD, MOP, THB, KHR, JPY, PHP, IDR, SGD, MYR, VND, plus RMB, USD, AUD, CAD, EUR, GBP, SGD as Hong Kong policy currencies. **At least 16 collection currencies.** | [HKEX FY2025, note 34](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf) · [fwd.com.hk](https://www.fwd.com.hk/en/support/premiums-payments/) |
| Top 3 Markets by Revenue (TWPI) | **1. Hong Kong & Macau US$2,903m · 2. Thailand & Cambodia US$2,621m · 3. Japan US$1,232m** (Emerging Markets US$1,027m). **Note how badly this diverges from the traffic ranking** — Thailand is 0.32% and Japan 0.35% of visible traffic while together generating US$3,853m of TWPI, because their domains were not in the supplied sample. | [HKEX FY2025, note 5.5](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf) |
| Billing channel split (web vs app store) | **Not applicable — and checked deliberately.** FWD bills insurance premium through bank rails, mandates, wallets, agents and branches. There is no Apple/Google in-app-purchase billing. The subscription reference §4 app-store trap does not apply, and this account is not at risk from it. | Sections 4 and 6 |
| Other operating metrics | Operating profit after tax US$499m (+5%); net profit US$166m; CTE US$8.72bn (+18%); group EV US$6.85bn (+19%); solvency ratio 265%; leverage 21.3%; **91% of new business applications submitted digitally** (up from 86%); 73% e-submission rate; end-to-end STP 47% (up from 40%); digital-commerce STU 79% in Hong Kong; **complaint ratio ~0.2% of transactions each year 2022–2025**; 320+ active AI models; 99% of applications on cloud | [HKEX FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf) |

---
### Overall Research Confidence

**High** — with two specific, named exclusions.

**Traffic data was SUPPLIED**, not API-sourced and not estimated: `accounts/traffic/fwd.md`, SimilarWeb PRO, Sep 2026, captured 2026-10-09, used verbatim and cited as "SimilarWeb (supplied 2026-10-09)". **But it covers 2 of 11 FWD domains**, and that is the single largest structural limitation in this report. It distorts the country profile badly in a knowable direction: Thailand appears at 0.32% of traffic while generating US$2,621m of TWPI, and Japan at 0.35% while generating US$1,232m. Any conclusion in this report that rests on traffic share — the top-5 markets table, the China gate's position as "#2", the "high traffic outside home" ICP row — carries that caveat. The conclusions that rest on FWD's own payment pages and audited filings do not.

**Strong coverage:**
- **Section 4 (payment methods) — the strongest section, and the one the brief cared most about.** Nine of ten markets enumerated method-by-method from FWD's own payment pages, fetched and parsed out of the client-side CMS payloads. Cambodia established as having no web payment surface at all, from its own route manifest.
- **Sections 2 and 12 (entities and financials).** The 249-page HKEX FY2025 annual results announcement is a primary source and was read directly: audited principal-subsidiaries list, TWPI and renewal premiums by geography, premium cash received, APE by distribution channel, customer and distribution counts, the Hong Kong offshore-VNB split.
- **Section 5 (complaints).** 310 Apple App Store reviews across 8 storefronts, pulled from the public RSS feeds with per-review ratings, dates and app versions. Far better than the thin web-review coverage typical of APAC accounts.
- **Sections 6 and 7 (developments and payment news).** FWD's own newsroom payload, parsed for dated press releases, plus the Thailand mPAY removal notice read off the live site.
- **Section 3B (orchestrator classification).** Positive evidence of fragmentation, not merely absence of evidence.

**Limited coverage, and why:**
- **Singapore premium collection.** `help.fwd.com.sg` returns HTTP 403 behind a Cloudflare challenge in **both** WebFetch and curl. Per the environment protocol I did not retry and did not route around it. SG methods are labelled `[UNVERIFIED — search summary only, page not fetched]`.
- **Section 8 (checkout audit) is partial by nature,** not by environment: the payment step genuinely sits behind authenticated policy-servicing logins (`eservices.fwd.com.hk` 403) or inside the FWD Omne mobile app in eight of ten markets. This is a property of FWD's architecture, not a gap in the research.
- **PSP identity in eight of ten markets.** Stated as "not established" rather than guessed. The two that could be named — iPay88 and AyoConnect — were named by FWD itself.
- **The IPO prospectus could not be retrieved** (English variant 404s, HKEX title-search API 403). This is the biggest single remaining gap, because a prospectus would likely carry policy counts, premium-frequency mix and collection-channel detail — which would convert the monthly transaction count from ASSUMED to DERIVED.
- **Hong Kong Insurance Authority per-insurer statistics: HTTP 403 in both tools.** Not used as a derivation input.

**No confidence downgrade applied for fetch access** — WebFetch and curl both worked against FWD's own domains and HKEX, and the two 403s (Cloudflare on `help.fwd.com.sg`, Akamai on `ia.org.hk` / HKEX search) are site-specific bot protection rather than an egress-proxy block. Both are disclosed above rather than papered over.

**Trap discipline applied.** `grep -P` was never used. All assets were fetched fresh in this session (scratchpad verified empty of prior-run material; mtimes checked). Client-side-rendered pages were parsed out of `__NEXT_DATA__` rather than from stripped HTML, because a plain text extraction of `fwd.com.hk/en/support/premiums-payments/` returns only the page title — a naive extraction would have reported "no payment methods found" on the single most important page in the report. Every vendor-name substring hit was context-checked before reporting: `omise` → *LifePromise*, `payu` → *payudara*, `stripe` → Chakra `hasStripe`, `doku` → *dokumen*, `bri` → Chakra `brightness` (with one genuine `bankCode==="BRI"`), and the Indonesian GoPay hit → a marketing **voucher**, not a payment rail. Five false vendor attributions avoided.

---

### Manual Research Recommendations

> **Area:** **Monthly transaction count — the only ASSUMED figure in the report.**
> **Why it matters:** It is the single ICP signal that can reject an account, it drives every business-case number, and it is currently an assumption resting on sourced premium totals rather than a measurement.
> **Suggested manual action:** Ask on the first call: *how many premium collection events do you process a month, group-wide, and what's the split between annual, semi-annual, quarterly and monthly billing modes?* If a document is preferred, the **IPO prospectus** is the likely source and could not be retrieved here — the Chinese version is at `hkexnews.hk/listedco/listconews/sehk/2025/0626/2025062600018_c.pdf`; locate the English listing document via the HKEX website's own search UI (its API is bot-blocked).

> **Area:** Singapore premium-payment methods.
> **Why it matters:** Singapore is the #3 traffic market at 8.95%, the fastest-growing domain in the batch is weighted to it, FWD Singapore uniquely holds a **life *and general*** licence, and it is the only market whose collection methods I could not verify from a fetched page.
> **Suggested manual action:** Open `help.fwd.com.sg/hc/en-us/sections/4409128406937-Payment-methods` in a normal browser — it blocks automated fetches but will load for a person. Confirm whether PayNow is accepted for premium *collection* or only for *payouts*; a July 2026 FWD notice confirms the payout use, and the two are being conflated in search results.

> **Area:** Hong Kong — the absence of a card checkout.
> **Why it matters:** It is Insight #2 and the second-strongest hook in the report. It rests on the published page, but the actual eServices payment step is behind a login I could not reach.
> **Suggested manual action:** Get a Hong Kong policyholder — or FWD themselves, in the meeting — to walk the eServices "My Policy → Policy Payment" step. Confirm there is genuinely no card option, and that Octopus, AlipayHK and WeChat Pay HK are genuinely absent. Also capture the acquirer behind "Pay with FPS" while you are in there.

> **Area:** The orchestration-addressable share of premium.
> **Why it matters:** FWD collects US$12.9bn of premium cash a year and **most of it is not orchestration-addressable** — bancassurance and brokerage/IFA are 74% of APE and bank partners often own the mandate. Overstating this is the fastest way to lose credibility on this account.
> **Suggested manual action:** Ask directly: *for your bancassurance book, who holds the direct-debit mandate — FWD or the bank?* And: *what share of renewal premium is collected through FWD's own portals and the Omne app, versus through a bank partner or an agent?* Those two answers size the deal.

> **Area:** Japan renewal failure rates.
> **Why it matters:** Japan is US$1,112m of renewal premium against only US$114m of first-year premium — almost purely a renewal book — and FWD's documented recovery path is postal. This is the strongest insight in the report and it currently has a mechanism but no magnitude.
> **Suggested manual action:** Ask what share of Japanese recurring charges fail on first presentment, how many end in a posted 払込取扱票, and what share of those recover before lapse. Do not assert a number; earn it. The subscription reference §5 has the full discovery set.

> **Area:** Entity registration numbers, and which entity would hold the relationship.
> **Why it matters:** Needed for contracting. FWD Group Management Holdings Limited owns the Omne app, while FWD Life Insurance Company (Bermuda) Limited is the merchant of record on the Hong Kong bill-payment and PPS rails, and FWD Financial Limited operates the HK premium-payment page as a licensed agent. Those are three different entities.
> **Suggested manual action:** Hong Kong Companies Registry, Singapore ACRA/BizFile, Malaysia SSM, Philippine SEC — one lookup each. Then ask FWD which entity would sign.

> **Area:** Great Eastern — missing from the target account list.
> **Why it matters:** A top-tier Singapore/Malaysia/Indonesia life insurer with direct FWD market overlap, absent from `accounts/apac-tal.csv`. Sun Life Asia (HK, PH, ID, VN, MY) is also absent.
> **Suggested manual action:** Add both to the TAL and queue Great Eastern for research. Also worth noting: MSIG and Singlife are already on the list and now have **confirmed 2C2P gateway relationships with no orchestration layer** — two warm, well-evidenced greenfield prospects in the same vertical.

---

### Appendix: All Source URLs

**Primary filings and corporate**
- HKEX FY2025 annual results, FWD Group Holdings Limited, stock code 1828 (249 pp, published 16 Mar 2026): https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0316/2026031600101.pdf
- FWD Group newsroom (press-release index): https://www.fwd.com/en/newsroom/
- H1 2026 record results, 26 Aug 2026: https://www.fwd.com/en/newsroom/press-releases/FWD-Group-reports-record-profit-amid-continued-growth
- 2026 interim report published, 11 Sep 2026: https://www.fwd.com/en/newsroom/press-releases/FWD-Group-publishes-2026-interim-report
- Q1 2026 new business update, 30 Apr 2026: https://www.fwd.com/en/newsroom/press-releases/FWD-Group-reports-strong-first-quarter-new-business-update-adding-to-its-consistent-track-record-of-financial-performance
- Mark Bensman appointed Chief Officer, FWD HNW, 18 May 2026: https://www.fwd.com/en/newsroom/press-releases/FWD-Group-makes-key-hire-for-its-high-net-worth-business-Mark-Bensman-to-join-as-Chief-Officer-FWD-High-Net-Worth
- Jeffrey Woo appointed President Director, FWD Indonesia, 2 Jun 2026: https://www.fwd.com/en/newsroom/press-releases/FWD-Group-appoints-Jeffrey-Woo-as-President-Director-of-FWD-Indonesia
- Martin Zingg appointed to the Board, 29 May 2026: https://www.fwd.com/en/newsroom/press-releases/FWD-Group-appoints-Martin-Zingg-to-Board-of-Directors
- 13th anniversary charitable grants, 14 Aug 2026: https://www.fwd.com/en/newsroom/press-releases/FWD-Group-marks-13-years-with-charitable-grants-benefitting-over-13,000-people-across-Asia
- ACN Newswire mirror of the FY2025 release, 16 Mar 2026: https://www.acnnewswire.com/press-release/english/105622/
- IPO prospectus, Chinese version (English variant not retrievable; 26 Jun 2025): https://www.hkexnews.hk/listedco/listconews/sehk/2025/0626/2025062600018_c.pdf

**FWD market domains (country selector source)**
- Group site, country_link_list payload: https://www.fwd.com/en/
- Hong Kong: https://www.fwd.com.hk/ · Macau: https://www.fwd.com.mo/ · Thailand: https://www.fwd.co.th/ · Cambodia: https://www.fwd.com.kh/ · Japan: https://www.fwdlife.co.jp/ · Philippines: https://www.fwd.com.ph/ · Indonesia: https://www.fwd.co.id/ · Singapore: https://www.fwd.com.sg/ · Vietnam: https://www.fwd.com.vn/ · Malaysia: https://www.fwd.com.my/ · China representative office: https://www.fwd.cn/ · Bermuda/HNW: https://www.fwdprivate.com.hk/

**Premium payment pages (Section 4 — the core sources)**
- Hong Kong: https://www.fwd.com.hk/en/support/premiums-payments/ (and the redirecting https://www.fwd.com.hk/en/support/premium-payment/)
- Macau: https://www.fwd.com.mo/en/support-claims/premium-payment/
- Thailand: https://www.fwd.co.th/en/support/premium-payment/ · card failure: https://www.fwd.co.th/en/support/premium-payment/cc/ · savings-account failure: https://www.fwd.co.th/en/support/premium-payment/dd/
- Japan: https://www.fwdlife.co.jp/support/procedure/payment/ · https://www.fwdlife.co.jp/support/cashless-payment/ · https://www.fwdlife.co.jp/support/credit_payment/
- Philippines: https://www.fwd.com.ph/support/premium-payment/ · portal: https://payment.fwd.com.ph/
- Indonesia: https://www.fwd.co.id/en/support/premium-payment/ · portal: https://www.fwd.co.id/FWDPayPortal/login · portal bundle: https://www.fwd.co.id/FWDPayPortal/assets/index-Bg68bk3R.js
- Malaysia: https://www.fwd.com.my/support/payments/
- Vietnam: https://www.fwd.com.vn/en/support/premium-payment/
- Cambodia route manifest (no payment routes): https://www.fwd.com.kh/_next/static/wfkH8t8gmtnq7fFBK2Ek72/_buildManifest.js
- Singapore (403, Cloudflare — unverified): https://help.fwd.com.sg/hc/en-us/sections/4409128406937-Payment-methods
- Singapore payout update (fetched): https://www.fwd.com.sg/travel-insurance/
- Singapore advisor portal: https://www.fwd.com.sg/iSmartWeb/ · bundle: https://www.fwd.com.sg/iSmartWeb/main.635392807373b0891aa6.js

**Complaints**
- FWD Omne App Store review RSS feeds (track id 1621673678), by storefront: https://itunes.apple.com/ph/rss/customerreviews/id=1621673678/sortby=mostrecent/json · and the same path for `th`, `id`, `vn`, `my`, `jp`, `sg`, `hk`

**Careers / hiring**
- FWD Workday jobs API: https://fwd.wd3.myworkdayjobs.com/wday/cxs/fwd/FWDcareersite/jobs
- Senior Manager, Backend Technology Delivery (HK, posted 2025-09-02): https://fwd.wd3.myworkdayjobs.com/FWDcareersite/job/Hong-Kong---Taikoo-Shing-Group-Office/Senior-Manager--Backend-Technical-Lead_JR-0024009

**Competitors and vertical**
- MSIG Insurance × 2C2P: https://www.casestudies.com/company/2c2p/case-study/msig-insurance-streamlines-payments-across-20-branches-with-2c2p
- Star Health × Juspay/Hyperswitch (403, unverified): https://hyperswitch.io/case-studies/star-health-insurance
- Adyen insurance page (checked — names Clearcover, **not** Cover Genius): https://www.adyen.com/en_SG/industries/financial-services/insurance
- AIA Vietnam × DBS API claims payout (unverified): https://www.dbs.com.sg/corporate/insights/case-studies/api-based-insurance-claim-payment-solution
- FWD Singapore × DBS PayNow claims payouts, June 2018: https://hnworth.com/article/invest/insurance/fwd-insurance-launches-electronic-claims-payments-via-paynow/

**Internal (repository)**
- `accounts/traffic/fwd.md` — supplied SimilarWeb traffic, 2026-10-09
- `accounts/apac-tal.csv` — target account list (lead data, unverified)
- `1-to-outreach/fwd.md` — stub and Prateek's starting hypotheses
- `.claude/reference/apac-payments.md` · `.claude/reference/subscription-payments.md` — checklists, **not sources**

**Not accessible in this environment (disclosed, not worked around)**
- `help.fwd.com.sg` — HTTP 403, Cloudflare challenge, in both WebFetch and curl
- `www.ia.org.hk` per-insurer statistics tables (L5–L11, 2024 and 2025) — HTTP 403 in both tools
- `www1.hkexnews.hk/search/titlesearchservlet` — HTTP 403, Akamai bot protection
- English-language IPO prospectus — HTTP 404 at every URL pattern tried
- `eservices.fwd.com.hk` — HTTP 403, authenticated portal

</details>
