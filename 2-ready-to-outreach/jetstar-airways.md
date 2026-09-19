# Jetstar Airways

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 18 / 29 → ⭐ **High Priority**
**Industry:** Airlines (low-cost carrier) · **HQ:** Melbourne, **Australia** — Jetstar Airways Pty Ltd, ABN 33 069 720 243, wholly owned by **Qantas Airways Ltd (ASX: QAN)** · **Researched:** 2026-09-19 · **First email sent:** —
**Motion:** **In-house (partial)** — a purpose-built payment service on top of Navitaire. Affirmative from certificate transparency, not absence. **Respect the build.**

---

> ## 🏢 THE CORPORATE SHAPE — "Jetstar" in 2026 is TWO airlines, not four
>
> **✅ From the Qantas Annual Report 2026 (year ended 30 June 2026), the primary filing:**
>
> | Entity | Status | Storefront |
> |---|---|---|
> | **Jetstar Airways (JQ)** — AU/NZ | **Operating. This is the account.** | `jetstar.com`, all POS |
> | **Jetstar Asia (3K)** — Singapore | 🔴 **CLOSED — ceased operations 31 July 2025** | gone |
> | **Jetstar Japan (GK)** | Operating, **but Qantas is exiting and the brand is being dropped** | `jetstar.com/jp` (shared) |
> | Jetstar Pacific (Vietnam) | 🔴 Gone since 2020 — rebranded Pacific Airlines, Qantas sold out | not a Jetstar storefront |
>
> Verbatim: *"Jetstar Asia ceased operations on 31 July 2025, recording an Underlying EBIT loss of $31 million… and $48 million of strategic restructure costs."* The impairment note now lists exactly **two** Jetstar CGUs — Australia/NZ and Japan.
>
> ⚠️ **But do not call Singapore dead.** The `/sg` and `/kr` footers still carry **Jetstar Regional Services Pte Ltd, BRN 201229688K**, the SG storefront still sells in SGD with its own fee schedule, and JQ still flies Singapore. **The airline is gone; the merchant is not.**
>
> 📌 **And the site still publishes Jetstar Asia fees 14 months after the airline shut** — *"Jetstar Asia (3K): SGD $50 / VND 900,000₫ / LKR Rs. 11,445"*. Stale content in a live fee table.

---

> ## 🎯 THE HOOK — a dated, sourced trigger, from Qantas's own filing
>
> **Qantas Annual Report 2026, Note 34(C) Guarantees, verbatim:**
> > *"As part of the business service agreements, the Qantas Group has extended support to **Jetstar Japan by allowing its credit card transactions to be acquired through the Qantas Group's contractual arrangements**."*
>
> **And in the same report:** *"Qantas has also signed a binding agreement with Japan Airlines to facilitate the change in Jetstar Japan's shareholder structure through a share buy-back transaction."*
>
> 📌 **Qantas is exiting Jetstar Japan — and Jetstar Japan's card acquiring runs on Qantas Group paper.** Someone has to unpick a shared merchant acquiring relationship across a JV boundary, on a deadline, with a rebrand away from "Jetstar" reportedly due to be announced October 2026. **That is a real, dated, first-party trigger — not a manufactured one.**
>
> ### And the second observation: they charge MORE for local rails than for cards
> In **Japan** — the only market where Jetstar runs local rails — the fee schedule is two-tier:
> - Cards / Apple Pay / Google Pay / PayPal / UnionPay: **¥690 domestic · ¥850 short-haul · ¥1,000 long-haul**
> - **au PAY / carrier billing / Wellnet (konbini, Pay-easy):** **¥740 · ¥900 · ¥1,200**
>
> **They charge ¥50–¥200 MORE to use the Japanese local rails than to use a card** — the inverse of the usual APM cost curve, and **a priced admission that local acceptance is currently expensive for them to run.** ⚠️ *Agent-sourced; I could not reach the JP page myself — see Source Notes.*

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Qantas's LCC. **FY26 (year ended 30 June 2026) Jetstar Group revenue A$6,022M (+5.4%), Underlying EBIT A$723M (−6%), seat factor a record 89.1%.** Australian domestic ran a **16% operating margin**.

