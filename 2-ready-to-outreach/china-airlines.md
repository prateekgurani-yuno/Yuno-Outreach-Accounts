# China Airlines

**Status:** 🟢 Ready to outreach — 12-touch sequence drafted
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

### Pain Vector Extraction

```
=== PAIN VECTOR EXTRACTION ===

Motion: Greenfield — BUT SEE THE CAVEAT IN SECTION 3. This is the weakest orchestration
        call in the repo: mostly an absence of search hits, with the Oct 2023 no-failover
        outage as the only behavioural corroboration. The sequence is written so that it
        NEVER asserts "you have no orchestration layer" — every observation is about
        observed behaviour, not about inferred architecture. If the greenfield call turns
        out to be wrong, nothing in these emails becomes false.

*** DISAMBIGUATION — GET THIS RIGHT OR THE THREAD IS DEAD ***
China Airlines is TAIWANESE. Taipei/Taoyuan, TWSE 2610. It is NOT Air China, NOT China
Eastern, NOT China Southern. Every reference in the sequence must be unmistakably to the
Taiwanese carrier.

Observable setup facts (verified first-hand, 2026-09-18):
- OCT 2023: Mastercard authorisation failed on china-airlines.com for roughly 4–5 days
  while Visa kept working. CI's own stated cause on 20 Oct: they updated their 3-D Secure
  protocol and 「mastercard沒有更新到」. CS denied a problem on 18 Oct 「都沒人反應」, then
  acknowledged it on the 20th. The remedy customers were offered: pay by LINE Pay instead
  and forfeit their card rewards.
- NOT A ONE-OFF: auth-failure threads recur on PTT's aviation board across 2018, 2020,
  2023 and 2024. One is titled 「華航網站購票常信用卡授權失敗」 — 常 means frequently.
- METHOD SCOPING, from CI's own 2022 release: PayPal in nine NAMED markets; LINE Pay on
  Taiwan-departing flights and the eMall only, Taiwan-issued cards only; UnionPay, WeChat
  Pay and Alipay on mainland-China departures only.
- Estate: at least three booking front ends, a standalone refund portal, a separate
  e-shop domain, plus Tigerair Taiwan and Mandarin Airlines on their own sites.
- FY2025 consolidated revenue NT$209.09bn. Roughly a third is CARGO — invoiced B2B and
  largely outside a card checkout. This must be said out loud on any call.

Selected observations for Phase 1 (E1 bullets, ranked by materiality):
1. The no-failover pattern -> "In October 2023 Mastercard auth failed on your site for
   about five days while Visa kept working, and the fix offered to customers was to pay
   another way. Similar reports show up on PTT in 2018, 2020 and 2024 too."
   MATERIALITY: highest. Verified from a fetched customer thread including CI's own
   stated cause. The 2018/2020/2024 recurrence is what makes a 2023 event current rather
   than stale — WITHOUT IT THIS BULLET IS THREE YEARS OLD AND SHOULD NOT BE SENT.
2. Per-market method scoping -> "PayPal is live in nine named markets, LINE Pay only on
   Taiwan-departing flights, and UnionPay, WeChat Pay and Alipay only on mainland-China
   departures."
   MATERIALITY: high, and it is their own announcement. Every method scoped to a route
   or a market rather than available to a customer.

   HELD AT 2. The multi-front-end estate is saved for LK4; the cargo caveat and the
   group-carrier question go to the manual touches.

Bridge variant: C — friction
Rationale: NOT A — I cannot evidence multi-PSP complexity because I cannot name a single
PSP. NOT B — "single visible PSP" requires a visible PSP and there is none. The
observations are real customer-facing friction that does not cleanly map to either
structural story, which is precisely what C exists for.

Hypothesis for Phase 2 (E3):
Methods look like they were added per market and per route rather than per customer, and
there is no visible fallback when one path degrades — so a single-point failure becomes a
customer-facing outage and the only remedy on offer is manual.
Backing logic: one scheme's 3DS mismatch took card acceptance down for days while the
other scheme was unaffected, which is what a stack without an alternate path looks like
from the outside. The remedy CI offered — pay by LINE Pay and lose your card rewards —
was a customer-executed workaround, not a system one. And the same complaint recurs
across four separate years.

Success case for Phase 3 (E4):
Selected case: Wingo
Tier: 1 — airline, AND the mechanism matches the hypothesis exactly. Yuno's own wording
      for Wingo is "automatic retries of failed payments through multiple providers",
      which is the direct answer to a single-path failure. This is the rare case where
      the industry match and the pattern match are the same case.
Numbers to lead with: +14% approval rate (stated as initial implementation phase) ·
1,000+ payment methods through one integration · 3DS and fraud tooling in the same layer
The 3DS bullet is deliberately third and deliberately included — CI's 2023 outage was
caused by a 3DS protocol update.
Plus one line naming Qatar Airways, Copa Airlines and Avianca — NO NUMBERS, ever.
Optional benchmark: SKIP. The "~8% average authorisation uplift" is Yuno's own blog
figure, and the IATA/EDC $20.3bn figure is untraced to primary source per our own skill
file.

Touch-by-touch angles:
- E2 angle: the no-failover pattern -> ONE mechanism: automatic failover to an alternate
  path when a provider or a scheme route degrades, so recovery is systemic not manual
- LK1 angle: the Oct 2023 five-day single-scheme failure, one sentence
- LK2 angle: methods per market and per route, with no visible fallback
- LK3 angle: Wingo — automatic retries across multiple providers, +14%
- LK4 angle: FRESH — three booking front ends, a standalone refund portal, a separate
  e-shop domain, and two subsidiary carriers on their own sites
- E8 angle: clean exit, offer to circle back

*** THINGS THIS SEQUENCE MUST NEVER CLAIM ***
- That CI lacks card instalments (分期). UNCHECKED, not sourced-absent. Instalments are
  the dominant mechanic for high-ticket travel in Taiwan and being wrong about it would
  be humiliating. It appears ONCE, as the embedded discovery question in E3.
- That CI lacks 超商代收 (convenience-store cash) or ATM transfer. Same reason.
- That CI lacks Apple Pay or Google Pay. Unchecked.
- Any PSP or acquirer name. Zero were identified.
- That Tigerair and Mandarin run separate stacks. Strongly implied, not verified.
- Any USD conversion of NT$209.09bn taken from Taipei Times — their figure is off by
  roughly 10x. Use the NTD number or nothing.
```

