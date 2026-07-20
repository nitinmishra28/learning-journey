# Sum of Subarray Minimums

## Problem

Given an array of integers `arr`, find the sum of the minimum value of every possible contiguous subarray.

Since the answer can be very large, return it modulo:

```text
10^9 + 7
```

---

# Example

```text
arr = [3, 1, 2, 4]
```

All contiguous subarrays are:

```text
[3]          → minimum = 3
[1]          → minimum = 1
[2]          → minimum = 2
[4]          → minimum = 4

[3, 1]       → minimum = 1
[1, 2]       → minimum = 1
[2, 4]       → minimum = 2

[3, 1, 2]    → minimum = 1
[1, 2, 4]    → minimum = 1

[3, 1, 2, 4] → minimum = 1
```

Sum:

```text
3 + 1 + 2 + 4 + 1 + 1 + 2 + 1 + 1 + 1

= 17
```

The brute-force idea works, but generating every subarray and finding its minimum is too expensive.

---

# Main Idea — Contribution Technique

Instead of asking:

```text
"What is the minimum of every subarray?"
```

we reverse the thinking:

```text
"For how many subarrays is arr[i] the minimum?"
```

For every element:

```text
arr[i]
```

we find how far it can extend toward the:

```text
LEFT ← arr[i] → RIGHT
```

while still acting as the minimum.

For this, we find:

```text
Previous Smaller Boundary
Next Smaller Boundary
```

Then:

```python
left = i - prev[i]
right = nxt[i] - i
```

The number of subarrays where `arr[i]` contributes as the minimum is:

```text
left × right
```

Therefore:

```text
Contribution of arr[i]

= arr[i] × left × right
```

And the final answer is:

```text
Sum of contribution of every element
```

---

# Why Do We Need Previous and Next Smaller Boundaries?

Suppose the current element is:

```text
arr[i]
```

We want to know the region in which this element can act as the minimum.

Conceptually:

```text
Previous Boundary        Current        Next Boundary

       ↓                    ↓                 ↓

   smaller/equal   |     arr[i]     |      smaller
                   |                |
                   ← Valid Region →
```

Once we cross these boundaries, another element takes control as the minimum.

So the boundaries tell us:

```text
How many different subarrays can include arr[i]
while keeping arr[i] as the chosen minimum?
```

---

# Why `left × right` Works

For every element:

```python
left = i - prev[i]
right = nxt[i] - i
```

`left` represents:

```text
How many valid starting positions can we choose?
```

`right` represents:

```text
How many valid ending positions can we choose?
```

Every valid start can be combined with every valid end.

Therefore:

```text
Total combinations
=
Left choices × Right choices
```

---

# Small Example of `left × right`

Consider:

```text
arr = [3, 1, 2, 4]
```

Take:

```text
arr[1] = 1
```

Suppose its boundaries are:

```text
prev[1] = -1
next[1] = 4
```

Then:

```text
left = 1 - (-1)
     = 2
```

The possible starting positions are:

```text
index 0
index 1
```

So:

```text
2 choices
```

Now:

```text
right = 4 - 1
      = 3
```

Possible ending positions are:

```text
index 1
index 2
index 3
```

So:

```text
3 choices
```

Therefore:

```text
Total subarrays
=
2 × 3
=
6
```

These are:

```text
[1]

[1, 2]

[1, 2, 4]

[3, 1]

[3, 1, 2]

[3, 1, 2, 4]
```

In all six subarrays:

```text
1
```

is the minimum.

Therefore its contribution is:

```text
1 × 2 × 3
=
6
```

This is the core idea of the entire problem.

---

# Why Do We Store Indices Instead of Values?

This problem requires distance calculations:

```python
left = i - prev[i]
right = nxt[i] - i
```

Therefore, we need:

```text
POSITIONS
```

not just values.

### Wrong

```python
stack.append(curr)
```

This stores:

```text
Value
```

### Correct

```python
stack.append(i)
```

This stores:

```text
Index
```

When we need the actual value:

```python
arr[stack[-1]]
```

Remember:

```text
stack[-1]
    ↓
Index


arr[stack[-1]]
    ↓
Value stored at that index
```

### Revision Rule

```text
Need only a value?
→ Values may be enough.

Need distance / width / number of choices?
→ Store indices.
```

