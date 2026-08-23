# Reveal Cards In Increasing Order

## Problem

You are given a deck of cards.

You can perform the following operations:

1. Reveal the top card.
2. Move the next top card to the bottom.
3. Repeat until all cards are revealed.

We need to arrange the deck so that the revealed cards appear in:

```text
Increasing order
```

### Example

Input:

```text
deck = [17, 13, 11, 2, 3, 5, 7]
```

Output:

```text
[2, 13, 3, 11, 5, 17, 7]
```

If we follow the reveal process:

```text
2 → 3 → 5 → 7 → 11 → 13 → 17
```

The cards are revealed in increasing order.

---

# Pattern

```text
Queue + Simulation + Index Mapping
```

---

# Main Idea

The important trick is:

> We don't simulate the cards themselves. We simulate the positions where the cards need to be placed.

First sort the cards:

```python
deck.sort()
```

Now the cards are in the order in which we want them to be revealed:

```text
[2, 3, 5, 7, 11, 13, 17]
```

We need to determine:

```text
Which position should contain each card?
```

For this, we use a queue of indices.

```python
idx = deque(range(len(deck)))
```

For 7 cards:

```text
[0, 1, 2, 3, 4, 5, 6]
```

---

# Why Are We Storing Indices?

This is the most important idea.

We already know the cards should be revealed in sorted order:

```text
2 → 3 → 5 → 7 → 11 → 13 → 17
```

But we don't know where these cards should be placed in the final array.

So instead of moving the actual cards, we maintain the positions:

```text
0, 1, 2, 3, 4, 5, 6
```

The queue simulates:

```text
Which position will be revealed next?
```

Then:

```python
ans[idx[0]] = deck[i]
```

means:

> Put the next smallest card into the position that will be revealed next.

---

# Why Use a Queue?

The actual reveal process is:

```text
Reveal front card
Move next card to the back
```

This is exactly queue behavior:

```text
Front → remove
Rear  → add
```

So `deque` is perfect for simulating the positions.

---

# Step 1: Sort the Deck

```python
deck.sort()
```

Example:

```text
Original:

[17, 13, 11, 2, 3, 5, 7]

Sorted:

[2, 3, 5, 7, 11, 13, 17]
```

We process the cards from smallest to largest.

---

# Step 2: Create Index Queue

```python
idx = deque(range(len(deck)))
```

For 7 cards:

```text
idx = [0, 1, 2, 3, 4, 5, 6]
```

This represents:

```text
Positions waiting to receive cards
```

---

# Step 3: Create Answer Array

```python
ans = [0] * len(deck)
```

Initially:

```text
ans = [0, 0, 0, 0, 0, 0, 0]
```

---

# Step 4: Put Smallest Card at Front Position

```python
ans[idx[0]] = deck[i]
```

Initially:

```text
idx = [0, 1, 2, 3, 4, 5, 6]
```

The smallest card is:

```text
2
```

So:

```text
ans[0] = 2
```

Now:

```text
ans = [2, 0, 0, 0, 0, 0, 0]
```

Remove that position:

```python
idx.popleft()
```

Now:

```text
idx = [1, 2, 3, 4, 5, 6]
```

---

# Step 5: Simulate Moving the Next Card to the Bottom

After revealing the top card, the original process says:

```text
Move the next card to the bottom.
```

We simulate this with indices:

```python
if idx:
    idx.append(idx[0])
    idx.popleft()
```

Suppose:

```text
idx = [1, 2, 3, 4, 5, 6]
```

Move the front index `1` to the back:

```text
[2, 3, 4, 5, 6, 1]
```

This exactly represents:

```text
Remove top position
Move next position to bottom
```

---

# Why Do We Do This After `popleft()`?

First:

```python
idx.popleft()
```

removes the position where we just placed the card.

Then:

```python
idx.append(idx[0])
idx.popleft()
```

moves the next position to the back.

So the sequence is:

```text
1. Use front position
2. Remove it
3. Move next position to back
```

This matches the original deck operation.

---

# Complete Example

Take:

```text
deck = [17, 13, 11, 2, 3, 5, 7]
```

