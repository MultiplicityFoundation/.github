# utils.py
# Utility functions for prime-indexed operations in the Multiplicity language
# Aligned with Λᵖ-Archivum and PIRTM for prime-based recursion

from sympy import nextprime
import json
from pathlib import Path
from typing import Dict, Any, Optional, List

def get_prime_tag(index: int) -> int:
    """Assign a unique prime tag based on index for Λᵖ auditability."""
    prime = 2
    for _ in range(index):
        prime = nextprime(prime)
    return prime

def multiplicity_gate(prime_index: int, tensor_state: Any) -> Any:
    """Prime gate modulating recursive link state per PIRTM and Langlands."""
    return hash(str(tensor_state)) % get_prime_tag(prime_index)

def load_glossary_json(root: Path | str = '.') -> Dict[str, Any]:
    """Load generated glossary JSON index from multiplicity/library/glossary/index.json."""
    glossary_path = Path(root) / 'multiplicity' / 'library' / 'glossary' / 'index.json'
    if not glossary_path.exists():
        raise FileNotFoundError(f"Glossary JSON not found at {glossary_path}")
    return json.loads(glossary_path.read_text(encoding='utf-8'))

def find_glossary_term(term: str, root: Path | str = '.') -> Optional[Dict[str, Any]]:
    glossary = load_glossary_json(root)
    for entry in glossary.get('terms', []):
        if entry.get('term', '').lower() == term.lower():
            return entry
    return None

def search_glossary(query: str, root: Path | str = '.') -> List[Dict[str, Any]]:
    glossary = load_glossary_json(root)
    query = query.strip().lower()
    results = []
    for entry in glossary.get('terms', []):
        if query in entry.get('term', '').lower() or query in entry.get('definition', '').lower():
            results.append(entry)
    return results
