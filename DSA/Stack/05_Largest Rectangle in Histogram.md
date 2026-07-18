# Largest Rectangle in Histogram

## Problem

Given an array `heights`, where each value represents the height of a histogram bar, find the largest rectangular area that can be formed.

Example:

```text
heights = [2, 1, 5, 6, 2, 3]
```

For every bar, we find how far that bar can expand toward the:

```text
Left  ← Current Bar →  Right
```

The rectangle can expand until we find a bar that is **smaller than the current bar**.

So for every bar we need:

```text
Previous Smaller Index
Next Smaller Index
```

Then:

```text
Width = Next Smaller Index - Previous Smaller Index - 1

Area = Height × Width
```

---

# Code with Comments

```python
class Solution:

    # Find index of Next Smaller Element for every bar
    def nextSmallest(self, heights, nxt, stack):

        # Next smaller is on the RIGHT,
        # so traverse from right to left
        for i in range(len(heights) - 1, -1, -1):

            curr = heights[i]

            # Stack stores INDICES.
            #
            # Remove bars that are greater than or equal
            # to the current bar because we need a
            # strictly smaller bar.
            while len(stack) > 0 and heights[stack[-1]] >= curr:
                stack.pop()

            # No smaller bar exists on the right
            if len(stack) == 0:
                nxt.append(-1)

            # Stack top contains the INDEX
            # of the next smaller bar
            else:
                nxt.append(stack[-1])

            # Store INDEX, not value
            stack.append(i)


    # Find index of Previous Smaller Element for every bar
    def prevSmallest(self, heights, prev, stack):

        # Previous smaller is on the LEFT,
        # so traverse from left to right
        for i in range(len(heights)):

            curr = heights[i]

            # Remove bars greater than or equal
            # to the current bar
            while len(stack) > 0 and heights[stack[-1]] >= curr:
                stack.pop()

            # No smaller bar exists on the left
            if len(stack) == 0:
                prev.append(-1)

            # Stack top contains the INDEX
            # of the previous smaller bar
            else:
                prev.append(stack[-1])

            # Store current bar's index
            stack.append(i)


    def largestRectangleArea(self, heights: List[int]) -> int:

        nxt = []
        prev = []

        stack = []

        # Find Next Smaller Index
        self.nextSmallest(heights, nxt, stack)

        # nextSmallest traverses right → left,
        # so answers were appended in reverse order
        nxt.reverse()


        # If no smaller element exists on the right,
        # imagine a boundary just after the array.
        #
        # Last valid index = n - 1
        # Virtual right boundary = n
        for i in range(len(nxt)):
            if nxt[i] == -1:
                nxt[i] = len(heights)


        # IMPORTANT:
        # Clear the stack before calculating previous smaller.
        #
        # Otherwise old indices from nextSmallest()
        # will still be present.
        stack = []


        # Find Previous Smaller Index
        self.prevSmallest(heights, prev, stack)


        maxArea = 0

        # Calculate area using every bar as the height
        for i in range(len(heights)):

            # Number of bars between the two
            # smaller boundaries
            width = nxt[i] - prev[i] - 1

            height = heights[i]

            currArea = width * height

            maxArea = max(maxArea, currArea)


        return maxArea
```

---

# Main Pattern

This problem uses:

```text
Monotonic Stack
+
Next Smaller Index
+
Previous Smaller Index
```

The important point is:

```text
We need the INDEX of the smaller elements,
not just their values.
```

---

# Why Do We Store Indices Instead of Values?

In basic Next Smaller Element, we could store values:

```python
stack.append(heights[i])
```

But here we need to calculate the rectangle's:

```text
WIDTH
```

Width depends on positions:

```text
width = right_index - left_index - 1
```

Therefore, the Stack stores:

```python
stack.append(i)
```

Then, whenever we need the value for comparison:

```python
heights[stack[-1]]
```

So remember:

```text
stack[-1]
    ↓
Index


heights[stack[-1]]
    ↓
Value at that index
```

For example:

```text
heights = [2, 1, 5, 6, 2, 3]
                    ↑
                  index 4
```

If:

```text
stack[-1] = 4
```

then:

```text
heights[stack[-1]]
```

means:

```text
heights[4] = 2
```

### Revision Rule

```text
Need only smaller VALUE?
→ Store values

Need position / distance / width?
→ Store indices
```

---

# Why Next Smaller Uses Right → Left

We need the next smaller element on the:

```text
RIGHT
```

So we process:

```text
Right → Left
```

```python
for i in range(len(heights) - 1, -1, -1):
```

