# Python OOP — Lecture 10: Object Introspection

My personal notes for understanding **Object Introspection in Python**, with practical examples, debugging techniques, and interview preparation.

## 1. What is Object Introspection?

**Object introspection** means examining an object, class, or function at runtime to understand:

- What type it is
- What attributes it has
- What methods it provides
- What class it belongs to
- What values it currently contains
- What methods and attributes are available
- What inheritance hierarchy it follows
- What parameters a function accepts

Python provides many built-in tools for this.

Example:

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello {self.name}"


user = User("Nitin", 25)

print(type(user))
print(user.__dict__)
print(dir(user))
```

### Simple Mental Model

```text
Object
   ↓
Inspect at Runtime
   ↓
Type
Attributes
Methods
Class
Inheritance
Metadata
   ↓
Understand Object
```

## 2. Why Object Introspection Matters

Introspection is useful for:

- Debugging
- Understanding unfamiliar code
- Working with dynamic Python code
- Framework development
- Writing reusable utilities
- Testing
- Plugin systems
- Serialization
- Dependency injection
- Understanding objects created by libraries
- Interview questions

For example, if you receive an object from a library and don't know what it contains:

```python
result = some_library_function()

print(type(result))
print(dir(result))
print(vars(result))
```

You can inspect it without reading the entire library source code.

## 3. `type()`

`type()` tells you the type/class of an object.

```python
x = 10
name = "Nitin"
numbers = [1, 2, 3]

print(type(x))
print(type(name))
print(type(numbers))
```

Output:

```text
<class 'int'>
<class 'str'>
<class 'list'>
```

With custom classes:

```python
class User:
    pass


user = User()

print(type(user))
```

Output:

```text
<class '__main__.User'>
```

### Why `type()` is useful

It answers:

> "What exact type is this object?"

## 4. `type()` vs `isinstance()`

This is an important interview topic.

Consider:

```python
class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()
```

Using `type()`:

```python
print(type(dog) == Dog)
```

Output:

```text
True
```

But:

```python
print(type(dog) == Animal)
```

Output:

```text
False
```

Using `isinstance()`:

```python
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
```

Output:

```text
True
True
```

Because `Dog` inherits from `Animal`.

### Important Difference

```text
type(obj)
    ↓
Exact type

isinstance(obj, Class)
    ↓
Whether object belongs to class
or one of its subclasses
```

### General Recommendation

When checking whether an object belongs to a class hierarchy, prefer:

```python
isinstance()
```

instead of:

```python
type(obj) == Class
```

## 5. `isinstance()`

`isinstance()` checks whether an object is an instance of a particular class or tuple of classes.

```python
x = 10

print(isinstance(x, int))
print(isinstance(x, str))
```

Output:

```text
True
False
```

You can check multiple types:

```python
value = 10

print(isinstance(value, (int, float)))
```

Output:

```text
True
```

### With inheritance

```python
class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
```

Both are:

```text
True
```

## 6. `issubclass()`

`issubclass()` checks whether one class inherits from another class.

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

But:

```python
print(issubclass(Animal, Dog))
```

Output:

```text
False
```

### Difference

```text
isinstance()
    ↓
Object → Class

issubclass()
    ↓
Class → Class
```

Example:

```python
dog = Dog()

isinstance(dog, Animal)

issubclass(Dog, Animal)
```

## 7. `id()`

`id()` returns an integer identifying an object during its lifetime.

```python
x = [1, 2, 3]

print(id(x))
```

The exact number is implementation-dependent.

You can compare object identity:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(id(a) == id(b))
print(id(a) == id(c))
```

Output:

```text
True
False
```

Because:

```text
a ───────┐
         ↓
      [1, 2, 3]
         ↑
b ───────┘

c → [1, 2, 3]
```

`a` and `b` reference the same object.

`c` is a different object.

## 8. `is` vs `==`

This is closely related to object identity.

### `==`

Checks value equality.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
```

Output:

```text
True
```

### `is`

Checks object identity.

```python
print(a is b)
```

Output:

```text
False
```

Because they are different objects.

### Mental Model

```text
==  → Same value?

