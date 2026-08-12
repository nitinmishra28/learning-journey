# ⚡ Python Short-Circuiting

Short-circuiting means Python **stops evaluating an expression as soon as the final result is already known**.

It mainly happens with:

- `and`
- `or`

Short-circuiting is important for:

- DSA conditions
- Avoiding unnecessary computation
- Preventing errors
- Writing clean Python conditions

---

# 🔹 `and` Short-Circuiting

For `and`:

```text
False AND anything
        ↓
      False
```

Once Python encounters a **falsy** value, it stops evaluating the remaining expression.

```python
a = False

result = a and expensive_function()
```

Since `a` is `False`, Python never executes:

```python
expensive_function()
```

---

# 🔹 `or` Short-Circuiting

For `or`:

```text
True OR anything
       ↓
      True
```

Once Python encounters a **truthy** value, it stops evaluating the remaining expression.

```python
x = True

result = x or expensive_function()
```

Since `x` is already `True`, Python never executes:

```python
expensive_function()
```

---

# 🔄 Evaluation Order

Python evaluates logical expressions:

```text
Left → Right
```

Example:

```python
A and B and C
```

Python evaluates:

```text
A
↓
B
↓
C
```

But it stops as soon as the final result is known.

---

# ⭐ `and` Rule

```text
and
 ↓
Stop at first Falsy value
```

Example:

```python
False and X
```

`X` is never evaluated.

If all values are truthy:

```python
True and True and 10
```

the last value is returned.

---

# ⭐ `or` Rule

```text
or
 ↓
Stop at first Truthy value
```

Example:

```python
True or X
```

`X` is never evaluated.

If all values are falsy:

```python
False or 0 or ""
```

the last value is returned.

---

# 🧠 `and` and `or` Return Values

A very important Python concept:

`and` and `or` do **not necessarily return `True` or `False`**.

They return one of their operands.

---

# `and`

`and` returns the **first falsy value**.

If everything is truthy, it returns the **last value**.

```python
result = 10 and 20

print(result)
```

Output:

```text
20
```

Why?

```text
10 → Truthy
20 → Returned
```

---

Another example:

```python
result = 0 and 20

print(result)
```

Output:

```text
0
```

Python stops at `0`.

---

Another example:

```python
result = "Hello" and 100

print(result)
```

Output:

```text
100
```

---

# `or`

`or` returns the **first truthy value**.

If everything is falsy, it returns the **last value**.

```python
result = 0 or 10

print(result)
```

Output:

```text
10
```

Why?

```text
0 → Falsy
10 → Truthy
```

---

Another example:

```python
result = 100 or 200

print(result)
```

Output:

```text
100
```

Python stops immediately.

---

# 📌 Quick Mental Model

Remember:

```text
and → First Falsy
or  → First Truthy
```

If no stopping value is found:

```text
and → Last Value
or  → Last Value
```

---

# 🔍 Truthy and Falsy Values

Common falsy values in Python:

```python
False
None
0
0.0
""
[]
()
{}
set()
```

Most other values are truthy.

---

# ⭐ DSA Pattern — Safe List Access

A very common Python pattern:

```python
if arr and arr[-1] == target:
    ...
```

Python first checks:

```python
arr
```

If:

```python
arr = []
```

the list is falsy.

Python stops and never evaluates:

```python
arr[-1]
```

Therefore, we avoid:

```text
IndexError
```

---

# 🌳 Linked List / Tree Pattern

```python
if node and node.left:
    ...
```

Python first checks:

```python
node
```

If:

```python
node = None
```

Python stops.

It never tries:

```python
node.left
```

This prevents:

```text
AttributeError
```

This pattern is common in:

- Linked Lists
- Trees
- Graphs

---

# 📚 Stack Pattern

```python
if stack and stack[-1] == "(":
    ...
```

If:

```python
stack = []
```

Python stops before accessing:

```python
stack[-1]
```

This prevents:

```text
IndexError
```

---

# 🚶 Queue Pattern

```python
if queue and queue[0] == target:
    ...
```

If the queue is empty, Python never accesses:

```python
queue[0]
```

---

# ➗ Division Pattern

```python
if divisor != 0 and num / divisor > 5:
    ...
```

Python first checks:

```python
divisor != 0
```

If this is `False`, division is never performed.

This prevents:

```text
ZeroDivisionError
```

---

# 🔥 Why This Matters in DSA

Short-circuiting allows us to combine:

```text
Safety Check
     +
Actual Operation
```

Example:

```python
if stack and stack[-1] > 0:
    ...
```

Think:

```text
Is stack non-empty?
        ↓
      Yes
        ↓
Access stack[-1]
```

This is extremely common in:

- Stack problems
- Queue problems
- Linked Lists
- Trees
- Graphs
- Sliding Window

---

# `or` for Default Values

A common Python pattern:

```python
name = user_input or "Guest"
```

If:

```python
user_input = ""
```

then:

```python
name = "Guest"
```

Because:

```text
""       → Falsy
"Guest"  → Truthy
```

---

# ⚠️ Important Trap

Consider:

```python
age = user_age or 18
```

