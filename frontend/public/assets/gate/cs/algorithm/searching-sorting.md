**Searching and Sorting Theory Notes**
=====================================

**Introduction**
---------------

This note covers fundamental concepts of searching and sorting algorithms, which are crucial for solving problems on graphs. Searching and sorting are essential techniques used to manipulate data efficiently.

**Core Concepts**
-----------------

### Graphs

A graph is a non-linear data structure consisting of nodes or vertices connected by edges. It can be directed or undirected, weighted or unweighted. We will focus on undirected weighted graphs for this note.

### Minimum Spanning Tree (MST)

The minimum spanning tree of a weighted graph G = (V, E) is a subgraph that connects all the vertices with the minimum total edge weight. An MST is always unique if the graph has no cycles and has distinct weights.

**Key Formulas/Theorems**
-------------------------

### Kruskal's Algorithm

Kruskal's algorithm builds an MST from scratch by selecting edges in non-decreasing order of their weights until all nodes are connected.

$E = \sum w(e) \text{ where } E = (V, E)$ is the minimum spanning tree of G$

### Prim's Algorithm

Prim's algorithm starts with a node and selects the edge with the smallest weight that connects it to another node, repeating this process until all nodes are connected.

**Problem Solving Patterns**
---------------------------

*   Analyze the problem: Identify the type of graph (connected, disconnected, weighted, unweighted) and what information is given.
*   Choose an appropriate algorithm: Select Kruskal's or Prim's algorithm based on the problem constraints.
*   Implement the algorithm: Write a step-by-step plan to find the minimum spanning tree.

**Examples with Solutions**
---------------------------

### Example 1

Given a connected undirected weighted graph G, show that there exists a minimum edge weight in G which is present in every MST of G.

Solution:

Let `e` be an edge in G with the smallest weight. If there are multiple edges with this weight, select one arbitrarily. Now, consider any MST T of G. Remove `e` from T and try to add it back. Since removing `e` does not disconnect the graph (because it has the minimum weight), adding `e` back will result in a valid MST. Therefore, every MST contains the edge with the smallest weight.

### Example 2

Prove that if every edge in G has distinct weights, then G has a unique MST.

Solution:

Suppose there are two different MSTs T1 and T2 of G. Since the edges have distinct weights, the first differing edge e' will be unique to one of the trees. Assume WLOG that `e'` is part of T1 but not T2. However, since both graphs connect all nodes with minimum total weight, adding `e'` to T2 and removing it from T1 would result in two valid MSTs, contradicting the uniqueness assumption.

### Example 3

Consider a graph G consisting of n vertices connected by k edges. If every edge has distinct weights, how many different MSTs can G have?

Solution:

Since the edges have distinct weights, Kruskal's algorithm will build an MST by selecting each edge in non-decreasing order of their weights. The first differing edge `e'` will determine which tree is built. Given that k edges have distinct weights and each MST is determined uniquely by the sequence of chosen edges, there can be at most 2^(k-1) different MSTs.

**Common Pitfalls**
-----------------

*   Failing to recognize if a graph has cycles or not.
*   Misunderstanding the difference between Kruskal's and Prim's algorithms.
*   Not considering edge weights when building an MST.

**Quick Summary**
----------------

*   A minimum spanning tree is a subgraph that connects all nodes with the minimum total weight.
*   Kruskal's algorithm selects edges in non-decreasing order of their weights to build an MST.
*   Prim's algorithm starts with a node and selects the edge with the smallest weight that connects it to another node.
*   If every edge has distinct weights, then G has a unique MST.

I hope this comprehensive theory note helps students tackle searching and sorting problems in graphs.