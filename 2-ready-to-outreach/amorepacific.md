# Amorepacific

**Status:** 🟢 Ready to outreach — sequence drafted
**ICP Score:** 17 / 29 → ⭐ **High Priority** — earned on arithmetic, no override applied
**Industry:** Cosmetics manufacturer and brand owner (Sulwhasoo, Laneige, Innisfree, Etude, Hera, COSRX) · **HQ:** Seoul, South Korea · **Listed:** Amorepacific Corporation, KRX **090430** · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** **Greenfield** — and unusually so: **four separate payment estates with nothing shared between them.** Classification is affirmative, verified by me from three live payment-config endpoints.

---

> ## ⚠️ READ THIS BEFORE ANYTHING ELSE — this is a complexity account, not a volume account
>
> Amorepacific Corp turns over roughly **KRW 4.25tn (~US$3.1bn)**. **Almost none of it touches an Amorepacific checkout.** Their own 1Q26 IR deck defines the "Online" channel as third-party marketplaces, verbatim:
>
> > *"Online: … Posted sales in all major platforms (**Naver, Kakao, Coupang**, etc.)"*
>
> And overseas reads the same: *"Diversified brand portfolio in **Amazon**"*, *"entry into **Sephora**"*, *"sales of **Tmall** increased"*, *"**Qoo10** Megawari"*, *"**TikTok Shop**"*, *"major platforms (**Shopee**, Tiktok)"*. Add **Olive Young and Daiso** (wholesale), department-store concessions, and **travel retail at 17% of domestic business**. Every one of those checkouts belongs to somebody else.
>
> The **only** own-checkout mention in the whole deck: *"sales doubled for the **Global Amore Mall (direct-to-consumer platform)**"* — with no absolute figure and no base.
>
> **If a sequence opens with "you process billions", it is wrong and they will know it in one line.** The addressable estate is low single-digit percent of the top line. What makes this account real is the *shape* of that estate, not its size.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Amorepacific is Korea's largest cosmetics group, selling overwhelmingly through marketplaces, wholesale, department stores and duty free. Its own direct-to-consumer estate is small but **structurally fragmented into four completely independent payment stacks** — a Korean in-house mall on KG Inicis, Korean brand sites on Cafe24, a cross-border global mall on Shopify running PayPal and Eximbay, and per-brand Western Shopify stores each on their own Shopify Payments account.

**SimilarWeb total visits:** **Not obtained** — none supplied and no MCP tools. **Geography below comes from audited IR segment revenue instead, which is the better source anyway** (same approach the YesStyle file took).

### Markets — Amorepacific Corp, 1Q26, from their own IR deck
| Segment | 1Q26 (KRW bn) | Share | YoY |
|---|---|---|---|
| **Domestic** | 626.4 | **55.2%** | +8.5% |
| Americas | 174.7 | 15.4% | +11.2% |
| Other Asia (Japan, ASEAN, India) | 143.1 | 12.6% | +15.0% |
| Greater China | 114.9 | 10.1% | **−13.5%** |
| EMEA | 64.4 | 5.7% | +16.4% |
| **Overseas total** | **497.1** | **43.8%** | +5.8% |

FY2024 direction: **Americas +83%, and it "surpassed Greater China to become the group's largest global market by revenue for the first time"**; EMEA tripled; Greater China −27%.

### The four payment estates — verified by me, first-hand
| # | Estate | Platform | Payment stack |
|---|---|---|---|
| 1 | **amoremall.com** (Korea) | In-house | **KG Inicis** (escrow relationship proven from their own footer) |
| 2 | **laneige.com/kr** etc. (Korea brand sites) | **Cafe24** (`aplaneige.cafe24.com`) | **PG not established** — Cafe24 bundles Inicis/NICEPAY/Toss/KCP |
| 3 | **global.amoremall.com** (cross-border) | Shopify, `shopId 62092247178` | **PayPal + Eximbay.** Shopify Payments **off** |
| 4 | **us.laneige.com · us.sulwhasoo.com · us.innisfree.com · cosrx.com · jp.laneige.com · int.sulwhasoo.com** | Shopify, **one shop ID each** | **Shopify Payments + Shop Pay + Apple Pay + Google Pay + PayPal + Afterpay** |