**Calendar.** Day 1 anchored to **Monday 19 October 2026**, clearing **National Day
(Double Ten, 10 Oct)** and any substitute weekday around it, plus the Mid-Autumn period,
rather than threading between them.

> ⚠️ **Taiwanese public holidays are partly lunar-dated and I have not verified the 2026
> calendar.** No holiday is known to fall inside 19 Oct – 18 Nov, but **check the DGPA's
> published 2026 calendar before Touch 1 goes out.**

**Times are Taiwan time (UTC+8), which is IST+2:30.** Slots run 14:00–16:00 local, i.e.
11:30–13:30 IST.

---

### Phase 1 — Curiosity (Days 1–5)

#### Touch 1 — Email 1 · Day 1 · Mon 19 Oct

**Subject:** Single-scheme outage on your booking flow

```text
Hey {{recipient.first_name}},

Spent some time on China Airlines' payment setup. Two things stood out:

- In October 2023 Mastercard authorisation failed on your site for about five days while Visa kept working, and the fix offered to customers was to pay another way. Similar reports show up on PTT in 2018, 2020 and 2024 as well.
- PayPal is live in nine named markets, LINE Pay only on Taiwan-departing flights, and UnionPay, WeChat Pay and Alipay only on mainland-China departures.

That kind of setup usually has some friction worth checking on.

I work at Yuno — top-100 fintech, a16z-backed. We consider ourselves the 'everything payments' platform: one integration, every PSP, every method, every market.

Rather than pitch you based on assumptions, is there anything payment-related you're working through that we might be able to help with?

Best,
Prateek
```

