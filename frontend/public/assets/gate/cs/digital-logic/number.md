# Digital Logic: Number System
## Introduction
The number system in digital logic refers to the representation of numbers using different bases or radix, such as binary (base-2), octal (base-8), decimal (base-10), hexadecimal (base-16), and others. Understanding the number system is crucial for representing and manipulating numbers in digital systems.

## Core Concepts
The core concept of the number system is the base or radix, which represents the number of unique digits used to represent a number. The most common bases are:

* Binary (base-2): 0, 1
* Octal (base-8): 0-7
* Decimal (base-10): 0-9
* Hexadecimal (base-16): 0-F

The place value of each digit in a number depends on the base. For example, in binary:

| Place Value | Digit |
| --- | --- |
| $2^3$ | 8 |
| $2^2$ | 4 |
| $2^1$ | 2 |
| $2^0$ | 1 |

## Key Formulas/Theorems
### Base Conversion

To convert a number from one base to another, we can use the following formula:

$$N = d_n \times b^n + d_{n-1} \times b^{n-1} + \cdots + d_0 \times b^0$$

where $N$ is the decimal equivalent of the number in base $b$, $d_i$ are the digits, and $b$ is the base.

### Radix Conversion

To convert a number from one radix to another, we can use the following formula:

$$N = \sum_{i=0}^{n-1} d_i \times b^i$$

where $N$ is the decimal equivalent of the number in radix $b$, $d_i$ are the digits, and $b$ is the radix.

## Problem Solving Patterns
### Pattern 1: Base Conversion

* Identify the base of the given number.
* Convert the number to decimal using the formula: $$N = d_n \times b^n + d_{n-1} \times b^{n-1} + \cdots + d_0 \times b^0$$
* Compare the decimal equivalent with the options.

### Pattern 2: Radix Conversion

* Identify the radix of the given number.
* Convert the number to decimal using the formula: $$N = \sum_{i=0}^{n-1} d_i \times b^i$$
* Compare the decimal equivalent with the options.

## Examples with Solutions

### Example 1:

Convert $121_8$ to decimal.

Solution:
Using the radix conversion formula, we get:

$$N = 1 \times 8^2 + 2 \times 8^1 + 1 \times 8^0$$
$$N = 64 + 16 + 1$$
$$N = 81$$

### Example 2:

Convert $A5_{16}$ to decimal.

Solution:
Using the radix conversion formula, we get:

$$N = 10 \times 16^1 + 5 \times 16^0$$
$$N = 160 + 5$$
$$N = 165$$

## Common Pitfalls

* Not converting the number to decimal before comparing with options.
* Incorrectly applying the conversion formulas.

## Quick Summary
* Understand the concept of base and radix.
* Use the conversion formulas to convert numbers between different bases.
* Be careful when comparing decimal equivalents with options.