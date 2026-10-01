# Lecture 1 — What is Functional Programming?

Functional Programming (FP) is a programming style where we try to build programs by combining **functions**, minimizing unnecessary state changes and side effects.

Python is not a purely functional language, but it provides many powerful functional programming features such as:

- First-class functions
- Higher-order functions
- Pure functions
- `map()`
- `filter()`
- `reduce()`
- `zip()`
- `lambda`
- Comprehensions
- `sorted()` with key functions
- `any()` and `all()`
- `iter()` and `next()`
- Generators
- Closures
- `functools`
- `operator`

The goal of this chapter is not to turn Python into a purely functional language.

The goal is to understand **when and how functional programming techniques make Python code cleaner, reusable, and easier to reason about**.

# 1. What is Functional Programming?

Functional Programming is a programming paradigm where computation is expressed primarily through **functions**.

A simple mental model:

```text
Input
  ↓
Function
  ↓
Output
```

For example:

```python
def square(x):
    return x * x
```

```text
5
 ↓
square()
 ↓
25
```

Instead of thinking primarily about:

```text
Change this variable
Change that variable
Update this state
Run this loop
```

functional programming encourages us to think:

```text
Take data
   ↓
Transform data
   ↓
Transform again
   ↓
Produce result
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

result = [x * 2 for x in numbers]

print(result)
```

Output:

```text
[2, 4, 6, 8, 10]
```

The focus is on the **transformation of data**.

# 2. Programming Paradigms

A programming paradigm is a style or approach to solving programming problems.

Common paradigms include:

```text
Programming
│
├── Imperative
│
├── Object-Oriented
│
├── Functional
│
└── Declarative
```

Python supports multiple paradigms.

This is one of Python's strengths.

## Imperative Programming

Imperative programming focuses on **how** something should happen.

Example:

```python
numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    result.append(number * 2)

print(result)
```

We explicitly tell Python:

```text
Create result
↓
Loop through numbers
↓
Take each number
↓
Multiply it
↓
Append it
```

## Functional Style

A functional-style solution can express the same transformation more directly:

```python
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

Here the focus is:

```text
numbers
   ↓
transform each value
   ↓
result
```

Both approaches are valid Python.

Functional programming gives us another way to think about the problem.

# 3. Functional Programming in Python

Python is a **multi-paradigm language**.

You can write:

```python
# Procedural
for x in numbers:
    ...
```

You can write:

```python
# Object-oriented
class Student:
    ...
```

You can also write:

```python
# Functional style
result = list(map(function, numbers))
```

You do not need to choose only one paradigm.

In real Python applications, these styles are often combined.

For example:

```text
Class
  ↓
contains business logic
  ↓
uses functions
  ↓
uses comprehensions
  ↓
uses map/filter
  ↓
uses generators
```

The important skill is knowing **which style makes the code clearer**.

# 4. Why Learn Functional Programming?

Functional programming is important for Python because it helps with:

### 1. Data Transformation

Very common in:

- Backend development
- Data processing
- AI/ML
- ETL pipelines
- APIs
- DSA
- Automation

Example:

```text
Raw Data
   ↓
Filter
   ↓
Transform
   ↓
Aggregate
   ↓
Result
```

### 2. Reusable Logic

Functions can be passed around and reused.

### 3. Reduced Side Effects

Functions that don't unexpectedly modify external state are easier to understand.

### 4. Cleaner Data Processing

Functional tools can express operations such as:

```text
map
filter
reduce
```

very naturally.

### 5. Better Reasoning

Pure functions are often easier to test because:

```text
same input
   ↓
same output
```

### 6. Important Python Features

Many Python features are closely related to functional programming:

```text
Functions
Lambda
map()
filter()
reduce()
zip()
sorted()
any()
all()
Generators
Closures
Decorators
functools
```

# 5. Functions as First-Class Objects

One of the most important ideas in Python functional programming is:

> Functions are objects.

This means a function can be:

- Assigned to a variable
- Passed to another function
- Returned from another function
- Stored in a list
- Stored in a dictionary

Example:

```python
def greet():
    return "Hello"


message = greet

