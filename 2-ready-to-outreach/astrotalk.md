# Astrotalk

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 19 / 29 → ⭐ **High Priority**
**Industry:** Online astrology consultation marketplace — wallet recharge, per-minute chat/call · **HQ:** Noida, India — **Astrotalk Services Private Limited**, CIN **U72900PB2015PTC039357** (formerly Codeyeti Software Solutions) · **Researched:** 2026-10-03 · **First email sent:** —
**Motion:** **Greenfield** — single gateway, **Razorpay direct**, confirmed from Razorpay's own published pages. No orchestrator anywhere.

---

> ## 🎯 THE HOOK — their own gateway published the number
>
> **Verified by me**, fetched from `razorpay.com/blog/astrotalk-explores-global-payments-with-razorpay-international-payments/` (18,349 b, control 18 hits for "astrotalk"):
>
> > *"As the business broadened its global customer base across **70+ countries**, they started encountering issues like **payment failure and fraud**. Most existing options had **slow approval processes and low success rates**... Astrotalk needed a reliable payments solution with **high international success rates**."*
>
> > *"Razorpay's **consistent payment success rate of over 80%** demonstrated its commitment to providing a seamless payment experience."*
>
> > *"...a remarkable **92% win rate in fraudulent chargebacks**." · "Offering support for over **160 currencies**."*
>
> **Over 80% is published as the achievement on their international traffic.** Prateek is not attacking the incumbent — he is quoting them.
>
> ⚠️ **Phrase it exactly.** "Over 80%" is a floor, not a measurement. **Never say "one in five of your international payments fails."** The defensible form: *"your gateway publishes 'over 80%' as the result on your international traffic."*
>
> ### ⭐⭐ And the sharpest fact in the file — they already have a US card rail. It serves gemstones, not consultations.
> Probed directly from Shopify's own config endpoints:
> ```
> global.astrotalk.store/payments/config  → "shopifyPaymentsEnabled": true   countryCode US, USD
>                                            PayPal merchantId L3DDADV8K2YZL
>                                            Apple Pay (visa, mc, amex, discover, elo, jcb, 3DS)
>                                            Google Pay PRODUCTION · Shop Pay
> astrotalk.store/payments/config         → applePayConfig: null · shopifyPayConfig: null
> gemstones.astrotalk.store/payments/config  googlePayConfig: null · paypalConfig: null   (INR)
> ```
> **Their US gemstone store acquires domestically in the US with Shopify Payments, PayPal, Apple Pay, Google Pay and Shop Pay.** Their **consultation** business — the actual revenue engine — acquires the same US customers **cross-border from India via Razorpay**, with no entity outside India.
> **Their merchandise gets better acquiring than their core product.** Both halves from their own configuration.
>
> ### The structure underneath it
> **~22.7% of traffic is outside India — and there is no Astrotalk entity anywhere outside India.** Every non-India consultation card payment is a cross-border authorisation from an Indian entity against a foreign issuer — the highest-decline configuration available.
>
> ### And the timing
> **DRHP targeted mid-2026, listing late 2026 / early 2027.** A **first-ever CFO, Deepak Khetan** (ex-Edelweiss, GlobalBees, GLS Group), was hired specifically for *"financial strategy, risk management, regulatory processes, international expansion and IPO preparation."* **No payments hire exists** — so payment decisions almost certainly sit with that CFO. **Enter at CFO level on cost-of-payments and approval-rate leakage ahead of a prospectus**, not at payments-PM level. The window closes: pre-IPO companies freeze vendor changes.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Astrotalk is India's largest online astrology consultation marketplace — users recharge a wallet and spend it per-minute on chat and call consultations with ~20,000 astrologers on revenue share. FY25 total income **₹1,214 Cr (+85%)**, operating revenue ₹1,176 Cr, **adjusted PBT ₹285 Cr — profitable**, which is rare for an Indian consumer startup. Unicorn at **$1Bn** via an ESOP buyback rather than a raise. A separate e-commerce arm (gemstones, rudraksha) did **>₹140 Cr in CY2025, ~₹200 Cr ARR**.

**SimilarWeb:** supplied — `accounts/traffic/astrotalk.md`. India **77.30%** ▲15.58%, US 10.19%, UK 3.90% ▼34.62%, Canada 1.75%, Australia 0.84%, UAE 0.44%, Singapore 0.40%. ⚠️ Country-domains toggle **OFF**. ⚠️ **App recharges do not appear in SimilarWeb at all** — this table understates the business.

