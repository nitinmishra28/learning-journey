# Lecture 13 — Python OOP Interview + Practical Practice

This lecture is focused on **testing whether I can actually apply Python OOP concepts in code**, not just explain the theory.

The goal is to take everything learned in the previous OOP lectures and use it to solve practical, real-world problems.

## What I Already Know

By this point, I have covered:

- Classes and Objects
- `__init__`
- Instance Variables
- Class Variables
- Instance Methods
- Class Methods
- Static Methods
- Encapsulation
- Properties
- Inheritance
- Method Overriding
- `super()`
- Polymorphism
- Duck Typing
- Abstraction
- Abstract Classes
- SOLID Principles
- Composition
- Association
- Aggregation
- Object Introspection
- Dunder Methods
- Python Object Model basics

This lecture is **not another theory lecture**.

It is about applying these concepts.

## Main Goal

I should be able to look at a small software requirement and decide:

- What classes are required?
- What should each class be responsible for?
- Which data belongs to which object?
- Which methods belong to which class?
- Should I use inheritance?
- Should I use composition?
- Where should encapsulation be used?
- Where does polymorphism make sense?
- Should a dependency be injected?
- How should objects interact?
- How can I keep the design simple and maintainable?

The goal is to move from:

```text
"I understand OOP"
```

to:

```text
"I can build software using OOP"
```

## Practice Method

I will solve **one practical problem at a time**.

The difficulty will gradually increase.

### Problem progression

```text
Problem 1
   ↓
Medium
   ↓
Problem 2
   ↓
Medium+
   ↓
Problem 3
   ↓
Advanced
   ↓
Problem 4+
   ↓
Interview-level
```

I should not jump directly into very complex systems.

The objective is to build OOP design ability gradually.

# How Each Problem Will Be Given

For every problem, the problem statement should contain only:

1. Problem Statement
2. Constraints
3. Example
4. Suggested Classes and Relationships
5. What to Implement
6. Test Cases
7. Hints if Stuck

The initial problem should **not contain the solution**.

I should first attempt the implementation myself.

## 1. Problem Statement

Describe a small real-world software requirement.

Example domains:

- Bank Account System
- Employee Management System
- Library Management System
- Payment System
- Notification System
- Food Ordering System
- Parking System
- Shopping Cart
- Vehicle Rental
- Student Management System

The problem should resemble something that could exist inside a real application.

## 2. Constraints

Clearly define important rules.

For example:

```text
- Account balance cannot become negative.
- A customer can have multiple accounts.
- A transaction must have a valid amount.
- A payment cannot be processed twice.
```

Constraints should force me to think about:

- Encapsulation
- Validation
- Object relationships
- Responsibilities
- State management

## 3. Example

Provide a small example showing expected behavior.

Example:

```text
Account balance = 5000

Deposit 2000
→ Balance = 7000

Withdraw 3000
→ Balance = 4000
```

The example should explain the expected behavior without giving away the implementation.

## 4. Suggested Classes and Relationships

Provide the classes I should consider, but **do not provide code**.

Example:

```text
Customer
    |
    | has
    ↓
BankAccount
    |
    | creates
    ↓
Transaction
```

Explain relationships such as:

```text
Customer
    ↓
has
    ↓
BankAccount
```

or:

```text
PaymentProcessor
    ↓
uses
    ↓
PaymentMethod
```

But do not provide the implementation.

## 5. What to Implement

Give a detailed checklist of functionality.

Example:

```text
Customer
- Store customer information
- Add an account
- Retrieve an account

BankAccount
- Deposit money
- Withdraw money
- Check balance
- Validate transactions

Transaction
- Store transaction information
- Store transaction type
- Store transaction amount
```

This tells me what the software must do while leaving the actual implementation to me.

## 6. Test Cases

Provide test cases that I can use after implementing the solution.

Example:

```text
Test Case 1
Create a customer.

Expected:
Customer should be created successfully.
```

