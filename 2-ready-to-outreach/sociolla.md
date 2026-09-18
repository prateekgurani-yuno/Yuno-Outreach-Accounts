# Sociolla

**Status:** 🟢 Ready to outreach — sequence drafted
**ICP Score:** 13 / 29 → 🟢 **Medium**
**Industry:** Beauty retail, omnichannel (e-commerce + 150 physical stores + SOCO app) · **HQ:** Jakarta Barat, Indonesia — **PT Social Bella Indonesia** · **Owner:** **General Atlantic, 54% since 23 Dec 2025** · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** **In-house layer** — a dedicated first-party payments microservice, verified live in June 2026. Respect the build; anchor on opportunity cost and reach, never "you need orchestration".

---

> ## 🎯 THE HOOK — a new majority owner, a hand-built payments service, and cards declining that work elsewhere
>
> **They built their own payments layer.** From Sociolla's own homepage source, captured June 2026 and **verified by me**, the site declares a microservice estate:
>
> `payments-api.sociolla.com` · `carts-api` · `orders-api` · `shipping-api` · `catalog-api1…5` · `soco-api` · `sso-broker.sociolla.com`
>
> **A separately-deployed payments service that has survived at least two front-end rewrites** — a home-grown abstraction sitting over Midtrans, a direct BCA integration, Kredivo and Vospay.
>
> **And it is visibly straining.** From the Apple App Store, Indonesian storefront, **22 June 2026**, one star, verbatim:
>
> > *"payment pke CC bolak balik gk bs, cb pke cc lain gk bs. **pdhl di app lain aman aja**"*
> > — *"Card payment fails over and over. I tried a different card, that fails too. Yet it works fine on other apps."*
>
> **Two different cards declining on Sociolla while working elsewhere is not a customer problem.** That is the exact failure mode a second acquirer and retry routing exist to fix.
>
> **The timing:** **General Atlantic took 54% on 23 December 2025.** New majority owner, nine months in, with a 500-store ASEAN expansion plan.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Sociolla is Indonesia's largest beauty retailer, operating sociolla.com, the SOCO app and **150 physical stores across Indonesia**, plus a Vietnamese storefront. Founded 2014, backed by Temasek, East Ventures, Jungle Ventures and L Catterton, and majority-acquired by **General Atlantic in December 2025**.

**SimilarWeb total visits:** **Not obtained.** `sociolla.com` is behind CloudFront/WAF (403) and no data was supplied. ecdb puts **97% of revenue in Indonesia** — the only geographic split available.

### Markets
| Market | Status | Evidence |
|---|---|---|
| **Indonesia** | ✅ Primary — 150 stores, ~45+ cities, 97% of revenue | Nikkei Asia; ecdb |
| **Vietnam** | ✅ Live — `vn.sociolla.com` crawled 2026-06-17 | Wayback CDX |
| Thailand, Philippines, Malaysia, Singapore | 🎯 Stated targets | `[UNVERIFIED — search summary only]` |

*The 2025 site revamp ships a country switcher with exactly two flags, `flag-id.svg` and `flag-vn.svg`. **No third market on the web front-end.***

### Known PSPs
- **Midtrans / Veritrans** — ✅ **confirmed from their own page source.** `api.midtrans.com/v2/token` and the Midtrans tokenisation JS both embedded, plus `veritrans.png` / `midtrans.png` on their own checkout and a `/veritrans-payment` callback route
- **BCA KlikPay** — ✅ **confirmed, and it is a direct bank integration, not a gateway passthrough.** Five dedicated routes: `klikpay-inquiry`, `klikpay-payment`, `klikpay-payment-flag`, `klikpay-validation`, `klikpay-thankyou`
- **Kredivo** (BNPL) — ✅ dedicated routes live to Jan 2025
- **Vospay** (cicilan/instalments) — ✅ dedicated route live to Apr 2024
- ❌ **Not found:** Xendit, DOKU, Faspay, iPay88, 2C2P, Espay, NicePay, Winpay, Durianpay, Stripe, Adyen, Checkout.com