### Orchestration status
**None detected — no orchestrator, no in-house layer, nothing shared.** Zero hits against Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails, IXOPAY and Yuno — but the real evidence is structural and positive, not an absent search result. See 3B.

### Buying signals
- 🧩 **Four independent payment estates**, each with its own provider, its own reporting and its own reconciliation
- 🚀 **New market entries named in 1Q26: Brazil and South Africa** (cross-border), IOPE into the Americas, Aestura into Europe and Sephora
- 📈 **Americas now the largest overseas market**, +83% in FY2024, while **Greater China fell 13.5% YoY** and is under active *"offline channel rationalization"*
- 🛒 **COSRX consolidated** — another entirely separate Shopify estate absorbed into the group
- ❌ **No payment RFP, no payments hire, no orchestration vendor found**

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

### Pain Vector Extraction

```
=== PAIN VECTOR EXTRACTION ===

Motion: Greenfield — none detected, affirmatively. Phase 1 may note the absence of a
        routing layer. But the framing is FRAGMENTATION, never volume (see the warning
        at the top of this file).

Observable setup facts (verified first-hand, 2026-09-18):
- global.amoremall.com/payments/config returns applePayConfig:null, shopifyPayConfig:null,
  googlePayConfig:null, amazonPayCv2Config:null — and paypalConfig present
- the SAME response carries dynamicCheckoutPrioritization:
  ["ApplePay","ShopifyPay","PayPal","AmazonPayCv2","GooglePay"] — it is configured to lead
  with two wallets that are switched off
- us.laneige.com (shopId 25501892660) and us.sulwhasoo.com (shopId 24983994413) both carry
  Apple Pay, Google Pay and Shop Pay, with applePayConfig.shopifyPaymentsEnabled = true
- Korea runs a separate in-house mall on KG Inicis; Korean brand sites run on Cafe24
- Cross-border runs PayPal + Eximbay; each Western brand has its own Shopify Payments account
- Domestic 55.2% / overseas 43.8%; Americas now the largest overseas market; Greater China
  -13.5% YoY and under active offline rationalization
- Brazil and South Africa named as new cross-border entries in the 1Q26 deck

Selected observations for Phase 1 (E1 bullets, ranked by materiality):
1. The wallet asymmetry → "Your US brand stores lead checkout with Apple Pay, Google Pay and
   Shop Pay. Your cross-border mall is configured to lead with Apple Pay and Shop Pay too,
   and neither is switched on."
   MATERIALITY: highest. Machine-readable from their own endpoints, both halves. It cannot
   be disputed and it needs no interpretation.
2. Four estates → "Korea runs on one provider, cross-border on another, and each Western
   brand store has its own separate merchant account."
   MATERIALITY: high. It is the structural fact the whole account rests on.

   (Held at 2. Deliberately NOT used: anything about volume, revenue or scale.)

Bridge variant: A — complexity
Rationale: multi-provider and multi-market is established first-hand, not inferred. Four
named providers across five platforms. Variant A describes that shape without projecting
pain, which Phase 1 forbids.

Hypothesis for Phase 2 (E3):
Each brand and each region is its own payment island, so nothing is shared — no common
vault, no common reporting, no common routing. A shopper who buys Laneige in the US and
Sulwhasoo cross-border is two unrelated customers to the payment stack.
Backing logic: three separate Shopify shop IDs with three independently-configured stacks,
plus KG Inicis and Cafe24 in Korea. Every new market entry — Brazil and South Africa are
named in their own 1Q26 deck — lands on whichever estate happens to serve it.

Success case for Phase 3 (E4):
Selected case: Rappi
Tier: 2 — same payment pattern (multi-country, multi-brand, heavy provider and method
breadth, operational reconciliation load), different industry and region. Stated in the email.
Match rationale: no Tier 1 exists. There is no cosmetics or Korean case in the library.
Rappi is the library's operational-burden case and is the closest to a merchant carrying
several parallel estates.
Numbers to lead with: zero implementation delays · hundreds of payment methods through one
integration · 80% less analyst work
Optional benchmark: SKIP. The "~8% average authorisation uplift" is Yuno's own blog figure,
not third-party evidence, and this sequence is not an approval-rate argument anyway.

Touch-by-touch angles:
- E2 angle: the four estates → unified reconciliation + a single routing layer (one mechanism)
- LK1 angle: the wallet asymmetry, one sentence
- LK2 angle: each brand and region is its own payment island
- LK3 angle: Rappi cut analyst work 80% without changing providers
- LK4 angle: FRESH — Brazil and South Africa are named in their own 1Q26 deck
- E8 angle: clean exit, offer to circle back after FY2026 results
```

