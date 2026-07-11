# 🐍 Python Basics

> Learn the fundamentals of Python programming, understand why Python is one of the world's most popular programming languages, and build a strong foundation before diving into Data Structures & Algorithms.

---

# 📚 Table of Contents

- Introduction
- What is Python?
- History of Python
- Why Learn Python?
- Features of Python
- Applications of Python
- Installing Python
- Running Your First Python Program
- Python Versions
- Python Interpreter
- CPython, PyPy & Other Implementations
- Best Practices
- Common Mistakes
- Interview Questions
- Quick Revision
- Practice Questions

---

# 📖 Introduction

Python is one of the most popular programming languages in the world. It is known for its **simple syntax**, **readability**, and **versatility**.

Whether you're building:

- Websites
- Artificial Intelligence applications
- Machine Learning models
- Automation scripts
- APIs
- Desktop applications
- Games

Python can do it all.

One of Python's biggest strengths is that it allows developers to focus on solving problems rather than worrying about complicated syntax.

---

# 🤔 What is Python?

Python is a **high-level**, **interpreted**, **general-purpose**, and **object-oriented** programming language created by **Guido van Rossum**.

It was first released on **20 February 1991**.

Python emphasizes:

- Readability
- Simplicity
- Productivity

Its syntax is designed to resemble plain English, making it easier for beginners to learn.

---

# 📜 History of Python

Python was created by **Guido van Rossum** while working at CWI (Centrum Wiskunde & Informatica) in the Netherlands.

The name **Python** does **not** come from the snake.

It was inspired by the British comedy show:

> **Monty Python's Flying Circus**

Python has evolved significantly over the years.

| Version | Release |
|---------|----------|
| Python 1.0 | 1994 |
| Python 2.0 | 2000 |
| Python 3.0 | 2008 |
| Python 3.x | Current |

Today, Python is maintained by the **Python Software Foundation (PSF)**.

---

# 🎯 Why Learn Python?

Python is one of the best programming languages for beginners and professionals alike.

## Advantages

✅ Easy to Learn

Python has clean and readable syntax.

Example:

```python
print("Hello World")
```

Compared to many other languages, Python requires fewer lines of code.

---

✅ Huge Community

Python has one of the largest developer communities.

If you get stuck, there are thousands of tutorials, articles, videos, and open-source projects available.

---

✅ Cross Platform

Python works on:

- Windows
- Linux
- macOS

The same Python code usually runs on all three operating systems without modification.

---

✅ Open Source

Python is completely free to use.

You don't need to purchase any license.

---

✅ Large Standard Library

Python comes with many built-in modules for common tasks.

Examples:

```python
import math
import random
import datetime
import os
```

This saves development time because you don't have to build everything from scratch.

---

✅ Huge Ecosystem

Python has thousands of third-party libraries.

Examples:

| Library | Purpose |
|----------|----------|
| NumPy | Numerical Computing |
| Pandas | Data Analysis |
| Matplotlib | Visualization |
| Django | Web Development |
| Flask | APIs |
| FastAPI | High Performance APIs |
| TensorFlow | Machine Learning |
| PyTorch | Deep Learning |

---

# ⭐ Features of Python

## 1. High-Level Language

Python hides low-level details like memory management.

You can focus on solving problems instead of managing memory manually.

---

## 2. Interpreted Language

Python executes code line by line.

Unlike C or C++, Python does not require a separate compilation step before execution.

**Benefits**

- Easier debugging
- Faster development
- Better portability

---

## 3. Dynamically Typed

You don't need to declare variable types.

```python
x = 10

x = "Python"
```

The variable can hold different types of values during execution.

---

## 4. Strongly Typed

Although Python is dynamically typed, it is also **strongly typed**.

Example:

```python
"10" + 20
```

Output

```
TypeError
```

Python does **not** perform implicit conversions between unrelated data types.

---

## 5. Object-Oriented

Everything in Python is an object.

Even integers are objects.

```python
x = 10

print(type(x))
```

Output

```
<class 'int'>
```

---

## 6. Portable

Python programs can run on multiple operating systems with little or no modification.

---

## 7. Automatic Memory Management

Python automatically allocates and frees memory.

Developers don't need to manually allocate or free memory like in C.

Python uses:

- Reference Counting
- Garbage Collector

