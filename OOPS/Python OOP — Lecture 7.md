# OOP — Lecture 7
# Abstraction

> **Goal:** Understand abstraction, abstract classes, abstract methods, interfaces in Python, and how abstraction is used with polymorphism in backend development and LLD.

## 1. What Is Abstraction?

**Abstraction** means:

> **Showing only the essential details and hiding unnecessary implementation details.**

Example:

When you use:

```python
car.start()
```

you don't need to know:

```text
How fuel is injected
How the engine works
How the battery works
How the ignition system works
```

You only need to know:

```text
start()
```

The internal implementation is hidden.

---

# 2. Simple Mental Model

```text
User / Caller
      │
      ↓
Simple Interface
      │
      ↓
Hidden Implementation
      │
      ↓
Complex Internal Logic
```

Example:

```python
payment.pay(1000)
```

The caller doesn't need to know:

```text
Bank API
↓
Authentication
↓
Payment gateway
↓
Transaction processing
↓
Database update
↓
Response handling
```

The caller only needs:

```python
pay()
```

---

# 3. Why Do We Need Abstraction?

Without abstraction, users of a class may need to understand too much internal logic.

Example:

```python
payment.connect_to_bank()
payment.authenticate()
payment.validate_card()
payment.process_transaction()
payment.update_database()
```

This exposes too many implementation details.

With abstraction:

```python
payment.pay()
```

The class handles the internal process.

Benefits:

- reduces complexity
- hides implementation details
- provides a clean interface
- reduces coupling
- improves maintainability
- makes systems easier to extend
- useful for LLD and backend architecture

---

# 4. Abstraction vs Encapsulation

These two concepts are often confused.

### Encapsulation

Focuses on:

```text
How do we protect and control data/state?
```

Example:

```python
class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
```

The internal state is controlled through methods.

### Abstraction

Focuses on:

```text
What should the user see?
What implementation details should be hidden?
```

Example:

```python
account.deposit(1000)
```

The caller doesn't need to know how the balance is internally updated.

Mental model:

```text
Encapsulation
    ↓
Protect / control internal state

Abstraction
    ↓
Hide unnecessary implementation complexity
```

---

# 5. Real-World Example

Think about an ATM.

You interact with:

```text
Insert Card
      ↓
Enter PIN
      ↓
Withdraw Money
```

You don't directly interact with:

```text
Bank database
Authentication server
Transaction service
Account validation
ATM hardware communication
```

The ATM provides an abstraction.

You use:

```text
withdraw()
```

without knowing the complete internal process.

---

# 6. Abstraction in Python

Python provides several ways to achieve abstraction.

The most important OOP mechanism is:

```python
ABC
```

and:

```python
@abstractmethod
```

from the:

```python
abc
```

module.

---

# 7. Abstract Base Class

An **Abstract Base Class (ABC)** is a class designed to define a common contract for its subclasses.

Example:

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

Here:

```text
Payment
   ↓
defines what every payment implementation must provide
```

It does not necessarily define how payment happens.

---

# 8. Abstract Method

An abstract method is a method that defines a required operation but does not provide the complete implementation.

Example:

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

The important part is:

```python
@abstractmethod
```

It tells Python:

> Subclasses are expected to implement this method.

---

# 9. Implementing the Abstract Class

Create a subclass:

```python
class CardPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using card")
```

Another:

```python
class UPIPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using UPI")
```

Now:

```text
Payment
   │
   ├── CardPayment
   │      └── pay()
   │
   └── UPIPayment
          └── pay()
```

The abstract class defines the contract.

The child classes provide the implementation.

---

# 10. Why Is This Abstraction?

The parent says:

```python
pay()
```

But it doesn't need to know exactly how every payment method works.

```text
Payment
   ↓
What should happen?
   ↓
pay()
```

Child classes decide:

```text
How should it happen?
```

Example:

```text
CardPayment
    ↓
Card implementation

UPIPayment
    ↓
UPI implementation

WalletPayment
    ↓
Wallet implementation
```

---

# 11. Abstract Class Cannot Be Used Like a Normal Class

Consider:

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

Trying:

```python
payment = Payment()
```

will raise an error because `Payment` contains an abstract method.

The class represents a contract rather than a complete implementation.

---

# 12. Why Prevent Instantiation?

Suppose:

```python
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

What should this do?

```python
Payment().pay(1000)
```

There is no concrete payment mechanism.

Should it use:

```text
Card?
UPI?
Wallet?
Cash?
```

The abstract class doesn't know.

So it defines:

```text
What must exist
```

instead of:

```text
Exactly how it works
```

---

# 13. Abstraction + Polymorphism

These two concepts work very well together.

```text
Abstraction
     ↓
