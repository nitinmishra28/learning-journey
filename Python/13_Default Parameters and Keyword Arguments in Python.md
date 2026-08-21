# Default Parameters and Keyword Arguments in Python

These two concepts are related to **how arguments are passed to functions**, but they solve different problems.

```text
Default Parameter
→ Provides a fallback value when an argument is not given.

Keyword Argument
→ Passes an argument using the parameter's name.
```

---

# 1. Default Parameters

A **default parameter** is a parameter that already has a value.

If the caller does not provide that argument, Python uses the default value.

### Example

```python
def greet(name="Guest"):
    print(f"Hello, {name}")
```

Calling without an argument:

```python
greet()
```

Output:

```text
Hello, Guest
```

Calling with an argument:

```python
greet("Nitin")
```

Output:

```text
Hello, Nitin
```

So:

```python
def greet(name="Guest"):
```

means:

```text
If name is provided → use the provided value
If name is not provided → use "Guest"
```

---

# 2. Why Use Default Parameters?

Default parameters make arguments **optional**.

Without a default:

```python
def greet(name):
    print(f"Hello, {name}")

greet()
```

This causes:

```text
TypeError: greet() missing 1 required positional argument
```

With a default:

```python
def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
```

Output:

```text
Hello, Guest
```

---

# 3. Multiple Default Parameters

You can have multiple parameters with default values.

```python
def calculate_price(price, tax=0.18, discount=0):
    final_price = price + price * tax - discount
    return final_price
```

Now:

```python
calculate_price(1000)
```

uses:

```text
price = 1000
tax = 0.18
discount = 0
```

You can also override the defaults:

```python
calculate_price(1000, 0.10, 50)
```

Now:

```text
price = 1000
tax = 0.10
discount = 50
```

---

# 4. Important Rule: Non-Default Parameters Before Default Parameters

This is valid:

```python
def greet(name, message="Hello"):
    print(message, name)
```

This is invalid:

```python
def greet(message="Hello", name):
    print(message, name)
```

Python raises a `SyntaxError`.

### Rule

```text
Required parameters → First
Default parameters  → After them
```

Correct:

```python
def function(a, b, c=10, d=20):
    ...
```

Incorrect:

```python
def function(a=10, b, c):
    ...
```

---

# 5. Keyword Arguments

Normally, arguments can be passed according to their position.

```python
def student(name, age, city):
    print(name, age, city)

student("Nitin", 25, "Bhopal")
```

Here:

```text
"Nitin" → name
25      → age
"Bhopal"→ city
```

This is called **positional arguments**.

With keyword arguments, you explicitly specify the parameter name:

```python
student(
    name="Nitin",
    age=25,
    city="Bhopal"
)
```

Now Python matches values using the parameter names.

---

# 6. Why Use Keyword Arguments?

Keyword arguments make function calls:

- More readable
- Less dependent on parameter order
- Easier to understand when there are many arguments

Example:

```python
def create_user(name, age, is_admin, city):
    ...
```

Instead of:

```python
create_user("Nitin", 25, True, "Bhopal")
```

you can write:

```python
create_user(
    name="Nitin",
    age=25,
    is_admin=True,
    city="Bhopal"
)
```

The second version makes the meaning of each value immediately clear.

---

# 7. Keyword Arguments Can Change the Order

With keyword arguments, you don't have to follow the parameter order.

```python
def student(name, age, city):
    print(name, age, city)

student(
    city="Bhopal",
    name="Nitin",
    age=25
)
```

This works because Python matches:

```text
city → city
name → name
age  → age
```

rather than matching based on position.

---

# 8. Combining Positional and Keyword Arguments

You can combine them.

```python
def student(name, age, city):
    print(name, age, city)

student("Nitin", age=25, city="Bhopal")
```

This is valid.

The first argument is positional:

```text
"Nitin" → name
```

The remaining arguments are keyword arguments:

```text
age=25
city="Bhopal"
```

---

# 9. Important Rule: Positional Arguments Must Come Before Keyword Arguments

Correct:

```python
student("Nitin", age=25, city="Bhopal")
```

Incorrect:

```python
student(name="Nitin", 25, city="Bhopal")
```

You cannot put a positional argument after a keyword argument.

### Remember

```text
Positional arguments
        ↓
Keyword arguments
```

Not:

```text
Keyword argument
        ↓
Positional argument
```

---

# 10. Default Parameters + Keyword Arguments

These concepts become especially useful together.

```python
def connect(host, port=5432, timeout=30):
    print(host, port, timeout)
```

You can use the defaults:

```python
connect("localhost")
```

Output:

```text
localhost 5432 30
```

You can override only one default using a keyword argument:

```python
connect("localhost", timeout=60)
```

Output:

```text
localhost 5432 60
```

Notice that we didn't have to provide `port`.

This is one of the main advantages of keyword arguments.

---

# 11. Skipping Default Parameters

Consider:

```python
def create_connection(host, port=5432, timeout=30, retries=3):
    ...
```

Suppose you only want to change `timeout`.

Without keyword arguments, you would have to provide earlier arguments:

```python
create_connection("localhost", 5432, 60, 3)
```

With keyword arguments:

```python
create_connection("localhost", timeout=60)
```

This is much clearer.

The defaults are used for:

```text
port    → 5432
retries → 3
```

and:

```text
timeout → 60
```

---

# 12. Default Value Is Evaluated When the Function Is Defined

Consider:

```python
def greet(name="Guest"):
    print(name)
```

The default value `"Guest"` is associated with the function definition.