#### Touch 2 — Email 2 · Day 3 · Wed 21 Oct · REPLY IN THREAD

```text
Hey {{recipient.first_name}},

Following up — wanted to put a bit more behind what Yuno actually does, and how it would address what I flagged.

- We sit above your existing providers. Additive, nothing gets ripped out.
- When a provider or a scheme route starts degrading, traffic moves to an alternate path automatically rather than waiting on a fix.
- Routing is per BIN, market and method, so one scheme's behaviour doesn't decide whether the checkout works.
- One integration to add a PSP, an acquirer, a rail or a method.

On the 2023 event specifically — the interesting part isn't that a 3DS update went out of step, that happens to everyone. It's that there was no second path for the traffic to take while it was fixed, so the recovery had to be the customer changing payment method.

I'll keep sharing what I'm seeing every few days. If your stack's where you want it, just say the word and I'll back off — otherwise happy to go deeper.

Cheers,
Prateek
```

#### Touch 3 — LinkedIn message 1 · Day 5 · Fri 23 Oct

```text
Hey {{recipient.first_name}} — figured I'd flag this here too in case more useful than email. Quick one: in Oct 2023 Mastercard auth was down on china-airlines.com for about five days while Visa was fine, and the remedy offered was to pay by another method. Curious if that maps to anything you're working through on the payments side.
```

---

### Phase 2 — Diagnosis (Days 7–9)

#### Touch 4 — Email 3 · Day 7 · Tue 27 Oct · NEW EMAIL

**Subject:** Read on your failover path

```text
Hey {{recipient.first_name}},

Going to take a swing at this — based on what I see, my read is that methods were added per market and per route rather than per customer, and that there's no visible fallback when one path degrades.

The 2023 event is the clearest signal. One scheme's 3DS mismatch took card acceptance down for days while the other scheme was unaffected, and the remedy on offer was a customer-executed workaround rather than a system one. The same complaint then recurs across four separate years.

None of that reads as anyone doing it badly — it reads as a stack with one path per method.

At Yuno (a16z-backed, top-100 fintech), we sit above your existing PSPs so traffic can move when a path degrades — keep your stack, add what's missing.

One thing I genuinely don't know and couldn't establish from outside: does your own checkout offer 分期付款, or do customers get instalments only through their issuing bank?

Thursday is open for me — would 15:00 or 16:00 your time work for a quick 15 minutes?

Best,
Prateek
```

#### Touch 5 — LinkedIn message 2 · Day 9 · Thu 29 Oct

```text
Hey {{recipient.first_name}} — sent a longer note over email this week. Short version: the methods look scoped per market and per route, with no visible fallback when one path degrades. If that's anywhere on your radar, would Monday the 2nd at 14:00 your time work for a quick 15?
```

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · Mon 2 Nov · NEW EMAIL

**Subject:** How Wingo solved this

```text
Hey {{recipient.first_name}},

On the read I shared last week — sharing an example of what solved looks like. Wingo is a Colombian low-cost carrier, so a different region and a smaller operation, but the mechanism is the one that matters here.

They put Yuno above their existing providers:

- +14% approval rate, from the initial implementation phase alone (pretty solid, right?)
- Automatic retries of failed payments through multiple providers, rather than a customer-executed workaround
- 1,000+ payment methods and 3DS handled in the same layer

That last point is the one I'd underline given 2023 — when 3DS sits in the routing layer rather than per-provider, a protocol mismatch on one scheme stops being a site-wide event.

Same orchestration layer above their existing stack — no rip-out. Qatar Airways, Copa Airlines and Avianca run on the same layer.

Wednesday the 4th is open — would 15:30 your time work?

Full case here if useful: https://y.uno/en/newsroom/wingo-improves-payment-efficiency-with-yuno-as-strategic-partner

Thanks,
Prateek
```

