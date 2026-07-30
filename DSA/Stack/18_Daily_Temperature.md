# 739. Daily Temperatures

## Problem

Given an array `temperatures`, return an array `answer` where:

* `answer[i]` = number of days until a **warmer temperature**.
* If no warmer day exists, return `0` for that day.

Example

```text
Input : [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

---

# Brute Force

## Idea

For every day, check all future days until a warmer temperature is found.

## Code

```python
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n

        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break

        return ans
```

### Complexity

* **Time:** `O(n²)`
* **Space:** `O(1)` (excluding output array)

### Why is it slow?

Each day may scan all remaining days.

---

# Pattern

```text
Monotonic Decreasing Stack (Next Greater Element)
```

---

# Main Idea

* Store **indices** of temperatures in a stack.
* The stack maintains temperatures in **decreasing order**.
* When a warmer temperature arrives, it becomes the answer for all smaller temperatures waiting in the stack.
* Pop them, calculate the distance, and continue.

---

# Optimal Solution

```python
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)

        stack = []          # Stores indices
        ans = [0] * n

        for i in range(n):

            # Current temperature is warmer
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx

            stack.append(i)

        return ans
```

---

# Why This Works

The stack stores indices whose next warmer temperature hasn't been found yet.

Whenever a higher temperature appears:

* Pop all colder temperatures.
* Calculate their waiting days.
* Push the current index.

Each index is:

* **Pushed once**
* **Popped once**

Hence the algorithm is linear.

---

# Dry Run

Input

```text
[73,74,75,71,69,72,76,73]
```

| Day | Temp | Stack (Indices) | Answer          |
| --- | ---- | --------------- | --------------- |
| 0   | 73   | 0               | 0               |
| 1   | 74   | 1               | 1,0,0,0,0,0,0,0 |
| 2   | 75   | 2               | 1,1,0,0,0,0,0,0 |
| 3   | 71   | 2,3             |                 |
| 4   | 69   | 2,3,4           |                 |
| 5   | 72   | 2,5             | 1,1,0,2,1,0,0,0 |
| 6   | 76   | 6               | 1,1,4,2,1,1,0,0 |
| 7   | 73   | 6,7             | Final           |

Output

```text
[1,1,4,2,1,1,0,0]
```

---

# Why Store Indices Instead of Temperatures?

We need to calculate

```text
Days = Current Index - Previous Index
```

If we stored only temperatures,

```text
73
74
75
```

we wouldn't know **which day** they occurred.

Therefore we store

```text
Indices
```

and access temperatures using

```python
temperatures[stack[-1]]
```

---

# Common Mistakes

### 1. Storing temperatures instead of indices

❌ Wrong

```python
stack.append(temperatures[i])
```

✅ Correct

```python
stack.append(i)
```

---

### 2. Using `if` instead of `while`

❌ Wrong

```python
if stack and temperatures[i] > temperatures[stack[-1]]:
```

There may be multiple colder temperatures waiting.

Always use

```python
while
```

---

### 3. Forgetting to initialize the answer array

Initialize with

```python
ans = [0] * n
```

If no warmer day exists, the answer remains `0`.

---

### 4. Using `>=` instead of `>`

The problem asks for a **strictly warmer** temperature.

Correct condition:

```python
temperatures[i] > temperatures[stack[-1]]
```

---

# Complexity Comparison

| Approach        | Time      | Space    |
| --------------- | --------- | -------- |
| Brute Force     | **O(n²)** | **O(1)** |
| Monotonic Stack | **O(n)**  | **O(n)** |

---

# Pattern Recognition

Use this pattern when the question asks for:

* Next Greater Element
* Next Warmer Day
* Next Larger Value
* First Greater Element on Right
* Distance to Next Greater Element

Similar Problems

* Next Greater Element I
* Next Greater Element II
* Stock Span
* Online Stock Span
* Next Greater Node in Linked List

---

# Revision Cheat Sheet

```text
Pattern:
Monotonic Decreasing Stack (Next Greater Element)

Store:
Indices

Algorithm:
1. Traverse left to right.
2. While current temperature is greater:
      Pop index
      Answer = current_index - popped_index
3. Push current index.
4. Remaining indices have answer = 0.

Remember:
✔ Store indices, not values.
✔ Use while, not if.
✔ Stack remains decreasing.
✔ Every index is pushed and popped once.

Time:
O(n)

Space:
O(n)
```
