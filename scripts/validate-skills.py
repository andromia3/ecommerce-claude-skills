#!/usr/bin/env python3
"""Validate every SKILL.md in this pack.

Run before shipping any change to the pack:

    python3 scripts/validate-skills.py
    python3 scripts/validate-skills.py --selftest

Checks, each of which exists because it caught something real:

- required sections present, using THIS pack's section names
- an activation phrase ("Use when") in the frontmatter description, because
  three skills shipped without one and were less likely to trigger
- at least 5 analysis steps
- no placeholder or templated filler text
- enough substance to be worth installing
- guardrails section actually contains prohibitions
- the evidence vocabulary a skill uses is declared in references/output-standard.md,
  so a skill cannot quietly invent a tag nothing else understands

exit 0 = PASS, 1 = FAIL.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_SECTIONS = [
    "## Use this skill when",
    "## Required input",
    "## Analysis workflow",
    "## Decision and evidence standard",
    "## Output format",
    "## Guardrails",
]
# either spelling of the worked-example section is accepted
EXAMPLE_SECTIONS = ["## Example input and output", "## Practical example"]

PLACEHOLDERS = ["Add the inputs", "Step one", "Step two", "Step three",
                "Column 1", "Column 2", "TODO", "TBD", "Lorem ipsum", "XXX"]
TEMPLATED_PHRASES = [
    "diagnosing, planning, reviewing",
    "asks for help with",
    "provides data, screenshots",
    "needs an approval-ready diagnosis",
    "Can you check this",
]
MIN_WORDS = 280
MIN_STEPS = 5


def section(text, heading):
    match = re.search(rf"^## {re.escape(heading)}\n(.*?)(?=\n## |\Z)", text, re.S | re.M)
    return match.group(1).strip() if match else ""


def known_tags():
    std = ROOT / "references" / "output-standard.md"
    if not std.exists():
        return None
    return set(re.findall(r"`([a-z_]+)`", std.read_text(encoding="utf-8")))


def check(text, rel, tags):
    errors = []
    for token in PLACEHOLDERS:
        if token in text:
            errors.append(f"{rel}: placeholder token: {token}")
    for phrase in TEMPLATED_PHRASES:
        if phrase in text:
            errors.append(f"{rel}: templated phrase: {phrase}")
    for heading in REQUIRED_SECTIONS:
        if heading not in text:
            errors.append(f"{rel}: missing section: {heading}")
    if not any(h in text for h in EXAMPLE_SECTIONS):
        errors.append(f"{rel}: missing a worked example section ({' or '.join(EXAMPLE_SECTIONS)})")

    frontmatter = text.split("---", 2)[1] if text.startswith("---") and text.count("---") >= 2 else ""
    name = next((l for l in frontmatter.splitlines() if l.startswith("name:")), "")
    description = next((l for l in frontmatter.splitlines() if l.startswith("description:")), "")
    if not name.strip():
        errors.append(f"{rel}: frontmatter has no name")
    if "Use when" not in description:
        errors.append(f"{rel}: description needs an activation phrase containing 'Use when'")
    if len(description) > 1024:
        errors.append(f"{rel}: description over 1024 chars, it will be truncated")

    steps = re.findall(r"^\d+\.\s+", section(text, "Analysis workflow"), re.M)
    if len(steps) < MIN_STEPS:
        errors.append(f"{rel}: analysis workflow has {len(steps)} steps, needs at least {MIN_STEPS}")

    guardrails = section(text, "Guardrails")
    if guardrails.count("Do not") < 3:
        errors.append(f"{rel}: guardrails should state at least 3 prohibitions")

    if len(text.split()) < MIN_WORDS:
        errors.append(f"{rel}: too short to be useful ({len(text.split())} words)")

    if tags is not None:
        used = set(re.findall(r"`([a-z_]+)`", section(text, "Decision and evidence standard")))
        unknown = {t for t in used if t not in tags and "_" in t}
        for tag in sorted(unknown):
            errors.append(f"{rel}: evidence tag `{tag}` is not declared in references/output-standard.md")
    return errors


def selftest():
    """Prove the checks fail on the defects they were written for."""
    good = (ROOT / "contribution-margin-check-ecommerce" / "SKILL.md").read_text(encoding="utf-8")
    cases = [
        ("no activation phrase", good.replace("Use when", "Use for", 1), "activation phrase"),
        ("thin workflow", re.sub(r"^\d+\.\s+.*$", "", good, count=8, flags=re.M), "analysis workflow"),
        ("placeholder left in", good.replace("Confirm the period", "TODO Confirm the period", 1), "placeholder"),
        ("undeclared evidence tag", good.replace("`payout_report`", "`vibes_export`", 1), "not declared"),
    ]
    failures = []
    for label, mutated, expect in cases:
        errs = check(mutated, "selftest", known_tags())
        if not any(expect in e for e in errs):
            failures.append(f"selftest: '{label}' was NOT caught (expected an error mentioning '{expect}')")
    if check(good, "selftest", known_tags()):
        failures.append("selftest: the unmodified skill failed validation")
    if failures:
        print("\n".join(failures))
        return 1
    print("OK: selftest passed, every check catches the defect it exists for")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()

    tags = known_tags()
    if tags is None:
        print("WARNING: references/output-standard.md not found, skipping evidence tag check")

    errors = []
    count = 0
    for path in sorted(ROOT.glob("*/SKILL.md")):
        count += 1
        errors.extend(check(path.read_text(encoding="utf-8"), path.relative_to(ROOT), tags))

    if not count:
        print("no SKILL.md found under %s" % ROOT)
        return 1
    if errors:
        print("\n".join(errors))
        print("\nFAIL: %d problems across %d skills" % (len(errors), count))
        return 1
    print("OK: %d skills passed validation" % count)
    return 0


if __name__ == "__main__":
    sys.exit(main())
