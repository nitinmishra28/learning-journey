---

# ⚖️ Comparison Operators

Comparison operators compare two values and always return a **Boolean (`True` or `False`)**.

## Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| == | Equal to | a == b |
| != | Not Equal to | a != b |
| > | Greater Than | a > b |
| < | Less Than | a < b |
| >= | Greater Than or Equal | a >= b |
| <= | Less Than or Equal | a <= b |

---

## Equal To (==)

Checks whether two values are equal.

```python
print(10 == 10)
```

Output

```
True
```

Example

```python
print("Python" == "Python")
```

Output

```
True
```

### Time Complexity

```
Numbers : O(1)

Strings : O(n)

Lists : O(n)

Tuples : O(n)
```

Because every element may need comparison.

---

## Not Equal (!=)

```python
print(10 != 20)
```

Output

```
True
```

---

## Greater Than (>)

```python
print(20 > 10)
```

Output

```
True
```

---

## Less Than (<)

```python
print(5 < 2)
```

Output

```
False
```

---

## Greater Than or Equal (>=)

```python
print(10 >= 10)
```

Output

```
True
```

---

## Less Than or Equal (<=)

```python
print(10 <= 15)
```

Output

```
True
```

---

# Chained Comparisons ⭐

Python allows chaining comparisons.

Example

```python
x = 15

print(10 < x < 20)
```

Output

```
True
```

Instead of writing

```python
10 < x and x < 20
```

Python internally evaluates it efficiently.

---

### Multiple Comparisons

```python
print(1 < 2 < 3 < 4)
```

Output

```
True
```

---

# Comparing Different Data Types

```python
print(10 == 10.0)
```

Output

```
True
```

Because

```
10 == 10.0
```

is mathematically equal.

But

```python
print(type(10))
print(type(10.0))
```

Output

```
<class 'int'>

<class 'float'>
```

---

# Comparing Lists

```python
print([1,2] == [1,2])
```

Output

```
True
```

Comparison happens element by element.

---

# Comparing Tuples

```python
print((1,2) == (1,2))
```

Output

```
True
```

---

# Lexicographical Comparison ⭐

Python compares strings like a dictionary.

```python
print("apple" < "banana")
```

Output

```
True
```

Comparison happens character by character using Unicode values.

---

Example

```python
print("abc" < "abd")
```

Output

```
True
```

---

# Logical Operators

Logical operators combine multiple conditions.

| Operator | Meaning |
|----------|---------|
| and | Both must be True |
| or | At least one True |
| not | Reverses Boolean |

---

## and

```python
age = 20

print(age > 18 and age < 30)
```

Output

```
True
```

---

## Truth Table

| A | B | A and B |
|---|---|----------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

---

## or

```python
print(True or False)
```

Output

```
True
```

Truth Table

| A | B | A or B |
|---|---|---------|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

---

## not

```python
print(not True)
```

Output

```
False
```

---

# ⭐ Short-Circuit Evaluation (Very Important)

Python does **not** evaluate unnecessary expressions.

---

## Short-Circuit with `and`

```python
False and print("Hello")
```

Output

```
False
```

`print()` is never executed.

Why?

Because

```
False AND Anything

↓

False
```

Python already knows the answer.

---

## Short-Circuit with `or`

```python
True or print("Hello")
```

Output

```
True
```

Again,

`print()` never executes.

---

### Why is this useful?

```python
if obj is not None and obj.is_valid():
```

Python checks

```
obj is not None
```

first.

If it's `False`, the second condition isn't evaluated.

This prevents errors like

```
AttributeError
```

---

# Return Value of Logical Operators ⭐

Many beginners think

```python
and

or
```

always return `True` or `False`.

Not true.

They return one of the operands.

---

Example

```python
print(10 and 20)
```

Output

```
20
```

---

```python
print(0 and 20)
```

Output

```
0
```

---

```python
print("" or "Python")
```

Output

```
Python
```

---

Rule

### `and`

Returns the **first falsy value**.

Otherwise returns the last value.

---

### `or`

Returns the **first truthy value**.

Otherwise returns the last value.

---

# Membership Operators

Checks whether an element exists.

| Operator | Meaning |
|----------|---------|
| in | Exists |
| not in | Doesn't Exist |

---

## in

```python
nums = [1,2,3]

print(2 in nums)
```

Output

```
True
```

---

## not in

```python
print(10 not in nums)
```

Output

```
True
```

---

### Complexity

| Data Structure | Complexity |
|---------------|------------|
| List | O(n) |
| Tuple | O(n) |
| String | O(n) |
| Set | O(1) Average |
| Dictionary Keys | O(1) Average |

---

### DSA Tip

Whenever you need frequent membership checking,

Don't use

```python
x in list
```

Use

```python
x in set
```

Much faster.

---

# Identity Operators

Identity checks memory location.

| Operator | Meaning |
|----------|---------|
| is | Same Object |
| is not | Different Objects |

---

Example

```python
a = [1,2]

b = a

print(a is b)
```

Output

```
True
```

---

```python
c = [1,2]

print(a is c)
```

Output

```
False
```

---

### `is` vs `==`

```python
a = [1,2]

b = [1,2]
```

```
a == b

↓

True
```

```
a is b

↓

False
```

Remember

```
==

↓

Value
```

```
is

↓

Identity
```

---

# Best Practices

✅ Use `==` for comparing values.

✅ Use `is` only for

```python
None
```

or identity checks.

✅ Use chained comparisons when possible.

✅ Take advantage of short-circuit evaluation.

---

# Common Mistakes

❌

```python
if x == None
```

Correct

```python
if x is None
```

---

❌

```python
a is 1000
```

Never use

```
is
```

for comparing numbers or strings.

---

❌

Using

```python
x in list
```

inside large loops.

Convert to

```python
set
```

first.

---

# DSA Tips

- Membership in `set` and `dict` is **O(1)** on average.
- Use short-circuit evaluation to avoid unnecessary computations.
- Chained comparisons make conditions cleaner and often more readable.
- Prefer `is None` over `== None`.

---

# Interview Questions

1. Difference between `==` and `is`?
2. What is short-circuit evaluation?
3. Why is `x in set` faster than `x in list`?
4. What does `10 and 20` return?
5. What does `0 or 100` return?
6. How does Python compare strings?
7. Explain chained comparisons.
8. Why is `is None` preferred?

---

# Quick Revision

✔ Comparison operators return Booleans.

✔ Strings are compared lexicographically.

✔ `and` and `or` use short-circuit evaluation.

✔ `and` returns the first falsy value.

✔ `or` returns the first truthy value.

✔ Use `set` for fast membership checking.

✔ `==` compares values.

✔ `is` compares object identity.