Defines common interface
     ↓
Polymorphism
     ↓
Different implementations
```

Example:

```python
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

Then:

```python
class CardPayment(Payment):

    def pay(self, amount):
        print("Card")


class UPIPayment(Payment):

    def pay(self, amount):
        print("UPI")
```

Caller:

```python
def process_payment(payment, amount):
    payment.pay(amount)
```

The caller knows:

```text
pay()
```

but not the implementation.

This combines abstraction and polymorphism.

---

# 14. Complete Example

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

Usage:

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

---

# 15. The Important Design Idea

The function:

```python
process_payment()
```

doesn't care about:

```text
CardPayment
UPIPayment
WalletPayment
```

It depends on the abstraction:

```text
Payment
   ↓
pay()
```

This is extremely important in LLD.

---

# 16. Abstraction Defines a Contract

A contract means:

```text
"If you belong to this abstraction,
you must provide these operations."
```

Example:

```python
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

Contract:

```text
Payment implementations
        ↓
must provide
        ↓
pay(amount)
```

---

# 17. Multiple Abstract Methods

An abstract class can contain multiple abstract methods.

Example:

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass
```

A concrete subclass must implement both:

```python
class CardPayment(Payment):

    def pay(self, amount):
        print("Card payment")

    def refund(self, amount):
        print("Card refund")
```

---

# 18. Abstract Class Can Have Concrete Methods

Important:

> An abstract class does not have to contain only abstract methods.

It can contain normal methods too.

Example:

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    def log_payment(self, amount):
        print(f"Payment amount: {amount}")
```

Child class:

```python
class CardPayment(Payment):

    def pay(self, amount):
        print("Card payment")
```

Now:

```python
payment = CardPayment()

payment.pay(1000)
payment.log_payment(1000)
```

Output:

```text
Card payment
Payment amount: 1000
```

So an abstract class can contain:

```text
Abstract methods
+
Concrete methods
+
Attributes
```

---

# 19. Why Have Concrete Methods in an Abstract Class?

Sometimes all implementations need the same behavior.

Example:

```text
Payment
   │
   ├── pay()          ← different implementation
   │
   └── log_payment()  ← same implementation
```

This allows common functionality to stay in one place.

---

# 20. Abstract Class With `__init__`

An abstract class can also have an initializer.

Example:

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    def __init__(self, transaction_id):
        self.transaction_id = transaction_id

    @abstractmethod
    def pay(self, amount):
        pass
```

Child:

```python
class CardPayment(Payment):

    def pay(self, amount):
        print(
            f"Payment {amount}, "
            f"Transaction: {self.transaction_id}"
        )
```

Usage:

```python
payment = CardPayment("TXN1001")

payment.pay(1000)
```

The parent can initialize common state.

---

# 21. Abstraction vs Implementation

A useful way to think about abstraction:

```text
WHAT
 ↓
Interface / Contract
```

versus:

```text
HOW
 ↓
Implementation
```

Example:

```text
WHAT:
pay(amount)

HOW:
Card processing
UPI processing
Wallet processing
```

Abstraction focuses on the **WHAT**.

Concrete classes handle the **HOW**.

---

# 22. Real Backend Example

Imagine a backend application that sends emails.

Instead of writing:

```python
def send_email():
    # SMTP implementation
    ...
```

everywhere, define an abstraction:

```python
from abc import ABC, abstractmethod


class EmailService(ABC):

    @abstractmethod
    def send(self, to, subject, body):
        pass
```

Implementation:

```python
class SMTPEmailService(EmailService):

    def send(self, to, subject, body):
        print("Sending email through SMTP")
```

Another implementation:

```python
class SendGridEmailService(EmailService):

    def send(self, to, subject, body):
        print("Sending email through SendGrid")
```

Business logic:

```python
def register_user(email_service, email):
    email_service.send(
        email,
        "Welcome",
        "Welcome to our platform"
    )
```

The business logic doesn't need to know:

```text
SMTP
SendGrid
API calls
Authentication
HTTP requests
```

It only knows:

```python
email_service.send()
```

That is abstraction.

---

# 23. Why This Is Useful in Backend Development

Suppose your application currently uses:

```text
SMTP
```

Later you want:

```text
SendGrid
```

If your business logic directly depends on SMTP:

```text
Business Logic
      ↓
SMTP
```

