# Scripts

Three skills in this pack are arithmetic-heavy. A model doing that arithmetic by
eye produces numbers that look right and are not, and an owner will act on them.
These scripts do the counting exactly and leave the judgement to the skill.

| Script | Used by | What it removes from the model's hands |
|---|---|---|
| `margin_stack.py` | Contribution Margin Check | The seven-line cost stack per SKU, CM2, CM3, breakeven ROAS |
| `cohort_read.py` | LTV and Cohort Read | Cohort grouping, cumulative value per horizon, and the maturity guard |
| `catalog_scan.py` | Catalog Content Audit | Whole-catalog counting, duplicate detection, attribute gaps |
| `promo_impact.py` | Promo and Discount Impact Review | Baseline, promo and recovery windows on the same footing |
| `shipping_recovery.py` | Shipping Economics Review | Recovery rate by zone and order value band, threshold test |
| `subscription_survival.py` | Subscription Churn Review | Survival by cycle with the voluntary / involuntary split |
| `dispute_rate.py` | Chargeback and Fraud Pattern Review | Dating disputes to the right period, reason families, rate per month |

No dependencies beyond the Python 3 standard library. Nothing writes to your
files, calls a network, or needs a store login.

## Usage

```bash
python3 scripts/margin_stack.py products.csv --payment-fee-pct 2.9 --payment-fee-fixed 0.30
python3 scripts/cohort_read.py orders.csv --by source
python3 scripts/catalog_scan.py catalog.csv --thin-words 40
python3 scripts/promo_impact.py daily.csv --promo-start 2026-11-27 --promo-end 2026-12-01
python3 scripts/shipping_recovery.py orders.csv --threshold 50
python3 scripts/subscription_survival.py subscribers.csv
python3 scripts/dispute_rate.py disputes.csv --orders-per-month "2026-01=1200"
```

Add `--json` to any of them for the full machine-readable output, which is what
you want when the skill needs every row rather than the printed top slice.

Each script accepts the common export spellings for its columns
(`Net sales` / `revenue` / `total`, `Cost per item` / `unit cost`, `Body (HTML)`
/ `description`, and so on), matched case-insensitively. If a required column is
genuinely absent the script exits 2 and prints the columns it did find, rather
than guessing which one you meant.

Every skill in this pack that does arithmetic on more than a handful of rows has
one. The two that do not, AI Shopping Readiness and Onsite Search and
Merchandising Review, are reading a page and sorting a query list: there is no
multi-step calculation for a script to protect.

## Testing the scripts

```bash
python3 scripts/selftest.py
```

Seventeen regression checks, one per bug that actually shipped and was caught by
someone running a script against a fixture rather than reading it. Negative
discounts adding back to revenue, a whole channel blanked by one new customer,
Shopify variant rows counted as separate products, a margin percentage derived
without a cost column, a trialing subscriber counted as a cancellation. Run it
before and after changing anything here. The pack's central claim is that these
scripts do not produce confidently wrong numbers, and that claim is worth exactly
what this file checks.

## The guarantees worth knowing

**Absent cost lines are reported, never invented.** `margin_stack.py` prints
which cost columns were missing from the export and flags every affected SKU.
A margin figure built on an absent column is an assumption, and the skill has
to label it as one.

**An immature cohort prints a dash, not a zero.** `cohort_read.py` measures each
cohort against the newest order in the file and refuses to report a horizon the
cohort has not lived through. A 365-day number from cohorts that are 200 days
old is the single most common way LTV analysis lies.

**Catalog counting is exhaustive or it says so.** `catalog_scan.py` reads every
row, and collapses Shopify's one-row-per-variant exports to one record per
product first. Above roughly 150 SKUs the Catalog Content Audit skill is required
to use it, because a model reading a large export summarises the rows it happened
to attend to and reports that as coverage.

**A promo is never judged on its own window.** `promo_impact.py` always reports
the recovery period alongside the promo, and says so out loud when ad spend rose
at the same time. Both omissions are how a pull-forward gets sold as growth.

**Churn is never one number.** `subscription_survival.py` splits endings into
voluntary, involuntary and paused-not-resumed, counts each cycle only against the
subscribers who reached it, and prints how many rows it had to infer a churn type
for.

**Money leaving the business subtracts, whatever sign the export used.**
`margin_stack.py` takes the magnitude of discounts and returns and says when it
had to, because a negative discount added back to revenue inflates every margin
below it silently.

## Exit codes

`0` ran, `2` could not run (file unreadable, required columns absent, or a
segment requested that is not in the export).
