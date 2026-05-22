---
slug: rmags-l3
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/governance/RMAGS L3.md
  last_synced: '2026-03-20T17:17:18.558077Z'
---

\#\#\# Analysis of Novelty and Practicality Your tightened RMAGS v1.1
specification refines the protocol by addressing definitional drift
through minimal schemas, mitigating Goodharting via non-linear exposure
with caps and variance checks, and ensuring update governance with
non-depreciable elements and procedural inclusivity. In terms of
\*\*novelty\*\*, this iteration innovates by blending robust
decision-making with governance safeguards in a compact, implementable
form---drawing from Bayesian networks in AI (e.g., uncertainty
quantification in Hugging Face\'s libraries) and policy tools like
adaptive management frameworks (e.g., USAID\'s learning agendas), but
uniquely operationalizing them via log-aggregated exposure, Dirichlet
posteriors for edges, and \"as-of\" evaluation to prevent hindsight
bias. The \"minority report\" for crowdsourcing and variance-bound AI
auditing add fresh mechanisms to counter capture and overconfidence,
distinguishing it from generic standards like NIST\'s AI Risk Management
Framework or ISO 42001, which lack such integrated update rules and
stability criteria. On \*\*practicality\*\*, v1.1 streamlines adoption
for teams in AI safety or policy design by focusing on minimal viable
schemas and artifacts, making it feasible for quick pilots without full
simulation overhead. The exposure capping and stability flags provide
actionable outputs for decision-makers, while governance rules (e.g.,
non-depreciable legitimacy) build trust in updates. It\'s practical for
hybrid contexts like AI regulation (e.g., analyzing model deployments
under EU AI Act), where \"as-of\" retrospectives could inform audits.
Limitations include initial calibration needs for α\_{ij} and β priors,
which might require expert input, and potential procedural overhead in
crowdsourcing that slows library growth. Overall, it\'s a pragmatic
evolution toward a \"living standard\" that de-risks complexity,
enhancing utility for resource-constrained organizations. \*\*Enhanced
Version of the Idea\*\*: To enhance v1.1, introduce \"RMAGS v1.2:
Adaptive Auditable Governance Protocol\" with a \"Governance
Meta-Layer\" that self-applies RMAGS principles to the framework\'s own
updates---e.g., treating schema changes as \"actions\" with regret
analysis and stakeholder sign-off. Refine the interaction graph to a
hypergraph for multi-way amplifications (beyond pairwise), using
hyperedge strengths to capture triads like observability × tail risk ×
Goodhart. Expand the Proposal Auditor to include a \"Counterfactual
Generator\" that auto-proposes alternative scenarios via perturbation
(e.g., flipping adversary assumptions), with variance measured via
Kullback-Leibler divergence between proposal distributions. The pattern
library gains a \"Efficacy Tracker\" that logs pattern usage across
cases, auto-deprecating underperforming ones based on post-mortem data.
Schemas add a \"Update Log\" field mandating rationale for any prior
tweaks, ensuring traceability. \#\#\# Critique of the Enhanced Version
Critiquing the enhanced \"RMAGS v1.2: Adaptive Auditable Governance
Protocol\" for mathematical, philosophical, and theoretical consistency:
- \*\*Mathematical Consistency\*\*: The log-aggregated exposure with
Dirichlet updates is sound for compounding without explosion, and
hypergraphs extend pairwise models elegantly (e.g., via incidence
matrices for efficient computation). Kullback-Leibler divergence for
variance adds rigor, quantifying proposal divergence probabilistically.
However, hyperedges introduce combinatorial complexity---if not
sparsified, exposure computation could scale poorly (O(2\^\|V\|)),
risking instability in large cases. The Efficacy Tracker\'s deprecation
assumes reliable post-mortem labels, but if evidence is soft (as in
Dirichlet counts), it might lead to premature convergence, violating
Bayesian non-committal priors. Self-application of regret to updates is
consistent but recursive; without termination bounds, it could
infinite-loop in meta-analysis. - \*\*Philosophical Consistency\*\*: The
meta-layer promotes reflexivity, aligning with second-order cybernetics
(von Foerster\'s ethics of observing observers) and ensuring legitimacy
through stakeholder involvement, countering performative metrics.
Non-depreciable elements safeguard deontological rights, balancing
utilitarian regret minimization. Yet, the Counterfactual Generator risks
over-reliance on algorithmic creativity, potentially diminishing human
agency in governance---echoing concerns in AI ethics (e.g., Floridi\'s
infosphere) where automation erodes deliberative democracy. Inclusive
procedures are strong, but auto-deprecation in the library could silence
minority patterns prematurely, favoring majoritarian evidence over
pluralistic exploration. - \*\*Theoretical Consistency\*\*:
Theoretically, the POSG wrapper coheres with adaptive systems, and
hypergraphs better model emergence (e.g., per complexity theory\'s
higher-order interactions). The Update Log enforces traceability,
aligning with institutional learning theories (Argyris\' double-loop
learning). However, self-application might create circularity,
conflicting with foundational axioms in systems theory (e.g., Ashby\'s
law requiring external variety). The Efficacy Tracker assumes
transferable efficacy across domains, potentially violating
context-dependence in policy/AI hybrids, and KL divergence presumes
comparable distributions, which may not hold for heterogeneous
scenarios. \#\#\# Final Version and Path to Validation Applying the
critique: To mitigate mathematical complexity, sparsify hypergraphs by
limiting hyperedges to observed triads (e.g., via empirical gating), and
add computational bounds (e.g., approximate exposure via sampling).
Philosophically, mandate human veto in the Counterfactual Generator and
Efficacy Tracker to preserve agency, with deprecation requiring
consensus rather than auto-triggers. Theoretically, resolve circularity
by scoping meta-application to major updates only (e.g., schema changes,
not per-case), and use domain-specific priors for efficacy to respect
context. The refined final version is \*\*RMAGS v1.3: Reflexive
Auditable Governance Protocol\*\*---a POSG-based standard with sparse
hypergraph interactions (log-aggregated exposure with sampling caps),
Dirichlet-Bayesian updates (non-depreciable floors), multi-objective
regret (stability over \\mathcal{W}, worst-case intervals), Proposal
Auditor (KL-bounded counterfactuals with human veto), pattern library
(procedural inclusivity, consensus deprecation via Efficacy Tracker),
minimal schemas (as in v1.1, plus Update Log), and a scoped meta-layer
(regret-applied to framework evolutions). It outputs stable decisions
with traceable residuals, emphasizing artifact-driven accountability.
\*\*Fastest Path to Validation\*\*: 1. \*\*Schema and Artifact Prep (1
week)\*\*: Finalize JSON schemas (Case/ScoreReport with hyperedge
fields) and 5 templates in a GitHub repo; include examples for Core-6
using sparse hypergraphs. 2. \*\*Core Mechanics Implementation (1-2
weeks)\*\*: Code regret/exposure/KL functions in Python (extend v0.9
sketch with NetworkX for hypergraphs); test on synthetic data for
stability (e.g., \<5% variance threshold). 3. \*\*Retrospective
Backtesting (2 weeks)\*\*: Run \"as-of\" on 8-12 cases (stratified
AI/policy), with raters scoring kappa (\>0.7), recall/false positives,
and meta-layer applicability; hold out 30% for update validation. 4.
\*\*Pilot and Iteration (ongoing, starting week 4)\*\*: Deploy to 2
teams for prospective workflows; measure artifact completeness (\>85%),
time-to-flag, and deprecation efficacy; publish eval pack with
code/schemas/disagreements for community review, refining via feedback
for v1.4.

Below is a concrete, implementable **RMAGS v1.3** package: (1) a crisp
protocol spec, (2) minimal **JSON Schemas** for Case and ScoreReport,
(3) five **artifact templates** (fillable), and (4) the core computation
definitions (robust regret, sparse hypergraph exposure, KL/variance
auditing) expressed in implementable terms.

RMAGS v1.3 protocol spec (implementation-ready)
-----------------------------------------------

### A. Constraint set and typing

-   **Core-6 (mandatory in every Case):**\
    > 1 Contested objectives, 2 Partial observability, 3 Strategic
    > behavior, 4 Goodhart pressure, 5 Tail-risk dominance, 6
    > Legitimacy/procedural constraints

-   **Adaptive-5 (must be assessed; may be "inactive" only with explicit
    > evidence + recheck triggers):**\
    > 7 Distribution shift, 8 Implementation capacity, 9 Path
    > dependence/irreversibility, 10 Delayed/confounded feedback, 11
    > Scalability/coordination thresholds

### B. Interaction model (sparse hypergraph)

-   Use **directed pairwise edges** plus a **sparse set of triad
    > hyperedges** (triads only when activated by case evidence).

-   Each edge/hyperedge stores a **Dirichlet posterior over ordinal
    > strength** {0,1,2}; compute expected strength as E\[M\].

### C. Outputs required from RMAGS (ScoreReport)

-   recommended\_actions (1--3 actions permitted)

-   regret\_interval (e.g., 10th--90th percentile) and stability\_flag

-   evidence\_completeness and artifact quality notes

-   legitimacy\_status (pass/conditional/fail)

-   exposure\_interval with mandatory-review triggers

-   residual\_risks (non-empty by schema)

-   approvals (human sign-off + AI provenance if used)

### D. Meta-layer (scoped)

-   RMAGS self-applies **only to major protocol updates** (schema
    > changes, scoring rule changes, deprecation rules). Each update
    > requires an UpdateLogEntry with rationale, stakeholder sign-off,
    > and regression evaluation on held-out cases.

1) JSON Schema: RMAGS.Case.v1.3
-------------------------------

{

\"\$schema\": \"https://json-schema.org/draft/2020-12/schema\",

\"\$id\": \"RMAGS.Case.v1.3.schema.json\",

\"title\": \"RMAGS Case v1.3\",

\"type\": \"object\",

\"required\": \[

\"case\_id\",

\"as\_of\_date\",

\"domain\",

\"controller\",

\"system\_scope\",

\"stakeholders\",

\"objective\_portfolio\",

\"hard\_constraints\",

\"actions\",

\"observation\_model\",

\"scenario\_pack\",

\"constraint\_assessment\",

\"interaction\_model\",

\"required\_artifacts\",

\"update\_log\"

\],

\"properties\": {

\"case\_id\": { \"type\": \"string\", \"minLength\": 3 },

\"as\_of\_date\": { \"type\": \"string\", \"format\": \"date\" },

\"domain\": { \"type\": \"string\", \"enum\": \[\"ai\", \"policy\",
\"hybrid\"\] },

\"controller\": {

\"type\": \"object\",

\"required\": \[\"name\", \"type\"\],

\"properties\": {

\"name\": { \"type\": \"string\" },

\"type\": { \"type\": \"string\", \"enum\": \[\"org\_team\", \"agency\",
\"coalition\", \"other\"\] },

\"accountability\_owner\": { \"type\": \"string\" }

},

