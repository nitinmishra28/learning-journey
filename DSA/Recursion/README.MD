# Recursion – Complete DSA Notes

My personal notes for learning **Recursion from basic to advanced**, following the problem-solving approach used in Love Babbar's DSA course.

The goal is to understand recursion deeply, learn how to break problems into smaller subproblems, solve recursive problems independently, and build a strong foundation for **Dynamic Programming (DP)**.

---

## 1. What is Recursion?

Recursion is a programming technique in which a function calls itself to solve a smaller version of the same problem.

Instead of solving the entire problem at once, we divide it into smaller subproblems until we reach a condition where the answer is already known.

### Example: Factorial

Factorial of a number:

\[
5! = 5 \times 4 \times 3 \times 2 \times 1 = 120
\]

Mathematically:

\[
n! = n \times (n-1)!
\]

Base condition:

\[
0! = 1
\]

Python implementation:

```python
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(5))  # 120
```

Here:
- `factorial(5)` calls `factorial(4)`.
- `factorial(4)` calls `factorial(3)`.
- This continues until `factorial(0)`.
- Once the base condition is reached, the function calls return their results.

---

## 2. Three Important Parts of Recursion

Every recursive solution should have three important components.

### 1. Base Case

The condition that stops recursion.

Without a base case, the function keeps calling itself until Python raises a `RecursionError`.

```python
if n == 0:
    return
```

### 2. Recursive Relation

The part where a function calls itself with a smaller or simpler input.

```python
return n * factorial(n - 1)
```

### 3. Progress Toward the Base Case

Every recursive call must move closer to the base condition.

For example:

```python
factorial(n - 1)
```

Here, `n` decreases by one on every call.

**Remember:**

- Base case stops recursion.
- Recursive relation breaks the problem into smaller problems.
- Progress ensures that recursion eventually terminates.

---

## 3. How Recursion Works Internally – Call Stack

Whenever a function is called, Python creates a stack frame containing information such as local variables and the function's execution state.

When a function calls itself:
1. The current function pauses.
2. A new function call is added to the call stack.
3. This continues until the base case is reached.
4. Functions start returning in reverse order.

This behavior follows **LIFO – Last In, First Out**.

### Example

```python
def print_number(n):
    if n == 0:
        return

    print(n)
    print_number(n - 1)

print_number(3)
```

Output:

```text
3
2
1
```

### Recursive Call Flow

```text
print_number(3)
    |
    v
print_number(2)
    |
    v
print_number(1)
    |
    v
print_number(0)  <-- Base case
```

### Return Flow

```text
print_number(0) returns
    |
    v
print_number(1) returns
    |
    v
print_number(2) returns
    |
    v
print_number(3) returns
```

### Important Concept

The recursive calls go deeper into the call stack, and the return process moves back through the previous calls.

This is why recursion is often explained in two phases:

- **Going down:** Recursive calls are made.
- **Coming back:** Previous function calls resume and execute remaining statements.

---

## 4. Recursion – Before and After the Recursive Call

The position of the recursive call matters.

### A. Work Before Recursive Call

```python
def print_increasing(n):
    if n == 0:
        return

    print(n)
    print_increasing(n - 1)

print_increasing(5)
```

Output:

```text
5
4
3
2
1
```

Printing happens while recursion goes deeper.

### B. Work After Recursive Call

```python
def print_decreasing(n):
    if n == 0:
        return

    print_decreasing(n - 1)
    print(n)

print_decreasing(5)
```

Output:

```text
1
2
3
4
5
```

Printing happens while recursive calls return.

### Difference

| Before recursive call | After recursive call |
|---|---|
| Work happens while going deeper | Work happens while returning |
| Prints in decreasing order | Prints in increasing order |
| Executes before the next recursive call | Executes after the recursive call returns |

This concept is useful in problems involving arrays, strings, backtracking, and tree traversal.

---

## 5. Types of Recursion

### A. Direct Recursion

A function directly calls itself.

```python
def solve(n):
    if n == 0:
        return

    solve(n - 1)
```

### B. Indirect Recursion

One function calls another function, which eventually calls the first function.

```python
def function_a(n):
    if n <= 0:
        return

    print("A", n)
    function_b(n - 1)


def function_b(n):
    if n <= 0:
        return

    print("B", n)
    function_a(n - 1)
```

### C. Tail Recursion

The recursive call is the last operation performed by the function.

