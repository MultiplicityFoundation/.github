---
slug: felix-sch-nbrodt
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "06-people/Felix Sch\xF6nbrodt.md"
  last_synced: '2026-03-20T17:17:13.478979Z'
---

\\documentclass{article}

\\usepackage{amsmath, amssymb, bm}

\\usepackage{graphicx}

\\usepackage{hyperref}

\\title{Integrating Schönbrodt F's Contributions with Multiplicity
Theory}

\\author{Your Name}

\\date{\\today}

\\begin{document}

\\maketitle

\\begin{abstract}

Schönbrodt F\'s work in psychological statistics, effect size
estimation, and open science practices emphasizes the dynamics of
statistical power, reproducibility, and meta-science. This paper
integrates Schönbrodt's contributions with Multiplicity Theory,
developing a mathematical framework for modeling effect size dynamics,
reproducibility feedback, and meta-analytic systems. Using
eigenvalue-driven models, tensor networks, and recursive feedback, the
synthesis provides insights into the emergent properties of research
ecosystems and their systemic coherence.

\\end{abstract}

\\section{Introduction}

Schönbrodt F's research focuses on improving statistical practices in
psychological science, emphasizing effect sizes, power analysis, and
reproducibility. Multiplicity Theory, with its focus on eigenvalue
dynamics, recursive feedback, and systemic interconnectivity, provides a
framework for modeling these interactions. This paper integrates
Schönbrodt's contributions with Multiplicity Theory to explore the
dynamic interplay between statistical inference, reproducibility, and
research ecosystems.

\\section{Effect Size Dynamics and Multiplicity}

Effect sizes (\\(d\\)) are central to assessing the strength of
relationships in psychological research. These can be modeled as dynamic
states within a system:

\\begin{equation}

d(t) = d\_0 + \\sum\_{i=1}\^N \\Delta d\_i e\^{-\\gamma\_i t},

\\end{equation}

where:

\\begin{itemize}

\\item \\(d\_0\\): Initial effect size estimate,

\\item \\(\\Delta d\_i\\): Changes in effect size due to sampling
variability or methodological adjustments,

\\item \\(\\gamma\_i\\): Damping coefficient representing attenuation
over time.

\\end{itemize}

\\subsection{Eigenvalue Representation of Effect Sizes}

Effect sizes across multiple studies can be represented as eigenvalues
of a dynamic system:

\\begin{equation}

M(t) = \\sum\_{i=1}\^N \\lambda\_i \\mu\_i e\^{i\\theta\_i(t)} \\cdot
v\_i,

\\end{equation}

where:

\\begin{itemize}

\\item \\(\\lambda\_i\\): Eigenvalues representing effect size
variability,

\\item \\(\\mu\_i\\): Multiplicity of studies contributing to each
effect,

\\item \\(e\^{i\\theta\_i(t)}\\): Phase evolution capturing temporal
coherence,

\\item \\(v\_i\\): Eigenvectors representing methodological
configurations.

\\end{itemize}

\\section{Statistical Power and Reproducibility}

Statistical power (\\(P\\)) determines the probability of detecting true
effects. Its dynamics are influenced by sample size, effect size, and
variability:

\\begin{equation}

P = 1 - \\Phi\\left(z\_\\alpha - \\frac{d \\sqrt{n}}{\\sigma}\\right),

\\end{equation}

where:

\\begin{itemize}

\\item \\(\\Phi\\): Standard normal cumulative distribution function,

\\item \\(z\_\\alpha\\): Critical value for significance level
\\(\\alpha\\),

\\item \\(d\\): Effect size,

\\item \\(n\\): Sample size,

\\item \\(\\sigma\\): Standard deviation.

\\end{itemize}

\\subsection{Feedback in Reproducibility}

Reproducibility (\\(R\\)) is influenced by statistical power, effect
size, and methodological rigor. Recursive feedback in reproducibility
can be modeled as:

