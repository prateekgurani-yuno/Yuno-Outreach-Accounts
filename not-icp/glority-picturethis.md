# Glority (PictureThis)

**Status:** 🔴 Not ICP — Phase 0 gate: app-store-dominated billing
**ICP Score:** not scored — **rejected at the Phase 0 gate before the research run**
**Industry:** Consumer app — AI plant identification (PictureThis) · **HQ:** **Glority Global Group Limited**, 11/F Capital Centre, 151 Gloucester Rd, Wan Chai, Hong Kong · **Researched:** 2026-10-09 · **First email sent:** —
**Motion:** n/a — there is no payment flow for an orchestrator to sit in front of

---

> ## 🛑 Why this was rejected
>
> **Territory PASSES. Billing FAILS.** The account dies on the app-store trap
> (`.claude/reference/subscription-payments.md` §4): PictureThis Premium is sold through
> Apple and Google in-app purchase, with **Apple named as Seller**, and there is **no web
> checkout at all**. Orchestration cannot touch store-billed revenue — the store owns the
> billing relationship end to end. No routing, no retry logic, no local acquiring.
>
> **This was caught at Phase 0, so no full 5-agent research run was spent on it.**

<details open>
<summary><h2>📊 Section 1 — Quick Look</h2></summary>

**Summary:** Glority publishes **PictureThis**, an AI plant-identification consumer app with a
freemium annual subscription. Monetisation runs through the App Store and Play Store.

**SimilarWeb (supplied 2026-10-09, Sep 2026):** `picturethisai.com` **1.286M visits, ▼22.91% MoM**,
29.34% desktop / 70.66% mobile web. US 12.35%, **Japan 11.72%**, **Korea 5.61%**, Russia 5.34%,
Brazil 4.92%, Italy, Germany, Mexico, Canada, Venezuela. **APAC visible only 17.33%, and no
market above 13%.** Full table in `accounts/traffic/glority-picturethis.md`.

### Legal entities found
| Entity | Country | Source |
|---|---|---|
| **Glority Global Group Limited** | **Hong Kong** — 11/F Capital Centre, 151 Gloucester Rd, Wan Chai · +852 5323 9112 | Play Store developer-contact block |
| Glority Global Group Ltd. | not stated — listed as App Store **developer and Seller** | App Store listing, `<dt>Seller</dt>` |
| Glority Global Group Limited | named as the contracting party in the Terms | `glority.com/terms_en.html` |
| "Glority LLC" / "Glority LLC Limited" | **no domicile stated anywhere** | `glority.com/about.html`, `picturethisai.com/faq` footer |

✅ **Territory verdict: IN TERRITORY.** The only entity with a verified registered address is
Hong Kong. **Nothing west of Dubai was found.** ⚠️ The privacy policy collapses the names:
*"…Global Group Limited (collectively, 'Company,' 'Glority,' 'Glority LLC,' 'we,' 'us,' or 'our')"* —
so "Glority LLC" reads as an alias, not a separate US entity. `[INFERENCE, not confirmed]`

### Known PSPs
- **None.** Apple App Store and Google Play are the billing rails, and **they are not Glority's PSPs** —
  they are storefronts that own the merchant-of-record relationship.

### Orchestration status
**n/a — no addressable payment flow.** Not greenfield, because there is no checkout to orchestrate.

</details>

<details>
<summary><h2>📚 Section 3 — Gate evidence</h2></summary>

## The app-store finding, verified twice

**Agent evidence, then independently re-verified by me on 2026-10-09 against freshly-fetched assets.**

### 1. Their own FAQ says no account is needed to go Premium

From `https://www.picturethisai.com/faq` (HTTP 200, 41,820 bytes, fetched fresh), verbatim:

> *"No user-created account is required even if you upgrade to PictureThis Premium."*

**A web checkout structurally requires an account.** The company states Premium does not need one.

And the only documented recovery path is a store restore:

> *"Make sure you are logged in with the same **Apple ID/Google account** that you used to sign up
> to a subscription… Tap Restore"*

**Zero occurrences of "credit card", "invoice" or "web purchase" anywhere in the FAQ** — confirmed
by my own grep, not just reported.

### 2. Apple is the Seller

The App Store listing names **Glority Global Group Ltd. as Seller** of the IAP subscriptions.
Apple is merchant of record for that revenue.

### 3. No purchase surface exists on the domain

My own probe, 2026-10-09 — every route returned **HTTP 404**:

```
/pricing 404 · /premium 404 · /subscription 404 · /account 404
/web 404 · /checkout 404 · /plans 404 · /upgrade 404
```

