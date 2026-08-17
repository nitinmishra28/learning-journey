# Implement Stack Using Two Queues

## Problem

Implement a **Stack** using two Queues.

A Stack follows:

```text
LIFO → Last In, First Out
```

A Queue follows:

```text
FIFO → First In, First Out
```

We need to use two queues to make the behavior of a Stack.

---

# Pattern

```text
Two Queues → Stack Simulation
```

---

# Main Idea

We use:

```python
q1
q2
```

The important idea is to keep `q1` arranged so that the **top of the stack is always at the front of `q1`**.

For example, after:

```python
push(1)
push(2)
push(3)
```

we want:

```text
q1 = [3, 2, 1]
       ↑
     front/top
```

Therefore:

```python
q1.popleft()
```

returns:

```text
3
```

which follows Stack's LIFO behavior.

---

# Why Do We Need `q2`?

A Queue is FIFO.

Suppose:

```text
q1 = [1,2,3]
```

The front is:

```text
1
```

But Stack needs:

```text
3
```

first.

So we use `q2` as a temporary queue to rearrange the elements.

The goal is:

```text
Old q1:
[1,2,3]

After push(4):

q1:
[4,3,2,1]
 ↑
top
```

Now:

```python
q1.popleft()
```

returns:

```text
4
```

which is exactly Stack behavior.

---

# Push Operation

The important part of this solution is `push()`.

Suppose:

```text
q1 = [1,2,3]
```

and we want:

```text
push(4)
```

If we simply do:

```python
q1.append(4)
```

we get:

```text
[1,2,3,4]
```

Then:

```python
q1.popleft()
```

would remove:

```text
1
```

But Stack needs:

```text
4
```

So we rearrange the queues.

---

# Push Step-by-Step

### Step 1: Move `q1` → `q2`

```python
while self.q1:
    self.q2.append(self.q1.popleft())
```

Before:

```text
q1 = [1,2,3]
q2 = []
```

After:

```text
q1 = []
q2 = [1,2,3]
```

---

### Step 2: Add the New Element to `q1`

```python
self.q1.append(x)
```

For:

```text
x = 4
```

we get:

```text
q1 = [4]
```

This is important because `4` will become the **front/top**.

---

### Step 3: Move `q2` → `q1`

```python
while self.q2:
    self.q1.append(self.q2.popleft())
```

Result:

```text
q1 = [4,1,2,3]
```

Now the front is:

```text
4
```

So:

```python
q1.popleft()
```

returns:

```text
4
```

Correct LIFO behavior.

---

# Why Does This Work?

Every time we push a new element:

```text
New element
    ↓
Placed at front of q1
    ↓
Older elements come after it
```

So `q1` always looks like:

```text
Newest → Older → Older → Oldest
```

For example:

```text
push(1)

q1:
[1]

push(2)

q1:
[2,1]

push(3)

q1:
[3,2,1]
```

Therefore:

```text
q1 front = Stack top
```

This is the key condition.

---

# Pop Operation

Because we maintain:

```text
q1 front = Stack top
```

`pop()` becomes very simple:

```python
def pop(self):
    return self.q1.popleft()
```

Example:

```text
q1 = [3,2,1]
```

Then:

```python
q1.popleft()
```

returns:

```text
3
```

This follows:

```text
LIFO
```

---

# Top Operation

We want to see the top without removing it.

The front of `q1` is the top.

So:

```python
def top(self):
    return self.q1[0]
```

Example:

```text
q1 = [3,2,1]
```

Therefore:

```python
q1[0] = 3
```

So:

```text
top() → 3
```

---

# Empty Operation

The stack is empty when `q1` is empty.

```python
def empty(self):
    return not self.q1
```

If:

```text
q1 = []
```

then:

```python
not self.q1
```

is:

```text
True
```

Otherwise:

```text
False
```

---

# Code

