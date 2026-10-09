# OneDegree

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 13 / 29 → 🟢 **Medium**
**Industry:** Insurance — Hong Kong virtual (digital) general insurer · **HQ:** Hong Kong (OneDegree Hong Kong Limited) · **Researched:** 2026-10-09 · **First email sent:** —
**Motion:** ✅ **GREENFIELD** — three payment providers across two unconnected stacks, no orchestration or routing layer found.

---

> ## 🔑 HEADLINE — the PSP question is answered, first-hand, and the answer is three providers on two stacks
>
> The brief flagged PSP identification as the biggest open question. It is now closed, from OneDegree's own live assets.
>
> **1. Adyen is live on the insurance flow.** The inline config block served on every `onedegree.hk` page carries, verbatim:
>
> ```
> var ADYEN_CLIENT_KEY='live_DDIKN53C5NDCNCIVW7IQTQB76Y6XYR47';
> var ADYEN_ENVIRONMENT='live-apse';
> var ADYEN_APPLEPAY_MERCHANT_NAME='OneDegree';
> var ADYEN_APPLEPAY_MERCHANT_ID='000000000580332';
> ```
>
> A **`live_` client key**, not test. `live-apse` is Adyen's **live Asia-Pacific South-East region** endpoint — the account is provisioned in APAC, not EU/US. Apple Pay runs through Adyen on an Adyen-issued merchant identifier. Corroborated independently by the CSP response header, where `*.adyen.com` appears in **both `connect-src` and `frame-src`** and is the **only** payment-processor domain present. Re-verified on a second cache-busted fetch.
> Source: `https://www.onedegree.hk/en-us/faq` (and every other page on the domain), fetched 2026-10-09.
>
> **2. Stripe is named by OneDegree itself — in the card-vault clause.** From their own Terms of Use, verbatim:
>
> > *"By consenting to the credit card information storage service, you agree that OneDegree may share information regarding your device, payment, location, and account with **Stripe and/or Adyen** (''Designated Payment Gateway'')."*
>
> Source: `https://www.onedegree.hk/en-us/terms-of-use` · repeated at `https://www.onedegree.hk/en-us/privacy-policy`
>
> **"and/or" is doing a lot of work, and it sits specifically on the stored-credential service** — the vault that carries every auto-renewal. Stripe appears nowhere in the CSP, so it is **not browser-facing**: consistent with legacy stored credentials, or a server-to-server integration, or a migration that is partly done. **Which of those it is, is the single best discovery question on this account.**
>
> **3. Pet Mart runs Shopify Payments — a completely separate stack.** See the Pet Mart block below.
>
> **No orchestrator.** No Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails or Yuno signature in the CSP, in any page bundle, or in search. `od-finance-checkout-prod-as.azurewebsites.net` in `connect-src` shows they built their **own** checkout service on Azure — but nothing evidences that it routes, cascades or fails over. Classified **greenfield**, with that caveat recorded.

---

> ## 🐾 PET MART IS A SECOND STACK — confirmed, and it is a different PSP, a different brand set and a different checkout
>
> The brief called this "a genuinely promising thread nobody has pulled." It is real.
>
> `store.onedegree.hk` is a **Shopify** store — `powered-by: Shopify`, `_shopify_essential` cookies, `cdn.shopify.com`, `shopify-complexity-score`. Internal shop `afhvbb-ze.myshopify.com`, shopId `67774218378`. **Merchant of record: "OneDegree Hong Kong Limited"** — the same licensed insurance entity. Pet Mart card volume lands on the same company.
>
> From the live public config at `https://store.onedegree.hk/payments/config` and the UCP manifest at `https://store.onedegree.hk/.well-known/ucp`:
>
> | | **Insurance** (`onedegree.hk`) | **Pet Mart** (`store.onedegree.hk`) |
> |---|---|---|
> | Platform | own Next.js + Azure checkout service | **Shopify** |
> | Processor | **Adyen** (`live-apse`) + **Stripe** named in T&Cs | **Shopify Payments** (`shopifyPaymentsEnabled:true`) |
> | Card brands | Visa, Mastercard, **Amex, JCB, UnionPay** + debit | Visa, Mastercard, Amex, **Discover, Diners** |
> | **UnionPay** | ✅ accepted | ❌ **not enabled** |
> | **JCB** | ✅ accepted | ❌ **not enabled** |
> | Apple Pay | ✅ via Adyen | ✅ via Shopify (Visa/MC only) |
> | **Google Pay** | ❌ not found | ✅ **live** (`environment: PRODUCTION`) |
> | Transaction type | recurring premium (MIT, card-on-file) | one-off physical goods |
> | Ships to | n/a | **`allowedCountryCodes: ["HK"]`** |
>
> **Two findings fall straight out of this table:**
>
> 1. **The brand sets are inconsistent in the wrong direction.** The insurance book accepts **UnionPay and JCB**; the pet store does not — but it does enable **Discover and Diners Club**, which is the stock Shopify Payments default. In Hong Kong that is backwards: a market-default brand set was shipped unadjusted, and the two properties under one entity now disagree about which cards a OneDegree customer may use.
> 2. **Google Pay exists on one stack and not the other.** Live and in production on Pet Mart; no Google Pay string, config or CSP entry anywhere on the insurance domain.
>
> Pet Mart also appears to be **partly a marketplace**: its own terms say *"Customers agree to allow OneDegree to share their contact details with merchants for third-party logistics arrangements"*, against a business-overview claim of *"over 100 leading pet brands"* in the network. OneDegree is merchant of record while settling third-party merchants — a split-payout shape. `[INFERENCE, not confirmed]` — the settlement mechanics are not published.
> Sources: `https://store.onedegree.hk/policies/terms-of-service` · `https://www.onedegree.hk/en-us/business-overview`
>
> The privacy policy independently confirms the store is theirs: *"processing purchase orders through our e-shop"* (`https://www.onedegree.hk/en-us/privacy-policy`).

---

> ## 🎯 THE LIVE ANGLE — OneDegree publishes its own dunning logic, and it is a fixed every-3-days retry
>
> This is the strongest hook on the account and it is **not an inference**. From OneDegree's own FAQ, verbatim:
>
> > **"Why was my payment declined?"** … *"If a payment is declined and the policy enters the grace period, **the system will attempt to deduct the payment every three days until the grace period ends.**"*
> > Source: `https://www.onedegree.hk/en-us/faq/article/why-was-my-payment-declined` (via `https://www.onedegree.hk/en-us/faq/tag/billing-and-payment`)
>
> > **"What would happen if I miss a premium payment?"** … *"During the grace period, the system will attempt to process the payment every 3 days. … the policy will be terminated if we still do not receive the overdue premium after the grace period ends. The Fire insurance policy will be automatically renewed 20 days before the next policy effective date. If the premium is not successfully deducted before the next policy effective date, the policy will be automatically terminated. \* The grace period for Pet insurance, Turtle, Tortoise & Bird Insurance, and Critical Illness insurance is **30 days**. The grace period for Home insurance and Home Appliances Warranty insurance is **7 days**."*
> > Source: `https://www.onedegree.hk/en-us/faq/article/what-would-happen-if-i-miss-a-premium-payment`
>
> **What this gives us, sourced:**
>
> | Product | Grace period | Max retry attempts at 3-day cadence |
> |---|---|---|
> | Pet / Turtle-Tortoise-Bird / Critical Illness | 30 days | ~10 |
> | Home insurance / Home Appliances Warranty | 7 days | ~2 |
> | **Fire** | none — auto-renew attempted 20 days ahead, **terminate if not collected by effective date** | effectively a single window |
>
> **A fixed 3-day cadence is a fixed schedule.** It is identical whether the decline was "insufficient funds" (retry later, likely to recover), "card expired" (retry never recovers — the credential must be refreshed) or "do not honour" (retry is counterproductive). `subscription-payments.md` §2 contrasts exactly this with *"retry logic informed by decline code and issuer."*
>
> **And every remedy they publish is customer-initiated.** Also verbatim from the decline FAQ: expired/incorrect card → *"You can log in to your account and add another payment card"*; insufficient credit limit → *"Please contact your card issuing bank"*; declined → *"Please contact your card issuing bank to approve the transaction."* The dashboard carries a matching hard-coded state, `"Transaction failed. Please change your credit card."`, and an expired-card string, `"Your card is expired. Please pay with an alternative card."`
>
> 🔑 **There is no account updater and no network-token refresh anywhere in the published flow.** A reissued or expired card is handled by asking the customer to go and type a new one in. `[INFERENCE, not confirmed]` — absence of a public statement is not proof of absence in the backend, and this is a discovery question, not an email claim. But the customer-facing remedy for a reissued card is unambiguous.
>
> **Two more sourced frictions:**
> - **The debit date cannot be moved.** *"No, unfortunately the payment debit date can't be changed."* No dunning-date optimisation is possible for a customer whose salary lands after their debit date.
> - **The billing cycle only changes at renewal.** *"You can change your billing cycle only when you renew your policy. The new premium billing option will be effective in the next policy year."* The monthly-vs-annual mix therefore moves at most once per policy-year — it is a sticky, slow-moving number.
>
> **And OneDegree absorbs the full cost of acceptance.** *"No, we don't charge any payment transaction fees. The amount debited should be exactly the same as the amount shown at checkout."* Every basis point of interchange, scheme fee and acquirer margin is a OneDegree P&L line, not a customer pass-through.

---

> ## ⚠️ TWO STUB NOTES ARE DISPROVEN — correct the record before using this file
>
> **1. ❌ "~$30M est. revenue" is wrong.** The statutory filing gives FY2025 **gross premiums of HK$331,910 thousand = HK$331.91M ≈ US$42.3M–42.8M** (HKD peg band 7.75–7.85). Independently corroborated twice: OneDegree's FY2025 results as reported by HK01 on 2026-01-19 give **revenue up 38% to HK$330 million**, and the Alibaba Entrepreneurs Fund wrote in April 2025 that **2024 revenue surpassed HK$240 million** — HK$240M → HK$330M is **+37.5%**, matching the stated +38%. The TAL understated the account by roughly 40%.
> ⚠️ Note that the publicly reported "revenue" (HK$330M) sits within 0.6% of statutory **gross** premiums (HK$331.91M), not net. **Net premium is only HK$59.75M** — 82.0% is ceded to reinsurance. Sizing this account off net premium would understate the card volume by **5.56×**. The cardholder pays gross; reinsurance changes who carries the risk, not who swipes.
>
> **2. ❌ "unlikely to clear 40,000 transactions/month" is unsupported.** Monthly billing carries **zero surcharge** — HK$222/mo × 12 = HK$2,664/yr exactly — and the gate clears above roughly **one-third monthly-billing adoption** (25.9%–35.6% depending on the policy-count assumption). On a discretionary consumer purchase with no penalty for spreading the cost, and 72.24% mobile-web traffic, that threshold is not a stretch. The figure remains **ASSUMED** and is labelled as such throughout — see Section 12.
>
> **New this run:** the multiplier's *structure* is no longer assumed. OneDegree's live pet-plan catalogue, embedded in `https://www.onedegree.hk/en-us/pet-insurance`, contains 18 `plan_payment_modes` objects across **9 plans** — and **every single plan** offers exactly two modes:
> `{"installment_count":1,"down_payment_count":1,"is_refundable":true,"payment_period":{"name":"Annual"}}` and
> `{"installment_count":12,"down_payment_count":1,"is_refundable":false,"payment_period":{"name":"Monthly"}}`.
> **9 of 9 plans carry `"is_auto_renewable":true`. Zero carry `false`.** So: a monthly policy is **12 card charges per policy-year**, an annual policy is **1**, and *every* policy generates at least one card-on-file renewal charge. The `P × (1 + 11m) / 12` formula is now structurally sourced. Only **m** — the adoption share — remains unsourced, and it is the one load-bearing unknown on this account.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** OneDegree Hong Kong Limited is Hong Kong's first virtual (digital-only) general insurer, authorised by the Insurance Authority in April 2020. It sells pet, home, home-appliance-warranty, fire and critical-illness cover direct to consumers online, plus professional indemnity, D&O, digital-asset insurance and cybersecurity services to businesses. It is the leading pet insurance brand in Hong Kong, reported its first full-year profit in 2025 — the first of the city's four virtual insurers to do so — and runs two adjacent non-insurance properties: the **PawBook®** pet-health app and the **OneDegree Pet Mart®** e-commerce store.

