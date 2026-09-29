# OOP — Lecture 8
# SOLID Principles

> **Goal:** Learn the five SOLID principles and understand how they help us write maintainable, extensible, loosely coupled Python code.
>
> SOLID is the bridge between **knowing OOP concepts** and **using OOP properly when designing real software**.

## 1. What Is SOLID?

**SOLID** is a collection of five object-oriented design principles:

```text
S → Single Responsibility Principle
O → Open/Closed Principle
L → Liskov Substitution Principle
I → Interface Segregation Principle
D → Dependency Inversion Principle
```

These principles help us design software that is:

- easier to understand
- easier to maintain
- easier to test
- easier to extend
- less tightly coupled
- less fragile when requirements change

Important:

> SOLID is not a framework, library, or Python feature.

It is a set of **design principles**.

---

# 2. Why Do We Need SOLID?

Suppose we write a large class:

```python
class User:
    def register(self):
        pass

    def validate_email(self):
        pass

    def save_to_database(self):
        pass

    def send_email(self):
        pass

    def generate_report(self):
        pass
```

This class is doing many unrelated things.

Now imagine the requirements change:

```text
Email provider changes
Database changes
Validation rules change
Report format changes
```

The same class keeps changing.

This creates:

```text
High coupling
+
Low maintainability
+
Difficult testing
+
Higher chance of bugs
```

SOLID gives us principles for avoiding these problems.

---

# 3. The Five Principles

```text
S → Single Responsibility
    One class should have one responsibility.

O → Open/Closed
    Open for extension, closed for modification.

L → Liskov Substitution
    Child objects should be usable wherever the parent is expected.

I → Interface Segregation
    Don't force clients to depend on methods they don't need.

D → Dependency Inversion
    High-level code should depend on abstractions, not concrete implementations.
```

---

# 4. SOLID Is Not a Set of Strict Rules

SOLID principles are **design guidelines**.

They should help us answer:

```text
Is this class doing too much?

Will adding a feature require modifying existing code unnecessarily?

Can this subclass actually behave like its parent?

Am I forcing a class to implement unnecessary methods?

Is my high-level code tightly coupled to a concrete implementation?
```

The goal is not:

```text
"Use SOLID everywhere."
```

The goal is:

```text
"Use good design where it solves a real problem."
```

---

# 5. S — Single Responsibility Principle

## Definition

> **A class should have one reason to change.**

This is the most important way to remember SRP.

A class should have one clear responsibility.

It does **not** simply mean:

```text
One class = one method
```

or:

```text
One class = one tiny operation
```

Instead:

```text
One class
    ↓
One cohesive responsibility
    ↓
One major reason to change
```

---

# 6. Bad SRP Example

Consider:

```python
class UserService:

    def create_user(self, user):
        pass

    def validate_user(self, user):
        pass

    def save_to_database(self, user):
        pass

    def send_email(self, user):
        pass
```

This class handles:

```text
User creation
Validation
Database persistence
Email communication
```

These are different responsibilities.

Potential reasons for change:

```text
Validation rules change
        ↓
UserService changes

Database changes
        ↓
UserService changes

Email provider changes
        ↓
UserService changes
```

That is a sign of poor separation of responsibilities.

---

# 7. Better SRP Design

Separate responsibilities:

```python
class UserValidator:

    def validate(self, user):
        pass
```

```python
class UserRepository:

    def save(self, user):
        pass
```

```python
class EmailService:

    def send_welcome_email(self, user):
        pass
```

```python
class UserService:

    def create_user(self, user):
        pass
```

Now:

```text
UserValidator
    ↓
Validation

UserRepository
    ↓
Persistence

EmailService
    ↓
Email

UserService
    ↓
User-related business flow
```

Each class has a clearer responsibility.

---

# 8. SRP Does Not Mean "One Function Per Class"

Bad interpretation:

```python
class AddUser:
    def add(self):
        pass
```

```python
class ValidateUser:
    def validate(self):
        pass
```

```python
class SaveUser:
    def save(self):
        pass
```

This can create unnecessary fragmentation.

SRP means:

> Keep responsibilities cohesive.

The goal is not to create hundreds of tiny classes.

---

# 9. How to Identify SRP Violations

Ask:

```text
How many different reasons could make this class change?
```

