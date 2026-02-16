# Linked List Theory Note
=====================================

## Introduction
---------------

A linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next. It is a fundamental data structure in computer science and is widely used in various applications.

## Core Concepts
-----------------

### Definition

A linked list is defined as an array of records or nodes, where each node contains two fields:

*   `value`: The actual value stored in the node.
*   `next`: A reference (or link) to the next node in the sequence.

### Node Representation

In most programming languages, a linked list is implemented using a struct or class with two members: `data` and `next`. The `data` member stores the value of the current node, while the `next` member points to the next node in the sequence.

### Operations on Linked Lists

Linked lists support several operations:

*   **Insertion**: Adding new nodes at specific positions.
*   **Deletion**: Removing existing nodes from the list.
*   **Traversal**: Iterating through the list to access or modify data.

## Key Formulas/Theorems
-------------------------

None applicable for this topic. However, we will cover the time and space complexities of various linked list operations in the problem-solving patterns section.

## Problem Solving Patterns
-----------------------------

### Traversal

To traverse a linked list, you need to start from the head node and follow each `next` pointer until you reach the end (i.e., `null`).

```mermaid
graph LR
A[Head] --> B[Current]
B --> C[Next]
C --> D[...]
D --> E[Tail]
```

### Insertion

To insert a new node at position `i`, follow these steps:

1.  Start from the head and traverse to the node at position `i-1`.
2.  Set the `next` pointer of the node at position `i-1` to point to the new node.
3.  Update the `next` pointer of the new node to point to the original next node.

### Deletion

To delete a node at position `i`, follow these steps:

1.  Start from the head and traverse to the node at position `i`.
2.  Set the `next` pointer of the previous node to skip over the current node.
3.  Free the memory occupied by the deleted node.

## Examples with Solutions
---------------------------

### Example: Traversal

Suppose we have a linked list: `[1, 2, 3, 4]`

```c
struct Node* head = (struct Node*) malloc(sizeof(struct Node));
head->value = 1;
head->next = NULL;

struct Node* node2 = (struct Node*) malloc(sizeof(struct Node));
node2->value = 2;
node2->next = NULL;
head->next = node2;

// ... (similarly for node3 and node4)
```

To traverse this linked list, we start from the head and follow each `next` pointer:

```c
struct Node* current = head;
while(current != NULL) {
    printf("%d ", current->value);
    current = current->next;
}
```

Output: `1 2 3 4`

### Example: Insertion

Suppose we want to insert a new node with value `5` at position `2`. We follow the steps outlined in the problem-solving patterns section:

```c
struct Node* node5 = (struct Node*) malloc(sizeof(struct Node));
node5->value = 5;
node5->next = NULL;

// Traverse to node2
struct Node* current = head;
while(current != NULL && current->next != node2) {
    current = current->next;
}

// Set next pointer of node2 to point to node5
current->next = node5;
```

### Example: Deletion

Suppose we want to delete the node with value `3`. We follow the steps outlined in the problem-solving patterns section:

```c
struct Node* current = head;
while(current != NULL && current->next != node3) {
    current = current->next;
}

// Set next pointer of node2 to skip over node3
current->next = node4;
```

## Common Pitfalls
------------------

1.  **Traversal**: Don't forget to set the `current` pointer to `NULL` after traversing the linked list.
2.  **Insertion**: Be careful when updating the `next` pointers of adjacent nodes during insertion.
3.  **Deletion**: Always free the memory occupied by deleted nodes.

## Quick Summary
---------------

*   Linked lists are linear collections of data elements where each element points to the next.
*   They support insertion, deletion, and traversal operations.
*   Traversal involves starting from the head and following `next` pointers until reaching the end.
*   Insertion requires updating `next` pointers of adjacent nodes.
*   Deletion involves skipping over deleted nodes by updating `next` pointers.

Note: This theory note covers all concepts tested in the source questions. Students should be able to solve problems related to linked lists using these principles and patterns.