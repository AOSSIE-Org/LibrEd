**Probability Theory Note**
==========================

**Introduction**
---------------

Probability is a branch of mathematics that deals with quantifying uncertainty and likelihood. It plays a crucial role in engineering, computer science, and many other fields. This note covers essential concepts, formulas, and problem-solving strategies for the GATE CS exam.

**Core Concepts**
-----------------

### 1. Events and Sample Spaces

* An **event** is a set of outcomes from a sample space.
* A **sample space** is the set of all possible outcomes of an experiment.

### 2. Probability Measure

* The probability measure assigns a real number between 0 and 1 to each event, representing its likelihood.
* The sum of probabilities of all events in a sample space is 1.

### 3. Axioms of Probability

* **Axiom 1**: The probability of an event is non-negative.
* **Axiom 2**: The probability of the entire sample space is 1.
* **Axiom 3**: The probability of the union of mutually exclusive events is the sum of their probabilities.

### 4. Conditional Probability

* The probability of an event given that another event has occurred.
* **Formula**: P(A|B) = P(A ∩ B) / P(B)

**Key Formulas/Theorems**
-------------------------

### 1. Multiplication Rule

* P(A ∩ B) = P(A) \* P(B|A)
* **LaTeX**: $P(A \cap B) = P(A) \cdot P(B|A)$

### 2. Addition Rule for 2 Events

* P(A ∪ B) = P(A) + P(B) - P(A ∩ B)

**Problem Solving Patterns**
---------------------------

1. **Tree Diagrams**: Useful for visualizing complex events and calculating probabilities.
   ```mermaid
   graph LR
     A[Event A] --> B[Event B]
     C[Event C] --> D[Event D]
   ```
2. **Independence**: If events are independent, the probability of their intersection is the product of their individual probabilities.

**Examples with Solutions**
-------------------------

### 1. Example 1: Coin Tosses

* A fair coin is tossed twice.
* What is the probability that both tosses result in heads?

Solution:

P(Head on 1st toss) = 0.5
P(Head on 2nd toss|Head on 1st toss) = 0.5
By multiplication rule, P(Both Heads) = 0.5 \* 0.5 = 0.25

### 2. Example 2: Bag with Red and Blue Balls

* A bag contains 10 red balls and 15 blue balls.
* Two balls are drawn randomly without replacement.
* Given that the first ball is red, what is the probability that both balls are red?

Solution:

By tree diagram or direct calculation:
P(Red Ball in 2nd draw) = (9/25)
Therefore, P(Both Red Balls) = (10/25) \* (9/24) = 0.375

**Common Pitfalls**
------------------

1. **Failing to account for dependencies**: Ensure events are independent before applying multiplication rule.
2. **Miscalculating conditional probabilities**: Pay attention to the correct formula and application.

**Quick Summary**
-----------------

* Sample space: Set of all possible outcomes
* Event: Subset of the sample space
* Probability measure: Assigns a real number between 0 and 1 to each event
* Conditional probability: P(A|B) = P(A ∩ B) / P(B)
* Key formulas: Multiplication rule, addition rule for 2 events

This comprehensive note covers essential concepts, formulas, and problem-solving strategies for the GATE CS exam in Probability.