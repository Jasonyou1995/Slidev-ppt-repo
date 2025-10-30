---
theme: default
class: text-center
title: NumPy Universal Functions
info: |
  Understanding NumPy's universal functions (ufuncs) - the foundation
  of efficient array operations in Python data science.
  
transition: slide-left
mdc: true
lineNumbers: false
---

# NumPy Universal Functions

### Efficient Array Operations for Data Science

<v-click>

**Why should you care?**

</v-click>

<v-click>

Universal functions make your data computations **orders of magnitude faster**

</v-click>

<!--
Welcome! Today we'll explore NumPy's universal functions - the secret to making Python data computations lightning fast. This is foundational knowledge for anyone working with large datasets in finance, analytics, or data science.
-->

---

# What You'll Learn Today

<v-clicks>

1. **The Problem**: Why Python loops are slow
2. **The Solution**: Vectorization with universal functions
3. **The Tools**: Key ufuncs for financial data
4. **Best Practices**: When and how to use them

</v-clicks>

<!--
We'll start by understanding why traditional Python loops are inefficient for numerical computations, then see how NumPy's ufuncs solve this problem elegantly. By the end, you'll know the essential functions for any data science work.
-->

---

# The Core Problem

## Python Loops Are Slow

<v-clicks>

When you write a loop to process data...

- Python must check data types repeatedly
- Dynamic typing adds overhead
- Each iteration is interpreted (not compiled)

**Result**: Operations that should be instant take seconds!

</v-clicks>

<!--
Here's the fundamental issue: Python is a dynamically typed, interpreted language. This makes it easy to write code, but slow to execute numerical operations. Every time Python runs through a loop, it has to figure out what type of data it's working with and what operation to perform. This overhead compounds when you're processing millions of values.
-->

---

# Real Example: Computing Reciprocals

## The Slow Way (Traditional Loop)

<v-clicks>

**Traditional approach:**

```python
def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output
```

**Time for 1 million calculations**: Several seconds! 😢

</v-clicks>

<!--
This code looks straightforward - loop through the array, compute the reciprocal for each value. But behind the scenes, Python is doing a LOT of work: checking types, looking up functions, managing memory. For a million operations, this adds up to seconds of wasted time.
-->

---

# The NumPy Solution

## Universal Functions (ufuncs)

<v-clicks>

- **Vectorized operations**: Apply to entire arrays at once
- **Compiled code**: Under the hood, it's fast C/Fortran
- **No type checking overhead**: Types are known in advance

**Same operation**: Milliseconds! ⚡

</v-clicks>

<!--
NumPy solves this by "vectorizing" operations. Instead of looping through elements one by one, NumPy performs the operation on the entire array at once using highly optimized compiled code. This is the core concept we need to understand - vectorization is the key to speed.
-->

---

# Vectorization in Action

## Same Operation, Different Speed

<v-clicks>

**Slow Python loop**: `compute_reciprocals(big_array)`  
→ Several seconds for 1M operations

**Fast NumPy vectorization**: `1.0 / big_array`  
→ Milliseconds for the same 1M operations

**Speed difference**: 100-1000x faster! 🚀

</v-clicks>

<!--
This is not a small improvement - we're talking about 100 to 1000 times faster execution. When you're working with financial data, stock prices, transaction volumes, or risk calculations, this speed difference can be the difference between a usable system and an unusable one.
-->

---

# Universal Functions Explained

## What Are Ufuncs?

<v-clicks>

**Ufunc** = Universal Function

- Operates element-wise on arrays
- Automatically handles any array size
- Works with scalars AND arrays
- Available for all common mathematical operations

</v-clicks>

<!--
Universal functions are NumPy's way of making mathematical operations work seamlessly on arrays. The "universal" part means they automatically handle different input types and sizes. You can operate on a single number, a small array, or a massive multi-dimensional array - the syntax stays the same.
-->

---

# Array Arithmetic: The Basics

## Addition, Subtraction, Multiplication

<v-clicks>

```python
x = np.arange(4)  # [0, 1, 2, 3]
```

```python {all}
x + 5   # Addition: [5, 6, 7, 8]
x - 5   # Subtraction: [-5, -4, -3, -2]
x * 2   # Multiplication: [0, 2, 4, 6]
```

</v-clicks>

<!--
Let's start with the basics. Notice how simple this is - we're using the same operators you learned in math class (+, -, *), but they work on entire arrays. NumPy automatically broadcasts the scalar value 5 to match the array's size.
-->

---

# Array Arithmetic: Division

## Standard and Floor Division

<v-clicks>

```python
x = np.arange(4)  # [0, 1, 2, 3]
```

```python {all}
x / 2      # Division: [0.0, 0.5, 1.0, 1.5]
x // 2     # Floor division: [0, 0, 1, 1]
```

