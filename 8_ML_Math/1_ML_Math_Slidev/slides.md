---
theme: default
class: text-center
title: Linear Algebra for Machine Learning
info: |
  Basic linear algebra concepts for understanding machine learning mathematics.
  Designed for non-technical students with clear examples and code demonstrations.
  
transition: slide-left
mdc: true
lineNumbers: true
---


# Linear Algebra for Machine Learning

### Building Blocks of ML Mathematics

<div class="text-sm opacity-75 mt-8">

Don't worry - we'll start simple! 🎯

</div>

<!--
Welcome! Today we'll explore the fundamental mathematics that powers machine learning. 
We'll break everything down into bite-sized pieces, one concept at a time.
-->

---

# What You'll Learn Today

<v-clicks>

1. **What Linear Algebra Is** - In simple terms
2. **Scalars** - Just numbers
3. **Vectors** - Lists of numbers
4. **Matrices** - Tables of numbers
5. **Tensors** - Multi-dimensional arrays
6. **Norms** - Measuring length
7. **Basis & Orthogonal** - Coordinate systems
8. **Practice** - Hands-on exercises

</v-clicks>

<!--
We'll cover these concepts step by step, with visual examples and code you can run yourself.
Each concept builds on the previous one, so follow along carefully!
-->

---

# What is Linear Algebra?

## Think of it as "Math with Multiple Numbers"

<div class="text-left mt-8" style="max-width: 800px; margin: 0 auto;">

<v-clicks>

**Instead of**: Working with one number at a time  
**We work with**: Collections of numbers organized together

**Simple idea**: Like organizing data in a spreadsheet, but with math!

</v-clicks>

</div>

<!--
VISUALIZATION NOTE: 
- Draw a simple analogy: Regular math = single numbers, Linear algebra = organized groups
- Show a single number "5" vs a list "[1, 2, 3]"
- Explain: Linear algebra helps us work with many numbers at once efficiently
-->

---

# Real-World Example: Temperature Conversion

$$F = \frac{9}{5}C + 32$$

<div class="text-left mt-6" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**What this means**:  
- If Celsius = 0° → Fahrenheit = 32°  
- If Celsius = 100° → Fahrenheit = 212°

**Why it's "linear"**:  
When you plot this, it makes a **straight line**!

</v-clicks>

</div>

<!--
VISUALIZATION NOTE: 
- Draw axes: X = Celsius, Y = Fahrenheit
- Plot two points: (0, 32) and (100, 212)
- Draw a straight line connecting them
- Emphasize: "Linear" = straight line relationship
- Show that this is a simple, predictable relationship
-->

---

# Scalars

## Just a Single Number

<div class="text-4xl mt-8 mb-8">

**5**

</div>

<div class="text-left mt-6" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**That's it!** A scalar is just one number.

**Examples**:
- Your age: **25**
- Temperature: **72°**
- Price: **$10**

</v-clicks>

</div>

```python
scalar = 5
print(scalar)  # Output: 5
```

<!--
VISUALIZATION NOTE:
- Draw a single box with "5" inside
- Show different examples: age, temperature, price
- Emphasize: Simplest building block - just one value
- This is what students already know - a single number!
-->

---

# Vectors

## A List of Numbers

<div class="mt-6">

$$
\mathbf{v} = \begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix}
$$

</div>

<div class="text-left mt-6" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Think of it as**: A list of numbers in a column

**Real example**:  
Your height, weight, age = **[175, 70, 25]**

**In ML**: One data point (like one person's features)

</v-clicks>

</div>

<!--
VISUALIZATION NOTE:
- Draw a vertical column with numbers stacked: 2, 3, 4
- Show an arrow pointing from origin to point (2,3) on a 2D plane
- Explain: Vector = direction + magnitude (like an arrow)
- Give concrete example: student's grades [85, 90, 78]
- Emphasize: Just organized numbers in a list
-->

---

# Vector Transpose

## Flipping Row ↔ Column

<div class="mt-6">

**Column vector**:  
$$
\mathbf{v} = \begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix}
$$

**Row vector** (transpose):  
$$
\mathbf{v}^T = \begin{bmatrix} 2 & 3 & 4 \end{bmatrix}
$$

</div>

<div class="text-left mt-6" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Simple idea**: Just rotate it 90 degrees!

**Same numbers**, different orientation.

