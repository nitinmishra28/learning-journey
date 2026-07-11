---

# 🔑 Python Keywords

Keywords are **reserved words** in Python that have predefined meanings.

You **cannot** use keywords as variable names, function names, or class names.

Example ❌

```python
if = 10
```

Output

```
SyntaxError
```

## How to View All Keywords

Python provides a built-in module named `keyword`.

```python
import keyword

print(keyword.kwlist)
```

Example Output

```python
['False', 'None', 'True', 'and', 'as', 'assert',
'async', 'await', 'break', 'class', 'continue',
'def', 'del', 'elif', 'else', 'except',
'finally', 'for', 'from', 'global',
'if', 'import', 'in', 'is', 'lambda',
'nonlocal', 'not', 'or', 'pass',
'raise', 'return', 'try', 'while',
'with', 'yield']
```

## Check if a Word is a Keyword

```python
import keyword

print(keyword.iskeyword("for"))
print(keyword.iskeyword("hello"))
```

Output

```
True
False
```

---

# 🆔 Identifiers

Identifiers are the names given to:

- Variables
- Functions
- Classes
- Modules
- Objects

Example

```python
name = "Nitin"

age = 22

def greet():
    pass

class Student:
    pass
```

Here,

- `name`
- `age`
- `greet`
- `Student`

are identifiers.

---

# Rules for Identifiers

✅ Can contain

- Letters
- Numbers
- Underscores

Example

```python
student_name

marks2025

_private
```

---

✅ Cannot start with a number

❌

```python
2name
```

---

✅ Cannot contain spaces

❌

```python
student name
```

---

✅ Cannot use keywords

❌

```python
class = 10
```

---

✅ Case Sensitive

```python
age

Age

AGE
```

All are different identifiers.

---

# Naming Conventions (PEP 8)

Variables

```python
student_name
```

Functions

```python
calculate_sum()
```

Classes

```python
class Student:
```

Constants

```python
PI = 3.14
```

Private Members

```python
_hidden
```

---

# 📝 Comments

Comments are ignored by Python.

They improve readability.

---

## Single-Line Comment

```python
# This is a comment

print("Hello")
```

---

## Multi-Line Comment

Python doesn't have true multi-line comments.

Instead, developers commonly use multiple `#` symbols.

```python
# First line

# Second line

# Third line
```

---

# 📄 Docstrings

Triple quotes are used for documentation.

Example

```python
def add(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b
```

Docstrings can be viewed using

```python
print(add.__doc__)
```

Output

```
Returns the sum of two numbers.
```

---

# 🖨️ print()

`print()` is one of the most frequently used built-in functions.

Syntax

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

---

## Printing Multiple Values

```python
print("Python", "Java", "C++")
```

Output

```
Python Java C++
```

---

# sep Parameter

Changes the separator.

```python
print("Python", "Java", sep="-")
```

Output

```
Python-Java
```

---

# end Parameter

Changes what is printed at the end.

Default

```python
print("Hello")
print("World")
```

Output

```
Hello
World
```

Using `end`

```python
print("Hello", end=" ")

print("World")
```

Output

```
Hello World
```

---

# flush Parameter

Normally, Python buffers output before displaying it.

`flush=True` forces Python to immediately display the output.

```python
print("Loading...", flush=True)
```

Useful in

- Progress bars
- Logging
- Real-time applications

---

# Return Value

```python
result = print("Hello")

print(result)
```

Output

```
Hello

None
```

## Interview Question

**Does `print()` return anything?**

Answer:

It always returns **None**.

---

# ⌨️ input()

Used to take input from the user.

```python
name = input("Enter your name: ")
```

---

# Important

`input()` **always returns a string**.

Example

```python
age = input("Enter age: ")

print(type(age))
```

Output

```
<class 'str'>
```

---

To convert into an integer

```python
age = int(input("Enter age: "))
```

---

# Why Does input() Return a String?

Because everything typed from the keyboard is initially treated as text.

You decide how to convert it.

---

# Python Interactive Shell (REPL)

REPL stands for

```
Read

Evaluate

Print

Loop
```

When you type

```bash
python
```

Python starts the interactive shell.

Example

```python
>>> 10 + 20

30
```

Useful for

- Quick testing
- Learning
- Debugging

---

# 🧘 Zen of Python

Run

```python
import this
```

You'll see

```
Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Readability counts.
```

These principles guide Python's design philosophy.

---

# 📏 PEP 8 Style Guide

PEP 8 is the official Python style guide.

## Use snake_case

```python
student_name
```

---

## Classes

```python
class Student:
```

---

## Constants

```python
MAX_SIZE = 100
```

---

## Indentation

Use **4 spaces**.

Never mix tabs and spaces.

---

## Line Length

Recommended

```
79 characters
```

---

## Blank Lines

Use blank lines to separate functions and classes.

---

# ⚠️ Common Beginner Mistakes

❌

```python
print = 10
```

Now `print()` no longer works.

---

❌

```python
list = [1,2,3]
```

Avoid using built-in names.

---

❌

```python
input = "Python"
```

Never overwrite built-in functions.

---

❌

```python
age = input()

print(age + 10)
```

Output

```
TypeError
```

Correct

```python
age = int(input())

print(age + 10)
```

---

# 💡 Best Practices

✅ Follow PEP 8.

✅ Use meaningful variable names.

✅ Keep functions short.

✅ Write comments only when necessary.

✅ Prefer docstrings for functions.

✅ Never overwrite built-in functions.

✅ Use virtual environments for projects.

---

# 💼 Interview Questions

### Why does `input()` return a string?

---

### Difference between comments and docstrings?

---

### What does `sep` do?

---

### What does `end` do?

---

### Does `print()` return anything?

---

### What is REPL?

---

### What is PEP 8?

---

### Difference between keywords and identifiers?

---

### What are built-in functions?

---

### Why should we avoid using built-in names?

---

# 📌 Quick Revision

✔ Keywords are reserved words.

✔ Identifiers are user-defined names.

✔ Follow snake_case for variables and functions.

✔ Use PascalCase for classes.

✔ `print()` returns `None`.

✔ `input()` always returns a string.

✔ `sep` changes the separator.

✔ `end` changes the line ending.

✔ `flush=True` forces immediate output.

✔ REPL stands for Read-Evaluate-Print-Loop.

✔ `import this` displays the Zen of Python.

✔ Follow PEP 8 coding standards.

---

# 📝 Practice Questions

### Theory

1. What is a keyword?
2. What is an identifier?
3. Why can't keywords be used as variable names?
4. Explain `sep` and `end`.
5. Why does `input()` return a string?
6. What is REPL?
7. What is PEP 8?
8. What are docstrings?
9. What is the Zen of Python?
10. Why should built-in function names not be overwritten?

---

### Coding

1. Print three values separated by `-`.
2. Print numbers from 1 to 5 on the same line.
3. Write a function with a proper docstring.
4. Take age as input and print age after adding 5.
5. Display all Python keywords.
6. Check whether `"while"` is a keyword.
7. Print today's date using the `datetime` module.
8. Create valid and invalid identifiers.
9. Demonstrate the `sep` parameter.
10. Demonstrate the `end` parameter.

---

# 🎉 Congratulations!

You have now completed **Python Basics**.

In the next chapter (**02_Variables.md**), we'll go much deeper into:

- Variable assignment
- Multiple assignment
- Object references
- Memory addresses (`id()`)
- Mutable vs Immutable
- Reference counting
- Garbage collection
- Variable aliasing
- Interning
- Identity (`is`) vs Equality (`==`)
- Common interview questions
- CPython internals
- Time complexity where applicable