**Complexity Analysis**
=======================

### Introduction
Complexity analysis is a crucial aspect of algorithm design and study. It involves evaluating the time and space requirements of an algorithm, typically expressed as a function of the input size `n`. This allows us to predict how efficiently an algorithm will perform on large inputs.

### Core Concepts

#### Big O Notation
Big O notation is used to describe the upper bound of an algorithm's complexity. It represents the worst-case scenario and is denoted by the symbol K (O). For example, if an algorithm has a time complexity of O(n), it means that the running time will not exceed `cn` for some constant `c`.

#### Big Ω Notation
Big Ω notation is used to describe the lower bound of an algorithm's complexity. It represents the best-case scenario and is denoted by the symbol ℵ (Ω). For example, if an algorithm has a time complexity of Ω(n), it means that the running time will be at least `dn` for some constant `d`.

#### Time Complexity
Time complexity measures how long an algorithm takes to complete as the input size increases. It is usually expressed in terms of big O and big Ω notations.

### Key Formulas/Theorems

*   The Master Theorem:
    ```latex
    \begin{aligned}
        T(n) &amp;= aT\left(\frac{n}{b}\right) + f(n) \\
        \end{aligned}
    ```
    where `a` is the number of subproblems, `b` is the factor by which each subproblem decreases in size, and `f(n)` is the time required to solve each subproblem.

### Problem Solving Patterns

*   **Single-Pass Algorithms**: These algorithms traverse the input once, using each element only once. An example is the bubble sort algorithm.
    ```mermaid
    graph LR;
        A[Start] --> B[Compare adjacent elements];
        C[Swap if necessary] --> D[Repeat until sorted];
    ```
*   **Divide and Conquer**: These algorithms break down the problem into smaller subproblems, solve each one recursively, and combine the results. An example is the merge sort algorithm.
    ```mermaid
    graph LR;
        A[Start] --> B[Divide array into two halves];
        C[Solve each half recursively] --> D[Merge sorted halves];
    ```

### Examples with Solutions

**Example 1:** Analyzing the time complexity of a single-pass sorting algorithm.

Suppose we have an array `[3, 2, 4, 1]` and want to sort it using a single-pass approach. The algorithm compares each element with its adjacent elements and swaps them if necessary.

*   **Step-by-Step Solution:**

    1.  Compare `3` and `2`. Swap since `3 > 2`.
    2.  Compare `4` and `1`. Swap since `4 < 1`.
    3.  Repeat steps 1 and 2 until the array is sorted.

*   **Time Complexity Analysis:**

    The algorithm makes `n-1` comparisons, where `n` is the number of elements in the array. Therefore, the time complexity of this single-pass sorting algorithm is O(n).

**Example 2:** Analyzing the time complexity of a divide-and-conquer sorting algorithm.

Suppose we have an array `[3, 2, 4, 1]` and want to sort it using a divide-and-conquer approach. The algorithm divides the array into two halves, sorts each one recursively, and merges them.

*   **Step-by-Step Solution:**

    1.  Divide the array into two halves `[3, 2]` and `[4, 1]`.
    2.  Recursively sort each half.
    3.  Merge the sorted halves to get the final sorted array.

*   **Time Complexity Analysis:**

    The algorithm has a time complexity of O(n log n) because it divides the array into two halves recursively until each subproblem is small enough to be solved in constant time.

### Common Pitfalls

*   **Underestimating Time Complexity:** Be careful when analyzing algorithms, as even simple-looking ones can have complex time complexities.
*   **Overlooking Lower Bounds:** Always consider both big O and big Ω notations to get a complete picture of an algorithm's complexity.

### Quick Summary

*   Big O notation describes the upper bound (worst-case scenario) of an algorithm's complexity.
*   Big Ω notation describes the lower bound (best-case scenario) of an algorithm's complexity.
*   Time complexity measures how long an algorithm takes to complete as input size increases.
*   Master Theorem helps analyze time complexities of recursive algorithms.

I hope this comprehensive theory note on complexity analysis will help you master the topic and ace your GATE CS exam!