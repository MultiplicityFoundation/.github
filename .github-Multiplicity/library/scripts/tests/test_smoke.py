import numpy as np
import pytest
pytest.importorskip('moc')
from moc import build_108, eval_word, R1, R2, R3, R_total

def test_pipeline_108():
    w = build_108(ternary_first=True, swap_offbeat=True)
    x0 = np.zeros((1,), dtype=float) + 1.0  # trivial seed
    x = w(x0)
    assert len(x) == 108
    # resonance against itself is 1
    tiers = [27,9,3,4,2]
    etas  = [0.30,0.25,0.20,0.15,0.10]
    r1 = R1(x, x)
    r2 = R2(x, x, tiers, etas)
    r3 = R3(x, x, tiers, etas)
    R = R_total(r1, r2, r3)
    assert 0.99 <= R <= 1.00001
