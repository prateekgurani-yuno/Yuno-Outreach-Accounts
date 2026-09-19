# Nok Air

**Status:** 🔴 Not ICP — analyst override (in court-supervised rehabilitation until ~2028)
**ICP Score:** not scored → **override applied before scoring**
**Industry:** Airlines (low-cost, mainly domestic) · **HQ:** Bangkok (Don Mueang), **Thailand** — บมจ.สายการบินนกแอร์ · **Researched:** 2026-09-19 · **First email sent:** —
**Motion:** n/a — rejected

---

> ## 🔴 REJECTED ON AN ANALYST OVERRIDE — AND THE DISTINCTION MATTERS
>
> ⚠️ **This is NOT a volume-gate rejection. The volume gate CLEARS.** Derived direct-channel transactions land at roughly **55,000–107,000 per month**, comfortably above the 40,000 floor. **Recorded honestly so nobody later "corrects" this file on the wrong grounds.**
>
> **The rejection is that Nok Air cannot buy.**
>
> ✅ **Verified by me directly** at InfoQuest, 24 July 2025 — headline 「**"นกแอร์"เล็งออกจากแผนฟื้นฟู ก.ย.71**」, *"Nok Air aims to exit the rehabilitation plan in September 2571"* (**2571 BE = 2028 CE**). CEO **วุฒิภูมิ จุฬางกูร** (Wuthipoom Jurangkool), verbatim:
>
> > 「การออกจากแผนฟื้นฟูของนกแอร์อยู่ในหลักการว่าจะต้องชำระหนี้ได้ตามแผน ซึ่งขณะนี้เจ้าหนี้ ไม่รวมส่วนของผู้ถือหุ้นเหลืออยู่ประมาณ **400 ล้านบาท** ซึ่งบริษัทตั้งเป้าออกจากแผนฟื้นฟูในราว **เดือน ก.ย. 71**」
>
> *"Exiting the rehabilitation plan depends in principle on repaying debt according to the plan. Creditors, excluding the shareholders' portion, currently amount to about **THB 400 million**, and the company targets exiting the rehabilitation plan around **September 2028**."*
>
> The same article records 「ประสบกับการขาดทุนติดต่อกันยาวนานกว่า **9 ปี**」 — **more than nine consecutive years of losses.**
>
> 📌 **A company under Central Bankruptcy Court supervision has a plan administrator gating discretionary spend.** Material new vendor commitments need administrator and creditor sign-off. **There is no budget authority to sell to, and won't be for roughly three years.**
>
> **Supporting, but agent-reported and NOT verified by me:** delisted from the SET effective **9 January 2025** after ~11 years listed; shareholders' equity approximately **THB −2.7bn**; creditors separately seeking to claw back THB 27.3bn; and an **August 2025 CAAT safety action** restricting the AOC to domestic-only, since apparently lifted with international services planned from 14 October 2026.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** A Thai LCC flying ~15 domestic routes from Don Mueang with **8 of 14 aircraft operational** as of mid-2025, ~100 flights a day and ~80% cabin factor. Genuinely operating, and genuinely improving — but under court supervision.

### ❌ THE STUB'S ~$300M FY24 REVENUE IS REFUTED
FY2024 revenue is approximately **THB 6,000–7,000m**, which at ~34 THB/USD is **US$175–205m**. **The stub overstates by roughly 40–50%.** Recommend the target list be corrected. `[Revenue band UNVERIFIED — search summary; the Jan–Jul 2025 figure of ~THB 4,000m is from the InfoQuest article I fetched.]`

### 💡 The payment stack is genuinely interesting — which is why this is a diary entry, not a kill
**Prateek's stub hypothesis was right, and then some.** The stub said bookings are *"often paid at local counters, by bank transfer or e-wallet"* — **confirmed, and the offline rail is not a side channel but a first-class, heavily built-out part of the checkout.** From Nok's own Thai-language booking page:

| Rail | Detail |
|---|---|
| **ATM via Paycode** | TTB, Bangkok Bank, SCB, Krungthai |
| **Counter Service @ 7-Eleven** | cash, all channels |
| **Krungthai Bank branch counter** | web, app, call centre |
| **CenPay · Big C · SE-ED Book Center** | physical payment points |
| **Airport ticket desk** | cash and card |
| Cards · QR Payment · UnionPay · **Alipay · WeChat Pay · LINE Pay** · direct debit / internet banking | online |
| Call centre 1318 | **THB 225 incl. VAT per booking per passenger** |

