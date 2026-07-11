---

# 🌍 Variable Scope

A variable's **scope** determines **where it can be accessed** within a program.

Python provides four scopes:

- Local Scope
- Enclosing Scope
- Global Scope
- Built-in Scope

Together, they form the **LEGB Rule**.

---

# Local Scope

A variable created inside a function is called a **local variable**.

Example

```python
def greet():
    message = "Hello"
    print(message)

greet()
```

Output

```
Hello
```

Trying to access it outside the function

```python
print(message)
```

Output

```
NameError: name 'message' is not defined
```

---

# Global Scope

Variables declared outside every function belong to the **global scope**.

Example

```python
language = "Python"

def display():
    print(language)

display()
```

Output

```
Python
```

Global variables can be **read** inside functions.

---

# Modifying Global Variables

Reading a global variable is allowed.

```python
count = 10

def show():
    print(count)

show()
```

Output

```
10
```

But modifying it directly causes an error.

```python
count = 10

def increase():
    count += 1

increase()
```

Output

```
UnboundLocalError
```

Why?

Python assumes `count` is a new local variable because it is being assigned inside the function.

---

# global Keyword

Use the `global` keyword when you want to modify a global variable.

```python
count = 10

def increase():
    global count
    count += 1

increase()

print(count)
```

Output

```
11
```

### Best Practice

Use `global` sparingly.

Excessive use of global variables makes code difficult to maintain and test.

---

# Enclosing Scope

Occurs when a function is defined inside another function.

Example

```python
def outer():
    x = "Outer"

    def inner():
        print(x)

    inner()

outer()
```

Output

```
Outer
```

Here,

`x` belongs to the enclosing function.

---

# nonlocal Keyword

`nonlocal` allows modifying variables from the enclosing scope.

Example

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(count)

    inner()

outer()
```

Output

```
1
```

Without `nonlocal`, Python would create a new local variable.

---

# Built-in Scope

Python searches built-in names last.

Example

```python
print(len("Python"))
```

`len()` comes from Python's built-in namespace.

---

# LEGB Rule

When Python encounters a variable, it searches in this order:

```
Local

↓

Enclosing

↓

Global

↓

Built-in
```

Example

```python
x = "Global"

def outer():
    x = "Outer"

    def inner():
        x = "Inner"
        print(x)

    inner()

outer()
```

Output

```
Inner
```

Python finds `x` in the **Local** scope first.

---

# Namespace

A **namespace** is a mapping between names and objects.

Think of it as a Python dictionary:

```
Variable Name

↓

Object
```

Python maintains different namespaces:

- Built-in Namespace
- Global Namespace
- Local Namespace

---

## Viewing Global Namespace

```python
print(globals())
```

Returns a dictionary of global variables.

---

## Viewing Local Namespace

```python
def demo():
    a = 10
    print(locals())

demo()
```

Output

```
{'a': 10}
```

---

# Variable Shadowing

A local variable can hide a global variable with the same name.

Example

```python
name = "Global"

def show():
    name = "Local"
    print(name)

show()

print(name)
```

Output

```
Local

Global
```

The local variable **shadows** the global variable.

---

# Object Lifetime

Objects live as long as they have references.

Example

```python
x = [1,2,3]
```

The list exists because `x` references it.

When

```python
del x
```

the reference is removed.

If no references remain, the object becomes eligible for garbage collection.

---

# Reference Counting

CPython uses **reference counting** to manage memory.

Example

```python
import sys

x = []

print(sys.getrefcount(x))
```

> **Note:** `getrefcount()` temporarily adds one extra reference while executing, so the reported count is usually one higher than expected.

Every new reference increases the count.

Removing references decreases it.

---

# del Statement

`del` removes a **name (reference)**, not necessarily the object.

Example

```python
x = [1,2]

y = x

del x

print(y)
```

Output

```
[1,2]
```

The list still exists because `y` references it.

---

# String Interning

Python may reuse immutable string objects.

Example

```python
a = "Python"

b = "Python"

print(a is b)
```

Often

```
True
```

Python may point both names to the same string object.

> **Important:** This is an optimization and should not be relied upon for program logic.

---

# Small Integer Caching

CPython caches small integers (typically `-5` to `256`).

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

For larger integers, behavior may differ depending on the implementation.

Again, never rely on this optimization in your code.

---

# Memory Optimization

Python reuses immutable objects whenever possible.

Benefits

- Faster execution
- Reduced memory usage
- Efficient object sharing

---

# Common Mistakes

## Mistake 1

```python
def test():
    x += 1
```

Output

```
UnboundLocalError
```

Python thinks `x` is local because of the assignment.

---

## Mistake 2

Overusing `global`.

Global variables make debugging difficult.

Prefer passing values as function parameters.

---

## Mistake 3

Using `is` to compare strings or numbers.

```python
a = 1000
b = 1000

print(a is b)
```

Do **not** rely on the result.

Use

```python
a == b
```

for value comparison.

---

# DSA Tips

✅ Prefer local variables inside functions.

Local variable lookup is generally faster than global lookup because Python checks the local namespace first.

---

✅ Avoid global state in algorithms.

Pass data as function parameters to make code reusable and easier to test.

---

✅ Understand aliasing before working with lists, dictionaries, and graphs.

---

# Best Practices

- Keep variable scope as small as possible.
- Avoid unnecessary global variables.
- Use `nonlocal` only when appropriate.
- Use descriptive variable names.
- Prefer function parameters over global state.

---

# Interview Questions

1. What is variable scope?
2. Explain the LEGB Rule.
3. Difference between `global` and `nonlocal`?
4. What is a namespace?
5. What does `locals()` return?
6. What does `globals()` return?
7. What does `del` actually delete?
8. What is reference counting?
9. What is string interning?
10. Why does Python cache small integers?

---

# Quick Revision

✔ Python follows the LEGB Rule.

✔ Local variables exist only inside functions.

✔ Global variables are accessible throughout the module.

✔ `global` modifies global variables.

✔ `nonlocal` modifies enclosing-scope variables.

✔ Namespaces map names to objects.

✔ `locals()` returns the local namespace.

✔ `globals()` returns the global namespace.

✔ `del` removes references, not necessarily objects.

✔ CPython uses reference counting for memory management.

✔ Python interns many string literals.

✔ CPython caches small integers (typically `-5` to `256`).

---

# Practice Questions

## Theory

1. Explain the LEGB Rule with an example.
2. What is the difference between `global` and `nonlocal`?
3. What is variable shadowing?
4. What is a namespace?
5. What does `del` do?
6. Explain reference counting.
7. What is string interning?
8. Why does CPython cache small integers?
9. What is object lifetime?
10. Why are local variables generally preferred?

---

## Coding

1. Demonstrate local and global variables.
2. Modify a global variable using `global`.
3. Modify an enclosing variable using `nonlocal`.
4. Print `globals()` and `locals()`.
5. Demonstrate variable shadowing.
6. Show that `del` removes a reference.
7. Use `sys.getrefcount()` to inspect reference counts.
8. Explore string interning using `is`.
9. Explore small integer caching.
10. Write nested functions using the LEGB rule.

---

# 🎉 Congratulations!

You have completed **Variables in Python**.

In the next chapter (**05_Input_Output.md**) we'll cover:

- `print()` in depth
- `input()`
- Formatted output
- f-Strings
- `%` formatting
- `str.format()`
- File output
- Escape sequences
- Unicode
- Encoding
- Interview Questions
- DSA Tips