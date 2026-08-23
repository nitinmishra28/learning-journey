# 🐍 Python OOP — Lecture 2
# Constructors and `__init__()`

In the previous lecture, we learned:

- Class
- Object
- Instance
- Attributes
- Methods
- `self`

Now we will learn how to **initialize an object when it is created**.

This is done using the `__init__()` method.

---

# ⭐ What is `__init__()`?

`__init__()` is a special method that Python calls automatically when an object is created.

Example:

```python
class Student:

    def __init__(self):
        print("Student object created")


student = Student()
```

Output:

```text
Student object created
```

We did not explicitly call:

```python
student.__init__()
```

Python automatically called it when:

```python
student = Student()
```

was executed.

---

# Constructor vs `__init__()`

You will often hear:

```text
__init__()
↓
Constructor
```

In beginner Python discussions, `__init__()` is commonly called the constructor.

Technically, Python's object creation process involves `__new__()` and initialization through `__init__()`.

For normal Python development and interviews, the important distinction is:

```text
__new__()
↓
Creates the object

__init__()
↓
Initializes the object
```

For now, focus mainly on `__init__()`.

---

# Why Do We Need `__init__()`?

Without `__init__()`:

```python
class Student:
    pass


student = Student()

student.name = "Alice"
student.age = 20
student.marks = 90
```

We have to manually assign every attribute after creating the object.

With `__init__()`:

```python
class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
```

Now:

```python
student = Student("Alice", 20, 90)
```

The object is initialized immediately.

---

# Understanding `self`

Consider:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

When we write:

```python
student = Student("Alice", 20)
```

Python creates an object and initializes it.

Conceptually:

```text
student
   ↓
Student Object
   ├── name → "Alice"
   └── age  → 20
```

---

# Parameter vs Attribute ⭐

This is extremely important.

```python
self.name = name
```

There are two different `name`s.

```text
self.name
   ↓
Instance attribute

name
   ↓
Parameter
```

So:

```python
self.name = name
```

means:

```text
Take the value received in `name`
              ↓
Store it inside the current object
              ↓
As `self.name`
```

---

# Example

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Alice", 20)
student2 = Student("Bob", 21)

print(student1.name)
print(student2.name)
```

Output:

```text
Alice
Bob
```

Each object has its own state.

---

# Object State ⭐⭐⭐

The collection of values stored inside an object represents its **state**.

Example:

```python
student = Student("Alice", 20)
```

Object state:

```text
name = "Alice"
age = 20
```

Another object:

```python
student2 = Student("Bob", 21)
```

has a different state:

```text
name = "Bob"
age = 21
```

So:

```text
Same Class
    ↓
Different Objects
    ↓
Different State
```

This concept is extremely important in LLD.

---

# Instance Attributes

Attributes created using:

```python
self.attribute
```

are generally instance attributes.

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Here:

```python
self.name
self.age
```

are instance attributes.

Each object gets its own values.

---

# Example: Different Objects

```python
class Car:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


car1 = Car("BMW", 100)
car2 = Car("Audi", 120)
```

Conceptually:

```text
car1
 ├── brand → BMW
 └── speed → 100


car2
 ├── brand → Audi
 └── speed → 120
```

The attributes belong to their respective objects.

---

# `__init__()` with Default Values

Parameters can have default values.

```python
class Student:

    def __init__(self, name, age=18):
        self.name = name
        self.age = age
```

Now:

```python
student1 = Student("Alice")
student2 = Student("Bob", 21)
```

Values:

```text
student1.age → 18
student2.age → 21
```

---

# Default Mutable Argument ⚠️

Avoid using mutable objects as default arguments.

Bad:

```python
class Student:

    def __init__(self, subjects=[]):
        self.subjects = subjects
```

The same default list can be reused across calls.

Instead:

```python
class Student:

    def __init__(self, subjects=None):
        if subjects is None:
            subjects = []

        self.subjects = subjects
```

This is an important Python interview concept.

---

# Object Creation Flow ⭐⭐⭐

Consider:

```python
class Student:

    def __init__(self, name):
        self.name = name


student = Student("Alice")
```

Conceptually:

```text
Student("Alice")
       ↓
Object is created
       ↓
__init__() runs
       ↓
self → newly created object
       ↓
name → "Alice"
       ↓
self.name = "Alice"
```

Final object:

```text
student
   ↓
Student Object
   └── name → "Alice"
```

---

# `__init__()` Is Called Automatically

You normally do:

```python
student = Student("Alice")
```

Not:

```python
student = Student()
student.__init__("Alice")
```

Python automatically invokes initialization during object creation.

---

# Can We Call `__init__()` Manually?

Technically yes:

```python
student.__init__("Bob")
```

But this is normally **not how you should use it**.

Calling it manually reinitializes the existing object.

Prefer creating the object correctly:

```python
student = Student("Bob")
```

---

# `__init__()` Must Return `None`

`__init__()` is an initializer and should not return another value.

Correct:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Incorrect:

```python
class Student:

    def __init__(self, name):
        self.name = name
        return self.name
```

This results in an error because `__init__()` must return `None`.

---

# Constructor Parameters

A class can require different information during object creation.

Example:

```python
class BankAccount:

    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
```

Creating an object:

```python
account = BankAccount(
    "12345",
    "Alice",
    10000
)
```

The object now contains its initial state.

---

# Required vs Optional Data

You can decide which attributes are required.

Example:

```python
class User:

    def __init__(self, username, email, age=None):
        self.username = username
        self.email = email
        self.age = age
```

Here:

```text
username → Required
email    → Required
age      → Optional
```

This becomes useful when designing classes in LLD.

---

# Constructor Validation ⭐

A constructor can validate input before storing it.

Example:

```python
class BankAccount:

    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.balance = balance
