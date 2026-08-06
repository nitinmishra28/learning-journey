# Queue Implementation Using Array

## Problem

Implement a Queue using an array.

Operations supported:

* `enqueue()` → Insert an element.
* `dequeue()` → Remove the front element.
* `isEmpty()` → Check if the queue is empty.
* `isFull()` → Check if the queue is full.

---

# Pattern

```text
Queue Simulation (FIFO)
```

---

# Main Idea

A queue follows the **FIFO (First In First Out)** principle.

* **Insertion** always happens at the **rear**.
* **Deletion** always happens from the **front**.

We maintain two pointers:

* `front` → Points to the first element.
* `rear` → Points to the last element.

Initially,

```text
front = -1
rear = -1
```

which means the queue is empty.

---

# Code

```python
class Queue:

    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.front = -1
        self.rear = -1

    # Check if queue is empty
    def isEmpty(self):
        return self.front == -1

    # Check if queue is full
    def isFull(self):
        return self.rear + 1 == self.size

    # Insert element
    def enqueue(self, val):

        if self.isFull():
            print("Overflow")
            return

        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear += 1

        self.arr[self.rear] = val

    # Remove element
    def dequeue(self):

        if self.isEmpty():
            print("Underflow")
            return None

        value = self.arr[self.front]

        # Queue becomes empty
        if self.front == self.rear:
            self.front = self.rear = -1

        else:
            self.front += 1

        return value
```

---

# Why `front = rear = -1`?

Initially,

```text
Queue

Empty
```

There is no valid index.

So we initialize

```python
front = rear = -1
```

This makes checking an empty queue easy.

---

# Why Set `front = rear = 0` on First Insertion?

Initially,

```text
front = -1
rear = -1
```

Insert

```text
10
```

Now both pointers should point to the first element.

```text
Front
Rear
 ↓
+----+
| 10 |
+----+
```

So,

```python
front = rear = 0
```

---

# Why Increase Only `rear` During Enqueue?

Insertion always happens at the end.

Example

```text
Front          Rear
 ↓              ↓

10 20 30
```

Insert

```text
40
```

Only the rear moves.

```text
Front             Rear
 ↓                 ↓

10 20 30 40
```

---

# Why Increase Only `front` During Dequeue?

Removal always happens from the front.

Example

```text
Front            Rear
 ↓                ↓

10 20 30 40
```

Remove

```text
10
```

Front moves to the next element.

```text
Front         Rear
 ↓             ↓

20 30 40
```

---

# Why Reset Both Pointers?

Suppose the queue has only one element.

```text
Front
Rear
 ↓

10
```

After removing it,

the queue becomes empty.

Therefore,

```python
front = rear = -1
```

Otherwise, the queue would incorrectly appear non-empty.

---

# Dry Run

Queue Size

```text
5
```

### Enqueue

```text
enqueue(10)
enqueue(20)
enqueue(30)
```

State

```text
Front
 ↓

10 20 30
      ↑
     Rear
```

---

### Dequeue

```text
dequeue()
```

Removed

```text
10
```

Queue

```text
Front
 ↓

20 30
   ↑
 Rear
```

---

### Dequeue Again

Removed

```text
20
```

Queue

```text
Front
 ↓

30
↑
Rear
```

---

### Dequeue Again

Removed

```text
30
```

Queue

```text
Empty

front = rear = -1
```

---

# Limitation of This Queue

Suppose the queue size is

```text
5
```

Insert

```text
10
20
30
40
50
```

Now remove

```text
10
20
30
```

Queue becomes

```text
_ _ _ 40 50
```

Although there are empty spaces,

`rear` has already reached the last index.

So,

```text
enqueue(60)
```

gives

```text
Overflow
```

This is called

```text
False Overflow
```

because memory exists but cannot be reused.

This problem is solved by a **Circular Queue**.

---

# Common Mistakes

### 1. Forgetting `return` after Overflow

Wrong

```python
if self.isFull():
    print("Overflow")
```

The function continues and causes an index error.

Correct

```python
if self.isFull():
    print("Overflow")
    return
```

---

### 2. Forgetting `return None` after Underflow

Wrong

```python
if self.isEmpty():
    print("Underflow")
```

The function continues and accesses an invalid index.

Correct

```python
if self.isEmpty():
    print("Underflow")
    return None
```

---

### 3. Not Resetting Pointers

Always reset

```python
front = rear = -1
```

when the last element is removed.

---

### 4. Calling `dequeue()` Instead of `deque()`

The standard queue operation is named

```text
dequeue
```

Your method is named

```python
deque()
```

Consider renaming it to

```python
dequeue()
```

to match standard terminology.

---

# Complexity

| Operation | Time |
| --------- | ---- |
| enqueue   | O(1) |
| dequeue   | O(1) |
| isEmpty   | O(1) |
| isFull    | O(1) |

---

# Pattern Recognition

Use this implementation when:

* Learning queue fundamentals.
* Implementing a queue using an array.
* Understanding `front` and `rear` pointers.

For production code and most Python DSA problems, prefer:

```python
from collections import deque
```

---

# Revision Cheat Sheet

```text
Pattern:
Queue Simulation (FIFO)

Pointers:
front → First element
rear  → Last element

Initially:
front = rear = -1

Enqueue:
Insert at rear

Dequeue:
Remove from front

Queue Empty:
front == -1

Queue Full:
rear + 1 == size

Limitation:
False Overflow

Solution:
Circular Queue

Time:
Enqueue → O(1)
Dequeue → O(1)

Space:
O(n)
``` 