print(message())
```

Output:

```text
Hello
```

Here:

```python
message = greet
```

does not call the function.

It stores a reference to the function.

Compare:

```python
message = greet
```

with:

```python
message = greet()
```

The first stores the function.

The second executes the function and stores its return value.

# 6. Function References

Consider:

```python
def add(a, b):
    return a + b
```

We can do:

```python
operation = add

print(operation(10, 20))
```

Output:

```text
30
```

The function can be treated like another Python object.

Mental model:

```text
add
 ↓
function object
 ↓
can be stored
 ↓
can be passed
 ↓
can be returned
```

This concept is fundamental to:

- `map()`
- `filter()`
- `sorted()`
- callbacks
- decorators
- higher-order functions

# 7. Passing Functions as Arguments

Because functions are objects, we can pass them to another function.

Example:

```python
def square(x):
    return x * x


def apply_operation(value, operation):
    return operation(value)


print(apply_operation(5, square))
```

Output:

```text
25
```

Here:

```text
square
   ↓
passed to
   ↓
apply_operation()
   ↓
operation(value)
```

This is one of the foundations of functional programming.

# 8. Higher-Order Functions

A **higher-order function** is a function that does at least one of these:

1. Takes another function as an argument
2. Returns another function

Example:

```python
def apply_operation(value, operation):
    return operation(value)
```

`apply_operation()` is a higher-order function because it accepts a function.

Another example:

```python
def create_multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply
```

Usage:

```python
double = create_multiplier(2)

print(double(10))
```

Output:

```text
20
```

Here:

```text
create_multiplier()
       ↓
returns a function
       ↓
double()
```

Higher-order functions are extremely important for understanding:

- `map()`
- `filter()`
- decorators
- callbacks
- closures

# 9. Functions vs Higher-Order Functions

Normal function:

```python
def square(x):
    return x * x
```

Higher-order function:

```python
def apply_operation(value, operation):
    return operation(value)
```

The important difference:

```text
Normal function
    ↓
works with data

Higher-order function
    ↓
works with functions
```

# 10. Pure Functions

A pure function is a function that:

1. Produces the same output for the same input.
2. Does not produce observable side effects.

Example:

```python
def add(a, b):
    return a + b
```

For:

```python
add(10, 20)
```

the result will always be:

```text
30
```

The function does not modify external state.

# 11. Pure Function Example

```python
def square(number):
    return number * number
```

This is pure.

```python
print(square(5))
print(square(5))
print(square(5))
```

Every call produces:

```text
25
25
25
```

The result depends only on the input.

Mental model:

```text
Input
  ↓
Pure Function
  ↓
Output

No external state
No unexpected modification
```

# 12. Impure Functions

Consider:

```python
total = 0


def add_to_total(value):
    global total
    total += value
```

This function modifies external state.

Therefore, it is not pure.

Calling:

```python
add_to_total(10)
```

changes something outside the function itself.

The behavior depends on external state.

# 13. Pure vs Impure Functions

### Pure

```python
def multiply(a, b):
    return a * b
```

### Impure

```python
total = 0


def update_total(value):
    global total
    total += value
```

Comparison:

```text
Pure Function
-------------------------
Same input → same output
No external state mutation
Easy to test
Easy to reason about
```

```text
Impure Function
-------------------------
May depend on external state
May modify external state
Can have side effects
Can be harder to test
```

# 14. Side Effects

A side effect occurs when a function does something beyond simply producing a return value.

Examples include:

```python
print()
```

```python
file.write(...)
```

```python
database.insert(...)
```

```python
global_variable += 1
```

```python
list.append(...)
```

Not every side effect is bad.

Real applications need side effects.

For example:

```text
API request
Database update
File write
Logging
Sending email
```

The goal is not:

```text
"Never use side effects."
```

The practical goal is:

```text
Keep side effects controlled and predictable.
```

# 15. Functional Programming and Immutability

Functional programming often prefers avoiding unnecessary mutation.

Consider:

```python
numbers = [1, 2, 3]

numbers.append(4)
```

The original list was modified.

An alternative approach is to create a new result:

```python
numbers = [1, 2, 3]

