# Python OOP — Lecture 11: Special / Dunder Methods

My personal notes for understanding **Special Methods (Dunder Methods) in Python**, with practical examples, operator overloading, Python's data model, common mistakes, and interview preparation.

## 1. What Are Dunder Methods?

**Dunder methods** are special methods in Python whose names start and end with double underscores.

Examples:

```python
__init__
__str__
__repr__
__len__
__eq__
__add__
```

"Dunder" means:

```text
Double UNDERscore
```

For example:

```python
__init__
```

is commonly called:

```text
dunder init
```

Dunder methods allow your custom objects to interact naturally with Python's built-in syntax and operations.

For example:

```python
numbers = [1, 2, 3]

print(len(numbers))
```

Python uses the object's special length behavior.

Similarly:

```python
a + b
```

can use:

```python
__add__
```

### Mental Model

```text
Normal Python Syntax
        ↓
Special Method
        ↓
Object Behavior
```

Examples:

```text
len(obj)
   ↓
obj.__len__()

obj + other
   ↓
obj.__add__(other)

obj == other
   ↓
obj.__eq__(other)

str(obj)
   ↓
obj.__str__()
```

## 2. Why Dunder Methods Matter

Dunder methods allow custom classes to behave like native Python objects.

Without `__str__()`:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance


account = BankAccount(1000)

print(account)
```

You may get output similar to:

```text
<__main__.BankAccount object at 0x...>
```

With `__str__()`:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return f"BankAccount(balance={self.balance})"


account = BankAccount(1000)

print(account)
```

Output:

```text
BankAccount(balance=1000)
```

You can also make objects support:

```python
len(obj)
obj[index]
obj + other
obj == other
for item in obj
obj()
```

This makes your classes feel natural to Python users.

## 3. Python Data Model

Dunder methods are part of Python's **data model**.

The Python data model defines how objects interact with Python syntax and built-in operations.

For example:

```python
len(obj)
```

uses the object's length protocol.

Similarly:

```python
obj + other
```

can use:

```python
obj.__add__(other)
```

The important idea is:

```text
Python Syntax
     ↓
Protocol / Special Method
     ↓
Object Behavior
```

You don't normally call dunder methods directly.

Prefer:

```python
len(obj)
```

instead of:

```python
obj.__len__()
```

Prefer:

```python
obj + other
```

instead of:

```python
obj.__add__(other)
```

Dunder methods are generally implemented by the class so that normal Python syntax can use them.

## 4. `__init__`

You have already studied `__init__`.

It initializes an object after it is created.

```python
class User:

    def __init__(self, name):
        self.name = name


user = User("Nitin")

print(user.name)
```

Here:

```text
User("Nitin")
      ↓
Object creation
      ↓
__init__()
      ↓
Object initialized
```

Important:

`__init__()` is an initializer, not the method that actually creates the object.

Object creation is associated with `__new__()`.

For normal Python classes, you usually only need to implement `__init__()`.

## 5. `__str__`

`__str__()` defines the user-friendly string representation of an object.

Example:

```python
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"User(name={self.name}, age={self.age})"


user = User("Nitin", 25)

print(user)
```

Output:

```text
User(name=Nitin, age=25)
```

Python calls:

```python
print(user)
```

which uses the object's string representation.

You can also explicitly call:

```python
str(user)
```

## 6. Rules for `__str__`

`__str__()` must return a string.

Correct:

```python
def __str__(self):
    return "Hello"
```

Incorrect:

```python
def __str__(self):
    return 100
```

This causes a `TypeError`.

### Good `__str__`

Use `__str__()` for:

```text
Human-readable
User-friendly
Readable
```

Example:

```python
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ₹{self.price}"
```

## 7. `__repr__`

`__repr__()` provides the official/developer-oriented representation of an object.

Example:

```python
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age!r})"


user = User("Nitin", 25)

print(repr(user))
```

Output:

```text
User(name='Nitin', age=25)
```

### `__str__` vs `__repr__`

Think:

```text
__str__
   ↓
Human-friendly

__repr__
   ↓
Developer/debugging-friendly
```

Example:

```python
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ₹{self.price}"

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price!r})"
```

Then:

```python
product = Product("Laptop", 50000)

print(product)
print(repr(product))
```

Output:

```text
Laptop - ₹50000
Product(name='Laptop', price=50000)
```

## 8. Why `repr()` Is Important

