# OOP — Lecture 4
# Encapsulation & Access Control

> **Goal:** Understand encapsulation, public/protected/private attributes, name mangling, getters/setters, and `@property`.
>
> This lecture is important for **Python interviews, backend development, DSA implementations, and especially LLD**.

## 1. What Is Encapsulation?

**Encapsulation** means keeping an object's data and the methods that operate on that data together inside a class, while controlling how the internal data can be accessed or modified.

Example:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

Here:

```text
BankAccount
    │
    ├── Data
    │    └── balance
    │
    └── Behavior
         └── deposit()
```

The class owns both:

```text
Data + Behavior
```

But encapsulation is not just about putting data and methods inside a class.

A major purpose is:

> **Control how the object's internal state is accessed and changed.**

---

# 2. Why Do We Need Encapsulation?

Suppose we have:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
```

Now someone can do:

```python
account = BankAccount(10000)

account.balance = -50000
```

The object is now in an invalid state.

A bank account should not normally have:

```text
balance = -50000
```

if negative balances are not allowed by our business rules.

Encapsulation allows us to control such changes.

Instead of allowing arbitrary modification:

```python
account.balance = -50000
```

we can provide controlled behavior:

```python
account.deposit(5000)
account.withdraw(2000)
```

and validate the input.

---

# 3. Core Idea of Encapsulation

Think:

```text
Without Encapsulation

Object
  │
  ├── Data
  │     ↑
  │     │
  │   Anyone can directly modify
  │
  └── Methods
```

With better encapsulation:

```text
Object
  │
  ├── Internal Data
  │
  └── Public Methods
          │
          ↓
       Validation
          │
          ↓
      State Change
```

The outside world interacts with the object through controlled operations.

---

# 4. Public Attributes

In Python, attributes are public by default.

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

`name` is public.

We can directly access it:

```python
student = Student("Nitin")

print(student.name)

student.name = "Rahul"
```

This is completely allowed.

There is no keyword like:

```text
public
```

required in Python.

---

# 5. Public Means Directly Accessible

Example:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
```

Anyone with the object can do:

```python
account.balance
```

or:

```python
account.balance = 5000
```

So:

```text
public attribute
      ↓
directly accessible
      ↓
directly modifiable
```

This is simple and sometimes exactly what we want.

Encapsulation does **not** mean every attribute must be hidden.

---

# 6. Protected Convention: `_variable`

Python uses a naming convention for attributes that are intended for internal/protected use:

```python
_variable
```

Example:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
```

The `_` means:

> "This is intended for internal use; please don't access it directly unless you know what you're doing."

But Python does **not** actually prevent access.

You can still do:

```python
account._balance
```

and:

```python
account._balance = 5000
```

So `_balance` is **not truly private**.

---

# 7. Important: `_variable` Is a Convention

This:

```python
self._balance
```

does not create a security mechanism.

Python trusts the programmer.

Think:

```text
_balance
   ↓
"Internal use"
   ↓
Convention
   ↓
Not enforced by Python
```

This is different from languages that provide strict access modifiers.

---

# 8. Private Attributes: `__variable`

Python also provides a stronger mechanism using **double underscore**:

```python
__variable
```

Example:

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
```

Now:

```python
account = BankAccount(10000)
```

Trying:

```python
print(account.__balance)
```

will raise an `AttributeError`.

This is because Python performs **name mangling**.

---

# 9. Name Mangling

When Python sees:

```python
self.__balance
```

inside:

```python
class BankAccount:
```

Python internally transforms the attribute name approximately into:

```python
self._BankAccount__balance
```

So:

```text
__balance
    ↓
_BankAccount__balance
```

This is called **name mangling**.

---

# 10. Why Does Python Use Name Mangling?

Name mangling mainly helps:

- avoid accidental name collisions
- protect internal implementation details from accidental access
- make subclassing safer

It is **not a security mechanism**.

Python does not provide strict private memory like:

```text
"Nobody can ever access this."
```

Instead, Python uses conventions and name mangling.

---

# 11. Example of Name Mangling

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance


account = BankAccount(10000)
```

This:

```python
account.__balance
```

does not work normally.

But internally the attribute is approximately:

```python
account._BankAccount__balance
```

So:

```python
print(account._BankAccount__balance)
```

can access it.

This demonstrates an important point:

> `__variable` is not truly private. It is name-mangled.

You generally should **not** bypass the intended interface like this in normal application code.

---

# 12. `_variable` vs `__variable`

This is a common interview question.

| Syntax | Meaning | Python Enforcement |
|---|---|---|
| `variable` | Public | No restriction |
| `_variable` | Internal/protected convention | No restriction |
| `__variable` | Private-like/name-mangled | Name mangling |

Remember:

```text
x
↓
Public

_x
↓
Internal-use convention

__x
↓
Name mangling
```

---

# 13. Encapsulation With Methods

One of the most useful ways to implement encapsulation is to control state changes through methods.

Example:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            return

        if amount <= self._balance:
            self._balance -= amount
```

Now instead of directly modifying:

```python
account._balance
```

the intended interface is:

```python
account.deposit(500)
account.withdraw(200)
```

---

# 14. Encapsulation and Validation

This is where encapsulation becomes practically useful.

Suppose:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
```

We can control changes:

```python
def withdraw(self, amount):
    if amount > self._balance:
        return

    self._balance -= amount
```

Now the class can enforce an invariant:

```text
balance should not become invalid
```

This is an important LLD concept.

---

# 15. What Is an Invariant?

An **invariant** is a condition that should remain true for an object.

For example, for a bank account:

```text
balance >= 0
```

might be an invariant.

For a student:

```text
marks must be between 0 and 100
```

might be an invariant.

For a parking spot:

```text
A spot can contain at most one vehicle
```

might be an invariant.

Encapsulation helps the class maintain these rules.

---

# 16. Example: Student Marks

Without controlled access:

```python
class Student:
    def __init__(self, marks):
        self.marks = marks
```

Someone can do:

```python
student.marks = 500
```

which may be invalid.

Better:

```python
class Student:
    def __init__(self, marks):
        self._marks = 0
        self.set_marks(marks)

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks
```

Now the class controls the valid range.

---

# 17. Getters

A **getter** is a method used to retrieve internal data.

Example:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance
```

Usage:

```python
account = BankAccount(10000)

print(account.get_balance())
```

Output:

```text
10000
```

---

# 18. Setters

A **setter** is a method used to modify internal data in a controlled way.

Example:

```python
class Student:
    def __init__(self, marks):
        self._marks = marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks
```

Usage:

```python
student.set_marks(90)
```

The setter can validate the value before changing the state.

---

# 19. Traditional Getter/Setter Pattern

Example:

```python
class Employee:
    def __init__(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        if salary >= 0:
            self._salary = salary
```

Usage:

```python
employee = Employee(50000)

print(employee.get_salary())

employee.set_salary(60000)
```

This pattern exists in many programming languages.

But Python provides a more Pythonic approach.

---

# 20. `@property`

Python provides:

```python
@property
```

to expose method-based behavior like an attribute.

Example:

```python
class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary
```

Now:

```python
employee = Employee(50000)

print(employee.salary)
```

Notice:

```python
employee.salary
```

instead of:

```python
employee.get_salary()
```

The method behaves like an attribute from the caller's perspective.

---

# 21. Why Use `@property`?

Suppose initially we have:

```python
class Employee:
    def __init__(self, salary):
        self.salary = salary
```

Later we want validation or calculated logic.

Changing every caller from:

```python
employee.salary
```

to:

```python
employee.get_salary()
```

would be inconvenient.

With `@property`, we can keep:

```python
employee.salary
```

while controlling how the value is retrieved.

This makes `@property` very useful for clean class APIs.

---

# 22. Property Getter

Example:

```python
class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks
```

Usage:

```python
student = Student(90)

print(student.marks)
```

Output:

```text
90
```

The method:

```python
def marks(self):
```

is accessed like:

```python
student.marks
```

because of:

```python
@property
```

---

# 23. Property Setter

We can also control assignment using:

```python
@marks.setter
```

Example:

```python
class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
```

Now:

```python
student = Student(80)

student.marks = 90
```

works.

But:

```python
student.marks = 150
```

will not update the value because it fails validation.

---

# 24. How `@property` Works Conceptually

When we write:

```python
student.marks
```

Python executes the property getter:

```python
@property
def marks(self):
    return self._marks
```

When we write:

```python
student.marks = 90
```

Python executes the property setter:

```python
@marks.setter
def marks(self, value):
    ...
```

Mental model:

```text
student.marks
      ↓
@property getter
      ↓
return self._marks
```

and:

```text
student.marks = 90
      ↓
@property setter
      ↓
validation
      ↓
self._marks = 90
```

---

# 25. Read-Only Property

Sometimes we want data to be readable but not directly changeable.

Example:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius * self._radius
```

Now:

```python
circle = Circle(5)

print(circle.area)
```

works.

But:

```python
circle.area = 100
```

doesn't work because no setter was defined.

This is useful for **computed/read-only values**.

---

# 26. Computed Properties

A property doesn't have to simply return stored data.

It can calculate something.

Example:

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width
```

Usage:

```python
rectangle = Rectangle(10, 5)

print(rectangle.area)
```

Output:

```text
50
```

There is no stored `area` attribute.

It is calculated when accessed.

---

# 27. Property With Validation

A very common practical pattern:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = value
```

Now:

```python
account = BankAccount(10000)
```

works.

But:

```python
account.balance = -500
```

raises an error.

The object protects its valid state.

---

# 28. Why Do We Use `_balance` Inside the Property?

Consider:

```python
@property
def balance(self):
    return self._balance
```

and:

```python
@balance.setter
def balance(self, value):
    self._balance = value
```

We cannot use:

```python
self.balance = value
```

inside the setter.

That would call the setter again:

```text
setter
  ↓
self.balance = value
  ↓
setter
  ↓
self.balance = value
  ↓
...
```

This would cause infinite recursion.

Therefore we store the actual value in:

```python
self._balance
```

and expose:

```python
balance
```

as the property.

---

# 29. Important Property Pattern

Remember this pattern:

```python
class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Invalid balance")

        self._balance = value
```

Usage:

```python
account = Account(1000)

print(account.balance)

account.balance = 2000
```

From outside, it looks like normal attribute access.

Internally, Python executes methods.

---

# 30. Encapsulation Does Not Mean "Hide Everything"

This is an important design principle.

Bad thinking:

```text
Everything must be private.
```

Better thinking:

```text
Hide implementation details that should not be manipulated directly.
Expose a clean interface for necessary operations.
```

For example:

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()
```

The important interface is:

```text
push()
pop()
```

The internal storage:

```text
_items
```

is an implementation detail.

---

# 31. Encapsulation in DSA

Consider a stack.

Without a class:

```python
stack = []

stack.append(10)
stack.append(20)
stack.pop()
```

Anyone can directly manipulate the list.

With a class:

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if not self._items:
            return None

        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0
```

Now the class controls how the stack behaves.

The user interacts with:

```text
push()
pop()
is_empty()
```

rather than needing to know how the stack stores its data.

---

# 32. Encapsulation in Backend Development

Imagine an `Order` class.

```python
class Order:
    def __init__(self):
        self._status = "pending"

    def cancel(self):
        if self._status == "pending":
            self._status = "cancelled"
```

Instead of allowing:

```python
order._status = "cancelled"
```

the intended operation is:

```python
order.cancel()
```

Why?

Because business rules can be placed inside the method.

For example:

```text
Can a shipped order be cancelled?
Can a delivered order be cancelled?
Can a paid order be refunded?
```

The class can enforce these rules.

---

# 33. Encapsulation in LLD ⭐⭐⭐

This is where encapsulation becomes extremely important.

Suppose we design:

```text
BankAccount
ParkingSpot
Vehicle
Order
Payment
Elevator
```

Each object should protect its own valid state.

For example:

```python
class ParkingSpot:
    def __init__(self):
        self._vehicle = None

    def park(self, vehicle):
        if self._vehicle is not None:
            return False

        self._vehicle = vehicle
        return True

    def remove_vehicle(self):
        vehicle = self._vehicle
        self._vehicle = None
        return vehicle
