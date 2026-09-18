# EVA Air

**Status:** 🟡 Research complete — outreach not yet generated
**ICP Score:** 15 / 29 → 🟢 **Medium**
**Industry:** Airlines (long-haul international, cargo-heavy) · **HQ:** Taoyuan/Taipei, **Taiwan** — EVA Airways Corp, Evergreen Group, **TWSE 2618** · **Researched:** 2026-09-18 · **First email sent:** —
**Motion:** **Greenfield** — none detected. ⚠️ The "no orchestrator" half rests largely on absent search hits, but there is affirmative counter-evidence of **in-house payment engineering** (see 3B).

> ⚠️ **DISAMBIGUATION — get this right.** EVA Air is Taiwanese (TWSE **2618**), and is **not** China Airlines (also Taiwanese, TWSE **2610**), nor any mainland Chinese carrier. Its regional subsidiary is **UNI Air 立榮航空**.

---

> ## 🎯 THE HOOK — the checkout takes a Dutch bank rail and not one Taiwanese one, and it refuses corporate cards outright
>
> **Both halves verified by me directly**, from EVA's own zh-TW booking terms, cross-checked against the FAQ on a snapshot six months apart. Both pages carry the identical closed list.
>
> **1. The complete published method set, verbatim:**
>
> > 「付款方式 長榮航空網路購票提供以下付款方式，**不同出發地可使用的付款方式不同**…
> > **信用卡/借記卡：** VISA卡 · 萬事達卡Master Card · 美國運通卡American Express · JCB · Discover卡 · **UATP**
> > **其他付款方式：** PayPal · 銀聯卡Union Pay · **iDeal** · 支付寶」
>
> **That is the whole list.** Note their own caveat — *different departure points have different available methods* — which makes this the **union** across every market. **A rail absent from this list is absent everywhere.**
>
> **Absent from it: 信用卡分期付款 (instalments) · 超商代收 (7-ELEVEN/FamilyMart/ibon) · 虛擬帳號/ATM轉帳 · LINE Pay · JKOPAY 街口 · Taiwan Pay · Apple Pay · Google Pay · WeChat Pay.** I grepped both pages: **zero hits for 分期, 超商, ATM, LINE Pay, 街口 or Apple Pay.**
>
> **A Taiwanese flag carrier whose checkout supports Dutch iDeal bank transfer and no Taiwanese local rail at all** — on a six-figure-NTD long-haul product, in the market where instalments are *the* mechanic for high-ticket travel.
>
> **2. They refuse corporate cards. In writing. While running a UATP corporate programme.**
>
> > 「由於商務卡/公司卡不受3DS認證政策的保護，為了您的交易安全，**本系統不接受以商務卡/公司卡進行交易**。」
> >
> > *"Because commercial/corporate cards are not protected by the 3DS authentication policy, for your transaction security, this system does not accept transactions with commercial/corporate cards."*
>
> **UATP — an airline corporate-settlement rail — is accepted four lines above it on the same page.** They have built for corporate travel and then closed the web channel to the instrument corporate travel actually uses. That is a self-imposed approval ceiling, and it is their own words.

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** EVA Air is Taiwan's second flag carrier and an Evergreen Group company. **FY2025 consolidated revenue NT$220,333mn (NT$2,203.33億) — the second-highest in company history**, with December 2025 setting an all-time monthly record at NT$20,261mn.

**SimilarWeb total visits:** **Not obtained.** No data supplied, and `evaair.com` returns **HTTP 403** to every automated fetch. Country profile unverified; **no split invented.**

### 🔒 3DS is a hard gate, not risk-based — and it has a manual failure mode
- **Mandatory since 2021-03-02:** every ticket purchase, change and ancillary requires a 3DS-capable card, with EVA's own page warning 「以避免交易**失敗**」.
- **If the card is not 3DS-verified, the passenger must present the physical card at an airport counter** — 48 hours or at minimum 1 hour before departure — and sign a 「長榮航空網路購票為他人付款同意書」.
- **Verified verbatim, and the consequence is severe:** 「若未能出示購票信用卡，旅客應於現場依票面價支付機票款，另購機票登機，**否則本公司將拒絕旅客搭機**」 — *fail to produce the card and you buy a new ticket at face value or you are refused boarding.*

