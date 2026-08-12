# 239. Sliding Window Maximum

## Problem

Given an array `nums` and a window size `k`, find the **maximum element in every window** of size `k`.

Example:

```text
nums = [1,3,-1,-3,5,3,6,7]
k = 3
```

Windows:

```text
[1, 3, -1] → 3
[3, -1, -3] → 3
[-1, -3, 5] → 5
[-3, 5, 3] → 5
[5, 3, 6] → 6
[3, 6, 7] → 7
```

Output:

```text
[3, 3, 5, 5, 6, 7]
```

---

# Brute Force

## Idea

For every window:

1. Look at all `k` elements.
2. Find the maximum.
3. Move the window one position forward.

```python
class Solution:
    def maxSlidingWindow(self, nums, k):
        ans = []

        for i in range(len(nums) - k + 1):
            window_max = nums[i]

            for j in range(i, i + k):
                window_max = max(window_max, nums[j])

            ans.append(window_max)

        return ans
```

### Complexity

```text
Time  → O(n × k)
Space → O(1) excluding answer
```

### Why is it slow?

Adjacent windows overlap heavily, but brute force checks the same elements again and again.

---

# Pattern

```text
Sliding Window + Monotonic Decreasing Deque
```

---

# Main Idea

We need the **maximum** of every window.

Instead of storing every element, maintain only the elements that can potentially become the maximum.

The deque stores **indices** in decreasing order of their values.

Example:

```text
nums = [1, 3, -1]
```

Deque:

```text
index:  1  2
value:  3 -1
```

Values are decreasing:

```text
3 > -1
```

Therefore:

```python
nums[q[0]]
```

is always the maximum of the current window.

---

# Why Are We Storing Indices?

This is extremely important for sliding window problems.

We could store values:

```python
q.append(num)
```

but then we would not know whether an element has **left the current window**.

For example:

```text
nums = [1, 3, -1, -3]
k = 3
```

When the window moves, we need to know whether the old maximum is still inside it.

Therefore we store:

```python
q.append(i)
```

Then:

```python
nums[q[0]]
```

gives us the value.

So remember:

```text
Deque stores → INDEX
Array gives  → VALUE
```

### Why indices are useful

Indices allow us to do:

```python
q[0] <= i - k
```

and determine whether the element has gone outside the current window.

---

# Why Remove Smaller Elements?

Suppose the deque contains:

```text
5, 3, 2
```

and the current number is:

```text
6
```

The `6` is larger than all of them.

Once `6` enters the window:

```text
5
3
2
```

can never become the maximum while `6` is present.

So we remove them:

```python
while q and nums[q[-1]] <= num:
    q.pop()
```

After that:

```text
Deque → 6
```

This is the key idea of the **Monotonic Decreasing Deque**.

---

# Why `while`, Not `if`?

Suppose:

```text
Deque values:

7 5 3
```

Current value:

```text
8
```

We need to remove:

```text
3
5
7
```

All three are smaller than `8`.

Therefore:

```python
while q and nums[q[-1]] <= num:
    q.pop()
```

not:

```python
if q and nums[q[-1]] <= num:
    q.pop()
```

`while` removes **all useless smaller elements**.

---

# Why Do We Remove From the Rear?

The deque is maintained in decreasing order of values.

Example:

```text
Front → 9 7 4 2 ← Rear
```

If a new value `8` arrives:

```text
2 < 8 → remove
4 < 8 → remove
7 < 8 → remove
```

We check from the **rear** because smaller candidates are at the rear.

After processing:

```text
9 8
```

The front always remains the largest candidate.

---

# Removing Expired Elements

The current window ending at index `i` is:

```text
[i-k+1, i]
```

Any index smaller than:

```text
i-k+1
```

is outside the window.

Equivalent condition:

```python
index <= i-k
```

So an expired index can be removed using:

```python
if q[0] <= i - k:
    q.popleft()
```

Your code uses:

```python
if q[0] == i - k:
    q.popleft()
```

This also works because expired indices would already have been removed in previous iterations, so the front can only become exactly `i-k` when it needs to leave.

For revision, remember the general condition:

```text
Expired index < window_start

window_start = i-k+1
```

or:

```text
index <= i-k
```

---

# Why Remove Expired Element Before Answer?

The deque's front should represent an element **inside the current window**.

If the maximum from the previous window has now left the window, we must remove it before using:

```python
nums[q[0]]
```

as the answer.

So the order is:

```text
1. Remove useless smaller elements
2. Add current index
3. Remove expired index
4. If window is complete → answer = nums[q[0]]
```

This ensures the front always belongs to the current window.

---

# Why `i >= k - 1`?

The first complete window appears when the right boundary reaches:

```text
k - 1
```

Example:

```text
k = 3
```

First window:

```text
indices: 0 1 2
```

So the first answer can be generated when:

```text
i = 2
```

which is:

```python
i >= k - 1
```

Before that, we don't have `k` elements yet.

---

