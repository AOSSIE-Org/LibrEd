**Array Theory Note**
=======================

### Introduction
---------------

Arrays are a fundamental data structure in programming, allowing for efficient storage and manipulation of collections of elements. This note covers key concepts, formulas, and problem-solving patterns related to arrays, ensuring you're well-prepared for GATE CS exam questions.

### Core Concepts
-----------------

*   **Array Definition**: An array is a collection of elements of the same data type stored in contiguous memory locations.
*   **Array Indexing**: Arrays use 0-based indexing, meaning the first element is at index 0 and the last element at `n-1` (where `n` is the size of the array).
*   **Memory Layout**: Elements are stored in adjacent memory locations.

### Key Formulas/Theorems
-------------------------

None specific to arrays. However, understanding pointer arithmetic is crucial:

$$
p[i] = p + i \cdot sizeof(element)
$$

$$
*(p + i) = (p)[i]
$$

### Problem Solving Patterns
-----------------------------

1.  **Pointer Arithmetic**: Understand how pointers move in memory and how to perform operations like incrementing, decrementing, and calculating offsets.
2.  **Array Indexing**: Recognize that arrays use 0-based indexing and know how to calculate indices for given elements or vice versa.

### Examples with Solutions
---------------------------

**Q1: Output of C Program**
-----------------------------

Given code:
```c
double a[2] = {20.0, 25.0}, *p, *q;

p = a;
q = p + 1;

printf (“%d, %d”, (int) (q – p), (int) (*q – *p));
```

Solution:

*   `q - p` calculates the offset in memory from `a[0]` to `a[1]`, which is `sizeof(double)` or 8 bytes.
*   `*(q - p)` accesses the element at that memory location, which is `25.0`.
*   The correct output should be `(int) q – (int) *p = 8`.

**Q5: Finding an Element in a Multidimensional Array**
------------------------------------------------------

Given code:
```c
#include <stdio.h>

int main() {
    int a[4][5];
    for (i = 0; i < 4; i++)
        for (j = 0; j < 5; j++)
            a[i][j] = 10 * i + j;
    printf("%d", *(a[1] + 9));
}
```

Solution:

*   `a[1]` is the second row, so its first element (`a[1][0]`) would be at address `*(a[1])`.
*   To access `a[1][4]`, add an offset of `sizeof(int) \* 5` to the base address, which gives `*(a[1] + 9)`.

### Common Pitfalls
--------------------

*   Failing to account for array indexing (0-based).
*   Not understanding pointer arithmetic.
*   Misusing multidimensional arrays and pointer expressions.

### Quick Summary
------------------

*   Arrays store elements of the same data type in contiguous memory locations.
*   0-based indexing is used, so the first element is at index 0.
*   Pointer arithmetic allows moving through an array's memory layout efficiently.