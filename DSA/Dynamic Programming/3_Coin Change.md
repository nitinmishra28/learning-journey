# Coin Change – Recursion, Top-Down DP (Memoization) & Bottom-Up DP (Tabulation)

**Problem:** LeetCode 322 – Coin Change  
**Pattern:** Dynamic Programming – 1D DP / Minimum Cost / Unbounded Knapsack  
**Language:** Python

---

# 1. Problem Statement

You are given an integer array `coins`, where each element represents a coin denomination, and an integer `amount` representing the target amount.

Return the **minimum number of coins** required to make the given amount.

If the amount cannot be made using the given coins, return `-1`.

**Important:** You can use each coin denomination unlimited times.

### Example 1

```python
coins = [1, 2, 5]
amount = 11
```

Output:

```text
3
```

Explanation:

```text
5 + 5 + 1 = 11
```

We need a minimum of 3 coins.

### Example 2

```python
coins = [2]
amount = 3
```

Output:

```text
-1
```

Explanation:

We cannot make amount `3` using only coins of denomination `2`.

---

# 2. Core Intuition – Try Every Possible Coin

We need to find the minimum number of coins required to make the target amount.

At every step, we can try all coins that are smaller than or equal to the current amount.

For example:

```python
coins = [1, 2, 5]
amount = 11
```

We have three choices:

- Select coin `1`.
- Select coin `2`.
- Select coin `5`.

After selecting a coin, we subtract its value from the current amount and solve the remaining amount.

For example, if we select coin `5`:

```text
Remaining amount = 11 - 5 = 6
```

Now we need to find the minimum coins required to make amount `6`.

We repeat this process until the amount becomes `0`.

### Recurrence Relation

Let:

```text
solve(amount) = Minimum coins required to make the given amount.
```

For every valid coin:

\[
solve(amount) = \min(1 + solve(amount-coin))
\]

We take the minimum because our objective is to use the fewest coins.

### Base Case

\[
solve(0) = 0
\]

Why?

Because if the amount is already `0`, we don't need any coins.

### Impossible Amount

If no combination of coins can make the amount, return infinity during calculation.

```python
float('inf')
```

At the end, convert infinity into `-1`.

---

# 3. Approach 1 – Normal Recursion

First, solve the problem using normal recursion.

### Python Code

```python
class Solution:

    def solve(self, coins, amount):

        if amount == 0:
            return 0

        minimum = float('inf')

        for coin in coins:

            if coin <= amount:

                recursiveAns = self.solve(
                    coins,
                    amount - coin
                )

                if recursiveAns != float('inf'):

                    ans = 1 + recursiveAns

                    minimum = min(ans, minimum)

        return minimum

    def coinChange(self, coins: list[int], amount: int) -> int:

        ans = self.solve(coins, amount)

        return -1 if ans == float('inf') else ans
```

### Code Explanation

**1. Base Case**

```python
if amount == 0:
    return 0
```

Agar amount `0` ho gaya, toh humein aur coins ki zaroorat nahi hai.

Isliye return `0`.

**2. Initialize Minimum**

```python
minimum = float('inf')
```

Initially, minimum answer infinity rakhenge.

Kyunki humein minimum number of coins find karne hain.

**3. Try Every Coin**

```python
for coin in coins:
```

Har available coin ko try karenge.

**4. Check Whether Coin Can Be Used**

```python
if coin <= amount:
```

Agar coin ki value current amount se chhoti ya equal hai, tabhi us coin ko use kar sakte hain.

**5. Recursive Call**

```python
recursiveAns = self.solve(coins, amount - coin)
```

Current coin use karne ke baad remaining amount ka answer calculate karenge.

**6. Avoid Invalid Answers**

```python
if recursiveAns != float('inf'):
```

Agar remaining amount impossible hai, toh us result mein `1` add nahi karna chahiye.

**7. Add Current Coin**

```python
ans = 1 + recursiveAns
```

Humne ek coin use kiya hai, isliye recursive answer mein `1` add karenge.

**8. Find Minimum**

```python
minimum = min(ans, minimum)
```

Har valid coin choice ka answer compare karke minimum store karenge.

**9. Return Final Answer**

```python
return minimum
```

### Dry Run

Input:

```python
coins = [1, 2, 5]
amount = 5
```

We try all possible coins.

```text
solve(5)
    |
    |-- Select coin 1
    |      solve(4)
    |
    |-- Select coin 2
    |      solve(3)
    |
    |-- Select coin 5
           solve(0)
```

For `solve(0)`:

```python
return 0
```

Therefore, selecting coin `5` gives:

```text
1 + solve(0)
= 1 + 0
= 1
```

Other choices may also produce valid answers, but we select the minimum.

