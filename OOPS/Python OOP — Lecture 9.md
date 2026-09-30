# OOP — Lecture 9
# Composition vs Inheritance + Association & Aggregation

> **Goal:** Understand how objects relate to each other in Python, when to use inheritance, when to use composition, and the difference between association, aggregation, and composition.
>
> This lecture is important because good OOP design is not only about creating classes. It is also about deciding **how those classes should be connected**.

## 1. Why Object Relationships Matter

When designing a system, classes rarely work completely independently.

For example, in a school management system:

```text
School
  ↓
Teachers
  ↓
Students
  ↓
Courses
```

Or in an e-commerce system:

```text
Order
  ↓
Customer
  ↓
Payment
  ↓
Product
```

The important question becomes:

> **How should these objects relate to each other?**

Common relationships include:

```text
Inheritance
Association
Aggregation
Composition
```

Understanding these relationships is essential for writing maintainable OOP code.

## 2. Two Major Ways Classes Relate

At a high level, relationships often fall into two categories:

```text
"is-a"
```

and:

```text
"has-a"
```

### Is-a

Usually represented by:

```text
Inheritance
```

Example:

```text
Dog is an Animal
```

### Has-a

Usually represented by:

```text
Composition / Aggregation
```

Example:

```text
Car has an Engine
```

Mental model:

```text
IS-A
  ↓
Inheritance

HAS-A
  ↓
Composition / Aggregation
```

## 3. Inheritance

You already learned inheritance in Lecture 5.

Inheritance represents an:

```text
is-a
```

relationship.

Example:

```python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    pass
```

Here:

```text
Dog is an Animal
```

Therefore:

```text
Animal
   ↑
   │
  Dog
```

## 4. Why Inheritance Is Useful

Inheritance can provide:

- code reuse
- specialization
- method overriding
- polymorphism
- shared behavior

Example:

```python
class Employee:

    def work(self):
        print("Employee working")


class Developer(Employee):

    def write_code(self):
        print("Writing code")
```

`Developer` inherits:

```python
work()
```

and adds:

```python
write_code()
```

## 5. The Problem With Overusing Inheritance

Inheritance creates a strong relationship between classes.

Example:

```text
Parent
  ↓
Child
```

The child depends on the parent structure and behavior.

If the hierarchy becomes deep:

```text
A
 ↓
B
 ↓
C
 ↓
D
 ↓
E
```

the design can become difficult to understand and modify.

A change near the top can affect many classes below it.

This is why inheritance should be used carefully.

## 6. Composition

Composition represents a:

```text
has-a
```

relationship.

Instead of inheriting behavior, an object contains another object.

Example:

```python
class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self):
        self.engine = Engine()
```

Now:

```text
Car
 │
 └── has an Engine
```

The relationship is:

```text
Car HAS-A Engine
```

not:

```text
Car IS-A Engine
```

## 7. Using Composition

```python
class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car started")
```

Usage:

```python
car = Car()

car.start()
```

Output:

```text
Engine started
Car started
```

The `Car` delegates engine-related behavior to its `Engine`.

## 8. Composition Mental Model

```text
Car
 │
 ├── Engine
 │
 ├── Transmission
 │
 └── Battery
```

Instead of:

```text
Car
  ↓
inherits from Engine
```

we have:

```text
Car
  ↓
contains Engine
```

This is composition.

## 9. Inheritance vs Composition

Compare:

### Inheritance

```text
Dog
  ↓
Animal
```

Meaning:

```text
Dog IS-A Animal
```

### Composition

```text
Car
  ↓
Engine
```

Meaning:

```text
Car HAS-A Engine
```

A simple rule:

```text
IS-A  → Inheritance

HAS-A → Composition/Aggregation
```

## 10. Composition Example — Computer

A computer can contain:

```text
Computer
   │
   ├── CPU
   ├── RAM
   ├── Storage
   └── PowerSupply
```

Python:

```python
class CPU:

    def process(self):
        print("CPU processing")


class RAM:

    def load(self):
        print("RAM loading")


class Computer:

    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
```

Now:

```python
computer = Computer()

computer.cpu.process()
computer.ram.load()
```

The `Computer` is composed of other objects.

## 11. Why Composition Is Powerful

Composition allows us to build complex objects from smaller objects.

Instead of creating:

```text
One giant class
```

we create:

```text
Small focused classes
       ↓
Combine them
       ↓
Create larger behavior
```

Example:

```text
Order
 │
 ├── Customer
 ├── Payment
 ├── Address
 └── OrderItems
```

Each object has its own responsibility.

## 12. Composition and Encapsulation

