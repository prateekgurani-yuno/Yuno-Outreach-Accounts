# Asiana Airlines

**Status:** 🔴 Not ICP
**ICP Score:** Not scored — rejected at the Phase 0 gate before research was run
**Industry:** Airlines · **HQ:** Seoul, South Korea · **Researched:** 2026-09-15 · **First email sent:** —
**Motion:** N/A

---

## Rejection Rationale

**Asiana Airlines ceases to exist as a legal entity on 17 December 2026, thirteen weeks from this report. Korean Air absorbs everything. There is no Asiana payment decision left to sell into.**

I verified this myself at a trade source rather than taking it from a summary. [ch-aviation](https://www.ch-aviation.com/news/167243-korean-air-to-merge-with-asiana-airlines-in-late-4q26), verbatim:

> *"Korean Air (KE, Seoul Incheon) and Asiana Airlines (OZ, Seoul Incheon) will integrate on **December 17, 2026**, after the respective boards approved the merger agreement on May 13. The two carriers signed a contract to execute the merger the day after."*

> *"**Korean Air will absorb all assets, liabilities, and employees of Asiana Airlines.**"*

Further detail from the same source: the merger ratio is one Korean Air share per 0.2736432 Asiana shares; Korean Air applied to South Korea's Ministry of Land, Infrastructure and Transport on 14 May; it planned to apply in June 2026 to amend its Operations Specifications so Asiana's aircraft and safety systems come under Korean Air's existing air operator's certificate; and Asiana held an extraordinary shareholders' meeting in August 2026 to vote on it. The two are consulting the Korea Fair Trade Commission on merging the frequent-flyer programmes.

Corroborating on the consumer-facing side: from 17 December all former Asiana flights operate under **Korean Air flight numbers and branding**, **Asiana Club folds into Korean Air's SKYPASS**, and the combined carrier is SkyTeam-only. `[UNVERIFIED — trade and enthusiast press summaries, not read at source: [Head for Points](https://www.headforpoints.com/2026/05/19/korean-asiana-merger/), [One Mile at a Time](https://onemileatatime.com/news/asiana-brand-disappear-merged-into-korean-air/)]`

### Why this is a Phase 0 rejection and not a low score

The auto-reject table in `/research` does not have a row for "target is being absorbed", so this is an analyst judgement, stated plainly:

- **The buying entity disappears.** Korean Air absorbs all assets and liabilities. Any contract signed with Asiana in Q4 2026 novates to Korean Air by default, so the real counterparty was always Korean Air.
- **The selling channel has a fixed end date.** `flyasiana.com` as a distinct storefront has roughly thirteen weeks of life. Nobody re-platforms payments on a website scheduled for retirement.
- **The decision-makers are already gone.** Commercial, digital and finance leadership for the combined carrier sits at Korean Air. An Asiana-addressed sequence reaches people who cannot buy.
- **Researching it would have produced a confidently wrong report.** A full run would have scored Asiana on traffic, entities and rails as though it were an ongoing concern. That is precisely the false positive the analyst override exists to catch.

`flyasiana.com` also returns **HTTP 403 to automated fetches** (confirmed twice, with two different browser user-agent strings), so a checkout audit was not available either way.

---

## Where the opportunity actually is: Korean Air

**The merger is not a reason to walk away from the account. It is the single strongest buying signal on the Korean market, and it belongs to Korean Air.**

Korean Air is already a separate **P1** row on the TAL (`koreanair.com`, HQ South Korea, est. revenue **$11.3B** — the largest airline figure on the list, roughly double Asiana's $5.8B).

What the integration creates, structurally:

- **Two payment stacks becoming one**, across two booking engines, two PSS instances and two sets of acquirer relationships spanning dozens of selling markets. That is the exact event that creates orchestration demand, and it is happening on a published date.
- **Two loyalty programmes merging** (Asiana Club into SKYPASS), which means mixed-tender and stored-instrument migration on top of the ticketing flows.
- **A hard cutover deadline of 17 December 2026**, which concentrates the work rather than letting it drift.
- **Korea gates domestic acquiring behind local presence and local PG intermediation** (see `.claude/reference/apac-payments.md` §2), so the consolidated carrier still needs a domestic Korean path alongside its international one.

**Recommended action:** run `/research Korean Air` and open on the integration. The angle is consolidation and cutover risk, not "you need orchestration" — a carrier of that size will have views already. Timing matters: the useful window is either now, while integration planning is live, or Q1–Q2 2027, once the cutover has exposed what did not consolidate cleanly.

⚠️ **Check before drafting:** Korean Air's own payment stack is **not researched** in this repo. Adyen's public boilerplate names Cathay Pacific and Singapore Airlines as customers but does **not** name Korean Air. Nothing on file connects Korean Air to any orchestrator. Establish the motion before writing a line of outreach.

---

## What was not researched

No traffic pull, no PSP identification, no rail analysis and no checkout audit were performed for Asiana. The Phase 0 gate fired first, and by design that stops the run rather than burning five agents on an entity with a December expiry date. Nothing in this file should be read as a payment-stack finding about Asiana, because none was made.

*Marked: 2026-09-15*
