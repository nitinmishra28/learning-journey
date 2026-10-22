# Task Scheduler (LeetCode 621)

## 1. Problem

You are given a list of CPU tasks represented by uppercase letters and a non-negative integer `n`.

The CPU must follow these rules:

- Each task takes exactly **one unit of time**.
- The same task must have at least `n` intervals between two executions.
- The CPU can execute tasks in any order.
- If no task can be executed because of the cooldown restriction, the CPU remains idle.

Return the **minimum number of time intervals** required to complete all tasks.

### Example

```python
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2

Output: 8
```

One possible schedule:

```text
A → B → Idle → A → B → Idle → A → B
```

The same task has two intervals between consecutive executions.

Total time = `8`.

---

## 2. Brute Force Approach

### Idea

Simulate the CPU one time interval at a time.

At every interval:

1. Find a task that is available to execute.
2. Prefer the task with the highest remaining frequency.
3. Execute it and decrease its remaining frequency.
4. Track when that task becomes available again.
5. If no task is available, execute an idle interval.

This approach requires tracking task frequencies and their cooldown times.

### Why Is It More Complicated?

We must maintain both the remaining frequency and the next time each task can execute.

A priority queue and cooldown queue provide a more organized way to simulate this process.

**Optimization:** Use a Max Heap to select the most frequent available task and process tasks in cycles of length `n + 1`.

---

## 3. Pattern: Greedy + Max Heap + Cooldown Cycles

The key idea is to execute the most frequent remaining tasks first.

Why?

If a task appears many times, it is more likely to cause idle intervals because its executions must be separated by cooldown periods.

Executing frequent tasks first helps us distribute different tasks between repeated executions.

We group execution into cycles of length:

```python
cycle = n + 1
```

For example, when `n = 2`:

```text
Cycle length = 2 + 1 = 3

[A, B, C]
```

Within this cycle, each task can execute at most once.

If fewer than `n + 1` tasks are available, the remaining intervals may be idle.

---

## 4. Main Idea

### Step 1: Count task frequencies

```python
freq = Counter(tasks)
```

For:

```python
tasks = ["A", "A", "A", "B", "B", "B"]
```

The frequency map becomes:

```python
{
    "A": 3,
    "B": 3
}
```

### Step 2: Build a Max Heap

```python
max_heap = [-count for count in freq.values()]
heapq.heapify(max_heap)
```

Python's `heapq` is a Min Heap.

We store negative frequencies to simulate a Max Heap, so the task with the highest remaining frequency is selected first.

For example:

```python
freq = [3, 3]

max_heap = [-3, -3]
```

The root `-3` represents a remaining frequency of `3`.

### Step 3: Start a cycle

```python
cycle = n + 1
temp = []
```

`cycle` determines how many intervals we process in one group.

`temp` temporarily stores tasks that still have remaining executions.

### Step 4: Execute tasks in the cycle

```python
for _ in range(cycle):
    if max_heap:
        count = heapq.heappop(max_heap)
        count += 1

        if count < 0:
            temp.append(count)

    time += 1

    if not max_heap and not temp:
        break
```

Let's understand the important operations.

**Pop the most frequent task:**

```python
count = heapq.heappop(max_heap)
```

Because the heap stores negative frequencies, the root corresponds to the most frequent remaining task.

**Decrease its frequency:**

```python
count += 1
```

Suppose the stored frequency is `-3`.

After executing the task once:

```text
-3 + 1 = -2
```

The task still needs two more executions.

We add `1` because the frequency is stored as a negative number.

**Store unfinished tasks temporarily:**

```python
if count < 0:
    temp.append(count)
```

If the frequency is still negative, the task has more executions remaining.

We do not immediately put it back into the heap because the same task must not execute again during the current cycle.

### Step 5: Count time, including idle intervals

```python
time += 1
```

Every loop iteration consumes one time interval.

If the heap is empty but tasks remain in `temp`, those tasks are waiting for the next cycle. The remaining intervals in the current cycle count as idle time.

### Step 6: Restore unfinished tasks

```python
for count in temp:
    heapq.heappush(max_heap, count)
```

After the current cycle finishes, put unfinished tasks back into the heap.

They can now compete for execution in the next cycle.

---

## 5. Complete Code with Comments

```python
from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

        # Step 1: Count the frequency of each task
        freq = Counter(tasks)

        # Step 2: Build a Max Heap using negative frequencies
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)

        time = 0

        # Continue until every task has been completed
        while max_heap:

            # Temporarily store unfinished tasks
            temp = []

            # Each cycle has n + 1 intervals
            cycle = n + 1

            # Process one cycle
            for _ in range(cycle):

                # Execute a task if one is available
                if max_heap:
                    count = heapq.heappop(max_heap)

                    # One execution reduces its remaining frequency
                    count += 1

                    # Store the task if more executions remain
                    if count < 0:
                        temp.append(count)

                # Count task execution or idle time
                time += 1

                # Stop early if every task is completed
                if not max_heap and not temp:
                    break

            # Restore unfinished tasks for the next cycle
            for count in temp:
                heapq.heappush(max_heap, count)

        return time
```

---

## 6. Dry Run

Consider:

```python
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
```

Initial frequencies:

```text
A = 3
B = 3
```

The heap stores:

```python
[-3, -3]
```

The cycle length is:

```python
cycle = n + 1
      = 2 + 1
      = 3
```

