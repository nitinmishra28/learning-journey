# Reverse a Queue

## Problem

Given a Queue, reverse all its elements.

Example:

```text
Input:
1 2 3 4

Output:
4 3 2 1
```

Queue follows FIFO, but we need to reverse its order.

---

# Pattern

```text
Queue + Recursion
```

Alternative:

```text
Queue + Stack
```

---

# Approach 1: Using Stack

## Idea

Use a stack to temporarily store all queue elements.

### Steps

1. Remove every element from the queue.
2. Push each element into the stack.
3. Pop from the stack and put it back into the queue.
4. Since Stack follows LIFO, the queue becomes reversed.

```text
Queue:
1 2 3 4

↓

Stack:
1
2
3
4

↓

Pop from Stack:

4
3
2
1

↓

Queue:
4 3 2 1
```

## Code

```python
from collections import deque

def getReversed(q):
    stack = []

    # Move Queue → Stack
    while q:
        stack.append(q.popleft())

    # Move Stack → Queue
    while stack:
        q.append(stack.pop())
```

---

# Approach 2: Using Recursion ⭐

## Idea

Instead of using an explicit stack, recursion itself behaves like a stack.

For every recursive call:

1. Remove the front element.
2. Recursively reverse the remaining queue.
3. Add the removed element to the rear.

```python
from collections import deque

def newGetReversed(q):

    # Base case
    if len(q) == 0:
        return

    # Remove front element
    element = q.popleft()

    # Reverse remaining queue
    newGetReversed(q)

    # Add removed element at the rear
    q.append(element)
```

---

# How Recursion Reverses the Queue

Suppose:

```text
Queue = 1 2 3 4
```

### Recursive Calls

```text
Remove 1
Queue = 2 3 4

Remove 2
Queue = 3 4

Remove 3
Queue = 4

Remove 4
Queue = empty
```

Now recursion starts returning.

### Returning from recursion

```text
Append 4
Queue = 4

Append 3
Queue = 4 3

Append 2
Queue = 4 3 2

Append 1
Queue = 4 3 2 1
```

So the queue is reversed.

---

# Complete Code

```python
from collections import deque

q = deque()


def newGetReversed(q):

    # Base case
    if len(q) == 0:
        return

    # Remove front element
    element = q.popleft()

    # Reverse remaining queue
    newGetReversed(q)

    # Add removed element at rear
    q.append(element)


q.append(1)
q.append(2)
q.append(3)
q.append(4)

newGetReversed(q)

while q:
    print(q.popleft())
```

Output:

```text
4
3
2
1
```

---

# Important Concept

The key idea is:

```text
Remove Front
      ↓
Recursive Call
      ↓
Add Removed Element at Rear
```

The **recursive call happens before `append()`**.

This is important.

If we append before recursion, the queue will not be reversed correctly.

---

# Why Does Recursion Work Like a Stack?

When we call:

```python
newGetReversed(q)
```

the current function call is paused.

Each call remembers its own:

```text
element
```

Example:

```text
Call 1 → remembers 1
Call 2 → remembers 2
Call 3 → remembers 3
Call 4 → remembers 4
```

The last call finishes first:

```text
4 → 3 → 2 → 1
```

This is exactly **LIFO**, the same behavior as a stack.

---

# Common Mistakes

### 1. Appending Before Recursion

❌ Wrong:

```python
q.append(element)
newGetReversed(q)
```

Correct:

```python
newGetReversed(q)
q.append(element)
```

The append must happen while recursion is **returning**.

---

### 2. Forgetting the Base Case

Always stop when:

```python
if len(q) == 0:
    return
```

Otherwise recursion never stops.

---

### 3. Using `pop()` Instead of `popleft()`

Queue removal happens from the front:

```python
q.popleft()
```

`pop()` removes from the rear and changes the behavior.

---

# Complexity

Let `n` be the number of queue elements.

### Recursion

* **Time:** `O(n)`
* **Space:** `O(n)` recursion call stack

### Stack Approach

* **Time:** `O(n)`
* **Space:** `O(n)` explicit stack

---

# Revision Cheat Sheet

```text
Problem:
Reverse a Queue

Pattern:
Queue + Recursion

Recursive Logic:

1. Remove front element.
2. Recursively reverse remaining queue.
3. Append removed element at rear.

Base Case:
Queue empty → return

Example:

1 2 3 4

Remove → 1
Remove → 2
Remove → 3
Remove → 4

Return:

4
3
2
1

Complexity:
Time  → O(n)
Space → O(n)

Alternative:
Queue → Stack → Queue
```

## One-Line Pattern

```text
Remove front → recurse on remaining queue → append removed element on return.
```
