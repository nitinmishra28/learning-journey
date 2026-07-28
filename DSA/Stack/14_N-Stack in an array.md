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



# K Stacks in a Single Array (Part 2)

# Push Operation

The complete push flow is:

```text
Need to insert x
        ↓
Take first free index
        ↓
Move freespot
        ↓
Store value
        ↓
Connect with old top
        ↓
Update top
```

Suppose initially:

```text
arr

Index:
0   1   2   3   4   5

Value:
_   _   _   _   _   _


top

[-1, -1]


next

1   2   3   4   5   -1


freespot

0
```

Everything is empty.

---

# Step 1 : Overflow Check

```python
if self.freespot == -1:
    return False
```

If

```text
freespot = -1
```

there is no empty location left.

That means the whole array is full.

Example

```text
Free List

-1
```

No insertion is possible.

So we simply return

```text
False
```

---

# Step 2 : Take First Free Index

```python
index = self.freespot
```

Suppose

```text
Free List

0 → 1 → 2 → 3 → 4
```

Current

```text
freespot = 0
```

Then

```python
index = 0
```

This index will store the new value.

Think of it as:

```text
Reservation

First empty room
        ↓
Take it
```

---

# Step 3 : Move freespot

```python
self.freespot = self.next[index]
```

This line is extremely important.

Suppose

```text
Before

Free List

0 → 1 → 2 → 3
```

After taking index

```text
0
```

the new Free List becomes

```text
1 → 2 → 3
```

Therefore

```text
freespot = 1
```

Graphically

Before

```text
freespot

↓

0 → 1 → 2 → 3
```

After

```text
freespot

↓

1 → 2 → 3
```

Remember

```text
Current free index used
        ↓
Move freespot
```

---

# Step 4 : Store Value

```python
self.arr[index] = x
```

Suppose

```text
Push(50)
```

Then

```text
arr

Index

0 1 2 3

Value

50 _ _ _
```

Very simple.

---

# Step 5 : Connect New Node

```python
self.next[index] = self.top[i-1]
```

This is the hardest line in the whole algorithm.

Suppose Stack 1 already contains

```text
20
10
```

Stored as

```text
Index

4
↓

2
```

Current

```text
top = 4
```

Now new value

```text
30
```

comes.

Suppose it is stored at

```text
index = 7
```

Then

```python
next[7] = 4
```

Now

```text
7
↓

4
↓

2
↓

-1
```

Notice something.

The new node points to the old top.

Exactly like insertion at the head of a Linked List.

Remember

```text
New Node
      ↓
Points to Old Top
```

---

# Step 6 : Update Top

```python
self.top[i-1] = index
```

After connecting

```text
7 → 4 → 2
```

the new top becomes

```text
7
```

Graphically

Before

```text
Top

↓

4
↓

2
```

After

```text
Top

↓

7
↓

4
↓

2
```

Insertion completed.

---

# Complete Push Dry Run

Suppose

```text
n = 5

k = 2
```

Initially

```text
arr

_ _ _ _ _

top

[-1,-1]

next

1 2 3 4 -1

freespot

0
```

Push

```text
10
```

into Stack 1.

Step 1

```text
index = 0
```

Step 2

```text
freespot = 1
```

Step 3

```text
arr

10 _ _ _ _
```

Step 4

```text
next[0] = -1
```

because Stack 1 was empty.

Step 5

```text
top[0] = 0
```

Final State

```text
arr

10 _ _ _ _

top

[0,-1]

next

-1 2 3 4 -1

freespot

1
```

---

# Pop Operation

The complete flow

```text
Current Top
      ↓
Move Top
      ↓
Return removed index
to Free List
      ↓
Return value
```

---

# Step 1 : Underflow Check

```python
if self.top[i-1] == -1:
    return -1
```

If

```text
top = -1
```

the stack is empty.

Nothing can be removed.

---

# Step 2 : Store Top Index

```python
index = self.top[i-1]
```

Suppose

```text
Top

↓

7
↓

4
↓

2
```

Current top is

```text
7
```

Store it.

```python
index = 7
```

---

# Step 3 : Move Top

```python
self.top[i-1] = self.next[index]
```

Suppose

```text
7
↓

4
↓

2
```

After removing

```text
7
```

Top becomes

```text
4
```

Graphically

Before

```text
Top

↓

7
↓

4
↓

2
```

After

```text
Top

↓

4
↓

2
```

---

# Step 4 : Return Index to Free List

```python
self.next[index] = self.freespot
self.freespot = index
```

This line confuses almost everyone.

Suppose current Free List is

```text
5
↓

6
↓

8
```

Now removed index is

```text
7
```

We don't throw it away.

Instead we make it reusable.

First

```python
next[7] = 5
```

Now

```text
7
↓

5
↓

6
↓

8
```

Then

```python
freespot = 7
```

Graphically

Before

```text
freespot

↓

5
↓

6
↓

8
```

After

```text
freespot

↓

7
↓

5
↓

6
↓

8
```

Remember

```text
Removed node
        ↓
Becomes first free node
```

---

# Step 5 : Return Value

```python
return self.arr[index]
```

Suppose

```text
arr[7] = 30
```

Return

```text
30
```

The value stays in the array physically, but logically that index is now free and may be overwritten by a future push.

---

# Push vs Pop

## Push

```text
Take Free Index
        ↓
Move freespot
        ↓
Store Value
        ↓
Point to Old Top
        ↓
Update Top
```

---

## Pop

```text
Take Top
      ↓
Move Top
      ↓
Return Removed Index
to Free List
      ↓
Return Value
```

---

# Mental Trick

Think of **freespot** as a queue of empty chairs.

Whenever you push:

```text
Take first empty chair
        ↓
Sit there
        ↓
Tell freespot where the next empty chair is
```

Whenever you pop:

```text
Vacate your chair
        ↓
Put that chair back
at the front of
the empty-chair list
```

No searching is ever needed.

Everything happens in constant time.
