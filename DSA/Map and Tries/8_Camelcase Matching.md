# Camelcase Matching — Trie + Pattern Matching

## 1. Problem Statement

Given an array of strings `queries` and a string `pattern`, determine whether each query matches the given pattern according to CamelCase matching rules.

A query matches the pattern when:

1. Every character in the pattern must appear in the query in the same order.
2. Additional **lowercase characters** are allowed anywhere in the query.
3. Additional **uppercase characters** are not allowed.
4. All characters of the pattern must be matched.

Return a Boolean list indicating whether each query matches the pattern.

This problem is commonly known as **Camelcase Matching (LeetCode 1023)**.

### Example

**Input:**

```python
queries = [
    "FooBar",
    "FooBarTest",
    "FootBall",
    "FrameBuffer",
    "ForceFeedBack"
]

pattern = "FB"
```

**Output:**

```python
[True, False, True, True, False]
```

### Explanation

| Query | Result | Reason |
|---|---|---|
| `"FooBar"` | `True` | `F` and `B` match; lowercase characters are allowed |
| `"FooBarTest"` | `False` | Extra uppercase `T` |
| `"FootBall"` | `True` | `F` and `B` match in order |
| `"FrameBuffer"` | `True` | `F` and `B` match in order |
| `"ForceFeedBack"` | `False` | Extra uppercase `F` and `B` cannot be ignored |

---

## 2. Approach: Trie + Pattern Matching

We build a Trie using the given pattern.

Then, for every query, we traverse its characters while following these rules:

- If the current character exists in the Trie node's children, move to that child.
- If the character does not exist and it is lowercase, ignore it.
- If the character does not exist and it is uppercase, the query is invalid.
- After processing the entire query, check whether the current Trie node marks the end of the pattern.

### Main Idea

The pattern represents the required sequence of characters.

The query can contain additional lowercase characters, but every uppercase character must match the next required character in the pattern.

---

## 3. Complete Python Code

```python
class Solution:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, pattern):
        node = self

        for char in pattern:
            if char not in node.children:
                node.children[char] = Solution()

            node = node.children[char]

        node.is_end = True

    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        self.insert(pattern)
        ans = []

        for word in queries:
            node = self

            for ch in word:
                if ch in node.children:
                    node = node.children[ch]

                elif ch.islower():
                    continue

                else:
                    break
            else:
                ans.append(node.is_end)
                continue

            ans.append(False)

        return ans
```

---

## 4. Understanding the Trie Structure

### Node Initialization

```python
def __init__(self):
    self.children = {}
    self.is_end = False
```

Each Trie node contains:

- `children`: Dictionary storing the next possible pattern characters.
- `is_end`: Indicates whether the complete pattern ends at this node.

For example, if the pattern is:

```python
pattern = "FB"
```

The Trie looks like:

```text
root
 |
 F
 |
 B  ← is_end = True
```

The Trie represents the required character sequence `"FB"`.

---

## 5. Understanding `insert(pattern)`

### Code

```python
def insert(self, pattern):
    node = self

    for char in pattern:
        if char not in node.children:
            node.children[char] = Solution()

        node = node.children[char]

    node.is_end = True
```

### Step-by-Step Explanation

**Step 1: Start from the root**

```python
node = self
```

**Step 2: Process each pattern character**

```python
for char in pattern:
```

For `"FB"`:

```text
F → B
```

**Step 3: Create a node if the character does not exist**

```python
if char not in node.children:
    node.children[char] = Solution()
```

**Step 4: Move to the child**

```python
node = node.children[char]
```

**Step 5: Mark the end of the pattern**

```python
node.is_end = True
```

This tells us that the complete pattern has been inserted.

### Complexity

Let `P` be the length of the pattern.

- Time: `O(P)` average.
- Space: `O(P)`.

---

## 6. Understanding `camelMatch()`

### Code

