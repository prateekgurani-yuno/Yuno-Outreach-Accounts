# Ruangguru

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 17 / 29 → ⭐ **High**
**Industry:** E-Learning & EdTech — K-12 tutoring, exam prep, adult upskilling · **HQ:** **PT Ruang Raya Indonesia**, Jakarta (founded 1 April 2014); **99.99% owned by Ruangguru Pte Ltd, Singapore** (6 Battery Road #38-04) · **Researched:** 2026-10-06 · **First email sent:** —
**Motion:** 🛑 **IN-HOUSE — they built a multi-brand, multi-country payment layer.** Verified first-hand: a **41-member payment-channel enum** in their own production JS, their own channel taxonomy with their own numeric IDs, and their own API gateway. **Never say they need orchestration.** The pitch is TCO, consolidation and the recurring-rail gap.

---

> ## ⭐ THE FINDING — a 41-channel payment enum, recovered from their own bundle
>
> `https://cdn-web.ruangguru.com/re-payment/_next/static/chunks/pages/_app-582fc9feab452616013f.js` — **I fetched it myself: HTTP 200, 2,084,354 bytes.** Extracted by brace-matching the single `Decode.$$enum([...])` block. Exact membership, in file order:
>
> ```
> bni-va, credit-card, bca-manual, bca-va, bca-klikpay, mandiri-clickpay,
> mandiri-echannel, indomaret, alfa, briva, danamon-online, cimb-clicks,
> gopay, shopeepay, bri-epay, permata-va, akulaku, voucher, ecoll, vt,
> momo, onepay-atm, onepay-cc, ovo, payoo, web-payoo, kredivo,
> pay-at-store-ba, pos-indonesia, apple-iap, alfa-mt, full-payment,
> new-apple-iap, ccpp, dana, payatall-cash, viettel-post,
> ccpp-bank, ccpp-otc, ccpp-e-wallet, ccpp-cc
> ```
>
> **I independently confirmed presence in that file** for `gopay`, `shopeepay`, `ovo`, `dana`, `kredivo`, `akulaku`, `indomaret`, `alfa`, `briva`, `bca-va`, `permata-va`, `ecoll`, `momo`, `payoo`, `viettel-post`, `apple-iap`, `ccpp-cc` and `vt`.
>
> **Two more enums from the same bundle prove one layer serves everything:**
> ```
> Brands:   ['Ruangguru','Kalananti','Kienguru','Startdee','ruangguruStaging',
>            'StartdeeStaging','KienguruStaging','schoters','skillacademy']
> Products: ['RUBEL','RGDB','COIN','OTG','RLO','DP','REPAYMENT','BELANJA','SKILLACADEMY',
>            'BA','BRAINACADEMY','RUANGLES','RUANGGURU-PRIVAT','ENGLISHACADEMY','RUANGUJIBUNDLE']
> States:   ['SUCCEED','IN_PROGRESS','IN_PAYMENT_VERIFICATION','CONFIRMED','EXPIRED',
>            'CANCELLED','FAILED','SYSTEM_FAILED','-']
> ```
>
> **Ruangguru, Brain Academy, ruangbelajar, Ruangles, English Academy, Skill Academy, Kien Guru (Vietnam), Startdee and Schoters all ride one checkout codebase.** `IN_PAYMENT_VERIFICATION` as a first-class state means **manual/async bank-transfer reconciliation.**
>
> **Their own channel taxonomy, with their own numeric IDs** (from the Ruangguru-side `payment-web` bundle):
> ```js
> IZ={MINIMARKET:25,TRANSFER_VIRTUAL_ACCOUNT:29,TRANSFER_BANK:30,
>     CARDLESS_INSTALLMENTS:32,E_WALLET:33,INSTANT_PAYMENT:34,CREDIT_CARD_OR_DEBIT_PAY:70,...}
> ```
> **A merchant on a single PSP uses the PSP's codes. These are abstractions OVER PSPs.** The method catalog is server-driven (`paymentMethodParents`, each method carrying `{description,expiryTime,id,isInstallment,logo}`) — **the frontend is gateway-agnostic and renders whatever the backend returns.**
>
> ⚠️ **NO PSP BRAND NAME APPEARS ANYWHERE IN CLIENT CODE.** A sweep across all 34 downloaded files for `midtrans|veritrans|xendit|2c2p|doku\.com|nicepay|faspay|espay|duitku|finpay|adyen|braintree|checkout\.com|primer\.io|gr4vy|payrails|spreedly|juspay` returned **ZERO matches.** What exists instead are *channel codes*: `ccpp-*` (four sub-channels — `CCPP` is 2C2P's own SDK namespace) and `vt` (Veritrans, Midtrans's legacy name, whose APIs are still `VT-Web`/`VT-Direct`). **These are strong inferences from naming conventions, NOT facts.**
>
> **🛑 Safe phrasing for outreach:** *"your checkout enumerates two separate gateway families plus direct bank VA products under your own channel taxonomy."* **Do NOT write "Ruangguru uses Midtrans and 2C2P."**

---

> ## 🎯 THE HOOK — card is their only automatic renewal rail, in a market where almost nobody has a card
>
> **Recurring billing exists and it is card-only.** Verbatim from `payment-web/_app-7d5c97b284027930.js`:
> ```js
> SN.Literal("CREDIT_CARD_RECURRING")          xi={ccRecurring:"cc-recurring"}
> isRecurring:SN.Boolean, subscriptionStartDate:SN.String,
> initialRecurring:SN.Boolean, totalOutstandingBalance:SN.Number
> SN.Record({sequence,scheduleSerial,installmentSerial,packageMappingSerial,isAutoDebit:SN.Boolean})
> .details.find(e=>"auto_debit"===e.type)
> ```
> Their own consent modal, in Indonesian, verbatim:
> > `title:"Penting! Cicilan Kartu Kredit"`
> > `nudgeText:"Paket akan dibayar berkala dengan <b>Kartu Kredit</b>"` — *"Package will be paid periodically with Credit Card"*
>
> And a **self-built instalment scheduler**, not a PSP subscription object — `dueDateType` ∈ `DAYS` | `FIXED`, with strings *"Akan di auto debit "+i+" hari setelah cicilan sebelumnya"* and *"Akan di auto debit pada "+r*.
>
> **The consequence is the pitch.** There is **no e-wallet autodebit** — GoPay, OVO, DANA and ShopeePay appear only as one-shot channels. **No GoPay autodebit, no OVO recurring, no bank direct debit anywhere in the 41-channel enum.**
>
> **So for the large majority of Indonesian learners who do not hold a credit card, renewal is a MANUAL re-purchase every term** through VA, minimarket or e-wallet. Their own guard string confirms they are managing dunning by hand:
> > `repurchasedSimilarPackage:"Kamu sudah memiliki paket aktif yang sama dan cicilan pembayaran yang belum lunas."`
>
> **A subscription business whose only automatic renewal rail is the one payment instrument its market barely has.** Recovery, retry, network tokenisation and card-on-file lifecycle (expiry, reissue) are all theirs to maintain.
>
> **And there is observable catalogue drift between their own two checkouts.** I verified it: **`qris` appears ZERO times in the Skill Academy `re-payment` enum**, while QRIS is confirmed on the Ruangguru side (`QR_CODE` mode, `qrImageUrl`, `qrOrgName`, `qrOrgId` in `payment-web`) and listed on english-academy.id. **LinkAja** likewise appears on the English Academy FAQ but is **absent from the `re-payment` enum.** Shared backend, forked frontends, drifting method catalogues.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Indonesia's largest online learning platform. Products per their own `llm-info` page (fetched): **ruangbelajar, Ruangguru Privat, Ruanguji, Mathchamps, Ruangguru For Kids, Dafa Lulu, Ruangkelas (school LMS), Champions Wonderlab (STEAM), AIRIS (AI learning assistant)** — plus English Academy, Brain Academy Online/Center and Skill Academy, all still live per the T&C. **"lebih dari 40 juta pengguna"** (40M+ users) and **31.1M cumulative app downloads since 2014.**

**SimilarWeb total visits:** **11.16M** (Aug 2026), **+32.9% MoM**, **85.07% mobile web**, **Indonesia 98.80%** — supplied by Prateek, Similarweb PRO. The most concentrated account in the batch. **Cross-border is explicitly NOT the angle.**

### ✅ The app-store trap — resolved, and it resolves in Yuno's favour
**This was the highest-stakes question on the account and it should have killed it. It doesn't.**

| Finding | Evidence |
|---|---|
| **iOS users are deliberately sent OUT to a browser** to pay at `bayar.ruangguru.com` | Ruangguru's own help article *"Cara Bayar Ruangguru untuk Pengguna iOS"* walks through it. Methods named: minimarket, virtual account, bank transfer, credit/debit card, online banking, GO-PAY. **Worked example is an Indomaret barcode. No Apple IAP step.** |
| **Android in-app flow terminates on Ruangguru's own checkout** — step 9 is *"Pilih metode pembayaran"*, then **"Lakukan pembayaran dan tunggu konfirmasi dari admin maksimal 1×24 jam"** | Fetched help article |
| **No Google Play Billing channel exists in the enum at all** | Swept all 28 JS files for `google.?play\|play.?billing\|gpb_\|playstore` → 12 hits for `iap`, **1** for `Playstore` (a store link), **ZERO Play Billing identifiers** |

**🔑 Why the "1×24 jam admin confirmation" line is decisive: Google Play Billing and Apple IAP settle instantly and cannot offer minimarket cash or bank virtual accounts. A 24-hour confirmation window on a VA/minimarket rail is categorically a merchant-operated PSP stack.** The iOS browser hand-off is the textbook Apple-IAP-avoidance pattern.

**So the 85% mobile share is addressable revenue, not store-locked revenue.**

⚠️ `apple-iap` and `new-apple-iap` **do** exist in the enum — so Apple IAP is or was a tracked channel in their own ledger, and `new-apple-iap` implies a migration. But their own iOS help page steers users off it.
⚠️ **Open risk: AIRIS "Stellar"** (the paid AI tier) — **whether that tier bills via store IAP could not be established.** This is the single question that could still undercut the case. **Ask it.**
⚠️ The only sources claiming store billing is primary were `subger.com` aggregator pages — **low-quality SEO content, not treated as evidence.**

### Billing model — one-off prepaid packages, NOT recurring subscriptions
From the fetched T&C (`ruangguru.com/terms-conditions/apps`), entity stated as "PT. Ruang Raya Indonesia":
- **ruangbelajar & Brain Academy Online: prepaid packages for fixed durations. NO auto-renewal — "users must actively repurchase."** SOURCED.
- **Instalments are a first-class product:** English Academy and Brain Academy Online offer **2×, 3×, 4×** plans; Brain Academy Center offers 2× or 3× manual instalments **plus auto-debit.**
- Brain Academy Center *"Biaya Fasilitas"* quoted as **Rp 5,000,000.**

**🎯 This is strictly BETTER for an orchestrator than a card-on-file recurring book:** no auto-renewal means **every renewal is a fresh, manually initiated, checkout-exposed transaction** — more checkouts, more auth events, more abandonment, more method-mix sensitivity. **And the 2×/3×/4× instalment plans multiply transaction count per sale by 2–4×.**

### Transaction volume — DERIVED, arithmetic shown
**No paying-subscriber count is disclosed anywhere.** All published figures (40M users, 31.1M downloads, 22M users in 2020) are **registered/download volume — do NOT use them as a payer count.** The only defensible route is revenue ÷ ticket.

```
FY2021 revenue (SOURCED, Katadata)        US$102.69 M
IDR/USD 2021 avg ≈ 14,300 (ASSUMED)    →  Rp 1.469 trillion
```
| Blended effective ticket (ASSUMED) | Transactions/yr | **Transactions/month** | Clears 40k? |
|---|---|---|---|
| Rp 800,000 (mix-weighted to discounted ruangbelajar + Skill Academy) | 1,836,000 | **153,000** | ✅ 3.8× |
| Rp 2,500,000 (aggressively skewed to premium) | 587,600 | **48,967** | ✅ 1.2× |
| Rp 5,000,000 (every transaction a top-tier package — **not credible**) | 293,800 | 24,483 | ❌ |

**The Rp5m row is the only failing one, and it requires assuming ZERO Rp50k–Rp725k transactions — which directly contradicts the sourced Skill Academy (Rp50,000–Rp1,000,000) and ruangbelajar (Rp725,000 discounted) price points. Reject it.** Note the 2×/3×/4× instalments *increase* counts above these figures, so all rows are conservative.

**Haircut for post-COVID contraction:** assume revenue has halved since the 2021 peak `[INFERENCE]`. At Rp800k ticket that still yields **~76,500/month.**

**Sanity check:** 40,000 transactions would need only a **0.36% visit-to-purchase rate** on 11.16M visits. At 0.5% → 55,800/month.

**🎯 Gate verdict: CLEARS. Label DERIVED** (anchored on a SOURCED revenue figure; ticket mix ASSUMED). Central estimate **~75,000–150,000/month**, conservative floor ~49,000. **Nothing here is a sourced sub-40k figure, so there is no basis to reject on volume.**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

> **Not yet generated.** Run `/full-outreach Ruangguru` to compose the 12-touch sequence into this section.
>
> **Motion is IN-HOUSE.** Per `/full-outreach` Step 6a, respect the build decision — they have paid to build this across three countries. **Anchor on opportunity cost, maintenance TCO and the recurring-rail gap, never on "the build was wrong."**
>
> **Also read `.claude/reference/subscription-payments.md`** — this is a subscription/recurring model. §4 (the app-store trap) has been checked and cleared, but **the AIRIS Stellar question must be resolved before sending.**
>
> **🛑 Do NOT lead with payment complaints — the evidence base is too thin to cite specifics (see Section 6). Lead with the AIRIS launch and the recurring-rail asymmetry.**

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

## Section 1: Entities

| Entity | Detail | Confidence |
|---|---|---|
| **PT Ruang Raya Indonesia** | Operating entity, Jakarta. Founded **1 April 2014.** Named verbatim as "PT. Ruang Raya Indonesia" in the T&C | **CONFIRMED, HIGH** |
| **Ruangguru Pte Ltd (Singapore)** | **Singapore holdco owning 99.99% of PT Ruang Raya Indonesia — 6,494,309 shares.** Registered **6 Battery Road #38-04, Singapore 049909.** Remaining 0.01% held by co-founder **Muhammad Iman Usman** | **CONFIRMED, HIGH** — multiple independent Indonesian outlets with share counts. CEO Belva Devara publicly addressed the "owned by Singapore" controversy in April 2020 |
| **Kien Guru (Vietnam)** | Entered 2019; *"served over 2.5 million students in Vietnam over four years."* **Acquired Vietnamese edtech Mclass in May 2023** | MEDIUM — confirmed operating May 2023, **current status unconfirmed.** No Vietnamese legal entity name found |
| **StartDee** | Thai market vehicle per Katadata (fetched) | MEDIUM — 2023 vintage, current status unknown |

⚠️ **The bundle corroborates the multi-country footprint independently of press:** the brand enum carries `Kienguru` and `Startdee`, and the channel enum carries Vietnam-specific rails (`momo`, `payoo`, `web-payoo`, `onepay-atm`, `onepay-cc`, `viettel-post`) plus **Thai-script i18n strings** for `bank_transfer` and `virtual_account`.

**Merchant-of-record read:** 98.8% of traffic is Indonesian, and acquiring is almost certainly done by the **Indonesian opco onto domestic rails** — that is what BCA/BRI VA and Indomaret/Alfamart require, since they are IDR-domestic and need a local entity `[INFERENCE]`. **The Singapore holdco is the likely locus of group-level vendor contracting and finance decision-making, not the acquiring entity.**

## Section 2: Payment hosts and bundle evidence

**Pages fetched (all HTTP 200):**
| URL | Bytes | Note |
|---|---|---|
| `ruangguru.com/` | 292,938 | HubSpot-built marketing site |
| `skillacademy.com/` | 766,332 | Next.js |
| `english-academy.id/` | 460,063 | **contains the full method list in its FAQ** |
| `bimbel.ruangguru.com/` | 292,938 | **redirects to `www.ruangguru.com`** — no separate Brain Academy storefront |
| **`bayar.ruangguru.com/`** | 1,655,585 | Next.js app `payment-web` |
| **`bayar.skillacademy.com/`** | 57,158 | Next.js app `re-payment` |

**Payment hosts discovered:** `bayar.ruangguru.com`, `bayar.skillacademy.com`, **`gw.ruangguru.com` (their own API gateway)**, `gw-staging.ruangguru.com`, `payment.sirogu.com` (staging base path), `e-meterai.skillacademy.com`, `account.ruangguru.com`, `rea.ruangguru.com`.

Config string, verbatim:
```
stgBasePath:r.env.STG_BASE_PATH||"http://payment.sirogu.com",
prdBasePath:r.env.PRD_BASE_PATH||"https://bayar.ruangguru.com"
apiEndPoint:"https://gw-staging.ruangguru.com",country:"id"
```

**Two separate Next.js payment apps on one CDN:** `payment-web/_app` (2,041,346 bytes) and `re-payment/_app` (2,084,354 bytes).

⚠️ **Control counts are LOW and here is why:** literal `payment` occurrences are `payment-web` = 3, `re-payment` = 1. **The apps are ReScript/Melange + Tamagui compiled — payment semantics live in encoded variant tables, not the word "payment."** Both bundles nonetheless carry the full channel enums, so **these are the right files.** Every other chunk had ≤1 hit (framework/polyfill/webpack runtime) — correctly identified as wrong files.

### i18n payment-category catalog, verbatim
```
ewallet -> Dompet Digital          creditcard -> Kartu Debit / Kartu Kredit
bank_transfer -> Transfer Bank     virtual_account -> Transfer Virtual Akun
minimarket -> Minimarket           momo -> momo          payoo -> Payoo
ccpp -> CCPP Payment               emoney -> E-Money
viettel -> Thanh toán tiền mặt khi nhận hàng (COD)
```
Note **"CCPP Payment" is shown to users as a literal label** — they surface a gateway's SDK namespace in their own UI.

### ⚠️ False positives ruled out — all checked with ±60–200 chars of context
- **`Snap` ×22** in `payment-web` → **NOT Midtrans Snap.** All are Tamagui Sheet `snapPoints` / `dismissOnSnapToBottom`, CSS `box-snap`/`line-snap` property maps, and XState `getSnapshot()`. Example: `{scrollBridge:a,position:l,snapPoints:s,frameSize:u,open:c}=U("SheetScrollView",e)`.
- **`Doku`/`doku` ×6** on skillacademy.com → **"dokumen"** (*"Mengelola Data dan Dokumen Administrasi Perkantoran"*). **Not DOKU.**
- **`doku` ×3** on english-academy.id → **"Gondokusuman"**, a Yogyakarta district in a branch address. **Not DOKU.**
- **`Permata` ×4** on english-academy.id → **"Permata Taman Yasmin"**, a Bogor branch name. *(Permata Bank is independently confirmed as a rail via `permata-va` in the enum.)*
- **`stripe` ×2** on ruangguru.com → Bootstrap `@keyframes progress-bar-stripes`. **Not Stripe.**
- **`dana`** → confirmed as **DANA the wallet**, not the ordinary Indonesian noun for "funds", because there is a **`t.Dana=j` icon component** in the asset registry alongside the `dana` channel code.

## Section 3: Orchestrator classification — IN-HOUSE, high confidence

1. **Own payment domains + own API gateway.** Checkout is `bayar.*`, talking only to `gw.ruangguru.com`. **No PSP-hosted checkout, no Snap.js, no PSP iframe, no redirect-to-gateway SDK anywhere in 2MB of bundles.**
2. **Own channel taxonomy with own numeric IDs** — abstractions over PSPs, not a PSP's codes.
3. **Two-plus gateway families live simultaneously** (`ccpp-*` and `vt`) alongside direct bank products (`ecoll`, `briva`, `bca-manual`) — the classic multi-PSP fan-out.
4. **Server-driven method catalog** — method availability, and therefore routing, is decided backend-side.
5. **They render their own payment instruction pages** — own VA-number display, own QR rendering, own Indomaret step-by-step UI — instead of handing off to a PSP's hosted page.
6. **One layer spans 6+ brands and 3 countries** (ID/VN/TH locales, Kien Guru + Startdee brands). This is a platform, maintained in-house.
7. Searches for `Ruangguru "payment orchestration" OR "payment routing"` and for Juspay/Spreedly/Primer/Gr4vy/Payrails returned **nothing.**

**🔑 Tell-tale of in-house cost:** two **separate** Next.js checkout apps with **divergent channel sets** over one payment backend. **They are maintaining parallel checkout frontends with observable drift** (verified: `qris` = 0 in `re-payment`; LinkAja on the English Academy FAQ but absent from the enum). **Duplicated effort, and it is visible from outside.**

⚠️ **What this does NOT establish:** whether any genuine routing/failover logic exists. The decision is server-side at `gw.ruangguru.com` and **invisible from the client.** "In-house orchestration layer" describes the **architecture**; the **sophistication is unverified.** Do not claim they do cost- or success-rate-based routing.

## Section 4: Indonesian rail table

| Rail | Status | Evidence |
|---|---|---|
| **QRIS** | ✅ CONFIRMED (Ruangguru side) | `<li>QRIS</li>` on english-academy.id; `QR_CODE` mode + `qrImageUrl`/`qrOrgName`/`qrOrgId`/`hideQrisIcon` in `payment-web`. ⚠️ **`qris` = 0 in the Skill Academy enum — I verified this** |
| **VA — BCA, BNI, BRI, Mandiri, Permata** | ✅ CONFIRMED | `bca-va`, `bni-va`, `ecoll` (BNI eCollection), `briva`, `mandiri-echannel`, `permata-va` |
| VA — CIMB | ❌ NOT FOUND as VA | only `cimb-clicks` (internet banking) |
| **Bank transfer (manual)** | ✅ CONFIRMED | `bca-manual` + `TRANSFER_BANK:30` + `IN_PAYMENT_VERIFICATION` state |
| **Internet banking** | ✅ CONFIRMED | `bca-klikpay`, `cimb-clicks`, `danamon-online`, `bri-epay`, `mandiri-clickpay` |
| **GoPay · OVO · DANA · ShopeePay** | ✅ CONFIRMED | all four in the enum; GoPay also has a `/assets/images/GoPay.png` icon component |
| **LinkAja** | ⚠️ CONFIRMED on ONE surface only | english-academy.id e-wallet list. **Absent from the `re-payment` enum — drift** |
| **Alfamart / Alfamidi / Alfa Express / DanDan / Lawson · Indomaret · Pos Indonesia** | ✅ CONFIRMED | `alfa`, `alfa-mt`, `indomaret`, `pos-indonesia`, `pay-at-store-ba`, `payatall-cash`; *"Melalui mesin 1-kios Indomaret"* / *"Melalui kasir Indomaret"* UI |
| **Cards — Visa, MC, AmEx, UCB** | ✅ CONFIRMED | `credit-card`, `ccpp-cc`; *"Kartu Kredit (Full Payment): MasterCard, Visa, American Express, UCB"* |
| Cards — JCB | ❌ NOT FOUND | absent from every list |
| **Credit-card instalments (cicilan)** | ✅ CONFIRMED | `CREDIT_CARD_INSTALLMENT`; *"Danamon, BNI, Mandiri, BRI, OCBC, BCA, DigiBank by DBS"*; **0% 3/6/12-month, min Rp500,000**, Indonesia-issued Visa/MC |
| **BNPL — Kredivo, Akulaku** | ✅ CONFIRMED | `kredivo`, `akulaku`, `CARDLESS_INSTALLMENTS:32` |
| BNPL — Indodana / Atome / Home Credit | ❌ NOT FOUND | zero occurrences |
| **Bank direct debit** | ❌ **NOT FOUND** | **no bank direct-debit channel in the enum** |
| **Recurring / autodebit** | ⚠️ **CONFIRMED — CARD-ONLY** | see The Hook |
| **Voucher / marketplace code** | ✅ CONFIRMED | `voucher` is a first-class enum member |

**Read: one-off method coverage in Indonesia is genuinely excellent. The gap is not methods — it is recurring rails.**

## Section 5: Financials & company health

**Sourced (Katadata, fetched):** Revenue FY2020 **US$63.25M** → FY2021 **US$102.69M** (+62%). FY2020 loss **US$1.2M** → FY2021 **first profit, US$3.7M.** Cash at Dec 2021: **US$129M.** Markets: Indonesia, Vietnam (KienGuru), Thailand (StartDee). 31.1M cumulative downloads.

**Funding:** total **US$205M** across 7 rounds, 11 investors. Series C **Dec 2019: US$150M** led by **General Atlantic + GGV Capital**, with EV Growth and UOB Venture Management (Rp1.4tn). **April 2021: US$55M led by Tiger Global** with GGV (Rp801bn, earmarked for Skill Academy and "Robo AI"). Valuation **US$500M** at Series C.

⚠️ **NO funding round after April 2021 could be found. Five years without a raise.** GSV was named in the original brief; **it was not surfaced in any source and cannot be confirmed.**

**Layoffs — sourced, but 2022 only:** **18 November 2022**, hundreds laid off; the company stated it was below 50% of headcount, citing global market conditions; full severance, insurance extension, redeployment support. **CEO Belva Devara issued a public apology.** `[UNVERIFIED — search summary only]`

⚠️ **NO reports of layoffs in 2023, 2024, 2025 or 2026** — searched directly, twice in Indonesian. Absence of evidence, not evidence of absence.

**Current state — WEAK, aggregator-only:** headcount **4,231 as of 31 March 2026** (Tracxn) and ~4.4K (Growjo) `[UNVERIFIED — aggregator estimates]`. **If roughly right, the company has re-grown well past its 2022 cut, not contracted.**

⚠️ **🛑 Revenue estimates circulating are noise: US$448.2M (Kona Equity), US$845.9M, "US$500M–1B" (Growjo). These are algorithmic guesses implying 4–8× growth over the sourced 2021 figure with no funding round and no press. DO NOT put any of these in an email.**

**The single best current-health signal is the SimilarWeb +32.9% MoM traffic growth, and it is positive. No down-round, no new raise, no shutdown, no distress reporting found.**

## Section 6: Payment complaints — THIN. This is a gap, stated plainly.

**What exists:** an academic sentiment analysis of the Ruangguru Play Store app, **JATI Vol. 10 No. 1, February 2026** (PDF fetched, text extracted): **10,000 reviews scraped**, 9,700 after cleaning; VADER labelling **6,726 positive / 2,214 neutral / 760 negative → negative share ≈ 7.8%**; Naive Bayes best accuracy 83.52%. ⚠️ **No date range, no topic breakdown, and NO payment-related topic surfaced.** The paper is methods-focused and says nothing about payments specifically.

Related papers that **do** topic modelling exist but the Telkom University repository returned **HTTP 403** and was not retried.

**Indirect evidence that payment failures occur at institutionalised volume:**
- The T&C carries a **named refund ground for "system errors causing payment transaction failures"**, with a 14-day claim window and 20-working-day settlement. **Companies do not write bespoke clauses for problems they don't have** `[INFERENCE on the volume implication]`.
- A **dedicated WhatsApp line for payment issues: +6281574410000** (T&C, fetched). **A human WhatsApp escalation path for payments is a manual-reconciliation smell.**
- Help article: *"If the previous package payment hasn't gone through, you can just re-order and ignore the previous order"* — **the documented remedy for a stuck payment is "try again and abandon the orphaned order."** An orphan-VA problem with official instructions attached.
- A help article on how to check whether a subscription actually activated — implies activation-after-payment is routine confusion.

**What was searched for and NOT found:** no specific dated Play/App Store reviews about failed payments; **no auto-renewal disputes** (structurally consistent — there is no auto-renewal to dispute); no Reddit r/indonesia payment threads; no Twitter/X clusters. The only social controversy surfaced was the **March 2021 intern/outsourced-worker wage row** — irrelevant to payments, but worth knowing it exists before writing anything about their employer brand.

**🛑 Recommendation: do NOT write a payments-complaint-led email. The evidence base is too thin to cite specifics.** The highest-yield remaining action is a direct scrape of Play Store 1–2 star reviews filtered on Indonesian payment keywords (`bayar`, `pembayaran`, `transfer`, `VA`, `kode`, `promo`, `gagal`, `belum aktif`) — that needs a scraper, not WebSearch.

## Section 7: Buying Signals

**🔑 AIRIS — the AI tutor, and it has a paid tier. This is the best trigger.** `ruangguru.com/airis` — *"Tutor AI Smart dan Interaktif Pertama di Indonesia."* Two modes: **Basic (free) and Stellar (paid** — faster/more accurate responses, exclusive content). Launched in limited free beta ~Feb–Mar 2024. `[UNVERIFIED — search summary only]`

**Why it is the best trigger:** a new AI tier at a low monthly price point is a **fundamentally different payments problem** from a Rp1.45m annual package — small-ticket, high-frequency, recurring, **and the one place where Ruangguru would be most tempted to fall back on store billing.** If they haven't solved small-ticket recurring on domestic rails, that is the conversation.

**Price points (⚠️ mostly 2020–2021 vintage — VERIFY before quoting):** ruangbelajar 2-year Kelas 10-11-12 list **Rp1,450,000**, **Rp725,000** with code JADIJUARA (50% off) · ruangbelajar annual *"tak sampai Rp1 juta"* · English Academy **Rp1,500,000/3mo**, **Rp5,000,000/yr** (2021 launch pricing) · Skill Academy courses **Rp50,000–Rp1,000,000** (2020 Prakerja era) · Brain Academy Center facility fee **Rp5,000,000** (SOURCED from T&C). **Heavy codified always-on discounting — 50%, and a 52%-off FESTIVALRG new-school-year promo — means effective ticket is roughly half list.**

**Co-branded payment promo microsites — this is the orchestration wedge:** `ruangguru.com/promo/mandiri` (Mandiri credit card), `ruangguru.com/cicilan/mandiri` and `/cicilan/bni` (bank instalments), `ruangguru.com/promo/linkaja` (LinkAja). **Bank-specific and wallet-specific promo pages mean they are already negotiating and maintaining multiple separate acquirer and wallet relationships by hand.**

⚠️ **Government / B2B — a genuine weakener, size unknown.** Ruangguru works with Kemendikbud and Kominfo on national education digitisation, and has historic Kartu Prakerja participation. **Prakerja and government programme revenue is invoiced/government-disbursed, not card-paid — it does not count toward the volume gate. It could not be sized as a share of revenue. This is the main unquantified drag on the account.** (The 2025-framed source is Kompasiana, which is **user-generated — low credibility, pointer only.**)

**Marketplace leakage — confirmed, and architecturally contained.** Tokopedia runs an **Official Store Ruangguru** selling Skill Academy e-vouchers, plus a dedicated co-marketing page `ruangguru.com/promo/tokopedia`. Mechanism: buyer pays **Tokopedia**, gets a voucher code, redeems at `bayar.ruangguru.com` → "Redeem Voucher". **Cross-validated by the bundle: `voucher` is a first-class member of the 41-channel enum.** Sister brand **Schoters** also sells via Tokopedia. **Shopee and Blibli: NOT FOUND.**
**Read: voucher-redeemed GMV is NOT addressable payment volume — Tokopedia collected it. Discount it when sizing.**

**Leadership:** **Belva Devara** still referenced as CEO; co-founder **Iman Usman** holds the 0.01% direct stake. **No 2025–2026 leadership change found.**

**Engineering job postings naming payment systems: NOT FOUND.** ⚠️ Not successfully searched — the careers page was not checked. **A "Payments Engineer" or "Billing Platform" req would be the cleanest possible trigger and is worth a direct pass.**

## Section 8: PCI DSS

**NOT FOUND.** No PCI DSS attestation, no ISO 27001 claim, no trust/security page. **No Bank Indonesia PJP licence found, and none expected — they are a merchant.**

Relevant: **there is no card-capture form in the client bundles** — no PAN/CVV field, no card-tokenisation SDK. Card entry is almost certainly delegated to the gateway (`ccpp-cc` / `credit-card` redirect), keeping them out of PCI scope, consistent with `redirection` appearing as a bundle variant. `[INFERENCE, not confirmed]`

The auto-debit T&C (`ruangguru.com/syarat-ketentuan/pembayaran-cicilan-auto-debit`) confirms automatic debiting — *"pendebitan secara otomatis oleh Penyedia Metode Pembayaran berdasarkan tanggal jatuh tempo"* — and **names no provider, network or bank.** Generic *"Penyedia Metode Pembayaran"*, i.e. **deliberately PSP-abstracted.** That is itself evidence of the in-house abstraction.

## Section 9: ICP Score — 17 / 29 → ⭐ High

| Signal | Max | Score | Evidence |
|---|---|---|---|
| Transaction volume | 5 | **3** | **~75k–150k/month DERIVED**, floor ~49k. Scored 3 not 5 because **the last hard revenue figure is FY2021 — five years stale and from the COVID peak** |
| Orchestration posture | 4 | **1** | **In-house** — 41-channel enum, own taxonomy, own API gateway, spanning 6 brands and 3 countries. Verified first-hand |
| Operates 3+ countries | 3 | **3** | ID + **Vietnam** (Kien Guru brand enum, `momo`/`payoo`/`viettel-post`/`onepay-*` rails) + **Thailand** (Startdee brand, Thai-script i18n) |
| Multiple PSPs in parallel | 3 | **3** | **Two gateway families live simultaneously** (`ccpp-*` four sub-channels, `vt`) **plus direct bank products** (`ecoll`, `briva`, `bca-manual`) |
| Local rail gap in a top market | 3 | **3** | **No e-wallet autodebit, no bank direct debit — card is the ONLY automatic renewal rail, in a market with low single-digit card penetration.** Plus verified QRIS and LinkAja drift between their own two checkouts |
| Recent market expansion | 2 | **2** | **AIRIS AI launch with a paid Stellar tier**; product line materially wider than the stub assumed |
| Known payment issues | 2 | **2** | T&C refund ground for *"system errors causing payment transaction failures"* · **dedicated WhatsApp line for payment issues** · documented remedy *"re-order and ignore the previous order"* · `IN_PAYMENT_VERIFICATION` as a first-class state |
| Recent funding | 2 | **0** | ⬜ **No round since April 2021.** Do not pitch a funding trigger |
| Traffic outside home market | 2 | **0** | ⬜ **Deliberate zero.** 98.80% Indonesia — the most concentrated account in the batch. Cross-border is explicitly off |
| Competitor on orchestration | 2 | **0** | ⬜ Not researched — no Indonesian edtech peer evidenced on an orchestrator |
| Payment job postings | 1 | **0** | ⬜ **Not found** — and the careers page was not successfully checked |
| **TOTAL** | **29** | **17** | ⭐ **High** |

**Four deliberate zeros and a deliberately reduced volume score.** 17 reflects a genuine multi-PSP in-house layer across three countries with a sharp, specific recurring-rail gap — the consolidation pitch Yuno exists for — discounted for stale financials and a concentrated single market.

## Section 10: Do NOT Say

- ❌ **"Ruangguru uses Midtrans and 2C2P."** `ccpp*` → 2C2P and `vt` → Veritrans/Midtrans are **inferences from channel-code conventions, not facts.** No PSP name appears in any client code. Use: *"your checkout enumerates two separate gateway families plus direct bank VA products under your own channel taxonomy."*
- ❌ **Any aggregator revenue estimate** (US$448M, US$845.9M, "US$500M–1B"). Algorithmic noise.
- ❌ **40M users, 31.1M downloads or 22M users as a payer count.** All are registered/download volume.
- ❌ **Cross-border approval rates or corridor framing.** 98.80% Indonesia.
- ❌ **Any payments-complaint specifics.** The evidence base is too thin.
- ❌ **Midtrans Snap** from the `Snap` hits — all 22 were Tamagui `snapPoints` and XState `getSnapshot()`.
- ❌ **DOKU** — every `doku` hit was *"dokumen"* or *"Gondokusuman"*.
- ❌ **Stripe** — the hit was Bootstrap `progress-bar-stripes`.
- ❌ **Current pricing** without re-checking. Most price points are 2020–2021 vintage and `bayar.ruangguru.com` pricing was never read.
- ❌ **GSV as an investor** — not corroborated.
- ❌ **Voucher/Tokopedia GMV as addressable volume.** Tokopedia collected it.
- ❌ **Government/Prakerja revenue as card-paid.** It is invoiced.
- ❌ Any claim that they do **cost- or success-rate-based routing.** The architecture is in-house; the sophistication is unverified.
- ❌ **That the app-store trap applies.** It was checked and cleared — but **resolve the AIRIS Stellar question first.**

## Section 11: Research Confidence

**Overall: HIGH on architecture and rails. MEDIUM-LOW on financials. THIN on complaints.**

- ✅ **Verified first-hand by me:** the `re-payment` bundle (HTTP 200, 2,084,354 bytes) and independent confirmation of 18 of the 41 channel codes within it, including `momo`, `payoo`, `viettel-post`, `apple-iap`, `ccpp-cc` and `vt` — **and `qris` = 0, confirming the Skill Academy catalogue drift.**
- ✅ **Fetched by the research pass:** `ruangguru.com/llm-info`, the Android payment-flow help article, the T&C (`/terms-conditions/apps`), the Katadata profit article, the JATI journal PDF, plus `skillacademy.com`, `english-academy.id`, `bimbel.ruangguru.com` and both `bayar.*` apps.
- ✅ **Rigorous false-positive control** with ±60–200 chars of context on every hit; six distinct false positives caught and discarded.
- ⚠️ **Blocked:** the Telkom University repository (403, both the PDF and `/bab1/` variants) · `repository.upnjatim.ac.id/11912/` · Pitchbook and Dealroom (paywalled) · the Play Store listing itself was **never fetched**, so the "In-app purchases" label and any Play-billing review mentions are **unchecked** — the IAP verdict rests on Ruangguru's own iOS help page plus the absence of Play Billing code, which is solid but one source short.
- ⚠️ **The live checkout was never exercised** — no package was added to a cart, so the **actually rendered, currently enabled** Indonesian method list was never seen. The enum is the full **capability** set; some codes are Vietnam-only and some Indonesian ones may be dormant. Telling detail: `payment-web`'s Indomaret instruction panel still contains **`"Lorem ipsum dolor sit amet"` placeholder copy in production** — not every path is live or polished.
- ⚠️ **Unresolved:** any paying-subscriber count · any revenue figure after FY2021 · **whether AIRIS Stellar bills via store IAP (highest-value open question)** · current pricing · Kien Guru / StartDee current operating status · government/Prakerja share of revenue · marketplace share of Skill Academy sales · any layoff/raise/distress event 2023–2026 · the current PSPs by name · payment-related job postings · **`payment.sirogu.com`**, an unexplained third-party-looking staging domain that was not investigated.

</details>