**SimilarWeb total visits:** **Not obtained.** No data supplied. Country profile unverified; **no split invented.**

### ★ WELLNET AGAIN — this is now the fourth carrier
Jetstar Japan's payment-options page names **ウェルネット (Wellnet)** for convenience-store, bank ATM (Pay-easy), Japan Post Bank and net-banking payment. **That makes four carriers in this repo on Wellnet: ANA, JAL, Korean Air (listed as "Wellnet (Konbini)") and now Jetstar Japan** — consistent with Wellnet's own claim to serve *"all of Japan's major domestic airlines."* ⚠️ Note **Seven-Eleven is explicitly excluded** from Jetstar's Wellnet flow.

### 💳 The AU surcharge schedule — ✅ verified by me, with a dating problem
**I could not reach `jetstar.com` at all** — curl gets an HTTP/2 stream error then an empty reply, WebFetch gets 503. **I recovered the AU fee table from a Wayback snapshot dated 2025-12-27:**

| Method | Fee (**2025-12-27 snapshot**) |
|---|---|
| **PayID · Jetstar voucher · Gift Card · 100% Points Plus Pay** | **Fee free** |
| **Debit/Prepaid Visa + EFTPOS** | **0.27%** |
| Debit/Prepaid Mastercard | 0.48% |
| Debit/Prepaid Visa | 0.52% |
| PayPal (Pay Now and Pay in 4) | 0.69% |
| Credit/charge — Amex, UnionPay, JCB | 1.11% |
| Mastercard credit | 1.11% |
| Visa credit | 1.24% |
| **Alipay** | **1.5%** |
| Afterpay | 1.5% per booking |
| Zip | 1.6% per booking |
| UATP | 1.75% |
| Apple Pay / Google Pay | **pass-through of the underlying card rate** |

✅ **Verified by me:** *"Your Payment Fee is determined by the first flight on your itinerary"*, and **no fee cap appears anywhere** — I searched for "maximum", "capped" and "cap of" and found nothing.

> ⚠️ **THE RATES ARE DISPUTED AND MUST BE RE-CHECKED BEFORE USE.** The research agent read the **live** page and reported materially different numbers — Visa debit 0.36%, Visa credit 1.06%, Amex 1.06%, Afterpay 1.66%, Zip 1.77% — and reported **no Alipay anywhere on Jetstar**. My snapshot shows **Alipay at 1.5% on the Australian storefront** and a **Visa+EFTPOS row at 0.27%** the agent did not report at all.
> **The most likely explanation is that Jetstar re-priced between December 2025 and now** — which is itself interesting, since it means the schedule is actively managed. **But I cannot confirm which is current. ⛔ Do not put a specific percentage in an email without loading the live page in a browser.** The *structure* — roughly fifteen distinct per-method rates, no cap, fee set by the first flight — is safe; the numbers are not.

📌 **The `Visa + EFTPOS` row at 0.27% is the sharpest single line in the table.** They already route Visa debit over the domestic EFTPOS rail where they can and price it ~25bp below the same card on the scheme rail — **least-cost routing they are doing today.** And it is explicitly **"not available for Apple Pay transactions"** — so the cheapest rail they have is the one their wallet flow cannot reach.

### 🌏 Everything east of Bali is cards-only
The agent pulled `/help/payment-options` for **ID, TH, PH, MY, HK, TW, KR, LK, VN** individually. Accepted methods are Visa, Mastercard, Amex, UnionPay, JCB, UATP, Apple Pay, Google Pay and vouchers — **plus PayPal in TH and HK, and nothing else anywhere.** Malaysia canonical-redirects to the Singapore page; **Taiwan and mainland China are stubs with no method list at all.**

