# Walrus Operator `:=` in Python

The **walrus operator** `:=` is called the **assignment expression operator**.

It allows you to **assign a value to a variable and use that value in the same expression**.

```text
=   → normal assignment
:=  → assignment + expression
```

---

## 1. Basic Example

Without the walrus operator:

```python
name = input("Enter your name: ")

if name:
    print(name)
```

With the walrus operator:

```python
if name := input("Enter your name: "):
    print(name)
```

Here:

```python
name := input(...)
```

does two things:

1. Assigns the input to `name`
2. Produces that value so the `if` condition can use it

---

## 2. `=` vs `:=`

### Normal assignment

```python
x = 10
```

This assigns `10` to `x`.

### Assignment expression

```python
(x := 10)
```

This:

1. Assigns `10` to `x`
2. Evaluates to `10`

For example:

```python
print(x := 10)
```

Output:

```text
10
```

Afterwards:

```python
print(x)
```

Output:

```text
10
```

So the key idea is:

```text
x := 10

x gets → 10
expression produces → 10
```

---

## 3. Common Use Case: `while`

Without `:=`:

```python
line = input()

while line != "quit":
    print(line)
    line = input()
```

With `:=`:

```python
while (line := input()) != "quit":
    print(line)
```

Here:

```python
line := input()
```

stores the input in `line` and also gives that value to the condition.

---

## 4. Using It in `if`

```python
numbers = [1, 2, 3, 4, 5]

if (n := len(numbers)) > 3:
    print(f"Length is {n}")
```

Output:

```text
Length is 5
```

Without the walrus operator:

```python
n = len(numbers)

if n > 3:
    print(f"Length is {n}")
```

The walrus operator combines the assignment and condition into one expression.

---

## 5. Why Parentheses Are Often Used

You will commonly see:

```python
if (n := len(numbers)) > 3:
    print(n)
```

The parentheses clearly show that:

```python
(n := len(numbers))
```

is the assignment expression.

Then its result is compared:

```python
(n := len(numbers)) > 3
```

Prefer parentheses when they make the expression easier to understand.

---

## 6. Useful When a Value Is Needed Twice

Suppose a function performs some calculation:

```python
result = some_function()

if result:
    print(result)
```

The walrus operator can combine these when the value is only needed as part of the condition and inside the block:

```python
if (result := some_function()):
    print(result)
```

The function is called once, and its result is stored in `result`.

---

## 7. Regular Expression Example

A common practical use is with regular expressions:

```python
import re

text = "My phone number is 12345"

if match := re.search(r"\d+", text):
    print(match.group())
```

Output:

```text
12345
```

Here:

```python
match := re.search(...)
```

stores the match object in `match`.

The `if` condition checks whether a match was found.

Without the walrus operator:

```python
match = re.search(r"\d+", text)

if match:
    print(match.group())
```

---

## 8. Important: Don't Use It Everywhere

The walrus operator is useful, but it should not be used simply to reduce the number of lines.

For example:

```python
if (x := calculate_something()) > 10:
    print(x)
```

can be good when `x` is needed inside the block.

But sometimes this is clearer:

```python
x = calculate_something()

if x > 10:
    print(x)
```

### Rule

> Use `:=` when it improves readability or avoids unnecessary repeated work.

Don't make code unnecessarily clever.

---

## 9. Scope

The variable created by a walrus operator follows Python's normal scope rules.

```python
if (x := 10):
    print(x)

print(x)
```

Output:

```text
10
10
```

The variable is still available after the `if` block in the same scope.

---

## 10. Python Version

The walrus operator was introduced in:

```text
Python 3.8
```

So code using `:=` requires Python 3.8 or later.

---

# Interview Perspective

### Q1. What is the walrus operator?

> The walrus operator `:=` is Python's assignment expression operator. It allows us to assign a value to a variable while also using that value as part of an expression.

Example:

```python
if (n := len(items)) > 5:
    print(n)
```

---

### Q2. What is the difference between `=` and `:=`?

```text
= 
→ Normal assignment

:=
→ Assignment expression
→ Assigns a value and also produces that value as an expression
```

---

### Q3. Where is `:=` commonly useful?

Common use cases:

```text
→ while loops
→ if conditions
→ regular expressions
→ file/input processing
→ avoiding repeated calculations
```

---

### Q4. When was the walrus operator introduced?

Python 3.8.

---

# Quick Revision

```text
:= 
↓
Assignment Expression
↓
Assign a value + use that value immediately
```

### Basic example

```python
if (x := get_value()):
    print(x)
```

### `while` example

```python
while (line := input()) != "quit":
    print(line)
```

### Regex example

```python
if match := re.search(pattern, text):
    print(match.group())
```

### Golden Rule

```text
=   → normal assignment

:=  → assignment expression

Use := when:
1. You need to assign a value
2. You also need that value immediately in an expression
```