### Orchestration status
**In-house layer.** Affirmatively evidenced by `payments-api.sociolla.com` as a distinct microservice, current June 2026. **No third-party orchestrator detected** — zero hits for Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY and Yuno, though that half is an absence of search hits rather than affirmative proof.

### Buying signals
- 💰 **General Atlantic acquired 54%, 23 December 2025** — new majority owner, reportedly ~US$250m mostly secondary with a ~$10m primary injection
- 🚀 **From 2 stores in 2019 to 150 today**, targeting **500** and naming Thailand, Philippines, Malaysia and Singapore as next markets
- 🔴 **Dated payment failures in 2026 app reviews** — see Section 5
- 🧾 **A hand-reconciled bank-transfer rail may still run:** their T&C requires *"pembeli memberikan konfirmasi pembayaran melalui e-mail ke cs@sociolla.com"* — the buyer emails proof of payment — and a 2026 review still complains of *"2 days payment confirmation"*
- 💼 **Backend engineering roles open (PHP)** — the legacy PrestaShop stack is still being maintained alongside the microservices. **No payments-specific role found**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

### Pain Vector Extraction

```
=== PAIN VECTOR EXTRACTION ===

Motion: IN-HOUSE. They built payments-api.sociolla.com deliberately and it works. The
        rulebook is explicit: respect the build, anchor on opportunity cost and reach,
        never argue the build was wrong. Phase 1 must NOT imply they lack orchestration —
        they have their own.

Observable setup facts (verified first-hand, 2026-09-18):
- payments-api.sociolla.com is a distinct deployed microservice, present in the June 2026
  capture alongside carts-api, orders-api, shipping-api, catalog-api1-5, soco-api,
  bj-public-api and sso-broker.sociolla.com
- Midtrans confirmed from their own page source (api.midtrans.com/v2/token + tokenisation JS)
- BCA KlikPay is a DIRECT bank integration, five dedicated routes: klikpay-inquiry,
  klikpay-payment, klikpay-payment-flag, klikpay-validation, klikpay-thankyou
- Kredivo and Vospay each have their own dedicated route sets
- App Store review, Indonesian storefront, 2026-06-22, 1 star, verbatim:
  "payment pke CC bolak balik gk bs, cb pke cc lain gk bs. pdhl di app lain aman aja"
  = "Card payment fails over and over. Tried a different card, also fails. Yet it works
  fine on other apps."
- App Store, 2026-06-03, 3 stars: checkout failed twice, voucher and gift-with-purchase lost
- 150 stores from 2 in 2019; targeting 500; Thailand, Philippines, Malaysia, Singapore named
- General Atlantic took 54% on 23 December 2025

Selected observations for Phase 1 (E1 bullets, ranked by materiality):
1. The card decline, in their customer's words → "One of your App Store reviews from June
   says two different cards failed on Sociolla and both worked fine on other apps."
   MATERIALITY: highest. It is dated, public, specific, and it is a customer's words rather
   than my inference. Observation, not projected pain — Phase 1 compliant.
2. The build, stated respectfully → "You run your own payments service alongside carts,
   orders and shipping, with Midtrans and a direct BCA integration underneath it."
   MATERIALITY: high. Demonstrates I understand what they built before saying anything else.
   This is the line that earns the right to the rest of the sequence with an in-house team.

   (Held at 2. Deliberately NOT used: QRIS. It is the most consequential unknown in the file
   and the evidence is a 2019-2020 inventory. Claiming they lack QRIS would very likely be
   wrong and would end the thread. It appears as a QUESTION in E3, never as a claim.)

Bridge variant: A — complexity
Rationale: multi-provider and multi-channel is established — Midtrans, direct BCA, Kredivo,
Vospay, across web, app and 150 stores in two countries. Variant A describes that shape
without implying the in-house build was a mistake, which the motion override forbids.

Hypothesis for Phase 2 (E3):
With one card gateway underneath their own layer, a declined card has nowhere to go. The
service can route between methods but not between acquirers, because there is only one.
Backing logic: Midtrans is the only card gateway found; BCA KlikPay, Kredivo and Vospay are
method-specific rails, not alternative card acquirers. So when a card fails, the only
fallback available is "pick a different method", which is what the reviewer experienced as
two cards failing in a row.

Success case for Phase 3 (E4):
Selected case: Livelo
Tier: 2 — same payment pattern (a declined card with no second acquirer to fall to),
different industry and region. Stated in the email.
Match rationale: the library flags Livelo as the decline-cascade case, and its mechanism —
instantly re-routing a declined transaction to a secondary acquirer — is a direct answer to
the exact failure the 22 June reviewer described. No Tier 1 exists; there is no Indonesian
or beauty-retail case in the library.
Numbers to lead with: +5% approval rate · 50% of failed transactions recovered by instant
re-routing to a secondary acquirer · millions of R$ saved
Optional benchmark: SKIP. The "~8% average authorisation uplift" is Yuno's own blog figure.

Touch-by-touch angles:
- E2 angle: the decline with no fallback → routing and retry across acquirers (one mechanism)
- LK1 angle: the June review, one sentence
- LK2 angle: one card gateway under the layer means a decline has nowhere to go
- LK3 angle: Livelo recovered half its failed transactions by sending the retry elsewhere
- LK4 angle: FRESH — 150 stores from 2, four more ASEAN markets named
- E8 angle: clean exit, offer to circle back after the GA-backed expansion firms up
```

