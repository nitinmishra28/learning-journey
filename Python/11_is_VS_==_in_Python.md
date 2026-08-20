# `is` vs `==` in Python

## 1. Core Difference

Both `is` and `==` are comparison operators, but they compare different things.

| Operator | Checks | Meaning |
|---|---|---|
| `==` | Equality | Do these objects have the same value? |
| `is` | Identity | Are these the exact same object? |

### Remember

```text
== → Same value?
is → Same object?
```

---

## 2. `==` — Equality

`==` compares the **value/content** of objects.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
```

Output:

```text
True
```

Both lists contain the same values.

But they are still separate objects.

```text
a → [1, 2, 3]   ← Object 1

b → [1, 2, 3]   ← Object 2
```

So:

```python
a == b     # True
```

---

## 3. `is` — Identity

`is` checks whether two variables refer to the **same object**.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
```

Output:

```text
False
```

Because:

```text
a → Object 1
b → Object 2
```

The values are the same, but the objects are different.

---

## 4. Same Object Example

When you do:

```python
a = [1, 2, 3]
b = a
```

Python does not create another list.

Both variables refer to the same object:

```text
a ─────┐
       ↓
   [1, 2, 3]
       ↑
b ─────┘
```

Therefore:

```python
print(a == b)   # True
print(a is b)   # True
```

This is an important distinction:

```python
a = [1, 2, 3]
b = [1, 2, 3]

a == b     # True
a is b     # False
```

versus:

```python
a = [1, 2, 3]
b = a

a == b     # True
a is b     # True
```

---

## 5. `id()` and Identity

Python's `id()` function returns an identifier for an object during its lifetime.

```python
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
```

Both IDs are the same because both variables refer to the same object.

Conceptually:

```python
a is b
```

corresponds to checking whether:

```python
id(a) == id(b)
```

In normal code, use `is` when you need an identity check rather than manually comparing IDs.

---

## 6. The Most Important Use: `None`

Use:

```python
is None
```

to check for `None`.

```python
result = None

if result is None:
    print("No result")
```

Similarly:

```python
if result is not None:
    print("Result exists")
```

### Why `is`?

`None` is a singleton object in Python. There is one `None` object, so we are checking whether the variable refers to that exact object.

### Preferred

```python
if value is None:
    ...
```

### Avoid

```python
if value == None:
    ...
```

The same rule applies to `is not None`.

---

## 7. Do NOT Use `is` for Value Comparison

Use `==` when comparing values.

### Correct

```python
x = 10

if x == 10:
    print("x is 10")
```

### Wrong

```python
if x is 10:
    print("x is 10")
```

Similarly:

```python
name == "Nitin"      # Correct
name is "Nitin"      # Wrong
```

```python
list1 == list2       # Correct
list1 is list2       # Only if you specifically want to check same object
```

---

## 8. Integer and String Interning

You may sometimes see surprising results like:

```python
a = 10
b = 10

print(a == b)   # True
print(a is b)   # Often True
```

Python may reuse certain immutable objects as an optimization.

Strings can also show this behavior:

```python
a = "hello"
b = "hello"

print(a == b)   # True
print(a is b)   # May be True
```

### Important

Never use this behavior for value comparison.

Do:

```python
a == b
```

not:

```python
a is b
```

The fact that `is` sometimes returns `True` for integers or strings does **not** mean `is` compares their values.

---

## 9. `==` Can Use `__eq__()`

Python classes can define how equality works using `__eq__()`.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
```

Now:

```python
s1 = Student("Nitin")
s2 = Student("Nitin")

print(s1 == s2)
print(s1 is s2)
```

Output:

```text
True
False
```

Why?

```python
s1 == s2
```

uses the custom equality logic.

But:

```python
s1 is s2
```

still checks whether they are the exact same object.

---

## 10. Mutable Objects Example

This is useful for understanding why identity matters.

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)
```

Output:

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

Because:

```python
a is b
```

is `True`.

Both variables refer to the same list.

Compare that with:

```python
a = [1, 2, 3]
b = [1, 2, 3]

b.append(4)

print(a)
print(b)
```

Output:

```text
[1, 2, 3]
[1, 2, 3, 4]
```

Here:

```python
a is b
```

is `False`.

---

# 11. Common Interview Traps

### Trap 1

```python
a = [1, 2]
b = [1, 2]

print(a == b)   # True
print(a is b)   # False
```

**Reason:** Same value, different objects.

---

### Trap 2

```python
a = [1, 2]
b = a

print(a == b)   # True
print(a is b)   # True
```

**Reason:** Same object.

---

### Trap 3

```python
x = None

print(x is None)
```

Output:

```text
True
```

This is the recommended way to check for `None`.

---

### Trap 4

```python
a = 10
b = 10

print(a is b)
```

Do not rely on the result.

Python may reuse the same integer object.

For value comparison:

```python
a == b
```

---

# 12. Interview Questions

### Q1. What is the difference between `is` and `==`?

**Answer:**

> `==` checks equality of values, while `is` checks object identity.

---

### Q2. Can `==` be `True` while `is` is `False`?

Yes.

```python
a = [1, 2]
b = [1, 2]

a == b     # True
a is b     # False
```

---

### Q3. Can both be `True`?

Yes.

```python
a = [1, 2]
b = a

a == b     # True
a is b     # True
```

---

### Q4. Why do we use `is None` instead of `== None`?

Because `None` is a singleton and we want to check whether the variable refers to that exact object.

```python
value is None
```

is the standard Python style.

---

### Q5. Should `is` be used for comparing strings or integers?

No.

Use:

```python
==
```

for value comparison.

Use:

```python
is
```

when identity itself matters.

---

# 13. Quick Revision

```text
==

→ Equality
→ Compares values
→ Use for numbers, strings, lists, objects, etc.


is

→ Identity
→ Compares object identity
→ Use when you specifically care whether two references
  point to the same object.


None

→ Use: is None
→ Use: is not None
→ Avoid: == None
```

### One example to remember forever:

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a == b     # True
a is b     # False

a == c     # True
a is c     # True
```

### Golden Rule

```text
== → Same value?
is → Same object?
```