```text
Test Case 2
Deposit money into an account.

Expected:
Account balance should increase correctly.
```

```text
Test Case 3
Withdraw more money than available.

Expected:
Transaction should be rejected.
```

Test cases should cover:

- Normal behavior
- Invalid input
- Boundary cases
- Object interactions
- Business rules

## 7. Hints

Hints should be provided only to help me get unstuck.

Hints should **not contain the complete solution**.

Example:

```text
Hint 1:
Think about which object owns the balance.

Hint 2:
The object that owns the balance should probably control
how that balance changes.
```

If I still cannot solve it, progressively stronger hints can be given.

# OOP Concepts I Must Apply

The problems should gradually require me to use the concepts I learned.

## Classes and Objects

I should identify real-world entities and represent them using classes.

```text
Real-world entity
       ↓
     Class
       ↓
     Object
```

Example:

```text
Employee
   ↓
employee1
employee2
employee3
```

## Encapsulation

I should protect important internal state and control how it changes.

For example:

```text
balance
salary
order_status
payment_status
```

Instead of allowing arbitrary modification:

```python
account.balance = -50000
```

I should design appropriate operations that maintain valid state.

## Inheritance

I should use inheritance only when there is a genuine:

```text
IS-A
```

relationship.

Example:

```text
Employee
   ↑
   |
Manager
```

I should avoid inheritance merely because two classes share some code.

## Polymorphism

I should identify situations where different objects should support the same interface but behave differently.

Example:

```text
Payment
   ↑
   ├── CardPayment
   ├── UPIPayment
   └── CashPayment
```

The caller should be able to work with the common behavior without depending unnecessarily on the concrete implementation.

## Abstraction

I should hide implementation details when the user of the object only needs the public behavior.

Think:

```text
WHAT
 ↓
Public interface
 ↓
HOW
 ↓
Internal implementation
```

## Composition

I should recognize:

```text
HAS-A
```

relationships.

Example:

```text
Order
  |
  ├── Customer
  ├── Product
  └── Payment
```

Composition should often be preferred when one object needs another object to perform its work.

## Association

I should recognize when two objects simply interact with each other without strong ownership.

Example:

```text
Teacher
   ↔
Student
```

## Aggregation

I should recognize relationships where one object contains or manages other objects but those objects can conceptually exist independently.

Example:

```text
Department
    |
    ├── Employee
    ├── Employee
    └── Employee
```

## SOLID Principles

As difficulty increases, I should consider:

### Single Responsibility Principle

Ask:

```text
Does this class have one clear responsibility?
```

### Open/Closed Principle

Ask:

```text
Can I add a new behavior without constantly modifying
existing working code?
```

### Liskov Substitution Principle

Ask:

```text
Can the child object genuinely behave as the parent type?
```

### Interface Segregation Principle

Ask:

```text
Am I forcing a class to implement behavior it doesn't need?
```

### Dependency Inversion Principle

Ask:

```text
Can this class depend on an abstraction or injected dependency
instead of being tightly coupled to a concrete implementation?
```

# Design Thinking Checklist

Before writing code, I should ask:

```text
1. What are the entities?

2. What classes should represent those entities?

3. What data belongs to each class?

4. What behavior belongs to each class?

5. Which class owns each piece of state?

6. Which objects need to interact?

7. Is the relationship IS-A or HAS-A?

8. Should I use inheritance or composition?

9. Where should validation happen?

10. Which state should be protected?

11. Is polymorphism useful here?

12. Are any classes doing too much?

13. Are any classes too tightly coupled?

14. Can I keep the design simpler?
```

# Implementation Workflow

For every problem, follow this process.

## Step 1 — Understand the Requirement

Read the problem carefully.

Do not immediately start writing classes.

First identify:

```text
Entities
Relationships
State
Behavior
Rules
```

## Step 2 — Identify Classes

Write down possible classes.

Example:

```text
Customer
Order
Product
Payment
```

Then ask whether every class is actually necessary.

Do not create classes just because OOP allows it.

