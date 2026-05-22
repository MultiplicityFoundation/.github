---
slug: a-student-s-guide-to-a-real-world-a-b-test
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/ui-ux/A Student_s Guide to a Real-World A_B Test.md
  last_synced: '2026-03-20T17:17:17.668547Z'
---

**A Student\'s Guide to a Real-World A/B Test: Primes vs. Standard Numbers**
============================================================================

### **Introduction: The Big Idea**

Welcome to a behind-the-scenes look at how data is used to make smart
product decisions. This guide will walk you through a real experiment,
breaking down each step of the scientific process. We\'ll explore how a
team tests a core component of their new **Adaptive UX Engine**---a
smart system designed to change the user interface in real time---using
data, not just opinions, to figure out what works best.

The experiment is designed to answer a simple but important question:
when we represent user actions with data, does using special numbers
(primes) offer any real benefit, or are they just \"representational
fluff\"? Let\'s find out!

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

**1. What\'s the Big Question?**
--------------------------------

The goal of this experiment is to empirically test whether encoding user
actions with prime numbers gives different results compared to using
standard, consecutive numbers (like 1, 2, 3\...).

At its core, the team is testing two competing ideas for how to turn a
user\'s click into a number that a computer can understand. Instead of
just seeing a \"click,\" the system creates a unique signature for that
action, like a fingerprint. It combines the event type, the page the
user is on, and the specific button they clicked into a single string,
like click\|/home\|btn\_signup. *That unique string* is what gets
assigned a number.

The two ideas being tested are:

-   **Standard Encoding:** Assigning a simple integer ID (1, 2, 3\...)
    > to each unique user action. This is the straightforward,
    > common-sense approach.

-   **Prime Encoding:** Assigning a unique prime number (2, 3, 5\...) to
    > each unique user action. This is a more complex idea, and we need
    > to know if that complexity adds any value.

An A/B test is the perfect scientific tool to find a clear, data-driven
answer to which method is better.

**2. Our Scientific Method: The A/B Test**
------------------------------------------

An A/B test is a controlled experiment used to compare two versions of
something to see which one performs better. Think of it like a taste
test: you give one group of people beverage \"A\" and another group
beverage \"B,\" and then you measure which group enjoyed their drink
more.

In our case, we\'re not testing beverages; we\'re testing data-encoding
methods. To do this scientifically, we must first state our hypothesis.
Our starting assumption, or **Null Hypothesis (H₀)**, is that the prime
numbers will make absolutely no difference.

H₀ (null): Prime encoding ≡ standard encoding; no difference in key UX
metrics.

In other words, we begin by assuming the new idea (Prime Encoding)
offers no advantage over the standard method. The experiment\'s job is
to collect enough evidence to either prove or disprove this starting
assumption.

**3. Setting Up the Experiment**
--------------------------------

To run a fair test, we divide our users into two groups. One group will
be our \"control\" (the existing method), and the other will be our
\"treatment\" (the new idea).

  Arm A (The Control Group)             Arm B (The Treatment Group)
  ------------------------------------- ---------------------------------------
  **Purpose:** Control (The Baseline)   **Purpose:** Treatment (The New Idea)
  Uses the StandardEncoder              Uses the PrimeEncoder
  (Assigns IDs like 1, 2, 3\...)        (Assigns IDs like 2, 3, 5\...)

The most important rule of the experiment is: **No other differences.**
The user interface, system performance, and all other variables must be
identical for both groups. The *only* thing that is different is the
encoding method running in the background.

To ensure the test is unbiased, users are randomly assigned to a group
based on their user\_id. The system takes each user\_id, hashes it into
a stable number, and then assigns the user to a group based on that
number. This ensures every user has a 50/50 chance of being in either
group and that they stay in the same group every time they visit. This
assignment is \"sticky,\" meaning once a user is in a group, they stay
in that group for the entire experiment.

**4. How We Keep Score: Defining Success with Metrics**
-------------------------------------------------------

To know which group \"wins,\" we must define what we are measuring
*before* the experiment starts. This prevents us from changing the rules
halfway through. We use three types of metrics:

1.  **The Primary Metric (The One that Really Counts):** This is the
    > single most important measure of success that will determine the
    > outcome of the test. For example, we might choose **\"Task
    > completion rate,\"** which measures the percentage of users who
    > successfully sign up for an account **within 24 hours of their
    > first session in the experiment.** If this number goes up, the
    > change is likely a good one.

2.  **Secondary Metrics (Other Interesting Clues):** These metrics
    > provide additional context and help us understand the results more
    > deeply. They don\'t decide the winner, but they can reveal other
    > interesting effects.

    -   *Example 1:* **Engagement** (e.g., the average number of actions
        > a user takes).

    -   *Example 2:* **Time-to-task-completion** (e.g., how long it
        > takes to sign up).

3.  **Guardrail Metrics (Making Sure We Don\'t Break Anything):** These
    > are safety checks to ensure the new idea isn\'t causing harm. If a
    > guardrail metric gets worse, we might have to stop the experiment
    > early.

    -   *Example 1:* **Error rate** (e.g., the number of system errors
        > users see).

    -   *Example 2:* **Latency of Adaptation API (p95, p99)** (e.g.,
        > ensuring the system doesn\'t get slower for our users).

Once we have our metrics, we can run the experiment and collect the data
needed to make a final decision.

**5. Analyzing the Results: Who Won?**
--------------------------------------

The experiment runs until a predetermined number of people (the \"sample
size\") have participated. This ensures we have enough data to make a
reliable decision.

Once the data is collected, we perform the analysis. We compare the
primary metric---for instance, the task completion rate---between Arm A
(Standard) and Arm B (Prime). The decision is based on a simple rule: if
the difference between the two groups is large enough to be
**statistically significant** (meaning it\'s very unlikely to be due to
random chance, typically with a p-value \< 0.05) and is **practically
meaningful**, we have a clear winner.

Here are the possible outcomes:

-   **Prime is better:** The data shows that the prime encoding system
    > led to a significant improvement in our primary metric. We will
    > keep the new system.

-   **Prime is worse:** The data shows that the prime encoding system
    > harmed our primary metric. We will discard the idea.

-   **No significant difference:** The data shows no meaningful
    > difference between the two groups. We **treat the hypothesis that
    > \'primes improve UX\' as falsified** at this effect-size scale.

**6. Conclusion: What We Learn, Win or Lose**
---------------------------------------------

A core part of the scientific process is being honest about the results,
whatever they may be.

If this experiment shows no measurable benefit from using prime numbers,
the honest and correct conclusion is to **admit that primes are
representational fluff in this user experience context.** The team would
then drop the idea of using primes and stick with the simpler, standard
encoding method.

This is not a failure! Even if a hypothesis doesn\'t work out, a
well-run experiment is always a success. It provides a clear,
data-driven answer that prevents the team from wasting time and
resources on an idea that doesn\'t actually help users. Every
experiment, win or lose, provides valuable knowledge.
