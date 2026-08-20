# `is` vs `==` in Python

Understanding the difference between `is` and `==` is very important in Python, especially for interviews.

Both operators are used for comparison, but they answer **different questions**.

```text
==  → Equality
is  → Identity
```

The easiest way to remember:

> `==` asks: **"Do these two objects have the same value?"**  
> `is` asks: **"Are these two references pointing to the exact same object?"**

---

# 1. Quick Difference

| Operator | Name | Checks | Question |
|---|---|---|---|
| `==` | Equality operator | Value / content | Are these objects equal? |
| `is` | Identity operator | Object identity | Are these the same object? |
| `!=` | Not equal | Value / content | Are these objects different in value? |
| `is not` | Not identity | Object identity | Are these different objects? |

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

Why?

```text
a → [1, 2, 3]
b → [1, 2, 3]
```

The values are equal, but they are two different list objects.

Therefore:

```python
a == b     # True
a is b     # False
```

---

# 2. `==` — Equality Operator

The `==` operator checks whether two objects are **equal in value**.

Example:

```python
a = 10
b = 10

print(a == b)
```

Output:

```text
True
```

Because both represent the value:

```text
10
```

Another example:

```python
a = "hello"
b = "hello"

print(a == b)
```

Output:

```text
True
```

The important point is:

> `==` is concerned with **equality of values**, not whether the objects are the same object.

---

# 3. `is` — Identity Operator

The `is` operator checks whether two variables refer to the **same object**.

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
```

Output:

```text
False
```

Why?

Python created two separate list objects:

```text
a ─────→ [1, 2, 3]

b ─────→ [1, 2, 3]
```

The contents are the same, but the objects are different.

Therefore:

```python
a == b     # True
a is b     # False
```

---

# 4. The Core Concept

Always remember this:

```text
                    Comparison
                       |
              ┌────────┴────────┐
              ↓                 ↓
             ==                is
              ↓                 ↓
          Equality           Identity
              ↓                 ↓
      "Same value?"       "Same object?"
```

For example:

```python
a = [10, 20]
b = [10, 20]
```

Then:

```python
a == b
```

means:

> Does `a` contain the same value as `b`?

Answer:

```text
True
```

But:

```python
a is b
```

means:

> Are `a` and `b` referring to the exact same object?

Answer:

```text
False
```

---

# 5. Real-World Analogy

Imagine you have two notebooks.

### Notebook A

```text
Name: Nitin
Age: 25
```

### Notebook B

```text
Name: Nitin
Age: 25
```

The information inside both notebooks is identical.

So:

```text
== → True
```

But they are still two different physical notebooks.

So:

```text
is → False
```

Now imagine:

```text
Person A ─────┐
              ↓
          Same Notebook
              ↑
Person B ─────┘
```

Both people are holding the exact same notebook.

Now:

```text
== → True
is → True
```

This is the fundamental difference between **equality** and **identity**.

---

# 6. Example with Lists

```python
a = [10, 20, 30]
b = [10, 20, 30]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

### Why is `==` True?

Python compares the contents:

```text
a = [10, 20, 30]
b = [10, 20, 30]
```

The contents are equal.

Therefore:

```python
a == b
```

is:

```text
True
```

### Why is `is` False?

There are two separate list objects:

```text
Object 1 → [10, 20, 30]
Object 2 → [10, 20, 30]

a → Object 1
b → Object 2
```

Therefore:

```python
a is b
```

is:

```text
False
```

---

# 7. When Both `==` and `is` Are `True`

Consider:

```python
a = [1, 2, 3]
b = a
```

Here, Python does **not** create another list.

Instead:

```text
a ───────┐
         ↓
      [1, 2, 3]
         ↑
b ───────┘
```

Both variables refer to the same object.

Therefore:

```python
print(a == b)
print(a is b)
```

Output:

```text
True
True
```

Because:

```text
Same object
     ↓
Same contents
     ↓
== True
is True
```

---

# 8. Assignment Does Not Automatically Create a New Object

This is one of the most important concepts.

Consider:

```python
a = [1, 2, 3]
b = a
```

A beginner might imagine:

```text
a → [1, 2, 3]

b → [1, 2, 3]
```

as two lists.

That is not what happened.

Instead:

```text
       ┌──────────────┐
       ↓              ↑
a ─→ [1, 2, 3] ←─ b
```

There is only **one list object**.

Both variables point to it.

Therefore:

```python
print(a is b)
```

Output:

```text
True
```

---

# 9. Modifying One Variable

This becomes very important with mutable objects.

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)
```

Output:

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

Why did changing `b` change `a`?

Because:

```text
a ───────┐
         ↓
      [1, 2, 3]
         ↑
b ───────┘
```

Both refer to the same list.

After:

```python
b.append(4)
```

the same object becomes:

```text
[1, 2, 3, 4]
```

So both `a` and `b` see the change.

---

# 10. Creating a New Object

Compare that with:

```python
a = [1, 2, 3]
b = [1, 2, 3]
```

Now:

```text
a ─────→ Object 1 → [1, 2, 3]

b ─────→ Object 2 → [1, 2, 3]
```

They contain the same values:

```python
a == b
```

returns:

```text
True
```

But they are different objects:

```python
a is b
```

returns:

```text
False
```

---

# 11. `id()` and Object Identity

Python provides the built-in `id()` function.

It returns an integer that identifies an object during its lifetime.

Example:

```python
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
```

The values will be the same:

```text
140000000000
140000000000
```

The exact number will vary.

This confirms that both variables refer to the same object.

Conceptually:

```python
a is b
```

can be thought of as checking:

```python
id(a) == id(b)
```

However, in normal Python code, you should use:

```python
a is b
```

when you actually want an identity comparison.

Do not unnecessarily write:

```python
id(a) == id(b)
```

---

# 12. `is` Means Object Identity

Object identity means:

> Whether two references point to the exact same object.

Consider:

```python
a = [1, 2, 3]
b = a
```

There is one object:

```text
          List Object
        ┌─────────────┐
        │ 1, 2, 3     │
        └─────────────┘
           ↑       ↑
           |       |
           a       b
```

Therefore:

```python
a is b
```

is:

```text
True
```

---

# 13. `==` Can Be Customized

One major difference between `==` and `is` is that equality can be customized.

Python objects can define how equality works using:

```python
__eq__()
```

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
```

Now:

```python
s1 = Student("Nitin")
s2 = Student("Nitin")

print(s1 == s2)
print(s1 is s2)
```

Output:

```text
True
False
```

Why?

`==` uses the equality logic defined by:

```python
__eq__()
```

Our implementation says:

```python
return self.name == other.name
```

Both objects have:

```text
name = "Nitin"
```

Therefore:

```python
s1 == s2
```

is:

```text
True
```

But they are still two different objects:

```text
s1 → Student Object 1
s2 → Student Object 2
```

Therefore:

```python
s1 is s2
```

is:

```text
False
```

---

# 14. `is` Is Not Based on `__eq__`

`is` does not ask the object:

> "Do you consider yourself equal to this object?"

Instead, it checks:

> "Are these two references pointing to the same object?"

So:

```python
a == b
```

can involve custom equality logic.

But:

```python
a is b
```

is strictly about identity.

---

# 15. The Most Important Use of `is`: `None`

One of the most important Python conventions is:

```python
if value is None:
    ...
```

Example:

```python
value = None

if value is None:
    print("No value")
```

Output:

```text
No value
```

You should generally write:

```python
value is None
```

instead of:

```python
value == None
```

---

# 16. Why Do We Use `is None`?

`None` is a **singleton object** in Python.

A singleton means that Python provides one unique `None` object.

Conceptually:

```text
             None object
                 ↑
          ┌──────┴──────┐
          |             |
          x             y
```

If:

```python
x = None
y = None
```

both variables refer to that same singleton object.

Therefore:

```python
x is None
```

is the appropriate identity check.

---

# 17. `None` Example

Consider a function:

```python
def get_user():
    return None
```

Then:

```python
result = get_user()

if result is None:
    print("User not found")
```

Output:

```text
User not found
```

This is standard Python style.

---

# 18. `is not None`

The opposite is:

```python
is not
```

Example:

```python
result = "Nitin"

if result is not None:
    print("Value exists")
```

Output:

```text
Value exists
```

Use:

```python
is not None
```

when you want to check that a value is not the `None` singleton.

---

# 19. Why `== None` Is Not Recommended

You might see:

```python
if value == None:
    ...
```

This may work in simple cases.

But it is not the preferred Python style.

Use:

```python
if value is None:
    ...
```

The reason is that `None` is a singleton and you are checking for that **specific object**.

Also, `==` can invoke custom equality behavior.

For example, a class could define unusual behavior for:

```python
__eq__()
```

So:

```python
value == None
```

does not communicate the same precise intent as:

```python
value is None
```

---

# 20. `is not` Operator

Python also provides:

```python
is not
```

Example:

```python
a = [1, 2]
b = [1, 2]

print(a is not b)
```

Output:

```text
True
```

Because they are different objects.

Similarly:

```python
a = [1, 2]
b = a

print(a is not b)
```

Output:

```text
False
```

Because they are the same object.

---

# 21. `!=` vs `is not`

These are also different concepts.

### `!=`

Checks value inequality:

```python
a = [1, 2]
b = [1, 3]

print(a != b)
```

Output:

```text
True
```

Because their contents are different.

### `is not`

Checks object identity:

```python
a = [1, 2]
b = [1, 2]

print(a is not b)
```

Output:

```text
True
```

Because they are two different objects.

---

# 22. Important Example

```python
a = [1, 2]
b = [1, 2]

print(a == b)
print(a != b)

print(a is b)
print(a is not b)
```

Output:

```text
True
False
False
True
```

Interpretation:

```text
a == b
→ Values are equal

a != b
→ Values are not different

a is b
→ They are not the same object

a is not b
→ They are different objects
```

---

# 23. Mutable Objects

The difference between `is` and `==` becomes particularly important with mutable objects.

Common mutable objects include:

```text
list
dict
set
bytearray
```

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False
```

Now:

```python
b.append(4)
```

Then:

```python
print(a)
print(b)
```

Output:

```text
[1, 2, 3]
[1, 2, 3, 4]
```

Because they were separate objects.

---

# 24. Mutable Object with Assignment

Now compare:

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)
```

Output:

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

Because:

```python
a is b
```

is:

```text
True
```

Both names refer to the same list.

---

# 25. Immutable Objects

Common immutable objects include:

```text
int
float
bool
str
tuple
frozenset
NoneType
```

For immutable objects, Python may sometimes reuse existing objects internally.

This can create confusing results when testing `is`.

For example:

```python
a = 10
b = 10

print(a == b)
print(a is b)
```

You may get:

```text
True
True
```

This does **not** mean:

> "`is` should be used to compare integers."

It means Python may have made both names refer to the same object.

---

# 26. Very Important: Do Not Use `is` for Normal Value Comparisons

Never write code like:

```python
a = 100
b = 100

if a is b:
    print("Same")
```

just because it happens to return:

```text
True
```

The correct comparison is:

```python
if a == b:
    print("Same")
```

Why?

Because you care about the **value**:

```text
100 == 100
```

not whether Python happens to use the same object.

---

# 27. Integer Caching / Interning

Python implementations may reuse certain immutable objects.

For example:

```python
a = 10
b = 10

print(a is b)
```

may return:

```text
True
```

Python can reuse the same integer object.

This is an implementation optimization.

The important lesson is:

> Never depend on `is` for value comparison.

Use:

```python
==
```

for values.

Use:

```python
is
```

for identity.

---

# 28. Why Large Integers Can Be Confusing

Consider:

```python
a = 1000
b = 1000

print(a == b)
print(a is b)
```

You may see:

```text
True
False
```

Depending on how the values were created and the Python implementation/context, identity behavior can differ.

The important thing is:

```python
a == b
```

is the correct way to ask:

> Are the integers equal?

You should never write:

```python
a is b
```

for this purpose.

---

# 29. Strings Can Also Be Confusing

Consider:

```python
a = "hello"
b = "hello"

print(a == b)
print(a is b)
```

You may see:

```text
True
True
```

This can happen because Python may intern/reuse certain strings.

But again:

```python
a is b
```

does **not** mean:

> "The strings have the same value."

It means:

> "Both variables refer to the same string object."

For string comparison, use:

```python
a == b
```

---

# 30. String Example Where Identity Should Not Be Trusted

```python
a = "".join(["hel", "lo"])
b = "hello"

print(a == b)
print(a is b)
```

The important comparison is:

```python
a == b
```

which checks the actual string value.

The result of:

```python
a is b
```

should not be used to determine whether two strings have the same content.

---

# 31. Interview Trap: `is` and Small Integers

Interviewers sometimes ask:

```python
a = 10
b = 10

print(a == b)
print(a is b)
```

Possible output:

```text
True
True
```

Then they may ask:

> Why is `is` True?

Because Python may reuse/caches certain immutable objects.

The correct interview answer is:

> `==` checks equality, while `is` checks identity. If `is` happens to return `True` for small integers, that is an implementation optimization and should not be relied upon for value comparison.

---

# 32. Interview Trap: Strings

Example:

```python
a = "python"
b = "python"

print(a == b)
print(a is b)
```

You might get:

```text
True
True
```

Again, do not conclude:

> "`is` compares strings."

It does not.

The correct explanation is:

```text
== → string values are equal
is → both variables happen to refer to the same object
```

For string values, always use:

```python
a == b
```

---

# 33. `is` vs `==` with Custom Classes

Consider:

```python
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Nitin")
p2 = Person("Nitin")

print(p1 == p2)
print(p1 is p2)
```

If `__eq__()` is not implemented, normally:

```text
p1 == p2 → False
p1 is p2 → False
```

Why?

There are two separate objects:

```text
p1 → Person Object 1
p2 → Person Object 2
```

Even though both have:

```text
name = "Nitin"
```

they are different objects.

---

# 34. Adding `__eq__()`

Now:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
```

Then:

```python
p1 = Person("Nitin")
p2 = Person("Nitin")

print(p1 == p2)
print(p1 is p2)
```

Output:

```text
True
False
```

This is an excellent example for understanding the distinction.

```text
== → "Do these Persons represent equal data?"
is → "Are these the same Person object?"
```

---

# 35. `is` Is Useful for Singleton Objects

`is` is particularly useful when dealing with singleton/sentinel objects.

The most common example is:

```python
None
```

Example:

```python
if result is None:
    ...
```

Other code can also define its own sentinel:

```python
MISSING = object()
```

Then:

```python
value = MISSING

if value is MISSING:
    print("Value was not provided")
```

Here `is` is appropriate because we want to check for that **exact sentinel object**.

---

# 36. Sentinel Object Example

Suppose we need to distinguish between:

```text
No argument provided
```

and:

```text
Argument explicitly provided as None
```

We can use:

```python
MISSING = object()

def function(value=MISSING):
    if value is MISSING:
        print("Argument was not provided")
    else:
        print("Argument was provided")
```

Now:

```python
function()
```

Output:

```text
Argument was not provided
```

And:

```python
function(None)
```

Output:

```text
Argument was provided
```

Why does `is` work well here?

Because we specifically want to identify the exact sentinel object:

```python
value is MISSING
```

---

# 37. Equality vs Identity Diagram

Consider:

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a
```

The object relationship is:

```text
             ┌───────────────┐
             │ [1, 2, 3]     │
             └───────────────┘
                ↑         ↑
                │         │
                a         c


             ┌───────────────┐
             │ [1, 2, 3]     │
             └───────────────┘
                       ↑
                       │
                       b
```

Therefore:

```python
a == b     # True
a is b     # False

a == c     # True
a is c     # True

b == c     # True
b is c     # False
```

This example is extremely important.

All three contain the same values:

```text
[1, 2, 3]
```

But only `a` and `c` point to the same object.

---

# 38. One Example to Memorize

If you remember only one example, remember this:

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a
```

Then:

```python
print(a == b)
print(a is b)

print(a == c)
print(a is c)
```

Output:

```text
True
False
True
True
```

Why?

```text
a and b
→ Same value
→ Different objects

