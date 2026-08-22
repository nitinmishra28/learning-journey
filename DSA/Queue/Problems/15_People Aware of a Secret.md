# People Aware of a Secret

## Problem

On day `1`, one person knows a secret.

Each person follows these rules:

```text
delay
→ They start sharing the secret after `delay` days.

forget
→ They forget the secret after `forget` days.

Once a person forgets the secret:
→ They can no longer share it.
```

We need to return the number of people who still remember the secret on day `n`.

Because the answer can become very large, return it modulo:

```text
10^9 + 7
```

---

# Pattern

```text
Queue + Sliding Window + Simulation
```

---

# Main Idea

We need to track two different events for every group of people:

```text
1. When they become active spreaders
2. When they forget the secret
```

So we use two queues:

```python
delayQ
forgetQ
```

### `delayQ`

Stores people who are waiting for their sharing delay to finish.

```text
(day they learned, number of people)
```

### `forgetQ`

Stores people who will eventually forget the secret.

```text
(day they learned, number of people)
```

---

# Why Do We Store `(day, people)`?

Suppose:

```text
day = 3
people = 5
```

This means:

```text
5 people learned the secret on day 3.
```

We need the original day because their future events depend on it.

They become active on:

```text
3 + delay
```

and forget on:

```text
3 + forget
```

So storing:

```python
(day, people)
```

allows us to know exactly when their state changes.

---

# What Does `curr` Mean?

```python
curr
```

represents:

```text
Number of people who currently know the secret
AND are allowed to spread it.
```

Important:

```text
curr ≠ total people who know the secret
```

For example:

```text
10 people remember the secret.

6 people are currently allowed to share it.

4 people are still waiting for their delay.

curr = 6
```

---

# What Does `ans` Mean?

```python
ans
```

represents:

```text
Total number of people who currently remember the secret.
```

So:

```text
ans → everyone who remembers
curr → people who can currently spread
```

This distinction is very important.

---

# Initial State

On day `1`:

```text
1 person knows the secret.
```

So:

```python
ans = 1
curr = 0
```

Why is:

```python
curr = 0
```

?

Because the first person has not waited for `delay` days yet.

We add this person to both queues:

```python
forgetQ.append((1, 1))
delayQ.append((1, 1))
```

Meaning:

```text
1 person learned on day 1.
```

They will:

```text
start spreading on day 1 + delay
forget on day 1 + forget
```

---

# Step 1: People Who Forget

```python
if forgetQ and forgetQ[0][0] + forget <= i:
```

Suppose:

```text
person learned on day 2
forget = 4
```

They forget on:

```text
2 + 4 = 6
```

So on day `6`:

```text
2 + 4 <= 6
```

They must be removed.

We do:

```python
day, people = forgetQ.popleft()
```

Then:

```python
ans = (ans - people) % M
curr = (curr - people) % M
```

Why both?

Because people who forget:

```text
are no longer counted in ans
AND
cannot spread anymore
```

---

# Why Do We Check Forgetting First?

This is important.

Suppose someone forgets on day `6`.

They should not be allowed to spread the secret on day `6`.

Therefore we remove them before calculating the new spreading for that day.

The order is:

```text
1. Forget
2. Become active
3. Spread
```

---

# Step 2: People Who Become Active

```python
if delayQ and delayQ[0][0] + delay <= i:
```

Suppose:

```text
person learned on day 2
delay = 3
```

They can start spreading on:

```text
2 + 3 = 5
```

On day `5`:

```text
2 + 3 <= 5
```

So they become active.

We remove them from the waiting queue:

```python
day, people = delayQ.popleft()
```

and add them to:

```python
curr
```

```python
curr = (curr + people) % M
```

---

# Step 3: Active People Spread

Now:

```python
if curr > 0:
```

means there are people who are currently allowed to share.

If:

```text
curr = 5
```

then these 5 people create:

```text
5 new people
```

who learn the secret today.

So:

```python
ans = (ans + curr) % M
```

The new people also need to be tracked for their future:

```text
sharing
forgetting
```

Therefore:

```python
delayQ.append((i, curr))
forgetQ.append((i, curr))
```

---

# Why Add `curr` to Both Queues?

Suppose:

```text
curr = 5
```

means 5 people learn the secret today.

These 5 people will eventually:

```text
start spreading
```

and:

```text
forget
```

So we add them to both:

```python
delayQ
forgetQ
```

with:

```text
(day they learned, number of people)
```

---

# Code

```python
from collections import deque


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        M = 10**9 + 7

        # Total people who currently know the secret
        ans = 1

        # People who are currently allowed to spread
        curr = 0

        # (day learned, number of people)
        forgetQ = deque()
        delayQ = deque()

        # Person who learns on day 1
        forgetQ.append((1, 1))
        delayQ.append((1, 1))

        for i in range(1, n + 1):

            # Step 1:
            # Remove people who forget the secret
            if forgetQ and forgetQ[0][0] + forget <= i:

                day, people = forgetQ.popleft()

                ans = (ans - people) % M
                curr = (curr - people) % M

            # Step 2:
            # People whose delay is over become spreaders
            if delayQ and delayQ[0][0] + delay <= i:

                day, people = delayQ.popleft()

                curr = (curr + people) % M

            # Step 3:
            # Active spreaders create new people
            if curr > 0:

                ans = (ans + curr) % M

                # New people will become spreaders later
                delayQ.append((i, curr))

                # New people will forget later
                forgetQ.append((i, curr))

        return ans
```

---

# Dry Run

Consider:

```text
n = 6
delay = 2
forget = 4
```