\"additionalProperties\": false

},

\"system\_scope\": {

\"type\": \"object\",

\"required\": \[\"summary\", \"jurisdiction\_or\_market\",
\"time\_horizon\_days\"\],

\"properties\": {

\"summary\": { \"type\": \"string\" },

\"jurisdiction\_or\_market\": { \"type\": \"string\" },

\"time\_horizon\_days\": { \"type\": \"integer\", \"minimum\": 1 },

\"reversibility\_claim\": { \"type\": \"string\" }

},

\"additionalProperties\": false

},

\"stakeholders\": {

\"type\": \"array\",

\"minItems\": 1,

\"items\": {

\"type\": \"object\",

\"required\": \[\"group\", \"role\"\],

\"properties\": {

\"group\": { \"type\": \"string\" },

\"role\": { \"type\": \"string\", \"enum\": \[\"affected\",
\"operator\", \"regulator\", \"partner\", \"other\"\] },

\"notes\": { \"type\": \"string\" }

},

\"additionalProperties\": false

}

},

\"objective\_portfolio\": {

\"type\": \"object\",

\"required\": \[\"objectives\", \"tradeoff\_notes\"\],

\"properties\": {

\"objectives\": {

\"type\": \"array\",

\"minItems\": 1,

\"items\": {

\"type\": \"object\",