**Calendar.** Day 1 anchored to **Monday 21 September 2026**. Times are **WIB (UTC+7), which
is IST+1:30** — the working day overlaps almost entirely.

> ⚠️ **Indonesian public holidays for this window could NOT be verified.** Indonesia's 2026
> calendar includes 17 national holidays plus eight *cuti bersama* collective-leave days set
> by joint ministerial decree, and I could not source the specific September–October dates.
> **Check publicholidays.co.id before sending** — a slot landing on a *cuti bersama* is worse
> than one landing on a public holiday, because the office is empty without it being obvious.

---

### Phase 1 — Curiosity (Days 1–5)

#### Touch 1 — Email 1 · Day 1 · Mon 21 Sep

**Subject:** A card decline in your June reviews

```text
Hey {{recipient.first_name}},

Spent some time on Sociolla's payment setup. Two things stood out:

- One of your App Store reviews from June says two different cards failed on Sociolla, and that both worked fine on other apps.
- You run your own payments service alongside carts, orders and shipping, with Midtrans and a direct BCA integration underneath it.

That kind of setup usually comes with some complexity.

I work at Yuno — top-100 fintech, a16z-backed. We consider ourselves the 'everything payments' platform: one integration, every PSP, every method, every market.

Rather than pitch you based on assumptions, is there anything payment-related you're working through that we might be able to help with?

Best,
Prateek
```

#### Touch 2 — Email 2 · Day 3 · Wed 23 Sep · REPLY IN THREAD

```text
Hey {{recipient.first_name}},

Following up. Wanted to put a bit more behind what Yuno actually does, and how it would sit with what you've already built.

- We sit above your existing providers, not instead of them. Your service keeps doing what it does.
- A declined card can be retried through a different acquirer automatically, rather than ending there.
- Retry logic runs on its own schedule instead of firing back at the same rail.
- Adding an acquirer or a method becomes configuration rather than a build against your own layer.

On the June review specifically, the part that matters is that second acquirer. Two cards failing in a row usually means the retry went back to the same place. With somewhere else to send it, the second attempt is a different rail rather than a repeat.

I'll keep sharing what I'm seeing every few days. If your stack's where you want it, just say the word and I'll back off. Otherwise happy to go deeper.

Cheers,
Prateek
```

#### Touch 3 — LinkedIn message 1 · Day 5 · Fri 25 Sep

```text
Hey {{recipient.first_name}} — dropped you a note over email, flagging it here too in case this is the easier channel. Quick one: a June App Store review says two different cards failed on Sociolla and both worked elsewhere. Curious whether that's a known pattern on your side or a one-off.
```

---

### Phase 2 — Diagnosis (Days 7–9)