changing providers becomes harder.

With abstraction:

```text
Business Logic
      ↓
EmailService
      ↓
┌───────────────┐
│               │
SMTP         SendGrid
```

The implementation can change without changing the business logic.

---

# 24. Repository Example

Another common backend pattern is a repository.

Define:

```python
from abc import ABC, abstractmethod


class UserRepository(ABC):

    @abstractmethod
    def get_user(self, user_id):
        pass

    @abstractmethod
    def save_user(self, user):
        pass
```

Implementation:

```python
class MySQLUserRepository(UserRepository):

    def get_user(self, user_id):
        print("Fetching user from MySQL")

    def save_user(self, user):
        print("Saving user to MySQL")
```

Later:

```python
class PostgreSQLUserRepository(UserRepository):

    def get_user(self, user_id):
        print("Fetching user from PostgreSQL")

    def save_user(self, user):
        print("Saving user to PostgreSQL")
```

Service layer:

```python
def get_user_profile(repository, user_id):
    return repository.get_user(user_id)
```

The service depends on:

```text
UserRepository
```

not directly on:

```text
MySQL
```

or:

```text
PostgreSQL
```

This is a very common backend design idea.

---

# 25. Abstraction and Dependency Inversion

This is an important connection for LLD.

Instead of:

```text
Service
  ↓
Concrete Database
```

we can design:

```text
Service
  ↓
Repository Abstraction
  ↓
Concrete Repository
  ↓
Database
```

The high-level service depends on an abstraction.

This idea is a major part of the **Dependency Inversion Principle**, which you will use later in SOLID.

---

# 26. Interface in Python

Python does not have a separate `interface` keyword like Java.

Instead, interface-like designs can be created using:

```text
ABC
+
abstractmethod
```

Example:

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

This behaves like a formal contract.

---

# 27. ABC vs Duck Typing

Python gives us multiple ways to design abstractions.

### Duck typing

```python
def process(payment):
    payment.pay(1000)
```

Any object providing:

```python
pay()
```

can work.

### ABC

```python
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

The expected contract is explicitly defined.

Mental model:

```text
Duck Typing
    ↓
Behavior-based contract

ABC
    ↓
Explicit contract
```

---

# 28. When Should You Use ABC?

ABC can be useful when:

- multiple implementations exist
- a common contract is important
- you are designing an LLD system
- you want clearer architecture
- implementations should follow required methods
- the abstraction is meaningful

Example:

```text
Payment
Notification
Repository
Storage
Cache
Logger
```

---

# 29. When Should You Not Use ABC?

Don't create an abstract class just because you can.

For a tiny piece of code:

```python
def calculate_total(items):
    ...
```

you probably don't need:

```python
class AbstractCalculator(ABC):
    ...
```

Avoid unnecessary abstraction.

Good abstraction should solve a real design problem.

---

# 30. Abstraction Does Not Mean Hiding Everything

Abstraction doesn't mean:

```text
Hide every implementation detail from everyone.
```

It means:

```text
Expose what the caller needs.
Hide what the caller doesn't need.
```

Example:

```python
payment.pay(1000)
```

The caller needs:

```text
pay()
```

The caller doesn't need:

```text
database_connection()
gateway_request()
authentication()
retry_logic()
```

---

# 31. Abstraction and Encapsulation Together

These often work together.

Example:

```python
class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount
```

### Encapsulation

```text
_balance
```

is internal state controlled by the class.

### Abstraction

The user simply calls:

```python
account.withdraw(500)
```

without knowing the internal validation and state update logic.

---

# 32. Abstraction and Polymorphism Together

This is one of the most important combinations.

```text
Abstraction
    ↓
Common contract
    ↓
Polymorphism
    ↓
Different implementations
```

Example:

```python
class Storage(ABC):

    @abstractmethod
    def save(self, data):
        pass
```

Implementations:

```text
MySQLStorage
PostgresStorage
S3Storage
```

All provide:

```python
save()
```

Caller:

```python
storage.save(data)
```

The same call can produce different behavior.

---

# 33. LLD Example — Storage System

Suppose an application needs to store files.

Possible implementations:

```text
Storage
   │
   ├── LocalStorage
   ├── S3Storage
   └── AzureStorage
```

Abstract class:

```python
from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def upload(self, file):
        pass

    @abstractmethod
    def delete(self, file):
        pass
```

Now:

```python
class S3Storage(Storage):

    def upload(self, file):
        print("Uploading to S3")

    def delete(self, file):
        print("Deleting from S3")
