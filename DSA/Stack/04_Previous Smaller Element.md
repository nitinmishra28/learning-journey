# Previous Smaller Element

## Problem Overview

Given an array, for every element find the **nearest smaller element on its left side**.

If there is no smaller element on the left, return:

```text
-1
```

Example:

```python
arr = [8, 4, 2, 6, 3]
```

Expected output:

```text
[-1, -1, -1, 2, 2]
```

Explanation:

```text
8 → -1

4 → -1

2 → -1

6 → 2

3 → 2
```

---

# Important Correction in the Code

Your current code is:

```python
arr = [8, 4, 2, 6, 3]

stack = []
ans = []

for i in range(len(arr)):

    curr = arr[i]

    while len(stack) > 0 and stack[-1] > curr:
        stack.pop()

    if len(stack) == 0:
        ans.append(-1)

    else:
        ans.append(stack[-1])

    stack.append(curr)

ans.reverse()

print(ans)
```

There are two important points.

## 1. Do Not Reverse the Answer

You are traversing:

```text
LEFT → RIGHT
```

The answers are already being stored in the correct order.

Therefore:

```python
ans.reverse()
```

should be removed.

---

## 2. Use `>=` for Strictly Smaller

If the problem asks for:

```text
Previous Smaller Element
```

then an equal element is not smaller.

Therefore use:

```python
stack[-1] >= curr
```

instead of:

```python
stack[-1] > curr
```

---

# Correct Optimal Code

```python
arr = [8, 4, 2, 6, 3]

stack = []
ans = []

# Traverse from left to right
for i in range(len(arr)):

    current = arr[i]

    # Remove elements that are greater than
    # or equal to the current element
    while len(stack) > 0 and stack[-1] >= current:
        stack.pop()

    # No smaller element exists on the left
    if len(stack) == 0:
        ans.append(-1)

    # Stack top is the previous smaller element
    else:
        ans.append(stack[-1])

    # Current element may become the answer
    # for elements on its right
    stack.append(current)


print(ans)
```

Output:

```text
[-1, -1, -1, 2, 2]
```

---

# Core Idea

For **Next Smaller Element**, we needed information from the right:

```text
Need answer from RIGHT
        ↓
Traverse RIGHT → LEFT
```

For **Previous Smaller Element**, we need information from the left:

```text
Need answer from LEFT
        ↓
Traverse LEFT → RIGHT
```

This is the most important difference.

---

# Why Traverse Left to Right?

Suppose:

```text
arr = [8, 4, 2, 6, 3]
```

When we are processing:

```text
6
```

we need to search among:

```text
8, 4, 2
```

These are the elements on its:

```text
LEFT
```

If we traverse:

```text
LEFT → RIGHT
```

then all these elements have already been processed.

The Stack contains useful candidates from the left side.

So:

```text
Need Previous Element
        ↓
Process Previous Elements First
        ↓
Traverse Left → Right
```

---

# Understanding the Stack

The Stack stores:

```text
Useful smaller candidates
from the LEFT side
```

For every current element:

```text
Remove useless elements
        ↓
Check Stack Top
        ↓
Store Answer
        ↓
Push Current
```

The core code is:

```python
while len(stack) > 0 and stack[-1] >= current:
    stack.pop()
```

After this loop finishes:

```text
Stack Empty
    ↓
No previous smaller element
    ↓
Answer = -1
```

Otherwise:

```text
Stack Not Empty
    ↓
Stack Top < Current
    ↓
Stack Top = Previous Smaller
```

---

# Complete Dry Run

Input:

```text
arr = [8, 4, 2, 6, 3]
```

Initially:

```text
stack = []

ans = []
```

Traversal:

```text
8 → 4 → 2 → 6 → 3
```

---

## Current Element = 8

Stack:

```text
[]
```

There is nothing on the left.

So:

```text
8 → -1
```

Answer:

```text
[-1]
```

Push `8`:

```text
stack = [8]
```

---

## Current Element = 4

Stack:

```text
[8]
```

Check:

```text
8 >= 4
```

True.

So remove `8`.

```text
stack = []
```

No smaller element exists.

Therefore:

```text
4 → -1
```

Answer:

```text
[-1, -1]
```

Push `4`:

```text
stack = [4]
```

---

## Current Element = 2

Stack:

```text
[4]
```

Check:

```text
4 >= 2
```

True.

Pop `4`.

Stack:

```text
[]
```

No smaller element exists.

Therefore:

```text
2 → -1
```

Answer:

```text
[-1, -1, -1]
```

Push `2`:

```text
stack = [2]
```

---

## Current Element = 6

Stack:

```text
[2]
```

Check:

```text
2 >= 6
```

False.

So `2` is smaller than `6`.

Therefore:

```text
6 → 2
```

Answer:

```text
[-1, -1, -1, 2]
```

Push `6`:

```text
stack = [2, 6]
```

---

## Current Element = 3

Stack:

```text
[2, 6]
```

Check the top:

```text
6 >= 3
```

True.

Pop `6`.

Stack becomes:

```text
[2]
```

Check again:

```text
2 >= 3
```

False.

So:

```text
3 → 2
```

Answer:

```text
[-1, -1, -1, 2, 2]
```

Push `3`:

```text
stack = [2, 3]
```

Final answer:

```text
[-1, -1, -1, 2, 2]
```

---

# Why Do We Use a `while` Loop?

Consider:

```text
stack = [2, 5, 7, 9]

current = 4
```

We need a smaller element than `4`.

Stack top:

```text
9
```

Not useful.

Pop it:

```text
[2, 5, 7]
```

Now top:

```text
7
```

Still not useful.

Pop:

```text
[2, 5]
```

Top:

```text
5
```

Still not useful.

Pop:

```text
[2]
```

Now:

```text
2 < 4
```

