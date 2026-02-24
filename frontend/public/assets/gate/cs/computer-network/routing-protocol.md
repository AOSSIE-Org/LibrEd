**Routing Protocol Theory Note**
=====================================

### Introduction
---------------

Routing protocols are essential components of computer networks, enabling efficient data transfer between nodes. In this note, we'll delve into the theoretical concepts and formulas required to tackle questions related to routing protocols.

### Core Concepts
-----------------

#### Routing Tables
A routing table is a data structure used by routers to store information about the network topology, including:

* Destination IP addresses
* Next-hop router IP addresses
* Interface (outbound link) identifiers

Routers use routing tables to make forwarding decisions for incoming packets.

#### Distance Vector Routing
Distance vector routing protocols, such as RIP (Routing Information Protocol), exchange routing table updates between neighboring routers. Each router maintains a copy of its neighbor's routing table and advertises its own routing table to neighbors.

Key aspects:

* **Routing information**: Each entry in the routing table contains the destination IP address, next-hop router IP address, and metric (cost).
* **Update interval**: Routers periodically send updates to their neighbors.
* **Convergence**: When all routers agree on the network topology, they converge on a common set of routing tables.

#### Link State Routing
Link state routing protocols, such as OSPF (Open Shortest Path First), maintain a graph of the network's links and nodes. Each router calculates the shortest path to reach other nodes in the network.

Key aspects:

* **Topology**: Each node maintains a link-state database, which contains information about all nodes and their associated links.
* **Shortest paths**: Routers calculate the shortest path between each pair of nodes using Dijkstra's algorithm or Bellman-Ford algorithm.

### Key Formulas/Theorems
-------------------------

#### Distance Vector Routing

The metric used in distance vector routing is typically hop count, which represents the number of hops (routers) a packet must traverse to reach its destination. The routing table update formula for distance vector routing is:

```latex
D_{ij} = \min(D_{ik} + c_{k(j-i)})
```

where $D_{ij}$ is the metric for reaching node $i$ from node $j$, $c_{k(j-i)}$ is the cost of link $(j-i)$, and $D_{ik}$ is the metric for reaching node $k$ from node $i$.

#### Link State Routing

The shortest path tree (SPT) algorithm, used in link state routing, calculates the shortest path between each pair of nodes. The SPT formula is:

```latex
d(u,v) = \min_{p \in P(u)} d(p,u) + c(u,p) + d(v,p)
```

where $d(u,v)$ is the shortest distance from node $u$ to node $v$, $P(u)$ is the set of nodes in the network, and $c(u,p)$ is the cost of link $(u-p)$.

### Problem Solving Patterns
-----------------------------

1.  **Identify the routing protocol**: Understand whether it's a distance vector or link state protocol.
2.  **Analyze the network topology**: Study the links, nodes, and their costs to determine the shortest path between nodes.
3.  **Use the correct formula**: Apply the relevant formula (e.g., $D_{ij}$ for distance vector routing or SPT algorithm for link state routing).
4.  **Consider convergence**: Ensure all routers agree on the network topology.

### Examples with Solutions
---------------------------

**Example 1: Distance Vector Routing**

Suppose we have a network with three nodes, A, B, and C. Node A has a direct link to node B (cost = 2) and an indirect link to node C through node B (cost = 4). The routing table for node A is:

| Destination | Next-hop | Metric |
| --- | --- | --- |
| B | B | 0 |
| C | B | 4 |

Node A wants to send a packet to node C. Using the distance vector routing formula, we get:

```latex
D_{AC} = \min(D_{AB} + c_{B(C-A)}) = \min(2+4) = 6
```

**Solution**: The shortest path from node A to node C is through node B with a total metric of 6.

### Common Pitfalls
-------------------

*   **Misunderstanding the routing protocol**: Ensure you identify whether it's distance vector or link state.
*   **Incorrect network topology analysis**: Double-check links, nodes, and costs.
*   **Incorrect formula application**: Use the correct formula for the given problem.

### Quick Summary
-----------------

Key concepts covered in this theory note:

*   Routing tables and their contents (destination IP addresses, next-hop router IP addresses, interface identifiers)
*   Distance vector routing protocol (exchange of routing table updates between neighboring routers)
*   Link state routing protocol (maintenance of a graph of the network's links and nodes)
*   Key formulas: distance vector routing ($D_{ij}$), link state routing (SPT algorithm)
*   Problem solving patterns: identify routing protocol, analyze network topology, use correct formula

This comprehensive theory note will help you tackle questions related to routing protocols on the GATE CS exam.