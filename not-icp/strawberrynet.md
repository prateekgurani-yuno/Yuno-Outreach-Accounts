# Strawberrynet

**Status:** 🔴 Not ICP — analyst override on volume (arithmetic scored 12/29)
**ICP Score:** 12 / 29 → 🟢 Medium on arithmetic → **🔴 rejected on an absolute-volume override**
**Industry:** Cross-border e-commerce (discount branded cosmetics & fragrance) · **HQ:** Hong Kong — **Strawberry Cosmetics (Services) Ltd** · **Owner:** Eastern Home Shopping & Leisure (Taiwan), 76% since Jan 2018 · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** Greenfield (would have been) — two live card acquirers routed by hand-written string comparisons in front-end React.

---

> ## 💔 THE PAINFUL PART — this is the best orchestration story in the batch, attached to the smallest business
>
> Strawberrynet's live checkout bundle contains this, verbatim, and **I verified it byte-for-byte myself**:
>
> ```js
> er = { AW_VISA:"Visa AW", AW_MC:"MC AW", SAMSUNG:"SPayWP",
>        WP_PA:["Visa WP-PA","MC WP-PA","Diners WP","JCB WP","Discov WP"] }
>
> es = e => e === er.AW_VISA || e === er.AW_MC   // isAirwallex
> eu = e => !!e && er.WP_PA.includes(e)           // isWorldPay
> ```
>
> **Visa and Mastercard each exist on two different acquirers at the same time** — `"Visa AW"` and `"Visa WP-PA"` — and which one a shopper gets is decided by a **string comparison in a React hook**. That is not a metaphor for the problem orchestration solves. That *is* the problem, hand-rolled, in production.
>
> **And it does not matter, because the volume is not there.** See the rejection rationale.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Strawberrynet is a Hong Kong cross-border retailer of discounted branded cosmetics and fragrance, trading since 1998, shipping worldwide in many currencies across 38 language sites. 76%-owned by Taiwan's Eastern Home Shopping & Leisure since January 2018.

**SimilarWeb:** **342.7K total visits, August 2026, −7.59% MoM.** Global rank #132,458. Bounce 43.4%, average visit 52 seconds. `[ESTIMATE, not confirmed]`

### Top markets `[ESTIMATE]`
| # | Country | Share |
|---|---|---|
| 1 | United States | 18.8% |
| 2 | **Hong Kong** *(home)* | 7.37% |
| 3 | Israel | 5.4% |
| 4 | Taiwan | 4.66% |
| 5 | India | 3.16% |

*Only the top 5 were retrievable; they sum to 39.4%, so ~60% sits in an unreturned tail.*

### Payment stack — richer than most accounts three times its size
- **Airwallex** — ✅ **confirmed**, natively integrated. `@airwallex/components-sdk` **v1.28.3** pinned in the bundle, initialised `env:"prod"`, hosted card Elements mounted directly (`mount("expiry")`, `mount("cvc")`), PaymentIntents `confirm({intent_id, client_secret})`, and Airwallex's own fraud script at `static.airwallex.com/webapp/fraud/device-fingerprint/index.js`
- **WorldPay** — ✅ **confirmed, named in their own code.** The predicate is literally `isWorldPay`, testing membership of the `WP_PA` array. Server-side/redirect integration, so no client endpoint is observable
- **Samsung Pay** — ✅ confirmed, settling through WorldPay (`SPayWP`), service ID `3c01346713304a94aab2cb`, `PROTOCOL_3DS`
- ⚠️ **A third and possibly fourth card arrangement is implied and unidentified** — **Amex has its own dedicated `aeThreeDS` component** and neither Amex nor UnionPay appears in the Airwallex or WorldPay arrays, yet both are in the published card list
- **3DS: ✅ confirmed present** — `threeDS` and a separate `aeThreeDS` in the checkout state
- ❌ **Zero hits**, word-boundary matched across all checkout chunks: Adyen, Checkout.com, Cybersource, Stripe, Braintree, Global Payments, Nuvei, AsiaPay, Oceanpayment, Ingenico, PPRO, Rapyd, 2C2P, dLocal, Paysafe, Fiserv, Elavon, PayerMax, Antom

