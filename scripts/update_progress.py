#!/usr/bin/env python3
"""Rebuild the README progress counts and local SVG progress bars from checkboxes.

The README is the source of truth; never edit generated SVGs manually.
Run: python3 scripts/update_progress.py [--check]
"""
from __future__ import annotations
import argparse
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ASSETS = ROOT / "assets" / "progress"
HEADING = re.compile(r"^### (\d+)\. (.+)$", re.M)
CHECKBOX = re.compile(r"^\s*[-*]\s+\[([ xX])\]\s+", re.M)
OVERALL = re.compile(r"\*\*Overall progress: \d+\s*/\s*\d+ topics completed \(\d+(?:\.\d+)?%\)\*\*")

def svg(done: int, total: int, label: str) -> str:
    pct = done / total * 100 if total else 0.0
    fill = round(520 * done / total, 2) if total else 0
    label = html.escape(label)
    summary = html.escape(f"{done}/{total} completed ({pct:.1f}%)")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="660" height="54" viewBox="0 0 660 54" role="img" aria-label="{label}: {summary}">
  <title>{label}: {summary}</title>
  <text x="0" y="15" font-family="Arial,sans-serif" font-size="14" fill="#57606a">{summary}</text>
  <rect x="0" y="25" width="520" height="14" rx="7" fill="#d8dee4"/>
  <rect x="0" y="25" width="{fill}" height="14" rx="7" fill="#2da44e"/>
</svg>
"""

def calculate(text: str):
    before_assessment = text.split("## Interview Readiness Assessment", 1)[0]
    headings = list(HEADING.finditer(before_assessment))
    if len(headings) != 15:
        raise ValueError(f"Expected 15 domain headings, found {len(headings)}")
    stats = []
    for i, match in enumerate(headings):
        body = before_assessment[match.end():headings[i+1].start() if i+1 < len(headings) else len(before_assessment)]
        if body.count("<details>") != 1 or body.count("</details>") != 1:
            raise ValueError(f"Invalid collapsible section for {match.group(2)}")
        states = CHECKBOX.findall(body)
        if not states:
            raise ValueError(f"No checkboxes in {match.group(2)}")
        stats.append((int(match.group(1)), match.group(2), sum(x.lower() == "x" for x in states), len(states)))
    done = sum(s[2] for s in stats)
    total = sum(s[3] for s in stats)
    if total != 829:
        raise ValueError(f"Expected 829 topics, found {total}; review changes before updating the total")
    summary = f"**Overall progress: {done} / {total} topics completed ({done / total * 100:.1f}%)**"
    updated, changes = OVERALL.subn(summary, text, count=1)
    if changes != 1:
        raise ValueError("Cannot find the overall progress line")
    results = {ASSETS / "overall.svg": svg(done,total,"Overall interview preparation")}
    for n, name, completed, count in stats:
        results[ASSETS / f"domain-{n}.svg"] = svg(completed,count,name)
    return updated, results, stats

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if any progress output is stale")
    args = parser.parse_args()
    original = README.read_text(encoding="utf-8")
    updated, files, stats = calculate(original)
    stale = original != updated or any(not p.exists() or p.read_text(encoding="utf-8") != content for p,content in files.items())
    if args.check:
        if stale:
            print("Progress assets or overall count are out of date", file=sys.stderr)
            return 1
    else:
        if updated != original:
            README.write_text(updated,encoding="utf-8")
        ASSETS.mkdir(parents=True, exist_ok=True)
        for path, content in files.items():
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                path.write_text(content,encoding="utf-8")
    print(f"Progress: {sum(x[2] for x in stats)}/{sum(x[3] for x in stats)} across {len(stats)} domains")
    return 0

if __name__ == "__main__":
    sys.exit(main())
