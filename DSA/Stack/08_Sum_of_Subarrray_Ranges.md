# Sum of Subarray Ranges

## Problem

For every contiguous subarray, calculate:

```text
Range = Maximum Element - Minimum Element
```

Then return the sum of the ranges of all possible subarrays.

Example:

```text
nums = [1, 2, 3]
```

All subarrays:

```text
[1]       → 1 - 1 = 0
[2]       → 2 - 2 = 0
[3]       → 3 - 3 = 0

[1, 2]    → 2 - 1 = 1
[2, 3]    → 3 - 2 = 1

[1, 2, 3] → 3 - 1 = 2
```

Total:

```text
0 + 0 + 0 + 1 + 1 + 2 = 4
```

---

# Main Idea

For every subarray:

```text
Range = Maximum - Minimum
```

Therefore:

```text
Sum of All Ranges

=

Sum of All Subarray Maximums

-

Sum of All Subarray Minimums
```

So instead of generating every subarray, we calculate two things:

```text
1. How much does every element contribute as a MINIMUM?

2. How much does every element contribute as a MAXIMUM?
```

Then:

```python
answer = MaxSum - MinSum
```

---

# Contribution Technique

For every element `nums[i]`, we calculate how many subarrays consider it their minimum.

```python
left = i - prev[i]
right = nxt[i] - i

count = left * right
```

Contribution as minimum:

```python
left * right * nums[i]
```

Similarly, for maximum:

```python
left = i - prevG[i]
right = nxtG[i] - i
```

Contribution as maximum:

```python
left * right * nums[i]
```

Finally:

```text
Answer = Maximum Contributions - Minimum Contributions
```

---

# Why Do We Need Four Boundaries?

For minimum contribution, we need:

```text
Next Smaller Boundary
Previous Smaller Boundary
```

For maximum contribution, we need:

```text
Next Greater Boundary
Previous Greater Boundary
```

So for every index `i`:

```text
MINIMUM CONTRIBUTION

prev[i] ← nums[i] → nxt[i]


MAXIMUM CONTRIBUTION

prevG[i] ← nums[i] → nxtG[i]
```

These boundaries tell us how far `nums[i]` can expand while remaining the chosen minimum or maximum.

---

# Final Code with Comments

```python
class Solution:

    # ---------------------------------------------------------
    # NEXT SMALLER OR EQUAL INDEX
    # ---------------------------------------------------------
    def nextSmaller(self, nums, stack, ans):

        # Next boundary is on the RIGHT,
        # so traverse from right to left
        for i in range(len(nums) - 1, -1, -1):

            curr = nums[i]

            # Stack stores indices.
            #
            # Pop only strictly greater values.
            # Equal values are allowed to remain.
            while stack and nums[stack[-1]] > curr:
                stack.pop()

            # No valid boundary exists on the right
            if len(stack) == 0:
                ans.append(len(nums))
            else:
                ans.append(stack[-1])

            # Store index because we need distances later
            stack.append(i)

        # Answers were generated right → left
        ans.reverse()

        return ans


    # ---------------------------------------------------------
    # PREVIOUS STRICTLY SMALLER INDEX
    # ---------------------------------------------------------
    def prevSmaller(self, nums, stack, ans):

        # Previous boundary is on the LEFT,
        # so traverse from left to right
        for i in range(len(nums)):

            curr = nums[i]

            # Pop greater and equal values.
            # Remaining top will be strictly smaller.
            while stack and nums[stack[-1]] >= curr:
                stack.pop()

            # No smaller element exists on the left
            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[-1])

            stack.append(i)

        return ans


    # ---------------------------------------------------------
    # NEXT GREATER OR EQUAL INDEX
    # ---------------------------------------------------------
    def nextGreater(self, nums, stack, ans):

        # Next boundary is on the RIGHT,
        # so traverse from right to left
        for i in range(len(nums) - 1, -1, -1):

            curr = nums[i]

            # Pop only strictly smaller values.
            # Equal values are allowed to remain.
            while stack and nums[stack[-1]] < curr:
                stack.pop()

            # No valid boundary exists on the right
            if len(stack) == 0:
                ans.append(len(nums))
            else:
                ans.append(stack[-1])

            stack.append(i)

        # Generated right → left
        ans.reverse()

        return ans


    # ---------------------------------------------------------
    # PREVIOUS STRICTLY GREATER INDEX
    # ---------------------------------------------------------
    def prevGreater(self, nums, stack, ans):

        # Previous boundary is on the LEFT,
        # so traverse from left to right
        for i in range(len(nums)):

            curr = nums[i]

            # Pop smaller and equal values.
            # Remaining top will be strictly greater.
            while stack and nums[stack[-1]] <= curr:
                stack.pop()

            # No greater element exists on the left
            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[-1])

            stack.append(i)

        return ans


    def subArrayRanges(self, nums: List[int]) -> int:

        # Boundaries for minimum contribution
        nxt = self.nextSmaller(nums, [], [])
        prev = self.prevSmaller(nums, [], [])

        # Boundaries for maximum contribution
        nxtG = self.nextGreater(nums, [], [])
        prevG = self.prevGreater(nums, [], [])


        MinSum = 0
        MaxSum = 0


        for i in range(len(nums)):

            # -----------------------------------------
            # Contribution of nums[i] as MINIMUM
            # -----------------------------------------

            # Possible starting positions
            left = i - prev[i]

            # Possible ending positions
            right = nxt[i] - i

            # Number of subarrays where nums[i]
            # is the chosen minimum = left * right
            MinSum += left * right * nums[i]


            # -----------------------------------------
            # Contribution of nums[i] as MAXIMUM
            # -----------------------------------------

            # Possible starting positions
            left = i - prevG[i]

            # Possible ending positions
            right = nxtG[i] - i

            # Number of subarrays where nums[i]
            # is the chosen maximum = left * right
            MaxSum += left * right * nums[i]


        # Range = Maximum - Minimum
        return MaxSum - MinSum
```