**SimilarWeb total visits (last full month):** **58,657** (Sep 2026) — ▼ **34.20%** MoM — *source: supplied by Prateek, SimilarWeb (supplied 2026-10-09). Not re-researched.*

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇭🇰 **Hong Kong** | **76.90%** | **Insurance:** Visa, Mastercard, Amex, JCB, UnionPay credit + debit cards; Apple Pay. **Pet Mart:** Visa, Mastercard, Amex, Discover, Diners + Apple Pay + Google Pay | **FPS**, PayMe, Octopus, AlipayHK, WeChat Pay HK — absent from **both** stacks. UnionPay + JCB absent from Pet Mart only | ✅ **OneDegree Hong Kong Limited** |
| 2 | 🇺🇸 United States | 4.67% | — not a selling market — | n/a | ❌ none found |
| 3 | 🇹🇼 **Taiwan** | **4.24%** | — not a selling market — | n/a | ⚠️ group tech/security presence referenced (Taipei role advertised); no selling entity found |
| 4 | 🇦🇺 **Australia** | **4.03%** | — not a selling market — | n/a | ❌ none found |
| 5 | 🇸🇬 **Singapore** | **2.69%** | — not a selling market — | n/a | ⚠️ **OneDegree Global (SG) Pte. Ltd.** referenced (B2B tech/security sister company, not a consumer insurer) |

> ⚠️ **Read this table with the HK-only caveat.** OneDegree holds a **Hong Kong** virtual insurer licence and nothing else; Pet Mart ships to **`["HK"]`** only, per its own live Shopify config. The non-HK traffic — 23.1% of visits across the US, Taiwan, Australia, Singapore, the UK, Canada, Japan and the Netherlands — is **almost certainly not transacting**. It is most plausibly research, diaspora browsing, press and bot traffic. **This is not international reach and must not be pitched as such.** It is scored at zero accordingly.

### Legal entities
- **OneDegree Hong Kong Limited** (Hong Kong) — the licensed insurer. Virtual insurance licence from the Insurance Authority, **April 2020**. Registration number **not found** (no free Companies Registry / IA register lookup was reachable in this environment). Source: `https://www.onedegree.hk/en-us/business-overview`
- **Parent: AI Financial Technology Holding Company ("AIFT")** — *"OneDegree Hong Kong Limited (OneDegree) is a wholly owned subsidiary of the internationally leading technology company AI Financial Technology Holding Company (AIFT)."* Source: `https://www.onedegree.hk/en-us/business-overview`
  ⚠️ **Discrepancy, both from OneDegree's own site:** an earlier release describes OneDegree HK as *"a subsidiary of OneDegree Group"* (`https://www.onedegree.hk/en-us/news/ODHK-5anniversary-en`). Most consistent with a group rename to AIFT rather than a change of control, but that is `[INFERENCE, not confirmed]`.
- **OneDegree Global (SG) Pte. Ltd.** (Singapore) — sister company, enterprise insurance core system and cyber security; named as the ISO 27001 holder. `[UNVERIFIED — search summary only, page not fetched]` (InvestHK client profile, dated 2021).
- **OneDegree Middle East** — referenced in OneDegree's own newsroom: *"OneDegree Group announced two key appointments to OneDegree Global and OneDegree Middle East"* (2024-01-08, `https://www.onedegree.hk/en-us/press`). **EMEA — out of territory.**
- Sibling AIFT businesses: **OneInfinity** (digital-asset insurance brand; `oneinfinity.global`) and **Vulcan** (generative-AI protection / red-teaming). Source: `https://www.onedegree.hk/en-us/business-overview`

### Known PSPs
- **Adyen** — `[Source Code]` + `[Checkout]` + CSP header. `ADYEN_CLIENT_KEY='live_…'`, `ADYEN_ENVIRONMENT='live-apse'`, Apple Pay merchant ID `000000000580332`; `*.adyen.com` in `connect-src` and `frame-src`. Market: Hong Kong (insurance). Source: `https://www.onedegree.hk/en-us/faq`
- **Stripe** — `[Terms/Privacy Policy]`. Named by OneDegree as a "Designated Payment Gateway" for the card-storage service, alongside Adyen. **Not browser-facing** — absent from the CSP. Source: `https://www.onedegree.hk/en-us/terms-of-use`
- **Shopify Payments** — `[Source Code]` + `[Checkout]`. `"shopifyPaymentsEnabled":true` on the Pet Mart store. Market: Hong Kong (e-commerce). Source: `https://store.onedegree.hk/payments/config`

### Orchestration status
**None detected — direct PSP integrations only.** No orchestrator domain appears in the `onedegree.hk` CSP (which is exhaustive and names Adyen as the sole payment processor), in any fetched page bundle, in the Pet Mart Shopify or UCP configs, or in targeted search for Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails or Yuno.

⚠️ **Caveat, recorded honestly:** OneDegree runs its **own** checkout backend — `od-finance-checkout-prod-as.azurewebsites.net` appears in `connect-src` (alongside dev/sit/uat/dr variants, i.e. a full in-house deployment pipeline). With **two card providers named in their own T&Cs**, that service plausibly holds provider-selection logic. **No evidence was found that it routes, cascades or fails over** — so the classification stays *greenfield* rather than *in-house orchestration layer*. If discovery reveals routing logic in that service, this row drops from **+4 to +1** and the score from **13 to 10**. Flag it on the first call.

### Buying signals
- 💼 **New CEO, 2026-07-13 — the most recent corporate event.** Emily Chow promoted from Deputy Chief Executive to **Chief Executive and Executive Director, with immediate effect**. The release frames the outgoing four-year tenure as delivering *"over Sixfold Revenue Growth & Full-Year Profitability."* A CEO transition three months before outreach is a live window for infrastructure review. `https://www.onedegree.hk/en-us/press`
- 🚀 **Stated plan to double total revenue within 5 years**, with explicit cross-sell of fire and home cover into the pet book — i.e. more policies per customer, so more card charges per customer. Emily Chow, via HK01, 2026-01-19. `https://www.hk01.com/財經快訊/60314167/`
- 💰 **First full-year profit in 2025** (seven-figure HKD) against a ~HK$40M loss in 2024, on revenue up 38% to HK$330M. Cost discipline is on the agenda — and acceptance cost is an uncontested P&L line they currently absorb in full. `https://www.hk01.com/財經快訊/60314167/`
- 🤝 **Non-insurance revenue is being actively expanded** — pet retail (Pet Mart) and pet-district merchant partnerships named as growth businesses, with *"over 100 leading pet brands"* in the network. That is net-new card acceptance on a second stack. `https://www.onedegree.hk/en-us/business-overview`
- 📋 **They say themselves they intend to add payment methods:** *"We will continue to introduce more payment methods to provide you with additional options that meet your needs."* FAQ last published **2026-09-04** — five weeks before this report. `https://www.onedegree.hk/en-us/faq/article/what-payment-methods-do-you-accept`
- ❌ **No public payment-related RFP found. No payment-engineering job postings found.**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach onedegree` to draft the 12-touch sequence, or call this from `/prepare_batch`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 13 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+3** | ⚠️ **NOT FOUND — ASSUMED ~56,000/month. `[ASSUMPTION — not researched.]`** Basis: ~124,591 policies (HK$331.91M GWP ÷ HK$2,664 list annual premium) × (1 + 11×0.40) ÷ 12, at an assumed 40% monthly-billing adoption. Billing unit counted: **premium collection events (card charges)** — not visits, not policies, not claims. Band 50,000–99,999 → **+3**. **An assumed figure never fires the under-40,000 rejection.** Breakeven against the 40,000 gate is **25.9%–35.6%** monthly adoption depending on policy count. See Section 12. |
| Orchestration status | **+4** | ✅ **None detected — direct PSP integrations only (greenfield).** Adyen live + Stripe named in T&Cs + Shopify Payments, with no orchestrator signature in the CSP, bundles, store configs or search. ⚠️ Conditional: an in-house Azure checkout service exists; if it proves to hold routing logic this becomes +1. |
| 3+ countries | **0** | ⬜ **Uncertain → 0, and stated deliberately.** The literal rule is met — 8 countries exceed 1% traffic share (HK 76.90%, US 4.67%, TW 4.24%, AU 4.03%, SG 2.69%, UK 2.64%, CA 2.55%, JP 1.09%) — **and I am declining to award it.** Sourced evidence affirmatively contradicts the signal this row proxies: a Hong Kong-only insurance licence, and Pet Mart's own live config restricting shipping to `allowedCountryCodes: ["HK"]`. Non-HK traffic is not transacting. Awarding +3 here would be exactly the false positive the analyst-override rules warn about. **Had the literal branch been taken, the score would be 16/29 — still 🟢 Medium.** |
| Multiple PSPs | **+3** | ✅ **Verified — three providers.** Adyen (`live_` client key + `live-apse` + CSP, `https://www.onedegree.hk/en-us/faq`); Stripe (OneDegree's own Terms of Use, `https://www.onedegree.hk/en-us/terms-of-use`); Shopify Payments (`"shopifyPaymentsEnabled":true`, `https://store.onedegree.hk/payments/config`). |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Verified — FPS is absent from both stacks in the #1 traffic market (HK, 76.90%).** *Absence sourced:* OneDegree's payment-methods FAQ (last published **2026-09-04**) enumerates cards and debit cards only; Pet Mart's UCP manifest enumerates card brands + Apple Pay + Google Pay only. *Prominence sourced:* HKMA inSight 2024-03-27 — FPS registrations **13.6 million at end-2023** against a 7.5 million population, **1.25 million transactions/day**, HK$9.0bn average daily HKD value, and *"more than 90% of Government departments accept the FPS."* Codapay's Hong Kong guide puts A2A at **~64% of transaction volume** and, in its own book (1 Oct 2024–30 Sep 2025), **FPS 61% vs cards 34%**. ⚠️ See the honest qualification in Section 4 — FPS is a push rail and is **not** a drop-in substitute for card-on-file recurring debits. |
| Recent expansion | **0** | ⬜ **No market expansion confirmed inside the 12 months to 2026-10-09.** Pet Mart and PawBook launched around the April 2025 fifth anniversary (~18 months prior). Digital-asset overseas expansion is reported for FY2025 activity and sits on the group/OneInfinity line, not the HK insurance book. |
| Payment issues | **0** | ⬜ **No payment complaints found.** Reddit, Trustpilot, X, app-store reviews and Chinese-language HK searches returned nothing on OneDegree. ⚠️ Note the distinction: OneDegree publishes extensive decline-handling *machinery* (a declines FAQ, a 3-day retry cadence, a duplicate-charge FAQ, a dashboard failure state). That is evidence of the **mechanism**, not of complaint **frequency**, and this row requires frequency. Scored 0. |
| Funding >$10M | **0** | ❌ **Not met.** Series B closed at **US$55M in 2023** (second tranche on top of ~US$28M raised 2021). AIFT reports *"over US$100 million capital in total"* by 2026 — cumulative, not a round. No round inside the last 12 months. |
| High traffic outside home | **0** | ❌ **Not met.** Hong Kong is **76.90%** of traffic, well above the 60% home-market threshold. |
| Competitor using orchestration | **0** | ⬜ **None found.** No Hong Kong virtual insurer (Bowtie, Avo, ZA Insure) was found using an orchestrator. Bowtie's marketing-site CSP contains **no payment-provider domain at all** and `form-action 'self'`; its checkout sits on a subdomain outside that CSP's scope. The nearest same-vertical adopters found are **Indian** insurers (Star Health/Juspay, an Airpay insurance case study) — not OneDegree competitors, and vendor-published. See 11C. |
| Payment job postings | **0** | ⬜ **Not found.** The careers page is JS-rendered with no job-board link; the Greenhouse board token did not resolve (404). No payment-engineering posting sourced. |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **🟢 Medium (13/29)**
**No public payment RFP was confirmed**, so no RFP override applies.

