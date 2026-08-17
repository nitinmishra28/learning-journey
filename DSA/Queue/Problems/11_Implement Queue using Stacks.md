# Implement Queue Using Two Stacks

## Problem

Implement a **Queue** using only two stacks.

A Queue follows:

```text
FIFO → First In, First Out
```

A Stack follows:

```text
LIFO → Last In, First Out
```

We need to use two stacks to make the behavior of a Queue.

---

# Pattern

```text
Two Stacks → Queue Simulation
```

---

# Main Idea

We use:

```python
s1
s2
```

The important idea is to keep `s1` arranged so that the **front of the queue is always at the top of `s1`**.

For example, after:

```python
push(1)
push(2)
push(3)
```

we want:

```text
s1 = [3, 2, 1]
             ↑
          top/front
```

So:

```python
s1.pop()
```

returns:

```text
1
```

which follows Queue's FIFO behavior.

---

# Why Do We Need `s2`?

A stack is LIFO.

Suppose:

```text
s1 = [1, 2, 3]
```

The top is:

```text
3
```

But Queue needs:

```text
1
```

first.

So we use `s2` to temporarily reverse the order.

```text
s1 = [1,2,3]

Move everything to s2:

s2 = [3,2,1]
```

Now `1` is at the top of `s2`.

Then we move everything back:

```text
s1 = [3,2,1]
```

Now:

```python
s1.pop()
```

returns:

```text
1
```

---

# Push Operation

When pushing a new element:

```python
def push(self, x):
```

we want the new element to go to the **bottom** of `s1`.

Why?

Because the oldest element must remain at the top.

Suppose:

```text
s1 = [3,2,1]
```

and we want:

```text
push(4)
```

If we simply do:

```python
s1.append(4)
```

we get:

```text
[3,2,1,4]
```

Now:

```python
s1.pop()
```

would return:

```text
4
```

which is wrong.

So we use `s2` to temporarily move the elements.

---

# Push Step-by-Step

Suppose:

```text
s1 = [3,2,1]
```

### Step 1: Move `s1` to `s2`

```python
while self.s1:
    self.s2.append(self.s1.pop())
```

Result:

```text
s1 = []

s2 = [1,2,3]
```

---

### Step 2: Add the new element

```python
self.s1.append(x)
```

If:

```text
x = 4
```

then:

```text
s1 = [4]
```

---

### Step 3: Move `s2` back to `s1`

```python
while self.s2:
    self.s1.append(self.s2.pop())
```

Result:

```text
s1 = [4,3,2,1]
```

Now the top is:

```text
1
```

So:

```python
s1.pop()
```

returns:

```text
1
```

Correct Queue behavior.

---

# Why Does Moving Between Stacks Reverse the Order?

This is the key concept.

Suppose:

```text
s1 = [3,2,1]
```

Move using:

```python
s2.append(s1.pop())
```

First:

```text
3 → s2
```

Then:

```text
2 → s2
```

Then:

```text
1 → s2
```

So:

```text
s2 = [1,2,3]
```

The order is reversed.

Moving it back reverses it again:

```text
s2 = [1,2,3]

→ s1 = [4,3,2,1]
```

Therefore the two stacks allow us to rearrange the elements.

---

# Pop Operation

Our `push()` operation already maintains:

```text
s1 top = Queue front
```

Therefore `pop()` is very simple:

```python
def pop(self):
    return self.s1.pop()
```

Example:

```text
s1 = [4,3,2,1]
```

Top:

```text
1
```

So:

```python
s1.pop()
```

returns:

```text
1
```

This is FIFO behavior.

---

# Peek Operation

We don't want to remove the element.

So instead of:

```python
pop()
```

we access:

```python
s1[-1]
```

Code:

```python
def peek(self):
    return self.s1[-1]
```

Example:

```text
s1 = [4,3,2,1]

s1[-1] = 1
```

Therefore:

```text
peek() → 1
```

---

# Empty Operation

The queue is empty when `s1` is empty.

```python
def empty(self):
    return not self.s1
```

If:

```text
s1 = []
```

then:

```python
not self.s1
```

is:

```text
True
```

If:

```text
s1 = [3,2,1]
```

then:

```text
not self.s1
```

is:

```text
False
```

---

# Code

```python
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:

        # Move all elements from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())

        # Add new element at the bottom of the queue
        self.s1.append(x)

        # Move elements back
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1
```

---

# Dry Run

Perform:

```text
push(1)
push(2)
push(3)
pop()
peek()
```

### `push(1)`

```text
s1 = []
s2 = []

Add 1

s1 = [1]
```

---

### `push(2)`

Move:

```text
s1 → s2

s1 = []
s2 = [1]
```

Add `2`:

```text
s1 = [2]
```

Move back:

```text
s1 = [2,1]
s2 = []
```

Top:

```text
1
```

---

### `push(3)`

Move:

```text
s1 = []
s2 = [1,2]
```

Add:

```text
s1 = [3]
```

Move back:

```text
s1 = [3,2,1]
```

Therefore:

```text
Queue:
1 → 2 → 3
```

---

### `pop()`

```python
s1.pop()
```

removes:

```text
1
```

Now:

```text
s1 = [3,2]
```

---

### `peek()`

```python
s1[-1]
```

returns:

```text
2
```

---

# Important Insight

The entire solution depends on maintaining this condition:

```text
TOP OF s1 = FRONT OF QUEUE
```

Once this is maintained:

```text
pop()  → s1.pop()
peek() → s1[-1]
```

become very easy.

The difficult part is only:

```text
push()
```

because we need to place the new element at the bottom of `s1`.

---

# Common Mistakes

### 1. Simply Appending to `s1`

Wrong:

```python
self.s1.append(x)
```

If:

```text
s1 = [3,2,1]
```

then:

```text
s1 = [3,2,1,4]
```

and:

```python
s1.pop()
```

would remove `4`.

That violates FIFO.

---

### 2. Forgetting the Purpose of `s2`

`s2` is a **temporary stack**.

Its job is to help move existing elements out of the way so that the new element can be placed at the bottom of `s1`.

Think:

```text
s1 → s2
add new element
s2 → s1
```

---

# Complexity

For this implementation:

```text
push() → O(n)
pop()  → O(1)
peek() → O(1)
empty() → O(1)
```

Space:

```text
O(n)
```

because we use two stacks to store the queue elements.

---

# Revision Cheat Sheet

```text
Implement Queue Using Two Stacks

Queue:
FIFO

Stack:
LIFO

Stacks:
s1 → main stack
s2 → temporary stack

Main condition:
TOP OF s1 = FRONT OF QUEUE

Push:
1. Move s1 → s2
2. Add new element to s1
3. Move s2 → s1

Why?
To place the new element at the bottom of s1.

Pop:
s1.pop()

Peek:
s1[-1]

Empty:
not s1

Important:
s2 is only used to rearrange elements during push.

Complexity:
push  → O(n)
pop   → O(1)
peek  → O(1)
empty → O(1)

Space:
O(n)
```

---

# One-Line Pattern

```text
Two Stacks → temporarily reverse elements → keep Queue front at the top of s1 → pop from s1 for FIFO behavior.
```