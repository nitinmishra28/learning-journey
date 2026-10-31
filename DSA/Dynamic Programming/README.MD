# Dynamic Programming (DP) – Complete DSA Notes

My personal notes for learning **Dynamic Programming from basic to advanced**, following the problem-solving sequence of Love Babbar's DSA course.

**Language:** Python  
**Reference:** Love Babbar – CodeHelp DP Series  
**Goal:** Understand DP concepts, identify DP patterns, solve problems using recursion, memoization, tabulation and space optimization.

---

# 1. What is Dynamic Programming?

Dynamic Programming (DP) ek problem-solving technique hai jisme hum kisi problem ko smaller subproblems mein divide karte hain aur unke answers store kar lete hain.

Agar same subproblem dobara aata hai, toh usko dobara calculate karne ki jagah stored answer use karte hain.

Isse unnecessary calculations avoid hoti hain aur time complexity improve hoti hai.

### Simple Example – Fibonacci

Fibonacci series:

```text
0, 1, 1, 2, 3, 5, 8, 13, 21...
```

Mathematical relation:

\[
F(n) = F(n-1) + F(n-2)
\]

Base cases:

\[
F(0)=0,\quad F(1)=1
\]

Recursive Python solution:

```python
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

print(fib(5))  # 5
```

Problem kya hai?

`fib(5)` calculate karte waqt same subproblems multiple times calculate hote hain.

```text
                  fib(5)
                 /      \
             fib(4)     fib(3)
             /   \       /   \
         fib(3) fib(2) fib(2) fib(1)
```

Notice karo `fib(3)` aur `fib(2)` repeat ho rahe hain.

Agar hum inka answer ek baar calculate karke store kar lein, toh repeated calculations avoid kar sakte hain.

Yahi Dynamic Programming ka basic idea hai.

---

# 2. When Can We Apply DP?

Har recursive problem DP problem nahi hoti.

DP identify karne ke liye do important properties samajhna zaroori hai.

## 2.1 Overlapping Subproblems

Jab same subproblem baar-baar calculate hota hai, usse overlapping subproblems kehte hain.

Example:

```text
fib(5)
    |
    |-- fib(4)
    |      |-- fib(3)
    |      |-- fib(2)
    |
    |-- fib(3)
           |-- fib(2)
           |-- fib(1)
```

Yahan `fib(3)` aur `fib(2)` repeat ho rahe hain.

Hum inke answers store kar sakte hain.

## 2.2 Optimal Substructure

Jab kisi larger problem ka optimal answer uske smaller subproblems ke optimal answers se construct ho sakta hai, toh usse optimal substructure kehte hain.

Example:

Minimum cost problem mein agar hum current step tak minimum cost calculate kar sakte hain, toh us result ka use karke next step ka minimum cost calculate kar sakte hain.

**Important:**

- Overlapping subproblems: Same calculation repeat ho rahi hai.
- Optimal substructure: Smaller subproblem ke answers se larger problem ka answer construct ho sakta hai.

DP ke liye ye dono properties important hain.

---

# 3. Recursion vs Dynamic Programming

Sabse pehle recursion se problem solve karna seekho.

Uske baad identify karo ki same states repeat ho rahi hain ya nahi.

| Recursion | Dynamic Programming |
|---|---|
| Function khud ko call karta hai | Previous results store karta hai |
| Same problem repeat ho sakti hai | Repeated calculation avoid hoti hai |
| Usually simple to understand | Efficient for overlapping states |
| May take exponential time | Often reduces time complexity |

DP generally recursion ko optimize karne ka ek method hai, lekin har DP solution ko recursion se implement karna compulsory nahi hai.

---

# 4. Four Steps of Dynamic Programming

Love Babbar ke DP learning sequence ko follow karte hue, har problem ko in approaches se samajhna hai.

```text
1. Recursion
      |
      v
2. Memoization (Top-Down DP)
      |
      v
3. Tabulation (Bottom-Up DP)
      |
      v
4. Space Optimization
```

In chaar approaches ko samajhna DP ka foundation hai.

---

# 5. Recursion – First Approach

Recursion mein problem ko smaller subproblems mein divide karte hain.

Example: Fibonacci.

```python
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

print(fib(5))
```

### Dry Run

```text
fib(5)
    |
    |-- fib(4)
    |      |
    |      |-- fib(3)
    |      |-- fib(2)
    |
    |-- fib(3)
           |
           |-- fib(2)
           |-- fib(1)
```

Problem: Same function calls repeat ho rahi hain.

### Complexity

- Time: `O(2^N)` as a common upper-bound estimate.
- Auxiliary Space: `O(N)` recursion stack.

Ab isko optimize karenge.

---

# 6. Memoization – Top-Down DP

Memoization ka matlab hai recursive function ke calculated answers ko store karna.

Jab same state dobara call hoti hai, toh stored answer return kar dete hain.

### Fibonacci Using Memoization

```python
def fib(n, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = fib(n - 1, dp) + fib(n - 2, dp)

    return dp[n]


n = 5
dp = [-1] * (n + 1)

print(fib(n, dp))  # 5
```

### Code Explanation

**1. DP array create karna**

```python
dp = [-1] * (n + 1)
```

`-1` ka matlab hai ki abhi state calculate nahi hui hai.

**2. Check whether answer already exists**

```python
if dp[n] != -1:
    return dp[n]
```

Agar answer already calculate ho chuka hai, toh directly return kar do.

**3. Calculate and store**

```python
dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
```

Result calculate karke DP array mein store kar diya.

### Dry Run

For `fib(5)`:

```text
fib(5)
    |
    |-- fib(4)
    |      |
    |      |-- fib(3)
    |      |-- fib(2)
    |
    |-- fib(3)  <-- Already calculated
```

Second time `fib(3)` call hone par function stored answer return karega.

### Complexity

- Time: `O(N)`
- DP Array: `O(N)`
- Recursion Stack: `O(N)`
- Total Auxiliary Space: `O(N)`

**Remember:** Memoization is Top-Down DP because hum final problem se start karte hain aur recursively smaller states tak jaate hain.

---

# 7. Tabulation – Bottom-Up DP

Tabulation mein recursion use nahi karte.

Hum smallest subproblems ka answer pehle calculate karte hain, phir un answers ko use karke larger subproblems solve karte hain.

### Fibonacci Using Tabulation

```python
def fib(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(fib(5))  # 5
```

### Dry Run

For `n = 5`:

Initially:

```text
dp = [0, 1, 0, 0, 0, 0]
```

Calculate:

```text
dp[2] = dp[1] + dp[0] = 1
dp[3] = dp[2] + dp[1] = 2
dp[4] = dp[3] + dp[2] = 3
dp[5] = dp[4] + dp[3] = 5
```

Final DP array:

```text
[0, 1, 1, 2, 3, 5]
```

Answer:

```python
return dp[n]
```

