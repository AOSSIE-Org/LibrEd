**Stack Operations**
=====================

**Introduction**
---------------

A stack is a linear data structure that follows the Last In First Out (LIFO) principle, where elements are added and removed from the top of the stack. This note covers the theoretical concepts, formulas, and insights required to solve questions related to stack operations.

**Core Concepts**
-----------------

*   A stack can be thought of as a collection of plates stacked on top of each other.
*   The top plate is always accessible and can be removed or added to.
*   When an element is pushed onto the stack, it becomes the new top element.
*   When an element is popped from the stack, the top element is removed.

**Key Formulas/Theorems**
-------------------------

No specific formulas are required for this topic. However, understanding the LIFO principle and how stacks work is essential.

**Problem Solving Patterns**
----------------------------

1.  **Top Element Access**: To access or remove the top element of a stack, you can use the `pop()` operation.
2.  **Element Insertion**: To add an element to the top of a stack, you can use the `push()` operation.

**Examples with Solutions**
---------------------------

### Example 1

Consider the following sequence of operations on an empty stack:

*   `push(54)`
*   `push(52)`
*   `pop()`
*   `push(55)`
*   `push(62)`
*   `s = pop()`

The value of `s` is `62`.

Solution: The `pop()` operation removes the top element, which in this case is `62`. Therefore, the value of `s` is `62`.

### Example 2

Consider the following sequence of operations on an empty queue:

*   `enqueue(21)`
*   `enqueue(24)`
*   `dequeue()`
*   `enqueue(28)`
*   `enqueue(32)`
*   `q = dequeue()`

The value of `q` is `24`.

Solution: The `dequeue()` operation removes the front element, which in this case is `21`. However, since we are interested in finding the value of `q`, and based on the given solution that `q` equals `24`, it implies that after removing 21 from queue, 24 was at the top (head) before another number was enqueued.

### Real-World Scenario

Suppose you have a stack-based system for managing task priorities. You want to add new tasks to the top of the priority list and remove tasks from the top when they are completed. How would you implement this using stacks?

Solution: You can use the `push()` operation to add tasks to the top of the priority list and the `pop()` operation to remove tasks from the top.

**Common Pitfalls**
-------------------

1.  **Confusing Stacks with Queues**: Be aware that stacks follow the LIFO principle, whereas queues follow the First In First Out (FIFO) principle.
2.  **Incorrectly Implementing Operations**: Make sure you understand how to correctly implement stack operations like `push()` and `pop()`.
3.  **Ignoring Edge Cases**: Always consider edge cases when solving problems related to stacks.

**Quick Summary**
----------------

*   A stack is a linear data structure that follows the LIFO principle.
*   Elements are added and removed from the top of the stack using `push()` and `pop()` operations.
*   Be aware of common pitfalls like confusing stacks with queues and incorrectly implementing operations.