#### Touch 4 — Email 3 · Day 7 · ~~Sun 27 Sep~~ → **send Mon 28 Sep** · NEW EMAIL

**Subject:** One card gateway under the layer

```text
Hey {{recipient.first_name}},

Going to take a swing at this. My read is that your payments service can route between methods but not between card acquirers, because there is only one underneath it.

Midtrans looks like the card rail. BCA KlikPay, Kredivo and Vospay are method-specific, so they are alternatives to a card rather than alternatives to an acquirer. Which means a declined card has nowhere to go but back to the same place, and the shopper experiences that as what your June reviewer described. Not because anyone built it badly — it is just what one acquirer allows.

Genuinely curious about one thing: do you run QRIS end-to-end across web, app and the stores, and is that acquired through the same rail?

At Yuno (a16z-backed, top-100 fintech) we sit above what you've already built, so your service keeps its logic and gains somewhere else to send a failed attempt. Keep your stack, add what's missing.

Thursday 1 October is open. Would 10am or 3pm your time work for a quick 15?

All the best,
Prateek
```

#### Touch 5 — LinkedIn message 2 · Day 9 · Tue 29 Sep

```text
Hey {{recipient.first_name}} — sent a longer note over email this week. Short version: your own payments layer can route between methods, but with one card acquirer underneath it a declined card has nowhere else to go. If that's anywhere on your radar, would Friday 2 or Monday 5 October at 11am your time work for a quick 15?
```

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · Thu 1 Oct · NEW EMAIL

**Subject:** How Livelo solved this

```text
Hey {{recipient.first_name}},

On the read I shared last week. Sharing a quick example of what solved looks like.

Livelo had the same shape: a declined transaction that ended where it failed. They put Yuno above the existing stack so that a decline gets instantly re-routed to a secondary acquirer instead. What that produced:

- Approval rate up 5%
- 50% of failed transactions recovered (half of them, which is the number that got my attention)
- Millions of reais saved

Worth saying plainly: Livelo is a Brazilian loyalty business, so this is a payment-pattern match rather than an industry one, and those results came out of Brazil. What carries over is the mechanism — a second acquirer to fall to, which is the piece a single card rail cannot provide however good the layer above it is.

Same orchestration layer above their existing stack. No rip-out.

Wednesday 7 October is open. Would 2pm or 4pm your time work for 15 minutes?

Full case here if useful: https://y.uno/en/success-stories/livelo

Thanks,
Prateek
```

#### Touch 7 — Email 5 · Day 13 · ~~Sat 3 Oct~~ → **send Mon 5 Oct** · MANUAL

*Placeholder — manual creative approach. Do not auto-write.*

> **Strongest asset:** the review corpus itself, presented back neutrally. Three dated 2026
> App Store reviews — **22 June** (two cards declined, work elsewhere), **3 June** (checkout
> failed twice, voucher and gift-with-purchase lost), **10 September** (funds held on a
> sold-out item, no self-serve refund). Present as data, not as an attack, and **include the
> 30 July five-star review saying the payment methods are easy** — the balance is what makes
> it credible rather than a hit piece.

#### Touch 8 — Email 6 · Day 15 · ~~Mon 5 Oct — taken by the shifted E5~~ → **send Tue 6 Oct** · MANUAL

*Placeholder — second manual approach, different format from E5.*

> **Suggested angle: Vietnam.** Research found `vn.sociolla.com` carrying Midtrans, BCA
> KlikPay, Kredivo and Vospay routes — **all Indonesian rails** — with MoMo, ZaloPay, VNPay
> and VietQR all not found. ⚠️ **That evidence is from 2022 and the current state is
> unverified.** Frame it as a question, never a claim: *"is Vietnam still running on the
> Indonesian checkout, or has it been localised since?"* If the answer is yes, it becomes the
> centre of the whole account.

#### Touch 9 — LinkedIn message 3 · Day 17 · Wed 7 Oct

```text
Hey {{recipient.first_name}} — Livelo recovered half of its failed transactions just by sending the retry to a different acquirer, without changing what it already had. Worth 15 minutes to see whether that maps to your setup? Monday 12 October at 10.30am your time is open.
```