is  → Same object?
```

Example:

```python
a = [1, 2, 3]
b = a

print(a == b)
print(a is b)
```

Both are:

```text
True
```

## 9. `dir()`

`dir()` returns the names available on an object.

```python
numbers = [1, 2, 3]

print(dir(numbers))
```

You will see things such as:

```text
append
clear
copy
count
extend
index
insert
pop
remove
reverse
sort
...
```

It also contains special methods:

```text
__len__
__getitem__
__iter__
__class__
...
```

### Custom Class

```python
class User:

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"


user = User("Nitin")

print(dir(user))
```

You will find:

```text
name
greet
__class__
__dict__
...
```

### Why `dir()` is useful

If you don't know what an object supports:

```python
print(dir(object))
```

It gives you a quick list of available attributes and methods.

## 10. Important Note About `dir()`

`dir()` is useful for exploration, but it should not be treated as a perfect representation of everything an object can do.

For example, dynamically provided attributes or custom attribute resolution may not always behave exactly as expected.

Use it as:

```text
Exploration / Debugging Tool
```

not as:

```text
Complete Formal API Definition
```

## 11. `help()`

`help()` displays documentation about an object, class, function, or module.

```python
help(str)
```

You can also inspect a specific method:

```python
help(str.upper)
```

For your own class:

```python
class User:

    def greet(self):
        """Return a greeting message."""
        return "Hello"


help(User)
```

Documentation strings can therefore make introspection more useful.

## 12. `hasattr()`

`hasattr()` checks whether an object has a particular attribute.

```python
class User:

    def __init__(self):
        self.name = "Nitin"


user = User()

print(hasattr(user, "name"))
print(hasattr(user, "age"))
```

Output:

```text
True
False
```

You can also check methods:

```python
class User:

    def greet(self):
        pass


user = User()

print(hasattr(user, "greet"))
```

Output:

```text
True
```

## 13. `getattr()`

`getattr()` retrieves an attribute dynamically.

```python
class User:

    def __init__(self):
        self.name = "Nitin"


user = User()

print(getattr(user, "name"))
```

Output:

```text
Nitin
```

Instead of:

```python
user.name
```

you can dynamically do:

```python
attribute_name = "name"

print(getattr(user, attribute_name))
```

This is useful when the attribute name is stored in a variable.

## 14. `getattr()` with a Default Value

You can provide a default value.

```python
class User:

    def __init__(self):
        self.name = "Nitin"


user = User()

print(getattr(user, "age", 0))
```

Output:

```text
0
```

Without a default:

```python
getattr(user, "age")
```

would raise:

```text
AttributeError
```

### Useful Pattern

```python
value = getattr(obj, "attribute_name", default_value)
```

## 15. `setattr()`

`setattr()` dynamically creates or modifies an attribute.

```python
class User:
    pass


user = User()

setattr(user, "name", "Nitin")

print(user.name)
```

Output:

```text
Nitin
```

Equivalent to:

```python
user.name = "Nitin"
```

But `setattr()` becomes useful when the attribute name is dynamic.

```python
field = "name"
value = "Nitin"

setattr(user, field, value)

print(user.name)
```

## 16. `delattr()`

`delattr()` dynamically removes an attribute.

```python
class User:

    def __init__(self):
        self.name = "Nitin"


user = User()

print(user.name)

delattr(user, "name")

print(hasattr(user, "name"))
```

Output:

```text
Nitin
False
```

Equivalent to:

```python
del user.name
```

## 17. `hasattr()` + `getattr()` + `setattr()` + `delattr()`

These four functions are commonly learned together.

```text
hasattr()
    ↓
Does attribute exist?

getattr()
    ↓
Get attribute

setattr()
    ↓
Set/create attribute

delattr()
    ↓
Delete attribute
```

Example:

```python
class User:
    pass


user = User()

setattr(user, "name", "Nitin")

if hasattr(user, "name"):
    print(getattr(user, "name"))

