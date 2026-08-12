# First Non-Repeating Character in a Stream

## Problem

Given a string/stream of characters, after reading each character, find the **first character that has appeared only once so far**.

If there is no non-repeating character, add:

```text
#
```

Example:

```text
Input:
a a b c

Output:
a # b b
```

---

# Pattern

```text
Queue + Hash Map
```

---

# Main Idea

We need two things:

### 1. Hash Map

Keep track of how many times each character has appeared.

```python
hash_map[ch] = hash_map.get(ch, 0) + 1
```

Example:

```text
a → 2
b → 1
c → 1
```

### 2. Queue

Keep characters in the order in which they appeared.

```text
a → b → c
```

Why?

Because we need the **first** non-repeating character.

Queue gives us:

```text
First In → First Out
```

So the front of the queue is always the oldest candidate.

---

# Why Do We Store Characters in the Queue?

We need to know:

> Which character appeared first and is still non-repeating?

Therefore:

```python
q.append(ch)
```

stores every character in its arrival order.

Example:

```text
Stream:

a b a c

Queue:

a b a c
```

When `a` becomes repeated, we remove it from the front.

```text
b a c
```

Now `b` is the first remaining candidate.

---

# Why Do We Need Both Queue and Hash Map?

They solve two different problems.

### Hash Map

Answers:

```text
How many times has this character appeared?
```

### Queue

Answers:

```text
Which candidate appeared first?
```

So:

```text
Hash Map → Frequency
Queue    → Order
```

This combination is the main pattern.

---

# Code

```python
from collections import deque

class Solution:
    def firstNonRepeating(self, s):
        hash_map = {}
        q = deque()
        ans = []

        for ch in s:

            # Count frequency
            hash_map[ch] = hash_map.get(ch, 0) + 1

            # Store character in arrival order
            q.append(ch)

            # Remove characters that are repeated
            while q:

                # Front is currently non-repeating
                if hash_map[q[0]] == 1:
                    ans.append(q[0])
                    break

                # Repeated → no longer a candidate
                else:
                    q.popleft()

            # No non-repeating character exists
            if not q:
                ans.append('#')

        return ''.join(ans)
```

---

# Why Use `while`, Not `if`?

Suppose:

```text
Queue:

a b c
```

and:

```text
a → repeated
b → repeated
c → non-repeating
```

We cannot remove only `a`.

We need to keep removing repeated characters until the first valid character is found.

Therefore:

```python
while q:
```

is required.

---

# Dry Run

Consider:

```text
s = "aabc"
```

### Character: `a`

Frequency:

```text
a → 1
```

Queue:

```text
a
```

`a` occurs once.

Answer:

```text
a
```

---

### Character: `a`

Frequency:

```text
a → 2
```

Queue:

```text
a a
```

Front `a` is repeated.

Remove:

```text
a
```

Remove again:

```text
Queue = empty
```

No non-repeating character.

Answer:

```text
#
```

---

### Character: `b`

Frequency:

```text
a → 2
b → 1
```

Queue:

```text
b
```

`b` occurs once.

Answer:

```text
b
```

---

### Character: `c`

Frequency:

```text
a → 2
b → 1
c → 1
```

Queue:

```text
b c
```

Front is `b`.

`b` occurs once.

Answer:

```text
b
```

Final:

```text
a#bb
```

---

# Important Point: Why Can Repeated Characters Stay Inside the Queue?

When a character becomes repeated, we don't immediately remove it from the queue unless it reaches the front.

Example:

```text
Queue:

a b c
```

Suppose `c` becomes repeated.

We could remove it immediately, but we don't need to.

The queue is mainly concerned with the **front candidate**.

When `c` eventually reaches the front, this check:

```python
hash_map[q[0]] == 1
```

will detect that it is repeated and remove it.

This keeps the implementation simple.

---

# Why `q[0]`?

```python
q[0]
```

means the **front character**.

Because the queue stores characters in their arrival order:

```text
First character → Front
Latest character → Rear
```

Therefore the front is the earliest candidate for being the first non-repeating character.

---

# Important Order of Operations

For every character:

```text
1. Increase frequency
        ↓
2. Add character to queue
        ↓
3. Remove repeated characters from front
        ↓
4. Front = first non-repeating character
        ↓
5. If queue empty → '#'
```

Remember:

```text
Frequency tells us WHAT is repeated.
Queue tells us WHICH comes first.
```

---

# Common Mistakes

### 1. Using Only a Hash Map

A hash map can tell us frequency, but it doesn't directly maintain the required candidate order.

We need:

```text
Hash Map + Queue
```

---

### 2. Using `pop()` Instead of `popleft()`

Queue removal must happen from the front:

```python
q.popleft()
```

Not:

```python
q.pop()
```

`pop()` removes from the rear.

---

### 3. Using `if` Instead of `while`

Wrong:

```python
if hash_map[q[0]] > 1:
    q.popleft()
```

There may be multiple repeated characters at the front.

Use:

```python
while q:
```

---

### 4. Forgetting the `#`

If:

```python
not q
```

then there is no non-repeating character.

Add:

```python
'#'
```

---

# Complexity

Let `n` be the length of the string.

### Time

```text
O(n)
```

Although there is a `while` loop, each character can be removed from the queue at most once.

So the total work is linear.

### Space

```text
O(n)
```

for the queue and frequency map.

---

# Pattern Recognition

When the problem says:

```text
Process characters one by one
+
Find the first character satisfying some condition
+
Maintain original order
```

Think:

```text
Queue + Hash Map
```

For this problem:

```text
Condition → frequency == 1
```

---

# Revision Cheat Sheet

```text
Problem:
First Non-Repeating Character in a Stream

Pattern:
Queue + Hash Map

Hash Map:
Stores frequency

Queue:
Stores characters in arrival order

For every character:

1. frequency[ch] += 1
2. q.append(ch)
3. Remove repeated characters from front
4. q[0] = first non-repeating character
5. If q is empty → '#'

Why Queue?
Need the FIRST valid character.

Why Hash Map?
Need character frequency.

Why while?
Multiple repeated characters may be at the front.

Queue operation:
popleft()

Time:
O(n)

Space:
O(n)
```

## One-Line Pattern

```text
Hash Map for frequency + Queue for order → remove repeated front characters → front gives first non-repeating.
```
