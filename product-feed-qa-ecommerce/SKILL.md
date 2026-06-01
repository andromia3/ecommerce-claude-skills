---
name: product-feed-qa-ecommerce
description: Audits e-commerce product feed exports, Google Merchant Center diagnostics, catalog screenshots, and product page samples to find data quality issues that can hurt Shopping ads, catalog ads, product discovery, or approvals.
---

# Product Feed QA - E-commerce

## Use this skill when

The user wants to check product feed or catalog quality before or after distribution issues.

Common requests:

- "Audit this product feed."
- "Why are products disapproved?"
- "Check feed issues before we scale Shopping."
- "Review product titles, prices, availability, and images."

## Required input

Minimum useful input:

- Product feed CSV sample or full export.
- Merchant Center diagnostics export or screenshots if available.
- Product page URLs for affected items.
- Product category and market.

Recommended columns:

- item ID / SKU
- title
- description
- price
- sale price
- availability
- image link
- product link
- brand
- GTIN / MPN where relevant
- product category
- condition

## Before analysis

1. Confirm target channel: Google Shopping, Meta catalog, TikTok catalog, marketplace, or internal feed.
2. Confirm whether the problem is approval, performance, match quality, or catalog completeness.
3. Treat platform policy enforcement as outside the model's control.

## Analysis workflow

1. Check feed completeness and consistency.
2. Look for:
   - price mismatch
   - availability mismatch
   - missing identifiers
   - weak titles
   - thin descriptions
   - broken or low-quality images
   - landing page mismatch
   - variant confusion
   - category mismatch
3. Prioritize issues by severity:
   - approval risk
   - performance risk
   - cleanup opportunity
4. Create a fix queue.

## Output format

### Feed verdict

Short summary of feed health.

### Issue table

| Item/SKU | Issue | Evidence | Severity | Recommended fix |
|---|---|---|---|---|

### Cleanup patterns

Reusable fixes for titles, descriptions, images, identifiers, and availability.

### Missing data

Any columns or diagnostics needed.

## Guardrails

- Do not guarantee platform approval.
- Do not invent GTINs, MPNs, brands, or product attributes.
- Do not edit feeds directly.
- Do not ignore landing page consistency.
- Do not recommend policy workarounds.
