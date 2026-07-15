# 📚 Stack — Complete DSA Notes in Python

A **Stack** is one of the most important linear data structures in Data Structures and Algorithms.

A Stack follows the principle:

```text
LIFO
```

which means:

```text
Last In, First Out
```

The element inserted last is the first element removed.

A simple real-life example is a stack of plates:

```text
        ┌───────┐
Top →   │ Plate 4 │  ← Removed First
        ├───────┤
        │ Plate 3 │
        ├───────┤
        │ Plate 2 │
        ├───────┤
        │ Plate 1 │  ← Inserted First
        └───────┘
```

If we remove a plate, we normally remove it from the top.

Similarly, in a Stack:

```text
Insertion → Top

Deletion  → Top
```

Understanding Stack is mainly about understanding:

* LIFO behavior
* Push
* Pop
* Peek / Top
* Empty Stack
* Stack implementation
* Call Stack
* Recursion and Stack
* Expression processing
* Parentheses matching
* Monotonic Stack
* Previous and Next Greater/Smaller patterns
* Stack-based simulation
* Important edge cases
* Time and space complexity

---

# 1. What is a Stack?

A Stack is a linear data structure where insertion and deletion happen from only one end.

That end is called:

```text
TOP
```

Example:

```text
Push 10

TOP
 ↓
10
```

Then:

```text
Push 20
```

Now:

```text
TOP
 ↓
20
10
```

Then:

```text
Push 30
```

Now:

```text
TOP
 ↓
30
20
10
```

If we perform:

```text
pop()
```

the element removed is:

```text
30
```

because `30` was inserted last.

After removal:

```text
TOP
 ↓
20
10
```

Therefore:

```text
Last Inserted
      ↓
First Removed
```

This is why Stack is called:

```text
LIFO
```

---

# 2. Stack Terminology

The most important Stack terms are:

## Push

Add an element to the top of the Stack.

```text
Before:

TOP
 ↓
20
10


Push 30


After:

TOP
 ↓
30
20
10
```

---

## Pop

Remove the top element.

```text
Before:

TOP
 ↓
30
20
10


Pop


After:

TOP
 ↓
20
10
```

The removed element is:

```text
30
```

---

## Peek / Top

Return the top element without removing it.

```text
TOP
 ↓
30
20
10
```

Peek returns:

```text
30
```

The Stack remains unchanged.

---

## isEmpty

Checks whether the Stack contains any elements.

```text
[]
```

means:

```text
Stack is empty
```

---

## Size

Returns the number of elements currently stored in the Stack.

Example:

```text
Stack:

30
20
10
```

Size:

```text
3
```

---

# 3. Stack Operations

The main Stack operations are:

| Operation          | Meaning                      |
| ------------------ | ---------------------------- |
| `push()`           | Insert an element            |
| `pop()`            | Remove the top element       |
| `peek()` / `top()` | View the top element         |
| `isEmpty()`        | Check whether Stack is empty |
| `size()`           | Number of elements           |

For a good Stack implementation:

| Operation | Time Complexity |
| --------- | --------------: |
| Push      |            O(1) |
| Pop       |            O(1) |
| Peek      |            O(1) |
| isEmpty   |            O(1) |
| Size      |            O(1) |

---

# 4. Stack Representation

Conceptually, a Stack can be shown vertically:

```text
       TOP
        ↓
    ┌───────┐
    │  40   │
    ├───────┤
    │  30   │
    ├───────┤
    │  20   │
    ├───────┤
    │  10   │
    └───────┘
```

Or horizontally:

```text
[10, 20, 30, 40]
                 ↑
                TOP
```

In Python, the second representation is very common when using a list.

---

# 5. Implementing Stack Using Python List

Python does not require us to create a Stack class for basic Stack operations.

We can use:

```python
stack = []
```

Push:

```python
stack.append(10)
stack.append(20)
stack.append(30)
```

Now:

```python
stack
```

contains:

```text
[10, 20, 30]
```

The top is:

```text
30
```

---

# 6. Push Operation in Python

Python's:

```python
append()
```

works as Stack push.

```python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)
```

Result:

```text
[10, 20, 30]
```

Top:

```text
30
```

Time Complexity:

```text
O(1) amortized
```

The word **amortized** means that most append operations are O(1), although occasionally Python may need to resize the internal dynamic array.

For DSA complexity analysis, we normally treat:

```python
stack.append(x)
```

as:

```text
O(1)
```

---

# 7. Pop Operation in Python

Python provides:

```python
stack.pop()
```

Example:

```python
stack = [10, 20, 30]

value = stack.pop()
```

Now:

```text
value = 30

stack = [10, 20]
```

Time Complexity:

```text
O(1)
```

Important:

```python
stack.pop()
```

removes from the end.

Avoid using:

```python
stack.pop(0)
```

for Stack operations.

Removing from index `0` requires shifting remaining elements.

Time Complexity:

```text
O(n)
```

---

# 8. Peek / Top Operation

Python lists do not have a built-in `peek()` method.

We use:

```python
stack[-1]
```

Example:

```python
stack = [10, 20, 30]

top = stack[-1]
```

Result:

```text
30
```

The Stack remains:

```text
[10, 20, 30]
```

Time Complexity:

```text
O(1)
```

Always check that the Stack is not empty before accessing:

```python
stack[-1]
```

---

# 9. Checking Whether Stack is Empty

Pythonic way:

```python
if not stack:
    print("Stack is empty")
```

Or:

```python
if len(stack) == 0:
    print("Stack is empty")
```

Preferred:

```python
if not stack:
```

To check that it contains elements:

```python
if stack:
```

---

# 10. Stack Size

Use:

```python
len(stack)
```

Example:

```python
stack = [10, 20, 30]

print(len(stack))
```

Output:

```text
3
```

Time Complexity:

```text
O(1)
```

Python stores the list's size internally, so `len()` does not traverse the entire list.

---

# 11. Complete Stack Implementation Using Python List

```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return None

        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None

        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
```

Usage:

```python
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())

stack.pop()

print(stack.peek())
```

---

# 12. Stack Underflow

Stack Underflow occurs when we try to remove or access an element from an empty Stack.

Example:

```python
stack = []

stack.pop()
```

Python raises:

```text
IndexError
```

Similarly:

```python
stack[-1]
```

on an empty list also raises an error.

Therefore, always check:

```python
if stack:
```

before accessing or removing the top.

---

# 13. Stack Overflow

In a fixed-size Stack, Stack Overflow means trying to insert an element when the Stack is already full.

Example:

```text
Maximum Capacity = 3

Stack:

30
20
10
```

Trying to push another element causes:

```text
Stack Overflow
```

Python lists are dynamic, so this type of Stack overflow normally does not happen when using a Python list.

However, the term **Stack Overflow** is also commonly associated with the function call stack.

Too much recursion can exceed Python's recursion depth.

---

# 14. Stack Using a Fixed-Size Array Concept

In languages where we manually manage Stack size, we maintain:

```text
top = -1
```

Initially:

```text
Stack is empty

top = -1
```

After pushing the first element:

```text
top = 0
```

After another:

```text
top = 1
```

General idea:

```text
Push:

top = top + 1
arr[top] = value
```

Pop:

```text
value = arr[top]
top = top - 1
```

Even though Python lists make this easier, understanding the `top` index is useful for understanding how Stack works internally.

---

# 15. Stack Using Linked List

A Stack can also be implemented using a Linked List.

The head acts as:

```text
TOP
```

Example:

```text
TOP
 ↓
30 → 20 → 10 → None
```

Push means inserting at the head.

Pop means deleting from the head.

Both operations take:

```text
O(1)
```

Python implementation:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node

        self._size += 1

    def pop(self):
        if self.top is None:
            return None

        value = self.top.data

        self.top = self.top.next

        self._size -= 1

        return value

    def peek(self):
        if self.top is None:
            return None

        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size
```

---

# 16. Why Use the Head as Stack Top?

In a Singly Linked List:

```text
10 → 20 → 30 → None
```

Insertion at the beginning:

```text
O(1)
```

Deletion at the beginning:

```text
O(1)
```

Therefore, using the head as the Stack top gives efficient push and pop operations.

If we used the tail without a previous pointer, removing the last node would require traversal.

That would take:

```text
O(n)
```

---

# 17. Python List vs Linked List Stack

| Feature              | Python List    | Linked List |
| -------------------- | -------------- | ----------- |
| Push                 | O(1) amortized | O(1)        |
| Pop                  | O(1)           | O(1)        |
| Peek                 | O(1)           | O(1)        |
| Implementation       | Simple         | More code   |
| Extra Node Reference | No             | Yes         |
| Dynamic Size         | Yes            | Yes         |

For most Python DSA problems:

```python
stack = []
```

is the preferred Stack implementation.

---

# 18. Stack and Recursion

Recursion internally uses a Stack called the:

```text
Call Stack
```

Consider:

```python
def solve(n):
    if n == 0:
        return

    solve(n - 1)
