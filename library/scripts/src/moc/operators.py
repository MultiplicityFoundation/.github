import numpy as np
from numpy.typing import NDArray
from .lattice import divisibility_mask, rotate

def S(x: NDArray, p: int, r: int = 1) -> NDArray:
    """Zero-order hold subdivision: repeat each sample p^r times.

    Parameters
    ----------
    x : ndarray
        Signal, length n.
    p : int
        Prime subdivision factor.
    r : int
        Power (repeat each item p^r times).

    Returns
    -------
    y : ndarray
        Length n * p^r signal.
    """
    n = len(x)
    factor = p ** r
    return np.repeat(x, factor, axis=0)

def A(x: NDArray, d: int, alpha: float, ch: int = 0) -> NDArray:
    """Additive accent at t ≡ 0 mod d on channel ch.

    Parameters
    ----------
    x : ndarray
        Signal, length n or (n, k).
    d : int
        Divisor (gate period).
    alpha : float
        Accent value.
    ch : int, optional
        Channel index (default: 0).

    Returns
    -------
    y : ndarray
        Signal with accents.
    """
    n = len(x)
    y = x.copy()
    m = divisibility_mask(n, d)
    if x.ndim == 1:
        y[m] += alpha
    else:
        y[m, ch] += alpha
    return y

def A_offset(x: NDArray, d: int, alpha: float, offset: int, ch: int = 0) -> NDArray:
    """Additive accent with periodic offset."""
    n = len(x)
    y = x.copy()
    m = divisibility_mask(n, d, offset)
    if x.ndim == 1:
        y[m] += alpha
    else:
        y[m, ch] += alpha
    return y

def R(x: NDArray, d: int, phi: float) -> NDArray:
    """Rotation by tau = phi * n/d ticks. Supports fractional via FFT phase.

    Parameters
    ----------
    x : ndarray
        Signal, length n.
    d : int
        Denominator (divisor of n).
    phi : float
        Rotation multiplier.

    Returns
    -------
    y : ndarray
        Rotated signal.
    """
    n = len(x)
    tau = phi * (n / d)
    if abs(tau - round(tau)) < 1e-12:
        return rotate(x, int(round(tau)))
    # fractional: per-channel FFT phase
    X = np.fft.rfft(x, axis=0)
    k = np.arange(X.shape[0])[:, None] if x.ndim == 2 else np.arange(X.shape[0])
    phase = np.exp(-2j * np.pi * k * tau / n)
    Y = X * phase
    y = np.fft.irfft(Y, n=n, axis=0)
    return y.astype(x.dtype, copy=False)

def W(x: NDArray, p: int, perm: list[int]) -> NDArray:
    """Within-cell permutation of size p (length must be multiple of p).

    Parameters
    ----------
    x : ndarray
        Signal, length n.
    p : int
        Cell size (arity).
    perm : list[int]
        Permutation of 0..mod-1.

    Returns
    -------
    y : ndarray
        Signal with permuted cells.

    Raises
    ------
    AssertionError
        If n is not a multiple of p.
    """
    n = len(x)
    assert n % p == 0, "length not multiple of p"
    y = x.copy()
    for c in range(0, n, p):
        blk = y[c:c+p]
        y[c:c+p] = blk[perm]
    return y
