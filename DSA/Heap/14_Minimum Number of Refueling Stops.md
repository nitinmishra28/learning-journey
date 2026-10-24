# Minimum Number of Refueling Stops

## 1. Problem

You are driving toward a target located `target` miles away.

- `startFuel` represents the fuel available initially.
- `stations[i] = [position, fuel]` represents a gas station at a given position that provides a certain amount of fuel.
- The car consumes 1 unit of fuel per mile.
- The car starts at position `0`.
- We need to find the **minimum number of refueling stops** required to reach the target.

If reaching the target is impossible, return `-1`.

### Example

**Input:**

```python
target = 100
startFuel = 10
stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
```

**Output:**

```python
2
```

**Explanation:**

1. Start with 10 units of fuel and reach station at position `10`.
2. Refuel with 60 units at position `10`.
3. Reach station at position `60` with 10 units of fuel remaining.
4. Refuel with 40 units at position `60`.
5. Reach the target at position `100`.

We make only **2 refueling stops**.

---

## 2. Brute Force Approach

### Idea

Try different combinations of gas stations and calculate how many refueling stops are needed for each combination.

We could explore both choices at every station:

- Refuel at the station.
- Skip the station.

Then select the minimum number of stops that allows us to reach the target.

### Why is it inefficient?

For `n` stations, there can be up to \(2^n\) different combinations of refueling decisions.

### Complexity

- **Time Complexity:** `O(2^n)` in a basic recursive solution.
- **Space Complexity:** `O(n)` for the recursion stack.

We can optimize this using a **Greedy Algorithm + Max Heap**.

---

## 3. Optimized Approach: Greedy + Max Heap

### Pattern

**Greedy + Max Heap + Delayed Decision Making**

### Main Idea

Our goal is to reach the target using the minimum number of refueling stops.

The key observation is:

**We do not need to decide immediately whether to refuel at a station. We can remember the fuel available at stations we have already passed and refuel from the largest available fuel amount only when necessary.**

Why?

Suppose we have passed these stations:

| Station | Available Fuel |
|---|---:|
| Station A | 20 |
| Station B | 50 |
| Station C | 30 |

When we run out of fuel before reaching the next station, we should choose the largest available fuel amount first.

Instead of making three small refueling stops, we may be able to make fewer stops by choosing the largest fuel amount.

We use a **Max Heap** to retrieve the largest available fuel amount efficiently.

Python's `heapq` is a Min Heap, so we store negative fuel values to simulate a Max Heap.

```python
heapq.heappush(max_heap, -stationFuel)
```

When we need fuel:

```python
fuel += -heapq.heappop(max_heap)
stops += 1
```

The heap stores fuel from stations we have already reached, but we only use that fuel when we need it.

---

## 4. Complete Code

```python
import heapq

class Solution:
    def minRefuelStops(
        self,
        target: int,
        startFuel: int,
        stations: list[list[int]]
    ) -> int:

        max_heap = []
        fuel = startFuel
        stops = 0

        # Add the target as a final destination with zero fuel.
        for pos, stationFuel in stations + [[target, 0]]:

            # Refuel until we can reach the current position.
            while fuel < pos:

                # No previously passed station can provide fuel.
                if not max_heap:
                    return -1

                # Choose the largest available fuel amount.
                fuel += -heapq.heappop(max_heap)
                stops += 1

            # Remember the current station's fuel for later.
            heapq.heappush(max_heap, -stationFuel)

        return stops
```

---

## 5. Understanding the Important Variables

### `fuel`

```python
fuel = startFuel
```

Tracks the **farthest position the car can currently reach** from the starting point, assuming we use the fuel we've already collected.

For example:

```python
fuel = 50
```

means the car can reach position `50` without making any additional refueling stops.

### `stops`

```python
stops = 0
```

Counts how many times we actually refuel.

Adding fuel to the heap does not increase `stops`. A stop is counted only when we remove fuel from the heap and use it.

### `max_heap`

```python
max_heap = []
```

Stores negative fuel amounts from stations we have already reached.

It allows us to choose the largest available fuel amount whenever we need to refuel.

---

## 6. Dry Run

Consider:

```python
target = 100
startFuel = 10
stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
```

The code processes:

```python
stations + [[target, 0]]
```

So the complete list becomes:

