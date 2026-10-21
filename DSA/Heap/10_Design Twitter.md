# Design Twitter

## 1. Problem

Design a simplified Twitter system that supports four operations:

- `postTweet(userId, tweetId)`: Create a tweet for a user.
- `getNewsFeed(userId)`: Return the 10 most recent tweets from the user and the people they follow.
- `follow(followerId, followeeId)`: Make one user follow another.
- `unfollow(followerId, followeeId)`: Remove a follow relationship.

The news feed must display tweets in **reverse chronological order**, meaning the newest tweets appear first.

### Example

```python
twitter = Twitter()

twitter.postTweet(1, 101)
twitter.postTweet(1, 102)
twitter.postTweet(2, 201)

twitter.follow(1, 2)

twitter.getNewsFeed(1)
# Possible output: [201, 102, 101]
```

User `1` follows user `2`, so their news feed contains tweets from both users, ordered from newest to oldest.

---

## 2. Brute Force Approach

### Idea

For `getNewsFeed(userId)`:

1. Get the user and all the users they follow.
2. Collect all their tweets.
3. Sort the collected tweets by timestamp in descending order.
4. Return the tweet IDs of the first 10 tweets.

### Code

```python
def getNewsFeed(self, userId: int) -> list[int]:
    users = self.following[userId] | {userId}
    all_tweets = []

    for uid in users:
        all_tweets.extend(self.tweets[uid])

    all_tweets.sort(reverse=True)

    return [tweetId for time, tweetId in all_tweets[:10]]
```

### Complexity

Let:
- `F` = number of users followed by the requesting user.
- `T` = total number of tweets belonging to those users and the requesting user.

- Collect tweets: `O(T)`
- Sort tweets: `O(T log T)`
- **Total time:** `O(T log T)`
- **Space:** `O(T)` for the collected tweets

### Why Is It Slow?

The feed only needs 10 tweets, but brute force collects and sorts every tweet from all relevant users.

**Optimization:** Use a Max Heap to merge the already time-ordered tweet lists without sorting all tweets.

---

## 3. Pattern: Heap + K-Way Merge

The main pattern is similar to **Merge K Sorted Lists**.

Each user's tweets are stored in chronological order:

```text
User 1: [101, 102, 105]
User 2: [201, 204]
User 3: [301, 303, 307]
```

The newest tweet from each user is at the end of their list.

Instead of putting every tweet into the heap, we initially insert only the newest tweet from each relevant user.

```text
                  Relevant Users
                        |
                        v
            Get the newest tweet per user
                        |
                        v
                 Insert into heap
                        |
                        v
             Pop the newest available tweet
                        |
                        v
                Add tweet ID to feed
                        |
                        v
          Insert the previous tweet from
                 the same user
                        |
                        v
             Repeat until 10 tweets
```

This is a **K-way merge using a heap**, where each user's tweet history is a sorted list.

---

## 4. Main Idea

### Step 1: Maintain a global timestamp

```python
self.time = 0
```

Every time any user posts a tweet, the timestamp increases.

```python
self.time += 1
self.tweets[userId].append((self.time, tweetId))
```

Each tweet is stored as:

```python
(timestamp, tweetId)
```

For example:

```python
[
    (1, 101),
    (2, 102),
    (5, 105)
]
```

The timestamp tells us the order in which tweets were posted.

**Why use a global timestamp?**

Tweet IDs do not necessarily indicate posting order. A timestamp lets us compare tweets from different users.

### Step 2: Store tweet histories

```python
self.tweets = defaultdict(list)
```

Each user's tweets are stored in a list in posting order.

```text
tweets = {
    1: [(1, 101), (3, 102)],
    2: [(2, 201), (4, 202)]
}
```

The newest tweet is at the end of each list, so we can access it using:

```python
index = len(self.tweets[uid]) - 1
```

### Step 3: Store follow relationships

```python
self.following = defaultdict(set)
```

Each user has a set containing the IDs of users they follow.

```python
self.following[1] = {2, 3}
```

This means user `1` follows users `2` and `3`.

To get the followed users and include the user themselves:

```python
users = self.following[userId] | {userId}
```

The `|` operator performs a set union.

For example:

```python
{2, 3} | {1}
# {1, 2, 3}
```

This ensures that a user's own tweets appear in their news feed even if they follow nobody.

### Step 4: Insert the newest tweet from each user

