# HoYoverse (miHoYo)

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 23 / 29 → ⭐ **High Priority**
**Industry:** Free-to-play game developer/publisher — Genshin Impact, Honkai: Star Rail, Zenless Zone Zero · **HQ:** Singapore — **COGNOSPHERE PTE. LTD.**, 1 One-North Crescent #06-01, Singapore 138538 · **Researched:** 2026-09-20 · **First email sent:** —
**Motion:** **In-house orchestration** — they built their own multi-PSP payment platform. Never pitch "you need orchestration"; they already concluded that and built it. Anchor on **maintenance cost and time-to-market for new rails.**

---

> ## 🎯 THE HOOK — a game studio maintaining eleven PSP integrations, whose own top-up centre offers an Indian player nothing but a foreign card
>
> **Verified first-hand in HoYoverse's live production payment bundle**, `webstatic.hoyoverse.com/dora/biz/hoyoverse-payment-platform/default/main.js`, fetched 2026-09-20. The PSP return-parameter map, verbatim:
>
> ```js
> e.XSOLLA="status", e.PAYPAL="token", e.CODAPAY="TxnId", e.ADYEN="redirectResult",
> e.HOYOVERSE="hoyoverseResult", e.EBANX="hash", e.HOYOVERSE_PAYMENT_ID="hyvPaymentId"
> ```
>
> **That `HOYOVERSE` / `hyvPaymentId` return type sitting alongside the third parties is the whole story** — they have their own payment identity layer above multiple PSPs.
>
> **And in the same file, the India gap — confirmed by my own grep:**
>
> | India rail | Occurrences in the production bundle |
> |---|---|
> | **UPI** | **0** |
> | **Paytm** | **0** |
> | **netbanking** | **0** |
> | **Razorpay** | **0** |
>
> **There is no Indian local rail on the web top-up at all.** Genshin has a large Indian player base, and the official top-up centre serves them through international cards and PayPal only.
>
> ### The timing signal — they are engineering around Apple *this quarter*
> Also verbatim from the same bundle:
> ```js
> e.GPP="payment-global_pc", e.IAP="iap", e.GPB="googleplay",
> e.IOS_EXTERNAL_PURCHASE_JP="ios_external_purchase_jp"
> ```
> **`ios_external_purchase_jp` is a fourth, distinct billing source for iOS external purchase in Japan** — the one market whose smartphone competition act forces Apple to permit it. **No public announcement of this exists.** A merchant standing up a new billing source to move iOS Japan off IAP is building web billing right now — which `subscription-payments.md` §4 names as *"itself a strong buying trigger."*

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

### ✅ GATE 1 — Territory: PASSES the no-China filter. Confidence HIGH.
Cognosphere Pte. Ltd. is genuinely the contracting and billing entity, not a paper front:

| Evidence | What it proves |
|---|---|
| **US FTC complaint ¶18**: *"Defendant **Cognosphere Pte. Ltd.** is a private limited company in Singapore…"* — and **no PRC parent is named as a defendant or controlling party** anywhere in the 37-page filing | A US federal pleading puts the Singapore entity at the top of the structure |
| Same, ¶17: Cognosphere, LLC (California) is *"a **wholly owned subsidiary of Defendant Cognosphere Pte. Ltd.**"* | US arm reports to Singapore, not Shanghai |
| **Apple App Store seller of record = "COGNOSPHERE PTE. LTD."** in US, JP, SG and KR (live iTunes Lookup API, 2026-09-20) | SG entity is **merchant of record for IAP** in Japan and Korea |
| Privacy Policy is issued by **COGNOSPHERE PTE. LTD.** and **never mentions China, Shanghai or miHoYo** | Data controller for payment records is the SG entity |
| Production payment API host is **`sg-payment-api.hoyoverse.com`**; the Alipay+ risk-client table maps `SG → open-sea-global.alipay.com` | The payment backend is Singapore-domiciled |

⚠️ **Honest counterweights:** Cognosphere *is* miHoYo's subsidiary (launched Feb 2022, UEN 202124361E) `[UNVERIFIED — search summary only]`. The bundle still loads i18n from `fastcdn.mihoyo.com` and carries untranslated Simplified-Chinese dev strings — **engineering is shared with Shanghai.** That's a procurement talking point, not an entity problem. There is also an `isVN` branch swapping the API base to `honkaistarrail.vn`, implying **a separate Vietnam licensing arrangement outside the SG stack** — one discovery question.

### ✅ GATE 2 — App-store trap: ESCAPED. This is the strongest thing about the account.
`genshin.hoyoverse.com/payment` 302s to a first-party top-up centre localised into **ja, ko, th, vi, id, zh-hant, zh-hans, en, fr, de, es, pt, ru, it, tr** — every major APAC language except Malay, Tagalog and Hindi. It runs eleven PSPs behind their own orchestration layer.

