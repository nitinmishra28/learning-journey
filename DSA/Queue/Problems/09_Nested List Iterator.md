# Nested List Iterator

## Problem

Given a nested list containing integers and other nested lists, return all integers in their original **left-to-right order**.

### Example

```text
Input:
[1,[4,[6]]]

Output:
1 4 6
```

---

# Pattern

```text
Stack + Nested List Traversal
```

---

# Why Do We Use a Stack?

The main reason is **LIFO (Last In, First Out)**.

When we encounter a nested list, we need to process the nested list before moving to the elements that come after it.

Example:

```text
[1,[2,3],4]

Required order:
1 → 2 → 3 → 4
```

A stack naturally supports this because the last added element is processed first.

But Python's:

```python
stack.pop()
```

removes from the **right side**.

If we push:

```text
1 2 3
```

then:

```text
pop() → 3
```

But we need:

```text
1 → 2 → 3
```

So we push elements in **reverse order**:

```text
Original:
1 2 3

Push:
3 2 1

Pop:
1 2 3
```

### Important Rule

```text
Stack = LIFO
pop() = removes from right
Therefore = reverse before pushing
```

---

# Why Are We Not Storing Indices?

In some stack problems, we store indices because we need to calculate:

```text
distance
window boundaries
previous/next elements
```

Here we don't need any of these.

We only need to maintain the order of:

```text
Integer / Nested List
```

So we directly store the elements in the stack.

---

# Main Idea

The stack can contain two types of elements:

```text
1. Integer
2. Nested List
```

For the element at the top:

### If it is an Integer

We are ready to return it.

### If it is a List

We need to expand it:

```text
Remove list
    ↓
Get its elements
    ↓
Reverse them
    ↓
Push them into stack
    ↓
Continue
```

The important condition is:

```text
Top of stack = next element to process
```

---

# Why Reverse the Initial List?

Suppose:

```text
nestedList = [1,[2,3],4]
```

If we directly store it:

```python
self.stack = nestedList
```

then:

```python
self.stack.pop()
```

returns:

```text
4
```

But we need:

```text
1
```

first.

So:

```python
self.stack = nestedList[::-1]
```

becomes:

```text
[4,[2,3],1]
```

Now:

```python
self.stack.pop()
```

returns:

```text
1
```

which is correct.

---

# `[::-1]` Reminder

```python
arr[::-1]
```

means reverse the list.

Example:

```python
[1,2,3][::-1]
```

Output:

```text
[3,2,1]
```

The `-1` means:

```text
Move from right → left
```

---

# Code

```python
class NestedIterator:

    def __init__(self, nestedList):
        # pop() removes from the right.
        # Reverse so the original first element
        # comes out first.
        self.stack = nestedList[::-1]

    def next(self):
        # Make sure the top is an integer
        self.hasNext()

        # Remove and return the integer
        return self.stack.pop().getInteger()

    def hasNext(self):

        while self.stack:

            # Top is already an integer
            if self.stack[-1].isInteger():
                return True

            # Top is a nested list
            nested_list = self.stack.pop().getList()

            # Reverse because stack follows LIFO
            for item in nested_list[::-1]:
                self.stack.append(item)

        return False
```

---

# Understanding `hasNext()`

`hasNext()` keeps expanding nested lists until an integer reaches the top.

### Case 1: Top is an Integer

```text
Stack:

[5,[6,7]]
 ↑
top
```

The top is `5`.

So:

```python
self.stack[-1].isInteger()
```

returns `True`.

Therefore:

```python
return True
```

---

### Case 2: Top is a List

```text
Stack:

[[4,5],6]
 ↑
top
```

The top is a list.

Remove it:

```python
nested_list = self.stack.pop().getList()
```

Now:

```text
nested_list = [4,5]
```

Reverse it:

```text
[5,4]
```

Push it:

```text
Stack:

4
5
6
```

Now `4` is at the top and will be processed first.

---

# Why `while` Instead of `if`?

Nested lists can have multiple levels.

Example:

```text
[[[1]]]
```

We need:

```text
[[[1]]]
   ↓
[[1]]
   ↓
[1]
   ↓
1
```

Therefore:

```python
while self.stack:
```

is required.

It keeps expanding until:

```text
Integer reaches the top
```

or:

```text
Stack becomes empty
```

---

# Why Does `next()` Call `hasNext()`?

`next()` expects an integer:

```python
self.stack.pop().getInteger()
```

But the top of the stack might currently be a nested list.

So:

```python
self.hasNext()
```

first prepares the stack.

Flow:

```text
next()
  ↓
hasNext()
  ↓
Expand nested lists
  ↓
Integer reaches top
  ↓
pop() integer
```

---

# Dry Run

Consider:

```text
nestedList = [1,[2,[3,4]],5]
```

### Step 1: Initial Stack

Reverse the outer list:

```text
[5,[2,[3,4]],1]
```

Top:

```text
1
```

So:

```text
next() → 1
```

### Step 2: Expand `[2,[3,4]]`

Current stack:

```text
[5,[2,[3,4]]]
```

Top is a list.

Reverse its elements:

```text
[[3,4],2]
```

Push them.

Stack becomes:

```text
[5,[3,4],2]
```

So:

```text
next() → 2
```

### Step 3: Expand `[3,4]`

Reverse:

```text
[4,3]
```

Push them.

Now:

```text
next() → 3
next() → 4
next() → 5
```

Final output:

```text
1 2 3 4 5
```

---

# Common Mistakes

## 1. Forgetting to Reverse

Wrong:

```python
for item in nested_list:
    self.stack.append(item)
```

Because the stack is LIFO, the order becomes reversed.

Correct:

```python
for item in nested_list[::-1]:
    self.stack.append(item)
```

---

## 2. Forgetting to Reverse the Initial List

Wrong:

```python
self.stack = nestedList
```

Correct:

```python
self.stack = nestedList[::-1]
```

---

## 3. Using `if` Instead of `while`

Nested lists can have multiple levels.

Use:

```python
while self.stack:
```

so all nested levels can be expanded.

---

## 4. Forgetting That the Stack Contains Two Types

The stack can contain:

```text
Integer
```

or:

```text
Nested List
```

So first check:

```python
self.stack[-1].isInteger()
```

before calling:

```python
getInteger()
```

---

## 5. Thinking Stack Is Used Just Because There Are Brackets

The important reason is:

```text
Nested structure
      ↓
Depth-first processing
      ↓
LIFO behavior
      ↓
Stack
```

The brackets themselves are not the reason.

---

# Complexity

Let `N` be the total number of elements in the nested structure.

```text
Time  → O(N)
Space → O(N)
```

Each element is pushed and popped a limited number of times.

---

# Revision Cheat Sheet

```text
Nested List Iterator

Pattern:
Stack + Nested List Traversal

Why Stack?
Nested structure → process inner/latest structure first
→ LIFO naturally fits.

Python:
pop() → removes from right

Therefore:
Reverse → Push → Pop

Initial:
self.stack = nestedList[::-1]

If top is Integer:
→ return True

If top is List:
→ pop the list
→ get its elements
→ reverse them
→ push them

Why reverse?
Because stack is LIFO.

Why while?
Nested lists can have multiple levels.

next():
→ call hasNext()
→ make sure integer is on top
→ pop integer

Important:
Top of stack = next element to process

Time:
O(N)

Space:
O(N)
```

---

# One-Line Pattern

```text
Nested List → Stack for LIFO traversal → reverse before pushing → pop in original left-to-right order.
```