Initial:

```text
Day 1:

ans = 1
curr = 0
```

Queues:

```text
delayQ  = [(1,1)]
forgetQ = [(1,1)]
```

---

## Day 1

The first person has not reached the delay yet.

```text
curr = 0
ans = 1
```

---

## Day 2

The person from day 1 becomes active:

```text
1 + 2 <= 2
```

So:

```text
curr = 1
```

They spread the secret.

New person:

```text
ans = 2
```

Queues now contain:

```text
day 2 → 1 new person
```

---

## Day 3

The person from day 2 becomes active.

Now:

```text
curr = 2
```

Both active people spread.

So:

```text
ans = 4
```

---

## Day 4

People continue spreading.

The exact number grows according to the number of active spreaders.

The important flow is always:

```text
Forget old people
        ↓
Activate people whose delay finished
        ↓
Active people create new people
        ↓
Store new people in both queues
```

---

# Queue Visualization

Think of `delayQ` as:

```text
People waiting to become spreaders

(day, people)
```

Example:

```text
[(3,5), (4,8), (5,10)]
```

When:

```text
day + delay <= current_day
```

they move from:

```text
waiting
```

to:

```text
active
```

---

`forgetQ` is:

```text
People waiting to forget
```

Example:

```text
[(2,3), (4,5), (5,8)]
```

When:

```text
day + forget <= current_day
```

they are removed.

---

# Why Are Queues Suitable?

People are added to the queues according to increasing days.

Example:

```text
Day 1
Day 2
Day 3
Day 4
...
```

Therefore the earliest event is always at:

```text
queue[0]
```

We can remove it using:

```python
popleft()
```

Once the front person is not ready yet, later people are also not ready.

This allows us to process events efficiently.

---

# Why Don't We Store Every Person?

Suppose:

```text
1 million people
```

know the secret.

We don't store:

```text
person 1
person 2
person 3
...
```

Instead we group people who learned on the same day:

```text
(day, people)
```

For example:

```text
(5, 1000)
```

means:

```text
1000 people learned the secret on day 5.
```

This is much more efficient.

---

# Why Is `curr` Updated When People Forget?

Suppose:

```text
curr = 10
```

and:

```text
3 people forget
```

Those 3 people cannot spread anymore.

So:

```python
curr -= 3
```

becomes:

```text
curr = 7
```

This is why we do:

```python
curr = (curr - people) % M
```

---

# Why Is `ans` Updated When People Forget?

`ans` represents everyone who remembers.

If 3 people forget:

```python
ans -= 3
```

because they no longer know the secret.

So:

```text
ans
↓
Total people remembering

curr
↓
People remembering who can spread
```

---

# Important Difference

Remember this:

```text
ans
=
Total people who know the secret
```

```text
curr
=
People who know the secret AND can currently spread
```

A person can be:

```text
Knowing the secret
but
Not yet allowed to spread
```

because of `delay`.

---

# Why Use Modulo?

The number of people can become extremely large.

So we use:

```python
M = 10**9 + 7
```

and perform:

```python
ans = (ans + curr) % M
```

and:

```python
curr = (curr + people) % M
```

This keeps the numbers manageable and matches the problem requirement.

---

# Common Mistakes

### 1. Treating `curr` as Total People

Wrong understanding:

```text
curr = everyone who knows the secret
```

Correct:

```text
curr = people who can currently spread
```

---

### 2. Forgetting to Remove People

People eventually forget.

So we must process:

```python
forgetQ
```

before calculating new spreaders.

---

### 3. Adding New People Only to `delayQ`

Wrong:

```python
delayQ.append((i, curr))
```

New people also need to be tracked until they forget.

So add them to both:

```python
delayQ.append((i, curr))
forgetQ.append((i, curr))
```

---

### 4. Using `if` Instead of `while`

There can be multiple groups ready to:

```text
forget
```

or:

```text
become active
```

A robust implementation generally processes all eligible groups:

```python
while forgetQ and forgetQ[0][0] + forget <= i:
    ...
```

and:

```python
while delayQ and delayQ[0][0] + delay <= i:
    ...
```

Your current code uses `if`, which works for the way these grouped events are generated, but the core idea to remember is:

```text
Process every event whose time has arrived.
```

---

# Complexity

Let `n` be the number of days.

Each day's grouped events are processed through the queues.

```text
Time  → O(n)
Space → O(n)
```

We store grouped information by day rather than individual people.

---

# Revision Cheat Sheet

```text
People Aware of a Secret

Pattern:
Queue + Simulation + Sliding Window

ans:
Total people who currently remember.

curr:
People who currently remember AND can spread.

delayQ:
People waiting for their sharing delay.

forgetQ:
People waiting to forget.

Store:
(day learned, number of people)

For each day:

1. Remove people who forget:

   day + forget <= i

   ans -= people
   curr -= people

2. Activate people whose delay is over:

   day + delay <= i

   curr += people

3. Active people spread:

   ans += curr

   Add new people to:

   delayQ
   forgetQ

Why two queues?

delayQ:
Tracks when people can START spreading.

forgetQ:
Tracks when people STOP knowing the secret.

Why store day?

Because future events depend on:

day + delay
day + forget

Why group people?

People who learn on the same day have
the same future timeline.

Why Queue?

Events happen in increasing day order,
so the oldest event is always at the front.

Modulo:

10^9 + 7

Time:
O(n)

Space:
O(n)
```

---

# One-Line Pattern

```text
Group people by the day they learn → use one queue for when they start spreading and another for when they forget → maintain active spreaders and total people. 
```