❌ **Sourced absence across all of Asia, checked page by page:** no QRIS, GoPay, OVO, DANA or ShopeePay · no PromptPay or TrueMoney · no GCash or Maya · no FPX, Touch 'n Go or Boost · no KakaoPay, Naver Pay, Toss or PAYCO · no LINE Pay · **no Alipay or WeChat Pay on CN/HK/TW** · no VNPay, MoMo or ZaloPay · no konbini outside Japan.

> 📌 **This is the account in one line.** Jetstar launched **Brisbane–Cebu, Melbourne–Colombo, Avalon–Denpasar, Maroochydore–Denpasar, Gold Coast–Denpasar and Newcastle–Denpasar in FY26** — and in every one of those markets the checkout offers international cards and nothing local.

### Known PSPs
| Finding | Status |
|---|---|
| **Navitaire New Skies / dotREZ** (PSS) | ✅ **CONFIRMED from certificate transparency** — `*.navitaire.jetstar.com`, `navitaire-partner-apis.jetstar.com` (+ staging), and a full **`dotrez-*.uat.jetstar.com` CI/CD ladder** (auto, base, ci, dev, devops, feature, hotfix, release, test, uat) with a cert issued **2025-07-08**. A branch-per-environment pipeline means they are **actively building against it**, not merely hosting it. **Same PSS as HK Express.** |
| **`jqpay.jetstar.com`** (+ `uat-jqpay`) | ✅ **Exists and resolves** — Jetstar's own payment service, prod and UAT. ⚠️ **Body unreachable (Akamai); the "payment abstraction layer" reading is inference from naming and topology.** |
| `jetcards.` · `financeadmin.` (+ UAT) · `merchandise.` | ✅ In-house voucher/gift-card and finance-admin services |
| **Wellnet** (JP cash rails) · au PAY · d払い · PayPal · UnionPay | ✅ Named on Jetstar's own Japanese page |
| **Card acquirer** | ❌ **NOT ESTABLISHED for JQ.** Only Jetstar *Japan*'s acquiring path is disclosed, and that is via Qantas Group. |

❌ **Adyen, Worldpay, Cybersource, Braintree, Stripe, Checkout.com, Global Payments, Fiserv, eWAY, Windcave, Tyro, Pin Payments, Accelya, CellPoint — NOT FOUND, but UNCHECKED-absence.** `booking.jetstar.com` serves an Akamai bot-challenge shell; its only CSP directive is `frame-ancestors`, so **no gateway hosts are recoverable**. The privacy policy names **zero** processors. ⛔ **Do not tell the prospect they don't use any of these.**

