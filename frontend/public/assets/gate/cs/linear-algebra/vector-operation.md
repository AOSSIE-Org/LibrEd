**Vector Operations in Linear Algebra**
=====================================

**Introduction**
---------------

In this note, we will cover the concept of vector operations, specifically the operation defined by $s(P, Q) = \sum_{i=1}^{n} P_i Q_i$, where $P$ and $Q$ are n-dimensional real vectors. We will also analyze a previous year's question to determine the scope and depth required to solve similar questions.

**Core Concepts**
-----------------

A vector is an ordered set of elements, called components or coordinates, that can be added together using the rules of linear combinations. The operation defined by $s(P, Q)$ measures the dot product of two vectors $P$ and $Q$, which is a fundamental concept in linear algebra.

**Key Formulas/Theorems**
-------------------------

The dot product of two vectors $P = (p_1, p_2, ..., p_n)$ and $Q = (q_1, q_2, ..., q_n)$ is defined as:

$$s(P, Q) = \sum_{i=1}^{n} P_i Q_i$$

The dot product satisfies the following properties:

*   Distributivity: $s(P + Q, R) = s(P, R) + s(Q, R)$
*   Scalar multiplication: $s(aP, Q) = as(P, Q)$
*   Commutativity: $s(P, Q) = s(Q, P)$

**Problem Solving Patterns**
---------------------------

To solve problems involving vector operations, follow these steps:

1.  Understand the definition of the operation and its properties.
2.  Analyze the given information and identify what is being asked.
3.  Use the properties of the dot product to simplify the problem.

**Examples with Solutions**

### Example 1

Suppose we have two vectors $P = (1, 2, 3)$ and $Q = (4, 5, 6)$. Find the value of $s(P, Q)$ using the definition:

$$s(P, Q) = \sum_{i=1}^{n} P_i Q_i = (1)(4) + (2)(5) + (3)(6) = 4 + 10 + 18 = 32$$

### Example 2

Consider a set of vectors $\{P_1, P_2, ..., P_n\}$ such that $s(P_i, P_j) = 0$ for all distinct pairs $(i, j)$. What is the maximum cardinality possible for this set?

The answer can be found by using the properties of the dot product and applying them to the given condition. The full solution will be provided in the next section.

**Common Pitfalls**
------------------

When working with vector operations, students often miss the following:

*   Not simplifying the problem using the properties of the dot product.
*   Not identifying what is being asked (e.g., finding the value of $s(P, Q)$ versus finding the maximum cardinality).

**Quick Summary**
-----------------

*   The operation defined by $s(P, Q) = \sum_{i=1}^{n} P_i Q_i$ measures the dot product of two vectors.
*   The dot product satisfies distributivity, scalar multiplication, and commutativity properties.
*   To solve problems involving vector operations, use the definition and properties of the dot product.

**Solution to Example 2**
-------------------------

To find the maximum cardinality possible for the set $\{P_1, P_2, ..., P_n\}$ such that $s(P_i, P_j) = 0$ for all distinct pairs $(i, j)$, we can use the following reasoning:

*   Since $s(P_i, P_j) = 0$, the dot product of any two vectors in the set is zero.
*   This implies that each vector in the set is orthogonal to every other vector.
*   For a set of n-dimensional real vectors, there are at most n mutually orthogonal vectors.
*   Therefore, the maximum cardinality possible for the set $\{P_1, P_2, ..., P_n\}$ is n.

In this case, since the set contains 10-dimensional non-zero real vectors, the maximum cardinality possible is 10.