#!/usr/bin/env python3
"""
extract_narr_templates.py

Parse NARR_TEMPLATES from LCC_AP_Coding_Review_v*.html into a structured
JSON. JS arrow-function template literals don't parse as JSON5, so this is
a custom extractor: regex + brace-counting + arrow-function-body parser.

Usage:
    python extract_narr_templates.py <input.html> [--output narration_templates.json]

If --output is omitted, prints to stdout.

The output JSON has the schema documented in narration_templates.json
"_meta._template_pattern_format".
"""

import sys
import re
import json
import argparse
from pathlib import Path


def extract_narr_block(html: str) -> str:
    """Locate `const NARR_TEMPLATES = {` and return the matching {...} body."""
    start_match = re.search(r"const\s+NARR_TEMPLATES\s*=\s*\{", html)
    if not start_match:
        raise ValueError("Could not find 'const NARR_TEMPLATES = {' in input")
    start = start_match.end() - 1  # position of opening brace
    depth = 0
    in_string = False
    string_char = None
    in_template = False
    i = start
    while i < len(html):
        c = html[i]
        if in_string:
            if c == "\\":
                i += 2
                continue
            if c == string_char:
                in_string = False
            i += 1
            continue
        if in_template:
            if c == "\\":
                i += 2
                continue
            if c == "`":
                in_template = False
            i += 1
            continue
        if c == '"' or c == "'":
            in_string = True
            string_char = c
            i += 1
            continue
        if c == "`":
            in_template = True
            i += 1
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return html[start:i+1]
        i += 1
    raise ValueError("Unmatched braces in NARR_TEMPLATES block")


def split_categories(block_body: str) -> dict:
    """Return {category_name: category_body_string} for the top-level entries."""
    # block_body is like "{ name1: { ... }, name2: { ... }, ... }"
    # Strip outer braces
    inner = block_body[1:-1].strip()
    result = {}
    i = 0
    while i < len(inner):
        # Skip whitespace and commas
        while i < len(inner) and inner[i] in " \t\n,":
            i += 1
        if i >= len(inner):
            break
        # Read category name (alphanumeric)
        name_match = re.match(r"([A-Za-z_][A-Za-z0-9_]*)\s*:\s*", inner[i:])
        if not name_match:
            raise ValueError(f"Expected category name at offset {i}: {inner[i:i+40]!r}")
        name = name_match.group(1)
        i += name_match.end()
        # Expect '{' for the category body
        if i >= len(inner) or inner[i] != "{":
            raise ValueError(f"Expected {{ after {name}: at offset {i}")
        # Find matching brace
        body_start = i
        depth = 0
        in_string = False
        string_char = None
        in_template = False
        while i < len(inner):
            c = inner[i]
            if in_string:
                if c == "\\":
                    i += 2
                    continue
                if c == string_char:
                    in_string = False
            elif in_template:
                if c == "\\":
                    i += 2
                    continue
                if c == "`":
                    in_template = False
            elif c == '"' or c == "'":
                in_string = True
                string_char = c
            elif c == "`":
                in_template = True
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    body = inner[body_start:i+1]
                    result[name] = body
                    i += 1
                    break
            i += 1
        else:
            raise ValueError(f"Unmatched brace in category {name}")
    return result


def parse_field_array(s: str) -> list:
    """Parse a JS array of field objects into Python list of dicts."""
    # Each entry is `{id:'...', label:'...', placeholder:'...'}`
    # Strip outer brackets and split on top-level commas
    s = s.strip()
    if not (s.startswith("[") and s.endswith("]")):
        raise ValueError("Field array doesn't start/end with []")
    inner = s[1:-1]
    fields = []
    depth = 0
    in_string = False
    string_char = None
    start = 0
    i = 0
    while i < len(inner):
        c = inner[i]
        if in_string:
            if c == "\\":
                i += 2
                continue
            if c == string_char:
                in_string = False
        elif c == '"' or c == "'":
            in_string = True
            string_char = c
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        elif c == "," and depth == 0:
            entry = inner[start:i].strip()
            if entry:
                fields.append(parse_field_object(entry))
            start = i + 1
        i += 1
    tail = inner[start:].strip()
    if tail:
        fields.append(parse_field_object(tail))
    return fields