\\begin{equation}

\\frac{dR}{dt} = F(P, \\mu, \\psi(t)),

\\end{equation}

where \\(F(P, \\mu, \\psi(t))\\) represents the coupling between power,
methodological multiplicity, and dynamic coherence.

\\section{Meta-Analysis and Multiplicity}

Meta-analyses aggregate effect sizes from multiple studies, providing an
overall estimate. These can be represented as weighted sums:

\\begin{equation}

d\_\\text{meta} = \\frac{\\sum\_{i=1}\^N w\_i d\_i}{\\sum\_{i=1}\^N
w\_i},

\\end{equation}

where:

\\begin{itemize}

\\item \\(w\_i\\): Weights based on study precision,

\\item \\(d\_i\\): Effect sizes from individual studies.

\\end{itemize}

\\subsection{Tensor Networks for Meta-Analysis}

The interactions between studies, effect sizes, and methodological
configurations can be represented using tensors:

\\begin{equation}

T\_{ijk} = \\sum\_{\\alpha, \\beta} E\_i\^\\alpha M\_j\^\\beta \\psi\_k,

\\end{equation}

where:

\\begin{itemize}

\\item \\(E\_i\^\\alpha\\): Effect size parameters,

\\item \\(M\_j\^\\beta\\): Methodological parameters,

\\item \\(\\psi\_k\\): Tensor weights representing systemic coherence.

\\end{itemize}

\\subsection{Systemic Resonance and Coherence}

The coherence of effect sizes across studies is modeled as:

\\begin{equation}

\\Psi\_\\text{res}(t) = \\sum\_{i,j} T\_{ij} \\cos(\\omega\_i t -
\\omega\_j t),

\\end{equation}

where \\(\\omega\_i\\) and \\(\\omega\_j\\) represent frequencies of
methodological changes or publication cycles.

\\section{Feedback Mechanisms in Research Ecosystems}

\\subsection{Recursive Feedback Loops}

Recursive feedback mechanisms adapt research ecosystems to improve
reproducibility and effect size accuracy:

\\begin{equation}

\\lambda\_i(t+1) = \\lambda\_i(t) + \\Delta \\lambda\_i \\cdot
e\^{-\\gamma t},

\\end{equation}

where \\(\\gamma\\) represents the resilience of methodological
frameworks.

\\subsection{Stability of Research Systems}

The stability of reproducibility in research systems is modeled as:

\\begin{equation}

R(t+1) = R(t) + \\Delta R \\cdot e\^{-\\delta t},

\\end{equation}

where \\(\\delta\\) represents the damping effect of systemic
variability.

\\section{Applications of the Schönbrodt-Multiplicity Framework}

\\subsection{Improving Reproducibility}

This framework can model:

\\begin{itemize}

\\item The dynamics of reproducibility under different methodological
conditions,

\\item The impact of statistical power on long-term research
reliability.

\\end{itemize}

\\subsection{Optimizing Meta-Analytic Practices}

Potential applications include:

\\begin{itemize}

\\item Designing meta-analytic frameworks for robust effect size
estimation,

\\item Identifying sources of heterogeneity in aggregated data.

\\end{itemize}

\\subsection{Enhancing Open Science Practices}

The integration supports:

\\begin{itemize}

\\item Modeling the adoption of open science practices,

\\item Predicting the impact of preregistration and data sharing on
research ecosystems.

\\end{itemize}

\\section{Conclusion}

Schönbrodt F's contributions, integrated with Multiplicity Theory,
provide a comprehensive mathematical framework for modeling
reproducibility, statistical power, and meta-analytic dynamics in
research ecosystems. By leveraging eigenvalue dynamics, tensor networks,
and recursive feedback, this synthesis advances our understanding of
effect size variability, methodological rigor, and systemic coherence in
scientific research.

\\bibliographystyle{plain}

\\bibliography{references}

\\end{document}