Composition also works well with encapsulation.

Example:

```python
class Engine:

    def start(self):
        print("Engine started")
```

```python
class Car:

    def __init__(self):
        self._engine = Engine()

    def start(self):
        self._engine.start()
```

The caller only needs:

```python
car.start()
```

The `Car` controls how the `Engine` is used.

This combines:

```text
Composition
+
Encapsulation
```

## 13. Composition and Polymorphism

Composition can also use polymorphism.

Suppose:

```python
class Payment:

    def pay(self, amount):
        pass
```

Different implementations:

```python
class CardPayment(Payment):

    def pay(self, amount):
        print("Card payment")
```

```python
class UPIPayment(Payment):

    def pay(self, amount):
        print("UPI payment")
```

Now:

```python
class OrderService:

    def __init__(self, payment):
        self.payment = payment

    def checkout(self, amount):
        self.payment.pay(amount)
```

Usage:

```python
service = OrderService(CardPayment())

service.checkout(1000)
```

We can change the behavior:

```python
service = OrderService(UPIPayment())

service.checkout(1000)
```

The `OrderService` doesn't need to inherit from payment classes.

It **has a payment object**.

## 14. Composition Over Inheritance

You may hear:

> **Favor composition over inheritance.**

This does not mean:

```text
Never use inheritance.
```

It means:

> When both inheritance and composition can reasonably solve the problem, composition can often provide more flexibility and lower coupling.

Example:

```text
Inheritance:

OrderService
    ↓
CardPaymentService
```

This creates a strong class hierarchy.

Composition:

```text
OrderService
    ↓
   HAS-A
    ↓
  Payment
    ↓
CardPayment / UPIPayment
```

The payment implementation can be supplied independently.

## 15. When Inheritance Makes Sense

Inheritance is appropriate when the relationship is genuinely:

```text
IS-A
```

Example:

```text
Dog is an Animal
Manager is an Employee
SavingsAccount is an Account
```

There should also be meaningful shared behavior or contract.

## 16. When Composition Makes Sense

Composition is useful when the relationship is:

```text
HAS-A
```

Examples:

```text
Car has an Engine
Order has Payment
Computer has CPU
UserService has Repository
Restaurant has Menu
```

Composition is especially useful when components may need to be replaced or configured independently.

## 17. Association

Now let's introduce another important relationship:

> **Association**

Association means:

> Two objects know about or interact with each other, but neither necessarily owns the other.

Example:

```text
Teacher
   ↔
Student
```

A teacher interacts with students.

A student interacts with a teacher.

But:

```text
Teacher does not own Student
Student does not own Teacher
```

This is association.

## 18. Simple Association Example

```python
class Teacher:

    def teach(self):
        print("Teaching")


class Student:

    def learn(self):
        print("Learning")
```

Suppose a teacher works with a student:

```python
class Teacher:

    def teach(self, student):
        print("Teaching student")
        student.learn()
```

The teacher interacts with the student.

But the teacher does not necessarily create or own the student.

## 19. Association Mental Model

```text
Teacher ───────── Student
```

The relationship simply means:

```text
Teacher interacts with Student
```

It does not automatically mean:

```text
Teacher owns Student
```

## 20. Real-World Association Examples

Examples:

```text
Doctor ───── Patient
Teacher ──── Student
Customer ─── Salesperson
Driver ───── Vehicle
User ─────── Product
```

The objects can exist independently.

For example:

```text
A Student can exist without a Teacher object.
A Teacher can exist without a Student object.
```

That is a strong indication of association.

## 21. Aggregation

Aggregation is a more specific form of "has-a" relationship.

It represents:

> A whole has references to parts, but the parts can exist independently of the whole.

Example:

```text
Department
     │
     ├── Teacher
     ├── Teacher
     └── Teacher
```

A department has teachers.

But teachers can exist independently of that particular department.

## 22. Aggregation Example

```python
class Teacher:

    def __init__(self, name):
        self.name = name


class Department:

    def __init__(self, teachers):
        self.teachers = teachers
```

Create teachers independently:

```python
teacher1 = Teacher("Amit")
teacher2 = Teacher("Rahul")
```

Then create department:

```python
department = Department([
    teacher1,
    teacher2
])
```

The teachers existed before the department.

They can also exist after the department is removed.

That represents aggregation.

## 23. Aggregation Mental Model

```text
Department
    │
    ├──────── Teacher 1
    │
    ├──────── Teacher 2
    │
    └──────── Teacher 3
```

The department references teachers.

But:

```text
Teacher lifecycle
        ≠
Department lifecycle
```