```

Call:

```python
solve(3)
```

Function calls are stored like:

```text
TOP

solve(0)
solve(1)
solve(2)
solve(3)
```

When the base case returns, functions are removed in reverse order:

```text
solve(0) returns
solve(1) returns
solve(2) returns
solve(3) returns
```

This is exactly:

```text
LIFO
```

The last function call added is the first one completed.

---

# 19. Stack Frames

Every function call creates a **stack frame**.

A stack frame may contain:

* Function parameters
* Local variables
* Return information
* Current execution state

Example:

```python
def calculate(n):
    x = n * 2
    calculate(n - 1)
```

Every recursive call gets its own separate:

```text
n
x
```

values.

These frames remain on the call stack until their function calls return.

---

# 20. Recursion to Iterative Stack Thinking

Many recursive algorithms can be converted into iterative algorithms using an explicit Stack.

Recursion:

```text
System Call Stack
```

Iterative approach:

```text
Our Own Stack
```

General idea:

```python
stack = [initial_state]

while stack:
    current = stack.pop()

    # process current

    # push future states
```

This is especially important in:

* Tree traversal
* Graph DFS
* Backtracking simulation

---

# 21. Why Stack is Useful

Stack is useful whenever we need to remember something and process the most recently remembered item first.

Think:

```text
Need to remember something
        ↓
Most recent thing should be processed first
        ↓
STACK
```

Examples include:

* Function calls
* Undo operations
* Browser history behavior
* Expression evaluation
* Parentheses matching
* DFS
* Backtracking
* Reversing order
* Monotonic Stack

---

# 22. Reversing Order Using Stack

Because Stack follows LIFO, it naturally reverses order.

Suppose:

```text
Input:

1 2 3 4
```

Push everything:

```text
TOP
 ↓
4
3
2
1
```

Pop everything:

```text
4 3 2 1
```

Therefore:

```text
Push in one order
        ↓