</v-clicks>

</div>

<!--
VISUALIZATION NOTE:
- Draw a column vector vertically
- Rotate it 90 degrees to show row vector horizontally
- Emphasize: Same information, just different layout
- Show in code: .T property flips it
-->

---

# Vector Transpose: Code Example

```python {1|3-6|8-11|13-16|all}
import numpy as np

# Column vector (vertical)
v_column = np.array([[2], [3], [4]])
print("Column vector:")
print(v_column)

# Row vector (horizontal)
v_row = np.array([2, 3, 4])
print("\nRow vector:")
print(v_row)

# Transpose: flip column to row
v_transposed = v_row.T
print("\nTransposed:")
print(v_transposed)
```

<div class="text-sm mt-4 opacity-75">

**Key point**: `.T` flips the orientation

</div>

<!--
CONCEPT NOTE:
- Show how NumPy handles this
- Demonstrate the transpose operation
- Let students see the output
- Emphasize: Simple operation, just changes layout
-->

---

# Norms: Measuring Vector Length

## How "Long" is a Vector?

<div class="mt-6">

$$
\mathbf{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}
$$

</div>

<div class="text-left mt-6" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Question**: How long is this arrow?

**Answer**: Use the **norm** (like measuring distance)

**L2 Norm** = $\sqrt{3^2 + 4^2} = \sqrt{9 + 16} = 5$

</v-clicks>

</div>

<!--
VISUALIZATION NOTE:
- Draw coordinate axes
- Draw vector from (0,0) to (3,4)
- Show the right triangle: base=3, height=4
- Draw the hypotenuse = 5 (the norm)
- Explain: Like Pythagorean theorem!
- Show: norm = straight-line distance from origin
-->

---

# Norms: Code Example

```python
import numpy as np

v = np.array([3, 4])

# L2 Norm (most common - straight line distance)
norm = np.linalg.norm(v)
print(f"Vector: {v}")
print(f"Length (norm): {norm}")  # Output: 5.0

# How it works:
# sqrt(3² + 4²) = sqrt(9 + 16) = sqrt(25) = 5
```

<div class="text-sm mt-4 opacity-75">

**Think of it**: Like measuring distance from origin to point

</div>

<!--
CONCEPT NOTE:
- Show the calculation
- Emphasize: Norm = length = distance
- Keep it simple - just L2 norm for now
- Later can introduce L1 as alternative
-->

---

# Unit Vectors

## Vectors with Length = 1

<div class="mt-6">

**Original vector**: $\mathbf{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$ (length = 5)

**Unit vector**: $\hat{\mathbf{v}} = \begin{bmatrix} 0.6 \\ 0.8 \end{bmatrix}$ (length = 1)

</div>

<div class="text-left mt-6" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**How to make it**: Divide by its length!

**Why useful**: Removes size, keeps only **direction**

</v-clicks>

</div>

<!--
VISUALIZATION NOTE:
- Draw original vector (3,4) - longer arrow
- Draw unit vector (0.6, 0.8) - shorter arrow, same direction
- Show they point the same way
- Explain: Unit vector = direction only, no magnitude
- Use analogy: Like a compass direction (north, south) vs distance
-->

---

# Unit Vectors: Code Example

```python
import numpy as np

v = np.array([3, 4])

# Get length
length = np.linalg.norm(v)  # = 5

# Create unit vector: divide by length
unit_v = v / length
print(f"Original: {v}")
print(f"Unit vector: {unit_v}")
print(f"Length of unit vector: {np.linalg.norm(unit_v)}")  # = 1.0
```

<div class="text-sm mt-4 opacity-75">

**Formula**: $\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|}$

</div>

<!--
CONCEPT NOTE:
- Show normalization process
- Emphasize: Same direction, length = 1
- Explain why this is useful: comparing directions
- Keep it simple - just the concept
-->

---

# Systems of Linear Equations

## Multiple Equations at Once

$$
\begin{cases}
2x + 3y = 7 \\
x - y = 1
\end{cases}
$$

<div class="text-left mt-6" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Question**: What values of $x$ and $y$ work for **both** equations?

**Answer**: Where the two **lines intersect**!

**Solution**: $x = 2$, $y = 1$

</v-clicks>

</div>