`repr()` is especially useful for:

- Debugging
- Logs
- Development
- Inspecting collections
- Understanding object state

For example:

```python
users = [
    User("Nitin", 25),
    User("Rahul", 30)
]

print(users)
```

Python uses representations of the objects inside the list.

Therefore implementing `__repr__()` makes collections of custom objects much easier to debug.

## 9. `__str__` Fallback to `__repr__`

If you don't define `__str__()`, Python can use `__repr__()` as a fallback for string conversion.

Example:

```python
class User:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"User(name={self.name!r})"


user = User("Nitin")

print(user)
```

Output:

```text
User(name='Nitin')
```

This is one reason implementing a useful `__repr__()` is valuable.

## 10. `__len__`

`__len__()` defines the behavior of:

```python
len(obj)
```

Example:

```python
class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


team = Team(["Nitin", "Rahul", "Amit"])

print(len(team))
```

Output:

```text
3
```

Python effectively asks the object for its length.

## 11. `__len__` Must Return an Integer

Correct:

```python
def __len__(self):
    return 10
```

Incorrect:

```python
def __len__(self):
    return "10"
```

The return value must be a non-negative integer suitable for Python's length protocol.

## 12. `__bool__`

`__bool__()` controls how an object behaves in a boolean context.

Example:

```python
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def __bool__(self):
        return self.balance > 0


account1 = BankAccount(1000)
account2 = BankAccount(0)

print(bool(account1))
print(bool(account2))
```

Output:

```text
True
False
```

Now:

```python
if account1:
    print("Account has balance")
```

works naturally.

### Relationship with `__len__`

If `__bool__()` is not defined, Python can use `__len__()` to determine truthiness.

Conceptually:

```text
__bool__()
    ↓
If defined → use it

Otherwise
    ↓
__len__()
    ↓
0 → False
non-zero → True
```

## 13. `__eq__`

`__eq__()` controls equality using:

```python
==
```

Example:

```python
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


user1 = User("Nitin", 25)
user2 = User("Nitin", 25)

print(user1 == user2)
```

Output:

```text
True
```

Without implementing appropriate equality behavior, two separate objects are not automatically considered equal merely because their attributes contain the same values.

## 14. Safe `__eq__` Implementation

A robust implementation should consider the type of the other object.

```python
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented

        return self.name == other.name and self.age == other.age
```

Then:

```python
user1 = User("Nitin", 25)
user2 = User("Nitin", 25)

print(user1 == user2)
```

Output:

```text
True
```

### Why `NotImplemented`?

It tells Python:

> "This comparison is not implemented for this type of object."

It is generally better than blindly accessing:

```python
other.name
```

because `other` might be an unrelated object.

## 15. `__ne__`

`__ne__()` represents:

```python
!=
```

Example:

```python
class User:

    def __init__(self, name):
        self.name = name

    def __ne__(self, other):
        if not isinstance(other, User):
            return NotImplemented

        return self.name != other.name
```

However, in modern Python, you often don't need to define `__ne__()` separately when `__eq__()` provides the appropriate equality behavior.

## 16. `__lt__`, `__le__`, `__gt__`, `__ge__`

These special methods support comparisons.

```text
<   → __lt__
<=  → __le__
>   → __gt__
>=  → __ge__
==  → __eq__
!=  → __ne__
```

Example:

```python
class Product:

    def __init__(self, price):
        self.price = price

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        return self.price < other.price


p1 = Product(100)
p2 = Product(200)

print(p1 < p2)
```

Output:

```text
True
```

## 17. Operator Overloading

**Operator overloading** means defining how operators behave for your custom objects.

Examples:

```text
+   → __add__
-   → __sub__
*   → __mul__
/   → __truediv__
==  → __eq__
<   → __lt__
>   → __gt__
```

Example:

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )


p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2

print(p3.x, p3.y)
```

Output:

```text
6 8
```

Instead of manually writing:

```python
p3 = Point(
    p1.x + p2.x,
    p1.y + p2.y
)
```

you can use:

```python
p3 = p1 + p2
```

## 18. `__add__`

`__add__()` controls:

```python
+
```

Example:

```python
class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented

        return Money(self.amount + other.amount)


m1 = Money(100)
m2 = Money(250)

m3 = m1 + m2

