# China Airlines

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 14 / 29 → 🟢 **Medium**
**Industry:** Airlines (passenger + unusually cargo-heavy) · **HQ:** Taoyuan, **Taiwan** — China Airlines Ltd, **TWSE 2610** · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** **Greenfield** — none detected. ⚠️ Weaker basis than most files here: mostly an absence of hits, with one piece of behavioural corroboration (see 3B).

> ⚠️ **Disambiguation, and get it right on the call:** China Airlines is **Taiwanese** (Taipei, TWSE 2610). It is **not** Air China, China Eastern or China Southern. Confusing them in an email would be fatal.

---

> ## 🎯 THE HOOK — a five-day single-scheme outage with no failover, and the workaround was "use a different payment method"
>
> **18–22 October 2023.** Mastercard authorisation failed on China Airlines' website for roughly four to five days. Visa worked throughout. From the customer thread:
>
> - CI's stated cause on 20 Oct: they had updated their **3-D Secure protocol** and *"mastercard沒有更新到"* — Mastercard had not updated to match
> - Customer service **denied any problem on 18 Oct** (*"都沒人反應"* — nobody has reported it), acknowledged it on the 20th with a two-day fix estimate
> - The workaround customers were given: **pay by LINE Pay instead and forfeit their card rewards**, or use a different card
>
> **A single scheme's 3DS mismatch took down card acceptance for days, and the only recovery path offered was manual.** That is what a merchant without routing or failover looks like from the outside.
>
> **And it is not one bad week.** Auth-failure complaints recur on Taiwan's PTT aviation board across **2018, 2020, 2023 and 2024** — one thread is titled *"華航網站購票常信用卡授權失敗"*, where **常** means *frequently*.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** China Airlines is Taiwan's flag carrier, TWSE-listed, with **FY2025 consolidated revenue of NT$209.09bn**. It is unusually cargo-weighted — roughly a third of revenue is freight, which is invoiced B2B and largely outside a card checkout. It also carries two subsidiary carriers on separate domains.

**SimilarWeb total visits:** **Not obtained.** No data supplied, and `china-airlines.com` returns HTTP 403 to automated fetches on every host. Country profile unverified; **no split invented.**

### Accepted methods — first-party, from CI's own 2022 press release
✅ **Verified by me directly** at `calec.china-airlines.com/csr/news20220816.html` (16 Aug 2022):

| Method | Scope, verbatim |
|---|---|
| **Visa, Mastercard, JCB** | *"VISA、Master Card、JCB 等信用卡"* |
| **LINE Pay** | **Taiwan-departing flights and the CI eMall only.** App, desktop web and mobile web. Usable for *"改票費用、預選座位及預購超額託運行李的付費"* — **change fees, seat selection and excess baggage**, not just the ticket. Must be linked to a Taiwan-issued card; **Visa/Mastercard/JCB only** |
| **PayPal** | **Nine markets:** *"台灣、日本、美國、加拿大、歐洲 (英國除外)、紐澳、菲律賓、新加坡、香港"* — Taiwan, Japan, US, Canada, Europe **excluding the UK**, Australia/NZ, Philippines, Singapore, Hong Kong |
| **UnionPay, WeChat Pay, Alipay** | *"銀聯支付、微信支付和支付寶"* — **mainland-China departures only** |
| **Miles + Cash** | *"哩程折抵票款"* split tender alongside full award tickets `[UNVERIFIED — URL only, page not fetched]` |

> 📌 **Read the scoping, because it is the pattern.** PayPal in nine named markets. LINE Pay only on Taiwan-departing. UnionPay, WeChat and Alipay only on China-departing. **Every method is bolted on per market rather than available per customer.** That is textbook pre-orchestration sprawl, and it comes from their own announcement.

### ⚠️ The biggest unknowns, and they are the Taiwanese rails that matter most
- **信用卡分期付款 (card instalments) — NOT ESTABLISHED.** Every instalment offer found is **bank-side or travel-agency**, not CI's own checkout. **Instalments are the dominant mechanic for high-ticket travel in Taiwan**, so whether CI offers them direct is the single most consequential open question on this account.
- **超商代收 (convenience-store cash at 7-ELEVEN / FamilyMart / ibon) — NOT ESTABLISHED.**
- **虛擬帳號 / ATM transfer — NOT ESTABLISHED.**
- **JKOPAY, Taiwan Pay, Apple Pay, Google Pay — NOT ESTABLISHED.**
- Multiple Taiwanese booking tutorials state the CI payment page shows *"共四個付款方式"* — **four payment options**. None transcribes them. **Four options would be a small, card-centric set for a Taiwanese merchant** — but it is unverified and must not be asserted.