You can inspect it using:

```python
print(greet.__defaults__)
```

Output:

```text
('Guest',)
```

This becomes particularly important with **mutable default arguments**.

---

# 13. Important Interview Topic: Mutable Default Arguments

Avoid using mutable objects such as lists or dictionaries as default parameters unless you specifically understand the behavior.

Example:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Now:

```python
print(add_item("A"))
print(add_item("B"))
print(add_item("C"))
```

You might expect:

```text
["A"]
["B"]
["C"]
```

But the actual result is:

```text
["A"]
["A", "B"]
["A", "B", "C"]
```

### Why?

The default list:

```python
[]
```

is created **once**, when the function is defined.

It is reused across calls where `items` is not provided.

Conceptually:

```text
Function definition
        ↓
One default list created
        ↓
Call 1 → modifies it
Call 2 → uses same list
Call 3 → uses same list
```

---

# 14. Correct Way to Handle Mutable Defaults

Instead of:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

use:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

Now:

```python
print(add_item("A"))
print(add_item("B"))
```

Output:

```text
["A"]
["B"]
```

A new list is created for each call where `items` is not provided.

### Important Pattern

```python
def function(data=None):
    if data is None:
        data = []
```

This pattern is very common in Python.

---

# 15. Default Parameter vs Keyword Argument

These are **not the same thing**.

### Default parameter

Defined in the function:

```python
def greet(name="Guest"):
    ...
```

`"Guest"` is the default value.

### Keyword argument

Used when calling the function:

```python
greet(name="Nitin")
```

`name="Nitin"` is a keyword argument.

So:

```text
Function definition
        ↓
Default parameter

Function call
        ↓
Keyword argument
```

---

# 16. Example Combining Everything

```python
def create_user(name, age=18, city="Bhopal"):
    print(name, age, city)
```

### Only required argument

```python
create_user("Nitin")
```

Output:

```text
Nitin 18 Bhopal
```

Defaults are used:

```text
age  → 18
city → Bhopal
```

### Override one default

```python
create_user("Nitin", age=25)
```

Output:

```text
Nitin 25 Bhopal
```

### Override both defaults

```python
create_user("Nitin", age=25, city="Delhi")
```

Output:

```text
Nitin 25 Delhi
```

### Use keywords in different order

```python
create_user(city="Delhi", name="Nitin", age=25)
```

Also valid.

---

# 17. Quick Comparison

| Concept | Where? | Example |
|---|---|---|
| Default parameter | Function definition | `def f(x=10)` |
| Positional argument | Function call | `f(20)` |
| Keyword argument | Function call | `f(x=20)` |

Example:

```python
def calculate(x, y=10):
    return x + y
```

Here:

```text
x       → required parameter
y=10    → default parameter
```

Calling:

```python
calculate(5)
```

means:

```text
x = 5
y = 10
```

Calling:

```python
calculate(5, y=20)
```

means:

```text
x = 5
y = 20
```

---

# 18. Rules to Remember

### Rule 1

Default parameters come after required parameters.

```python
def f(a, b=10):
    ...
```

---

### Rule 2

Positional arguments come before keyword arguments.

```python
f(10, b=20)
```

---

### Rule 3

Keyword arguments can be provided in any order.

```python
f(b=20, a=10)
```

---

### Rule 4

Default parameters are used only when the caller does not provide that argument.

```python
def f(x=10):
    print(x)

f()       # 10
f(20)     # 20
f(x=30)   # 30
```

---

### Rule 5

Avoid mutable default arguments such as:

```python
def f(items=[]):
    ...
```

Prefer:

```python
def f(items=None):
    if items is None:
        items = []
```

---

# 19. Interview Questions

### Q1. What is a default parameter?

A parameter that has a predefined value used when the caller does not provide an argument.

```python
def greet(name="Guest"):
    ...
```

---

### Q2. What is a keyword argument?

An argument passed using the parameter name.

```python
greet(name="Nitin")
```

---

### Q3. Can positional and keyword arguments be combined?

Yes.

```python
def f(a, b, c):
    ...

f(10, b=20, c=30)
```

But positional arguments must come before keyword arguments.

---

### Q4. Can keyword arguments be passed in a different order?

Yes.

```python
def f(a, b, c):
    ...

f(c=30, a=10, b=20)
```

---

### Q5. What is the mutable default argument problem?

Default values are created when the function is defined, not every time the function is called.

Therefore, using a mutable default such as `[]` can cause state to be shared between function calls.

---

### Q6. How do you avoid the mutable default argument problem?

Use `None` as the default:

```python
def f(items=None):
    if items is None:
        items = []
```

---

# 20. Quick Revision

```text
DEFAULT PARAMETER
→ Defined in the function
→ Provides a fallback value

def greet(name="Guest"):
    ...


KEYWORD ARGUMENT
→ Used when calling the function
→ Specifies parameter by name

greet(name="Nitin")
```

### Example

```python
def create_user(name, age=18, city="Bhopal"):
    print(name, age, city)

create_user("Nitin")
# Nitin 18 Bhopal

create_user("Nitin", age=25)
# Nitin 25 Bhopal

create_user(city="Delhi", name="Nitin", age=25)
# Nitin 25 Delhi
```

### Golden Rules

```text
Default parameter → function definition

Keyword argument → function call

Required parameters → before default parameters

Positional arguments → before keyword arguments

Avoid mutable defaults like [] and {}

Use None when you need a mutable default:
def f(data=None):
    if data is None:
        data = []
```