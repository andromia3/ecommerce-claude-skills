# AGENTS.md: E-commerce operator skills

This repo is a pack of 20 Claude Skills for running an online store. Each skill is
a self-contained `SKILL.md` under its own folder, following the Agent Skills
standard, so the pack also runs in any other Agent Skills tool.

## How these skills behave

- **Data-first.** Every skill reads what you provide: store exports, COGS files,
  carrier invoices, product page URLs, screenshots, reviews, tickets, dispute
  reports. If the data is missing, the skill marks the finding `hypothesis` or
  `needs_data` instead of producing a number. This is the pack's one hard rule.
- **Human-in-the-loop.** Skills diagnose and recommend. They do not log into the
  store, the ad accounts, the payment provider or the helpdesk, and they change
  nothing live.
- **Honest about limits.** Every threshold inside a skill is a starting heuristic,
  not a rule any platform published. Where a genuine external standard exists it
  is named and dated, because the agentic commerce standards in particular are
  moving faster than any checklist.
- **Two-layer aware.** The storefront and the economics underneath it disagree
  constantly. A page can convert well and lose money; a channel can look cheap on
  ROAS and be unprofitable on contribution. Skills 1-10 read the first layer,
  11-20 read the second, and the pack expects you to check both.

## How the pack composes

- `weekly-ecommerce-growth-readout` is the entry point on a familiar store. It
  says what changed and routes to the right deep dive.
- `contribution-margin-check` comes before any scaling decision. Paid Traffic
  Waste Triage optimising on top of an unknown margin produces confident, wrong
  answers, and so does every promo and channel decision in the pack.
- Measurement before optimisation, twice over: know your margin before you judge
  a channel, and know your cohorts before you set a CAC target.
- `launch-readiness-check` is the cheapest skill to run and the one that catches
  the most expensive mistakes. It works from a brief and screenshots alone.
- Seven skills ship deterministic helpers in `scripts/` so the arithmetic is
  exact: `margin_stack.py`, `cohort_read.py`, `catalog_scan.py`,
  `promo_impact.py`, `shipping_recovery.py`, `subscription_survival.py` and
  `dispute_rate.py`. Prefer running them over
  eyeballing the numbers, and above roughly 150 SKUs the catalog audit requires
  its script rather than preferring it. `scripts/selftest.py` locks the
  guarantees those scripts make.
- `references/getting-your-data.md` says where every input actually lives. The
  bottleneck for most stores is assembling the file, not the analysis, so route
  there before telling someone their data is insufficient.
- `references/output-standard.md` holds the shared evidence, confidence and
  decision vocabulary every skill uses. `examples/` holds copy-paste prompts and
  worked output shapes. `playbooks/` chains skills into whole workflows.

## Where judgement shifts by store type

The same skill reads differently depending on what the store sells. This is the
context the skills expect you to supply, because it changes the answer.

- **Replenishable consumables** (coffee, supplements, skincare). The second-order
  window is short and the LTV read is the most valuable skill in the pack.
  Frequency mismatch is the dominant subscription churn cause. Returns are rare,
  so a return spike is a product or fulfilment signal, not noise.
- **Considered one-off purchases** (furniture, electronics, tools). Long research
  cycles, so onsite search and PDP content carry more weight than lifecycle
  flows. Shipping economics dominate margin because the items are heavy or
  oversize. Repeat purchase may genuinely not be the growth lever, and a skill
  suggesting otherwise should be overruled.
- **Fashion and apparel.** Returns are structural rather than exceptional, so the
  returns miner and sizing content are first-order concerns, and any margin
  number that ignores return rate is fiction. Catalog scale is high, so the
  catalog audit needs its script.
- **Marketplace-dependent stores.** Feed QA, catalog attributes and identifier
  completeness move from hygiene to survival, because a disapproval removes
  revenue rather than degrading it.
- **Subscription-first stores.** Run the subscription skill before the cohort
  skill; involuntary churn distorts every cohort curve until it is separated out.

## What not to do

- Do not run a skill without its required input. Skip it and say why.
- Do not treat ROAS as profit, or revenue-based LTV as something comparable to CAC.
- Do not report a cohort horizon the data has not reached.
- Do not present a sampled read of a large catalog as a full audit.
- Do not promise conversion lift, ranking, or inclusion on any AI or marketplace
  surface. Nobody controls those.
- Do not make a store change live because a skill recommended it. Every skill in
  this pack stops at approval-ready.
