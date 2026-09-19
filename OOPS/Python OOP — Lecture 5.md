# OOP — Lecture 5
# Inheritance

> **Goal:** Understand inheritance, parent/child classes, method overriding, `super()`, multiple inheritance, MRO, and inheritance vs composition.
>
> This lecture is important for **Python interviews, backend development, DSA implementations, and especially LLD**.

## 1. What Is Inheritance?

**Inheritance** allows one class to reuse and extend the attributes and methods of another class.

Example:

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")
```

Now:

```python
dog = Dog()

dog.eat()
dog.bark()
```

Output:

```text
Eating
Barking
```

`Dog` inherited `eat()` from `Animal`.

Mental model:

```text
Animal
  ↓
Parent / Base Class
  ↓
Dog
  ↓
Child / Derived Class
```

---

# 2. Why Do We Need Inheritance?

Inheritance can provide:

- Code reuse
- Shared behavior
- Common interfaces
- Extension of existing classes
- Polymorphic designs
- A natural way to model certain `is-a` relationships

Example:

```text
Vehicle
   │
   ├── Car
   ├── Bike
   └── Truck
```

All vehicles may have common behavior:

```text
start()
stop()
```

while individual vehicle types can have their own behavior.

---

# 3. Parent and Child Classes

Terminology:

```text
Parent Class
Base Class
Super Class
```

These generally refer to the class being inherited from.

```text
Child Class
Derived Class
Subclass
```

These refer to the class that inherits.

Example:

```python
class Animal:
    pass


class Dog(Animal):
    pass
```

Here:

```text
Animal → Parent/Base class
Dog    → Child/Derived class
```

---

# 4. Basic Syntax

Inheritance syntax:

```python
class Child(Parent):
    pass
```

Example:

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    pass
```

Now:

```python
dog = Dog()

dog.eat()
```

Output:

```text
Eating
```

---

# 5. What Does the Child Inherit?

A child class can use accessible attributes and methods from its parent class.

Example:

```python
class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):
    def bark(self):
        print(self.name, "is barking")
```

Usage:

```python
dog = Dog("Tommy")

dog.eat()
dog.bark()
```

Output:

```text
Tommy is eating
Tommy is barking
```

The child class can use:

```python
self.name
```

and:

```python
eat()
```

from the parent.

---

# 6. Inheritance Does Not Copy the Code Literally

A common beginner misunderstanding is:

> "Python copies all parent code into the child."

That's not the best mental model.

Instead, think:

```text
Dog
 ↓
Can use/inherit behavior from Animal
```

Python's attribute lookup mechanism determines where methods and attributes are found.

This becomes especially important when we study:

```text
Method Overriding
MRO
Multiple Inheritance
```

---

# 7. Simple Real-World Example

Consider:

```text
Vehicle
   │
   ├── Car
   └── Bike
```

A vehicle can:

```text
start()
stop()
```

A car may additionally:

```text
open_trunk()
```

A bike may additionally:

```text
kick_start()
```

This can be represented as:

```python
class Vehicle:

    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")


class Car(Vehicle):

    def open_trunk(self):
        print("Trunk opened")


class Bike(Vehicle):

    def kick_start(self):
        print("Bike kick started")
```

---

# 8. `is-a` Relationship

Inheritance generally represents an **is-a relationship**.

Example:

```text
Dog is an Animal
Car is a Vehicle
Manager is an Employee
```

Therefore:

```python
class Dog(Animal):
    pass
```

makes sense.

But:

```text
Car is an Engine
```

does not make sense.

A car **has an engine**.

That is a different relationship.

---

# 9. `is-a` vs `has-a`

This distinction is extremely important for LLD.

### Is-a

Usually represented using inheritance.

```text
Car is a Vehicle
```

```python
class Car(Vehicle):
    pass
```

### Has-a

Usually represented using composition.

```text
Car has an Engine
```

```python
class Car:
    def __init__(self):
        self.engine = Engine()
```