Because we use:

```python
nxt.append(...)
```

the answers are also added from right to left.

Therefore:

```python
nxt.reverse()
```

is required.

---

# Why Previous Smaller Uses Left → Right

Previous smaller exists on the:

```text
LEFT
```

So we process:

```text
Left → Right
```

```python
for i in range(len(heights)):
```

Since this is already the original array order:

```text
No reverse is required.
```

---

# Why Do We Use `>=`?

```python
while len(stack) > 0 and heights[stack[-1]] >= curr:
    stack.pop()
```

We need a:

```text
STRICTLY SMALLER
```

bar as our boundary.

So equal-height bars must also be removed.

Remember:

```text
Need strictly smaller
        ↓
Pop >= current
```

This is an easy condition to forget.

---

# Why Replace Next `-1` With `n`?

Suppose:

```text
heights = [2, 3, 4]
```

For `2`, there is no smaller element on its right.

So initially:

```text
next smaller = -1
```

But `-1` cannot be used as the right boundary in the width formula.

The bar can actually expand until the end of the histogram.

So we imagine a virtual boundary:

```text
Index:

0   1   2   3
            ↑
       Virtual boundary
```

For an array of length `3`:

```text
n = 3
```

Therefore:

```python
if nxt[i] == -1:
    nxt[i] = len(heights)
```

Remember the boundaries:

```text
No smaller on LEFT
→ -1

No smaller on RIGHT
→ n
```

This makes the width formula work automatically.

---

# The Most Important Formula

For every bar:

```python
width = nxt[i] - prev[i] - 1
```

Why `-1`?

Suppose:

```text
Previous Smaller Index = 1

Current Index = 3

Next Smaller Index = 5
```

The smaller elements at indices `1` and `5` cannot be included.

The valid rectangle is only between them:

```text
Index:

1 | 2  3  4 | 5
↑             ↑
smaller     smaller
```

Width:

```text
5 - 1 - 1
= 3
```

So:

```text
width = right_boundary - left_boundary - 1
```

Then:

```python
area = heights[i] * width
```

---

# How to Think About Each Bar

For every bar `i`, ask:

```text
How far can this height expand left and right
before finding something smaller?
```

That gives:

```text
Previous Smaller
        ↓
   [ Rectangle ]
        ↑
Next Smaller
```

Then:

```text
Height = heights[i]

Width = nxt[i] - prev[i] - 1

Area = Height × Width
```

We calculate this for every bar and keep the maximum.

---

# Things You May Forget

### 1. Store indices, not values

Wrong for this problem:

```python
stack.append(heights[i])
```

Correct:

```python
stack.append(i)
```

Because we need:

```text
distance → width → indices
```

---

### 2. Compare values through indices

Since the Stack contains indices:

```python
heights[stack[-1]]
```

not:

```python
stack[-1]
```

The first gives the bar height.

The second is only the index.

---

### 3. Reset the Stack

After Next Smaller:

```python
stack = []
```

before calculating Previous Smaller.

Do not reuse a Stack containing old indices.

---

### 4. Reverse only `nxt`

```python
nxt.reverse()
```

because Next Smaller was generated:

```text
Right → Left
```

Previous Smaller is generated:

```text
Left → Right
```

so `prev` does not need reversing.

---

### 5. Replace right-side `-1` with `n`

Remember:

```text
Previous Smaller not found → -1

Next Smaller not found     → n
```

---

### 6. Width formula

Do not forget:

```python
width = nxt[i] - prev[i] - 1
```

The final `-1` removes the two boundary gap calculation correctly.

---

### 7. Use `>=`

```python
while stack and heights[stack[-1]] >= curr:
```

For strictly smaller boundaries:

```text
Pop greater AND equal elements.
```

---

# Complexity

Each element is pushed once and popped at most once in each monotonic-stack pass.

```text
Next Smaller     → O(n)

Previous Smaller → O(n)

Area Calculation → O(n)
```

Overall:

```text
Time Complexity: O(n)

Space Complexity: O(n)
```

---

# Revision Template

```text
For every histogram bar:

1. Find Previous Smaller Index

2. Find Next Smaller Index

3. If Next Smaller doesn't exist:
      next = n

4. Calculate:
      width = next - prev - 1

5. Calculate:
      area = height × width

6. Keep maximum area
```

## Pattern Name

```text
Monotonic Stack + Previous/Next Smaller Index
```

The one line to remember for this problem is:

```text
Smaller elements create the boundaries,
indices give the width,
and each bar becomes the possible rectangle height.
```
