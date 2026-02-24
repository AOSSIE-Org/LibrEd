**Push Down Automata**
======================

### Introduction

A pushdown automaton (PDA) is a type of automaton that uses a stack to remember information about the input. It's an extension of finite automata with the ability to use a stack, which enables it to recognize context-free languages.

### Core Concepts

*   **States**: A PDA has a set of states, denoted as Σ = {s1, s2, ..., sn}.
*   **Stack Symbols**: A PDA uses a stack to store symbols from its stack alphabet Γ.
*   **Transition Function**: The transition function δ(s, a, X) = (s', β), where:
    *   s is the current state
    *   a is the input symbol
    *   X is the top of the stack
    *   s' is the next state
    *   β is the string to be pushed onto the stack
*   **Acceptance**: A PDA accepts an input string if it reaches an accepting state with an empty stack.

### Key Formulas/Theorems

There are no specific formulas or theorems related to pushdown automata. However, we can define a context-free grammar (CFG) using production rules:

`S → AB | ε`

Where `S` is the start symbol, `A` and `B` are non-terminal symbols, and `ε` represents the empty string.

### Problem Solving Patterns

When solving PDA problems, follow these steps:

1.  **Understand the PDA**: Read through the transition function to understand how the PDA operates.
2.  **Draw a diagram**: Visualize the PDA's behavior using a Mermaid diagram or other visual aids.
3.  **Analyze input strings**: Break down each string into its constituent parts and analyze how they interact with the PDA.

### Examples with Solutions

**Example 1**

Consider the following PDA:

|  |  | ε |
| --- | --- | --- |
| s | a, A → p | s' |

The PDA has two states: `s` and `p`. The transition function is defined as follows:

*   When in state `s`, reading an input `a` and having `A` on top of the stack, push `p` onto the stack.

**Solution**

To determine whether a string is accepted by this PDA, we can follow these steps:

1.  Start with an empty stack.
2.  Read each character in the input string.
3.  Apply the transition function based on the current state and top of the stack.
4.  If at any point the stack becomes empty and the PDA is in an accepting state, accept the input.

**Example 2**

Consider the following PDA:

|  |  | ε |
| --- | --- | --- |
| s | a, A → p | s' |

This PDA has two states: `s` and `p`. However, there's no transition defined for reading an input `a` in state `s`.

**Solution**

Since the PDA does not have a defined transition for reading an input `a` in state `s`, it will reject any string that starts with `a`.

### Common Pitfalls

*   **Misunderstanding the transition function**: Make sure to carefully read and understand the PDA's transition function.
*   **Incorrect analysis of stack operations**: Pay close attention to how the stack is modified during each step.
*   **Overlooking acceptance criteria**: Ensure that you're checking for an empty stack in accepting states.

### Quick Summary

*   Pushdown automata use a stack to recognize context-free languages.
*   Transition function: δ(s, a, X) = (s', β)
*   Acceptance: Empty stack in accepting state
*   Examples:
    *   Analyze PDA behavior using diagrams and visual aids.
    *   Follow strict analysis for each input string.