Mental model:

```text
is-a
  ↓
Inheritance

has-a
  ↓
Composition
```

We will return to this in detail later.

---

# 10. Method Overriding

A child class can provide its own implementation of a method inherited from the parent.

This is called **method overriding**.

Example:

```python
class Animal:

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):

    def speak(self):
        print("Dog barks")
```

Now:

```python
dog = Dog()

dog.speak()
```

Output:

```text
Dog barks
```

The child's `speak()` overrides the parent's `speak()`.

---

# 11. Why Override Methods?

Because the child may need behavior that is different from the generic parent behavior.

Example:

```text
Animal
  ↓
speak()

Dog
  ↓
bark

Cat
  ↓
meow
```

The parent defines a common operation:

```text
speak()
```

Each child can provide its own implementation.

This becomes extremely important when we study **polymorphism**.

---

# 12. Example: Payment System

This is a common LLD-style example.

```python
class Payment:

    def pay(self, amount):
        print("Processing payment")


class CardPayment(Payment):

    def pay(self, amount):
        print("Processing card payment")


class UPIPayment(Payment):

    def pay(self, amount):
        print("Processing UPI payment")
```

Each child overrides:

```python
pay()
```

with its own behavior.

This design will later connect directly to polymorphism.

---

# 13. Method Overriding Is Not Method Overloading

These are different concepts.

### Overriding

Child class changes the implementation of a parent method.

```python
class Parent:
    def show(self):
        print("Parent")


class Child(Parent):
    def show(self):
        print("Child")
```

### Overloading

Same method name with different parameter signatures.

Python does not support traditional compile-time method overloading like Java/C++.

For example, this does **not** create two overloaded methods:

```python
class A:

    def add(self, a):
        return a

    def add(self, a, b):
        return a + b
```

The second definition replaces the first.

We can simulate flexible arguments using:

```python
*args
**kwargs
```

or default arguments, but that's separate from inheritance.

---

# 14. Calling the Parent Method

Suppose the child overrides a method:

```python
class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):

    def speak(self):
        print("Dog sound")
```

Sometimes the child wants to:

1. Execute the parent's behavior
2. Add its own behavior

This is where:

```python
super()
```

becomes useful.

---

# 15. What Is `super()`?

`super()` gives access to the next class in the method resolution order, allowing a child class to call inherited behavior.

Example:

```python
class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):

    def speak(self):
        super().speak()
        print("Dog sound")
```

Now:

```python
dog = Dog()

dog.speak()
```

Output:

```text
Animal sound
Dog sound
```

---

# 16. Why Use `super()`?

Without `super()`:

```python
class Dog(Animal):

    def speak(self):
        print("Dog sound")
```

The parent's implementation is replaced for this method.

With:

```python
super().speak()
```

the child can extend the parent's behavior.

Mental model:

```text
Parent behavior
      ↓
super()
      ↓
Child behavior
```

---

# 17. `super()` in `__init__()`

This is one of the most important practical uses.

Example:

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no
```

Create:

```python
student = Student("Nitin", 101)
```

Now:

```python
student.name
student.roll_no
```

work.

The parent initializes:

```text
name
```

The child initializes:

```text
roll_no
```

---

# 18. Why Use `super().__init__()`?

Suppose:

```python
class Person:

    def __init__(self, name):
        self.name = name
```

and:

```python
class Student(Person):

    def __init__(self, name, roll_no):
        self.roll_no = roll_no
```

Now:

```python
student = Student("Nitin", 101)
```

What happened to `name`?

The parent `__init__()` was not called automatically.

Therefore:

```python
student.name
```

doesn't exist.

If the child needs the parent initialization, call:

```python
super().__init__(name)
```

---

# 19. Complete Constructor Example

```python
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):

    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no
```

Now:

```python
student = Student("Nitin", 22, 101)
```

State:

```text
student
   │
   ├── name
   ├── age
   └── roll_no
