content: |
---

# 🔘 Boolean (bool)

Boolean is a built-in data type that represents one of two values:

- `True`
- `False`

Internally, `bool` is a subclass of `int`.

Example

```python
print(type(True))
print(type(False))
```

Output

```
<class 'bool'>
<class 'bool'>
```

---

## Boolean is a Subclass of Integer

This surprises many beginners.

```python
print(True == 1)
print(False == 0)
```

Output

```
True
True
```

Even

```python
print(True + True)
```

Output

```
2
```

### Why?

Internally,

```
True  → 1

False → 0
```

---

## Truthy and Falsy Values

Python considers some values as **False** automatically.

Falsy values

```python
False

None

0

0.0

0j

""

[]

()

{}

set()

range(0)
```

Everything else is considered **Truthy**.

Example

```python
if []:
    print("Hello")
else:
    print("Empty")
```

Output

```
Empty
```

---

# 🚫 None

`None` represents the absence of a value.

Example

```python
x = None

print(type(x))
```

Output

```
<class 'NoneType'>
```

---

## None is a Singleton

Python creates **only one** `None` object.

Example

```python
a = None

b = None

print(a is b)
```

Output

```
True
```

This is why

```python
if value is None:
```

is preferred over

```python
if value == None:
```

---

# 🧠 Memory Model

Everything created in Python is stored as an object in memory.

Example

```python
x = 10
```

Internally

```
Variable x

↓

Reference

↓

Integer Object (10)
```

Variables do **not** contain values.

They contain references.

---

# Reference Counting

CPython manages memory using **Reference Counting**.

Every object keeps track of how many references point to it.

Example

```python
x = [1,2,3]

y = x

z = x
```

Internally

```
        x

         \

          List Object

         /

        y

       /

      z
```

Reference Count = **3**

---

When

```python
del y
```

Reference Count becomes

```
2
```

When it reaches

```
0
```

Python frees the memory automatically.

---

# Garbage Collection

Reference counting cannot clean every object.

Example

```python
a = []

b = []

a.append(b)

b.append(a)
```

Now

```
a ↔ b
```

Both objects reference each other.

Reference Count never becomes zero.

Without another mechanism, this would cause a memory leak.

Python solves this using the **Garbage Collector**.

---

## Garbage Collector Module

```python
import gc

print(gc.isenabled())
```

Output

```
True
```

Run manually

```python
gc.collect()
```

Useful during debugging.

---

# Object Lifetime

Example

```python
x = [1,2,3]
```

Object Created

↓

Reference Exists

↓

Object Used

↓

Reference Removed

↓

Garbage Collector Frees Memory

---

# CPython Internal Notes

CPython stores every object using a structure similar to:

```
PyObject

↓

Reference Count

↓

Type Pointer

↓

Object Data
```

This is one reason Python objects consume more memory than primitive types in languages like C or Java.

---

# Why Python Uses More Memory Than C++

Because every value is an object.

Even

```python
x = 10
```

creates an integer object.

Whereas in C

```cpp
int x = 10;
```

is simply stored as a primitive integer.

Python trades memory efficiency for flexibility.

---

# Memory Comparison

Approximate sizes on a 64-bit CPython build:

| Object | Approx. Size |
|---------|--------------:|
| int | 28 bytes |
| float | 24 bytes |
| bool | 28 bytes |
| empty string | 49 bytes |
| empty list | 56 bytes |
| empty tuple | 40 bytes |
| empty dict | 64 bytes |

> **Note:** Sizes vary by Python version and platform.

---

# Internal Summary

```
Python Code

↓

Objects Created

↓

Variables Store References

↓

Reference Count Updated

↓

Reference Count = 0 ?

↓

Yes

↓

Garbage Collector Frees Memory
```

---

# Best Practices

✅ Prefer immutable objects when data should not change.

✅ Use mutable objects only when modification is required.

✅ Use `is None` instead of `== None`.

✅ Use `isinstance()` instead of comparing type names as strings.

✅ Avoid unnecessary object creation inside loops.

---

# Common Mistakes

### Mistake 1

```python
a = []

b = a
```

Many beginners think

```
a

↓

List

b

↓

Another List
```

Actually

```
a

 \

  List

 /

b
```

Both variables point to the same object.

---

### Mistake 2

```python
0.1 + 0.2 == 0.3
```

Output

```
False
```

Because floating-point numbers are approximations.

Use

```python
import math

math.isclose(0.1 + 0.2, 0.3)
```

---

### Mistake 3

```python
a = None

if a == None:
```

Better

```python
if a is None:
```

---

# DSA Tips

Understanding data types helps write faster and safer code.

### Use List When

- Frequent updates
- Dynamic size
- Stack
- Queue (better: `deque`)
- Arrays

---

### Use Tuple When

- Fixed data
- Coordinates
- Dictionary keys
- Better memory efficiency

---

### Use Set When

- Fast membership checking
- Remove duplicates

Average complexity

```
O(1)
```

---

### Use Dictionary When

- Key-Value mapping
- Frequency counting
- Hash tables

Average complexity

```
O(1)
```

---

### Use String When

- Text processing
- Pattern matching

Remember

Strings are immutable.

---

# Interview Questions

### What is the difference between mutable and immutable objects?

---

### Why is Python slower than C++?

---

### What is Reference Counting?

---

### What is Garbage Collection?

---

### Why does Python use more memory?

---

### Is `bool` a subclass of `int`?

---

### Why should we use `is None`?

---

### What are Truthy and Falsy values?

---

### What is `NoneType`?

---

### Why are Python integers unlimited?

---

# Quick Revision

✔ Everything in Python is an object.

✔ Variables store references, not values.

✔ Every object has:

- Identity
- Type
- Value

✔ Mutable objects change in place.

✔ Immutable objects create new objects.

✔ `bool` is a subclass of `int`.

✔ `None` is a singleton.

✔ CPython uses reference counting.

✔ Garbage Collector handles cyclic references.

✔ `is` checks identity.

✔ `==` checks equality.

✔ Use `is None` for checking `None`.

✔ Use `isinstance()` instead of comparing type names.

---

# Practice Questions

## Theory

1. What is a data type?
2. Why is everything in Python an object?
3. Difference between `is` and `==`?
4. What is Reference Counting?
5. What is Garbage Collection?
6. Explain Truthy and Falsy values.
7. Why is `bool` a subclass of `int`?
8. Why is `None` a singleton?
9. Why are Python integers unlimited?
10. Explain mutable vs immutable objects.

---

## Coding

1. Print the type of different Python objects.
2. Check whether two variables reference the same object.
3. Demonstrate Truthy and Falsy values.
4. Use `isinstance()` with different types.
5. Convert between different data types.
6. Show the effect of mutable and immutable objects.
7. Display object IDs using `id()`.
8. Use the `gc` module to inspect garbage collection.
9. Compare `is` vs `==`.
10. Explore object sizes using `sys.getsizeof()`.

---

# 🎉 Congratulations!

You have successfully completed **Python Data Types**.

In the next chapter (**03_Variables.md**) we'll dive deep into:

- Variable Assignment
- Multiple Assignment
- Variable Aliasing
- Object References
- `id()`
- `type()`
- `del`
- Namespace
- Scope
- Interning
- Memory Optimization
- Mutable vs Immutable Variables
- Variable Shadowing
- Local vs Global Variables
- `global`
- `nonlocal`
- Interview Questions
- DSA Tips