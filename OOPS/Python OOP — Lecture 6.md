# OOP — Lecture 6
# Polymorphism

> **Goal:** Understand polymorphism, method overriding, duck typing, common interfaces, polymorphic behavior, and how polymorphism is used in real Python code and LLD.
>
> This lecture is important for **Python interviews, backend development, and especially LLD**.

## 1. What Is Polymorphism?

**Polymorphism** means:

> **One interface, multiple implementations.**

The same operation can behave differently depending on the object on which it is performed.

Example:

```python
class Dog:
    def speak(self):
        print("Bark")


class Cat:
    def speak(self):
        print("Meow")
```

Both classes have:

```python
speak()
```

but the behavior is different.

```python
dog = Dog()
cat = Cat()

dog.speak()
cat.speak()
```

Output:

```text
Bark
Meow
```

Same method name:

```text
speak()
```

Different behavior:

```text
Dog → Bark
Cat → Meow
```

This is polymorphism.

---

# 2. Core Idea

Think:

```text
             Common Interface
                    │
             ┌──────┴──────┐
             │             │
            Dog           Cat
             │             │
          speak()       speak()
             │             │
           Bark          Meow
```

The caller only needs to know:

```text
"I can call speak()."
```

It doesn't necessarily need to know the exact implementation.

---

# 3. Why Is Polymorphism Important?

Polymorphism helps us write code that works with different object types without constantly checking their exact type.

Without polymorphism:

```python
if type == Dog:
    ...
elif type == Cat:
    ...
elif type == Cow:
    ...
```

This can become difficult to maintain.

With polymorphism:

```python
animal.speak()
```

Each object decides how `speak()` behaves.

Mental model:

```text
Same interface
      ↓
Different objects
      ↓
Different behavior
```

---

# 4. Polymorphism Through Method Overriding

The most common OOP example uses inheritance and method overriding.

```python
class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):

    def speak(self):
        print("Bark")


class Cat(Animal):

    def speak(self):
        print("Meow")
```

Now:

```python
dog = Dog()
cat = Cat()

dog.speak()
cat.speak()
```

Output:

```text
Bark
Meow
```

The parent defines the common method:

```python
speak()
```

Each child provides its own implementation.

---

# 5. Polymorphic Function

Now we can write one function:

```python
def make_sound(animal):
    animal.speak()
```

Use it with different objects:

```python
make_sound(Dog())
make_sound(Cat())
```

Output:

```text
Bark
Meow
```

Notice that `make_sound()` does not need:

```python
if isinstance(animal, Dog):
```

or:

```python
if isinstance(animal, Cat):
```

It simply expects the object to provide:

```python
speak()
```

This is the power of polymorphism.

---

# 6. The Important Question

What does `make_sound()` actually care about?

Not:

```text
Is this a Dog?
Is this a Cat?
Is this a Cow?
```

It cares about:

```text
Can this object perform speak()?
```

This idea leads directly to **duck typing**.

---

# 7. Duck Typing

Python follows a principle commonly described as:

> **If it behaves like the required type, it can be used like that type.**

This is called **duck typing**.

The common phrase is:

```text
"If it walks like a duck and quacks like a duck,
treat it like a duck."
```

In Python, we often care about an object's behavior rather than its exact class.

---

# 8. Duck Typing Example

Consider:

```python
class Dog:

    def speak(self):
        print("Bark")


class Cat:

    def speak(self):
        print("Meow")


class Robot:

    def speak(self):
        print("Hello")
```

Now:

```python
def make_sound(obj):
    obj.speak()
```

All of these work:

```python
make_sound(Dog())
make_sound(Cat())
make_sound(Robot())
```

Output:

```text
Bark
Meow
Hello
```

`Robot` doesn't inherit from `Animal`.

It still works because it provides the required behavior:

```python
speak()
```

---

# 9. Inheritance-Based Polymorphism vs Duck Typing

These are related but different.

### Inheritance-based polymorphism

```text
Animal
  │
  ├── Dog
  └── Cat
```

The objects share a common parent.

### Duck typing

```text
Dog ──→ speak()
Cat ──→ speak()
Robot → speak()
```

They don't need to share a parent.

The important thing is the behavior.

---

# 10. Python Is Dynamically Typed

Python doesn't require us to specify the exact object type in:

```python
def make_sound(animal):
```

We don't write:

```python
def make_sound(animal: Animal):
```

for Python to execute the function.

The function can work with any object that provides the required method.

This is one reason duck typing is common in Python.

---

# 11. Polymorphism With Different Classes

Polymorphism doesn't always require inheritance.

Example:

```python
class PDF:

    def open(self):
        print("Opening PDF")


class Image:

    def open(self):
        print("Opening Image")


class Video:

    def open(self):
        print("Opening Video")
```

Now:

```python
def open_file(file):
    file.open()
```

Usage:

```python
open_file(PDF())
open_file(Image())
open_file(Video())
```

Output:

```text
Opening PDF
Opening Image
Opening Video
```

The function uses the common behavior:

```python
open()
```

---

# 12. Polymorphism With Built-in Python Types

Python's built-in functions also demonstrate polymorphism.

Consider:

```python
len("Python")
len([1, 2, 3])
len((10, 20))
```

The same function:

```python
len()
```

works with different types.

Conceptually:

```text
len()
 │
 ├── string
 ├── list
 ├── tuple
 ├── dictionary
 └── set
```

Each type provides the behavior required for determining its length.

This is another example of polymorphic behavior.

---

# 13. Operator Polymorphism

Operators can also behave differently depending on the operands.

Example:

```python
print(10 + 20)
```

Output:

```text
30
```

But:

```python
print("Hello " + "World")
```

Output:

```text
Hello World
```

The same operator:

```text
+
```

has different behavior depending on the types.

```text
int + int
    ↓
addition

str + str
    ↓
concatenation
```

This is a form of polymorphic behavior.

---

# 14. `+` With Lists

Another example:

```python
a = [1, 2]
b = [3, 4]

print(a + b)
```

Output:

```text
[1, 2, 3, 4]
```

Again:

```text
+
```

behaves according to the objects involved.

---

# 15. Method Polymorphism

A very common interview example:

```python
class Dog:

    def speak(self):
        return "Bark"


class Cat:

    def speak(self):
        return "Meow"


animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
```

Output:

```text
Bark
Meow
```

The loop doesn't need to know whether the object is:

```text
Dog
```

or:

```text
Cat
```

It only needs:

```text
speak()
```

---

# 16. Why This Is Better Than Type Checking

Consider this approach:

```python
def make_sound(animal):

    if isinstance(animal, Dog):
        print("Bark")

    elif isinstance(animal, Cat):
        print("Meow")
```

This becomes problematic as the number of types grows.

Suppose later we add:

```text
Cow
Horse
Lion
Bird
```

The function must keep changing.

With polymorphism:

```python
def make_sound(animal):
    animal.speak()
```

We don't need to modify the function for every new animal type.

This supports extensibility.

---

# 17. Open/Closed Thinking

Polymorphism supports an important design principle:

> **Software should be open for extension and closed for unnecessary modification.**

Suppose:

```python
def process_payment(payment):
    payment.pay()
```

We can add:

```text
CardPayment
UPIPayment
WalletPayment
```

without changing:

```python
process_payment()
```

as long as each object provides:

```python
pay()
```

This becomes very important in LLD.

---

# 18. LLD Example — Payment System

Imagine:

```text
Payment
   │
   ├── CardPayment
   ├── UPIPayment
   └── WalletPayment
```

Parent:

```python
class Payment:

    def pay(self, amount):
        raise NotImplementedError
```

Child classes:

```python
class CardPayment(Payment):

    def pay(self, amount):
        print("Paid using card")


class UPIPayment(Payment):

    def pay(self, amount):
        print("Paid using UPI")


class WalletPayment(Payment):

    def pay(self, amount):
        print("Paid using wallet")
```

Now:

```python
def process_payment(payment, amount):
    payment.pay(amount)
```

Usage:

```python
process_payment(CardPayment(), 1000)
process_payment(UPIPayment(), 1000)
process_payment(WalletPayment(), 1000)
```

The function doesn't care about the exact payment type.

---

# 19. Why This Is Useful in LLD

Without polymorphism:

```text
Payment processor
       │
       ├── if Card
       ├── if UPI
       ├── if Wallet
       ├── if Cash
       └── ...
```

With polymorphism:

```text
Payment processor
       │
       ↓
   payment.pay()
       │
       ├── Card → card implementation
       ├── UPI → UPI implementation
       └── Wallet → wallet implementation
```

The caller depends on the common behavior rather than every implementation.

---

# 20. Another LLD Example — Notification

Suppose:

```text
Notification
      │
      ├── EmailNotification
      ├── SMSNotification
      └── PushNotification
```

Each class implements:

```python
send()
```

Example:

```python
class EmailNotification:

    def send(self, message):
        print("Sending email:", message)


class SMSNotification:

    def send(self, message):
        print("Sending SMS:", message)


class PushNotification:

    def send(self, message):
        print("Sending push notification:", message)
```

Now:

```python
def notify(notification, message):
    notification.send(message)
```

Usage:

```python
notify(EmailNotification(), "Hello")
notify(SMSNotification(), "Hello")
notify(PushNotification(), "Hello")
```

One function works with multiple implementations.

---

# 21. Polymorphism Through a Common Interface

A useful LLD mental model:

```text
                Common Interface
                       │
                       ↓
                     send()
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
       Email          SMS          Push
          │            │            │
       send()        send()       send()
```

The caller depends on:

```text
send()
```

not on:

```text
Email
SMS
Push
```

---

# 22. Abstract Base Classes

Sometimes we want to explicitly define what methods subclasses are expected to implement.

Python provides:

```python
abc
```

and:

```python
ABC
```

from the `abc` module.

Example:

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

Now child classes are expected to implement:

```python
pay()
```

---

# 23. Why Use Abstract Base Classes?

An abstract base class can define a common contract.

Example:

```text
Payment
   ↓
Every payment implementation must provide:

pay()
```

Then:

```python
class CardPayment(Payment):

    def pay(self, amount):
        print("Card payment")
```

and:

```python
class UPIPayment(Payment):

    def pay(self, amount):
        print("UPI payment")
```

This makes the expected interface explicit.

---

# 24. Abstract Method

Example:

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass
```

A subclass should implement:

```python
class Dog(Animal):

    def speak(self):
        print("Bark")
```

The abstract base class defines the contract:

```text
Every Animal subclass must provide speak()
```

---

# 25. Abstract Class Cannot Normally Be Instantiated

Example:

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass
```

Trying:

```python
animal = Animal()
```

raises an error because the class still contains an unimplemented abstract method.

The idea is:

```text
Animal
   ↓
Defines contract
   ↓
Not meant to be used directly
```

while:

```text
Dog
   ↓
Provides implementation
```

can be instantiated.

---

# 26. Abstract Base Class + Polymorphism

Complete example:

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):

    def pay(self, amount):
        print("Card payment:", amount)


class UPIPayment(Payment):

    def pay(self, amount):
        print("UPI payment:", amount)
```

Now:

```python
def process_payment(payment, amount):
    payment.pay(amount)
```

Usage:

```python
process_payment(CardPayment(), 1000)
process_payment(UPIPayment(), 1000)
```

This is a strong LLD pattern.

---

# 27. Duck Typing vs Abstract Base Class

These are two different approaches.

### Duck Typing

```text
"Does the object provide the required behavior?"
```

Example:

```python
def process(payment):
    payment.pay()
```

No explicit inheritance required.

### Abstract Base Class

```text
"Does this class follow the defined contract?"
```

Example:

```python
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
```

Both can be useful.

Python commonly uses duck typing, while ABCs are useful when an explicit contract is valuable.

---

# 28. Polymorphism Without Inheritance

Important interview point:

> **Polymorphism does not always require inheritance in Python.**

Example:

```python
class Dog:

    def speak(self):
        print("Bark")


class Robot:

    def speak(self):
        print("Hello")
```

They have no common parent.

Still:

```python
def make_sound(obj):
    obj.speak()
```

works for both.

This is duck typing.

---

# 29. Polymorphism With Inheritance

Another approach:

```python
class Animal:

    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        print("Bark")


class Cat(Animal):

    def speak(self):
        print("Meow")
```

Here:

```text
Animal
  │
  ├── Dog
  └── Cat
```

and both override:

```text
speak()
```

---

# 30. Polymorphism and Method Overriding

Remember the relationship:

```text
Inheritance
     ↓
Method Overriding
     ↓
Different implementations
     ↓
