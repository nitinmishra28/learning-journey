# Reverse First K Elements of a Queue

## 📌 Problem

Given a queue and an integer `k`, reverse the **first `k` elements** of the queue while keeping the remaining elements in their original order.

### Example

```text
Queue:  1 2 3 4 5 6 7 8
k = 3

Output:
3 2 1 6 5 4 8 7
```

---

## 💡 Approach

We use a **Stack + Recursion**.

1. Take the first `k` elements from the queue.
2. Store them in a stack.
3. Pop elements from the stack and put them back into the queue.
4. Recursively process the next `k` elements.
5. If fewer than `k` elements remain, rotate them to the back of the queue.

### Pattern

```text
Queue → Stack → Queue
```

---

## 🧠 Code

```python
from collections import deque

q = deque()

def newGetReversed(q, k, count):

    if count >= k:
        stack = []

        # Store first k elements in stack
        for i in range(k):
            stack.append(q.popleft())

        # Put them back in reversed order
        for i in range(k):
            q.append(stack.pop())

        # Process next k elements
        newGetReversed(q, k, count - k)

    else:
        # Rotate remaining elements
        for i in range(count):
            q.append(q.popleft())


q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)
q.append(7)
q.append(8)

k = 3
count = len(q)

newGetReversed(q, k, count)

while q:
    print(q.popleft())
```

---

## 🔍 Dry Run

For:

```text
Queue = 1 2 3 4 5 6 7 8
k = 3
```

### First Group

```text
1 2 3
```

Using stack:

```text
1 2 3 → 3 2 1
```

Queue:

```text
3 2 1 4 5 6 7 8
```

### Second Group

```text
4 5 6 → 6 5 4
```

Queue:

```text
3 2 1 6 5 4 7 8
```

### Remaining Elements

Only:

```text
7 8
```

Since `2 < 3`, rotate them:

```text
7 8 → 8 7
```

### Final Queue

```text
3 2 1 6 5 4 8 7
```

---

## ⏱️ Complexity

* **Time:** `O(n)`
* **Auxiliary Space:** `O(k)` for the stack
* **Recursion Stack:** `O(n/k)`

Where `n` is the number of elements in the queue.

---

## 🔑 Key Takeaway

> **Reverse every group of K elements using a stack, recursively process the remaining queue, and rotate the leftover elements.**