```python
for uid in users:
    if self.tweets[uid]:
        index = len(self.tweets[uid]) - 1
        time, tweetId = self.tweets[uid][index]

        heapq.heappush(heap, (-time, tweetId, uid, index))
```

Each heap entry has four values:

```python
(-time, tweetId, uid, index)
```

| Value | Purpose |
|---|---|
| `-time` | Makes Python's Min Heap behave like a Max Heap for timestamps |
| `tweetId` | Identifies the tweet |
| `uid` | Identifies the user who posted it |
| `index` | Tracks the tweet's position in that user's list |

We store `-time` because Python's `heapq` is a Min Heap. The most recent tweet has the largest timestamp and therefore the smallest negative timestamp.

Consequently, the newest tweet is popped first.

The `tweetId` also acts as a tie-breaker if timestamps match. Because the global timestamp increases with each post, distinct posts normally have distinct timestamps.

### Step 5: Pop the newest tweet and move backward

```python
while heap and len(result) < 10:
    time, tweetId, uid, index = heapq.heappop(heap)
    result.append(tweetId)

    index -= 1
```

The root contains the newest currently available tweet among the users represented in the heap.

After adding that tweet to the result, we move to the previous tweet from the same user.

```python
if index >= 0:
    time, tweetId = self.tweets[uid][index]
    heapq.heappush(heap, (-time, tweetId, uid, index))
```

We insert the previous tweet only if it exists.

This is the central optimization: **each user contributes at most one tweet to the heap at a time**.

### Step 6: Stop after 10 tweets

```python
while heap and len(result) < 10:
```

We stop when:
- We have collected 10 tweets, or
- The heap becomes empty because no more tweets are available.

---

## 5. Complete Code with Comments

```python
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        # Global timestamp shared by all users
        self.time = 0

        # userId -> list of (timestamp, tweetId)
        self.tweets = defaultdict(list)

        # followerId -> set of followeeIds
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:

        # Assign a unique increasing timestamp
        self.time += 1

        # Store the tweet in chronological order
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:

        heap = []

        # Include followed users and the requesting user
        users = self.following[userId] | {userId}

        # Insert the newest tweet from each relevant user
        for uid in users:

            if self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][index]

                # Negative timestamp simulates a Max Heap
                heapq.heappush(
                    heap,
                    (-time, tweetId, uid, index)
                )

        result = []

        # Collect at most 10 newest tweets
        while heap and len(result) < 10:

            # Pop the newest available tweet
            time, tweetId, uid, index = heapq.heappop(heap)

            result.append(tweetId)

            # Move to the previous tweet from the same user
            index -= 1

            if index >= 0:
                time, tweetId = self.tweets[uid][index]

                # Add the previous tweet to the heap
                heapq.heappush(
                    heap,
                    (-time, tweetId, uid, index)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:

        # A user cannot follow themselves
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        # discard() safely does nothing if followeeId is absent
        self.following[followerId].discard(followeeId)
```

---

## 6. Dry Run

Suppose the following tweets exist:

```text
User 1:
(1, 101), (4, 102)

User 2:
(2, 201), (5, 202)

User 3:
(3, 301), (6, 302)
```

User `1` follows users `2` and `3`.

We want the news feed for user `1`.

### Step 1: Initialize the heap

Take the newest tweet from each user:

```text
User 1 -> (4, 102)
User 2 -> (5, 202)
User 3 -> (6, 302)
```

After inserting negative timestamps, the logical priority order is:

```text
(-6, 302, 3, 1)  <- newest
(-5, 202, 2, 1)
(-4, 102, 1, 1)
```

The heap array itself is not necessarily fully sorted; the root is the highest-priority entry.

### Step 2: Pop the newest tweet

Pop user `3`'s tweet `302`.

```python
result = [302]
```

Move backward in user `3`'s list and insert tweet `301`, timestamp `3`.

### Step 3: Continue merging

The next newest tweet is `202`, timestamp `5`.

```python
result = [302, 202]
```

Then tweet `102`, timestamp `4`:

```python
result = [302, 202, 102]
```

Then tweet `301`, timestamp `3`:

```python
result = [302, 202, 102, 301]
```

Continue popping the newest available tweet and inserting its predecessor until 10 tweets are collected or the heap becomes empty.

The final feed is ordered from newest to oldest:

```python
[302, 202, 102, 301, 201, 101]
```

---

## 7. Why Store the Index in the Heap?

