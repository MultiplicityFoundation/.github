from dataclasses import dataclass
from typing import List

@dataclass
class Hypergraph:
    V: int
    E: int
    edge_ptr: list[int]       # CSR pointers (size E+1)
    edge_vtx: list[int]       # flattened vertex ids
    # Minimal placeholder. Relation ops can be added later.
