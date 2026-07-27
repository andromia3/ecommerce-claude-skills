# Demo outputs

These are synthetic examples that show output shape. They are not case studies, testimonials, or promised results.

## Mini demo: Paid Traffic Waste Triage

### Inputs

- Meta Ads export summary
- Product margin CSV
- Product page URL
- Inventory notes

### Expected output shape

#### Triage verdict

The likely leak is not only paid media. The ad export shows high spend on two products with acceptable ROAS, but the margin file suggests one product may be unprofitable after refunds and fulfillment. Treat this as a margin and product mix issue before scaling.

#### Waste table

| Segment | Evidence | Likely layer | Severity | Confidence | Business impact | Effort | Owner decision |
|---|---|---|---|---|---|---|---|
| Campaign promotes low-margin SKU A | `export`, `margin_csv` | margin/product mix | high | medium | margin | S | investigate |
| Landing page B has high clicks and low purchase rate | `export`, `url` | product page | medium | medium | conversion | M | test |
| Catalog item C has availability mismatch | `feed_diagnostics`, `needs_data` | feed/inventory | high | low | revenue/risk | S | investigate |

#### Action queue

1. Verify contribution margin and refund rate for SKU A before increasing budget.
2. Run Product Page Conversion Review on landing page B.
3. Check Merchant Center or catalog diagnostics for item C.

#### What not to do yet

- Do not scale the campaign based only on ROAS.
- Do not pause the full campaign without product-level margin and inventory confirmation.

## Mini demo: Checkout Friction Finder

### Inputs

- Cart screenshot
- Checkout screenshots
- Shipping policy
- Checkout funnel metrics

### Expected output shape

#### Checkout verdict

The largest likely friction is late disclosure of shipping cost and delivery timing. This is supported by checkout screenshots and support questions. Conversion impact is plausible but must be measured after changes.

#### Ranked friction table

| Rank | Friction point | Evidence | Severity | Confidence | Business impact | Effort | Owner decision |
|---|---|---|---|---|---|---|---|
| 1 | Shipping cost appears after email step | `screenshot`, `policy` | high | high | conversion/support_load | S | do_now |
| 2 | Delivery window unclear until final step | `screenshot`, `support_ticket` | medium | medium | conversion | S | test |
| 3 | Discount box dominates mobile checkout | `screenshot`, `hypothesis` | low | low | conversion | XS | monitor |

#### Measurement plan

- Checkout completion rate.
- Shipping-related support tickets.
- Cart to checkout step completion.
- Purchase conversion by mobile vs desktop.

## Mini demo: Review and Objection Miner

### Inputs

- 200 owned reviews
- Product page URL
- Support objections

### Expected output shape

#### Review verdict

Customers repeatedly praise ease of use and fast setup, but negative reviews cluster around sizing uncertainty and unclear compatibility. The page should answer these before the CTA.

#### Theme table

| Theme | Evidence | Customer language | Business implication | Recommended use |
|---|---|---|---|---|
| Easy first use | `review_cluster` | "took five minutes" | proof | PDP proof block |
| Compatibility confusion | `review_cluster`, `support_ticket` | "wasn't sure if it fits" | conversion/support_load | FAQ + compatibility table |
| Sizing uncertainty | `review_cluster`, `return_reason` | "runs smaller than expected" | returns | sizing guide update |

#### Guardrail

Use customer language for insight. Do not publish quotes unless review display rights and attribution rules are clear.

---

# Demos for skills 11-20

The three script-backed demos below are **real runs** against the synthetic
fixtures in this repo's test data, not hand-written numbers. The commands are the
ones you would run. The commentary underneath each is the part the skill adds.

## Mini demo: Contribution Margin Check

### Input

A four-SKU sales export with units, net sales, discounts, returns, cost per item,
shipping cost, shipping charged and attributed ad spend. No packaging column.

```bash
python3 scripts/margin_stack.py products.csv --payment-fee-pct 2.9 --payment-fee-fixed 0.30
```

### Actual script output

```text
SKUs: 4   CM2 total: 5182.82   CM3 total: 262.82
MISSING COST COLUMNS (excluded from the stack, findings are assumptions): packaging_cost
negative before ad spend: 0   negative only after ad spend: 1

sku                       units  net_revenue        cm2    cm2_%    breakeven  missing
HAT-004                      60      1830.00     608.93     33.3         3.01  packaging
BAG-003                      95      4630.00     802.23     17.3         5.77  packaging
MUG-002                     180      3060.00    1181.26     38.6         2.59  packaging
TEE-001                     420      8400.00    2590.40     30.8         3.24  packaging
```

### What the skill does with it

The whole store cleared 5182.82 before ad spend and 262.82 after it. That gap is
the finding, not the products.

BAG-003 is the one to look at. It carries the second-highest net revenue and the
worst margin percentage in the catalog, and its breakeven ROAS is 5.77 while
every other SKU sits between 2.59 and 3.24. If the media buyer is holding one
blended ROAS target across the account, this product is being scaled at a loss
and the account average is hiding it.

#### Decision summary