---

### Touch 10 — Email 7 · Day 19 · Fri 9 Oct · MANUAL

*Placeholder — manual creative bridge. Anchor to something fresh.*

> **Freshest hook: General Atlantic took 54% on 23 December 2025.** A new majority owner
> roughly nine months in, with a stated path from 150 stores to 500 and four more ASEAN
> markets named. New ownership is when infrastructure decisions get revisited, and a payments
> layer built for one-and-a-bit countries is exactly the kind of thing that surfaces.
> ⚠️ **Deal specifics beyond "General Atlantic, 54%" are unverified** — do not cite the
> value, the valuation or which investors exited.

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21 · ~~Sun 11 Oct~~ → **send Mon 12 Oct**

```text
Hey {{recipient.first_name}} — last LinkedIn ping from me on this. One thing I never raised: you've gone from 2 stores in 2019 to 150, with Thailand, the Philippines, Malaysia and Singapore named next. Four new markets is four new rail sets against your own layer. If timing works, Thursday 15 October at 3.30pm your time is open for a quick 15.
```

#### Touch 12 — Email 8 · Day 23 · Tue 13 Oct · REPLY IN THREAD to Touch 4 or Touch 6

```text
Hey {{recipient.first_name}},

Going to stop pinging unless you want to pick this back up.

If the timing is just off, happy to circle back once the next wave of market launches firms up. And if payments sits with someone else on your side, happy to be pointed there.

If it ever comes back up, just reply here.

All the best,
Prateek
```

---

### CTA schedule — five distinct slots, all WIB

| Touch | Sent | Proposed slot(s) | WIB → IST |
|---|---|---|---|
| E3 | Mon 28 Sep | **Thu 1 Oct, 10:00 or 15:00** | 11:30 / 16:30 IST |
| LK2 | Tue 29 Sep | **Fri 2 or Mon 5 Oct, 11:00** | 12:30 IST |
| E4 | Thu 1 Oct | **Wed 7 Oct, 14:00 or 16:00** | 15:30 / 17:30 IST |
| LK3 | Wed 7 Oct | **Mon 12 Oct, 10:30** | 12:00 IST |
| LK4 | Mon 12 Oct | **Thu 15 Oct, 15:30** | 17:00 IST |

⚠️ **Verify against Indonesian public holidays and *cuti bersama* before sending** — see the
calendar note above. No booking link anywhere, by decision.

---

### Source Notes

- ✅ **`payments-api.sociolla.com` verified by me** in the 2026-06-08 capture, alongside the other named microservices. E1's second bullet rests on this and is accurate.
- ✅ **The June review is quoted from the Apple RSS customer-reviews API**, Indonesian storefront, dated 2026-06-22. E1 paraphrases it in English rather than quoting the Indonesian, which keeps it readable without changing the claim.
- ✅ **Midtrans confirmed from Sociolla's own page source**; BCA KlikPay from five dedicated routes.
- ✅ **Livelo is Tier 2 and E4 says so outright**, including that the results came from Brazil.
- ⚠️ **THE MOTION IS IN-HOUSE AND THE SEQUENCE IS BUILT FOR IT.** E1's second bullet names what they built, E2 opens *"how Yuno would sit with what you've already built"*, E3 includes the diplomatic clause *"not because anyone built it badly"*, and E4 closes on *"the piece a single card rail cannot provide however good the layer above it is"*. **Nothing in the sequence suggests the build was wrong.** If anyone edits these touches, preserve that.
- ⚠️ **QRIS appears only as a question in E3, never as a claim.** The evidence for its absence is a 2019–2020 inventory taken before QRIS became near-universal in Indonesian retail. **Asserting they lack QRIS would very likely be wrong and would end the thread.**
- ⚠️ **The Vietnam angle is a 2022 finding and is flagged as a question in E6, not a claim.**
- ⚠️ **Indonesian public holidays could not be verified for the window.** Flagged on the calendar and in the CTA table.
- ❌ **ecdb's US$6m revenue figure is rejected and appears nowhere.** No volume or revenue claim is made in any touch.
- ❌ **General Atlantic deal specifics beyond the 54% and the date are unverified** and E7's note says so explicitly.
- ❌ **No recipient identified.** All twelve touches use `{{recipient.first_name}}`.

