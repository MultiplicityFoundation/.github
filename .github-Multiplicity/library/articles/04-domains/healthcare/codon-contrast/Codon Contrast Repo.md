---
slug: codon-contrast-repo
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/healthcare/codon-contrast/Codon Contrast Repo.md
  last_synced: '2026-03-20T17:17:18.826341Z'
---

here's a clean, CI-ready repo scaffold. Drop your two working modules
into the marked files and push.

codon-contrast/

├─ README.md

├─ LICENSE

├─ pyproject.toml

├─ .gitignore

├─ Makefile

├─ CITATION.cff

├─ src/

│ └─ codon\_contrast/

│ ├─ \_\_init\_\_.py

│ ├─ harness.py \# put your validated codon\_contrast\_harness.py here

│ ├─ integration.py \# put your cleaned codon\_integration.py here

│ ├─ edits.py \# shared edit types/helpers (optional)

│ └─ cli.py \# thin CLI wrapper

├─ tests/

│ ├─ test\_harness\_fwht.py

│ ├─ test\_flows\_math.py

│ └─ test\_integration\_gc2.py

├─ scripts/

│ ├─ validate.sh

│ └─ bench.sh

├─ examples/

│ └─ demo\_notebook.ipynb \# optional; may omit

└─ .github/

└─ workflows/

└─ ci.yml

**File contents**
-----------------

### **README.md**

\# codon-contrast

Walsh--Hadamard codon contrasts + fast flow metrics with prime-codon
integration.

\#\# Quickstart

