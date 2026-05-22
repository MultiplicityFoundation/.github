
import csv, io

# I-WKD Module: Inverted Wasserstein Knowledge Distillation
# The inversion targets the teacher→student distillation pipeline:
# Forward WKD: Teacher(full ACFL) → Wasserstein transport → Student(edge)
#   Goal: minimize WD between teacher and student logits
# Inverted WKD: Student(edge) → inverse transport → Teacher(full)
#   Goal: maximize WD to find adversarial student states,
#   detect drift, and stress-test distillation fidelity

module_files = [
    # Phase 1 - Operator Core
    ("ipwkd/__init__.py", "module", 1, "Public API: exports operators, transport, drift_detector, fidelity, adversarial"),
    ("ipwkd/operators.py", "module", 1, "Inverted distillation operators: student→teacher reverse transport, anti-fidelity computation, categorical truth-scale divergence"),
    ("ipwkd/transport.py", "module", 1, "Inverted optimal transport: maximize WD instead of minimize, anti-transport pathway selector, worst-case transport plan computation"),
    
    # Phase 2 - Drift Detection Engine
    ("ipwkd/drift_detector.py", "module", 2, "Student model drift quantification: categorical truth-scale fidelity loss over time, veto axiom preservation monitor, compensatory property degradation tracker"),
    ("ipwkd/fidelity.py", "module", 2, "Inverted fidelity analysis: truth-value divergence per predicate, categorical label flip detector, confidence interval collapse monitor"),
    
    # Phase 3 - Anti-Distillation Stress Engine
    ("ipwkd/stress.py", "module", 3, "Anti-distillation stress tests: generate adversarial inputs that maximize student-teacher divergence, find minimum-fidelity input regions, veto-axiom-breaking input search"),
    ("ipwkd/predicate_inverter.py", "module", 3, "Health predicate inversion: apply De Morgan to 5 ACFL predicates through distillation pipeline, measure truth-value preservation loss per predicate tree depth"),
    
    # Phase 4 - Governance & Validators
    ("ipwkd/governance.py", "module", 4, "CCRE-gated distillation governance: inverted gain function behavior under distillation, FREEZE-RESONANCE trigger sensitivity in student model, contraction certification stress under inverse transport"),
    ("ipwkd/validators.py", "module", 4, "Input validation: transport plan validity, fidelity threshold checks, truth-scale range enforcement, Wasserstein distance bounds"),
    
    # Phase 5 - Cross-System Adversarial Harness
    ("ipwkd/adversarial.py", "module", 5, "3-way adversarial harness: WKD(forward) vs I-WKD(inverted) vs I-WKD-CCRE(governance-stressed), distillation fidelity comparison, edge-cloud divergence analysis"),
]

test_files = [
    # Phase 1
    ("tests/iwkd/__init__.py", "test", 1, "Test package init"),
    ("tests/iwkd/conftest.py", "test", 1, "Fixtures: teacher/student model mocks, ACFL predicate outputs, transport plans, categorical truth-scale vectors, edge device constraints"),
    ("tests/iwkd/test_operators.py", "test", 1, 
     "8 methods: reverse_transport_basic, anti_fidelity_computation, boundary_all_zero, boundary_all_one, "
     "known_value_n2, known_value_n5, dtype_consistency, nan_rejection"),
    ("tests/iwkd/test_transport.py", "test", 1,
     "7 methods: max_wd_exceeds_min_wd, anti_transport_plan_validity, worst_case_vs_average, "
     "transport_cost_bounds, symmetric_input_behavior, n1_identity, large_predicate_set_stability"),
    
    # Phase 2
    ("tests/iwkd/test_drift_detector.py", "test", 2,
     "6 methods: zero_drift_at_fresh_distillation, drift_increases_with_perturbation, "
     "veto_axiom_preservation_monitor, compensatory_degradation_detection, "
     "categorical_label_stability, threshold_trigger_accuracy"),
    ("tests/iwkd/test_fidelity.py", "test", 2,
     "5 methods: per_predicate_divergence, categorical_flip_detection, "
     "confidence_interval_collapse, fidelity_monotonicity, teacher_student_gap_ordering"),
    
    # Phase 3
    ("tests/iwkd/test_stress.py", "test", 3,
     "6 methods: adversarial_input_maximizes_divergence, minimum_fidelity_region_found, "
     "veto_breaking_input_search, stress_across_all_5_predicates, "
     "depth_dependent_preservation_loss, non_associativity_stress"),
    ("tests/iwkd/test_predicate_inverter.py", "test", 3,
     "6 methods: de_morgan_through_distillation, per_predicate_truth_loss, "
     "tree_depth_preservation_gradient, inverted_predicate_axiom_check, "
     "compound_meta_predicate_inversion, ql_implication_chain_survival"),
    
    # Phase 4
    ("tests/iwkd/test_governance.py", "test", 4,
     "6 methods: inverted_gain_three_regime, freeze_resonance_student_sensitivity, "
     "contraction_certification_under_inverse_transport, ccre_witness_object_emission, "
     "lipschitz_bound_stress, drift_bound_100_updates"),
    ("tests/iwkd/test_validators.py", "test", 4,
     "5 methods: invalid_transport_plan_rejection, fidelity_threshold_enforcement, "
     "truth_scale_out_of_range, wd_bounds_validation, type_coercion_passthrough"),
    
    # Phase 5
    ("tests/iwkd/test_adversarial.py", "test", 5,
     "7 methods: three_way_output_consistency, forward_vs_inverted_divergence_ordering, "
     "governance_stressed_vs_unstressed, distillation_fidelity_comparison_all_predicates, "
     "edge_cloud_divergence_quantification, veto_break_both_directions, "
     "positional_sensitivity_through_distillation"),
    ("tests/iwkd/test_integration.py", "test", 5,
     "7 methods: shared_types_import, end_to_end_pipeline, round_trip_de_morgan_through_distillation, "
     "cross_module_type_compatibility, large_predicate_stress_n20, determinism_across_runs, "
     "error_propagation_validators_through_operators"),
]

all_files = module_files + test_files

# Count test methods
total_methods = 0
for path, ftype, phase, desc in test_files:
    if "methods:" in desc.lower() or "method" in desc.lower():
        parts = desc.split(":")
        if len(parts) > 1:
            methods = [m.strip() for m in parts[1].split(",") if m.strip()]
            total_methods += len(methods)

# Write CSV manifest
output = io.StringIO()
writer = csv.writer(output)
writer.writerow(["path", "type", "phase", "description"])
for path, ftype, phase, desc in all_files:
    writer.writerow([f"packages/dnakey/src/{path}" if ftype == "module" else f"packages/dnakey/{path}", ftype, phase, desc])

csv_content = output.getvalue()
with open("iwkd_scaffold_manifest.csv", "w") as f:
    f.write(csv_content)

module_count = len(module_files)
test_count = len(test_files)
print(f"Module files: {module_count}")
print(f"Test files: {test_count}")
print(f"Total files: {module_count + test_count}")
print(f"Total test methods: {total_methods}")
print(f"CSV written: iwkd_scaffold_manifest.csv")
