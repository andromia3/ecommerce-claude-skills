# Output standard

Use this standard when evaluating whether a skill output is useful for a store owner.

## Required qualities

An output is good when it:

- separates evidence from hypothesis
- names missing data clearly
- prioritizes findings
- includes business impact
- includes confidence
- includes effort
- gives an owner decision
- avoids live changes without approval
- avoids unsupported ROI or conversion lift claims

## Evidence tags

Use one or more:

- `export`
- `screenshot`
- `url`
- `review_cluster`
- `support_ticket`
- `return_reason`
- `policy`
- `feed_diagnostics`
- `margin_csv`
- `inventory_export`
- `hypothesis`
- `needs_data`

## Decision fields

| Field | Values |
|---|---|
| Severity | `low`, `medium`, `high`, `critical` |
| Confidence | `low`, `medium`, `high` |
| Business impact | `revenue`, `margin`, `cashflow`, `retention`, `conversion`, `support_load`, `risk` |
| Effort | `XS`, `S`, `M`, `L` |
| Owner decision | `do_now`, `test`, `investigate`, `monitor`, `ignore`, `approval_needed` |

## Decision summary template

```md
## Decision Summary

| Finding | Evidence | Severity | Confidence | Business impact | Effort | Owner decision |
|---|---|---|---|---|---|---|
| [finding] | [tag] | [value] | [value] | [value] | [value] | [value] |

## What not to do yet

- [live/costly/public action that should wait for approval or better data]

## Missing data

- [data needed to improve confidence]
```

## Common failure modes

Fail the output if it:

- treats ROAS as profit without margin data
- recommends increasing spend without stock and margin context
- recommends discounts as the first solution without evidence
- invents testimonials, product claims, or benchmark numbers
- treats screenshots as proof of impact
- hides missing data
- presents projected savings as guaranteed savings
- recommends live changes without approval
