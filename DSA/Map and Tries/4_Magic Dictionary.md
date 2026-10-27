# Magic Dictionary — Trie + DFS + Backtracking

## 1. Problem Statement

Design a `MagicDictionary` that supports two operations:

1. `buildDict(dictionary)` — Build a dictionary containing the given words.
2. `search(searchWord)` — Return `True` if the search word matches any dictionary word after modifying **exactly one character**.

This problem is commonly known as **Implement Magic Dictionary (LeetCode 676)**.

### Example

```python
magicDictionary = MagicDictionary()

magicDictionary.buildDict(["hello", "leetcode"])

print(magicDictionary.search("hello"))  # False
print(magicDictionary.search("hhllo"))  # True
print(magicDictionary.search("hell"))   # False
print(magicDictionary.search("leetcoded"))  # False
```

### Why These Results?

- `"hello"` returns `False` because it matches exactly, with zero character changes.
- `"hhllo"` returns `True` because changing the second character from `"h"` to `"e"` produces `"hello"`.
- `"hell"` returns `False` because its length differs from `"hello"`.
- `"leetcoded"` returns `False` because its length differs from `"leetcode"`.

**Important:** Exactly one character must be different. Zero changes or two or more changes are not allowed.

---

## 2. Approach: Trie + DFS

We use a Trie to store the dictionary words and DFS to search for a match.

The main idea is to track whether we have already changed a character.

We use a Boolean variable:

```python
changed = False
```

- `False`: We have not changed any character yet.
- `True`: We have already changed exactly one character.

### Search Strategy

For every character in `searchWord`:

1. If the same character exists in the Trie, follow that path without changing anything.
2. If we have not changed a character yet, try every different character available at the current node.
3. Once we choose a different character, set `changed = True`.
4. Continue searching the remaining characters.
5. At the end, return `True` only if a complete dictionary word exists and `changed` is `True`.

This ensures that exactly one character is modified.

---

## 3. Complete Python Code

```python
class MagicDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def buildDict(self, dictionary: list[str]) -> None:
        for word in dictionary:
            node = self

            for char in word:
                if char not in node.children:
                    node.children[char] = MagicDictionary()

                node = node.children[char]

            node.is_end = True

    def search(self, searchWord: str) -> bool:

        def dfs(node, i, changed):
            if i == len(searchWord):
                return node.is_end and changed

            char = searchWord[i]

            # Option 1: Match the same character
            if char in node.children:
                if dfs(node.children[char], i + 1, changed):
                    return True

            # Option 2: Change one character
            if not changed:
                for ch, child in node.children.items():
                    if ch != char:
                        if dfs(child, i + 1, True):
                            return True

            return False

        return dfs(self, 0, False)
```

---

## 4. Understanding the Trie Structure

Every `MagicDictionary` object represents a Trie node.

```python
def __init__(self):
    self.children = {}
    self.is_end = False
```

### `children`

Stores child nodes using a dictionary.

For example:

```python
{
    "h": MagicDictionary(),
    "l": MagicDictionary()
}
```

The keys represent characters, and the values represent child nodes.

### `is_end`

Indicates whether a complete dictionary word ends at the current node.

For example, after inserting `"hello"`, the node corresponding to the final `"o"` has:

```python
is_end = True
```

This is necessary because a character path alone does not guarantee that a complete word exists.

---

## 5. Understanding `buildDict(dictionary)`

### Code

```python
def buildDict(self, dictionary: list[str]) -> None:
    for word in dictionary:
        node = self

        for char in word:
            if char not in node.children:
                node.children[char] = MagicDictionary()

            node = node.children[char]

        node.is_end = True
```

### Step-by-Step Explanation

**Step 1: Process each dictionary word**

```python
for word in dictionary:
```

For example:

```python
["hello", "leetcode"]
```

Each word is inserted separately.

**Step 2: Start at the root**

```python
node = self
```

**Step 3: Process each character**

```python
for char in word:
```

For `"hello"`:

```text
h → e → l → l → o
```

**Step 4: Create a missing node**

```python
if char not in node.children:
    node.children[char] = MagicDictionary()
```

If the character already exists, reuse its node. This allows words to share common prefixes.

**Step 5: Move to the child**

```python
node = node.children[char]
```

**Step 6: Mark the complete word**

```python
node.is_end = True
```

### Complexity

Let `S` be the total number of characters across all dictionary words.

- Time: `O(S)` average.
- Space: `O(S)` in the worst case.

---

## 6. Understanding `search(searchWord)`

### Code

