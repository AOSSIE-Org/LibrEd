**Big O Notation Analysis**
==========================

### Introduction

Big O notation analysis is a crucial aspect of algorithm design and complexity theory. It provides an upper bound on the time or space complexity of an algorithm, allowing us to predict its performance as the input size increases.

### Core Concepts

* **Time Complexity**: The amount of time an algorithm takes to complete, typically measured in terms of the number of operations (e.g., comparisons, assignments).
* **Space Complexity**: The amount of memory used by an algorithm.
* **Big O Notation**: A mathematical notation that describes the upper bound on an algorithm's complexity.

### Key Formulas/Theorems

#### Asymptotic Notations

| Notation | Description |
| --- | --- |
| O(g(n)) | Upper bound (at most) |
| Ω(g(n)) | Lower bound (at least) |
| Θ(g(n)) | Tight bound (exactly) |

#### Big O Operations

| Operation | Complexity |
| --- | --- |
| Assignment | O(1) |
| Comparison | O(1) |
| Loop Iteration | O(n), O(log n), ... |
| Array Access | O(1) |

### Problem Solving Patterns

When analyzing the time or space complexity of an algorithm, consider:

* **Loop Iterations**: Count the number of iterations and multiply by the operation inside the loop.
* **Recursion**: Analyze the recursive calls and their impact on the overall complexity.

### Examples with Solutions

**Example 1: Finding the Maximum Element in an Array**

```python
def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val
```

Time Complexity: O(n), where n is the length of the array.

**Example 2: Bubble Sort**

```python
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

Time Complexity: O(n^2), where n is the length of the array.

### Common Pitfalls

* **Overlooking Loop Iterations**: Failing to account for loop iterations can lead to incorrect time complexity analysis.
* **Ignoring Recursive Calls**: Neglecting recursive calls can result in a misunderstanding of an algorithm's overall complexity.

### Quick Summary

* Big O notation provides an upper bound on the time or space complexity of an algorithm.
* Time and space complexities are essential in understanding an algorithm's performance.
* Loop iterations, recursive calls, and array access operations impact complexity analysis.

Note: This theory note is designed to cover the concepts tested in the source question (Q1). Additional examples and explanations can be added as needed.