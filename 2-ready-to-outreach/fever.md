# Fever

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 16 / 29 → 🟢 **Medium**
**Industry:** Live-entertainment discovery & ticketing marketplace (Candlelight, immersive experiences) · **HQ:** ⚠️ **Fever Labs Inc., Delaware / New York** — *not Madrid* · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** ⚠️ **COMPETITIVE — a global orchestrator is already in production.** Not greenfield. Read 3B before drafting a single line.

---

> ## ⛔ TWO CORRECTIONS TO THE STUB, BOTH OF WHICH WOULD EMBARRASS US IN EMAIL ONE
>
> **1. Fever is not Madrid-headquartered.** Their own Terms of Use, fetched and verified by me:
> > *"**Fever Labs Inc.** ("Fever") is a corporation duly organized and existing under the laws of the **State of Delaware**, United States of America, TAX ID 99-0368536, with offices at **50 Greene St 3 Fl, New York, NY 10013**, United States."*
>
> Madrid is the founding city and the largest engineering office, and it is a notice address — **but the contracting entity is Delaware/NY.** The stub and the target list both say "Madrid-based."
>
> **2. They already run payment orchestration.** See below. **Opening with anything resembling "you don't have a routing layer" ends the thread instantly.**

---

> ## 🎯 THE HOOK — they shipped Kakao and Naver login for Korea, and never shipped a Korean payment rail
>
> **Verified by me directly**, byte-for-byte identical on both `feverup.com/en/seoul` and `feverup.com/en/singapore`:
>
> ```json
> "gateways":{
>   "nuvei":{"payUEnvironment":"live","nuveiEnvironment":"prod"},
>   "paypal":{"debug":"false"},
>   "checkout":{"key":"pk_ypka55zhracx7kz5xggqow7o4e4"},
>   "googlePay":{"merchantId":"BCR2DN4TZSMIDPLF","environment":"PRODUCTION"},
>   "processOut":{"key":"proj_fPlZa4x4bP3fkC7A1jrKdDCZDILrLGA7","riskEnvironment":"PRODUCTION"}
> }
> "paymentMethods":[]
> ```
>
> **The same config is served to every APAC city.** No market-specific gateway, no market-specific method, and `paymentMethods` is an **empty array**.
>
> **Now the Korea part.** On the Seoul page I found **seven Kakao and seven Naver references — and every single one is OAuth authentication**: `kauth.kakao.com/oauth/authorize`, `kapi.kakao.com/v2/user/me`, `nid.naver.com/oauth2.0/authorize`, `openapi.naver.com/v1/nid/me`, with populated `WEBCLIENT_KAKAO_CLIENT_ID` and `WEBCLIENT_NAVER_CLIENT_ID` redirecting to `/oauth-callback`.
>
> **Occurrences of KakaoPay, Naver Pay, Toss Pay, PAYCO or Samsung Pay: ZERO.**
>
> **They localized the front door and never localized the till.** Korean-language product, Korean social login, Korean-won pricing — and a card-and-wallet-only checkout in a market where that is a known conversion killer. That observation is machine-verifiable from their own production page and cannot be argued with.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Fever is a live-entertainment discovery and ticketing marketplace best known for the **Candlelight** concert series, operating in 55 countries. It runs a genuine, substantial APAC business — **not** token stub pages.

**SimilarWeb total visits:** **Not obtained.** No data supplied. **Geography below is from live ticketed inventory counts and embedded currency codes on Fever's own city pages**, which is better evidence than an estimate.

### ✅ TERRITORY GATE — PASSES DECISIVELY
| City | Live ticketed events | Currency |
|---|---|---|
| Melbourne / Sydney | 133 / 132 | AUD |
| **Singapore** | **126** | SGD |
| Seoul | 62 | KRW |
| Auckland | 56 | NZD |
| New Delhi / Mumbai / Bengaluru | 54 / 40 / 22 | INR |
| Tokyo / Osaka | 52 / 49 | JPY |
| Hong Kong | 47 | HKD |
| Jakarta | 21 | IDR |
| Bangkok | 2 | THB — **near-stub** |

