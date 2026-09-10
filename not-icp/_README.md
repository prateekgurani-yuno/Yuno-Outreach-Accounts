# not-icp

Accounts rejected during `/prepare_batch` because the ICP score fell below 8 on the 24-point
APAC matrix, or rejected manually via `/mark_not_icp`.

Each file carries its rejection rationale. Common APAC rejection reasons:

- **App-store-dominated revenue** — orchestration cannot touch Apple/Google IAP billing
- **Single-market, low-volume** — the matrix can score these deceptively high
- **PSP / payment infrastructure** — out of ICP, routes to Partnerships
- **Out of territory** — HQ west of Dubai with no APAC operations
- **Existing Yuno customer**

To re-evaluate, move the file back to `1-to-outreach/`.
