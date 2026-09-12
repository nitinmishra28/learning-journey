# OOP — Lecture 3
# Instance vs Class Data & Methods

> **Goal:** Understand how Python stores data and behavior at the object level and class level, and when to use instance methods, class methods, and static methods.
>
> This lecture is important for **Python interviews, backend development, DSA implementations, and LLD**.

## 1. What We Already Know

From the previous lectures:

```text
Class
   ↓
Blueprint

Object
   ↓
Actual instance of the class

Attributes
   ↓
Data / State

Methods
   ↓
Behavior

self
   ↓
Current object
```

Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(self.name, self.age)


s1 = Student("Nitin", 22)
s2 = Student("Rahul", 21)
```

Here:

```text
Student
   │
   ├── s1 → name="Nitin", age=22
   │
   └── s2 → name="Rahul", age=21
```

Each object has its **own state**.

Now we need to understand:

- What belongs to an object?
- What belongs to the class?
- What is an instance method?
- What is a class method?
- What is a static method?
- When should we use each one?

## 2. Instance Attributes

An **instance attribute** is data that belongs to a particular object.

Usually, instance attributes are created using:

```python
self.attribute
```

Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Create objects:

```python
s1 = Student("Nitin", 22)
s2 = Student("Rahul", 21)
```

Now:

```text
s1.name → "Nitin"
s1.age  → 22

s2.name → "Rahul"
s2.age  → 21
```

The objects have different values.

## 3. Why Are They Called Instance Attributes?

Because they belong to an **instance** of a class.

Remember:

```python
s1 = Student("Nitin", 22)
```

`s1` is an instance/object of `Student`.

Therefore:

```python
s1.name
s1.age
```

are instance attributes.

Another object:

```python
s2 = Student("Rahul", 21)
```

has its own:

```python
s2.name
s2.age
```

## 4. Object State

The collection of data stored inside an object represents its **state**.

Example:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
```

Object:

```python
account = BankAccount("Nitin", 10000)
```

State:

```text
owner   → "Nitin"
balance → 10000
```

If:

```python
account.balance += 5000
```

then:

```text
owner   → "Nitin"
balance → 15000
```

The object's state changed.

This idea is extremely important in OOP and LLD.

## 5. Instance Attributes Are Usually Created in `__init__`

Common pattern:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
```

Every object gets its own:

```text
name
salary
```

Example:

```python
e1 = Employee("A", 50000)
e2 = Employee("B", 70000)
```

Conceptually:

```text
e1
 ├── name = "A"
 └── salary = 50000

e2
 ├── name = "B"
 └── salary = 70000
```

## 6. Class Attributes

A **class attribute** belongs to the class rather than being separately created for every object.

Example:

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name
```

Here:

```python
school
```

is a class attribute.

It is defined directly inside the class body:

```python
class Student:
    school = "ABC School"
```

not inside `__init__`.

## 7. Instance Attribute vs Class Attribute

Consider:

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name
```

Create:

```python
s1 = Student("Nitin")
s2 = Student("Rahul")
```

Conceptually:

```text
Student class
    │
    └── school = "ABC School"

s1
    └── name = "Nitin"

s2
    └── name = "Rahul"
```

Both objects can access:

```python
print(s1.school)
print(s2.school)
```

Output:

```text
ABC School
ABC School
```

But `school` is class-level data.

## 8. When Should We Use Class Attributes?

Use a class attribute when a value is conceptually **shared by all objects**.

Example:

```python
class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name
```

All employees belong to the same company:

```python
e1 = Employee("A")
e2 = Employee("B")
```

Both can access:

```python
e1.company
e2.company
```

## 9. Another Example

```python
class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand
```

Here:

```text
wheels → class attribute
brand  → instance attribute
```

Because:

```text
Every car has 4 wheels
```

while:

```text
Different cars have different brands
```

## 10. Important Rule

Ask:

> **Is this value specific to each object or shared conceptually by the class?**

If specific to each object:

```python
self.value
```

If shared by the class:

```python
Class.value
```

Example:

```python
class Student:
    school = "ABC"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
```

Here:

```text
school  → shared
name    → object-specific
roll_no → object-specific
```

## 11. Class Attribute Access

A class attribute can be accessed through the class:

```python
Student.school
```

and usually through an instance:

```python
s1.school
```

Example:

```python
class Student:
    school = "ABC"


