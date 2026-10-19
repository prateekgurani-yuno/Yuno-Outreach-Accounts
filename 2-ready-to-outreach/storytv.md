# StoryTV

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 11 / 29 → 🟢 Medium
**Industry:** Video & music streaming — Indian vertical micro-drama subscription app (part of the Eloelo Group) · **HQ:** **Bengaluru, India** — `Greenhorn Wellness Private Limited`, CIN `U92490KA2020PTC132881` · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **Greenfield** — one direct PSP (Cashfree) for UPI Autopay, alongside Google Play Billing and Apple IAP. **The target list's `Juspay` value was not confirmed** (see below).

---

> ## 🔀 THE MOTION — the TAL said Juspay. The evidence says Cashfree, direct.
>
> `accounts/apac-tal.csv` carries `Payment Orchestrator = Juspay` for Greenhorn Wellness. **No source supports it.**
> What the evidence does show:
>
> - **Cashfree published a case study on Story TV** — *"From Signup to Renewal: How Cashfree Powers Story TV's
>   Subscription Growth at Scale"*, dated 5 Mar 2026, product listed as **Payment Gateway**, with a quote from
>   **Raunak Gupta, Product Manager, Story TV**. It says *"Story TV relies on UPI Autopay mandates to power
>   renewals"* and credits Cashfree's own *"dynamic routing for faster mandate authorization"* and smart retries.
>   [Cashfree](https://www.cashfree.com/case-study/from-signup-to-renewal-how-cashfree-powers-story-tv-s-subscription-growth-at-scale/) — fetched and read 2026-10-19.
> - A user complaint quotes the collecting VPA as **`storytv.cfp@cashfreensdlpb`**, which is a Cashfree handle on NSDL
>   Payments Bank. That is user-submitted, but it matches the case study. [Voxya](https://voxya.com/consumer-complaints/fraudulent-autopay-subscription-deduction-without-consent-by-story-tv-/268221)
> - Searches pairing Juspay with Story TV, Greenhorn or Eloelo returned nothing. Story TV's web bundle contains
>   no PSP or orchestrator token, but there is **no web checkout** to inspect, so that absence says little.
>
> ⚠️ **This refutes Juspay on balance; it does not prove Juspay is absent.** The Android APK, the one artefact that would
> settle it, **was not inspected**: the apkpure mirror returned 403 and other mirrors were blocked in this session. Agent 5 also
> found the TAL's `Juspay` value on **nearly every Indian OTT row** (Kuku FM, STAGE, Flick, Hoichoi, aha, SonyLIV,
> ZEE5), with `Payment Gateway` blank on all of them. Kuku FM's own FAQ says Razorpay. **That column looks bulk-filled — don't trust it.**

> ## 🎯 THE HOOK — 3.5M+ paying subscribers on one UPI Autopay rail, with no second PSP behind it
>
> - **Scale:** 3.5M+ paid subscribers, ₹699/quarter and ₹1,099/year ([The Hollywood Reporter India, 1 Jun 2026](https://www.hollywoodreporterindia.com/features/insight/indias-microdrama-boom-how-data-desire-and-aritifical-intelligence-are-reshaping-entertainment)).
>   It was India's **#1 short-drama app in Q2 2026**, the only one in the top-10 downloads, with **>50% QoQ revenue growth**
>   and nearly **3× ad spend** in H1 2026 ([MediaNews4U / Sensor Tower, 1 Aug 2026](https://www.medianews4u.com/indias-mobile-app-market-hits-record-345-million-iap-revenue-in-q2-2026-story-tv-tops-short-drama-apps-report/)).
>   The Play listing shows 10Cr+ (100M+) downloads.
> - **Rail:** their own FAQ says *"We currently offer UPI Payment Stack and Play Billing Payment Stack"*. Neither the
>   FAQ nor any review mentions cards, netbanking, e-NACH or wallets. Mandate creation is the acquisition funnel:
>   Cashfree's own words are *"lags in mandate setup or failure in the setup of mandates meant losing high intent
>   customers at the point of signup."*
> - **Single point of failure:** every direct renewal for a 3.5M-subscriber base runs through one gateway's UPI switch.
>   We found no second PSP and no failover.
> - **The timing trigger:** NPCI is reported to be making UPI Autopay **interoperable**: *"merchants switching payment gateways
>   or acquiring banks would be able to move existing mandates to the new provider without requiring customers to
>   register again"* ([Inc42, 31 Aug 2026](https://inc42.com/buzz/npci-to-let-users-port-upi-autopay-mandates-across-apps-report/),
>   citing Mint; expected to be announced at Global Fintech Fest). ⚠️ This is **reported and proposed, not a confirmed
>   circular.** If it lands, the lock-in that keeps a mandate merchant on one gateway goes away, and multi-PSP mandate
>   routing becomes practical for the first time.
>
> ⚠️ **The honest counterweight, and it is substantial.** This is a **~98%-India, UPI-first** merchant. Cross-border,
> APM breadth and multi-market acquiring — Yuno's usual pitch — barely apply. The opportunity is **domestic UPI
> Autopay redundancy and mandate routing**. **Before any outreach, confirm that Yuno can actually serve Indian UPI
> Autopay mandates through Indian PA partners.** If it can't, this account has no pitch.

> ## ⚠️ THE COMPLAINT PATTERN — read this before using it
>
> Complaints are **high-volume and rising**. Agent 4 scraped 2,000 Play reviews from India: **988 (49%) mention payments**,
> and monthly payment complaints went from 1–2 a month to **91 in Apr, 218 in May, 173 in Jun, 174 in Jul and 200 in Aug 2026**,
> in step with the ad-spend ramp. The iOS rating is **2.3★** against Play's 4.4★.
> **Most of these complaints are about consent and cancellation** (a ₹1 trial auto-converting to ₹399–699, no in-app
> cancel, refunds refused), **not infrastructure failure.** Do **not** pitch these as payment-rail failures, and never
> pitch "your users say you scam them". The infrastructure-adjacent minority is real but small: **double debits
> (~26)**, **paid-but-not-activated** accounts, and charges landing minutes after the ₹1 payment. Those point to problems with
> mandate execution or entitlement sync.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Story TV is an Indian vertical micro-drama app (1–2 minute episodes) launched mid-2025 by the Eloelo
Group, which operates through `Greenhorn Wellness Private Limited`, Bengaluru, alongside the Eloelo live-social
app and the Master micro-learning app. It monetises through a ₹1 paid trial that auto-converts to a quarterly (84-day)
plan. Billing runs on UPI Autopay mandates via Cashfree, with Google Play Billing and Apple IAP alongside.

**SimilarWeb total visits (last full month):** ~5.1 million avg/month (Jul–Sep 2026; 15.29M over 3 months) — source: **supplied** (`accounts/traffic/storytv.md`, pulled 2026-10-19). ⚠️ The website is a landing and legal-pages shell with no checkout, and the traffic is 99.56% mobile web. **App traffic is not counted**, so web visits say nothing about transaction volume.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇮🇳 India | 98.25% | UPI Autopay (Cashfree), Google Play Billing, Apple IAP | Cards / RuPay, netbanking / e-NACH, wallets: not offered per own FAQ ("UPI Payment Stack and Play Billing Payment Stack") | ✅ Greenhorn Wellness Pvt Ltd |
| 2 | 🇺🇸 United States | 1.38% | Google Play Billing only ($4.49–$9.99 per item); **not on the US App Store** | Any direct billing (cards, Apple Pay, PayPal) | ❌ |
| 3 | 🇸🇬 Singapore | 0.10% | Not found | Not assessed (<1%) | ❌ |
| 4 | 🇫🇷 France | 0.07% | Not found | Not assessed (<1%) | ❌ |
| 5 | 🇨🇦 Canada | 0.06% | Not found | Not assessed (<1%) | ❌ |

### Legal entities
- **Greenhorn Wellness Private Limited** (India) — CIN `U92490KA2020PTC132881`, incorporated 20 Feb 2020, ROC Bangalore. Directors: Saurabh Pandey and Akshay Kumar Dubey.
- No foreign subsidiary found.

### Known PSPs
- **Cashfree Payments** — [Provider Case Study] + [Third-Party Report] (VPA in a user complaint) — India, UPI Autopay
- **Google Play Billing** — [Terms/Privacy Policy] (own FAQ) — India and US Android. App-store billing, not a PSP.
- **Apple IAP** — [Third-Party Report] (App Store listing: ₹599 / ₹699 quarterly, ₹1,099 annual) — India iOS. App-store billing, not a PSP.

### Orchestration status
**None detected — direct PSP integrations only.** Cashfree is named in its own case study and in a collecting VPA.
Juspay (from the TAL) was not confirmed by any source. The APK was not inspected — see the motion box.

### Buying signals
- 🚀 Q2 2026: India's #1 short-drama app, >50% QoQ revenue growth, ~3× ad spend in H1 ([MediaNews4U / Sensor Tower](https://www.medianews4u.com/indias-mobile-app-market-hits-record-345-million-iap-revenue-in-q2-2026-story-tv-tops-short-drama-apps-report/))
- 🔁 NPCI reported to be making UPI Autopay mandates portable between gateways ([Inc42, 31 Aug 2026](https://inc42.com/buzz/npci-to-let-users-port-upi-autopay-mandates-across-apps-report/)). Reported, not confirmed.
- 💰 Eloelo is reportedly targeting a ~$50M raise ([StartupWired, 31 Mar 2026](https://startupwired.com/2026/03/31/eloelo-targets-50m-as-micro-drama-market-explodes-now/)) `[UNVERIFIED — search summary only]`. The last confirmed round is the **$13.5M Series B in Apr 2025** ([Entrepreneur India](https://india.entrepreneur.com/news-and-trends/eloelo-raises-usd-135-mn-series-b-led-by-play-ventures-to/489831)).
- 💼 Nikunj Mundhra joined as VP Revenue & Growth (monetisation and retention), May 2026 ([MediaNews4U](https://www.medianews4u.com/nikunj-mundhra-joins-eloelo-group-as-vp-revenue-growth/)) `[UNVERIFIED — search summary only]`
- 🤝 Content deals with Balaji Telefilms (Oct 2025), Zee (Feb 2026) and Applause Entertainment (Mar 2026). Signals scale, not payments.

**Contacts surfaced:** Saurabh Pandey (Co-founder & CEO, Eloelo Group) · Akshay Kumar Dubey (Co-founder, director) · **Raunak Gupta (Product Manager, Story TV — the quoted owner of the Cashfree integration)** · Sagar Gaonkar (CTO, per [Caplight](https://www.caplight.com/company/greenhornwellness), unconfirmed) · Nikunj Mundhra (VP Revenue & Growth).

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach StoryTV` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

⚠️ **Constraints for whoever drafts this:**
- **Greenfield, but not naive.** They run a vendor-built UPI switch with its own "dynamic routing" and smart retries. Don't argue that they lack retries. Argue that **one gateway means one point of failure** for mandate creation and execution.
- **Never name Cashfree** in outreach. Say "your mandate gateway".
- **Never imply the consent complaints are payment-infrastructure failures**, and never quote "scam" reviews at them.
- **Do not lead with cross-border or APM breadth.** At ~98% India, it doesn't apply.
- **The NPCI portability point is reported, not confirmed.** Phrase it as "if mandate portability lands as reported" until there is an NPCI circular.
- **Confirm Yuno's India UPI Autopay capability first** (see Manual Research Recommendations).

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 11 / 29
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | **+5** | ✅ **DERIVED: ≥~290,000/month (floor), likely ~1.0–1.3M.** 3.5M+ paid subscribers ([THR India, 1 Jun 2026](https://www.hollywoodreporterindia.com/features/insight/indias-microdrama-boom-how-data-desire-and-aritifical-intelligence-are-reshaping-entertainment)) ÷ the billing cadence defined in their own T&Cs (Quarterly = **84 days**, Annual = **360 days**; [storytv.asia/tnc](https://storytv.asia/tnc)). Floor, as if everyone were annual: 3.5M ÷ 12 ≈ **292k/month**. If everyone were quarterly: 3.5M × 30.4/84 ≈ **1.27M/month**. Both inputs are sourced. **Billing unit:** subscription charges (₹1 trial charges and renewals), across UPI Autopay, Play and IAP combined. ⚠️ The App Store and Play share sits outside the addressable count, but even a 50% store share leaves the floor above 100k. ⚠️ The subscriber figure is a press number from 1 Jun 2026, not a filing. |
| Orchestration status | **+4** | ✅ None detected — direct Cashfree integration (provider case study + VPA). Juspay from the TAL is not supported. ⚠️ APK not inspected. |
| 3+ countries | 0 | ❌ India 98.25%, US 1.38%, everything else <1%. One legal entity. |
| Multiple PSPs | 0 | ❌ One PSP confirmed (Cashfree). Play Billing and Apple IAP are app stores, not PSPs. |
| Local rail or licensing gap in a top-3 market | 0 | ❌ UPI Autopay, India's dominant recurring rail, is live. Cards and netbanking are absent per their own FAQ, but neither is the dominant rail. The US runs on Play only, but at 1.38% it doesn't qualify. |
| Recent expansion | 0 | ❌ South-Indian content push (Jul 2026) is content, not a new market. Dolphin AI "global" (Sep 2026) is a different product, and the claim comes from a search summary only. |
| Payment issues reported | **+2** | ✅ **High frequency.** 49% of 2,000 sampled Play reviews mention payments, rising sharply from Apr 2026, plus Voxya and iOS reviews. ⚠️ These are mostly consent and cancellation complaints, not rail failures. See Section 5. |
| Funding >$10M | 0 | ⬜ Series B $13.5M was Apr 2025, outside the 12-month window. A Mar 2026 "growth equity" round (Caplight) has no amount, and the $50M raise is a target. |
| High traffic outside home | 0 | ❌ Home market is 98.25%. |
| Competitor using orchestration | 0 | ⬜ Pocket FM's Juspay case study is indexed but **now returns 404** (Wayback rate-limited), so it is unverified. ZEE5's Juspay logo is a logo only. Shemaroo/Juspay is verified in this repo, but Shemaroo is an SVOD peer, not a micro-drama competitor. |
| Payment job postings | 0 | ❌ No payments roles found. The VP Revenue & Growth is a monetisation hire, not a payments hire. |

**Tier:** Medium (10–16) 🟢 → **🟢 Medium**
No public payment RFP found. **No analyst override applied, but two caveats sit right at the boundary:**
1. **App-store share:** **not an override.** The evidence points to direct UPI Autopay as the main rail: own FAQ, most complaints describe UPI debits, and Sensor Tower's store revenue estimate of ~$40K/month is tiny next to 3.5M paid subscribers (that estimate is `[UNVERIFIED — search summary only]`). The account is not app-store dominated.
2. **Regulatory and capability reality:** **potential override DOWN.** The whole pitch is domestic UPI Autopay mandate routing. If Yuno can't originate and route UPI mandates in India, through licensed PA partners, there is no product to sell here. **Resolve this before outreach.**

### Source Notes
- ✅ Legal entity, address and CIN — T&Cs/privacy pages in the site bundle; [companydetails.in](https://www.companydetails.in/company/greenhorn-wellness-private-limited); Play and App Store seller name.
- ✅ Eloelo Group ownership — same directors as Eloelo's co-founders; [Storyboard18 on the Master launch](https://storyboard18.com/digital/eloelo-group-enters-info-tainment-space-with-launch-of-micro-learning-app-master-85974.htm) says the group "currently operates live social platform Eloelo and Story TV".
- ✅ Cashfree as gateway — [Cashfree case study](https://www.cashfree.com/case-study/from-signup-to-renewal-how-cashfree-powers-story-tv-s-subscription-growth-at-scale/), read first-hand.
- ✅ 3.5M+ paid subscribers, ₹699 / ₹1,099 — THR India, read first-hand.
- ✅ #1 short-drama app in Q2 2026, >50% QoQ revenue — MediaNews4U citing Sensor Tower, read first-hand.
- ✅ NPCI mandate portability **report** — Inc42, read first-hand. The underlying policy is unconfirmed.
- ⚠️ Juspay (TAL) — not supported by any source.
- ⚠️ Download counts conflict across sources: 50M+ (Cashfree, Mar 2026; company, Feb 2026), 90M+ (THR, Jun 2026), 10Cr+/100M+ (Play listing, Oct 2026). These read as growth over time, not a contradiction.
- ⚠️ FY25 revenue of ₹69.5 Cr — aggregator page only, not a filing.
- ⚠️ Kalaari's Series B post carries a 28 Apr 2026 date, but the round is Apr 2025 per Entrepreneur and Inc42. Don't cite it as 2026 funding.

### Success Case Alternatives
- **Livelo** — decline recovery by routing failed transactions to a secondary acquirer (+5% approval, 50% of failed transactions recovered). The closest **mechanism** match to "a second rail behind your mandate gateway". It is **loyalty, LATAM, card-based — a pattern match, not a UPI case.** Say so.
- **Vibra** — first-time-buyer approval (+30pp to 80%). It maps loosely to the ₹1-trial mandate-creation funnel. Also LATAM; a pattern match only.
- **Open English** — subscription logo with no public numbers. Relevance signal only.
- **No Indian UPI Autopay or micro-drama case exists in the library.** Ask Prateek for any internal India reference before Phase 3.

---

## Executive Summary

Story TV is the Eloelo Group's micro-drama app, operated by Greenhorn Wellness Pvt Ltd (Bengaluru). It launched mid-2025 and was India's #1 short-drama app by Q2 2026, with 3.5M+ paid subscribers on ₹699 quarterly and ₹1,099 annual plans, sold through a ₹1 paid trial. The defining payment fact: **almost all direct revenue runs on UPI Autopay mandates through a single gateway, Cashfree**, confirmed by Cashfree's own case study, with Google Play Billing and Apple IAP beside it, and no cards, netbanking or second PSP visible. The opportunity is **domestic mandate redundancy and routing**. If NPCI's reported mandate portability lands, that becomes switchable rather than locked in. Motion: **Greenfield**. The TAL's Juspay value is unsupported.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** **Supplied SimilarWeb data** — `accounts/traffic/storytv.md`, Similarweb Sales Intelligence, pulled 2026-10-19, period Jul–Sep 2026, domain `storytv.asia` only, desktop + mobile web.

**Caveats carried over from the traffic file:**
1. Sales Intelligence view: shares only, top 10 countries. Per-country visits below are **[DERIVED from supplied share, not a SimilarWeb figure]** = share × 5.099M average monthly visits.
2. Single domain. No regional variants found (`storytv.asia` is the only web property; there is no web checkout on it).
3. **Mobile app traffic is not included.** This is an app-first business, so app sessions, where all purchases happen, are invisible here.
4. **Web traffic must not be used to size transactions.** The country split is a market-mix signal only. The Phase-0 volume gate was sized from subscriber data instead (Section 12).

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | India | 98.25% | ~5.01M [DERIVED] | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | United States | 1.38% | ~70K [DERIVED] | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 3 | Singapore | 0.10% | ~5K [DERIVED] | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 4 | France | 0.07% | ~3.6K [DERIVED] | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 5 | Canada | 0.06% | ~3.1K [DERIVED] | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 6 | Pakistan | 0.03% | ~1.5K [DERIVED] | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 7 | Qatar | 0.02% | ~1K [DERIVED] | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 8 | Germany | 0.02% | ~1K [DERIVED] | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 9 | Norway | 0.01% | ~0.5K [DERIVED] | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 10 | Australia | 0.01% | ~0.5K [DERIVED] | Not supplied | SimilarWeb (supplied 2026-10-19) |

- Total visits: 15.29M over 3 months, 5.099M monthly average. Device split: desktop 0.44%, mobile web 99.56%. Global rank: not captured.
- **High priority (>5%):** India only.
- **Top-10 markets with no local entity:** every market except India. All are below 1.5%, and the US is the only one above 1%.
- Interpretation: 99.56% mobile web on a site with no checkout most likely reflects ad-landing and deep-link traffic into the app stores, plus the in-app legal pages (the bundle has separate `/mtnc`, `/mprivacy` and `/mrefund` routes flagged `isInAppBrowser`). `[INFERENCE, not confirmed]`

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Bengaluru, Karnataka, India. Entity incorporated 20 Feb 2020. Story TV launched mid-2025: Play release 24 Jun 2025, iOS release 30 Aug 2025.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| India | Greenhorn Wellness Private Limited | CIN U92490KA2020PTC132881 (ROC Bangalore, Active; authorised capital ₹5,00,000, paid-up ₹3,34,920; directors Akshay Kumar Dubey DIN 08706080, Saurabh Pandey DIN 08706081) | [companydetails.in](https://www.companydetails.in/company/greenhorn-wellness-private-limited); T&Cs in the [site bundle](https://storytv.asia/tnc) |

- **Registered office per their T&Cs and privacy policy:** 1257/37, 2nd & 3rd Floor, Hanto Orion Center, 14th Main St, Sector-7, HSR Layout, Bengaluru 560102. The MCA snapshot shows an older BHIVE HSR Sector 6 address, so the snapshot may be stale.
- **Governing law:** India; exclusive jurisdiction of the courts in Bengaluru (T&Cs).
- **Group context:** Greenhorn Wellness is the legal entity behind the **Eloelo Group**, which also runs **Eloelo** (live social and gaming) and **Master** (micro-learning, launched 16 Dec 2025; [Storyboard18](https://storyboard18.com/digital/eloelo-group-enters-info-tainment-space-with-launch-of-micro-learning-app-master-85974.htm)). The T&Cs also mention a "Story Max App" that may carry the same content. No other source mentions Story Max, and its ownership is unconfirmed.
- **Foreign entities:** No public information found. The Apr 2025 Series B stated an intent to expand into "Indian diaspora markets" ([Entrepreneur India](https://india.entrepreneur.com/news-and-trends/eloelo-raises-usd-135-mn-series-b-led-by-play-ventures-to/489831)). That is a plan, not evidence of a live operation.

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| India | ✅ #1 (98.25%) | ✅ | N/A — local entity present | None |
| United States | ✅ #2 (1.38%) | ❌ | Not assessed | Low. Monetised via Google Play Billing only, and **not listed on the US App Store** (iTunes lookup returns 0 results; apps.apple.com/us returns 404). No direct billing to cross-border. |
| Singapore, France, Canada, Pakistan, Qatar, Germany, Norway, Australia | ✅ #3–#10 (all ≤0.10%) | ❌ | Not assessed | Immaterial at these shares |

> No top-5 market triggers the cross-border warning in a way that matters commercially. The US is ~1.4% of web traffic and earns only through Google Play.

> **MANUAL:** The billing entity is already confirmed in the T&Cs. The refund policy says *"Please contact us if you would like to know the name and address of the third-party payment service provider"*, so the PSP is withheld on purpose. Don't expect it in their legal pages.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| India | **Cashfree Payments** — Payment Gateway; UPI Autopay mandate creation and execution; Cashfree's in-house UPI switch, "dynamic routing for faster mandate authorization", pre-debit notifications with "up to 6 retry attempts", smart retries, mandate webhooks | [Provider Case Study] (dated 5 Mar 2026) | https://www.cashfree.com/case-study/from-signup-to-renewal-how-cashfree-powers-story-tv-s-subscription-growth-at-scale/ |
| India | Cashfree — collecting VPA `storytv.cfp@cashfreensdlpb` (NSDL Payments Bank sponsor) | [Third-Party Report] — user complaint, unverified | https://voxya.com/consumer-complaints/fraudulent-autopay-subscription-deduction-without-consent-by-story-tv-/268221 |
| India (Android), US (Android) | Google Play Billing (store billing, not a PSP). Play shows ₹10–₹999 per item (IN) and $4.49–$9.99 (US). | [Terms/Privacy Policy] — own FAQ: "UPI Payment Stack and Play Billing Payment Stack" | https://storytv.asia/faq-2 ; https://play.google.com/store/apps/details?id=story.tv.drama.reels&hl=en_IN |
| India (iOS) | Apple IAP (store billing, not a PSP). Premium Plan (3 months) ₹599 / ₹699, Premium Plan (12 months) ₹1,099 | [Third-Party Report] — App Store listing | https://apps.apple.com/in/app/id6746484263 |
| India | Paytm UPI, BHIM, PhonePe, Google Pay — **UPI apps where users approve mandates, not PSPs**. Paytm and BHIM run co-marketed cashback offers that require setting up an Autopay mandate. | [Source Code] (site bundle `/paytmcashback`, `/bhimcashback`) + user reviews | https://storytv.asia/paytmcashback ; https://storytv.asia/bhimcashback |
| — | Razorpay, PayU, Juspay, Setu, Decentro, BillDesk, Easebuzz, Stripe | Searched — **Not found** | — |

**Single-PSP dependency:** ✅ confirmed as far as the public record goes. One gateway carries every direct UPI Autopay mandate.

#### 3B. Payment Orchestrator

**Classification: None detected — direct PSP integrations only.**

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with
> PSP(s), which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

- Evidence: the Cashfree [Provider Case Study] describes a direct gateway relationship, and the "dynamic routing" in it is a Cashfree feature, not a merchant-side layer. The VPA sits directly on a Cashfree handle.
- **TAL `Payment Orchestrator = Juspay`: not confirmed.** Three search angles (Story TV, Greenhorn, Eloelo with Juspay) returned nothing. Agent 5 notes the TAL carries Juspay on nearly every Indian OTT row with a blank gateway column, so the value looks bulk-filled.
- Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, Yuno: not found.

> **MANUAL:** Pull the Android APK (`story.tv.drama.reels`) and grep the dex files for `in.juspay`, `hypersdk`, `com.cashfree`, `com.razorpay`, `com.phonepe` and `com.android.billingclient`. That one check settles the Juspay question. It was blocked in this session.

---

### Section 4: Alternative & Local Payment Methods

Only India and the US are above 1% traffic share.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| India | UPI Autopay (recurring mandate) | Direct debit / mandate | **Active in checkout** (in-app) | [Cashfree](https://www.cashfree.com/case-study/from-signup-to-renewal-how-cashfree-powers-story-tv-s-subscription-growth-at-scale/); [own FAQ](https://storytv.asia/faq-2); many Play reviews |
| India | UPI via Paytm, BHIM, PhonePe, Google Pay apps | Bank transfer / A2A (UPI) | **Active in checkout** (as mandate approval apps) | [/paytmcashback](https://storytv.asia/paytmcashback), [/bhimcashback](https://storytv.asia/bhimcashback); [App Store reviews](https://apps.apple.com/in/app/id6746484263) |
| India | Google Play Billing | Store billing | **Mentioned in docs** (own FAQ) | [own FAQ](https://storytv.asia/faq-2) |
| India | Apple IAP | Store billing | **Active** (IAP list on the App Store) | [App Store](https://apps.apple.com/in/app/id6746484263) |
| India | Cards (Visa / MC / RuPay) | Cards | **Not found** — the FAQ lists only UPI and Play Billing as the stacks offered | [own FAQ](https://storytv.asia/faq-2) |
| India | Netbanking / e-NACH | Bank transfer / mandate | Not found | — |
| India | Wallets (Paytm wallet, Amazon Pay, etc.) | Digital wallet | Not found | — |
| India | EMI / BNPL | BNPL / Instalments | Not found (not relevant at ₹699 ticket size) | — |
| India | Carrier billing | Carrier billing | Not found | — |
| India | Coins / per-episode unlocks | Monetisation model | **Not found.** Every iOS IAP SKU is a Premium Plan subscription. The TAL's "buy coins in-app" description looks wrong. | [App Store](https://apps.apple.com/in/app/id6746484263) |
| US | Google Play Billing ($4.49–$9.99 per item) | Store billing | Active (Play US storefront) | https://play.google.com/store/apps/details?id=story.tv.drama.reels&hl=en_US&gl=US |
| US | Apple IAP | Store billing | **Not available** — not on the US App Store | iTunes lookup, US storefront: 0 results |
| US | Cards, Apple Pay, PayPal (direct) | Cards / wallet | Not found (no web checkout) | — |

- **Dominant India rail (UPI, including UPI Autopay for recurring) is present.** No rail-gap warning applies to India.
- **Cards are missing for direct billing**, which matters at the margin: a subscriber without a UPI Autopay-capable bank or app has only Play or IAP left. This is commercially minor next to UPI, and we have no figure on card demand among micro-drama users. `[INFERENCE, not confirmed]`
- **Coins:** the TAL INFO column ("viewers buy coins in-app to unlock episodes") isn't supported. The model observed is subscription-only.

---

### Section 5: Payment Issues & Customer Complaints

Agent 4 scraped 2,000 English-language Play reviews from India ("Most relevant" sort, dated 28 Oct 2025 – 19 Sep 2026). **988 (49%) mention payments; 1,049 are 1–2★.** Payment complaints by month: 1–2 a month until Feb 2026, then 8 (Mar), **91 (Apr), 218 (May), 173 (Jun), 174 (Jul), 200 (Aug)**, and 118 (Sep, partial). iOS: **2.3★ from ~1.7k ratings**, against Play's 4.4★.

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| ₹1 trial auto-converts to ₹399–₹699 (consent / dark pattern) | Google Play, App Store, Voxya | **High** (~622 of 2,000 Play reviews) | Mar–Oct 2026 | https://play.google.com/store/apps/details?id=story.tv.drama.reels&hl=en_IN ; https://apps.apple.com/in/app/id6746484263 |
| No in-app cancel; mandate must be revoked in the UPI app | Google Play, App Store | Moderate (~98) | Dec 2025 onward | same |
| Refund refused under the "non-refundable" policy | Google Play, Voxya | **High** (~608 mention refunds) | Jan–Oct 2026 | Play listing; e.g. https://voxya.com/consumer-complaints/-unauthorized-599-autopay-deduction-and-refund-refusal-by-story-tv-app-/259623 |
| **Duplicate charges** | Google Play | Low–moderate (~26) | Aug–Sep 2026 | Play listing ("₹599 was deducted from my account twice", 27 Aug 2026) |
| **Paid but subscription not activated / shows expired** | Google Play | Isolated (~5), but highly upvoted | Oct 2025 – Jun 2026 | Play listing ("charged ₹599 within just 10 minutes of paying ₹1… my subscription is still not active", 610 helpful votes) |
| Wrong entitlement period (paid for 3 months, got 1) | Google Play | Isolated | Feb 2026 | Play listing |
| ₹1 payment shown as "failed", then a ₹300 charge requested | Google Play | Isolated | Jun 2026 | Play listing |
| Repeated failed debit attempts on low balance ("3-4 fail attempts each day") | App Store / Play | Isolated | 2026 | Play / App Store listings |
| Voxya consumer complaints (unauthorised autopay, refunds), ~16 dated items | Voxya | Moderate | 17 Jan – 12 Jul 2026 | e.g. https://voxya.com/consumer-complaints/-autopay-unwanted-subscription-/257355 , https://voxya.com/consumer-complaints/story-tv-unauthorized-autopay-deduction/262355 , https://voxya.com/consumer-complaints/the-payment-of-the-subscription-has-been-deducted-before-the-end-of-trial-period/270139 `[titles from search results; pages not all opened]` |
| Reddit, X, Trustpilot | — | None surfaced | — | — |

**Caveats:** many Play reviews follow one near-identical copy-paste template, which inflates the raw count, though each comes from a separate account. Developer replies are boilerplate ("all charges are processed only after user authorization…"). Keyword counts overlap.

> *Pattern: the dominant pattern is a consent and cancellation problem in the trial-to-paid funnel, which is a product and
> regulatory issue, **not** something orchestration fixes.* The infrastructure-adjacent minority (**double debits,
> paid-but-not-activated, wrong entitlement period**) suggests mandate-execution and webhook/entitlement sync problems
> on a single-gateway integration. A unified transaction and mandate-state layer plus a second rail addresses those
> directly. `[INFERENCE, not confirmed]`

Regulatory context (not applied to Story TV): India's CCPA dark-pattern guidelines define a "subscription trap", and the regulator has acted against other platforms ([Outlook Business](https://www.outlookbusiness.com/news/inside-indias-dark-pattern-crackdown-why-zepto-bookmyshow-and-others-are-under-ccpa-scanner)) `[UNVERIFIED — search summary only]`. **No action against Story TV found.**

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 1 Aug 2026 | Sensor Tower: Story TV was India's #1 short-drama app and the only one in the top-10 downloads in Q2 2026 (3rd non-gaming app after ChatGPT and JioHotstar); >50% QoQ revenue growth; ~3× digital ad spend in H1 2026 | Market Expansion (scale) | https://www.medianews4u.com/indias-mobile-app-market-hits-record-345-million-iap-revenue-in-q2-2026-story-tv-tops-short-drama-apps-report/ |
| 2 | 28 Jul 2026 | Plan for 1,000+ Telugu, Tamil, Kannada and Malayalam originals by Mar 2027 `[UNVERIFIED — search summary only]` | Market Expansion (content / regional, domestic) | https://www.mediainfoline.com/brand/story-tv-bets-big-on-south-india-expanding-premium-vertical-storytelling-across-the-region |
| 3 | May 2026 | Nikunj Mundhra joins Eloelo Group as VP Revenue & Growth (monetisation, retention) `[UNVERIFIED — search summary only]` | Leadership Change | https://www.medianews4u.com/nikunj-mundhra-joins-eloelo-group-as-vp-revenue-growth/ |
| 4 | 31 Mar 2026 | Eloelo reportedly targets a $50M raise. Caplight lists a "Growth Equity" round dated 31 Mar 2026 with no amount. `[UNVERIFIED — search summary only]` | Funding | https://startupwired.com/2026/03/31/eloelo-targets-50m-as-micro-drama-market-explodes-now/ ; https://www.caplight.com/company/greenhornwellness |
| 5 | 16 Dec 2025 | Eloelo Group launches Master (micro-learning); claims 4M+ users in 50 days | Market Expansion (new product) | https://storyboard18.com/digital/eloelo-group-enters-info-tainment-space-with-launch-of-micro-learning-app-master-85974.htm |
| — | Apr 2025 | Series B ₹114.3 Cr (US$13.5M) led by Play Ventures, with Kalaari, MIXI, Gameskraft, Griffin, Waterbridge, Courtside, Rocket. Total raised >US$50M. Stated use: international expansion into Indian diaspora markets. | Funding (outside the 12-month window) | https://india.entrepreneur.com/news-and-trends/eloelo-raises-usd-135-mn-series-b-led-by-play-ventures-to/489831 |

- **No public payment-related RFP found.**
- **No job postings mentioning payments, PSP evaluation or orchestration found.** Eloelo hires through `eloelo.keka.com`; the only Story TV role seen was script-writing.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 31 Aug 2026 | NPCI reportedly set to make UPI Autopay interoperable: users port mandates across UPI apps, and merchants move mandates between gateways or acquiring banks "without requiring customers to register again". Expected to be announced at Global Fintech Fest. | **High.** It removes mandate lock-in to a single gateway, so multi-PSP mandate routing becomes practical. Reported, not confirmed. | https://inc42.com/buzz/npci-to-let-users-port-upi-autopay-mandates-across-apps-report/ |
| 2 | 5 Mar 2026 | Cashfree case study: "How Cashfree Powers Story TV's Subscription Growth at Scale" | Confirms the incumbent gateway and that UPI Autopay is the renewal engine | https://www.cashfree.com/case-study/from-signup-to-renewal-how-cashfree-powers-story-tv-s-subscription-growth-at-scale/ |
| 3 | Undated (site bundle, live) | Paytm UPI cashback (₹50) and BHIM cashback (₹60 on first mandate execution ≥₹90) for setting up an Autopay mandate on Story TV | UPI-app co-marketing to grow mandate adoption | https://storytv.asia/paytmcashback ; https://storytv.asia/bhimcashback |
| — | — | No provider removals found | — | — |

---

### Section 8: Checkout Experience Audit

*"Full checkout flow not accessible. Findings limited to publicly observable elements."* The website has **no checkout**; all purchases happen in the app.

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | In-app paywall; UPI Autopay mandate via Cashfree, or Play Billing / Apple IAP | Not assessed | No web checkout exists |
| Guest checkout | Login by phone number (privacy policy) | Not assessed | Account required |
| Steps to complete payment | Not observed | Not assessed | Cashfree claims fast mandate creation |
| Card input experience | No cards offered (FAQ) | N/A | — |
| Payment methods visible | UPI (Paytm, BHIM, PhonePe, GPay apps), Play Billing, Apple IAP | Fair | No card fallback |
| Location-based method display | US gets Play only; no US App Store listing | Not assessed | — |
| Instalment / EMI options | None | N/A | Not expected at ₹699 |
| 3DS implementation | N/A (no cards) | N/A | — |
| PCI indicator | No card data handled, as far as observed | N/A | — |
| Mobile responsiveness | Web is 99.56% mobile; app-first | Not assessed | — |
| Multi-currency / local pricing | INR; USD on Play US | Not assessed | — |
| Saved payment methods | Mandate-based recurring | Not assessed | — |
| Error message clarity | Reviews report a "payment failed" message followed by a charge request | Poor (anecdotal) | Isolated |

> **MANUAL:** Install the Android app on an Indian device and walk the ₹1 trial paywall. Record which UPI flow is used (intent vs collect), whether a card or Play option is offered alongside, and the mandate amount and frequency shown.

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found | — |
| Card data handling | **Not found / likely out of scope.** No card rail is offered on direct billing; UPI mandates and app stores carry no PAN. | Own FAQ |
| Recommended Yuno integration | SDK — mobile, in-app UPI mandate flows | — |

*"No direct PCI compliance documentation found publicly for Story TV."* PCI scope reduction is **not** a relevant angle here.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: Single gateway behind 3.5M+ subscriptions' renewals**
> **Evidence:** S3A — Cashfree is the only PSP found, and Story TV "relies on UPI Autopay mandates to power renewals" ([Cashfree](https://www.cashfree.com/case-study/from-signup-to-renewal-how-cashfree-powers-story-tv-s-subscription-growth-at-scale/)). S12 — 3.5M+ paid subscribers ([THR India](https://www.hollywoodreporterindia.com/features/insight/indias-microdrama-boom-how-data-desire-and-aritifical-intelligence-are-reshaping-entertainment)). S6 — >50% QoQ revenue growth ([MediaNews4U](https://www.medianews4u.com/indias-mobile-app-market-hits-record-345-million-iap-revenue-in-q2-2026-story-tv-tops-short-drama-apps-report/)).
> **Pain Point:** a gateway or sponsor-bank outage, or mandate-creation latency, hits signups (Cashfree's own words: lag "meant losing high intent customers at the point of signup") and the renewal book at the same moment. Nothing sits behind it.
> **Yuno Value Proposition:** a second mandate rail and routing for mandate creation and execution, with a single view of mandate state across providers.
> **Best Success Case:** Livelo (failed transactions recovered via a secondary acquirer). Mechanism match only; LATAM, cards. State that plainly.
> **Outreach Angle:** "When you're adding subscribers at your current pace, mandate setup is your top-of-funnel. What happens to signups the hour your one gateway's UPI switch degrades?"
> **Suggested Subject Line:** "Story TV's second mandate rail"

> **Insight #2: Mandate portability turns lock-in into a choice**
> **Evidence:** S7 — NPCI reported to let merchants "move mandates from one payment provider to another" ([Inc42, 31 Aug 2026](https://inc42.com/buzz/npci-to-let-users-port-upi-autopay-mandates-across-apps-report/)). S3B — no orchestration layer; one gateway holds the mandate base.
> **Pain Point:** today their mandate base is effectively tied to the gateway it was created on. Adding a second provider has meant new mandates only.
> **Yuno Value Proposition:** be the layer that holds multi-provider mandate routing, ready when portability lands. ⚠️ Depends on Yuno's India UPI Autopay capability, which is unconfirmed.
> **Best Success Case:** none directly. Use Rappi for provider breadth through one integration, as a pattern match.
> **Outreach Angle:** "If NPCI's mandate portability lands as reported, the mandate base stops being tied to one gateway. Worth deciding now what you'd route where."
> **Suggested Subject Line:** "UPI Autopay portability and Story TV's renewals"

> **Insight #3: Entitlement and mandate-state sync at scale**
> **Evidence:** S5 — double debits (~26 in sample), paid-but-not-activated and wrong-entitlement-period complaints, against a 49% payment-complaint rate in Play reviews. S3A — mandate webhooks from a single gateway feed entitlement.
> **Pain Point:** each mis-sync turns into a refund request or chargeback, plus a 1★ review, on an app whose iOS rating is already 2.3★.
> **Yuno Value Proposition:** unified transaction and mandate-state data across rails, including Play and IAP reconciliation in one place. `[INFERENCE, not confirmed]` that Yuno's reporting covers store billing; verify.
> **Best Success Case:** Rappi ("80% less analyst work"), pattern match.
> **Outreach Angle:** "Paid-but-not-activated is the expensive complaint. It costs the refund and the review. How do you reconcile mandate debits against entitlements today?"
> **Suggested Subject Line:** "Debits vs entitlements at Story TV"

> **Insight #4 (secondary, group-level): Eloelo's stated diaspora expansion**
> **Evidence:** S2 — the Series B stated international expansion into Indian diaspora markets ([Entrepreneur India](https://india.entrepreneur.com/news-and-trends/eloelo-raises-usd-135-mn-series-b-led-by-play-ventures-to/489831)). S1/S4 — the US is the #2 web market but monetised through Play only; no US App Store listing and no direct billing.
> **Pain Point:** any move into diaspora markets starts on app stores (15–30% fees) because there is no direct international billing.
> **Yuno Value Proposition:** international card and APM acceptance from one integration, if and when they go direct outside India.
> **Best Success Case:** inDrive (multi-country launches), pattern match.
> **Outreach Angle:** keep this for the call; at 1.38% US traffic it's not an opener.
> **Suggested Subject Line:** —

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. #1 short-drama app in India in Q2 with 50%+ quarter-on-quarter revenue growth, and every direct renewal goes through one mandate gateway.
2. If NPCI's mandate portability lands as reported, your Autopay base stops being tied to the gateway it was created on.
3. At 3.5M+ paying subscribers, mandate setup speed is your acquisition funnel. What's behind it when the primary rail slows?

**Cold call openers (conversational, one sentence each):**
1. "You've scaled faster than anyone in micro-drama this year. How many gateways sit behind your Autopay mandates today?"
2. "With NPCI looking at mandate portability, are you thinking about putting a second provider behind renewals?"
3. "Paid-but-not-activated is the complaint that costs you the refund and the review. How are mandate debits reconciled to entitlements?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| Kuku TV (Kuku / Mebigo Labs) | kukufm.com | India | Group 10M+ paying subs; $85M round Oct 2025 | India | **Razorpay** per own FAQ (possibly stale); UPI Autopay merchant | https://techcrunch.com/2025/10/15/indias-kuku-snags-85m-as-mobile-content-wars-intensify/ ; kukufm.com FAQ |
| Quick TV (ShareChat / Moj) | — | India | 40M+ users watching micro-drama (company claim) | India | Not found | https://techcrunch.com/2026/01/21/indias-app-downloads-rebounded-to-25-5-billion-in-2025-fueled-by-ai-assistants-and-microdrama-boom/ |
| Pocket FM (Pocket Saga, after Pocket TV shut in Jun 2026) | pocketfm.com | India | >$500M ARR (group); $103M Series D | India, US | **Stripe** (US/EU/LatAm, verified); **Juspay** (India UPI, case study now 404, unverified) | https://stripe.com/customers/pocket-fm ; https://inc42.com/buzz/pocket-fm-shuts-pocket-tv-despite-indias-microdrama-boom/ |
| Flick TV (Flick Media Pvt Ltd) | flicktv.in | India (Noida) | $2.3M seed (Stellaris); 1M+ downloads | India | Not found | https://flicktv.in |
| ReelSaga | reelsaga.com | India (Mumbai) | $2.1M seed (Picus) | India, SEA, Middle East | Not found | https://startuptalky.com/news/reelsaga-raised-seed-round-funding/ |
| Chai Shots (Chai Bisket) | chaishots.in | India (Hyderabad) | $5M seed | Telugu / regional India | Not found | https://inc42.com/buzz/chai-bisket-raises-5-mn-to-launch-microdrama-ott-platform |
| ReelShort (Crazy Maple) | reelshort.com | US / China | ~$1.2B gross consumer spend 2025 | Global, incl. India | Not found | https://india.entrepreneur.com/technology/indias-usd-300-mn-microdrama-market-is-just-taking-off |
| DramaBox | dramaboxdb.com | Singapore / China | ~$140M IAP revenue Q1 2026 | Global, incl. India | Not found | https://sensortower.com/blog/state-of-short-drama-apps-2026-report |

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| STAGE | stage.in | Regional-language OTT | India | UPI Autopay + Paytm option in checkout config; 4.4M paying subs | https://entrackr.com/fintrackr/ott-platform-stages-revenue-jumps-6x-to-rs-111-cr-in-fy25-11106217 |
| aha (Arha Media) | aha.video | Telugu / Tamil OTT | India + diaspora | UPI Autopay + Play / Apple / Amazon / Roku + Stripe international | aha.video FAQ |
| ShemarooMe | shemaroome.com | SVOD | India + diaspora | Juspay verified in production + in-house switch (this repo) | `2-ready-to-outreach/shemaroo.md` |
| Hoichoi (SVF) | hoichoi.tv | Bengali OTT | India + ~40% international revenue (old data) | Diaspora billing | https://svf.in/news/hoichoi-has-13-million-viewers-with-40-of-revenue-being-international/amp/ |
| Sun NXT | sunnxt.com | South-Indian OTT | India | Telco-bundled distribution | https://telecomtalk.info/?p=461004 |
| ZEE5 | zee5.com | OTT | India + global | Juspay logo on HyperCheckout page (logo only) | https://juspay.io/lp/hypercheckout/contact |

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| Shemaroo (ShemarooMe) | Juspay (India), with an in-house switch above it | Verified 2026-10-15 | SVOD | `2-ready-to-outreach/shemaroo.md` |
| Pocket FM | Juspay (India UPI) — **unverified, case study now 404** | Dec 2023 (indexed) | Audio series / micro-drama | https://juspay.io/case-studies/pocketfm-tunes-to-higher-success-rates (404) |

*No verified case study of a direct micro-drama competitor adopting payment orchestration.*

#### 11D. Prospect Scoring

Only verified signals; quick pass on the strongest peers.

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| Pocket FM — multiple PSPs (Stripe + Juspay/India) | 3 | ⬜ Stripe verified, Juspay unverified | Stripe customer page |
| Pocket FM — high traffic outside home (US) | 2 | ⬜ not checked (no traffic data) | — |
| Kuku FM — orchestration status | — | ⬜ Razorpay direct per FAQ; TAL Juspay contradicted | kukufm.com FAQ |
| aha — multiple billing channels + Stripe international | 3 | ⬜ Stripe named in FAQ; no second card PSP found | aha.video FAQ |
| STAGE — UPI Autopay, single rail | — | ⬜ PSP not found | stage.in |

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Pocket FM | Competitor / peer | India, US | Not scored | — | Stripe international + India UPI; >$500M ARR | ✅ (Juspay) |
| 2 | Kuku FM / Kuku TV | Competitor | India | Not scored | — | 10M+ paying subs; TAL Juspay contradicted by Razorpay FAQ | ✅ (Juspay) |
| 3 | aha | Peer | India + diaspora | Not scored | — | Five billing channels incl. Stripe international | ✅ (Juspay) |
| 4 | STAGE | Peer | India | Not scored | — | UPI Autopay, 4.4M paying subs | ✅ (Juspay) |
| 5 | Hoichoi | Peer | India + diaspora | Not scored | — | ~40% international revenue (old data) | ✅ (Juspay) |
| 6 | ReelShort | Competitor | Global | Not scored | — | ~$1.2B gross spend | ✅ |
| 7 | DramaBox | Competitor | Global | Not scored | — | ~$140M IAP Q1 2026 | ✅ |
| 8 | **ReelSaga** | Competitor | India, SEA, Middle East | Not scored | — | Multi-region intent from launch | ❌ **Not in TAL — genuine find** |
| 9 | **Chai Shots** | Competitor | India (regional) | Not scored | — | $5M seed, regional micro-drama | ❌ **Not in TAL** (small) |
| 10 | **Quick TV (ShareChat)** | Competitor | India | Not scored | — | 40M+ micro-drama users | ❌ **Not in TAL** (sits inside ShareChat) |

⚠️ **TAL data-quality flag:** `Payment Orchestrator = Juspay` appears on nearly every Indian OTT row (Kuku FM, STAGE, Flick, Hoichoi, aha, SonyLIV, ZEE5, Greenhorn) with `Payment Gateway` blank on all of them. Two of those were checked this run and contradicted (Story TV → Cashfree; Kuku FM → Razorpay FAQ). **Re-verify before trusting the column on any of them.**

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | Group FY24: **zero operating revenue**, net loss ₹99 Cr (confirmed, RoC via Entrackr). FY25: ₹69.5 Cr (~US$8M) operating revenue, net loss ₹98.5 Cr `[aggregator, not filing]`. Apr 2025 company claim: ₹200 Cr run rate (US$23M ARR), Eloelo-wide, before Story TV scaled. **No FY26 / Story TV-specific revenue found.** | https://entrackr.com/fintrackr/five-year-old-eloelo-reports-zero-revenue-and-rs-99-cr-loss-in-fy24-8939085 ; https://lapaasvoice.com/startup/eloelo/financials/ ; https://inc42.com/?p=508790 |
| GMV / Gross Transaction Volume | Not found | — |
| Average Transaction Value (USD) | ~₹599–₹699 per quarterly charge (~US$7–8); ₹1,099 annual (~US$13); ₹1 trial | App Store IAP list; THR India |
| Est. Annual Transactions | ~3.5M–15M+ | 3.5M subs × 1 (all annual) to × ~4.35 (all 84-day quarterly), plus trial charges. `[ESTIMATE, not confirmed]` range |
| **Monthly transaction count** | ✅ **DERIVED: ≥~290,000/month floor; ~1.0–1.3M if mostly quarterly.** 3.5M+ paid subscribers (THR India, 1 Jun 2026) ÷ T&C-defined billing cadence (84-day quarter / 360-day year). Both inputs sourced. Billing unit: subscription charges across all rails, so the addressable (non-store) share is lower but unquantified. | THR India; storytv.asia/tnc |
| Active Customers / Users | 3.5M+ paid subscribers (Jun 2026); "10M+ users" (Caplight signal, Jun 2026); 10Cr+ Play downloads (Oct 2026) | THR India; Caplight; Play listing |
| Primary Currency | INR | — |
| Top 3 Markets by Revenue | India (overwhelming); US (Play only); others negligible `[INFERENCE from traffic + listings]` | — |
| Billing channel split (web vs app store) | **Not found as a figure.** Evidence points to direct UPI Autopay as dominant: own FAQ, most complaints describe UPI debits, and Sensor Tower's store revenue estimate is ~$40K/month (`[UNVERIFIED — search summary only]`). No web checkout. | Own FAQ; reviews; https://www.exchange4media.com/digital-news/microdrama-apps-break-into-indias-top-streaming-giants-whats-changing-in-ott-153391.html |

---

### Overall Research Confidence

**Medium.** Traffic data was **supplied** (SimilarWeb Sales Intelligence, 2026-10-19). It is single-domain and web-only, and it doesn't count app traffic for an app-first business, so it was used as a market-mix signal only.
**Strong:** legal entity; billing model and rails (from their own FAQ/T&Cs in the site bundle); incumbent PSP (Cashfree's own case study, read first-hand); subscriber scale and growth (THR India and MediaNews4U/Sensor Tower, read first-hand); complaint volume (2,000-review scrape).
**Limited:** no APK inspection (the one check that would settle the Juspay question); no in-app checkout walkthrough; no billing-channel split; Story TV-specific revenue unknown; several corporate items search-only; the funding window is unclear.

---

### Manual Research Recommendations

> **Area:** Yuno capability fit — India UPI Autopay
> **Why it matters:** the entire pitch is domestic mandate routing and redundancy. If Yuno can't create and route UPI Autopay mandates in India through licensed partners, there is no product to sell, and this account should be overridden down.
> **Suggested manual action:** ask internally which Indian PA / UPI partners Yuno routes to, and whether recurring mandates (creation and execution) are supported.

> **Area:** Orchestration status (Section 3B)
> **Why it matters:** the TAL says Juspay. If it's right, the motion flips to displacement and the opening line changes.
> **Suggested manual action:** download the APK on a personal device (or from the Play Store via a device dump) and grep the dex files for `in.juspay` / `hypersdk` / `com.cashfree` / `com.razorpay`.

> **Area:** Billing-channel split (Section 12)
> **Why it matters:** the higher the app-store share, the less is addressable.
> **Suggested manual action:** walk the ₹1 trial paywall on Android and iOS in India. Ask on discovery: "What share of active subscriptions sit on UPI Autopay vs Play vs Apple?"

> **Area:** Monthly transaction count (confirm)
> **Why it matters:** it's derived from a press-reported subscriber figure (Jun 2026), not a filing.
> **Suggested manual action:** confirm on discovery. Also confirm the plan mix (quarterly vs annual), which moves the figure by ~4×.

> **Area:** NPCI mandate portability status
> **Why it matters:** it's the timing hook for Insight #2, and it's currently a press report of a proposal.
> **Suggested manual action:** check NPCI circulars and GFF 2026 announcements before using it in outreach.

> **Area:** Funding window
> **Why it matters:** a confirmed 2026 round would add +2 and show fresh capital for infrastructure.
> **Suggested manual action:** check Tracxn / Entrackr for the Mar 2026 "growth equity" round amount.

---

### Appendix: All Source URLs

**Section 1 — Traffic**
- `accounts/traffic/storytv.md` (SimilarWeb Sales Intelligence, supplied 2026-10-19)

**Section 2 — Legal entities**
- https://storytv.asia/tnc · https://storytv.asia/privacy · https://storytv.asia/refund (served from https://storytv.asia/assets/index-CsUtyg6W.js)
- https://www.companydetails.in/company/greenhorn-wellness-private-limited
- https://www.caplight.com/company/greenhornwellness
- https://storyboard18.com/digital/eloelo-group-enters-info-tainment-space-with-launch-of-micro-learning-app-master-85974.htm
- https://india.entrepreneur.com/news-and-trends/eloelo-raises-usd-135-mn-series-b-led-by-play-ventures-to/489831
- https://play.google.com/store/apps/details?id=story.tv.drama.reels&hl=en_IN
- https://apps.apple.com/in/app/id6746484263

**Section 3 — PSPs**
- https://www.cashfree.com/case-study/from-signup-to-renewal-how-cashfree-powers-story-tv-s-subscription-growth-at-scale/
- https://voxya.com/consumer-complaints/fraudulent-autopay-subscription-deduction-without-consent-by-story-tv-/268221
- https://storytv.asia/faq-1 · https://storytv.asia/faq-2 · https://storytv.asia/paytmcashback · https://storytv.asia/bhimcashback

**Section 4 — APMs**
- https://play.google.com/store/apps/details?id=story.tv.drama.reels&hl=en_US&gl=US
- https://apps.apple.com/in/app/id6746484263

**Section 5 — Complaints**
- https://play.google.com/store/apps/details?id=story.tv.drama.reels&hl=en_IN
- https://voxya.com/consumer-complaints/-autopay-unwanted-subscription-/257355
- https://voxya.com/consumer-complaints/-unauthorized-599-autopay-deduction-and-refund-refusal-by-story-tv-app-/259623
- https://voxya.com/consumer-complaints/story-tv-unauthorized-autopay-deduction/262355
- https://voxya.com/consumer-complaints/the-payment-of-the-subscription-has-been-deducted-before-the-end-of-trial-period/270139
- https://voxya.com/consumer-complaints/unauthorised-payment-/264216
- https://www.outlookbusiness.com/news/inside-indias-dark-pattern-crackdown-why-zepto-bookmyshow-and-others-are-under-ccpa-scanner

**Section 6 — Corporate**
- https://www.medianews4u.com/indias-mobile-app-market-hits-record-345-million-iap-revenue-in-q2-2026-story-tv-tops-short-drama-apps-report/
- https://www.mediainfoline.com/brand/story-tv-bets-big-on-south-india-expanding-premium-vertical-storytelling-across-the-region
- https://www.medianews4u.com/nikunj-mundhra-joins-eloelo-group-as-vp-revenue-growth/
- https://startupwired.com/2026/03/31/eloelo-targets-50m-as-micro-drama-market-explodes-now/
- https://inc42.com/?p=508790
- https://entrackr.com/fintrackr/five-year-old-eloelo-reports-zero-revenue-and-rs-99-cr-loss-in-fy24-8939085
- https://lapaasvoice.com/startup/eloelo/financials/

**Section 7 — Payment news**
- https://inc42.com/buzz/npci-to-let-users-port-upi-autopay-mandates-across-apps-report/

**Section 11 — Competitors**
- https://techcrunch.com/2025/10/15/indias-kuku-snags-85m-as-mobile-content-wars-intensify/
- https://techcrunch.com/2026/01/21/indias-app-downloads-rebounded-to-25-5-billion-in-2025-fueled-by-ai-assistants-and-microdrama-boom/
- https://stripe.com/customers/pocket-fm
- https://inc42.com/buzz/pocket-fm-shuts-pocket-tv-despite-indias-microdrama-boom/
- https://flicktv.in
- https://startuptalky.com/news/reelsaga-raised-seed-round-funding/
- https://inc42.com/buzz/chai-bisket-raises-5-mn-to-launch-microdrama-ott-platform
- https://india.entrepreneur.com/technology/indias-usd-300-mn-microdrama-market-is-just-taking-off
- https://sensortower.com/blog/state-of-short-drama-apps-2026-report
- https://entrackr.com/fintrackr/ott-platform-stages-revenue-jumps-6x-to-rs-111-cr-in-fy25-11106217
- https://svf.in/news/hoichoi-has-13-million-viewers-with-40-of-revenue-being-international/amp/
- https://telecomtalk.info/?p=461004
- https://juspay.io/lp/hypercheckout/contact
- https://juspay.io/case-studies/pocketfm-tunes-to-higher-success-rates (404)

**Section 12 — Business case**
- https://www.hollywoodreporterindia.com/features/insight/indias-microdrama-boom-how-data-desire-and-aritifical-intelligence-are-reshaping-entertainment
- https://www.exchange4media.com/digital-news/microdrama-apps-break-into-indias-top-streaming-giants-whats-changing-in-ott-153391.html

</details>
