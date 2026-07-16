# Check if a Stack is Sorted Using Recursion

## Problem Overview

Given a Stack, check whether its elements are sorted.

For this Stack:

```text
TOP
 ↓
50
40
30
20
10
```

Python representation:

```python
stack = [10, 20, 30, 40, 50]
```

The Stack is sorted because, when moving from the **top toward the bottom**, the elements are in decreasing order:

```text
50 > 40 > 30 > 20 > 10
```

The goal is to check this recursively.

---

# Approach — Recursion + Adjacent Element Comparison

The main idea is:

```text
Take the top element
        ↓
Compare it with the previous element
        ↓
If sorted
        ↓
Pass current element to recursion
        ↓
Check the remaining Stack
```

We compare two elements at a time:

```text
element1 → Previously processed element

element2 → Current Stack top
```

The required condition is:

```python
element2 < element1
```

If this condition is true, we continue checking the remaining Stack.

---

# Python Code

```python
def checkSorted(stack, element1):

    # Base Case:
    # If no elements are left,
    # the complete stack was sorted
    if len(stack) == 0:
        return True

    # Get the current top element
    element2 = stack[-1]

    # Remove it so recursion can process
    # the remaining stack
    stack.pop()

    # Check whether the current pair
    # follows the required sorted order
    if element2 < element1:
        return checkSorted(stack, element2)

    else:
        return False


stack = []

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

element1 = float('inf')

result = checkSorted(stack, element1)

print(result)
```

Output:

```text
True
```

---

# Understanding the Stack

The Stack is:

```python
[10, 20, 30, 40, 50]
```

Remember that in Python:

```text
[10, 20, 30, 40, 50]
 ↑                   ↑
Bottom              Top
```

So visually:

```text
TOP
 ↓
50
40
30
20
10
```

We need to verify:

```text
50 > 40 > 30 > 20 > 10
```

Since we process from top to bottom, our comparisons become:

```text
50 < infinity
40 < 50
30 < 40
20 < 30
10 < 20
```

If every comparison is true, the Stack is sorted.

---

# Why Do We Use Two Elements?

The function receives:

```python
element1
```

and finds:

```python
element2 = stack[-1]
```

Their roles are:

```text
element1
    ↓
Previously processed element


element2
    ↓
Current top element
```

After checking:

```python
element2 < element1
```

we pass:

```python
element2
```

as the new `element1`.

```python
return checkSorted(stack, element2)
```

This creates a chain of comparisons.

---

# Why Start With Infinity?

Initially:

```python
element1 = float('inf')
```

In Python:

```python
float('inf')
```

represents positive infinity.

Conceptually:

```text
∞
```

Every normal finite number is smaller than positive infinity.

Therefore:

```text
50 < ∞
```

is:

```text
True
```

This allows the first Stack element to pass the comparison naturally.

Without infinity, we would need special handling for the first element.

So infinity acts as a:

```text
Sentinel Value
```

The pattern is:

```text
Use a special initial value
        ↓
Avoid separate handling
for the first comparison
```

---

# Complete Dry Run

Initial Stack:

```text
[10, 20, 30, 40, 50]
```

Initial:

```text
element1 = ∞
```

---

## Recursive Call 1

Current:

```text
element1 = ∞
```

Top:

```text
element2 = 50
```

Compare:

```text
50 < ∞
```

Result:

```text
True
```

Remove `50`.

Stack:

```text
[10, 20, 30, 40]
```

Recursive call:

```python
checkSorted(stack, 50)
```

---

## Recursive Call 2

Now:

```text
element1 = 50
```

Top:

```text
element2 = 40
```

Compare:

```text
40 < 50
```

Result:

```text
True
```

Stack becomes:

```text
[10, 20, 30]
```

Recursive call:

```python
checkSorted(stack, 40)
```

---

## Recursive Call 3

```text
element1 = 40
element2 = 30
```

Check:

```text
30 < 40
```

True.

Continue:

```text
[10, 20]
```

---

## Recursive Call 4

```text
element1 = 30
element2 = 20
```

Check:

```text
20 < 30
```

True.

Continue:

```text
[10]
```

---

## Recursive Call 5

```text
element1 = 20
element2 = 10
```

Check:

```text
10 < 20
```

True.

Continue:

```text
[]
```

---

## Base Case

Now:

```python
len(stack) == 0
```

So:

```python
return True
```

The final answer becomes:

```text
True
```

---

# Recursive Flow

```text
check(∞)

50 < ∞
   ↓
check(50)

40 < 50
   ↓
check(40)

30 < 40
   ↓
check(30)

20 < 30
   ↓
check(20)

10 < 20
   ↓
check(10)

Stack Empty
   ↓
True
```

---

# What Happens If the Stack Is Not Sorted?

Suppose:

```python
stack = [10, 20, 50, 30, 40]
```

Visually:

```text
TOP
 ↓
40
30
50
20
10
```

The comparisons begin:

```text
40 < ∞
    ↓
True


30 < 40
    ↓
True


50 < 30
    ↓
False
```

As soon as this condition fails:

```python
if element2 < element1:
```

the function executes:

```python
return False
```

The recursion stops immediately.

This is called:

```text
Early Termination
```

There is no need to check the remaining elements because we already know the Stack is not sorted.

---

# Base Case

The base case is:

```python
if len(stack) == 0:
    return True
```

Why do we return `True`?

Because reaching an empty Stack means:

```text
Every previous comparison was valid
```

If any comparison had failed, the function would already have returned:

```text
False
```

Therefore:

```text
Reached Empty Stack
        ↓
No Invalid Pair Found
        ↓
Stack is Sorted
        ↓
True
```

---

# The Recursive Relation

The problem can be thought of as:

```text
Is current element correctly ordered
with the previous element?

        +

Is the remaining Stack sorted?
```

Conceptually:

```text
checkSorted(stack)
        ↓
Check Current Pair
        ↓
Check Smaller Stack
```

Every recursive call reduces the problem size by one element.

---

# Why Do We Pop the Element?

We do:

```python
stack.pop()
```

because recursion needs to access the next element below the current top.

Before:

```text
TOP
 ↓
50
40
30
20
10
```

Pop `50`:

```text
TOP
 ↓
40
30
20
10
```

Now recursion can compare:

```text
40
```

with:

```text
50
```

So the Stack itself is used to move deeper into the data.

---

# Important: This Function Changes the Original Stack

Your current code does:

```python
stack.pop()
```

but does not restore the removed elements.

Therefore, after checking a fully sorted Stack:

```python
stack = [10, 20, 30, 40, 50]
```

the Stack becomes:

```text
[]
```

because every element was popped.

So this solution:

```text
Checks the Stack
        +
Consumes the Stack
```

This may be acceptable depending on the problem requirements.

If the original Stack must remain unchanged, we need to restore elements while recursion returns.

---

# Version That Preserves the Original Stack

We can use recursion and backtracking:

```python
def checkSorted(stack, element1):

    if len(stack) == 0:
        return True

    element2 = stack.pop()

    if element2 < element1:
        result = checkSorted(stack, element2)
    else:
        result = False

    # Restore the element
    stack.append(element2)

    return result
```

Now:

```text
Pop
 ↓
Check Recursively
 ↓
Restore
```

The original Stack remains unchanged.

This introduces the familiar pattern:

```text
Pop → Recurse → Restore
```

---

# Strictly Sorted vs Duplicate Values

Your condition is:

```python
element2 < element1
```

This checks for a **strictly sorted** Stack.

For example:

```text
50
40
40
30
```

will return:

```text
False
```

because:

```text
40 < 40
```

is false.

If duplicate values should be allowed, use:

```python
element2 <= element1
```

Then:

```text
50
40
40
30
```

would be considered sorted.

The difference is:

```text
<

Strictly sorted


<=

Sorted with duplicates allowed
```

Always check the problem definition before choosing the comparison.

---

# Time Complexity

Every element is processed once.

For `n` elements:

```text
Time Complexity = O(n)
```

If the Stack is unsorted, the function may stop early.

But in the worst case:

```text
O(n)
```

---

# Space Complexity

The recursion depth can reach:

```text
n
```

Therefore, the recursive call stack uses:

```text
Space Complexity = O(n)
```

Even though we do not create another explicit Stack, recursion itself uses the:

```text
Call Stack
```

---

# Pattern Used

For your DSA pattern sheet:

```text
Recursion + Adjacent Comparison
```

A more descriptive version is:

```text
Pop → Compare → Recurse
```

The solution also uses:

```text
Sentinel Value
```

because of:

```python
float('inf')
```

So the complete pattern can be written as:

```text
Recursion + Adjacent Comparison + Sentinel
```

---

# Difference From Delete Middle Stack Pattern

In the previous recursive Stack pattern:

```text
Pop
 ↓
Recurse
 ↓
Restore
```

we used backtracking because the removed elements needed to be placed back.

In this current code:

```text
Compare
 ↓
Pop
 ↓
Recurse
```

there is no restoration.

Therefore:

```text
Delete Middle:

Pop → Recurse → Restore

Pattern:
Recursion + Backtracking


Check Sorted:

Compare → Pop → Recurse

Pattern:
Recursive Linear Check
```

This distinction is important.

Not every recursive Stack problem uses backtracking.

Backtracking is required when we need to restore or undo the changes made while going deeper.

---

# Key Learning

The main idea is:

```text
Remember Previous Element
        ↓
Look at Current Top
        ↓
Compare Both
        ↓
Remove Current Top
        ↓
Pass Current as Previous
        ↓
Repeat
```

The core recursive template is:

```python
def check(stack, previous):

    if not stack:
        return True

    current = stack[-1]
    stack.pop()

    if current < previous:
        return check(stack, current)

    return False
```

The most important concepts are:

```text
1. Recursion reduces the Stack one element at a time.

2. element1 remembers the previously processed element.

3. element2 represents the current top element.

4. float('inf') acts as a sentinel for the first comparison.

5. Returning True at the base case means every comparison succeeded.

6. Returning False immediately provides early termination.

7. The current implementation modifies the original Stack.

8. If the Stack must remain unchanged, use:

   Pop → Recurse → Restore

9. '<' checks strict ordering.

10. '<=' allows duplicate values.
```

The main mental model is:

```text
Current Pair Valid?
       │
       ├── No → False
       │
       └── Yes
             ↓
       Check Remaining Stack
```

This is a classic example of reducing a larger Stack problem into the same problem on a smaller Stack using recursion.
