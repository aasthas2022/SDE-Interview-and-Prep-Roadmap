
#!/usr/bin/env python3
"""Regenerate README progress summary and SVG bars from leaf checklist items.

Usage:
    python3 scripts/update_progress.py
    python3 scripts/update_progress.py --check

A checkbox is a parent when the immediately following checkbox is more deeply
indented. Only leaf checkboxes count as study topics. The README is the source
of truth; generated SVGs should not be edited manually.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ASSETS = ROOT / "assets" / "progress"

EXPECTED_DOMAINS = 15

# Set to an integer after verifying the actual leaf count in your README.
EXPECTED_TOPICS: int | None = None

HEADING = re.compile(
    r"^###\s+(\d+)\.\s+(.+?)\s*$",
    re.MULTILINE,
)

CHECKBOX = re.compile(
    r"^(?P<indent>[ \t]*)[-*]\s+\[(?P<state>[ xX])\]\s+",
    re.MULTILINE,
)

OVERALL = re.compile(
    r"\*\*Overall progress:\s*\d+\s*/\s*\d+"
    r"\s+topics completed\s*\(\d+(?:\.\d+)?%\)\*\*"
)

PROGRESS_IMAGE = re.compile(
    r"(?P<path>(?:\./)?assets/progress/"
    r"(?P<name>overall|domain-\d+)\.svg)"
    r"(?:\?v=[a-fA-F0-9]+)?"
)


def svg(done: int, total: int, label: str) -> str:
    """Generate a progress bar SVG."""

    percentage = done / total * 100 if total else 0.0
    width = 520 * done / total if total else 0.0

    safe_label = html.escape(label, quote=True)

    summary = html.escape(
        f"{done}/{total} completed ({percentage:.1f}%)",
        quote=True,
    )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="660" height="54" viewBox="0 0 660 54" role="img" aria-label="{safe_label}: {summary}">
  <title>{safe_label}: {summary}</title>
  <text x="0" y="15" font-family="Arial,sans-serif" font-size="14" fill="#57606a">{summary}</text>
  <rect x="0" y="25" width="520" height="14" rx="7" fill="#d8dee4"/>
  <rect x="0" y="25" width="{width:.2f}" height="14" rx="7" fill="#2da44e"/>
</svg>
'''


def leaf_states(section: str) -> list[bool]:
    """Find leaf checkbox states, even with varying nesting depth."""

    matches = list(CHECKBOX.finditer(section))
    results: list[bool] = []

    for index, match in enumerate(matches):

        indent = len(
            match.group("indent").expandtabs(4)
        )

        # A checkbox is a parent if the following checkbox
        # is nested more deeply than the current one.
        next_is_child = (
            index + 1 < len(matches)
            and len(
                matches[index + 1]
                .group("indent")
                .expandtabs(4)
            ) > indent
        )

        # Count only individual topics, not parent categories.
        if not next_is_child:
            results.append(
                match.group("state").lower() == "x"
            )

    return results


def calculate(
    text: str,
) -> tuple[
    str,
    dict[Path, str],
    list[tuple[int, str, int, int]],
]:
    """Calculate progress for all domains and generate new outputs."""

    # Exclude interview readiness self-assessment.
    before_assessment = text.split(
        "## Interview Readiness Assessment", 1
    )[0]

    headings = list(
        HEADING.finditer(before_assessment)
    )

    if len(headings) != EXPECTED_DOMAINS:
        raise ValueError(
            f"Expected {EXPECTED_DOMAINS} domain headings, "
            f"found {len(headings)}"
        )

    stats: list[tuple[int, str, int, int]] = []

    for index, match in enumerate(headings):

        boundary = (
            headings[index + 1].start()
            if index + 1 < len(headings)
            else len(before_assessment)
        )

        body = before_assessment[
            match.end():boundary
        ]

        domain_number = int(match.group(1))
        domain_name = match.group(2)

        # Validate collapsible checklist structure.
        if (
            body.count("<details>") != 1
            or body.count("</details>") != 1
        ):
            raise ValueError(
                "Expected one collapsible checklist in domain "
                f"{domain_name}"
            )

        states = leaf_states(body)

        if not states:
            raise ValueError(
                f"No leaf checkbox topics in domain {domain_name}"
            )

        completed = sum(states)
        total = len(states)

        stats.append(
            (
                domain_number,
                domain_name,
                completed,
                total,
            )
        )

    # Calculate overall progress.
    done = sum(
        record[2] for record in stats
    )

    total = sum(
        record[3] for record in stats
    )

    if (
        EXPECTED_TOPICS is not None
        and total != EXPECTED_TOPICS
    ):
        raise ValueError(
            f"Expected {EXPECTED_TOPICS} leaf topics; "
            f"found {total}"
        )

    percentage = done / total * 100

    summary = (
        f"**Overall progress: {done} / {total} "
        f"topics completed ({percentage:.1f}%)**"
    )

    # Update overall progress text.
    updated, changed = OVERALL.subn(
        lambda _: summary,
        text,
        count=1,
    )

    if changed != 1:
        raise ValueError(
            "Cannot locate the "
            "**Overall progress: ...** summary"
        )

    # Generate overall SVG.
    outputs = {
        ASSETS / "overall.svg": svg(
            done,
            total,
            "Overall interview preparation",
        )
    }

    # Generate one SVG per domain.
    for number, name, completed, count in stats:

        outputs[
            ASSETS / f"domain-{number}.svg"
        ] = svg(
            completed,
            count,
            name,
        )

    # Create stable image versions based on SVG contents.
    # Changes only when progress actually changes.
    versions = {
        path.stem: hashlib.sha256(
            content.encode("utf-8")
        ).hexdigest()[:10]
        for path, content in outputs.items()
    }

    # Prevent GitHub from displaying cached SVGs.
    def cache_bust(match: re.Match[str]) -> str:
        return (
            f"{match.group('path')}"
            f"?v={versions[match.group('name')]}"
        )

    updated = PROGRESS_IMAGE.sub(
        cache_bust,
        updated,
    )

    return updated, outputs, stats


def main() -> int:

    parser = argparse.ArgumentParser(
        description=__doc__
    )

    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if generated files are stale",
    )

    args = parser.parse_args()

    original = README.read_text(
        encoding="utf-8"
    )

    updated, outputs, stats = calculate(
        original
    )

    # Determine whether anything needs updating.
    stale = (
        updated != original
        or any(
            not path.exists()
            or path.read_text(encoding="utf-8")
            != content
            for path, content in outputs.items()
        )
    )

    if args.check:
        if stale:
            print(
                "Progress summary or SVG files are out of date",
                file=sys.stderr,
            )
            return 1

    else:

        # Update README only when necessary.
        if updated != original:
            README.write_text(
                updated,
                encoding="utf-8",
            )

        ASSETS.mkdir(
            parents=True,
            exist_ok=True,
        )

        # Regenerate SVG files.
        for path, content in outputs.items():

            if (
                not path.exists()
                or path.read_text(encoding="utf-8")
                != content
            ):
                path.write_text(
                    content,
                    encoding="utf-8",
                )

    # Log progress for debugging in GitHub Actions.
    done = sum(
        record[2] for record in stats
    )

    total = sum(
        record[3] for record in stats
    )

    print(
        f"Overall: {done}/{total} "
        f"({done / total * 100:.1f}%)"
    )

    for number, name, completed, count in stats:
        print(
            f"Domain {number}: "
            f"{completed}/{count} - {name}"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