s1 = Student()

print(Student.school)
print(s1.school)
```

Output:

```text
ABC
ABC
```

But these two accesses are not conceptually the same.

## 12. Attribute Lookup

When Python evaluates:

```python
s1.school
```

Python searches for the attribute.

For normal attribute access, an important basic mental model is:

```text
object
   ↓
instance attributes
   ↓
class attributes
   ↓
relevant inheritance hierarchy
```

So if `school` is not found directly on the object, Python can find it on the class.

Example:

```python
class Student:
    school = "ABC"

s1 = Student()
```

There may be no `school` stored directly on `s1`.

Still:

```python
s1.school
```

works because Python can find it through the class.

## 13. Instance Attribute Can Shadow Class Attribute

This is very important for interviews.

Example:

```python
class Student:
    school = "ABC"

    def __init__(self, name):
        self.name = name


s1 = Student("Nitin")

s1.school = "XYZ"
```

Now:

```python
print(s1.school)
```

Output:

```text
XYZ
```

while:

```python
print(Student.school)
```

Output:

```text
ABC
```

The instance now has its own `school` attribute.

Conceptually:

```text
Student
 └── school = "ABC"

s1
 ├── name = "Nitin"
 └── school = "XYZ"
```

The instance attribute **shadows** the class attribute for that object.

## 14. Class Attribute Mutation

Example:

```python
class Student:
    school = "ABC"
```

Then:

```python
Student.school = "XYZ"
```

Now:

```python
s1 = Student()
s2 = Student()

print(s1.school)
print(s2.school)
```

Output:

```text
XYZ
XYZ
```

because both are reading the class attribute.

## 15. Important Class Attribute Trap: Mutable Data

Be careful with mutable class attributes.

Bad example:

```python
class Student:
    subjects = []

    def __init__(self, name):
        self.name = name
```

Now:

```python
s1 = Student("Nitin")
s2 = Student("Rahul")

s1.subjects.append("Python")
```

You may expect:

```text
s1.subjects → ["Python"]
s2.subjects → []
```

But that's not what happens.

Both may see:

```text
["Python"]
```

because the list is shared at the class level.

## 16. Why This Happens

The class has:

```python
subjects = []
```

There is one shared list associated with the class.

Objects can access that same list unless they have their own instance attribute.

Conceptually:

```text
Student
   │
   └── subjects → []

s1 ──────────────┐
                 ↓
              same list

s2 ──────────────┘
```

Therefore:

```python
s1.subjects.append("Python")
```

mutates the shared list.

## 17. Correct Way for Per-Object Mutable Data

If every object should have its own list:

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = []
```

Now:

```python
s1 = Student("Nitin")
s2 = Student("Rahul")

s1.subjects.append("Python")
```

Result:

```text
s1.subjects → ["Python"]
s2.subjects → []
```

This is the correct design when the data belongs to each object.

## 18. Instance Methods

An **instance method** operates on a particular object.

It normally takes:

```python
self
```

as the first parameter.

Example:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

Call:

```python
account = BankAccount(1000)

account.deposit(500)
```

Now:

```text
balance = 1500
```

The method operates on the state of `account`.

## 19. Why `self`?

`self` represents the current object.

Example:

```python
account.deposit(500)
```

Conceptually, Python uses the object when calling the method.

You can think of:

```python
account.deposit(500)
```

roughly as:

```python
BankAccount.deposit(account, 500)
```

So inside:

```python
def deposit(self, amount):
```

`self` refers to:

```text
account
```

## 20. Instance Method Example

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return self.marks >= 40
```

Usage:

```python
s1 = Student("Nitin", 80)
s2 = Student("Rahul", 30)

print(s1.is_passed())
print(s2.is_passed())
```

Output:

```text
True
False
```

The method works with the state of the specific object.

## 21. Class Methods

A **class method** operates at the class level.

It is created using:

```python
@classmethod
```

and takes:

```python
cls
```

as the first parameter.

Example:

```python
class Student:
    school = "ABC"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
```

Call:

```python
Student.change_school("XYZ")
```

Now:

```python
print(Student.school)
```

Output:

```text
XYZ
```

## 22. `self` vs `cls`

This distinction is extremely important.

### Instance method

```python
def method(self):
```

`self` → current object

### Class method

```python
@classmethod
def method(cls):
```

`cls` → current class

Think:

```text
self → object
cls  → class
```

## 23. Instance Method Example

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(self.name)
```

