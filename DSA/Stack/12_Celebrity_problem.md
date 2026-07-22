# Celebrity Problem

## Problem

A party contains `n` people represented by a matrix:

```python
mat[i][j]
```

where:

```text
mat[i][j] = 1
→ Person i knows Person j

mat[i][j] = 0
→ Person i does not know Person j
```

A person is a **Celebrity** if:

```text
1. Celebrity knows nobody.

2. Everybody knows the Celebrity.
```

Return the celebrity's index.

If no celebrity exists:

```text
-1
```

---

# Main Idea

We solve this problem in two phases:

```text
Phase 1 → Find one possible candidate using elimination

Phase 2 → Verify whether that candidate is actually a celebrity
```

The complete flow is:

```text
Put all people into Stack
        ↓
Take two people: a and b
        ↓
Does a know b?
     /       \
   Yes        No
    ↓          ↓
a cannot     b cannot
be celebrity be celebrity
    ↓          ↓
Keep b       Keep a
        ↓
Repeat until one candidate remains
        ↓
Verify candidate
```

---

# Code with Comments

```python
class Solution:
    def celebrity(self, mat):

        stack = []

        # Put every person's index into the stack
        for i in range(len(mat)):
            stack.append(i)


        # Keep eliminating one person
        # until only one possible candidate remains
        while len(stack) > 1:

            a = stack.pop()
            b = stack.pop()


            # If a knows b:
            #
            # a cannot be a celebrity because
            # a celebrity knows nobody.
            #
            # So eliminate a and keep b.
            if mat[a][b] == 1:
                stack.append(b)


            # If a does NOT know b:
            #
            # b cannot be a celebrity because
            # everyone must know the celebrity.
            #
            # Since a does not know b,
            # eliminate b and keep a.
            else:
                stack.append(a)


        # Only one possible candidate remains
        candidate = stack.pop()


        # Verify whether the candidate
        # actually satisfies both celebrity conditions
        for i in range(len(mat)):

            # Do not compare candidate with themselves
            if i != candidate:

                # Candidate knows someone
                # OR
                # Someone does not know candidate
                #
                # Either condition means candidate
                # is not a celebrity
                if (
                    mat[candidate][i] == 1
                    or
                    mat[i][candidate] == 0
                ):
                    return -1


        return candidate
```

---

# Understanding the Matrix

Suppose:

```text
mat[a][b]
```

The first index represents:

```text
a
↓
Who is doing the knowing?
```

The second index represents:

```text
b
↓
Who is being known?
```

So:

```python
mat[a][b] == 1
```

means:

```text
a knows b
```

This direction is important.

Do not confuse:

```text
mat[a][b]
```

with:

```text
mat[b][a]
```

They represent different relationships.

---

# Celebrity Conditions in Matrix Form

Suppose:

```text
candidate = c
```

For `c` to be a celebrity:

## Candidate's Row

The celebrity knows nobody:

```text
mat[c][i] == 0
```

for every other person.

So the candidate's row should contain:

```text
0
```

for everyone else.

---

## Candidate's Column

Everybody knows the celebrity:

```text
mat[i][c] == 1
```

for every other person.

So the candidate's column should contain:

```text
1
```

for everyone else.

Remember:

```text
Celebrity ROW
→ All 0
→ Celebrity knows nobody


Celebrity COLUMN
→ All 1
→ Everybody knows celebrity
```

We ignore the diagonal:

```text
mat[c][c]
```

because whether a person knows themselves does not matter.

---

# Why Does the Elimination Work?

Take any two people:

```text
a
b
```

Now check only:

```python
mat[a][b]
```

There are only two possibilities.

---

# Case 1: `a` Knows `b`

```python
if mat[a][b] == 1:
```

This means:

```text
a → knows → b
```

Can `a` be the celebrity?

No.

Because:

```text
Celebrity knows nobody.
```

But we just found:

```text
a knows b.
```

Therefore:

```text
a is definitely NOT celebrity.
```

So we eliminate `a`:

```python
stack.append(b)
```

Important:

```text
We are NOT saying that b is definitely the celebrity.
```

We only know:

```text
a is definitely not the celebrity.
```

Therefore `b` survives as a **possible candidate**.

---

# Case 2: `a` Does Not Know `b`

```python
mat[a][b] == 0
```

This means:

```text
a does NOT know b.
```

Can `b` be the celebrity?

No.

Because:

```text
Everybody must know the celebrity.
```

But:

```text
a does not know b.
```

Therefore:

```text
b is definitely NOT celebrity.
```

So we eliminate `b`:

```python
stack.append(a)
```

Again:

```text
We are NOT proving that a is the celebrity.
```

We only proved:

```text
b cannot be the celebrity.
```

---

# Most Important Elimination Rule

Remember this:

```text
a knows b
    ↓
a is OUT
    ↓
Keep b


a does not know b
    ↓
b is OUT
    ↓
Keep a
```

Or even shorter:

```text
a → b = 1
Eliminate a


a → b = 0
Eliminate b
```

---

# Why Do We Only Check `mat[a][b]`?

This is an important point.

Suppose:

```python
mat[a][b] == 1
```

Then we already know:

```text
a cannot be celebrity.
```

That is enough to eliminate one person.

We do not need to check:

```python
mat[b][a]
```

at this stage.

The goal of this phase is not to find the celebrity immediately.

The goal is only:

```text
Eliminate one impossible person
from every comparison.
```

Each comparison removes one person.

So eventually:

```text
n people
    ↓
n - 1 eliminations
    ↓
1 possible candidate
```

---

# Important: The Remaining Person Is Only a Candidate

After the elimination phase:

```python
candidate = stack.pop()
```

This person is not automatically the celebrity.

The elimination process only guarantees:

```text
Everyone else was eliminated
based on some contradiction.
```

But the remaining candidate may still fail the complete celebrity conditions.

Therefore, final verification is compulsory.

---

# Final Verification

For every other person `i`:

```python
if i != candidate:
```

we check two conditions.

---

## Condition 1: Candidate Must Know Nobody

```python
mat[candidate][i] == 1
```

If this is true:

```text
Candidate knows i.
```

Therefore:

```text
Candidate cannot be celebrity.
```

---

## Condition 2: Everybody Must Know Candidate

```python
mat[i][candidate] == 0
```

If this is true:

```text
Person i does not know candidate.
```

Therefore:

```text
Candidate cannot be celebrity.
```

So:

```python
if mat[candidate][i] == 1 or mat[i][candidate] == 0:
    return -1
```

---

# Why Do We Use `or`?

The candidate must satisfy **both** conditions:

```text
Candidate knows nobody

AND

Everybody knows candidate
```

If even one condition fails, the person is not a celebrity.

So failure means:

```text
Candidate knows someone

OR

Someone does not know candidate
```

That is why we use:

```python
or
```

in:

```python
if mat[candidate][i] == 1 or mat[i][candidate] == 0:
```

---

# Why `i != candidate`?

We use:

```python
if i != candidate:
```

because we do not need to check:

```text
Does candidate know themselves?
```

The value:

```python
mat[candidate][candidate]
```

does not affect whether the person is a celebrity.

We only care about relationships with other people.

---

# Example

Suppose:

```python
mat = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 1, 0]
]
```

Person `1` is the celebrity.

Why?

Row `1`:

```text
[0, 0, 0]
```

Person `1` knows nobody.

Column `1`:

```text
1
0
1
```

Ignoring:

```text
mat[1][1]
```

every other person knows person `1`.

So:

```text
Celebrity = 1
```

---

# Elimination Dry Run

Initial Stack:

```text
[0, 1, 2]
```

Pop:

```text
a = 2
b = 1
```

Check:

```python
mat[2][1] == 1
```

So:

```text
2 knows 1
```

Therefore:

```text
2 cannot be celebrity
```

Keep:

```text
1
```

Stack:

```text
[0, 1]
```

Now pop:

```text
a = 1
b = 0
```

Check:

```python
mat[1][0] == 0
```

So:

```text
1 does not know 0
```

Therefore:

```text
0 cannot be celebrity
```

Keep:

```text
1
```

Now:

```text
candidate = 1
```

Then verify person `1`.

---

# A Common Confusion

Suppose:

```python
if mat[a][b] == 1:
    stack.append(b)
```

You may think:

```text
"But what if b also knows someone?
Then b is also not a celebrity."
```

That can absolutely happen.

But right now we only know:

```text
a knows b
```

From this information, we can definitely eliminate:

```text
a
```

We do not yet have enough information to eliminate `b`.

So `b` remains only as a:

```text
Possible Candidate
```

If `b` is not actually a celebrity, either:

```text
b may get eliminated later
```

or:

```text
b may survive but fail final verification
```

That is why the algorithm is:

```text
Eliminate first
Verify later
```

---

# Things You May Forget

## 1. Matrix Direction

```python
mat[a][b]
```

means:

```text
a knows b
```

not:

```text
b knows a
```

---

## 2. Elimination Rule

```text
a knows b
→ a cannot be celebrity
→ Keep b


a does not know b
→ b cannot be celebrity
→ Keep a
```

---

## 3. Surviving Does Not Mean Confirmed

When you do:

```python
stack.append(b)
```

you are not saying:

```text
b is celebrity.
```

You are only saying:

```text
Based on this comparison,
b has not been eliminated yet.
```

---

## 4. Final Verification Is Mandatory

Check:

```python
mat[candidate][i] == 0
```

Candidate knows nobody.

And:

```python
mat[i][candidate] == 1
```

Everybody knows candidate.

---

## 5. Verification Failure Condition

The easiest form to remember:

```python
if mat[candidate][i] == 1 or mat[i][candidate] == 0:
    return -1
```

Meaning:

```text
Candidate knows someone
OR
Someone doesn't know candidate
        ↓
Not a Celebrity
```

---

## 6. Skip Self-Comparison

```python
if i != candidate:
```

because:

```text
mat[candidate][candidate]
```

does not matter.

---

# Complexity

## Time Complexity

Putting everyone into the Stack:

```text
O(n)
```

Elimination:

```text
O(n)
```

Verification:

```text
O(n)
```

Overall:

```text
O(n)
```

## Space Complexity

The Stack stores all people initially:

```text
O(n)
```

---

# Revision Summary

```text
Put all indices in Stack
        ↓
Pop a and b
        ↓
Check mat[a][b]
        ↓

If a knows b:
    a is OUT
    keep b

If a doesn't know b:
    b is OUT
    keep a
        ↓
Repeat
        ↓
One candidate remains
        ↓
Verify:
    Candidate knows nobody
    Everybody knows candidate
```

The easiest line to remember is:

```text
a knows b → a OUT

a doesn't know b → b OUT
```

And the complete thinking is:

```text
Elimination gives a possible candidate.

Verification gives the actual celebrity.
```

## Pattern Name

```text
Stack + Pairwise Candidate Elimination
```
