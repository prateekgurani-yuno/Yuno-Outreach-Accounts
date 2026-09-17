# Ticketek

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 16 / 29 → ⭐ **High Priority** (upward analyst override — see breakdown)
**Industry:** Live event ticketing (primary sale + owned secondary marketplace), agent-of-seller model · **HQ:** Sydney, Australia — **Ticketek Pty Ltd (ABN 92 010 129 110)**, part of **Ticketek Entertainment Group (TEG)**, owned by **Silver Lake** since 2019–20 · **Researched:** 2026-09-17 · **First email sent:** —
**Motion:** **In-house** — TEG operates its own payment layer, **"Softix PayGate"**, on its own `pay.` subdomains in at least AU and NZ. Verified first-hand. Respect the build; anchor on opportunity cost and reach, never "you need orchestration".

---

> ## 🎯 THE HOOK — they have documented their own false-decline problem for seven years and it is still there
>
> **2019.** Ticketek's own help centre, verbatim, captured 11 March 2019:
>
> > *"Ticketek uses a **third party verification system** for online transactions. When a transaction doesn't pass this verification **it may decline the purchase**. **Multiple attempts on the same account/name or using other cards in the account may result in the same decline message.** When you receive this **we cannot permit the transaction at that time online**, you will need to contact our call centre or visit an agency in person to transact with us. Please note that our call centre and agencies **are unable to sell tickets during online only pre-sales**. Check event pages for any special conditions, **some events may have all sales online only.**"*
>
> Read the last two sentences together. A false decline during an **online-only pre-sale** — the highest-intent, highest-value, most time-boxed inventory they sell — has **no recovery path at all**, by their own documentation. The customer cannot phone it in. There is no channel left.
>
> **2026.** Same article, same ID, retitled to foreground 3DS, updated 22 January 2026:
>
> > *"If you reach the purchase page, enter your card details, **complete the 3D Secure verification, but still receive a credit card error**, the issue may be related to the 3D Secure process. While we can't comment on individual cases… you will need to follow up directly with your issuing bank."*
>
> **Seven years apart, same admission: good customers, correctly authenticated, still declined.** The article was rewritten. The problem wasn't fixed. And 2019's readers agreed — *"2 out of 9 found this helpful."*
>
> **The timing is the second half of the hook.** New CEO Cameron Hoy since 1 June 2026, a cost-reduction programme cutting ~5.5% of the workforce, and **two flagship venue contracts lost — Venues NSW to Ticketmaster and Melbourne Park to AXS**. Conversion is no longer a finance line. It is a competitive retention argument in front of every venue client they have left.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Ticketek is Australia and New Zealand's largest ticketing company and the engine of **TEG**, which on its own homepage says it sells **30 million tickets a year** across **"more than 30 brands in 40 countries on six continents."** Ticketek sells **as agent for the venue or promoter** — it collects the money and remits to the seller — and also owns and operates **Ticketek Marketplace**, a capped-price resale platform with its own payout obligations. Silver Lake has owned TEG since 2019–20.

