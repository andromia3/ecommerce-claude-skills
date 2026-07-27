#!/usr/bin/env python3
"""Score a whole product catalog for content gaps.

Used by: catalog-content-audit-ecommerce

Why this exists: this is the one skill in the pack that breaks at scale. A model
handed an 800-row catalog export reads the rows it happens to attend to and then
reports that as catalog coverage. The percentages come out confident and wrong.
Counting is mechanical, so it belongs in a script; the judgement about what to
fix first stays in the skill.

Input: one CSV with a row per product.

  sku or handle                  required
  title                          required
  description                    optional but this is the point
  category or product type       optional, gaps cluster by category
  images or image count          optional
  revenue and sessions           optional, used to weight the queue commercially
  gtin, brand, mpn, size, colour, material   optional, checked if present

A Shopify-style export with one row per variant is collapsed to one record per
handle before anything is counted, keeping the first non-empty value of each
field, the highest image count and the longest description. Without that,
continuation rows inflate the product count and every one reads as an empty
description, and a product's image count is taken from whichever row came first.

Duplicate detection is exact-match on a normalised description, which is what
catches supplier copy pasted across every reseller. Near-duplicate detection is
deliberately not attempted here: a wrong fuzzy match is worse than none.

usage:
  python3 scripts/catalog_scan.py catalog.csv
  python3 scripts/catalog_scan.py catalog.csv --thin-words 40 --json

exit 0 = ran, 2 = could not run.
"""
import argparse
import csv
import hashlib
import json
import re
import sys

ALIASES = {
    "sku": ["sku", "handle", "variant sku", "product id", "id"],
    "title": ["title", "name", "product title", "product name"],
    "description": ["description", "body html", "body (html)", "product description", "content"],
    "category": ["category", "product type", "type", "product category", "collection"],
    "images": ["images", "image count", "image src", "images count", "number of images"],
    "revenue": ["revenue", "net sales", "total sales", "sales"],
    "sessions": ["sessions", "visits", "pageviews", "views"],
}
ATTRIBUTES = ["gtin", "barcode", "brand", "mpn", "size", "colour", "color", "material", "age group", "condition"]


def norm(s):
    return " ".join(str(s or "").strip().lower().replace("_", " ").split())


def strip_html(s):
    return re.sub(r"<[^>]+>", " ", str(s or ""))


def words(s):
    return len([w for w in re.split(r"\s+", strip_html(s).strip()) if w])