#### Analyst override — tier unchanged, ceiling stated

**No tier override is applied. 13/29 is the honest arithmetic.** But the brief asked for candour about the ceiling, and three things need saying:

1. **The score is load-bearing on one unsourced number.** 7 of the 13 points come from the transaction-count row (+3, assumed) and the orchestration row (+4, conditional on the in-house checkout service not routing). **If monthly-billing adoption proves to be below ~26–36%, the account falls under the 40,000 gate and must be re-scored and rejected.** The tier is provisional in a way a bare "🟢 Medium" does not convey.
2. **The classic Yuno stories do not apply here.** This is a **single-market, single-currency, HK-only, card-based** book. There is no cross-border corridor to argue, no multi-currency FX leg, no regulatory acquiring gate, and 83.4% of gross premium sits in **one** statutory class. The cross-border approval-rate pitch and the local-rail-coverage pitch — Yuno's two strongest APAC arguments — are both **thin on this account.** Do not stretch them.
3. **What is left is genuinely good, and it is narrow.** The whole business case is **recurring-payment performance in one market**: a 91% renewal rate on a 100%-auto-renewing card book, dunned on a fixed 3-day cadence with no account updater in the published flow, across two unconnected stacks with three providers and inconsistent brand coverage. That is a real, specific, defensible conversation. It is not a reach-and-expansion conversation, and an email that pretends otherwise will be caught.

**No app-store override applies.** `subscription-payments.md` §4 does not bite: premium is collected on the web via Adyen with card-on-file renewal, and Pet Mart sells physical goods on Shopify. Neither is Apple/Google IAP-eligible. PawBook is a companion pet-health app, not a billing channel. ⚠️ App-store listings themselves were **not retrievable** in this environment (`itunes.apple.com` returned 403 at the proxy; guessed listing IDs 404 and were not pursued).

### Source Notes
- ✅ **Adyen live on the insurance flow** — `ADYEN_CLIENT_KEY='live_…'`, `ADYEN_ENVIRONMENT='live-apse'`, plus `*.adyen.com` in CSP `connect-src` and `frame-src`. Re-verified on a second cache-busted fetch. `https://www.onedegree.hk/en-us/faq`
- ✅ **Stripe and Adyen both named by OneDegree** as "Designated Payment Gateway" for card storage. `https://www.onedegree.hk/en-us/terms-of-use`
- ✅ **Shopify Payments live on Pet Mart**, merchant of record "OneDegree Hong Kong Limited". `https://store.onedegree.hk/payments/config`
- ✅ **Card-only acceptance, enumerated by the merchant, last published 2026-09-04.** `https://www.onedegree.hk/en-us/faq/article/what-payment-methods-do-you-accept`
- ✅ **Every-3-days retry; 30-day pet / 7-day home grace; fire auto-terminates.** `https://www.onedegree.hk/en-us/faq/article/what-would-happen-if-i-miss-a-premium-payment`
- ✅ **9/9 pet plans auto-renewable; Annual = 1 instalment, Monthly = 12.** Live plan catalogue in `https://www.onedegree.hk/en-us/pet-insurance`
- ✅ **Pet renewal rate 91% (FY2025); >200,000 pet policies issued over 5 years; 65% of insured pets are cats; a quarter of customers hold more than one pet policy, one holds 16.** `https://www.hk01.com/財經快訊/60314167/`
- ✅ **FY2025 revenue HK$330M (+38%), first full-year profit; FY2024 revenue >HK$240M.** HK01 2026-01-19 + Alibaba Entrepreneurs Fund 2025-04-24.
- ✅ **FY2025 statutory gross premiums HK$331,910k; 82.0% ceded; property damage 83.4% of GWP.** `https://odhk.blob.core.windows.net/common/25DS_en.pdf` (verified first-hand by the orchestrator at Phase 0).
- ✅ **No HKMA Stored Value Facility licence** — verified against the SVF register with known licensees confirmed present as a control. Only authorisation is the IA virtual insurer licence (April 2020).
- ⚠️ **A WebSearch summary asserted "customer base expanded 19-fold to more than 240,000 cumulative policies." This is wrong and I caught it.** The 240,000 figure is **Census and Statistics Department data on Hong Kong households owning cats and dogs** (9.4% of all households, ~400,000 cats and dogs total), quoted by OneDegree as *market context* — not its policy count. The real company figure is **"over 200,000 pet policies issued"** across five years. Logged as a live instance of the documented summary-fabrication hazard.
- ⚠️ **OneInfinity market position — two figures conflict.** The Phase 0 gate recorded "~80% of licensed virtual-asset operators in Hong Kong"; HK01 (2026-01-19) reports *"香港市場目前市佔率達7成"* — **~70% Hong Kong market share**. Different denominators, possibly both true. Both presented; neither adopted as fact.
- ⚠️ **Premium levy** — OneDegree's FAQ states the Insurance Authority levy rate rose to **0.1% with a cap** as of 1 April 2021, citing `https://www.ia.org.hk/en/aboutus/role/financial_arrangements.html`. **Attributed to OneDegree's statement; not independently verified** (`ia.org.hk` was unreachable). Do not cite the rate as current without checking the IA page.
- ⚠️ **No local entity, registration number or IA register entry independently confirmed.** No free registry lookup was reachable.
- ⚠️ **ISO 27001 attaches to OneDegree Global (SG), not the HK insurer.** `[UNVERIFIED — search summary only, page not fetched]`
- ⚠️ **The ▼34.20% MoM traffic decline is unexplained.** See Section 7.
- ❌ **No PCI DSS documentation found.** No complaints found. No payment job postings found. No competitor orchestration found.

### Success Case Alternatives
⚠️ **Be straight about this: no publicly referenceable Yuno case study matches a single-market APAC recurring insurance book.** Forcing one would be the weakest part of the outreach.

- **NetEase Games** and **Garena** — the closest publicly nameable Yuno profiles on *transaction shape only*: APAC-based consumer businesses running high-frequency card acceptance with heavy mobile-web skew. **No published metrics exist for either, so attach no numbers to them.** They match on volume pattern, **not** on vertical, not on recurring billing, and not on single-market concentration. Use as a credibility marker at most.
- **Qatar Airways, Copa Airlines, Avianca** — nameable, but travel/high-ticket/multi-currency. Wrong shape for this account. Do not use.
- **Recommended instead:** build the business case from **discovery**, not from a case study. Section 12 gives the sizing skeleton; the four numbers that fill it (monthly-vs-annual mix, first-attempt renewal failure rate, recovery rate, blended MDR) are all things only OneDegree has. That is the honest and more persuasive route with a company that just posted its first profit and knows its own numbers cold.
- **Vertical precedent that does exist, with its caveat:** Indian insurers **Star Health** (Juspay) and an unnamed insurer in an **Airpay** case study have publicly adopted orchestration for premium collection and recurring mandates. Both are **vendor-published marketing**, in a different market with different rails. Usable as "this is a solved problem in insurance," **not** as a benchmark. `https://juspay.io/customer-stories/star-health-insurance` · `https://airpay.co.in/case-studies/re-architecting-insurance-payments-for-scale-in-a-digital-first-ecosystem`

---

### Executive Summary

OneDegree Hong Kong Limited is Hong Kong's first virtual general insurer (IA licence, April 2020) and the market's leading pet insurance brand, with FY2025 statutory gross premiums of **HK$331.91M (≈US$42.6M)** and its first full-year profit — correcting the target list's stale "~$30M est." by roughly 40%. The key payment-infrastructure finding is that OneDegree runs **three payment providers across two entirely unconnected stacks under one legal entity**: Adyen live on `live-apse` for insurance premium collection, Stripe named alongside Adyen in its own card-vault terms but absent from the browser, and Shopify Payments on the `store.onedegree.hk` Pet Mart e-commerce store — with **no orchestration layer anywhere**, and inconsistent card-brand coverage between the two (UnionPay and JCB accepted on insurance, neither enabled on Pet Mart; Google Pay live on Pet Mart, absent from insurance). The orchestration opportunity is **not** cross-border or rail coverage — this is a single-market, single-currency, HK-only, card-only book — but **involuntary churn on a 100%-auto-renewing card book**: OneDegree publishes a **fixed every-3-days retry** cadence inside grace periods of 30 days (pet) and 7 days (home), with fire policies auto-terminating if the renewal is not collected, and every published decline remedy requiring the customer to supply a new card by hand. **Motion: greenfield**, with a conditional caveat on their in-house Azure checkout service.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** **Path 1 — pasted/supplied SimilarWeb data.** Supplied by Prateek 2026-10-09 (Google Sheet, *HK October Target Accounts — Similarweb Traffic*), period **Sep 2026**, Similarweb PRO, Worldwide, All traffic. Used verbatim and **not re-researched**, per the method. Figures not independently verified against Similarweb.

**Domain:** `onedegree.hk` (1 domain pulled). Resolved live: `onedegree.hk` and `www.onedegree.hk` both 301/302 to **`https://www.onedegree.hk/en-us`** — a single property, no separate regional domains. `store.onedegree.hk` (Pet Mart, Shopify), `od-wp.onedegree.hk` (WordPress.com-hosted content property) and `partnership.onedegree.hk` are subdomains of the same registrable domain and are **not** broken out in the supplied top-10 cut.

**Total visits (Sep 2026): 58,657 · MoM ▼34.20% · Desktop 27.76% · Mobile web 72.24%**

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | 🇭🇰 **Hong Kong** — **high priority** | **76.90%** | ~45,107 | Total domain ▼34.20% MoM; per-country trend not supplied | SimilarWeb (supplied 2026-10-09) |
| 2 | 🇺🇸 United States | 4.67% | ~2,739 | not supplied | SimilarWeb (supplied 2026-10-09) |
| 3 | 🇹🇼 Taiwan | 4.24% | ~2,487 | not supplied | SimilarWeb (supplied 2026-10-09) |
| 4 | 🇦🇺 Australia | 4.03% | ~2,364 | not supplied | SimilarWeb (supplied 2026-10-09) |
| 5 | 🇸🇬 Singapore | 2.69% | ~1,578 | not supplied | SimilarWeb (supplied 2026-10-09) |
| 6 | 🇬🇧 United Kingdom | 2.64% | ~1,549 | not supplied | SimilarWeb (supplied 2026-10-09) |
| 7 | 🇨🇦 Canada | 2.55% | ~1,496 | not supplied | SimilarWeb (supplied 2026-10-09) |
| 8 | 🇯🇵 Japan | 1.09% | ~639 | not supplied | SimilarWeb (supplied 2026-10-09) |
| 9 | 🇳🇱 Netherlands | 0.79% | ~463 | not supplied | SimilarWeb (supplied 2026-10-09) |
| 10 | 🇵🇭 Philippines | 0.24% | ~141 | not supplied | SimilarWeb (supplied 2026-10-09) |

**APAC visible total: 89.19%** across 6 of the top 10 (HK, TW, AU, SG, JP, PH). This is a **top-10 cut**, so APAC totals are a **visible floor**, not a complete figure. Gulf markets (UAE, Saudi) and Turkey are EMEA and excluded from every total; Russia and Kazakhstan are outside the territory market list and also excluded.

**Markets >5% traffic share: Hong Kong only.**

**Top-10 countries with no local entity — cross-referenced against Section 2:** United States, Taiwan, Australia, United Kingdom, Canada, Japan, Netherlands, Philippines (8 of 10). Singapore has a sister **tech** entity, not a selling insurer.

