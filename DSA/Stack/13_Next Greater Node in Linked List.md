# Next Greater Node in Linked List

## Problem

Given a singly linked list, for every node find the **first greater value on its right side**.

If no greater node exists on the right, the answer for that node is:

```text
0
```

Example:

```text
Linked List:

2 → 1 → 5
```

Output:

```text
[5, 5, 0]
```

Explanation:

```text
2 → Next Greater = 5

1 → Next Greater = 5

5 → No Greater Element = 0
```

---

# Main Idea

This problem is basically:

```text
Next Greater Element
+
Linked List
```

The easiest approach is:

```text
Linked List
    ↓
Convert to Array
    ↓
Traverse Right → Left
    ↓
Use Monotonic Stack
    ↓
Find Next Greater Value
```

The complete flow is:

```text
Linked List values Array me store karo

→ Answer array ko 0 se initialize karo

→ Right se Left traverse karo

→ Stack se smaller/equal elements hatao

→ Stack empty nahi hai to top = Next Greater

→ Current value Stack me push karo
```

---

# Code with Comments

```python
class Solution:
    def nextLargerNodes(
        self,
        head: Optional[ListNode]
    ) -> List[int]:

        # -----------------------------------------
        # STEP 1: Convert Linked List to Array
        # -----------------------------------------

        values = []

        curr = head

        while curr:

            # Store every node value
            values.append(curr.val)

            curr = curr.next


        # -----------------------------------------
        # STEP 2: Find Next Greater Element
        # -----------------------------------------

        stack = []

        # Default answer is 0 because if no
        # greater element exists on the right,
        # answer should remain 0
        ans = [0] * len(values)


        # Traverse from right to left because
        # we need the Next Greater element
        for i in range(
            len(values) - 1,
            -1,
            -1
        ):

            # Remove all elements that are
            # smaller than or equal to current.
            #
            # They cannot be the Next Greater
            # for the current element.
            while stack and stack[-1] <= values[i]:
                stack.pop()


            # If Stack is not empty,
            # the top is the nearest greater
            # element on the right
            if stack:
                ans[i] = stack[-1]


            # Current element may become the
            # Next Greater for elements on its left
            stack.append(values[i])


        return ans
```

---

# Why Convert the Linked List to an Array?

The problem asks for the:

```text
Next Greater Element on the RIGHT
```

The monotonic-stack approach is easiest when we can traverse:

```text
Right → Left
```

But a singly linked list only gives us:

```text
curr.next
```

So we can naturally move:

```text
Left → Right
```

but we cannot directly move:

```text
Right → Left
```

because there is no:

```text
curr.prev
```

Therefore, we first store all values:

```python
values = []

while curr:
    values.append(curr.val)
    curr = curr.next
```

Now:

```text
Linked List:

2 → 1 → 5
```

becomes:

```text
values = [2, 1, 5]
```

And now we can easily traverse:

```text
5 → 1 → 2
```

using indices.

### Remember

```text
Singly Linked List
        ↓
Cannot directly traverse backward
        ↓
Convert to Array
        ↓
Now Right → Left traversal is easy
```

---

# Why Traverse Right to Left?

For every element, we need information from its:

```text
RIGHT
```

So when processing the current element, we want the Stack to already contain useful elements from the right side.

Therefore:

```text
Need answer from RIGHT
        ↓
Process RIGHT side first
        ↓
Traverse Right → Left
```

The loop is:

```python
for i in range(len(values) - 1, -1, -1):
```

Here:

```text
start = len(values) - 1
```

means:

```text
Start from the last index
```

The second:

```text
-1
```

is the stopping boundary.

Python stops before reaching it, so index `0` is included.

The final:

```text
-1
```

is the step:

```text
Move one position backward
```

So:

```python
range(len(values) - 1, -1, -1)
```

means:

```text
Last Index → 0
```

---

# Understanding the Stack

The Stack stores possible:

```text
Next Greater Candidates
```

For every current value:

```text
Remove useless smaller/equal values
        ↓
Check Stack top
        ↓
Store answer
        ↓
Push current value
```

The main logic is:

```python
while stack and stack[-1] <= values[i]:
    stack.pop()
```

After this loop:

```text
Stack Empty
    ↓
No Greater Element


Stack Not Empty
    ↓
Stack Top > Current
    ↓
Stack Top = Next Greater
```

---

# Why Do We Pop `<=`?

We need a:

```text
STRICTLY GREATER
```

element.

Suppose:

```text
Current = 5

Stack Top = 5
```

Can `5` be the Next Greater of `5`?

No.

Because:

```text
5 is equal to 5
```

not greater.

Therefore equal elements must also be removed.

So we use:

```python
stack[-1] <= values[i]
```

Remember:

```text
Need Greater
    ↓
Keep >
    ↓
Pop <=
```

---

# Why Is the Stack Top the Next Greater?

After:

```python
while stack and stack[-1] <= values[i]:
    stack.pop()
```

all smaller and equal values on top have been removed.

If the Stack still contains something:

```text
stack[-1] > values[i]
```

So:

```python
ans[i] = stack[-1]
```