a and c
→ Same value
→ Same object
```

---

# 39. Common Mistake #1

### Wrong:

```python
if x is 10:
    print("x is 10")
```

### Correct:

```python
if x == 10:
    print("x is 10")
```

Why?

You are asking whether:

```text
x has the value 10
```

That is an equality check.

Therefore:

```python
==
```

should be used.

---

# 40. Common Mistake #2

### Wrong:

```python
if username is "Nitin":
    ...
```

### Correct:

```python
if username == "Nitin":
    ...
```

You care about the string's value/content, not object identity.

---

# 41. Common Mistake #3

### Wrong:

```python
if result == None:
    ...
```

### Preferred:

```python
if result is None:
    ...
```

Here you are checking specifically for the `None` singleton.

---

# 42. Common Mistake #4

Do not assume:

```python
a == b
```

means:

```python
a is b
```

They are completely different concepts.

For example:

```python
a = [1, 2]
b = [1, 2]
```

Then:

```python
a == b
```

is:

```text
True
```

but:

```python
a is b
```

is:

```text
False
```

---

# 43. Common Mistake #5

Do not assume:

```python
a is b
```

means Python compared their contents.

For example:

```python
a = [1, 2]
b = a
```

Then:

```python
a is b
```

is:

```text
True
```

because both variables refer to the same object.

It does not mean Python compared:

```text
1 == 1
2 == 2
```

It is an identity check.

---

# 44. Decision Rule

When writing Python code, ask yourself:

### Question 1

> Am I checking whether two values are equal?

Use:

```python
==
```

Example:

```python
if age == 25:
    ...
```

```python
if name == "Nitin":
    ...
```

```python
if list1 == list2:
    ...
```

---

### Question 2

> Am I checking whether two references point to the same object?

Use:

```python
is
```

Example:

```python
if a is b:
    ...
```

---

### Question 3

> Am I checking for `None`?

Use:

```python
is None
```

Example:

```python
if result is None:
    ...
```

---

### Question 4

> Am I checking that something is not `None`?

Use:

```python
is not None
```

Example:

```python
if result is not None:
    ...
```

---

# 45. Cheat Sheet

```text
==================================================
              is vs ==
==================================================

==

Meaning:
    Equality

Question:
    "Do these objects have equal values?"

Example:
    [1, 2] == [1, 2]

Result:
    True


is

Meaning:
    Identity

Question:
    "Are these references pointing to the same object?"

Example:
    a = [1, 2]
    b = a

    a is b

Result:
    True


None

Use:

    value is None

    value is not None


Do NOT use:

    value == None
    value is 10
    value is "hello"

Use:

    value is None
    value == 10
    value == "hello"
```

---

# 46. Interview Perspective

## Q1. What is the difference between `is` and `==`?

**Answer:**

> `==` checks equality, meaning whether two objects have equal values. `is` checks identity, meaning whether two variables refer to the exact same object.

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

a == b     # True
a is b     # False
```

---

## Q2. When should you use `is`?

**Answer:**

> Use `is` when checking object identity, especially when comparing against singleton objects such as `None`.

Example:

```python
if value is None:
    ...
```

---

## Q3. Why is `is None` preferred over `== None`?

**Answer:**

> Because `None` is a singleton and we want to check whether the value refers to that exact object. `==` performs equality comparison and can invoke custom equality behavior.

Correct:

```python
if value is None:
    ...
```

---

## Q4. Can `==` and `is` both return `True`?

Yes.

Example:

```python
a = [1, 2, 3]
b = a

print(a == b)
print(a is b)
```

Output:

```text
True
True
```

Because both variables refer to the same object, and therefore that object is also equal to itself.

---

## Q5. Can `==` be `True` while `is` is `False`?

Yes.

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

This is probably the most important example to remember.

---

## Q6. Can `is` be `True` while `==` is `False`?

For normal Python objects, if two variables are referring to the exact same object, comparing the object with itself normally gives equality.

So:

```python
a is b
```

strongly implies that they are the same object, and normal equality will be true as well.

However, Python allows custom `__eq__()` implementations, so unusual user-defined behavior can make equality behave unexpectedly.

