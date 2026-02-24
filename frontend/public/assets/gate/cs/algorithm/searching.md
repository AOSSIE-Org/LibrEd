**Searching Theory Note**
=======================

**Introduction**
---------------

Searching is a fundamental algorithmic problem where we aim to find an element or satisfy a condition within a given data structure. In this note, we'll focus on essential concepts and techniques required for solving searching-related questions in the GATE CS exam.

**Core Concepts**
-----------------

### 1. Searching Basics

*   **Searching Problem**: Given a data set `D` and a query element `q`, find an instance of `q` within `D`.
*   **Search Algorithm**: A procedure that takes input `D` and `q` to produce output indicating whether `q` is present in `D`.

### 2. Searching Data Structures

*   **Array**:
    *   Unordered arrays: Linear search, Binary Search
    *   Ordered arrays (sorted): Binary Search
*   **Heap**: Min-heap, Max-heap; heap operations (insertion, deletion)
*   **Balanced BSTs** (e.g., AVL tree, Red-Black tree): insertion, deletion, searching

### 3. Time Complexity Analysis

*   **Best-case, Worst-case, and Average-case time complexities**: definitions and examples
*   **Big O notation**: formal definition and examples of usage

**Key Formulas/Theorems**
-------------------------

*   Binary Search:
    $$
    T(n) = \Theta(\log_2 n)
    $$
*   Linear Search:
    $$
    T(n) = \Theta(n)
    $$

### Heap Properties

*   Min-heap: the parent node is either less than (not greater than) or equal to its child nodes
*   Max-heap: the parent node is either greater than (not less than) or equal to its child nodes

**Problem Solving Patterns**
---------------------------

1.  **Linear Search**: Iterate through all elements in the array, checking for matches.
2.  **Binary Search**: Divide the search space into two halves and repeat until a match is found.

### Example: Linear Search

```markdown
// Find the index of `target` in sorted array `arr`
function linearSearch(arr, target) {
    let low = 0;
    let high = arr.length - 1;

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);

        if (arr[mid] === target) return mid; // Found

        if (arr[mid] < target) low = mid + 1; // Search right half
        else high = mid - 1; // Search left half
    }

    return -1; // Not found
}
```

### Example: Binary Search (sorted array)

```markdown
// Find the index of `target` in sorted array `arr`
function binarySearch(arr, target) {
    let low = 0;
    let high = arr.length - 1;

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);

        if (arr[mid] === target) return mid; // Found

        if (arr[mid] < target) low = mid + 1; // Search right half
        else high = mid - 1; // Search left half
    }

    return -1; // Not found
}
```

**Common Pitfalls**
------------------

*   **Misunderstanding time complexities**: Always consider the worst-case scenario.
*   **Incorrect application of algorithms**: Understand the problem constraints before choosing an algorithm.

### Example: Misapplying Binary Search

```markdown
// Incorrect implementation for searching in an unsorted array using binary search
function binarySearch(arr, target) {
    arr.sort(); // Sorting is not specified or feasible in all cases
    return binarySearchSortedArray(arr, target);
}
```

**Quick Summary**
-----------------

*   Searching: finding an element within a data structure.
*   Linear Search and Binary Search are fundamental searching algorithms.
*   Time complexities are essential for analyzing algorithm efficiency.

### Additional Study Resources

For further study, consult the following:

*   [Data Structures (Arrays, Heaps, BSTs) in GATE CS](https://www.gatevidya.com/gate-cs/data-structures/)

[<-- Previous Note](../previous-note.md)[Next Note -->](../next-note.md)