The method needs a specific employee.

```python
e1.introduce()
```

uses:

```text
e1
```

## 24. Class Method Example

```python
class Employee:
    company = "ABC"

    @classmethod
    def change_company(cls, company):
        cls.company = company
```

This operation changes class-level information.

```python
Employee.change_company("XYZ")
```

## 25. When Should We Use a Class Method?

Use a class method when the operation needs to work with the **class itself** rather than one particular object.

Common use cases:

1. Modifying class-level state
2. Alternative constructors / factory methods
3. Creating objects from another representation

Example:

```python
class Employee:
    company = "ABC"

    @classmethod
    def change_company(cls, company):
        cls.company = company
```

## 26. Class Methods as Factory Methods ⭐

This is especially useful for **LLD**.

Suppose:

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

We normally create:

```python
user = User("Nitin", 22)
```

But suppose data comes as a string:

```text
"Nitin,22"
```

We can create a class method:

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))
```

Now:

```python
user = User.from_string("Nitin,22")
```

This creates a `User`.

## 27. Why Use `cls` Instead of `User`?

Notice:

```python
return cls(name, int(age))
```

instead of:

```python
return User(name, int(age))
```

Using `cls` allows the method to work properly with subclasses as well.

This makes class methods useful for:

- Factory methods
- Alternative constructors
- Extensible class designs
- LLD

You don't need to master advanced inheritance yet; just remember this reason.

## 28. Static Methods

A **static method** belongs logically to the class but does not need:

```text
self
```

or:

```text
cls
```

It is defined using:

```python
@staticmethod
```

Example:

```python
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b
```

Call:

```python
MathUtils.add(10, 20)
```

Output:

```text
30
```

## 29. Why Use Static Methods?

Use a static method when a function:

- logically belongs to the class
- does not need object state
- does not need class state

Example:

```python
class Validator:

    @staticmethod
    def is_valid_age(age):
        return age >= 18
```

It doesn't need:

```text
self
```

or:

```text
cls
```

Therefore:

```python
Validator.is_valid_age(22)
```

## 30. Static Method Example

```python
class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9 / 5) + 32
```

Usage:

```python
print(Temperature.celsius_to_fahrenheit(100))
```

Output:

```text
212.0
```

There is no object state involved.

## 31. Instance vs Class vs Static Method

This is one of the most important interview topics from this lecture.

| Method | First Parameter | Works With | Typical Use |
|---|---|---|---|
| Instance Method | `self` | Object | Object state/behavior |
| Class Method | `cls` | Class | Class-level behavior/factory |
| Static Method | None | Neither automatically | Utility logic |

Mental model:

```text
Instance Method
      ↓
     self
      ↓
    Object


Class Method
      ↓
     cls
      ↓
    Class


Static Method
      ↓
   neither
      ↓
 independent logic
```

## 32. Complete Example

```python
class Employee:

    company = "ABC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method
    def show_details(self):
        print(self.name, self.salary)

    # Class method
    @classmethod
    def change_company(cls, company):
        cls.company = company

    # Static method
    @staticmethod
    def is_valid_salary(salary):
        return salary >= 0
```

Usage:

```python
e1 = Employee("Nitin", 50000)

e1.show_details()

Employee.change_company("XYZ")

print(Employee.company)

print(Employee.is_valid_salary(50000))
```

## 33. Analyze the Example

### Instance method

```python
def show_details(self):
```

Needs:

```text
specific employee
```

because it uses:

```python
self.name
self.salary
```

### Class method

```python
@classmethod
def change_company(cls, company):
```

Needs:

```text
class
```

because it changes:

```python
cls.company
```

### Static method

```python
@staticmethod
def is_valid_salary(salary):
```

Needs:

```text
neither object nor class
```

It only performs a calculation/check.

## 34. Attribute Namespace

Python objects and classes have namespaces.

For an object:

```python
obj.__dict__
```

can show its instance attributes.

Example:

```python
class Student:
    school = "ABC"

    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Nitin", 22)

