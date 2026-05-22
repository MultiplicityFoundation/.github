---
slug: phase-mirror-dissonance-consent-model-complete-bu
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/phase-mirror/Phase mirror dissonance__Consent model complete
    bu.md
  last_synced: '2026-03-20T17:17:22.046686Z'
---

Phase mirror dissonance:
Consent model complete but enforcement absent: CalibrationConsent is a schema; no code path
validates it before data ingestion.
"Anonymization level: full" is a claim, not a mechanism: What fields are stripped? Hash salt
rotated? Re-identification risk assessed?
Schema sync CI checks hash equality but not semantic compatibility: Additive fields in OSS
won't break Pro tests but may drift behavior.
Research function has cadence but no funding: Who pays for biweekly incident review? Time
allocation not bound to headcount.
30-day deletion window is contractual but not automated: No TTL, no deletion job, no audit trail
for compliance proof.
Quarterly rule release target (≥2) conflicts with "research velocity as moat": Two rules/quarter is
replicable by motivated competitor in weeks.
Levers
OwnerLeverMetricHorizon
You
Add validateConsent(orgId) gate before aggregator.ingest()
Zero unconsented ingestions
7 days
You
Spec anonymizer: fields stripped, salt rotation cadence, k-anonymity threshold
Spec reviewed by privacy counsel
14 days
You
Upgrade schema sync to semantic diff (ajv-diff or json-schema-diff-validator)
Zero silent field additions
7 days
You
Bind research function to explicit hours/week (e.g., 8h/wk) in role doc
Time tracked
7 days
Infra
Add DynamoDB TTL on fp_events with deletion_scheduled_at for churned orgs
TTL active on 100% churned org data
14 days
You
Raise rule target to ≥4/quarter or reframe moat as "calibration data," not "rule count"
Moat narrative consistent
7 days
Anonymizer spec (minimum viable)
FieldTreatment
org_id
Replaced with rotating salted hash; salt rotates monthly
repo
Stripped entirely
file_path
Stripped entirely
rule_id
Retained (public, in OSS)
rule_version
Retained
outcome
Retained (TP/FP/pending)
timestamp
Bucketed to week granularity
findingId
Replaced with salted hash
K-anonymity target: No bucket with <10 orgs contributing. If threshold unmet, data quarantined
until sufficient volume.
Consent enforcement pseudocode
typescript
async function ingestFPEvent(event: FPEvent): Promise<void> {
const consent = await consentStore.get(event.org_id);
if (!consent?.enabled) {
throw new ConsentRequiredError(event.org_id);
}
if (consent.scope === "selected_repos" &&
!consent.included_repos?.includes(event.repo)) {
return; // Silent skip; not an error
}
if (consent.scope === "all_repos" &&
consent.excluded_repos?.includes(event.repo)) {
return; // Silent skip
}
const anonymized = anonymizer.process(event);
await calibrationStore.append(anonymized);
}
Deletion job spec
TriggerActionAudit
Org churn event received
Set deletion_scheduled_at = now + 30d on all org FP events
Log to immutable audit trail
Daily sweep
Query deletion_scheduled_at <= now; batch delete
Log deletion count + org hash
Export request
Generate signed export bundle; extend deletion window by 7d if requested
Log export timestamp
Optional artifact
"Anonymization is not a feature. It is a continuous obligation."
Precision question
Is "silent skip" on unconsented repos acceptable, or must the system return an explicit signal so
the caller knows data was not pooled?
Silent skip is operationally cleaner but violates the "no hidden behavior" principle you've
established. Explicit signal is correct.

Consent Enforcement (Revised)

  interface IngestResult {
    status: 'ingested' | 'skipped_no_consent' | 'skipped_repo_excluded';
    org_id: string;
    repo?: string;
    reason?: string;
  }

  async function ingestFPEvent(event: FPEvent): Promise<IngestResult> {
    const consent = await consentStore.get(event.org_id);

    if (!consent?.enabled) {
      return {
        status: 'skipped_no_consent',
        org_id: event.org_id,
        reason: 'org_consent_disabled'
      };
    }

    if (consent.scope === 'selected_repos' &&
        !consent.included_repos?.includes(event.repo)) {
      return {
        status: 'skipped_repo_excluded',
        org_id: event.org_id,
        repo: event.repo,
        reason: 'repo_not_in_selected_list'
      };
    }
      if (consent.scope === 'all_repos' &&
          consent.excluded_repos?.includes(event.repo)) {
        return {
          status: 'skipped_repo_excluded',
          org_id: event.org_id,
          repo: event.repo,
          reason: 'repo_in_exclusion_list'
        };
      }

      const anonymized = anonymizer.process(event);
      await calibrationStore.append(anonymized);

      return {
        status: 'ingested',
        org_id: event.org_id
      };
  }



