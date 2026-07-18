# Next Smaller Element to the Right

## Problem Overview

Given an array, for every element find the **first smaller element on its right side**.

If there is no smaller element on the right, return:

```text
-1
```

Example:

```python
arr = [7, 3, 5, 1, 2]
```

Output:

```text
[3, 1, 1, -1, -1]
```

Explanation:

```text
7 → 3
3 → 1
5 → 1
1 → -1
2 → -1
```

---

# Approach 1 — Brute Force

The simple approach is:

```text
Take one element
      ↓
Check elements on its right
      ↓
Find the first smaller element
      ↓
Store it
```

## Code

```python
arr = [7, 3, 5, 1, 2]

answer = []

for i in range(len(arr)):

    found = -1

    for j in range(i + 1, len(arr)):

        if arr[j] < arr[i]:
            found = arr[j]
            break

    answer.append(found)

print(answer)
```

Output:

```text
[3, 1, 1, -1, -1]
```

---

# Why Do We Use `break`?

Suppose:

```text
arr = [7, 3, 5, 1, 2]
```

For `7`, the elements on the right are:

```text
3, 5, 1, 2
```

The first smaller element is:

```text
3
```

So as soon as we find `3`, we stop:

```python
if arr[j] < arr[i]:
    found = arr[j]
    break
```

We do not continue searching because we need the:

```text
NEXT smaller element
```

not the:

```text
SMALLEST element
```

Therefore:

```text
Next Smaller ≠ Smallest on Right
```

---

# Brute Force Complexity

For every element, we may check all elements on its right.

Therefore:

```text
Time Complexity = O(n²)
```

Ignoring the output array:

```text
Auxiliary Space = O(1)
```

---

# Approach 2 — Optimal Monotonic Stack

The brute-force approach repeatedly searches the right side.

We can optimize it using a:

```text
Monotonic Stack
```

The key idea is:

```text
We need the answer from the RIGHT side.
```

So we process the array:

```text
RIGHT → LEFT
```

While moving from right to left, the Stack stores useful candidates that may be the next smaller element.

---

# Easy-to-Understand Optimal Code

```python
arr = [7, 3, 5, 1, 2]

stack = []
answer = []

# Traverse from right to left
for i in range(len(arr) - 1, -1, -1):

    current = arr[i]

    # Remove elements that are greater than
    # or equal to the current element
    while len(stack) > 0 and stack[-1] >= current:
        stack.pop()

    # No smaller element exists
    if len(stack) == 0:
        answer.append(-1)

    # Stack top is the next smaller element
    else:
        answer.append(stack[-1])

    # Current element may become the answer
    # for an element on its left
    stack.append(current)

# We created the answer from right to left,
# so reverse it to restore the original order
answer.reverse()

print(answer)
```

Output:

```text
[3, 1, 1, -1, -1]
```

---

# Understanding `range(len(arr) - 1, -1, -1)`

This is one of the most important things to understand in this code.

Python's `range()` can take three values:

```python
range(start, stop, step)
```

Meaning:

```text
start → Where to begin

stop  → Where to stop

step  → How much to move each time
```

For our array:

```python
arr = [7, 3, 5, 1, 2]
```

The indices are:

```text
Index:    0   1   2   3   4

Value:    7   3   5   1   2
```

The length is:

```python
len(arr)
```

which is:

```text
5
```

Therefore:

```python
len(arr) - 1
```

is:

```text
4
```

So:

```python
range(len(arr) - 1, -1, -1)
```

becomes:

```python
range(4, -1, -1)
```

Let's understand all three values.

---

## First Value — `len(arr) - 1`

```python
range(4, -1, -1)
      ↑
    start
```

The first value is:

```text
4
```

This means:

```text
Start from index 4
```

Index `4` is the last index:

```text
Index:    0   1   2   3   4
                         ↑
                        Start
```

So the traversal starts from:

```text
arr[4] = 2
```

---

## Second Value — `-1`

```python
range(4, -1, -1)
         ↑
        stop
```

The second value is the:

```text
STOP
```

But there is one very important Python rule:

> The `stop` value in `range()` is not included.

For example:

```python
range(0, 5)
```

produces:

```text
0, 1, 2, 3, 4
```

It does not include:

```text
5
```

Similarly:

```python
range(4, -1, -1)
```

stops before:

```text
-1
```

Therefore, it includes:

```text
0
```

and produces:

```text
4, 3, 2, 1, 0
```

This is why we use:

```text
stop = -1
```

instead of:

```text
stop = 0
```

If we wrote:

```python
range(4, 0, -1)
```

the output would be:

```text
4, 3, 2, 1
```

Index `0` would not be processed.

So remember:

```text
Want to include index 0
        ↓
Stop at -1
```

because the stop value itself is excluded.

---

## Third Value — `-1`

```python
range(4, -1, -1)
             ↑
            step
```

The third value tells Python:

```text
How should I move?
```

Normally:

```python
range(0, 5, 1)
```

moves forward:

```text
0 → 1 → 2 → 3 → 4
```

because:

```text
step = +1
```

But here:

```text
step = -1
```

means:

```text
Move backward by one position.
```

Therefore:

```text
4 → 3 → 2 → 1 → 0
```

So the complete meaning is:

```python
range(len(arr) - 1, -1, -1)
```

```text
START = len(arr) - 1
        ↓
Start from last index


STOP = -1
       ↓
Stop before -1,
so index 0 is included


STEP = -1
       ↓
Move backward one index at a time
```

In short:

```text
range(4, -1, -1)

Start = 4
Stop  = -1 (excluded)
Step  = -1

Result:

4, 3, 2, 1, 0
```

---

# Why Do We Traverse Right to Left?

We need to find:

```text
Next Smaller Element on the RIGHT
```

So when we process an element, it is useful if we have already processed everything on its right.

For:

```text
[7, 3, 5, 1, 2]
```

we process:

```text
2 → 1 → 5 → 3 → 7
```

This means when we reach `5`, we have already processed:

```text
1, 2
```

which are exactly the elements on the right of `5`.

The Stack stores useful information from that processed right side.

Mental model:

```text
Need answer from RIGHT
        ↓
Process RIGHT first
        ↓
Traverse RIGHT → LEFT
```

---

# Understanding the Stack

The Stack stores:

```text
Useful candidates from the right side
```

For each current element, we remove elements that cannot be its next smaller element.

The most important code is:

```python
while len(stack) > 0 and stack[-1] >= current:
    stack.pop()
```

After this loop:

```text
If Stack is empty
        ↓
No smaller element exists


If Stack is not empty
        ↓
Stack Top is the next smaller element
```

---

# Complete Dry Run

Input:

```text
arr = [7, 3, 5, 1, 2]
```

Initial:

```text
stack = []

answer = []
```

Traversal:

```text
2 → 1 → 5 → 3 → 7
```

---

## Current = 2

Stack:

```text
[]
```

The Stack is empty.

So:

```python
answer.append(-1)
```

Answer:

```text
[-1]
```

Push `2`:

```text
stack = [2]
```

---

## Current = 1

Stack:

```text
[2]
```

Check:

```text
2 >= 1
```

True.

So pop `2`.

Stack:

```text
[]
```

No smaller element exists.

Answer:

```text
[-1, -1]
```

Push `1`:

```text
stack = [1]
```

---

## Current = 5

Stack:

```text
[1]
```

Check:

```text
1 >= 5
```

False.

So the Stack top is smaller.

```text
5 → 1
```

Answer:

```text
[-1, -1, 1]
```

Push `5`:

```text
stack = [1, 5]
```

---

## Current = 3

Stack:

```text
[1, 5]
```

Top:

```text
5
```

Check:

```text
5 >= 3
```

True.

Pop `5`.

Stack:

```text
[1]
```

Check again:

```text
1 >= 3
```

False.

So:

```text
3 → 1
```

Answer:

```text
[-1, -1, 1, 1]
```

Push `3`:

```text
stack = [1, 3]
```

---

## Current = 7

Stack:

```text
[1, 3]
```

Top:

```text
3
```

Check:

```text
3 >= 7
```

False.

So:

```text
7 → 3
```

Answer:

```text
[-1, -1, 1, 1, 3]
```

Push `7`:

```text
stack = [1, 3, 7]
```

---

# Why Do We Reverse the Answer?

We processed the array from:

```text
RIGHT → LEFT
```

