---
name: subscription-churn-review-ecommerce
description: Diagnoses subscription and replenishment churn from subscriber exports, cancellation reasons, failed payments, and flow settings. Use for subscribe-and-save, refill, or membership programmes when churn is rising, cycle-two drop-off is heavy, or involuntary churn has never been separated from voluntary.
---

# Subscription Churn Review - E-commerce

## Use this skill when

The store runs subscriptions, replenishment, or a membership, and retention is worse than it should be.

Common requests:

- "Why do people cancel after the second box?"
- "Our churn is 9% a month. Is that bad?"
- "How much of this is failed payments?"
- "Should we let people skip instead of cancel?"

## Required input

Minimum useful input:

- Subscriber export: start date, cycle number, status, cancellation date.
- Cancellation reasons if captured.
- Billing interval and product.

Recommended additional input:

- Failed payment and dunning logs.
- Skip, pause, swap, and delay usage.
- Cancellation flow screenshots.
- Support tickets about subscriptions.
- Discount structure on first cycle versus later cycles.
- Delivery timing performance.

## Before analysis

1. Separate voluntary churn from involuntary churn before saying anything about the offer. Failed cards are a billing problem, not a value problem.
2. Confirm the cycle length, because month-based churn on a 60-day cycle is misleading.
3. Confirm whether pauses and skips are counted as churn in the store's own reporting. They usually are, wrongly.
4. Ask whether the first cycle was discounted, and by how much.

## Analysis workflow

1. Build survival by cycle: what share of subscribers reach cycle 2, 3, 4, 6, and 12.
2. Split churn into voluntary, involuntary, and pause-not-resumed. Report each separately.
3. For involuntary churn, check the dunning setup: retry count, retry spacing, card updater, pre-dunning notice, and what the customer sees.
4. For voluntary churn, cluster cancellation reasons into: too much product, price, product fit, delivery problems, forgot they subscribed, life change, and unspecified.
5. Check the cancellation flow for missing off-ramps: skip, delay, reduce quantity, swap product, change frequency. Cancellation is often the only visible button.
6. Compare cohorts by first-cycle discount depth, acquisition source, and entry product.
7. Match frequency to real consumption rate. Sending product faster than people use it is the most common cause of "too much product" churn.

## Decision and evidence standard

Tag every finding with evidence: `subscription_export`, `export`, `support_ticket`, `screenshot`, `policy`, `hypothesis`, or `needs_data`. Full vocabulary: `references/output-standard.md`.

Each finding also carries severity, confidence, business impact, effort, and owner decision.

Cancellation reason fields are self-reported. Treat them as signal, not proof, and say so.

## Output format

### Churn verdict

Is the leak billing, frequency, product fit, price, or flow design. State confidence.

### Survival table

| Cycle | Subscribers entering | Retained | Voluntary churn | Involuntary churn | Paused |
|---|---|---|---|---|---|

### Involuntary churn findings

Dunning gaps and the recoverable share, stated as an estimate with its basis.

### Voluntary churn clusters

| Reason cluster | Share | Evidence | Fix | Effort |
|---|---|---|---|---|

### Flow fixes

Off-ramps missing from the cancellation flow, ordered by expected retention effect.

### Missing data

## Example input and output

Input:

- subscriber export with cycle and status
- cancellation reason export
- dunning log
- cancellation flow screenshots

Good output excerpt:

| Finding | Evidence | Severity | Confidence | Business impact | Effort | Owner decision |
|---|---|---|---|---|---|---|
| A third of cancellations are failed payments with a single retry and no card updater | `subscription_export`, `needs_data` | critical | medium | revenue/retention | S | do_now |
| The cancellation flow offers no skip or frequency change, and "too much product" is the largest stated reason | `screenshot`, `support_ticket` | high | medium | retention | M | test |

What not to do yet: rebuild the offer because churn is high, when a third of it is a card retry setting.

## Guardrails

- Do not report a single churn number without splitting voluntary and involuntary.
- Do not treat pauses as cancellations.
- Do not make retention harder by hiding the cancel option. Fix the reason, not the exit.
- Do not promise a recovery percentage from dunning changes.
- Do not change live billing, retry, or subscription settings without approval.
