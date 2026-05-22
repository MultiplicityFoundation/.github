#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONFIG_DIR="${ROOT_DIR}/repro/configs"
OUT_DIR="${ROOT_DIR}/repro/outputs"

mkdir -p "${OUT_DIR}/figs" "${OUT_DIR}/tables" "${OUT_DIR}/logs" "${OUT_DIR}/checkpoints"

echo "[1/4] Running experiments ..."
python "${ROOT_DIR}/repro/scripts/run_exps.py" --configs "${CONFIG_DIR}" --out "${OUT_DIR}" --threads 1

echo "[2/4] Building figures ..."
python "${ROOT_DIR}/repro/scripts/make_figs.py" --in "${OUT_DIR}" --out "${OUT_DIR}/figs"

echo "[3/4] Building tables ..."
python "${ROOT_DIR}/repro/scripts/make_tables.py" --in "${OUT_DIR}" --out "${OUT_DIR}/tables"

echo "[4/4] Emitting seed report ..."
python "${ROOT_DIR}/repro/scripts/seed_report.py" --logs "${OUT_DIR}/logs" --out "${OUT_DIR}/seed_report.txt"

echo "Done."
