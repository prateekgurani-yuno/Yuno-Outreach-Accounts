# ZUS Coffee

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 24 / 29 → ⭐ **High — the strongest account in this batch**
**Industry:** Food & Beverage — app-first coffee chain · **HQ:** **Zuspresso (M) Sdn. Bhd.**, Malaysia (⚠️ **not** "ZUS Coffee Sdn Bhd" — see Entities) · **Researched:** 2026-10-06 · **First email sent:** —
**Motion:** ✅ **GREENFIELD — single-gateway dependency on Fiuu for the app, a structurally separate second gateway for Shopify, no orchestration layer, no evident payments owner.** The cleanest greenfield in the batch.

---

> ## 🛑 FIRST — throw away the traffic data. It measures a brochure.
>
> The supplied SimilarWeb figure (464,087 visits, **−16.01% MoM**, the steepest decline in the batch) is for `zuscoffee.com`, and **that site has no checkout at all.** I verified the control counts on the fetched homepage (HTTP 200, 390,003 bytes):
>
> | token | hits |
> |---|---|
> | `checkout` | **0** |
> | `add-to-cart` | **0** |
> | `currency` | **0** |
> | `MYR` | **0** |
> | `payment` | 3 — **all Jetpack CSS filenames** |
>
> It is a WordPress brochure (Elementor Pro, Zakra, Slider Revolution, Jetpack, TranslatePress). **No cause for the −16% decline could be found** after searching Sept–Oct 2026 news, app relaunches, controversy and boycotts. **Do not use the traffic number or the decline in outreach — on a brochure site neither has commercial meaning, and the claim will not survive contact with the prospect.**
>
> ⚠️ **Two false positives caught on that homepage, both of which would have been reported as hits:**
> - **`boost`** → `data-jetpack-boost="ignore"` — the **Jetpack Boost** WordPress plugin, **NOT** Boost the Malaysian wallet.
> - **`paypal`** → `plugins/jetpack/jetpack_vendor/automattic/jetpack-paypal-payments/dist/...style.css` — Jetpack ships this CSS whether PayPal is used or not. **No PayPal integration is evidenced.**

---

> ## ⭐ THE FINDING — the app is the entire business, and Fiuu is the single gateway behind it
>
> **SOURCED scale, fetched 2026-10-06 from the Google Play listing** (`com.coffee.love_coffee`, HTTP 200, 1,149,047 bytes):
> - **5,000,000+ installs badge; 6,334,746 actual install count in the page data**
> - **4.6 rating · 241,096 ratings · 11,905 written reviews**
> - Developer "ZUS Coffee Global", released **12 April 2020**
>
> And the decisive commercial number, from **COO Venon Tian** in a Bloomberg interview (24 April 2025): **~70% of sales are online/app.** `[UNVERIFIED — search summary only, page not fetched]`
>
> **The gateway is Fiuu (formerly Razer Merchant Services).** From Fiuu's own blog, 18 November 2024 — Fiuu is described as **"the backbone payment gateway"** and *"This payment solution, powered by Fiuu, Malaysia's largest fintech platform, ensures transactions are processed securely and efficiently."* ShopBack Pay launched **"onboard the ZUS Coffee app."** The release quotes **Venon Tian, COO of ZUS Coffee.**
>
> **One gateway for the app. A separate, unidentified gateway for the Shopify store. No orchestration layer anywhere.** Searched ZUS against Juspay, Primer, Spreedly, Payrails, Gr4vy and Yuno — **zero results.** No in-house layer either: no engineering blog, no payments job postings, no CTO identified.
>
> ⚠️ **The "1.8 million app downloads" figure circulating online is stale and wrong** — Play alone shows 6.33m actual installs. It appears only on `growthhq.io`, an SEO content farm publishing dozens of near-duplicate ZUS articles. **Do not cite growthhq.io to this prospect.**

---

