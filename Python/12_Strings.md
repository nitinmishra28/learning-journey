# 🔤 Python Strings

> Strings are one of the most frequently used data types in Python. They are immutable sequences of Unicode characters and play a major role in DSA, Competitive Programming, Backend Development, and Interviews.

---

# 📚 Table of Contents

- What is a String?
- Creating Strings
- Internal Working
- Why Strings are Immutable
- Unicode
- String Indexing
- Negative Indexing
- String Slicing
- String Concatenation
- String Repetition
- Escape Sequences
- Raw Strings
- Triple Quotes
- Memory Behavior
- Time Complexity
- Common Mistakes
- Interview Questions
- Quick Revision

---

# 📖 What is a String?

A string is an **ordered sequence of Unicode characters**.

Examples

```python
name = "Nitin"

language = 'Python'

message = """Hello"""
```

Every string is an object of type

```python
str
```

Example

```python
print(type("Python"))
```

Output

```
<class 'str'>
```

---

# Strings are Immutable ⭐

One of the most important interview concepts.

Once a string is created,

it **cannot be modified**.

Example

```python
name = "Python"

name[0] = "J"
```

Output

```
TypeError

'str' object does not support item assignment
```

---

## Then What Happens?

Example

```python
name = "Python"

name += "3"
```

Python does **not** modify the original string.

Instead

```
Old Object

↓

"Python"

↓

New Object

↓

"Python3"
```

A completely new object is created.

---

# Why Are Strings Immutable?

Advantages

✅ Faster hashing

✅ Safe dictionary keys

✅ Thread-safe

✅ Memory optimization

✅ String interning

---

# Internal Working

Internally,

a string is stored as

```
Object Header

↓

Length

↓

Hash

↓

Unicode Characters
```

Python also caches many strings to reduce memory usage.

---

# Unicode Support

Python strings store **Unicode characters**.

Example

```python
text = "नमस्ते"

print(text)
```

Output

```
नमस्ते
```

---

Emoji

```python
print("😀")
```

Works perfectly.

---

# Creating Strings

Using double quotes

```python
name = "Python"
```

---

Single quotes

```python
name = 'Python'
```

---

Triple quotes

```python
text = """
Hello

Python
"""
```

Useful for

- Multi-line strings
- SQL Queries
- Documentation

---

# String Indexing

Every character has an index.

```
P  y  t  h  o  n

0  1  2  3  4  5
```

Example

```python
name = "Python"

print(name[0])
```

Output

```
P
```

---

Last character

```python
print(name[5])
```

Output

```
n
```

---

# Negative Indexing

Python also supports negative indexing.

```
 P  y  t  h  o  n

-6 -5 -4 -3 -2 -1
```

Example

```python
print(name[-1])
```

Output

```
n
```

---

# String Slicing

Syntax

```python
string[start:end:step]
```

Example

```python
name = "Python"

print(name[1:4])
```

Output

```
yth
```

---

Beginning

```python
print(name[:3])
```

Output

```
Pyt
```

---

End

```python
print(name[2:])
```

Output

```
thon
```

---

Entire String

```python
print(name[:])
```

Creates a new string.

---

Reverse String

```python
print(name[::-1])
```

Output

```
nohtyP
```

---

# Slicing Creates a New Object

```python
name = "Python"

copy = name[:]

print(name is copy)
```

Depending on Python optimizations, this may return `True` or `False`, but you should **treat slicing as producing a new string value**, not rely on object identity.

---

# String Concatenation

```python
first = "Hello"

second = "Python"

print(first + second)
```

Output

```
HelloPython
```

### Complexity

```
O(n)
```

A new string is created.

---

# String Repetition

```python
print("Hi " * 3)
```

Output

```
Hi Hi Hi
```

Complexity

```
O(n × k)
```

where

```
n

↓

Length

k

↓

Repetitions
```

---

# Escape Sequences

| Escape | Meaning |
|---------|---------|
| \n | New Line |
| \t | Tab |
| \\ | Backslash |
| \' | Single Quote |
| \" | Double Quote |

Example

```python
print("Hello\nPython")
```

Output

```
Hello

Python
```

---

# Raw Strings

Ignore escape sequences.

Example

```python
path = r"C:\Users\Nitin"

print(path)
```

Output

```
C:\Users\Nitin
```

Useful for

- Windows paths
- Regular Expressions

---

# Memory Optimization

Python internally performs

```
String Interning
```

Frequently used strings may share memory.

Example

```python
a = "hello"

b = "hello"
```

Often

```python
a is b
```

returns

```
True
```

Do **not** rely on this optimization.

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Indexing | O(1) |
| Length | O(1) |
| Slicing | O(k) |
| Concatenation | O(n) |
| Membership (`in`) | O(n) |
| Iteration | O(n) |

---

# Best Practices

✅ Use f-strings for formatting.

✅ Avoid repeated string concatenation in loops.

✅ Use `"".join()` when joining many strings.

✅ Use raw strings for file paths and regex.

---

# Common Mistakes

❌

```python
name[0] = "J"
```

Strings are immutable.

---

❌

Using

```python
+=
```

inside large loops.

This creates many temporary strings.

---

# DSA Tips

- String slicing creates a new string.
- Membership (`x in string`) is O(n).
- Prefer lists when you need frequent modifications.
- Convert to a list when performing many character updates, then `''.join()` at the end.

---

# Interview Questions

1. Why are strings immutable?
2. Why is string concatenation O(n)?
3. Difference between indexing and slicing?
4. What is string interning?
5. Why are strings good dictionary keys?
6. What is a raw string?
7. Difference between `str()` and `repr()`? *(We'll revisit this later.)*
8. Why is `len()` O(1) for strings?

---

# Quick Revision

✔ Strings are immutable.

✔ Strings store Unicode characters.

✔ Indexing is O(1).

✔ Slicing is O(k).

✔ Concatenation creates a new string.

✔ Python interns many strings.

✔ Raw strings ignore escape sequences.

✔ Use `''.join()` for efficient string building.