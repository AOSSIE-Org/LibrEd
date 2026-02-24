**Time Complexity Theory Note**
=====================================

### Introduction
---------------

Time complexity is a fundamental concept in algorithm analysis that measures the amount of time an algorithm takes to complete as a function of the size of its input. It's crucial for evaluating and comparing algorithms' efficiency.

### Core Concepts
-----------------

*   **Asymptotic Notation**: A mathematical notation that describes the limiting behavior of a function as the input size increases.
*   **Big O, Ω, and Θ**: Three types of asymptotic notations used to describe time complexity:

    *   **Big O (Upper Bound)**: The maximum amount of time an algorithm takes.
    *   **Ω (Lower Bound)**: The minimum amount of time an algorithm takes.
    *   **Θ (Theta)**: The average amount of time an algorithm takes.

### Key Formulas/Theorems
-------------------------

*   **Master Theorem**:

    \[T(n) = \begin{cases}
        O(n^{\log_b a}) & \text{if } f(n) = O(n^c), 0 \leq c < d \\
        O(n^d \log n) & \text{if } f(n) = \Theta(n^c), c = d \\
        O(f(g(n)) & \text{otherwise}
    \end{cases}\]

### Problem Solving Patterns
---------------------------

*   **Analyzing Loops**: Count the number of iterations and multiply by the operation cost.

### Examples with Solutions
-------------------------

1.  **Example 1**

    Function: f(n) = n^2

    Complexity: O(n^2)

2.  **Example 2**

    Function: f(n) = 2^n

    Complexity: O(2^n)

3.  **Example 3**

    Function: f(n) = n \* log(n)

    Complexity: O(n log n)

### Common Pitfalls
------------------

*   **Ignoring Constant Factors**: Do not drop constant factors when analyzing time complexity.

### Quick Summary
---------------

*   Time complexity measures an algorithm's performance.
*   Asymptotic notation describes limiting behavior.
*   Big O, Ω, and Θ are used to describe upper bound, lower bound, and average case respectively.
*   Master theorem helps analyze recurrence relations.

Note: This content is a starting point for your GATE CS exam preparation. It is crucial to practice problems from previous years' question papers to solidify your understanding of time complexity concepts.