If you find:

```text
Database changes
+
Email changes
+
Validation changes
+
Report changes
```

then the class may have too many responsibilities.

Another useful question:

> "Can I describe what this class does with one clear responsibility?"

If not, investigate whether it is doing too much.

---

# 10. SRP Example — Invoice

Bad:

```python
class Invoice:

    def calculate_total(self):
        pass

    def save_to_database(self):
        pass

    def print_invoice(self):
        pass

    def send_email(self):
        pass
```

The class handles:

```text
Calculation
Database
Printing
Email
```

Better:

```python
class Invoice:

    def calculate_total(self):
        pass
```

```python
class InvoiceRepository:

    def save(self, invoice):
        pass
```

```python
class InvoicePrinter:

    def print(self, invoice):
        pass
```

```python
class InvoiceEmailService:

    def send(self, invoice):
        pass
```

Now each component has a more focused responsibility.

---

# 11. SRP Mental Model

```text
Bad:

One Class
   │
   ├── Validation
   ├── Database
   ├── Email
   ├── Reporting
   └── Formatting


Good:

UserService
    │
    └── Business Flow

UserValidator
    │
    └── Validation

UserRepository
    │
    └── Persistence

EmailService
    │
    └── Communication
```

---

# 12. O — Open/Closed Principle

## Definition

> **Software entities should be open for extension but closed for modification.**

Meaning:

```text
New behavior
    ↓
Add/extend code

instead of

Changing existing stable code
```

The goal is to make systems easier to extend without constantly modifying existing logic.

---

# 13. Bad OCP Example

Suppose we have:

```python
class PaymentProcessor:

    def process(self, payment_type, amount):

        if payment_type == "card":
            print("Processing card")

        elif payment_type == "upi":
            print("Processing UPI")
```

Now we add:

```text
Wallet
Net Banking
Crypto
```

We must modify:

```python
PaymentProcessor.process()
```

every time.

That means existing code keeps changing.

---

# 14. Better OCP Design

Create a common interface:

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

Implementations:

```python
class CardPayment(Payment):

    def pay(self, amount):
        print("Processing card")
```

```python
class UPIPayment(Payment):

    def pay(self, amount):
        print("Processing UPI")
```

Processor:

```python
class PaymentProcessor:

    def process(self, payment, amount):
        payment.pay(amount)
```

Now add:

```python
class WalletPayment(Payment):

    def pay(self, amount):
        print("Processing wallet")
```

We don't need to modify:

```python
PaymentProcessor
```

We extend the system by adding a new implementation.

---

# 15. OCP Mental Model

```text
Before:

PaymentProcessor
      ↓
if card
if UPI
if wallet
if cash
if ...


After:

PaymentProcessor
      ↓
   Payment
      ↓
┌─────┼─────┐
↓     ↓     ↓
Card  UPI  Wallet
```

The processor works with the abstraction.

---

# 16. OCP and Polymorphism

Polymorphism is one of the most useful tools for achieving OCP.

```text
Common Interface
       ↓
Polymorphism
       ↓
Different implementations
       ↓
Extend without modifying caller
```

Example:

```python
def process(payment):
    payment.pay()
```

New payment types can be added without changing:

```python
process()
```

---

# 17. OCP Does Not Mean "Never Modify Existing Code"

This is important.

OCP does **not** mean:

```text
Never change existing code.
```

Real software evolves.

The principle means:

> Design stable areas so that new variations can often be added through extension rather than repeatedly modifying existing logic.

Use judgment.

Don't create abstractions for every possible future requirement.

---

# 18. L — Liskov Substitution Principle

## Definition

> **Objects of a subclass should be usable wherever objects of the parent type are expected without breaking the correctness of the program.**

This is one of the most important and commonly misunderstood SOLID principles.

Simple version:

```text
If B is a subtype of A,
then B should behave like a valid A.
```

---

# 19. Simple LSP Example

Suppose:

```python
class Bird:

    def fly(self):
        print("Flying")
```

Then:

```python
class Sparrow(Bird):

    def fly(self):
        print("Sparrow flying")
```

This is reasonable because:

```text
Sparrow
is a
Bird
```

and a Sparrow can perform:

```text
fly()
```

---

# 20. LSP Violation Example

