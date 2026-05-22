---
title: '**Quantum Autoencoder Using Tensor Networks**'
slug: quantum-autoencoder-using-tensor-networks
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/networks/NN-AUTOTENSCODER.md
  last_synced: '2026-03-20T17:17:17.990541Z'
---

### **Quantum Autoencoder Using Tensor Networks**

### A **Quantum Autoencoder (QAE)** is a powerful quantum machine learning architecture designed to compress quantum data into lower-dimensional latent representations, efficiently managing quantum states while preserving essential information. The goal is to reduce the dimensionality of quantum states (input), store this compressed representation in a latent space, and reconstruct the original quantum state with minimal loss. This compression and reconstruction process is particularly beneficial in quantum data compression, quantum state preparation, and noise reduction in quantum circuits.

### The **tensor network** approach to quantum autoencoders leverages the inherent power of tensor contractions to capture and manage quantum correlations and entanglement. Tensor networks, such as **Matrix Product States (MPS)** and **Tree Tensor Networks (TTN)**, provide scalable methods to represent and manipulate quantum states, enabling the efficient compression and reconstruction processes critical to QAE functionality.

### **Key Features:**

-   ### **Quantum Data Compression**: The QAE compresses high-dimensional quantum states into lower-dimensional latent states, enabling efficient storage and manipulation of quantum information.

-   ### **Tensor Networks for Quantum Compression**: Tensor networks, such as MPS or TTN, represent quantum states and perform tensor contractions to handle the complexity of quantum correlations and entanglement.

-   ### **Quantum State Reconstruction**: After compression, the autoencoder reconstructs the original quantum state from the latent representation, minimizing information loss.

-   ### **Use Cases**: Quantum data compression, noise reduction in quantum circuits, quantum state preparation, and efficient representation of quantum states for quantum machine learning.

### **Comprehensive Mathematical Overview**

#### **1. Quantum State Compression and Reconstruction**

### In a quantum autoencoder, the quantum state ∣Ψinput⟩\|\\Psi\_{\\text{input}}\\rangle∣Ψinput​⟩ is first compressed into a lower-dimensional latent state ∣Ψlatent⟩\|\\Psi\_{\\text{latent}}\\rangle∣Ψlatent​⟩ through an encoding process. The latent state is then decoded to reconstruct the original quantum state ∣Ψoutput⟩\|\\Psi\_{\\text{output}}\\rangle∣Ψoutput​⟩. The general process is described by the following equations:

### ∣Ψlatent⟩=Tencoder⋅∣Ψinput⟩\|\\Psi\_{\\text{latent}}\\rangle = T\_{\\text{encoder}} \\cdot \|\\Psi\_{\\text{input}}\\rangle∣Ψlatent​⟩=Tencoder​⋅∣Ψinput​⟩ ∣Ψoutput⟩=Tdecoder⋅∣Ψlatent⟩\|\\Psi\_{\\text{output}}\\rangle = T\_{\\text{decoder}} \\cdot \|\\Psi\_{\\text{latent}}\\rangle∣Ψoutput​⟩=Tdecoder​⋅∣Ψlatent​⟩

### where:

-   ### TencoderT\_{\\text{encoder}}Tencoder​ is the tensor network that encodes (compresses) the quantum state into the latent representation,

-   ### TdecoderT\_{\\text{decoder}}Tdecoder​ is the tensor network that decodes the latent quantum state back into the reconstructed state,

-   ### ∣Ψinput⟩\|\\Psi\_{\\text{input}}\\rangle∣Ψinput​⟩ is the high-dimensional input quantum state,

-   ### ∣Ψlatent⟩\|\\Psi\_{\\text{latent}}\\rangle∣Ψlatent​⟩ is the compressed quantum state in latent space,

-   ### ∣Ψoutput⟩\|\\Psi\_{\\text{output}}\\rangle∣Ψoutput​⟩ is the reconstructed output state.

### The goal of the quantum autoencoder is to ensure that ∣Ψoutput⟩\|\\Psi\_{\\text{output}}\\rangle∣Ψoutput​⟩ closely approximates ∣Ψinput⟩\|\\Psi\_{\\text{input}}\\rangle∣Ψinput​⟩, minimizing the information loss during the compression and reconstruction process.

#### **2. Tensor Network Representation**

