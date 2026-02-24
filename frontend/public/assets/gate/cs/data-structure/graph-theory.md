**Graph Theory**
================

### Introduction

Graph theory is a branch of mathematics that studies the properties and structures of graphs, which are collections of nodes or vertices connected by edges. In the context of computer science, graph theory has numerous applications in data structures, algorithms, and network analysis.

### Core Concepts

#### 1. Graph Representation

A graph can be represented using two main types:

* **Adjacency Matrix**: A square matrix where the entry at row $i$ and column $j$ represents the weight of the edge between vertex $i$ and $j$. If there is no edge, the entry is usually set to 0.
* **Adjacency List**: An array of lists, where each list contains the vertices adjacent to a particular vertex.

#### 2. Graph Traversal

Graph traversal algorithms visit each node in the graph once. Common types include:

* **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking.
* **Breadth-First Search (BFS)**: Explores all nodes at a given depth before moving to the next depth.

#### 3. Minimum Spanning Tree (MST)

An MST of a graph is a subgraph that connects all vertices with the minimum total edge weight.

#### 4. Chromatic Number

The chromatic number of a graph is the minimum number of colors needed to color each vertex such that no two adjacent vertices have the same color.

### Key Formulas/Theorems

* **Handshaking Lemma**: The sum of degrees of all vertices in a graph is equal to twice the number of edges.
\[ \sum_{v \in V} deg(v) = 2|E| \]
* **Menger's Theorem**: The minimum number of edges that must be removed from an undirected graph to disconnect two vertices is equal to the maximum number of independent paths between those vertices.

### Problem Solving Patterns

#### Minimum Spanning Tree (MST)

* Use Kruskal's algorithm or Prim's algorithm to find the MST.
* Count the number of distinct minimum-weight spanning trees by considering all possible combinations of edges.

#### Chromatic Number

* Check if the graph is bipartite. If so, the chromatic number is 2.
* Apply a greedy coloring algorithm or use a known result for specific types of graphs (e.g., complete graphs).

### Examples with Solutions

**Example 1: Minimum Spanning Tree**

Consider the following graph:

```
   A
  / \
 B---C
  \ /
   D
```

Find the number of distinct minimum-weight spanning trees.

Solution:
Using Kruskal's algorithm, we sort the edges by weight and select them one by one. There are 9 possible combinations of edges that result in a minimum-weight spanning tree:

| Combination | Weight |
| --- | --- |
| (A-B-C-D) | 3-2-1 = 6 |
| (A-C-B-D) | 3-1-2 = 6 |
| ... | ... |

There are 9 distinct combinations.

**Example 2: Chromatic Number**

Consider the following graph:

```
  B---R
 /    \
R---B
 \    /
  B---R
```

Determine the chromatic number of this graph.

Solution:
This graph is bipartite, so its chromatic number is 2.

### Common Pitfalls

* When finding the MST, do not forget to consider all possible combinations of edges.
* When determining the chromatic number, do not assume a graph is complete or regular without proof.

### Quick Summary

* Graph representation: Adjacency matrix and adjacency list
* Graph traversal: DFS and BFS
* Minimum Spanning Tree (MST): Kruskal's algorithm and Prim's algorithm
* Chromatic Number: Check for bipartiteness, use greedy coloring, or apply known results

This comprehensive theory note should provide a solid foundation for tackling graph theory questions on the GATE CS exam.