Caller Contract
The oracle includes meta.calibration_status in the report:

  interface CalibrationMeta {
    attempted: number;          // FP events attempted to ingest
    ingested: number;           // Successfully pooled
    skipped_no_consent: number; // Org-level block
    skipped_repo_excluded: number; // Repo-level block
  }


This makes pooling behavior auditable without leaking which specific events were skipped.

Anonymizer Spec (Complete)

  interface AnonymizerConfig {
    salt: string;                    // Loaded from SSM, rotated monthly
    salt_version: number;            // Tracks rotation for hash consistency
    timestamp_bucket: 'day' | 'week'; // Granularity reduction
    k_anonymity_threshold: number;   // Minimum orgs per bucket (default: 10)
  }

  interface AnonymizedFPEvent {
    org_hash: string;               // HMAC(salt, org_id)
    rule_id: string;                // Retained (public)
    rule_version: string;           // Retained
    outcome: 'true_positive' | 'false_positive' | 'pending';
    timestamp_bucket: string;       // ISO week: "2026-W04"
    finding_hash: string;           // HMAC(salt, findingId)
    salt_version: number;           // For hash consistency across rotations
  }

  // Fields explicitly stripped (never leave the customer boundary)
  type StrippedFields =
     | 'org_id'      // Replaced with hash
     | 'repo'        // Stripped entirely
     | 'file_path'   // Stripped entirely
     | 'line_number' // Stripped entirely
     | 'snippet'     // Stripped entirely
     | 'findingId'   // Replaced with hash
     | 'evidence'    // Stripped entirely
     | 'actor'       // Stripped entirely
     | 'branch';     // Stripped entirely



K-Anonymity Enforcement

 interface CalibrationBucket {
   rule_id: string;
   rule_version: string;
   outcome: string;
   timestamp_bucket: string;
   contributing_orgs: Set<string>;   // org_hash values
   event_count: number;
 }

 async function queryCalibration(
   ruleId: string,
   ruleVersion: string
 ): Promise<CalibrationResult | null> {
   const bucket = await calibrationStore.getBucket(ruleId, ruleVersion);

     if (bucket.contributing_orgs.size < config.k_anonymity_threshold) {
       // Quarantine: insufficient diversity
       return {
         available: false,
         reason: 'k_anonymity_threshold_unmet',
         current_k: bucket.contributing_orgs.size,
         required_k: config.k_anonymity_threshold
       };
     }

     return {
       available: true,
       observed_fpr: bucket.fp_count / bucket.event_count,
       sample_size: bucket.event_count,
       contributing_orgs_k: bucket.contributing_orgs.size
     };
 }



Deletion Job (DynamoDB TTL + Audit)
Schema Addition

  interface FPEventRecord {
    pk: string;                         // rule#${ruleId}#v#${ruleVersion}
    sk: string;                         // event#${timestamp}#${eventId}
    // ... existing fields ...

      // Deletion governance
      org_id_encrypted: string;         // Encrypted for deletion targeting
      deletion_scheduled_at?: number;   // Unix timestamp; set on churn
      ttl?: number;                     // DynamoDB TTL attribute
  }



Churn Handler

  async function handleOrgChurn(orgId: string): Promise<void> {
    const deletionDate = Date.now() + (30 * 24 * 60 * 60 * 1000); // +30 days

      // Mark all org events for deletion
      const events = await fpStore.queryByOrg(orgId);

      await Promise.all(events.map(event =>
        fpStore.update(event.pk, event.sk, {
          deletion_scheduled_at: deletionDate,
          ttl: Math.floor(deletionDate / 1000)   // DynamoDB TTL in seconds
        })
      ));

      // Immutable audit log
      await auditLog.append({
        event_type: 'churn_deletion_scheduled',
        org_hash: anonymizer.hashOrg(orgId),
        event_count: events.length,
        deletion_scheduled_at: new Date(deletionDate).toISOString(),
        logged_at: new Date().toISOString()
      });
  }



