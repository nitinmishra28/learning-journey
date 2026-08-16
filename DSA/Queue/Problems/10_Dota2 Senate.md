# Dota2 Senate

## Problem

Given a string `senate` containing:

```text
R → Radiant
D → Dire
```

Each senator can ban one senator from the opposite party.

The senators act in the given order.

The process continues until only one party has senators remaining.

Return:

```text
"Radiant"
```

or:

```text
"Dire"
```

### Example

```text
Input:
"RDD"

Output:
"Dire"
```

---

# Pattern

```text
Queue + Simulation
```

---

# Why Do We Use a Queue?

The senators act in **order**.

For example:

```text
R D D R
```

The first senator acts first.

After acting, if that senator is still alive, they get another turn after the remaining senators.

This naturally matches a **Queue**:

```text
First In → First Out
```

We use:

```python
deque()
```

because we need:

```python
popleft()   # remove the senator whose turn is now
append()    # put the surviving senator at the back
```

---

# Why Do We Store Indices Instead of `R` and `D`?

We store the **index** of every senator:

```text
senate = "RDD"

Index:
0 → R
1 → D
2 → D
```

So:

```text
Radiant queue = [0]
Dire queue    = [1,2]
```

The index tells us **who gets to act first**.

Smaller index means the senator appears earlier in the current round.

Therefore:

```python
r < d
```

means:

```text
Radiant senator acts before Dire senator.
```

---

# Main Idea

We maintain two queues:

```python
radiant = deque()
dire = deque()
```

Each queue stores the indices of the senators who are still active.

Example:

```text
senate = "RDDRR"

Radiant:
[0,3,4]

Dire:
[1,2]
```

Then we compare the front senator from each queue.

```python
r = radiant.popleft()
d = dire.popleft()
```

The senator with the **smaller index acts first**.

The senator who acts first bans the other senator.

The surviving senator gets another turn, so we put them back into their queue with:

```python
index + n
```

---

# Why Do We Use `index + n`?

This is the most important part of the problem.

Suppose:

```text
senate = "RDD"
n = 3
```

Initially:

```text
Radiant = [0]
Dire    = [1,2]
```

Radiant `0` acts before Dire `1`.

Radiant survives and gets another turn.

But we cannot put `0` back directly:

```text
[0]
```

because `0` would again look like it comes before everyone.

Instead:

```python
radiant.append(0 + n)
```

so:

```text
0 + 3 = 3
```

Now:

```text
Radiant = [3]
Dire    = [2]
```

Index `3` represents:

> Radiant senator `0` getting another turn in the next round.

So:

```text
Original index:
0

Next round:
0 + n = 3

Next round again:
3 + n = 6
```

This lets us simulate the circular order using increasing indices.

---

# Why Does `r < d` Decide the Winner?

Suppose:

```text
Radiant queue = [2]
Dire queue    = [5]
```

Since:

```text
2 < 5
```

Radiant appears earlier in the current order.

Therefore:

```python
if r < d:
    radiant.append(r + n)
```

Radiant bans Dire `5`.

If:

```text
r > d
```

then Dire acts first and bans Radiant.

```python
else:
    dire.append(d + n)
```

---

# Code

```python
class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        radiant = deque()
        dire = deque()

        n = len(senate)

        # Store the indices of each party
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:

            # Get the next senator from each party
            r = radiant.popleft()
            d = dire.popleft()

            # Smaller index acts first
            if r < d:
                # Radiant bans Dire
                # Radiant gets another turn in next round
                radiant.append(r + n)

            else:
                # Dire bans Radiant
                # Dire gets another turn in next round
                dire.append(d + n)

        # One queue becomes empty
        return 'Radiant' if radiant else 'Dire'
```

---

# Dry Run

Consider:

```text
senate = "RDD"
```

Indexes:

```text
0 → R
1 → D
2 → D
```

Initial queues:

```text
Radiant = [0]
Dire    = [1,2]
```

---

### Round 1

Take:

```text
r = 0
d = 1
```

Since:

```text
0 < 1
```

Radiant acts first.

Dire `1` is banned.

Radiant gets another turn:

```text
0 + 3 = 3
```

Queues:

```text
Radiant = [3]
Dire    = [2]
```

---

### Round 2

Take:

```text
r = 3
d = 2
```

Since:

```text
3 > 2
```

Dire acts first.

Radiant `3` is banned.

Queues:

```text
Radiant = []
Dire    = [5]
```

Radiant queue is empty.

Therefore:

```text
Answer = "Dire"
```

---

# Why Do We Stop When One Queue Becomes Empty?

The loop is:

```python
while radiant and dire:
```

This means:

```text
Continue only while both parties have senators.
```

If:

```text
radiant = []
```

then no Radiant senator is left to act.

Therefore:

```text
Dire wins.
```

Similarly:

```text
dire = []
```

means:

```text
Radiant wins.
```

---

# Important Mistakes

### 1. Using a Normal List Instead of a Queue

You could use a list, but repeatedly removing from the front using:

```python
pop(0)
```

takes:

```text
O(n)
```

because remaining elements have to shift.

Use:

```python
from collections import deque
```

and:

```python
popleft()
```

which is:

```text
O(1)
```

---

### 2. Storing `R` and `D` Instead of Indices

We need to know **which senator acts first**.

So we store:

```text
indices
```

not just:

```text
R / D
```

The comparison:

```python
r < d
```

tells us who gets the current turn first.

---

### 3. Forgetting `+ n`

Wrong:

```python
radiant.append(r)
```

The same senator would appear to act at the same position again.

Correct:

```python
radiant.append(r + n)
```

This represents the senator's turn in the next round.

---

### 4. Thinking `r + n` Is a Real Index

It is not an actual index in the original string.

It is a **virtual index** used to represent future rounds.

```text
0      → first round
0 + n  → second round
0 + 2n → third round
```

---

# Complexity

Let `n` be the number of senators.

```text
Time  → O(n)
Space → O(n)
```

Each senator is processed through the queues a limited number of times relative to the total elimination process.

---

# Revision Cheat Sheet

```text
Dota2 Senate

Pattern:
Queue + Simulation

Use:
Two queues

radiant → Radiant senator indices
dire    → Dire senator indices

Why indices?
Smaller index = senator acts earlier.

Compare:
r < d
→ Radiant acts first
→ Dire is banned

r > d
→ Dire acts first
→ Radiant is banned

Winner gets another turn:
index + n

Why + n?
Represents the same senator's turn in the next round.

Queue operations:
popleft() → current senator acts
append()  → surviving senator gets another turn

Stop:
while radiant and dire

If radiant empty:
→ Dire wins

If dire empty:
→ Radiant wins

Time:
O(n)

Space:
O(n)
```

# One-Line Pattern  

```text
Store party indices in two queues → compare front indices → smaller index acts first → losing senator is removed → winner goes to next round using index + n. 
```