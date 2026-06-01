# E-commerce Operator Claude Skills

A pack of 10 practical Claude Skills for e-commerce owners, operators, and lean growth teams. The skills are designed to run without live platform integrations. They work from exports, screenshots, URLs, pasted reports, reviews, tickets, and store documentation.

Each skill is a self-contained `SKILL.md` with triggers, required inputs, an analysis workflow, output format, and guardrails. Drop them into Claude Code and they activate automatically when their use case matches the conversation.

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

## License and attribution

Free to use, modify, and redistribute for personal and commercial work. If you ship something built on top of these skills, a credit is appreciated but not required.

Built and maintained by [AdLume](https://adlume.co) - performance marketing infrastructure for AI-native operators.
