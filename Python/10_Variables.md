# 📦 Variables in Python

> Variables in Python are **names (references)** that point to objects in memory. Unlike many programming languages, variables do **not** store values directly.

---

# 📚 Table of Contents

- What is a Variable?
- Why Do We Need Variables?
- Variable Assignment
- How Variables Work Internally
- Object References
- Memory Addresses (`id()`)
- Multiple Assignment
- Multiple Variable Initialization
- Variable Swapping
- Dynamic Typing
- Variable Naming Rules
- Reserved Keywords
- Constants
- Best Practices
- Common Mistakes
- Interview Questions
- Quick Revision

---

# 📖 What is a Variable?

A variable is a **name** given to an object stored in memory.

Think of a variable as a label attached to an object.

Example

```python
name = "Nitin"
```

Here

```
name

↓

" Nitin "
```

`name` does **not** contain `"Nitin"`.

It simply points to the string object.

---

# 🤔 Why Do We Need Variables?

Without variables,

```python
print(10 + 20)

print(10 + 20)

print(10 + 20)
```

Instead

```python
total = 10 + 20

print(total)
print(total)
print(total)
```

Variables improve

- Readability
- Reusability
- Maintainability

---

# ⚙ Variable Assignment

Assignment uses

```
=
```

Example

```python
x = 100
```

Python

1. Creates an integer object.

2. Creates the name `x`.

3. Makes `x` point to that object.

Internally

```
x

↓

100
```

---

# 🧠 Variables Store References

This is one of Python's most important concepts.

Many beginners think

```
x

↓

100
```

means

```
Variable stores value
```

Actually

```
Variable

↓

Reference

↓

Object
```

Variables store references to objects.

---

# Example

```python
x = [10,20]

y = x
```

Memory

```
      x

       \

        →

      List Object

        ←

       /

      y
```

Both variables point to the **same object**.

---

# Verify Using id()

```python
x = [1,2]

y = x

print(id(x))
print(id(y))
```

Output

```
438728

438728
```

Same memory address.

---

# 🔥 Aliasing

When multiple variables reference the same object, it is called **Aliasing**.

Example

```python
numbers = [1,2,3]

backup = numbers
```

Now

```
numbers

↓

List

↑

backup
```

---

Modify

```python
backup.append(4)
```

Output

```python
print(numbers)
```

```
[1,2,3,4]
```

Why?

Because there is only **one list object**.

---

# Memory Address

Use

```python
id()
```

to check an object's identity.

Example

```python
x = 10

print(id(x))
```

Output

```
140293482
```

---

## Important

Memory addresses are **implementation details**.

Never write logic like

```python
if id(a) == id(b):
```

Use

```python
is
```

instead.

---

# Multiple Assignment

Python allows assigning multiple variables in one line.

```python
x = y = z = 100
```

Internally

```
x

 \

  \

   →

 100

   ↑

  /

 /

y

z
```

All variables point to the same object.

---

# Mutable Object Example ⭐

```python
a = b = []
```

Looks fine...

But

```python
a.append(10)

print(b)
```

Output

```
[10]
```

Because

```
a

↓

List

↑

b
```

Same object.

---

## Correct Way

```python
a = []

b = []
```

Now

Both lists are different.

---

# Multiple Variable Assignment

```python
name = "Nitin"

age = 23

city = "Bangalore"
```

Can be written as

```python
name, age, city = "Nitin", 23, "Bangalore"
```

---

# Tuple Packing

```python
person = "Nitin",23,"India"
```

Python creates

```python
("Nitin",23,"India")
```

automatically.

---

# Tuple Unpacking

```python
name, age, country = person
```

---

# Variable Swapping ⭐

Most languages require a temporary variable.

Example in C

```c
temp = a;

a = b;

b = temp;
```

Python

```python
a = 10

b = 20

a, b = b, a
```

Internally,

Python creates a temporary tuple.

```
(a,b)

↓

(b,a)
```

---

# Dynamic Typing

Variables have **no fixed type**.

Objects have types.

Example

```python
x = 100

x = "Python"

x = [1,2]
```

Perfectly valid.

---

# Variable Naming Rules

✅ Letters

```python
age
```

---

✅ Underscore

```python
_student
```

---

✅ Numbers (Not First)

```python
student1
```

---

❌

```python
1student
```

Invalid.

---

# Naming Conventions

Variable

```python
student_name
```

Function

```python
calculate_sum()
```

Class

```python
class Student
```

Constant

```python
MAX_SIZE
```

Private Variable

```python
_hidden
```

---

# Constants

Python has no true constants.

Convention

```python
PI = 3.14
```

Should not be modified.

---

# Best Practices

✅ Use meaningful names.

```python
student_marks
```

Instead of

```python
x
```

---

✅ Follow snake_case.

---

✅ Keep variable names descriptive.

---

# Common Mistakes

### Mistake 1

```python
a = b = []
```

Creates one list.

---

### Mistake 2

```python
list = [1,2]
```

Never overwrite built-in names.

---

### Mistake 3

Using

```python
l

O

I
```

as variable names.

They are difficult to read.

---

# Interview Questions

### Do variables store values?

No.

Variables store references.

---

### Difference between

```python
a = b
```

and

```python
a = b.copy()
```

---

### Why does

```python
a = b = []
```

cause problems?

---

### What is aliasing?

---

### What is tuple unpacking?

---

### Why is Python dynamically typed?

---

### Why should constants be uppercase?

---

# DSA Tips

✅ Avoid

```python
a = b = [[0]*3]*3
```

Huge bug.

---

✅ Use tuple unpacking.

```python
a,b = b,a
```

Cleaner and faster.

---

✅ Understand references before learning lists and dictionaries.

---

# Quick Revision

✔ Variables store references.

✔ Objects store values.

✔ Multiple variables can point to one object.

✔ `id()` returns object identity.

✔ Python supports multiple assignment.

✔ Python supports tuple unpacking.

✔ Python supports dynamic typing.

✔ Constants are a naming convention only.

---

# Practice Questions

## Theory

1. What is a variable?
2. Do variables store values?
3. Explain aliasing.
4. Explain tuple unpacking.
5. Why is Python dynamically typed?
6. Difference between object and variable?
7. Explain multiple assignment.
8. Explain constants.

---

## Coding

1. Swap two variables.
2. Use tuple unpacking.
3. Print object IDs.
4. Demonstrate aliasing.
5. Demonstrate dynamic typing.
6. Show why `a = b = []` is dangerous.
7. Create constants.
8. Assign multiple variables in one line.

---

# 🎉 Congratulations!

You have completed the fundamentals of variables.

In the next part, we'll go much deeper into:

- Variable Scope
- Local Variables
- Global Variables
- `global`
- `nonlocal`
- Namespace
- LEGB Rule
- Reference Counting
- Garbage Collection (Variable Perspective)
- Interning
- Object Lifetime