**Calendar.** Day 1 anchored to **Monday 28 September 2026** — deliberately *after* **Chuseok
(24–26 Sep)**. Korean holidays inside the send window: **Mon 5 Oct** (substitute for National
Foundation Day, 3 Oct falling on a Saturday) and **Fri 9 Oct** (Hangeul Day). **No send day
and no proposed meeting slot falls on either**, or on a weekend.

**Times are KST (UTC+9), which is IST+3:30.** Per the rulebook, Korea gets afternoon-local
slots so they land as late morning for Prateek — every slot below is 14:00–16:30 KST,
i.e. 10:30–13:00 IST.

---

### Phase 1 — Curiosity (Days 1–5)

#### Touch 1 — Email 1 · Day 1 · Mon 28 Sep

**Subject:** Wallets on your cross-border mall

```text
Hey {{recipient.first_name}},

Spent some time on Amorepacific's payment setup. Two things stood out:

- Your US brand stores lead checkout with Apple Pay, Google Pay and Shop Pay. Your cross-border mall is configured to lead with Apple Pay and Shop Pay too, and neither is switched on.
- Korea runs on one provider, cross-border on another, and each Western brand store sits on its own separate merchant account.

That kind of setup usually comes with some complexity.

I work at Yuno — top-100 fintech, a16z-backed. We consider ourselves the 'everything payments' platform: one integration, every PSP, every method, every market.

Rather than pitch you based on assumptions, is there anything payment-related you're working through that we might be able to help with?

Best,
Prateek
```

#### Touch 2 — Email 2 · Day 3 · Wed 30 Sep · REPLY IN THREAD

```text
Hey {{recipient.first_name}},

Following up. Wanted to put a bit more behind what Yuno actually does, and how it would address what I flagged.

- We sit above your existing providers. Additive, nothing gets ripped out.
- One integration covers every brand and every region, so a method enabled once is available everywhere.
- Settlement, refunds and disputes from every provider land in one ledger.
- Adding a PSP, an acquirer or a wallet becomes a configuration change rather than a project.

On the four estates specifically, the part that matters is the reconciliation layer. Today Korea, cross-border and each Western brand report separately, so there is no single view of a customer or a settlement. That is the piece that collapses first.

I'll keep sharing what I'm seeing every few days. If your stack's where you want it, just say the word and I'll back off. Otherwise happy to go deeper.

Cheers,
Prateek
```

#### Touch 3 — LinkedIn message 1 · Day 5 · Fri 2 Oct

```text
Hey {{recipient.first_name}} — dropped you a note over email, flagging it here too in case this is the easier channel. Quick one: your US brand stores lead checkout with Apple Pay, Google Pay and Shop Pay, and your cross-border mall is set up to lead with Apple Pay and Shop Pay but has neither enabled. Curious whether that's deliberate or just where the roadmap landed.
```

---

### Phase 2 — Diagnosis (Days 7–9)