### Success Case Alternatives
- **Rappi** — hundreds of methods through one integration, 80% less analyst work. The better swap if discovery shows the pain is **reconciliation across 150 stores plus web plus app** rather than card declines.
- **Vibra** — new-user approval up more than 30 points to 80%. Worth switching to if the conversation turns to **first-time-buyer conversion**, plausible given SOCO's 1M+ app installs.
- **inDrive** — 10 new countries in under 8 months. The right swap if the four named ASEAN markets become the centre of the conversation.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 13 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+3** | ⚠️ **NOT FOUND — ASSUMED ~50,000–100,000 online transactions/month.** `[ASSUMPTION — not researched.]` **No order count, GMV or AOV is published.** **Billing unit counted: online transactions only** — the 150 physical stores generate card-present volume that orchestration does not address, so counting them would overstate the addressable number. **Basis:** 1M+ SOCO app downloads, 150 stores in ~45 cities, a ~US$595m valuation at the General Atlantic deal. ⚠️ **ecdb's US$6m 2025 web revenue figure is rejected** — it is implausible for a 150-store omnichannel retailer valued near US$600m and is almost certainly a model of the .com web shop alone. **I have not built a derivation on it.** Scored conservatively; an assumption cannot fire the under-40k gate. |
| Orchestration status | **+1** | ✅ **In-house layer, affirmatively evidenced.** `payments-api.sociolla.com` is a distinct deployed service alongside carts, orders, shipping and catalog APIs, still present in the June 2026 capture. |
| 3+ countries | **0** | ❌ **Genuinely not met — this is a two-market business.** Indonesia and Vietnam, and their own country switcher carries exactly two flags. Entities: PT Social Bella Indonesia is confirmed; PT Sociolla Ritel Indonesia and a Singapore holdco are both unverified, so the 3-entity route does not clear either. |
| Multiple PSPs | **+3** | ✅ **Midtrans/Veritrans confirmed from their own page source**, plus a **direct BCA KlikPay integration** with its own five-route inquiry/validation/callback set, plus Kredivo and Vospay. |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **Not scorable, and this is the most consequential gap in the file. QRIS is NOT FOUND — but the last readable payment inventory is 2019–2020**, and the site went to a Vue SPA afterwards, so archived captures return only a 27.8KB shell. QRIS became near-universal in Indonesian retail *after* that inventory. **That is unchecked absence, not sourced absence, and the matrix requires a source.** Same for DANA, ShopeePay and Alfamart OTC. **Do not claim any of these are missing.** |
| Recent expansion | **+2** | ✅ **2 stores in 2019 → 150 today** (Nikkei), targeting 500, with Thailand, Philippines, Malaysia and Singapore named. Vietnam live. |
| Payment issues reported | **+2** | ✅ **Dated, specific, and from the Apple RSS reviews API** — two cards declining while working on other apps (2026-06-22), checkout failing twice with voucher and gift-with-purchase lost (2026-06-03), funds held on a sold-out item with no self-serve refund (2026-09-10). Moderate frequency. ⚠️ **Counterpoint kept on the record:** a 5★ from 2026-07-30 says *"metode pembayaran nya pun mudah"* — payment methods are easy. It is not uniformly bad. |
| Funding >$10M | **+2** | ✅ **General Atlantic took 54% on 23 December 2025** — within 12 months. ⚠️ Mostly a **secondary** purchase with a reported ~$10m primary, so it is a control transaction rather than a growth round. Scored on the capital event and the new owner's mandate. Deal specifics beyond "General Atlantic, 54%, Indonesia" are `[UNVERIFIED — search summary only]`. |
| High traffic outside home | **0** | ❌ Not met. ecdb puts **97% of revenue in Indonesia**. Home-dominant by any measure. |
| Competitor using orchestration | **0** | ❌ None confirmed. |
| Payment job postings | **0** | ⬜ Backend PHP, front-end, PM and design roles found. **No payments-specific role naming a provider.** |