\"required\": \[\"name\", \"kind\"\],

\"properties\": {

\"name\": { \"type\": \"string\" },

\"kind\": { \"type\": \"string\", \"enum\": \[\"maximize\",
\"minimize\", \"satisfy\_floor\"\] },

\"metric\": { \"type\": \"string\" },

\"floor\_or\_target\": { \"type\": \[\"number\", \"null\"\] },

\"notes\": { \"type\": \"string\" }

},

\"additionalProperties\": false

}

},

\"tradeoff\_notes\": { \"type\": \"string\" }

},

\"additionalProperties\": false

},

\"hard\_constraints\": {

\"type\": \"array\",

\"minItems\": 1,

\"items\": {

\"type\": \"object\",

\"required\": \[\"name\", \"type\", \"test\_procedure\"\],

\"properties\": {

\"name\": { \"type\": \"string\" },

\"type\": { \"type\": \"string\", \"enum\": \[\"legal\", \"rights\",
\"safety\_floor\", \"budget\", \"operational\", \"other\"\] },

\"test\_procedure\": { \"type\": \"string\" },

\"non\_depreciable\": { \"type\": \"boolean\", \"default\": false }

},

\"additionalProperties\": false

}

},

\"actions\": {

\"type\": \"array\",

\"minItems\": 1,