### Cycle 1

Execute `A`, then `B`.

Their frequencies decrease:

```text
A: 3 → 2
B: 3 → 2
```

After three intervals:

```text
A → B → Idle
```

The heap is empty during the final interval, but unfinished tasks remain in `temp`.

```text
time = 3
temp = [-2, -2]
```

Restore the unfinished tasks to the heap.

### Cycle 2

Execute `A`, then `B` again.

```text
A: 2 → 1
B: 2 → 1
```

Schedule:

```text
A → B → Idle
```

Now:

```text
time = 6
temp = [-1, -1]
```

Restore the unfinished tasks.

### Cycle 3

Execute the remaining `A` and `B`.

```text
A: 1 → 0
B: 1 → 0
```

Both tasks are completed, so the loop stops early instead of counting an unnecessary third interval.

Schedule:

```text
A → B
```

Total schedule:

```text
A → B → Idle → A → B → Idle → A → B
```

Therefore:

```python
Output: 8
```

---

## 7. Why Do We Use `temp`?

Consider this code:

```python
count = heapq.heappop(max_heap)
count += 1

if count < 0:
    temp.append(count)
```

Why not immediately push the unfinished task back into the heap?

Because it could be selected again in the same cycle.

For example, suppose:

```text
A = 3
B = 1
n = 2
```

If we immediately reinsert `A` after executing it, it could be selected again before the cooldown period has passed.

By storing unfinished tasks in `temp`, we prevent them from being selected again during the current cycle.

At the end of the cycle:

```python
for count in temp:
    heapq.heappush(max_heap, count)
```

The tasks become available for selection in the next cycle.

**Remember:** `temp` is not a permanent cooldown queue. It temporarily holds unfinished tasks until the current cycle finishes.

---

## 8. Why Is the Cycle Length `n + 1`?

The cooldown `n` specifies how many intervals must separate two executions of the same task.

For example, when `n = 2`:

```text
A → B → Idle → A
```

There are two intervals (`B` and `Idle`) between the two executions of `A`.

The cycle length is therefore:

```python
n + 1
```

The extra `1` represents the interval in which the task itself executes.

### Special Case: `n = 0`

```python
cycle = 0 + 1
      = 1
```

Every task can execute immediately after the previous one.

No idle intervals are needed.

The algorithm correctly processes one task per cycle until all tasks are completed.

---

## 9. Complexity Analysis

Let:
- `N` = total number of tasks.
- `K` = number of distinct task types.
- `n` = cooldown interval.

### Time Complexity

- Counting frequencies: `O(N)`
- Building the heap: `O(K)`
- Heap operations: `O(N log K)` overall, because every task execution causes at most one pop and each unfinished task is pushed back.

**Total time:** `O(N log K)`.

### Space Complexity

- Frequency map: `O(K)`
- Max Heap: `O(K)`
- Temporary list: `O(K)`

**Auxiliary space:** `O(K)`.

---

## 10. Common Mistakes

1. **Using positive frequencies in `heapq`:** Python would select the smallest frequency first. Use negative frequencies.
2. **Decreasing a negative frequency incorrectly:** Use `count += 1`, not `count -= 1`.
3. **Reinserting unfinished tasks immediately:** This can allow the same task to execute more than once in the current cycle.
4. **Forgetting idle intervals:** Every cycle iteration increases `time`, even when the heap is empty.
5. **Always counting the entire final cycle:** Break early when both `max_heap` and `temp` are empty.
6. **Confusing frequency with time:** The heap stores remaining task counts, while `time` stores total elapsed intervals.

---

## 11. Brute Force vs Optimized Approach

| Feature | Direct Simulation | Max Heap + Cycles |
|---|---|---|
| Task selection | Search for an available task | Pop highest remaining frequency |
| Cooldown handling | Track availability times | Temporarily remove tasks for the current cycle |
| Idle intervals | Explicitly simulate | Count empty cycle slots |
| Time complexity | Depends on task-selection implementation | `O(N log K)` |
| Space complexity | Depends on cooldown tracking | `O(K)` |

The heap-and-cycle approach makes the greedy task selection efficient and prevents repeated execution of the same task within a cycle.

---

## 12. Pattern Recognition

Recognize **Greedy + Max Heap + Cooldown Cycles** when:

- Tasks have different frequencies.
- Repeating a task too soon is prohibited.
- You want to minimize idle time.
- The most frequent tasks are most likely to determine the schedule length.

The general approach is:

1. Count task frequencies.
2. Put negative frequencies into a Max Heap.
3. Process tasks in cycles of length `n + 1`.
4. Temporarily hold unfinished tasks.
5. Count every execution and idle interval.
6. Restore unfinished tasks after each cycle.

---

## 13. Revision Cheat Sheet

- **Frequency map:** `Counter(tasks)`
- **Max Heap:** Negative task frequencies.
- **Cycle length:** `n + 1`
- **Task execution:** `count += 1`
- **Unfinished task:** `count < 0`
- **Temporary storage:** Prevents repeating a task in the same cycle.
- **Idle time:** Counted when a cycle slot has no available task.
- **Early stop:** No tasks remain in either the heap or `temp`.
- **Time:** `O(N log K)`
- **Space:** `O(K)`

> **One-Line Pattern:** Task Scheduler = Greedy + Max Heap + Cycles of Size `n + 1` + Temporarily Hold Unfinished Tasks to Respect Cooldown.