print(s1.__dict__)
```

You will see something like:

```python
{
    'name': 'Nitin',
    'age': 22
}
```

Notice:

```text
school
```

is not stored in `s1`'s instance dictionary.

It is a class attribute.

## 35. Class Namespace

The class itself also has a namespace.

You may inspect:

```python
Student.__dict__
```

This contains class-level definitions and other class metadata.

For normal development, you generally don't need to manipulate `__dict__` directly.

But understanding it helps explain:

```text
instance attributes
vs
class attributes
```

and is useful in interviews.

## 36. `obj.__dict__` Mental Model

Example:

```python
class Student:
    school = "ABC"

    def __init__(self, name):
        self.name = name


s1 = Student("Nitin")
```

Think:

```text
Student class
 ├── school
 ├── __init__
 └── methods...

s1
 └── __dict__
      └── name = "Nitin"
```

So:

```python
s1.name
```

comes from the instance.

While:

```python
s1.school
```

can be found from the class.

## 37. Class Attribute vs Instance Attribute — Interview Example

Consider:

```python
class A:
    x = 10

    def __init__(self):
        self.y = 20


a = A()
```

Now:

```python
print(a.x)
print(a.y)
```

Output:

```text
10
20
```

Because:

```text
x → class attribute
y → instance attribute
```

## 38. What Happens If We Change `a.x`?

```python
a.x = 50
```

Now:

```python
print(a.x)
print(A.x)
```

Output:

```text
50
10
```

Why?

Because:

```python
a.x = 50
```

creates an instance attribute named `x`.

Conceptually:

```text
A
 └── x = 10

a
 ├── y = 20
 └── x = 50
```

The instance value shadows the class value.

## 39. What Happens If We Change `A.x`?

```python
A.x = 100
```

Then an object that does not have its own `x` will see:

```python
A.x
```

through class lookup.

Example:

```python
class A:
    x = 10

a = A()

A.x = 100

print(a.x)
```

Output:

```text
100
```

because `a` doesn't have its own `x`.

## 40. Important Difference: Assignment vs Mutation

This distinction becomes very important with class attributes.

Consider:

```python
class A:
    items = []
```

If:

```python
a = A()
a.items.append(10)
```

you mutate the shared list.

But:

```python
a.items = [10]
```

assigns a new instance attribute.

These are different operations.

### Mutation

```python
a.items.append(10)
```

Changes the existing object.

### Assignment

```python
a.items = [10]
```

Creates/sets an attribute on the instance.

## 41. DSA Connection

These concepts are useful when implementing data structures using classes.

Example:

```python
class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()
```

Here:

```text
items → instance attribute
push  → instance method
pop   → instance method
```

Why?

Because every stack needs its own storage.

```text
stack1 → [1, 2, 3]
stack2 → [10, 20]
```

They should not share the same list.

## 42. DSA Example: Linked List

```python
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
```

Here:

```text
value → instance attribute
next  → instance attribute
```

because every node has its own:

```text
value
next
```

## 43. DSA Example: Graph

```python
class Graph:

    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        self.adj[u] = self.adj.get(u, [])
        self.adj[u].append(v)
```

Again:

```text
adj → instance state
add_edge → instance method
```

because each graph object should maintain its own graph.

## 44. LLD Connection ⭐⭐⭐

These concepts become very important in LLD.

Suppose we design:

```text
ParkingLot
Vehicle
ParkingSpot
Ticket
Payment
```

Each object will have its own state.

Example:

```python
class ParkingSpot:

    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.vehicle = None

    def park(self, vehicle):
        self.vehicle = vehicle
```

Here:

```text
spot_id → instance state
vehicle → instance state
park()  → instance behavior
```

The object owns both:

```text
Data
 +
Behavior
```

This is one of the core ideas behind OOP-based LLD.

## 45. Choosing the Correct Method

When designing a method, ask:

### Question 1

> Does this method need a particular object's data?

Use:

```text
instance method
```

Example:

```python
account.deposit(100)
```

uses the state of a specific account.

### Question 2

> Does this method need class-level data or create objects through the class?

Use:

```text
@classmethod
```

Example:

```python
User.from_string("Nitin,22")
```

### Question 3

> Does this method need neither object nor class state?

Use:

```text
@staticmethod
```

Example:

```python
Validator.is_valid_age(22)
```

## 46. Simple Decision Tree

```text
Does method need object state?
        │
       Yes
        ↓
 Instance Method
      self


        No
        │
        ↓
Does method need class state
or act as an alternative constructor?
        │
       Yes
        ↓
 Class Method
      cls


        No
        ↓
 Static Method
   neither
