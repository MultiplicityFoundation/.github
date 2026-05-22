---
slug: instructions
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Instructions.md
  last_synced: '2026-03-20T17:17:21.745660Z'
---

I**nstallation and testing instructions** for the QARI Runner H Agent,
suitable for inclusion in your README.md or submission post:

**⚙️ QARI Runner H Agent -- Setup & Testing Guide**
---------------------------------------------------

This guide walks you through cloning, configuring, running, and testing
the QARI AI agent prototype designed for the Runner H challenge.

### **📁 1. Clone the Repository**

bash

CopyEdit

git clone https://github.com/\<your-org\>/Q-Calculator.git

cd Q-Calculator/qari-runnerh-agent

### **🔧 2. Create and Activate Virtual Environment (Optional but Recommended)**

bash

CopyEdit

python -m venv venv

source venv/bin/activate \# Use \`venv\\Scripts\\activate\` on Windows

### **📦 3. Install Dependencies**

bash

CopyEdit

pip install -r requirements.txt

If requirements.txt is missing, simply install:

bash

CopyEdit

pip install pytest

### **🔐 4. Configure Environment Variables**

Duplicate and edit the sample .env file:

bash

CopyEdit

cp .env.example .env

\# Then edit .env to insert your API keys or configuration

### **▶️ 5. Run the Agent**

bash

CopyEdit

python agent/main.py

This will process a sample prompt and show ethics scoring and recursion
output.

### **🧪 6. Run Unit Tests**

bash

CopyEdit

pytest test/

Tests cover:

-   Ethics tensor scoring

-   Recursive logic loop

-   Prime-indexed encoding

### **🐳 7. Run with Docker (Optional)**

Build and run the container:

bash

CopyEdit

docker build -t qari-agent .

docker run -it \--rm \--env-file .env qari-agent

### **🧠 8. Testing Sample Prompts**

To simulate multiple prompt cases:

bash

CopyEdit

python agent/main.py \--file test/mock\_input.json

This will evaluate multiple inputs and output logs to the console or
file (optional enhancement).

### **📤 9. Submitting to Runner H**

-   Ensure runnerh.config.json is complete

-   Include screenshots or logs in your submission post

-   Reference prompt-design.md and qari-overview.pdf in your explanation