## Step 3 — Identify Responsibilities

For every class, write:

```text
Class
    ↓
What does it know?
    ↓
What does it do?
```

Example:

```text
BankAccount

Knows:
- account number
- balance

Does:
- deposit
- withdraw
```

## Step 4 — Identify Relationships

Determine whether classes have:

```text
IS-A
HAS-A
USES
INTERACTS-WITH
```

relationships.

## Step 5 — Implement the Core Behavior

Start with the most important behavior.

Do not try to implement everything simultaneously.

## Step 6 — Add Validation

Check the constraints.

Examples:

```text
Invalid amount
Insufficient balance
Invalid status transition
Duplicate operation
Missing object
```

## Step 7 — Test

Run the provided test cases.

Then create your own additional test cases.

## Step 8 — Refactor

After the code works, ask:

```text
Can I make this simpler?

Is any class doing too much?

Is there unnecessary inheritance?

Is there duplicated logic?

Is there tight coupling?

Can polymorphism improve this?

Can composition improve this?
```

# Practical Problem Levels

## Level 1 — Medium

Focus on:

- Classes
- Objects
- `__init__`
- Instance attributes
- Instance methods
- Encapsulation
- Basic relationships

Possible problems:

```text
Bank Account System
Library Management System
Student Management System
```

## Level 2 — Medium+

Focus on:

- Inheritance
- Method overriding
- Polymorphism
- Composition
- Validation
- Class responsibilities

Possible problems:

```text
Payment System
Notification System
Vehicle Rental System
```

## Level 3 — Advanced

Focus on:

- Multiple interacting objects
- Composition
- Polymorphism
- Abstraction
- Dependency Injection
- SOLID principles
- Better separation of responsibilities

Possible problems:

```text
Food Ordering System
Parking System
Order Management System
```

## Level 4 — Interview Level

Focus on:

- Requirements analysis
- Class design
- Object relationships
- Extensibility
- Edge cases
- Clean Python implementation
- Refactoring
- Explaining design decisions

The goal is not to create huge applications.

The goal is to solve a reasonably sized problem with a clean object-oriented design.

# What I Should NOT Do

## Don't Overengineer

Do not create:

```text
20 classes
10 abstract classes
5 inheritance levels
```

for a problem that needs only a few classes.

Simple and correct is better.

## Don't Force Every OOP Concept

Not every problem needs:

```text
Inheritance
Polymorphism
ABC
SOLID
Properties
Class methods
Static methods
```

Use a concept only when the problem actually benefits from it.

## Don't Use Inheritance Just for Code Reuse

This is a common mistake.

Bad reasoning:

```text
Both classes have the same method
        ↓
Therefore inheritance
```

Instead ask:

```text
Is there a genuine IS-A relationship?
```

## Don't Make Everything Private

Python does not require every attribute to be hidden.

Use encapsulation where it protects state or maintains an invariant.

## Don't Create Getters and Setters Automatically

Don't write:

```python
get_name()
set_name()
```

for every attribute without a reason.

Use direct attributes when appropriate and properties/methods when behavior or validation requires them.

# Code Quality Checklist

Before considering a problem complete:

```text
[ ] Classes have clear responsibilities
[ ] Objects are initialized correctly
[ ] State is valid
[ ] Important state is properly encapsulated
[ ] Methods have meaningful names
[ ] No unnecessary inheritance
[ ] Relationships make sense
[ ] No unnecessary duplication
[ ] Validation is handled
[ ] Edge cases are tested
[ ] Code is readable
[ ] Classes are not unnecessarily large
[ ] Dependencies are not unnecessarily hard-coded
```

# Interview Questions

After completing the practical problems, I should be able to answer questions such as:

### OOP Fundamentals

1. What is OOP?
2. What is the difference between a class and an object?
3. What is `self`?
4. Why do we use `__init__`?
5. What is the difference between instance and class variables?

### Encapsulation