# Optimal Solution

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []

        for i, num in enumerate(nums):

            # Remove smaller/equal elements.
            # They can never become maximum while `num` is present.
            while q and nums[q[-1]] <= num:
                q.pop()

            # Store index, not value
            q.append(i)

            # Remove index that is outside current window
            if q[0] == i - k:
                q.popleft()

            # First complete window
            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans
```

---

# Dry Run

```text
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
```

### `i = 0`, `num = 1`

```text
Deque = [0]
Values = [1]
```

Window not complete.

---

### `i = 1`, `num = 3`

`1 <= 3`, so remove index `0`.

```text
Deque = [1]
Values = [3]
```

---

### `i = 2`, `num = -1`

`3 > -1`, so keep `3`.

```text
Deque = [1, 2]
Values = [3, -1]
```

Window is complete:

```text
[1, 3, -1]
```

Answer:

```text
3
```

---

### `i = 3`, `num = -3`

```text
Deque = [1, 2, 3]
Values = [3, -1, -3]
```

Index `1` is still inside the window:

```text
Current window = [3, -1, -3]
```

Answer:

```text
3
```

---

### `i = 4`, `num = 5`

Current deque values:

```text
3, -1, -3
```

All are smaller than `5`.

Remove them:

```text
Deque = []
```

Add index `4`:

```text
Deque = [4]
```

Current window:

```text
[-1, -3, 5]
```

Answer:

```text
5
```

---

# Important Visualization

The deque does **not** contain every element of the window.

It contains only **useful candidates for maximum**.

Example:

```text
Window:

[-1, -3, 5]
```

We only keep:

```text
5
```

because:

```text
-1 < 5
-3 < 5
```

Neither `-1` nor `-3` can become the maximum while `5` is inside the window.

This is why the solution is O(n).

---

# Common Mistakes

### 1. Storing Values Instead of Indices

❌

```python
q.append(num)
```

✅

```python
q.append(i)
```

We need indices to detect expired elements.

---

### 2. Comparing Indices Instead of Values

Since the deque stores indices:

❌

```python
q[-1] <= num
```

This compares:

```text
index <= value
```

Correct:

```python
nums[q[-1]] <= num
```

This compares:

```text
value <= value
```

---

### 3. Using `if` Instead of `while`

❌

```python
if q and nums[q[-1]] <= num:
    q.pop()
```

Multiple smaller elements may need to be removed.

✅

```python
while q and nums[q[-1]] <= num:
    q.pop()
```

---

### 4. Removing Expired Elements From the Rear

Expired elements are checked from the **front** because the oldest index is at the front.

Correct:

```python
q.popleft()
```

---

### 5. Forgetting Window Completion

Don't add an answer until:

```python
i >= k - 1
```

---

### 6. Confusing `i-k` With Window Start

Current window:

```text
[i-k+1, i]
```

Expired:

```text
index <= i-k
```

Example:

```text
i = 4
k = 3

window = [2, 3, 4]

expired <= 1
```

---

# Why Is the Time Complexity O(n)?

At first, the `while` loop may look like it makes the solution O(n²).

It doesn't.

Every index is:

```text
Added to deque → at most once
Removed from deque → at most once
```

So total deque operations are at most:

```text
O(n) + O(n)
```

Therefore:

```text
Time = O(n)
```

This is called **amortized O(1)** work per element.

---

# Complexity Comparison

| Approach        |     Time | Space |
| --------------- | -------: | ----: |
| Brute Force     | O(n × k) |  O(1) |
| Monotonic Deque |     O(n) |  O(k) |

The deque contains at most `k` useful indices because indices outside the current window are removed.

---

# Pattern Recognition

When you see:

```text
Sliding Window
+
Maximum
```

think:

```text
Monotonic Decreasing Deque
```

When you see:

```text
Sliding Window
+
Minimum
```

think:

```text
Monotonic Increasing Deque
```

---

# Important Connection With First Negative

For **First Negative in Every Window**:

```text
Store indices of negative elements.
Keep them in normal increasing index order.
Front = first negative.
```

For **Sliding Window Maximum**:

```text
Store indices of useful maximum candidates.
Keep values in decreasing order.
Front = maximum.
```

So both use:

```text
Sliding Window + Deque + Indices
```

but maintain the deque differently.

---

# Revision Cheat Sheet

```text
Problem:
Maximum in Every Window of Size K

Pattern:
Sliding Window + Monotonic Decreasing Deque

Store:
INDEX, not VALUE

Why?
To know when an element leaves the window.

For every i:

1. Remove smaller/equal values from rear
       while nums[q[-1]] <= nums[i]

2. Add current index
       q.append(i)

3. Remove expired front index
       q[0] <= i-k

4. If window is complete
       i >= k-1

5. Maximum
       nums[q[0]]

Why q[0]?
Deque values are maintained in decreasing order,
so the front is the largest.

Window:
[i-k+1, i]

Expired:
index <= i-k

Time:
O(n)

Space:
O(k)

Important:
✔ Store indices
✔ Compare nums[index]
✔ Use while
✔ Remove expired elements
✔ Answer only after window is complete
```

## One-Line Pattern

```text
Sliding Window → maintain useful indices in decreasing value order → remove expired → front gives maximum.
```
