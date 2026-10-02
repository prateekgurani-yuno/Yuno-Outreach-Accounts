# Travelex Japan

**Status:** 🟢 Ready to outreach — research complete, sequence not yet drafted
**ICP Score:** 21 / 29 → ⭐ **High Priority**
**Industry:** Foreign-exchange retail + licensed funds transfer (remittance) + prepaid card issuing · **HQ:** Tokyo, Japan — トラベレックスジャパン株式会社, 法人番号 **3010401058641**; group parent UK · **Researched:** 2026-10-02 · **First email sent:** —
**Motion:** **Greenfield** — no orchestrator detected. Direct, per-market, brand-by-brand integrations. **But read the counter-argument in Section 10 before drafting: the Mastercard skew may be contractual, not neglect.**

---

> ## 🎯 THE HOOK — a Japanese customer holding a Visa card cannot buy currency online from Travelex
>
> **Verified first-hand, from Travelex Japan's own page** (`travelex.co.jp/travelex-online`, fetched 2026-10-02):
> > 「クレジットカードでも購入可能 **Mastercard、ライフカードのクレジットカード決済、銀行振込と代金引換支払いからお選びいただけます。**」
> > *"Purchase by credit card is also possible — you may choose from **Mastercard, Lifecard credit card payment, bank transfer, and cash on delivery.**"*
>
> Their own 2025-01-20 press release is more precise: 「**Mastercardおよびライフカード発行のJCB/VISA**」 — *Mastercard, and JCB/VISA **issued by Lifecard***. So Visa and JCB work only if the issuer happens to be Lifecard.
>
> ### Set that against the UK, same company, same product, same front-end template
> | | **Japan** | **United Kingdom** |
> |---|---|---|
> | Card schemes | **Mastercard + Lifecard-issued only** | **Visa · Mastercard · Maestro** |
> | Wallets | **None** | **Apple Pay · Google Pay** |
> | Local methods | 銀行振込 (bank transfer), **代金引換 (cash on delivery, ¥330 fee)** | — |
> | Order cap | ¥300,000/order · ¥600,000/day · ¥1.5m/30 days | not published |
>
> ### ⭐ And the tokenization layer is configured for cards the acquiring side does not accept
> I decoded the Cybersource `captureContext` JWT that each checkout hands the browser. **`allowedCardNetworks` is byte-identical on the Japanese and UK checkouts:**
> ```
> VISA, MAESTRO, MASTERCARD, AMEX, DISCOVER, DINERSCLUB, JCB, CUP, CARTESBANCAIRES
> ```
> **The Japanese card field is configured to tokenize Visa, JCB, UnionPay — and Cartes Bancaires, a French domestic scheme — while the published acceptance is Mastercard plus one issuer.** Those two facts are both theirs. The gap between them is the opening question, not a claim about what the customer experiences — I never reached the live payment step.
>
> ### The fix propagates across a white-label estate
> Travelex Japan runs co-branded online FX ordering for **JTB, IACE Travel, 77 Bank, KMP, Lifecard** under `/onlinex/{partner}`, plus partner-hosted pages at **Ashikaga Bank, 82 Bank, Toho Bank, Chugoku Bank and ANA**. **Every partner channel inherits the same restricted method set.** This is not a single-merchant fix.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Travelex Japan KK is the Japanese arm of UK-headquartered Travelex — retail currency exchange at airports and city stores, **online currency ordering with home delivery** (`buy.travelex.co.jp`), mail-in buyback, wholesale banknotes, and the Travelex Money Card / キャッシュパスポート prepaid multi-currency card. Established **March 2003**, capital **¥100,000,000**, 100% subsidiary, representative director **大谷 淳**. **資金移動業者 関東財務局長第00001号** — registration number *one* on Japan's funds transfer register, Type II, active as of 31 July 2026, one of only 84 providers nationally.