```python
[[10, 60], [20, 30], [30, 30], [60, 40], [100, 0]]
```

The final `[100, 0]` represents the target. It lets us use the same logic to check whether we can reach the destination.

### Initial State

```python
fuel = 10
stops = 0
max_heap = []
```

The car can reach position `10`.

### Step 1: Station `[10, 60]`

Current station position:

```python
pos = 10
```

Check:

```python
fuel < pos
10 < 10  # False
```

We can reach the station, so no refueling is necessary yet.

Add its fuel to the heap:

```python
heapq.heappush(max_heap, -60)
```

State:

```python
fuel = 10
stops = 0
max_heap = [-60]
```

**Important:** We remember the 60 units of fuel without using them yet.

### Step 2: Station `[20, 30]`

Current position:

```python
pos = 20
```

Check:

```python
fuel < pos
10 < 20  # True
```

We cannot reach position `20` with the current fuel.

We need to refuel.

The heap contains:

```python
[-60]
```

Remove the largest available fuel amount:

```python
fuel += -heapq.heappop(max_heap)
```

Calculation:

```python
fuel = 10 + 60
fuel = 70
stops = 1
```

Now:

```python
70 < 20  # False
```

We can reach station `20`.

Add its fuel to the heap:

```python
heapq.heappush(max_heap, -30)
```

State:

```python
fuel = 70
stops = 1
max_heap = [-30]
```

### Step 3: Station `[30, 30]`

Check:

```python
70 < 30  # False
```

We can reach station `30` without refueling.

Add its fuel:

```python
heapq.heappush(max_heap, -30)
```

State:

```python
fuel = 70
stops = 1
max_heap = [-30, -30]
```

We now have fuel amounts of `30` and `30` available from the stations we have passed.

### Step 4: Station `[60, 40]`

Check:

```python
70 < 60  # False
```

We can reach station `60` without another stop.

Add its fuel:

```python
heapq.heappush(max_heap, -40)
```

State:

```python
fuel = 70
stops = 1
max_heap = [-40, -30, -30]
```

We have not used the 30, 30, or 40 fuel amounts yet.

### Step 5: Target `[100, 0]`

Current position:

```python
pos = 100
```

Check:

```python
70 < 100  # True
```

We cannot reach the target yet.

The heap contains:

```python
[-40, -30, -30]
```

The largest available fuel amount is `40`.

Use it:

```python
fuel = 70 + 40
fuel = 110
stops = 2
```

Now:

```python
110 < 100  # False
```

We can reach the target.

The loop finishes and returns:

```python
2
```

### Final Result

```python
2
```

We refueled at the stations providing `60` and `40` units of fuel.

---

## 7. Why Do We Add Fuel to the Heap Without Immediately Refueling?

This is the most important idea in this problem.

Consider:

```python
heapq.heappush(max_heap, -stationFuel)
```

We are **not refueling at the current station**. We are saving its fuel amount as an option for later.

Why delay the decision?

Because we want to minimize the number of stops, not necessarily refuel at every station.

For example, if the car can already reach the next station, we should keep moving. When we eventually cannot reach a station or the target, we can select the largest fuel amount among all the stations we have already passed.

This greedy strategy makes each refueling stop as useful as possible.

**Important:** The heap contains only fuel from stations we have already reached. We must never use fuel from a station we have not reached yet.

---

## 8. Why Do We Use a Max Heap Instead of a Min Heap?

Suppose the heap contains these available fuel amounts:

```python
[20, 50, 30]
```

We need to choose which fuel amount to use when we cannot continue.

A Max Heap lets us choose `50` first.

If we choose `20` first, we might need to make another refueling stop later even though we could have used `50` instead.

By choosing the largest available fuel amount, we maximize how far each stop can take us.

### Python's Negative-Number Trick

Python's `heapq` is a Min Heap, so we store:

```python
-20
-50
-30
```

The heap becomes:

```python
[-50, -20, -30]
```

The smallest negative number is `-50`.

Therefore:

```python
heapq.heappop(max_heap)
```

returns `-50`, and:

```python
-heapq.heappop(max_heap)
```

gives us the actual fuel amount `50`.

---

## 9. Why Do We Use `while fuel < pos` Instead of `if fuel < pos`?

```python
while fuel < pos:
```

We use `while` because we may need multiple refueling stops to reach the next station or target.

