**Combinatorics Theory Notes**
===========================

### Introduction

Combinatorics is a branch of mathematics that deals with counting and arranging objects, often used to solve problems in computer science, engineering, and other fields. It involves the study of permutations, combinations, and other counting techniques.

### Core Concepts

#### Permutations

A permutation is an arrangement of objects in a specific order. For example, if we have three distinct objects: A, B, and C, there are 6 possible permutations:

1. ABC
2. ACB
3. BAC
4. BCA
5. CAB
6. CBA

The number of permutations can be calculated using the formula: n! = n × (n-1) × ... × 2 × 1, where n is the number of objects.

#### Combinations

A combination is a selection of objects from a larger set, without considering the order. For example, if we have three distinct objects: A, B, and C, there are 4 possible combinations:

1. ABC
2. AB
3. AC
4. BC

The number of combinations can be calculated using the formula: nCr = n! / (r!(n-r)!), where n is the total number of objects and r is the number of objects being selected.

#### Principles of Counting

There are several principles of counting that are essential in combinatorics:

* **The Addition Principle**: If there are m ways to perform one task and n ways to perform another task, then there are m + n ways to perform either task.
* **The Multiplication Principle**: If there are m ways to perform one task and n ways to perform another task, then there are m × n ways to perform both tasks.

### Key Formulas/Theorems

$P(n) = n!$

$C(n,r) = \frac{n!}{r!(n-r)!}$

$\binom{n}{k} = \frac{n!}{k!(n-k)!}$

### Problem Solving Patterns

When solving combinatorics problems, the following patterns can be useful:

* **Break down complex problems into smaller sub-problems**: Divide the problem into manageable parts and solve each part separately.
* **Use formulas and theorems to simplify calculations**: Apply mathematical formulas and theorems to reduce the complexity of the problem.

### Examples with Solutions

**Example 1**

A rectangular paper sheet of dimensions 54cm × 4cm is taken. The two longer edges of the sheet are joined together to create a cylindrical tube. A cube whose surface area is equal to the area of the sheet is also taken. What is the ratio of the volume of the cylindrical tube to the volume of the cube?

**Solution**

Surface area of rectangular sheet = 54 × 4 = 216 cm²

Circumference of cylinder = 2πr
h = 4cm
r = 54cm / (2π) = 8.63cm

Volume of cylindrical tube = πr² h = π(8.63)² × 4 = 1175.51 cm³

Cube surface area = 6a² = 216 cm²
a = √(36) = 6 cm
Volume of cube = a³ = 216 cm³

Ratio of volumes = Volume of cylindrical tube : Volume of cube = 1175.51 : 216 ≈ 5.43 : 1 ≈ π / (2π/4) = 2π / 2 = π

**Example 2**

A group of 6 friends want to sit in a row for a photo. If the order matters, how many ways can they sit?

**Solution**

Using permutations formula: P(n) = n!
n = 6
P(6) = 6! = 720

### Common Pitfalls

* **Forgetting to consider order**: Make sure to account for permutations when the order matters.
* **Overcounting or undercounting**: Double-check calculations to avoid errors.

### Quick Summary

* Permutations: Calculate using n!
* Combinations: Calculate using nCr = n! / (r!(n-r)!)
* Principles of counting:
	+ Addition Principle
	+ Multiplication Principle
* Formulas and theorems:
	+ P(n) = n!
	+ C(n,r) = n! / (r!(n-r)!)

Note: This is a basic introduction to combinatorics. For more advanced topics, additional study materials may be required.