delattr(user, "name")
```

## 18. `vars()`

`vars()` returns the `__dict__` of an object when available.

Example:

```python
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Nitin", 25)

print(vars(user))
```

Output:

```text
{'name': 'Nitin', 'age': 25}
```

It is similar to:

```python
print(user.__dict__)
```

You can also use:

```python
print(vars(User))
```

to inspect the class namespace.

## 19. `__dict__`

`__dict__` contains an object's namespace.

```python
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Nitin", 25)

print(user.__dict__)
```

Output:

```text
{
    'name': 'Nitin',
    'age': 25
}
```

You can also inspect a class:

```python
print(User.__dict__)
```

This contains the class namespace, including methods and class-level attributes.

## 20. Object `__dict__` vs Class `__dict__`

This distinction is important.

```python
class User:

    company = "ABC"

    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello"
```

Create object:

```python
user = User("Nitin")
```

Object dictionary:

```python
print(user.__dict__)
```

Output:

```text
{'name': 'Nitin'}
```

Class dictionary:

```python
print(User.__dict__)
```

Contains entries related to:

```text
company
__init__
greet
...
```

### Mental Model

```text
user.__dict__
    ↓
Object-specific state

User.__dict__
    ↓
Class namespace
```

## 21. Class Attribute Lookup Through Introspection

Consider:

```python
class User:

    company = "ABC"

    def __init__(self, name):
        self.name = name


user = User("Nitin")
```

Now:

```python
print(user.__dict__)
```

Output:

```text
{'name': 'Nitin'}
```

Notice that `company` isn't stored in the object's dictionary.

But:

```python
print(user.company)
```

works.

Why?

Python looks roughly like:

```text
user.__dict__
     ↓
Does company exist?
     ↓
No
     ↓
Look at class
     ↓
User.__dict__
     ↓
company found
```

This connects directly to the attribute lookup concepts from earlier OOP lectures.

## 22. `__class__`

Every normal Python object has a `__class__` reference.

```python
class User:
    pass


user = User()

print(user.__class__)
```

Output:

```text
<class '__main__.User'>
```

This is conceptually related to:

```python
type(user)
```

For normal objects:

```python
type(user) == user.__class__
```

will generally be:

```text
True
```

## 23. `__name__`

Classes and functions can have a `__name__`.

```python
class User:
    pass


print(User.__name__)
```

Output:

```text
User
```

For functions:

```python
def calculate():
    pass


print(calculate.__name__)
```

Output:

```text
calculate
```

Useful when debugging or building dynamic systems.

## 24. `__module__`

`__module__` tells you the module where a class or function was defined.

```python
class User:
    pass


print(User.__module__)
```

If defined directly in your Python file, you may see:

```text
__main__
```

This becomes more useful when working with packages and modules.

## 25. `__bases__`

`__bases__` tells you the direct parent classes of a class.

```python
class Animal:
    pass


class Dog(Animal):
    pass


print(Dog.__bases__)
```

Output:

```text
(<class '__main__.Animal'>,)
```

For multiple inheritance:

```python
class A:
    pass


class B:
    pass


class C(A, B):
    pass


print(C.__bases__)
```

Output:

```text
(<class '__main__.A'>, <class '__main__.B'>)
```

## 26. MRO Introspection

Python uses Method Resolution Order (MRO) to determine where methods are searched.

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


class C(B):
    pass


print(C.mro())
```

You can also use:

```python
print(C.__mro__)
```

Typical result:

```text
C
B
A
object
```

### Why this matters

MRO becomes especially important with multiple inheritance and `super()`.

Mental model:

```text
C
↓
B
↓
A
↓
object
```

Python searches according to the MRO.

## 27. `callable()`

`callable()` checks whether an object can be called using `()`.

```python
def greet():
    return "Hello"


print(callable(greet))
```

Output:

```text
True
```

For an integer:

```python
x = 10

print(callable(x))
```

Output:

```text
False
```

Classes are callable too:

```python
class User:
    pass


print(callable(User))
```

Output:

```text
True
```

Why?

Because:

```python
User()
```

creates an object.