### Complexity

- Time: `O(N)`
- Space: `O(N)`

**Remember:** Tabulation is Bottom-Up DP because hum base cases se start karke final answer tak pahunchte hain.

---

# 8. Space Optimization

Tabulation mein hum poora DP array store kar rahe the.

Lekin Fibonacci mein current answer calculate karne ke liye sirf previous two values chahiye.

Toh poora array store karne ki zaroorat nahi hai.

### Fibonacci Using Space Optimization

```python
def fib(n):
    if n <= 1:
        return n

    prev2 = 0
    prev1 = 1

    for i in range(2, n + 1):
        curr = prev1 + prev2

        prev2 = prev1
        prev1 = curr

    return prev1


print(fib(5))  # 5
```

### Dry Run

```text
Initial:
prev2 = 0
prev1 = 1

i = 2:
curr = 0 + 1 = 1

i = 3:
curr = 1 + 1 = 2

i = 4:
curr = 1 + 2 = 3

i = 5:
curr = 2 + 3 = 5
```

### Complexity

- Time: `O(N)`
- Space: `O(1)`

### Important

Space optimization tabhi possible hai jab current state calculate karne ke liye limited previous states ki zaroorat ho.

Har DP problem mein space optimization possible nahi hoti.

---

# 9. Memoization vs Tabulation vs Space Optimization

| Approach | Technique | Time | Space |
|---|---|---|---|
| Recursion | Repeated function calls | `O(2^N)` for naive Fibonacci | `O(N)` |
| Memoization | Recursion + DP array | `O(N)` | `O(N)` |
| Tabulation | Iteration + DP array | `O(N)` | `O(N)` |
| Space Optimization | Iteration + variables | `O(N)` | `O(1)` |

### Difference

**Memoization**
- Recursion use hota hai.
- Answer calculate hone ke baad store hota hai.
- Sirf required states calculate ho sakti hain.

**Tabulation**
- Iteration use hota hai.
- Base cases se start karte hain.
- DP array mein states calculate hoti hain.

**Space Optimization**
- DP array ki jagah limited variables use karte hain.
- Previous required states maintain karte hain.

---

# 10. How to Solve Any DP Problem

DP problem solve karte waqt ye steps follow karo.

## Step 1: Identify the State

State ka matlab hai kisi subproblem ko uniquely identify karna.

Example:

```python
solve(index)
```

Yahan `index` state hai.

Agar problem mein index aur target dono change ho rahe hain:

```python
solve(index, target)
```

Toh state mein dono parameters involved hain.

## Step 2: Identify the Base Case

Smallest possible state ka answer identify karo.

Example:

```python
if index == 0:
    return 0
```

Base case problem ke according change hoga.

## Step 3: Write the Recurrence Relation

Current state ka answer smaller states ke answers se kaise calculate hoga?

Example:

```python
return solve(index - 1) + solve(index - 2)
```

## Step 4: Implement Recursion

Pehle simple recursive solution likho.

## Step 5: Add Memoization

Changing parameters ko DP array ya dictionary mein store karo.

## Step 6: Convert to Tabulation

Recursive calls ko loops mein convert karo.

## Step 7: Space Optimize

Check karo ki previous kitni states ki zaroorat hai.

### DP Problem Checklist

```text
1. State kya hai?
2. Base case kya hai?
3. Choices kya hain?
4. Recurrence relation kya hai?
5. Memoization kaise lagayenge?
6. Tabulation ka order kya hoga?
7. Space optimize ho sakta hai?
```

---

# 11. DP State – 1D, 2D and More Dimensions

DP state samajhna bahut important hai.

State ke basis par DP array ka dimension decide hota hai.

## 11.1 1D DP

Jab ek changing parameter ho.

Example:

```python
solve(index)
```

DP:

```python
dp = [-1] * n
```

Problems:
- Fibonacci.
- Climbing Stairs.
- Maximum Sum of Non-Adjacent Elements.
- Minimum Cost Climbing Stairs.

## 11.2 2D DP

Jab do changing parameters ho.

Example:

```python
solve(index, target)
```

DP:

```python
dp = [[-1] * (target + 1) for _ in range(n + 1)]
```

Problems:
- 0/1 Knapsack.
- Subset Sum.
- Coin Change.
- Longest Common Subsequence.

## 11.3 3D DP

Jab three changing parameters ho.

Example:

```python
solve(index, buy, transactions)
```

DP:

```python
dp = [
    [
        [-1] * (transactions + 1)
        for _ in range(2)
    ]
    for _ in range(n + 1)
]
```

Problems:
- Stock Buy and Sell with transaction limits.
- Some multi-state DP problems.

**Important:** DP dimensions changing parameters se decide hote hain, problem ke naam se nahi.

---

# 12. DP Pattern 1 – Fibonacci / Linear DP

Is pattern mein current state previous one or two states par depend karti hai.

## Example: Climbing Stairs

LeetCode 70

Problem:

Tumhare paas `n` stairs hain. Har baar tum 1 ya 2 steps climb kar sakte ho.

Total kitne different ways se top tak pahunch sakte ho?

### Observation

Agar tum step `n` par pahunchna chahte ho, toh:
- Ya step `n-1` se aaoge.
- Ya step `n-2` se aaoge.

Therefore:

\[
ways(n) = ways(n-1) + ways(n-2)
\]

### Recursion

```python
def climbStairs(n):
    if n <= 2:
        return n

    return climbStairs(n - 1) + climbStairs(n - 2)
```

### Memoization

```python
def climbStairs(n):
    dp = [-1] * (n + 1)

    def solve(n):
        if n <= 2:
            return n

        if dp[n] != -1:
            return dp[n]

        dp[n] = solve(n - 1) + solve(n - 2)

        return dp[n]

    return solve(n)
```

### Tabulation

```python
def climbStairs(n):
    if n <= 2:
        return n

    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```

### Space Optimization

```python
def climbStairs(n):
    if n <= 2:
        return n

    prev2 = 1
    prev1 = 2

    for i in range(3, n + 1):
        curr = prev1 + prev2

        prev2 = prev1
        prev1 = curr

    return prev1
```

### Complexity

| Approach | Time | Space |
|---|---|---|
| Recursion | Exponential | `O(N)` stack |
| Memoization | `O(N)` | `O(N)` |
| Tabulation | `O(N)` | `O(N)` |
| Optimization | `O(N)` | `O(1)` |

---

# 13. DP Pattern 2 – Minimum Cost Climbing Stairs

LeetCode 746

Problem:

Har stair ki ek cost hai. Tum 1 ya 2 steps move kar sakte ho.

Top tak pahunchne ke liye minimum total cost find karni hai.

Example:

```python
cost = [10, 15, 20]
```

Answer:

```text
15
```

### Recurrence

Agar current stair `i` hai:

\[
dp[i] = cost[i] + min(dp[i-1], dp[i-2])
\]

