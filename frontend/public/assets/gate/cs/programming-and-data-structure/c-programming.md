**C Programming Study Note**
==========================

### Introduction
---------------

C programming is a fundamental skill for any aspiring computer scientist or software engineer. This study note covers key concepts, formulas, and problem-solving patterns essential for tackling questions on C programming in the GATE CS exam.

### Core Concepts
-----------------

#### Function Evaluation Order
In C, function parameters are evaluated from right to left. This means that when a function is called with multiple arguments, the expressions on the right side of the comma operator are evaluated first.

**Example:**
```c
int g(int p) { printf("%d", p); return p; }
int h(int q) { printf("%d", q); return q; }

void f(int x, int y) {
    g(x);
    h(y);
}
```
In the function `f`, `x` is evaluated first (since it's on the right side of the comma), then its value is passed to `g`. The expression `h(20)` is evaluated next, and so on.

#### Function Evaluation Order Formula

No specific formula for this concept. It's essential to understand how function parameters are evaluated in C.

### Key Formulas/Theorems
-------------------------

None specific to C programming in these notes. However, we'll cover relevant algorithms and data structures later.

### Problem Solving Patterns
-----------------------------

#### Pattern 1: Function Evaluation Order

When solving problems involving function evaluation order, follow these steps:

1. Identify the functions involved.
2. Determine the parameter order (left-to-right or right-to-left).
3. Evaluate each expression from right to left if necessary.

**Example (Q1):**
```c
f(g(10), h(20))
```
In this example, `g(10)` is evaluated first since its expression is on the right side of the comma. Then `h(20)` is evaluated, and finally their values are passed to `f`.

#### Pattern 2: Loop Control

When dealing with loops in C programming, be aware of the following:

* The condition inside a loop (e.g., `i < y`) will always be checked before executing the loop body.
* When incrementing/decrementing variables within a loop, remember that this affects the values used in subsequent iterations.

**Example (Q2):**
```c
for (int i = 0; i < y; i++) {
    x += x + y;
}
```
In this example, the value of `y` remains unchanged throughout the loop. The expression `x + y` is evaluated first, and then the result is added to `x`.

### Examples with Solutions
---------------------------

#### Example 1: Function Evaluation Order

```c
int g(int p) { printf("%d", p); return p; }
int h(int q) { printf("%d", q); return q; }

void f(int x, int y) {
    g(x);
    h(y);
}

int main() {
    f(g(10), h(20));
}
```
**Solution:**

1. Evaluate `g(10)` first: `x = 10`.
2. Evaluate `h(20)` next: `y = 20`.
3. Pass the values to `f`: `f(10, 20)`.

The output will be `20102010`.

#### Example 2: Loop Control

```c
int f(int x, int y) {
    for (int i = 0; i < y; i++) {
        x += x + y;
    }
}

int main() {
    printf("%d", f(1, 3));
}
```
**Solution:**

1. Initialize `i` to 0.
2. Evaluate the condition `i < y`: since `y = 3`, it's always true.
3. Execute the loop body:
	* Increment `x` by `x + y`: `x += x + 3`.
4. Repeat steps 2-3 for `i = 1, 2`.
5. Return the final value of `x`.

The output will be `27`.

### Common Pitfalls
-------------------

#### Inadequate Function Evaluation Order Understanding

Many students forget that function parameters are evaluated from right to left.

**Example:**
```c
int g(int p) { printf("%d", p); return p; }
void f(int x, int y) {
    g(x + y);
}
```
In this example, `x` and `y` are evaluated first (right-to-left order), then their sum is passed to `g`.

### Quick Summary
----------------

* C programming involves function evaluation order from right to left.
* Loops in C involve checking the condition before executing the loop body.
* Be aware of increment/decrement operations within loops.

This study note covers essential concepts and patterns for tackling questions on C programming. Make sure to practice these examples to solidify your understanding!