gives the next greater value.

Because of the monotonic-stack processing, the top represents the nearest useful greater candidate on the right.

---

# Why Initialize `ans` With `0`?

The problem says:

```text
If no greater node exists
→ Answer = 0
```

So instead of writing:

```python
if stack:
    ans[i] = stack[-1]
else:
    ans[i] = 0
```

we directly initialize:

```python
ans = [0] * len(values)
```

Example:

```text
values = [2, 1, 5]
```

Initially:

```text
ans = [0, 0, 0]
```

We only update an answer when a greater element exists:

```python
if stack:
    ans[i] = stack[-1]
```

If the Stack is empty, we do nothing.

The existing:

```text
0
```

remains as the answer.

### Remember

```text
Default answer already correct
        ↓
Only update when Next Greater exists
```

---

# Dry Run

Consider:

```text
values = [2, 1, 5]
```

Initially:

```text
stack = []

ans = [0, 0, 0]
```

We traverse:

```text
5 → 1 → 2
```

---

## Current = `5`

Stack:

```text
[]
```

No greater element exists.

So:

```text
ans[2] = 0
```

Push `5`:

```text
stack = [5]
```

---

## Current = `1`

Stack:

```text
[5]
```

Check:

```text
5 <= 1
```

False.

So Stack top is greater:

```text
Next Greater = 5
```

Update:

```text
ans = [0, 5, 0]
```

Push `1`:

```text
stack = [5, 1]
```

---

## Current = `2`

Stack:

```text
[5, 1]
```

Check top:

```text
1 <= 2
```

True.

Pop `1`:

```text
stack = [5]
```

Check again:

```text
5 <= 2
```

False.

So:

```text
Next Greater = 5
```

Update:

```text
ans = [5, 5, 0]
```

Push `2`:

```text
stack = [5, 2]
```

Final answer:

```text
[5, 5, 0]
```

---

# Why Use `while` Instead of `if`?

Suppose:

```text
Current = 4

Stack = [8, 6, 5, 2]
```

We need a value greater than `4`.

First:

```text
2 <= 4
```

Pop `2`.

Now:

```text
5 > 4
```

So `5` can be the answer.

In another case:

```text
Current = 7

Stack = [10, 9, 6, 5, 2]
```

We may need to remove:

```text
2
5
6
```

before reaching:

```text
9
```

Therefore, multiple elements may need to be removed.

So use:

```python
while stack and stack[-1] <= values[i]:
    stack.pop()
```

not:

```python
if stack and stack[-1] <= values[i]:
    stack.pop()
```

---

# Why Push the Current Value?

After finding the answer:

```python
stack.append(values[i])
```

The current value may become the Next Greater Element for a node on its left.

Example:

```text
values = [1, 3]
```

When processing `3`, it has no Next Greater.

But we still push it:

```text
stack = [3]
```

Later, when processing `1`:

```text
3
```

becomes its Next Greater.

So remember:

```text
Current may not have an answer
        ↓
But current may become the answer
for elements on its left
```

---

# Things You May Forget

## 1. Convert Linked List to Array

A singly linked list cannot directly traverse backward.

So:

```text
Linked List
→ Array
→ Right-to-Left Monotonic Stack
```

---

## 2. Traverse Right to Left

```text
Need Next Greater on RIGHT
        ↓
Traverse RIGHT → LEFT
```

---

## 3. Use `<=`

```python
while stack and stack[-1] <= values[i]:
    stack.pop()
```

because we need:

```text
Strictly Greater
```

Equal values are not valid answers.

---

## 4. Answer Default Is `0`

```python
ans = [0] * len(values)
```

If no greater value exists, simply leave the answer unchanged.

---

## 5. No `ans.reverse()` Is Needed

This is important.

We are traversing right to left, but we are storing answers directly at their correct index:

```python
ans[i] = stack[-1]
```

We are **not** doing:

```python
ans.append(...)
```

Therefore:

```text
No reverse needed.
```

Remember:

```text
Right → Left + append()
        ↓
Usually reverse answer


Right → Left + ans[i]
        ↓
No reverse needed
```

---

# Complexity

## Time Complexity

Converting the Linked List to an array:

```text
O(n)
```

Monotonic Stack traversal:

```text
O(n)
```

Each element is pushed once and popped at most once.

Overall:

```text
O(n)
```

## Space Complexity

```text
O(n)
```

Extra space is used for:

```text
values array
answer array
stack
```

---

# Revision Summary

```text
Linked List
    ↓
Convert to values array
    ↓
Initialize ans with 0
    ↓
Traverse Right → Left
    ↓
Pop all <= current
    ↓
Stack not empty?
    ↓
Top = Next Greater
    ↓
Store directly at ans[i]
    ↓
Push current
```

The easiest way to remember:

```text
Linked List ko Array banao

→ Right se Left chalo

→ Current se chhote ya equal sab pop karo

→ Stack top bacha to wahi Next Greater

→ Nahi bacha to answer already 0 hai

→ Current ko push karo
```

## Pattern Name

```text
Linked List → Array + Monotonic Stack (Next Greater)
```