Final answer:

```text
1
```

### Complexity

Let:
- `A` = target amount.
- `C` = number of coin denominations.

- **Time Complexity:** Exponential in the worst case. A loose upper bound is `O(C^A)` for positive integer coin denominations.
- **Auxiliary Space:** `O(A)` recursion stack depth.

Why exponential?

Because at each recursive call, we can try multiple coins, and the same remaining amounts may be calculated repeatedly.

This leads to overlapping subproblems.

---

# 4. Approach 2 – Top-Down DP (Memoization)

In normal recursion, the same remaining amounts are calculated multiple times.

For example:

```text
solve(5)
    |
    |-- solve(4)
    |      |
    |      |-- solve(3)
    |
    |-- solve(3)
```

Notice that `solve(3)` is called more than once.

We can avoid this by storing the answer for every amount.

This is called **Memoization or Top-Down DP**.

### Python Code

```python
class Solution:

    def solve(self, coins, amount, dp):

        if amount == 0:
            return 0

        # Step 1: Check whether answer already exists
        if dp[amount] != -1:
            return dp[amount]

        minimum = float('inf')

        for coin in coins:

            if coin <= amount:

                recursiveAns = self.solve(
                    coins,
                    amount - coin,
                    dp
                )

                if recursiveAns != float('inf'):

                    ans = 1 + recursiveAns

                    minimum = min(ans, minimum)

        # Step 2: Calculate and store the answer
        dp[amount] = minimum

        return dp[amount]

    def coinChange(self, coins: list[int], amount: int) -> int:

        # Step 3: Create DP array
        dp = [-1] * (amount + 1)

        ans = self.solve(coins, amount, dp)

        return -1 if ans == float('inf') else ans
```

### Code Explanation

**1. Create DP Array**

```python
dp = [-1] * (amount + 1)
```

We create a DP array of size `amount + 1`.

Why?

Because our changing parameter is `amount`.

We need to store answers for:

```text
dp[0], dp[1], dp[2], ..., dp[amount]
```

Initially:

```text
dp = [-1, -1, -1, -1, ...]
```

`-1` means that the state has not been calculated yet.

**2. Base Case**

```python
if amount == 0:
    return 0
```

Zero amount requires zero coins.

**3. Check Whether Answer Exists**

```python
if dp[amount] != -1:
    return dp[amount]
```

Agar current amount ka answer already calculate ho chuka hai, toh directly return kar do.

**4. Initialize Minimum**

```python
minimum = float('inf')
```

We need the minimum number of coins, so initially the answer is infinity.

**5. Try Every Valid Coin**

```python
for coin in coins:

    if coin <= amount:
```

Only coins smaller than or equal to the current amount can be selected.

**6. Recursive Call**

```python
recursiveAns = self.solve(
    coins,
    amount - coin,
    dp
)
```

Current coin select karne ke baad remaining amount ka answer calculate karenge.

**7. Calculate Minimum**

```python
if recursiveAns != float('inf'):

    ans = 1 + recursiveAns

    minimum = min(ans, minimum)
```

Agar remaining amount possible hai, toh current coin count add karke minimum update karenge.

**8. Store the Answer**

```python
dp[amount] = minimum
```

Current amount ka final answer DP array mein store kar diya.

**9. Return Stored Answer**

```python
return dp[amount]
```

### Dry Run

Input:

```python
coins = [1, 2, 5]
amount = 5
```

Initially:

```text
dp = [-1, -1, -1, -1, -1, -1]
```

Suppose we calculate `solve(5)`.

After solving the smaller states, we store their answers.

```text
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 1
```

Final DP array:

```text
[0, 1, 1, 2, 2, 1]
```

If `solve(3)` is called again, the function checks:

```python
if dp[3] != -1:
    return dp[3]
```

It returns the stored answer without recalculating it.

### Complexity

- **Time Complexity:** `O(A * C)` – each amount is calculated once, and each state tries all coins.
- **DP Array Space:** `O(A)`.
- **Recursion Stack:** `O(A)` for positive coin denominations.
- **Total Auxiliary Space:** `O(A)`.

### Important

Memoization is Top-Down DP because we start with the target amount and recursively solve smaller amounts.

---

# 5. Approach 3 – Bottom-Up DP (Tabulation)

Now we will remove recursion.

In Top-Down DP, we started from the target amount and recursively moved towards zero.

In Bottom-Up DP, we start from amount `0` and calculate answers for increasing amounts.

### State Definition

Let:

```text
dp[amt] = Minimum number of coins required to make amount amt.
```

### Base Case

\[
dp[0] = 0
\]

Because zero amount requires zero coins.

### Recurrence Relation

For every valid coin:

\[
dp[amt] = \min(dp[amt], 1 + dp[amt-coin])
\]

We try all valid coins and choose the minimum answer.

### Python Code

```python
class Solution:

    def solve(self, coins, amount):

        # Step 1: Create DP array
        dp = [-1] * (amount + 1)

        # Step 2: Initialize base case
        dp[0] = 0

        # Step 3: Calculate answers from 1 to amount
        for amt in range(1, amount + 1):

            minimum = float('inf')

            for coin in coins:

                if coin <= amt:

                    recursiveAns = dp[amt - coin]

                    if recursiveAns != float('inf'):

                        ans = 1 + recursiveAns

                        minimum = min(ans, minimum)

            dp[amt] = minimum

        return dp[amount]

    def coinChange(self, coins: list[int], amount: int) -> int:

        ans = self.solve(coins, amount)

        return -1 if ans == float('inf') else ans
```

### Code Explanation

**1. Create DP Array**

```python
dp = [-1] * (amount + 1)
```

We create an array to store the minimum coins required for every amount from `0` to the target amount.

**2. Initialize Base Case**

```python
dp[0] = 0
```

Zero amount requires zero coins.

**3. Traverse Amounts**

```python
for amt in range(1, amount + 1):
```

We start from amount `1` and move towards the target amount.

Why?

Because smaller amounts must be calculated before larger amounts.

**4. Initialize Minimum**

```python
minimum = float('inf')
```

For every new amount, we start with infinity.

We will find the minimum number of coins required for this amount.

**5. Try Every Coin**

```python
for coin in coins:
```

We try all available coin denominations.

**6. Check Whether Coin Is Valid**

```python
if coin <= amt:
```

A coin cannot be selected if its value is greater than the current amount.

**7. Get Previous State**

```python
recursiveAns = dp[amt - coin]
```

This is the important difference from recursion.

In recursion, we were calling:

```python
self.solve(coins, amount - coin)
```

In tabulation, the smaller amount has already been calculated.

So we directly access:

```python
dp[amt - coin]
```

**8. Calculate Current Answer**

```python
ans = 1 + recursiveAns
```

We use one current coin, so add `1` to the answer for the remaining amount.

**9. Store Minimum**

```python
minimum = min(ans, minimum)
```

Compare all valid coin choices and keep the minimum.

**10. Update DP Array**

```python
dp[amt] = minimum
```

After trying all coins, store the minimum answer for the current amount.

**11. Return Final Answer**

```python
return dp[amount]
```

The last DP state contains the minimum coins required for the target amount.

---

# 6. Bottom-Up DP – Detailed Dry Run

Input:

```python
coins = [1, 2, 5]
amount = 11
```

Initially:

```python
dp = [-1] * 12
dp[0] = 0
```

Initial DP array:

```text
Index:  0   1   2   3   4   5   6   7   8   9  10  11
dp:     0  -1  -1  -1  -1  -1  -1  -1  -1  -1  -1  -1
```

### amt = 1

Available coin: `1`

```text
dp[1 - 1] = dp[0] = 0

ans = 1 + 0 = 1
```

```text
dp[1] = 1
```

### amt = 2

Try coin `1`:

```text
1 + dp[1] = 1 + 1 = 2
```

Try coin `2`:

```text
1 + dp[0] = 1 + 0 = 1
```

Minimum:

```text
dp[2] = 1
```

### amt = 3

Try coin `1`:

```text
1 + dp[2] = 2
```

Try coin `2`:

```text
1 + dp[1] = 2
```

Minimum:

```text
dp[3] = 2
```

### amt = 4

Try coin `1`:

```text
1 + dp[3] = 3
```

Try coin `2`:

```text
1 + dp[2] = 2
```

Minimum:

```text
dp[4] = 2
```

### amt = 5

Try coin `1`:

```text
1 + dp[4] = 3
```

Try coin `2`:

```text
1 + dp[3] = 3
```

Try coin `5`:

```text
1 + dp[0] = 1
```

Minimum:

```text
dp[5] = 1
```

Continue the same process until amount `11`.

Final DP array:

```text
Index:  0   1   2   3   4   5   6   7   8   9  10  11
dp:     0   1   1   2   2   1   2   2   3   3   2   3
```

Final answer:

```python
return dp[11]  # 3
```

Explanation:

```text
5 + 5 + 1 = 11
```

Minimum coins = `3`.

### Complexity

Let:
- `A` = target amount.
- `C` = number of coins.

- **Time Complexity:** `O(A * C)` – every amount tries every coin.
- **Space Complexity:** `O(A)` – DP array.
- No recursion stack.

---

# 7. Important: Why Do We Use `float('inf')`?

We are solving a minimum coins problem.

Initially, we don't know the minimum answer.

