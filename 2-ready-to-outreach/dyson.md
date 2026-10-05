# Dyson

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 15 / 29 → 🟢 **Medium** — ⚠️ **but read the access note below before accepting that number**
**Industry:** Premium consumer appliances — floorcare, hair care, air treatment, lighting, audio. High-ticket D2C (~US$550–575 AOV) · **HQ:** Singapore — **Dyson Holdings Pte. Ltd., UEN 201903799Z**, inc. 31 Jan 2019, 3 Sentosa Gateway; global HQ at St James Power Station · **Researched:** 2026-10-05 · **First email sent:** —
**Motion:** ⬜ **STILL CANNOT CLASSIFY at group level — but the picture moved on 2026-10-05.** **Türkiye is now confirmed as a direct, single-PSP hosted integration (iyzico), with no orchestration layer in the documented flow** — that one market reads greenfield. Across every other market, 104 research agents found **no orchestrator, no orchestrator logo-wall appearance, and no acquirer at all outside Türkiye**. That is much stronger than before, but an adversarial pass still refuted the architectural inference 0–3 on the grounds it is not observable, and the rendered checkout remains unreachable everywhere. **Do not pitch "you have no orchestration."** Open on the observable asymmetries, which hold either way.

---

> ## ⚠️ THE SCORE IS MEASURING OUR ACCESS, NOT THE ACCOUNT
>
> Three of the four zero-scored rows are **artefacts of the Cloudflare block**, not findings about Dyson:
>
> | Row | Scored | Why zero | If resolved |
> |---|---|---|---|
> | Orchestration status | **0** | Detection route blocked; architectural inference refuted 0–3 | **+4** — Türkiye alone now reads greenfield; confirm one more market and this moves |
> | Monthly transactions | **+2** | Sourced figure covers `dyson.com` **only**, excluding every APAC ccTLD | +5 if the full estate confirms ≥100k |
> | Local rail gap | **0** | Genuinely good coverage — this one IS a finding | — |
> | Multiple PSPs | **+3** | Now firm — **iyzico is acquirer-class**, read first-hand off Dyson Türkiye's own legal document | — |
>
> **Resolve the first two and this account scores 22/29 ⭐.** The honest position is that Dyson is probably a stronger account than 15/29 implies, and the way to find out is twenty minutes with a browser in Korea, not another research run. See Manual Research Recommendations.

---

> ## 🎯 THE HOOK — in their #2 market, the wallet and the instalment cancel each other out
>
> **Korea is Dyson's second-largest market in the world — 8.69% of global traffic, ahead of Germany, France and the UK, growing +21.02%** — with the best engagement in the entire 114-country dataset (5.25 pages/visit, 23.00% bounce).
>
> Dyson Korea publishes a monthly card-promotion table offering **12-month 무이자 할부 (interest-free instalments)**:
>
> | Issuer | Threshold | Term |
> |---|---|---|
> | 롯데 Lotte | ≥ ₩250,000, < ₩3,000,000 | 12-month 무이자 |
> | 현대 / 하나 / 삼성 Hyundai / Hana / Samsung | ≥ ₩300,000, < ₩3,000,000 | 12-month 무이자 |
> | 삼성 Samsung, selected SKUs | — | **36-month 무이자** |
>
> ### And the 간편결제 wallets are explicitly carved out of it
> **KakaoPay, NaverPay, Samsung Pay, PAYCO and TossPay are excluded from 무이자 할부.** A wallet transaction falls under *the wallet's* instalment policy; Dyson's issuer-funded benefit cannot apply.
>
> **So a Korean customer buying a ₩600,000 Supersonic chooses one of two things, never both:** the wallet they actually use, or the 12-month interest-free plan that makes the basket affordable. Every wallet checkout is an instalment Dyson didn't fund. Every instalment checkout is a wallet the customer abandoned.
>
> ### The same conflict exists in Taiwan, implemented completely differently
> Verbatim from the live Taiwanese site — the one APAC storefront that was readable:
> > 持中國信託LINE Pay卡於Dyson官方線上商城刷卡消費，單筆消費滿10,000元即享LINE POINTS 6%回饋…**分期交易恕不適用**
>
> 6% LINE POINTS on baskets ≥ NT$10,000 — **"instalment transactions are not eligible."** Two markets, two unrelated implementations, the same structural failure: the rewards rail and the instalment rail are mutually exclusive.
>
> ⚠️ **Caveat that matters: the Taiwan store is not Dyson's** — see the disqualifier below. Use Taiwan as corroborating pattern, never as a Dyson market.
>
> **This is issuer-level instalment routing that survives wallet selection. It is precisely what an orchestration layer does, and it is a specific, checkable, non-insulting observation to open on.**

---

> ## 🔴 SIX MARKETS, SIX UNRELATED INSTALMENT RAILS
>
> | Market | Mechanism | Arranged with |
> |---|---|---|
> | 🇰🇷 Korea | Card 무이자 할부, published monthly issuer table, 3-item basket cap | Lotte / Hyundai / Hana / Samsung |
> | 🇯🇵 Japan | **Post-order loan redirect**, repaid by bank direct debit on the 27th | **JACCS** (tripartite contract) |
> | 🇮🇳 India | **Merchant-funded no-cost EMI**, in-checkout, 3/6/12/18/24 months | Axis / BoB / Citi / HDFC / Federal / AMEX |
> | 🇹🇼 Taiwan | Card 12-month 分期零利率 — **and it is the distributor's, not Dyson's** | CTBC / E.SUN / SinoPac, via 恆隆行 |
> | 🇦🇺 Australia | **BNPL**, 4 fortnightly instalments | Afterpay |
> | 🇬🇧🇮🇪🇺🇸🇨🇦 | Klarna Pay in 3 / Affirm 0% | Klarna / Affirm |
>
> Six markets, six different providers — and each programme carries its own issuer negotiations, promo calendars, exclusion rules and thresholds.
>
> ⚠️ **Scope discipline, added 2026-10-05.** That Dyson *names* this many different deferred-payment providers is verified fact. That they are **separately integrated rather than routed through something** is **NOT established** — an adversarial verification pass refuted that inference 0–3, on the grounds that the architecture is simply not observable from provider pages. **Pitch the provider sprawl, which is theirs and checkable. Do not assert "point-to-point rather than orchestrated."** **Japan's is not even a card instalment — it is a separate shopping loan from JACCS where the credit application appears *after* the customer completes the order**, then debits a bank account rather than their card. That is a post-purchase approval cliff sitting outside Dyson's checkout entirely.

---

> ## 🛑 DISQUALIFIER — Taiwan is not Dyson's to sell to
>
> **Verified by reading the live site** (`shop.dyson.tw` returned HTTP 200 to a plain curl — it sits on a different stack from the blocked `dyson.*` estate). Verbatim from its terms:
> > 恆隆行貿易股份有限公司(以下簡稱本公司)依據本購物與服務條款…提供Dyson 線上服務平台之服務
> > 台灣總代理 恆隆行貿易股份有限公司 **統一編號 96946292** · service@**hlh.com.tw** · 0800 251 209
>
> **The Taiwanese checkout, PG contracts, instalment deals and merchant of record all belong to 恆隆行 (HLH / Hengstyle), Dyson's Taiwan sole agent since 2006.** Nobody at Dyson Singapore can sign a payments change for Taiwan.
>
> **Pitch Dyson on "your Taiwan checkout" and you will be wrong in front of the prospect.** Drop Taiwan from the Dyson narrative. Separately: 恆隆行 is a large multi-brand Taiwanese distributor and is arguably a better-qualified target in its own right — **consider a stub.**
>
> **And the open question this forces:** which other APAC markets are Dyson-operated versus agent-operated? **Korea is verifiably Dyson's own** (own entity, ISMS scope covering 공식몰 + membership + app). **Taiwan is not.** Japan, India, Australia and China were **not established either way.** Resolve this before contacting anyone — it is the fastest way to be embarrassed on this account.

---

---