```python
def print_numbers(n):
    if n == 0:
        return

    print(n)
    print_numbers(n - 1)
```

### D. Non-Tail Recursion

Some work remains after the recursive call returns.

```python
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)
```

Python does not perform tail-call optimization, so tail recursion does not automatically eliminate stack usage.

---

# 6. How to Approach Any Recursion Problem

Follow this approach whenever you solve a recursion problem.

### Step 1: Identify the Smaller Problem

Ask yourself:

Can I solve this problem using the solution of a smaller input?

Example:

\[
factorial(n) = n \times factorial(n-1)
\]

### Step 2: Identify the Base Case

Ask:

When can I directly return the answer without making another recursive call?

Example:

```python
if n == 0:
    return 1
```

### Step 3: Find the Recursive Relation

Determine how the current problem depends on a smaller problem.

Example:

```python
return n * factorial(n - 1)
```

### Step 4: Trust the Recursive Call

Assume that the recursive function correctly solves the smaller problem.

Your responsibility is to:
- Make the recursive call correctly.
- Use its result.
- Return the answer for the current problem.

### Step 5: Dry Run

Trace the function with a small input.

### Step 6: Analyze Complexity

Calculate:
- Time complexity.
- Auxiliary space complexity.
- Recursion stack space.

**Important:** Do not try to manually solve every recursive call. Understand the smaller problem and trust the recursive function to solve it.

---

# 7. Basic Recursion Problems

These problems help build the foundation of recursion.

## 7.1 Print Numbers from 1 to N

```python
def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n)

print_numbers(5)
```

Output:

```text
1
2
3
4
5
```

**Concept:** Printing after the recursive call.

Complexity:
- Time: `O(N)`
- Auxiliary Space: `O(N)`

## 7.2 Print Numbers from N to 1

```python
def print_numbers(n):
    if n == 0:
        return

    print(n)
    print_numbers(n - 1)

print_numbers(5)
```

Output:

```text
5
4
3
2
1
```

**Concept:** Printing before the recursive call.

Complexity:
- Time: `O(N)`
- Auxiliary Space: `O(N)`

## 7.3 Sum of First N Natural Numbers

Formula:

\[
Sum(n) = n + Sum(n-1)
\]

```python
def sum_n(n):
    if n == 0:
        return 0

    return n + sum_n(n - 1)

print(sum_n(5))  # 15
```

Complexity:
- Time: `O(N)`
- Auxiliary Space: `O(N)`

## 7.4 Factorial of N

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))  # 120
```

Complexity:
- Time: `O(N)`
- Auxiliary Space: `O(N)`

## 7.5 Power of a Number

Calculate:

\[
a^b = a \times a^{b-1}
\]

```python
def power(a, b):
    if b == 0:
        return 1

    return a * power(a, b - 1)

print(power(2, 5))  # 32
```

Complexity:
- Time: `O(B)`
- Auxiliary Space: `O(B)`

## 7.6 Fibonacci Number

Fibonacci sequence:

```text
0, 1, 1, 2, 3, 5, 8, 13...
```

Mathematical relation:

\[
F(n) = F(n-1) + F(n-2)
\]

Base cases:

\[
F(0)=0,\quad F(1)=1
\]

```python
def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))  # 5
```

Complexity:
- Time: `O(2^N)` as a common upper-bound estimate.
- Auxiliary Space: `O(N)` recursion stack.

**Important:** Fibonacci is the first important example of overlapping subproblems. The same values are calculated multiple times. This leads directly to Dynamic Programming.

---

# 8. Recursion with Arrays

Array problems teach how to use recursion with indexes instead of modifying the entire array.

## 8.1 Print Array Elements

```python
def print_array(arr, index):
    if index == len(arr):
        return

    print(arr[index])
    print_array(arr, index + 1)

arr = [10, 20, 30, 40]
print_array(arr, 0)
```

Complexity:
- Time: `O(N)`
- Auxiliary Space: `O(N)`

## 8.2 Find Sum of Array Elements

```python
def array_sum(arr, index):
    if index == len(arr):
        return 0

    return arr[index] + array_sum(arr, index + 1)

arr = [1, 2, 3, 4, 5]
print(array_sum(arr, 0))  # 15
```

Complexity:
- Time: `O(N)`
- Auxiliary Space: `O(N)`

## 8.3 Find Maximum Element

```python
def find_max(arr, index):
    if index == len(arr) - 1:
        return arr[index]

    return max(arr[index], find_max(arr, index + 1))

