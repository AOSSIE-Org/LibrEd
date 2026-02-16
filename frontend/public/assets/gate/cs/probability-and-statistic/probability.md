**Probability Theory Note**
==========================

### Introduction
-----------------

Probability is a branch of mathematics that deals with measuring uncertainty and chance events. It provides a framework for modeling random phenomena, making predictions, and estimating the likelihood of future outcomes. In this note, we'll cover the essential concepts and formulas to tackle probability questions, including those similar to Q1 (cs_2022_61).

### Core Concepts
-----------------

#### Random Experiments and Sample Spaces

*   A **random experiment** is an action or situation where the outcome is uncertain.
*   The **sample space**, denoted by $\Omega$, is the set of all possible outcomes.

```mermaid
graph LR
A[Random Experiment] --> B[Sample Space]
```

#### Events and Their Probabilities

*   An **event** is a subset of the sample space, e.g., rolling an even number.
*   The **probability** of an event $A$, denoted by $P(A)$, is a real-valued function that satisfies:

$$
P(\Omega) = 1 \quad \text{and} \quad P(\emptyset) = 0
$$

#### Conditional Probability and Independence

*   The **conditional probability** of an event $A$ given $B$, denoted by $P(A|B)$, is defined as:

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

*   Two events $A$ and $B$ are **independent** if:

$$
P(A \cap B) = P(A) \cdot P(B)
$$

### Key Formulas/Theorems
-------------------------

#### Bayes' Theorem

*   Given two events $A$ and $B$, the posterior probability of $A$ given $B$ is:

$$
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
$$

#### Probability Mass Function (PMF)

*   The **probability mass function** (PMF), denoted by $p(x)$, assigns a probability to each outcome $x$ in the sample space.

$$
\sum_{x \in \Omega} p(x) = 1
$$

### Problem Solving Patterns
---------------------------

#### Q1-like Problems

*   **Without Replacement**: When drawing a ball from the box without replacement (e.g., drawing a green ball), calculate probabilities using conditional probability.
*   **With Replacement**: When drawing a ball with replacement (e.g., drawing an orange ball), use simple probability multiplication.

### Examples with Solutions
---------------------------

#### Example 1

Consider a random experiment where we roll a fair six-sided die. What is the probability of rolling an even number?

*   Sample space: $\Omega = \{1, 2, 3, 4, 5, 6\}$
*   Event: $A$ (rolling an even number)
*   Probability: $P(A) = P(\{2, 4, 6\}) = \frac{1}{2}$

#### Example 2

Suppose we have a box with three green balls and two orange balls. What is the probability of drawing an orange ball on the second draw if the first drawn ball was green?

*   **Without Replacement**: Since a green ball was drawn without replacement, calculate the conditional probability.

```latex
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
```

*   Apply the formula using specific values:

$$
P(\text{orange}|G) = \frac{\frac{2}{5}}{\frac{3}{5}}
$$

### Common Pitfalls
-------------------

*   **Confusing With and Without Replacement**: Pay attention to whether the problem specifies replacement or not.
*   **Forgetting to Apply Conditional Probability**: Use conditional probability when necessary (e.g., Q1).

### Quick Summary
-----------------

*   Random experiments, sample spaces, and events
*   Probabilities of events, including conditional probability
*   Independence and Bayes' theorem
*   PMF and problem-solving patterns for Q1-like problems

---

I hope this comprehensive theory note meets your requirements.