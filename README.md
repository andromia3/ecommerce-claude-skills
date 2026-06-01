# E-commerce Operator Claude Skills

A pack of 10 practical Claude Skills for e-commerce owners, operators, and lean growth teams. The skills are designed to run without live platform integrations. They work from exports, screenshots, URLs, pasted reports, reviews, tickets, and store documentation.

Each skill is a self-contained `SKILL.md` with triggers, required inputs, an analysis workflow, output format, and guardrails. Drop them into Claude Code and they activate automatically when their use case matches the conversation.

What this repo is not:

- not a collection of proven case studies
- not an ROI calculator
- not a live Shopify, Klaviyo, Meta Ads, or Google Ads integration
- not a replacement for analytics, inventory planning, legal review, or human approval

The first version is intentionally practical: bring exports, screenshots, URLs, reports, or pasted customer text, then use the skills to produce clearer decisions.

## What's inside

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

## How to install

### Option A - Claude Code

1. Clone or download this repository.
2. Copy the skill folders into your project's `.claude/skills/` directory, or into the user-level skills directory at `~/.claude/skills/`.
3. Start a new Claude Code session. Skills will activate automatically when their description matches the conversation.

```bash
git clone https://github.com/mardab96/ecommerce-claude-skills.git
cp -r ecommerce-claude-skills/* ~/.claude/skills/
```

### Option B - Other Claude environments

The skills are plain Markdown with YAML frontmatter. Paste the relevant `SKILL.md` content into context when you want to use it.

## Quick start packs

Use these combinations when you have a real store situation and do not know where to start.

| Situation | Skills to run | Final decision you want |
|---|---|---|
| Pre-scale audit | Product Page Conversion Review -> Checkout Friction Finder -> Paid Traffic Waste Triage -> Inventory Risk Brief | Which products/pages are safe to scale, what must be fixed first, what not to touch |
| Paid traffic loss diagnosis | Paid Traffic Waste Triage -> Product Page Conversion Review -> Product Feed QA -> Review and Objection Miner | Is the leak in ads, product page, offer, feed, margin, tracking, or inventory |
| Retention deep dive | Repeat Purchase Flow Review -> Review and Objection Miner -> Support Ticket Theme Miner | What should improve second purchase, post-purchase experience, and customer education |
| Inventory and operations review | Inventory Risk Brief -> Returns Reason Miner -> Support Ticket Theme Miner -> Weekly E-commerce Growth Readout | Which SKUs are stockout/overstock/support/return risks |
| Weekly owner review | Weekly E-commerce Growth Readout -> whichever skill the readout flags | What changed, what matters, and the next 3 actions |

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
- make unsupported performance claims

Use them to structure diagnosis and prepare approval-ready recommendations.

## Output standard

Every useful output should separate evidence from hypothesis and end with a decision summary.

Use these fields when a skill returns findings:

| Field | Allowed values |
|---|---|
| Evidence | `export`, `screenshot`, `url`, `review_cluster`, `support_ticket`, `return_reason`, `policy`, `feed_diagnostics`, `margin_csv`, `inventory_export`, `hypothesis`, `needs_data` |
| Severity | `low`, `medium`, `high`, `critical` |
| Confidence | `low`, `medium`, `high` |
| Business impact | `revenue`, `margin`, `cashflow`, `retention`, `conversion`, `support_load`, `risk` |
| Effort | `XS`, `S`, `M`, `L` |
| Owner decision | `do_now`, `test`, `investigate`, `monitor`, `ignore`, `approval_needed` |

Minimum decision summary:

| Finding | Evidence | Severity | Confidence | Business impact | Effort | Owner decision |
|---|---|---|---|---|---|---|

Hard rule: if the skill lacks evidence, it must mark the finding as `hypothesis` or `needs_data`, not as fact.

## Examples and playbooks

- Copy-paste prompts: [`examples/copy-paste-prompts.md`](examples/copy-paste-prompts.md)
- Example outputs: [`examples/demo-outputs.md`](examples/demo-outputs.md)
- Owner playbooks: [`playbooks/README.md`](playbooks/README.md)
- Output quality rubric: [`references/output-standard.md`](references/output-standard.md)

## License and attribution

Free to use, modify, and redistribute for personal and commercial work. If you ship something built on top of these skills, a credit is appreciated but not required.

Built and maintained by [AdLume](https://adlume.co) - performance marketing infrastructure for AI-native operators.