arr = [10, 50, 20, 80, 30]
print(find_max(arr, 0))  # 80
```

Complexity:
- Time: `O(N)`
- Auxiliary Space: `O(N)`

## 8.4 Check Whether Array Is Sorted

```python
def is_sorted(arr, index):
    if index == len(arr) - 1:
        return True

    if arr[index] > arr[index + 1]:
        return False

    return is_sorted(arr, index + 1)

arr = [1, 2, 3, 4, 5]
print(is_sorted(arr, 0))  # True
```

Complexity:
- Time: `O(N)`
- Auxiliary Space: `O(N)`

## 8.5 Linear Search Using Recursion

```python
def linear_search(arr, target, index):
    if index == len(arr):
        return False

    if arr[index] == target:
        return True

    return linear_search(arr, target, index + 1)

arr = [10, 20, 30, 40]
print(linear_search(arr, 30, 0))  # True
```

Complexity:
- Time: `O(N)`
- Auxiliary Space: `O(N)`

## 8.6 Binary Search Using Recursion

Binary search works on a sorted array.

```python
def binary_search(arr, target, start, end):
    if start > end:
        return -1

    mid = start + (end - start) // 2

    if arr[mid] == target:
        return mid

    if target < arr[mid]:
        return binary_search(arr, target, start, mid - 1)

    return binary_search(arr, target, mid + 1, end)

arr = [10, 20, 30, 40, 50]
print(binary_search(arr, 40, 0, len(arr) - 1))  # 3
```

Complexity:
- Time: `O(log N)`
- Auxiliary Space: `O(log N)`

---

# 9. Recursion on Strings

String problems help understand how recursion processes characters one by one.

## 9.1 Reverse a String

```python
def reverse_string(s):
    if len(s) == 0:
        return ""

    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))  # olleh
```

Complexity:
- Time: `O(N^2)` for this slicing and concatenation approach.
- Auxiliary Space: `O(N)` recursion depth, with additional string allocations.

## 9.2 Check Palindrome

```python
def is_palindrome(s, start, end):
    if start >= end:
        return True

    if s[start] != s[end]:
        return False

    return is_palindrome(s, start + 1, end - 1)

s = "madam"
print(is_palindrome(s, 0, len(s) - 1))  # True
```

Complexity:
- Time: `O(N)`
- Auxiliary Space: `O(N)`

## 9.3 Remove a Character from String

Example: Remove all occurrences of `"a"`.

```python
def remove_char(s, target):
    if len(s) == 0:
        return ""

    if s[0] == target:
        return remove_char(s[1:], target)

    return s[0] + remove_char(s[1:], target)

print(remove_char("banana", "a"))  # bnn
```

Complexity:
- Time: `O(N^2)` in the worst case because slicing and concatenation create new strings.
- Auxiliary Space: `O(N)` recursion depth, excluding temporary string allocations.

---

# 10. Recursion Tree

A recursion tree is a visual representation of recursive function calls.

It is especially important for understanding:
- Multiple recursive calls.
- Fibonacci.
- Subsets.
- Subsequences.
- Permutations.
- Backtracking.
- Dynamic Programming.

### Example: Fibonacci(4)

```text
                 fib(4)
                /      \
            fib(3)     fib(2)
            /   \       /   \
        fib(2) fib(1) fib(1) fib(0)
         /  \
     fib(1) fib(0)
```

Notice that `fib(2)` is calculated more than once.

This is called **overlapping subproblems**.

The same subproblem gets solved repeatedly, which wastes time.

Dynamic Programming solves this issue by storing previously calculated results.

---

# 11. Multiple Recursive Calls

Until now, most examples used one recursive call.

Some problems require multiple recursive calls.

Example:

```python
def fibonacci(n):
    if n <= 1:
        return n

    left = fibonacci(n - 1)
    right = fibonacci(n - 2)

    return left + right
```

Here:
- First recursive call solves one subproblem.
- Second recursive call solves another subproblem.
- Their results are combined.

This pattern is important for:
- Fibonacci.
- Climbing Stairs.
- House Robber.
- Unique Paths.
- Subset Sum.
- Knapsack.
- Many DP problems.

**Remember:** Multiple recursive calls do not automatically mean DP. DP becomes useful when the problem has overlapping subproblems and suitable optimal substructure.

---

# 12. Recursion and Backtracking

Backtracking is an extension of recursion.

In normal recursion, we solve smaller subproblems.

In backtracking, we:
1. Make a choice.
2. Explore the choice recursively.
3. Undo the choice.
4. Explore another possibility.

The common structure is:

```python
def solve():
    if base_condition:
        return

    for choice in choices:
        # Make a choice
        apply(choice)

        # Explore
        solve()

        # Undo the choice
        undo(choice)