The teachers can survive independently.

## 24. Composition vs Aggregation

This distinction is important.

### Composition

```text
Strong ownership
```

The contained object's lifecycle is generally tied to the owner.

### Aggregation

```text
Weak ownership
```

The contained object can exist independently.

Mental model:

```text
Composition
    ↓
Strong has-a
    ↓
Part depends on whole

Aggregation
    ↓
Weak has-a
    ↓
Part can exist independently
```

## 25. Composition Example

```python
class Engine:

    def __init__(self):
        print("Engine created")


class Car:

    def __init__(self):
        self.engine = Engine()
```

The `Car` creates its own `Engine`.

```python
car = Car()
```

The engine is created as part of constructing the car.

This represents strong ownership.

## 26. Aggregation Example

```python
class Engine:

    def __init__(self):
        print("Engine created")


class Car:

    def __init__(self, engine):
        self.engine = engine
```

Now:

```python
engine = Engine()

car = Car(engine)
```

The engine exists independently.

The car simply receives a reference to it.

This is a common aggregation/composition boundary in Python.

## 27. Important Python Perspective

Python does not enforce:

```text
Association
Aggregation
Composition
```

through special language keywords.

These are **design relationships**.

We communicate them through:

```python
object references
```

and:

```python
object ownership/lifecycle
```

The exact distinction often depends on the design intent.

## 28. Composition Through Constructor Injection

Composition doesn't always mean:

```python
self.engine = Engine()
```

We can inject the dependency:

```python
class Car:

    def __init__(self, engine):
        self.engine = engine
```

Then:

```python
engine = Engine()

car = Car(engine)
```

This gives us more flexibility.

It also connects to:

```text
Dependency Injection
```

which you learned as part of SOLID/DIP.

## 29. Composition + Dependency Injection

Example:

```python
class Engine:

    def start(self):
        print("Engine started")
```

```python
class Car:

    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()
```

Usage:

```python
engine = Engine()

car = Car(engine)

car.start()
```

The `Car` doesn't create the dependency itself.

The dependency is injected.

## 30. Composition With Different Implementations

Suppose we have:

```python
class PetrolEngine:

    def start(self):
        print("Petrol engine started")
```

```python
class ElectricEngine:

    def start(self):
        print("Electric engine started")
```

Car:

```python
class Car:

    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()
```

Now:

```python
petrol_car = Car(PetrolEngine())
electric_car = Car(ElectricEngine())
```

Both use the same `Car` class.

The behavior changes based on the injected object.

This combines:

```text
Composition
+
Polymorphism
+
Dependency Injection
```

## 31. Why This Is Better Than Inheritance Here

We could try:

```text
PetrolCar
ElectricCar
DieselCar
HybridCar
```

and put engine behavior into the inheritance hierarchy.

But the engine is really a component of the car.

It is not:

```text
Car IS-A PetrolEngine
```

It is:

```text
Car HAS-A Engine
```

Composition models the domain more naturally.

## 32. Association vs Aggregation vs Composition

A useful comparison:

| Relationship | Meaning | Ownership | Lifecycle |
|---|---|---|---|
| Association | Objects interact | None/weak | Independent |
| Aggregation | Whole has parts | Weak | Parts can exist independently |
| Composition | Whole owns parts | Strong | Part lifecycle tied to whole |

Examples:

```text
Association:
Doctor ↔ Patient

Aggregation:
Department → Teachers

Composition:
House → Rooms
```

## 33. Association vs Aggregation

Association:

```text
Teacher ───── Student
```

means:

```text
Teacher interacts with Student
```

Aggregation:

```text
Department ───── Teacher
```

means:

```text
Department contains/references Teachers
```

The difference is mainly about:

```text
"whole-part" relationship
```

Aggregation has a stronger structural relationship than general association.

## 34. Aggregation vs Composition

Both are:

```text
HAS-A
```

relationships.

The key difference is ownership/lifecycle.

### Aggregation

```text
Department
    ↓
Teacher
```

Teacher can exist without Department.

### Composition

```text
House
   ↓
Room
```

The room is considered a part of that house and its lifecycle is conceptually tied to the house.

## 35. Practical Python Example

Let's compare three relationships.

### Association

```python
class Doctor:

    def treat(self, patient):
        print(f"Treating {patient.name}")


class Patient:

    def __init__(self, name):
        self.name = name
```

The doctor interacts with the patient.

### Aggregation

```python
class Teacher:

    def __init__(self, name):
        self.name = name


class Department:

    def __init__(self, teachers):
        self.teachers = teachers
```

Teachers are created outside the department.

### Composition