```python
def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
    self.insert(pattern)
    ans = []

    for word in queries:
        node = self

        for ch in word:
            if ch in node.children:
                node = node.children[ch]

            elif ch.islower():
                continue

            else:
                break
        else:
            ans.append(node.is_end)
            continue

        ans.append(False)

    return ans
```

This method processes every query independently.

### Step 1: Insert the Pattern

```python
self.insert(pattern)
```

Build the Trie using the required pattern.

### Step 2: Initialize the Answer

```python
ans = []
```

This list stores the matching result for every query.

### Step 3: Process Every Query

```python
for word in queries:
    node = self
```

For every query, start from the Trie root.

**Important:** We reset `node = self` for every query because each query must be checked independently.

### Step 4: Traverse Each Character

```python
for ch in word:
```

Now we process the query character by character.

There are three possible situations.

#### Case 1: Character Exists in the Trie

```python
if ch in node.children:
    node = node.children[ch]
```

If the character matches the next required pattern character, move to the corresponding child.

For example:

```text
Pattern: FB
Query:   FooBar
```

- `"F"` matches the first Trie child.
- `"o"` does not match `"B"` and is lowercase, so it will be ignored.
- `"B"` matches the next Trie child.

#### Case 2: Character Is Lowercase but Does Not Match

```python
elif ch.islower():
    continue
```

If the character is lowercase and does not match the next required pattern character, ignore it.

For example:

```text
Pattern: FB
Query:   FooBar
```

After matching `"F"`, the next required character is `"B"`.

The characters `"o"`, `"o"`, and `"a"` are lowercase, so they can be skipped.

#### Case 3: Character Is Uppercase but Does Not Match

```python
else:
    break
```

If the character is uppercase and does not match the next required pattern character, the query is invalid.

Why?

Because additional uppercase characters are not allowed.

For example:

```text
Pattern: FB
Query:   FooBarTest
```

After matching `"FB"`, the remaining uppercase `"T"` cannot be ignored.

Therefore, we break out of the loop.

---

## 7. Understanding Python's `for-else`

This is an important Python concept used in your solution.

```python
for ch in word:
    if ch in node.children:
        node = node.children[ch]

    elif ch.islower():
        continue

    else:
        break
else:
    ans.append(node.is_end)
    continue

ans.append(False)
```

Python allows an `else` block with a `for` loop.

**The `else` block executes only when the loop finishes normally, without encountering `break`.**

### Case 1: Loop Completes Successfully

If every character is either:

- Matched in the Trie, or
- An allowed lowercase character,

the loop finishes without `break`.

Then:

```python
else:
    ans.append(node.is_end)
```

We check whether the complete pattern has been matched.

If `node.is_end` is `True`, the query matches.

If it is `False`, some pattern characters are still missing.

### Case 2: Loop Encounters `break`

If an unmatched uppercase character is found:

```python
else:
    break
```

The `for-else` block is skipped.

Execution moves to:

```python
ans.append(False)
```

The query is invalid.

**Interview takeaway:** A `for-else` block runs only if the loop completes without `break`.

---

## 8. Why Do We Check `node.is_end`?

Consider:

```python
pattern = "FB"
query = "Foo"
```

The query starts with `"F"` and contains allowed lowercase characters.

However, the required `"B"` is missing.

After processing the query:

```python
node
```

is still pointing to the `"F"` node.

At that node:

```python
node.is_end = False
```

Therefore:

```python
ans.append(node.is_end)
```

appends `False`.

This ensures that all pattern characters must be matched, not just some of them.

---

## 9. Complete Dry Run

Consider:

```python
queries = [
    "FooBar",
    "FooBarTest",
    "FootBall",
    "FrameBuffer",
    "ForceFeedBack"
]

pattern = "FB"
```

### Step 1: Build the Trie

```text
root
 |
 F
 |
 B  ← is_end = True
```

### Step 2: Process `"FooBar"`

| Character | Action | Current node |
|---|---|---|
| `F` | Match | F |
| `o` | Ignore lowercase | F |
| `o` | Ignore lowercase | F |
| `B` | Match | B |
| `a` | Ignore lowercase | B |
| `r` | Ignore lowercase | B |

