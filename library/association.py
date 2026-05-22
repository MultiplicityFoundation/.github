# association.py
# Defines multiplicity bounds and prime-audited associations for the Multiplicity language
# Aligned with Ξ-Constitution and Λᵖ-Archivum for lawful recursion

import uuid
from typing import List
from dataclasses import dataclass, field
from enum import Enum
from .utils import get_prime_tag

class MultiplicityBound(Enum):
    ZERO_TO_ONE = "0..1"  # Optional, at most one
    ONE = "1"            # Exactly one
    ZERO_TO_MANY = "0..*" # Zero or more
    ONE_TO_MANY = "1..*"  # One or more

@dataclass
class PrimeAuditedAssociation:
    """Association with prime-indexed auditability and multiplicity constraints."""
    source_class: str
    target_class: str
    source_multiplicity: MultiplicityBound
    target_multiplicity: MultiplicityBound
    association_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    prime_tag: int = field(default_factory=lambda: get_prime_tag(0))
    audit_log: List[str] = field(default_factory=list)

    def log_event(self, event: str):
        """Log events for Λᵖ-Archivum traceability."""
        self.audit_log.append(f"[Prime-{self.prime_tag}]: {event}")

    def validate(self, source_instances: int, target_instances: int) -> bool:
        """Verify multiplicity constraints."""
        def check_bound(bound: MultiplicityBound, count: int) -> bool:
            if bound == MultiplicityBound.ZERO_TO_ONE:
                return 0 <= count <= 1
            elif bound == MultiplicityBound.ONE:
                return count == 1
            elif bound == MultiplicityBound.ZERO_TO_MANY:
                return count >= 0
            elif bound == MultiplicityBound.ONE_TO_MANY:
                return count >= 1
            return False
        is_valid = check_bound(self.source_multiplicity, source_instances) and \
                   check_bound(self.target_multiplicity, target_instances)
        self.log_event(f"Validation {'passed' if is_valid else 'failed'}")
        return is_valid
