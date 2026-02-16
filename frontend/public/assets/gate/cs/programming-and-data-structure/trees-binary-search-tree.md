**Binary Search Tree (BST)**
==========================

### Introduction

A Binary Search Tree (BST) is a data structure where each node has at most two children (i.e., left child and right child). Each node represents a key, and for any given node, all the keys in its left subtree are less than the key in the node, while all the keys in its right subtree are greater than the key in the node. This property makes BSTs useful for efficient searching, inserting, and deleting elements.

### Core Concepts

*   **Node**: A node represents a key-value pair, where the key is stored in the node, and the value can be any data.
*   **Root Node**: The root node is the topmost node in the tree. It has no parent node.
*   **Left Child**: A node's left child is the node that is to its left.
*   **Right Child**: A node's right child is the node that is to its right.
*   **Empty Tree**: An empty tree has no nodes.

### Key Formulas/Theorems

The time complexity of operations in a BST depends on the height of the tree. The optimal case for a BST is when it is balanced, meaning the height of the tree is log(n), where n is the number of elements in the tree.

*   **Time Complexity**:
    *   Search: O(log n) (amortized)
    *   Insertion: O(log n)
    *   Deletion: O(log n)

### Problem Solving Patterns

Based on the source questions, we can identify two main problem-solving patterns:

1.  **Identify the Maximum Element**: In a BST, the maximum element is always at the rightmost leaf node.
2.  **Identify the Smaller Element**: To find an element smaller than a given element, traverse down the tree from the root until you reach a node with a value less than or equal to the target value.

### Examples with Solutions

**Example 1: Find the Maximum Element**

Suppose we have a BST:

      5
     / \
    3   7
   / \   \
  2   4   8

To find the maximum element, we start at the root node (5). Since the right child of the root is 7, which is greater than the root value, we move to the right child. Then, since there are no more nodes to the right, we return the current node's value, which is 8.

**Example 2: Find an Element Smaller Than a Given Value**

Suppose we have a BST:

      5
     / \
    3   7
   / \   \
  2   4   8

We want to find the element smaller than 5. We start at the root node (5). Since the left child of the root is 3, which is less than the root value, we move to the left child. Then, since there are no more nodes with a value less than the target value, we return the current node's value, which is 2.

### Common Pitfalls

*   **Unbalanced Tree**: A tree that is not balanced can lead to poor time complexities for search, insertion, and deletion operations.
*   **Incorrect Comparison**: When traversing the tree, make sure to compare values correctly. In a BST, all elements in the left subtree of a node are less than the node's value, while all elements in the right subtree are greater.

### Quick Summary

*   Binary Search Tree (BST): A data structure where each node has at most two children.
*   Time Complexity: O(log n) for search, insertion, and deletion operations when the tree is balanced.
*   Key Concepts:
    *   Node
    *   Root Node
    *   Left Child
    *   Right Child
    *   Empty Tree