Hum top par last two possible positions se aa sakte hain.

### Tabulation

```python
def minCostClimbingStairs(cost):
    n = len(cost)

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = min(
            dp[i - 1] + cost[i - 1],
            dp[i - 2] + cost[i - 2]
        )

    return dp[n]
```

### Space Optimization

```python
def minCostClimbingStairs(cost):
    prev2 = 0
    prev1 = 0

    for i in range(2, len(cost) + 1):
        curr = min(
            prev1 + cost[i - 1],
            prev2 + cost[i - 2]
        )

        prev2 = prev1
        prev1 = curr

    return prev1
```

Complexity:
- Time: `O(N)`
- Space: `O(1)` in optimized version.

---

# 14. DP Pattern 3 – Minimum Number of Coins

LeetCode 322 – Coin Change

Problem:

Coins ke different denominations diye hain.

Target amount banane ke liye minimum coins find karo.

Example:

```python
coins = [1, 2, 5]
amount = 11
```

Answer:

```text
3
```

Explanation:

```text
5 + 5 + 1 = 11
```

### Recurrence

Har coin ko use karke remaining amount solve kar sakte hain.

\[
dp[amount] = 1 + min(dp[amount-coin])
\]

Invalid amount ke liye answer infinity rakhenge.

### Python Tabulation

```python
def coinChange(coins, amount):
    dp = [float("inf")] * (amount + 1)

    dp[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:

            if current_amount >= coin:
                dp[current_amount] = min(
                    dp[current_amount],
                    1 + dp[current_amount - coin]
                )

    if dp[amount] == float("inf"):
        return -1

    return dp[amount]
```

### Dry Run

```text
coins = [1, 2, 5]
amount = 11
```

Possible minimum combination:

```text
5 + 5 + 1 = 11
```

Answer = 3.

### Complexity

- Time: `O(Amount * Number of Coins)`
- Space: `O(Amount)`

**Important:** Minimum coin count aur number of ways to make amount are different problems. Dono ka recurrence alag ho sakta hai.

---

# 15. DP Pattern 4 – Maximum Sum of Non-Adjacent Elements

Problem:

Array diya hai. Maximum sum find karo, lekin adjacent elements select nahi kar sakte.

Example:

```python
arr = [2, 1, 4, 9]
```

Answer:

```text
11
```

Explanation:

```text
2 + 9 = 11
```

### Choices

Har element par two choices hain:

1. Include current element.
2. Exclude current element.

Agar current element include karte hain, toh previous element skip karna padega.

### Recurrence

\[
dp[i] = max(arr[i] + dp[i-2], dp[i-1])
\]

### Python Code

```python
def maximumNonAdjacentSum(arr):
    n = len(arr)

    if n == 0:
        return 0

    prev2 = 0
    prev1 = 0

    for num in arr:
        curr = max(
            num + prev2,
            prev1
        )

        prev2 = prev1
        prev1 = curr

    return prev1


print(maximumNonAdjacentSum([2, 1, 4, 9]))  # 11
```

Complexity:
- Time: `O(N)`
- Space: `O(1)`

---

# 16. DP Pattern 5 – House Robber

LeetCode 198

Problem:

Houses ek line mein hain. Adjacent houses ko rob nahi kar sakte.

Maximum money find karo.

This is the same non-adjacent maximum sum pattern.

```python
def rob(nums):
    prev2 = 0
    prev1 = 0

    for money in nums:
        curr = max(
            money + prev2,
            prev1
        )

        prev2 = prev1
        prev1 = curr

    return prev1
```

Complexity:
- Time: `O(N)`
- Space: `O(1)`

**Pattern:** Include current OR exclude current.

---

# 17. DP Pattern 6 – Cut Rod into Segments

Problem:

Ek rod ki length `n` hai. Tum rod ko given lengths `x`, `y`, `z` mein cut kar sakte ho.

Maximum number of segments find karo.

Example:

```text
n = 7
x = 5
y = 2
z = 2
```

Answer:

```text
2
```

Possible cuts:

```text
5 + 2 = 7
```

### Tabulation

```python
def maximizeTheCuts(n, x, y, z):
    dp = [-float("inf")] * (n + 1)

    dp[0] = 0

    for i in range(1, n + 1):

        for cut in (x, y, z):
            if i >= cut and dp[i - cut] != -float("inf"):
                dp[i] = max(
                    dp[i],
                    1 + dp[i - cut]
                )

    return max(0, dp[n])
```

Complexity:
- Time: `O(N * 3)` = `O(N)`
- Space: `O(N)`

---

# 18. DP Pattern 7 – Count Derangements

Derangement ka matlab hai permutation mein koi bhi element apni original position par nahi hona chahiye.

Example:

Original:

```text
[1, 2, 3]
```

Valid derangements:

```text
[2, 3, 1]
[3, 1, 2]
```

Answer = 2.

### Recurrence

Derangement recurrence:

\[
D(n) = (n-1)(D(n-1)+D(n-2))
\]

Base cases:

\[
D(1)=0
\]

\[
D(2)=1
\]

### Python Code

```python
def countDerangements(n):
    if n == 1:
        return 0

    if n == 2:
        return 1

    prev2 = 0
    prev1 = 1

    for i in range(3, n + 1):
        curr = (i - 1) * (prev1 + prev2)

        prev2 = prev1
        prev1 = curr

    return prev1
```

Complexity:
- Time: `O(N)`
- Space: `O(1)`

For large values, apply modulo if the problem requires it.

---

# 19. DP Pattern 8 – Painting Fence Algorithm

Problem:

`n` fence posts hain aur `k` different colors hain.

Condition: Three consecutive posts same color nahi ho sakte.

Find total possible ways.

### State

Let `dp[i]` be the number of ways to paint `i` posts.

### Recurrence

\[
dp[i] = (k-1)(dp[i-1]+dp[i-2])
\]

Base cases:

\[
dp[1] = k
\]

\[
dp[2] = k^2
\]

### Python Code

```python
def countWays(n, k):
    if n == 1:
        return k

    if n == 2:
        return k * k

    prev2 = k
    prev1 = k * k

    for i in range(3, n + 1):
        curr = (k - 1) * (prev1 + prev2)

        prev2 = prev1
        prev1 = curr

    return prev1
```

Complexity:
- Time: `O(N)`
- Space: `O(1)`

---

# 20. DP Pattern 9 – 0/1 Knapsack

This is one of the most important DP patterns.

Problem:

Tumhare paas items hain. Har item ka:
- Weight.
- Value.

Bag ki maximum capacity given hai.

Maximum value find karo without exceeding capacity.

**0/1 ka meaning:**

Har item ko:
- Either include kar sakte ho.
- Ya exclude kar sakte ho.

Ek item ko multiple times use nahi kar sakte.

Example:

```python
weights = [1, 2, 4, 5]
values = [5, 4, 8, 6]
capacity = 5
```

