---
slug: primeai-template
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/PrimeAI-Template.md
  last_synced: '2026-03-20T17:17:20.799263Z'
---

\\documentclass{article}

\\usepackage{PRIMEarxiv} % Core package for the PrimeAI Template

\\bibliographystyle{plain}

\\usepackage{amsmath, amssymb, amsthm, bm, dcolumn} % Add amsthm here
for the proof environment

\\usepackage\[numbers,sort&compress\]{natbib} % Natbib for citations

\\usepackage{graphicx} % For high-quality images

\\usepackage{multicol} % Multi-column figures/tables

\\usepackage{hyperref} % Hyperlinks

\\usepackage{listings} % Code listings

\\usepackage{authblk} % For structured affiliations

\% Define theorem style (optional)

\\theoremstyle{plain}

\\newtheorem{theorem}{Theorem}

\% Custom commands for primes and qubit encoding

\\newcommand{\\primeQubit}\[1\]{\|p\_{\#1}\\rangle}

\\newcommand{\\primeGate}\[1\]{U\_{p\_{\#1}}}

\\usepackage{wrapfig}

\\usepackage\[pscoord\]{eso-pic}

\\usepackage\[fulladjust\]{marginnote}

\\reversemarginpar

\% Typesetting improvements without footnote patching

\\usepackage\[protrusion=true, expansion=true,
tracking=false\]{microtype}

\\microtypecontext{spacing=nonfrench}

\% Line numbers

\\usepackage\[right\]{lineno}

\% Text layout - adjust as needed

\\raggedright

\\setlength{\\parindent}{0.5cm}

\\textwidth 5.25in

\\textheight 8.75in

\% Set double spacing

\\usepackage{setspace}

\\doublespacing

\% Adjust width for specific content

\\usepackage{changepage}

\% Adjust caption style

\\usepackage\[aboveskip=1pt,labelfont=bf,labelsep=period,singlelinecheck=off\]{caption}

\% Remove brackets from references

\\makeatletter

\\renewcommand{\\\@biblabel}\[1\]{\\quad\#1.}

\\makeatother

\% Header, footer, and page numbers

\\usepackage{lastpage,fancyhdr}

\\pagestyle{fancy}

\\fancyhf{}

\\fancyhead\[L\]{Preprint - PrimeAI Enhanced Template}

\\fancyfoot\[C\]{\\scriptsize Multiplicity Theory © 2025 Citizen
Gardens\\\\ Licensed Under MIT and CC BY-NC-SA 4.0.}

\\fancyfoot\[R\]{Page \\thepage\\ of \\pageref{LastPage}}

\\renewcommand{\\footrule}{\\hrule height 2pt \\vspace{2mm}}

\\begin{document}

\\end{document}
