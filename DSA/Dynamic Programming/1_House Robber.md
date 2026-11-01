# House Robber – Recursion, Top-Down DP, Bottom-Up DP & Space Optimization

**Problem:** LeetCode 198 – House Robber  
**Pattern:** Dynamic Programming – 1D DP / Include-Exclude  
**Language:** Python

## 1. Problem Statement

You are given an integer array `nums` where `nums[i]` represents the amount of money present in the `i-th` house.

A robber wants to rob houses to get the maximum amount of money.

**Condition:** Adjacent houses cannot be robbed because the security system will alert the police if two adjacent houses are robbed.

Return the maximum amount of money that can be robbed without robbing two adjacent houses.

### Example

```python
nums = [2, 7, 9, 3, 1]
```

Output:

```text
12
```

Explanation:

Rob house at index `0`, index `2`, and index `4`.

```text
2 + 9 + 1 = 12
```

We cannot rob adjacent houses.

---

# 2. Core Intuition – Include or Exclude

At every index, we have two choices:

1. **Include:** Rob the current house.
2. **Exclude:** Skip the current house.

### Choice 1: Include Current House

If we rob the current house, we cannot rob the next house.

Therefore, we move two indexes ahead.

```python
includeAns = nums[i] + solve(nums, i + 2)
```

### Choice 2: Exclude Current House

If we skip the current house, we can consider the next house.

Therefore, we move one index ahead.

```python
excludeAns = solve(nums, i + 1)
```

### Final Answer

We choose whichever option gives us more money.

```python
finalAns = max(includeAns, excludeAns)
```

The recurrence relation is:

\[
solve(i) = \max(nums[i] + solve(i+2), solve(i+1))
\]

Base case:

\[
solve(i) = 0 \quad \text{if } i \geq n
\]

---

# 3. Approach 1 – Normal Recursion

First, solve the problem using recursion.

### Python Code

```python
class Solution:
    def solve(self, nums, i):

        if i >= len(nums):
            return 0

        includeAns = nums[i] + self.solve(nums, i + 2)

        excludeAns = 0 + self.solve(nums, i + 1)

        finalAns = max(includeAns, excludeAns)

        return finalAns

    def rob(self, nums: list[int]) -> int:
        return self.solve(nums, 0)
```

### Code Explanation

**1. Base Case**

```python
if i >= len(nums):
    return 0
```

Agar index array ki length ke equal ya greater ho gaya, toh koi house available nahi hai.

Isliye return `0`.

**2. Include Current House**

```python
includeAns = nums[i] + self.solve(nums, i + 2)
```

Current house ka money add karenge aur next adjacent house skip karke `i + 2` par move karenge.

**3. Exclude Current House**

```python
excludeAns = 0 + self.solve(nums, i + 1)
```

Current house ko rob nahi karenge aur next house consider karenge.

**4. Select Maximum**

```python
finalAns = max(includeAns, excludeAns)
```

Dono choices mein se maximum money return karenge.

### Dry Run

Input:

```python
nums = [2, 7, 9, 3, 1]
```

At index `0`:

```text
Include = 2 + solve(2)
Exclude = 0 + solve(1)
```

At index `2`:

```text
Include = 9 + solve(4)
Exclude = 0 + solve(3)
```

At index `4`:

```text
Include = 1 + solve(6) = 1
Exclude = 0 + solve(5) = 0
```

Index `5` and `6` base case mein chale jayenge aur `0` return karenge.

Final maximum:

```text
2 + 9 + 1 = 12
```

### Recursion Tree

```text
                       solve(0)
                      /        \
                 Include       Exclude
                 2+solve(2)    solve(1)
                  /   \          /   \
             solve(4) solve(3) solve(3) solve(2)
```

Notice karo `solve(2)` aur `solve(3)` jaise same states multiple times calculate ho rahi hain.

Yahi overlapping subproblems hain.

### Complexity

- **Time Complexity:** `O(2^N)` – common upper-bound estimate because each state can generate two recursive calls.
- **Auxiliary Space:** `O(N)` – maximum recursion stack depth.

---

# 4. Approach 2 – Top-Down DP (Memoization)

Normal recursion mein same index multiple times calculate ho raha tha.

Hum har index ka answer store kar lenge.

Agar same index dobara call hota hai, toh calculation repeat karne ki jagah stored answer return kar denge.

