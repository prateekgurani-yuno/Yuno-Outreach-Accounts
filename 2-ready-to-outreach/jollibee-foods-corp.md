# Jollibee Foods Corporation

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 16 / 29 → 🟢 **Medium**
**Industry:** QSR / Food & Beverage — multi-brand restaurant group · **HQ:** Jollibee Foods Corporation, Pasig City, Philippines (PSE: **JFC**), incorporated 11 Jan 1978 · **Researched:** 2026-10-06 · **First email sent:** —
**Motion:** 🟡 **GREENFIELD on orchestration, but NOT on payments engineering.** Exactly two direct PSPs (Maya + GCash), no orchestrator — verified first-hand. But they have built the same ordering-and-payment stack **three times over**. The pitch is **consolidation and engineering cost, not approval rates.**

---

> ## ⭐ THE FINDING — their entire payment method list is a 105-byte file
>
> I fetched it myself. `https://order.chowking.ph/assets/payment-types-Cx22qD1x.js` — **HTTP 200, 105 bytes.** This is the complete file:
>
> ```js
> var e=function(e){return e.Card=`card`,e.Cash=`cash`,e.Gcash=`gcash`,e.Maya=`maya`,e}({});export{e as t};
> ```
>
> **Four methods. Card, cash, GCash, Maya. That is the whole list** for a PHP 455bn-system-wide-sales group in the market where GCash and Maya are the two dominant wallets.
>
> And I verified the PSP allowlist directly. `https://order.greenwich.com.ph/env.js` — **HTTP 200, 1,405 bytes**:
>
> ```js
> features: ['maya', 'gcash'],
> referrers: ['https://payments.gcash.com/', 'https://payments.maya.ph/', 'https://checkouts.maya.ph/']
> ```
>
> **That is a complete PSP return-URL allowlist: exactly two providers, both integrated directly, with zero redundancy.** `checkouts.maya.ph` is Maya's hosted checkout page — meaning **Maya is the acquirer for cards, not just the wallet.** Red Ribbon's bundle confirms it in plain language: `"paymaya-redirect":"Maya or Credit/Debit Card"`.
>
> **No orchestrator domain. No secondary acquirer. No fallback PSP.** Swept all 149 Chowking chunks, four `env.js` files and a 1MB Red Ribbon bundle for Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, PortOne, Corefy, IXOPAY, inai, MoneyHash and Yuno — **zero matches.** Also zero for Adyen, Stripe, Braintree, 2C2P, Xendit, Dragonpay, Paynamics, PesoPay, AsiaPay, Cybersource and Worldpay.

---