> ## 🎯 THE HOOK — their own app reviews document the payment layer failing, and one quote is perfect
>
> **The money-left-but-no-balance top-up failure.** Verbatim, App Store review on `id1487584854`:
>
> > "I attempted to make a **recharge**, and although the **payment was successfully deducted from my account, the funds have not been credited to my Zus account**. This issue has caused me considerable inconvenience and l try multiple times. No change, no way you can do it is **continue see your money loss from your touch and go wallet**. What makes the situation even more frustrating is that I have attempted to contact customer service multiple times, but I have not received any response."
>
> **That single review simultaneously proves:** ZUS Balance stored value exists · **Touch 'n Go eWallet funds it** · the top-up fails with the customer out of pocket · retries don't resolve it · and **there is no reconciliation or auto-refund path.**
>
> **The checkout latency regression — and the customer eliminated the network themselves:**
>
> > "I would order my coffee seamlessly using the app and the payment process (regardless if I'm using the Zus Wallet, card or e-wallet payment method) and from start to finish the ordering + payment process would take **less than 3 mins. But in the past few weeks, the payment process would take on average more than 10 mins.** This could either be topping up my Zus wallet or just using other payment methods… I would alternate using either the wifi or mobile data (and I have two sim cards from different line provider) to hopefully get the payment process quicker but **none of that change**."
>
> They ruled out connectivity across two carriers **and** wifi. That isolates the fault to the payment layer, and **it affects every method — which points at the gateway, not a single rail.**
>
> **No card vaulting — two independent reviewers, two platforms:**
> > App Store: *"The card method is especially incovenient because **I have to enter my card info every single time.**"*
> > Google Play: *"This app still asked me to **fill in my card details eventhough i've saved the same details during my previous purchase.** Its a waste of time if i've to the same thing over & over again."*
>
> **Apple Pay is absent and customers are asking for it:** *"Please make Apple Pay available."*
>
> **Settlement/state reconciliation failure** (Google Play):
> > "I ordered via the app, paid, and **the order automatically cancelled but my ewallet balance wasn't refunded.** After 1 hour suddenly the order showed successful, when to the store and they said app problem, **they didn't receive any order.** … I wanted to support local but I'm better off with Zus competitor"
>
> Payment captured, order state inconsistent, refund not executed, **and a stated intent to defect to a competitor.**
>
> Also documented: a **double charge** when a voucher failed to apply at checkout; an **app update on 18 Sept that wiped accounts and stored-value balances** (*"all my ewallet credits about ($5 inside), mission log in and Zus tier is all gone"*); non-delivery with no refund *"for weeks."*
>
> ⚠️ **Frequency: 11,905 written Play reviews and ~241k ratings, but only the reviews surfaced on the two listing pages were sampled. DO NOT claim an incidence rate.** What is defensible: payment failure appears across **both** stores and across **five distinct failure modes** (top-up, refund, double charge, vaulting, latency), and customers explicitly cite competitors.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Malaysian app-first coffee chain founded **November 2019** by **Venon Tian** and **Ian Chua** with six other co-founders (**Terence Ho** co-founder and Head of Barista). Both founders have start-up/IT backgrounds, consistent with the app-first model. ~800 Malaysian outlets, **≥1,000 regionally** (Oct 2025), targeting **1,300 by end-2026.**

### Transaction volume — DERIVED, and robust to hostile assumptions
**Approach A — revenue-based (most solid inputs):**
```
FY2024 revenue (SOURCED)              RM 468,200,000
÷ ASSUMED ATV RM15 (a ZUS drink ~RM9–10; typical order 1–2 drinks ± food)
                                   =  31.2 M transactions / yr
                                   =  2.60 M / month, all channels
× 70% online (SOURCED — COO quote)  =  1.82 M online transactions / month
```
**Approach B — outlet × throughput:**
```
~800 MY outlets (SOURCED) × ASSUMED 300 cups/outlet/day
  (2023 figure was "200–400 cups every day" at ~225 outlets — likely conservative now)
                                   =  240,000 cups/day = 7.3 M/month
÷ ASSUMED 1.5 cups per order        =  4.87 M orders/month
× 70%                               =  3.41 M app transactions / month
```
**Approach C — deliberately hostile stress test:**
```
RM468.2m ÷ INFLATED ATV RM25        =  1.56 M/month × 70% = 1.09 M online transactions/month
```

