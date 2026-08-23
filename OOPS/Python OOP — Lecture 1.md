# 🐍 Python OOP — Lecture 1
# Introduction to Object-Oriented Programming

Object-Oriented Programming (**OOP**) is a programming paradigm where we organize code around **objects**.

An object combines:

```text
Data
+
Behavior
```

For example, a `Car` object can have:

```text
Data:
    brand
    model
    speed

Behavior:
    accelerate()
    brake()
```

OOP becomes especially important when building:

- Large applications
- Backend systems
- Reusable components
- Maintainable software
- Low-Level Design (LLD)
- Interview design problems

---

# Why Do We Need OOP?

Consider a program that manages multiple students.

Without OOP, we might have:

```python
student1_name = "Alice"
student1_age = 20
student1_marks = 90

student2_name = "Bob"
student2_age = 21
student2_marks = 85
```

As the application grows, this becomes difficult to manage.

We would also need separate functions:

```python
def display_student(name, age, marks):
    ...

def calculate_grade(marks):
    ...
```

The data and behavior are separated.

OOP allows us to group related data and behavior together.

---

# Object-Oriented Approach

Instead of:

```python
student1_name = "Alice"
student1_age = 20
student1_marks = 90
```

we can create:

```python
student1 = Student("Alice", 20, 90)
```

Now the student object contains both:

```text
Data
↓
name
age
marks

Behavior
↓
display()
calculate_grade()
```

This makes the code easier to organize and reuse.

---

# 🧱 Class

A **class** is a blueprint for creating objects.

Example:

```python
class Student:
    pass
```

Here:

```text
Student
   ↓
Class
```

The class itself does not represent one specific student.

It defines what a student object can contain.

---

# Object

An **object** is an instance of a class.

```python
class Student:
    pass


student1 = Student()
student2 = Student()
```

Here:

```text
Student
   ↓
  Class
   ↓
 ┌───────────┐
 │           │
 ↓           ↓
student1   student2
Object     Object
```

Both objects are created from the same class.

---

# Class vs Object

| Class | Object |
|---|---|
| Blueprint | Actual instance |
| Defines structure | Contains actual data |
| Logical definition | Real entity in memory |
| Example: `Student` | Example: `student1` |

Think:

```text
Class
 ↓
Blueprint

Object
 ↓
Actual thing created from blueprint
```

---

# Simple Example

```python
class Student:
    pass


student1 = Student()

print(student1)
```

`Student` is the class.

`student1` is an object of that class.

---

# `type()`

We can check the type of an object using:

```python
class Student:
    pass


student = Student()

print(type(student))
```

Output will look similar to:

```text
<class '__main__.Student'>
```

This tells us that:

```text
student
   ↓
object
   ↓
Student
```

---

# `isinstance()`

`isinstance()` checks whether an object belongs to a particular class.

```python
class Student:
    pass


student = Student()

print(isinstance(student, Student))
```

Output:

```text
True
```

This is useful in interviews and real applications when checking object types.

---

# Multiple Objects

A class can create many independent objects.

```python
class Student:
    pass


student1 = Student()
student2 = Student()
student3 = Student()
```

Conceptually:

```text
             Student
                |
        ┌───────┼───────┐
        ↓       ↓       ↓
     student1 student2 student3
```

Each object is a separate instance.

---

# Attributes

Objects need data.

This data is stored in **attributes**.

Example:

```python
class Student:
    pass


student = Student()

student.name = "Alice"
student.age = 20
student.marks = 90
```

Now the object contains:

```text
student
 ├── name = "Alice"
 ├── age = 20
 └── marks = 90
```

Accessing attributes:

```python
print(student.name)
print(student.age)
print(student.marks)
```

Output:

```text
Alice
20
90
```

---

# Methods

Functions defined inside a class are called **methods**.

Example:

```python
class Student:

    def display(self):
        print("Student details")


student = Student()

student.display()
```

Output:

```text
Student details
```

Here:

```text
display()
   ↓
Method
```

A method represents behavior associated with an object.

---

# Data + Behavior

This is one of the most important ideas in OOP.

A class can combine:

```text
Data
+
Behavior
```

Example:

```python
class Student:

    def display(self):
        print("Student")


student = Student()

student.display()
```

Later, we will add attributes and methods together.

---

# `self` ⭐⭐⭐

One of the most important concepts in Python OOP.

`self` represents the **current object**.

Example:

```python
class Student:

    def display(self):
        print(self)


student1 = Student()
student2 = Student()

student1.display()
student2.display()
```

The `self` inside the method refers to the object that called the method.

Conceptually:

```text
student1.display()
        ↓
self = student1
```

and:

```text
student2.display()
        ↓
self = student2
```

---

# Why Do We Need `self`?

Suppose each student has a different name.

```python
class Student:

    def set_name(self, name):
        self.name = name
```

Now:

```python
student1 = Student()
student2 = Student()

student1.set_name("Alice")
student2.set_name("Bob")
```

Memory conceptually becomes:

```text
student1
 └── name → "Alice"


student2
 └── name → "Bob"
```

`self` tells Python **which object's attribute** we are accessing.

---

# `self.name`

Consider:

```python
class Student:

    def set_name(self, name):
        self.name = name
```

There are two different things here:

```python
self.name
```

and:

```python
name
```

`name`:

```text
Local parameter
```

`self.name`:

```text
Attribute belonging to the current object
```

So:

```python
self.name = name
```

means:

```text
Take the parameter `name`
        ↓
Store it inside the current object
        ↓
As attribute `self.name`
```

---

# Example

```python
class Student:

    def set_name(self, name):
        self.name = name

    def display(self):
        print(self.name)


student1 = Student()
student2 = Student()

student1.set_name("Alice")
student2.set_name("Bob")

student1.display()
student2.display()
```