After sorting:

```text
deck = [2, 3, 5, 7, 11, 13, 17]
```

Initial indices:

```text
idx = [0, 1, 2, 3, 4, 5, 6]
```

---

## Put `2`

Front index:

```text
0
```

So:

```text
ans[0] = 2
```

Remove `0`:

```text
[1, 2, 3, 4, 5, 6]
```

Move `1` to back:

```text
[2, 3, 4, 5, 6, 1]
```

---

## Put `3`

Front index:

```text
2
```

So:

```text
ans[2] = 3
```

Remove `2`:

```text
[3, 4, 5, 6, 1]
```

Move `3` to back:

```text
[4, 5, 6, 1, 3]
```

---

## Put `5`

Front index:

```text
4
```

So:

```text
ans[4] = 5
```

Then:

```text
idx = [5, 6, 1, 3]
```

Move `5` to back:

```text
[6, 1, 3, 5]
```

---

Continue the same process.

Final answer:

```text
[2, 13, 3, 11, 5, 17, 7]
```

---

# Code

```python
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        # Sort cards because they must be revealed
        # in increasing order
        deck.sort()

        # Queue of positions
        idx = deque(range(len(deck)))

        # Final arrangement
        ans = [0] * len(deck)

        for i in range(len(deck)):

            # Put smallest remaining card
            # at the next reveal position
            ans[idx[0]] = deck[i]

            # Remove that position
            idx.popleft()

            # Simulate:
            # move next position to the back
            if idx:
                idx.append(idx[0])
                idx.popleft()

        return ans
```

---

# Important Concept

There are actually **two different things** being simulated.

### Cards

Sorted:

```text
2 → 3 → 5 → 7 → 11 → 13 → 17
```

### Positions

Managed by:

```python
idx
```

The position queue tells us:

```text
Where should the next smallest card go?
```

So:

```text
Sorted cards
      ↓
Next smallest card
      ↓
Next reveal position
      ↓
Place card there
```

---

# Why Don't We Put Cards Directly Into the Queue?

Because if we put cards directly into the queue, we would need to reverse-engineer the arrangement.

Using indices makes the problem much easier.

We simulate the **reveal order of positions first**.

Then assign the sorted cards to those positions.

This is a common technique:

```text
Simulate positions
+
Assign sorted values
```

---

# Common Mistakes

## 1. Forgetting to Sort

We need cards to be revealed in increasing order.

So:

```python
deck.sort()
```

is necessary.

---

## 2. Using Card Values Instead of Indices

The queue should contain:

```text
indices
```

not:

```text
card values
```

Because we are trying to determine where each card belongs.

---

## 3. Moving the Wrong Index

After placing a card:

```python
idx.popleft()
```

Then the next position must move to the back:

```python
idx.append(idx[0])
idx.popleft()
```

This simulates:

```text
Reveal top
Move next top to bottom
```

---

# Complexity

Sorting:

```text
O(n log n)
```

Index simulation:

```text
O(n)
```

Overall:

```text
Time → O(n log n)
Space → O(n)
```

---

# Revision Cheat Sheet

```text
Deck Revealed Increasing

Pattern:
Queue + Simulation + Index Mapping

Main Trick:

1. Sort the deck.
2. Create a queue of indices.
3. The front index represents the next position
   that will be revealed.
4. Put the smallest remaining card there.
5. Remove that index.
6. Move the next index to the back.

Why store indices?

We know the order of cards to reveal,
but we need to find their positions
in the final array.

Why Queue?

Reveal:
remove from front

Move next card:
front → back

So deque naturally simulates the process.

Code:

deck.sort()

idx = deque(range(len(deck)))
ans = [0] * len(deck)

for i in range(len(deck)):

    ans[idx[0]] = deck[i]
    idx.popleft()

    if idx:
        idx.append(idx[0])
        idx.popleft()

Complexity:

Time  → O(n log n)
Space → O(n)
```

---

# One-Line Pattern

```text
Sort the values, simulate the reveal order using a queue of indices, and place each smallest value at the next position that would be revealed.
```