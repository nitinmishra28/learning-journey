# Minimum Number of Swaps to Make the String Balanced

## Problem

Given a string containing only:

```text
[
]
```

The string contains an equal number of opening and closing brackets.

We can swap any two characters.

Find the minimum number of swaps required to make the bracket string balanced.

Example:

```text
s = "][]["
```

After one swap:

```text
[][]
```

So:

```text
Answer = 1
```

---

# Main Idea

First, remove all brackets that are already correctly matched.

After removing all valid pairs, only the unmatched brackets remain.

Then:

```text
Count unmatched brackets
        ↓
Find number of unmatched opening/closing brackets
        ↓
Calculate minimum swaps needed
```

The complete flow is:

```text
Match valid [] pairs
        ↓
Keep unmatched brackets in Stack
        ↓
unmatched_pairs = len(stack) // 2
        ↓
swaps = (unmatched_pairs + 1) // 2
```

---

# Code with Comments

```python
class Solution:
    def minSwaps(self, s: str) -> int:

        stack = []

        for ch in s:

            # Opening bracket:
            # store it because it may match
            # with a future closing bracket
            if ch == '[':
                stack.append(ch)

            else:

                # If current ']' can match with
                # an opening '[' on the top,
                # remove the matched opening bracket
                if stack and stack[-1] == '[':
                    stack.pop()

                # Otherwise this closing bracket
                # is currently unmatched
                else:
                    stack.append(ch)


        # After removing all valid pairs,
        # stack contains only unmatched brackets.
        #
        # Since the original string contains an equal
        # number of '[' and ']',
        # unmatched opening and closing counts are equal.
        unmatched_pairs = len(stack) // 2


        # One swap can fix two misplaced pairs.
        #
        # We need ceil(unmatched_pairs / 2).
        #
        # Integer version of ceil(x / 2):
        return (unmatched_pairs + 1) // 2
```

---

# How the Stack Works

Whenever we find:

```text
[
```

we push it:

```python
stack.append(ch)
```

because it may be matched by a future:

```text
]
```

When we find:

```text
]
```

we check whether the Stack top is:

```text
[
```

If yes:

```text
[]
```

forms a valid pair.

So we remove the opening bracket:

```python
stack.pop()
```

If the Stack is empty or the top is already `]`, the current closing bracket cannot form a valid pair.

So we keep it:

```python
stack.append(ch)
```

---

# Example

Consider:

```text
s = "]]][[["
```

Start:

```text
stack = []
```

Process the first three `]`:

```text
stack = [']', ']', ']']
```

None of them can be matched because no `[` appeared before them.

Now process the three `[`:

```text
stack = [']', ']', ']', '[', '[', '[']
```

So:

```text
len(stack) = 6
```

These are all unmatched brackets.

---

# Why `len(stack) // 2`?

After all valid pairs are removed, the remaining brackets look conceptually like:

```text
]]...[[...
```

Because the original string has an equal number of:

```text
[
```

and:

```text
]
```

the number of unmatched opening brackets and unmatched closing brackets must also be equal.

For:

```text
]]][[[
```

we have:

```text
3 unmatched ]

3 unmatched [
```

Total unmatched brackets:

```text
6
```

Therefore:

```python
unmatched_pairs = len(stack) // 2
```

gives:

```text
6 // 2 = 3
```

So:

```text
unmatched_pairs
```

represents the number of unmatched brackets of **each type**.

You can think of it as:

```text
Stack size = 2 × unmatched_pairs
```

Therefore:

```text
unmatched_pairs = Stack size / 2
```

---

# Why Is the Answer `(unmatched_pairs + 1) // 2`?

Suppose:

```text
unmatched_pairs = 3
```

The unmatched pattern is:

```text
]]][[[
```

One swap can fix two misplaced bracket positions at once.

So the required number of swaps is:

```text
ceil(unmatched_pairs / 2)
```

For:

```text
unmatched_pairs = 3
```

we need:

```text
ceil(3 / 2)
=
2
```

Instead of using floating-point `ceil()`, we use:

```python
(unmatched_pairs + 1) // 2
```

So:

```text
(3 + 1) // 2
=
4 // 2
=
2
```

Another example:

```text
unmatched_pairs = 4
```

Then:

```text
(4 + 1) // 2
=
5 // 2
=
2
```

So this formula gives:

```text
ceil(unmatched_pairs / 2)
```

using integer division.

---

# Important Formula

If:

```text
stack_size = number of unmatched brackets
```

then:

```python
unmatched_pairs = stack_size // 2
```

And:

```python
minimum_swaps = (unmatched_pairs + 1) // 2
```

The complete formula is:

```text
Unmatched Brackets
        ↓
len(stack)
        ↓
Unmatched Count of Each Type
        ↓
len(stack) // 2
        ↓
Minimum Swaps
        ↓
ceil(unmatched_pairs / 2)
```

---

# Why Do We Only Match With Stack Top?

When the current character is:

```text
]
```

it can close an unmatched opening bracket only when the latest unmatched bracket is:

```text
[
```

So:

```python
if stack and stack[-1] == '[':
    stack.pop()
```

If the top is:

```text
]
```

then the current `]` also cannot create a valid pair.

So it remains unmatched.

---

# Things You May Forget

## 1. Only pop for a valid `[]` pair

```python
if stack and stack[-1] == '[':
    stack.pop()
```

Do not blindly pop whenever you see `]`.

---

## 2. Unmatched brackets stay in the Stack

After processing the complete string:

```text
Stack contains only brackets
that could not be matched.
```

---

## 3. Why divide Stack length by 2?

```python
unmatched_pairs = len(stack) // 2
```

Because unmatched opening and closing brackets occur in equal counts.

Example:

```text
]]][[[

3 closing
3 opening

Total = 6

6 // 2 = 3
```

---

## 4. Do not directly return `unmatched_pairs`

One swap can fix more than one misplaced bracket pair.

So the answer is not:

```python
return unmatched_pairs
```

It is:

```python
return (unmatched_pairs + 1) // 2
```

---

## 5. Remember the ceiling formula

For a positive integer `x`:

```text
ceil(x / 2)
```

can be written using integer division as:

```python
(x + 1) // 2
```

Here:

```python
(unmatched_pairs + 1) // 2
```

---

# Complexity

## Time Complexity

```text
O(n)
```

We traverse the string once.

## Space Complexity

```text
O(n)
```

In the worst case, all brackets may remain in the Stack.

---

# Revision Summary

```text
Traverse brackets
        ↓
'[' → Push
        ↓
']' + Stack top '[' → Pop
        ↓
Otherwise → Push unmatched ']'
        ↓
After traversal:
Stack contains unmatched brackets
        ↓
unmatched_pairs = len(stack) // 2
        ↓
Minimum swaps = ceil(unmatched_pairs / 2)
        ↓
(unmatched_pairs + 1) // 2
```

The easiest way to remember the solution is:

```text
Pehle saare valid [] pairs hatao
        ↓
Stack me sirf unmatched brackets bachenge
        ↓
Unmatched count of each type = stack size / 2
        ↓
One swap can fix two misplaced pairs
        ↓
Answer = ceil(unmatched_pairs / 2)
```

## Pattern Name

```text
Stack + Unmatched Bracket Counting
```