### Accepted methods — enumerated, first-party (their FAQ)
**Cards:** *"Visa, MasterCard, American Express, Discover, JCB, Diners Club, UnionPay"* — seven brands.
**Alternatives:** *"Paypal, Bank In, Alipay, Wechat Pay, PayMe, Octopus, Hoolah, iDEAL, Nordea, Afterpay"*, plus money order and bank draft by arrangement.

### Orchestration status
**None detected — affirmative.** Zero hits for Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY, Juspay, Hyperswitch, Corefy, Paydock, Yuno, or `orchestrat*` / `smart routing` / `cascad*` / `retry logic`, across all 27 checkout chunks. The positive evidence is stronger: **you do not mount a raw Airwallex card Element if an orchestration layer sits in front of it.**

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 12 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **0** | ⚠️ **NOT FOUND — ASSUMED ~7,000–15,000/month. Below the matrix's lowest band.** `[ASSUMPTION — not researched.]` **Basis, and note it is traffic-led rather than revenue-led because traffic is the more reliable input:** SimilarWeb reports **342.7K visits in August 2026, declining 7.59% MoM**. Even at a generous 3% conversion that is ~10,000 orders/month; **even at an implausible 10% it is 34,000, still under the 40,000 floor.** Corroborating: ECDB estimates **US$12m GMV for 2025, declining**, which at a ~US$70 AOV gives ~14,000 orders/month. **Scored 0 rather than rejected on this row** — the disclosure rule is explicit that the under-40k gate fires only on a *sourced or soundly-derived* figure, and every input here is a third-party estimate. The rejection below comes from the analyst override, not from this gate. |
| Orchestration status | **+4** | ✅ **None detected — affirmative**, from 27 checkout chunks. Native Airwallex SDK integration plus hand-rolled routing is the opposite of an orchestration layer. |
| 3+ countries | **+3** | ✅ Ships to 200 countries, 38 language sites; five countries above 3% traffic share. |
| Multiple PSPs | **+3** | ✅ **Two card acquirers confirmed in their own code** — Airwallex and WorldPay — carrying Visa and Mastercard **simultaneously**, plus Samsung Pay via WorldPay and at least one unidentified arrangement for Amex/UnionPay. |
| Local rail or licensing gap in a top-3 market | **0** | ❌ **Genuinely not met.** Top-3 traffic is US, Hong Kong, Israel. Hong Kong already has **PayMe, Octopus, Alipay and WeChat Pay**; the US has cards, PayPal and Afterpay. **There is no missing dominant rail to point at** — this merchant has done local methods properly. |
| Recent expansion | **0** | ❌ Nothing since 2018. Traffic declining. The most recent substantive trade coverage in English or Chinese is from **2019**. |
| Payment issues reported | **0** | ⬜ No complaint corpus established. |
| Funding >$10M | **0** | ❌ The 2018 acquisition is eight years old. A planned 2019 Hong Kong IPO has no evidence of completing. |
| High traffic outside home | **+2** | ✅ Hong Kong is **7.37%**, far below the 60% threshold. |
| Competitor using orchestration | **0** | ❌ None confirmed. |
| Payment job postings | **0** | ⬜ None found. |

**Tier: 12 / 29 → 🟢 Medium on arithmetic. Overridden down to 🔴 and rejected.**

---

## Rejection Rationale

**Rejected on the analyst override for absolute volume, not on the score.** SimilarWeb puts the site at **342.7K visits/month and falling 7.59% MoM**; ECDB estimates **US$12m GMV for 2025, also declining**; ZoomInfo puts headcount at **86**. Three independent weak signals agree, and the traffic figure alone caps plausible monthly orders around 7,000–15,000 — below the 40,000 floor even under implausibly generous conversion assumptions. The matrix's own override exists for exactly this case: *"a high percentage score on a company with negligible transaction volume is a false positive."* **The 12 points are earned on payment complexity, which is real and unusually strong, but complexity without volume cannot carry orchestration economics.**