## 28. Inspecting Methods Dynamically

Suppose:

```python
class User:

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"

    def logout(self):
        return "Logged out"


user = User("Nitin")
```

You can inspect:

```python
print(dir(user))
```

You can check:

```python
print(hasattr(user, "greet"))
```

You can retrieve:

```python
method = getattr(user, "greet")

print(method())
```

This gives:

```text
Hello Nitin
```

### Dynamic Method Calling

```python
method_name = "greet"

method = getattr(user, method_name)

result = method()

print(result)
```

This technique appears in dynamic Python applications.

## 29. Practical Example — Dynamic Command Execution

Suppose:

```python
class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b
```

Instead of:

```python
calculator.add(10, 5)
```

you can dynamically select the operation:

```python
calculator = Calculator()

operation = "multiply"

method = getattr(calculator, operation)

result = method(10, 5)

print(result)
```

Output:

```text
50
```

The method name can come from configuration, user input, or another part of the program.

## 30. `inspect` Module

Python also provides the `inspect` module for more advanced introspection.

```python
import inspect
```

It provides utilities for inspecting:

- Functions
- Classes
- Methods
- Signatures
- Source code
- Modules
- Callables
- Members

For practical Python development, the most useful functions are:

```python
inspect.getmembers()
inspect.signature()
inspect.isfunction()
inspect.ismethod()
inspect.isclass()
```

## 31. `inspect.signature()`

You can inspect the parameters accepted by a function.

```python
import inspect


def add(a, b, c=0):
    return a + b + c


print(inspect.signature(add))
```

Output:

```text
(a, b, c=0)
```

This is useful when working with unknown functions or framework code.

## 32. `inspect.getmembers()`

`inspect.getmembers()` returns members of an object.

```python
import inspect


class User:

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"


members = inspect.getmembers(User)

for name, value in members:
    print(name, value)
```

This gives you a collection of:

```text
(name, value)
```

pairs.

You can also filter them.

## 33. Filtering Methods with `inspect`

```python
import inspect


class User:

    def greet(self):
        pass

    def logout(self):
        pass


methods = inspect.getmembers(User, predicate=inspect.isfunction)

for name, method in methods:
    print(name)
```

Output:

```text
greet
logout
```

This is useful when you specifically want to inspect functions/methods rather than every member.

## 34. `inspect.isfunction()`

```python
import inspect


def greet():
    pass


print(inspect.isfunction(greet))
```

Output:

```text
True
```

You can use similar helpers:

```python
inspect.isclass()
inspect.ismethod()
inspect.isfunction()
inspect.isbuiltin()
```

These allow you to identify what kind of object you are inspecting.

## 35. Introspection Example — Debugging an Unknown Object

Imagine a function returns an object:

```python
result = get_result()
```

You don't know much about it.

Instead of guessing:

```python
print(type(result))
print(result.__dict__)
print(dir(result))
```

Then:

```python
print(vars(result))
```

And:

```python
print(hasattr(result, "status"))
```

You can investigate the object systematically.

### Practical Debugging Flow

```text
Unknown Object
      ↓
type()
      ↓
dir()
      ↓
vars() / __dict__
      ↓
hasattr()
      ↓
getattr()
      ↓
inspect
```

## 36. Introspection and Frameworks

Introspection is heavily used by Python frameworks and libraries.

Examples include:

- Web frameworks
- ORM systems
- Testing frameworks
- Serialization libraries
- CLI frameworks
- Dependency injection systems
- Plugin systems

A framework may inspect:

```text
function parameters
class methods
type annotations
attributes
decorators
inheritance
```

and use that information to decide what to execute or how to configure an object.

## 37. Introspection vs Reflection

These terms are related but not exactly identical.

### Introspection

Examining an object.

Examples:

```python
type(obj)
dir(obj)
vars(obj)
hasattr(obj, "name")
```

### Reflection

A broader concept involving examining and potentially dynamically interacting with program structure.

Examples:

```python
getattr()
setattr()
delattr()
```

Python supports both introspection and reflective capabilities.

