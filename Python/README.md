# 🐍 Python Notes

> A beginner-friendly collection of Python fundamentals with explanations, examples, and best practices.

---

# 📚 Table of Contents

1. Introduction to Python
2. Why Learn Python?
3. Features of Python
4. Dynamic Typing
5. Interpreted Language
6. Python Scope
7. Lists vs Tuples
8. Variable Naming Rules
9. Expressions vs Statements
10. Augmented Assignment Operators

---

# 1️⃣ Introduction to Python

Python is a **high-level**, **interpreted**, **general-purpose** programming language created by **Guido van Rossum** and released in **1991**.

Python is one of the most popular programming languages because it has simple syntax and is easy to read.

It is widely used for:

- Web Development
- Artificial Intelligence
- Machine Learning
- Data Science
- Automation
- Game Development
- Desktop Applications
- Cyber Security
- Scripting

---

# 2️⃣ Why Learn Python?

Python is beginner-friendly and powerful enough for professional software development.

## Advantages

- Easy to learn
- Easy to read
- Huge community
- Free & Open Source
- Cross-platform
- Large Standard Library
- Supports Object-Oriented Programming
- Excellent for AI & Machine Learning
- Huge number of third-party libraries

---

# 3️⃣ Features of Python

- High-Level Language
- Interpreted Language
- Dynamically Typed
- Object-Oriented
- Platform Independent
- Extensive Libraries
- Automatic Memory Management

---

# 4️⃣ Dynamically Typed Language

Python does **not** require you to declare variable types.

Example:

```python
x = 10

x = "Python"

print(x)
```

Output

```
Python
```

The variable changes from **integer** to **string** automatically.

---

# 5️⃣ Interpreted Language

Python executes code **line by line**.

Unlike C or C++, Python does not need compilation before execution.

Example

```python
print("Hello")

print("World")
```

Python executes the first statement and then moves to the next.

Advantages

- Easier debugging
- Faster development
- Better portability

---

# 6️⃣ Scope in Python

Scope determines where a variable is accessible.

Python follows the **LEGB Rule**

## Local Scope

Variables declared inside a function.

```python
def greet():
    name = "Nitin"
    print(name)

greet()
```

---

## Enclosing Scope

Variables inside nested functions.

```python
def outer():

    msg = "Hello"

    def inner():
        print(msg)

    inner()

outer()
```

---

## Global Scope

Variables declared outside all functions.

```python
name = "Python"

def show():
    print(name)

show()
```

---

## Built-in Scope

Python's built-in names.

```python
print(len("Python"))
```

---

# 7️⃣ List vs Tuple

## List

- Mutable
- Uses []
- Slower
- More memory

```python
numbers = [1,2,3]

numbers.append(4)
```

---

## Tuple

- Immutable
- Uses ()
- Faster
- Less memory

```python
numbers = (1,2,3)
```

---

## Difference

| List        | Tuple       |
| ----------- | ----------- |
| Mutable     | Immutable   |
| []          | ()          |
| Slower      | Faster      |
| More Memory | Less Memory |

---

# 8️⃣ Variable Naming Rules

Python follows some naming conventions.

## Rules

✔ Use snake_case

```python
student_name
```

✔ Start with lowercase or underscore

```python
age

_count
```

✔ Can contain

- Letters
- Numbers
- Underscores

```python
student1

marks_2025
```

✔ Cannot start with a number

❌

```python
1name
```

✔ Case Sensitive

```python
age

Age

AGE
```

All three are different variables.

✔ Don't use Python keywords

❌

```python
if

for

while

class
```

✔ Use meaningful names

Good

```python
student_name

total_marks

employee_salary
```

Bad

```python
a

x

temp
```

---

# 9️⃣ Expressions vs Statements

## Expression

An expression produces a value.

Examples

```python
10 + 20

len("Python")

age >= 18

5 * 10
```

Expressions can be assigned.

```python
result = 10 + 20
```

---

## Statement

A statement performs an action.

Examples

```python
if age >= 18:
    print("Adult")
```

```python
for i in range(5):
    print(i)
```

```python
def greet():
    print("Hello")
```

---

## Difference

| Expression                     | Statement          |
| ------------------------------ | ------------------ |
| Produces a value               | Performs an action |
| Can be assigned                | Controls execution |
| Used inside another expression | Usually cannot     |

---

# 🔟 Augmented Assignment Operators

Instead of writing

```python
x = x + 5
```

We can write

```python
x += 5
```

## Operators

| Operator | Example   |
| -------- | --------- |
| +=       | x += 5    |
| -=       | x -= 5    |
| \*=      | x \*= 5   |
| /=       | x /= 5    |
| //=      | x //= 5   |
| %=       | x %= 5    |
| \*\*=    | x \*\*= 2 |