Now:

```python
class Bird:

    def fly(self):
        print("Flying")
```

Then:

```python
class Penguin(Bird):

    def fly(self):
        raise Exception("Penguins cannot fly")
```

Problem:

```python
def make_bird_fly(bird):
    bird.fly()
```

Works for:

```python
make_bird_fly(Sparrow())
```

but breaks for:

```python
make_bird_fly(Penguin())
```

The subclass cannot properly satisfy the behavior expected from the parent.

This is an LSP problem.

---

# 21. Better Bird Design

Instead of:

```text
Bird
  ↓
fly()
```

we can separate capabilities.

For example:

```python
class Bird:
    pass
```

Flying birds:

```python
class FlyingBird(Bird):

    def fly(self):
        print("Flying")
```

Then:

```python
class Sparrow(FlyingBird):

    def fly(self):
        print("Sparrow flying")
```

Penguin:

```python
class Penguin(Bird):
    pass
```

Now we don't force Penguin to implement behavior it cannot support.

---

# 22. LSP Is About Behavior

LSP is not simply:

```text
"Child inherits from parent."
```

It is about whether the child can actually satisfy the expectations of the parent abstraction.

Think:

```text
Parent contract
      ↓
Child must honor the contract
```

A child should not unexpectedly:

- reject valid parent inputs
- break expected behavior
- violate important guarantees
- throw unsupported-operation errors for behavior it inherited as valid

---

# 23. Another LSP Example

Consider:

```python
class Rectangle:

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
```

Now suppose:

```python
class Square(Rectangle):

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height
```

This can create surprising behavior for code expecting independent width and height.

The issue is not that:

```text
Square is not mathematically a rectangle.
```

The issue is:

```text
Square does not necessarily preserve the behavioral expectations
of the Rectangle API.
```

This is the important LSP perspective.

---

# 24. How to Detect LSP Problems

Ask:

```text
Can I replace the parent object with the child object
without breaking the caller's assumptions?
```

If:

```python
process(parent)
```

works but:

```python
process(child)
```

unexpectedly fails, the inheritance relationship may be wrong.

---

# 25. I — Interface Segregation Principle

## Definition

> **Clients should not be forced to depend on methods they do not use.**

The word "interface" here means the set of operations exposed to a client.

The idea:

```text
Prefer smaller, focused interfaces
over
large interfaces containing unrelated operations.
```

---

# 26. Bad ISP Example

Suppose:

```python
from abc import ABC, abstractmethod


class Worker(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass
```

Now imagine a robot:

```python
class Robot(Worker):

    def work(self):
        print("Robot working")

    def eat(self):
        raise NotImplementedError

    def sleep(self):
        raise NotImplementedError
```

The robot is forced to implement:

```text
eat()
sleep()
```

even though it doesn't need them.

That's an interface design problem.

---

# 27. Better ISP Design

Separate capabilities:

```python
class Workable(ABC):

    @abstractmethod
    def work(self):
        pass
```

```python
class Eatable(ABC):

    @abstractmethod
    def eat(self):
        pass
```

Now:

```python
class Human(Workable, Eatable):

    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")
```

Robot only needs:

```python
class Robot(Workable):

    def work(self):
        print("Robot working")
```

Now the robot isn't forced to implement irrelevant methods.

---

# 28. ISP Mental Model

Bad:

```text
Large Interface
      │
 ┌────┼────┬────┐
work eat sleep print
```

Every client must deal with everything.

Better:

```text
Workable
   ↓
work()

Eatable
   ↓
eat()

Sleepable
   ↓
sleep()
```

Clients depend only on what they need.

---

# 29. ISP in Backend Development

Suppose we create:

```python
class UserService:

    def create_user(self):
        pass

    def delete_user(self):
        pass

    def send_email(self):
        pass

    def generate_report(self):
        pass
```

If another component only needs:

```text
create_user()
```

it shouldn't necessarily depend on every unrelated operation.

Smaller abstractions can make dependencies clearer.

---

# 30. D — Dependency Inversion Principle

## Definition

> **High-level modules should not depend directly on low-level modules. Both should depend on abstractions.**

And:

> **Abstractions should not depend on details. Details should depend on abstractions.**

This is one of the most important SOLID principles for backend and LLD design.

