# Getting your data out

The bottleneck for most stores is not the analysis, it is assembling the file.
This is where each input actually lives and what it is usually called, so the
gap between installing the pack and getting an answer is minutes rather than an
afternoon.

Nothing here needs a developer or a data warehouse. Every export below is a
button somewhere in an admin panel.

## The five files that unlock most of the pack

### 1. Product sales by SKU

Shopify: Analytics, Reports, "Sales by product variant SKU". Set the date range,
add the columns for net sales, discounts, returns and quantity, export CSV.
WooCommerce: Analytics, Products, download. BigCommerce: Analytics, Products.

Feeds: Contribution Margin Check, Catalog Content Audit (partly).

### 2. Product cost

This is the one nobody has cleanly, and it is worth thirty minutes once.

Shopify stores cost per item on the variant (Products, Inventory, Cost per item).
If it is filled in, export Products from the admin and you have it. If it is
empty for most SKUs, ask your bookkeeper for a purchase price list and match by
SKU, or export from your supplier's order confirmations.

The distinction that matters more than precision: **unit cost** is what you paid
the supplier, **landed cost** adds freight, duty and any import handling. Most
stores have the first and think they have the second, which is why margins read
better on paper than in the bank. If you only have unit cost, say so when you run
the skill. It will label the output as an assumption rather than quietly
overstating every margin.

Feeds: Contribution Margin Check, LTV and Cohort Read (to state value in
contribution rather than revenue).

### 3. Orders with customer id

Shopify: Analytics, Reports, "Sales over time" will not do it. You want the raw
orders export: Orders, Export, "All orders", CSV for Excel. It carries email,
created date, total and financial status.

The column you actually need is a stable customer identifier. Email works if
guest checkout is not fragmenting people across addresses, which it usually is a
little. Perfect is not required; consistent is.

Feeds: LTV and Cohort Read, Promo and Discount Impact Review, Shipping Economics
Review.

### 4. Carrier invoice

Your carrier account, billing or invoices, monthly PDF or CSV. Ask for CSV if you
only get PDFs; every major carrier will provide it.

What to check before using it: whether surcharges are itemised or bundled into
one figure per shipment. Fuel, residential delivery and address correction are
the three that usually hide inside a total, and a recovery rate calculated
without them looks better than reality.

Feeds: Shipping Economics Review, Contribution Margin Check.

### 5. Payment provider payouts and disputes

Stripe: Payments, then Disputes, export. Balance, Payouts for the settlement
report that shows real fees. Shopify Payments: Finances, Payouts, and Finances,
Disputes. PayPal: Reports, Activity download.

Feeds: Chargeback and Fraud Pattern Review, Contribution Margin Check (fee
rates).

## The rest, briefly

| Input | Where it lives |
|---|---|
| Subscriber export | Recharge, Skio, Stay AI or Shopify Subscriptions, Subscribers, export. Ask for cycle number and status |
| Dunning and failed payments | Same subscription app, or Stripe Billing, Invoices filtered to unpaid |
| Site search queries | Your search app (Searchanise, Klevu, Algolia, Boost) has a queries report. Shopify natively reports search terms under Analytics, Reports, "Top online store searches". If nothing logs zero-result queries, switching that on is the first job |
| Return reasons | Loop, Returnly, AfterShip or your platform's returns section, export with reason codes |
| Support tickets | Gorgias, Zendesk, Help Scout: export with tags and created dates. Tags matter more than ticket bodies here |
| Reviews | Judge.me, Okendo, Yotpo, Loox: export reviews with rating and product |
| Catalog | Shopify: Products, Export, all products, CSV. Note it writes one row per variant, which the catalog script collapses for you |
| Rendered page markup | Open a product page, view source, save it. Or use Google's Rich Results Test and copy the detected structured data |

## Two habits that save the most time

**Export wider than you think you need.** Adding a column later means redoing the
export and rerunning the analysis. Date, SKU, quantity, revenue, discount and any
cost column are cheap to include and expensive to go back for.

**Check the date range on the file, not on the screen.** Exports frequently
default to a different range than the report you were looking at. Every script in
this pack prints the period it actually found in the file. If that does not match
what you asked for, the export is the problem, not the analysis.

## What none of this needs

No API keys, no app installs, no read access granted to anyone, no data leaving
your machine except into the conversation you are already having. Every skill in
this pack works from files you already have permission to download.
