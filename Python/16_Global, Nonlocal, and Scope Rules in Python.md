# Global, Nonlocal, and Scope Rules in Python

Python determines **where a variable can be accessed** using scope.

The most important scope levels are:

```text
Local
Enclosing
Global
Built-in
```

This is commonly remembered as the **LEGB rule**.

---

# 1. Scope

**Scope** is the region of a program where a variable can be accessed.

Example:

```python
x = 10

def test():
    y = 20
    print(x)
    print(y)
```

Here:

```text
x → global scope
y → local scope of test()
```

---

# 2. LEGB Rule

When Python encounters a variable name, it searches for it in this order:

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

### Local

The current function.

### Enclosing

The surrounding function when functions are nested.

### Global

The module/file level.

### Built-in

Names provided by Python itself.

Example:

```python
x = 10

def outer():
    y = 20

    def inner():
        z = 30
        print(z)      # Local
        print(y)      # Enclosing
        print(x)      # Global
        print(len([])) # Built-in
```

Python searches:

```text
z → Local
y → Enclosing
x → Global
len → Built-in
```

---

# 3. Local Scope

A variable created inside a function is normally local to that function.

```python
def greet():
    name = "Nitin"
    print(name)

greet()
```

`name` exists inside `greet()`.

Trying to access it outside:

```python
print(name)
```

results in:

```text
NameError
```

because `name` is not in the global scope.

---

# 4. Global Scope

A variable created outside functions is in the global scope.

```python
name = "Nitin"

def greet():
    print(name)

greet()
```

Output:

```text
Nitin
```

The function can **read** the global variable.

---

# 5. Reading a Global Variable

You do not need the `global` keyword just to read a global variable.

```python
count = 10

def show():
    print(count)

show()
```

This works.

Python searches for `count`:

```text
Local → Enclosing → Global
```

and finds it in the global scope.

---

# 6. Modifying a Global Variable

This is where `global` becomes important.

Consider:

```python
count = 10

def update():
    count = 20

update()

print(count)
```

Output:

```text
10
```

The `count` inside `update()` is a **new local variable**.

It does not modify the global `count`.

---

# 7. `global` Keyword

The `global` keyword tells Python:

> This variable refers to the variable in the global scope.

Example:

```python
count = 10

def update():
    global count
    count = 20

update()

print(count)
```

Output:

```text
20
```

Now:

```python
global count
```

makes the assignment modify the global variable.

---

# 8. Why Does Python Need `global`?

Consider:

```python
count = 10

def update():
    count = count + 1
```

This causes:

```text
UnboundLocalError
```

Why?

Because Python sees:

```python
count = ...
```

inside the function and therefore treats `count` as a **local variable**.

But the right side:

```python
count + 1
```

tries to read that local variable before it has a value.

Using:

```python
global count
```

fixes it:

```python
count = 10

def update():
    global count
    count = count + 1

update()

print(count)
```

Output:

```text
11
```

---

# 9. `nonlocal`

`nonlocal` is used with **nested functions**.

It allows an inner function to modify a variable belonging to its **enclosing function**.

Example:

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1

    inner()
    print(count)

outer()
```

Output:

```text
1
```

Without `nonlocal`:

```python
def outer():
    count = 0

    def inner():
        count += 1

    inner()
```

This causes:

```text
UnboundLocalError
```

because Python treats `count` inside `inner()` as a local variable.

---

# 10. `global` vs `nonlocal`

This is the most important distinction.

### `global`

Used to modify a variable from the **global scope**.

```python
count = 0

def update():
    global count
    count += 1
```

### `nonlocal`

Used to modify a variable from an **enclosing function's scope**.

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
```

Remember:

```text
global
→ goes to module/global scope

nonlocal
→ goes to nearest enclosing function scope
```

---

# 11. `nonlocal` Does Not Mean Global

This is a common mistake.

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()
```

Output:

```text
20
```

`x` is **not global**.

It belongs to `outer()`.

`nonlocal` tells `inner()` to use the `x` from `outer()`.

---

# 12. Nested Functions and Enclosing Scope

Consider:

```python
def outer():
    x = 10

    def inner():
        print(x)

    inner()

outer()
```

Output:

```text
10
```

`inner()` doesn't have a local `x`.

Python searches:

```text
Local → Enclosing → Global → Built-in
```

and finds `x` in the enclosing `outer()` function.

---

# 13. `nonlocal` Uses the Nearest Enclosing Scope

Consider:

```python
def outer():
    x = "outer"

    def middle():
        x = "middle"

        def inner():
            nonlocal x
            x = "changed"

        inner()
        print(x)

    middle()
```

`nonlocal x` refers to the **nearest enclosing `x`**, which belongs to `middle()`.

So it changes:

```text
middle's x
```

not:

```text
outer's x
```

---

# 14. `nonlocal` Requires an Enclosing Variable

This is invalid:

```python
def outer():
    def inner():
        nonlocal x
        x = 10