print(m3.amount)
```

Output:

```text
350
```

## 19. `__sub__`

Controls:

```python
-
```

Example:

```python
class Money:

    def __init__(self, amount):
        self.amount = amount

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented

        return Money(self.amount - other.amount)


m1 = Money(500)
m2 = Money(200)

m3 = m1 - m2

print(m3.amount)
```

Output:

```text
300
```

## 20. `__mul__`

Controls:

```python
*
```

Example:

```python
class Price:

    def __init__(self, amount):
        self.amount = amount

    def __mul__(self, quantity):
        return Price(self.amount * quantity)


price = Price(100)

total = price * 5

print(total.amount)
```

Output:

```text
500
```

## 21. `__truediv__`

Controls:

```python
/
```

Example:

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        if not isinstance(other, Number):
            return NotImplemented

        return Number(self.value / other.value)
```

## 22. Reverse Operators

Python also provides reverse arithmetic methods.

Examples:

```text
__radd__
__rsub__
__rmul__
__rtruediv__
```

Suppose:

```python
5 + obj
```

Python may first try the appropriate operation on the left operand and may then give the right operand an opportunity through its reflected operation.

For example:

```python
__radd__
```

can support:

```python
5 + obj
```

when the custom object needs to handle the operation.

Example:

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __radd__(self, other):
        return Number(other + self.value)


num = Number(10)

result = 5 + num

print(result.value)
```

Output:

```text
15
```

## 23. `__getitem__`

`__getitem__()` controls indexing and subscription.

Example:

```python
class ShoppingCart:

    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]


cart = ShoppingCart(["Laptop", "Mouse", "Keyboard"])

print(cart[0])
```

Output:

```text
Laptop
```

Python translates:

```python
cart[0]
```

into the object's subscription behavior.

## 24. Supporting Slicing with `__getitem__`

`__getitem__()` can also receive slices.

```python
class Numbers:

    def __init__(self, values):
        self.values = values

    def __getitem__(self, index):
        return self.values[index]


numbers = Numbers([10, 20, 30, 40, 50])

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

The important point is that `index` may be:

```python
int
```

or:

```python
slice
```

depending on the expression.

## 25. `__setitem__`

`__setitem__()` controls assignment through indexing.

Example:

```python
class ShoppingCart:

    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value


cart = ShoppingCart(["Laptop", "Mouse", "Keyboard"])

cart[1] = "Monitor"

print(cart[1])
```

Output:

```text
Monitor
```

This supports:

```python
cart[index] = value
```

## 26. `__delitem__`

`__delitem__()` controls:

```python
del obj[index]
```

Example:

```python
class ShoppingCart:

    def __init__(self, items):
        self.items = items

    def __delitem__(self, index):
        del self.items[index]


cart = ShoppingCart(["Laptop", "Mouse", "Keyboard"])

del cart[1]

print(cart.items)
```

Output:

```text
['Laptop', 'Keyboard']
```

## 27. `__contains__`

`__contains__()` controls membership testing:

```python
item in obj
```

Example:

```python
class ShoppingCart:

    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items


cart = ShoppingCart(["Laptop", "Mouse"])

print("Laptop" in cart)
print("Phone" in cart)
```

Output:

```text
True
False
```

## 28. `__iter__`

`__iter__()` allows an object to be used in a `for` loop.

Example:

```python
class Team:

    def __init__(self, members):
        self.members = members

    def __iter__(self):
        return iter(self.members)


team = Team(["Nitin", "Rahul", "Amit"])

for member in team:
    print(member)
```

Output:

```text
Nitin
Rahul
Amit
```

This is an important bridge between OOP and Python's iteration protocol.

## 29. `__next__`

`__next__()` defines how an iterator produces its next value.

A custom iterator typically implements both:

```python
__iter__()
__next__()
```

Example:

```python
class Counter:

    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration

        value = self.current
        self.current += 1

        return value


counter = Counter(3)

for value in counter:
    print(value)
```

Output:

```text
0
1
2
```

### Important

When there are no more values:

```python
raise StopIteration
```

signals that iteration is complete.

## 30. Iterable vs Iterator

This distinction is important.

### Iterable

An object that can provide an iterator.

Example:

```python
numbers = [1, 2, 3]
```

You can do:

```python
iter(numbers)
```

### Iterator

An object that produces values one at a time.

It implements:

```python
__iter__()
__next__()
```

Mental model:

```text
Iterable
   ↓
iter()
   ↓
Iterator
   ↓
next()
   ↓
Next value
```