> ## 🌍 GLOBAL PASS — added 2026-10-05 from a 104-agent deep-research run, non-APAC scope
>
> Prateek can pitch every region Dyson operates in, so the APAC-only scope of the first pass was lifted. The non-APAC markets are ~60% of traffic and had never been researched. **Three things changed materially, and one of my own claims was corrected.**
>
> ### ⭐ 1. The first acquirer-class PSP identified anywhere in the world — iyzico, in Türkiye
> **Verified first-hand by me**, read off Dyson Türkiye's own legally-mandated **İşlem Rehberi** (an Article 7 disclosure under Turkey's e-commerce intermediary regulation, Resmî Gazete 32058). Clause **1.8** verbatim:
> > 「Ödeme sayfasındaki "Ödeme Bilgileri" bölümünde **"iyzico ile Öde"** seçeneğini ile alışverişinizin toplam tutarını Türk lirası cinsinden ödeyebilirsiniz. **İyzi Ödeme ve Elektronik Para Hizmetleri Anonim Şirketi ("İyzico")** hesabı ile, İyzico sistemine kayıtlı kredi/banka kartları veya İyzico güvencesi kapsamında Havale/EFT yaparak, **İyzico tarafından sağlanan ödeme hizmeti arayüzünde ("İyzico Ekranı")** talep edilen bilgiler… veya **Tüketici Kredisi** kullanma yolu ile…」
>
> And clause **1.10**, which is what makes this acquiring rather than a consumer wallet:
> > 「**İyzico Ekranı'nda kredi/banka kartı ile ödeme yapmak** istediğinizde kredi/banka kartı bilgilerinizi girdikten sonra varsa **3D Secure** (3 Boyutlu Güvenlik) **ve/veya taksit seçeneklerini seçebilirsiniz.**」
>
> **Raw card PAN entry, 3-D Secure step-up AND taksit selection all happen on iyzico's hosted screen.** The guide walks checkout end to end (1.5 address → 1.6 payment page → 1.7 consent → 1.8 payment → 1.10 3DS/taksit → 1.11 confirmation) and **names no other payment provider**.
>
> ⚠️ **Two limits, both enforced by adversarial verification.** First, "iyzico is the only counterparty *named in this document*" is **not** the same as "Türkiye has no other rails" — the claim that Masterpass, BKM Express, Papara, PayTR, Param, Craftgate, Sipay and MOKA are all absent was refuted **0–3**. Second, the implication that *instalment logic therefore sits outside Dyson's control* was refuted **1–2**, and Finding 3 below actively contradicts it.
>
> ✅ **False positive I caught:** "garanti" appears 5× in that document and **every occurrence is the Turkish word for *warranty*** (`garanti işlemleri`, `Garanti koşulları`, linking to `/destek/garanti-kosullari`). **Garanti Bank is not named.**
>
> ### 2. Türkiye is Dyson-operated, not a distributor — and taksit is presented by Dyson, not iyzico
> Merchant of record is **Dyson Turkey Elektrikli Ürünler Ticaret Limited Şirketi**, İstanbul Trade Registry **146206/5**, MERSİS **0323087411500001**, Ataşehir, İstanbul. Dyson parted from its Turkish distributor and went direct in 2019; it runs branded stores (Akasya, İstinyePark, Buyaka, Marmara Forum) and employs retail staff directly.
>
> **Issuer campaigns put the instalment selection on Dyson's own page.** Akbank, 1–31 Jul 2025, verbatim from the issuer's live campaign page: *"peşin fiyatına **6 ve 9 taksit**"* on spend at Dyson.com.tr, and the load-bearing line —
> > 「alışveriş tamamlanmadan önce **Dyson.com.tr ödeme sayfasında ilgili taksit seçeneği seçilmelidir. Taksit seçeneği Firma tarafından ödeme sırasında sunulmaktadır**」
>
> *The instalment option is presented **by the merchant** during payment.* Separately İş Bankası Maximum, 1–30 Sep 2026: *"Dyson'da Peşin Fiyatına 9 Taksit!"* Both cap at 9 months, which the BDDK instalment ceiling for electrical home appliances independently explains.
> ⚠️ "Merchant-funded" is market-practice inference — *peşin fiyatına* establishes only zero extra cost to the cardholder. Both campaigns have expired.
> 🔎 **Best open acquirer lead anywhere:** İş Bankası's terms exclude *"Maximum POS cihazından yapılmayan işlemler"*, implying **İş Bankası acts as virtual-POS/acquirer for Dyson Turkey**. Unconfirmed.
>
> ### 3. 🇮🇳 THE KOREA CONFLICT EXISTS IN INDIA TOO — and I read this one first-hand
> From **Dyson India's own terms and conditions**, verbatim:
> > *"**No Cost EMI** is available on payments made using certain Credit Cards issued by Banks / Financial Institutions and is **not available on Debit Cards, Cash on Delivery, through Net Banking, UPI, Wallets** Payment Methods or any other payment mode."*
>
> **In the largest UPI market on earth, a customer paying by UPI cannot have the No-Cost EMI offer.** This is structurally the same trade-off documented for Korea — the rail the customer actually uses is carved out of the financing benefit that makes a ₹45,000 basket affordable. **Korea is still `[SYNTH]`; India is now verified from Dyson's own document.** Two markets, two independent implementations, one pattern. **This is the strongest version of the hook and it should lead.**
>
> India's full method list, clause 8.1 verbatim: *"Mastercard, Visa, Maestro, American Express, Dinersclub, NetBanking, **UPI**, Wallets, card on delivery and cash on delivery."* ✅ **RuPay is confirmed still absent from the method list** — the RuPay strings on that page belong to an **HSBC credit-card promotion** ("HSBC RuPay Platinum" as an eligible card), not to accepted methods. A raw keyword count would have produced a false correction here.
>
> ### 4. 🇯🇵 Japan upgraded from `[SYNTH]` to verified
> Dyson Japan's own payment page, verbatim:
> > 「クレジットカード、代金引換、**分割払い（JACCSショッピングクレジット）**、銀行振込、**コンビニ支払い**、**楽天ペイ**、**PayPay**、**Amazon Pay**および**Apple Pay**がご利用いただけます。」
>
> ✅ And the absences are now first-hand rather than inferred: **Paidy, ボーナス払い, LINE Pay, Google Pay, au PAY and リボ払い are all absent from the official method list.** Paidy in particular was flagged as the most likely real gap in the first pass — that now stands on Dyson's own page.
>
> ### 5. The deferred-payment estate outside APAC
> | Market | Products | Provider(s) |
> |---|---|---|
> | 🇬🇧 UK | **Klarna Pay in 3** (unregulated) · **Klarna Pay Over Time / Financing** 6–36 months, variable interest, Direct Debit, soft credit search, sometimes a deposit · **PayPal Credit** (0% to 12 months) · **PayPal Pay in 3** | Klarna + PayPal UK Ltd |
> | 🇩🇪 Germany | **Kauf auf Rechnung** (invoice) · **Ratenkauf** (instalments) — *Klarna is payee and invoice issuer*; Dyson stays invoice issuer for Sofort, card and PayPal | **Klarna Bank AB (publ)** |
> | 🇺🇸 US | **Affirm** 0–36% APR up to 24 months, real-time decision · **Afterpay** Pay-in-4 plus 6/12-month at 6.99–35.5% | Affirm + Afterpay |
> | 🇨🇦 Canada | **Affirm Canada Holdings Ltd.** (formerly PayBright), $100–$15,000, 0–31.99% APR | Affirm Canada |
> | 🇦🇺 Australia | **Afterpay** — confirmed live from Afterpay's own system of record (`merchantId=933803`, `online=true`, **`isSUP=False`** ruling out the single-use-card false positive) | Afterpay |
>
> **Dyson's own UK page draws the regulatory line itself:** *"Klarna's Pay in 3 is an unregulated credit agreement"*, while the longer plans are regulated with **Dyson Limited as credit intermediary**. Germany's Ratenkauf terms link the **SECCI** disclosure mandated by the EU Consumer Credit Directive — Dyson's own terms self-classify it as regulated EU consumer credit.
>
> ### 6. ⚖️ Regulatory exposure sits on a Dyson entity, not only on its partners
> **Dyson Limited is FCA-authorised, FRN 716591**, self-disclosed on its own financing page as *"a credit intermediary and not a lender, offering credit products provided by a limited number of finance providers."* That puts **CONC and financial-promotion obligations on Dyson itself** — so any payments decision touching these programmes has a UK-regulated entity in the loop, not just the Singapore parent.
> ⚠️ Medium confidence only: `register.fca.org.uk` returned 403, so the FRN's live status and permission scope could not be independently confirmed. This is Dyson's self-declaration.
>
> ### 7. ❌ Confirmed negative — Cybersource
> A Cybersource PDF circulating as evidence of a Dyson relationship is a **merchant-agnostic template contract with zero occurrences of "Dyson"** — verified three ways (case-insensitive text search, a regex allowing arbitrary inter-letter whitespace to rule out kerning artefacts, and a raw-byte search of the full 146KB binary to rule out metadata and form fields). **Record as a confirmed negative.** Dyson also appears in no Adyen, Stripe, Checkout.com or Worldpay case study.
>
> ### 8. 🔧 METHOD — the Cloudflare block is *partially* bypassable, and I bounded it myself
> The deep-research run claimed the 403 constraint is wrong because a text-extraction proxy retrieves `dyson.*` intact. **I tested that claim and it is overstated.** The proxy works for **`dyson.com.tr`, `dyson.co.uk`, `dyson.de`, `dyson.co.jp`, `dyson.in`, `dyson.com`, `dysoncanada.ca`** — but **`dyson.co.kr` still returns Cloudflare's "Just a moment…" interstitial through it**, which matches Korea sitting on a different Cloudflare IP cluster. My control (`example.com` through the same proxy → HTTP 200, real content) proves the proxy itself is fine.
>
> **So: Japan, India, Türkiye, UK, Germany, US and Canada are retrievable. Korea — the #2 market and the home of the headline hook — is not.** Separately, `/static/` asset paths respond on *every* domain with no proxy at all, which is how the Magento fingerprinting was done.
> ⚠️ **Still blocked everywhere, by every route: authenticated and stateful paths** — `/checkout/cart`, `/customer/account/login`. **The rendered checkout payment selector remains unobserved in every market.** That is the one gap that would convert this whole picture from inferred to observed.

---

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Premium consumer-appliance manufacturer — vacuums, hair care, air treatment, lighting, audio — selling direct-to-consumer online, through its own Dyson Demo stores, and through mass retail and marketplaces. **Relocated its group HQ from Malmesbury UK to Singapore in 2019**, where the holding company, the family office, the global HQ building and the finance and supply-chain functions now sit. FY2025 revenue **£6.13bn (~US$7.7–8.0bn), down 6.7%** and declining three years running.

**SimilarWeb total visits (last full month):** **Not shown** — Prateek supplied shares only. Scope: `dyson.com` **+ 60 domains**, all-country-domains ON, 114 countries, Jun–Aug 2026. **Supplied, not estimated** — see `accounts/traffic/dyson.md`.

### Top 5 APAC markets
Ranked within territory. Globally the largest single market is the US at 14.93%; Türkiye at 7.54% is #5 worldwide but sits with EMEA.

| Rank | Country | Traffic | Accepted methods | Missing / absent | Local entity |
|------|---------|---------|------------------|------------------|--------------|
| 1 | 🇰🇷 **Korea** | **8.69%** ▲21.02% — **#2 in the world** | Cards; **KakaoPay, NaverPay, TossPay, PAYCO, Samsung Pay**; 12-month 무이자 할부 (Lotte/Hyundai/Hana/Samsung) | **Nothing missing — the problem is that wallets are *excluded* from instalments** | ✅ 다이슨코리아(유), biz reg 811-81-00675, ~₩549.3bn revenue |
| 2 | 🇯🇵 Japan | 5.10% ▼10.45% | Cards (V/MC/JCB/AMEX/Diners), **konbini**, COD, bank transfer, **PayPay, Rakuten Pay, Amazon Pay, Apple Pay, d払い**; **JACCS 36-month 0% shopping credit** | **ボーナス払い not found**; **Paidy not determinable** | ✅ ダイソン株式会社, 法人番号 8010001063616 |
| 3 | 🇮🇳 India | 4.68% ▲28.58% | **UPI**, cards, NetBanking, wallets, **COD and card-on-delivery**; **no-cost EMI 3/6/12/18/24** | **RuPay not named**; **Bajaj cardless EMI not confirmed on dyson.in** | ✅ Dyson Technology India Pvt Ltd, CIN U51909HR2017FTC068554 |
| 4 | 🇦🇺 Australia | 4.03% ▼16.56% | Mastercard/Visa, PayPal, **Afterpay**; Zip reportedly | **PayTo not found · BPAY not found · Klarna not found · Apple/Google Pay not evidenced** | ✅ Dyson Appliances (Aust.) Pty Ltd, ABN 50 073 072 509 |
| 5 | 🇹🇼 Taiwan | 1.76% ▲32.35% | Cards, 12-month 分期零利率 (CTBC/E.SUN/SinoPac), COD, CTBC LINE Pay card | LankaQR-equivalents not assessed — **moot, see disqualifier** | ❌🛑 **No Dyson entity — operated by 恆隆行, 統一編號 96946292** |
| — | 🇨🇳 China | 1.01% ▲**355.08%** | Tmall / JD / WeChat mini-program; Adobe Commerce own store | **Largely unaddressable — see below** | ⚠️ Dyson Trading (Shanghai) Co. Ltd named in litigation; not confirmed as the e-commerce entity |

⚠️ **China's +355% looks exciting and should be deprioritised.** It is growth on a 1.01% base, and the **JD 自营 (self-operated) store means JD buys the stock wholesale and is itself the merchant of record** — Dyson is a supplier there, with zero payment surface. Tmall and WeChat take their own rails. Do not build a China slide.

### Legal entities
- **Dyson Holdings Pte. Ltd.** (Singapore) — **UEN 201903799Z**, inc. 31 Jan 2019, 3 Sentosa Gateway — **group holding entity**
- Dyson Operations Pte. Ltd. (Singapore) — UEN 200711832N · Dyson Singapore Pte. Limited — UEN 200517219H
- **다이슨코리아(유) / Dyson Korea Ltd.** — biz reg 811-81-00675, inc. 12 Apr 2017, Gangnam-gu Seoul
- **ダイソン株式会社** (Japan) — 法人番号 8010001063616, Kojimachi, Chiyoda-ku
- **Dyson Technology India Private Limited** — CIN U51909HR2017FTC068554, Gurgaon
- **Dyson Appliances (Aust.) Pty Limited** — ABN 50 073 072 509
- Dyson Technology Limited (UK) — 01959090 · Dyson Limited (UK) — 02627406 · Weybourne Group Limited (UK) — 08445070
- ❌ **No Taiwan entity.** ❌ No Thailand entity — distributed via Central Trading. ❌ No Malaysia *selling* entity — only Dyson Manufacturing Sdn Bhd (factory).

### Known PSPs
- **NHN KCP** — Korea — `[Third-Party Report]`, **moderate confidence**. Dyson Korea's promo copy instructs shoppers to *"select KakaoPay in the KCP payment window"* (**KCP 결제창**). A merchant does not say "the KCP payment window" unless KCP is the PG. **Page never read directly — reached via search index on two independent queries.**
- **JACCS Co., Ltd.** — Japan — shopping-credit instalment provider, tripartite contract, post-order redirect
- **Afterpay** — Australia — `[Provider Page]`, verified from Afterpay's own merchant directory
- **Rakuten Ichiba** — Japan **marketplace channel only** — verified from Dyson's own Rakuten terms: Rakuten contacts the customer on card failure and **auto-cancels after 7 days**
- **Klarna** (UK/IE), **Affirm** (US/CA) — out of territory, listed for pattern
- ❌ **No acquirer identified for any market.** ❌ **Nothing at all for Singapore — their own HQ market.**
- ❌ **No PSP case study, logo-wall entry or press mention of Dyson at Adyen, Stripe, Checkout.com, Worldpay, Cybersource, Braintree or Global Payments.** A genuine absence in published material — **not** evidence they aren't a customer.

