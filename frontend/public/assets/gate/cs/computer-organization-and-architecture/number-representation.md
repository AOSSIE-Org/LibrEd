**Number Representation**
========================

### Introduction
-----------------

Number representation is a fundamental concept in computer organization and architecture, enabling computers to process and store numerical data. In this section, we will delve into the principles of number representation, focusing on binary, decimal, and hexadecimal systems.

### Core Concepts
------------------

#### Binary Number System
The binary number system uses base 2, consisting of only two digits: 0 and 1. This system is essential for computer architecture as it directly relates to the physical implementation of digital circuits.

*   **Binary Digits**: A single binary digit is called a bit (binary digit).
*   **Binary Number**: A sequence of bits represents a binary number.
*   **Weighted Binary**: Each bit in a weighted binary system has an associated weight, which can be 1, 2, 4, 8, or any power of 2.

#### Decimal and Hexadecimal Systems
While the binary system is used for digital circuitry, decimal (base 10) and hexadecimal (base 16) systems are more intuitive for humans. Understanding these systems is crucial for converting between representations.

*   **Decimal System**: Uses digits 0-9.
*   **Hexadecimal System**: Uses digits 0-9 and letters A-F (A=10, B=11, ..., F=15).

### Key Formulas/Theorems
---------------------------

The following formulas are essential for number representation:

*   **Binary-to-Decimal Conversion**:
    $$D = b_{n} \times 2^{n} + b_{n-1} \times 2^{n-1} + ... + b_{0} \times 2^{0}$$
    where $D$ is the decimal equivalent and $b_i$ are the binary digits.
*   **Decimal-to-Binary Conversion**:
    The process of converting a decimal number to its equivalent binary representation involves repeated division by 2 and noting the remainders.

### Problem Solving Patterns
-----------------------------

To solve questions on number representation, consider the following patterns:

1.  **Identify the Number System**: Determine whether the problem deals with binary, decimal, or hexadecimal numbers.
2.  **Understand the Operation**: Clearly define the operation involved (e.g., addition, subtraction, multiplication, division).
3.  **Apply Conversion Formulas**: Use conversion formulas to switch between number systems as required.

### Examples with Solutions
---------------------------

**Example 1: Binary-to-Decimal Conversion**

Given binary number $101_2$, find its decimal equivalent using the formula above:

$$D = 1 \times 2^{2} + 0 \times 2^{1} + 1 \times 2^{0} = 4 + 0 + 1 = 5_{10}.$$

**Example 2: Decimal-to-Binary Conversion**

Convert decimal number $12_{10}$ to its binary representation using repeated division by 2:

*   $12 \div 2 = 6$ remainder 0
*   $6 \div 2 = 3$ remainder 0
*   $3 \div 2 = 1$ remainder 1
*   $1 \div 2 = 0$ remainder 1

Therefore, the binary representation of $12_{10}$ is $1100_2$.

### Common Pitfalls
-------------------

*   **Misunderstanding Binary Weights**: Be aware that each bit in a weighted binary system has an associated weight.
*   **Incorrect Conversion**: Double-check conversions between number systems to ensure accuracy.

### Quick Summary
------------------

Key points for revision:

*   **Binary System**: Base 2, uses digits 0 and 1, crucial for computer architecture.
*   **Decimal and Hexadecimal Systems**: More intuitive for humans, but conversion formulas are essential.
*   **Conversion Formulas**: Apply binary-to-decimal and decimal-to-binary conversion formulas correctly.

This comprehensive theory note covers the fundamental concepts of number representation in computer organization and architecture. By mastering these principles, you will be well-equipped to tackle questions on this topic in the GATE CS exam.