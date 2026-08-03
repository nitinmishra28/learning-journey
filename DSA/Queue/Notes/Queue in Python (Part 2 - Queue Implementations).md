# Queue in Python (Part 2 - Queue Implementations)

In Python, a Queue can be implemented in multiple ways.

Each implementation has different time complexity and use cases.

---

# 1. Queue Using List

The simplest way is to use a Python list.

## Code

```python
queue = []

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

# Dequeue
removed = queue.pop(0)

print(removed)
print(queue)
```

Output

```text
[10, 20, 30]

10

[20, 30]
```

---

## Complexity

| Operation | Complexity |
| --------- | ---------- |
| append()  | O(1)       |
| pop(0)    | O(n)       |
| Front     | O(1)       |
| Rear      | O(1)       |

---

## Why is `pop(0)` O(n)?

Suppose

```text
10 20 30 40
```

After

```python
queue.pop(0)
```

the list becomes

```text
20 30 40
```

Python shifts every remaining element one position to the left.

```text
20 ← Shift

30 ← Shift

40 ← Shift
```

Hence

```text
Time = O(n)
```

❌ Therefore, Python List is **not recommended** for implementing a Queue.

---

# 2. Queue Using collections.deque ⭐ (Recommended)

Python provides a built-in **Double Ended Queue (deque)**.

Import

```python
from collections import deque
```

---

## Code

```python
from collections import deque

queue = deque()

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

# Dequeue
print(queue.popleft())

print(queue)
```

Output

```text
deque([10, 20, 30])

10

deque([20, 30])
```

---

## Complexity

| Operation | Complexity |
| --------- | ---------- |
| append()  | O(1)       |
| popleft() | O(1)       |
| Front     | O(1)       |
| Rear      | O(1)       |

---

## Why is deque Better?

Unlike a list,

`deque` does **not shift elements**.

Internally it is optimized for insertion and deletion from both ends.

That is why

```python
queue.popleft()
```

is

```text
O(1)
```

This is the implementation used in almost every Python DSA solution.

---

# Useful deque Operations

## Insert at Rear

```python
queue.append(10)
```

---

## Remove from Front

```python
queue.popleft()
```

---

## Front Element

```python
queue[0]
```

---

## Rear Element

```python
queue[-1]
```

---

## Check Empty

```python
if not queue:
    print("Queue is Empty")
```

---

## Size

```python
len(queue)
```

---

# 3. Queue Using queue.Queue

Python also provides

```python
from queue import Queue
```

This is mainly used in

* Multi-threading
* Producer Consumer Problems

Not commonly used in DSA.

---

## Code

```python
from queue import Queue

q = Queue()

q.put(10)
q.put(20)
q.put(30)

print(q.get())
print(q.qsize())
```

---

## Complexity

| Operation | Complexity |
| --------- | ---------- |
| put()     | O(1)       |
| get()     | O(1)       |

---

## When to Use?

✅ Multi-threaded programs

❌ DSA Interviews

For DSA, always prefer

```python
collections.deque
```

---

# Queue Using Linked List

A queue can also be implemented using a Linked List.

Maintain:

* Front Pointer
* Rear Pointer

Insertion happens at the rear.

Deletion happens at the front.

Both operations take

```text
O(1)
```

You usually implement this manually in interviews only if asked.

For Python DSA problems,

`deque` is simpler and preferred.

---

# Which Queue Should You Use?

| Implementation | Recommended?      | Reason                            |
| -------------- | ----------------- | --------------------------------- |
| List           | ❌ No              | `pop(0)` is O(n)                  |
| deque          | ✅ Yes             | O(1) enqueue & dequeue            |
| queue.Queue    | ⚠️ Rarely         | Mainly for threading              |
| Linked List    | ⚠️ Interview only | Good for implementation questions |

---

# Interview Notes

If the interviewer asks:

> Which Queue implementation do you prefer in Python?

Answer:

> I use **collections.deque** because it provides **O(1)** insertion and deletion from both ends, unlike a Python list where `pop(0)` takes **O(n)**.

---

# Common Mistakes

### 1. Using `pop()` instead of `popleft()`

Wrong

```python
queue.pop()
```

This removes from the **rear**, making it behave like a stack.

Correct

```python
queue.popleft()
```

---

### 2. Using a List for Large Inputs

Avoid

```python
queue.pop(0)
```

because it is O(n).

---

### 3. Forgetting to Import deque

Always import

```python
from collections import deque
```

---

### 4. Using queue.Queue in LeetCode

Most LeetCode problems expect

```python
collections.deque
```

because it is simpler and faster.

---

# Complexity Comparison

| Implementation | Enqueue | Dequeue |
| -------------- | ------- | ------- |
| List           | O(1)    | O(n)    |
| deque          | O(1)    | O(1)    |
| queue.Queue    | O(1)    | O(1)    |
| Linked List    | O(1)    | O(1)    |

---

# Revision Cheat Sheet

```text
Queue Implementations

1. List
   append()
   pop(0) ❌ O(n)

2. deque ⭐
   append()
   popleft()
   Recommended

3. queue.Queue
   put()
   get()
   Used in threading

4. Linked List
   Front Pointer
   Rear Pointer

Interview Choice

✅ collections.deque
```
