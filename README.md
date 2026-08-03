# 20 Claude Skills for E-commerce Owners

A pack of 20 practical Claude Skills for e-commerce owners, operators, and lean growth teams. The skills are designed to run without live platform integrations. They work from exports, screenshots, URLs, pasted reports, reviews, tickets, and store documentation.

Each skill is a self-contained `SKILL.md` with triggers, required inputs, an analysis workflow, output format, and guardrails. Drop them into Claude Code and they activate automatically when their use case matches the conversation.

The pack started at 10 skills, all of them about the storefront: the page, the checkout, the feed, the traffic. Skills 11-20 cover the two things that were missing. First, the money underneath the store: margin, discounts, shipping cost, customer value over time, and disputes. Second, the store as data: a catalog reviewed at scale rather than page by page, internal search as demand signal, and whether a machine reading the store gets the product right.

What this repo is not:

- not a collection of proven case studies
- not an ROI calculator
- not a live Shopify, Klaviyo, Meta Ads, or Google Ads integration
- not a replacement for analytics, inventory planning, legal review, or human approval

The first version is intentionally practical: bring exports, screenshots, URLs, reports, or pasted customer text, then use the skills to produce clearer decisions.

## What's inside

### Storefront and demand (1-10)

| # | Skill | Folder | Purpose |
|---|---|---|---|
| 1 | Checkout Friction Finder | `checkout-friction-finder-ecommerce` | Find likely cart and checkout friction from screenshots, funnel data, policies, and support notes |
| 2 | Product Page Conversion Review | `product-page-conversion-review-ecommerce` | Audit a product page for clarity, trust, proof, objections, and buying friction |
| 3 | Paid Traffic Waste Triage | `paid-traffic-waste-triage-ecommerce` | Connect paid traffic issues to store-side leaks, offer problems, feed issues, and margin constraints |
| 4 | Repeat Purchase Flow Review | `repeat-purchase-flow-review-ecommerce` | Review email/SMS lifecycle flows for second-purchase opportunities |
| 5 | Inventory Risk Brief | `inventory-risk-brief-ecommerce` | Turn inventory and sales exports into stockout, overstock, and promo risk notes |
| 6 | Product Feed QA | `product-feed-qa-ecommerce` | Check catalog and product feed issues before Shopping or catalog ads suffer |
| 7 | Returns Reason Miner | `returns-reason-miner-ecommerce` | Mine return exports for preventable return patterns and product/page fixes |
| 8 | Support Ticket Theme Miner | `support-ticket-theme-miner-ecommerce` | Turn repeated support tickets into FAQ, PDP, policy, automation, and product improvement notes |
| 9 | Review and Objection Miner | `review-objection-miner-ecommerce` | Extract buying triggers, objections, proof, and customer language from reviews |
| 10 | Weekly E-commerce Growth Readout | `weekly-ecommerce-growth-readout` | Produce a weekly owner-level readout across traffic, conversion, AOV, retention, inventory, support, and returns |

### Profit, retention and machine-readable store (11-20)

| # | Skill | Folder | Purpose |
|---|---|---|---|
| 11 | Contribution Margin Check | `contribution-margin-check-ecommerce` | Build the full cost stack per SKU and find which products make money after fees, shipping, returns, and ad spend |
| 12 | Promo and Discount Impact Review | `promo-discount-impact-review-ecommerce` | Test whether a promo added profit or pulled demand forward, and find discount leakage |
| 13 | Shipping Economics Review | `shipping-economics-review-ecommerce` | Compare shipping charged against shipping paid, and set a defensible threshold and delivery promise |
| 14 | LTV and Cohort Read | `ltv-cohort-read-ecommerce` | Read cohorts for repeat rate, second-order window, and payback by acquisition source |
| 15 | Subscription Churn Review | `subscription-churn-review-ecommerce` | Split voluntary from involuntary churn and find the flow, frequency, and billing causes behind both |
| 16 | Catalog Content Audit | `catalog-content-audit-ecommerce` | Audit product content across the whole catalog for gaps, duplicates, and channel blockers |
| 17 | AI Shopping Readiness | `ai-shopping-readiness-ecommerce` | Check whether product data, policies, and markup can be read correctly by AI assistants and agentic checkout |
| 18 | Chargeback and Fraud Pattern Review | `chargeback-fraud-pattern-review-ecommerce` | Separate genuine fraud from service failure and friendly fraud, and find the store-side causes |
| 19 | Onsite Search and Merchandising Review | `onsite-search-merchandising-review-ecommerce` | Turn internal search queries and zero-result searches into merchandising and assortment decisions |
| 20 | Launch Readiness Check | `launch-readiness-check-ecommerce` | Run a go/no-go across stock, page, checkout, feed, tracking, flows, support, and margin before traffic arrives |

## How to install

### Option A - Claude Code

