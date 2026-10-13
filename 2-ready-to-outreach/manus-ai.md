# Manus AI

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 23 / 29 → ⭐ **High Priority**
**Industry:** AI agents — consumer/prosumer subscription + credits (Free / Pro / Team) · **HQ:** Singapore · **Billing entity:** Butterfly Effect Pte. Ltd. (Singapore) · **Researched:** 2026-10-13 · **First email sent:** —
**Motion:** **Greenfield** — single card PSP (Stripe), no orchestration layer
**Motion detail:** Stripe is the *sole* named Payment Processor in their own Terms of Use. Apple IAP and Google Play Billing run alongside it as store channels (synced via RevenueCat), but there is no second acquirer and no routing layer. Lead with reach and local rails, not with "you need orchestration" — they know they have one PSP.

---

> ### ⚠️ Three things to read before anything else
>
> **1. This account is in territory, but almost none of its revenue is.** Singapore-HQ'd (so Prateek's, per `CLAUDE.md`), yet **Singapore does not appear in the top 11 traffic markets at all.** The largest market is **Brazil at 17.76%**. Pix/boleto is the highest-value rail check in this account, and it has been treated accordingly — LATAM, North American, MENA and European rails are first-class here, not footnotes.
>
> **2. Traffic is contracting almost everywhere.** Ten of eleven top markets are down over Jul–Sep 2026 (Vietnam ↓47.20%, UK ↓41.83%, Japan ↓33.49%). **Do not write an expansion narrative off the traffic table, and never tell them their traffic is falling.** It does shape the angle: a company with a shrinking top of funnel cares about conversion and approval rates, not about scale.
>
> **3. The corporate situation is live and recent, and it is why this is a buying window.** Meta's acquisition was blocked by Chinese regulators on 2026-04-27; Manus announced independent operation on **2026-08-11**, deleted some user data, cancelled and hand-refunded subscriptions across Stripe/Apple/Google/Alipay, and then **raised >US$500M on 2026-10-08 — five days before this report**. Report this factually. No geopolitical commentary in any outreach.

---

---

> ## 🔍 ANALYST AUDIT — Prateek, 2026-10-13
>
> I verified the load-bearing claims against live sources and scanned the site myself **before** reading the report, so my baseline was not anchored on its conclusions. **The ICP is unchanged at 23/29 ⭐ — no row was struck.** This is the best-evidenced run in the pipeline to date; the corrections below are additive, not remedial.
>
> ### ✅ Confirmed first-hand
> - **⭐ Stripe is the sole PSP, beyond doubt.** I found the live `stripePublicKey` (`pk_live_…`) embedded in both `manus.im/` and `manus.im/pricing` **before** the run reported it, then independently confirmed its claims by fetching **all 21 Next.js chunks (16.18 MB)** from `files.manuscdn.com`. Present and verified by me: **`validateStripeCheckoutUrl` (4 hits)**, **`checkout.stripe.com`**, **`billing.stripe.com`**, plus a complete Stripe-shaped flow — `getStripeSetupCardCheckoutUrl`, `redirectToStripeCheckout`, `buildStripePayUrls`, `STRIPE_ERROR_CODES.PAYMENT_METHOD_REQUIRED`, `stripeErrorCode`/`stripeErrorMessage`, `NeedAction_Update_Payment_Method`. **No second acquirer and no orchestrator exists in 16 MB of production code.** The **+4 greenfield row and the 0 on "Multiple PSPs" both hold.**
> - **⭐ The funding round, verified.** TechCrunch `datePublished 2026-10-08`: *"Boyu Capital and IDG Capital led the funding round, and existing shareholders Tencent, HSG (formerly known as Sequoia China), ZhenFund, and others also participated."* **Five days inside the 12-month window. The +2 is decisive, not marginal.**
> - **`manus.ai` → 302 → `manus.im`**, confirmed independently. Not a separate property; traffic attributed to it is a redirect artefact.
> - **`/checkout`, `/billing` and `/subscribe` are soft-404s** — all within ~50 bytes of my nonsense control `/zzz-control-not-real-7742`. Only `/pricing` is a real distinct page.
>
> ### ⚠️ What I could NOT independently verify
> **The Terms §3.1 quote.** `manus.im/terms` is client-rendered: the body text is absent from the HTML (`Payment Processor`, `third-party service provider`, `automatic billing`, `electronic invoice` all return **0**) **and absent from all 21 chunks** the page loads. Both `stripe` hits on `/terms` are the same `__manus_env__` config blob, not the clause. **This does not mean the quote is wrong** — the run may have reached rendered content I did not — but **I could not confirm it, and the citation should be treated as unverified-by-audit.** It matters little in practice: the *substance* (Stripe as sole payment processor) is confirmed four other ways, including my own first-party evidence above.
>
> ### ⛔ FIVE VENDOR TOKENS FIRED IN THE CHUNKS. ALL FIVE ARE FALSE POSITIVES.
> I checked every one in context rather than trusting the counts:
>
> | Token | Hits | What it actually is |
> |---|---|---|
> | `payu` | 7 | **`buildStripePayUrls`** — the `PayUrl` trap, exactly as predicted |
> | `cellpoint` | 5 | **`onCellPointerDown` / `handleCellPointerDown`** — a table-editor UI handler |
> | `paddle` | 4 | **`faTableTennisPaddleBall`** — a ping-pong icon |
> | `paypal` | 6 | 5 are Font Awesome icons; **1 is real but is a *payout* enum** (below) |
> | `alipay` | 2 | **`faAlipay`** — a Font Awesome brand icon |
>
> ### ⭐⭐ A SYSTEMIC TRAP, NEWLY PROVEN — ADD THIS TO THE PERMANENT LIST
> **Font Awesome's `fab` brand set ships icon definitions for nearly every payment vendor.** Verified in this bundle: `faAlipay`, `faAmazonPay`, `faApplePay`, `faCcAmazonPay`, `faCcAmex`, `faCcApplePay`, `faCcDiscover`, `faCcJcb`, `faCcMastercard`, `faCcPaypal`, **`faCcStripe`**, `faCcVisa`, `faGooglePay`, `faBitcoin`. **`stripe` alone has 3 icon definitions.**
> **Consequence: on any site bundling Font Awesome Brands, a raw grep for payment vendors is worthless.** It will return non-zero for Alipay, PayPal, Apple Pay, Google Pay, Amex, Visa, Mastercard, JCB, Discover and Stripe whether or not any of them is used. **Always check hits in context, and never report a vendor from a count alone.** This affects every future run in this repo, not just this account.
>
> ### 🔎 One substantive distinction the chunks settle
> **PayPal is a REFUND PAYOUT rail, not a pay-in method.** The one genuine PayPal hit is the enum `RefundPayoutMethod{UNSPECIFIED=0, PAYPAL=1, BANK_ACCOUNT=2}`, sitting beside `MANUAL_REFUND_SUCCESS` / `MANUAL_REFUND_FAILED`. That corroborates the run's finding that a failed renewal drops into a manual payout process. **Do not list PayPal as an accepted payment method in any outreach.**
>
> ### 📋 Rows I examined but did not change
> - **Payment issues +2** — satisfied on the matrix's own wording (high-frequency complaints). ⚠️ **Caveat for outreach:** a 1.2/5 Trustpilot with 95% one-star, dated Apr–Oct 2026, almost certainly reflects **the Meta split, the service cancellation and the mass-refund event of August 2026** far more than payment *infrastructure*. Treat it as evidence of payment **operations** strain (the manual SWIFT/PayPal refund path), **not** as evidence of declines or routing failure, and never cite their Trustpilot score to them.
> - **Recent expansion +2** — the run flagged it as a judgement call; it stands on 13 paid-plan countries for "Cue by Manus". Fair.
> - **Tier is robust either way:** striking both of the above still leaves **19/29 ⭐**.
>
> ### ✔️ Safety checks passed
> **No key value anywhere in the file** — the `pk_live` and `cesdkLicense` are correctly held as `[live key present — value deliberately not recorded]` (3 guard phrases). No booking link. The only Yuno-competitor mention is inside a negative-check list. Structure 3/3 collapsibles. ICP re-added independently: **5+4+3+0+3+2+2+2+2+0+0 = 23 across 11 rows.** ✅
>
> ### 📌 The one thing that could still change the verdict
> **The web-vs-app-store revenue split is unpublished.** `hasInAppPurchases: true` is correctly paired to Manus's own bundleId `tech.butterfly.app`, and Google Play shows **$9.99–$4,999.99 per item**. The run argues no override is warranted — chiefly because **Team, SSO, SCIM, Cloud Computer and phone-number plans have no IAP plan keys at all** — and I accept that reasoning. But if IAP turns out to dominate consumer revenue, the orchestratable subset shrinks materially. **This is discovery question #1 and the report says so.**

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Manus is a general AI agent — it runs its own cloud virtual computer to plan, research, write code, build websites, generate slides/video and operate a browser on the user's behalf. It is sold as a recurring subscription (Free / Pro from US$20 per month / Team) that grants a monthly **credit** allowance, with purchasable credit packs, auto top-ups and overage on top. Built by **Butterfly Effect Pte. Ltd.**, which also makes **Monica**; founded in China (Beijing/Wuhan, 2022) and relocated to Singapore in mid-2025.

**SimilarWeb total visits (last full month):** **Not found.** The supplied extract (SimilarWeb, supplied by Prateek 2026-10-13, Jul–Sep 2026, "include all country domains" ON) gives country **shares**, change, audience share and engagement, but **no absolute visit counts**. No visit total is asserted anywhere in this report.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | **Brazil** | **17.76%** (↓21.22%) | Visa, Mastercard, Amex, JCB, UnionPay, Apple Pay, Google Pay, Alipay, Link — all USD-priced | **Pix**, **boleto**, **cartão parcelado** (instalments). Boleto is *structurally* unreachable on a Singapore Stripe account (Stripe: boleto business location = BR only, domestic only). Pix *is* available to SG accounts but is not enabled. | ❌ none found |
| 2 | United States | 13.25% (↓28.22%) | as above | **PayPal** (appears only as a *refund payout* destination, never as an inbound method) | ❌ none found |
| 3 | India | 5.65% (↓26.62%) | as above | **UPI** (Stripe supports UPI from SG accounts — not enabled), **UPI Autopay**, netbanking, RuPay, EMI/no-cost EMI | ❌ none found |
| 4 | Japan | 4.26% (↓33.49%) | as above | **konbini**, **PayPay** — both require a **JP** business location on Stripe, so structurally unreachable today; carrier billing; instalment/bonus payment | ❌ none found |
| 5 | Egypt | 2.95% (↓30.91%) | as above | **Fawry** — not offered by Stripe for any account country | ❌ none found |

Markets 6–11: Saudi Arabia 2.77% (**↑6.87%**, the only market growing) — **mada** absent, not a Stripe method · Thailand 2.52% — **PromptPay** requires a TH account · Korea 2.41% — no Korean local rail on Stripe at all · Vietnam 2.24% — **MoMo/ZaloPay/VNPay** none on Stripe · UK 2.08% — cards only, no PayPal · Taiwan 2.05% — **JKOPay/LINE Pay/ATM transfer** none on Stripe.

> **Entity cells are marked ❌, not ❌🔒.** The APAC reference flags India, Korea, Vietnam and China as markets that gate domestic acquiring behind local presence, but **that is a checklist item, not a source, and no live regulatory source was verified in this run.** The gate that *is* evidenced here is a PSP-level one from Stripe's own documentation (boleto → BR, konbini/PayPay → JP, PromptPay → TH), which is stronger because it is citable.

