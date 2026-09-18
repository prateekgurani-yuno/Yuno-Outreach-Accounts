# Stylevana

**Status:** 🟢 Ready to outreach — sequence drafted
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

### Pain Vector Extraction

```
=== PAIN VECTOR EXTRACTION ===

Motion: Greenfield — three gateway families wired directly into Magento with nothing routing
        between them. Affirmative, from their own live front-end route registration.

Observable setup facts (verified first-hand, 2026-09-18):
- Their payment page, verbatim: "Payments on STYLEVANA are all processed in USD. If your
  credit card requires currency conversion, you may be charged exchange rates and transaction
  fees by your bank and/or payment gateway. STYLEVANA are not liable for these charges."
  The same disclaimer is repeated under each method, four times on one page.
- 20 localised storefronts live in their own switcher: de_DE fr_FR es_ES it_IT nl_NL pl_PL
  hu_HU cs_CZ pt_PT en_EU en_GB en_US en_CA es_MX zh_HK en_AU en_NZ en_MY ar_AE en_AE
- Enumerated accepted methods, first-party: Visa, Mastercard, American Express, PayPal,
  Google Pay, Apple Pay, coupon/store credit. That is the whole list.
- Sourced absent from that enumeration: JCB, UnionPay, Discover, Diners, Alipay, WeChat Pay,
  PayMe, Octopus, FPS, iDEAL, BLIK, Przelewy24, Klarna, Afterpay, Atome, FPX, PayNow,
  GrabPay, QRIS, OXXO, SPEI, boleto, Pix. Nothing local, in any of the twenty markets.
- Magento route registration exposes: authorizenet/directpost_payment/place,
  braintree/paypal/placeorder, braintree/googlepay/placeorder, paypal/express/placeorder,
  paypal/payflowexpress/placeorder
- Their own words: "All transactions are processed on the PayPal platform."
- Manual fraud review in the flow: "All payment forms are subject to verification and
  reviewed by STYLEVANA."

Selected observations for Phase 1 (E1 bullets, ranked by materiality):
1. USD-only across 20 localised storefronts → "You run twenty localised storefronts, and your
   payment page says every one of them is charged in USD."
   MATERIALITY: highest. Verbatim from their own page, customer-visible, and the contrast
   with the locale switcher is self-evident. They cannot dispute either half.
2. Six methods, nothing local → "Your accepted methods are three card brands, PayPal, Google
   Pay and Apple Pay. No local method in any of the twenty."
   MATERIALITY: high. A closed first-party enumeration, so the absences are sourced.

   (Held at 2. The gateway finding is NOT used in Phase 1 — it requires them to accept my
   reading of their Magento config, and Phase 1 must be observational and undeniable. It is
   held for E3 where assertion is allowed.)

Bridge variant: B — limitations
Rationale: to a customer, and on their own payment page, this reads as a single-PSP setup
("All transactions are processed on the PayPal platform") across a large and growing market
count. Variant B fits the observations actually used in E1. Variant A would fit the gateway
finding, which Phase 1 deliberately does not raise.

Hypothesis for Phase 2 (E3):
Localisation stops at the language and currency switcher and never reaches the payment page.
Twenty storefronts, one settlement currency, one method set, so every non-US shopper takes a
conversion they can see and an auth that crosses a border.
Backing logic: their own disclaimer tells the shopper the conversion cost is theirs and not
Stylevana's, which is a conscious decision rather than an oversight. Cross-border auths
decline at higher rates than locally acquired ones, and a card-only checkout in markets like
Poland, the Netherlands, Mexico and Malaysia is missing the rails those markets actually use.

Success case for Phase 3 (E4):
Selected case: inDrive
Tier: 2 — same payment pattern (many markets, one stack, market-entry speed), different
industry and region. Stated in the email.
Match rationale: no Tier 1 exists — there is no Asian-beauty or cross-border-retail case in
the library. inDrive is the library's multi-country-scale case and maps directly onto a
merchant running twenty storefronts off one method set.
Numbers to lead with: ~90% approval rate · 10 new countries live in under 8 months ·
50+ countries on one integration
Optional benchmark: SKIP. The "~8% average authorisation uplift" traces to Yuno's own blog
and is our marketing, not independent evidence.

Touch-by-touch angles:
- E2 angle: the missing local rails → one integration to add any method, no per-rail rebuild
- LK1 angle: twenty storefronts, one currency
- LK2 angle: localisation stops before the payment page
- LK3 angle: inDrive opened 10 countries in under 8 months on one integration
- LK4 angle: FRESH — the manual fraud review line on their own payment page
- E8 angle: clean exit
```

**Calendar.** Day 1 anchored to **Monday 21 September 2026**. **Hong Kong general holidays in
the window: Saturday 26 September** (day following Mid-Autumn) **and Thursday 1 October**
(National Day), both checked at source. **No send day and no proposed slot falls on either**,
or on **Monday 19 October** (day following Chung Yeung), or on a weekend.

**Times are HKT (UTC+8), which is IST+2:30** — most of the working day overlaps.

