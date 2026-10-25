# Trie - Insert, Search, Prefix Search, Autocomplete, and Longest Common Prefix

## 1. What Is a Trie?

A **Trie**, also called a **Prefix Tree**, is a tree-like data structure used to store strings character by character.

It is useful for:
- Inserting words.
- Searching for complete words.
- Checking whether a prefix exists.
- Finding autocomplete suggestions.
- Solving longest common prefix problems.
- Implementing dictionaries and search suggestions.

### Example

If we insert `"cat"`, `"car"`, and `"care"`, the Trie shares the common prefix `"ca"`.

```text
root
 |
 c
 |
 a
 / \
t   r
    |
    e
```

Each node stores its child nodes and whether a complete word ends there.

---

## 2. Trie Node Structure

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```

### `children`

```python
self.children = {}
```

A dictionary that stores child nodes.

- Key: character.
- Value: TrieNode object.

For example:

```python
{
    "a": TrieNode(),
    "b": TrieNode()
}
```

### `is_end`

```python
self.is_end = False
```

Indicates whether a complete word ends at the current node.

For example, if `"app"` and `"apple"` are inserted, the node for the second `"p"` has `is_end = True`, and the path continues toward `"apple"`.

**Important:** A prefix can exist without being a complete word.

---

## 3. Operation 1: Insert a Word

### Code

```python
def insert(self, word: str) -> None:
    node = self

    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()

        node = node.children[char]

    node.is_end = True
```

### Explanation

1. Start from the root.
2. Traverse every character in the word.
3. Create a new node if the character does not exist.
4. Move to the corresponding child node.
5. Mark the final node as the end of a word.

### Dry Run

Insert `"cat"`.

```text
root → c → a → t
                 |
            is_end = True
```

If we insert `"car"` afterward, the nodes for `"c"` and `"a"` are reused.

### Complexity

- Time: `O(L)`, where `L` is the word length.
- Additional space: `O(L)` in the worst case for a single insertion.

---

## 4. Operation 2: Search a Complete Word

### Code

```python
def search(self, word: str) -> bool:
    node = self

    for char in word:
        if char not in node.children:
            return False

        node = node.children[char]

    return node.is_end
```

### Explanation

The method traverses each character.

- If a character is missing, return `False`.
- If all characters exist, check `node.is_end`.

### Example

Suppose only `"apple"` has been inserted.

```python
search("apple")  # True
search("app")    # False
search("bat")    # False
```

`"app"` is a valid prefix, but it is not a complete word unless it has also been inserted.

### Complexity

- Time: `O(L)`.
- Auxiliary space: `O(1)`.

---

## 5. Operation 3: Check Whether a Prefix Exists

### Code

```python
def startsWith(self, prefix: str) -> bool:
    node = self

    for char in prefix:
        if char not in node.children:
            return False

        node = node.children[char]

    return True
```

### Explanation

This operation checks only whether the prefix path exists.

Unlike `search()`, it does not check `node.is_end`.

### Example

If `"apple"` has been inserted:

```python
startsWith("app")   # True
startsWith("apple") # True
startsWith("bat")   # False
```

### Complexity

- Time: `O(L)`, where `L` is the prefix length.
- Auxiliary space: `O(1)`.

---

## 6. Operation 4: Autocomplete

### Problem Statement

Given a prefix, return all words stored in the Trie that start with that prefix.

### Example

Suppose the Trie contains:

```python
["apple", "app", "application", "apt", "bat"]
```

Input:

```python
prefix = "app"
```

Output:

```python
["app", "apple", "application"]
```

The order of suggestions depends on the order in which children are traversed.

### Code

The following method assumes the Trie has a separate root node accessible as `self.root`.

```python
def autocomplete(self, prefix: str):
    node = self.root

    for char in prefix:
        if char not in node.children:
            return []

        node = node.children[char]

    suggestions = []

    def collect(node, current_word):
        if node.is_end:
            suggestions.append(current_word)

        for char, child in node.children.items():
            collect(child, current_word + char)

    collect(node, prefix)

    return suggestions
```

**Important:** In this code, `self.root` must exist. If `autocomplete()` is implemented directly inside a `TrieNode` object, use `node = self` instead of `node = self.root`.

### Understanding the Logic

The autocomplete operation has two main stages.

#### Stage 1: Find the Prefix Node

```python
node = self.root

for char in prefix:
    if char not in node.children:
        return []

    node = node.children[char]
```

Suppose the prefix is `"app"`.

The traversal follows:

```text
root → a → p → p
```

If any character is missing, no stored word can match the prefix, so return an empty list.

Once traversal finishes, `node` points to the final character of the prefix.

#### Stage 2: Collect All Words Below That Node

```python
suggestions = []
```

This list stores all matching words.

The nested function explores the subtree rooted at the prefix node.

```python
def collect(node, current_word):
    if node.is_end:
        suggestions.append(current_word)

    for char, child in node.children.items():
        collect(child, current_word + char)
```

There are two important operations.

**1. Check whether a complete word ends here**

```python
if node.is_end:
    suggestions.append(current_word)
```

If `node.is_end` is `True`, the current string is a complete word, so add it to the suggestions.

**2. Explore every child**

```python
for char, child in node.children.items():
    collect(child, current_word + char)
```

For every child:
- Add the child's character to the current word.
- Recursively explore the child's subtree.

Finally:

```python
collect(node, prefix)
return suggestions
```

Start collecting words from the prefix node, using the prefix itself as the initial word.

### Dry Run

Suppose the Trie contains:

```python
["app", "apple", "application", "apt", "bat"]
```

Call:

```python
autocomplete("app")
```

First, locate the `"app"` node.

```text
root → a → p → p
```

Now explore its subtree:

```text
app                 ← is_end = True
 |
 l
 |
 e                   ← is_end = True
 |
 ...
 |
 application         ← is_end = True