So answers were added in this order:

```text
2 → -1
1 → -1
5 → 1
3 → 1
7 → 3
```

Therefore:

```text
answer = [-1, -1, 1, 1, 3]
```

But the original array order is:

```text
7, 3, 5, 1, 2
```

So we reverse:

```python
answer.reverse()
```

Now:

```text
[3, 1, 1, -1, -1]
```

which matches the original array order.

---

# Understanding the `while` Condition

```python
while len(stack) > 0 and stack[-1] >= current:
    stack.pop()
```

We want a:

```text
SMALLER element
```

Therefore, anything that is:

```text
Greater than current
```

or:

```text
Equal to current
```

cannot be the answer.

So we remove it.

We continue removing until:

```text
Stack becomes empty
```

or:

```text
Stack top < current
```

At that point, the Stack top is our answer.

---

# Why Do We Need `while` Instead of `if`?

Suppose:

```text
stack = [1, 4, 5, 6]

current = 3
```

We need to remove:

```text
6
5
4
```

Using:

```python
if stack[-1] >= current:
    stack.pop()
```

would remove only:

```text
6
```

But `5` and `4` are also useless.

Therefore, we need:

```python
while stack and stack[-1] >= current:
    stack.pop()
```

The `while` loop keeps removing until a valid smaller element is found.

---

# Why Do We Push `current`?

At the end:

```python
stack.append(current)
```

The current element may become the next smaller element for an element on its left.

For example:

```text
[7, 3]
```

When processing `3`, there is no smaller element on its right.

But we still push:

```text
3
```

Later, when processing `7`:

```text
7 → 3
```

So remember:

```text
The current element may not have an answer,
but it may become an answer for someone else.
```

---

# Time Complexity

Each element is:

```text
Pushed once
```

and:

```text
Popped at most once
```

Therefore:

```text
Time Complexity = O(n)
```

Even though there is a `while` loop inside a `for` loop, it is not O(n²), because an element cannot be popped multiple times after it has already been removed.

---

# Space Complexity

The Stack can contain up to `n` elements.

Therefore:

```text
Auxiliary Space Complexity = O(n)
```

The answer array also requires:

```text
O(n)
```

---

# Brute Force vs Optimal

| Approach        | Time Complexity | Auxiliary Space |
| --------------- | --------------: | --------------: |
| Brute Force     |           O(n²) |            O(1) |
| Monotonic Stack |            O(n) |            O(n) |

---

# Pattern Used

For your DSA pattern sheet:

```text
Monotonic Stack + Right-to-Left Traversal
```

Short version:

```text
Next Smaller → Monotonic Stack
```

---

# Easy Template to Remember

```python
stack = []
answer = []

for i in range(len(arr) - 1, -1, -1):

    current = arr[i]

    # Remove useless elements
    while len(stack) > 0 and stack[-1] >= current:
        stack.pop()

    # Find answer
    if len(stack) == 0:
        answer.append(-1)
    else:
        answer.append(stack[-1])

    # Current may help elements on the left
    stack.append(current)

answer.reverse()
```

Remember this flow:

```text
RIGHT → LEFT
      ↓
POP useless elements
      ↓
STACK EMPTY?
   /       \
 Yes       No
  ↓         ↓
 -1      Stack Top
      ↓
PUSH current
      ↓
REVERSE answer at end
```

---

# Key Learning

The complete thinking is:

```text
1. We need the answer from the right side.

2. Therefore, traverse Right → Left.

3. The Stack stores useful candidates
   from the right side.

4. Remove elements greater than or equal
   to the current element.

5. After removing useless elements:

   Empty Stack → Answer is -1

   Non-Empty Stack → Top is the answer

6. Push the current element because it may
   help an element on its left.

7. Since answers are added Right → Left,
   reverse the answer at the end.
```

And remember the reverse `range()`:

```text
range(len(arr) - 1, -1, -1)

START → Last index

STOP  → -1, excluded,
        so index 0 is included

STEP  → -1,
        so move backward
```

The strongest mental model is:

```text
Need Next Smaller on RIGHT
        ↓
Go RIGHT → LEFT
        ↓
Remove elements that are NOT smaller
        ↓
Stack Top gives the answer
        ↓
Push current for future elements
```
