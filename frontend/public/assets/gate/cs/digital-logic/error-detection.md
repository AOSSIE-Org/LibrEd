**Error Detection**
====================

### Introduction

Error detection is a crucial aspect of digital communication systems. It involves detecting errors that occur during data transmission, storage, or processing. In this note, we'll focus on cyclic redundancy check (CRC) based error detecting schemes.

### Core Concepts

#### Cyclic Redundancy Check (CRC)

A CRC is an error-detecting code used to detect errors in digital data transmission. It appends a small number of check bits to the message before transmission. The receiver can then use these check bits to detect if any errors occurred during transmission.

**Theorem**: A CRC can detect all single-bit and two-bit errors, as well as odd-numbered multi-bit errors.

#### Generator Polynomial

A generator polynomial is a binary polynomial used in CRC calculations. It's typically represented in the form of $g(x) = g_0x^n + g_1x^{n-1} + \ldots + g_n$, where $g_i$ are coefficients and $n$ is the degree of the polynomial.

#### Message Polynomial

A message polynomial is a binary polynomial representing the data being transmitted. It's typically represented in the form of $m(x) = m_0x^n + m_1x^{n-1} + \ldots + m_n$, where $m_i$ are coefficients and $n$ is the degree of the polynomial.

### Key Formulas/Theorems

* **CRC Calculation**: The CRC check bits are calculated using the formula:
$$
c(x) = (m(x) \cdot g(x)) \mod (x^n + 1)
$$
where $c(x)$ is the polynomial representing the check bits, $m(x)$ is the message polynomial, and $g(x)$ is the generator polynomial.

* **Error Detection**: The receiver can detect errors using the formula:
$$
E = c(x) \cdot g(x)
$$
where $E$ is the error value, and $c(x)$ and $g(x)$ are the polynomials used in CRC calculations.

### Problem Solving Patterns

1.  **Understand the generator polynomial**: Make sure to understand the structure of the generator polynomial, as it's essential for calculating the CRC check bits.
2.  **Apply the CRC calculation formula**: Use the formula $c(x) = (m(x) \cdot g(x)) \mod (x^n + 1)$ to calculate the CRC check bits.

### Examples with Solutions

**Example 1:**

Suppose we have a message polynomial $m(x) = x^3 + x^2 + 1$ and a generator polynomial $g(x) = x^4 + x^3 + 1$. We want to calculate the CRC check bits using this scheme.

```mermaid
graph LR
    A[Message Polynomial] --> B[m(x)]
    B[x^3 + x^2 + 1]
    C[Generator Polynomial] --> D[g(x)]
    D[x^4 + x^3 + 1]
```

Using the CRC calculation formula, we get:

$$
c(x) = (x^3 + x^2 + 1 \cdot x^4 + x^3 + 1) \mod (x^8 + 1)
$$

Simplifying this expression, we get $c(x) = x^7 + x^6 + x^5$.

**Example 2:**

Suppose we have a message polynomial $m(x) = x^4 + x^3 + x^2 + x + 1$ and a generator polynomial $g(x) = x^8 + x^7 + 1$. We want to calculate the CRC check bits using this scheme.

```mermaid
graph LR
    A[Message Polynomial] --> B[m(x)]
    B[x^4 + x^3 + x^2 + x + 1]
    C[Generator Polynomial] --> D[g(x)]
    D[x^8 + x^7 + 1]
```

Using the CRC calculation formula, we get:

$$
c(x) = (x^4 + x^3 + x^2 + x + 1 \cdot x^8 + x^7 + 1) \mod (x^{16} + 1)
$$

Simplifying this expression, we get $c(x) = x^{15} + x^{14} + \ldots + x^9$.

### Common Pitfalls

*   Failing to understand the generator polynomial and its structure.
*   Not applying the CRC calculation formula correctly.

### Quick Summary

*   Cyclic redundancy check (CRC) is an error-detecting code used in digital communication systems.
*   The generator polynomial and message polynomial are essential components of a CRC scheme.
*   The CRC check bits can be calculated using the formula $c(x) = (m(x) \cdot g(x)) \mod (x^n + 1)$.

Note: This is a comprehensive theory note on error detection, specifically focusing on cyclic redundancy check (CRC) based schemes. It covers key concepts, formulas, and problem-solving patterns to help students prepare for the GATE CS exam.