### 🆚 Qantas mainline vs Jetstar — related, but NOT the Cathay/HK Express situation
Group acquiring is shared **at least for Jetstar Japan**, and **PayPal and UATP price identically across both carriers** — implying group-level commercial agreements. **But card rates differ by 17–35bp on identical schemes, and Qantas caps its surcharge (A$22 domestic / A$120 international) while Jetstar discloses no cap at all.** Qantas also takes **BPAY**, which Jetstar does not; Jetstar takes **Afterpay** and **POLi** (NZ), which Qantas does not. **Treat as one group relationship with two merchant configurations, not two unrelated accounts.**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Jetstar Airways` to draft the 12-touch sequence.*

**Six instructions for whoever drafts it:**
1. **The Jetstar Japan acquiring unwind is the opener.** It is dated, first-party from Qantas's own annual report, and genuinely time-bound. Nothing else here is as clean.
2. **"Everything east of Bali is cards-only" is the second observation**, and it pairs with the six new FY26 leisure routes into exactly those markets.
3. **The Japan two-tier fee is the third** — they charge more for local rails than for cards. Frame it as an observation about acceptance economics, not a criticism.
4. ⛔ **Do NOT quote any surcharge percentage without a live browser check.** My snapshot and the agent's live read disagree materially.
5. ⛔ **Do NOT use the refunds class action as a payments signal.** It is about refund *policy* and the voucher/credit construct, it is **live unprovisioned litigation**, and conflating it with processing failure would be both wrong and tone-deaf. **The ACCC ground-handling penalty is a labour case — nothing to do with payments.**
6. ⛔ **Never say Jetstar Asia is "your Singapore business."** The airline closed 31 July 2025; the Singapore *merchant entity* still sells.

**Never claim:** any acquirer for JQ (none established), that Jetstar accepts no Alipay (my snapshot shows it on the AU page), Jetstar Group passenger counts (not disclosed), or that POLi/BPAY/PayTo/Klarna are on the AU storefront — **POLi is NZ-only and the other three are absent.**

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 18 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED as a bound** from the Qantas FY26 Annual Report: **Jetstar Group revenue A$6,022M**, ASKs 57,736M, seat factor **89.1%**. Even at an implausibly high **A$500 per booking**, that is ~12m bookings/year = **~1m/month**. **Every plausible divisor clears 100k.** ⚠️ **Jetstar Group passengers carried are NOT disclosed separately** — only Group-total (55,945k) and Jetstar seat factor/ASK. The "record 16 million domestic" figure is search-summary only. |
| Orchestration status | **+1** | ✅ **In-house (partial), on affirmative CT evidence** — a prod+UAT `jqpay` service, `jetcards`, `financeadmin`, Navitaire partner APIs and a dotREZ CI/CD ladder, plus per-POS surcharge config that differs *structurally* (percentage in AU/NZ, flat in SG, two-tier flat in JP). **No third-party orchestrator detected** — Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY, Yuno all absent — ⚠️ **but that half is absence-of-evidence, since the checkout was unreachable.** |
| 3+ countries | **+3** | ✅ ~14 storefronts, **16 currencies**, FX *"at an exchange rate agreed on with our payment partners"* (plural, unnamed). |
| Multiple PSPs | **+2** | ✅ **Structurally proven:** Wellnet handles Japanese cash rails, Jetstar Japan's **cards are acquired via Qantas Group arrangements** per the AR, and JQ's own acquirer is separate and undisclosed. ⚠️ Only **Wellnet** is nameable. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **Sourced absence, checked page by page across nine Asian storefronts.** Cards, UnionPay, JCB, UATP and wallets — and **not one local rail outside Japan**, in markets they are actively expanding into. |
| Recent expansion | **+2** | ✅ **Six new routes in FY26** from the primary filing — Brisbane–Cebu, Melbourne–Colombo, Avalon–Denpasar, Brisbane–Queenstown, Brisbane–Rarotonga, Maroochydore–Denpasar — plus 25 A321LRs now ~47% of narrowbody capacity, each delivering A$10M of EBITDA. |
| Payment issues reported | **0** | ⬜ **Not awarded, deliberately, and the reason matters.** The visible evidence is the **August 2024 refunds class action** — which alleges Jetstar *"was unjustly enriched by holding customer funds"* — but that is **refund policy and the voucher construct, not payment processing**, and it is live unprovisioned litigation. The only processing-failure material (a July 2024 duplicate-charge episode) traces to a low-quality aggregator quoting a review site. **Not usable.** |
| Funding >$10M | **0** | ❌ Wholly owned by an ASX-listed parent. |
| High traffic outside home | **0** | ⬜ No traffic data. |
| Competitor using orchestration | **+2** | ✅ **Cebu Pacific runs CellPoint Digital** (established in our own file), and **Jetstar launched Brisbane–Cebu in FY26** — a direct route overlap with a peer LCC already on an orchestration layer. Same basis on which this row was awarded for HK Express. |
| Payment job postings | **0** | ⬜ Not found — careers portals need a live browser session. Unchecked. |

**Tier: 18 / 29 → ⭐ High Priority.** No override applied.

### Source Notes
- ✅ **The AU fee table, the "first flight determines the fee" rule and the absence of any cap were verified by me** from Wayback snapshot `20251227064144`.
- 🚩 **`jetstar.com` is unreachable from this session by every method** — curl returns an HTTP/2 `INTERNAL_ERROR`, HTTP/1.1 returns an empty reply, and WebFetch returns 503. Wayback worked only on the second attempt after a connection reset. **All live-page findings below are the agent's, not mine.**
- ⚠️ **THE FEE RATES ARE DISPUTED.** See the table caveat. **The agent read the live page; I read a December snapshot; they disagree on at least six rows and on whether Alipay is accepted at all.**
- ⚠️ **Navitaire/dotREZ, `jqpay`, the nine Asian storefront method lists, the Japan two-tier fee, the SGD 10 flat fee and the Qantas-vs-Jetstar comparison are all agent-sourced and were not re-verified by me.** The CT-log evidence for Navitaire is independently checkable at `crt.sh` and is the strongest of these.
- ⚠️ **Qantas AR figures** (revenue, EBIT, seat factor, Note 34(C), the Jetstar Asia closure) are from the agent's extraction of the primary PDF. **Directionally certain and internally consistent; not re-extracted by me.**
- ⚠️ **The Navitaire cert found is valid to 2025-08-16 with no 2026 renewal in the result set** — possibly a crt.sh pagination artefact rather than decommissioning. The dotREZ pipeline breadth makes current use the strong reading.
- ❌ **No PSP or acquirer for JQ could be identified.** `booking.jetstar.com` is an Akamai bot-challenge shell; CSP carries only `frame-ancestors`; no `pay.`/`checkout.`/`gateway.` subdomains exist in DNS; the privacy policy names zero processors.
- 📌 **A documentation defect worth noting:** the AU payment-options page reportedly says Google Pay is accepted and that a fee will display — and the NZ fee table has a Google Pay row. **My snapshot of the AU table does include Google Pay**, so the agent's "missing row" finding may also be a dating artefact. **Another reason to re-check live.**
- 📌 **The Korean storefront reportedly offers POLi**, which is NZ-only — a copy bug, if current.

### Manual Research Recommendations
> **1. Load a live Jetstar booking to the payment page in a real browser** and read the network requests and iframe origins. **This is a ten-minute job that would name the acquirer and settle the entire fee-table dispute at once.** It is by far the highest-value action on this account.
> **2. Re-read the AU, NZ, SG and JP fee tables live** and date them. Do not quote a rate until this is done.
> **3. Confirm the Jetstar Japan exit timeline** and whether the acquiring unwind has a stated date.
> **4. Check whether Qantas and Jetstar share one AU acquirer.** The 17–35bp surcharge spread on identical schemes argues they price — and possibly acquire — separately.

---

## Executive Summary

Jetstar is Qantas's LCC — **FY26 revenue A$6,022M, Underlying EBIT A$723M, a record 89.1% seat factor** and a 16% margin on Australian domestic. The corporate shape has changed more than the target list suggests: **Jetstar Asia ceased operations on 31 July 2025** and Jetstar Pacific has been gone since 2020, leaving two operating airlines — though the Singapore *merchant entity* still sells in SGD and the site was still publishing Jetstar Asia fees fourteen months after the airline shut. The cleanest opening is dated and first-party: Qantas's own annual report discloses that **Jetstar Japan's card transactions are acquired through Qantas Group contractual arrangements**, and in the same report Qantas confirms a **binding agreement to exit Jetstar Japan** — so a shared merchant acquiring relationship has to be unpicked across a JV boundary on a deadline. Underneath sits **Navitaire New Skies**, confirmed through certificate transparency including a full `dotrez-*` CI/CD ladder, alongside Jetstar's own **`jqpay`** payment service in prod and UAT. And the method coverage tells the commercial story: across nine Asian storefronts the checkout offers international cards, UnionPay, JCB and wallets **and not one local rail outside Japan** — in the same year Jetstar launched six new leisure routes into Indonesia, the Philippines, Sri Lanka and the Pacific. Where they *do* run local rails, in Japan, **they charge ¥50–¥200 more to use them than to use a card.** ⚠️ One caution runs through this file: **`jetstar.com` is unreachable from this session**, my fee table is a December 2025 snapshot, and it **disagrees with the agent's live read on six rows and on whether Alipay is accepted** — so the structure is usable and the percentages are not, until someone opens a browser.

</details>
