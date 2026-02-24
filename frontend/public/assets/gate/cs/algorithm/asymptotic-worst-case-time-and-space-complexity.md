Asymptotic Worst Case Time and Space Complexity
==============================================

Introduction
------------

Asymptotic worst-case time and space complexity are fundamental concepts in algorithm analysis. They provide a way to measure the performance of algorithms by quantifying their time or space requirements as the input size grows.

Core Concepts
---------------

*   **Time Complexity**: The amount of time an algorithm takes to complete as a function of the input size.
*   **Space Complexity**: The amount of memory an algorithm uses as a function of the input size.

Notations
----------

| Notation | Meaning |
| --- | --- |
| $\Theta(f(n))$ | Big Theta: Lower and upper bounds within a constant factor. |
| $O(f(n))$ | Big O: Upper bound, not necessarily tight. |
| $\Omega(f(n))$ | Big Omega: Lower bound, not necessarily tight. |

Key Formulas/Theorems
----------------------

*   **Master Theorem** (for recurrence relations):
    \[T(n) = a \cdot T\left(\frac{n}{b}\right) + f(n)\]
    Where:
    *   $a$ is the number of recursive calls.
    *   $b$ is the size reduction factor.
    *   $f(n)$ is the time complexity of the non-recursive part.

    | Case | Condition |
    | --- | --- |
    1 | $f(n) = O(n^{\log_b a - \epsilon})$ for some $\epsilon > 0$. Then, $T(n) = \Theta(n^{\log_b a})$ |
    2 | $f(n) = \Omega(n^{\log_b a + \epsilon})$ for some $\epsilon > 0$, and $a \geq b$. Then, $T(n) = \Theta(f(n))$ |
    3 | Otherwise. Then, $T(n) = O(n^{\log_b a})$ |

Problem Solving Patterns
-------------------------

*   **Identify Recurrence Relations**: Convert algorithms to recurrence relations.
*   **Solve Using Master Theorem**: Apply the master theorem or case analysis.

Examples with Solutions
------------------------

### Example 1

Consider the following recurrence relation:

\[T(n) = 2 \cdot T\left(\frac{n}{2}\right) + n\]

Using the master theorem, we can determine that this is a Case 1 problem since $f(n) = O(n^{log_2(2)-\epsilon})$ for some $\epsilon > 0$. Thus:

\[T(n) = \Theta(n^{\log_2 2}) = \Theta(n)\]

### Example 2

Consider the following recurrence relation:

\[T(n) = 3 \cdot T\left(\frac{n}{4}\right) + n^2\]

This is a Case 2 problem since $f(n) = O(n^{log_4(3)+\epsilon})$ for some $\epsilon > 0$, and $a \geq b$. Therefore:

\[T(n) = \Theta(f(n)) = \Theta(n^2)\]

Common Pitfalls
----------------

*   **Incorrect Analysis**: Misclassifying a recurrence relation or misunderstanding the master theorem conditions.
*   **Inadequate Case Consideration**: Failing to consider all relevant cases (e.g., ignoring Case 3).

Quick Summary
-------------

*   Time complexity measures an algorithm's performance as input size grows.
*   Space complexity measures an algorithm's memory usage.
*   Master theorem and recurrence relations are key concepts for time complexity analysis.

### Quick References

*   Notations: $\Theta$, $O$, $\Omega$
*   Master Theorem:
    +   Case 1: $T(n) = \Theta(n^{\log_b a})$ when $f(n) = O(n^{\log_b a - \epsilon})$
    +   Case 2: $T(n) = \Theta(f(n))$ when $f(n) = \Omega(n^{\log_b a + \epsilon})$ and $a \geq b$
    +   Case 3: $T(n) = O(n^{\log_b a})$ otherwise