Answer:

```text
13
```

Choose:
- Weight 1, value 5.
- Weight 4, value 8.

Total weight = 5.

Total value = 13.

### Recursion

```python
def knapsack(weights, values, capacity, index):
    if index == 0:
        if weights[0] <= capacity:
            return values[0]

        return 0

    exclude = knapsack(
        weights,
        values,
        capacity,
        index - 1
    )

    include = 0

    if weights[index] <= capacity:
        include = values[index] + knapsack(
            weights,
            values,
            capacity - weights[index],
            index - 1
        )

    return max(include, exclude)
```

### Memoization

```python
def knapsack(weights, values, capacity):
    n = len(weights)

    dp = [
        [-1] * (capacity + 1)
        for _ in range(n)
    ]

    def solve(index, remaining):
        if index == 0:
            if weights[0] <= remaining:
                return values[0]

            return 0

        if dp[index][remaining] != -1:
            return dp[index][remaining]

        exclude = solve(index - 1, remaining)

        include = 0

        if weights[index] <= remaining:
            include = values[index] + solve(
                index - 1,
                remaining - weights[index]
            )

        dp[index][remaining] = max(include, exclude)

        return dp[index][remaining]

    return solve(n - 1, capacity)
```

### Tabulation

```python
def knapsack(weights, values, capacity):
    n = len(weights)

    dp = [
        [0] * (capacity + 1)
        for _ in range(n)
    ]

    for w in range(weights[0], capacity + 1):
        dp[0][w] = values[0]

    for index in range(1, n):

        for w in range(capacity + 1):

            exclude = dp[index - 1][w]

            include = 0

            if weights[index] <= w:
                include = values[index] + dp[
                    index - 1
                ][w - weights[index]]

            dp[index][w] = max(include, exclude)

    return dp[n - 1][capacity]
```

### Complexity

Let `N` be number of items and `W` be capacity.

- Time: `O(N * W)`
- Space: `O(N * W)`

### Space Optimization

```python
def knapsack(weights, values, capacity):
    n = len(weights)

    dp = [0] * (capacity + 1)

    for index in range(n):

        for w in range(capacity, weights[index] - 1, -1):

            dp[w] = max(
                dp[w],
                values[index] + dp[w - weights[index]]
            )

    return dp[capacity]
```

Complexity:
- Time: `O(N * W)`
- Space: `O(W)`

**Important:** 0/1 Knapsack mein capacity loop reverse direction mein chalta hai. Isse current item ek hi baar use hota hai.

---

# 21. 0/1 Knapsack vs Unbounded Knapsack

Dono bahut important patterns hain.

| 0/1 Knapsack | Unbounded Knapsack |
|---|---|
| Item ek baar use ho sakta hai | Item multiple times use ho sakta hai |
| Include or exclude | Include and reuse possible |
| Capacity loop reverse | Capacity loop forward |
| Previous item row use hoti hai | Current row reuse ho sakti hai |

### 0/1 Knapsack

```python
for w in range(capacity, weight - 1, -1):
    dp[w] = max(
        dp[w],
        value + dp[w - weight]
    )
```

### Unbounded Knapsack

```python
for w in range(weight, capacity + 1):
    dp[w] = max(
        dp[w],
        value + dp[w - weight]
    )
```

Loop direction is important because it decides whether an item can be reused in the same iteration.

---

# 22. DP Pattern 10 – Subset Sum Problem

Problem:

Array diya hai. Check karo kya kisi subset ka sum target ke equal ho sakta hai.

Example:

```python
arr = [2, 3, 7, 8, 10]
target = 11
```

Answer:

```text
True
```

Because:

```text
3 + 8 = 11
```

### Choices

Har element ke liye:
- Include.
- Exclude.

### Tabulation

```python
def subsetSum(arr, target):
    n = len(arr)

    dp = [
        [False] * (target + 1)
        for _ in range(n + 1)
    ]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):

        for j in range(1, target + 1):

            exclude = dp[i - 1][j]

            include = False

            if arr[i - 1] <= j:
                include = dp[i - 1][j - arr[i - 1]]

            dp[i][j] = include or exclude

    return dp[n][target]
```

Complexity:
- Time: `O(N * Target)`
- Space: `O(N * Target)`

### Space Optimization

```python
def subsetSum(arr, target):
    dp = [False] * (target + 1)

    dp[0] = True

    for num in arr:

        for current in range(target, num - 1, -1):
            dp[current] = dp[current] or dp[current - num]

    return dp[target]
```

Complexity:
- Time: `O(N * Target)`
- Space: `O(Target)`

---

# 23. DP Pattern 11 – Equal Sum Partition

Problem:

Array ko two subsets mein divide karna hai such that dono subsets ka sum equal ho.

Example:

```python
arr = [1, 5, 11, 5]
```

Total sum:

```text
22
```

Required subset sum:

```text
22 / 2 = 11
```

Agar target `11` ka subset exist karta hai, toh equal partition possible hai.

### Python Code

```python
def canPartition(nums):
    total = sum(nums)

    if total % 2 != 0:
        return False

    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:

        for current in range(target, num - 1, -1):
            dp[current] = dp[current] or dp[current - num]

    return dp[target]
```

Complexity:
- Time: `O(N * Target)`
- Space: `O(Target)`

---

# 24. DP Pattern 12 – Minimum Subset Sum Difference

Problem:

Array ko two subsets mein divide karo such that dono subset sums ka absolute difference minimum ho.

Let total sum be `S`.

Agar first subset ka sum `s1` hai, then second subset ka sum:

\[
s2 = S-s1
\]

Difference:

\[
|s1-s2| = |S-2s1|
\]

We need to find the achievable subset sum closest to `S/2`.

### Python Code

```python
def minSubsetSumDifference(arr):
    total = sum(arr)

    dp = [False] * (total + 1)
    dp[0] = True

    for num in arr:

        for current in range(total, num - 1, -1):
            dp[current] = dp[current] or dp[current - num]

    answer = float("inf")

    for s1 in range(total // 2 + 1):
        if dp[s1]:
            s2 = total - s1
            answer = min(answer, abs(s1 - s2))

    return answer
```

Complexity:
- Time: `O(N * Total Sum)`
- Space: `O(Total Sum)`

---

# 25. DP Pattern 13 – Coin Change: Number of Ways

LeetCode 518 – Coin Change II

Minimum coins aur number of ways different problems hain.

Problem:

Coins diye hain. Target amount banane ke total combinations count karo.

Example:

```python
coins = [1, 2, 5]
amount = 5
```

Possible combinations:

```text
5
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1
```

Answer = 4.

### Tabulation

```python
def change(amount, coins):
    dp = [0] * (amount + 1)

    dp[0] = 1

    for coin in coins:

        for current in range(coin, amount + 1):
            dp[current] += dp[current - coin]

    return dp[amount]
```

