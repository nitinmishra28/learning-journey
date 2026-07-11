# 📦 Python Data Types

> Everything in Python is an object. Every value you create belongs to a specific data type. Understanding data types is essential because variables don't store values directly—they reference Python objects.

---

# 📚 Table of Contents

- What are Data Types?
- Why are Data Types Important?
- Python Object Model
- Categories of Data Types
- Numeric Types
- Sequence Types
- Mapping Type
- Set Types
- Binary Types
- None Type
- Mutable vs Immutable
- Type Conversion
- type()
- isinstance()
- Best Practices
- Interview Questions
- Quick Revision

---

# 📖 What are Data Types?

A **data type** defines:

- What kind of value is stored.
- How much memory is required.
- What operations can be performed.
- How Python internally represents the value.

Example

```python
age = 22

name = "Nitin"

marks = 95.5
```

Here,

```
22        → int

"Nitin"  → str

95.5      → float
```

---

# 🤔 Why Do Data Types Matter?

Imagine writing

```python
10 + 20
```

Python performs **integer addition**.

Now,

```python
"10" + "20"
```

Python performs **string concatenation**.

Output

```
1020
```

The operator is the same (`+`), but the result depends on the data type.

---

# 🧠 Everything is an Object

One of Python's biggest differences from languages like C is:

> **Everything is an object.**

Even integers.

Example

```python
x = 10

print(type(x))
```

Output

```
<class 'int'>
```

Even `10` is an object.

---

## Everything Has

- Identity
- Type
- Value

Example

```python
x = 100

print(id(x))

print(type(x))

print(x)
```

Output

```
140235498...

<class 'int'>

100
```

We'll study `id()` in detail later.

---

# 📦 Categories of Data Types

Python provides several built-in data types.

```
Data Types

│

├── Numeric

│      ├── int

│      ├── float

│      ├── complex

│

├── Sequence

│      ├── str

│      ├── list

│      ├── tuple

│

├── Mapping

│      └── dict

│

├── Set

│      ├── set

│      └── frozenset

│

├── Binary

│      ├── bytes

│      └── bytearray

│

└── None
```

---

# 🔢 Numeric Data Types

Python supports three numeric types.

## int

Represents whole numbers.

Example

```python
x = 10

y = -25

z = 100000
```

Python integers have **unlimited precision**.

Unlike C/C++, Python integers don't overflow under normal circumstances.

Example

```python
x = 999999999999999999999999999999999999

print(x)
```

Works perfectly.

---

## float

Represents decimal numbers.

Example

```python
pi = 3.14159

temperature = 27.5
```

Internally,

Python uses IEEE-754 double precision floating point.

This means floating-point numbers are **approximations**, not exact values.

Example

```python
print(0.1 + 0.2)
```

Output

```
0.30000000000000004
```

### Why?

Because decimal numbers like `0.1` cannot always be represented exactly in binary.

---

## complex

Represents complex numbers.

Syntax

```python
a + bj
```

Example

```python
z = 2 + 5j

print(type(z))
```

Output

```
<class 'complex'>
```

Accessing parts

```python
print(z.real)

print(z.imag)
```

Output

```
2.0

5.0
```

---

# 📋 Sequence Types

A sequence stores multiple values in order.

Python provides

- String
- List
- Tuple

We'll study each in detail later.

---

## String

Stores text.

```python
name = "Python"
```

---

## List

Stores mutable data.

```python
numbers = [1,2,3]
```

---

## Tuple

Stores immutable data.

```python
coordinates = (10,20)
```

---

# 🗂 Mapping Type

Python provides one mapping type.

Dictionary.

```python
student = {

    "name":"Nitin",

    "age":22
}
```

Stores data as

```
Key → Value
```

---

# 🎯 Set Types

Python provides

## set

Mutable

```python
numbers = {1,2,3}
```

---

## frozenset

Immutable

```python
fs = frozenset({1,2,3})
```

---

# 💾 Binary Types

Used for binary data.

- bytes
- bytearray

Mostly used in networking, files and low-level programming.

---

# 🚫 None Type

Represents the absence of a value.

Example

```python
x = None

print(type(x))
```

Output

```
<class 'NoneType'>
```

Important:

`None`

is **not**

- 0
- False
- ""
- []

It is a completely different object.

---

# 📌 Mutable vs Immutable

One of the most important Python concepts.

## Mutable Objects

Can be modified after creation.

Examples

- list
- dict
- set
- bytearray

---

## Immutable Objects

Cannot be modified after creation.

Examples

- int
- float
- bool
- tuple
- str
- frozenset
- bytes

---

## Quick Comparison

| Mutable | Immutable |
|----------|------------|
| list | int |
| dict | float |
| set | bool |
| bytearray | str |
| | tuple |
| | frozenset |
| | bytes |

---

# 🔄 Type Conversion

Python allows conversion between compatible data types.

```python
int("25")
```

Output

```
25
```

---

```python
float(10)
```

Output

```
10.0
```

---

```python
str(100)
```

Output

```
"100"
```

---

```python
list("Python")
```

Output

```
['P','y','t','h','o','n']
```

---

# 🔍 type()

Returns the data type.

```python
x = 10

print(type(x))
```

Output

```
<class 'int'>
```

---

# 🔍 isinstance()

Preferred over `type()` for inheritance checks.

```python
print(isinstance(10, int))
```

Output

```
True
```

---

# 💡 Best Practices

- Use the correct data type for the problem.
- Prefer `isinstance()` over `type()` in most real-world code.
- Understand mutable vs immutable objects.
- Don't compare data types using strings.

---

# ⚠ Common Mistakes

❌

```python
type(x) == "int"
```

Correct

```python
isinstance(x, int)
```

---

❌

Thinking

```python
None == 0
```

It is not.

---

# 💼 Interview Questions

- Is everything in Python an object?
- Difference between mutable and immutable?
- Why does `0.1 + 0.2` not equal exactly `0.3`?
- Difference between `type()` and `isinstance()`?
- Why are Python integers unlimited?
- What is `NoneType`?

---

# 📌 Quick Revision

- Everything in Python is an object.
- Every object has a type.
- Python has built-in data types.
- Mutable objects can change.
- Immutable objects cannot.
- Use `type()` to check type.
- Prefer `isinstance()` in production code.
- `None` is its own data type.