```

Another implementation:

```python
class LocalStorage(Storage):

    def upload(self, file):
        print("Saving locally")

    def delete(self, file):
        print("Deleting local file")
```

The application can work with:

```python
Storage
```

rather than directly depending on:

```text
S3
```

or:

```text
Local filesystem
```

---

# 34. Common Mistake #1

Thinking:

```text
Abstract class = class with only abstract methods
```

Not true.

An abstract class can contain:

```text
abstract methods
+
normal methods
+
attributes
+
__init__
```

---

# 35. Common Mistake #2

Thinking abstraction and encapsulation are identical.

They are related but different.

```text
Encapsulation
→ Control/protect state and behavior

Abstraction
→ Hide unnecessary complexity and expose essential behavior
```

---

# 36. Common Mistake #3

Creating abstraction everywhere.

Bad:

```text
Simple function
      ↓
Abstract class
      ↓
Interface
      ↓
Factory
      ↓
Five implementations
```

for a problem that only needs:

```python
def calculate():
    ...
```

Abstraction should solve complexity, not create complexity.

---

# 37. Common Mistake #4

Putting implementation details into the abstraction

Bad design:

```python
class Payment(ABC):

    def pay(self):
        connect_to_mysql()
        call_specific_card_api()
        send_email()
```

The abstraction should represent the common contract.

Concrete implementations should handle implementation-specific behavior.

---

# 38. Common Mistake #5

Confusing Abstract Class With Object

An abstract class defines a contract.

A concrete class provides an implementation.

Example:

```text
Payment
   ↓
Abstract concept

CardPayment
   ↓
Concrete implementation
```

---

# 39. Interview Question: What Is Abstraction?

### Answer

Abstraction is the OOP concept of exposing essential behavior while hiding unnecessary implementation details.

In Python, abstraction can be implemented using abstract base classes with `ABC` and `@abstractmethod`, as well as through interface-like designs and duck typing.

---

# 40. Interview Question: How Do You Implement Abstraction in Python?

Common approaches include:

```text
1. ABC
2. @abstractmethod
3. Duck typing
4. Interface-like contracts
```

Example:

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

---

# 41. Interview Question: What Is an Abstract Method?

An abstract method is a method declared as part of an abstract contract that concrete subclasses are expected to implement.

Example:

```python
@abstractmethod
def pay(self, amount):
    pass
```

---

# 42. Interview Question: Can an Abstract Class Have Normal Methods?

Yes.

Example:

```python
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    def log(self):
        print("Logging payment")
```

An abstract class can contain both abstract and concrete methods.

---

# 43. Interview Question: Can an Abstract Class Have `__init__()`?

Yes.

Example:

```python
class Payment(ABC):

    def __init__(self, transaction_id):
        self.transaction_id = transaction_id

    @abstractmethod
    def pay(self, amount):
        pass
```

The child class can use the inherited initialization.

---

# 44. Interview Question: Can We Instantiate an Abstract Class?

Normally, no, if it still contains unimplemented abstract methods.

Example:

```python
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

This cannot be instantiated directly:

```python
payment = Payment()
```

A concrete subclass must implement the abstract methods.

---

# 45. Interview Question: Abstraction vs Encapsulation?

### Encapsulation

```text
Focus:
How to control/protect internal state?
```

### Abstraction

```text
Focus:
What should the caller see?
What implementation details should be hidden?
```

Example:

```text
BankAccount
    ↓
_balance → encapsulation

withdraw() → abstraction
```

---

# 46. Interview Question: Abstraction vs Polymorphism?

### Abstraction

Defines:

```text
Common interface / contract
```

### Polymorphism

Allows:

```text
Different implementations
through the common interface
```

Relationship:

```text
Abstraction
     ↓
Common contract
     ↓
Polymorphism
     ↓
Different behavior
```

---

# 47. Interview Question: Does Python Have Interfaces?

Python doesn't have a separate `interface` keyword like Java.

However, interface-like contracts can be created using:

```python
ABC
```

and:

```python
@abstractmethod
```

Python can also use duck typing for behavior-based interfaces.

---

# 48. Interview Question: Why Use Abstraction in Backend Systems?

Abstraction allows high-level business logic to depend on stable interfaces instead of implementation-specific details.

Example:

```text
Business Logic
      ↓
EmailService
      ↓
SMTP / SendGrid
```

instead of:

```text
Business Logic
      ↓
SMTP implementation
```

This makes implementations easier to replace and test.

---

# 49. Interview Question: Why Is Abstraction Important in LLD?