The index tells us which tweet to read next from the same user's history.

For example:

```python
self.tweets[1] = [
    (1, 101),
    (4, 102),
    (7, 103)
]
```

Initially:

```python
index = 2
```

We insert tweet `103` into the heap.

After popping it:

```python
index -= 1  # 1
```

We insert tweet `102`.

After popping that:

```python
index -= 1  # 0
```

We insert tweet `101`.

After that, the index becomes `-1`, so no earlier tweet exists.

Without the index, we would not know where to continue in that user's tweet history.

**Remember:** The index is not a timestamp. It is the position of a tweet in that particular user's list.

---

## 8. Complexity Analysis

Let:
- `F` = number of users followed by the requesting user.
- `U = F + 1` = number of relevant users, including the requesting user.
- `L = min(10, T)` where `T` is the total number of relevant tweets available.

### `postTweet()`

Appending a tweet to a user's list takes amortized `O(1)` time.

- **Time:** `O(1)` amortized
- **Extra space:** `O(1)` per operation, excluding stored tweet history

### `follow()` and `unfollow()`

Set insertion and removal are `O(1)` on average.

- **Time:** `O(1)` average per operation

### `getNewsFeed()`

- Initialize the heap with up to `U` newest tweets: `O(U log U)`.
- Pop up to `L` tweets, with at most one replacement push per pop: `O(L log U)`.

**Total time:**

`O(U log U + L log U)`

Since `L` is at most `10`, this can be written as:

`O(U log U + 10 log U)`

**Auxiliary space:** `O(U)` for the heap, plus `O(L)` for the result list. Since `L <= 10`, the result uses at most 10 entries.

---

## 9. Common Mistakes

1. **Using positive timestamps in a Min Heap:** That would return the oldest tweet first. Use `-time`.
2. **Including only followed users:** Always include the requesting user's own ID.
3. **Pushing every tweet into the heap:** Only insert the newest available tweet from each user, then add that user's previous tweet after popping.
4. **Forgetting the index:** You need it to move backward through the user's tweet list.
5. **Not limiting the feed to 10 tweets:** Use `len(result) < 10`.
6. **Reinserting an invalid index:** Check `index >= 0` before accessing the tweet list.
7. **Using `remove()` for unfollow:** `discard()` is safer because it doesn't raise an error if the relationship doesn't exist.
8. **Allowing self-follow:** Prevent it by checking `followerId != followeeId`.

---

## 10. Brute Force vs Optimized Approach

| Feature | Brute Force | Heap + K-Way Merge |
|---|---|---|
| Gather tweets | All relevant tweets | Newest tweet per user |
| Ordering | Sort all tweets | Heap selects newest |
| Feed retrieval | `O(T log T)` | `O(U log U + L log U)` |
| Extra retrieval space | `O(T)` | `O(U + L)` |
| Stops after 10 tweets | After sorting | As soon as 10 are collected |

The heap approach avoids sorting every tweet and stops once the required feed is complete.

---

## 11. Pattern Recognition

Recognize **Heap + K-Way Merge** when:

- Multiple users each have a sorted list of items.
- You need the globally newest or smallest items across those lists.
- You only need the first `k` results rather than the entire merged list.

The approach is the same general pattern used in Merge K Sorted Lists:

1. Put one current candidate from every list into the heap.
2. Pop the best candidate.
3. Advance only the list that supplied it.
4. Insert its next candidate.
5. Repeat until enough results are collected.

---

## 12. Revision Cheat Sheet

- **Global timestamp:** Establishes posting order across users.
- **Tweets:** Store `(timestamp, tweetId)` in chronological order.
- **Following:** Use a set for each follower.
- **Heap entry:** `(-time, tweetId, uid, index)`.
- **Negative timestamp:** Makes the newest tweet pop first.
- **Index:** Locates the previous tweet in the same user's history.
- **One tweet per user:** Keeps the heap small.
- **Stop condition:** Heap empty or 10 tweets collected.
- **`postTweet()`:** `O(1)` amortized.
- **`follow()` / `unfollow()`:** `O(1)` average.
- **`getNewsFeed()`:** `O(U log U + L log U)`, where `L <= 10`.
- **Heap space:** `O(U)`.

> **One-Line Pattern:** Design Twitter = Global Timestamp + Per-User Sorted Tweet Lists + Max Heap + K-Way Merge to Retrieve the 10 Newest Tweets.