### Legal entities
- **Butterfly Effect Pte. Ltd.** (Singapore) — the contracting and billing entity, named in the Terms of Use (last updated 28 Sep 2026) and as the Apple App Store seller of record. Governing law Singapore, arbitration SIAC, seat Singapore. UEN **202330764R** per two third-party aggregators (incorporated 02 Aug 2023, 109 North Bridge Road #06-W112, Funan, Singapore 179097) — ⚠️ **aggregators only, not confirmed on ACRA BizFile+, and neither listing mentions Manus.** Treat the UEN as unverified.
- **Beijing Butterfly Effect Technology** (China) — the original company, which "continued to exist as a Chinese-registered company" after the Singapore entity took over the product outside China. No evidence it bills international customers.
- Legal-notice address in the Terms is a US mail drop: *455 Market St Ste 1940, PMB 846230, San Francisco, CA 94105-2448* — a PMB for service of notice, **not** a US operating entity.
- **No entity found in any of the eleven top-traffic markets.**

### Known PSPs
- **Stripe** — **the only card PSP.** Named singular in Terms §3.1; a live `pk_live_` publishable key is embedded in the page config `[live key present — value deliberately not recorded]`; the app's URL allowlist contains exactly `checkout.stripe.com` and `billing.stripe.com`; the entire billing RPC surface is Stripe-shaped. Global.
- **Apple App Store (IAP)** — store billing channel. `hasInAppPurchases: true`, paired to bundleId `tech.butterfly.app`.
- **Google Play Billing** — store billing channel. "In-app purchases $9.99 – $4,999.99 per item", paired to package `tech.butterfly.app`.
- **RevenueCat** — IAP subscription infrastructure (a `RevenuecatSyncCustomer` RPC exists on their own `user.v1.SubscriptionService`). Not an acquirer.
- **Alipay** and **Link** are delivered *through Stripe* (their own help centre cites Stripe's Alipay documentation for the 90-day refund limit). **PayPal and SWIFT bank transfer exist only as manual *refund payout* destinations** — never as inbound methods.

### Orchestration status
**None detected — direct PSP integrations only.** One card acquirer, no routing, no failover, no second acquirer anywhere in the stack. There *is* a thin `payment_platform` switch (`stripe*` / `apple` / `google_play` / `live_event`) that selects a **billing channel by device**, but that is channel selection, not acquirer routing. Greenfield.
Evidence: Terms of Use §3.1 (`https://manus.im/terms`); embedded `stripePublicKey` in `manus.im` page config; `validateStripeCheckoutUrl` allowlist in `files.manuscdn.com/webapp/_next/static/chunks/3okoj2tnxlwg5.js`; help centre "our payment processors (Stripe, Apple, Google)".

### Buying signals
- 💰 **>US$500M raised, announced 2026-10-08 — five days before this report.** Led by Boyu Capital and IDG Capital; Tencent, HSG and ZhenFund participating. Bloomberg reported a ~US$4B target valuation; **the company has not confirmed a valuation.** ([TechCrunch, 2026-10-08](https://techcrunch.com/2026/10/08/chinas-manus-raises-over-500m-in-first-funding-round-since-split-with-meta/))
- 🚀 **Brand-new paid product line: "Cue by Manus"** hit the App Store **2026-10-08** (`ai.manus.agents`, 10K+ Play downloads already) selling **monthly phone-number subscriptions in 13 countries** — AU, CA, CH, EE, GB, HK, IL, IT, JP, NL, SG, TH, US. **None of Brazil, India, Egypt, Saudi, Korea, Vietnam or Taiwan is in that list.**
- 🔁 **They just re-papered the entire commercial relationship.** Independent operation announced 2026-08-11; subscriptions cancelled and pro-rata refunded across Stripe, Google Play, Apple (batch exception) and Alipay; a live `https://manus.im/claim-refund` page still runs a **manual** PayPal-or-SWIFT refund fallback. A company that has just rebuilt its billing relationships is in a re-platforming window.
- 📉 **Conversion pressure, not scale pressure.** Ten of eleven top markets contracting Jul–Sep 2026. The commercial conversation is approval rate and recovered revenue.
- 🤝 **Agentic payments are being built right now.** A first-party `agents.v1.StripeLinkService` lets a user authorise Stripe once and then have the Manus agent pay *third-party merchants* on their behalf, with `payment_failure_code`, `network_id` and `credential_type` on every bill. That is a payments roadmap, not a billing afterthought.
- 📋 **No public payment RFP found.** No payment-related job posting found on `careers.manus.im` or in search.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Manus AI` to draft the 12-touch sequence, or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 23 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ⚠️ **NOT FOUND — ASSUMED ≥100,000/month. `[ASSUMPTION — not researched.]`** See the disclosure block below. **An assumption never fires the under-40,000 rejection**, and here the rejection is not even arithmetically reachable. |
| Orchestration status | **+4** | ✅ "None detected — direct PSP integrations only" (greenfield). Terms §3.1 names Stripe singular; only two Stripe hosts allowlisted; no second acquirer anywhere. **⚑ LOAD-BEARING — audit first.** |
| 3+ countries | **+3** | ✅ 121 countries in the supplied traffic set; eleven markets above 2% share. |
| Multiple PSPs | **0** ❌ | **Row does NOT fire.** One card PSP only. Apple/Google are store billing channels and RevenueCat is IAP infrastructure — none is a second acquirer. Scored down deliberately; this is the point of the account, not a gap in it. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ Top-3 are Brazil, US, India. The merchant's **own published accepted-methods list** (updated 2026-04-29) contains no Pix, no boleto and no UPI; Stripe's own docs confirm boleto needs a BR business location while Pix and UPI *are* available to SG accounts and are simply not switched on. Sourced absence, not a grep. **⚑ LOAD-BEARING — audit second.** |
| Recent expansion | **+2** | ✅ "Cue by Manus" launched 2026-10-08 with **paid monthly phone-number plans in 13 countries**; Manus 2.0 and a desktop app shipped in the same window. **⚑ Judgement call — this is product-led multi-country expansion, not a new-market entry in the classic sense. Audit third.** |
| Payment issues reported | **+2** | ✅ **High frequency.** Trustpilot `manus.im`: **1.2/5 across 214 reviews, 95% one-star**, with dated payment/billing complaints Apr–Oct 2026 from GB, US, VN, SG, TR and GR. |
| Funding >$10M | **+2** | ✅ **>US$500M announced 2026-10-08 — 5 days inside the 12-month window.** Decisive, not marginal. |
| High traffic outside home | **+2** | ✅ Singapore is not in the top 11; the largest single market is Brazil at 17.76%. Home-market share is nowhere near 60%. The most internationally distributed account in this pipeline. |
| Competitor using orchestration | **0** ⬜ | No public case study found of an AI-agent competitor adopting a payment orchestrator. |
| Payment job postings | **0** ❌ | None found on their own careers site (SPA, scanned via its JS bundle) or in search. |

**Tier:** ⭐ **High Priority (17+)** → 23 / 29. No public payment RFP was confirmed, so no RFP override applies.

**Analyst override considered and NOT applied — but read this:**
The app-store override (subscription reference §4) is the one that could invalidate this account, and **the split is genuinely unknown.** IAP is real and material: `hasInAppPurchases: true` on `tech.butterfly.app`, Google Play IAP to $4,999.99 per item, a RevenueCat sync RPC, a `payment_platform` field threaded through the whole billing schema, dedicated help-centre branches for Apple/Google dunning, and a batch refund exception Apple granted them in August. **No split is published anywhere.**
I did not score down, for four evidenced reasons: (a) the Terms name Stripe as **the** Payment Processor, singular, and never name Apple or Google as processors in that clause; (b) the entire `user.v1.SubscriptionService` RPC surface is Stripe-specific — `StripeSetupCheckout`, `StripeCloudComputerCheckout`, `StripePhoneNumberCheckout`, `SSOCheckout`, `SCIMCheckout`, `BillingPage`, `ListInvoices`; (c) **Team, SSO, SCIM, Cloud Computer and phone numbers have no IAP plan keys at all** — the whole business and high-ACV surface is web-only; (d) the IAP schema (`resource_iap.proto`) is scoped to "resource" purchases, not to the core agent membership. **Confirming the split is discovery question #1 and the first thing to re-audit if it comes back app-store-heavy.**

#### Monthly transaction count — mandatory disclosure

**Billing unit being counted:** individual **charges** — i.e. monthly or annual subscription renewals, plus discrete **credit-pack purchases**, plus **auto top-ups**, plus overage charges. Established from first-party schema: `AgentsPlan { plan_key, credit_pack, credits, credit_validity_ms, weekly_limit_credits, stripe_price }` and `AgentsStripePriceDetails { unit_amount, currency, interval, interval_count }`, with intervals limited to monthly and yearly in the `Plan_Key` enum, plus `BUY_PERSON_CREDITS { MIN 1,000 … MAX 999,000 credits }` and `USER_AUTO_TOPUP_OPTIONS [0, 500, 1000, 2000, 3000, 4000, 5000]`. **SOURCED** (their own compiled schema).

**⚠️ NOT FOUND — ASSUMED ≥100,000/month. `[ASSUMPTION — not researched.]`**
Basis, stated so it cannot be mistaken for a measurement:
- Sourced input: **US$125M total revenue run-rate**, company's own statement — "Manus reaches $100M ARR … With $125M total revenue run-rate" (`https://manus.im/blog/manus-100m-arr`, Dec 2025). That is ~**US$10.4M of billing per month**.
- **Unsourced input: average transaction value.** No ATV, order count or subscriber count is published anywhere I could find. **Because one input is unsourced, this is an assumption and not a derivation**, per the method's rule 2.
- Sensitivity, using the sourced US$20/month entry price as an anchor: at a $20 average charge → ~520,000/month · at $60 → ~174,000/month · at $250 → ~42,000/month. **The under-40,000 rejection would require an average charge above roughly US$260**, which is irreconcilable with a free tier, a $20 entry tier and a $9.99 minimum store item. The rejection is not arithmetically reachable here.
- A third-party estimate of **~US$450M annualized as of June 2026** (Sacra) would push the count ~3.6× higher again — `[ESTIMATE, not confirmed]`, not used in the score.
- **Caveat that matters for the business case:** an unknown share of these charges are Apple/Google IAP and **never touch Manus's own acquirer**, so the *orchestratable* (Stripe-web) subset is smaller than the figure above and is not knowable from outside.

**Action:** "confirm monthly transaction count, and the web-vs-app-store split" is item #1 in Manual Research Recommendations.

### Source Notes
- ✅ Stripe is the sole card PSP — Terms of Use §3.1, embedded `pk_live_` key, `checkout.stripe.com`/`billing.stripe.com` allowlist, Stripe-shaped RPC surface, help-centre "our payment processors (Stripe, Apple, Google)".
- ✅ USD-only pricing with no localisation — merchant's own help centre, 2026-02-27.
- ✅ Published accepted-methods list with no Pix, boleto, UPI, konbini, PayPay, Fawry, mada, PromptPay or any Korean/Vietnamese/Taiwanese rail — merchant's own help centre, 2026-04-29.
- ✅ Billing entity Butterfly Effect Pte. Ltd., Singapore law, SIAC — Terms of Use, 28 Sep 2026; Apple seller of record.
- ✅ >US$500M round announced 2026-10-08 — TechCrunch, fetched and read.
- ✅ `hasInAppPurchases: true` paired to bundleId `tech.butterfly.app` by brace-matched object extraction, with two controls that correctly resolved to `false` (`com.granola.ios-prod`) and `true` (`im.monica.app.monica`).
- ✅ BIS Entity List check negative, with a passing control — see the compliance note in Section 6.
- ⚠️ **ACRA UEN 202330764R is from third-party aggregators only**, neither of which links the entity to Manus. Not confirmed on BizFile+.
- ⚠️ **The web-vs-app-store revenue split is not published and is not known.** Nothing in this report asserts one.
- ⚠️ **Whether Pix, UPI or any other method is additionally enabled in their Stripe Dashboard cannot be seen from outside.** Stripe Checkout renders enabled methods server-side on Stripe's own domain. Every rail finding here rests on the merchant's *published* accepted-methods page plus Stripe's *documented* account-country eligibility — never on a grep of Manus's HTML.
- ⚠️ `~US$4B valuation` is Bloomberg-reported and **company-unconfirmed**. `~US$450M annualized` is a Sacra estimate.
- ⚠️ Trustpilot reviews are unverified individual accounts. They evidence a *complaint pattern*, not confirmed company behaviour.

### Success Case Alternatives
- **No Yuno public case study was verified in this research run, so none is named.** Naming a customer or attaching a number to one would breach the repo's referenceability rule. **Required profile for the right reference:** a global digital-subscription or credits business, single-PSP before Yuno, Brazil-weighted or heavily LATAM+APAC distributed, with a measured recovered-revenue or approval-rate outcome on renewals. Pull the matching named reference from Yuno's current published customer list before the sequence is written.

---

## Executive Summary

Manus AI is a Singapore-HQ'd AI-agent company (Butterfly Effect Pte. Ltd., founded in China in 2022, relocated to Singapore mid-2025) selling a recurring subscription with a credits model, from US$20 per month, into **121 countries with no home market** — Brazil is its largest at 17.76% and Singapore does not reach the top eleven. The payment infrastructure finding is unusually clean and unusually strong: **one card acquirer, Stripe, named singular in their own Terms of Use, with USD-only pricing worldwide that their help centre explicitly tells customers their bank will convert and charge foreign-transaction fees on.** The orchestration opportunity is not an efficiency argument but a reach argument — on Stripe's own published eligibility rules a **Singapore**-domiciled account cannot reach boleto (BR-only), konbini or PayPay (JP-only) or PromptPay (TH-only) at all, and Stripe offers no rail whatsoever for Egypt, Saudi Arabia, Korea, Vietnam or Taiwan, which together with Brazil and Japan is **eight of their top eleven markets**; the two rails Stripe *could* serve from Singapore, Pix and UPI, are absent from the merchant's own published accepted-methods list. **Motion: greenfield**, with a re-platforming window opened by August's separation from Meta and a US$500M round closed five days ago.

---

## Section 1: Website Traffic Analysis by Country

**Data source:** **Path 1 — pasted SimilarWeb data supplied by Prateek.** `accounts/traffic/manus-ai.md`, cited throughout as *SimilarWeb (supplied 2026-10-13)*, period Jul–Sep 2026, "All traffic", "Include all country domains" ON. Used verbatim; **not re-researched**. No SimilarWeb API or search-estimate path was used.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | **Brazil** | **17.76%** | Not found | ↓ 21.22% — declining | SimilarWeb (supplied 2026-10-13) |
| 2 | **United States** | **13.25%** | Not found | ↓ 28.22% — declining | SimilarWeb (supplied 2026-10-13) |
| 3 | **India** | **5.65%** | Not found | ↓ 26.62% — declining | SimilarWeb (supplied 2026-10-13) |
| 4 | Japan | 4.26% | Not found | ↓ 33.49% — declining | SimilarWeb (supplied 2026-10-13) |
| 5 | Egypt | 2.95% | Not found | ↓ 30.91% — declining | SimilarWeb (supplied 2026-10-13) |
| 6 | Saudi Arabia | 2.77% | Not found | **↑ 6.87% — the only growing market** | SimilarWeb (supplied 2026-10-13) |
| 7 | Thailand | 2.52% | Not found | ↓ 20.02% — declining | SimilarWeb (supplied 2026-10-13) |
| 8 | Republic of Korea | 2.41% | Not found | ↓ 30.84% — declining | SimilarWeb (supplied 2026-10-13) |
| 9 | Vietnam | 2.24% | Not found | ↓ 47.20% — declining | SimilarWeb (supplied 2026-10-13) |
| 10 | United Kingdom | 2.08% | Not found | ↓ 41.83% — declining | SimilarWeb (supplied 2026-10-13) |
| 11 | Taiwan | 2.05% | Not found | ↓ 20.75% — declining | SimilarWeb (supplied 2026-10-13) |

**Est. Monthly Visits is "Not found" on every row by design.** The supplied extract carries shares, change, audience share and engagement but **no absolute visit counts**, and inventing one would be the exact failure mode this method forbids.

**Markets above 5% share — high priority:** Brazil, United States, India.

**Structural reading (per the supplied analyst notes, which are honoured in full):**
- **There is no home market.** Singapore, the HQ, is absent from the top eleven. No country reaches 18%.
- **Extreme fragmentation: 121 countries, listed total 57.94% across eleven rows, ~42% of traffic in 110 further countries.** Any rail strategy here has to be portfolio-wide; this is not a "localise two markets" account.
- **✅ Engagement is real and strong.** 6–8 minute sessions, 4–6 pages per visit, 32–40% bounce across the top markets, and **Vietnam is exceptional at 15:36 and 12.80 pages per visit**. All eleven are treated as real markets. The two weakest — Thailand (2:25, 53.30%) and Taiwan (48.83% bounce) — are ordinary, not suspect.
- **🚩 Ten of eleven markets are contracting**, several steeply. **No expansion narrative is drawn from this table.** Any volume estimate rests on a declining base; the most recent period is preferred over the quarterly average and the trend is labelled on every row above. Commercially this helps rather than hurts the pitch — a company whose top of funnel is shrinking is more interested in conversion and approval rates than one that is doubling — but it is never said to the prospect.
- **Audience-share pattern is healthy and differs by market.** India's audience share (7.39%) *exceeds* its traffic share (5.65%) — many distinct users, fewer repeat visits. Brazil is the reverse (14.93% vs 17.76%) — fewer users, visiting more often. Neither pattern suggests inflated traffic.

### ⚠️ The "+2 unnamed domains" — RESOLVED, and the answer changes how the table should be read

The supplied extract aggregates `manus.im` **plus two domains that the screenshot does not name**. I probed every candidate property that appears in Manus's own production config and resolved them:

| Domain | Result | Verdict |
|---|---|---|
| `manus.ai` | **HTTP 302 → `https://manus.im/`** (CloudFront) | **Redirect, not a property.** Any traffic attributed to it is an artefact of the redirect. |
| `manus.space` | **HTTP 302 → `https://manus.im/`** at the apex | **Redirect at the apex, not a property.** Subdomains host user-deployed sites; the apex is a redirect. |
| `pages.manus.im` | 302 → `manus.im` | Redirect. |
| `manus.computer`, `manus-preview.space` | No apex site served | Not properties. |
| `monica.im` | HTTP 200 on its own host, same Apple seller of record (Butterfly Effect Pte. Ltd.) | **A real, separate property** — and therefore the only credible candidate for a genuinely additive second domain. ⚠️ **I could not confirm it is in the SimilarWeb set**, so this stays a hypothesis. |

**Consequence to carry into any conversation:** at least one and probably both of the two unnamed aggregated domains are **redirects to `manus.im`**, so the shares above most likely describe `manus.im` alone, slightly inflated by redirect traffic double-counted as separate properties. If the second domain is in fact `monica.im`, the country split is a **blend of two different products** and no single market can be attributed to Manus specifically. Either way, **do not attribute a specific market to a specific property in outreach.**

**Top-traffic markets with no local entity: all eleven.** See Section 2.

---

## Section 2: Legal Entities & Local Presence

**Headquarters:** **Singapore.** Butterfly Effect was founded in China in 2022 with offices in Beijing and Wuhan; following its April 2025 Series B it relocated its headquarters to Singapore, with the three co-founders moving in mid-2025. Of ~120 China-based staff, ~40 core technical employees relocated and the rest were laid off; by late 2025 the company had ~100 employees, mostly in Singapore. ([Wikipedia, *Manus (AI agent)*](https://en.wikipedia.org/wiki/Manus_(AI_agent)), citing Tech in Asia, SCMP, Nikkei Asia and TechCrunch; co-founder Zhang Tao stated "This company right now is headquartered in Singapore" at SuperAI Singapore on 2025-06-18, per [Malay Mail, 2025-07-10](https://www.malaymail.com/news/singapore/2025/07/10/china-born-ai-firm-manus-moves-hq-to-singapore-amid-scrutiny-over-us-chip-curbs-national-security-review/183448).)

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| **Singapore** | **BUTTERFLY EFFECT PTE. LTD.** — the contracting and billing entity | ⚠️ UEN **202330764R** per aggregators only; **not confirmed on ACRA BizFile+**, and neither listing mentions Manus | [Terms of Use](https://manus.im/terms) §Agreement ("This Agreement forms a legally binding contract between you … and Butterfly Effect Pte. Ltd."); Apple App Store seller of record (`https://itunes.apple.com/lookup?id=6740909540`); [companieshouse.sg](https://companieshouse.sg/butterfly-effect-pte-ltd) for the UEN |
| China | Beijing Butterfly Effect Technology — "continued to exist as a Chinese-registered company" | Not found | [Wikipedia](https://en.wikipedia.org/wiki/Manus_(AI_agent)) |
| Cayman Islands | ⚠️ **Not established.** Wikipedia records only that, per people familiar with a US Treasury inquiry, Benchmark's counsel cited the company's **incorporation in the Cayman Islands** as a reason the investment fell outside OISP requirements. It does **not** describe a Cayman parent or the ownership chain. | Not found | [Wikipedia](https://en.wikipedia.org/wiki/Manus_(AI_agent)) |
| USA | ❌ **No operating entity.** The Terms give *455 Market St Ste 1940, PMB 846230, San Francisco, CA 94105-2448* as the certified-mail address for arbitration opt-out and copyright notices. A PMB mail drop for service of notice. | n/a | [Terms of Use](https://manus.im/terms) §12, §13 |
| Brazil, India, Japan, Egypt, Saudi Arabia, Thailand, Korea, Vietnam, UK, Taiwan | **None found** | — | — |

**Cross-Border Gap Analysis**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| Brazil (17.76%) | ✅ #1 | ❌ No | **Evidenced at PSP level:** Stripe boleto requires a **BR** business location and is **domestic-only, ✗ crossborder**. Pix is available to SG accounts but presents in **BRL** and attracts **3.5% IOF**, collected from Brazilian customers paying businesses "domiciled outside of Brazil". Regulatory gate per se not verified in this run. | **High.** USD-priced cards into Brazil's #1 market. |
| United States (13.25%) | ✅ #2 | ❌ No | Not gated | Moderate. USD pricing matches the market; cards acquired from Singapore. |
| India (5.65%) | ✅ #3 | ❌ No | ⚠️ The APAC reference flags India as gating domestic acquiring behind local presence, **but no live RBI/regulatory source was verified in this run, so no regulatory claim is asserted.** What *is* sourced: Stripe supports UPI from a **SG** account (presentment INR), so the rail is reachable and simply not enabled. | **High.** USD-priced cards, no UPI, no UPI Autopay for renewals. |
| Japan (4.26%) | ✅ #4 | ❌ No | **Evidenced at PSP level:** konbini and PayPay both require a **JP** business location on Stripe. | **High.** Two dominant non-card rails structurally unreachable. |
| Egypt (2.95%) | ✅ #5 | ❌ No | Fawry is **not a Stripe payment method in any account country** | **High.** No local rail available from this PSP at all. |
| Saudi Arabia (2.77%) | ✅ #6 | ❌ No | mada is **not a Stripe payment method in any account country** | **High**, and this is the **only growing market** in the portfolio. |
| Thailand (2.52%) | ✅ #7 | ❌ No | **Evidenced:** Stripe PromptPay requires a **TH** business location | High. |
| Korea (2.41%) | ✅ #8 | ❌ No | **No Korean local rail appears in Stripe's payment-method support table at all** (no KakaoPay, Naver Pay or Toss row). ⚠️ The reference's "Korea needs a local entity to acquire domestically" is *not* independently verified here. | High. |
| Vietnam (2.24%) | ✅ #9 | ❌ No | MoMo, ZaloPay and VNPay are **not Stripe payment methods in any account country** | **High** — and Vietnam has the strongest engagement in the whole portfolio (15:36, 12.80 pages/visit). |
| United Kingdom (2.08%) | ✅ #10 | ❌ No | Not gated | Moderate. Cards work; **PayPal is not accepted.** |
| Taiwan (2.05%) | ✅ #11 | ❌ No | JKOPay, LINE Pay and ATM transfer are **not Stripe payment methods in any account country** | High. |

> *"Warning: potential cross-border operation in **Brazil, the United States, India, Japan and Egypt** — the top five markets, ~44% of listed traffic. No local entity found in any of them. Transactions are processed cross-border from a Singapore-domiciled acquirer, with higher scheme costs, lower approval rates and FX exposure. The merchant acknowledges the FX leg in its own help centre: 'Some banks or credit card companies charge a fee for any transaction processed outside of your home country.'"*

> **PSP-level reach gate (this is the citable version of the gate, and it is stronger than the regulatory one):** *"On Stripe's own published eligibility rules, a **Singapore**-domiciled Stripe account cannot accept boleto (BR business location only, domestic only), konbini or PayPay (JP only) or PromptPay (TH only), and Stripe offers no rail at all for Egypt, Saudi Arabia, Korea, Vietnam or Taiwan. That is the dominant local rail in eight of Manus's eleven top markets, unreachable without a second acquirer."*

> **MANUAL:** Verify UEN 202330764R and the officer/shareholder list on ACRA BizFile+ (paid). The aggregator listing has the right name and a plausible incorporation date (02 Aug 2023, which precedes the 2025 relocation and is consistent with Monica launching in 2023) but does not mention Manus, so the match is by name only.

---

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| **Global (web, all markets)** | **Stripe** — sole Payment Processor | `[Terms/Privacy Policy]` — Terms of Use §3.1: *"The Company uses **Stripe** as its third-party service provider for payment services (e.g., card acceptance, merchant settlement, and related services) ("Payment Processor")."* Singular; no other processor is named in that clause. | https://manus.im/terms |
| Global (web) | **Stripe** | `[Source Code]` — a live `stripePublicKey` set to a `pk_live_…` value is embedded in `globalThis.__manus_env__` on both `manus.im/` and `manus.im/pricing`. **[live key present — value deliberately not recorded]** | https://manus.im/ |
| Global (web) | **Stripe Checkout + Stripe Billing portal** | `[Source Code]` — `validateStripeCheckoutUrl()` validates against an allowlist of exactly `new Set(["checkout.stripe.com","billing.stripe.com"])`, then `redirectToStripeCheckout()` throws `"Invalid or untrusted checkout url"` for anything else. **Two hosts. No other PSP checkout domain exists in the allowlist.** | https://files.manuscdn.com/webapp/_next/static/chunks/3okoj2tnxlwg5.js |
| Global (web) | **Stripe Billing is the subscription system of record** | `[Source Code]` — their `SubscriptionStatus` enum mirrors Stripe's own subscription statuses verbatim: `Init / Active / PastDue / IncompleteExpired / Canceled / Trialing`. `AgentsStripePriceDetails { unit_amount, currency, interval, interval_count }` is a Stripe Price. `CreateAgentsStripeCheckout → { checkout_url, hosted_invoice_url }`. `payment_intent_client_secret`, `stripe_error_code`, `stripe_error_message`, `proration_date` all appear as response fields. There is **no independent billing engine.** | decoded `user/v1/subscription.proto`, `user/v1/agents_billing.proto` in https://files.manuscdn.com/webapp/_next/static/chunks/3-xpy7erphbc6.js |
| Global | **Stripe, Apple, Google** named as the processor set | `[Terms/Privacy Policy]` (help centre) — *"These taxes are collected by our payment processors (**Stripe, Apple, Google**) and remitted to the appropriate tax authorities."* | https://help.manus.im/en/articles/11813620-why-are-there-additional-charges |
| iOS | **Apple App Store IAP** | `[App Store]` — `hasInAppPurchases: true`, **paired to bundleId `tech.butterfly.app`** by brace-matched enclosing-object extraction. Controls: `com.granola.ios-prod` → **false**, `im.monica.app.monica` → **true**. The page carries 24 such flags (4 false, 20 true), almost all belonging to carousel neighbours. | https://apps.apple.com/us/app/manus-ai-agent-automation/id6740909540 |
| Android | **Google Play Billing** | `[App Store]` — "In-app purchases **$9.99 – $4,999.99 per item**", paired to `tech.butterfly.app`. Neighbour ranges on the same page belong to `com.anthropic.claude` ($20.00–$279.99), `com.foyer.merlin` ($3.49–$499.99) and `com.connectinno.chataiultraapp` ($1.99–$59.99) and were discarded. **10M+ downloads.** | https://play.google.com/store/apps/details?id=tech.butterfly.app |
| Mobile (both stores) | **RevenueCat** — IAP subscription infrastructure, **not an acquirer** | `[Source Code]` — a `RevenuecatSyncCustomer` RPC exists on their own `user.v1.SubscriptionService`. Also `resource_iap.proto`: `ResourceIAPSource { payment_platform, store, store_environment, bundle_or_package }`. | decoded `user/v1/subscription.proto` in https://files.manuscdn.com/webapp/_next/static/chunks/3-xpy7erphbc6.js |
| Global | **Alipay and Link are served *through Stripe***, not direct | `[Terms/Privacy Policy]` (help centre) — the Alipay 90-day refund limit is attributed to *"the payment provider"* and the reader is pointed at **Stripe's official Alipay documentation**. | https://help.manus.im/en/articles/11711102-how-can-i-request-a-refund-for-a-purchased-membership |
| Global (**outbound refunds only**) | **PayPal** and **SWIFT bank transfer** | `[Source Code]` — `RefundPayoutMethod { UNSPECIFIED, PAYPAL, BANK_ACCOUNT }` with `RefundPayoutRecipientInfo { paypal_email, beneficiary_name, beneficiary_account_number, bank_swift_code, recipient_bank_name, recipient_bank_address_line_1..3 }`. **Refund payout destinations, never inbound methods.** | decoded `userdump/v1/userdump_refund_payout.proto` in https://files.manuscdn.com/webapp/_next/static/chunks/3okoj2tnxlwg5.js |
| Adyen · Checkout.com · Worldpay · Braintree · Airwallex · Razorpay · PayU · Cashfree · 2C2P · Xendit · Midtrans · iPay88 · Omise · GMO · KOMOJU · Toss Payments · NICEPAY · eWAY · Windcave | **Not found** | Vendor scan across all 69 JS chunks served by `manus.im` and `/pricing` (22MB). Every apparent hit was checked in context and was a false positive: `paypal` → FontAwesome `faPaypal`/`faCcPaypal` icon glyphs · `alipay` → the ICANN TLD list and a FontAwesome glyph · `wechat` → user-agent sniffing (`micromessenger`) · `paddle` → `table-tennis-paddle-ball`. | — |

**⛔ Note on the `pix` grep, because Brazil is the #1 market and this is the most dangerous check in the account.** `pix` fires constantly on tracking pixels. The only `pix` hit on `manus.im/pricing` is a component named **`VectorPixel`**. **Zero real Pix hits.** But — critically — **a zero in their HTML is not evidence of absence**, because Stripe Checkout renders enabled methods server-side on `checkout.stripe.com` and they would never appear in Manus's source. **No rail claim in this report rests on a grep of Manus's pages.** Every rail finding rests on (a) the merchant's own *published* accepted-methods page and (b) Stripe's own *documented* account-country eligibility. Section 4 states "Unknown, checkout not accessible" wherever those two sources run out.

### 3B. Payment Orchestrator

**Classification: None detected — direct PSP integrations only (greenfield).**
Evidence type `[Terms/Privacy Policy]` + `[Source Code]`.

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with a single PSP, which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

Searches and scans for Yuno, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, BR-DGE, Pagos and Juspay returned nothing across the 22MB of production JavaScript, the Terms, the privacy policy and the help centre. `accounts/apac-tal.csv` has **no row for Manus, Butterfly Effect or Monica**, so there was no orchestrator column to cross-check.

**One honest nuance, so nobody over-claims in a live conversation.** There *is* a thin platform switch: `PaymentPlatform = { apple: "apple", googlePlay: "google_play", liveEvent: "live_event" }` with `isStripePlatform(e) { return e.startsWith("stripe") }`, and a `payment_platform` field threaded through `AgentsMembership`, `AgentsPlan`, `AgentsInvoice` and `cloud_pc`. **That selects a billing channel by device/OS. It does not route card traffic between acquirers, because there is only one acquirer to route to.** The correct framing is reach and local rails — never "you have nothing".

### 3C. PCI and card-data handling

Checkout is a **hosted Stripe redirect**: `redirectToStripeCheckout()` sends the user to `checkout.stripe.com`, and subscription management goes to `billing.stripe.com`. The served CSP contains a `script-src` directive only — **no `form-action`, no `connect-src`, no `frame-src`, no `frame-ancestors`** — so it provides no asset map, and `strict-dynamic` means the absence of `js.stripe.com` from `script-src` implies nothing at all. **No card fields are posted to a Manus origin on the evidenced flow.** See Section 9.

> **MANUAL:** Walk a live checkout with DevTools from a Brazilian and an Indian IP and record which methods Stripe actually renders. That is the only way to close the Pix/UPI question, and it is the single highest-value manual step in this file.

---

## Section 4: Alternative & Local Payment Methods

**Primary source — the merchant's own published accepted-methods list**, *"What can I do if the payment method is not supported?"*, **updated 2026-04-29**, https://help.manus.im/en/articles/11813666-what-can-i-do-if-the-payment-method-is-not-supported :

| Category | Supported Payment Methods (verbatim) |
|---|---|
| Credit/Debit Cards | Visa, Mastercard, American Express, JCB, China UnionPay |
| Digital Wallets | Apple Pay, Google Pay, Alipay, Link |
| Direct Debit | **PayNow (for users in Singapore)** |

Plus a documented restriction: *"While we gladly accept Alipay for standard subscription payments, please note that Alipay is **not supported for free trial subscriptions**."*

> **⭐ The single most striking fact in this account.** The **only** local rail Manus has built is **PayNow — for Singapore**, the one market that does not appear in its top eleven by traffic. Brazil at 17.76%, India at 5.65% and Japan at 4.26% are served by USD-priced cards and nothing else.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| Global | Visa, Mastercard, Amex, JCB, UnionPay | Cards | **Active in checkout** | help centre, 2026-04-29 |
| Global | Apple Pay, Google Pay | Digital wallet | **Active in checkout** | help centre, 2026-04-29 |
| Global | Alipay (via Stripe) | Digital wallet | **Active in checkout** — excluded from free trials | help centre, 2026-04-29 |
| Global | Link (via Stripe) | Digital wallet | **Active in checkout** | help centre, 2026-04-29 |
| **Singapore** | **PayNow** | Bank transfer / A2A | **Active in checkout** — the only localised rail | help centre, 2026-04-29 |
| **Brazil** (#1, 17.76%) | **Pix** | Real-time A2A | **Not found** on the published list. Reachable in principle — Stripe business locations for Pix include **SG** (settling SGD) — so this is a configuration gap, not a PSP limit. But presentment is **BRL**, which collides with their USD-only policy; **3.5% IOF** applies and by default *"your customer pays the IOF… marked up by 3.5% in your customer's banking app"*; the statement descriptor shows **Ebanx**, not Manus; single Pix capped at **US$3,000** and one customer at **US$10,000/month**; and Checkout in **subscription** mode requires **Pix Automático**. | https://docs.stripe.com/payments/pix |
| **Brazil** | **boleto** | Cash / voucher | **Not found**, and **structurally unreachable.** Stripe boleto: *"Business location: BR"*, *"Geographic coverage: ✓ Domestic, ✗ Crossborder"*. A Singapore account cannot accept boleto at all. | https://docs.stripe.com/payments/boleto |
| **Brazil** | cartão parcelado (card instalments) | BNPL / Instalments | **Not found** | help centre list, 2026-04-29 |
| **United States** (#2) | **PayPal** | Digital wallet | **Not found as an inbound method.** PayPal appears in their stack only as a *refund payout* destination. | help centre list; `RefundPayoutMethod` enum |
| **India** (#3) | **UPI** | Real-time A2A | **Not found** on the published list. Stripe supports UPI from **SG** accounts (presentment INR, customers IN), so it is reachable and not enabled. | https://docs.stripe.com/payments/upi ; help centre list |
| **India** | **UPI Autopay**, netbanking, RuPay, EMI / no-cost EMI | A2A mandate / Cards / Instalments | **Not found** | help centre list |
| **Japan** (#4) | **konbini** | Cash / voucher | **Not found**, and **structurally unreachable** — Stripe konbini business location: **JP** only | Stripe payment-method support table |
| **Japan** | **PayPay** | Digital wallet | **Not found**, and **structurally unreachable** — Stripe PayPay business location: **JP** only | Stripe payment-method support table |
| **Japan** | carrier billing, instalment/bonus payment | Carrier billing / Instalments | **Not found** | help centre list |
| **Egypt** (#5) | **Fawry** | Cash / voucher | **Not found.** **No Fawry row exists in Stripe's payment-method support table for any account country.** | Stripe payment-method support table |
| **Saudi Arabia** (#6) | **mada** | Cards (domestic scheme) | **Not found.** **No mada row exists in Stripe's table for any account country.** The only growing market has no local rail option on this PSP. | Stripe payment-method support table |
| **Thailand** (#7) | **PromptPay** | Real-time A2A | **Not found**, and **structurally unreachable** — Stripe PromptPay business location: **TH** only | Stripe payment-method support table |
| **Thailand** | TrueMoney | Digital wallet | **Not found** | help centre list |
| **Korea** (#8) | **KakaoPay, Naver Pay, Toss, domestic card PG** | Wallets / Cards | **Not found.** **No Korean local rail appears in Stripe's table at all.** | Stripe payment-method support table |
| **Vietnam** (#9) | **MoMo, ZaloPay, VNPay** | Wallets / A2A | **Not found.** **None appears in Stripe's table for any account country.** | Stripe payment-method support table |
| **United Kingdom** (#10) | Cards | Cards | **Active in checkout** — cards cover this market. PayPal absent. | help centre list |
| **Taiwan** (#11) | **JKOPay, LINE Pay, ATM / virtual-account transfer, convenience-store cash** | Wallets / A2A / Cash | **Not found.** **None appears in Stripe's table for any account country.** | Stripe payment-method support table |
| All | Carrier billing, BNPL, crypto | — | **Not found** | help centre list |

> *"Warning: in **Brazil** — Manus's largest market at 17.76% of traffic — **Pix** and **boleto** are the dominant consumer rails and neither appears on Manus's own published accepted-methods list. Boleto cannot be reached at all from a Singapore-domiciled Stripe account, and Pix, which can, presents only in BRL and carries a 3.5% IOF borne by the Brazilian customer by default because Manus is domiciled outside Brazil."*

> *"Warning: in **Japan** (4.26%), konbini and PayPay require a Japanese business location on Stripe. In **Thailand** (2.52%), PromptPay requires a Thai one. In **Egypt**, **Saudi Arabia**, **Korea**, **Vietnam** and **Taiwan** — a further 12.42% of traffic combined — Stripe publishes no local rail for any account country. Across Manus's eleven top markets, the dominant local rail is unreachable on today's stack in eight of them."*

**⚠️ The honest limit of this section, stated plainly.** Manus uses Stripe-hosted Checkout, so the enabled method set is configured in the Stripe Dashboard and rendered on Stripe's domain. The merchant's published list (2026-04-29) and Stripe's documented eligibility are the best obtainable external evidence, and they agree, but **the live geo-rendered method set was not observed**. If Manus has quietly enabled Pix or UPI since April 2026 without updating the help page, this section would be wrong about those two rails — and only those two, since the other eight are blocked at the PSP level. **Status for the live checkout: "Unknown, checkout not accessible."**

> **MANUAL:** VPN into Brazil, India and Japan and screenshot the Stripe Checkout method list for a Pro monthly subscription.

---

## Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| **Unauthorised / repeated charges** — *"They take money from my card without any authorization. 5 transactions in 5 minutes. They rejected refund"* (GB) | Trustpilot | **High** | 2026-10-08 | https://www.trustpilot.com/review/manus.im |
| Unapproved charges — *"they charge your card money that you did not approve!"* (US) | Trustpilot | High | 2026-08-24 | https://www.trustpilot.com/review/manus.im |
| **Wrong-tier renewal charge** — *"When the billing cycle renewed, I was charged the higher tier amount anyway"*, *"no refund has appeared"* (**VN — their #9 market**) | Trustpilot | High | 2026-09-03 | https://www.trustpilot.com/review/manus.im |
| Overcharge vs list price — *"I was charged $40 USD when standard subscription is $20 USD"* (**SG — the HQ market**) | Trustpilot | High | 2026-08-18 | https://www.trustpilot.com/review/manus.im |
| **Refunds refused or unconfirmable** — *"Manus has now admitted in writing that they cannot confirm that my refund was processed"* (US) | Trustpilot | **High** | 2026-09-15 | https://www.trustpilot.com/review/manus.im |
| Refund partially refused (US) | Trustpilot | High | 2026-09-08 | https://www.trustpilot.com/review/manus.im |
| **Credits expiring / clawed back** — *"When the next billing cycle started, 31,132 unused credits expired"* (TR); *"they took those credits back twice"* (GR) | Trustpilot | High | 2026-10-06, 2026-10-07 | https://www.trustpilot.com/review/manus.im |
| Repeat/compounding charges — *"was getting hit charges and more charges"* (GB) | Trustpilot | High | 2026-09-06 | https://www.trustpilot.com/review/manus.im |
| Billing inconsistencies at scale — *"more than $1,000 (thousand USD) worth of billing inconsistencies"* | Trustpilot | Moderate | 2026-04-15 | https://www.trustpilot.com/review/manus.im |
| **Overall rating** | Trustpilot | **1.2 / 5 across 214 reviews — 95% one-star, 2% five-star** | current | https://www.trustpilot.com/review/manus.im |
| **Failed-renewal retry storm with per-attempt bank fees**, and no visible cancel button | Trustpilot (reported in search synthesis) | Moderate | Feb 2026 | `[UNVERIFIED — search summary only, page not fetched]` |
| Chargebacks and consumer-agency complaints (Japan NCAC, a US state AG) reportedly filed | Trustpilot (reported in search synthesis) | Moderate | 2026 | `[UNVERIFIED — search summary only, page not fetched]` |
| **No Reddit threads surfaced.** App-store review text was not mined (only aggregate ratings read: Apple 4.73 / 39,031 ratings US). | Reddit / App Store | — | — | — |

> *"Pattern: the complaint set is dominated by **renewal-time billing failures and irrecoverable refunds**, not by product dissatisfaction — repeated charge attempts, wrong-tier renewals, refunds that the company itself cannot confirm, and credits clawed back at cycle boundaries. Every one of those is a payments-layer failure, and they cluster in exactly the markets where Manus has no local acquiring: GB, US, VN, SG, TR, GR. This maps directly to orchestration: decline-code-aware retries instead of blind repeats, account updater and network tokens so a reissued card does not break a renewal, and refunds that return to the original instrument instead of a manual payout queue."*

**Two complaint themes are corroborated by the merchant's own documentation, which is what makes them usable:**
1. **No decline visibility.** *"Note: **We typically don't receive detailed decline reasons from banks**, so reaching out to them directly is often the quickest way to resolve payment issues."* — https://help.manus.im/en/articles/11711093-why-did-my-payment-fail (2025-12-05). (Verified in both apostrophe forms; the page uses U+2019.)
2. **No automated recovery.** *"**If automatic billing fails for any reason, the Company will issue an electronic invoice indicating that you must manually make full payment** corresponding to the billing period indicated on the invoice by a specified due date."* — Terms of Use §4.2.

---

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | **2026-10-08** | **Butterfly Effect raised >US$500M** — its first round since the Meta deal collapsed. **Boyu Capital** and **IDG Capital** led; existing shareholders **Tencent**, **HSG** (formerly Sequoia China) and **ZhenFund** participated. **No valuation disclosed by the company.** Bloomberg and the WSJ had reported a ~US$4B target; *"The company did not respond to TechCrunch's questions about its valuation."* | **Funding** | https://techcrunch.com/2026/10/08/chinas-manus-raises-over-500m-in-first-funding-round-since-split-with-meta/ |
| 2 | **2026-10-08** | **"Cue by Manus" launched on the App Store** (`ai.manus.agents`, id 6808613358, seller Butterfly Effect Pte. Ltd.) — an agent with its own email address and phone number. Already 10K+ Google Play downloads and Play IAP of $9.99–$1,999.99 per item. Backed by monthly phone-number plan keys for **13 countries** (AU, CA, CH, EE, GB, HK, IL, IT, JP, NL, SG, TH, US) and a first-party `TelecomService`. **A new paid, per-country, recurring product line, five days old.** | **Market Expansion** | https://itunes.apple.com/lookup?id=6808613358 ; decoded `user/v1/subscription.proto` |
| 3 | **2026-08-11** | **Manus announced it would operate as an independent company.** This is the "notification day (August 11)" named in their own refund documentation: subscriptions cancelled, pro-rata refunds issued, user data deleted in a window of 2026-08-23 08:00 → 2026-08-25 07:59 SGT. | M&A / Payment Infrastructure | https://en.wikipedia.org/wiki/Manus_(AI_agent) ; https://help.manus.im/en/articles/16147909-service-change-overview-refunds-timeline-calculation-and-special-cases |
| 4 | **2026-04-27** | **China's NDRC blocked Meta's acquisition**, requiring *"the parties involved to withdraw the acquisition transaction."* Meta announced it was cutting ties on 2026-06-15. Meta had announced the acquisition in **December 2025**, reportedly valued at US$2–3B. | M&A | https://en.wikipedia.org/wiki/Manus_(AI_agent) |
| 5 | **mid-2025** | **Headquarters relocated from Beijing/Wuhan to Singapore** after the April 2025 Series B. Co-founder Zhang Tao: *"This company right now is headquartered in Singapore"* (SuperAI Singapore, 2025-06-18). ~40 of ~120 China-based staff relocated; a separate Singapore entity took over the product outside China; the Beijing company continued to exist as a Chinese-registered firm. | Leadership / Corporate Restructuring | https://en.wikipedia.org/wiki/Manus_(AI_agent) ; https://www.malaymail.com/news/singapore/2025/07/10/china-born-ai-firm-manus-moves-hq-to-singapore-amid-scrutiny-over-us-chip-curbs-national-security-review/183448 |
| 6 | **2025-04-25** | **~US$75M Series B at a ~US$500M valuation**, reportedly **Benchmark**-led, per Bloomberg. Five times the prior valuation, which followed a ~US$10M round from **Tencent** and **HSG**. Funds earmarked for the **US, Japan and the Middle East**. ⚠️ Bloomberg-sourced; **not company-confirmed**. | Funding | https://techcrunch.com/2025/04/25/chinese-ai-startup-manus-reportedly-gets-funding-from-benchmark-at-500m-valuation/ ; https://siliconangle.com/2025/04/25/chinese-startup-behind-manus-reportedly-raises-75m-funding/ |

**Funding verification, since the brief flagged traps here.** Both rounds are real and both are reported, not announced-with-numbers:
- The **April 2025** round — *~US$75M, Benchmark-led, ~US$500M valuation* — is Bloomberg-sourced and carried by TechCrunch and SiliconANGLE. One outlet (Bridge Middle East) wrongly attributes the figures to a company announcement. **Outside the 12-month window; contributes 0 to the ICP row.**
- The **October 2026** round — *>US$500M, Boyu + IDG led* — is a company statement (a WeChat post) for the **amount**, with the **~US$4B valuation reported by Bloomberg and explicitly unconfirmed by the company.** **This is the round that fires the +2 row: 2026-10-08 is five days before 2026-10-13.** Prateek's recollection of "~$75M at ~$500M in 2025" was right, and the "further raise at a much higher valuation" is this one.

**No public payment-related RFP found.**

**No payment-related job posting found.** `careers.manus.im` is a client-rendered SPA (its own Manus-built WebDev app, served from `/__manus/`, hiring via `hiring@manus.ai`, job data behind `/api/trpc/hr`); scanning its JavaScript bundle returned zero hits for payment, billing, monetization, Stripe, fraud, risk or pricing. Third-party boards list ~28 open Singapore roles (security, data, frontend, Golang backend) with **no payments or billing title**. That ICP row scores 0.

**🛡️ Compliance pre-check — negative, with a passing control.** Given the z.ai precedent in this repo, I checked the US BIS Entity List corpus directly rather than from memory. Federal Register API, documents from the Bureau of Industry and Security:
- `"Butterfly Effect"` → **count 0**
- `"Manus"` → **count 0**
- **Control: `"Zhipu"` → count 1**, returning *Addition of Entities to and Revision of Entry on the Entity List*, published 2025-01-16 — the known listing. **The control passes, so the zeros are meaningful, not an artefact of a broken query.**
⚠️ **Scope limit, stated so nobody over-reads it:** this covers **BIS Federal Register documents only**. The eCFR Supplement No. 4 to 15 CFR Part 744 returned **HTTP 403** at the egress proxy and a sanity grep of the failed download correctly found neither "Huawei" nor "Zhipu", confirming the fetch produced nothing usable. **OFAC SDN/Consolidated, DoD 1260H and the BIS Denied Persons List were NOT checked in this run.** This is **not** a compliance clearance. Escalate to Yuno legal if the China-origin history is material to a deal, and note that the US Treasury OISP question around the Benchmark investment is referenced in public reporting.

---

## Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | **2026-09-02** | **"Service Change Overview: Refunds' Timeline, Calculation, and Special Cases"** — their own operational account of mass refunds following the separation. Platform-specific handling: *"Refunds for purchases made via **Stripe or Google Play** will be automatically routed back to your original payment method"*; **Alipay** payments older than 90 days *"cannot be refunded… For details about the payment-provider limitation, see Stripe's official Alipay documentation"*; **Apple** *"has granted an exception for this business separation event… We will proactively submit a **batch refund request to Apple** covering all affected users."* | **The clearest possible read on their actual payment stack and its limits**, written by them, under pressure | https://help.manus.im/en/articles/16147909-service-change-overview-refunds-timeline-calculation-and-special-cases |
| 2 | **2026-09-02** | **The manual refund fallback, and why it exists.** *"If you paid by credit card but **your credit card has expired**, in this case you will receive a one-time encrypted refund receipt, please open http://manus.im/claim-refund to submit the refund receipt… We will verify your refund receipt and **manually process the refund**. Please note that this takes **approximately 3 weeks** from submission."* The matching first-party schema asks the customer for a **PayPal email** or a full international wire — `beneficiary_account_number`, `bank_swift_code`, `recipient_bank_name`, `recipient_bank_address_line_1..3`. **`https://manus.im/claim-refund` is live today: HTTP 200, 176,711 bytes, `<title>Provide your refund details - Manus</title>`, against a 404 control of 137,445 bytes on a nonsense path.** | **A stale card credential forces a 3-week manual SWIFT or PayPal payout.** Account updater and network tokens are the mechanism that removes this entire queue. | https://manus.im/claim-refund ; decoded `userdump/v1/userdump_refund_payout.proto` |
| 3 | **2026-04-29** | Accepted-methods page updated — Visa/MC/Amex/JCB/UnionPay, Apple Pay, Google Pay, Alipay, Link, **PayNow (Singapore only)**. *"We are continuously working to expand our supported options."* | The authoritative rail list, and an explicit statement that expansion is on their roadmap | https://help.manus.im/en/articles/11813666-what-can-i-do-if-the-payment-method-is-not-supported |
| 4 | **2026-02-27** | **"What is the pricing unit for Manus globally? Can I pay in local currency?"** — *"All our subscription and credit prices are standardized in **United States Dollars (USD)** to ensure fairness and equality for all users, regardless of their location."* The page then assigns to the customer's bank the jobs of converting the currency, setting the rate and *"Applies any relevant fees, such as currency conversion or foreign transaction fees."* | **USD-only pricing into Brazil, India, Japan, Egypt, Saudi Arabia and Vietnam, documented by the merchant.** The FX leg and the foreign-transaction fee are pushed onto the customer by policy. | https://help.manus.im/en/articles/11711125-what-is-the-pricing-unit-for-manus-globally-can-i-pay-in-local-currency |
| 5 | **2025-12-15** | **"Why are there additional charges?"** — *"the membership prices for Manus on both mobile and web platforms are consistent"*; taxes *"collected by our payment processors (Stripe, Apple, Google)"*; and *"Some banks or credit card companies charge a fee for **any transaction processed outside of your home country**."* | Price parity across web and IAP means the 15–30% store commission is absorbed, not passed on `[INFERENCE, not confirmed]` — a direct margin argument for growing web billing. And the merchant concedes every transaction is foreign-acquired. | https://help.manus.im/en/articles/11813620-why-are-there-additional-charges |
| 6 | **2025-12-05** | **"Why did my payment fail?"** — *"Some banks block certain online or **international transactions** by default"*; *"**We typically don't receive detailed decline reasons from banks**"*; and *"we strictly prohibit the use of **third-party payment platforms** for transactions… Such behavior may lead to… **Account Risk Control**… your account may be restricted."* | **Three findings in one page:** cross-border declines are a known issue; they have no decline-code visibility; and enough customers are paying through intermediaries — the predictable behaviour when a local rail is missing — that they had to publish a prohibition and wire it to risk controls. | https://help.manus.im/en/articles/11711093-why-did-my-payment-fail |

**No provider removal found.** Nothing indicates Stripe, Apple, Google or Alipay has been discontinued.

---

## Section 8: Checkout Experience Audit

**Partially accessible.** Pricing is behind client-side rendering and checkout is behind authentication on Stripe's domain, so this is assembled from the served HTML, the decompiled production bundle, the CSP, route probing against controls, and the merchant's own help centre. **The live geo-adapted method list was not observed.**

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | **Hosted redirect to Stripe Checkout** | **Good** | `redirectToStripeCheckout()` validates against `new Set(["checkout.stripe.com","billing.stripe.com"])` and throws `"Invalid or untrusted checkout url"` otherwise. Desktop app opens it via `desktopApis.system.openExternal`. |
| Guest checkout | **No** — an account is required before purchase | Fair | Purchase is bound to a Manus account; plan state lives on `AgentsMembership`. |
| Steps to complete payment | Account → `/pricing` → plan select → redirect to Stripe Checkout → return | Good | `CreateAgentsStripeCheckout → { checkout_url, hosted_invoice_url }`. |
| Card input experience | **Tokenised on Stripe's own domain** | **Good** | No card fields on a Manus origin on the evidenced flow. |
| Payment methods visible | Cards (Visa/MC/Amex/JCB/UnionPay), Apple Pay, Google Pay, Alipay, Link; PayNow in Singapore | **Poor for the portfolio** | Zero local rails in ten of the eleven top markets. |
| Location-based method display | **Unknown, checkout not accessible.** Stripe can adapt the method set by customer country — but it can only offer what the merchant enabled, and the published list shows one localised rail. | **Unknown** | Highest-value manual check. |
| Instalment / EMI options | **Not found** — no India EMI, no Japan instalment/bonus, no Brazil parcelado, no Taiwan instalment | **Poor** | Lower-impact for a $20/month SKU, but the Pro ladder runs far higher. |
| 3DS implementation | **Not detected directly.** Stripe Checkout applies 3DS2 where required `[INFERENCE, not confirmed]`. Terms §3.1: *"online payment transactions may be subject to validation checks by our Payment Processor and your card issuer."* | Unknown | — |
| PCI indicator | PSP-hosted redirect — card data never reaches a Manus origin | **Good** | See Section 9. |
| Mobile responsiveness | Native iOS and Android apps with store IAP; `PAYMENT_PLATFORM_DISPLAY_MAP = { google_play: "Android app", apple: "iOS app" }` | Good | Apple 4.73/5 from 39,031 US ratings; Google Play 10M+ downloads. |
| Multi-currency / local pricing | **❌ USD only, worldwide, by stated policy.** Corroborated in code: the price formatter is `` `$${(r/100).toLocaleString("en-US", …)}` `` — a hard-coded `$` glyph and a hard-coded `en-US` locale. | **Poor** | *"All our subscription and credit prices are standardized in United States Dollars (USD)… regardless of their location."* |
| Saved payment methods | Yes — Stripe Billing portal, reached via an **"Edit billing"** button; `StripeSetupCheckout` exists for card-on-file setup | Good | Help centre documents add-new-then-delete-old, and *"If you cannot see the 'Edit billing' button, please contact us."* |
| Error message clarity | **Poor, by their own admission** | **Poor** | *"We typically don't receive detailed decline reasons from banks."* The customer-facing remedy is "contact your bank". |
| **Dunning / involuntary churn** | **❌ No automated recovery path documented** | **Poor** | Terms §4.2: automatic billing failure → a manual electronic invoice. Help centre: a past-due renewal *"may be temporarily suspended"* and *"can restrict your ability to manage your subscription, such as downgrading, canceling, or making other changes"*; the documented fixes are "Edit billing" with a different card, or "Downgrade to Free" and re-purchase. App-store subscribers are sent to Apple or Google. |

**Route probing, each against a deliberately nonsense control.** A 200 was never treated as a page without one:

| Path | HTTP | Bytes (transfer) | Verdict |
|---|---|---|---|
| `/` | 200 | 45,919 | Real |
| `/pricing` | 200 | 29,662 | **Real and distinct** — but body fully client-rendered: stripping tags leaves **710 characters** and the markup carries `BAILOUT_TO_CLIENT_SIDE_RENDERING`. No prices in the HTML. |
| `/terms`, `/privacy` | 200 | 10,852 / 10,878 | Real pages; text leaves **15 / 17 characters** after tag-stripping. The actual legal text is a Notion export embedded in chunk `30_trvxj7u1af.js`. |
| **`/claim-refund`** | **200** | 23,802 (176,711 decompressed) | **Real** — `<title>Provide your refund details - Manus</title>` |
| `/checkout` | **404** | — | Does not exist |
| `/billing` | **404** | — | Does not exist |
| `/subscribe` | **404** | — | Does not exist |
| `/payment` | **404** | — | Does not exist |
| `/zzz-nonsense-control-9f3a` (control) | **404** | — | Control |
| `/zzz-control-2-not-real-8831` (control) | **404** | — | Control |

**Served CSP** — a single directive, `script-src 'self' 'nonce-…' 'strict-dynamic' 'wasm-unsafe-eval' https://cdn.vector.co https://a.usbrowserspeed.com`. **No `connect-src`, `frame-src`, `form-action` or `frame-ancestors`**, so it is not usable as an asset map, and because `strict-dynamic` lets any trusted script inject further scripts, **the absence of `js.stripe.com` implies nothing.** The embedded `pk_live_` key proves Stripe regardless. Third-party tags observed: Google Tag Manager (`GTM-TFGFC7KH`), Plausible, Amplitude, Intercom, FingerprintJS, Cloudflare Turnstile, hCaptcha, Sentry at `sentry.prod.ops.butterfly-effect.dev`.

> **MANUAL:** Purchase a Pro monthly subscription from a Brazilian IP with DevTools open, and record the rendered method list, the presentment currency, the 3DS flow and the statement descriptor.

---

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | **Not found.** No PCI documentation is published. A Trust Center exists at `https://trust.manus.im/` but was not interrogated in this run. | — |
| Card data handling | **SAQ A profile** `[INFERENCE, not confirmed]` — checkout is a full redirect to `checkout.stripe.com` with an allowlist that rejects any other host, and the served CSP exposes no `form-action` pointing at a Manus origin. No evidence of card fields on a Manus origin. | `validateStripeCheckoutUrl` / `redirectToStripeCheckout` in `3okoj2tnxlwg5.js`; Terms §3.1 *"you will be required to provide your payment details… directly to our Payment Processor"* |
| Recommended Yuno integration | **Back-to-back API, with Yuno-hosted or SDK method rendering for new rails.** They already hand card capture entirely to a PSP and their own billing state machine is thin and Stripe-shaped, so adding acquirers and rails behind an orchestration layer does not pull card data back into their scope. | — |

> `[INFERENCE, not confirmed]`: Based on confirmed use of Stripe's hosted tokenised checkout, the company's PCI scope is likely reduced, with Stripe handling card data.

*No direct PCI compliance documentation found publicly for Manus AI.* No compliance level is stated here, because none is evidenced.

---

## Section 10: Strategic Insights & Outreach Angles

> ### Insight #1: Brazil is their biggest market and their worst-served one — and one of the two fixes is impossible on today's stack
> **Evidence:** **S1** — Brazil is #1 at **17.76%** of traffic, ahead of the US at 13.25%, with 7-minute sessions and a 32.95% bounce rate (SimilarWeb, supplied 2026-10-13). **S4** — Manus's own published accepted-methods list (2026-04-29) has **no Pix and no boleto**; the only localised rail they have built is **PayNow for Singapore**, a market that is not in their top eleven. **S3A/S2** — the sole acquirer is a **Singapore**-domiciled Stripe account, and per Stripe's own documentation **boleto requires a BR business location and is domestic-only, ✗ crossborder** (https://docs.stripe.com/payments/boleto), while **Pix is available to SG accounts but presents in BRL, carries a 3.5% IOF that by default "your customer pays… marked up by 3.5% in your customer's banking app" because Manus is domiciled outside Brazil, shows Ebanx as the statement descriptor, caps a single payment at US$3,000, and needs Pix Automático for subscription mode** (https://docs.stripe.com/payments/pix). **S7** — pricing is **USD-only by stated policy**, so a Brazilian buyer pays USD, their bank sets the rate, and their bank adds a foreign-transaction fee.
> **Pain Point:** Their largest market is asked to pay in a foreign currency, on a card, with an FX spread and a cross-border fee, with no access to the two rails most Brazilian consumers actually use — and the better of those two, boleto, cannot be switched on at any price without a Brazilian acquiring relationship. Every one of those is a conversion tax on 17.76% of their traffic, at the exact moment that traffic is contracting.
> **Yuno Value Proposition:** One integration that adds a **Brazilian acquirer** alongside Stripe, so Pix and boleto become domestic rails with BRL presentment, no IOF markup passed to the customer, a recognisable descriptor, and **Pix Automático for renewals** — with card traffic still routed to whichever acquirer performs best per BIN. Nothing is ripped out; Stripe keeps the rest of the world.
> **Best Success Case:** A global digital-subscription business, Brazil-weighted, previously single-PSP, with a published recovered-revenue or approval-rate number. **Name the specific Yuno reference only from the current published customer list — none was verified in this run.**
> **Outreach Angle:** Brazil is their single largest market and the one place their published method list offers nothing local; the boleto limit is a property of where their acquirer sits, not of their roadmap.
> **Suggested Subject Line:** Brazil is 17.76% of your traffic — and your biggest rail gap

> ### Insight #2: The only local rail they've built is for the market with the least traffic
> **Evidence:** **S4** — the accepted-methods page lists exactly one localised rail: *"Direct Debit — **PayNow (for users in Singapore)**"* (2026-04-29). **S1** — **Singapore does not appear in the top eleven markets at all**; the eleven listed run from Brazil at 17.76% down to Taiwan at 2.05% and total 57.94%, with ~42% in 110 further countries. **S2** — Singapore is where the billing entity sits (Butterfly Effect Pte. Ltd., Terms of Use, 28 Sep 2026).
> **Pain Point:** Rail investment has followed the **entity**, not the **customers**. The one market where they have presence got a native rail; the markets generating the revenue got USD cards. That is the signature of a stack chosen for where the company is incorporated rather than where it sells — and it means the next ten rails are each a separate PSP project under today's architecture.
> **Yuno Value Proposition:** Decouple rail coverage from entity footprint. One integration, local acquiring and local methods per market, without standing up an entity or a PSP contract per country.
> **Best Success Case:** A company that scaled rail coverage far beyond its entity footprint. **Reference to be named from Yuno's published list.**
> **Outreach Angle:** They built PayNow for the one market not in their top eleven — an observation about where the stack came from, not a criticism of it.
> **Suggested Subject Line:** PayNow in Singapore, cards everywhere else

> ### Insight #3: They have told their customers, in writing, that they cannot see why payments fail
> **Evidence:** **S7/S5** — *"**We typically don't receive detailed decline reasons from banks**, so reaching out to them directly is often the quickest way to resolve payment issues"* and *"Some banks block certain online or **international transactions** by default"* (https://help.manus.im/en/articles/11711093-why-did-my-payment-fail, 2025-12-05). **S3A** — one acquirer, Singapore-domiciled, so every card transaction in all 121 countries is cross-border. **S5** — Trustpilot 1.2/5 across 214 reviews, with renewal-time billing failures dated Apr–Oct 2026 from GB, US, VN, SG, TR and GR, including *"5 transactions in 5 minutes"* (2026-10-08).
> **Pain Point:** No decline-code visibility plus a single foreign acquirer plus no retry intelligence equals blind repeat attempts, bank fees landing on the customer, and support deflection to the issuer. The declines they cannot explain are disproportionately the cross-border ones they cannot route around.
> **Yuno Value Proposition:** Normalised decline codes across providers in one view; retries sequenced by decline reason and issuer rather than on a fixed schedule; correct MIT/stored-credential flagging on renewals; and the option to route a failed renewal to a local acquirer in the cardholder's own market. The decline reason stops being a thing their PSP doesn't pass on.
> **Best Success Case:** A subscription business that cut involuntary churn through decline-aware retries and local renewal routing. **Reference to be named from Yuno's published list.**
> **Outreach Angle:** Their own help centre says they don't get decline reasons — a fixable visibility gap, not a product problem.
> **Suggested Subject Line:** "We typically don't receive detailed decline reasons"

> ### Insight #4: An expired card currently costs them a three-week manual SWIFT wire
> **Evidence:** **S7** — *"If you paid by credit card but **your credit card has expired**… please open http://manus.im/claim-refund to submit the refund receipt… we will **manually process the refund**… approximately **3 weeks** from submission"* (https://help.manus.im/en/articles/16147909-…, 2026-09-02). **S3A** — the matching first-party schema, `RefundPayoutService`, asks the customer for a **`paypal_email`** or a full international wire: `beneficiary_name`, `beneficiary_account_number`, **`bank_swift_code`**, `recipient_bank_name`, `recipient_bank_address_line_1..3`, with statuses `MANUAL_REFUND_PENDING / IN_PROGRESS / SUCCESS / FAILED` and `NEEDS_SUPPORT`. `https://manus.im/claim-refund` is **live today (HTTP 200, 176,711 bytes, title "Provide your refund details")** against a 404 control. **S8** — no account-updater or network-token behaviour is evidenced anywhere; Terms §4.2 says a failed automatic bill becomes a manual invoice.
> **Pain Point:** A stale card credential — the most ordinary event in subscription billing — currently escalates into a hand-built payout queue with PayPal and SWIFT legs, three-week turnarounds, wire fees, and a support load. The same missing capability that makes a refund manual is what makes a **renewal** fail in the first place.
> **Yuno Value Proposition:** Network tokens and account updater inside the routing layer, so credentials refresh without customer action and without a per-PSP project — and refunds return to a live instrument instead of a manual queue. One capability, both problems.
> **Best Success Case:** A subscription business where network tokens and account updater removed a manual exception queue. **Reference to be named from Yuno's published list.**
> **Outreach Angle:** The expired-card path they documented in September is the same gap that breaks renewals; card lifecycle management closes both.
> **Suggested Subject Line:** The expired-card path on your refund page

> ### Insight #5: They just re-papered the whole commercial relationship, and funded it five days ago
> **Evidence:** **S6** — independent operation announced **2026-08-11**; subscriptions cancelled and pro-rata refunded across **Stripe, Google Play, Apple (under a batch exception Apple granted) and Alipay**; data deletion window 2026-08-23 → 08-25 SGT; **>US$500M raised 2026-10-08** led by Boyu and IDG. **S6** — **"Cue by Manus"** shipped **2026-10-08** with **monthly phone-number plans in 13 countries** — and **none of Brazil, India, Egypt, Saudi Arabia, Korea, Vietnam or Taiwan is among them.** **S3B** — orchestration status today: none detected, one acquirer. **S11** — of their closest Chinese-origin AI peers, the two furthest along (per internal TAL research, 2026-09-30) have already moved past single-PSP Stripe to in-house multi-rail stacks.
> **Pain Point:** Every commercial system was touched in the last eight weeks, a new per-country recurring product line just launched on a rail set that cannot bill most of their own largest markets, and there is now capital to fix it. A payment stack gets rebuilt in windows like this one or not for two years.
> **Yuno Value Proposition:** Arrive while the architecture is open. Add acquirers and rails per market behind one integration so Cue's country list is a commercial decision rather than a PSP-eligibility one, and so the next launch does not inherit the same eight-market rail gap.
> **Best Success Case:** A company that consolidated payments onto orchestration during a post-separation or post-funding replatform. **Reference to be named from Yuno's published list.**
> **Outreach Angle:** Cue launched into 13 countries that do not include their top three markets — a rail-availability pattern, not a product decision.
> **Suggested Subject Line:** Cue's 13 countries don't include your top three

---

## Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. Brazil is Manus's single largest market at 17.76% of traffic, and their own accepted-methods page lists neither Pix nor boleto — and boleto cannot be enabled at all on a Singapore-domiciled Stripe account, because Stripe requires a Brazilian business location for it.
2. The only localised payment rail Manus has built is PayNow for Singapore — the one market that does not appear in their top eleven by traffic.
3. Their help centre tells customers, in their own words, that they "typically don't receive detailed decline reasons from banks" — on a stack where every card transaction in 121 countries is cross-border.

**Cold call openers (conversational, one sentence each):**
1. "I was looking at your pricing page — everything is quoted in USD worldwide, and Brazil is your biggest market; how is that landing on approval rates there?"
2. "Your refund page has a path for customers whose card has expired, where you wire the money manually and it takes about three weeks — is that volume you're still carrying?"
3. "Cue launched into thirteen countries last week, and Brazil, India and Japan weren't among them — was that a product call or a rail-availability call?"

---

## Section 11: Similar Companies & Prospecting Pipeline

### 11A. Direct Competitors (AI agents / agentic coding and automation)

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| **Genspark** | genspark.ai | USA | Growth-stage | Global, strong APAC | Not found | App Store neighbour (`ai.mainfunc.genspark`, IAP true) |
| **Lovable** | lovable.dev | Sweden | Growth-stage | Global | Not found | App Store neighbour (`dev.lovable.build`, IAP true); named on Manus's own `/compare/lovable` |
| **Replit** | replit.com | USA | Large | Global | Not found | Named on Manus's own `/compare/manus-vs-replit` |
| **OpenAI (ChatGPT agent mode)** | openai.com | USA | Very large | Global | Not found | Named on Manus's own `/compare/vs-chatgpt` |
| **Moonshot AI (Kimi)** | moonshot.ai | China (bills from Singapore) | Large | Global, APAC-weighted | **IN-HOUSE** — internal TAL research decoded `growth.pay.v1.PayService` from their production bundle; ICP **22/29**. Billing entity NOVASCENT PRIVATE LIMITED (Singapore, UEN 202326494K). ⚠️ internal TAL, researched 2026-09-30, **not re-verified here** | `accounts/apac-tal.csv`; App Store neighbour `com.moonshot.kimichat` |
| **MiniMax** | minimax.io | China (bills from Singapore) | Large | Global; Vietnam #1 | **IN-HOUSE** over Stripe/Airwallex/Alipay; ICP **23/29**; **already outreached** (`3-outreached/minimax-io.md`). **And Manus's own code sets `FREE_VIDEO_MODEL: "minimax-h3"` — Manus is a MiniMax customer.** ⚠️ internal TAL, not re-verified here | `accounts/apac-tal.csv`; decoded chunk `3d4s07pvglcez.js` |
| **z.ai (Zhipu AI)** | z.ai | China (bills from Singapore) | Large | Global | **IN-HOUSE** (Stripe + PayPal); ICP **23/29**; 🛑 **BLOCKED — BIS Entity List compliance hold.** ⚠️ internal TAL, not re-verified here | `accounts/apac-tal.csv` |
| **Kling AI** | kling.ai | China (bills from Singapore) | ~US$500M ARR claim | Global | **GREENFIELD, single-PSP Stripe** — ICP **23/29**. Billing entity Kling AI Pte. Ltd. (Singapore, UEN 202502609E). **The closest structural twin to Manus in this repo.** ⚠️ internal TAL, researched 2026-09-29, not re-verified here | `accounts/apac-tal.csv` |
| **Monica** | monica.im | Singapore | — | Global | **Same company** — Butterfly Effect Pte. Ltd. is the Apple seller of record for both. Not a competitor; a sibling product, and the only credible candidate for the second aggregated SimilarWeb domain. | `https://itunes.apple.com/lookup?id=6450770590` |

### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Ahrefs | ahrefs.com | SaaS | Global | **Singapore-HQ'd, "Stripe; cards" in the TAL, ~$150M est.** — the same Singapore-entity/USD-cards/global-customers shape | `accounts/apac-tal.csv` |
| Canva | canva.com | SaaS | Global, ANZ-HQ | Very large global consumer subscription with credits-style add-ons; sits in `1-to-outreach/canva.md` | `accounts/apac-tal.csv` |
| Linktree | linktr.ee | SaaS | Global | ~$100M ARR est., global consumer subscription | `accounts/apac-tal.csv` |
| BrowserStack | browserstack.com | SaaS | Global, India-HQ | ~$250M ARR est., usage-metered developer subscription | `accounts/apac-tal.csv` |
| Chargebee | chargebee.com | SaaS | Global, India-HQ | Subscription-billing vendor; useful for recurring-rails context, **not a prospect** | `accounts/apac-tal.csv` |
| Goodnotes | goodnotes.com | SaaS | Global, HK-HQ | App-store-heavy consumer subscription — the right comparison for the IAP-split question | `accounts/apac-tal.csv` |
| TRAX | traxretail.com | SaaS | SG + Global | Singapore-HQ'd, ~$100M est., global B2B | `accounts/apac-tal.csv` |
| InVideo AI / Murf AI | invideo.io / murf.ai | AI | Global, India-HQ | Credits-based AI subscriptions, USD-priced, global long tail | `accounts/apac-tal.csv` |

### 11C. Companies Recently Adopting Payment Orchestration

*No public case studies found of direct competitors adopting payment orchestration.* Searches across the AI-agent and AI-model vertical returned nothing. The pattern visible in internal TAL research is different and worth knowing: **the Chinese-origin AI companies that have scaled furthest have built their own multi-rail layers in-house rather than buying orchestration** — MiniMax, Moonshot and z.ai are all recorded as in-house, while Kling AI remains single-PSP Stripe like Manus. **That is the competitive risk on this account: Manus is more likely to build than to buy unless it is reached in the current window.** The ICP row scores **0** because no orchestrator adoption is confirmed.

### 11D. Prospect Scoring (29-point matrix, verified signals only)

| Signal | Points | Status | Evidence Source |
|--------|--------|--------|-----------------|
| **Genspark** — monthly transactions | 0 ⬜ | Not researched | — |
| Genspark — orchestration | 0 ⬜ | Unknown | — |
| Genspark — 3+ countries | +3 ✅ | Global consumer AI product, IAP across App Store regions | App Store listing |
| Genspark — funding >$10M | 0 ⬜ | Not verified in this run | — |
| **Genspark subtotal** | **3 (floor)** | Under-researched; a real score needs its own run | — |
| **Kling AI** — full matrix | **23/29** ⚠️ | **GREENFIELD, single-PSP Stripe, Singapore billing entity.** The closest structural twin to Manus. ⚠️ internal TAL figure, researched 2026-09-29, not re-verified here | `accounts/apac-tal.csv` |
| **Moonshot AI** — full matrix | **22/29** ⚠️ | IN-HOUSE motion. ⚠️ internal TAL, 2026-09-30, not re-verified | `accounts/apac-tal.csv` |
| **MiniMax** — full matrix | **23/29** ⚠️ | IN-HOUSE; **already outreached** | `accounts/apac-tal.csv`, `3-outreached/minimax-io.md` |
| **z.ai** — full matrix | **23/29** ⚠️ | 🛑 BLOCKED on compliance | `accounts/apac-tal.csv`, `2-ready-to-outreach/z-ai.md` |
| **Monica (Butterfly Effect)** | **n/a** | **Same company and same billing entity as Manus** — not a separate prospect. If `monica.im` is the second aggregated SimilarWeb domain, it is also inside this account's traffic. | Apple seller of record |

**Only verified signals are scored. Genspark, Lovable and Replit are genuinely under-researched here and their rows show floors, not scores** — the research budget went into Manus itself, as it should have.

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | **Manus AI** | Target | BR, US, IN, JP, EG, SA, TH, KR, VN, UK, TW | **23/29** | ⭐ High | Single-PSP Stripe on 121 countries; USD-only; 8 of 11 top markets' dominant rail unreachable; US$500M raised 5 days ago | **❌ NO — genuine new find** |
| 2 | **Genspark** | Direct competitor | Global, APAC-weighted | 3 (floor) | 🟡 Needs own run | Closest product analogue; no stack evidence either way | **❌ No** |
| 3 | **Lovable** | Direct competitor | Global | Not scored | 🟡 Needs own run | Named on Manus's own comparison page | **❌ No** |
| 4 | **Replit** | Direct competitor | Global | Not scored | 🟡 Needs own run | Named on Manus's own comparison page | **❌ No** |
| 5 | Kling AI | Peer (closest twin) | Global | 23/29 ⚠️ | ⭐ High | Greenfield single-PSP Stripe, Singapore entity | ✅ Yes, Not Contacted, P1 |
| 6 | Moonshot AI (Kimi) | Peer | Global | 22/29 ⚠️ | ⭐ High | In-house pay service | ✅ Yes, Not Contacted, P1 |
| 7 | MiniMax | Peer **and Manus's own vendor** | Global, VN #1 | 23/29 ⚠️ | ⭐ High | Already outreached | ✅ Yes |
| 8 | Ahrefs | Peer | Global, SG-HQ | Not scored | 🟢 Medium | Singapore + Stripe + cards, same shape | ✅ Yes |
| 9 | Goodnotes | Peer | Global, HK-HQ | Not scored | 🟢 Medium | App-store-heavy — the IAP-split comparison | ✅ Yes |
| 10 | z.ai | Peer | Global | 23/29 ⚠️ | 🛑 Blocked | Compliance hold | ✅ Yes |

> **⭐ Manus AI is a genuine new find. I confirmed independently that `accounts/apac-tal.csv` contains no row for "Manus", "Butterfly Effect" or "Monica"** — a case-insensitive scan returned **zero** matches across all 1,219 data rows. **Genspark, Lovable, Replit, Cursor/Anysphere, Abacus AI, Perplexity and Monica are also all absent from the TAL** — the AI-agent and agentic-coding vertical is essentially unrepresented on the list, which has only 8 rows tagged `AI` and 46 tagged `SaaS`. That is a gap worth raising with whoever owns the list, independently of this account.

---

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | **US$100M ARR / US$125M total revenue run-rate** — company's own claim, Dec 2025. More recent third-party estimate: **~US$450M annualized, June 2026** `[ESTIMATE, not confirmed]` (Sacra). A separate Chinese research estimate put Oct 2025 ARR at ~US$94M `[ESTIMATE, not confirmed]`. | https://manus.im/blog/manus-100m-arr (first-party meta: *"Manus reaches $100M ARR… With $125M total revenue run-rate"*); https://sacra.com/c/manus/ |
| GMV / Gross Transaction Volume | **No public GMV data found.** Manus is not a marketplace; subscription + credit revenue is the volume. | — |
| Average Transaction Value (USD) | **Not found.** Nothing is published. Anchor points only: **Pro from US$20/month**, **17% annual discount**, Google Play IAP **$9.99–$4,999.99 per item**, credit packs **1,000–999,000 credits**, auto top-up options **$10 minimum / $100,000 maximum**. | help centre; `bizConst` in chunk `3d4s07pvglcez.js`; Google Play |
| Est. Annual Transactions | **~6.2M/year** if the average charge equals the US$20 entry price; **~2.1M/year** at a US$60 average; **~500k/year** at US$250. **All three are assumptions, not calculations**, because no ATV is sourced. | US$125M ÷ assumed ATV |
| **Monthly transaction count** | **⚠️ NOT FOUND — ASSUMED ≥100,000/month. `[ASSUMPTION — not researched.]`** **Billing unit counted: individual charges** — subscription renewals (monthly or annual) + credit-pack purchases + auto top-ups + overage, per the first-party `AgentsPlan` / `AgentsStripePriceDetails` / `BUY_PERSON_CREDITS` schema. Basis: sourced **US$125M run-rate ÷ 12 = ~US$10.4M/month**; at the sourced US$20 entry price ≈ 520,000 charges/month, at US$60 ≈ 174,000, at US$250 ≈ 42,000. **The under-40,000 rejection would need an average charge above ~US$260** and is not arithmetically reachable. **ATV is unsourced, so this is an assumption and it cannot and does not reject the account.** An unknown share also runs through Apple/Google IAP and never touches Manus's own acquirer, so the orchestratable subset is smaller. | See the disclosure block in the ICP breakdown |
| Active Customers / Users | **No paying-subscriber count found.** Proxies: Google Play **10M+ downloads** (Manus) and **10K+** (Cue); Apple **39,031 US ratings at 4.73**; company-cited **"more than 147T tokens"** and **"more than 80M virtual computers"** since launch; ~100 employees, mostly Singapore. | Google Play; `https://itunes.apple.com/lookup?id=6740909540`; https://manus.im/blog/manus-100m-arr; Wikipedia |
| **Primary Currency** | **USD — exclusively, worldwide, by stated policy.** *"All our subscription and credit prices are standardized in United States Dollars (USD)… regardless of their location."* Corroborated in their own code: the price formatter hard-codes a `$` glyph and the `en-US` locale. | https://help.manus.im/en/articles/11711125-what-is-the-pricing-unit-for-manus-globally-can-i-pay-in-local-currency ; chunk `3d4s07pvglcez.js` |
| Top 3 Markets by Revenue | **Not found.** No revenue split is published. **By traffic:** Brazil 17.76%, United States 13.25%, India 5.65%. ⚠️ Traffic is not revenue, and the aggregation across three domains (two of which resolve to redirects) means no market can be attributed to a single property. | SimilarWeb (supplied 2026-10-13) |
| **Billing channel split (web vs app store)** | **❌ NOT PUBLISHED AND NOT KNOWN. Nothing in this report asserts one.** Both channels are confirmed live: web via Stripe (Terms §3.1, `pk_live_` key, Stripe Checkout/Billing allowlist) and stores via Apple IAP (`hasInAppPurchases: true` on `tech.butterfly.app`) and Google Play ($9.99–$4,999.99 per item), synced through RevenueCat. Evidence tilting web-primary: the Terms name Stripe as *the* Payment Processor singular; the whole RPC surface is Stripe-specific; **Team, SSO, SCIM, Cloud Computer and phone numbers have no IAP plan keys at all**; the IAP schema is scoped to "resource" purchases. Evidence tilting IAP-material: price parity across web and mobile, 10M+ Android downloads, dedicated Apple/Google dunning and refund branches, and a batch refund exception Apple granted them. **This is the single number that could change the account's grade.** | Terms §3.1; App Store; Google Play; decoded `resource_iap.proto`, `agents_billing.proto`, `subscription.proto` |
| Plan structure (SOURCED) | **Free** US$0 — 300 daily refresh credits, 1 concurrent task, 2 scheduled automations. **Pro** from **US$20/month**, 17% off annually, from **4,000 credits/month**, 20 concurrent tasks. **Team.** Plus Cloud Computer (Basic/Standard/Advanced/Storage, monthly) and per-country phone numbers (13 countries, monthly). Internal plan keys show a tiered ladder `PRO_20 … PRO_20000` and `TEAM_20 … TEAM_10000` monthly and yearly, where the suffix matches the US$20 entry price `[INFERENCE, not confirmed — only the US$20 entry point and the 17% annual discount are sourced]`. | https://help.manus.im/en/articles/11711111-what-is-the-current-membership-pricing-for-manus ; decoded `Plan_Key` enum and `bizConst` |
| Recurring mechanics (SOURCED) | Billed **monthly in advance**, auto-renewing at then-current pricing (Terms §4.1); billing cycle anchored to the subscribe date and **invoice dates cannot be changed**; **credits are non-refundable and expire**, and unused credits may be forfeited on termination (§4.3); refunds non-refundable by default with a 14-day withdrawal right for EU/UK/Turkey consumers, returned to the original method in **1–15 business days** (§4.4); **sales tax collected in addition** (§3.3) via Stripe/Apple/Google. **`DISABLE_SUBSCRIPTION_RENEW` exists as a user config key.** | https://manus.im/terms ; decoded `UserClientConfigKey` enum |

---

## Overall Research Confidence

**HIGH — unusually high for this repo, and deliberately uneven.**

**Very strong coverage.** The payment stack (S3), the rail gaps (S4), the billing mechanics and billing unit (S12), the checkout architecture (S8) and the billing entity (S2) rest on **first-party evidence**: the merchant's own Terms of Use, their own help centre, their own live production configuration, their own compiled protobuf service descriptors decoded out of 22MB of shipped JavaScript, their own App Store and Play listings, and Stripe's own published eligibility documentation. Almost nothing important here depends on a press release or a search synthesis. Route findings were each checked against a deliberately nonsense control; the Apple IAP flag was paired to the subject bundleId by brace-matched object extraction with two controls that resolved correctly in both directions; the BIS check carries a passing positive control.

**Traffic data was SUPPLIED, not API-sourced and not estimated** — `accounts/traffic/manus-ai.md`, SimilarWeb, Jul–Sep 2026, used verbatim per the method's resolution order. That makes the country profile, the APM gap analysis and two ICP signals as reliable as the supplied extract. Two caveats carry through: it gives **no absolute visit counts** (so none is stated), and it **aggregates three domains of which two resolve to redirects to `manus.im`**, so no single market may be attributed to a specific property.

**Weaker coverage, named honestly:**
- **The web-versus-app-store split is unknown.** This is the one gap that could change the grade.
- **The live geo-rendered checkout method set was not observed.** Pix and UPI are reachable on a Singapore Stripe account, so if they have been quietly enabled since the April 2026 help-centre update, two rows in Section 4 would be wrong. The other eight rail gaps are blocked at the PSP level and are not exposed to that risk.
- **ACRA registration is aggregator-sourced only** and does not mention Manus.
- **No live APAC regulatory source was verified**, so no regulatory acquiring gate is asserted anywhere in this file — the PSP-level gate from Stripe's documentation is used in its place.
- **Compliance screening is partial.** BIS Federal Register only. OFAC, DoD 1260H and the Denied Persons List were not checked.
- **Section 11 competitor scoring is thin** for Genspark, Lovable and Replit; their rows are floors, not scores.
- **Trustpilot was fetched through WebFetch after a 403 to direct `curl`**; the ratings and quotes come from the rendered page, but individual reviews remain unverified customer accounts.

**Method deviation, disclosed as instructed.** The Agent/Task tool was **not available**, so Phases 1→2→3 were executed single-threaded by one analyst, treating the five per-agent budgets as per-workstream totals. In practice the mix shifted sharply toward first-party technical work — bundle decompilation, protobuf descriptor decoding, controlled route probing, store-metadata pairing — and away from web search, which is why the evidence base is stronger than a search-led run would have produced, and why Section 11's competitor coverage is weaker.

---

## Manual Research Recommendations

> **Area:** **Monthly transaction count, and the web-versus-app-store split.** (S12, and the ICP row that carries the tier)
> **Why it matters:** The transaction count is the only ICP signal that can reject an account, and here it is **assumed, not sourced**. The app-store split is the one fact that could trigger the subscription-reference §4 override and invalidate the whole account.
> **Suggested manual action:** Ask both on the first call: "roughly how many billing events a month across subscriptions, credit packs and top-ups?" and "what share of that runs through Apple and Google versus your own checkout?" Do not build a business case before both are answered.

> **Area:** **Whether Pix and UPI are actually enabled in their Stripe Dashboard.** (S4)
> **Why it matters:** These are the only two rail gaps in the top three markets that are a configuration choice rather than a PSP limit. If Pix is already live, Insight #1 needs rewriting around boleto and BRL presentment alone — which is still strong, but different.
> **Suggested manual action:** VPN into Brazil and India, start a Pro monthly purchase with DevTools open, and screenshot the Stripe Checkout method list, the presentment currency and the descriptor. This is the highest-value hour anyone can spend on this account.

> **Area:** **ACRA verification of Butterfly Effect Pte. Ltd.** (S2)
> **Why it matters:** The billing entity is confirmed from the Terms and from Apple, but UEN **202330764R** comes from third-party aggregators that never mention Manus. Getting the entity wrong in a commercial conversation is an avoidable own goal.
> **Suggested manual action:** Pull the BizFile+ business profile (paid) and confirm the UEN, officers and shareholding chain, including whether a Cayman parent sits above it.

> **Area:** **Involuntary churn and renewal recovery.** (S5, S7, S8)
> **Why it matters:** Their Terms say a failed automatic bill becomes a manual invoice, and their help centre says they do not receive decline reasons. If first-renewal failure rates are as high as that implies, it is the entire business case on its own.
> **Suggested manual action:** Use the §5 discovery questions from `subscription-payments.md` verbatim: what share of renewals fail on first attempt, what share recover, is the first-renewal cliff visible in cohort data, are network tokens live, and how is India recurring handled today. Do not assert a benchmark; earn the number.

> **Area:** **The agentic-payments roadmap (`StripeLinkService`).** (S1 buying signals)
> **Why it matters:** They are building agent-initiated payments to third-party merchants, with `payment_failure_code`, `network_id` and `credential_type` on every bill. That is a second, strategically important payments surface and potentially a much larger conversation than subscription billing — and it may also mean a payments-adjacent product team already exists internally.
> **Suggested manual action:** Find the owner of that surface on LinkedIn before picking the contact. The right first meeting may be about agentic commerce rather than about renewals.

> **Area:** **Compliance screening beyond BIS.** (S6)
> **Why it matters:** The z.ai precedent in this repo shows how late a compliance blocker can surface. Manus is clean on BIS Federal Register with a passing control, but OFAC, DoD 1260H and the Denied Persons List were not checked, and public reporting references a US Treasury OISP question around the Benchmark investment.
> **Suggested manual action:** Run the standard screen through Yuno legal before a contract conversation, not before a discovery call. **This is not a reason to delay outreach — it is a reason not to be surprised later.**

> **Area:** **A missing vertical on the target account list.** (S11)
> **Why it matters:** The TAL has no row for Manus, Butterfly Effect, Monica, Genspark, Lovable, Replit, Cursor, Abacus AI or Perplexity, and only 8 rows tagged `AI` in 1,219. The agentic-AI vertical — global by default, USD-priced by default, single-PSP by default — is close to the ideal orchestration profile and is essentially unrepresented.
> **Suggested manual action:** Raise the gap with whoever owns `apac-tal.csv` and propose a batch add. Start with Kling AI, which internal research already scores 23/29 as greenfield single-PSP Stripe and which is the closest structural twin to this account.

---

## Appendix: All Source URLs

**Supplied data**
- `accounts/traffic/manus-ai.md` — SimilarWeb, supplied by Prateek 2026-10-13, Jul–Sep 2026
- `accounts/apac-tal.csv` — target account list (**no Manus / Butterfly Effect / Monica row**; peer rows for Kling AI, Moonshot AI, MiniMax, z.ai, Ahrefs, Goodnotes, Kuaishou)
- `2-ready-to-outreach/z-ai.md`, `3-outreached/minimax-io.md` — internal prior research

**First-party — Manus / Butterfly Effect**
- https://manus.im/ — homepage; `globalThis.__manus_env__` with `stripePublicKey` = `pk_live_…` **[live key present — value deliberately not recorded]**; Sentry at `sentry.prod.ops.butterfly-effect.dev`
- https://manus.im/pricing — real page, client-rendered (710 chars of text; `BAILOUT_TO_CLIENT_SIDE_RENDERING`)
- https://manus.im/terms — Terms of Use, last updated 28 Sep 2026 (§3.1 Stripe sole Payment Processor; §3.2 Payment and Order Processing; §3.3 Taxes; §4.1 Subscription Management; §4.2 Billing and Fee Changes; §4.3 Credits; §4.4 Refund Policy; §12 Governing Law / SIAC Singapore; Apple third-party-beneficiary clauses)
- https://manus.im/privacy — Privacy Policy (client-rendered)
- **https://manus.im/claim-refund** — live manual-refund submission page (HTTP 200, 176,711 bytes, `<title>Provide your refund details - Manus</title>`)
- https://manus.im/blog/manus-100m-arr — *"Manus reaches $100M ARR… With $125M total revenue run-rate"*
- https://careers.manus.im/ — careers SPA (`/api/trpc/hr`; `hiring@manus.ai`); no payment/billing role found
- Production JavaScript on `https://files.manuscdn.com/webapp/_next/static/chunks/` — 69 chunks, ~22MB, scanned in full:
  - `3okoj2tnxlwg5.js` — `validateStripeCheckoutUrl` / `redirectToStripeCheckout` with the `["checkout.stripe.com","billing.stripe.com"]` allowlist; `SubscriptionService`, `StripeLinkService`, `PromotionService`, `RefundPayoutService`; decoded `userdump/v1/userdump_refund_payout.proto`, `agents/v1/stripe_link.proto`, `promotion/v1/promotion.proto`, `cloud_pc/v1/cloud_pc.proto`
  - `3-xpy7erphbc6.js` — decoded `user/v1/subscription.proto` (Plan_Key enum, `RevenuecatSyncCustomer`, `RecoveryRefund`, all Stripe\* RPCs), `user/v1/agents_billing.proto` (`AgentsPlan`, `AgentsStripePriceDetails`, `CreateAgentsStripeCheckout`), `user/v1/resource_iap.proto`, `user/v1/agents_invoice.proto`
  - `3d4s07pvglcez.js` — `PaymentPlatform = { apple, googlePlay, liveEvent }`, `isStripePlatform()`, `getPaymentPlatformName()`, `PAYMENT_PLATFORM_DISPLAY_MAP = { google_play: "Android app", apple: "iOS app" }`, `getAnnualDiscountPercent() → 17`, `BUY_PERSON_CREDITS`, `USER_AUTO_TOPUP_OPTIONS`, `PERSONAL_AUTO_TOPUP_LIMITS`, `PRO_20…PRO_20000` / `TEAM_20…TEAM_10000` plan configs, `FREE_VIDEO_MODEL: "minimax-h3"`, the hard-coded `$` + `en-US` price formatter
  - `30_trvxj7u1af.js` — the Terms of Use body (Notion export)
- `https://api.manus.im/user.v1.SubscriptionService/GetAgentsSubscriptionPlans` → **401 `{"code":"unauthenticated","message":"missing authorization header"}`**, against a 404 control on a bogus method — confirming the service and method exist and are auth-gated

**First-party — help centre (`help.manus.im`)**
- /en/articles/11711125-… — USD-only global pricing (2026-02-27)
- /en/articles/11813666-… — accepted payment methods incl. PayNow Singapore (2026-04-29)
- /en/articles/11711111-… — Free / Pro from $20 / Team, 17% annual discount, 4,000 credits
- /en/articles/11711093-… — *"We typically don't receive detailed decline reasons from banks"*; international blocks; third-party-payment prohibition (2025-12-05)
- /en/articles/11985185-… — past-due handling, Stripe vs App Store branches (2026-03-11)
- /en/articles/11813620-… — *"our payment processors (Stripe, Apple, Google)"*; web/mobile price parity; FX and foreign-transaction fees (2025-12-15)
- /en/articles/11813630-… — changing payment method via "Edit billing" (2026-01-23)
- /en/articles/11711102-… — refunds by channel; Alipay 90-day limit citing Stripe's Alipay docs; Apple refunds via Apple; Cue phone numbers
- /en/articles/11711089-… — invoices emailed, fixed billing cycles, no invoice modification (2025-12-15)
- /en/articles/11711819-… — where Privacy Policy and Terms live (2025-12-04)
- /en/articles/16147909-… — **Service Change refunds**: Aug 11 notification, Aug 23–25 deletion, platform-specific routing, expired-card manual path, `/claim-refund`, ~3 weeks (2026-09-02)
- /en/collections/13760762-billing · /en/collections/19704025-data-back-up-and-restoration

**App stores**
- https://apps.apple.com/us/app/manus-ai-agent-automation/id6740909540 — `hasInAppPurchases: true` paired to `tech.butterfly.app`; controls `com.granola.ios-prod` → false, `im.monica.app.monica` → true
- https://itunes.apple.com/lookup?id=6740909540 — seller BUTTERFLY EFFECT PTE. LTD.; v26.18.1 released 2026-10-12; first released 2025-03-27; 4.73 / 39,031 US ratings
- https://itunes.apple.com/lookup?id=6808613358 — **Cue by Manus**, `ai.manus.agents`, released **2026-10-08**, same seller
- https://itunes.apple.com/lookup?id=6450770590 — **Monica**, `im.monica.app.monica`, same seller, released 2023-07-09
- https://play.google.com/store/apps/details?id=tech.butterfly.app — 10M+ downloads; IAP **$9.99–$4,999.99 per item** (neighbour ranges for `com.anthropic.claude`, `com.foyer.merlin`, `com.connectinno.chataiultraapp` discarded)
- https://play.google.com/store/apps/details?id=ai.manus.agents — 10K+ downloads; IAP $9.99–$1,999.99 per item

**Stripe documentation (used for account-country eligibility, never for what Manus has enabled)**
- https://docs.stripe.com/payments/pix — business locations include **SG**; presentment **BRL**; **3.5% IOF**, customer pays by default; Ebanx descriptor; US$3,000 per payment, US$10,000 per customer per month; Pix Automático required for Checkout subscription mode
- https://docs.stripe.com/payments/boleto — **business location BR only**; **✗ crossborder**; presentment BRL
- https://docs.stripe.com/payments/payment-methods/payment-method-support — UPI (INR, business locations incl. **SG**, customers IN) · Konbini (JPY, **JP** only) · PayPay (JPY, **JP** only) · PromptPay (THB, **TH** only) · PayNow (SGD, **SG** only) · GrabPay (MYR/SGD, MY/SG). **No row for Fawry, mada, MoMo, ZaloPay, VNPay, JKOPay, LINE Pay, KakaoPay, Naver Pay or Toss** — verified with GrabPay and PayNow as positive controls

**Corporate, funding and press**
- https://techcrunch.com/2026/10/08/chinas-manus-raises-over-500m-in-first-funding-round-since-split-with-meta/ — fetched and read: >US$500M, 2026-10-08, Boyu + IDG led, Tencent/HSG/ZhenFund participating, valuation undisclosed and unconfirmed, Meta Dec 2025 → blocked Apr 2026 → independent Aug 2026 with user-data deletion
- https://www.cnbc.com/2026/10/08/manus-fund-raise-meta-muse-tencent.html — **HTTP 403, not read**
- https://en.wikipedia.org/wiki/Manus_(AI_agent) — relocation, corporate structure, Meta timeline (NDRC 2026-04-27; Meta cut ties 2026-06-15; independent 2026-08-11), Monica 2023
- https://www.malaymail.com/news/singapore/2025/07/10/china-born-ai-firm-manus-moves-hq-to-singapore-amid-scrutiny-over-us-chip-curbs-national-security-review/183448 — Zhang Tao, SuperAI Singapore, 2025-06-18
- https://techcrunch.com/2025/04/25/chinese-ai-startup-manus-reportedly-gets-funding-from-benchmark-at-500m-valuation/ and https://siliconangle.com/2025/04/25/chinese-startup-behind-manus-reportedly-raises-75m-funding/ — ~US$75M, Benchmark-led, ~US$500M valuation, Bloomberg-sourced
- https://sacra.com/c/manus/ — ~US$450M annualized, June 2026 `[ESTIMATE, not confirmed]`
- https://companieshouse.sg/butterfly-effect-pte-ltd — UEN 202330764R, inc. 02 Aug 2023, Funan 109 North Bridge Road #06-W112 ⚠️ **aggregator, not ACRA; does not mention Manus**

**Complaints**
- https://www.trustpilot.com/review/manus.im — 1.2/5, 214 reviews, 95% one-star; dated payment complaints Apr–Oct 2026 (GB, US, VN, SG, TR, GR). Direct `curl` returned **403**; read via WebFetch.

**Compliance**
- `https://www.federalregister.gov/api/v1/documents.json?conditions[term]="Butterfly Effect"&conditions[agencies][]=industry-and-security-bureau` → **count 0**
- same query for `"Manus"` → **count 0**
- same query for `"Zhipu"` → **count 1** (*Addition of Entities to and Revision of Entry on the Entity List*, 2025-01-16) — **positive control, passes**
- `https://www.ecfr.gov/api/versioner/v1/full/2026-09-01/title-15.xml?part=744` → **HTTP 403 at the egress proxy; download unusable** (confirmed by a control grep finding neither "Huawei" nor "Zhipu")

</details>