Output:

```text
Alice
Bob
```

Each object has its own `name`.

---

# Important: `self` Is Not a Keyword

`self` is a naming convention.

Python does not technically require the name `self`.

For example:

```python
class Student:

    def display(obj):
        print(obj)
```

This works.

However, you should **always use `self`**.

```python
class Student:

    def display(self):
        print(self)
```

`self` is the standard Python convention and is expected in interviews and professional code.

---

# Method Calling Internally ⭐

When we write:

```python
student.display()
```

Python internally passes the object to the method.

Conceptually:

```python
Student.display(student)
```

Therefore:

```python
self
```

refers to:

```python
student
```

This explains why `self` is required in instance methods.

---

# Instance

An object created from a class is called an **instance** of that class.

```python
class Student:
    pass


student = Student()
```

Here:

```text
Student
   ↓
Class

student
   ↓
Instance / Object
```

These terms are often used interchangeably:

```text
Object
Instance
```

---

# Instance Attributes

Attributes belonging to a specific object are called **instance attributes**.

Example:

```python
class Student:

    def set_name(self, name):
        self.name = name


student1 = Student()
student2 = Student()

student1.set_name("Alice")
student2.set_name("Bob")
```

Now:

```text
student1.name → Alice
student2.name → Bob
```

Each object has its own value.

---

# Instance Methods

A method that works with a particular object's data is called an **instance method**.

Example:

```python
class Student:

    def display(self):
        print(self.name)
```

The method uses:

```python
self.name
```

Therefore it operates on the current object.

---

# OOP Mental Model ⭐

Think of:

```python
student1.display()
```

as:

```text
Which object?
      ↓
   student1
      ↓
Pass it as self
      ↓
Run display()
```

This mental model will become very important when we learn:

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
- `@classmethod`
- `@staticmethod`
- LLD

---

# OOP and DSA

OOP is also useful while implementing DSA data structures.

For example, a stack can be implemented using a class:

```python
class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()
```

Then:

```python
stack = Stack()

stack.push(10)
stack.push(20)

print(stack.pop())
```

Output:

```text
20
```

Here:

```text
Stack
 ↓
Class

stack
 ↓
Object

items
 ↓
Data

push()
pop()
 ↓
Behavior
```

This is exactly where OOP starts becoming useful for DSA.

---

# OOP and LLD ⭐⭐⭐

OOP is the foundation of many LLD concepts.

For example, in a parking lot system we may have:

```text
ParkingLot
Vehicle
Car
Bike
ParkingSpot
Ticket
Payment
```

Each can potentially be represented as a class.

The goal is not simply to create classes.

The goal is to model:

```text
Entities
+
Responsibilities
+
Relationships
+
Interactions
```

We will study these concepts later.

---

# Four Major OOP Pillars

The four commonly discussed pillars of OOP are:

```text
1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism
```

We will study each in depth in upcoming lectures.

For now, remember:

### Encapsulation

Bundling data and methods together and controlling access to the data.

### Abstraction

Hiding unnecessary implementation details and exposing what is necessary.

### Inheritance

Allowing one class to derive behavior and structure from another class.

### Polymorphism

Allowing the same interface/method concept to behave differently for different objects.

---

# Class Responsibility ⭐

A class should represent a meaningful entity or responsibility.

Good example:

```python
class BankAccount:
    ...
```

It can manage:

```text
balance
deposit()
withdraw()
```

Avoid creating classes just for the sake of creating classes.

In LLD, this idea becomes extremely important.

---

# Common Beginner Mistakes

### ❌ Forgetting `self`

Incorrect:

```python
class Student:

    def display():
        print("Student")
```

Calling:

```python
student.display()
```

causes an error because Python passes the object automatically.

Correct:

```python
class Student:

    def display(self):
        print("Student")
```

---

### ❌ Confusing Class and Object

```python
class Student:
    pass
```

`Student` is the class.

```python
student = Student()
```

`student` is the object/instance.

---

### ❌ Confusing Attribute and Local Variable

```python
class Student:

    def set_name(self, name):
        self.name = name
```

Here:

```text
name
 ↓
Parameter / local variable

self.name
 ↓
Instance attribute
```

---

# Interview Questions

1. What is OOP?
2. Why do we use OOP?
3. What is a class?
4. What is an object?
5. What is an instance?
6. Difference between class and object?
7. What is `self` in Python?
8. Why is `self` required in instance methods?
9. Is `self` a keyword in Python?
10. What is an instance attribute?
11. What is an instance method?
12. What happens internally when `obj.method()` is called?
13. What are the four pillars of OOP?
14. How is OOP useful in DSA?
15. Why is OOP important for LLD?

---

# Quick Revision

✔ OOP organizes code around objects.

✔ A class is a blueprint for creating objects.

✔ An object is an instance of a class.

✔ Objects contain data through attributes.

✔ Objects contain behavior through methods.

✔ `self` represents the current object.

✔ `self` is a convention, not a Python keyword.

✔ `self.name` is an instance attribute.

✔ `name` can be a local variable or parameter.

✔ Instance attributes can have different values for different objects.

✔ Instance methods operate on the current object.

✔ `obj.method()` conceptually passes `obj` as `self`.

✔ OOP is heavily used when designing reusable systems.

✔ OOP is the foundation for many LLD concepts.

✔ The four major OOP pillars are:

```text
Encapsulation
Abstraction
Inheritance
Polymorphism
```

---

# 🎯 DSA + LLD Connection

Keep this mental model:

```text
Class
  ↓
Blueprint

Object
  ↓
Actual Entity

Attributes
  ↓
Data / State

Methods
  ↓
Behavior

self
  ↓
Current Object
```

This foundation will be used throughout the upcoming OOP lectures and later when we move into **LLD/System Design**.