new_numbers = numbers + [4]
```

Now:

```text
numbers
→ [1, 2, 3]

new_numbers
→ [1, 2, 3, 4]
```

Python is **not immutable by default**.

Lists, dictionaries, and sets are mutable.

Functional programming is therefore a style you apply when useful, not a restriction imposed by Python.

# 16. Mutation vs Transformation

Mutation:

```python
numbers = [1, 2, 3]

numbers.append(4)
```

The existing object changes.

Transformation:

```python
numbers = [1, 2, 3]

new_numbers = numbers + [4]
```

A new result is produced.

In functional-style programming, we often prefer:

```text
Input
 ↓
Transformation
 ↓
New Output
```

rather than repeatedly modifying shared state.

# 17. Declarative Thinking

Functional programming often encourages a more declarative style.

Imperative:

```python
numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    if number % 2 == 0:
        result.append(number)
```

The code explains **how** to perform the operation.

A more declarative approach:

```python
result = [number for number in numbers if number % 2 == 0]
```

This focuses more directly on:

```text
"Give me the even numbers."
```

Python supports both styles.

# 18. Functional Programming Is Not Just map/filter/reduce

A common misconception is:

```text
Functional Programming
=
map() + filter() + reduce()
```

That is incomplete.

Functional programming also involves concepts such as:

```text
First-class functions
Higher-order functions
Pure functions
Side effects
Immutability
Function composition
Closures
Lazy evaluation
Iterators
Generators
Declarative thinking
```

Python provides tools for many of these concepts.

# 19. Function Composition

Function composition means combining functions so that the output of one becomes the input of another.

Suppose:

```python
def double(x):
    return x * 2


def add_ten(x):
    return x + 10
```

We can conceptually compose them:

```text
Input
  ↓
double()
  ↓
add_ten()
  ↓
Output
```

For example:

```python
value = 5

result = add_ten(double(value))

print(result)
```

Output:

```text
20
```

Because:

```text
5
 ↓
double → 10
 ↓
add_ten → 20
```

Python does not have a built-in general-purpose `compose()` function, but function composition can be implemented when useful.

# 20. A Simple Composition Function

```python
def compose(function1, function2):

    def composed(value):
        return function2(function1(value))

    return composed
```

Usage:

```python
def double(x):
    return x * 2


def add_ten(x):
    return x + 10


process = compose(double, add_ten)

print(process(5))
```

Output:

```text
20
```

This example combines several important ideas:

```text
Functions as objects
        +
Higher-order functions
        +
Functions returning functions
        +
Function composition
```

# 21. `map()`, `filter()`, `reduce()`

These are major Python functional programming tools.

They will be covered individually in upcoming lectures.

```text
Lecture 1
Functional Programming Fundamentals
        ↓
Lecture 2
Pure Functions
        ↓
Lecture 3
map()
        ↓
Lecture 4
filter()
        ↓
Lecture 5
zip()
        ↓
Lecture 6
reduce()
        ↓
Lecture 7
Exercises
        ↓
Lecture 8
Lambda Expressions
        ↓
Lecture 9
Lambda Exercises
        ↓
Lecture 10
List Comprehensions
        ↓
Lecture 11
Set & Dictionary Comprehensions
        ↓
Lecture 12
Comprehension Exercises
```

# 22. Functional Programming with Python Built-ins

Python already provides many functions that support functional-style programming.

Important ones:

```python
map()
filter()
sorted()
min()
max()
sum()
any()
all()
zip()
enumerate()
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

result = sorted(numbers, reverse=True)

print(result)
```

`sorted()` can also receive a function through its `key` parameter.

Example:

```python
students = [
    ("Nitin", 85),
    ("Rahul", 92),
    ("Aman", 78)
]

result = sorted(students, key=lambda student: student[1])

print(result)
```

This demonstrates that functional concepts are used throughout normal Python programming.

# 23. `any()` and `all()`

These are useful functional-style built-ins.

## `any()`

Returns `True` if at least one element is truthy.

```python
numbers = [1, 3, 5, 8]

result = any(number % 2 == 0 for number in numbers)

print(result)
```

Output:

```text
True
```

Because `8` is even.

## `all()`

Returns `True` if every element is truthy.

```python
numbers = [2, 4, 6, 8]