### Orchestration status
**⬜ Cannot classify — insufficient evidence.** Four negative searches against a signal that is almost never published, with the one detection route blocked. Deliberately **not** recorded as greenfield.

**Directional hypothesis, label it as such:** the *divergence* between markets is itself informative — Korea on a Korean domestic PG, Japan on a Japan-shaped domestic stack with a third-party lender, China on a separate Adobe Commerce instance, Taiwan wholly outsourced, Australia on a thin cards+PayPal set. A single global orchestrator tends to pull method sets toward uniformity. This looks more like per-market PSP contracts hanging off a shared commerce core. **That is a reasonable inference from structure, not a verified absence. Never state it as fact.**

### Buying signals
- 💼 ⭐ **Open "Head of E-Commerce" requisition** — mandate and budget in motion, and a plausible entry point ([builtin](https://builtin.com/job/head-e-commerce/7457531)) `[UNVERIFIED — search summary only]`
- 💼 **Open "Head of IT Ecommerce"** (Amsterdam) — SAP Hybris / Adobe Commerce; names **"Cyber Risk, Data Privacy and Fraud technologies"** as core ([builtin](https://builtin.com/job/head-it-ecommerce/10008073), fetched by agent)
- 🚀 **India is the expansion engine** — **23+ Dyson Demo stores**, tier-2 push into Lucknow, Pune and Ahmedabad ([PR Newswire](https://www.prnewswire.com/in/news-releases/dyson-launches-its-first-dyson-demo-store-in-west-delhi-302276190.html))
- 🚀 **Korea pop-up, 15 May 2026** — "Supersonic Travel" at Shinsegae Gangnam ([Asia Business Daily](https://www.asiae.co.kr/en/article/2026051510364873831)). **The only 2026-dated APAC commercial activity found — the freshest hook available.**
- 💰 **Revenue declining three years running** — £7.1bn → £6.57bn → £6.13bn, with EBITDA defended by cost-out (+18% on falling revenue). **This is a margin-pressure buyer, not a growth-at-any-cost buyer.** MDR reduction and approval-rate recovery land better than "scale faster."
- 📋 **No public payment RFP found.** Stated explicitly.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Dyson` to draft the 12-touch sequence, or call this from `/prepare_batch`.*

**Constraints for whoever drafts this:**
1. **Motion is UNCLASSIFIED, not greenfield.** Never write "you have no orchestration layer" — we could not look. Open on the observable asymmetries (wallet-vs-instalment, six rails) which are true regardless of what sits underneath.
2. **Never mention Taiwan as a Dyson market.** It is 恆隆行's.
3. **Do not build a China angle.** JD self-operated means Dyson is a supplier there.
4. **Target Singapore.** The holding company, global HQ, finance and supply-chain functions are all there — and it is in territory. No named CTO/CIO/CDO exists publicly; the open Head of E-Commerce req is the live entry point. **Use `/enrich` against LinkedIn for Dyson Singapore e-commerce/payments/digital titles** — web search cannot do this.
5. **⚠️ Never write the name "Mark Brown."** *"Dyson Group appoints new CIO, Mark Brown"* is the **Australian bus and coach operator**, a different company. Several other "Dyson CIO" hits are Pamela C. Dyson, an unrelated person.
6. **Do not open on restructuring.** The job cuts are July/Oct 2024 — two years stale. It will read as out-of-date research.
7. **Do not pitch Japan 3DS as compliance.** The mandate deadline passed in March 2025. The question is what blanket 3DS did to their approval rate.
8. **Do not use:** the "91% online" figure (unreliable, self-contradictory); "Chinese consumers are 70% of global sales" (implausible, almost certainly garbled); the A$1,600 duplicate-charge figure (unverified); the 2020 US credential-stuffing breach (it is not a payments breach, it is six years old and out of territory).
9. **No booking link.** Every CTA is a plain time proposal in the prospect's local zone.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 15 / 29

| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+2** | ✅ **DERIVED (floor): ≥46,307/month.** Grips Intelligence, **May 2026: US$25,556,983 from 46,307 transactions**, AOV US$550–575, conversion 1.00–1.50%. **Billing unit: a web order on `dyson.com`.** ⚠️ **This covers `dyson.com` ONLY** — it excludes `dyson.co.kr`, `dyson.co.jp`, `dyson.in`, `dyson.com.au` and every other ccTLD, which together carry ~25% of global traffic. The true own-site total is materially higher and **very likely in the ≥100,000 band (+5)**. Scored conservatively on the verified floor. **This is the single highest-value number to confirm.** |
| Orchestration status | **0** | ⬜ **Cannot classify at group level — but closer than before.** **Türkiye is a confirmed direct single-PSP hosted integration (iyzico)**, read first-hand: PAN entry, 3DS and taksit all on iyzico's screen, no other provider named in the checkout walkthrough. 104 agents found no orchestrator in any market and Dyson on no orchestrator's logo wall. **Still scored 0** because an adversarial pass refuted the "point-to-point rather than orchestrated" inference **0–3** — the architecture is not observable from provider pages, and `/checkout/cart` is blocked by every route. **I am not overriding a 0–3 refutation with my own judgement.** Confirm the pattern in one more market and this becomes +4, taking the account to 19/29. |
| 3+ countries | **+3** | ✅ **61 domains, 114 countries** (supplied SimilarWeb). A **15-market commerce platform** verified by DNS, 10 of them APAC. **6+ legal entities confirmed** across SG/KR/JP/IN/AU/UK. |
| Multiple PSPs | **+3** | ✅ **Now firm, and one is acquirer-class.** **iyzico** (Türkiye — PAN + 3DS + taksit on its hosted screen; verified first-hand), **NHN KCP** (Korea, moderate), plus **JACCS** (JP), **Klarna** (UK/IE/DE), **Affirm** (US/CA), **Afterpay** (US/AU), **PayPal Credit / Pay in 3** (UK), **Rakuten Ichiba** (JP marketplace). Earlier caveat that no acquirer-class provider existed anywhere is now superseded for Türkiye. |
| Local rail or licensing gap in a top-3 market | **0** | ⬜ **And this zero is a real finding, not an access artefact.** Korea has five wallets plus issuer instalments. Japan has konbini, PayPay, Rakuten Pay, Amazon Pay, d払い, COD and 36-month 0% credit. India has UPI, NetBanking, COD and no-cost EMI across six issuers. **Their APAC rail coverage is genuinely good.** The gaps that exist — PayTo/BPAY in Australia (#4 APAC, #10 global), ボーナス払い in Japan, RuPay not named in India — do not meet "dominant rail absent from a top-3 market." **Do not stretch this row to fit the wallet/instalment conflict; that belongs in Section 10.** |
| Recent expansion | **+2** | ✅ India 23+ Demo stores with a tier-2 push (Lucknow, Pune, Ahmedabad); Korea pop-up May 2026. |
| Payment issues | **+2** | ✅ **Moderate frequency across three APAC markets.** Korea: payment captured and confirmation email sent, **but the order does not exist in Dyson's system** — on Dyson's own mall. Japan: **four distinct refund-delay threads on `jp.community.dyson.com`, Dyson's own forum.** Australia: duplicate charges and a website error generating duplicate orders. |
| Funding >$10M | **0** | ❌ Private, family-owned. No funding round — the cash flows the other way: a **£750m dividend** to Weybourne Holdings in FY2025. |
| High traffic outside home | **+2** | ✅ **Emphatically.** Home market is Singapore, which does not appear in the visible top 18 at all. The largest single market is the US at 14.93% — far below the 60% threshold. |
| Competitor using orchestration | **0** | ❌ **Not one competitor confirmed on an orchestrator**, and **no orchestration case study exists for any premium consumer-electronics or appliance DTC brand, in APAC or anywhere.** Closest: SharkNinja is a named participant in Adyen's "Adyen Agentic" launch (16 Jun 2026) — but Adyen is a processor, not an orchestrator, the programme is US-only, and no source states Adyen processes for SharkNinja. ⚠️ **This cuts both ways: Yuno has no category reference to show Dyson either. Expect "who else in our category runs this?" and have an honest answer.** |
| Payment job postings | **+1** | ✅ Marginal but real: the open **Head of IT Ecommerce** req names **"Cyber Risk, Data Privacy and Fraud technologies"** as core knowledge. ⚠️ **No payments-specific or checkout-specific role exists anywhere in public postings**, and no "Head of Payments" title exists in the company. Awarded for payment-adjacent e-commerce leadership hiring, not for a payments hire. |

**Tier:** High Priority (17+) ⭐ / Medium (10–16) 🟢 / Low (<10) 🔴 → **🟢 Medium (15)**

**No RFP override** — none found.

**No analyst override applied, and I considered three:**
- *App-store revenue* — **not applicable, and verifiably so.** Dyson sells physical goods; there is no IAP leg. Confirmed further by the MyDyson app having no commerce capability at all.
- *Absolute volume too small* — rejected. 46,307 transactions/month at ~US$560 AOV on one domain alone is real volume, and the true figure is higher.
- *Double counting* — checked. "3+ countries" fires on the 61-domain/114-country footprint and the DNS-verified 15-market platform; "multiple PSPs" fires on separately-evidenced providers in different markets. Independent facts.

⚠️ **What I did NOT do: inflate the tier to match the account's feel.** 15/29 is what the verified evidence supports. The access note at the top of this file explains why that is probably an understatement, with the arithmetic. **A fudged ⭐ would be worse than an honest 🟢 plus a clear path to resolve it.**

### Source Notes

**✅ Verified first-hand by me (fetched or probed, with controls)**
- **Dyson runs a market-partitioned commerce platform at `{market}-{env}.commerce.dyson.com`.** Confirmed by DNS across **15 production markets** — APAC: `kr` `in` `au` `nz` `hk` `my` `th` `id` `ph` `vn`; plus `tr` `ae` `sa` `mx` `za`. Production on Fastly, non-production on Cloudflare. India alone carries **11 numbered `fit` environments plus `uat`, `sit` and `preprod`**; every market spot-checked returned 5/5 non-prod environments.
- **Control run and it mattered:** `*.commerce.dyson.com` is **not** a wildcard — nonsense hostnames do not resolve, so those records are real. But **`*.dyson.com` IS a wildcard** (`zzzznonsense.dyson.com` resolves), so any enumeration under that zone would have been meaningless.
- **Japan, Singapore, China, Taiwan, the US, UK, Germany, France and Canada are NOT on that platform** — and I ruled out alternate market codes (`jp`/`ja`/`jpn`/`japan`, `sg`/`sgp`, `uk`/`gb`/`gbr`, …) before concluding it. **Singapore — their own global HQ — is not on the same commerce platform as ten of their APAC markets.**
- **Every `dyson.*` property returns HTTP 403 (Cloudflare)** — verified on dyson.com, .co.kr, .co.jp, .in, .com.au, .tw, .com.sg, dysoncanada.ca, careers.dyson.com; control host returns 200, so this is site-level bot protection, not an egress block.
- **`dyson.com.tw` is a PARKED SEDO DOMAIN**, not a Dyson property — it redirects to a domain-sales lander. `dyson.com.cn`, `.com.my`, `.com.ph`, `.com.hk` and `.cn` do not serve. **A resolving domain is not a storefront.**
- **Grips Intelligence: `dyson.com` = US$523.6m (2025)**, +5–10% YoY, "all countries", main market US, methodology not disclosed.
- **ECDB: `dyson.com` = US$98m (2025)**, 100% first-party, conversion 2.0–2.5%, no country breakdown.
- **Hanno Kirner confirmed as CEO since February 2024**, ex-Tata/JLR, succeeding Roland Krueger — who moved to a board role at **Dyson Holdings**, independently corroborating the Singapore holdco.
- **No Dyson case study at Yuno** — Phase 0 clear. Yuno's publicly-citable cases are Rappi, inDrive and Livelo.

**✅ Verified by agents, directly from a readable page**
- **Taiwan is 恆隆行's** — read off the live `shop.dyson.tw` terms, with tax ID and contact domain.
- **Dyson Japan's official Rakuten storefront payment terms**, read in full from `rakuten.ne.jp`.
- **MyDyson app has no commerce capability** — Apple iTunes Search API, isolated to `bundleId == com.dyson.dysonlink`, 3,616-character description keyword-scanned for buy/purchase/shop/payment/checkout/cart/subscribe. **Exactly one hit, and it is "order replacements" — a deep-link out to the web store.** The similar-apps trap was hit and handled: 7 of 8 API results were unrelated top-chart apps.
- **Afterpay merchant listing for Dyson Australia**, from Afterpay's own directory.
- **Japan's EMV 3-D Secure mandate** — Credit Card Security Guideline required EMV 3DS of essentially all EC merchants **by end of March 2025**; guideline 5.0 published 14 Mar 2024, 6.0 on 4 Mar 2025. Multiple independent Japanese sources. **Sourced live, not from background knowledge.**

**⚠️ Strong but search-summary only — the page was never read**
- The entire Korea payment picture: the 무이자 issuer table, thresholds, the **wallet exclusion**, and NHN KCP. Specific and internally consistent across independent queries, but **nobody has seen that page.**
- Korea's payment-captured-but-order-missing reports (Clien, Coolenjoy); Japan's refund-delay threads; Australia's duplicate charges.
- Japan's own-store method list (PayPay, Rakuten Pay, Amazon Pay, d払い, konbini).
- India's no-cost EMI issuer list and the full method list.
- Dyson's FY2025 regional commentary, including **"the strength of the pound against Asian currencies impacted sales in key markets."**

**❌ Could not establish**
- **Any acquirer, in any market.** No PSP was fingerprinted. **Nothing at all for Singapore.**
- **Whether Dyson uses an orchestrator.** Genuinely unknown.
- **Which APAC markets are Dyson-operated vs agent-operated**, beyond Korea (Dyson's) and Taiwan (恆隆行's).
- **PCI DSS posture, tokenization, vaulting, 3DS approach** — nothing, in any market.
- **Marketplace vs D2C revenue split** — presence confirmed in every market, share in none. **Do not let this become a number in a deck.**
- **Any named CTO, CIO, Chief Digital or E-commerce officer.**
- **India's payment complaints** — zero found. Likely a venue artefact (Indian consumers use X and the National Consumer Helpline); **do not infer India is clean.**

**Corrections made during this run**
- **The TAL says "~$9B global." That is wrong** — FY2025 is **£6.13bn (~US$7.7–8.0bn) and declining**. Using $9B in an email is an error a merchant would catch.
- **I claimed Dyson runs a "Technology+" subscription. It could not be confirmed to exist under that name** — that was my assumption, not a finding, and it is withdrawn.
- **Agent 1 reported a US$783m ECDB own-domain figure. I fetched that page: it shows $98m for `dyson.com` and no $783m anywhere.** Not supported by its citation; excluded.
- **Agent 5 treated Grips' $523.6m as Dyson's global own-site total and derived "6–8% of group revenue" from it.** It is `dyson.com` alone and excludes every APAC ccTLD, so that derivation understates. Excluded.
- **The two third-party estimates of the same domain differ by more than 5× ($98m vs $523.6m).** Both are presented; neither is adopted.

**⚠️ False positives and traps caught — recorded so nobody downstream repeats them**
- **"Dyson Group appoints new CIO, Mark Brown"** → the **Australian bus and coach operator**. Different company. Other "Dyson CIO" hits are **Pamela C. Dyson**, an unrelated person.
- **Trustpilot `jp.`, `au.` and `nz.` subdomains are country *front-ends* rendering reviews of the UK and Canada entities** — not reviews of Dyson's Japanese or Australian stores. Anyone reading the raw URL list will mis-attribute this.
- **A Wayback retrieval for `dyson.co.kr/card-promotion` returned ~106KB of Korean online-game payment terms for GnJoy / ㈜그라비티 (Gravity Co.)** — wrong company entirely. Discarded. Any re-run must validate payload provenance.
- **`dyson.com.tw` is a parked Sedo domain** (3× "Parking", 1× "sedo" in the body).
- **"Chinese consumers contributed 70% of Dyson's global sales"** — implausible and almost certainly garbled. **Do not use under any circumstances.**
- **Bajaj Finserv markets Dyson EMI heavily, but describes it as "through partner platforms and authorised retail stores"** — that is Bajaj's own network, **not evidence of Bajaj at `dyson.in` checkout.**
- **BuiltWith returns a live page reading "We cannot lookup results on this domain sorry"** for dyson.com, sharkninja.com and roborock.com — a 200 response that is not a result.

### Success Case Alternatives
- **inDrive** — Tier 2. Operating in 50+ countries, reached a **90% payment approval rate** and integrated **ten new countries in eight months**. The profile match is *many markets, each needing local rails* — which is Dyson's exact shape at 15 commerce markets and 114 countries. The "ten countries in eight months" figure speaks directly to per-market integration cost.
- **Livelo** — Tier 2. **Recovered 50% of transactions** and **increased approval rates by 5%**, with no implementation required for new providers. The approval-rate recovery argument fits a margin-pressure buyer.
- **Rappi** — Tier 3 credibility default. Nine countries, 35M+ users; previously took **five to ten minutes to detect and respond to provider disruptions manually**.
- ⚠️ **All three metrics above came via search summary of Yuno's own success-stories page, which is on a blocked host.** **Verify each figure on `y.uno/en/success-stories` before putting a number in an email.** Never attach a number to a Yuno customer without a published metric.
- ⚠️ **There is no appliance or premium-consumer-electronics orchestration reference anywhere.** Have an honest answer ready for "who else in our category?"

---

## Section 1: Website Traffic Analysis by Country

**Data source:** ✅ **Resolution path 1 — pasted SimilarWeb data supplied by Prateek, 2026-10-05.** Full table in `accounts/traffic/dyson.md`. Scope `dyson.com` + 60 domains, all-country-domains **ON**, 114 countries, Jun–Aug 2026. **Shares only — total visits not shown in the supplied view.**

| Rank | Country | Share | Change | Trend | In territory? |
|------|---------|-------|--------|-------|---------------|
| 1 | 🇺🇸 United States | 14.93% | ▲ 2.67% | Growing | No |
| 2 | 🇰🇷 **Republic of Korea** | **8.69%** | ▲ **21.02%** | **Growing fast** | ✅ **high priority** |
| 3 | 🇩🇪 Germany | 8.00% | ▼ 5.92% | Declining | No |
| 4 | 🇫🇷 France | 7.82% | ▼ **54.20%** | **Collapsing** | No |
| 5 | 🇹🇷 Türkiye | 7.54% | ▲ 21.25% | Growing | ❌ EMEA |
| 6 | 🇬🇧 United Kingdom | 6.10% | ▼ 12.99% | Declining | No |
| 7 | 🇯🇵 **Japan** | **5.10%** | ▼ 10.45% | Declining | ✅ **high priority** |
| 8 | 🇮🇳 **India** | **4.68%** | ▲ **28.58%** | **Growing fast** | ✅ |
| 9 | 🇮🇹 Italy | 4.21% | ▼ 27.46% | Declining | No |
| 10 | 🇦🇺 **Australia** | **4.03%** | ▼ 16.56% | Declining | ✅ |
| 13 | 🇹🇼 Taiwan | 1.76% | ▲ 32.35% | Growing | 🛑 distributor-run |
| 18 | 🇨🇳 China | 1.01% | ▲ **355.08%** | Spiking off a small base | ⚠️ unaddressable |

**APAC visible subtotal: ≥25.27%.** Rows beyond #18 were below the fold; **Singapore — the group's own HQ market — does not appear in the visible top 18 and its share is unknown.**

**The directional story matters more than the levels.** Four of six visible APAC markets are growing — Korea +21.02%, India +28.58%, Taiwan +32.35%, China +355.08% — while every large European market contracts: France −54.20%, Netherlands −31.50%, Italy −27.46%, Spain −24.72%, UK −12.99%. **The growth is in territory.**

⚠️ **India's engagement is the weakest in the top 18** — 00:00:56 and 2.17 pages/visit, against markets running 2–4 minutes. On a ₹45,000 product that is worth a question, but browsing behaviour is not by itself a payments finding.

## Section 2: Legal Entities & Local Presence

**Headquarters:** Singapore. Group HQ relocated from Malmesbury, UK in 2019; **Dyson Holdings Pte. Ltd. (UEN 201903799Z) was incorporated 31 January 2019, the same month the move was announced.** Global HQ building: St James Power Station, opened 25 March 2022, 110,000 sq ft. **~1,400–2,000 staff in Singapore spanning R&D, advanced manufacturing and global HQ functions including supply chain and finance.**

| Country | Entity | Reg. # | Source |
|---|---|---|---|
| 🇸🇬 Singapore | **Dyson Holdings Pte. Ltd.** — group holdco | **201903799Z** | [OpenGov](https://opengovsg.com/corporate/201903799Z) |
| 🇸🇬 Singapore | Dyson Operations Pte. Ltd. | 200711832N | [OpenGov](https://opengovsg.com/corporate/200711832N) |
| 🇸🇬 Singapore | Dyson Singapore Pte. Limited — likely SG selling entity | 200517219H | [OpenGov](https://opengovsg.com/corporate/200517219H) |
| 🇰🇷 Korea | 다이슨코리아(유) Dyson Korea Ltd. | 811-81-00675 | nicebizinfo / saramin `[UNVERIFIED]` |
| 🇯🇵 Japan | ダイソン株式会社 | 法人番号 8010001063616 | [gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=8010001063616) |
| 🇮🇳 India | Dyson Technology India Pvt Ltd | U51909HR2017FTC068554 | [Zauba](https://www.zaubacorp.com/company/DYSON-TECHNOLOGY-INDIA-PRIVATE-LIMITED/U51909HR2017FTC068554) |
| 🇦🇺 Australia | Dyson Appliances (Aust.) Pty Limited | ABN 50 073 072 509 | [ABR](https://abr.business.gov.au/ABN/View/50073072509) |
| 🇬🇧 UK | Dyson Technology Limited | 01959090 | Companies House |
| 🇬🇧 UK | Weybourne Group Limited — family office | 08445070 | Companies House |
| 🇲🇾 Malaysia | Dyson Manufacturing Sdn. Bhd. — **manufacturing only** | 200001007356 | LEI lookup |
| 🇹🇼 Taiwan | **❌ none — 恆隆行貿易股份有限公司** | **統一編號 96946292** | `shop.dyson.tw` terms, **read directly** |

**Cross-Border Gap Analysis**

| Country | Top-10 traffic? | Local entity? | Domestic acquiring gated? | Cross-border risk |
|---|---|---|---|---|
| 🇰🇷 Korea | ✅ #2 | ✅ Dyson Korea Ltd | **Yes — Korea gates domestic acquiring behind local presence** | **Low** — entity present, domestic PG in the flow |
| 🇯🇵 Japan | ✅ #7 | ✅ ダイソン株式会社 | Practically, yes | **Low** |
| 🇮🇳 India | ✅ #8 | ✅ Dyson Technology India | Yes — RBI PA framework | **Low** |
| 🇦🇺 Australia | ✅ #10 | ✅ Dyson Appliances (Aust.) | No | **Low** |
| 🇹🇼 Taiwan | ✅ #13 | **❌ none** | — | **N/A — not Dyson's operation** |
| 🇨🇳 China | #18 | ⚠️ unconfirmed | Yes — licensed local path required | **Largely moot — marketplace-mediated** |
| 🇹🇭 🇲🇾 🇮🇩 🇵🇭 🇻🇳 | not visible | **❌ no selling entity found** | Varies | ⚠️ **On the commerce platform but with no confirmed entity** |

> **Notable, and it cuts against the usual APAC pitch: there is no cross-border acquiring gap in Dyson's major APAC markets.** Korea, Japan, India and Australia each have a local entity and a local payment arrangement. **The standard cross-border approval-rate argument does not apply here** — say so internally rather than reaching for it. The argument on this account is rail fragmentation, instalment-vs-wallet conflict and reconciliation.

> ⚠️ **Except in one documented case.** Dyson's own Japanese Rakuten terms list, among the grounds for cancelling an order: 「**海外で発行されたカードなど、ご利用いただけないカードでのご注文の場合**」 — *orders placed with unusable cards, **such as cards issued overseas***. That is a **cross-border acceptance limitation stated as policy.** Scope discipline: it is the Rakuten channel, where Rakuten Ichiba is the processor — not necessarily `dyson.co.jp`.

> **MANUAL:** Establish which APAC markets are Dyson-operated vs agent-operated. Korea ✅ Dyson's. Taiwan 🛑 恆隆行's. Japan, India, Australia, China, Thailand, Malaysia **unknown**.

## Section 3: Payment Providers & Payment Stack

### 3A. PSPs & Acquirers

| Country | Provider | Role | Evidence | Source |
|---|---|---|---|---|
| 🇰🇷 Korea | **NHN KCP** | Payment gateway | `[Third-Party Report]` — **moderate**; "KCP 결제창" in Dyson's own promo copy, via search index ×2 | `dyson.co.kr/card-promotion` (blocked) |
| 🇯🇵 Japan | **JACCS Co., Ltd.** | Shopping-credit instalments, tripartite loan | `[Third-Party Report]` + a Yahoo Chiebukuro thread read in full | [chiebukuro](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q13263311823) |
| 🇯🇵 Japan | **Rakuten Ichiba** | Processor — **marketplace channel only** | `[Terms]` **read in full** | [rakuten.ne.jp](https://www.rakuten.ne.jp/gold/dyson/sp/info/termsofsale.html) |
| 🇦🇺 Australia | **Afterpay** | BNPL | `[Provider Page]` **read in full** | [afterpay.com](https://www.afterpay.com/en-AU/stores/dyson) |
| 🇦🇺 Australia | Zip / Zip Money | BNPL | `[Third-Party Report]` — **unconfirmed, "reportedly"** | — |
| 🇬🇧🇮🇪 | Klarna — Pay in 3 | BNPL | On Dyson's own financing page `[UNVERIFIED]` | dyson.co.uk/financing (blocked) |
| 🇺🇸🇨🇦 | Affirm | BNPL / 0% APR | `[UNVERIFIED]` | dyson.com/financing (blocked) |
| 🇹🇼 Taiwan | CTBC / E.SUN / SinoPac | Card instalments — **via 恆隆行** | `[Checkout]` **read directly** | `shop.dyson.tw` |
| 🇸🇬 Singapore | **❌ NOTHING FOUND** | — | — | — |

**Card tokenization, vaulting, network tokens, 3DS approach: no evidence in any market.**

**E-commerce platform:** ✅ **Magento 2 / Adobe Commerce — CORRECTED 2026-10-05.** An earlier inference in this file said SAP Commerce Cloud/Hybris; that was wrong. Static assets are served from Magento 2's canonical deployed-static-content path `/static/version<epoch>/frontend/Dyson/commerce/<locale>/`. **The discriminating test:** Magento 2's shipped nginx config carries `rewrite ^/static/(version\d*/)?(.*)$ /static/$2 last`, so a *numeric* version segment must be stripped and a *non-numeric* one must not — and that is exactly what the origin does: `version1790867174`, `version1`, `version999999999` and no-version all return 200, while **`versionFOO` returns 404**. That digit boundary is Magento's own regex and is not reproducible by a CDN rule. The theme path is literally `Dyson/commerce`, matching the `commerce.dyson.com` naming. ⚠️ Adobe Commerce vs Magento Open Source edition is indistinguishable from these signals. **China remains separately on Adobe Commerce/Magento 2** per third-party reporting.

**Platform boundary, independently confirmed two ways.** 404-body fingerprinting: `dyson.com.tr`, `dyson.in`, `dyson.com.au` and `dyson.co.za` return the **same 8,029-byte page, md5 `08cd7d187d2098d6ddc269491d817e99`** — one shared application instance — while `dyson.co.uk` (md5 `ae2c5a01...`), `dyson.com` (md5 `83b0f3e2...`) and `dyson.co.jp` are each a different stack. That corroborates the DNS enumeration in this file from a completely independent angle.

### 3B. Payment Orchestrator

**⬜ CANNOT CLASSIFY — INSUFFICIENT EVIDENCE.**

| Check | Result |
|---|---|
| `"Dyson" "payment orchestration" OR "payment routing" OR "multi-acquirer"` | No Dyson mention |
| `"Dyson"` + nine named orchestrators | No mention at any |
| Orchestrator customer logo walls | Dyson appears on none |
| Dyson job specs for orchestration/routing language | None |
| **Tech-profiler detection of the live checkout** | **UNAVAILABLE — the only route that answers this** |

> *"No public evidence of a payment orchestration platform was found. **This must not be read as 'none detected'.** Orchestration leaves no trace in promotional copy, payment-method lists or press; the one route that detects it — a technology profile of the live checkout — was blocked at three independent providers. Four negative searches against a rarely-published signal is weak evidence."*

### 3C. PCI DSS
**No PCI statement, AoC, trust page or payment-security documentation obtained, in any market.** Their security pages are on blocked domains and no cache or third-party reproduction was found.

**One confirmed security incident, and it is not a payments breach.** A California AG breach notification (`PINC2020.78`, circa 2020) records an incident *"that occurred outside of Dyson"* affecting the Dyson **US** website, giving a third party access to user accounts. Dyson states **no financial information was involved**; **account login credentials** were potentially compromised. **This is credential stuffing / account takeover.** Six years old, US market, out of territory. **Recommendation: leave it out of outreach entirely.**

> **MANUAL:** Open a cart to the payment step on `dyson.co.kr`, `dyson.co.jp`, `dyson.in` and `dyson.com.au` in a browser with DevTools. **This single action answers 3A, 3B and 3C and is the highest-leverage thing anyone can do on this account.**

## Section 4: Alternative & Local Payment Methods

| Country | Method | Category | Status | Source |
|---|---|---|---|---|
| 🇰🇷 Korea | KakaoPay · NaverPay · TossPay · PAYCO · Samsung Pay | Digital wallet | **Active** — but **excluded from 무이자 할부** | `[SYNTH]` dyson.co.kr |
| 🇰🇷 Korea | 12-month 무이자 할부 (Lotte/Hyundai/Hana/Samsung); 36-month on selected Samsung SKUs | Instalments | **Active**, with thresholds and a **3-item basket cap** | `[SYNTH]` |
| 🇰🇷 Korea | Toss Pay 계좌이체 — 5% Toss Points ≥₩300,000 | Bank transfer | **Active** | `[SYNTH]` |
| 🇯🇵 Japan | konbini · COD · bank transfer | Cash / A2A | **Active** | `[SYNTH]` + Rakuten terms |
| 🇯🇵 Japan | PayPay · Rakuten Pay · Amazon Pay · Apple Pay · d払い | Wallet | **Active on the own store** | `[SYNTH]` ×2 independent |
| 🇯🇵 Japan | **JACCS 分割払い, up to 36 instalments, 0%, fee borne by Dyson** | Instalments | **Active — post-order loan redirect, bank direct debit on the 27th** | `[3P]` read in full |
| 🇯🇵 Japan | **ボーナス払い (bonus payment)** | Instalments | **NOT FOUND** on the own store; **explicitly not accepted** on the Rakuten storefront | `[SYNTH]` |
| 🇯🇵 Japan | **Paidy** | BNPL | **NOT DETERMINABLE** — and the most likely real gap | — |
| 🇯🇵 Japan | LINE Pay | Wallet | **NOT FOUND** — and LINE Pay is winding down in Japan; **don't pitch it** | — |
| 🇮🇳 India | **UPI** | A2A | **Active** | `[SYNTH]` T&Cs |
| 🇮🇳 India | NetBanking · wallets · **COD and card-on-delivery** | Mixed | **Active** | `[SYNTH]` |
| 🇮🇳 India | **No-cost EMI 3/6/12/18/24 — Dyson absorbs the interest** | Instalments | **Active.** AMEX capped at 3/6/12; Axis, BoB, Citi, HDFC, Federal reach 24 | `[SYNTH]` |
| 🇮🇳 India | **RuPay** | Cards | **NOT NAMED** in the stated list — worth a question, **not confirmed absent** | — |
| 🇦🇺 Australia | Mastercard / Visa / PayPal | Cards | **Active** | `[SYNTH]` |
| 🇦🇺 Australia | **Afterpay** — 4 fortnightly instalments, co-branded Afterpay Day campaigns | BNPL | **Active** | `[3P]` read in full |
| 🇦🇺 Australia | **PayTo · BPAY · Klarna · Apple Pay · Google Pay** | A2A / BNPL / wallet | **NOT FOUND** | — |
| 🇹🇼 Taiwan | 12-month 分期零利率 (CTBC/E.SUN/SinoPac); CTBC LINE Pay card 6% LINE POINTS; 貨到付款 | Mixed | **Active — 恆隆行's** | `[Checkout]` read directly |
| 🇨🇳 China | Alipay · WeChat Pay · 白条 | Wallet / instalments | **Platform capabilities of Tmall/JD — not Dyson-controlled** | `[SYNTH]` |

### The three things worth saying about rails

**1. Their APAC coverage is genuinely good — do not invent a gap.** Korea has five wallets and issuer instalments. Japan has konbini, four wallets, COD and 36-month 0% credit. India has UPI, NetBanking, COD and merchant-funded EMI across six issuers. **The pitch here is not "you're missing a rail."**

**2. Australia is the thinnest major APAC market.** Cards + PayPal + Afterpay, with **PayTo, BPAY, Klarna, Apple Pay and Google Pay all not found.** On an A$1,200 basket **PayTo is the obvious cost play against card + BNPL** — and if they haven't evaluated it, that is a conversation. Australia is #4 in APAC so this does not meet the ICP row's "top-3" bar, but it is a real observation.

**3. Japan's instalment mechanism is the structural oddity.** JACCS is a **tripartite shopping loan**: the credit application appears **after the customer completes the order**, underwriting happens outside Dyson's checkout, and repayment is by **bank direct debit on the 27th**, not card. Compare Paidy or card-native 分割, both of which keep the customer inside checkout. **"What does your post-redirect JACCS approval and drop-off look like?" is a strong, specific discovery question.**

> **MANUAL:** VPN into Korea, Japan, India and Australia and walk a cart to the payment step. Every row marked `[SYNTH]` above comes from a search engine's summary of a page nobody has seen.

## Section 5: Payment Issues & Customer Complaints

| Issue Type | Platform | Frequency | Date Range | Source |
|---|---|---|---|---|
| **Payment completed and confirmation email received, but the order does not exist in Dyson's system** | Clien, Coolenjoy — **Dyson's own Korean mall** | Moderate | not determinable | [Clien](https://www.clien.net/service/board/park/12929640), [Clien](https://m.clien.net/service/board/kin/9959907) `[UNVERIFIED]` |
| Card authorisation **not cancelled for over a month** after return collected | Clien / Coolenjoy | Moderate | not determinable | [Coolenjoy](https://coolenjoy.net/bbs/freeboard2/56245?page=4531) `[UNVERIFIED]` |
| **Refund not issued after returned goods received — multi-month delays** | **`jp.community.dyson.com` — Dyson's OWN official Japanese forum** | **Moderate-to-high — 4 distinct threads** | threads 440–502 | [thread 502](https://jp.community.dyson.com/一般的なディスカッション-52/ダイソン公式の業務処理遅延-二ヶ月経過も返金されない-502), [495](https://jp.community.dyson.com/一般的なディスカッション-52/返金対応が謎すぎる-495), [440](https://jp.community.dyson.com/一般的なディスカッション-57/返金されない-440), [479](https://jp.community.dyson.com/一般的なディスカッション-57/返品手続きが遅すぎる-479) |
| **konbini payment-confirmation emails from the processor fail to arrive**, leaving paid orders unconfirmed | jp.community.dyson.com | — | — | `[UNVERIFIED]` |
| **Duplicate charges; a website error ("Requested order quantity is not available in stock") generating duplicate orders and multiple charges** | ProductReview.com.au | Moderate | not determinable | [ProductReview](https://www.productreview.com.au/listings/dyson) `[UNVERIFIED]` |
| Paid, no order confirmation, told no order exists, funds already debited | ProductReview.com.au | Moderate | not determinable | same |
| 🇮🇳 India | consumercomplaints.in | **ZERO found** | — | **Genuine negative** |

> **Pattern — and it is consistent across three APAC markets.** The failure is not declines, not 3DS, not fraud. It is **payment captured, order not persisted**, and **refunds that take months**. The Korean "payment succeeded but the order doesn't exist" reports are the classic authorisation-captured-but-order-not-created signature — in Dyson's **#2 market in the world.**
>
> **And the Rakuten terms explain a plausible mechanism:** *payment method cannot be changed after ordering* — the only remedy is cancel and re-order. **That forces a re-authorisation on every correction**, which is exactly how duplicate charges appear.
>
> **Yuno mapping:** callback consumption, transaction-status reconciliation and idempotent retry as platform behaviour rather than per-market merchant code.

⚠️ **Three honest limits on this section.**
1. **Dyson's stated refund policy is itself ~3 months worst case** — 4–8 weeks to process a return, then 10–14 business days to issue, then 1–2 billing cycles to land. **Many "delay" complaints are Dyson performing to spec.** That is a working-capital and CX argument, not a failure argument, and must be pitched as such.
2. **No evidence of false-positive fraud declines, 3DS/OTP failures, or high-ticket decline problems was found** — despite looking for exactly those. **Do not assert them.**
3. **India produced zero payment complaints.** Likely a venue artefact. **Do not infer India is clean.**

## Section 6: Corporate & Payment Strategy Developments

| # | Date | Development | Category | Source |
|---|------|-------------|----------|--------|
| 1 | **15 May 2026** | **"Supersonic Travel" pop-up, Shinsegae Gangnam, Seoul** — the only 2026-dated APAC commercial activity found | Market activity | [Asia Business Daily](https://www.asiae.co.kr/en/article/2026051510364873831) |
| 2 | **2026 (current)** | ⭐ **Open "Head of E-Commerce" requisition** — charter to "set the market vision for E-Commerce sales across existing and new channels" | Hiring / buying trigger | [builtin](https://builtin.com/job/head-e-commerce/7457531) `[UNVERIFIED]` |
| 3 | **2026 (current)** | **Open "Head of IT Ecommerce"** (Amsterdam) — SAP Hybris/Adobe Commerce; **"Cyber Risk, Data Privacy and Fraud technologies"** | Hiring | [builtin](https://builtin.com/job/head-it-ecommerce/10008073) |
| 4 | **Oct 2024 →** | **India: 23+ Dyson Demo stores**, tier-2 expansion into Lucknow, Pune, Ahmedabad | Market expansion | [PR Newswire](https://www.prnewswire.com/in/news-releases/dyson-launches-its-first-dyson-demo-store-in-west-delhi-302276190.html) |
| 5 | **1 Oct 2024** | ⚠️ **Surprise layoffs in Singapore** — three months after Dyson said Singapore, "its global head office," was not directly impacted by the UK restructure | Restructuring | [Malay Mail](https://www.malaymail.com/news/singapore/2024/10/02/people-are-shocked-and-have-low-morale-as-dyson-implements-surprise-layoffs-in-singapore/152321) |
| 6 | **9 Jul 2024** | ~1,000 UK job cuts, roughly a third of the UK workforce | Restructuring | [Fortune](https://fortune.com/europe/2024/07/09/dyson-to-axe-a-third-of-its-u-k-workforce-ceo-hanno-kirner-warns-the-vacuum-giant-needs-to-be-prepared-for-the-future) |
| 7 | **Feb 2024** | **Hanno Kirner appointed CEO**, ex-Tata/JLR, succeeding Roland Krueger (→ board role at **Dyson Holdings**) | Leadership | [Investing.com](https://uk.investing.com/news/stock-market-news/dyson-appoints-car-industry-veteran-as-ceo-amid-product-expansion-plans-3299626) |

**No public payment RFP found.** **No payment-adjacent licence anywhere** — no MAS PSA licence, no India PA/PG authorisation. ⚠️ That is the **expected and correct** result: Dyson is a merchant, not a payment institution. Recorded so the absence isn't later misread as a research gap.

⚠️ **The restructuring narrative is two years stale.** No 2025 or 2026 restructuring news was found. **Do not open with "I saw you're restructuring."**

## Section 7: Payment-Specific News

**❌ Dyson has no payments-industry press footprint whatsoever.** `thepaypers.com`, `finextra.com` and `pymnts.com` returned nothing. No PSP win or loss, no orchestration story, no tokenisation story, no checkout announcement.

**Consequence for the pitch, and it is genuinely useful:** there is **no incumbent publicly claimed** and **no displacement narrative to work against**. Nobody has planted a flag on this account.

**No provider addition or removal could be dated.** BNPL availability was found (Klarna UK/IE on Dyson's own financing page; Afterpay AU; Zip and Sezzle US) but **nothing is datable**, so no "they just added / just dropped X" story exists. ⚠️ Afterpay, Zip and Sezzle maintain SEO store-directory pages for merchants where BNPL is available **via retail partners** — those are not proof of a direct integration.

**No confirmed outage.** Crowd-report trackers log checkout-specific reports on 2026-03-27, 2025-10-25 and 2025-06-17, but three isolated reports over nine months on unmoderated SEO-farmed sites is **not a pattern**. Use as conversation colour only.

## Section 8: Checkout Experience Audit

⚠️ **Partially completed.** Dyson's own checkout was **not accessible in any market** — Cloudflare 403 across the entire `dyson.*` estate, BuiltWith refusing the domain family, SimilarTech unreachable, and `web.archive.org` egress-blocked. Findings below are limited to publicly observable elements and to **one readable storefront (Taiwan, which is the distributor's) and one official marketplace channel (Japan Rakuten).**

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | **Not observable** on any Dyson-operated store | — | Platform inferred as SAP Commerce Cloud from DNS + hiring |
| Commerce estate | **15-market platform** at `{market}-{env}.commerce.dyson.com`, **DNS-verified with a wildcard control** | — | **Japan, Singapore, China, Taiwan, US, UK, EU are NOT on it** |
| **Mobile commerce** | **❌ NONE. The MyDyson app has no store, no cart, no checkout, no payment and no IAP.** Full 3,616-char description keyword-scanned; the only commerce-adjacent string is *"easily **order** replacements"*, i.e. a deep-link to web | **Poor** | **100% of D2C transactions run through the web checkout.** For an APAC-weighted, app-first customer base this is a conspicuous structural gap, and the app-to-web handoff is itself a conversion leak |
| Conversion rate | **1.00–1.50%** (Grips, May 2026) at **AOV US$550–575** | **Poor-to-fair** | At that AOV, **10bps of checkout completion ≈ US$255k/yr** on the May-2026 run rate |
| Payment methods visible | **Korea / Japan / India / Australia: search-summary only.** Taiwan and Japan-Rakuten: read directly | — | — |
| Location-based method display | **Yes — emphatically.** Six markets, six unrelated instalment mechanisms | — | Each separately negotiated |
| Instalment options | **Present in every major APAC market**, by a different mechanism in each | Fair | And in Korea and Taiwan **mutually exclusive with the wallet/rewards rail** |
| 3DS | **Not detected anywhere.** Not referenced in any readable documentation | — | Japan's EMV 3DS mandate deadline passed Mar 2025, so it is presumably live — **unconfirmed** |
| PCI indicator | **Not determinable** | — | — |
| Multi-currency | Per-market: KRW, JPY, INR, AUD, TWD, CNY, SGD | — | — |
| Saved payment methods | **No evidence in any market** | — | — |
| **Payment method change after ordering** | **❌ Not possible** (Rakuten channel, verified) — cancel and re-order is the only path | **Poor** | **Forces a re-authorisation on every correction** — a plausible mechanism behind the duplicate-charge reports |
| Refund mechanics | **Manual bank transfer for non-card methods, with the customer bearing the transfer fee**; no interest paid; card refunds crossing the issuer cutoff land in the following billing cycle (Rakuten channel, verified) | **Poor** | Directly explains the Section 5 refund-delay pattern |
| **Foreign-issued cards** | **An explicit order-cancellation trigger**: 「海外で発行されたカードなど、ご利用いただけないカードでのご注文の場合」 (Rakuten channel, verified) | **Poor** | A documented cross-border acceptance limitation stated as policy |

## Section 9: PCI DSS Compliance

| Dimension | Finding | Source |
|---|---|---|
| PCI DSS Level | **Not found** | — |
| Card data handling | **Not determinable** | — |
| Tokenization / network tokens | **No evidence in any market** | — |
| Recommended Yuno integration | **Cannot recommend** without knowing the current card-capture model | — |

*"No direct PCI compliance documentation was found publicly for Dyson."* Their trust and security pages are on blocked domains and no cache or third-party reproduction exists.

## Section 10: Strategic Insights & Outreach Angles

> ### Insight #1: In their #2 market, the wallet and the instalment cancel each other out
> **Evidence:** Section 1 — **Korea is 8.69% of global traffic, #2 worldwide, +21.02%**, best engagement in the 114-country set + Section 4 — **KakaoPay, NaverPay, Samsung Pay, PAYCO and TossPay are explicitly excluded from 무이자 할부**, and the instalment table runs per-issuer thresholds with a 3-item basket cap.
> **Pain Point:** Two conversion rails that cannot co-exist on one transaction. On a ₩600,000 basket the customer takes the wallet they use or the 12-month interest-free plan — never both. Dyson pays for an issuer-funded instalment programme that the most convenient checkout path silently forfeits, and cannot see the trade-off because it is invisible in per-PG reporting.
> **Yuno Value Proposition:** Issuer-level instalment routing that survives wallet selection — the instalment decision made on the BIN and issuer rather than on which button the customer pressed.
> **Best Success Case:** inDrive — Tier 2, many-markets-many-rails profile. ⚠️ Verify the 90% approval figure on Yuno's own page first.
> **Outreach Angle:** Observe the exclusion and ask what it costs. It is specific, checkable, and implies no criticism of their build.
> **Suggested Subject Line:** "KakaoPay or 12-month 무이자, not both"

> ### Insight #2: Six markets, six unrelated instalment rails
> **Evidence:** Section 4 — Korea card 무이자, Japan **JACCS post-order loan redirect**, India merchant-funded no-cost EMI, Taiwan card 分期 (distributor's), Australia Afterpay, UK/US Klarna/Affirm + Section 3A — **no acquirer identified in any market and no two acquirers confirmed on one checkout.**
> **Pain Point:** Every market's instalment programme is separately negotiated, separately configured, separately reconciled, with its own thresholds, exclusions and promo calendar. India alone runs ragged issuer coverage — AMEX capped at 12 months while Axis, BoB, Citi, HDFC and Federal reach 24. The marginal cost of the next market's instalment rail is paid in engineering and finance-ops time.
> **Yuno Value Proposition:** One integration across markets; instalment and BNPL rails become configuration rather than per-market build.
> **Best Success Case:** inDrive — **ten new countries in eight months** speaks directly to per-market integration cost.
> **Outreach Angle:** Lay out the six mechanisms as an observation. It is factual, it is theirs, and the sprawl argues itself.
> **Suggested Subject Line:** "Six markets, six instalment rails"

> ### Insight #3: The payment succeeds and the order doesn't exist — in the #2 market
> **Evidence:** Section 5 — Korean reports of **payment captured and confirmation email sent with no order created**, plus month-plus authorisation-cancellation delays; four refund-delay threads on **Dyson's own Japanese community forum**; Australian duplicate charges + Section 8 — **payment method cannot be changed after ordering, so every correction forces a cancel-and-re-order re-authorisation.**
> **Pain Point:** Three APAC markets showing the same class of failure — captured authorisation with no persisted order, and refunds measured in months. On a US$550+ basket each instance is a lost high-value order plus a manual refund plus a CX escalation.
> **Yuno Value Proposition:** Callback consumption, transaction-status reconciliation and idempotent retry as platform behaviour rather than per-market merchant code.
> **Best Success Case:** Livelo — **recovered 50% of transactions**. ⚠️ Verify before quoting.
> **Outreach Angle:** Their own Japanese community forum is the most credible possible source. Reference the pattern, never a named customer's complaint.
> **Suggested Subject Line:** "Paid, but no order"
> ⚠️ **Handle carefully:** Dyson's published refund policy is itself ~3 months worst case, so some of this is performing to spec. Pitch the captured-but-not-created failures, not the refund timelines.

> ### Insight #4: No mobile commerce at all, on an APAC-weighted customer base
> **Evidence:** Section 8 — **the MyDyson app has no store, cart, checkout, payment or IAP**, verified by keyword-scanning the full app description; the only commerce string is a deep-link to "order replacements" + Section 1 — **≥25.27% of traffic is APAC**, led by Korea, Japan and India, all app-first markets, with India showing the weakest engagement in the top 18 (00:00:56, 2.17 pages/visit).
> **Pain Point:** 100% of D2C transactions funnel through one web checkout at a **1.00–1.50% conversion rate on a US$550–575 AOV**. Consumables reordering — the most repeat-friendly, lowest-friction revenue Dyson has — bounces the customer out of the app and into a web checkout with no stored credential evidence.
> **Yuno Value Proposition:** Stored credentials, network tokens and wallet rails that make a repeat consumables purchase a one-tap action rather than a re-entered PAN.
> **Best Success Case:** Tier 3 credibility default — no appliance-category reference exists.
> **Outreach Angle:** Non-obvious, entirely verified, and not a criticism of anyone's build.
> **Suggested Subject Line:** "Filter reorders leave the app"
> **Arithmetic worth having ready:** at US$560 AOV and ~46,307 transactions/month on `dyson.com` alone, **10bps of checkout completion ≈ US$255k/year.**

> ### Insight #5: Declining revenue, defended margin, and a cost story they told themselves
> **Evidence:** Section 6 — revenue **£7.1bn → £6.57bn → £6.13bn** (−14% over two years) with EBITDA **+18%** on falling revenue, ~1,000 UK jobs cut and surprise Singapore layoffs + Section 2 — **the finance function sits in Singapore, in territory** + reported FY2025 commentary attributing part of the decline to **"the strength of the pound against Asian currencies"** in key markets `[UNVERIFIED — needs re-sourcing]`.
> **Pain Point:** This is a margin-pressure buyer. Growth arguments will not land; cost of acceptance, approval-rate recovery and FX handling will.
> **Yuno Value Proposition:** MDR reduction through local acquiring and PSP diversification; approval-rate recovery as recovered revenue at zero marginal CAC.
> **Best Success Case:** Livelo — **+5% approval rate**. ⚠️ Verify.
> **Outreach Angle:** **If the FX quote verifies, it is the single sharpest opening available** — a manufacturer publicly attributing revenue decline to currency in Asia, talking to someone whose product routes and settles in Asia. **Do not use it until re-sourced.**
> **Suggested Subject Line:** "Sterling against the won"

### Quick Hits: Ready-to-Use Sales Ammunition

**Email hooks**
1. Your Korean customers choose between the wallet they use and the 12-month 무이자 — KakaoPay, NaverPay, Samsung Pay, PAYCO and TossPay are all carved out of the instalment benefit.
2. You run six different instalment mechanisms across six markets — and Japan's isn't even a card instalment, it's a JACCS loan the customer applies for after they've already placed the order.
3. The MyDyson app can tell a customer their filter needs replacing but can't sell them one — every reorder bounces out to the web checkout.
4. Korea is your second-largest market in the world, ahead of Germany, France and the UK.

**Cold call openers**
1. "I was looking at your Korean card-promotion page — am I reading it right that simple-pay wallets don't qualify for the 무이자 할부?"
2. "Quick one: when a Japanese customer picks the JACCS instalment, they apply for the credit after the order's placed. Do you see drop-off at that step?"
3. "You're running six different instalment rails across APAC. Who owns that — is it one team or six?"

## Section 11: Similar Companies & Prospecting Pipeline

### 11A. Direct Competitors

| Company | Website | HQ | Size | APAC markets | Known PSP/Orchestrator | Source |
|---|---|---|---|---|---|---|
| **SharkNinja** (Shark + Shark Beauty) | sharkninja.com | US (NYSE: SN) | **US$6.399bn FY2025** | Japan, China | ⭐ **Adyen** — named participant in "Adyen Agentic", 16 Jun 2026. ⚠️ US-only programme; no source says Adyen processes for them | [Fintech News SG](https://fintechnews.sg/133226/ai/adyen-agentic/) |
| **Roborock** | roborock.com | Beijing (Shanghai STAR) | ~US$1.8bn; **#1 global robot-vac share ~17%** | China, Korea, Japan, SEA, AU | Affirm (US BNPL) only | [Seoul Economic Daily](https://en.sedaily.com/finance/2026/09/29/roborock-tops-global-robot-vacuum-shipments-in-q2-with-237) |
| **Coway** | coway.com | Seoul (KRX) | **KRW 4.96tn / ~US$3.7bn FY2025, +15.2%** | Korea, Malaysia, Thailand, Indonesia, Japan | **Not found** — Korean domestic PG + bank CMS auto-debit inferred | [Korea Times](https://www.koreatimes.co.kr/business/companies/20260206/coway-logs-15-revenue-growth-in-2025-on-strong-domestic-overseas-demand) |
| **Ecovacs** | ecovacs.com | Suzhou (Shanghai) | ~US$2.0bn; ~11.5% share | China, Japan, Korea, SEA | **Not found** | — |
| **Dreame** | dreametech.com | Suzhou | ~7.5% share | China, Korea, SEA, AU | **Shopify Payments** `[INFERENCE from the badge set]` + Klarna, Afterpay | [dreametech](https://www.dreametech.com/pages/payment-method) |
| **Laifen** | laifentech.com | Shenzhen | ~10% premium hair-dryer share vs Dyson ~30% | China, SEA, Korea, Japan | **Not found** | — |
| **Miele** | miele.com | Germany, private | group revenue **not established** | AU, CN, JP, KR, SG | **Not found** | — |

**Also in the set, not individually researched:** Samsung and LG (Korean, both sell premium cordless stick vacuums — **and Korea is Dyson's #2 market**), Panasonic Beauty, ghd, T3, Blueair, Philips, Xiaomi/Smartmi, Narwal.

⚠️ **Structural point worth knowing: APAC is 45–50% of the global robotic-vacuum market, and the top four players by share are three Chinese companies plus one American. Dyson is not in the top four of robot floorcare at all.** Its online share of China's high-end hair-dryer segment reportedly fell to ~7% in H1 2024 `[UNVERIFIED, second-hand]`.

### 11B. Industry Peers / Channels

| Company | Vertical | Key markets | Why similar (payment context) |
|---|---|---|---|
| **Coupang** | Marketplace | Korea | 22.5% of Korean e-commerce; home appliances 16.4% of its revenue — **where Dyson's Korean volume partly goes** |
| **Rakuten Ichiba / Yahoo! Shopping** | Marketplace | Japan | Dyson runs official storefronts on both; **Rakuten is the processor there** |
| **Tmall / JD** | Marketplace | China | **JD 自営 means JD is the merchant of record** |
| **恆隆行 (HLH / Hengstyle)** | Distributor | Taiwan | **Operates Dyson's entire Taiwan checkout** — a target in its own right |
| **Central Trading / PowerBuy** | Distributor | Thailand | Dyson Thailand appears to run through them |

### 11C. Companies Recently Adopting Payment Orchestration

**❌ None found.** No competitor appears on any orchestrator's customer list, and **no orchestration case study exists for any premium consumer-electronics or appliance DTC brand, in APAC or anywhere.** Published orchestration case studies that surfaced are fashion and marketplace (Boozt, Vinted) or other verticals entirely (GetYourGuide, Grammarly, Trek Bicycle, Wikimedia).

⚠️ **Read this honestly in both directions.** There is no "your competitor already did this" proof point for Dyson — **and Yuno has no category reference to show them either.** Expect the question and have an honest answer.

### 11D. Prospect Scoring — top finds

| Company | Est. score | Rationale | In TAL? |
|---|---|---|---|
| **Coway** | Est. 16–19 🟢/⭐ | **~US$3.7bn, +15.2%, and a genuine recurring-billing business** — 1.85m new rental contracts in 2025, millions of active mandates across **Korea, Malaysia, Thailand, Indonesia, Japan**. Mandate management, retry logic and involuntary churn are core economics for them in a way they are not for Dyson. **The strongest new prospect this run surfaced.** | ❓ check |
| **恆隆行 (HLH / Hengstyle)** | Est. 10–14 🟢 | Multi-brand Taiwanese distributor **running Dyson's entire Taiwan e-commerce and payment stack**, plus other brands. Owns the checkout decision Dyson does not. | ❌ **not on TAL — genuine find** |
| **Roborock** | Est. 12–15 🟢 | **#1 global robot-vac share**, Chinese, heavy D2C across China, Korea, Japan, SEA, Australia. No PSP evidence = possibly greenfield | ❓ check |
| **Dreame** | Est. 10–13 🟢 | Private, D2C-heavy, floorcare **and** premium hair care, likely single-PSP on a packaged gateway | ❌ |
| **Ecovacs** | Est. 10–13 🟢 | ~US$2.0bn, listed Shanghai, China/Japan/Korea/SEA | ❓ check |

**✅ Dyson IS already on `accounts/apac-tal.csv`** — but the row needs correcting (see below). **恆隆行 is not, and is a genuine find.**

⚠️ **No PSP/ICP conflict:** none of the companies above is a PSP or payment-infrastructure business. NHN KCP, JACCS, Afterpay, Klarna, Affirm and Rakuten appear only as vendors. **2C2P surfaced once as an unrelated search artefact with no Dyson relationship** — flagged because it is on the exclusion list.

## Section 12: Business Case Data

| Metric | Value | Source / Methodology |
|---|---|---|
| Annual Revenue | **£6.13bn FY2025 (~US$7.7–8.0bn), −6.7% YoY.** FY2024 £6.57bn; FY2023 £7.1bn — **~14% decline over two years** | [channelnews](https://www.channelnews.com.au/dyson-family-takes-a1-43-billion-dividend-as-revenue-slides-and-chinese-rivals-attack/) ⚠️ **TAL says "~$9B" — wrong, correct it** |
| Operating profit / EBITDA / PAT | £600m (+15%) · **£1.11bn (+18%)** · £381m (−14%) | same |
| Dividend | **£750m** to Weybourne Holdings — ~197% of net profit | [BM Magazine](https://bmmagazine.co.uk/news/james-dyson-dividend-rises-750m/) |
| Units sold | **>20 million products** FY2024 (record volumes) | channelnews `[UNVERIFIED]` |
| **Average Transaction Value** | **US$550–575** (Grips, May 2026) | Third-party estimate. Separately, a **US retail panel** gives ASP US$421.86 — ⚠️ **different thing: that is Amazon/Best Buy/Lowe's, not Dyson's own checkout, and not APAC** |
| **Monthly transaction count** | **✅ DERIVED (floor): ≥46,307/month.** Grips Intelligence, **May 2026: US$25,556,983 from 46,307 transactions** on `dyson.com`, conversion 1.00–1.50%. **Billing unit: a web order on `dyson.com`.** ⚠️ **Excludes every APAC ccTLD** (`dyson.co.kr`, `.co.jp`, `.in`, `.com.au`), which carry ~25% of global traffic. **The true own-site total is materially higher and very likely ≥100,000.** Scored +2 on the verified floor; **+5 if confirmed.** | [Grips](https://gripsintelligence.com/insights/retailers/dyson.com) |
| ⚠️ **Conflicting own-site revenue estimates** | **Grips: `dyson.com` = US$523.6m (2025)** vs **ECDB: `dyson.com` = US$98m (2025)**. **Both fetched directly. They differ by >5×.** Different scope definitions; **neither is adopted.** | [Grips](https://gripsintelligence.com/insights/retailers/dyson.com) · [ECDB](https://ecdb.com/resources/sample-data/retailer/dyson) |
| Korea entity revenue | **₩549,288,910,000 (~US$390–400m)** — most recent filed, year not stated | nicebizinfo `[UNVERIFIED]` |
| India entity revenue | **>INR 500 crore** FY ending 31 Mar 2024 | [Zauba](https://www.zaubacorp.com/company/DYSON-TECHNOLOGY-INDIA-PRIVATE-LIMITED/U51909HR2017FTC068554) |
| Employees | **~10,000 (2025)**, down from ~13,000 (2022). Singapore ~1,400–2,000 | channelnews ⚠️ sources conflict (14,000+ / 17,185) — **cite the direction, not the level** |
| Primary currencies | KRW, JPY, INR, AUD, TWD, CNY, SGD, GBP, USD, EUR, TRY | Supplied SimilarWeb + entity set |
| Top 3 markets by traffic | US 14.93% · **Korea 8.69%** · Germany 8.00% | Supplied SimilarWeb |
| **Billing channel split (web vs app store)** | **✅ 100% web. Not applicable in the usual sense — and verified.** Physical goods, no IAP leg, and **the MyDyson app has no commerce capability at all.** **The app-store trap does not apply to this account.** | Apple iTunes Search API, bundle `com.dyson.dysonlink` |
| ⚠️ **Addressable-base warning** | **Only Dyson's own storefronts are orchestration-addressable.** Coupang, Naver, Rakuten, Yahoo!, Tmall, JD, Amazon, Flipkart, Harvey Norman, 新光三越, PowerBuy and 恆隆行 all collect payment themselves. **Marketplace presence is confirmed in every APAC market; the share is unknown in every one.** Anyone sizing this off the £6.13bn group number will be wrong by roughly an order of magnitude. | Agents 3 & 5 |

### Overall Research Confidence

**⚠️ LOW-TO-MEDIUM — downgraded one level, and the cause is environmental, not editorial.**

- **Traffic: HIGH, and it is the strongest part of this file.** ✅ **Supplied by Prateek**, consolidated across 61 domains and 114 countries with the all-country-domains toggle ON. This is the best traffic basis of any account in the repo.
- **Payment stack: LOW. This is the downgrade.** Every `dyson.*` property returns Cloudflare 403 in every available tool; **BuiltWith refuses the domain family** with a 200-response page reading *"We cannot lookup results on this domain sorry"*; SimilarTech is DNS-unreachable; **`web.archive.org` is egress-blocked and returned contaminated content on its one partial success.** Four independent routes to the checkout, all closed. **No acquirer is identified in any market, nothing at all is known about Singapore, and orchestration is genuinely unclassifiable.** Roughly 70% of the PSP question is unanswered.
- **Payment methods: MEDIUM.** Korea, Japan and India are specific and internally consistent across independent queries — but **nobody has seen those pages.** Only Taiwan (the distributor's) and Japan-Rakuten (a marketplace channel) were read directly.
- **Entities and financials: MEDIUM-HIGH.** Registration numbers obtained for Singapore, Japan, India, Australia and the UK. Revenue is consistent across three independent outlets. **But Dyson's own FY2025 results release is on a blocked domain and was never read** — everything financial is secondary.
- **Complaints: MEDIUM for Japan and Korea, LOW for Australia, NONE for India.** Japan's evidence is strongest because it sits on **Dyson's own community forum**.
- **Competitive: MEDIUM**, with a hard ceiling — no category orchestration reference exists in either direction.
- **Section 8: PARTIALLY COMPLETED**, not skipped. Reconstructed from one readable distributor storefront, one marketplace channel, the app-store API and DNS.

### Manual Research Recommendations

> **Area:** ⭐ **Open a cart to the payment step in Korea, Japan, India and Australia**
> **Why it matters:** This single action answers Sections 3A, 3B, 3C, most of 4 and most of 8 — the acquirer per market, whether an orchestrator SDK is present, the 3DS behaviour, and the real method list. **It would move the ICP score by up to 7 points on its own.** Every route a research agent has is closed; a human with a browser has none of that problem.
> **Suggested action:** VPN into each market, add a product, proceed to payment, and watch the network tab for `adyen`, `stripe`, `checkout.com`, `cybersource`, `kcp`, `inicis`, `tosspayments`, `gmo`, `veritrans`, `razorpay` or any orchestrator signature. **Twenty minutes, and it is worth more than this entire run.**

> **Area:** Confirm the monthly transaction count across the full own-site estate
> **Why it matters:** The scored figure (≥46,307) covers `dyson.com` only and excludes every APAC storefront. **Confirming ≥100,000 moves the ICP row from +2 to +5.**
> **Suggested action:** Ask on a discovery call, or obtain per-ccTLD estimates. Note the two public estimates of `dyson.com` alone differ by >5×, so third-party data is unreliable here.

> **Area:** ⭐ **Which APAC markets are Dyson-operated vs agent-operated**
> **Why it matters:** **Taiwan is 恆隆行's, not Dyson's** — pitching Dyson on their Taiwan checkout would be wrong in front of the prospect. Korea is verifiably Dyson's own. **Japan, India, Australia, Thailand and Malaysia are unknown**, and Thailand and Malaysia show no selling entity at all.
> **Suggested action:** Check each market's T&Cs for the contracting entity. This is the fastest way to avoid embarrassment on this account.

> **Area:** Re-source the "strength of the pound against Asian currencies" quote
> **Why it matters:** **It is the single sharpest opening available** — a manufacturer publicly attributing revenue decline to currency in Asia. It is currently search-summary only and the primary release is on a blocked domain.
> **Suggested action:** Find Dyson's FY2025 results release via a third-party reproduction or trade press, and get the exact wording.

> **Area:** Named digital and payments leadership
> **Why it matters:** **No CTO, CIO, Chief Digital or E-commerce officer is publicly identifiable**, and no "Head of Payments" title exists. The open Head of E-Commerce req is the only live signal.
> **Suggested action:** **Run `/enrich` against LinkedIn** for Dyson Singapore e-commerce, digital and payments titles. Web search cannot do this and burned budget trying. ⚠️ **Never write "Mark Brown" — that is the Australian bus and coach operator's CIO.**

> **Area:** ⭐ **The seven markets never reached — ~22% of global traffic**
> **Why it matters:** France (7.82%), Italy (4.21%), Spain (3.59%), Netherlands (1.76%), Poland (1.52%), Belgium (1.28%) and Mexico (1.16%) have **no payment data at all**, in either pass. France alone is larger than Japan.
> **Suggested action:** **Mexico is the cheapest next target** — `dyson.com.mx` is confirmed on the 15-market Magento platform, and the text proxy reaches the non-Korean domains. The EU country scope of the Klarna relationship is also unresolved (a DE/NL/AT three-market claim was refuted 0–3).

> **Area:** ⭐ **Where payments decision authority actually sits**
> **Why it matters:** This determines who the buyer is, and the answer is genuinely unclear. Türkiye's merchant of record is a Dyson entity, but contemporaneous reporting places the Turkey office under a **Middle East regional office in Dubai** — which would be EMEA, not APAC. The UK programmes run through FCA-authorised **Dyson Limited**. The parent is in **Singapore**. The formal parent of Dyson Turkey could not be determined (shareholder fields paywalled).
> **Suggested action:** Resolve whether payments is owned globally from Singapore, regionally, or per-entity before picking a contact. If it is regional, Türkiye may not be yours to sell.

> **Area:** The Korean checkout specifically
> **Why it matters:** Korea is the #2 market and the home of the headline wallet-vs-instalment hook, and it is **the one domain the text proxy cannot reach** — it still returns a Cloudflare challenge. The Korea evidence remains `[SYNTH]` while India's equivalent is now verified.
> **Suggested action:** A browser in Korea, or any route that renders `dyson.co.kr/card-promotion`. Verifying it would make the strongest hook in the file first-hand.

> **Area:** Correct the TAL row
> **Why it matters:** It records **"~$9B global"**. Actual is **£6.13bn (~US$7.7–8.0bn) and declining**. A merchant would catch it.
> **Suggested action:** Update Est. Revenue; add **恆隆行 (HLH)** and **Coway** as new stubs.

### Appendix: All Source URLs

**Verified by me directly**
- DNS enumeration of `{market}-{env}.commerce.dyson.com` with wildcard controls on both `*.commerce.dyson.com` and `*.dyson.com`
- Cloudflare 403 confirmation across the `dyson.*` estate, with a 200 control host
- `dyson.com.tw` → Sedo parking lander
- https://gripsintelligence.com/insights/retailers/dyson.com · https://ecdb.com/resources/sample-data/retailer/dyson · https://gripsintelligence.com/insights/retailers/dyson.co.kr (404)

**Entities & financials:** opengovsg.com (201903799Z, 200711832N, 200517219H) · info.gbiz.go.jp (8010001063616) · zaubacorp.com (U51909HR2017FTC068554) · abr.business.gov.au (50073072509) · find-and-update.company-information.service.gov.uk (01959090, 02627406, 08445070) · channelnews.com.au · bmmagazine.co.uk · nicebizinfo.com · saramin.co.kr
**Payment methods:** shop.dyson.tw/support/TermsAndConditions · rakuten.ne.jp/gold/dyson/sp/info/termsofsale.html · rakuten.ne.jp/gold/dyson/sp/info/faq.html · afterpay.com/en-AU/stores/dyson · detail.chiebukuro.yahoo.co.jp/qa/question_detail/q13263311823 · paypay.ne.jp/notice/20221005/c-dyson/ · apps.apple.com/sg/app/mydyson/id993135524
**Japan 3DS mandate:** jcb.co.jp/merchant/release/emv3-dsecure.html · netshop.impress.co.jp/node/12342 · businesslawyers.jp/articles/1447 · saisoncard.co.jp/merchant/news/guidance/20241008.html
**Complaints:** jp.community.dyson.com (threads 440, 479, 495, 502) · clien.net · coolenjoy.net · productreview.com.au/listings/dyson
**Corporate:** fortune.com · malaymail.com · prnewswire.com/in · asiae.co.kr · builtin.com (job/head-e-commerce/7457531, job/head-it-ecommerce/10008073) · pmo.gov.sg · uk.investing.com
**Competitors:** fintechnews.sg/133226/ai/adyen-agentic/ · koreatimes.co.kr · kedglobal.com · sedaily.com · dreametech.com/pages/payment-method · tmogroup.asia
**Security:** oag.ca.gov/system/files/California%20PINC2020.78%20Notification%202.pdf

</details>
