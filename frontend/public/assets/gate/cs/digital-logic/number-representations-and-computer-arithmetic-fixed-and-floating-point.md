**Number Representations and Computer Arithmetic: Fixed and Floating Point**
====================================================================================

**Introduction**
---------------

Computer arithmetic deals with the representation of numbers in binary form, which is essential for digital logic and computer science. This topic focuses on fixed-point and floating-point representations, including their advantages and disadvantages.

**Core Concepts**
-----------------

### Bit-Level Operations

*   **Bit**: The basic unit of information storage in a computer.
*   **Byte**: A group of 8 bits representing a single character or number.
*   **Shift Operation**: Moving the bits of a binary number to the left (left shift) or right (right shift).
*   **Masking**: Applying a binary mask to select specific bits.

### Fixed-Point Representation

*   **Fixed Point**: A binary number with a fixed position for the radix point.
*   **Sign Bit**: The most significant bit indicating the sign of the number (0 for positive, 1 for negative).
*   **Magnitude Bits**: The remaining bits representing the absolute value of the number.

### Floating-Point Representation

*   **Floating Point**: A binary number with a variable position for the radix point.
*   **Sign Bit**: The most significant bit indicating the sign of the number (0 for positive, 1 for negative).
*   **Exponent Bits**: Representing the power of 2 to which the mantissa should be raised.
*   **Mantissa Bits**: The remaining bits representing the fractional part of the number.

### Endianness

*   **Big Endian**: A system where the most significant byte is stored first (e.g., Intel).
*   **Little Endian**: A system where the least significant byte is stored first (e.g., ARM).

**Key Formulas/Theorems**
-------------------------

$E=mc^2$

(No direct relevance, but a reminder that LaTeX can be used for math formulas)

**Problem Solving Patterns**
---------------------------

### Analyzing Byte Order

*   Identify the endianness of the system.
*   Determine the byte order (big or little).
*   Calculate the numerical value in both systems.

### Converting Between Fixed and Floating Point

*   Understand the representation of fixed-point numbers.
*   Convert fixed-point numbers to floating-point numbers by rearranging bits.
*   Use scaling factors for accurate conversion.

**Examples with Solutions**
---------------------------

### Q1 (cs_2021-N_25)

If the numerical value of a 2-byte unsigned integer on a little-endian computer is 255 more than that on a big-endian computer, which choice represents the unsigned integer on a little-endian computer?

```mermaid
graph LR
A[Start] --> B[Little Endian]
B --> C[Big Endian]
C --> D[Difference of 255]
D --> E[Represented as Unsigned Integer]
E --> F[Choice (B) or (D)]
```

Solution:

| Choice | Description |
| --- | --- |
| A | Incorrect representation |
| B | Correct representation (0 6665 ×) |
| C | Incorrect representation |
| D | Correct representation (0 0100 ×) |

The numerical value of a 2-byte unsigned integer on a little-endian computer is indeed 255 more than that on a big-endian computer. Both choice (B) and (D) represent the correct unsigned integer on a little-endian computer.

**Common Pitfalls**
------------------

*   Confusing endianness when analyzing byte order.
*   Misunderstanding the representation of fixed-point numbers.

**Quick Summary**
-----------------

*   Understand bit-level operations, including shift and masking.
*   Familiarize yourself with fixed-point and floating-point representations.
*   Analyze byte order and convert between fixed and floating point accurately.
*   Be aware of endianness when working with binary data.