6. What is encapsulation?
7. What is the difference between `_x` and `__x`?
8. What is name mangling?
9. When would you use `@property`?

### Inheritance

10. What is inheritance?
11. What is method overriding?
12. What is `super()`?
13. How does MRO work?
14. What is multiple inheritance?
15. What is the diamond problem?

### Polymorphism

16. What is polymorphism?
17. What is duck typing?
18. How does method overriding provide polymorphism?
19. What is operator overloading?

### Abstraction

20. What is abstraction?
21. What is an abstract class?
22. What is `@abstractmethod`?
23. Can an abstract class have implemented methods?

### Design

24. What is the difference between inheritance and composition?
25. What is the difference between association and aggregation?
26. What does "favor composition over inheritance" mean?
27. Explain the SOLID principles.
28. What is dependency injection?
29. How does composition help reduce coupling?

### Python Object Model

30. What are dunder methods?
31. What is `__str__` vs `__repr__`?
32. How does `__eq__` relate to `__hash__`?
33. How does Python implement iteration?
34. What is a context manager?
35. What is `__slots__`?
36. What are descriptors?

# Self-Assessment

After completing the practical problems, rate yourself based on actual implementation ability.

## Beginner OOP

I can:

```text
[ ] Create classes and objects
[ ] Initialize objects correctly
[ ] Use instance attributes
[ ] Write instance methods
[ ] Understand class attributes
```

## Intermediate OOP

I can:

```text
[ ] Apply encapsulation
[ ] Use properties when appropriate
[ ] Implement inheritance
[ ] Override methods
[ ] Use super()
[ ] Apply polymorphism
[ ] Use abstraction
[ ] Choose composition appropriately
```

## Strong OOP

I can:

```text
[ ] Identify class responsibilities
[ ] Design object relationships
[ ] Avoid unnecessary inheritance
[ ] Apply SOLID principles when useful
[ ] Reduce unnecessary coupling
[ ] Use dependency injection
[ ] Handle edge cases
[ ] Refactor an initial design
```

## Interview Ready

I can:

```text
[ ] Understand an unfamiliar OOP requirement
[ ] Identify classes without being told
[ ] Decide relationships between classes
[ ] Explain my design decisions
[ ] Implement the solution without copying
[ ] Handle edge cases
[ ] Refactor my own code
[ ] Explain trade-offs during an interview
```

# Final OOP Mental Model

When I receive a new software requirement:

```text
Requirement
     ↓
Identify Entities
     ↓
Identify Classes
     ↓
Identify State
     ↓
Identify Behavior
     ↓
Identify Relationships
     ↓
Choose Composition / Inheritance
     ↓
Apply Encapsulation
     ↓
Use Polymorphism Where Useful
     ↓
Apply SOLID Where Appropriate
     ↓
Implement
     ↓
Test
     ↓
Refactor
```

# Final Goal

The purpose of this lecture is not to memorize more OOP terminology.

The goal is:

```text
Read Requirement
      ↓
Think in Objects
      ↓
Design Classes
      ↓
Define Responsibilities
      ↓
Implement in Python
      ↓
Test
      ↓
Refactor
      ↓
Explain the Design
```

If I can consistently do this without needing a solution first, then I have moved beyond **knowing OOP concepts** and can actually **apply Python OOP in code**.

## OOP Completion Checklist

```text
[ ] Lecture 1 — OOP Fundamentals
[ ] Lecture 2 — __init__ & Object Initialization
[ ] Lecture 3 — Instance/Class Data & Methods
[ ] Lecture 4 — Encapsulation
[ ] Lecture 5 — Inheritance
[ ] Lecture 6 — Polymorphism
[ ] Lecture 7 — Abstraction
[ ] Lecture 8 — SOLID Principles
[ ] Lecture 9 — Composition / Association / Aggregation
[ ] Lecture 10 — Object Introspection
[ ] Lecture 11 — Special / Dunder Methods
[ ] Lecture 12 — OOP Interview + Practical Practice

OOP Complete → Practical Python Development
```