Pop in reverse order
```

This property appears in many Stack-based algorithms.

---

# 23. Parentheses Matching Pattern

Stacks are commonly used when elements must be matched in nested order.

Example:

```text
{ [ ( ) ] }
```

Opening brackets are pushed.

```text
{
[
(
```

When a closing bracket appears:

```text
)
```

it should match the most recent unmatched opening bracket:

```text
(
```

This is naturally LIFO.

General pattern:

```text
Opening Symbol
      ↓
Push


Closing Symbol
      ↓
Check Stack Top
      ↓
Match
      ↓
Pop
```

Important edge cases:

```text
Closing bracket but Stack is empty
        ↓
Invalid


Top does not match closing bracket
        ↓
Invalid


Stack still contains elements at end
        ↓
Invalid
```

---

# 24. Matching Pairs Using a Dictionary

Python allows us to store matching relationships.

```python
pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}
```

Then:

```python
if stack[-1] == pairs[ch]:
```

checks whether the top opening bracket matches the current closing bracket.

This is a useful combination:

```text
Stack
+
Hash Map
```

---

# 25. Nested Structure Pattern

Whenever a problem contains nested structures such as:

```text
(...)
[...]

{...}

a(b(c)d)e
```

a Stack may be useful.

The reason is:

```text
The most recently opened structure
must usually be closed first.
```

That is exactly:

```text
LIFO
```

---

# 26. Expression Basics

Stacks are important in mathematical expression processing.

There are three common expression formats:

```text
Infix
Prefix
Postfix
```

---

# 27. Infix Expression

The operator appears between operands.

Example:

```text
A + B
```

Another example:

```text
A + B * C
```

This is the normal mathematical format humans use.

---

# 28. Prefix Expression

The operator appears before operands.

```text
+ A B
```

Example:

```text
A + B
```

becomes:

```text
+ A B
```

Prefix is also called:

```text
Polish Notation
```

---

# 29. Postfix Expression

The operator appears after operands.

```text
A B +
```

Example:

```text
A + B
```

becomes:

```text
A B +
```

Postfix is also called:

```text
Reverse Polish Notation
```

---

# 30. Why Prefix and Postfix Are Useful

Consider:

```text
A + B * C
```

In infix form, we need to understand operator precedence.

Multiplication happens first.

In postfix:

```text
A B C * +
```

The evaluation order is already encoded.

No parentheses are required to determine precedence.

This makes Stack-based evaluation straightforward.

---

# 31. Operator Precedence

Common precedence:

```text
Highest

^       Exponent

* /     Multiplication / Division

+ -     Addition / Subtraction

Lowest
```

Parentheses can override normal precedence.

Example:

```text
(A + B) * C
```

Here addition happens before multiplication.

---

# 32. Associativity

When operators have the same precedence, associativity determines evaluation direction.

Most arithmetic operators are:

```text
Left Associative
```

Examples:

```text
+
-
*
/
```

Exponentiation is commonly:

```text
Right Associative
```

This matters when converting expressions using a Stack.

---

# 33. Postfix Evaluation Pattern

For postfix expressions, scan:

```text
Left → Right
```

If the token is an operand:

```text
Push
```

If the token is an operator:

```text
Pop two operands
Apply operator
Push result
```

Important:

If we pop:

```python
b = stack.pop()
a = stack.pop()
```

then calculate:

```python
a operator b
```

The order matters for:

```text
-
/
```

because:

```text
a - b
```

is not the same as:

```text
b - a
```

---

# 34. Prefix Evaluation Pattern

For prefix expressions, scan:

```text
Right → Left
```

Operand:

```text
Push
```

Operator:

```text
Pop required operands
Evaluate
Push result
```

The traversal direction is opposite to postfix.

---

# 35. Infix Conversion Core Idea

When converting an infix expression, the Stack usually stores:

```text
Operators
```

The output stores:

```text
Operands / Final Expression
```

The Stack helps handle:

* Operator precedence
* Associativity
* Parentheses

The main mental model is:

```text
Operand
   ↓
Usually send directly to output


Operator
   ↓
Compare with Stack Top


Opening Parenthesis
   ↓
Push


Closing Parenthesis
   ↓
Pop until matching opening parenthesis
```

---

# 36. Stack-Based Simulation

Sometimes a problem describes a process where operations happen and may need to be undone or resolved in reverse order.

A Stack can simulate this naturally.

General pattern:

```python
stack = []

for item in items:

    if some_condition:
        stack.append(item)

    else:
        while stack and another_condition:
            stack.pop()
```

The important clue is:

```text
The current item interacts with the most recent unresolved item.
```

That often suggests Stack.

---

# 37. Monotonic Stack

A **Monotonic Stack** is a Stack that maintains elements in a specific sorted order.

It can be:

```text
Monotonically Increasing
```

or:

```text
Monotonically Decreasing
```

This does not necessarily mean the original input is sorted.

The Stack maintains the order by removing elements that violate the required property.

---

# 38. Monotonically Increasing Stack

Values are maintained in increasing order from bottom to top.

Example:

```text
Bottom → 2, 4, 7, 10 ← Top
```

When a smaller value arrives, larger values may need to be popped.

General pattern:

```python
while stack and stack[-1] > current:
    stack.pop()

stack.append(current)
```

The exact comparison depends on the problem.

---

# 39. Monotonically Decreasing Stack

Values are maintained in decreasing order from bottom to top.

Example:

```text
Bottom → 10, 7, 4, 2 ← Top
```

When a larger value arrives, smaller values may need to be popped.

General pattern:

```python
while stack and stack[-1] < current:
    stack.pop()

stack.append(current)
```

Again, the exact comparison depends on the requirement.

---

# 40. Why Monotonic Stack is Important

A normal brute-force approach may compare every element with many other elements.

That can take:

```text
O(n²)
```

A Monotonic Stack can often reduce this to:

```text
O(n)
```

At first, the nested loops may look like O(n²):

```python
for item in arr:

    while stack:
        stack.pop()
```

But every element is usually:

```text
Pushed once
+
Popped at most once
```

Therefore, total work is:

```text
O(n)
```

This is called **amortized analysis**.

---

# 41. Next Greater Pattern

The idea is to find the first greater element in a particular direction.

The Stack stores elements whose answer has not yet been found.

Mental model:

```text
Current Element
      ↓
Can it resolve previous unresolved elements?
      ↓
Yes → Pop and resolve
No  → Push current
```

This is one of the most important Monotonic Stack ideas.

---

# 42. Next Smaller Pattern

Similar to Next Greater, but we search for a smaller value.

The comparison direction changes.

The core idea remains:

```text
Maintain unresolved candidates
        ↓
Current value resolves some of them
        ↓
Pop resolved elements
        ↓
Push current
```

---

# 43. Previous Greater / Previous Smaller Pattern

Sometimes we need information about the left side instead of the right side.

The Stack can represent useful candidates seen so far.

General pattern:

```python
for current in arr:

    while stack and stack[-1] does_not_satisfy_condition:
        stack.pop()

    # stack top may now represent the answer

    stack.append(current)
```

The exact traversal direction and comparison depend on whether we need:

```text
Next Greater
Next Smaller
Previous Greater
Previous Smaller
```

---

# 44. Values vs Indices in Stack

A Stack can store:

```text
Values
```

or:

```text
Indices
```

Example storing values:

```python
stack.append(arr[i])
```

Example storing indices:

```python
stack.append(i)
```

Store values when you only need:

```text
The value itself
```

Store indices when you need:

```text
Distance
Width
Position
Original index
```

This distinction is extremely important.

If a problem asks:

```text
How far?
How many positions?
What width?
Which index?
```

you probably need to store indices.

---

# 45. Monotonic Stack with Indices

Common structure:

```python
stack = []

for i in range(len(arr)):

    while stack and arr[stack[-1]] < arr[i]:
        index = stack.pop()

    stack.append(i)
```

Here:

```python
stack[-1]
```

is an index.

Therefore:

```python
arr[stack[-1]]
```

is the corresponding value.

This allows us to calculate distances such as:

```python
i - index
```

---

# 46. Unresolved Elements Pattern

One of the best ways to understand Monotonic Stack is:

```text
The Stack stores elements
whose answer is still unknown.
```

When a new element arrives:

```text
Can current element answer something
for the elements waiting in Stack?
```

If yes:

```text
Resolve them
Pop them
```

Then:

```text
Push current if it may need an answer later
```

This mental model is more useful than memorizing increasing or decreasing rules.

---

# 47. Sentinel Values

Sometimes we use a special value or index called a:

```text
Sentinel
```

A sentinel simplifies boundary conditions.

Example:

```python
stack = [-1]
```

Here `-1` may represent:

```text
No valid index before this position
```

It can help calculate widths:

```python
current_index - stack[-1]
```

without requiring separate handling for an empty Stack.

A sentinel is similar in spirit to the Dummy Node pattern in Linked Lists.

It exists to simplify edge cases.

---

# 48. Stack of Pairs

Sometimes one value is not enough.

We can store:

```python
stack.append((value, information))
```

Examples of additional information:

```text
Index
Count
Minimum
Maximum
Frequency
State
```

Example:

```python
stack.append((value, index))
```

Python tuples make this easy.

---

# 49. Maintaining Extra Information in Stack

Sometimes every Stack position needs additional information.

For example:

```text
Current Value
+
Minimum So Far
```

We can store:

```python
(value, current_minimum)
```

Example:

```python
stack.append((value, minimum))
```

This allows certain queries to remain:

```text
O(1)
```

The general technique is:

> Store enough information at insertion time so that future queries do not require scanning the entire Stack.

---

# 50. Two-Stack Technique

Sometimes one Stack is used for actual data and another for additional information.

Conceptually:

```text
Main Stack
+
Helper Stack
```

The helper Stack may track:

```text
Minimum
Maximum
History
Temporary elements
```

This is a general design pattern.

---

# 51. Stack and DFS

Depth-First Search follows Stack behavior.

Recursive DFS uses:

```text
Call Stack
```

Iterative DFS uses:

```text
Explicit Stack
```

General iterative DFS structure:

```python
stack = [start]

while stack:
    node = stack.pop()

    # process node

    for neighbor in neighbors:
        stack.append(neighbor)
```

Because the most recently discovered node is processed first, traversal goes deep before returning.

---

# 52. Stack and Backtracking

Backtracking also behaves like a Stack.

We:

```text
Make Choice
    ↓
Go Deeper
    ↓
Undo Choice
    ↓
Try Another Choice
```

The call stack remembers previous states.

Conceptually:

```text
Push State
    ↓
Explore
    ↓
Pop State
    ↓
Return
```

This is why understanding Stack helps with recursion and backtracking.

---

# 53. Stack and Undo Operations

Suppose actions happen in this order:

```text
Action A
Action B
Action C
```

If we press Undo:

```text
Undo C
```

Then:

```text
Undo B
```

Then:

```text
Undo A
```

This follows:

```text
LIFO
```

The most recent action is undone first.

---

# 54. Stack and Browser Navigation

Navigation history can use Stack-like behavior.

Suppose:

```text
Page A
→ Page B
→ Page C
```

Pressing Back should return to:

```text
Page B
```

Then:

```text
Page A
```

More complete browser history behavior often uses:

```text
Back Stack
+
Forward Stack
```

This is another example of the Two-Stack technique.

---

# 55. Stack and String Processing

Stacks are useful when processing strings containing:

* Nested structures
* Repeated patterns
* Operators
* Encoded sections
* Characters that cancel previous characters

General pattern:

```python
stack = []

for ch in string:

    if stack and some_relation(stack[-1], ch):
        stack.pop()

    else:
        stack.append(ch)
```

This is common when the current character interacts with the most recent unresolved character.

---

# 56. Removing Elements Using Stack

Sometimes we process elements and remove previous elements that violate a condition.

General pattern:

```python
stack = []

for value in values:

    while stack and should_remove(stack[-1], value):
        stack.pop()

    stack.append(value)
```

This pattern is the foundation of many optimized Stack algorithms.

---

# 57. Circular Array with Stack

Sometimes the array is considered circular.

Example:

```text
[1, 2, 3]
```

After `3`, we conceptually return to:

```text
1
```

A common technique is to simulate multiple passes using modulo:

```python
index = i % n
```

Instead of physically creating:

```text
[1, 2, 3, 1, 2, 3]
```

we can simulate it.

This technique is often combined with a Monotonic Stack.

---

# 58. Why Stack Solutions Often Traverse in Reverse

Sometimes the answer for the current element depends on something to its right.

One approach is to traverse:

```text
Right → Left
```

Then the Stack already contains useful information from the right side.

General thinking:

```text
Need information from right?
        ↓
Consider reverse traversal


Need information from left?
        ↓
Consider forward traversal
```

This is not an absolute rule, but it is a useful pattern-recognition technique.

---

# 59. Stack Traversal Direction

Always ask:

```text
Where should the useful candidates already exist?
```

If you need information about previous elements:

```text
Traverse Left → Right
```

If you need information about future/right-side elements:

```text
Sometimes traverse Right → Left
```

Another approach is to traverse left to right while keeping unresolved elements in the Stack.

Both styles are valid depending on the problem.

---

# 60. Common Stack Template

Basic Stack:

```python
stack = []

for item in items:

    while stack and condition:
        stack.pop()

    stack.append(item)
```

This simple structure appears in many Stack algorithms.

The important part is understanding:

```text
What does the Stack represent?

Why are elements popped?

Why is the current element pushed?
```

Never use a Stack pattern without answering these three questions.

---

# 61. Important Monotonic Stack Mental Model

Before writing code, define:

```text
1. What is stored in Stack?
   Value or Index?

2. What order does Stack maintain?
   Increasing or Decreasing?

3. What does a Stack element represent?
   Candidate or Unresolved element?

4. When should we pop?

5. When should we push?

6. When is the answer calculated?
   Before pop?
   During pop?
   After pop?

7. Which direction should we traverse?
```

If these questions are clear, the code becomes much easier.

---

# 62. Stack vs Queue

Stack:

```text
LIFO

Last In
First Out
```

Queue:

```text
FIFO

First In
First Out
```

Example:

```text
Stack:

Push 10
Push 20
Push 30

Remove → 30
```

Queue:

```text
Insert 10
Insert 20
Insert 30

Remove → 10
```

---

# 63. Stack vs Recursion

Recursion uses the system's call stack.

Explicit Stack uses a data structure created by us.

| Recursion               | Explicit Stack                |
| ----------------------- | ----------------------------- |
| Uses Call Stack         | Uses Our Stack                |
| Often simpler code      | More control                  |
| Can hit recursion limit | Avoids recursion-depth issues |
| Stack frames automatic  | State managed manually        |

Both often represent the same underlying idea.

---

# 64. Common Mistake — Popping Empty Stack

Wrong:

```python
stack.pop()
```

without checking whether elements exist.

Safe:

```python
if stack:
    stack.pop()
```

---

# 65. Common Mistake — Accessing Empty Stack Top

Wrong:

```python
stack[-1]
```

when:

```python
stack = []
```

Safe:

```python
if stack and stack[-1] == value:
```

Python evaluates conditions left to right.

If:

```python
stack
```

is empty, Python does not evaluate:

```python
stack[-1]
```

This is called:

```text
Short-Circuit Evaluation
```

---

# 66. Common Mistake — Using `pop(0)`

Wrong Stack implementation:

```python
stack.pop(0)
```

This removes from the beginning and takes:

```text
O(n)
```

Correct:

```python
stack.pop()
```

which removes from the end in:

```text
O(1)
```

---

# 67. Common Mistake — Confusing Stack Top

For a Python list Stack:

```python
stack = [10, 20, 30]
```

The top is:

```python
stack[-1]
```

not:

```python
stack[0]
```

Think:

```text
[10, 20, 30]
         ↑
        TOP
```

---

# 68. Common Mistake — Forgetting Operand Order

When evaluating an expression:

```python
right = stack.pop()
left = stack.pop()
```

The operation is:

```python
left - right
```

not:

```python
right - left
```

This matters for non-commutative operators:

```text
-
/
```

---

# 69. Common Mistake — Storing Values When Indices Are Needed

Suppose you need:

```text
Distance between two elements
```

If you only store values:

```python
stack.append(arr[i])
```

you lose the original position.

Instead:

```python
stack.append(i)
```

Then:

```python
i - stack[-1]
```

can calculate distance.

Always decide carefully between:

```text
Value
vs
Index
```

---

# 70. Common Mistake — Thinking Nested While Means O(n²)

Code like:

```python
for value in arr:

    while stack and condition:
        stack.pop()
```

may still be:

```text
O(n)
```

if every element is:

```text
Pushed once
Popped at most once
```

Do not calculate complexity only by counting nested loops.

Analyze how many times each element can actually be processed.

---

# 71. Common Mistake — Wrong Comparison in Monotonic Stack

These conditions are different:

```python
stack[-1] < current
```

and:

```python
stack[-1] <= current
```

The choice matters when duplicate values exist.

Always ask:

```text
Should equal values remain?

Or should equal values be removed?
```

This affects:

* Boundaries
* Duplicate handling
* Previous/next relationships

---

# 72. Common Mistake — Modifying Stack While Needing Old Information

Before popping, sometimes we need the top value or index.

Correct:

```python
index = stack.pop()

# use index
```

Do not pop information before saving it if it will be needed later.

---

# 73. Common Mistake — Not Understanding What Stack Stores

Before writing code, complete this sentence:

```text
"My Stack stores __________________."
```

Examples:

```text
unmatched opening brackets

indices waiting for a greater element

previous smaller candidates

function states

operators

characters not yet cancelled
```

If you cannot explain what the Stack represents, the algorithm is probably not yet clear.

---

# 74. Stack Complexity Cheat Sheet

| Operation   | Python           |           Time |
| ----------- | ---------------- | -------------: |
| Push        | `append()`       | O(1) amortized |
| Pop         | `pop()`          |           O(1) |
| Peek        | `stack[-1]`      |           O(1) |
| Empty Check | `if not stack`   |           O(1) |
| Size        | `len(stack)`     |           O(1) |
| Search      | Manual traversal |           O(n) |

A Stack does not provide efficient arbitrary searching.

Its strength comes from accessing:

```text
The Top
```

---

# 75. Stack Space Complexity

If a Stack stores `n` elements:

```text
O(n)
```

space is required.

A recursive algorithm with recursion depth `n` also uses approximately:

```text
O(n)
```

call-stack space.

A Monotonic Stack can contain up to:

```text
n
```

elements in the worst case.

Therefore:

```text
Space Complexity = O(n)
```

---

# 76. How to Dry Run Stack Code

Suppose:

```text
Input:

[3, 1, 4]
```

Always draw:

```text
Current Element
Stack Before
Operations
Stack After
```

Example:

```text
Current = 3

Before:
[]

Push 3

After:
[3]
```

Next:

```text
Current = 1

Before:
[3]

Perform condition

After:
[...]
```

For Monotonic Stack, also track:

```text
Index
Value
Stack Indices
Stack Values
Answer
```

This makes complicated Stack logic much easier to understand.

---

# 77. How to Recognize a Stack Problem

Look for clues such as:

```text
Nested structures
        ↓
Stack


Matching opening and closing elements
        ↓
Stack


Undo / reverse order
        ↓
Stack


Most recent unresolved item
        ↓
Stack


Current element affects previous elements
        ↓
Stack


Next greater / smaller
        ↓
Monotonic Stack


Previous greater / smaller
        ↓
Monotonic Stack


Need nearest boundary
        ↓
Monotonic Stack


Expression evaluation
        ↓
Stack


Need to simulate recursion
        ↓
Explicit Stack


Depth-first processing
        ↓
Stack
```

---

# 78. Important Stack Patterns Cheat Sheet

| Situation                       | Pattern                |
| ------------------------------- | ---------------------- |
| Basic LIFO processing           | Normal Stack           |
| Matching nested symbols         | Opening elements Stack |
| Reverse order                   | Push then Pop          |
| Most recent unresolved item     | Stack                  |
| Expression evaluation           | Operand Stack          |
| Expression conversion           | Operator Stack         |
| Next Greater                    | Monotonic Stack        |
| Next Smaller                    | Monotonic Stack        |
| Previous Greater                | Monotonic Stack        |
| Previous Smaller                | Monotonic Stack        |
| Need position/distance          | Store Indices          |
| Need extra state                | Stack of Tuples        |
| Need min/max history            | Helper Stack           |
| Recursive traversal iteratively | Explicit Stack         |
| DFS                             | Stack                  |
| Circular sequence               | Modulo + Stack         |
| Simplify boundary handling      | Sentinel               |

---

# 79. Normal Stack vs Monotonic Stack

Normal Stack:

```text
Maintains insertion order according to LIFO.
```

Monotonic Stack:

```text
Maintains a useful increasing or decreasing property.
```

Normal Stack example:

```text
[5, 1, 8, 2]
```

Any order is allowed.

Monotonic Increasing Stack:

```text
[1, 3, 5, 8]
```

Monotonic Decreasing Stack:

```text
[9, 7, 4, 2]
```

The monotonic property is maintained by popping elements when necessary.

---

# 80. The Most Important Monotonic Stack Insight

Do not blindly memorize:

```text
Next Greater = decreasing Stack
Next Smaller = increasing Stack
```

Instead understand:

```text
What elements are waiting for an answer?

Can the current element answer them?

If yes:
    resolve them and pop them

If no:
    keep them waiting
```

This approach makes Monotonic Stack patterns much easier to remember.

---

# 81. Final Stack Mental Model

Think of a Stack as:

```text
A waiting area where the most recent item
gets attention first.
```

Normal Stack:

```text
Most recent item
      ↓
Processed first
```

Parentheses:

```text
Most recent opening bracket
      ↓
Must close first
```

Recursion:

```text
Most recent function call
      ↓
Returns first
```

Monotonic Stack:

```text
Most recent useful/unresolved candidates
      ↓
Current element may resolve them
```

---

# 82. Final Revision Map

```text
Stack
│
├── Core Principle
│   └── LIFO
│
├── Basic Operations
│   ├── Push
│   ├── Pop
│   ├── Peek / Top
│   ├── isEmpty
│   └── Size
│
├── Implementation
│   ├── Python List
│   ├── Fixed Array Concept
│   └── Linked List
│
├── Important Concepts
│   ├── Top
│   ├── Underflow
│   ├── Overflow
│   ├── Call Stack
│   ├── Stack Frames
│   └── Recursion
│
├── Core Uses
│   ├── Reversal
│   ├── Matching
│   ├── Nested Structures
│   ├── Expression Processing
│   ├── Simulation
│   ├── DFS
│   └── Backtracking
│
├── Expression Concepts
│   ├── Infix
│   ├── Prefix
│   ├── Postfix
│   ├── Precedence
│   └── Associativity
│
├── Monotonic Stack
│   ├── Increasing
│   ├── Decreasing
│   ├── Next Greater
│   ├── Next Smaller
│   ├── Previous Greater
│   ├── Previous Smaller
│   └── Amortized O(n)
│
├── Advanced Techniques
│   ├── Store Values
│   ├── Store Indices
│   ├── Stack of Pairs
│   ├── Helper Stack
│   ├── Sentinel
│   ├── Circular Traversal
│   └── Explicit Stack
│
└── Problem-Solving Questions
    ├── What does my Stack store?
    ├── When do I push?
    ├── When do I pop?
    ├── Why do I pop?
    ├── Do I need values or indices?
    ├── What order should Stack maintain?
    └── Which direction should I traverse?
```

---

# 🎯 Final Takeaway

Stack problems become easier when you stop thinking only about:

```text
push()
pop()
```

and start thinking about:

```text
What does my Stack represent?
```

The most important concepts to remember are:

```text
1. Stack follows LIFO.

2. In Python:
   append() → Push
   pop()    → Pop
   stack[-1] → Peek

3. Always check before popping or accessing the top.

4. The system call stack is responsible for recursion.

5. Stack is useful when the most recent unresolved item
   must be processed first.

6. For Monotonic Stack, every element is usually pushed once
   and popped at most once, giving O(n) time.

7. Store indices when you need positions, widths, or distances.

8. Store values when you only need direct value comparison.

9. A Stack can store more than values:
   indices, tuples, states, operators, or nodes.

10. Before writing any Stack solution, answer:

    "What exactly is waiting inside my Stack,
     and what event causes it to leave?"
```

The strongest mental model is:

```text
Normal Stack
    ↓
Remember recent information


Monotonic Stack
    ↓
Remember useful unresolved candidates


Call Stack
    ↓
Remember unfinished function calls
```

Once these three ideas are clear, most Stack-based algorithms become much easier to understand and recognize.