For example:

```python
fuel = 20
pos = 100
max_heap = [-40, -30, -20]
```

We cannot reach position `100` with 20 units of fuel.

First refuel:

```python
fuel = 20 + 40  # 60
```

Still cannot reach position `100`.

Second refuel:

```python
fuel = 60 + 30  # 90
```

Still cannot reach position `100`.

Third refuel:

```python
fuel = 90 + 20  # 110
```

Now we can reach position `100`.

A single `if` would attempt only one refueling operation. The `while` loop continues until we can reach the current position or no fuel options remain.

---

## 10. Why Do We Return `-1`?

```python
if not max_heap:
    return -1
```

If we cannot reach the current station or target and the heap is empty, there are no previously reached stations from which we can take fuel.

Therefore, reaching the destination is impossible.

Example:

```python
target = 100
startFuel = 10
stations = []
```

The car can reach only position `10`, and there are no stations available.

When the algorithm tries to reach position `100`, the heap is empty, so it returns:

```python
-1
```

---

## 11. Why Append `[target, 0]`?

```python
for pos, stationFuel in stations + [[target, 0]]:
```

We add the target as a final station with zero fuel.

This means the target is processed using the same logic as every other position.

If the car cannot reach the target, the `while` loop attempts to refuel from the heap.

If no fuel is available, the algorithm returns `-1`.

If the car can reach the target, the loop finishes and the algorithm returns the number of stops.

This avoids writing a separate block of code just to check whether the destination is reachable.

---

## 12. Complexity Analysis

Let:

- `n` = number of gas stations.
- `k` = number of stations whose fuel amounts are stored in the heap at a particular time.

### Time Complexity: `O(n log n)`

Each station is processed once and its fuel is pushed into the heap.

Each station's fuel can also be popped at most once.

Each heap insertion or removal costs at most `O(log n)`.

Therefore, the overall time complexity is:

\[
O(n \log n)
\]

### Space Complexity: `O(n)`

The heap can contain fuel amounts from up to `n` stations.

The expression:

```python
stations + [[target, 0]]
```

also creates a new list containing the stations and the target.

Therefore, the total auxiliary space complexity is:

\[
O(n)
\]

---

## 13. Common Mistakes

### Mistake 1: Refueling immediately at every station

This may increase the number of stops unnecessarily.

Instead, save fuel amounts in the heap and refuel only when necessary.

### Mistake 2: Using a Min Heap with positive fuel values

This would choose the smallest fuel amount first.

Use negative fuel values to simulate a Max Heap.

### Mistake 3: Forgetting to increment `stops`

Every time we actually take fuel from the heap, we make one refueling stop.

```python
fuel += -heapq.heappop(max_heap)
stops += 1
```

### Mistake 4: Using `if` instead of `while`

We may need several refueling stops before reaching the current position.

### Mistake 5: Adding fuel from an unreachable station

A station's fuel should be added to the heap only after the car can reach that station.

The current code correctly checks reachability before pushing the station's fuel.

---

## 14. Brute Force vs Optimized

| Feature | Brute Force | Greedy + Max Heap |
|---|---|---|
| Approach | Try combinations of stations | Choose the largest available fuel when needed |
| Time Complexity | `O(2^n)` in basic recursion | `O(n log n)` |
| Space Complexity | `O(n)` recursion stack | `O(n)` |
| Decision | Explore refuel/skip choices | Delay decisions until fuel is needed |
| Best use | Understanding all possibilities | Efficient solution |

---

## 15. Revision Cheat Sheet

- **Problem:** Reach the target with the minimum refueling stops.
- **Pattern:** Greedy + Max Heap.
- **Greedy Choice:** Use the largest available fuel amount when refueling becomes necessary.
- **Heap Trick:** Store negative fuel amounts to simulate a Max Heap.
- **Important Condition:** `while fuel < pos`.
- **Impossible Case:** If fuel is insufficient and the heap is empty, return `-1`.
- **Target Trick:** Append `[target, 0]` to process the destination like a station.
- **Time Complexity:** `O(n log n)`.
- **Space Complexity:** `O(n)`.

> **One-Line Pattern:** Minimum Refueling Stops = Greedy + Max Heap + Save Fuel from Reached Stations + Refuel with the Largest Available Amount Only When Necessary.