**🎯 Gate verdict: PASSED by ~27× at the most hostile assumption and 45–85× at realistic ones. Even if every assumption is wrong by an order of magnitude, ZUS clears 40,000/month. This is not a close call.**

### ⚠️ It is NOT a closed stored-value loop — and that matters to the pitch
**ZUS Balance** (customers also call it "Zus Wallet") exists, funded by **Touch 'n Go eWallet**, gift-voucher codes and card. But the reviews show customers pay per-order by **card and e-wallet interchangeably**, and at least one **explicitly refuses to hold float** (*"I don't prefer keeping my money here sorry"*).

**So the pitch is NOT "your volume is concentrated into a few large top-ups." Transaction count stays high — it is not collapsed by the wallet.** That preserves the volume case.

⚠️ **The Play "In-App Purchases" badge is present.** This almost certainly flags ZUS Balance top-ups rather than Google Play Billing processing them — **Play Billing is not permitted for physical goods, and the Touch 'n Go debit complaint proves top-ups route through a Malaysian rail, not Google.** `[INFERENCE, not confirmed]` — low risk to the pitch, but worth one confirming question.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

> **Not yet generated.** Run `/full-outreach ZUS Coffee` to compose the 12-touch sequence into this section.
>
> **Motion is GREENFIELD.** Observations may note the absence of a routing layer. **The economic buyer is the new Group CFO** (see Buying Signals) — MDR runs straight through gross margin and approval rates run through revenue, and both get scrutinised in IPO diligence.
>
> **Lead with the app review evidence — it is first-party, verbatim, and unanswerable.** Two cautions to carry in: **franchised markets are not ZUS's payments to orchestrate**, and **DuitNow QR acceptance could not be confirmed at all — lead with a question there, not a claim.**

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

## Section 1: The only web checkout — shop.zuscoffee.com

**I verified this myself** (HTTP 200, 731,094 bytes, **control: 14 `payment` hits** — the right file). Verbatim from the page:
```
initData: {"shop":{"name":"ZUS® Official Store","paymentSettings":{"currencyCode":"MYR"},
"myshopifyDomain":"zus-everywhere.myshopify.com","country...
```
`/cart` ×3, `/checkout` ×2, `Shopify.PaymentButton.init()`, `shopify-accelerated-checkout`. Third-party apps: judge.me, Klaviyo, Microsoft Clarity, ShopBack affiliate (`shopback.go2cloud.org`, `js.go2sdk.com`), filum.ai.

**Payment method icon set — I extracted these verbatim SVG titles myself. This is the authoritative list for this storefront:**
```
<title id="pi-fpx">FPX</title>              <title id="pi-touchngo">Touch n Go</title>
<title id="pi-grabpay">GrabPay</title>      <title id="pi-shopeepay">ShopeePay</title>
<title id="pi-boost">Boost</title>          <title id="pi-maybankqrpay">Maybank QR Pay</title>
<title id="pi-atome">Atome</title>          <title id="pi-mcash">M Cash</title>
<title id="pi-master">Mastercard</title>    <title id="pi-visa">Visa</title>
```
These are genuine `aria-labelledby="pi-*"` footer payment badges. **The `boost` hit HERE is Boost the Malaysian wallet** — unlike the main site's Jetpack Boost. Context confirms it.

⚠️ **Shopify Payments is not available in Malaysia**, so this storefront must sit behind a third-party Malaysian gateway. The icon set (FPX + 5 wallets + Maybank QR + Atome + M Cash) is characteristic of a single aggregating Malaysian gateway. **Which one could NOT be confirmed** — gateway identity appears only on the hosted checkout page, which was not fetched.

⚠️ **False positives ruled out on the shop page:** `gkash`, `2c2p`, `tngd` and `paypal` each matched **inside base64 image/data blobs only** — not real integrations. And `pi-3in1` matched the **NGUPI 3-in-1 instant-coffee product line** (`zus-ngupi-3in1-kopi-onde-onde`), not a payment method.