---

# Next Smaller Boundary

For the next smaller element, we need information from the:

```text
RIGHT
```

Therefore, we traverse:

```text
RIGHT → LEFT
```

```python
for i in range(len(arr) - 1, -1, -1):
```

The comparison is:

```python
while stack and arr[stack[-1]] >= curr:
    stack.pop()
```

This removes:

```text
Greater elements
+
Equal elements
```

So the remaining Stack top is:

```text
Strictly Smaller
```

If no next smaller element exists:

```python
ans.append(len(arr))
```

---

# Previous Smaller Boundary

For the previous boundary, we need information from the:

```text
LEFT
```

Therefore, we traverse:

```text
LEFT → RIGHT
```

```python
for i in range(len(arr)):
```

The comparison is:

```python
while stack and arr[stack[-1]] > curr:
    stack.pop()
```

Notice:

```text
>
```

instead of:

```text
>=
```

This means equal elements are allowed to remain.

Therefore, this side effectively finds the previous:

```text
Smaller or Equal
```

boundary.

---

# Important — Handling Duplicate Values

This is one of the most important parts of this problem.

If all values are unique, using strictly smaller boundaries on both sides may appear to work.

But duplicate values create ambiguity.

Consider:

```text
arr = [2, 2]
```

The subarray:

```text
[2, 2]
```

has minimum:

```text
2
```

But which `2` should receive this subarray's contribution?

```text
First 2?

or

Second 2?
```

If both elements claim it:

```text
Double Counting
```

If neither claims it:

```text
Under Counting
```

So we need a consistent tie-breaking rule.

In this solution:

```text
Next side
→ Strictly Smaller


Previous side
→ Smaller or Equal
```

Implemented using:

```python
# Next
while stack and arr[stack[-1]] >= curr:
    stack.pop()
```

and:

```python
# Previous
while stack and arr[stack[-1]] > curr:
    stack.pop()
```

The exact side chosen for strict/non-strict can be reversed, but they must be asymmetric.

For example, this is also a valid strategy:

```text
Previous → Strictly Smaller

Next → Smaller or Equal
```

The important rule is:

```text
One side handles equality.

The other side does not.
```

This gives every duplicate-containing subarray exactly one owner.

---

# Boundary Values

When no valid boundary exists, we use virtual boundaries.

## No Previous Boundary

Use:

```text
-1
```

This represents a position:

```text
just before the array
```

---

## No Next Boundary

Use:

```text
n
```

where:

```python
n = len(arr)
```

This represents a position:

```text
just after the array
```

So remember:

```text
Virtual Left Boundary  = -1

Array indices          = 0 ... n - 1

Virtual Right Boundary = n
```

This allows:

```python
left = i - prev[i]
right = nxt[i] - i
```

to work without special cases.

---

# Mistakes I Made and What I Learned

## Mistake 1 — Storing Values Instead of Indices

Initially:

```python
stack.append(curr)
```

But later I needed:

```python
left = i - prev[i]
right = nxt[i] - i
```

These calculations require indices.

Correct:

```python
stack.append(i)
```

Then compare values using:

```python
arr[stack[-1]]
```

Remember:

```text
stack[-1]       → index

arr[stack[-1]]  → value
```

---

## Mistake 2 — Comparing Index With Value

After storing indices, this is wrong:

```python
stack[-1] >= curr
```

because it compares:

```text
index >= value
```

Correct:

```python
arr[stack[-1]] >= curr
```

because now we compare:

```text
value >= value
```

---

## Mistake 3 — Using `-1` for Missing Next Boundary

If:

```text
next[i] = -1
```

then:

```python
right = next[i] - i
```

can become negative.

Instead:

```text
Previous boundary missing → -1

Next boundary missing     → n
```

These represent virtual boundaries outside the array.

---

## Mistake 4 — Using the Same Comparison on Both Sides

Using:

```python
>=
```

on both sides can incorrectly handle duplicates.

This solution uses:

```python
# Next strictly smaller
while stack and arr[stack[-1]] >= curr:
```

and:

```python
# Previous smaller or equal
while stack and arr[stack[-1]] > curr:
```

Remember:

```text
Duplicates
    ↓
One strict side
+
One non-strict side
```

---

## Mistake 5 — Reusing Stack and Answer Arrays