```python
class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self):
        self.engine = Engine()
```

The car creates its engine internally.

## 36. Inheritance vs Composition — Decision Framework

When deciding between inheritance and composition, ask:

### Question 1

Is there a genuine:

```text
IS-A
```

relationship?

If yes, inheritance may be appropriate.

### Question 2

Is there a:

```text
HAS-A
```

relationship?

If yes, composition/aggregation may be more appropriate.

### Question 3

Do I want to replace the behavior dynamically?

If yes, composition can be useful.

### Question 4

Is the child genuinely substitutable for the parent?

If no, don't force inheritance.

### Question 5

Will the hierarchy become complicated?

If yes, consider composition.

## 37. Example — Payment System

Bad inheritance model:

```text
Payment
   ↑
OrderService
```

This would imply:

```text
OrderService IS-A Payment
```

which is incorrect.

Better:

```text
OrderService
     ↓
    HAS-A
     ↓
   Payment
```

Example:

```python
class OrderService:

    def __init__(self, payment):
        self.payment = payment

    def checkout(self, amount):
        self.payment.pay(amount)
```

This models the relationship correctly.

## 38. Example — Logger

Suppose:

```python
class Logger:

    def log(self, message):
        print(message)
```

And:

```python
class UserService:

    def __init__(self, logger):
        self.logger = logger

    def create_user(self):
        self.logger.log("Creating user")
```

`UserService` is not a Logger.

It:

```text
HAS-A Logger
```

Therefore composition is more appropriate than inheritance.

## 39. Example — Repository

```python
class UserRepository:

    def save(self, user):
        print("Saving user")
```

```python
class UserService:

    def __init__(self, repository):
        self.repository = repository

    def create_user(self, user):
        self.repository.save(user)
```

Relationship:

```text
UserService
     │
     └── HAS-A → UserRepository
```

Not:

```text
UserService IS-A UserRepository
```

## 40. Composition and SOLID

Composition works very well with SOLID.

### SRP

Small classes can have focused responsibilities.

### OCP

Different components can be added without changing the main class.

### DIP

Dependencies can be injected.

### LSP

Polymorphic components can implement common abstractions.

### ISP

Components can depend on focused interfaces.

This is why composition is so common in maintainable software design.

## 41. Common Mistake #1

Thinking:

```text
Composition = inheritance
```

No.

```text
Inheritance:
IS-A

Composition:
HAS-A
```

## 42. Common Mistake #2

Using inheritance just for code reuse.

Example:

```python
class Car(Engine):
    pass
```

This technically gives access to engine methods, but semantically:

```text
Car IS-A Engine
```

is incorrect.

Use composition:

```python
class Car:

    def __init__(self):
        self.engine = Engine()
```

## 43. Common Mistake #3

Creating Deep Inheritance Hierarchies

Avoid unnecessarily deep structures:

```text
A
 ↓
B
 ↓
C
 ↓
D
 ↓
E
```

Ask whether some behavior should instead be composed.

## 44. Common Mistake #4

Confusing Aggregation and Composition

Remember:

```text
Aggregation
→ Parts can exist independently.

Composition
→ Strong ownership / lifecycle relationship.
```

## 45. Common Mistake #5

Thinking Composition Requires Creating Objects Internally

Composition can also be implemented through dependency injection:

```python
class Car:

    def __init__(self, engine):
        self.engine = engine
```

The object receives the component from outside.

This is often more flexible.

## 46. Common Mistake #6

Assuming Python Enforces These Relationships

Python doesn't have:

```python
class Car has Engine
```

or:

```python
@composition
```

These are design concepts.

Python uses:

```python
self.engine
```

and object references to represent them.

## 47. Interview Question: Inheritance vs Composition?

### Answer

Inheritance represents an **is-a** relationship, while composition represents a **has-a** relationship.

Example:

```text
Dog IS-A Animal
Car HAS-A Engine
```

Inheritance creates a class hierarchy, while composition builds objects by combining smaller objects.

## 48. Interview Question: Why Prefer Composition Over Inheritance?

Composition can:

- reduce coupling
- avoid deep inheritance hierarchies
- allow behavior to be replaced
- make components independently testable
- improve flexibility
- support dependency injection

However, inheritance is still appropriate when there is a genuine is-a relationship and the subclass can correctly satisfy the parent contract.

## 49. Interview Question: What Is Association?

Association is a general relationship where two independent objects know about or interact with each other.

Example:

```text
Doctor ↔ Patient
```

Neither object necessarily owns the other.

## 50. Interview Question: What Is Aggregation?

Aggregation is a weak whole-part relationship where the contained objects can exist independently.