Example

```python
count = 0

count += 1

count += 1

print(count)
```

Output

```
2
```

---

# ✅ Quick Revision

- Python is interpreted.
- Python is dynamically typed.
- Python follows LEGB scope.
- Lists are mutable.
- Tuples are immutable.
- Expressions produce values.
- Statements perform actions.
- Augmented operators make code cleaner.

---

➡ Continue to **Part 2** (Strings, Escape Sequences, Formatted Strings)

# 1️⃣1️⃣ Strings

A **string** is a sequence of characters enclosed in quotes. Strings are used to store text such as names, messages, addresses, passwords, and more.

Python provides three ways to create strings:

## Single Quotes

```python
name = 'Nitin'
```

---

## Double Quotes

```python
city = "Bangalore"
```

---

## Triple Quotes (Multi-line Strings)

```python
message = """
Welcome to Python.
This is a multi-line string.
"""
```

Triple quotes are useful for:

- Multi-line text
- SQL Queries
- Documentation (Docstrings)
- HTML Templates

---

# String Indexing

Every character in a string has an index.

```python
text = "Python"
```

| Character | P   | y   | t   | h   | o   | n   |
| --------- | --- | --- | --- | --- | --- | --- |
| Index     | 0   | 1   | 2   | 3   | 4   | 5   |

Examples

```python
text[0]
```

Output

```
P
```

```python
text[3]
```

Output

```
h
```

---

# Negative Indexing

Negative indexing starts from the end.

| Character | P   | y   | t   | h   | o   | n   |
| --------- | --- | --- | --- | --- | --- | --- |
| Index     | -6  | -5  | -4  | -3  | -2  | -1  |

Example

```python
text[-1]
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
text = "Python"
```

```python
text[0:3]
```

Output

```
Pyt
```

---

```python
text[2:6]
```

Output

```
thon
```

---

```python
text[:4]
```

Output

```
Pyth
```

---

```python
text[2:]
```

Output

```
thon
```

---

```python
text[:]
```

Output

```
Python
```

---

```python
text[::2]
```

Output

```
Pto
```

---

```python
text[::-1]
```

Output

```
nohtyP
```

This is a common way to reverse a string.

---

# String Concatenation

Joining two or more strings using the `+` operator.

```python
first = "Hello"

second = "World"

result = first + " " + second

print(result)
```

Output

```
Hello World
```

---

# String Repetition

Use the `*` operator.

```python
text = "Hi "

print(text * 3)
```

Output

```
Hi Hi Hi
```

---

# Membership Operators

```python
text = "Python"
```

```python
"Py" in text
```

Output

```
True
```

---

```python
"Java" in text
```

Output

```
False
```

---

```python
"Java" not in text
```

Output

```
True
```

---

# Strings are Immutable

Strings **cannot be modified** after creation.

Incorrect

```python
text = "Python"

text[0] = "J"
```

Output

```
TypeError
```

Correct

```python
text = "J" + text[1:]
```

Output

```
Jython
```

---

# Common String Methods

### upper()

```python
text.upper()
```

Output

```
PYTHON
```

---

### lower()

```python
text.lower()
```

Output

```
python
```

---

### title()

```python
text.title()
```

Output

```
Python Programming
```

---

### capitalize()

```python
text.capitalize()
```

Output

```
Python
```

---

### strip()

Removes leading and trailing spaces.

```python
text.strip()
```

---

### replace()

```python
text.replace("Python", "Java")
```

---

### split()

```python
text.split()
```

Output

```
['Python', 'Programming']
```

---

### join()

```python
"-".join(["a","b","c"])
```

Output

```
a-b-c
```

---

### startswith()

```python
text.startswith("Py")
```

Output

```
True
```

---

### endswith()

```python
text.endswith("on")
```

Output

```
True
```

---

### find()

```python
text.find("Pro")
```

Returns the first occurrence index.

---

### count()

```python
text.count("a")
```

Counts occurrences.

---

# 1️⃣2️⃣ Escape Sequences

