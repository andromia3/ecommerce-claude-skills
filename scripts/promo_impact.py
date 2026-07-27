#!/usr/bin/env python3
"""Measure a promo against a baseline, including the trough after it.

Used by: promo-discount-impact-review-ecommerce

Why this exists: the promo week always beats an ordinary week, so the promo
always looks like it worked. The question is what the surrounding weeks did.
This computes the baseline, the window, and the recovery period on the same
footing, so pull-forward shows up as the negative number it is instead of being
left out of the story.

Input: one CSV with a row per DAY (or per order; days are aggregated).

  date, revenue      required
  orders             optional, gives AOV
  ad_spend           optional, so budget-driven lift is not credited to the discount
  discount           optional, total discount given that day

usage:
  python3 scripts/promo_impact.py daily.csv --promo-start 2026-11-27 --promo-end 2026-12-01
  python3 scripts/promo_impact.py daily.csv --promo-start ... --promo-end ... --json

Baseline defaults to the 28 days before the promo, recovery to the same number
of days as the promo itself. Both are overridable.

exit 0 = ran, 2 = could not run.
"""
import argparse
import csv
import json
import sys
from datetime import datetime, timedelta

ALIASES = {
    "date": ["date", "day", "order date", "created at", "processed at"],
    "revenue": ["revenue", "net sales", "total sales", "sales", "total"],
    "orders": ["orders", "order count", "quantity", "count"],
    "ad_spend": ["ad spend", "spend", "amount spent", "marketing cost"],
    "discount": ["discount", "discounts", "discount amount", "total discounts"],
}
DATE_FORMATS = ["%Y-%m-%d", "%Y/%m/%d", "%d/%m/%Y", "%m/%d/%Y", "%d.%m.%Y"]


def norm(s):
    return " ".join(str(s or "").strip().lower().replace("_", " ").split())


def parse_date(raw):
    s = str(raw or "").strip().split("T")[0].split(" ")[0]
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None


def money(raw):
    s = str(raw or "").strip()
    neg = s.startswith("(") and s.endswith(")")
    for ch in "()$£€ ,":
        s = s.replace(ch, "")
    try:
        v = float(s)
    except ValueError:
        return 0.0
    return -v if neg else v


