**Cache Hierarchy**
=====================

### Introduction
-----------------

A cache hierarchy is a multi-level memory hierarchy that consists of multiple caches, each with its own size and access latency. The goal of a cache hierarchy is to provide fast access to frequently accessed data while minimizing the number of accesses to the slower main memory.

### Core Concepts
------------------

#### Cache Hierarchy Structure

A typical cache hierarchy consists of three levels:

1.  **Level 1 (L1) Cache**: The smallest and fastest cache, typically located on the processor chip.
2.  **Level 2 (L2) Cache**: A larger cache that is shared among multiple processors or cores.
3.  **Main Memory**: The largest memory storage unit.

#### Inclusive vs Exclusive Caches

*   **Inclusive Caches**: A cache hierarchy where each level includes all the lines from its lower levels. If a line is present in L1, it must also be present in L2 and main memory.
*   **Exclusive Caches**: A cache hierarchy where each level only contains unique lines not present in its lower levels.

#### Write Policies

*   **Write Through (WT)**: When a processor writes data to the cache, it is immediately written to both the cache and main memory. This policy ensures that the cache and main memory are always consistent.
*   **Write Back (WB)**: When a processor writes data to the cache, it is temporarily stored in the cache until a write-back occurs.

### Key Formulas/Theorems
---------------------------

#### Cache Hit Rate

$$\text{Cache Hit Rate} = \frac{\text{Number of Cache Hits}}{\text{Total Number of Accesses}}$$

#### Average Access Time

$$\text{Average Access Time} = \text{Cache Hit Time} + (1 - P_H) \times (\text{Cache Miss Penalty} + \text{Main Memory Access Time})$$

where $P_H$ is the cache hit probability.

### Problem Solving Patterns
---------------------------

*   Analyze the problem to determine the type of cache hierarchy and write policy used.
*   Understand the trade-offs between different cache sizes, levels, and policies.
*   Use formulas and theorems to calculate metrics such as cache hit rate and average access time.

### Examples with Solutions
-------------------------

**Example 1**

Consider a two-level inclusive cache hierarchy with L2 being larger than L1. Assume that all read misses in the L1 cache result in write-backs of dirty lines to the L2 cache.

*   **Statement 1**: Read misses in a write-through L1 cache do not result in writebacks of dirty lines to the L2.
	+ Solution: False, because write-through caches always update main memory with the latest changes.
*   **Statement 2**: Write allocate policy must be used in conjunction with write-through caches and no-write allocate policy is used with write-back caches.
	+ Solution: True, because write-through caches require write allocation to ensure consistency between cache and main memory.

**Example 2**

Consider a three-level cache hierarchy with L3 being the largest level. Assume that each level has a size of 16 KB, and the miss penalty for L1 is 10 cycles, L2 is 20 cycles, and L3 is 50 cycles.

*   **Solution**: Calculate the average access time using the formula:

$$\text{Average Access Time} = \text{Cache Hit Time} + (1 - P_H) \times (\text{L1 Miss Penalty} + \text{L2 Miss Penalty} + \text{L3 Miss Penalty})$$

Assuming a cache hit probability of 90%, the average access time would be:

$$\text{Average Access Time} = 10 + (1 - 0.9) \times (10 + 20 + 50) = 15 + 8 \times 80 = 15 + 640 = 655 \text{ cycles}$$

### Common Pitfalls
-------------------

*   Confusing inclusive and exclusive caches.
*   Misunderstanding the differences between write-through and write-back policies.

### Quick Summary
-----------------

*   Cache hierarchy consists of multiple levels, each with its own size and access latency.
*   Inclusive caches include all lines from lower levels, while exclusive caches only contain unique lines.
*   Write policies determine how data is written to cache and main memory.
*   Average access time can be calculated using formulas and theorems.

**Cache Hierarchy Structure**

```mermaid
graph LR
    A[Level 1 (L1) Cache] --> B[Level 2 (L2) Cache]
    C[Main Memory] --> D[Level 3 (L3) Cache]
```

Note: This is a basic representation of a three-level cache hierarchy. Inclusive and exclusive caches can be represented similarly.

**External Resources**

*   [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Cache_hierarchy.svg): A diagram illustrating the structure of a cache hierarchy.
*   [Computer Organization and Architecture](https://www.cs.cmu.edu/~gil/462/notes-13.pdf): A lecture note on computer organization and architecture, covering topics related to cache hierarchy.