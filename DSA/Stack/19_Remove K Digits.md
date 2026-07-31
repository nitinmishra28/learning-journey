# 402. Remove K Digits

## Problem

Given a non-negative integer `num` represented as a string and an integer `k`, remove exactly `k` digits so that the remaining number is the **smallest possible**.

Return the result as a string.

### Examples

```text
Input : num = "1432219", k = 3
Output: "1219"

Input : num = "10200", k = 1
Output: "200"

Input : num = "10", k = 2
Output: "0"
```

---

# Brute Force

## Idea

The most straightforward approach is to try **every possible way** of removing exactly `k` digits.

For each possible combination:

1. Remove those digits.
2. Construct the remaining number.
3. Remove leading zeros.
4. Compare it with the smallest number found so far.

Finally, return the minimum number.

Although this always produces the correct answer, it is extremely slow because the number of possible combinations grows exponentially.

---

## Brute Force Code

```python
from itertools import combinations

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        n = len(num)
        smallest = None

        # Try every possible combination of k indices
        for remove_indices in combinations(range(n), k):

            remove_set = set(remove_indices)
            curr = []

            # Build remaining number
            for i in range(n):
                if i not in remove_set:
                    curr.append(num[i])

            # Convert into string
            candidate = "".join(curr).lstrip("0")

            if candidate == "":
                candidate = "0"

            # Keep the smallest number
            if smallest is None or int(candidate) < int(smallest):
                smallest = candidate

        return smallest
```

---

## Dry Run (Brute Force)

Input

```text
num = "1432219"
k = 3
```

Some possible removals are

| Removed Digits | Remaining Number |
| -------------- | ---------------- |
| 1,4,3          | 2219             |
| 4,3,2          | 1219 ✅           |
| 3,2,1          | 1429             |
| 1,2,9          | 4321             |
| ...            | ...              |

The algorithm checks **every combination** before deciding that

```text
1219
```

is the smallest.

---

## Complexity

* **Time:** `O(C(n,k) × n)`
* **Space:** `O(n)`

---

## Why is it Slow?

Suppose

```text
n = 30
k = 15
```

Then

```text
C(30,15) = 155,117,520
```

possible combinations exist.

For each combination we again rebuild the string.

Clearly this cannot pass LeetCode constraints.

---

# Pattern

```text
Monotonic Increasing Stack + Greedy
```

---

# Key Observation

To obtain the **smallest possible number**, larger digits should never appear before smaller digits if we still have removals left.

Example

```text
43
```

Keeping

```text
43
```

is always worse than

```text
34
```

So whenever we see

```text
Previous Digit > Current Digit
```

it is beneficial to remove the previous digit.

This is exactly what the greedy algorithm does.

---

# Main Idea

Maintain a stack representing the smallest number built so far.

For every digit:

* If the current digit is smaller than the stack top,
* and removals are still available,
* remove the larger digit.

Continue until the stack becomes increasing.

After traversal:

* If `k` is still remaining,
* remove digits from the end because the number is already increasing.

Finally:

* Join the stack.
* Remove leading zeros.
* If the result becomes empty, return `"0"`.

---

# Optimal Solution

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for ch in num:

            # Remove larger previous digits
            while stack and k > 0 and stack[-1] > ch:
                stack.pop()
                k -= 1

            stack.append(ch)

        # Remove remaining digits from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Remove leading zeros
        result = "".join(stack).lstrip("0")

        return result if result else "0"
```

---

# Intuition Behind the Stack

Suppose we process

```text
1432219
```

Initially

```text
Stack

1
```

Next digit

```text
4
```

Stack

```text
1 4
```

Now we encounter

```text
3
```

Since

```text
4 > 3
```

keeping

```text
143...
```

will always be larger than

```text
13...
```

So we remove **4** immediately.

The same logic continues throughout the traversal.

This greedy decision guarantees the smallest possible prefix at every step.




# Why This Greedy Approach Works

The greedy decision is:

> **Whenever the previous digit is larger than the current digit, remove the previous digit if `k > 0`.**

Why?

Suppose we have

```text
43
```

There are only two possible prefixes:

```text
43
34
```

Obviously,

```text
34 < 43
```

So keeping `4` before `3` can never produce the smallest number.

Therefore, removing the larger digit immediately is always the best choice.

The stack helps us undo previous decisions whenever a smaller digit appears.

---

# Why Remove Remaining Digits From the End?

Sometimes the stack never removes any digit.

Example

```text
num = "12345"
k = 2
```

The stack becomes

```text
1 2 3 4 5
```

Since the digits are already increasing,

```python
stack[-1] > current_digit
```

is never true.

But we still have to remove two digits.

Possible answers:

```text
345
234
123  ✅
```

Removing digits from the **end** always gives the smallest number because the leftmost digits have the highest significance.

That's why we do

```python
while k > 0:
    stack.pop()
    k -= 1