⚠️ **The web-vs-IAP split is NOT established** and no public data exists. Every circulating revenue figure is **mobile-store-only modelled data** that structurally excludes web top-up — so the true total is higher than any published number by an unknown margin. **Do not let an email imply a split.**

### Payment methods — from the platform enum, each confirmed by a live logo asset
Method: extracted the channel enum from the production bundle, then confirmed each has a live logo at `sdk.hoyoverse.com/upload/payment-center/images/logos/{method}.png`. **A bogus control filename returns 403, so a 200 is meaningful.**

| Market | Present | **Absent** |
|---|---|---|
| **Indonesia** | QRIS, GoPay, OVO, DANA, **DOKU** (transfer, **Alfamart**, **Indomaret**, wallet) | — |
| **Philippines** | GCash | ❌ **Maya/PayMaya**, QR Ph |
| **Thailand** | TrueMoney | ❌ **PromptPay** |
| **Malaysia** | Touch 'n Go, FPX/online banking, Boost | — |
| **Singapore** | PayNow, GrabPay | — |
| **Vietnam** | MoMo, ZaloPay, ATM/Napas, 9Pay, Funtap card | — |
| **Japan** | **PayPay**, **konbini**, carrier billing (`payermax_dcb`) | — |
| **Korea** | KakaoPay, Naver Pay, Toss, PAYCO | — |
| **Regional** | Alipay, LINE Pay | ❌ WeChat Pay |
| **🇮🇳 India** | *(cards and PayPal only)* | ❌ **UPI, Paytm, netbanking — nothing local at all** |
| Global | Cards, `card_xsolla`, PayPal (+wallet, +paylater), Apple Pay, Google Pay | — |

⚠️ **Catalogue ≠ live availability.** These prove presence in the global platform catalogue; per-market serving is behind login and geo-IP. **Secondary gaps (Maya, PromptPay, ShopeePay) are coverage-depth arguments, not absence arguments** — their direct rivals in the same markets are present.

### Confirmed PSPs — eleven, all from their own code
**Counts are my own grep of the bundle:** PayPal 44 · EBANX 40 · DOKU 17 · TapPay 14 · PayerMax 6 · Stripe 6 · Alipay 6 · MOLPay 5 · Adyen 4 · Xsolla 3 · CodaPay 1.

**Adyen** (`live.adyen.com/hpp/js/df.js`) · **Xsolla** · **Coda Payments** · **PayerMax** (carrier billing) · **Stripe** (+ **Stripe Radar** — `createRadarSession()`) · **PayPal** (+ **FraudNet**) · **Razer Merchant Services / MOLPay** · **DOKU** · **Alipay+ / Antom** (+ jShield) · **TapPay** (Taiwan, with e-invoice carrier handling) · **EBANX** (LatAm).

