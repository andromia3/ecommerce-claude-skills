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
