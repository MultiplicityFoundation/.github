from dataclasses import dataclass
from typing import Literal, Optional, Sequence
import numpy as np
from numpy.typing import NDArray
from .operators import S, A, A_offset, R, W

Kind = Literal["S","A","Aoff","R","W"]

@dataclass(frozen=True)
class Op:
    kind: Kind
    p: Optional[int] = None
    r: Optional[int] = None
    d: Optional[int] = None
    alpha: Optional[float] = None
    phi: Optional[float] = None
    ch: int = 0
    perm: Optional[Sequence[int]] = None
    offset: int = 0

def eval_word(x: NDArray, ops: list[Op]) -> NDArray:
    """Apply a sequence of operators to signal x (right-to-left)."""
    y = x
    for op in ops:
        if op.kind == "S":
            y = S(y, op.mod, op.r or 1)
        elif op.kind == "A":
            y = A(y, op.d, op.alpha or 0.0, op.ch)
        elif op.kind == "Aoff":
            y = A_offset(y, op.d, op.alpha or 0.0, op.offset, op.ch)
        elif op.kind == "R":
            y = R(y, op.d, op.modhi or 0.0)
        elif op.kind == "W":
            y = W(y, op.mod, list(op.moderm or []))
        else:
            raise ValueError(f"unknown op: {op}")
    return y

@dataclass
class Word:
    ops: list[Op]
    def __call__(self, x: NDArray) -> NDArray:
        return eval_word(x, self.ops)