The loop finishes without `break`.

```python
node.is_end = True
```

Result: `True`.

### Step 3: Process `"FooBarTest"`

| Character | Action |
|---|---|
| `F` | Match |
| `o` | Ignore |
| `o` | Ignore |
| `B` | Match |
| `a` | Ignore |
| `r` | Ignore |
| `T` | Unmatched uppercase → break |

The loop breaks, so the query is invalid.

Result: `False`.

### Step 4: Process `"FootBall"`

| Character | Action |
|---|---|
| `F` | Match |
| `o` | Ignore |
| `o` | Ignore |
| `t` | Ignore |
| `B` | Match |
| `a` | Ignore |
| `l` | Ignore |
| `l` | Ignore |

The complete pattern is matched.

Result: `True`.

### Step 5: Process `"FrameBuffer"`

| Character | Action |
|---|---|
| `F` | Match |
| `r` | Ignore |
| `a` | Ignore |
| `m` | Ignore |
| `e` | Ignore |
| `B` | Match |
| `u` | Ignore |
| `f` | Ignore |
| `f` | Ignore |
| `e` | Ignore |
| `r` | Ignore |

The complete pattern is matched.

Result: `True`.

### Step 6: Process `"ForceFeedBack"`

| Character | Action |
|---|---|
| `F` | Match |
| `o` | Ignore |
| `r` | Ignore |
| `c` | Ignore |
| `e` | Ignore |
| `F` | Unmatched uppercase → break |

The query contains an extra uppercase character that cannot be ignored.

Result: `False`.

### Final Output

```python
[True, False, True, True, False]
```

---

## 10. Time and Space Complexity

Let:

- `P` = length of the pattern.
- `Q` = number of queries.
- `N` = total number of characters across all queries.

### Building the Trie

Every pattern character is inserted once.

\[
O(P)
\]

### Processing Queries

Each query is traversed character by character.

Across all queries, the total number of processed characters is `N`.

\[
O(N)
\]

### Total Time Complexity

\[
O(P + N)
\]

### Space Complexity

The Trie stores at most `P` character nodes.

The answer list stores one Boolean per query.

\[
O(P + Q)
\]

---

## 11. Common Mistakes

### Mistake 1: Ignoring Every Unmatched Character

Incorrect:

```python
else:
    continue
```

This would allow unmatched uppercase characters, which violates CamelCase matching rules.

Correct:

```python
elif ch.islower():
    continue
else:
    break
```

### Mistake 2: Forgetting to Check `node.is_end`

A query may finish without an invalid uppercase character but still fail to match the complete pattern.

Correct:

```python
ans.append(node.is_end)
```

### Mistake 3: Not Resetting the Trie Node

Incorrect:

```python
for word in queries:
    # Continue from the previous node
```

Correct:

```python
for word in queries:
    node = self
```

Every query must start from the root.

### Mistake 4: Confusing `continue` and `break`

- `continue`: Skip the current character and process the next one.
- `break`: Stop processing the current query because it is invalid.

### Mistake 5: Forgetting Python's `for-else` Behavior

The `else` block runs only when the loop finishes without `break`.

This is why it is useful for distinguishing a successfully processed query from one containing an invalid uppercase character.

---

## 12. Quick Revision Cheat Sheet

| Concept | Remember |
|---|---|
| Trie | Stores the required pattern |
| `insert(pattern)` | Builds the Trie |
| Matching character | Move to the child |
| Unmatched lowercase | Ignore using `continue` |
| Unmatched uppercase | Reject using `break` |
| `node.is_end` | Checks whether the full pattern was matched |
| `for-else` | Executes `else` only if no `break` occurs |
| Time complexity | `O(P + N)` |
| Space complexity | `O(P + Q)` |

## One-Line Pattern

**CamelCase Matching pattern:** Match required characters in order using a Trie, skip unmatched lowercase characters, reject unmatched uppercase characters, and finally check `node.is_end`.