```

---

# Why Remove Leading Zeros?

Consider

```text
num = "10200"
k = 1
```

After processing,

Stack becomes

```text
0200
```

The answer should not be

```text
0200
```

It should be

```text
200
```

Hence,

```python
result = "".join(stack).lstrip("0")
```

removes all unnecessary leading zeros.

---

# Why Return "0" Instead of an Empty String?

Example

```text
num = "10"
k = 2
```

Both digits are removed.

Stack

```text
[]
```

Joined string

```text
""
```

After removing leading zeros,

```text
""
```

But according to the problem,

the smallest possible number is

```text
0
```

Therefore,

```python
return result if result else "0"
```

---

# Dry Run

Input

```text
num = "1432219"
k = 3
```

| Current Digit | Stack Before | Action        | Stack After | Remaining k |
| ------------- | ------------ | ------------- | ----------- | ----------: |
| 1             | []           | Push          | 1           |           3 |
| 4             | 1            | Push          | 1 4         |           3 |
| 3             | 1 4          | Pop 4, Push 3 | 1 3         |           2 |
| 2             | 1 3          | Pop 3, Push 2 | 1 2         |           1 |
| 2             | 1 2          | Push          | 1 2 2       |           1 |
| 1             | 1 2 2        | Pop 2, Push 1 | 1 2 1       |           0 |
| 9             | 1 2 1        | Push          | 1 2 1 9     |           0 |

Final Stack

```text
1 2 1 9
```

Result

```text
1219
```

---

# Common Mistakes

## 1. Using `if` Instead of `while`

❌ Wrong

```python
if stack and stack[-1] > ch:
    stack.pop()
```

A single digit may require removing **multiple larger digits**.

Example

```text
7654
```

When `4` arrives,

we should remove

```text
7
6
5
```

Hence always use

```python
while
```

---

## 2. Forgetting Remaining `k`

Example

```text
12345
k = 2
```

No digit gets removed during traversal.

Without

```python
while k > 0:
    stack.pop()
```

the answer becomes incorrect.

---

## 3. Forgetting Leading Zeros

Example

```text
10200
```

Returning

```text
0200
```

is wrong.

Correct answer

```text
200
```

---

## 4. Comparing Characters Incorrectly

This works because digits are characters.

```python
'8' > '3'
```

returns

```text
True
```

Since `'0'`–`'9'` follow increasing ASCII order, direct comparison is valid.

No integer conversion is needed.

---

## 5. Forgetting Empty Result

Example

```text
num = "9"
k = 1
```

Stack becomes empty.

Always return

```text
0
```

instead of

```text
""
```

---

# Complexity Comparison

| Approach                   | Time               | Space    |
| -------------------------- | ------------------ | -------- |
| Brute Force                | **O(C(n, k) × n)** | **O(n)** |
| Monotonic Increasing Stack | **O(n)**           | **O(n)** |

> **Why O(n)?**
>
> Every digit is **pushed exactly once** and **popped at most once**.
> Therefore, the total number of stack operations is linear.

---

# Pattern Recognition

This pattern is useful when:

* You must build the **smallest** or **largest** number.
* Previous choices may need to be undone.
* A better current element invalidates earlier decisions.
* The problem asks you to remove elements greedily.
* The answer depends on maintaining an increasing/decreasing order.

### Similar Problems

* 316. Remove Duplicate Letters
* 1673. Find the Most Competitive Subsequence
* 739. Daily Temperatures
* 901. Online Stock Span
* 496. Next Greater Element I
* 84. Largest Rectangle in Histogram

---

# Revision Cheat Sheet

```text
Problem:
Remove exactly k digits to make the smallest number.

Pattern:
Monotonic Increasing Stack + Greedy

Store:
Digits

Algorithm:
1. Traverse every digit.
2. While stack top > current digit and k > 0:
      Pop.
3. Push current digit.
4. Remove remaining digits from the end.
5. Join stack.
6. Remove leading zeros.
7. If empty → return "0".

Remember:
✔ Remove larger previous digits.
✔ Use while, not if.
✔ Remove remaining digits from the end.
✔ Strip leading zeros.
✔ Every digit is pushed once and popped at most once.

Time:
O(n)

Space:
O(n)
```
