# Lion Air Group

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 19 / 29 → ⭐ **High Priority**
**Industry:** Airlines (LCC group — Lion Air, Batik Air, Wings Air, Batik Air Malaysia, Thai Lion Air) · **HQ:** Jakarta, **Indonesia** — PT Lion Mentari Airlines, **privately held by the Kirana family** · **Researched:** 2026-09-19 · **First email sent:** —
**Motion:** **Greenfield** — no group-level orchestration detected. ⚠️ Partly affirmative (four stacks across four countries), partly absent-hits, and **weakened by a Cloudflare block on the real checkout.** Pitch as a hypothesis to test, not established fact.

---

> ## 🎯 THE HOOK — their own front-end ships a payment-failure taxonomy
>
> **✅ Verified by me directly** in the live `bookcabin.com` bundle — BookCabin is the group's own booking app, launched May 2024. Every one of these keys is present:
>
> | Key | What it implies |
> |---|---|
> | **`MaxPaymentMethodChanges`** | a counter capping how many times a customer may switch method |
> | **`paymentMaxFailuresReached`** | a hard lock after repeated failures |
> | `PaymentAlreadyInitiated` · `PaymentTimeOut` · `paymentFailed` | a full decline/timeout state machine |
> | `pendingPayment` · `WaitingForPayment` | async settlement states |
>
> Alongside them, their own customer-facing copy: *"Jika Anda sudah melakukan pembayaran, **mohon jangan mencoba lagi**"* — *"if you have already paid, please do not try again"* — and **"E-tiket akan dikirim dalam 2 jam"**, a two-hour asynchronous issuance window.
>
> 📌 **Nobody builds a max-payment-method-changes counter, a max-failures lock, a don't-double-pay warning and a two-hour issuance gap unless declines, retries and payment/issuance desync are routine.** This is the cleanest evidence-backed pain signal in the repo, and it comes from their own published front-end — **so it can be raised as an observation without accusing anyone of anything.**
>
> ### And the second hook: a nationwide agent deposit network on what looks like one bank rail
> **✅ Both agent portals verified live by me — HTTP 200:** `agent.lionair.co.id/LionAirAgentsPortal/` (Indonesia) and `b2b.lionairthai.com/LionAirThaiAgentsPortal/` (Thailand). Both **ASP.NET**, near-identical path naming — **one in-house B2B platform, deployed separately per country.**
>
> From the Indonesian portal's own bulletin board: *"Layanan **top-up agen** sekarang tersedia untuk **Virtual Account (VA) BNI**"* · *"Jumlah refund secara otomatis akan dikreditkan kembali ke **saldo agen**"* · agent **PIN** introduced 1 Feb 2024.
>
> **A closed-loop prepaid B2B wallet — top-up, balance, PIN, auto-refund-to-balance — built in-house, funded through what appears to be a single bank rail.** That is a concentration risk and a live payout/orchestration use case.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Indonesia's largest airline group by domestic share, spanning five carriers across three countries plus its own OTA-style app. **Privately held, files nothing public** — say "privately held and opaque" on any call, because it is accurate and they know it.

**SimilarWeb total visits:** **Not obtained.** No data supplied. Country profile unverified; **no split invented.**

### ❌ THE STUB'S ~$2B REVENUE IS REFUTED AS UNSOURCED
**No filing, audited account or company statement supporting it exists anywhere reachable.** It also contradicts what little exists: a data-vendor estimate puts PT Lion Air at **$250M–$500M** (4–8× *below* the stub), and founder Rusdi Kirana publicly discussed a **Rp 7 trillion (~US$430M) valuation** — **a valuation, not revenue, and the two are being conflated in circulating summaries.** `[Both UNVERIFIED — search summary]` **Recommend the target list be corrected to "no public revenue figure; privately held."**

### Accepted methods — official group policy, from their own newsroom
Lion Group went **cashless (non-tunai) for all ticket sales from July 2024**. Two newsroom articles give an identical closed list:

**Kartu Debit · Kartu Kredit · QRIS · Payment Code · Payment Link · Travel Voucher · Transfer antarbank**

⚠️ **Bank transfer is restricted to group bookings of 10+ passengers**, verbatim: *"Pembelian tiket secara perseorangan **tidak dapat dilakukan** melalui transfer antarbank."*
**Payment Code** is payable at ATM and at **Indomaret and Alfamart**, both named explicitly.

**BookCabin's own components confirm the consumer set:** `QrisPayment`, **`QrisBniPromo`**, `virtualAccount`, **`BNIDebitCard`**, `PaymentCode`. QRIS renders **in-page** (*"Pindai QRIS yang ditampilkan di halaman BookCabin"*) — merchant-presented dynamic QR, not a redirect.

