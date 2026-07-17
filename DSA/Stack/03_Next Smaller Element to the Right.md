# Next Smaller Element to the Right

## Problem Overview

Given an array, for every element find the **first smaller element present on its right side**.

If no smaller element exists on the right, return:

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

---

# Understanding the Problem

For every element, we need to look toward its:

```text
RIGHT SIDE
```

and find the:

```text
FIRST SMALLER ELEMENT
```

For:

```text
[7, 3, 5, 1, 2]
```

### For `7`

Elements on the right:

```text
3, 5, 1, 2
```

The first smaller element is:

```text
3
```

So:

```text
7 → 3
```

---

### For `3`

Elements on the right:

```text
5, 1, 2
```

`5` is not smaller.

The next element `1` is smaller.

So:

```text
3 → 1
```

---

### For `5`

Elements on the right:

```text
1, 2
```

The first smaller element is:

```text
1
```

So:

```text
5 → 1
```

---

### For `1`

Elements on the right:

```text
2
```

There is no smaller element.

So:

```text
1 → -1
```

---

### For `2`

There are no elements on the right.

So:

```text
2 → -1
```

Final answer:

```text
[3, 1, 1, -1, -1]
```

---

# Approach 1 — Brute Force

Your approach uses two loops.

For every element:

```text
Look at every element on its right
        ↓
Find the first smaller element
        ↓
Stop immediately
        ↓
Store the answer
```

---

# Brute Force Code

```python
arr = [7, 3, 5, 1, 2]

answer = []

for i in range(len(arr)):

    # Assume no smaller element exists
    found = -1

    # Search on the right side
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

# How the Brute Force Approach Works

The outer loop selects the current element:

```python
for i in range(len(arr)):
```

The inner loop starts from:

```python
i + 1
```

because we only need to search on the right side.

```python
for j in range(i + 1, len(arr)):
```

Then:

```python
if arr[j] < arr[i]:
```

checks whether we found a smaller element.

The moment we find one:

```python
found = arr[j]
break
```

we stop searching.

The `break` is important because the problem asks for the:

```text
NEXT / FIRST smaller element
```

not the smallest element on the entire right side.

---

# Important Difference — Next Smaller vs Smallest on Right

Suppose:

```text
[7, 5, 2, 1]
```

For `7`, the next smaller element is:

```text
5
```

not:

```text
1
```

Because `5` is the first smaller element encountered on the right.

So:

```text
Next Smaller ≠ Minimum on Right
```

---

# Brute Force Complexity

The outer loop runs:

```text
n times
```

For every element, the inner loop may also run approximately:

```text
n times
```

Therefore:

```text
Time Complexity = O(n²)
```

The answer array requires:

```text
Space Complexity = O(n)
```

Ignoring the output array, auxiliary space is:

```text
O(1)
```

---

# Approach 2 — Optimal Monotonic Stack

The optimal solution uses a:

```text
Monotonic Stack
```

Time Complexity:

```text
O(n)
```

The key observation is:

```text
We need information from the RIGHT side.
```

So instead of traversing:

```text
Left → Right
```

we traverse:

```text
Right → Left
```

This way, when processing an element, the Stack already contains useful elements from its right side.

---

# Optimal Code

```python
arr = [7, 3, 5, 1, 2]

stack = []
answer = [-1] * len(arr)

for i in range(len(arr) - 1, -1, -1):

    # Remove elements that cannot be the answer
    while stack and stack[-1] >= arr[i]:
        stack.pop()

    # If stack is not empty,
    # top is the next smaller element
    if stack:
        answer[i] = stack[-1]

    # Current element may become the
    # next smaller element for elements on its left
    stack.append(arr[i])

print(answer)
```

Output:

```text
[3, 1, 1, -1, -1]
```

---

# Core Pattern

The optimal solution follows:

```text
Traverse Right → Left

        ↓

Remove useless elements

        ↓

Stack Top = Answer

        ↓

Push Current Element
```

In code:

```python
while stack and stack[-1] >= arr[i]:
    stack.pop()

answer[i] = stack[-1] if stack else -1

