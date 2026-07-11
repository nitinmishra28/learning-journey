---

# ⚙️ How Python Executes Your Code

Many beginners think Python directly executes `.py` files. That's **not entirely true**.

When you run a Python program, several steps happen behind the scenes before your code executes.

```
Python Source Code (.py)

        │
        ▼

      Lexical Analysis (Lexer)

        │
        ▼

        Parser

        │
        ▼

 Abstract Syntax Tree (AST)

        │
        ▼

      Bytecode Compilation

        │
        ▼

      Bytecode (.pyc)

        │
        ▼

Python Virtual Machine (PVM)

        │
        ▼

 Machine Instructions

        │
        ▼

 Program Output
```

Let's understand every stage.

---

# Step 1️⃣ Source Code

This is the code you write.

Example

```python
x = 10

print(x)
```

The file is saved as

```
program.py
```

---

# Step 2️⃣ Lexical Analysis (Lexer)

The **Lexer** reads your source code character by character.

Its job is to convert code into **tokens**.

## What is a Token?

A token is the smallest meaningful unit of a program.

Example

```python
x = 10
```

Tokens

```
Identifier -> x

Operator -> =

Number -> 10
```

Another example

```python
print("Hello")
```

Tokens

```
Identifier -> print

(

String -> Hello

)
```

---

### Why is Lexical Analysis Needed?

Because computers don't understand Python syntax directly.

They first break the program into small pieces.

---

# Step 3️⃣ Parsing

After tokenization,

Python checks whether the tokens follow Python grammar.

Example

Correct

```python
x = 10
```

Wrong

```python
= x 10
```

Parser Error

```
SyntaxError
```

The parser ensures your program follows Python syntax.

---

# Step 4️⃣ Abstract Syntax Tree (AST)

After parsing,

Python creates something called an **Abstract Syntax Tree**.

It represents the structure of your program.

Example

```python
x = 10 + 20
```

AST

```
Assignment

│

├── Variable (x)

│

└── Addition

     ├──10

     └──20
```

The AST is easier for Python to analyze and optimize.

---

# Step 5️⃣ Compilation to Bytecode

Now Python converts the AST into **Bytecode**.

## What is Bytecode?

Bytecode is an intermediate language.

It is **not machine code**.

It is also **not Python code**.

Think of it as a language that only Python understands.

---

Example

Python Code

```python
print("Hello")
```

gets converted into Bytecode.

The bytecode instructions are much lower level than Python.

---

# Step 6️⃣ .pyc Files

Python stores compiled bytecode inside

```
__pycache__/
```

Example

```
program.py

↓

program.cpython-313.pyc
```

These files help Python execute programs faster next time.

---

### Does Python Always Create .pyc Files?

No.

Usually only imported modules are cached.

Simple scripts may not create them.

---

# Step 7️⃣ Python Virtual Machine (PVM)

The **Python Virtual Machine** executes bytecode.

Think of it like a CPU specifically designed for Python bytecode.

```
Python Code

↓

Bytecode

↓

PVM

↓

Machine Code

↓

Output
```

---

# What Does PVM Do?

- Reads bytecode
- Executes instructions
- Allocates memory
- Calls built-in functions
- Handles exceptions

---

# Why Doesn't Python Generate Machine Code Directly?

Because Python is designed to be portable.

Instead of generating machine code,

Python generates bytecode.

Only the PVM depends on the operating system.

This is why the same Python code works on Windows, Linux, and macOS.

---

# Bytecode is Platform Independent

```
Windows

↓

CPython

↓

Same Bytecode

↑

Linux

↑

macOS
```

Only the interpreter changes.

---

# Is Python Really Interpreted?

This is a common interview question.

Many people answer:

> Python is interpreted.

This is **partially correct**.

The actual process is:

```
Python Source Code

↓

Compiled to Bytecode

↓

Interpreted by Python Virtual Machine
```

So Python is **both compiled and interpreted**.

- Compiled into **bytecode**
- Interpreted by the **Python Virtual Machine**

---

# CPython

The default Python implementation is **CPython**.

It is written in the **C programming language**.

CPython

```
Python Code

↓

Bytecode

↓

PVM (Written in C)

↓

Machine Instructions
```

---

# Other Python Implementations

| Implementation | Written In | Special Feature |
|---------------|------------|-----------------|
| CPython | C | Official implementation |
| PyPy | Python + C | Faster due to JIT |
| Jython | Java | Runs on JVM |
| IronPython | C# | Runs on .NET |
| MicroPython | C | Embedded devices |

---

# What is JIT?

JIT stands for

```
Just-In-Time Compiler
```

Used by **PyPy**.

Instead of interpreting bytecode repeatedly,

JIT converts frequently executed bytecode into machine code.

Result

✅ Faster execution

---

# Bytecode Inspection

Python provides a module called

```python
dis
```

Example

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

Output

```
LOAD_FAST

LOAD_FAST

BINARY_ADD

RETURN_VALUE
```

This lets you see the actual bytecode instructions.

Very useful during interviews.

---

# Why Learn This?

Understanding Python execution helps you

- Debug better
- Write efficient code
- Understand performance
- Crack interviews
- Learn CPython internals

---

# Common Mistakes

❌ Thinking Python directly executes source code.

❌ Thinking Python never compiles code.

❌ Confusing bytecode with machine code.

❌ Assuming .pyc files always exist.

---

# Interview Questions

### Does Python compile code?

✅ Yes.

Python first compiles source code into bytecode.

---

### Is Python interpreted?

✅ Yes.

The bytecode is interpreted by the Python Virtual Machine.

---

### What is Bytecode?

An intermediate representation of Python code executed by the PVM.

---

### What is PVM?

Python Virtual Machine.

It executes Python bytecode.

---

### What are .pyc files?

Compiled bytecode files stored inside

```
__pycache__
```

---

### Which Python implementation is official?

CPython.

---

### Which Python implementation is fastest?

Generally **PyPy** for long-running pure Python code because of JIT compilation.

---

# 🧠 DSA Tip

You don't need to memorize bytecode instructions.

Instead, understand:

- Why Python is slower than C++
- Why PyPy is often used in competitive programming
- Why CPython is the standard interpreter
- Why bytecode makes Python portable

This knowledge is useful in interviews and helps you make informed choices when writing performance-sensitive code.

---

# 📌 Quick Revision

- Source code is tokenized by the Lexer.
- Tokens are validated by the Parser.
- Python builds an AST.
- AST is compiled into Bytecode.
- Bytecode is executed by the Python Virtual Machine.
- `.pyc` files store compiled bytecode.
- CPython is the official implementation.
- PyPy uses JIT compilation for better performance.
- Python is compiled to bytecode and then interpreted.