<!--
VISUALIZATION NOTE:
- Draw coordinate plane
- Draw first line: 2x + 3y = 7
- Draw second line: x - y = 1  
- Show intersection point (2, 1)
- Explain: This point satisfies both equations
- Use different colors for each line
-->

---

# Plotting Systems of Equations

```python
import numpy as np
import matplotlib.pyplot as plt

# Define x values
x = np.linspace(-1, 4, 100)

# Solve each equation for y
y1 = (7 - 2*x) / 3  # From: 2x + 3y = 7
y2 = x - 1          # From: x - y = 1

# Plot both lines
plt.plot(x, y1, label='2x + 3y = 7', linewidth=2)
plt.plot(x, y2, label='x - y = 1', linewidth=2)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, alpha=0.3)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('System of Linear Equations')
plt.xlim(-1, 4)
plt.ylim(-1, 3)
plt.show()

# Solution: x=2, y=1 (intersection point)
```

<!--
VISUALIZATION NOTE:
- Run this code to show the plot
- Point to intersection
- Explain: Visual way to solve systems
- Show that (2,1) is on both lines
-->

---

# Orthogonal Vectors

## Perpendicular (90° Angle)

<div class="mt-6">

$$
\mathbf{u} = \begin{bmatrix} 1 \\ 0 \end{bmatrix} \quad
\mathbf{v} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

</div>

<div class="text-left mt-6" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**These vectors are perpendicular** (at right angle)

**How to check**: Dot product = 0