#### Touch 7 — Email 5 · Day 13 · Wed 4 Nov · ⚠️ MANUAL

> **Placeholder — Prateek writes this one.**
>
> **Suggested angle:** the honest scoping map. Take CI's own 2022 release and lay out which
> method is available on which departure — PayPal in nine named markets, LINE Pay Taiwan-departing
> only and Taiwan-issued cards only, UnionPay/WeChat/Alipay mainland-departing only — against
> their route map. **Entirely their own published material.** ⚠️ **Leave the unchecked rails
> (分期, 超商代收, ATM transfer, Apple Pay, Google Pay) off the map entirely rather than
> marking them absent.**

#### Touch 8 — Email 6 · Day 15 · Fri 6 Nov · ⚠️ MANUAL

> **Placeholder — different format from E5.**
>
> **Suggested angle:** the cargo honesty move. Roughly a third of CI's revenue is freight,
> invoiced B2B and largely outside a card checkout. **Saying that out loud, unprompted, before
> they have to** is the single most credibility-building thing available on this account — it
> shows we read the results rather than the headline revenue number. Then scope the
> conversation to the passenger and eMall side deliberately.

#### Touch 9 — LinkedIn message 3 · Day 17 · Tue 10 Nov

```text
Hey {{recipient.first_name}} — Wingo got +14% approval by retrying failed payments automatically across multiple providers, instead of asking the customer to switch method. Worth 15 minutes to see if it maps to your setup? Thursday the 12th at 14:30 your time is open.
```

---

### Between Phases (Day 19)

#### Touch 10 — Email 7 · Day 19 · Thu 12 Nov · ⚠️ MANUAL

> **Placeholder — manual creative bridge.**
>
> **Freshest unused anchor:** the group question. CI, **Tigerair Taiwan** and **Mandarin
> Airlines** each run their own domain and their own FAQ. ⚠️ **Ask whether the payment stacks
> are shared — do not assert that they aren't.** Separate stacks are strongly implied and
> completely unverified, and asserting it invites a one-word correction.

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21 · Mon 16 Nov

```text
Hey {{recipient.first_name}} — last LK ping from me on this. One thing I kept running into: there are at least three separate booking front ends on china-airlines.com plus a standalone refund portal. If timing works, Wednesday the 18th at 16:00 your time is open for a quick 15.
```

#### Touch 12 — Email 8 · Day 23 · Wed 18 Nov · REPLY IN THREAD to E3

```text
Hey {{recipient.first_name}},

Going to stop pinging unless you want to pick this back up.

Entirely possible payments isn't where the attention is right now, and that's fair. If timing's just off, happy to circle back next quarter.

If it ever comes back up, just reply here — and if payments sits with someone else, happy to be pointed there.

All the best,
Prateek
```

---

### ⚠️ Send-time checklist — six things before Touch 1 goes out

1. ⛔ **China Airlines is TAIWANESE.** Not Air China, not China Eastern, not China Southern.
   Check every reference and check the recipient's own title and entity.
2. ⛔ **Never claim they lack instalments, 超商代收, ATM transfer, Apple Pay or Google Pay.**
   All unchecked. Instalments appear exactly once, as a question, in E3.
3. ⛔ **Never assert "you have no orchestration layer."** The greenfield call here is the
   weakest in the repo. Every observation in this sequence is about observed behaviour, so
   none of it breaks if the call is wrong.
4. ⛔ **Never name a PSP or acquirer.** Zero were identified.
5. ⚠️ **The 2018/2020/2024 recurrence is load-bearing.** Without it the opener is a
   three-year-old incident. **Re-check the PTT threads are still reachable before send.**
6. ⚠️ **Verify the 2026 Taiwanese public holiday calendar.** Partly lunar-dated, unverified.

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
