# Day 07 - What are Tensors?

> **Course:** CampusX - 100 Days of Machine Learning

---

# 🎯 Learning Objectives

After completing this lecture, you will be able to:

- Understand what a Tensor is.
- Differentiate between Scalar, Vector, Matrix, and Tensor.
- Understand Rank and Shape of a Tensor.
- Learn why tensors are important in Machine Learning.
- Create basic tensors using NumPy.

---

# 📚 Prerequisites

Before starting this lecture, you should know:

- Basic Python
- NumPy Arrays
- Dimensions in Mathematics

---

# Introduction

Whenever we work in Machine Learning, we deal with **data**.

This data can be represented in different forms:

- A single number
- A list of numbers
- A table
- Multiple tables

All these representations are called **Tensors**.

A Tensor is simply a mathematical structure used to represent data.

You can think of a Tensor as a **generalization of Scalars, Vectors, and Matrices**.

---

# What is a Tensor?

A **Tensor** is a multi-dimensional array that stores numerical data.

Depending on the number of dimensions, a tensor can represent different types of data.

```
Scalar  → 0D Tensor

Vector  → 1D Tensor

Matrix  → 2D Tensor

Higher Dimension → 3D, 4D, ...
```

So,

Every Scalar is a Tensor.

Every Vector is a Tensor.

Every Matrix is a Tensor.

---

# Why Do We Need Tensors?

Machine Learning algorithms work with numerical data.

Different problems have different data formats.

Examples:

Age

```
25
```

Marks of a Student

```
80 85 90 95
```

Sales Data

| Product | Sales |
|----------|------:|
| Milk | 200 |
| Bread | 180 |
| Eggs | 150 |

All these can be represented using tensors.

Instead of creating different structures for different data types, we use a single concept—**Tensor**.

---

# 0D Tensor (Scalar)

A Scalar is a single numerical value.

Examples

```
5

100

3.14

-25
```

NumPy Example

```python
import numpy as np

scalar = np.array(10)

print(scalar)
print(scalar.ndim)
```

Output

```
10

0
```

A Scalar has **0 dimensions**.

---

# 1D Tensor (Vector)

A Vector is a collection of values arranged in a single direction.

Example

```
[10, 20, 30, 40]
```

NumPy Example

```python
vector = np.array([10, 20, 30, 40])

print(vector.ndim)
```

Output

```
1
```

Applications

- Student Marks
- Daily Sales
- Temperature Readings

---

# 2D Tensor (Matrix)

A Matrix contains rows and columns.

Example

```
[
 [1, 2, 3],
 [4, 5, 6]
]
```

NumPy Example

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix.ndim)
```

Output

```
2
```

Applications

- Excel Sheets
- Customer Data
- Employee Records
- Sales Dataset

---

# 3D Tensor

A 3D Tensor is a collection of matrices.

Example

```
[
 [
  [1,2],
  [3,4]
 ],

 [
  [5,6],
  [7,8]
 ]
]
```

NumPy Example

```python
tensor3d = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

print(tensor3d.ndim)
```

Output

```
3
```

Similarly,

4D, 5D and higher-dimensional tensors are also possible.

---

# Rank of a Tensor

The **Rank** of a tensor means the **number of dimensions (axes)** it has.

Examples

| Tensor | Rank |
|---------|------|
| Scalar | 0 |
| Vector | 1 |
| Matrix | 2 |
| 3D Tensor | 3 |

NumPy

```python
print(scalar.ndim)

print(vector.ndim)

print(matrix.ndim)

print(tensor3d.ndim)
```

---

# Shape of a Tensor

The **Shape** tells us how many elements exist in each dimension.

Examples

Vector

```
[10,20,30]
```

Shape

```
(3,)
```

---

Matrix

```
[
 [1,2,3],
 [4,5,6]
]
```

Shape

```
(2,3)
```

Meaning

- 2 Rows
- 3 Columns

---

3D Tensor

Shape

```
(2,2,2)
```

Meaning

- 2 Matrices
- Each Matrix has 2 Rows
- Each Row has 2 Columns

---

NumPy Example

```python
print(vector.shape)

print(matrix.shape)

print(tensor3d.shape)
```

Output

```
(4,)

(2,3)

(2,2,2)
```

---

# Number of Elements

The total number of elements in a tensor is simply the product of its shape.

Examples

Shape

```
(3,)
```

Elements

```
3
```

---

Shape

```
(2,3)
```

Elements

```
2 × 3 = 6
```

---

Shape

```
(2,2,2)
```

Elements

```
2 × 2 × 2 = 8
```

NumPy

```python
print(matrix.size)

