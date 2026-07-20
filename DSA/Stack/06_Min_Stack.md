# Min Stack

## Problem

Design a Stack that supports all these operations:

```text
push()    → Add an element

pop()     → Remove the top element

top()     → Get the top element

getMin()  → Get the minimum element
```

The important requirement is that every operation should work in:

```text
O(1)
```

---

# Code with Comments

```python
class MinStack:

    def __init__(self):

        # Stores all elements normally
        self.stack = []

        # Stores the minimum elements
        # that are still active in the main stack
        self.min_stack = []


    def push(self, val: int) -> None:

        # Every value goes into the main stack
        self.stack.append(val)

        # Add value to min_stack only if:
        #
        # 1. min_stack is empty
        # OR
        # 2. val is smaller than or equal
        #    to the current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)


    def pop(self) -> None:

        # If the element being removed is also
        # the current minimum, remove it from
        # min_stack as well
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        # Remove from the main stack
        self.stack.pop()


    def top(self) -> int:

        # Top element of the normal stack
        return self.stack[-1]


    def getMin(self) -> int:

        # Top of min_stack always contains
        # the current minimum
        return self.min_stack[-1]
```

---

# Main Idea

We maintain two stacks:

```text
stack
↓
Stores every element


min_stack
↓
Stores minimum elements
```

The top of:

```text
min_stack
```

always represents the:

```text
Current Minimum
```

Therefore:

```python
getMin()
```

can simply return:

```python
self.min_stack[-1]
```

in:

```text
O(1)
```

---

# Why Do We Need Another Stack?

Suppose we only have:

```text
[5, 3, 7, 2, 6]
```

If someone asks:

```text
What is the minimum?
```

Without storing extra information, we would need to search:

```text
5 → 3 → 7 → 2 → 6
```

This takes:

```text
O(n)
```

But the problem requires:

```text
getMin() → O(1)
```

So we maintain the minimum information while inserting elements.

That is the purpose of:

```python
self.min_stack
```

---

# How `min_stack` Works

Suppose we push:

```text
5, 3, 7, 2, 6
```

Initially:

```text
stack     = []
min_stack = []
```

---

## Push `5`

Main Stack:

```text
[5]
```

`min_stack` is empty, so push `5`.

```text
stack     = [5]
min_stack = [5]
```

Current minimum:

```text
5
```

---

## Push `3`

Check:

```text
3 <= 5
```

True.

So:

```text
stack     = [5, 3]
min_stack = [5, 3]
```

Current minimum:

```text
3
```

---

## Push `7`

Check:

```text
7 <= 3
```

False.

So `7` goes only into the main Stack.

```text
stack     = [5, 3, 7]
min_stack = [5, 3]
```

Current minimum is still:

```text
3
```

---

## Push `2`

Check:

```text
2 <= 3
```

True.

So:

```text
stack     = [5, 3, 7, 2]
min_stack = [5, 3, 2]
```

Current minimum:

```text
2
```

---

## Push `6`

Check:

```text
6 <= 2
```

False.

So:

```text
stack     = [5, 3, 7, 2, 6]
min_stack = [5, 3, 2]
```

Current minimum:

```text
2
```

Notice:

```text
min_stack[-1] = 2
```

So `getMin()` can directly return the minimum.

---

# Why Don't We Store Every Element in `min_stack`?

The purpose of `min_stack` is only to remember:

```text
Current minimum
+
Previous minimums
```

For:

```text
5, 3, 7, 2, 6
```

The values:

```text
7
6
```

never become minimum values.

So there is no need to store them in `min_stack`.

We only store values when:

```python
val <= self.min_stack[-1]
```

---

# Why Do We Store Previous Minimums?

Suppose:

```text
stack     = [5, 3, 7, 2]
min_stack = [5, 3, 2]
```

Current minimum:

```text
2
```

Now pop `2`.

The new Stack becomes:

```text
[5, 3, 7]
```

What is the new minimum?

```text
3
```

Because `min_stack` stored previous minimums:

```text
[5, 3, 2]
```

we simply remove `2`:

```text
[5, 3]
```

Now:

```text
min_stack[-1] = 3
```

So the previous minimum is automatically restored.

This is the main reason `min_stack` stores a **history of minimum values**.

---

# Understanding `pop()`

The code is:

```python
if self.stack[-1] == self.min_stack[-1]:
    self.min_stack.pop()

self.stack.pop()
```

Before removing the main Stack's top, we ask:

```text
Is the element being removed
the current minimum?
```

If no:

```text
Remove only from stack
```

If yes:

```text
Remove from both stacks
```

Example:

```text
stack     = [5, 3, 7, 2]
min_stack = [5, 3, 2]
```