```

The class controls:

```text
Who can occupy the spot?
Can another vehicle enter?
How is the vehicle removed?
```

This is much better than allowing arbitrary external modification.

---

# 34. Encapsulation and Class Responsibility

A good LLD class should own the rules related to its state.

For example:

```text
BankAccount
    ↓
should manage account-related rules

ParkingSpot
    ↓
should manage whether it is occupied

Order
    ↓
should manage valid order transitions
```

Instead of:

```text
External code
    ↓
directly changes everything
```

we want:

```text
Object
   ↓
owns its state
   ↓
owns relevant behavior
   ↓
enforces its rules
```

This is a major LLD mindset.

---

# 35. Encapsulation vs Abstraction

These concepts are related but different.

### Encapsulation

Focuses on:

```text
How data and behavior are packaged
and how access to internal state is controlled.
```

### Abstraction

Focuses on:

```text
What the user needs to know
while hiding unnecessary implementation details.
```

Simple mental model:

```text
Encapsulation
    ↓
Protect/control state


Abstraction
    ↓
Hide unnecessary complexity
```

We will study abstraction separately.

---

# 36. Encapsulation vs Data Hiding

These terms are often used together but are not exactly identical.

### Encapsulation

Bundling:

```text
data + behavior
```

inside a class and controlling interaction with the object.

### Data Hiding

Restricting or discouraging direct access to internal implementation details.

In Python:

```python
_balance
```

and:

```python
__balance
```

help implement data-hiding conventions/mechanisms.

---

# 37. Public vs Protected vs Private

A useful mental model:

```text
public
   ↓
Anyone can access

_variable
   ↓
"Please treat as internal"
Convention

__variable
   ↓
Name mangling
Private-like implementation detail
```

But remember:

> Python generally relies on programmer discipline rather than strict access modifiers.

---

# 38. Important: Don't Overuse `__private`

You don't need to write:

```python
self.__name
self.__age
self.__salary
self.__email
```

for every attribute.

Often this is enough:

```python
self._balance
```

combined with a clean public API.

Use double underscore when name mangling provides a meaningful benefit, especially to avoid accidental name collisions in inheritance.

---

# 39. Example: Better Class Design

### Less controlled

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
```

Anyone can directly change:

```python
account.balance = -100000
```

### Better

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = value
```

Now:

```python
account.balance = 5000
```

is controlled by the setter.

---

# 40. Another Example: Temperature

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")

        self._celsius = value
```

Now:

```python
temperature = Temperature(25)

temperature.celsius = 30
```

works.

But:

```python
temperature.celsius = -500
```

raises an error.

The class protects its invariant.

---

# 41. Property vs Getter/Setter Methods

Traditional style:

```python
class Student:
    def get_marks(self):
        return self._marks

    def set_marks(self, marks):
        self._marks = marks
```

Usage:

```python
student.get_marks()
student.set_marks(90)
```

Pythonic property style:

```python
class Student:

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        self._marks = value
```

Usage:

```python
student.marks
student.marks = 90
```

For Python code, `@property` is often cleaner when attribute-like access makes sense.

---

# 42. When Should You Use `@property`?

Good use cases:

### 1. Validation

```python
@property
def age(self):
    return self._age

@age.setter
def age(self, value):
    if value < 0:
        raise ValueError()
    self._age = value
```

### 2. Computed values

```python
@property
def area(self):
    return self.length * self.width
```

### 3. Read-only values

```python
@property
def id(self):
    return self._id
```

### 4. Preserving a clean API

You can add internal logic without changing:

```python
object.attribute
```

into:

```python
object.get_attribute()
```

---

# 43. When Not to Use `@property`

Don't turn every method into a property.

If an operation:

- performs a significant action
- changes state substantially
- has side effects
- may be expensive
- behaves more like an action

a normal method is often clearer.

For example:

```python
account.withdraw(500)
```

is better than:

```python
account.withdraw_amount = 500
```

because withdrawal is an action.

Think:

```text
Property
→ looks like data

Method
→ represents behavior/action
```

---