### ⭐ Five payment surfaces — verified by me, all HTTP 200
| # | Property | Platform | Identity | Country · currency | Checkout layer |
|---|---|---|---|---|---|
| 1 | **astrotalk.com** — consultations | Next.js + Turbopack, API `aws.astrotalk.com` | — | India | **Razorpay direct** |
| 2 | **astrotalk.store** | **Shopify** | `c839d4-19.myshopify.com` | IN · INR+USD | **GoKwik** |
| 3 | **gemstones.astrotalk.store** | **Shopify** | `astrotalk-gemstones.myshopify.com` | India | **GoKwik** |
| 4 | **global.astrotalk.store** | **Shopify** | **`astrotalk-usa.myshopify.com`** | **US · USD** | **NONE — plain Shopify** |
| 5 | **astrologer.astrotalk.com** | "Portal" | — | India | **Astrologer payouts — rail unknown** |

**Second observation, from their own markup:** GoKwik is live on both Indian Shopify stores (`gokwik-checkout`, `gokwik-buy-now`, `gokwik-widgets.js`, `gokwik.co`) and **entirely absent from the US store** — the market that is 10.19% of their web traffic. `c839d4-19.myshopify.com` is an **auto-generated Shopify handle**: a store spun up fast and never renamed.
*(A sixth property, `store.astrotalk.com`, surfaced unexamined.)*

### Billing channels
| Channel | Status |
|---|---|
| **Apple IAP** | ✅ **LIVE.** Verified by me on the US App Store — nine `Wallet Recharge` tiers: **$5 / $10 / $20 / $30 / $50 / $100 / $200 / $500 / $1,000**. India storefront ₹9,900. **Seller of record: Codeyeti Software Solutions Private Limited.** Apple takes 15–30% of every one |
| **Google Play Billing** | ⬜ **Probably NOT used, but not positively confirmed.** The Play listing carries **no in-app-purchase badge** — which argues against it. Independently, my own Play fetch returned price ranges belonging to **neighbouring apps in the similar-apps carousel**, not Astrotalk; a second agent hit the same trap and caught it the same way. **Do not cite those ranges, and do not assume parity with iOS** |
| **Direct gateway** | ✅ **Razorpay**, including **Razorpay International Payments** — "73 Countries", 160+ currencies, 92% chargeback win rate |
| **US Shopify store** | ✅ **Shopify Payments (US domestic) + PayPal + Apple Pay + Google Pay + Shop Pay** — probed directly |
| **Indian Shopify stores** | ✅ **GoKwik full suite** — KwikCheckout, KwikPass (phone/OTP login), KwikCart. `mid: "19pmjg24asf0"`, `environment: "production"`. **No Shopify-level wallet enabled at all.** The RBI-licensed aggregator settling behind GoKwik is **not publicly disclosed** |
| **Astrologer payouts** | ⬜ **₹511 Cr paid out in FY2024-25** across 13,000+ astrologers, weekly/bi-weekly, min ₹1,000, TDS deducted. **Rail not disclosed anywhere.** A half-billion-rupee disbursement book with no named provider |
| **Shopify estate** | ✅ Entirely outside app-store billing — ₹140 Cr CY2025 |

⇒ **This is NOT an app-store-trapped account.** Indian UPI/netbanking/cards cannot run through Apple or Google billing, and the e-commerce arm is wholly outside it. The unsized risk is the **iOS share**, which nobody discloses.

### Legal entities
- **Astrotalk Services Private Limited** — CIN **U72900PB2015PTC039357**, ROC Chandigarh, incorporated 01 Apr 2015, directors Puneet Gupta and Anmol Jain
- **Astrotalk Online Private Limited** — ⚠️ a candidate CIN exists (U62010UP2025PTC233801, 27 Sep 2025) but **its listed directors do not match the founders — low confidence, do not cite**
- Both named in the Terms of Usage at Flat No.713, Devika Tower 6, Nehru Place, New Delhi. Registered office is Bathinda, Punjab; **operating HQ is Noida — use Noida**
- ⚠️ **The two app stores name different entities.** Google Play's developer is **ASTROTALK SERVICES PRIVATE LIMITED** at the Bathinda, Punjab address matching CIN U72900PB2015PTC039357; **Apple still carries the pre-rename "Codeyeti Software Solutions Private Limited."**
- ❌ **No entity in the US, UK, Canada, Australia, UAE, Singapore or anywhere else.**