1. Clone or download this repository.
2. Copy the skill folders into your project's `.claude/skills/` directory, or into the user-level skills directory at `~/.claude/skills/`.
3. Copy `scripts/` and `references/` alongside them. Ten skills reach for those by relative path (`../scripts/margin_stack.py`, `../references/output-standard.md`), so a skills-only copy installs the skills and quietly breaks their helpers.
4. Start a new Claude Code session. Skills will activate automatically when their description matches the conversation.

```bash
git clone https://github.com/mardab96/ecommerce-claude-skills.git
mkdir -p ~/.claude/skills
cp -r ecommerce-claude-skills/*ecommerce* \
      ecommerce-claude-skills/scripts \
      ecommerce-claude-skills/references \
      ~/.claude/skills/
```

### Option B - Other Claude environments

The skills are plain Markdown with YAML frontmatter. Paste the relevant `SKILL.md` content into context when you want to use it.

## Start here: what you can run today

Twenty skills is too many to triage on a Tuesday. This orders them by how hard
they are to feed, not by how interesting they are. Work down the list until you
run out of data.

| Effort to feed | Skills | What you need |
|---|---|---|
| Nothing to export | Launch Readiness Check, Product Page Conversion Review, Checkout Friction Finder | A brief, some URLs, screenshots |
| One export you already have | Shipping Economics Review, Chargeback and Fraud Pattern Review, Returns Reason Miner, Support Ticket Theme Miner, Review and Objection Miner, Onsite Search and Merchandising Review | One CSV from one tool |
| One export plus a cost file | Contribution Margin Check, Inventory Risk Brief, Promo and Discount Impact Review | Sales plus COGS, which is the file most stores have to build once |
| Needs history | LTV and Cohort Read, Subscription Churn Review | Twelve months or two purchase cycles |
| Needs a specific setup | AI Shopping Readiness, Catalog Content Audit, Product Feed QA | Rendered page markup, or a full catalog export |

If you have never run any of these, start with **Launch Readiness Check** (costs
nothing to feed and catches the most expensive mistakes) and **Contribution
Margin Check** (the one whose answer changes every other decision in the pack).

Building the COGS file is the single most common blocker, and it unlocks four
skills at once. [`references/getting-your-data.md`](references/getting-your-data.md)
says where every input in this pack actually lives in Shopify, Stripe, your
carrier account and your subscription app.

## Quick start packs

Use these combinations when you have a real store situation and do not know where to start.

| Situation | Skills to run | Final decision you want |
|---|---|---|
| Pre-scale audit | Product Page Conversion Review -> Checkout Friction Finder -> Paid Traffic Waste Triage -> Inventory Risk Brief | Which products/pages are safe to scale, what must be fixed first, what not to touch |
| Paid traffic loss diagnosis | Paid Traffic Waste Triage -> Product Page Conversion Review -> Product Feed QA -> Review and Objection Miner | Is the leak in ads, product page, offer, feed, margin, tracking, or inventory |
| Retention deep dive | Repeat Purchase Flow Review -> Review and Objection Miner -> Support Ticket Theme Miner | What should improve second purchase, post-purchase experience, and customer education |
| Inventory and operations review | Inventory Risk Brief -> Returns Reason Miner -> Support Ticket Theme Miner -> Weekly E-commerce Growth Readout | Which SKUs are stockout/overstock/support/return risks |
| Weekly owner review | Weekly E-commerce Growth Readout -> whichever skill the readout flags | What changed, what matters, and the next 3 actions |
| Profit reality check | Contribution Margin Check -> Shipping Economics Review -> Promo and Discount Impact Review | Which products and which promos actually make money after every variable cost |
| Acquisition budget decision | LTV and Cohort Read -> Contribution Margin Check -> Paid Traffic Waste Triage | What a first order can cost, and which channel earns customers who come back |
| Retention and subscription rescue | Subscription Churn Review -> LTV and Cohort Read -> Support Ticket Theme Miner | Whether the leak is billing, frequency, product fit, or flow design |
| Catalog and discoverability push | Catalog Content Audit -> AI Shopping Readiness -> Product Feed QA -> Onsite Search and Merchandising Review | Whether the catalog is readable by customers, channels, and machines |
| Pre-launch go/no-go | Launch Readiness Check -> whichever layer it flags | Go, go with conditions, or hold, with owners and a rollback plan |
| Rising disputes | Chargeback and Fraud Pattern Review -> Support Ticket Theme Miner -> Returns Reason Miner | Whether the cause is fraud, service failure, or friendly fraud |

## Bring your data

These skills do not require live access to Shopify, WooCommerce, Klaviyo, Meta Ads, Google Ads, Gorgias, Zendesk, GA4, or Google Merchant Center.

They work best with:

