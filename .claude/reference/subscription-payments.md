# Subscription & Recurring Payments Reference

Loaded by `/full-outreach` when the prospect runs a subscription, membership, SaaS or any
recurring-revenue model. Missing from the original EMEA pack; written here for APAC.

> Same rule as the APAC reference: this is a checklist of what to look for and how to
> frame it. No number in here is a citable fact. Any benchmark used in an email must come
> from research with a live source.

---

## 1. The core mechanic: involuntary churn

Voluntary churn is a product problem. **Involuntary churn is a payments problem** — the
customer still wants the service, the renewal simply failed. The usual causes:

| Cause | What fixes it |
|---|---|
| Card expired or reissued | Network tokens / account updater — credentials refresh without customer action |
| Soft decline (insufficient funds, issuer velocity) | Intelligent retry — timing and sequencing matter more than retry count |
| Issuer treats the recurring MIT as suspicious | Correct MIT flagging, stored-credential framework, local acquiring |
| Cross-border decline on the renewal | Route the renewal to a local acquirer in the cardholder's geography |
| Regulatory auth requirement on the debit | Market-specific mandate handling (see §3) |

**Where the money is:** first-renewal drop-off is usually the sharpest cliff in the funnel,
and it is disproportionately involuntary. Ask about it on the call rather than asserting a
number in an email.

## 2. What Yuno actually contributes

Framed as mechanism, not claims — E2 rules apply, no percentages without a source.

- **Network tokens and account updater** inside the routing layer, so credential refresh is
  not a per-PSP project.
- **Retry logic informed by decline code and issuer**, rather than a fixed schedule.
- **Routing the renewal** to whichever acquirer performs best for that BIN and geography —
  which for a global subscriber base means local acquiring in the subscriber's market.
- **One integration for local recurring rails**, which in APAC are not cards (see §3).
- **Unified view of failed renewals** across providers, instead of per-PSP dashboards.

## 3. APAC-specific recurring constraints

This is where a global-only subscription stack quietly breaks. Verify current rules per
account — these regimes change.

- **India.** Recurring card debits fall under the RBI e-mandate framework: registration of
  the mandate, additional factor authentication, pre-debit notification to the customer, and
  a ceiling above which AFA is required on every debit. Card-on-file tokenization
  requirements apply separately. Naive "store the card, retry monthly" logic that works in
  the US does not work here. UPI Autopay is the local recurring rail and is frequently
  absent from global stacks. **This is the single strongest recurring-payments hook in the
  territory.**
- **Japan.** Card instalment and bonus-payment conventions, konbini for non-card payers,
  carrier billing for smaller-ticket subscriptions, plus EC 3DS requirements to verify.
- **Indonesia / Vietnam / Philippines.** Wallet and account-to-account rails dominate;
  card-based recurring covers a minority of the addressable base. Recurring on wallets is a
  different integration, not a toggle.
- **Australia / New Zealand.** PayTo is the account-to-account mandate rail; direct debit
  conventions differ from SEPA. Verify current PayTo merchant adoption before citing it.
- **South Korea / China.** Local acquiring and licensed local rails gate recurring entirely;
  entity questions come before optimisation questions.

## 4. The app-store trap — check this before pitching

If a consumer subscription business bills primarily through Apple App Store or Google Play
in-app purchase, **orchestration cannot touch that revenue.** No routing, no retry logic, no
local acquiring — the store owns the billing relationship end to end.

Before building a sequence for any consumer subscription app:
1. Find the actual billing split — web checkout vs IAP. Terms of service, help centre and
   the signup flow itself usually reveal it.
2. If IAP dominates, say so in the report and score the account down regardless of what the
   matrix computes. This is the documented `not-icp` failure mode from the EMEA pack: an
   account scored ⭐ on paper and was rejected on exactly this ground.
3. Web-first or web-significant billing is the qualifier. Growing web-checkout share (to
   escape store fees) is itself a strong buying trigger — those merchants are building web
   billing infrastructure right now.

## 5. Discovery questions worth earning

Do not assert these in email. They are what the meeting is for.
- What share of renewals fail on first attempt, and what share of those recover?
- Is the first-renewal cliff visible in the cohort data?
- Are network tokens live, and across which providers?
- How is India recurring handled today — cards under e-mandate, UPI Autopay, or not served?
- What share of billing runs through app stores versus web?
