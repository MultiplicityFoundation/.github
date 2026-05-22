---
title: '**Quantum Tensor Graph Neural Networks (QGNN)**'
slug: quantum-tensor-graph-neural-networks-qgnn
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/networks/NN-TENSORGRAPH.md
  last_synced: '2026-03-20T17:17:18.108225Z'
---

### **Quantum Tensor Graph Neural Networks (QGNN)**

### The **Quantum Graph Neural Network (QGNN)** is a cutting-edge framework designed to process quantum data represented in the form of graphs. In QGNNs, nodes and edges of the graph correspond to quantum states and entanglement, respectively, allowing the network to model quantum correlations and interactions within a system. QGNNs extend classical graph neural networks (GNNs) to the quantum domain, utilizing **tensor networks** to efficiently represent and manipulate quantum states associated with graph structures.

### QGNNs are particularly suited for applications such as **quantum chemistry**, where molecular structures are naturally represented as graphs, **quantum network analysis**, and the **modeling of quantum systems** that involve complex entangled relationships between subsystems.

### **Key Features:**

-   ### **Quantum State Representation in Graphs**: Nodes represent quantum states, while edges capture the entanglement or interaction between these states. The graph-based structure facilitates the modeling of multi-particle quantum systems.

-   ### **Tensor Networks for Quantum Graphs**: Tensor networks efficiently encode the states and interactions, capturing quantum correlations across the graph and propagating information using tensor contractions.

-   ### **Information Propagation on Quantum Graphs**: Quantum data is processed over the graph structure through recurrent tensor operations, ensuring efficient computation and entanglement preservation.

-   ### **Use Cases**: QGNNs are highly applicable in **quantum chemistry** (modeling molecular graphs), **quantum communication networks**, and **quantum system simulations**, where understanding the relationships between subsystems is crucial.

### **Comprehensive Mathematical Overview**

#### **1. Quantum Graph Representation**

### In a QGNN, the graph is denoted by G=(V,E)G = (V, E)G=(V,E), where:

-   ### V={v1,v2,...,vN}V = \\{v\_1, v\_2, \\dots, v\_N\\}V={v1​,v2​,...,vN​} represents the set of nodes, with each node viv\_ivi​ corresponding to a quantum state ∣Ψi⟩\|\\Psi\_i\\rangle∣Ψi​⟩,

-   ### E={(vi,vj)}E = \\{(v\_i, v\_j)\\}E={(vi​,vj​)} represents the set of edges, with each edge representing the quantum entanglement or interaction between nodes viv\_ivi​ and vjv\_jvj​.

### The goal of the QGNN is to propagate quantum information across this graph, evolving the quantum states of the nodes based on their connections (edges) and input quantum states.

#### **2. Quantum State and Edge Tensor Encoding**

### For each node viv\_ivi​, the quantum state is represented as ∣Ψi⟩\|\\Psi\_i\\rangle∣Ψi​⟩, which may be a high-dimensional quantum state in a Hilbert space. For each edge (vi,vj)(v\_i, v\_j)(vi​,vj​), a tensor EijE\_{ij}Eij​ encodes the entanglement or interaction between the quantum states at nodes viv\_ivi​ and vjv\_jvj​.

### The quantum state of the entire graph can be written as the tensor product of node and edge states:

### ∣ΨG⟩=⨂i=1N∣Ψi⟩⊗⨂(i,j)∈EEij\|\\Psi\_G\\rangle = \\bigotimes\_{i=1}\^{N} \|\\Psi\_i\\rangle \\otimes \\bigotimes\_{(i,j) \\in E} E\_{ij}∣ΨG​⟩=i=1⨂N​∣Ψi​⟩⊗(i,j)∈E⨂​Eij​

### Here, ∣ΨG⟩\|\\Psi\_G\\rangle∣ΨG​⟩ represents the combined quantum state of the graph, where node and edge tensors together describe the quantum correlations across the system.

#### **3. Graph Propagation Using Tensor Contractions**

### Information propagation in a QGNN is performed through **tensor contractions** along the edges of the graph. At each time step, the quantum state of each node is updated based on the quantum states of its neighbors and the entanglement encoded in the edge tensors. The propagation rule is given by:

### ∣Ψiout⟩=Tgraph⋅(∣Ψiin⟩,⨂j∈Neighbors(i)Eij∣Ψjin⟩)\|\\Psi\_i\^{\\text{out}}\\rangle = T\_{\\text{graph}} \\cdot \\left( \|\\Psi\_i\^{\\text{in}}\\rangle, \\bigotimes\_{j \\in \\text{Neighbors}(i)} E\_{ij} \|\\Psi\_j\^{\\text{in}}\\rangle \\right)∣Ψiout​⟩=Tgraph​⋅​∣Ψiin​⟩,j∈Neighbors(i)⨂​Eij​∣Ψjin​⟩​

### where:

-   ### TgraphT\_{\\text{graph}}Tgraph​ is the tensor operation that governs the graph update, encoding the evolution rules for the quantum states of the nodes,

-   ### ∣Ψiin⟩\|\\Psi\_i\^{\\text{in}}\\rangle∣Ψiin​⟩ is the input quantum state at node viv\_ivi​,

-   ### ∣Ψjin⟩\|\\Psi\_j\^{\\text{in}}\\rangle∣Ψjin​⟩ are the quantum states of neighboring nodes,

-   ### EijE\_{ij}Eij​ are the tensors representing the interactions between nodes viv\_ivi​ and vjv\_jvj​.