> ## 🎯 THE HOOK — they built the same stack three times, and the flagship brand has no checkout at all
>
> **This is an asymmetry inside their own estate, which is the strongest kind of observation.**
>
> | Brand | Own checkout? | Platform generation |
> |---|---|---|
> | **Jollibee** (the flagship) | ❌ **NONE** — `jollibee.com.ph/order` is a link-out page | n/a |
> | Chowking | ✅ `order.chowking.ph` | **Current Falcon** (Vite, 149 chunks, PGP-encrypted payloads) |
> | Mang Inasal | ✅ `order.manginasal.ph` | **Current Falcon** |
> | Greenwich | ✅ `order.greenwich.com.ph` | **Prior Falcon generation** — flat BFF URL, no PGP key, explicit feature flags |
> | Red Ribbon | ✅ `redribbondelivery.com.ph` | **A different app entirely** (1,074,764 bytes, 78 `payment` hits) |
>
> **I verified the flagship has no checkout.** `https://www.jollibee.com.ph/order` — HTTP 200, 74,680 bytes, **control: 0 `payment` hits.** The only two ordering links on the page are `grab.onelink.me/2695613898?...` and `foodpanda.ph/chain/cg0ep/jollibee`. Rendered text, verbatim: *"Order Jollibee Delivery on GrabFood or foodpanda."*
>
> **Hard proof the siblings share one payment backend.** Both `env.js` files reference an in-house platform codenamed **Falcon** on JFC-owned infrastructure (`jfcapps.com`, `jfcapis.com`), and the decoded PGP key identity is **`falcon <falcon@jfcapps.io>`**. I confirmed by hashing the whitespace-stripped key material:
>
> | File | `pgpPublicKey` sha256 (24) | len | `jwtPublicKey` sha256 (24) |
> |---|---|---|---|
> | Chowking `env.js` | `25cea92ca4586ea273fd35df` | 836 | `4963f196de53fb30f59c7045` |
> | Mang Inasal `env.js` | `25cea92ca4586ea273fd35df` | 836 | `95a6d3549acafd17e89e23b0` |
>
> **The PGP payment-encryption key is byte-identical across two different brands; the JWT signing keys differ.** One shared payment-data key for the whole platform, per-brand auth tenancy.
>
> And a copy-paste artefact in `order.chowking.ph/assets/global-configs-DBRIO193.js` makes the templating visible — **Chowking's own config carries Mang Inasal's URLs**:
> ```js
> brandSettings:{initials:`CK`,corporation:`Chowking Philippines, Inc`, ...
>   websites:{marketing:`https://www.manginasal.ph`,delivery:`https://order.manginasal.ph`, ...
> ```
>
> **Four brands, three platform generations, two PSPs, no redundancy — all auditable from their own public JavaScript.** That is a consolidation argument they cannot dispute, because it is their code.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** The Philippines' largest restaurant group and an aggressively acquisitive multinational. 8 wholly-owned brands (Jollibee, Chowking, Greenwich, Red Ribbon, Mang Inasal, Yonghe King, Hong Zhuang Yuan, Smashburger) plus Coffee Bean & Tea Leaf 80%, Milksha 51%, Compose Coffee 70%. **10,421 restaurants and cafés across 33 countries**, 1,126 opened in 2025 — "the most in our company's history."

| Metric | FY2025 | Change |
|---|---|---|
| System-wide sales | **PHP 455,111M (~US$7,914M)** | **+16.6%** |
| Revenues | PHP 305,112M (~US$5,306M) | +13.0% |
| Operating income | PHP 20,150M (~US$350M) | +19.3% |
| Net income attrib. to parent | PHP 10,872M (~US$189M) | +5.4% |
| EBITDA | PHP 41,830M (~US$727M) | +13.8% |

**Q2 2026 (reported 8 Sep 2026):** revenue US$1.4bn (+12%), SWS +14.2% to US$2.1bn, net income US$55M — *"highest quarterly profit in the company's history"*, operating margin 9.1%. `[UNVERIFIED — search summary only, malaymail page 403'd]`

**SimilarWeb total visits:** **468,669** (Aug 2026), +9.29% MoM, 67.54% mobile web — **supplied by Prateek**, Similarweb PRO. ⚠️ **This is `jollibee.com.ph` only — ONE brand in ONE market**, and that domain has no checkout. Full caveat in `accounts/traffic/jollibee-foods-corp.md`.

### ⚠️ Revenue vs SWS — 33% of the estate is franchised
PHP 305bn revenue vs PHP 455bn SWS = **~PHP 150bn (33%) of system-wide sales sit in franchised stores**, where JFC books only royalty and rent, not the transaction. **Franchisee-operated stores are almost certainly not on a JFC-controlled payment stack.** `[INFERENCE, not confirmed]` The US expansion is explicitly franchised — *"seven franchise groups aiming to grow to 330 franchised restaurants by 2030"* — and US/Canada run separate apps with separate help centres. **Do not attribute North American payment volume to JFC.**

### 🛑 Transaction volume — NOT ESTABLISHED. Read this before pitching.
Three derivations, and they disagree by two orders of magnitude. **All arithmetic shown.**

**Derivation A — top-down from the digital share**
```
FY2025 SWS                    PHP 455,111 M
× 19% digital              =  PHP  86,471 M / yr
÷ 12                       =  PHP   7,206 M / month
÷ ASSUMED AOV PHP 600      ≈  12.0 M digital transactions / month
× 10% residual (stripping aggregator-MoR + drive-thru + COD)
                           ≈  1.2 M transactions / month
```
⚠️ The 19% is **search-summary only**. The PHP 600 AOV is **my assumption with no source**. SWS includes 33% franchised volume. **Directional at best.**

**Derivation B — bottom-up from the one hard data point**
```
jollibee.com.ph visits (Aug 2026)   468,669 / month
× ASSUMED e-commerce conversion 2–4%
                                 ≈  9,373 – 18,747 orders / month
```
**This does NOT clear the 40,000/month gate.** ⚠️ But the domain measured **has no checkout** — ordering lives on the sibling brands' storefronts and the Jollibee app, which are wholly excluded from this figure. **This derivation measures the wrong thing.**

**Derivation C — registered app users**
```
600,000 registered users  × ASSUMED 10% monthly active × ASSUMED 1.5 orders
                           ≈  90,000 transactions / month
```
⚠️ The 600,000 figure is **undated, unsourced, no market specified.** Two assumed rates on top.

**🛑 VERDICT: the gate is NOT established with a sourced number, and the gate therefore does NOT fire** — per the rule, only a *sourced or soundly-derived* sub-40k figure rejects, and an assumption never does. The group almost certainly clears 40,000/month in aggregate `[INFERENCE]`, but **every path there runs through an assumption I had to invent. DO NOT put a transaction number in outreach.**

### ⚠️ The "digital sales" metric is NOT a card-not-present proxy
JFC does disclose a digital-sales percentage, but it is contaminated three ways:
1. **Drive-thru is counted inside the digital framing.** CFO Richard Chong Woo Shin, Q1 2026 call (fetched): *"Of course, digital is a key part both through drive-throughs and also off-premise, like delivery."* **Drive-thru payment is card-present or cash.**
2. **Third-party aggregators collect the consumer payment on their own rails.** JFC is a supplier settling net, not merchant of record. **An orchestrator cannot touch that volume.**
3. **Cash on delivery is a first-class method** in every brand's code — so even own-channel "digital orders" are not all digital *payments*.

**And the trend is flat, which kills the "digital is exploding" angle:** *"digital sales account for 18 percent of total sales"* in **Q1 2023** per the CFO, versus **19%** cited for 2026. ⚠️ Both figures are `[UNVERIFIED — search summary only]`. **The FY2025 results release contains no digital, e-commerce, app, delivery-mix, loyalty or payments figure at all — I fetched it and checked. That absence IS verified.**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

> **Not yet generated.** Run `/full-outreach Jollibee Foods Corp` to compose the 12-touch sequence into this section.
>
> **Motion is GREENFIELD on orchestration but NOT on payments engineering.** They have a real in-house layer (Falcon) with a `v1/payments/options` endpoint, `updateOrderPayment`, a `retry-payment-button` chunk and a shared PGP key. **That means an internal team with sunk cost and an opinion.** Do not open with "you need orchestration" — open on the three-generations-of-the-same-stack asymmetry.
>
> **Lead with consolidation and engineering cost. Do NOT lead with approval rates** — there is zero approval-rate, MDR, decline or chargeback visibility, and any such claim would be fabrication.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

## Section 1: Legal Entities — merchant-of-record candidates

| Entity | Jurisdiction | Status | Confidence |
|---|---|---|---|
| **Jollibee Foods Corporation** | Philippines | **CONFIRMED.** Incorporated 11 Jan 1978, PSE-listed | High — PSE Edge is the primary registry (`edge.pse.com.ph/companyInformation/form.do?cmpy_id=86`), page not fetched |
| **Jollibee Worldwide Pte. Ltd.** | **Singapore** | Singapore-HQ'd; the acquiring vehicle for Compose Coffee (70%) | Medium `[UNVERIFIED — search summary only]`. **ACRA/BizFile NOT reached, no UEN obtained** |
| **Golden Plate Pte. Ltd. (GPPL)** | **Singapore** | Wholly-owned by Jollibee Worldwide / JFC. JV with Beeworks Investment Pte Ltd for **West Malaysia** (120 branches planned); co-owns the **Singapore** Jollibee franchise; also created to operate **UAE** stores | Medium `[UNVERIFIED]` |
| **JSF Investments Pte. Ltd.** | **Singapore** | **New find, not on the original list.** Holds the JFC side of SuperFoods Group | Low-Medium `[UNVERIFIED]` |
| **SuperFoods Group** | **Vietnam** | JFC **60%**. Owns **Highlands Coffee** and Pho 24, plus Hard Rock Cafe franchises in Vietnam, Macau, Hong Kong | Medium — ⚠️ **the 60% conflicts with "wholly-owned subsidiary of JSF Investments and Viet Thai International JSC" in the same source. The ownership chain is muddled and needs a filing to resolve** |
| **All Day Fresh** | **South Korea** | **100% acquired 2026** (operator of Shabu All Day) | Medium `[UNVERIFIED]` |
| JFC International · Jollibee Group Foods Inc · Jollibee Group Asia Pacific | — | **ALL THREE NOT FOUND.** Searched explicitly. May be internal labels, not registered companies | — |

**Markets with a confirmed JFC-side entity:** Philippines (parent), Singapore (three entities), Vietnam (via Singapore), South Korea (Compose, All Day Fresh), Malaysia (JV). **All in APAC territory.**

**Territory note:** GPPL was created to operate **UAE** stores. UAE is EMEA and out of territory — but GPPL is **Singapore-incorporated under a Philippine parent**, so per CLAUDE.md (an APAC-HQ'd company selling into the Gulf is still in scope) the entity stays in scope. **Do not pitch the Gulf estate.**

## Section 2: PSP Stack & Orchestration

**Classification: `None detected (direct PSP integrations only)` — but see the nuance below, it matters.**

| PSP | Role | Evidence | Confidence |
|---|---|---|---|
| **Maya (PayMaya) / Maya Business** | **PRIMARY — cards (Visa/MC/JCB) AND the Maya wallet.** Also in-store terminals, kiosks, drive-thru | `checkouts.maya.ph` + `payments.maya.ph` in Greenwich `env.js` (**I verified both**); `"paymaya-redirect":"Maya or Credit/Debit Card"` in Red Ribbon; `e.Maya='maya'` in the enum | **CONFIRMED — first-party code** |
| **GCash** | Direct wallet integration — its own rail, not resold via Maya | `payments.gcash.com` in Greenwich referrers (**verified**); `features:['maya','gcash']` (**verified**); `externalProtocols:["gcash://"]`; `e.Gcash='gcash'` | **CONFIRMED — first-party code** |
| AsiaPay / PesoPay | **LEGACY, 2011**, on the now-dead `jollibeedelivery.com` | theglobaltreasurer.com 21 Nov 2011; asiapay.com PDF | **🛑 Historical. The domain no longer resolves. DO NOT cite as current — it is 15 years old and pre-dates GCash, the app, and the entire international build-out** |

Maya's scope is corroborated by press: terminals, self-ordering kiosks, drive-thru counters and **Maya Checkout on their websites and mobile apps**. The Visa PH press release confirms *"powered by Maya Business"*, 1,000+ stores, Feb 2023 — but is **vague on Maya's technical layer and does not itself prove acquiring.**

### ⚠️ Do not oversell "greenfield"
There **is** a real in-house layer. From `order.chowking.ph/assets/endpoints-Ch4ts4A3.js` (HTTP 200, 17,533 bytes):
```js
order:{checkoutOrder:e=>`v1/stores/${e}/orders`,
       paymentOptions:`v1/payments/options?touchpoint=${P}`,
       updateOrderPayment:e=>`v1/orders/${e}/payment`...
```
**No PSP JS SDK loads client-side anywhere across the 149 chunks** — everything routes through JFC's own `order-web-bff.<brand>` endpoints.

**But on the evidence this is a thin method-presentation BFF, not an orchestration layer:** two PSPs, no routing logic, no cascading, no vault (Maya holds the PAN), no multi-acquirer. The `retry-payment-button` is **user-initiated retry, not an auto-retry cascade** — there is no routing config in any bundle.

**Honest framing: they have built real in-house payment plumbing, so there is an internal team with sunk cost and an opinion. The gap is that the plumbing terminates in two domestic PSPs with zero redundancy, and has been built three separate times.**

## Section 3: Philippine Rails

| Rail | Status | Source |
|---|---|---|
| **Maya wallet** | ✅ **CONFIRMED** | enum `e.Maya='maya'`; `checkouts.maya.ph` |
| **GCash** | ✅ **CONFIRMED** | enum `e.Gcash='gcash'`; `payments.gcash.com`; `gcash://` |
| **Cards — Visa, Mastercard, JCB** | ✅ **CONFIRMED** | `/images/logo/{visa,mastercard,jcb}.webp` in the payment accordion; acquired **via Maya** |
| **Cash (COD / pay-on-pickup)** | ✅ **CONFIRMED** | enum `e.Cash='cash'`; `"cod":"Cash"`; `maxTenderedAmount:3000`, a "Change for" field |
| **Card-on-file** | ✅ **CONFIRMED — PSP-side** | PHP 10.00 test charge, see below |
| GrabPay · ShopeePay · **QR Ph** · InstaPay/PESONet · online banking · 7-Eleven/OTC · **BNPL (BillEase, Atome, Cashalo, TendoPay)** · card instalments · **Apple Pay / Google Pay** | ❌ **ALL NOT FOUND** | Zero hits across every bundle |

**A PHP 455bn QSR group in the Philippines accepting four methods, no QR Ph, no BNPL, no instalments, and no Apple/Google Pay.** Apple Pay and Google Pay **do** appear in the **North America** app — out of territory, noted only so it is not mistaken for PH capability.

⚠️ **Note:** foodpanda PH added QR Ph on cash-on-delivery orders (May 2026). **That is foodpanda's rail, not JFC's.**

### Card-on-file is PSP-side, and JFC says so explicitly
From the Red Ribbon T&C and the jollibee.com.ph privacy notice, verbatim:
> *"our **authorized third party** will apply a **test charge of Php10.00** when you save your credit card details. The test charge will be automatically triggered for voiding after validation"*

> *"Credit Card Details are collected, stored, and processed by our **service provider** … **not by us**, and we are not responsible for securing and protecting said Credit Card Details."*

**JFC explicitly disclaims holding PAN.** Vaulting sits with Maya. The PHP 10 auth-and-void is a Maya-side card-verification pattern.

⚠️ **On COD dominance:** COD is a first-class method in every brand's code, with separate refund flows (*"If paid online (Gcash, Maya, debit or credit card), store will process the refund"*). **No cash-vs-digital split for JFC's own channels could be found. DO NOT assert a COD share — you do not have it.** Context only: PH digital payments reached 64.7% of retail *volume* in 2025 `[UNVERIFIED — search summary only]`.

## Section 4: 🛑 Aggregator dependency — this should govern how the account is pitched

**For the Jollibee brand in PH, aggregators ARE the online channel.** Verified: `jollibee.com.ph/order` offers GrabFood and foodpanda and nothing else, with zero `payment` code on the page. **On those orders the aggregator is merchant of record and JFC never touches the payment. Orchestration cannot address that revenue.**

JFC does operate its own **Jollibee App** (GCash, credit/debit, COD). ⚠️ The app bundle is native and could not be fetched, and the help-centre article listing its methods is **Cloudflare-blocked (403)**.

**🛑 The number one gap: no own-app vs aggregator split is publicly disclosed anywhere.** Nothing in FY2025 results breaks out digital channel mix. The only datapoint found — delivery at **5% of PH system-wide sales in early 2020** — is six years stale; **do not use it.** Market context: GrabFood 61% / foodpanda 39% of PH food delivery `[UNVERIFIED — search summary only]`.

**Blunt read: the addressable payment volume is the SIBLING brands' storefronts plus the Jollibee app — not "Jollibee's delivery business." If Prateek pitches total JFC delivery GMV, a payments lead will know immediately that he is wrong.**

## Section 5: Non-PH Markets

**Vietnam — Highlands Coffee (JFC-owned via SuperFoods).** Website returned **HTTP 403** (Cloudflare), help centre 403; not retried. Per search: accepts MoMo, ZaloPay, cash, credit/debit and **VietQR**, varying by store and platform `[UNVERIFIED — search summary only, 403 on fetch]`. **VNPay NOT confirmed. No PSP or gateway identified for Vietnam.** Notable: Highlands runs a **MoMo mini-app** for ordering — **a second wallet-as-channel dependency, structurally the same problem as GrabFood in PH.**

**🔑 Korea — Compose Coffee (70%, acquired July 2024, ~2,612–3,000 stores).** **Nothing found on its PSPs or PG.** Korea is local-PG-gated (KCP / Toss / Inicis / NICE / PortOne class) but there is **zero evidence — do not speculate in outreach.** ⚠️ **This is the single highest-value unexplored thread on the account:** a newly acquired 3,000-store Korean chain being integrated into a Philippine parent's payment estate is exactly the trigger Yuno sells into, and nobody has written about it.

**China / Taiwan / HK:** not investigated.

## Section 6: Buying Signals

### M&A — they are actively acquisitive, and this is the strongest signal class
- **All Day Fresh / Shabu All Day (South Korea)** — 100%, **KRW 130bn (~US$88.6M)**, **172 stores**, annual sales ~KRW 480bn. Completed around **20 April 2026.** `[UNVERIFIED — search summary only]` **In-territory, recent, and a fresh integration problem.**
- **Compose Coffee (South Korea)** — Jollibee Worldwide acquired **70%**; **2,600 branches** at acquisition, now "north of 3,000" (Q1 2026 call, fetched). Took the group to ~10,000 stores. **Since acquisition Compose has expanded into Southeast Asia — the Philippines and Singapore.** ⚠️ **Price discrepancy: US$238M for 70% in one summary vs "340m" in the Verdict URL slug. Resolve before quoting.**
- JFC has publicly said it is scouting a ~US$1bn US-based target. `[UNVERIFIED, likely dated]`

**Cross-border brand transplants:** a Korean brand (Compose) now selling in PH + Singapore; a Vietnamese brand (Highlands) in PH; a Hong Kong franchise-holder majority buyout in 2023. **A Korean-acquired brand selling in PH and SG is exactly the multi-market, multi-PSP stack problem Yuno sells against.** `[INFERENCE on the pain]`

### Digital
- **🔑 New Jollibee PH delivery app launched 28 July** at Whitespace Makati — *"newly redesigned delivery app with new features and user-centric design aimed at simplifying ordering and boosting customer loyalty."* ⚠️ **The year is ambiguous (2025 or 2026) — verify before referencing.** **A checkout rebuild is the single best-timed hook in this list.**
- **Jollibee Rewards** — *"first-ever global loyalty program"*, debuted **North America**, identity by Landor, 10 points per $1, $5-off-$10+ promo **September 2025.** **Launched NA-first, so the global rollout to APAC is likely still in flight.**
- **Atome Philippines partnership** (BNPL) — `jollibee.com.ph/index.php/news/jollibee-partners-with-atome-philippines`. ⚠️ **Low-Medium, undated, page not fetched.** If current it is direct evidence of bolting on alternative methods one integration at a time — but note Atome appears **nowhere** in any bundle I swept.
- **DXC Technology** — five-year contract to modernise applications and accelerate digital transformation across then-3,200+ stores, signed **August 2023.** A 5-year deal runs to **2028**; they are mid-programme, which cuts both ways — budget exists, but an SI incumbent sits in the way.

### Leadership
| Name | Role | Note |
|---|---|---|
| **Marcos Cadena** | Global Chief Technology Officer | in seat **since end-2020** — stable, not a new-arrival trigger |
| **Carlson Choi** | former Global CDO/CIO | **departed to Jack in the Box as CIO (~May 2024).** ⚠️ **Whether the seat was refilled is UNRESOLVED** |
| **Andrew Lee** | Head of Digital Transformation Strategy & Adoption Success, and Data Privacy | plausible entry point |
| **Kate Yu** | CMO | Low confidence, undated |

**No payments-specific hire, no payments RFP, no "unified commerce" announcement found. NOT FOUND.**

## Section 7: Payment Complaints

### 🔑 The strongest pain signal — JFC's own help centre
Jollibee PH maintains a **five-article dedicated GCash refund-dispute workflow**:
1. "Where can I request for refund of the GCash payment"
2. "If there are issues on the refund (e.g. wrong amount, incorrect GCash, longer waiting time etc.) who can I reach out"
3. "How long will it take to process the refund"
4. "Will I be notified once I have been refunded"
5. "Are there documents/information I need to provide"

**What the content reveals** `[UNVERIFIED — search summaries only; the pages 403'd on fetch]`:
- The documented failure mode is explicitly **"payment goes through but the order didn't."**
- **Refunds are manual and store-level** — the customer contacts the **individual branch** and supplies a **receipt, order-confirmation email, or a screenshot of the GCash SMS** as evidence.
- **Refund SLA: 3–7 business days.**
- GCash explicitly disclaims refund handling — *"GCash acts only as a payment channel"*; **JFC must approve and initiate each refund.**

**Read:** a five-article dispute workflow, evidence upload by screenshot, per-branch escalation and a 3–7 day SLA **is not what a merchant builds for an isolated problem.** Issue type: orphaned online payments and manual refund recovery. Frequency: **moderate-to-high, inferred from the depth of the self-service documentation, NOT from a counted complaint volume.** ⚠️ **This is the most defensible payment-pain hook in the file, and it is still an inference about volume, not a measurement. Label it as such.**

### Gaps, stated plainly
- ⚠️ **Reddit: NOT REACHED.** reddit.com is blocked to this user agent (API error on the domain-restricted search). **r/Philippines and r/phinvest threads on Jollibee payment failures remain UNCHECKED.** A real gap.
- ⚠️ **PH app reviews: NOT FOUND.** No install count, rating or review corpus retrieved for the Philippine app.
- The figures that surfaced — **~100,000 installs, 4.8★, 6.7K reviews** — are for package **`com.olo.jollibeeusa`**, the **US/Canada** app. Reported issues there: sign-in authorization errors, rewards not saving, *"limited payment methods"*, burger-combo add failures. **🛑 DO NOT transplant these to the Philippines.** Note the `com.olo.` prefix means the US app is built on **Olo**, the US restaurant ordering platform `[INFERENCE from the Android package namespace only]` — North America is on a different stack. A separate UK app exists too (`com.jollibeeuk.app`). **JFC runs market-specific apps, i.e. a fragmented per-market ordering stack — that fragmentation is the actual orchestration story.**

## Section 8: PCI DSS

**NOT FOUND.** No PCI DSS statement, AOC, SAQ level or compliance claim for JFC anywhere.

From code: JFC **pushes PAN out of its own scope** — the privacy notice disclaims collecting or storing card data, card entry happens on `checkouts.maya.ph` (PSP-hosted redirect), and payment payloads to their BFF are PGP-encrypted to `falcon@jfcapps.io`. **Consistent with an SAQ A / A-EP redirect posture. This is an inference from architecture, not a documented claim — flag it as such if used.**

## Section 9: ⚠️ A security observation — do NOT reference in outreach

`https://order.greenwich.com.ph/env.js` publicly exposes `scPwdService.keys.clientSecret` (a UUID), plus `clientId` and `apiKey` for `sc-pwd.jfcapis.com` — **a server-side-looking credential triple shipped to the browser.** I confirmed `clientSecret` is present in the file I fetched. The same `scPwd` apiKey is reused across all three brands. **No credential was used.**

It is not a payment credential, but it is a real finding about engineering maturity. **🛑 Do not mention it in outreach — it reads as hostile and would end the conversation.**

## Section 10: ICP Score — 16 / 29 → 🟢 Medium

| Signal | Max | Score | Evidence |
|---|---|---|---|
| Transaction volume | 5 | **3** | PHP 455bn SWS and 10,421 stores are enormous, **but the card-not-present slice is undisclosed and the one hard proxy points below the gate.** Scored 3, not 5, because the *addressable* volume is unmeasured |
| Orchestration posture | 4 | **4** | **Greenfield — exactly two direct PSPs, no orchestrator.** Verified first-hand in their own `env.js` allowlist |
| Operates 3+ countries | 3 | **3** | **33 countries**, confirmed entities in PH, SG, VN, KR, MY |
| Multiple PSPs in parallel | 3 | **0** | ⬜ **Deliberate zero.** Exactly **two** PSPs, and they are complementary (Maya for cards+wallet, GCash for its wallet) rather than parallel/redundant. This row does not honestly fire |
| Local rail gap in a top market | 3 | **3** | **No QR Ph, no BNPL, no instalments, no Apple/Google Pay, no GrabPay, no ShopeePay, no OTC cash** in the PH market — a four-method checkout |
| Recent market expansion | 2 | **2** | **All Day Fresh (KR) April 2026** · Compose into PH + SG · 1,126 new stores in 2025 |
| Known payment issues | 2 | **2** | **Five-article GCash refund-dispute workflow**, manual store-level refunds, 3–7 day SLA, screenshot evidence, documented "payment went through but the order didn't" |
| Recent funding | 2 | **0** | ⬜ Listed, profitable, self-funding acquisitions. No raise |
| Traffic outside home market | 2 | **0** | ⬜ **Deliberate zero.** The measured domain is 81.52% PH, and it is the wrong domain anyway. Group-level offshore mix is **unmeasured** — I will not score a row on data I do not have |
| Competitor on orchestration | 2 | **0** | ⬜ Not researched — no PH or SEA QSR peer evidenced on an orchestrator |
| Payment job postings | 1 | **0** | ⬜ **No payments-specific hire, no RFP found** |
| **TOTAL** | **29** | **16** | 🟢 **Medium** |

**Five deliberate zeros and a deliberately reduced volume score.** The honest read: this account passes size, territory and industry comfortably, has a genuinely verified greenfield orchestration posture and a real rail gap — but **the addressable payment surface is undisclosed and the aggregator dependency may be most of it.**

## Section 11: Outreach Angles, Ranked

1. **They built the same ordering-and-payment stack three times for four brands** — Chowking and Mang Inasal on current Falcon, Greenwich on a prior generation, Red Ribbon on a different app entirely — **and every one terminates in exactly two domestic PSPs with no redundancy.** Auditable from their own public JavaScript. **A consolidation argument, not an approval-rate one.**
2. **The flagship brand has no first-party checkout at all** — `jollibee.com.ph/order` sends customers to GrabFood and foodpanda, while Chowking, Mang Inasal, Greenwich and Red Ribbon each run their own. **That asymmetry inside their own estate is the sharpest possible observation.**
3. **A four-method checkout in the Philippines** — card, cash, GCash, Maya. No QR Ph, no BNPL, no instalments, no Apple/Google Pay.
4. **The Korea integration.** 3,000+ Compose Coffee stores and 172 All Day Fresh stores acquired, in a local-PG-gated market, being absorbed into a Philippine parent's estate. **Ask the question — do not assert an answer.**
5. **The manual, store-level GCash refund workflow** with a 3–7 day SLA and screenshot evidence. Frame as an inference about volume, not a measurement.
6. **The redesigned PH delivery app** — a checkout rebuild is the best-timed trigger. **Verify the year first.**
7. **Maya is the single acquirer for cards.** `"paymaya-redirect":"Maya or Credit/Debit Card"` — one acquirer, no fallback, for every card transaction across the group's PH storefronts.

## Section 12: Do NOT Say

- ❌ **Any transaction number.** Three derivations disagree by 100×. Not established.
- ❌ **AsiaPay / PesoPay as their current gateway.** That is from **2011** and the domain is dead.
- ❌ **Total JFC delivery GMV** as addressable. Aggregators are merchant of record on the flagship brand's online orders.
- ❌ **Any approval-rate, MDR, decline or chargeback figure.** Zero visibility — it would be fabrication.
- ❌ **A COD share for JFC.** Not found.
- ❌ **The US/Canada app's 100k installs or 4.8★** as Philippine data. Different app, different stack (Olo), out of territory.
- ❌ **The 2020 "delivery = 5% of PH SWS" figure.** Six years stale.
- ❌ **Apple Pay or Google Pay** as PH capability. North America only.
- ❌ **Atome as confirmed** — the partnership page is undated and unfetched, and Atome appears in **no** bundle.
- ❌ **The exposed `clientSecret`.** Reads as hostile.
- ❌ **Any Korean or Vietnamese PSP.** Zero evidence. Do not speculate.
- ❌ **North American payment volume** as JFC's — the US estate is **franchised**.
- ❌ **"Jollibee the brand" and "Jollibee Foods Corporation the group"** interchangeably. Be explicit which one every figure covers.
- ❌ **Coffee Bean & Tea Leaf's payments** as JFC's without evidence — it is 80%-owned but operates globally on its own stack.
- ❌ **QR Ph on foodpanda** as JFC's rail. It is foodpanda's.

## Section 13: Research Confidence

**Overall: HIGH on the PH web payment stack. LOW on volume. ZERO on Korea and Vietnam.**

- ✅ **Verified first-hand by me:** the 105-byte `payment-types` enum (HTTP 200, quoted in full), Greenwich's `features: ['maya','gcash']` and all three PSP referrer hosts, `jollibee.com.ph/order` returning 0 `payment` hits with only GrabFood and foodpanda links, and the exposed `clientSecret`.
- ✅ **Fetched primary-mirror text:** FY2025 results (SWS, revenue, operating income, EBITDA, store count, 33 countries, Singapore estate) and the Q1 2026 earnings transcript (10,421 stores, the CFO's drive-thru-is-digital quote).
- ✅ **Rigorous false-positive control.** On `redribbondelivery.com.ph`, `cod` matched **84 times but only 1 was genuine** (`"cod":"Cash"`) — **82 were `code`/`promoCode`.** Also caught: `"name":"Mayantoc"` (a PH municipality) matching `maya`. No surviving `omise`/`emi`/`cred`/`tap` hits.
- ⚠️ **Blocked:** `help.jollibee.com.ph` (403 Cloudflare, both tools) · `help.highlandscoffee.com.vn` (403) · `highlandscoffee.com.vn` (403) · `malaymail.com` ×2 (403) · the live `GET /v1/payments/options` call (blocked by the permission system — it required replaying the site's own API key; correct call, not retried) · the Jollibee native app binary.
- ⚠️ **Unresolved:** own-app vs aggregator split · any current digital-sales % from a primary source · whether "digital sales" includes drive-thru and aggregator orders · COD share · PCI documentation · Compose Coffee's PSP · Highlands Coffee's gateway · whether the global CDO seat was refilled · the SuperFoods ownership chain (60% vs wholly-owned) · the Compose price (US$238M vs US$340M) · the redesigned app's launch year · store count by brand × territory.

</details>