#### Touch 4 — Email 3 · Day 7 · ~~Sun 4 Oct~~ · ~~Mon 5 Oct — National Foundation Day substitute~~ → **send Tue 6 Oct** · NEW EMAIL

**Subject:** Four payment estates, nothing shared

```text
Hey {{recipient.first_name}},

Going to take a swing at this. My read is that each brand and each region is its own payment island: Korea on one provider, cross-border on another, and every Western brand store on its own separate merchant account.

Which means nothing is shared across them. No common vault, no common reporting, no common routing. Someone who buys Laneige in the US and Sulwhasoo cross-border is two unrelated customers to the payment stack, and every new market lands on whichever estate happens to serve it.

When a new market goes live, does payments sit with the regional team or with a central group?

At Yuno (a16z-backed, top-100 fintech) we sit above your existing providers, so the brands stay where they are and the layer above them becomes one. Keep your stack, add what's missing.

Thursday 8 October is open. Would 2pm or 4pm your time work for a quick 15?

All the best,
Prateek
```

#### Touch 5 — LinkedIn message 2 · Day 9 · ~~Tue 6 Oct — taken by the shifted E3~~ → **send Wed 7 Oct**

```text
Hey {{recipient.first_name}} — sent a longer note over email this week. Short version: every brand and every region looks like its own payment island, so nothing is shared between them — not the vault, not the reporting, not the routing. If that's anywhere on your radar, would Monday 12 or Tuesday 13 October at 3pm your time work for a quick 15?
```

---

### Phase 3 — Proof (Days 11–17)

#### Touch 6 — Email 4 · Day 11 · Thu 8 Oct · NEW EMAIL

**Subject:** How Rappi solved this

```text
Hey {{recipient.first_name}},

On the read I shared last week. Sharing a quick example of what solved looks like.

Rappi runs multiple brands and verticals across a lot of countries, with a different provider mix in most of them. They put Yuno above the existing stack rather than replacing it. What that produced:

- Zero implementation delays on new payment integrations
- Hundreds of payment methods reachable through one integration
- 80% less analyst work on reconciliation (that one surprised me too)

Worth saying plainly: Rappi is a Latin American super app, not a beauty group, so this is a payment-pattern match rather than an industry one. What carries over is the shape — several parallel estates, each with its own provider and its own reporting, and the reconciliation load that creates.

Same orchestration layer above their existing stack. No rip-out.

Wednesday 14 October is open. Would 2.30pm or 4.30pm your time work for 15 minutes?

Full case here if useful: https://y.uno/success-cases/rappi

Thanks,
Prateek
```

#### Touch 7 — Email 5 · Day 13 · ~~Sat 10 Oct~~ → **send Mon 12 Oct** · MANUAL

*Placeholder — manual creative approach. Do not auto-write.*

> **Strongest asset available:** a side-by-side screenshot of the three `/payments/config`
> responses. `global.amoremall.com` with four `null` wallet configs next to `us.laneige.com`
> and `us.sulwhasoo.com` with all three enabled. It is their own data, it takes ten seconds
> to read, and it makes the point without a sentence of argument.

#### Touch 8 — Email 6 · Day 15 · ~~Mon 12 Oct — taken by the shifted E5~~ → **send Tue 13 Oct** · MANUAL

*Placeholder — second manual approach, different format from E5.*

> **Suggested angle: the China contraction.** Greater China fell **13.5% YoY** and is under
> explicit *"offline channel rationalization"* in their own 1Q26 deck, while **Americas
> became the largest overseas market**. A short written note on what shifting weight from
> China to the Americas and EMEA does to a payment estate that was built region by region.

#### Touch 9 — LinkedIn message 3 · Day 17 · Wed 14 Oct

```text
Hey {{recipient.first_name}} — Rappi cut reconciliation analyst work by 80% without changing a single provider, just by putting one layer above them. Worth 15 minutes to see whether that maps to your setup? Monday 19 October at 3.30pm your time is open.
```