Complexity:
- Time: `O(Number of Coins * Amount)`
- Space: `O(Amount)`

**Important:** Coin loop outside and amount loop forward gives combinations where order does not matter.

---

# 26. DP Pattern 14 – Longest Increasing Subsequence (LIS)

LeetCode 300

Problem:

Array diya hai. Longest strictly increasing subsequence ki length find karo.

Example:

```python
nums = [10, 9, 2, 5, 3, 7, 101, 18]
```

Answer:

```text
4
```

One LIS:

```text
[2, 3, 7, 101]
```

### Approach 1 – DP O(N²)

Let `dp[i]` be the LIS length ending at index `i`.

Initially:

```python
dp = [1] * n
```

Har element ka minimum LIS length 1 hota hai.

### Python Code

```python
def lengthOfLIS(nums):
    n = len(nums)

    dp = [1] * n

    for i in range(n):

        for j in range(i):

            if nums[j] < nums[i]:
                dp[i] = max(
                    dp[i],
                    dp[j] + 1
                )

    return max(dp)
```

Complexity:
- Time: `O(N²)`
- Space: `O(N)`

### Approach 2 – Binary Search O(N log N)

```python
from bisect import bisect_left

def lengthOfLIS(nums):
    lis = []

    for num in nums:
        index = bisect_left(lis, num)

        if index == len(lis):
            lis.append(num)
        else:
            lis[index] = num

    return len(lis)
```

Complexity:
- Time: `O(N log N)`
- Space: `O(N)`

**Important:** Binary search approach length find karta hai. `lis` array necessarily actual LIS nahi hota.

---

# 27. DP Pattern 15 – Longest Arithmetic Subsequence

Problem:

Array diya hai. Longest arithmetic subsequence ki length find karo.

Arithmetic subsequence mein consecutive selected elements ka difference same hota hai.

Example:

```python
nums = [3, 6, 9, 12]
```

Answer:

```text
4
```

Difference = 3.

### Python Code

```python
def longestArithSeqLength(nums):
    n = len(nums)

    dp = [{} for _ in range(n)]

    answer = 0

    for i in range(n):

        for j in range(i):

            diff = nums[i] - nums[j]

            length = dp[j].get(diff, 1) + 1

            dp[i][diff] = length

            answer = max(answer, length)

    return answer
```

Complexity:
- Time: `O(N²)` average dictionary operations.
- Space: `O(N²)` in the worst case.

---

# 28. DP Pattern 16 – Longest Arithmetic Subsequence with Given Difference

LeetCode 1218

Problem:

Given difference ke saath longest arithmetic subsequence ki length find karo.

### Python Code

```python
def longestSubsequence(arr, difference):
    dp = {}

    answer = 0

    for num in arr:

        previous = num - difference

        dp[num] = dp.get(previous, 0) + 1

        answer = max(answer, dp[num])

    return answer
```

Complexity:
- Time: `O(N)` average.
- Space: `O(N)`.

---

# 29. DP Pattern 17 – Unique Binary Search Trees

LeetCode 96

Problem:

`n` unique values `1` to `n` diye hain.

Kitne structurally unique Binary Search Trees create ho sakte hain?

This problem is related to Catalan numbers.

### Recurrence

Har number ko root choose kar sakte hain.

Agar `i` root hai:
- Left subtree mein `i-1` nodes.
- Right subtree mein `n-i` nodes.

\[
dp[n] = \sum_{i=1}^{n} dp[i-1] \times dp[n-i]
\]

Base case:

\[
dp[0] = 1
\]

### Python Code

```python
def numTrees(n):
    dp = [0] * (n + 1)

    dp[0] = 1

    if n >= 1:
        dp[1] = 1

    for nodes in range(2, n + 1):

        for root in range(1, nodes + 1):

            left = root - 1
            right = nodes - root

            dp[nodes] += dp[left] * dp[right]

    return dp[n]
```

Complexity:
- Time: `O(N²)`
- Space: `O(N)`

---

# 30. DP Pattern 18 – Stock Buy and Sell Problems

Stock problems are important examples of state-based DP.

Different variations have different constraints.

## Stock I – One Transaction

LeetCode 121

One buy and one sell allowed.

Goal: Maximum profit.

### Python Code

```python
def maxProfit(prices):
    min_price = float("inf")
    max_profit = 0

    for price in prices:

        min_price = min(min_price, price)

        profit = price - min_price

        max_profit = max(max_profit, profit)

    return max_profit
```

Complexity:
- Time: `O(N)`
- Space: `O(1)`

## Stock II – Unlimited Transactions

LeetCode 122

Multiple transactions allowed, but one stock can be held at a time.

```python
def maxProfit(prices):
    profit = 0

    for i in range(1, len(prices)):

        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit
```

Complexity:
- Time: `O(N)`
- Space: `O(1)`

## Stock III – At Most Two Transactions

LeetCode 123

At most two buy-sell transactions allowed.

A common DP state is:

```text
index
buy
transactions_left
```

Here:
- `index`: Current day.
- `buy`: Whether we can buy.
- `transactions_left`: Remaining transactions.

### Memoization

```python
from functools import lru_cache

def maxProfit(prices):

    n = len(prices)

    @lru_cache(None)
    def solve(index, can_buy, remaining):

        if index == n or remaining == 0:
            return 0

        if can_buy:

            buy = -prices[index] + solve(
                index + 1,
                0,
                remaining
            )

            skip = solve(
                index + 1,
                1,
                remaining
            )

            return max(buy, skip)

        else:

            sell = prices[index] + solve(
                index + 1,
                1,
                remaining - 1
            )

            hold = solve(
                index + 1,
                0,
                remaining
            )

            return max(sell, hold)

    return solve(0, 1, 2)
```

Complexity:
- Time: `O(N * 2 * 3)` = `O(N)`.
- Space: `O(N * 2 * 3)` for memoized states, plus recursion stack.

## Stock IV – At Most K Transactions

LeetCode 188

Same idea, but transactions limit is `k`.

```python
from functools import lru_cache

def maxProfit(k, prices):

    n = len(prices)

    @lru_cache(None)
    def solve(index, can_buy, remaining):

        if index == n or remaining == 0:
            return 0

        if can_buy:

            buy = -prices[index] + solve(
                index + 1,
                0,
                remaining
            )

            skip = solve(
                index + 1,
                1,
                remaining
            )

            return max(buy, skip)

        sell = prices[index] + solve(
            index + 1,
            1,
            remaining - 1
        )

        hold = solve(
            index + 1,
            0,
            remaining
        )

        return max(sell, hold)

    return solve(0, 1, k)
```

Complexity:
- Time: `O(N * K)`
- Space: `O(N * K)` for memoized states, plus recursion stack.

---

# 31. DP Pattern 19 – Longest Common Subsequence (LCS)

LeetCode 1143

Problem:

Do strings diye hain. Longest common subsequence ki length find karo.

Subsequence ka matlab hai characters ka relative order same rahe, lekin continuous hona compulsory nahi hai.

Example:

```python
text1 = "abcde"
text2 = "ace"
```

Answer:

```text
3
```

LCS:

```text
"ace"
```

### Recurrence

Agar characters match karte hain:

\[
dp[i][j] = 1 + dp[i-1][j-1]
\]

Agar match nahi karte:

\[
dp[i][j] = max(dp[i-1][j],dp[i][j-1])
\]

### Tabulation

```python
def longestCommonSubsequence(text1, text2):

    n = len(text1)
    m = len(text2)

    dp = [
        [0] * (m + 1)
        for _ in range(n + 1)
    ]

    for i in range(1, n + 1):

        for j in range(1, m + 1):

            if text1[i - 1] == text2[j - 1]:

                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:

                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    return dp[n][m]
```

Complexity:
- Time: `O(N * M)`
- Space: `O(N * M)`

---

# 32. DP Pattern 20 – Longest Palindromic Subsequence

LeetCode 516

Problem:

String mein longest palindromic subsequence ki length find karo.

Example:

```python
s = "bbbab"
```

Answer:

```text
4
```

One possible subsequence:

```text
"bbbb"
```

### Important Observation

Longest Palindromic Subsequence ko LCS ke through solve kar sakte hain.

String ka reverse banao aur dono ka LCS find karo.

### Python Code

```python
def longestPalindromeSubseq(s):

    reversed_s = s[::-1]

    n = len(s)

    dp = [
        [0] * (n + 1)
        for _ in range(n + 1)
    ]

    for i in range(1, n + 1):

        for j in range(1, n + 1):

            if s[i - 1] == reversed_s[j - 1]:

                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:

                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    return dp[n][n]
```

Complexity:
- Time: `O(N²)`
- Space: `O(N²)`

---

# 33. DP Pattern 21 – Edit Distance

LeetCode 72

Problem:

Ek string ko doosri string mein convert karne ke liye minimum operations find karo.

Allowed operations:

1. Insert
2. Delete
3. Replace

Example:

```python
word1 = "horse"
word2 = "ros"
```

Answer:

```text
3
```

### Recurrence

Agar characters match karte hain:

\[
dp[i][j] = dp[i-1][j-1]
\]

Agar match nahi karte:

\[
dp[i][j] = 1 + min(
dp[i-1][j],
dp[i][j-1],
dp[i-1][j-1]
)
\]

### Python Code

```python
def minDistance(word1, word2):

    n = len(word1)
    m = len(word2)

    dp = [
        [0] * (m + 1)
        for _ in range(n + 1)
    ]

    for i in range(n + 1):
        dp[i][0] = i

    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):

        for j in range(1, m + 1):

            if word1[i - 1] == word2[j - 1]:

                dp[i][j] = dp[i - 1][j - 1]

            else:

                insert = dp[i][j - 1]
                delete = dp[i - 1][j]
                replace = dp[i - 1][j - 1]

                dp[i][j] = 1 + min(
                    insert,
                    delete,
                    replace
                )

    return dp[n][m]
```

Complexity:
- Time: `O(N * M)`
- Space: `O(N * M)`

---

# 34. DP Pattern 22 – Wildcard Pattern Matching

LeetCode 44

Problem:

String aur pattern diye hain.

Pattern mein:
- `?` matches exactly one character.
- `*` matches any sequence of characters, including empty sequence.

Example:

```python
s = "adceb"
p = "*a*b"
```

Answer:

```text
True
```

### Important Cases

If characters match:

```text
Move both pointers.
```

If pattern character is `?`:

```text
Move both pointers.
```

If pattern character is `*`:

Two possibilities:
1. `*` matches empty sequence – move pattern pointer.
2. `*` matches current character – move string pointer.

### Memoization

```python
from functools import lru_cache

def isMatch(s, p):

    n = len(s)
    m = len(p)

    @lru_cache(None)
    def solve(i, j):

        if j == m:
            return i == n

        if i == n:
            return all(ch == '*' for ch in p[j:])

        if p[j] == s[i] or p[j] == '?':
            return solve(i + 1, j + 1)

        if p[j] == '*':
            return (
                solve(i, j + 1) or
                solve(i + 1, j)
            )

        return False

    return solve(0, 0)
```

Complexity:
- Time: `O(N * M)` memoized states, with up to constant work per state apart from the terminal suffix check.
- Space: `O(N * M)` cache plus recursion stack.

---

# 35. DP Pattern 23 – Maximum Rectangle with All 1s

Problem:

Binary matrix diya hai. Maximum area of rectangle containing only 1s find karo.

Example:

```python
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
```

This problem combines:
- Dynamic Programming.
- Histogram.
- Monotonic Stack.

### Main Idea

Har row ko histogram ki tarah treat karo.

For every row:
1. If current cell is `1`, increase previous height.
2. If current cell is `0`, reset height to zero.
3. Calculate largest rectangle in the histogram.

### Python Code

```python
def largestRectangleArea(heights):

    stack = []
    answer = 0

    for i in range(len(heights) + 1):

        current = heights[i] if i < len(heights) else 0

        while stack and heights[stack[-1]] > current:

            height = heights[stack.pop()]

            left = stack[-1] if stack else -1

            width = i - left - 1

            answer = max(answer, height * width)

        stack.append(i)

    return answer


def maximalRectangle(matrix):

    if not matrix:
        return 0

    cols = len(matrix[0])

    heights = [0] * cols

    answer = 0

    for row in matrix:

        for j in range(cols):

            if row[j] == "1":
                heights[j] += 1
            else:
                heights[j] = 0

        answer = max(
            answer,
            largestRectangleArea(heights)
        )

    return answer
```

Complexity:
- Time: `O(R * C)`
- Space: `O(C)`

---

# 36. Other Important DP Topics to Cover

Love Babbar's DP series includes several more problem variations. Inke patterns ko bhi practice karna hai.

## Knapsack and Subset DP

- [ ] 0/1 Knapsack
- [ ] Unbounded Knapsack
- [ ] Subset Sum
- [ ] Equal Sum Partition
- [ ] Minimum Subset Sum Difference
- [ ] Count Subsets with Given Sum
- [ ] Target Sum
- [ ] Coin Change – Minimum Coins
- [ ] Coin Change – Number of Ways
- [ ] Rod Cutting

## Sequence DP

- [ ] Longest Increasing Subsequence
- [ ] Longest Arithmetic Subsequence
- [ ] Longest Arithmetic Subsequence with Given Difference
- [ ] Maximum Sum Increasing Subsequence
- [ ] Russian Doll Envelopes
- [ ] Number of Longest Increasing Subsequences

## String DP

