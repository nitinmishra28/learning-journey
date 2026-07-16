# Reverse a Stack Using Recursion

## Problem Overview

Given a Stack, reverse it using recursion.

The goal is to reverse:

```text id="rxseoz"
TOP
 ↓
50
40
30
20
10
```

into:

```text id="0wg3yh"
TOP
 ↓
10
20
30
40
50
```

Python representation:

```text id="8x53r4"
Before:

[10, 20, 30, 40, 50]


After:

[50, 40, 30, 20, 10]
```

Remember that in a Python list used as a Stack:

```text id="1x09dz"
[10, 20, 30, 40, 50]
 ↑                   ↑
Bottom              Top
```

---

# Approach — Recursion + Insert at Bottom

The main idea is:

```text id="il98v3"
Remove every element
        ↓
Reach an empty Stack
        ↓
While recursion returns
        ↓
Insert each removed element
at the BOTTOM
```

Normally, when we pop elements recursively and push them back, the Stack remains in the same order.

To reverse the Stack, instead of putting each element back on the top, we put it at the:

```text id="mv46k1"
BOTTOM
```

This requires a helper function:

```python id="mbi2yd"
insertAtBottom()
```

So the complete solution contains two recursive ideas:

```text id="zd74kl"
reverse()
    ↓
Removes elements recursively


insertAtBottom()
    ↓
Places each element at the bottom
```

---

# Python Code

```python id="o5mg0x"
def insertAtBottom(stack, topElement):

    # Base Case:
    # If the stack is empty,
    # insert the element at the bottom
    if len(stack) == 0:
        stack.append(topElement)
        return

    # Save the current top element
    topE = stack[-1]

    # Remove the current top
    stack.pop()

    # Insert the target element
    # into the bottom of the remaining stack
    insertAtBottom(stack, topElement)

    # Backtracking:
    # Restore the removed top element
    stack.append(topE)


def reverse(stack):

    # Base Case
    if len(stack) == 0:
        return

    # Remove the current top element
    topElement = stack.pop()

    # Reverse the remaining stack
    reverse(stack)

    # Insert the removed element
    # at the bottom of the reversed stack
    insertAtBottom(stack, topElement)


stack = []

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

reverse(stack)

print(stack)
```

Output:

```text id="hx0i66"
[50, 40, 30, 20, 10]
```

---

# The Core Idea

The complete algorithm can be understood as:

```text id="m8w0br"
POP ALL ELEMENTS
        ↓
RECURSIVELY REVERSE SMALLER STACK
        ↓
INSERT REMOVED ELEMENTS AT BOTTOM
```

The key recursive relation is:

```text id="hz8oyy"
Reverse Stack
      =
Reverse Smaller Stack
      +
Insert Current Top at Bottom
```

This is the most important idea behind the solution.

---

# Why Do We Need `insertAtBottom()`?

Suppose:

```text id="xjwlrc"
Stack:

[10, 20, 30]
```

If we simply do:

```text id="07l2zx"
Pop 30
Pop 20
Pop 10
```

and then push them back during recursion:

```text id="1njl9m"
Push 10
Push 20
Push 30
```

we again get:

```text id="ehtcb3"
[10, 20, 30]
```

The Stack is not reversed.

To reverse it, each removed element must be inserted at the:

```text id="24w9j8"
Bottom
```

Therefore:

```text id="rm2k6w"
30 → Insert at Bottom

20 → Insert at Bottom

10 → Insert at Bottom
```

This changes the order.

---

# Understanding `reverse()`

The function is:

```python id="pfif9v"
def reverse(stack):

    if len(stack) == 0:
        return

    topElement = stack.pop()

    reverse(stack)

    insertAtBottom(stack, topElement)
```

It has three important steps:

```text id="g70z67"
1. POP

2. RECURSE

3. INSERT AT BOTTOM
```

---

# Step 1 — Pop the Top Element

```python id="0ik5by"
topElement = stack.pop()
```

Suppose:

```text id="smuod9"
[10, 20, 30, 40, 50]
```

Then:

```text id="ufhxje"
topElement = 50
```

Stack becomes:

```text id="p7lqma"
[10, 20, 30, 40]
```

The recursive call now solves the smaller problem.

---

# Step 2 — Reverse the Remaining Stack

```python id="rxp7wv"
reverse(stack)
```

The recursive calls continue:

```text id="g7t3bs"
reverse([10, 20, 30, 40, 50])

Pop 50
        ↓

reverse([10, 20, 30, 40])

Pop 40
        ↓

reverse([10, 20, 30])

Pop 30
        ↓

reverse([10, 20])

Pop 20
        ↓

reverse([10])

Pop 10
        ↓

reverse([])

Base Case
```

At the deepest point:

```text id="u61jj5"
stack = []
```

Now recursion starts returning.

---

# Recursive Call Stack

Each recursive call remembers its own:

```python id="i16i1p"
topElement
```

Conceptually:

```text id="op3hdq"
Call 1:

topElement = 50


Call 2:

topElement = 40


Call 3:

topElement = 30


Call 4:

topElement = 20


Call 5:

topElement = 10
```

These values are stored in different recursive stack frames.

When recursion returns, they are processed in reverse call order:

```text id="4x2fcd"
10
20
30
40
50
```

But instead of normal pushing, each one is inserted at the bottom.

---

# Understanding `insertAtBottom()`

The helper function is:

```python id="b21oxb"
def insertAtBottom(stack, topElement):

    if len(stack) == 0:
        stack.append(topElement)
        return

    topE = stack[-1]

    stack.pop()

    insertAtBottom(stack, topElement)

    stack.append(topE)
```

Its job is:

```text id="0jqedr"
Take one element
        ↓
Put it below every existing Stack element
```

---

# How Does `insertAtBottom()` Work?

Suppose:

```text id="cavd6a"
Stack:

[10, 20, 30]
```

We want to insert:

```text id="5t5jvh"
5
```

at the bottom.

Desired result:

```text id="yrz6d8"
[5, 10, 20, 30]
```

But Stack only gives access to the top.

So we temporarily remove everything.

---

## Step 1

Current:

```text id="d04nnq"
[10, 20, 30]
```

Save:

```text id="oq8p3r"
topE = 30
```

Pop:

```text id="vz68xb"
[10, 20]
```

---

## Step 2

Save:

```text id="lh5j9u"
topE = 20
```

Pop:

```text id="d39vcc"
[10]
```

---

## Step 3

Save:

```text id="zrujxz"
topE = 10
```

Pop:

```text id="5ecam4"
[]
```

---

## Step 4 — Base Case

Now:

```text id="o17e4w"
stack = []
```

So:

```python id="81h6yt"
stack.append(5)
```

Stack:

```text id="n6d0if"
[5]
```

The target element has reached the bottom.

---

# Backtracking in `insertAtBottom()`

Now recursion returns.

The removed elements are restored.

First:

```text id="2qpkc4"
Append 10
```

Stack:

```text id="18rzf8"
[5, 10]
```

Then:

```text id="9qkw1n"
Append 20
```

Stack:

```text id="vhp5pu"
[5, 10, 20]
```

Then:

```text id="8kvf75"
Append 30
```

Stack:

```text id="52xudc"
[5, 10, 20, 30]
```

Final result:

```text id="akxpjv"
[5, 10, 20, 30]
```

So the helper follows:

```text id="p5uh4r"
POP
 ↓
RECURSE
 ↓
INSERT TARGET
 ↓
RESTORE
```

---

# Complete Dry Run

Initial:

```text id="47bgd7"
[10, 20, 30, 40, 50]
```

---

## Phase 1 — Remove Everything

```text id="2dp52y"
Pop 50

[10, 20, 30, 40]


Pop 40

[10, 20, 30]


Pop 30

[10, 20]


Pop 20

[10]


Pop 10

[]
```

Now the base case is reached.

---

# Phase 2 — Insert Elements at Bottom

The first recursive call returning has:

```text id="ukxarq"
topElement = 10
```

Insert `10` at bottom:

```text id="j9ws5q"
[10]
```

---

Next:

```text id="6q0mdq"
topElement = 20
```

Insert `20` at bottom of:

```text id="mq3whx"
[10]
```

Result:

```text id="a5un3j"
[20, 10]
```

---

Next:

```text id="s4b03h"
topElement = 30
```

Insert `30` at bottom:

```text id="y4l7fq"
[30, 20, 10]
```

---

Next:

```text id="pmfzxu"
topElement = 40
```

Result:

```text id="q3zkcr"
[40, 30, 20, 10]
```

---

Finally:

```text id="l8x7kw"
topElement = 50
```

Result:

```text id="fg9os2"
[50, 40, 30, 20, 10]
```

The Stack is now reversed.

---

# Complete Recursion Flow

```text id="ohuqss"
FORWARD RECURSION
=================

[10, 20, 30, 40, 50]

        Pop 50
           ↓

[10, 20, 30, 40]

        Pop 40
           ↓

[10, 20, 30]

        Pop 30
           ↓

[10, 20]

        Pop 20
           ↓

[10]

        Pop 10
           ↓

[]


BACKTRACKING
============

Insert 10 at Bottom

[10]

        ↓

Insert 20 at Bottom

[20, 10]

        ↓

Insert 30 at Bottom

[30, 20, 10]

        ↓

Insert 40 at Bottom

[40, 30, 20, 10]

        ↓

Insert 50 at Bottom

[50, 40, 30, 20, 10]
```

---

# Two Levels of Recursion

This solution is important because there are actually two recursive processes.

## Outer Recursion

```python id="e7nccy"
reverse(stack)
```

Its job is:

```text id="m9q17y"
Remove every element
        ↓
Process smaller Stack
        ↓
Send removed element to insertAtBottom()
```

Pattern:

```text id="1v2rhb"
Pop → Recurse → Insert at Bottom
```

---

## Inner Recursion

```python id="84v8an"
insertAtBottom(stack, element)
```

Its job is:

```text id="6ny85a"
Remove existing elements
        ↓
Reach empty Stack
        ↓
Insert target
        ↓
Restore existing elements
```

Pattern:

```text id="5p4lf8"
Pop → Recurse → Insert → Restore
```

Together:

```text id="v4sz2c"
reverse()
    ↓
Uses
    ↓
insertAtBottom()
```

---

# Where Is Backtracking Used?

Backtracking happens inside:

```python id="1m7yfh"
insertAtBottom()
```

Specifically:

```python id="eb8prx"
stack.append(topE)
```

Consider:

```python id="q3c9ow"
topE = stack.pop()

insertAtBottom(stack, topElement)

stack.append(topE)
```

The flow is:

```text id="yqb0pm"
POP
 ↓
Go Deeper
 ↓
Insert Target
 ↓
Come Back
 ↓
RESTORE
```

The restoration step is backtracking.

---

# Why Does This Reverse the Stack?

This is the key idea.

Normal recursive restoration would do:

```text id="e8mvle"
Pop 50
Pop 40
Pop 30

Then:

Push 30
Push 40
Push 50
```

which recreates the original order.

But this solution does:

```text id="bbgr97"
Pop 50
Pop 40
Pop 30

Then:

Insert 30 at Bottom
Insert 40 at Bottom
Insert 50 at Bottom
```

Each element is placed below the elements already present.

Therefore, the original top elements gradually become the bottom elements.

That reverses the Stack.

---

# Recursive Faith

A useful way to think about this solution is:

Suppose:

```python id="r8vzhp"
reverse(stack)
```

already knows how to reverse the smaller Stack.

Then your only job is:

```text id="cjq5x1"
Remove Current Top
        ↓
Ask Recursion to Reverse Remaining Stack
        ↓
Put Current Top at Bottom
```

Example:

```text id="mkhkg7"
Original:

[10, 20, 30]
```

Remove:

```text id="llqmxj"
30
```

Trust recursion to reverse:

```text id="h0gwmn"
[10, 20]
```

into:

```text id="tfnm18"
[20, 10]
```

Now insert:

```text id="fyyd6m"
30
```

at the bottom:

```text id="q7jqz9"
[30, 20, 10]
```

Done.

This is called:

```text id="r0vpne"
Recursive Faith
```

You solve one small part and trust recursion to solve the smaller version of the same problem.

---

# Base Case of `reverse()`

```python id="xbr9a5"
if len(stack) == 0:
    return
```

An empty Stack is already reversed.

There is nothing left to process.

So recursion stops.

---

# Base Case of `insertAtBottom()`

```python id="ll62m8"
if len(stack) == 0:
    stack.append(topElement)
    return
```

When the Stack becomes empty, we have reached the bottom.

Therefore, the target element can be inserted.

Then recursion returns and restores everything above it.

---

# Time Complexity

This solution has two recursive operations.

For every element removed by:

```python id="83oq3f"
reverse()
```

we call:

```python id="9rt7je"
insertAtBottom()
```

For a Stack of `n` elements:

```text id="7eowf8"
First insertion     → O(1)

Second insertion    → O(2)

Third insertion     → O(3)

...

Nth insertion       → O(n)
```

Total:

```text id="g8f93q"
1 + 2 + 3 + ... + n
```

The sum is:

```text id="5jq2nh"
n(n + 1) / 2
```

Therefore:

```text id="xvxblh"
Time Complexity = O(n²)
```

---

# Space Complexity

The algorithm does not create another explicit Stack.

However, recursion uses the call stack.

The maximum recursion depth is proportional to:

```text id="x1aajh"
n
```

Therefore:

```text id="h4j8i4"
Auxiliary Space Complexity = O(n)
```

The two recursive functions do not produce O(n²) simultaneous stack depth. Their maximum active recursion depth remains proportional to `n`.

---

# Important Difference From Insert at Bottom

## Insert at Bottom

```text id="8xf37b"
Remove Existing Elements
        ↓
Insert One Target
        ↓
Restore Existing Elements
```

Pattern:

```text id="i9y0mb"
Pop → Recurse → Restore
```

---

## Reverse Stack

```text id="9lf5tq"
Remove Current Element
        ↓
Reverse Remaining Stack
        ↓
Insert Current Element at Bottom
```

Pattern:

```text id="gx2m2m"
Pop → Recurse → Insert at Bottom
```

The reverse operation is built using the Insert-at-Bottom operation.

---

# Common Mistake — Using Normal Append

If we write:

```python id="cah13h"
def reverse(stack):

    if not stack:
        return

    top = stack.pop()

    reverse(stack)

    stack.append(top)
```

the Stack will not reverse.

Why?

Because recursion removes:

```text id="3bqx4v"
50
40
30
20
10
```

and then normal append restores:

```text id="47lnw8"
10
20
30
40
50
```

giving the original Stack again.

The key is:

```text id="gjb6x5"
Do not insert at Top.

Insert at Bottom.
```

---

# Common Mistake — Forgetting to Restore in `insertAtBottom()`

If we forget:

```python id="2s83xi"
stack.append(topE)
```

then the existing elements will be permanently removed.

The helper must follow:

```text id="4msml6"
Save
 ↓
Pop
 ↓
Recurse
 ↓
Restore
```

---

# Common Mistake — Confusing `topElement` and `topE`

In your code:

```python id="28fsw4"
topElement
```

is the element we want to insert at the bottom.

```python id="prvfdc"
topE
```

is an existing element temporarily removed from the Stack.

Think:

```text id="u97kv5"
topElement
    ↓
TARGET element


topE
    ↓
TEMPORARILY removed element
```

The target travels unchanged through all recursive calls.

The temporary elements are restored during backtracking.

---

# Pattern Used

For your DSA pattern sheet, use:

```text id="9clw4e"
Recursion + Insert at Bottom
```

A more descriptive version is:

```text id="c2oyc3"
Pop → Recurse → Insert at Bottom
```

The helper itself uses:

```text id="hq8hrh"
Recursion + Backtracking
```

So the complete pattern is:

```text id="p0e9fd"
Recursion + Backtracking + Insert at Bottom
```

---

# Key Learning

The complete logic is:

```text id="yl1fvg"
reverse(stack)

        ↓

Pop current top

        ↓

Reverse remaining Stack recursively

        ↓

Insert removed element at bottom
```

And:

```text id="xdxf9x"
insertAtBottom(stack, element)

        ↓

Pop everything

        ↓

Reach empty Stack

        ↓

Insert target element

        ↓

Restore everything
```

The most important concepts are:

```text id="wun0ag"
1. Recursion removes elements one by one.

2. The call stack remembers every removed element.

3. The remaining smaller Stack is reversed first.

4. The removed element is inserted at the bottom,
   not pushed normally at the top.

5. insertAtBottom() uses backtracking to restore
   temporarily removed elements.

6. The solution contains recursion inside recursion.

7. Time Complexity is O(n²).

8. Auxiliary Space Complexity is O(n).

9. The problem follows the idea:

   Solve Smaller Problem
          +
   Place Current Element Correctly
```

The strongest mental model is:

```text id="txwstb"
REVERSE STACK
     =
REVERSE SMALLER STACK
     +
INSERT CURRENT TOP AT BOTTOM
```

This is a classic **recursion + backtracking** pattern where a helper recursive operation is used to place each element in its correct reversed position.