---

### Touch 10 — Email 7 · Day 19 · Fri 16 Oct · MANUAL

*Placeholder — manual creative bridge. Anchor to something fresh.*

> **Freshest hook:** their own 1Q26 deck names **Brazil and South Africa** as new cross-border
> entries, plus **IOPE into the Americas** and **Aestura into Europe and Sephora**. Four new
> market entries landing on an estate that already has four providers. That is the
> expansion-readiness conversation, and it is dated and first-party.

---

### Phase 4 — Breakup (Days 21–23)

#### Touch 11 — LinkedIn message 4 · Day 21 · ~~Sun 18 Oct~~ → **send Mon 19 Oct**

```text
Hey {{recipient.first_name}} — last LinkedIn ping from me on this. One thing I never raised: your own 1Q26 deck names Brazil and South Africa as new cross-border markets, on top of IOPE into the Americas. Four new entries across an estate that already runs four providers. If timing works, Thursday 22 October at 2pm your time is open for a quick 15.
```

#### Touch 12 — Email 8 · Day 23 · Tue 20 Oct · REPLY IN THREAD to Touch 4 or Touch 6

```text
Hey {{recipient.first_name}},

Going to stop pinging unless you want to pick this back up.

If the timing is just off, happy to circle back once your FY2026 results land. And if payments sits with someone else on your side, happy to be pointed there.

If it ever comes back up, just reply here.

All the best,
Prateek
```

---

### CTA schedule — five distinct slots, all KST

| Touch | Sent | Proposed slot(s) | KST → IST |
|---|---|---|---|
| E3 | Tue 6 Oct | **Thu 8 Oct, 14:00 or 16:00** | 10:30 / 12:30 IST |
| LK2 | Wed 7 Oct | **Mon 12 or Tue 13 Oct, 15:00** | 11:30 IST |
| E4 | Thu 8 Oct | **Wed 14 Oct, 14:30 or 16:30** | 11:00 / 13:00 IST |
| LK3 | Wed 14 Oct | **Mon 19 Oct, 15:30** | 12:00 IST |
| LK4 | Mon 19 Oct | **Thu 22 Oct, 14:00** | 10:30 IST |

No slot falls on **5 Oct** or **9 Oct**, the two Korean public holidays in the window, or on a
weekend. No booking link anywhere, by decision — the reply is the booking.

---

### Source Notes

- ✅ **Every Phase 1 observation was verified by me first-hand** on 2026-09-18 from three live `/payments/config` endpoints. Both halves of the wallet asymmetry are machine-readable from Amorepacific's own responses.
- ✅ **The `dynamicCheckoutPrioritization` array is verbatim** — `["ApplePay","ShopifyPay","PayPal","AmazonPayCv2","GooglePay"]` — sitting in the same response as four `null` wallet configs.
- ✅ **KG Inicis** from their own Korean footer escrow disclosure; **Eximbay + PayPal** from `global.amoremall.com/pages/faqs`.
- ✅ **Korean public holidays checked at source.** Chuseok 24–26 Sep, National Foundation Day substitute Mon 5 Oct, Hangeul Day Fri 9 Oct. Day 1 was moved to 28 Sep specifically to clear Chuseok.
- ✅ **Rappi is Tier 2 and E4 says so outright.** No implication that the results came from Asia.
- ⚠️ **No volume claim appears anywhere in the sequence.** This is deliberate and non-negotiable — see the warning at the top of this file. No revenue figure, no transaction count, no "you process X".
- ⚠️ **No recipient identified.** All twelve touches use `{{recipient.first_name}}`. The likely owner is a group digital or e-commerce lead rather than a brand-level marketer — the fragmentation argument only lands with someone who sees more than one estate.
- ❌ **Benchmark omitted from E4.** The "~8% authorisation uplift" is Yuno's own blog figure and this is not an approval-rate argument.
- ❌ **Not used, deliberately:** the "Amorepacific Holdings" rename (aggregator-only and contradicted by their own site), the COSRX deal terms (search-summary only), and "over 40% of global sales from e-commerce" (exists in no IR document).

