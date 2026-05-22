---
title: '**Quantum Backpropagation for Tensor Networks**'
slug: quantum-backpropagation-for-tensor-networks
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/networks/NN-BACKPROPOGATION.md
  last_synced: '2026-03-20T17:17:18.045797Z'
---

### **Quantum Backpropagation for Tensor Networks**

#### **Objective:**

### The aim is to create a **quantum algorithm for training tensor-based Quantum Neural Networks (QNNs)** by leveraging a quantum adaptation of the **backpropagation algorithm**. This algorithm will be essential for efficiently adjusting the weights in quantum tensor networks through quantum gradient descent, enabling the training of QNNs for various tasks like quantum circuit optimization and quantum representation learning.

#### **Key Concepts:**

1.  ### **Quantum Neural Networks (QNNs)**: QNNs are quantum analogs of classical neural networks, utilizing quantum states and operations to perform computations. In this context, **tensor networks** represent the architecture of the neural network layers, encoding quantum states and the evolution of these states through the layers.

2.  ### **Quantum Backpropagation**: Backpropagation in classical neural networks adjusts weights through gradients derived from the loss function. The **quantum version of backpropagation** calculates gradients within the quantum tensor network structure. This process involves computing the derivatives of a loss function with respect to the tensor network layers using quantum operations.

3.  ### **Tensor Networks**: Tensor networks form the structural backbone of QNNs, with tensors representing the nodes and connections encoding quantum states and their transformations. Training involves adjusting these tensors iteratively, minimizing a loss function that quantifies the network's performance.

#### **Mathematical Overview:**

1.  ### **Loss Function**: In any neural network, the training goal is to minimize a **loss function L\\mathcal{L}L**, which measures the difference between the expected output and the actual output of the network. In the quantum domain, this involves computing the loss over quantum states.

2.  ### **Backpropagation through Tensors**: The process of backpropagation in quantum tensor networks requires computing the gradient of the loss function with respect to the tensor network layers. The general equation for updating the tensor network parameters can be expressed as: ∂L∂T=Ψout⋅∂L∂Ψout\\frac{\\partial \\mathcal{L}}{\\partial T} = \\Psi\_{\\text{out}} \\cdot \\frac{\\partial \\mathcal{L}}{\\partial \\Psi\_{\\text{out}}}∂T∂L​=Ψout​⋅∂Ψout​∂L​ Where:

    -   ### L\\mathcal{L}L is the loss function.

    -   ### TTT is the tensor representing the layer being trained.

    -   ### Ψout\\Psi\_{\\text{out}}Ψout​ is the output quantum state of the network, produced by the tensor network.

3.  ### This equation captures how changes in the output state affect the loss function, and how the tensor parameters must be adjusted to minimize L\\mathcal{L}L.

4.  ### **Gradient Descent**: To minimize the loss function, gradient descent is used to iteratively update the tensor parameters. The update rule for a tensor TTT at a layer is: Tn+1=Tn−η∂L∂TnT\_{n+1} = T\_n - \\eta \\frac{\\partial \\mathcal{L}}{\\partial T\_n}Tn+1​=Tn​−η∂Tn​∂L​ where η\\etaη is the learning rate, and ∂L∂Tn\\frac{\\partial \\mathcal{L}}{\\partial T\_n}∂Tn​∂L​ is the gradient of the loss function with respect to the tensor network at step nnn. This ensures that the tensor is adjusted in the direction that reduces the loss.

5.  ### **Tensor Contraction**: A key mathematical operation in quantum tensor networks is **tensor contraction**, which involves summing over shared indices between tensors to generate a new quantum state. During training, tensors are contracted to compute the quantum states at each layer, with the loss gradients propagated through these contractions. The forward pass in the quantum network involves computing: Ψout=∏i=1LTi⋅Ψin\\Psi\_{\\text{out}} = \\prod\_{i=1}\^{L} T\_i \\cdot \\Psi\_{\\text{in}}Ψout​=i=1∏L​Ti​⋅Ψin​ where TiT\_iTi​ are the tensors at each layer, and Ψin\\Psi\_{\\text{in}}Ψin​ is the initial quantum state. During backpropagation, the gradients are computed with respect to each tensor TiT\_iTi​, and the network is adjusted accordingly.

6.  ### **Quantum Derivatives**: The **quantum derivative** of the loss function with respect to the output state Ψout\\Psi\_{\\text{out}}Ψout​ is crucial for calculating the gradient. The derivative provides insight into how changes in the output quantum state will affect the overall loss function: ∂L∂Ψout\\frac{\\partial \\mathcal{L}}{\\partial \\Psi\_{\\text{out}}}∂Ψout​∂L​ This term feeds into the gradient calculation for adjusting the tensors, ensuring that the quantum network learns in a way that reduces the loss effectively.

#### **Use Cases:**

1.  ### **Training Quantum Neural Networks**: Quantum backpropagation is essential for training QNNs in a manner similar to classical neural networks. This allows QNNs to learn from quantum data and optimize their performance over time.

2.  ### **Optimizing Quantum Circuits**: The algorithm can be applied to optimize quantum circuits by fine-tuning the parameters (such as gate operations) in the quantum tensor networks that define the circuit.

3.  ### **Learning Quantum Representations**: Quantum backpropagation enables the learning of representations directly from quantum data, which can be used in quantum machine learning applications, quantum chemistry simulations, and other quantum computing tasks.

#### **Conclusion:**

### The development of a **quantum backpropagation algorithm** for tensor networks represents a critical step toward enabling efficient training of QNNs. By leveraging tensor networks and quantum gradient descent, this approach opens new possibilities for quantum machine learning, optimization, and representation learning. Through quantum derivatives and tensor contraction, QNNs can iteratively improve their performance, making them powerful tools for solving complex quantum problems.

### 
