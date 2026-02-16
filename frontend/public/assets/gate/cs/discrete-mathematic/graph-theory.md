**Graph Theory Study Note**
==========================

### Introduction
---------------

Graph theory is a branch of discrete mathematics that deals with the study of graphs, which are non-linear data structures consisting of nodes or vertices connected by edges. Graphs can be used to model many real-world systems, such as social networks, transportation networks, and computer networks.

### Core Concepts
-----------------

#### Definition of a Graph

A graph is defined as an ordered pair $G = (V,E)$ where:

*   $V$ is a set of vertices or nodes.
*   $E$ is a set of edges that connect the vertices.

**Example:** A social network can be represented as a graph, where each person is a vertex and each friendship is an edge between two vertices.

#### Types of Graphs

*   **Undirected Graph**: An undirected graph is a graph in which the edges have no direction. For example:
    ```mermaid
    graph LR
    A[Start] --> B[Process]
    ```
    In this graph, there are two edges: $A \rightarrow B$ and $B \rightarrow A$, but they represent the same connection.
*   **Directed Graph**: A directed graph is a graph in which the edges have direction. For example:
    ```mermaid
    graph LR
    A[Start] --> B[Process]
    B --> C[End]
    ```
    In this graph, there are two edges: $A \rightarrow B$ and $B \rightarrow C$. The first edge represents a connection from $A$ to $B$, while the second edge represents a connection from $B$ to $C$.

#### Degree of a Vertex

The degree of a vertex is the number of edges incident on it. For example, in the graph:

    ```mermaid
    graph LR
    A[Start] --> B[Process]
    C --> D[End]
    ```
    The vertex $A$ has degree 1 (one edge), while the vertex $C$ has degree 2 (two edges).

#### Connectivity

A graph is said to be connected if there exists a path between every pair of vertices. For example:

    ```mermaid
    graph LR
    A[Start] --> B[Process]
    B --> C[End]
    ```
    This graph is connected because there are paths from $A$ to $B$, and from $B$ to $C$.

### Key Formulas/Theorems

*   **Handshaking Lemma**: The sum of the degrees of all vertices in a graph is equal to twice the number of edges. Mathematically, this can be represented as:
    $$\sum_{v \in V} deg(v) = 2|E|$$
*   **Euler's Formula for Planar Graphs**: If a graph is planar (can be drawn in a plane without any edge crossings), then the number of vertices ($V$), edges ($E$), and faces ($F$) satisfy the following equation:
    $$V - E + F = 2$$

### Problem Solving Patterns
---------------------------

*   **Path Finding**: Given two vertices $u$ and $v$, find a path from $u$ to $v$. This can be done using graph traversal algorithms such as Depth-First Search (DFS) or Breadth-First Search (BFS).
*   **Shortest Path**: Find the shortest path between two vertices in a weighted graph. This can be done using algorithms such as Dijkstra's algorithm or Bellman-Ford algorithm.

### Examples with Solutions
---------------------------

**Example 1:** A directed acyclic graph (DAG) has a source vertex $s$, and the quality-score of each vertex is defined to be the product of the weights of the edges on the path. The quality-score of $s$ is assumed to be 1.

    ```markdown
    # The given graph

    g
    t
    f
    1
    1
    9
    9
    c
    d
    e
    9
    1
    9
    1
    1
    1
    9
    1
    b
    a
    s

    # Calculate the quality-score of each vertex

    Quality-score(s) = 1
    Quality-score(g) = 1 × 9 = 9
    Quality-score(t) = max(9, 9) = 9
    Quality-score(f) = max(1, 9) = 9
    ...
    ```
**Example 2:** The number of spanning trees in a complete graph with 4 vertices labelled A, B, C, and D is given by the formula:

    $$\text{Number of Spanning Trees} = n^{n-2}$$

    where $n$ is the number of vertices. In this case, $n=4$, so:

    $$\text{Number of Spanning Trees} = 4^{4-2} = 4^2 = 16$$

### Common Pitfalls
------------------

*   **Confusing Directed and Undirected Graphs**: Be careful when dealing with graphs to determine whether they are directed or undirected.
*   **Failing to Account for Multiple Paths**: When calculating the quality-score of a vertex in a DAG, make sure to consider all possible paths from the source vertex.

### Quick Summary
-----------------

*   A graph is an ordered pair $G = (V,E)$ where $V$ is a set of vertices and $E$ is a set of edges.
*   Graphs can be classified into directed and undirected graphs, depending on whether the edges have direction or not.
*   The degree of a vertex is the number of edges incident on it.
*   A graph is connected if there exists a path between every pair of vertices.

This study note covers the fundamental concepts in graph theory, including definitions, types of graphs, and key formulas. It also includes examples with solutions to illustrate how these concepts can be applied to solve problems.