For everyday Python development, the practical focus should be:

```text
Inspect
Understand
Dynamically access when necessary
```

## 38. Introspection and Encapsulation

Remember the encapsulation lecture.

Consider:

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance
```

Python name-mangles the attribute.

You might inspect:

```python
account = BankAccount(1000)

print(account.__dict__)
```

You may see something similar to:

```text
{'_BankAccount__balance': 1000}
```

This demonstrates that:

```text
__balance
```

is not true security.

It is name mangling.

You can learn more about this through introspection.

## 39. Introspection and `__slots__`

Not every object necessarily has a normal `__dict__`.

Example:

```python
class User:

    __slots__ = ("name",)

    def __init__(self, name):
        self.name = name
```

Now:

```python
user = User("Nitin")
```

Trying:

```python
print(user.__dict__)
```

may raise:

```text
AttributeError
```

This is an important reminder:

> Don't assume every Python object has `__dict__`.

For general inspection:

```python
print(dir(user))
```

may still be useful.

## 40. `vars()` vs `dir()`

These are not interchangeable.

### `dir()`

Shows available names.

```python
dir(obj)
```

### `vars()`

Shows the object's namespace when available.

```python
vars(obj)
```

Example:

```python
class User:

    company = "ABC"

    def __init__(self, name):
        self.name = name
```

For:

```python
user = User("Nitin")
```

You might see:

```python
vars(user)
```

as:

```text
{'name': 'Nitin'}
```

while:

```python
dir(user)
```

includes many more names inherited or provided by the class.

### Mental Model

```text
dir()
    ↓
"What names are available?"

vars()
    ↓
"What is stored in this namespace?"
```

## 41. Practical Example — Generic Object Inspector

You can create a small debugging utility:

```python
def inspect_object(obj):
    print("Type:", type(obj))
    print("Class:", obj.__class__)
    print("ID:", id(obj))
    print("Callable:", callable(obj))

    print("\nAttributes:")
    for name in dir(obj):
        if not name.startswith("__"):
            print(name)
```

Example:

```python
class User:

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"


user = User("Nitin")

inspect_object(user)
```

This is a practical application of several introspection concepts.

## 42. Practical Example — Safe Dynamic Attribute Access

Instead of:

```python
print(user.age)
```

when the attribute may not exist:

```python
age = getattr(user, "age", None)

if age is not None:
    print(age)
else:
    print("Age not available")
```

This is useful when working with dynamic objects.

## 43. Common Mistake — Using `type()` Everywhere

Avoid writing:

```python
if type(value) == int:
    ...
```

when inheritance or compatible subclasses matter.

Usually:

```python
if isinstance(value, int):
    ...
```

is more flexible.

## 44. Common Mistake — Assuming `__dict__` Always Exists

This can fail:

```python
print(obj.__dict__)
```

because some objects use:

```python
__slots__
```

or implement their structure differently.

Use it when you know the object supports it.

## 45. Common Mistake — Using `dir()` as an API Contract

Don't assume:

```python
dir(obj)
```

is a guaranteed complete API specification.

It is mainly useful for:

```text
Exploration
Debugging
Learning
```

For library usage, rely on the documented API.

## 46. Common Mistake — Overusing Dynamic Attribute Access

This:

```python
getattr(obj, "name")
```

is useful when the attribute name is dynamic.

But if you already know the attribute:

```python
obj.name
```

is usually clearer.

Use introspection because it solves a real problem, not simply because Python allows it.

## 47. Object Introspection Cheat Sheet

| Tool | Purpose |
|---|---|
| `type()` | Get exact object type |
| `isinstance()` | Check object/class relationship |
| `issubclass()` | Check class inheritance |
| `id()` | Get object identity |
| `is` | Check object identity |
| `dir()` | List available names |
| `help()` | Display documentation |
| `hasattr()` | Check attribute existence |
| `getattr()` | Dynamically get attribute |
| `setattr()` | Dynamically set attribute |
| `delattr()` | Dynamically delete attribute |
| `vars()` | Get object's namespace |
| `__dict__` | Access namespace directly |
| `__class__` | Get object's class |
| `__name__` | Get class/function name |
| `__module__` | Get defining module |
| `__bases__` | Get direct base classes |
| `__mro__` | Get MRO |
| `callable()` | Check if object can be called |
| `inspect.signature()` | Inspect callable parameters |
| `inspect.getmembers()` | Inspect object members |

## 48. Object Introspection Decision Guide

When you encounter an unknown object:

### Step 1 — What is it?

```python
type(obj)
```

### Step 2 — Is it a particular type?

```python
isinstance(obj, SomeClass)
```

### Step 3 — What does it provide?

```python
dir(obj)
```

### Step 4 — What state does it contain?

```python
vars(obj)
```

or:

```python
obj.__dict__
```

### Step 5 — Does a particular attribute exist?

```python
hasattr(obj, "name")
```

### Step 6 — Get it dynamically

```python
getattr(obj, "name", default)
```

### Step 7 — Modify dynamically if required

```python
setattr(obj, "name", value)
```

### Step 8 — Understand inheritance

```python
obj.__class__.mro()
```

### Step 9 — Need deeper inspection?

```python
import inspect