\`\`\`bash

python3 -m venv venv

source venv/bin/activate

pip install -U pip

pip install -e .\[bench\] \# installs numpy and sklearn extra

**Run**
-------

\# validation from harness

python -m codon\_contrast.harness

\# integration test

python -m codon\_contrast.integration \--integrate-test

\# benchmark (needs scikit-learn)

python -m codon\_contrast.integration \--benchmark

**Tests**
---------

pip install -e .\[dev\]

pytest -q

\#\#\# LICENSE

\`\`\`text

MIT License

Copyright (c) 2025 \...

Permission is hereby granted, free of charge, to any person obtaining a
copy

\...

### **.gitignore**

\# python

\_\_pycache\_\_/

\*.pyc

\*.pyo

\*.pyd

\*.egg-info/

.venv/

venv/

.env

.ipynb\_checkpoints

.dist/

.build/

.pytest\_cache/

.coverage

htmlcov/

\# OS

.DS\_Store

Thumbs.db

### **Makefile**

.PHONY: venv install dev test bench lint fmt ci

PY ?= python3

venv:

\$(PY) -m venv venv

install:

. venv/bin/activate && pip install -U pip && pip install -e .

dev:

. venv/bin/activate && pip install -e .\[dev,bench\]

test:

. venv/bin/activate && pytest -q

bench:

. venv/bin/activate && python -m codon\_contrast.integration
\--benchmark

fmt:

. venv/bin/activate && ruff format src tests

lint:

. venv/bin/activate && ruff check src tests

ci: lint test bench

### **pyproject.toml**

\[project\]

name = \"codon-contrast\"

version = \"0.1.0\"

description = \"Walsh--Hadamard codon contrasts and fast codon-flow
metrics\"

readme = \"README.md\"

requires-python = \"\>=3.9\"

license = { text = \"MIT\" }

authors = \[{ name = \"Your Name\" }\]

dependencies = \[\"numpy\>=1.22\"\]

\[project.optional-dependencies\]

bench = \[\"scikit-learn\>=1.1\"\]

dev = \[\"pytest\>=7\", \"ruff\>=0.5\"\]

\[project.urls\]

homepage = \"https://example.com\"

repository = \"https://example.com/repo\"

\[tool.ruff\]

line-length = 100

### **src/codon\_contrast/init.py**

from .harness import (

walsh\_hadamard\_contrasts,

walsh\_hadamard\_contrasts\_norm,

analyze\_codon\_flows\_fast,

Sub,

idx\_to\_digits,

digits\_to\_idx,

run\_validation\_suite, \# if you export it in harness.py

)

from .integration import (

CodonSequence,

Contribution,

create\_contribution\_from\_edits,

)

\_\_all\_\_ = \[

\"walsh\_hadamard\_contrasts\",

\"walsh\_hadamard\_contrasts\_norm\",

\"analyze\_codon\_flows\_fast\",

\"Sub\",

\"idx\_to\_digits\",

\"digits\_to\_idx\",

\"run\_validation\_suite\",

\"CodonSequence\",

\"Contribution\",

\"create\_contribution\_from\_edits\",

\]

### **src/codon\_contrast/harness.py**

\# PLACE YOUR VERIFIED codon\_contrast\_harness.py CONTENT HERE

\# Keep function names stable:

\# - walsh\_hadamard\_contrasts

\# - walsh\_hadamard\_contrasts\_norm

\# - analyze\_codon\_flows\_fast

\# - Sub, idx\_to\_digits, digits\_to\_idx

\# - run\_validation\_suite

if \_\_name\_\_ == \"\_\_main\_\_\":

\# default to validation

ok = run\_validation\_suite()

raise SystemExit(0 if ok else 1)

### **src/codon\_contrast/integration.py**

\# PLACE YOUR CLEANED codon\_integration.py CONTENT HERE

\# It must expose:

\# - CodonSequence, Contribution, create\_contribution\_from\_edits

\# - CLI flags: \--integrate-test, \--benchmark, \--validate

if \_\_name\_\_ == \"\_\_main\_\_\":

import sys

\# delegate to its own CLI (already implemented in your file)

### **src/codon\_contrast/edits.py (optional)**

from dataclasses import dataclass

from typing import Tuple

\@dataclass(frozen=True)

class Sub:

old: int

new: int

pos: int = -1

\# Stubs for future Ins/Del if you split types

\@dataclass(frozen=True)

class Ins:

pos: int

payload: Tuple\[int, \...\]

\@dataclass(frozen=True)

class Del:

pos: int

length: int

payload\_old: Tuple\[int, \...\]

### **src/codon\_contrast/cli.py**

import argparse

from . import run\_validation\_suite

from .integration import run\_integration\_test, ContrastBenchmark

def main():

p = argparse.ArgumentParser(\"codon-contrast\")

p.add\_argument(\"\--validate\", action=\"store\_true\")

p.add\_argument(\"\--integrate-test\", action=\"store\_true\")

p.add\_argument(\"\--benchmark\", action=\"store\_true\")

args = p.parse\_args()

if args.validate:

ok = run\_validation\_suite()

raise SystemExit(0 if ok else 1)

if args.integrate\_test:

run\_integration\_test(); raise SystemExit(0)

if args.benchmark:

bm = ContrastBenchmark(); ok = bm.run\_benchmark()

raise SystemExit(0 if ok else 1)

\# default

run\_integration\_test(); raise SystemExit(0)

if \_\_name\_\_ == \"\_\_main\_\_\":

main()

### **tests/test\_harness\_fwht.py**

import numpy as np

from codon\_contrast import walsh\_hadamard\_contrasts\_norm

def test\_gc3\_bias\_sign():

dh = np.zeros(64)

for i in range(64):

if (i & 3) in (1,2):

dh\[i\] = 1.0

c = walsh\_hadamard\_contrasts\_norm(dh)

assert c\[\"GC3\"\] \> 0.1

### **tests/test\_flows\_math.py**

import numpy as np

from codon\_contrast import Sub, idx\_to\_digits, digits\_to\_idx

from codon\_contrast import analyze\_codon\_flows\_fast

def make\_sub(old\_idx, pos, new\_base):

d = list(idx\_to\_digits(old\_idx))

mapping = {\"A\":0,\"C\":1,\"G\":2,\"T\":3}

d\[pos\] = mapping\[new\_base\]

new = digits\_to\_idx(\*d)

return Sub(old=old\_idx, new=new, pos=pos)

def test\_transition\_ratio\_extremes():

\# all transitions at wobble

subs = \[\]

for old\_idx in range(64):

pos = 2

d = list(idx\_to\_digits(old\_idx))

base = \"ACGT\"\[d\[pos\]\]

new = \"G\" if base==\"A\" else \"A\" if base==\"G\" else \"T\" if
base==\"C\" else \"C\"

subs.append(make\_sub(old\_idx, pos, new))

m = analyze\_codon\_flows\_fast(subs)

assert m\[\"transition\_ratio\"\] == 1.0

assert m\[\"wobble\_transitions\"\] \>= 0.25

### **tests/test\_integration\_gc2.py**

import numpy as np

from codon\_contrast.integration import
create\_contribution\_from\_edits, CodonSequence, Sub

from math import log

def test\_gc2\_pair():

seq = CodonSequence(k=np.array(\[0,1,2,3,4,5\], dtype=np.uint8))

edits = \[Sub(old=0,new=4,pos=0), Sub(old=1,new=5,pos=1)\]

contrib = create\_contribution\_from\_edits(seq, edits,
actors=b\"\\x01\", timestamp=0)

dh = contrib.delta\_h

assert dh\[0\]==-1 and dh\[1\]==-1 and dh\[4\]==1 and dh\[5\]==1 and
dh.sum()==0

cn = contrib.contrasts\_norm

assert abs(cn\[\"GC2\"\] - 0.125) \< 1e-6

fl = contrib.flows

assert fl\[\"transition\_ratio\"\] == 0.0

assert fl\[\"wobble\_transitions\"\] == 0.0

assert abs(fl\[\"gc\_bias\"\] - 1.0) \< 1e-12

assert abs(fl\[\"flow\_entropy\"\] - log(2.0)) \< 1e-12

### **scripts/validate.sh**

\#!/usr/bin/env bash

set -euo pipefail

python -m codon\_contrast.harness

python -m codon\_contrast.integration \--integrate-test

### **scripts/bench.sh**

\#!/usr/bin/env bash

set -euo pipefail

python -m codon\_contrast.integration \--benchmark

### **.github/workflows/ci.yml**

name: CI

on: \[push, pull\_request\]

jobs:

test:

runs-on: ubuntu-latest

strategy:

matrix:

python-version: \[\'3.9\', \'3.11\'\]

steps:

\- uses: actions/checkout\@v4

\- uses: actions/setup-python\@v5

with:

python-version: \${{ matrix.python-version }}

\- run: pip install -e .\[dev,bench\]

\- run: pytest -q

\- run: python -m codon\_contrast.integration \--integrate-test

\- run: python -m codon\_contrast.integration \--benchmark

### **CITATION.cff (optional)**

cff-version: 1.2.0

message: \"If you use codon-contrast, please cite:\"

title: \"codon-contrast: Walsh--Hadamard codon contrasts and flow
metrics\"

authors:

\- family-names: YourLast

given-names: YourFirst

version: \"0.1.0\"

date-released: \"2025-11-06\"