### ❌ Sourced absence — verified by me in the live bundle
**GoPay · OVO · DANA · LinkAja · ShopeePay · Kredivo · Akulaku · internet banking · Direct Debit**
I grepped the live 601KB bundle myself: **zero occurrences of GoPay, OVO, ShopeePay, LinkAja, Kredivo and Akulaku.** They are also absent from both official method lists.

> 🚩 **TWO FALSE POSITIVES CAUGHT, AND BOTH WERE ALREADY ON OUR RUNNING LIST — independent corroboration:**
> - **`DANA` → `pengembalian dana`** ("refund"). I checked every occurrence myself: all are *"Pengembalian Dana"* or *"dana kamu aman"*. **DANA the e-wallet is NOT evidenced.**
> - **`DOKU` → `dokumen`.** DOKU the PSP is **NOT** evidenced.

> ⚠️ **Read the wallet gap fairly.** QRIS is interoperable — GoPay, OVO, DANA, ShopeePay and LinkAja can all scan it, so one integration nominally covers them. **That is a legitimate architecture, not an oversight.** What it costs them: no in-app wallet balance or token flows, no wallet-specific promo mechanics, **no BNPL at all for a price-sensitive LCC base**, and total dependence on a single QRIS acquirer. **Frame it that way — as an observation from their published method list, never as a claim about their backend.**

### Known PSPs
| Finding | Status |
|---|---|
| **GoQuo** (Kuala Lumpur, acquired by TWAI 2022) — airline IBE / e-commerce layer | ✅ **CONFIRMED** via Android packages **`com.goquo.jt.app`** (Lion Air) and **`com.goquo.ig.app`** (Batik Air), independently corroborated by the 2019 Malindo breach publicly attributed to ex-GoQuo staff |
| **GoQuo Pay** — GoQuo's own payment-switching product | ⚠️ **NOT CONFIRMED for Lion Air.** "GoQuo is the booking layer" is established; "GoQuo Pay is the payment layer" is a hypothesis |
| **2C2P** → Thai Lion Air · **YeePay + FPX** → Batik Air Malaysia | ⚠️ `[UNVERIFIED — search summary only]` |
| **Yellow.ai** (CS automation) | ✅ Confirmed live — homepage loads `cdn.yellowmessenger.com` and `r2.cloud.yellow.ai` |
| **Indonesian consumer acquirer** | ❌ **NOT ESTABLISHED — the single biggest unknown** |

❌ **Sourced-absent from every surface reached** (41-page T&C, both newsroom articles, homepage, agent portal, BookCabin bundle): Midtrans, Xendit, DOKU, Faspay, iPay88, Espay, Finnet, NICEPAY, Winpay, Duitku, OY!, Adyen, Worldpay, Cybersource, Stripe, Checkout.com, Amadeus, Accelya, CellPoint Digital, **Navitaire (checked hard — no hit)**.

> ⚠️ **DO NOT QUOTE A CSP FOR THIS ACCOUNT.** `secure2.lionair.co.id`, `batikair.com.my` and `lionairthai.com` all return a **Cloudflare 403 bot challenge**, and the CSP observed there is **Cloudflare's challenge-page CSP, not the application's.** The Wayback snapshot of the booking host is an **11-byte stub.** **The real payment page and its JS were never seen — any PSP behind that challenge is invisible to this pass.**

**🏦 BNI appears three times across independent surfaces** — agent top-up VA, `QrisBniPromo`, `BNIDebitCard`. **Hypothesis only: BNI may be the principal collecting bank. No page states it.**

### 🧩 The group runs at least FOUR payment stacks
| Carrier / property | Stack evidence |
|---|---|
| **Lion Air (JT)** — `lionair.co.id`, booking on `secure2.` | IIS/ASP.NET; app `com.goquo.jt.app` |
| **Batik Air (ID)** | app `com.goquo.ig.app`; ⚠️ **no independent domain resolves** — `batikair.co.id`, `id.batikair.com` all fail |
| **Batik Air Malaysia (OD)** — `batikair.com` → `batikair.com.my` | **separate** — card + FPX, YeePay MoU |
| **Thai Lion Air (SL)** — `lionairthai.com` | **separate** — app `com.thailionair.app`, *not* a GoQuo package; 2C2P reported |
| **BookCabin** — `bookcabin.com` | **its own stack** — Next.js/Cloudflare, package `com.kabinkitatop.bookcabin` |
| Wings Air (IW) | ❌ nothing found at all |
| Super Air Jet | ⚠️ **legally separate — do NOT fold into group figures** |