- product page URLs or screenshots
- checkout screenshots
- Shopify, WooCommerce, BigCommerce, Magento, or custom store exports
- ad platform CSV exports
- Google Merchant Center diagnostics exports or screenshots
- Klaviyo, Mailchimp, Omnisend, Attentive, or email/SMS flow reports
- reviews exports
- support tickets or chat transcripts
- return reason exports
- weekly analytics summaries
- COGS or landed cost files
- payment provider payout and settlement reports
- carrier invoices including surcharges
- customer-level order history for cohorts
- subscriber lists with cycle and status
- dispute and chargeback exports with reason codes
- internal site search and zero-result query exports
- rendered product page markup

## Guardrails

By default these skills do not:

- change budgets
- publish ads
- edit product pages
- change checkout settings
- update product feeds
- alter return policies
- send customer messages
- modify inventory systems
- change prices, discounts, or shipping thresholds
- change billing, dunning, fraud, or risk settings
- change robots, crawl, or bot protection rules
- make unsupported performance claims
- promise visibility or inclusion on any AI or marketplace surface

Use them to structure diagnosis and prepare approval-ready recommendations.

## Output standard

Every useful output should separate evidence from hypothesis and end with a decision summary.

Use these fields when a skill returns findings:

| Field | Allowed values |
|---|---|
| Evidence | `export`, `screenshot`, `url`, `review_cluster`, `support_ticket`, `return_reason`, `policy`, `feed_diagnostics`, `margin_csv`, `inventory_export`, `cogs_export`, `payout_report`, `shipping_invoice`, `cohort_export`, `subscription_export`, `chargeback_export`, `site_search_export`, `structured_data`, `promo_calendar`, `hypothesis`, `needs_data` |
| Severity | `low`, `medium`, `high`, `critical` |
| Confidence | `low`, `medium`, `high` |
| Business impact | `revenue`, `margin`, `cashflow`, `retention`, `conversion`, `support_load`, `risk` |
| Effort | `XS`, `S`, `M`, `L` |
| Owner decision | `do_now`, `test`, `investigate`, `monitor`, `ignore`, `approval_needed` |

Minimum decision summary:

| Finding | Evidence | Severity | Confidence | Business impact | Effort | Owner decision |
|---|---|---|---|---|---|---|

Hard rule: if the skill lacks evidence, it must mark the finding as `hypothesis` or `needs_data`, not as fact.

## Scripts

Seven skills are arithmetic-heavy, and a model doing that arithmetic by eye
produces numbers that look right and are not. Those seven ship deterministic
helpers instead. Python 3 standard library only, no dependencies, no network,
nothing written back to your files.

| Script | Used by |
|---|---|
| [`scripts/margin_stack.py`](scripts/margin_stack.py) | Contribution Margin Check |
| [`scripts/cohort_read.py`](scripts/cohort_read.py) | LTV and Cohort Read |
| [`scripts/catalog_scan.py`](scripts/catalog_scan.py) | Catalog Content Audit |
| [`scripts/promo_impact.py`](scripts/promo_impact.py) | Promo and Discount Impact Review |
| [`scripts/shipping_recovery.py`](scripts/shipping_recovery.py) | Shipping Economics Review |
| [`scripts/subscription_survival.py`](scripts/subscription_survival.py) | Subscription Churn Review |
| [`scripts/dispute_rate.py`](scripts/dispute_rate.py) | Chargeback and Fraud Pattern Review |

```bash
python3 scripts/margin_stack.py products.csv --payment-fee-pct 2.9
python3 scripts/cohort_read.py orders.csv --by source
python3 scripts/catalog_scan.py catalog.csv
```

Details in [`scripts/README.md`](scripts/README.md). The guarantees worth
knowing: absent cost lines are reported rather than invented, an immature cohort
prints a dash rather than a zero, catalog counting is exhaustive or the output
says it was sampled, a promo is never judged without its recovery period, and
churn is never reported as one number.

`scripts/validate-skills.py` checks every skill in the pack for required
sections, an activation phrase, workflow depth and undeclared evidence tags, and
`scripts/selftest.py` runs seventeen regression checks over the analysis scripts,
one per bug that actually shipped. Both have a `--selftest` or self-proving mode,
because a check nobody has seen fail is not evidence of anything.

## Examples and playbooks

- Copy-paste prompts: [`examples/copy-paste-prompts.md`](examples/copy-paste-prompts.md)
- Example outputs, including real script runs: [`examples/demo-outputs.md`](examples/demo-outputs.md)
- Owner playbooks: [`playbooks/README.md`](playbooks/README.md)
- Output quality rubric: [`references/output-standard.md`](references/output-standard.md)
- Where every input actually lives in your admin panels: [`references/getting-your-data.md`](references/getting-your-data.md)
- How the pack composes and where judgement shifts by store type: [`AGENTS.md`](AGENTS.md)
- Version history: [`CHANGELOG.md`](CHANGELOG.md)

## License and attribution

MIT, see [`LICENSE`](LICENSE). Free to use, modify, and redistribute for personal and commercial work. If you ship something built on top of these skills, a credit is appreciated but not required.

Built and maintained by [AdLume](https://adlume.co) - performance marketing infrastructure for AI-native operators.