Polymorphic behavior
```

Example:

```python
class Animal:

    def speak(self):
        print("Animal")


class Dog(Animal):

    def speak(self):
        print("Dog")
```

Calling:

```python
animal = Dog()

animal.speak()
```

executes:

```text
Dog.speak()
```

not:

```text
Animal.speak()
```

because the actual object is a `Dog`.

---

# 31. Compile-Time vs Runtime Polymorphism

This distinction is common in OOP interviews.

### Compile-time polymorphism

Often associated with:

```text
method overloading
operator overloading
```

in languages such as Java/C++.

### Runtime polymorphism

Commonly associated with:

```text
method overriding
```

where the implementation depends on the actual object at runtime.

Python is dynamically typed, so traditional compile-time method overloading is not used in the same way as Java/C++.

For Python interviews, focus heavily on:

```text
method overriding
duck typing
polymorphic behavior
```

---

# 32. Python's `+` and `__add__`

Operator behavior can be implemented through special methods.

For example:

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)
```

Now:

```python
a = Number(10)
b = Number(20)

c = a + b

print(c.value)
```

Output:

```text
30
```

The `+` operator calls the appropriate special method.

This is operator polymorphism.

---

# 33. Don't Confuse Polymorphism With Overloading

These concepts overlap in broader OOP terminology but should not be treated as identical.

### Polymorphism

```text
One interface
Multiple implementations
```

### Method Overriding

```text
Child changes inherited method behavior
```

### Operator Overloading

```text
Operators work with user-defined objects
```

### Duck Typing

```text
Behavior matters more than exact type
```

These concepts can work together.

---

# 34. Example Combining Everything

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using card")


class UPIPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class WalletPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using wallet")


def process_payment(payment, amount):
    payment.pay(amount)
```

Now:

```python
payments = [
    CardPayment(),
    UPIPayment(),
    WalletPayment()
]

for payment in payments:
    process_payment(payment, 1000)
```

Output:

```text
Paid 1000 using card
Paid 1000 using UPI
Paid 1000 using wallet
```

The same:

```python
process_payment()
```

works with multiple implementations.

That is the core of polymorphism.

---

# 35. Why This Design Is Extensible

Suppose tomorrow we add:

```python
class CryptoPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using crypto")
```

We don't need to modify:

```python
process_payment()
```

We simply pass:

```python
process_payment(CryptoPayment(), 1000)
```

This is one of the biggest benefits of polymorphism in LLD.

---

# 36. LLD Mental Model

When designing a system, think:

```text
What common behavior exists?
          ↓
Define a common interface/contract
          ↓
Create multiple implementations
          ↓
Caller depends on the interface
          ↓
Each implementation handles its own behavior
```

Example:

```text
Payment
   ↓
pay()
   │
   ├── CardPayment
   ├── UPIPayment
   └── WalletPayment
```

The payment processor only knows:

```text
pay()
```

---

# 37. Polymorphism Reduces Conditional Logic

Without polymorphism:

```python
def process(payment_type, amount):

    if payment_type == "card":
        ...

    elif payment_type == "upi":
        ...

    elif payment_type == "wallet":
        ...
```

As types increase, this function becomes larger.

With polymorphism:

```python
def process(payment, amount):
    payment.pay(amount)
```

The implementation moves into the appropriate class.

This keeps responsibilities separated.

---

# 38. Important LLD Principle

Instead of asking:

> "What type of object is this?"

try to ask:

> "What behavior do I need from this object?"

Example:

Bad:

```python
if isinstance(payment, CardPayment):
    ...
```

Better:

```python
payment.pay(amount)
```

when the design supports that common interface.

This reduces coupling to concrete classes.

---

# 39. Polymorphism and Dependency Inversion

Polymorphism also supports an important LLD idea:

```text
High-level code
      ↓
depends on
      ↓
Common abstraction/interface
      ↓
instead of concrete implementation
```

Example:

```text
PaymentProcessor
      ↓
Payment
      ↓
CardPayment / UPIPayment / WalletPayment
```

The processor doesn't need to know every concrete implementation.

This concept becomes important later when we study **SOLID principles**.

---

# 40. Backend Example

Imagine a notification service:

```python
def send_notification(notification, message):
    notification.send(message)
```

Different implementations:

```python
class EmailNotification:

    def send(self, message):
        print("Email:", message)


