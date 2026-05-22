#!/usr/bin/env python3
"""Validate a glossary JSON file against the SHF glossary schema.

Usage:
  python docs/hypercompute/validate_glossary.py
  python docs/hypercompute/validate_glossary.py --schema docs/hypercompute/glossary.schema.json --glossary docs/hypercompute/glossary.v1.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate glossary JSON against glossary schema.")
    parser.add_argument(
        "--schema",
        default="docs/hypercompute/glossary.schema.json",
        help="Path to glossary schema JSON file.",
    )
    parser.add_argument(
        "--glossary",
        default="docs/hypercompute/glossary.v1.json",
        help="Path to glossary JSON file.",
    )
    return parser.parse_args()


def load_json(path: Path) -> object:
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate(schema_path: Path, glossary_path: Path) -> int:
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        print(
            "ERROR: Missing dependency 'jsonschema'. Install it with: pip install jsonschema",
            file=sys.stderr,
        )
        return 2

    try:
        schema = load_json(schema_path)
        glossary = load_json(glossary_path)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(glossary), key=lambda e: list(e.absolute_path))

    if not errors:
        print(
            f"PASS: {glossary_path} is valid against {schema_path}",
            file=sys.stdout,
        )
        return 0

    print(
        f"FAIL: {len(errors)} validation error(s) in {glossary_path} against {schema_path}",
        file=sys.stderr,
    )
    for index, err in enumerate(errors, start=1):
        path = ".".join(str(p) for p in err.absolute_path) or "<root>"
        print(f"  {index}. path={path} :: {err.message}", file=sys.stderr)
    return 1


def main() -> int:
    args = parse_args()
    return validate(Path(args.schema), Path(args.glossary))


if __name__ == "__main__":
    raise SystemExit(main())
