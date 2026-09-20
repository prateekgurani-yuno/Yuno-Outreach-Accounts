# VNGGames

**Status:** 🔴 **Not ICP — Phase 0 gate: payment infrastructure. ROUTE TO PARTNERSHIPS.**
**ICP Score:** n/a — Phase 0 rejection, not scored
**Industry:** Game publishing (VNG Corporation's games division) · **HQ:** Ho Chi Minh City, Vietnam · **Researched:** 2026-09-20 · **First email sent:** —
**Motion:** n/a

---

> ## ⛔ PHASE 0 REJECTION — VNG operates a payment gateway. Verified from a primary SEC filing.
>
> `CLAUDE.md`: *"All industries with the exception of **PSPs and payment infrastructure companies**… If a prospect turns out to be one, **stop and flag rather than researching it — those route to Partnerships.**"*
>
> **I verified this myself in VNG Limited's SEC Form F-1** (filed Aug 2023, CIK 1930799), fetched and grepped 2026-09-20. Verbatim:
>
> > *"…we are required to obtain and maintain various licenses to operate ZaloPay, including **licenses to operate an electronic payment gateway, to maintain digital wallets on behalf of users and to maintain an intermediary payment services permit**."*
>
> > *"**We also operate the ZaloPay payment gateway for clearing online and offline transactions** using traditional payment networks such as Visa and MasterCard."*
>
> **VNG is a licensed payment-infrastructure provider that runs a merchant-acquiring gateway.** Not adjacent to one — it *is* one. ZaloPay serves third-party merchants including, per the same filing, a Shopify integration as *"a direct payment gateway."*
>
> ### Why the games division doesn't rescue it
> VNGGames is a **division of that group**, not an arm's-length company. The 2025 "VNGGames Co Ltd" spin-off is search-summary only and is contradicted by VNG's own FY2025 release, which still treats games as a division (*"mảng"*). Even taken at face value, a Yuno approach lands inside a group whose fintech arm competes directly with part of Yuno's surface area.
>
> **This is the same call as Razer**, excluded at stub-selection for Razer Fintech. ⚠️ **My error:** I knew VNG owned ZaloPay — I wrote it into the research brief — and should have excluded it alongside Razer before spending a research run. The filter was right; I applied it inconsistently.

<details>
<summary><h2>📚 Research findings — retained, because the work is done and the intel is reusable</h2></summary>

### Orchestrator: IN-HOUSE LAYER — confirmed, not inferred
The target list's "In-house Routing" is independently verified and stronger than the list implies. VNGGames runs **its own merchant-side billing and routing platform**:

| Evidence | Source |
|---|---|
| Response header **`server: VNG-PMT-SEA`** on every regional shop page | `shop.vnggames.com/{vn,ph,id,th,sgmy}` |
| `preconnect` to **`sbx-billing.vnggames.com`** and **`sandbox-pay.mto.zing.vn`** — own billing service with sandbox tiers | shop page HTML |
| Legacy gateway `pay.zing.vn` carries per-title pay URLs (`storeID:"payzing"`, `payUrl:"https://pay.zing.vn/pubgm"`) and now **302s to the unified shop** | curl -L |
| **Identical `paymentGroup` taxonomy** across VN/PH/ID/TH/SG-MY — one codebase, one payment layer | diff of five regional pages |
| VNG's own words: *"Payment processing fees… for in-app purchases made through **our proprietary platforms** are lower than the platform fee for third party platforms."* | SEC F-1 — **verified by me** |

Their Vietnamese ToS confirms multiple unnamed PSPs sit underneath: 「Gói Nạp cũng có thể được mua trực tiếp từ một số **bên thứ ba cung cấp dịch vụ thanh toán mà Chúng Tôi hợp tác**」.

### App-store trap: HYBRID, not the failure mode
F-1, verbatim: *"Users can purchase virtual items through various payment channels, including through the **Apple App Store, Google Play Store, as well as ZaloPay, bank transfers, mobile top ups and prepaid cards**."*

`shop.vnggames.com` is the official worldwide top-up site across **VN, ID, TH, PH, MY, SG, TW, HK, US, BR + global**, and game sites push players to it explicitly: *"Metal Slug: Awakening has only one official top-up page… All other websites are not reliable."* **The web/direct channel is large and actively promoted.** The split is undisclosed.

### Vietnam payment methods — CONFIRMED from the live shop UI
ZaloPay (own wallet, with account-binding and auto-debit) · ATM/domestic cards · internet banking · **VietQR** · Mobile Money · SMS billing · convenience-store OTC/O2O · Zing Card / VNGGames Card ePIN · credit card · Point / VNGGames Credit.

⚠️ **MoMo — NOT FOUND.** Vietnam's largest e-wallet is absent from the server-rendered shop. The only `MoMo` string match was inside a base64 blob (`3MMoMoKJuAsg`) — **false positive, excluded**. Absence is not proven (methods load per-game via API), but if it holds, an in-house layer under-serving the market's #1 wallet is notable.

**TH/PH/ID/MY/SG/TW/HK methods: NOT ESTABLISHED** — all regional storefronts ship the same generic taxonomy with no brand names; per-market lists come from a checkout API.

### Scale — SOURCED (FY2025 press release)
Consolidated net revenue **VND 10,894bn (+17%)** · **games bookings VND 8,162bn (+13%)** · paying-player rate 3.7%→4.6% · 57.3M quarterly users · ZaloPay TPV +76%.

Derived transactions ~**3.4M–13.6M/month** (central ~6.8M) on an assumed VND 100k ticket; an independent ARPPU cross-check converges. Volume was never the issue here.

### What could not be established
The web-vs-IAP split · the identity of any third-party PSP behind the in-house layer (redirect checkout, **zero CSP header**, so in-band techniques cannot reach them) · per-market methods outside Vietnam · per-market legal entities · current SBV licensing status (evidence is the 2023 F-1).

### 🧰 Technique notes
`support.vnggames.com` is a **custom Laravel portal, not Zendesk** — the help-centre API technique does not apply. **False positives caught and excluded after context inspection:** `jcB`/`Jcb`, `dAna`, `oVo`, `AtM`, `FPX`, `boost`, `MoMo` — all base64 blobs or the UI string `"levelBoost":"Level boost"`.

</details>

## Rejection Rationale

VNG Corporation holds State Bank of Vietnam licences to operate an electronic payment gateway and intermediary payment services, and runs the ZaloPay merchant-acquiring gateway for third parties — verified verbatim in its own SEC Form F-1. Under the `CLAUDE.md` exclusion for PSPs and payment infrastructure companies, the group routes to Partnerships rather than being prospected, and VNGGames is a division of it rather than an arm's-length merchant.