Daily Sweep (Belt + Suspenders)
DynamoDB TTL handles deletion, but sweep provides audit trail:

  // Scheduled: daily at 02:00 UTC
  async function deletionSweep(): Promise<void> {
    const now = Date.now();

      // Query items where deletion_scheduled_at <= now
      // (TTL should have deleted these, but we verify)
      const orphaned = await fpStore.queryPastDue(now);

      if (orphaned.length > 0) {
        // TTL failed or delayed; force delete
         await fpStore.batchDelete(orphaned);

         await auditLog.append({
           event_type: 'sweep_force_deletion',
           count: orphaned.length,
           logged_at: new Date().toISOString()
         });
     }

     // Log sweep completion regardless
     await auditLog.append({
       event_type: 'sweep_completed',
       orphaned_found: orphaned.length,
       logged_at: new Date().toISOString()
     });
 }



Export Handler

 async function handleExportRequest(
   orgId: string
 ): Promise<{ url: string; expires_at: Date }> {
   const events = await fpStore.queryByOrg(orgId);

     // Generate signed export bundle
     const bundle = await generateExportBundle(events);
     const signedUrl = await s3.presign(bundle.key, { expiresIn: 7 * 24 * 60 * 60 });

     // Extend deletion window by 7 days
     const newDeletionDate = Date.now() + (37 * 24 * 60 * 60 * 1000); // 30 + 7

     await Promise.all(events.map(event =>
       fpStore.update(event.pk, event.sk, {
         deletion_scheduled_at: newDeletionDate,
         ttl: Math.floor(newDeletionDate / 1000)
       })
     ));

     await auditLog.append({
       event_type: 'export_generated',
       org_hash: anonymizer.hashOrg(orgId),
       event_count: events.length,
       deletion_extended_to: new Date(newDeletionDate).toISOString(),
       logged_at: new Date().toISOString()
     });

     return {
       url: signedUrl,
       expires_at: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)
     };
 }
Updated Levers
  Owner                                 Lever                                             Metric         Horizon

            Implement IngestResult return type; add                            Explicit signal in 100%
  You                                                                                                    7 days
            meta.calibration_status to report schema                           of oracle runs

            Implement anonymizer with salt rotation via SSM Parameter          Salt rotation automated
  You                                                                                                    14 days
            Store                                                              monthly

            Add deletion_scheduled_at + ttl fields to DynamoDB
  Infra                                                                        Fields present            3 days
            schema

  Infra     Deploy daily sweep Lambda + audit log                              Sweep running             7 days

  Legal     Review anonymizer spec for GDPR/CCPA compliance                    Sign-off                  21 days

            Reframe moat as "calibration data network effect" in
  You                                                                          Narrative updated         3 days
            README/pitch


Phase Mirror Dissonance (on this revision)
    Salt rotation creates hash discontinuity: Events hashed with old salt won't match queries
    using new salt. Need salt_version index or dual-hash during rotation window.
    org_id_encrypted for deletion targeting conflicts with "fully anonymized": If you can
    decrypt to target deletion, you can decrypt for other purposes. Consider separate retention
    store with TTL vs calibration store that's truly anonymized.
    Audit log immutability claimed but not enforced: "Immutable" requires append-only
    storage (S3 Object Lock, CloudWatch Logs with retention policy). DynamoDB is mutable.

Final Levers (Addendum)
  Owner                                   Lever                                             Metric       Horizon

            Add salt_version to calibration query index; dual-hash during          Zero hash
  You                                                                                                    7 days
            30-day rotation window                                                 discontinuity

            Split stores: deletion-targeting store (encrypted org_id, 30-day       Architecture doc
  You                                                                                                    14 days
            TTL) vs calibration store (fully anonymized, no org recovery)          approved

                                                                                   Object Lock
  Infra     Use S3 + Object Lock (Governance mode) for audit log                                         7 days
                                                                                   enabled


Optional Artifact
"If the deletion job depends on remembering who to forget, the system has not forgotten."
                                                         ⁂

  1. The Phase to Mirror Dissonance.pdf