# 44. Encapsulation Design Rule

A useful rule for LLD:

> **Expose what other objects need; keep implementation details internal.**

For example:

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()
```

External code needs:

```text
push
pop
```

It doesn't need to know:

```text
how the stack stores its data
```

This separation makes the design easier to change later.

---

# 45. Example: Changing Internal Implementation

Suppose initially:

```python
class Stack:
    def __init__(self):
        self._items = []
```

Later, we change the implementation to another internal structure.

If outside code only uses:

```python
stack.push()
stack.pop()
```

the outside code doesn't need to change.

This is one of the practical benefits of encapsulation.

```text
Public Interface
       ↓
push()
pop()
       ↓
Internal Implementation
       ↓
Can change
```

---

# 46. Common Mistake #1

Thinking:

```text
_private = impossible to access
```

This is false in Python.

For:

```python
self._balance
```

there is no actual access restriction.

For:

```python
self.__balance
```

Python uses name mangling.

But it can still be accessed using the mangled name.

Therefore:

```text
Python privacy ≠ absolute security
```

---

# 47. Common Mistake #2

Using `__variable` everywhere.

Don't do:

```python
class Student:
    def __init__(self, name, age, marks, email):
        self.__name = name
        self.__age = age
        self.__marks = marks
        self.__email = email
```

just because you learned "private variables."

Choose the access design based on the class's actual requirements.

---

# 48. Common Mistake #3

Creating Getters and Setters for Everything

You don't need:

```python
get_name()
set_name()
get_age()
set_age()
```

for every simple attribute.

Python allows direct attributes when no special control is needed.

Use properties or methods when there is a reason:

```text
validation
computed values
read-only behavior
controlled state changes
API stability
```

---

# 49. Common Mistake #4

Using a Setter When a Behavior Method Is Better

Instead of:

```python
account.balance = account.balance - 500
```

or exposing a setter that allows arbitrary balance changes, prefer:

```python
account.withdraw(500)
```

Why?

Because:

```text
withdraw()
```

represents a business operation.

It can enforce rules such as:

```text
sufficient balance
transaction limits
account status
```

This is much more useful in LLD.

---

# 50. Common Mistake #5

Putting Business Logic Outside the Object

Bad design:

```python
account.balance -= 500
```

everywhere in the application.

Better:

```python
account.withdraw(500)
```

The `BankAccount` class owns the logic related to withdrawing money.

This keeps responsibilities clear.

---

# 51. Interview Question: What Is Encapsulation?

### Answer

Encapsulation is the practice of bundling data and the behavior that operates on that data inside a class and controlling how the object's internal state is accessed or modified.

In Python, encapsulation is commonly implemented using:

- classes
- methods
- `_name` conventions
- `__name` name mangling
- properties
- controlled state-changing methods

---

# 52. Interview Question: Is Python Truly Private?

Python does not have strict private access control in the same way some languages do.

For example:

```python
self.__balance
```

uses name mangling:

```text
_BankAccount__balance
```

So it is better described as **private-like/name-mangled**, not absolute security.

---

# 53. Interview Question: Difference Between `_x` and `__x`

### `_x`

A naming convention indicating:

> "This is intended for internal/protected use."

Python does not enforce it.

### `__x`

Triggers name mangling.

For:

```python
class A:
    def __init__(self):
        self.__x = 10
```

Python internally stores it approximately as:

```python
self._A__x
```

---

# 54. Interview Question: What Is Name Mangling?

Name mangling is Python's mechanism of changing the name of attributes beginning with double underscores inside a class.

Example:

```python
class Student:
    def __init__(self):
        self.__marks = 90
```

Internally:

```text
__marks
   ↓
_Student__marks
```

It mainly helps prevent accidental name conflicts, especially with inheritance.

---

# 55. Interview Question: What Is `@property`?

`@property` allows a method to be accessed like an attribute.

Example:

```python
class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks
```

Now:

```python
student.marks
```

calls the property getter.

It is useful for:

- validation
- computed values
- read-only attributes
- maintaining a clean API

---

# 56. Interview Question: What Is a Property Setter?

A property setter allows assignment to a property to trigger custom logic.

Example:

```python
class Student:
    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