> ⚠️ **The standard cross-border warning does NOT apply to this account, and it is important not to issue it reflexively.** Those markets have no entity because **OneDegree does not sell there.** Its authorisation is a Hong Kong virtual insurer licence and nothing else, and Pet Mart's live Shopify config restricts shipping to `allowedCountryCodes: ["HK"]`. There is no cross-border acquiring inefficiency here because there is no cross-border selling. Treating 23.1% non-HK traffic as unserved demand would be a factual error.
>
> **Two legitimate readings of that non-HK traffic remain open and are worth one question on the call:** (a) it is non-transacting — press, research, diaspora, competitor and bot traffic; or (b) a slice is Hong Kong residents and returning diaspora browsing from abroad, who would transact on an HK-issued card. (a) is far more likely. Neither is sourced. Do not build a pitch on (b).

**Engagement metrics (bounce rate, pages/visit, visit duration) and global rank:** **not supplied** in the sheet and not re-researched, per the method.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Hong Kong. **OneDegree Hong Kong Limited**, granted a virtual insurance licence by the Hong Kong Insurance Authority in **April 2020** — described on its own site as *"one of the first insurtech companies in Hong Kong to obtain such a license."* Operating since 2020; the pet product (Pawfect Care, now Pet CEO Plan®) launched April 2020. Headcount **92** as of January 2026, of whom **25% are technology staff**, with a stated intent to stay under 100.

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| 🇭🇰 Hong Kong | **OneDegree Hong Kong Limited** (the licensed insurer; also the Shopify merchant of record for Pet Mart) | **Not found** | `https://www.onedegree.hk/en-us/business-overview` · `https://store.onedegree.hk/payments/config` · site footer *"© 2026 OneDegree Hong Kong Limited"* |
| — (holding) | **AI Financial Technology Holding Company ("AIFT")** — OneDegree HK is described as a *"wholly owned subsidiary"* | Not found; jurisdiction of incorporation not stated | `https://www.onedegree.hk/en-us/business-overview` |
| 🇸🇬 Singapore | **OneDegree Global (SG) Pte. Ltd.** — sister company; enterprise insurance core system + cyber security; named ISO 27001 holder | Not found | `[UNVERIFIED — search summary only, page not fetched]` — InvestHK client profile, dated 2021 |
| 🌍 Middle East (EMEA) | **OneDegree Middle East** — referenced in OneDegree's own newsroom | Not found | `https://www.onedegree.hk/en-us/press` (item dated 2024-01-08) |
| — (brands, not confirmed as separate entities) | **OneInfinity** (digital-asset insurance; `oneinfinity.global`, `cyber-hk.oneinfinity.global`) · **Vulcan** (generative-AI protection) · **PawBook®** · **OneDegree Pet Mart®** | n/a | `https://www.onedegree.hk/en-us/business-overview` |

**Investors named on OneDegree's own page:** Cathay Capital (a subsidiary of Cathay Financial Holding), **Dubai Insurance Company**, and **Kyobo Life Insurance** (Korea). AIFT reports raising *"over US$100 million capital in total"* by 2026. Earlier rounds: Series A ~US$25.5M–30M (2019–2020), Series B closed at **US$55M** across two tranches (~US$28M in 2021 with Sun Hung Kai and the AEF Greater Bay Area Fund; a further ~US$27M in 2023 with Gobi Partners and BitRock Capital). ⚠️ The 2021/2023 tranche details come from **search summaries only, pages not fetched** — `[UNVERIFIED]`. The Cathay/Dubai Insurance/Kyobo names are from OneDegree's own page and are sourced.

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| 🇭🇰 Hong Kong | ✅ #1 (76.90%) | ✅ Yes — the licensed insurer | **No** — not a gated market for this merchant; it holds the local licence and acquires locally via Adyen `live-apse` | **None.** Domestic acquiring, domestic entity, single currency (HKD) |
| 🇺🇸 United States | ✅ #2 (4.67%) | ❌ No | n/a — not a selling market | **None — no selling activity** |
| 🇹🇼 Taiwan | ✅ #3 (4.24%) | ⚠️ Group tech/security role advertised in Taipei; no selling entity found | n/a — not a selling market | **None — no selling activity** |
| 🇦🇺 Australia | ✅ #4 (4.03%) | ❌ No | n/a — not a selling market | **None — no selling activity** |
| 🇸🇬 Singapore | ✅ #5 (2.69%) | ⚠️ OneDegree Global (SG) Pte. Ltd. — B2B tech, not a consumer insurer | n/a — not a selling market | **None — no selling activity** |
| 🇬🇧 UK · 🇨🇦 CA · 🇯🇵 JP · 🇳🇱 NL · 🇵🇭 PH | ✅ #6–#10 | ❌ No | n/a | **None — no selling activity** |

> **No cross-border warning is issued for any market on this account.** The standard warning assumes unserved transacting demand; here the sourced evidence is that OneDegree sells only in Hong Kong, under a Hong Kong licence, shipping only to Hong Kong, in HKD. **Writing a cross-border warning here would be factually wrong, and the brief was right to predict the cross-border story is thin.**
>
> ⚠️ **One genuine regulatory point, stated carefully.** OneDegree holds **no HKMA Stored Value Facility licence** — verified at Phase 0 against the HKMA SVF register, with known licensees (Octopus, Alipay, WeChat Pay, PayPal, HKT Payment, Autotoll) confirmed present as a control before trusting the zero. Its only authorisation is the IA virtual insurer licence. **This confirms it is not a payment business** (see Phase 0 / ICP exclusion) — it is not a constraint on Yuno serving it.

> **MANUAL:** Registration numbers were not obtainable here. Verify **OneDegree Hong Kong Limited** against the Hong Kong Companies Registry (ICRIS, paid lookup) and confirm current authorised-insurer status on the Insurance Authority register. ⚠️ Environment note: `iir.ia.org.hk` returned an empty 246-byte response and `ia.org.hk` returned 403 during the Phase 0 run; neither was reachable in this run either.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| 🇭🇰 Hong Kong — **insurance premium** | **Adyen** — live client key `live_DDIKN53C5NDCNCIVW7IQTQB76Y6XYR47`, `ADYEN_ENVIRONMENT='live-apse'` (live APAC-SE region), Apple Pay merchant ID `000000000580332`, merchant name `OneDegree` | `[Source Code]` | `https://www.onedegree.hk/en-us/faq` (inline config block, served on every page) |
| 🇭🇰 Hong Kong — **insurance premium** | **Adyen** — `*.adyen.com` present in CSP `connect-src` **and** `frame-src`; the **only** payment-processor domain in the entire policy. No `form-action` directive is set at all, so card capture runs through Adyen's JS/iframe components rather than a self-posted form | `[Source Code]` (response header) | `https://www.onedegree.hk/` (CSP response header, fetched 2026-10-09) |
| 🇭🇰 Hong Kong — **card-on-file vault** | **Stripe** *and* **Adyen** — named jointly by OneDegree as *"Designated Payment Gateway"* for the credit-card storage service. Stripe is **absent from the CSP**, so it is not browser-facing | `[Terms/Privacy Policy]` | `https://www.onedegree.hk/en-us/terms-of-use` · `https://www.onedegree.hk/en-us/privacy-policy` |
| 🇭🇰 Hong Kong — **Pet Mart e-commerce** | **Shopify Payments** — `"shopifyPaymentsEnabled":true`; merchant of record *"OneDegree Hong Kong Limited"*; shopId `67774218378`; internal shop `afhvbb-ze.myshopify.com`; currency HKD | `[Source Code]` + `[Checkout]` | `https://store.onedegree.hk/payments/config` |
| 🇭🇰 Hong Kong — **own checkout service** | **In-house** — `od-finance-checkout-prod-as.azurewebsites.net` in CSP `connect-src`, with `dev` / `dev2` / `dev3` / `sit` / `sit2` / `sit3` / `uat` / `uat2` / `uat3` / `dr` siblings. A full in-house checkout deployment pipeline on Azure App Service. **Not a PSP** — their own middleware | `[Source Code]` (response header) | `https://www.onedegree.hk/` (CSP response header) |
| — | **PayPal** — ❌ **not enabled.** `"paypalConfig":null` on Pet Mart. ⚠️ The generic `ShopifyPaypalV4VisibilityTracking` script ships on all Shopify stores and is **not** evidence of PayPal | `[Source Code]` | `https://store.onedegree.hk/payments/config` |
| — | **Amazon Pay** — ❌ not enabled (`"amazonPayCv2Config":null`). **Shop Pay** — `"shopifyPayConfig":null`, though a `dev.shopify.shop_pay` handler is declared in the UCP manifest | `[Source Code]` | `https://store.onedegree.hk/payments/config` · `https://store.onedegree.hk/.well-known/ucp` |

**Not established — searched and not found:** AsiaPay/PayDollar, Global Payments, Mastercard Payment Gateway Services (MPGS), Braintree, Checkout.com, 2C2P, Worldpay, Cybersource, Omise, Xendit, Midtrans, Razorpay. **None of these appears in the CSP, in any fetched bundle, or in search.** The CSP is exhaustive for browser-facing processors and names only Adyen, so a second *browser-facing* acquirer is effectively ruled out; a **server-side** acquirer would not appear there, which is precisely the gap Stripe occupies.

⚠️ **Substring false positives logged during this run — all verified as non-findings:**
- `stripe` matched **"Striped mud turtle"** in a species dropdown on `od-wp.onedegree.hk` (turtle insurance). *New trap for the repo's list.*
- `stripe` matched the CSS path `images/stripes/textline.png` on a competitor site (the documented table-striping trap).
- `payme` matched **"payment" / "Payment" 18 times** on the Pet Mart store and 85–240 times per page on `onedegree.hk`. **PayMe is not present anywhere.** This trap fires constantly here.
- `octopus` matched a **partner logo image filename** on Bowtie's homepage, not a payment method.
- `wechat` matched **image filenames** (`WechatIMG943`, `wechat_pet_care.png`) on a competitor site.
- `poli` fires on "policy" constantly across every page, exactly as the repo warned. No POLi finding.

#### 3B. Payment Orchestrator

**Classification: None detected — direct PSP integrations only (greenfield).**

**Evidence:**
- `[Source Code]` — the `onedegree.hk` CSP enumerates every host the browser may contact. **No orchestrator domain appears.** The only payment-processor domain is `*.adyen.com`. Source: `https://www.onedegree.hk/` response header.
- `[Source Code]` — no orchestrator string in any fetched page bundle (homepage, FAQ, pet insurance, terms, privacy policy, business overview, press, careers, PawBook, Pet Mart).
- `[Source Code]` — Pet Mart's `payments/config` and UCP manifest enumerate handlers exhaustively: Shopify card, Shopify Shop Pay, Google Pay, Apple Pay. No orchestrator.
- Search for `OneDegree` against Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails and Yuno returned **no evidence of any orchestration platform.**
- The `Payment Orchestrator` column in `accounts/apac-tal.csv` is **empty** for OneDegree — consistent with this finding, and now independently corroborated rather than merely repeated.

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with PSP(s), which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

⚠️ **The caveat that must travel with this classification.** OneDegree has **two card providers named in its own terms** and **its own checkout service** (`od-finance-checkout-*-as.azurewebsites.net`) sitting in front of them. That is the shape of a nascent in-house provider-selection layer. **No evidence was found that it routes, retries across providers, or fails over** — the published dunning behaviour is a single fixed 3-day retry, which is what a *single*-provider integration looks like. So: **greenfield (+4)**, not in-house (+1). **Confirm on the first call.** If that service does select between Stripe and Adyen, the motion shifts from "you have no orchestration layer" to "you built one and are now maintaining it" — a different, harder, but still live conversation about opportunity cost.

**Card tokenization approach:** card-on-file vaulting is confirmed and is customer-consented. From the checkout bundle, verbatim: *"your credit card information will be saved for faster future checkouts and automatic policy renewals."* The vault is held at **Stripe and/or Adyen** per the Terms of Use. **Network tokens: not found** — no `network token` or tokenisation string anywhere in the fetched assets, and the published remedy for an expired or reissued card is for the customer to enter a new one. `[INFERENCE, not confirmed]` — absence from public assets is not proof of absence in the backend.