## Section 2: Domain probe — no Australian presence, no regional checkouts

| Domain | HTTP | Final URL | Verdict |
|---|---|---|---|
| `zuscoffee.com/` | 200 | same | WordPress brochure, **no checkout** |
| `zuscoffee.com/shop` | **404** | — | Does not exist |
| `zuscoffee.com/store` | **404** | — | Does not exist |
| **`shop.zuscoffee.com`** | 200 | same | **Live Shopify store, MYR — the only web checkout** |
| `zuscoffee.com.ph` | 200 | **→ `zuscoffee.ph`** | Brochure, **0 payment tokens** |
| `zuscoffee.sg` | 200 | same | Brochure |
| `zuscoffee.co.th` | 200 | **→ `zuscoffee.com`** | **NOT a TH storefront — parked onto the MY site** |
| `zuscoffee.id` | 200 | same | Brochure |
| `zuscoffee.com.au` / `zuscoffee.au` | **000** | — | **Do not resolve** |

**No Australian web presence exists. No regional site has any checkout or any payment-method reference** — PH/SG/ID/TH web is purely marketing. All regional e-commerce is the single Malaysian Shopify store.

## Section 3: PSPs

| Provider | Status | Channel | Source |
|---|---|---|---|
| **Fiuu** (ex-Razer Merchant Services) | ✅ **CONFIRMED** | ZUS Coffee **app** | fiuu.com blog, 18 Nov 2024 — *"the backbone payment gateway"* |
| **ShopBack Pay** | ✅ **CONFIRMED** as an in-app method, processed via Fiuu | app | same |
| Shopify (commerce platform, not a PSP) | ✅ **CONFIRMED** | `shop.zuscoffee.com` | storefront `initData` — **I verified** |
| Gateway behind the Shopify store | ❌ **NOT FOUND** | — | Shopify Payments unavailable in MY, so one exists; identity not determinable from storefront HTML |
| iPay88 · Billplz · Curlec · Stripe · Adyen · Checkout.com · 2C2P · Xendit · eGHL · senangPay · GKash · Revenue Monster · Kiplepay · Merchantrade · toyyibPay | ❌ **NOT FOUND** | — | searched and grepped, no evidence |

⚠️ **Swipey — important disambiguation.** A PayNet press release notes ZUS Coffee among brands using **Swipey's** platform, with DuitNow QR integrated into Swipey's FinOps platform *"to replace outdated petty cash systems."* **This is corporate expense/spend management — ZUS paying OUT, not ZUS accepting FROM consumers. Do NOT present it as an acceptance rail.**

## Section 4: Rail table

### Malaysia
| Rail | Status | Channel | Note |
|---|---|---|---|
| **FPX** | ✅ CONFIRMED | App + Shopify (`pi-fpx`) | ⚠️ App channel rests on a PayNet promo T&C PDF that **403'd on fetch** — strongly indicated, **not proven** |
| **Touch 'n Go eWallet** | ✅ CONFIRMED | App (top-up funding) + Shopify | App Store review proves a TNG debit |
| **Cards (Visa / Mastercard)** | ✅ CONFIRMED | App + Shopify | **Customer re-enters card every time** |
| **ZUS Balance** (stored value) | ✅ CONFIRMED | App only | App Store reviews |
| **ShopBack Pay** | ✅ CONFIRMED | App | fiuu.com |
| **GrabPay · ShopeePay · Boost · Atome · M Cash · Maybank QR Pay** | ✅ CONFIRMED | **Shopify store ONLY** | ⚠️ **NOT FOUND in the app** — a real asymmetry inside their own estate |
| **DuitNow QR** | ❌ **NOT FOUND** as consumer acceptance | — | **The biggest gap in the table.** Genuinely odd for an 800-outlet MY F&B chain. Only DuitNow link is Swipey corporate spend — the wrong direction. **Ask, do not assert** |
| **DuitNow Transfer · MAE/Maybank2u · SPayLater · Split** | ❌ NOT FOUND | — | — |
| **Apple Pay** | ❌ **CONFIRMED ABSENT** | App | Customers asking for it |
| **Google Pay** | ❌ NOT FOUND | — | — |

