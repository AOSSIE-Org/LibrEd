**Random Variable**
=====================

### Introduction
A random variable is a function that assigns a real number to each outcome of an experiment or a set of outcomes. It's a crucial concept in probability and statistics, allowing us to quantify uncertainty and make informed decisions.

### Core Concepts
#### Definition
Given an experiment with possible outcomes $\Omega$, a random variable $X$ is a function that maps each outcome $\omega \in \Omega$ to a real number $x \in \mathbb{R}$.

#### Types of Random Variables
* **Discrete random variables**: Take on distinct, countable values (e.g., number of heads in coin tosses).
* **Continuous random variables**: Can take any value within a given interval or range (e.g., temperature, lifetime of a component).

#### Probability Distribution Functions
A probability distribution function (pdf) $f(x)$ describes the probability of observing a particular value $x$.

### Key Formulas/Theorems

#### Exponential Distribution
For an exponentially distributed random variable with parameter $\lambda$, the pdf is given by:

$$f(x) = \begin{cases} \lambda e^{-\lambda x} & x \geq 0 \\ 0 & x < 0 \end{cases}$$

The expected value and variance of an exponential distribution are:

$E(X) = \frac{1}{\lambda}$

$Var(X) = \frac{1}{\lambda^2}$

#### Binomial Distribution
For a binomial distribution with $n$ trials, each with probability $p$ of success, the pdf is given by:

$$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$$

The expected value and variance of a binomial distribution are:

$E(X) = np$

$Var(X) = np(1-p)$

### Problem Solving Patterns
#### Source Question 1: Exponential Distribution
* Identify the probability density function as exponential with parameter $\lambda = 2$.
* Find the expected lifetime by taking the reciprocal of $\lambda$: $E(X) = \frac{1}{\lambda} = \frac{1}{2}$.
* Round the expected lifetime to 2 decimal places: $0.50$.
* Calculate the probability that the lifetime exceeds the expected value using the exponential distribution's cumulative distribution function (CDF):

$$P(X > E(X)) = P(X > 0.50) = 1 - F(0.50)$$

where $F(x)$ is the CDF of an exponential distribution.

#### Source Question 2: Binomial Distribution
* Identify the probability of success as $p = 0.4$ and the number of trials as $n = 1000$.
* Use the binomial distribution's formula to find the expected value:

$$E(X) = np = 1000 \times 0.4 = 400$$

* Calculate the standard deviation using the formula for variance:

$$Var(X) = np(1-p) = 1000 \times 0.4 \times (1-0.4) = 160$$

### Examples with Solutions
#### Example: Exponential Distribution
Suppose the lifetime of a component is exponentially distributed with parameter $\lambda = 3$. Find the probability that its lifetime exceeds $2$.

```mermaid
graph LR
    A[Expected value] -->|1/λ|> B(1/3)
    C[Lifetime] -->|>2| D(P(X > 2))
```

Solution:

Using the CDF of an exponential distribution:

$$P(X > 2) = 1 - F(2) = 1 - e^{-\lambda x} = 1 - e^{-3 \times 2} = 0.98$$

#### Example: Binomial Distribution
Suppose we toss a biased coin with probability $p = 0.5$ of landing heads up. Find the expected value and standard deviation of the number of heads in $n = 10$ tosses.

```mermaid
graph LR
    A[Expected value] -->|np|> B(5)
    C[Variance] -->|np(1-p)|> D(2.5)
```

Solution:

Expected value: $E(X) = np = 10 \times 0.5 = 5$

Variance: $Var(X) = np(1-p) = 10 \times 0.5 \times (1-0.5) = 2.5$

Standard deviation: $\sigma = \sqrt{Var(X)} = \sqrt{2.5} = 1.58$ (rounded to 2 decimal places)

### Common Pitfalls
* Confusing the expected value with the median or mode.
* Failing to account for the parameter values when applying distribution formulas.

### Quick Summary
* Random variables are functions that assign real numbers to outcomes of an experiment.
* Types: discrete, continuous.
* Probability distributions: exponential, binomial.
* Key formulas and theorems: expected value, variance, CDF.