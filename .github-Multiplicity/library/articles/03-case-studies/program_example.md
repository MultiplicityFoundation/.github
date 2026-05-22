---
slug: program-example
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/program_example.md
  last_synced: '2026-03-20T17:17:21.064000Z'
---

In this modified example, we define a dictionary called
celestial\_bodies that stores the properties of the Sun, Moon, and
Earth. Each celestial body is assigned a nucleus and a list of electrons
representing their interactions.

We create a quantum circuit and add quantum registers for each celestial
body using QuantumRegister(). The number of qubits for each register is
determined by the number of electrons associated with each celestial
body.

To represent the interactions between the celestial bodies, we apply
quantum gates to the corresponding qubits. In the example, we
demonstrate the interaction between the Sun and the Earth by applying
CNOT gates between their respective qubits.

Finally, we measure the quantum registers, simulate the quantum circuit
using the qasm\_simulator backend, and print the results.

The output of this program will be a dictionary (counts) that represents
the measurement outcomes of the quantum circuit. The keys of the
dictionary will be binary strings representing the states of the qubits,
and the values will be the number of times each state was observed
during the simulation.

This modified example shows how the Quantum Calculator program can be
adapted to represent interactions between celestial bodies like the Sun,
Moon, and Earth. The quantum circuit models the relationships and
influences between these entities, with the quantum gates representing
the nature of their interactions:

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister,
execute, Aer

*\# Define the celestial bodies and their corresponding quantum
registers*

celestial\_bodies = {

\'Sun\': {\'nucleus\': \'Energy\', \'electrons\': \[\'Radiates\',
\'Illuminates\', \'Gravitates\'\], \'prime\': 2},

\'Moon\': {\'nucleus\': \'Reflection\', \'electrons\': \[\'Orbits\',
\'Influences\'\], \'prime\': 3},

\'Earth\': {\'nucleus\': \'Life\', \'electrons\': \[\'Sustains\',
\'Evolves\', \'Adapts\'\], \'prime\': 5},

}

*\# Create a quantum circuit*

qc = QuantumCircuit()

*\# Create quantum registers for each celestial body*

for body, properties in celestial\_bodies.items():

qr = QuantumRegister(len(properties\[\'electrons\'\]), name=body)

qc.add\_register(qr)

*\# Apply quantum gates to represent interactions between celestial
bodies*

*\# Example: Interaction between the Sun and the Earth*

sun\_qubits = qc.qubits\[:3\] *\# Sun has 3 electrons*

earth\_qubits = qc.qubits\[5:8\] *\# Earth has 3 electrons*

*\# Apply interaction gates (e.g., CNOT) between the Sun and the Earth*

for i in range(3):

qc.cx(sun\_qubits\[i\], earth\_qubits\[i\])

*\# Measure the quantum registers*

cr = ClassicalRegister(len(qc.qubits), name=\'cr\')

qc.add\_register(cr)

qc.measure(qc.qubits, cr)

*\# Simulate the quantum circuit*

backend = Aer.get\_backend(\'qasm\_simulator\')

result = execute(qc, backend, shots=1024).result()

counts = result.get\_counts(qc)

*\# Print the results*

print(counts)