We'll study this in detail later.

---

## 8. Extensive Standard Library

Python follows the philosophy:

> **"Batteries Included."**

Many useful modules come built-in.

Examples:

```python
math

random

statistics

datetime

collections

heapq

itertools
```

---

# 🌍 Applications of Python

Python is used in almost every area of software development.

## 🌐 Web Development

Popular frameworks:

- Django
- Flask
- FastAPI

---

## 🤖 Artificial Intelligence

Used to build intelligent systems.

Libraries:

- TensorFlow
- PyTorch
- Keras

---

## 📊 Data Science

Libraries:

- NumPy
- Pandas
- Matplotlib
- Seaborn

---

## 📈 Machine Learning

Libraries:

- Scikit-Learn
- TensorFlow
- PyTorch

---

## ⚙ Automation

Python is widely used to automate repetitive tasks.

Examples:

- File automation
- Email automation
- Excel automation
- Browser automation

---

## 🔐 Cyber Security

Python is commonly used for:

- Network scanning
- Penetration testing
- Automation
- Security scripting

---

## 🎮 Game Development

Popular library:

- Pygame

---

## ☁ Backend Development

Modern APIs are often built using:

- FastAPI
- Flask
- Django

---

## 📦 DevOps

Python is widely used for:

- Deployment automation
- Cloud scripting
- Infrastructure management

---

# 💻 Installing Python

Download Python from the official website:

https://www.python.org/downloads/

During installation:

✅ Check

```
Add Python to PATH
```

before clicking **Install**.

---

# ✅ Verify Installation

Open the terminal or command prompt.

```bash
python --version
```

or

```bash
python3 --version
```

Example

```
Python 3.13.5
```

---

# ▶ Your First Python Program

```python
print("Hello, World!")
```

Output

```
Hello, World!
```

Congratulations 🎉

You've written your first Python program.

---

# 🐍 Python Versions

Python currently has two major versions:

- Python 2 (Deprecated)
- Python 3 (Recommended)

Always use **Python 3** for new projects.

---

# ⚙ Python Implementations

Most people use **CPython**, but Python has multiple implementations.

| Implementation | Description |
|---------------|-------------|
| CPython | Official implementation written in C |
| PyPy | Faster implementation using JIT Compiler |
| Jython | Runs on JVM |
| IronPython | Runs on .NET |
| MicroPython | Used on microcontrollers |

### Interview Question

**Which Python implementation is used most commonly?**

✅ **Answer:** CPython

---

# 💡 Best Practices

- Install the latest stable version of Python.
- Use meaningful file names.
- Keep Python updated.
- Learn using the official documentation.
- Practice coding every day.

---

# ⚠ Common Mistakes

❌ Installing Python but forgetting to add it to PATH.

❌ Using Python 2 instead of Python 3.

❌ Naming your file `python.py` or `random.py`, which can conflict with standard library modules.

---

# 💼 Interview Questions

### Q1. Who created Python?

**Answer:** Guido van Rossum

---

### Q2. Is Python compiled or interpreted?

**Answer:** Python is generally considered an interpreted language. CPython first compiles source code to **bytecode**, which is then executed by the Python Virtual Machine (PVM). We'll cover this process in detail in the next part.

---

### Q3. Is Python strongly typed?

**Answer:** Yes.

---

### Q4. Is Python object-oriented?

**Answer:** Yes.

---

### Q5. Which implementation of Python is most commonly used?

**Answer:** CPython

---

# 📝 Quick Revision

- Python is high-level.
- Python is interpreted.
- Python is dynamically typed.
- Python is strongly typed.
- Python is object-oriented.
- Python is cross-platform.
- Python has automatic memory management.
- CPython is the official implementation.

---

# 🎯 Practice Questions

1. Who developed Python?
2. Why is Python called a high-level language?
3. What is the difference between dynamic typing and strong typing?
4. Name five real-world applications of Python.
5. What is the difference between CPython and PyPy?
6. Why is Python called an interpreted language?
7. Which Python implementation is used most often?
8. What are the advantages of Python?
9. Which library would you use for web development?
10. Why should beginners learn Python?

---

## 📚 References

- Official Documentation: https://docs.python.org/3/
- Python Software Foundation: https://www.python.org/
- PEP 8 Style Guide: https://peps.python.org/pep-0008/