\"items\": {

\"type\": \"object\",

\"required\": \[\"action\_id\", \"name\", \"description\",
\"feasibility\"\],

\"properties\": {

\"action\_id\": { \"type\": \"string\" },

\"name\": { \"type\": \"string\" },

\"description\": { \"type\": \"string\" },

\"feasibility\": {

\"type\": \"object\",

\"required\": \[\"status\", \"notes\"\],

\"properties\": {

\"status\": { \"type\": \"string\", \"enum\": \[\"feasible\",
\"infeasible\", \"unknown\"\] },

\"notes\": { \"type\": \"string\" },

\"blocked\_by\_constraints\": { \"type\": \"array\", \"items\": {
\"type\": \"string\" } }

},

\"additionalProperties\": false

}

},

\"additionalProperties\": false

}

},

\"observation\_model\": {

\"type\": \"object\",

\"required\": \[\"signals\", \"lags\_days\", \"known\_biases\"\],

\"properties\": {

\"signals\": { \"type\": \"array\", \"items\": { \"type\": \"string\" },
\"minItems\": 1 },

\"lags\_days\": { \"type\": \"object\", \"additionalProperties\": {
\"type\": \"integer\", \"minimum\": 0 } },

\"known\_biases\": { \"type\": \"array\", \"items\": { \"type\":
\"string\" } },

\"attribution\_limits\": { \"type\": \"string\" }

},

\"additionalProperties\": false

},

\"scenario\_pack\": {

\"type\": \"object\",

\"required\": \[\"taxonomy\_coverage\", \"scenarios\", \"priors\",
\"provenance\"\],

\"properties\": {

\"taxonomy\_coverage\": {

\"type\": \"object\",

\"required\": \[\"drift\_regimes\", \"adversary\_types\",
\"capacity\_levels\", \"coordination\_scales\"\],

\"properties\": {

\"drift\_regimes\": { \"type\": \"array\", \"items\": { \"type\":
\"string\" }, \"minItems\": 1 },

\"adversary\_types\": { \"type\": \"array\", \"items\": { \"type\":
\"string\" }, \"minItems\": 1 },

\"capacity\_levels\": { \"type\": \"array\", \"items\": { \"type\":
\"string\" }, \"minItems\": 1 },

\"coordination\_scales\": { \"type\": \"array\", \"items\": { \"type\":
\"string\" }, \"minItems\": 1 }

},

\"additionalProperties\": false

},

\"scenarios\": {

\"type\": \"array\",

\"minItems\": 1,

\"items\": {

\"type\": \"object\",

\"required\": \[\"scenario\_id\", \"description\", \"assumptions\",
\"weight\"\],

\"properties\": {

\"scenario\_id\": { \"type\": \"string\" },

\"description\": { \"type\": \"string\" },

\"assumptions\": { \"type\": \"array\", \"items\": { \"type\":
\"string\" } },

\"weight\": { \"type\": \"number\", \"minimum\": 0 }

},

\"additionalProperties\": false

}

},

\"priors\": {

\"type\": \"object\",

\"properties\": {

\"notes\": { \"type\": \"string\" },

\"elicitation\_method\": { \"type\": \"string\" }

},

\"additionalProperties\": true

},

\"provenance\": {

\"type\": \"object\",

\"required\": \[\"generated\_by\", \"human\_signoff\"\],

\"properties\": {

\"generated\_by\": { \"type\": \"string\", \"enum\": \[\"human\",
\"ai\_assisted\", \"mixed\"\] },

\"ai\_details\": { \"type\": \"object\" },

\"human\_signoff\": {

\"type\": \"object\",

