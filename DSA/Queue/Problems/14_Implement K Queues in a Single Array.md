# Implement K Queues in a Single Array

## Problem

We need to implement:

```text
K independent queues
```

using only:

```text
One array of size n
```

Each queue should support:

```text
enqueue(x, i) → add x to queue i
dequeue(i)    → remove front element from queue i
isEmpty(i)    → check if queue i is empty
isFull()      → check if the array is full
```

The main challenge is:

> How can multiple queues share one array without wasting unused spaces?

---

# Pattern

```text
Array + Linked List using Indices + Free Space Management
```

---

# Main Idea

We use **three important arrays**:

```python
arr
front
rear
next
```

and one variable:

```python
freespot
```

Think of the structure as:

```text
arr
 ↓
Stores actual values

front
 ↓
Stores the first index of every queue

rear
 ↓
Stores the last index of every queue

next
 ↓
Connects elements together

freespot
 ↓
Points to the first unused index
```

---

# Why Can't We Use K Separate Arrays?

A simple approach would be:

```text
queue1 → separate array
queue2 → separate array
queue3 → separate array
...
```

But this can waste space.

Example:

```text
n = 10
k = 2
```

If we divide the array equally:

```text
Queue 1 → 5 spaces
Queue 2 → 5 spaces
```

Suppose Queue 1 needs 8 elements.

It cannot use Queue 2's unused spaces.

This solution avoids that problem.

All queues share the same:

```text
array of n positions
```

So any free position can be used by any queue.

---

# Data Structures

## 1. `arr`

```python
self.arr = [0] * n
```

This stores the actual values.

Example:

```text
arr = [10, 20, 30, 40, ...]
```

---

# 2. `front`

```python
self.front = [-1] * k
```

`front[i]` stores the index of the first element of queue `i`.

Example:

```text
Queue 0:
front[0] = 3

Queue 1:
front[1] = 7
```

If:

```python
front[i] == -1
```

then queue `i` is empty.

---

# 3. `rear`

```python
self.rear = [-1] * k
```

`rear[i]` stores the index of the last element of queue `i`.

Example:

```text
Queue 0:

front[0] = 2
rear[0] = 5
```

So the queue is connected from:

```text
2 → ... → 5
```

---

# 4. `next`

This is the most important array.

```python
self.next = [i + 1 for i in range(n)]
self.next[n - 1] = -1
```

Initially:

```text
next = [1,2,3,4,5,...,-1]
```

This creates a linked list of all free positions:

```text
0 → 1 → 2 → 3 → 4 → ... → n-1 → -1
```

So `next` has **two jobs**.

### When an index is free

It points to the:

```text
next free index
```

### When an index is being used by a queue

It points to the:

```text
next element of that queue
```

This dual use of `next` is the key idea of the problem.

---

# 5. `freespot`

```python
self.freespot = 0
```

This stores the index of the first available position.

Initially:

```text
freespot = 0
```

because index `0` is free.

The free list is:

```text
0 → 1 → 2 → 3 → 4 → -1
↑
freespot
```

---

# Initial Structure

Suppose:

```text
n = 5
k = 2
```

Initially:

```text
arr:
[0, 0, 0, 0, 0]

front:
[-1, -1]

rear:
[-1, -1]

next:
[1, 2, 3, 4, -1]

freespot:
0
```

Free positions:

```text
0 → 1 → 2 → 3 → 4 → -1
```

---

# Enqueue

To insert:

```python
enqueue(x, i)
```

we need to:

```text
1. Validate queue number
2. Check whether space exists
3. Take a free index
4. Store the value
5. Connect it to the queue
6. Update front/rear
7. Update freespot
```

---

# Step 1: Check Queue Number

```python
if i < 0 or i >= self.k:
    return False
```

Valid queue numbers are:

```text
0 ... k-1
```

Anything outside this range is invalid.

---

# Step 2: Check Full

```python
if self.isFull():
    return False
```

The array is full when:

```python
self.freespot == -1
```

Why?

Because `freespot` points to the next available position.

If:

```text
freespot = -1
```

there is no free position left.

---

# Step 3: Get a Free Index

```python
index = self.freespot
```

Suppose:

```text
freespot = 2
```

Then:

```text
index = 2
```

We use index `2`.

---

# Step 4: Move `freespot`

```python
self.freespot = self.next[index]
```

Suppose:

```text
next[2] = 3
```

After using index `2`:

```text
freespot = 3
```

So the free list moves forward.

---

# Step 5: Store the Value

```python
self.arr[index] = x
```

For:

```text
x = 50
index = 2
```

we get:

```text
arr[2] = 50
```

---

# Step 6: Handle Empty Queue

If the queue is empty:

```python
if self.front[i] == -1:
    self.front[i] = index
```

The newly inserted element becomes the first element.

Example:

```text
Queue 0 is empty

front[0] = -1
```

Insert at index `2`:

```text
front[0] = 2
rear[0] = 2
```

---

# Step 7: Connect to Existing Queue

If the queue already contains elements:

```python
else:
    self.next[self.rear[i]] = index
```

Suppose:

```text
Queue 0:

front = 1
rear = 3
```

and we insert at index:

```text
5
```

We connect:

```text
next[3] = 5
```

So:

```text
1 → ... → 3 → 5
```

---

# Step 8: Update Rear

```python
self.rear[i] = index
```

The new element is now the last element.

---

# Step 9: Mark New Rear

```python
self.next[index] = -1
```

The new rear does not point to another queue element.

So:

```text
next[rear] = -1
```

---

# Enqueue Example

Suppose:

```text
n = 5
k = 2
```

Initially:

```text
Free:
0 → 1 → 2 → 3 → 4
```

Perform:

```python
enqueue(10, 0)
```

Use index `0`.

```text
arr[0] = 10

front[0] = 0
rear[0] = 0
```

Free positions:

```text
1 → 2 → 3 → 4
```

---

Now:

```python
enqueue(20, 1)
```

Use index `1`.

```text
arr[1] = 20

front[1] = 1
rear[1] = 1
```

Free:

```text
2 → 3 → 4
```

---

Now:

```python
enqueue(30, 0)
```

Use index `2`.

Queue 0 currently ends at index `0`.

So:

```python
next[0] = 2
```

Queue 0 becomes:

```text
0 → 2
```

Values:

```text
10 → 30
```

So:

```text
front[0] = 0
rear[0] = 2
```

---

# Important Visualization

After these operations:

```python
enqueue(10, 0)
enqueue(20, 1)
enqueue(30, 0)
```

we have:

```text
arr:

index:  0   1   2   3   4
        -------------------
value: 10  20  30   -   -
```

Queue 0:

```text
front[0]
   ↓
   0 → 2 → -1

10 → 30
```

Queue 1:

```text
front[1]
   ↓
   1 → -1

20
```

Free list:

```text
freespot
   ↓
   3 → 4 → -1
```

This is the whole structure.

---

# Why Do We Need `next`?

Without `next`, we would not know:

```text
Which array index comes next in a queue?
```

For example:

```text
Queue 0:

index 0 → index 2 → index 5
```

The actual array positions are not necessarily continuous.

They could be:

```text
0 → 4 → 1 → 7
```

So `next` acts like the pointer of a linked list.

Instead of storing actual memory addresses, we store:

```text
array indices
```

---

# Why Does `next` Also Store Free Positions?

This is the clever part.

Initially:

```text
0 → 1 → 2 → 3 → 4
```

This represents free positions.

After using index `0`:

```text
freespot = 1
```

Now:

```text
1 → 2 → 3 → 4
```

So the same `next` array is being used as a:

```text
Free List
```

When an index becomes part of a queue, its `next` value changes to point to the next element of that queue.

Therefore:

```text
next = Queue links + Free-list links
```

---

# Dequeue

To remove the front element:

```python
dequeue(i)
```

we:

```text
1. Check queue number
2. Check if queue is empty
3. Get front index
4. Move front to next element
5. If queue becomes empty, reset rear
6. Return removed index to free list
7. Return the value
```