---

# 31. What Is a High-Level Module?

A high-level module contains business logic.

Example:

```text
OrderService
PaymentService
UserService
NotificationService
```

These describe:

```text
What the application wants to accomplish.
```

---

# 32. What Is a Low-Level Module?

A low-level module usually handles implementation details.

Examples:

```text
MySQL
PostgreSQL
SMTP
Redis
S3
Payment Gateway
```

These describe:

```text
How the work is performed.
```

---

# 33. Bad Dependency Design

Suppose:

```python
class MySQLDatabase:

    def save(self, data):
        print("Saving to MySQL")
```

Then:

```python
class UserService:

    def __init__(self):
        self.database = MySQLDatabase()

    def save_user(self, user):
        self.database.save(user)
```

Problem:

```text
UserService
    ↓
directly creates
    ↓
MySQLDatabase
```

Now `UserService` is tightly coupled to MySQL.

---

# 34. Why Is This a Problem?

Suppose tomorrow we move from:

```text
MySQL
```

to:

```text
PostgreSQL
```

We need to modify:

```python
UserService
```

Testing is also harder because:

```text
UserService
    ↓
real MySQL
```

instead of:

```text
UserService
    ↓
replaceable dependency
```

---

# 35. Better DIP Design

Create an abstraction:

```python
from abc import ABC, abstractmethod


class UserRepository(ABC):

    @abstractmethod
    def save(self, user):
        pass
```

Implementation:

```python
class MySQLUserRepository(UserRepository):

    def save(self, user):
        print("Saving user to MySQL")
```

Now:

```python
class UserService:

    def __init__(self, repository):
        self.repository = repository

    def save_user(self, user):
        self.repository.save(user)
```

Usage:

```python
repository = MySQLUserRepository()

service = UserService(repository)

service.save_user(user)
```

Now the dependency is supplied from outside.

---

# 36. Dependency Injection

The previous example introduces:

> **Dependency Injection**

Instead of creating the dependency inside the class:

```python
self.repository = MySQLUserRepository()
```

we provide it from outside:

```python
service = UserService(repository)
```

The class receives what it needs.

This reduces coupling.

---

# 37. Constructor Dependency Injection

The most common form in Python:

```python
class UserService:

    def __init__(self, repository):
        self.repository = repository
```

Then:

```python
repository = MySQLUserRepository()

service = UserService(repository)
```

Mental model:

```text
Outside Code
     ↓
creates dependency
     ↓
injects dependency
     ↓
Service
```

---

# 38. DIP Mental Model

Bad:

```text
High-Level
    ↓
Concrete Low-Level
```

Example:

```text
UserService
    ↓
MySQLUserRepository
```

Better:

```text
          Abstraction
          UserRepository
             ↑
             │
    ┌────────┴─────────┐
    │                  │
MySQL Repository   PostgreSQL Repository
```

High-level code depends on:

```text
UserRepository
```

not directly on:

```text
MySQLUserRepository
```

---

# 39. SOLID Principles Together

The five principles are not isolated.

They support each other.

Example:

```text
SRP
 ↓
Separate responsibilities

OCP
 ↓
Allow new implementations

LSP
 ↓
Ensure implementations remain substitutable

ISP
 ↓
Keep interfaces focused

DIP
 ↓
Depend on abstractions
```

Together:

```text
Clean
Maintainable
Extensible
Loosely Coupled
```

---

# 40. Complete Example Using SOLID

Consider a notification system.

We want:

```text
Email
SMS
Push
```

## Step 1 — Abstraction

```python
from abc import ABC, abstractmethod


class NotificationService(ABC):

    @abstractmethod
    def send(self, message):
        pass
```

---

## Step 2 — Implementations

```python
class EmailNotification(NotificationService):

    def send(self, message):
        print(f"Email: {message}")
```

```python
class SMSNotification(NotificationService):

    def send(self, message):
        print(f"SMS: {message}")
```

```python
class PushNotification(NotificationService):

    def send(self, message):
        print(f"Push: {message}")
```

---

## Step 3 — High-Level Service

```python
class NotificationManager:

    def __init__(self, notification_service):
        self.notification_service = notification_service

    def notify(self, message):
        self.notification_service.send(message)
```

---

## Step 4 — Usage