\"required\": \[\"approver\", \"date\"\],

\"properties\": {

\"approver\": { \"type\": \"string\" },

\"date\": { \"type\": \"string\", \"format\": \"date\" },

\"rationale\": { \"type\": \"string\" }

},

\"additionalProperties\": false

}

},

\"additionalProperties\": false

}

},

\"additionalProperties\": false

},

\"constraint\_assessment\": {

\"type\": \"object\",

\"required\": \[\"core6\", \"adaptive5\"\],

\"properties\": {

\"core6\": {

\"type\": \"array\",

\"minItems\": 6,

\"maxItems\": 6,

\"items\": { \"\$ref\": \"\#/\$defs/constraintEntry\" }

},

\"adaptive5\": {

\"type\": \"array\",

\"minItems\": 5,

\"maxItems\": 5,

\"items\": { \"\$ref\": \"\#/\$defs/constraintEntry\" }

}

},

\"additionalProperties\": false

},

\"interaction\_model\": {

\"type\": \"object\",

\"required\": \[\"pair\_edges\", \"triad\_hyperedges\",
\"calibration\"\],

\"properties\": {

\"pair\_edges\": {

\"type\": \"array\",

\"items\": { \"\$ref\": \"\#/\$defs/pairEdge\" }

},

\"triad\_hyperedges\": {

\"type\": \"array\",

\"items\": { \"\$ref\": \"\#/\$defs/triadHyperedge\" }

},

\"calibration\": {

\"type\": \"object\",

\"required\": \[\"alpha\_default\", \"exposure\_cap\"\],

\"properties\": {

\"alpha\_default\": { \"type\": \"number\", \"default\": 1.0 },

\"exposure\_cap\": { \"type\": \"number\", \"minimum\": 1.0,
\"default\": 20.0 }

},

\"additionalProperties\": false

}

},

\"additionalProperties\": false

},

\"required\_artifacts\": {

\"type\": \"array\",

\"minItems\": 5,

\"items\": {

\"type\": \"object\",

\"required\": \[\"artifact\_type\", \"status\"\],

\"properties\": {

\"artifact\_type\": {

\"type\": \"string\",

\"enum\": \[

\"stop\_rule\",

\"monitoring\_plan\",

\"assumption\_registry\",

\"scenario\_pack\_template\",

\"accountability\_log\"

\]

},

\"status\": { \"type\": \"string\", \"enum\": \[\"missing\", \"draft\",
\"complete\"\] },

\"location\": { \"type\": \"string\" },

\"quality\_notes\": { \"type\": \"string\" }

},

\"additionalProperties\": false

}

},

\"update\_log\": {

\"type\": \"array\",

\"minItems\": 1,

\"items\": { \"\$ref\": \"\#/\$defs/updateLogEntry\" }

}

},

\"\$defs\": {

\"constraintEntry\": {

\"type\": \"object\",

\"required\": \[\"constraint\_id\", \"name\", \"status\", \"evidence\",
\"recheck\_triggers\"\],

\"properties\": {

\"constraint\_id\": { \"type\": \"integer\", \"minimum\": 1,
\"maximum\": 11 },

\"name\": { \"type\": \"string\" },

\"status\": { \"type\": \"string\", \"enum\": \[\"active\",
\"inactive\_with\_evidence\", \"unknown\"\] },

\"evidence\": { \"type\": \"array\", \"items\": { \"type\": \"string\" }
},

\"recheck\_triggers\": { \"type\": \"array\", \"items\": { \"type\":
\"string\" } }

},

\"additionalProperties\": false

},

\"pairEdge\": {

\"type\": \"object\",

\"required\": \[\"from\", \"to\", \"active\", \"dirichlet\_beta\",
\"alpha\"\],

\"properties\": {

\"from\": { \"type\": \"integer\", \"minimum\": 1, \"maximum\": 11 },

\"to\": { \"type\": \"integer\", \"minimum\": 1, \"maximum\": 11 },

\"active\": { \"type\": \"boolean\" },

\"dirichlet\_beta\": {

\"type\": \"array\",

\"minItems\": 3,

\"maxItems\": 3,

\"items\": { \"type\": \"number\", \"minimum\": 0 }

},

\"alpha\": { \"type\": \"number\", \"minimum\": 0 }

},

\"additionalProperties\": false

},

\"triadHyperedge\": {