def money(raw):
    s = str(raw or "").strip()
    for ch in "()$£€ ,":
        s = s.replace(ch, "")
    try:
        return float(s)
    except ValueError:
        return 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path")
    ap.add_argument("--thin-words", type=int, default=40,
                    help="descriptions under this word count count as thin (default 40)")
    ap.add_argument("--min-images", type=int, default=3)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

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
    attr_cols = {a: header[a] for a in ATTRIBUTES if a in header}

    if "sku" not in cm or "title" not in cm:
        print("missing required columns: sku/handle and title", file=sys.stderr)
        print("columns found: %s" % ", ".join(rows[0].keys()), file=sys.stderr)
        return 2

    # Shopify's native product export writes one row per VARIANT and per extra
    # image, with title and description populated only on the first row of each
    # handle. Treating those continuation rows as products would report a
    # catalog several times its real size and count every continuation row as an
    # empty description. Collapse to one record per sku/handle first, keeping
    # the first non-empty value of each field and the highest image count.
    merged = {}
    order = []
    for raw in rows:
        key = str(raw.get(cm["sku"], "")).strip()
        if not key:
            continue
        if key not in merged:
            merged[key] = dict(raw)
            order.append(key)
            continue
        target = merged[key]
        for col, val in raw.items():
            sval = str(val or "").strip()
            if not sval:
                continue
            existing = str(target.get(col) or "").strip()
            if not existing:
                target[col] = val
            elif cm.get("images") and col == cm["images"]:
                # variant rows carry different image counts; the product has the
                # highest of them, not whichever row happened to come first
                try:
                    if float(sval) > float(existing):
                        target[col] = val
                except ValueError:
                    pass
            elif cm.get("description") and col == cm["description"] and len(sval) > len(existing):
                target[col] = val
    collapsed = len(rows) - len(merged)
    rows = [merged[k] for k in order]

    products = []
    desc_hashes = {}
    for row in rows:
        sku = str(row.get(cm["sku"], "")).strip()
        if not sku:
            continue
        desc = row.get(cm.get("description", ""), "") if cm.get("description") else ""
        wc = words(desc)
        flat = norm(strip_html(desc))
        dhash = hashlib.sha1(flat.encode("utf-8")).hexdigest() if flat else None
        if dhash:
            desc_hashes.setdefault(dhash, []).append(sku)

        img_raw = row.get(cm.get("images", ""), "") if cm.get("images") else ""
        try:
            images = int(float(str(img_raw).strip() or 0))
        except ValueError:
            images = len([p for p in str(img_raw).split(",") if p.strip()])

        missing_attrs = []
        for attr, col in attr_cols.items():
            if not str(row.get(col, "")).strip():
                missing_attrs.append(attr)

        products.append({
            "sku": sku,
            "title": str(row.get(cm["title"], "")).strip(),
            "category": str(row.get(cm.get("category", ""), "")).strip() or "(uncategorised)" if cm.get("category") else "(uncategorised)",
            "words": wc,
            "thin": wc < args.thin_words,
            "empty": wc == 0,
            "images": images,
            "image_gap": images < args.min_images if cm.get("images") else None,
            "missing_attributes": missing_attrs,
            "revenue": money(row.get(cm.get("revenue", ""), "")) if cm.get("revenue") else 0.0,
            "sessions": money(row.get(cm.get("sessions", ""), "")) if cm.get("sessions") else 0.0,
            "desc_hash": dhash,
        })

    dupes = {h: skus for h, skus in desc_hashes.items() if len(skus) > 1}
    duped_skus = {s for skus in dupes.values() for s in skus}

    by_cat = {}
    for p in products:
        c = by_cat.setdefault(p["category"], {
            "products": 0, "thin": 0, "empty": 0, "image_gap": 0,
            "missing_attr_products": 0, "duplicate": 0, "revenue": 0.0})
        c["products"] += 1
        c["thin"] += 1 if p["thin"] else 0
        c["empty"] += 1 if p["empty"] else 0
        c["image_gap"] += 1 if p["image_gap"] else 0
        c["missing_attr_products"] += 1 if p["missing_attributes"] else 0
        c["duplicate"] += 1 if p["sku"] in duped_skus else 0
        c["revenue"] += p["revenue"]

    attr_gap_counts = {}
    for attr in attr_cols:
        attr_gap_counts[attr] = sum(1 for p in products if attr in p["missing_attributes"])

    def defect_score(p):
        return ((1 if p["empty"] else 0) * 3 + (1 if p["thin"] else 0) * 2
                + (1 if p["sku"] in duped_skus else 0) * 2
                + (1 if p["image_gap"] else 0) + len(p["missing_attributes"]))

    queue = sorted((p for p in products if defect_score(p) > 0),
                   key=lambda p: (-p["revenue"], -defect_score(p)))

    summary = {
        "products": len(products),
        "attributes_checked": sorted(attr_cols.keys()) or ["none present in export"],
        "thin_descriptions": sum(1 for p in products if p["thin"]),
        "empty_descriptions": sum(1 for p in products if p["empty"]),
        "duplicate_description_products": len(duped_skus),
        "duplicate_description_clusters": len(dupes),
        "products_missing_attributes": sum(1 for p in products if p["missing_attributes"]),
        "attribute_gap_counts": attr_gap_counts,
        "revenue_column_present": bool(cm.get("revenue")),
        "variant_rows_collapsed": collapsed,
    }

    if args.json:
        print(json.dumps({
            "summary": summary,
            "by_category": by_cat,
            "work_queue_top50": queue[:50],
            "duplicate_clusters": [{"skus": s} for s in list(dupes.values())[:50]],
        }, indent=2))
        return 0

    print("products: %d   thin: %d   empty: %d   duplicate copy: %d products in %d clusters"
          % (summary["products"], summary["thin_descriptions"], summary["empty_descriptions"],
             summary["duplicate_description_products"], summary["duplicate_description_clusters"]))
    if collapsed:
        print("NOTE: %d continuation rows (extra variants/images sharing a handle) "
              "collapsed into their parent product." % collapsed)
    print("attributes checked: %s" % ", ".join(summary["attributes_checked"]))
    if attr_gap_counts:
        print("attribute gaps: %s"
              % ", ".join("%s=%d" % (a, n) for a, n in sorted(attr_gap_counts.items(), key=lambda x: -x[1]) if n))
    if not summary["revenue_column_present"]:
        print("NOTE: no revenue column, so the work queue is not commercially weighted.")
    print()
    print("%-28s %9s %7s %7s %7s %10s %12s"
          % ("category", "products", "thin", "empty", "dupes", "img_gap", "revenue"))
    for cat, c in sorted(by_cat.items(), key=lambda kv: -kv[1]["revenue"]):
        print("%-28s %9d %7d %7d %7d %10d %12.2f"
              % (cat[:28], c["products"], c["thin"], c["empty"], c["duplicate"],
                 c["image_gap"], c["revenue"]))
    print()
    print("top of the work queue (revenue first):")
    for p in queue[:15]:
        flags = []
        if p["empty"]:
            flags.append("empty")
        elif p["thin"]:
            flags.append("thin(%dw)" % p["words"])
        if p["sku"] in duped_skus:
            flags.append("duplicate")
        if p["image_gap"]:
            flags.append("images=%d" % p["images"])
        if p["missing_attributes"]:
            flags.append("missing:" + ",".join(p["missing_attributes"][:3]))
        print("  %-22s %10.2f  %s" % (p["sku"][:22], p["revenue"], " ".join(flags)))
    if len(queue) > 15:
        print("  ... %d more, use --json for the full queue" % (len(queue) - 15))
    return 0


if __name__ == "__main__":
    sys.exit(main())
