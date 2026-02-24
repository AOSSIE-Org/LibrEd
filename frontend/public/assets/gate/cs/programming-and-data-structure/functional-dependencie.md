**Functional Dependencies**
=========================

### Introduction
-----------------

In database design and relational algebra, functional dependencies (FDs) are a fundamental concept that helps determine the relationships between attributes of a relation. They play a crucial role in identifying the superkeys of a relation.

### Core Concepts
-----------------

A **functional dependency** is a relationship between two sets of attributes in a relation, where one set determines the other. It's denoted as:

$$X \rightarrow Y$$

where $X$ and $Y$ are subsets of the relation's attribute set.

*   **Determinant**: The left-hand side of the FD ($X$) is called the determinant.
*   **Dependent attributes**: The right-hand side of the FD ($Y$) consists of dependent attributes.

**Examples:**

*   $AB \rightarrow C$: Attribute $C$ depends on both $A$ and $B$.
*   $D \rightarrow C$: Attribute $C$ is determined by attribute $D$ alone.

### Key Formulas/Theorems
-------------------------

No specific formulas or theorems are directly applicable to functional dependencies, but understanding the concepts of determinants and dependent attributes is essential for solving problems related to FDs.

### Problem Solving Patterns
-----------------------------

When dealing with functional dependencies:

1.  **Identify the determinant** ($X$) and the dependent attributes ($Y$).
2.  **Analyze each attribute's influence**: Determine which attributes are determinants of other attributes.
3.  **Determine superkeys**: Find combinations of attributes that satisfy all FDs.

### Examples with Solutions
------------------------------

Consider a relation `R(A, B, C, D, E)` with the following functional dependencies:

*   $AB \rightarrow C$
*   $BC \rightarrow A$
*   $D \rightarrow C$
*   $E \rightarrow A$

**Step 1: Identify determinants and dependent attributes**

| FD | Determinant (X) | Dependent Attributes (Y) |
| --- | --- | --- |
| 1 | AB | C |
| 2 | BC | A |
| 3 | D | C |
| 4 | E | A |

**Step 2: Analyze each attribute's influence**

*   $AB$ determines $C$, and $BC$ determines $A$. This implies that if we have both $A$ and $B$, we can find $C$.
*   Attribute $D$ directly determines $C$.

**Step 3: Determine superkeys**

To find the number of superkeys, identify combinations that cover all determinants:

| Superkey | Reasoning |
| --- | --- |
| A | Contains determinant for FD (4) |
| B | Contains determinant for FD (1) |
| AB | Contains determinants for FDs (1) and (2) |
| AC | Contains determinants for FDs (1) and (3) |
| BC | Contains determinants for FDs (1) and (2), but not D |
| AD | Does not contain the determinant for FD (4) |
| BD | Does not contain the determinant for FD (1) |
| ABCD | Contains all determinants, including D |

There are **8 superkeys**:

*   $A$
*   $B$
*   $AB$
*   $AC$
*   $BC$
*   $AD$ does not qualify as a valid combination
*   $BD$ does not qualify as a valid combination
*   $ABCD$

**Common Pitfalls**
-------------------

1.  **Ignoring transitive dependencies**: If attribute $A$ determines $B$, and attribute $B$ determines $C$, then attribute $A$ also determines $C$. This is known as a transitive dependency.
2.  **Insufficient analysis of determinants and dependent attributes**.

### Quick Summary
-------------------

*   Functional dependencies (FDs) are relationships between attributes in a relation, where one set determines the other.
*   Determinant: The left-hand side of the FD ($X$).
*   Dependent attributes: The right-hand side of the FD ($Y$).
*   To find superkeys, analyze each attribute's influence and determine combinations that cover all determinants.

### Visuals
-------------

No diagrams or images are required for this topic.

This comprehensive theory note covers all theoretical concepts related to functional dependencies, ensuring you're well-prepared to tackle questions like the one provided in the source question (ID: cs\_2022\_52). Practice with sample problems and analyze each concept carefully to excel in your exams.