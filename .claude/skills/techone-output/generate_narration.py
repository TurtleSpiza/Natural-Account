#!/usr/bin/env python3
"""
generate_narration.py

Runtime that loads narration_templates.json and produces a TechOne narration
string from a category name + field values dict. Replicates the in-browser
NARR_TEMPLATES tool's output exactly, including conditional segments.

Usage as a library:
    from generate_narration import generate, list_categories, get_category

    s = generate('mowing', {
        'narr_vendor':  'Austspray',
        'narr_service': 'Zone mowing',
        'narr_zone':    'Zone 3',
        'narr_period':  'March 2026',
        'narr_po':      'PO 485102',
        'narr_svc':     '20371',
    })
    # → "Austspray — Zone mowing Zone 3 March 2026 Ref: PO 485102 Svc 20371"

CLI usage:
    python generate_narration.py <category> --field narr_vendor=Austspray ...
    python generate_narration.py --list
    python generate_narration.py --inspect mowing
"""

import sys
import json
import argparse
from pathlib import Path


_DEFAULT_TEMPLATES = Path(__file__).parent / "narration_templates.json"


def load_templates(path=None):
    p = Path(path) if path else _DEFAULT_TEMPLATES
    return json.loads(p.read_text(encoding="utf-8"))


def list_categories(templates=None):
    templates = templates or load_templates()
    return list(templates["categories"].keys())


def get_category(name, templates=None):
    templates = templates or load_templates()
    if name not in templates["categories"]:
        raise KeyError(f"Unknown category: {name!r}. Available: {list_categories(templates)}")
    return templates["categories"][name]


def render_segments(segments, field_values):
    """Walk a segment list and return the concatenated string."""
    out = []
    for seg in segments:
        if "literal" in seg:
            out.append(seg["literal"])
        elif "field" in seg:
            value = field_values.get(seg["field"], "")
            if value:
                out.append(str(value))
            elif "fallback" in seg:
                out.append(seg["fallback"])
            # else: bare field with no value and no fallback → empty string
        elif "if_field" in seg:
            value = field_values.get(seg["if_field"], "")
            if value:  # truthy, mirroring JS truthiness
                out.append(render_segments(seg["then_segments"], field_values))
        else:
            raise ValueError(f"Unknown segment type: {seg!r}")
    return "".join(out)


def generate(category, field_values, templates=None):
    """
    Produce a narration string from category + field values.

    Args:
        category: category name (e.g. 'mowing', 'maintenance', 'general')
        field_values: dict of {field_id: value}. Missing or empty-string values
                      trigger the fallback or skip the conditional segment, as
                      per the in-browser tool.
        templates: optional pre-loaded templates dict

    Returns:
        the rendered narration string
    """
    cat = get_category(category, templates)
    return render_segments(cat["template_pattern"], field_values)


def describe_category(category, templates=None):
    """Return a human-readable description of a category."""
    cat = get_category(category, templates)
    lines = []
    lines.append(f"Category: {category}")
    lines.append(f"Title:    {cat['title']}")
    lines.append(f"Account:  {cat['account'] or '(none — picked at use time)'}")
    lines.append(f"Fields ({len(cat['fields'])}):")
    for f in cat["fields"]:
        lines.append(f"  - {f['id']:<16} {f['label']:<24} {f['placeholder']}")
    # Render an empty-input example to show the fallback shape
    empty_render = render_segments(cat["template_pattern"], {})
    lines.append(f"Empty render: {empty_render}")
    return "\n".join(lines)


def _cli():
    ap = argparse.ArgumentParser(description="Generate a TechOne narration from a category template")
    ap.add_argument("category", nargs="?", help="Category name (e.g. mowing, maintenance)")
    ap.add_argument("--field", "-f", action="append", default=[],
                    help="Field value as KEY=VALUE; repeatable")
    ap.add_argument("--templates", "-t", help="Path to narration_templates.json")
    ap.add_argument("--list", "-l", action="store_true", help="List available categories")
    ap.add_argument("--inspect", "-i", help="Show category metadata")
    args = ap.parse_args()

    templates = load_templates(args.templates)

    if args.list:
        cats = list_categories(templates)
        for c in cats:
            cat = templates["categories"][c]
            print(f"{c:<14} {cat['title']:<32} account={cat['account']}")
        return

    if args.inspect:
        print(describe_category(args.inspect, templates))
        return

    if not args.category:
        ap.print_usage()
        print("Error: category required (or use --list / --inspect)", file=sys.stderr)
        sys.exit(2)

    field_values = {}
    for f in args.field:
        if "=" not in f:
            print(f"Bad --field value (need KEY=VALUE): {f!r}", file=sys.stderr)
            sys.exit(2)
        k, v = f.split("=", 1)
        field_values[k.strip()] = v

    print(generate(args.category, field_values, templates))


if __name__ == "__main__":
    _cli()
