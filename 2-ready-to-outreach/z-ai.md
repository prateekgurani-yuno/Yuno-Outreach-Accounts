# z.ai (Zhipu AI / Z.AI Co., Ltd., HKEX: 2513)

**Status:** 🔴 **BLOCKED — compliance hold. Do not outreach until Yuno legal/compliance clears it.** Research complete; no outreach sequence generated, by decision.
**ICP Score:** 23 / 29 → ⭐ **High** — one of the strongest payment-fit profiles in this pipeline. **The score and the block are independent axes. Read both.**
**Industry:** AI / LLM model-as-a-service — prepaid API credits + auto-renewing developer subscriptions · **HQ:** Beijing, China · **Billing entity:** JINGSHENG HENGXING TECHNOLOGY PTE. LTD. (Singapore) · **Researched:** 2026-09-24 · **First email sent:** —
**Motion:** 🛑 BLOCKED (compliance hold) · IN-HOUSE when cleared
**Motion detail:** ⚠️ **IN-HOUSE — but an unusually thin one.** Two PSPs (Stripe + PayPal) behind a hand-rolled eligibility/preference layer. Respect the build; anchor on reach and localisation, never on "you need orchestration."

---

> ## 🛑 BLOCKING FLAG — Zhipu AI is on the US BIS Entity List, and a second rule lands in 46 days
>
> **I verified this myself against primary sources. It is not an agent claim and it is not from memory.**
>
> **1. The listing is real, and it is current.**
>
> Federal Register full-text search returns **exactly one** document mentioning "Zhipu" — the original rule. No removal, no modification, no later action.
>
> - **Rule:** *Addition of Entities to and Revision of Entry on the Entity List*, BIS · **90 FR 4617** · published & effective **2025-01-16**
>   https://www.federalregister.gov/documents/2025/01/16/2025-00704/addition-of-entities-to-and-revision-of-entry-on-the-entity-list
> - Verbatim rationale, read by me at govinfo (https://www.govinfo.gov/content/pkg/FR-2025-01-16/html/2025-00704.htm):
>
>   > *"These additions are being made because these entities advance the People's Republic of China's military modernization through the development and integration of advanced artificial intelligence research. This activity is contrary to the national security and foreign policy interests of the United States under Section 744.11 of the EAR. **A license is required for all items subject to the EAR, with a license review policy of a presumption of denial.**"*
>
> - **Still listed today.** I fetched Supplement No. 4 to 15 CFR Part 744 from the current eCFR (edition 2026-09-01) and grepped it: **seven Zhipu-named entries present, unchanged.** Verbatim alias block:
>
>   > *"a.k.a., the following two aliases: —**Zhipu AI**; and —**Beijing Knowledge Atlas Technology Co., Ltd.** Floor 10, Building 9, No. 1, Zhongguancun East Road, Haidian District, Beijing, 100080, China. For all items subject to the EAR. (See § 744.11 of the EAR) **Presumption of denial** 90 FR 4619, 1/16/25."*
>
>   Source: `https://www.ecfr.gov/api/versioner/v1/full/2026-09-01/title-15.xml?part=744`
>
> **2. ⏰ The 50% "Affiliates Rule" un-suspends on 2026-11-10 — 46 days from today.**
>
> Today, the Singapore billing entity is **not** automatically swept in by ownership. From 10 November 2026 it is, if it is ≥50% owned by the listed Beijing company. Verbatim DATES field from the suspension rule, read by me via the Federal Register API:
>
> > *"Effective November 10, 2025, the amendments to 15 CFR parts 732, 734, 736, 744, and 748 in the interim final rule published at 90 FR 47201, on September 30, 2025, are stayed until **November 9, 2026**."*
> > — *One Year Suspension of Expansion of End-User Controls for Affiliates of Certain Listed Entities*, **90 FR 50857**, pub. 2025-11-12. Abstract adds: *"The suspension is set to end November 9, 2026, **absent a future extension**."*
> > https://www.federalregister.gov/documents/2025/11/12/2025-19846/one-year-suspension-of-expansion-of-end-user-controls-for-affiliates-of-certain-listed-entities
>
> **So "contract with Singapore, not Beijing" is a solution with an expiry date on it** — and only if the ownership chain is under 50%, which the available reporting says it is not (*"间接全资子公司"* — indirect wholly-owned subsidiary).
>
> **3. What this is NOT.** Not OFAC SDN. Not OFAC Consolidated/NS-CMIC. Not DoD Section 1260H. Not UK OFSI. Not EU consolidated. Not BIS Denied Persons. *(Agent-verified against downloaded list files with sanity checks; I did not re-download these myself — see the verification ledger.)* Entity List = an **export licence requirement with presumption of denial** on items subject to the EAR. It is not an asset freeze, and it does not by itself bar a non-US company from contracting with them.
>
> **4. 🪤 A name-only screen will miss this company.** BIS lists *"Beijing Zhipu Huazhang Technology **Co., Ltd.**"*. The company has since converted to a joint-stock company and renamed its English brand **Z.AI Co., Ltd.** for the HK listing. BIS has not updated the entry. Anyone screening "Z.AI Co., Ltd." against the Consolidated Screening List gets a clean result. The identity chain is nailed by two independent facts: the Entity List address is **character-identical** to the address in the company's own IR footer, and the Entity List alias *"Beijing Knowledge Atlas Technology"* matches the **HKEX stock short name "Knowledge Atlas"**.
>
> ### My recommendation
>
> **Do not send anything until compliance answers one question:** does Yuno's service to this merchant involve items subject to the EAR — US-origin software, US cloud infrastructure, or US-person involvement — and if so, what happens on 2026-11-10?
>
> **That call belongs to Yuno legal and compliance, not to research or to sales.** I am deliberately not scoring this as a disqualification, because it isn't mine to make. But it is also not a footnote, which is why it sits above the research rather than inside it.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** z.ai is the **international** property of Zhipu AI — China's first major LLM company to IPO (HKEX: 2513, 8 Jan 2026). It sells prepaid API credits and auto-renewing **GLM Coding Plan** subscriptions from **$18/month**, priced exclusively in USD, to developers in 233 countries. Its Chinese business runs on entirely separate domains (`bigmodel.cn`, `chatglm.cn`) and is **not** in the traffic dataset — so **z.ai traffic ≈ Zhipu's outbound international business** and should be read that way throughout.

**SimilarWeb traffic:** supplied by Prateek 2026-09-24, `z.ai` incl. all country domains, **122 countries**. ⚠️ **Shares only — no absolute visit count supplied**, so monthly transactions cannot be derived from traffic. Full data: `accounts/traffic/z-ai.md`.

### Top markets against the accepted payment set
Accepted set is the same in every one of the 122 countries: **international card (Stripe) or PayPal where PayPal is available.** There is no geo-adaptation.

| Rank | Country | Traffic | Accepted | Missing | Local entity |
|---|---|---|---|---|---|
| 1 | 🇮🇳 India | **11.20%** ▼24.07% | Card (Visa/MC/Amex/JCB/UnionPay), PayPal | ❌ **UPI** ❌ netbanking ❌ RuPay ❌ EMI ❌ UPI Autopay for the recurring book | ❌ None |
| 2 | 🇺🇸 United States | **8.78%** ▼17.18% | Card, PayPal | ❌ ACH ❌ Apple/Google Pay | ❌ None |
| 3 | 🇨🇳 China | **8.33%** ▲**38.24%** | Card, PayPal | ❌ Alipay ❌ WeChat Pay — *absent from the **international** property; the CN platform has them* | ✅ Beijing parent (separate platform) |
| 4 | 🇷🇺 Russia | **6.87%** ▲3.76% | — | ❌ **Effectively nothing serviceable.** Stripe does not acquire in Russia; PayPal exited. ❌ Mir ❌ SBP | ❌ None |
| 5 | 🇮🇩 Indonesia | **5.57%** ▼32.55% | Card, PayPal | ❌ **QRIS** ❌ virtual account ❌ GoPay/OVO/DANA ❌ Alfamart/Indomaret | ❌ None |
| 6 | 🇪🇬 Egypt | **5.04%** ▲3.53% | Card, PayPal | ❌ Meeza ❌ Fawry ❌ mobile wallet — *EMEA territory; corridor evidence only* | ❌ None |
| 7 | 🇻🇳 Vietnam | 4.44% ▼**55.49%** | Card, PayPal | ❌ MoMo ❌ ZaloPay ❌ VNPay/VietQR ❌ NAPAS | ❌ None |
| 8 | 🇧🇩 Bangladesh | 3.87% ▼6.74% | Card, PayPal | ❌ bKash ❌ Nagad — **PayPal does not operate in Bangladesh** | ❌ None |
| 9 | 🇵🇰 Pakistan | 3.03% ▼38.57% | Card, PayPal | ❌ JazzCash ❌ Easypaisa — **PayPal does not operate in Pakistan** | ❌ None |
| 10 | 🇧🇷 Brazil | 2.60% ▼27.08% | Card, PayPal | ❌ **Pix** ❌ boleto ❌ parcelamento | ❌ None |
| 13 | 🇹🇭 Thailand | 1.66% ▼29.69% | Card, PayPal | ❌ PromptPay ❌ TrueMoney | ❌ None |
| 18 | 🇰🇷 Korea | 1.23% ▼41.26% | Card, PayPal | ❌ KakaoPay ❌ Naver Pay ❌ Toss ❌ local card PG | ❌ None |

⚠️ **Egypt, Russia and Brazil are out of APAC territory.** z.ai is China-HQ'd so the *account* is in scope per `CLAUDE.md`; those rows are corridor evidence, not an EMEA/LatAm claim.

### Legal entities
- ⭐ **JINGSHENG HENGXING TECHNOLOGY PTE. LTD.** — **Singapore, UEN 202346299M**, incorporated 23 Nov 2023, formerly *ZHIPU HENGYAO TECHNOLOGY*. **This is the contracting party, biller and data controller for international z.ai.** Verified by me in z.ai's own Terms of Use and Privacy Policy. Corroborating operational tell: peak-hour pricing windows are defined in **Singapore Standard Time (UTC+8)**.
- **Z.AI Co., Ltd. / 北京智谱华章科技股份有限公司** — Beijing. HKEX Main Board **2513**, stock short name **"Knowledge Atlas"**. **The BIS Entity-Listed party.** Verified by me in the HKEX filing.
- **Corethinks Technology SDN. BHD.** (Malaysia) and **ZYNIX LIMITED** (UK) — `[UNVERIFIED — single Chinese secondary source]`.
- ⚠️ **The ownership chain Singapore→Beijing is NOT confirmed from a primary filing.** Chinese reporting calls it an *indirect wholly-owned subsidiary*; the HK IPO prospectus subsidiary list would settle it and was not retrieved. **This is the one gap that matters most for the compliance question.**

### Known PSPs — exactly two, and I verified both first-hand
| Rail | Evidence (mine) | Coverage |
|---|---|---|
| **Stripe** | Live publishable key `pk_live_51Rh0IhRp8MKof9Wn…` in the billing bundle; `react-stripe-js` with `CardNumberElement`, `confirmCardSetup`, `confirmCardPayment`, `requiresAction` 3DS handling → **z.ai captures card data itself, not a hosted redirect**; endpoints `/pay/stripe/{recharge,pay,check,invoicePay,bind,query,unbind}` | Primary rail, all markets |
| **PayPal** | Endpoints `/pay/paypal/{isSupport,setupToken,subscribe}`. **`isSupport` is a geo/eligibility pre-check** → PayPal is not offered everywhere | Secondary, geo-gated |

**Orchestrator: NONE of Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY or Yuno.** Also absent: Adyen, Checkout.com, Antom/Alipay+, Airwallex, PingPong, PayerMax, Paddle. What exists instead is **hand-rolled**: `/pay/authorized/payment-types` serves a `payTypes` array, `/pay/preference/{get,add}` stores a chosen default, transaction records branch on `paymentChannel === "PAYPAL" ? "PayPal" : "Card"`, and a runtime guard warns *"Auto-recharge requires a Stripe payment method."* Two rails, reconciled separately, with eligibility logic they wrote themselves.

### The three findings that would open a conversation
1. **3DS is not supported — they say so themselves.** Verified verbatim by me at `docs.z.ai/help/faq.md`: *"When using a credit card to recharge, please ensure that you are not using 3DS verification. **3DS verification is not supported in our platform at this moment.**"* For a merchant billing India, Indonesia, Brazil and the EU, that is not a preference — it is a structural decline source.
2. **Two verified lost sales, in public, from their own buyers.** Both fetched and read by me via the HN API.
3. **The billing core is China-domestic, extended outward.** `api.z.ai/api/biz/overseas/team/subscribe/product/public_pricing` is live and unauthenticated, returns Chinese `purchaseMethodName` values (`连续包月`, `连续包年`, `按月采购`, `按季采购`) — and **has no `currency` field at all.**

</details>

<details>
<summary><h2>✉️ Section 2 — Full Outreach Sequence</h2></summary>

## ⛔ Not generated — by decision, not by omission.

`/full-outreach` was **not** run on this account. The BIS Entity List status is unresolved and the Affiliates Rule reimposes on 2026-11-10. Drafting a 12-touch sequence for a merchant that compliance may rule undeliverable wastes the work and risks it being sent.

**The sequence is cheap to generate once the block clears.** Run `/full-outreach z.ai` at that point. The angle is already settled by the research:

- **Motion is in-house, so respect the build.** They wrote their own eligibility layer over two PSPs. Never suggest they need orchestration.
- **Lead on the 3DS admission**, in their own words, against the India/Indonesia/Brazil traffic mix. It is their sentence, not our claim.
- **Second bullet is the localisation asymmetry**, not a missing-rail list: they run a separate USD price book, Singapore-time pricing windows and a dedicated international entity — i.e. they built a genuine international business — and then accept payment in exactly one way in all 122 countries.
- **Third bullet is the reseller leakage**, which is quantified and theirs: 19 GLM model IDs on OpenRouter, `z-ai/glm-5.3` served by **34 endpoints**, Z.AI's own priced **$1.40/M** against Baidu at **$0.561/M** and DeepInfra at **$0.562/M** — and `z-ai/glm-5.3-prime` served by **Alibaba only**, not by z.ai at all.
- **Do not pitch API token volume.** Aggregators have it. Pitch the **subscription book** — recurring, card-on-file, 122 countries, USD-only, and contractually un-resellable by their own terms (below).

</details>

<details>
<summary><h2>🔍 Section 3 — Full Research</h2></summary>

## 1. ICP Score Breakdown — 23 / 29 ⭐

| Signal | Max | Awarded | Basis |
|---|---|---|---|
| Transaction volume / company size | 5 | **5** | HKEX-listed, ~**US$47bn** market cap (465,623,090 shares × HK$793 close, both from the primary filing). H1 2026 revenue **RMB 953.89m**, +399.7% YoY, of which **MaaS = RMB 825.18m (86.5%)**. 7.4m platform users, 233 countries, paying DAU **+603%** YTD. Entry ticket **$18/month** → high-count, low-ticket book. ⚠️ Driven by company size and business model, **not** by a disclosed international transaction count — see §4. |
| Orchestration status | 4 | **1** | **In-house.** Hand-rolled two-PSP eligibility/preference layer, verified in their own bundle. |
| Operates 3+ countries | 3 | **3** | **122** countries in traffic; company claims **233 countries and regions**. |
| Multiple PSPs | 3 | **3** | Stripe + PayPal, separately reconciled (`paymentChannel` branch). ⚠️ The weakest qualifying form of this signal — two global PSPs, not a fragmented estate. |
| Local rail gap | 3 | **3** | **Zero local methods anywhere.** Strongest possible award — see §3. |
| Recent expansion | 2 | **2** | Sept 2026 raise; use of proceeds names *"MaaS platform, API, **Coding Plan**"* — verbatim from the filing, read by me. CEO stating a shift to overseas cost-performance selling and CSP partnerships. |
| Known payment issues | 2 | **2** | Two verified public lost sales + a self-published 3DS non-support statement. |
| Recent funding | 2 | **2** | ~**US$5.0bn net in a single day**, 12 Sept 2026 (H-share placing at HK$714.00 + **zero-coupon** CB). Primary filing, verified by me. |
| Traffic outside home market | 2 | **2** | China is **third at 8.33%**; ~92% of visits non-China; no country above 11.2% across 122. Widest margin of any account in this pipeline. |
| Competitor orchestration | 2 | **0** | **None found.** No AI/LLM API provider publicly uses an orchestrator. Moonshot has `NEXT_PUBLIC_AIRWALLEX_ENV` provisioned — an inference from an env var, not a case study. |
| Payment job postings | 1 | **0** | None found. |
| **Total** | **29** | **23** | ⭐ **High** |

**Honest note on the score.** 23/29 makes this the second-highest-scoring account in the pipeline. It is also the only one with an unresolved export-control question. **The matrix measures payment fit. It has no compliance row.** Do not let 23/29 carry this past the block at the top of the file.

## 2. The stack, in their own code

`z.ai/payment` returns 200 and loads 36 chunks. Live endpoint surface (I probed three; all returned `{"code":1001,"msg":"Authentication parameter not received in Header..."}` — live and auth-gated, not dead code):

```
/pay/stripe/recharge   /pay/stripe/pay   /pay/stripe/check   /pay/stripe/invoicePay
/pay/stripe/bind       /pay/stripe/query /pay/stripe/unbind
/pay/paypal/isSupport  /pay/paypal/setupToken  /pay/paypal/subscribe
/pay/authorized/payment-types    /pay/preference/get    /pay/preference/add
/pay/user/refund/{preview,status,submit}    /pay/user/unsubscribe
```

Card copy, verbatim: *"Pay securely using Visa, Mastercard, American Express, JCB or UnionPay card."*

**The billing core is Chinese and was extended, not rebuilt.** `api.z.ai/api/biz/overseas/team/subscribe/product/public_pricing` — live, unauthenticated — returns `purchaseMethodName` values in Chinese (`连续包月` continuous monthly, `连续包年` continuous annual, `按月采购` monthly purchase, `按季采购` quarterly purchase) and carries **no `currency` field**. The path segment is literally `overseas`. A China-domestic subscription core with an international skin on it.

## 3. Local payment methods — zero, and I disproved every apparent hit

Their own FAQ states the accepted set: charges fall to *"your linked payment method (e.g., **bank card or PayPal**)"*. No local rail appears anywhere in the bundles.

**Five apparent hits, all false positives, all context-printed before rejection:**

| Apparent | Actual | Note |
|---|---|---|
| UPI | `classGroupId` (tailwind-merge) | ⭐ **New false positive for the running list** |
| Pix | `devicePixelRatio` | known |
| WeChat Pay | browser user-agent detection | known |
| Apple Pay | `ApplePaySession` — FingerprintJS capability probe | known |
| iDEAL | substring of ordinary English copy | known |

⚠️ **CSP methodology:** z.ai sends **no `form-action` directive**, so CSP absence is *not* usable as sourced evidence of rail absence here. The absence claim rests on the bundle enumeration **plus** their own FAQ stating the accepted set — a positive statement, which is stronger.

**What that costs them, market by market:** India (11.20%) has no UPI, the rail that carries the majority of Indian online payments. Indonesia (5.57%) has no QRIS and no virtual account. Vietnam (4.44%), Bangladesh (3.87%) and Pakistan (3.03%) have no local wallet — **and PayPal does not operate in Bangladesh or Pakistan at all**, so those buyers have exactly one option: an international card. Russia (6.87%) has neither rail serviceable. Brazil (2.60%) has no Pix. That is **~37% of traffic in markets where a USD-card-only checkout is the worst-performing option available.**

## 4. Volume — clears the gate, but the denominator is genuinely undisclosed

**The 40,000/month gate does not fire.** It fires only on a *sourced* figure under 40,000. No such figure exists — and the scenario range straddles it only at the most pessimistic corner.

Billing-unit mechanics matter here more than revenue, and they all **suppress** transaction count. All verified by me in z.ai's own docs:

- **Subscriptions auto-renew** → monthly plan = 1 transaction/month; **annual = 1 per year**, and annual is pushed at 30% off.
- **The charge waterfall means many renewals generate no payment transaction at all.** Verbatim, `docs.z.ai/devpack/faq`: *"1. Credits balance will be used first. 2. If insufficient, cash balance will be used. 3. If still insufficient, the remaining amount will be charged from your linked payment method (e.g., bank card or PayPal)."*
- **Prepaid top-ups:** one top-up = one transaction regardless of how many API calls it funds. Denominations **not published**.
- 🔎 **A card-minimum round-up exists**, verbatim: *"a small minimum applies when charging your credit card. If the remaining amount is less, we will round up the deduction to meet this minimum."* Worth a discovery question — that is a merchant working around card economics by hand.

| Input | Value | Label |
|---|---|---|
| Group H1 2026 MaaS revenue | RMB 825.18m | **SOURCED** |
| → monthly average | RMB 137.53m ≈ **US$19.6–20.5m** | **DERIVED** |
| z.ai (international) share of that | **NOT DISCLOSED** | ⚠️ **No public information found** |
| Blended average successful charge | $25 / $40 / $80 tested | **ASSUMED** |

| z.ai share *(assumed)* | @ $25 | @ $40 | @ $80 |
|---|---|---|---|
| 10% | 78–82k | **49–51k** | 25–26k |
| 25% | 196–205k | **123–128k** | 61–64k |
| 40% | 314–328k | **196–205k** | 98–102k |

**Break-even against 40,000/month:** needs the international share to be ~**8%** at a $40 ticket, ~**16%** at $80. Given China is only 8.33% of z.ai traffic, z.ai prices exclusively in USD, and the whole property is the international one, the international share almost certainly clears that. `[INFERENCE, not confirmed]`

⚠️ **Never put a transaction number in outreach.** The denominator is undisclosed, deliberately — the company publishes growth *rates* (603%, 40×, 23×, 98×, +101% ASP) and no absolute bases.

**Volume that is NOT orchestration-relevant:** the On-Premise segment (RMB 128.72m H1 2026, and *falling* 54.6% YoY) is invoiced project revenue, not card volume. Ignore it.

## 5. Pricing and currency

**PRIMARY, `docs.z.ai/guides/overview/pricing`, read by me:** *"This page provides pricing information for Z.AI's models and tools. **All prices are in USD.**"*

**GLM Coding Plan.** Price floor is primary, from `docs.z.ai/devpack/overview`: *"**Starting at just 18 USD per month**, with Pro and Max plans designed for high-frequency, complex projects."* Quota tiers are primary — Lite 2,000 credits/5h & 10,000/week · Pro 12,000 & 60,000 · Max 28,000 & 140,000.

⚠️ **Pro/Max prices of $80/$168 are `[UNVERIFIED — not confirmed on a z.ai page]`.** `z.ai/pricing` and `z.ai/subscribe` fetch plan data client-side; the RSC payload carries only the meta description (*"Plans from 18/month"*). Two third-party trackers give $18/$80/$168 and are credible **because their quoted credit allowances match z.ai's primary docs exactly** — but that is corroboration, not confirmation. A third tracker gives $80→$72/$168→$160 and is stale. **Do not quote a Pro or Max price in outreach.**

**Peak/off-peak:** peak is Mon–Fri 14:00–18:00 **Singapore Standard Time (UTC+8)**; off-peak is charged at 50% of standard credits. Another tell that Singapore runs this.

**Team Plan** (`docs.z.ai/devpack/teamplan`) — **price not published**. Two things in it matter: *"Centralized billing and invoicing… Verified enterprises can request special VAT invoices"* — **增值税专用发票 is a PRC tax instrument**, so the Team Plan billing rail may run through the Beijing entity rather than Singapore, which is directly relevant to the compliance question. And it carries **on-demand overage** at a 10% discount to API list price → **variable-amount recurring charges**, not a flat subscription.

## 6. The contract terms that define the opportunity

All read by me at `docs.z.ai/legal-agreement/subscription-terms`:

- **Auto-renew:** *"Paid Subscriptions **renew automatically** at the end of each subscription term, and your Payment Method will be charged for the renewal term."*
- **Non-refundable:** *"Except where required by law or explicitly stated, all payments are **non-refundable**."*
- **They already accept third-party billing rails in principle:** *"If you subscribe through a third-party distributor (e.g., an app store), your payment, billing, and refund terms are governed by the distributor's policies."*
- 🎯 **They know they carry processor risk, and they say so in the plural:** *"Z.ai is not liable for errors or issues caused by third-party payment **processors**."*
- 🎯 **The subscription book is contractually protected from the aggregators:** *"Unless otherwise agreed in writing, you may not **resell, sub-resell, repackage, aggregate, proxy** or otherwise provide the GLM Coding Plan to any third party… nor may you use the GLM Coding Plan to provide model capabilities as a service to third parties."*

**Why that last clause is the whole commercial thesis.** The pay-as-you-go API token business is being eaten by aggregators (§8). The subscription book cannot be, by z.ai's own terms. So the orchestratable volume is **recurring, card-on-file, 122 countries, USD-only, Stripe-or-PayPal-only, auto-renewing, non-refundable, with renewal failure as the churn mechanism** — a smaller TAM than the ARR headline implies, and exactly the shape orchestration improves.

## 7. Verified payment failures

**Both fetched and read by me via `hacker-news.firebaseio.com`. Verbatim.**

**① 2026-08-28, user `csomar` (item 49475556, reply to 49474891):**
> *"I don't see it as much as before but recently I had issues with paying z.ai with my card and the only payment alternative they have is PayPal. PayPal now requires an account with a verified phone number just to process your payment, so it's strictly a no-go for me."*

This is `/pay/paypal/isSupport` failing in the field: card declines, PayPal is the only fallback, PayPal is unusable, sale lost.

**② 2026-01-18, user `dust42` (item 46665745, reply to 46664631):**
> *"I just wanted to give z.ai a try and buy some credits. I used Firefox with uBlock and the payment didn't go through. I tried again with Chrome and no adblock, but now there is an error: **"Payment Failed: p.confirmCardPayment is not a function."** The irony is, that this is certainly vibe-coded with z.ai which tries to sell me how good they are but then not being able to conclude the sale."*

⭐ **This one is self-corroborating.** `confirmCardPayment` is the exact `react-stripe-js` call I independently found in their production bundle. A buyer hit it as an unhandled JS error at checkout. **The hand-rolled layer broke in public.**

**③ Self-published, `docs.z.ai/help/faq.md`, verbatim:** *"When using a credit card to recharge, please ensure that you are not using 3DS verification. **3DS verification is not supported in our platform at this moment.**"*

⚠️ `[UNVERIFIED — could not fetch]` GitHub issue `zai-org/GLM-5#148` (reported as payment captured but credits never provisioned, open 13 days unanswered). **This session's proxy scopes GitHub to the working repo, so I could not reach it and cannot confirm it exists.** Do not use it in outreach. Also unverified from the same batch: three 2026 price rises, the January sign-up throttle, and the 钛媒体 *"passport tax"* / *"智谱让微信支付宝躺赢了"* story about overseas developers opening Alipay/WeChat accounts to buy the cheaper China-region plan. **That last one is worth Prateek's time to verify** — if true, it is buyers routing around the international checkout to reach the domestic one, which is the sharpest possible version of this account's problem.

## 8. Aggregator leakage — measured, and it reshapes the pitch

All figures from OpenRouter's public APIs, queried by me.

- **19 `z-ai/*` model IDs** on OpenRouter (22 counting variants), against DeepSeek 16, Moonshot 8, MiniMax 8 in a 458-model catalogue. ⚠️ **I am dropping the "4th-largest author" ranking the research reported**, because it is internally inconsistent: 19 cannot rank ahead of the Anthropic count (28) given in the same list. The count is verified; the ranking is not.
- **`z-ai/glm-5.3` is served by 34 endpoints.** `glm-5.3-flash` by 31 — InferenceNet, DeepInfra, Novita, Fireworks, Together, BaseTen, CoreWeave, Cloudflare, SiliconFlow, Alibaba, Baidu, Mistral and ~20 more. **Z.AI is one of them, mid-list on price.**
- **Z.AI's own endpoint is not the cheapest way to buy its own model:** Z.AI **$1.40/M** vs Baidu **$0.561/M** vs DeepInfra **$0.562/M**. Under OpenRouter's default price-and-uptime routing, z.ai loses most of its own aggregator volume.
- **`z-ai/glm-5.3-prime` has exactly one endpoint: Alibaba. z.ai does not serve its own newest flagship there at all.**
- GLM weights are open (`zai-org/*` on Novita and Fireworks), which is *why* ~30 companies can serve them.
- On transactions that do reach GLM via OpenRouter, **OpenRouter is the merchant of record, not z.ai.**

**Consequence, stated plainly: do not pitch API token volume.** Pitch the subscription book, which §6 shows no aggregator may touch.

⚠️ **No direct-vs-aggregator revenue split is public** for z.ai or any peer. The leakage is demonstrated qualitatively and quantified only on OpenRouter — a floor, not a total.

## 9. Competitors and their stacks — the peer answer cuts against the obvious pitch

| Company | Processor | Currency | Local APMs | Orchestrator |
|---|---|---|---|---|
| **z.ai** *(target)* | Stripe + PayPal | USD only | **none** | in-house, 2 rails |
| **Moonshot AI / Kimi** | Stripe (hosted redirect); **Airwallex provisioned** | USD | none *(intl)* | none |
| **MiniMax** | Stripe + bank transfer | USD ("all payments are in USD") | none | none |
| **DeepSeek** | **not named anywhere public** | USD | Alipay/WeChat (CN) | none |
| **01.AI** | n/a — exited model APIs Mar 2025 | — | — | — |

**The expected answer was "peers are China-rails-only." That is wrong.** Moonshot and MiniMax both run Stripe, USD and real international cards — **the same stack as z.ai, with the same gap**. So z.ai is not behind its peers on acquiring; it is level with them.

**That makes the story better, not worse.** The unsolved problem in this vertical is not "can't accept cards" — it is **card-only in markets where cards are the minority rail**, and *nobody* in the peer group has localised. Yuno would not be fixing a broken checkout; it would be the first localisation move in a vertical where all four leaders are leaving approval rate on the table in exactly the emerging markets driving their growth.

**No orchestrator has a named customer in this vertical.** That means no competitor has claimed the category — and equally that **Yuno has no social proof to lean on here.** `/full-outreach` E4 will need a Tier-2 (same payment pattern) or Tier-3 case, not a Tier-1 industry match.

**DeepSeek's opacity is itself a finding.** A whole reseller ecosystem — virtual cards, crypto bridges, proxied API keys — exists specifically to get money to Chinese AI labs. That is demand leaking to intermediaries because direct acquiring doesn't reach the buyer. ⚠️ **But every source making specific claims about DeepSeek's methods is one of those resellers, and they profit from the claim.** Do not put a named DeepSeek PSP in outreach.

## 10. Financials

| Period | Revenue (RMB m) | Gross profit | Operating income | Net income |
|---|---|---|---|---|
| **H1 2026** | **953.89** | 251.61 | −2,147 | −2,021 |
| H2 2025 | 533.46 | 200.12 | −1,897 | −925.2 |
| H1 2025 | 190.88 | 95.42 | −1,899 | −993.28 |
| H2 2024 | 267.51 | 153.57 | −1,525 | −806.47 |

H1 2026 segments: **Cloud/MaaS RMB 825.18m · On-Premise RMB 128.72m.** Gross margin moved from −0.4% to +24.6%. MaaS share of revenue went **26.3% → 86.5%** as enterprise general-model revenue *fell* 54.6%.

⚠️ **Source caveat:** these come from stockanalysis.com (independent aggregator) and Chinese press quoting the interim results announcement verbatim. The two agree exactly, but **neither is the filing.** I could not locate the H1 2026 interim results PDF on HKEXnews.

**⚠️ Push back on a number you will encounter.** Search summaries circulate *"2025 revenue reached 7.24 billion yuan."* **Wrong by 10×.** FY2025 = 190.88 + 533.46 = **RMB 724.34m** — 7.24 *亿*, not 72.4 亿. Do not let that into any outreach.

**Capital raised, from the primary HKEX filing (verified by me, `2026091300025.pdf`):** H-share placing of up to 21,965,000 new H shares at **HK$714.00**; concurrent **zero-coupon** USD-settled convertible bonds due 2027; **~US$5.0bn combined net proceeds in a single day**, 12 Sept 2026. Shares in issue 465,623,090; 11 Sept close HK$793.00 → **~US$47bn market cap** (my arithmetic on primary inputs).

**Use of proceeds, verbatim from the filing:** *"…**MaaS platform, API, Coding Plan** and Agent and Co-work related products and services, and to build an open and collaborative developer and business ecosystem around its technologies…"* — **the buying trigger is in the filing.**

## 11. Verification ledger — what I checked myself vs. what I did not

**Verified first-hand by me, this session:**
- BIS Entity List rule at govinfo; Federal Register full-text count (**exactly 1** Zhipu document); **current** eCFR Supplement No. 4 to 15 CFR 744 (7 Zhipu entries, alias block, presumption of denial); Affiliates Rule suspension DATES field via the FR API
- HKEX filing `2026091300025.pdf` — issuer name, stock code 2513, HK$714.00, 465,623,090 shares, zero-coupon CB, use-of-proceeds text
- z.ai's own docs: subscription terms (auto-renew, non-refundable, resale ban, processor-liability disclaimer, distributor clause); `devpack/faq` charge waterfall + card-minimum round-up; `guides/overview/pricing` USD line; `devpack/overview` $18 floor, quota tiers, Singapore-time peak window; `help/faq.md` 3DS non-support
- Singapore billing entity named in Terms of Use and Privacy Policy
- The payment stack: live Stripe publishable key, 36 chunks, `/pay/*` endpoint surface, three endpoints probed for liveness, `paymentChannel` branch, `payTypes` guard
- `public_pricing` endpoint — Chinese `purchaseMethodName` values, no `currency` field
- All five apparent local-method hits disproved by context-printing
- Both Hacker News items, via the HN API

**NOT verified by me — treat accordingly:**
- OFAC / DoD 1260H / UK OFSI / EU / BIS DPL negative results (agent-downloaded list files with sanity checks; methodology sound, not re-run by me)
- ACRA registry details for UEN 202346299M (two agreeing ACRA mirrors; **BizFile+ itself Cloudflare-blocked**)
- **The Singapore→Beijing ownership chain** — Chinese secondary reporting only. ⚠️ **The single most important open item.** The HK IPO prospectus subsidiary list would settle it.
- H1 2026 financials (aggregator + press, not the filing)
- Pro/Max subscription prices ($80/$168)
- Pre-IPO funding history, IPO pricing, STAR Market plans (search summaries)
- GitHub issue `zai-org/GLM-5#148` — **unreachable, existence unconfirmed**
- Malaysia and UK subsidiaries
- Competitor stacks (Moonshot/MiniMax/DeepSeek) — agent bundle-mining, methodology sound, not re-run by me
- Which acquirer sits behind Stripe, the settlement currency, and whether `payTypes` holds anything beyond STRIPE and PAYPAL

## 12. Next actions

1. 🛑 **Compliance first.** Put the Entity List status and the 2026-11-10 Affiliates Rule date to Yuno legal. Nothing else proceeds until that returns.
2. **Pull the HK IPO prospectus subsidiary list** to settle the Singapore ownership chain — it is the one primary document that decides whether the Singapore entity is caught on 10 November.
3. **Add to the TAL** — z.ai is not currently on it. Recommended: **P1, orchestrator = "in-house (Stripe+PayPal)", HQ = China.**
4. **Consider three new TAL rows from the competitor sweep:** Moonshot AI / Kimi (**P1** — Airwallex already provisioned, so a payments team exists and has made a vendor decision), MiniMax (**P1** — HKEX-listed, Stripe-only, USD-only, confirmed from its own ToS), DeepSeek (**P2 on reachability, not on fit**). ⚠️ **All three are China-HQ'd and carry the same compliance question as z.ai — check before adding.** Also flagged: SiliconFlow (China-HQ inference host, in territory).
5. **Verify the 钛媒体 "passport tax" story.** If overseas developers really are opening Alipay/WeChat accounts to buy the China-region plan, that is buyers routing around the international checkout — the single best hook in the account.
6. **Do not run `/full-outreach`** until item 1 clears.

## 13. Methodology notes for the pipeline

- ⭐ **New false positive for the running list: `classGroupId` (tailwind-merge) → UPI.**
- ⚠️ **Scratchpad cross-contamination happened twice this session** — an "Airwallex" hit from Moonshot pages leaked into a z.ai grep, and earlier a "LINE Pay" hit from an airline account leaked into Cygames. Both were caught only by context-printing every hit. **Recommend per-account scratchpad scoping for agents.**
- **The repo-scoped GitHub proxy is a real research limit.** `curl` to `github.com/<any other repo>` returns a 403 with a repo-scope message, not a network error. Third-party GitHub issues are effectively unreachable for research in this environment unless the repo is attached.
- **CSP `form-action` rule held again:** z.ai sends none, so CSP absence proved nothing here. The absence claim rests on bundle enumeration plus the merchant's own published accepted-method list.

</details>