So the answer is:

```text
2
```

This is why we need:

```python
while stack and stack[-1] >= current:
    stack.pop()
```

and not just:

```python
if stack and stack[-1] >= current:
    stack.pop()
```

There can be multiple useless elements that need to be removed.

---

# Why Do We Pop `>= current`?

We want a:

```text
STRICTLY SMALLER
```

element.

Therefore, the valid condition is:

```text
stack[-1] < current
```

So everything that does not satisfy this condition must be removed:

```text
stack[-1] >= current
```

That gives us:

```python
while stack and stack[-1] >= current:
    stack.pop()
```

Remember:

```text
Want Smaller
    ↓
Keep <
    ↓
Pop >=
```

---

# Why Not Use Only `>`?

Suppose:

```text
arr = [5, 5]
```

If we use:

```python
stack[-1] > current
```

then for the second `5`:

```text
5 > 5
```

is false.

So `5` remains in the Stack and becomes the answer.

We would incorrectly get:

```text
[-1, 5]
```

But `5` is not smaller than `5`.

The correct answer is:

```text
[-1, -1]
```

Therefore:

```text
Strictly Smaller
      ↓
Use >= while popping
```

---

# Why Is the Stack Top the Answer?

After this loop:

```python
while stack and stack[-1] >= current:
    stack.pop()
```

all elements on top that are not smaller have been removed.

Therefore, if the Stack still contains something:

```text
stack[-1] < current
```

The Stack top is the nearest useful smaller candidate from the left.

So:

```python
ans.append(stack[-1])
```

---

# Why Push the Current Element?

After finding the answer:

```python
stack.append(current)
```

The current element may become the previous smaller element for some future element.

Example:

```text
[2, 6]
```

For `2`:

```text
Previous Smaller = -1
```

But we still push `2`.

Later, for `6`:

```text
Previous Smaller = 2
```

So:

```text
Current may not have an answer
        ↓
But current may become an answer
for future elements
```

---

# Why Don't We Reverse `ans`?

For Next Smaller to Right, we traversed:

```text
RIGHT → LEFT
```

So answers were created backward.

Therefore we needed:

```python
answer.reverse()
```

But here we traverse:

```text
LEFT → RIGHT
```

which is the same order as the original array.

For:

```text
[8, 4, 2, 6, 3]
```

we calculate answers in exactly this order:

```text
8
4
2
6
3
```

So:

```text
ans = [-1, -1, -1, 2, 2]
```

is already correct.

Therefore:

```python
ans.reverse()
```

is not required.

---

# Next Smaller vs Previous Smaller

This is the easiest way to remember both problems.

## Next Smaller to Right

```text
Need answer from RIGHT
        ↓
Traverse RIGHT → LEFT
```

Template:

```python
for i in range(len(arr) - 1, -1, -1):
```

If using `append()` for answers:

```python
answer.reverse()
```

at the end.

---

## Previous Smaller to Left

```text
Need answer from LEFT
        ↓
Traverse LEFT → RIGHT
```

Template:

```python
for i in range(len(arr)):
```

No answer reversal is needed.

---

# Comparison

| Problem                  | Answer Side | Traversal    |
| ------------------------ | ----------- | ------------ |
| Next Smaller Element     | Right       | Right → Left |
| Previous Smaller Element | Left        | Left → Right |

The Stack logic is almost the same:

```python
while stack and stack[-1] >= current:
    stack.pop()
```

The main thing that changes is the:

```text
Traversal Direction
```

---

# Time Complexity

Every element is pushed into the Stack once.

Every element can also be popped at most once.

Therefore:

```text
Total Pushes ≤ n

Total Pops ≤ n
```

So:

```text
Time Complexity = O(n)
```

Even though there is a `while` loop inside the `for` loop, the overall complexity is not O(n²).

---

# Space Complexity

In the worst case, the Stack may contain all elements.

Therefore:

```text
Auxiliary Space Complexity = O(n)
```

The answer array also uses:

```text
O(n)
```

space.

---

# Pattern Used

For your DSA pattern sheet:

```text
Monotonic Stack + Left-to-Right Traversal
```

Short version:

```text
Previous Smaller → Monotonic Stack
```

---

# Easy Template to Remember

```python
stack = []
answer = []

for i in range(len(arr)):

    current = arr[i]

    # Remove useless elements
    while stack and stack[-1] >= current:
        stack.pop()

    # Find answer
    if not stack:
        answer.append(-1)
    else:
        answer.append(stack[-1])

    # Current may help future elements
    stack.append(current)
```

The flow is:

```text
LEFT → RIGHT
      ↓
POP elements >= current
      ↓
STACK EMPTY?
   /       \
 Yes       No
  ↓         ↓
 -1      Stack Top
      ↓
PUSH current
```

---

# Key Learning

The complete thinking is:

```text
1. We need the answer from the LEFT side.

2. Therefore, traverse LEFT → RIGHT.

3. Stack stores useful candidates
   from the already processed left side.

4. Remove elements greater than or equal
   to the current element.

5. After popping:

   Empty Stack
       ↓
   Answer = -1

   Non-Empty Stack
       ↓
   Answer = Stack Top

6. Push current because it may become
   the answer for future elements.

7. Do NOT reverse the answer because
   traversal is already Left → Right.
```

The strongest mental model is:

```text
Need Previous Smaller on LEFT
        ↓
Go LEFT → RIGHT
        ↓
Remove elements that are NOT smaller
        ↓
Stack Top gives the answer
        ↓
Push current for future elements
```

## Quick Pattern Connection

```text
NEXT smaller on RIGHT
        ↓
Right → Left


PREVIOUS smaller on LEFT
        ↓
Left → Right
```

Once you understand this direction rule, both problems use almost the same Monotonic Stack logic.
