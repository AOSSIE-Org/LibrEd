**Recursion and Loop**
=======================

**Introduction**
---------------

Recursion and loops are fundamental concepts in programming that enable repetitive tasks to be performed efficiently. Recursion involves breaking down a problem into smaller sub-problems, while loops allow for iterative execution of code segments.

**Core Concepts**
-----------------

### Recursion

*   **Definition**: A function that calls itself until it reaches a base case.
*   **Key Properties**:
    *   **Recurrence relation**: The solution to the problem is expressed in terms of smaller sub-problems.
    *   **Base case**: A trivial instance of the problem that can be solved directly.
    *   **Inductive step**: The process of combining solutions to sub-problems to obtain a solution for the original problem.

### Loops

*   **Definition**: Control structures that allow for repetitive execution of code segments.
*   **Types**:
    *   **For loops**: Used for iterating over a sequence or collection of data.
    *   **While loops**: Used for repeating a set of instructions while a condition is true.
    *   **Do-while loops**: Similar to while loops, but the loop body is executed at least once.

### Loop Control Statements

*   **Break**: Terminates the execution of a loop prematurely.
*   **Continue**: Skips to the next iteration of a loop.
*   **Next**: Jumps to the next statement after the current one (not typically used in modern programming).

**Key Formulas/Theorems**
-------------------------

None applicable.

**Problem Solving Patterns**
-----------------------------

### Recursion

*   **Identify the recurrence relation**: Express the problem as a function of smaller sub-problems.
*   **Determine the base case**: Find a trivial instance of the problem that can be solved directly.
*   **Implement the inductive step**: Combine solutions to sub-problems to obtain a solution for the original problem.

### Loops

*   **Choose the correct loop type**: Select a suitable loop structure based on the problem requirements (e.g., for, while, do-while).
*   **Set up the loop control variables**: Initialize and update variables as necessary to control the loop iteration.
*   **Implement the loop body**: Write code that is executed repeatedly within the loop.

**Examples with Solutions**
---------------------------

### Example 1: Recursive Factorial Calculation

```c
int factorial(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}
```

### Example 2: Loop-Based Summation

```c
#include <stdio.h>

int main() {
    int sum = 0, i;

    for (i = 1; i <= 10; i++)
        sum += i;

    printf("%d", sum);

    return 0;
}
```

**Common Pitfalls**
-------------------

*   **Recursion**: Avoiding the base case or not handling edge cases properly can lead to stack overflows.
*   **Loops**: Failing to initialize loop control variables correctly or neglecting to update them within the loop body can result in infinite loops.

**Quick Summary**
----------------

| Topic | Key Points |
| --- | --- |
| Recursion | Break down problems into smaller sub-problems, base case, inductive step |
| Loops | For loops, while loops, do-while loops, loop control statements (break, continue, next) |

Note: This is a starting point for creating comprehensive theory notes. You can expand on the topics and include more examples to make it more exhaustive and helpful.