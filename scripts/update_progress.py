
#!/usr/bin/env python3
"""Update interview preparation progress from README checklist states."""

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
EXPECTED_TOPICS = 829

HEADING = re.compile(r"^### (\d+)\. (.+)$", re.MULTILINE)

CHECKBOX = re.compile(
    r"^(?P<indent>[ \t]*)[-*]\s+\[(?P<state>[ xX])\]\s+",
    re.MULTILINE,
)

OVERALL = re.compile(
    r"\*\*Overall progress:\s*\d+\s*/\s*\d+"
    r"\s+topics completed\s*\([\d.]+%\)\*\*"
)

PROGRESS_IMAGE = re.compile(
    r"(?P<prefix>assets/progress/"
    r"(?:overall|domain-\d+)\.svg)"
    r"(?:\?v=[a-f0-9]+)?"
)


def generate_svg(done: int, total: int, label: str) -> str:
    percentage = 100 * done / total if total else 0
    fill_width = 520 * done / total if total else 0

    safe_label = html.escape(label, quote=True)
    summary = html.escape(
        f"{done}/{total} completed ({percentage:.1f}%)",
        quote=True,
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg"
     width="660" height="54" viewBox="0 0 660 54"
     role="img" aria-label="{safe_label}: {summary}">
  <title>{safe_label}: {summary}</title>
  <text x="0" y="15"
        font-family="Arial,sans-serif"
        font-size="14" fill="#57606a">{summary}</text>
  <rect x="0" y="25" width="520" height="14"
        rx="7" fill="#d8dee4"/>
  <rect x="0" y="25" width="{fill_width:.2f}" height="14"
        rx="7" fill="#2da44e"/>
</svg>
"""


def get_topic_states(body: str) -> list[bool]:
    """Count leaf-level checkboxes, not parent categories."""

    matches = list(CHECKBOX.finditer(body))

    if not matches:
        return []

    # Find deepest checklist indentation in this section.
    max_indent = max(
        len(match.group("indent").expandtabs(4))
        for match in matches
    )

    return [
        match.group("state").lower() == "x"
        for match in matches
        if len(match.group("indent").expandtabs(4)) == max_indent
    ]


def calculate(text: str):
    content = text.split(
        "## Interview Readiness Assessment", 1
    )[0]

    headings = list(HEADING.finditer(content))

    if len(headings) != EXPECTED_DOMAINS:
        raise ValueError(
            f"Expected {EXPECTED_DOMAINS} domains, "
            f"found {len(headings)}"
        )

    stats = []

    for index, heading in enumerate(headings):
        start = heading.end()

        end = (
            headings[index + 1].start()
            if index + 1 < len(headings)
            else len(content)
        )

        body = content[start:end]

        name = heading.group(2)
        domain_number = int(heading.group(1))

        if (
            body.count("<details>") != 1
            or body.count("</details>") != 1
        ):
            raise ValueError(
                f"Invalid collapsible section: {name}"
            )

        states = get_topic_states(body)

        if not states:
            raise ValueError(
                f"No leaf topics found in: {name}"
            )

        stats.append({
            "number": domain_number,
            "name": name,
            "completed": sum(states),
            "total": len(states),
        })

    completed = sum(
        domain["completed"] for domain in stats
    )

    total = sum(
        domain["total"] for domain in stats
    )

    if total != EXPECTED_TOPICS:
        raise ValueError(
            f"Expected {EXPECTED_TOPICS} leaf topics, "
            f"found {total}. "
            "Verify whether the checklist structure changed."
        )

    percentage = completed / total * 100

    summary = (
        f"**Overall progress: {completed} / {total} "
        f"topics completed ({percentage:.1f}%)**"
    )

    updated, replacements = OVERALL.subn(
        summary, text, count=1
    )

    if replacements != 1:
        raise ValueError(
            "Overall progress summary not found in README."
        )

    generated_files = {
        ASSETS / "overall.svg": generate_svg(
            completed, total,
            "Overall interview preparation"
        )
    }

    for domain in stats:
        filename = (
            ASSETS / f"domain-{domain['number']}.svg"
        )

        generated_files[filename] = generate_svg(
            domain["completed"],
            domain["total"],
            domain["name"],
        )

    # Fingerprint each SVG's content.
    # Only changes when the actual progress changes.
    versions = {
        path.name: hashlib.sha256(
            content.encode("utf-8")
        ).hexdigest()[:10]
        for path, content in generated_files.items()
    }

    def update_image_reference(match):
        original_path = match.group("prefix")
        filename = Path(original_path).name
        return (
            f"{original_path}?v={versions[filename]}"
        )

    updated = PROGRESS_IMAGE.sub(
        update_image_reference, updated
    )

    return updated, generated_files, stats


def main() -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if generated progress is out of date",
    )

    args = parser.parse_args()

    original = README.read_text(encoding="utf-8")

    updated, files, stats = calculate(original)

    stale = (
        original != updated
        or any(
            not path.exists()
            or path.read_text(encoding="utf-8") != content
            for path, content in files.items()
        )
    )

    if args.check:
        if stale:
            print(
                "Progress information is out of date.",
                file=sys.stderr,
            )
            return 1

    else:
        if updated != original:
            README.write_text(
                updated, encoding="utf-8"
            )

        ASSETS.mkdir(
            parents=True, exist_ok=True
        )

        for path, content in files.items():
            if (
                not path.exists()
                or path.read_text(encoding="utf-8")
                != content
            ):
                path.write_text(
                    content, encoding="utf-8"
                )

    completed = sum(
        domain["completed"] for domain in stats
    )

    total = sum(
        domain["total"] for domain in stats
    )

    print(
        f"Overall progress: {completed}/{total} "
        f"({completed / total * 100:.1f}%)"
    )

    for domain in stats:
        print(
            f"Domain {domain['number']}: "
            f"{domain['completed']}/{domain['total']} "
            f"- {domain['name']}"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