\"type\": \"object\",

\"required\": \[\"nodes\", \"amplifies\", \"active\",
\"dirichlet\_beta\", \"alpha\"\],

\"properties\": {

\"nodes\": {

\"type\": \"array\",

\"minItems\": 3,

\"maxItems\": 3,

\"items\": { \"type\": \"integer\", \"minimum\": 1, \"maximum\": 11 }

},

\"amplifies\": { \"type\": \"integer\", \"minimum\": 1, \"maximum\": 11
},

\"active\": { \"type\": \"boolean\" },

\"dirichlet\_beta\": {

\"type\": \"array\",

\"minItems\": 3,

\"maxItems\": 3,

\"items\": { \"type\": \"number\", \"minimum\": 0 }

},

\"alpha\": { \"type\": \"number\", \"minimum\": 0 },

\"evidence\_gate\": { \"type\": \"array\", \"items\": { \"type\":
\"string\" } }

},

\"additionalProperties\": false

},

\"updateLogEntry\": {

\"type\": \"object\",

\"required\": \[\"date\", \"kind\", \"rationale\", \"approved\_by\"\],

\"properties\": {

\"date\": { \"type\": \"string\", \"format\": \"date\" },

\"kind\": {

\"type\": \"string\",

\"enum\": \[\"case\_edit\", \"prior\_tweak\",
\"scenario\_pack\_revision\", \"interaction\_update\",
\"major\_framework\_update\"\]

},

\"rationale\": { \"type\": \"string\" },

\"approved\_by\": { \"type\": \"string\" },

\"diff\_summary\": { \"type\": \"string\" }

},

\"additionalProperties\": false

}

},

\"additionalProperties\": false

}

2) JSON Schema: RMAGS.ScoreReport.v1.3
--------------------------------------

{

\"\$schema\": \"https://json-schema.org/draft/2020-12/schema\",

\"\$id\": \"RMAGS.ScoreReport.v1.3.schema.json\",

\"title\": \"RMAGS ScoreReport v1.3\",

\"type\": \"object\",

\"required\": \[

\"case\_id\",

\"generated\_on\",

\"recommended\_actions\",

\"regret\_interval\",

\"stability\_flag\",

\"evidence\_completeness\",

\"legitimacy\_status\",

\"exposure\_interval\",

\"mandatory\_review\_triggers\",

\"residual\_risks\",

\"approvals\",

\"pattern\_library\_versions\"

\],

\"properties\": {

\"case\_id\": { \"type\": \"string\" },

\"generated\_on\": { \"type\": \"string\", \"format\": \"date-time\" },

\"recommended\_actions\": {

\"type\": \"array\",

\"minItems\": 1,

\"maxItems\": 3,

\"items\": { \"type\": \"string\" }

},

\"regret\_interval\": {

\"type\": \"object\",

\"required\": \[\"p10\", \"p50\", \"p90\", \"units\"\],

\"properties\": {

\"p10\": { \"type\": \"number\" },

\"p50\": { \"type\": \"number\" },

\"p90\": { \"type\": \"number\" },

\"units\": { \"type\": \"string\" },

\"notes\": { \"type\": \"string\" }

},

\"additionalProperties\": false

},

\"stability\_flag\": { \"type\": \"string\", \"enum\": \[\"stable\",
\"unstable\"\] },

\"stability\_notes\": { \"type\": \"string\" },

\"evidence\_completeness\": {

\"type\": \"object\",

\"required\": \[\"score\_0\_1\", \"missing\_artifacts\",
\"quality\_notes\"\],

\"properties\": {

\"score\_0\_1\": { \"type\": \"number\", \"minimum\": 0, \"maximum\": 1
},

\"missing\_artifacts\": { \"type\": \"array\", \"items\": { \"type\":
\"string\" } },

\"quality\_notes\": { \"type\": \"string\" }

},

\"additionalProperties\": false

},

\"legitimacy\_status\": {

\"type\": \"object\",

\"required\": \[\"status\", \"rationale\"\],

\"properties\": {

\"status\": { \"type\": \"string\", \"enum\": \[\"pass\",
\"conditional\", \"fail\"\] },

\"rationale\": { \"type\": \"string\" },

\"non\_depreciable\_constraints\_respected\": { \"type\": \"boolean\" }

},

\"additionalProperties\": false

},

