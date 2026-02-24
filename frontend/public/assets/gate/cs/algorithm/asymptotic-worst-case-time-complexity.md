**Asymptotic Worst Case Time Complexity**
=====================================

### Introduction
Asymptotic worst-case time complexity refers to the upper bound on the number of steps an algorithm takes to complete, measured as a function of the input size. This concept is crucial in analyzing algorithms' performance and predicting their scalability.

### Core Concepts

#### Recurrence Relations
A recurrence relation is a way of defining a sequence by specifying how each term depends on previous terms. In the context of time complexity analysis, we use recurrence relations to express the running time of an algorithm as a function of the input size.

#### Asymptotic Notation
Asymptotic notation provides a way to describe the growth rate of functions. The three main types of asymptotic notation are:

* O (Big Oh): An upper bound on the number of steps.
* Ω (Big Omega): A lower bound on the number of steps.
* Θ (Theta): Both an upper and lower bound on the number of steps.

#### Master Theorem
The Master Theorem is a powerful tool for solving recurrence relations. It provides a general solution to a wide range of problems and is based on three parameters:

* $a$ : The ratio of the new problem size to the old one.
* $b$ : The cost of solving sub-problems.
* $d$ : The number of sub-problems.

The Master Theorem states that if we have a recurrence relation of the form:
$$T(n) = a \cdot T\left(\frac{n}{b}\right) + d$$
then:

* If $a > 1$, $T(n) = \Theta(n^{\log_b a})$
* If $a < 1$ and $d=o(a^k)$, $T(n) = O(n^{\log_b a})$

```math
\begin{aligned}
\text{Master Theorem} &: T(n) = a \cdot T\left(\frac{n}{b}\right) + d \\
&= 
\begin{cases}
\Theta(n^{\log_b a}), & \text{if }a > 1 \\
O(n^{\log_b a}), & \text{if }a < 1 \land d=o(a^k)
\end{cases} \\
\end{aligned}
```

### Key Formulas/Theorems

#### Master Theorem (Recurrence Relation)

```math
T(n) = 
\begin{cases}
O(1), & \text{if } f(n)=c \\
O(\log n), & \text{if } f(n)=cn^{\alpha}\log^\beta n \\
O(n^\gamma), & \text{if } f(n)=cn^\alpha\log^\beta n
\end{cases}
```

### Problem Solving Patterns

* Identify the recurrence relation and apply the Master Theorem.
* Determine the constants $a$, $b$, and $d$ from the problem statement.
* Use the parameters to determine the time complexity.

### Examples with Solutions

**Example 1:**
Consider the following recurrence relation:
$$T(n) = 2 \cdot T\left(\frac{n}{2}\right) + n$$
Apply the Master Theorem:

```math
a=2, b=2, d=n \\
\log_b a=\log_2 2=1 \\
\text{Since }a>1, T(n)=\Theta(n^{\log_b a})=\Theta(n)
```

**Example 2:**
Consider the following recurrence relation:
$$T(n) = 3 \cdot T\left(\frac{n}{4}\right) + n$$
Apply the Master Theorem:

```math
a=3, b=4, d=n \\
\log_b a=\log_4 3<1 \\
\text{Since }d=o(a^k), T(n)=O(n^{\log_b a})=O(n)
```

### Common Pitfalls

* Misidentifying the recurrence relation or the constants.
* Failing to apply the Master Theorem correctly.

### Quick Summary
* Asymptotic worst-case time complexity is essential in analyzing algorithms' performance.
* Recurrence relations and asymptotic notation are crucial concepts.
* The Master Theorem provides a general solution for solving recurrence relations.
* Apply the Master Theorem by identifying the constants $a$, $b$, and $d$.

This note covers all theoretical concepts, formulas, and insights required to solve the source questions. Practice problems and more examples will help reinforce understanding of these concepts.