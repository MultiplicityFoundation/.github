import numpy as np
from .word import Op, Word

def build_108(ternary_first: bool = True, swap_offbeat: bool = False) -> Word:
    """Build canonical 108-cycle operator word."""
    ops: list[Op] = []
    if ternary_first:
        ops += [Op(kind="S", p=3, r=3), Op(kind="S", p=2, r=2)]
        for d,a in [(27,1.0),(9,0.7),(3,0.5),(4,0.3),(2,0.2)]:
            ops += [Op(kind="A", d=d, alpha=a)]
        if swap_offbeat:
            ops += [Op(kind="W", p=2, perm=[1,0])]
    else:
        ops += [Op(kind="S", p=2, r=2)]
        if swap_offbeat:
            ops += [Op(kind="W", p=2, perm=[1,0])]
        ops += [Op(kind="S", p=3, r=3)]
        for d,a in [(4,0.3),(2,0.2),(27,1.0),(9,0.7),(3,0.5)]:
            ops += [Op(kind="A", d=d, alpha=a)]
    return Word(ops)

def generate_108(weights=None, swap=False, rot_phi27=0) -> np.ndarray:
    """
    Generate 108-tick pattern with tiered weights, optional swap and rotation.

    Parameters
    ----------
    weights : dict, optional
        Weights for tiers (keys: w27, w9, w3, w4, w2).
    swap : bool
        Whether to swap within 4-grids.
    rot_phi27 : int
        Rotation multiplier for 27-tier (downbeat pin).

    Returns
    -------
    x : ndarray
        108-length scalar pattern.
    """
    n = 108
    w = dict(w27=1.0, w9=0.7, w3=0.5, w4=0.3, w2=0.2)
    if weights: w.update(weights)
    x = np.zeros(n, dtype=float)
    for t in range(n):
        if t % 27 == 0: x[t] += w["w27"]
        elif t % 9 == 0: x[t] += w["w9"]
        elif t % 3 == 0: x[t] += w["w3"]
        elif t % 4 == 0: x[t] += w["w4"]
        elif t % 2 == 0: x[t] += w["w2"]
    if swap:
        y = x.copy()
        for b in range(0, n, 4):
            y[b+0], y[b+2] = x[b+2], x[b+0]
        x = y
    # pin by rotation on 27-tier
    tau = int(round(rot_phi27 * (n/27)))
    x = np.roll(x, tau)
    return x