```

Parent handles:

```text
name
age
```

Child handles:

```text
roll_no
```

---

# 20. `super()` Mental Model

Don't think:

```text
super() = parent object
```

A better mental model is:

```text
super()
   ↓
Access the next class in the MRO
   ↓
Call inherited behavior
```

For simple single inheritance:

```text
Child
  ↓
super()
  ↓
Parent
```

But with multiple inheritance, this distinction becomes very important.

---

# 21. `super()` Is Not Always "Direct Parent"

This is an important interview point.

In simple inheritance:

```python
class Dog(Animal):
```

`super()` commonly reaches `Animal`.

But in multiple inheritance, `super()` follows the **MRO**, not simply "the parent written on the left."

Example:

```python
class A:
    pass


class B(A):
    pass
```

For:

```python
class B(A):
```

`super()` from `B` follows the MRO after `B`.

Later we will see why this matters in multiple inheritance.

---

# 22. Inheritance With Additional Methods

A child can:

- inherit methods
- override methods
- add new methods

Example:

```python
class Animal:

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")


class Dog(Animal):

    def bark(self):
        print("Barking")

    def sleep(self):
        print("Dog sleeping")
```

Dog gets:

```text
eat()
```

from parent.

Dog defines:

```text
bark()
```

itself.

Dog overrides:

```text
sleep()
```

---

# 23. Three Important Possibilities

When a child inherits from a parent:

```text
1. Use parent method as-is
2. Override parent method
3. Add a completely new method
```

Example:

```python
class Parent:

    def a(self):
        print("A")

    def b(self):
        print("B")


class Child(Parent):

    def b(self):
        print("Child B")

    def c(self):
        print("C")
```

Child can:

```text
a() → inherited
b() → overridden
c() → new
```

---

# 24. Single Inheritance

When one child inherits from one parent:

```text
Parent
   ↓
Child
```

Example:

```python
class Animal:
    pass


class Dog(Animal):
    pass
```

This is called **single inheritance**.

---

# 25. Multilevel Inheritance

Inheritance can form multiple levels.

Example:

```text
Animal
   ↓
Mammal
   ↓
Dog
```

Python:

```python
class Animal:
    def eat(self):
        print("Eating")


class Mammal(Animal):
    def walk(self):
        print("Walking")


class Dog(Mammal):
    def bark(self):
        print("Barking")
```

Now:

```python
dog = Dog()

dog.eat()
dog.walk()
dog.bark()
```

Dog can access behavior from the inheritance chain.

---

# 26. Multilevel Inheritance Mental Model

```text
Animal
   │
   │ inherits
   ↓
Mammal
   │
   │ inherits
   ↓
Dog
```

Dog can access inherited behavior through the hierarchy.

However, very deep inheritance chains can make systems difficult to understand.

In LLD, prefer simple and meaningful hierarchies.

---

# 27. Hierarchical Inheritance

Multiple child classes inherit from the same parent.

```text
        Animal
        /    \
       /      \
     Dog      Cat
```

Example:

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")


class Cat(Animal):

    def meow(self):
        print("Meowing")
```

Both:

```text
Dog
Cat
```

inherit:

```text
eat()
```

from:

```text
Animal
```

---

# 28. Multiple Inheritance

Python allows a class to inherit from multiple classes.

Example:

```python
class A:
    def show_a(self):
        print("A")


class B:
    def show_b(self):
        print("B")


class C(A, B):
    pass
```

Now:

```python
c = C()

c.show_a()
c.show_b()
```

Both methods are available.

Conceptually:

```text
A       B
 \     /
   \ /
    C
```

---

# 29. Why Can Multiple Inheritance Become Complicated?

Suppose both parent classes define the same method:

```python
class A:

    def show(self):
        print("A")


class B:

    def show(self):
        print("B")


class C(A, B):
    pass
```

Now:

```python
c = C()

c.show()
```

