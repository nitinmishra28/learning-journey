# First Negative Integer in Every Window of Size K

## Problem

Given an array `arr` and a window size `k`, find the **first negative integer** in every window of size `k`.

If a window contains no negative number, return `0`.

### Example

```text
arr = [12, -1, -7, 8, -15, 30, 16]
k = 3
```

Windows:

```text
[12, -1, -7] → -1
[-1, -7, 8]  → -1
[-7, 8, -15] → -7
[8, -15, 30] → -15
[-15, 30,16] → -15
```

Output:

```text
[-1, -1, -7, -15, -15]
```

---

# Pattern

```text
Sliding Window + Queue (Deque)
```

---

# Brute Force

## Idea

For every window:

1. Check all `k` elements.
2. Find the first negative number.
3. If no negative exists, add `0`.

```python
class Solution:
    def firstNegInt(self, arr, k):
        ans = []

        for i in range(len(arr) - k + 1):

            found = 0

            for j in range(i, i + k):
                if arr[j] < 0:
                    found = arr[j]
                    break

            ans.append(found)

        return ans
```

### Complexity

```text
Time  → O(n × k)
Space → O(1) excluding answer
```

The problem is that we repeatedly check the same elements in overlapping windows.

---

# Optimal Approach

Instead of checking every element of every window, maintain the negative elements that are currently inside the window.

Use a queue/deque to store their **indices**.

---

# Why Are We Storing Indices?

This is one of the most important things to remember.

We could store the negative value:

```python
q.append(arr[i])
```

But we don't just need to know **which negative number** it is.

We also need to know:

> **Is this negative number still inside the current window?**

For that, we need its position.

So we store:

```python
q.append(i)
```

where `i` is the index.

Then we can get the actual value using:

```python
arr[q[0]]
```

### Important Pattern

```text
Queue stores → INDEX
Array gives  → VALUE
```

Example:

```text
arr = [12, -1, -7, 8]

Queue:
[1, 2]

arr[1] → -1
arr[2] → -7
```

This allows us to:

* Know the negative value.
* Know where it is.
* Check whether it is still inside the current window.

---

# Main Idea

For every index `i`:

### Step 1: Add Current Negative

If current element is negative:

```python
if arr[i] < 0:
    q.append(i)
```

We store its **index**, not its value.

---

### Step 2: Remove Expired Negative

The current window has size `k`.

For index `i`, the current window is:

```text
[i-k+1, i]
```

So any index smaller than:

```text
i-k+1
```

is outside the window.

The condition

```python
q[0] <= i - k
```

means:

```text
This negative element is outside the current window.
```

Therefore:

```python
q.popleft()
```

removes it.

---

# Why `i - k`?

This is the part you should remember carefully.

Suppose:

```text
i = 4
k = 3
```

Current window is:

```text
[i-k+1, i]

[4-3+1, 4]

[2, 4]
```

So valid indices are:

```text
2, 3, 4
```

Any index:

```text
<= 1
```

is outside the window.

And:

```text
i-k = 4-3 = 1
```

Therefore:

```python
q[0] <= i - k
```

means the index is outside the current window.

### Equivalent way to think about it

```text
Window starts at:

i - k + 1

If:

index < i - k + 1

then it has expired.
```

Which is exactly the same as:

```python
index <= i - k
```

---

# Why Remove Before Adding the Answer?

This is **very important**.

The queue may contain a negative element that belonged to the previous window but has now gone outside the current window.

We must remove expired indices **before** using:

```python
q[0]
```

as the answer.

Otherwise, we may return a negative number that is no longer inside the current window.

### Example

```text
arr = [1, -2, 3]
k = 2
```

For the first window:

```text
[1, -2]
```

answer:

```text
-2
```

Now move to the next window:

```text
[-2, 3]
```

Here `-2` is still valid.

But consider:

```text
arr = [-2, 1, 3]
k = 2
```

First window:

```text
[-2, 1]
```

answer:

```text
-2
```

Next window:

```text
[1, 3]
```

`-2` is now outside.

If we don't remove it first, we might incorrectly return:

```text
-2
```

But the correct answer is:

```text
0
```

Therefore the order is:

```text
1. Add current negative index
2. Remove expired indices
3. Check if window is complete
4. Generate answer
```

---

# Optimal Code

```python
from collections import deque

class Solution:
    def firstNegInt(self, arr, k):
        q = deque()
        ans = []

        for i in range(len(arr)):

            # Store index of negative element
            if arr[i] < 0:
                q.append(i)

            # Remove negative elements
            # that are outside the current window
            if q and q[0] <= i - k:
                q.popleft()

            # Window is complete
            if i >= k - 1:

                # Front contains the first negative
                # because indices are stored in increasing order
                if q:
                    ans.append(arr[q[0]])
                else:
                    ans.append(0)

        return ans
```

---

# Why Does `q[0]` Give the First Negative?

We traverse the array from **left to right**.

Therefore, negative indices are inserted in increasing order.

Example:

```text
Negative indices:

1 → 2 → 4
```

