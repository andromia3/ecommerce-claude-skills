# Copy-paste prompts

These prompts use synthetic situations. Replace the bracketed fields with your store data, exports, screenshots, URLs, or pasted reports.

## Checkout Friction Finder

```text
Use Checkout Friction Finder.

Store: [category, platform, market]
Goal: find checkout friction before increasing paid traffic.

Inputs attached/pasted:
- cart screenshot
- checkout screenshots
- shipping and return policy
- last 30 days checkout funnel, if available
- support questions about shipping, payment, discounts, and returns

Output:
- ranked friction table
- evidence tag for each finding
- severity, confidence, business impact, effort, owner decision
- what to measure after each fix

Do not promise conversion lift. Mark anything without data as hypothesis.
```

## Product Page Conversion Review

```text
Use Product Page Conversion Review.

Product URL or screenshots: [paste]
Category: [category]
Price point: [price]
Traffic source: [paid social / paid search / organic / email / mixed]
Target customer: [who buys]

Inputs attached/pasted:
- product facts and specs
- top reviews or objections
- competitor examples, optional

Output:
- top 3 conversion blockers
- unanswered buyer questions
- recommended page edits
- decision summary with evidence tags

Do not invent product claims or testimonials.
```

## Paid Traffic Waste Triage

```text
Use Paid Traffic Waste Triage.

Goal: find whether the performance problem is ads, product page, offer, feed, tracking, margin, or inventory.

Inputs attached/pasted:
- Meta/Google/TikTok ad export for [date range]
- landing page URLs
- product prices and margins, if available
- inventory status, if available
- recent changes to offer, tracking, product page, or budget

Output:
- likely leak layer
- waste table by segment
- evidence tags and confidence
- action queue grouped by ads, PDP, offer, feed, tracking, inventory, margin

Do not treat ROAS as profit unless margin data is provided.
```

## Repeat Purchase Flow Review

```text
Use Repeat Purchase Flow Review.

Store: [category]
Goal: improve second purchase / retention.

Inputs attached/pasted:
- flow screenshots or exports
- flow performance metrics
- product replenishment or repurchase cycle
- customer segments, if available

Output:
- missing or weak flows
- second-purchase hypotheses
- priority changes
- measurement plan

Do not recommend discounts as the default retention tactic.
```

## Inventory Risk Brief

```text
Use Inventory Risk Brief.

Goal: identify products that are stockout risks, overstock risks, or unsafe to promote.

Inputs attached/pasted:
- inventory export
- sales export for last [30/60/90] days
- incoming stock and ETA, if available
- promo calendar, if available
- margins or priority SKU list, if available

Output:
- stockout and overstock risk table
- marketing implication per SKU
- products safe to promote / avoid scaling / investigate

Do not infer inventory risk without inventory or sales exports.
```

## Product Feed QA

```text
Use Product Feed QA.

Goal: find feed issues before Shopping or catalog ads scale.

Inputs attached/pasted:
- product feed CSV or sample
- Merchant Center or catalog diagnostics screenshots
- affected product URLs
- target channel: [Google Shopping / Meta catalog / TikTok catalog / marketplace]

Output:
- approval risks
- performance risks
- feed cleanup queue
- evidence tags and severity

Do not invent product identifiers or guarantee platform approval.
```

## Returns Reason Miner

```text
Use Returns Reason Miner.

Goal: find preventable return patterns.

Inputs attached/pasted:
- returns export
- sales volume by SKU for the same period, if available
- return reason tags or free text
- product page URLs for affected products

Output:
- return pattern table
- likely root causes
- fixes grouped by PDP, sizing/specs, fulfillment, product, policy

Do not rank severity by return count alone if sales volume is missing.
```

## Support Ticket Theme Miner

```text
Use Support Ticket Theme Miner.

Goal: find repeated support themes and store-side fixes.

Inputs attached/pasted:
- support ticket export or chat transcripts
- tags/categories, if available
- help center or policy links
- affected product URLs, if relevant

Output:
- top themes
- likely root information gaps
- FAQ/PDP/policy/help center updates
- automation candidates and human escalation topics

Do not expose personal customer data in the output.
```

## Review and Objection Miner

```text
Use Review and Objection Miner.

Goal: extract buying triggers, objections, customer language, and PDP/ad angle ideas.

Inputs attached/pasted:
- review export or pasted reviews
- product facts
- product page URL
- competitor reviews, optional and clearly labeled

Output:
- repeated buying triggers
- repeated objections
- proof points
- customer language
- PDP FAQ and ad angle ideas

Do not fabricate testimonials or use competitor reviews as owned proof.
```

## Weekly E-commerce Growth Readout

```text
Use Weekly E-commerce Growth Readout.

Week: [date range]
Comparison period: [previous week / previous 4-week average / same week last year]
Owner goal: [revenue / profit / new customers / retention / sell-through / operations]

Inputs attached/pasted:
- store summary
- analytics summary
- paid traffic summary
- email/SMS summary
- inventory exceptions
- support and returns highlights

Output:
- weekly verdict
- scorecard
- what changed
- recommended 3 actions
- watch list
- missing data

Separate facts from hypotheses.
```