class SMSNotification:

    def send(self, message):
        print("SMS:", message)


class PushNotification:

    def send(self, message):
        print("Push:", message)
```

Backend code can use:

```python
send_notification(EmailNotification(), "Welcome")
send_notification(SMSNotification(), "Welcome")
send_notification(PushNotification(), "Welcome")
```

The service doesn't need to know how each notification is implemented.

---

# 41. DSA Connection

Polymorphism is not usually the main technique for solving DSA problems.

But it can appear when designing reusable data structures.

Example:

```python
class Stack:

    def push(self, value):
        pass

    def pop(self):
        pass
```

Different implementations could use:

```text
ArrayStack
LinkedListStack
```

Both can expose:

```text
push()
pop()
```

The caller can use the common behavior without caring about the internal implementation.

This is more relevant to **software design** than algorithm solving.

---

# 42. Common Mistake #1

Thinking polymorphism requires inheritance.

Not necessarily.

Python supports duck typing:

```python
class A:
    def show(self):
        print("A")


class B:
    def show(self):
        print("B")
```

Both can work with:

```python
def display(obj):
    obj.show()
```

No inheritance is required.

---

# 43. Common Mistake #2

Using `isinstance()` everywhere.

This:

```python
if isinstance(obj, Dog):
    ...
elif isinstance(obj, Cat):
    ...
```

can defeat the purpose of polymorphic design when all you need is a common behavior.

Prefer:

```python
obj.speak()
```

when the interface is designed appropriately.

---

# 44. Common Mistake #3

Creating a giant parent class

Don't create a parent like:

```text
BaseClass
    ↓
100 unrelated methods
```

just so every child can inherit code.

The parent should represent meaningful common behavior.

---

# 45. Common Mistake #4

Forcing Unrelated Classes Into One Hierarchy

Bad design:

```text
Animal
  ├── Dog
  └── Car
```

just because both have:

```text
move()
```

Having one common method does not automatically mean inheritance is appropriate.

Duck typing or composition may be better depending on the design.

---

# 46. Common Mistake #5

Confusing Interface With Implementation

For example:

```text
Interface:
    pay()

Implementation:
    how card payment happens
    how UPI payment happens
    how wallet payment happens
```

The caller should usually depend on:

```text
pay()
```

rather than the internal implementation.

This is the foundation of flexible LLD.

---

# 47. Interview Question: What Is Polymorphism?

### Answer

Polymorphism means that the same interface or operation can work with different object types and produce type-specific behavior.

Example:

```python
def make_sound(animal):
    animal.speak()
```

Different objects can provide different implementations of:

```python
speak()
```

---

# 48. Interview Question: Does Polymorphism Require Inheritance in Python?

No.

Python supports duck typing, so unrelated classes can participate in polymorphic behavior if they provide the required interface.

Example:

```python
class Dog:
    def speak(self):
        print("Bark")


class Robot:
    def speak(self):
        print("Hello")
```

Both can be passed to:

```python
def make_sound(obj):
    obj.speak()
```

---

# 49. Interview Question: What Is Duck Typing?

Duck typing is a Python approach where the behavior an object provides is more important than its exact type.

Instead of asking:

```text
"What type is this object?"
```

we often ask:

```text
"Does this object provide the operation I need?"
```

---

# 50. Interview Question: What Is Runtime Polymorphism?

Runtime polymorphism occurs when the method implementation used depends on the actual object at runtime.

Example:

```python
class Animal:

    def speak(self):
        print("Animal")


class Dog(Animal):

    def speak(self):
        print("Dog")


animal = Dog()

animal.speak()
```

Output:

```text
Dog
```

The overridden method is selected based on the actual object.

---

# 51. Interview Question: What Is an Abstract Base Class?

An abstract base class defines a common contract for subclasses.

Example:

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

Subclasses are expected to implement:

```python
pay()
```

---

# 52. Interview Question: Why Use ABC?

ABCs are useful when you want to make a common contract explicit.

For example:

```text
Payment
   ↓
Every payment implementation must provide:
pay()
```

This can make larger LLD designs easier to understand and enforce.

---

# 53. Interview Question: Polymorphism vs Inheritance

They are not the same.

```text
Inheritance
   ↓