- [ ] Longest Common Subsequence
- [ ] Longest Palindromic Subsequence
- [ ] Longest Common Substring
- [ ] Edit Distance
- [ ] Minimum Insertions to Make String Palindrome
- [ ] Wildcard Pattern Matching
- [ ] Distinct Subsequences

## Stock DP

- [ ] Best Time to Buy and Sell Stock I
- [ ] Best Time to Buy and Sell Stock II
- [ ] Best Time to Buy and Sell Stock III
- [ ] Best Time to Buy and Sell Stock IV
- [ ] Best Time to Buy and Sell Stock with Cooldown
- [ ] Best Time to Buy and Sell Stock with Transaction Fee

## Other DP Problems

- [ ] Minimum Cost Climbing Stairs
- [ ] House Robber
- [ ] House Robber II
- [ ] Cut Rod into Segments
- [ ] Count Derangements
- [ ] Painting Fence Algorithm
- [ ] Unique Binary Search Trees
- [ ] Guess Number Higher or Lower II
- [ ] Minimum Cost Tree From Leaf Values
- [ ] Maximum Rectangle with All 1s

---

# 37. Important DP Patterns – Quick Reference

| Pattern | State | Common Problems |
|---|---|---|
| Fibonacci / Linear DP | `dp[i]` | Fibonacci, Climbing Stairs |
| Minimum / Maximum Cost | `dp[i]` | Minimum Cost Climbing Stairs |
| Include / Exclude | `dp[index]` | House Robber |
| Knapsack | `dp[index][capacity]` | 0/1 Knapsack |
| Subset Sum | `dp[index][target]` | Partition Equal Subset Sum |
| Coin Change | `dp[amount]` | Minimum Coins, Number of Ways |
| LIS | `dp[index]` | Longest Increasing Subsequence |
| LCS | `dp[i][j]` | Longest Common Subsequence |
| Stock DP | `dp[index][buy][limit]` | Buy and Sell Stock |
| Interval DP | `dp[left][right]` | Matrix Chain Multiplication |
| Tree DP | Depends on node/state | House Robber III |
| Bitmask DP | `dp[mask]` or `dp[mask][state]` | Assignment Problems |

---

# 38. More DP Concepts You Should Know

These are important extensions beyond the initial DP problems.

## 38.1 1D DP

One changing state.

```python
dp = [0] * n
```

Examples:
- Climbing Stairs.
- House Robber.
- LIS.

## 38.2 2D DP

Two changing states.

```python
dp = [[0] * m for _ in range(n)]
```

Examples:
- Knapsack.
- LCS.
- Edit Distance.

## 38.3 3D DP

Three changing states.

```python
dp = [
    [
        [0] * k
        for _ in range(m)
    ]
    for _ in range(n)
]
```

Examples:
- Stock with transaction limit.
- DP with index, state and remaining operations.

## 38.4 Grid DP

Problem matrix/grid ke cells par based hoti hai.

Examples:
- Unique Paths.
- Minimum Path Sum.
- Minimum Falling Path Sum.
- Maximal Square.

Typical state:

```python
dp[row][col]
```

## 38.5 Interval DP

Ek range `[left, right]` ko solve karte hain.

Examples:
- Matrix Chain Multiplication.
- Burst Balloons.
- Minimum Cost to Cut a Stick.
- Minimum Cost Tree From Leaf Values.

Typical state:

```python
dp[left][right]
```

## 38.6 Tree DP

Tree ke har node par states calculate hoti hain.

Examples:
- House Robber III.
- Diameter-related DP problems.
- Maximum Path Sum.

## 38.7 Bitmask DP

Jab subsets ya visited elements ko bitmask se represent karna useful ho.

Examples:
- Traveling Salesperson Problem.
- Assignment Problems.
- Small N subset optimization.

## 38.8 DP on DAG

Directed Acyclic Graph mein topological order ke through DP solve kar sakte hain.

Examples:
- Longest Path in DAG.
- Number of Ways in DAG.

## 38.9 Digit DP

Large numbers ke digits par constraints ke saath counting problems solve karte hain.

Typical state may include:

```text
position
tight
started
other constraints
```

Examples:
- Count numbers with a particular digit property.
- Count numbers within a range satisfying constraints.

---

# 39. Common DP Mistakes

## 1. State Correctly Define Nahi Karna

Agar state incomplete hai, toh DP answer wrong ho sakta hai.

## 2. Base Case Galat Hona

Base case smallest input ke liye manually verify karo.

## 3. Include / Exclude Confuse Karna

Check karo:
- Include karne ke baad next state kya hogi?
- Exclude karne ke baad next state kya hogi?

## 4. Wrong DP Array Size

Agar target `W` tak jaana hai, toh usually `W + 1` size chahiye.

## 5. Loop Direction Galat Hona

0/1 Knapsack mein reverse loop important hai.

Unbounded Knapsack mein forward loop important hai.

## 6. Wrong Initialization

- Counting problem: Often `dp[0] = 1`.
- Boolean subset problem: `dp[0] = True`.
- Minimum problem: Unreachable states often infinity.
- Maximum problem: Initial value depends on whether empty choices are allowed.

## 7. Confusing Minimum and Number of Ways

Minimum coins aur total combinations different recurrences hain.

## 8. Not Handling Impossible States

Impossible state ko `float("inf")`, `False`, ya appropriate sentinel se represent karo.

## 9. Wrong Transition Order

Tabulation mein required previous states pehle calculate hone chahiye.

## 10. Space Optimization Too Early

Pehle correct 2D ya 1D tabulation likho. Uske baad optimize karo.

## 11. Python List Aliasing

Wrong:

```python
dp = [[0] * 5] * 4
```

Ismein rows same list ko refer kar sakti hain.

Correct:

```python
dp = [[0] * 5 for _ in range(4)]
```

## 12. Forgetting Recursion Stack

Memoization mein DP array ke alawa recursion stack bhi memory use karta hai.

---

# 40. Python Tools Useful for DP

## List Initialization

```python
dp = [-1] * n
```

## 2D DP Initialization

```python
dp = [[-1] * m for _ in range(n)]
```

## Infinity

```python
float("inf")
```

## Negative Infinity

```python
float("-inf")
```

## Dictionary-Based Memoization

```python
from functools import lru_cache

@lru_cache(None)
def solve(index):
    pass
```

## Manual Memoization

```python
dp = {}

def solve(state):

    if state in dp:
        return dp[state]

    answer = calculate(state)

    dp[state] = answer

    return answer
```

**Note:** `lru_cache` is useful when states are tuples or multiple parameters. Its cache keys must be hashable.

---

# 41. DP Complexity Analysis

Let:
- `N` = number of elements.
- `W` = capacity or target.
- `M` = length of second string.