</v-clicks>

<!--
Division works the same way. Notice the difference between / (regular division, returns floats) and // (floor division, returns integers by rounding down). This distinction matters in financial calculations where you need integer results.
-->

---

# More Arithmetic Operations

## Negation, Exponentiation, Modulo

<v-clicks>

```python
x = np.arange(4)
```

```python {all}
-x          # Negation: [0, -1, -2, -3]
x ** 2      # Exponentiation: [0, 1, 4, 9]
x % 2       # Modulo: [0, 1, 0, 1]
```

</v-clicks>

<!--
You can chain these operations just like in regular math. The - operator negates all values. ** is for exponentiation (raising to a power). The % operator gives you the remainder after division - very useful for checking even/odd numbers or implementing circular logic.
-->

---

# Complex Arithmetic Expressions

## Combining Operations

<v-clicks>

```python
x = np.arange(4)
```

```python {all}
-(0.5*x + 1) ** 2
```

</v-clicks>

**Result**: Applies the full formula to every element!

<v-clicks>

Standard order of operations applies (PEMDAS).

</v-clicks>

<!--
Notice how we can combine operations in a natural mathematical way. NumPy follows the standard order of operations you learned in algebra - parentheses, exponents, multiplication/division, addition/subtraction. This makes numerical formulas easy to translate from mathematical notation to code.
-->

---

# The Real Function Names

## Behind the Scenes

<v-clicks>

Every operator is actually a function:

```python {all}
np.add(x, 2)     # Instead of: x + 2
np.subtract(x, 2) # Instead of: x - 2
np.multiply(x, 2) # Instead of: x * 2
np.divide(x, 2)  # Instead of: x / 2
```

**Why know both?** Sometimes you need the function form!

</v-clicks>

<!--
While operators are more readable, the function form is sometimes necessary - for example, when you need to pass custom parameters or when using advanced features like specifying output arrays. Both forms do exactly the same computation.
-->

---

# Quick Reference: Arithmetic Operators

| Operator | Function | Example |
|----------|----------|---------|
| `+` | `np.add` | `1 + 1 = 2` |
| `-` | `np.subtract` | `3 - 2 = 1` |
| `-` (unary) | `np.negative` | `-2` |
| `*` | `np.multiply` | `2 * 3 = 6` |
| `/` | `np.divide` | `3 / 2 = 1.5` |
| `//` | `np.floor_divide` | `3 // 2 = 1` |
| `**` | `np.power` | `2 ** 3 = 8` |
| `%` | `np.mod` | `9 % 4 = 1` |

<!--
Keep this table handy. Most of the time you'll use operators because they're more readable, but the function form gives you more control when needed.
-->

---

# Absolute Value

## Working with Negative Numbers



```python
x = np.array([-2, -1, 0, 1, 2])
```

```python {all}
abs(x)        # Built-in Python function
np.abs(x)     # NumPy function (preferred)
np.absolute(x)# Alias for np.abs
```

<v-click>

**Output**: `[2, 1, 0, 1, 2]`

</v-click>

<!--
Absolute value is commonly used in finance for calculating deviations, risk measures, and analyzing volatility. Use np.abs() when working with NumPy arrays for maximum performance.
-->

---

# Absolute Value with Complex Numbers

## Magnitude Calculation

<v-clicks>

```python
x = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])
```

```python {all}
np.abs(x)  # Returns the magnitude
```

**Output**: `[5.0, 5.0, 2.0, 1.0]`

</v-clicks>

<v-clicks>

For complex numbers, `abs()` gives you the magnitude (distance from origin).

</v-clicks>

<!--
This is important when working with signal processing, Fourier transforms, or any domain where complex numbers appear. The absolute value of a complex number is its magnitude (the distance from zero on the complex plane).
-->

---

# Trigonometric Functions

## Working with Angles

<v-clicks>

First, create angles (in radians):

```python {all}
theta = np.linspace(0, np.pi, 3)
```

**Output**: `[0, π/2, π]` (0°, 90°, 180°)

</v-clicks>

<!--
Trigonometric functions are fundamental in many data science applications - from signal processing to time series analysis. Understanding how to generate angles and compute their trigonometric values is essential.
-->

---

# Computing Trigonometric Values

## Sine, Cosine, Tangent

<v-clicks>

```python {all}
np.sin(theta)   # Sine values
np.cos(theta)   # Cosine values
np.tan(theta)   # Tangent values
```

**Key point**: Input in radians, not degrees!

</v-clicks>

<!--
These functions are commonly used in:
- Time series analysis (seasonal patterns)
- Signal processing (Fourier analysis)
- Financial modeling (cyclical patterns)
- Physics simulations