def window_stats(days, start, end):
    rows = [d for d in days.values() if start <= d["date"] <= end]
    n = (end - start).days + 1
    rev = sum(r["revenue"] for r in rows)
    orders = sum(r["orders"] for r in rows)
    spend = sum(r["ad_spend"] for r in rows)
    disc = sum(r["discount"] for r in rows)
    return {
        "days": n, "days_with_data": len(rows),
        "revenue": round(rev, 2), "revenue_per_day": round(rev / n, 2) if n else 0.0,
        "orders": round(orders, 2), "orders_per_day": round(orders / n, 2) if n else 0.0,
        "aov": round(rev / orders, 2) if orders else None,
        "ad_spend": round(spend, 2), "ad_spend_per_day": round(spend / n, 2) if n else 0.0,
        "discount_given": round(disc, 2),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path")
    ap.add_argument("--promo-start", required=True)
    ap.add_argument("--promo-end", required=True)
    ap.add_argument("--baseline-days", type=int, default=28)
    ap.add_argument("--recovery-days", type=int, default=None)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    p_start, p_end = parse_date(args.promo_start), parse_date(args.promo_end)
    if not p_start or not p_end or p_end < p_start:
        print("promo start/end must be valid dates with end on or after start", file=sys.stderr)
        return 2

    try:
        with open(args.csv_path, newline="", encoding="utf-8-sig") as fh:
            rows = list(csv.DictReader(fh))
    except OSError as exc:
        print("could not read %s: %s" % (args.csv_path, exc), file=sys.stderr)
        return 2
    if not rows:
        print("no rows", file=sys.stderr)
        return 2

    header = {norm(h): h for h in rows[0].keys()}
    cm = {}
    for key, aliases in ALIASES.items():
        for alias in aliases:
            if alias in header:
                cm[key] = header[alias]
                break
    for req in ("date", "revenue"):
        if req not in cm:
            print("missing required column: %s" % req, file=sys.stderr)
            print("columns found: %s" % ", ".join(rows[0].keys()), file=sys.stderr)
            return 2

    days = {}
    skipped = 0
    for row in rows:
        d = parse_date(row.get(cm["date"]))
        if d is None:
            skipped += 1
            continue
        rec = days.setdefault(d, {"date": d, "revenue": 0.0, "orders": 0.0,
                                  "ad_spend": 0.0, "discount": 0.0})
        rec["revenue"] += money(row.get(cm["revenue"]))
        for key in ("orders", "ad_spend", "discount"):
            if cm.get(key):
                rec[key] += money(row.get(cm[key]))
    if not days:
        print("no parseable dates", file=sys.stderr)
        return 2

    promo_len = (p_end - p_start).days + 1
    rec_len = args.recovery_days if args.recovery_days is not None else promo_len

    base = window_stats(days, p_start - timedelta(days=args.baseline_days), p_start - timedelta(days=1))
    promo = window_stats(days, p_start, p_end)
    after = window_stats(days, p_end + timedelta(days=1), p_end + timedelta(days=rec_len))

    uplift = promo["revenue_per_day"] - base["revenue_per_day"]
    trough = after["revenue_per_day"] - base["revenue_per_day"]
    net_per_day = uplift + trough
    combined_gain = uplift * promo_len + trough * rec_len

    spend_rose = (promo["ad_spend_per_day"] > base["ad_spend_per_day"] * 1.1
                  and base["ad_spend_per_day"] > 0)

    result = {
        "baseline": base, "promo": promo, "recovery": after,
        "promo_days": promo_len, "recovery_days": rec_len,
        "uplift_per_day_vs_baseline": round(uplift, 2),
        "trough_per_day_vs_baseline": round(trough, 2),
        "net_revenue_vs_baseline_over_both_windows": round(combined_gain, 2),
        "discount_given_in_window": promo["discount_given"],
        "ad_spend_rose_during_promo": spend_rose,
        "rows_skipped": skipped,
        "coverage_warnings": [],
    }
    for label, w in (("baseline", base), ("promo", promo), ("recovery", after)):
        if w["days_with_data"] < w["days"]:
            # every gappy window matters: a missing baseline invalidates the
            # uplift, a missing recovery hides the trough. Collect them all
            # rather than letting the last one overwrite the rest.
            result["coverage_warnings"].append(
                "%s window has %d of %d days present in the file"
                % (label, w["days_with_data"], w["days"]))

    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print("promo %s to %s (%d days), baseline %d days before, recovery %d days after"
          % (p_start, p_end, promo_len, args.baseline_days, rec_len))
    print()
    print("%-12s %12s %12s %10s %12s" % ("window", "rev/day", "orders/day", "AOV", "spend/day"))
    for label, w in (("baseline", base), ("promo", promo), ("recovery", after)):
        print("%-12s %12.2f %12.2f %10s %12.2f"
              % (label, w["revenue_per_day"], w["orders_per_day"],
                 "-" if w["aov"] is None else "%.2f" % w["aov"], w["ad_spend_per_day"]))
    print()
    print("uplift during promo:      %+12.2f per day" % uplift)
    print("trough after promo:       %+12.2f per day" % trough)
    print("net across both windows:  %+12.2f total" % combined_gain)
    if promo["discount_given"]:
        print("discount given away:      %12.2f" % promo["discount_given"])
    print()
    if trough < 0 and combined_gain <= 0:
        print("READ: the window plus its recovery period did not beat the baseline. "
              "That is pull-forward, not growth.")
    elif trough < 0:
        print("READ: there is a real trough after the promo. The gain is smaller than "
              "the promo window alone suggests.")
    if spend_rose:
        print("WARNING: ad spend per day rose %.0f%% during the promo. Lift cannot be "
              "credited to the discount without separating the two."
              % ((promo["ad_spend_per_day"] / base["ad_spend_per_day"] - 1) * 100))
    if not cm.get("ad_spend"):
        print("NOTE: no ad spend column, so budget-driven lift cannot be ruled out at all.")
    for warning in result["coverage_warnings"]:
        print("WARNING: %s" % warning)
    return 0


if __name__ == "__main__":
    sys.exit(main())