Escape sequences begin with a backslash (`\`) and allow special formatting inside strings.

## Common Escape Sequences

| Escape Sequence | Description     |
| --------------- | --------------- |
| \n              | New Line        |
| \t              | Horizontal Tab  |
| \\              | Backslash       |
| \'              | Single Quote    |
| \"              | Double Quote    |
| \b              | Backspace       |
| \r              | Carriage Return |

---

## New Line

```python
print("Hello\nWorld")
```

Output

```
Hello
World
```

---

## Tab

```python
print("Name\tAge")
```

Output

```
Name    Age
```

---

## Backslash

```python
print("C:\\Users\\Nitin")
```

Output

```
C:\Users\Nitin
```

---

## Single Quote

```python
print('It\\'s raining')
```

Output

```
It's raining
```

---

## Double Quote

```python
print("He said, \\"Python\\"")
```

Output

```
He said, "Python"
```

---

## Backspace

```python
print("Helloo\\b")
```

Output

```
Hello
```

---

## Carriage Return

```python
print("12345\\rABC")
```

Output

```
ABC45
```

---

# Why Use Escape Sequences?

They help us

- Print multiple lines
- Add tabs
- Display quotes
- Show file paths correctly
- Improve output formatting

---

# 1️⃣3️⃣ Formatted Strings

Formatted strings allow variables and expressions to be inserted directly inside a string.

Python provides three methods.

- f-Strings ✅ (Recommended)
- format()
- % Formatting (Old)

---

# f-Strings (Recommended)

```python
name = "Nitin"

age = 23

print(f"My name is {name} and I am {age} years old.")
```

Output

```
My name is Nitin and I am 23 years old.
```

---

# Expressions inside f-Strings

```python
x = 10

y = 20

print(f"Sum = {x + y}")
```

Output

```
Sum = 30
```

---

```python
price = 100

quantity = 3

print(f"Total = {price * quantity}")
```

Output

```
Total = 300
```

---

# format() Method

```python
print("Hello {}".format(name))
```

---

Named Arguments

```python
print("Name: {n}, Age: {a}".format(n="Nitin", a=23))
```

---

# % Formatting

```python
print("My name is %s" % name)
```

Common specifiers

| Specifier | Meaning |
| --------- | ------- |
| %s        | String  |
| %d        | Integer |
| %f        | Float   |

---

# Formatting Numbers

```python
pi = 3.14159265

print(f"{pi:.2f}")
```

Output

```
3.14
```

---

```python
price = 99.999

print(f"{price:.1f}")
```

Output

```
100.0
```

---

# Width Formatting

```python
num = 42

print(f"{num:5}")
```

Output

```
   42
```

---

```python
print(f"{num:05}")
```

Output

```
00042
```

---

# Text Alignment

Left

```python
print(f"{'Python':<10}")
```

Right

```python
print(f"{'Python':>10}")
```

Center

```python
print(f"{'Python':^10}")
```

---

# Why Prefer f-Strings?

- Easier to read
- Faster
- Cleaner syntax
- Supports expressions
- Recommended in Python 3.6+

---

# 💡 Interview Tips

✔ Strings are immutable.

✔ Python uses zero-based indexing.

✔ `[::-1]` reverses a string.

✔ `split()` converts a string to a list.

✔ `join()` converts a list to a string.

✔ Prefer f-strings over `%` formatting.

---

# ✅ Quick Revision

- Strings store text.
- Strings are immutable.
- Indexing starts from `0`.
- Negative indexing starts from `-1`.
- Slicing extracts part of a string.
- `upper()`, `lower()`, `replace()`, and `split()` are commonly used methods.
- Escape sequences improve string formatting.
- f-strings are the recommended way to format strings.

---

➡ Continue to **Part 3** (Built-in Functions, Methods, Function vs Method, Summary, and Next Topics)

# 1️⃣4️⃣ Built-in Functions

Python provides many **built-in functions** that can be used directly without importing any modules.

Syntax:

```python
function_name(arguments)
```

Example:

```python
print("Hello, World!")
```

Output

```
Hello, World!
```

---

# Common Built-in Functions

## 1. print()

Displays output on the screen.

```python
print("Hello, Python!")
```

---

## 2. input()

Takes input from the user.

```python
name = input("Enter your name: ")
print(name)
```

---

## 3. len()

Returns the length of an object.

```python
text = "Python"

print(len(text))
```

Output

```
6
```

---

## 4. type()

Returns the data type of an object.

```python
x = 10

print(type(x))
```

Output

```
<class 'int'>
```

---

## 5. int()

Converts a value to an integer.

```python
num = int("25")

print(num)
```

Output

```
25
```

---

## 6. float()

Converts a value to a floating-point number.

```python
price = float("99.5")

print(price)
```

Output

```
99.5
```

---

## 7. str()

Converts a value into a string.

```python
age = 23

print(str(age))
```

Output

```
23
```

---

## 8. bool()

Converts a value into Boolean.

```python
print(bool(1))
print(bool(0))
```

Output

```
True
False
```

---

## 9. max()

Returns the largest value.

```python
print(max(10, 50, 30))
```

Output

```
50
```

---

## 10. min()

Returns the smallest value.

```python
print(min(10, 50, 30))
```

Output

```
10
```

---

## 11. sum()

Returns the sum of all elements.

```python
numbers = [10, 20, 30]

print(sum(numbers))
```

Output

```
60
```

---

## 12. abs()

Returns the absolute value.

```python
print(abs(-25))
```

Output

```
25
```

---

## 13. round()

Rounds a number.

```python
print(round(3.14159, 2))
```

Output

```
3.14
```

---

## 14. sorted()

Returns a sorted list.

```python
numbers = [4, 2, 1, 5]

print(sorted(numbers))
```

Output

```
[1, 2, 4, 5]
```

---

## 15. range()

Generates a sequence of numbers.

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

## 16. enumerate()

Returns both the index and value while iterating.

```python
fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output

```
0 Apple
1 Banana
2 Mango
```

---

## 17. zip()

Combines multiple iterables.

```python
names = ["Nitin", "Rahul"]
marks = [90, 85]

print(list(zip(names, marks)))
```

Output

```
[('Nitin', 90), ('Rahul', 85)]
```

---

# 1️⃣5️⃣ Methods in Python

A **method** is a function that belongs to an object.

Methods are called using **dot notation**.

Syntax

```python
object.method()
```

Example

```python
text = "python"

print(text.upper())
```

Output

```
PYTHON
```

---

# Common String Methods

## upper()

```python
text.upper()
```

Output

```
PYTHON
```

---

## lower()

```python
text.lower()
```

Output

```
python
```

---

## title()

```python
text.title()
```

Output

```
Python Programming
```

---

## capitalize()

```python
text.capitalize()
```

Output

```
Python
```

---

## strip()

Removes leading and trailing spaces.

```python
text.strip()
```

---

## replace()

```python
text.replace("Java", "Python")
```

---

## split()

Splits a string into a list.

```python
text.split()
```

---

## join()

Joins list elements into a string.

```python
languages = ["Python", "Java", "C++"]

print(", ".join(languages))
```

Output

```
Python, Java, C++
```

---

## startswith()

```python
text.startswith("Py")
```

Output

```
True
```

---

## endswith()

```python
text.endswith("on")
```

Output

```
True
```

---

## find()

Returns the first occurrence index.

```python
text.find("Pro")
```

---

## count()

Returns the number of occurrences.

```python
text.count("a")
```

---

# Function vs Method

| Built-in Function           | Method               |
| --------------------------- | -------------------- |
| Called directly             | Called on an object  |
| `len(text)`                 | `text.upper()`       |
| Doesn't belong to an object | Belongs to an object |
| General-purpose             | Object-specific      |

---

# 💡 Best Practices

- Use meaningful variable names.
- Follow **snake_case** naming convention.
- Prefer **f-strings** over older formatting styles.
- Keep your code simple and readable.
- Avoid hardcoding values whenever possible.
- Write comments where necessary.
- Follow PEP 8 style guidelines.
- Practice coding regularly to improve problem-solving skills.

---

# 📝 Interview Tips

- Python is **interpreted**, **high-level**, and **dynamically typed**.
- Strings are **immutable**.
- Lists are **mutable**, tuples are **immutable**.
- Indexing starts from **0**.
- Negative indexing starts from **-1**.
- Use `len()` to find the length of an object.
- Prefer `sorted()` over manually sorting lists.
- `zip()` is commonly used to iterate over multiple lists.
- Methods are called using dot (`.`) notation.

---

# 📚 Quick Revision

✅ Python Basics

✅ Variables

✅ Expressions

✅ Statements

✅ Augmented Assignment Operators

✅ Strings

✅ String Indexing

✅ String Slicing

✅ Escape Sequences

✅ Formatted Strings

✅ Built-in Functions

✅ Methods

---

# 🚀 What's Next?

Continue learning the following topics:

- Data Types
- Operators
- Conditional Statements (`if`, `elif`, `else`)
- Loops (`for`, `while`)
- Functions
- Lists
- Tuples
- Sets
- Dictionaries
- File Handling
- Exception Handling
- Modules & Packages
- Object-Oriented Programming (OOP)
- Iterators & Generators
- Decorators
- Lambda Functions
- List Comprehensions
- Virtual Environments
- Popular Python Libraries

---

# 📖 Learning Resources

- Python Official Documentation: https://docs.python.org/3/
- W3Schools Python Tutorial: https://www.w3schools.com/python/
- GeeksforGeeks Python: https://www.geeksforgeeks.org/python-programming-language/
- Real Python: https://realpython.com/

---

# 📌 About This Repository

This repository is part of my **Learning Journey**, where I document my Python concepts, notes, code examples, and practice problems.

The goal is to build a strong foundation in Python while maintaining organized and easy-to-understand documentation.

If you find these notes useful, feel free to ⭐ this repository.

---

## 👨‍💻 Happy Coding! 🚀