## 31. `__call__`

`__call__()` makes an object callable.

Without `__call__`:

```python
class Greeter:
    pass


greeter = Greeter()

greeter()
```

would raise an error.

With `__call__`:

```python
class Greeter:

    def __call__(self, name):
        return f"Hello {name}"


greeter = Greeter()

print(greeter("Nitin"))
```

Output:

```text
Hello Nitin
```

Now the object behaves like a function.

## 32. Why `__call__` Is Useful

`__call__()` is useful when an object needs:

- Internal state
- Configuration
- Reusable callable behavior
- Function-like syntax

Example:

```python
class Multiplier:

    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


double = Multiplier(2)

print(double(10))
print(double(20))
```

Output:

```text
20
40
```

The object behaves like a function while retaining state.

## 33. `__enter__` and `__exit__`

These methods support the context manager protocol used by:

```python
with
```

Example:

```python
class MyContext:

    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


with MyContext():
    print("Inside context")
```

Output:

```text
Entering context
Inside context
Exiting context
```

### Mental Model

```text
with object:
    ↓
__enter__()
    ↓
Execute block
    ↓
__exit__()
```

## 34. Why Context Managers Matter

Context managers are commonly used for resources such as:

- Files
- Database connections
- Locks
- Transactions
- Network resources

For example:

```python
with open("data.txt") as file:
    data = file.read()
```

Python handles setup and cleanup around the `with` block.

## 35. `__enter__` Return Value

The object returned by `__enter__()` is assigned to the variable after `as`.

Example:

```python
class Resource:

    def __enter__(self):
        print("Opening resource")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing resource")


with Resource() as resource:
    print(resource)
```

Here:

```python
resource
```

refers to whatever `__enter__()` returned.

## 36. `__exit__` and Exceptions

`__exit__()` receives information about an exception if one occurred inside the `with` block.

Its parameters are:

```python
def __exit__(self, exc_type, exc_value, traceback):
    ...
```

Example:

```python
class MyContext:

    def __enter__(self):
        print("Start")

    def __exit__(self, exc_type, exc_value, traceback):
        print("End")
        print(exc_type)
```

If an exception occurs, `exc_type` contains the exception type.

Returning:

```python
True
```

from `__exit__()` can suppress the exception.

This should be done deliberately because hiding exceptions can make debugging difficult.

## 37. `__hash__`

`__hash__()` determines an object's hash value.

Hashing is important for objects used in:

```python
set
dict
```

as keys.

Example:

```python
class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def __hash__(self):
        return hash(self.user_id)
```

However, implementing `__hash__()` requires careful consideration of equality.

### Important Rule

If two objects compare equal:

```python
a == b
```

then they must have the same hash:

```python
hash(a) == hash(b)
```

Objects used as dictionary keys or set members should have a stable hash while they are stored.

## 38. `__eq__` and `__hash__`

This is an important interview topic.

Suppose:

```python
class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented

        return self.user_id == other.user_id

    def __hash__(self):
        return hash(self.user_id)
```

Now:

```python
u1 = User(1)
u2 = User(1)

print(u1 == u2)
print(hash(u1) == hash(u2))
```

Output:

```text
True
True
```

### Important

If an object is mutable in a way that changes values used for equality/hash, it can become unsafe to use as a dictionary key or set element.

This is why hashable objects should generally have stable identity-relevant state.

## 39. `__bool__`, `__len__`, and Truthiness

Python decides whether an object is truthy or falsy using the boolean protocol.

Example:

```python
class Collection:

    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


collection = Collection([])

if collection:
    print("Not empty")
else:
    print("Empty")
```

Output:

```text
Empty
```

Because:

```python
len(collection) == 0
```

## 40. `__format__`

`__format__()` controls custom formatting using:

```python
format(obj, spec)
```

and formatted strings.

Example:

```python
class Price:

    def __init__(self, amount):
        self.amount = amount

    def __format__(self, spec):
        if spec == "currency":
            return f"₹{self.amount:,.2f}"

        return str(self.amount)


price = Price(50000)

print(f"{price:currency}")
```

Output:

```text
₹50,000.00
```

This is useful when custom objects need controlled formatting.

## 41. `__bytes__`

`__bytes__()` controls conversion through:

```python
bytes(obj)
```

Example:

