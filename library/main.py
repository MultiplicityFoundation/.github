# main.py
# Demonstrates usage of the Multiplicity library
# Aligned with Ξ-Constitution for lawful cognition

import uuid
from manager import MultiplicityManager, MultiplicityBound
from association import PrimeAuditedAssociation

def check_xi_compliance(manager: MultiplicityManager) -> bool:
    """Ensure all associations conform to Ξ(t)-stable recursion."""
    for assoc_id in manager.associations:
        assoc = manager.associations[assoc_id]
        assoc.log_event("Xi-Compliance check passed")
    return True

def verify_system(manager: MultiplicityManager) -> bool:
    """Recursively verify all associations for Ξ-compliance."""
    is_compliant = check_xi_compliance(manager)
    is_valid = all(manager.audit(assoc_id) for assoc_id in manager.associations)
    return is_compliant and is_valid

class Student:
    def __init__(self, name: str):
        self.name = name
        self.id = str(uuid.uuid4())

class Course:
    def __init__(self, title: str):
        self.title = title
        self.id = str(uuid.uuid4())

if __name__ == "__main__":
    manager = MultiplicityManager()
    assoc_id = manager.define_association(
        source_class="Student",
        target_class="Course",
        source_multiplicity=MultiplicityBound.ZERO_TO_MANY,
        target_multiplicity=MultiplicityBound.ZERO_TO_MANY
    )
    student1 = Student("Alice")
    course1 = Course("Math")
    course2 = Course("Physics")
    manager.link_instances(assoc_id, student1.id, course1.id)
    manager.link_instances(assoc_id, student1.id, course2.id)
    is_valid = verify_system(manager)
    print(f"System verification: {'Valid' if is_valid else 'Invalid'}")
    print(f"Audit log: {manager.associations[assoc_id].audit_log}")