### Known PSPs
**None. Zero PSPs, gateways or acquirers identified** — checked against NewebPay 藍新, ECPay 綠界, TapPay, O'Pay, ESUN/CTBC/Fubon/Taishin acquiring, Adyen, Worldpay, Cybersource, Braintree, Stripe, Checkout.com, AsiaPay, Amadeus, Accelya, CellPoint Digital and UATP. The carriage terms name only generic categories — *"資訊處理機構、代理商、政府機關、信用卡公司"*.

⚠️ **CTBC (中國信託) appears only as a co-brand card ISSUER**, on CI's own booking portal. **Do not infer acquiring from it.**

### Orchestration status
**None detected — greenfield.** ⚠️ **Honest caveat: this is mostly an absence of search hits.** CI does not appear on CellPoint Digital's airline customer wall or in its 2025 releases. The behavioural corroboration is the October 2023 outage: a single scheme failing for days with a manual workaround is not what a routing layer produces.

### Buying signals
- 🔴 **The Oct 2023 outage and a 2018–2024 pattern of auth-failure complaints**
- 🧩 **A visibly fragmented estate** — at least three booking front ends (`bookingportal.` on legacy .NET `.aspx`, `booking.`, `flights.`), plus `ancillary.`, a standalone **refund portal** at `calec.china-airlines.com/RefundPortal/`, `calee.`, `calcfec.`, `members.` and a separate e-shop on `cishop.cilink.com.tw`
- ✈️ **Three carriers, three sites** — CI plus **Tigerair Taiwan** (`tigerairtw.com`, FY2025 revenue NT$16.899bn, +2.90%) and **Mandarin Airlines** (`mandarin-airlines.com`). Separate stacks strongly implied, **not verified**
- 📱 **App rated 2.6/5** with 1M+ Play installs `[UNVERIFIED]`
- ❌ **No payment RFP, no payments hire, no 2025–26 payment programme found**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach China Airlines` to draft the 12-touch sequence.*

**Two instructions for whoever drafts it:**
1. **The Oct 2023 outage is the opener** and it is verified. Frame it as an observation about failover, not as a dig at their engineering.
2. **Do not claim they lack instalments or convenience-store payment.** Both are *unchecked*, not sourced-absent, and instalments in particular would be an embarrassing thing to get wrong in Taiwan. They belong in E3 as a question.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 14 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED as a bound, ~170,000+/month floor.** Sourced input: **FY2025 consolidated revenue NT$209.09bn** (Taipei Times, 14 Jan 2026). **Billing unit: bookings, not passengers** — one PNR covers several passengers, and changes, seat selection, excess baggage and the eMall each bill separately, which CI's own LINE Pay release confirms. **Presented as a bound because the divisor is unsourced:** even treating the *entire* NT$209bn as ticketed sales at an implausibly high NT$65,000 (~US$2,000) per booking gives ~3.2m bookings/year, **~268k/month**. ⚠️ **Roughly a third of revenue is cargo** — invoiced B2B, not card checkout — so the addressable figure is lower; against the ~NT$125bn passenger line the same implausible divisor still yields **~160k/month**. **Every plausible divisor clears the 100,000 band**, which is why this is ✅ rather than ⚠️. |
| Orchestration status | **+4** | ✅ **None detected.** ⚠️ **Weakest orchestration call in this repo** — principally an absence of hits, with the Oct 2023 no-failover outage as behavioural corroboration. **Verify on the call before building a sequence on "greenfield".** |
| 3+ countries | **+3** | ✅ **PayPal alone is scoped to nine named markets** in CI's own release, plus mainland-China departures on a separate method set. |
| Multiple PSPs | **0** | ⬜ **Zero PSPs identified**, first-party or third-party. Not "they have one" — nobody could name any. |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **Not scorable, and this is the most consequential gap.** Taiwan is obviously the #1 market, and **instalments (分期), convenience-store cash (超商代收) and ATM transfer are all NOT ESTABLISHED** — the payment page is JS-rendered and every CI host 403s. **Unchecked absence, not sourced absence.** Settle this and the row is very likely +3. |
| Recent expansion | **0** | ⬜ No dated 2025–26 market entry or payment programme found. |
| Payment issues reported | **+2** | ✅ **The strongest evidenced row.** The Oct 2023 five-day Mastercard 3DS outage is from a fetched customer thread with CI's own stated cause. Auth-failure complaints recur on PTT across **2018, 2020, 2023 and 2024**, one thread titled *"常信用卡授權失敗"* — *frequently*. |
| Funding >$10M | **0** | ❌ TWSE-listed. No round. |
| High traffic outside home | **0** | ⬜ No traffic data. Cannot verify either way. |
| Competitor using orchestration | **0** | ❌ None confirmed. |
| Payment job postings | **0** | ⬜ None found. |

**Tier: 14 / 29 → 🟢 Medium.** No analyst override applied.

> **Two rows are blocked rather than absent, and both are settleable in one browser session.** The rail gap needs someone to load the CI payment page from Taiwan; the PSP row needs the same walkthrough. If instalments and 超商代收 turn out to be missing, this becomes 17 ⭐ and a much sharper pitch. **I am not awarding points for a checkout nobody has seen.**

### Source Notes
- ✅ **The method table was verified by me directly** against CI's own press release, including the Chinese verbatim for every scope restriction.
- ✅ **FY2025 revenue NT$209.09bn** — Taipei Times, fetched. 📌 **That article's own USD conversion is wrong.** It renders NT$209.09bn as *"US$594 million"*; the correct figure is roughly **US$6.4–6.6bn**. **Use the NTD number and never repeat their conversion.**
- ✅ **The Oct 2023 outage thread was fetched**, including CI's stated cause and the CS denial-then-acknowledgement timeline.
- ⚠️ **Passenger/cargo split (passenger NT$124.9bn ~60%, cargo NT$66.8bn ~32%, +10.08%)** is `[UNVERIFIED — search summary only; investor PDFs return 403]`. The cargo skew is directionally important and should be stated out loud on any call: **a third of CI's revenue is freight and largely out of scope.**
- ⚠️ **`china-airlines.com` returns HTTP 403 to curl on every host** including `booking.`, `bookingportal.` and `calec.`; **WebFetch does reach the HTML**, but booking content is JS-rendered and investor PDFs 403. `web.archive.org` was unreachable during the run. **That combination is why the checkout is unseen.**
- ❌ **A Knoji claim that CI does not accept Apple Pay** (researched Feb 2023) is weak, dated and third-party. **Do not repeat it.**
- ❌ **"Four payment options" comes from Taiwanese booking tutorials**, none of which transcribes the four. Suggestive only.
- ⚠️ **Tigerair Taiwan and Mandarin Airlines run separate domains and separate FAQs**, so separate stacks are strongly implied — **not verified.** Do not assert a group-consolidation story until someone checks.

### Manual Research Recommendations
> **1. Load the CI payment page from a Taiwanese IP and screenshot it.** It settles instalments, 超商代收, ATM transfer, the wallets, *and* the "four options" claim in one pass — and it is the difference between 14 and 17.
> **2. Identify any acquirer or PSP.** Zero are known. The same walkthrough answers it.
> **3. Confirm whether Tigerair Taiwan and Mandarin run separate payment stacks** before pitching a group consolidation.
> **4. Get the FY2025 passenger/cargo split from the investor deck** rather than a news summary.

---

## Executive Summary

China Airlines is Taiwan's flag carrier, TWSE-listed, **FY2025 revenue NT$209.09bn**, and unusually cargo-heavy — roughly a third of that is freight and largely outside a card checkout, which any pitch must say out loud. Its published method set is **scoped market by market**: PayPal in nine named markets, LINE Pay only on Taiwan-departing flights, and UnionPay, WeChat Pay and Alipay only on mainland-China departures — bolted on per market rather than available per customer. The estate is visibly fragmented across at least three booking front ends, a standalone refund portal, a separate e-shop domain and two subsidiary carriers on their own sites. The strongest verified asset is a **five-day Mastercard authorisation outage in October 2023** caused by CI's own 3DS update, where Visa kept working, customer service denied the problem for two days, and the remedy offered was to pay by LINE Pay and forfeit card rewards — with matching auth-failure complaints recurring across 2018, 2020 and 2024. **Two things are unknown because nobody can see the checkout: whether CI offers card instalments — the dominant mechanic for high-ticket travel in Taiwan — and which acquirer it runs on.** Settling those in one browser session would likely move this from 14/29 to ⭐.

</details>
