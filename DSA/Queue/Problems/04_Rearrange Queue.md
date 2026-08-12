# Rearrange Queue

## Problem

Given a queue containing an **even number of elements**, rearrange it by interleaving the first half with the second half.

Example:

```text
Input:
1 2 3 4

First Half:
1 2

Second Half:
3 4

Output:
1 3 2 4
```

Another example:

```text
Input:
1 2 3 4 5 6

Output:
1 4 2 5 3 6
```

---

# Pattern

```text
Queue + Auxiliary Queue + Interleaving
```

---

# Main Idea

Split the queue into two halves.

For:

```text
1 2 3 4 5 6
```

Split into:

```text
First Half:
1 2 3

Second Half:
4 5 6
```

Store the first half in another queue:

```text
q2 = 1 2 3
```

Original queue:

```text
q = 4 5 6
```

Now repeatedly take:

```text
1 from q2
4 from q

2 from q2
5 from q

3 from q2
6 from q
```

Result:

```text
1 4 2 5 3 6
```

---

# Code

```python
from collections import deque

class Solution:
    def rearrangeQueue(self, q):

        q2 = deque()

        # Get the first half
        half = len(q) // 2

        while half > 0:
            q2.append(q.popleft())
            half -= 1

        # Remaining elements are the second half
        size = len(q)

        while size > 0:

            # Take one from first half
            q.append(q2.popleft())

            # Take one from second half
            q.append(q.popleft())

            size -= 1

        return q
```

---

# Why `len(q) // 2`?

The problem assumes the queue contains an **even number of elements**.

For:

```text
n = 6
```

```python
n // 2
```

gives:

```text
3
```

So:

```text
First Half  → 3 elements
Second Half → 3 elements
```

---

# Why Use `q2`?

After removing the first half from `q`, we need to keep those elements somewhere.

Therefore:

```python
q2 = deque()
```

stores the first half.

Example:

```text
Original q:

1 2 3 4 5 6

        ↓

q2:

1 2 3

q:

4 5 6
```

Now both halves can be accessed independently.

---

# Important Part

This is the core:

```python
q.append(q2.popleft())
q.append(q.popleft())
```

It means:

```text
Take 1st element from first half
        ↓
Add it to result

Take 1st element from second half
        ↓
Add it to result
```

Then repeat.

So the pattern is:

```text
First Half → Second Half
First Half → Second Half
First Half → Second Half
```

---

# Dry Run

Input:

```text
1 2 3 4 5 6
```

### Step 1: Split

```text
q2 = 1 2 3

q = 4 5 6
```

### Step 2: Interleave

First iteration:

```text
Take 1 from q2
Take 4 from q

q = 1 4 5 6
```

Second:

```text
Take 2 from q2
Take 5 from q

q = 1 4 2 5 6
```

Third:

```text
Take 3 from q2
Take 6 from q

q = 1 4 2 5 3 6
```

Final:

```text
1 4 2 5 3 6
```

---

# Common Mistakes

### 1. Taking the wrong half

Remember:

```python
len(q) // 2
```

elements go into `q2`.

---

### 2. Taking two elements from the same queue

Wrong:

```python
q.append(q.popleft())
q.append(q.popleft())
```

This would not interleave the two halves.

Correct:

```python
q.append(q2.popleft())
q.append(q.popleft())
```

---

### 3. Using List `pop(0)`

Avoid:

```python
arr.pop(0)
```

because it takes `O(n)`.

Use:

```python
q.popleft()
```

with `deque`.

---

### 4. Forgetting the Queue Must Be Even

The approach assumes:

```text
len(q) % 2 == 0
```

because both halves must have the same number of elements.

---

# Complexity

Let `n` be the number of elements.

### Time

```text
O(n)
```

Every element is moved a constant number of times.

### Space

```text
O(n)
```

because `q2` stores half of the elements.

---

# Revision Cheat Sheet

```text
Pattern:
Queue + Auxiliary Queue + Interleaving

Steps:

1. Find half = n // 2
2. Move first half → q2
3. q contains second half
4. Take one from q2
5. Take one from q
6. Repeat

Example:

1 2 3 4 5 6

↓

q2 = 1 2 3
q  = 4 5 6

↓

1 4 2 5 3 6

Time  → O(n)
Space → O(n)

Important:
Queue must contain an even number of elements.
```

### One-Line Pattern

```text
Split queue into two halves → take one from each alternately → interleave.
```
