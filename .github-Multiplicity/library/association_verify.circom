// association_verify.circom
// zk-SNARK circuit for verifying prime-audited associations
// Aligned with Λᵖ-Archivum and PIRTM

pragma circom 2.0.0;

template AssociationVerify() {
    signal input source_count;    // Number of source instances
    signal input target_count;    // Number of target instances
    signal input source_mult;     // Encoded multiplicity (0: 0..1, 1: 1, 2: 0..*, 3: 1..*)
    signal input target_mult;
    signal input prime_tag;       // Prime tag for auditability
    signal output is_valid;

    // Simple prime check (mock for small primes)
    signal is_prime;
    is_prime <== (prime_tag == 2 || prime_tag == 3 || prime_tag == 5 || prime_tag == 7) ? 1 : 0;

    // Multiplicity validation
    signal source_valid;
    signal target_valid;

    // 0..1: count <= 1
    signal source_zero_one;
    source_zero_one <== (source_mult == 0) ? (source_count <= 1 ? 1 : 0) : 1;
    
    // 1: count == 1
    signal source_one;
    source_one <== (source_mult == 1) ? (source_count == 1 ? 1 : 0) : 1;
    
    // 0..*: count >= 0
    signal source_zero_many;
    source_zero_many <== (source_mult == 2) ? (source_count >= 0 ? 1 : 0) : 1;
    
    // 1..*: count >= 1
    signal source_one_many;
    source_one_many <== (source_mult == 3) ? (source_count >= 1 ? 1 : 0) : 1;

    source_valid <== source_zero_one * source_one * source_zero_many * source_one_many;

    // Repeat for target
    signal target_zero_one;
    target_zero_one <== (target_mult == 0) ? (target_count <= 1 ? 1 : 0) : 1;
    signal target_one;
    target_one <== (target_mult == 1) ? (target_count == 1 ? 1 : 0) : 1;
    signal target_zero_many;
    target_zero_many <== (target_mult == 2) ? (target_count >= 0 ? 1 : 0) : 1;
    signal target_one_many;
    target_one_many <== (target_mult == 3) ? (target_count >= 1 ? 1 : 0) : 1;

    target_valid <== target_zero_one * target_one * target_zero_many * target_one_many;

    // Final validity
    is_valid <== source_valid * target_valid * is_prime;
}

component main = AssociationVerify();