Which method should Python call?

```text
A.show()
```

or:

```text
B.show()
```

Python solves this using:

```text
MRO
Method Resolution Order
```

---

# 30. Method Resolution Order (MRO)

**MRO** defines the order in which Python searches classes for an attribute or method.

You can inspect it using:

```python
ClassName.mro()
```

Example:

```python
class A:
    pass


class B(A):
    pass


print(B.mro())
```

Conceptually:

```text
B
A
object
```

The final `object` is Python's root base class for ordinary classes.

---

# 31. MRO Example

```python
class A:

    def show(self):
        print("A")


class B:

    def show(self):
        print("B")


class C(A, B):
    pass
```

Check:

```python
print(C.mro())
```

Conceptually:

```text
C
A
B
object
```

Therefore:

```python
c = C()
c.show()
```

finds:

```text
C → no show()
A → show() found
```

So output:

```text
A
```

---

# 32. `__mro__`

You can also inspect MRO using:

```python
C.__mro__
```

Example:

```python
print(C.__mro__)
```

Both:

```python
C.mro()
```

and:

```python
C.__mro__
```

help you understand the lookup order.

For interviews, remember:

```text
MRO = Method Resolution Order
```

---

# 33. Diamond Problem

Consider:

```text
       A
      / \
     B   C
      \ /
       D
```

This is called the **diamond inheritance pattern**.

Example:

```python
class A:
    def show(self):
        print("A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass
```

Now:

```python
d = D()
d.show()
```

Python needs to determine which path to follow.

MRO solves this.

---

# 34. Diamond MRO

For:

```python
class D(B, C):
```

Python calculates an MRO similar to:

```text
D
B
C
A
object
```

Therefore method lookup follows that order.

The important thing is:

> Python's MRO prevents the same ancestor from being processed incorrectly multiple times.

You do not need to memorize the full algorithm for normal interviews unless specifically asked.

Understand the concept and how to inspect MRO.

---

# 35. C3 Linearization

Python uses **C3 linearization** to calculate MRO.

For most interviews:

```text
MRO
↓
Python's method lookup ordering
↓
Uses C3 linearization
```

Knowing the name is useful.

You usually don't need to manually calculate complex C3 linearization unless the interviewer specifically asks.

---

# 36. `isinstance()`

`isinstance()` checks whether an object is an instance of a class or one of its subclasses.

Example:

```python
class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
```

Output:

```text
True
True
```

Why is the second one `True`?

Because:

```text
Dog is an Animal
```

through inheritance.

---

# 37. `isinstance()` With Multiple Classes

You can also provide a tuple of classes:

```python
isinstance(dog, (Dog, Animal))
```

Example:

```python
print(isinstance(dog, (Dog, Animal)))
```

Output:

```text
True
```

Python checks whether the object belongs to any of the specified types.

---

# 38. `issubclass()`

`issubclass()` checks the relationship between classes.

Example:

```python
class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog, Animal))
```

Output:

```text
True
```

Because:

```text
Dog inherits from Animal
```

---

# 39. `isinstance()` vs `issubclass()`

This is a common interview question.

### `isinstance()`

Checks:

```text
object → class
```

Example:

```python
isinstance(dog, Animal)
```

### `issubclass()`

Checks:

```text
class → class
```

Example:

```python
issubclass(Dog, Animal)
```

Mental model:

```text
isinstance
    ↓
Is this object an instance of this class?


issubclass
    ↓
Is this class derived from this class?
```

---

# 40. Inheritance and Constructors

Consider:

```python
class Parent:

    def __init__(self):
        print("Parent constructor")


class Child(Parent):
    pass
```

Now:

```python
child = Child()
```

Output:

```text
Parent constructor
```

The child has no `__init__()`, so the inherited constructor can be used.

---

# 41. What If Child Defines `__init__()`?

```python
class Parent:

    def __init__(self):
        print("Parent constructor")


class Child(Parent):

    def __init__(self):
        print("Child constructor")
```