Abstraction helps:

- separate interface from implementation
- reduce coupling
- support polymorphism
- make systems extensible
- make responsibilities clearer
- support dependency inversion
- simplify complex systems

---

# 50. Complete LLD Example

```python
from abc import ABC, abstractmethod


class NotificationService(ABC):

    @abstractmethod
    def send(self, recipient, message):
        pass


class EmailNotification(NotificationService):

    def send(self, recipient, message):
        print(f"Email → {recipient}: {message}")


class SMSNotification(NotificationService):

    def send(self, recipient, message):
        print(f"SMS → {recipient}: {message}")


class PushNotification(NotificationService):

    def send(self, recipient, message):
        print(f"Push → {recipient}: {message}")


class NotificationManager:

    def __init__(self, service):
        self.service = service

    def notify(self, recipient, message):
        self.service.send(recipient, message)
```

Usage:

```python
email_service = EmailNotification()

manager = NotificationManager(email_service)

manager.notify(
    "user@example.com",
    "Welcome!"
)
```

The important architecture is:

```text
NotificationManager
        ↓
NotificationService
        ↓
┌──────────────┬──────────────┐
↓              ↓              ↓
Email          SMS            Push
```

`NotificationManager` doesn't need to know how each notification is sent.

It depends on the abstraction.

---

# 51. Four OOP Pillars — Complete View

You have now covered all four major OOP pillars:

```text
                     OOP
                      │
       ┌──────────────┼──────────────┐
       │              │              │
       ↓              ↓              ↓
Encapsulation    Inheritance    Polymorphism
       │              │              │
       ↓              ↓              ↓
 Protect State    Reuse/Extend   Multiple Behaviors
       │              │              │
       └──────────────┼──────────────┘
                      ↓
                 Abstraction
                      │
                      ↓
              Hide Complexity
              Expose Essentials
```

More simply:

```text
Encapsulation
→ Protect/control internal state

Inheritance
→ Reuse and specialize behavior

Polymorphism
→ Same interface, different behavior

Abstraction
→ Hide unnecessary implementation details
```

---

# 52. How the Four Pillars Work Together

Consider:

```text
Payment System
```

### Encapsulation

Payment object controls its internal state.

### Inheritance

```text
Payment
   ↓
CardPayment
UPIPayment
WalletPayment
```

### Abstraction

Payment defines:

```python
pay()
```

### Polymorphism

Each payment implements:

```python
pay()
```

differently.

Together:

```text
                    Payment
                       │
                ┌──────┴──────┐
                │             │
           Abstraction    Encapsulation
                │             │
                ↓             ↓
              pay()      internal state
                │
                ↓
           Polymorphism
                │
       ┌────────┼────────┐
       ↓        ↓        ↓
     Card      UPI     Wallet
```

This is how OOP concepts are normally used together in real systems.

---

# 53. Final Mental Model

Remember:

```text
Abstraction
     ↓
"What should the caller know?"
     ↓
Expose essential behavior
     ↓
Hide unnecessary implementation
```

And:

```text
ABC
 ↓
Common Contract
 ↓
Concrete Implementations
 ↓
Polymorphism
 ↓
Flexible Design
```

---

# 54. Quick Revision

### Abstraction

```text
Hide unnecessary complexity
Expose essential behavior
```

### ABC

```python
from abc import ABC
```

### Abstract Method

```python
@abstractmethod
```

### Contract

```text
Defines what implementations must provide
```

### Concrete Class

```text
Provides the actual implementation
```

### Backend

```text
Business Logic
      ↓
Abstraction
      ↓
Concrete Service
```

### LLD

```text
High-level code
      ↓
Interface / Abstraction
      ↓
Multiple implementations
```

---

# 55. Must-Know Interview Checklist

Before moving forward, you should be able to explain:

- What is abstraction?
- Why is abstraction needed?
- Abstraction vs encapsulation?
- What is an abstract class?
- What is `ABC`?
- What is `@abstractmethod`?
- Can an abstract class have normal methods?
- Can an abstract class have `__init__()`?
- Can we instantiate an abstract class?
- What is an abstract method?
- What is an interface?
- Does Python have an `interface` keyword?
- How can Python implement interface-like behavior?
- ABC vs duck typing?
- Abstraction vs polymorphism?
- How does abstraction reduce coupling?
- How is abstraction used in backend development?
- How is abstraction used in LLD?
- How does abstraction support dependency inversion?
- Why shouldn't abstraction be overused?

# OOP Lecture 7 Complete