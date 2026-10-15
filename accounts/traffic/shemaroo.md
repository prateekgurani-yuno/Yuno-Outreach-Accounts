# ShemarooMe (Shemaroo Entertainment) — SimilarWeb traffic

**Supplied by Prateek:** 2026-10-15 (screenshot, Website analysis → Geography) · **Period:** Jul 2026 – Sep 2026 · **Scope:** `shemaroome.com`
✅ **"Include all country domains" toggle is ON.** · **Countries in dataset:** 68 · **Total visits & global rank: not shown** — shares only.

| # | Country | Traffic share | Change | Engagement | Territory |
|---|---------|---------------|--------|------------|-----------|
| 1 | 🇮🇳 **India** | **67.27%** | ▼ 9.80% | — | ✅ APAC (home) |
| 2 | 🇵🇰 **Pakistan** | **8.05%** | ▲ **23.96%** | — | ✅ APAC |
| 3 | 🇺🇸 United States | 3.32% | ▲ 19.37% | — | AMER |
| 4 | 🇧🇩 **Bangladesh** | 2.06% | ▼ 22.07% | — | ✅ APAC |
| 5 | 🇦🇺 **Australia** | 2.02% | ▼ **52.15%** | — | ✅ APAC |
| 6 | 🇬🇧 United Kingdom | 1.90% | — | — | EMEA |
| 7 | 🇨🇦 Canada | 1.52% | — | — | AMER |
| 8 | 🇸🇦 **Saudi Arabia** | 1.52% | ▲ **379.00%** | **00:06:14 · 7.08 pages · 22.99% bounce** | EMEA |
| 9 | 🇦🇪 United Arab Emirates | 1.29% | — | — | EMEA |
| 10 | 🇩🇪 Germany | 0.90% | — | — | EMEA |
| 11 | 🇿🇦 South Africa | 0.66% | — | — | EMEA |
| 12 | 🇱🇰 **Sri Lanka** | 0.61% | — | — | ✅ APAC |
| 13 | 🇫🇷 France | 0.48% | — | — | EMEA |
| 14 | 🇳🇱 Netherlands | 0.44% | — | — | EMEA |
| 15 | 🇸🇬 **Singapore** | 0.42% | — | — | ✅ APAC |
| 16 | 🇳🇵 **Nepal** | 0.41% | — | — | ✅ APAC |

*Rows 17–68 not captured in the supplied view. Per-country visit duration, pages/visit and bounce
were only legible for Saudi Arabia in the supplied screenshot — the remaining engagement cells are
gaps, not zeroes.*

## Read

### The home market is 67.27%, so the "traffic outside home market" ICP row scores 0

The matrix awards +2 only where the home country sits **under 60%**. India is **67.27%**, which
misses by 7.3 points. **This row scores 0 and must not be argued up.** It is the single clearest
reason this account does not reach ⭐ on geography alone.

Note the direction of travel, though: India is **down 9.80%** while Pakistan is **up 23.96%** and
the US **up 19.37%**. The home share is shrinking. This row may well fire on the next pull — but we
score what is in front of us.

### Pakistan is the #2 market and the most important number in this file

**8.05% and growing 24%** — larger than the US, and larger than UK + Canada combined. For a Hindi,
devotional and regional-content service this is unsurprising demand, and it is the one market a
global payment stack never serves by default.

⚠️ **This share is the reason the routing audit in the research file matters.** Cross-referenced
against ShemarooMe's own served checkout code: **Pakistan has localised plans priced in PKR that are
rendered `disabled` on web.** Traffic is arriving and growing, and the web checkout will not take
the money.

### Saudi Arabia is the standout engagement row in the entire dataset

1.52% share is small. **▲379.00%, 00:06:14 average session, 7.08 pages per visit and a 22.99%
bounce rate is not small** — it is the deepest engagement of any country in the supplied view, by a
wide margin. Six minutes and seven pages is browsing behaviour, not a bounce-through.

Same cross-reference, same answer: **SAR 120/year and SAR 39/quarter are priced and `disabled`.**

⚠️ **Territory note.** CLAUDE.md places **Saudi Arabia and the UAE in EMEA**, out of APAC territory.
They are recorded here because they are part of the traffic picture and part of the payment-routing
finding — **not** as APAC-attributable demand. Shemaroo is **India-HQ'd**, so the account itself is
squarely in territory; the Gulf rows are just markets it sells into.

### The diaspora bloc is real but splits across two different payment fates

Visible non-India traffic totals **~32.7%**, and it does not behave as one group:

| Bloc | Markets | Share | What the checkout does |
|---|---|---|---|
| **Served (Stripe)** | US, Australia, UK, Canada, Germany, France, Netherlands, Singapore | **~10.6%** | Enabled, local-currency checkout |
| **Priced but switched off** | Pakistan, Bangladesh, Saudi, UAE, Sri Lanka | **~13.5%** | Plans render `disabled`; user is told to subscribe in the app |
| Not separately assessed | South Africa, Nepal, remaining 52 countries | ~8.6% | Unknown — not probed |

**The switched-off bloc (~13.5%) is larger than the served bloc (~10.6%).** That is the finding this
traffic file exists to support, and it is sourced to Shemaroo's own code rather than to inference.

### Australia is down 52.15% and nobody should build an argument on it without asking why

The sharpest decline in the dataset, in a market that **does** have an enabled Stripe checkout
(AUD 19/quarter, AUD 49/year). A halving in a served market is the opposite pattern to Pakistan and
Saudi. **Cause unknown — not investigated.** Content licensing, a competitor, or seasonality are all
plausible and none is verified. Flagged so it is not mistaken for a payment problem.

## Gaps in this record

- **Total monthly visits and global rank** — not shown in the supplied view. Without visits, no
  share can be converted into an absolute number, so nothing here feeds the volume gate.
- **Engagement metrics for 67 of 68 countries** — only Saudi Arabia was legible.
- **Rows 17–68** — the long tail is uncaptured.
- **Device split (mobile vs desktop)** — not supplied. Material for an app-first OTT, since it bears
  directly on how much subscription revenue routes through app-store billing.
- **Traffic sources** — not supplied.
