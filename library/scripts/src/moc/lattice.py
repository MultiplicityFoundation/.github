import numpy as np
from numpy.typing import NDArray

def rotate(x: NDArray, tau: int) -> NDArray:
    """Circularly shift x by tau ticks (modulo length)."""
    tau %= len(x)
    if tau == 0: return x
    return np.concatenate([x[-tau:], x[:-tau]])

def divisibility_mask(n: int, d: int, offset: int = 0) -> NDArray[np.bool_]:
    """Create a boolean mask of length n, True where (t-offset)%d==0."""
    t = np.arange(n, dtype=int)
    return ((t - offset) % d) == 0
