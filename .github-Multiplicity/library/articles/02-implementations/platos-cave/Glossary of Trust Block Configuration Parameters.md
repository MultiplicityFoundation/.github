---
slug: glossary-of-trust-block-configuration-parameters
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 02-implementations/platos-cave/Glossary of Trust Block Configuration Parameters.md
  last_synced: '2026-03-20T17:17:15.901044Z'
---

**Glossary of Trust Block Configuration Parameters**
====================================================

Welcome to the Plato\'s Cave Simulator. This glossary introduces the
primary \"tuning knobs\" that control the social dynamics of the trust
block. Think of these parameters as the controls on a complex scientific
instrument. Understanding these settings allows you to move from being a
passive observer to an active experimenter, shaping how agents engage in
their dialectic of learning, who they decide to trust, and how the
entire system converges on the truth.

**1. Core Trust Calculation: The Engine of Belief**
---------------------------------------------------

This first group of parameters controls the fundamental method for
calculating the base level of trust between every pair of agents in the
simulation.

  Parameter              What It Does                                                                                                                                                                                                                                                    Strategic Insight for Newcomers
  ---------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **trust\_mode**        Selects the core trust calculation method. Options are **proxy** (a fast approximation based on state distance), **exact** (the standard, accurate \'counterfactual\' method), and **exact\_chunked** (a memory-safe version of exact for large populations).   The \'proxy\' mode is the fastest but least accurate, useful only for quick tests. The real trade-off is between \'exact\' and \'exact\_chunked\'. Use **exact** for its simplicity and speed in smaller simulations (N ≤ 150). For anything larger, **exact\_chunked** is essential, trading a minor computational overhead for the ability to scale without memory failures.
  **chunk\_threshold**   Sets the number of agents (N) at which the simulation automatically switches from exact to the memory-safe exact\_chunked mode.                                                                                                                                 This is a built-in performance safeguard. You typically won\'t need to change this, as it\'s designed to automatically protect your simulation from memory errors as the agent population grows.
  **chunk\_size**        Defines the \"batch size\" for processing agents when exact\_chunked mode is active.                                                                                                                                                                            This parameter directly controls the memory footprint of the trust calculation. Smaller values use less memory per step, which can be helpful if you have memory constraints, but may cause the simulation to run slightly slower overall.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

After calculating these raw trust scores, the next step is to control
how sensitively the system reacts to them, especially as the simulation
progresses over time.

**2. Trust Sensitivity Schedule: Controlling the Learning Rate**
----------------------------------------------------------------

These \"alpha\" parameters manage the simulation\'s learning rate,
designed to prevent the system from either converging too quickly on a
\"false sun\" (\'premature lock-in\') or changing so erratically that
the agents never escape the cave.

-   **dynamic\_alpha**

    -   **Function:** A True/False switch that enables or disables the
        > time-decaying trust sensitivity schedule. When False,
        > sensitivity is fixed throughout the simulation.

    -   **Strategic Role:** Setting this to True is crucial for most
        > simulations. It allows for rapid, exploratory learning at the
        > beginning when agents\' beliefs are forming, and then promotes
        > stability in later stages as the system converges on a
        > consensus.

-   **alpha\_schedule**

    -   **Function:** Sets the mathematical function used for the decay
        > of trust sensitivity. The options are \"exp\" for a smooth
        > exponential decay or \"linear\" for a straight-line decay.

    -   **Strategic Role:** The \"exp\" schedule provides a smoother,
        > more gradual decay, which is generally preferred for achieving
        > stable convergence without abrupt changes in system dynamics.

-   **alpha\_tau**

    -   **Function:** This parameter controls the *rate* of decay for
        > trust sensitivity.

    -   **Strategic Role:** Higher values cause a slower decay. If you
        > observe that your simulation is converging too quickly or
        > seems unstable in its early phases, **increase this value** to
        > slow down the learning rate.

-   **alpha\_min**

    -   **Function:** Defines the absolute minimum floor for trust
        > sensitivity (alpha\_t), preventing it from ever decaying to
        > zero.

    -   **Strategic Role:** This acts as a critical safeguard. It
        > ensures that the system never completely stops learning,
        > allowing it to remain adaptable and responsive to new
        > information even very late in the simulation.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Beyond controlling the learning rate, it\'s also important to stabilize
the trust scores themselves against short-term, noisy fluctuations.

**3. Trust Smoothing: Adding \"Epistemic Inertia\"**
----------------------------------------------------

In this simulation, trust is treated as a belief state that possesses
\"epistemic inertia\"---it doesn\'t change instantly based on a single
new piece of information. This principle helps to prevent rapid, noisy
fluctuations in the social dynamics. This prevents agents from radically
changing who they trust based on a single, noisy interaction, leading to
more believable social dynamics.

-   **trust\_ema**

    -   **Function:** This is the blending factor for the Exponential
        > Moving Average (EMA) applied to trust scores. A value of 1.0
        > means only the brand-new, current score is used. A value of
        > 0.0 means only the previously smoothed score is used.

    -   **Strategic Role:** Increasing this value (e.g., from 0.3 to
        > 0.5) gives more weight to historical trust, making the overall
        > trust matrix more stable and resistant to being swayed by
        > short-term noise. If trust dynamics in your simulation seem
        > too volatile, **increase this value**.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

While the previous parameters shape how trust is formed between agents,
the following parameters act as a critical safeguard. They are designed
to prevent the entire system from converging on a popular but incorrect
belief---what the simulation\'s creators call a \"false sun.\" This
mechanism ensures the system remains tethered to the objective ground
truth.

**4. The Oracle Penalty: A Safeguard Against Relativism**
---------------------------------------------------------

This powerful mechanism protects the simulation from \"herding\"
behavior, where agents might converge on a comfortable consensus that is
objectively wrong. It works by penalizing agents whose worldviews, if
adopted more widely, would degrade the system\'s global best-fit
estimate of the truth (the \"oracle\").

### **4.1. Penalty Strength & Application**

These parameters control the core application of the oracle penalty.

  Parameter                  What It Does                                                                                                                Strategic Role
  -------------------------- --------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **oracle\_penalty**        The master switch and strength coefficient for the penalty. A value of 0.0 disables it completely.                          This is your primary lever for controlling the influence of the objective truth. Higher values will more strongly suppress trust in agents whose worldviews deviate from the globally optimal solution.
  **oracle\_penalty\_tau**   A scaling factor that moderates the harshness of the penalty calculation, making it less sensitive to small fluctuations.   If the penalty seems to be causing instability or noisy trust changes, **increase this value** (e.g., from 0.05 to 0.1). This will smooth its application and make it less reactive.
  **penalty\_min**           The minimum penalty factor allowed (e.g., 0.20).                                                                            This acts as a floor, preventing an agent\'s trust score from being completely zeroed out by the penalty. It ensures that no agent, no matter how deviant, is ever fully silenced or removed from the dialectic.

### **4.2. Penalty Computation & Efficiency**

These settings control the performance and memory usage of the oracle
penalty calculation, which can be computationally intensive in large
simulations.

-   **oracle\_subsample**: The fraction of agents (e.g., 0.20 for 20%)
    > used in a stratified subsample to *estimate* the oracle penalty.
    > *This is a classic speed-versus-accuracy trade-off. Lowering the
    > fraction speeds up each step but risks a less reliable penalty
    > signal.*

-   **oracle\_chunk\_size**: The chunk size used for the penalty
    > computation to manage memory. If set to None, it automatically
    > defaults to the main chunk\_size parameter.

-   **memory\_threshold\_floats**: A memory safety limit (measured in
    > the number of floating-point numbers) that will force the penalty
    > calculation to use chunks, even if the main trust\_mode is not
    > chunked.

-   **shuffle\_oracle\_batches**: If True, the simulation shuffles the
    > order of agents before processing them in chunks. *Setting this to
    > True is a best practice that prevents subtle biases from emerging
    > if, for example, high-level agents were always processed first in
    > every batch.*

### **4.3. Oracle Sampling Strategy**

These parameters fine-tune *which* agents are selected for the oracle
subsample. This is a key strategic choice for how you want to guide the
simulation\'s search for the truth.

-   **stratify\_balance**: If True, the sampling process attempts to
    > create a balanced representation from all hierarchy levels based
    > on their population size, ensuring that small, high-level groups
    > aren\'t ignored.

-   **min\_k\_per\_level**: The guaranteed minimum number of agents to
    > be sampled from each hierarchy level. This ensures that even very
    > sparsely populated levels (e.g., a single leader) are always
    > represented in the oracle calculation.

-   **high\_layer\_bias**: A bias factor that favors sampling more
    > agents from the higher, more informed levels of the hierarchy.
    > This strategically reinforces \"ascent fidelity\" by giving more
    > weight to the worldviews of agents who have a more complete view
    > of the \"Form\" (the ground truth).

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Understanding these individual parameters is the first step. To master
the simulator, however, you must learn to orchestrate them. This final
section moves from theory to practice, providing concrete tuning
strategies for the most common experimental challenges.

**5. Quick Tuning Guide: Common Scenarios**
-------------------------------------------

Here is a concise guide to solving common problems by adjusting the
parameters discussed above.

-   **Scenario: My simulation is running out of memory or is very slow
    > with many agents.**

    -   **Solution:** Ensure trust\_mode is set to \"exact\_chunked\".
        > The simulation should do this automatically if the number of
        > agents N is greater than chunk\_threshold. If memory is still
        > an issue, you can further reduce the memory footprint by
        > decreasing chunk\_size and/or oracle\_chunk\_size.

-   **Scenario: The simulation converges too quickly to a bad solution
    > or seems unstable at the start.**

    -   **Solution:** The simulation\'s learning rate is too aggressive.
        > You can make two key adjustments to calm it down:

        1.  **Increase alpha\_tau** to slow the decay of trust
            > sensitivity, giving agents more time to learn.

        2.  **Increase trust\_ema** to add more \"epistemic inertia,\"
            > making trust scores more stable and less reactive to
            > short-term noise.

-   **Scenario: The oracle penalty seems to be causing noisy or erratic
    > trust changes.**

    -   **Solution:** The penalty is being applied too aggressively or
        > is overreacting to small changes. **Increase
        > oracle\_penalty\_tau** (e.g., to 0.1) to smooth the penalty
        > and make it less sensitive.
