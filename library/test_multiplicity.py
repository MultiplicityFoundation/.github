# test_multiplicity.py
# Unit tests for the Multiplicity library
# Aligned with Ξ-Constitution for lawful verification

import unittest
from manager import MultiplicityManager, MultiplicityBound
from parser import parse_multiplicity_dsl

class TestMultiplicity(unittest.TestCase):
    def setUp(self):
        self.manager = MultiplicityManager()

    def test_association_definition(self):
        assoc_id = self.manager.define_association(
            "Student", "Course", MultiplicityBound.ZERO_TO_MANY, MultiplicityBound.ZERO_TO_MANY
        )
        self.assertIn(assoc_id, self.manager.associations)
        self.assertEqual(self.manager.associations[assoc_id].source_class, "Student")

    def test_link_instances(self):
        assoc_id = self.manager.define_association(
            "Student", "Course", MultiplicityBound.ZERO_TO_MANY, MultiplicityBound.ZERO_TO_MANY
        )
        result = self.manager.link_instances(assoc_id, "alice", "math")
        self.assertTrue(result)
        self.assertIn("alice", self.manager.instance_map["Student"])

    def test_multiplicity_violation(self):
        assoc_id = self.manager.define_association(
            "Student", "Course", MultiplicityBound.ZERO_TO_ONE, MultiplicityBound.ONE
        )
        self.manager.link_instances(assoc_id, "alice", "math")
        with self.assertRaises(ValueError):
            self.manager.link_instances(assoc_id, "alice", "physics")  # Violates 0..1

    def test_dsl_parser(self):
        dsl = """
        association Student 0..* Course 0..*;
        link Student:alice Course:math;
        """
        parse_multiplicity_dsl(dsl, self.manager)
        self.assertIn("alice", self.manager.instance_map["Student"])
        self.assertIn("math", self.manager.instance_map["Course"])

if __name__ == "__main__":
    unittest.main()