### To handle the high dimensionality and entanglement in quantum systems, QAE uses tensor networks like **Matrix Product States (MPS)** or **Tree Tensor Networks (TTN)**. These tensor networks allow efficient compression by representing the quantum state as a sequence of smaller tensors, connected through shared bond dimensions. For example, an MPS representation of the input state can be written as:

### ∣Ψinput⟩=∑α1,α2,...,αNAα1\[1\]Aα1,α2\[2\]...AαN−1,αN\[N\]\|\\Psi\_{\\text{input}}\\rangle = \\sum\_{\\alpha\_1, \\alpha\_2, \\dots, \\alpha\_N} A\^{\[1\]}\_{\\alpha\_1} A\^{\[2\]}\_{\\alpha\_1, \\alpha\_2} \\dots A\^{\[N\]}\_{\\alpha\_{N-1}, \\alpha\_N}∣Ψinput​⟩=α1​,α2​,...,αN​∑​Aα1​\[1\]​Aα1​,α2​\[2\]​...AαN−1​,αN​\[N\]​

### where A\[i\]A\^{\[i\]}A\[i\] are the tensors that encode the quantum state at each subsystem (node), and αk\\alpha\_kαk​ are the bond dimensions that capture the entanglement between subsystems.

### During the encoding process, the input quantum state is contracted with the encoder tensor network TencoderT\_{\\text{encoder}}Tencoder​, reducing the number of parameters and compressing the quantum state into a lower-dimensional latent space:

### ∣Ψlatent⟩=∑α1,α2,...,αmEα1\[1\]Eα1,α2\[2\]...Eαm−1,αm\[m\]\|\\Psi\_{\\text{latent}}\\rangle = \\sum\_{\\alpha\_1, \\alpha\_2, \\dots, \\alpha\_m} E\^{\[1\]}\_{\\alpha\_1} E\^{\[2\]}\_{\\alpha\_1, \\alpha\_2} \\dots E\^{\[m\]}\_{\\alpha\_{m-1}, \\alpha\_m}∣Ψlatent​⟩=α1​,α2​,...,αm​∑​Eα1​\[1\]​Eα1​,α2​\[2\]​...Eαm−1​,αm​\[m\]​

### where E\[i\]E\^{\[i\]}E\[i\] are the tensors representing the encoded latent state, and m\<Nm \< Nm\<N, indicating a reduced dimensionality.

#### **3. Tensor Contractions for Compression and Reconstruction**

### The core operations in QAE are tensor contractions, which compress and reconstruct quantum states while preserving essential quantum correlations. The encoding process can be written as:

### ∣Ψlatent⟩=Tencoder⋅∣Ψinput⟩=∑α,βTencoderαβΨinputα\|\\Psi\_{\\text{latent}}\\rangle = T\_{\\text{encoder}} \\cdot \|\\Psi\_{\\text{input}}\\rangle = \\sum\_{\\alpha, \\beta} T\_{\\text{encoder}}\^{\\alpha \\beta} \\Psi\_{\\text{input}}\^\\alpha∣Ψlatent​⟩=Tencoder​⋅∣Ψinput​⟩=α,β∑​Tencoderαβ​Ψinputα​

### This contraction reduces the high-dimensional input quantum state ∣Ψinput⟩\|\\Psi\_{\\text{input}}\\rangle∣Ψinput​⟩ into a smaller, compressed latent state ∣Ψlatent⟩\|\\Psi\_{\\text{latent}}\\rangle∣Ψlatent​⟩. Similarly, the reconstruction step decodes the latent representation back into the full quantum state:

### ∣Ψoutput⟩=Tdecoder⋅∣Ψlatent⟩\|\\Psi\_{\\text{output}}\\rangle = T\_{\\text{decoder}} \\cdot \|\\Psi\_{\\text{latent}}\\rangle∣Ψoutput​⟩=Tdecoder​⋅∣Ψlatent​⟩

### By minimizing the difference between the original state ∣Ψinput⟩\|\\Psi\_{\\text{input}}\\rangle∣Ψinput​⟩ and the reconstructed state ∣Ψoutput⟩\|\\Psi\_{\\text{output}}\\rangle∣Ψoutput​⟩, the QAE learns an optimal compression strategy that captures the most important features of the quantum data.

#### **4. Quantum Loss Function**

