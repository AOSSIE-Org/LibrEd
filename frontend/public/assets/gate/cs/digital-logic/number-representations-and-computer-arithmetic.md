**Number Representations and Computer Arithmetic**
=====================================================

**Introduction**
---------------

In computer science, number representations play a crucial role in digital logic. The IEEE 754 standard defines two floating-point formats: single-precision (32-bit) and double-precision (64-bit). This theory note focuses on the single-precision format.

**Core Concepts**
-----------------

### Floating-Point Representation

The single-precision floating-point representation consists of:

1. **Sign bit**: 1 bit indicating the sign of the number.
2. **Exponent**: 8 bits representing the exponent, which determines the magnitude of the number.
3. **Mantissa**: 23 bits representing the fractional part of the number.

### Normalized Numbers

A normalized number is a floating-point number with a mantissa that has a leading digit of 1 and no trailing zeros. The smallest normalized positive number has an exponent of 00000001 and a mantissa of 10000000...00.

**Key Formulas/Theorems**
-------------------------

### Exponent Representation

The exponent is represented in biased form, where the bias is 127 (for single-precision). The formula for calculating the actual exponent value is:

$$e = E - 127$$

where $E$ is the exponent field value.

### Mantissa Representation

The mantissa is a binary fraction with 23 bits. The leading bit is always 1, and the remaining 22 bits represent the fractional part of the number.

**Problem Solving Patterns**
---------------------------

When solving problems involving floating-point representation, follow these patterns:

1. Identify the sign bit.
2. Calculate the actual exponent value using the biased form formula.
3. Interpret the mantissa as a binary fraction.

### Example: Smallest Normalized Positive Number

Given the IEEE 754 single-precision format, what is the smallest normalized positive number?

**Step 1:** The smallest exponent value is 00000001 ( bias + 1 ).
**Step 2:** Calculate the actual exponent value: $e = E - 127 = 1 - 127 = -126$
**Step 3:** Interpret the mantissa as a binary fraction: $10000000...00$

The correct answer is $(C)$.

### Example: Floating-Point Operations

Given two floating-point numbers A and B, stored in registers as per IEEE 754:

```mermaid
graph LR
A[0x14000000] -->|stored value|> R1
B[0x42100000] -->|stored value|> R2
```

Which of the following statements is false?

**Step 1:** Identify the sign bits: A is positive, B is positive.
**Step 2:** Calculate the actual exponent values using the biased form formula:
$e_A = E_A - 127 = 0x14 - 127 = -123$
$e_B = E_B - 127 = 0x42 - 127 = 15$

The correct answer is $(C)$.

**Common Pitfalls**
-------------------

* Misinterpreting the sign bit.
* Failing to calculate the actual exponent value correctly.
* Incorrectly representing the mantissa as a binary fraction.

**Quick Summary**
-----------------

* Single-precision floating-point representation:
	+ Sign bit: 1 bit
	+ Exponent: 8 bits (biased form)
	+ Mantissa: 23 bits (binary fraction)
* Smallest normalized positive number:
	+ Exponent: 00000001 (bias + 1)
	+ Mantissa: $10000000...00$
* Floating-point operations:
	+ Calculate actual exponent values using biased form formula.