> 📌 **That is a fraud-control policy being paid for in airport staff time and denied boardings.** It is the operational cost of having no risk-based alternative to a blanket 3DS mandate.

### Other first-party payment facts
- **PayPal is blocked for Taiwan-registered PayPal accounts** — 「若您PayPal帳號註冊地為台灣，將目前無法使用PayPal進行交易」
- **Refund SLA:** 7 working days back to the original card, 1–2 statement cycles to appear; **20 working days** where the original purchase was cash or cheque
- **Fare Lock (「保留您的票價」)** is live and bills as its own separate transaction — **and cannot be paid with miles**
- **Miles + Cash is NOT supported** as a tender

### Known PSPs
**None. Zero PSPs, gateways or acquirers identified.** The zh-TW **privacy policy was read in full** and names no 金流服務商 — only generic 「金融機構」 and an unenumerated 「委外廠商」 category.

> ⚠️ **A research heuristic failed here and it is worth recording.** Taiwanese merchants usually name their gateway in the 隱私權政策. **EVA's does not** — it is drafted to GDPR/CPRA/PDPA structure, not the local SME e-commerce template. **Do not expect vendor disclosure from this company.**

**One affirmative acquiring signal, and it is architectural.** EVA's own 2023-09-11 newsroom release states it built a **real-time in-flight card authorisation mechanism over satellite Wi-Fi from 2014**, and certified it directly with 「**收單銀行**」 (an acquiring bank) and multiple card schemes. The acquirer is unnamed — but **this is a company doing its own payment engineering, not buying a turnkey layer.**

### UNI Air (立榮航空) — separate stack, confirmed
`uniair.com.tw` is **not** behind Akamai and serves fine. Completely separate booking engine — classic **ASP.NET WebForms** at `/rwd/B2C/booking/ubk_search.aspx` versus mainline `booking.evaair.com/flyeva/eva/b2c/booking-online.aspx`. Its accepted methods are narrower still: 「您可以使用**信用卡或銀聯卡**付款」 — **VISA, MasterCard, JCB, American Express, 銀聯卡 only.**

### Buying signals
- 💳 **The corporate-card refusal**, against a live UATP corporate programme
- 🇹🇼 **Zero Taiwanese local rails** on a high-ticket product in an instalment-driven market
- 🔒 **A blanket 3DS mandate with an airport-counter manual fallback**
- 📈 **FY2025 revenue NT$220.3bn**, second-highest ever; December an all-time monthly record
- 🛫 **Fleet and network growth** — 24× A350-1000 on order (deliveries 2027–2033), A321neo order, ~US$1.94bn for four more 787-9s `[UNVERIFIED]`
- ❌ No payment RFP, no payments hire found

</details>

<details open>
<summary><h2>✉️ Section 2 — Full Outreach</h2></summary>

*Not yet generated. Run `/full-outreach EVA Air` to draft the 12-touch sequence.*

**Four instructions for whoever drafts it:**
1. **The iDeal-versus-no-Taiwanese-rails contrast is the opener.** It is a single sentence, it is from their own page, and it needs no interpretation.
2. **The corporate-card refusal is the second observation and it is the sharper of the two commercially** — it is revenue they are declining on purpose, alongside a UATP programme aimed at exactly those buyers. Use the diplomatic clause; it was a security decision, not carelessness.
3. **Say the cargo caveat out loud.** Roughly a quarter of EVA's revenue is freight, invoiced B2B and outside any card checkout. Naming it unprompted is the most credibility-building move available on this account.
4. **Do not assert an acquirer, a PSS vendor, or Amadeus.** Nothing is established. The `.aspx` booking front end argues against an Amadeus-hosted retail layer but proves nothing about the PSS.

**Never claim:** that EVA uses Amadeus (unverified in both directions), any PSP name (zero identified), that ATM transfer is available (a search summary asserted it; **I grepped both first-party pages and found zero ATM hits — treat the summary as wrong**), or anything from the complaint corpus (see Source Notes).

</details>

<details>
<summary><h2>📚 Section 3 — Full Research</h2></summary>