---

# Why Store Indices?

The Stack stores:

```text
Indices
```

not values.

Correct:

```python
stack.append(i)
```

because later we calculate distances:

```python
left = i - prev[i]
right = nxt[i] - i
```

If the Stack stored values, we could not calculate these distances.

Since the Stack contains indices:

```text
stack[-1]
    ↓
Index
```

To access the value:

```text
nums[stack[-1]]
```

Remember:

```text
Need distance / width / number of choices
        ↓
Store indices
```

---

# Understanding the Four Comparisons

This is the most important revision point.

Your code uses:

```text
NEXT SMALLER
Pop >

PREVIOUS SMALLER
Pop >=


NEXT GREATER
Pop <

PREVIOUS GREATER
Pop <=
```

Why are the comparisons different?

Because of duplicate values.

We must avoid counting the same subarray more than once when equal elements exist.

---

# Minimum Side

## Next Smaller

```python
while stack and nums[stack[-1]] > curr:
    stack.pop()
```

We pop only elements that are:

```text
Greater than current
```

Equal elements remain.

So the boundary can be:

```text
Smaller or Equal
```

---

## Previous Smaller

```python
while stack and nums[stack[-1]] >= curr:
    stack.pop()
```

We remove:

```text
Greater
+
Equal
```

So the remaining element must be:

```text
Strictly Smaller
```

Therefore, for minimum contribution:

```text
Previous → Strictly Smaller

Next     → Smaller or Equal
```

---

# Maximum Side

The exact opposite logic is used.

## Next Greater

```python
while stack and nums[stack[-1]] < curr:
    stack.pop()
```

We remove only smaller elements.

Equal elements remain.

Therefore:

```text
Next → Greater or Equal
```

---

## Previous Greater

```python
while stack and nums[stack[-1]] <= curr:
    stack.pop()
```

We remove:

```text
Smaller
+
Equal
```

Therefore, the remaining element is:

```text
Strictly Greater
```

So for maximum contribution:

```text
Previous → Strictly Greater

Next     → Greater or Equal
```

---

# Comparison Table to Remember

| Boundary         | Pop Condition | Boundary Found   |
| ---------------- | ------------- | ---------------- |
| Next Smaller     | `>`           | Smaller or Equal |
| Previous Smaller | `>=`          | Strictly Smaller |
| Next Greater     | `<`           | Greater or Equal |
| Previous Greater | `<=`          | Strictly Greater |

This table is the most important thing to revise if you forget the duplicate handling.

---

# Why Different Comparisons for Equal Elements?

Consider:

```text
nums = [2, 2]
```

For the subarray:

```text
[2, 2]
```

both elements have the same minimum and maximum.

But while using the contribution technique, we must assign this subarray to only one of them.

Otherwise:

```text
First 2 claims [2, 2]
+
Second 2 claims [2, 2]
        ↓
Double Counting
```

Using one strict boundary and one non-strict boundary creates a consistent ownership rule.

For minimum:

```text
Previous → Strict

Next → Non-Strict
```

For maximum:

```text
Previous → Strict

Next → Non-Strict
```

