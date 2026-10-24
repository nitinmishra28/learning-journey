# Trie (Prefix Tree) in Python

My notes for learning **Trie data structures in Python**, including implementation, insertion, searching, prefix matching, complexity, and interview problems.

## 1. What Is a Trie?

A **Trie**, also called a **Prefix Tree**, is a tree-based data structure used to store and search strings efficiently.

It is especially useful when multiple words share common prefixes.

Example words:

```python
["cat", "car", "care", "dog"]
```

Conceptual Trie:

```text
                 root
               /      \
              c        d
              |        |
              a        o
             / \       |
            t   r      g
               |
               e
```

The words `cat`, `car`, and `care` share the prefix `"ca"`.

A Trie stores the shared prefix only once in its structure.

**Important:** A Trie is not a binary tree. A node can have multiple children.

## 2. Why Do We Need a Trie?

Suppose we have thousands of words and need to find all words beginning with a given prefix.

For example:

```python
words = ["apple", "application", "app", "bat", "ball"]
prefix = "app"
```

Expected matching words:

```python
["apple", "application", "app"]
```

A simple approach scans every word and checks whether it starts with the prefix.

A Trie stores characters in a tree structure, allowing us to follow the prefix character by character.

This is useful for:

- Prefix searches.
- Autocomplete.
- Dictionary word lookup.
- Word games.
- Contact search.
- Search suggestions.

## 3. Structure of a Trie Node

Each Trie node typically stores:

1. A collection of child nodes.
2. A boolean indicating whether a complete word ends at this node.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```

### Understanding `children`

```python
self.children = {}
```

The dictionary maps each character to its child node.

For example, if a node represents the beginning of `"cat"`:

```python
{
    "a": another_node
}
```

The child node for `"a"` may then contain a child for `"t"`.

### Understanding `is_end`

```python
self.is_end = False
```

This tells us whether the current node marks the end of a complete word.

Consider inserting:

```python
["app", "apple"]
```

The node for the final `"p"` marks the end of `"app"`, even though it also has a child leading to `"apple"`.

Without `is_end`, we could not reliably distinguish complete words from prefixes.

## 4. Complete Trie Implementation

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
```

## 5. Insertion

### Idea

To insert a word:

1. Start at the root.
2. Process each character.
3. If the character does not exist as a child, create a new node.
4. Move to the child node.
5. After processing every character, mark the final node as the end of a word.

### Code

```python
def insert(self, word: str) -> None:
    node = self.root

    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()

        node = node.children[char]

    node.is_end = True
```

### Example

Insert:

```python
trie.insert("cat")
```

The Trie creates the path:

```text
root -> c -> a -> t
```

The final node has:

```python
is_end = True
```

Now `"cat"` exists as a complete word.

## 6. Searching for a Word

### Idea

To search for a complete word:

1. Start from the root.
2. Follow the child corresponding to each character.
3. If a character is missing, return `False`.
4. After processing all characters, return `True` only if the final node marks the end of a word.

### Code

```python
def search(self, word: str) -> bool:
    node = self.root

    for char in word:
        if char not in node.children:
            return False

        node = node.children[char]

    return node.is_end
```

### Example

Suppose the Trie contains:

```python
trie.insert("apple")
```

Then:

```python
trie.search("apple")  # True
trie.search("app")    # False
```

Why is `"app"` false?

The path exists, but `"app"` has not been marked as a complete word.

If we also insert `"app"`:

```python
trie.insert("app")
```

Then:

```python
trie.search("app")  # True
```

## 7. Prefix Search

### Idea

Prefix search checks whether a path exists for the supplied prefix.

Unlike complete-word search, it does not require the final node to have `is_end = True`.

### Code

```python
def startsWith(self, prefix: str) -> bool:
    node = self.root

    for char in prefix:
        if char not in node.children:
            return False

        node = node.children[char]

    return True
```

### Example

```python
trie.insert("apple")

print(trie.startsWith("app"))  # True
print(trie.startsWith("bat"))  # False
```

The prefix `"app"` exists even though `"app"` might not be a complete word in the Trie.

## 8. Understanding the Difference Between `search()` and `startsWith()`

Suppose we inserted:

```python
trie.insert("apple")
```

| Operation | Result | Reason |
|---|---|---|
| `search("apple")` | `True` | Complete word exists |
| `search("app")` | `False` | Prefix exists but is not a complete word |
| `startsWith("app")` | `True` | Prefix path exists |
| `startsWith("bat")` | `False` | Prefix path does not exist |

