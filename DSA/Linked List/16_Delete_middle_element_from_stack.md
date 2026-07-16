# Delete Middle Element of a Stack

## Problem Overview

Given a Stack, remove its middle element without using another Stack or additional data structure.

Example:

```text
Stack:

TOP
 ↓
50
40
30   ← Middle
20
10
```

After removing the middle element:

```text
TOP
 ↓
50
40
20
10
```

Python representation:

```text
Before:

[10, 20, 30, 40, 50]

After:

[10, 20, 40, 50]
```

---

# Approach — Recursion + Backtracking

The main idea is:

```text
Remove elements from the top
        ↓
Reach the middle element
        ↓
Delete the middle element
        ↓
Return from recursion
        ↓
Restore all previously removed elements
```

This uses two important concepts:

```text
Recursion
    +
Backtracking
```

---

# Python Code

```python
def getMiddleStack(stack, count):

    # Base Case:
    # We have reached the middle element
    if count == 0:
        stack.pop()
        return

    # Remove the current top element
    top = stack.pop()

    # Move one level closer to the middle
    count -= 1

    # Recursive call
    getMiddleStack(stack, count)

    # Backtracking:
    # Restore the removed element
    stack.append(top)


stack = []

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

length = len(stack)

count = length // 2

getMiddleStack(stack, count)

print(stack)
```

Output:

```text
[10, 20, 40, 50]
```

---

# Understanding the Stack

We insert:

```python
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
```

Python represents the Stack as:

```text
[10, 20, 30, 40, 50]
```

Remember:

```text
LEFT                RIGHT
 ↓                     ↓
Bottom                Top
```

So:

```text
TOP
 ↓
50
40
30
20
10
```

The middle element is:

```text
30
```

---

# Finding How Deep We Need to Go

We calculate:

```python
length = len(stack)
```

Here:

```text
length = 5
```

Then:

```python
count = length // 2
```

Therefore:

```text
count = 5 // 2

count = 2
```

This means we need to remove:

```text
2 elements
```

from the top before reaching the middle.

The elements above the middle are:

```text
50
40
```

After removing them:

```text
TOP
 ↓
30   ← Middle
20
10
```

Now:

```text
count = 0
```

and the top element is exactly the middle element.

---

# Base Case

The base case is:

```python
if count == 0:
    stack.pop()
    return
```

When:

```text
count = 0
```

the middle element is currently at the top of the Stack.

So:

```python
stack.pop()
```

removes it.

Before:

```text
TOP
 ↓
30
20
10
```

After:

```text
TOP
 ↓
20
10
```

Then:

```python
return
```

starts returning to the previous recursive calls.

---

# Why Do We Pop Before Recursion?

The only element we can directly access in a Stack is:

```text
TOP
```

But the element we want to remove is somewhere inside:

```text
TOP
 ↓
50
40
30   ← Need to remove
20
10
```

We cannot directly remove `30`.

So we temporarily remove the elements above it:

```text
Pop 50
Pop 40
```

Now:

```text
TOP
 ↓
30
20
10
```

The middle element has reached the top.

Now it can be removed using:

```python
stack.pop()
```

---

# Why Do We Store `top`?

Before removing an element, we save it:

```python
top = stack.pop()
```

For example:

```text
top = 50
```

The Stack becomes:

```text
[10, 20, 30, 40]
```

The value `50` is stored inside the local variable:

```text
top
```

Then another recursive call stores:

```text
top = 40
```

Each recursive call has its own separate local variable.

Conceptually:

```text
Call 1:

top = 50


Call 2:

top = 40


Call 3:

Remove 30
```

The recursion call stack remembers these values for us.

---

# Recursive Flow

Initial:

```text
Stack = [10, 20, 30, 40, 50]

count = 2
```

---

## Recursive Call 1

```text
count = 2
```

Remove:

```text
50
```

Save:

```text
top = 50
```

Stack:

```text
[10, 20, 30, 40]
```

Decrease:

```text
count = 1
```

Call recursion.

---

## Recursive Call 2

```text
count = 1
```

Remove:

```text
40
```

Save:

```text
top = 40
```

Stack:

```text
[10, 20, 30]
```

Decrease:

```text
count = 0
```

Call recursion.

---

## Recursive Call 3 — Base Case

```text
count = 0
```

Current Stack:

```text
[10, 20, 30]
```

Top:

```text
30
```

Remove it:

```python
stack.pop()
```

Stack becomes:

```text
[10, 20]
```

Then:

```python
return
```

Now recursion starts going backward.

---

# Backtracking Phase

This line is extremely important:

```python
stack.append(top)
```

It executes **after** the recursive call returns.

This is the backtracking step.

The elements we temporarily removed must now be restored.

---

## Returning to Call 2

Call 2 had stored:

```text
top = 40
```

Current Stack:

```text
[10, 20]
```

Execute:

```python
stack.append(40)
```

Now:

```text
[10, 20, 40]
```

---

## Returning to Call 1

Call 1 had stored:

```text
top = 50
```

Execute:

```python
stack.append(50)
```

Now:

```text
[10, 20, 40, 50]
```

Final Stack:

```text
TOP
 ↓
50
40
20
10
```

The middle element `30` is gone.

---

# Complete Recursion Flow

```text
                FORWARD / RECURSION

[10, 20, 30, 40, 50]
count = 2
        |
        | pop 50
        ↓
[10, 20, 30, 40]
count = 1
        |
        | pop 40
        ↓
[10, 20, 30]
count = 0
        |
        | pop 30
        ↓
[10, 20]


                BACKTRACKING

[10, 20]
        |
        | append 40
        ↓
[10, 20, 40]
        |
        | append 50
        ↓
[10, 20, 40, 50]
```