> **MANUAL:** Walk the pet quote → checkout flow with DevTools open. Watch for (a) a call to Adyen's `/paymentMethods` endpoint and what it returns — this is the only way to see whether local rails are enabled server-side but not advertised in the FAQ; (b) whether `od-finance-checkout-prod-as.azurewebsites.net` is called before the Adyen component mounts, and whether its response names a provider; (c) any Stripe.js load on the saved-card or renewal path specifically, which is where Stripe most plausibly still lives.

---

### Section 4: Alternative & Local Payment Methods

Checked for every country in Section 1 with >1% traffic share. **In practice only Hong Kong is a transacting market** (HK-only licence; Pet Mart ships `["HK"]` only), so APM analysis for the US, Taiwan, Australia, Singapore, the UK, Canada and Japan is **not applicable** rather than "a gap" — there is no checkout to serve those users. Scored accordingly.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| 🇭🇰 HK — insurance | **Visa, Mastercard, American Express, JCB, UnionPay** (credit) + **debit cards** | Cards | ✅ **Active in checkout** | `https://www.onedegree.hk/en-us/faq/article/what-payment-methods-do-you-accept` (last published **2026-09-04**) |
| 🇭🇰 HK — insurance | **Apple Pay** | Digital wallet | ✅ **Active in checkout** — Adyen Apple Pay merchant ID configured; dedicated UX strings incl. *"Apple Pay is not available on this device. Please choose another payment method."* and a Device Account Number explainer on the **renewal** path | `https://www.onedegree.hk/en-us/faq` (Adyen config + i18n bundle) |
| 🇭🇰 HK — insurance | **Google Pay** | Digital wallet | ❌ **Not found** — no string, config or CSP entry anywhere on `onedegree.hk` | `https://www.onedegree.hk/` (CSP) |
| 🇭🇰 HK — insurance | **Card-on-file recurring (MIT)** — Annual = 1 charge/yr, Monthly = 12 charges/yr; 9/9 plans auto-renewable | Direct debit / mandate (card-based) | ✅ **Active** | `https://www.onedegree.hk/en-us/pet-insurance` (live plan catalogue, 18 `plan_payment_modes` objects) |
| 🇭🇰 HK — insurance | **FPS** (Faster Payment System) | Bank transfer / A2A | ❌ **Not found** | Absent from the merchant's own enumerated method list (2026-09-04) and from the CSP |
| 🇭🇰 HK — insurance | **PayMe** | Digital wallet | ❌ **Not found** (all 85–240 per-page "payme" matches are the substring "payment") | as above |
| 🇭🇰 HK — insurance | **Octopus** | Digital wallet / prepaid | ❌ **Not found** (0 matches across all fetched pages) | as above |
| 🇭🇰 HK — insurance | **AlipayHK** · **Alipay** | Digital wallet | ❌ **Not found** (0 matches) | as above |
| 🇭🇰 HK — insurance | **WeChat Pay HK** | Digital wallet | ❌ **Not found** (0 matches) | as above |
| 🇭🇰 HK — insurance | **Instalments / BNPL** (Atome, Klarna, Afterpay) | BNPL / Instalments | ❌ **Not found.** ⚠️ Note: "Monthly" billing is a **12-instalment premium schedule at zero surcharge**, which functions as a native instalment offer — but it is not a BNPL product | `https://www.onedegree.hk/en-us/pet-insurance` |
| 🇭🇰 HK — insurance | **Direct debit (eDDA / autopay)** | Direct debit / mandate | ⚠️ **Ambiguous — flagged, not resolved.** The privacy policy lists *"processing requests for payment, and for direct debit authorization"* as a data-processing purpose, yet **no direct-debit option appears in the checkout or in the enumerated payment methods.** Present both; do not assert either | `https://www.onedegree.hk/en-us/privacy-policy` vs `https://www.onedegree.hk/en-us/faq/article/what-payment-methods-do-you-accept` |
| 🇭🇰 HK — **Pet Mart** | **Visa, Mastercard, American Express, Discover, Diners Club** | Cards | ✅ **Active in checkout** (`enabled_card_brands`) | `https://store.onedegree.hk/.well-known/ucp` |
| 🇭🇰 HK — **Pet Mart** | **UnionPay** · **JCB** | Cards | ❌ **Not enabled** — while **both are accepted on the insurance flow** | `https://store.onedegree.hk/.well-known/ucp` |
| 🇭🇰 HK — **Pet Mart** | **Apple Pay** | Digital wallet | ✅ **Active** — `merchantCapabilities:["supports3DS"]`, `supportedNetworks:["visa","masterCard"]` only | `https://store.onedegree.hk/payments/config` |
| 🇭🇰 HK — **Pet Mart** | **Google Pay** | Digital wallet | ✅ **Active** — `environment:"PRODUCTION"`, `gateway:"shopify"`, `allowPrepaidCards:false` | `https://store.onedegree.hk/payments/config` |
| 🇭🇰 HK — **Pet Mart** | **FPS, PayMe, Octopus, AlipayHK, WeChat Pay HK** | A2A / wallets | ❌ **Not enabled** — the Shopify and UCP configs enumerate handlers exhaustively; none appears | `https://store.onedegree.hk/payments/config` · `.well-known/ucp` |
| 🇭🇰 HK — **Pet Mart** | **Gift cards** | — | ❌ `"supportsGiftCards":false` | `https://store.onedegree.hk/payments/config` |
| 🇺🇸 US · 🇹🇼 TW · 🇦🇺 AU · 🇸🇬 SG · 🇬🇧 UK · 🇨🇦 CA · 🇯🇵 JP | all local rails | — | **N/A — not a selling market.** HK-only licence; Pet Mart ships `allowedCountryCodes:["HK"]` | `https://store.onedegree.hk/payments/config` |

> ⚠️ **Warning: In Hong Kong — OneDegree's #1 traffic market at 76.90% — FPS is widely used but is not supported by OneDegree on either of its two checkouts.**
>
> **Prominence of FPS, sourced:** per the HKMA's own inSight article of 27 March 2024 (Howard Lee, Deputy Chief Executive), FPS registrations grew from over 2 million at end-2018 to **13.6 million at end-2023** — *"almost doubling the population of Hong Kong"* (7.5 million at end-2023 per the Census and Statistics Department); FPS averaged **1.25 million transactions per day in 2023** at an average daily HKD value of **HK$9.0 billion**; *"more than 90% of Government departments accept the FPS as a means of payment"*; and merchant payments, bill payments, e-wallet top-ups and business payments have grown to **50% of turnover**, from P2P being over 90% at launch. Source: `https://www.hkma.gov.hk/eng/news-and-media/insight/2024/03/20240327/`
> Codapay's Hong Kong market guide states that *"Account-to-Account (A2A) payments account for around **64% of transaction volume**, surpassing credit and debit cards"* and, from its own book for 1 Oct 2024 – 30 Sep 2025, **FPS 61% vs card payments 34%**, concluding that *"prioritizing FPS integration is key."* Source: `https://www.coda.co/market-guides/hong-kong/`
>
> **Three honest qualifications — these matter, and the email must respect them:**
> 1. **Codapay's mix is not insurance.** Coda is a digital-goods and games payments company; low-ticket, high-frequency, youth-skewed. Its 61/34 split is **its own** book, not the Hong Kong market, and it is the weaker of the two citations. The HKMA figures are the ones to lean on.
> 2. **Codapay's own page is internally inconsistent** — it reports A2A at ~64% of transaction **volume** while also saying cards account for *"over 50% of transaction value in 2026."* Volume and value are different measures, so both can hold, but flag the discrepancy rather than quoting one as settled.
> 3. 🔑 **FPS is a push rail, and that limits the claim.** FPS cannot simply replace card-on-file MIT for an automatic monthly premium debit. Hong Kong has **eDDA** for pull debits, but **eDDA's suitability for recurring insurance premium collection was not sourced in this run** and must not be asserted. **The defensible version of this gap is narrower and still strong:** FPS absence costs OneDegree at **first purchase** (the acquisition checkout, where the customer is choosing how to pay) and in the **failure-recovery path** (when a renewal card declines, the only published remedy is "enter another card" — there is no non-card way for a willing customer to pay and keep the policy alive before a 7-day or 30-day grace period expires). That is the claim to make.

> ⚠️ **Second, smaller warning — a discrepancy inside OneDegree's own disclosures.** The payment-methods FAQ enumerates cards and debit cards and does **not** mention Apple Pay, yet Apple Pay is demonstrably live (Adyen Apple Pay merchant ID configured, dedicated purchase **and renewal** UX strings, an Apple Pay billing-cycle constraint for bundled policies). Their published method list is **incomplete relative to their own checkout.** Present both; it is a small credibility detail that shows the research was done properly.

> ⚠️ **Methodological caveat required by this repo's own history.** Adyen's Drop-in/Components render the available method list from a server-side `/paymentMethods` call. **A method's absence from the merchant's front-end bundle therefore proves nothing** — this exact error produced a published false claim in this repository once. The FPS/PayMe/Octopus/AlipayHK/WeChat findings above do **not** rest on bundle greps. They rest on **OneDegree's own affirmative enumeration** of accepted methods, last published 2026-09-04 — a positive statement of what they take, which is legitimate evidence of what they do not. For Pet Mart they rest on Shopify's and UCP's **exhaustive** handler manifests. A DevTools walk of the live Adyen `/paymentMethods` response (see the MANUAL note in 3B) is the only way to close the remaining gap.

> **MANUAL:** Use an HK IP and walk both checkouts. For insurance, capture the Adyen `/paymentMethods` response. For Pet Mart, add an item and reach the Shopify checkout to see the rendered method list, which can include app-based local rails not present in `payments/config`.

---

### Section 5: Payment Issues & Customer Complaints

*No payment-related complaints found on Reddit, X, Trustpilot, or app-store reviews.* Searches covered English and Traditional Chinese (`OneDegree 一度保 投保 信用卡 付款 問題 續保 失敗 投訴`), Hong Kong consumer forums, and pet-insurance complaint corpora. The English-language pet-insurance complaint results that surfaced were **UK insurers** via the Financial Ombudsman Service and Trustpilot — **not OneDegree**, and not usable.

⚠️ **App-store reviews — the richest APAC source — were not retrievable in this environment.** `itunes.apple.com` returned **403 at the egress proxy**; constructed Play Store and App Store listing URLs returned 404 and were not pursued rather than guessed at. One search summary reported an App Store rating of 4.0 from 1 rating and a third-party tracker reporting 5.0 from 14 reviews — **`[UNVERIFIED — search summary only, page not fetched]`**, mutually inconsistent, and far too small a sample to read anything into either way.