```

## 47. Common Mistake #1

Putting shared data inside every object unnecessarily.

Example:

```python
class Employee:

    def __init__(self, name):
        self.name = name
        self.company = "ABC"
```

This is not always wrong.

But if `company` is truly class-level information shared by all employees, a class attribute may be more appropriate:

```python
class Employee:
    company = "ABC"

    def __init__(self, name):
        self.name = name
```

The design depends on whether the value is conceptually per-object or class-level.

## 48. Common Mistake #2

Using mutable class attributes for per-object state.

Avoid:

```python
class Stack:
    items = []
```

if every stack should have independent storage.

Prefer:

```python
class Stack:
    def __init__(self):
        self.items = []
```

## 49. Common Mistake #3

Using `@staticmethod` when the method actually needs object state.

Bad design:

```python
class BankAccount:

    @staticmethod
    def deposit(account, amount):
        account.balance += amount
```

This can work technically, but if the operation is naturally behavior of the account, an instance method is clearer:

```python
class BankAccount:

    def deposit(self, amount):
        self.balance += amount
```

Prefer the method type that communicates the responsibility clearly.

## 50. Common Mistake #4

Thinking `cls` means "class name".

`cls` is just a conventional parameter name.

This:

```python
@classmethod
def change(cls):
```

means:

```text
cls → current class
```

You could technically name it differently, but `cls` is the standard convention.

Similarly:

```python
self
```

is the standard convention for the current object.

## 51. Common Mistake #5

Thinking Static Method Is "Better" Because It Doesn't Need `self`

Not every method should be static.

Don't choose method type based on:

> "I can avoid self."

Choose based on responsibility.

```text
Object state required?
→ instance method

Class state required?
→ class method

Neither required?
→ static method
```

## 52. Interview Question: Difference Between Instance and Class Attribute

### Answer

An **instance attribute** belongs to a specific object and is usually created using:

```python
self.attribute
```

A **class attribute** belongs to the class and is shared through the class unless an instance provides/shadows that attribute.

Example:

```python
class Student:
    school = "ABC"

    def __init__(self, name):
        self.name = name
```

Here:

```text
school → class attribute
name   → instance attribute
```

## 53. Interview Question: What Is `self`?

`self` refers to the current object on which an instance method is operating.

Example:

```python
class Student:

    def show(self):
        print(self)
```

When:

```python
s1.show()
```

is called:

```text
self → s1
```

## 54. Interview Question: What Is `cls`?

`cls` refers to the current class inside a class method.

Example:

```python
class Student:

    @classmethod
    def create(cls):
        return cls()
```

Here:

```text
cls → Student
```

when called on `Student`.

## 55. Interview Question: Difference Between Instance, Class, and Static Methods

### Instance Method

```python
def method(self):
```

Works with object state.

### Class Method

```python
@classmethod
def method(cls):
```

Works with class state or acts as an alternative constructor.

### Static Method

```python
@staticmethod
def method():
```

Doesn't automatically receive object or class.

## 56. Interview Question: Can We Call a Class Method Using an Object?

Yes.

Example:

```python
class A:

    value = 10

    @classmethod
    def show(cls):
        print(cls.value)


a = A()

a.show()
```

It works because the class method receives the class as `cls`.

However, use the form that best communicates intent.

If the operation is class-level:

```python
A.show()
```

is often clearer.

## 57. Interview Question: Can We Call a Static Method Using an Object?

Yes.

Example:

```python
class Math:

    @staticmethod
    def add(a, b):
        return a + b


m = Math()

print(m.add(2, 3))
```

It works.

But because it doesn't depend on an object, calling:

```python
Math.add(2, 3)
```

usually communicates the intent better.

## 58. Interview Question: Why Use a Class Method as an Alternative Constructor?

Because a class method can create an object from a different input format.

Example:

```python
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))
```

Now:

```python
user = User.from_string("Nitin,22")
```

This keeps object creation logic organized inside the class.

## 59. Interview Question: What Happens Here?

```python
class A:
    x = 10

a = A()

a.x = 20

print(A.x)
print(a.x)
```

Output:

```text
10
20
```

Reason:

```python
a.x = 20
```

creates/shadows an instance attribute.

It does not change:

```python
A.x
```

## 60. Interview Question: What Is the Problem Here?

```python
class A:
    items = []

    def __init__(self):
        pass