print(tensor3d.size)
```

---

# Summary Table

| Tensor Type | Dimensions | Example |
|-------------|------------|---------|
| Scalar | 0D | `5` |
| Vector | 1D | `[1,2,3]` |
| Matrix | 2D | `[[1,2],[3,4]]` |
| Tensor | 3D+ | `[[[...]]]` |

---

# NumPy Methods Used

| Method | Purpose |
|---------|----------|
| `np.array()` | Create Tensor |
| `.ndim` | Number of Dimensions |
| `.shape` | Shape of Tensor |
| `.size` | Total Elements |

---

# Interview Questions

### What is a Tensor?

A Tensor is a multi-dimensional array used to represent numerical data.

---

### Is every Matrix a Tensor?

Yes.

A Matrix is a 2D Tensor.

---

### Difference between Vector and Matrix?

Vector has one dimension.

Matrix has two dimensions.

---

### What is Rank?

Rank is the number of dimensions (axes) of a tensor.

---

### What is Shape?

Shape tells how many elements exist along each dimension.

---

### How do you find the Rank in NumPy?

```python
array.ndim
```

---

### How do you find the Shape?

```python
array.shape
```

---

### How do you find the total number of elements?

```python
array.size
```

---

# Common Mistakes

❌ Rank means number of elements.

✅ Rank means number of dimensions.

---

❌ Shape tells the total number of elements.

✅ Shape tells the size of each dimension.

---

❌ Matrix and Tensor are different concepts.

✅ Matrix is a special case of a Tensor.

---

# Key Takeaways

- A Tensor is a general representation of numerical data.
- Scalars, Vectors, and Matrices are all Tensors.
- Rank represents the number of dimensions.
- Shape represents the size of each dimension.
- NumPy provides simple methods like `.ndim`, `.shape`, and `.size` to work with tensors.

---

# Visual Representation of Tensors

Understanding tensors visually makes the concept much easier.

## 0D Tensor (Scalar)

A single value.

```

7

```

Shape

```

()

```

Rank

```

0

```

---

## 1D Tensor (Vector)

A collection of values.

```

[10, 20, 30, 40]

```

Shape

```

(4,)

```

Rank

```

1

```

---

## 2D Tensor (Matrix)

Rows and Columns.

```

[
[1, 2, 3],
[4, 5, 6]
]

```

Shape

```

(2,3)

```

Rank

```

2

```

---

## 3D Tensor

Collection of multiple matrices.

```

[
[
[1,2],
[3,4]
],

[
[5,6],
[7,8]
]
]

```

Shape

```

(2,2,2)

```

Rank

```

3

```

---

# Understanding Rank vs Shape

Many beginners confuse these two terms.

## Rank

Rank tells **how many dimensions** a tensor has.

Examples

| Tensor | Rank |
|----------|------|
| Scalar | 0 |
| Vector | 1 |
| Matrix | 2 |
| 3D Tensor | 3 |

---

## Shape

Shape tells **how many values are present in each dimension**.

Example

```

[
[1,2,3],
[4,5,6]
]

```

Shape

```

(2,3)

```

Meaning

- 2 Rows
- 3 Columns

---

### Easy Memory Trick

```

Rank = Number of Dimensions

Shape = Size of each Dimension

```

---

# Real Machine Learning Examples

Machine Learning datasets are usually represented as tensors.

## Example 1: Student Dataset

| Math | Science | English |
|-------|----------|----------|
| 80 | 75 | 90 |
| 65 | 82 | 88 |
| 91 | 79 | 95 |

This dataset is a **2D Tensor**.

Shape

```

(3,3)

```

---

## Example 2: Retail Sales Dataset

| Store | Product | Sales |
|--------|----------|-------|
| A | Milk | 120 |
| A | Bread | 90 |
| B | Milk | 150 |

Again,

this is a **2D Tensor** because it contains rows and columns.

---

## Example 3: Weather Data

```

[32, 31, 29, 35, 34]

```

Daily temperatures stored as a **1D Tensor**.

---

# Why Are Tensors Useful in Machine Learning?

Machine Learning algorithms expect numerical input.

Tensors provide a standard way to represent data, regardless of whether it is:

- A single value
- A list of values
- A table of values
- Higher-dimensional structured data

Using one common representation makes data processing easier.

---

# NumPy Practice Examples

## Creating a Scalar

```python
import numpy as np

scalar = np.array(15)

print(scalar.ndim)
print(scalar.shape)
```

---

## Creating a Vector

```python
vector = np.array([5,10,15,20])

print(vector.ndim)
print(vector.shape)
```

---

## Creating a Matrix

```python
matrix = np.array([
    [1,2],
    [3,4]
])

print(matrix.ndim)
print(matrix.shape)
```

---

## Creating a 3D Tensor

```python
tensor = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

print(tensor.ndim)
print(tensor.shape)
```

---

# Summary

| Tensor Type | Rank | Shape Example |
|--------------|------|---------------|
| Scalar | 0 | () |
| Vector | 1 | (4,) |
| Matrix | 2 | (2,3) |
| 3D Tensor | 3 | (2,2,2) |

---

# Revision Notes

- Tensor is a generalization of Scalars, Vectors, and Matrices.
- Scalar is a 0D Tensor.
- Vector is a 1D Tensor.
- Matrix is a 2D Tensor.
- Higher-order tensors have three or more dimensions.
- Rank tells the number of dimensions.
- Shape tells the size of each dimension.
- NumPy provides `.ndim`, `.shape`, and `.size` to inspect tensors.

---

# Practice Questions

1. What is a Tensor?
2. Is every Matrix a Tensor?
3. What is the difference between Rank and Shape?
4. What is the Rank of a Matrix?
5. What is the Shape of a Vector containing 8 elements?
6. Which NumPy attribute returns the number of dimensions?
7. Which NumPy attribute returns the shape?
8. Which NumPy attribute returns the total number of elements?

---

# Final Takeaways

- Tensor is the fundamental data structure used to represent numerical data in Machine Learning.
- Scalars, Vectors, and Matrices are all special cases of tensors.
- Rank and Shape are the two most important properties of a tensor.
- Understanding tensors makes it easier to work with NumPy arrays and prepares you for more advanced Machine Learning topics.