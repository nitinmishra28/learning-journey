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