stack.append(arr[i])
```

This is the core template for this problem.

---

# Why Traverse Right to Left?

Suppose we are currently processing:

```text
5
```

in:

```text
[7, 3, 5, 1, 2]
```

We need to know what exists on the right of `5`:

```text
1, 2
```

If we traverse from right to left, these elements have already been processed.

So the Stack contains information about:

```text
Elements on the right
```

This is why reverse traversal is useful.

Mental model:

```text
Need answer from right side
        ↓
Process right side first
        ↓
Traverse Right → Left
```

---

# Understanding the Most Important `while` Loop

The most important part is:

```python
while stack and stack[-1] >= arr[i]:
    stack.pop()
```

Ask:

```text
What are we looking for?
```

Answer:

```text
A SMALLER element
```

Therefore, if the Stack top is:

```text
Greater than current
```

or:

```text
Equal to current
```

it cannot be the answer.

So we remove it.

The condition is:

```text
stack[-1] >= arr[i]
```

because we want:

```text
stack[-1] < arr[i]
```

to remain.

After the `while` loop finishes, if the Stack is not empty:

```text
stack[-1] < arr[i]
```

Therefore, the top is the next useful smaller element.

---

# Complete Dry Run

Input:

```text
arr = [7, 3, 5, 1, 2]
```

We traverse:

```text
2 → 1 → 5 → 3 → 7
```

Initial:

```text
stack = []

answer = [-1, -1, -1, -1, -1]
```

---

## Current Element = 2

Stack:

```text
[]
```

No element exists on the right.

Answer:

```text
2 → -1
```

Push `2`:

```text
stack = [2]
```

---

## Current Element = 1

Stack:

```text
[2]
```

Check:

```text
2 >= 1
```

True.

Pop `2`.

Stack:

```text
[]
```

No smaller element remains.

Answer:

```text
1 → -1
```

Push `1`:

```text
stack = [1]
```

---

## Current Element = 5

Stack:

```text
[1]
```

Check:

```text
1 >= 5
```

False.

So `1` is smaller than `5`.

Answer:

```text
5 → 1
```

Push `5`:

```text
stack = [1, 5]
```

Remember:

```text
RIGHTMOST SIDE = STACK BOTTOM
MOST RECENT ELEMENT = STACK TOP
```

---

## Current Element = 3

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

So pop `5`.

Stack becomes:

```text
[1]
```

Now check:

```text
1 >= 3
```

False.

So:

```text
3 → 1
```

Push `3`:

```text
stack = [1, 3]
```

---

## Current Element = 7

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

Push `7`:

```text
stack = [1, 3, 7]
```

Final answer:

```text
[3, 1, 1, -1, -1]
```

---

# Why Can We Pop Elements Permanently?

This is the most important Monotonic Stack concept.

Consider:

```text
Current = 3

Stack = [1, 5]
```

The top is:

```text
5
```

Since:

```text
5 >= 3
```

`5` cannot be the next smaller element for `3`.

So we remove it.

But why can we remove it permanently?

Because `3` is:

```text
Smaller than 5
```

and:

```text
Closer to all future elements on the left
```

Therefore, `5` becomes useless.

For any future element on the left, if `5` could have been useful as a smaller element, then `3` is even better because:

```text
3 < 5
```

and `3` appears closer.

This is called:

```text
Removing Dominated / Useless Candidates
```

That is the main idea behind Monotonic Stack optimization.

---

# Why Do We Push the Current Element?

After finding the answer for:

```text
arr[i]
```

we do:

```python
stack.append(arr[i])
```

Why?

Because the current element may become the next smaller element for some element on its left.

Example:

```text
[7, 3]
```

When processing `3`:

```text
3 → no smaller element
```

But we still push `3`.

Later, when processing `7`:

```text
7 → 3
```

So:

```text
Current element may not have an answer,
but it may become an answer for someone else.
```

This is an important Monotonic Stack idea.

---

# What Does the Stack Store?

In this solution:

```text
The Stack stores useful candidates
from the right side.
```

More specifically:

```text
Elements that may become the
Next Smaller Element for future elements
on the left.
```

Before writing Monotonic Stack code, always complete this sentence:

```text
"My Stack stores __________."
```

For this problem:

```text
"My Stack stores useful smaller candidates
from the right side."
```

---

# Why Is This a Monotonic Stack?

After processing elements, the Stack maintains a useful monotonic order.

Because we remove:

```python
stack[-1] >= arr[i]
```

before pushing the current element.

The Stack maintains candidates so that useless larger or equal values are removed.

The important thing is not just memorizing:

```text
Increasing Stack
```

Instead understand:

```text
Remove everything that cannot be
the answer for the current element.
```

That is the real Monotonic Stack idea.

---

# Why Use `>=` Instead of `>`?

The problem asks for:

```text
Next SMALLER Element
```

Suppose:

```text
[5, 5, 3]
```

For the first `5`, another `5` is not smaller.

Therefore equal values cannot be answers.

So we remove them using:

```python
while stack and stack[-1] >= arr[i]:
```

If we used:

```python
stack[-1] > arr[i]
```

then equal values would remain.

That would incorrectly treat:

```text
5
```

as smaller than:

```text
5
```

So:

```text
Strictly Smaller
        ↓