**The account list figure that got this onto the queue is refuted.** `~$150M est.` traces to a **2017/2018** report — *"average annual sales of about HK$1.1 billion (US$140.13 million)"*, Taipei Times, 16 May 2018 — and that same stale number is still sitting unmaintained on Eastern Media Group's own corporate page today, alongside *"over the past 20 years"* copy that dates it to ~2018. **It was never a current figure for this decade.**

> **Worth revisiting if any of these change:** a confirmed GMV or order count materially above the estimates; a return to traffic growth; or an EHS-led relaunch or the shelved IPO reviving. The payment architecture would make this a genuinely attractive account at 10× the volume.

---

### Source Notes
- ✅ **The routing map, the `isWorldPay` predicate and every Airwallex artefact were verified by me** directly from `https://www.strawberrynet.com/_next/static/chunks/pages/checkout-e63e6fbf0dd788e6.js` (HTTP 200, 75,015 bytes) on 2026-09-18.
- 📌 **A correction I issued against myself.** On first pass I doubted the WorldPay identification, reasoning that `WP` was an abbreviation the agent had expanded. **I was wrong.** The literal string `worldpay` appears twice in the bundle, as the predicate name `isWorldPay`. The merchant names the acquirer in its own code.
- ✅ **Card and alternative-method lists are verbatim** from `https://www.strawberrynet.com/en-US/customer-service/faq`.
- ✅ **The currency admission, quotable and first-party:** *"**not all local currencies are supported by payment gateways.** Depending on which payment method you choose, there may be cases in which **your order cannot be charged in the local currency that is displayed.** If this happens, your order will be charged in a different currency."*
- ✅ **Ownership verified:** EHS acquired **76% of Strawberry Cosmetic Holdings Limited (BVI) in January 2018 for NT$1.06bn (US$35.51m)** — Taipei Times, fetched. Still listed as a group company on Eastern Media Group's own site.
- ❌ **REFUTED — do not repeat:** ZoomInfo, Tracxn and Owler all claim *"acquired by GigaMedia on Jun 26, 2015."* No primary source supports it, GigaMedia is a Taiwanese online-games company with no cosmetics business, and it is contradicted by the 2018 EHS record. A database artifact propagating between aggregators.
- ❌ **Junk figures seen and excluded:** Owler *"$50M–$100M"*, Zippia *"$34.8 million in 2026"*. Algorithmic profile estimates with no methodology.
- ⚠️ **Substring false positive caught:** a naive grep for `ppro` returns 16 hits, all from *"Inappropriate"* and *"Approve"* in their i18n table. **PPRO is not present.** (Adds to the running list alongside `payme` inside "pay**me**nt", which I caught on this same site.)
- ⚠️ **The 342.7K visits figure carries an ambiguous 3-month note.** Treated as monthly. **If it is a 3-month total, true monthly traffic is ~114K and the business is smaller still** — which would only strengthen this rejection.
- ❌ **Not established:** the acquirer behind PayPal, Alipay, WeChat Pay, Octopus, PayMe, iDEAL, Nordea, Afterpay and Hoolah (the method list is served server-side from `web-api.strawberrynet.com` and needs a live cart); who processes Amex and UnionPay; the HK company registration number; and any confirmed revenue figure after 2017.

### TAL correction — `accounts/apac-tal.csv`
| Column | Current | Should be |
|---|---|---|
| `Est. Revenue (USD)` | `~$150M est.` | ❌ **Refuted — stale 2017 figure.** Replace with `~US$12M GMV (2025, ECDB estimate, declining)` |
| `INFO` | — | Add: 76%-owned by Eastern Home Shopping & Leisure (Taiwan) since Jan 2018 |
| `Payment Gateway` | *(empty)* | Airwallex + WorldPay (two live card acquirers) |

</details>
