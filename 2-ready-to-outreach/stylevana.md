# Stylevana

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 13 / 29 → 🟢 **Medium**
**Industry:** Cross-border e-commerce (Korean & Japanese beauty) · **HQ:** Hong Kong · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** **Greenfield** — three payment integrations wired directly into Magento with no routing layer between them. The classification is affirmative, read out of their own live front-end config.

---

> ## 🎯 THE HOOK — twenty storefronts, one currency
>
> Stylevana runs **20 localised storefronts** — `de_DE`, `fr_FR`, `es_ES`, `it_IT`, `pl_PL`, `nl_NL`, `hu_HU`, `cs_CZ`, `pt_PT`, `ar_AE`, `es_MX`, `en_MY`, `zh_HK`, `en_AU`, `en_NZ` and more. And from their own payment page, verbatim:
>
> > *"**Payments on STYLEVANA are all processed in USD.** If your credit card requires currency conversion, you may be charged exchange rates and transaction fees by your bank and/or payment gateway. **STYLEVANA are not liable for these charges** as they are not processed, or received by us."*
>
> Twenty localised shopfronts, **one settlement currency, and the FX cost handed to the shopper in writing.** The same page repeats the disclaimer three more times, once under each method.
>
> **The method list is just as thin.** Their enumerated payment page offers **Visa, Mastercard, American Express, PayPal, Google Pay and Apple Pay.** That is the entire list. No JCB, no UnionPay, no Discover, no Diners. Nothing local in any of the twenty markets.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Stylevana is a Hong Kong cross-border e-commerce retailer shipping Korean and Japanese beauty products worldwide, running on **Magento (Adobe Commerce)** across 20 localised storefronts. The business model is close to YesStyle's: Asian beauty, outbound from Hong Kong, heavy EU and US demand, priced and settled in USD.

**SimilarWeb total visits:** **Not obtained.** No data supplied and no MCP tools in this environment. **The country profile is therefore unverified and I have not invented one** — this costs two ICP signals outright and is the single biggest gap in this file.

### Markets
Twenty locales are live and enumerated in their own storefront switcher:

| Region | Locales |
|---|---|
| **Europe** | `de_DE` `fr_FR` `es_ES` `it_IT` `nl_NL` `pl_PL` `hu_HU` `cs_CZ` `pt_PT` `en_EU` `en_GB` |
| **Americas** | `en_US` `en_CA` `es_MX` |
| **APAC** | `zh_HK` `en_AU` `en_NZ` `en_MY` |
| **Middle East** | `ar_AE` `en_AE` |

> ⚠️ **Only four of the twenty are APAC**, and one of those is the Hong Kong home market. On locale coverage alone this is a Europe-and-Americas business run out of Hong Kong. **Traffic data would settle it and we do not have any.**

### Accepted methods — enumerated, first-party
**Visa · Mastercard · American Express · PayPal (incl. PayPal Express one-click) · Google Pay · Apple Pay · coupon / store credit.**

**Sourced absent from that enumerated list:** JCB, UnionPay, Discover, Diners Club, Alipay, WeChat Pay, PayMe, Octopus, FPS, iDEAL, BLIK, Przelewy24, Klarna, Afterpay, Atome, FPX, PayNow, GrabPay, QRIS, OXXO, SPEI, boleto, Pix. **Nothing local, in any of the twenty markets.**

### Known PSPs
Read by me out of the live Magento front-end config on `stylevana.com`:

| Provider | Evidence |
|---|---|
| **Authorize.Net** (Visa-owned) | `authorizenet/directpost_payment/place` route registered |
| **Braintree** (PayPal-owned) | `braintree/paypal/placeorder` **and** `braintree/googlepay/placeorder` |
| **PayPal Express** | `paypal/express/placeorder` |
| **PayPal Payflow** | `paypal/payflowexpress/placeorder` |

Corroborated in their own words: *"**All transactions are processed on the PayPal platform** which is secure and encrypted."*

❌ Searched and not found in the front-end: Adyen, Stripe, Checkout.com, Worldpay, Cybersource, dLocal, EBANX, Airwallex, Oceanpayment, AsiaPay/PayDollar, 2C2P.

### Orchestration status
**None detected — direct integrations only (greenfield).** This is an **affirmative finding**: Magento registers each payment module's routes in the front-end config, and what is registered is three separate gateway families wired in side by side. An orchestration layer would not present that way.