---

# Step 1: Validate Queue

```python
if i < 0 or i >= self.k:
    return -1
```

---

# Step 2: Check Empty

```python
if self.isEmpty(i):
    return -1
```

Queue is empty when:

```python
front[i] == -1
```

---

# Step 3: Store Front Index

```python
index = self.front[i]
```

Suppose:

```text
front[0] = 2
```

then:

```text
index = 2
```

This is the element we need to remove.

---

# Step 4: Move Front

```python
self.front[i] = self.next[index]
```

Suppose:

```text
2 → 5
```

After removing `2`:

```text
front[i] = 5
```

So the next element becomes the new front.

---

# Step 5: Handle Empty Queue

If:

```python
self.front[i] == -1
```

then there is no element left.

So:

```python
self.rear[i] = -1
```

Both front and rear must indicate that the queue is empty.

---

# Step 6: Return Index to Free List

This is very important.

The removed index should become available again.

```python
self.next[index] = self.freespot
self.freespot = index
```

Suppose:

```text
freespot = 3
```

and we removed index:

```text
1
```

We do:

```text
next[1] = 3
freespot = 1
```

Now the free list becomes:

```text
1 → 3 → ...
```

So index `1` can be reused by any queue.

---

# Why Do We Add the Freed Index to the Front of the Free List?

Because we don't need to search for free space.

We simply make the newly freed index the new `freespot`.

```text
Old free list:

3 → 4 → -1

Freed index:

1

New free list:

1 → 3 → 4 → -1
↑
freespot
```

This makes insertion:

```text
O(1)
```

---

# Full Code

```python
class kQueues:

    def __init__(self, n, k):

        self.n = n
        self.k = k

        # Stores actual values
        self.arr = [0] * n

        # Front index of each queue
        self.front = [-1] * k

        # Rear index of each queue
        self.rear = [-1] * k

        # Initially all positions are free
        self.next = [i + 1 for i in range(n)]
        self.next[n - 1] = -1

        # First free position
        self.freespot = 0

    def enqueue(self, x, i):

        # Invalid queue number
        if i < 0 or i >= self.k:
            return False

        # No free space
        if self.isFull():
            return False

        # Get a free index
        index = self.freespot

        # Move freespot to next free index
        self.freespot = self.next[index]

        # Store value
        self.arr[index] = x

        # If queue is empty
        if self.front[i] == -1:
            self.front[i] = index

        else:
            # Connect old rear to new element
            self.next[self.rear[i]] = index

        # New element becomes rear
        self.rear[i] = index

        # New rear points to nothing
        self.next[index] = -1

        return True

    def dequeue(self, i):

        # Invalid queue number
        if i < 0 or i >= self.k:
            return -1

        # Queue is empty
        if self.isEmpty(i):
            return -1

        # Get front index
        index = self.front[i]

        # Move front to next element
        self.front[i] = self.next[index]

        # If queue becomes empty
        if self.front[i] == -1:
            self.rear[i] = -1

        # Return removed index to free list
        self.next[index] = self.freespot
        self.freespot = index

        return self.arr[index]

    def isEmpty(self, i):
        return self.front[i] == -1

    def isFull(self):
        return self.freespot == -1
```

---

# Complete Dry Run

Suppose:

```text
n = 5
k = 2
```

Perform:

```python
enqueue(10, 0)
enqueue(20, 1)
enqueue(30, 0)
dequeue(0)
enqueue(40, 1)
```

---

## Initial

```text
Free list:

0 → 1 → 2 → 3 → 4 → -1

freespot = 0
```

---

## `enqueue(10, 0)`

Use:

```text
index = 0
```

Queue 0:

```text
0 → -1
```

Free:

```text
1 → 2 → 3 → 4
```

---

## `enqueue(20, 1)`

Use:

```text
index = 1
```

Queue 1:

```text
1 → -1
```

Free:

```text
2 → 3 → 4
```

---

## `enqueue(30, 0)`

Use:

```text
index = 2
```

Queue 0 was:

```text
0 → -1
```

Connect:

```text
next[0] = 2
```

Queue 0:

```text
0 → 2 → -1
```

Values:

```text
10 → 30
```

Free:

```text
3 → 4
```

---

## `dequeue(0)`

Front of Queue 0:

```text
index = 0
```

Remove it.

New front:

```text
front[0] = next[0]
         = 2
```

Queue 0:

```text
2 → -1
```

Index `0` becomes free.

Free list:

```text
0 → 3 → 4 → -1
```

Returned value:

```text
10
```

---

## `enqueue(40, 1)`

`freespot` is:

```text
0
```

So index `0` is reused.

Queue 1 currently:

```text
1 → -1
```

Connect:

```text
next[1] = 0
```

Queue 1 becomes:

```text
1 → 0 → -1
```

Values:

```text
20 → 40
```

This demonstrates why the array does **not** need to be contiguous.

---

# Key Concept

The queues are not stored like:

```text
Queue 0:
[10,30]

Queue 1:
[20,40]
```

Instead, they are linked using array indices.

Example:

```text
Queue 0:

index 2
   ↓
  30
```

Queue 1:

```text
index 1 → index 0
   ↓         ↓
  20        40
```

The `next` array tells us how to move between elements.

---

# Important: `front` and `rear`

For every queue:

```text
front[i]
```

means:

```text
Where does this queue start?
```

and:

```text
rear[i]
```

means:

```text
Where does this queue end?
```

Example:

```text
Queue 1:

front[1] = 4
rear[1] = 2

4 → 0 → 2
```

Even though:

```text
4 > 0 > 2
```

the queue order is determined by `next`, not by index values.

---

# Common Mistakes

### 1. Thinking Queue Elements Must Be Contiguous

They don't.

A queue can be:

```text
2 → 5 → 1 → 7
```

The `next` array maintains the connection.

---

### 2. Forgetting to Update `freespot`

After enqueue:

```python
self.freespot = self.next[index]
```

After dequeue:

```python
self.next[index] = self.freespot
self.freespot = index
```

These operations maintain the free list.

---

### 3. Forgetting to Update `rear`

When a new element is inserted:

```python
self.rear[i] = index
```

When the last element is removed:

```python
self.rear[i] = -1
```

---

### 4. Confusing `next` With an Actual Pointer

Here `next` stores:

```text
array indices
```

not memory addresses.

For example:

```text
next[3] = 7
```

means:

```text
From index 3, the next queue element is at index 7.
```

---

# Complexity

Each operation performs only a constant number of operations.

```text
enqueue → O(1)
dequeue → O(1)
isEmpty → O(1)
isFull  → O(1)
```

Space:

```text
O(n + k)
```

because we use:

```text
arr  → O(n)
next → O(n)
front → O(k)
rear  → O(k)
```

---

# Revision Cheat Sheet

```text
K Queues in One Array

Pattern:
Array + Linked List using Indices + Free List

Arrays:
arr
→ stores values

front
→ first index of every queue

rear
→ last index of every queue

next
→ connects queue elements
→ also maintains free positions

freespot
→ first available array index

Initial free list:

0 → 1 → 2 → 3 → ... → -1

Enqueue:

1. Get index = freespot
2. Move freespot forward
3. Store value in arr
4. If queue empty:
      front[i] = index
   Else:
      next[rear[i]] = index
5. rear[i] = index
6. next[index] = -1

Dequeue:

1. index = front[i]
2. front[i] = next[index]
3. If queue becomes empty:
      rear[i] = -1
4. Return index to free list:
      next[index] = freespot
      freespot = index

Queue empty:
front[i] == -1

Array full:
freespot == -1

Most important:
next has TWO jobs:

1. Connect elements of queues
2. Connect free array positions

Complexity:

enqueue → O(1)
dequeue → O(1)
isEmpty → O(1)
isFull  → O(1)

Space:
O(n + k)
```

---

# One-Line Pattern

```text
Use front/rear to track each queue, next to link elements and free positions, and freespot to quickly find the next available array index.
```