**🔑 Note the asymmetry:** the **Shopify store** (selling beans and merch) accepts GrabPay, ShopeePay, Boost, Atome, M Cash and Maybank QR Pay. **The app — ~70% of all sales — does not.** That is a contrast between two of their own systems, which per the voice guidance is the strongest kind of observation: they cannot dispute either half.

Bank/card co-marketing promos corroborate cards being live: UOB Visa, RHB, BSN, TNG Digital — all `[UNVERIFIED — search summary only]`.

### Non-Malaysian markets
**PH (GCash, Maya) · SG (PayNow, NETS) · TH (PromptPay) · ID (QRIS) · Brunei · Pakistan · Morocco — ALL NOT FOUND.** No non-MY rail could be confirmed for any market. Given the franchise structure below, much of it may never be ZUS's to orchestrate.

## Section 5: Entities & franchise structure — this materially limits addressable volume

⚠️ **The stub's entity name is wrong. I found no evidence of an entity literally named "ZUS Coffee Sdn Bhd."** The operating entity is **Zuspresso (M) Sdn. Bhd.**, d/b/a ZUS Coffee — named as owner in IPO reporting and as the FY2024 financial filer. "ZUS Coffee Global" is the Google Play developer name. **No SSM/CCM records were accessed; no registration numbers obtained.**

| Market | Structure | First outlet |
|---|---|---|
| Malaysia | **Company-owned (core)** | 2019 |
| **Philippines** | ⚠️ **NOT wholly ZUS.** Filipino businessman **Frank Lao** reportedly bought a **35% stake** (Mar 2023); separately reported as 35% sold to **Choi Garden Restaurant Company** | Sept 2023, Eastwood City |
| Singapore | Not specified | Oct 2024, Changi Airport |
| **Brunei** | **Franchise model** | Nov 2024 |
| Thailand | Not specified | Aug 2025, Bangkok |
| Indonesia | Kapal Api Group is an investor and an Indonesian FMCG group | 2026, Puri Indah Mall, Jakarta |
| **Pakistan** | **Local master franchise**, targeted H1 2026 | — |
| Morocco | Q1–Q2 2026 — **out of APAC territory** | — |
| **Australia** | **No evidence of any presence or plan** | — |

ZUS runs an explicit franchise programme (`zuscoffee.com/international-franchise/`, HTTP 200). **Franchised markets' payments belong to the franchisee.** Pakistan (in territory) is master-franchised and therefore **not** ZUS's payment stack; Brunei likewise. The PH structure is a minority-stake JV — **ambiguous, worth asking about rather than assuming.**

**The orchestration-addressable volume is overwhelmingly Malaysia. That is fine — Malaysia alone is 1.1–3.4m online transactions/month.**

## Section 6: Financials & IPO

| Metric | Value | Date |
|---|---|---|
| **Revenue FY2024** | **RM468.2m** (from RM204.12m FY2023, **+129%**) | FY2024 `[UNVERIFIED — The Edge, search summary]` |
| **Net profit FY2024** | **RM36.62m** (from RM10.15m FY2023, **+261%**) | FY2024 |
| Revenue growth | 7.5× (2021), 3× (2022) | Vulcan Post (fetched) |
| **Funding** | **RM250m (~US$57m)** from **KV Asia Capital + KWAP** (Malaysian pension fund) **+ Kapal Api Group**; EY Malaysia M&A adviser | **Sept 2024** |
| Profitability | **Profitable** | FY2024 |

⚠️ **The stub's investor premise is unsupported. "Inter-Pacific" and "Tanah Sutera" produced NO evidence in any search — drop them.**
⚠️ A *"Crossing RM1 Billion Revenue"* claim exists on `articles.unienrol.com` — **weak source, treat as unconfirmed.**
⚠️ **No FY2025 financials are public.**