### ICP Score breakdown — 15 / 29
| Signal | Points | Status |
|--------|--------|--------|
| **Monthly transaction count** | **+5** | ✅ **DERIVED as a bound.** Sourced input: **FY2025 consolidated revenue NT$220,333mn**, verified by me at 工商時報. December 2025 split — passenger NT$12,676mn vs cargo NT$5,300mn — implies passenger ≈63% of revenue, so the card-addressable line is roughly **NT$140bn/year**. **Presented as a bound because the divisor is unsourced:** even at an implausibly high **NT$60,000 (~US$1,850) per booking**, that is ~2.3m bookings/year = **~194k/month**. ⚠️ **Two honest deductions**: ~25% of revenue is cargo, invoiced B2B and outside a card checkout; and an unknown (likely majority) share of tickets sells through GDS and travel agents, never touching evaair.com. **Every plausible divisor still clears 100k**, hence ✅. **Do not compute a transaction count from the 13.33m passenger figure** — it is unverified and PNRs carry up to 9 tickets. |
| Orchestration status | **+4** | ✅ **None detected.** ⚠️ **State the basis honestly on the call:** the "no orchestrator" finding is mostly absent search hits. The affirmative evidence points at **in-house payment engineering** (the 2014 in-flight authorisation build, certified directly with an acquiring bank). Combined with a checkout offering iDeal but no local rails — the signature of a single platform's **stock LPM menu** rather than a curated routing layer — the read is single-acquirer, no orchestration. **Moderate confidence. Do not assert a vendor.** |
| 3+ countries | **+3** | ✅ Site locale footprint: 台灣, 香港澳門, 中国大陆, 日本, 대한민국, Việt Nam, ประเทศไทย, Indonesia, plus North America and global. Long-haul to North America and Europe. |
| Multiple PSPs | **0** | ⬜ **Zero PSPs identified** — not "they have one". The privacy policy, booking terms and FAQ were all read in full in Chinese and name none. |
| Local rail or licensing gap in a top-3 market | **+3** | ✅ **The best-sourced row, and the strongest rail evidence in this repo.** Taiwan is the #1 market. **Instalments, 超商代收, ATM transfer, LINE Pay, JKOPAY, Taiwan Pay, Apple Pay and Google Pay are all absent from an exhaustive first-party list I read twice, from two snapshots six months apart** — and EVA's own wording confirms the list is the **union across all departure markets**, so absence from it means absence everywhere. Meanwhile **iDeal**, a Dutch rail, is present. |
| Recent expansion | **0** | ⬜ **Not awarded — unverified.** TPE–Dallas/Fort Worth (Oct 2025) and TPE–Washington Dulles (Jun 2026) launches, plus New Delhi/Boston/Helsinki under evaluation, are all `[UNVERIFIED — search summary only]`. **Verifying any one of them likely makes this +2.** New Delhi would be directly relevant — INR, UPI and RBI card-on-file tokenisation would all land on this checkout. |
| Payment issues reported | **0** | ⬜ **Not awarded, deliberately.** Complaint threads were identified (PTT Aviation duplicate-charge 2016, payment-page errors, Dcard booking failures) but **zero were actually read** — every one is search-summary paraphrase. **I do not award points on unverified data**, and none of it may be quoted. See Source Notes. |
| Funding >$10M | **0** | ❌ TWSE-listed. No round. |
| High traffic outside home | **0** | ⬜ No traffic data. Cannot verify either way. |
| Competitor using orchestration | **0** | ❌ **Not established, and the honest read cuts against us.** EVA's closest peer is **China Airlines**, whose own file in this repo scores it greenfield with no orchestration. Singapore Airlines runs a competitor's layer and overlaps EVA on long-haul, but it is not the like-for-like Taiwanese comparison. |
| Payment job postings | **0** | ⬜ None found. |

**Tier: 15 / 29 → 🟢 Medium.** No analyst override applied.

> **The score understates the outreach quality and it is worth saying why.** Four rows are zero because things are *unverified* rather than absent — expansion, complaints, PSPs, competitor adoption. **The two hooks are among the best-evidenced in this repo**, both verbatim first-party and both verified twice. This is a 15 with a much stronger opening than several higher-scoring accounts.