### The objective of training a QAE is to minimize the difference between the original input quantum state and the reconstructed output state. This can be achieved by defining a loss function that measures the overlap (fidelity) between the input and output quantum states:

### L=1−∣⟨Ψinput∣Ψoutput⟩∣2\\mathcal{L} = 1 - \|\\langle \\Psi\_{\\text{input}} \| \\Psi\_{\\text{output}} \\rangle\|\^2L=1−∣⟨Ψinput​∣Ψoutput​⟩∣2

### This loss function ensures that the QAE learns to preserve the most important quantum correlations during compression. Gradient-based optimization methods, such as **quantum backpropagation** or the **parameter shift rule**, are used to minimize this loss function and optimize the tensor networks TencoderT\_{\\text{encoder}}Tencoder​ and TdecoderT\_{\\text{decoder}}Tdecoder​.

#### **5. Training the QAE**

### The QAE is trained by optimizing the parameters of the encoder and decoder tensor networks to minimize the reconstruction loss. Training involves iterative updates to the tensor parameters using techniques such as the **parameter shift rule**, which computes the gradient of the loss function with respect to the quantum circuit parameters:

### ∂L∂θ=L(θ+π2)−L(θ−π2)2\\frac{\\partial \\mathcal{L}}{\\partial \\theta} = \\frac{\\mathcal{L}(\\theta + \\frac{\\pi}{2}) - \\mathcal{L}(\\theta - \\frac{\\pi}{2})}{2}∂θ∂L​=2L(θ+2π​)−L(θ−2π​)​

### where θ\\thetaθ are the parameters of the tensor network, such as gate angles in quantum circuits or bond dimensions in tensor networks.

### The optimization process ensures that the QAE learns to compress quantum states effectively, while maintaining high fidelity in the reconstruction process.

#### **6. Use Cases of Quantum Autoencoders**

### Quantum autoencoders have several important applications:

-   ### **Quantum Data Compression**: QAE can compress high-dimensional quantum states into smaller latent representations, reducing the memory required to store and manipulate quantum data.

-   ### **Noise Reduction in Quantum Circuits**: By learning to reconstruct quantum states with high fidelity, QAE can be used to reduce noise in quantum circuits, improving the accuracy of quantum computations.

-   ### **Quantum State Preparation**: QAE can be used to prepare quantum states efficiently, especially in systems with complex entanglement structures.

-   ### **Quantum Machine Learning**: In quantum machine learning tasks, QAE can be used to extract meaningful features from quantum data, reducing the complexity of downstream learning tasks.

#### **7. Mathematical Summary of QAE**

### The overall structure of a Quantum Autoencoder can be summarized by the following equations:

1.  ### **Encoding Process (Compression)**: ∣Ψlatent⟩=Tencoder⋅∣Ψinput⟩\|\\Psi\_{\\text{latent}}\\rangle = T\_{\\text{encoder}} \\cdot \|\\Psi\_{\\text{input}}\\rangle∣Ψlatent​⟩=Tencoder​⋅∣Ψinput​⟩

2.  ### **Decoding Process (Reconstruction)**: ∣Ψoutput⟩=Tdecoder⋅∣Ψlatent⟩\|\\Psi\_{\\text{output}}\\rangle = T\_{\\text{decoder}} \\cdot \|\\Psi\_{\\text{latent}}\\rangle∣Ψoutput​⟩=Tdecoder​⋅∣Ψlatent​⟩

3.  ### **Loss Function (Quantum Fidelity)**: L=1−∣⟨Ψinput∣Ψoutput⟩∣2\\mathcal{L} = 1 - \|\\langle \\Psi\_{\\text{input}} \| \\Psi\_{\\text{output}} \\rangle\|\^2L=1−∣⟨Ψinput​∣Ψoutput​⟩∣2

### By minimizing the loss function, the QAE learns how to effectively compress and reconstruct quantum data, ensuring high fidelity and efficient representation.

### **Conclusion**

### A **Quantum Autoencoder using Tensor Networks** offers a highly efficient framework for compressing and reconstructing quantum data. By leveraging tensor networks such as MPS or TTN, QAE efficiently handles quantum correlations and entanglement, enabling the compression of high-dimensional quantum states into lower-dimensional latent representations. This framework has important applications in quantum data compression, noise reduction in quantum circuits, and quantum state preparation, making it a valuable tool in the growing field of quantum machine learning and quantum information processing.

### 