### Success Case Alternatives
- **inDrive** — 50+ countries, ~90% approval, 10 new countries in under 8 months. Better swap if the conversation turns to **market entry** (Brazil, South Africa, IOPE Americas) rather than reconciliation load.
- **McDonald's / Arcos Dorados** — unified processing across 21 countries. The closest structural analogue to a multi-brand group with regional estates, but no public link and no published metrics, so it cannot carry an E4.
- **Livelo** — use only if discovery reveals declines with no failover. Nothing in this research points there yet.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 17 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+3** | ⚠️ **NOT FOUND — ASSUMED ~50,000–150,000/month across all four estates combined.** `[ASSUMPTION — not researched.]` **Amorepacific publishes no order count, no DTC GMV, no AOV and no own-mall/marketplace split.** **Basis:** own-checkout revenue is bounded by part of the 22% "Travel Retail & Cross-border" slice of domestic (and travel retail alone is 17% of domestic, so cross-border is the smaller half) plus the Western and Japanese Shopify stores — call it low single-digit percent of KRW 4.25tn, so roughly US$60–150m at a beauty AOV of US$40–60. **Scored the 50k–100k band, deliberately one band below where the midpoint arithmetic lands**, because every input is inferred from disclosed *structure* rather than a published figure. **Deriving this from group revenue would be flatly wrong** — the overwhelming majority of that revenue never touches an Amorepacific checkout. An assumption cannot fire the under-40k gate and this one does not. |
| Orchestration status | **+4** | ✅ **None detected, and affirmatively so.** Three live payment-config endpoints return three independently-configured stacks; Korea runs two more on entirely different platforms. An orchestration layer would normalise them. Nothing does. |
| 3+ countries | **+3** | ✅ Korea, US, Japan, Greater China, EMEA, ASEAN, India — segment-reported. Plus Brazil and South Africa entering. |
| Multiple PSPs | **+3** | ✅ **Four named:** KG Inicis (Korea), Eximbay (cross-border), PayPal (cross-border + West), Shopify Payments (per-brand West/JP). A fifth is unidentified behind Cafe24. |
| Local rail or licensing gap in a top-3 market | **0** | ❌ **Honestly not met.** Korea is the #1 market at 55.2%, and the Korean rails that matter are **present** — KakaoPay, Naver Pay, card instalments (무이자 할부) and bank transfer (무통장입금) are all confirmed on amoremall.com. The wallet gap in 3C is real but it is an *asymmetry*, not an absent dominant rail. **Not awarding points for a gap that isn't there.** |
| Recent expansion | **+2** | ✅ **Brazil and South Africa** named as cross-border entries in the 1Q26 deck; IOPE launched in the Americas; Aestura entering Europe and Sephora. |
| Payment issues reported | **0** | ⬜ Not researched. No complaint corpus established. |
| Funding >$10M | **0** | ❌ KRX-listed. No round. |
| High traffic outside home | **+2** | ✅ **Domestic is 55.2% of revenue, below the 60% threshold**, with overseas at 43.8% and growing faster. ⚠️ **Basis is audited segment revenue, not traffic** — no traffic data exists for this account. The YesStyle file set the precedent for using audited revenue where it is the better source. |
| Competitor using orchestration | **0** | ❌ None confirmed. |
| Payment job postings | **0** | ⬜ None found. |

**Tier: 17 / 29 → ⭐ High Priority.** No analyst override applied.

> **The override was considered and rejected, in the downward direction.** The matrix allows scoring down when *"absolute volume is too small — a high percentage score on a company with negligible transaction volume is a false positive."* That is the obvious risk here, given the whole top of this file argues the addressable estate is a fraction of the headline. **But low single-digit percent of US$3.1bn is still roughly US$60–150m of own-checkout volume**, which is comparable to other accounts in this pipeline and is not negligible. So the score stands.
>
> **What must not happen is a volume-led pitch.** The score is earned on fragmentation, market count, provider count and expansion — not on size. Read the warning at the top of the file before drafting.