---

### Phase 1 — Curiosity (Days 1–5)

#### Touch 1 — Email 1 · Day 1 · Mon 21 Sep

**Subject:** Twenty storefronts, one currency

```text
Hey {{recipient.first_name}},

Spent some time on Stylevana's payment setup. Two things stood out:

- You run twenty localised storefronts, from de_DE and fr_FR to es_MX, en_MY and ar_AE. Your payment page says every one of them is charged in USD.
- Accepted methods are three card brands, PayPal, Google Pay and Apple Pay. No local method in any of the twenty.

At your stage, that kind of setup usually comes with some limitations.

I work at Yuno — top-100 fintech, a16z-backed. We consider ourselves the 'everything payments' platform: one integration, every PSP, every method, every market.

Rather than pitch you based on assumptions, is there anything payment-related you're working through that we might be able to help with?

Best,
Prateek
```

#### Touch 2 — Email 2 · Day 3 · Wed 23 Sep · REPLY IN THREAD

```text
Hey {{recipient.first_name}},

Following up. Wanted to put a bit more behind what Yuno actually does, and how it would address what I flagged.

- We sit above your existing gateways. Additive, nothing gets ripped out.
- A method enabled once is available on every storefront, without a per-market rebuild.
- Traffic routes per BIN, market and method to whichever rail performs best.
- Local acquiring per geography, so a transaction can settle in the market it came from.

On the twenty storefronts specifically, the part that matters is that adding iDEAL for the Netherlands, BLIK for Poland, or FPX for Malaysia stops being three separate integrations and becomes three configuration changes on one.

I'll keep sharing what I'm seeing every few days. If your stack's where you want it, just say the word and I'll back off. Otherwise happy to go deeper.

Cheers,
Prateek
```

#### Touch 3 — LinkedIn message 1 · Day 5 · Fri 25 Sep

```text
Hey {{recipient.first_name}} — dropped you a note over email, flagging it here too in case this is the easier channel. Quick one: you run twenty localised storefronts and your own payment page says all of them are charged in USD, with the conversion cost passed to the shopper. Curious whether that's a deliberate call or just where things landed.
```

---

### Phase 2 — Diagnosis (Days 7–9)

#### Touch 4 — Email 3 · Day 7 · ~~Sun 27 Sep~~ → **send Mon 28 Sep** · NEW EMAIL

**Subject:** Where the localisation stops

```text
Hey {{recipient.first_name}},

Going to take a swing at this. My read is that the localisation stops at the language and currency switcher and never reaches the payment page.

Twenty storefronts, one settlement currency, one method set. So a shopper in Warsaw or Kuala Lumpur sees prices in their own language, then pays in USD on a card, takes a conversion they can see, and has an auth that crosses a border. Cross-border auths tend to decline at higher rates than locally acquired ones, and a card-only checkout in those markets is missing the rails people there actually use.

When you added the newer storefronts, did payments come up as part of that, or did the market go live on the existing setup?

At Yuno (a16z-backed, top-100 fintech) we sit above your existing gateways, so you can add local methods and acquire locally where it's worth it. Keep your stack, add what's missing.

Friday 2 October is open. Would 10am or 3.30pm your time work for a quick 15?

All the best,
Prateek
```

#### Touch 5 — LinkedIn message 2 · Day 9 · Tue 29 Sep

```text
Hey {{recipient.first_name}} — sent a longer note over email this week. Short version: your localisation looks like it stops at the currency switcher and never reaches the payment page — twenty storefronts, one settlement currency, one method set. If that's anywhere on your radar, would Monday 5 or Tuesday 6 October at 11am your time work for a quick 15?
```

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · ~~Thu 1 Oct — HK National Day~~ → **send Fri 2 Oct** · NEW EMAIL

**Subject:** How inDrive solved this

```text
Hey {{recipient.first_name}},

On the read I shared last week. Sharing a quick example of what solved looks like.

inDrive operates in a lot of countries with very different payment habits in each. They put Yuno above their existing stack rather than replacing it. What that produced:

- Around 90% approval rate
- 10 new countries live in under 8 months
- 50+ countries running through one integration

Worth saying plainly: inDrive is a mobility platform and those results came out of its own markets, not Asia, so this is a payment-pattern match rather than an industry one. What carries over is the shape — many markets, one stack, and the cost of adding a rail per market.

Same orchestration layer above their existing stack. No rip-out.

Thursday 8 October is open. Would 3pm or 4.30pm your time work for 15 minutes?

Full case here if useful: https://y.uno/en/success-stories/indrive

Thanks,
Prateek
```

#### Touch 7 — Email 5 · Day 13 · ~~Sat 3 Oct~~ → **send Mon 5 Oct** · MANUAL

*Placeholder — manual creative approach. Do not auto-write.*

> **Strongest asset:** a market-by-market rail teardown. Take five of their twenty locales —
> **nl_NL, pl_PL, es_MX, en_MY, zh_HK** — and put the dominant local rail beside what
> Stylevana actually accepts today. iDEAL, BLIK and Przelewy24, OXXO and SPEI, FPX, and
> PayMe/FPS/Octopus respectively, against a checkout offering three card brands and two
> wallets. One table, no argument needed.