```python
class Message:

    def __init__(self, text):
        self.text = text

    def __bytes__(self):
        return self.text.encode("utf-8")


message = Message("Hello")

print(bytes(message))
```

Output:

```text
b'Hello'
```

This is less commonly needed in everyday application code but is part of Python's data model.

## 42. `__getattr__`

`__getattr__()` is called when normal attribute lookup fails.

Example:

```python
class User:

    def __init__(self, name):
        self.name = name

    def __getattr__(self, name):
        return f"{name} does not exist"


user = User("Nitin")

print(user.name)
print(user.age)
```

Output:

```text
Nitin
age does not exist
```

Important:

`__getattr__()` is called only when normal lookup does not find the attribute.

## 43. `__getattribute__`

`__getattribute__()` is called for attribute access.

It is more powerful and therefore easier to misuse.

Example:

```python
class User:

    def __getattribute__(self, name):
        print("Accessing:", name)
        return object.__getattribute__(self, name)
```

Now:

```python
user = User()

user.name
```

can trigger the custom attribute-access behavior.

### Important

`__getattribute__()` should be used carefully.

Incorrect implementations can easily cause infinite recursion.

For normal applications, you usually don't need to override it.

## 44. `__setattr__`

`__setattr__()` controls attribute assignment.

For example:

```python
class User:

    def __setattr__(self, name, value):
        print("Setting:", name)
        object.__setattr__(self, name, value)
```

Then:

```python
user = User()

user.name = "Nitin"
```

triggers the custom assignment behavior.

Again, this is advanced behavior and should be used only when there is a clear reason.

## 45. `__delattr__`

`__delattr__()` controls attribute deletion.

```python
class User:

    def __delattr__(self, name):
        print("Deleting:", name)
        object.__delattr__(self, name)
```

Then:

```python
del user.name
```

can trigger the custom behavior.

## 46. `__new__`

`__new__()` is responsible for creating and returning a new instance.

Example:

```python
class User:

    def __new__(cls):
        print("Creating object")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing object")


user = User()
```

Output:

```text
Creating object
Initializing object
```

### Object Creation Flow

```text
User()
  ↓
__new__()
  ↓
Object created
  ↓
__init__()
  ↓
Object initialized
```

For normal classes, you usually don't need to override `__new__()`.

It becomes useful in advanced cases such as:

- Immutable types
- Custom object creation
- Certain singleton implementations
- Metaprogramming

## 47. Comparison Dunder Methods

Python provides special methods for rich comparisons.

| Operator | Method |
|---|---|
| `a == b` | `__eq__` |
| `a != b` | `__ne__` |
| `a < b` | `__lt__` |
| `a <= b` | `__le__` |
| `a > b` | `__gt__` |
| `a >= b` | `__ge__` |

Example:

```python
class Student:

    def __init__(self, marks):
        self.marks = marks

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented

        return self.marks < other.marks


s1 = Student(70)
s2 = Student(90)

print(s1 < s2)
```

Output:

```text
True
```

## 48. Arithmetic Dunder Methods

Common arithmetic mappings:

| Operator | Method |
|---|---|
| `+` | `__add__` |
| `-` | `__sub__` |
| `*` | `__mul__` |
| `/` | `__truediv__` |
| `//` | `__floordiv__` |
| `%` | `__mod__` |
| `**` | `__pow__` |
| `@` | `__matmul__` |

Reverse versions include:

```text
__radd__
__rsub__
__rmul__
__rtruediv__
...
```

In-place versions include:

```text
__iadd__
__isub__
__imul__
...
```

## 49. In-Place Operators

For:

```python
a += b
```

Python can use:

```python
__iadd__
```

when the object provides it.

Example:

```python
class Counter:

    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other
        return self


counter = Counter(10)

counter += 5

print(counter.value)
```

Output:

```text
15
```

The method should return the object appropriately.

## 50. `__repr__` in Collections

Consider:

```python
class User:

    def __init__(self, name):
        self.name = name
```

Then:

```python
users = [
    User("Nitin"),
    User("Rahul")
]

print(users)
```

Without a custom `__repr__()`, the output is difficult to understand.

Adding:

```python
def __repr__(self):
    return f"User(name={self.name!r})"
```

makes it much clearer:

```text
[User(name='Nitin'), User(name='Rahul')]
```

This is one of the most practical reasons to implement `__repr__()`.

## 51. Complete Practical Example

