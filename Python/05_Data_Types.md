content: |
  ---
  # 🧠 Python Object Model

  One of the most important concepts in Python is:

  > **Everything in Python is an Object.**

Unlike C or C++, where primitive types (like `int`, `char`, `float`) are not objects, Python treats **every value as an object**.

Examples:

```python
x = 10
y = 3.14
name = "Python"
numbers = [1, 2, 3]
```

All of these are objects.

---

## Every Object Has Three Properties

Every object in Python has:

1. **Identity**
2. **Type**
3. **Value**

Example:

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

---

## Identity

Identity is the unique memory address of an object.

Use

```python
id()
```

to get it.

Example

```python
x = 10

print(id(x))
```

Every object has a unique identity during its lifetime.

---

## Type

Type defines what kind of object it is.

Example

```python
type(10)

type("Python")

type([1,2,3])
```

Output

```
<class 'int'>

<class 'str'>

<class 'list'>
```

---

## Value

The actual data stored inside the object.

Example

```python
x = 25
```

Identity

```
14029385...
```

Type

```
int
```

Value

```
25
```

---

# 📦 Variables Don't Store Values

This is one of the biggest misconceptions.

Many beginners think

```
Variable

↓

Value
```

This is **incorrect**.

Python actually does

```
Variable

↓

Reference

↓

Object
```

Example

```python
x = 100
```

Internally

```
x

↓

Integer Object (100)
```

Variables simply reference objects.

---

# Object References

Example

```python
x = 10

y = x
```

Internally

```
      x

       \

        → 10 ← y
```

Both variables point to the same object.

Verify

```python
print(id(x))

print(id(y))
```

Output

```
140312345

140312345
```

Same identity.

---

# 📌 Identity (`is`) vs Equality (`==`)

This is one of Python's favorite interview questions.

---

## Equality (`==`)

Checks whether values are equal.

Example

```python
a = [1,2,3]

b = [1,2,3]

print(a == b)
```

Output

```
True
```

Because values are the same.

---

## Identity (`is`)

Checks whether both variables point to the same object.

```python
print(a is b)
```

Output

```
False
```

Different objects.

---

## Example

```python
x = [1,2]

y = x

print(x == y)

print(x is y)
```

Output

```
True

True
```

Because both refer to the same object.

---

# 🎯 When to Use `is`

Use `is` only when checking object identity.

Especially

```python
if value is None:
```

Preferred over

```python
if value == None:
```

Reason:

`is` checks identity and is faster for singleton objects like `None`.

---

# 🧊 Small Integer Caching (Interview Favorite)

Python caches small integers.

Range

```
-5 to 256
```

Example

```python
a = 100

b = 100

print(a is b)
```

Output

```
True
```

Because Python reuses the same object.

---

Now

```python
a = 1000

b = 1000

print(a is b)
```

Depending on the Python implementation, this may return `False`.

### Why?

Python usually doesn't cache large integers.

> **Note:** Small integer caching is an implementation detail of CPython. Don't rely on it for program logic.

---

# 📚 String Interning

Python also caches many string literals.

Example

```python
a = "hello"

b = "hello"

print(a is b)
```

Often

```
True
```

Python reuses the same immutable string object.

Again, don't rely on this behavior in your programs.

---

# 🔄 Mutable vs Immutable (Deep Understanding)

Immutable objects

```
int

float

bool

tuple

str

frozenset

bytes
```

Cannot change after creation.

Example

```python
x = "Python"

x += "3"
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

---

Mutable objects

```
list

dict

set

bytearray
```

Can change without creating a new object.

Example

```python
numbers = [1,2]

numbers.append(3)
```

The same object is modified.

---

# Why Does This Matter?

Because mutable and immutable objects behave differently when passed to functions, copied, or assigned.

We'll study this in detail in later chapters.

---

# 📊 Memory Representation

Immutable

```
Variable

↓

Object

↓

Cannot Change
```

Mutable

```
Variable

↓

Object

↓

Can Change
```

---

# 🔄 Type Conversion

Python provides two types of conversion.

## Implicit Conversion

Python automatically converts compatible types.

Example

```python
x = 10

y = 5.5

print(x + y)
```

Output

```
15.5
```

Integer converted to float automatically.

---

## Explicit Conversion

You convert manually.

```python
age = int("25")
```

---

More examples

```python
float(10)

str(25)

bool(0)

list("ABC")

tuple([1,2,3])

set([1,2,2,3])
```

Output

```
10.0

"25"

False

['A','B','C']

(1,2,3)

{1,2,3}
```

---

# ⚠ Dangerous Conversions

```python
int("Python")
```

Output

```
ValueError
```

---

```python
int(3.9)
```

Output

```
3
```

Notice

It **truncates**.

It does **not** round.

---

# 📋 Data Type Summary

| Type | Mutable | Ordered | Example |
|------|----------|---------|---------|
| int | ❌ | N/A | 10 |
| float | ❌ | N/A | 3.14 |
| complex | ❌ | N/A | 2+3j |
| bool | ❌ | N/A | True |
| str | ❌ | ✅ | "Python" |
| list | ✅ | ✅ | [1,2] |
| tuple | ❌ | ✅ | (1,2) |
| dict | ✅ | ✅* | {"a":1} |
| set | ✅ | ❌ | {1,2} |
| frozenset | ❌ | ❌ | frozenset({1}) |
| bytes | ❌ | ✅ | b"abc" |
| bytearray | ✅ | ✅ | bytearray(b"abc") |
| None | ❌ | N/A | None |

> **Note:** Dictionaries preserve insertion order in Python 3.7+, but conceptually they are hash maps.

---

# 💡 Best Practices

✅ Prefer `isinstance()` over `type()`.

✅ Use `is None` instead of `== None`.

✅ Understand mutable vs immutable objects before learning lists and dictionaries.

✅ Don't rely on object IDs or caching behavior.

---

# ⚠ Common Mistakes

❌ Using

```python
a is b
```

to compare values.

Use

```python
a == b
```

unless you specifically want identity comparison.

---

❌ Thinking variables store values.

Variables store **references to objects**.

---

❌ Assuming every equal object has the same identity.

They can have equal values but different memory addresses.

---

# 🧠 DSA Tips

- Lists are mutable; changes affect all references to the same list.
- Strings and tuples are immutable, making them safe as dictionary keys.
- Use `==` to compare contents.
- Use `is` only for identity checks (especially `None`).

---

# 💼 Interview Questions

1. What is the difference between `==` and `is`?
2. Why does Python cache small integers?
3. What is string interning?
4. Do variables store values?
5. What is object identity?
6. Why are strings immutable?
7. Difference between implicit and explicit type conversion?
8. Why is `is None` preferred over `== None`?

---

# 📌 Quick Revision

- Everything in Python is an object.
- Every object has identity, type, and value.
- Variables reference objects.
- `==` compares values.
- `is` compares identities.
- Python caches small integers (`-5` to `256`) in CPython.
- Immutable objects create new objects when modified.
- Mutable objects change in place.
- Use `is None` for checking `None`.