**In ML**: Independent directions (don't overlap)

</v-clicks>

</div>

<!--
VISUALIZATION NOTE:
- Draw x and y axes
- Draw vector [1,0] along x-axis (horizontal arrow)
- Draw vector [0,1] along y-axis (vertical arrow)
- Show they form a 90° angle
- Explain: Like north and east - completely independent directions
- Show that they don't "mix" - pointing in different directions
-->

---

# Orthogonal Vectors: Code Example

```python
import numpy as np

# Two perpendicular vectors
u = np.array([1, 0])  # Horizontal
v = np.array([0, 1])  # Vertical

# Check if orthogonal: dot product should be 0
dot_product = np.dot(u, v)
print(f"Dot product: {dot_product}")  # Output: 0

if dot_product == 0:
    print("They are orthogonal! ✅")
```

<div class="text-sm mt-4 opacity-75">

**Rule**: If dot product = 0, vectors are perpendicular

</div>

<!--
CONCEPT NOTE:
- Show how to check orthogonality
- Emphasize: Dot product = 0 means perpendicular
- Keep it simple - just the check
- Later can explain what dot product means
-->

---

# Basis Vectors

## Building Blocks of Coordinate System

<div class="mt-6">

**Standard basis**:
$$
\mathbf{e}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad
\mathbf{e}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

</div>

<div class="text-left mt-6" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Think of it**: The "rulers" that measure space

**Any point** can be written as:  
$\text{point} = x \cdot \mathbf{e}_1 + y \cdot \mathbf{e}_2$

**Example**: Point $(3, 4) = 3 \cdot \mathbf{e}_1 + 4 \cdot \mathbf{e}_2$

</v-clicks>

</div>

<!--
VISUALIZATION NOTE:
- Draw coordinate axes
- Draw e1 = [1,0] along x-axis
- Draw e2 = [0,1] along y-axis
- Show point (3,4)
- Show how to get there: 3 steps in e1 direction + 4 steps in e2 direction
- Explain: Basis vectors are like "directions" we use to describe any point
- Use analogy: Like saying "3 blocks east, 4 blocks north"
-->

---

# Basis Vectors: Code Example

```python
import numpy as np

# Standard basis vectors
e1 = np.array([1, 0])  # East
e2 = np.array([0, 1])  # North

# Express point (3, 4) using basis
point = np.array([3, 4])

# Reconstruct using basis vectors
reconstructed = 3*e1 + 4*e2
print(f"Point: {point}")
print(f"Using basis: {reconstructed}")  # Same!

# Check: They're orthogonal and unit length
print(f"\ne1 · e2 = {np.dot(e1, e2)}")  # 0 (orthogonal)
print(f"||e1|| = {np.linalg.norm(e1)}")  # 1 (unit)
print(f"||e2|| = {np.linalg.norm(e2)}")  # 1 (unit)
```

<!--
CONCEPT NOTE:
- Show how basis vectors work
- Demonstrate reconstruction
- Show orthonormal properties
- Keep it concrete with examples
-->

---

# Matrices

## Tables of Numbers

<div class="mt-6">

$$
\mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
$$

</div>

<div class="text-left mt-6" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Think of it**: Like a spreadsheet table

**2 rows × 2 columns** = 2×2 matrix

**In ML**: Used to transform data

</v-clicks>

</div>

<!--
VISUALIZATION NOTE:
- Draw a 2×2 grid/table
- Fill in numbers: 
  Row 1: [1, 2]
  Row 2: [3, 4]
- Explain: Rows and columns
- Show it's like a table/spreadsheet
- Emphasize: Organized rectangular arrangement
-->

---

# Matrices: Code Example

```python
import numpy as np

# Create a 2×2 matrix
A = np.array([[1, 2],
              [3, 4]])

print("Matrix A:")
print(A)
print(f"\nShape: {A.shape}")  # (2, 2) = 2 rows, 2 columns

# Access elements
print(f"\nElement at row 0, col 0: {A[0, 0]}")  # 1
print(f"Element at row 1, col 1: {A[1, 1]}")  # 4
```

<div class="text-sm mt-4 opacity-75">

**Remember**: Matrix = rows × columns

</div>

<!--
CONCEPT NOTE:
- Show basic matrix creation
- Show shape (dimensions)
- Show element access
- Keep it simple - just introduction
-->

---

# Tensors

## Multi-Dimensional Arrays

<div class="text-left mt-6" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Scalar** = 0D tensor (just a number)  
**Vector** = 1D tensor (a list)  
**Matrix** = 2D tensor (a table)  
**Tensor** = 3D+ (like a stack of matrices)

**In ML**: Everything is a tensor!

</v-clicks>

</div>

<div class="mt-6 text-sm opacity-75">

**Simple idea**: Just add more dimensions!

</div>

<!--
VISUALIZATION NOTE:
- Draw progression:
  1. Single box "5" for scalar
  2. Row of boxes [1,2,3] for vector
  3. 2×2 grid for matrix
  4. Two 2×2 grids stacked for 3D tensor
- Explain: Each level adds a dimension
- Use analogy: Scalar = point, Vector = line, Matrix = plane, Tensor = space
- Keep it visual and simple
-->

---

# Tensors: Code Example

```python
import numpy as np

# Scalar (0D tensor)
scalar = np.array(5)
print(f"Scalar shape: {scalar.shape}")  # ()

# Vector (1D tensor)
vector = np.array([1, 2, 3])
print(f"Vector shape: {vector.shape}")  # (3,)

# Matrix (2D tensor)
matrix = np.array([[1, 2], [3, 4]])
print(f"Matrix shape: {matrix.shape}")  # (2, 2)

# 3D Tensor (like stacking matrices)
tensor_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(f"3D Tensor shape: {tensor_3d.shape}")  # (2, 2, 2)
```

<!--
CONCEPT NOTE:
- Show the progression
- Demonstrate shapes
- Emphasize: Just adding dimensions
- Keep examples simple
-->

---

# Tensor Notation

## How ML Papers Write Math

<div class="text-left mt-6" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Scalars**: lowercase italic → $a$, $x$  
**Vectors**: lowercase bold → $\mathbf{v}$, $\mathbf{x}$  
**Matrices**: uppercase bold → $\mathbf{A}$, $\mathbf{W}$  
**Tensors**: calligraphic → $\mathcal{T}$

**Why**: Makes formulas easier to read!

</v-clicks>

</div>

<!--
VISUALIZATION NOTE:
- Write out notation conventions on board
- Show examples:
  - Scalar: a = 5
  - Vector: v = [1, 2, 3]
  - Matrix: A = [[1,2],[3,4]]
- Explain: Different fonts = different types
- Emphasize: This is just a convention to make things clear
-->

---

# Tensor Notation: Examples

$$
\begin{align}
\mathbf{v} &= \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} \\
\mathbf{A} &= \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}
\end{align}
$$

<div class="text-left mt-6" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Subscripts** show position:
- $v_1$ = first element of vector
- $a_{12}$ = row 1, column 2 of matrix

**In code**: `v[0]`, `A[0, 1]`

</v-clicks>

</div>