```

### Example: Generate All Subsequences

```python
def subsequences(index, arr, current):
    if index == len(arr):
        print(current)
        return

    # Include current element
    current.append(arr[index])
    subsequences(index + 1, arr, current)

    # Backtrack
    current.pop()

    # Exclude current element
    subsequences(index + 1, arr, current)


arr = [1, 2, 3]
subsequences(0, arr, [])
```

Output:

```text
[1, 2, 3]
[1, 2]
[1, 3]
[1]
[2, 3]
[2]
[3]
[]
```

Each element has two choices:
- Include.
- Exclude.

Therefore, the total number of subsequences is:

\[
2^N
\]

Complexity:
- Time: `O(N * 2^N)` including the cost of constructing/printing each subsequence.
- Auxiliary Space: `O(N)` for recursion depth and the current subsequence, excluding output storage.

### Important Backtracking Problems

- Subsequences.
- Subsets.
- Permutations.
- Combination Sum.
- Rat in a Maze.
- N-Queens.
- Sudoku Solver.

---

# 13. Recursion Patterns You Must Understand Before DP

These patterns are especially important because many DP problems are first solved using recursion.

## Pattern 1: Single Recursive Call

The current problem depends on one smaller subproblem.

Examples:
- Factorial.
- Sum of N numbers.
- Array traversal.
- Reverse string.

General structure:

```python
def solve(n):
    if base_case:
        return answer

    return current_work + solve(smaller_input)
```

## Pattern 2: Two Recursive Calls

The current problem depends on two smaller subproblems.

Examples:
- Fibonacci.
- Climbing Stairs.
- Some tree problems.

General structure:

```python
def solve(n):
    if base_case:
        return answer

    left = solve(smaller_problem_1)
    right = solve(smaller_problem_2)

    return combine(left, right)
```

## Pattern 3: Multiple Choices / Include-Exclude

At every position, we have multiple choices.

Examples:
- Subsequences.
- Subsets.
- Subset Sum.
- 0/1 Knapsack.

General structure:

```python
def solve(index):
    if base_case:
        return answer

    include = solve(next_index)
    exclude = solve(next_index)

    return combine(include, exclude)
```

## Pattern 4: Try All Possible Choices

At every step, explore all valid choices.

Examples:
- Permutations.
- Combination Sum.
- N-Queens.
- Rat in a Maze.

General structure:

```python
def solve(state):
    if base_case:
        return

    for choice in choices:
        if is_valid(choice):
            make_choice(choice)
            solve(updated_state)
            undo_choice(choice)
```

## Pattern 5: Recursion with Index and State

The recursive function carries additional information.

Examples:
- Knapsack.
- Subset Sum.
- Coin Change.
- Target Sum.

```python
def solve(index, target):
    if base_case:
        return answer

    # Explore choices using index and target
```

This pattern is particularly important for Dynamic Programming because the function parameters often become DP state variables.

---

# 14. Introduction to Dynamic Programming – Why Do We Need It?

Dynamic Programming is an optimization technique used to avoid solving the same subproblem repeatedly.

Consider Fibonacci:

```python
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)
```

For `fib(5)`, the same smaller Fibonacci values are calculated repeatedly.

This creates unnecessary work.

Dynamic Programming stores the result of a subproblem so that it can be reused.

### Two Important Properties of DP

#### 1. Overlapping Subproblems

The same subproblem is calculated multiple times.

Example:

```text
fib(5)
 ├── fib(4)
 │    ├── fib(3)
 │    └── fib(2)
 └── fib(3)
      ├── fib(2)
      └── fib(1)
