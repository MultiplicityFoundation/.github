import numpy as np
from numpy.typing import NDArray

def _normed_corr(a: NDArray, b: NDArray) -> float:
    num = float(np.dot(a.ravel(), b.ravel()))
    den = float(np.linalg.norm(a) * np.linalg.norm(b))
    return 0.0 if den == 0 else (num / den) ** 2

def R1(x: NDArray, D: NDArray, window: str = "hann") -> float:
    """Time-domain resonance score."""
    n = len(x)
    if window == "hann":
        w = 0.5 - 0.5 * np.cos(2*np.pi*np.arange(n)/n)
    else:
        w = np.ones(n)
    xa = x * w[:, None] if x.ndim == 2 else x * w
    Da = D * w[:, None] if D.ndim == 2 else D * w
    best = 0.0
    for tau in range(n):
        best = max(best, _normed_corr(xa, np.roll(Da, tau, axis=0)))
    return float(best)

def _energy_on_combs(X: NDArray, K: list[int]) -> float:
    num = np.sum(np.abs(X[K])**2)
    den = np.sum(np.abs(X)**2)
    return 0.0 if den == 0 else float(num/den)

def R2(x: NDArray, D: NDArray, tiers: list[int], etas: list[float]) -> float:
    """Harmonic-lock resonance score."""
    n = len(x)
    X = np.fft.rfft(x, axis=0); X = np.sum(np.abs(X)**2, axis=-1) if x.ndim==2 else np.abs(X)**2
    Y = np.fft.rfft(D, axis=0); Y = np.sum(np.abs(Y)**2, axis=-1) if D.ndim==2 else np.abs(Y)**2
    def K(d): return np.arange(0, (n//2)+1, n//d, dtype=int)
    s = 0.0
    for eta, d in zip(etas, tiers):
        s += eta * np.sqrt(_energy_on_combs(X, K(d)) * _energy_on_combs(Y, K(d)))
    return float(s)

def R3(x: NDArray, D: NDArray, tiers: list[int], etas: list[float]) -> float:
    """Phase-coherence resonance score."""
    n = len(x)
    X = np.fft.rfft(x, axis=0); Y = np.fft.rfft(D, axis=0)
    if x.ndim==2: X = np.sum(X, axis=-1)
    if D.ndim==2: Y = np.sum(Y, axis=-1)
    s = 0.0
    for eta, d in zip(etas, tiers):
        step = n//d
        idx = np.arange(step, (n//2)+1, step, dtype=int)  # exclude DC
        if len(idx)==0: continue
        ph = np.exp(1j * (np.angle(X[idx]) - np.angle(Y[idx])))
        s += eta * float(np.abs(np.mean(ph)))
    return float(s)

def R_total(R1v: float, R2v: float, R3v: float, lambdas=(0.4,0.35,0.25)) -> float:
    """Aggregate resonance score."""
    l1,l2,l3 = lambdas
    return float(l1*R1v + l2*R2v + l3*R3v)