```

Now:

```python
account = BankAccount(-100)
```

raises an error.

This is useful because the object does not enter an invalid state.

---

# Maintaining Valid Object State ⭐⭐⭐

One important OOP principle:

> An object should ideally be created in a valid state.

Example:

```python
class Rectangle:

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")

        self.width = width
        self.height = height
```

Now every valid `Rectangle` object has:

```text
width > 0
height > 0
```

This idea becomes very important in LLD.

---

# Constructor and Methods

`__init__()` initializes the object.

Other methods perform operations on the initialized state.

Example:

```python
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
```

Usage:

```python
account = BankAccount(1000)

account.deposit(500)

account.withdraw(200)

print(account.balance)
```

Output:

```text
1300
```

Mental model:

```text
__init__()
   ↓
Initialize State

Methods
   ↓
Modify / Use State
```

---

# Constructor in DSA ⭐

Constructors are heavily used when implementing data structures.

Example: Linked List Node

```python
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
```

Creating a node:

```python
node = Node(10)
```

Object state:

```text
data → 10
next → None
```

---

# Stack Example

```python
class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()
```

Creating:

```python
stack = Stack()
```

The constructor creates the initial internal state:

```text
stack
  ↓
items → []
```

---

# Queue Example

```python
from collections import deque


class Queue:

    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.popleft()
```

The constructor initializes:

```python
self.items
```

with an empty queue.

---

# Why Constructors Matter in LLD ⭐⭐⭐

In LLD, classes often need initial configuration.

For example:

```python
class ParkingSpot:

    def __init__(self, spot_id, vehicle_type):
        self.spot_id = spot_id
        self.vehicle_type = vehicle_type
        self.vehicle = None
```

When the object is created:

```python
spot = ParkingSpot(101, "CAR")
```

it immediately has a valid initial state.

This is exactly how object modeling starts in LLD.

---

# Multiple Constructors?

Python does **not support traditional method overloading** like some languages.

You cannot normally define:

```python
class Student:

    def __init__(self, name):
        ...

    def __init__(self, name, age):
        ...
```

The second definition replaces the first one.

Instead, use:

### Default arguments

```python
class Student:

    def __init__(self, name, age=None):
        self.name = name
        self.age = age
```

Or:

### Class methods / factory methods

These will be covered later.

---

# Constructor vs Normal Method

| `__init__()` | Normal Method |
|---|---|
| Called automatically during initialization | Usually called explicitly |
| Initializes object state | Performs behavior |
| Special method | Regular method |
| Name is fixed | Name can be chosen |
| Receives `self` | Usually receives `self` |

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
```

Here:

```text
__init__()
   ↓
Initialize

display()
   ↓
Behavior
```

---

# `__init__()` and `self` ⭐

Always remember:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

When:

```python
student = Student("Alice")
```

conceptually:

```text
self
 ↓
student
```

Therefore:

```python
self.name
```

means:

```text
student.name
```

---

# Common Mistakes

## ❌ Forgetting `self`

Incorrect:

```python
class Student:

    def __init__(name):
        self.name = name
```

Correct:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

---

## ❌ Confusing Parameter and Attribute

```python
self.name = name
```

Remember:

```text
self.name → Object's attribute
name      → Parameter
```

---

## ❌ Mutable Default Argument

Avoid:

```python
def __init__(self, items=[]):
    self.items = items
```

Prefer:

```python
def __init__(self, items=None):
    if items is None:
        items = []

    self.items = items
```

---

## ❌ Returning a Value from `__init__()`

Incorrect:

```python
def __init__(self):
    return 10
```

`__init__()` must return `None`.

---

## ❌ Putting Too Much Logic in `__init__()`

The constructor should primarily establish the object's initial valid state.

Avoid putting unrelated business logic into it.

Prefer:

```text
__init__()
   ↓
Initialize

Methods
   ↓
Perform operations
```

---

# 🎯 Interview Questions

1. What is `__init__()`?
2. Why is `__init__()` called automatically?
3. What is the difference between `__init__()` and `__new__()`?
4. Is `__init__()` technically a constructor?
5. What is the purpose of `self` inside `__init__()`?
6. What is an instance attribute?
7. What happens when `Student("Alice")` is executed?
8. Can `__init__()` return a value?
9. What happens if we define two `__init__()` methods?
10. Why should mutable default arguments be avoided?
11. How can a constructor validate object state?
12. How are constructors useful when implementing DSA data structures?
13. How are constructors useful in LLD?

---

# 📝 Quick Revision

✔ `__init__()` initializes an object.

✔ Python automatically calls `__init__()` during normal object creation.

✔ `self` refers to the current object.

✔ `self.name = name` stores the parameter inside the object.

✔ Instance attributes belong to individual objects.

✔ Different objects can have different states.

✔ Constructors should establish a valid initial state.

✔ Constructor validation can prevent invalid objects.

✔ `__init__()` must return `None`.

✔ Python does not support traditional constructor overloading.

✔ Default arguments can provide optional constructor parameters.

✔ Avoid mutable default arguments such as `[]` and `{}`.

✔ `__new__()` is responsible for creating the object.

✔ `__init__()` initializes the created object.

✔ Constructors are heavily used when implementing:

- Linked List
- Stack
- Queue
- Trees
- Graphs
- Other data structures

✔ Constructors are fundamental to object modeling in LLD.

---

# 🎯 Core Mental Model

```text
Class
  ↓
Create Object
  ↓
__new__()
  ↓
Object Created
  ↓
__init__()
  ↓
Object Initialized
  ↓
Valid Object State
  ↓
Methods Operate on State
```

The most important idea from this lecture:

```text
__init__()
    ↓
Initialize the object's state
```

And:

```python
self.attribute = value
```

means:

```text
Store value inside the current object.
```