<!--
VISUALIZATION NOTE:
- Show how notation maps to code
- Draw matrix and label elements with subscripts
- Show: Notation = math way, Code = programming way
- Emphasize: Both mean the same thing!
-->

---

# Practice: Exercise 1

## Vector Operations

<div class="text-left mt-6" style="max-width: 700px; margin: 0 auto;">

**Task**:  
Create vector $\mathbf{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$

1. Calculate its length (norm)
2. Create its unit vector

</div>

<v-click>

```python
import numpy as np

# Your code here
v = np.array([3, 4])

# Step 1: Calculate norm
norm = np.linalg.norm(v)
print(f"Length: {norm}")

# Step 2: Create unit vector
unit_v = v / norm
print(f"Unit vector: {unit_v}")
```

</v-click>

<!--
PRACTICE NOTE:
- Let students try first
- Then show solution
- Encourage experimentation
- Check understanding
-->

---

# Practice: Exercise 2

## Matrix-Vector Multiplication

<div class="text-left mt-6" style="max-width: 700px; margin: 0 auto;">

**Task**:  
$$
\mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad
\mathbf{x} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}
$$

Calculate $\mathbf{A} \mathbf{x}$

</div>

<v-click>

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
x = np.array([1, 2])

# Matrix multiplication
result = A @ x
print(f"Result: {result}")  # [5, 11]

# How it works:
# First row: 1*1 + 2*2 = 5
# Second row: 3*1 + 4*2 = 11
```

</v-click>

<!--
VISUALIZATION NOTE:
- Draw matrix and vector
- Show step-by-step calculation:
  - Take first row [1,2]
  - Multiply with x: 1*1 + 2*2 = 5
  - Take second row [3,4]
  - Multiply with x: 3*1 + 4*2 = 11
- Show arrows connecting elements
-->

---

# Practice: Exercise 3

## Check Orthogonality

<div class="text-left mt-6" style="max-width: 700px; margin: 0 auto;">

**Task**:  
Check if these vectors are orthogonal:

$$
\mathbf{u} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \quad
\mathbf{v} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}
$$

</div>

<v-click>

```python
import numpy as np

u = np.array([1, 1])
v = np.array([1, -1])

# Check dot product
dot_product = np.dot(u, v)
print(f"Dot product: {dot_product}")

if dot_product == 0:
    print("✅ They are orthogonal!")
else:
    print("❌ They are NOT orthogonal")
```

</v-click>

<!--
VISUALIZATION NOTE:
- Draw both vectors on coordinate plane
- Show they're perpendicular (45° and -45°)
- Show dot product calculation: 1*1 + 1*(-1) = 0
- Emphasize: Dot product = 0 means perpendicular
-->

---

# Key Takeaways

<div class="text-left mt-6" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

✅ **Scalars** = single numbers

✅ **Vectors** = lists of numbers

✅ **Matrices** = tables (rows × columns)

✅ **Tensors** = multi-dimensional arrays

✅ **Norm** = vector length

✅ **Unit vector** = length 1

✅ **Orthogonal** = perpendicular

✅ **Basis** = coordinate system building blocks

</v-clicks>

</div>

<div class="mt-6 text-sm opacity-75">

**Remember**: These are the building blocks of ML! 🎯

</div>

<!--
CONCEPT SUMMARY:
- Linear algebra provides the language for ML
- Start simple: scalars → vectors → matrices → tensors
- Visualize when possible
- Practice with code
- These concepts appear everywhere in ML!
-->

---

# What's Next?

<v-clicks>

🔹 **Matrix Operations**: Addition, multiplication

🔹 **Eigenvalues**: Important directions in data

🔹 **Applications**: How ML uses these concepts

</v-clicks>

<div class="mt-8">

**You now have the foundation!** 🎉

</div>

<!--
FUTURE LEARNING:
- Matrix operations are next logical step
- Eigenvalues reveal important patterns
- Each concept builds on what we learned
- Practice makes perfect!
-->

---

# Questions?

### Thank you for learning!

<div class="text-sm mt-8 opacity-75">

**Practice Resources**:
- NumPy docs: https://numpy.org/doc/
- 3Blue1Brown: Essence of Linear Algebra
- Interactive: https://www.math3d.org/

</div>

<!--
ENCOURAGEMENT:
- Math becomes easier with practice
- Start simple, build gradually
- Visualize concepts
- Code helps understanding
- You're building essential ML skills!
-->