### This tensor contraction ensures that information is shared between connected nodes while preserving the quantum entanglement structure of the graph.

#### **4. Quantum Graph State Evolution**

### The evolution of the quantum state of the graph is driven by iteratively applying the tensor contractions over the nodes and edges. The quantum state at each node viv\_ivi​ is updated based on the incoming quantum states from neighboring nodes and the edge interactions. The process can be summarized as:

### ∣Ψi(t+1)⟩=∑jTgraph(∣Ψi(t)⟩,Eij∣Ψj(t)⟩)\|\\Psi\_i\^{(t+1)}\\rangle = \\sum\_j T\_{\\text{graph}} \\left( \|\\Psi\_i\^{(t)}\\rangle, E\_{ij} \|\\Psi\_j\^{(t)}\\rangle \\right)∣Ψi(t+1)​⟩=j∑​Tgraph​(∣Ψi(t)​⟩,Eij​∣Ψj(t)​⟩)

### where ∣Ψi(t)⟩\|\\Psi\_i\^{(t)}\\rangle∣Ψi(t)​⟩ and ∣Ψj(t)⟩\|\\Psi\_j\^{(t)}\\rangle∣Ψj(t)​⟩ represent the quantum states of nodes viv\_ivi​ and vjv\_jvj​ at time ttt, and the sum is taken over the neighbors jjj of node iii.

### The recurrent application of the graph update rule allows the quantum states of the nodes to evolve, with quantum information being propagated through the entangled structure of the graph.

#### **5. Tensor Network Representation for Scalability**

### To handle the exponential complexity of quantum systems, QGNNs utilize **tensor networks** such as **Matrix Product States (MPS)** or **Tree Tensor Networks (TTN)** to represent quantum states and edge interactions. This allows for efficient compression and computation of high-dimensional quantum data.

### For example, in MPS representation, the quantum state of each node can be decomposed into a sequence of smaller tensors:

### ∣ΨG⟩=∑α1,α2,...,αNAα1\[1\]Aα1,α2\[2\]...AαN−1,αN\[N\]\|\\Psi\_G\\rangle = \\sum\_{\\alpha\_1, \\alpha\_2, \\dots, \\alpha\_N} A\^{\[1\]}\_{\\alpha\_1} A\^{\[2\]}\_{\\alpha\_1, \\alpha\_2} \\dots A\^{\[N\]}\_{\\alpha\_{N-1}, \\alpha\_N}∣ΨG​⟩=α1​,α2​,...,αN​∑​Aα1​\[1\]​Aα1​,α2​\[2\]​...AαN−1​,αN​\[N\]​

### where A\[i\]A\^{\[i\]}A\[i\] are the tensors encoding the quantum state at node viv\_ivi​, and αk\\alpha\_kαk​ are bond dimensions representing the entanglement between connected nodes.

### This tensor decomposition allows for scalable processing of large quantum graphs by reducing the number of parameters required to represent the entire system.

#### **6. Training and Optimization**

### Training the QGNN involves optimizing the parameters of the recurrent tensor network TgraphT\_{\\text{graph}}Tgraph​ and edge tensors EijE\_{ij}Eij​ to minimize a quantum loss function. This could be a cost function that measures the difference between the predicted quantum state and the desired output state, similar to classical neural networks.

### Gradient-based optimization, such as quantum backpropagation or the **parameter shift rule**, is used to update the quantum parameters:

### ∂C∂θ=C(θ+π2)−C(θ−π2)2\\frac{\\partial C}{\\partial \\theta} = \\frac{C(\\theta + \\frac{\\pi}{2}) - C(\\theta - \\frac{\\pi}{2})}{2}∂θ∂C​=2C(θ+2π​)−C(θ−2π​)​

### where C(θ)C(\\theta)C(θ) represents the quantum cost function, and θ\\thetaθ are the parameters of the QGNN. The quantum gradients are used to train the QGNN to accurately propagate quantum information across the graph.

#### **7. Mathematical Summary of QGNN**

### The general formulation of a QGNN can be expressed as:

### ∣Ψout⟩=Tgraph⋅Ψin\|\\Psi\_{\\text{out}}\\rangle = T\_{\\text{graph}} \\cdot \\Psi\_{\\text{in}}∣Ψout​⟩=Tgraph​⋅Ψin​

-   ### ∣Ψin⟩\|\\Psi\_{\\text{in}}\\rangle∣Ψin​⟩ represents the input quantum state associated with the graph nodes and edges.

-   ### TgraphT\_{\\text{graph}}Tgraph​ is the tensor network that governs the propagation of quantum information across the graph.

-   ### ∣Ψout⟩\|\\Psi\_{\\text{out}}\\rangle∣Ψout​⟩ is the output quantum state, resulting from the propagation of quantum information through the graph.

### The graph propagation is performed through iterative tensor contractions, allowing information to flow between entangled quantum states across the graph structure.

### **Conclusion**

### Quantum Graph Neural Networks (QGNNs) provide a powerful framework for processing quantum data structured as graphs. By leveraging tensor networks, QGNNs efficiently propagate quantum states and entanglement across graph nodes and edges, making them highly suitable for tasks such as quantum chemistry, quantum network analysis, and the modeling of entangled quantum systems. The mathematical foundation of QGNNs ensures scalability and adaptability to a wide range of quantum machine learning and simulation applications, offering new tools for solving complex quantum problems.

### 