def parse_field_object(s: str) -> dict:
    """Parse `{id:'...', label:'...', placeholder:'...'}` into a Python dict."""
    s = s.strip()
    if not (s.startswith("{") and s.endswith("}")):
        raise ValueError(f"Field object doesn't start/end with {{}}: {s!r}")
    inner = s[1:-1]
    result = {}
    # Match key:'value' pairs separated by commas, with care for commas inside strings
    pattern = re.compile(
        r"\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*'((?:[^'\\]|\\.)*)'\s*(?:,|$)"
    )
    for m in pattern.finditer(inner):
        key = m.group(1)
        val = m.group(2).encode().decode("unicode_escape")
        result[key] = val
    return result


def extract_arrow_body(category_body: str) -> str:
    """Extract the body string of `template: (f) => \`...\``."""
    # Find `template: (f) => `
    m = re.search(
        r"template\s*:\s*\(\s*[A-Za-z_][A-Za-z0-9_]*\s*\)\s*=>\s*`",
        category_body,
    )
    if not m:
        raise ValueError("Could not find template arrow function")
    start = m.end()  # one past the opening backtick
    # Find the matching closing backtick (not preceded by backslash)
    i = start
    while i < len(category_body):
        c = category_body[i]
        if c == "\\":
            i += 2
            continue
        if c == "`":
            return category_body[start:i]
        i += 1
    raise ValueError("Unterminated template literal")


def parse_template_body(body: str) -> list:
    """
    Parse a JS template-literal body into a list of segments.

    Segment types:
      {"literal": "..."}
      {"field": "narr_X", "fallback": "[...]"}     (from `${f.narr_X||'[...]'}`)
      {"field": "narr_X"}                          (from `${f.narr_X}`)
      {"if_field": "narr_X", "then_segments": [...]}  (from `${f.narr_X?' Ref: '+f.narr_X:''}`)
    """
    segments = []
    i = 0
    while i < len(body):
        # Find next ${...}
        dollar_idx = body.find("${", i)
        if dollar_idx == -1:
            # Rest is literal
            tail = body[i:]
            if tail:
                segments.append({"literal": tail})
            break
        # Literal up to ${
        if dollar_idx > i:
            segments.append({"literal": body[i:dollar_idx]})
        # Find matching `}` for `${`
        depth = 1
        j = dollar_idx + 2
        in_string = False
        string_char = None
        while j < len(body) and depth > 0:
            c = body[j]
            if in_string:
                if c == "\\":
                    j += 2
                    continue
                if c == string_char:
                    in_string = False
            elif c == '"' or c == "'":
                in_string = True
                string_char = c
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            j += 1
        expr = body[dollar_idx+2:j-1]
        segments.append(parse_expr(expr))
        i = j
    return segments


def parse_expr(expr: str) -> dict:
    """
    Parse a single ${...} expression into a segment dict.

    Patterns:
      f.narr_X                              → {"field": "narr_X"}
      f.narr_X||'[Fallback]'                → {"field": "narr_X", "fallback": "[Fallback]"}
      f.narr_X?' Ref: '+f.narr_X:''         → {"if_field": "narr_X", "then_segments": [...]}
    """
    expr = expr.strip()
    # Pattern: ternary  f.X ? truthy : falsy
    tern = re.match(
        r"^[A-Za-z_]\w*\.([A-Za-z_]\w*)\s*\?\s*(.+?)\s*:\s*(.+?)\s*$",
        expr,
        re.DOTALL,
    )
    if tern:
        field = tern.group(1)
        truthy = tern.group(2).strip()
        falsy = tern.group(3).strip()
        # Falsy should be empty string (typically '')
        if falsy not in ("''", '""'):
            raise ValueError(f"Unexpected ternary falsy branch: {falsy!r}")
        # Truthy is a series of `'literal'+f.X` concatenations
        then_segments = parse_concat_chain(truthy)
        return {"if_field": field, "then_segments": then_segments}
    # Pattern: field with fallback  f.X||'[F]'
    fb = re.match(
        r"^[A-Za-z_]\w*\.([A-Za-z_]\w*)\s*\|\|\s*'((?:[^'\\]|\\.)*)'$",
        expr,
    )
    if fb:
        return {
            "field": fb.group(1),
            "fallback": fb.group(2).encode().decode("unicode_escape"),
        }
    # Pattern: bare field  f.X
    bare = re.match(r"^[A-Za-z_]\w*\.([A-Za-z_]\w*)$", expr)
    if bare:
        return {"field": bare.group(1)}
    raise ValueError(f"Unrecognised template expression: {expr!r}")


