# Insert an Element at the Bottom of a Stack

## Problem

Given a stack and a value `val`, insert the value at the **bottom of the stack** without changing the order of the existing elements.

### Example

```text
Initial Stack:

Top
 ↓
60
50
40
30
20

Insert: 10
```

After inserting `10` at the bottom:

```text
Top
 ↓
60
50
40
30
20
10
↑
Bottom
```

---

## Pattern Used

### Recursion + Backtracking

This problem uses two important concepts:

- **Recursion** → Remove elements until we reach the bottom of the stack.
- **Backtracking** → Restore all removed elements while recursive calls return.

The pattern is:

```text
DO SOMETHING
    ↓
RECURSIVE CALL
    ↓
UNDO / RESTORE SOMETHING
```

For this problem:

```text
POP
 ↓
RECURSIVE CALL
 ↓
PUSH BACK
```

In code:

```python
topElement = stack.pop()

insertAtBottom(stack, val)

stack.append(topElement)
```

This is the main pattern to remember.

---

## Code

```python
def insertAtBottom(stack, val):
    # Base Case:
    # When the stack becomes empty, we have reached
    # the bottom of the original stack.
    if len(stack) == 0:
        stack.append(val)
        return

    # Store the current top element before removing it.
    # Every recursive call stores its own topElement.
    topElement = stack.pop()

    # Recursion Phase:
    # Keep removing elements until the stack becomes empty.
    insertAtBottom(stack, val)

    # Backtracking Phase:
    # After inserting 'val' at the bottom, restore the
    # removed elements one by one in their original order.
    stack.append(topElement)


stack = []

stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
stack.append(60)

insertAtBottom(stack, 10)

while stack:
    item = stack.pop()
    print(item)
```

---

# How the Approach Works

Suppose our stack is:

```text
Bottom                  Top
  ↓                      ↓
[20, 30, 40, 50, 60]
```

We want to insert:

```text
10
```

The problem is that we cannot directly access the bottom of a stack.

We can only access the top.

Therefore, we:

```text
1. Remove all elements using recursion.
2. Insert 10 when the stack becomes empty.
3. Restore all removed elements using backtracking.
```

---

# Phase 1: Recursion

We keep removing the top element.

### Call 1

```python
topElement = stack.pop()
```

Removes:

```text
60
```

Stack:

```text
[20, 30, 40, 50]
```

Then:

```python
insertAtBottom(stack, 10)
```

---

### Call 2

Remove `50`:

```text
[20, 30, 40]
```

---

### Call 3

Remove `40`:

```text
[20, 30]
```

---

### Call 4

Remove `30`:

```text
[20]
```

---

### Call 5

Remove `20`:

```text
[]
```

Now the stack is empty.

---

# Base Case

The condition becomes true:

```python
if len(stack) == 0:
```

So we insert:

```python
stack.append(10)
```

Now:

```text
[10]
```

At this moment, `10` has successfully been inserted at the bottom.

---

# Phase 2: Backtracking

Now the recursive calls start returning.

This line starts executing:

```python
stack.append(topElement)
```

Each recursive call remembers its own `topElement`.

The call stack conceptually contains:

```text
Call 1 → saved 60
Call 2 → saved 50
Call 3 → saved 40
Call 4 → saved 30
Call 5 → saved 20
```

Because recursion follows LIFO, the calls return in reverse order.

---

### Restore 20

```text
[10, 20]
```

### Restore 30

```text
[10, 20, 30]
```

### Restore 40

```text
[10, 20, 30, 40]
```

### Restore 50

```text
[10, 20, 30, 40, 50]
```

### Restore 60

```text
[10, 20, 30, 40, 50, 60]
```

Final stack:

```text
Bottom                  Top
  ↓                      ↓
[10, 20, 30, 40, 50, 60]
```

---

# Recursion Tree / Call Flow

```text
insertAtBottom([20,30,40,50,60], 10)
│
├── pop 60
│
└── insertAtBottom([20,30,40,50], 10)
    │
    ├── pop 50
    │
    └── insertAtBottom([20,30,40], 10)
        │
        ├── pop 40
        │
        └── insertAtBottom([20,30], 10)
            │
            ├── pop 30
            │
            └── insertAtBottom([20], 10)
                │
                ├── pop 20
                │
                └── insertAtBottom([], 10)
                    │
                    └── push 10  ← BASE CASE
```

Now backtracking starts:

```text
                push 20
            push 30
        push 40
    push 50
push 60
```

---

# The Most Important Part

```python
topElement = stack.pop()

insertAtBottom(stack, val)

stack.append(topElement)
```

Think about these three lines as:

```text
Choose / Remove
      ↓
Explore using Recursion
      ↓
Restore during Backtracking
```

For this problem:

```text
POP
 ↓
GO DEEPER
 ↓
PUSH BACK
```

The recursive call goes **towards the bottom**:

```python
insertAtBottom(stack, val)
```

The code after the recursive call restores the stack:

```python
stack.append(topElement)
```

That restoration phase is **backtracking**.

---

# Pattern Recognition

When you see a Stack problem where you need to modify something at the **bottom** while preserving the remaining order, think about:

```text
Recursion + Backtracking
```

General template:

```python
def solve(stack):

    # Base Case
    if base_condition:
        return

    # Save / Remove
    top = stack.pop()

    # Recursive Call
    solve(stack)

    # Backtrack / Restore
    stack.append(top)
```

This same core pattern can appear in problems where you need to:

- Reach the bottom of a stack.
- Remove an element temporarily.
- Perform an operation on the remaining stack.
- Restore removed elements afterward.

---

# Complexity Analysis

## Time Complexity

```text
O(n)
```

Every element is:

- Popped once.
- Pushed back once.

Therefore:

```text
O(n) + O(n) = O(n)
```

which simplifies to:

```text
O(n)
```

## Space Complexity

```text
O(n)
```

We use the recursive call stack.

For `n` stack elements, there can be `n` recursive calls.

---

# Key Takeaway

The core pattern of this problem is:

```text
POP
 ↓
RECURSE
 ↓
BASE CASE → INSERT AT BOTTOM
 ↓
BACKTRACK
 ↓
PUSH REMOVED ELEMENTS BACK
```

Remember this code pattern:

```python
top = stack.pop()

recursive_call()

stack.append(top)
```

The operation before recursion takes us deeper into the problem, while the operation after recursion restores the previous state during backtracking.