After finding `nxt`, the Stack contains old indices.

So before calculating `prev`:

```python
stack = []
ans = []
```

The two calculations must start with clean temporary data.

---

## Mistake 6 — Incorrect Modulo

Wrong:

```python
mod = 10e9 + 7
```

`10e9` means:

```text
10 × 10^9
=
10^10
```

and scientific notation creates a float.

Correct:

```python
mod = 10**9 + 7
```

which gives:

```text
1,000,000,007
```

---

# Final Solution with Comments

```python
class Solution:

    def nextSmaller(self, arr, stack, ans):

        # Next boundary is on the right,
        # so traverse right → left
        for i in range(len(arr) - 1, -1, -1):

            curr = arr[i]

            # Stack stores indices.
            #
            # Pop greater and equal elements
            # so the remaining top is strictly smaller.
            while stack and arr[stack[-1]] >= curr:
                stack.pop()

            # No smaller element on the right:
            # use virtual boundary n
            if len(stack) == 0:
                ans.append(len(arr))
            else:
                ans.append(stack[-1])

            # Store index because we need distances later
            stack.append(i)

        return ans


    def prevSmaller(self, arr, stack, ans):

        # Previous boundary is on the left,
        # so traverse left → right
        for i in range(len(arr)):

            curr = arr[i]

            # Use > instead of >= so equal values
            # remain and handle duplicate ownership.
            while stack and arr[stack[-1]] > curr:
                stack.pop()

            # No previous boundary:
            # use virtual boundary -1
            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[-1])

            stack.append(i)

        return ans


    def sumSubarrayMins(self, arr: List[int]) -> int:

        stack = []
        ans = []

        # Find next smaller indices
        nxt = self.nextSmaller(arr, stack, ans)

        # Generated right → left,
        # so restore original index order
        nxt.reverse()


        # Reset temporary structures
        stack = []
        ans = []

        # Find previous smaller/equal indices
        prev = self.prevSmaller(arr, stack, ans)


        total = 0

        mod = 10**9 + 7


        for i in range(len(arr)):

            # Number of possible starting positions
            left = i - prev[i]

            # Number of possible ending positions
            right = nxt[i] - i

            # Number of subarrays where arr[i]
            # is the chosen minimum
            count = left * right

            # Add current element's contribution
            total = (
                total + (count * arr[i]) % mod
            ) % mod


        return total
```

---

# Complexity Analysis

## Time Complexity

```text
O(n)
```

Each element is:

```text
Pushed at most once

Popped at most once
```

in each monotonic-stack pass.

We perform:

```text
Next boundary     → O(n)

Previous boundary → O(n)

Contribution      → O(n)
```

Therefore:

```text
O(n) + O(n) + O(n)
=
O(n)
```

---

## Space Complexity

```text
O(n)
```

Extra space is used for:

```text
Monotonic Stack

Previous Boundaries

Next Boundaries
```

---

# Things to Remember for Revision

### 1. Store indices

```python
stack.append(i)
```

because:

```text
Distance calculations need positions.
```

### 2. Compare values

```python
arr[stack[-1]]
```

because the Stack contains indices.

### 3. Boundary defaults

```text
Left missing  → -1

Right missing → n
```

### 4. Handle duplicates asymmetrically

```text
One side → strict

Other side → non-strict
```

### 5. Direction

```text
Next boundary     → Right to Left

Previous boundary → Left to Right
```

### 6. Contribution formula

```python
left = i - prev[i]

right = nxt[i] - i

count = left * right

contribution = count * arr[i]
```

---

# Pattern Recognition

This problem follows:

```text
Monotonic Stack + Contribution Technique
```

The complete thinking is:

```text
For every arr[i]:

Find LEFT boundary
        ↓
Find RIGHT boundary
        ↓
Count valid start positions
        ↓
Count valid end positions
        ↓
Multiply both choices
        ↓
Multiply by arr[i]
        ↓
Add to total
```

The strongest mental model is:

```text
Don't generate every subarray.

Give every subarray to the element
that acts as its minimum.
```

And for each element:

```text
How many starts can I choose?
        ×
How many ends can I choose?
        =
How many subarrays do I own?
```

## Pattern Name

```text
Monotonic Stack + Contribution Technique
```