result = all(number % 2 == 0 for number in numbers)

print(result)
```

Output:

```text
True
```

These will become especially useful when working with iterators and generators.

# 24. Functional Programming and DSA

Functional programming techniques can also appear in DSA.

Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]
```

Filtering:

```python
even_numbers = [x for x in numbers if x % 2 == 0]
```

Aggregation:

```python
total = sum(numbers)
```

Checking conditions:

```python
has_even = any(x % 2 == 0 for x in numbers)
```

Checking all conditions:

```python
all_positive = all(x > 0 for x in numbers)
```

The important skill is not using functional syntax everywhere.

The important skill is recognizing:

```text
Transform
Filter
Aggregate
Check
Combine
```

# 25. Functional Programming and Backend Development

Functional programming concepts are useful in backend development.

Example API data:

```python
users = [
    {"name": "A", "active": True},
    {"name": "B", "active": False},
    {"name": "C", "active": True}
]
```

We may need:

```text
Filter active users
        ↓
Transform user data
        ↓
Return required fields
```

Functional-style operations can make these transformations concise.

These concepts are also useful when processing:

- API responses
- Database results
- JSON data
- Logs
- Configuration data
- CSV records
- AI/ML datasets

# 26. Functional Programming and AI/Data Processing

Functional-style transformations are particularly useful when processing collections of data.

Typical pipeline:

```text
Raw Data
   ↓
Filter
   ↓
Transform
   ↓
Clean
   ↓
Aggregate
   ↓
Result
```

For example:

```text
Transactions
    ↓
Remove invalid transactions
    ↓
Extract amounts
    ↓
Calculate total
```

This way of thinking becomes useful when working with:

- Pandas
- NumPy
- Data pipelines
- ML preprocessing
- ETL
- AI applications

# 27. When Functional Style Is Useful

Functional style is particularly useful when:

### Data needs transformation

```text
input → transformation → output
```

### Logic is reusable

```python
def normalize(value):
    ...
```

### You want predictable functions

```text
same input → same output
```

### You are processing collections

```text
map
filter
reduce
comprehension
```

### You want to reduce unnecessary state changes

```text
less mutation
```

# 28. When Not to Force Functional Programming

Do not use functional programming just because it looks advanced.

For example:

```python
result = list(map(lambda x: x * 2, numbers))
```

may be less readable than:

```python
result = [x * 2 for x in numbers]
```

In Python, readability matters.

A useful rule:

```text
Choose the clearest solution,
not the most "functional" solution.
```

# 29. Functional Style vs Pythonic Style

Functional programming and Pythonic programming are not exactly the same thing.

For example:

```python
result = list(map(lambda x: x * 2, numbers))
```

is functional.

But:

```python
result = [x * 2 for x in numbers]
```

is often considered more readable and idiomatic Python.

Therefore:

```text
Functional programming
        ↓
A tool/style

Pythonic programming
        ↓
Writing code that fits Python's strengths
```

Good Python developers know both.

# 30. Common Mistakes

## Mistake 1 — Thinking FP Means No Loops

Functional programming does not mean loops are forbidden in Python.

Loops are still useful.

## Mistake 2 — Using `map()` Everywhere

Don't replace every simple loop with `map()`.

Choose the clearer approach.

## Mistake 3 — Confusing Function and Function Call

```python
process
```

means the function object.

```python
process()
```

calls the function.

## Mistake 4 — Thinking Pure Functions Cannot Use Python Objects

A function can accept objects and still be pure if its result depends only on its inputs and it does not create observable side effects.

## Mistake 5 — Thinking Side Effects Are Always Bad

Backend applications need side effects.

The goal is to control them, not eliminate them completely.

## Mistake 6 — Thinking Python Is a Pure Functional Language

Python supports functional programming but is not a purely functional language.

# 31. Important Terminology

### First-Class Function

A function that can be treated like a normal object.

```text
Store
Pass
Return
```

### Higher-Order Function

A function that accepts or returns another function.

### Pure Function

A function whose result depends only on its inputs and which has no observable side effects.

### Side Effect

