# Queue in Python (Part 3 - Circular Queue)

# Why Do We Need a Circular Queue?

Suppose we implement a queue using an array of size **5**.

Initially

```text
Front = 0
Rear = 0

+----+----+----+----+----+
|    |    |    |    |    |
+----+----+----+----+----+
```

Insert

```text
10 20 30 40 50
```

```text
Front
 ↓
+----+----+----+----+----+
| 10 | 20 | 30 | 40 | 50 |
+----+----+----+----+----+
                          ↑
                        Rear
```

Now remove three elements.

```text
Remove

10
20
30
```

Queue becomes

```text
          Front
            ↓
+----+----+----+----+----+
|    |    |    | 40 | 50 |
+----+----+----+----+----+
                          ↑
                        Rear
```

Notice something.

The first three positions are empty.

Now suppose we insert

```text
60
```

In a normal array queue,

Rear is already at the last index.

There is no more space.

Although the array has empty cells,

the queue incorrectly reports

```text
Queue Full
```

This is called **False Overflow** (or Wasted Space).

---

# Solution

Instead of stopping at the last index,

move back to the beginning.

```text
0 → 1 → 2 → 3 → 4
↑                 ↓
└─────────────────┘
```

The queue becomes **circular**.

This is called a

```text
Circular Queue
```

---

# How Circular Queue Works

When Rear reaches the last index,

it moves to

```text
0
```

instead of stopping.

Similarly,

Front also wraps around.

We use

```python
(index + 1) % size
```

to move forward.

Example

```python
(4 + 1) % 5
```

Result

```text
0
```

---

# Circular Queue Representation

```text
        0
    +-------+
  4 |       | 1
    |       |
  3 |       | 2
    +-------+
```

After reaching the last position,

we again continue from index

```text
0
```

---

# Circular Queue Implementation (Array)

```python
class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):

        if self.isFull():
            print("Queue Full")
            return

        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value

    def dequeue(self):

        if self.isEmpty():
            print("Queue Empty")
            return None

        value = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1

        else:
            self.front = (self.front + 1) % self.size

        return value
```

---

# Why `(index + 1) % size`?

Suppose

```text
Size = 5
```

Indices

```text
0 1 2 3 4
```

Current Rear

```text
4
```

Next position

```python
(4 + 1) % 5
```

Result

```text
0
```

The pointer comes back to the beginning.

Similarly

```python
(2 + 1) % 5
```

gives

```text
3
```

So this formula works for every position.

---

# How Do We Know Queue is Full?

Condition

```python
(rear + 1) % size == front
```

Example

```text
Size = 5

Front = 2

Rear = 1
```

Visual

```text
      F
      ↓
0 1 2 3 4
↑
R
```

Rear's next position becomes

```text
2
```

which is already occupied by Front.

Hence,

the queue is full.

---

# How Do We Know Queue is Empty?

When both pointers become

```text
-1
```

```python
front == -1
```

means

```text
Queue Empty
```

---

# Dry Run

Queue Size

```text
5
```

### Enqueue

```text
10
20
30
40
50
```

```text
Front = 0

Rear = 4
```

Now

```text
Dequeue()

↓

10

↓

20
```

Queue

```text
_ _ 30 40 50
```

Front

```text
2
```

Rear

```text
4
```

Now

```text
Enqueue(60)
```

Rear becomes

```python
(4+1)%5
```

```text
0
```

Queue

```text
60 _ 30 40 50
```

Next

```text
Enqueue(70)
```

Rear

```python
(0+1)%5
```

```text
1
```

Queue

```text
60 70 30 40 50
```

Notice

the empty space is reused.

No false overflow occurs.

---

# Common Mistakes

### 1. Forgetting Modulo

Wrong

```python
rear += 1
```

Correct

```python
rear = (rear + 1) % size
```

---

### 2. Incorrect Full Condition

Wrong

```python
rear == size - 1
```

Correct

```python
(rear + 1) % size == front
```

---

### 3. Forgetting to Reset Pointers

When the last element is removed,

always reset

```python
front = rear = -1
```

Otherwise,

future operations become incorrect.

---

# Complexity

| Operation | Complexity |
| --------- | ---------- |
| Enqueue   | **O(1)**   |
| Dequeue   | **O(1)**   |
| Front     | **O(1)**   |
| Rear      | **O(1)**   |

---

# Applications

Circular Queue is used in:

* CPU Scheduling
* Circular Buffers
* Network Packet Processing
* Streaming Data
* Producer Consumer Problems
* Round Robin Scheduling

---

# Pattern Recognition

Use Circular Queue when:

* Fixed-size buffer.
* Memory should be reused.
* Queue implemented using an array.
* Continuous insertion and deletion.

---

# Revision Cheat Sheet

```text
Circular Queue

Problem:
Normal Queue wastes space.

Solution:
Reuse empty positions.

Formula

Next Index

(index + 1) % size

Queue Full

(rear + 1) % size == front

Queue Empty

front == -1

Time

Enqueue → O(1)

Dequeue → O(1)

Applications

• Circular Buffer
• CPU Scheduling
• Round Robin
• Streaming
```