---

### Section 3B. Orchestrator check → **NONE DETECTED (affirmative)**

Verified by me on 2026-09-18 by fetching `/payments/config` on three of their live storefronts:

| Storefront | shopId | Apple Pay | Shop Pay | Google Pay | PayPal |
|---|---|---|---|---|---|
| **global.amoremall.com** | 62092247178 | `null` | `null` | `null` | ✅ present |
| **us.laneige.com** | 25501892660 | ✅ present | ✅ present | ✅ present | ✅ present |
| **us.sulwhasoo.com** | 24983994413 | ✅ present | ✅ present | ✅ present | ✅ present |

**Three different shop IDs, three independently-configured payment stacks.** `us.laneige.com` carries `applePayConfig.shopifyPaymentsEnabled = true` and a `googlePayConfig` whose `iframeSrc` points at `checkout.shopify.com/25501892660/...`, i.e. a direct Shopify binding, not an orchestrator-issued token. Add the in-house Korean mall on KG Inicis and the Cafe24-hosted Korean brand sites, and that is **five platforms and at least four providers with no shared layer, no shared vault and no shared reporting.**

### Section 3C. ⭐ The wallet asymmetry — found in their own config, and better than it first looks

`global.amoremall.com/payments/config` returns, verbatim:

```
"applePayConfig": null, "shopifyPayConfig": null, "googlePayConfig": null,
"amazonPayCv2Config": null,
"paypalConfig": { "merchantId": "4WTQVJTHH2X7N", "environment": "production", ... },
"dynamicCheckoutPrioritization": ["ApplePay","ShopifyPay","PayPal","AmazonPayCv2","GooglePay"]
```

**Read the last line against the first.** The storefront's own checkout prioritisation ranks **Apple Pay first and Shop Pay second — and both are `null`.** The configuration expresses an intent the merchant account cannot fulfil: it is set up to lead with wallets that are not enabled, so the flow falls through to PayPal.

**This is the cross-border mall.** It is the storefront serving Korea cross-border, China, Malaysia, Hong Kong, the Philippines, Indonesia and now Brazil and South Africa — presenting in **USD** — and it is the one estate with **no wallet at all**, while `us.laneige.com` and `us.sulwhasoo.com` carry Apple Pay, Google Pay and Shop Pay across six card networks (visa, masterCard, amex, discover, elo, jcb).

> **The one-sentence version for outreach:** *your US brand stores lead with Apple Pay, Google Pay and Shop Pay; your cross-border mall is configured to lead with Apple Pay and Shop Pay too, but neither is switched on.* Both halves come from their own endpoints. Neither is arguable.

### Section 4. Local payment methods — own checkouts only

**global.amoremall.com**, verbatim from their FAQ: *"All region Global Credit Card: VISA, Master, JCB, AMEX, Uionpay [sic] / **Korea:** Local Credit card issued in South Korea, **Kakao Pay, Naver Pay, Payco** / **China: Alipay, WeChat** / **Malaysia: FPX** / **Southeast Asia: Alipay+, DANA** (Indonesia), **Alipay HK**, **GCash** (Philippines), **Touch'n Go** (Malaysia)"*. Footer badges add **PayPal and Klarna**.

**amoremall.com (Korea):** KakaoPay, Naver Pay (`npay.amorepacificmall.com` resolves), **card instalments (무이자 할부)**, **bank transfer (무통장입금)** under KG Inicis escrow. **Payco confirmed cross-border but NOT on the Korean mall.** Apple Pay and Google Pay **not found** on either Korean or global mall.

**US/JP brand stores:** Visa, Mastercard, Amex, Discover, PayPal, Apple Pay, Google Pay, Shop Pay, **Afterpay**.

