#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"

if ! command -v npx >/dev/null 2>&1; then
  echo "Error: npx not found. Install Node.js + npm first."
  exit 1
fi

# Collect markdown files, excluding common noisy dirs
mapfile -d '' FILES < <(
  find "$ROOT" -type f -name '*.md' \
    -not -path '*/node_modules/*' \
    -not -path '*/.git/*' \
    -not -path '*/dist/*' \
    -not -path '*/build/*' \
    -not -path '*/.venv/*' \
    -not -path '*/__pycache__/*' \
    -print0
)

if [ "${#FILES[@]}" -eq 0 ]; then
  echo "No Markdown files found under: $ROOT"
  exit 0
fi

echo "Auto-fixing ${#FILES[@]} Markdown files..."

# Use xargs to avoid argument-length limits on big repos
printf '%s\0' "${FILES[@]}" \
  | xargs -0 -n 200 npx -y markdownlint-cli --fix

echo "Done."