The exact orientation can also be reversed, but both sides should not treat equality the same way.

Remember:

```text
Duplicates
    ↓
One side strict
+
One side non-strict
```

---

# Why Missing Left Boundary Is `-1`

Suppose no valid previous boundary exists.

We use:

```text
-1
```

This represents a virtual position before the array:

```text
-1 | 0   1   2   3
 ↑
Virtual Boundary
```

Then:

```python
left = i - (-1)
```

correctly counts all possible starting positions.

---

# Why Missing Right Boundary Is `n`

If no valid next boundary exists:

```python
n = len(nums)
```

is used.

It represents a virtual position after the array:

```text
0   1   2   3 | 4
                ↑
          Virtual Boundary
```

Then:

```python
right = n - i
```

correctly counts all possible ending positions.

Remember:

```text
Missing LEFT boundary  → -1

Missing RIGHT boundary → n
```

---

# Why `left × right`?

Suppose for index `i`:

```text
left = 3

right = 2
```

This means we have:

```text
3 possible starting positions
```

and:

```text
2 possible ending positions
```

Every start can be combined with every end.

Therefore:

```text
Number of subarrays
=
3 × 2
=
6
```

So:

```python
count = left * right
```

Then:

```python
contribution = count * nums[i]
```

---

# Minimum Contribution

For every element:

```python
left = i - prev[i]
right = nxt[i] - i

MinSum += left * right * nums[i]
```

This calculates:

```text
How many subarrays choose nums[i] as minimum
×
nums[i]
```

---

# Maximum Contribution

Similarly:

```python
left = i - prevG[i]
right = nxtG[i] - i

MaxSum += left * right * nums[i]
```

This calculates:

```text
How many subarrays choose nums[i] as maximum
×
nums[i]
```

---

# Final Formula

The problem asks for:

```text
Maximum - Minimum
```

for every subarray.

Therefore:

```python
return MaxSum - MinSum
```

Conceptually:

```text
Σ(maximum - minimum)

=

Σ(maximum) - Σ(minimum)

=

MaxSum - MinSum
```

This transformation is the main idea of the problem.

---

# Things You May Forget

## 1. There Are Four Boundaries

```text
For MINIMUM:

Previous Smaller
Next Smaller


For MAXIMUM:

Previous Greater
Next Greater
```

---

## 2. Store Indices

```python
stack.append(i)
```

because contribution calculations need distances.

Compare values using:

```python
nums[stack[-1]]
```

---

## 3. Direction

```text
NEXT boundary
    ↓
Right → Left


PREVIOUS boundary
    ↓
Left → Right
```

When using `append()` while traversing right to left:

```python
ans.reverse()
```

is required.

---

## 4. Missing Boundaries

```text
Previous missing → -1

Next missing     → n
```

These are virtual boundaries.

---

## 5. Duplicate Handling

For your exact implementation, remember:

```text
SMALLER

Next → pop >
Prev → pop >=


GREATER

Next → pop <
Prev → pop <=
```

The shortcut is:

```text
Next keeps equals.

Previous removes equals.
```

---

## 6. Do Not Add Minimum and Maximum

Wrong:

```python
MaxSum + MinSum
```

Correct:

```python
MaxSum - MinSum
```

because:

```text
Range = Maximum - Minimum
```

---

# Complexity

Each monotonic-stack operation takes:

```text
O(n)
```

We perform four passes:

```text
Next Smaller     → O(n)

Previous Smaller → O(n)

Next Greater     → O(n)

Previous Greater → O(n)
```

Then one contribution pass:

```text
O(n)
```

Total:

```text
O(5n) = O(n)
```

Space:

```text
O(n)
```

---

# Revision Summary

```text
Sum of Subarray Ranges
        ↓

Sum of Maximums - Sum of Minimums
        ↓

For Minimum:
    Previous Smaller
    Next Smaller

For Maximum:
    Previous Greater
    Next Greater
        ↓

For every element:
    left = i - previous
    right = next - i
        ↓

Number of subarrays:
    left × right
        ↓

Contribution:
    left × right × nums[i]
```

## Comparison Cheat Sheet

```text
MINIMUM CONTRIBUTION

Previous Smaller:
    pop >=

Next Smaller:
    pop >


MAXIMUM CONTRIBUTION

Previous Greater:
    pop <=

Next Greater:
    pop <
```

## Pattern Name

```text
Monotonic Stack + Contribution Technique
```

The one line to remember is:

```text
Sum of Ranges
=
Contribution as Maximum
-
Contribution as Minimum
```