```

There is no `x` in an enclosing function scope.

Python raises:

```text
SyntaxError
```

`nonlocal` must refer to a variable that already exists in an enclosing function scope.

---

# 15. `global` Requires a Global Variable for Reading/Assignment

For example:

```python
def update():
    global count
    count = 10
```

This creates the global variable `count` if it didn't already exist.

But `global` means:

```text
Use the module/global namespace for this name.
```

It does not mean "create a local variable shared everywhere."

---

# 16. Scope Is Different from Lifetime

These concepts are related but different.

### Scope

Where a variable can be accessed.

### Lifetime

How long the object/variable remains available.

Example:

```python
def test():
    x = 10
```

`x` has local scope.

After the function finishes, the local name `x` is normally no longer accessible from outside the function.

---

# 17. Important Scope Rule: Assignment Creates Local Variables

Inside a function:

```python
x = 10
```

normally creates a local variable.

Example:

```python
x = 100

def test():
    x = 10
    print(x)

test()

print(x)
```

Output:

```text
10
100
```

The two `x` variables belong to different scopes.

---

# 18. Reading vs Assigning

This distinction is extremely important.

### Reading

```python
x = 10

def test():
    print(x)
```

Python can find `x` in the global scope.

### Assigning

```python
x = 10

def test():
    x = 20
```

Python treats `x` as local to `test()`.

So:

```text
Reading an undeclared local
→ Python searches outward

Assignment inside function
→ Python normally treats the name as local
```

---

# 19. `global` Is Only Needed for Assignment

You don't need:

```python
global x
```

for:

```python
print(x)
```

if `x` is global.

You need it when assigning to the global name:

```python
global x
x = 20
```

or:

```python
global x
x += 1
```

---

# 20. `nonlocal` Is Only for Enclosing Function Variables

Example:

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x += 1
```

Here `x` belongs to `outer()`.

`nonlocal` allows `inner()` to modify it.

---

# 21. LEGB Example

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()

outer()
```

Output:

```text
local
```

Why?

Python finds `x` immediately in the local scope of `inner()`.

If we remove the local variable:

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        print(x)

    inner()

outer()
```

Output:

```text
enclosing
```

Python searches:

```text
Local
↓
Enclosing  ← found here
↓
Global
↓
Built-in
```

---

# 22. Common Interview Example

```python
x = 10

def test():
    print(x)
    x = 20

test()
```

This does **not** print `10`.

It raises:

```text
UnboundLocalError
```

Why?

Because Python sees:

```python
x = 20
```

inside `test()` and treats `x` as local throughout that function.

Then:

```python
print(x)
```

tries to read the local `x` before it has been assigned.

---

# 23. Quick Comparison

| Keyword | Used For | Scope |
|---|---|---|
| No keyword | Normal local variable | Current function |
| `global` | Modify/use global variable | Global/module |
| `nonlocal` | Modify/use enclosing variable | Nearest enclosing function |

---

# 24. Interview Questions

### Q1. What is the LEGB rule?

> LEGB stands for Local, Enclosing, Global, and Built-in. Python searches for a variable in this order when resolving a name.

```text
Local
↓
Enclosing
↓
Global
↓
Built-in
```

---

### Q2. Can a function read a global variable?

Yes.

```python
x = 10

def test():
    print(x)
```

---

### Q3. Can a function modify a global variable without `global`?

Not by assigning to the global name.

```python
x = 10

def test():
    x = 20
```

This creates a local `x`.

Use:

```python
global x
```

to modify the global variable.

---

### Q4. What is the difference between `global` and `nonlocal`?

```text
global
→ refers to global/module scope

nonlocal
→ refers to an enclosing function scope
```

---

### Q5. What happens when you assign to a variable inside a function?

Python normally treats that variable as **local to the function**.

---

# Quick Revision

```text
SCOPE
→ Where a variable can be accessed.


LEGB
→ Local
→ Enclosing
→ Global
→ Built-in
```

### Global

```python
x = 10

def update():
    global x
    x = 20
```

Use `global` when an inner function needs to assign to a global variable.

### Nonlocal

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20
```

Use `nonlocal` when an inner function needs to modify a variable from an enclosing function.

### Most Important Rule

```text
Inside a function:

Reading a variable
→ Python searches outward using LEGB.

Assigning to a variable
→ Python normally treats it as local.

Want to modify a global variable?
→ global

Want to modify an enclosing function's variable?
→ nonlocal
```

### Golden Rule

```text
Local     → current function
Enclosing → outer/nested function
Global    → module/file level
Built-in  → Python's built-in names

global    → modify global
nonlocal  → modify enclosing function variable
```