❌ **Sourced-absent from that page:** instalments (ผ่อนชำระ) — notable for Thai high-ticket retail — plus BNPL, TrueMoney, ShopeePay and Rabbit LINE Pay.
⚠️ **"QR Payment" is listed but never named as PromptPay.** In Thailand a merchant QR is almost always PromptPay Bill Payment, **but that is inference, not evidence.** Do not assert it.

### ✅ NAVITAIRE REFUTED — they run Sabre
I asked the agent to check Navitaire hard, because HK Express and Jetstar both run New Skies. **It is not Navitaire.** `booking.nokair.com` loads its API from **`https://nokair-api.ezycommerce.sabre.com`** — **Sabre EzyCommerce** (the Radixx-lineage LCC platform Sabre acquired in 2019), with content from Prismic CMS. **Zero Navitaire, New Skies or SkySales fingerprints anywhere.** That is affirmative evidence, not an absent hit.

📌 **And it matters strategically:** Sabre EzyCommerce's native payment module typically brokers multiple PSPs and local methods **inside the PSS** — which is both the reason an LCC this size has no separate orchestration layer, and **the structural competitor to a Yuno pitch.**

❌ **The acquirer/PSP is NOT ESTABLISHED.** CSP on both hosts is only `upgrade-insecure-requests` — no allowlist to mine. The agent explicitly declined to name a likely Thai PSP from the method bundle, which was the right call.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

**None, and none should be generated.** `/full-outreach` must never run on a rejected company.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### Why this was not scored on the 29-point matrix
The override applies **before** scoring, the same treatment given to the volume-gate rejections in this pipeline. Assigning a number would imply a comparability the account does not have while it sits under court supervision. **Recorded as an override, not as a low score, and not as a volume failure.**

### Source Notes
- ✅ **The decisive fact — a September 2028 rehabilitation exit target and ~THB 400m of remaining creditor debt — was verified by me directly** from InfoQuest (24 Jul 2025), including the CEO's verbatim Thai and the nine-consecutive-years-of-losses line.
- ✅ **Sabre EzyCommerce confirmed** from the booking host's own API endpoint; **Navitaire refuted** on the same evidence.
- ✅ **The payment-method table** was fetched by the agent from Nok's own Thai-language booking page. ⚠️ **That page's copyright reads ©2024 and may be stale**, and no live checkout was reached — so a real booking session may expose methods it omits.
- ⚠️ **The SET delisting (9 Jan 2025), negative equity of ~THB −2.7bn, the THB 27.3bn clawback claim and the CAAT AOC restriction are all agent-reported `[search summary only]`** and were not verified by me. **They corroborate the override; the override does not depend on them.**
- ⚠️ **FY2024 net profit is unresolved** — sources give THB 60m and THB 90m.
- ❌ **No going-concern audit opinion was obtained.** Post-delisting, filings sit on `sec.or.th` rather than SET. Negative equity plus active rehabilitation makes an emphasis-of-matter likely, **but it is not asserted.**
- ❌ **Direct versus OTA/agent distribution split: not established** — the largest analytical hole, and the one that would most move the volume arithmetic. Nok sells heavily through airport desks, 7-Eleven, CenPay, Big C, SE-ED, a call centre and a dedicated travel-agent channel; **much of that is not card-not-present traffic we would touch**, and OTA bookings settle on the OTA's rails.
- ❌ **Bangkok Post article on the red flag being lifted returns HTTP 451 (geo-block)** to both curl and WebFetch.
- 📌 **An unrelated observation worth recording:** `content.nokair.com` served the agent's anonymous, cookie-less request **a page rendered with another user's logged-in state** (a named Nok Fan Club member and point balance). Consistent with Cloudflare edge-cache poisoning of a personalised Kentico page. **Not a payments finding and not verified** — but a credible security talking point if this account ever revives.

## Rejection Rationale

Nok Air is in active business rehabilitation under Thailand's Central Bankruptcy Court with a targeted exit of **September 2028**, verified from the CEO's own statement, following more than nine consecutive years of losses and with roughly THB 400m of creditor debt still to repay under the plan; a plan administrator gates discretionary spend, so there is no budget authority capable of signing a payments contract. **This is an analyst override, not a volume rejection — the volume gate clears at a derived 55,000–107,000 direct transactions per month.**

> ### 📅 REVISIT TRIGGER — late 2028
> **Rehabilitation exit plus SET relisting.** The account is otherwise a reasonable fit: a Thai LCC with an unusually deep offline cash rail, no orchestration layer, an undisclosed acquirer, and Sabre EzyCommerce as the incumbent payment surface to displace. **The revenue figure in the target list should be corrected to ~US$175–205m regardless.**

</details>