Now:

```python
child = Child()
```

Output:

```text
Child constructor
```

The child's `__init__()` is used.

If the parent initialization is also required:

```python
class Child(Parent):

    def __init__(self):
        super().__init__()
        print("Child constructor")
```

Output:

```text
Parent constructor
Child constructor
```

---

# 42. Constructor Design With Inheritance

Example:

```python
class Employee:

    def __init__(self, name):
        self.name = name


class Manager(Employee):

    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size
```

Now:

```python
manager = Manager("Nitin", 5)
```

State:

```text
manager
   ├── name
   └── team_size
```

Parent handles common state.

Child handles specialized state.

---

# 43. Inheritance and Access to Parent Attributes

Example:

```python
class Parent:

    def __init__(self):
        self.name = "Parent"


class Child(Parent):
    def show(self):
        print(self.name)
```

Usage:

```python
child = Child()

child.show()
```

Output:

```text
Parent
```

The child can use the inherited instance state.

---

# 44. Inheritance and `_protected` Convention

Example:

```python
class Parent:

    def __init__(self):
        self._value = 10


class Child(Parent):

    def show(self):
        print(self._value)
```

This works.

The underscore is a convention, not a strict access restriction.

---

# 45. Inheritance and `__private` Attributes

Double underscore behaves differently because of name mangling.

Example:

```python
class Parent:

    def __init__(self):
        self.__value = 10
```

The attribute becomes approximately:

```text
_Parent__value
```

A child class using:

```python
self.__value
```

would refer to:

```text
_Child__value
```

not:

```text
_Parent__value
```

This is one reason name mangling can help prevent accidental name collisions between parent and child classes.

---

# 46. Inheritance vs Composition ⭐⭐⭐

This is one of the most important LLD concepts.

### Inheritance

Represents:

```text
is-a
```

Example:

```text
Dog is an Animal
```

### Composition

Represents:

```text
has-a
```

Example:

```text
Car has an Engine
```

Inheritance:

```python
class Dog(Animal):
    pass
```

Composition:

```python
class Car:
    def __init__(self):
        self.engine = Engine()
```

---

# 47. Why Composition Is Often Preferred

Inheritance creates a strong relationship between parent and child.

If the parent changes significantly, children may also be affected.

Composition often provides more flexibility because objects can be combined rather than forming a rigid hierarchy.

Example:

```text
Car
 └── Engine
```

The `Car` can use an `Engine` object without becoming a subtype of `Engine`.

---

# 48. Bad Inheritance Example

Suppose:

```text
Car
 ↓
ElectricCar
 ↓
TeslaModelX
 ↓
SpecialTeslaModelX
```

A very deep hierarchy can become difficult to maintain.

Problems can include:

- Hard-to-understand relationships
- Tight coupling
- Difficult changes
- Complex overriding
- MRO complications
- Fragile designs

Inheritance should represent a meaningful domain relationship, not simply:

> "I want to reuse this code."

---

# 49. Better Question Before Using Inheritance

Ask:

> **Is the child genuinely a specialized form of the parent?**

If:

```text
Dog is an Animal
```

Yes.

If:

```text
Car is an Engine
```

No.

Instead:

```text
Car has an Engine
```

Use composition.

---

# 50. LLD Example: Payment

Inheritance can make sense:

```text
Payment
   │
   ├── CardPayment
   ├── UPIPayment
   └── CashPayment
```

because each represents a type of payment mechanism.

Example:

```python
class Payment:

    def pay(self, amount):
        raise NotImplementedError


class CardPayment(Payment):

    def pay(self, amount):
        print("Card payment")


class UPIPayment(Payment):

    def pay(self, amount):
        print("UPI payment")
```

Later, polymorphism can allow the system to work with:

```text
Payment
```

without caring about the exact subtype.

---

# 51. LLD Example: Notification

Another common hierarchy:

```text
Notification
      │
      ├── EmailNotification
      ├── SMSNotification
      └── PushNotification
```

Each notification type may implement:

```python
send()
```

Example:

```python
class Notification:

    def send(self, message):
        raise NotImplementedError


class EmailNotification(Notification):

    def send(self, message):
        print("Sending email")


class SMSNotification(Notification):

    def send(self, message):
        print("Sending SMS")
```

This will become especially useful in the next lecture on **Polymorphism**.

---

# 52. DSA Connection

Inheritance is less central to solving typical DSA problems than arrays, trees, graphs, recursion, etc.

But it is useful when implementing reusable data structures or creating specialized structures.

Example:

```python
class Stack:
    def push(self, value):
        pass


class MinStack(Stack):
    def get_min(self):
        pass
```

`MinStack` can reuse the stack behavior while adding specialized behavior.

However, don't force inheritance into DSA implementations where it doesn't naturally help.

---

# 53. Backend Connection

Inheritance can be useful for shared behavior.

Example:

```text
BaseRepository
      │
      ├── UserRepository
      ├── OrderRepository
      └── ProductRepository
```

Or:

```text
BaseService
      │
      ├── UserService
      └── OrderService
```

But in production backend systems, composition and dependency injection are also very important.

Don't assume:

```text
inheritance = always better
```

---

# 54. Common Mistake #1

Using inheritance only for code reuse.

Bad reasoning:

```text
Parent has a useful method
        ↓
I'll inherit from Parent
```

First ask:

```text
Is this actually an "is-a" relationship?
```

If not, composition may be better.

---

# 55. Common Mistake #2

Forgetting `super().__init__()`

Example:

```python
class Parent:

    def __init__(self, name):
        self.name = name


class Child(Parent):

    def __init__(self, name, age):
        self.age = age
```

The parent initialization is skipped.

If required:

```python
class Child(Parent):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
```

---

# 56. Common Mistake #3

Calling the Parent Class Directly Instead of Using `super()`

You might see:

```python
Parent.__init__(self, name)
```

This can work in some cases.

But:

```python
super().__init__(name)
```

is generally preferred in inheritance hierarchies because it works with Python's MRO and cooperative multiple inheritance.

---

# 57. Common Mistake #4

Creating Very Deep Inheritance Trees

Avoid unnecessarily complicated structures like:

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
 ↓
F
```

Deep inheritance can make behavior harder to reason about.

Prefer simple hierarchies or composition when appropriate.

---

# 58. Common Mistake #5

Misunderstanding `super()`

Don't think:

```text
super() = always direct parent
```

Better:

```text
super()
   ↓
next class in MRO
```

This distinction becomes important with multiple inheritance.

---

# 59. Interview Question: What Is Inheritance?

### Answer

Inheritance is an OOP mechanism where a child class derives from a parent class and can reuse, extend, or override its attributes and methods.

Example:

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    pass
```

`Dog` inherits `eat()` from `Animal`.

---

# 60. Interview Question: What Is Method Overriding?

Method overriding occurs when a child class provides its own implementation of a method inherited from the parent.

Example:

```python
class Animal:

    def speak(self):
        print("Animal")


class Dog(Animal):

    def speak(self):
        print("Dog")
```

The `Dog` implementation overrides the `Animal` implementation.

---

# 61. Interview Question: What Is `super()`?

`super()` provides access to the next class in the MRO.

It is commonly used to:

- call parent initialization
- extend parent behavior
- support cooperative multiple inheritance

Example:

```python
class Child(Parent):

    def __init__(self):
        super().__init__()
```

---

# 62. Interview Question: What Is MRO?

MRO stands for:

```text
Method Resolution Order
```

It defines the order Python follows when searching for a method or attribute in an inheritance hierarchy.

You can inspect it using:

```python
ClassName.mro()
```

or:

```python
ClassName.__mro__
```

---

# 63. Interview Question: What Is the Diamond Problem?