**SimilarWeb total visits:** 🛑 **Group-scope only, NOT Japan.** Supplied pull is `travelex.co.uk` +19 domains — see `accounts/traffic/travelex-japan.md`. Japan is **15.40%** of *group* traffic (#2 globally behind Australia 19.16%), **▼9.98%**. **A Japan-scoped pull is still required.**

### Top 5 markets (group traffic — see scope warning)
| Rank | Country | Traffic | Accepted methods | Missing methods | Local entity |
|---|---|---|---|---|---|
| 1 | 🇦🇺 Australia | 19.16% ▼2.72% | Visa · Mastercard · **PayID** · **BPAY** | PayTo, POLi, Afterpay/Zip, Apple/Google Pay — all Not found | ✅ Travelex Australia Holdings Pty Ltd |
| 2 | 🇯🇵 **Japan** | **15.40%** ▼9.98% | **Mastercard · Lifecard-issued Visa/JCB · 銀行振込 · 代金引換** | **コンビニ決済 · ペイジー · PayPay · 楽天ペイ · d払い · au PAY · LINE Pay · メルペイ · Apple Pay · Google Pay · 分割払い — all Not found** | ✅ Travelex Japan KK |
| 3 | 🇳🇱 Netherlands | 14.80% ▲0.53% | Not researched — **EMEA territory** | — | ✅ Travelex N.V. (gwktravelex.nl) |
| 4 | 🇬🇧 United Kingdom | 8.72% ▼7.33% | Visa · Mastercard · Maestro · Apple Pay · Google Pay | Amex, PayPal, open banking, BNPL — Not found | ✅ Travellers Exchange Corporation Ltd |
| 6 | 🇳🇿 New Zealand | 5.15% ▼22.45% | Visa · Mastercard · "Bill Payment" | POLi / Account2Account — Not found | ✅ Travelex Financial Services NZ Ltd |

*⚠️ A search summary returned "PayID" for New Zealand. **PayID is an Australian NPP service and does not exist in NZ** — treated as cross-market bleed and excluded. Verify `travelex.co.nz/faq` before using the NZ row.*

### Legal entities — APAC (company's own group list, correct as of 21 April 2026)
**Travelex Japan KK** · Travelex Currency Exchange & Payments Sdn Bhd (MY) · Travelex (Thailand) Ltd · Travelex Currency Exchange (China) Ltd · Travelex Holding (HK) Ltd + Travelex Card Services Ltd · Travelex Holdings (S) Pte Ltd · Travelex India Pvt Ltd · Travelex Australia Holdings Pty Ltd + Travelex Limited (Australia) · Travelex Financial Services NZ Ltd
**Chain:** Barings **51.49%** (at 31 Dec 2025) + Vector / Corre / Mariner (>95% combined) → **Travelex International Limited** → **Travelex Acquisitionco Limited** → **Travelex Japan KK**
❌ **No entity in Indonesia, Korea, Philippines, Vietnam or Taiwan** — and Indonesia is the fastest-growing market in the traffic at ▲344.57%.

### Known PSPs
| Layer | Finding |
|---|---|
| **Card tokenization** | ✅ **Cybersource Flex Microform v2.0.2** — confirmed by me on **both** `buy.travelex.co.jp` and `checkout.travelex.co.uk`, by decoding the `captureContext` JWT each page serves (`iss: "Flex API"`, `clientLibrary: flex.cybersource.com/microform/bundle/v2.0.2/flex-microform.min.js`) |
| **Hosts** | `flex.cybersource.com` · **`flex.cybersource-travelex.securedataplatform.co.uk`** — a Travelex-branded Cybersource endpoint on a **`.co.uk`** domain, present on the **Japanese** checkout · `api.travelex.net` · `prod.cpsmt.mhshosting.com` |
| **Acquirer** | ❌ **NOT ESTABLISHED.** Cybersource is Visa-owned and is a gateway; who acquires is unknown. **Do not name an acquirer.** |
| **Japan card arrangement** | **Mastercard (any issuer) + Lifecard-issued Visa/JCB.** A bilateral issuer deal, not a scheme-wide acceptance — first-party sourced |
| **3DS** | ❌ Not established. No 3Dセキュア / 本人認証サービス reference found, but the live payment step was never reached |
| **ATM estate** | **NCR Atleos** — 2024 network overhaul (separate from checkout) |

### Orchestration status
**None detected — direct, per-market, brand-by-brand integrations.** Evidence: (1) the Japan and UK checkouts share a front-end template and a Cybersource version yet expose materially different method sets; (2) Japan's card acceptance was built **one press release at a time** — JCB only until Dec 2018, then Mastercard and Lifecard added; (3) no orchestration vendor appears anywhere. **Greenfield.**

### Buying signals
- 🔴 **Q1 2026: revenue £93.8m, down £22.3m YoY; underlying EBITDA LOSS £2.9m**, £3.7m adverse. Company language: *"continues to focus on cost discipline and operational efficiency."* → **approval-rate and cost-of-acceptance framing. Growth framing will not land.**
- 🏗️ **Group Transformation Programme live; 2025 Oracle cloud migration completed** — a systems-change window, from their own FY2025 governance statement
- 💻 Stated pivot to *"self-serve, home delivery, e-commerce and new digital products (one of the fastest growing areas)"*
- 🇦🇺 **Sydney Airport named Travelex its FX partner (24 June 2026)**; Hobart Airport sites added July 2026; Fukuoka (Japan) won 2025
- 🇯🇵 **INR, KHR and TRY added to Japanese online home delivery, 20 Jan 2025** — the release that restates the Mastercard/Lifecard constraint
- 💳 **777,000 Travelex Money Cards in circulation globally, +29% YoY; reloads +26%; reload penetration +50%**
- 🤝 **Travelex × Everyday Rewards (Woolworths, AU), 5 Aug 2026** — loyalty tied to checkout
- ⚠️ **Sale process still open.** Owners exploring a sale since Sept 2023 (Barclays, Smith Square Partners). No transaction announced. Cuts both ways — test it in discovery, do not assume.

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach Travelex Japan`.*

⚠️ **Read before drafting.**
1. **Lead with the Visa question, phrased as a question.** See the counter-argument in Section 10 — the Mastercard skew may be contractual. *"What would it take to add Visa, JCB and PayPay?"* lands; *"you're leaving money on the table"* ends the conversation if scheme exclusivity exists.
2. **Never say they need orchestration** — actually here you may, motion is greenfield. But **do not** say the Japanese stack is bad; say it is *different from the UK's*, which is their own fact.
3. **Do not use the Nuvei "4% authorisation uplift" or "5% multi-acquirer" figures.** Competing vendor, anonymous airline, not an FX reference.
4. **Do not claim a competitor uses orchestration.** No FX, travel-money or remittance business has a public orchestration case study. Verified absent.
5. **Do not use group loss figures as a taunt.** Q1 2026 cost discipline is context for *framing*, not a line in an email.
6. **Never state "Travelex Japan rejects Visa" flatly.** The precise, defensible form is their own wording: Mastercard, and JCB/VISA issued by Lifecard.
7. **The white-label estate is the multiplier** — JTB, IACE, 77 Bank, Ashikaga, 82 Bank, Toho, Chugoku, ANA, Lifecard all inherit the same method set.

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 21 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ⚠️ **NOT FOUND — ASSUMED ~100,000+/month.** `[ASSUMPTION — not researched.]` Basis: group ~15m retail transactions/year `[UNVERIFIED — press]` ÷ 12 ≈ 1.25m/month; Asia is 16.8% of group revenue (£80.2m / £477.2m, **audited**) → ~210k/month Asia; Japan is the largest Asia market by stores and traffic. **Only the revenue share is sourced; every later link is not.** An assumption never rejects, so the implied ≥100,000 band is scored and the row marked ⚠️. |
| Orchestration status | **+4** | ✅ **None detected — greenfield.** Per-market brand-by-brand integrations; no orchestrator found |
| 3+ countries | **+3** | ✅ Audited Asia segment = Japan, China, Malaysia, Singapore, Hong Kong; plus AU, NZ, India, Thailand entities |
| Multiple PSPs | 0 | ⬜ Only Cybersource confirmed. The Japan Mastercard/Lifecard arrangement implies separate acquiring but is **not confirmed as a second PSP** |
| **Local rail / licensing gap in a top-3 market** | **+3** | ✅ **Japan is the #2 market and the online checkout carries no konbini, no Pay-easy, no PayPay, no Rakuten Pay, no d払い, no au PAY, no LINE Pay, no merpay.** Sourced from Travelex Japan's own published method list, not inferred |
| Recent expansion | **+2** | ✅ Sydney Airport FX partner (Jun 2026), Hobart (Jul 2026), Fukuoka (2025), INR/KHR/TRY added to JP online (Jan 2025) |
| Payment issues reported | **+2** | ✅ Moderate. Visa-unavailability named as customer dissatisfaction on JP comparison sites; refund delays and declines-despite-balance recurring on Trustpilot/productreview AU+UK |
| Funding >$10M | 0 | ❌ No round. Capital structure is the 2020 restructuring notes |
| High traffic outside home | **+2** | ✅ UK is 8.72% of group traffic, far below 60% |
| Competitor using orchestration | 0 | ❌ **Verified absent** — no FX, travel-money, bureau-de-change or remittance business has a public orchestration case study |
| Payment job postings | 0 | ❌ Searched; ~84 open roles, all retail plus one generic engineering manager |

**Tier:** ⭐ **High Priority (17+).**
> **Score moved 12 → 21** once Phases 2–3 ran. The earlier 12/29 was depressed by unrun research, exactly as flagged.

### Source Notes — what I verified personally vs what came from agents
- ✅ **Mine, first-hand:** the Japanese tender sentence (fetched `travelex.co.jp/travelex-online`); the Cybersource `captureContext` JWT decode on both checkouts; `allowedCardNetworks` identical JP vs UK; zero Japanese rails in the JP checkout shell; the FSA register PDF; the audited FY2025 regional revenue table; the group companies list
- ⚠️ **Agent-sourced, page-fetched:** UK footer logo set; GPA cash-on-delivery-only; World Currency Shop no online channel
- ⚠️ **Search-summary only — verify before quoting:** every individual complaint; the ¥50bn figure; store counts; Q1 2026 figures; Barings 51.49%

### ⭐ Resolving the one conflict in this research
My Cybersource decode showed the Japanese checkout configured for **nine card networks including Visa**. Travelex Japan's own page says **Mastercard + Lifecard-issued only**. These are not contradictory: **Flex Microform's `allowedCardNetworks` governs client-side tokenization and brand detection, not acquiring.** The tokenizer is permissive; the acquiring is narrow. **I did not reach the live payment step, so I cannot say what happens to a Visa entered there** — and the file must not claim otherwise. Stating both facts side by side is the strongest honest version.

### Conflicts flagged, not resolved
| Item | Values seen |
|---|---|
| **Licence registration date** | 平成22年4月1日 (**1 Apr 2010**) from the FSA register PDF vs 令和2年3月9日 (**9 Mar 2020**) from a second source. **Unresolved** |
| Japan store count | ~79 (2017) · **60+** (Jan 2025) · 83 (agent). Three figures |
| Employee count (Japan) | 260 / 317 / 356. **Do not quote one** |
| Japan minimum order value | ¥10,000 vs ¥30,000 from bank co-brand pages. Official FAQ gives maxima only |
| JCB online | Was the *only* online brand pre-Dec-2018; now absent from the online list. **Dropped, or narrowed to Lifecard-issued?** Inference from two sources, not an announcement |
| Nium (HK remittance, 2021) | **Silent since launch.** Neither confirmed live nor dead |

### Environment notes
- All Travelex domains fetch at HTTP 200. **`buy.travelex.co.jp` and `checkout.travelex.co.uk` both redirect to `/Error/SessionExpired`** — session-gated SPAs — but the app shell still carries the full payment config, which is where the Cybersource evidence came from.
- Same error path with only a locale prefix (`/jajp/` vs `/gb/`), same `api.travelex.net`, same Cybersource version ⇒ **one platform, locale-prefixed**, not separate per-market builds. *(I speculated earlier that different checkout domains meant different stacks. That was wrong.)*
- JP checkout shell: **zero** hits for コンビニ/ローソン/ファミリーマート/セブン/銀行振込/ペイジー/PayPay/楽天ペイ/d払い/au PAY/LINE Pay/メルペイ/代金引換/分割, control passing at 30 hits for 円/JPY/日本. ⚠️ **Shell, not the live payment step — phrase as "nothing in the checkout references a Japanese rail", never "they don't support konbini."**
- **New false positive for the running list: `captureContext`** (a Cybersource Flex field) matches a grep for **`econtext`**, the Japanese PSP. It appears on both checkouts.

### Section 11 — Competitors
**Japanese retail FX has almost no card-acceptance stack to displace**, which makes Travelex's digital channel a genuine differentiator rather than a laggard:
- **GPA / Greenport Agency** (Narita Airport's own subsidiary) — online store is **cash on delivery via Japan Post only**: 「※クレジットカードでのお支払はできません」. Page-verified. Zero online card acceptance.
- **World Currency Shop** (MUFG / Tokyo Credit Services) — **no online channel at all.** Page-verified.
- **Revolut and Wise** — both build in-house **and now sell acquiring** (Revolut publishes Payment Processing Services Agreements; Wise publishes HK acquiring terms). UK-HQ. **Route to Partnerships, do not pitch.**
- Substitution pressure on Travelex Japan: **Sony Bank WALLET** (10 currencies, no per-transaction FX fee when pre-funded), **SMBC Trust GLOBAL PASS** (18 currencies), **Seven Bank ATMs** (inbound). This is the structural reason the store estate is shrinking.

**Prospects found in the sweep, none currently in `accounts/apac-tal.csv`:**
🇮🇳 **BookMyForex** — online-first FX with ordering + delivery, the closest structural analogue to Travelex's model in APAC; apparently single-PSP on Razorpay since 2017 · 🇮🇳 **Thomas Cook (India)** — listed, just launched a 0%-markup forex card into a price war · 🇯🇵 **GPA** — verified zero online card acceptance, but a **first-PSP** conversation, not orchestration, and NAA ownership means slow procurement · 🇮🇳 **Niyo Global**

### Section 10 — 🛑 The counter-argument to hold before drafting
**The Mastercard skew is probably not an accident.** The Travelex Money Card is a **Mastercard-branded** product issued under the Japanese 資金移動業 licence, and Cash Passport is licensed from **Mastercard Asia/Pacific Pte Ltd**. There may be a commercial scheme arrangement that makes Mastercard-first deliberate. **Lead with "what would it take to add Visa, JCB and PayPay" as a question.** If scheme exclusivity exists, an accusatory framing ends the thread on the first email.

### Section 12 — Business Case Data
| Metric | Value | Source |
|---|---|---|
| Group revenue FY2025 | **£477.2m** (FY2024 £511.1m, ▼6.6%) | Audited consolidated statements |
| **Asia segment revenue FY2025** | **£80.2m** (▲2.2%; ▲3% constant currency) — **#2 region, one of only two that grew** | Audited, Note 4 |
| Q1 2026 | Revenue **£93.8m** (▼£22.3m YoY); underlying **EBITDA loss £2.9m** | `[UNVERIFIED — search summary]` |
| Travelex Japan KK revenue | **No reliable public figure.** KK accounts not publicly filed | — |
| **Monthly transaction count** | ⚠️ **ASSUMED ~100,000+/month** — see the ICP row for the chain and why it is an assumption | — |
| Japan order limits | ¥300,000/order · ¥600,000/day · ¥1.5m/30 days; shipping ¥990 under ¥100k, free above; COD fee ¥330 | travelex.co.jp/faq |

### Overall Research Confidence
**MEDIUM–HIGH.** The payment-method picture, regulatory status, entity map, ownership chain and regional revenues are all primary-sourced — several fetched and extracted by me directly. **Two caps remain:** the live payment step was never reached in either market, so the acquirer, 3DS and card-input mechanism are unknown; and the traffic is **group-scoped, not Japan-scoped**.

### Manual Research Recommendations
> **Area:** The live Japanese payment step. **Why:** names the acquirer and settles what happens to a Visa. **Action:** walk `buy.travelex.co.jp` to payment with a real session from a Japanese IP, DevTools open.

> **Area:** Japan-scoped SimilarWeb. **Why:** supplied pull is the global group. **Action:** pull `travelex.co.jp`, `travelex.jp`, `buy.travelex.co.jp`.

> **Area:** `travelex.co.jp/legal/travelex-online-terms-and-conditions`. **Why:** likely the authoritative method list, refund timing and authorisation handling; would also settle the minimum order value.

> **Area:** The 2010-vs-2020 licence date conflict. **Why:** "registration number one, since the regime began" is a strong line and must be right. **Action:** confirm against the Kanto Local Finance Bureau listing.

</details>
