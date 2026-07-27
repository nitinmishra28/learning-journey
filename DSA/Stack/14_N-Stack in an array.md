# K Stacks in a Single Array

## Problem

Design **`k` stacks** using **only one array of size `n`**.

Each stack should support:

```text
push(x, stackNumber)
pop(stackNumber)
```

without creating separate arrays for each stack.

---

# Main Idea

Instead of dividing the array into fixed parts:

```text
Stack 1 → 0 to 9

Stack 2 → 10 to 19

Stack 3 → 20 to 29
```

we allow every stack to use **any free index** in the array.

The complete idea is:

```text
One Common Array
        ↓
Free Index List
        ↓
Each Stack stores only its TOP
        ↓
next[] connects nodes
```

---

# Data Structures Used

We use four important data structures.

```python
arr
top
next
freespot
```

---

# 1. `arr`

```python
self.arr = [0] * n
```

Stores the actual values.

Example:

```text
Index:

0   1   2   3   4   5


Value:

10  50  30  80  --  --
```

Nothing special here.

---

# 2. `top`

```python
self.top = [-1] * k
```

Stores the **top index** of every stack.

Example:

```text
top =

[4, 2, -1]
```

means:

```text
Stack 1 top → index 4

Stack 2 top → index 2

Stack 3 is empty
```

Remember:

```text
top[i]
      ↓
Stores INDEX
not value
```

---

# 3. `next`

This is the most important array.

```python
self.next = [0] * n
```

`next[]` performs **two different jobs**.

---

## Job 1 → Connect Elements Inside a Stack

Suppose Stack 1 contains:

```text
30
20
10
```

inside the array:

```text
Index:

5   2   7
```

Then:

```text
top[0]

↓

5 → 2 → 7 → -1
```

is stored using:

```text
next[5] = 2

next[2] = 7

next[7] = -1
```

So:

```text
next[]
```

works exactly like:

```text
next pointer
```

of a linked list.

---

## Job 2 → Maintain Free Indices

Initially:

```text
0 1 2 3 4 5
```

are all free.

So:

```text
next

↓

0 → 1 → 2 → 3 → 4 → 5 → -1
```

The first free location is stored in:

```python
freespot
```

Initially:

```text
freespot = 0
```

So:

```text
next[]
```

acts like a linked list of free indices.

### Remember

```text
Used Index
        ↓
next → Stack Connection


Free Index
        ↓
next → Free List Connection
```

The same array performs both jobs.

---

# 4. `freespot`

```python
self.freespot = 0
```

Always stores:

```text
First Available Free Index
```

Suppose:

```text
Free List

3 → 5 → 7
```

Then:

```text
freespot = 3
```

Whenever we insert:

```text
Take freespot
Move freespot to next free index
```

---

# Initialization

```python
for i in range(n - 1):
    self.next[i] = i + 1

self.next[n - 1] = -1
```

Initially:

```text
Index:

0   1   2   3   4
```

Next:

```text
1   2   3   4  -1
```

Graphically:

```text
0 → 1 → 2 → 3 → 4 → -1
```

This represents:

```text
All locations are free.
```

---

# Push Operation

The complete push flow:

```text
Take first free index
        ↓
Move freespot
        ↓
Store value
        ↓
Connect with previous top
        ↓
Update top
```

---

## Step 1 → Overflow Check

```python
if self.freespot == -1:
    return False
```

If:

```text
freespot = -1
```

No free location exists.

The array is full.

---

## Step 2 → Take Free Index

```python
index = self.freespot
```

Suppose:

```text
freespot = 3
```

Then:

```text
index = 3
```

This location will store the new value.

---

## Step 3 → Move Free Pointer

```python
self.freespot = self.next[index]
```

Suppose:

```text
Free List

3 → 5 → 7
```

After taking `3`:

```text
Free List

5 → 7
```

So:

```text
freespot = 5
```

This is probably the easiest line to forget.

Remember:

```text
Current free index used
        ↓
Move freespot to next free index
```

---

## Step 4 → Store Value

```python
self.arr[index] = x
```

Simple insertion.

---

## Step 5 → Connect New Node

```python
self.next[index] = self.top[i - 1]
```

This line is the heart of the algorithm.

Suppose:

```text
Stack

20
10
```

Top:

```text
top = 4
```