```python
from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:

        # Move all existing elements to q2
        while self.q1:
            self.q2.append(self.q1.popleft())

        # New element becomes the front/top
        self.q1.append(x)

        # Move old elements back
        while self.q2:
            self.q1.append(self.q2.popleft())

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1
```

---

# Dry Run

Perform:

```text
push(1)
push(2)
push(3)
pop()
top()
```

### `push(1)`

```text
q1 = []

Add 1

q1 = [1]
```

---

### `push(2)`

Move:

```text
q1 → q2

q1 = []
q2 = [1]
```

Add `2`:

```text
q1 = [2]
```

Move `q2` back:

```text
q1 = [2,1]
```

Now:

```text
Top = 2
```

---

### `push(3)`

Move:

```text
q1 = []
q2 = [2,1]
```

Add `3`:

```text
q1 = [3]
```

Move back:

```text
q1 = [3,2,1]
```

Now:

```text
Stack:

Top
 ↓
3
2
1
```

---

### `pop()`

```python
q1.popleft()
```

removes:

```text
3
```

Now:

```text
q1 = [2,1]
```

Correct because:

```text
3
```

was the last element pushed.

---

### `top()`

```python
q1[0]
```

returns:

```text
2
```

without removing it.

---

# Important Insight

The entire solution depends on maintaining this condition:

```text
FRONT OF q1 = TOP OF STACK
```

Once this is maintained:

```python
pop()  → q1.popleft()
top()  → q1[0]
```

become very easy.

The difficult part is only:

```text
push()
```

because we need to move the new element to the front of `q1`.

---

# Stack vs Queue

Remember the difference:

```text
Stack:
LIFO
Last In → First Out
```

```text
Queue:
FIFO
First In → First Out
```

Our implementation converts:

```text
Queue behavior
```

into:

```text
Stack behavior
```

by rearranging the elements during `push()`.

---

# Why Are We Using `popleft()`?

`deque` supports:

```python
popleft()
```

in:

```text
O(1)
```

We need to remove elements from the **front of the queue**.

Using:

```python
list.pop(0)
```

would be slower because remaining elements have to shift.

Therefore:

```python
from collections import deque
```

is preferred.

---

# Common Mistakes

### 1. Simply Appending to `q1`

Wrong:

```python
self.q1.append(x)
```

If:

```text
q1 = [1,2,3]
```

then:

```text
q1 = [1,2,3,4]
```

and:

```python
q1.popleft()
```

would remove:

```text
1
```

But Stack needs:

```text
4
```

---

### 2. Forgetting to Move `q1` to `q2`

We need to temporarily remove the old elements so that the new element can become the front of `q1`.

Flow:

```text
q1 → q2
add new element to q1
q2 → q1
```

---

### 3. Confusing `append()` and `popleft()`

For a `deque`:

```python
append(x)
```

adds to the **right**.

```python
popleft()
```

removes from the **left**.

Our goal is:

```text
Newest element → left/front
Older elements → after it
```

---

# Complexity

For this implementation:

```text
push()  → O(n)
pop()   → O(1)
top()   → O(1)
empty() → O(1)
```

Space:

```text
O(n)
```

---

# Revision Cheat Sheet

```text
Implement Stack Using Two Queues

Stack:
LIFO

Queue:
FIFO

Queues:
q1 → main queue
q2 → temporary queue

Main condition:
FRONT OF q1 = TOP OF STACK

Push:
1. Move q1 → q2
2. Add new element to q1
3. Move q2 → q1

Why?
To make the newest element the front of q1.

Pop:
q1.popleft()

Top:
q1[0]

Empty:
not q1

Important:
q2 is temporary.
The main goal is to keep the newest element
at the front of q1.

Complexity:
push  → O(n)
pop   → O(1)
top   → O(1)
empty → O(1)

Space:
O(n)
```

---

# One-Line Pattern

```text
Two Queues → move old elements aside → insert new element first → move old elements back → front of q1 becomes Stack top.
```