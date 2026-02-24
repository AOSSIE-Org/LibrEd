**Data Structures and Algorithms**
==============================

**Introduction**
---------------

Data structures are the building blocks of efficient algorithms. They provide a way to organize and store data in a manner that allows for efficient retrieval, manipulation, and storage. In this note, we will cover some of the most commonly used data structures: arrays, stacks, queues, linked lists, trees (binary search trees, binary heaps), and graphs.

**Core Concepts**
-----------------

### Arrays

An array is a collection of elements of the same data type stored in contiguous memory locations. Arrays are indexed, meaning each element can be accessed using its index.

*   **Access Time:** O(1)
*   **Insertion/Deletion Time:** O(n)

```mermaid
graph LR
A[Array] -->|Indexed|> B[Index]
```

### Stacks

A stack is a Last-In-First-Out (LIFO) data structure. Elements are added and removed from the top of the stack.

*   **Access Time:** O(1)
*   **Insertion/Deletion Time:** O(1)

```mermaid
graph LR
A[Stack] -->|Push|> B[Element]
C[Popped Element] <--|Pop|> A
```

### Queues

A queue is a First-In-First-Out (FIFO) data structure. Elements are added to the end of the queue and removed from the front.

*   **Access Time:** O(1)
*   **Insertion/Deletion Time:** O(1)

```mermaid
graph LR
A[Queue] -->|Enqueue|> B[Element]
C[Dequeued Element] <--|Dequeue|> A
```

### Linked Lists

A linked list is a dynamic collection of elements, where each element points to the next element.

*   **Access Time:** O(n)
*   **Insertion/Deletion Time:** O(1)

```mermaid
graph LR
A[Head] -->|Next Pointer|> B[Element]
C[Tail] <--|Previous Pointer|> B
```

### Trees

A tree is a hierarchical data structure, consisting of nodes and edges.

*   **Node:** A node has a value and zero or more child nodes.
*   **Edge:** An edge connects two nodes.

```mermaid
graph LR
A[Root] -->|Edge|> B[Child]
C[Grandchild] <--|Edge|> B
```

### Binary Search Trees (BSTs)

A BST is a type of tree where each node has at most two child nodes and all elements in the left subtree are less than the root, while all elements in the right subtree are greater.

*   **Height:** O(log n)
*   **Search Time:** O(log n)

```mermaid
graph LR
A[Root] -->|Left Child|> B
C[Right Child] <--|Edge|> A
```

### Binary Heaps

A binary heap is a type of BST where the parent node is either greater than (max heap) or less than (min heap) its child nodes.

*   **Height:** O(log n)
*   **Insertion/Deletion Time:** O(log n)

```mermaid
graph LR
A[Root] -->|Left Child|> B
C[Right Child] <--|Edge|> A
```

### Graphs

A graph is a non-linear data structure consisting of nodes and edges.

*   **Node:** A node has zero or more adjacent nodes.
*   **Edge:** An edge connects two nodes.

```mermaid
graph LR
A[Node 1] -->|Edge|> B[Node 2]
C[Node 3] <--|Edge|> B
```

**Key Formulas/Theorems**
-------------------------

### Time Complexity

| Data Structure | Access Time | Insertion/Deletion Time |
| --- | --- | --- |
| Array | O(1) | O(n) |
| Stack | O(1) | O(1) |
| Queue | O(1) | O(1) |
| Linked List | O(n) | O(1) |
| BST | O(log n) | O(log n) |
| Binary Heap | O(log n) | O(log n) |

### Space Complexity

*   Array: O(n)
*   Stack: O(n)
*   Queue: O(n)
*   Linked List: O(n)
*   BST: O(n)
*   Binary Heap: O(n)

**Problem Solving Patterns**
---------------------------

### Arrays

*   Use arrays when the size of the collection is fixed and known.
*   Use array operations (e.g., `push`, `pop`) to implement stacks and queues.

```python
# Implement a stack using an array
class Stack:
    def __init__(self):
        self.array = []

    def push(self, element):
        self.array.append(element)

    def pop(self):
        return self.array.pop()
```

### Linked Lists

*   Use linked lists when the size of the collection is dynamic and unknown.
*   Use pointer operations (e.g., `next`, `previous`) to navigate the list.

```python
# Implement a linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
```

### Trees (BSTs)

*   Use BSTs when the collection needs to be sorted and frequently searched.
*   Use tree traversal algorithms (e.g., inorder, preorder) to navigate the tree.

```python
# Implement a BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = Node(value)
                        break
                    current = current.left
                elif value > current.value:
                    if current.right is None:
                        current.right = Node(value)
                        break
                    current = current.right
```

### Graphs

*   Use graphs when the collection needs to be represented as a network of nodes and edges.
*   Use graph traversal algorithms (e.g., BFS, DFS) to navigate the graph.

```python
# Implement a graph
class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent_nodes = []

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        self.nodes[value] = Node(value)

    def add_edge(self, node1_value, node2_value):
        node1 = self.nodes[node1_value]
        node2 = self.nodes[node2_value]
        node1.adjacent_nodes.append(node2)
        node2.adjacent_nodes.append(node1)
```

**Examples with Solutions**
---------------------------

### Array Example

```python
# Find the maximum element in an array
def max_element(arr):
    return max(arr)

arr = [3, 5, 1, 9]
print(max_element(arr))  # Output: 9
```

### Linked List Example

```python
# Append an element to a linked list
def append(head, value):
    new_node = Node(value)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

head = LinkedList()
append(head, 3)
append(head, 5)
print(head.value)  # Output: 3
```

### BST Example

```python
# Insert an element into a BST
def insert(root, value):
    if root is None:
        return Node(value)
    current = root
    while True:
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
                break
            current = current.left
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
                break
            current = current.right

root = BST()
insert(root, 5)
insert(root, 3)
print(root.value)  # Output: 5
```

### Graph Example

```python
# Add an edge to a graph
def add_edge(graph, node1_value, node2_value):
    node1 = graph.nodes[node1_value]
    node2 = graph.nodes[node2_value]
    node1.adjacent_nodes.append(node2)
    node2.adjacent_nodes.append(node1)

graph = Graph()
add_edge(graph, 3, 5)
print(graph.nodes[3].adjacent_nodes)  # Output: [Node(5)]
```

**Common Pitfalls**
------------------

*   Arrays and linked lists are often confused with each other. Make sure to use the correct data structure for your problem.
*   When using trees (BSTs), make sure to maintain the tree's balance factor to ensure efficient search, insertion, and deletion operations.
*   When working with graphs, make sure to properly implement edge traversal algorithms to avoid infinite loops.

**Quick Summary**
-----------------

| Data Structure | Time Complexity | Space Complexity |
| --- | --- | --- |
| Array | O(1) | O(n) |
| Stack | O(1) | O(n) |
| Queue | O(1) | O(n) |
| Linked List | O(n) | O(n) |
| BST | O(log n) | O(n) |
| Binary Heap | O(log n) | O(n) |

By following this study note, you should be well-prepared to tackle questions related to arrays, stacks, queues, linked lists, trees (BSTs), binary heaps, and graphs. Practice solving problems using these data structures and algorithms to improve your skills.