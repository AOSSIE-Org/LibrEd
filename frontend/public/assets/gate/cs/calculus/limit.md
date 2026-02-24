**Limit Theory Note**
=====================

### Introduction
---------------

The concept of limits is a fundamental principle in calculus, used to define the behavior of functions as they approach a specific value. In this note, we will explore the theoretical foundation of limits and provide examples to illustrate their application.

### Core Concepts
-----------------

*   **Limits**: The limit of a function `f(x)` as `x` approaches `a` is denoted by `\lim_{x\to a} f(x)`. It represents the value that the function approaches as `x` gets arbitrarily close to `a`.
*   **Types of Limits**:
    *   **Right-hand Limit**: `\lim_{x\to a^+} f(x)`
    *   **Left-hand Limit**: `\lim_{x\to a^-} f(x)`
    *   **Two-sided Limit**: `\lim_{x\to a} f(x)` (also denoted as `f(a)` if it exists)

### Key Formulas/Theorems
-------------------------

*   **Definition of a Limit**:
    ```
    \lim_{x\to a} f(x) = L \iff \forall \epsilon > 0, \exists \delta > 0: 
    \forall x \in D(f), (|x-a| < \delta \implies |f(x)-L| < \epsilon)
    ```
*   **Properties of Limits**:
    *   `\lim_{x\to a} [f(x) + g(x)] = \lim_{x\to a} f(x) + \lim_{x\to a} g(x)`
    *   `\lim_{x\to a} [f(x) \cdot g(x)] = (\lim_{x\to a} f(x)) \cdot (\lim_{x\to a} g(x))`
    *   `\lim_{x\to a} \frac{f(x)}{g(x)} = \frac{\lim_{x\to a} f(x)}{\lim_{x\to a} g(x)}`

### Problem Solving Patterns
-----------------------------

*   **Indeterminate Form**: When evaluating a limit and encountering an indeterminate form (`0/0`, `∞/∞`), use algebraic manipulations, L'Hôpital's Rule, or trigonometric identities to simplify the expression.
*   **Limits Involving Trigonometric Functions**:
    *   Use the properties of limits and known values for specific angles (e.g., `\sin(\pi/2) = 1`).
    *   Apply trigonometric identities to rewrite expressions.

### Examples with Solutions
---------------------------

1.  Evaluate `\lim_{x\to 0} \frac{\sin(x)}{x}`:
    ```
    We know that \lim_{x\to 0} \frac{\sin(x)}{x} = 1.
    ```

2.  Find the limit `\lim_{x\to -\infty} (3x^2 + 5x)`:
    ```
    As x approaches -\infty, the quadratic term dominates.
    Therefore, \lim_{x\to -\infty} (3x^2 + 5x) = \lim_{x\to -\infty} 3x^2 = -\infty
    ```

### Common Pitfalls
-------------------

*   Failing to identify the correct type of limit (`one-sided` vs. `two-sided`) or the behavior as `x` approaches a specific value.
*   Misapplying properties of limits (e.g., interchanging limits and derivatives).
*   Neglecting to check for convergence or divergence when evaluating infinite series.

### Quick Summary
-------------------

*   Limits are used to define the behavior of functions as they approach a specific value.
*   Understand types of limits (`right-hand`, `left-hand`, `two-sided`).
*   Familiarize yourself with key formulas and properties.
*   Practice solving problems involving limits, particularly those with indeterminate forms.

**Revision Questions:**

1.  Evaluate `\lim_{x\to \pi} (\sin(x) + \cos(x))`
2.  Find the limit `\lim_{x\to -\infty} (4x^3 - x^2)`