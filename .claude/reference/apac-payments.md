# APAC Payments Reference

Orientation notes for research and outreach across the APAC territory. Two rules govern
everything in this file:

> **1. This file is a checklist, not a source.** Nothing here may be stated as fact in a
> report or an email on the strength of this document alone. Every market claim, share
> figure, regulatory requirement, and date used in outreach must be verified against a
> live source at research time and cited with a URL.
>
> **2. Regulation moves fast in APAC.** Licensing regimes, tokenization mandates and
> e-mandate rules in India, Indonesia, Vietnam and Japan have all changed inside recent
> 24-month windows. Treat every regulatory line below as "check whether this still holds"
> rather than "this holds."

---

## 1. Why APAC is structurally different from EMEA

The EMEA playbook leans on two pillars that do not transfer cleanly:

| EMEA assumption | APAC reality |
|---|---|
| Interchange is capped intra-EEA (IFR), so cross-border framing only applies outside the zone | No regional cap regime. There is no APAC equivalent of the IFR — no single zone inside which cross-border is fee-neutral. Cross-border framing is **more** available here, not less, but must be argued per corridor. |
| Cards are the default rail, APMs are a conversion add-on | In several of the largest markets cards are the *minority* rail. Account-to-account and wallet rails (UPI, QRIS, PayNow, PromptPay, FPS, DuitNow) are the default consumer behaviour, not an upsell. |
| A single EU entity can acquire across the bloc | Domestic acquiring in India, Indonesia, China, Vietnam and South Korea is effectively gated behind local entity and/or local licensing. "No local entity" is often a *regulatory* blocker, not just a fee inefficiency. |
| Orchestration is greenfield — most merchants integrate PSPs directly | Large parts of the Indian market are already orchestration-aware via Juspay. That changes the pitch from education to displacement. |

**Practical consequence for the ICP matrix:** the "public RFP" signal is rare in APAC and
"local rail / licensing gap" is common and high-value. The scoring matrix in `research.md`
reflects that swap.

---

## 2. Market-by-market orientation

Rails listed are the ones whose absence from a checkout is worth flagging. Percentages are
deliberately omitted — look them up and cite them.

### India
- **Rails:** UPI (dominant for domestic consumer payments), cards (Visa/MC/RuPay),
  netbanking, wallets (Paytm, PhonePe), EMI / no-cost EMI and card instalments.
- **Instalments matter commercially.** High-ticket categories — edtech programme fees,
  travel, electronics, healthcare — commonly convert on EMI. A high-ticket Indian merchant
  with no instalment offering is a conversion story, not just a rails story.
- **Regulatory items to verify per account:** RBI card-on-file tokenization requirements;
  RBI e-mandate framework for recurring/subscription debits (additional factor
  authentication, pre-debit notification, per-transaction ceilings above which AFA is
  required); RBI Payment Aggregator authorisation for anyone handling funds; the separate
  cross-border payment aggregator (PA-CB) regime for import/export flows.
- **Why this is Yuno-relevant:** recurring billing in India is genuinely hard — the
  e-mandate rules break naive card-on-file retry logic that works everywhere else. A
  subscription business billing Indian customers on a global-only stack is a strong lead.
- **Orchestration incumbency:** Juspay is widely deployed. Treat a Juspay account as
  *displacement*, not greenfield — see §4.

### Indonesia
- **Rails:** QRIS (the national interoperable QR standard — a single acceptance mark
  spanning the wallets), bank transfer / virtual account, wallets (GoPay, OVO, DANA,
  ShopeePay), cards as a minority rail, convenience-store cash (Alfamart, Indomaret).
- **Verify:** Bank Indonesia payment-services provider (PJP) licensing categories and
  whether the merchant's flow requires a licensed local partner.
- **Angle:** virtual-account and QRIS coverage is the whole game. A card-only Indonesian
  checkout is leaving most of the market unaddressed.

### China (Mainland)
- **Rails:** Alipay, WeChat Pay, UnionPay. Cards in the Western sense are marginal.
- **Verify:** cross-border collection typically runs through licensed partners; the
  compliance path is the constraint, not the integration.
- **Angle:** usually access and settlement, not routing.

### Japan
- **Rails:** cards (with a strong instalment and bonus-payment culture), konbini
  (convenience-store cash), PayPay, LINE Pay, Rakuten Pay, carrier billing, Paidy (BNPL),
  bank transfer.
- **Verify:** EMV 3-D Secure adoption requirements for e-commerce merchants — Japan moved
  to mandate 3DS for EC sites, confirm current status and deadline before citing it.
- **Angle:** konbini and PayPay absence on a Japan-facing checkout is a concrete gap.
  3DS migration is a live integration-pain hook.

### South Korea
- **Rails:** domestic card networks with local PG intermediation, KakaoPay, Naver Pay,
  Toss, local instalment offerings.
- **Verify:** whether the merchant can acquire domestically without a Korean entity — the
  practical answer is usually no, which makes the entity question a hard gate.
- **Angle:** foreign merchants routinely run Korea cross-border and eat the approval hit.