So we initialize:

```python
minimum = float('inf')
```

Infinity is greater than every finite number.

This allows us to compare valid answers easily.

Example:

```python
minimum = float('inf')

minimum = min(minimum, 3)  # 3
minimum = min(minimum, 2)  # 2
minimum = min(minimum, 4)  # 2
```

Final minimum:

```text
2
```

### Why Do We Check This Condition?

```python
if recursiveAns != float('inf'):
```

Suppose we cannot make the remaining amount.

Then its answer is infinity.

We should not add `1` to an impossible state and treat it as a valid solution.

### Why Do We Return -1?

```python
return -1 if ans == float('inf') else ans
```

The problem requires `-1` if no combination can make the target amount.

Infinity is only an internal representation of an impossible state.

---

# 8. Why Is the DP Array Size `amount + 1`?

Our changing parameter is `amount`.

We need to store the answers for every amount from `0` to the target.

For example:

```python
amount = 5
dp = [-1] * (amount + 1)
```

This creates:

```text
Index: 0  1  2  3  4  5
```

Total positions = `6`.

We need `amount + 1` because Python arrays start from index `0`.

---

# 9. Why Is There No Separate Space Optimization Here?

Our tabulation uses:

```python
dp[amt] = min(
    dp[amt],
    1 + dp[amt - coin]
)
```

To calculate the answer for a particular amount, we may need previous DP states for different coin values.

Unlike Fibonacci, where only the previous two states are required, Coin Change can depend on many previous amounts.

Therefore, we cannot directly replace the DP array with just two variables.

For this standard approach, we keep the complete one-dimensional DP array.

---

# 10. Comparison of All Approaches

| Approach | Technique | Time Complexity | Space Complexity |
|---|---|---|---|
| Normal Recursion | Try every valid coin | Exponential | `O(A)` stack |
| Top-Down DP | Recursion + Memoization | `O(A * C)` | `O(A)` |
| Bottom-Up DP | Tabulation | `O(A * C)` | `O(A)` |

### Complete Flow

```text
Normal Recursion
       |
       | Same amounts repeat
       v
Top-Down DP
(Memoization)
       |
       | Replace recursive calls with DP lookups
       v
Bottom-Up DP
(Tabulation)
```

---

# 11. Common Mistakes

### 1. Forgetting the Base Case

```python
if amount == 0:
    return 0
```

Without this, recursion will not have the correct stopping condition.

### 2. Not Checking Coin Validity

```python
if coin <= amount:
```

We cannot select a coin greater than the remaining amount.

### 3. Forgetting to Add One Coin

```python
ans = 1 + recursiveAns
```

The current coin must be counted.

### 4. Using `max()` Instead of `min()`

The problem asks for the minimum number of coins.

### 5. Not Handling Impossible Amounts

Use infinity for impossible states and return `-1` if the final answer remains infinity.

### 6. Wrong DP Array Size

Use:

```python
dp = [-1] * (amount + 1)
```

### 7. Confusing Minimum Coins with Number of Ways

These are different problems.

- Coin Change – LeetCode 322: Minimum number of coins.
- Coin Change II – LeetCode 518: Number of combinations.

Their recurrence relations and DP initialization are different.

### 8. Forgetting to Store the Answer in Memoization

```python
dp[amount] = minimum
```

If we don't store the calculated result, repeated subproblems will still be calculated.

---

# 12. Pattern Recognition – Minimum / Unbounded Knapsack

Coin Change follows the **Unbounded Knapsack** pattern.

Why?

Because each coin can be used unlimited times.

When we select a coin, we don't move to the next coin index. Instead, we reduce the remaining amount and can select the same coin again.

General idea:

```python
for coin in coins:

    if coin <= amount:

        remaining = amount - coin

        # Solve the remaining amount
```

### Related Problems

- Coin Change – LeetCode 322
- Coin Change II – LeetCode 518
- Minimum Cost for Tickets
- Unbounded Knapsack
- Rod Cutting

---

# 13. Final Revision

| Concept | Remember |
|---|---|
| Problem | Minimum number of coins |
| State | `dp[amount]` |
| Base Case | `dp[0] = 0` |
| Choices | Try every valid coin |
| Transition | `1 + dp[amount - coin]` |
| Operation | `min()` |
| Impossible State | `float('inf')` |
| Top-Down | Recursion + Memoization |
| Bottom-Up | Calculate amounts from `1` to `amount` |
| Final Answer | `dp[amount]` |
| Impossible Result | Return `-1` |

---

# 14. One-Line Takeaway

**Coin Change is a minimum-value Unbounded Knapsack DP problem. Try every valid coin, add one to the answer for the remaining amount, store the minimum, and reuse previously calculated states.**