```python
email = EmailNotification()

manager = NotificationManager(email)

manager.notify("Welcome!")
```

Output:

```text
Email: Welcome!
```

Change implementation:

```python
sms = SMSNotification()

manager = NotificationManager(sms)

manager.notify("Welcome!")
```

Output:

```text
SMS: Welcome!
```

The manager didn't change.

---

# 41. Where Is SOLID Used Here?

### SRP

```text
NotificationManager
→ manages notification flow

EmailNotification
→ email sending

SMSNotification
→ SMS sending
```

Responsibilities are separated.

### OCP

New notification types can be added:

```python
class PushNotification(NotificationService):
    ...
```

without modifying `NotificationManager`.

### LSP

Each notification implementation can be used where:

```text
NotificationService
```

is expected.

### ISP

The abstraction only exposes:

```python
send()
```

instead of unrelated operations.

### DIP

`NotificationManager` depends on:

```text
NotificationService
```

rather than:

```text
EmailNotification
```

---

# 42. SOLID and Tight Coupling

### Tight coupling

```text
Service
  ↓
Concrete Implementation
```

Example:

```python
class OrderService:

    def __init__(self):
        self.payment = StripePayment()
```

The service is directly tied to:

```text
StripePayment
```

### Lower coupling

```text
Service
  ↓
Payment abstraction
  ↓
Stripe / Razorpay / PayPal
```

Now the implementation can change more easily.

---

# 43. SOLID and Testing

DIP makes testing easier.

Suppose:

```python
class UserService:

    def __init__(self, repository):
        self.repository = repository
```

During testing, we can provide a fake repository:

```python
class FakeUserRepository:

    def save(self, user):
        print("Fake save")
```

Then:

```python
repository = FakeUserRepository()

service = UserService(repository)
```

We don't need a real database.

This is one reason dependency injection is valuable.

---

# 44. SOLID Does Not Mean More Classes = Better Design

A common mistake is:

```text
SOLID
  ↓
Create 50 classes
```

That's not the goal.

Good design means:

```text
Clear responsibilities
+
Meaningful abstractions
+
Low unnecessary coupling
+
Easy extension
```

Not:

```text
Maximum number of classes
```

---

# 45. SOLID Does Not Mean Zero Coupling

Some coupling is necessary.

For example:

```python
NotificationManager
```

must know about the abstraction:

```python
NotificationService
```

The goal is not:

```text
No dependencies
```

The goal is:

```text
Manage dependencies intelligently
```

---

# 46. Practical SOLID Checklist

When designing a class, ask:

### S — Single Responsibility

```text
Does this class have multiple unrelated reasons to change?
```

### O — Open/Closed

```text
Will adding a new variation require modifying stable code?
```

### L — Liskov Substitution

```text
Can subclasses safely replace the parent abstraction?
```

### I — Interface Segregation

```text
Am I forcing clients to depend on methods they don't need?
```

### D — Dependency Inversion

```text
Does high-level code depend directly on concrete implementation details?
```

---

# 47. SOLID Decision Flow

Use this mental process:

```text
I have a class
      ↓
Is it doing too many things?
      ↓
       YES
       ↓
      SRP


I need to add a new behavior
      ↓
Do I have to keep modifying existing logic?
      ↓
       YES
       ↓
      OCP


I created a subclass
      ↓
Can it actually behave like its parent?
      ↓
       NO
       ↓
      LSP


My interface is becoming huge
      ↓
Do clients need all these methods?
      ↓
       NO
       ↓
      ISP


My service directly creates concrete dependencies
      ↓
Can I depend on an abstraction and inject the implementation?
      ↓
       YES
       ↓
      DIP
```

---

# 48. SOLID vs OOP Pillars

The four OOP pillars are:

```text
Encapsulation
Inheritance
Polymorphism
Abstraction
```

SOLID is different.

SOLID tells us:

```text
How should we use OOP concepts to design maintainable software?
```

Think:

```text
OOP
 ↓
Building blocks

SOLID
 ↓
Design guidelines for using those building blocks
```

---

# 49. SOLID and the Previous Lectures

You have already learned:

```text
Encapsulation
     ↓
Protect and control state

Inheritance
     ↓
Reuse / specialization

Polymorphism
     ↓
Multiple implementations

Abstraction
     ↓
Common contracts
```