The key difference is the final return statement.

For complete-word search:

```python
return node.is_end
```

For prefix search:

```python
return True
```

## 9. Dry Run

Insert these words:

```python
["cat", "car", "care"]
```

### Insert `"cat"`

Create:

```text
root
 |
 c
 |
 a
 |
 t*
```

`*` means the node marks the end of a word.

### Insert `"car"`

The path `c -> a` already exists.

Only the missing `r` node needs to be created.

```text
root
 |
 c
 |
 a
 / \
t*  r*
```

### Insert `"care"`

The path `c -> a -> r` already exists.

Create a new `e` node after `r` and mark it as the end of `"care"`.

```text
root
 |
 c
 |
 a
 / \
t*  r*
     |
     e*
```

### Search Results

```python
trie.search("cat")       # True
trie.search("car")       # True
trie.search("care")      # True
trie.search("ca")        # False
trie.startsWith("ca")    # True
trie.startsWith("car")   # True
trie.startsWith("dog")   # False
```

The Trie reuses common prefixes instead of creating separate character paths for every word.

## 10. Time Complexity

Let `L` be the length of the word or prefix being processed.

| Operation | Time Complexity |
|---|---:|
| Insert a word | `O(L)` average |
| Search for a word | `O(L)` average |
| Search for a prefix | `O(L)` average |

Each character is processed once, and dictionary child lookup takes `O(1)` average time.

### Space Complexity

The total space required depends on the number of characters stored across all inserted words.

If the total number of characters across all words is `S`, the Trie uses up to `O(S)` space.

Common prefixes reduce duplicated nodes, so the actual number of nodes may be smaller than `S`.

## 11. Trie vs Hash Map

| Feature | Hash Map | Trie |
|---|---|---|
| Main purpose | Key-value lookup | String and prefix lookup |
| Search | `O(1)` average for a key | `O(L)` for a string of length `L` |
| Prefix search | Usually requires scanning keys | Naturally supported |
| Structure | Hash table | Tree of character nodes |
| Common use | Frequency counting, lookup | Autocomplete, dictionaries, word search |

A hash map is usually the simpler choice for ordinary key-value lookups. A Trie is useful when prefixes are central to the problem.

## 12. Common Trie Variations

### Variation 1: Count Words with a Prefix

Store a counter at each node representing how many inserted words pass through it.

Useful for:

- Prefix frequency.
- Search suggestions.
- Counting words that share a prefix.

### Variation 2: Word Dictionary with Wildcards

Support searching for patterns such as:

```text
c.t
```

where `.` can match any single character.

This typically requires DFS or backtracking over possible children.

### Variation 3: Trie + DFS for Word Search

Use a Trie to store a dictionary of words, then search a grid while following Trie paths.

Useful for problems where many words must be found in a board.

### Variation 4: Bitwise Trie

Instead of characters, store bits of integers.

Useful for:

- Maximum XOR of two numbers.
- XOR queries.
- Bitwise prefix searches.

## 13. Important Interview Problems

### Easy

- Implement Trie (Prefix Tree)
- Longest Common Prefix
- Search Suggestions System

### Medium

- Design Add and Search Words Data Structure
- Replace Words
- Map Sum Pairs
- Implement Magic Dictionary

### Advanced

- Word Search II
- Maximum XOR of Two Numbers in an Array
- Maximum XOR With an Element From Array

## 14. Common Mistakes

1. Forgetting to move to the next node after checking a character.
2. Forgetting to set `node.is_end = True` after insertion.
3. Returning `True` for every complete-word search without checking `is_end`.
4. Requiring `is_end` in a prefix search.
5. Creating a new node even when a character already exists.
6. Confusing a Trie with a binary tree.
7. Assuming Trie space is always smaller than storing the original words; the result depends on shared prefixes and node overhead.

## 15. Revision Cheat Sheet

| Concept | Meaning |
|---|---|
| Trie | Tree-based structure for strings |
| Root | Starting node |
| Children | Character-to-node mapping |
| `is_end` | Marks the end of a complete word |
| Insert | Create missing character nodes |
| Search | Follow the path and check `is_end` |
| Prefix search | Follow the path without requiring `is_end` |
| Insert complexity | `O(L)` |
| Search complexity | `O(L)` |
| Prefix complexity | `O(L)` |
| Space complexity | `O(S)` for `S` total input characters |

> **One-Line Pattern:** Trie = Character-by-Character Tree + Shared Prefixes + `is_end` to Distinguish Complete Words from Prefixes.