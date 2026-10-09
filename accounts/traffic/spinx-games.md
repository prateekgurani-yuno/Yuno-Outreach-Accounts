# SpinX Games — SimilarWeb traffic

**Supplied by Prateek:** 2026-10-09 (Google Sheet, *HK October Target Accounts — Similarweb Traffic*) · **Period:** Sep 2026 (1 month) · **Source:** Similarweb PRO, Worldwide, All traffic · **Captured:** 2026-10-09 05:15 IST
**Domains pulled:** 1 · **Top 10 countries per domain only** — this is a top-10 cut, not the full country list, so any APAC total below is a **visible** floor, not a complete one.

## `spinxgames.com`

**Total visits:** 337,627 · **MoM:** ▼ **5.15%** · **Desktop:** 1.04% · **Mobile web:** 98.96%

| # | Country | Traffic share | In APAC territory |
|---|---------|---------------|-------------------|
| 1 | 🇺🇸 United States | 91.33% | — |
| 2 | 🇬🇧 United Kingdom | 2.80% | — |
| 3 | 🇩🇪 Germany | 0.97% | — |
| 4 | 🇦🇷 Argentina | 0.84% | — |
| 5 | 🇫🇷 France | 0.80% | — |
| 6 | 🇰🇿 Kazakhstan | 0.67% | — |
| 7 | 🇪🇸 Spain | 0.37% | — |
| 8 | 🇮🇳 **India** | **0.32%** | ✅ |
| 9 | 🇯🇵 **Japan** | **0.30%** | ✅ |
| 10 | 🇦🇺 **Australia** | **0.24%** | ✅ |

**APAC visible total: 0.86%** across 3 of the top 10 (India, Japan, Australia).

---

## 🛑 CORRECTION — 2026-10-09: THIS MEASURES THE WRONG DOMAIN

**`spinxgames.com` is a corporate brochure site that sells nothing.** Verified first-hand on
2026-10-09: the homepage is an **894-byte** SPA shell, and its router contains only
`/`, `/about`, `/cookie_notice`, `/data_delete`, `/ethics`, `/game`, `/join_social`, `/privacy`,
`/terms`. Keyword counts in that bundle: `shop` 0, `payment` 0, `cart` 0, `checkout` 0, `coins` 0.

**So the 337,627 visits, the 91.33% United States share and the 0.86% APAC total above describe a
site with no storefront.** They do not describe SpinX's payment surface, and they must not be used
to size it or to argue the account has no APAC exposure.

### The revenue-bearing domains, confirmed live and never measured

| Domain | What it is | Verified |
|---|---|---|
| **`jackpot-world.com`** | Jackpot World token store — `/en/shop/token` and `/en/shop/gash` | ✅ HTTP 200, **78,737 bytes** of real storefront |
| **`lotsa-slots.com`** | Lotsa Slots web store — `/web_store`, with a persisted cart | ✅ HTTP 200 |
| **`tpp.spinxbi.com`** | SpinX's own payment gateway. Page metadata, verbatim: *"Spinx Games, Third Party Payment, Online Payment, Jackpot World, Cash Frenzy, Airwallex, Paypal"* | ✅ HTTP 200 |
| `cfweb.spinxgames.com` | Probable Cash Frenzy web store — appears in certificate transparency, but **connection reset, never loaded** | ⚠️ inferred only |

### 🔑 Action for Prateek

**Re-pull SimilarWeb on `jackpot-world.com` and `lotsa-slots.com`.** Those are the domains that
take money. It is the single highest-value missing input on this account: it would convert the
web-vs-IAP revenue argument from inference into evidence, and it would give a real country profile
for the storefronts rather than for a brochure page.

⚠️ **Until then, this account has NO usable traffic data**, and the two ICP rows that depend on a
country profile cannot be verified from this file.

---

⚠️ **Territory note.** APAC here is CLAUDE.md's definition: everything east of Dubai. **Saudi Arabia, the UAE and Turkey are EMEA and are excluded from every total above.** Russia and Kazakhstan are also excluded: neither appears in the territory market list.

*Transcribed verbatim from the supplied sheet. Not re-researched. Figures not independently verified against Similarweb.*
