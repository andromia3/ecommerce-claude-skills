---
name: inventory-risk-brief-ecommerce
description: Turns e-commerce inventory and sales exports into a practical risk brief for stockouts, overstock, promo conflicts, and traffic allocation. Use when the user provides inventory CSVs, stock reports, sell-through data, or asks which products are risky to promote.
---

# Inventory Risk Brief - E-commerce

## Use this skill when

The user wants an inventory-aware growth or promo review from exports.

Common requests:

- "Review this inventory export."
- "Which products are at risk of stockout?"
- "Which products need promo support?"
- "What should we avoid pushing in ads?"

## Required input

Minimum useful input:

- Inventory export with SKU, product name, current stock, and variant.
- Sales export for the last 30, 60, or 90 days.
- Date range and sales velocity.
- Promo calendar or planned campaign notes if available.

Recommended columns:

- SKU
- product name
- variant
- current inventory
- units sold
- revenue
- margin or priority flag if available
- incoming stock quantity and ETA if available
- supplier lead time if available

## Before analysis

1. Confirm the purpose: prevent stockout, reduce overstock, plan promo, or protect paid traffic.
2. Ask for exports if the user only describes inventory from memory.
3. Mark missing lead time, incoming stock, and margin data as caveats.
4. Do not pretend to run demand forecasting.

## Analysis workflow

1. Normalize SKU and product names.
2. Calculate simple signals where data allows:
   - recent sales velocity
   - days of inventory remaining
   - sell-through risk
   - slow mover status
   - promo conflict risk
3. Classify products:
   - stockout risk
   - overstock risk
   - safe to promote
   - do not scale traffic
   - needs more data
4. Tie risks to marketing action.

## Output format

### Inventory verdict

Short owner-level summary.

### Risk table

| Product/SKU | Status | Evidence | Marketing implication | Recommended action |
|---|---|---|---|---|

### Promo notes

Products suitable for promotion, products to protect, and products to avoid scaling.

### Missing data

Fields needed for better confidence.

## Guardrails

- Requires an inventory or sales export. Do not infer stock risk from product names alone.
- Do not replace ERP, inventory planning, or demand forecasting systems.
- Do not recommend purchase orders without lead time, margin, and business approval.
- Do not recommend pushing products that may stock out during the campaign.
- Do not ignore variant-level constraints.
