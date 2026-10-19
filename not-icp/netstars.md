# NetStars

**Status:** 🔴 **Not ICP — Phase 0 gate: payment gateway / payment infrastructure. Routes to Partnerships.**
**ICP Score:** Not computed. The gate fires before scoring, per `CLAUDE.md` and `/research` Phase 0.
**Industry:** Payment gateway (multi-QR acceptance, StarPay) · **HQ:** Tokyo, Japan · **Researched:** 2026-10-19 · **First email sent:** —
**Motion:** — *(none; not a sales account)*

---

> ## 🛑 WHY THIS STOPPED
>
> `CLAUDE.md`: *"All industries with the exception of PSPs and payment infrastructure companies (Adyen, Stripe, Checkout.com, Razorpay, PayU, Juspay, 2C2P, Xendit, Midtrans, etc.). If a prospect turns out to be one, stop and flag rather than researching it — those route to Partnerships."*
>
> **NetStars describes its own product as a payment gateway, on its own homepage.** Its flagship, StarPay, aggregates QR wallets for merchants and connects them into other payment platforms, Stripe among them. That is the payment-infrastructure layer Yuno sits beside, not a merchant that buys from it. The supplied traffic file had already flagged this risk (`accounts/traffic/netstars.md`, caveat 4); the run confirmed it and stopped.

<details open>
<summary><h2>📊 Section 1 — The gate, and the evidence</h2></summary>

### 1. Self-description: "決済ゲートウェイ「StarPay」" — primary, fetched

`https://www.netstars.co.jp/`, fetched 2026-10-19. The homepage lists its businesses as:

- **StarPay**, described as both *"マルチキャッシュレス決済ソリューション"* (multi-cashless payment solution) and *"決済ゲートウェイ「StarPay」"* (**payment gateway** StarPay), under its payments business
- **StarPay-DX**, store automation and digitisation
- **StarPay-Global**, cashless promotion overseas

The page describes the company as building *"決済を基盤にしたフィンテック事業"* (a fintech business built on payments). `[Checkout]`-tier evidence isn't relevant here; this is the merchant's own words.

### 2. It supplies wallet connectivity *to* Stripe

The same homepage carries a news headline about connecting five major domestic code-payment brands to Stripe (*"国内主要コード決済5ブランドを接続"*). Trade press says the same thing:

- Paymentnavi: *"Stripeがネットスターズと接続してd払い、au PAY、楽天ペイ、メルペイ、AEON Pay に対応へ"*. StarPay connects Stripe to d払い, au PAY, 楽天ペイ, メルペイ and AEON Pay for online payments, with Stripe Terminal to follow. https://paymentnavi.com/?p=183020 `[UNVERIFIED — search summary only, page not fetched]`
- Paymentnavi: StarPay connected to Stripe Terminal for PayPay in-store acceptance (reported as Sep 2025, after a PayPay online connection in Apr 2025). https://paymentnavi.com/?p=165199 `[UNVERIFIED — search summary only, page not fetched]`

A company that sells local-wallet connectivity to Stripe is a **supplier or partner of PSPs**, which is the same position Yuno takes when it integrates local APMs. That is a Partnerships conversation, possibly a useful one (see §3).

### 3. Third-party descriptions match

- Finextra headline: *"Japanese QR code gateway NetStars raises $60 million"* (2021; reported $40M from KKR-managed funds). https://www.finextra.com/newsarticle/37864/japanese-qr-code-gateway-netstars-raises-60-million `[UNVERIFIED — search summary only, page not fetched]`
- IBS Intelligence: *"NetStars, a Japanese QR code payment gateway, raises $60 million"*. https://ibsintelligence.com/ibsi-news/netstars-a-japanese-qr-code-payment-gateway-raises-60-million `[UNVERIFIED — search summary only, page not fetched]`
- Envalith (TSE: 5590): StarPay connects 40+ domestic and overseas QR brands under one merchant agreement. Listed on TSE Growth in Sep 2023. FY12/2025 gross payment volume up 33.2% to about JPY 2.12 trillion. https://envalith.com/en/companies/5590/overview · https://envalith.com/en/companies/5590/reports/019e1a90-5063-7876-a5ca-773db45c222e `[UNVERIFIED — search summary only, page not fetched]`

### 4. The traffic data says nothing about volume

The supplied SimilarWeb file (Sales Intelligence, Jul–Sep 2026, `netstars.co.jp` only) shows about 13,352 avg monthly visits: Japan 94.96%, Singapore 3.99%, United States 1.05%. Desktop and mobile web only; no per-country visit counts; no global rank. As caveat 4 of that file notes, StarPay's payment volume runs through merchant terminals and partner wallets, not this corporate site. Traffic here measures interest in a B2B corporate site. It is not an input to any ICP signal and was not used for one.

</details>

<details>
<summary><h2>🤝 Section 2 — Handover note for Partnerships</h2></summary>

Not a sales account, but potentially relevant to Partnerships:

- **Japan QR wallet coverage.** StarPay reportedly aggregates 40+ QR brands, including PayPay, d払い, au PAY, 楽天ペイ, メルペイ and AEON Pay (sourcing per §2–3). If Yuno's Japan APM coverage needs domestic code payments, NetStars is a candidate connector. It already plays that role for Stripe.
- **Inbound / cross-border wallets.** StarPay-Global and the 40+ "domestic and overseas" brands suggest acceptance of inbound-tourist wallets in Japan `[INFERENCE, not confirmed]`. The overseas brand list was not verified.
- **Before any approach:** confirm the brand list, the merchant-agreement model and whether NetStars holds the acquiring relationship or only routes, from NetStars IR filings (TSE 5590) directly. None of this was fetched in this run.

`apac-tal.csv` lists NetStars with **HQ Country = Australia**. That is wrong: every source above places the company in Tokyo, and it is TSE-listed. The INFO column ("multi-QR acceptance gateway") is correct and should itself have tripped the gate before the account was queued. Fix the row or remove it from the TAL.

</details>

<details>
<summary><h2>📚 Section 3 — Run notes & sources</h2></summary>

**What was done:** read the supplied traffic file and TAL row; 2 web searches; 1 fetch (`netstars.co.jp`, succeeded, so WebFetch works in this environment). The run stopped at Phase 0, and Agents 1–5 were not launched.

**Monthly transaction count:** not assessed; the gate fires first. (NetStars's "transactions" are its merchants' wallet payments, so the metric doesn't apply to a gateway anyway.)

**Sources**
- https://www.netstars.co.jp/ — fetched 2026-10-19 (primary)
- `accounts/traffic/netstars.md` — SimilarWeb Sales Intelligence, supplied 2026-10-19
- https://paymentnavi.com/?p=183020 — search summary only
- https://paymentnavi.com/?p=165199 — search summary only
- https://www.finextra.com/newsarticle/37864/japanese-qr-code-gateway-netstars-raises-60-million — search summary only
- https://ibsintelligence.com/ibsi-news/netstars-a-japanese-qr-code-payment-gateway-raises-60-million — search summary only
- https://envalith.com/en/companies/5590/overview — search summary only
- https://envalith.com/en/companies/5590/reports/019e1a90-5063-7876-a5ca-773db45c222e — search summary only

</details>