```

The traversal also visits every other descendant of `"app"`.

The result is:

```python
["app", "apple", "application"]
```

The `"apt"` word is not included because it branches away from the `"app"` node. `"bat"` is not included because its path starts with a different character.

### Why Is `current_word` Passed Recursively?

```python
collect(child, current_word + char)
```

Each recursive call builds the word character by character.

For example:

```text
"app" → "appl" → "apple"
```

This lets the algorithm reconstruct complete words without storing the entire word separately in every Trie node.

### Complexity

Let:
- `P` = length of the prefix.
- `V` = number of Trie nodes visited while collecting suggestions.
- `K` = number of returned words.

**Time complexity:**

- Finding the prefix node: `O(P)`.
- Collecting all matching words: proportional to the subtree explored, plus the cost of constructing strings.

A simple upper bound is `O(P + V × M)`, where `M` is the maximum length of a returned word, because string concatenation can copy characters.

**Auxiliary space:**

- Recursive traversal stack: up to the height of the Trie, `O(M)` beyond the stored results.
- Suggestions list: depends on the number and total length of returned words.

### When Is Autocomplete Useful?

- Search engine suggestions.
- IDE code completion.
- Contact search.
- Product search.
- Dictionary applications.

---

## 7. Operation 5: Longest Common Prefix Using Trie

### Problem Statement

Given a list of strings, find the longest prefix shared by all strings.

### Example

```python
strs = ["flower", "flow", "flight"]
```

Output:

```python
"fl"
```

### Code

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self

        for char in word:
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

### Explanation

1. Insert all strings into the Trie.
2. Start at the root.
3. Continue while the current node has exactly one child.
4. Stop if the current node marks the end of a word.
5. Return the characters collected along the path.

### Why Check `len(node.children) == 1`?

If the current node has exactly one child, all strings that reach it continue through the same character.

If it has multiple children, the strings branch into different paths, so the common prefix ends.

### Why Check `not node.is_end`?

Consider:

```python
strs = ["app", "apple", "application"]
```

The longest common prefix is `"app"`.

The node for the final `"p"` is marked as the end of `"app"`. Even if it has one child, we must stop because one word has already ended.

### Complexity

Let `S` be the total number of characters across all strings.

- Time: `O(S)` to build the Trie, followed by at most `O(M)` for traversal, where `M` is the maximum word length.
- Space: `O(S)` in the worst case.

---

## 8. Complete Trie Class With Autocomplete

Here is a reusable implementation that supports insertion, complete-word search, prefix search, and autocomplete.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        return True

    def autocomplete(self, prefix: str) -> list[str]:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return []

            node = node.children[char]

        suggestions = []

        def collect(current_node, current_word):
            if current_node.is_end:
                suggestions.append(current_word)

            for char, child in current_node.children.items():
                collect(child, current_word + char)

        collect(node, prefix)

        return suggestions
```

### Usage

```python
trie = Trie()

trie.insert("apple")
trie.insert("app")
trie.insert("application")
trie.insert("apt")
trie.insert("bat")

print(trie.search("apple"))
# True

print(trie.search("ap"))
# False

print(trie.startsWith("ap"))
# True

print(trie.autocomplete("app"))
# ['app', 'apple', 'application']
```

The exact order of autocomplete results depends on the insertion order of the child characters.

---

## 9. Common Mistakes

### Mistake 1: Confusing Prefix Search With Complete-Word Search

- `search()` checks `node.is_end`.
- `startsWith()` only checks whether the path exists.

### Mistake 2: Forgetting to Mark the End of a Word

```python
node.is_end = True
```

Without this, complete-word searches and autocomplete collection will miss inserted words.

### Mistake 3: Starting Autocomplete From the Root Instead of the Prefix Node

After locating the prefix, collect words from that node rather than traversing the entire Trie.

### Mistake 4: Forgetting the Prefix in `current_word`

Correct:

```python
collect(node, prefix)
```

Passing an empty string would cause the collected words to omit the requested prefix.

### Mistake 5: Forgetting That a Prefix Can Be a Complete Word

If `"app"` and `"apple"` are both inserted, autocomplete for `"app"` should include `"app"` as well as `"apple"`.

That is why `collect()` checks `node.is_end` before visiting the children.

### Mistake 6: Assuming Autocomplete Returns a Fixed Number of Suggestions

This implementation returns **all** words matching the prefix. Returning only the top `k` suggestions would require additional logic.

---

## 10. Quick Revision Cheat Sheet

| Operation | Core idea | Time complexity |
|---|---|---|
| `insert(word)` | Create missing nodes and mark the final node | `O(L)` average |
| `search(word)` | Traverse and check `is_end` | `O(L)` average |
| `startsWith(prefix)` | Check whether the prefix path exists | `O(P)` average |
| `autocomplete(prefix)` | Find the prefix node and collect descendant words | Depends on subtree size and output |
| `longestCommonPrefix(strs)` | Follow the single-child path until a branch or word end | `O(S)` |

Where:
- `L` = word length.
- `P` = prefix length.
- `S` = total characters across inserted strings.

## One-Line Patterns

- **Insert:** Create missing character nodes and mark the last node.
- **Search:** Traverse the word and check `is_end`.
- **Prefix search:** Traverse the prefix without checking `is_end`.
- **Autocomplete:** Find the prefix node, then use DFS to collect all complete words below it.
- **Longest common prefix:** Follow single-child nodes until a branching node or the end of a word.