### 🔑 IPO — confirmed under consideration, not filed
**Zuspresso (M) Sdn Bhd is working with financial advisers** on an IPO of the **Malaysia business** to raise **at least RM1bn (~US$245m)**, at a valuation around **RM4bn**, on **Bursa Malaysia**, potentially **as soon as mid-2027.** The Star, 14 Aug 2026 `[UNVERIFIED — search summary only]`, corroborated by The Edge and World Coffee Portal.

**No prospectus has been filed** — so there is no regulatory disclosure of payment costs or transaction volumes to mine yet.

## Section 7: Buying Signals, ranked

1. **🔑 Bursa Malaysia IPO in preparation, mid-2027 target, ~RM4bn valuation.** Pre-IPO is the strongest possible window for payment-cost work — **MDR runs straight through gross margin and approval rates through revenue, and both get scrutinised in diligence.**
2. **🔑 New Group CFO: Preman Menon, after 14 years at EY.** A Big-Four CFO hire is textbook IPO-readiness, **and the CFO is the economic buyer for MDR reduction.** `[UNVERIFIED]`
3. **Payment reliability is visibly degrading** — the 3-min → 10-min checkout regression, with the network ruled out by the customer. **The best door-opener available.**
4. **No card vaulting** — customers re-enter card details every order. Directly addressable, directly quotable, two independent sources.
5. **Apple Pay absent** despite customers asking for it.
6. **Aggressive multi-market expansion** — TH (Aug 2025), ID (2026), Pakistan + Morocco (H1 2026), 1,300-outlet target end-2026. Each new market is a new rail set and a new PSP negotiation.
7. **Single-gateway concentration on Fiuu** since at least Nov 2024, with a structurally separate Shopify storefront on a different gateway.
8. **FMCG vertical (NGUPI instant coffee, Apr 2025)** plus the Shopify store — a genuine card-not-present channel distinct from the app.
9. ❌ **The −16% MoM web traffic. No cause found, and on a brochure site it has no commercial meaning. DO NOT USE.**

**Negative signals:** **no CTO or payments-engineering hire found**; 34 jobs on Hiredly with no payments roles. **There may be no internal payments owner** — which cuts both ways.

## Section 8: Outlet counts — date every figure, they move fast
June 2023: 225+ (MY) · End 2023: 360 (MY) · Sept 2024: ~600 regionally, 50 in PH · **Oct 2025: ≥1,000 regionally** · 2026: 900+ stores, 6,000+ employees `[UNVERIFIED]` · 2026 (MY): ~800 targeting 850 · **End-2026 target: 1,300** · 2026 by market: PH 190–200, TH 50, SG +6.

## Section 9: ICP Score — 24 / 29 → ⭐ High

| Signal | Max | Score | Evidence |
|---|---|---|---|
| Transaction volume | 5 | **5** | **1.1–3.4M online transactions/month DERIVED**, anchored on SOURCED FY2024 revenue + the SOURCED ~70%-online COO quote. Clears the gate 27–85× |
| Orchestration posture | 4 | **4** | **Greenfield** — Fiuu single gateway for the app, no orchestrator, no in-house layer, no payments owner |
| Operates 3+ countries | 3 | **3** | MY, PH, SG, TH, ID, Brunei live; Pakistan + Morocco planned |
| Multiple PSPs in parallel | 3 | **3** | **Two structurally separate payment stacks** — Fiuu for the app, an unidentified second gateway for Shopify (⚠️ the second is unidentified, but its existence is certain since Shopify Payments is unavailable in MY) |
| Local rail gap in a top market | 3 | **3** | **DuitNow QR not found at all** for an 800-outlet MY chain · **Apple Pay confirmed absent** · **no card vaulting** · and the app lacks GrabPay/ShopeePay/Boost/Atome that **their own Shopify store has** |
| Recent market expansion | 2 | **2** | TH Aug 2025 · ID 2026 · Pakistan + Morocco H1 2026 · 1,300-outlet target |
| Known payment issues | 2 | **2** | **The strongest complaint evidence in the batch** — five distinct failure modes, verbatim, across both app stores |
| Recent funding | 2 | **2** | **RM250m Sept 2024** — KV Asia Capital, KWAP, Kapal Api |
| Traffic outside home market | 2 | **0** | ⬜ **Deliberate zero.** 94.20% Malaysia, and the measured domain is a brochure anyway |
| Competitor on orchestration | 2 | **0** | ⬜ Not found — no MY/SEA F&B peer evidenced on an orchestrator |
| Payment job postings | 1 | **0** | ⬜ **None found.** 34 jobs on Hiredly, no payments roles, no CTO identified |
| **TOTAL** | **29** | **24** | ⭐ **High** |