### Buying signals
- 🔴 **A payment-failure taxonomy in their own live code** — verified
- 🔴 **Agent deposit top-up on a single bank rail**, in-house ASP.NET, PIN added Feb 2024
- 🧩 **Four stacks, four countries, one group** — exactly the shape orchestration consolidates
- 🛒 **BookCabin (May 2024)** — the group built its own OTA against its own inventory: a second checkout, second method set, second failure surface
- ❌ **No BNPL** for a price-sensitive LCC base
- ⛔ **No IPO pressure** — Kirana called the Rp 7T figure *"kekecilan"* and deprioritised listing. **Do not build a pitch on IPO readiness.**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Lion Air Group` to draft the 12-touch sequence.*

**Six instructions for whoever drafts it:**
1. **Open on the agent deposit network.** It is confirmed, not inferred, and it is the most commercially interesting thing here — a nationwide prepaid agent wallet funded through what appears to be one bank rail.
2. **The failure taxonomy is the second observation.** Reference the *behaviour their own front-end describes*, never an accusation. *"Your booking app has a max-payment-method-changes counter"* is a fact; *"your payments fail a lot"* is a jab.
3. **State the wallet gap as an observation from their published method list**, and **acknowledge the QRIS argument yourself** — it makes us look like we understand the market rather than like we are counting missing logos.
4. ⛔ **Never use the $2B revenue figure.** Nothing supports it.
5. ⛔ **Never build on an IPO angle.** The founder explicitly deprioritised it.
6. ⛔ **Never quote a CSP or name an Indonesian PSP.** The checkout was never seen.

**Never claim:** any Indonesian acquirer, that BNI is the acquiring bank (hypothesis), that they use DANA or DOKU (both false positives), a BCA virtual-account code (unverified), or any transaction count — **see the volume warning in Section 3.**

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 19 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ⚠️ **Awarded on scale, but this is the softest volume call in the repo alongside Fever — read the warning.** No filings exist. Lion Air alone reportedly carried **18.28M passengers (2023)** at 27.7% domestic share, with the group near 65% of Indonesia's 65.95M domestic passengers `[UNVERIFIED — search summary]`. **The gate cannot fire — no sourced sub-40k figure exists.** **But three deflators make the addressable count far below the passenger count, and I cannot quantify any of them:** (a) multi-passenger bookings, routine on LCC domestic; (b) **the agent channel, where ticket issuance is a *balance decrement*, not a payment event** — the addressable event is the lower-frequency, higher-value **top-up**; (c) the OTA channel, where Traveloka/tiket.com process the payment themselves — **confirmed in practice by a complaint where Lion Air's own refund team said refunds must route back through the OTA because the airline never touched the card.** ⛔ **No transaction number may go in an email.** |
| Orchestration status | **+4** | ✅ **None detected at group level.** ⚠️ **Basis stated plainly: partial affirmative + absent hits, weakened by the checkout block.** Affirmative: four stacks across four countries, an in-house ASP.NET B2B platform deployed per country, GoQuo IBE package names, BookCabin as a fourth independent checkout. **A group running one orchestrator would not look like this.** Negative-only: zero hits for Juspay, Spreedly, Primer, Gr4vy, APEXX, Payrails, IXOPAY, Yuno **and CellPoint Digital** — the airline specialist that would normally be here. |
| 3+ countries | **+3** | ✅ Indonesia, Thailand, Malaysia, plus Singapore operations (moved to Changi T4, 11 Nov 2025). |
| Multiple PSPs | **+2** | ✅ **Structurally proven by the per-country split** — separate apps, separate domains, separate method sets (QRIS/VA in ID, 2C2P in TH, FPX/YeePay in MY). ⚠️ **Only GoQuo can be named**, and GoQuo is the IBE, not necessarily the acquirer. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Sourced absence, verified by me in the live bundle.** Indonesia is the #1 market and **GoPay, OVO, DANA, LinkAja, ShopeePay, Kredivo and Akulaku all return zero occurrences**, and are absent from both official method lists. ⚠️ **Score it, but pitch it with the QRIS nuance** — see Section 1. |
| Recent expansion | **0** | ⬜ Not awarded. The Changi T4 move and the Nataru fleet allocation are operational; BookCabin launched May 2024, which is a new channel but not a market entry. No verified 2025–26 expansion. |
| Payment issues reported | **+2** | ✅ **The best-evidenced payment-issues row in the repo, and it is machine-readable.** `MaxPaymentMethodChanges`, `paymentMaxFailuresReached`, `PaymentAlreadyInitiated`, `PaymentTimeOut`, a don't-double-pay warning and a two-hour async issuance window — **all verified by me in the live front-end.** Supported by dated complaints: a May 2026 unresolved refund, and a Sept 2025 case where **Lion Air stated refunds cannot be returned to the card by the airline and must route via the OTA** — a routing-architecture limitation, not a policy preference. |
| Funding >$10M | **0** | ❌ Privately held. No round, and the IPO is explicitly deprioritised. |
| High traffic outside home | **0** | ⬜ No traffic data, and no channel-mix disclosure exists. |
| Competitor using orchestration | **0** | ❌ Not established. AirAsia — the closest regional LCC peer — was not checked. Cebu Pacific runs CellPoint but is a different home market with limited overlap. |
| Payment job postings | **0** | ⬜ Not found. |

**Tier: 19 / 29 → ⭐ High Priority.** No override applied.

### Source Notes
- ✅ **Verified by me in the live `bookcabin.com` bundle (601KB):** the complete failure taxonomy, the payment components (`QrisPayment`, `QrisBniPromo`, `virtualAccount`, `BNIDebitCard`, `PaymentCode`), **zero occurrences of six named wallets/BNPL providers**, and that every `dana` hit is `pengembalian dana`.
- ✅ **Both agent portals verified live by me at HTTP 200** — Indonesia and Thailand, separately deployed.
- ✅ **The cashless policy and its closed method list** come from two of Lion Air's own newsroom articles (22 Aug and 25/27 Sep 2024), including the individual-bank-transfer exclusion and the Indomaret/Alfamart naming.
- ✅ **GoQuo** is confirmed by Play Store package names plus independent breach attribution.
- ⚠️ **2C2P, YeePay, FPX, the fleet count, market shares and passenger figures are all `[UNVERIFIED — search summary only]`.**
- ⚠️ **A BCA virtual-account company code (`20191`) surfaced in a search summary. It was NOT confirmed. Do not cite it.**
- ❌ **`secure2.lionair.co.id`, `batikair.com.my`, `lionairthai.com` all Cloudflare-403.** The Wayback snapshot of the booking host is an **11-byte stub**. **The payment page and its CSP were never observed.**
- ❌ **The 31-page agent portal user guide is a scanned PDF with no text layer** — would need OCR, and likely documents the top-up flow in detail.
- ❌ **Bank Indonesia licence registry was never queried** — an *unchecked* absence. ⚠️ **Worth ten minutes: the agent deposit wallet is a closed-loop prepaid balance, which in Indonesia can raise e-money licensing questions.** If it checks out it is a sharp, credible opener.

### Manual Research Recommendations
> **1. Get behind the Cloudflare challenge on `secure2.lionair.co.id`** and name the Indonesian acquirer. Biggest unknown by far.
> **2. Query the BI licensee registry** for any Lion Group payment or e-money licence — see the note above.
> **3. OCR the agent portal user guide.** It probably documents the deposit top-up flow properly, and that flow is the lead hook.
> **4. Establish channel mix — direct vs agent vs OTA.** It gates every volume claim, and nothing may be said about transaction counts until someone has it.
> **5. Check Lion Parcel**, the group's logistics arm — a plausible second entry point whose stack was never examined.

---

## Executive Summary

Lion Air Group is Indonesia's largest airline group by domestic share — five carriers across three countries — and it is **privately held, files nothing public, and the target list's ~$2B revenue figure has nothing behind it** and should be corrected. What the research established instead is architecture. The group runs **at least four separate payment stacks**: QRIS and virtual accounts in Indonesia, 2C2P reported in Thailand, FPX and a YeePay arrangement in Malaysia, and **BookCabin**, its own OTA-style app launched in May 2024, on a stack of its own. Consumer method coverage has been deliberately narrowed since going cashless in July 2024 to **card, QRIS, payment code, payment link and voucher**, with bank transfer blocked for individuals — and **no direct e-wallet and no BNPL integration anywhere**, which I verified by grepping their live bundle rather than taking it on trust. The two strongest hooks are both confirmed rather than inferred. First, a **nationwide travel-agent deposit network** — top-up, balance, PIN, auto-refund-to-balance — built in-house on ASP.NET, deployed separately per country, and funded through what appears to be a **single bank rail**. Second, and more unusual: **their own front-end ships a payment-failure taxonomy**, including a counter for how many times a customer may change payment method and a hard lock after repeated failures, alongside a "please do not pay again" warning and a two-hour asynchronous ticket-issuance window. **Nobody builds those unless declines, retries and payment/issuance desync are routine** — and because it is their own published code, it can be raised as an observation rather than an accusation.

</details>