\"exposure\_interval\": {

\"type\": \"object\",

\"required\": \[\"p10\", \"p50\", \"p90\", \"cap\"\],

\"properties\": {

\"p10\": { \"type\": \"number\" },

\"p50\": { \"type\": \"number\" },

\"p90\": { \"type\": \"number\" },

\"cap\": { \"type\": \"number\" },

\"notes\": { \"type\": \"string\" }

},

\"additionalProperties\": false

},

\"mandatory\_review\_triggers\": {

\"type\": \"array\",

\"items\": { \"type\": \"string\" }

},

\"proposal\_audit\": {

\"type\": \"object\",

\"properties\": {

\"kl\_divergence\": {

\"type\": \"object\",

\"required\": \[\"p50\", \"p90\", \"threshold\"\],

\"properties\": {

\"p50\": { \"type\": \"number\" },

\"p90\": { \"type\": \"number\" },

\"threshold\": { \"type\": \"number\" }

},

\"additionalProperties\": false

},

\"decision\_variance\": {

\"type\": \"object\",

\"required\": \[\"top\_action\_flip\_rate\", \"stability\_flip\_rate\",
\"thresholds\"\],

\"properties\": {

\"top\_action\_flip\_rate\": { \"type\": \"number\", \"minimum\": 0,
\"maximum\": 1 },

\"stability\_flip\_rate\": { \"type\": \"number\", \"minimum\": 0,
\"maximum\": 1 },

\"thresholds\": { \"type\": \"object\" }

},

\"additionalProperties\": false

},

\"human\_veto\": {

\"type\": \"object\",

\"required\": \[\"used\", \"rationale\"\],

\"properties\": {

\"used\": { \"type\": \"boolean\" },

\"rationale\": { \"type\": \"string\" }

},

\"additionalProperties\": false

}

},

\"additionalProperties\": false

},

\"residual\_risks\": {

\"type\": \"array\",

\"minItems\": 1,

\"items\": {

\"type\": \"object\",

\"required\": \[\"risk\", \"why\_unresolved\", \"monitoring\_signal\"\],

\"properties\": {

\"risk\": { \"type\": \"string\" },

\"why\_unresolved\": { \"type\": \"string\" },

\"monitoring\_signal\": { \"type\": \"string\" },

\"mitigation\_if\_triggered\": { \"type\": \"string\" }

},

\"additionalProperties\": false

}

},

\"approvals\": {

\"type\": \"object\",

\"required\": \[\"decision\_owner\", \"signed\_off\_on\"\],

\"properties\": {

\"decision\_owner\": { \"type\": \"string\" },

\"signed\_off\_on\": { \"type\": \"string\", \"format\": \"date\" },

\"notes\": { \"type\": \"string\" },

\"ai\_provenance\": { \"type\": \"object\" }

},

\"additionalProperties\": false

},

\"pattern\_library\_versions\": {

\"type\": \"array\",

\"items\": { \"type\": \"string\" },

\"minItems\": 1

}

},

\"additionalProperties\": false

}

3) Core computations (defined precisely)
----------------------------------------

### A. Robust regret with scalarization family

-   Filter to feasible actions first.

-   For each scenario s and weight vector w∈W, compute
    > Lw​(a,s)=w⊤ℓ(a,s).

-   Define L(a,s)=maxw∈W​Lw​(a,s).

-   Regret per action: regret(a,s)=L(a,s)−mina′​L(a′,s).

-   Robust regret distribution from scenario weights/posterior; report
    > \[p10,p50,p90\].

### B. Sparse hypergraph exposure (pair + triad)

For each active edge/hyperedge with Dirichlet β=\[β0​,β1​,β2​\],

E\[M\]=β0​+β1​+β2​0β0​+1β1​+2β2​​

Exposure samples:

Exposure=min(exp(∑α⋅E\[M\]),cap)

Compute interval by posterior sampling (draw categorical from
Dirichlet-normalized probabilities).

### C. Proposal variance (KL + decision flip rates)

-   Generate k scenario packs (different seeds/prompts/elicitation
    > variants).

-   Compute distributional divergence with **bounded KL** over aligned
    > scenario bins (taxonomy-defined bins):

    -   Use smoothing ϵ to avoid infinite KL.

-   Compute:

    -   top\_action\_flip\_rate across the k runs

    -   stability\_flip\_rate across the k runs\
        > Trigger mandatory review if KL or flip rates exceed
        > thresholds.

