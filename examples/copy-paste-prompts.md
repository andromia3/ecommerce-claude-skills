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

## Contribution Margin Check

```text
Use Contribution Margin Check.

Period: [date range]
Store: [category, platform, market]
Goal: find which SKUs make money after every variable cost.

Inputs attached/pasted:
- product sales export with units, revenue, discounts
- COGS per SKU [unit cost only / landed cost]
- payment and platform fee rates
- shipping cost basis [real per order / per zone / flat assumption]
- ad spend mapped to products or collections, if available
- refund rate per SKU, if available

Output:
- cost stack table with the source and confidence of every line
- contribution margin before and after ad spend, kept separate
- per-SKU table with breakeven ROAS
- money-losing SKUs and the smallest change that flips each one
- missing data

Mark every cost I did not supply as an assumption with low confidence.
Do not treat ROAS as profit.
```

## Promo and Discount Impact Review

```text
Use Promo and Discount Impact Review.

Promo: [mechanic, depth, dates]
Baseline period: [date range]
Goal of the promo was: [revenue / profit / new customers / clearing stock / cash]

Inputs attached/pasted:
- daily orders or revenue covering baseline, promo, and the weeks after
- discount code usage export
- COGS or margin for the discounted products
- ad spend during the window
- promo calendar for the last 12 months

Output:
- promo verdict with the baseline stated
- promo economics table
- pull-forward check on the weeks after
- leakage findings
- promo rules for the next calendar
- missing data

Do not attribute lift to the discount if ad spend also rose.
```

## Shipping Economics Review

```text
Use Shipping Economics Review.

Market(s): [where we ship]
Current rules: [thresholds, flat rates, zones, express]
Goal: [protect margin / set a threshold / fix delivery promise / decide on paid returns]

Inputs attached/pasted:
- carrier invoice for [period], including surcharges
- order export with order value, destination, shipping charged
- product weights and dimensions, if available
- packaging cost per order type
- support tickets tagged delivery

Output:
- shipping recovery rate overall and by zone
- order value bands where we lose money on delivery
- threshold analysis against actual AOV distribution
- two or three scenarios with assumptions and risks stated
- delivery promise versus performance
- missing data

Label projected savings as projected. Do not change live rates.
```

## LTV and Cohort Read

```text
Use LTV and Cohort Read.

History available: [months]
Value basis: [revenue / contribution margin]
Decision this feeds: [CAC target / channel budget / entry product / flow timing]

Inputs attached/pasted:
- order export with customer id, date, value
- acquisition source per first order, if available
- first product or collection purchased
- discount used on first order
- ad spend by channel by month
- COGS per SKU

Output:
- cohort table at 30 / 90 / 180 / 365 days
- repeat rate and median time to second order
- the second-order window where reorder probability collapses
- segment comparison with cohort sizes shown
- payback window by channel
- missing data

Do not project the curve past the data. State cohort sizes next to every comparison.
```

## Subscription Churn Review

```text
Use Subscription Churn Review.

Programme: [subscribe-and-save / refill / membership]
Billing interval: [interval]
First cycle discount: [depth or none]

Inputs attached/pasted:
- subscriber export with start date, cycle number, status, cancellation date
- cancellation reasons
- failed payment and dunning logs
- skip / pause / swap usage
- cancellation flow screenshots
- support tickets about subscriptions

Output:
- survival by cycle
- churn split into voluntary, involuntary, and paused-not-resumed
- dunning gaps
- voluntary churn reason clusters
- missing off-ramps in the cancellation flow
- missing data

Do not report one churn number. Split it before interpreting the offer.
```

## Catalog Content Audit

```text
Use Catalog Content Audit.

Catalog size: [number of SKUs]
Destination: [own store / marketplace / Shopping feed / catalog ads]
Benchmark: [URLs of our best product pages]

Inputs attached/pasted:
- catalog export with title, description, attributes, image count, category, price
- sessions and revenue per product
- attribute requirements for the destination channel
- brand voice or copy guidelines

Output:
- coverage scorecard by category, weighted by revenue
- duplicate and supplier-copy detection
- attribute gaps that block the destination channel
- priority work queue by commercial weight
- template proposals that close whole clusters
- missing data

Never fill a missing specification from assumption. Mark it needs_data.
```

## AI Shopping Readiness

```text
Use AI Shopping Readiness.

Goal: [be described correctly / be findable / support agentic checkout]
Platform and payment provider: [stack]

Inputs attached/pasted:
- product page URLs or rendered HTML
- feed sample
- shipping, returns, and warranty policy pages
- screenshots of an assistant describing our product incorrectly, if any

Output:
- readiness verdict with what was checked and when
- data legibility table
- policy legibility check
- standards exposure by layer with platform support today
- work split: fix now / wait for platform / not worth it yet
- missing data

Do not promise visibility or ranking on any AI surface.
Do not present a moving standard as settled.
```

## Chargeback and Fraud Pattern Review

```text
Use Chargeback and Fraud Pattern Review.

Period: [date range]
Provider warning received: [yes / no]
Recurring billing: [yes / no]

Inputs attached/pasted:
- dispute export with date, amount, reason code, product, outcome
- order volume for the same period
- current fraud rules or risk tool settings
- declined order export
- bank statement descriptor
- support tickets preceding disputes

Output:
- dispute rate against the correct denominator
- breakdown by reason family with the likely real cause
- store-side operational causes ranked by volume
- over-blocking check with its cost basis
- prevention queue
- missing data

Reason codes are what the customer claimed, not what happened. Treat them that way.
Do not give legal or card-scheme advice.
```

## Onsite Search and Merchandising Review

```text
Use Onsite Search and Merchandising Review.

Period: [date range]
Volume floor: [minimum searches to include]
Search tool: [tool, and whether it logs zero-result queries]

Inputs attached/pasted:
- site search query export with volume and result count
- zero-result queries
- conversion rate for searchers versus non-searchers
- collection page performance
- product naming and tagging conventions
- review export for customer language

Output:
- query table with failure type per query
- zero-result clusters classified as: no such product / naming mismatch / synonym gap / misspelling
- assortment questions sized and handed to me as decisions
- merchandising fixes ordered by volume covered per unit of work
- missing data

Do not turn query volume into a sales forecast.
```

## Launch Readiness Check

```text
Use Launch Readiness Check.

Launching: [what]
Date: [date]
Expected traffic or spend: [number]
Hard launch or staged: [which]
Who owns the go decision: [name]

Inputs attached/pasted:
- launch product URLs or screenshots
- stock position for launch SKUs
- feed or catalog status
- tracking status
- email and SMS flows scheduled around the launch
- promo code details and exclusions
- margin at the planned price
- rollback plan and who can execute it

Output:
- go / go with conditions / hold, with conditions owned
- readiness board across all eight layers
- blockers ordered by launch-day cost
- oversell scenario
- first-hour watch list with rollback triggers
- missing data

A layer nobody verified is needs_data, not ready.
```