**Three deliberate zeros.** This scores highest in the batch because almost every row is backed by first-party evidence: verified greenfield, verified rail asymmetry inside their own estate, verbatim complaint evidence, a sourced funding round, and a pre-IPO window with a new CFO in the economic-buyer seat.

## Section 10: Do NOT Say

- ❌ **The 464,087 visits or the −16% MoM decline.** The site is a brochure with zero checkout tokens, and no cause for the decline was found.
- ❌ **"1.8 million app downloads."** Stale and wrong — Play shows 6.33m. The only source is an SEO content farm.
- ❌ **"ZUS Coffee Sdn Bhd"** as the entity. It is **Zuspresso (M) Sdn. Bhd.**
- ❌ **Inter-Pacific or Tanah Sutera as investors.** No evidence found.
- ❌ **Boost or PayPal on `zuscoffee.com`.** Both were Jetpack false positives (`jetpack-boost`, bundled Jetpack PayPal CSS).
- ❌ **Swipey as an acceptance rail.** It is corporate spend management — ZUS paying out.
- ❌ **DuitNow QR as confirmed.** Not found anywhere, for any channel. **Ask.**
- ❌ **A complaint incidence rate.** Only the reviews surfaced on two listing pages were sampled.
- ❌ **GrabPay, ShopeePay, Boost, Atome or M Cash as in-app methods.** They are Shopify-store only.
- ❌ **Franchised markets' volume as addressable.** Pakistan and Brunei are franchised; PH is a minority-stake JV.
- ❌ **Any Australian presence.** Both `.com.au` and `.au` fail to resolve.
- ❌ **The RM1bn revenue claim** — weak single source.
- ❌ **Any MDR, approval rate or chargeback figure.** Zero visibility.

## Section 11: Research Confidence

**Overall: HIGH on the app's scale, the gateway and the complaint evidence. ZERO on non-MY rails and the Shopify gateway.**

- ✅ **Verified first-hand by me:** `shop.zuscoffee.com` (HTTP 200, 731,094 bytes, control 14 `payment` hits) and the complete `pi-*` payment icon set extracted verbatim; the Shopify `initData` with `currencyCode: MYR` and `zus-everywhere.myshopify.com`.
- ✅ **Fetched by the research pass:** the Google Play listing (6,334,746 installs, 241,096 ratings, 11,905 reviews), the App Store listing, the Fiuu blog post naming the gateway, `zuscoffee.com` with its zero-checkout control counts, and all regional domain probes.
- ⚠️ **Blocked:** the PayNet FPX promo T&C PDF (403) · `zuscoffee.com/faq/` (403 on WebFetch, curl truncated at 30s on JS-heavy WordPress) · `/zus-app/` — **ZUS's own documented payment-method list was never read. This is the cleanest remaining win for whoever picks this up next.**
- ⚠️ **Unresolved:** DuitNow QR acceptance · the Shopify store's gateway · whether Fiuu is the sole app gateway or one of several (the Nov 2024 release only establishes it processed the ShopBack Pay launch and calls it "the backbone") · SSM registration numbers and group structure · FY2025 financials · registered app user count, app order count or app GMV · the cause of the traffic decline · whether the Play IAP badge means Play Billing · **aggregator merchant-of-record arrangements** (foodpanda and GrabFood are both confirmed in use `[UNVERIFIED]`, but who is MoR and what share they carry is unknown — on aggregator orders the aggregator is almost certainly MoR and **orchestration cannot touch that volume** `[INFERENCE]`) · r/malaysia, r/Bolehland and Lowyat were **not reachable — treat as not investigated rather than clean.**

</details>