```

`fib(3)` and `fib(2)` are repeated.

#### 2. Optimal Substructure

The optimal solution to a larger problem can be constructed using optimal solutions to smaller subproblems.

This property is important in optimization problems such as:
- Knapsack.
- Minimum Cost.
- Shortest Path.
- Longest Common Subsequence.

Not every recursive problem is a DP problem.

---

# 15. Two Approaches to Dynamic Programming

## A. Memoization – Top-Down DP

Memoization means storing the results of recursive calls.

We start with recursion and add a cache.

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

How it works:
1. Call the recursive function.
2. Check whether the answer is already stored.
3. If stored, return it.
4. Otherwise, calculate the answer.
5. Store the answer.
6. Return the result.

Complexity:
- Time: `O(N)`
- Auxiliary Space: `O(N)` for the DP array and recursion stack.

## B. Tabulation – Bottom-Up DP

Tabulation solves smaller subproblems first and builds toward the final answer.

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

How it works:
1. Create a DP array.
2. Initialize the base cases.
3. Calculate answers from smaller states to larger states.
4. Return the final state.

Complexity:
- Time: `O(N)`
- Space: `O(N)`

### Memoization vs Tabulation

| Memoization | Tabulation |
|---|---|
| Top-down approach | Bottom-up approach |
| Uses recursion | Usually uses iteration |
| Calculates states when needed | Calculates states in an order |
| Uses recursion stack | No recursion stack |
| Can avoid unused states | May calculate unused states |

---

# 16. Space Optimization in DP

Sometimes we do not need the entire DP array.

For Fibonacci, we only need the previous two values.

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

Complexity:
- Time: `O(N)`
- Space: `O(1)`

This is called **Space Optimization**.

---

# 17. How to Convert Recursion into DP

Follow this process when solving a DP problem.

### Step 1: Write the Recursive Solution

Understand how the problem can be broken into smaller subproblems.

### Step 2: Identify the Changing Parameters

Check which parameters define a subproblem.

For example:

```python
solve(index, target)
```

Here, `index` and `target` may define the state.

### Step 3: Check for Overlapping Subproblems

Draw the recursion tree.

If the same state appears multiple times, memoization may help.

### Step 4: Create a DP Structure

For two changing parameters, you may need a 2D DP array.

Example:

```python
dp = [[-1] * (target + 1) for _ in range(n + 1)]
```

### Step 5: Add Memoization

Before calculating a state, check whether its result is already stored.

### Step 6: Convert to Tabulation

Identify:
- Base cases.
- State transitions.
- Correct order of calculation.

### Step 7: Optimize Space

Check whether all previously calculated states are actually required.

---

# 18. Recursion vs Backtracking vs Dynamic Programming

| Concept | Purpose | Main Idea |
|---|---|---|
| Recursion | Solve smaller versions of a problem | Function calls itself |
| Backtracking | Explore different possible choices | Choose, explore, undo |
| Dynamic Programming | Avoid repeated calculations | Store and reuse results |

### Important Differences

- Recursion is a problem-solving technique.
- Backtracking uses recursion to explore possibilities.
- Dynamic Programming uses stored subproblem results to avoid repeated work.
- A problem can use recursion without requiring DP.
- Backtracking problems do not automatically become DP problems.
- Some problems can be solved using both backtracking and DP, depending on whether states overlap and what result is required.

---

# 19. Common Recursion Mistakes

### 1. Missing Base Case

Incorrect:

```python
def solve(n):
    return solve(n - 1)
```

There is no stopping condition.

### 2. Incorrect Base Case

The base case may stop too early or return the wrong value.

Always verify the smallest valid input.

### 3. Not Moving Toward the Base Case

Incorrect:

```python
def solve(n):
    if n == 0:
        return

    solve(n)
```

The input never changes.

### 4. Forgetting to Return the Recursive Result

Incorrect:

```python
def factorial(n):
    if n == 0:
        return 1

    factorial(n - 1)