---

# The Most Important Pattern

This solution follows:

```text
POP
 ↓
RECURSE
 ↓
DO THE REQUIRED WORK
 ↓
BACKTRACK
 ↓
PUSH BACK
```

More specifically:

```text
Remove Top Elements
        ↓
Reach Target Position
        ↓
Remove Target
        ↓
Return from Recursion
        ↓
Restore Removed Elements
```

This is a very important **Stack + Recursion pattern**.

---

# Where is Backtracking Happening?

The backtracking happens here:

```python
stack.append(top)
```

Anything written:

```text
Before Recursive Call
```

happens while going deeper.

Anything written:

```text
After Recursive Call
```

happens while returning.

In this code:

```python
top = stack.pop()

getMiddleStack(stack, count)

stack.append(top)
```

We can think:

```text
stack.pop()
     ↓
Going Down


Recursive Call
     ↓
Go Deeper


stack.append(top)
     ↓
Coming Back / Backtracking
```

---

# Why Is Another Stack Not Required?

Normally, we could temporarily store removed elements in another Stack.

But here recursion itself provides a hidden Stack:

```text
Call Stack
```

Each function call remembers its own:

```text
top
```

value.

Conceptually:

```text
Call Stack

┌─────────────┐
│ top = 40    │
├─────────────┤
│ top = 50    │
└─────────────┘
```

When recursion returns:

```text
40 is restored first
50 is restored next
```

This naturally follows:

```text
LIFO
```

So the recursion call stack temporarily stores the removed elements for us.

---

# Important Concept — Each Recursive Call Has Its Own `top`

Even though the variable name is always:

```python
top
```

each recursive call gets its own copy.

Conceptually:

```text
getMiddleStack(count=2)

top = 50


    getMiddleStack(count=1)

    top = 40


        getMiddleStack(count=0)

        remove 30
```

So `top = 50` is not overwritten by `top = 40`.

They belong to different function calls.

---

# Why `count -= 1` Works

Every time we remove one element from the top, we move one position closer to the middle.

```text
count = 2

Pop 50

count = 1

Pop 40

count = 0
```

When:

```text
count == 0
```

the target element is now at the top.

---

# Time Complexity

We recursively remove elements until reaching the middle.

For a Stack of size `n`, approximately:

```text
n / 2
```

elements are removed and restored.

Therefore:

```text
Time Complexity = O(n)
```

---

# Space Complexity

No explicit extra Stack is created.

However, recursion uses the internal:

```text
Call Stack
```

The recursion depth is approximately:

```text
n / 2
```

In Big O notation:

```text
Space Complexity = O(n)
```

This is an important point:

> Using recursion does not mean O(1) space.

The recursive function calls consume call-stack memory.

---

# Important Edge Case — Even-Sized Stack

Suppose:

```text
[10, 20, 30, 40]
```

Then:

```python
length = 4
count = 4 // 2
```

So:

```text
count = 2
```

From the top:

```text
TOP
 ↓
40    position 0
30    position 1
20    position 2
10    position 3
```

This implementation removes:

```text
20
```

For an even-sized Stack, there are two possible middle elements:

```text
20 and 30
```

So the expected middle must be defined by the problem.

Depending on the required middle, the initial `count` may need to change.

---

# Common Mistake — Forgetting to Restore Elements

If we write:

```python
top = stack.pop()

getMiddleStack(stack, count)
```

but forget:

```python
stack.append(top)
```

then all elements above the middle will also be removed.

For example:

```text
Original:

[10, 20, 30, 40, 50]
```

Without backtracking:

```text
Final:

[10, 20]
```

Instead of:

```text
[10, 20, 40, 50]
```

Therefore:

```python
stack.append(top)
```

is essential.

---

# Common Mistake — Appending Before Recursion

This would not work:

```python
top = stack.pop()

stack.append(top)

getMiddleStack(stack, count)
```

Because we immediately put the same element back.

The Stack never gets smaller.

The target element never reaches the top.

Correct order:

```text
POP
 ↓
RECURSE
 ↓
PUSH BACK
```

---

# Common Mistake — Not Understanding the Base Case

The base case:

```python
if count == 0:
    stack.pop()
    return
```

does two things:

```text
1. Removes the target element

2. Stops further recursive calls
```

If we continue recursion after reaching the middle, we may remove elements below the target.

---

# Pattern Used

For your DSA sheet, the short pattern name is:

```text
Recursion + Backtracking on Stack
```

Or more specifically:

```text
Pop → Recurse → Restore
```

---

# Key Learning

The main concept behind this solution is:

```text
We cannot directly access the middle of a Stack.

So:

Temporarily remove top elements
        ↓
Use recursion to remember them
        ↓
Reach and remove the middle
        ↓
Backtrack
        ↓
Restore the removed elements
```

The core template is:

```python
def solve(stack):

    # Base Case
    if target_reached:
        # perform required operation
        return

    # Remove current top
    top = stack.pop()

    # Recursive call
    solve(stack)

    # Backtracking
    stack.append(top)
```

The most important thing to remember is:

```text
Before recursion
    ↓
We remove / make a choice


During recursion
    ↓
We solve the smaller problem


After recursion
    ↓
We restore / backtrack
```

This **Pop → Recurse → Restore** pattern is one of the most important recursive patterns when working with Stacks.
