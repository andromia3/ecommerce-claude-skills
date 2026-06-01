---
name: returns-reason-miner-ecommerce
description: Mines e-commerce returns exports, refund reasons, support notes, and product page data to find preventable return patterns and fixes for product pages, sizing, expectations, fulfillment, packaging, and quality.
---

# Returns Reason Miner - E-commerce

## Use this skill when

The user wants to understand why products are returned and what can be fixed.

Common requests:

- "Analyze our return reasons."
- "Which products create preventable returns?"
- "What should we change on the product page?"
- "Find return patterns by SKU."

## Required input

Minimum useful input:

- Returns export with SKU/product, date, quantity, and reason.
- Sales volume by SKU for the same period if available.
- Product page URLs or screenshots for affected products.

Optional:

- Refund cost.
- Margin impact.
- Support notes.
- Photos or QC notes.
- Size guide or product specs.

## Before analysis

1. Confirm the return window and policy.
2. Ask whether reasons are customer-selected, agent-selected, or free text.
3. Normalize reason labels before drawing conclusions.
4. Separate preventable returns from normal category behavior.

## Analysis workflow

1. Group returns by SKU, category, variant, reason, and time period.
2. Calculate return concentration where sales volume exists.
3. Classify themes:
   - sizing/fit
   - product expectation mismatch
   - quality issue
   - shipping damage
   - wrong item
   - late delivery
   - buyer remorse
   - unclear compatibility
4. Map each theme to possible fixes:
   - PDP copy
   - images/video
   - sizing guide
   - FAQ
   - packaging/fulfillment
   - product/QC
5. Prioritize preventable high-impact patterns.

## Output format

### Returns verdict

Top return drivers and whether they look preventable.

### Return pattern table

| Product/SKU | Return theme | Evidence | Likely root cause | Recommended fix |
|---|---|---|---|---|

### Preventable return fixes

Action list grouped by PDP, policy, fulfillment, and product.

### Missing data

Data needed before changing policy or operations.

## Guardrails

- Do not recommend stricter return policy as the default fix.
- Do not blame customers without evidence.
- Do not call product quality issues without enough signal.
- Do not use return rate without sales volume when ranking severity.
- Do not publish customer quotes without permission.