def parse_concat_chain(s: str) -> list:
    """
    Parse a string-concat chain like  ' Ref: '+f.narr_po
    into a list of segments.
    """
    segments = []
    parts = []
    depth = 0
    in_string = False
    string_char = None
    start = 0
    i = 0
    while i < len(s):
        c = s[i]
        if in_string:
            if c == "\\":
                i += 2
                continue
            if c == string_char:
                in_string = False
        elif c == '"' or c == "'":
            in_string = True
            string_char = c
        elif c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
        elif c == "+" and depth == 0:
            parts.append(s[start:i].strip())
            start = i + 1
        i += 1
    parts.append(s[start:].strip())
    for part in parts:
        if not part:
            continue
        # Literal
        if (part.startswith("'") and part.endswith("'")) or \
           (part.startswith('"') and part.endswith('"')):
            lit = part[1:-1].encode().decode("unicode_escape")
            segments.append({"literal": lit})
            continue
        # Field reference  f.X
        m = re.match(r"^[A-Za-z_]\w*\.([A-Za-z_]\w*)$", part)
        if m:
            segments.append({"field": m.group(1)})
            continue
        raise ValueError(f"Unrecognised concat part: {part!r}")
    return segments


def parse_account(category_body: str):
    """Extract the `account: '...' | null` value."""
    m = re.search(r"account\s*:\s*('([^']*)'|null)", category_body)
    if not m:
        raise ValueError("Could not find account field")
    if m.group(1) == "null":
        return None
    return m.group(2)


def parse_title(category_body: str) -> str:
    m = re.search(r"title\s*:\s*'((?:[^'\\]|\\.)*)'", category_body)
    if not m:
        raise ValueError("Could not find title field")
    return m.group(1).encode().decode("unicode_escape")


def parse_fields(category_body: str) -> list:
    m = re.search(r"fields\s*:\s*(\[.*?\])\s*,\s*account", category_body, re.DOTALL)
    if not m:
        raise ValueError("Could not find fields array")
    return parse_field_array(m.group(1))


def main():
    ap = argparse.ArgumentParser(description="Extract NARR_TEMPLATES from AP Coding Review HTML")
    ap.add_argument("input_html", help="Path to LCC_AP_Coding_Review_v*.html")
    ap.add_argument("--output", "-o", help="Output JSON path (default: stdout)")
    args = ap.parse_args()

    html = Path(args.input_html).read_text(encoding="utf-8")
    block = extract_narr_block(html)
    categories = split_categories(block)
    result = {
        "_meta": {
            "extracted_from": str(Path(args.input_html).name),
            "category_count": len(categories),
            "extractor_version": "1.0",
            "_template_pattern_format": (
                "Each pattern is an ordered list of segments. Each segment is one "
                "of: {literal: '...'}, {field: 'narr_X', fallback: '[Contractor]'}, "
                "or {if_field: 'narr_po', then_segments: [...]}. The runtime walks "
                "segments and concatenates."
            ),
        },
        "categories": {},
    }
    for name, body in categories.items():
        try:
            arrow_body = extract_arrow_body(body)
            pattern = parse_template_body(arrow_body)
            result["categories"][name] = {
                "title": parse_title(body),
                "account": parse_account(body),
                "fields": parse_fields(body),
                "template_pattern": pattern,
            }
        except Exception as e:
            print(f"Failed to parse category '{name}': {e}", file=sys.stderr)
            raise

    out_json = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        Path(args.output).write_text(out_json, encoding="utf-8")
        print(f"Wrote {len(result['categories'])} categories to {args.output}")
    else:
        print(out_json)


if __name__ == "__main__":
    main()
