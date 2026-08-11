# Queue in Python (Part 6 - Monotonic Queue & Queue Patterns)

# What is a Monotonic Queue? 

A **Monotonic Queue** is a deque that always maintains its elements in a specific order.

There are two types:

* **Monotonic Increasing Queue**
* **Monotonic Decreasing Queue**  

Unlike a normal queue, elements that are no longer useful are removed immediately.

---

# Why Do We Need a Monotonic Queue?

Suppose we need the **maximum element** of every sliding window.

Example

```text id="mnq1"
nums = [1,3,-1,-3,5,3,6,7]
k = 3
```

Windows

```text id="mnq2"
[1,3,-1] → 3
[3,-1,-3] → 3
[-1,-3,5] → 5
[-3,5,3] → 5
[5,3,6] → 6
[3,6,7] → 7
```

If we scan every window,

Time becomes

```text id="mnq3"
O(n × k)
```

Using a Monotonic Queue,

it becomes

```text id="mnq4"
O(n)
```

---

# Monotonic Increasing Queue

Elements remain in increasing order.

Example

```text id="mnq5"
1 3 5 8
```

Before inserting a new element,

remove every larger element from the rear.

Used for:

* Sliding Window Minimum

---

# Monotonic Decreasing Queue

Elements remain in decreasing order.

Example

```text id="mnq6"
8 5 3 1
```

Before inserting,

remove every smaller element.

Used for:

* Sliding Window Maximum

---

# Python Example

```python id="mnq7"
from collections import deque

dq = deque()

nums = [1, 3, -1, -3, 5]

for num in nums:

    while dq and dq[-1] < num:
        dq.pop()

    dq.append(num)

print(dq)
```

---

# Why Use deque Instead of Queue?

We need to remove elements from the **rear** while inserting.

Queue cannot do this efficiently.

Deque supports

```text id="mnq8"
append()

appendleft()

pop()

popleft()
```

all in O(1).

Therefore,

Monotonic Queue is always implemented using a **deque**.

---

# Queue vs Deque vs Monotonic Queue

| Feature         | Queue | Deque | Monotonic Queue         |
| --------------- | ----- | ----- | ----------------------- |
| Insert Front    | ❌     | ✅     | ❌                       |
| Insert Rear     | ✅     | ✅     | ✅                       |
| Delete Front    | ✅     | ✅     | ✅                       |
| Delete Rear     | ❌     | ✅     | ✅                       |
| Maintains Order | FIFO  | No    | Increasing / Decreasing |

---

# Which Queue Should I Use?

| Problem                | Data Structure  |
| ---------------------- | --------------- |
| BFS                    | Queue (`deque`) |
| Level Order Traversal  | Queue (`deque`) |
| Producer Consumer      | Queue           |
| Browser History        | Two Stacks      |
| Sliding Window Maximum | Monotonic Queue |
| Sliding Window Minimum | Monotonic Queue |
| Top K Elements         | Priority Queue  |
| Dijkstra               | Priority Queue  |
| Round Robin            | Circular Queue  |

---

# Queue Pattern Recognition

## 1. Normal Queue

Keywords

```text id="mnq9"
FIFO

Level Order

BFS

Waiting Line

Scheduling
```

---

## 2. Circular Queue

Keywords

```text id="mnq10"
Fixed Size

Buffer

Round Robin

Reuse Space
```

---

## 3. Deque

Keywords

```text id="mnq11"
Insert/Delete

Both Ends

Sliding Window

Palindrome
```

---

## 4. Priority Queue

Keywords

```text id="mnq12"
Smallest

Largest

Priority

Top K

Shortest Path
```

---

## 5. Monotonic Queue

Keywords

```text id="mnq13"
Sliding Window Maximum

Sliding Window Minimum

Maintain Max

Maintain Min
```

---

# Common Mistakes

### 1. Using Queue Instead of Deque

Sliding Window problems require deletion from both ends.

Use

```python id="mnq14"
deque
```

---

### 2. Forgetting to Remove Useless Elements

A Monotonic Queue only keeps useful candidates.

Always remove elements that can never become the answer.

---

### 3. Storing Values Instead of Indices

For most sliding window problems,

store **indices**, not values.

This helps identify elements that move out of the current window.

---

# Complexity Summary

| Queue Type      | Insert         | Delete         |
| --------------- | -------------- | -------------- |
| Queue           | O(1)           | O(1)           |
| Circular Queue  | O(1)           | O(1)           |
| Deque           | O(1)           | O(1)           |
| Priority Queue  | O(log n)       | O(log n)       |
| Monotonic Queue | O(1) Amortized | O(1) Amortized |

---

# Interview Decision Tree

```text id="mnq15"
Need FIFO?

↓

Yes

↓

Need Both Ends?

↓

No
↓

Queue


Yes

↓

Need Min/Max?

↓

No
↓

Deque


Yes

↓

Sliding Window?

↓

Yes
↓

Monotonic Queue


Need Priority?

↓

Priority Queue
```

---

# Complete Queue Revision Cheat Sheet

```text id="mnq16"
QUEUE

FIFO

Python

from collections import deque

append()

popleft()

----------------------------------

CIRCULAR QUEUE

Reuse Space

(index + 1) % size

----------------------------------

DEQUE

append()

appendleft()

pop()

popleft()

----------------------------------

PRIORITY QUEUE

import heapq

heappush()

heappop()

heapify()

Default → Min Heap

Max Heap → Negative Values

----------------------------------

MONOTONIC QUEUE

Increasing Queue

→ Sliding Window Minimum

Decreasing Queue

→ Sliding Window Maximum

Store Indices

Time

O(1) Amortized
```

---

# Similar Interview Problems

### Queue

* Implement Queue using Stacks
* Design Circular Queue
* First Non-Repeating Character in a Stream
* Rotten Oranges
* Number of Recent Calls

### Deque

* Sliding Window Maximum
* Sliding Window Minimum
* Shortest Subarray with Sum at Least K

### Priority Queue

* Kth Largest Element
* Top K Frequent Elements
* Merge K Sorted Lists
* Dijkstra's Algorithm
* Find Median from Data Stream

### Monotonic Queue

* Sliding Window Maximum
* Sliding Window Minimum
* Constrained Subsequence Sum
* Jump Game VI
