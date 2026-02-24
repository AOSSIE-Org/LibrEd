Arrays, Stacks, Queues, and Linked Lists
=====================================

Introduction
------------

Arrays, stacks, queues, and linked lists are fundamental data structures used in computer science. They provide efficient ways to store and manipulate large amounts of data. Understanding these data structures is essential for programming and problem-solving.

Core Concepts
-------------

### Arrays

An array is a collection of elements of the same data type stored in contiguous memory locations.

*   **Indexing**: Arrays are indexed, meaning each element can be accessed using an index or subscript.
*   **Fixed Size**: The size of an array is fixed at compile time and cannot be changed during execution.

### Stacks

A stack is a last-in-first-out (LIFO) data structure, where the most recently added element is removed first.

*   **Push**: Adding an element to the top of the stack.
*   **Pop**: Removing an element from the top of the stack.

### Queues

A queue is a first-in-first-out (FIFO) data structure, where the first added element is removed first.

*   **Enqueue**: Adding an element to the end of the queue.
*   **Dequeue**: Removing an element from the front of the queue.

### Linked Lists

A linked list is a dynamic collection of elements, where each element points to the next one.

*   **Node**: Each element in a linked list is called a node.
*   **Pointer**: Each node contains a pointer to the next node.

Key Formulas/Theorems
--------------------

None specific to this topic

Problem Solving Patterns
----------------------

1.  **Array Indexing**:
    *   Use `a[i][j][k]` for multi-dimensional arrays.
2.  **Stack Operations**:
    *   Use `push` and `pop` operations for stacks.
3.  **Queue Operations**:
    *   Use `enqueue` and `dequeue` operations for queues.

Examples with Solutions
----------------------

### Example 1: Array Indexing

```c
int a[3][3] = {{1, 2}, {3, 4}};
printf("%d %d", a[0][0], a[1][1]);
```

Output:

*   `1 4`

Explanation:

*   We use `a[0][0]` to access the element at row 0, column 0.
*   We use `a[1][1]` to access the element at row 1, column 1.

### Example 2: Stack Operations

```c
#include <stdio.h>

void push(int *stack, int new_element) {
    stack[++top] = new_element;
}

int pop(int *stack) {
    return stack[top--];
}

int main() {
    int stack[10];
    top = -1;
    push(stack, 5);
    push(stack, 3);
    printf("%d", pop(stack));
    return 0;
}
```

Output:

*   `3`

Explanation:

*   We use the `push` function to add elements to the stack.
*   We use the `pop` function to remove an element from the stack.

Common Pitfalls
----------------

1.  **Array Indexing**:
    *   Off-by-one errors when accessing array indices.
2.  **Stack Operations**:
    *   Using `push` and `pop` operations on queues, or vice versa.
3.  **Queue Operations**:
    *   Using `enqueue` and `dequeue` operations on stacks, or vice versa.

Quick Summary
--------------

*   Arrays: Fixed-size collection of elements, indexed using subscripts.
*   Stacks: LIFO data structure, with push and pop operations.
*   Queues: FIFO data structure, with enqueue and dequeue operations.
*   Linked Lists: Dynamic collection of elements, with pointers between nodes.