Example:

```text
Department
    ↓
Teachers
```

A teacher can exist independently of a particular department.

## 51. Interview Question: What Is Composition?

Composition is a strong whole-part relationship where the contained object's lifecycle is conceptually tied to the owning object.

Example:

```text
House
  ↓
Rooms
```

The room is treated as a part of the house.

## 52. Interview Question: Difference Between Aggregation and Composition?

### Aggregation

```text
Weak ownership
Parts can exist independently
```

### Composition

```text
Strong ownership
Part lifecycle is tied to whole
```

Mental model:

```text
Aggregation:
"I have this object."

Composition:
"This object is a part of me."
```

## 53. Interview Question: Can Composition Use Dependency Injection?

Yes.

Example:

```python
class Car:

    def __init__(self, engine):
        self.engine = engine
```

Then:

```python
car = Car(Engine())
```

The `Car` contains the engine, but the dependency is provided from outside.

This is useful for flexibility and testing.

## 54. Interview Question: Is Composition Always Better Than Inheritance?

No.

The correct answer is:

> Composition is often more flexible and can reduce coupling, but inheritance is appropriate when there is a genuine is-a relationship and the child can correctly satisfy the parent contract.

Don't say:

```text
"Always use composition."
```

## 55. Interview Question: How Does Composition Help Testing?

Suppose:

```python
class UserService:

    def __init__(self, repository):
        self.repository = repository
```

During testing, we can inject:

```text
FakeRepository()
```

instead of:

```text
MySQLRepository()
```

This makes the service easier to test independently.

## 56. Composition + Polymorphism + Dependency Injection

This is a very important Python design combination.

```text
Common abstraction
       ↓
Multiple implementations
       ↓
Inject implementation
       ↓
Compose object
       ↓
Caller uses common behavior
```

Example:

```python
class Payment:

    def pay(self, amount):
        pass
```

```python
class CardPayment(Payment):

    def pay(self, amount):
        print("Card")
```

```python
class UPIPayment(Payment):

    def pay(self, amount):
        print("UPI")
```

```python
class OrderService:

    def __init__(self, payment):
        self.payment = payment

    def checkout(self, amount):
        self.payment.pay(amount)
```

Now:

```python
order1 = OrderService(CardPayment())
order2 = OrderService(UPIPayment())
```

Same `OrderService`.

Different behavior.

This is a very common design technique.

## 57. Big Picture

You have now learned:

```text
Inheritance
    ↓
IS-A

Composition
    ↓
HAS-A

Association
    ↓
Objects interact

Aggregation
    ↓
Weak whole-part relationship

Composition
    ↓
Strong whole-part relationship
```

## 58. Relationship Diagram

```text
                    Object Relationships
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ↓             ↓             ↓
        Inheritance    Association    Has-A
             │             │             │
            IS-A       interacts       │
                                       │
                              ┌────────┴────────┐
                              ↓                 ↓
                         Aggregation       Composition
                              │                 │
                         Weak ownership    Strong ownership
                         Independent       Lifecycle tied
```

## 59. Final Decision Cheat Sheet

Use:

```text
IS-A
 ↓
Inheritance
```

Use:

```text
HAS-A
 ↓
Composition / Aggregation
```

Use:

```text
INTERACTS-WITH
 ↓
Association
```

Use:

```text
Whole + independent parts
 ↓
Aggregation
```

Use:

```text
Whole + strongly owned parts
 ↓
Composition
```

## 60. Quick Revision

### Inheritance

```text
Dog IS-A Animal
```

### Composition

```text
Car HAS-A Engine
```

### Association

```text
Doctor interacts with Patient
```

### Aggregation

```text
Department has Teachers
```

Teachers can exist independently.

### Composition

```text
Car has Engine
```

when the design treats the engine as a strongly owned component.

## 61. Must-Know Interview Checklist

Before moving to the next lecture, you should be able to explain:

- What is inheritance?
- What is composition?
- What is the difference between is-a and has-a?
- Why can composition reduce coupling?
- Why is composition often preferred over inheritance?
- When should inheritance be used?
- When should composition be used?
- What is association?
- What is aggregation?
- What is composition?
- Association vs aggregation?
- Aggregation vs composition?
- How are these relationships represented in Python?
- Does Python have a special keyword for composition?
- Can composition use dependency injection?
- How does composition work with polymorphism?
- How does composition support SOLID?
- Give a real-world example of each relationship.
- Identify whether a given relationship should use inheritance or composition.
- Explain why using inheritance only for code reuse can be a bad design.

# OOP Lecture 9 Complete