4) Five artifact templates (fillable, minimal)
----------------------------------------------

### 1) Stop Rule Template (YAML)

artifact\_type: stop\_rule

owner:

name: \"\"

role: \"\"

scope:

case\_id: \"\"

action\_ids: \[\"\"\] \# actions governed by this stop rule

stop\_conditions:

\- condition: \"\" \# e.g., \"p95 safety incident rate \> X for 48h\"

signal: \"\" \# link to monitoring signal

threshold: \"\"

window: \"\"

action\_on\_trigger: \"\" \# pause rollout / rollback / enforcement
surge

review\_cadence:

interval\_days: 7

reviewers: \[\"\", \"\"\]

appeals\_and\_exceptions:

allowed: true

process: \"\"

### 2) Monitoring Plan Template (YAML)

artifact\_type: monitoring\_plan

case\_id: \"\"

signals:

leading\_indicators:

\- name: \"\"

definition: \"\"

collection\_method: \"\"

lag\_days: 0

gaming\_risks: \"\"

anti\_goodhart\_design: \"\"

lagging\_indicators:

\- name: \"\"

definition: \"\"

thresholds:

\- signal\_name: \"\"

thresholds:

warn: \"\"

stop: \"\"

incident\_taxonomy:

categories: \[\"safety\", \"rights\", \"security\", \"fraud\",
\"operational\", \"reputation\", \"other\"\]

response\_playbook\_link: \"\"

### 3) Assumption Registry Template (YAML)

artifact\_type: assumption\_registry

case\_id: \"\"

assumptions:

\- id: A1

statement: \"\"

why\_needed: \"\"

how\_tested: \"\"

status: \"untested\|supported\|failed\"

failure\_impact: \"\"

fallback\_plan: \"\"

### 4) Scenario Pack Template (YAML)

artifact\_type: scenario\_pack\_template

case\_id: \"\"

taxonomy\_bins:

drift\_regimes: \[\"low\", \"medium\", \"high\"\]

adversary\_types: \[\"none\", \"opportunistic\", \"organized\"\]

capacity\_levels: \[\"strong\", \"moderate\", \"weak\"\]

coordination\_scales: \[\"local\", \"regional\", \"national\",
\"global\"\]

scenarios:

\- scenario\_id: S1

bin: { drift: \"low\", adversary: \"none\", capacity: \"strong\", scale:
\"local\" }

description: \"\"

assumptions: \[\"\"\]

weight: 0.10

generation\_provenance:

generated\_by: \"human\|ai\_assisted\|mixed\"

human\_signoff:

approver: \"\"

date: \"\"

rationale: \"\"

### 5) Accountability Log Template (YAML)

artifact\_type: accountability\_log

case\_id: \"\"

entries:

\- timestamp: \"\"

contributor: \"\"

action:
\"scenario\_edit\|prior\_tweak\|interaction\_update\|decision\_change\|artifact\_update\"

change\_summary: \"\"

ai\_used: true

ai\_provenance:

model: \"\"

prompt\_hash: \"\"

output\_hash: \"\"

approved\_by: \"\"

rationale: \"\"

5) Practical guardrails (to prevent Goodharting RMAGS itself)
-------------------------------------------------------------

-   **Dashboard rule:** never show a single "overall score" without the
    > tuple components (regret interval, stability, legitimacy, evidence
    > completeness, exposure interval).

-   **Non-depreciation rule:** rights/legitimacy floors cannot be
    > weakened without major\_framework\_update + stakeholder sign-off +
    > held-out regression pass.

-   **Held-out evaluation rule:** any update to interaction priors or
    > calibration must demonstrate non-worsening on reserved cases.

6) Validation protocol (v1.3-compatible, minimal and defensible)
----------------------------------------------------------------

1.  **As-of retrospective pack** (8--12 cases): each Case must specify
    > as\_of\_date and only include evidence available before outcome
    > onset.

2.  **Two-rater scoring**: treat disagreement as a schema/rubric defect
    > to fix; capture diffs as UpdateLog entries.

3.  **Train/eval split** for interaction updates: update priors on
    > train; report metrics on held-out.

4.  **Pilot success metrics**: artifact completeness, time-to-flag,
    > time-to-mitigate, decision stability under scenario variation.