Pop >=
```

This is an important pattern.

---

# Why Is the Optimal Solution O(n)?

At first, this code looks like it might be O(n²):

```python
for i in range(...):

    while stack:
        stack.pop()
```

But every element is:

```text
Pushed exactly once
```

and:

```text
Popped at most once
```

For example, if there are `n` elements:

```text
Maximum Push Operations = n

Maximum Pop Operations = n
```

Therefore, the total number of Stack operations is proportional to:

```text
2n
```

Ignoring constants:

```text
Time Complexity = O(n)
```

This is called:

```text
Amortized Analysis
```

---

# Space Complexity

In the worst case, the Stack may contain all elements.

For example:

```text
[1, 2, 3, 4, 5]
```

during reverse traversal.

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

| Approach        |  Time | Auxiliary Space |
| --------------- | ----: | --------------: |
| Brute Force     | O(n²) |            O(1) |
| Monotonic Stack |  O(n) |            O(n) |

The optimization changes the thinking from:

```text
For every element
    ↓
Search the complete right side again
```

to:

```text
Process right side once
    ↓
Keep only useful candidates
    ↓
Reuse that information
```

---

# Common Mistake — Finding the Smallest Instead of Next Smaller

For:

```text
[7, 3, 1]
```

The answer for `7` is:

```text
3
```

not:

```text
1
```

Because we need the:

```text
First smaller element on the right
```

not the minimum element.

---

# Common Mistake — Traversing Left to Right With This Exact Pattern

The answer exists on the:

```text
RIGHT
```

So in this approach, we process:

```text
Right → Left
```

This ensures that when we process the current element, the Stack already contains candidates from its right.

---

# Common Mistake — Using Only `if`

Wrong:

```python
if stack and stack[-1] >= arr[i]:
    stack.pop()
```

Why?

Because there may be multiple useless elements.

Example:

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

Using `if` removes only one element.

So we need:

```python
while stack and stack[-1] >= arr[i]:
    stack.pop()
```

The `while` continues until the Stack top becomes a valid smaller candidate or the Stack becomes empty.

---

# Pattern Used

For your DSA sheet, use:

```text
Monotonic Stack + Right-to-Left Traversal
```

A shorter version:

```text
Next Smaller → Monotonic Stack
```

The core template is:

```python
for i in range(n - 1, -1, -1):

    while stack and stack[-1] >= arr[i]:
        stack.pop()

    answer[i] = stack[-1] if stack else -1

    stack.append(arr[i])
```

---

# Key Learning

The brute-force thinking is:

```text
For every element
        ↓
Search right side
        ↓
Find first smaller
```

The optimized thinking is:

```text
Traverse Right → Left
        ↓
Keep useful candidates in Stack
        ↓
Remove candidates >= current
        ↓
Stack Top = Next Smaller
        ↓
Push Current
```

The most important questions to ask are:

```text
1. Where is my answer?

   Right side


2. Which direction should I traverse?

   Right → Left


3. What does my Stack store?

   Useful candidates from the right


4. What should I remove?

   Elements >= current


5. Why remove them?

   They cannot be the required smaller answer


6. What is my answer?

   Stack top after removing useless elements


7. Why push current?

   It may become an answer for elements on the left
```

The strongest mental model is:

```text
NEED ANSWER FROM RIGHT
        ↓
TRAVERSE RIGHT TO LEFT
        ↓
REMOVE USELESS CANDIDATES
        ↓
STACK TOP IS THE ANSWER
        ↓
PUSH CURRENT FOR FUTURE
```