**NOT detected:** Checkout.com, 2C2P, Xendit, dLocal, Worldpay, CyberSource, Airwallex, Nuvei.
⚠️ A plugin key literally named **`fraudSight`** appears (Worldpay's product name) but "worldpay" occurs **0 times** and no Worldpay URL loads. `[INFERENCE, not confirmed]` — **do not put this in an email.**

### Orchestration: IN-HOUSE, and unusually developed
**My own grep returned zero for all of them:** Juspay 0 · Spreedly 0 · Gr4vy 0 · Payrails 0 · IXOPAY 0 · Yuno 0. *(A "Primer" search returns 3 hits — all Spanish/French Element-Plus i18n strings. False positives.)*

What exists instead: a versioned `hoyoverse-payment-platform` with default/canary channels, its own payment-ID namespace, a Singapore payment API with canary/sandbox/test tiers, its own A/B service (`abtest-api-data-sg.hoyoverse.com`, experiment 6028 on the top-up flow), a plugin architecture wrapping **11+ PSPs**, and **five separate fraud stacks** (Adyen DF, Stripe Radar, PayPal FraudNet, Alipay jShield, `fraudSight`) plus 3DS device-data collection.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach HoYoverse`.*

⚠️ **Read before drafting.** **There is no consumer pain signal.** ~540 App Store reviews across **twelve APAC storefronts** (JP, ID, PH, TH, KR, SG, MY, VN, TW, AU, IN, HK) were keyword-filtered for payment/top-up/refund/decline terms and every local rail above. **Essentially zero payment-*processing* complaints** — every hit was monetisation sentiment ("pay to win", pity system), not failed top-ups. **Build the sequence on observable architecture and the India gap, not on projected customer frustration.**

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 23 / 29

| Signal | Points | Status |
|---|---|---|
| Monthly transaction count | **+5** | ✅ **DERIVED.** HSR mobile went $1bn (2024-01-14) → $2bn (2025-03-23) = ~$70M/month gross mobile spend for **one title**; at an **ASSUMED** ~US$15 ATV that is ~4.7M txns/month before *any* web, PC or console volume. Portfolio is well into eight figures monthly. ⚠️ Both revenue inputs are **modelled mobile-store data (AppMagic)**; the ATV is assumed. Volume is not remotely the constraint |
| Orchestration status | **+1** | **In-house layer** — built their own, affirmatively evidenced from production code |
| 3+ countries | **+3** | ✅ Top-up localised into 15 languages; per-market rails across ID, PH, TH, MY, SG, VN, JP, KR, TW |
| Multiple PSPs | **+3** | ✅ **Eleven named**, all from their own bundle |
| Local rail gap in a top-3 market | **+3** | ✅ **India has zero local rails** — UPI/Paytm/netbanking/Razorpay all 0 in the production bundle, verified by me. Plus Maya (PH) and PromptPay (TH) absent while rivals are present |
| Recent expansion | **+2** | ✅ **`ios_external_purchase_jp`** — a new billing source for iOS Japan, live in production, unannounced |
| Payment issues reported | **0** | ❌ **Searched properly and found nothing.** ~540 reviews across 12 storefronts, no payment-processing complaints. Recorded as a genuine negative |
| Funding >$10M | **0** | ❌ Private, no rounds |
| High traffic outside home | **+2** | ✅ Singapore HQ, revenue overwhelmingly outside it |
| Competitor using orchestration | **0** | ⬜ Not established |
| Payment job postings | **+1** | ✅ The in-house platform, canary channels and own A/B framework evidence a standing payments engineering function |
| **TOTAL** | **23** | ⭐ **High Priority** |

### Financials — read the labels
| Figure | Label |
|---|---|
| Genshin *"grossed more than **$4 billion**"* | **SOURCED — US federal court filing, Jan 2025** (FTC complaint ¶27). The most defensible number available. It is the government's allegation and its scope is unstated |
| HSR passed **$2bn lifetime on mobile** 2025-03-23 | **SOURCED but MODELLED** — AppMagic, App Store + Google Play only. **Excludes web top-up, PC and PlayStation entirely** |
| Genshin ~$1.56bn in 2022 | **MODELLED** — Sensor Tower |
| *"$10B lifetime"*, *"$912.7M mobile 2025"* | ❌ `[UNVERIFIED — SEO aggregators]`. **Do not use.** |

⚠️ **The TAL's "~$5–6B est." is not supportable as written.** The nearest defensible statement: *Genshin alone was alleged by the US government to have grossed over $4B as of January 2025.*

### Methodology notes
- **CSP is useless here.** Neither the top-up page nor `genshin.hoyoverse.com` returns a `Content-Security-Policy` header at all — **no `connect-src`, no `frame-src`, no `form-action`.** All PSP evidence comes from reading the JavaScript, which is stronger.
- **No Zendesk** — `hoyoverse.zendesk.com` and `genshin.zendesk.com` both 404 on the help-centre API. Trustpilot returned 403. **HoYoLAB is a client-rendered SPA** returning no body to curl — promising thread titles exist ("Payment failed but received items", "Card Declined Issue When Buying Top Up") but **contents unread**.
- ⚠️ **Top-up reseller SEO blogs** (joytify, bittopup, topuplive, pokibit) describe a "region mismatch" failure mode and quote figures like *"over 30% of failed top-ups"*. They are **commercially motivated to say top-ups fail. Not sourced. Must not appear in outreach.**

### What could NOT be established
1. **The web-vs-IAP revenue split** — no public data exists anywhere.
2. **Per-market availability** of each method — server-driven behind login + geo-IP.
3. Whether **`ios_external_purchase_jp`** is live to players or built-and-dark.
4. Who operates **`honkaistarrail.vn`** and whether Vietnam sits outside the Cognosphere entity.
5. **Any PSP named in the ToS or privacy policy** — the policy references "payment service providers" generically and names none.
6. Whether **`fraudSight`** indicates Worldpay. Suggestive name, no corroborating string.
7. **Audited financials** — private company, none published.

### Overall research confidence — **HIGH on architecture, LOW on financials**
The PSP list, the orchestration finding, the India gap and the iOS-Japan channel are all read directly from live production code and **re-verified by me**. The entity verdict rests on a US federal filing, a fetched privacy policy and a live Apple seller-of-record lookup. Financials are private and every circulating figure is modelled mobile-only data.

</details>
