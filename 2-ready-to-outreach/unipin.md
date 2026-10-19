# UniPin

**Status:** 🔴 **Phase 0 STOP — payment provider / gaming payment aggregator. Out of ICP, route to Partnerships.** Full research not run.
**ICP Score:** Not scored (Phase 0 gate fired before scoring)
**Industry:** Gaming payments: game-credit top-up, e-pins (UniPin Credits) and voucher distribution · **HQ:** Jakarta, Indonesia per press. The T&Cs name a Malaysian platform entity (see below) · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** N/A. Partnerships, not SDR.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** UniPin sells game credits and electronic pins ("UniPin Credits") that work across many publishers' titles. It also runs a D2C top-up storefront at unipin.com. Game publishers and other PSPs integrate it **as a payment method**. That puts it on the supply side of payments, the same box as Coda/Codashop and Razer Gold, not a merchant buying payments.

**SimilarWeb total visits (last full month):** 1.655M average per month, Jul–Sep 2026 (4.965M over 3 months). Source: SimilarWeb (supplied 2026-10-19, `accounts/traffic/unipin.md`).

### Why Phase 0 fires — evidence

| # | Evidence | Type | Source |
|---|----------|------|--------|
| 1 | Paymentwall: *"We've officially added UniPin, an Indonesian payment method to our collection of more than 120 global payment options… Our global payment gateway now supports UniPin Express and UniPin Wallet payments"* (2016-04-27) | `[Third-Party Report]` | https://blog.paymentwall.com/news/weve-added-a-new-indonesian-payment-system |
| 2 | Headline: *"Indonesia's largest gaming payment gateway announces partnership with KK Super Mart"*. CEO Ashadi Ang says UniPin has *"more than 300 game publishers"* and *"10,000 game titles"* (2019-09-10, dated) | `[Press Release]` | https://www.digitalnewsasia.com/business/indonesias-largest-gaming-payment-gateway-announces-partnership-kk-super-mart |
| 3 | 2026 boilerplate: *"Supported by a comprehensive network of payment channels, UniPin provides electronic pins (UniPin Credits) that can be used across a wide variety of games from various publishers"*. It claims *"25.9 million active users across 33 countries"* (2026-07-28, promotional) | `[Press Release]` | https://ipsnews.net/business/2026/07/28/unipin-expands-services-to-support-philippine-mobile-gamers-and-local-ecosystem/ |
| 4 | **In-repo:** UniPin shows up as a **payment channel on other targets' checkouts**: Gravity TH (`services.unipin.com` in the `gnjoy.in.th` CSP `form-action`), Bigo Live BD (`unipin-bd_unipin_voucher`) and Asiasoft PlayPark MY (voucher aggregator) | `[Source Code]`, from prior runs | `2-ready-to-outreach/gravity.md`, `2-ready-to-outreach/bigo-live.md`, `2-ready-to-outreach/asiasoft-playpark.md` |
| 5 | Search summaries describe UniPin as *"Southeast Asia's leading payment service provider for online games and digital products"* | `[UNVERIFIED — search summary only, page not fetched]` | Fortune IDN result: https://www.fortuneidn.com/business/mengenal-unipin-payment-gateway-dalam-game-online-00-xkln4-6vk2by |

**Verdict:** CLAUDE.md excludes PSPs and payment-infrastructure companies (*"stop and flag rather than researching it — those route to Partnerships"*), and the traffic file flagged the same risk in advance. Rows 1–4 are fetched or in-repo primary evidence that publishers and gateways treat UniPin as a payment method. So the gate fires on evidence, not on the name.

**The one counter-argument, recorded so Partnerships can weigh it:** unipin.com is also a D2C storefront that itself accepts payments. The Indonesian homepage, fetched 2026-10-19, promotes *"Top Up Pakai GoPay Cashback 90% GoPay Coins!"*. Its User T&Cs say delivery happens *"after successful payment confirmation, subject to Payment Channel processing"*. So there is a merchant-side collection stack behind the storefront. Razer is the precedent: it was kept at 🟢 because Razer's payments arm was a minority of group revenue and separate from razer.com. **UniPin is the reverse case: payments *are* the core business.** Grab, the closer precedent, was rejected to `not-icp/`.