The diamond problem occurs when a class inherits from two classes that both derive from the same parent.

Example:

```text
       A
      / \
     B   C
      \ /
       D
```

Python uses MRO to determine a consistent method lookup order.

---

# 64. Interview Question: Difference Between `isinstance()` and `issubclass()`

### `isinstance()`

Checks an object:

```python
isinstance(obj, Class)
```

### `issubclass()`

Checks classes:

```python
issubclass(Child, Parent)
```

Mental model:

```text
isinstance
    ↓
object → class


issubclass
    ↓
class → class
```

---

# 65. Interview Question: Inheritance vs Composition

### Inheritance

```text
is-a
```

Example:

```text
Dog is an Animal
```

### Composition

```text
has-a
```

Example:

```text
Car has an Engine
```

Use inheritance when there is a genuine subtype relationship.

Use composition when one object contains or uses another object.

---

# 66. Complete Example

Let's combine the major concepts.

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print("Employee is working")


class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        super().work()
        print("Manager is managing the team")

    def conduct_meeting(self):
        print("Conducting meeting")
```

Usage:

```python
manager = Manager("Nitin", 80000, 5)

print(manager.name)
print(manager.salary)
print(manager.team_size)

manager.work()
manager.conduct_meeting()
```

Output:

```text
Nitin
80000
5
Employee is working
Manager is managing the team
Conducting meeting
```

Here:

```text
Employee
   ↓
Parent class

Manager
   ↓
Child class

name, salary
   ↓
Inherited state

team_size
   ↓
Child-specific state

work()
   ↓
Overridden method

super().work()
   ↓
Parent behavior

conduct_meeting()
   ↓
Child-specific behavior
```

---

# 67. Inheritance Mental Model

```text
                Parent Class
                     │
          ┌──────────┴──────────┐
          │                     │
     Common State          Common Behavior
          │                     │
          └──────────┬──────────┘
                     ↓
                Child Class
                     │
          ┌──────────┴──────────┐
          │                     │
   Specialized State      Specialized Behavior
                               │
                               ↓
                         Method Override
```

---

# 68. The Important LLD Rule

Before using inheritance, ask:

```text
Is it genuinely an "is-a" relationship?
        │
       Yes
        ↓
Inheritance may make sense
        │
       No
        ↓
Consider Composition
```

Remember:

```text
Dog
 ↓
is-a
 ↓
Animal

Car
 ↓
has-a
 ↓
Engine
```

---

# 69. Quick Revision

### Inheritance

```python
class Child(Parent):
    pass
```

Child derives from parent.

### Method Overriding

```python
class Child(Parent):

    def method(self):
        ...
```

Child provides its own implementation.

### `super()`

```python
super().method()
```

Accesses the next implementation according to MRO.

### MRO

```python
ClassName.mro()
```

Shows method resolution order.

### `isinstance()`

```python
isinstance(obj, Class)
```

Checks object/class relationship.

### `issubclass()`

```python
issubclass(Child, Parent)
```

Checks class inheritance relationship.

### Inheritance

```text
is-a
```

### Composition

```text
has-a
```

---

# 70. Must-Know Interview Checklist

Before moving to the next lecture, you should be able to explain:

- What is inheritance?
- Why do we use inheritance?
- What is a parent/base class?
- What is a child/derived class?
- What is an `is-a` relationship?
- What is method overriding?
- Difference between overriding and overloading?
- What is `super()`?
- Why use `super().__init__()`?
- Is `super()` always the direct parent?
- What is single inheritance?
- What is multilevel inheritance?
- What is hierarchical inheritance?
- What is multiple inheritance?
- What is MRO?
- How can you inspect MRO?
- What is the diamond problem?
- What is `isinstance()`?
- What is `issubclass()`?
- Difference between inheritance and composition?
- Why can excessive inheritance become problematic?
- Why is composition often preferred in LLD?

# OOP Lecture 5 Complete