**What I found instead is different in kind, and arguably more useful: OneDegree's own documentation of its failure modes.** This is **not** a complaint record and **no failure rate is asserted** — there is no source for one. It is the published mechanism.

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| **Failed recurring payments** — dedicated dashboard state: *"Transaction failed. Please change your credit card."* | OneDegree member dashboard (i18n bundle) | **Unknown** — a hard-coded UI state proves the case is designed for, not how often it occurs | current (fetched 2026-10-09) | `https://www.onedegree.hk/en-us/faq` (bundle) |
| **Failed recurring payments** — fixed **every-3-days** retry inside grace; **30 days** pet/CI, **7 days** home/appliances; **fire auto-terminates** if not collected by the effective date | OneDegree FAQ | Unknown | current | `https://www.onedegree.hk/en-us/faq/article/what-would-happen-if-i-miss-a-premium-payment` |
| **Declined transactions** — a published taxonomy with customer-action remedies: expired/incorrect card → add another card; insufficient limit → contact your bank; declined → contact your bank to approve | OneDegree FAQ | Unknown | current | `https://www.onedegree.hk/en-us/faq/article/why-was-my-payment-declined` |
| **Duplicate charges** — a dedicated FAQ exists: *"I received two transaction notifications. Was my card charged twice?"*, explaining expected annual/monthly charge timing and routing anything else to `care@onedegree.hk` | OneDegree FAQ | **Unknown, but a standalone FAQ implies recurring customer contact volume** `[INFERENCE, not confirmed]` | current | `https://www.onedegree.hk/en-us/faq/article/i-received-two-transaction-notifications-was-my-card-charged-twice` |
| **Decline-code coverage in the bundle** — distinct customer-facing strings for invalid card number (`422004`), insufficient balance (`422005`), unsupported card type (`422011`), CVC failure (`422012`), transaction refused (`422013`), expired card, and *"Payment declined. Please contact your card issuer."* | OneDegree checkout (i18n bundle) | Unknown | current | `https://www.onedegree.hk/en-us/faq` (bundle) |
| **Card management friction** — a linked card *"cannot be deleted"* directly; the customer must add a replacement first, then delete the old one | OneDegree FAQ | Unknown | current | `https://www.onedegree.hk/en-us/faq/tag/billing-and-payment` |
| **Debit date is immovable** — *"No, unfortunately the payment debit date can't be changed."* | OneDegree FAQ | Unknown | current | `https://www.onedegree.hk/en-us/faq/tag/billing-and-payment` |
| **Third-party cardholders permitted** — a family member's or friend's card may pay the premium, provided the cardholder enters the details themselves | OneDegree FAQ | Unknown | current | `https://www.onedegree.hk/en-us/faq/tag/billing-and-payment` |
| **Test-mode decline string shipped in the production bundle** — `general_payment_testmode_decline: "Please use a valid credit card for payment."` | OneDegree checkout (i18n bundle) | Isolated / cosmetic | current | `https://www.onedegree.hk/en-us/faq` (bundle) |

> *"The pattern here is not a complaint pattern — it is a design pattern. Every published remedy for a failed renewal terminates in the customer manually supplying a different card, inside a grace window of 30 days (pet), 7 days (home and appliances) or effectively zero (fire), against a retry schedule that fires every 3 days regardless of why the payment failed. On a book where **9 of 9 pet plans are `is_auto_renewable: true`** and the pet renewal rate is **91%**, the specific orchestration opportunity is decline-code-aware retry sequencing plus network tokens and account updater, so that an expired or reissued card refreshes without the customer ever being asked — which is precisely the leak a fixed 3-day retry cannot address, because retrying an expired credential never succeeds."*

⚠️ **Do not assert a failure rate in any email.** None is published, and `subscription-payments.md` §5 is explicit that this is what the meeting is for.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | **2026-07-13** | **Emily Chow promoted from Deputy Chief Executive to Chief Executive and Executive Director, with immediate effect.** The release frames the outgoing four-year tenure as *"Passing Four-Year Tenure with Flying Colors, Delivering over Sixfold Revenue Growth & Full-Year Profitability."* **Most recent corporate event — three months before this report.** | **Leadership Change** | `https://www.onedegree.hk/en-us/press` |
| 2 | **2026-01-19** | **FY2025 results: revenue up 38% to HK$330M; first full-year profit (seven-figure HKD), against a ~HK$40M loss in 2024** — the fastest of Hong Kong's four virtual insurers and eight digital banks to turn profitable. Stated next-phase target: **double total revenue within 5 years**, via deeper customer relationships and **cross-selling fire and home cover to pet insurance customers**. Headcount **92**, 25% technology staff, to stay under 100. Digital-asset insurance **up 1.5× YoY** with ~**70% Hong Kong market share**. Pet book: 5-year CAGR ~100%, **over 200,000 policies issued**, renewal rate **91%**, 65% of insured pets are cats, 54% aged 4 or under, **a quarter of customers hold more than one pet policy and one holds 16**. | **Funding / Financial Results + Strategy** | `https://www.hk01.com/財經快訊/60314167/` |
| 3 | **2025-07-07** | Pet CEO Plan® enhanced — additional Feline Infectious Peritonitis (FIP) cover and a new **Prestige Plan** covering MRI and CT costs. | Product Expansion | `https://www.onedegree.hk/en-us/press` |
| 4 | **2025-06-02** | New product line: **Solar Photovoltaic System coverage** for village houses. | Product Expansion | `https://www.onedegree.hk/en-us/press` |
| 5 | **2025-04-23 / 2025-04-24** | Fifth anniversary: **2024 revenue surpassed HK$240 million** — a 27-fold increase on the launch year, CAGR 131%; customer numbers up **more than 17×** since launch with a **25% rise in 2024 alone**; pet segment revenue up **24×** since 2020 (CAGR 124%); **67% of customers under 40**, with over-60s up **62%** in 2024; home insurance revenue **+57% YoY** in 2024; fire insurance **grew 5×**. **PawBook® app and Pet Mart® e-commerce platform launched alongside the anniversary.** | Market Expansion / Financial Results | `https://ent-fund.org/en/news/details/480` · `https://www.onedegree.hk/en-us/news/ODHK-5anniversary-en` |

**Older but relevant:** **2024-01-08** — *"OneDegree Group announced two key appointments to OneDegree Global and OneDegree Middle East"* (`https://www.onedegree.hk/en-us/press`). **2024-04-22** — top spot among Hong Kong's four digital insurers for a second consecutive year. **2024-05-07** — Head of Growth hired *"to strengthen product engagement and grow customer lifetime value."*

**Public payment RFP:** *No public payment-related RFP found.*
**Payment infrastructure hiring:** **Not found.** The careers page is JS-rendered with no job-board link, and the Greenhouse board token did not resolve (404). No posting mentioning PSP evaluation, payment platform migration or orchestration was sourced. One search summary referenced an *"Information Security Officer, Virtual Insurance"* role in **Taipei** — `[UNVERIFIED — search summary only, page not fetched]`, and security, not payments.
**Licence applications:** none found beyond the existing IA virtual insurer licence (April 2020). Confirmed **no HKMA Stored Value Facility licence**.

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | **2026-09-04** | **"What payment methods do you accept?" republished** — cards and debit cards only, closing with *"We will continue to introduce more payment methods to provide you with additional options that meet your needs."* | 🔑 **The strongest single signal on the account.** A dated, merchant-published statement of intent to expand payment methods, five weeks before outreach, on a checkout that currently carries **no Hong Kong local rail**. This is the opening. | `https://www.onedegree.hk/en-us/faq/article/what-payment-methods-do-you-accept` |
| 2 | **2026-01-19** | FY2025 first full-year profit on revenue up 38% to HK$330M; five-year revenue-doubling target; explicit pet→fire/home cross-sell strategy | More policies per customer means more card charges per customer, and multi-policy billing alignment becomes a real operational constraint (see the Apple Pay billing-cycle restriction in Section 8) | `https://www.hk01.com/財經快訊/60314167/` |
| 3 | 2025-04 | **Pet Mart® e-commerce platform launched** alongside the fifth anniversary | Created the **second payment stack** — Shopify Payments, a different PSP, different card brands, non-recurring transaction type, under the same legal entity | `https://ent-fund.org/en/news/details/480` |
| 4 | — | **Pet Mart runs Shopify's UCP (Universal Commerce Protocol) manifest, version 2026-08-25**, with live agentic-commerce endpoints (`dev.ucp.shopping`, MCP transport) and `dev.shopify.card`, `com.google.pay` and `dev.shopify.shop_pay` payment handlers declared | An agent-initiated checkout surface is live on the pet-retail side. Not OneDegree's own build — it ships with Shopify — but it means a second, newer payment surface exists that the insurance stack has no equivalent of | `https://store.onedegree.hk/.well-known/ucp` |
| 5 | — | **No provider removal found.** No evidence of a PSP being dropped. ⚠️ The *"Stripe and/or Adyen"* construction in OneDegree's own terms is the only hint of provider change, and it is ambiguous in both directions | A migration **in progress or stalled** is the most interesting unresolved possibility on this account | `https://www.onedegree.hk/en-us/terms-of-use` |

**Nothing found** on `thepaypers.com`, `finextra.com`, `pymnts.com` (beyond 2022 OneInfinity/Munich Re coverage), `techinasia.com` or `e27.co` relating to OneDegree's payment stack.

> ⚠️ **The ▼34.20% MoM traffic decline — UNRESOLVED. No sourced explanation found, and I am not going to guess.**
>
> What can be said rigorously:
> - **The timing gap matters.** The GWP figure is **FY2025** (statutory, to 31 Dec 2025). The traffic figure is **Sep 2026**. **The drop therefore does not, by itself, evidence a decline in transaction volume** — the two measure different periods nine or more months apart.
> - **Equally, a 2026 deterioration cannot be ruled out.** There is no FY2026 statutory comparative: **every FY2024 comparative in the Disclosure Statement reads "Not Applicable"** (first year under the new IA disclosure regime), so there is no prior-year statutory baseline and no trend line to read. Do not imply a statutory trend in either direction.
> - **For a 76.90%-domestic insurer, web visits are a weak proxy for billing volume anyway.** Renewals are automatic card-on-file MITs that generate **no site visit at all**. A book that is 91%-renewing by design decouples transaction count from traffic — which is exactly why the volume gate was derived from premium count rather than visits.
> - **One checkable hypothesis, offered as a hypothesis only:** third-party comparison sites list OneDegree promotional codes expiring **30 June 2026** and **31 July 2026** (`https://www.moneysmart.hk/en/pet-insurance/onedegree`, `[UNVERIFIED — search summary only, page not fetched]`). A paid-acquisition and promo cycle ending in late Q2/Q3 2026 would depress August–September sessions without any change in the in-force book. **This is unverified speculation and must not appear in outreach.** It is in Manual Research Recommendations as something Prateek can check against a 12-month traffic series.

---

### Section 8: Checkout Experience Audit

