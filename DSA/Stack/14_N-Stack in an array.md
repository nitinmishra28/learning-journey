# K Stacks in a Single Array

## Problem

Design **K Stacks** using only **one array** of size `n`.

The data structure should support:

```python
push(x, stackNumber)
pop(stackNumber)
```

Every stack should behave exactly like a normal stack.

Example:

Suppose

```text
n = 10

k = 3
```

Instead of creating

```text
Stack1
Stack2
Stack3
```

as three different arrays,

we create only

```text
One Common Array
```

and all stacks share this array dynamically.

---

# Why Not Divide the Array?

A simple idea is:

```text
Array Size = 12

Stack 1 → Index 0-3

Stack 2 → Index 4-7

Stack 3 → Index 8-11
```

Looks easy.

But suppose:

```text
Stack1 uses 4 elements

Stack2 uses only 1 element

Stack3 uses only 1 element
```

Now Stack1 becomes full while Stack2 and Stack3 still have many free cells.

```text
Stack1

10
20
30
40

FULL


Stack2

50

Empty
Empty
Empty


Stack3

60

Empty
Empty
Empty
```

There is still free space inside the array, but Stack1 cannot use it.

This wastes memory.

---

# Main Idea

Instead of reserving fixed space for every stack,

every stack can use **any free index** inside the array.

We maintain:

```text
One Array
        ↓
Free List
        ↓
Every Stack stores only its Top Index
        ↓
next[] connects everything
```

The entire solution depends on four data structures.

```python
arr
top
next
freespot
```

---

# Complete Code with Comments

```python
class kStacks:

    def __init__(self, n, k):

        # ------------------------------------------------
        # arr stores the actual values.
        #
        # Example:
        #
        # Index : 0 1 2 3 4
        # Value : _ _ _ _ _
        # ------------------------------------------------
        self.arr = [0] * n


        # ------------------------------------------------
        # top[i] stores the INDEX of the top element
        # of the i-th stack.
        #
        # Initially every stack is empty.
        # ------------------------------------------------
        self.top = [-1] * k


        # ------------------------------------------------
        # next[] has two purposes:
        #
        # 1. Connect elements inside a stack.
        #
        # 2. Maintain the Free List.
        # ------------------------------------------------
        self.next = [0] * n


        # ------------------------------------------------
        # Initially every index is free.
        #
        # Create the Free List:
        #
        # 0 → 1 → 2 → 3 → ... → n-1
        # ------------------------------------------------
        for i in range(n - 1):
            self.next[i] = i + 1

        self.next[n - 1] = -1


        # ------------------------------------------------
        # First available free location.
        # ------------------------------------------------
        self.freespot = 0


    def push(self, x, i):

        # ------------------------------------------------
        # Overflow
        #
        # No free location is available.
        # ------------------------------------------------
        if self.freespot == -1:
            return False


        # Take first free index
        index = self.freespot


        # Move freespot to the next free index
        self.freespot = self.next[index]


        # Store value
        self.arr[index] = x


        # Connect new node with previous top
        self.next[index] = self.top[i - 1]


        # Make new node the top
        self.top[i - 1] = index

        return True


    def pop(self, i):

        # ------------------------------------------------
        # Underflow
        # ------------------------------------------------
        if self.top[i - 1] == -1:
            return -1


        # Current top index
        index = self.top[i - 1]


        # Move top
        self.top[i - 1] = self.next[index]


        # Return removed index back
        # to Free List
        self.next[index] = self.freespot
        self.freespot = index


        # Return removed value
        return self.arr[index]
```

---

# Data Structures Used

This problem uses four arrays/variables.

```text
arr
top
next
freespot
```

These four together manage every stack.

---

# 1. arr[]

```python
self.arr = [0] * n
```

This stores the actual values.

Example

```text
Index

0   1   2   3   4   5


Value

10  80  30  60  --  --
```

Nothing special happens here.

It is simply the storage array.

---

# 2. top[]

```python
self.top = [-1] * k
```

Every stack stores only one thing:

```text
Top Index
```

Example

```text
top

[4, 2, -1]
```

means

```text
Stack 1 top → Index 4

Stack 2 top → Index 2

Stack 3 is empty
```

Notice something important.

It stores

```text
INDEX

NOT VALUE
```

Many beginners think

```text
top = 60
```

Wrong.

Correct thinking is

```text
top = 4
```

Later

```text
arr[4]
```

contains

```text
60
```

So remember

```text
top
    ↓
Stores INDEX

arr[index]
    ↓
Stores VALUE
```

---

# 3. next[]

This is the heart of the entire problem.

```python
self.next = [0] * n
```

Most beginners think

```text
next[]
```

does only one job.

Actually it performs

```text
TWO JOBS
```

---

## Job 1

When an index belongs to a stack,

```text
next[]
```

acts exactly like

```text
next pointer
```

of a Linked List.

Example

```text
Stack

30
20
10
```

Suppose

```text
30 stored at index 7

20 stored at index 2

10 stored at index 5
```

Then

```text
top

↓

7
↓
2
↓
5
↓
-1
```

is represented using

```text
next[7] = 2

next[2] = 5

next[5] = -1
```

So

```text
next[]
```

connects stack elements.

---

## Job 2

Initially every location is free.

Suppose

```text
n = 6
```

Initially

```text
0
1
2
3
4
5
```

are all unused.

So

```text
next

↓

0 → 1 → 2 → 3 → 4 → 5 → -1
```

This is called

```text
Free List
```

Instead of searching the whole array for an empty cell,

we simply use

```text
freespot
```

to get the first free index in O(1).

---

# 4. freespot

```python
self.freespot = 0
```

This always stores

```text
First Free Index
```

Example

```text
Free List

3 → 6 → 9
```

Then

```text
freespot = 3
```

Whenever we insert,

we simply take

```text
Index = freespot
```

No searching.

No loops.

Everything happens in O(1).

---

# Initialization

Initially

```python
for i in range(n-1):
    self.next[i] = i + 1

self.next[n-1] = -1
```

Suppose

```text
n = 6
```

Initially

```text
Index

0   1   2   3   4   5
```

After initialization

```text
next

1   2   3   4   5   -1
```

Graphically

```text
0
↓

1
↓

2
↓

3
↓

4
↓

5
↓

-1
```

This means

```text
Every location is currently free.
```

Finally

```python
self.freespot = 0
```

means

```text
The first free location is Index 0.
```

---

# Mental Model

Think of the array as a hotel.

```text
arr[]
```

contains rooms.

```text
freespot
```

tells you the first empty room.

```text
top[]
```

tells you where each guest's luggage stack starts.

```text
next[]
```

works like hallways.

If a room is occupied,

the hallway connects it to the next room in that stack.

If a room is empty,

the hallway connects it to the next empty room.

The same hallway (`next[]`) is reused for both purposes.