Always remember that Python uses radians, not degrees. Convert degrees with: `np.radians(degrees)` or multiply by `np.pi/180`.
-->

---

# Inverse Trigonometric Functions

## Going Backwards

<v-clicks>

```python
x = [-1, 0, 1]
```

```python {all}
np.arcsin(x)  # Inverse sine (returns radians)
np.arccos(x)  # Inverse cosine
np.arctan(x)  # Inverse tangent
```

**Use case**: Finding angles from known ratios

</v-clicks>

<!--
Inverse trigonometric functions (also called "arc" functions) do the opposite of regular trig functions. If sine gives you the ratio from an angle, arcsin gives you the angle from a ratio. These are essential when you need to work backwards from calculated values.
-->

---

# Exponential Functions

## Growing Numbers

<v-clicks>

```python
x = [1, 2, 3]
```

```python {all}
np.exp(x)           # e^x (natural exponential)
np.exp2(x)          # 2^x
np.power(3, x)      # 3^x
```

**Financial use**: Compound interest, exponential growth models

</v-clicks>

<!--
Exponential functions are crucial in finance for modeling:
- Compound interest calculations
- Population growth
- Exponential decay
- Time value of money
- Option pricing models

The natural exponential (e^x) is especially important because it has special mathematical properties that make calculus and differential equations cleaner.
-->

---

# Logarithmic Functions

## The Inverse of Exponentials

<v-clicks>

```python
x = [1, 2, 4, 10]
```

```python {all}
np.log(x)      # Natural log (base e)
np.log2(x)     # Base 2 log
np.log10(x)    # Base 10 log
```

**Financial use**: Normalizing skewed data, returns analysis

</v-clicks>

<!--
Logarithms are essential for:
- Converting multiplicative relationships to additive ones
- Normalizing skewed data (log transformation)
- Calculating continuously compounded returns
- Power-law distributions

In finance, log returns are often preferred over simple returns because they're additive across time periods and have better statistical properties.
-->

---

# Specialized Log/Exp Functions

## Precision for Small Numbers

<v-clicks>

```python
x = [0, 0.001, 0.01, 0.1]  # Very small values
```

```python {all}
np.expm1(x)   # exp(x) - 1 (more precise)
np.log1p(x)   # log(1 + x) (more precise)
```

**Why use these?** Better numerical precision near zero!

</v-clicks>

<!--
These specialized functions solve a numerical precision problem. When x is very close to zero, computing exp(x) - 1 directly loses precision due to floating-point arithmetic. expm1 and log1p use special algorithms to maintain accuracy. This matters in financial calculations where small rounding errors can compound.
-->

---

# Advanced Ufunc Features

## Specifying Output Location

<v-clicks>

For memory efficiency on large arrays:

```python {1-3|4-8|all}
x = np.arange(5)
y = np.empty(5)

np.multiply(x, 10, out=y)
print(y)
```

**Result**: Values computed directly into `y`

**Benefit**: No temporary array created!

</v-clicks>

<!--
This advanced feature is about memory management. Normally, when you compute something like `x * 10`, Python creates a temporary array to hold the result. With the `out` parameter, you tell NumPy to write directly into your pre-allocated array. This saves memory and can be faster for large computations.
-->

---

# Advanced: Writing to Array Slices

## Targeted Output Assignment

<v-clicks>

```python {1-2|3-6|all}
y = np.zeros(10)
x = np.arange(5)

np.power(2, x, out=y[::2])
print(y)
```

**Result**: Values written to every other element!

**Use case**: Sparsely populating large arrays

</v-clicks>

<!--
This shows the power of the `out` parameter - you can even write to specific elements using slicing. This is useful when you're building sparse arrays or need to selectively update array values based on computed results.
-->

---

# Aggregation: Reducing Arrays

## The `reduce` Method

<v-clicks>

Sum all elements:

```python {all}
x = np.arange(1, 6)  # [1, 2, 3, 4, 5]
np.add.reduce(x)      # 1 + 2 + 3 + 4 + 5 = 15
```

**What it does**: Applies operation repeatedly until one value remains

</v-clicks>

<!--
Reduction operations collapse an array down to a single value by repeatedly applying an operation. Think of it as: start with the first element, then keep combining it with the next element using the specified operation, until you have one final result.
-->

---

# Aggregation: Product

## Multiplying All Elements

<v-clicks>

```python
x = np.arange(1, 6)
```

```python {all}
np.multiply.reduce(x)  # 1 * 2 * 3 * 4 * 5 = 120
```

**Use case**: Computing factorials, compound multipliers

</v-clicks>

<!--
This computes the product of all elements. In finance, you might use this to calculate cumulative returns or compound multipliers over time periods.
-->

---

# Aggregation: Accumulation

