# Fibonacci – Recursion, Top-Down DP, Bottom-Up DP & Space Optimization

**Problem:** LeetCode 509 – Fibonacci Number  
**Pattern:** Dynamic Programming – 1D DP  
**Language:** Python

---

# 1. Problem Statement

The Fibonacci sequence is a sequence in which each number is the sum of the previous two numbers.

The sequence starts with:

```text
0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
```

Mathematically:

\[
F(n) = F(n-1) + F(n-2)
\]

Base cases:

\[
F(0) = 0
\]

\[
F(1) = 1
\]

Given an integer `n`, return the `n-th` Fibonacci number.

### Example

```python
n = 5
```

Output:

```text
5
```

Explanation:

```text
F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
```

---

# 2. Core Intuition

Fibonacci follows a simple recurrence relation:

\[
fib(n) = fib(n-1) + fib(n-2)
\]

To calculate the current Fibonacci number, we need the previous two Fibonacci numbers.

For example:

```text
fib(5) = fib(4) + fib(3)
       = 3 + 2
       = 5
```

We will solve this problem using four approaches:

1. Normal Recursion.
2. Top-Down DP – Memoization.
3. Bottom-Up DP – Tabulation.
4. Space Optimization.

---

# 3. Approach 1 – Normal Recursion

First, solve the problem using recursion.

### Python Code

```python
class Solution:
    def fib(self, n: int) -> int:

        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)
```

### Code Explanation

**1. Base Case**

```python
if n <= 1:
    return n
```

If `n` is `0`, return `0`.

If `n` is `1`, return `1`.

These are the starting values of the Fibonacci sequence.

**2. Recursive Relation**

```python
return self.fib(n - 1) + self.fib(n - 2)
```

Current Fibonacci number previous two Fibonacci numbers ka sum hota hai.

### Dry Run

Input:

```python
n = 5
```

Calculation:

```text
fib(5)
    |
    |-- fib(4)
    |      |
    |      |-- fib(3)
    |      |      |
    |      |      |-- fib(2)
    |      |      |-- fib(1)
    |      |
    |      |-- fib(2)
    |
    |-- fib(3)
           |
           |-- fib(2)
           |-- fib(1)
```

Final calculation:

```text
fib(5) = fib(4) + fib(3)
       = 3 + 2
       = 5
```

### Problem with Normal Recursion

Notice karo:

- `fib(3)` multiple times calculate ho raha hai.
- `fib(2)` bhi multiple times calculate ho raha hai.

Same subproblems repeat ho rahe hain.

This is called **Overlapping Subproblems**.

### Complexity

- **Time Complexity:** `O(2^N)` – common upper-bound estimate.
- **Auxiliary Space:** `O(N)` – recursion stack.

---

# 4. Approach 2 – Top-Down DP (Memoization)

Normal recursion mein same Fibonacci values baar-baar calculate ho rahi thi.

Ab hum ek DP array create karenge aur calculated answers store karenge.

Agar same state dobara call hoti hai, toh stored answer return kar denge.

This is called **Memoization or Top-Down DP**.

### Python Code

```python
class Solution:

    def solve(self, n, dp):

        if n <= 1:
            return n

        # Step 1: Check whether answer is already calculated
        if dp[n] != -1:
            return dp[n]

        # Step 2: Calculate and store the answer
        dp[n] = self.solve(n - 1, dp) + self.solve(n - 2, dp)

        return dp[n]

    def fib(self, n: int) -> int:

        # Step 3: Create DP array
        dp = [-1] * (n + 1)

        return self.solve(n, dp)
```

### Code Explanation

**1. Create DP Array**

```python
dp = [-1] * (n + 1)
```

We create an array of size `n + 1`.

Initially:

```text
dp = [-1, -1, -1, -1, -1, -1]
```

`-1` means the answer for that state has not been calculated yet.

**2. Base Case**

```python
if n <= 1:
    return n
```

Fibonacci of `0` is `0` and Fibonacci of `1` is `1`.

**3. Check Whether Answer Exists**

```python
if dp[n] != -1:
    return dp[n]
```

Agar current Fibonacci number ka answer already calculate ho chuka hai, toh directly return kar do.

**4. Calculate and Store**

```python
dp[n] = self.solve(n - 1, dp) + self.solve(n - 2, dp)
```

Previous two Fibonacci numbers calculate karo aur unka sum DP array mein store kar do.

**5. Return Stored Answer**

```python
return dp[n]
```

### Dry Run

Input:

```python
n = 5
```

Initially:

```text
dp = [-1, -1, -1, -1, -1, -1]
```

After calculation:

```text
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 3
dp[5] = 5
```

Final DP array:

```text
[0, 1, 1, 2, 3, 5]
```

If `fib(3)` is called again, the function checks:

```python
if dp[3] != -1:
    return dp[3]
```

It directly returns `2`, without recalculating it.

### Complexity

- **Time Complexity:** `O(N)` – each state is calculated only once.
- **DP Array Space:** `O(N)`.
- **Recursion Stack:** `O(N)`.
- **Total Auxiliary Space:** `O(N)`.

### Important

Memoization is called Top-Down DP because we start from the final problem `fib(n)` and recursively solve smaller subproblems.

---

# 5. Approach 3 – Bottom-Up DP (Tabulation)

In Top-Down DP, we used recursion.

Now we will remove recursion and calculate Fibonacci values using a loop.

Instead of starting from `fib(n)`, we will start from the base cases:

```text
fib(0) = 0
fib(1) = 1
```

Then calculate the remaining Fibonacci values one by one.

### Python Code

```python
class Solution:
    def fib(self, n: int) -> int:

        if n <= 1:
            return n

        # Step 1: Create DP array
        dp = [0] * (n + 1)

        # Step 2: Initialize base cases
        dp[0] = 0
        dp[1] = 1

        # Step 3: Calculate remaining states
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
```

### Code Explanation

**1. Create DP Array**

```python
dp = [0] * (n + 1)
```

We create an array of size `n + 1` to store all Fibonacci values from index `0` to `n`.

**2. Initialize Base Cases**

```python
dp[0] = 0
dp[1] = 1
```

These are the starting values of Fibonacci.

**3. Iterate from 2 to n**

```python
for i in range(2, n + 1):
```

We start from index `2` because indexes `0` and `1` are already initialized.

**4. Calculate Current State**

```python
dp[i] = dp[i - 1] + dp[i - 2]
```

Current Fibonacci number is the sum of the previous two numbers.

**5. Return Final Answer**

```python
return dp[n]
```

### Dry Run

Input:

```python
n = 5
```

Initially:

```text
dp = [0, 1, 0, 0, 0, 0]
```

Now calculate:

**i = 2**

```python
dp[2] = dp[1] + dp[0]
      = 1 + 0
      = 1
```

**i = 3**

```python
dp[3] = dp[2] + dp[1]
      = 1 + 1
      = 2
```

**i = 4**

```python
dp[4] = dp[3] + dp[2]
      = 2 + 1
      = 3
```

**i = 5**

```python
dp[5] = dp[4] + dp[3]
      = 3 + 2
      = 5
```

Final DP array:

```text
[0, 1, 1, 2, 3, 5]
```

Answer:

```python
return dp[5]  # 5
```

### Complexity

- **Time Complexity:** `O(N)` – one loop from `2` to `n`.
- **Space Complexity:** `O(N)` – DP array.
- No recursion stack is required.

### Important

Tabulation is called Bottom-Up DP because we solve smaller states first and use them to calculate larger states.

---

# 6. Approach 4 – Space Optimization

In Bottom-Up DP, we created a complete DP array:

```python
dp = [0] * (n + 1)
```

But think about the recurrence:

```python
dp[i] = dp[i - 1] + dp[i - 2]
```

To calculate the current Fibonacci number, we only need:

- Previous Fibonacci number: `dp[i - 1]`.
- Second previous Fibonacci number: `dp[i - 2]`.

We don't need the entire DP array.

Therefore, we can replace the DP array with two variables.

### Python Code

```python
class Solution:
    def fib(self, n: int) -> int:

        if n <= 1:
            return n

        prev = 0
        curr = 1

        for i in range(2, n + 1):

            ans = prev + curr

            prev, curr = curr, ans

        return curr
```

### Code Explanation

**1. Initialize Two Variables**

```python
prev = 0
curr = 1
```

These represent:

```text
prev = Previous Fibonacci number
curr = Current Fibonacci number
```

Initially:

```text
prev = fib(0) = 0
curr = fib(1) = 1
```

**2. Calculate Next Fibonacci Number**

```python
ans = prev + curr
```

Add the previous two Fibonacci numbers.

**3. Update Variables**

```python
prev, curr = curr, ans
```

This is the most important line.

We move forward in the Fibonacci sequence.

Before update:

```text
prev = fib(i - 2)
curr = fib(i - 1)
ans  = fib(i)
```

After update:

```text
prev = fib(i - 1)
curr = fib(i)
```

Python evaluates the right-hand side first, so both values are updated correctly.