### Source Notes
- ✅ **The complete method list, the corporate-card refusal, the 3DS mandate, the airport card-verification penalty, the PayPal Taiwan block and the refund SLA were all verified by me directly**, from two independently snapshotted EVA pages (2026-03-11 booking terms and 2026-09-11 FAQ). Grep counts for 分期/超商/ATM/LINE Pay/街口/Apple Pay were **zero on both**.
- ✅ **FY2025 revenue NT$2,203.33億 verified by me** at 工商時報, 2026-01-09: 「累計整體2025年合併營收達2,203.33億元，創下歷史次高」. Same article gives the December record and its passenger/cargo split.
- ⚠️ **`evaair.com` returns HTTP 403 to curl AND to WebFetch** (Akamai, `errors.edgesuite.net` reference IDs). **Everything first-party here came via `web.archive.org` snapshots.** Re-confirm from a browser before quoting.
- ⚠️ **A search summary asserted 網路ATM transfer is available for Taiwan-origin itineraries with a NT$100k daily cap. I could not find that text on either page and grep returned zero ATM hits. Treat it as wrong or stale — do not put it in an email.**
- ⚠️ **The FY2025 passenger/cargo split (passenger NT$140,344mn, cargo NT$54,759mn, 13.33m passengers, 77.8% load factor)** is `[UNVERIFIED — search summary only]`. **It is corroborated by the December split I did verify**, which lands in the same place, so it is directionally safe — but do not quote the exact figures.
- ⚠️ **The complaint corpus is entirely unread.** PTT threads, Dcard, Threads and app-store reviews were all identified but none fetched. A search summary paraphrases an "error 15" at the payment step and cases of a booking reference issuing without payment completing — **that pattern would be a textbook auth-captured-but-order-not-created desync, and it is exactly the kind of thing we must not quote unverified. Do not use "error 15" with a prospect.**
- ❌ **Whether EVA runs Amadeus Altéa: no evidence either way.** Do not assert it.
- ❌ **EVA SKY SHOP (`evaskyshop.com`) payment methods — 403.** Its 2023 revamp release mentions 「新增多元付款方式」 without enumerating. **This is the single most likely place a Taiwanese 金流 is named.**

### Manual Research Recommendations
> **1. Walk the live checkout from a Taiwanese IP** and watch the 3DS redirect host and the checkout POST target. That is where the acquirer is, and it is the one thing nobody has.
> **2. Confirm the per-departure-market matrix.** EVA states methods vary by origin but never publishes it. Nothing is known for JP, KR, VN, TH, ID, HK/MO or CN.
> **3. Get into EVA SKY SHOP** — most likely place a local gateway is named.
> **4. Verify one route launch** (DFW, IAD or the Delhi evaluation). It is worth +2 and Delhi would change the pitch.
> **5. Read two PTT threads properly** before anyone cites a payment incident.

---

## Executive Summary

EVA Air is Taiwan's second flag carrier, **FY2025 revenue NT$220.3bn**, roughly a quarter of it cargo and therefore outside any card checkout. Its published payment set — verified by me twice from its own pages — is **six card schemes including UATP, plus PayPal, UnionPay, Alipay and Dutch iDeal**, and EVA's own wording confirms that list is the union across every departure market. **Not one Taiwanese local rail appears on it**: no instalments, no 超商代收, no ATM transfer, no LINE Pay, no JKOPay, no Taiwan Pay, no Apple or Google Pay — on a six-figure-NTD long-haul product sold in the market where instalments are the dominant mechanic for high-ticket travel. Alongside that sits a blanket **3DS mandate since March 2021** whose failure mode is a passenger presenting a physical card at an airport counter or being **refused boarding**, and an explicit written refusal to accept **corporate cards** on the web channel — while accepting **UATP** four lines above it and running a corporate travel programme. **No PSP, gateway or acquirer could be identified at all**; EVA's privacy policy names none, and the one architectural signal available is that they built their own in-flight card authorisation over satellite Wi-Fi in 2014 and certified it directly with an acquiring bank. At **15/29** the score is held down by four rows that are unverified rather than absent, and the two hooks are among the best-evidenced in this repo.

</details>