**Scope note.** The **pre-authentication** layer was fully accessible and is reported from first-hand fetches: response headers and CSP, the inline payment configuration, the live product/plan catalogue, the complete checkout i18n string bundle, and — for Pet Mart — Shopify's public `payments/config` and UCP manifests. The **post-authentication** card-entry step was **not** walked: *"Sign in you will see credit card input field"* and *"Register / Login to Checkout Now"* confirm the card form sits behind account creation, which this environment cannot complete. Findings below are limited to publicly observable elements and are labelled where inferred.

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| **Checkout type** | **Custom-built**, embedded. Own Next.js front end + own Azure checkout service (`od-finance-checkout-prod-as.azurewebsites.net`) + Adyen components. **Pet Mart: Shopify hosted checkout** | **Fair** | Two architecturally unrelated checkouts under one legal entity |
| **Guest checkout** | ❌ **No — account creation is mandatory.** *"Register / Login to Checkout Now"*, *"Sign Up / Login to Check Out"*, *"Sign in you will see credit card input field"* | **Poor** | A forced-registration wall ahead of the card form on a discretionary consumer purchase. Known conversion cost. Pet Mart (Shopify) does not share this constraint |
| **Steps to complete payment** | Quote → select coverage → purchase info → **Review** → register/login → payment details → confirm popup (*"Are you sure the information is all right?"*) → processing. Quotes are savable and expirable (*"The quotation is expired. Please quote again."*) | **Fair** | Long but appropriate for insurance underwriting; save-quote-by-email recovery is a good touch |
| **Card input experience** | **Adyen-hosted fields/iframe.** `*.adyen.com` in `connect-src` **and** `frame-src`; **no `form-action` directive is set at all**, so the card form does not self-post. Fields: card number, expiration date, CVV (per the card-update FAQ) | **Good** | ⚠️ `script-src` includes `'unsafe-inline'` **and** `'unsafe-eval'` — permissive for a page in PCI scope, and worth raising |
| **Payment methods visible** | **Insurance:** "Credit Card" primary, Apple Pay, plus a string for *"or other payment methods"*. **Pet Mart:** cards + Apple Pay + Google Pay; `dynamicCheckoutPrioritization: ["ApplePay","ShopifyPay","PayPal","AmazonPayCv2","GooglePay"]` (Shopify default ordering — PayPal and Amazon Pay configs are `null`, so not live) | **Fair** | No Hong Kong local rail on either |
| **Location-based method display** | ❌ **Not applicable / none.** Single market, single currency, HK-only fulfilment | **N/A** | Nothing to geo-adapt |
| **Instalment / EMI options** | ✅ **Native and zero-cost.** Monthly = **12 instalments, 1 down payment** on every plan, at **exactly 1/12 of the annual premium** (HK$222 × 12 = HK$2,664). **No surcharge for spreading the cost** | **Good** | 🔑 **Load-bearing for the volume gate.** Zero-surcharge monthly on a discretionary purchase, with 72.24% mobile-web traffic, materially raises likely monthly adoption. `[INFERENCE, not confirmed]` — adoption is unpublished |
| **3DS implementation** | **Not directly observed.** ⚠️ Pet Mart's Apple Pay config declares `merchantCapabilities: ["supports3DS"]` and its Google Pay config declares `allowedAuthMethods: ["PAN_ONLY","CRYPTOGRAM_3DS"]` — **but both are standard Shopify wallet configuration and are evidence about the Shopify store, not about the insurance checkout.** No 3DS version determined for the insurance flow | **Unknown** | Requires a DevTools walk |
| **PCI indicator** | **PSP iframe/hosted fields**, not self-hosted card fields — inferred from Adyen in `frame-src` plus the absent `form-action` | **Good** | See Section 9 |
| **Mobile responsiveness** | ⚠️ **Not tested** (no rendering in this environment). **72.24% of traffic is mobile web** — materially more than desktop | **Unknown — and this is the single biggest untested gap.** | Must be checked manually. On a mobile-dominant HK consumer flow, Apple Pay/Google Pay placement above the card form is usually the largest single conversion lever available |
| **Multi-currency / local pricing** | **Single currency: HKD.** `Shopify.currency = {"active":"HKD","rate":"1.0"}`; `paymentSettings.currencyCode: "HKD"`; statutory filing in HKD | **N/A** | No FX leg. Removes an entire Yuno value lever from this account |
| **Saved payment methods** | ✅ **Yes, and consented.** *"your credit card information will be saved for faster future checkouts and automatic policy renewals."* Dashboard supports multiple cards, a default card (*"You have successfully set the default credit card"*), *"Use a New Card"*, and deletion — but **a linked card cannot be deleted until a replacement is added** | **Fair** | Vault held at Stripe and/or Adyen per the Terms of Use. Multi-card + default-card UI is a decent foundation for a fallback-instrument strategy they do not appear to use automatically |
| **Error message clarity** | ✅ **Genuinely good, and specific** — distinct strings for invalid card number, insufficient balance, unsupported card type, CVC failure, transaction refused, expired card, plus a guided failure popup (*"If you are blocked with the payment, you can try the following method: 1. … 2. Contact our customer service if the issue persists."*) | **Good** | ⚠️ **But every remedy routes to customer action.** Clear messaging about a problem the platform could have solved silently |
| **Bundled-policy constraint** | ⚠️ *"If you're paying with Apple Pay, both policies must use the same billing cycle (either both annual or both monthly). If they differ, please pay by credit card instead."* | **Poor** | 🔑 **Directly collides with the stated strategy.** They intend to cross-sell fire and home cover into the pet book — and their own wallet checkout forces customers with mismatched billing cycles **off Apple Pay and onto manual card entry.** A self-imposed tax on the exact growth motion the CEO named in January |
| **Free trial** | A `"Free Trial"` string exists in the checkout bundle | **Unknown** | Implies a trial-to-paid first-charge event, which is the highest-risk charge in any recurring book. Not confirmed as live on any current plan |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| **PCI DSS Level** | **Not found.** No PCI DSS documentation, level, certification or Attestation of Compliance published | Searched; nothing found |
| **Card data handling** | **Likely SAQ A / SAQ A-EP** — see the inference below | `https://www.onedegree.hk/` (CSP) · `https://www.onedegree.hk/en-us/terms-of-use` |
| **Related certification** | **ISO 27001 — attaches to OneDegree Global (SG) Pte. Ltd., the B2B tech sister company, not to the licensed HK insurer.** Do not attribute it to OneDegree Hong Kong Limited | `[UNVERIFIED — search summary only, page not fetched]` (InvestHK client profile, dated 2021) |
| **Recommended Yuno integration** | **SDK** (drop-in / hosted fields) for the insurance flow, to preserve the reduced PCI scope they already have. ⚠️ **But note the real constraint:** migrating the **existing card-on-file vault** held at Stripe and/or Adyen is a PSP-to-PSP token migration project, not an SDK swap, and it is the hard part of any change here | — |

> `[INFERENCE, not confirmed]`: Based on confirmed use of **Adyen** with `*.adyen.com` in CSP `frame-src` and **no `form-action` directive**, card data is captured in an Adyen-controlled iframe or hosted field rather than posted to OneDegree's own domain. On that basis OneDegree's PCI scope is likely **reduced (SAQ A or SAQ A-EP)**, with Adyen handling card data. **No compliance level is stated anywhere publicly and none is claimed here.**

⚠️ **One observation worth raising on a technical call:** the `onedegree.hk` CSP sets `script-src` with both **`'unsafe-inline'` and `'unsafe-eval'`**, and the **live Adyen client key is exposed in an inline script variable**. The client key is designed to be public and origin-restricted, so that is not a vulnerability in itself. But `'unsafe-inline'` + `'unsafe-eval'` on pages in PCI scope is a weaker posture than the iframe boundary otherwise implies, and PCI DSS v4 script-integrity requirements for payment pages are the kind of thing a security-conscious insurer will already be thinking about. ⚠️ **Do not cite any specific PCI DSS v4 requirement or deadline — none was sourced in this run.** Raise it as a question, not a claim.

*No direct PCI compliance documentation found publicly for OneDegree.*

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: A 100%-auto-renewing card book is dunned on a fixed 3-day clock, and the 83%-of-premium product lines get the shortest clock**
> **Evidence:** **Section 4 + Section 5 + Phase 0 statutory filing.** Section 4: OneDegree's own live pet-plan catalogue shows **9 of 9 plans `"is_auto_renewable":true`**, Annual = 1 charge/yr, Monthly = 12 (`https://www.onedegree.hk/en-us/pet-insurance`). Section 5: their own FAQ publishes the dunning mechanic — *"the system will attempt to deduct the payment every three days until the grace period ends"*, with **30 days** for pet/turtle-bird/critical illness, **7 days** for home and home-appliances warranty, and fire *"automatically terminated"* if the premium is not collected before the next effective date (`https://www.onedegree.hk/en-us/faq/article/what-would-happen-if-i-miss-a-premium-payment`). Phase 0: **property damage is 83.4% of FY2025 gross premiums** — HK$276,705k of HK$331,910k (`https://odhk.blob.core.windows.net/common/25DS_en.pdf`).
> ⚠️ **The mapping of the statutory "property damage" class to the fire/home/appliance products is `[INFERENCE, not confirmed]`** — the filing does not break the class down by product name. Say "your property lines" on a call, not "83.4% of your premium is on a 7-day clock."
> **Pain Point:** A fixed 3-day retry is blind to *why* the payment failed. Retrying an **expired or reissued card** every three days for 30 days cannot succeed — the credential is gone, not temporarily short of funds — and the only published remedy is for the customer to log in and type a new card. Meanwhile the lines with the most premium behind them have 7 days or one shot. Every one of those lapses is a customer who still wanted the cover.
> **Yuno Value Proposition:** Network tokens and account updater inside the routing layer, so a reissued card refreshes **without the customer being asked** — which is the only thing that fixes the expired-credential case. Retry sequencing driven by decline code and issuer rather than a fixed 3-day tick, so soft declines are retried when they can actually clear and hard declines stop burning grace-period days. One view of failed renewals across providers instead of per-PSP dashboards — relevant because there are three providers here.
> **Best Success Case:** ⚠️ **None that is publicly referenceable and honest.** No published Yuno case study covers a single-market APAC recurring insurance book. Do not substitute a travel or gaming case. Build the case from their numbers in discovery — `subscription-payments.md` §5 questions, led by first-attempt renewal failure rate and recovery rate.
> **Outreach Angle:** Their own help centre publishes the retry cadence and the grace periods. That is the observation — not a claim about their performance, just a reading of what they published, and an open question about what the expired-card case does to a 91% renewal rate.
> **Suggested Subject Line:** `your 3-day retry and the expired-card case`

> **Insight #2: Three payment providers, two stacks, one legal entity — and the two stacks disagree about which cards a OneDegree customer may use**
> **Evidence:** **Section 3A + Section 4.** Adyen live on the insurance flow (`ADYEN_CLIENT_KEY='live_…'`, `ADYEN_ENVIRONMENT='live-apse'`, `*.adyen.com` in CSP `connect-src` and `frame-src` — `https://www.onedegree.hk/en-us/faq`); **Stripe** named by OneDegree alongside Adyen as *"Designated Payment Gateway"* for the card-storage service (`https://www.onedegree.hk/en-us/terms-of-use`); **Shopify Payments** live on Pet Mart with merchant of record *"OneDegree Hong Kong Limited"* (`https://store.onedegree.hk/payments/config`). Section 4: the insurance flow accepts **Visa, Mastercard, Amex, JCB, UnionPay** + debit; Pet Mart's UCP manifest enables **visa, master, american_express, discover, diners_club** — **no UnionPay, no JCB** — while Google Pay is live on Pet Mart and absent from insurance (`https://store.onedegree.hk/.well-known/ucp`).
> **Pain Point:** Same company, same customer, two different answers to "can I pay with this card?" The Pet Mart brand set is the stock Shopify Payments default — Discover and Diners enabled, UnionPay not — which is backwards for Hong Kong and was almost certainly never a decision. Card-on-file tokens are split across Stripe and Adyen, so a customer's stored credential lives in one vault, their pet-food purchases in another, and nothing reconciles acceptance performance across the three. Three providers is also three sets of reporting, three reconciliation paths and three contract negotiations for a 92-person company with 25% technical staff.
> **Yuno Value Proposition:** One integration and one token vault across both properties, so brand and wallet coverage is configured once rather than drifting per platform; the pet-retail and premium flows become comparable on approval rate and cost; and provider choice stops being a function of which platform a product happened to be built on.
> **Best Success Case:** ⚠️ None publicly referenceable for this profile. **NetEase Games** and **Garena** are the nearest nameable Yuno profiles on transaction shape only — APAC consumer, high-frequency card acceptance — **with no published metrics, so quote no figures**, and they match on volume pattern, not vertical.
> **Outreach Angle:** Their own terms name two gateways for one vault, and their two checkouts take different cards. Both facts are public and neither is likely to be a deliberate choice.
> **Suggested Subject Line:** `UnionPay on your policies, not on Pet Mart`