## Keeping Intermediate Values

<v-clicks>

**Cumulative sum:**

```python {all}
np.add.accumulate(x)  # [1, 3, 6, 10, 15]
```

**Each value**: Running total up to that point

</v-clicks>

<!--
Unlike reduce, accumulate keeps all intermediate values. This creates a cumulative running total. In finance, this is how you compute cumulative returns over time.
-->

---

# Accumulation: Cumulative Product

<v-clicks>

```python {all}
np.multiply.accumulate(x)  # [1, 2, 6, 24, 120]
```

**Pattern**: Each value is the product of all previous elements

**Use case**: Cumulative returns, compounding

</v-clicks>

<!--
For cumulative product, each element is the running product. This is exactly how compound returns work - each period's return multiplies with all previous returns.
-->

---

# Outer Products

## Computing All Pairs

<v-clicks>

**Creating a multiplication table:**

```python
x = np.arange(1, 6)  # [1, 2, 3, 4, 5]
```

```python {all}
np.multiply.outer(x, x)
```

**Output**: 5x5 table where each cell is `row * column`

</v-clicks>

<!--
The outer operation computes the result of applying an operation to every possible pair of inputs. One input from the first array, one input from the second array, for all combinations. This is useful for distance matrices, correlation matrices, or any pairwise computation.
-->

---

# Why This Matters for Financial Data

## Practical Applications

<v-clicks>

1. **Return calculations**: Vectorized across entire portfolios
2. **Risk metrics**: Fast covariance and correlation computations
3. **Price aggregations**: Operations on thousands of assets
4. **Time series**: Efficient rolling window calculations

**Bottom line**: 100-1000x faster than Python loops!

</v-clicks>

<!--
When you're working with financial data - stock prices, portfolio values, returns - you're often operating on millions of data points. The difference between seconds and milliseconds of computation time is the difference between a usable system and an unusable one. Vectorized operations aren't optional for real financial analysis - they're essential.
-->

---

# Key Takeaways

<v-clicks>

1. **Always use vectorized operations** on NumPy arrays
2. **Avoid Python loops** for numerical computations
3. **Prefer operators** (`+`, `*`, `-`, `/`) for readability
4. **Know the function form** for advanced features
5. **Ufuncs work** with any array size and dimension

</v-clicks>

<!--
Remember: if you find yourself writing a loop to process array elements, there's almost certainly a vectorized operation that can do it faster. Before you optimize, before you refactor, before you accept that your code is "just slow" - check if there's a NumPy ufunc that does what you need.
-->

---

# Remember This Pattern

<v-clicks>

**❌ Slow:**
```python
for i in range(len(data)):
    result[i] = operation(data[i])
```

**✅ Fast:**
```python
result = operation(data)
```

**Same computation, orders of magnitude faster!**

</v-clicks>

<!--
This is the key insight you should take away. Every time you think "I need to loop through this array," ask yourself first: "Is there a NumPy operation that does this directly?" The answer is often yes, and using it will make your code both faster and more readable.
-->

---

# What's Next?

<v-clicks>

- **Aggregations**: Min, max, mean, and more
- **Broadcasting**: Operating on arrays of different sizes
- **Boolean indexing**: Advanced data selection
- **Structured arrays**: Complex data types

**All built on the foundation of ufuncs!**

</v-clicks>

<!--
Universal functions are just the beginning. They work in concert with other NumPy features like broadcasting, fancy indexing, and aggregations. But understanding ufuncs gives you the foundation to work efficiently with any numerical data.
-->

---

# Summary: NumPy UFuncs

**Universal functions are NumPy's superpower:**

<v-clicks>

- ⚡ **Fast**: Compiled C/Fortran code
- 🔄 **Vectorized**: Work on entire arrays
- 📈 **Scalable**: Millions of operations in milliseconds
- 🎯 **Flexible**: Same syntax for any array size
- 💼 **Essential**: Foundation of all data science

**Master this, and you can handle any numerical computation efficiently!**

</v-clicks>

<!--
You now understand one of the most important concepts in numerical computing with Python. Universal functions are not just a convenience - they're what make NumPy-based data science possible. Every library in the Python data science ecosystem - pandas, scikit-learn, TensorFlow - relies on these efficient operations.

Thank you for your attention, and remember: when in doubt, vectorize!
-->

---

# Questions?

### Thank you for your attention!

**Resources:**
- NumPy documentation: https://numpy.org/doc/
- SciPy documentation: https://docs.scipy.org/
- Stack Overflow: numpy universal-functions

<!--
Feel free to ask any questions! Understanding universal functions is the foundation for efficient numerical computing in Python. Practice with different operations, experiment with timing (using %timeit), and remember that vectorization is almost always the answer.
-->