### Orchestration status
**None detected — direct Razorpay integration.** Razorpay's own case study and International Payments blog present it as *the* partner; no orchestrator, router or second PSP is named. **Greenfield.**
⚠️ **GoKwik** sits on the Indian Shopify stores as a checkout/COD-RTO layer — a separate estate, not an orchestrator on the consultation business. **GoKwik is not on the never-name list.**

### Buying signals
- 📈 **DRHP targeted mid-2026; listing late 2026 / early 2027**
- 💼 **First-ever CFO hired ahead of the IPO** — Deepak Khetan, brief explicitly includes regulatory processes and international expansion
- 🌏 **International live in Sri Lanka, Australia, US and UK, localisation in progress**; Razorpay cites **70+ countries**
- 🛍️ **E-commerce arm from zero to ₹140 Cr in CY2025** — launched Nov 2024 off a ₹30 lakh investment, now **~₹1 Cr daily GMV and 1.6 million orders in 2025**. A second payment estate built inside a year
- 📱 **Play Store: 100M+ downloads, 1.72M reviews, 4.8 stars**
- 💰 **Unicorn at $1Bn via ESOP buyback**, funded from profit

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Astrotalk`.*

⚠️ **Read before drafting.**
1. **Lead with Razorpay's published "over 80%".** Quote the gateway, not a benchmark. Never convert it into a failure rate.
2. **Enter at CFO level.** There is no payments owner. The DRHP is the context — approval-rate leakage and cost of acceptance in a prospectus year.
3. **Never name the incumbent orchestrators** — and note **Razorpay and Cashfree both suspended third-party orchestrator integrations in January 2025**. That is a real structural obstacle in India and Prateek should know it before the call, not during it.
4. **Do not use the refund complaints.** The *dominant* complaint theme is refund refusal and support stonewalling — **orchestration does not fix a refund policy**. Conflating the two is the easiest way to lose credibility here.
5. **Do use the reconciliation evidence** (below) — it is a different, defensible failure class.
6. **Do not mention Trustpilot's suppressed TrustScore or the removed fake reviews.** Context for us, never for a prospect.
7. **Gulf is EMEA.** UAE has the best engagement on the site (6.94 pages/visit) — flag it to them, do not pitch it.
8. ⛔ **Do NOT use the "40% higher than market success rates" figure.** It sits in Razorpay's generic product blurb, **not** in Astrotalk's results. Not attributable.
9. ⛔ **Do NOT use the reported "2,000 CAD charged instead of ₹2,000" incident.** The cited Voxya complaint was fetched and is a **different, redacted complaint about astrologer refunds** with no payment or currency detail. **The story is unsupported.**

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 19 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED: ~650,000–2,000,000 sessions/month.** FY25 operating revenue **₹1,176 Cr** (fetched, Outlook Business) ÷ **₹500–1,500 per user per session** (fetched, `astrotalk.com/pricing`: *"the range of transactions on our Android and iOS applications varies from INR 500 to 1500 per user per session"*) ÷ 12. **Both inputs sourced.** ⚠️ Payment count ≤ session count, since one recharge can fund several sessions — but even at a 5× discount this clears 100,000/month comfortably |
| Orchestration status | **+4** | ✅ **None detected — greenfield.** Razorpay direct, from Razorpay's own pages |
| 3+ countries | **+3** | ✅ India, US, UK, Canada all >1% traffic |
| Multiple PSPs | **+3** | ✅ **Three, evidenced by direct probe of Shopify's own config endpoint:** **Razorpay** (consultations) · **Shopify Payments** (US store, `"shopifyPaymentsEnabled": true`) · **PayPal** (US store, `merchantId L3DDADV8K2YZL`). Plus Apple IAP as a fourth billing channel. **They are not single-gateway — they are multi-gateway with no layer across any of it.** |
| Local rail / licensing gap in a top-3 market | 0 | ⬜ **Not established as a sourced absence.** The only granular India method list traces to a staging page that **503'd**, and `astrotalk.com/pricing` publishes no methods at all. UPI Autopay, e-mandate and RuPay are **NOT FOUND** — which for a recharge business is notable, but "not found" is not a source |
| Recent expansion | **+2** | ✅ International live in LK/AU/US/UK with localisation in progress; e-commerce arm to ₹140 Cr in CY2025 |
| Payment issues reported | **+2** | ✅ Moderate–high. See the reconciliation evidence below |
| Funding >$10M | 0 | ❌ The ~$20M round was 2024. The $1Bn unicorn mark came via an **ESOP buyback funded from profit**, not a raise |
| High traffic outside home | 0 | ❌ **India is 77.30%**, above the 60% threshold |
| Competitor using orchestration | 0 | ❌ **Verified absent.** No astrology, spiritual or per-minute consultation marketplace has a public orchestration case study — and the one record we held (InstaAstro/Juspay) **has been refuted**, see below |
| Payment job postings | 0 | ❌ None surfaced. ~11 open roles are Java, Android, UX and content |

**Tier:** ⭐ High Priority (17+).
> **Score moved 16 → 19** when the PSP agent probed Shopify's `/payments/config` directly and established three evidenced PSPs rather than one. Two remaining zeros are **structural, not weaknesses**: "traffic outside home" cannot fire because India-dominance *is* the business model, and "funding" cannot fire because they are profitable and do not raise. A third (local rail gap) is zero only because a staging page 503'd.

### ⭐ The reconciliation evidence — this is the usable complaint material
Trustpilot, **fetched**, 2 Sep 2026:
> *"transactions were even **declined by my bank yet still appeared as posted charges**"* · *"there are **NO transactions at all, yet they charged me**"*

**The merchant's ledger and the acquirer's ledger disagree.** A bank-declined transaction surfacing as a posted charge, and a charge with no matching in-app record, is a payment-status and reconciliation failure — not a support failure. Corroborated more weakly by Indian consumer-forum posts titled *"Money deducted but not credited into my wallet"* `[UNVERIFIED]`.

⚠️ **Honest counter-read:** by volume the dominant theme is **refund refusal and stonewalling**, which orchestration does not fix. Lead with the confirmed reconciliation wording; do not conflate.
⚠️ Trustpilot profile: 305 reviews, **55% one-star**, **TrustScore suppressed for a guidelines breach with fake reviews removed.** Internal context only.

### ⛔ A correction to our own repo, made during this run
`1-to-outreach/instaastro.md` carried *"Orchestrator on file: Juspay — if confirmed, this is a displacement motion... do not open with 'you have no orchestration'."* **That was wrong and the warning was backwards.** I fetched Razorpay's InstaAstro case study: **20 hits for "instaastro", ZERO for "juspay"**, no orchestrator named. A fetched Juspay customer list contains no astrology app. And **Razorpay and Cashfree both suspended third-party orchestrator integrations in January 2025**, the same month that case study published — a Juspay-fronting-Razorpay setup would have broken then. **The stub has been corrected to greenfield/Razorpay.**

⚠️ **And a distinction I nearly lost:** Razorpay's **Astrotalk** page says *"payment success rate of over 80%"*. Its **InstaAstro** page says *"supporting over **80% of InstaAstro's international transactions via cards**"* — **a share of volume, not a success rate.** Same number, different metrics. Do not merge them.

### Competitors — and four genuine prospects
| Company | HQ | Scale | PSP | Prospect? |
|---|---|---|---|---|
| **InstaAstro** | Gurugram | FY26 ₹111 Cr, $12M Series A, 25% intl, 183 countries | **Razorpay — confirmed, single gateway, >80% of intl card volume** | ⭐ **Best in set.** Already in `1-to-outreach/` |
| **AppsForBharat / Sri Mandir** | Bengaluru | FY25 ₹82.2 Cr (+341%), ₹175 Cr Series C | Not found | ⭐ **Overseas ARPU ~₹7,000 vs ₹600–800 domestic** on ~90k of 3.5M MAU — their most valuable users are their hardest to approve. Sharpest hook in the sweep |
| **Astroyogi** (Netway India) | India | ~₹96 Cr FY25, **bootstrapped and profitable** | Not found | 🟢 Bootstrapped ⇒ MDR is a real line item. Lead on cost, not growth |
| **AstroSage** | Noida | ₹84 Cr FY25 (+40%), unfunded since 2004 | Not found | 🟢 Confirm it runs a paid per-minute marketplace first |

**None are in `accounts/apac-tal.csv`.** Clickastro (report sales, not a marketplace), Bodhi and Anytime Astro are sub-scale — park them.
⚠️ Correction to my own brief: **Bodhi is not a ShareChat/Moj company** — independent, Ghaziabad, seed-stage.

### 🛑 Structural obstacle Prateek should know before the call
**Razorpay (Optimizer) and Cashfree (FlowWise) now ship their own orchestrators, and both suspended third-party orchestrator integrations in January 2025** (PhonePe did the same in Dec 2024). In India the incumbent gateway is simultaneously the competitor and the gatekeeper. Sourced to Inc42, Entrackr and YourStory `[UNVERIFIED — search summaries]`. This is not a reason not to pitch; it is a reason not to be surprised.

### Regulatory note — flagged, not asserted
Astrotalk's "Service Credits" are a closed-loop stored-value product, and closed-loop instruments generally need no RBI authorisation **provided there are no third-party payments**. But credits are spent on consultations delivered by ~20,000 independent astrologers on revenue share, whom Astrotalk pays out. **Whether the regulator treats Astrotalk as principal or as a marketplace settling to third parties is not resolvable from public sources.** No RBI communication, filing or reporting found on this point. **Do not assert either answer.** Their T&Cs do confirm a **two-tier ledger** — "Real Service Credits" vs "Virtual Service Credits" — and dual credit ledgers are where reconciliation and revenue-recognition pain lives, which matters more than usual in a DRHP year.

### Four disconnected payment stacks — the structural picture
1. **Razorpay** — consultations, web and Android, domestic and international
2. **Apple IAP** — iOS consultations, nine USD tiers to $1,000, Apple's acquiring at 15–30%
3. **GoKwik + an undisclosed Indian aggregator** — the two INR Shopify stores
4. **Shopify Payments + PayPal + Apple/Google/Shop Pay** — the US Shopify store

**No unifying layer across any of them.** Plus a fifth flow, astrologer payouts, with no disclosed rail at all.

### Useful quotes from the Razorpay case study (fetched)
- **Puneet Gupta, Founder & CEO:** *"It was one of the best onboarding experiences we had ever had with any third party provider. Just one line of code made us go live."*
- **Anmol Jain, CBO:** *"Razorpay is one of the best when it comes to protecting merchants from fraudulent chargebacks. We see **significantly better win rates at Razorpay compared with other payment providers**."*
  ⇒ **They benchmark providers against each other.** That is a buyer who will entertain a comparison — useful framing, and it reads retrospective rather than current.
- Published headline: *"Business Expansion in over **73 Countries**"* (the blog says 70+; minor inconsistency in their own material).

### Section 12 — Business Case Data
| Metric | Value | Source |
|---|---|---|
| FY25 total income | **₹1,214 Cr (+85%)** | Outlook Business (fetched) |
| FY25 operating revenue | **₹1,176 Cr** | same |
| FY25 adjusted PBT | **₹285 Cr** | same. ⚠️ *Adjusted* — excludes a ~₹120 Cr employee one-off and a ~₹80 Cr non-cash CCPS mark-to-market |
| ⚠️ Conflicting figures | Entrackr reports **₹1,182 Cr / >₹250 Cr**. Close but unreconciled — **use one set, don't mix** | Entrackr |
| E-commerce arm | **>₹140 Cr CY2025, ~₹200 Cr ARR** | Entrackr |
| Average session spend | **₹500–1,500 per user per session** | `astrotalk.com/pricing` (fetched) |
| **Monthly transaction count** | ✅ **DERIVED ~650k–2.0M sessions/month** — see the ICP row for the arithmetic and the payment-vs-session caveat | — |
| Billing channel split (web vs app store) | ❌ **No public information found.** The single biggest open question | — |

### Overall Research Confidence
**MEDIUM–HIGH.** The gateway, billing channels, property estate, financials and corporate timing are all well sourced — several verified by me directly (the Razorpay blog, both App Store storefronts, all five properties, the Shopify and GoKwik configuration). **Two real caps:** the India payment-method list rests entirely on a staging page that 503'd, so no production page confirms any specific Indian method; and the **web-vs-app-store revenue split is undisclosed**, which caps any sizing.

### Manual Research Recommendations
> **Area:** Walk a real recharge on `astrotalk.com` and in the Android app. **Why:** settles UPI Autopay, RuPay, tokenisation, min/max recharge, and whether Google Play Billing is in play. **Action:** DevTools from an Indian IP, plus one Android install.

> **Area:** Web vs app-store revenue split. **Why:** it is the only thing standing between this and a sized business case. **Action:** discovery question — it will not be found publicly.

> **Area:** The astrologer payout rail (`astrologer.astrotalk.com`). **Why:** ~20,000 payees on revenue share is half the payment estate and nothing public describes it. **Action:** discovery question.

> **Area:** `astrotalk.com/refund-and-cancellation-policy` and `store.astrotalk.com`. **Why:** a reported ₹100 refund processing fee compounds the reconciliation complaints; the sixth property is unexamined. **Action:** two fetches.

</details>