Now new value:

```text
30
```

comes.

Suppose new index is:

```text
7
```

We do:

```python
next[7] = 4
```

Now:

```text
7 → 4
```

The new node points to the old top.

Exactly like:

```text
Linked List insertion at head
```

Remember:

```text
New Node
      ↓
Points to Old Top
```

---

## Step 6 → Update Top

```python
self.top[i - 1] = index
```

Now the new node becomes:

```text
Top of Stack
```

---

# Pop Operation

The complete flow:

```text
Take current top
        ↓
Move top
        ↓
Return removed index to free list
        ↓
Return value
```

---

## Step 1 → Underflow Check

```python
if self.top[i - 1] == -1:
    return -1
```

Stack is empty.

---

## Step 2 → Get Top Index

```python
index = self.top[i - 1]
```

This is the node to remove.

---

## Step 3 → Move Top

```python
self.top[i - 1] = self.next[index]
```

Suppose:

```text
7 → 4 → 2
```

Top:

```text
7
```

After popping:

```text
4 → 2
```

So:

```text
top = 4
```

---

## Step 4 → Return Removed Index to Free List

```python
self.next[index] = self.freespot
self.freespot = index
```

Suppose current free list:

```text
5 → 6
```

Removed index:

```text
7
```

After returning:

```text
7 → 5 → 6
```

Notice:

```text
Removed node
        ↓
Becomes new head
of free list
```

---

## Step 5 → Return Value

```python
return self.arr[index]
```

The value stored at that index is returned.

---

# Dry Run

Suppose:

```text
n = 5

k = 2
```

Initially:

```text
arr

[_, _, _, _, _]


top

[-1, -1]


next

[1, 2, 3, 4, -1]


freespot

0
```

---

## Push 10 in Stack 1

Take:

```text
index = 0
```

Store:

```text
arr[0] = 10
```

Update:

```text
top[0] = 0
```

Move free:

```text
freespot = 1
```

State:

```text
top

[0, -1]
```

---

## Push 20 in Stack 1

Take:

```text
index = 1
```

Connect:

```text
next[1] = 0
```

Update:

```text
top[0] = 1
```

Now Stack 1:

```text
1 → 0
```

---

## Pop Stack 1

Current top:

```text
1
```

Move top:

```text
top = 0
```

Return removed index to free list:

```text
1 → 2 → 3 → 4
```

Return:

```text
20
```

---

# Why Does `next[]` Have Two Jobs?

This is the most important concept.

When an index is:

```text
FREE
```

its `next[]` entry connects it with the next free index.

When the same index becomes:

```text
USED
```

its `next[]` entry connects it with the next node in its stack.

So:

```text
Free Index
      ↓
next → Free List


Used Index
      ↓
next → Stack Link
```

The same array is reused.

That is why only:

```text
O(n)
```

extra memory is required.

---

# Common Mistakes

## 1. `top` Stores Indices

Wrong thinking:

```text
top stores value
```

Correct:

```text
top stores INDEX
```

---

## 2. Move `freespot`

Never forget:

```python
self.freespot = self.next[index]
```

Otherwise the same location will be reused.

---

## 3. Connect Before Updating Top

Correct order:

```python
next[index] = top

top = index
```

If you update `top` first, the old connection is lost.

---

## 4. Return Removed Index to Free List

Never forget:

```python
next[index] = freespot

freespot = index
```

Otherwise that location is permanently lost.

---

## 5. `next[]` Is Reused

Do not think:

```text
next[]
```

only stores stack connections.

It also stores:

```text
Free List Connections
```

---

# Complexity

## Time Complexity

```text
Push → O(1)

Pop → O(1)
```

## Space Complexity

```text
O(n + k)
```

where:

```text
arr  → O(n)

next → O(n)

top  → O(k)
```

---

# Revision Summary

```text
Initialization

Create Free List
        ↓

Push

Take freespot
        ↓
Move freespot
        ↓
Store value
        ↓
Point new node to old top
        ↓
Update top


Pop

Take top
        ↓
Move top
        ↓
Return removed index to free list
        ↓
Return value
```

The easiest way to remember is:

```text
Push:
Take free index → Link with old top → New top

Pop:
Remove top → Move top → Return removed index to free list
```

## Pattern Name

```text
Multiple Stacks in One Array + Free List
```