> **Insight #3: The #1 market is 76.90% of traffic, the checkout is card-only, and they have published that they intend to add methods**
> **Evidence:** **Section 1 + Section 4 + Section 7.** Section 1: Hong Kong is **76.90%** of visits (SimilarWeb, supplied 2026-10-09). Section 4: OneDegree's own payment-methods FAQ, **last published 2026-09-04**, enumerates cards and debit cards only, and **no FPS, PayMe, Octopus, AlipayHK or WeChat Pay HK appears on either stack** — Pet Mart's Shopify and UCP manifests enumerate handlers exhaustively and contain no local rail. Section 7: the same FAQ closes with *"We will continue to introduce more payment methods to provide you with additional options that meet your needs"* (`https://www.onedegree.hk/en-us/faq/article/what-payment-methods-do-you-accept`). FPS prominence per the **HKMA's own** inSight article of 2024-03-27: **13.6 million registrations at end-2023** against a 7.5 million population, **1.25 million transactions/day**, HK$9.0bn average daily value, *"more than 90% of Government departments accept the FPS"* (`https://www.hkma.gov.hk/eng/news-and-media/insight/2024/03/20240327/`).
> **Pain Point:** Two distinct costs. At **acquisition**, a card-only checkout behind a mandatory registration wall, on 72.24% mobile-web traffic, in a market where A2A is a default consumer behaviour. At **recovery**, a customer whose renewal card has declined has **no non-card way to pay and keep the policy alive** before a 7-day or 30-day grace window closes — the published remedy is "add another card", and if they do not have one to hand, the policy lapses.
> ⚠️ **Constrain this claim honestly:** FPS is a **push** rail and is not a drop-in replacement for an automatic card-on-file monthly debit. Hong Kong's eDDA may serve that purpose but **its suitability for recurring premium collection was not sourced** and must not be asserted. Pitch first-purchase conversion and failure recovery — not "replace your recurring rail."
> **Yuno Value Proposition:** One integration for local Hong Kong rails alongside the existing Adyen card flow, so the method list stops being a per-PSP project — and, specifically, a non-card recovery path a willing customer can actually use inside the grace window.
> **Best Success Case:** ⚠️ None publicly referenceable. Use the HKMA figures as market evidence and their own sentence as the trigger.
> **Outreach Angle:** They wrote the trigger themselves, five weeks ago, in their own help centre. Lead with their sentence, not with a lecture about FPS.
> **Suggested Subject Line:** `"we will continue to introduce more payment methods"`

> **Insight #4: The stated growth plan is more policies per customer — and their own checkout penalises exactly that**
> **Evidence:** **Section 6 + Section 8.** Section 6: FY2025 results (2026-01-19) — first full-year profit, revenue +38% to HK$330M, a stated target to **double total revenue within five years**, explicitly by *"recommending suitable fire or home insurance to pet insurance customers"*, with **a quarter of customers already holding more than one pet policy and one holding 16** (`https://www.hk01.com/財經快訊/60314167/`). Section 8: their own checkout bundle carries *"If you're paying with Apple Pay, both policies must use the same billing cycle (either both annual or both monthly). If they differ, please pay by credit card instead."* Plus: *"You can change your billing cycle only when you renew your policy"* and *"the payment debit date can't be changed."*
> **Pain Point:** The growth strategy is multi-policy households. The checkout's response to a multi-policy household with mismatched billing cycles is to **push them off Apple Pay and onto manual card entry** — on a 72.24% mobile-web book, where the wallet is the highest-converting instrument available. And because billing cycles only change at renewal and debit dates cannot move, a customer accumulating policies across the year accumulates **misaligned debit dates they cannot consolidate** — more charges, more failure surface, more chances for one decline to lapse one of several policies. Every incremental cross-sell makes the billing picture messier rather than simpler.
> **Yuno Value Proposition:** Orchestrating billing across multiple policies on one stored credential, so adding a policy does not fragment the payment relationship — wallet eligibility preserved regardless of cycle mix, and a single instrument with automatic credential refresh behind however many policies a household holds.
> **Best Success Case:** ⚠️ None publicly referenceable for a multi-policy insurance book. This one is best argued from their own numbers: a quarter of customers already hold more than one policy, and the CEO has said she wants that share to grow.
> **Outreach Angle:** The cross-sell strategy was stated publicly in January. The Apple Pay billing-cycle restriction is in their own checkout. Putting those two facts next to each other is the whole email.
> **Suggested Subject Line:** `the cross-sell plan and the Apple Pay cycle rule`

---

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks (one sentence each):**
1. Your help centre says the system retries a declined premium every three days until the grace period ends — which works for insufficient funds and can never work for a card that has been reissued.
2. Your terms name Stripe *and* Adyen as the gateway for stored cards, your insurance checkout takes UnionPay and JCB, and Pet Mart takes Discover and Diners but neither — three providers, two stacks, one entity.
3. Your payment-methods FAQ was republished on 4 September and ends with "we will continue to introduce more payment methods," on a Hong Kong checkout that currently has no FPS.
4. Fire policies terminate automatically if the renewal premium is not collected before the effective date, and home cover gets a seven-day grace — the lines with the most premium behind them have the least tolerance for a failed card.
5. You told the market in January you want to cross-sell fire and home into the pet book, and your checkout tells customers with mismatched billing cycles to stop using Apple Pay.

**Cold call openers (conversational, one sentence each):**
1. "I was reading your billing FAQs — you publish the three-day retry cadence and the grace periods, which is more than most insurers do; I wanted to ask what happens on the expired-card cases, because that's the one a retry can't fix."
2. "Quick one — your terms of use name Stripe and Adyen for the stored-card service; is that a migration in flight, or do both carry live tokens?"
3. "Your pet renewal rate was 91% last year on a book where every plan auto-renews — do you know what share of the 9% that didn't renew was involuntary rather than a customer choosing to leave?"
4. "Pet Mart's on Shopify Payments and the insurance side's on Adyen — was that a decision, or just how the two got built?"
5. "You're taking UnionPay on policies but not on Pet Mart — is that deliberate, or did the store just ship with Shopify's defaults?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| **Bowtie Life Insurance** | `bowtie.com.hk` | 🇭🇰 Hong Kong | Sun Life took a majority stake for a reported US$70M in July 2025 `[UNVERIFIED — search summary only]` | Hong Kong | **Not established.** First-hand: its marketing-site CSP (Webflow-hosted) contains **no payment-provider domain at all**, and sets `form-action 'self' www.facebook.com`. Checkout sits on a `*.bowtie.com.hk` subdomain outside that CSP's scope | CSP fetched 2026-10-09 from `https://www.bowtie.com.hk/` |
| **Avo Insurance** | not resolved (`avoinsurance.com` returned no response) | 🇭🇰 Hong Kong | Asia Insurance (Asia Financial Group) 51% / Zhang Lei 49% `[UNVERIFIED — search summary only]` | Hong Kong | **Not established** — site unreachable in this environment | — |
| **ZA Insure** (ZhongAn HK) | `za.group` (corporate) | 🇭🇰 Hong Kong | Operated by ZhongAn's HK unit; life licensee `[UNVERIFIED — search summary only]` | Hong Kong | **Not established.** First-hand: no payment signature on the corporate homepage | fetched 2026-10-09 from `https://za.group/` |
| **Petcare (HK)** | `petcarehk.com` | 🇭🇰 Hong Kong | Not found | Hong Kong | **Not established.** First-hand: WordPress site; the single `stripe` match was the CSS path `images/stripes/textline.png` — **a false positive** | fetched 2026-10-09 |

⚠️ **Honest limitation on 11A.** Hong Kong's virtual insurers are **four licensed players** (OneDegree and Avo on general licences; Bowtie and ZA Insure on life licences), so Bowtie and ZA Insure are **adjacent rather than direct** — they do not sell pet or property cover. OneDegree's true direct competitors in pet insurance are the **traditional HK general insurers' pet products**, which were **not** researched in this run; they are conventional insurers whose checkouts are typically broker- or bank-intermediated and not comparable. The licence-class and ownership details above all come from **search summaries, pages not fetched** — `[UNVERIFIED]`. **Verify licence classes against the Insurance Authority register before using any of this.**

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| **Bowtie** | `bowtie.com.hk` | Digital insurance (life/medical) | 🇭🇰 HK | Direct-to-consumer recurring premium, HK-only, card-based; same involuntary-churn mechanics and the same single-market ceiling | `https://www.bowtie.com.hk/` |
| **Avo Insurance** | not resolved | Digital insurance (general) | 🇭🇰 HK | D2C with no brokers or agents — the closest structural analogue to OneDegree | `[UNVERIFIED — search summary only]` |
| **ZA Insure** | `za.group` | Digital insurance (life/medical) | 🇭🇰 HK | Recurring premium, digital-only, ZhongAn-backed | `https://za.group/` |
| **Star Health** | — | Health insurance | 🇮🇳 India | **Publicly adopted orchestration for premium collection and recurring mandates** — the best same-vertical precedent found, though a different market. See 11C | `https://juspay.io/customer-stories/star-health-insurance` |

⚠️ **This section is thin and I am not going to pad it.** Section 11 is meant to generate pipeline, and OneDegree's peer set is a **four-company licensed market in one city**. There is no large APAC cohort of digital insurers matching this profile that was identifiable within this run's budget. The honest recommendation is in the pipeline table below.

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| **Star Health Insurance** | **Juspay** — payment orchestration with success-rate-based PSP routing, plus mandates (e-NACH, debit + e-NACH, UPI Autopay) for recurring premium collection | Date not stated on the case study | Health insurance, 🇮🇳 India | `https://juspay.io/customer-stories/star-health-insurance` |
| **Unnamed insurer** | **Airpay** — intelligent retry logic and dynamic routing across acquiring banks; the case study claims online premium failure rates fell from ~8% to under 1.5% | Date not stated | Insurance, 🇮🇳 India | `https://airpay.co.in/case-studies/re-architecting-insurance-payments-for-scale-in-a-digital-first-ecosystem` |

⚠️ **Both are vendor-published marketing material with no independent verification, in a different market with different rails (e-NACH and UPI Autopay do not exist in Hong Kong). Quote no figures from either.** Their value is narrow but real: they establish that **failed premium collection is a recognised, solved problem in insurance**, which is useful when a prospect's first reaction is "we're an insurer, not an e-commerce company."

> *No public case studies found of OneDegree's direct Hong Kong competitors adopting payment orchestration.* The **competitor using orchestration** ICP row therefore scores **0** — Star Health is not a OneDegree competitor.

#### 11D. Prospect Scoring

⚠️ **Not scored, deliberately.** Applying the 29-point matrix to Bowtie, Avo and ZA Insure would require researching each one's traffic, entities, PSP stack and transaction volume — a full research run each. **Every input I have on them is a `[UNVERIFIED]` search summary, and scoring an account from search summaries is precisely what this repo's integrity rules forbid.** Producing a table of invented scores would be worse than producing none.

What can be said without inventing anything: all three share OneDegree's **structural ceiling** — Hong Kong-only, HKD-only, card-based recurring D2C premium. On the matrix, each would almost certainly fail *high traffic outside home*, *3+ countries* and *local rail gap in a top-3 market* for the same reasons OneDegree does, and each would hinge on the same unsourced monthly transaction count. **The whole Hong Kong virtual insurer cohort is a Medium-at-best, volume-gate-dependent segment.** That is the useful finding for pipeline planning, and it is more honest than four fabricated scores.

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | **OneDegree** | Target | 🇭🇰 HK | **13/29** | 🟢 Medium | Three PSPs, two stacks, no orchestration; published 3-day retry on a 100%-auto-renewing book; own stated intent to add payment methods (2026-09-04) | ✅ **Yes** |
| 2 | **Bowtie Life Insurance** | Direct peer | 🇭🇰 HK | **Not scored** | ⚠️ Research first | Sun Life majority stake (reported July 2025) → post-acquisition infrastructure review is a classic window. Marketing site is Webflow with no PSP in CSP; checkout on a separate subdomain | ❓ **Not checked against the TAL in this run** |
| 3 | **Avo Insurance** | Direct peer | 🇭🇰 HK | **Not scored** | ⚠️ Research first | The closest structural analogue — D2C general insurer, no brokers or agents. Site was unreachable here, so start with a live fetch | ❓ Not checked |
| 4 | **ZA Insure** (ZhongAn HK) | Direct peer | 🇭🇰 HK | **Not scored** | ⚠️ Research first | ZhongAn-backed; a mainland parent may mean an existing China payment stack extended into HK — worth one CSP fetch | ❓ Not checked |

⚠️ **I am not filling six more rows to reach ten.** The method asks for genuine finds cross-checked against `accounts/apac-tal.csv`; I did not identify six further qualified prospects from this account's research, and inventing them would corrupt the pipeline. **The three peers above are the real output, and all three need a `/research` run before they are worth scoring or contacting.** None was cross-checked against the TAL in this run — that check is in Manual Research Recommendations.

---