#### Touch 8 — Email 6 · Day 15 · ~~Mon 5 Oct — taken by the shifted E5~~ → **send Tue 6 Oct** · MANUAL

*Placeholder — second manual approach, different format from E5.*

> **Suggested format: a short screen recording of their own checkout** from a European locale,
> showing the currency switch to USD at the payment step. Their disclaimer is on the page in
> writing; showing it happening is stronger than quoting it.

#### Touch 9 — LinkedIn message 3 · Day 17 · Wed 7 Oct

```text
Hey {{recipient.first_name}} — inDrive opened ten new countries in under eight months without standing up a new payment integration for any of them. Worth 15 minutes to see whether that maps to your setup? Monday 12 October at 10.30am your time is open.
```

---

### Touch 10 — Email 7 · Day 19 · Fri 9 Oct · MANUAL

*Placeholder — manual creative bridge. Anchor to something fresh.*

> **Options, in order of strength.** (1) Their **Magento** stack — adding a method means a
> module, a contract and a release, which is the buy-versus-build conversation stated
> concretely. (2) The **es_MX storefront**: Mexico is live, and OXXO is the rail that market
> runs on. (3) Anything Prateek can find on a recent market launch — **no expansion signal
> was found in research**, so this touch is the place to use something he sources himself.

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21 · ~~Sun 11 Oct~~ → **send Mon 12 Oct**

```text
Hey {{recipient.first_name}} — last LinkedIn ping from me on this. One thing I never raised: your payment page says every order is subject to manual verification and review before it's processed. At twenty storefronts that's a real operational load, and it's usually a symptom rather than a policy. If timing works, Thursday 15 October at 2pm your time is open for a quick 15.
```

#### Touch 12 — Email 8 · Day 23 · Tue 13 Oct · REPLY IN THREAD to Touch 4 or Touch 6

```text
Hey {{recipient.first_name}},

Going to stop pinging unless you want to pick this back up.

If the timing is just off, happy to circle back next quarter. And if payments sits with someone else on your side, happy to be pointed there.

If it ever comes back up, just reply here.

All the best,
Prateek
```

---

### CTA schedule — five distinct slots, all Hong Kong time

| Touch | Sent | Proposed slot(s) | HKT → IST |
|---|---|---|---|
| E3 | Mon 28 Sep | **Fri 2 Oct, 10:00 or 15:30** | 07:30 / 13:00 IST |
| LK2 | Tue 29 Sep | **Mon 5 or Tue 6 Oct, 11:00** | 08:30 IST |
| E4 | Fri 2 Oct | **Thu 8 Oct, 15:00 or 16:30** | 12:30 / 14:00 IST |
| LK3 | Wed 7 Oct | **Mon 12 Oct, 10:30** | 08:00 IST |
| LK4 | Mon 12 Oct | **Thu 15 Oct, 14:00** | 11:30 IST |

No booking link anywhere, by decision — the reply is the booking.

---

### Source Notes

- ✅ **Both Phase 1 observations are verbatim or enumerated from Stylevana's own pages**, fetched by me on 2026-09-18. The site is not WAF'd.
- ✅ **The USD-only quote is exact** and appears with the liability disclaimer repeated four times on one page.
- ✅ **The twenty locales come from their own storefront switcher**, not from an inference about shipping.
- ✅ **The method list is a closed first-party enumeration**, which is what makes the absences sourced rather than assumed.
- ✅ **Hong Kong general holidays checked at source** — 26 Sep and 1 Oct; 19 Oct also avoided.
- ✅ **inDrive is Tier 2 and E4 says so outright**, including that the results came from its own markets and not Asia.
- ⚠️ **The gateway finding is deliberately absent from Phase 1.** Authorize.Net, Braintree and PayPal are registered Magento routes, which proves modules are installed, **not that each renders at checkout**. E3 and later reference the shape without naming providers. **Confirm on a live checkout before naming any of them to the prospect.**
- ⚠️ **No traffic data.** The sequence therefore never claims a market ranking — every geographic reference is to a storefront that demonstrably exists, not to a market's share.
- ⚠️ **No expansion signal was found in research**, which is why E7 is the touch flagged for Prateek to source something himself.
- ❌ **The ~$200M revenue figure on the account list is unverified and appears nowhere in the sequence.**
- ❌ **No recipient identified.** All twelve touches use `{{recipient.first_name}}`.

### Success Case Alternatives
- **Vibra** — new-user approval lifted more than 30 points to 80%, with Apple Pay, Nu Pay and Google Pay launched on the same integration. The better swap if discovery shows the problem is **first-time-buyer conversion** rather than market coverage.
- **Rappi** — hundreds of methods through one integration, 80% less analyst work. Use if the conversation turns to **operational load** rather than market entry.
- **Livelo** — decline recovery via a secondary acquirer. Only if discovery surfaces declines with no failover; nothing in this research points there yet.

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
