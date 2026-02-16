# Recurrence Relation
=======================

## Introduction
---------------

A recurrence relation is an equation that defines a sequence recursively by giving its initial values and specifying how each subsequent value depends on previous ones. It's a fundamental concept in algorithm analysis, used to solve problems involving sequences with overlapping subproblems.

## Core Concepts
-----------------

Recurrence relations are typically expressed as:

$$a_n = f(a_{n-1}, a_{n-2}, ..., a_0)$$

where $f$ is a function of the previous terms. The recurrence relation defines how each term in the sequence depends on its predecessors.

## Key Formulas/Theorems
-----------------------

### Master Theorem

The master theorem provides a general solution for solving linear non-homogeneous recurrence relations with constant coefficients:

**Case 1:** $a_n = a_{n-1} + f(n)$, $f(n) \in O(1)$

$$T(n) = O(n^{\log_b(a)})$$

where $b$ is the branching factor.

### Solving Recurrence Relations

To solve recurrence relations:

1.  **Make an educated guess** for the solution.
2.  **Substitute** the guessed solution into the recurrence relation.
3.  **Verify** that the substitution satisfies the recurrence relation.

## Problem Solving Patterns
---------------------------

### Pattern 1: Constant Multiplication

When a constant is multiplied with each term in the recurrence relation:

```mermaid
graph LR
A[Recurrence Relation] --> B[Constant Multiplied]
```

Use the following formula to solve:

$$T(n) = O(f(n)^{\log_b(a)})$$

where $f(n)$ represents the complexity of the function.

### Pattern 2: Logarithmic Reduction

When a logarithmic reduction occurs in the recurrence relation:

```mermaid
graph LR
A[Recurrence Relation] --> B[Logarithmic Reduction]
```

Use the following formula to solve:

$$T(n) = O(f(\log n)^{\log_b(a)})$$

## Examples with Solutions
---------------------------

### Example 1: Solve using Master Theorem

Solve $T_n = 3T_{\frac{n}{2}} + n^2$

Using master theorem, we get:

*   Case: $a_n = a_{n-1} + f(n)$, $f(n) \in O(1)$
*   Branching factor: $b=2$
*   We have: $$T(n) = O(n^{\log_2(3)}) = O(n^{1.58496})$$

### Example 2: Solve Recurrence Relation with Constant Multiplication

Solve $T_n = 5T_{\frac{n}{2}} + n$

Using the formula for constant multiplication, we get:

*   We have: $$T(n) = O((n)^{\log_2(5)})$$
*   Simplifying, we get: $$T(n) = O(n^{2.32193})$$

## Common Pitfalls
------------------

### Underestimating the Branching Factor

When solving using master theorem, ensure you identify the correct branching factor.

### Missing Subcases

Ensure to check for all possible subcases while applying patterns to solve recurrence relations.

## Quick Summary
---------------

*   **Recurrence Relations**: Define sequences recursively.
*   **Master Theorem**: Solves linear non-homogeneous recurrence relations with constant coefficients.
*   **Solving Recurrence Relations**: Make an educated guess, substitute the guessed solution into the recurrence relation, and verify it satisfies the relation.
*   **Patterns**:
    *   Constant Multiplication
    *   Logarithmic Reduction