### 4. ⭐ The one route that looked like a checkout, and is not

The agent's sweep left a hole and I closed it. The front-end bundle contains a real route string:

```js
function clickAppGuide(e){ … location.href=getJumpLanguageUrlByUrl("pay/subscription") }
```

`/pay/subscription` returns **HTTP 200**, so a lazier check would have called it a web checkout.
It is not. Fetched and parsed:

| Probe | Count |
|---|---|
| `stripe` · `paypal` · `paddle` | **0 · 0 · 0** |
| `card number` · `credit card` · `checkout` | **0 · 0 · 0** |
| `apps.apple.com` | 0 |
| **`play.google.com`** | **5** |

Its visible text: *"Get PictureThis now — Try out PictureThis App on your phone… **Scan QR code to
download**"*, and the only sign-in offered is **"Sign in with Apple"**. **It is an app-download
guide page with a misleading route name**, consistent with the function that calls it being named
`clickAppGuide`. 🚩 **Worth recording as a general trap: a route called `pay/` is not evidence of a
payment page. Fetch it.**

### 5. No PSP anywhere in the front-end

484 KB of freshly-fetched bundles from `picturethisai.com` (`common_load.js`, `jquery.js`,
`react.js`, `tracking.js`, `home.js`), raw `LC_ALL=C grep` counts — **all zero**:

```
stripe 0 · paypal 0 · paddle 0 · fastspring 0 · recurly 0 · braintree 0
adyen 0 · revenuecat 0 · chargebee 0 · lemonsqueezy 0 · 2checkout 0 · xsolla 0
```

⚠️ **These are genuine zeros, not filtered substring noise** — there was nothing to disambiguate.
The only `subscription*` strings in the bundle are CSS class names on the download block
(`subscription-wrap-content-right-downloads-btn`, `…-downloads-qrcode`).

## ⚠️ The one loose end, stated plainly

The product footer's Terms link points at **`https://api-java.picturethisai.com/static/user_agreement_web.html?region=0`** —
a **web-specific** user agreement, distinct from the app's `user_agreement.html`. **It could not be
read.** That host sits behind a Cloudflare interactive challenge: 403 to curl with a full browser
UA, 403 to WebFetch, no Wayback snapshot, and `web.archive.org` is itself blocked from this
environment. The adjacent `privacy_policy.html` on that host would name any payment processor and
is equally unread.

**It most likely just governs use of the website. But it is the single document that could reveal a
web billing relationship, and it is unread.** 🔑 **Reopen this account only if someone reads that
page from an unblocked network and it names a web billing entity or a PSP. Nothing else would
change the answer.**

## What could NOT be verified
- ⚠️ **No corporate registry record was retrieved.** The Hong Kong address comes from Google's
  developer-verification data, not from the HK Companies Registry, which is paywalled.
- ⚠️ **No Shanghai, Hangzhou, Tokyo, Japan or US entity was confirmed by any fetched page.** The
  stub's "usually reported as China/Japan" is **unsupported** by anything sourceable here. A
  targeted search for a Japanese entity returned only unrelated companies.
- ⚠️ The Android package ID is `cn.danatech.xingseus` (`cn.` prefix; 形色/"xingse" is PictureThis's
  Chinese brand). Suggestive of mainland engineering origin, but **a bundle ID is not evidence of
  corporate domicile.** `[INFERENCE, not confirmed]`
- ⚠️ **Where the commercial and engineering team actually sits is not established.** Hong Kong is a
  standard holding-company domicile for mainland-operated app businesses. It does not change the
  gate — HK and mainland are both in territory — but **do not write "Hong Kong-headquartered team"
  into any outreach.**
- ⚠️ **No web-vs-IAP revenue split is published by any source.** The verdict rests on
  one-directional indirect evidence, which is strong but is not a percentage.

## Rejection Rationale

**Rejected at the Phase 0 gate on app-store-dominated billing, not on territory.** Hong Kong HQ
clears the territory test cleanly. The account fails because PictureThis Premium is sold through
Apple and Google IAP with Apple as Seller, the company's own FAQ confirms no user account is needed
to upgrade, all eight candidate purchase routes return 404, the one HTTP 200 `pay/` route is an
app-download page, and 484 KB of front-end bundles contain zero references to any PSP — so there is
no payment flow for an orchestration layer to sit in front of. Secondary support: web traffic is
**▼22.91% MoM** with **APAC visible at only 17.33%** and no market above 13%, so even the web
audience is neither large nor concentrated in territory.

**Not a PSP or payment-infrastructure company — no Partnerships re-route needed.**

</details>
