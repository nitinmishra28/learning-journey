# `*args` and `**kwargs` in Python

`*args` and `**kwargs` are used when a function needs to accept a **variable number of arguments**.

```text
*args    → multiple positional arguments
**kwargs → multiple keyword arguments
```

---

# 1. `*args`

`*args` allows a function to accept **any number of positional arguments**.

### Without `*args`

```python
def add(a, b):
    return a + b

add(10, 20)
```

This function accepts exactly two arguments.

If you want to pass more:

```python
add(10, 20, 30)
```

you get an error.

### With `*args`

```python
def add(*args):
    print(args)
```

Now:

```python
add(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

`args` is a **tuple**.

---

# 2. How `*args` Works

Consider:

```python
def add(*args):
    total = 0

    for num in args:
        total += num

    return total
```

Now:

```python
print(add(10, 20))
print(add(10, 20, 30))
print(add(1, 2, 3, 4, 5))
```

Output:

```text
30
60
15
```

Conceptually:

```python
add(10, 20, 30)
```

becomes:

```python
args = (10, 20, 30)
```

So:

```text
*args → tuple of positional arguments
```

---

# 3. `args` Is Just a Name

The name `args` is not special.

The `*` is what matters.

These are equivalent:

```python
def function(*args):
    ...
```

and:

```python
def function(*numbers):
    ...
```

Example:

```python
def add(*numbers):
    return sum(numbers)

print(add(10, 20, 30))
```

Output:

```text
60
```

However, `*args` is the standard convention, so it is best to use it.

---

# 4. `**kwargs`

`**kwargs` allows a function to accept **any number of keyword arguments**.

Example:

```python
def show_info(**kwargs):
    print(kwargs)
```

Calling:

```python
show_info(name="Nitin", age=25, city="Bhopal")
```

Output:

```text
{
    'name': 'Nitin',
    'age': 25,
    'city': 'Bhopal'
}
```

`kwargs` is a **dictionary**.

So:

```text
*args    → tuple
**kwargs → dictionary
```

---

# 5. Using `**kwargs`

Because `kwargs` is a dictionary, you can access values using keys.

```python
def show_info(**kwargs):
    print(kwargs["name"])
    print(kwargs["age"])

show_info(name="Nitin", age=25)
```

Output:

```text
Nitin
25
```

You can also iterate:

```python
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
```

---

# 6. `*args` vs `**kwargs`

| Feature | `*args` | `**kwargs` |
|---|---|---|
| Accepts | Positional arguments | Keyword arguments |
| Stored as | Tuple | Dictionary |
| Example | `func(10, 20)` | `func(a=10, b=20)` |

Remember:

```text
*args
→ positional
→ tuple

**kwargs
→ keyword
→ dictionary
```

---

# 7. Using Both Together

A function can accept both:

```python
def function(*args, **kwargs):
    print(args)
    print(kwargs)
```

Calling:

```python
function(10, 20, 30, name="Nitin", age=25)
```

Output:

```text
(10, 20, 30)

{'name': 'Nitin', 'age': 25}
```

So:

```text
10, 20, 30
    ↓
*args
    ↓
(10, 20, 30)


name="Nitin", age=25
    ↓
**kwargs
    ↓
{"name": "Nitin", "age": 25}
```

---

# 8. Combining Normal Parameters with `*args` and `**kwargs`

You can also have regular parameters.

```python
def function(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)
```

Calling:

```python
function(
    "Nitin",
    10,
    20,
    age=25,
    city="Bhopal"
)
```

Output:

```text
Nitin
(10, 20)
{'age': 25, 'city': 'Bhopal'}
```

Here:

```text
"Nitin"       → name
10, 20        → args
age=25, city= → kwargs
```

---

# 9. Parameter Order

When using all types of parameters, the general order is:

```python
def function(positional, *args, **kwargs):
    ...