inspect.getmembers(obj)
inspect.signature(function)
```

## 49. Interview Questions

### Beginner

#### Q1. What is object introspection?

Object introspection is the ability to examine objects, classes, functions, and their properties at runtime.

#### Q2. What is the difference between `type()` and `isinstance()`?

```python
type(obj)
```

gets the exact type.

```python
isinstance(obj, Class)
```

checks whether the object is an instance of that class or its subclasses.

#### Q3. What does `issubclass()` do?

It checks whether one class inherits from another class.

```python
issubclass(Dog, Animal)
```

#### Q4. What does `dir()` do?

It returns a list of names available on an object.

#### Q5. What does `vars()` do?

For objects that have a `__dict__`, `vars(obj)` returns that namespace dictionary.

### Intermediate

#### Q6. Difference between `dir()` and `__dict__`?

```text
dir()
    → available names

__dict__
    → namespace data stored directly in the object/class
```

#### Q7. What is the difference between `is` and `==`?

```text
is
    → identity

==
    → equality/value
```

#### Q8. What is `getattr()` used for?

It dynamically retrieves an attribute.

```python
getattr(obj, "name")
```

#### Q9. What is `setattr()`?

It dynamically creates or modifies an attribute.

```python
setattr(obj, "name", "Nitin")
```

#### Q10. What is MRO?

MRO stands for Method Resolution Order.

It defines the order in which Python searches classes for attributes and methods.

It can be inspected using:

```python
Class.mro()
```

or:

```python
Class.__mro__
```

### Advanced

#### Q11. Why can `obj.__dict__` fail?

Because not every object has a `__dict__`. For example, classes using `__slots__` may not have one.

#### Q12. What is `callable()`?

It checks whether an object can be called using:

```python
()
```

#### Q13. How can you inspect a function's parameters?

Using:

```python
import inspect

inspect.signature(function)
```

#### Q14. How can you dynamically call a method?

```python
method = getattr(obj, method_name)
result = method()
```

#### Q15. How can you inspect all members of an object?

```python
import inspect

inspect.getmembers(obj)
```

## 50. Interview Coding Example

What will this print?

```python
class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(type(dog) == Dog)
print(type(dog) == Animal)

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

print(issubclass(Dog, Animal))
```

Expected:

```text
True
False
True
True
True
```

The important concept is:

```text
Dog is exactly the type of dog.

Dog is also an Animal because Dog inherits from Animal.
```

## 51. Interview Coding Example — Dynamic Attribute

```python
class User:

    def __init__(self):
        self.name = "Nitin"


user = User()

field = "name"

print(getattr(user, field))
```

Output:

```text
Nitin
```

The important idea is that the attribute name is dynamic.

## 52. Interview Coding Example — `is` vs `==`

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)

print(a == c)
print(a is c)
```

Output:

```text
True
False
True
True
```

Reason:

```text
a and b
→ same values
→ different objects

a and c
→ same values
→ same object
```

## 53. Object Introspection and Your Previous OOP Topics

Object introspection connects several concepts you've already learned.

```text
Classes
   ↓
Objects
   ↓
Attributes
   ↓
Methods
   ↓
Inheritance
   ↓
MRO
   ↓
Introspection
```

Examples:

### Classes and objects

```python
type(obj)
obj.__class__
```

### Encapsulation

```python
obj.__dict__
```

can help you inspect stored state.

### Inheritance

```python
isinstance()
issubclass()
```

### MRO

```python
Class.mro()
Class.__mro__
```

### Dynamic attributes

```python
getattr()
setattr()
hasattr()
delattr()
```

This makes introspection a practical tool for understanding the OOP concepts you already learned.

## 54. When Should You Use Introspection?

Use introspection when:

- Debugging unfamiliar objects
- Building dynamic systems
- Working with plugins
- Inspecting library objects
- Writing generic utilities
- Inspecting function signatures
- Building framework-like functionality
- Dynamically selecting methods
- Understanding inheritance
- Exploring an unfamiliar Python API

Don't use it unnecessarily when normal Python syntax is clearer.

## 55. Quick Revision

Before moving to the next lecture, you should be comfortable with:

```text
type()
    ↓
Exact type

isinstance()
    ↓
Object belongs to class hierarchy

issubclass()
    ↓
Class inheritance

id()
    ↓
Object identity

is
    ↓
Same object?

dir()
    ↓
Available names

help()
    ↓
Documentation

hasattr()
    ↓
Does attribute exist?

getattr()
    ↓
Get dynamically

setattr()
    ↓
Set dynamically

delattr()
    ↓
Delete dynamically

vars()
    ↓
Namespace dictionary

__dict__
    ↓
Object/class namespace

__class__
    ↓
Object's class

__bases__
    ↓
Direct parent classes

__mro__
    ↓
Method Resolution Order

callable()
    ↓
Can this object be called?

inspect
    ↓
Deeper introspection
```

## 56. Final Mental Model

Think of introspection as a **runtime investigation toolkit**.

```text
                    Python Object
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
        Type           State          Behavior
          │              │              │
       type()         vars()          dir()
       isinstance()   __dict__        getattr()
       issubclass()                    callable()
          │
          ↓
      Inheritance
          │
       mro()
       __mro__
       __bases__

          ↓
     Deep Inspection
          │
       inspect
```

The key idea is:

> **Python lets you inspect and interact with objects dynamically at runtime.**

## 57. Lecture 10 Checklist

- [ ] Understand object introspection
- [ ] Understand `type()`
- [ ] Understand `isinstance()`
- [ ] Understand `issubclass()`
- [ ] Understand `id()`
- [ ] Understand `is` vs `==`
- [ ] Understand `dir()`
- [ ] Understand `help()`
- [ ] Understand `hasattr()`
- [ ] Understand `getattr()`
- [ ] Understand `setattr()`
- [ ] Understand `delattr()`
- [ ] Understand `vars()`
- [ ] Understand `__dict__`
- [ ] Understand `__class__`
- [ ] Understand `__name__`
- [ ] Understand `__module__`
- [ ] Understand `__bases__`
- [ ] Understand MRO introspection
- [ ] Understand `callable()`
- [ ] Know basic `inspect` usage
- [ ] Understand `inspect.signature()`
- [ ] Understand `inspect.getmembers()`
- [ ] Know when introspection is useful
- [ ] Know the limitations of `dir()` and `__dict__`
- [ ] Practice dynamic attribute access

## Next Lecture

**Lecture 11 → Special / Dunder Methods**

Topics:

- What are dunder methods?
- `__str__`
- `__repr__`
- `__len__`
- `__eq__`
- `__lt__`
- `__add__`
- `__contains__`
- `__getitem__`
- `__setitem__`
- `__iter__`
- `__next__`
- `__call__`
- `__enter__`
- `__exit__`
- Operator overloading
- Python's data model
- Practical custom classes
- Interview questions