**Tier: 13 / 29 → 🟢 Medium.** No analyst override applied.

> **Why not higher, and why that is the right answer.** Two rows that would lift this are genuinely blocked rather than absent. **QRIS is the big one** — if Sociolla does not run QRIS end-to-end across web, app and 150 stores, that is a +3 row and a much sharper pitch; if they do, the rail argument collapses and the account becomes a pure reach-and-reconciliation story. **Nobody can tell from outside**, because the live site is WAF'd and the archive stops at an SPA shell. And the two-market footprint is a real structural limit, not a research gap.

---

### ⚠️ The strangest finding, and the sharpest one if it still holds

**Vietnam appears to have launched on a copy of the Indonesian checkout.** `vn.sociolla.com` carries `veritrans-payment`, the five `klikpay-*` routes, `faq-kredivo`, `kredivo-notification`, `kredivo-success` and `vospay-transaction-success` — **Midtrans, BCA KlikPay, Kredivo and Vospay are all Indonesian rails**, and all four have routes on the Vietnamese storefront (captured 2022-06-27).

Meanwhile **MoMo, ZaloPay, VNPay and VietQR are all NOT FOUND** for Vietnam.

> **If that is still true in 2026, it is the best observation in this file:** a Vietnamese storefront running Indonesian payment rails, with none of Vietnam's dominant wallets. **But the evidence is from 2022 and the current state is unverified** — the VN site is an SPA shell in every later capture. **Treat as a question to ask, not a claim to make.** Confirming it is the single highest-value manual action on this account.

---

### Section 4. Local payment methods — Indonesia

**⚠️ Read the vintage caveat first.** The last **server-rendered** payment inventory is **2019–2020**. Post-2020 the site is a Vue SPA and archived captures return a 27.8KB shell with no payment content. **"Not found" below usually means "not visible in the last readable inventory", not "absent today".**

**CONFIRMED** from their own `/how-to-pay` tab list and footer icon set: **Bank transfer / VA (BCA, Mandiri, BNI, BRI, Permata, CIMB Clicks, Panin, UOB, digibank, Niaga) · Credit & debit cards (Visa, Mastercard, JCB, American Express) · Indomaret OTC cash · OVO · GoPay · LinkAja (+ legacy TCASH) · Kredivo · Vospay · COD · in-store cash · card instalments (cicilan)**.

**NOT FOUND — and explicitly unchecked, not sourced-absent: QRIS · DANA · ShopeePay · Alfamart OTC · Akulaku · Atome · Indodana.**

*One corroborating signal: a 2026 Play review complains that after topping up OVO the system would not let them change payment method — so **OVO is live today**, which is useful because it dates at least one rail past the 2020 inventory.*

### Section 5. Payment issues

| Date | Rating | Issue | Source |
|---|---|---|---|
| **2026-06-22** | 1★ | **Two different cards declined; both work on other apps** | Apple RSS, Indonesian storefront |
| **2026-06-03** | 3★ | Checkout failed twice; voucher and gift-with-purchase lost; promo amount changed between views | Apple RSS |
| **2026-09-10** | 1★ | Money held on a sold-out item, no refund request path, bot-only CS | Apple RSS |
| undated | — | OVO topped up, then payment method could not be changed | Google Play |
| undated | — | Partial cancellation refunded manually by email | Google Play |
| **2026-07-30** | 5★ | *"metode pembayaran nya pun mudah"* — counterpoint | Apple RSS |

> **Pattern → opportunity.** The card decline is the one that matters: **two cards failing on Sociolla while working elsewhere points at acquirer or auth routing, not at the shopper.** With a single card gateway and an in-house layer above it, there is no second rail for a declined card to fall to. The voucher-lost-on-failed-checkout complaint is the same event seen from the promo engine's side.