```

Now:

```python
student.marks = 90
```

runs the setter.

---

# 57. Interview Question: Why Use `_balance` Instead of `balance` Inside the Setter?

Because:

```python
@balance.setter
def balance(self, value):
    self.balance = value
```

would call the setter again.

That creates recursive calls.

Instead:

```python
@balance.setter
def balance(self, value):
    self._balance = value
```

stores the actual value separately.

Mental model:

```text
balance
   ↓
Public interface

_balance
   ↓
Internal storage
```

---

# 58. Interview Question: Encapsulation vs Abstraction

### Encapsulation

Focuses on:

```text
Bundling data + behavior
and controlling access to state.
```

### Abstraction

Focuses on:

```text
Exposing essential behavior
while hiding unnecessary implementation details.
```

They work together, but they are not the same concept.

---

# 59. Interview Question: Why Is Encapsulation Important in LLD?

Encapsulation helps:

- protect object state
- enforce business rules
- maintain invariants
- reduce coupling
- hide implementation details
- make classes easier to modify
- keep responsibilities inside the correct class

Example:

```python
account.withdraw(500)
```

is better than having every part of the system manipulate:

```python
account.balance
```

directly.

---

# 60. LLD Mental Model

When designing a class, ask:

```text
What state does this object own?
        ↓
What rules must always be true?
        ↓
Who should be allowed to change that state?
        ↓
What operations should I expose?
        ↓
What implementation details should remain internal?
```

This is a very useful LLD mindset.

---

# 61. Complete Example

```python
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount
```

Usage:

```python
account = BankAccount("Nitin", 10000)

print(account.balance)

account.deposit(5000)

account.withdraw(2000)

print(account.balance)
```

The important design is:

```text
owner
   ↓
Public attribute

_balance
   ↓
Internal state

balance
   ↓
Controlled property

deposit()
   ↓
Controlled state change

withdraw()
   ↓
Controlled state change
```

---

# 62. Final Encapsulation Mental Model

```text
                    OBJECT
                       │
              ┌────────┴────────┐
              │                 │
          Internal State      Public API
              │                 │
          _balance          deposit()
          _items             withdraw()
          _status             push()
              │                 pop()
              │
              ↓
        Controlled Access
              │
              ↓
          Validation
              │
              ↓
        Valid Object State
```

And:

```text
public
   ↓
Directly accessible

_variable
   ↓
Internal-use convention

__variable
   ↓
Name mangling

@property
   ↓
Attribute-like controlled access

Methods
   ↓
Controlled behavior/state changes
```

# 63. Quick Revision

### Encapsulation

```text
Data + Behavior
      ↓
Class
      ↓
Controlled interaction with state
```

### Public

```python
self.name
```

Normal public attribute.

### Protected Convention

```python
self._name
```

Internal-use convention; not enforced.

### Private-like

```python
self.__name
```

Name mangling is applied.

### Getter

```python
def get_value(self):
    return self._value
```

### Setter

```python
def set_value(self, value):
    self._value = value
```

### Property

```python
@property
def value(self):
    return self._value
```

### Property Setter

```python
@value.setter
def value(self, value):
    self._value = value
```

### LLD Rule

```text
Object owns its state
        ↓
Object owns its rules
        ↓
Expose necessary operations
        ↓
Hide unnecessary implementation details
```

# 64. Must-Know Interview Checklist

Before moving to the next lecture, you should be able to explain:

- What is encapsulation?
- Why do we need encapsulation?
- What is a public attribute?
- What does `_variable` mean in Python?
- Is `_variable` actually protected?
- What does `__variable` mean?
- What is name mangling?
- Is `__variable` truly private?
- Difference between `_x` and `__x`
- What is a getter?
- What is a setter?
- What is `@property`?
- What is a property setter?
- Why use `_value` inside a property?
- What is an invariant?
- How does encapsulation help maintain valid object state?
- Difference between encapsulation and abstraction?
- Why is encapsulation important in LLD?
- When should you use a method instead of a setter?
- Why shouldn't every attribute automatically be made private?

# OOP Lecture 4 Complete