Let's combine several dunder methods.

```python
class ShoppingCart:

    def __init__(self, items):
        self.items = items

    def __str__(self):
        return f"ShoppingCart({len(self.items)} items)"

    def __repr__(self):
        return f"ShoppingCart(items={self.items!r})"

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)


cart = ShoppingCart([
    "Laptop",
    "Mouse",
    "Keyboard"
])

print(cart)
print(repr(cart))

print(len(cart))
print(cart[0])
print("Mouse" in cart)

for item in cart:
    print(item)
```

Output:

```text
ShoppingCart(3 items)
ShoppingCart(items=['Laptop', 'Mouse', 'Keyboard'])
3
Laptop
True
Laptop
Mouse
Keyboard
```

This demonstrates how dunder methods make custom objects behave naturally.

## 52. Dunder Methods vs Normal Methods

### Normal method

```python
class User:

    def greet(self):
        return "Hello"
```

Called explicitly:

```python
user.greet()
```

### Dunder method

```python
class User:

    def __str__(self):
        return "User"
```

Usually triggered by Python syntax:

```python
print(user)
```

Mental model:

```text
Normal Method
    ↓
Developer explicitly calls it

Dunder Method
    ↓
Python syntax / built-in operation triggers it
```

## 53. Don't Call Dunder Methods Directly Without a Reason

You technically can write:

```python
obj.__str__()
```

but normally prefer:

```python
str(obj)
```

Similarly:

```python
obj.__len__()
```

should normally be:

```python
len(obj)
```

And:

```python
obj.__add__(other)
```

should normally be:

```python
obj + other
```

### Why?

Because Python's built-in operations communicate intent more clearly and correctly use the relevant protocol.

## 54. Common Mistake — Wrong Return Type

Dunder methods often have required return types.

For example:

```python
def __str__(self):
    return 100
```

is incorrect.

`__str__()` must return:

```python
str
```

Similarly:

```python
__len__()
```

must return an appropriate integer.

Always understand the protocol expected by the special method.

## 55. Common Mistake — Returning `None` from `__add__`

Consider:

```python
def __add__(self, other):
    self.amount += other.amount
```

Then:

```python
result = money1 + money2
```

would receive:

```text
None
```

unless the method returns an appropriate result.

A typical implementation is:

```python
def __add__(self, other):
    return Money(self.amount + other.amount)
```

Dunder methods should follow the expected semantics of the operation.

## 56. Common Mistake — Unsafe `__eq__`

Avoid:

```python
def __eq__(self, other):
    return self.id == other.id
```

because `other` may not be the same type.

Prefer:

```python
def __eq__(self, other):
    if not isinstance(other, User):
        return NotImplemented

    return self.id == other.id
```

## 57. Common Mistake — Incorrect `__hash__`

If you customize:

```python
__eq__()
```

you must think carefully about hashing.

Objects that compare equal should have the same hash.

Do not blindly write:

```python
def __hash__(self):
    return id(self)
```

if equality is based on some other logical value.

The equality and hashing rules must remain consistent.

## 58. Common Mistake — Overusing Dunder Methods

Don't implement dunder methods just because you can.

Bad design:

```python
class User:

    def __add__(self, other):
        ...
```

if adding users has no meaningful domain interpretation.

Good use:

```python
class Money:

    def __add__(self, other):
        ...
```

because adding monetary values has a clear meaning.

### Rule

> Use operator overloading when the operation is intuitive and semantically meaningful.

## 59. Dunder Methods and Pythonic Code

Dunder methods help classes follow Python's conventions.

Instead of:

```python
cart.get_length()
```

you can provide:

```python
len(cart)
```

Instead of:

```python
cart.get_item(index)
```

you can provide:

```python
cart[index]
```

Instead of:

```python
cart.contains(item)
```

you can provide:

```python
item in cart
```

Instead of:

```python
money.add(other)
```

you can provide:

```python
money + other
```

This is what makes a class feel **Pythonic**.

## 60. Important Dunder Methods to Know

You do not need to memorize every dunder method.

Focus on commonly used ones:

```text
Object creation / initialization
---------------------------------
__new__
__init__

String representation
---------------------
__str__
__repr__

Size / truthiness
-----------------
__len__
__bool__

Comparison
----------
__eq__
__ne__
__lt__
__le__
__gt__
__ge__

Arithmetic
----------
__add__
__sub__
__mul__
__truediv__
__floordiv__
__mod__
__pow__

Collection behavior
-------------------
__getitem__
__setitem__
__delitem__
__contains__

Iteration
---------
__iter__
__next__

Callable objects
---------------
__call__

Context managers
----------------
__enter__
__exit__

Hashing
-------
__hash__

Attribute behavior
------------------
__getattr__
__getattribute__
__setattr__
__delattr__
```

## 61. Dunder Method Cheat Sheet

| Python Syntax | Special Method |
|---|---|
| `str(obj)` | `__str__` |
| `repr(obj)` | `__repr__` |
| `len(obj)` | `__len__` |
| `bool(obj)` | `__bool__` |
| `obj == other` | `__eq__` |
| `obj != other` | `__ne__` |
| `obj < other` | `__lt__` |
| `obj <= other` | `__le__` |
| `obj > other` | `__gt__` |
| `obj >= other` | `__ge__` |
| `obj + other` | `__add__` |
| `obj - other` | `__sub__` |
| `obj * other` | `__mul__` |
| `obj / other` | `__truediv__` |
| `obj[index]` | `__getitem__` |
| `obj[index] = value` | `__setitem__` |
| `del obj[index]` | `__delitem__` |
| `item in obj` | `__contains__` |
| `for x in obj` | `__iter__` |
| `next(obj)` | `__next__` |
| `obj()` | `__call__` |
| `with obj` | `__enter__`, `__exit__` |
| `hash(obj)` | `__hash__` |

## 62. Interview Questions

### Q1. What are dunder methods?

Dunder methods are Python special methods whose names begin and end with double underscores.

They allow objects to participate in Python's built-in protocols and syntax.

### Q2. Why are they called dunder methods?

"Dunder" is short for:

```text
Double UNDERscore
```

### Q3. What is the difference between `__str__` and `__repr__`?

```text
__str__
    ↓
Human-readable representation

__repr__
    ↓
Developer/debugging representation
```

### Q4. What does `__len__` do?

It defines the behavior of:

```python
len(obj)
```

### Q5. What is operator overloading?

Operator overloading allows custom classes to define how operators behave.

Example:

```python
a + b
```

can be implemented using:

```python
__add__
```

### Q6. What does `__getitem__` do?

It defines indexing/subscription behavior.

```python
obj[index]
```

### Q7. What does `__call__` do?

It makes an object callable.

```python
obj()
```

### Q8. What is the purpose of `__iter__`?

It allows an object to provide an iterator and participate in iteration.

### Q9. What is the purpose of `__next__`?

It returns the next item from an iterator and raises `StopIteration` when iteration is complete.

### Q10. What is the purpose of `__enter__` and `__exit__`?

They implement the context manager protocol used by:

```python
with
```

### Q11. Why should `__eq__` sometimes return `NotImplemented`?

When the other object is not a compatible type, returning `NotImplemented` lets Python handle the comparison appropriately instead of forcing an invalid comparison.

### Q12. Why must `__eq__` and `__hash__` be consistent?

If:

```python
a == b
```

is true, then:

```python
hash(a) == hash(b)
```

must also be true for objects participating in hashing.

## 63. Interview Coding Question

What will this code print?

```python
class Box:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Box({self.value})"

    def __len__(self):
        return self.value


box = Box(5)

print(box)
print(len(box))
```

Output:

```text
Box(5)
5
```

Why?

```text
print(box)
    ↓
__str__()

len(box)
    ↓
__len__()
```

## 64. Interview Coding Question — Operator Overloading

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)


a = Number(10)
b = Number(20)

c = a + b

print(c.value)
```

Output:

```text
30
```

Because:

```python
a + b
```

uses:

```python
a.__add__(b)
```

## 65. Interview Coding Question — Callable Object

```python
class Multiplier:

    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


double = Multiplier(2)

print(double(5))
```

Output:

```text
10
```

The object behaves like a function because it implements:

```python
__call__
```

## 66. Interview Coding Question — Iteration

```python
class Numbers:

    def __init__(self, values):
        self.values = values

    def __iter__(self):
        return iter(self.values)


numbers = Numbers([1, 2, 3])

for number in numbers:
    print(number)