An observable interaction with state or the outside world beyond returning a value.

### Immutability

An object cannot be changed after creation.

Python supports immutable types but is not an immutable language.

### Function Composition

Combining functions so that the output of one becomes the input of another.

### Declarative Style

Describing what result is wanted rather than explicitly describing every step required to produce it.

# 32. Interview Questions

### Basic

1. What is functional programming?
2. Is Python a functional programming language?
3. What are the main characteristics of functional programming?
4. What is a first-class function?
5. What is a higher-order function?
6. What is a pure function?
7. What is a side effect?
8. What is immutability?
9. What is function composition?

### Python

10. How are functions treated as objects in Python?
11. Can a function be passed as an argument?
12. Can a function return another function?
13. What is the difference between a function and a function call?
14. What is the purpose of `map()`?
15. What is the purpose of `filter()`?
16. What is the purpose of `reduce()`?
17. Why might a list comprehension be preferred over `map()`?
18. What are `any()` and `all()` used for?

### Practical

19. How would you identify whether a function is pure?
20. Give an example of a side effect.
21. How can you reduce unnecessary mutation in Python?
22. Where is functional programming useful in backend development?
23. Where is functional programming useful in data processing?
24. When should you avoid using functional-style code?

# 33. Quick Revision

Remember these core ideas:

```text
Functional Programming
        ↓
Functions are important building blocks
        ↓
Functions are first-class objects
        ↓
Functions can be passed around
        ↓
Higher-order functions can accept/return functions
        ↓
Pure functions are predictable
        ↓
Avoid unnecessary side effects
        ↓
Prefer transformations over unnecessary mutation
        ↓
Compose operations when useful
```

## Core Python Tools

```text
map()
filter()
reduce()
zip()
lambda
comprehensions
sorted()
any()
all()
```

## Core Concepts

```text
First-Class Functions
Higher-Order Functions
Pure Functions
Side Effects
Immutability
Function Composition
Declarative Thinking
```

# 34. Mental Model

When processing data, think:

```text
                DATA
                  ↓
             FILTER
                  ↓
            TRANSFORM
                  ↓
             TRANSFORM
                  ↓
             AGGREGATE
                  ↓
               RESULT
```

And when designing functions:

```text
Input
  ↓
Function
  ↓
Output
```

Prefer functions where:

```text
Input
  ↓
Predictable Logic
  ↓
Output
```

rather than functions that unexpectedly modify unrelated state.

# 35. What I Need to Remember

The most important lessons from this lecture are:

```text
1. Python supports multiple programming paradigms.

2. Functional programming focuses heavily on functions
   and transformations.

3. Functions are first-class objects in Python.

4. Functions can be passed as arguments.

5. Functions can return other functions.

6. Higher-order functions work with other functions.

7. Pure functions are easier to reason about and test.

8. Side effects should be controlled, not blindly eliminated.

9. Functional programming often favors transformation
   over unnecessary mutation.

10. Function composition allows small functions to be
    combined into larger operations.

11. map(), filter(), reduce(), zip(), lambda and
    comprehensions are important tools, but they are
    not the entire concept of functional programming.

12. In Python, readability is more important than
    forcing functional syntax everywhere.
```

# Lecture 1 Checklist

```text
[ ] Understand functional programming
[ ] Understand programming paradigms
[ ] Understand Python's multi-paradigm nature
[ ] Understand first-class functions
[ ] Understand function references
[ ] Understand passing functions as arguments
[ ] Understand higher-order functions
[ ] Understand pure functions
[ ] Understand impure functions
[ ] Understand side effects
[ ] Understand immutability
[ ] Understand mutation vs transformation
[ ] Understand declarative thinking
[ ] Understand function composition
[ ] Understand functional-style Python
[ ] Know where functional programming is useful
[ ] Know when NOT to force functional programming
```

# Next Lecture

## Lecture 2 — Pure Functions

Next, go deeper into:

```text
Pure Functions
     ↓
Deterministic Functions
     ↓
Side Effects
     ↓
State
     ↓
Mutation
     ↓
Immutability
     ↓
Referential Transparency
     ↓
Practical Python Examples
     ↓
Exercises
```