### Source Notes
- ✅ **`payments-api.sociolla.com` verified by me** in the 2026-06-08 Wayback capture, alongside `carts-api`, `orders-api`, `shipping-api`, `catalog-api1–5`, `soco-api`, `bj-public-api` and `sso-broker`. This is the basis of the In-house classification.
- ✅ **Midtrans confirmed from Sociolla's own page source** — `api.midtrans.com/v2/token` plus the tokenisation JS. 📌 Note the sloppiness worth knowing about: the **sandbox** JS (`api.sandbox.midtrans.com`) shipped on a production page next to the **production** token endpoint.
- ✅ **PT Social Bella Indonesia** confirmed verbatim in their own Indonesian T&C and site footer, with the Jakarta Barat address.
- ✅ **App review quotes pulled from the Apple RSS customer-reviews API** for the Indonesian storefront — dated and specific, not scraped summaries.
- ⚠️ **The live site, `soco.id` and `payments-api.sociolla.com` all return 403** (CloudFront/WAF). **Their Zendesk does not exist** — `sociolla.zendesk.com`, `socialbella.zendesk.com` and `soco.zendesk.com` all 404 on the help-centre API, and `help.sociolla.com` does not resolve. **That route is dead; do not retry it on this account.**
- ⚠️ **Entity ambiguity unresolved:** ecdb names **PT Sociolla Ritel Indonesia** as the sociolla.com operator, which differs from the PT Social Bella Indonesia on the T&C. A Singapore holdco is also referenced. **Verify before any contract-stage conversation.**
- ❌ **ecdb's US$6m 2025 revenue is rejected as implausible** for a 150-store retailer valued near US$600m. Not used in any derivation.
- ⚠️ **Total raised is contested** — Dealroom gives a $100–500m band; other sources say $220m or $226m. **Do not quote a single number.** Temasek, East Ventures, Jungle Ventures and L Catterton as investors are corroborated.
- ⚠️ **General Atlantic deal specifics** beyond "General Atlantic, 54%, Indonesia, 23 Dec 2025" are search-summary only — the ~$250m value, the secondary/primary split, the Pavilion and L Catterton exits and the ~$595m valuation all `[UNVERIFIED]`. Primary sources are paywalled or removed.
- ❌ **Vietnam payment methods: nothing established.** The Indonesian-rail routes on `vn.sociolla.com` are a strong 2022 lead, not a 2026 conclusion.

### Manual Research Recommendations
> **1. Settle QRIS.** Does Sociolla run QRIS end-to-end across web, app and 150 stores, and who acquires it? This one answer swings the pitch and a +3 ICP row. Nothing public can answer it.
> **2. Confirm whether Vietnam still runs Indonesian rails.** If it does, that is the opening line.
> **3. Confirm Midtrans is still the gateway in 2026.** Last direct evidence is 2019 page source; last indirect is a 2022 route.
> **4. Establish whether the email-proof-of-payment bank transfer flow still runs.** A 2026 review mentioning "2 days payment confirmation" suggests it might.
> **5. Resolve the contracting entity** — PT Social Bella Indonesia vs PT Sociolla Ritel Indonesia vs the Singapore holdco.

---

## Executive Summary

Sociolla is Indonesia's largest beauty retailer — **150 stores, the SOCO app with 1M+ downloads, sociolla.com and a Vietnamese storefront** — majority-acquired by **General Atlantic in December 2025** and targeting 500 stores across ASEAN. It runs an **in-house payments layer**, `payments-api.sociolla.com`, verified as a live distinct microservice in June 2026, sitting over **Midtrans**, a **direct BCA KlikPay integration** with its own five-route callback set, **Kredivo** and **Vospay**. The motion is therefore **In-house**, and the pitch is reach and opportunity cost rather than the case for orchestration itself. The sharpest evidence is a dated 2026 app review reporting **two different cards declining on Sociolla while working on other apps** — a single-acquirer failure mode with no second rail to fall to. **Two things are genuinely unknowable from outside and both matter: whether QRIS runs end-to-end, and whether Vietnam is still running Indonesian payment rails.** Either answer materially changes the account, and the score of 13/29 reflects that uncertainty honestly rather than guessing past it.

</details>