**Local-currency base pricing, not EUR shown in Asia.** APAC offices confirmed on their careers site (Melbourne, Singapore, Sydney, Seoul, Tokyo, Hong Kong), a live Korean hire, and `supportedLocales` including `ko-KR`, `ja-JP`, `zh-HK`. **India runs under a second brand** — `liveyourcity.com`, `"channel":"live-your-city-marketplace"`.

**Not present anywhere: Taipei, Manila, Kuala Lumpur, mainland China, Vietnam.** Dubai is excluded as EMEA.

### Known PSPs — all from the production config, verified by me
| Provider | Role |
|---|---|
| **ProcessOut** | ⚠️ **Orchestration layer, `riskEnvironment:"PRODUCTION"`** |
| **Nuvei** | PSP, `nuveiEnvironment:"prod"` |
| **Checkout.com** | PSP, public key `pk_ypka...` |
| **PayPal** | Wallet, `debug:"false"` |
| **Google Pay** | Wallet, merchant ID, `PRODUCTION` |
| **Forter** | Fraud, siteId `039249618c32` |
| Stripe | ⬜ Config block present but **`stripeWithPaymentRequest:false`**, no publishable key — **appears dormant** |

⚠️ **`payUEnvironment` sits INSIDE the `nuvei` object** — almost certainly a legacy field name in Nuvei's SDK. **Do not claim Fever uses PayU.**

### ❌ Absent in every APAC market — sourced from `paymentMethods:[]`
**PayNow · GrabPay (SG) · FPS · PayMe · AlipayHK (HK) · PayPay · konbini · LINE Pay · Rakuten Pay (JP) · KakaoPay · Naver Pay · Toss (KR) · UPI · net banking (IN) · QRIS · GoPay · OVO · DANA (ID) · PromptPay · TrueMoney (TH) · PayTo · BPAY · Afterpay · Zip (AU/NZ)**

⚠️ **Honest limit.** Method availability is finally resolved **server-side per cart** — there is a live `feverup.com/api/4.3/payment/payment-gateways-per-method/` endpoint that requires a `cart_id`. So: **"Fever has no dedicated local APAC acquirer and declares no APM client-side" is high-confidence. "Zero APMs render at final checkout" is not proven.** Both Nuvei and Checkout.com carry some APAC APMs natively. **Apple Pay is genuinely unresolved — unchecked-absence.**

### 💰 Two-sided money movement — verified verbatim
> *"Fever also acts as the Organizer's **limited agent** solely for the purpose of using its third-party payment providers to collect payments made by Customers… and **passing such payments through to the applicable Organizer**."*

**They collect and they pay out**, monthly, to event organizers across nine APAC currencies — funded by a card-centric collection stack, and entangled with an **event-financing arm** where recoupment comes out of ticketing settlement. Their terms also warn customers about *"fees for purchasing tickets and registrations in foreign currencies or from foreign persons"* and *"credit card surcharges and currency conversion rates"* — an acknowledgement of material cross-border card exposure.