```

Output:

```text
1
2
3
```

Because Python obtains an iterator through:

```python
__iter__()
```

## 67. Dunder Methods and Your Previous OOP Topics

Dunder methods connect directly with the concepts you've already learned.

### Encapsulation

Special methods can control access and behavior around objects.

```python
__getattr__
__getattribute__
__setattr__
__delattr__
```

### Polymorphism

Different classes can implement the same special method differently.

```python
class Dog:

    def __str__(self):
        return "Dog"


class Cat:

    def __str__(self):
        return "Cat"
```

Same operation:

```python
str(obj)
```

Different behavior.

### Abstraction

Python protocols allow you to define behavior without requiring callers to know the implementation details.

### Inheritance

Dunder methods can be inherited and overridden like other methods.

### Object Introspection

You can inspect special methods using:

```python
dir(obj)
```

or:

```python
type(obj).__dict__
```

## 68. Practical Rules for Using Dunder Methods

### Rule 1

Don't memorize every dunder method.

Understand the important protocols.

### Rule 2

Prefer normal Python syntax.

Use:

```python
len(obj)
```

instead of:

```python
obj.__len__()
```

### Rule 3

Only overload operators when the meaning is obvious.

### Rule 4

Maintain consistency between:

```python
__eq__
__hash__
```

when objects are hashable.

### Rule 5

Return the correct type required by the protocol.

### Rule 6

Use `__repr__()` for useful debugging output.

### Rule 7

Don't override advanced methods such as:

```python
__getattribute__
```

unless you have a clear reason.

## 69. Quick Revision

Remember these core mappings:

```text
str(obj)
    ↓
__str__

repr(obj)
    ↓
__repr__

len(obj)
    ↓
__len__

bool(obj)
    ↓
__bool__

obj == other
    ↓
__eq__

obj + other
    ↓
__add__

obj[index]
    ↓
__getitem__

obj[index] = value
    ↓
__setitem__

item in obj
    ↓
__contains__

for item in obj
    ↓
__iter__

next(obj)
    ↓
__next__

obj()
    ↓
__call__

with obj
    ↓
__enter__
__exit__

hash(obj)
    ↓
__hash__
```

## 70. Final Mental Model

Think of dunder methods as **hooks that allow Python's syntax to communicate with your objects**.

```text
                    Python Syntax
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
      Built-ins       Operators      Keywords
          │              │              │
      len(obj)         a + b         with obj
      str(obj)         a == b            │
      bool(obj)        a < b             ↓
          │              │          __enter__
          ↓              ↓          __exit__
     __len__          __add__
     __str__          __eq__
     __bool__         __lt__
                         │
                         ↓
                  Custom Object
```

The key idea is:

> **Dunder methods let your custom objects participate naturally in Python's built-in operations, operators, and protocols.**

## 71. Lecture 11 Checklist

- [ ] Understand what dunder methods are
- [ ] Understand Python's data model
- [ ] Understand `__init__`
- [ ] Understand `__new__`
- [ ] Understand `__str__`
- [ ] Understand `__repr__`
- [ ] Understand `__len__`
- [ ] Understand `__bool__`
- [ ] Understand `__eq__`
- [ ] Understand comparison methods
- [ ] Understand operator overloading
- [ ] Understand `__add__`
- [ ] Understand reverse operators
- [ ] Understand in-place operators
- [ ] Understand `__getitem__`
- [ ] Understand `__setitem__`
- [ ] Understand `__delitem__`
- [ ] Understand `__contains__`
- [ ] Understand `__iter__`
- [ ] Understand `__next__`
- [ ] Understand iterable vs iterator
- [ ] Understand `__call__`
- [ ] Understand `__enter__`
- [ ] Understand `__exit__`
- [ ] Understand `__hash__`
- [ ] Understand `__eq__` and `__hash__` relationship
- [ ] Know basic attribute-access dunder methods
- [ ] Understand when operator overloading makes sense
- [ ] Know common dunder-method mistakes
- [ ] Practice building Pythonic custom classes

## Next Lecture

**Lecture 12 → Python OOP Design Patterns**

Topics:

- What is a design pattern?
- Why design patterns are useful
- Creational patterns
- Factory Pattern
- Singleton Pattern
- Builder Pattern
- Structural patterns
- Adapter Pattern
- Decorator Pattern
- Facade Pattern
- Behavioral patterns
- Strategy Pattern
- Observer Pattern
- Command Pattern
- Template Method Pattern
- Python-specific ways of implementing patterns
- When to use and avoid patterns
- Common interview questions