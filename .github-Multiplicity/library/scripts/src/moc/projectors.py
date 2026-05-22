import numpy as np
from numpy.typing import NDArray

def Pi_indices(n: int, d: int) -> np.ndarray:
    """Return harmonic indices preserved by Pi_d: multiples of d in [0..n-1]."""
    return np.arange(0, n, d, dtype=int)

def apply_Pi(x: NDArray, d: int) -> NDArray:
    """Zero all harmonics except multiples of d.

    Parameters
    ----------
    x : ndarray
        Signal, length n.
    d : int
        Tier (divisor).

    Returns
    -------
    y : ndarray
        Projected signal.
    """
    X = np.fft.rfft(x, axis=0)
    n = len(x)
    keep = Pi_indices(n, d)
    mask = np.zeros_like(X, dtype=bool)
    mask[keep[:len(mask)]] = True  # rfft length n//2+1
    X_filtered = np.where(mask, X, 0)
    y = np.fft.irfft(X_filtered, n=n, axis=0)
    return y.astype(x.dtype, copy=False)

def tier_energy(x: NDArray, d: int) -> float:
    """Energy of Pi_d(x)."""
    y = apply_Pi(x, d)
    return float(np.sum(y * y))