This is called **Memoization or Top-Down DP**.

### Python Code

```python
class Solution:
    def solve(self, nums, i):

        n = len(nums)

        dp = [-1] * (n + 2)

        def helper(i):

            if i >= n:
                return 0

            if dp[i] != -1:
                return dp[i]

            includeAns = nums[i] + helper(i + 2)

            excludeAns = 0 + helper(i + 1)

            dp[i] = max(includeAns, excludeAns)

            return dp[i]

        return helper(i)

    def rob(self, nums: list[int]) -> int:
        return self.solve(nums, 0)
```

### Code Explanation

**1. Create DP Array**

```python
dp = [-1] * (n + 2)
```

We create a DP array to store the maximum money that can be robbed starting from each index.

Initially, every position contains `-1`, which means that state has not been calculated yet.

**Why `n + 2`?**

Because our recursion can access:

```python
helper(i + 1)
helper(i + 2)
```

For the last index, `i + 2` can reach `n + 1`.

Creating an array of size `n + 2` makes both `dp[n]` and `dp[n+1]` valid indexes.

**2. Base Case**

```python
if i >= n:
    return 0
```

If we have crossed the array boundary, no more money can be collected.

**3. Check Already Calculated State**

```python
if dp[i] != -1:
    return dp[i]
```

Agar current index ka answer already calculated hai, toh directly return kar do.

**4. Calculate Include and Exclude**

```python
includeAns = nums[i] + helper(i + 2)

excludeAns = 0 + helper(i + 1)
```

Same include-exclude logic as normal recursion.

**5. Store the Answer**

```python
dp[i] = max(includeAns, excludeAns)
```

Current index ka maximum answer DP array mein store kar diya.

### Complexity

- **Time Complexity:** `O(N)` – each index is calculated only once.
- **DP Array Space:** `O(N)`.
- **Recursion Stack:** `O(N)`.
- **Total Auxiliary Space:** `O(N)`.

### Important Note

Top-Down DP mein hum `solve(0)` se start karte hain aur recursion ke through smaller subproblems solve karte hain.

---

# 5. Approach 3 – Bottom-Up DP (Tabulation)

Ab recursion ko remove karenge.

Top-Down mein hum starting index `0` se recursively aage ja rahe the.

Bottom-Up mein hum last index se start karke reverse direction mein answers calculate karenge.

### State Definition

Let:

```python
dp[i] = Maximum money that can be robbed starting from index i.
```

Our recurrence:

\[
dp[i] = \max(nums[i] + dp[i+2], dp[i+1])
\]

Base cases:

\[
dp[n] = 0
\]

\[
dp[n+1] = 0
\]

Why?

Because if we are at or beyond the array boundary, there are no more houses to rob.

### Python Code

```python
class Solution:
    def solve(self, nums, i):

        n = len(nums)

        dp = [-1] * (n + 2)

        dp[n] = 0
        dp[n + 1] = 0

        for i in range(n - 1, -1, -1):

            includeAns = nums[i] + dp[i + 2]

            excludeAns = 0 + dp[i + 1]

            dp[i] = max(includeAns, excludeAns)

        return dp[0]

    def rob(self, nums: list[int]) -> int:
        return self.solve(nums, 0)
```

### Code Explanation

**1. Create DP Array**

```python
dp = [-1] * (n + 2)
```

We need `n + 2` positions because we access `dp[i+1]` and `dp[i+2]`.

**2. Initialize Base Cases**

```python
dp[n] = 0
dp[n + 1] = 0
```

No houses are available at these positions, so the maximum money is zero.

**3. Traverse Backwards**

```python
for i in range(n - 1, -1, -1):
```

We start from the last house and move towards the first house.

Why backwards?

Because `dp[i]` depends on:

```python
dp[i + 1]
dp[i + 2]
```

These values must already be calculated before calculating `dp[i]`.

**4. Include Current House**

```python
includeAns = nums[i] + dp[i + 2]
```

Rob current house and move two positions ahead.

**5. Exclude Current House**

```python
excludeAns = 0 + dp[i + 1]
```

Skip current house and move one position ahead.

**6. Store Maximum Answer**

```python
dp[i] = max(includeAns, excludeAns)
```

**7. Return Final Answer**

```python
return dp[0]
```

`dp[0]` represents the maximum money that can be robbed starting from the first house.

### Dry Run

Input:

```python
nums = [2, 7, 9, 3, 1]
```

Here:

```python
n = 5
dp = [-1, -1, -1, -1, -1, 0, 0]
```

Initially:

```text
Index:  0   1   2   3   4   5   6
dp:    -1  -1  -1  -1  -1   0   0
```

Now iterate backwards.

**i = 4**

```python
includeAns = nums[4] + dp[6]
            = 1 + 0
            = 1

excludeAns = dp[5]
            = 0

dp[4] = max(1, 0) = 1
```

**i = 3**

```python
includeAns = nums[3] + dp[5]
            = 3 + 0
            = 3

excludeAns = dp[4]
            = 1

dp[3] = max(3, 1) = 3
```

**i = 2**

```python
includeAns = nums[2] + dp[4]
            = 9 + 1
            = 10

excludeAns = dp[3]
            = 3

dp[2] = max(10, 3) = 10
```

**i = 1**

```python
includeAns = nums[1] + dp[3]
            = 7 + 3
            = 10

excludeAns = dp[2]
            = 10

dp[1] = max(10, 10) = 10
```

**i = 0**

```python
includeAns = nums[0] + dp[2]
            = 2 + 10
            = 12

excludeAns = dp[1]
            = 10

dp[0] = max(12, 10) = 12
```

Final DP array:

```text
Index:  0   1   2   3   4   5   6
dp:    12  10  10   3   1   0   0
```

Answer:

```python
return dp[0]  # 12
```

### Complexity

- **Time Complexity:** `O(N)` – one loop over the array.
- **Space Complexity:** `O(N)` – DP array.
- No recursion stack is required.

---

# 6. Approach 4 – Space Optimization

In Bottom-Up DP, we created an entire array:

```python
dp = [0] * (n + 2)
```

But notice something important.

To calculate:

```python
dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
```

We only need two previous calculated states:

```python
dp[i + 1]
dp[i + 2]
```

We don't need the entire DP array.

So instead of storing all values, we can maintain only two variables.

### Variable Meaning

```python
next1 = dp[i + 1]
next2 = dp[i + 2]
```

These variables represent the next two states in the backward traversal.

### Python Code

```python
class Solution:
    def solve(self, nums, i):

        n = len(nums)

        next1 = 0
        next2 = 0

        for i in range(n - 1, -1, -1):

            includeAns = nums[i] + next2

            excludeAns = 0 + next1

            curr = max(includeAns, excludeAns)

            next2, next1 = next1, curr

        return next1

    def rob(self, nums: list[int]) -> int:
        return self.solve(nums, 0)
```

### Code Explanation

**1. Initialize Two Variables**

```python
next1 = 0
next2 = 0
```

These represent:

```text
next1 = dp[i + 1]
next2 = dp[i + 2]
```

Initially, both are zero because:

```python
dp[n] = 0
dp[n + 1] = 0
```

**2. Calculate Include Answer**

```python
includeAns = nums[i] + next2
```

If we rob current house, we need the answer from two positions ahead.

**3. Calculate Exclude Answer**

```python
excludeAns = 0 + next1
```

If we skip current house, we need the answer from the next position.

**4. Calculate Current Answer**

```python
curr = max(includeAns, excludeAns)
```

Store the maximum of both choices in `curr`.

**5. Update Variables**

```python
next2, next1 = next1, curr
```

This is the most important line.

We move one step backwards in the array, so the states must also shift.

Before update:

```text
next2 = dp[i + 2]
next1 = dp[i + 1]
curr  = dp[i]
```

After update:

```text
next2 = dp[i + 1]
next1 = dp[i]
```

Python evaluates the right-hand side first, so both values are updated correctly.

This is equivalent to:

```python
temp = next1
next2 = temp
next1 = curr
```

**6. Return Answer**

```python
return next1
```

After the loop finishes, `next1` contains `dp[0]`, which is our final answer.

### Dry Run

Input:

```python
nums = [2, 7, 9, 3, 1]
```

Initial:

```text
next1 = 0
next2 = 0
```

**i = 4**

```text
include = 1 + 0 = 1
exclude = 0

curr = 1
```

Update:

```text
next2 = 0
next1 = 1
```

**i = 3**

```text
include = 3 + 0 = 3
exclude = 1

curr = 3
```

Update:

```text
next2 = 1
next1 = 3
```

**i = 2**

