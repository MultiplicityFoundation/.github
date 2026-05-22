# manager.py
# Manages prime-audited associations for the Multiplicity language
# Aligned with Ξ-Constitution and Prime Cascade 2.0 for lawful recursion

from typing import Dict, List, Any
from .association import PrimeAuditedAssociation, MultiplicityBound
from .engine import EvolutionEngine

class MultiplicityManager:
    """Manages prime-audited associations and enforces constraints."""
    def __init__(self):
        self.associations: Dict[str, PrimeAuditedAssociation] = {}
        self.instance_map: Dict[str, Dict[str, List[Any]]] = {}
        self.evolution_engine = EvolutionEngine()

    def define_association(self, source_class: str, target_class: str,
                         source_multiplicity: MultiplicityBound,
                         target_multiplicity: MultiplicityBound) -> str:
        """Define a prime-audited association."""
        assoc = PrimeAuditedAssociation(source_class, target_class,
                                      source_multiplicity, target_multiplicity)
        self.associations[assoc.association_id] = assoc
        if source_class not in self.instance_map:
            self.instance_map[source_class] = {}
        if target_class not in self.instance_map:
            self.instance_map[target_class] = {}
        assoc.log_event(f"Defined association {assoc.association_id}")
        return assoc.association_id

    def link_instances(self, assoc_id: str, source_instance: Any, target_instance: Any) -> bool:
        """Link instances, enforce multiplicity, and evolve state."""
        if assoc_id not in self.associations:
            raise ValueError(f"Association {assoc_id} not found")
        assoc = self.associations[assoc_id]
        source_class = assoc.source_class
        target_class = assoc.target_class
        if source_instance not in self.instance_map[source_class]:
            self.instance_map[source_class][source_instance] = []
        if target_instance not in self.instance_map[target_class]:
            self.instance_map[target_class][target_instance] = []
        current_targets = self.instance_map[source_class][source_instance]
        current_sources = self.instance_map[target_class][target_instance]
        if not assoc.validate(len(current_sources) + 1, len(current_targets) + 1):
            raise ValueError(f"Multiplicity constraint violated for {assoc_id}")
        state = (source_instance, target_instance)
        self.evolution_engine.evolve(state)
        self.instance_map[source_class][source_instance].append(target_instance)
        self.instance_map[target_class][target_instance].append(source_instance)
        assoc.log_event(f"Linked {source_instance} to {target_instance}")
        return True

    def audit(self, assoc_id: str) -> bool:
        """Audit an association for compliance with multiplicity and Ξ(t)."""
        if assoc_id not in self.associations:
            return False
        assoc = self.associations[assoc_id]
        for source, targets in self.instance_map[assoc.source_class].items():
            if not assoc.validate(len(targets), len(self.instance_map[assoc.target_class].get(targets[0], []))):
                assoc.log_event(f"Audit failed for {assoc_id}")
                return False
        assoc.log_event(f"Audit passed for {assoc_id}")
        return True
