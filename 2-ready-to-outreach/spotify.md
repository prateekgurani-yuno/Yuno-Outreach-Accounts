# Spotify

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 14 / 29 → 🟢 Medium **on arithmetic** — **ANALYST OVERRIDE applied, tier set DOWN to 🔴 Low.** See the ICP breakdown for the reasoning.
**Industry:** Audio streaming subscription (music, podcasts, audiobooks; consumer) · **HQ:** Stockholm, Sweden — Spotify Technology S.A. (Luxembourg, NYSE: SPOT); main operating company **Spotify AB**; APAC entities in India, Japan, Singapore, Australia · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **In-house** — Spotify runs a central in-house Global Payments team and its own payments platform and Payment SDK, with several PSPs behind it. Checkout.com was signed in Feb 2026 for global acquiring with AI routing. No third-party orchestrator found.
**⛔ READ BEFORE ANY OUTREACH:** The payments buying centre is global: the VP Global Head of Payments is in Stockholm/London, and the PSP decision was made 8 months ago. A JAPAC payments function does exist (a "Payments Associate Director, JAPAC" is named in a 2024 job ad). Check account ownership with your manager before sequencing from APAC.

---

> # 🔒 PHASE 0 — QUALIFICATION GATE
>
> | Rule | Result |
> |---|---|
> | PSP / gateway / acquirer / orchestrator | **Does not fire.** Spotify is a merchant. |
> | Existing Yuno customer | **Not found.** `https://y.uno/en` fetched 2026-10-19 (HTTP 200, 747 KB): zero occurrences of "spotify". Caveat: a logo shown only as an image without alt text would not show up in this check. |
> | No online payment volume | Does not fire. |
> | HQ west of Dubai with no APAC operations | **Does not fire, but borderline.** HQ is in Sweden. APAC operations exist: the FY2025 20-F lists Spotify India LLP, Spotify Japan K.K., Spotify Singapore Pte Ltd. and Spotify Australia Pty Ltd as subsidiaries ([Ex-8.1](https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/spot-20251231xexx81.htm)). The same 20-F reports leased offices in Australia, India, Indonesia, Japan, Singapore, South Korea and Taiwan ([20-F](https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm)). |
> | Monthly transactions < 40,000 (sourced) | **Does not fire.** Spotify states it "processes more than a billion payments annually" ([lifeatspotify.com](https://www.lifeatspotify.com/find-your-team/job-categories/payments)), which is more than 83M a month. |

> # ⚠️ METHOD NOTES — disclosed up front
>
> 1. **Traffic was supplied** (`accounts/traffic/spotify.md`, Similarweb Sales Intelligence, pulled 2026-10-19, Jul–Sep 2026, spotify.com only). Its caveats apply throughout this report:
>    - **(a)** Only the top 10 countries are shown, as share only. Per-country visits below are `[DERIVED from supplied share, not a SimilarWeb figure]` (share × 583.0M average monthly visits).
>    - **(b)** It covers a single domain. Spotify has no regional ccTLDs; markets sit under spotify.com paths such as `/in-en/`. No recombination was needed.
>    - **(c)** **Mobile app traffic is excluded.** Similarweb counts desktop and mobile web only (63.05% / 36.95%).
>    - **(d)** **Spotify is app-heavy, and some Premium is billed through Google Play, telcos and prepaid vouchers.** Web traffic is used only as a market-mix signal. It was **not** used to size transactions or for the 40k gate.
>    - **(e)** The top 10 cover only 64.05% of traffic. The other 35.95% includes every APAC market except India and the Philippines (Indonesia, Japan, Australia and others), so those markets have **no** traffic figure here.
> 2. **Fetching worked** (WebFetch and curl). The Phase 2 agents ran in parallel with Agent 1 because the supplied traffic already fixed the market list.
> 3. **Spotify's own country pages were read directly.** Two sources were used:
>    - `support.spotify.com/{cc}/article/...` help pages for India, the Philippines, Indonesia, Japan, Australia, Malaysia, Thailand, Singapore, Korea and Taiwan.
>    - `spotify.com/{cc}/premium/` pages. On JP, KR, MY, VN, SG, TW and HK these carry a payment-logo strip served from `paymentsdk.spotifycdn.com`. The IN, PH, ID, AU, NZ and TH pages do not render that strip.
>
>    **These pages are the backbone of Section 4.** A method missing from a logo strip is weak evidence of absence, because checkout itself sits behind login.
> 4. **Territory weighting.** Only 2 of the top 10 traffic markets are in territory: India (#3) and the Philippines (#6). The research focuses on those two, plus the APAC markets where Spotify's own pages could be read. US, Brazil and EU markets were not researched for methods.
> 5. **Q3 2026 results are due 22 Oct 2026**, three days after this report. Re-check the figures after that date.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Spotify is the world's largest audio streaming subscription service, serving 184 countries with 751M MAUs and 290M Premium subscribers at end-2025, and FY2025 revenue of €17.19B ([20-F](https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm)). In Q2 2026 it reached 777M MAUs and 300M subscribers on €4.78B revenue ([Q2'26 6-K](https://www.sec.gov/Archives/edgar/data/1639920/000114036126031044/ef20078867_ex99-1.htm)). Premium is sold mostly direct on web, because Spotify does not sell Premium inside its iOS app ([support](https://support.spotify.com/in-en/article/cant-subscribe-to-premium-in-the-ios-app/)). Partner/telco billing, Google Play Billing and prepaid vouchers are also used.

**SimilarWeb total visits (last full month):** ~583.0M average monthly visits (Jul–Sep 2026; 1.749B over 3 months). Source: supplied. Web only; app traffic excluded.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | United States | 24.98% | Not researched (out of territory) | — | Not researched (Spotify USA Inc. not checked) |
| 2 | Brazil | 13.71% | Not researched (out of territory) | — | Not researched |
| 3 | **India** | 4.19% | Visa/MC cards (recurring only at listed banks), **UPI Intent/Collect/QR with UPI Autopay**, PayPal, Google Play Billing, one-time prepaid plan (₹799/yr), Vi postpaid bundle | **RuPay, netbanking, wallets not found** on any Spotify page; card recurring limited to a published bank list | ✅ **Spotify India LLP**, merchant of record for direct India purchases ([ToU](https://www.spotify.com/in-en/legal/end-user-agreement/)) |
| 4 | United Kingdom | 3.93% | Not researched (out of territory) | — | Not researched |
| 5 | Mexico | 3.25% | Not researched (out of territory) | — | Not researched |
| *6* | ***Philippines*** | *3.03%* | *Carrier billing via Fortumo, PayPal, Google Play Billing; GCash (moderator statement, summary-level)* | *Maya, GrabPay, InstaPay, OTC not confirmed* | *❌ No PH entity in Ex-8.1. Users contract with **Spotify AB** (Sweden), so billing is cross-border* |

*The italic row is the only other in-territory market in the top 10, added because it falls outside the overall top 5.*

### Legal entities
- **Spotify AB** (Sweden): main operating company and contracting party for PH, JP and AU users ([20-F](https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm), [PH ToU](https://www.spotify.com/ph-en/legal/end-user-agreement/)).
- **Spotify India LLP** (India): "Sales, distribution, and marketing", and MoR for direct India purchases. LLPIN AAP-6218 `[UNVERIFIED — search summary only]`.
- **Spotify Japan K.K.** (Japan): sales and marketing support. Corporate number not found.
- **Spotify Singapore Pte Ltd.** (Singapore): sales and marketing support. UEN 201133483D `[UNVERIFIED — search summary only]`.
- **Spotify Australia Pty Ltd** (Australia): sales and marketing support. ABN 70 154 200 941 `[UNVERIFIED — search summary only]`.

### Known PSPs
- **Checkout.com**: `[Press Release]`, 3 Feb 2026, global acquiring with Intelligent Acceptance (AI routing), Network Tokens and Authentication ([Checkout.com](https://www.checkout.com/newsroom/checkout-com-announces-strategic-partnership-with-spotify-to-power-efficient-scalable-payments-globally)). **Verified.**
- **Adyen**: `[Third-Party Report]` from SEC filings. It handled ~74% of payment processing in FY2019, and Adyen plus PayPal/Braintree handled "the vast majority" in FY2022. **The FY2025 20-F no longer names any processor**, so the current share is unknown.
- **PayPal / Braintree**: FY2022 20-F, and PayPal is a consumer method on the IN, PH, JP, MY, SG, TW, HK, AU and NZ help pages.
- **Boku** (carrier billing): `[Developer Docs]`, named on the JP, AU, MY, SG and TW help pages.
- **Fortumo** (carrier billing): named on the PH and TH help pages.
- **Google Play Billing**: offered on Android in all APAC markets checked.
- **No processor is named for UPI (India), GCash (PH) or GoPay (ID).**

### Orchestration status
**In-house orchestration layer.** Evidence:
- Spotify's Global Payments team calls itself "central in-house payment specialists". It runs a "payments platform [that] supports a multitude of business lines" and manages "PSPs, Payment Networks, APM providers, Issuers" ([lifeatspotify.com](https://www.lifeatspotify.com/find-your-team/job-categories/payments), verified).
- The checkout assets load from `paymentsdk.spotifycdn.com`, which points to Spotify's own Payment SDK `[Source Code]`.
- Spotify has run several PSPs at once (Adyen + PayPal/Braintree, and now Checkout.com).
- No third-party orchestrator (Juspay, Spreedly, Primer, Gr4vy, Payrails, Yuno) was found.

### Buying signals
- 🤝 **New global acquirer in Feb 2026.** Checkout.com was signed for global acquiring with AI routing and network tokens ([Checkout.com](https://www.checkout.com/newsroom/checkout-com-announces-strategic-partnership-with-spotify-to-power-efficient-scalable-payments-globally)). Spotify is actively changing its PSP mix, but this decision is fresh, which **narrows** the window rather than opening it.
- 🇮🇳 **India is growing fast and now profitable.** Spotify India LLP's FY25 revenue was ₹513.77 crore (+59.8%), and subscription income was ₹316.83 crore (+88.8%) ([Storyboard18](https://www.storyboard18.com/how-it-works/spotify-india-turns-profitable-in-fy25-as-subscriptions-surge-and-marketing-costs-shrink-86189.htm)).
- 🤝 **First India telco bundle (Vi), 26 Jun 2026** ([MBW](https://www.musicbusinessworldwide.com/spotify-bundles-three-months-of-premium-with-vodafone-ideas-postpaid-plans-in-its-first-indian-telco-partnership/)). Billing mix in India is diversifying.
- 💼 **India local-acquiring agenda.** A "Payments Growth Optimisation Lead, India" (Mumbai, reporting to "Payments Associate Director, JAPAC") was hired to cover "local PA/PG and issuer set ups" and data localisation. Posted Sep 2024, closed Aug 2025 ([TCV job board](https://portfoliojobs.tcv.com/companies/spotify/jobs/40297684-payments-growth-optimisation-lead-india)). **No open payments roles today.**
- 📱 **Web checkout matters more after the iOS link-out.** Since May 2025, Apple's US rules let Spotify link out to web checkout from its iOS app ([20-F](https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm)). This applies in the US only, not APAC.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach spotify` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 14 / 29
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | +5 | ✅ **SOURCED: >83M/month.** "Today, Spotify processes more than a billion payments annually" ([lifeatspotify.com](https://www.lifeatspotify.com/find-your-team/job-categories/payments), fetched 2026-10-19; the page is undated). 1B ÷ 12 ≈ 83M. **Billing unit:** any payment across Premium, Ad Studio, Podcast Advertising and Live ticketing; Premium monthly renewals dominate. Cross-check: 300M subscribers ([Q2'26](https://www.sec.gov/Archives/edgar/data/1639920/000114036126031044/ef20078867_ex99-1.htm)) billed monthly would be up to ~3.6B a year, but partner-billed, Google Play and prepaid-voucher subscribers do not run through Spotify's own processing. That makes "more than a billion" a floor, not an overstatement. |
| Orchestration status | +1 | ✅ **In-house layer** ([lifeatspotify.com](https://www.lifeatspotify.com/find-your-team/job-categories/payments), verified; `paymentsdk.spotifycdn.com` in page source). Hardest sell. |
| 3+ countries | +3 | ✅ 10 countries above 2.5% each (supplied Similarweb). |
| Multiple PSPs | +3 | ✅ Checkout.com ([press, Feb 2026](https://www.checkout.com/newsroom/checkout-com-announces-strategic-partnership-with-spotify-to-power-efficient-scalable-payments-globally)), Adyen + PayPal/Braintree ([FY2022 20-F](https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/ck0001639920-20221231.htm)), and carrier billing via Boku and Fortumo (Spotify's own help pages). |
| Local rail or licensing gap in a top-3 market | 0 | ❌ **Not met.** The top 3 are US, Brazil and India. India (#3) has UPI with UPI Autopay ([support](https://support.spotify.com/in-en/article/paying-for-spotify-with-upi/)) and a local entity (Spotify India LLP). RuPay and netbanking are not found, but neither is the rail this signal names. US and Brazil are out of territory. |
| Recent expansion | 0 | ❌ No new-market launch in the last 12 months; Spotify already serves 184 countries. The new tiers (Lite/Standard/Platinum in IN and ID, Nov 2025, [TechCrunch](https://techcrunch.com/2025/11/13/spotify-introduces-a-premium-platinum-plan-with-lossless-access-in-five-markets/)) and the Vi bundle are product and distribution changes, not market entry. |
| Payment issues reported | 0 | ⬜ One verified India UPI Autopay reconciliation thread from Jul 2025, which is just outside 12 months ([community](https://community.spotify.com/t5/Subscriptions/Spotify-showing-payment-failed-while-GPay-shows-autopay-success/m-p/7065132)). Several more India UPI and PH GCash threads appear in search summaries only, with unclear dates. That pattern is plausible but not verified as moderate. |
| Funding >$10M | 0 | ❌ N/A. Public company, no funding round. |
| High traffic outside home | +2 | ✅ The home market, Sweden, is not even in the top 10. The US, the largest market, is 24.98%. |
| Competitor using orchestration | 0 | ⬜ No music or audio streamer was found on a payment orchestrator. Gaana's Juspay link (for UPI AutoPay, per NPCI 2021) is `[UNVERIFIED — search summary only]`. |
| Payment job postings | 0 | ⬜ The India payments lead role was posted Sep 2024 and closed Aug 2025, outside the window. Spotify's live Lever feed (80 roles, pulled 2026-10-19) has no open payments, checkout or billing role. The open roles are Subscriptions engineering/PM and a Fraud Analyst (Revenue Protection), all in London/Stockholm. |

**Arithmetic tier:** 14 → 🟢 Medium.

**⚖️ ANALYST OVERRIDE — tier set DOWN to 🔴 Low.** Reasoning:
1. **The matrix is double-counting scale.** Ten of the 14 points come from transaction volume, 3+ countries and traffic outside home, which are true of any global consumer giant. The other four (multiple PSPs, in-house) describe a sophisticated stack, not a gap.
2. **In-house and freshly re-tendered.** Spotify has:
   - a central in-house Global Payments team that owns "payment fees" and PSP/APM relationships;
   - its own Payment SDK;
   - a new global acquirer (Checkout.com) signed in **Feb 2026**, whose product includes AI routing, retries and network tokens. That covers the core of an orchestration pitch.

   A cold "you need orchestration/routing" pitch will not land, and the PSP-selection window has just closed.
3. **The buying centre is mostly out of territory.** The VP Global Head of Payments sits in the global organisation (Stockholm/London). The one exception is the JAPAC payments function (a Payments Associate Director, JAPAC, plus an India optimisation lead). It is real, but it works within the global team's vendor decisions.
4. **APAC is a small share of monetisation.** Rest of World, which includes all of APAC plus MENA and Africa, is ~37% of MAUs but only ~15% of Premium subscribers ([MBW citing the Q2'26 deck](https://www.musicbusinessworldwide.com/spotify-hits-300-million-premium-subscribers-in-q2-202/)). Spotify India LLP's FY25 revenue was ₹513.77 crore, and APAC is not broken out in filings.
5. **Part of APAC billing is untouchable.** Telco bundles (Vi in India, plus Telkomsel and Globe as legacy partners), Google Play Billing and prepaid vouchers (Tokopedia in Indonesia) bill outside Spotify's own processing.

**What would reverse this:**
- a new APAC payments hire or RFP;
- evidence that Checkout.com does not cover a local rail Spotify wants (e.g. India local PA/PG, Indonesian wallets/QRIS, Philippine wallets);
- a warm path into the JAPAC payments lead.

The narrow, credible angle is **APAC local-rail depth and reliability** (India UPI Autopay reconciliation, PH GCash failures, Indonesian wallets), which a global acquirer does not solve by itself. Until one of those triggers appears, treat this as a **named strategic account for manager or enterprise review, not an SDR cold sequence.**

### Source Notes
- ✅ India UPI: three checkout flows (Intent, Collect for iOS, QR for desktop) and a dependency on UPI Autopay support. The page also says "wait 24-48 hours… processing delay from your bank". Verified by curl on 2026-10-19: [support.spotify.com/in-en/article/paying-for-spotify-with-upi](https://support.spotify.com/in-en/article/paying-for-spotify-with-upi/)
- ✅ India failed-payment page: "Due to new banking regulations in India, some payment providers no longer support recurring payments". It lists the banks whose Visa and Mastercard cards support recurring (e.g. SBI credit only) and offers a prepaid plan as the fallback. Verified by curl: [support.spotify.com/in-en/article/failed-payment](https://support.spotify.com/in-en/article/failed-payment/)
- ✅ Payment-logo strips on the Premium pages, verified by curl on 2026-10-19:
  - JP: Visa/MC/Amex/JCB/UnionPay, PayPay, au/docomo/SoftBank, PayPal
  - KR: cards, KakaoPay, Naver Pay, Toss Pay, U+/KT/SKT
  - MY: cards, Touch 'n Go, ShopeePay, Digi/Maxis/Celcom
  - VN: MoMo and cards
  - SG: cards, PayPal, ShopeePay
  - TW: Visa/MC/JCB, Taiwan Mobile/Chunghwa/FET
  - HK: cards and PayPal
- ✅ Carrier-billing partners named on help pages, verified by curl: Boku (JP, AU, MY, SG, TW) and Fortumo (PH, TH).
- ✅ Indonesia "Pay as you go" is 1, 3 or 6-month Premium vouchers sold via Tokopedia. Verified: [support.spotify.com/id-en/article/pay-as-you-go](https://support.spotify.com/id-en/article/pay-as-you-go/)
- ✅ Checkout.com partnership, 3 Feb 2026. Verified fetch: [checkout.com newsroom](https://www.checkout.com/newsroom/checkout-com-announces-strategic-partnership-with-spotify-to-power-efficient-scalable-payments-globally)
- ✅ "More than a billion payments annually" and the in-house Global Payments team. Verified fetch: [lifeatspotify.com](https://www.lifeatspotify.com/find-your-team/job-categories/payments)
- ✅ Entities, financials and payment-fee disclosure (FY2025 20-F, Q2'26 6-K). Verified by the research agent from SEC EDGAR.
- ⚠️ **Is Adyen still current?** Adyen is confirmed only through FY2022 filings. The FY2025 20-F names no processor. Do not cite Adyen as current in outreach.
- ⚠️ **India plan line-up conflict.** TechCrunch (Nov 2025) reported Lite ₹139, Standard ₹199 and Platinum ₹299. The live India page on 2026-10-19 shows Standard ₹139, Platinum ₹299, Student ₹69 and no Lite. No source explains the change; the live page wins for current prices.
- ⚠️ PH GCash and Maya, ID GoPay current status, and Indonesia "cards not supported" all come from community threads or old press. GoPay's 2020 launch is confirmed by [detikInet, 31 Aug 2020](https://inet.detik.com/cyberlife/d-5154295/bayar-spotify-premium-kini-bisa-pakai-gopay); its current availability is not verified.
- ⚠️ The registration numbers for Spotify India LLP, Singapore and Australia come from search summaries only.

### Success Case Alternatives
- **No strong Yuno success case match.** No published Yuno case covers a global audio-streaming subscription business with an in-house payments platform. Any case cited in outreach must come from Yuno's current case library, verified at time of use. Do not pull from memory.

---

## Executive Summary

Spotify (Stockholm; 300M Premium subscribers, 777M MAUs, €4.78B Q2'26 revenue) sells audio subscriptions in 184 countries. Premium is billed mostly direct on web, plus Google Play, telco bundles and prepaid vouchers. Payments are run by a central in-house Global Payments team on its own payments platform and SDK, processing more than a billion payments a year across several PSPs. In February 2026 that team added **Checkout.com** for global acquiring with AI routing. In APAC, Spotify already covers the major local rails in most markets it was checked in (UPI with Autopay, PayPay, KakaoPay/Naver Pay/Toss, Touch 'n Go, MoMo, carrier billing via Boku and Fortumo). The visible friction is **reliability on local rails**: India UPI Autopay reconciliation, India card recurring limited to a bank list, and GCash failures in the Philippines. The motion is **in-house**, the hardest sell. The account is analyst-overridden to 🔴 Low, as a strategic account rather than a cold SDR sequence.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** Path 1, supplied Similarweb (Sales Intelligence view), `accounts/traffic/spotify.md`, pulled 2026-10-19, Jul–Sep 2026, spotify.com, desktop + mobile web. Caveats are in the method notes above.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | United States | 24.98% | ~145.6M `[DERIVED from supplied share, not a SimilarWeb figure]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | Brazil | 13.71% | ~79.9M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |
| 3 | **India** ⭐ in territory | 4.19% | ~24.4M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |
| 4 | United Kingdom | 3.93% | ~22.9M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |
| 5 | Mexico | 3.25% | ~18.9M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |
| 6 | **Philippines** ⭐ in territory | 3.03% | ~17.7M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |
| 7 | Germany | 2.98% | ~17.4M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |
| 8 | Canada | 2.78% | ~16.2M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |
| 9 | Spain | 2.62% | ~15.3M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |
| 10 | France | 2.58% | ~15.0M `[DERIVED]` | Not supplied | SimilarWeb (supplied) |

- **High priority (>5%):** US and Brazil, both out of territory. No in-territory market exceeds 5%.
- **Global MAU split (end-2025):** Europe 26%, North America 16%, Latin America 21%, Rest of World 37%. Rest of World grew fastest, +21% YoY ([20-F](https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm)).
- **Top-10 markets with no confirmed local entity:** Philippines (in territory) and Brazil, Mexico, Spain, France (not researched; out of territory). See Section 2.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Stockholm, Sweden. The parent, Spotify Technology S.A., is incorporated in Luxembourg; Spotify AB (Regeringsgatan 19, 111 53 Stockholm) is the main operating company. Founded 2006.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Sweden | Spotify AB | Not captured | [20-F](https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm) |
| India | Spotify India LLP (MoR for direct India Premium, "as a distributor of Spotify AB") | LLPIN AAP-6218 `[UNVERIFIED — search summary only]` | [Ex-8.1](https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/spot-20251231xexx81.htm), [IN ToU](https://www.spotify.com/in-en/legal/end-user-agreement/) |
| India | Spotify India Private Limited (status unclear; possibly legacy) | CIN U74999MH2017FTC295679 `[UNVERIFIED — search summary only]` | [infyner](https://www.infyner.com/company/spotify/U74999MH2017FTC295679) |
| Japan | Spotify Japan K.K. | Not found | [Ex-8.1](https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/spot-20251231xexx81.htm) |
| Singapore | Spotify Singapore Pte Ltd. | UEN 201133483D `[UNVERIFIED — search summary only]` | [Ex-8.1](https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/spot-20251231xexx81.htm) |
| Australia | Spotify Australia Pty Ltd | ABN 70 154 200 941 `[UNVERIFIED — search summary only]` | [Ex-8.1](https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/spot-20251231xexx81.htm) |
| Indonesia, South Korea, Taiwan | Office leases reported; no entity in Ex-8.1 (which looks like a significant-subsidiaries list) | Not found | [20-F Item 4.D](https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm) |

**Contracting entity per the Terms of Use (verified):**
- **India:** direct purchases are with Spotify India LLP.
- **Philippines, Japan, Australia:** "between you and Spotify AB" ([PH](https://www.spotify.com/ph-en/legal/end-user-agreement/), [JP](https://www.spotify.com/jp/legal/end-user-agreement/), [AU](https://www.spotify.com/au/legal/end-user-agreement/)).

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| India | Yes (#3) | ✅ Spotify India LLP (MoR) | Not assessed for this account; the LLP's existence makes it moot | Low. The local MoR exists, and a 2024 job ad references "local PA/PG and issuer set ups" |
| Philippines | Yes (#6) | ❌ None found; ToU contracts with Spotify AB | Not verified, so no claim made | **Yes.** See warning below |
| Japan | Not in top 10 | ⚠️ Spotify Japan K.K. exists, but ToU contracts with Spotify AB | Not verified | Possible. The MoR appears to be Spotify AB |
| Australia | Not in top 10 | ⚠️ Spotify Australia Pty Ltd exists, but ToU contracts with Spotify AB | Not verified | Possible |
| Indonesia / Korea | Not in top 10 | ⚠️ Office lease only; no entity confirmed | Not verified (the APAC reference flags both as typically gated; verify before use) | Unknown |

> *"Warning: Potential cross-border operation in the Philippines. No local entity found, and the Terms of Use name Spotify AB (Sweden) as the contracting party. Card transactions are likely processed cross-border, with higher scheme costs, lower approval rates and FX exposure."* `[INFERENCE, not confirmed]`: Checkout.com's local acquiring footprint may already cover this; the acquiring entity per market is unknown.

> **MANUAL:** On a PH and an ID account, check the billing descriptor and receipt entity on a Premium charge.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Global (180+ countries) | **Checkout.com**: global acquiring, Intelligent Acceptance (AI routing), Network Tokens, Authentication. Announced 3 Feb 2026 | [Press Release] | https://www.checkout.com/newsroom/checkout-com-announces-strategic-partnership-with-spotify-to-power-efficient-scalable-payments-globally |
| Global | **Adyen**: ~74% of payment processing (FY2019) | [Third-Party Report]: SEC 20-F | https://www.sec.gov/Archives/edgar/data/1639920/000156459020004357/ck0001639920-20f_20191231.htm |
| Global | **Adyen + PayPal (incl. Braintree)**: "the vast majority of our payment processing" (FY2022) | [Third-Party Report]: SEC 20-F | https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/ck0001639920-20221231.htm |
| Global | FY2025 20-F names **no processor**. It lists cards via "third-party processors", telco integrated billing, Google Play IAP and prepaid code vendors | [Third-Party Report]: SEC 20-F | https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm |
| Global | Adyen recurring-payments case study (2017, stale) | [Provider Case Study] | https://www.adyen.com/sv_SE/kunskapshubb/fem-tips-om-betalningar-fran-spotify |
| JP, AU, MY, SG, TW | **Boku**: carrier billing | [Developer Docs]: Spotify help pages | https://support.spotify.com/jp/article/mobile-billing-payments/ · https://support.spotify.com/au/article/mobile-billing-payments/ |
| PH, TH | **Fortumo**: carrier billing | [Developer Docs]: Spotify help pages | https://support.spotify.com/ph-en/article/mobile-billing-payments/ · https://support.spotify.com/th-en/article/mobile-billing-payments/ |
| ID, PH (2016) | Fortumo carrier billing (Smart, Globe, Indosat) | [Third-Party Report] | https://thepaypers.com/payments/news/spotify-partners-fortumo-to-expand-carrier-billing-availability-in-asia |
| India | **Processor for UPI / UPI Autopay: not found.** No Razorpay, PayU, Cashfree, Juspay, BillDesk or Paytm PG link | — | — |
| PH / ID | **Processor for GCash / GoPay: not found.** No Xendit, 2C2P, Midtrans or DOKU link | — | — |
| India | Vi (Vodafone Idea) postpaid bundle; continuing billing via "Add to Bill" | [Press Release] (MBW) | https://www.musicbusinessworldwide.com/spotify-bundles-three-months-of-premium-with-vodafone-ideas-postpaid-plans-in-its-first-indian-telco-partnership/ ("Add to Bill" detail summary-only) |
| Indonesia | Tokopedia: prepaid Premium vouchers | [Developer Docs] | https://support.spotify.com/id-en/article/pay-as-you-go/ |

The privacy policy names no processors ([privacy policy](https://www.spotify.com/us/legal/privacy-policy/)).

#### 3B. Payment Orchestrator

**Classification: In-house orchestration layer.**
- [Job Listing / careers page] Spotify's Global Payments team is described as "central in-house payment specialists". Its "payments platform supports a multitude of business lines such as Premium, Ad Studio, Podcast Advertising, Live ticketing" and works with "PSPs, Payment Networks, APM providers, Issuers, and regulators". Source: https://www.lifeatspotify.com/find-your-team/job-categories/payments (verified 2026-10-19).
- [Source Code] The Premium pages load payment-method assets from `paymentsdk.spotifycdn.com`, which points to an in-house payment SDK.
- `[UNVERIFIED — search summary only]` Older job ads describe a "Payment SDK squad" in the Commerce Platform. A Nordic APIs talk describes an internal API abstracting multiple gateways ([nordicapis.com](https://nordicapis.com/sessions/spotify-payments-creates-apis-manage-complexity/); the fetch was blocked by Cloudflare).
- Searches for Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails and Yuno with Spotify returned nothing.
- **Note:** Checkout.com's Intelligent Acceptance adds acquirer-side AI routing on top of the in-house layer.

> *"Confirmed orchestration-aware and self-built. The opening is local-rail depth and reliability in APAC, not the case for orchestration itself."*

> **MANUAL:** Walk through checkout on a logged-in IN and PH account with DevTools open. Watch which domains the UPI and GCash flows hit (look for PA/PG signatures).

---

### Section 4: Alternative & Local Payment Methods

Only India and the Philippines exceed 1% within the supplied top 10. Other APAC markets are included because Spotify's own pages could be read.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| India | UPI: Intent (Android), Collect (iOS), QR (desktop) | Bank transfer / A2A | Mentioned in docs | https://support.spotify.com/in-en/article/paying-for-spotify-with-upi/ |
| India | UPI Autopay (recurring) | Direct debit / mandate | Mentioned in docs ("Your UPI provider supports recurring payments through UPI Autopay") | same |
| India | Visa / Mastercard (recurring only at listed banks) | Cards | Mentioned in docs | https://support.spotify.com/in-en/article/failed-payment/ |
| India | PayPal | Digital wallet | Mentioned in docs (help sidebar) | https://support.spotify.com/in-en/article/payment-methods/ |
| India | Google Play Billing | App store | Mentioned in docs | https://support.spotify.com/in-en/article/google-play-help/ |
| India | One-time prepaid plan (Standard, ₹799 / 1 year, no auto-renew) | Prepaid | Active on Premium page | https://www.spotify.com/in-en/premium/ |
| India | Vi postpaid bundle | Carrier billing | Mentioned in press | https://www.musicbusinessworldwide.com/spotify-bundles-three-months-of-premium-with-vodafone-ideas-postpaid-plans-in-its-first-indian-telco-partnership/ |
| India | RuPay, netbanking, Paytm/PhonePe wallets (as wallets, not UPI), EMI | — | Not found | — |
| Philippines | Carrier billing (Fortumo) | Carrier billing | Mentioned in docs | https://support.spotify.com/ph-en/article/mobile-billing-payments/ |
| Philippines | PayPal, Google Play Billing | Wallet / app store | Mentioned in docs | https://support.spotify.com/ph-en/article/payment-methods/ |
| Philippines | GCash | Digital wallet | Unknown, checkout not accessible. A moderator says "still possible… not removed" (date unclear) | https://community.spotify.com/t5/Subscriptions/Paying-with-Gcash/m-p/7161068 |
| Philippines | Maya / PayMaya | Digital wallet | Unknown. Older guides only `[UNVERIFIED]` | https://unbox.ph/news/spotify-introduces-premium-mini-for-the-philippines/ |
| Philippines | GrabPay, InstaPay/PESONet, OTC cash | — | Not found | — |
| Indonesia | Carrier billing, Google Play, Tokopedia vouchers | Carrier / app store / prepaid | Mentioned in docs | https://support.spotify.com/id-en/article/pay-as-you-go/ |
| Indonesia | GoPay | Digital wallet | Mentioned in press (launched Aug 2020; current status unverified) | https://inet.detik.com/cyberlife/d-5154295/bayar-spotify-premium-kini-bisa-pakai-gopay |
| Indonesia | QRIS, OVO, DANA, virtual accounts, Alfamart/Indomaret | — | Not found | — |
| Japan | Visa/MC/Amex/JCB/UnionPay, PayPay, au/docomo/SoftBank carrier (Boku), PayPal, gift cards | Cards / wallet / carrier | Active on Premium page (logo strip) | https://www.spotify.com/jp/premium/ |
| Japan | Konbini, Paidy, LINE Pay, Rakuten Pay | — | Not found on logo strip | — |
| South Korea | Cards, KakaoPay, Naver Pay, Toss Pay, U+/KT/SKT carrier | Cards / wallets / carrier | Active on Premium page (logo strip) | https://www.spotify.com/kr-en/premium/ |
| Malaysia | Cards, Touch 'n Go, ShopeePay, Digi/Maxis/Celcom carrier | Cards / wallets / carrier | Active on Premium page (logo strip) | https://www.spotify.com/my-en/premium/ |
| Malaysia | FPX, DuitNow | — | Not found on logo strip | — |
| Vietnam | MoMo, cards | Wallet / cards | Active on Premium page (logo strip) | https://www.spotify.com/vn-en/premium/ |
| Singapore | Cards, PayPal, ShopeePay, carrier (Boku) | Cards / wallets / carrier | Active on Premium page (logo strip) | https://www.spotify.com/sg-en/premium/ |
| Singapore | PayNow, GrabPay | — | Not found on logo strip | — |
| Taiwan | Visa/MC/JCB, Taiwan Mobile/Chunghwa/FET carrier | Cards / carrier | Active on Premium page (logo strip) | https://www.spotify.com/tw/premium/ |
| Taiwan | JKOPay, LINE Pay, convenience-store cash | — | Not found on logo strip | — |
| Hong Kong | Cards, PayPal | Cards / wallet | Active on Premium page (logo strip) | https://www.spotify.com/hk-en/premium/ |
| Hong Kong | FPS, Octopus, AlipayHK, WeChat Pay HK | — | Not found on logo strip | — |
| Australia / NZ / Thailand | AU: carrier (Boku), PayPal, gift cards. NZ: PayPal, gift cards. TH: carrier (Fortumo) | Carrier / wallet | Mentioned in docs | https://support.spotify.com/au/article/payment-methods/ |
| Australia / NZ / Thailand | PayTo, BPAY, Afterpay, PromptPay, TrueMoney | — | Not found (logo strip not rendered on these pages) | — |
| All APAC | **iOS in-app Premium purchase** | App store | **Not offered.** "due to Apple restrictions, you can't subscribe to Premium through the app for iPhone and iPad" | https://support.spotify.com/in-en/article/cant-subscribe-to-premium-in-the-ios-app/ |

**Gaps worth noting (none in a top-3 market, and absence is "not found", not proven):**
- **India:** RuPay and netbanking are absent from every page read. Card recurring is restricted to a published list of banks, with prepaid offered as the workaround. That is a real e-mandate friction point, but UPI Autopay is the dominant recurring rail and it *is* supported.
- **Indonesia:** QRIS is not found.
- **Malaysia:** FPX is not found on the logo strip.
- **Singapore:** PayNow is not found.
- **Thailand:** PromptPay is not found.

Each of these needs a logged-in checkout check before use.

> **MANUAL:** With a VPN, open checkout for IN, PH and ID. Confirm GCash/Maya (PH), QRIS/OVO/DANA (ID) and RuPay (IN).

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| UPI/wallet-specific failure: UPI Autopay debited in GPay, but Spotify shows "payment failed" and UPI is missing from payment methods | Spotify Community (India) | Isolated (verified); see the next row | Jul 2025 | https://community.spotify.com/t5/Subscriptions/Spotify-showing-payment-failed-while-GPay-shows-autopay-success/m-p/7065132 |
| UPI Autopay charged but Premium not activated / payment marked failed | Spotify Community (India) | Moderate `[UNVERIFIED — search summary only]` | Mostly 2025 | https://community.spotify.com/t5/Subscriptions/UPI-Autopay-charged-me-but-Spotify-says-payment-failed/m-p/6106214 · https://community.spotify.com/t5/Premium-Student/UPI-AUTOPAY-FAILED/td-p/6935183 |
| Failed recurring payments: card recurring blocked under India banking regulations | Spotify Help (official) | Structural (Spotify publishes a list of supported banks) | Live page, 2026-10-19 | https://support.spotify.com/in-en/article/failed-payment/ |
| UPI activation delay: Spotify tells users to "wait 24-48 hours" if paid but not activated | Spotify Help (official) | Structural | Live page, 2026-10-19 | https://support.spotify.com/in-en/article/paying-for-spotify-with-upi/ |
| GCash payments keep failing despite sufficient balance | Spotify Community (Philippines) | Moderate `[UNVERIFIED — search summary only]` | Dates unclear | https://community.spotify.com/t5/Subscriptions/GCash-payments-keep-failing/td-p/6399186 |
| GoPay failing on Premium Duo | Spotify Community (Indonesia) | Isolated `[UNVERIFIED]`, likely 2021–22 | Old | https://community.spotify.com/t5/Subscriptions/Premium-Duo-cannot-take-GoPay-Payement/m-p/5415628 |

No Reddit, Trustpilot or X threads were found in the searches run.

> *"A pattern of UPI Autopay reconciliation failures in India suggests a mandate-status sync problem between the UPI PA/PG and Spotify's subscription state. That points to an opportunity around local recurring-rail handling and status reconciliation, not routing."* `[INFERENCE, not confirmed]`

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 30 Jun 2026 (announced 26 Jun) | Vi (Vodafone Idea) postpaid bundle, Spotify's first India telco partnership | Market Expansion (distribution) | https://www.musicbusinessworldwide.com/spotify-bundles-three-months-of-premium-with-vodafone-ideas-postpaid-plans-in-its-first-indian-telco-partnership/ |
| 2 | 3 Feb 2026 | Checkout.com strategic partnership for global acquiring | Payment Infrastructure | https://www.checkout.com/newsroom/checkout-com-announces-strategic-partnership-with-spotify-to-power-efficient-scalable-payments-globally |
| 3 | 1 Jan 2026 (announced 30 Sep 2025) | Daniel Ek becomes Executive Chairman; Alex Norström and Gustav Söderström become co-CEOs | Leadership Change | https://newsroom.spotify.com/2025-09-30/spotify-announcement-daniel-ek-executive-chairman/ `[UNVERIFIED — search summary only]` |
| 4 | 13 Nov 2025 | Premium Lite / Standard / Platinum tiers launched in India and Indonesia (plus UAE, KSA, South Africa); Duo and Family closed to new subscribers there | Product / pricing | https://techcrunch.com/2025/11/13/spotify-introduces-a-premium-platinum-plan-with-lossless-access-in-five-markets/ |
| 5 | Sep 2024 – Aug 2025 | "Payments Growth Optimisation Lead, India" (Mumbai), reporting to "Payments Associate Director, JAPAC": local PA/PG and issuer set-ups, data localisation | Payment Infrastructure Hiring (closed) | https://portfoliojobs.tcv.com/companies/spotify/jobs/40297684-payments-growth-optimisation-lead-india |

- **No public payment-related RFP found.**
- No open payments, checkout or billing roles in Spotify's live Lever feed as of 2026-10-19 (80 roles). Related open roles are in London/Stockholm: Senior Backend Engineer – Subscriptions, Senior Web Engineer – Subscriptions, Senior PM – Subscriptions, and Fraud Analyst (Revenue Protection).
- In APAC, the open Business Development Senior Manager role (Singapore/Seoul) asks for experience with "telcos, OEMs, payments" ([Lever](https://jobs.lever.co/spotify/973b0b71-e8d2-4d7d-9c4b-1c716bd45c8b)).

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 3 Feb 2026 | Checkout.com to provide global acquiring, AI routing (Intelligent Acceptance) and network tokens to Spotify | **High.** A new acquirer was just added, and its product overlaps the orchestration value proposition | https://www.checkout.com/newsroom/checkout-com-announces-strategic-partnership-with-spotify-to-power-efficient-scalable-payments-globally |
| 2 | May 2025 | Apple's US rules change after the Epic injunction; Spotify adds external web-checkout links in its US iOS app | Medium. It raises the importance of web checkout (US only) | [20-F](https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm); [TechCrunch](https://techcrunch.com/2025/05/21/spotify-says-support-for-external-payments-on-ios-has-already-boosted-subscriptions) `[UNVERIFIED — search summary only]` |
| 3 | Aug–Sep 2025 | Price increases in India (Individual ₹119→₹139) and the Philippines (₱149→₱169) | Low. The PH prices match the live page | https://www.fonearena.com/blog/460914/spotify-premium-price-hike-india-august-2025.html · https://unbox.ph/news/spotify-price-hike-2025/ `[UNVERIFIED — search summary only]` |
| 4 | FY2025 / H1 2026 | Payment processing fees rose €34M YoY in FY25 and €16M YoY in H1'26, inside Premium cost of revenue (the total is not disclosed) | Medium. Fees are a disclosed cost line Spotify tracks | [20-F](https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm) · [Q2'26 6-K](https://www.sec.gov/Archives/edgar/data/1639920/000162828026052543/spot-20260630x6xk.htm) |
| 5 | Mar 2022 | Spotify was Google's launch partner for Play User Choice Billing | Low/background. No current APAC market list found | https://9to5google.com/2022/03/23/google-play-user-choice-billing-spotify/ `[UNVERIFIED — search summary only]` |

**Provider removals:** none confirmed. The FY2025 20-F stops naming Adyen and PayPal, but that is a disclosure change, not a confirmed removal.

---

### Section 8: Checkout Experience Audit

*Full checkout flow not accessible (it sits behind login). Findings are limited to publicly observable elements on Spotify's Premium and help pages.*

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | Custom-built, using Spotify's own Payment SDK (assets on `paymentsdk.spotifycdn.com`) | N/A | In-house |
| Guest checkout | Not available; a Spotify account is required | N/A | Normal for subscriptions |
| Steps to complete payment | Not observable | — | — |
| Card input experience | Not observable | — | Checkout.com/Adyen tokenisation is likely `[INFERENCE, not confirmed]` |
| Payment methods visible | Logo strips by market (Section 4); UPI flows adapt to the device (Intent on Android, Collect on iOS, QR on desktop) | Good | The device-aware UPI handling is notably mature |
| Location-based method display | Yes. Methods differ by country page | Good | — |
| Instalment / EMI options | Not found. Low relevance at a ₹139–₹299 monthly price | N/A | — |
| 3DS implementation | Checkout.com "Authentication services" in use | Not observable directly | — |
| PCI indicator | Spotify runs its own PCI DSS scope with annual external audits (FY2025 20-F) | — | See Section 9 |
| Mobile responsiveness | Not assessed. iOS in-app purchase is blocked, so iOS users are sent to web | — | — |
| Multi-currency / local pricing | Local-currency pricing (₹, ₱, Rp, etc.) and 2-month trials | Good | — |
| Saved payment methods | Not observable | — | — |
| Error message clarity | Help pages are detailed: a bank list for India recurring, and a 24–48h guidance note for UPI | Fair | The need for these pages is itself a friction signal |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not stated. The FY2019 20-F said "fully compliant with… PCI DSS v3.2.1". The FY2025 20-F describes "an external audit of our systems and environments in scope for PCI DSS, including an external penetration test, on an annual basis" | [FY2019 20-F](https://www.sec.gov/Archives/edgar/data/1639920/000156459020004357/ck0001639920-20f_20191231.htm), [FY2025 20-F](https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm) |
| Card data handling | Spotify has its own in-scope cardholder-data environment; "Spotify never stores your full card number" (privacy policy) | [privacy policy](https://www.spotify.com/us/legal/privacy-policy/) |
| Recommended Yuno integration | Back-to-back API, given the in-house Payment SDK and PCI environment | `[INFERENCE, not confirmed]` |

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: India recurring is supported but fragile**
> **Evidence:**
> - S4: UPI Autopay is supported, but card recurring works only at a published bank list, with prepaid offered as the workaround ([failed-payment](https://support.spotify.com/in-en/article/failed-payment/)).
> - S5: a verified UPI Autopay "charged in GPay, failed in Spotify" thread ([community](https://community.spotify.com/t5/Subscriptions/Spotify-showing-payment-failed-while-GPay-shows-autopay-success/m-p/7065132)), plus Spotify's own "wait 24-48 hours" guidance.
> - S12: India subscription income grew +88.8% in FY25.
>
> **Pain Point:** Involuntary churn and support load on India's fastest-growing revenue line. Grace-period subscribers are counted as Premium for up to 30 days after a failed payment (20-F).
> **Yuno Value Proposition:** Local recurring-rail handling (UPI Autopay mandates, RBI e-mandate card flows) and mandate-status reconciliation through one integration, with failover between Indian PA/PGs.
> **Best Success Case:** No verified Yuno case. Pull one from the current case library before use.
> **Outreach Angle:** "Your India help pages carry a bank-by-bank list of which cards can renew. Curious how much of India's renewal volume ends up on prepaid or in the grace period because of it."
> **Suggested Subject Line:** India renewals: the bank list on your help page

> **Insight #2: A new global acquirer doesn't settle local-rail coverage in SEA**
> **Evidence:**
> - S3: Checkout.com was signed in Feb 2026 for global acquiring.
> - S3: no processor is named for GCash (PH), GoPay (ID) or UPI (IN).
> - S4: QRIS (ID) and PayNow (SG) are not found, and Maya (PH) is unverified.
> - S5: GCash failures are visible in the Philippines (summary-level).
> - S2: users in the Philippines contract with Spotify AB.
>
> **Pain Point:** Local wallets and A2A rails sit on separate, market-by-market integrations next to the global acquirer.
> **Yuno Value Proposition:** One integration for SEA wallets and QR rails, next to (not instead of) the existing acquirers.
> **Best Success Case:** No verified Yuno case. Pull one from the current case library before use.
> **Outreach Angle:** "Checkout.com covers cards globally; I'm curious who carries GCash and Indonesian wallets for you, and whether that's one integration or several."
> **Suggested Subject Line:** Who carries GCash for Spotify?

> **Insight #3: The in-house team already believes in orchestration, so pitch reach and opportunity cost**
> **Evidence:**
> - S3B: the in-house Global Payments team runs a platform across PSPs and APM providers.
> - S6: a dedicated JAPAC payments structure works on "local PA/PG and issuer set ups".
> - S1: Rest of World is the fastest-growing MAU region (+21% YoY).
>
> **Pain Point:** Each new APAC rail or PA/PG is engineering time taken from a central team serving every business line.
> **Yuno Value Proposition:** Extend the in-house layer with pre-built APAC connections rather than replace it.
> **Best Success Case:** None verified.
> **Outreach Angle:** For the JAPAC payments lead only: how they prioritise new local integrations against central platform roadmap capacity.
> **Suggested Subject Line:** JAPAC rails vs central roadmap

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. Your India failed-payment page lists, bank by bank, which Visa and Mastercard cards can auto-renew. That is a lot of renewal logic to maintain by hand.
2. Spotify India's subscription income grew 88.8% in FY25 ([Storyboard18](https://www.storyboard18.com/how-it-works/spotify-india-turns-profitable-in-fy25-as-subscriptions-surge-and-marketing-costs-shrink-86189.htm)), so every point of UPI Autopay reliability now compounds.
3. You run UPI three ways (Intent, Collect, QR) depending on device. Few global subscription merchants get that far in India.

**Cold call openers (conversational, one sentence each):**
1. "I saw the Checkout.com announcement in February. I'm curious how far that reaches into the local wallets in Southeast Asia."
2. "Your India help page tells users to wait 24 to 48 hours when a UPI payment doesn't activate Premium. Is reconciliation something the JAPAC team is working on?"
3. "Who owns new local payment rails for APAC: the Mumbai/Singapore team, or the central platform in Stockholm?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| JioSaavn | jiosaavn.com | India (Reliance) | Not verified | India + diaspora | TAL says Juspay; **no supporting evidence** | TAL row only |
| Gaana | gaana.com | India (Times Internet) | Not found | India | Paytm + Juspay for UPI AutoPay (NPCI, 2021) `[UNVERIFIED — search summary only]` | https://www.npci.org.in/PDF/npci/press-releases/2021/NPCI-Press-Release-UPI-AutoPay-goes-live-on-Gaana.pdf |
| KKBOX (KKCompany) | kkbox.com | Taiwan | 2024 revenue ~US$114.8M `[UNVERIFIED]` | TW, HK, JP, SG, MY | Not found | https://interspacemusic.com/blog/kkbox-owns-60-of-taiwan-streaming-most-distributors-never-deliver-to-it/ |
| JOOX (Tencent Music) | joox.com | Hong Kong / Shenzhen | Not found | HK, SEA | Fortumo carrier billing in ID (2018) `[UNVERIFIED]` | https://teknologi.bisnis.com/read/20180207/105/735586/langganan-joox-cukup-potong-pulsa |
| Melon (Kakao) | melon.com | South Korea | Not found | KR | Not found | TAL row |
| Genie Music (KT) | genie.co.kr | South Korea | Not found | KR | Not found | TAL row |
| Deezer | deezer.com | France | ~10M subscribers | Global (out of territory) | **Adyen**, partner for ~10 years (verified) | https://www.adyen.com/fr_FR/ressources/flow-paiement-deezer |
| Anghami | anghami.com | Abu Dhabi (out of territory) | — | MENA | Checkout.com, sole card partner from 2020 (verified) | https://www.checkout.com/case-studies/anghami-improved-payment-bring-freedom-of-music |

Resso is defunct (exited India Jan 2024; TikTok Music closed Nov 2024 `[UNVERIFIED]`), so it is excluded.

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Netflix | netflix.com | SVOD | Global, IN/KR/JP | In-house commerce platform; Visa/MC + UPI AutoPay only in India | `2-ready-to-outreach/netflix.md` |
| JioHotstar | jiohotstar.com | OTT | India | PhonePe PG for UPI AutoPay on RuPay credit `[UNVERIFIED]` | https://www.phonepe.com/press/phonepe-pg-rupay-and-jiohotstar-collaborate-to-simplify-subscription-payments-with-upi-autopay/ |
| SonyLIV | sonyliv.com | OTT | India | Razorpay for UPI AutoPay per NPCI; the TAL's Juspay conflicts with this `[UNVERIFIED]` | `2-ready-to-outreach/netflix.md` |
| Viu | viu.com | OTT | SEA, MENA | No orchestrator; Coda in ID/PH, carrier billing | `2-ready-to-outreach/viu.md` |
| Vidio | vidio.com | OTT | Indonesia | Fortumo carrier billing (2019) | https://www.thefastmode.com/technology-solutions/15607-indonesias-ott-platform-vidio-launches-direct-carrier-billing-with-fortumo |
| Pocket FM | pocketfm.com | Audio | India, US | Stripe for US/EU/LatAm (verified); Juspay for India (case study now 404s) | https://stripe.com/customers/pocket-fm |
| Kuku FM | kukufm.com | Audio | India | Razorpay per its FAQ; the TAL's Juspay is contradicted | `2-ready-to-outreach/storytv.md` |

#### 11C. Companies Recently Adopting Payment Orchestration

*No public case studies found of direct music/audio-streaming competitors adopting payment orchestration.*

Nearest streaming findings already in this repo: ELEVEN Sports and Setplex on Gr4vy, and YuppTV on Juspay (see `yupptv.md`). These are video/OTT, not music.

#### 11D. Prospect Scoring

Not scored line by line. For every competitor above, the only signals available are TAL rows or search summaries, and the matrix awards points only for verified signals. Scoring them now would produce numbers built on unverified inputs.

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Gaana | Competitor | India | Not scored | Check stage | **TAL stage "Reengage"**: per the TAL notes, a 26 Aug conversation agreed to re-engage in a month. That date has passed | Yes |
| 2 | JioSaavn | Competitor | India + diaspora | Not scored | — | Diaspora billing; TAL's Juspay unverified | Yes |
| 3 | KKBOX | Competitor | TW, HK, JP, SG, MY | Not scored | — | Multi-market North Asia + SEA | Yes |
| 4 | JOOX | Competitor | HK, SEA | Not scored | — | Multi-market SEA | Yes |
| 5 | Pocket FM | Peer | India, US | Not scored | — | Stripe abroad + India rails | Yes |
| 6 | Kuku FM | Peer | India | Not scored | — | Razorpay single-PSP (FAQ) | Yes |
| 7 | Hungama | Competitor | India | Not scored | — | TAL Juspay (unverified) | Yes |
| 8 | Genie Music | Competitor | KR | Not scored | — | — | Yes |
| 9 | Melon | Competitor | KR | Not scored | — | — | Yes |
| 10 | Vidio | Peer | ID | Not scored | — | Carrier billing; ID wallets | Yes |

**No strong prospect outside the TAL was identified.** Deezer and Anghami are out of territory.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | €17,186M FY2025 (reported in EUR; not converted) | [20-F](https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm) |
| Latest quarter | Q2 2026: €4,777M revenue (Premium €4,331M), +14% YoY | [Q2'26 6-K](https://www.sec.gov/Archives/edgar/data/1639920/000114036126031044/ef20078867_ex99-1.htm) |
| India entity revenue | Spotify India LLP FY25 (to Mar 2025): ₹513.77 crore revenue from operations; subscription income ₹316.83 crore | [Storyboard18](https://www.storyboard18.com/how-it-works/spotify-india-turns-profitable-in-fy25-as-subscriptions-surge-and-marketing-costs-shrink-86189.htm) |
| GMV / Gross Transaction Volume | Not disclosed | — |
| Average Transaction Value | Premium ARPU €4.89/month (Q2'26). Live list prices: IN ₹139 (Standard), PH ₱169, ID Rp 59.900 per month | [Q2'26 6-K](https://www.sec.gov/Archives/edgar/data/1639920/000114036126031044/ef20078867_ex99-1.htm); spotify.com/{in-en,ph-en,id-en}/premium |
| Est. Annual Transactions | >1 billion payments a year | [lifeatspotify.com](https://www.lifeatspotify.com/find-your-team/job-categories/payments) |
| **Monthly transaction count** | **✅ SOURCED: >83M/month.** "Spotify processes more than a billion payments annually" ([lifeatspotify.com](https://www.lifeatspotify.com/find-your-team/job-categories/payments), fetched 2026-10-19, page undated). **Billing unit:** any payment across all Spotify business lines, dominated by Premium monthly renewals. It excludes partner-billed (telco) and, almost certainly, Google Play-billed subscriptions. | Direct statement |
| Active Customers / Users | 777M MAUs; 300M Premium subscribers (Q2 2026) | [Q2'26 6-K](https://www.sec.gov/Archives/edgar/data/1639920/000114036126031044/ef20078867_ex99-1.htm) |
| Primary Currency | EUR reporting; local-currency pricing per market | 20-F |
| Top 3 Markets by Revenue | US is €1,734M of €4,777M in Q2'26; no other single country is ≥10% | [Q2'26 interim 6-K](https://www.sec.gov/Archives/edgar/data/1639920/000162828026052543/spot-20260630x6xk.htm) |
| Billing channel split (web vs app store) | **Not disclosed.** Premium is "primarily sold directly to end users", with additional sales through telco partners, Google Play IAP and prepaid code vendors. iOS IAP is not offered. Direct web is clearly the majority, but **no percentage is sourced** | [20-F](https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm), [support](https://support.spotify.com/in-en/article/cant-subscribe-to-premium-in-the-ios-app/) |
| Payment processing fees | Total not disclosed; +€34M YoY in FY25, +€16M YoY in H1'26 | 20-F; Q2'26 6-K |

**App-store check:** this account passes. App-store billing does **not** dominate: iOS IAP is not offered at all, and Google Play is one option among several. The override is driven by in-house sophistication and a fresh PSP decision, not by app-store exposure.

---

### Overall Research Confidence

**Medium-High.**
- **Traffic was supplied** (Similarweb Sales Intelligence, top 10 only, web only).
- **Strong:** entities, financials and payment-fee disclosure (SEC primary sources), PSP stack (Checkout.com primary release and historic 20-F disclosures), orchestration classification (Spotify's own careers page), and methods per market (Spotify's own help and Premium pages).
- **Limited:**
  - checkout itself, which sits behind login;
  - which processor carries UPI, GCash and GoPay;
  - complaint frequency, where most threads are search-summary-only and dates are unclear;
  - whether Adyen is still current;
  - the PH, ID, AU, NZ and TH method lists, where the logo strip did not render.

---

### Manual Research Recommendations

> **Area:** Account ownership
> **Why it matters:** The global payments leadership (VP Global Head of Payments) sits outside APAC, and a JAPAC payments lead exists. A cold APAC sequence risks colliding with enterprise coverage.
> **Suggested manual action:** Confirm ownership with your manager. If APAC is cleared, find the current "Payments Associate Director, JAPAC" and the India payments lead on LinkedIn (via Chief).

> **Area:** UPI / GCash / GoPay processors
> **Why it matters:** The entire APAC angle is local-rail depth. If Checkout.com already carries these rails, Insight #2 weakens.
> **Suggested manual action:** On a logged-in IN and PH test account, inspect network requests during UPI and GCash checkout. Also check NPCI's UPI Autopay live-merchant announcements for Spotify.

> **Area:** Complaint frequency (India UPI Autopay, PH GCash)
> **Why it matters:** It decides whether the reliability angle is real or anecdotal.
> **Suggested manual action:** Skim r/india, r/Philippines and Play Store reviews (filter: "payment") for the last 6 months.

> **Area:** Q3 2026 results (22 Oct 2026)
> **Why it matters:** They may include new payment-fee or regional commentary.
> **Suggested manual action:** Re-check the shareholder deck after release.

---

### Appendix: All Source URLs

**Traffic:** `accounts/traffic/spotify.md` (Similarweb, supplied 2026-10-19)

**Phase 0 / Entities / Financials**
- https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm
- https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/spot-20251231xexx81.htm
- https://www.sec.gov/Archives/edgar/data/1639920/000114036126031044/ef20078867_ex99-1.htm
- https://www.sec.gov/Archives/edgar/data/1639920/000162828026052543/spot-20260630x6xk.htm
- https://www.spotify.com/in-en/legal/end-user-agreement/ · https://www.spotify.com/ph-en/legal/end-user-agreement/ · https://www.spotify.com/jp/legal/end-user-agreement/ · https://www.spotify.com/au/legal/end-user-agreement/
- https://www.storyboard18.com/how-it-works/spotify-india-turns-profitable-in-fy25-as-subscriptions-surge-and-marketing-costs-shrink-86189.htm
- https://www.musicbusinessworldwide.com/spotify-hits-300-million-premium-subscribers-in-q2-202/
- https://www.thecompanycheck.com/company/spotify-india-llp/AAP-6218 · https://www.infyner.com/company/spotify/U74999MH2017FTC295679 · https://www.ibisworld.com/australia/company/spotify-australia-pty-ltd/521677/ · https://recordowl.com/company/spotify-singapore-pte-ltd (all search-summary only)
- https://y.uno/en (Yuno customer check)

**PSP / Orchestration / PCI**
- https://www.checkout.com/newsroom/checkout-com-announces-strategic-partnership-with-spotify-to-power-efficient-scalable-payments-globally
- https://fintechnews.sg/125579/payments/checkout-com-spotify/
- https://www.sec.gov/Archives/edgar/data/1639920/000156459020004357/ck0001639920-20f_20191231.htm
- https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/ck0001639920-20221231.htm
- https://www.adyen.com/sv_SE/kunskapshubb/fem-tips-om-betalningar-fran-spotify
- https://thepaypers.com/payments/news/spotify-partners-fortumo-to-expand-carrier-billing-availability-in-asia
- https://paymentsdive.com/ex/mpt/news/boku-provides-direct-carrier-billing-in-japan-for-spotify
- https://www.lifeatspotify.com/find-your-team/job-categories/payments
- https://nordicapis.com/sessions/spotify-payments-creates-apis-manage-complexity/ (not fetched)
- https://www.spotify.com/us/legal/privacy-policy/

**Methods**
- https://support.spotify.com/in-en/article/paying-for-spotify-with-upi/
- https://support.spotify.com/in-en/article/failed-payment/
- https://support.spotify.com/in-en/article/google-play-help/
- https://support.spotify.com/in-en/article/cant-subscribe-to-premium-in-the-ios-app/
- https://support.spotify.com/{in-en,ph-en,id-en,jp,au,nz,my-en,th-en,sg-en,kr-en,tw,hk-en,vn-en}/article/payment-methods/
- https://support.spotify.com/{ph-en,id-en,jp,au,my-en,th-en,sg-en,kr-en,tw}/article/mobile-billing-payments/
- https://support.spotify.com/id-en/article/pay-as-you-go/
- https://www.spotify.com/{in-en,ph-en,id-en,jp,kr-en,my-en,vn-en,sg-en,tw,hk-en}/premium/
- https://community.spotify.com/t5/Subscriptions/Paying-with-Gcash/m-p/7161068
- https://inet.detik.com/cyberlife/d-5154295/bayar-spotify-premium-kini-bisa-pakai-gopay
- https://unbox.ph/news/spotify-introduces-premium-mini-for-the-philippines/

**Complaints / News / Corporate**
- https://community.spotify.com/t5/Subscriptions/Spotify-showing-payment-failed-while-GPay-shows-autopay-success/m-p/7065132
- https://community.spotify.com/t5/Subscriptions/UPI-Autopay-charged-me-but-Spotify-says-payment-failed/m-p/6106214
- https://community.spotify.com/t5/Premium-Student/UPI-AUTOPAY-FAILED/td-p/6935183
- https://community.spotify.com/t5/Subscriptions/GCash-payments-keep-failing/td-p/6399186
- https://community.spotify.com/t5/Subscriptions/Premium-Duo-cannot-take-GoPay-Payement/m-p/5415628
- https://www.musicbusinessworldwide.com/spotify-bundles-three-months-of-premium-with-vodafone-ideas-postpaid-plans-in-its-first-indian-telco-partnership/
- https://techcrunch.com/2025/11/13/spotify-introduces-a-premium-platinum-plan-with-lossless-access-in-five-markets/
- https://techcrunch.com/2025/05/21/spotify-says-support-for-external-payments-on-ios-has-already-boosted-subscriptions
- https://newsroom.spotify.com/2025-09-30/spotify-announcement-daniel-ek-executive-chairman/
- https://www.fonearena.com/blog/460914/spotify-premium-price-hike-india-august-2025.html
- https://unbox.ph/news/spotify-price-hike-2025/
- https://9to5google.com/2022/03/23/google-play-user-choice-billing-spotify/
- https://portfoliojobs.tcv.com/companies/spotify/jobs/40297684-payments-growth-optimisation-lead-india
- https://jobs.lever.co/spotify/973b0b71-e8d2-4d7d-9c4b-1c716bd45c8b
- https://jobs.lever.co/spotify/9fd98cde-6a1b-419c-a27a-daae7a7483f0

**Competitors / Peers**
- https://www.adyen.com/fr_FR/ressources/flow-paiement-deezer
- https://www.checkout.com/case-studies/anghami-improved-payment-bring-freedom-of-music
- https://www.npci.org.in/PDF/npci/press-releases/2021/NPCI-Press-Release-UPI-AutoPay-goes-live-on-Gaana.pdf
- https://interspacemusic.com/blog/kkbox-owns-60-of-taiwan-streaming-most-distributors-never-deliver-to-it/
- https://teknologi.bisnis.com/read/20180207/105/735586/langganan-joox-cukup-potong-pulsa
- https://www.phonepe.com/press/phonepe-pg-rupay-and-jiohotstar-collaborate-to-simplify-subscription-payments-with-upi-autopay/
- https://www.thefastmode.com/technology-solutions/15607-indonesias-ott-platform-vidio-launches-direct-carrier-billing-with-fortumo
- https://stripe.com/customers/pocket-fm

</details>