```

For example:

```python
def example(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
```

The important idea is:

```text
normal parameters
        ↓
*args
        ↓
**kwargs
```

---

# 10. Very Important: `*` Has Two Uses

The `*` syntax can mean different things depending on where it appears.

### In a function definition

```python
def func(*args):
    ...
```

It means:

> Collect multiple positional arguments into a tuple.

### In a function call

```python
numbers = [10, 20, 30]

func(*numbers)
```

It means:

> Unpack the iterable and pass its elements as separate positional arguments.

So:

```python
*args
```

can mean **collect** in a function definition, while:

```python
*values
```

can mean **unpack** in a function call.

---

# 11. `*` Unpacking Example

```python
def add(a, b, c):
    return a + b + c

numbers = [10, 20, 30]

print(add(*numbers))
```

This is equivalent to:

```python
add(10, 20, 30)
```

The `*` unpacks:

```text
[10, 20, 30]
      ↓
10, 20, 30
```

---

# 12. `**` Unpacking

`**` can also be used when calling a function to unpack a dictionary into keyword arguments.

```python
def student(name, age, city):
    print(name, age, city)

data = {
    "name": "Nitin",
    "age": 25,
    "city": "Bhopal"
}

student(**data)
```

This is equivalent to:

```python
student(
    name="Nitin",
    age=25,
    city="Bhopal"
)
```

So:

```text
Function definition:

*args
→ collect positional arguments

**kwargs
→ collect keyword arguments


Function call:

*data
→ unpack positional arguments

**data
→ unpack keyword arguments
```

---

# 13. Common Interview Example

```python
def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(1, 2, 3, name="Nitin", age=25)
```

Output:

```text
(1, 2, 3)
{'name': 'Nitin', 'age': 25}
```

Remember:

```text
1, 2, 3
→ positional
→ args
→ tuple


name="Nitin", age=25
→ keyword
→ kwargs
→ dictionary
```

---

# 14. Common Mistake

Don't confuse:

```python
*args
```

with:

```python
**kwargs
```

### `*args`

```python
func(10, 20, 30)
```

Collects:

```python
args = (10, 20, 30)
```

### `**kwargs`

```python
func(name="Nitin", age=25)
```

Collects:

```python
kwargs = {
    "name": "Nitin",
    "age": 25
}
```

---

# 15. Why Are They Useful?

They are useful when you don't know beforehand how many arguments a function will receive.

For example:

```python
def add(*args):
    return sum(args)
```

Now all of these work:

```python
add(1, 2)
add(1, 2, 3)
add(1, 2, 3, 4, 5)
```

`**kwargs` is useful when you want flexible named options:

```python
def create_user(**kwargs):
    print(kwargs)
```

Then:

```python
create_user(
    name="Nitin",
    age=25,
    city="Bhopal"
)
```

---

# 16. Interview Questions

### Q1. What is `*args`?

> `*args` allows a function to accept a variable number of positional arguments. Inside the function, those arguments are stored as a tuple.

```python
def func(*args):
    print(args)
```

---

### Q2. What is `**kwargs`?

> `**kwargs` allows a function to accept a variable number of keyword arguments. Inside the function, those arguments are stored as a dictionary.

```python
def func(**kwargs):
    print(kwargs)
```

---

### Q3. What type is `args`?

```python
tuple
```

---

### Q4. What type is `kwargs`?

```python
dict
```

---

### Q5. Can we use both?

Yes:

```python
def func(*args, **kwargs):
    ...
```

---

### Q6. What does `*` do in a function call?

It **unpacks** an iterable into positional arguments.

```python
numbers = [1, 2, 3]

func(*numbers)
```

---

### Q7. What does `**` do in a function call?

It **unpacks** a dictionary into keyword arguments.

```python
data = {"name": "Nitin", "age": 25}

func(**data)
```

---

# 17. Quick Revision

```text
*args
→ Variable number of positional arguments
→ Stored as tuple

**kwargs
→ Variable number of keyword arguments
→ Stored as dictionary
```

### Definition

```python
def func(*args, **kwargs):
    ...
```

### Call

```python
func(1, 2, 3, name="Nitin", age=25)
```

Result:

```python
args = (1, 2, 3)

kwargs = {
    "name": "Nitin",
    "age": 25
}
```

### Unpacking

```python
func(*[1, 2, 3])
```

means:

```python
func(1, 2, 3)
```

And:

```python
func(**{"name": "Nitin", "age": 25})
```

means:

```python
func(name="Nitin", age=25)
```

### Golden Rule

```text
*args
→ collect positional arguments
→ tuple

**kwargs
→ collect keyword arguments
→ dictionary

* in function call
→ unpack positional arguments

** in function call
→ unpack keyword arguments
```
```