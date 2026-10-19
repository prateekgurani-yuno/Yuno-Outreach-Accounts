# Razer

**Status:** 🟡 Research complete — outreach not yet generated · ⚠️ **Phase 0 flag: group owns a PSP (Fiuu). Partnerships check required before any sequence runs**
**ICP Score:** 20 / 29 → ⭐ High Priority computed → **analyst override DOWN to 🟢 Medium** (see ICP breakdown)
**Industry:** Gaming hardware and peripherals, sold D2C through RazerStore Online (razer.com), plus Razer Gold virtual credits and Fiuu (payments subsidiary) · **HQ:** Dual HQ in Singapore (1 one-north Crescent) and Irvine, CA. Parent Razer Inc. is a Cayman Islands company · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** **Greenfield on razer.com, with a structural catch.** The store runs a single card acquirer (Worldpay) across all 15 configured storefronts and has no orchestration layer. However, Razer's own 81%-owned subsidiary Fiuu is a Southeast Asian acquirer and gateway. The obvious internal answer to the APAC rail gap below is "plug in Fiuu", not "buy an orchestrator".

---

> ## 🎯 THE HOOK: Razer's payments arm sells FPX and PromptPay, but razer.com doesn't offer them
>
> Malaysia (10.6%) and Thailand (8.4%) are razer.com's #2 and #3 traffic markets. Neither has its own storefront: `/my-en` and `/th-en` return 404. Both are served by a shared **"Razer AP-EN Base Store"** (MY, TH, PH, NZ) whose configured payment modes are **only** `apple-pay`, `google-pay`, `worldpay-apen-cc`, `paypal-apen` and a rewards-redemption mode. There is **no FPX, DuitNow, Touch 'n Go, PromptPay or TrueMoney**. Source: the storefront config embedded in razer.com page source, retrieved 2026-10-19.
>
> Meanwhile Razer Merchant Services, now Fiuu, won PayNet's **"Best Non-Bank FPX Acquirer"** award ([razer.com newsroom](https://www.razer.com/newsroom/company-news/razer-merchant-services-bags-best-non-bank-fpx-acquirer-award-by-paynet-for-industry-leading-growth)) and markets "over 110 payment methods" across SEA ([razer.com newsroom, 2024-03-08](https://www.razer.com/newsroom/company-news/razers-fintech-arm-rebrands-as-fiuu)).
>
> **Why this is a hook and also a risk:** it proves the gap is real, and it proves the gap is not a capability problem. Razer has the rails in-house and hasn't wired them to its own store. That is either an opening (the hardware e-commerce team runs on a separate, Worldpay-only SAP Commerce stack and may not want to depend on a sister company) or a dead end (they'll just connect Fiuu). **Find out which before writing a sequence.**

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Razer designs and sells gaming peripherals (mice, keyboards, headsets) and Blade laptops. It sells through retail and its own RazerStore Online. It also runs Razer Gold (virtual credits for game top-ups) and owns 81% of Fiuu, formerly Razer Merchant Services/MOLPay, a Southeast Asian payment processor. Last audited revenue was **US$1,619.6M (FY2021), 89.7% of it hardware**. Razer went private in 2022 and has published no figures since ([AR2021, HKEX](https://www1.hkexnews.hk/listedco/listconews/sehk/2022/0427/2022042702636.pdf)).

**SimilarWeb total visits (last full month):** ≈8.63M/month (razer.com, Jul–Sep 2026 average; 25.89M over 3 months). Source: SimilarWeb (supplied 2026-10-19), `accounts/traffic/razer.md`. **Caveats from the supplied file:**
- It is the Sales Intelligence view: top 10 countries only, by share, with no per-country visit counts. Per-country figures below are derived.
- It counts desktop and mobile web only; app traffic is excluded.
- Razer Gold and Razer Pay flows are not fully reflected, so treat any volume sizing from it as a floor.
- It is a single domain, razer.com.

### Top 5 markets
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|------|---------|---------|------------------|-----------------|--------------|
| 1 | 🇺🇸 United States *(out of territory)* | 20.83% | Worldpay cards, PayPal, PayPal Pay Later, Affirm, Apple Pay, Google Pay, Razer Gift Card | Not assessed: out of territory | ✅ Razer USA Ltd. |
| 2 | 🇲🇾 **Malaysia** | 10.63% | Worldpay cards, PayPal, Apple Pay, Google Pay (shared AP-EN store) | **FPX, DuitNow, Touch 'n Go, Boost, GrabPay, instalments** | ⚠️ Group entities exist (Fiuu/RMS, Razer Gold, MOL AccessPortal). **No razer.com selling entity or storefront for MY** |
| 3 | 🇹🇭 **Thailand** | 8.42% | Worldpay cards, PayPal, Apple Pay, Google Pay (shared AP-EN store) | **PromptPay, TrueMoney, Thai card instalments** | ⚠️ Razer (Thailand) Co., Ltd. and MOL Payment Co., Ltd. exist. Neither is named as a razer.com seller |
| 4 | 🇩🇪 Germany *(out of territory)* | 3.93% | Worldpay cards, PayPal, Klarna, Apple Pay, Google Pay | Not assessed | ✅ Razer (Europe) GmbH |
| 5 | 🇬🇧 UK *(out of territory)* | 3.86% | Worldpay cards, PayPal, PayPal Credit, Klarna, Apple Pay, Google Pay | Not assessed | ⚠️ No UK entity confirmed |

### Other in-territory markets
| Market | Traffic | Methods | Missing | Entity |
|---|---|---|---|---|
| 🇨🇳 China | 3.29% | **No razer.com store** (`/cn` 404). Traffic is non-transacting on razer.com | n/a | ❌ None confirmed |
| 🇸🇬 Singapore | 2.14% | Worldpay cards, PayPal, Apple Pay, Google Pay, split tender | **PayNow, GrabPay, Atome** | ✅ Razer (Asia-Pacific) Pte. Ltd., Razer Online Pte. Ltd. |
| 🇯🇵🇰🇷🇹🇼🇭🇰🇦🇺 JP / KR / TW / HK / AU | Not in top 10 | Cards (Worldpay), PayPal, Apple/Google Pay. AU also has PayPal Credit | konbini/PayPay (JP), local wallets (KR), JKOPay (TW), FPS/Octopus (HK), Afterpay/PayTo (AU) | Razer Korea LLC and Razer Taiwan Co., Ltd. exist (AR2021) |

### Legal entities
- Razer Inc. (Cayman Islands), the parent ([AR2021](https://www1.hkexnews.hk/listedco/listconews/sehk/2022/0427/2022042702636.pdf))
- Razer (Asia-Pacific) Pte. Ltd. (Singapore). Paid-up SGD 432.0M. Named seller in razer.com Terms of Sale
- Razer Online Pte. Ltd. (Singapore). Virtual credits; named seller in Terms of Sale
- Razer USA Ltd. (Delaware/Irvine). Named seller in Terms of Sale
- Razer (Europe) GmbH (Hamburg). Named seller in Terms of Sale
- Razer Merchant Services Sdn. Bhd. (Malaysia), 81%. **Payment, clearing and settlement (Fiuu)**
- MOL Payment Co., Ltd. (Thailand); Razer (Thailand) Co., Ltd.; Razer Taiwan Co., Ltd.; Razer Korea LLC; Razer Gold (SG) Pte. Ltd.; Razer Merchant Services (SG/Taiwan/PH) entities
- Registration numbers: not found

### Known PSPs (razer.com store)
- **Worldpay**: `[Source Code]`. Configured as `"paymentProvider":"Worldpay"` in all 15 storefronts (`worldpay-{us,ca,uk,de,fr,es,it,eu,au,sg,hk,jp,kr,tw,apen}-cc`). US description: *"Your credit card payments are secured in the US with WorldPay"*. Covers all markets.
- **PayPal** (+ PayPal Pay Later / Credit): `[Source Code]`, all stores
- **Klarna**: `[Source Code]`, UK/DE/FR/ES/IT
- **Affirm**: `[Source Code]` + financing page, US/CA
- **Apple Pay / Google Pay**: `[Source Code]`, all stores
- **Forter** (fraud, not a PSP): `[Terms/Privacy Policy]`. *"If your payment information does not satisfy Forter's criteria, the payment request will be declined"* ([privacy policy](https://www.razer.com/legal/customer-privacy-policy), last modified 2026-09-28)
- **Not used on razer.com:** Fiuu/RMS/MOLPay, Adyen, Stripe, Braintree, Cybersource, Checkout.com. None found in the config.

### Orchestration status
**None detected on razer.com: a single card acquirer (Worldpay) with wallet and BNPL add-ons wired directly into the SAP Commerce storefront config.** No Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails or Yuno found. The `apac-tal.csv` value "In-house Routing" is **not supported** for razer.com. It may describe Fiuu or Razer Gold, which are themselves routing platforms, but no source was found.

### Buying signals
- 💼 Razer advertised a **"Channels & Payments Sales Analyst"** role covering payment-method optimisation, conversion and fraud ([hitmarker](https://hitmarker.net/jobs/razer-channels-payments-sales-analyst-830751)). **Posting date unknown.**
- 🤝 Razer Gold received **in-principle MAS approval for a Major Payment Institution licence** covering merchant acquisition and e-money ([razer.com newsroom, 2024-11-05](https://www.razer.com/newsroom/company-news/razer-gold-receives-in-principal-approval-letter-for-major-payment-institution-licence)). This deepens the group's in-house payments capability, which is a headwind rather than a signal for us.
- 📉 Razer **pulled Blade laptops from the US razer.com store from 2 April 2025**, during the tariff shock ([Tom's Hardware](https://www.tomshardware.com/laptops/razer-halts-laptop-sales-to-us-consumers-this-response-to-us-tariffs-could-become-commonplace)). This is a contraction signal, and it is not known whether sales have resumed.
- No funding, RFP or market launch found in the last 12 months.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach razer` to draft the 12-touch sequence,
or call this from `/prepare_batch`.*

**Hold:** resolve the Phase 0 flag first (see Manual Research Recommendations #1).

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 20 / 29
| Signal | Points | Status |
|--------|--------|--------|
| Monthly transaction count | +3 | ⚠️ **NOT FOUND — ASSUMED ~60,000/month. [ASSUMPTION — not researched.]** Basis: 8.63M avg monthly web visits (supplied) × an assumed 0.5–1.0% e-commerce conversion gives ~43k–86k orders/month; midpoint ~60k. The billing unit is one razer.com order. Neither the conversion rate nor razer.com's share of Razer's hardware revenue is sourced, so this cannot reject or confirm the account. Razer Gold top-ups are a separate business and are excluded. |
| Orchestration status | +4 | ✅ None detected on razer.com. A single Worldpay acquirer across 15 stores (`[Source Code]`). **Caveat:** the group owns a PSP, so this is not greenfield in spirit. |
| 3+ countries | +3 | ✅ US 20.83%, MY 10.63%, TH 8.42%, DE 3.93%, UK 3.86% and more all exceed 1% (supplied) |
| Multiple PSPs | +3 | ✅ Worldpay (cards) + PayPal in all stores, plus Klarna (EU/UK) and Affirm (US/CA) (`[Source Code]`). **Caveat:** config entries carry `isProduction:false`. This is likely a config flag, but no live checkout was walked. |
| Local rail or licensing gap in a top-3 market | +3 | ✅ Malaysia (#2) has no FPX/DuitNow/TNG and Thailand (#3) has no PromptPay/TrueMoney in the AP-EN store config, which is the complete list of configured payment modes |
| Recent expansion | 0 | ❌ None found in the last 12 months. The US laptop sales halt (Apr 2025) points the other way. |
| Payment issues reported | +2 | ✅ Moderate. A repeated cluster of "order cancelled / unsuccessful after payment" threads on Razer Insider (2020–2025, most dates unverified), consistent with Forter-driven declines. Razer Gold top-up complaints are a separate product and are **not counted**. |
| Funding >$10M | 0 | ❌ None found (private since 2022) |
| High traffic outside home | +2 | ✅ Singapore (HQ) is 2.14% of traffic. Even counting the US as home (dual HQ), it is 20.83% |
| Competitor using orchestration | 0 | ❌ None found for Logitech, Corsair, Secretlab, ASUS, Lenovo |
| Payment job postings | 0 | ⬜ "Channels & Payments Sales Analyst" exists but is undated; other payments roles look like Fiuu/Razer Gold roles |

**Computed tier:** 20 → ⭐ High Priority.

**ANALYST OVERRIDE — DOWN to 🟢 Medium.** Reasoning, in full:
1. **Phase 0 gate partially fires.** CLAUDE.md excludes PSPs and payment-infrastructure companies. Razer Inc. owns 81% of Razer Merchant Services Sdn. Bhd. ("payment, clearing and settlement", AR2021 Note 15), operating as Fiuu, *"a standalone subsidiary of Razer Inc."* and *"one of the largest payment processors in Southeast Asia"* with TPV over US$6.6B in FY2023 ([newsroom](https://www.razer.com/newsroom/company-news/razers-fintech-arm-rebrands-as-fiuu)). Razer Gold is pursuing MAS merchant-acquisition licensing. Unlike Grab (rejected to `not-icp/`), the payments business is a **minority of group revenue**: Software & Services was 10.0% of FY2021 revenue and hardware 89.7% (AR2021). Fiuu also does **not** process razer.com. So the merchant side looks separable, but that is a Partnerships call, not an SDR one.
2. **Regulatory and organisational reality blunts the strongest signal.** The 3-point rail gap is in exactly the two markets (MY, TH) where Razer owns acquiring capability. The natural internal fix is Fiuu, not Yuno.
3. **The matrix double-counts the store config.** "Multiple PSPs", "Orchestration none" and "Rail gap" all come from one config blob, unverified by a live checkout.
4. **Volume is assumed.** The +3 rests on an unsourced conversion rate.

If Partnerships clears it and the e-commerce team confirms they own their own stack, restore ⭐. If Partnerships objects, run `/mark_not_icp Razer`.

### Source Notes
- ✅ Worldpay is the card provider in all 15 storefronts. Verified directly in razer.com page source (`/legal/customer-privacy-policy`, `/`, `/store/financing`), 2026-10-19
- ✅ AP-EN Base Store (MY/TH/PH/NZ) payment modes are Apple Pay, Google Pay, Worldpay card, PayPal and redemption only. Verified in page source
- ✅ Forter declines payments that fail its criteria. Quoted from the [privacy policy](https://www.razer.com/legal/customer-privacy-policy)
- ✅ Sellers named in the [Terms of Sale](https://www.razer.com/legal/terms-of-sale) (last modified 2025-04-14): Razer (Asia-Pacific) Pte. Ltd. / Razer USA Ltd. / Razer (Europe) GmbH / Razer Online Pte. Ltd., listed together with no mapping to regions
- ✅ FY2021 revenue of US$1,619.6M and the regional split. Verified in AR2021 text
- ✅ The RMS stake went from 51% to 81%. Verified in AR2021 text
- ⚠️ Fiuu 2025 TPV of US$13B and 960M+ transactions: [Business Today MY](https://www.businesstoday.com.my/2026/03/24/fiuus-total-payment-volume-hits-us13-billion-in-2025/) `[UNVERIFIED — search summary only, page 403]`
- ⚠️ Whether Razer Gold's final MPI licence was granted (vs. in-principle approval in Nov 2024) is not confirmed
- ⚠️ All payment-mode entries carry `"isProduction":false` and `"supports3DS":false`. The meaning is unverified; it could be a config default
- ⚠️ `apac-tal.csv` "In-house Routing" for Razer: not confirmed for razer.com

### Success Case Alternatives
- **inDrive** — multi-country scale: 50+ countries, ~90% approval, ten new countries in under eight months ([y.uno](https://y.uno/en/success-stories/indrive)). The closest match to a 15-storefront, single-acquirer retailer; it is not a hardware or gaming case. Use it only as a pattern match for "one integration, many markets".
- **Livelo** — use only if discovery confirms the false-decline pattern (Forter + single acquirer, no retry path) ([y.uno](https://y.uno/en/success-stories/livelo)). Nothing in this research quantifies Razer's decline rate.
- There is no named Yuno consumer-electronics case in the repo. Do not imply one.

---

## Executive Summary

Razer is a Singapore/Irvine gaming hardware brand (FY2021 revenue US$1.62B, 89.7% hardware; private since 2022) selling D2C through razer.com, which runs **one card acquirer (Worldpay) across 15 storefronts** with PayPal, Klarna, Affirm and Apple/Google Pay layered on. It has no orchestration layer, Forter screening in front, and **no local rails in any APAC store**. Malaysia and Thailand, its #2 and #3 web markets, are lumped into a shared AP-EN store accepting only cards, PayPal and wallets. The catch: Razer owns 81% of **Fiuu**, a Southeast Asian acquirer that offers exactly those missing rails. That makes this a **Phase 0 / Partnerships question first** and a greenfield sales motion only if the hardware e-commerce stack is run independently of Fiuu.

---

### Section 1: Website Traffic Analysis by Country

**Data source:** Path 1, pasted SimilarWeb data. *SimilarWeb Sales Intelligence (supplied 2026-10-19), `accounts/traffic/razer.md`.* Period Jul–Sep 2026, worldwide, desktop + mobile web. Domain: razer.com only. Avg monthly visits 8.630M. Device split 55.09% desktop / 44.91% mobile web. Global rank not captured.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|------|---------|-------------------|---------------------|-------|--------|
| 1 | United States | 20.83% | ~1.80M `[DERIVED from supplied share, not a SimilarWeb figure]` | Not supplied | SimilarWeb (supplied 2026-10-19) |
| 2 | **Malaysia** | 10.63% | ~0.92M `[DERIVED]` | Not supplied | same |
| 3 | **Thailand** | 8.42% | ~0.73M `[DERIVED]` | Not supplied | same |
| 4 | Germany | 3.93% | ~0.34M `[DERIVED]` | Not supplied | same |
| 5 | United Kingdom | 3.86% | ~0.33M `[DERIVED]` | Not supplied | same |
| 6 | China | 3.29% | ~0.28M `[DERIVED]` | Not supplied | same |
| 7 | Russia | 2.58% | ~0.22M `[DERIVED]` | Not supplied | same |
| 8 | Canada | 2.56% | ~0.22M `[DERIVED]` | Not supplied | same |
| 9 | France | 2.23% | ~0.19M `[DERIVED]` | Not supplied | same |
| 10 | Singapore | 2.14% | ~0.18M `[DERIVED]` | Not supplied | same |

The top 10 cover 60.47% of traffic; the other 39.53% is unlisted, so JP, KR, TW, HK, AU, PH and ID shares are unknown.

**High-priority markets (>5%):** US, Malaysia, Thailand.

**Caveats (from the supplied file, carried forward):**
1. This is the Sales Intelligence view: top 10 only, with no per-country visit counts. Every visit figure above is share × 8.630M, labelled derived.
2. Single domain only. No regional razer.com variants or other domains were supplied.
3. Mobile app traffic is excluded.
4. Razer Gold top-ups and Razer Pay flows are not fully in razer.com web traffic, so treat web-based volume sizing as a floor.
5. **Added in this run:** China (3.29%) and Russia (2.58%) have **no razer.com storefront** (`/cn`, `/ru-ru` return 404; no CN/RU store in the config). Their traffic cannot transact on razer.com, so the transacting web audience is smaller than 8.63M.

**Top-10 markets without a confirmed local entity** (cross-ref Section 2): Malaysia and Thailand (no razer.com seller; group entities exist), UK, China, Russia, Canada, France.

---

### Section 2: Legal Entities & Local Presence

**Headquarters:** Dual HQ at 1 one-north Crescent #02-01, Singapore 138538 and 9 Pasteur, Suite 100, Irvine, CA 92618. Founded 2005. Parent Razer Inc. is incorporated in the Cayman Islands (registered office Ugland House) ([AR2021, Note 1](https://www1.hkexnews.hk/listedco/listconews/sehk/2022/0427/2022042702636.pdf)). Taken private in 2022 at HK$2.82/share; 94.74% of disinterested votes approved on 26 Apr 2022 ([Vulcan Post](https://vulcanpost.com/786487/shareholders-approve-razer-privatisation-deal-singapore)).

| Country | Entity Name | Registration # | Source |
|---------|-------------|----------------|--------|
| Cayman Islands | Razer Inc. (parent) | Not found | AR2021 Note 1 |
| Singapore | Razer (Asia-Pacific) Pte. Ltd. (100%; paid-up SGD 432.0M; razer.com seller) | Not found | AR2021 Note 15; [Terms of Sale](https://www.razer.com/legal/terms-of-sale) |
| Singapore | Razer Online Pte. Ltd. (software and virtual credits; razer.com seller) | Not found | AR2021; Terms of Sale |
| Singapore | Razer Gold (SG) Pte. Ltd.; Razer Fintech Holdings Pte. Ltd.; Razer Merchant Services (SG) Pte. Ltd. | Not found | AR2021 (directors' bios) |
| USA | Razer USA Ltd. (Delaware; Irvine and San Francisco; razer.com seller) | Not found | AR2021; Terms of Sale |
| Germany | Razer (Europe) GmbH (Hamburg; razer.com seller) | Not found | AR2021; Terms of Sale |
| Malaysia | Razer Merchant Services Sdn. Bhd. (81%; payment, clearing and settlement, i.e. Fiuu); RMS Reloads Sdn. Bhd.; MOL AccessPortal Sdn. Bhd.; Razer Gold Sdn. Bhd.; Razer Fintech (M) Sdn. Bhd. | Not found | AR2021 Note 15 + bios |
| Thailand | MOL Payment Co., Ltd. (100%); Razer (Thailand) Co., Ltd.; e-Innovations Systems & Networks Thai Co., Ltd. | Not found | AR2021 |
| Taiwan | Razer Taiwan Co., Ltd.; Razer Merchant Services (Taiwan) Corp. | Not found | AR2021 |
| Korea | Razer Korea LLC | Not found | AR2021 |
| Philippines | RMS Reloads (Philippines) Inc.; Razer Merchant Services (PH) Inc. | Not found | AR2021 |

The Terms of Sale name four sellers together and do not say which one bills which region. The AR2021 entity list is FY2021 and may be out of date.

**Cross-Border Gap Analysis:**

| Country | In Top 10 Traffic? | Has Local Entity? | Domestic acquiring gated? | Cross-Border Risk? |
|---------|-------------------|-------------------|---------------------------|---------------------|
| United States | Yes (#1) | ✅ Razer USA Ltd. | n/a (out of territory) | Low |
| Malaysia | Yes (#2) | ⚠️ Group entities, none named as razer.com seller | Not verified this run | **Possible**: shared AP-EN store with a single `worldpay-apen-cc` mode; the acquiring location is unknown |
| Thailand | Yes (#3) | ⚠️ Razer (Thailand) Co., Ltd. exists, not named as seller | Not verified this run | **Possible**: same AP-EN store |
| Germany | Yes (#4) | ✅ Razer (Europe) GmbH | n/a | Low |
| UK | Yes (#5) | ❌ Not confirmed | n/a | Unknown |
| China | Yes (#6) | ❌ None confirmed | n/a | No razer.com store; not transacting |
| Russia | Yes (#7) | ❌ None | n/a | No razer.com store |
| Canada | Yes (#8) | ❌ Not confirmed | n/a | Unknown |
| France | Yes (#9) | ❌ Not confirmed (EU via GmbH likely, not confirmed) | n/a | Unknown |
| Singapore | Yes (#10) | ✅ | No | Low |

> *Warning: Potential cross-border operation in Malaysia and Thailand. No local razer.com storefront or named selling entity was found; both are served by a shared "AP-EN" store whose single card mode (`worldpay-apen-cc`) covers MY, TH, PH and NZ. Where Worldpay acquires these transactions is not public. If it is outside MY/TH, transactions are cross-border, with higher scheme costs, lower approval rates and FX exposure.* `[INFERENCE, not confirmed]`

No regulatory gate claim is made. Malaysian and Thai acquiring rules were not verified in this run.

> **MANUAL:** Place a test order from a Malaysian IP/address and check the currency shown (the AP-EN config carries MYR loyalty tiers and NZD currency entries), the billing descriptor and the seller entity on the invoice.

---

### Section 3: Payment Providers & Payment Stack

#### 3A. PSPs & Acquirers

| Country/Region | PSP/Acquirer | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| All 15 storefronts (US, CA, UK, EU, DE, FR, ES, IT, AU, SG, HK, JP, KR, TW, AP-EN) | **Worldpay** (cards) | `[Source Code]` | Storefront config in https://www.razer.com/legal/customer-privacy-policy, https://www.razer.com/ (retrieved 2026-10-19) |
| All stores | PayPal (+ Pay Later / Credit in US, UK, FR, ES, IT, AU) | `[Source Code]` | same |
| UK, DE, FR, ES, IT | Klarna | `[Source Code]` | same |
| US, CA | Affirm | `[Source Code]` + financing page | https://www.razer.com/store/financing |
| All stores | Apple Pay, Google Pay | `[Source Code]` | same |
| US | Razer Gift Card ("RGC", $500 daily limit) | `[Source Code]` | same |
| All stores | Forter (fraud screening, not a PSP) | `[Terms/Privacy Policy]` | https://www.razer.com/legal/customer-privacy-policy |
| Razer Gold (historical) | Worldpay, selected in 2017 for virtual credits incl. Alipay | `[Press Release]` | https://thepaypers.com/online-payments/razer-worldpay-to-streamline-online-payments--770816 |

**Not found on razer.com:** Fiuu/RMS/MOLPay, Adyen, Stripe, Braintree, Cybersource, Checkout.com, 2C2P, iPay88, Omise.

**Group-level PSP (context, not a vendor to razer.com):** Fiuu, formerly Razer Fintech + Razer Merchant Services. It was rebranded on 2024-03-08 as a standalone subsidiary of Razer Inc., with Eng Sheng Guan as CEO from 1 March 2024 ([newsroom](https://www.razer.com/newsroom/company-news/razers-fintech-arm-rebrands-as-fiuu); [FinTech Futures](https://www.fintechfutures.com/fintech/razer-fintech-and-razer-merchant-services-rebranded-to-form-standalone-subsidiary-fiuu)). Fiuu holds a Mastercard direct acquiring licence ([fiuu.com](https://fiuu.com/blog/detail/fiuu-razer-merchant-services-obtains-mastercards-acquiring-licence)) and JCB direct acquiring for MY/SG/PH ([The Asian Banker](https://www.theasianbanker.com/press-releases/fiuu-becomes-jcb-direct-acquirer-for-malaysia-singapore-and-the-philippines)). Razer Gold's partner portal markets a "Razer Pay Payment Gateway" to merchants ([partners.gold.razer.com](https://partners.gold.razer.com/en/product-and-services/razer-pay)).

#### 3B. Payment Orchestrator

**Classification: None detected (razer.com).** Evidence type: `[Source Code]`. The storefront config maps each store to a single `paymentProvider: "Worldpay"` for cards, with PayPal, Klarna, Affirm and wallets as separate direct modes. A `"Multi"` provider entry exists in several stores; it is most likely split-tender (gift card + card). `[INFERENCE, not confirmed]`

> *"No public evidence found of a payment orchestration platform. The company appears to integrate directly with PSP(s), which limits routing optimization, failover capabilities, and multi-acquirer strategies."*

No Juspay, Spreedly, Primer, Gr4vy, CellPoint, APEXX, Payrails or Yuno found. `apac-tal.csv` lists "In-house Routing"; this run could not confirm it for razer.com. It may refer to Fiuu or Razer Gold, which route across 100+ methods for other merchants.

> **MANUAL:** Walk a checkout with DevTools on the US and AP-EN stores. Confirm whether Worldpay is called directly (e.g. `secure.worldpay.com` / Access Worldpay) and whether any card retry or second acquirer appears.

---

### Section 4: Alternative & Local Payment Methods

Source for every "Configured" row: the razer.com storefront config retrieved 2026-10-19 from https://www.razer.com/help, https://www.razer.com/de-de/help, https://www.razer.com/legal/customer-privacy-policy. Entries carry `isProduction:false`, so read "Configured" as listed in the site config, not seen at a live checkout.

| Country/Region | Method | Category | Status | Source |
|----------------|--------|----------|--------|--------|
| US | Visa/MC/Amex/Diners via Worldpay | Cards | Configured; FAQ also lists them | razer.com/help |
| US | PayPal, PayPal Pay Later | Digital wallet / BNPL | Configured | config |
| US / CA | Affirm (0–36% APR; 0% for 24 months on purchases ≥$2,000) | BNPL/Instalments | Active (financing page) | https://www.razer.com/store/financing |
| US | Razer Gift Card | Voucher | Configured (US only) | config |
| All | Apple Pay, Google Pay | Digital wallet | Configured | config |
| **Malaysia** | Cards (Worldpay), PayPal, Apple/Google Pay | Cards / wallet | Configured (AP-EN) | config |
| **Malaysia** | FPX | Bank transfer / A2A | **Not found** | config + FAQ |
| **Malaysia** | DuitNow, Touch 'n Go, Boost, GrabPay | A2A / wallet | **Not found** | config + FAQ |
| **Malaysia** | Atome / card instalments | BNPL/Instalments | **Not found** | config + FAQ |
| **Thailand** | Cards (Worldpay), PayPal, Apple/Google Pay | Cards / wallet | Configured (AP-EN) | config |
| **Thailand** | PromptPay, TrueMoney | A2A / wallet | **Not found** | config + FAQ |
| **Thailand** | Card instalment plans | Instalments | **Not found** | config + FAQ |
| Germany | Klarna | BNPL | Configured | config |
| Germany | Giropay | Bank transfer | **Mentioned in docs only**: the DE FAQ says *"…und GiroPay. Nur Bestellungen von unter 10.000€ sind für Giropay berechtigt"* but it is not in the config. The FAQ looks stale | https://www.razer.com/de-de/help |
| UK / FR | Klarna, PayPal Credit | BNPL | Configured | config |
| China | Alipay, WeChat Pay, UnionPay | Wallet / cards | **No razer.com China store** | `/cn` 404 |
| Russia | — | — | **No razer.com Russia store** | `/ru-ru` 404 |
| Canada | Affirm, PayPal, cards | Cards / BNPL | Configured | config |
| France | Cartes Bancaires (as a named method) | Cards | Not found | config |
| **Singapore** | PayNow, GrabPay, Atome | A2A / wallet / BNPL | **Not found** | config + FAQ |
| JP / KR / TW / HK / AU | konbini, PayPay, KakaoPay/Naver Pay, JKOPay, FPS/Octopus, Afterpay/PayTo | Various | **Not found**; each store is cards, PayPal and Apple/Google Pay only (AU adds PayPal Credit) | config |
| All | Razer Gold as payment for hardware | Voucher | **Not found** as a payment mode | config |
| All | Carrier billing, crypto | — | Not found | config |

> *Warning: In Malaysia, FPX is widely used but not currently supported by razer.com.* The prominence source is Razer's own: Razer Merchant Services won PayNet's "Best Non-Bank FPX Acquirer" award ([razer.com newsroom](https://www.razer.com/newsroom/company-news/razer-merchant-services-bags-best-non-bank-fpx-acquirer-award-by-paynet-for-industry-leading-growth)). An independent FPX usage-share figure was not sourced in this run.

> *Warning: In Thailand, PromptPay is not currently supported by razer.com.* No market-share source for PromptPay was retrieved in this run; cite one before using a share figure in outreach.

**Instalments:** Affirm (US/CA) and Klarna (EU/UK) cover the West. **No instalment option exists in any APAC store**, including Blade laptops, which are high-ticket. Whether Blades are sold in the AP-EN store was not checked.

> **MANUAL:** Use a MY and a TH VPN to load razer.com/ap-en checkout with a Blade laptop in the cart. Confirm the methods shown, the currency and whether instalments appear.

---

### Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Checkout errors / false fraud declines: order cancelled after card charged | Razer Insider | Moderate (cluster of threads) | ~2023 (date from summary) | https://insider.razer.com/razer-support-45/cancelled-order-credit-card-charged-46673 |
| Charged for a cancelled order | Razer Insider | same cluster | Not dated | https://insider.razer.com/razer-support-45/charged-for-a-cancelled-order-47041 |
| "Your order was unsuccessful": PayPal authorisation voided | Razer Insider | same cluster | ~Jul 2025 `[UNVERIFIED — search summary only]` | https://insider.razer.com/razer-support-45/your-order-was-unsuccessful-why-78883 |
| Laptop order auto-cancelled three times | Razer Insider | same cluster | ~Oct 2024 `[UNVERIFIED — search summary only]` | https://insider.razer.com/razer-support-45/why-was-my-order-cancelled-60564 |
| Cancelled for "payment verification failure"; guest re-order with the same card worked | Razer Insider | same cluster | ~Jul 2020 `[UNVERIFIED — search summary only]` | https://insider.razer.com/general-discussion-6/your-razer-com-order-was-unsuccessful-13331 |
| Cancelled with no reason given | Razer Insider | same cluster | Not dated | https://insider.razer.com/razer-support-45/cancelled-order-for-no-apparent-reason-37721 · https://insider.razer.com/razer-support-45/razer-cancelled-our-order-without-notice-15444 · https://insider.razer.com/razer-support-45/transaction-cancelled-68780 |
| *Separate product:* Razer Gold top-up deducted but not credited (PayNow SG, GCash PH, cards/bank) | Razer Insider | High | Not dated | https://insider.razer.com/razer-gold-silver-20/paynow-topup-problem-two-topup-still-pending-47966 · https://insider.razer.com/razer-support-45/what-happen-to-my-top-using-gcash-50080 · https://insider.razer.com/razer-gold-silver-20/razer-gold-reload-fail-and-money-was-deducted-from-my-bank-account-and-i-didn-t-get-any-razer-gold-8399 |

No Trustpilot or Reddit hits for razer.com payments surfaced in this run. App store reviews were not checked: razer.com is web-first, and the Razer Gold app is out of scope.

> *Pattern of post-authorisation cancellations on razer.com, alongside a privacy policy stating that payments failing Forter's criteria "will be declined", suggests false declines with no secondary path (no second acquirer, no retry routing).* `[INFERENCE, not confirmed]`. No decline rate is public.

---

### Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | Jan 2026 | At CES, Razer reportedly committed ~US$600M to AI and plans 150 engineering hires `[UNVERIFIED — search summary only]` | Tech Signal | https://respawn.outlookindia.com/gaming/gaming-news/razer-focuses-on-ai-gaming-technology-invests-600-million |
| 2 | 2024-11-05 | Razer Gold received MAS in-principle approval for a Major Payment Institution licence (account issuance, domestic and cross-border transfers, merchant acquisition, e-money). It had been operating under a temporary exemption | Licence Application | https://www.razer.com/newsroom/company-news/razer-gold-receives-in-principal-approval-letter-for-major-payment-institution-licence |
| 3 | 2025-04-02 | Blade laptops were pulled from the US razer.com store amid US tariffs | Market contraction | https://www.tomshardware.com/laptops/razer-halts-laptop-sales-to-us-consumers-this-response-to-us-tariffs-could-become-commonplace · https://www.pcworld.com/article/2662097/razer-laptops-vanish-from-razers-site-as-tariffs-skyrocket.html |
| 4 | 2024-03-08 | Razer Fintech and RMS rebranded to Fiuu as a standalone subsidiary | M&A / restructuring | https://www.razer.com/newsroom/company-news/razers-fintech-arm-rebrands-as-fiuu |
| 5 | Undated | "Channels & Payments Sales Analyst" role covering payment-method optimisation, conversion and fraud | Payment Infrastructure Hiring | https://hitmarker.net/jobs/razer-channels-payments-sales-analyst-830751 |

Also found: Bloomberg via OCBJ reported CVC Capital Partners exploring a sale of its Razer stake; the article is undated relative to 2026 ([OCBJ](https://www.ocbj.com/technology/cvc-considering-possible-razer-sale-bloomberg/)). Its current status is unverified. A Senior Manager, eCommerce Sales (SG) role "owning global Razer.com revenue" was reportedly posted 2026-01-20 and is now closed `[UNVERIFIED — search summary only]` ([justpostedjobs](https://justpostedjobs.co/jobs/razer-snr-manager-ecommerce-sales-54304)).

**No public payment-related RFP found.**

---

### Section 7: Payment-Specific News

| # | Date | Headline/Summary | Relevance | Source URL |
|---|------|------------------|-----------|------------|
| 1 | 2026-03-24 | Fiuu 2025 TPV reportedly US$13B (RM54B), up 32.65%, with 960M+ transactions `[UNVERIFIED — search summary only, page 403]` | Scale of the in-house PSP | https://www.businesstoday.com.my/2026/03/24/fiuus-total-payment-volume-hits-us13-billion-in-2025/ |
| 2 | 2024-11-05 | Razer Gold received MAS MPI in-principle approval | Group payments licensing | https://www.razer.com/newsroom/company-news/razer-gold-receives-in-principal-approval-letter-for-major-payment-institution-licence |
| 3 | 2024-03-08 | Razer Fintech / RMS rebranded to Fiuu | Group PSP restructure | https://www.fintechfutures.com/fintech/razer-fintech-and-razer-merchant-services-rebranded-to-form-standalone-subsidiary-fiuu |
| 4 | 2021-09-30 | Razer Pay e-wallet and Razer Card shut down in MY and SG | Consumer wallet exit | https://ringgitplus.com/en/blog/apps/razer-pay-is-shutting-down-on-30-september.html · https://www.fintechfutures.com/paytech/razer-plans-shutdown-of-razer-pay-service-three-years-after-launch |
| 5 | Jul 2022 | TWBS became exclusive Razer Gold e-money partner for the EEA and UK | Razer Gold distribution | https://prnewswire.co.uk/news-releases/twbs-signs-exclusive-partnership-with-razer-to-bring-razer-gold-to-the-european-market-852325628.html |

> *REMOVAL: Razer discontinued its Razer Pay consumer e-wallet as of 30 September 2021. Source: https://ringgitplus.com/en/blog/apps/razer-pay-is-shutting-down-on-30-september.html.* The "Razer Pay" name now appears on a merchant gateway product on the Razer Gold partner portal.

No 2025–2026 news found about razer.com's own checkout or PSP changes.

---

### Section 8: Checkout Experience Audit

*"Full checkout flow not accessible. Findings limited to publicly observable elements"*: the storefront config in page source, help pages and the financing page.

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | Custom-built on SAP Commerce (hybris) config, Worldpay card mode | Not rated | Hosted vs. embedded card fields not observed |
| Guest checkout | Guest cart path exists; a 2020 forum thread confirms guest re-order worked | Fair | Not walked |
| Steps to complete payment | Not observed | — | — |
| Card input experience | Not observed | — | — |
| Payment methods visible | Cards, PayPal, Apple/Google Pay everywhere; Klarna (EU/UK); Affirm (US/CA) | **Poor in APAC** | No local rails in any APAC store |
| Location-based method display | Per-store method lists exist, but MY/TH/PH/NZ share one AP-EN list | Poor for SEA | — |
| Instalment / EMI options | US/CA (Affirm), EU/UK (Klarna, PayPal Credit); none in APAC | Poor in APAC | — |
| 3DS implementation | Not detected. Config flags `"supports3DS":false` on all 9 US payment entries | Unknown | Config flag meaning unverified; not proof that 3DS is off |
| PCI indicator | Not observed | — | — |
| Mobile responsiveness | 44.91% of traffic is mobile web (supplied); UX not tested | — | — |
| Multi-currency / local pricing | Per-store currencies; AP-EN carries MYR loyalty tiers and NZD entries | Unclear | Which currency MY/TH shoppers are charged in is unverified |
| Saved payment methods | Not observed | — | — |
| Error message clarity | Forum users report generic "Your order was unsuccessful" messages | Poor `[from complaints, not observed]` | — |

---

### Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Not found for razer.com. Fiuu (RMS) held a PCI DSS v4.0 Level 1 Service Provider certificate valid 2024-10-01 to 2025-09-30 (search summary; PDF not fetched) | https://fiuu.com/news/uploads/2024/Fiuu_PCI_DSS_COC.pdf |
| Card data handling | Not found | — |
| Recommended Yuno integration | SDK, assuming razer.com does not want card data in scope. Confirm in discovery | — |

*No direct PCI compliance documentation found publicly for razer.com.*

---

### Section 10: Strategic Insights & Outreach Angles

> **Insight #1: The SEA rail gap sits in Razer's own backyard**
> **Evidence:** S1 shows MY (10.63%) and TH (8.42%) are the #2 and #3 web markets. S4 shows the AP-EN store config lists no FPX, DuitNow, TNG, PromptPay or TrueMoney. S2 shows no razer.com MY/TH storefront or named selling entity.
> **Pain Point:** Nearly a fifth of razer.com's web traffic lands in a store that offers only cards, PayPal and wallets. Shoppers who pay by online banking or QR have no route.
> **Yuno Value Proposition:** Add local rails per market through one integration, alongside existing Worldpay, without re-platforming each store.
> **Best Success Case:** inDrive: one integration, many markets ([y.uno](https://y.uno/en/success-stories/indrive)). It is a pattern match only, not a hardware case.
> **Outreach Angle:** "Your MY and TH shoppers check out in a shared AP-EN store with cards, PayPal and Apple/Google Pay only, in markets where your own Fiuu team sells FPX and PromptPay to everyone else."
> **Suggested Subject Line:** "FPX on razer.com/ap-en"
> ⚠️ **Risk:** the obvious reply is "we'll use Fiuu". Position this as the e-commerce team's own decision, and do not send it before the Partnerships check.

> **Insight #2: One acquirer for 15 storefronts, behind an aggressive fraud gate**
> **Evidence:** S3A shows Worldpay as the sole card provider in every store config. S5 shows a repeated pattern of post-authorisation cancellations. S3A also shows the privacy policy stating that payments failing Forter's criteria "will be declined".
> **Pain Point:** No second acquirer or retry path. Every false decline or Worldpay outage is a lost order, including on high-ticket Blade laptops.
> **Yuno Value Proposition:** Failover and smart retries across acquirers, and decoupling fraud decisioning from a single processor.
> **Best Success Case:** Livelo, the decline-cascade case ([y.uno](https://y.uno/en/success-stories/livelo)). Use it only if discovery confirms the decline issue.
> **Outreach Angle:** "Every razer.com store, from the US to AP-EN, points cards at one acquirer. When it or the fraud screen says no, there's no second path."
> **Suggested Subject Line:** "One acquirer, fifteen stores"
> Note: most of this volume is out of territory (US/EU). Hand off or co-sell with the relevant AE if this angle lands.

> **Insight #3: Western stores get instalments, APAC stores don't**
> **Evidence:** S4 shows Affirm (US/CA) and Klarna (EU/UK) configured, and no instalment option in any APAC store. S1 shows MY and TH as top-3 markets.
> **Pain Point:** High-ticket items in SEA (laptops, chairs, bundles) have no instalment path. Whether Blades are sold in AP-EN is unverified.
> **Yuno Value Proposition:** Plug local BNPL and card-instalment rails in per market.
> **Best Success Case:** inDrive (breadth). No instalment-specific case is sourced.
> **Outreach Angle:** "A US buyer can split a Blade over 24 months with Affirm. A Malaysian buyer on razer.com sees cards and PayPal only."
> **Suggested Subject Line:** "Affirm in Irvine, nothing in KL"

---

### Quick Hits: Ready-to-Use Sales Ammunition

*Hold until the Phase 0 / Partnerships question is answered.*

**Email hooks:**
1. razer.com's Malaysia and Thailand shoppers, your #2 and #3 web markets, check out in a shared AP-EN store that offers cards, PayPal and Apple/Google Pay, with no FPX or PromptPay.
2. All 15 razer.com storefronts send cards to a single acquirer; if it, or the fraud screen in front of it, says no, the order has nowhere else to go.
3. US and EU razer.com buyers get Affirm and Klarna; no APAC store has an instalment option.

**Cold call openers:**
1. "Quick one: is the razer.com checkout run by the e-commerce team independently, or does it have to go through Fiuu for anything in Southeast Asia?"
2. "I noticed Malaysia and Thailand share one AP-EN store with no local bank or QR payments. Is that deliberate, or just where the roadmap is?"
3. "When Worldpay declines a Blade order, is there any second route today, or is it just cancelled?"

---

### Section 11: Similar Companies & Prospecting Pipeline

#### 11A. Direct Competitors

| Company | Website | HQ Country | Est. Size | Overlap Markets | Known PSP/Orchestrator | Source |
|---------|---------|------------|-----------|-----------------|------------------------|--------|
| Logitech (Logitech G) | logitechg.com | Switzerland/US | FY2026 sales $4.84B; gaming $1.41B; APAC $1.35B `[UNVERIFIED — search summary only]` | Global, APAC | Not found | https://www.sec.gov/Archives/edgar/data/0001032975/000103297526000021/logi-20260331.htm |
| Corsair | corsair.com | US | FY2025 revenue $1,472.5M `[UNVERIFIED — search summary only]` | Global | Not found | https://www.businesswire.com/news/home/20260212080218/en/Corsair-Reports-Strong-Revenue-and-Profit-Growth-for-4Q25-and-FY25 |
| Secretlab | secretlab.co | Singapore | Revenue estimates conflict; do not quote | SG, global | Atome BNPL (SG) `[UNVERIFIED — search summary only]`; card PSP not found | https://secretlab.sg/pages/atome |
| ASUS (ROG) | asus.com | Taiwan | Not researched | Global, APAC | 2C2P (SG, 2022) `[UNVERIFIED — search summary only]` | https://ibsintelligence.com/ibsi-news/asus-partners-with-2c2p-for-a-more-seamless-online-shopping-experience |
| Lenovo (Legion) | lenovo.com | China/HK | 42.54M avg monthly visits (supplied) | US, India, Japan, Indonesia | Not found | `accounts/traffic/lenovo.md` |
| SteelSeries, HyperX, Alienware, Acer Predator, MSI | — | — | Not researched (budget) | — | Not found | — |

#### 11B. Industry Peers / Same Vertical

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source |
|---------|---------|----------|-------------|-------------------------------|--------|
| Samsung | samsung.com | Consumer electronics D2C | India 29.06%, ID, TH | Multi-market D2C electronics store | `accounts/traffic/samsung.md` |
| Back Market | backmarket.com | Refurbished electronics marketplace | EU/US (out of territory) | The only electronics orchestration reference found | https://www.payplug.com/blog/payment-orchestration-back-market/ |

Other APAC peers were not researched (search budget).

#### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator Adopted | Date | Vertical | Source URL |
|---------|---------------------|------|----------|------------|
| Back Market | Multi-PSP strategy (Payplug write-up); "acceptance rate increase by 15–20%" is Payplug's summary, not a direct quote | Not dated | Refurbished electronics | https://www.payplug.com/blog/payment-orchestration-back-market/ |

*No public case studies found of direct competitors adopting payment orchestration.*

#### 11D. Prospect Scoring

Not scored. Competitor payment stacks are almost entirely unknown, and scoring on that basis would be guesswork. ASUS, Lenovo and Samsung are already in `apac-tal.csv` with blank payment columns.

#### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal | In TAL? |
|------|---------|------|-------------|-------|----------|------------|---------|
| 1 | Lenovo | Competitor/peer | US, IN, JP, ID | Not scored | — | Large multi-market D2C; traffic file exists | ✅ Yes |
| 2 | ASUS | Competitor | Global, SG | Not scored | — | 2C2P in SG (unverified) | ✅ Yes |
| 3 | Samsung | Peer | IN, ID, TH | Not scored | — | India-heavy D2C traffic | ✅ Yes |
| 4 | Secretlab | Competitor | SG, global | Not scored | — | **SG-HQ'd, global D2C, not on the list** | ❌ **No: genuine find** |
| 5 | Logitech | Competitor | Global, APAC $1.35B | Not scored | — | APAC its fastest-growing region `[UNVERIFIED]` | ❌ No |
| 6 | Corsair | Competitor | Global | Not scored | — | US-HQ'd; APAC presence unverified | ❌ No |

**Genuine find:** Secretlab is Singapore-HQ'd, sells D2C globally and is not on `apac-tal.csv`. It is worth a research run.

---

### Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | US$1,619.6M (FY2021, last audited); hardware 89.7% (Peripherals $1,084.3M, Systems $368.2M); Software & Services $162.5M | [AR2021](https://www1.hkexnews.hk/listedco/listconews/sehk/2022/0427/2022042702636.pdf). No figures since the 2022 take-private |
| Revenue by region (FY2021) | Americas $721.9M · EMEA $413.3M · APAC excl. China $300.0M · China $184.5M | AR2021 segment note |
| GMV / Gross Transaction Volume | razer.com: not found. Fiuu TPV US$6.6B+ (FY2023, newsroom); US$13B (2025) `[UNVERIFIED]` | See Section 7 |
| Average Transaction Value (USD) | Not found | — |
| Est. Annual Transactions | Not calculable (no razer.com revenue or ATV) | — |
| **Monthly transaction count** | ⚠️ **NOT FOUND — ASSUMED ~60,000/month. [ASSUMPTION — not researched.]** Basis: 8.63M monthly web visits × an assumed 0.5–1.0% conversion = ~43k–86k orders. China and Russia traffic (5.87%) cannot transact on razer.com, which shrinks the base slightly. The billing unit is one razer.com order. Razer Gold top-ups are excluded. | Assumption |
| Active Customers / Users | ~177.7M total user accounts; Razer Gold ~33.1M registered users (both at 31 Dec 2021) | AR2021 |
| Primary Currency | USD (US store); per-store local currencies | Config |
| Top 3 Markets by Revenue | FY2021: US ($673.2M within Americas $721.9M), EMEA ($413.3M), APAC excl. China ($300.0M) | AR2021 |
| Billing channel split (web vs app store) | n/a. Hardware e-commerce is web checkout; no app-store billing involved | — |

---

### Overall Research Confidence

**Medium.**
- **Strong:** the PSP stack and payment methods. Both are read directly from razer.com's own storefront config, privacy policy and Terms of Sale, and cross-checked by three agents and a direct grep.
- **Strong:** entities and FY2021 financials, from the audited annual report.
- **Weak:** anything after 2021 on revenue, any razer.com order volume, and live checkout behaviour (config is flagged `isProduction:false`; no checkout was walked).
- **Weak:** the complaint dates, which are mostly from search summaries, and competitor stacks, which are almost entirely unknown.
- **Traffic data was supplied** (SimilarWeb Sales Intelligence, 2026-10-19): top 10 only, shares only, single domain, web only.

---

### Manual Research Recommendations

> **Area:** Phase 0: Fiuu ownership vs. ICP exclusion
> **Why it matters:** CLAUDE.md routes PSPs to Partnerships. Razer owns 81% of an SEA acquirer. Pitching a rail gap that Fiuu could fill risks a political own-goal and may step on a Partnerships relationship.
> **Suggested manual action:** Ask Partnerships whether Fiuu is a current or target partner and whether Razer's merchant side is fair game. If not, run `/mark_not_icp Razer`.

> **Area:** Monthly transaction count (assumed)
> **Why it matters:** It is the only signal that can reject an account, and it is currently an assumption.
> **Suggested manual action:** Confirm razer.com order volume or D2C revenue share in discovery.

> **Area:** Live checkout in the AP-EN store
> **Why it matters:** Every method finding rests on config flagged `isProduction:false`.
> **Suggested manual action:** Walk checkout from MY and TH (VPN). Record the methods, currency, seller entity and Worldpay endpoint.

> **Area:** Who owns razer.com payments
> **Why it matters:** The whole pitch depends on the e-commerce team running its own stack rather than Fiuu deciding for it.
> **Suggested manual action:** Find the Head of eCommerce / Payments for Razer.com on LinkedIn, plus the owner of the Senior Manager, eCommerce Sales role (SG).

---

### Appendix: All Source URLs

**Traffic:** `accounts/traffic/razer.md` (SimilarWeb Sales Intelligence, supplied 2026-10-19)

**Section 2:**
- https://www1.hkexnews.hk/listedco/listconews/sehk/2022/0427/2022042702636.pdf
- https://www.razer.com/legal/terms-of-sale
- https://vulcanpost.com/786487/shareholders-approve-razer-privatisation-deal-singapore

**Section 3:**
- https://www.razer.com/legal/customer-privacy-policy
- https://www.razer.com/
- https://www.razer.com/store/financing
- https://thepaypers.com/online-payments/razer-worldpay-to-streamline-online-payments--770816
- https://www.razer.com/newsroom/company-news/razers-fintech-arm-rebrands-as-fiuu
- https://www.fintechfutures.com/fintech/razer-fintech-and-razer-merchant-services-rebranded-to-form-standalone-subsidiary-fiuu
- https://fiuu.com/blog/detail/fiuu-razer-merchant-services-obtains-mastercards-acquiring-licence
- https://www.theasianbanker.com/press-releases/fiuu-becomes-jcb-direct-acquirer-for-malaysia-singapore-and-the-philippines
- https://partners.gold.razer.com/en/product-and-services/razer-pay

**Section 4:**
- https://www.razer.com/help
- https://www.razer.com/de-de/help
- https://www.razer.com/newsroom/company-news/razer-merchant-services-bags-best-non-bank-fpx-acquirer-award-by-paynet-for-industry-leading-growth

**Section 5:**
- https://insider.razer.com/razer-support-45/cancelled-order-credit-card-charged-46673
- https://insider.razer.com/razer-support-45/charged-for-a-cancelled-order-47041
- https://insider.razer.com/razer-support-45/your-order-was-unsuccessful-why-78883
- https://insider.razer.com/razer-support-45/why-was-my-order-cancelled-60564
- https://insider.razer.com/general-discussion-6/your-razer-com-order-was-unsuccessful-13331
- https://insider.razer.com/razer-support-45/cancelled-order-for-no-apparent-reason-37721
- https://insider.razer.com/razer-support-45/razer-cancelled-our-order-without-notice-15444
- https://insider.razer.com/razer-support-45/transaction-cancelled-68780
- https://insider.razer.com/razer-gold-silver-20/paynow-topup-problem-two-topup-still-pending-47966
- https://insider.razer.com/razer-support-45/what-happen-to-my-top-using-gcash-50080
- https://insider.razer.com/razer-gold-silver-20/razer-gold-reload-fail-and-money-was-deducted-from-my-bank-account-and-i-didn-t-get-any-razer-gold-8399

**Sections 6–7:**
- https://respawn.outlookindia.com/gaming/gaming-news/razer-focuses-on-ai-gaming-technology-invests-600-million
- https://www.razer.com/newsroom/company-news/razer-gold-receives-in-principal-approval-letter-for-major-payment-institution-licence
- https://www.tomshardware.com/laptops/razer-halts-laptop-sales-to-us-consumers-this-response-to-us-tariffs-could-become-commonplace
- https://www.pcworld.com/article/2662097/razer-laptops-vanish-from-razers-site-as-tariffs-skyrocket.html
- https://hitmarker.net/jobs/razer-channels-payments-sales-analyst-830751
- https://justpostedjobs.co/jobs/razer-snr-manager-ecommerce-sales-54304
- https://www.ocbj.com/technology/cvc-considering-possible-razer-sale-bloomberg/
- https://www.businesstoday.com.my/2026/03/24/fiuus-total-payment-volume-hits-us13-billion-in-2025/
- https://ringgitplus.com/en/blog/apps/razer-pay-is-shutting-down-on-30-september.html
- https://www.fintechfutures.com/paytech/razer-plans-shutdown-of-razer-pay-service-three-years-after-launch
- https://prnewswire.co.uk/news-releases/twbs-signs-exclusive-partnership-with-razer-to-bring-razer-gold-to-the-european-market-852325628.html

**Section 9:** https://fiuu.com/news/uploads/2024/Fiuu_PCI_DSS_COC.pdf

**Section 11:**
- https://www.sec.gov/Archives/edgar/data/0001032975/000103297526000021/logi-20260331.htm
- https://www.businesswire.com/news/home/20260212080218/en/Corsair-Reports-Strong-Revenue-and-Profit-Growth-for-4Q25-and-FY25
- https://secretlab.sg/pages/atome
- https://ibsintelligence.com/ibsi-news/asus-partners-with-2c2p-for-a-more-seamless-online-shopping-experience
- https://www.payplug.com/blog/payment-orchestration-back-market/
- `accounts/traffic/lenovo.md`
- `accounts/traffic/samsung.md`

**Success cases:**
- https://y.uno/en/success-stories/indrive
- https://y.uno/en/success-stories/livelo

</details>