### Singapore
- **Rails:** cards (high penetration), PayNow, GrabPay, bank transfer.
- **Verify:** MAS Payment Services Act licence classes where the merchant touches funds.
- **Angle:** often the regional HQ but a small share of volume — do not let an SG HQ
  distract from where the transactions actually are.

### Malaysia
- **Rails:** FPX (online banking), DuitNow, Touch 'n Go eWallet, Boost, GrabPay, cards.
- **Angle:** FPX absence is the classic gap on a global-only stack.

### Thailand
- **Rails:** PromptPay, TrueMoney, bank transfer, cards, instalment plans.

### Vietnam
- **Rails:** MoMo, ZaloPay, VNPay / VietQR, domestic bank cards (NAPAS), cash on delivery.
- **Verify:** State Bank of Vietnam licensing for intermediary payment services; local
  entity expectations.

### Philippines
- **Rails:** GCash, Maya, InstaPay/PESONet bank transfer, over-the-counter cash, cards.
- **Angle:** GCash is close to table stakes for consumer flows.

### Hong Kong / Taiwan
- **Hong Kong:** FPS, Octopus, AlipayHK, WeChat Pay HK, cards.
- **Taiwan:** JKOPay, LINE Pay, ATM / virtual-account transfer, convenience-store cash,
  domestic instalments.

### Australia / New Zealand
- **Rails:** cards, PayTo (NPP), BPAY, Afterpay / Zip (BNPL), POLi (NZ, verify current
  availability), Apple/Google Pay.
- **Verify:** RBA interchange standards and least-cost-routing expectations for
  card-present and increasingly card-not-present — a live cost-of-acceptance angle.
- **Angle:** ANZ merchants are the most "Western-looking" stacks in the territory, so the
  EMEA-style routing and failover pitch lands most directly here.

### Pakistan / Bangladesh / Sri Lanka
- **Rails:** wallets (JazzCash, Easypaisa in PK; bKash, Nagad in BD), bank transfer, cash
  on delivery, limited card penetration.
- Usually secondary markets — flag only when traffic justifies it.

---

## 3. Cross-border framing in APAC

There is no IFR-equivalent cap, so the EMEA caution ("do not claim interchange premium
intra-zone") does not apply. What does apply:

- **Argue the corridor, not the region.** "APAC cross-border" is meaningless. "Cards issued
  in India processed against a Singapore entity" is a claim you can support.
- **Approval rate is usually the stronger argument than fee.** Domestic issuers in India,
  Indonesia, Japan and Korea decline foreign-acquired transactions at materially higher
  rates than local-acquired ones. This is well documented per market — find the citation
  rather than asserting a number.
- **FX is a second line.** Multi-currency pricing across a dozen APAC currencies carries an
  FX leg that sits outside any card-scheme cost discussion.
- **Regulatory gating is the third and strongest.** In markets where domestic acquiring
  requires local presence, "you cannot access the local rail at all" beats any fee argument.

**Diaspora flows are a distinct and underrated pattern.** An Indian or Southeast Asian
content, remittance or services business billing its diaspora in the US, UK, Gulf, Australia
and Canada is running *outbound* cross-border from an APAC base — the mirror image of the
usual pattern, and typically on a stack chosen for the home market. Check the traffic split
before assuming the home market is where the payment pain is.

---

## 4. Juspay and the displacement motion

The target account list flags confirmed Juspay merchants. These are **not** greenfield and
must not be pitched as if they were.

**What changes:**
- They already believe in orchestration. Skip the education layer entirely.
- The Phase 1 observation cannot be "you have no orchestration layer" — that is factually
  wrong and burns the thread.
- The argument shifts to coverage and reach: global PSP and APM breadth beyond the home
  market, multi-region routing, and international expansion the incumbent was not built for.
- Confirm current status before writing. A merchant list is a snapshot; relationships end.

**What does not change:** the never-name-competitors rule in `full-outreach.md`. Position on
what Yuno adds, not on who is being replaced.

---

## 5. Vertical notes for this territory

- **OTT / streaming with diaspora audiences** — cross-border subscription billing, recurring
  auth across many issuer geographies, involuntary churn. Check whether billing is web or
  app-store; app-store-dominant revenue is largely untouchable by orchestration.
- **Airlines / OTA / travel** — high ticket value, multi-currency, peak-load routing,
  instalments in India/Japan/Taiwan, and cross-border on inbound bookings. Approval rate on
  a high-ticket booking is a direct revenue number.
- **EdTech** — high-ticket programme fees, instalments and EMI, recurring collection under
  the India e-mandate rules, and international student payments.
- **Gaming / esports** — many small transactions, wallet and carrier-billing rails, high
  decline sensitivity, frequent new-market entry.
- **Crypto / digital assets** — acquirer appetite and MCC-driven declines dominate;
  acquirer diversification is the whole pitch. Check local legality per market first.
- **Super apps / marketplaces / q-commerce** — split payouts, multi-corridor settlement,
  local rail coverage per country.
- **SaaS / B2B / AI** — do not lead with APM gaps. Lead with cross-border card processing,
  approval rates by issuer geography, and failover.
- **PSPs / payment infrastructure** — out of ICP. Stop and flag.
