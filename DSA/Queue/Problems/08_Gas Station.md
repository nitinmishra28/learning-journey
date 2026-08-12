# Gas Station

## Problem

You have two arrays:

```python
gas[i]
cost[i]
```

At station `i`:

* You receive `gas[i]` gas.
* You spend `cost[i]` gas to travel to the next station.

You need to find the **starting station index** from which you can complete the entire circular route exactly once.

If impossible, return:

```text
-1
```

### Example

```text
gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
```

Answer:

```text
3
```

Starting from station `3`:

```text
4 → 1 → 2 → 3 → 4 → 5 → 1
```

The complete circuit is possible.

---

# Pattern

```text
Greedy + Running Balance
```

---

# Main Idea

For every station, calculate:

```python
gas[i] - cost[i]
```

This tells us the **net gain/loss** at that station.

Maintain:

```python
balance
```

which represents the gas available while travelling from the current candidate start.

If:

```python
balance < 0
```

we cannot reach the next station from the current starting point.

So we discard the current start and try:

```python
start = i + 1
```

---

# Why Can We Skip All Stations Up To `i`?

This is the most important greedy idea.

Suppose we started at:

```text
start
```

and after reaching station `i`:

```text
balance < 0
```

That means the total gas collected from `start` through `i` was not enough to cover the total cost.

Now suppose we try any station between:

```text
start ... i
```

as the new starting point.

It cannot work either.

Why?

Because we already know that the complete segment from `start` to `i` has a deficit. Starting somewhere in the middle gives us **even less accumulated gas before reaching `i`**.

Therefore:

```text
If balance becomes negative at i,
all stations from start to i are impossible starts.
```

So we can safely jump to:

```python
start = i + 1
```

This is the key greedy step.

---

# Meaning of `balance`

```python
balance += gas[i] - cost[i]
```

`balance` represents:

> How much gas is left after travelling through the stations from the current `start` to `i`.

Example:

```text
gas  =  [4, 6]
cost =  [5, 3]
```

At station `0`:

```text
4 - 5 = -1
```

So:

```text
balance = -1
```

We cannot continue.

Therefore station `0` cannot be the answer.

---

# Why Reset `balance = 0`?

When the current start fails:

```python
if balance < 0:
    start = i + 1
    balance = 0
```

We are starting a completely new journey from `i + 1`.

So the previous balance is no longer relevant.

Therefore:

```python
balance = 0
```

---

# What is `deficit`?

When a candidate start fails, `balance` may be negative.

Example:

```text
balance = -5
```

This means we are short by `5` units of gas.

The code stores this shortage:

```python
deficit += abs(balance)
```

So:

```text
deficit = total gas shortage from failed segments
```

Then we check whether the successful segment's remaining gas can cover all previous shortages:

```python
balance - deficit >= 0
```

If yes, the chosen `start` can complete the circular journey.

---

# Important: `balance` vs `deficit`

Think of them separately:

```text
balance
↓
Gas left from the current candidate start.

deficit
↓
Gas shortage created by previous failed candidates.
```

At the end:

```python
balance - deficit
```

tells us whether the final candidate has enough extra gas to cover those earlier shortages.

---

# Code

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        start = 0
        balance = 0
        deficit = 0

        for i in range(len(gas)):

            # Net gas at current station
            balance += gas[i] - cost[i]

            # Current start cannot reach next station
            if balance < 0:
                deficit += abs(balance)

                # Try next station as starting point
                start = i + 1

                # Start fresh
                balance = 0

        # Current candidate must cover previous deficit
        if balance - deficit >= 0:
            return start

        return -1
```

---

# Dry Run

```text
gas  =  [1, 2, 3, 4, 5]
cost =  [3, 4, 5, 1, 2]
```

Calculate net:

```text
gas - cost

[ -2, -2, -2, +3, +3 ]
```

### Start = 0

Station `0`:

```text
balance = -2
```

Failed.

```text
deficit = 2
start = 1
balance = 0
```

---

Station `1`:

```text
balance = -2
```

Failed.

```text
deficit = 4
start = 2
balance = 0
```

---

Station `2`:

```text
balance = -2
```

Failed.

```text
deficit = 6
start = 3
balance = 0
```

---

Station `3`:

```text
balance = 3
```

---

Station `4`:

```text
balance = 6
```

At the end:

```text
balance = 6
deficit = 6
```

Therefore:

```text
balance - deficit
= 6 - 6
= 0
```

So:

```text
answer = 3
```

---

# Important Global Condition

A solution is possible only if:

```text
Total Gas >= Total Cost
```

Because the car needs enough total gas to complete the complete circular journey.

If:

```text
sum(gas) < sum(cost)
```

then:

```text
answer = -1
```

No starting position can fix a global shortage.

---

# Alternative Standard Solution

The same greedy idea can be written more simply by using the total balance.

```python
class Solution:
    def canCompleteCircuit(self, gas, cost):

        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):

            gain = gas[i] - cost[i]

            total += gain
            tank += gain

            if tank < 0:
                start = i + 1
                tank = 0

        if total >= 0:
            return start

        return -1
```

This version is usually easier to remember.

### Difference

Your version explicitly tracks:

```text
balance + deficit
```

The standard version tracks:

```text
total + tank
```

Both are based on the same greedy observation.

---

# Common Mistakes

### 1. Trying Every Starting Point

Brute force:

```text
Try station 0
Try station 1
Try station 2
...
```

can take:

```text
O(n²)
```

The greedy approach finds the answer in:

```text
O(n)
```

---

### 2. Only Checking Local Balance

Seeing:

```text
gas[i] < cost[i]
```

doesn't necessarily mean station `i` cannot be part of the answer.

What matters is the **running balance from the candidate start**.

---

### 3. Forgetting the Circular Nature

After the last station:

```text
n - 1
```

we return to:

```text
0
```

The algorithm handles this implicitly through the total balance and candidate start.

---

### 4. Forgetting the Global Check

Even if a candidate survives the forward traversal, we still need:

```text
Total Gas >= Total Cost
```

Otherwise no solution exists.

---

# Complexity

```text
Time  → O(n)
Space → O(1)
```

We traverse the arrays only once and use constant extra space.

---

# Pattern Recognition

When you see:

```text
Circular route
+
Gain/Loss at every position
+
Find a valid starting point
```

think:

```text
Greedy + Running Balance
```

The key condition is:

```text
If running balance < 0
→ current start fails
→ skip all positions up to i
→ start = i + 1
```

---

# Revision Cheat Sheet

```text
Gas Station

Pattern:
Greedy + Running Balance

Net Gain:
gas[i] - cost[i]

balance:
Current candidate's remaining gas.

If:
balance < 0

Then:
Current start fails.

Do:
start = i + 1
balance = 0

Why can we skip all previous stations?
If start → i already has a deficit,
starting anywhere between them cannot
have enough gas to reach i either.

Global condition:
sum(gas) >= sum(cost)

If not:
return -1

Complexity:
Time  → O(n)
Space → O(1)
```

## One-Line Pattern

```text
Running balance becomes negative → discard all starts up to i → start from i+1 → final total balance decides whether a solution exists.
```
