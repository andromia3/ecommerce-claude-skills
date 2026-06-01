---
name: support-ticket-theme-miner-ecommerce
description: Analyzes e-commerce support ticket exports, chat transcripts, email samples, and help center content to identify repeated questions, policy confusion, product information gaps, and automation candidates.
---

# Support Ticket Theme Miner - E-commerce

## Use this skill when

The user wants to turn support tickets into store improvements.

Common requests:

- "Analyze these support tickets."
- "What questions keep repeating?"
- "What should we add to product pages or FAQ?"
- "Find automation candidates for support."

## Required input

Minimum useful input:

- Support tickets, chats, or email samples.
- Time period and channel.
- Tags or categories if available.
- Help center, policy, or FAQ links if available.

Optional:

- Product page URLs.
- Order status tags.
- Resolution time.
- Customer sentiment.
- Refund or return outcomes.

## Before analysis

1. Confirm whether tickets are pre-purchase, post-purchase, support, returns, or mixed.
2. Remove or avoid exposing sensitive customer data where possible.
3. Do not recommend full automation before identifying theme quality.
4. Keep escalation topics human.

## Analysis workflow

1. Cluster tickets by theme:
   - order status
   - shipping time
   - returns/exchanges
   - sizing/fit
   - compatibility
   - product usage
   - discount/payment issues
   - damaged/wrong item
   - policy confusion
2. Identify repeated questions and root information gaps.
3. Map themes to fixes:
   - product page
   - checkout
   - help center
   - transactional email
   - support macro
   - automation candidate
   - human escalation
4. Prioritize by frequency, buyer impact, and operational load.

## Output format

### Support verdict

Top repeated themes and the likely store-side causes.

### Theme table

| Theme | Frequency signal | Likely cause | Recommended fix | Automation fit |
|---|---|---|---|---|

### Content updates

FAQ, PDP, policy, and help center updates to consider.

### Human escalation topics

Issues that should stay with a human agent.

## Guardrails

- Do not expose personal customer data.
- Do not write final support macros unless policy and tone are provided.
- Do not automate refunds, cancellations, or sensitive complaints by default.
- Do not treat high frequency as proof that customers are wrong.
- Do not ignore product or fulfillment root causes.