| Finding | Evidence | Severity | Confidence | Business impact | Effort | Owner decision |
|---|---|---|---|---|---|---|
| BAG-003 needs ROAS 5.77 to break even against an account target near 3 | `export`, `cogs_export` | high | high | margin | XS | do_now |
| One SKU is profitable before ad spend and unprofitable after it | `export` | high | high | margin | S | investigate |
| Packaging cost is absent from the export, so every margin here is slightly optimistic | `needs_data` | medium | high | margin | XS | investigate |

#### What not to do yet

Do not cut BAG-003. Its breakeven is a pricing and shipping question first, and
the packaging line is still missing from every row.

## Mini demo: LTV and Cohort Read

### Input

24 months of orders with customer id, date, value and acquisition source.

```bash
python3 scripts/cohort_read.py orders.csv --by source
```

### Actual script output

```text
orders parsed: 140   customers: 60   skipped rows: 0   as of: 2025-02-13
median days to second order: 48   repeat customers: 60

source          customers   repeat_%        d30        d90       d180       d365
google                 19      100.0     117.33     194.83          -          -
meta                   17      100.0     130.31     239.08     239.08          -
organic                24      100.0     129.63     204.86     204.86          -

A dash means the group has not had that many days yet, measured against 2025-02-13.
It is not a zero. Do not report a horizon a cohort has not reached.
```

### What the skill does with it

The median second order lands at day 48, which is the number the retention flows
should be built around. Anything firing at day 7 is talking to people who have
not finished the first product yet.

The source comparison looks like meta wins at day 90, and it is not reportable.
Seventeen customers is too small a cohort to separate 239.08 from 204.86, and
google has not even reached day 180. The honest output names the gap and asks for
more history rather than moving budget on it.

#### Decision summary

| Finding | Evidence | Severity | Confidence | Business impact | Effort | Owner decision |
|---|---|---|---|---|---|---|
| Median second order at day 48; no lifecycle flow currently targets that window | `cohort_export` | high | high | retention | S | do_now |
| Meta appears strongest at day 90 on 17 customers, which is not a decidable difference | `cohort_export`, `hypothesis` | low | low | retention | M | monitor |
| No cohort has reached 365 days, so no annual LTV figure exists yet | `needs_data` | medium | high | retention | S | investigate |

#### What not to do yet

Do not set CAC targets from a 365-day LTV. The column is empty for a reason.

## Mini demo: Catalog Content Audit

### Input

A 220-SKU catalog export with descriptions, category, image counts, revenue,
GTIN and brand.

```bash
python3 scripts/catalog_scan.py catalog.csv
```

### Actual script output

```text
products: 220   thin: 130   empty: 17   duplicate copy: 36 products in 1 clusters
attributes checked: brand, gtin
attribute gaps: gtin=55, brand=25

category                      products    thin   empty   dupes    img_gap      revenue
Tees                                74      56       7       0         30    143838.76
Outerwear                           73      51       7       0         33    141687.18
Accessories                         73      23       3      36         28    139725.34
```

### What the skill does with it

Thirty-six products share one description word for word, and all of them sit in
Accessories. One cluster, one category, one cause: supplier copy pasted in
unedited, which every other reseller of those products also has.

The GTIN gap is the blocker, not the copy. Fifty-five products without an
identifier will fail a marketplace push regardless of how good their descriptions
become, so that queue runs first even though it is duller work.

#### Decision summary

| Finding | Evidence | Severity | Confidence | Business impact | Effort | Owner decision |
|---|---|---|---|---|---|---|
| 55 products have no GTIN, which blocks the planned marketplace push | `export`, `feed_diagnostics` | critical | high | revenue | M | do_now |
| 36 Accessories products share identical supplier copy | `export` | high | high | conversion/risk | M | do_now |
| 130 thin descriptions spread evenly across categories, so this is a process gap not a category gap | `export` | medium | high | conversion | L | test |

#### What not to do yet

Do not start rewriting 130 descriptions. Close the identifier gap, then fix the
one duplicate cluster, then measure whether description length moves anything.

## Output shapes for the rest

The remaining skills follow the same contract: a verdict with confidence, a
ranked table with an evidence tag per row, a decision summary, an explicit
"what not to do yet", and a missing-data list. What differs is the middle table.

| Skill | The table that carries the finding | The line owners most often skip |
|---|---|---|
| Promo and Discount Impact Review | Promo window versus baseline, then the trough after | Whether ad spend also rose during the promo |
| Shipping Economics Review | Recovery rate by zone and order value band | Which threshold change risks conversion |
| Subscription Churn Review | Survival by cycle, split voluntary / involuntary / paused | The share that is simply failed cards |
| AI Shopping Readiness | Element by element legibility, with the date checked | What the platform already supports natively |
| Chargeback and Fraud Pattern Review | Reason family versus likely real cause | The cost of the good orders current rules reject |
| Onsite Search and Merchandising Review | Query, volume, failure type | Whether the product already exists under another name |
| Launch Readiness Check | Eight-layer readiness board with owners | The oversell scenario |