### Traffic (supplied) — market-mix signal only

| Rank | Country | Traffic share | Est. monthly visits `[DERIVED from supplied share, not a SimilarWeb figure]` |
|------|---------|---------------|------|
| 1 | Indonesia | 73.69% | ~1.22M |
| 2 | Malaysia | 7.84% | ~130K |
| 3 | India | 7.46% | ~123K |
| 4 | Philippines | 2.16% | ~36K |
| 5 | United States | 1.05% | ~17K |
| 6–10 | Bangladesh 0.88% · Singapore 0.79% · Nepal 0.46% · Japan 0.40% · Thailand 0.32% | | |

**Caveats from the traffic file, carried over:**
1. This is the Sales Intelligence view. Only the top 10 countries and their shares are shown (95.05% of traffic). Per-country visit counts above are share × 1.655M, not SimilarWeb numbers.
2. One domain only: `unipin.com`.
3. Mobile app traffic is excluded. The split is desktop 12.85% / mobile web 87.15%.
4. **This is an app-heavy business.** Most top-ups go through the app and the physical voucher / reseller network, such as Indomaret and KK Super Mart (source row 2). **Web traffic cannot size transaction volume.** No transaction count was derived from it, so the 40K/month gate was not tested.

### Legal entities (lightly checked, not a full Agent 1 run)
- **MOBILE ARTS SDN. BHD.** (Malaysia). The User T&Cs say *"The Platform is developed and maintained by MOBILE ARTS SDN. BHD."* and name *"the relevant UniPin entity"* as seller per transaction. Registration number not found. Source: https://www.unipin.com/user-terms-and-conditions (fetched 2026-10-19)
- **Indonesian operating entity:** not confirmed. "PT Uniplay" was checked and **no source ties it to UniPin**, so it is not asserted.
- ⚠️ **HQ discrepancy:** press says Jakarta, but the platform-maintaining entity named in the T&Cs is Malaysian. Unresolved.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not generated, and should not be. Phase 0 stop. Do not run `/full-outreach UniPin`.*

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### Not run — Phase 0 gate

Sections 1–12 of the research report were deliberately not compiled. The skill's Phase 0 says to *"stop and tell Prateek instead of burning a research run"* when the target is a PSP, gateway, acquirer or orchestrator.

**Environment note:** `curl` reached unipin.com, its T&Cs and its privacy policy, plus the third-party pages above. `corp.unipin.com` returned a JS-rendered shell with no extractable text, so UniPin's own B2B/publisher self-description was not captured.

### Recommended next steps
1. **Rejection — Prateek's call:** run `/mark_not_icp UniPin | Phase 0 — gaming payment aggregator / PSP, route to Partnerships`. That moves this file to `not-icp/` and rebuilds the README.
2. **Hand to Partnerships.** UniPin aggregates SEA gaming rails (e-wallets, bank transfer, Indomaret / convenience-store cash, carrier billing in MY) and has a publisher network. That makes it a plausible **APM / connector partner** for Yuno's gaming merchants. Gravity, Bigo and Asiasoft in this repo already route through it.
3. **Prospecting value is in UniPin's publishers, not UniPin.** The 2019 "300+ publishers" claim is dated. UniPin's current storefront lists Moonton (MLBB), HoYoverse, Tencent, HAEGIN, Nordeus, Zepetto and CREO (unipin.com homepage, fetched 2026-10-19). Check those against `accounts/apac-tal.csv`.

### Source Notes
- ✅ Paymentwall integrates UniPin as a payment method: https://blog.paymentwall.com/news/weve-added-a-new-indonesian-payment-system
- ✅ Described as "Indonesia's largest gaming payment gateway" in trade press (2019): https://www.digitalnewsasia.com/business/indonesias-largest-gaming-payment-gateway-announces-partnership-kk-super-mart
- ✅ Malaysian entity named in T&Cs: https://www.unipin.com/user-terms-and-conditions
- ⚠️ Active-user figures conflict: 25.9M across 33 countries (2026 press release) vs 21.4M in 32 countries (job listing, undated, search summary only) vs 6M+ in 40+ countries (older profile, search summary only). None of these is a transaction count.
- ⚠️ "Payment service provider for online games" wording seen only in search summaries. Pages not fetched.

</details>