```text
include = 9 + 1 = 10
exclude = 3

curr = 10
```

Update:

```text
next2 = 3
next1 = 10
```

**i = 1**

```text
include = 7 + 3 = 10
exclude = 10

curr = 10
```

Update:

```text
next2 = 10
next1 = 10
```

**i = 0**

```text
include = 2 + 10 = 12
exclude = 10

curr = 12
```

Update:

```text
next2 = 10
next1 = 12
```

Final answer:

```python
return next1  # 12
```

### Complexity

- **Time Complexity:** `O(N)` – one loop.
- **Space Complexity:** `O(1)` – only two variables are used.
- No recursion stack.
- No DP array.

---

# 7. Comparison of All Four Approaches

| Approach | Technique | Time Complexity | Space Complexity |
|---|---|---|---|
| Normal Recursion | Include / Exclude | `O(2^N)` upper bound | `O(N)` |
| Top-Down DP | Recursion + Memoization | `O(N)` | `O(N)` |
| Bottom-Up DP | Tabulation | `O(N)` | `O(N)` |
| Space Optimization | Two Variables | `O(N)` | `O(1)` |

### Flow

```text
Normal Recursion
       |
       | Same states repeat
       v
Top-Down DP
(Memoization)
       |
       | Remove recursion
       v
Bottom-Up DP
(Tabulation)
       |
       | Only two states required
       v
Space Optimization
```

---

# 8. Important Concepts to Remember

### 1. Why Do We Use `i + 2` in Include?

Because adjacent houses cannot be robbed.

If we rob house `i`, the next available house is `i + 2`.

### 2. Why Do We Use `i + 1` in Exclude?

Because we skip the current house and can consider the next house.

### 3. Why Does Tabulation Run Backwards?

Because the current state depends on future indexes:

```python
dp[i + 1]
dp[i + 2]
```

These must be calculated first.

### 4. Why Is `dp` Size `n + 2`?

Because we access:

```python
dp[n]
dp[n + 1]
```

Both positions are required for the base cases.

### 5. Why Do We Need Only Two Variables in Space Optimization?

Because the current state depends only on the next two states.

There is no need to store the entire DP array.

### 6. Why Does `next1` Contain the Final Answer?

The loop starts from the last index and finishes at index `0`.

After processing index `0`:

```text
next1 = dp[0]
```

Therefore, we return `next1`.

---

# 9. Common Mistakes

- Using `i + 1` after including a house, which violates the adjacent-house condition.
- Forgetting the base case in recursion.
- Using `dp[i + 2]` without allocating enough DP array space.
- Traversing forwards in tabulation without changing the recurrence.
- Updating `next1` before preserving its old value.
- Confusing `dp[i]` with the maximum amount collected up to index `i`. Here, `dp[i]` means the maximum amount obtainable starting from index `i`.
- Trying space optimization before understanding the tabulation dependencies.

---

# 10. Pattern Recognition – Include / Exclude DP

This problem follows the **Include / Exclude pattern**.

Whenever a problem gives you choices such as:
- Select an element or skip it.
- Take an item or leave it.
- Rob a house or skip it.
- Include an element in a subset or exclude it.

Think about this pattern.

General structure:

```python
def solve(index):

    if base_case:
        return 0

    include = current_value + solve(next_index_after_include)

    exclude = solve(next_index_after_exclude)

    return max(include, exclude)
```

Depending on the problem, you may use `max`, `min`, addition, or Boolean OR instead of always using `max`.

### Related Problems

- House Robber – LeetCode 198
- House Robber II – LeetCode 213
- Maximum Sum of Non-Adjacent Elements
- 0/1 Knapsack
- Subset Sum
- Partition Equal Subset Sum
- Target Sum

---

# 11. Final Revision

| Concept | Remember |
|---|---|
| Recursion | Solve smaller problems using function calls |
| Include | `nums[i] + solve(i + 2)` |
| Exclude | `solve(i + 1)` |
| Recurrence | `max(include, exclude)` |
| Top-Down | Recursion + DP array |
| Bottom-Up | Reverse iteration + DP array |
| Space Optimization | Maintain only two required states |
| Final Answer | `dp[0]` or `next1` |

**One-line takeaway:** House Robber is an Include/Exclude DP problem. First solve it using recursion, store repeated states using memoization, convert it into reverse tabulation, and finally optimize space by maintaining only the next two states.