# Number of Recent Calls

## Problem

You are given a `RecentCounter` class that counts how many requests happened in the **last 3000 milliseconds**.

For every:

```python
ping(t)
```

a new request happens at time `t`.

We need to count requests whose time lies in:

```text
[t - 3000, t]
```

### Example

```text
ping(1)     → 1
ping(100)   → 2
ping(3001)  → 3
ping(3002)  → 3
```

For:

```text
ping(3002)
```

the valid range is:

```text
[2, 3002]
```

So the request at `1` is removed.

---

# Pattern

```text
Queue + Sliding Window
```

---

# Why Do We Use a Queue?

Requests arrive in **increasing order of time**.

Example:

```text
1 → 100 → 3001 → 3002
```

The oldest request is always at the **front** of the queue.

We need to remove old requests from the front:

```python
popleft()
```

and add new requests at the back:

```python
append(t)
```

This is exactly Queue behavior:

```text
First In → First Out
```

So we use:

```python
deque()
```

---

# Main Idea

For every new request at time:

```text
t
```

the valid time range is:

```text
[t - 3000, t]
```

Any request before:

```text
t - 3000
```

is too old and must be removed.

So:

```python
while self.q and self.q[0] < t - 3000:
    self.q.popleft()
```

After removing all old requests:

```python
self.q.append(t)
```

Then:

```python
len(self.q)
```

gives the number of requests inside the current 3000ms window.

---

# Why `< t - 3000` and Not `<=`?

This is very important.

The valid range is:

```text
[t - 3000, t]
```

Both endpoints are included.

Suppose:

```text
t = 3000
```

Then the valid range is:

```text
[0, 3000]
```

A request at:

```text
0
```

is still valid because:

```text
3000 - 0 = 3000
```

So we should **not remove** it.

Therefore we remove only:

```text
time < t - 3000
```

not:

```text
time <= t - 3000
```

---

# Why Remove Before Adding `t`?

The new request at time `t` is obviously valid.

We first remove all requests that are too old:

```python
while self.q and self.q[0] < t - 3000:
    self.q.popleft()
```

Then add the current request:

```python
self.q.append(t)
```

Finally:

```python
return len(self.q)
```

This ensures the queue contains **only valid requests**.

---

# Why Can We Check Only `q[0]`?

Because requests arrive in increasing order.

Example:

```text
q = [1, 100, 500, 2000]
```

The queue is sorted by time.

If:

```text
q[0]
```

is still valid, then every request after it is also valid.

If:

```text
q[0] < t - 3000
```

then it is too old.

We remove it:

```python
popleft()
```

and check the next oldest request.

That's why:

```python
while
```

is used.

---

# Code

```python
from collections import deque


class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:

        # Remove requests outside the 3000ms window
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()

        # Add current request
        self.q.append(t)

        # Number of requests in the current window
        return len(self.q)
```

---

# Dry Run

Consider:

```text
ping(1)
ping(100)
ping(3001)
ping(3002)
```

### `ping(1)`

Window:

```text
[-2999, 1]
```

Queue is empty.

Add:

```text
[1]
```

Answer:

```text
1
```

---

### `ping(100)`

Window:

```text
[-2900, 100]
```

`1` is valid.

Add:

```text
[1,100]
```

Answer:

```text
2
```

---

### `ping(3001)`

Window:

```text
[1,3001]
```

Check oldest:

```text
1 < 1
```

False.

So `1` is still valid.

Add:

```text
[1,100,3001]
```

Answer:

```text
3
```

---

### `ping(3002)`

Window:

```text
[2,3002]
```

Check:

```text
1 < 2
```

True.

Remove:

```text
[100,3001]
```

Add `3002`:

```text
[100,3001,3002]
```

Answer:

```text
3
```

---

# Important Sliding Window Idea

Think of the queue as a moving window:

```text
          3000 ms window
        <---------------->
        [valid requests]
```

When `t` increases:

```text
window moves → right
```

Old requests fall outside the left side.

We remove them:

```python
popleft()
```

New requests enter from the right:

```python
append(t)
```

So:

```text
Queue = Current Sliding Window
```

---

# Why `deque` Instead of List?

We need to remove elements from the front frequently.

With a list:

```python
pop(0)
```

takes:

```text
O(n)
```

because remaining elements need to shift.

With:

```python
deque.popleft()
```

the operation is:

```text
O(1)
```

Therefore `deque` is the correct choice.

---

# Common Mistakes

### 1. Using `<=`

Wrong:

```python
self.q[0] <= t - 3000
```

Because the boundary is valid.

Correct:

```python
self.q[0] < t - 3000
```

---

### 2. Removing Only One Old Request

Wrong:

```python
if self.q and self.q[0] < t - 3000:
    self.q.popleft()
```

There may be multiple old requests.

Example:

```text
q = [1,2,3,1000]
t = 5000
```

We need to remove multiple elements.

Therefore use:

```python
while self.q and self.q[0] < t - 3000:
    self.q.popleft()
```

---

### 3. Counting Before Removing Old Requests

If we do:

```python
self.q.append(t)
return len(self.q)
```

without removing old requests, the answer will include expired requests.

Always:

```text
Remove expired
      ↓
Add current request
      ↓
Return queue size
```

---

# Complexity

Each request is:

```text
added once
removed once
```

Even though there is a `while` loop, an element cannot be removed more than once.

Therefore:

```text
Time  → O(n) total
Space → O(n)
```

For each individual `ping`, the worst-case work can be `O(n)`, but **amortized** time per request is `O(1)`.

---

# Revision Cheat Sheet

```text
Number of Recent Calls

Pattern:
Queue + Sliding Window

Window:
[t - 3000, t]

Queue:
Stores timestamps inside the current window.

For every ping(t):

1. Remove expired timestamps:

   while q and q[0] < t - 3000:
       q.popleft()

2. Add current timestamp:

   q.append(t)

3. Return:

   len(q)

Why Queue?
Oldest request is at the front.

Why deque?
popleft() is O(1).

Why < and not <=?
t - 3000 is still inside the valid range.

Why while?
Multiple old requests may need to be removed.

Key idea:
Queue represents the current sliding window.

Time:
O(n) total / O(1) amortized per ping

Space:
O(n)
```

---

# One-Line Pattern

```text
Queue stores timestamps → remove all timestamps outside [t-3000, t] → add current t → queue size is the answer.
```