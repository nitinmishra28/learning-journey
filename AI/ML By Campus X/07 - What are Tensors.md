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