**SimilarWeb total visits:** **~7.74M/month combined** — `ticketek.com.au` **7.1M** (global #7,003; **#1 in Ecommerce > Tickets, Australia**) + `ticketek.co.nz` **638.5K** (NZ +22.1% MoM). `[ESTIMATE, not confirmed]` — SimilarWeb free tier, agent-sourced, **I could not re-fetch it myself**. **Roots only: `premier.*` is a subdomain of each root and its visits are a subset, not an addition — they must not be summed.**

> ⚠️ **Almost the entire Ticketek estate is WAF'd.** `premier.ticketek.com.au`, `www.ticketek.com.au`, `marketplace.ticketek.com.au` and `www.eventopia.co` all return a **byte-identical 6,674-byte Akamai block page** (`AKA_A2` cookie, `akamai-grn` header) — the same custom-branded *"Something doesn't feel quite right…"* page, titled "Ticketek Australia", on all four. That is one shared front door across the primary site, the resale marketplace and Eventopia. **Section 8 could not be completed by walking the live checkout.** Everything below came from routes around it: the open Zendesk help-centre APIs, the un-WAF'd `pay.` payment hosts, TEG's own site, and the Wayback Machine.

### Markets
| Rank | Market | Traffic | Accepted methods (first-party, enumerated) | Missing methods | Local entity |
|---|---|---|---|---|---|
| 1 | **Australia** | **82.6%** · ~6.39M/mo `[EST]` | Visa, Mastercard, Amex · **Afterpay** · **Google Pay** · **Apple Pay** · **PayPal** (+ Pay in 4) · Ticketek Gift Voucher/Gift Card · **Qantas Points** (Points Plus Pay, split-tender with cash) | **BPAY — SOURCED ABSENT** · **PayTo — SOURCED ABSENT** · Zip, POLi, humm, Latitude, Klarna — absent | ✅ Ticketek Pty Ltd (ABN 92 010 129 110) |
| 2 | **New Zealand** | **10.5%** · ~815K/mo `[EST]` | **Cards + Afterpay only** | **Apple Pay, Google Pay and PayPal all absent as payment methods** — see the asymmetry below | ✅ Ticketek New Zealand Ltd |
| 3 | United States | 3.5% `[EST]` | — | — | ❌ none — diaspora/bot, not a market |
| — | **Singapore · Malaysia · Philippines · UK** | **Not measured** — these properties were never pulled | Not established | Not established | ✅ **TEG wholly-owned ticketing brands** — see below |

*Also: India 0.5%, UK 0.4%, "other" 2.4%. **SimilarWeb's free tier exposes only five countries per domain**, so ranks 7–10 do not exist in the data. **AU + NZ = 93.1% of measured traffic — this is a two-market business by volume.** The in-territory Asian properties were not measured at all, and those are precisely the ones an APM pitch hangs on.*

*Ticketek's AU **Payment Methods** article is a genuine first-party enumeration, last updated **21 January 2026**. It hedges with "including", so treat the absences as strong rather than absolute — but BPAY and PayTo do not appear anywhere in a help centre where **Afterpay, Google Pay, Apple Pay and PayPal each get their own dedicated article**.*

### ⚡ The asymmetry inside their own stack — AU vs NZ
Two independent, separately-sourced versions of the same gap:

1. **Payment methods.** AU's own article says *"Apple Pay **was launched for Australian sites**"*. The NZ help centre documents **only cards and Afterpay** — its "Apple Wallet and Google Pay" article is about *storing a ticket*, not paying, and still refers to *"the new iPhone 5"* and *"iOS 6"*.
2. **Monitoring.** `pay.ticketek.com.au` carries a full **Dynatrace RUM agent**; `pay.ticketek.co.nz` is the same page **with no Dynatrace tag at all** (2,482 bytes vs 854). **Australia's payment page is instrumented. New Zealand's is not.**

### Legal entities
- **Ticketek Pty Ltd — ABN 92 010 129 110 / ACN 010 129 110** — the contracting entity, named in the first line of Ticketek's own Terms and Conditions of Sale, **independently confirmed on ABN Lookup** (active from 1 Nov 1999; Level 3, 175 Liverpool St, Sydney NSW 2000). Trading names include **EZYTICKET** and **OVATION AMP**
- **Ticketek New Zealand Limited** — **company no. 670708, NZBN 9429038502545**, Registered
- **Amplify Bidco Pty Ltd — ABN 30 636 456 623** — ⚠️ **the Silver Lake acquisition vehicle and the ASIC-filing head entity, trading as TEG.** This is the consolidated reporting entity
- **TEG Pty Limited — ABN 78 604 938 534**; **TEG Ticketing Asia Pte. Ltd. — UEN 201617731H** (Singapore, `[UNVERIFIED — not confirmed against a register]`)
- **TEG Rewards Pty Ltd**, **Eventopia Pty Ltd** — named as related companies in TEG's privacy policy
- **Group companies confirmed in:** *"New Zealand, Malaysia, Philippines, Singapore, Hong Kong, European Union, United Kingdom and the United States"* — TEG's own words
- Personal data *"may also be processed in… **The Philippines and New Zealand**"* — the Philippines reads as an offshore operations centre (corroborated by the restructure cutting 2 Philippines roles)

### 🌏 TEG's ticketing brands — from TEG's own brand page, headed *"AUSTRALIA | NEW ZEALAND | UNITED KINGDOM | SINGAPORE"*
**Ticketek Australia** · **Ticketek New Zealand** · **Ticketek UK** (`premier.ticketek.co.uk`) · **Ticketek Singapore** (`ticketek.com.sg`) · **Ticketek Marketplace** · **Softix** (`softix.com`, the white-label platform) · **TicketWorld** (`ticketworld.com.ph` — **Philippines**) · **TicketCharge** (`ticketcharge.com.my` — **Malaysia**) · **Eventfinda** (AU + NZ) · **Ovation** · **VIP Now**

> **TEG Asia is real and already operating — Ticketek Singapore + TicketCharge (Malaysia) + TicketWorld (Philippines), described by TEG as wholly-owned companies.** This is materially more than "a GM was appointed": there are three live in-territory ticketing businesses in exactly the markets where card-only checkouts fail — **PayNow (SG), FPX/DuitNow (MY), and GCash/Maya (PH), where card penetration is low**. ❌ **No current TEG ticketing operation found in Hong Kong, Japan, Thailand, Indonesia, Korea or mainland China** — Softix licensees in HK/Macau are a licensing relationship, not TEG as merchant of record.
>
> ⚠️ **Eventopia — status contested, and I can partly settle it.** It is absent from TEG's 2026 brand page, which suggests dormancy. But `www.eventopia.co` serves the **byte-identical Ticketek Akamai block page**, so the domain is still live on TEG's own infrastructure. **Live domain, retired brand** is the reading that fits both facts.

### Known PSPs
**None identified. This is the single biggest gap in the file and I am not going to paper over it.**
- ✅ **"Softix PayGate"** — `https://pay.ticketek.com.au/` and `https://pay.ticketek.co.nz/`, both HTTP 200, both titled **"Softix PayGate"**, **both fetched by me**. Notably these are the **only Ticketek hosts not behind the WAF**. Softix is TEG's own ticketing platform, so PayGate is a **merchant-built payment layer** — but it is a layer, not an acquirer. *Who settles the money is unknown.*
- ⚠️ **Windcave (ex-Payment Express)** — a Softix integration listing exists in Windcave's own partner directory (`paymentexpress.com/softix`), and Windcave is confirmed on NZ competitor **iTICKET**. **This is a hypothesis, not a finding.** The listing is a stub and Softix licenses its platform to third-party operators, so the integration may exist for licensees rather than Ticketek itself. **Do not state it in outreach.**
- ❌ **Searched and not found:** Adyen, Stripe, Checkout.com, Worldpay, Braintree, Cybersource, eWAY, Tyro, Fat Zebra, Pin Payments, ANZ Worldline, NAB, Westpac, CBA.

### Orchestration status
**In-house layer — "Softix PayGate".** Affirmatively evidenced by the payment hosts above, not a failed search. Zero hits against Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY and Yuno — but for a merchant that has **never once appeared in payments trade press**, that null is weak evidence and I am treating it as such.

### Buying signals
- 💥 **New CEO Cameron Hoy from 1 June 2026**, running a cost programme: *"assess our operating model to ensure it is fit for purpose as we head into the next financial year."* ~**42 roles in Australia and 2 in the Philippines, c. 5.5% of the workforce.**
- 📉 **Two flagship contracts lost to direct competitors** — **Venues NSW → Ticketmaster** (SCG, Accor, Allianz, CommBank, Penrith Stadiums) and **Melbourne Park → AXS** (Rod Laver, AAMI Park, John Cain, Margaret Court).
- 👤 **New Managing Director, Ticketing — Amy Mackie, announced 15 June 2026**, owning *"ticketing strategy and operations across Australia, New Zealand, Asia and the UK."* **The exact seat that owns the checkout, filled three months ago.**
- 🌏 **"Ticketek Accelerates Growth in Asia"** — **Melvin Koh appointed GM, Ticketing Asia, based in Singapore, June 2026**, plus Shaun Nik to TEG Sport Asia in March 2026. CEO Hoy: *"our ongoing commitment to Asia, a region we have operated in for many decades."*
- 🇳🇿 **March 2026: a decade-long ticketing commitment with Dunedin Venues Management (NZ)** — long-term NZ volume, on the stack that has no Apple Pay, no Google Pay and no PayPal.
- 📋 **No public payment RFP found.** No payments engineering roles found. **The RFP override does not apply.**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Ticketek` to draft the 12-touch sequence.*

**Two instructions for whoever drafts it:**
1. **Do not open on the on-sale queue collapse.** It is the thing Ticketek is famous for, they have heard it from every vendor, and it is a **capacity/queueing problem, not a payment problem** — TEG has already engineered against it with automated IT provisioning. Raising it makes the email indistinguishable from noise. The false-decline admission is the payment story; use that.
2. **Do not use review sentiment.** Ticketek scores **3.7 / 5 across 3,910 reviews on ProductReview.com.au** — which is *good*, and actively contradicts a "your customers are angry" framing. The mechanism is the evidence, not the mood.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 16 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED — floor of ~250,000 card transactions/month, realistically ~1 million.** Sourced input: TEG's own homepage, live today — *"we bring thousands of live events to fans, **sell 30 million tickets**… **each year**"*. 30m ÷ 12 = **2.5m tickets/month**. **Billing unit matters here and I am counting orders, not tickets** — one card transaction carries several tickets, so tickets overstate transactions. The divisor (tickets per order) is **not sourced**, so this is presented as a **bound, not a point estimate**: even at an implausibly high 10 tickets per order the floor is **250,000 orders/month**, and at a realistic 2–3 it is ~830k–1.25m. **Every plausible divisor lands far above the 100,000 top band**, which is why I am marking this ✅ rather than ⚠️ — the band conclusion does not depend on the unsourced input. ⚠️ **Three caveats, all of which I want on the record.** (i) 30m is **TEG group-wide** across all brands and 15+ countries including the UK — Ticketek AU/NZ is the largest share, not all of it; even at one third the floor still clears the top band. (ii) **The figure has been stuck at "30 million" since at least October 2019** while the countries count moved 13 → 15 → 40. It is marketing furniture, not a reported metric. (iii) It **predates the 2026 loss of Venues NSW and Melbourne Park**, which will cut AU volume. **None of the three moves the band.** |
| Orchestration status | **+1** | ✅ **In-house — "Softix PayGate"**, verified first-hand on two live hosts. See 3B for the honest limits of what that proves. |
| 3+ countries | **+3** | ✅ TEG's own privacy policy names group companies in **NZ, Malaysia, Philippines, Singapore, Hong Kong, EU, UK and US**; homepage claims **40 countries**. Two contracting entities confirmed by name and ABN. |
| Multiple PSPs | **0** | ⬜ **Not scorable — zero PSPs identified, for any market.** Not "they only have one" — *nobody could name even one*. Four independent research paths (search, trade press, checkout, source code) all came back empty. **This is the one row holding the arithmetic down, and it is opacity, not absence.** The only lead anyone surfaced is the 2019 article's phrase *"a third party verification system"*. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Australia is the #1 market and both ANZ rails named in the matrix are absent.** **BPAY** and **PayTo** appear nowhere in Ticketek's enumerated first-party Payment Methods article (updated 2026-01-21), in a help centre that gives Afterpay, Apple Pay, Google Pay and PayPal each a dedicated article. **NZ (#2) is worse**: cards and Afterpay only. |
| Recent expansion | **+2** | ✅ **"Ticketek Accelerates Growth in Asia"** — TEG's own newsroom, June 2026, Singapore-based GM of Ticketing Asia appointed; second Asia leadership hire March 2026; decade-long NZ venue deal March 2026. |
| Payment issues reported | **+2** | ✅ **Awarded on merchant-documented decline behaviour, not on complaint volume — and I want that distinction on the record.** Ticketek's own help centre has documented a false-decline mode continuously from **March 2019 to January 2026**, and a **third-party venue operator (Marriner Group) maintains its own help article titled "Blocked credit card error message on Ticketek"** — venues only write those for problems their box office is repeatedly asked about. ⚠️ **Review sentiment does NOT support this row and must not be used**: ProductReview 3.7/5 across 3,910 reviews is healthy. |
| Funding >$10M | **0** | ❌ Silver Lake-owned since 2019–20. No round in the last 12 months. A ~A$1.1bn dividend recapitalisation is reported for Feb 2024 — >12 months old, and a recap is not funding. |
| High traffic outside home | **0** | ❌ **Not met, and now measured rather than assumed: Australia is 82.6% of combined traffic** `[EST]`, far above the 60% threshold. NZ adds 10.5%, so AU+NZ is 93.1%. A genuine "no". |
| Competitor using orchestration | **0** | ❌ **Affirmative null, and a useful one.** No ticketing or live-events company anywhere was found to have publicly adopted an orchestration layer. The closest are Klook publicly testing routing *inside* Adyen, and Eventbrite running Stripe + Braintree + Adyen without ever calling it a strategy. **Ticketing is an orchestration-naive vertical** — no peer-pressure proof point exists, and no competitor is about to take this off the table. |
| Payment job postings | **0** | ⬜ None found. **No in-house payments function is visible at all** — the nearest adjacent role is a Senior Product Designer for the web and app booking experience. |

**Tier: computed 16 / 29 → 🟢 Medium. Overridden upward to ⭐ High Priority.**

> **The override, stated in full — and I have argued myself out of one of these this week, so here is the reasoning.**
>
> The score is held at 16 by exactly one row: **Multiple PSPs, which scored 0 because nobody can see the stack, not because the stack is simple.** Ticketek WAFs its entire estate and has never issued a payments press release, so the row is measuring *opacity*. Penalising a prospect for being hard to research is a scoring artefact, not a judgement about fit. **One named PSP pair in discovery moves this to 19 and ⭐ on the arithmetic alone.**
>
> Against that sit three things the matrix under-weights: **absolute volume is the largest in this repo** (a floor of 250k orders/month, realistically ~1m); the **buying trigger is unusually live** (new CEO at month four, explicit cost mandate, two marquee contracts lost to Ticketmaster and AXS, a new MD of Ticketing in seat since June); and the **hook is verified first-hand and seven years old in their own words**, which is rarer than a score can express.
>
> **What would invalidate this override:** if discovery shows PayGate is a mature multi-acquirer router that already does failover and BIN-level routing, the in-house build is stronger than it looks and this drops back to 🟢. That is the first question to ask on the call.
>
> **Contrast with the LivU file,** where I declined the same upward move: there, the unknowns were *volume* and *territory* — the two things that decide whether an account is worth working at all. Here volume is sourced and enormous, territory is certain, and the unknown is merely *which vendor*. The account's value does not hinge on the answer.

---

### Source Notes
- ✅ **The Zendesk help-centre APIs were the key that opened this account.** The 403 response headers on `premier.ticketek.com.au` carry `link: <https://static.zdassets.com>; rel="preconnect"` — Ticketek runs Zendesk. `help.ticketek.com.au/api/v2/help_center/en-us/articles.json` (50 articles), `ticketeknz.zendesk.com` (44) and `tixsupport.moshtix.com.au` (100) all returned **full article bodies as open JSON with creation and update timestamps**, while the HTML 403s. **All pulled and parsed by me.** Same technique that cracked Indodax, Viu, Azar, Envato and LivU.
- ✅ **`pay.ticketek.com.au` and `pay.ticketek.co.nz` fetched directly** — the only un-WAF'd hosts in the estate, and the source of the PayGate finding and the Dynatrace payment-page map.
- ✅ **The 2019 help article verified by me** from the Wayback snapshot of 14 March 2019, not taken on an agent's word. The archived page is dated *"March 11, 2019 23:54 Updated"*. Its closing line — *"some events may have all sales online only"* — is the part that makes the finding load-bearing, and it was missing from the agent's summary.
- ✅ **Block-page fingerprinting.** The Akamai page is **byte-identical (6,674 bytes, identical hash after stripping the request ID) across `premier`, `www` and `marketplace` on ticketek.com.au plus `eventopia.co`** — which is how I established those are one shared front door rather than four separate properties. `premier.ticketek.co.nz` returns a different, 376-byte block.
- ⚠️ **Traffic is agent-sourced and not re-verified by me** — `similarweb.com` returned a 202 challenge to my own curl. Free tier caps at five countries per domain, and **the three Asian properties were never measured**, so the table understates the APAC footprint.
- ✅ **Entity registrations independently confirmed** against **ABN Lookup** (Ticketek Pty Ltd, TEG Pty Limited, Amplify Bidco) and the **NZ Companies Office** (Ticketek New Zealand Limited, no. 670708) — not taken from the T&Cs alone.
- ⚠️ **Windcave is a hypothesis only.** See 3A. It is the most plausible candidate on priors and it is not evidence.
- ❌ **TAL row 174 is wrong and I verified the correction myself: Moshtix is NOT TEG-owned.** **Ticketmaster acquired Moshtix in February 2019.** Moshtix is a Live Nation-owned *competitor*, not a sibling. Corroborated across IQ Magazine, Billboard, Pollstar, Music Business Worldwide and Digital Music News. **Any outreach calling Moshtix a TEG brand would be wrong in front of the prospect.**
- ❌ **A search synthesis claimed "Ticketek was acquired by Qantas Airways in September 2023." That is false** — no source supports it, and it is almost certainly a confusion with the genuine Qantas Frequent Flyer *payment* partnership. Recording it because it will resurface on any re-run.
- ❌ **No ACCC action on refunds or payments exists.** The only confirmed ACCC matter is a 2011 s46 misuse-of-market-power case (A$2.5m penalty, Dec 2011) — **unrelated to payments**. Do not imply regulator attention on payments in Australia.
- ⚠️ **"48 NZ Commerce Commission inquiries" is NOT citable** — the underlying article returned a headline with no body. The directional finding (refund *timing* was the largest NZ complaint category) is usable; the number is not.

### Success Case Alternatives
- **Chosen on payment pattern:** high-volume domestic card acquiring with extreme demand spikes, an agent-of-seller collect-and-remit model, a merchant-built payment layer, and a documented false-decline problem. Any case must be verified against a published source before use — this repo has already corrected one case-study misattribution.
- ⚠️ **The Klook/Adyen case study is the only quantified number available in this vertical** (+3% authorisation from local methods, +4.32% from network tokens and streamlined authentication) — but it is **Adyen-authored marketing about an Adyen customer**. Use it as a directional benchmark with attribution, or not at all. Never as a Yuno result.

---

## Executive Summary

Ticketek is Australia and New Zealand's largest ticketing company and the core of TEG, which publishes **30 million tickets sold a year** across 30 brands and 40 countries, under Silver Lake ownership since 2019–20. It sells **as agent for venues and promoters**, so its payment stack handles both collection and remittance, and it also runs its own capped-price resale marketplace where **sellers must hold an Australian bank account and wait up to 30 business days after the event to be paid**. The motion is **In-house**: TEG operates its own payment layer, **Softix PayGate**, on the only two hosts in its estate that are not behind Akamai — but **not one acquirer or PSP could be identified for any market**, which is both the biggest gap in this file and the reason the arithmetic reads 16 instead of 19. The commercial asset is exceptional and verified first-hand: Ticketek has documented, in its own help centre continuously from **March 2019 to January 2026**, that a third-party verification layer declines legitimate customers, that retrying with a different card on the same account returns the same decline, and that **during online-only pre-sales there is no recovery channel at all** — a permanently lost sale on their highest-value inventory. That lands into a company with a new CEO since 1 June 2026 running a 5.5% cost reduction, a brand-new Managing Director of Ticketing, two flagship venue contracts just lost to Ticketmaster and AXS, and an explicit, newly-staffed **acceleration into Asia out of Singapore**.

---

### Section 1: Website Traffic Analysis by Country

**Data source: path 3 — SimilarWeb free tier, obtained by a research agent.** Not supplied by Prateek; no MCP tools in this environment; **`similarweb.com` returned a 202 challenge to my own curl**, so this is the one block of data here I have not personally re-verified. `[ESTIMATE, not confirmed]` throughout.

**Redirect structure, verified:** `ticketek.com.au` **301s** to `www.ticketek.com.au`; `premier.ticketek.com.au` resolves **directly** with no redirect — it is the purchase/checkout hostname and a **subdomain of the root**, not a separate property. SimilarWeb's root view aggregates subdomains, **so `premier.*` figures are a subset and must never be added to the root**. Roots only below.

| Property | Monthly visits | Global rank | Engagement | MoM |
|---|---|---|---|---|
| **ticketek.com.au** | **7.1M** | **#7,003** · **#1 Ecommerce>Tickets AU** | 33.8% bounce · 4.64 pp/visit · 3m41s | −3.9% |
| **ticketek.co.nz** | **638.5K** | #65,616 | 35.1% bounce · 5.07 pp/visit · 4m03s | **+22.1%** |
| *(premier.ticketek.com.au)* | *4.4M — subset, not added* | — | 45.0% bounce | −3.6% |
| *(premier.ticketek.co.nz)* | *418.9K — subset, not added* | — | 63.1% bounce | +14.1% |

**Combined roots ≈ 7.74M visits/month.**

| # | Country | Est. monthly visits | Share | Entity? |
|---|---|---|---|---|
| 1 | **Australia** | 6,389,666 | **82.6%** | ✅ Ticketek Pty Ltd |
| 2 | **New Zealand** | 814,565 | **10.5%** | ✅ Ticketek New Zealand Ltd |
| 3 | United States | 267,070 | 3.5% | ❌ none |
| — | *Other (not broken out)* | 185,758 | 2.4% | — |
| 4 | India | 41,890 | 0.5% | ❌ none |
| 5 | United Kingdom | 31,825 | 0.4% | Ticketek UK operates; no entity found |

**Reading it honestly:** AU + NZ is **93.1%** of measured traffic. US at 3.5% and India at 0.5% are diaspora and bot/VPN noise, not markets — **do not build a cross-border story out of this table.** The NZ trend is the interesting line: **+22.1% MoM growth on the checkout that has no wallets and no PayPal.**

**What is NOT measured, and it matters:** `ticketek.com.sg`, `ticketworld.com.ph` and `ticketcharge.com.my` were never pulled. Those are live, in-territory TEG businesses and they are invisible in this table — so this data understates the APAC footprint and cannot be used to size the Asia opportunity either way.

Domains identified: `premier.ticketek.com.au` (AU sales), `premier.ticketek.co.nz` (NZ sales), `marketplace.ticketek.com.au` (resale), `help.ticketek.com.au` + `ticketeknz.zendesk.com` (support), `pay.ticketek.com.au` + `pay.ticketek.co.nz` (payment), `www.eventopia.co` (TEG brand, same front door), `www.ticketek.com.sg` (exists, returns a *different* 377-byte block — **not on the same infrastructure**; status not established).

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Sydney, Australia. Ticketek traces to 1979 (created by Kerry Packer's PBL to sell World Series Cricket tickets); TEG formed as an independent group in 2015; **first Australian company to sell tickets online, 1997** — all per TEG's own timeline.

| Country | Entity | Identifier | Source |
|---|---|---|---|
| Australia | **Ticketek Pty Ltd** | **ABN 92 010 129 110** | Ticketek Terms and Conditions of Sale, opening line |
| Australia | TEG Pty Limited · TEG Rewards Pty Ltd · Eventopia Pty Ltd | — | TEG privacy policy |
| New Zealand | **Ticketek New Zealand Ltd** | — | TEG privacy policy |
| Malaysia, Philippines, Singapore, Hong Kong, EU, UK, US | Group companies, unnamed | — | TEG privacy policy, verbatim list |

**Cross-border gap analysis.** Ticketek's own T&Cs establish the model: *"Ticketek Pty Ltd… provides ticketing services, including the sale and distribution of tickets, **as agent for the venue, promoter or person responsible for holding the relevant event (the "Seller")**."* So Ticketek is the **collecting agent**: money in from fans, money out to promoters. That is a two-sided flow with settlement obligations, not a simple merchant.

**The Asia expansion is the cross-border question that matters.** TEG has a Singapore-based GM of Ticketing Asia as of June 2026 and confirmed group companies in Singapore, Malaysia, Hong Kong and the Philippines. Per `.claude/reference/apac-payments.md`, each of those markets has a dominant local rail a card-only stack cannot reach — **PayNow (SG), FPX/DuitNow (MY), FPS (HK), GCash/Maya (PH)** — and the Philippines in particular has low card penetration. **I could not establish anything about TEG's payment stack in any Asian market**, so this is an open question to ask, not a claim to make.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Region | Provider | Evidence type | Source |
|---|---|---|---|
| AU | **Softix PayGate** | `[Source Code]` — HTTP 200, `<title>Softix PayGate</title>`, **fetched by me** | `https://pay.ticketek.com.au/` |
| NZ | **Softix PayGate** | `[Source Code]` — HTTP 200, same title, **fetched by me** | `https://pay.ticketek.co.nz/` |
| MY | Softix PayGate | Search-indexed title only | `pay.ticketcharge.com.my` — `[UNVERIFIED — not fetched; host unreachable from here]` |
| AU | **Forter / fraud vendor — NOT identified** | The 2019 article's phrase *"third party verification system"* is the only hint | — |
| AU/NZ | **Windcave** | A Softix listing exists in Windcave's partner directory; the listing is a **stub** with empty description and integration fields | `paymentexpress.com/softix` — **hypothesis only** |
| AU | **Refund Protect / Refundable.me** — "Refundable Tickets" upsell | Third-party add-on at checkout, provider **not confirmed** | `[UNVERIFIED — search summary only]` |
| AU | **Qantas Frequent Flyer** — Points Plus Pay | Redirect handoff to Qantas's own redemption rails, then return to Ticketek | Ticketek Qantas FAQ, pulled by me |

**No acquirer, no gateway, no processor is publicly identifiable for any Ticketek market.** Four independent paths were tried — web search, payments trade press, live checkout, and archived source code — and all came back empty. TEG appears in **no** payments trade publication (thepaypers, finextra, pymnts), which is itself consistent with a long-lived in-house/legacy stack that has never been news.

#### 3B. Payment Orchestrator → **IN-HOUSE ("Softix PayGate")**

`pay.ticketek.com.au` and `pay.ticketek.co.nz` both serve a page titled **"Softix PayGate"**. Softix is TEG's own ticketing platform — so this is a payment layer the merchant built, on domains the merchant owns, in at least two markets.

> **What that proves, and what it does not.** It proves a **merchant-operated payment layer exists** and is the checkout handoff point. It does **not** prove multi-acquirer routing, failover, or BIN-level logic — the things that would make it genuine orchestration rather than an in-house hosted payment page in front of a single acquirer. **I cannot tell which from outside, and the difference is commercially enormous.** If it is a router, this is a hard build-vs-buy sell. If it is a single-PSP wrapper, the account is much closer to greenfield and the score rises. **This is question one on the call.**

A telling architectural detail: **the `pay.` hosts are the only Ticketek properties not behind Akamai.** Everything else — sales site, marketplace, Eventopia — sits behind the WAF. The payment surface is deliberately carved out of the bot-protection perimeter.

#### 3C. The payment page, reconstructed from their own monitoring config ⭐ *found first-hand; not in any agent report*

`pay.ticketek.com.au` carries a **Dynatrace RUM agent** (`ruxitagentjs`) whose `data-dtconfig` enumerates the live payment page's own element classes, because Dynatrace is configured to mask them in session replay. Decoded, the payment page contains:

| Element class | What it is |
|---|---|
| `captureCreditCardNumber`, `TrCardName`, `TrCvc` | **Card number, name and CVC captured in Ticketek's own form fields, on Ticketek's own domain** |
| `paymentOption afterpayPaymentOption` | Afterpay |
| `googlePayButton` | Google Pay |
| **`paymentOption visaCheckoutPaymentOption`** | **Visa Checkout** |
| `giftVoucherIcon` | Gift voucher redemption |
| `btn btn-primary qantas-button use-points` | Qantas Points |
| `payment-row payment-row-radio` | The method selector |

**Three findings fall out of this, in order of importance:**

1. 💳 **They are in full PCI DSS scope.** `captureCreditCardNumber` is an element **on their own payment host** — raw PAN is entered into Ticketek's own form, not a PSP-hosted iframe or hosted field. Combined with a card vault (3D), that is SAQ D territory, not SAQ A. **PCI scope reduction is a real, quantifiable pitch here** — and it is Yuno's most concrete non-conversion argument.
2. 🕰️ **`visaCheckoutPaymentOption` is a dead payment method.** Visa retired Visa Checkout — US merchants were transitioned to Click to Pay / Secure Remote Commerce on 21 January **2020**, with other countries following "over the course of 2020." **The Dynatrace config carrying this selector was last modified 2026-09-16 — yesterday.** Either the Visa Checkout option still renders in the live checkout six years after Visa killed it, or the payment-page monitoring config has not been cleaned in six years. **Both readings say the same thing about how much attention this layer gets.** *(Stated as the two readings, because I could not load the live checkout to see which.)*
3. 📉 **Apple Pay and PayPal are absent from the selector list** — despite launching in July 2024 and June 2025. That is suggestive of a stale config, but **not conclusive**: redirect-based methods may not need session-replay masking. Noting it, not claiming it.

The same config also reveals the platform and the stack around it: `window.SOFTIX.order[…]`, `window.SOFTIX.GAData.Basket.TotalCosts.TotalCost` (the **Softix** object model is the live front end); `ctl00_ctl00_uiBodyMain_uiBodyMain_uiLogin_tbLoginCode` (**ASP.NET WebForms**); `/bundles/jquery`, `/bundles/bootstrap`, `/bundles/modernizr` (**ASP.NET MVC bundling, jQuery, Bootstrap, Modernizr** — a legacy .NET web stack); **Optimizely** A/B testing; **Zopim/Zendesk Chat**; and excluded beacons for **Adobe Audience Manager (demdex), Google Analytics, FullStory and Microsoft Clarity**.

> 👀 **And one detail worth more than all of it: `mdcc14=a.errorMessage.alert-warning`.** They capture the **text of the payment error message** as a Dynatrace custom metric. **Somebody inside Ticketek is already instrumenting declines.** That person is the buyer, and they already have the data to prove the problem to themselves.

#### 3D. Card vault — saved cards that still demand a CVC

Ticketek stores cards in the MyTicketek account, in both markets. From NZ's own article: *"The credit card pre-fill feature allows you to save time and securely save the details of a credit or debit card to your MyTicketek account… **all you need to enter is the CVC security code**"*, and *"only the first 6 digits and last 4 digits of the relevant card number will appear as clear text."*

**A saved card that requires CVC re-entry on every purchase is not a tokenized one-click flow** — it is stored card data being re-presented. In a business whose entire model is speed in the first ninety seconds of an on-sale, that is friction at precisely the worst moment. It also means no network tokens, no account updater, and no stored-credential framework — all standard orchestration-layer capabilities. Also noted: *"the Payment Details page is **not accessible from the Ticketek App**."*

#### 3E. PCI DSS
**No PCI DSS statement, level or Attestation of Compliance found for Ticketek or TEG.** Nothing published. But see 3C.1 — the element evidence points to **full scope (card data entered on their own page)**, which makes the *absence* of any published PCI posture more notable, not less.

---

### Section 4: Alternative & Local Payment Methods

**Australia** — from the first-party enumerated **Payment Methods** article (updated 2026-01-21), plus dedicated per-method articles:

| Method | Category | Status | Note |
|---|---|---|---|
| Visa, Mastercard, Amex | Cards | ✅ Active | CVC required; 3DS with **6-digit SMS OTP** |
| **Afterpay** | BNPL | ✅ Active | Min A$50, **max A$3,000**; online channels only |
| **Google Pay** | Wallet | ✅ Active | Article created **Dec 2018** |
| **Apple Pay** | Wallet | ✅ Active | Created **Jul 2024** — *"launched for Australian sites"* |
| **PayPal** + **Pay in 4** | Wallet + BNPL | ✅ Active | Created **Jun 2025** — *"**PayPal is Ticketek's newest way to pay online**"* |
| **Ticketek Gift Voucher / Gift Card** | Voucher | ✅ Active | Sold via Coles, Woolworths, Australia Post, Officeworks; 3-year expiry |
| **Qantas Points** (Points Plus Pay) | Loyalty, **split-tender** | ✅ Active | Min 2,000 points; *"a mix of Qantas Points and cash"* |
| **BPAY** | Bank transfer / A2A | ❌ **Sourced absent** | Not in the enumerated list |
| **PayTo** | Direct debit / mandate | ❌ **Sourced absent** | Not in the enumerated list |
| Zip, humm, Latitude, Klarna | BNPL | ❌ Sourced absent | **Afterpay only.** Zip is offered by competitor Oztix |
| POLi | A2A | ❌ Sourced absent | — |

**New Zealand** — from the NZ help centre: **credit/debit cards and Afterpay (min NZ$50, max NZ$2,000). That is the entire list.**

> ⚠️ **Warning — Australia.** **BPAY** and **PayTo** are both absent from Ticketek's #1 market. PayTo is the NPP-based mandate rail and BPAY is a long-established Australian bill/A2A rail; neither appears anywhere in a help centre detailed enough to give four other methods their own article. *Sourced absence from an enumerated first-party list, with the "including" hedge noted.*
>
> ⚠️ **Warning — New Zealand.** Ticketek NZ has **no wallet payment option and no PayPal** — while the same company, same brand, same platform shipped Apple Pay to Australia in 2024 and PayPal in 2025. Their own AU article says Apple Pay *"was launched for **Australian** sites."* **Caveat honestly: the NZ help centre is visibly stale** (its wallet article still references "the new iPhone 5" and iOS 6; nothing updated past 2024), so this is a strong signal one verification step short of proof — **confirm on a live NZ checkout before it goes in an email.**

**One integration per year, each one a project.** Google Pay 2018 → Afterpay 2020 → Apple Pay 2024 → PayPal 2025. And they say it themselves: *"PayPal is Ticketek's newest way to pay online."* That cadence **is** the one-integration-every-method argument, in their own release history.

**Ticketek Marketplace runs a lagging stack.** Their own articles state PayPal *"is not currently available on Ticketek Marketplace"* and Apple Pay is *"not currently available on Ticketek Marketplace."* **Their own resale platform cannot take the two methods they spent 2024 and 2025 launching.**

---

### Section 5: Payment Issues & Customer Complaints

**The (a)/(b) split matters and I am keeping it rigid.**

**(a) Queueing / capacity / bot failures — NOT payment problems.** These dominate Ticketek's public reputation and must be kept out of outreach. TEG treats this as a capacity problem and has engineered against it with automated IT provisioning.

**(b) Actual payment failures:**

| Issue | Frequency | Date range | Evidence |
|---|---|---|---|
| **False declines from a third-party verification layer, with no online recovery path** | **Systemic — self-documented** | **Mar 2019 → Jan 2026** | ✅ **VERIFIED by me** — both the 2019 Wayback capture and the current article body via the Zendesk API |
| **3DS completed successfully → card error still returned** | Merchant documents it as a known state | Current (updated 2026-01-22) | ✅ **VERIFIED by me** via the Zendesk API |
| Venue partner maintaining its own article on Ticketek card blocks | Recurring enough to warrant documentation | Current | Marriner Group Zendesk — title/URL confirmed, body `[UNVERIFIED]` |
| Marketplace seller payout held 30 business days post-event | Isolated (1 review) | ~Aug 2026 | ProductReview |
| Double charges / charged-with-no-ticket | Moderate | Ongoing | `[UNVERIFIED — search summary only]` |
| Refund *timing* — largest NZ Commerce Commission complaint category | Moderate–high | 2022–23 baseline | `[UNVERIFIED]` — **the "48 inquiries" figure is NOT citable** |

> **Pattern → opportunity.** An account-level decline that persists across different cards is not issuer behaviour — it is **velocity or account-level rules in a screening tier**, firing hardest exactly when a customer retries during an on-sale. That is the textbook false-decline profile, and it is the thing routing, retry logic and a properly tuned fraud layer exist to fix. Their own 2019 text describes the mechanism precisely.

**Do not use:** ProductReview sentiment (3.7/5 from 3,910 — healthy), any ACCC claim (none exists on payments), or the 48-inquiry NZ figure.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | **Jul 2026** | Restructure and cost-cutting; **~42 AU + 2 PH roles, c.5.5% of workforce**. Hoy: *"Since stepping into the CEO role, I have been working closely with the senior management team to develop our **FY27 strategy** and assess our operating model to ensure it is **fit for purpose**"* | Restructure | ticketnews.com — ✅ fetched |
| 1b | **Jun 2026** | **Cameron Hoy became CEO on 1 June 2026**, reportedly succeeding **Brad Banducci**, with long-time CEO **Geoff Jones moving to Chairman**. ⚠️ Hoy is confirmed CEO on TEG's own site; the succession detail is `[UNVERIFIED — trade press only]` | Leadership | ticketnews.com |
| 2 | **Jun 2026** | **Amy Mackie appointed Managing Director, Ticketing** — *"ticketing strategy and operations across Australia, New Zealand, Asia and the UK"* | Leadership | teg.com.au — ✅ fetched |
| 3 | **Jun 2026** | **Melvin Koh appointed GM, Ticketing Asia, Singapore-based** — *"as TEG accelerates its presence in Asia"* | Market expansion | teg.com.au — ✅ fetched |
| 4 | **2026** | **Venues NSW contract lost to Ticketmaster**; **Melbourne Park lost to AXS** | Competitive loss | ticketnews.com — ✅ fetched |
| 5 | **Mar 2026** | Decade-long commitment with Dunedin Venues Management (NZ); Shaun Nik to TEG Sport Asia | Expansion | teg.com.au |
| 5b | **Jun 2025** | **Record 370,000-ticket day.** Note Cameron Hoy is quoted in this release a year *before* becoming group CEO — **the current CEO came up through Ticketek and knows the ticketing platform personally.** Useful for pitching altitude | Volume record | teg.com.au — ✅ fetched |
| 6 | 2019–20 | **Silver Lake acquired TEG from Affinity Equity Partners** (announced 4 Oct 2019, ~A$1bn+) | Ownership | Multiple outlets — ⚠️ **six years old, not recent** |

**No public payment RFP found. No payments engineering roles found. No in-house payments function visible.**

Also relevant: TEG has replatformed its core system of record onto **MongoDB on AWS**, signed a **Google Cloud** partnership for AI/data, and reportedly appointed **three CTOs in three years**. `[UNVERIFIED — search summaries]` **Read: a company demonstrably willing to rip out and replace core infrastructure — but every modernisation story is about data, AI and infrastructure. Payments is the un-modernised layer.** The CTO churn also means: multi-thread, and expect a long, discontinuous cycle.

---

### Section 7: Payment-Specific News

**Effectively none — and the absence is the finding.** TEG and Ticketek appear in **no** payments trade press (thepaypers, finextra, pymnts). The only payment-adjacent product item found is a **Ticketek App Clip** allowing purchase via Apple Pay without installing the app `[UNVERIFIED — search summary]`, which at least confirms someone internally owns checkout conversion.

**No provider removals detected.**

---

### Section 8: Checkout Experience Audit

**The live flow could not be walked — every sales surface is behind Akamai Bot Manager.** I did not attempt to defeat the bot protection. What follows is reconstructed from first-party help articles and the payment host's own monitoring config.

| Dimension | Finding | Quality |
|---|---|---|
| Checkout type | Custom-built **ASP.NET WebForms/MVC**, jQuery/Bootstrap/Modernizr, handing off to **`pay.ticketek.com.au` (Softix PayGate)** | Fair |
| **Guest checkout** | ❌ **No — account required.** NZ: *"You will need to be signed in to make a purchase tickets online."* **Competitor Moshtix offers guest checkout.** | **Poor** |
| Card input | **Own form fields on own domain** (`captureCreditCardNumber`) — not a PSP iframe | **Poor** (full PCI scope) |
| Methods visible | AU: cards, Afterpay, GPay, ApplePay, PayPal, gift voucher, Qantas Points. NZ: cards + Afterpay | Good (AU) / **Poor (NZ)** |
| **Split tender** | ✅ Qantas Points + cash; gift voucher + balance | Good — and genuinely complex |
| Instalments | Afterpay (A$50–3,000) + PayPal Pay in 4 (AU only) | Good (AU) |
| **3DS** | ✅ In production — **6-digit SMS OTP**, described as a step the customer completes on-site. Reads as challenge-driven rather than frictionless 3DS2 — **but the version is NOT established, do not assert "3DS1"** | **Poor** — and declines persist *after* successful completion |
| Saved payment methods | Vault exists; **CVC required every time**; not manageable in the app | **Poor** |
| Mobile | App exists for AU and NZ; payment details page unavailable in-app | Fair |
| Multi-currency | AUD and NZD per market entity; no evidence of local pricing elsewhere | Not established |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding |
|---|---|
| PCI DSS Level | **No public information found** |
| Card data handling | **Card fields on the merchant's own payment host** (`captureCreditCardNumber`, `TrCardName`, `TrCvc` on `pay.ticketek.com.au`), plus a stored-card vault → **points to full PCI scope (SAQ D-class), not SAQ A** |
| Recommended Yuno integration | **SDK / hosted fields** — the scope-reduction argument is unusually concrete here |

`[INFERENCE, not confirmed]` on the scope conclusion — it follows from the element evidence in 3C, not from any published attestation.

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: A seven-year-old false-decline problem with no recovery path on premium inventory**
> **Evidence:** §5 (2019 + 2026 help articles, both verified first-hand) + §3C (`mdcc14=a.errorMessage.alert-warning` — they already instrument payment error text) + §8 (3DS completed → still declined)
> **Pain:** Legitimate, authenticated buyers are declined; retrying with another card on the same account repeats the decline; during online-only pre-sales the sale is simply **lost**, not deferred.
> **Yuno:** Routing and retry across multiple acquirers turns a hard decline into a second attempt on a different rail; a properly tuned screening tier stops account-level velocity rules from eating good customers.
> **Angle:** Quote them to themselves — 2019 and 2026 side by side.
> **Subject:** `Your 2019 card-block article, still live`

> **Insight #2: One new payment method per year, and the resale platform can't take any of them**
> **Evidence:** §4 (Google Pay 2018 → Afterpay 2020 → Apple Pay 2024 → PayPal 2025; *"PayPal is Ticketek's newest way to pay online"*) + §4 (PayPal and Apple Pay both *"not currently available on Ticketek Marketplace"*)
> **Pain:** Every method is a bespoke build against an in-house layer, and the build doesn't propagate — their own secondary marketplace runs two years behind the primary site.
> **Yuno:** One integration; a method added once is available on every surface.
> **Angle:** The asymmetry is inside their own estate. Neither half is arguable.
> **Subject:** `Apple Pay on ticketek.com.au, not on Marketplace`

> **Insight #3: Australia is instrumented, New Zealand is not — in two independent ways**
> **Evidence:** §4 (AU: 7 methods; NZ: cards + Afterpay) + §1 (`pay.ticketek.com.au` carries Dynatrace; `pay.ticketek.co.nz` carries nothing) + §6 (a **decade-long** NZ venue commitment signed March 2026)
> **Pain:** NZ conversion is neither optimised nor measured, on a market they just committed to for ten years.
> **Yuno:** Method parity across markets from one integration, with routing visibility in both.
> **Angle:** *"Apple Pay was launched for Australian sites"* — their words.
> **Subject:** `NZ checkout vs AU checkout`

> **Insight #4: Asia expansion into the hardest rail markets, with no visible payments function**
> **Evidence:** §6 (GM Ticketing Asia, Singapore, June 2026; group companies in SG/MY/HK/PH) + §6 (no payments hires, no payments function) + §6 (5.5% headcount cut)
> **Pain:** PayNow, FPX/DuitNow, FPS and GCash are each a separate integration on an in-house layer, commissioned by a team that is shrinking.
> **Yuno:** Market entry becomes configuration, not a per-country build.
> **Angle:** Save for touch 2 — it is a hypothesis about their roadmap, not an observation about their checkout.
> **Subject:** `Ticketek Asia — PayNow and GCash`

> **Insight #5: Full PCI scope, plus a Visa Checkout button Visa retired in 2020**
> **Evidence:** §3C (`captureCreditCardNumber` on their own host; `visaCheckoutPaymentOption` in a config modified 2026-09-16) + §9 (no published PCI posture)
> **Pain:** Card data on their own page is the expensive kind of compliance, and dead method code is unowned code.
> **Yuno:** Hosted fields collapse the scope.
> ⚠️ **Handle with care.** Lead with this only if the conversation is technical. Told bluntly it reads as "we scraped your monitoring config", which is a bad first impression even though the config is publicly served.
> **Subject:** `PCI scope on your payment page`

> **Insight #6: A 4.5× peak-day spike, on a single unknown acquirer**
> **Evidence:** §12 (**370,000+ tickets in one day**, 30 June 2025, 320,000+ from AC/DC alone — TEG's own release) + §3A (not one acquirer identified; no evidence of a second) + §5 (their own 2019 text: retrying after a decline returns the same decline)
> **Pain:** On-sale days concentrate a year's worth of risk into hours. If one acquirer degrades during an AC/DC or Ashes on-sale, there is no visible second rail — and their own documentation says a customer who retries gets blocked harder, so the failure compounds rather than recovers.
> **Yuno:** Automatic failover across acquirers, and retry logic that routes the second attempt somewhere else instead of into the same decline.
> **Angle:** Use their own record as the compliment, then ask the question. They are proud of this number and rightly so.
> **Subject:** `370,000 tickets in a day — on how many acquirers?`

### Quick Hits

**Email hooks:**
1. *"Your help centre has told customers since 2019 that a third-party verification layer may decline them, and that retrying with a different card on the same account returns the same decline. The article was rewritten in January. The admission is still in it."*
2. *"You launched Apple Pay in 2024 and PayPal in 2025 — and neither is available on Ticketek Marketplace, which you also own."*
3. *"Ticketek NZ takes cards and Afterpay. Ticketek AU takes seven methods. Same company, same platform."*

**Cold call openers:**
1. *"When a card gets declined during an online-only pre-sale — where the call centre can't transact yet — what happens to that sale?"*
2. *"Does PayGate route across more than one acquirer, or is it one processor behind it?"*
3. *"You've got a GM of Ticketing Asia in Singapore now. Is PayNow on the roadmap, or is that a per-market build?"*

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct competitors
| Company | Website | HQ | Position | Known stack |
|---|---|---|---|---|
| **Ticketmaster ANZ** (Live Nation) | ticketmaster.com.au | US / AU ops | The other half of the AU duopoly; **just won Venues NSW off Ticketek** | **PayPal Braintree is "Ticketmaster's primary global payment processor"** (announced 3 Apr 2023, 21 countries — **AU not individually named**) |
| **AXS** (AEG) | axs.com | US | **Just won Melbourne Park off Ticketek** | Not established |
| **Moshtix** | moshtix.com.au | Sydney | ⚠️ **Ticketmaster-owned since Feb 2019 — a competitor, NOT a TEG sibling** | Cards, Apple Pay, Google Pay, **PayPal + Pay in 4**, Afterpay; **dropped Zip**; **guest checkout**; partial gift-voucher redemption |
| **Oztix** | oztix.com.au | Brisbane | Australia's largest independent | Zip offered; gateway not established |
| **Eventbrite** | eventbrite.com | San Francisco | Global self-serve | **Stripe + Braintree + Adyen** (per their own PCI AoC) |
| **Humanitix / TryBooking** | — | Sydney / Melbourne | Community & mid-market | Not established |
| **iTICKET** | iticket.co.nz | Auckland | NZ independent | **Windcave** (vendor case-study page exists) |
| **Flicket** | flicket.co.nz | NZ | NZ events commerce | **Stripe** |

> 📌 **Moshtix is the sharpest competitive comparison available**, and it belongs to Ticketmaster. Its help centre (100 articles, pulled by me) shows **guest checkout, PayPal Pay in 4, partial gift-voucher redemption and a documented path for cards issued outside AU/NZ** — all things Ticketek either lacks or hasn't shipped to every surface. **Never name it in outreach as a comparison; use it to know where they're behind.**

#### 11B. APAC peers
**SISTIC** (Singapore — licenses its platform into SG/MY/ID/HK/Macau, the closest APAC analogue to Ticketek's model; **ownership unresolved**, do not state it), **Klook** (HK — Adyen, sole PSP, publicly testing routing), **Trip.com** attractions, **CTS Eventim / See Tickets**, **DICE**, **Secutix**.

#### 11C. Orchestration adoption in this vertical
**None found, anywhere.** No ticketing or live-events company has publicly adopted an orchestration layer. Closest analogues: Klook testing routing *inside* Adyen, and Eventbrite running three acquirers without ever framing it as strategy.

> **This cuts both ways and both ways are useful.** There is no "your peers are doing this" proof point to lean on — the case has to be built from first principles. But there is also **no competitive displacement risk**: nobody is about to take this off the table, and TEG has not already been sold this story by somebody else.

#### 11D. Top prospect pipeline
| Rank | Company | Type | Markets | Top signal | In TAL? |
|---|---|---|---|---|---|
| 1 | **TEG** (group) | Parent | AU/NZ/Asia/UK | Same account, group-level | ✅ **row 179** |
| 2 | **Ticketmaster Asia** | Competitor | SG + | Braintree single-processor concentration | ✅ row 185 |
| 3 | **SISTIC** | APAC peer | SG/MY/ID/HK/Macau | Platform licensor, multi-market | ❌ **not on the list — genuine find** |
| 4 | **Oztix** | Competitor | AU | Largest AU independent, stack unknown | ❌ **not on the list — genuine find** |
| 5 | **AXS / AEG APAC** | Competitor | AU + | Just won Melbourne Park | ❌ not on the list |
| 6 | **iTICKET / Flicket** | NZ competitors | NZ | Windcave / Stripe | ❌ not on the list |

⚠️ **Do not work TEG (row 179) and Ticketek (row 183) as separate accounts** — Ticketek is TEG's ticketing division and the payment decision sits with the new MD of Ticketing. Two sequences into one company would be visible to them.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|---|---|---|
| Annual revenue | **A$925,408,000 (2025)** — **Amplify Bidco Pty Ltd t/a TEG**, the ASIC-filing head entity | IBISWorld company record `[ESTIMATE/third-party, not a filing I read]`. ⚠️ Same record lists 587 employees, implausibly low for a A$925m group — treat headcount as unreliable, revenue as the better figure |
| **Tickets sold per year** | **30 million** | ✅ TEG homepage, live 2026-09-17, **fetched by me** |
| Average ticket price | Not found | — |
| **Monthly transaction count** | ✅ **DERIVED — floor ~250,000 orders/month; realistically ~830,000–1,250,000** | 30m tickets ÷ 12 = 2.5m tickets/month, ÷ tickets-per-order. **Billing unit: card transactions (orders), not tickets.** Presented as a bound because the divisor is unsourced; every plausible divisor clears the ≥100,000 band. **Group-wide figure** |
| ⭐ **Peak single-day volume** | **370,000+ tickets in one day** (30 June 2025) — all-time platform record. **320,000+ from the AC/DC 2025 on-sale alone** across multiple cities, plus ~50,000 across NRL, AFL, theatre and Lightscape. Beat the record set days earlier by **The Ashes** on-sale | ✅ **TEG press release, fetched and verified by me** |
| **Peak-to-average ratio** | **~4.5×** — 370k peak day vs a smoothed 30m ÷ 365 ≈ 82k/day | Calculated from the two figures above |
| Venue/promoter clients | 135+ venue and promoter clients (2019 figure) | ⚠️ dated |
| Scale | *"more than 30 brands in 40 countries on six continents"*; 2m fans to own venues/yr | ✅ TEG homepage |
| Primary currency | AUD (Ticketek Pty Ltd), NZD (Ticketek New Zealand Ltd) | ✅ entity structure |
| Top 3 markets by revenue | **Not established** — no traffic or revenue split available | — |
| Billing channel split | **100% web/app/agency — no app-store dependency.** Tickets are not IAP. **The app-store trap does not apply** | ✅ |
| Payout obligations | Agent-of-seller remittance to promoters; **Marketplace sellers paid within 30 business days after the event, AU bank account required** | ✅ first-party |

---

### Overall Research Confidence

**High on payment methods, the payment surface and corporate timing. Zero on the PSP stack. None on traffic.**

- ✅ **High** — accepted methods per market, the false-decline history, entity structure, corporate developments, the payment-host architecture and PCI-scope evidence. All from first-party sources I fetched myself today: three open Zendesk APIs, the two `pay.` hosts, TEG's own site and newsroom, and a Wayback capture.
- 🔴 **Zero** — **no PSP, acquirer or gateway identified for any market.** Four paths, nothing.
- 🟡 **Medium** — traffic. Obtained via SimilarWeb free tier by an agent; **I could not re-fetch it (202 challenge)**, the free tier caps at five countries per domain, and the three Asian properties were never measured.
- 🟡 **Medium** — complaints: the mechanism is verified, the volume is not.

**Confidence downgraded one level overall** for the WAF: Section 8 could not be completed by walking the live checkout, exactly as the skill's fallback contemplates.

### Manual Research Recommendations

> **1. Name the PSP.** *Why:* it is the only row keeping this at 16 and it decides whether the motion is in-house or effectively greenfield. *Action:* **walk a real checkout to the payment step in a browser.** The 3DS challenge origin and the payment POST target will name the gateway in about five minutes. Nothing else in this file is worth as much.

> **2. Establish whether PayGate routes.** *Why:* a multi-acquirer router with failover is a hard build-vs-buy sell; a single-PSP hosted-page wrapper is nearly greenfield. *Action:* question one on the call — *"does PayGate sit in front of more than one acquirer?"*

> **3. Confirm the NZ method list on a live NZ checkout.** *Why:* Insight #3 rests on it and the NZ help centre is visibly stale. *Action:* NZ VPN, load a checkout, screenshot.

> **4. Confirm whether the Visa Checkout option still renders.** *Why:* dead-method code in a live checkout is a much stronger statement than a stale monitoring config. *Action:* same checkout walkthrough as #1.

> **5. Find two citable customer posts of "3DS completed → still declined."** *Why:* it turns a merchant-documented issue into a demonstrable one. *Action:* mine ProductReview's paginated review pages — indexed and fetchable.

> **6. Check whether Ticketmaster Asia or TEG is already owned elsewhere** before sequencing. *Action:* cross-check TAL rows 179, 183 and 185 with the team.

### TAL corrections — `accounts/apac-tal.csv`
| Row | Column | Current | Should be |
|---|---|---|---|
| **174 Moshtix** | `INFO` | *"**owned by TEG**"* | ❌ **WRONG — Moshtix has been owned by Ticketmaster (Live Nation) since February 2019.** It is a competitor, not a TEG brand. Verified across five outlets. |
| **183 Ticketek** | `Payment Gateway` | *(empty)* | **"Softix PayGate" (TEG's own layer) — underlying acquirer unknown** |
| 183 Ticketek | `Payment Orchestrator` | *(empty)* | **In-house (Softix PayGate)** |
| 183 Ticketek | `Operating Countries` | "AU/NZ (TEG)" | AU, NZ **+ group companies in Malaysia, Philippines, Singapore, Hong Kong, EU, UK, US**; Ticketek Asia GM appointed Singapore June 2026 |
| 183 / 179 | — | Listed as two rows | ⚠️ **Same company.** Ticketek is TEG's ticketing division — do not sequence both |
| 179 TEG | `Est. Revenue (USD)` | "~$1B est. (private)" | Unverified. **What is sourced is 30m tickets/year** (TEG homepage) |

---

### Appendix: Key Source URLs

**First-party, fetched by me:** `pay.ticketek.com.au` · `pay.ticketek.co.nz` · `help.ticketek.com.au/api/v2/help_center/en-us/articles.json` (50 articles) · `ticketeknz.zendesk.com/api/v2/help_center/en-us/articles.json` (44) · `tixsupport.moshtix.com.au/api/v2/help_center/en-au/articles.json` (100) · `teg.com.au` · `teg.com.au/privacy-policy/` · `teg.com.au/the-teg-story/` · `teg.com.au/ticketek-entertainment-group-appoints-melvin-koh-as-ticketek-accelerates-growth-in-asia/` · `teg.com.au/ticketek-entertainment-group-teg-announces-amy-mackie-as-managing-director-ticketing/`

**Key help articles:** Payment Methods `…/4408558478105` · 3D Secure `…/360001885348` · PayPal `…/48264188990617` · Apple Pay `…/35064620455193` · Afterpay `…/360050752994` · Qantas `…/35998333029017` · T&Cs of Sale `…/26000971458969` · Marketplace `…/360012407014` · NZ Credit Card `…/4408376221977`

**Archived:** `web.archive.org/web/20190314194304/https://help.ticketek.com.au/hc/en-us/articles/360001885348-The-website-says-my-card-has-been-blocked`

**Third-party:** ticketnews.com (restructure, July 2026) · americanbanker.com (Visa Checkout sunset) · business.ticketmaster.com (Braintree) · adyen.com (Klook) · iqmagazine.com, billboard.com, pollstar.com, musicbusinessworldwide.com, digitalmusicnews.com (Moshtix/Ticketmaster) · productreview.com.au

</details>