❌ **Samsung Pay not found anywhere.** ⚠️ **Toss** appears only as a cashback promotion on the Korean mall — treat as *inferred tender, not confirmed*, and do not assert Toss Payments as a PG.

### Source Notes
- ✅ **The three `/payments/config` endpoints were fetched and parsed by me today.** The wallet asymmetry, the shop IDs, the `dynamicCheckoutPrioritization` array and the USD currency on the global mall are all first-hand.
- ✅ **KG Inicis** proven from Amorepacific's own Korean footer escrow disclosure; **Eximbay + PayPal** proven from `global.amoremall.com/pages/faqs` (*"refund the product amount by PayPal or Eximbay(Payment Gateway)"*).
- ✅ **All IR figures come from Amorepacific's own fetched PDFs and press releases**, not from aggregators.
- 📌 **One correction to the agent report.** It stated `"shopifyPaymentsEnabled": true` as a top-level field on the US stores. It is not — it is **nested inside `applePayConfig`**. The claim is right, the location was wrong, and I verified the corrected version myself. Also: I could **not** confirm the reported `supports3DS` flag under `applePayConfig` — that key is absent in the current response, so **do not assert 3DS on these storefronts**.
- ⚠️ **The FY2025 Amorepacific Corp figures are reported in 억원 (KRW 100m)** and were rescaled to KRW 4.2528tn. Arithmetic cross-checks against FY2024 (3.8851tn × 1.09 ≈ 4.235tn). **Re-verify before quoting a revenue number in an email.**
- ⚠️ **The April-2025 "Amorepacific Holdings Corp." rename is aggregator-only and is contradicted** by the company's own Feb-2026 release headed *"Amorepacific Group 2025 Earnings Summary"*. **Do not use the Holdings name.**
- ❌ **"Over 40% of global sales from e-commerce" appeared in a search synthesis and could not be found in any IR document. Do not use it.** Even if true it counts marketplaces as e-commerce, so it would not support a DTC claim.
- ❌ **COSRX deal terms** (38.4% → ~93.2%, KRW 755.1bn, Oct 2023) are search-summary only. The **consolidation itself** is first-party confirmed via the IR PDFs.
- ❌ **No DTC revenue figure exists in any market, at any date.** This is the gap that decides how big the account really is.

### Manual Research Recommendations
> **1. Get a DTC revenue or order figure on the call.** Everything about sizing this account depends on it and nothing public answers it.
> **2. Establish the PG behind the Cafe24 Korean brand sites** — the one estate of five with no identified provider.
> **3. Ask why the global mall has no wallets** when the US stores lead with three. That question is the whole opening.
> **4. Confirm whether Amazon, Sephora, Tmall, Qoo10, TikTok Shop and Shopee volume is genuinely out of scope**, or whether any of it settles back through an Amorepacific entity.

---

## Executive Summary

Amorepacific is a KRW 4.25tn Korean cosmetics group whose revenue runs overwhelmingly through channels it does not own — **Naver, Kakao, Coupang, Olive Young, Amazon, Sephora, Tmall, Qoo10, TikTok Shop, Shopee**, department-store concessions and travel retail. Its own direct-to-consumer estate is small and completely undisclosed in size, but it is **fragmented into five platforms and at least four payment providers with nothing shared between them**: an in-house Korean mall on **KG Inicis**, Korean brand sites on **Cafe24**, a cross-border mall on Shopify running **PayPal and Eximbay**, and a set of Western and Japanese brand stores each on **its own separate Shopify Payments account**. I verified that fragmentation directly from three live payment-config endpoints, which also surfaced the sharpest observation in the file: **the cross-border mall is configured to lead checkout with Apple Pay and Shop Pay, and has both switched off**, while the US stores carry all three wallets. The motion is **greenfield** and the score is **17/29 ⭐** — but it is earned entirely on fragmentation, market count and expansion, **never on volume**, and any sequence that implies otherwise will not survive a reply.

</details>