Relationship between classes
```

while:

```text
Polymorphism
   ↓
Same interface/operation
Multiple possible implementations
```

Inheritance can be one way to achieve polymorphic behavior, but Python's duck typing allows polymorphism without inheritance.

---

# 54. Interview Question: Why Is Polymorphism Useful in LLD?

Polymorphism helps:

- reduce conditional logic
- reduce coupling
- separate implementations
- make systems easier to extend
- allow common interfaces
- support dependency inversion
- make code easier to maintain

Example:

```python
def process_payment(payment):
    payment.pay()
```

The function can work with many payment implementations.

---

# 55. Complete Practical Example

```python
from abc import ABC, abstractmethod


class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):

    def send(self, message):
        print(f"Email sent: {message}")


class SMSNotification(Notification):

    def send(self, message):
        print(f"SMS sent: {message}")


class PushNotification(Notification):

    def send(self, message):
        print(f"Push notification sent: {message}")


def notify(notification, message):
    notification.send(message)


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notify(notification, "Welcome!")
```

Output:

```text
Email sent: Welcome!
SMS sent: Welcome!
Push notification sent: Welcome!
```

The important part is:

```python
notification.send(message)
```

The caller doesn't need to know the concrete implementation.

---

# 56. The Big Picture of OOP So Far

You have now covered the major OOP pillars and their foundations.

```text
                    OOP
                     │
       ┌─────────────┼─────────────┐
       │             │             │
 Encapsulation   Inheritance   Polymorphism
       │             │             │
       ↓             ↓             ↓
 Protect State   Reuse/Extend   Multiple Behaviors
       │             │             │
       ↓             ↓             ↓
@property        super()       overriding
_methods         MRO           duck typing
```

The remaining major pillar is:

```text
Abstraction
```

---

# 57. Connection Between the Four Pillars

## Encapsulation

```text
Control internal state
```

## Inheritance

```text
Create relationships between classes
```

## Polymorphism

```text
One interface → multiple implementations
```

## Abstraction

```text
Expose essential behavior
Hide unnecessary implementation details
```

These concepts often work together rather than independently.

---

# 58. Core Polymorphism Mental Model

```text
                  COMMON INTERFACE
                         │
                         ↓
                       method()
                         │
            ┌────────────┼────────────┐
            ↓            ↓            ↓
        Object A     Object B     Object C
            │            │            │
            ↓            ↓            ↓
      implementation implementation implementation
            │            │            │
            ↓            ↓            ↓
        Behavior A   Behavior B   Behavior C
```

The caller only needs to know:

```text
method()
```

not every implementation detail.

---

# 59. Final Mental Model

Remember these five ideas:

```text
Inheritance
    ↓
"is-a" relationship


Method Overriding
    ↓
Child changes inherited behavior


Polymorphism
    ↓
Same interface, different behavior


Duck Typing
    ↓
Behavior matters more than exact type


LLD
    ↓
Depend on common behavior/interface
rather than concrete implementations
```

---

# 60. Quick Revision

### Polymorphism

```text
One interface
      ↓
Multiple implementations
```

### Method Overriding

```python
class Dog(Animal):

    def speak(self):
        ...
```

### Duck Typing

```python
def make_sound(obj):
    obj.speak()
```

Object type doesn't need to be explicitly checked.

### Abstract Base Class

```python
from abc import ABC, abstractmethod
```

Used to define an explicit contract.

### Polymorphic Design

```python
def process(payment):
    payment.pay()
```

The caller depends on the common behavior.

---

# 61. Must-Know Interview Checklist

Before moving to the next lecture, you should be able to explain:

- What is polymorphism?
- Why is polymorphism useful?
- What is method overriding?
- How does overriding produce polymorphic behavior?
- What is duck typing?
- Does Python require inheritance for polymorphism?
- What is runtime polymorphism?
- What is an abstract base class?
- What is `ABC`?
- What is `@abstractmethod`?
- Why use an abstract base class?
- Difference between inheritance and polymorphism?
- Difference between duck typing and ABC?
- How does polymorphism reduce conditional logic?
- How is polymorphism useful in LLD?
- How can polymorphism help extensibility?
- Why should code depend on common behavior rather than concrete classes?
- How does polymorphism relate to SOLID and dependency inversion?

# OOP Lecture 6 Complete