```

Correct:

```python
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)
```

### 5. Confusing Work Before and After Recursion

Remember that statements after the recursive call execute when the function returns.

### 6. Incorrectly Handling Mutable Data

When using lists for backtracking, undo the changes after exploring a choice.

```python
current.append(value)
solve()
current.pop()
```

### 7. Ignoring Repeated Subproblems

A recursive solution may be correct but very slow.

Draw the recursion tree to identify overlapping subproblems.

### 8. Ignoring Recursion Stack Space

Recursive calls consume memory even when no extra data structure is created.

### 9. Using Slicing Without Considering Its Cost

Operations like `arr[1:]` and `s[1:]` create new objects in Python.

Prefer index-based recursion when appropriate.

### 10. Assuming Every Recursive Problem Needs DP

DP is useful when there are overlapping subproblems and the problem supports reusing their results.

---

# 20. Recursion Complexity Cheat Sheet

Let:
- `N` = input size.
- `H` = maximum recursion depth.
- `B` = number of branches per recursive call.

| Pattern | Typical Time | Stack Space |
|---|---|---|
| One call with N decreasing by 1 | `O(N)` | `O(N)` |
| Binary search recursion | `O(log N)` | `O(log N)` |
| Fibonacci naive recursion | `O(2^N)` upper bound | `O(N)` |
| Generate all subsets | `O(N * 2^N)` including output | `O(N)` |
| Generate all permutations | `O(N * N!)` including output | `O(N)` |

**Important:** These are common patterns, not universal formulas. Always analyze the number of calls, work performed in each call, and maximum recursion depth.

---

# 21. Recommended Recursion Practice Order

Complete these patterns in order before moving deeply into DP.

## Level 1 – Recursion Basics

- [ ] Print numbers from 1 to N
- [ ] Print numbers from N to 1
- [ ] Sum of first N natural numbers
- [ ] Factorial of a number
- [ ] Power of a number
- [ ] Fibonacci number
- [ ] Understand call stack
- [ ] Draw recursion trees

## Level 2 – Arrays

- [ ] Print array elements
- [ ] Find sum of array
- [ ] Find maximum element
- [ ] Check whether array is sorted
- [ ] Linear search
- [ ] Binary search using recursion

## Level 3 – Strings

- [ ] Reverse a string
- [ ] Check palindrome
- [ ] Remove a character
- [ ] Replace a character
- [ ] Remove duplicate characters
- [ ] Check whether a string is a subsequence of another

## Level 4 – Multiple Recursive Calls

- [ ] Fibonacci
- [ ] Climbing Stairs
- [ ] Understand recursion trees
- [ ] Identify overlapping subproblems

## Level 5 – Subsequences and Subsets

- [ ] Generate all subsequences
- [ ] Generate all subsets
- [ ] Subset Sum
- [ ] Count subsets with a given sum
- [ ] Check whether a subset with a target sum exists

## Level 6 – Backtracking

- [ ] Permutations
- [ ] Combination Sum
- [ ] Rat in a Maze
- [ ] N-Queens
- [ ] Sudoku Solver

## Level 7 – Recursion to DP Foundation

- [ ] Fibonacci using recursion
- [ ] Fibonacci using memoization
- [ ] Fibonacci using tabulation
- [ ] Fibonacci using space optimization
- [ ] Understand state and state transitions
- [ ] Understand overlapping subproblems
- [ ] Understand optimal substructure

---

# 22. Final Revision – Important Points

1. Every recursive function needs a correct base case.
2. Every recursive call should move toward the base case.
3. The call stack stores active function calls.
4. Statements before recursion execute while going deeper.
5. Statements after recursion execute while returning.
6. Multiple recursive calls can create a recursion tree.
7. Repeated states in a recursion tree indicate overlapping subproblems.
8. Backtracking follows choose, explore, and undo.
9. Memoization is top-down DP.
10. Tabulation is bottom-up DP.
11. Space optimization reduces unnecessary DP storage.
12. Always calculate recursion stack space separately from other auxiliary space.

---

# 23. Most Important DP Connection

Before starting DP, make sure you can answer these questions:

- Can I write the recursive solution?
- Can I identify the base cases?
- Can I identify the changing parameters?
- Can I draw the recursion tree?
- Can I identify overlapping subproblems?
- Can I define the DP state?
- Can I write the recurrence relation?
- Can I convert recursion into memoization?
- Can I convert memoization into tabulation?
- Can I optimize the DP space?

If you understand these concepts, learning DP becomes much easier.

**My learning strategy:** First become comfortable with recursion and backtracking. Then start DP by solving problems using recursion, memoization, tabulation, and finally space optimization.

---

## Quick Revision Formula

```text
RECURSION
   |
   |-- Base Case
   |
   |-- Recursive Relation
   |
   |-- Call Stack
   |
   |-- Recursion Tree
   |
   |-- Multiple Recursive Calls
   |
   |-- Include / Exclude
   |
   |-- Backtracking
   |
   v
DYNAMIC PROGRAMMING
   |
   |-- Overlapping Subproblems
   |
   |-- Optimal Substructure
   |
   |-- Memoization (Top-Down)
   |
   |-- Tabulation (Bottom-Up)
   |
   |-- Space Optimization
```

**One-line takeaway:** Recursion teaches you how to break a problem into smaller problems; backtracking teaches you how to explore choices; Dynamic Programming teaches you how to reuse solutions to repeated subproblems.