Pop:

```text
2
```

Since:

```text
stack[-1] == min_stack[-1]

2 == 2
```

we remove from both:

```text
stack     = [5, 3, 7]
min_stack = [5, 3]
```

Now:

```text
getMin() = 3
```

---

# The Most Important Detail — Why `<=` Instead of `<`?

This is the easiest mistake to make.

Your code correctly uses:

```python
val <= self.min_stack[-1]
```

not:

```python
val < self.min_stack[-1]
```

Consider:

```text
Push 5
Push 2
Push 2
```

With `<=`:

```text
stack     = [5, 2, 2]
min_stack = [5, 2, 2]
```

Now pop one `2`.

Since:

```text
2 == 2
```

we remove one `2` from both:

```text
stack     = [5, 2]
min_stack = [5, 2]
```

The minimum is still correctly:

```text
2
```

---

# What Goes Wrong With `<`?

Suppose we used:

```python
if val < self.min_stack[-1]:
```

Then after:

```text
Push 5
Push 2
Push 2
```

we would have:

```text
stack     = [5, 2, 2]

min_stack = [5, 2]
```

The second `2` would not be stored.

Now pop one `2`.

Because:

```text
stack[-1] == min_stack[-1]
```

we would remove `2` from `min_stack`.

Result:

```text
stack     = [5, 2]

min_stack = [5]
```

But the actual minimum is:

```text
2
```

while `getMin()` would return:

```text
5
```

Wrong.

Therefore, remember:

```text
Duplicate minimums must also be stored.
```

That is why:

```python
val <= self.min_stack[-1]
```

is required.

---

# Dry Run With Duplicate Minimum

Operations:

```text
push(5)
push(2)
push(3)
push(2)
```

State:

```text
stack:

[5, 2, 3, 2]


min_stack:

[5, 2, 2]
```

Current minimum:

```text
2
```

Now:

```text
pop()
```

removes the last `2`.

Since it is also the minimum, remove it from both.

Result:

```text
stack:

[5, 2, 3]


min_stack:

[5, 2]
```

Current minimum is still:

```text
2
```

This works because duplicate minimums were stored separately.

---

# `top()` vs `getMin()`

These two methods access different stacks.

## `top()`

```python
return self.stack[-1]
```

Returns:

```text
Most recently inserted element
```

---

## `getMin()`

```python
return self.min_stack[-1]
```

Returns:

```text
Current minimum element
```

Example:

```text
stack     = [5, 2, 7]

min_stack = [5, 2]
```

Then:

```text
top()    → 7

getMin() → 2
```

---

# Things You May Forget

## 1. Every element goes into the main Stack

```python
self.stack.append(val)
```

But only minimum candidates go into:

```python
self.min_stack
```

---

## 2. Use `<=`, not `<`

```python
val <= self.min_stack[-1]
```

because duplicate minimums must be tracked.

This is probably the most important edge case.

---

## 3. When popping, compare before removing

Correct:

```python
if self.stack[-1] == self.min_stack[-1]:
    self.min_stack.pop()

self.stack.pop()
```

We first check whether the main Stack's top is also the current minimum.

---

## 4. `min_stack` stores minimum history

Example:

```text
Push: 5, 3, 7, 2

min_stack:

[5, 3, 2]
```

If `2` is removed:

```text
3 automatically becomes the previous minimum.
```

---

## 5. `getMin()` does not search

Do not do:

```python
min(self.stack)
```

That would take:

```text
O(n)
```

The whole point of `min_stack` is:

```python
return self.min_stack[-1]
```

which takes:

```text
O(1)
```

---

# Complexity

All operations take constant time:

```text
push()   → O(1)

pop()    → O(1)

top()    → O(1)

getMin() → O(1)
```

Space Complexity:

```text
O(n)
```

because we maintain additional Stack storage.

---

# Pattern Used

For your DSA pattern sheet:

```text
Two Stacks + Auxiliary Min Stack
```

Short version:

```text
Min Stack / Auxiliary Stack
```

---

# Revision Summary

```text
Main Stack
    ↓
Stores all elements


Min Stack
    ↓
Stores current + previous minimums


Push:
    Always push into main stack

    Push into min_stack if:
    val <= current minimum


Pop:
    If main top == minimum
        pop from min_stack

    Then pop from main stack


getMin:
    min_stack[-1]
```

The most important thing to remember is:

```text
min_stack is not storing all values.

It stores the HISTORY of minimum values,
including duplicate minimums.
```

And the line you should never forget:

```python
if not self.min_stack or val <= self.min_stack[-1]:
```

The `=` in `<=` is important because of duplicate minimum values.
