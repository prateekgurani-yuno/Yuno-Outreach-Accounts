# Moshtix

**Status:** 🟠 **BLOCKED — research complete, outreach withheld pending a rules-of-engagement decision.** See the blocker below.
**ICP Score:** 12 / 29 → 🟢 **Qualified** (score alone would clear the ≥10 threshold; the blocker, not the score, is why no sequence was generated)
**Industry:** Live-music and festival ticketing (agent-of-promoter; collects from buyers, settles to promoters) · **HQ:** Sydney, Australia — **Moshtix Pty Ltd, ABN 72 076 980 955** · **Researched:** 2026-09-19 · **First email sent:** —
**Motion:** **In-house** — Moshtix has built its own gateway router. Card traffic is switched between **three** gateways by a per-event flag, in hand-rolled jQuery. Respect the build; anchor on opportunity cost and reach, never "you need orchestration."

---

> ## ⛔ BLOCKER — THE STUB'S PREMISE IS WRONG. **Moshtix is not TEG. It is Ticketmaster / Live Nation.**
>
> `accounts/apac-tal.csv` line 174 says *"owned by TEG"* and *"Part of TEG"*. **Both are refuted.**
>
> **Verified first-hand on Moshtix's own B2B site**, `https://business.moshtix.com/our-story`, 2026-09-19 — Moshtix describes itself as working alongside *"global market leaders: **Ticketmaster, Live Nation Concerts, and Live Nation Media & Sponsorship**"*, and `business.moshtix.com` serves a logo file literally named:
>
> ```
> Moshtix-a-Ticketmaster-Comany-ReverseLogo.png
> ```
>
> (Ticketmaster's own typo, not mine.) Corroborated by Live Nation's Feb-2019 announcement at `/2019/02/ticketmaster-acquires-moshtix` — the route resolves, though the page body is JS-rendered and did not extract — and by Moshtix's buyer T&Cs, which name *"Moshtix Pty Ltd … **and Ticketmaster NZ Ltd** incorporating Moshtix.co.nz."*
>
> ### Why this blocks outreach rather than just correcting a field
> Moshtix Pty Ltd is Australian-incorporated and AU+NZ-only, so it is **in territory** and it is **not a PSP** — no Phase 0 gate fires. But a payments decision at a **Live Nation subsidiary** is almost certainly a global-account decision, not an APAC SDR one. **Whether Live Nation-owned subsidiaries are approachable at all — versus routing to a global-account or partnerships motion — is a rules-of-engagement call above this research.**
>
> **I have not generated a sequence and have not pulled a replacement.** The research is banked and the file is complete; the decision is Prateek's. This is the same posture as Viu (blocked pending the Adyen decision) — deliberately parked, not abandoned.
>
> **Also corrected:** the Ticketek comparison in the stub's framing is not a sibling comparison. It is a comparison against **a competitor's parent**.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Moshtix is an Australian live-music and festival ticketing platform, founded 2003, **owned by Ticketmaster (Live Nation) since February 2019**. It operates in **Australia and New Zealand only**. Its payment layer is genuinely interesting: **three card gateways behind a hand-built per-event switch**, with **merchant of record varying by event**, and dead Masterpass, Zip and LatitudePay integrations still shipping in the production bundle.

> ⚠️ **No SimilarWeb data was supplied** and none was obtained. Market weighting is from Moshtix's own published figures and its two-country entity structure.

### Volume — **clears the gate, but derived, with a tight floor**
Moshtix's own published figures, **re-verified verbatim by me** at `https://business.moshtix.com/our-story`:
> *"1 million fans and growing · **110,240 events delivered** and counting · **1,785,600 tickets scanned per year**"*

Bluesfest case study: **100k+ tickets sold in 2022**, against 69.6k general-entry tickets scanned — i.e. **scanned ≈ 70% of sold**.

| Construction | Result |
|---|---|
| 1,785,600 scanned/yr | 148,800 scanned/month |
| Grossed up at the observed 70% scanned:sold ratio | **~2.5M sold/yr ≈ 210k tickets/month** |
| At 2–2.5 tickets/order (typical live-music basket) | **~85,000–105,000 transactions/month** |
| **Pessimistic floor** — treat scanned as sold *and* assume 3.5 tickets/order | **~42,500/month** |

**Verdict: PASS on every assumption I can justify — but the floor case clears by only ~6%.** ⚠️ **Derived, not sourced.** Moshtix publishes no order count. Third-party revenue figures (Growjo ~$5.3M, Owler ~$8.2M) are scraper estimates and **must not go in an email.**

### ⚡ Three card gateways behind a hand-built switch — the technical core
**Verified first-hand by me, 2026-09-19.** `cdn.moshtix.com.au` is un-WAF'd and serves the booking bundle in plain JS with comments intact (HTTP 200, 260,019 bytes):

```
https://cdn.moshtix.com.au/v2/bundles/book/js/scripts?v=M8293k-p0onNSRJnAJGk52aiWS0Kk9RpaBA7xNuXf6Q1
```

**The switch** — `isStripeBooking` · `isCommWebMpgsBooking` · `isFatZebraBooking`

**Eleven per-method handlers**, all confirmed present: `moshtixStripeHandler` · `moshtixCommWebMpgsHandler` · `moshtixFatZebraHandler` · `moshtixPayPalHandler` · `moshtixAfterpayHandler` · `moshtixZipPayHandler` · `moshtixMasterPassHandler` · `moshtixFZMasterPassHandler` · `moshtixFZVisaCheckoutHandler` · `moshtixPayByInstalmentHandler` · `moshtixNoPaymentHandler`

| Gateway | Evidence | Read |
|---|---|---|
| **Stripe** | Payment Element + Payment Intents + Setup Intents, 3DS2, `blocked_card_brands_beta_2`, **`isMotoEnabled`** (call-centre/box-office card entry) | Likely the wallet surface too — **inferred, not proven** |
| **CommWeb / MPGS** | `commWebMpgsSessionId` (×4), hosted-session tokenisation | **Commonwealth Bank of Australia's** gateway on Mastercard Payment Gateway Services — a named **bank acquirer** relationship |
| **Fat Zebra** | `gethostedpaymentpage`, completion by `postMessage` from a `https://paynow*` origin | Hosted page at `paynow.pmnts.io`. Also carries Visa Checkout and Masterpass |

**Why three?** Because **merchant of record varies by event.** The checkout says so to the buyer verbatim:
> *"By choosing this payment method, you are paying **the Event Organiser** directly, as they are the merchant for this payment type for this Event. **The Event Organiser's** name will appear on your statement."*

And the promoter agreement clause 12.1 codifies it:
> *"MOSHTIX collects all payments … using the MOSHTIX merchant facility, **unless Moshtix gives written permission to the PROMOTER to establish and use their own merchant facility.**"*

**That is a split-MoR, multi-gateway routing problem maintained in hand-rolled jQuery.** It is precisely the Yuno conversation — if the account clears the ownership blocker.

### Accepted methods (Australia)
First-party: *"Sitewide Moshtix accepts: • VISA • MasterCard • American Express\* • ApplePay\* • GooglePay\* • PayPal\* • PayPal Pay in 4\* • Afterpay\* • Moshtix Gift Voucher\* (\*Selected events only)"*

| Method | Status | Detail |
|---|---|---|
| Visa / Mastercard / Amex | **CONFIRMED** | `data-supported-cardtypes='["Amex","Visa","MasterCard"]'`; Amex event-discretionary |
| Apple Pay / Google Pay | **CONFIRMED** | Mechanism (Stripe) inferred, not proven |
| PayPal + PayPal Pay in 4 | **CONFIRMED** | AUD $30–$2,000, no split above $2,000 |
| Afterpay | **CONFIRMED** | AU+NZ, **$50–$4,000**, excluded on Ticket Requests, organiser-discretionary |
| **BECS direct debit** | **CONFIRMED, undocumented in the FAQ** | The native instalment product collects `#pay-by-instalment-direct-debit-bsb`, `-account-number`, `-account-name` |
| 3DS | **CONFIRMED** | `supports-3d-secure=true`; Stripe path is 3DS2 with an **MOTO exemption toggle** |
| Gift vouchers | **Redeemable, WITHDRAWN from sale** | *"Gift Vouchers are no longer for sale through Moshtix"* |
| **Zip** | **SOURCED ABSENCE — DISCONTINUED** | *"Moving forward, Zip Pay will no longer be a payment option."* Legacy `moshtixZipPayHandler`, Zip fonts and `booking-icon-zip-pay.png` **still shipping** |
| **LatitudePay** | **SOURCED ABSENCE — DISCONTINUED** | Was Moshtix's BNPL for Bluesfest 2022 (*"+14% AOV vs other payment methods, $500+ average order"*). The Control Room's "Sales By Payment Type" report **still defaults to "LatitudePay / GenoaPay"** |
| **Masterpass** | Dead scheme, **still loaded** | `MasterPass.client.js` — Mastercard retired it |
| Klarna · humm · POLi · PayID / PayTo · BPAY | **NOT FOUND — sourced absence** | Absent from the sitewide list and from 225 help articles, the checkout DOM and the booking bundle. (All "poli" hits were "policy" — the existing false-positive class held.) |
| Cash + card at box office | **CONFIRMED** | Box Office dashboard splits funds by Cash and Card |

**Fees:** no public surcharge schedule. But the promoter agreement states the booking fee **bundles the acquiring cost** — *"Moshtix sets a booking fee per ticket that includes Moshtix fee **and a credit card processing fee**."* **That is the commercial hook: card cost is buried inside the booking fee, so every basis point of MDR is Moshtix's margin, not the promoter's.**

### The promoter payout leg
- **Pull-based, post-event.** Event auto-flips to "Ready for Settlement"; the promoter must log into **Control Room** and lodge a settlement request. **Processed Mondays, Wednesdays and Fridays before 12pm; funds clear 1–3 business days after.**
- **Contractual term: EFT within 7 business days** of bank details being received (clause 12.3). PayPal-collected funds settle **only at successful event completion** (12.1).
- **Moshtix floats 100% of ticket proceeds from on-sale to event completion** — often 6–12 months on festivals.
- **Chargeback reserve, explicit:** *"moshtix reserves the right to hold a **CHARGE BACK RESERVE of up to 20% of Total Internet & Phone ticket proceeds including GST, held in trust for 90 days** past the successful event completion date. For events that are **cancelled, disrupted or otherwise considered unsuccessfully delivered, MOSHTIX reserves the right to hold 100% in reserve … held in trust for 270 days.**"*
- **Chargeback liability sits with the promoter** where a refund was refused.
- **⚠️ Manual refund fallback:** where the auto-refund to original payment method errors, Moshtix collects the buyer's BSB/account (or IBAN/SWIFT for international cards) and pays by **manual bank transfer, "allow up to 4 weeks."** **That is a real operational tell of refund-rail failure at volume.**

### ⚡ Not the same stack as Ticketek — zero overlap
| | **Ticketek (TEG)** | **Moshtix** |
|---|---|---|
| Parent | TEG (Silver Lake) | **Ticketmaster / Live Nation** |
| CDN | Akamai | **Fastly — `ticketmaster9.map.fastly.net`** |
| Engine | Softix | In-house ASP.NET MVC ("Control Room") |
| Payment host | `pay.ticketek.com.au` (Softix PayGate) | **No `pay.` host — NXDOMAIN.** Inline in `/v2/book/` |
| Bot defence | Akamai WAF | **Ticketmaster EPS** (`/eps-mgr`, `tm-bl: 1` header) |
| RUM | **Dynatrace** | **None** — GTM + Braze |
| Gateways | Softix PayGate | **Stripe + CommWeb MPGS + Fat Zebra** |
| Queueing | — | **Queue-it** |

**No Softix, no PayGate, no `pay.` subdomain, no Dynatrace, different CDN, different bot vendor, different gateways.** The Cathay/HK Express precedent holds — and here it is cleaner, because the parents differ too.

**⚠️ Also corrected:** the Silver Lake / TEG date commonly cited as 2022 is wrong — Silver Lake acquired TEG in **2019**. KKR and Temasek appear later (2023–24) as **lenders** in a dividend recapitalisation, not owners. `[UNVERIFIED — search summary only; deprioritised once TEG ceased to be load-bearing.]`

</details>

<details>
<summary><h2>✉️ Section 2 — Full Outreach Sequence</h2></summary>

*Not generated — **deliberately withheld**, pending the ownership / rules-of-engagement decision in the blocker above. Do not run `/full-outreach` until that is settled.*

If it clears, the pitch is unusually well-evidenced and writes itself: **three card gateways behind a hand-rolled `isStripeBooking / isCommWebMpgsBooking / isFatZebraBooking` switch, split merchant-of-record by event, card cost buried inside the booking fee, a 20%/90-day chargeback trust reserve, thrice-weekly manual settlement runs, a manual bank-transfer refund fallback that takes four weeks, and dead Masterpass, Zip and LatitudePay integrations still shipping in production.** Every one is verifiable from a public URL in this file.

</details>

<details>
<summary><h2>🔬 Section 3 — Full Research</h2></summary>

## Verification note
**Re-fetched and verified first-hand by me, 2026-09-19:** the booking bundle (260,019 bytes) and every handler, gateway-switch and orchestrator grep; `business.moshtix.com` and `/our-story` for the ownership statement, the logo filename and the volume figures. The Wayback-archived checkout DOM, the two Zendesk corpora and the promoter agreement were verified by the research agent; **a Wayback fetch of the buyer T&Cs failed on my retry** (connection reset through the proxy) so the entity-naming quote is agent-sourced, not re-verified by me.

## Zendesk technique — worked twice
`moshtix.zendesk.com` is a **decoy** (0 articles). The live ones:
- **Consumer:** `https://moshtix-au.zendesk.com/api/v2/help_center/en-au/articles.json?per_page=100` → **126 articles** (note the `en-au` locale; `/locales.json` reveals it)
- **Promoter/B2B:** `https://clientsupport.moshtix.com/api/v2/help_center/en-us/articles.json?per_page=100` → **99 articles** — **this one holds the settlement and payout mechanics**

> **Technique note for the running list:** when the obvious `{brand}.zendesk.com` returns zero articles, it is a decoy, not a dead end. Check `/locales.json` for the right locale and look for a separate B2B desk. The B2B desk is consistently the richer corpus.

## Orchestration — none, on affirmative evidence
Zero hits for **Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY, Yuno, Adyen, Braintree** across the booking bundle — **swept by me directly.** Also not found anywhere (checkout DOM, 225 help articles, T&Cs, promoter agreement): Worldpay, Cybersource, Checkout.com, eWAY, Windcave, Tyro, Pin Payments, Till, Global Payments, Fiserv, NAB, Westpac, Softix.

**Classification: home-grown orchestration**, and unusually this rests on **affirmative evidence, not absent hits** — the three-way switch with eleven per-method handlers *is* a hand-built routing layer, sitting in a jQuery bundle alongside a dead Masterpass integration, a dead Zip integration and a dead LatitudePay report default.

⚠️ **Absence of Braintree is mildly surprising given PayPal**, and was not disproved server-side.

## Complaints — fetched and read directly
`https://www.productreview.com.au/listings/moshtix` — **1.2 / 5 from 199 reviews, 96% negative.**

- **Processing failures:** *"Trying to buy tickets and your processing payment is just spinning. I tried waiting 15 minutes, multiple sites…"*
- **Double charges:** *"DOUBLE CHECK YOUR PURCHASE. I was charged twice because of a site error while purchasing through moshtix and they have refused to refund me any money… if you receive an error message while purchasing through moshtix, wait a few minutes and double check your bank account before retrying, because they may charge you twice."*
- **Refund friction:** cancelled-show rebooking failures; Booking Protect (third-party refund-protection partner) demanding extensive documentation.

**The double-charge-on-error pattern is consistent with a hosted-payment-page / redirect flow lacking idempotent order reconciliation — which is exactly what `api/booking/rollBackOrder` in the bundle exists to paper over.** Reddit and the app stores were **not checked** (budget).

## Corporate
**Ownership chain:** founded 2003 → News Corp / News Digital Media 2007 → management buyout 2013 (Harley Evans + Vanessa Bond) → **Ticketmaster (Live Nation Entertainment) Feb 2019 → present.** `[Pre-2019 steps: search-summary grade — treat 2007/2013 as indicative. The 2019 step is verified.]`

**Entities:** **Moshtix Pty Ltd, ABN 72 076 980 955**, PO Box 1272 Darlinghurst NSW 1300 · **Ticketmaster NZ Ltd** (moshtix.co.nz).

**Portals:** `admin.moshtix.com/v2/clientlogin` (CloudFront, `X-Frame-Options: DENY`) · `control-room.moshtix.com/register` · `business.moshtix.com` (Squarespace + Braze) · `clientsupport.moshtix.com` (Zendesk) · `queue.moshtix.com.au` (Queue-it) · `my.moshtix.com.au` (Cloudflare). `promoter.moshtix.com.au` does not exist. `secure.staging.moshtix.com.au` and `*.pretzel.moshtix.com.au` appear in certificate transparency.

## 4. ICP Score breakdown — 12 / 29

| Signal | Weight | Score | Basis |
|---|---|---|---|
| Transaction volume | 5 | **5** | ~85k–105k/month derived; floor ~42.5k. ⚠️ derived, not sourced |
| Orchestration | 4 | **1** | **In-house** — hand-built three-way gateway router, on affirmative evidence |
| 3+ countries | 3 | **0** | **AU + NZ only — two markets** |
| Multiple PSPs | 2 | **2** | Stripe + CommWeb/MPGS + Fat Zebra + PayPal + Afterpay |
| Local rail gap | 3 | **2** | PayTo, BPAY, PayID, POLi all sourced-absent; Zip and LatitudePay discontinued. Partial — wallets, PayPal and Afterpay are all present |
| Recent expansion | 2 | **0** | None found |
| Payment issues | 2 | **2** | ProductReview 1.2/5; double charges; spinning payments; 4-week manual refund fallback |
| Funding | 2 | **0** | Live Nation subsidiary — no funding events |
| Traffic outside home market | 2 | **0** | AU + NZ only |
| Competitor orchestration | 2 | **0** | Ticketek runs Softix PayGate in-house; no third-party orchestrator in the category |
| Job postings | 2 | **0** | Not established |
| **TOTAL** | **29** | **12** | 🟢 **Qualified on score — but BLOCKED on ownership** |

**The score is capped by geography, not by opportunity.** A two-market business loses 5 points it can never earn (3+ countries, traffic outside home), and the in-house build costs 3 more against greenfield. **The payment complexity is genuinely high for a 12/29 account** — which is worth remembering if the ownership question resolves favourably.

## 5. What could NOT be established
1. **Which gateway carries the majority of volume.** The three-way switch is proven; the split is not. No `pk_live_…` was exposed — `stripePublicKey` is injected server-side.
2. **The acquirer behind Stripe and Fat Zebra**, and whether CommWeb is Moshtix's own CBA facility or a promoter-owned one. The per-event MoR flag makes the second reading plausible.
3. **Any published surcharge schedule** — genuinely not published; fees are per-event, set at build time in Control Room.
4. **Whether Apple Pay / Google Pay render via Stripe** — strongly implied, not proven.
5. **⚠️ Whether Moshtix and Ticketmaster AU share a payment stack.** Shared CDN and bot-defence are proven; `ticketmaster.com.au`'s gateways were **not examined**, so a Ticketmaster-side consolidation programme can be neither ruled in nor out. **This is the real question for any follow-up — it would kill or make an orchestration pitch**, and it compounds the ownership blocker.
6. Reddit / App Store / Google Play complaint channels.

## 6. Overall Research Confidence — **HIGH on the payment stack, MEDIUM on the account's viability**

The technical findings are the strongest in this batch: the gateway switch, all eleven handlers and the orchestrator absence were **grepped first-hand from a live, un-minified, un-WAF'd production bundle.** Ownership was confirmed from Moshtix's own site.

**Viability is the uncertainty, not the facts** — see the blocker.

</details>