For interview purposes, remember:

```text
Same object → normally equal to itself
```

---

# 47. Important Mental Model

Do not think of:

```python
a = [1, 2, 3]
```

as:

```text
a contains [1, 2, 3]
```

A better mental model is:

```text
a ─────→ Object
          ↓
       [1, 2, 3]
```

The variable `a` is a **name/reference** associated with an object.

Now:

```python
b = a
```

means:

```text
a ───────┐
         ↓
      Object
         ↑
b ───────┘
```

This is why:

```python
a is b
```

is `True`.

---

# 48. Think in Terms of "Value" vs "Object"

Whenever you see:

```python
==
```

think:

```text
VALUE
```

Whenever you see:

```python
is
```

think:

```text
OBJECT
```

So:

```text
==  → VALUE
is  → OBJECT
```

This mental shortcut is extremely useful during interviews.

---

# 49. Practical Examples

### Comparing numbers

```python
age = 25

if age == 25:
    print("Correct age")
```

Use `==`.

---

### Comparing strings

```python
name = "Nitin"

if name == "Nitin":
    print("Correct name")
```

Use `==`.

---

### Comparing lists

```python
a = [1, 2, 3]
b = [1, 2, 3]

if a == b:
    print("Same contents")
```

Use `==`.

---

### Checking same object

```python
a = [1, 2, 3]
b = a

if a is b:
    print("Same object")
```

Use `is`.

---

### Checking `None`

```python
result = None

if result is None:
    print("No result")
```

Use `is None`.

---

### Checking not `None`

```python
result = 100

if result is not None:
    print("Result exists")
```

Use `is not None`.

---

# 50. `is` Does Not Mean "Same Value"

This is perhaps the most important misconception to eliminate.

Never interpret:

```python
a is b
```

as:

```text
a and b have the same value
```

Instead interpret it as:

```text
a and b are references to the same object
```

Similarly:

```python
a == b
```

does not necessarily mean:

```text
a and b are the same object
```

It only means:

```text
a and b are equal according to their equality semantics
```

---

# 51. Final Comparison Table

| Situation | Use |
|---|---|
| Compare numbers | `==` |
| Compare strings | `==` |
| Compare lists | `==` |
| Compare dictionaries | `==` |
| Compare sets | `==` |
| Compare object values | `==` |
| Check same object | `is` |
| Check `None` | `is None` |
| Check not `None` | `is not None` |
| Check a specific sentinel object | `is` |
| Check whether two references point to the same object | `is` |

---

# 52. Golden Rules

Memorize these rules:

```text
Rule 1:
== checks equality.

Rule 2:
is checks identity.

Rule 3:
Use == for comparing values.

Rule 4:
Use is for checking object identity.

Rule 5:
Use is None instead of == None.

Rule 6:
Use is not None instead of != None.

Rule 7:
Never use is for normal integer/string/list value comparisons.

Rule 8:
Do not depend on integer/string interning or caching behavior.

Rule 9:
Assignment like b = a makes both names refer to the same object.

Rule 10:
Two objects can be equal (== True) without being identical (is False).
```

---

# 53. One-Line Interview Answer

If the interviewer asks:

> **"What is the difference between `is` and `==` in Python?"**

Say:

> **"`==` checks equality of values, while `is` checks object identity. `==` asks whether two objects are equal, whereas `is` asks whether both references point to the exact same object. `is` is commonly used with singleton objects such as `None`.**

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True
print(a is b)  # False

print(a == c)  # True
print(a is c)  # True
```

---

# 54. Quick Revision

Before an interview, remember only this:

```text
              is vs ==

        ┌──────────────────┐
        │       ==         │
        └────────┬─────────┘
                 ↓
             Equality
                 ↓
          "Same value?"
                 

        ┌──────────────────┐
        │       is         │
        └────────┬─────────┘
                 ↓
             Identity
                 ↓
          "Same object?"
```

The classic example:

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a == b     # True
a is b     # False

a == c     # True
a is c     # True
```

And the most important Python convention:

```python
if value is None:
    ...
```

```text
== → Same value?
is → Same object?
```