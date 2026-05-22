# Determinism and Exact Replay

Set these environment variables before running experiments or figure scripts:

```bash
export PYTHONHASHSEED=0
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MKL_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
# Optional GPU-related flags (not required; CPU-only is fine)
export TF_CUDNN_DETERMINISTIC=1
export CUBLAS_WORKSPACE_CONFIG=:4096:8
```

Recommended invocation:

```bash
conda env create -f repro/env/environment.yml
conda activate moc-repro
# lock matplotlib cache for stable rendering
rm -rf ~/.cache/matplotlib

# run experiments and build artifacts
export PYTHONHASHSEED=0 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1
python repro/scripts/run_exps.py --configs repro/configs --out repro/outputs --threads 1
python repro/scripts/make_figs.py --in repro/outputs --out repro/outputs/figs
python repro/scripts/make_tables.py --in repro/outputs --out repro/outputs/tables
```

Notes:

- Use single-threaded FFT plans; avoid autoscaling thread pools.
- Keep library versions pinned (see `environment.yml` or `requirements.txt`).
- Use fixed seeds provided in configs; do not override unless testing.
- For NumPy/SciPy FFTs, keep workers=1; avoid multi-threaded FFT backends.
- Clean caches between runs if plots differ across OS themes.
