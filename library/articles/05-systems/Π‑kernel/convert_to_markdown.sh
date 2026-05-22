#!/usr/bin/env bash
set -euo pipefail

SRC_DIR=${1:-.}
OUT_DIR=${2:-./markdown}

if [ -e "$OUT_DIR" ] && [ ! -d "$OUT_DIR" ]; then
  echo "Error: Output directory '$OUT_DIR' exists but is not a directory." >&2
  exit 1
fi
mkdir -p "$OUT_DIR"
shopt -s nullglob

# Dependency checks
need() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "Missing dependency: $1"
    exit 1
  }
}

need pandoc
need pdftotext

echo "Source: $SRC_DIR"
echo "Output: $OUT_DIR"
echo

# DOCX → MD
for f in "$SRC_DIR"/*.[dD][oO][cC][xX]; do
  [ -e "$f" ] || continue
  name=${f##*/}
  base=${name%.*}
  out="$OUT_DIR/$base.md"

  echo "DOCX → MD: $f -> $out"
  pandoc "$f" -t markdown -o "$out"
done

# PDF → MD (Best effort via pdftotext)
for f in "$SRC_DIR"/*.[pP][dD][fF]; do
  [ -e "$f" ] || continue
  name=${f##*/}
  base=${name%.*}
  out="$OUT_DIR/$base.md"

  echo "PDF  → MD: $f -> $out"
  # pdftotext outputs plain text, which is valid (if basic) markdown
  pdftotext -layout "$f" "$out"
done

# HTML → MD
for f in "$SRC_DIR"/*.[hH][tT][mM][lL]; do
  [ -e "$f" ] || continue
  name=${f##*/}
  base=${name%.*}
  out="$OUT_DIR/$base.md"

  echo "HTML → MD: $f -> $out"
  pandoc "$f" -t markdown -o "$out"
done

# JSON (Pandoc AST) → MD
for f in "$SRC_DIR"/*.[jJ][sS][oO][nN]; do
  [ -e "$f" ] || continue
  name=${f##*/}
  base=${name%.*}
  out="$OUT_DIR/$base.md"

  # Check if it looks like a Pandoc AST (usually starts with {"pandoc-api-version":...} or [{"unMeta":...}])
  # We'll try to convert it and see if pandoc accepts it as json
  if grep -q "pandoc-api-version" "$f"; then
    echo "JSON → MD: $f -> $out"
    pandoc "$f" -f json -t markdown -o "$out"
  fi
done

echo
echo "Done."
