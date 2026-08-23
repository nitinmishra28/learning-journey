# Find the Winner of the Circular Game

## Problem

There are `n` friends standing in a circle:

```text
1, 2, 3, ..., n
```

Starting from friend `1`, count `k` friends and eliminate the `k-th` friend.

Continue until only one friend remains.

Return the number of the winning friend.

### Example

```text
n = 5
k = 2
```

The elimination order is:

```text
2 → 4 → 1 → 5
```

Winner:

```text
3
```

---

# Pattern

```text
Circular Queue + Josephus Problem
```

There are two approaches:

```text
1. Queue Simulation
2. Josephus Mathematical Recurrence
```

---

# Approach 1: Queue Simulation

## Main Idea

Use `deque` to represent the circular game:

```python
q = deque(range(1, n + 1))
```

For:

```text
n = 5
```

the queue is:

```text
[1, 2, 3, 4, 5]
```

Instead of actually moving around a circle, we move the front element to the back.

```python
q.append(q.popleft())
```

Example:

```text
[1, 2, 3, 4, 5]
```

Move `1` to the back:

```text
[2, 3, 4, 5, 1]
```

This simulates moving to the next person in the circle.

---

# Why `k - 1` Rotations?

Suppose:

```text
k = 3
```

We need to remove the 3rd person.

Starting with:

```text
[1, 2, 3, 4, 5]
```

Move the first person:

```text
[2, 3, 4, 5, 1]
```

Move the second person:

```text
[3, 4, 5, 1, 2]
```

Now `3` is at the front.

`3` is the 3rd person, so we remove it:

```python
q.popleft()
```

Therefore:

```python
for _ in range(k - 1):
    q.append(q.popleft())

q.popleft()
```

means:

```text
Move k-1 people to the back
        ↓
The kth person reaches the front
        ↓
Remove the kth person
```

---

# Queue Simulation Code

```python
from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        q = deque(range(1, n + 1))

        while len(q) > 1:

            # Move k-1 people to the back
            for _ in range(k - 1):
                q.append(q.popleft())

            # Remove kth person
            q.popleft()

        return q[0]
```

---

# Dry Run

```text
n = 5
k = 2
```

Initial:

```text
[1, 2, 3, 4, 5]
```

### Round 1

Move `k-1 = 1` person:

```text
1 → back
```

Queue:

```text
[2, 3, 4, 5, 1]
```

Remove front:

```text
2
```

Remaining:

```text
[3, 4, 5, 1]
```

---

### Round 2

Move:

```text
3 → back
```

Queue:

```text
[4, 5, 1, 3]
```

Remove:

```text
4
```

Remaining:

```text
[5, 1, 3]
```

---

### Round 3

Move:

```text
5 → back
```

Queue:

```text
[1, 3, 5]
```

Remove:

```text
1
```

Remaining:

```text
[3, 5]
```

---

### Round 4

Move:

```text
3 → back
```

Queue:

```text
[5, 3]
```

Remove:

```text
5
```

Remaining:

```text
[3]
```

Winner:

```text
3
```

---

# Approach 2: Josephus Mathematical Recurrence

The queue solution simulates every elimination.

We can solve the problem more efficiently using the **Josephus recurrence**.

The key formula is:

```python
winner = (winner + k) % size
```

---

# Why Start With `winner = 0`?

The mathematical solution uses **0-based indexing**.

For one person:

```text
index: 0
```

The winner is obviously:

```python
winner = 0
```

This is the base case.

Then we gradually increase the circle size.

---

# How the Formula Works

Suppose we already know the winner's position for a smaller circle.

When we add one more person, the elimination position shifts by `k`.

Therefore:

```python
winner = (winner + k) % size
```

The modulo keeps the index inside:

```text
0 ... size - 1
```

Because the people are arranged in a circle.

---

# Mathematical Solution Code

```python
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        winner = 0

        for size in range(2, n + 1):
            winner = (winner + k) % size

        # Convert 0-based index to 1-based friend number
        return winner + 1
```

---

# Dry Run of Mathematical Approach

Take:

```text
n = 5
k = 2
```

Start:

```text
winner = 0
```

### Size = 2

```text
winner = (0 + 2) % 2
       = 0
```

### Size = 3

```text
winner = (0 + 2) % 3
       = 2
```

### Size = 4

```text
winner = (2 + 2) % 4
       = 0
```

### Size = 5

```text
winner = (0 + 2) % 5
       = 2
```

Final 0-based index:

```text
2
```

Convert to friend number:

```text
2 + 1 = 3
```

Answer:

```text
3
```

---

# Why `winner + 1`?

The mathematical formula uses:

```text
0-based indexing
```

But the problem numbers friends from:

```text
1 to n
```

Therefore:

```python
return winner + 1
```

converts:

```text
0 → 1
1 → 2
2 → 3
...
```

---

# Queue vs Mathematical Approach

| Approach | Idea | Time | Space |
|---|---|---:|---:|
| Queue Simulation | Simulate every elimination | `O(n × k)` | `O(n)` |
| Josephus | Calculate winner position | `O(n)` | `O(1)` |

The queue approach is easier to understand and visualize.

The Josephus approach is more optimized.

---

# Common Mistakes

## 1. Using `k` Instead of `k - 1`

Wrong:

```python
for _ in range(k):
    q.append(q.popleft())

q.popleft()
```

Correct:

```python
for _ in range(k - 1):
    q.append(q.popleft())

q.popleft()
```

Why?

Because after moving `k - 1` people, the `k-th` person is at the front.

---

## 2. Forgetting the Circular Nature

After reaching the last person, counting continues from the first person.

The queue handles this naturally:

```python
q.append(q.popleft())
```

The front person goes to the back.

---

## 3. Forgetting 0-Based Indexing

The Josephus formula returns a:

```text
0-based index
```

Therefore:

```python
return winner + 1
```

is required.

---

# Complexity

## Queue Simulation

```text
Time  → O(n × k)
Space → O(n)
```

## Josephus

```text
Time  → O(n)
Space → O(1)
```

---

# Revision Cheat Sheet

```text
Find the Winner of the Circular Game

Pattern:
Circular Queue / Josephus Problem

Queue Approach:

q = deque(1 ... n)

Repeat until one person remains:

1. Move k-1 people from front to back.
2. Remove the kth person.

Code:

for _ in range(k - 1):
    q.append(q.popleft())

q.popleft()

Why k-1?

After moving k-1 people,
the kth person comes to the front.

--------------------------------------------------

Josephus Approach:

winner = 0

for size in range(2, n + 1):
    winner = (winner + k) % size

return winner + 1

Why +1?

Formula uses 0-based indexing,
but friends are numbered 1 to n.

Complexity:

Queue:
Time  → O(n × k)
Space → O(n)

Josephus:
Time  → O(n)
Space → O(1)
```

---

# One-Line Pattern

```text
Circular elimination → move k-1 elements and pop using a queue, or use the Josephus recurrence: (winner + k) % size.
```