```python
def search(self, searchWord: str) -> bool:

    def dfs(node, i, changed):
        if i == len(searchWord):
            return node.is_end and changed

        char = searchWord[i]

        if char in node.children:
            if dfs(node.children[char], i + 1, changed):
                return True

        if not changed:
            for ch, child in node.children.items():
                if ch != char:
                    if dfs(child, i + 1, True):
                        return True

        return False

    return dfs(self, 0, False)
```

The nested `dfs()` function receives three parameters:

| Parameter | Meaning |
|---|---|
| `node` | Current Trie node |
| `i` | Current index in `searchWord` |
| `changed` | Whether one character has already been changed |

The algorithm explores possible paths while keeping track of the number of character changes.

---

## 7. Understanding the DFS Logic

### Case 1: Base Case

```python
if i == len(searchWord):
    return node.is_end and changed
```

This is the most important condition.

When `i` reaches the length of `searchWord`, every character has been processed.

We return `True` only if:

1. `node.is_end` is `True`, meaning a complete dictionary word exists.
2. `changed` is `True`, meaning exactly one character was changed.

Consider searching `"hello"` when `"hello"` is in the dictionary.

The path exists, but no character was changed.

```python
node.is_end = True
changed = False
```

Therefore:

```python
True and False  # False
```

The exact match is rejected.

Now consider `"hhllo"`.

It can match `"hello"` after changing one character, so:

```python
node.is_end = True
changed = True
```

The result is:

```python
True and True  # True
```

### Case 2: Get the Current Character

```python
char = searchWord[i]
```

For `"hhllo"`:

```text
i = 0 → h
i = 1 → h
i = 2 → l
i = 3 → l
i = 4 → o
```

At each position, we decide whether to keep the character or change it.

### Case 3: Follow the Same Character

```python
if char in node.children:
    if dfs(node.children[char], i + 1, changed):
        return True
```

If the current character exists in the Trie, we can follow it without using our character change.

Notice that `changed` remains unchanged.

For example, when searching `"hhllo"` against `"hello"`, the first `"h"` matches normally.

At the second position, however, the search character is `"h"` while the dictionary word requires `"e"`.

The algorithm must consider changing that character.

### Case 4: Try Changing One Character

```python
if not changed:
    for ch, child in node.children.items():
        if ch != char:
            if dfs(child, i + 1, True):
                return True
```

This is the key logic.

**Step 1: Allow a change only if one has not happened yet**

```python
if not changed:
```

Once a character has been changed, this block is skipped for the remaining characters.

**Step 2: Explore all possible child characters**

```python
for ch, child in node.children.items():
```

Each `ch` is a character available at the current Trie node.

**Step 3: Ignore the same character**

```python
if ch != char:
```

We only want to count an actual substitution as a change.

**Step 4: Continue with the changed character**

```python
dfs(child, i + 1, True)
```

The search moves to the selected child and sets `changed = True`.

This records that the one allowed character change has been used.

### Case 5: No Path Matches

```python
return False
```

If neither the unchanged character path nor any permitted changed-character path succeeds, the search returns `False`.

---

## 8. Dry Run: `search("hhllo")`

Suppose we have built the dictionary:

```python
dictionary = ["hello"]
```

We search:

```python
search("hhllo")
```

The stored word is `"hello"`, and the search word is `"hhllo"`.

Compare the characters:

| Index | Search word | Dictionary word | Action |
|---|---|---|---|
| 0 | `h` | `h` | Match normally |
| 1 | `h` | `e` | Change `h` to `e` |
| 2 | `l` | `l` | Match normally |
| 3 | `l` | `l` | Match normally |
| 4 | `o` | `o` | Match normally |

### Step 1: First Character

```python
dfs(root, 0, False)
```

The current character is `"h"`.

The `"h"` child exists, so follow it:

```python
dfs(h_node, 1, False)
```

### Step 2: Second Character

The current search character is `"h"`.

But the dictionary path for `"hello"` requires `"e"`.

At this node, the child `"e"` exists.

The unchanged path for `"h"` is unavailable, so the algorithm considers changing the character.

```python
if not changed:
```

Since `changed` is `False`, the algorithm can choose a different child:

```python
ch = "e"
ch != "h"  # True
```

It follows `"e"` and calls:

```python
dfs(e_node, 2, True)
```

Now the change has been used.

### Step 3: Remaining Characters

The remaining characters match:

```text
l → l → o
```

The algorithm follows the matching path without changing anything else.

### Step 4: Reach the End

At the end:

```python
i == len("hhllo")
```

The final node represents `"hello"`:

```python
node.is_end = True
changed = True
```

Therefore:

```python
return True and True
```

**Final result: `True`.**

---

## 9. Dry Run: Why `search("hello")` Returns False

Suppose `"hello"` is in the dictionary.

