**Linked List**
===============

**Introduction**
---------------

A linked list is a linear data structure where each element (called a node) points to the next node in the sequence. This allows for efficient insertion and deletion of elements at any position in the list.

**Core Concepts**
-----------------

### Node Structure

A node in a linked list typically consists of two parts:

*   `data`: The value stored in the node.
*   `next`: A reference (or link) to the next node in the sequence.

```mermaid
graph LR
    Node -->|data| Data Value
    Node -->|next| Next Node
```

### Linked List Operations

The primary operations on a linked list are:

*   **Insertion**: Adding a new element at a specific position.
*   **Deletion**: Removing an existing element from the list.
*   **Traversal**: Visiting each node in the list.

**Key Formulas/Theorems**
-------------------------

None specifically applicable to linked lists. However, understanding Big-O notation is crucial for analyzing time and space complexities:

*   `O(1)`: Constant time complexity (i.e., operations take the same amount of time regardless of the size of the input).
*   `O(n)`: Linear time complexity (i.e., operations take time proportional to the size of the input).

**Problem Solving Patterns**
---------------------------

### Reversing a Linked List

Given a linked list, reversing it involves changing the direction of the links between nodes. This can be achieved using an iterative approach or recursion.

#### Iterative Approach

```python
def reverse_linked_list(head):
    prev = None
    current = head
    
    while current is not None:
        next_node = current.next  # Store next node before overwriting
        current.next = prev  # Reverse the link
        prev = current  # Move to the new previous node
        current = next_node  # Move to the next node
        
    return prev
```

#### Recursive Approach

```python
def reverse_linked_list(head):
    if head is None or head.next is None:
        return head
    
    new_head = reverse_linked_list(head.next)
    head.next.next = head  # Reverse the link
    head.next = None  # Break the loop
    
    return new_head
```

**Examples with Solutions**
---------------------------

### Example 1: Reversing a Linked List

Suppose we have a linked list `1 -> 2 -> 3 -> 4`. What is the reversed linked list?

Solution:

Using the iterative approach, we can reverse the linked list as follows:

```python
Input: 1 -> 2 -> 3 -> 4
Output: 4 -> 3 -> 2 -> 1
```

### Example 2: Reversing a Linked List (Recursion)

Suppose we have a linked list `5 -> 6 -> 7 -> 8`. What is the reversed linked list?

Solution:

Using the recursive approach, we can reverse the linked list as follows:

```python
Input: 5 -> 6 -> 7 -> 8
Output: 8 -> 7 -> 6 -> 5
```

**Common Pitfalls**
-------------------

*   **Incorrectly Implementing Reversal**: Make sure to correctly implement the reversal logic, either iteratively or recursively.
*   **Not Handling Edge Cases**: Consider edge cases such as empty lists or lists with a single node.

**Quick Summary**
-----------------

*   Linked list: A linear data structure where each element (node) points to the next node.
*   Node structure: `data` and `next` components.
*   Key operations: Insertion, deletion, traversal.
*   Reversing linked lists using iterative or recursive approaches.

Note: This theory note covers the core concepts, key formulas/theorems, problem-solving patterns, examples with solutions, and common pitfalls for the topic of linked lists.