Suppose:

```python
user_age = 0
```

Then:

```python
age = 18
```

because `0` is falsy.

But `0` might be a valid value.

If you specifically want to check for `None`, use:

```python
age = 18 if user_age is None else user_age
```

Remember:

```text
Falsy ≠ None
```

---

# 🔥 Short-Circuiting with Function Calls

```python
def check():
    print("Executed")
    return True
```

Now:

```python
False and check()
```

Nothing is printed.

Why?

```text
False
  ↓
Stop
```

---

But:

```python
True and check()
```

prints:

```text
Executed
```

Because Python must evaluate the second operand.

---

# `or` Example

```python
True or check()
```

Nothing is printed.

Python already knows:

```text
True OR anything
=
True
```

Therefore, it stops.

---

# 🔗 Chained Conditions

Example:

```python
if x > 0 and x < 10 and arr[x] == 5:
    ...
```

Python evaluates from left to right.

If:

```python
x > 0
```

is `False`:

```text
STOP
```

It never evaluates the remaining conditions.

If it is `True`, Python checks:

```python
x < 10
```

If that is `False`:

```text
STOP
```

Only when both are true does Python evaluate:

```python
arr[x] == 5
```

---

# `and` vs `&`

Do not confuse:

```python
and
```

with:

```python
&
```

`and` is a logical operator and supports short-circuiting.

Example:

```python
False and expensive_function()
```

The function is not executed.

`&` is a bitwise operator for integers and is also used by types such as sets.

They are different operators.

---

# `or` vs `|`

Similarly:

```python
or
```

is a logical operator.

```python
True or expensive_function()
```

The function is not executed.

While:

```python
|
```

is a bitwise/set operator.

They are different operations.

---

# ⚡ Performance Benefit

Short-circuiting can avoid unnecessary computation.

Example:

```python
if condition1 and expensive_operation():
    ...
```

If:

```python
condition1
```

is `False`, Python never calls:

```python
expensive_operation()
```

Therefore, when possible, put a **cheap condition that can fail early** before an expensive condition.

---

# ✅ Best Practice

Prefer:

```python
if node and node.value == target:
    ...
```

instead of trying to access:

```python
node.value
```

before checking whether `node` exists.

Similarly:

```python
if divisor != 0 and num / divisor > 5:
    ...
```

Check the safety condition first.

---

# ❌ Common Mistakes

## Mistake 1 — Thinking `and` always returns Boolean

```python
result = 10 and 20

print(result)
```

Output:

```text
20
```

---

## Mistake 2 — Thinking `or` always returns Boolean

```python
result = 0 or 50

print(result)
```

Output:

```text
50
```

---

## Mistake 3 — Confusing `and` with `&`

```python
and
```

and

```python
&
```

are different operators.

---

## Mistake 4 — Confusing `or` with `|`

```python
or
```

and

```python
|
```

are different operators.

---

## Mistake 5 — Forgetting Falsy Values

Remember:

```python
False
None
0
0.0
""
[]
()
{}
set()
```

are falsy.

---

# 📊 Quick Reference

| Expression | Behavior |
|------------|----------|
| `A and B` | Stops at first falsy |
| `A or B` | Stops at first truthy |
| `and` | Returns first falsy, otherwise last value |
| `or` | Returns first truthy, otherwise last value |
| Evaluation | Left → Right |

---

# 🎯 DSA Patterns to Remember

### Safe Stack Access

```python
if stack and stack[-1] == target:
    ...
```

### Safe Queue Access

```python
if queue and queue[0] == target:
    ...
```

### Safe List Access

```python
if arr and arr[-1] == target:
    ...
```

### Safe Node Access

```python
if node and node.left:
    ...
```

### Safe Division

```python
if divisor != 0 and num / divisor > 5:
    ...
```

---

# 🎤 Interview Questions

1. What is short-circuit evaluation?
2. How does `and` short-circuit?
3. How does `or` short-circuit?
4. What does `and` return?
5. What does `or` return?
6. Why is `arr and arr[-1]` safe for an empty list?
7. How can short-circuiting prevent `ZeroDivisionError`?
8. What is the difference between `and` and `&`?
9. What is the difference between `or` and `|`?
10. Give a DSA example where short-circuiting prevents an exception.

---

# 📝 Quick Revision

✔ Python evaluates `and` and `or` from left to right.

✔ `and` stops at the first falsy value.

✔ `or` stops at the first truthy value.

✔ `and` returns the first falsy operand.

✔ If all operands are truthy, `and` returns the last operand.

✔ `or` returns the first truthy operand.

✔ If all operands are falsy, `or` returns the last operand.

✔ Short-circuiting prevents unnecessary computation.

✔ Short-circuiting can prevent errors.

✔ `arr and arr[-1]` is a common DSA pattern.

✔ `node and node.left` is common in trees and linked lists.

✔ `divisor != 0 and num / divisor` safely protects division.

✔ `and` is different from `&`.

✔ `or` is different from `|`.

---

# ⭐ Remember

```text
and → First Falsy
or  → First Truthy
```

This is the main rule to remember.