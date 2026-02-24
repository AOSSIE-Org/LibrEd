**Angles in 3D Objects**
=========================

### Introduction

In three-dimensional geometry, angles between lines and planes play a crucial role in understanding spatial relationships. This topic deals with calculating and interpreting various types of angles within 3D objects, such as cubes.

### Core Concepts

*   **Diagonal**: A line segment connecting two non-adjacent vertices of a polyhedron.
*   **Edge**: A line segment joining two adjacent vertices of a polyhedron.
*   **Cosine Law**: $c^2 = a^2 + b^2 - 2ab \cos(C)$, where $a$, $b$, and $c$ are sides of a triangle, and $C$ is the angle opposite side $c$. We'll use this law to find $\cos(\theta)$ in our problem.
*   **Cube**: A regular hexahedron with six square faces, twelve edges, and eight vertices. The longest diagonal of a cube connects two opposite corners.

### Key Formulas/Theorems

$$\cos(\theta) = \frac{a^2 + b^2 - c^2}{2ab}$$

where $\theta$ is the angle between sides $a$ and $b$, and $c$ is the side opposite to $\theta$. In our case, we'll apply this formula to find $\cos(\theta)$.

### Problem Solving Patterns

*   **Identify type of triangle**: Determine if it's a right-angled, acute, or obtuse triangle.
*   **Apply Pythagoras' theorem**: If the triangle is right-angled, use $a^2 + b^2 = c^2$ to find missing sides.
*   **Use cosine law**: For non-right-angled triangles, apply the formula $\cos(\theta) = \frac{a^2 + b^2 - c^2}{2ab}$.

### Examples with Solutions

**Example 1**

Suppose we have a cube with edge length $s$. The longest diagonal $d$ connects two opposite corners. To find the angle between this diagonal and an edge, let's use the cosine law:

Let $a = b = s$, $c = d$, and $\theta$ be the angle between the diagonal and an edge.

$$\cos(\theta) = \frac{a^2 + a^2 - c^2}{2aa}$$

Simplifying,

$$\cos(\theta) = \frac{2s^2 - d^2}{2s^2}$$

Using the formula for the diagonal of a cube, $d = s\sqrt{3}$:

$$\cos(\theta) = \frac{2s^2 - 3s^2}{2s^2}$$

$$\cos(\theta) = -\frac{1}{2}$$

This means $\cos^{-1}\left(-\frac{1}{2}\right) = 120^\circ$. However, we're not interested in the angle itself but its cosine. Our answer is thus:

$\boxed{\cos(\theta) = \frac{1}{2}}$

**Example 2**

Consider a cube with edge length $s$. Find $\cos(\theta)$ where $\theta$ is the angle between any diagonal and an edge.

Applying the same logic as before, we get

$$\cos(\theta) = -\frac{1}{2}$$

### Common Pitfalls

*   Failing to identify the correct type of triangle.
*   Applying Pythagoras' theorem when it's not applicable (e.g., non-right-angled triangles).
*   Not simplifying expressions before taking the inverse cosine.

### Quick Summary

| Concept | Description |
| --- | --- |
| Diagonal | A line segment connecting two non-adjacent vertices. |
| Edge | A line segment joining two adjacent vertices. |
| Cosine Law | $c^2 = a^2 + b^2 - 2ab \cos(C)$, where $a$, $b$, and $c$ are sides of a triangle, and $C$ is the angle opposite side $c$. |

Visuals:
For this topic, we'll rely on mathematical derivations rather than visual diagrams.

I hope this helps!