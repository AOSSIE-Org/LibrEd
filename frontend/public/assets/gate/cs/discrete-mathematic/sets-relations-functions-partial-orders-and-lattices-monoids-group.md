**Theory Note: Sets, Relations, Functions, Partial Orders and Lattices, Monoids, Group**

### Introduction
Discrete mathematics is a branch of mathematics that deals with mathematical structures that are fundamentally discrete rather than continuous. In this note, we will cover the concepts of sets, relations, functions, partial orders and lattices, monoids, and groups.

### Core Concepts

#### Sets
A set is an unordered collection of distinct objects, known as elements or members. Sets can be represented using curly brackets {} and elements are separated by commas.

* **Set Operations**:
	+ Union: $\bigcup A_i = \{a | a \in \bigcup A_i\}$
	+ Intersection: $\bigcap A_i = \{a | a \in \bigcap A_i\}$
	+ Difference: $A - B = \{a | a \in A \land a \notin B\}$
	+ Symmetric Difference: $A \triangle B = (A \cup B) - (A \cap B)$

#### Relations
A relation is a set of ordered pairs. Relations can be represented using arrows $\rightarrow$ or sets of ordered pairs.

* **Types of Relations**:
	+ Reflexive: $\forall x, xRx$
	+ Irreflexive: $\neg \forall x, xRx$
	+ Symmetric: $\forall x, y, (xRy \Rightarrow yRx)$
	+ Asymmetric: $\forall x, y, (xRy \land yRx \Rightarrow x = y)$

#### Functions
A function is a relation between a set of inputs and a set of possible outputs. Functions can be represented using arrows $f: A \rightarrow B$.

* **Properties**:
	+ Injective (One-to-One): $\forall x, y, f(x) = f(y) \Rightarrow x = y$
	+ Surjective (Onto): $\forall b \in B, \exists a \in A, f(a) = b$
	+ Bijective: Both injective and surjective

#### Partial Orders and Lattices
A partial order is a relation that is reflexive, transitive, and antisymmetric.

* **Properties**:
	+ Reflexive: $\forall x, xRx$
	+ Transitive: $\forall x, y, z, (xRy \land yRz \Rightarrow xRz)$
	+ Antisymmetric: $\forall x, y, (xRy \land yRx \Rightarrow x = y)$

A lattice is a partially ordered set in which every two elements have a least upper bound and a greatest lower bound.

* **Types of Lattices**:
	+ Total Lattice: Every two elements are comparable
	+ Distributive Lattice: The order is distributive over meets and joins

#### Monoids
A monoid is an algebraic structure consisting of a set together with a single associative binary operation on the set that has an identity element.

* **Properties**:
	+ Associative: $\forall x, y, z, (x \circ y) \circ z = x \circ (y \circ z)$
	+ Identity Element: $\exists e, \forall x, e \circ x = x \circ e = x$

#### Groups
A group is an algebraic structure consisting of a set together with a single associative binary operation on the set that has an identity element and every element has an inverse.

* **Properties**:
	+ Associative: $\forall x, y, z, (x \circ y) \circ z = x \circ (y \circ z)$
	+ Identity Element: $\exists e, \forall x, e \circ x = x \circ e = x$
	+ Inverse Element: $\forall x, \exists y, x \circ y = y \circ x = e$

### Key Formulas/Theorems

* **Theorem**: A relation $R$ on a set $A$ is reflexive if and only if $\forall x, xRx$.
* **Theorem**: A relation $R$ on a set $A$ is transitive if and only if $\forall x, y, z, (xRy \land yRz \Rightarrow xRz)$.

### Problem Solving Patterns

* **Identify the Type of Relation**: Given a relation, determine its type (reflexive, irreflexive, symmetric, asymmetric).
* **Apply Function Properties**: When working with functions, apply properties such as injectivity and surjectivity.
* **Lattice Theory**: Familiarize yourself with lattice theory concepts, including total lattices and distributive lattices.

### Examples with Solutions

**Example 1**

Suppose we have a set $A = \{a, b, c\}$ and a relation $R$ defined as:

$$
R = \{(a, b), (b, c), (c, a)\}
$$

Is the relation $R$ symmetric?

Solution:
Yes, since $\forall x, y, (xRy \Rightarrow yRx)$.

**Example 2**

Consider the set $A = \{1, 2, 3\}$ and the function $f: A \rightarrow A$ defined as:

$$
f(x) = x^2
$$

Is the function $f$ injective?

Solution:
No, since $f(1) = f(-1)$ but $1 \neq -1$.

**Example 3**

Let $A = \{a, b\}$ and $B = \{c, d\}$. What is the symmetric difference of $A$ and $B$?

Solution:
$$
A \triangle B = (A \cup B) - (A \cap B)
$$

### Common Pitfalls

* **Confusing Reflexive with Transitive**: Remember that a reflexive relation has $\forall x, xRx$, while a transitive relation has $\forall x, y, z, (xRy \land yRz \Rightarrow xRz)$.
* **Mixing Up Function Properties**: Be careful not to confuse injectivity and surjectivity. If $f$ is injective, then $\forall x, y, f(x) = f(y) \Rightarrow x = y$. If $f$ is surjective, then $\forall b \in B, \exists a \in A, f(a) = b$.

### Quick Summary

* **Key Concepts**:
	+ Sets
	+ Relations (reflexive, irreflexive, symmetric, asymmetric)
	+ Functions (injective, surjective, bijective)
	+ Partial Orders and Lattices
	+ Monoids
	+ Groups
* **Important Formulas/Theorems**:
	+ Reflexivity: $\forall x, xRx$
	+ Transitivity: $\forall x, y, z, (xRy \land yRz \Rightarrow xRz)$
* **Problem Solving Patterns**:
	+ Identify the type of relation
	+ Apply function properties
	+ Familiarize yourself with lattice theory concepts

Please note that this is a comprehensive theory note covering all the required topics. The examples and solutions provided are just illustrations to help understand the concepts better.