### Buying signals
- 🇰🇷 **Korean login without Korean payment** — the sharpest observation available
- 🇮🇳 **Three Indian cities, INR pricing, a dedicated second brand, and no UPI**
- 💸 **Monthly organizer payouts in nine APAC currencies**, tangled with a credit book
- 💵 **$227M round led by Goldman Sachs Asset Management** (verified); ~$100M Series E 2025 and $1.8B valuation `[UNVERIFIED]`
- ⚠️ **Orchestration already in place** — this is a displacement conversation

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Fever` to draft the 12-touch sequence.*

**Five instructions for whoever drafts it — this one is high-risk and needs care:**
1. ⛔ **MOTION IS COMPETITIVE. Never imply they lack orchestration.** They run ProcessOut in production. The `/full-outreach` rule is to proceed only where research surfaced a concrete gap — **it did, and it is unusually clean: orchestration in production and zero local rails across nine live APAC markets.** The pitch is *"your orchestration isn't reaching APAC"*, never *"you need orchestration."*
2. ⛔ **NEVER NAME THE INCUMBENT.** Not ProcessOut, not Checkout.com, not Nuvei. Naming it turns this into a vendor bake-off and breaks the rulebook.
3. **Open on the Korea asymmetry.** It is inside their own stack, it is machine-verifiable, and it needs no external benchmark.
4. **Get the entity right.** Fever Labs Inc., Delaware/NY. **Do not write "Madrid-based."**
5. **The payout leg is the underweighted second wedge** — monthly settlement to APAC organizers in nine currencies. Most orchestration pitches ignore payouts; this one shouldn't.

**Never claim:** that Fever uses PayU (the field is inside the Nuvei object), that Apple Pay is absent (unresolved), any APAC revenue share (not disclosed — **do not fabricate one**), or the Trustpilot double-charge pattern as fact (see Source Notes).

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 16 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ⚠️ **The softest volume call in this repo — flag it on the call.** **No revenue, GMV or ticket-volume figure is disclosed anywhere and I refuse to invent one.** What is verified: ~796 live ticketed events across 13 APAC cities at a single snapshot, 55 countries, and a **$227M round led by Goldman Sachs Asset Management** (their own PR, fetched by me) which also states revenues had *"grown 10x"* and a presence in *"over 60 cities."* **The volume gate cannot fire — there is no sourced sub-40k figure** — and a marketplace at this funding and footprint clears 100k/month comfortably. **But this rests on scale inference, not on a number.** |
| Orchestration status | **+1** | ⚠️ **Global orchestrator incumbent — ProcessOut, in production.** Verified by me on two APAC city pages. Per the matrix this is the **+1 band**, and correctly so: it is the hardest motion. ⚠️ **Their orchestrator is owned by one of the PSPs it routes to** — a structural conflict worth understanding, though **not a line to put in an email.** |
| 3+ countries | **+3** | ✅ **55 countries; nine live APAC markets with local-currency base pricing**, verified by me from embedded page data. |
| Multiple PSPs | **+2** | ✅ **The best-evidenced multi-PSP row in this repo** — Nuvei, Checkout.com, PayPal and Google Pay all named with live production keys from their own config, plus Forter for fraud and a dormant Stripe block. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ Top APAC markets by live inventory are **Melbourne, Sydney and Singapore**. **PayNow and GrabPay absent in Singapore; PayTo, BPAY, Afterpay and Zip absent in Australia** — sourced from `paymentMethods:[]` and a gateway config with no local acquirer. ⚠️ **High-confidence, not proven-absolute** — final method resolution is server-side per cart. |
| Recent expansion | **0** | ⬜ Nine APAC markets is footprint, not dated expansion. A live Korean Client Success role exists but is **agent-sourced**. |
| Payment issues reported | **0** | ⬜ **Not awarded — unverified.** Trustpilot carries ~2,900 reviews with a recurring **"payment reported as failed when it had actually gone through, producing a duplicate charge"** pattern. **That is the textbook signature of retry logic without reliable idempotency across PSPs — i.e. a direct technical hook into their orchestration — and it is exactly why it must be verified before use.** Nobody fetched it. |
| Funding >$10M | **+2** | ✅ **Verified by me** — PR Newswire, Goldman Sachs Asset Management **leads $227m** investment in Fever. The 2025 ~$100M Series E, ~$527M total raised and $1.8B valuation are `[UNVERIFIED]`. |
| High traffic outside home | **0** | ⬜ No traffic data, and **no APAC revenue share is disclosed.** Their own 2022 PR says *"The US is currently Fever's largest market"* — so APAC is outside home, but **unquantified.** |
| Competitor using orchestration | **0** | ❌ Not established for Eventbrite, Ticketmaster, Dice, Klook or Trip.com. |
| Payment job postings | **0** | ⬜ Careers pages render ~18 roles client-side; no payments, billing, treasury or payout roles seen. **Weak evidence — the full listing was never seen.** |

**Tier: 16 / 29 → 🟢 Medium.** No analyst override applied.

### Source Notes
- ✅ **The gateway config was verified by me byte-for-byte on two APAC city pages** (`/en/seoul`, `/en/singapore`), including `processOut` with `riskEnvironment:"PRODUCTION"` and `"paymentMethods":[]`.
- ✅ **Every Kakao/Naver reference was inspected individually and every one is OAuth**, with zero occurrences of KakaoPay, Naver Pay, Toss Pay, PAYCO or Samsung Pay.
- ✅ **Local-currency pricing verified** — KRW 199 hits on Seoul and 0 on Singapore; SGD 421 on Singapore and 0 on Seoul.
- ✅ **The Delaware entity, the limited-agent clause and the foreign-currency warning were all verified verbatim** from `feverup.com/legal/terms_en.html`.
- ✅ **The $227M Goldman round was verified** at PR Newswire, which also yields *"revenues 10x"* and *"over 60 cities"* and **"The US is currently Fever's largest market."**
- 📌 **ProcessOut was acquired by Checkout.com in February 2020** and sells multi-PSP smart routing, cross-provider retry and acceptance-rate optimisation — i.e. our category. `[UNVERIFIED — TechCrunch/Checkout.com newsroom, search-summary level]`, but the **production key on their page is first-party and verified.**
- ⚠️ **The agent grepped the 320KB main JS bundle for 20+ absent vendors and reported every apparent hit as a substring false positive** — `omise` from `Promise`, `eway` from `gateway`, `tyro` from the CSS colour `mistyrose`, `square` from CSS. **Consistent with our running false-positive list; a useful confirmation that the absence is real.**
- ⚠️ **Funding beyond the 2022 round, the APAC job posting, and the entire complaint corpus are agent-sourced and unfetched.**
- ❌ **No APAC revenue or GMV share exists publicly. Do not fabricate one.**
- ❌ **No engineering blog or public GitHub org surfaced.**

### Manual Research Recommendations
> **1. Create a cart in Seoul or Singapore and hit `/api/4.3/payment/payment-gateways-per-method/`.** It is the one call that converts high-confidence into proven, and it settles Apple Pay too.
> **2. Verify the Trustpilot duplicate-charge pattern properly.** If real, it is the sharpest technical hook on the account and worth +2.
> **3. Establish an APAC entity by registry lookup** (ACRA, ASIC, Japan NTA). Offices are confirmed via careers; entities are not.
> **4. Confirm organizer payout mechanics and FX handling on the Asia leg** — the second wedge rests on it.

---

## Executive Summary

Fever is a live-entertainment marketplace operating in 55 countries, and — contrary to the stub — is **Fever Labs Inc. of Delaware and New York**, not a Madrid company. Its APAC presence is real and substantial: **nine live markets with local-currency base pricing**, roughly 800 live ticketed events across thirteen cities, offices in six APAC cities, Korean-language product, and a separate India brand. It is **not a greenfield account**: its own production page config, which I verified byte-for-byte on two APAC cities, shows a **global orchestration layer running live** above **Nuvei, Checkout.com, PayPal and Google Pay**, with Forter for fraud. And that is precisely what makes the account interesting — **the orchestration is in production and has still produced not one local payment rail anywhere in APAC.** The config served to Seoul is identical to the one served everywhere else, with `paymentMethods` an empty array: no PayNow or GrabPay in Singapore, no PayTo or BPAY in Australia, no UPI across three Indian cities, and — the sharpest observation available — **no KakaoPay, Naver Pay or Toss in Korea, on a site that ships fully-configured Kakao and Naver OAuth login.** They localized the front door and never localized the till. At **16/29** the score is held down by a volume row that rests on scale inference rather than any disclosed figure, and by a duplicate-charge complaint pattern that would be worth real points if anyone verified it.

</details>
