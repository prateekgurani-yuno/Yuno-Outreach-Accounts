# InstaAstro

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 16 / 29 → 🟢 **Medium** *(re-scored from 18 ⭐ by analyst audit — see the breakdown)*
**Industry:** Online astrology & spiritual-wellness consultation marketplace — wallet top-up, per-minute chat/call · **HQ:** **Noida, Uttar Pradesh, India** — **InstaAstro Technology Private Limited**, CIN **U72900UP2021PTC145574** · **Researched:** 2026-10-12 · **First email sent:** —
**Motion:** **Greenfield** — single gateway, **Razorpay direct**, independently re-verified this run. No orchestrator found anywhere.

---

> ## 🎯 THE SPINE — funded to expand internationally, on a card-only international rail
>
> Three facts, each sourced, that only mean something together:
>
> **1. They raised US$12M on 27 August 2026 and named international expansion as the use of proceeds.** Series A led by **Singularity AMC** and **Artha Venture Fund**, founders participating. Proceeds earmarked for *"expansion across regional and international markets"*, AI (sentiment analysis, multilingual), Pooja Seva and spiritual commerce. — [Entrepreneur India](https://india.entrepreneur.com/business-news/instaastro-crosses-inr-200-crore-in-annualized-revenue-raises-usd-12-million-series-a) · [Indian Startup News](https://indianstartupnews.com/funding/online-astrology-and-spiritual-wellness-platform-instaastro-raises-12-million-in-series-a-funding-12443449) · [Inc42](https://inc42.com/buzz/instaastro-bags-12-mn-to-build-ai-tools-expand-online-pooja-services/) — all three fetched.
>
> **2. Their own gateway published that cross-border payments were the problem.** Razorpay's InstaAstro case study, re-fetched this run: *"**Payment failures were a major hurdle.** For users eager to continue their spiritual consultations, any failed transaction led to a potential loss of engagement."* — across *"**North America, European, SEA, and the MENA region**"*. — https://razorpay.com/blog/razorpay-supercharged-instaastros/
>
> **3. Their own Terms say the only way to put money in is cards, net banking or UPI.** Verbatim, fetched: *"All payments for accessing Paid Services on the Website **must be made exclusively through the Registered Member's InstaAstro Wallet**, linked to their account. To add funds to this Wallet, the Registered Member **must use valid banking methods such as debit/credit cards, net banking, or UPI**."* — https://instaastro.com/terms-and-conditions/
>
> **Net banking and UPI are India-only domestic rails.** So for the ~25% of revenue that comes from outside India — their own figure, *"driven largely by the Indian diaspora"* — **a card is the only way to pay.** No PayPal, no Apple Pay, no Google Pay, no ACH, no Interac, no BECS/PayTo, no iDEAL. And Razorpay's page confirms the consequence: *"By supporting over **80% of InstaAstro's international transactions via cards**, Razorpay is helping InstaAstro cater to users worldwide."*
>
> ⚠️ **Phrase that number correctly.** "Over 80% of international transactions **via cards**" is a **share of volume, not a success rate.** Razorpay's separate *Astrotalk* page carries a *"consistent payment success rate of over 80%"* line. **Two different metrics that happen to share the number 80. Never conflate them, and never say "one in five of your international payments fails."** The defensible form: *"your gateway's own page says cards carry over 80% of your international volume."*
>
> ### ⭐⭐ The sharpest single finding — unlike their closest competitor, 100% of this revenue is orchestrable
> Probed directly from Apple's own product-page JSON on **both** the US and India storefronts:
> ```
> "bundleId":"com.instaastro.onlineastrology"  →  "hasInAppPurchases": false, "hasExternalPurchases": false
> ```
> **Control, in the same payload:** `codeyeti.com.AstroYeti` (**Astrotalk**) `true` · `com.at.pooja` `true` · `com.melooha.app` `true` · `com.itl.tarot` `true` · `com.answer.light` `true` · `com.jaanemann` `true`.
> The zero is a **real negative validated against six known positives in the same document**. The Google Play listing likewise carries **no in-app-purchase badge** for InstaAstro while its carousel neighbours do.
> ⇒ **InstaAstro does not bill through Apple IAP.** Wallet top-ups on both platforms run through their own gateway. **This account is NOT app-store trapped** — which is the opposite of Astrotalk, where Apple IAP is live and takes 15–30% of every iOS recharge. **The entire payment estate is addressable.**
>
> ### And the balance sheet says cost of payments is a live P&L line, not a nice-to-have
> MCA-derived FY25 movements, fetched: **Total Revenue ↗108.34%**, but **EBITDA ↘65.20%**, **Net Profit ↘67.93%**, **Networth ↘215.33%** (i.e. into negative) and **Borrowings ↗599,900%**. — https://www.falconebiz.com/company/INSTAASTRO-TECHNOLOGY-PRIVATE-LIMITED-U72900UP2021PTC145574
> **They doubled revenue in FY25 while profit collapsed and net worth went negative, financed by new borrowing.** The Series A is as much balance-sheet repair as growth capital. A company in that position hears "approval rate" and "MDR" as P&L, not as a technology conversation.
> ⚠️ Absolute values are paywalled on that source; only the percentage movements are visible. Treat as directional.
>
> ### ⛔ The one thing that could sink this account
> **Monthly transaction count is an ASSUMPTION, not a measurement**, and at a plausible average top-up value it lands near the 40,000/month ICP floor. **Average top-up value was not found anywhere.** See the ICP row and Section 12 — this is the first discovery question, ahead of everything else.

---

> ## 🔍 ANALYST AUDIT — Prateek, 2026-10-12
>
> I verified the load-bearing claims against live sources rather than accepting them, and scanned the site myself **before** reading the report so my baseline was not anchored on its conclusions. **The ICP moved from 18 ⭐ to 16 🟢.** Three rows changed; two down, one up.
>
> ### ✅ Confirmed first-hand
> - **⭐ THE APP-STORE QUESTION — confirmed, with a clean control.** Apple's embedded product JSON, paired to bundleId (never to a loose flag): **`com.instaastro.onlineastrology` → `hasInAppPurchases: false`**, and **`codeyeti.com.AstroYeti` (Astrotalk) → `true`**. InstaAstro reads `false` even where it appears as a *neighbour inside Astrotalk's own carousel*, and Astrotalk reads `true` on its own page. That cross-page consistency is a genuinely strong validation. **InstaAstro is NOT app-store trapped; its largest competitor is.** This is the single most important finding in the account and it holds.
> - **⭐ The funding round, fully verified.** Inc42, `datePublished 2026-08-27`: *"InstaAstro has raised $12 Mn (about ₹114.5 Cr) in a Series A funding round led by Singularity AMC and Artha Venture Fund, with founder Nitin Verma and Artha managing partner Anirudh Damani also participating in their personal capacities."* Use of proceeds verbatim: *"expand across regional and international markets, strengthen its pooja seva offerings, and grow its product business"*, plus AI-led product development. **Six weeks before report date, so the +2 fires correctly.** And the run was right that **no specific country is named** — do not attribute a target-market list to them.
> - **Astroyogi's Juspay is comment-only.** Re-fetched independently: 3 `juspay`, 1 `razorpay`, 3 `paypal`, **all inside HTML comments, zero outside**, across 347 comments. Their payment paths are a byte-identical ~365KB soft-404 against my nonsense control, with no live Juspay anywhere.
> - **No web checkout, confirmed independently** before the run reported it: `/recharge`, `/wallet`, `/checkout`, `/payment`, `/pay` and a nonsense control all return an **identical 119,223 bytes**. `server: gunicorn`, **no CSP header at all**.
> - **Billing unit, from their own copy:** *"INR 100. You need to recharge in order to talk to"* and *"Recharge and add money to your wallet."* One top-up = one transaction, floor ₹100.
>
> ### ⛔ What the audit CHANGED
> 1. **Volume +2 → +5. A 10× arithmetic error, in the account's favour.** The original row put the ceiling at the ₹100 minimum at "≤92,700/month". ₹111.26 Cr ÷ 12 = ₹92.7M/month, and ₹92.7M ÷ ₹100 = **927,167/month**. **To fall under the 40,000 reject line the average top-up would have to exceed ₹2,318** — not credible here. Full sensitivity table is in the row.
> 2. **Australia rail gap +3 → 0.** The matrix wants a dominant **local rail** absent. The run correctly declined to fire on PayTo/BPAY (2% of all payments) and instead aggregated **BPAY + PayPal + device wallets** to ~45%. PayPal and Apple/Google Pay are **global methods, not local rails**, and device wallets are card credentials this merchant already accepts — so that aggregate double-counts. India supports UPI; neither the US nor Australia regulatorily gates domestic acquiring. Australia is also **18-second sessions, 1.25 pages, 66.92% bounce, ↓52.31%**.
> 3. **Competitor orchestration +2 → 0.** Commented-out markup proves an integration exists in a codebase; it does not establish **adoption**, which is what the row measures. The TAL was already wrong once about Juspay in this exact vertical, so a second unconfirmed Juspay claim gets the stricter standard.
>
> ### ⚠️ One trap claim I could NOT reproduce
> The run logged *"Apple writes 'In‑App Purchases' with U+2011, and a plain-hyphen grep returned ZERO on a page containing ten of them."* **On my fetch of the `/in/` storefront the opposite held: plain hyphen = 6 hits, U+2011 = 0.** It may be storefront- or render-specific. **Do not add it to the permanent trap list on this evidence.** The trap that *did* reproduce, and matters more, is the **carousel-neighbour** one: that page carries **24 `hasInAppPurchases` keys, 18 false and 6 true**, almost all belonging to other apps. **Always pair the flag to its bundleId.**
>
> ### ✔️ Safety checks passed
> No credential value anywhere (the Astroyogi PayPal client-ids correctly withheld as `[live key present — value deliberately not recorded]`). No booking link. No banned competitor name in outreach-facing text. Structure 3/3 collapsibles. ICP re-added independently: **5+4+3+0+0+2+0+2+0+0+0 = 16 across 11 rows.** ✅
>
> ### 📌 The tier understates the account — read this before deciding priority
> 16/29 is 🟢 Medium, but the matrix is penalising this account for things that are not commercial weaknesses. What is actually true: **~100% of revenue is orchestrable while their largest competitor surrenders 15–30% of every iOS recharge to Apple**; a **US$12M round six weeks old explicitly earmarked for international expansion**; a **diaspora that can only pay by card**; and a **balance sheet that makes cost-of-acceptance a P&L conversation**. The two cheapest routes back to ⭐ are evidencing a **second PSP (+3)** or **confirming live orchestrator use at a competitor (+2)**.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** InstaAstro is an India-headquartered online astrology and spiritual-wellness marketplace. Users top up an in-app wallet and spend it per minute on chat and call consultations with 5,000+ verified astrologers, tarot readers, numerologists and vastu experts, with a first consultation at ₹1 (₹1/- in India, free for international users). It has expanded from consultations into **Pooja Seva** (`puja.instaastro.com`) and **spiritual commerce** (`instaastro.com/shop/`). FY26 revenue **₹111.26 Cr**, up from **₹52 Cr** in FY25; company says annualised run-rate has crossed **₹200 Cr**. **12 million registered users**, **183 countries**, **~25% of revenue international and diaspora-driven**. Founded 2021 by **Nitin Verma** (Founder & CEO).

**SimilarWeb total visits:** not supplied as an absolute. Country shares supplied — see below. **Source: SimilarWeb (supplied 2026-10-12), `accounts/traffic/instaastro.md`, Jul–Sep 2026, all-country-domains ON, 37 countries.**
⚠️ **Web visits are a weak proxy for this merchant.** There is **no web checkout at all** (proven below), so every transaction happens inside the apps and none of it appears in this table.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | **India** | **62.80%** ↑19.79% | Cards, net banking, **UPI** — all three sourced to their own Terms | EMI / no-cost EMI · UPI Autopay · Paytm/PhonePe wallets — all **Not found** (low-ticket ₹100 top-up, so EMI is not a real gap) | ✅ InstaAstro Technology Pvt Ltd, Noida |
| 2 | **United States** | 7.58% ↓23.50% | **Cards only** | **PayPal · Apple Pay · Google Pay · ACH** — all absent per their own Terms | ❌ None found |
| 3 | **Australia** | 4.78% ↓52.31% | **Cards only** | **BPAY/internet banking (25% of AU online payments) · PayPal/BNPL (20%) · Apple Pay & Google Pay (~40% of card payments) · PayTo** — RBA-sourced | ❌ None found |
| 4 | **Canada** | 3.61% ↓37.89% | **Cards only** | **Interac · PayPal · Apple Pay · Google Pay** | ❌ None found |
| 5 | **United Kingdom** | 1.98% ↑120.18% | **Cards only** | **PayPal · Apple Pay · Google Pay · Open Banking** | ❌ None found |

🚩 **Sri Lanka (2.68%), UAE (2.38%), Indonesia (1.95%), Brazil (0.94%) and the Netherlands (0.92%) are deliberately excluded from this table** as probable non-human or junk traffic — visit durations of 3–13 seconds, bounce rates to 95.34%, and Audience Share sitting well below Traffic Share. Per the supplied analyst notes, **these must not be used to claim market breadth.** The genuinely addressable non-India set is **US, Canada, UK, Australia**.

### Legal entities
- **InstaAstro Technology Private Limited** — CIN **U72900UP2021PTC145574**, RoC **Uttar Pradesh II**, incorporated **23 April 2021**. Registered office **C 705, Greenwich Grand Omaxe, Sector 93B, Gautam Buddha Nagar, Noida, Uttar Pradesh 201304**. Authorised capital **₹10,00,000**, paid-up **₹3,36,120**. Directors **Nitin Kumar Verma**, **Sanjeev Kumar**, **Sudarshan Choudhary** (nominee). Last AGM **23 Sep 2025**; financials last filed **31 Mar 2025**. **0 active charges.** — [Falcon Ebiz, fetched](https://www.falconebiz.com/company/INSTAASTRO-TECHNOLOGY-PRIVATE-LIMITED-U72900UP2021PTC145574)
  - This is the entity named as owner/operator in both the **Privacy Policy** and the **Terms**, and as the **Google Play developer** — at the identical Noida address. Three independent confirmations.
- ⚠️ **MANK Technology Private Limited** — CIN **U72900DL2008PTC185604**, RoC Delhi, incorporated **08 Dec 2008**, directors **Nitin Kumar Verma** and **Sanjeev Kumar**, registered **Pandav Nagar, Mayur Vihar Phase-1, East Delhi 110091**. Authorised **and** paid-up capital **₹1.00 lac**; operating revenue **"Under INR 1 cr"** for FY ending 31 Mar 2021. — [Tofler, fetched](https://www.tofler.in/mank-technology-private-limited/company/U72900DL2008PTC185604)
  - **This is the Apple App Store developer of record** (`sellerName: MANK TECHNOLOGY PRIVATE LIMITED`, confirmed via Apple's lookup API). It is a **₹1-lakh legacy shell, not the operating company** — it cannot be carrying ₹111 Cr of revenue. Same pattern as Astrotalk, where Apple still carries the pre-rename "Codeyeti Software Solutions".
- ⚠️ **A third name appears in their own Terms.** The opening paragraph of `/terms-and-conditions/` says *"InstaAstro Private Limited"*, while the same document twice says *"INSTAASTRO TECHNOLOGY PRIVATE LIMITED"*. **No company by the name "InstaAstro Private Limited" was found in any registry.** Treat as a drafting error, not a fourth entity.
- ❌ **No entity, office or branch found outside India** — not in the US, Canada, UK, Australia or anywhere else. Governing law is India and jurisdiction is **exclusively the courts of New Delhi** (Terms, fetched). **Every non-India card payment is a cross-border authorisation from an Indian entity against a foreign issuer.**
- ⚠️ **No CIN is disclosed anywhere on the website.** (Note: a `grep` for "CIN" on their legal pages returns hits — all of them are the substring inside **"pri-CIN-g"**. New false positive, logged below.)

### Known PSPs
- **Razorpay** — `[Provider Case Study]`, dedicated and detailed: **Cards SR Boosters**, **UPI** for wallet recharges, **Razorpay International Payment gateway**. https://razorpay.com/blog/razorpay-supercharged-instaastros/
- **No second PSP found anywhere.** Their Privacy Policy refers throughout to *"**the concerned payment gateway aggregator**"* — **singular and unnamed** — which is consistent with exactly one RBI-authorised aggregator behind the wallet. `[Terms/Privacy Policy]`

### Orchestration status
**None detected — direct PSP integration only (single gateway, Razorpay).** → **Greenfield.**

**⛔ TAL CORRECTION — LOGGED.** `accounts/apac-tal.csv` lists InstaAstro with `Payment Orchestrator = Juspay`. **That cell is wrong and should be cleared.** Re-verified independently this run, not inherited from the stub:

| Test | Result |
|---|---|
| Re-fetched Razorpay's InstaAstro case study (88,715 b decompressed) | **93 hits "instaastro" · 0 hits "juspay" · 0 hits "orchestrat" · 0 hits "optimizer"** |
| Live homepage, privacy policy, terms, `puja.instaastro.com`, `/shop/` | **0 hits** for juspay, gr4vy, primer, spreedly, payrails, cellpoint, br-dge, pagos, apexx, hyperswitch, yuno |
| Two targeted web searches for an InstaAstro orchestrator | Nothing. No page connects InstaAstro to any orchestrator |
| Timing | Razorpay and Cashfree both suspended third-party orchestrator integrations in **January 2025** — the same month that case study published. A Juspay-fronting-Razorpay setup would have broken in exactly that window. `[UNVERIFIED — search summary only]` |

**Standard of proof reached: strong absence of evidence across the merchant's own production assets, its gateway's own case study and the open web — not positive proof of a negative.** I cannot exclude that InstaAstro once trialled an orchestrator, or that one sits inside the Android/iOS binary where I could not look. But nothing supports the TAL cell, and **opening on "you have no orchestration layer" is the correct motion.**

### Buying signals
- 💰 **US$12M Series A closed 27 Aug 2026** — led by **Singularity AMC** + **Artha Venture Fund**, founders participating; ~₹114.5 Cr. [Inc42](https://inc42.com/buzz/instaastro-bags-12-mn-to-build-ai-tools-expand-online-pooja-services/)
- 🚀 **Proceeds explicitly earmarked for "expansion across regional and international markets"** — plus AI sentiment analysis, multilingual consultations, Pooja Seva and spiritual commerce. [Entrepreneur India](https://india.entrepreneur.com/business-news/instaastro-crosses-inr-200-crore-in-annualized-revenue-raises-usd-12-million-series-a)
- 🌏 **~25% of revenue already international, "driven largely by the Indian diaspora"**, across 183 countries — their own figure, and the single most useful sentence in the coverage.
- 🏗️ **A second and third payment surface are being stood up right now** — `puja.instaastro.com` is live on its own separate codebase and CDN (`cf-puja.instaastro.com`), and `instaastro.com/shop/` ships physical products with *"shipping/custom fees"* in the refund terms. Both are funded expansion targets.
- 💼 **A nominee director, Sudarshan Choudhary, was appointed 28 Feb 2025** — an investor board seat predating the Series A. `[UNVERIFIED — search summary only, aggregator sources]`
- ❌ **No payment-related hire found.** Open roles are Django / Python / Backend Developer and BD, all Noida. **There is no payments owner** — so the conversation belongs with the founder/CEO or finance, not a payments PM.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach InstaAstro` to draft the 12-touch sequence.*

⚠️ **Read before drafting.**
1. **Lead with the funding-plus-rails collision**, not with pain projection. They said they are expanding internationally; their own Terms show cards as the only international rail; their own gateway said cross-border failures were *"a major hurdle"*. All three are quotable.
2. ⛔ **"Over 80% of international transactions via cards" is a SHARE OF VOLUME.** Never convert it to a success or failure rate. Astrotalk's page is the one with the success-rate line.
3. ⛔ **Never name Juspay, Gr4vy, Primer, Spreedly, Payrails, CellPoint, BR-DGE, Pagos or APEXX in anything outreach-facing** — and note Juspay is wrong on the TAL for this vertical anyway.
4. **Do NOT lead with complaints.** The dominant review theme is wallet draw-down, per-minute billing transparency and refund refusal — **orchestration does not fix any of that**, and conflating them is the fastest way to lose credibility. The one usable complaint is the card-on-file one (Section 5).
5. **Enter high.** No payments hire exists; the founder/CEO **Nitin Verma** is the decision-maker. Frame as cost of acceptance and international approval rate in the first post-raise year.
6. **Gulf is EMEA** — UAE appears in their traffic and in Razorpay's "MENA" list. Per Prateek's instruction this account's non-APAC markets are in scope because it is India-HQ'd, but **UAE traffic is almost certainly junk** (4-second visits) — do not build an angle on it.
7. **Do not cite the 12M-registered-users figure as active users.** Google Play shows **1M+ downloads**. The two are not reconcilable as the same thing (Section 12).
8. ⛔ **Do not quote a transaction volume.** It is assumed, not derived from sourced inputs.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 16 / 29  *(was 18; re-scored by Prateek's audit 2026-10-12)*
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ⚠️ **NOT FOUND — ASSUMED ~185,000/month. [ASSUMPTION — average top-up value not researched.]** **Billing unit: one wallet top-up = one transaction.** Consultations draw down the balance and are NOT separate transactions. ⛔ **CORRECTED BY PRATEEK'S AUDIT 2026-10-12 — the original row scored +2 on arithmetic that was out by a factor of ten.** ₹111.26 Cr/yr = ₹1,112,600,000 ÷ 12 = **₹92.7M per month**. At the **sourced ₹100 minimum top-up** the true ceiling is **927,167 txn/month**, not the 92,700 originally stated. **Sensitivity on FY26 revenue:** ₹100 avg → 927,167 · ₹300 → 309,056 · ₹500 → **185,433** · ₹1,000 → 92,717 · ₹2,000 → 46,358. **To fall below the 40,000 reject line the average top-up would have to exceed ₹2,318** — not credible for an app with a ₹100 minimum selling per-minute consultations typically priced in tens of rupees. The +5 band (≥100,000) holds for any average below ~₹927. Scored **+5**. ⚠️ Still an assumption, so it could never have *rejected* the account either way; and it rests on ₹111.26 Cr being gross wallet collections — **if that figure is net commission, the true count is several-fold HIGHER, not lower.** Resolving average top-up value remains manual-research item #1. |
| Orchestration status | **+4** | ✅ **None detected — direct PSP integration only. Greenfield.** Re-verified independently: 0 orchestrator hits across the Razorpay case study, the homepage, privacy policy, terms, `puja.` and `/shop/`, plus two targeted searches. Their Privacy Policy says *"the concerned payment gateway **aggregator**"* — singular. **TAL's `Juspay` cell corrected.** |
| 3+ countries | **+3** | ✅ **Five markets >1% traffic share** — India 62.80%, US 7.58%, Australia 4.78%, Canada 3.61%, UK 1.98%. Even excluding every junk-traffic market, four remain. SimilarWeb (supplied 2026-10-12). |
| Multiple PSPs | **0** | ❌ **Only one PSP evidenced — Razorpay.** No second gateway found on any asset. Their Privacy Policy's singular *"the concerned payment gateway aggregator"* corroborates. This zero **is** the opportunity, not a weakness in the account. |
| Local rail or licensing gap in a top-3 market | **0 ⬜** | ⛔ **STRUCK BY PRATEEK'S AUDIT 2026-10-12. Originally +3 on Australia; it does not survive.** The matrix requires **a dominant *local rail*** absent from a top-3 market, or no local entity where domestic acquiring is **regulatorily gated**. Neither limb fires: **(a)** The run itself correctly declined to fire on **PayTo/BPAY**, the matrix's named ANZ rail, because the same RBA table puts BPAY at **2% of all payments**. It instead built a ~45% aggregate from **BPAY + PayPal + device wallets**. **PayPal and Apple/Google Pay are global methods, not local rails**, and device wallets are *card credentials* — which this merchant already accepts as cards, so counting them as an absent rail double-counts. **(b)** India (#1) **supports UPI**, so no gap there. The US (#2) and Australia (#3) have no local entity, but **neither regulatorily gates domestic acquiring**. **(c)** Australia's traffic quality is weak and falling — **00:00:18 average visit, 1.25 pages, 66.92% bounce, ↓52.31%** — so it is a questionable basis for a tier-carrying row regardless. ⚠️ **The underlying commercial observation is still true and still the pitch** — the diaspora corridor is card-only with no PayPal, Apple Pay, Google Pay, ACH, Interac or BECS. It simply is not what this ICP row measures. |
| Recent expansion | **+2** | ✅ **US$12M Series A of 27 Aug 2026 explicitly earmarked for "expansion across regional and international markets"**, plus Pooja Seva and spiritual commerce; `puja.instaastro.com` is live. ⚠️ **Honest counter-read:** the supplied traffic shows the Western markets **contracting** — US ↓23.50%, Australia ↓52.31%, Canada ↓37.89%, South Africa ↓71.44% — while India ↑19.79%. **Expansion is funded and stated intent; it is not yet visible as growth.** The row asks for expansion in the last 12 months, which is satisfied; the narrative must not overclaim. |
| Payment issues | **0** | ❌ **Isolated, not moderate or high — scored down deliberately.** Exactly **one** genuine payment-infrastructure complaint surfaced (the card-on-file AED case, Section 5). The **dominant** complaint theme is wallet draw-down, per-minute billing transparency and refund refusal, which **orchestration does not fix.** Awarding this row would be inflation. |
| Funding >$10M | **+2** | ✅ **US$12M Series A, announced 27 August 2026** — **1 month, 15 days** before this report date, comfortably inside 12 months. Led by **Singularity AMC** and **Artha Venture Fund**. Verified from **three independently fetched pages** (Inc42 27 Aug'26, Entrepreneur India 27 Aug 2026, Indian Startup News 27 Aug 2026 15:06 IST). |
| High traffic outside home | **0** | ❌ **India is 62.80%, above the 60% threshold.** Outside-India traffic is 37.20%. Per the supplied analyst notes, **not rounded down to make the row fire.** |
| Competitor using orchestration | **0 ⬜** | ⛔ **STRUCK BY PRATEEK'S AUDIT 2026-10-12. Originally +2.** I re-fetched `astroyogi.com` myself and **confirmed the run's finding exactly**: of 3 `juspay`, 1 `razorpay` and 3 `paypal` references, **every single one sits inside an HTML comment — zero outside** (347 comments on the page). I then checked their `/recharge`, `/wallet`, `/checkout`, `/payment`, `/astrologers` and `/talk-to-astrologer` paths against a nonsense control (`/zzz-control-not-real-8831`): **all return a byte-identical ~365KB soft-404**, and **none carries live Juspay outside comments**. The matrix requires a competitor **adopting** an orchestrator. Commented-out markup proves the integration exists in their codebase; it does **not** establish live production use. **Extra caution applies here:** the TAL was already wrong once about Juspay in this exact vertical (InstaAstro's own cell), so a second unconfirmed Juspay claim gets the stricter standard. ⚠️ **The finding is retained as genuine competitive intelligence in Section 11** — Astroyogi has built Juspay HyperSDK and a production PayPal SDK in **USD**, while InstaAstro gives the diaspora cards only. That contrast is usable; it just cannot carry an ICP point. |
| Payment job postings | **0** | ❌ **None found.** Open roles are Backend / Django / Python Developer and Business Development, all Noida. No payments, fintech or billing role. |

**Tier:** 🟢 **Medium (10–16)** → **16 / 29.** ⛔ **Re-scored from 18 ⭐ by Prateek's audit, 2026-10-12.** Net of three changes: volume **+2 → +5** (a 10× arithmetic error, in the account's favour), Australia rail gap **+3 → 0**, competitor orchestration **+2 → 0**. ⚠️ **The tier understates this account.** The qualitative case is strong and is unaffected by the re-score: **no app-store trap** (decisive, and their largest competitor *is* trapped), a **US$12M round six weeks old explicitly earmarked for international expansion**, a **diaspora that can only pay by card**, and a **P&L under real pressure**. The two cheapest routes back to ⭐ are evidencing a **second PSP (+3)** or **confirming live orchestrator use at a competitor (+2)**.

> **Two rows carry the tier and Prateek should audit them first.** "Local rail gap" (+3) and "competitor using orchestration" (+2) together are 5 points. **Strike both and the score is 13 → 🟢 Medium.** Everything else is hard-sourced.
> **No analyst override applied.** The app-store override explicitly does **not** fire — Apple's own JSON says `hasInAppPurchases: false` on both storefronts, so orchestration can reach this revenue. ⚠️ **But the absolute-volume concern is live:** at ₹111 Cr FY26 revenue (~US$12.5M) this is a materially smaller merchant than Astrotalk (₹1,214 Cr), and the transaction count is assumed. I have **not** applied a downward override because an unsourced number must not drive a rejection — but if discovery returns an average top-up above ~₹420 on the current run-rate, this account falls below the ICP volume floor and should be re-scored.

### Source Notes
- ✅ **Verified by me, first-hand, this run:** the Series A amount/leads/date (3 fetched pages) · the Razorpay case study and all its quotes (re-fetched, 93/0/0 control) · the billing unit and the cards/net-banking/UPI rail list (Terms) · card-on-file tokenisation via an unnamed aggregator (Privacy Policy) · the CIN, incorporation date, capital, directors and FY25 financial movements (Falcon Ebiz) · the Noida registered office (matching the Google Play developer disclosure exactly) · MANK Technology as the Apple developer and as a ₹1-lakh shell · `hasInAppPurchases: false` on both Apple storefronts against six known-true controls · no in-app-purchase badge on Play · the soft-404 catch-all · INR-only pricing across every page · Astroyogi's commented-out Juspay HyperSDK · Google's India alternative-billing policy · the RBA 2025 Consumer Payments Survey table.
- ⚠️ **FY26 revenue ₹111.26 Cr and FY25 ₹52 Cr are company-stated figures in press coverage, NOT MCA filings.** The registry shows financials last filed **31 Mar 2025 (FY25)**. The independent corroboration available is the FY25 **Total Revenue ↗108.34%** movement on the registry, which is consistent with ~₹25 Cr → ₹52 Cr. **FY26 cannot be verified from a filing as of today.**
- ⚠️ **The ₹200 Cr+ annualised run-rate is a company claim**, repeated by outlets, not an audited figure.
- ⚠️ **12M registered users, 5,000+ experts, 183 countries, ~25% international** — all company-stated via press, consistently across three fetched pages. Credible but self-reported.
- ⚠️ `[UNVERIFIED — search summary only, page not fetched]`: the ₹3.2 Cr seed (Nov 2021, Artha) and ₹18.5 Cr pre-Series A (Artha) · the nominee-director appointment date · the Jan 2025 Razorpay/Cashfree orchestrator suspensions · the CB Insights figure of $2.73M over 2 rounds, which **contradicts** all other coverage and should be disregarded.
- ⚠️ **HQ discrepancy resolved against "Gurugram."** `ipoplatform.com` says "Gurugram based". **Three stronger sources say Noida:** the MCA registered office (Sector 93B, Gautam Buddha Nagar), the Google Play developer address (identical), and Indian Startup News (*"The Noida-based startup"*). All job listings are Noida. **Use Noida.**
- ❌ **Not found at all:** average wallet top-up value · web-vs-app revenue split · the named target countries for the Series A · any PCI documentation · any second PSP · the astrologer payout rail · any public payment RFP.

### Success Case Alternatives
Per repo policy I name only publicly-referenceable Yuno customers and attach **no numbers** to any customer without published metrics. **No Yuno case study with a matching profile — India-HQ'd, app-first, wallet-top-up consultation marketplace with a diaspora corridor — was identified from sources available in this run.** The honest recommendation is to use the **structural** match rather than a named logo: a single-gateway merchant whose growth capital is committed to markets its current rail set cannot serve. **Prateek should pick the case from Yuno's current approved list** — this is flagged in Manual Research Recommendations rather than filled with a guess.

---

## Executive Summary

InstaAstro is a Noida-headquartered online astrology and spiritual-wellness marketplace that bills through in-app wallet top-ups and sells per-minute chat and call consultations with 5,000+ experts. It closed a **US$12M Series A on 27 August 2026** (Singularity AMC, Artha Venture Fund) explicitly earmarked for international expansion, on FY26 revenue of **₹111.26 Cr** and a claimed **₹200 Cr+** run-rate, with **~25% of revenue already coming from the Indian diaspora** abroad. The key payment-infrastructure finding is a **single-gateway stack — Razorpay direct, no orchestrator** — serving a four-market Western corridor (US, Canada, UK, Australia) on **cards as the only available rail**, confirmed from the company's own Terms, with **no legal entity anywhere outside India**. The orchestration opportunity is **greenfield**, and unusually for a consumer app the **entire revenue base is addressable**, because Apple's own product data shows InstaAstro does **not** use in-app purchase. **Motion: Greenfield.**

---

## Section 1: Website Traffic Analysis by Country

**Data source:** **Path 1 — pasted/supplied SimilarWeb data**, `accounts/traffic/instaastro.md`, SimilarWeb (supplied 2026-10-12), Jul–Sep 2026, all traffic, "Include all country domains" **ON**, single domain `instaastro.com`, 37 countries listed. **Not re-researched**, per instruction.

| Rank | Country | Traffic Share | Est. Monthly Visits | Trend | Engagement | Source |
|---|---|---|---|---|---|---|
| 1 | **India** 🔴 high priority | **62.80%** | Not supplied as absolute | **↑ 19.79%** | 3:04 · 2.83 pp/v · 40.87% bounce — **real, engaged** | SimilarWeb (supplied) |
| 2 | **United States** 🔴 high priority | **7.58%** | " | **↓ 23.50%** | 1:29 · 2.43 · 61.65% — **real** | " |
| 3 | **Australia** | 4.78% | " | **↓ 52.31%** | 0:18 · 1.25 · 66.92% — **weak, but a real market** | " |
| 4 | **Canada** | 3.61% | " | **↓ 37.89%** | **4:35** · 2.21 · 45.71% — **real, best-engaged market on the list** | " |
| 5 | Sri Lanka | 2.68% | " | ↑ 25.19% | **0:06 · 1.07 · 95.34%** — 🚩 **not real sessions** | " |
| 6 | United Arab Emirates | 2.38% | " | ↑ 6.69% | **0:04** · 1.06 · 78.69% — 🚩 **not real** | " |
| 7 | **United Kingdom** | 1.98% | " | **↑ 120.18%** | 0:40 · 1.99 · 53.42% — **real** | " |
| 8 | Indonesia | 1.95% | " | ↑ 3.99% | 0:13 · 1.30 · 81.57% — 🚩 **doubtful** | " |
| 9 | South Africa | 1.93% | " | **↓ 71.44%** | 0:30 · 1.51 · 78.06% — doubtful | " |
| 10 | Brazil | 0.94% | " | ↑ 490.66% | 0:09 · 1.73 · 42.16% — 🚩 **doubtful despite the growth** | " |
| 11 | Netherlands | 0.92% | " | ↓ 8.78% | **0:03** · 1.13 · 62.09% — 🚩 **not real** | " |

**Listed total 91.55%** across 11 rows; ~8.45% across 26 further countries not shown.

**Three things this table forces, all honoured in this report:**
1. **India at 62.80% is above 60%, so the "high traffic outside home" ICP row scores 0.** Not rounded down.
2. **India is the only market growing at scale.** The three largest Western markets are contracting hard. **Any "your expansion is working" framing is false** and would be caught immediately.
3. **Five of the eleven listed markets are probably junk.** Audience Share corroborates: Sri Lanka carries 2.68% of traffic but **0.77%** of audience. The addressable non-India set is **US, Canada, UK, Australia — ~17.95% of traffic.**

⚠️ **Flagged for Section 2 cross-reference: markets 2–11 have NO local entity.** Only India does.
⚠️ **This table materially understates the business.** There is no web checkout; 100% of payment is in-app.

---

## Section 2: Legal Entities & Local Presence

**Headquarters:** **Noida, Uttar Pradesh, India.** Founded **2021** (company incorporated 23 April 2021) by **Nitin Verma**, Founder & CEO.

| Country | Entity Name | Registration # | Source |
|---|---|---|---|
| **India** | **InstaAstro Technology Private Limited** *(operating + billing entity)* | CIN **U72900UP2021PTC145574** · Reg. no. 145574 · RoC Uttar Pradesh II | [Falcon Ebiz (fetched)](https://www.falconebiz.com/company/INSTAASTRO-TECHNOLOGY-PRIVATE-LIMITED-U72900UP2021PTC145574); named in [Privacy Policy](https://instaastro.com/privacy-policies/) and [Terms](https://instaastro.com/terms-and-conditions/); Google Play "About the developer" |
| **India** | **MANK Technology Private Limited** *(Apple App Store developer of record only)* | CIN **U72900DL2008PTC185604** · RoC Delhi | [Tofler (fetched)](https://www.tofler.in/mank-technology-private-limited/company/U72900DL2008PTC185604); Apple lookup API `sellerName` |
| Everywhere else | **None found** | — | — |

**Entity detail, InstaAstro Technology Private Limited** (all from the fetched Falcon Ebiz page): incorporated **23 Apr 2021**; status **Active**; authorised capital **₹10,00,000**; paid-up **₹3,36,120**; **3** directors — **Nitin Kumar Verma**, **Sanjeev Kumar**, **Sudarshan Choudhary**; activity *"Other computer related activities"*; last AGM **23 Sep 2025**; balance sheet last filed **31 Mar 2025**; **0 active charges**.
⚠️ Paid-up equity of ₹3.36 lakh against a US$12M raise is normal for an Indian VC-funded company — investment typically arrives as CCPS, which does not appear in paid-up equity. **Do not read it as a sign the raise did not happen.**
⚠️ **0 active charges** means no registered security interest — consistent with equity, not debt, financing at the Series A, though the registry also shows **Borrowings ↗599,900%** in FY25. Unreconciled; flagged.

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---|---|---|---|---|
| **India** | ✅ #1 (62.80%) | ✅ Yes | ✅ Yes — RBI PA authorisation regime | **None** — domestic, local aggregator |
| **United States** | ✅ #2 (7.58%) | ❌ **None found** | ❌ No regulatory gate | 🔴 **HIGH** — cross-border card auth, INR pricing |
| **Australia** | ✅ #3 (4.78%) | ❌ **None found** | ❌ No regulatory gate | 🔴 **HIGH** — same, plus ~45% of AU online rails unsupported |
| **Canada** | ✅ #4 (3.61%) | ❌ **None found** | ❌ No regulatory gate | 🔴 **HIGH** — same; best-engaged market on the list |
| **United Kingdom** | ✅ #7 (1.98%) | ❌ **None found** | ❌ No regulatory gate | 🟠 **MEDIUM-HIGH** — fastest-growing real market (↑120%) |
| Sri Lanka / UAE / Indonesia / Brazil / Netherlands | ✅ by share | ❌ None found | varies | ⬜ **Not assessed — traffic judged non-genuine** |

> *"**Warning: Potential cross-border operation in the United States, Australia, Canada and the United Kingdom.** No local entity found in any of them. Transactions are processed cross-border from an Indian entity, with higher scheme costs, lower approval rates and FX exposure."*

**No regulatory acquiring gate applies in the Western corridor** — unlike China, Korea, Indonesia or Vietnam, the US/UK/CA/AU markets do not require local presence for acquiring. **So this is a cost-and-approval-rate story, not a licensing-blocker story, and it should be argued that way.** Overclaiming a regulatory gate here would be wrong.

> **MANUAL:** Confirmed on the live T&Cs and Privacy Policy — both fetched 2026-10-12. Governing law **India**; exclusive jurisdiction **courts of New Delhi**. No foreign entity, foreign jurisdiction clause or foreign billing entity appears anywhere.

---

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|---|---|---|---|
| **India (domestic)** | **Razorpay** — UPI for wallet recharges, Cards SR Boosters | `[Provider Case Study]` | https://razorpay.com/blog/razorpay-supercharged-instaastros/ |
| **International (NA, Europe, SEA, MENA)** | **Razorpay International Payment gateway** — carries *"over 80% of InstaAstro's international transactions via cards"* | `[Provider Case Study]` | same |
| All | **One unnamed "payment gateway aggregator"**, singular, performing **card-on-file tokenisation** | `[Terms/Privacy Policy]` | https://instaastro.com/privacy-policies/ |
| Any | **No second PSP found** | — | — |

**From the Privacy Policy, fetched verbatim:**
> *"Once you grant your consent for the tokenisation of your payment information as mentioned above, a request is generated on your behalf and transferred to **the concerned payment gateway aggregator**. The concerned payment gateway aggregator uses this information to create a token corresponding to the combination of the payment information, the token requestor, and the concerned device."*

Two things follow. **Card-on-file tokenisation is live** — consistent with the RBI CoF tokenisation regime, and it means **stored credentials and therefore repeat billing exist**. And the phrasing is **singular throughout** — *"the concerned payment gateway aggregator"* — which is how a merchant with exactly one RBI-authorised aggregator writes. ⚠️ `[INFERENCE, not confirmed]` that the aggregator is Razorpay; the policy does not name it, and Razorpay's case study is the only PSP evidence that exists.

> **MANUAL:** Nothing public names the aggregator. A single Android recharge with a proxy would settle it in one minute.

### 3B. Payment Orchestrator

**Classification: None detected — direct PSP integrations only. GREENFIELD.**

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with a single PSP, which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

Evidence and the standard of proof reached are set out in full in the **Orchestration status** block of Section 1 and in the TAL correction. In short: **0 orchestrator hits across five of the merchant's own production assets, 0 across the gateway's own case study (against a 93-hit control for "instaastro"), and 0 from two targeted searches.** This is **strong absence of evidence, not proof of absence** — an orchestrator inside the mobile binaries cannot be excluded from public sources.

⛔ **The `accounts/apac-tal.csv` `Payment Orchestrator = Juspay` cell for InstaAstro is incorrect and should be cleared.** Logged as a TAL correction.

> **MANUAL:** DevTools on a real Android recharge is the only remaining test. The web cannot answer it — there is no web checkout.

---

## Section 4: Alternative & Local Payment Methods

**The authoritative source for this section is the merchant's own Terms**, which state the complete permitted top-up method set. Fetched verbatim:

> *"**All payments for accessing Paid Services on the Website must be made exclusively through the Registered Member's InstaAstro Wallet**, linked to their account. To add funds to this Wallet, the Registered Member **must use valid banking methods such as debit/credit cards, net banking, or UPI**."*

| Country/Region | Method | Category | Status | Source |
|---|---|---|---|---|
| **India** | **UPI** | Bank transfer / A2A | ✅ **Active** — named in Terms *and* in Razorpay's case study for wallet recharges | Terms; Razorpay case study |
| **India** | **Debit / credit cards** | Cards | ✅ **Active**, with **card-on-file tokenisation** | Terms; Privacy Policy |
| **India** | **Net banking** | Bank transfer | ✅ **Active** | Terms |
| **India** | UPI Autopay | Direct debit / mandate | ❌ **Not found** | — |
| **India** | EMI / no-cost EMI | BNPL / Instalments | ❌ **Not found** — and **not a real gap**: a ₹100-minimum top-up is not an instalment product | — |
| **India** | Paytm / PhonePe wallets | Digital wallet | ❌ **Not found** | — |
| **India** | RuPay specifically | Cards | ❌ **Not found** (generic "cards" only) | — |
| **US / Canada / UK / Australia** | **Cards (cross-border)** | Cards | ✅ **Active — and the only option.** *"over 80% of InstaAstro's international transactions via cards"* | Razorpay case study |
| **US / Canada / UK / Australia** | **PayPal** | Digital wallet | ❌ **Not found** — absent from the Terms' exhaustive method list | Terms |
| **US / Canada / UK / Australia** | **Apple Pay / Google Pay** | Digital wallet | ❌ **Not found** | Terms |
| **United States** | ACH | Bank transfer | ❌ **Not found** | Terms |
| **Canada** | Interac | Bank transfer / debit | ❌ **Not found** | Terms |
| **Australia** | **BPAY / PayTo / BECS** | Bank transfer / mandate | ❌ **Not found** | Terms |
| **Netherlands** | iDEAL | Bank transfer | ❌ **Not found** (and NL traffic judged non-genuine) | Terms |
| **All markets** | **Apple IAP / Google Play Billing** | App-store billing | ❌ **NOT USED** — see Section 8A | Apple product JSON, both storefronts |

> *"**Warning: In Australia, BPAY and internet banking account for 25% of online consumer payments and PayPal/BNPL a further 20% — together ~45% of the market — while device-based wallets are ~40% of card payments. None of these is supported by InstaAstro.**"* — RBA 2025 Consumer Payments Survey, Table 2 and Graph 6, [fetched](https://www.rba.gov.au/publications/bulletin/2026/may/consumer-payment-behaviour-in-australia.html)

> *"**Warning: In the United States — their #2 market — PayPal, Apple Pay and Google Pay are mainstream consumer checkout rails and none is supported.**"* ⚠️ **I did not source a US method-share figure in this run.** The absence is sourced; the prominence is not. **Argue the US on approval rate and cross-border cost, where I do have evidence, and argue Australia on rail coverage, where the RBA backs it.**

**⭐ And the currency finding, first-hand.** `INR`/`₹` are the **only** currency markers present on the homepage, `/shop/` and the Terms. **No USD, GBP, AUD, CAD or AED appears anywhere** across those three fetched pages. `[INFERENCE, not confirmed]` **The platform prices in INR only**, so a US, Canadian, British or Australian cardholder is charged in rupees on a cross-border authorisation — the configuration with the highest decline rate and an FX leg on top. ⚠️ **Caveat: the web is not the payment surface.** The app may localise pricing and I could not test it. The Terms govern the app too and name no other currency.

> **MANUAL:** Install the Android app behind a US and an Australian IP, start a recharge, and record the method sheet and the display currency. This is the single highest-value 10 minutes available on this account.

---

## Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|---|---|---|---|---|
| **Card-on-file repeat deduction, cross-border, in AED** | Google Play (India storefront, reviewer "Mamata Pant") | **Isolated — 1 instance, 7 found helpful** | **13 Sep 2026** | [Play listing (fetched)](https://play.google.com/store/apps/details?id=com.instaastro.onlineastrology&hl=en_IN) |
| Wallet draw-down / per-minute billing transparency | Google Play | Moderate | 9 Sep 2026 | same |
| Wallet debited instead of free trial minutes; partial refunds only | Apple App Store reviews | Moderate | Not dated in summary | `[UNVERIFIED — search summary only, page not fetched]` |
| **Duplicate payments for the same service** | **Merchant's own Terms** | Documented as policy | current | [Terms (fetched)](https://instaastro.com/terms-and-conditions/) |
| **"Payment gateway timeout"** | **Merchant's own Terms** | Documented as policy | current | same |

### ⭐ The one usable complaint — and it is a payments complaint, not a support complaint
Google Play, 13 Sep 2026, fetched verbatim:
> *"I added only **10 AED**, but this app charged **200 AED +** from my card **WITHOUT permission**. Even after I **removed my card, it keeps deducting money every time because it secretly saves your card details.**"*

Strip the accusation and what remains is a **stored-credential failure on a cross-border card**: a token that outlived the cardholder's attempt to delete it, and an amount that did not match the intent. The Privacy Policy independently confirms **card-on-file tokenisation via an unnamed aggregator** is live. ⚠️ **This is one consumer's allegation, not a verified incident** — it is quotable as a risk theme, never as an established fact.

### ⭐⭐ Stronger than the reviews: they document the failure class in their own Terms
> *"**If a User makes multiple payments for the same service, the additional amount will be refunded in full** without deductions. Refunds for technical glitches (e.g., **payment gateway timeout**) will be issued after verification. **Users must ensure their bank hasn't been debited before retrying payment.**"*

**A merchant writes "ensure your bank hasn't been debited before retrying" into its refund policy because that has happened enough times to need a clause.** That is a payment-status and reconciliation problem — debit succeeds, status does not return, the user retries, and now there are two payments. It is the single most defensible complaint-side evidence in this file, because it comes from the merchant itself rather than from an angry reviewer.

### ⚠️ Honest counter-read — and the reason this ICP row scored 0
**By volume the dominant themes are wallet draw-down, pricing transparency and refund refusal.** The 9 Sep review — *"the astrologer responded very late, yet the chat time kept running, so I lost my balance"* and *"the chat rates increased unexpectedly"* — is a **product and pricing** grievance. **Orchestration does not fix any of it.** Scoring "payment issues" would have been inflation, so it scored **0**. The same trap is already flagged in `astrotalk.md`; it applies identically here.

---

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|---|---|---|---|
| 1 | **27 Aug 2026** | **US$12M (~₹114.5 Cr) Series A led by Singularity AMC and Artha Venture Fund**, founders participating. Proceeds: AI sentiment analysis + multilingual consultations, **expansion across regional and international markets**, Pooja Seva, spiritual commerce. **No valuation disclosed.** | **Funding** | [Inc42](https://inc42.com/buzz/instaastro-bags-12-mn-to-build-ai-tools-expand-online-pooja-services/) · [Entrepreneur India](https://india.entrepreneur.com/business-news/instaastro-crosses-inr-200-crore-in-annualized-revenue-raises-usd-12-million-series-a) · [ISN](https://indianstartupnews.com/funding/online-astrology-and-spiritual-wellness-platform-instaastro-raises-12-million-in-series-a-funding-12443449) |
| 2 | **27 Aug 2026** | **Annualised revenue run-rate crosses ₹200 Cr (~US$21M)**; FY26 revenue **₹111.26 Cr** vs FY25 **₹52 Cr**; registered users up ~400% in two years to **12 million**; experts up from ~1,500 to **5,000+**; **~25% of revenue international, diaspora-driven**; 183 countries | Financial disclosure | Entrepreneur India; ISN |
| 3 | **Live as of 2026-10-12** | **`puja.instaastro.com` in production** — a **separate codebase on its own CDN** (`cf-puja.instaastro.com`), Microsoft Clarity instrumented. The Pooja Seva business the Series A funds. **A new payment surface being built now.** | Market / product expansion | Fetched directly, 325,365 b |
| 4 | **28 Feb 2025** | **Sudarshan Choudhary appointed nominee director** (DIN 09459009) — an investor board seat predating the Series A | Leadership / governance | `[UNVERIFIED — search summary only]`; director list confirmed on [Falcon Ebiz](https://www.falconebiz.com/company/INSTAASTRO-TECHNOLOGY-PRIVATE-LIMITED-U72900UP2021PTC145574) |
| 5 | **2021 / 2024** | Prior rounds: **₹3.2 Cr seed, Nov 2021** (Artha Venture Fund) and **₹18.5 Cr pre-Series A** (Artha-led). **Artha has now led or co-led three consecutive rounds.** | Funding history | `[UNVERIFIED — search summary only]` |

**Public payment RFP:** **No public payment-related RFP found.** No override applies.

**Payment-infrastructure hiring:** ❌ **None.** Open roles found are **Backend Developer (Noida)**, **Django Developer (Noida, 3–7 yrs)**, **Python Developer (Noida, 2–8 yrs)**, plus Business Development Executive, IT Helpdesk and a video-editing internship. **No payments, billing or fintech role exists.** `[UNVERIFIED — aggregator listings, dates unclear]`
⇒ `[INFERENCE, not confirmed]` **There is no payments owner in the organisation.** Payment decisions sit with the founder/CEO or finance. **Enter there.** (The Django/Python roles independently corroborate the `server: gunicorn` stack observed on the live site.)

### ⭐ What they said they would spend it on — and what they did NOT say
Prateek asked specifically for the named target markets. **The honest answer: they named none.**
Across all three fetched funding articles the stated use of proceeds is **"regional and international markets"** — generic. **No country is named by the founder or in any coverage.** The only market list attached to InstaAstro anywhere is **Razorpay's**, from Feb 2025: *"North America, European, SEA, and the MENA"*. The corridor in this report is therefore built from **their own 25%-international-and-diaspora statement + the supplied traffic + Razorpay's list** — not from a founder quote. **Do not attribute a target-market list to them in outreach.**

**Founder quote, for context (fetched, Entrepreneur India):**
> *"We're committed to building the world's most trusted spiritual platform by prioritizing quality over quantity. This investment will help us strengthen our leadership in trusted astrology services, **expand across regional and international markets**, and accelerate our online Pooja Seva and spiritual commerce offerings."* — **Nitin Verma, Founder & CEO**

**Investor quote (fetched, ISN):** *"The first consultation is marketing. The second one is a business."* — **Anirudh A Damani, Managing Partner, Artha Venture Fund.**
⇒ ⭐ **That is a repeat-purchase thesis stated by the lead investor.** A repeat-purchase business lives or dies on whether the *second* top-up authorises. That is precisely what cross-border card approval rate determines, and it is the most useful sentence in the entire funding coverage for Prateek's purposes.

---

## Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|---|---|---|---|
| 1 | **3 Feb 2025** | **"How Razorpay Supercharged InstaAstro's Global Growth"** — the only PSP case study. Names Cards SR Boosters, UPI, International Payment gateway. States *"payment failures were a major hurdle"* and *"over 80% of InstaAstro's international transactions via cards"* | **Primary payment-stack evidence** | https://razorpay.com/blog/razorpay-supercharged-instaastros/ |
| 2 | 27 Aug 2026 | US$12M Series A with international expansion as stated use of proceeds | Buying trigger | as Section 6 |
| 3 | **30 Sep 2026** | **"Introducing Apple Pay on Razorpay: A new way for India to Pay"** — Razorpay launched Apple Pay support | ⭐ **Their own gateway shipped a new wallet rail 12 days ago.** A natural, non-adversarial reason to ask what their roadmap for wallet rails is | Title and date listed on the fetched Razorpay case-study page; **page itself not fetched** `[UNVERIFIED]` |
| 4 | **7 Oct 2026** | *"Payment Gateway Tokenisation and Encryption in India 2026: The Complete Card and Customer Data Checklist"* — Razorpay | Context: CoF tokenisation is live and current for this merchant | same; **not fetched** `[UNVERIFIED]` |
| 5 | Jan 2025 | **Razorpay and Cashfree both suspended third-party orchestrator integrations**; PhonePe did the same Dec 2024 | 🛑 **Structural obstacle — see below** | `[UNVERIFIED — search summary only]` |

**No provider removals found.** No evidence InstaAstro has discontinued any provider or method.

### 🛑 Structural obstacle Prateek should know BEFORE the call, not during it
**Razorpay (Optimizer) and Cashfree (FlowWise) now ship their own orchestration products, and both reportedly suspended third-party orchestrator integrations in January 2025.** In India the incumbent gateway is simultaneously the competitor and the gatekeeper. This is `[UNVERIFIED — search summary only]` and is carried forward from `astrotalk.md`, where it was recorded the same way. **It is not a reason to skip the account** — the international corridor is where Yuno's argument is strongest and is least dependent on an Indian domestic integration — **but walking in without knowing it is a mistake.**

---

## Section 8: Checkout Experience Audit

## ⛔ **NOT COMPLETABLE — there is no web checkout, and the site serves a soft-404 that returns HTTP 200 on every payment path.**

**Verified first-hand, twice (by Prateek's own baseline scan and independently by me):**

| Path | HTTP | Decompressed size | Verdict |
|---|---|---|---|
| `/recharge`, `/wallet`, `/checkout`, `/payment`, `/pay` | **200** | **119,223 b — all identical** | **Catch-all, not real pages** |
| `/zzz-control-not-real-9931/` *(my control)* | **200** | **119,223 b — byte-identical** | **Confirms the catch-all** |
| `/` | 200 | 225,673 b | Real |
| `/shop/` | 200 | 151,161 b | **Real — distinct from the catch-all** |
| `puja.instaastro.com/` | 200 | 325,365 b | **Real — separate property** |

⚠️ **A 200 on a payment path on this domain is NOT evidence a payment page exists.** Any agent that reports `/recharge` as a checkout page has been fooled.

**And the positive mechanism that confirms it:** the homepage's own "Recharge Now" CTA links to **`https://instaastro.app.link/one`** — a **Branch deeplink that pushes the user into the mobile app.** The web does not take money; it hands off.

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | **In-app only.** Web has no checkout | — | `server: gunicorn`, Django, server-rendered |
| Guest checkout | **No** — a `#loginModal` gates the recharge button | Poor | Account mandatory |
| Payment methods visible | **None on web** | — | Methods known only from the Terms |
| Location-based method display | **Not testable on web.** Terms name one global set (cards/net banking/UPI) with no geo-variation | `[INFERENCE]` **Poor** | Would need app testing per geo |
| Multi-currency / local pricing | **INR only** across homepage, `/shop/` and Terms — no USD/GBP/AUD/CAD/AED marker anywhere | **Poor** `[INFERENCE]` | Highest-value thing to confirm in-app |
| Card input / 3DS / PCI indicator / saved methods / error clarity | **Not accessible** | — | **CoF tokenisation confirmed via Privacy Policy** — implies saved cards exist |
| Mobile responsiveness | Mobile-specific markup present and extensive | Good | App-first business |
| **Security headers** | **No Content-Security-Policy header at all.** Only `x-frame-options: DENY`, `x-content-type-options: nosniff`, `referrer-policy: same-origin`, `cross-origin-opener-policy: same-origin-allow-popups` | — | ⚠️ **So the CSP-as-asset-map technique is unavailable for this account.** No `connect-src`/`frame-src` to mine |

> *"Full checkout flow not accessible. Findings limited to publicly observable elements."*

### 8A. ⭐⭐ App-store billing split — THE qualification question, and it resolves in Yuno's favour

Per `subscription-payments.md` §4 this was checked **early and explicitly**, because IAP dominance would invalidate the account.

| Channel | Status | Evidence |
|---|---|---|
| **Apple IAP** | ❌ **NOT USED** | Apple's own product-page JSON, **both US and India storefronts**: `"bundleId":"com.instaastro.onlineastrology"` → **`"hasInAppPurchases": false, "hasExternalPurchases": false`**. Apple lookup API: `price 0.0`, `formattedPrice "Free"`, `advisories []` |
| **Google Play Billing** | ❌ **Probably not used — argued, not proven** | The Play listing's app-info row carries **only "Rated for 3+"** and **no in-app-purchase chip**, while carousel neighbours carry one. **No price-range string belongs to InstaAstro** |
| **Direct gateway** | ✅ **The whole business** | Terms: wallet top-ups via cards / net banking / UPI. Razorpay case study |
| **Spiritual commerce** (`/shop/`) | ✅ Outside app-store billing entirely | Fetched; physical goods with shipping and customs |
| **Pooja Seva** (`puja.instaastro.com`) | ✅ Separate property, outside app-store billing | Fetched |

**The negative is validated against known positives in the same documents** — mandatory, because a zero against the wrong asset is worthless:

| Bundle ID | App | `hasInAppPurchases` |
|---|---|---|
| **`com.instaastro.onlineastrology`** | **InstaAstro** | **false** ⬅ |
| `com.instaastro.astrologer` / `com.instaastro.hiring` | InstaAstro's own sibling apps | false |
| **`codeyeti.com.AstroYeti`** | **Astrotalk** | **true** ✅ control |
| `com.at.pooja` · `com.melooha.app` · `com.itl.tarot` · `com.answer.light` · `com.jaanemann` | peers | **true** ✅ controls |
| `com.ojassoft.astrosagekundli` (AstroSage) · `com.bodhiastrology.app` (Bodhi) · `com.astrolokal.astrology` · `com.dashaspeaks.astrology` · `com.kasamba.ios` | peers | false |

**Six known-true controls fired in the same payload. The zero is real.** And note the cross-validation: **Astrotalk reads `true`, which independently matches `astrotalk.md`'s finding that Apple IAP is live there** — so the method is confirmed against a case this repo already verified by hand.

⇒ ✅ **InstaAstro is NOT an app-store-trapped account. Orchestration can reach effectively 100% of its revenue.** This is a **material advantage over Astrotalk**, where Apple takes 15–30% of every iOS recharge.

⚠️ **Two honest limits.** First, `hasInAppPurchases` is Apple's store metadata for *declared* IAP products; it is strong evidence, not a billing-ledger extract. Second — **and this is unresolved — I could not establish the mechanism by which a paid consultation app bills outside IAP.** I will not assert Apple's review guidelines from memory. **Policy context I did source live:** Google's own Play Console page states *"In response to recent regulatory developments in India, we are now offering **all developers the ability to offer an alternative billing system** alongside Google Play's for their mobile and tablet users in India. If a user pays through an alternative billing system, the Google Play service fee will be **reduced by 4%**."* — [support.google.com, fetched](https://support.google.com/googleplay/android-developer/answer/13306652?hl=en). ⚠️ Note that is *user-choice billing alongside* Play's, which still carries a service fee — **it does not by itself explain a complete absence of Play billing.** **Mechanism: unresolved. Observed outcome: no IAP on either store.**

---

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|---|---|---|
| PCI DSS Level | **Not found** | — |
| Card data handling | **`[INFERENCE, not confirmed]` SAQ A-style, reduced scope** | See below |
| Recommended Yuno integration | **SDK (mobile-first)** — the payment surface is the Android and iOS apps, not the web | Section 8 |

> *"No direct PCI compliance documentation found publicly for InstaAstro."* No PCI statement, trust-centre page, security page or compliance badge exists on any fetched asset.

> `[INFERENCE, not confirmed]`: Based on the confirmed use of a third-party **"payment gateway aggregator"** performing **card-on-file tokenisation** — *"All such information is collected through a **secure third-party payment gateway**"* (Privacy Policy, fetched) — the company's PCI scope is likely reduced, with the aggregator handling card data. **No evidence establishes a level and none is asserted.**

**Relevant and sourced:** **card-on-file tokenisation is live**, with explicit user consent flow, token requestor and device binding described in the Privacy Policy. That is consistent with the RBI CoF tokenisation regime. ⚠️ Per repo rules I do not cite the regulation's current scope or deadlines from background knowledge — **the merchant's own description is the source here, not the rulebook.**

🔒 **No credential, key, token or merchant ID from InstaAstro is recorded in this file.** None was found on InstaAstro's assets. (One *was* found elsewhere — see the Astroyogi note in Section 11 — and is deliberately not recorded.)

---

## Section 10: Strategic Insights & Outreach Angles

> ### **Insight #1: They raised US$12M to go international on a rail set that cannot serve international**
> **Evidence:** **S6** — US$12M Series A, 27 Aug 2026, proceeds for *"expansion across regional and international markets"*, with ~25% of revenue already diaspora-driven ([Entrepreneur India](https://india.entrepreneur.com/business-news/instaastro-crosses-inr-200-crore-in-annualized-revenue-raises-usd-12-million-series-a)) **+ S4** — their own Terms permit only *"debit/credit cards, net banking, or UPI"*, of which net banking and UPI are India-only ([Terms](https://instaastro.com/terms-and-conditions/)) **+ S2** — no legal entity outside India.
> **Pain Point:** Every dollar of the raise aimed at the US, Canada, UK and Australia lands on a single cross-border card rail acquired from an Indian entity. Growth spend converts at the approval rate of the worst-configured leg of the stack, and no amount of marketing fixes a declined authorisation.
> **Yuno Value Proposition:** One integration that adds local acquiring in the cardholder's own market plus the wallet rails those markets actually use, so the expansion budget meets a checkout built for the destination rather than for Noida.
> **Best Success Case:** No matching Yuno published case identified in this run — **use the structural match and select the logo from Yuno's approved list** (see Manual Research Recommendations).
> **Outreach Angle:** *"You raised in August to expand internationally. Your terms say the only way an overseas user can fund a wallet is a card — net banking and UPI don't exist outside India. Curious how you're thinking about the rails in those markets."*
> **Suggested Subject Line:** `the rail question behind the $12M`

> ### **Insight #2: Their own gateway published that cross-border failure was the problem — and named cards as the whole solution**
> **Evidence:** **S3A/S7** — Razorpay's case study: *"Payment failures were a major hurdle"* across *"North America, European, SEA, and the MENA region"*, and *"over 80% of InstaAstro's international transactions via cards"* **+ S3B** — single PSP, no orchestrator, no failover **+ S2** — no local entity in any of those regions.
> **Pain Point:** A concentration risk stated by the provider itself. Over 80% of international volume on one method through one provider means no second path when an issuer, a BIN range or the provider itself has a bad hour — and nothing to route to.
> **Yuno Value Proposition:** Multi-acquirer routing and failover on the international corridor specifically, with retry logic informed by decline code and issuer rather than a fixed schedule — and local acquiring in the markets where the diaspora's cards are actually issued.
> **Best Success Case:** As above.
> **Outreach Angle:** *"Razorpay's own write-up of your business says cross-border payment failures were a major hurdle, and that cards carry over 80% of your international volume. That's a lot of weight on one method and one provider."*
> **Suggested Subject Line:** `"a major hurdle" — their words, not mine`

> ### **Insight #3: Unlike their closest competitor, all of this revenue is actually addressable**
> **Evidence:** **S8A** — Apple's own product JSON returns `hasInAppPurchases: false` for `com.instaastro.onlineastrology` on both US and India storefronts, against six known-true controls in the same payload; Play carries no IAP badge **+ S11** — `astrotalk.md` verified Apple IAP **live** at Astrotalk with nine USD wallet-recharge tiers, and my own probe returns `true` for `codeyeti.com.AstroYeti`.
> **Pain Point:** Internal qualification point rather than a customer pain. Astrotalk surrenders 15–30% of every iOS recharge to Apple and cannot route it. InstaAstro keeps the billing relationship on every platform — which means the full top-up book is routable, and also that **InstaAstro owns 100% of the approval-rate risk** that Astrotalk partly outsources to Apple.
> **Yuno Value Proposition:** The entire revenue base is in scope for routing, tokenisation, retries and local acquiring. There is no untouchable majority.
> **Best Success Case:** As above.
> **Outreach Angle:** ⚠️ **Internal use only — do not put a competitor's billing architecture in an email.** Use it to justify prioritising this account over its larger competitor.
> **Suggested Subject Line:** *n/a — not an outreach insight.*

> ### **Insight #4: Profit collapsed while revenue doubled, so cost of acceptance is a board-level number this year**
> **Evidence:** **S2/S12** — registry FY25 movements: Total Revenue **↗108.34%** but EBITDA **↘65.20%**, Net Profit **↘67.93%**, Networth **↘215.33%**, Borrowings **↗599,900%** ([Falcon Ebiz](https://www.falconebiz.com/company/INSTAASTRO-TECHNOLOGY-PRIVATE-LIMITED-U72900UP2021PTC145574)) **+ S6** — a US$12M round closed six months into the following year **+ S6** — **no payments hire exists**, so the decision sits with the founder or finance.
> **Pain Point:** A company that doubled revenue into a profit decline and negative net worth, then raised, is under direct pressure on unit economics. MDR on cross-border card volume and revenue lost to declines are both line items on that P&L, and nobody in the company owns them.
> **Yuno Value Proposition:** PSP diversification to pull down blended MDR on the international corridor, and recovered revenue from authorisations that currently fail — framed as margin, not as technology.
> **Best Success Case:** As above.
> **Outreach Angle:** *"Most of the orchestration conversations I have start with growth. Given where your FY25 numbers went, I suspect yours would start with cost of acceptance on the international book."*
> **Suggested Subject Line:** `cost of acceptance on the 25%`

> ### **Insight #5: The investor thesis is the second purchase — which is exactly what a stored card decides**
> **Evidence:** **S6** — Artha's Anirudh Damani: *"The first consultation is marketing. The second one is a business."* ([ISN](https://indianstartupnews.com/funding/online-astrology-and-spiritual-wellness-platform-instaastro-raises-12-million-in-series-a-funding-12443449)) **+ S3A** — card-on-file tokenisation live via one unnamed aggregator ([Privacy Policy](https://instaastro.com/privacy-policies/)) **+ S5** — a Play review alleging a stored card charged beyond intent and surviving deletion, plus their own Terms warning users to *"ensure their bank hasn't been debited before retrying payment"*.
> **Pain Point:** The business model depends on the repeat top-up, and the repeat top-up depends on a stored credential authorising cleanly on a cross-border leg. A failed second top-up looks exactly like churn in the cohort data, and a duplicate one generates a refund and a one-star review.
> **Yuno Value Proposition:** Network tokens and account-updater inside the routing layer so credentials refresh without a per-PSP project; decline-code-aware retries; and a single view of failed top-ups instead of one provider's dashboard.
> **Best Success Case:** As above.
> **Outreach Angle:** *"Your lead investor's line was that the second consultation is the business. On a cross-border stored card, whether there is a second one is partly a payments question — what does your first-repeat top-up success rate look like?"*
> **Suggested Subject Line:** `"the second one is a business"`

---

## Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. *"You raised $12M in August to expand internationally — and your own terms say an overseas user's only way to fund a wallet is a card, because net banking and UPI stop at the Indian border."*
2. *"Razorpay's write-up of your business says cross-border payment failures were 'a major hurdle', and that cards carry over 80% of your international volume — that's a lot of weight on one method through one provider."*
3. *"A quarter of your revenue comes from the diaspora, and there's no InstaAstro entity outside India — so every one of those authorisations is cross-border from Noida."*

**Cold call openers (conversational, one sentence each):**
1. *"I read your Series A coverage — the international expansion line. Can I ask what the payment side of that plan looks like, because today it reads as cards-only outside India?"*
2. *"Your investor said the first consultation is marketing and the second is the business — how much visibility do you have into whether the second top-up actually authorises?"*
3. *"Your refund policy tells users to check their bank hasn't been debited before retrying — how often does that one come up?"*

⛔ **Never use:** "one in five of your international payments fails" (the 80% is a volume share) · any transaction-count figure (assumed) · the refund and pricing complaints (orchestration doesn't fix them) · any competitor-orchestrator name.

---

## Section 11: Similar Companies & Prospecting Pipeline

**Mined from `2-ready-to-outreach/astrotalk.md` as instructed — Astrotalk was NOT re-researched.** New-to-repo findings this run are marked ⭐.

### 11A. Direct Competitors

| Company | Website | HQ | Est. Size | Overlap Markets | Known PSP / Orchestrator | Source |
|---|---|---|---|---|---|---|
| **Astrotalk** | astrotalk.com | Noida, India | FY25 income **₹1,214 Cr**, PBT ₹285 Cr, **$1Bn** | India, US, UK, CA, AU | **Razorpay direct** + Shopify Payments + PayPal + GoKwik + **Apple IAP live** | `astrotalk.md` (19/29 ⭐) |
| **Astroyogi** (Netway India Pvt Ltd) | astroyogi.com | India | ~₹96 Cr FY25, **bootstrapped, profitable** | India, US, UK | ⭐ **Juspay HyperSDK + Razorpay + PayPal (USD) in their own markup — commented out.** Angular, Cloudflare, no CSP | Fetched 2026-10-12 |
| **AstroSage** (Ojas Softech) | astrosage.com | Noida, India | ₹84 Cr FY25 (+40%), unfunded since 2004 | India | Not found. ⭐ `com.ojassoft.astrosagekundli` → **no Apple IAP** | `astrotalk.md`; Apple JSON |
| **AppsForBharat / Sri Mandir** | srimandir.com | Bengaluru, India | FY25 ₹82.2 Cr (+341%), ₹175 Cr Series C | India + diaspora | Not found | `astrotalk.md` |
| ⭐ **Melooha** | — | India | Not found | India, US | ⭐ `com.melooha.app` → **Apple IAP live** | Apple JSON |
| ⭐ **Bodhi** | — | Ghaziabad, India | Seed-stage | India | ⭐ `com.bodhiastrology.app` → **no Apple IAP** | Apple JSON; `astrotalk.md` |
| ⭐ **AstroLokal** | — | India | Not found | India | ⭐ `com.astrolokal.astrology` → **no Apple IAP** | Apple JSON |
| ⭐ **Kasamba** | kasamba.com | US / Israel | Not found | US | ⭐ `com.kasamba.ios` → **no Apple IAP**. **Western incumbent in the diaspora corridor** | Apple JSON |

### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---|---|---|---|---|---|
| **Astrotalk** | astrotalk.com | Astrology marketplace | IN/US/UK/CA/AU | Same wallet top-up unit, same Razorpay-direct stack, same diaspora corridor, **also no entity outside India** | `astrotalk.md` |
| **Astroyogi** | astroyogi.com | Astrology marketplace | IN/US/UK | Same model; **bootstrapped ⇒ MDR is a felt cost.** Lead on cost, not growth | Fetched; TAL |
| **AppsForBharat** | srimandir.com | Devotional / pooja seva | IN + diaspora | ⭐ **Direct overlap with InstaAstro's new Pooja Seva arm.** `astrotalk.md` records overseas ARPU ~₹7,000 vs ₹600–800 domestic — **their most valuable users are their hardest to approve** | `astrotalk.md` |
| ⭐ **"Pooja" app** (`com.at.pooja`) | — | Pooja seva | IN | Apple IAP live; same category as `puja.instaastro.com` | Apple JSON |
| **AstroSage** | astrosage.com | Kundli / reports | IN | Confirm it runs a paid per-minute marketplace before prospecting | `astrotalk.md` |
| **Clickastro** | clickastro.com | Report sales | IN | Report sales, not a marketplace — **different billing unit, park it** | `astrotalk.md` |

### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator | Date | Vertical | Source |
|---|---|---|---|---|
| **Astroyogi** (Netway India) | **Juspay HyperSDK** — ⚠️ **integration present in production markup but commented out** | Unknown; observed 2026-10-12 | Astrology consultation | Fetched https://www.astroyogi.com/ |

**This is the only orchestration evidence in the vertical, and it is qualified.** Astroyogi's live homepage contains, inside a **single HTML comment**: Juspay's `PIL.js`, Juspay's `hyper-sdk-web/JuspayPaymentsInterface.js`, Razorpay's `checkout.js`, and a **production PayPal SDK with `currency=USD`** (plus a separately commented **sandbox** PayPal tag — a signature of active development work).

🔒 **Two PayPal client-ids (production and sandbox) are present on that page. `[live key present — value deliberately not recorded]`** — they prove PayPal only, and they are not transcribed here.

**What this does and does not establish.** It establishes that **Astroyogi built against Juspay's orchestrator and against PayPal in USD** — you do not carry those exact release URLs without having integrated them. It does **not** establish live production use, because the block is commented and the homepage is not their checkout (an Angular SPA that loads payment code on route).
⇒ **The TAL's `Astroyogi → Juspay` cell is now better supported than it was, but still short of confirmed.** Recommend changing it to `Juspay (integration evidenced in source, live status unconfirmed)` rather than leaving it as a bare assertion.
⭐ **And the competitive point that matters more than the orchestrator:** **Astroyogi built PayPal in USD. InstaAstro's own Terms offer the diaspora cards and nothing else.**

### 11D. Prospect Scoring

Applied to the two best new prospects only — the rest lack the sourced signals to score honestly.

| Company | Signal | Points | Status | Evidence Source |
|---|---|---|---|---|
| **Astroyogi** | Orchestration status | **+1** | ⚠️ Orchestrator integration evidenced ⇒ not greenfield | Fetched markup |
| | 3+ countries | ⬜ 0 | No traffic data held | — |
| | Multiple PSPs | **+3** | ✅ Juspay + Razorpay + PayPal all in own markup | Fetched markup |
| | Payment job postings / funding / expansion | 0 | Bootstrapped, nothing found | `astrotalk.md` |
| | **Subtotal** | **~4 + unscored volume** | 🟢 **Real but a different sale** — orchestration-aware, so coverage and reach, never education | — |
| **AppsForBharat** | Local rail / cross-border gap | **+3** | ✅ Overseas ARPU ~₹7,000 vs ₹600–800 domestic | `astrotalk.md` |
| | Funding >$10M | **+2** | ✅ ₹175 Cr Series C | `astrotalk.md` |
| | Recent expansion | **+2** | ✅ FY25 revenue +341% | `astrotalk.md` |
| | Orchestration status | ⬜ 0 | Not found — needs the Section 3B check | — |
| | **Subtotal** | **~7 + unscored** | ⭐ **Sharpest unworked prospect in the vertical** | — |

### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|---|---|---|---|---|---|---|---|
| 1 | **InstaAstro** | Target | IN, US, CA, UK, AU | **18/29** | ⭐ | $12M raise + cards-only international + **no IAP** | ✅ **Yes — orchestrator cell WRONG, correction logged** |
| 2 | **Astrotalk** | Direct competitor | IN, US, UK, CA, AU | 19/29 | ⭐ | Razorpay-direct, pre-IPO, CFO hired | ❌ **No — genuine gap** |
| 3 | **AppsForBharat / Sri Mandir** | Peer | IN + diaspora | ~7+ | ⭐ | Overseas ARPU ~10× domestic | ❌ **No — genuine gap** |
| 4 | **Astroyogi** | Direct competitor | IN, US, UK | ~4+ | 🟢 | Orchestration-aware; bootstrapped ⇒ cost-led | ✅ Yes (P2) |
| 5 | **AstroSage** | Peer | IN | Unscored | 🟢 | ₹84 Cr FY25, unfunded; confirm marketplace model | ❌ No |
| 6 | **Melooha** | Competitor | IN, US | Unscored | 🟢 | ⭐ Apple IAP live ⇒ check the split before investing time | ❌ No |
| 7 | **Kasamba** | Western incumbent | US | Unscored | 🟢 | ⭐ No Apple IAP; US-side comparator | ❌ No |
| 8 | **Bodhi** | Competitor | IN | Unscored | 🔴 | Seed-stage — too small for now | ❌ No |
| 9 | **AstroLokal** | Competitor | IN | Unscored | 🔴 | No scale evidence | ❌ No |
| 10 | **Clickastro** | Adjacent | IN | Unscored | 🔴 | Report sales, different billing unit — park | ❌ No |

⭐ **Genuine finds not on `accounts/apac-tal.csv`: Astrotalk, AppsForBharat/Sri Mandir, AstroSage, Melooha, Kasamba, Bodhi, AstroLokal.** **Astrotalk is the glaring one** — a ₹1,214 Cr, 19/29 ⭐ account already fully researched in this repo and **still absent from the target account list.**
⚠️ **Correction carried forward from `astrotalk.md`:** Bodhi is **not** a ShareChat/Moj company — independent, Ghaziabad, seed-stage.

---

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|---|---|---|
| **Annual Revenue** | **FY26 ₹111.26 Cr (~US$11.71M)**; FY25 **₹52 Cr (~US$5.47M)** | [Entrepreneur India](https://india.entrepreneur.com/business-news/instaastro-crosses-inr-200-crore-in-annualized-revenue-raises-usd-12-million-series-a) + [ISN](https://indianstartupnews.com/funding/online-astrology-and-spiritual-wellness-platform-instaastro-raises-12-million-in-series-a-funding-12443449), both fetched. ⚠️ **Company-stated in press, NOT an MCA filing** — registry shows financials last filed 31 Mar 2025 |
| Annualised run-rate | **₹200 Cr+ (~US$21M)** | Same. ⚠️ **Company claim** |
| Independent corroboration | FY25 **Total Revenue ↗108.34%** (consistent with ~₹25 Cr → ₹52 Cr) | [Falcon Ebiz](https://www.falconebiz.com/company/INSTAASTRO-TECHNOLOGY-PRIVATE-LIMITED-U72900UP2021PTC145574), fetched |
| FY25 profitability | **EBITDA ↘65.20% · Net Profit ↘67.93% · Networth ↘215.33% · Borrowings ↗599,900% · Assets ↗98.90%** | Same. ⚠️ Percentage movements only; absolutes paywalled |
| GMV / Gross Transaction Volume | **No public data found** | ⚠️ **Unknown whether the ₹111.26 Cr is gross wallet collections or net commission.** As a revenue-share marketplace paying 5,000+ experts, the two could differ several-fold. **This materially changes the business case and the transaction count** |
| **Average Transaction Value** | ❌ **NOT FOUND.** Only a sourced **floor: ₹100 minimum recharge** | Homepage, fetched: *"INR 100. You need to recharge in order to talk to"*; *"Recharge and add money to your wallet. Choose any amount that suits you"*. Entry price **₹1** for a first call/chat |
| **Billing unit** | ⭐ **ONE WALLET TOP-UP = ONE TRANSACTION.** Consultations draw down the balance and are **NOT** separate transactions | ✅ **SOURCED**, [Terms](https://instaastro.com/terms-and-conditions/): *"All payments … must be made exclusively through the Registered Member's InstaAstro Wallet"* |
| Est. Annual Transactions | **≤1.11M** (FY26 rev ÷ ₹100 floor) to **≤2.0M** (run-rate ÷ ₹100 floor) — **ceilings, not estimates** | Calculated. The floor on ATV produces a ceiling on count |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ~40,000–50,000/month. [ASSUMPTION — not researched.]** **Ceiling ≤92,700/month** (₹111.26 Cr ÷ ₹100 ÷ 12) or **≤166,700/month** on the run-rate. At a plausible ₹300–500 average top-up: **~33,000–67,000/month**. ⛔ **The under-40,000 auto-reject does NOT fire — the input is assumed, and an assumption never rejects an account.** Scored at the 40,000–49,999 band (+2), conservatively | **ASSUMED.** Revenue sourced; **average top-up value NOT sourced.** Per the disclosure rule, an unsourced input makes the output an assumption regardless of the arithmetic |
| Active Customers / Users | **12 million registered users** (up ~400% in 2 years); **5,000+ verified experts**; **183 countries** | Press, fetched. ⚠️ **Registered, not active.** ⚠️ **Reconcile against Google Play's 1M+ downloads and 19,180 iOS India ratings — "12M registered" is not an active-user figure and must not be used as one** |
| App scale, verified by me | **Play: 1M+ downloads, 4.x** · **App Store India: 19,180 ratings, 4.48, Chart #23 in Lifestyle** · **App Store US: 977 ratings, 4.5** · iOS released **02 Feb 2021**, current v2.0.30, **21 Sep 2026** | Play listing + Apple lookup API, both fetched |
| Razorpay-era scale (Feb 2025) | **1,500+ astrologers · 4 crore (40M) call/chat minutes · 50 lakh+ customers** | Razorpay case study, fetched |
| **Primary Currency** | **INR.** No USD/GBP/AUD/CAD/AED marker found on any fetched page | First-hand grep of homepage, `/shop/`, Terms |
| Top 3 Markets by Revenue | **India (~75%)**; **international ~25% combined, "driven largely by the Indian diaspora"** — no country-level revenue split published | Press, fetched. Traffic suggests US > Australia > Canada > UK within that 25% |
| **Billing channel split (web vs app store)** | ⭐ **RESOLVED, unusually for this vertical: effectively 0% app-store.** No Apple IAP (`hasInAppPurchases: false`, both storefronts, six controls); no Play IAP badge. **100% direct gateway.** ⚠️ Web-vs-app *gateway* split is undisclosed, but **there is no web checkout**, so it is overwhelmingly in-app-via-own-gateway | Section 8A |
| Funding to date | **US$12M Series A (27 Aug 2026)** + ₹18.5 Cr pre-Series A + ₹3.2 Cr seed (Nov 2021). Cumulative reported ~**$14.73M**. **No valuation disclosed** | Press, fetched; prior rounds `[UNVERIFIED — search summary]`. ⚠️ **CB Insights' "$2.73M over 2 rounds" contradicts everything else — disregard** |
| Market context | India astrology app market **US$163M (2024) → US$1.8B (2030)** per MarkNtel Advisors; **1,400+ religion-tech startups** per Tracxn | Entrepreneur India, fetched (secondary citation) |

---

## Overall Research Confidence

**MEDIUM–HIGH**, with one sharply defined hole.

**Strong coverage, verified by me directly this run:** the funding round (amount, both leads, exact date, use of proceeds — three independently fetched pages) · the orchestrator question (re-verified against the gateway's own case study with a 93/0 control, plus five of the merchant's own production assets) · the legal entity, CIN, incorporation date, capital, directors and FY25 financial movements (registry, fetched) · the HQ (three concordant sources, Gurugram rejected) · **the billing unit and the complete top-up method list, from the merchant's own Terms** · card-on-file tokenisation via a single unnamed aggregator (Privacy Policy) · **the app-store billing split, resolved decisively from Apple's own product JSON on two storefronts against six known-true controls** · the absence of a web checkout, proven with a byte-identical soft-404 control · INR-only pricing · Astroyogi's commented-out Juspay HyperSDK · the Australian rail shares (RBA, fetched).

**Traffic data was SUPPLIED**, not API-sourced and not estimated — `accounts/traffic/instaastro.md`, SimilarWeb Jul–Sep 2026, all-country-domains ON. It drives the country profile, the APM gap analysis and two ICP rows, and its analyst notes were honoured without adjustment: **India stays at 62.80%** (so "high traffic outside home" scores 0), the five junk-traffic markets are excluded from every market claim, and the declining-Western-markets counter-read is stated wherever expansion is discussed.

**The hole, stated plainly:** **average wallet top-up value could not be found anywhere**, so the monthly transaction count — the one ICP signal that can reject an account on its own — is an **assumption**, and it sits close to the 40,000/month floor. Compounding it, **it is unknown whether the ₹111.26 Cr is gross wallet collections or net commission**, which could move the count several-fold in either direction. **Everything about this account is well evidenced except its size.**

**Confidence downgrades applied:** Section 8 (Checkout Experience Audit) **cannot be completed** — there is no web checkout and the payment surface is inside the mobile binaries. The **CSP-as-asset-map technique was unavailable** (no CSP header is served). **No APK was decompiled** in this run, which is where the remaining answers live.

**Execution deviation, disclosed as instructed:** the `research` method specifies five parallel agents with per-agent budgets. **I do not have the Agent/Task tool in this environment and could not spawn subagents.** I ran Phases 1→2→3 **single-threaded myself**, treating the per-agent budgets as per-workstream totals. Approximate spend: **13 web searches** and **~22 fetches** (via `curl --compressed`, since the method's `curl` fallback path proved more reliable and allowed byte-level control for the grep work). `zaubacorp.com` and `thecompanycheck.com` were **blocked/403** as warned; `yourstory.com` returned **403**; `tofler.in` returned **503** for the InstaAstro entity but **200** for MANK. `inc42.com` **did fetch successfully** this session, contrary to the prior-session warning — worth noting for future runs.

---

## Manual Research Recommendations

> **Area:** ⭐⭐ **Average wallet top-up value, and whether revenue is gross collections or net commission.** *(#1 — everything else is secondary.)*
> **Why it matters:** It is the only thing standing between this account and either a sized business case or an honest rejection. The monthly transaction count is currently an **assumption** that straddles the ICP volume floor; at an average top-up above ~₹420 on the current run-rate the account falls below 40,000/month.
> **Suggested manual action:** Two discovery questions — *"what's your average recharge size?"* and *"is the ₹111 Cr gross wallet collections or your net take?"* Neither is findable publicly; both are easy to ask.

> **Area:** ⭐ **Walk a real recharge in the Android app, from an Indian IP and again from a US or Australian IP.**
> **Why it matters:** It is the only remaining way to settle four things at once — the actual method sheet per geography, the display currency, whether UPI Autopay or any wallet rail exists, and **whether any orchestrator SDK sits inside the binary** (the one scenario that would flip this from greenfield to displacement). The web cannot answer any of it.
> **Suggested manual action:** Install `com.instaastro.onlineastrology`, start a top-up, capture the network trace. Optionally pull the APK and grep for vendor SDK package names.

> **Area:** The identity of the RBI-authorised **"payment gateway aggregator"** named only generically in the Privacy Policy.
> **Why it matters:** Razorpay's case study is from **February 2025** — twenty months old. It is the sole PSP evidence in this file and the relationship may have changed. The whole motion rests on it being current.
> **Suggested manual action:** The recharge trace above settles it. Failing that, ask directly on the call — it is not a sensitive question.

> **Area:** The named target markets behind the Series A.
> **Why it matters:** They publicly said "regional and international markets" and **named no country**. The corridor in this report is inferred from traffic, their 25%-diaspora statement and Razorpay's Feb-2025 region list — **it is not their stated plan**, and outreach must not pretend otherwise.
> **Suggested manual action:** Ask. It is the natural opening question and it qualifies the account in one answer.

> **Area:** The Yuno success case to pair with this profile.
> **Why it matters:** No published Yuno case matching an India-HQ'd, app-first, wallet-top-up consultation marketplace with a diaspora corridor was identified from sources available in this run, and repo policy forbids naming a customer without a public reference or attaching a number to one without published metrics. **I left it unfilled rather than guessing.**
> **Suggested manual action:** Pick from Yuno's current approved reference list on the structural match — single-gateway merchant, funded international expansion, cross-border card concentration.

> **Area:** **Astrotalk is not on `accounts/apac-tal.csv`.**
> **Why it matters:** A ₹1,214 Cr, 19/29 ⭐ account, already fully researched in this repo, is missing from the target list — along with AppsForBharat, AstroSage, Melooha and Kasamba.
> **Suggested manual action:** Add them. The research is already done for Astrotalk.

> **Area:** Astroyogi's live checkout (not its homepage).
> **Why it matters:** If the Juspay integration is live rather than dormant, the "competitor using orchestration" signal hardens from qualified to confirmed, and the +2 ICP row becomes unimpeachable. If it is dead, that row should come off and InstaAstro scores 16 → 🟢 Medium.
> **Suggested manual action:** Walk Astroyogi's recharge flow with DevTools and watch for `payments.juspay.in` on the wire.

---

## ⛔ Repo maintenance actions from this run

1. **TAL correction — `accounts/apac-tal.csv`, InstaAstro row, `Payment Orchestrator` cell: clear `Juspay`.** Independently re-verified as unsupported (details in Section 3B). The motion is **Greenfield / Razorpay direct**. *(Not edited by me — Prateek audits first.)*
2. **TAL refinement — Astroyogi row, `Payment Orchestrator`:** change the bare `Juspay` to `Juspay (integration evidenced in own source, commented out; live status unconfirmed)`.
3. **TAL additions:** Astrotalk, AppsForBharat/Sri Mandir, AstroSage, Melooha, Kasamba.
4. **New false positives for the permanent trap list:**
   - ⭐ **`cin` → `pricing`.** A grep for "CIN" on InstaAstro's legal pages returns 6–8 hits; **every one is the substring inside "pri-CIN-g".** No CIN is disclosed on the site at all.
   - ⭐⭐ **`In-App Purchases` on Apple pages uses U+2011 (NON-BREAKING HYPHEN), not `-`.** A plain-hyphen `grep -F "In-App Purchases"` returns **ZERO on a page that contains ten of them.** This is the smart-quote trap in a new costume and it nearly produced a false negative on the single most important question in this account. **Always test `-` and `‑` (`$'\xe2\x80\x91'`).**
   - ⭐ **Google Play and Apple "similar apps" carousels embed neighbouring apps' price ranges and IAP badges.** All three `"per item"` price strings on InstaAstro's Play page belong to `com.vetrov.astromagic`, `com.feelweel.astro` and `com.vedicastrology`. **Always pair a flag to its `bundleId` before believing it.** (`astrotalk.md` logged this trap; it fired again here exactly as predicted.)
   - **`upi` → `Jupiter`** and **`emi` → `Gemini` / `Feminine`** — confirmed independently. On an astrology merchant both are useless as bare tokens.
   - **`stripe` → `.scrolling-stripe` / `.stripe-text`** CSS, 42 hits, zero PSP.
   - **A 200 response is not a page.** `instaastro.com` serves a **byte-identical 119,223-byte catch-all** on every unknown path, including `/recharge`, `/wallet`, `/checkout`, `/payment` and `/pay`. Always fetch a deliberate nonsense control and compare sizes.

---

## Appendix: All Source URLs

**Fetched directly this run (primary evidence):**
- https://instaastro.com/ — homepage, headers, billing-unit copy, Branch deeplink, currency
- https://instaastro.com/privacy-policies/ — operating entity, CoF tokenisation, "payment gateway aggregator"
- https://instaastro.com/terms-and-conditions/ — ⭐ billing unit, complete top-up method list, refund/duplicate-payment clauses, jurisdiction
- https://instaastro.com/shop/ — spiritual commerce property
- https://puja.instaastro.com/ — Pooja Seva property, separate codebase
- https://razorpay.com/blog/razorpay-supercharged-instaastros/ — ⭐ PSP case study, re-verified 93/0/0
- https://play.google.com/store/apps/details?id=com.instaastro.onlineastrology&hl=en_IN&gl=IN — developer entity + Noida address, 1M+ downloads, no IAP badge, payment reviews
- https://apps.apple.com/us/app/instaastro-talk-to-astrologer/id1547565515 — ⭐ `hasInAppPurchases: false` + controls
- https://apps.apple.com/in/app/instaastro-talk-to-astrologer/id1547565515 — ⭐ same, India storefront
- https://itunes.apple.com/lookup?id=1547565515&country=in — MANK Technology as seller, ratings, release dates
- https://india.entrepreneur.com/business-news/instaastro-crosses-inr-200-crore-in-annualized-revenue-raises-usd-12-million-series-a — ⭐ funding, FY25/FY26 revenue, founder quote
- https://indianstartupnews.com/funding/online-astrology-and-spiritual-wellness-platform-instaastro-raises-12-million-in-series-a-funding-12443449 — ⭐ funding, Noida, prior rounds, investor quote
- https://inc42.com/buzz/instaastro-bags-12-mn-to-build-ai-tools-expand-online-pooja-services/ — ⭐ funding, date 27 Aug'26, ₹114.5 Cr
- https://www.falconebiz.com/company/INSTAASTRO-TECHNOLOGY-PRIVATE-LIMITED-U72900UP2021PTC145574 — ⭐ CIN, capital, directors, FY25 movements
- https://www.tofler.in/mank-technology-private-limited/company/U72900DL2008PTC185604 — MANK shell confirmation
- https://www.astroyogi.com/ — ⭐ competitor Juspay HyperSDK + Razorpay + PayPal (commented)
- https://support.google.com/googleplay/android-developer/answer/13306652?hl=en — Google Play India alternative billing, live-sourced
- https://www.rba.gov.au/publications/bulletin/2026/may/consumer-payment-behaviour-in-australia.html — ⭐ Australian online-payment rail shares

**Fetch attempted and blocked/failed:** `yourstory.com` (403) · `thecompanycheck.com` (403) · `tofler.in` InstaAstro entity (503) · `zaubacorp.com` (not attempted — known blocked)

**Search-summary only, `[UNVERIFIED]`:** CB Insights InstaAstro financials · prior-round details (₹3.2 Cr seed, ₹18.5 Cr pre-Series A) · nominee-director date · Jan 2025 Razorpay/Cashfree orchestrator suspensions · App Store review content · job listings (Glassdoor, Indeed, Internshala, NextLeap, Jobaaj) · Razorpay Apple Pay launch and tokenisation blog posts

**Repo sources:** `accounts/traffic/instaastro.md` (supplied SimilarWeb) · `accounts/apac-tal.csv` · `1-to-outreach/instaastro.md` · `2-ready-to-outreach/astrotalk.md` · `.claude/reference/apac-payments.md` · `.claude/reference/subscription-payments.md`

</details>