| Problem | Time | Space |
|---|---|---|
| Fibonacci with Memoization | `O(N)` | `O(N)` |
| Fibonacci Optimized | `O(N)` | `O(1)` |
| Climbing Stairs | `O(N)` | `O(1)` optimized |
| Minimum Coins | `O(N * Amount)` | `O(Amount)` |
| 0/1 Knapsack | `O(N * W)` | `O(W)` optimized |
| Subset Sum | `O(N * Target)` | `O(Target)` optimized |
| LIS Basic DP | `O(N²)` | `O(N)` |
| LIS Binary Search | `O(N log N)` | `O(N)` |
| LCS | `O(N * M)` | `O(N * M)` |
| Edit Distance | `O(N * M)` | `O(N * M)` |
| Stock with K Transactions | `O(N * K)` | `O(N * K)` memoized |

**Important:** Complexity depends on the exact implementation and state definition. Always count the number of states and the work performed per state.

---

# 42. Love Babbar DP Series – Learning Order

The following is the course-oriented progression to follow.

| Lecture | Topic |
|---|---|
| 102 | Introduction to DP, Memoization, Tabulation, Space Optimization |
| 103 | Minimum Cost Climbing Stairs |
| 104 | Minimum Number of Coins |
| 105 | Maximum Sum of Non-Adjacent Elements |
| 106 | House Robbery |
| 107 | Cut Rod into Segments X, Y, Z |
| 108 | Count Derangements |
| 109 | Painting Fence Algorithm |
| 110 | 0/1 Knapsack and 2D DP |
| 111 onward | Knapsack and related DP variations |
| Later lectures | LIS and sequence DP |
| Later lectures | Stock Buy and Sell variations |
| Later lectures | DP on Strings |
| Final DP lectures | LCS, Palindromic Subsequence, Edit Distance, Wildcard Matching |

The course sequence is a guide. Keep the official playlist open while following the lectures because video ordering or availability can change.

---

# 43. My DP Practice Strategy

For every important DP problem, I will follow this sequence:

```text
1. Understand the problem.
2. Identify the choices.
3. Write the recursive solution.
4. Identify the changing parameters.
5. Draw the recursion tree.
6. Identify overlapping subproblems.
7. Apply memoization.
8. Convert to tabulation.
9. Optimize space if possible.
10. Analyze TC and SC.
11. Solve the problem again without looking at notes.
```

### Practice Rule

Don't just watch the lecture and copy the code.

For every problem:
- First understand the intuition.
- Pause the video and try the recursive solution.
- Write memoization yourself.
- Convert it into tabulation.
- Try space optimization.
- Solve it again after a few days.

---

# 44. DP Completion Checklist

## Foundation

- [ ] Understand what DP is.
- [ ] Understand overlapping subproblems.
- [ ] Understand optimal substructure.
- [ ] Understand recursion tree.
- [ ] Understand state and recurrence relation.
- [ ] Understand memoization.
- [ ] Understand tabulation.
- [ ] Understand space optimization.

## 1D DP

- [ ] Fibonacci
- [ ] Climbing Stairs
- [ ] Minimum Cost Climbing Stairs
- [ ] Minimum Number of Coins
- [ ] Maximum Sum of Non-Adjacent Elements
- [ ] House Robber
- [ ] Cut Rod into Segments
- [ ] Count Derangements
- [ ] Painting Fence

## Knapsack and Subset DP

- [ ] 0/1 Knapsack
- [ ] Unbounded Knapsack
- [ ] Subset Sum
- [ ] Equal Sum Partition
- [ ] Minimum Subset Sum Difference
- [ ] Count Subsets with Given Sum
- [ ] Coin Change II
- [ ] Rod Cutting

## Sequence DP

- [ ] LIS
- [ ] Longest Arithmetic Subsequence
- [ ] Longest Arithmetic Subsequence with Given Difference
- [ ] Russian Doll Envelopes
- [ ] Number of LIS

## Stock DP

- [ ] Stock I
- [ ] Stock II
- [ ] Stock III
- [ ] Stock IV
- [ ] Stock with Cooldown
- [ ] Stock with Transaction Fee

## String DP

- [ ] LCS
- [ ] Longest Palindromic Subsequence
- [ ] Longest Common Substring
- [ ] Edit Distance
- [ ] Wildcard Matching
- [ ] Distinct Subsequences

## Advanced DP

- [ ] Grid DP
- [ ] Interval DP
- [ ] Tree DP
- [ ] Bitmask DP
- [ ] DP on DAG
- [ ] Digit DP

---

# 45. Final DP Revision Cheat Sheet

```text
DYNAMIC PROGRAMMING
        |
        |
        v
  Identify the State
        |
        v
   Write Base Case
        |
        v
 Write Recurrence Relation
        |
        v
      Recursion
        |
        v
    Memoization
   (Top-Down DP)
        |
        v
     Tabulation
   (Bottom-Up DP)
        |
        v
  Space Optimization
```

### Important Formulas

**Fibonacci**

\[
dp[i] = dp[i-1] + dp[i-2]
\]

**Climbing Stairs**

\[
dp[i] = dp[i-1] + dp[i-2]
\]

**Minimum Cost**

\[
dp[i] = cost[i] + min(dp[i-1],dp[i-2])
\]

**Non-Adjacent Maximum Sum**

\[
dp[i] = max(arr[i]+dp[i-2],dp[i-1])
\]

**0/1 Knapsack**

\[
dp[i][w] = max(
dp[i-1][w],
value[i]+dp[i-1][w-weight[i]]
)
\]

**LCS**

\[
dp[i][j] =
\begin{cases}
1+dp[i-1][j-1], & a[i-1]=b[j-1] \\
max(dp[i-1][j],dp[i][j-1]), & otherwise
\end{cases}
\]

---

# 46. Final Takeaway

DP ko directly memorize mat karna.

Har problem mein pehle ye samjho:

1. Problem ko smaller subproblems mein kaise divide kar sakte hain?
2. Kaunse parameters state define kar rahe hain?
3. Base case kya hoga?
4. Current answer previous states se kaise calculate hoga?
5. Kya same state repeat ho rahi hai?
6. Kya memoization se repeated calculation avoid ho sakti hai?
7. Kya tabulation possible hai?
8. Kya space optimize ho sakta hai?

**My learning approach:** Pehle Love Babbar ke DP lectures complete karunga. Har problem ko Python mein recursion, memoization, tabulation aur space optimization ke through implement karunga. Uske baad topic-wise practice aur revision karunga.

**One-line takeaway:** Dynamic Programming ka core idea hai – *same subproblem ko baar-baar solve mat karo; ek baar solve karo, answer store karo aur reuse karo.*

---

## References

- [Love Babbar – Lecture 102: Introduction to Dynamic Programming](https://www.youtube.com/watch?v=PGsgv6nXhLw)
- [Love Babbar – CodeHelp YouTube Channel](https://www.youtube.com/@CodeHelp)
- [Love Babbar DP Series – Lecture Outline](https://www.classcentral.com/course/youtube-dp-series-by-babbar-513347)