```

If you do:

```python
a1 = A()
a2 = A()

a1.items.append(10)
```

both objects can observe the mutation because the list is shared at the class level.

For independent lists:

```python
class A:
    def __init__(self):
        self.items = []
```

## 61. Practical Design Example

Let's combine everything.

```python
class BankAccount:

    bank_name = "ABC Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    @classmethod
    def from_string(cls, data):
        owner, balance = data.split(",")
        return cls(owner, int(balance))

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0
```

## 62. Analyze the Example

### Class Attribute

```python
bank_name
```

Shared class-level information.

### Instance Attributes

```python
self.owner
self.balance
```

Each account has its own state.

### Instance Methods

```python
deposit()
withdraw()
```

Operate on a particular account.

### Class Method

```python
change_bank_name()
```

Changes class-level information.

### Factory/Class Method

```python
from_string()
```

Creates an account from another representation.

### Static Method

```python
is_valid_amount()
```

Pure validation logic that doesn't need account or class state.

## 63. DSA + Backend + LLD Relevance

### DSA

You will use instance state when implementing:

```text
Stack
Queue
Linked List
Tree
Graph
LRU Cache
Heap wrappers
```

Example:

```python
class Queue:
    def __init__(self):
        self.items = []
```

### Backend

You will encounter classes representing:

```text
User
Order
Product
Payment
Database objects
Services
Validators
Repositories
```

Different method types help separate responsibilities.

### LLD

This becomes even more important.

For example:

```text
ParkingLot
    ↓
has ParkingSpots

ParkingSpot
    ↓
has Vehicle

Vehicle
    ↓
has vehicle details
```

Each object maintains its own state and exposes behavior through methods.

This is the foundation for later topics such as:

```text
Encapsulation
Inheritance
Polymorphism
Abstraction
Composition
Aggregation
SOLID
Design Patterns
```

## 64. Quick Comparison Table

| Concept | Belongs To | Access | Example |
|---|---|---|---|
| Instance Attribute | Object | `self.x` | `self.balance` |
| Class Attribute | Class | `Class.x` | `Employee.company` |
| Instance Method | Object | `self` | `account.deposit()` |
| Class Method | Class | `cls` | `User.from_string()` |
| Static Method | Class namespace logically | Neither | `Validator.is_valid()` |

## 65. Quick Revision

### Instance Attribute

```python
self.name = name
```

Own data for each object.

### Class Attribute

```python
class Employee:
    company = "ABC"
```

Class-level/shared data.

### Instance Method

```python
def deposit(self, amount):
```

Works with object state.

### Class Method

```python
@classmethod
def change_company(cls, name):
```

Works with class state.

### Static Method

```python
@staticmethod
def is_valid(value):
```

Doesn't require object or class state.

### Factory Method

```python
@classmethod
def from_string(cls, data):
```

Alternative way to create an object.

## 66. Must-Know Interview Points

Before moving forward, make sure you can explain:

- What is an instance attribute?
- What is a class attribute?
- Difference between instance and class attributes?
- What is attribute lookup?
- What is attribute shadowing?
- Why can mutable class attributes be dangerous?
- What is `self`?
- What is `cls`?
- What is an instance method?
- What is a class method?
- What is a static method?
- Difference between instance/class/static methods?
- Why use `@classmethod`?
- What is a factory method?
- Why use `@staticmethod`?
- How does `obj.__dict__` help understand instance attributes?
- Why should per-object mutable state usually be created inside `__init__`?

## 67. Core Mental Model

```text
                CLASS
                  │
        ┌─────────┴─────────┐
        │                   │
   Class Attribute      Class Method
        │                   │
   Shared Data              cls
                            │
                            ↓
                    Class-level behavior


                OBJECT
                  │
        ┌─────────┴─────────┐
        │                   │
 Instance Attribute    Instance Method
        │                   │
     self.data              self
        │                   │
        └─────────┬─────────┘
                  ↓
             Object State


             STATIC METHOD
                  │
                  ↓
          Neither self nor cls
                  │
                  ↓
          Independent Utility
```

### Final Rule to Remember

```text
Need object data?
→ Instance Method → self

Need class data / alternative construction?
→ Class Method → cls

Need neither?
→ Static Method

Data belongs to one object?
→ Instance Attribute

Data is conceptually shared by the class?
→ Class Attribute
```

# OOP Lecture 3 Complete