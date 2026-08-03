# Queue in Python (Part 4 - Deque)

# What is a Deque?

A **Deque (Double Ended Queue)** is a data structure in which insertion and deletion can happen from **both ends**.

Unlike a normal queue,

```text id="s4lcrn"
Queue

Insert → Rear

Delete → Front
```

A deque allows

```text id="0f16pv"
Insert → Front or Rear

Delete → Front or Rear
```

---

# Why Do We Need a Deque?

Suppose we want to remove elements from both ends.

A normal queue cannot do this efficiently.

A deque supports:

* Insert at front
* Insert at rear
* Delete from front
* Delete from rear

all in

```text id="s12xra"
O(1)
```

time.

---

# Deque Representation

```text id="vv9ey5"
Front                      Rear
 ↓                          ↓

10 20 30 40
```

Possible operations

```text id="wkq6gk"
Insert Front

↓

5 10 20 30 40


Insert Rear

↓

10 20 30 40 50


Delete Front

↓

20 30 40


Delete Rear

↓

10 20 30
```

---

# Python Implementation

Python provides

```python id="rldahv"
from collections import deque
```

This is the most commonly used deque implementation in DSA.

---

# Create a Deque

```python id="5lkx7v"
from collections import deque

dq = deque()
```

---

# Insert at Rear

```python id="8v9xrr"
dq.append(10)
dq.append(20)
dq.append(30)
```

Output

```text id="7bfjrq"
deque([10, 20, 30])
```

Complexity

```text id="bd6uxu"
O(1)
```

---

# Insert at Front

```python id="t2swt7"
dq.appendleft(5)
```

Output

```text id="w6vhsv"
deque([5, 10, 20, 30])
```

Complexity

```text id="5nfwqo"
O(1)
```

---

# Delete from Front

```python id="jlwmz2"
dq.popleft()
```

Output

```text id="2pqvtr"
5
```

Deque

```text id="jvw2eh"
deque([10,20,30])
```

Complexity

```text id="q5g7tp"
O(1)
```

---

# Delete from Rear

```python id="o9bm6k"
dq.pop()
```

Output

```text id="3ybl09"
30
```

Deque

```text id="l6czs8"
deque([10,20])
```

Complexity

```text id="ndc4n4"
O(1)
```

---

# Front Element

```python id="v5q7p7"
dq[0]
```

Returns

```text id="hgc12w"
Front Element
```

---

# Rear Element

```python id="q4gkk8"
dq[-1]
```

Returns

```text id="j2mrtg"
Last Element
```

---

# Check Empty

```python id="dd7ppw"
if not dq:
    print("Empty")
```

---

# Size

```python id="njlwm7"
len(dq)
```

---

# Why Use deque Instead of List?

Suppose we want to insert at the beginning.

Using a list

```python id="ojtsbq"
arr.insert(0, 5)
```

takes

```text id="89tf8b"
O(n)
```

because every element shifts.

Similarly,

```python id="1r78cn"
arr.pop(0)
```

is also

```text id="mhc9lf"
O(n)
```

In contrast,

```python id="v5tzfr"
deque.appendleft()
deque.popleft()
```

both take

```text id="zjlwmc"
O(1)
```

---

# Queue vs Deque

| Queue                | Deque               |
| -------------------- | ------------------- |
| Insert only at rear  | Insert at both ends |
| Delete only at front | Delete at both ends |
| FIFO                 | Flexible            |
| Limited operations   | More powerful       |

---

# Common Mistakes

### 1. Forgetting to import deque

Always write

```python id="5d6mhf"
from collections import deque
```

---

### 2. Using list instead of deque

Avoid

```python id="egw46w"
arr.pop(0)
arr.insert(0, x)
```

Both are

```text id="r9jpxo"
O(n)
```

Use

```python id="lsm6g0"
deque
```

instead.

---

### 3. Confusing Queue and Deque

Queue

```text id="2hmx8v"
Rear → Insert

Front → Delete
```

Deque

```text id="dlm6iu"
Front → Insert/Delete

Rear → Insert/Delete
```

---

# Complexity

| Operation    | Complexity |
| ------------ | ---------- |
| append()     | O(1)       |
| appendleft() | O(1)       |
| pop()        | O(1)       |
| popleft()    | O(1)       |
| Front        | O(1)       |
| Rear         | O(1)       |

---

# Applications

Deque is used in:

* Sliding Window
* Monotonic Queue
* LRU Cache
* Palindrome Checking
* 0-1 BFS
* Task Scheduling

---

# Pattern Recognition

Use Deque when:

* Insertion is required from both ends.
* Deletion is required from both ends.
* Sliding window problems.
* Need O(1) operations at both ends.

---

# Revision Cheat Sheet

```text id="wxtpsm"
Deque

Double Ended Queue

Insert

Front ✔
Rear ✔

Delete

Front ✔
Rear ✔

Python

from collections import deque

append()

appendleft()

pop()

popleft()

Time

All Operations → O(1)

Applications

• Sliding Window
• Monotonic Queue
• LRU Cache
• 0-1 BFS
```