### Buying signals
- 💱 **USD-only settlement across 20 localised storefronts**, with the FX cost explicitly disclaimed onto the customer, four times on one page
- 🧩 **Three gateway families in parallel** — Authorize.Net, Braintree and PayPal — with no layer choosing between them
- 🔍 **Manual fraud review in the flow:** *"All payment forms are subject to verification and reviewed by STYLEVANA. STYLEVANA reserves the right to refuse to process any transaction"*
- 🏪 **Magento / Adobe Commerce**, so adding a method means a module, a contract and a release, not a configuration change
- ❌ **No funding, no payment RFP, no payments hire found.** Privately held; the ~$200M revenue figure on the account list is **unverified**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Stylevana` to draft the 12-touch sequence.*

**Note for whoever drafts it:** the strongest single line is the USD-only quote against the 20-locale switcher. It is their own page, it is customer-visible, and it needs no interpretation.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 13 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+3** | ⚠️ **NOT FOUND — ASSUMED ~150,000–250,000/month.** `[ASSUMPTION — not researched.]` **No order count, GMV or audited revenue exists publicly** — Stylevana is private and files nothing. **Basis:** the account list carries *"~$200M est."*, which is itself **unverified**, and a beauty-e-commerce AOV in the US$50–70 band (YesStyle's audited AOV is US$65.1, the closest comparable). US$200m ÷ US$65 ÷ 12 ≈ 256,000 orders/month. **Both inputs are unsourced, so this is an assumption stacked on an estimate and I have scored it down a band from what the arithmetic implies.** Per the disclosure rule an assumption can never fire the under-40k rejection, and this one does not. **"Confirm monthly transaction count" is item 1 in Manual Research Recommendations.** |
| Orchestration status | **+4** | ✅ **None detected — affirmative**, from the live Magento route registration. Not a failed search. |
| 3+ countries | **+3** | ✅ **20 localised storefronts** enumerated in their own switcher, spanning Europe, the Americas, APAC and the Middle East. |
| Multiple PSPs | **+3** | ✅ **Three gateway families** — Authorize.Net, Braintree, PayPal (Express + Payflow) — all four module routes read from the live front-end. |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **Not scorable without traffic data, and I will not fake it.** The rail gap is enormous and sourced — *nothing local in any market* — but the rule requires the gap to sit in a **top-3 traffic market**, and **no traffic data exists for this account**. Locale presence is not traffic. **This row alone is worth +3 the moment SimilarWeb is supplied**, and on the evidence it would almost certainly be awarded. |
| Recent expansion | **0** | ⬜ No dated market entry found. |
| Payment issues reported | **0** | ⬜ No complaint corpus established. Not searched to exhaustion. |
| Funding >$10M | **0** | ❌ Private, no round found. |
| High traffic outside home | **0** | ⬜ **Cannot verify without traffic data.** Hong Kong is the home market and 19 of 20 locales are elsewhere, so this is very likely met — but "very likely" scores zero. |
| Competitor using orchestration | **0** | ❌ None confirmed. |
| Payment job postings | **0** | ⬜ None found. |

**Tier: 13 / 29 → 🟢 Medium.** No analyst override applied.

> **Why no override, and why the number understates the account.** Three rows scored zero purely because **no traffic data was supplied** — rail gap, traffic-outside-home, and indirectly the transaction count. On this evidence a SimilarWeb export would plausibly add **+5** and land it at 18 ⭐. I am not going to award points for data I do not have, but Prateek should read 13 as a floor set by a missing input rather than a ceiling set by the account.
>
> **What is genuinely strong here regardless of score:** an affirmatively-evidenced greenfield stack, three gateways with nothing routing between them, twenty storefronts on one settlement currency, and zero local methods anywhere. That is about as clean an orchestration case as this repo has produced.

### Source Notes
- ✅ **All payment findings are first-party and were read by me today** from `https://www.stylevana.com/en_US/` (HTTP 200, 1.37 MB) and `https://www.stylevana.com/en_US/payment` (HTTP 200). **The site is not WAF'd**, which is why this file has affirmative stack evidence where the YesStyle file had to infer.
- ✅ **The gateway list comes from Magento's own front-end route registration**, not from a search. Four payment module routes are registered: `authorizenet/directpost_payment/place`, `braintree/paypal/placeorder`, `braintree/googlepay/placeorder`, `paypal/express/placeorder`, `paypal/payflowexpress/placeorder`.
- ✅ **The USD-only quote and the method enumeration are verbatim** from their own payment page.
- ⚠️ **No traffic data.** Costs three ICP rows. **This is the one thing to fix before working the account.**
- ⚠️ **The ~$200M revenue figure is from the account list and is unverified.** It is the sole basis for the transaction assumption and must not be quoted to the prospect.
- ⚠️ **`authorizenet/directpost_payment` is a registered route, not proof the method renders at checkout.** A Magento module can be installed and disabled. Confirm on a live checkout before telling them they run Authorize.Net.
- ❌ **Checkout not walked.** The live payment step needs a real basket. Everything above is from public pages.

### Competitive note — read before drafting
**Strawberrynet is the other Hong Kong cross-border beauty retailer in this batch, and its method set is dramatically richer:** seven card brands plus PayPal, Alipay, WeChat Pay, PayMe, Octopus, Hoolah, iDEAL, Nordea, Afterpay and bank transfer. Same city, same cross-border model, opposite rail depth. **Useful for calibrating how far behind Stylevana is. Never name a competitor in outreach.**

---

## Executive Summary

Stylevana is a Hong Kong cross-border retailer of Korean and Japanese beauty running **Magento across 20 localised storefronts**, with **three gateway families wired in directly — Authorize.Net, Braintree and PayPal — and no routing layer between them**. The motion is **greenfield**, established affirmatively from their own live front-end configuration rather than from an absence of search hits. The commercial centre of the account is a single sentence on their own payment page: **"Payments on STYLEVANA are all processed in USD"**, stated across twenty localised markets and paired with an explicit disclaimer pushing every conversion cost onto the shopper. Their accepted-method list is **Visa, Mastercard, Amex, PayPal, Google Pay and Apple Pay and nothing else** — no local rail in any of the twenty markets they sell into. **The file scores 13/29 only because no traffic data was supplied**; three rows are unscorable without it and would very likely push this to ⭐ once it exists.

### Manual Research Recommendations
> **1. Supply SimilarWeb for stylevana.com.** *Why:* three ICP rows are unscorable without it and the rail-gap argument needs a ranked top-3 market to stand on. *Action:* export Worldwide, last 3 months, include subdomains — the same export shape supplied for YesStyle.
> **2. Confirm the monthly transaction count.** Currently an assumption built on an unverified revenue estimate.
> **3. Walk a live checkout** to confirm which of the four registered payment modules actually render, and whether 3DS is applied.
> **4. Verify the ~$200M revenue figure** or drop it from the account list.

</details>
