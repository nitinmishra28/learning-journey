# Longest Common Prefix Using Trie

## 1. Problem Statement

Given a list of strings `strs`, find the **longest common prefix** shared by all strings.

If no common prefix exists, return an empty string `""`.

### Example 1

**Input:**
```python
strs = ["flower", "flow", "flight"]
```

**Output:**
```python
"fl"
```

**Explanation:**

- `"flower"` starts with `"fl"`.
- `"flow"` starts with `"fl"`.
- `"flight"` starts with `"fl"`.

The longest common prefix is `"fl"`.

### Example 2

**Input:**
```python
strs = ["dog", "racecar", "car"]
```

**Output:**
```python
""
```

**Explanation:** The strings do not share a common prefix.

### Example 3

**Input:**
```python
strs = ["apple", "app", "application"]
```

**Output:**
```python
"app"
```

---

## 2. Approach: Trie

A **Trie (Prefix Tree)** stores strings character by character.

Our strategy is:

1. Insert every string into the Trie.
2. Start traversing from the root.
3. Continue while the current node has exactly one child and is not the end of a word.
4. Add that child's character to the prefix.
5. Stop when a node has multiple children or marks the end of a word.

The characters traversed before stopping form the longest common prefix.

### Why Does This Work?

The common prefix must follow a single path in the Trie.

- **Exactly one child:** All inserted strings that reach this node continue through the same character.
- **Multiple children:** The strings branch into different characters, so the common prefix ends.
- **`is_end = True`:** At least one inserted word ends here. The prefix cannot extend beyond the end of that word.

---

## 3. Complete Python Code

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, strs):
        node = self

        for char in strs:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        root = TrieNode()

        for word in strs:
            root.insert(word)

        node = root
        prefix = ""

        while len(node.children) == 1 and not node.is_end:
            for char in node.children:
                prefix += char
                node = node.children[char]

        return prefix
```

---

## 4. Understanding the Code

### Part 1: Trie Node

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```

Each node contains:

- `children`: A dictionary mapping characters to child nodes.
- `is_end`: Indicates whether a complete word ends at this node.

For example, a node with the character `"a"` may have `"p"` as its child.

### Part 2: Insert a Word

```python
def insert(self, strs):
    node = self

    for char in strs:
        if char not in node.children:
            node.children[char] = TrieNode()

        node = node.children[char]

    node.is_end = True
```

Suppose we insert `"cat"`.

```text
root
  |
  c
  |
  a
  |
  t  ← is_end = True
```

Each character becomes a node in the Trie. If a node already exists, we reuse it instead of creating a duplicate.

### Part 3: Handle Empty Input

```python
if not strs:
    return ""
```

If the input list is empty, there is no common prefix to return.

### Part 4: Build the Trie

```python
root = TrieNode()

for word in strs:
    root.insert(word)
```

Insert every word into the Trie. Common prefixes share the same nodes.

### Part 5: Initialize Traversal

```python
node = root
prefix = ""
```

- `node` tracks our current position in the Trie.
- `prefix` stores the characters in the longest common prefix.

### Part 6: Traverse the Common Path

```python
while len(node.children) == 1 and not node.is_end:
```

This is the **most important condition** in the solution.

The loop continues only when:

1. The current node has exactly one child.
2. The current node is not the end of a word.

If either condition fails, traversal stops.

### Part 7: Add the Character and Move Forward

```python
for char in node.children:
    prefix += char
    node = node.children[char]
```

Because the current node has exactly one child, its `children` dictionary contains only one character.

We add that character to `prefix` and move to its child node.

**Why use a `for` loop?**

A dictionary can contain multiple keys, but the `while` condition guarantees exactly one child here. Therefore, the loop runs only once per iteration.

---

## 5. Dry Run

Consider:

```python
strs = ["flower", "flow", "flight"]
```

After inserting all words, the relevant Trie structure is:

```text
root
  |
  f
  |
  l
 / \
o   i
```

The `"o"` branch continues toward `"flower"` and `"flow"`, while the `"i"` branch continues toward `"flight"`.

### Step 1: Start at the Root

```python
node = root
prefix = ""
```

The root has exactly one child: `"f"`.

Condition:

```python
len(node.children) == 1  # True
node.is_end              # False
```

Add `"f"`.

```python
prefix = "f"
```

### Step 2: Move to the `"f"` Node

The `"f"` node has exactly one child: `"l"`.

The condition is still true.

Add `"l"`.

```python
prefix = "fl"
```

### Step 3: Move to the `"l"` Node

The `"l"` node has two children: `"o"` and `"i"`.

```python
len(node.children) == 1  # False
```

The loop stops because the strings branch into different paths.

### Final Result

```python
return "fl"
```

The longest common prefix is `"fl"`.

---

## 6. Why Check `not node.is_end`?

Consider:

```python
strs = ["app", "apple", "application"]
```

The Trie contains the path:

```text
root → a → p → p → l → ...
```

At the second `"p"` node:

```python
node.is_end = True
```

This is because `"app"` ends there.

Even though the node has only one child (`"l"`), we must stop. Otherwise, we might incorrectly return `"appl"`.

Therefore, this condition matters:

```python
while len(node.children) == 1 and not node.is_end:
```

It ensures that the prefix cannot extend beyond the end of the shortest matching word.

---

## 7. Edge Cases

| Input | Output | Reason |
|---|---|---|
| `[]` | `""` | Empty list |
| `["apple"]` | `"apple"` | Only one word |
| `["dog", "racecar"]` | `""` | Different first characters |
| `["app", "apple"]` | `"app"` | One word ends at the common prefix |
| `["flower", "flow", "flight"]` | `"fl"` | Characters branch after `"fl"` |
| `["abc", "abc", "abc"]` | `"abc"` | All strings are identical |

---

## 8. Time and Space Complexity

Let:

- `N` = number of strings.
- `M` = length of the longest string.
- `S` = total number of characters across all strings.

### Time Complexity

**Building the Trie:**

Every character is processed once during insertion.

\[
O(S)
\]

**Traversing the Trie:**

The prefix traversal visits at most `M` nodes.

\[
O(M)
\]

**Total:**

\[
O(S + M) = O(S)
\]

Since `M` is at most `S` for a non-empty input.

### Space Complexity

In the worst case, the Trie stores nodes for all distinct character prefixes, bounded by the total number of characters.

\[
O(S)
\]

---

## 9. Common Mistakes

### Mistake 1: Checking Only the Number of Children

Incorrect:

```python
while len(node.children) == 1:
```

This may continue past the end of a shorter word.

Correct:

```python
while len(node.children) == 1 and not node.is_end:
```

### Mistake 2: Forgetting to Update the Node

Incorrect:

```python
prefix += char
```

Without moving to the child node, the traversal cannot progress.

Correct:

```python
prefix += char
node = node.children[char]
```

### Mistake 3: Forgetting the Empty Input Check

Without checking `if not strs`, the solution may not handle an empty list correctly.

### Mistake 4: Thinking a Trie Is Always the Best Approach

A Trie is useful for understanding prefix trees and becomes valuable when multiple prefix operations are needed.

For a single longest-common-prefix problem, sorting or direct character-by-character comparison may be simpler.

---

## 10. Alternative: Character-by-Character Comparison

A Trie is not necessary for every longest common prefix problem.

```python
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix
```

This approach starts with the first word as the candidate prefix and repeatedly shortens it until each word starts with that prefix.

Its worst-case time complexity is generally `O(S)` for this implementation under typical string-operation costs, and its auxiliary space is `O(M)` for prefix slicing.

**Interview tip:** Know the Trie solution, but also understand the simpler approach. Choose based on the problem constraints and whether the Trie will be reused for additional prefix queries.

---

## 11. Quick Revision Cheat Sheet

| Concept | Remember |
|---|---|
| Trie | Stores strings character by character |
| `children` | Dictionary of child nodes |
| `is_end` | Marks the end of a complete word |
| Build Trie | Insert every string |
| Single child | Common path continues |
| Multiple children | Strings branch; stop |
| `is_end = True` | A word ends here; stop |
| Time complexity | `O(S)` |
| Space complexity | `O(S)` |

## One-Line Pattern

**Longest Common Prefix using Trie:** Build the Trie, then follow the single-child path until a branching node or the end of a word is reached.