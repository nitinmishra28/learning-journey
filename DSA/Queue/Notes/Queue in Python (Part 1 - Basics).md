# Queue in Python (Part 1 - Basics)

# What is a Queue?

A **Queue** is a linear data structure that follows the **FIFO (First In First Out)** principle.

This means:

> The element inserted **first** is removed **first**.

Example:

```text
Queue

Front                          Rear
 ↓                              ↓
+----+----+----+----+
| 10 | 20 | 30 | 40 |
+----+----+----+----+

Remove → 10
```

After removing:

```text
Front                     Rear
 ↓                         ↓
+----+----+----+
| 20 | 30 | 40 |
+----+----+----+
```

---

# FIFO Principle

FIFO stands for

```text
First In First Out
```

Example

```text
Insert Order

10
20
30
40
```

Removal Order

```text
10
20
30
40
```

The first inserted element always leaves first.

---

# Real Life Examples

### 1. Ticket Counter

```text
Person A

↓

Person B

↓

Person C
```

Service Order

```text
A

↓

B

↓

C
```

---

### 2. Printer Queue

```text
Print File1

↓

Print File2

↓

Print File3
```

Printing Order

```text
File1

↓

File2

↓

File3
```

---

### 3. Food Order Queue

The customer who orders first receives the food first.

---

### 4. CPU Scheduling

Processes waiting for execution are often managed using queues.

---

### 5. BFS (Breadth First Search)

The queue processes nodes level by level.

---

# Queue Terminology

```text
Front
```

The first element of the queue.

Removal always happens from the front.

---

```text
Rear
```

The last element of the queue.

Insertion always happens at the rear.

Example

```text
Front                   Rear
 ↓                       ↓

10 20 30 40
```

---

# Queue Operations

## 1. Enqueue

Insert an element into the queue.

```text
Before

10 20 30

↓

Enqueue(40)

↓

10 20 30 40
```

---

## 2. Dequeue

Remove the front element.

```text
Before

10 20 30 40

↓

Dequeue()

↓

20 30 40
```

---

## 3. Front / Peek

Returns the front element without removing it.

Example

```text
Queue

10 20 30

Peek()

↓

10
```

Queue remains unchanged.

---

## 4. Rear

Returns the last element.

Example

```text
Queue

10 20 30

Rear()

↓

30
```

---

## 5. isEmpty()

Checks whether the queue is empty.

```python
if len(queue) == 0:
    print("Empty")
```

---

## 6. Size

Returns the number of elements.

```python
len(queue)
```

---

# Queue vs Stack

| Queue             | Stack        |
| ----------------- | ------------ |
| FIFO              | LIFO         |
| Insert from Rear  | Push on Top  |
| Remove from Front | Pop from Top |
| Used in BFS       | Used in DFS  |
| Printer Queue     | Undo/Redo    |

---

# Time Complexity (Ideal Queue)

| Operation | Complexity |
| --------- | ---------- |
| Enqueue   | O(1)       |
| Dequeue   | O(1)       |
| Front     | O(1)       |
| Rear      | O(1)       |
| isEmpty   | O(1)       |
| Size      | O(1)       |

---

# Why Not Use a Python List as a Queue?

Many beginners write:

```python
queue = []

queue.append(10)
queue.append(20)
queue.append(30)

queue.pop(0)
```

Although this works,

```python
pop(0)
```

is **O(n)**.

Why?

After removing the first element,

every remaining element shifts one position to the left.

Example

```text
Before

10 20 30 40

↓

pop(0)

↓

20 30 40
```

All elements shift.

Therefore,

```python
list.pop(0)
```

is inefficient for queues.

---

# Recommended Queue in Python

Python provides

```python
from collections import deque
```

A `deque` (Double Ended Queue) allows:

* O(1) insertion at both ends.
* O(1) deletion at both ends.

This is the preferred implementation for almost all DSA problems.

We'll study it in the next README.

---

# Where Are Queues Used?

Queues are commonly used in:

* Breadth First Search (BFS)
* Level Order Traversal
* Task Scheduling
* CPU Scheduling
* Printer Queue
* Call Center Systems
* Message Queues
* Network Packet Processing
* Producer Consumer Problems
* Sliding Window Problems
* Cache Systems

---

# Common Mistakes

### 1. Using `list.pop(0)`

❌ Slow (`O(n)`)

Use `deque.popleft()` instead.

---

### 2. Confusing Stack and Queue

Remember:

```text
Stack

Last In → First Out
```

```text
Queue

First In → First Out
```

---

### 3. Mixing Front and Rear

Insertion always happens at the **Rear**.

Removal always happens from the **Front**.

---

# Pattern Recognition

Whenever you see:

* Level-by-level traversal
* First come first serve
* Scheduling
* Buffer processing
* Waiting line
* BFS

Think of a **Queue**.

---

# Revision Cheat Sheet

```text
Queue

FIFO (First In First Out)

Insertion  → Rear
Removal    → Front

Operations

Enqueue
Dequeue
Front
Rear
isEmpty
Size

Python

❌ list.pop(0)

✅ collections.deque

Applications

• BFS
• Level Order Traversal
• Scheduling
• Producer Consumer
• Sliding Window

Time Complexity

Enqueue → O(1)
Dequeue → O(1)
Front → O(1)
Rear → O(1)
```
