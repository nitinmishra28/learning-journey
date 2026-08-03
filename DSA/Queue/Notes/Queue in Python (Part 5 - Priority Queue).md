# Queue in Python (Part 5 - Priority Queue)

# What is a Priority Queue?

A **Priority Queue** is a special type of queue where elements are removed based on **priority**, **not** on insertion order.

Normal Queue

```text id="w5zcsy"
FIFO

10 → 20 → 30

Output

10
20
30
```

Priority Queue

```text id="5jqtm0"
Elements

30
10
20
```

Output (Min Priority Queue)

```text id="w0o2h5"
10
20
30
```

The smallest element always comes out first.

---

# Why Do We Need a Priority Queue?

Suppose a hospital has patients.

```text id="83j7oq"
Patient A → Normal

Patient B → Critical

Patient C → Moderate
```

Although Patient A arrived first,

Patient B should be treated first.

This cannot be handled by a normal queue.

A Priority Queue solves this problem.

---

# How is Priority Queue Implemented in Python?

Python provides

```python id="u5v3j4"
import heapq
```

The `heapq` module implements a **Min Heap**.

---

# Min Heap

In a Min Heap,

the smallest element always remains at the top.

Example

```text id="zvdupd"
Heap

10

20

30

5
```

Removing elements gives

```text id="5i4rns"
5

10

20

30
```

---

# Creating a Priority Queue

```python id="m20otc"
import heapq

pq = []
```

---

# Insert Element

Use

```python id="ehjk8u"
heapq.heappush()
```

Example

```python id="1is9c6"
import heapq

pq = []

heapq.heappush(pq, 30)
heapq.heappush(pq, 10)
heapq.heappush(pq, 20)

print(pq)
```

Output

```text id="8ppf0i"
[10, 30, 20]
```

Notice

The list is **not sorted**.

It only satisfies the **heap property**.

---

# Remove Highest Priority Element

Use

```python id="zwpcv4"
heapq.heappop()
```

Example

```python id="cnfx2l"
print(heapq.heappop(pq))
```

Output

```text id="5ovp7x"
10
```

The smallest element is always removed first.

---

# Peek Minimum Element

```python id="n1ix1j"
pq[0]
```

Returns

```text id="gw91kq"
Smallest Element
```

without removing it.

---

# Build Heap from Existing List

```python id="40v5y4"
import heapq

nums = [40, 10, 50, 20]

heapq.heapify(nums)

print(nums)
```

Complexity

```text id="ef83bp"
O(n)
```

---

# Max Heap in Python

Python's `heapq` only supports a **Min Heap**.

To simulate a Max Heap,

store negative values.

Example

```python id="xkyhha"
import heapq

pq = []

heapq.heappush(pq, -10)
heapq.heappush(pq, -30)
heapq.heappush(pq, -20)

print(-heapq.heappop(pq))
```

Output

```text id="b6q0wc"
30
```

The largest value comes out first.

---

# Priority Queue vs Normal Queue

| Queue                       | Priority Queue                |
| --------------------------- | ----------------------------- |
| FIFO                        | Based on Priority             |
| First inserted leaves first | Smallest/Largest leaves first |
| deque                       | heapq                         |
| Linear Order                | Heap Order                    |

---

# Common Operations

### Insert

```python id="jlwmfa"
heapq.heappush(heap, value)
```

---

### Remove Minimum

```python id="ecr6h9"
heapq.heappop(heap)
```

---

### Peek Minimum

```python id="e8nsrf"
heap[0]
```

---

### Build Heap

```python id="iow4vb"
heapq.heapify(nums)
```

---

# Common Mistakes

### 1. Thinking the heap is sorted

Wrong

```text id="wjlwm0"
10
20
30
40
```

A heap only guarantees

```text id="mjlwm1"
Parent <= Children
```

It is **not** a sorted array.

---

### 2. Using `sort()` Instead of `heapq`

Sorting after every insertion takes

```text id="jlwm2"
O(n log n)
```

A heap insertion takes

```text id="jlwm3"
O(log n)
```

---

### 3. Forgetting Negative Values for Max Heap

Python has no built-in Max Heap.

Always use

```python id="jlwm4"
-value
```

while inserting.

---

### 4. Calling `heappop()` on an Empty Heap

Always check

```python id="jlwm5"
if heap:
```

before popping.

---

# Complexity

| Operation | Complexity |
| --------- | ---------- |
| heappush  | O(log n)   |
| heappop   | O(log n)   |
| Peek      | O(1)       |
| heapify   | O(n)       |

---

# Applications

Priority Queue is used in:

* Dijkstra's Algorithm
* Prim's Algorithm
* Merge K Sorted Lists
* Top K Frequent Elements
* Kth Largest Element
* Task Scheduling
* Huffman Coding
* Event Simulation

---

# Pattern Recognition

Use a Priority Queue when:

* Smallest/Largest element is repeatedly required.
* Tasks have priorities.
* Need efficient retrieval of min/max.
* Top K problems.
* Scheduling based on priority.

---

# Revision Cheat Sheet

```text id="jlwm6"
Priority Queue

Python

import heapq

Insert

heappush(heap, x)

Remove

heappop(heap)

Peek

heap[0]

Build Heap

heapify(list)

Default

Min Heap

Max Heap

Store negative values

Time

Push → O(log n)

Pop → O(log n)

Peek → O(1)

Heapify → O(n)

Applications

• Dijkstra
• Prim
• Merge K Lists
• Top K Problems
• Scheduling
```
