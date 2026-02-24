**Recurrence Relation in Combinatorics**
=====================================

**Introduction**
---------------

A recurrence relation is a mathematical equation that defines a sequence recursively, where each term is defined as a function of previous terms. In combinatorial problems, recurrence relations are often used to count the number of ways to perform certain tasks, such as arranging objects or making choices.

**Core Concepts**
-----------------

*   **Recurrence Relation**: A relation between consecutive terms in a sequence, where each term is defined recursively.
*   **Initial Conditions**: The starting values of the sequence, which are typically specified explicitly.
*   **Recursive Formula**: An equation that defines each term in the sequence as a function of previous terms.

**Key Formulas/Theorems**
------------------------

### Fibonacci Sequence

The Fibonacci sequence is a classic example of a recurrence relation:

$$F(n) = \begin{cases} F(1) &\text{if } n=1 \\ F(2) &\text{if } n=2 \\ F(n-1) + F(n-2) &\text{otherwise} \end{cases}$$

where $F(n)$ is the $n$th Fibonacci number.

### Binet's Formula

Binet's formula provides an explicit expression for the $n$th Fibonacci number:

$$F(n) = \frac{\phi^n - (1-\phi)^n}{\sqrt{5}}$$

where $\phi = \frac{1+\sqrt{5}}{2}$.

**Problem Solving Patterns**
---------------------------

### Cutting a Rod Problem

The problem presented in source question Q1 can be solved using a recurrence relation:

$$R(n) = \max_{i=1}^n (p(i) + R(n-i))$$

where $R(n)$ is the maximum revenue obtainable by cutting a rod of length $n$.

### Solving Recurrence Relations

To solve a recurrence relation, we can use various techniques such as:

*   **Unfolding**: Expanding the recurrence relation to obtain an explicit expression.
*   **Guessing**: Making educated guesses about the form of the solution based on the initial conditions and recursive formula.
*   **Substitution**: Substituting different values for $n$ to obtain a system of equations.

**Examples with Solutions**
-------------------------

### Cutting a Rod Problem

Suppose we want to cut a rod of length 7 into one or more pieces of integer length. We are given the prices per meter:

| Length | Price (per meter) |
| --- | --- |
| 1     | 1                |
| 2     | 5                |
| 3     | 8                |
| 4     | 9                |
| 5     | 10               |
| 6     | 17               |
| 7     | 13               |

We can use the recurrence relation to solve for $R(7)$:

$$R(7) = \max_{i=1}^7 (p(i) + R(7-i))$$

Using the given prices, we have:

*   $R(1) = p(1) = 1$
*   $R(2) = p(2) = 5$
*   $R(3) = \max(p(3), p(2)+R(1)) = \max(8, 6) = 8$
*   $R(4) = \max(p(4), p(2)+R(2)) = \max(9, 10) = 10$
*   $R(5) = \max(p(5), p(3)+R(2)) = \max(10, 13) = 13$
*   $R(6) = \max(p(6), p(4)+R(2)) = \max(17, 15) = 17$
*   $R(7) = \max(p(7), p(5)+R(2)) = \max(13, 18) = 18$

Therefore, the maximum revenue obtainable by cutting a rod of length 7 is 18.

### Fibonacci Sequence

Suppose we want to find the 10th Fibonacci number using Binet's formula:

$$F(n) = \frac{\phi^n - (1-\phi)^n}{\sqrt{5}}$$

We can calculate $F(10)$ as follows:

*   $\phi^{10} = (\frac{1+\sqrt{5}}{2})^{10}$
*   $(1-\phi)^{10} = (\frac{1-\sqrt{5}}{2})^{10}$
*   $F(10) = \frac{\phi^{10} - (1-\phi)^{10}}{\sqrt{5}}$

Using a calculator or computational tool, we can evaluate the expression to obtain:

$$F(10) = 55$$

**Common Pitfalls**
-------------------

When solving recurrence relations, students often miss the following:

*   **Initial Conditions**: Failing to specify the initial conditions correctly can lead to incorrect solutions.
*   **Recursive Formula**: Misunderstanding or misapplying the recursive formula can result in errors.

**Quick Summary**
-----------------

Recurrence relation is a mathematical equation that defines a sequence recursively, where each term is defined as a function of previous terms. To solve recurrence relations, we can use techniques such as unfolding, guessing, and substitution. Common pitfalls include initial conditions and recursive formulas.

### References

*   [1] "Introduction to Algorithms" by Thomas H. Cormen
*   [2] "Discrete Mathematics and Its Applications" by Kenneth H. Rosen