Now SOLID connects them:

```text
Abstraction
     +
Polymorphism
     ↓
OCP / DIP

Inheritance
     ↓
LSP

Encapsulation
     ↓
SRP / maintainable responsibilities

Abstraction
     ↓
ISP / focused interfaces
```

---

# 50. Common Interview Traps

### Trap 1

> "SRP means one class should have only one method."

Wrong.

SRP means:

```text
One cohesive responsibility
+
One major reason to change
```

---

### Trap 2

> "OCP means never modify code."

Wrong.

It means designing stable areas so new variations can often be added through extension rather than repeated modification.

---

### Trap 3

> "LSP means every child must inherit every behavior."

Wrong.

The child must satisfy the behavioral expectations of the parent abstraction.

---

### Trap 4

> "ISP means create an interface for every method."

Wrong.

The goal is focused, meaningful interfaces.

---

### Trap 5

> "DIP means dependency injection."

Related, but not identical.

```text
DIP
→ design principle

Dependency Injection
→ technique commonly used to implement the principle
```

---

# 51. Interview Questions

## Beginner

1. What is SOLID?
2. What are the five SOLID principles?
3. What is SRP?
4. What does "one reason to change" mean?
5. What is OCP?
6. What is LSP?
7. What is ISP?
8. What is DIP?

## Intermediate

9. Give a real-world example of SRP.
10. How does polymorphism help with OCP?
11. Give an example of an LSP violation.
12. Why is the Rectangle/Square example often discussed with LSP?
13. What problem does ISP solve?
14. What is the difference between DIP and dependency injection?
15. Why does DIP reduce coupling?
16. How does SOLID improve testability?
17. Can SOLID be overused?
18. Does SOLID mean creating more classes?

## Practical

19. Identify the SOLID violation in a given class.
20. Refactor a large class using SRP.
21. Refactor `if/elif` type-based logic using OCP and polymorphism.
22. Identify an LSP violation in an inheritance hierarchy.
23. Split a large interface according to ISP.
24. Refactor a service using dependency injection.
25. Design a payment system following SOLID.

---

# 52. Quick Revision Table

| Principle | Core Idea | Main Problem |
|---|---|---|
| **S — SRP** | One cohesive responsibility | Classes doing too much |
| **O — OCP** | Extend without unnecessary modification | Constantly changing stable code |
| **L — LSP** | Subtypes must honor parent behavior | Broken inheritance contracts |
| **I — ISP** | Small focused interfaces | Clients depending on unnecessary methods |
| **D — DIP** | Depend on abstractions | Tight coupling to implementations |

---

# 53. One-Line Memory Trick

```text
S → Single Responsibility
O → Open for Extension
L → Legitimate Substitution
I → Interfaces should be focused
D → Depend on abstractions
```

A better exact interview version:

```text
S → One reason to change
O → Open for extension, closed for modification
L → Subtypes must be substitutable
I → Don't force unnecessary dependencies
D → High-level code should depend on abstractions
```

---

# 54. Final SOLID Mental Model

```text
                    SOLID
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ↓             ↓             ↓
       SRP           OCP           LSP
        │             │             │
   Clear roles    Easy extension   Safe substitution
        │             │             │
        └─────────────┼─────────────┘
                      │
                 ┌────┴────┐
                 ↓         ↓
                ISP       DIP
                 │         │
           Focused      Low coupling
           interfaces   + abstractions
```

The overall goal:

```text
                    SOLID
                      ↓
              Better OOP Design
                      ↓
             Lower Coupling
                      ↓
            Higher Cohesion
                      ↓
              Easier Testing
                      ↓
             Easier Extension
                      ↓
           Maintainable Software
```

# 55. Before Moving to Lecture 9

You should be able to look at a Python class and ask:

```text
1. Is this class doing too much?
        → SRP

2. Will new features require modifying this class repeatedly?
        → OCP

3. Can subclasses safely replace their parent?
        → LSP

4. Are clients forced to depend on unnecessary methods?
        → ISP

5. Is high-level code tightly coupled to implementation details?
        → DIP
```

If you can identify these problems in code and explain **why** they are problems, you have understood SOLID.

# OOP Lecture 8 Complete