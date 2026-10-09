# SpinX Games

**Website:** spinxgames.com · **Industry:** Gaming — social casino · **HQ:** Hong Kong
**Priority:** P1 · **Added:** 2026-10-09 · **Phase 0 gate:** ✅ cleared 2026-10-09 (web-material)

## Notes

- TAL on file: owned by **Netmarble** (Korea), titles **Cash Frenzy** and **Lotsa Slots**, est. revenue **~$1B**, operating HK + Global. TAL note says monetised *"mainly in America"* — **VERIFY, because it decides the account.**
- ✅ **GATE CLEARED 2026-10-09 — risk ② is DISPROVEN and must not be repeated.** SpinX is **WEB-MATERIAL**, not IAP-dominated. They run their own payment gateway at `tpp.spinxbi.com` across three channels per title (WEB / EXE / in-app alternative billing), with **Airwallex** as primary card processor (consumer-facing disclosure verbatim in their bundle), plus **GASH and MyCard** for Taiwan, **Appcharge**, **Xsolla** (Russia fallback) and **PayPal**. Routing config and per-channel `is_close` kill-switches verified first-hand. **Adyen, Stripe, Checkout.com, Nuvei, 2C2P, Coda, Razer, dLocal and PayerMax all score zero.**
- 🛑 **Risk ① was reasoning from the WRONG DOMAIN.** `spinxgames.com` is an 894-byte brochure shell that sells nothing. The 91.33% US / 0.86% APAC figures describe it, not the storefronts (`jackpot-world.com`, `lotsa-slots.com`). **Re-pull SimilarWeb on those two domains** — see `accounts/traffic/spinx-games.md`. Taiwan is in fact a live surface: GASH points are bought as cash at 7-Eleven, FamilyMart, Circle K and Hi-Life, and Japan has a 特定商取引法 filing, which is only required of a merchant selling direct to Japanese consumers.
- ⚠️ **The ~$1B revenue figure is UNSUPPORTED.** Verified anchors: $432M (2020, pre-acquisition) and three SpinX titles at 7% each ≈ 21% of Netmarble group revenue (Q2 2026 deck). Netmarble ownership confirmed first-party: 100% for ₩2.5tn ($2.19bn), HQ Sheung Wan.
- ⚠️ **$3.5M US class action verified** — *Heathcote v. SpinX Games Limited et al.*, W.D. Wash. 2:20-cv-01310-RSM, over virtual-coin sales under Washington gambling law. Defendants deny all claims. Not a gate failure, but it explains the geo-gating and the kill switches. **Handle factually; never imply wrongdoing.**
- **The local-method gap is the pitch:** no UPI, QRIS, PayNow, PromptPay, GCash, konbini, Alipay or WeChat Pay anywhere in the stack.
- **Social casino also carries acquirer-appetite and MCC questions.** Check the high-risk-vertical framing in the research skill before assuming a standard routing pitch.
- Traffic: 337,627 visits Sep 2026, ▼5.15% MoM.

> Everything above comes from the target account list and Prateek's supplied traffic
> sheet, and is an unverified starting hypothesis. `/research` must confirm each item
> with a source or drop it.

**Traffic data:** ✅ supplied — see `accounts/traffic/spinx-games.md`