We search for the exact same word:

```python
search("hello")
```

Every character follows the matching path.

No character is changed, so:

```python
changed = False
```

At the end:

```python
return node.is_end and changed
```

Becomes:

```python
True and False
```

The result is:

```python
False
```

This confirms that the problem requires exactly one character to differ.

---

## 10. Dry Run: Why Two Changes Are Not Allowed

Suppose the dictionary contains:

```python
["hello"]
```

Search:

```python
search("hhxlo")
```

Comparison:

```text
Search:     h h x l o
Dictionary: h e l l o
              ↑ ↑
```

Two positions differ.

The algorithm may change the second character from `"h"` to `"e"`, setting:

```python
changed = True
```

At the next differing position, `"x"` cannot follow the required `"l"` path.

Because `changed` is already `True`, the algorithm cannot substitute `"x"` with another character.

The search returns:

```python
False
```

**Key idea:** `changed` ensures that at most one character is changed, and the base case ensures that at least one character is changed.

Together, they enforce exactly one change.

---

## 11. Why Do We Need DFS and Backtracking?

When a character does not match, several different characters may be available in the Trie.

For example, the current node might contain:

```python
{
    "a": child_a,
    "e": child_e,
    "i": child_i
}
```

If the search character is `"o"`, any of these children could represent the one allowed substitution.

DFS explores each possible path.

If a path succeeds, the algorithm returns `True`.

If it fails, the algorithm returns to the previous call and tries another child.

This process is commonly described as **backtracking**: explore a possible choice, continue recursively, and try another choice if needed.

In this implementation, we do not manually restore `changed` because it is passed as a Boolean argument to each recursive call. Each branch has its own value.

---

## 12. Time and Space Complexity

Let:

- `S` = total number of characters across all dictionary words.
- `M` = length of `searchWord`.
- `B` = maximum number of children a Trie node can have.

### Building the Dictionary

Every dictionary character is processed once.

- Time: `O(S)` average.
- Space: `O(S)` in the worst case.

### Searching Without Character Substitution

If the search follows only one path, it processes at most `M` characters.

- Time: `O(M)` average.
- Recursive stack space: `O(M)`.

### Searching With Substitution

At a position where a character is changed, DFS explores other child characters.

Because `changed` becomes `True` after one substitution, further branching for substitutions is not permitted. However, before the change occurs, the algorithm can explore several possible paths while matching the earlier characters.

A general upper bound is:

\[
O(B^M)
\]

This is a loose worst-case bound for a Trie with branching factor `B`. The actual work depends on the paths present in the Trie and the location of the possible substitution.

- Recursive stack space: `O(M)`.
- Additional search space: `O(M)` for the recursion stack, excluding the Trie already stored.

---

## 13. Common Mistakes

### Mistake 1: Accepting an Exact Match

Incorrect:

```python
if i == len(searchWord):
    return node.is_end
```

This accepts words that match without any changes.

Correct:

```python
if i == len(searchWord):
    return node.is_end and changed
```

### Mistake 2: Allowing More Than One Change

Incorrect logic would allow substitutions even when `changed` is already `True`.

Correct:

```python
if not changed:
```

This allows the substitution branch only once along each path.

### Mistake 3: Setting `changed = True` for Matching Characters

Matching the current character does not count as a modification.

Correct:

```python
dfs(node.children[char], i + 1, changed)
```

The existing value of `changed` is preserved.

### Mistake 4: Changing to the Same Character

Incorrect:

```python
for ch, child in node.children.items():
    if dfs(child, i + 1, True):
        return True
```

This could count an unchanged character as a substitution.

Correct:

```python
if ch != char:
```

A change must substitute one character with a different character.

### Mistake 5: Forgetting to Check `is_end`

A matching character path is not enough. The path must represent a complete dictionary word.

Correct:

```python
return node.is_end and changed
```

---

## 14. Quick Revision Cheat Sheet

| Concept | Remember |
|---|---|
| Trie | Stores dictionary words character by character |
| `buildDict()` | Inserts every word into the Trie |
| `search()` | Uses DFS to explore possible matches |
| `changed = False` | No substitution used yet |
| `changed = True` | One substitution already used |
| Matching character | Follow the child without changing the flag |
| Different character | Allowed only when `changed` is `False` |
| Base case | Return `node.is_end and changed` |
| Exact match | Returns `False` |
| Exactly one substitution | Returns `True` if a dictionary word matches |
| Different lengths | Cannot match because every search character must follow one Trie edge |

## One-Line Pattern

**Trie + DFS + Backtracking:** Follow matching characters normally; allow one different child exactly once, and accept only if the path ends at a complete dictionary word.