**4. Return Final Answer**

```python
return curr
```

After the loop finishes, `curr` contains the `n-th` Fibonacci number.

### Dry Run

Input:

```python
n = 5
```

Initial values:

```text
prev = 0
curr = 1
```

**i = 2**

```text
ans = 0 + 1 = 1

prev = 1
curr = 1
```

**i = 3**

```text
ans = 1 + 1 = 2

prev = 1
curr = 2
```

**i = 4**

```text
ans = 1 + 2 = 3

prev = 2
curr = 3
```

**i = 5**

```text
ans = 2 + 3 = 5

prev = 3
curr = 5
```

Final answer:

```python
return curr  # 5
```

### Complexity

- **Time Complexity:** `O(N)` – one loop.
- **Space Complexity:** `O(1)` – only two variables.
- No DP array.
- No recursion stack.

---

# 7. Comparison of All Four Approaches

| Approach | Technique | Time Complexity | Space Complexity |
|---|---|---|---|
| Normal Recursion | Function calls itself | `O(2^N)` upper bound | `O(N)` |
| Top-Down DP | Recursion + Memoization | `O(N)` | `O(N)` |
| Bottom-Up DP | Tabulation | `O(N)` | `O(N)` |
| Space Optimization | Two Variables | `O(N)` | `O(1)` |

### Complete Flow

```text
Normal Recursion
       |
       | Repeated subproblems
       v
Top-Down DP
(Memoization)
       |
       | Remove recursion
       v
Bottom-Up DP
(Tabulation)
       |
       | Only two previous states needed
       v
Space Optimization
```

---

# 8. Important Concepts to Remember

### 1. Why Does Fibonacci Have Two Recursive Calls?

Because:

\[
fib(n) = fib(n-1) + fib(n-2)
\]

We need the previous two Fibonacci values to calculate the current value.

### 2. Why Is Memoization Faster?

Because every Fibonacci state is calculated only once and then reused.

### 3. Why Does the DP Array Have Size `n + 1`?

Because we need to store values from:

```text
dp[0] to dp[n]
```

That is a total of `n + 1` positions.

### 4. Why Does Tabulation Start from Index 2?

Because:

```python
dp[0] = 0
dp[1] = 1
```

The first two states are already initialized.

### 5. Why Do We Need Only Two Variables?

Because the recurrence depends only on the previous two values.

### 6. Why Is Space Optimization `O(1)`?

Because we maintain only:

```python
prev
curr
ans
```

The number of variables remains constant regardless of `n`.

---

# 9. Common Mistakes

- Forgetting the base cases `F(0) = 0` and `F(1) = 1`.
- Creating a DP array of size `n` instead of `n + 1`.
- Starting the tabulation loop from index `0` without initializing or handling base cases correctly.
- Using `dp[i] = dp[i] + dp[i - 1]` instead of the correct recurrence.
- Updating `prev` before using its old value.
- Forgetting that Python tuple assignment updates variables using the old right-hand-side values.
- Assuming memoization and tabulation use the same execution direction.
- Forgetting recursion stack space while analyzing memoization.

---

# 10. Pattern Recognition – Linear DP

Fibonacci is a basic example of **Linear DP**.

The current state depends on a fixed number of previous states.

For Fibonacci:

```python
dp[i] = dp[i - 1] + dp[i - 2]
```

Other problems with similar state dependencies:

- Climbing Stairs.
- Minimum Cost Climbing Stairs.
- Maximum Sum of Non-Adjacent Elements.
- House Robber.
- Some tiling problems.

### General Structure

```python
prev2 = initial_value_1
prev1 = initial_value_2

for i in range(start, n + 1):

    curr = calculate(prev1, prev2)

    prev2 = prev1
    prev1 = curr

return prev1
```

The exact recurrence and base cases depend on the problem.

---

# 11. Final Revision

| Concept | Remember |
|---|---|
| Fibonacci Formula | `fib(n) = fib(n-1) + fib(n-2)` |
| Base Case | `n <= 1` |
| Normal Recursion | Two recursive calls |
| Overlapping Subproblems | Same Fibonacci states repeat |
| Top-Down DP | Recursion + DP array |  
| Bottom-Up DP | Iteration + DP array |  
| Space Optimization | Maintain previous two values |    
| Final Answer | `curr` |    

**One-line takeaway:** Fibonacci is the foundation of DP. First understand its recursive relation, then store repeated states using memoization, calculate values iteratively using tabulation, and finally optimize space by keeping only the previous two Fibonacci numbers.   