Queue:

```text
front
 ↓
1  2  4
```

Index `1` is the leftmost negative element.

Therefore:

```python
arr[q[0]]
```

is the **first negative element in the current window**.

---

# Why Use a Queue?

We need the negative elements in the same order in which they appeared.

The first negative should leave first when it goes outside the window.

That is exactly **FIFO** behavior.

```text
First negative added
        ↓
First negative removed
```

Therefore a queue/deque fits naturally.

---

# Dry Run

```text
arr = [12, -1, -7, 8, -15, 30, 16]
k = 3
```

### `i = 0`

```text
12
```

Not negative.

Window not complete.

```text
q = []
```

---

### `i = 1`

```text
-1
```

Negative:

```text
q = [1]
```

Window not complete.

---

### `i = 2`

```text
-7
```

Negative:

```text
q = [1, 2]
```

Window:

```text
[12, -1, -7]
```

First negative:

```text
arr[q[0]]
= arr[1]
= -1
```

Answer:

```text
[-1]
```

---

### `i = 3`

Current:

```text
8
```

Not negative.

Check expired:

```text
q[0] <= i-k

1 <= 3-3

1 <= 0 → False
```

So queue remains:

```text
[1, 2]
```

Current window:

```text
[-1, -7, 8]
```

First negative:

```text
arr[1] = -1
```

Answer:

```text
[-1, -1]
```

---

### `i = 4`

Current:

```text
-15
```

Add its index:

```text
q = [1, 2, 4]
```

Check expired:

```text
q[0] <= i-k

1 <= 4-3

1 <= 1 → True
```

So remove index `1`:

```text
q = [2, 4]
```

Current window:

```text
[-7, 8, -15]
```

First negative:

```text
arr[2] = -7
```

Answer:

```text
[-1, -1, -7]
```

---

# The 3-Step Sliding Window Process

This is the exact process shown in your notes and is worth remembering:

```text
        Sliding Window
              ↓
        ┌─────────────┐
        │             │
        ↓             ↓
     1) Process    2) Remove
        current       expired
        element       elements
              ↓
        3) Generate Answer
```

For this problem:

```text
1. Process current element
       ↓
   If negative → store index

2. Remove expired index
       ↓
   q[0] <= i-k

3. Generate answer
       ↓
   q[0] → first negative
```

### Important

The exact order matters:

```text
Process → Remove → Answer
```

---

# Common Mistakes

### 1. Storing Values Instead of Indices

❌

```python
q.append(arr[i])
```

✅

```python
q.append(i)
```

Because we need to know when the element leaves the window.

---

### 2. Using `i-k+1` Incorrectly

The condition can be written as:

```python
q[0] < i - k + 1
```

or equivalently:

```python
q[0] <= i - k
```

The code uses:

```python
q[0] <= i - k
```

---

### 3. Generating Answer Before Removing Expired Elements

❌ Wrong order:

```text
Answer
↓
Remove expired
```

An expired negative might incorrectly become the answer.

Correct:

```text
Add current
↓
Remove expired
↓
Answer
```

---

### 4. Generating Answer Before Window Is Complete

For the first `k-1` elements, there isn't a complete window yet.

Therefore:

```python
if i >= k - 1:
```

is used.

---

### 5. Using `q.popleft()` Without Checking

Use:

```python
if q and q[0] <= i - k:
    q.popleft()
```

so we don't remove from an empty queue.

---

# Complexity

Each negative index is:

* Added once.
* Removed at most once.

Therefore:

```text
Time  → O(n)
Space → O(n)
```

Even though there is a `while`/queue operation pattern in sliding-window problems, every element is processed only a constant number of times.

---

# Brute Force vs Optimal

| Approach               | Time     | Space |
| ---------------------- | -------- | ----- |
| Brute Force            | O(n × k) | O(1)  |
| Queue + Sliding Window | O(n)     | O(n)  |

---

# Pattern Recognition

Whenever you see:

```text
Every window of size K
```

think:

```text
Sliding Window
```

Then ask:

```text
What information do I need from the window?
```

For this problem:

```text
First Negative
```

So maintain:

```text
Queue of negative indices
```

---

# Revision Cheat Sheet

```text
Problem:
First Negative Integer in Every Window of Size K

Pattern:
Sliding Window + Queue

Store:
INDEX, not VALUE

Why index?
To know whether the element
is still inside the current window.

Window:
[i-k+1, i]

Expired:
index < i-k+1

Equivalent:
index <= i-k

Process:
1. If current element is negative:
      q.append(i)

2. Remove expired:
      if q[0] <= i-k:
          q.popleft()

3. If window is complete:
      if q:
          answer = arr[q[0]]
      else:
          answer = 0

Why q[0]?
Negative indices are stored
from left to right, so q[0]
is the first negative.

Important Order:
Process → Remove → Answer

Time:
O(n)

Space:
O(n)
```

### One-Line Pattern

```text
Sliding Window → store useful element indices → remove expired indices → use front for the answer.
```
