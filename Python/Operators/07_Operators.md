# ➕ Python Operators

> Operators are special symbols used to perform operations on values and variables. Understanding operators is essential for writing conditions, loops, algorithms, and solving DSA problems.

---

# 📚 Table of Contents

- What are Operators?
- Types of Operators
- Arithmetic Operators
- Unary Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Membership Operators
- Identity Operators
- Bitwise Operators (Overview)
- Operator Precedence
- Best Practices
- Interview Questions
- Quick Revision

---

# 📖 What are Operators?

Operators are symbols that tell Python to perform a specific operation.

Example

```python
a = 10
b = 20

print(a + b)
```

Output

```
30
```

Here

- `+` → Operator
- `10`, `20` → Operands

---

# Categories of Operators

Python provides the following operators:

- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Membership Operators
- Identity Operators
- Bitwise Operators

---

# ➕ Arithmetic Operators

Arithmetic operators perform mathematical operations.

| Operator | Meaning | Example |
|----------|---------|---------|
| + | Addition | a + b |
| - | Subtraction | a - b |
| * | Multiplication | a * b |
| / | Division | a / b |
| // | Floor Division | a // b |
| % | Modulus | a % b |
| ** | Exponent | a ** b |

---

## Addition (+)

Adds two values.

```python
a = 10
b = 5

print(a + b)
```

Output

```
15
```

### Works With

- int
- float
- complex
- strings (concatenation)
- lists (concatenation)
- tuples (concatenation)

Example

```python
print("Hello " + "Python")
```

Output

```
Hello Python
```

### Time Complexity

Numbers

```
O(1)
```

Strings

```
O(n)
```

because a new string is created.

---

## Subtraction (-)

```python
print(20 - 5)
```

Output

```
15
```

Works only with numeric types.

---

## Multiplication (*)

```python
print(5 * 6)
```

Output

```
30
```

### String Repetition

```python
print("Hi " * 3)
```

Output

```
Hi Hi Hi
```

### List Repetition

```python
print([1,2] * 3)
```

Output

```
[1,2,1,2,1,2]
```

⚠️ **Interview Pitfall**

```python
matrix = [[0] * 3] * 3
```

Looks correct, but it's **not**.

All rows reference the same inner list.

```python
matrix[0][0] = 1

print(matrix)
```

Output

```
[[1,0,0],
 [1,0,0],
 [1,0,0]]
```

✅ Correct way

```python
matrix = [[0] * 3 for _ in range(3)]
```

---

## Division (/)

Always returns a float.

```python
print(10 / 2)
```

Output

```
5.0
```

Even if the result is a whole number, Python returns a `float`.

---

## Floor Division (//)

Returns the quotient after rounding **down**.

```python
print(10 // 3)
```

Output

```
3
```

### Negative Numbers

```python
print(-10 // 3)
```

Output

```
-4
```

⚠️ **Important**

Python floors toward **negative infinity**, not toward zero.

This is a common interview question.

---

## Modulus (%)

Returns the remainder.

```python
print(10 % 3)
```

Output

```
1
```

### Negative Numbers

```python
print(-10 % 3)
```

Output

```
2
```

Python guarantees:

```text
(a // b) * b + (a % b) == a
```

---

## Exponent (**)

Raises a number to a power.

```python
print(2 ** 5)
```

Output

```
32
```

---

# Unary Operators

Unary operators work with a single operand.

Positive

```python
x = 10

print(+x)
```

Output

```
10
```

Negative

```python
print(-x)
```

Output

```
-10
```

Logical NOT

```python
print(not True)
```

Output

```
False
```

---

# Assignment Operators

Assignment operators assign values to variables.

| Operator | Example | Equivalent |
|----------|---------|------------|
| = | x = 5 | Assign |
| += | x += 2 | x = x + 2 |
| -= | x -= 2 | x = x - 2 |
| *= | x *= 2 | x = x * 2 |
| /= | x /= 2 | x = x / 2 |
| //= | x //= 2 | x = x // 2 |
| %= | x %= 2 | x = x % 2 |
| **= | x **= 2 | x = x ** 2 |

---

### In-place or Not?

For immutable objects like integers and strings, augmented assignment creates a new object.

```python
x = 10

old_id = id(x)

x += 1

print(old_id == id(x))
```

Output

```
False
```

For mutable objects (like lists), `+=` modifies the existing list in place.

```python
a = [1, 2]
b = a

a += [3]

print(a)
print(b)
```

Output

```
[1, 2, 3]
[1, 2, 3]
```

⚠️ This difference is important in interviews.

---

# 💡 Best Practices

- Use `//` when integer division is required.
- Use `**` instead of repeated multiplication.
- Avoid using `+=` with immutable objects inside performance-critical loops involving string concatenation; prefer `"".join()` when building large strings.
- Be careful with list multiplication for nested lists.

---

# ⚠️ Common Mistakes

❌ Assuming `/` returns an integer.

```python
print(10 / 2)
```

Returns

```
5.0
```

---

❌ Creating matrices using

```python
[[0] * n] * m
```

This creates shared references.

---

❌ Forgetting that `//` rounds toward negative infinity.

```python
-7 // 3
```

Returns

```
-3
```

not `-2`.

---

# 🧠 DSA Tips

- `%` is heavily used for cyclic indexing and hashing.
- `//` is commonly used in binary search (`mid = (low + high) // 2`).
- `**` is useful for mathematical problems, but prefer `pow()` when using modular exponentiation (`pow(a, b, mod)`).
- Understanding operator behavior helps avoid bugs in algorithms.

---

# 📌 Quick Revision

- `/` always returns a float.
- `//` performs floor division.
- `%` returns the remainder.
- `**` performs exponentiation.
- `+=` behaves differently for mutable and immutable objects.
- Avoid `[[0] * n] * m` when creating matrices.