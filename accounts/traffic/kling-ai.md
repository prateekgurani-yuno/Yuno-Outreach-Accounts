# Kling AI — SimilarWeb traffic

**Supplied by Prateek:** 2026-09-29 · **Period:** Jun 2026 – Aug 2026 · **Scope:** `kling.ai`, **All traffic**
⚠️ **"Include all country domains" toggle is OFF** — this is the `kling.ai` property alone.
**Countries in dataset:** 121 · **Total visits figure:** NOT shown in the supplied view — shares only.

| # | Country | Traffic share | Change | Audience share | Country rank | Visit duration | Pages/visit | Bounce |
|---|---------|---------------|--------|----------------|--------------|----------------|-------------|--------|
| 1 | 🇮🇳 India | **15.21%** | ▼ 0.06% | **20.90%** | #1,699 | 05:09 | **6.79** | 31.99% |
| 2 | 🇺🇸 United States | **11.75%** | ▼ 10.03% | 10.20% | #7,402 | **09:23** | 5.51 | 35.05% |
| 3 | 🇰🇷 Republic of Korea | **5.08%** | ▲ 7.51% | 2.99% | #1,943 | 06:12 | 4.33 | 39.68% |
| 4 | 🇧🇷 Brazil | 4.47% | ▲ **9.41%** | 4.78% | #6,859 | 06:05 | 4.72 | 30.13% |
| 5 | 🇷🇺 Russia | 3.92% | ▼ 8.06% | 3.20% | #3,686 | 05:06 | 3.49 | **45.00%** |
| 6 | 🇮🇩 Indonesia | 3.35% | ▼ **46.45%** | 4.02% | #5,176 | 06:04 | 5.76 | 29.73% |
| 7 | 🇵🇰 Pakistan | 2.77% | ▼ 26.08% | 3.32% | **#1,031** | 05:23 | 4.94 | 31.21% |
| 8 | 🇯🇵 Japan | 2.69% | ▲ 7.72% | 1.83% | #6,551 | 08:04 | 5.36 | 36.86% |
| 9 | 🇩🇪 Germany | 2.50% | ▲ 2.41% | 2.46% | #5,677 | 05:48 | 4.38 | 39.03% |
| 10 | 🇫🇷 France | 2.41% | ▼ 10.19% | 2.16% | #5,052 | 07:35 | 4.46 | 34.17% |
| 11 | 🇬🇧 United Kingdom | 2.39% | ▼ 2.48% | 1.87% | #5,428 ⚠️ | 06:22 | 4.51 | 34.81% |

⚠️ The UK country rank is **partially obscured by a UI element** in the supplied screenshot.
Read as #5,428 but treat as uncertain. Every other cell is legible.

## Arithmetic (computed by me from the rows above — not from SimilarWeb)

- **Visible top 11 = 56.54% of total traffic.** The remaining **43.46% is spread across 110
  countries not shown.** Any claim about the long tail is unsupported by this dataset.
- **APAC (east of Dubai, per `CLAUDE.md`) across the visible rows = 29.10%** —
  India 15.21 + Korea 5.08 + Indonesia 3.35 + Pakistan 2.77 + Japan 2.69.
  This is a **floor, not a total**, because APAC markets certainly appear below rank 11.
- APAC (29.10%) is **2.5× the United States** (11.75%).
- LATAM visible = Brazil 4.47% only.

## Analyst notes

**1. Domain resolution — checked by me, 2026-09-29. The scope is correct.**
Kling runs several hostnames, so a toggle set to OFF would normally invalidate the dataset.
I resolved them directly:

```
https://klingai.com     → 301 → https://kling.ai/        (1 redirect, HTTP 200)
https://www.kling.ai    → 301 → https://kling.ai/        (1 redirect, HTTP 200)
https://app.klingai.com → 301 → https://kling.ai/app/    (2 redirects, HTTP 200)
https://kling.ai        → HTTP 200, no redirect          (canonical)
```

`kling.ai` **is** the canonical international property; the others fold into it. So the
country-domains toggle being OFF does **not** undercount here.
⚠️ **One caveat:** if that consolidation is recent, SimilarWeb may still be attributing some
historical sessions to `klingai.com` separately. Shares would be directionally right, absolute
visits possibly understated. Unresolved — the supplied view shows no visit count to test it against.

**2. China is absent from the top 11 — and that is expected, not an anomaly.**
The Chinese product sits on a **separate Kuaishou-owned hostname** (`klingai.kuaishou.com`),
which is not part of the `kling.ai` property at all. **This dataset describes the
international business only.** Do not read "no China traffic" as "no China business" — it is
a scoping artefact. [INFERENCE from the domain structure, not confirmed against a filing.]

**3. India is the #1 market and the engagement leader.**
15.21% traffic on **20.90% audience share** — the only row where audience share materially
exceeds traffic share. Indian users are the largest user base and visit less often each, but
at the **highest pages/visit in the table (6.79)** and the second-lowest bounce (31.99%).
This is a large, engaged, under-monetised-per-session cohort.

**4. India is flat while the US falls.**
India ▼0.06% is effectively unchanged; the US is ▼10.03%. The mix is shifting toward APAC
without India growing — the US is shrinking under it.

**5. Two APAC markets are in sharp decline.**
Indonesia **▼46.45%** and Pakistan **▼26.08%** are the two steepest falls in the table.
Cause not established — could be competitive, pricing, or a payment/access barrier.
**Do not assert a payment cause without evidence.**

**6. Korea and Japan are both growing** (▲7.51%, ▲7.72%) against a declining US. Korea at
5.08% is the #3 market worldwide and outranks Brazil.

**7. Pakistan's country rank is #1,031 — by far the strongest in the table**, ahead of India's
#1,699. Kling is a top-1,100 site in Pakistan on only 2.77% of its traffic, i.e. it is
disproportionately significant *inside* that market.

## Not established by this dataset

- Absolute visit volumes (shares only — **no transaction-count derivation is possible from this**)
- Paid vs free user split, or any revenue-by-country figure
- Traffic to the Chinese property
- Anything about the 110 countries below rank 11
- Device split, traffic sources, or channel mix
